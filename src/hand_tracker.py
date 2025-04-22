import mediapipe as mp
import cv2
from src.config import MAX_HANDS, MIN_DETECTION_CONFIDENCE, MIN_TRACKING_CONFIDENCE


class HandTracker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=MAX_HANDS,
            min_detection_confidence=MIN_DETECTION_CONFIDENCE,
            min_tracking_confidence=MIN_TRACKING_CONFIDENCE
        )
        self.mp_draw = mp.solutions.drawing_utils
        self.prev_positions = {}

    def find_hands(self, frame, draw=True):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(rgb_frame)

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    landmarks_style = self.mp_draw.DrawingSpec(
                        color=(255, 255, 255),  # White
                        thickness=2,
                        circle_radius=6
                    )
                    connections_style = self.mp_draw.DrawingSpec(
                        color=(255, 255, 255),  # White
                        thickness=1,
                        circle_radius=2
                    )

                    self.mp_draw.draw_landmarks(
                        frame,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS,
                        landmarks_style,
                        connections_style
                    )
        return frame

    def get_hand_position(self, frame, hand_number=0):
        landmark_list = []

        if self.results.multi_hand_landmarks:
            if len(self.results.multi_hand_landmarks) > hand_number:
                hand = self.results.multi_hand_landmarks[hand_number]
                for i, landmark in enumerate(hand.landmark):
                    height, width, _ = frame.shape
                    cx, cy = int(landmark.x * width), int(landmark.y * height)
                    landmark_list.append((i, cx, cy))

        return landmark_list

    def get_finger_position(self, frame, finger_id, hand_number=0):
        positions = self.get_hand_position(frame, hand_number)
        if not positions:
            return None

        finger_pos = None
        for i, x, y in positions:
            if i == finger_id:
                finger_pos = (x, y)
                break

        if finger_pos is None:
            return None

        if finger_id in self.prev_positions:
            alpha = 0.5
            smooth_x = int(alpha * finger_pos[0] + (1 - alpha) * self.prev_positions[finger_id][0])
            smooth_y = int(alpha * finger_pos[1] + (1 - alpha) * self.prev_positions[finger_id][1])
            finger_pos = (smooth_x, smooth_y)

        self.prev_positions[finger_id] = finger_pos
        return finger_pos

    def get_finger_up_status(self, frame, hand_number=0):
        positions = self.get_hand_position(frame, hand_number)
        if not positions:
            return [False] * 5

        landmarks = dict([(i, (x, y)) for i, x, y in positions])

        # Finger MCP (base) joints
        finger_bases = [5, 9, 13, 17]
        # Finger PIP joints
        finger_pips = [6, 10, 14, 18]
        # Finger tip positions
        finger_tips = [8, 12, 16, 20]

        fingers_up = []

        if landmarks[4][0] > landmarks[3][0]:
            fingers_up.append(True)
        else:
            fingers_up.append(False)

        # Other fingers
        for tip, pip in zip(finger_tips, finger_pips):
            if landmarks[tip][1] < landmarks[pip][1]:
                fingers_up.append(True)
            else:
                fingers_up.append(False)

        return fingers_up