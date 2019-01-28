from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGridLayout, QWidget, QVBoxLayout

from src.data_loader import DataLoader
from src.data_processor import DataProcessor
import sys
import time

import numpy as np

from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self, data):
        super().__init__()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)

        static_canvas = FigureCanvas(Figure(figsize=(3, 2)))
        layout.addWidget(static_canvas)

        dynamic_canvas = FigureCanvas(Figure(figsize=(3, 2)))
        layout.addWidget(dynamic_canvas)



        self._static_ax = static_canvas.figure.subplots()
        d = data.get_temperature_dict("Warszawa")
        self._static_ax.plot(d.keys(), d.values(), ".")

        self._dynamic_ax = dynamic_canvas.figure.subplots()
        self._timer = dynamic_canvas.new_timer(
            100, [(self._update_canvas, (), {})])
        self._timer.start()

    def _update_canvas(self):
        self._dynamic_ax.clear()
        t = np.linspace(0, 10, 101)
        # Shift the sinusoid as a function of time.
        self._dynamic_ax.plot(t, np.sin(t + time.time()))
        self._dynamic_ax.figure.canvas.draw()

def clearLayout(layout):
  while layout.count():
    child = layout.takeAt(0)
    if child.widget():
      child.widget().deleteLater()

def render_window():
    city_name = dlg.comboBox_2.currentText()
    date = dlg.comboBox.currentText()

    dlg.curLabel.setText(data.get_weather_stat_string_for_date(city_name, date))
    dlg.forLabel.setText(data.get_weather_desc_string_for_date(city_name, date))
    dlg.addLabel.setText(data.get_additional_info_string(city_name, date))

    clearLayout(dlg.verticalLayout)

    dlg.label_6.setPixmap(QPixmap('screen.jpg'))

    static_canvas1 = FigureCanvas(Figure(figsize=(5, 1.8)))
    static_canvas2 = FigureCanvas(Figure(figsize=(5, 1.8)))
    static_canvas3 = FigureCanvas(Figure(figsize=(5, 1.8)))
    static_canvas4 = FigureCanvas(Figure(figsize=(5, 1.8)))

    dlg.verticalLayout.removeWidget(static_canvas1)
    dlg.verticalLayout.removeWidget(static_canvas2)
    dlg.verticalLayout.removeWidget(static_canvas3)
    dlg.verticalLayout.removeWidget(static_canvas4)

    dlg.verticalLayout.addWidget(static_canvas1)
    dlg.verticalLayout.addWidget(static_canvas2)
    dlg.verticalLayout.addWidget(static_canvas3)
    dlg.verticalLayout.addWidget(static_canvas4)

    dlg._static_ax = static_canvas1.figure.subplots()
    d = data.get_temperature_dict(city_name)
    dlg._static_ax.set_ylabel("Temperature [°C]")
    dlg._static_ax.set_label("Temperature")
    dlg._static_ax.set_xticklabels(data.get_xticks())
    dlg._static_ax.plot(d.keys(), d.values(), "g-")

    dlg._static_ax = static_canvas2.figure.subplots()
    d = data.get_wind_dict(city_name)
    dlg._static_ax.set_ylabel("Wind [m/s]")
    dlg._static_ax.set_label("Wind")
    dlg._static_ax.set_xticklabels(data.get_xticks())
    dlg._static_ax.plot(d.keys(), data.get_wind_list(city_name), "b-")

    dlg._static_ax = static_canvas3.figure.subplots()
    d = data.get_humidity_dict(city_name)
    dlg._static_ax.set_ylabel("Humidity [%]")
    dlg._static_ax.set_label("Temperature")
    dlg._static_ax.set_xticklabels(data.get_xticks())
    dlg._static_ax.plot(d.keys(), d.values(), "r-")

    dlg._static_ax = static_canvas4.figure.subplots()
    d = data.get_cloudiness_dict(city_name)
    dlg._static_ax.set_ylabel("Cloudiness [%]")
    dlg._static_ax.set_label("Cloudiness")
    dlg._static_ax.set_xticklabels(data.get_xticks())
    dlg._static_ax.plot(d.keys(), d.values(), "y-")

    dlg.show()


if __name__ == "__main__":

    qapp = QtWidgets.QApplication(sys.argv)
    dlg = uic.loadUi("layout.ui")
    data = DataProcessor()

    dlg.comboBox.addItems(data.get_list_of_dates())
    dlg.comboBox.currentIndexChanged.connect(render_window)
    dlg.comboBox_2.addItems(data.data.city_ids.keys())
    dlg.comboBox_2.currentIndexChanged.connect(render_window)

    city_name = dlg.comboBox_2.currentText()
    date = dlg.comboBox.currentText()

    render_window()
    qapp.exec_()

def data_test():
    data = DataProcessor()
    print(data.get_temperature_dict("Warszawa"))
    print(data.get_humidity_dict("Warszawa"))
    print(data.get_wind_dict("Warszawa"))
    print(data.get_cloudiness_dict("Warszawa"))
    print(data.get_weather_description_dict("Warszawa"))
    print(data.get_current_date())
    print(data.get_list_of_dates())



