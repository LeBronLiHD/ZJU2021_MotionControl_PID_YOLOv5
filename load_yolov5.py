# -*- coding: utf-8 -*-

import torch


def load_yolo_model():
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    # or yolov5m, yolov5l, yolov5x, custom
    return model


if __name__ == '__main__':
    model = load_yolo_model()
