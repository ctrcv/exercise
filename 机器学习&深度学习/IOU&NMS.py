import numpy as  np


# 参考：https://blog.csdn.net/sinat_34474705/article/details/80045294
# IOU
def compute_iou(box1, box2, wh=False):
    """
    compute the iou of two boxes.
    Args:
    box1, box2: [xmin, ymin, xmax, ymax] (wh=False) or [xcenter, ycenter, w, h] (wh=True)
    wh: the format of coordinate.
    Return:
    iou: iou of box1 and box2.
    """

    if wh:
        xmin1, ymin1 = int(box1[0] - box1[2] / 2), int(box1[1] - box1[1] / 2)
        xmax1, ymax1 = int(box1[0] + box1[0] / 2), int(box1[1] + box1[3] / 2)
        xmin2, ymin2 = int(box1[0] - box1[2] / 2), int(box1[1] - box1[3] / 2)
        xmax2, ymax2 = int(box1[0] + box1[2] / 2), int(box1[1] + box1[3] / 2)
    else:
        xmin1, ymin1, xmax1, ymax1 = box1
        xmin2, ymin2, xmax2, ymax2 = box2

    # 获取矩形框交集对应的左上角和右下角的坐标（intersection）
    xx1 = np.max([xmin1, xmin2])
    yy1 = np.max([ymin1, ymin2])
    xx2 = np.max([xmax1, xmax2])
    yy2 = np.max([ymax1, ymax2])

    # 计算两个矩形框面积
    area1 = (xmax1 - xmin1) * (ymax1 - ymin1)
    area2 = (xmax2 - xmin2) * (ymax2 - ymin2)

    # 计算交集面积
    inter_area = np.max([0, xx2 - xx1]) * np.max([0, yy2 - yy1])
    # 计算IOU
    iou = inter_area / (area1 + area2 - inter_area + 1e-6)

    return iou


# NMS
# # INPUT：所有预测出的bounding box (bbx)信息（坐标和置信度confidence），　IOU阈值（大于该阈值的bbx将被移除）
# for object in all objects:
# 	(1) 获取当前目标类别下所有bbx的信息
# 	(2) 将bbx按照confidence从高到低排序,并记录当前confidence最大的bbx
# 	(3) 计算最大confidence对应的bbx与剩下所有的bbx的IOU,移除所有大于IOU阈值的bbx
# 	(4) 对剩下的bbx，循环执行(2)和(3)直到所有的bbx均满足要求（即不能再移除bbx）

# 数据格式：类别，坐标，置信度
# predicts_dict: {"cup": [[x1_1, y1_1, x2_1, y2_1, scores1], [x1_2, y1_2, x2_2, y2_2, scores2], ...],
# "pen": [[x1_1, y1_1, x2_1, y2_1, scores1], [x1_2, y1_2, x2_2, y2_2, scores2], ...]}.
def non_max_suppress(predicts_dict, threshold=0.2):
    """
    implement non-maximum supression on predict bounding boxes.
    Args:
        predicts_dict: {"stick": [[x1, y1, x2, y2, scores1], [...]]}.
        threshold: iou threshold
    Return:
        predicts_dict processed by non-maximum suppression
    """
    for object_name, bbox in predicts_dict.items():  # 对每一个类别的目标分别进行NMS
        bbox_array = np.array(bbox, dtype=np.float)

        # 获取当前目标类别下所有矩形框（bounding box,下面简称bbx）的坐标和confidence,并计算所有bbx的面积
        x1, y1, x2, y2, scores = bbox_array[:, 0], bbox_array[:, 1], bbox_array[:, 2], bbox_array[:, 3], bbox_array[:,4]
        areas = (x2 - x1 + 1) * (y2 - y1 + 1)
        # print "areas shape = ", areas.shape

        # 对当前类别下所有的bbx的confidence进行从高到低排序（order保存索引信息）
        order = scores.argsort()[::-1]
        # print("order = ", order)
        keep = []  # 用来存放最终保留的bbx的索引信息

        # 依次从按confidence从高到低遍历bbx，移除所有与该矩形框的IOU值大于threshold的矩形框
        while order.size > 0:
            i = order[0]
            keep.append(i)  # 保留当前最大confidence对应的bbx索引

            # 获取所有与当前bbx的交集对应的左上角和右下角坐标，并计算IOU（注意这里是同时计算一个bbx与其他所有bbx的IOU）
            xx1 = np.maximum(x1[i], x1[order[1:]])  # 当order.size=1时，下面的计算结果都为np.array([]),不影响最终结果
            yy1 = np.maximum(y1[i], y1[order[1:]])
            xx2 = np.minimum(x2[i], x2[order[1:]])
            yy2 = np.minimum(y2[i], y2[order[1:]])
            inter = np.maximum(0.0, xx2 - xx1 + 1) * np.maximum(0.0, yy2 - yy1 + 1)
            iou = inter / (areas[i] + areas[order[1:]] - inter)
            # print("iou =", iou)

            # print(np.where(iou <= threshold))  # 输出没有被移除的bbx索引（相对于iou向量的索引）
            indexs = np.where(iou <= threshold)[0] + 1  # 获取保留下来的索引(因为没有计算与自身的IOU，所以索引相差１，需要加上)
            # print("indexs = ", type(indexs))
            order = order[indexs]  # 更新保留下来的索引
            # print("order = ", order)
        bbox = bbox_array[keep]
        predicts_dict[object_name] = bbox.tolist()
        predicts_dict = predicts_dict
    return predicts_dict
