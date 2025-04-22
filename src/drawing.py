import cv2
import numpy as np
from enum import Enum
from src.colors import Colors

class Tools(Enum):
    PEN = 1
    ERASER = 2


class DrawingCanvas:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.canvas = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        self.current_color_name = Colors.RED.name
        self.current_color = Colors.RED
        self.thickness = 15
        self.eraser_thickness = 125
        self.current_tool = Tools.PEN
        self.drawing = False
        self.start_point = None

    def draw(self, point):
        if not self.drawing or self.start_point is None:
            return

        if self.current_tool == Tools.PEN:
            bgr_color = self.current_color.value
            cv2.line(self.canvas, self.start_point, point, bgr_color, self.thickness)
            self.start_point = point
            return

        if self.current_tool == Tools.ERASER:
            cv2.line(self.canvas, self.start_point, point, (0, 0, 0), self.eraser_thickness)
            self.start_point = point

    def start_drawing(self, point):
        self.drawing = True
        self.start_point = point
        print(f"Bắt đầu vẽ: {self.current_color_name}")

    def stop_drawing(self):
        self.drawing = False
        self.start_point = None

    def set_color(self, color: str):
        self.current_color_name = color
        self.current_color = Colors[color]
        print(f"Canvas color set to: {color}, BGR: {self.current_color}")

    def set_tool(self, tool: Tools):
        self.current_tool = tool

    def get_display(self):
        return self.canvas.copy()

    def clear(self):
        self.canvas = np.zeros((self.height, self.width, 3), dtype=np.uint8)