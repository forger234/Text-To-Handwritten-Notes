✍️ Text to Handwriting Notes

Convert your typed digital notes into realistic handwritten-style images using Python and OpenCV — no internet or external API required!
🖼️ Project Preview

📌 Features

    ✅ Converts any input text to a handwriting-style image

    ✅ Fully offline (no internet or API required)

    ✅ Customizable text color, font, and page size

    ✅ Great for generating handwritten notes for fun or presentations

🛠️ Tech Stack

    Python 🐍

    OpenCV

    NumPy

    PIL (Pillow)

    TrueType handwriting fonts (.ttf)

🗂️ Folder Structure

📁 Text-to-Handwriting/
│
├── handwriting.py        # Main Python script
├── handwriting.ttf       # Handwriting-style font file
├── handwriting_output.png  # Sample output
├── README.md             # Project documentation

⚙️ Installation & Setup
1. Clone the Repository

git clone https://github.com/yourusername/text-to-handwriting.git
cd text-to-handwriting

2. Install Required Libraries

pip install opencv-python pillow numpy

3. Download a Handwriting Font

    Get a free handwriting font from dafont.com

    Rename it to handwriting.ttf and place it in the project directory.

🚀 How to Run
Step-by-Step

    Open handwriting.py in your code editor

    Edit the text variable with your own content

    Run the script:

python handwriting.py

    The output image handwriting_output.png will be generated in the same folder.

🖊️ Customization
Option	How to Customize
Font style	Replace handwriting.ttf with any .ttf font
Font size	Adjust font_size in the code
Text color	Change the RGB value in fill=(R,G,B)
Page size	Change img_width and img_height
📄 License

This project is open-source under the MIT License.
💡 Credits

Built with ❤️ using Python and OpenCV.
Font credits to respective designers from dafont.com.
