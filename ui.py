from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel, QMessageBox, QListWidget, QListWidgetItem, QInputDialog
from plotter import FunctionPlotter

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Построитель графиков")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.input_layout = QVBoxLayout()
        self.layout.addLayout(self.input_layout)

        self.function_label = QLabel("Функция:")
        self.input_layout.addWidget(self.function_label)

        self.function_input = QLineEdit()
        self.function_input.setPlaceholderText("Например, sin(x)")
        self.input_layout.addWidget(self.function_input)

        self.x_range_label = QLabel("Диапазон x:")
        self.input_layout.addWidget(self.x_range_label)

        self.x_range_input = QLineEdit()
        self.x_range_input.setPlaceholderText("Например, -10:10")
        self.input_layout.addWidget(self.x_range_input)

        self.plot_button = QPushButton("Построить график")
        self.plot_button.clicked.connect(self.plot_function)
        self.input_layout.addWidget(self.plot_button)

        self.add_plot_button = QPushButton("Добавить график")
        self.add_plot_button.clicked.connect(self.add_plot)
        self.input_layout.addWidget(self.add_plot_button)

        self.remove_plot_button = QPushButton("Удалить график")
        self.remove_plot_button.clicked.connect(self.remove_plot)
        self.input_layout.addWidget(self.remove_plot_button)

        self.plotter = FunctionPlotter()
        self.layout.addWidget(self.plotter.canvas)

        self.functions = []
        self.x_ranges = []

    def plot_function(self):
        function = self.function_input.text()
        x_range = self.x_range_input.text()

        if function and x_range:
            try:
                self.functions = [function]
                self.x_ranges = [x_range]
                self.plotter.plot(self.functions, self.x_ranges)
                self.plotter.figure.tight_layout()
                self.plotter.canvas.draw()
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка: {e}")

    def add_plot(self):
        function = self.function_input.text()
        x_range = self.x_range_input.text()

        if function and x_range:
            try:
                self.functions.append(function)
                self.x_ranges.append(x_range)
                self.plotter.plot(self.functions, self.x_ranges)
                self.plotter.figure.tight_layout()
                self.plotter.canvas.draw()
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка: {e}")

    def remove_plot(self):
        if self.functions:
            items = [f"{i+1}: {func}" for i, func in enumerate(self.functions)]
            item, ok = QInputDialog.getItem(self, "Удалить график", "Выберите график для удаления:", items, 0, False)
            if ok and item:
                index = int(item.split(":")[0]) - 1
                self.functions.pop(index)
                self.x_ranges.pop(index)
                self.plotter.plot(self.functions, self.x_ranges)
                self.plotter.figure.tight_layout()
                self.plotter.canvas.draw()
