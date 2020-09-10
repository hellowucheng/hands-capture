import os
import cv2
import time
from config import args

if not os.path.exists(args.save_path):
    os.makedirs(args.save_path)


cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'xvid')
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out = cv2.VideoWriter(args.video_path, fourcc, 10, size)

print('saving to %s' % args.video_path)
print('Are you Ready!')

start = 0
im_width, im_height = int(cap.get(3)), int(cap.get(4))

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    image_np = frame.copy()

    if start <= 150:
        cv2.rectangle(image_np, (100, 100), (400, 400), (255, 0, 0), 3, 1)
        cv2.imshow('window', image_np)
        if start % 30 == 0:
            print(5 - start // 30)
        if start == 150:
            print('go')
    else:
        cv2.imshow('window', image_np)
        out.write(frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        print('end')
        break
    start += 1

cap.release()
out.release()
cv2.destroyAllWindows()