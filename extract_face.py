# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import cv2
import os
import argparse

CASCADE_DIR_PATH = r"E:\Anaconda3\envs\python3.5\Library\etc\haarcascades"
CASCADE_FILE_NAME = r"haarcascade_frontalface_alt.xml"
id = 0
# コマンドライン引数の定義
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", type=str, choices=["lfw_pos", "lfw_neg"])
args = parser.parse_args()

# 対象人物ではない python extract_face.py -t lfw_neg
if args.type == "lfw_neg":
    folder_list = ["Tony_Blair", "Hugo_Chavez"]
    suffix = "neg"
    SRC_DIR_PATH = "./data/lfw/"
    DST_DIR_PATH = "./data/faces/negative"
# 対象人物の画像 python extract_face.py -t lfw_pos
elif args.type == "lfw_pos":
    folder_list = ["George_W_Bush"]
    suffix = "pos"
    SRC_DIR_PATH = "./data/lfw/"
    DST_DIR_PATH = "./data/faces/positive"

# 顔画像検出器を初期化する
cascade_path = os.path.join(CASCADE_DIR_PATH, CASCADE_FILE_NAME)
cascade = cv2.CascadeClassifier(cascade_path)

# ファイルセットを作る
