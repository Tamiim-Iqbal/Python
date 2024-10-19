import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break
    cv2.imshow('mycam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()

