# File Converter

A Python-based file conversion tool that converts images and videos to various formats. Supports multiple image formats (JPEG, PNG, GIF, WEBP, PDF, etc.) and video formats (MP4, AVI, MOV, MKV, WEBM, etc.) with an intuitive CLI interface.

## Project Status: Active Development

This project provides a working CLI for both image and video format conversions. Future development will add a web interface and additional features.

## Current Features

### Image Conversion
- **Multiple format support**: JPEG, PNG, GIF, WEBP, BMP, TIFF, PDF, ICO, HEIC, AVIF
- **Customizable quality**: Adjustable compression quality for lossy formats (default: 85)
- **Multi-frame support**: Handles animated GIFs and converts all frames to PDF
- **Format detection**: Automatically detects output format from file extension

### Video Conversion
- **Multiple format support**: MP4, AVI, MOV, MKV, WEBM, FLV, WMV, M4V, 3GP, OGV
- **Quality presets**: Low, Medium, High, and Copy (no re-encoding)
- **Codec selection**: Support for H.264, H.265, VP9, VP8, and more
- **Bundled ffmpeg**: No manual installation required - ffmpeg is automatically bundled via `imageio-ffmpeg`

### General Features
- **Modular architecture**: Separate modules for image and video conversion
- **Unified interface**: Single entry point (`main.py`) for all conversions
- **Interactive CLI**: User-friendly command-line interface
- **Automatic path generation**: Generates output paths if not specified
- **Directory creation**: Automatically creates output directories if needed

## Planned Features

### Backend Development
- [x] Basic image conversion (JPEG, PNG, GIF, WEBP, PDF, etc.)
- [x] Video conversion (MP4, AVI, MOV, MKV, WEBM, etc.)
- [x] Bundled ffmpeg (no manual installation)
- [ ] Support for additional file types:
  - [ ] Documents (DOCX, TXT, etc.)
  - [ ] Audio files (MP3, WAV, etc.)
- [ ] Batch processing capabilities
- [ ] Advanced compression options
- [x] Basic error handling and validation
- [ ] API endpoint development
- [ ] File upload/download functionality

## Frontend Development
- [ ] Modern React/Next.js web interface
- [ ] Drag-and-drop file upload
- [ ] Progress indicators for conversions
- [ ] Preview functionality
- [ ] User authentication
- [ ] Conversion history
- [ ] Responsive design

## Infrastructure (Planned)
- [ ] Database integration for user data and conversion history
- [ ] Cloud storage integration
- [ ] Containerization with Docker
- [ ] CI/CD pipeline
- [ ] Automated testing
- [ ] Performance monitoring
- [ ] Rate limiting and queue system

## Tech Stack

### Current
- **Backend**: Python 3.8+
- **Image Processing**: Wand (ImageMagick bindings)
- **Video Processing**: ffmpeg (bundled via `imageio-ffmpeg`)
- **CLI Interface**: Built-in Python interactive prompts
- **Architecture**: Modular design with separate converters for images and videos

### Planned
- FastAPI/Django
- PostgreSQL
- Redis (Caching/Queue)

### Frontend
- React/Next.js
- TypeScript
- Tailwind CSS
- Material-UI/Chakra UI

### Infrastructure
- Docker
- AWS/GCP
- GitHub Actions
- Nginx

## Installation

### Prerequisites

- Python 3.8+ (supports type hints with `str | None`)
- ImageMagick (required by Wand for image processing)
- Virtual environment (recommended)

### Setup

1. **Install ImageMagick** (required for image conversion):
   - **macOS**: `brew install imagemagick`
   - **Linux**: `sudo apt-get install imagemagick` (Debian/Ubuntu) or `sudo yum install ImageMagick` (RHEL/CentOS)
   - **Windows**: Download from [ImageMagick website](https://imagemagick.org/script/download.php)

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   This will install:
   - `Wand` - ImageMagick bindings for image processing
   - `imageio-ffmpeg` - Bundles ffmpeg for video processing (no manual installation needed)

**Note**: ffmpeg will be automatically downloaded on first video conversion use. No manual installation required!

## Usage

### Main Entry Point

Run the main converter:

```bash
python main.py
```

This will present a menu to choose between image or video conversion.

### Individual Converters

You can also run the converters individually:

```bash
# Image converter only
python image_converter.py

# Video converter only
python video_converter.py
```

### Image Conversion Example

```
=== Image Converter ===

Supported output formats:
  1) JPEG
  2) PNG
  3) GIF
  4) WEBP
  5) PDF
  6) BMP
  7) TIFF
  8) ICO
  9) HEIC
  10) AVIF

Enter output format (name or number): 1
Enter path to input image file: /path/to/image.png
Enter output path [default: /path/to/image.jpg]: 
Enter quality (1-100) [default: 85]: 
```

### Video Conversion Example

```
=== Video Converter ===

Supported output formats:
  1) MP4
  2) AVI
  3) MOV
  4) MKV
  5) WEBM
  ...

Enter output format (name or number): 1
Enter path to input video file: /path/to/video.avi
Enter output path [default: /path/to/video.mp4]: 

Quality options:
  1) Low (faster, larger file)
  2) Medium (balanced)
  3) High (slower, smaller file)
  4) Copy (no re-encoding, fastest)
Enter quality (1-4) [default: 2]: 
```

### Programmatic Usage

You can also use the conversion functions directly in your Python code:

```python
from image_converter import convert_image
from video_converter import convert_video

# Convert image to JPEG
output = convert_image("input.png", output_format="jpeg", quality=85)

# Convert image to PNG
output = convert_image("input.jpg", "output.png", output_format="png")

# Convert video to MP4 with high quality
output = convert_video("input.avi", "output.mp4", output_format="mp4", quality="high")

# Convert video with custom codec
output = convert_video("input.mov", output_format="mp4", quality="medium", codec="h265")
```


## Project Structure

```
File Converter/
├── main.py              # Main entry point - unified interface
├── image_converter.py   # Image conversion module
├── video_converter.py   # Video conversion module
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Development Roadmap

### Phase 1: Core Backend Development
- [x] Implement basic file conversion functionality (JPEG and PDF)
- [x] Set up modular project structure
- [x] Add support for multiple image formats
- [x] Add video conversion support
- [x] Bundle ffmpeg (no manual installation)
- [x] Add basic error handling
- [x] Create CLI interface
- [ ] Add batch processing capabilities
- [ ] Enhance error handling with more specific error messages

### Phase 2: API Development
- [ ] Design RESTful API
- [ ] Implement endpoints
- [ ] Add request validation
- [ ] Set up authentication system

### Phase 3: Frontend Development
- [ ] Create React application
- [ ] Design user interface
- [ ] Implement file upload
- [ ] Add conversion progress tracking

### Phase 4: Infrastructure
- [ ] Set up database
- [ ] Implement caching
- [ ] Add monitoring
- [ ] Deploy MVP


[MIT License](LICENSE)

## Author

- [@tmac006](https://github.com/tmac006)

---
This README is a living document and will be updated as the project evolves.