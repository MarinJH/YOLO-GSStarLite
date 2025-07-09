#coding: utf-8
from ultralytics import YOLO
import matplotlib
matplotlib.use( "TkAgg")
if __name__ == '__main__':
    #加载训练好的模型
    model = YOLO(r'xxxxxx\best.pt')
    # 对验证集进行评估
    metrics = model.val(data = r'xxxxx\DATA.yaml',batch=64)
