# -*- coding: utf-8 -*-

"""
obstacle avoidance of balance car
"""

import math
import time
from bt_balancecar import control
import bt_balancecar


def read_ultra():
    # @TODO: read ultra distance
    return bt_balancecar.read_ultra()


def delta(cur_pos, target):
    return math.sqrt((cur_pos[0] - target[0])**2 + (cur_pos[1] - target[1])**2)


def get_cur_pos(cur_pos, speed, angle, time):
    new_pos = cur_pos
    new_pos[0] += speed * math.cos(angle) * time
    new_pos[1] += speed * math.sin(angle) * time
    return new_pos


def calculate_heading(cur_pos, target):
    delty = target[1] - cur_pos[1]
    deltx = target[0] - cur_pos[0]

    if deltx >= 0:
        theta = math.atan(delty / deltx)
    elif delty >= 0:
        theta = math.pi + math.atan(delty / deltx)
    else:
        theta = -math.pi + math.atan(delty / deltx)

    return theta


def obstacle_avoidance(target):
    print("target ->", target)
    cur_pos = [0, 0]  # 以小车初始位置为原点
    theta = 0  # 小车朝向
    w = 3.75  # 小车角速度  单位rad/s
    speed = 80  # 小车速度 单位cm/s
    flag = 4  # 直行一定长度矫正一次方向
    w_time = 0.1  # 小车单次前进时间
    while delta(cur_pos=cur_pos, target=target) > 40:
        dist = read_ultra()
        if dist > 20:
            # 前进一定距离
            control(mode='w')
            time.sleep(w_time)
            cur_pos = get_cur_pos(cur_pos, speed, theta, w_time)
            flag += 1
        else:
            # 遇到障碍物暂停
            control(mode='q')
            time.sleep(0.1)
            while dist <= 20:
                # 向右转60°
                t = (math.pi/6)/w
                theta -= math.pi/6
                control(mode='d')
                time.sleep(t)
                dist = read_ultra()

        # 当前进到了一定距离，转向目标朝向
        if flag >= 5:
            flag = 0
            delt_theta = calculate_heading(cur_pos, target) - theta
            t = delt_theta / w
            if t > 0:
                control(mode='q')
                time.sleep(0.1)
                control(mode='a')
                time.sleep(t)
                theta += delt_theta
                control(mode='q')
                time.sleep(0.1)
            elif t < 0:
                control(mode='q')
                time.sleep(0.1)
                control(mode='d')
                time.sleep(-t)
                theta += delt_theta
                control(mode='q')
                time.sleep(0.1)
    print('arrived')


if __name__ == "__main__":
    print("Input target ->", end="")
    x, y = map(int, input().split())
    obstacle_avoidance([x, y])
