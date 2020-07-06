# -*- coding: utf-8 -*-

import sys
import math

def main():
    input = sys.stdin.readline
    a, b, h, m = map(int, input().split())
    h_angle = h * 30 + m * 0.5
    m_angle = m * 6
    radian = 0
    if h_angle > m_angle:
        angle = h_angle - m_angle
    else:
        angle = m_angle - h_angle
    if angle > 180:
        angle = 360 - angle
    radian = math.radians(angle)
    c_2 = (a**2 + b**2) - (2 * a * b * math.cos(radian))
    print('{:.20f}'.format(math.sqrt(c_2)))
    return 


if __name__ == '__main__':
    main()


