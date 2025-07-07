from ultralytics import YOLO

# 定义训练参数
if __name__=='__main__':
    model = YOLO(r"")   # model
    model.train(data=r'',  # data
                epochs=300,
                imgsz=640,
                batch=64,
                workers=16,
                device=0,
                lr0=0.1,
                lrf=0.01                          )
