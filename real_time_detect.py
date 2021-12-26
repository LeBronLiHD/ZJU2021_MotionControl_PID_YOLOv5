# -*- coding: utf-8 -*-

import torch
import load_yolov5
import time
import os
import cv2


def real_time_detect(model, img_path):
    """
    :param model:
    :return:
    1. read current image
    2. detect the image
    3. calculate
    4. show the result
    """
    count = 0
    while True:
        count += 1
        images = os.listdir(img_path)
        images = sorted(images,
                        key=lambda files: os.path.getmtime(os.path.join(img_path, files)),
                        reverse=False)
        img = os.path.join(img_path, images[0])
        results = model(img)
        results.print()
        results.show()
        time.sleep(0.1)
        if count >= 2:
            break


if __name__ == '__main__':
    model = load_yolov5.load_yolo_model()
    img_path = "./cur_img"
    real_time_detect(model, img_path)
