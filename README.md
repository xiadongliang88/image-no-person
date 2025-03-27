# Image Processing with YOLO and Inpainting

This project provides a framework for removing people from images using YOLO for object detection and OpenCV or LaMa for inpainting. You can configure the behavior of the program by editing the `conf.py` file.

## Configuration

Edit the `conf.py` file to select the processing scheme and customize its parameters:

```python
scheme = 'A'  # Choose 'A' or 'B'

schemeA = {
    'image_name': 'd1.jpg',  # Input image name
    'is_lama': False,        # Use LaMa for inpainting (True/False)
    'inpaint_radius': 3,     # Radius for OpenCV inpainting
    'is_gaussianblur': True, # Apply Gaussian blur to the mask
    'gaussian_radius': 9     # Gaussian blur radius (odd number)
}

schemeB = {
    'image_name': 'd1.jpg',      # Input image name
    'gaussian_radius': 51,       # Gaussian blur radius (odd number)
    'is_use_fill_color': False,  # Use a fill color for blending
    'fill_color': [227, 234, 244] # RGB fill color
}
```

- **Scheme A**: Uses OpenCV or LaMa for inpainting.
- **Scheme B**: Uses OpenCV for blending without inpainting.

## How to Run

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure the `conf.py` file to select the desired scheme and parameters.

3. Run the main script:
   ```bash
   python main.py
   ```

## Outputs

Processed images will be saved in the `outputs/` directory with filenames indicating the scheme and input image.

## Directory Structure

```
├── images/          # Input images
├── outputs/         # Processed images
├── conf.py          # Configuration file
├── main.py          # Main script
├── schemeA.py       # Scheme A implementation
├── schemeB.py       # Scheme B implementation
├── requirements.txt # Python dependencies
```

## Contact

If you have suggestions for improving this project or new schemes to add, feel free to contact me:

**Email**: xiadongliang88@163.com