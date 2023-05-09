import cv2

video = cv2.VideoCapture('videos\\hello_1.mp4')

if not video.isOpened():
    print('error')

while True:
    success, img = video.read()
    cv2.imshow("Video", img)

    if cv2.waitKey(25) & 0xFF == ord('u'):
          break

# ======================================================================================
# === Словарь видео.
# ===


tasks_video = {}
