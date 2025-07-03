import json
import os
import glob
import os.path as osp

def labelme2yolov2Seg(jsonfilePath="", resultDirPath="", classList=['purple_grape', 'green_grape']):
    """
    将labelme标注好的数据集转换为yolov5_7.0sege中使用的数据集
    :param jsonfilePath: labelme标注好的*.json文件所在文件夹
    :param resultDirPath: 转换好后的*.txt保存文件夹
    :param classList: 数据集中的类别标签
    :return:
    """
    # 创建保存转换结果的文件夹
    if not os.path.exists(resultDirPath):
        os.mkdir(resultDirPath)

    # 获取目录下所有的labelme标注好的Json文件，存入列表中
    jsonfileList = glob.glob(osp.join(jsonfilePath, "*.json"))
    print(f"Found {len(jsonfileList)} JSON files: {jsonfileList}")  # 打印文件夹下的文件名称

    # 遍历json文件，进行转换
    for jsonfile in jsonfileList:
        # 检查文件是否为空
        if os.stat(jsonfile).st_size == 0:
            print(f"Skipping empty file: {jsonfile}")
            continue

        # 打开json文件
        try:
            with open(jsonfile, "r", encoding='utf-8') as f:
                file_in = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON file {jsonfile}: {e}")
            continue

        # 读取文件中记录的所有标注目标
        shapes = file_in["shapes"]

        # 确保imageWidth和imageHeight存在
        imageWidth = file_in.get("imageWidth", None)
        imageHeight = file_in.get("imageHeight", None)

        if imageWidth is None or imageHeight is None:
            print(f"Image width/height missing in {jsonfile}, please check the JSON file.")
            continue  # 跳过没有尺寸信息的文件

        # 使用图像名称创建一个txt文件，用来保存数据
        with open(osp.join(resultDirPath, jsonfile.split("/")[-1].replace(".json", ".txt")), "w") as file_handle:
            # 遍历shapes中的每个目标的轮廓
            for shape in shapes:
                # 根据json中目标的类别标签，从classList中寻找类别的ID，然后写入txt文件中
                file_handle.writelines(str(classList.index(shape["label"])) + " ")

                # 遍历shape轮廓中的每个点，进行图像尺寸的缩放
                for point in shape["points"]:
                    x = point[0] / imageWidth  # X坐标
                    y = point[1] / imageHeight  # Y坐标
                    file_handle.writelines(str(x) + " " + str(y) + " ")  # 写入mask轮廓点

                # 每个物体一行数据，一个物体遍历完成后换行
                file_handle.writelines("\n")

if __name__ == "__main__":
    jsonfilePath = "/home/ubuntu22/yolov8/data_seg/jsons"  # 要转换的json文件所在目录
    resultDirPath = "/home/ubuntu22/yolov8/data_seg/labels"  # 要生成的txt文件夹
    labelme2yolov2Seg(jsonfilePath=jsonfilePath, resultDirPath=resultDirPath, classList=["waiyuan", "neiyuan"])

