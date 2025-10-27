from PIL import Image

image_path = ""
pdf_path = ""

try:
        img = Image.open(image_path)
        img.save(pdf_path, 'PDF', resolution=100.0) 
        print(f"Successfully converted {image_path} to {pdf_path}")
except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
except Exception as e:
        print(f"An error occurred: {e}")