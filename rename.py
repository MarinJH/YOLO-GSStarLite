from ultralytics import YOLO

# Load a model
if __name__ == '__main__':
    model = YOLO(r'D:\marin program\yolov8\ultralytics\runs\detect\train\weights\last.pt')  # load a partially trained model

    # Resume training
    results = model.train(resume=True)