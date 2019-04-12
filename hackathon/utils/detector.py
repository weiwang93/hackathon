'''
File: detector.py
Project: utils
File Created: 2019-04-12 2:34:29 pm
Author: wangwei (wangw11.thu@gmail.com)
-----
Last Modified: 2019-04-12 2:34:31 pm
Modified By: wangwei (wangw11.thu@gmail.com>)
'''
from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import dlib


# 初始化DLIB的人脸检测器（HOG），然后创建面部标志物预测
print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# 分别获取左右眼面部标志的索引
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]