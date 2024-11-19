import sys
import os
import tempfile
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QFileDialog, QLineEdit, QColorDialog, QSpinBox,
    QMessageBox, QGroupBox, QFormLayout, QMenu, QAction, QSizePolicy,
    QRadioButton, QScrollArea
)
from PyQt5.QtCore import Qt, pyqtSignal, QRectF, QPointF, QTimer
from PyQt5.QtGui import (
    QPixmap, QPainter, QColor, QFont, QClipboard, QPainterPath,
    QBrush, QPen, QLinearGradient, QImage, QTransform
)


class ImageDropLabel(QLabel):
    image_dropped = pyqtSignal(str)
    image_pasted = pyqtSignal(str)
    transformation_changed = pyqtSignal()

    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window  # Reference to the main window
        self.setAlignment(Qt.AlignCenter)
        self.setAcceptDrops(True)
        self.setMouseTracking(True)

        # For panning
        self.setCursor(Qt.OpenHandCursor)
        self.is_panning = False
        self.last_mouse_pos = QPointF()

        # Image manipulation variables
        self.scale_factor = 1.0
        self.translation = QPointF(0, 0)

        # Set initial size
        self.update_preview_size()

        # Adjust size policy
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

    def update_preview_size(self):
        if self.main_window.mode == "cropping":
            self.setFixedSize(200, 200)
            self.setStyleSheet("border: 2px dashed #aaa; background-color: #fff;")
        else:
            self.setFixedSize(self.main_window.output_width, self.main_window.output_height)
            self.setStyleSheet("border: 1px solid #aaa; background-color: #fff;")
        self.update()

    def set_pixmap(self, pixmap):
        self.main_window.original_pixmap = pixmap
        self.scale_factor = 1.0
        self.translation = QPointF(0, 0)
        self.update()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if len(urls) == 1:
                url = urls[0]
                if url.isLocalFile():
                    file_path = url.toLocalFile()
                    if file_path.lower().endswith(('.webp', '.png', '.jpg', '.jpeg')):
                        event.acceptProposedAction()
                        return
                else:
                    event.acceptProposedAction()
                    return
        event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            url = event.mimeData().urls()[0]
            if url.isLocalFile():
                file_path = url.toLocalFile()
                if file_path.lower().endswith(('.webp', '.png', '.jpg', '.jpeg')):
                    self.image_dropped.emit(file_path)
                    return
            else:
                image_data = event.mimeData().data('application/octet-stream')
                if image_data:
                    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
                    temp_file.write(image_data)
                    temp_file.close()
                    self.image_dropped.emit(temp_file.name)
                    return
        event.ignore()

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        paste_action = QAction("Paste Image", self)
        paste_action.triggered.connect(self.paste_image)
        menu.addAction(paste_action)
        menu.exec_(event.globalPos())

    def paste_image(self):
        clipboard = QApplication.clipboard()
        mime_data = clipboard.mimeData()
        if mime_data.hasImage():
            image = clipboard.image()
            if not image.isNull():
                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
                image.save(temp_file.name, "PNG")
                temp_file.close()
                self.image_pasted.emit(temp_file.name)
            else:
                QMessageBox.warning(self, "Paste Error", "Failed to paste image from clipboard.")
        else:
            QMessageBox.warning(self, "Paste Error", "Clipboard does not contain an image.")

    def mousePressEvent(self, event):
        if self.main_window.mode == "cropping":
            if event.button() == Qt.LeftButton and self.main_window.original_pixmap:
                self.setCursor(Qt.ClosedHandCursor)
                self.is_panning = True
                self.last_mouse_pos = event.pos() - self.translation

    def mouseMoveEvent(self, event):
        if self.main_window.mode == "cropping":
            if self.is_panning and self.main_window.original_pixmap:
                self.translation = event.pos() - self.last_mouse_pos
                self.update()
                self.transformation_changed.emit()

    def mouseReleaseEvent(self, event):
        if self.main_window.mode == "cropping":
            if event.button() == Qt.LeftButton and self.main_window.original_pixmap:
                self.setCursor(Qt.OpenHandCursor)
                self.is_panning = False

    def wheelEvent(self, event):
        if self.main_window.mode == "cropping":
            if self.main_window.original_pixmap:
                angle = event.angleDelta().y()
                factor = 1.15 if angle > 0 else 0.85
                self.scale_factor *= factor
                self.scale_factor = max(0.1, min(self.scale_factor, 10))
                self.update()
                self.transformation_changed.emit()

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.main_window.original_pixmap:
            rendered_pixmap = self.main_window.render_image(
                self.width(), self.height(), self.main_window.overlay_text, preview=True
            )
            painter.drawPixmap(0, 0, rendered_pixmap)
        else:
            painter.fillRect(self.rect(), Qt.white)
            painter.setPen(Qt.black)
            painter.drawText(self.rect(), Qt.AlignCenter, "Image Preview Will Appear Here")


class ImageToPNGConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TokenTally - Token Numbering Tool")
        self.setGeometry(100, 100, 400, 800)  # Increased height to accommodate new settings
        self.setMinimumSize(400, 800)

        # Initialize variables
        self.image_path = None
        self.original_pixmap = None
        self.overlay_text = ""
        self.font_size = 36
        self.font_color = QColor(255, 255, 255)
        self.overlay_x_offset = 0
        self.overlay_y_offset = 0
        self.batch_start_spin = QSpinBox()
        self.batch_end_spin = QSpinBox()
        self.batch_start = 1
        self.batch_end = 1
        self.save_directory = None
        self.output_width = 200
        self.output_height = 200
        self.output_dpi = 96
        self.scale_factor = 1.0
        self.translation = QPointF(0, 0)
        self.temp_files = []
        self.mode = "cropping"

        # Initialize gradient colors
        self.gradient_start_color = QColor(255, 255, 255, 0)  # Transparent white
        self.gradient_end_color = QColor(0, 0, 0, 255)        # Opaque black

        # Setup UI
        self.setup_ui()

    def setup_ui(self):
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

        # Mode Selection
        mode_group = QGroupBox("Mode Selection")
        mode_layout = QHBoxLayout()
        self.cropping_mode_radio = QRadioButton("Cropping Mode")
        self.cropping_mode_radio.setChecked(True)
        self.cropping_mode_radio.toggled.connect(self.change_mode)
        self.conversion_mode_radio = QRadioButton("Conversion Mode")
        mode_layout.addWidget(self.cropping_mode_radio)
        mode_layout.addWidget(self.conversion_mode_radio)
        mode_group.setLayout(mode_layout)
        main_layout.addWidget(mode_group)

        # Image Display
        self.image_label = ImageDropLabel(self)
        self.image_label.image_dropped.connect(self.handle_dropped_image)
        self.image_label.image_pasted.connect(self.handle_pasted_image)
        self.image_label.transformation_changed.connect(self.update_preview)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setAlignment(Qt.AlignCenter)
        scroll_area.setWidget(self.image_label)
        main_layout.addWidget(scroll_area)

        # Overlay Settings Group
        self.overlay_group = QGroupBox("Overlay Settings")
        overlay_layout = QFormLayout()
        self.text_input = QLineEdit()
        self.text_input.setMaxLength(10)
        self.text_input.textChanged.connect(self.update_overlay_text)
        overlay_layout.addRow("Overlay Text:", self.text_input)
        self.font_size_spin = QSpinBox()
        self.font_size_spin.setRange(10, 100)
        self.font_size_spin.setValue(self.font_size)
        self.font_size_spin.valueChanged.connect(self.update_font_size)
        overlay_layout.addRow("Font Size:", self.font_size_spin)
        self.color_button = QPushButton("Choose Font Color")
        self.color_button.clicked.connect(self.choose_color)
        self.color_button.setStyleSheet(f"background-color: {self.font_color.name()}")
        overlay_layout.addRow("Font Color:", self.color_button)
        position_layout = QHBoxLayout()
        self.left_button = QPushButton("\u2190")
        self.left_button.pressed.connect(lambda: self.start_moving_overlay("left"))
        self.right_button = QPushButton("\u2192")
        self.right_button.pressed.connect(lambda: self.start_moving_overlay("right"))
        self.up_button = QPushButton("\u2191")
        self.up_button.pressed.connect(lambda: self.start_moving_overlay("up"))
        self.down_button = QPushButton("\u2193")
        self.down_button.pressed.connect(lambda: self.start_moving_overlay("down"))
        for btn in [self.left_button, self.right_button, self.up_button, self.down_button]:
            btn.released.connect(self.stop_moving_overlay)
        position_layout.addWidget(self.left_button)
        position_layout.addWidget(self.right_button)
        position_layout.addWidget(self.up_button)
        position_layout.addWidget(self.down_button)
        overlay_layout.addRow("Move Text:", position_layout)
        self.overlay_group.setLayout(overlay_layout)
        main_layout.addWidget(self.overlay_group)

        # Gradient Settings Group
        self.gradient_group = QGroupBox("Gradient Settings")
        gradient_layout = QFormLayout()
        self.gradient_start_button = QPushButton("Choose Gradient Start Color")
        self.gradient_start_button.clicked.connect(self.choose_gradient_start_color)
        self.gradient_start_button.setStyleSheet(f"background-color: {self.gradient_start_color.name()}")
        gradient_layout.addRow("Start Color:", self.gradient_start_button)
        self.gradient_end_button = QPushButton("Choose Gradient End Color")
        self.gradient_end_button.clicked.connect(self.choose_gradient_end_color)
        self.gradient_end_button.setStyleSheet(f"background-color: {self.gradient_end_color.name()}")
        gradient_layout.addRow("End Color:", self.gradient_end_button)
        self.gradient_group.setLayout(gradient_layout)
        main_layout.addWidget(self.gradient_group)

        # Output Settings Group
        self.output_group = QGroupBox("Output Settings")
        output_layout = QFormLayout()
        self.output_width_spin = QSpinBox()
        self.output_width_spin.setRange(50, 5000)
        self.output_width_spin.setValue(self.output_width)
        self.output_width_spin.valueChanged.connect(self.update_output_dimensions)
        output_layout.addRow("Output Width (px):", self.output_width_spin)
        self.output_height_spin = QSpinBox()
        self.output_height_spin.setRange(50, 5000)
        self.output_height_spin.setValue(self.output_height)
        self.output_height_spin.valueChanged.connect(self.update_output_dimensions)
        output_layout.addRow("Output Height (px):", self.output_height_spin)
        self.output_dpi_spin = QSpinBox()
        self.output_dpi_spin.setRange(72, 600)
        self.output_dpi_spin.setValue(self.output_dpi)
        self.output_dpi_spin.valueChanged.connect(self.update_output_dpi)
        output_layout.addRow("Output DPI:", self.output_dpi_spin)
        self.batch_start_spin.setRange(1, 9999)
        self.batch_start_spin.setValue(self.batch_start)
        output_layout.addRow("Batch Start Number:", self.batch_start_spin)
        self.batch_end_spin.setRange(1, 9999)
        self.batch_end_spin.setValue(self.batch_end)
        output_layout.addRow("Batch End Number:", self.batch_end_spin)
        self.save_dir_button = QPushButton("Select Save Directory")
        self.save_dir_button.clicked.connect(self.select_save_directory)
        output_layout.addRow("Save Directory:", self.save_dir_button)
        self.output_group.setLayout(output_layout)
        main_layout.addWidget(self.output_group)

        # Save Button
        self.save_button = QPushButton("Save as PNG")
        self.save_button.setEnabled(False)
        self.save_button.clicked.connect(self.save_image)
        main_layout.addWidget(self.save_button, alignment=Qt.AlignRight)
        self.setLayout(main_layout)

        # Timer for overlay movement
        self.movement_timer = QTimer()
        self.movement_timer.timeout.connect(self.move_overlay)
        self.movement_direction = None

    def change_mode(self):
        if self.cropping_mode_radio.isChecked():
            self.mode = "cropping"
            self.output_width_spin.setEnabled(False)
            self.output_height_spin.setEnabled(False)
            self.output_width = 200
            self.output_height = 200
            self.output_width_spin.setValue(self.output_width)
            self.output_height_spin.setValue(self.output_height)
            self.overlay_group.setEnabled(True)
            self.gradient_group.setEnabled(True)
        else:
            self.mode = "conversion"
            self.output_width_spin.setEnabled(True)
            self.output_height_spin.setEnabled(True)
            self.overlay_group.setEnabled(True)
            self.gradient_group.setEnabled(True)
        self.image_label.update_preview_size()
        self.image_label.update()

    def handle_dropped_image(self, file_path):
        self.image_path = file_path
        self.file_label.setText(os.path.basename(file_path))
        self.load_image_from_path()
        self.save_button.setEnabled(True)

    def handle_pasted_image(self, file_path):
        self.image_path = file_path
        self.temp_files.append(file_path)
        self.file_label.setText("Pasted Image")
        self.load_image_from_path()
        self.save_button.setEnabled(True)

    def open_file_dialog(self):
        options = QFileDialog.Options()
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
            self.load_image_from_path()
            self.save_button.setEnabled(True)

    def load_image_from_path(self):
        try:
            pixmap = QPixmap(self.image_path)
            if pixmap.isNull():
                raise ValueError("Failed to load image. The file may be corrupted or unsupported.")
            self.image_label.set_pixmap(pixmap)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load image.\n{e}")
            self.save_button.setEnabled(False)

    def choose_color(self):
        color = QColorDialog.getColor(initial=self.font_color, title="Select Font Color")
        if color.isValid():
            self.font_color = color
            self.color_button.setStyleSheet(f"background-color: {self.font_color.name()}")
            self.image_label.update()

    def choose_gradient_start_color(self):
        color = QColorDialog.getColor(initial=self.gradient_start_color, title="Select Gradient Start Color")
        if color.isValid():
            self.gradient_start_color = color
            self.gradient_start_button.setStyleSheet(f"background-color: {self.gradient_start_color.name()}")
            self.image_label.update()

    def choose_gradient_end_color(self):
        color = QColorDialog.getColor(initial=self.gradient_end_color, title="Select Gradient End Color")
        if color.isValid():
            self.gradient_end_color = color
            self.gradient_end_button.setStyleSheet(f"background-color: {self.gradient_end_color.name()}")
            self.image_label.update()

    def update_overlay_text(self, text):
        if len(text) > 10:
            self.text_input.setText(text[:10])
            return
        self.overlay_text = text
        self.image_label.update()

    def update_font_size(self, size):
        self.font_size = size
        self.image_label.update()

    def update_output_dimensions(self):
        self.output_width = self.output_width_spin.value()
        self.output_height = self.output_height_spin.value()
        self.image_label.update_preview_size()
        self.image_label.update()

    def update_output_dpi(self):
        self.output_dpi = self.output_dpi_spin.value()

    def select_save_directory(self):
        directory = QFileDialog.getExistingDirectory(
            self,
            "Select Directory",
            "",
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )
        if directory:
            self.save_directory = directory

    def update_preview(self):
        self.image_label.update()

    def start_moving_overlay(self, direction):
        self.movement_direction = direction
        self.movement_timer.start(50)

    def stop_moving_overlay(self):
        self.movement_timer.stop()

    def move_overlay(self):
        if self.movement_direction == "left":
            self.overlay_x_offset -= 5
        elif self.movement_direction == "right":
            self.overlay_x_offset += 5
        elif self.movement_direction == "up":
            self.overlay_y_offset -= 5
        elif self.movement_direction == "down":
            self.overlay_y_offset += 5
        self.image_label.update()

    def render_image(self, width, height, overlay_text, preview=False):
        final_pixmap = QPixmap(width, height)
        final_pixmap.fill(Qt.transparent)
        painter = QPainter(final_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.mode == "cropping":
            path = QPainterPath()
            path.addEllipse(0, 0, width, height)
            painter.setClipPath(path)

            transform = QTransform()
            scale_x = self.image_label.scale_factor
            scale_y = self.image_label.scale_factor
            trans_x = self.image_label.translation.x()
            trans_y = self.image_label.translation.y()
            transform.translate(trans_x + width / 2, trans_y + height / 2)
            transform.scale(scale_x, scale_y)
            painter.setTransform(transform)

            if self.original_pixmap:
                image_center = QPointF(self.original_pixmap.width() / 2, self.original_pixmap.height() / 2)
                painter.drawPixmap(-image_center, self.original_pixmap)

            painter.resetTransform()
            painter.setClipping(False)

            gradient = QLinearGradient(0, 0, width, height)
            gradient.setColorAt(0, self.gradient_start_color)
            gradient.setColorAt(1, self.gradient_end_color)
            pen = QPen(QBrush(gradient), 10)
            painter.setPen(pen)
            painter.drawEllipse(5, 5, width - 10, height - 10)

        else:
            if self.original_pixmap:
                scaled_pixmap = self.original_pixmap.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                x = (width - scaled_pixmap.width()) / 2
                y = (height - scaled_pixmap.height()) / 2
                painter.drawPixmap(QPointF(x, y), scaled_pixmap)

        if overlay_text:
            font = QFont("Arial", self.font_size)
            painter.setFont(font)
            painter.setPen(self.font_color)
            metrics = painter.fontMetrics()
            text_width = metrics.horizontalAdvance(overlay_text)
            text_height = metrics.ascent()
            x = self.overlay_x_offset + width / 2 - text_width / 2
            y = self.overlay_y_offset + height / 2 + text_height / 2
            painter.drawText(QPointF(x, y), overlay_text)

        painter.end()
        return final_pixmap

    def save_image(self):
        if not self.original_pixmap:
            QMessageBox.warning(self, "No Image", "There is no image to save.")
            return

        start_num = self.batch_start_spin.value()
        end_num = self.batch_end_spin.value()

        if start_num > end_num:
            QMessageBox.critical(self, "Invalid Range", "Start Number must be less than or equal to End Number.")
            return

        # Determine if batch processing is active
        is_batch = end_num - start_num >= 1

        if self.image_path:
            base_name = os.path.splitext(os.path.basename(self.image_path))[0]
        else:
            base_name = "pasted_image"

        save_dir = self.save_directory if self.save_directory else os.path.dirname(self.image_path) if self.image_path else os.getcwd()

        for num in range(start_num, end_num + 1):
            if is_batch:
                if self.overlay_text == "1":
                    # Use only the batch number as the overlay text
                    overlay_text = str(num)
                else:
                    # Append the batch number to the existing overlay text
                    overlay_text = f"{self.overlay_text} {num}"
            else:
                # Single image save; use the overlay text as is
                overlay_text = self.overlay_text if self.overlay_text else ""

            rendered_pixmap = self.render_image(self.output_width, self.output_height, overlay_text)

            image = rendered_pixmap.toImage()
            image.setDotsPerMeterX(int(self.output_dpi * 39.3701))
            image.setDotsPerMeterY(int(self.output_dpi * 39.3701))

            output_filename = f"{base_name}{num}.png"
            output_path = os.path.join(save_dir, output_filename)

            success = image.save(output_path, "PNG")
            if not success:
                QMessageBox.critical(self, "Save Failed", f"Failed to save image {output_filename}.")
                continue

        QMessageBox.information(self, "Success", f"Images saved from {start_num} to {end_num} in {save_dir}")
        self.cleanup_temp_files()

    def cleanup_temp_files(self):
        for temp_file in self.temp_files:
            try:
                os.unlink(temp_file)
            except Exception as e:
                print(f"Error deleting temporary file {temp_file}: {e}")
        self.temp_files = []


def main():
    app = QApplication(sys.argv)
    converter = ImageToPNGConverter()
    converter.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
