TokenTally

TokenTally is a user-friendly application designed to help you create and number your game tokens effortlessly. Whether you're a Dungeon Master preparing for a Dungeons & Dragons campaign or a player customizing tokens for any tabletop game, TokenTally streamlines the process of adding overlays and numbering your tokens.
Features

    Drag and Drop Interface: Easily import images by dragging and dropping them into the application.
    Supported Formats: Accepts .webp, .png, .jpg, and .jpeg image files.
    Customizable Overlays: Add numbers or short text overlays to your tokens.
    Font Customization: Adjust the font size and color of the overlay text.
    Overlay Positioning: Reposition the overlay using intuitive arrow buttons.
    Batch Processing: Generate sequences of numbered tokens with ease.
    Output Settings: Customize output dimensions and DPI settings.
    Save Options: Choose the save directory or save to the original image directory.

Table of Contents

    Prerequisites
    Installation
    Running TokenTally
    Using TokenTally
        1. Importing an Image
            Via File Dialog
            Via Drag and Drop
        2. Customizing the Overlay
            Entering Overlay Text
            Adjusting Font Size
            Choosing Font Color
        3. Repositioning the Overlay
        4. Batch Processing
        5. Configuring Output Settings
            Output Dimensions
            Output DPI
        6. Selecting Save Directory
        7. Saving the Image(s)
    Troubleshooting
    License

Prerequisites

    Python 3.x: Ensure you have Python 3 installed. You can download it from the official website.

    PyQt5: TokenTally uses the PyQt5 library for its graphical user interface.

    Install PyQt5 using pip:

    pip install PyQt5

Installation

    Clone or Download the Repository

    Clone the repository using git:

git clone https://github.com/Flaxcon/TokenTally.git

Or download the ZIP file and extract it to your preferred location.

Navigate to the Directory

cd TokenTally

Install Required Dependencies

Ensure that PyQt5 is installed:

    pip install PyQt5

Running TokenTally

Run the application using the following command:

python tokentally.py

Note: Replace tokentally.py with the actual filename if it's different.
Using TokenTally
1. Importing an Image

You can import an image into TokenTally in two ways:
Via File Dialog

    Click the "Select Image File" button at the top of the application window.
    In the file dialog that appears, navigate to the image file you wish to use.
    Select the file and click "Open".
        Supported image formats: .webp, .png, .jpg, .jpeg.

Via Drag and Drop

    Open the folder containing your image file.
    Click and drag the image file over to the image preview area in TokenTally.
        The area labeled "Image Preview Will Appear Here".
    Release the mouse button to drop the image into the application.

2. Customizing the Overlay

Once your image is loaded, you can customize the overlay text that will appear on your token.
Entering Overlay Text

    In the "Overlay Settings" section, find the "Enter 1 or 2 Digits:" input field.
    Type the number or text (up to 2 characters) you wish to overlay on the image.

Adjusting Font Size

    Use the "Font Size:" spin box to adjust the size of the overlay text.
        Click the up or down arrows to increase or decrease the font size.
        You can also type a value directly into the field.
        Font size range: 10 to 100.

Choosing Font Color

    Click the "Choose Font Color" button.
    A color dialog will appear.
    Select your desired color and click "OK".
    The button's background will change to the selected color.

3. Repositioning the Overlay

You can adjust the position of the overlay text using the arrow buttons in the "Reposition Overlay" section.

    Up (↑): Moves the overlay up.
    Down (↓): Moves the overlay down.
    Left (←): Moves the overlay to the left.
    Right (→): Moves the overlay to the right.

Each click moves the overlay by 5 pixels. Adjust as needed to position the overlay precisely.
4. Batch Processing

TokenTally allows you to generate a sequence of numbered tokens automatically.

    In the "Batch Overlay Settings" section:
        Start Number: Set the starting number of your sequence.
        End Number: Set the ending number of your sequence.

    Example:
        Start Number: 1
        End Number: 5

    This will generate tokens numbered from 1 to 5.

Note: If you set both the start and end numbers to 1, only one image will be generated.
5. Configuring Output Settings
Output Dimensions

    In the "Output Settings" section, you can specify the dimensions of the output image.
        Output Width (px): Set the desired width in pixels.
        Output Height (px): Set the desired height in pixels.

    Adjust these values to meet the requirements of your virtual tabletop or printing needs.

Output DPI

    Output DPI: Set the dots per inch (DPI) for the output image.
        DPI range: 72 to 600.
        Higher DPI values result in higher resolution images.

6. Selecting Save Directory

    By default, TokenTally saves the generated images in the same directory as the original image.

    To choose a different save location:
        Click the "Select Save Directory" button.
        In the directory selection dialog, navigate to the desired folder.
        Click "Select Folder".
        The chosen directory path will appear next to the button.

7. Saving the Image(s)

    Once you have configured all settings and are satisfied with the preview:
        Click the "Save as PNG" button at the bottom of the application window.
        TokenTally will process the image(s) and save them to the specified directory.
        A confirmation message will appear upon successful saving.

    Output Filenames:
        The generated images will be saved with filenames based on the original image's name and the overlay numbers.
        Example: If the original image is token.png and you're generating numbers from 1 to 5, the output files will be token1.png, token2.png, ..., token5.png.

Troubleshooting

    Application Does Not Start:

        Ensure you have Python 3.x installed.

        Verify that PyQt5 is installed correctly by running:

    pip install PyQt5

Cannot Import PyQt5 Module:

    There might be conflicting versions of PyQt5.

    Try reinstalling PyQt5:

    pip uninstall PyQt5
    pip install PyQt5

Drag and Drop Not Working:

    Ensure you're dragging the image over the image preview area.
    Verify that the image file is one of the supported formats: .webp, .png, .jpg, .jpeg.
    On some operating systems, running the application with elevated privileges can interfere with drag and drop. Run the application with standard user privileges.

Overlay Text Not Appearing:

    Make sure you've entered text in the "Enter 1 or 2 Digits:" field.
    Check that the font size is not too small.
    Verify that the font color contrasts with the image background.

Saved Images Not Found:

    Confirm the save directory path displayed next to the "Select Save Directory" button.
    If no directory is selected, images are saved in the same folder as the original image.

Error Messages:

    If an error message appears, read the details provided.
    Common issues include unsupported image formats or problems saving files due to permissions.
    Ensure you have write permissions to the save directory.
