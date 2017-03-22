# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import cv2
import os
import argparse

CASCADE_DIR_PATH = "E:\Anaconda3\envs\python3.5\Library\etc\haarcascades"
CASCADE_FILE_NAME = "haarcascade_frontalface_alt.xml"
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
for folder in folder_list:
    src_file_list = os.listdir(SRC_DIR_PATH + folder)
    for file in src_file_list:
        # 不要なファイルに判定処理を使わない
        if file.startswitch(".") or file.endswith(".txt"):
            continue

        try:
            # 画像の読み込み
            image = cv2.imread(os.path.join(SRC_DIR_PATH + folder, file))

            # 画像を読み込めなかった場合に処理を飛ばす
            if image is None:
                continue

            if (len(image.shape)) == 2:
                image_gray = image
                continue
            else:
                print("グレースケールの変換を開始する. {}".format(os.path.join(SRC_DIR_PATH, file)))
                image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        except Exception as e:
            print(e, file)
            continue
        # 画像スケールの調整
        scale_height = 512.0 / image.shape[0]
        scale_width = 512.0 / image.shape[1]

        resize_image_gray = cv2.resize(image_gray, (512, 512))
        print("グレースケール変換を完了する.")

        minsize = (int(resize_image_gray.shape[0] * 0.1),
                   int(resize_image_gray.shape[1] * 0.1))
