import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QFileDialog, QLineEdit, QColorDialog, QSpinBox,
    QMessageBox, QGroupBox, QFormLayout
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QPainter, QColor, QFont


class ImageDropLabel(QLabel):
    image_dropped = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAlignment(Qt.AlignCenter)
        self.setText('Image Preview Will Appear Here')
        self.setAcceptDrops(True)
        print("Initialized ImageDropLabel")

    def dragEnterEvent(self, event):
        print("Drag Enter Event")
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            print(f"Dragged URLs: {urls}")
            if len(urls) == 1:
                url = urls[0]
                if url.isLocalFile():
                    file_path = url.toLocalFile()
                    if file_path.lower().endswith(('.webp', '.png', '.jpg', '.jpeg')):
                        event.acceptProposedAction()
                        print("Accepted image file")
                    else:
                        event.ignore()
                        print("Ignored non-image file")
                else:
                    event.ignore()
                    print("Ignored non-local file")
            else:
                event.ignore()
                print("Ignored multiple files")
        else:
            event.ignore()
            print("Ignored non-URL drag")

    def dropEvent(self, event):
        print("Drop Event")
        if event.mimeData().hasUrls():
            url = event.mimeData().urls()[0]
            if url.isLocalFile():
                file_path = url.toLocalFile()
                print(f"Dropped file path: {file_path}")
                if file_path.lower().endswith(('.webp', '.png', '.jpg', '.jpeg')):
                    self.image_dropped.emit(file_path)
                    print("Emitted image_dropped signal")
                else:
                    print("Dropped file is not a supported image")
            else:
                print("Dropped file is not a local file")
        else:
            event.ignore()
            print("Ignored non-URL drop")


class ImageToPNGConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image to PNG Converter with Overlay")
        self.setGeometry(100, 100, 800, 900)
        self.setFixedSize(800, 900)

        # Initialize variables
        self.image_path = None
        self.original_pixmap = None  # QPixmap
        self.modified_pixmap = None  # QPixmap
        self.overlay_text = ""
        self.font_size = 36
        self.font_color = QColor(255, 255, 255)  # White by default

        # Position variables
        self.padding = 10  # Initial padding from the edges
        self.x_offset = 0  # Horizontal offset from default position
        self.y_offset = 0  # Vertical offset from default position
        self.step = 5  # Pixels to move per arrow press

        # Batch processing variables
        self.batch_start = 1
        self.batch_end = 1

        # Save directory
        self.save_directory = None  # If None, save to original image directory

        # Output dimensions
        self.output_width = 200
        self.output_height = 200
        self.output_dpi = 96  # Dots Per Inch

        # Setup UI
        self.setup_ui()

    def setup_ui(self):
        # Main layout
        main_layout = QVBoxLayout()

        # File Picker Layout
        file_picker_layout = QHBoxLayout()
        self.select_button = QPushButton("Select Image File")
        self.select_button.clicked.connect(self.open_file_dialog)
        file_picker_layout.addWidget(self.select_button)
        self.file_label = QLabel("No file selected.")
        self.file_label.setStyleSheet("font-weight: bold;")
        file_picker_layout.addWidget(self.file_label)
        main_layout.addLayout(file_picker_layout)

        # Image Display
        self.image_label = ImageDropLabel()
        self.image_label.setFixedSize(760, 400)
        self.image_label.setStyleSheet("border: 2px dashed #aaa;")
        self.image_label.image_dropped.connect(self.handle_dropped_image)
        main_layout.addWidget(self.image_label, alignment=Qt.AlignCenter)

        # Overlay Settings Group
        overlay_group = QGroupBox("Overlay Settings")
        overlay_layout = QFormLayout()

        # Overlay Text Input
        self.text_input = QLineEdit()
        self.text_input.setMaxLength(2)
        self.text_input.textChanged.connect(self.update_overlay_text)
        overlay_layout.addRow("Enter 1 or 2 Digits:", self.text_input)

        # Font Size Selector
        self.font_size_spin = QSpinBox()
        self.font_size_spin.setRange(10, 100)
        self.font_size_spin.setValue(self.font_size)
        self.font_size_spin.valueChanged.connect(self.update_font_size)
        overlay_layout.addRow("Font Size:", self.font_size_spin)

        # Font Color Picker
        self.color_button = QPushButton("Choose Font Color")
        self.color_button.clicked.connect(self.choose_color)
        self.color_button.setStyleSheet(f"background-color: {self.font_color.name()}")
        overlay_layout.addRow("Font Color:", self.color_button)

        # Add form layout to group
        overlay_group.setLayout(overlay_layout)
        main_layout.addWidget(overlay_group)

        # Repositioning Buttons Group
        reposition_group = QGroupBox("Reposition Overlay")
        reposition_layout = QHBoxLayout()

        # Up Button
        self.up_button = QPushButton("↑")
        self.up_button.clicked.connect(self.move_up)
        reposition_layout.addWidget(self.up_button)

        # Down Button
        self.down_button = QPushButton("↓")
        self.down_button.clicked.connect(self.move_down)
        reposition_layout.addWidget(self.down_button)

        # Left Button
        self.left_button = QPushButton("←")
        self.left_button.clicked.connect(self.move_left)
        reposition_layout.addWidget(self.left_button)

        # Right Button
        self.right_button = QPushButton("→")
        self.right_button.clicked.connect(self.move_right)
        reposition_layout.addWidget(self.right_button)

        reposition_group.setLayout(reposition_layout)
        main_layout.addWidget(reposition_group, alignment=Qt.AlignCenter)

        # Batch Processing Group
        batch_group = QGroupBox("Batch Overlay Settings")
        batch_layout = QFormLayout()

        # Start Number
        self.batch_start_spin = QSpinBox()
        self.batch_start_spin.setRange(1, 9999)
        self.batch_start_spin.setValue(1)
        batch_layout.addRow("Start Number:", self.batch_start_spin)

        # End Number
        self.batch_end_spin = QSpinBox()
        self.batch_end_spin.setRange(1, 9999)
        self.batch_end_spin.setValue(1)
        batch_layout.addRow("End Number:", self.batch_end_spin)

        batch_group.setLayout(batch_layout)
        main_layout.addWidget(batch_group)

        # Output Settings Group
        output_group = QGroupBox("Output Settings")
        output_layout = QFormLayout()

        # Output Width
        self.output_width_spin = QSpinBox()
        self.output_width_spin.setRange(50, 5000)
        self.output_width_spin.setValue(self.output_width)
        self.output_width_spin.valueChanged.connect(self.update_output_dimensions)
        output_layout.addRow("Output Width (px):", self.output_width_spin)

        # Output Height
        self.output_height_spin = QSpinBox()
        self.output_height_spin.setRange(50, 5000)
        self.output_height_spin.setValue(self.output_height)
        self.output_height_spin.valueChanged.connect(self.update_output_dimensions)
        output_layout.addRow("Output Height (px):", self.output_height_spin)

        # Output DPI
        self.output_dpi_spin = QSpinBox()
        self.output_dpi_spin.setRange(72, 600)
        self.output_dpi_spin.setValue(self.output_dpi)
        self.output_dpi_spin.valueChanged.connect(self.update_output_dpi)
        output_layout.addRow("Output DPI:", self.output_dpi_spin)

        output_group.setLayout(output_layout)
        main_layout.addWidget(output_group)

        # Save Directory Selection
        save_dir_layout = QHBoxLayout()
        self.save_dir_button = QPushButton("Select Save Directory")
        self.save_dir_button.clicked.connect(self.select_save_directory)
        save_dir_layout.addWidget(self.save_dir_button)
        self.save_dir_label = QLabel("Saving to original directory.")
        save_dir_layout.addWidget(self.save_dir_label)
        main_layout.addLayout(save_dir_layout)

        # Save Button
        self.save_button = QPushButton("Save as PNG")
        self.save_button.setEnabled(False)
        self.save_button.clicked.connect(self.save_image)
        main_layout.addWidget(self.save_button, alignment=Qt.AlignRight)

        self.setLayout(main_layout)

    def handle_dropped_image(self, file_path):
        if not file_path.lower().endswith(('.webp', '.png', '.jpg', '.jpeg')):
            QMessageBox.critical(self, "Invalid File", "Please drop a valid image file (.webp, .png, .jpg, .jpeg).")
            return
        self.image_path = file_path
        self.file_label.setText(os.path.basename(file_path))
        self.load_image()
        self.save_button.setEnabled(True)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        # Allow selection of .webp, .png, .jpg, and .jpeg files
        file_filter = "Image Files (*.webp *.png *.jpg *.jpeg);;All Files (*)"
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select an Image File",
            "",
            file_filter,
            options=options
        )
        if file_path:
            if not file_path.lower().endswith(('.webp', '.png', '.jpg', '.jpeg')):
                QMessageBox.critical(self, "Invalid File", "Please select a valid image file (.webp, .png, .jpg, .jpeg).")
                return
            self.image_path = file_path
            self.file_label.setText(os.path.basename(file_path))
            self.load_image()
            self.save_button.setEnabled(True)

    def load_image(self):
        try:
            # Load image as QPixmap
            pixmap = QPixmap(self.image_path)
            if pixmap.isNull():
                raise ValueError("Failed to load image. The file may be corrupted or unsupported.")
            # Resize pixmap to output dimensions while keeping aspect ratio
            self.original_pixmap = pixmap.scaled(
                self.output_width,
                self.output_height,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.modified_pixmap = self.original_pixmap.copy()
            self.image_label.setPixmap(self.modified_pixmap)
            self.image_label.setText("")
            # Do NOT reset position offsets to maintain overlay position
            # Reset batch settings
            self.batch_start_spin.setValue(1)
            self.batch_end_spin.setValue(1)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load image.\n{e}")
            self.image_label.setText("Image Preview Will Appear Here")
            self.save_button.setEnabled(False)

    def update_overlay_text(self, text):
        if len(text) > 2:
            self.text_input.setText(text[:2])
            return
        self.overlay_text = text
        self.apply_overlay()
        self.display_image()

    def update_font_size(self, size):
        self.font_size = size
        self.apply_overlay()
        self.display_image()

    def choose_color(self):
        color = QColorDialog.getColor(initial=self.font_color, title="Select Font Color")
        if color.isValid():
            self.font_color = color
            self.color_button.setStyleSheet(f"background-color: {self.font_color.name()}")
            self.apply_overlay()
            self.display_image()

    def update_output_dimensions(self):
        self.output_width = self.output_width_spin.value()
        self.output_height = self.output_height_spin.value()
        # If an image is already loaded, resize it accordingly
        if self.original_pixmap:
            self.original_pixmap = self.original_pixmap.scaled(
                self.output_width,
                self.output_height,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.modified_pixmap = self.original_pixmap.copy()
            self.apply_overlay()
            self.display_image()

    def update_output_dpi(self):
        self.output_dpi = self.output_dpi_spin.value()

    def apply_overlay(self):
        if not self.original_pixmap:
            return
        # Start with original pixmap
        self.modified_pixmap = self.original_pixmap.copy()

        if self.overlay_text:
            painter = QPainter(self.modified_pixmap)
            try:
                painter.setRenderHint(QPainter.Antialiasing)
                # Set font
                font = QFont("Arial", self.font_size)
                painter.setFont(font)
                # Set color
                painter.setPen(self.font_color)
                # Calculate position: Bottom Right with padding and offset
                metrics = painter.fontMetrics()
                text_width = metrics.horizontalAdvance(self.overlay_text)
                text_height = metrics.height()
                x = self.modified_pixmap.width() - text_width - self.padding + self.x_offset
                y = self.modified_pixmap.height() - self.padding + self.y_offset
                # Ensure text is within image boundaries
                x = max(0, min(x, self.modified_pixmap.width() - text_width))
                y = max(text_height, min(y, self.modified_pixmap.height()))
                # Draw text
                painter.drawText(x, y, self.overlay_text)
            except Exception as e:
                QMessageBox.critical(self, "Drawing Error", f"Failed to draw text on image.\n{e}")
            finally:
                painter.end()

    def display_image(self):
        if self.modified_pixmap:
            self.image_label.setPixmap(self.modified_pixmap)
        else:
            self.image_label.setText("Image Preview Will Appear Here")

    def move_up(self):
        self.y_offset -= self.step
        self.apply_overlay()
        self.display_image()

    def move_down(self):
        self.y_offset += self.step
        self.apply_overlay()
        self.display_image()

    def move_left(self):
        self.x_offset -= self.step
        self.apply_overlay()
        self.display_image()

    def move_right(self):
        self.x_offset += self.step
        self.apply_overlay()
        self.display_image()

    def select_save_directory(self):
        directory = QFileDialog.getExistingDirectory(
            self,
            "Select Directory",
            "",
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )
        if directory:
            self.save_directory = directory
            self.save_dir_label.setText(directory)

    def save_image(self):
        if not self.original_pixmap:
            QMessageBox.warning(self, "No Image", "There is no image to save.")
            return

        # Get batch range
        start_num = self.batch_start_spin.value()
        end_num = self.batch_end_spin.value()

        if start_num > end_num:
            QMessageBox.critical(self, "Invalid Range", "Start Number must be less than or equal to End Number.")
            return

        # Get base filename without extension
        base_name = os.path.splitext(os.path.basename(self.image_path))[0]

        # Determine save directory
        save_dir = self.save_directory if self.save_directory else os.path.dirname(self.image_path)

        # Iterate over the range and save each image
        for num in range(start_num, end_num + 1):
            if not self.overlay_text:
                # If no overlay text, save original image with number appended
                modified_pixmap = self.original_pixmap.copy()
            else:
                # Create a copy for each number
                modified_pixmap = self.original_pixmap.copy()
                painter = QPainter(modified_pixmap)
                try:
                    painter.setRenderHint(QPainter.Antialiasing)
                    # Set font
                    font = QFont("Arial", self.font_size)
                    painter.setFont(font)
                    # Set color
                    painter.setPen(self.font_color)
                    # Prepare text
                    text = str(num)
                    # Calculate position
                    metrics = painter.fontMetrics()
                    text_width = metrics.horizontalAdvance(text)
                    text_height = metrics.height()
                    x = modified_pixmap.width() - text_width - self.padding + self.x_offset
                    y = modified_pixmap.height() - self.padding + self.y_offset
                    # Ensure text is within image boundaries
                    x = max(0, min(x, modified_pixmap.width() - text_width))
                    y = max(text_height, min(y, modified_pixmap.height()))
                    # Draw text
                    painter.drawText(x, y, text)
                except Exception as e:
                    QMessageBox.critical(self, "Drawing Error", f"Failed to draw text on image {num}.\n{e}")
                    painter.end()
                    continue  # Skip saving this image
                finally:
                    painter.end()

            # Resize to output dimensions
            resized_pixmap = modified_pixmap.scaled(
                self.output_width,
                self.output_height,
                Qt.IgnoreAspectRatio,
                Qt.SmoothTransformation
            )

            # Convert QPixmap to QImage to set DPI
            image = resized_pixmap.toImage()
            image.setDotsPerMeterX(int(self.output_dpi * 39.3701))  # 1 inch = 39.3701 meters
            image.setDotsPerMeterY(int(self.output_dpi * 39.3701))

            # Define output path
            output_filename = f"{base_name}{num}.png"
            output_path = os.path.join(save_dir, output_filename)

            # Save as PNG with DPI
            success = image.save(output_path, "PNG")
            if not success:
                QMessageBox.critical(self, "Save Failed", f"Failed to save image {output_filename}.")
                continue

        QMessageBox.information(self, "Success", f"Images saved from {start_num} to {end_num} in {save_dir}")


def main():
    app = QApplication(sys.argv)
    converter = ImageToPNGConverter()
    converter.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
