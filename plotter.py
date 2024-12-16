import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from sympy import sympify, symbols, lambdify

class FunctionPlotter:
    def __init__(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

    def plot(self, function, x_range):
        self.ax.clear()

        try:
            x_min, x_max = map(float, x_range.split(":"))
            x = np.linspace(x_min, x_max, 1000)

            expr = sympify(function)
            x_sym = symbols('x')
            f = lambdify(x_sym, expr, "numpy")

            y = f(x)

            self.ax.plot(x, y)
            self.ax.set_xlabel("x")
            self.ax.set_ylabel("y")
            self.ax.set_title(f"График функции: {function}")
        except Exception as e:
            raise ValueError(f"Ошибка при построении графика: {e}")
