import cv2
import mediapipe as mp
class faceDetector():
    def __init__(self, mode=False, max_faces=2, detection_confidence=0.5, track_confidence=0.5):
        self.mode = mode
        self.max_hands = max_faces
        self.detection_confidence = detection_confidence
        self.track_confidence = track_confidence

        self.mp_face_detection = mp.solutions.face_detection
        self.hands = self.mpHands.Hands(self.mode, self.max_hands, self.detection_confidence, self.track_confidence)
        self.mpDraw = mp.solutions.drawing_utils


mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_detection.process(image)

        # Draw the face detection annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(image, detection)
        # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
