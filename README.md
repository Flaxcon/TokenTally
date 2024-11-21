# TokenTally - Advanced Image Numbering and Customization Tool 
![TokenTally Logo](https://github.com/Flaxcon/TokenTally/raw/main/logo.png) 

TokenTally is a powerful and user-friendly PyQt5-based application designed to simplify image editing and batch processing tasks. Whether you're a photographer, graphic designer, or digital artist, TokenTally offers a comprehensive set of tools to customize and manage your images with ease.

## Table of Contents 
 
- [Features](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#features)
 
- [Installation](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#installation)  
  - [Prerequisites](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#prerequisites)
 
  - [Installation Steps](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#installation-steps)
 
- [Usage](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#usage)  
  - [Launching the Application](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#launching-the-application)
 
  - [Importing Images](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#importing-images)
 
  - [Selecting Operational Mode](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#selecting-operational-mode)
 
  - [Customizing Overlays](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#customizing-overlays)
 
  - [Gradient Circle Customization](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#gradient-circle-customization)
 
  - [Output Settings](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#output-settings)
 
  - [Saving Images](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#saving-images)
 
- [Troubleshooting](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#troubleshooting)
 
- [Contributing](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#contributing)
 
- [License](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#license)
 
- [Acknowledgements](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#acknowledgements)


---


## Features 
 
- **Flexible Image Importing:**  
  - **File Selection:**  Easily select images using an intuitive file dialog supporting PNG, JPG, and WEBP formats.
 
  - **Drag-and-Drop:**  Quickly drag images directly into the application for seamless access.
 
  - **Clipboard Support:**  Paste images directly from your clipboard for a streamlined workflow.
 
- **Dual Operational Modes:**  
  - **Cropping Mode:**  Precisely frame and crop images with interactive panning and zooming tools.
 
  - **Conversion Mode:**  Perform general image processing with customizable output settings.
 
- **Interactive Image Manipulation:**  
  - **Panning & Zooming:**  Navigate images effortlessly to focus on specific areas for detailed editing.
 
  - **Real-Time Preview:**  Instantly view changes to ensure edits meet your expectations before saving.
 
- **Customizable Overlays:**  
  - **Text Overlay:**  Add personalized text with options to adjust font size, color, and position.
 
  - **Gradient Circle Customization:**  Select and customize start and end colors for gradient circles to enhance image aesthetics.
 
- **Comprehensive Output Settings:**  
  - **Dimensions & DPI:**  Define output width, height, and DPI to match specific requirements.
 
  - **Batch Numbering:**  Automate the numbering process with customizable batch start and end options. 
    - **Conditional Numbering:** 
      - If the overlay text is exactly "1" and batch processing is active, images will display only the batch numbers (1-5).

      - If the overlay text is anything else, the batch number will be appended to the overlay text (e.g., "Token 1", "Token 2").
 
  - **Save Directory Selection:**  Choose your preferred save location with ease.
 
- **High-Quality Saving:**  
  - **PNG Format:**  Save customized images as high-quality PNG files, preserving transparency and color fidelity.
 
  - **Batch Processing:**  Efficiently process and save multiple images simultaneously, saving valuable time.
 
- **User-Friendly Interface:**  
  - **Intuitive Design:**  Navigate features effortlessly with a clean and organized layout.
 
  - **Responsive Controls:**  Enjoy smooth interactions and immediate feedback during customization.
 
- **Additional Features:**  
  - **Temporary File Management:**  Automatically handles temporary files to keep your workspace clean.
 
  - **Error Handling:**  Provides informative messages and warnings to guide users through any issues.


---


## Installation 

### Prerequisites 

Before installing TokenTally, ensure that your system meets the following requirements:
 
- **Operating System:**  Windows, macOS, or Linux
 
- **Python:**  Version 3.7 or higher
 
- **Python Package Manager:**  `pip`

### Installation Steps 
 
1. **Clone the Repository** 
Begin by cloning the TokenTally repository to your local machine using Git:


```bash
git clone https://github.com/Flaxcon/TokenTally.git
```

Alternatively, you can download the repository as a ZIP file and extract it.
 
2. **Navigate to the Project Directory** 

```bash
cd TokenTally
```
 
3. **Create a Virtual Environment (Optional but Recommended)** 
It's good practice to use a virtual environment to manage dependencies.


```bash
python3 -m venv venv
```

Activate the virtual environment:
 
  - **Windows:** 

```bash
venv\Scripts\activate
```
 
  - **macOS/Linux:** 

```bash
source venv/bin/activate
```
 
4. **Install Dependencies** Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```
**Note:**  If a `requirements.txt` file is not provided, you can install the necessary packages manually:

```bash
pip install PyQt5
```
 
5. **Run the Application** 
Launch TokenTally by running the main script:


```bash
python token_tally.py
```
Replace `token_tally.py` with the actual name of your main Python file if different.


---


## Usage 

Once installed, follow these steps to use TokenTally effectively.

### Launching the Application 

After installation, launch the application using the following command:


```bash
python token_tally.py
```

Upon successful launch, the TokenTally interface will appear, ready for image processing tasks.

### Importing Images 

TokenTally offers multiple methods to import images:
 
1. **File Selection:**  
  - Click the **"Select Image File"**  button.
 
  - Browse and select an image file (supports `.png`, `.jpg`, `.jpeg`, `.webp`).
 
2. **Drag-and-Drop:** 
  - Drag an image file from your file explorer and drop it onto the designated area in the application.
 
3. **Clipboard Support:** 
  - Copy an image to your clipboard.
 
  - Right-click within the application and select **"Paste Image"**  from the context menu.

### Selecting Operational Mode 

TokenTally operates in two distinct modes:
 
1. **Cropping Mode:**  
  - **Purpose:**  Precisely crop images into circular shapes with adjustable panning and zooming.
 
  - **Features:** 
    - Interactive panning by clicking and dragging the image.

    - Zoom in and out using the mouse wheel for detailed cropping.

    - Gradient circle around the cropped image with customizable colors.
 
2. **Conversion Mode:**  
  - **Purpose:**  General image processing without the cropping feature.
 
  - **Features:** 
    - Customize output dimensions, DPI, and batch numbering.

    - Apply text overlays without cropping.
**Switching Modes:**  
  - Navigate to the **"Mode Selection"**  section.
 
  - Choose between **"Cropping Mode"**  and **"Conversion Mode"**  by selecting the corresponding radio button.

### Customizing Overlays 

Enhance your images by adding customizable text overlays:
 
1. **Adding Text:**  
  - Locate the **"Overlay Settings"**  section.
 
  - Enter your desired text in the **"Overlay Text"**  field (maximum 10 characters).
 
2. **Adjusting Font Size:**  
  - Use the **"Font Size"**  spin box to set the desired size of the overlay text.
 
3. **Choosing Font Color:**  
  - Click the **"Choose Font Color"**  button.

  - Select your preferred color from the color picker dialog.
 
4. **Positioning Text:**  
  - Use the arrow buttons (**←** , **→** , **↑** , **↓** ) to move the text overlay to the desired position on the image.
**Conditional Numbering:**  
  - **If `Overlay Text` is exactly "1":** 
    - During batch processing, only the batch numbers (1-5) will appear on the images.
 
  - **If `Overlay Text` is anything else:** 
    - Batch numbers will be appended to the overlay text (e.g., "Token 1", "Token 2").

### Gradient Circle Customization 

Add a personalized gradient circle around your images:
 
1. **Selecting Gradient Start Color:**  
  - Navigate to the **"Gradient Settings"**  section.
 
  - Click the **"Choose Gradient Start Color"**  button.

  - Select your desired start color from the color picker.
 
2. **Selecting Gradient End Color:**  
  - Click the **"Choose Gradient End Color"**  button.

  - Select your desired end color from the color picker.
**Real-Time Preview:** 
  - The gradient circle around the image will update in real-time to reflect your color selections.

### Output Settings 

Configure how your images will be saved:
 
1. **Dimensions & DPI:**  
  - **Output Width (px):**  Set the desired width of the saved image in pixels.
 
  - **Output Height (px):**  Set the desired height of the saved image in pixels.
 
  - **Output DPI:**  Define the resolution (dots per inch) for the saved image.
**Note:**  In **Cropping Mode** , the dimensions are fixed to 200x200 pixels and DPI settings are disabled.
 
2. **Batch Numbering:**  
  - **Batch Start Number:**  Specify the starting number for batch processing.
 
  - **Batch End Number:**  Specify the ending number for batch processing.
**Numbering Behavior:**  
  - **Overlay Text is "1":**  Images will display only the batch numbers (e.g., "1", "2", "3").
 
  - **Overlay Text is anything else:**  Batch numbers will be appended to the overlay text (e.g., "Token 1", "Token 2").
 
3. **Save Directory Selection:**  
  - Click the **"Select Save Directory"**  button.

  - Choose the folder where you want the processed images to be saved.

### Saving Images 

Once all settings are configured, proceed to save your images:
 
1. **Single Image Save:**  
  - Ensure that **Batch Start Number**  and **Batch End Number**  are set to the same value.
 
  - Click the **"Save as PNG"**  button.

  - The image will be saved with the specified overlay text.
 
2. **Batch Image Save:**  
  - Set different values for **Batch Start Number**  and **Batch End Number**  (e.g., Start: 1, End: 5).
 
  - Click the **"Save as PNG"**  button.
 
  - **If Overlay Text is "1":**  Images will be saved with overlay texts "1" to "5".
 
  - **If Overlay Text is "Token":**  Images will be saved with overlay texts "Token 1" to "Token 5".
 
3. **Completion Notification:** 
  - After saving, a confirmation dialog will appear, indicating the range of saved images and their save location.


---


## Troubleshooting 

Encountering issues? Here are some common problems and their solutions:
 
- **All Batch Images Display the Same Number:**  
  - **Cause:**  The overlay text is set to "1", which triggers the numbering logic to use only batch numbers.
 
  - **Solution:**  Ensure that the overlay text is set appropriately based on your desired numbering behavior.
 
- **Application Fails to Save Images:**  
  - **Cause:**  Possible write permissions in the selected save directory or invalid file paths.
 
  - **Solution:**  Verify that you have write permissions to the chosen directory and that the path is valid.
 
- **Images Not Displaying Properly:**  
  - **Cause:**  Unsupported image formats or corrupted files.
 
  - **Solution:**  Use supported formats (`.png`, `.jpg`, `.jpeg`, `.webp`) and ensure that the images are not corrupted.
 
- **Application Crashes or Freezes:**  
  - **Cause:**  Insufficient system resources or bugs in the application.
 
  - **Solution:**  Ensure your system meets the prerequisites and consider updating Python and PyQt5 to the latest versions.
 
- **Gradient Colors Not Applying:**  
  - **Cause:**  Issues with color selection or rendering.
 
  - **Solution:**  Re-select gradient colors using the provided buttons and ensure that color values are valid.


---


## Contributing 

We welcome contributions from the community! If you'd like to contribute to TokenTally, please follow these guidelines:
 
1. **Fork the Repository** Click the **"Fork"**  button at the top-right corner of the repository page to create a copy in your GitHub account.
 
2. **Clone Your Fork** 

```bash
git clone https://github.com/your-username/TokenTally.git
cd TokenTally
```
 
3. **Create a New Branch** 

```bash
git checkout -b feature/YourFeatureName
```
 
4. **Make Your Changes** 
Implement your feature or bug fix.
 
5. **Commit Your Changes** 

```bash
git add .
git commit -m "Description of your changes"
```
 
6. **Push to Your Fork** 

```bash
git push origin feature/YourFeatureName
```
 
7. **Create a Pull Request** Navigate to your fork on GitHub and click the **"Compare & pull request"**  button. Provide a clear description of your changes and submit the pull request.
**Please ensure that your contributions adhere to the project's coding standards and include appropriate documentation and tests.** 

---


## License 
Distributed under the [MIT License]() .

---


## Acknowledgements 
 
- [PyQt5]()  - Python bindings for the Qt application framework.
 
- [Python](https://www.python.org/)  - The programming language used for development.
 
- [GitHub](https://github.com/)  - Hosting platform for version control and collaboration.


---

**Thought for 7 seconds
# TokenTally - Advanced Image Numbering and Customization Tool 
![TokenTally Logo](https://github.com/Flaxcon/TokenTally/raw/main/logo.png) 

TokenTally is a powerful and user-friendly PyQt5-based application designed to simplify image editing and batch processing tasks. Whether you're a photographer, graphic designer, or digital artist, TokenTally offers a comprehensive set of tools to customize and manage your images with ease.

## Table of Contents 
 
- [Features](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#features)
 
- [Installation](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#installation)  
  - [Prerequisites](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#prerequisites)
 
  - [Installation Steps](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#installation-steps)
 
- [Usage](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#usage)  
  - [Launching the Application](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#launching-the-application)
 
  - [Importing Images](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#importing-images)
 
  - [Selecting Operational Mode](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#selecting-operational-mode)
 
  - [Customizing Overlays](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#customizing-overlays)
 
  - [Gradient Circle Customization](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#gradient-circle-customization)
 
  - [Output Settings](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#output-settings)
 
  - [Saving Images](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#saving-images)
 
- [Troubleshooting](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#troubleshooting)
 
- [Contributing](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#contributing)
 
- [License](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#license)
 
- [Acknowledgements](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#acknowledgements)


---


## Features 
 
- **Flexible Image Importing:**  
  - **File Selection:**  Easily select images using an intuitive file dialog supporting PNG, JPG, and WEBP formats.
 
  - **Drag-and-Drop:**  Quickly drag images directly into the application for seamless access.
 
  - **Clipboard Support:**  Paste images directly from your clipboard for a streamlined workflow.
 
- **Dual Operational Modes:**  
  - **Cropping Mode:**  Precisely frame and crop images with interactive panning and zooming tools.
 
  - **Conversion Mode:**  Perform general image processing with customizable output settings.
 
- **Interactive Image Manipulation:**  
  - **Panning & Zooming:**  Navigate images effortlessly to focus on specific areas for detailed editing.
 
  - **Real-Time Preview:**  Instantly view changes to ensure edits meet your expectations before saving.
 
- **Customizable Overlays:**  
  - **Text Overlay:**  Add personalized text with options to adjust font size, color, and position.
 
  - **Gradient Circle Customization:**  Select and customize start and end colors for gradient circles to enhance image aesthetics.
 
- **Comprehensive Output Settings:**  
  - **Dimensions & DPI:**  Define output width, height, and DPI to match specific requirements.
 
  - **Batch Numbering:**  Automate the numbering process with customizable batch start and end options. 
    - **Conditional Numbering:** 
      - If the overlay text is exactly "1" and batch processing is active, images will display only the batch numbers (1-5).

      - If the overlay text is anything else, the batch number will be appended to the overlay text (e.g., "Token 1", "Token 2").
 
  - **Save Directory Selection:**  Choose your preferred save location with ease.
 
- **High-Quality Saving:**  
  - **PNG Format:**  Save customized images as high-quality PNG files, preserving transparency and color fidelity.
 
  - **Batch Processing:**  Efficiently process and save multiple images simultaneously, saving valuable time.
 
- **User-Friendly Interface:**  
  - **Intuitive Design:**  Navigate features effortlessly with a clean and organized layout.
 
  - **Responsive Controls:**  Enjoy smooth interactions and immediate feedback during customization.
 
- **Additional Features:**  
  - **Temporary File Management:**  Automatically handles temporary files to keep your workspace clean.
 
  - **Error Handling:**  Provides informative messages and warnings to guide users through any issues.


---


## Installation 

### Prerequisites 

Before installing TokenTally, ensure that your system meets the following requirements:
 
- **Operating System:**  Windows, macOS, or Linux
 
- **Python:**  Version 3.7 or higher
 
- **Python Package Manager:**  `pip`

### Installation Steps 
 
1. **Clone the Repository** 
Begin by cloning the TokenTally repository to your local machine using Git:


```bash
git clone https://github.com/Flaxcon/TokenTally.git
```

Alternatively, you can download the repository as a ZIP file and extract it.
 
2. **Navigate to the Project Directory** 

```bash
cd TokenTally
```
 
3. **Create a Virtual Environment (Optional but Recommended)** 
It's good practice to use a virtual environment to manage dependencies.


```bash
python3 -m venv venv
```

Activate the virtual environment:
 
  - **Windows:** 

```bash
venv\Scripts\activate
```
 
  - **macOS/Linux:** 

```bash
source venv/bin/activate
```
 
4. **Install Dependencies** Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```
**Note:**  If a `requirements.txt` file is not provided, you can install the necessary packages manually:

```bash
pip install PyQt5
```
 
5. **Run the Application** 
Launch TokenTally by running the main script:


```bash
python token_tally.py
```
Replace `token_tally.py` with the actual name of your main Python file if different.


---


## Usage 

Once installed, follow these steps to use TokenTally effectively.

### Launching the Application 

After installation, launch the application using the following command:


```bash
python token_tally.py
```

Upon successful launch, the TokenTally interface will appear, ready for image processing tasks.

### Importing Images 

TokenTally offers multiple methods to import images:
 
1. **File Selection:**  
  - Click the **"Select Image File"**  button.
 
  - Browse and select an image file (supports `.png`, `.jpg`, `.jpeg`, `.webp`).
 
2. **Drag-and-Drop:** 
  - Drag an image file from your file explorer and drop it onto the designated area in the application.
 
3. **Clipboard Support:** 
  - Copy an image to your clipboard.
 
  - Right-click within the application and select **"Paste Image"**  from the context menu.

### Selecting Operational Mode 

TokenTally operates in two distinct modes:
 
1. **Cropping Mode:**  
  - **Purpose:**  Precisely crop images into circular shapes with adjustable panning and zooming.
 
  - **Features:** 
    - Interactive panning by clicking and dragging the image.

    - Zoom in and out using the mouse wheel for detailed cropping.

    - Gradient circle around the cropped image with customizable colors.
 
2. **Conversion Mode:**  
  - **Purpose:**  General image processing without the cropping feature.
 
  - **Features:** 
    - Customize output dimensions, DPI, and batch numbering.

    - Apply text overlays without cropping.
**Switching Modes:**  
  - Navigate to the **"Mode Selection"**  section.
 
  - Choose between **"Cropping Mode"**  and **"Conversion Mode"**  by selecting the corresponding radio button.

### Customizing Overlays 

Enhance your images by adding customizable text overlays:
 
1. **Adding Text:**  
  - Locate the **"Overlay Settings"**  section.
 
  - Enter your desired text in the **"Overlay Text"**  field (maximum 10 characters).
 
2. **Adjusting Font Size:**  
  - Use the **"Font Size"**  spin box to set the desired size of the overlay text.
 
3. **Choosing Font Color:**  
  - Click the **"Choose Font Color"**  button.

  - Select your preferred color from the color picker dialog.
 
4. **Positioning Text:**  
  - Use the arrow buttons (**←** , **→** , **↑** , **↓** ) to move the text overlay to the desired position on the image.
**Conditional Numbering:**  
  - **If `Overlay Text` is exactly "1":** 
    - During batch processing, only the batch numbers (1-5) will appear on the images.
 
  - **If `Overlay Text` is anything else:** 
    - Batch numbers will be appended to the overlay text (e.g., "Token 1", "Token 2").

### Gradient Circle Customization 

Add a personalized gradient circle around your images:
 
1. **Selecting Gradient Start Color:**  
  - Navigate to the **"Gradient Settings"**  section.
 
  - Click the **"Choose Gradient Start Color"**  button.

  - Select your desired start color from the color picker.
 
2. **Selecting Gradient End Color:**  
  - Click the **"Choose Gradient End Color"**  button.

  - Select your desired end color from the color picker.
**Real-Time Preview:** 
  - The gradient circle around the image will update in real-time to reflect your color selections.

### Output Settings 

Configure how your images will be saved:
 
1. **Dimensions & DPI:**  
  - **Output Width (px):**  Set the desired width of the saved image in pixels.
 
  - **Output Height (px):**  Set the desired height of the saved image in pixels.
 
  - **Output DPI:**  Define the resolution (dots per inch) for the saved image.
**Note:**  In **Cropping Mode** , the dimensions are fixed to 200x200 pixels and DPI settings are disabled.
 
2. **Batch Numbering:**  
  - **Batch Start Number:**  Specify the starting number for batch processing.
 
  - **Batch End Number:**  Specify the ending number for batch processing.
**Numbering Behavior:**  
  - **Overlay Text is "1":**  Images will display only the batch numbers (e.g., "1", "2", "3").
 
  - **Overlay Text is anything else:**  Batch numbers will be appended to the overlay text (e.g., "Token 1", "Token 2").
 
3. **Save Directory Selection:**  
  - Click the **"Select Save Directory"**  button.

  - Choose the folder where you want the processed images to be saved.

### Saving Images 

Once all settings are configured, proceed to save your images:
 
1. **Single Image Save:**  
  - Ensure that **Batch Start Number**  and **Batch End Number**  are set to the same value.
 
  - Click the **"Save as PNG"**  button.

  - The image will be saved with the specified overlay text.
 
2. **Batch Image Save:**  
  - Set different values for **Batch Start Number**  and **Batch End Number**  (e.g., Start: 1, End: 5).
 
  - Click the **"Save as PNG"**  button.
 
  - **If Overlay Text is "1":**  Images will be saved with overlay texts "1" to "5".
 
  - **If Overlay Text is "Token":**  Images will be saved with overlay texts "Token 1" to "Token 5".
 
3. **Completion Notification:** 
  - After saving, a confirmation dialog will appear, indicating the range of saved images and their save location.


---


## Troubleshooting 

Encountering issues? Here are some common problems and their solutions:
 
- **All Batch Images Display the Same Number:**  
  - **Cause:**  The overlay text is set to "1", which triggers the numbering logic to use only batch numbers.
 
  - **Solution:**  Ensure that the overlay text is set appropriately based on your desired numbering behavior.
 
- **Application Fails to Save Images:**  
  - **Cause:**  Possible write permissions in the selected save directory or invalid file paths.
 
  - **Solution:**  Verify that you have write permissions to the chosen directory and that the path is valid.
 
- **Images Not Displaying Properly:**  
  - **Cause:**  Unsupported image formats or corrupted files.
 
  - **Solution:**  Use supported formats (`.png`, `.jpg`, `.jpeg`, `.webp`) and ensure that the images are not corrupted.
 
- **Application Crashes or Freezes:**  
  - **Cause:**  Insufficient system resources or bugs in the application.
 
  - **Solution:**  Ensure your system meets the prerequisites and consider updating Python and PyQt5 to the latest versions.
 
- **Gradient Colors Not Applying:**  
  - **Cause:**  Issues with color selection or rendering.
 
  - **Solution:**  Re-select gradient colors using the provided buttons and ensure that color values are valid.


---


## Contributing 

We welcome contributions from the community! If you'd like to contribute to TokenTally, please follow these guidelines:
 
1. **Fork the Repository** Click the **"Fork"**  button at the top-right corner of the repository page to create a copy in your GitHub account.
 
2. **Clone Your Fork** 

```bash
git clone https://github.com/your-username/TokenTally.git
cd TokenTally
```
 
3. **Create a New Branch** 

```bash
git checkout -b feature/YourFeatureName
```
 
4. **Make Your Changes** 
Implement your feature or bug fix.
 
5. **Commit Your Changes** 

```bash
git add .
git commit -m "Description of your changes"
```
 
6. **Push to Your Fork** 

```bash
git push origin feature/YourFeatureName
```
 
7. **Create a Pull Request** Navigate to your fork on GitHub and click the **"Compare & pull request"**  button. Provide a clear description of your changes and submit the pull request.
**Please ensure that your contributions adhere to the project's coding standards and include appropriate documentation and tests.** 

---


## License 
Distributed under the [MIT License]() .

---


## Acknowledgements 
 
- [PyQt5]()  - Python bindings for the Qt application framework.
 
- [Python](https://www.python.org/)  - The programming language used for development.
 
- [GitHub](https://github.com/)  - Hosting platform for version control and collaboration.


---

Enjoy using TokenTally! For any questions or support, please open an issue in the [GitHub repository](https://github.com/Flaxcon/TokenTally/issues) .**

You: 

please provide the above response in markdown

ChatGPT: 

Thought for 4 seconds
Sure, here's the previous response in markdown format:

# TokenTally - Advanced Image Numbering and Customization Tool 
![TokenTally Logo](https://github.com/Flaxcon/TokenTally/raw/main/logo.png) 

TokenTally is a powerful and user-friendly PyQt5-based application designed to simplify image editing and batch processing tasks. Whether you're a photographer, graphic designer, or digital artist, TokenTally offers a comprehensive set of tools to customize and manage your images with ease.

## Table of Contents 
 
- [Features](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#features)
 
- [Installation](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#installation)  
  - [Prerequisites](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#prerequisites)
 
  - [Installation Steps](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#installation-steps)
 
- [Usage](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#usage)  
  - [Launching the Application](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#launching-the-application)
 
  - [Importing Images](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#importing-images)
 
  - [Selecting Operational Mode](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#selecting-operational-mode)
 
  - [Customizing Overlays](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#customizing-overlays)
 
  - [Gradient Circle Customization](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#gradient-circle-customization)
 
  - [Output Settings](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#output-settings)
 
  - [Saving Images](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#saving-images)
 
- [Troubleshooting](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#troubleshooting)
 
- [Contributing](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#contributing)
 
- [License](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#license)
 
- [Acknowledgements](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#acknowledgements)


---


## Features 
 
- **Flexible Image Importing:**  
  - **File Selection:**  Easily select images using an intuitive file dialog supporting PNG, JPG, and WEBP formats.
 
  - **Drag-and-Drop:**  Quickly drag images directly into the application for seamless access.
 
  - **Clipboard Support:**  Paste images directly from your clipboard for a streamlined workflow.
 
- **Dual Operational Modes:**  
  - **Cropping Mode:**  Precisely frame and crop images with interactive panning and zooming tools.
 
  - **Conversion Mode:**  Perform general image processing with customizable output settings.
 
- **Interactive Image Manipulation:**  
  - **Panning & Zooming:**  Navigate images effortlessly to focus on specific areas for detailed editing.
 
  - **Real-Time Preview:**  Instantly view changes to ensure edits meet your expectations before saving.
 
- **Customizable Overlays:**  
  - **Text Overlay:**  Add personalized text with options to adjust font size, color, and position.
 
  - **Gradient Circle Customization:**  Select and customize start and end colors for gradient circles to enhance image aesthetics.
 
- **Comprehensive Output Settings:**  
  - **Dimensions & DPI:**  Define output width, height, and DPI to match specific requirements.
 
  - **Batch Numbering:**  Automate the numbering process with customizable batch start and end options. 
    - **Conditional Numbering:** 
      - If the overlay text is exactly "1" and batch processing is active, images will display only the batch numbers (1-5).

      - If the overlay text is anything else, the batch number will be appended to the overlay text (e.g., "Token 1", "Token 2").
 
  - **Save Directory Selection:**  Choose your preferred save location with ease.
 
- **High-Quality Saving:**  
  - **PNG Format:**  Save customized images as high-quality PNG files, preserving transparency and color fidelity.
 
  - **Batch Processing:**  Efficiently process and save multiple images simultaneously, saving valuable time.
 
- **User-Friendly Interface:**  
  - **Intuitive Design:**  Navigate features effortlessly with a clean and organized layout.
 
  - **Responsive Controls:**  Enjoy smooth interactions and immediate feedback during customization.
 
- **Additional Features:**  
  - **Temporary File Management:**  Automatically handles temporary files to keep your workspace clean.
 
  - **Error Handling:**  Provides informative messages and warnings to guide users through any issues.


---


## Installation 

### Prerequisites 

Before installing TokenTally, ensure that your system meets the following requirements:
 
- **Operating System:**  Windows, macOS, or Linux
 
- **Python:**  Version 3.7 or higher
 
- **Python Package Manager:**  `pip`

### Installation Steps 
 
1. **Clone the Repository** 
Begin by cloning the TokenTally repository to your local machine using Git:


```bash
git clone https://github.com/Flaxcon/TokenTally.git
```

Alternatively, you can download the repository as a ZIP file and extract it.
 
2. **Navigate to the Project Directory** 

```bash
cd TokenTally
```
 
3. **Create a Virtual Environment (Optional but Recommended)** 
It's good practice to use a virtual environment to manage dependencies.


```bash
python3 -m venv venv
```

Activate the virtual environment:
 
  - **Windows:** 

```bash
venv\Scripts\activate
```
 
  - **macOS/Linux:** 

```bash
source venv/bin/activate
```
 
4. **Install Dependencies** Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```
**Note:**  If a `requirements.txt` file is not provided, you can install the necessary packages manually:

```bash
pip install PyQt5
```
 
5. **Run the Application** 
Launch TokenTally by running the main script:


```bash
python token_tally.py
```
Replace `token_tally.py` with the actual name of your main Python file if different.


---


## Usage 

Once installed, follow these steps to use TokenTally effectively.

### Launching the Application 

After installation, launch the application using the following command:


```bash
python token_tally.py
```

Upon successful launch, the TokenTally interface will appear, ready for image processing tasks.

### Importing Images 

TokenTally offers multiple methods to import images:
 
1. **File Selection:**  
  - Click the **"Select Image File"**  button.
 
  - Browse and select an image file (supports `.png`, `.jpg`, `.jpeg`, `.webp`).
 
2. **Drag-and-Drop:** 
  - Drag an image file from your file explorer and drop it onto the designated area in the application.
 
3. **Clipboard Support:** 
  - Copy an image to your clipboard.
 
  - Right-click within the application and select **"Paste Image"**  from the context menu.

### Selecting Operational Mode 

TokenTally operates in two distinct modes:
 
1. **Cropping Mode:**  
  - **Purpose:**  Precisely crop images into circular shapes with adjustable panning and zooming.
 
  - **Features:** 
    - Interactive panning by clicking and dragging the image.

    - Zoom in and out using the mouse wheel for detailed cropping.

    - Gradient circle around the cropped image with customizable colors.
 
2. **Conversion Mode:**  
  - **Purpose:**  General image processing without the cropping feature.
 
  - **Features:** 
    - Customize output dimensions, DPI, and batch numbering.

    - Apply text overlays without cropping.
**Switching Modes:**  
  - Navigate to the **"Mode Selection"**  section.
 
  - Choose between **"Cropping Mode"**  and **"Conversion Mode"**  by selecting the corresponding radio button.

### Customizing Overlays 

Enhance your images by adding customizable text overlays:
 
1. **Adding Text:**  
  - Locate the **"Overlay Settings"**  section.
 
  - Enter your desired text in the **"Overlay Text"**  field (maximum 10 characters).
 
2. **Adjusting Font Size:**  
  - Use the **"Font Size"**  spin box to set the desired size of the overlay text.
 
3. **Choosing Font Color:**  
  - Click the **"Choose Font Color"**  button.

  - Select your preferred color from the color picker dialog.
 
4. **Positioning Text:**  
  - Use the arrow buttons (**←** , **→** , **↑** , **↓** ) to move the text overlay to the desired position on the image.
**Conditional Numbering:**  
  - **If `Overlay Text` is exactly "1":** 
    - During batch processing, only the batch numbers (1-5) will appear on the images.
 
  - **If `Overlay Text` is anything else:** 
    - Batch numbers will be appended to the overlay text (e.g., "Token 1", "Token 2").

### Gradient Circle Customization 

Add a personalized gradient circle around your images:
 
1. **Selecting Gradient Start Color:**  
  - Navigate to the **"Gradient Settings"**  section.
 
  - Click the **"Choose Gradient Start Color"**  button.

  - Select your desired start color from the color picker.
 
2. **Selecting Gradient End Color:**  
  - Click the **"Choose Gradient End Color"**  button.

  - Select your desired end color from the color picker.
**Real-Time Preview:** 
  - The gradient circle around the image will update in real-time to reflect your color selections.

### Output Settings 

Configure how your images will be saved:
 
1. **Dimensions & DPI:**  
  - **Output Width (px):**  Set the desired width of the saved image in pixels.
 
  - **Output Height (px):**  Set the desired height of the saved image in pixels.
 
  - **Output DPI:**  Define the resolution (dots per inch) for the saved image.
**Note:**  In **Cropping Mode** , the dimensions are fixed to 200x200 pixels and DPI settings are disabled.
 
2. **Batch Numbering:**  
  - **Batch Start Number:**  Specify the starting number for batch processing.
 
  - **Batch End Number:**  Specify the ending number for batch processing.
**Numbering Behavior:**  
  - **Overlay Text is "1":**  Images will display only the batch numbers (e.g., "1", "2", "3").
 
  - **Overlay Text is anything else:**  Batch numbers will be appended to the overlay text (e.g., "Token 1", "Token 2").
 
3. **Save Directory Selection:**  
  - Click the **"Select Save Directory"**  button.

  - Choose the folder where you want the processed images to be saved.

### Saving Images 

Once all settings are configured, proceed to save your images:
 
1. **Single Image Save:**  
  - Ensure that **Batch Start Number**  and **Batch End Number**  are set to the same value.
 
  - Click the **"Save as PNG"**  button.

  - The image will be saved with the specified overlay text.
 
2. **Batch Image Save:**  
  - Set different values for **Batch Start Number**  and **Batch End Number**  (e.g., Start: 1, End: 5).
 
  - Click the **"Save as PNG"**  button.
 
  - **If Overlay Text is "1":**  Images will be saved with overlay texts "1" to "5".
 
  - **If Overlay Text is "Token":**  Images will be saved with overlay texts "Token 1" to "Token 5".
 
3. **Completion Notification:** 
  - After saving, a confirmation dialog will appear, indicating the range of saved images and their save location.


---


## Troubleshooting 

Encountering issues? Here are some common problems and their solutions:
 
- **All Batch Images Display the Same Number:**  
  - **Cause:**  The overlay text is set to "1", which triggers the numbering logic to use only batch numbers.
 
  - **Solution:**  Ensure that the overlay text is set appropriately based on your desired numbering behavior.
 
- **Application Fails to Save Images:**  
  - **Cause:**  Possible write permissions in the selected save directory or invalid file paths.
 
  - **Solution:**  Verify that you have write permissions to the chosen directory and that the path is valid.
 
- **Images Not Displaying Properly:**  
  - **Cause:**  Unsupported image formats or corrupted files.
 
  - **Solution:**  Use supported formats (`.png`, `.jpg`, `.jpeg`, `.webp`) and ensure that the images are not corrupted.
 
- **Application Crashes or Freezes:**  
  - **Cause:**  Insufficient system resources or bugs in the application.
 
  - **Solution:**  Ensure your system meets the prerequisites and consider updating Python and PyQt5 to the latest versions.
 
- **Gradient Colors Not Applying:**  
  - **Cause:**  Issues with color selection or rendering.
 
  - **Solution:**  Re-select gradient colors using the provided buttons and ensure that color values are valid.


---


## Contributing 

We welcome contributions from the community! If you'd like to contribute to TokenTally, please follow these guidelines:
 
1. **Fork the Repository** Click the **"Fork"**  button at the top-right corner of the repository page to create a copy in your GitHub account.
 
2. **Clone Your Fork** 

```bash
git clone https://github.com/your-username/TokenTally.git
cd TokenTally
```
 
3. **Create a New Branch** 

```bash
git checkout -b feature/YourFeatureName
```
 
4. **Make Your Changes** 
Implement your feature or bug fix.
 
5. **Commit Your Changes** 

```bash
git add .
git commit -m "Description of your changes"
```
 
6. **Push to Your Fork** 

```bash
git push origin feature/YourFeatureName
```
 
7. **Create a Pull Request** Navigate to your fork on GitHub and click the **"Compare & pull request"**  button. Provide a clear description of your changes and submit the pull request.
**Please ensure that your contributions adhere to the project's coding standards and include appropriate documentation and tests.** 

---


## License 
Distributed under the [MIT License]() .

---


## Acknowledgements 
 
- [PyQt5]()  - Python bindings for the Qt application framework.
 
- [Python](https://www.python.org/)  - The programming language used for development.
 
- [GitHub](https://github.com/)  - Hosting platform for version control and collaboration.


---

**Thought for 4 seconds
Sure, here's the previous response in markdown format:

# TokenTally - Advanced Image Numbering and Customization Tool 
![TokenTally Logo](https://github.com/Flaxcon/TokenTally/raw/main/logo.png) 

TokenTally is a powerful and user-friendly PyQt5-based application designed to simplify image editing and batch processing tasks. Whether you're a photographer, graphic designer, or digital artist, TokenTally offers a comprehensive set of tools to customize and manage your images with ease.

## Table of Contents 
 
- [Features](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#features)
 
- [Installation](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#installation)  
  - [Prerequisites](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#prerequisites)
 
  - [Installation Steps](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#installation-steps)
 
- [Usage](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#usage)  
  - [Launching the Application](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#launching-the-application)
 
  - [Importing Images](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#importing-images)
 
  - [Selecting Operational Mode](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#selecting-operational-mode)
 
  - [Customizing Overlays](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#customizing-overlays)
 
  - [Gradient Circle Customization](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#gradient-circle-customization)
 
  - [Output Settings](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#output-settings)
 
  - [Saving Images](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#saving-images)
 
- [Troubleshooting](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#troubleshooting)
 
- [Contributing](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#contributing)
 
- [License](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#license)
 
- [Acknowledgements](https://chatgpt.com/c/673b8c6a-aca0-8002-8d8d-48ce27041a51?model=o1-preview#acknowledgements)


---


## Features 
 
- **Flexible Image Importing:**  
  - **File Selection:**  Easily select images using an intuitive file dialog supporting PNG, JPG, and WEBP formats.
 
  - **Drag-and-Drop:**  Quickly drag images directly into the application for seamless access.
 
  - **Clipboard Support:**  Paste images directly from your clipboard for a streamlined workflow.
 
- **Dual Operational Modes:**  
  - **Cropping Mode:**  Precisely frame and crop images with interactive panning and zooming tools.
 
  - **Conversion Mode:**  Perform general image processing with customizable output settings.
 
- **Interactive Image Manipulation:**  
  - **Panning & Zooming:**  Navigate images effortlessly to focus on specific areas for detailed editing.
 
  - **Real-Time Preview:**  Instantly view changes to ensure edits meet your expectations before saving.
 
- **Customizable Overlays:**  
  - **Text Overlay:**  Add personalized text with options to adjust font size, color, and position.
 
  - **Gradient Circle Customization:**  Select and customize start and end colors for gradient circles to enhance image aesthetics.
 
- **Comprehensive Output Settings:**  
  - **Dimensions & DPI:**  Define output width, height, and DPI to match specific requirements.
 
  - **Batch Numbering:**  Automate the numbering process with customizable batch start and end options. 
    - **Conditional Numbering:** 
      - If the overlay text is exactly "1" and batch processing is active, images will display only the batch numbers (1-5).

      - If the overlay text is anything else, the batch number will be appended to the overlay text (e.g., "Token 1", "Token 2").
 
  - **Save Directory Selection:**  Choose your preferred save location with ease.
 
- **High-Quality Saving:**  
  - **PNG Format:**  Save customized images as high-quality PNG files, preserving transparency and color fidelity.
 
  - **Batch Processing:**  Efficiently process and save multiple images simultaneously, saving valuable time.
 
- **User-Friendly Interface:**  
  - **Intuitive Design:**  Navigate features effortlessly with a clean and organized layout.
 
  - **Responsive Controls:**  Enjoy smooth interactions and immediate feedback during customization.
 
- **Additional Features:**  
  - **Temporary File Management:**  Automatically handles temporary files to keep your workspace clean.
 
  - **Error Handling:**  Provides informative messages and warnings to guide users through any issues.


---


## Installation 

### Prerequisites 

Before installing TokenTally, ensure that your system meets the following requirements:
 
- **Operating System:**  Windows, macOS, or Linux
 
- **Python:**  Version 3.7 or higher
 
- **Python Package Manager:**  `pip`

### Installation Steps 
 
1. **Clone the Repository** 
Begin by cloning the TokenTally repository to your local machine using Git:


```bash
git clone https://github.com/Flaxcon/TokenTally.git
```

Alternatively, you can download the repository as a ZIP file and extract it.
 
2. **Navigate to the Project Directory** 

```bash
cd TokenTally
```
 
3. **Create a Virtual Environment (Optional but Recommended)** 
It's good practice to use a virtual environment to manage dependencies.


```bash
python3 -m venv venv
```

Activate the virtual environment:
 
  - **Windows:** 

```bash
venv\Scripts\activate
```
 
  - **macOS/Linux:** 

```bash
source venv/bin/activate
```
 
4. **Install Dependencies** Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```
**Note:**  If a `requirements.txt` file is not provided, you can install the necessary packages manually:

```bash
pip install PyQt5
```
 
5. **Run the Application** 
Launch TokenTally by running the main script:


```bash
python token_tally.py
```
Replace `token_tally.py` with the actual name of your main Python file if different.


---


## Usage 

Once installed, follow these steps to use TokenTally effectively.

### Launching the Application 

After installation, launch the application using the following command:


```bash
python token_tally.py
```

Upon successful launch, the TokenTally interface will appear, ready for image processing tasks.

### Importing Images 

TokenTally offers multiple methods to import images:
 
1. **File Selection:**  
  - Click the **"Select Image File"**  button.
 
  - Browse and select an image file (supports `.png`, `.jpg`, `.jpeg`, `.webp`).
 
2. **Drag-and-Drop:** 
  - Drag an image file from your file explorer and drop it onto the designated area in the application.
 
3. **Clipboard Support:** 
  - Copy an image to your clipboard.
 
  - Right-click within the application and select **"Paste Image"**  from the context menu.

### Selecting Operational Mode 

TokenTally operates in two distinct modes:
 
1. **Cropping Mode:**  
  - **Purpose:**  Precisely crop images into circular shapes with adjustable panning and zooming.
 
  - **Features:** 
    - Interactive panning by clicking and dragging the image.

    - Zoom in and out using the mouse wheel for detailed cropping.

    - Gradient circle around the cropped image with customizable colors.
 
2. **Conversion Mode:**  
  - **Purpose:**  General image processing without the cropping feature.
 
  - **Features:** 
    - Customize output dimensions, DPI, and batch numbering.

    - Apply text overlays without cropping.
**Switching Modes:**  
  - Navigate to the **"Mode Selection"**  section.
 
  - Choose between **"Cropping Mode"**  and **"Conversion Mode"**  by selecting the corresponding radio button.

### Customizing Overlays 

Enhance your images by adding customizable text overlays:
 
1. **Adding Text:**  
  - Locate the **"Overlay Settings"**  section.
 
  - Enter your desired text in the **"Overlay Text"**  field (maximum 10 characters).
 
2. **Adjusting Font Size:**  
  - Use the **"Font Size"**  spin box to set the desired size of the overlay text.
 
3. **Choosing Font Color:**  
  - Click the **"Choose Font Color"**  button.

  - Select your preferred color from the color picker dialog.
 
4. **Positioning Text:**  
  - Use the arrow buttons (**←** , **→** , **↑** , **↓** ) to move the text overlay to the desired position on the image.
**Conditional Numbering:**  
  - **If `Overlay Text` is exactly "1":** 
    - During batch processing, only the batch numbers (1-5) will appear on the images.
 
  - **If `Overlay Text` is anything else:** 
    - Batch numbers will be appended to the overlay text (e.g., "Token 1", "Token 2").

### Gradient Circle Customization 

Add a personalized gradient circle around your images:
 
1. **Selecting Gradient Start Color:**  
  - Navigate to the **"Gradient Settings"**  section.
 
  - Click the **"Choose Gradient Start Color"**  button.

  - Select your desired start color from the color picker.
 
2. **Selecting Gradient End Color:**  
  - Click the **"Choose Gradient End Color"**  button.

  - Select your desired end color from the color picker.
**Real-Time Preview:** 
  - The gradient circle around the image will update in real-time to reflect your color selections.

### Output Settings 

Configure how your images will be saved:
 
1. **Dimensions & DPI:**  
  - **Output Width (px):**  Set the desired width of the saved image in pixels.
 
  - **Output Height (px):**  Set the desired height of the saved image in pixels.
 
  - **Output DPI:**  Define the resolution (dots per inch) for the saved image.
**Note:**  In **Cropping Mode** , the dimensions are fixed to 200x200 pixels and DPI settings are disabled.
 
2. **Batch Numbering:**  
  - **Batch Start Number:**  Specify the starting number for batch processing.
 
  - **Batch End Number:**  Specify the ending number for batch processing.
**Numbering Behavior:**  
  - **Overlay Text is "1":**  Images will display only the batch numbers (e.g., "1", "2", "3").
 
  - **Overlay Text is anything else:**  Batch numbers will be appended to the overlay text (e.g., "Token 1", "Token 2").
 
3. **Save Directory Selection:**  
  - Click the **"Select Save Directory"**  button.

  - Choose the folder where you want the processed images to be saved.

### Saving Images 

Once all settings are configured, proceed to save your images:
 
1. **Single Image Save:**  
  - Ensure that **Batch Start Number**  and **Batch End Number**  are set to the same value.
 
  - Click the **"Save as PNG"**  button.

  - The image will be saved with the specified overlay text.
 
2. **Batch Image Save:**  
  - Set different values for **Batch Start Number**  and **Batch End Number**  (e.g., Start: 1, End: 5).
 
  - Click the **"Save as PNG"**  button.
 
  - **If Overlay Text is "1":**  Images will be saved with overlay texts "1" to "5".
 
  - **If Overlay Text is "Token":**  Images will be saved with overlay texts "Token 1" to "Token 5".
 
3. **Completion Notification:** 
  - After saving, a confirmation dialog will appear, indicating the range of saved images and their save location.


---


## Troubleshooting 

Encountering issues? Here are some common problems and their solutions:
 
- **All Batch Images Display the Same Number:**  
  - **Cause:**  The overlay text is set to "1", which triggers the numbering logic to use only batch numbers.
 
  - **Solution:**  Ensure that the overlay text is set appropriately based on your desired numbering behavior.
 
- **Application Fails to Save Images:**  
  - **Cause:**  Possible write permissions in the selected save directory or invalid file paths.
 
  - **Solution:**  Verify that you have write permissions to the chosen directory and that the path is valid.
 
- **Images Not Displaying Properly:**  
  - **Cause:**  Unsupported image formats or corrupted files.
 
  - **Solution:**  Use supported formats (`.png`, `.jpg`, `.jpeg`, `.webp`) and ensure that the images are not corrupted.
 
- **Application Crashes or Freezes:**  
  - **Cause:**  Insufficient system resources or bugs in the application.
 
  - **Solution:**  Ensure your system meets the prerequisites and consider updating Python and PyQt5 to the latest versions.
 
- **Gradient Colors Not Applying:**  
  - **Cause:**  Issues with color selection or rendering.
 
  - **Solution:**  Re-select gradient colors using the provided buttons and ensure that color values are valid.


---
