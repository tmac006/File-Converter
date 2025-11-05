import sys
import os

# Add the current directory to the path so we can import the converters
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_converter import main as image_main
from video_converter import main as video_main


def main() -> None:
    """Main entry point for the file converter application."""
    print("=" * 50)
    print("       FILE CONVERTER")
    print("=" * 50)
    print("\nWhat would you like to convert?")
    print("  1) Images (JPEG, PNG, GIF, WEBP, PDF, etc.)")
    print("  2) Videos (MP4, AVI, MOV, MKV, WEBM, etc.)")
    print("  3) Exit")
    
    while True:
        choice = input("\nEnter your choice (1, 2, or 3): ").strip()
        
        if choice == '1':
            print("\n" + "=" * 50)
            image_main()
            print("\n" + "=" * 50)
            break
        elif choice == '2':
            print("\n" + "=" * 50)
            video_main()
            print("\n" + "=" * 50)
            break
        elif choice == '3':
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)

