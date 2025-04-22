import cv2
from src.colors import Colors


class UIManager:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.box_size = 120
        self.margin = 20
        self.selected_color = Colors.RED.name

        self.color_boxes = {}
        y_pos = self.margin
        x_pos = self.width - self.box_size - self.margin

        for color in Colors:
            self.color_boxes[color.name] = (
                x_pos,
                y_pos,
                self.box_size,
                self.box_size,
            )
            y_pos += self.box_size + self.margin

    def draw_box(self, frame, color_name, x, y, w, h):
        cv2.rectangle(frame, (x, y), (x + w, y + h), Colors[color_name].value, -1)

    def draw_text(
        self, frame, text, x, y, font_scale=1, color=(255, 255, 255), thickness=2
    ):
        cv2.putText(
            frame,
            text,
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            font_scale,
            color,
            thickness,
            cv2.LINE_AA,
            False,
        )

    def draw_selected_color(self, frame, box):
        (x, y, w, h) = box
        cv2.rectangle(frame, (x - 3, y - 3), (x + w + 3, y + h + 3), (255, 255, 255), 2)

    def draw(self, frame):
        for color_name, (x, y, w, h) in self.color_boxes.items():
            self.draw_box(frame, color_name, x, y, w, h)

        self.draw_selected_color(frame, self.color_boxes[self.selected_color])

        cv2.rectangle(
            frame, (10, 10), (50, 50), Colors[self.selected_color].value, -1
        )
        cv2.rectangle(frame, (10, 10), (50, 50), (255, 255, 255), 2)

    def handle_selection(self, point):
        for color_name, (x, y, w, h) in self.color_boxes.items():
            if (x <= point[0] <= x + w) and (y <= point[1] <= y + h):
                self.selected_color = color_name
                return True, color_name
        return False, None

    def set_color(self, color_name):
        self.selected_color = color_name