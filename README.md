# ascii-maker

This Python script converts an image into ASCII art using the Python Imaging Library (PIL). The output is a text representation of the image, where different characters represent different shades of gray.

## Features

- Converts images to grayscale.
- Resizes images to a specified width while maintaining the aspect ratio.
- Maps pixel values to ASCII characters to create a visual representation of the image.

## Requirements

- Python 3.x
- Pillow (Python Imaging Library)

You can install Pillow using pip:

```bash
pip install Pillow
```

## Usage

To run the script, use the following command in your terminal:

```bash
python ascii_image.py <image_path> [new_width]
```

### Parameters

- `<image_path>`: The path to the image file you want to convert to ASCII art.
- `[new_width]`: (Optional) The desired width of the ASCII output. The default value is 100.

### Example

```bash
python ascii_image.py example.jpg 80
```

This command will convert `example.jpg` to ASCII art with a width of 80 characters.

## How It Works

1. **Resize the Image**: The image is resized to the specified width while maintaining the aspect ratio.
2. **Convert to Grayscale**: The image is converted to grayscale to simplify the mapping of pixel values to ASCII characters.
3. **Map Pixels to ASCII**: Each pixel's brightness is mapped to a corresponding ASCII character from a predefined set of characters.
4. **Output the ASCII Art**: The resulting ASCII string is printed to the console.

## ASCII Character Set

The following characters are used to represent different shades of gray, from darkest to lightest:

```
@ % # * + = - : .  
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## Acknowledgments

- [Pillow Documentation](https://pillow.readthedocs.io/en/stable/)
- ASCII art inspiration from various online sources.

---

Feel free to customize this README file further based on your preferences or any additional information you want to include!
