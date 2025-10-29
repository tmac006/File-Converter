# File Converter

A Python-based file conversion tool that converts images to JPEG or PDF format. The goal is to evolve it into a full-stack application with both backend conversion capabilities and a modern frontend interface.

## Project Status: Active Development

This project currently provides a working CLI for image format conversions. Future development will add a web interface and support for additional file types.

## Current Features

- **Image to JPEG conversion**: Convert images to JPEG format with customizable compression quality (default: 85)
- **Image to PDF conversion**: Convert images to PDF format (supports multi-frame images like animated GIFs)
- **Command-line interface**: Interactive CLI for easy conversions
- **Automatic output path generation**: Automatically generates output paths if not specified
- **Directory creation**: Automatically creates output directories if they don't exist
- **Python-based backend**: Uses Wand (ImageMagick) for image processing

## Planned Features

### Backend Development
- [x] Basic image conversion (JPEG, PDF)
- [ ] Support for additional file types:
  - [ ] More image formats (PNG, GIF, WEBP, etc.)
  - [ ] Documents (DOCX, TXT, etc.)
  - [ ] Audio files (MP3, WAV, etc.)
  - [ ] Video files (MP4, AVI, etc.)
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
- **CLI Interface**: Built-in Python interactive prompts

### Planned
- FastAPI/Django
- FFmpeg (Media processing)
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
- ImageMagick (required by Wand)
- Virtual environment (recommended)

### Setup

1. Install ImageMagick:
   - **macOS**: `brew install imagemagick`
   - **Linux**: `sudo apt-get install imagemagick` (Debian/Ubuntu) or `sudo yum install ImageMagick` (RHEL/CentOS)
   - **Windows**: Download from [ImageMagick website](https://imagemagick.org/script/download.php)

2. Install Python dependencies:
   ```bash
   pip install Wand
   ```

## Usage

Run the converter from the command line:

```bash
python converter.py
```

The interactive CLI will prompt you to:
1. Select conversion type (PDF or JPEG)
2. Enter the input file path
3. Optionally specify an output path (defaults to same directory with new extension)

### Examples

**Convert to JPEG:**
```
Available conversion types:
1) PDF
2) JPEG
3) JPG

Enter conversion type (1, 2, pdf, or jpeg): 2
Enter path to input image file: /path/to/image.png
Enter output path [default: /path/to/image.jpg]: 
```

**Convert to PDF:**
```
Enter conversion type (1, 2, pdf, or jpeg): pdf
Enter path to input image file: /path/to/image.jpg
Enter output path [default: /path/to/image.pdf]: 
```

### Programmatic Usage

You can also use the conversion functions directly in your Python code:

```python
from converter import convert_to_jpeg, convert_to_pdf

# Convert to JPEG
output = convert_to_jpeg("input.png")

# Convert to PDF
output = convert_to_pdf("input.jpg", "output.pdf")
```


## Development Roadmap

### Phase 1: Core Backend Development
- [x] Implement basic file conversion functionality (JPEG and PDF)
- [x] Set up project structure
- [x] Add basic error handling
- [x] Create basic CLI interface
- [ ] Add support for additional image formats
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