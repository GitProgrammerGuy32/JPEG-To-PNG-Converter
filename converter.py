from PIL import Image
import os

def convert_jpeg_to_png(input_folder, output_folder):
    jpeg_images = []
    
    # Check if the output folder exists, create if not
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.jpeg') or filename.lower().endswith('.jpg'):
            jpeg_images.append(filename)

    for jpeg_image in jpeg_images:
        input_path = os.path.join(input_folder, jpeg_image)
        output_path = os.path.join(output_folder, os.path.splitext(jpeg_image)[0] + '.png')

        try:
            # Open the JPEG image
            with Image.open(input_path) as img:
                # Save the image in PNG format
                img.save(output_path, format='PNG')
            print(f"Conversion successful: {jpeg_image} -> {os.path.basename(output_path)}")
        except Exception as e:
            print(f"Error converting {jpeg_image}: {e}")

# Example usage
if __name__ == "__main__":
    # Replace 'Images' with the path to your input folder containing JPEG images
    input_folder_path = 'Images'
    
    # Replace 'Output' with the desired output folder for PNG images
    output_folder_path = 'Output'
    
    # Convert JPEG images to PNG
    convert_jpeg_to_png(input_folder_path, output_folder_path)
