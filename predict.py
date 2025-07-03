from ultralytics import YOLO

model = YOLO(r'D:\marin program\YOLO-GSStarLite\ultralytics\runs\detect\源码\weights\best.pt')
model.predict(r'D:\marin program\YOLO-GSStarLite\plant_data_new_new\images\val\4930.jpg', save=True, conf=0.5)
