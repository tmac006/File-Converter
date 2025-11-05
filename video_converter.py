import os
import sys
import subprocess

try:
    import imageio_ffmpeg
except ImportError:
    imageio_ffmpeg = None


# Supported video formats
SUPPORTED_FORMATS = {
    'mp4': ['mp4'],
    'avi': ['avi'],
    'mov': ['mov'],
    'mkv': ['mkv'],
    'webm': ['webm'],
    'flv': ['flv'],
    'wmv': ['wmv'],
    'm4v': ['m4v'],
    '3gp': ['3gp'],
    'ogv': ['ogv'],
}


def get_ffmpeg_path() -> str:
    """Get the path to ffmpeg executable (bundled or system)."""
    if imageio_ffmpeg is None:
        raise RuntimeError(
            "imageio-ffmpeg is not installed. Please install it with: pip install imageio-ffmpeg"
        )
    # Get bundled ffmpeg path (will download automatically on first use)
    return imageio_ffmpeg.get_ffmpeg_exe()


def get_format_from_extension(extension: str) -> str | None:
    """Get the format name from a file extension."""
    extension = extension.lower().lstrip('.')
    for format_name, extensions in SUPPORTED_FORMATS.items():
        if extension in extensions:
            return format_name
    return None


def convert_video(input_path: str, output_path: str | None = None, output_format: str | None = None, 
                  quality: str = 'medium', codec: str | None = None) -> str:
    """Convert an input video to a specified format using ffmpeg.
    
    Args:
        input_path: Path to the input video file
        output_path: Path for the output file (optional, auto-generated if not provided)
        output_format: Output format (mp4, avi, mov, mkv, webm, etc.). If None, inferred from output_path extension
        quality: Video quality preset ('low', 'medium', 'high', 'copy'). Default: 'medium'
        codec: Video codec (h264, h265, vp9, etc.). If None, uses default for format
    
    Returns:
        The output path on success.
    """
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Determine output format
    if output_format is None:
        if output_path:
            ext = os.path.splitext(output_path)[1]
            output_format = get_format_from_extension(ext)
        if output_format is None:
            raise ValueError(f"Could not determine output format from extension. Please specify output_format.")
    
    output_format = output_format.lower()
    
    # Validate output format
    if output_format not in SUPPORTED_FORMATS:
        raise ValueError(f"Unsupported output format: {output_format}. Supported formats: {', '.join(SUPPORTED_FORMATS.keys())}")
    
    # Generate output path if not provided
    if output_path is None or output_path.strip() == "":
        default_ext = SUPPORTED_FORMATS[output_format][0]
        output_path = os.path.splitext(input_path)[0] + f".{default_ext}"
    
    # Ensure parent directory exists
    out_dir = os.path.dirname(output_path)
    if out_dir and not os.path.isdir(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    
    # Get bundled ffmpeg executable path
    ffmpeg_exe = get_ffmpeg_path()
    
    # Build ffmpeg command
    cmd = [ffmpeg_exe, '-i', input_path, '-y']  # -y to overwrite output file
    
    # Set codec if specified, otherwise use defaults
    if codec:
        if codec.lower() in ['h264', 'libx264']:
            cmd.extend(['-c:v', 'libx264'])
        elif codec.lower() in ['h265', 'hevc', 'libx265']:
            cmd.extend(['-c:v', 'libx265'])
        elif codec.lower() == 'vp9':
            cmd.extend(['-c:v', 'libvpx-vp9'])
        elif codec.lower() == 'vp8':
            cmd.extend(['-c:v', 'libvpx'])
        else:
            cmd.extend(['-c:v', codec])
    else:
        # Default codecs for common formats
        if output_format == 'mp4':
            cmd.extend(['-c:v', 'libx264'])
        elif output_format == 'webm':
            cmd.extend(['-c:v', 'libvpx-vp9'])
        elif output_format == 'mkv':
            cmd.extend(['-c:v', 'libx264'])
    
    # Set quality preset
    if quality == 'copy':
        cmd.extend(['-c:v', 'copy', '-c:a', 'copy'])
    elif quality == 'low':
        cmd.extend(['-crf', '28', '-preset', 'fast'])
    elif quality == 'medium':
        cmd.extend(['-crf', '23', '-preset', 'medium'])
    elif quality == 'high':
        cmd.extend(['-crf', '18', '-preset', 'slow'])
    else:
        cmd.extend(['-crf', '23', '-preset', 'medium'])
    
    # Set audio codec
    if quality != 'copy':
        cmd.extend(['-c:a', 'aac'])
    
    cmd.append(output_path)
    
    # Run ffmpeg
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return output_path
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr if e.stderr else str(e)
        raise RuntimeError(f"ffmpeg conversion failed: {error_msg}")


def list_supported_formats() -> list[str]:
    """Return a list of supported output formats."""
    return list(SUPPORTED_FORMATS.keys())


def main() -> None:
    """Interactive CLI for video conversion."""
    try:
        # Check if imageio-ffmpeg is available (will auto-download ffmpeg on first use)
        try:
            get_ffmpeg_path()
        except RuntimeError as e:
            print(f"Error: {e}")
            print("\nPlease install imageio-ffmpeg:")
            print("  pip install imageio-ffmpeg")
            sys.exit(1)
        
        print("=== Video Converter ===\n")
        print("Note: ffmpeg will be automatically downloaded on first use if needed.\n")
        print("Supported output formats:")
        for i, fmt in enumerate(list_supported_formats(), 1):
            print(f"  {i}) {fmt.upper()}")
        
        # Get output format
        format_choice = input("\nEnter output format (name or number): ").strip().lower()
        
        # Convert number to format name
        formats_list = list_supported_formats()
        if format_choice.isdigit():
            choice_num = int(format_choice) - 1
            if 0 <= choice_num < len(formats_list):
                output_format = formats_list[choice_num]
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(formats_list)}.")
                return
        else:
            if format_choice not in formats_list:
                print(f"Invalid format: {format_choice}")
                print(f"Supported formats: {', '.join(formats_list)}")
                return
            output_format = format_choice
        
        # Get input file path
        input_path = input("\nEnter path to input video file: ").strip().strip('"')
        if not input_path:
            print("No input provided — exiting.")
            return
        
        # Generate default output path
        default_ext = SUPPORTED_FORMATS[output_format][0]
        default_output = os.path.splitext(input_path)[0] + f".{default_ext}"
        
        # Get output path
        output_path = input(f"Enter output path [default: {default_output}]: ").strip().strip('"')
        if not output_path:
            output_path = default_output
        
        # Get quality
        print("\nQuality options:")
        print("  1) Low (faster, larger file)")
        print("  2) Medium (balanced)")
        print("  3) High (slower, smaller file)")
        print("  4) Copy (no re-encoding, fastest)")
        quality_choice = input("Enter quality (1-4) [default: 2]: ").strip()
        
        quality_map = {'1': 'low', '2': 'medium', '3': 'high', '4': 'copy'}
        quality = quality_map.get(quality_choice, 'medium')
        
        # Optional: codec selection
        codec = None
        if quality != 'copy':
            codec_input = input("Enter codec (h264, h265, vp9, or press Enter for default): ").strip().lower()
            if codec_input:
                codec = codec_input
        
        print(f"\nConverting:\n  Input: {input_path}\n  Output: {output_path}\n  Format: {output_format.upper()}\n  Quality: {quality}")
        if codec:
            print(f"  Codec: {codec}")
        print("\nThis may take a while...")
        
        # Perform conversion
        out = convert_video(input_path, output_path, output_format, quality, codec)
        print(f"✓ Successfully converted to: {out}")
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(2)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(2)
    except RuntimeError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print("Conversion failed. Common causes:")
        print("  - Unsupported input format")
        print("  - Insufficient disk space")
        print("  - Corrupted input file")
        print("  - imageio-ffmpeg not installed")
        print(f"\nError details: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()


