import os
import cv2
import uuid
import pickle
from config import args


# 随机生成图片id
def id_generator():
    return str(uuid.uuid1())


# 通过cv2.waitKey()判断是否按下某个按键
def press(fg, trigger):
    if isinstance(trigger, str):
        return fg & 0xFF == ord(trigger)
    else:
        return fg & 0xFF == trigger


if __name__ == '__main__':

    cap = cv2.VideoCapture(args.video_path)

    im_width, im_height = int(cap.get(3)), int(cap.get(4))

    # mode : 0-左手, 1-右手, 2-双手
    num_hands_detect = 1
    if args.mode == 2:
        num_hands_detect = 2

    cv2.namedWindow('Window', cv2.WINDOW_NORMAL)

    if os.path.exists(args.boxes_path):
        with open(args.boxes_path, 'rb') as f:
            boxes_dict = pickle.load(f)
    else:
        boxes_dict = {}

    if args.mode == 2:
        final_boxes = [[100, 100, 400, 400], [0, 0, 0, 0]]
    else:
        final_boxes = [[100, 100, 400, 400]]

    # left, top, right, bottom = 0, 0, 0, 0
    assert args.mode in [0, 1, 2]

    whichhand = 0
    while cap.isOpened():
        ret, image_np = cap.read()
        image_np = cv2.flip(image_np, 0);
        # 使用上一帧的检测框作为当前帧的初始框,再进行微调
        left, top, right, bottom = [int(i) for i in final_boxes[whichhand]]
        while True:
            image_ini = image_np.copy()
            for i, x in enumerate(final_boxes):
                cv2.rectangle(image_ini, tuple(x[:2]), tuple(x[2:]), args.color_map[i], 3, 1)
            cv2.imshow('Window', image_ini)

            flag = cv2.waitKey(0)
            # 保存
            if press(flag, 'm'):
                id = id_generator()
                path = args.save_path + id + '.jpg'

                print('-----------------------------------')
                print('save as', path)
                print('box coordinate: ', final_boxes)
                cv2.imwrite(path, image_np)
                print('-----------------------------------')

                boxes_dict[id] = final_boxes.copy()
                with open(args.boxes_path, 'wb') as f:
                    pickle.dump(boxes_dict, f)
                break
            # 空格 跳到下一帧
            elif press(flag, 32):
                break
            # 上移
            elif press(flag, 'w'):
                top = max(top - 2, 0)
                bottom -= 2
            # 下移
            elif press(flag, 's'):
                top += 2
                bottom = min(im_height, bottom + 2)
            # 左移
            elif press(flag, 'a'):
                left = max(left - 2, 0)
                right -= 2
            # 右移
            elif press(flag, 'd'):
                left += 2
                right = min(im_width, right + 2)
            # 上下拉伸
            elif press(flag, 'i'):
                top = max(top - 2, 0)
                bottom = min(im_height, bottom + 2)
            # 上下压缩
            elif press(flag, 'k'):
                top += 2
                bottom -= 2
            # 左右拉伸
            elif press(flag, 'j'):
                left = max(left - 2, 0)
                right = min(im_width, right + 2)
            # 左右压缩
            elif press(flag, 'l'):
                left += 2
                right -= 2
            elif press(flag, 'r'):
                if args.mode == 2:
                    # whichhand == 0 表示当前控制的是左手,需要切换到右手
                    if whichhand == 0:
                        left, top, right, bottom = final_boxes[1]
                    else:
                        left, top, right, bottom = final_boxes[0]
                    whichhand = abs(whichhand - 1)
                else:
                    pass
            elif press(flag, 'q'):
                exit(0)
            # 输出改变结果
            print(left, top, right, bottom)
            final_boxes[whichhand] = [left, top, right, bottom]
