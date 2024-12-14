from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt
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

        self.input_layout = QHBoxLayout()
        self.layout.addLayout(self.input_layout)

        self.function_label = QLabel("Функция:")
        self.input_layout.addWidget(self.function_label)

        self.function_input = QLineEdit()
        self.function_input.setPlaceholderText("Например, sin(x)")
        self.input_layout.addWidget(self.function_input)

        self.plot_button = QPushButton("Построить график")
        self.plot_button.clicked.connect(self.plot_function)
        self.input_layout.addWidget(self.plot_button)

        self.plotter = FunctionPlotter()
        self.layout.addWidget(self.plotter.canvas)

    def plot_function(self):
        function = self.function_input.text()
        if function:
            try:
                self.plotter.plot(function)
                self.plotter.figure.tight_layout()
                self.plotter.canvas.draw()
            except Exception as e:
                print(f"Ошибка: {e}")
