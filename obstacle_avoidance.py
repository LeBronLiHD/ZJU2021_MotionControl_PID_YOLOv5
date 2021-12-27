# -*- coding: utf-8 -*-

"""
obstacle avoidance of balance car
"""

import bt_balancecar
import math


def read_ultra():
    # @TODO: read ultra distance
    return 1


def delta(cur_pos, target):
    return math.sqrt((cur_pos[0] - target[0])**2 + (cur_pos[1] - target[1])**2)


def get_cur_pos(cur_pos, speed, angle, time):
    new_pos = cur_pos
    new_pos[0] += speed * math.cos(angle) * time
    new_pos[1] += speed * math.sin(angle) * time
    return new_pos


def obstacle_avoidance(target):
    print("target ->", target)
    cur_pos = [0, 0]
    while delta(cur_pos=cur_pos, target=target) > 0.25:
        # @TODO: read the current distance and give the next command
        cur_delta = [target[0] - cur_pos[0], target[1] - cur_pos[1]]


if __name__ == "__main__":
    print("Input target ->", end="")
    x, y = map(int, input().split())
    obstacle_avoidance([x, y])
