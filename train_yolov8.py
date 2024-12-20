from ultralytics import YOLO

# 定义训练参数
if __name__=='__main__':
    model = YOLO(r"D:\marin program\yolov8\ultralytics\ultralytics\cfg\models\v8\yolov8.yaml")  # 替换为你的模型文件
    model.train(data=r'D:\marin program\yolov8\plant_data_new_new\DATA.yaml',
                epochs=200,
                imgsz=640,
                batch=64,
                workers=12,
                device=0,
                patience=30,
                lr0=0.01,
                lrf=0.01                          )
