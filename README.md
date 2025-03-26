his is a simple Python script that generates a QR code for a given text or URL and saves it as both an SVG and PNG file.

Features

Generates QR codes from text or URLs

Saves QR codes in SVG and PNG formats

Easy to use and lightweight

Prerequisites

Ensure you have Python installed on your system. You also need to install the following dependencies:

pip install pyqrcode pypng

Usage

Clone this repository:

git clone https://github.com/your-username/your-repo.git
cd your-repo

Run the script:

python qr_generator.py

The generated QR codes will be saved as myqr.svg and myqr.png in the project directory.

Code Explanation

import pyqrcode
import png
from pyqrcode import QRCode

# String which represents the QR code
s = "www.geeksforgeeks.org"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file
url.svg("myqr.svg", scale=8)

# Create and save the png file
url.png("myqr.png", scale=6)

Customization

To generate a QR code for a different URL or text, modify this line:

s = "your_custom_text_or_url"

License

This project is licensed under the MIT License.

Contributions

Feel free to submit pull requests or report issues. Happy coding! 
