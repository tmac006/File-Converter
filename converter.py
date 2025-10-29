import os
import sys
from wand.image import Image


def convert_to_jpeg(input_path: str, output_path: str | None = None) -> str:
        """Convert an input image to JPEG format using Wand.
        
        Returns the output path on success.
        """
        if not os.path.isfile(input_path):
                raise FileNotFoundError(f"Input file not found: {input_path}")

        if output_path is None or output_path.strip() == "":
                output_path = os.path.splitext(input_path)[0] + ".jpg"

        out_dir = os.path.dirname(output_path)
        if out_dir and not os.path.isdir(out_dir):
                os.makedirs(out_dir, exist_ok=True)

        with Image(filename=input_path) as img:
                img.format = 'jpeg'
                img.compression_quality = 85
                img.save(filename=output_path)

        return output_path


def convert_to_pdf(input_path: str, output_path: str | None = None) -> str:
        """Convert an input image to a PDF using Wand.

        Returns the output path on success
        """
        if not os.path.isfile(input_path):
                raise FileNotFoundError(f"Input file not found: {input_path}")

        if output_path is None or output_path.strip() == "":
                output_path = os.path.splitext(input_path)[0] + ".pdf"

        # Ensure parent directory exists for output
        out_dir = os.path.dirname(output_path)
        if out_dir and not os.path.isdir(out_dir):
                os.makedirs(out_dir, exist_ok=True)

        # Use Wand to write a PDF. This will use ImageMagick under the hood.
        # For multi-frame images (e.g. animated GIF), ImageMagick will write all frames to the PDF.
        with Image(filename=input_path) as img:
                img.format = 'pdf'
                img.save(filename=output_path)

        return output_path


def main() -> None:
        try:
                # Ask for conversion type
                print("Available conversion types:")
                print("1) PDF")
                print("2) JPEG")
                print("3) JPG")
                
                choice = input("\nEnter conversion type (1, 2, pdf, or jpeg): ").strip().lower()
                
                # Get input file path
                input_path = input("Enter path to input image file: ").strip().strip('"')
                if not input_path:
                        print("No input provided — exiting.")
                        return
                
                # Determine output format and create output path
                if choice == '1' or choice == 'pdf':
                        format_type = 'pdf'
                        default_output = os.path.splitext(input_path)[0] + ".pdf"
                elif choice == '2' or choice == 'jpeg' or choice == 'jpg':
                        format_type = 'jpeg'
                        default_output = os.path.splitext(input_path)[0] + ".jpg"
                else:
                        print("Invalid choice. Please enter 1, 2, pdf, or jpeg.")
                        return
                
                # Ask for output path
                output_path = input(f"Enter output path [default: {default_output}]: ").strip().strip('"')
                if not output_path:
                        output_path = default_output

                print(f"\nConverting:\n  input: {input_path}\n  output: {output_path}")
                
                # Perform conversion
                if format_type == 'pdf':
                        out = convert_to_pdf(input_path, output_path)
                else:
                        out = convert_to_jpeg(input_path, output_path)
                
                print(f"Successfully converted to: {out}")

        except FileNotFoundError as e:
                print(e)
                sys.exit(2)
        except Exception as e:
                print("Conversion failed. Common causes: ImageMagick (or Ghostscript) not installed, or unsupported input format.")
                print("Error:\n", e)
                sys.exit(1)


if __name__ == '__main__':
        main()