import os
import sys
from wand.image import Image


# Supported image formats
SUPPORTED_FORMATS = {
    'jpeg': ['jpg', 'jpeg'],
    'png': ['png'],
    'gif': ['gif'],
    'webp': ['webp'],
    'bmp': ['bmp'],
    'tiff': ['tiff', 'tif'],
    'pdf': ['pdf'],
    'ico': ['ico'],
    'heic': ['heic', 'heif'],
    'avif': ['avif'],
}


def get_format_from_extension(extension: str) -> str | None:
    """Get the Wand format name from a file extension."""
    extension = extension.lower().lstrip('.')
    for format_name, extensions in SUPPORTED_FORMATS.items():
        if extension in extensions:
            return format_name
    return None


def convert_image(input_path: str, output_path: str | None = None, output_format: str | None = None, quality: int = 85) -> str:
    """Convert an input image to a specified format using Wand.
    
    Args:
        input_path: Path to the input image file
        output_path: Path for the output file (optional, auto-generated if not provided)
        output_format: Output format (jpeg, png, gif, webp, pdf, etc.). If None, inferred from output_path extension
        quality: Compression quality for lossy formats (1-100, default: 85)
    
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
    
    # Perform conversion
    with Image(filename=input_path) as img:
        img.format = output_format
        
        # Set quality for lossy formats
        if output_format in ['jpeg', 'jpg', 'webp']:
            img.compression_quality = quality
        
        img.save(filename=output_path)
    
    return output_path


def list_supported_formats() -> list[str]:
    """Return a list of supported output formats."""
    return list(SUPPORTED_FORMATS.keys())


def main() -> None:
    """Interactive CLI for image conversion."""
    try:
        print("=== Image Converter ===\n")
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
        input_path = input("\nEnter path to input image file: ").strip().strip('"')
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
        
        # Get quality for lossy formats
        quality = 85
        if output_format in ['jpeg', 'jpg', 'webp']:
            quality_input = input(f"Enter quality (1-100) [default: {quality}]: ").strip()
            if quality_input:
                try:
                    quality = int(quality_input)
                    if not (1 <= quality <= 100):
                        print("Quality must be between 1 and 100. Using default: 85")
                        quality = 85
                except ValueError:
                    print("Invalid quality value. Using default: 85")
                    quality = 85
        
        print(f"\nConverting:\n  Input: {input_path}\n  Output: {output_path}\n  Format: {output_format.upper()}")
        
        # Perform conversion
        out = convert_image(input_path, output_path, output_format, quality)
        print(f"✓ Successfully converted to: {out}")
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(2)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(2)
    except Exception as e:
        print("Conversion failed. Common causes:")
        print("  - ImageMagick (or Ghostscript for PDF) not installed")
        print("  - Unsupported input format")
        print("  - Insufficient permissions")
        print(f"\nError details: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()


