# -*- coding: utf-8 -*-

import cv2


def camera_save_to_local(show):
    # set for camera
    capCamera = cv2.VideoCapture(0)
    capCamera.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
    capCamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1920)

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    fps = 30
    framesize = (int(capCamera.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capCamera.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    outCamera = cv2.VideoWriter('./runs/output_' + str(fps) + '.mp4', fourcc, fps, framesize)

    while capCamera.isOpened():
        ret, frameCamera = capCamera.read()
        outCamera.write(frameCamera)
        if show:
            cv2.imshow('output', frameCamera)
        if cv2.waitKey(1) == ord('q'):
            break

    capCamera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    camera_save_to_local(show=True)
