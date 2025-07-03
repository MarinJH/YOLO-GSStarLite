from ultralytics import YOLO

# 定义训练参数
if __name__=='__main__':
    model = YOLO(r"D:\marin program\YOLO-GSStarLite\ultralytics\ultralytics\cfg\models\v8\yolov8.yaml")  # 替换为你的模型文件
    model.train(data=r'D:\marin program\YOLO-GSStarLite\GZMH_Dataset\DATA.yaml',
                epochs=300,
                imgsz=640,
                batch=16,
                workers=16,
                device=0,
                patience=150,
                lr0=0.1,
                lrf=0.01                          )
