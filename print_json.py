import json

# 解析JSON文件
with open("/home/ubuntu22/yolov8/plant_data/train_label.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

# 使用一个集合来存储唯一的类别
labels = set()

# 遍历JSON对象，收集所有类别
for item in data:
    label = item["标签"]
    labels.add(label)

# 打印出所有的类别
print("JSON文件中含有的类别：")
for label in labels:
    print(label)




