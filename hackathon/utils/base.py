'''
File: base.py
Project: utils
File Created: 2019-03-06 3:12:07 pm
Author: wangwei (wangw11.thu@gmail.com)
-----
Last Modified: 2019-03-06 3:12:09 pm
Modified By: wangwei (wangw11.thu@gmail.com>)
'''
from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2

# 定义两个常数
# 眼睛长宽比
# 闪烁阈值
EYE_AR_THRESH = 0.2
EYE_AR_CONSEC_imageS = 3
# 初始化帧计数器和眨眼总数
COUNTER = 0
TOTAL = 0

# 初始化DLIB的人脸检测器（HOG），然后创建面部标志物预测
print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('./utils/shape_predictor_68_face_landmarks.dat')

# 分别获取左右眼面部标志的索引
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

def get_rate(data):
    width = []
    height = []
    for d in data:
        [a, b] = d
        width.append(a)
        height.append(b)
    return (max(height)-min(height))/(max(width)-min(width))

def check_blink(path):
    # Load the jpg file into a numpy array
    image = cv2.imread(path)
    # Find all facial features in all the faces in the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 检测灰度帧中的人脸
    rects = detector(gray, 0)
    # 人脸检测循环
    for rect in rects:
        # 确定脸部区域的面部标志，然后将面部标志（x，y）坐标转换为数字阵列
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        # 提取左眼和右眼坐标，然后使用坐标计算双眼的眼睛长宽比
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        # print(get_rate(leftEye))
        # print(get_rate(rightEye))

        return (get_rate(leftEye)+get_rate(rightEye))/2
        # # 计算左眼和右眼的标志点并绘制
        # leftEyeHull = cv2.convexHull(leftEye)
        # rightEyeHull = cv2.convexHull(rightEye)
        # cv2.drawContours(image, [leftEyeHull], -1, (0, 255, 0), 1)
        # cv2.drawContours(image, [rightEyeHull], -1, (0, 255, 0), 1)

        # # 在图片中标注人脸，并显示
        # left = rect.left()
        # top = rect.top()
        # right = rect.right()
        # bottom = rect.bottom()
        # cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 3)

        # for (x, y) in shape:
        #     cv2.circle(image, (x, y), 1, (0, 0, 255), -1)


        # cv2.imshow("image", image)



if __name__ == '__main__':
    check_blink('../../png/00001.png')
    st = time.time()
    check_blink('../../1.jpg')
    print(time.time() -st)

