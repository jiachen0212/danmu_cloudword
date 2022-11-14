import cv2
import sys, os
import numpy as np 


# # 判断框中框
# def is_inside(o, i):
#     ox, oy, ow, oh = o
#     ix, iy, iw, ih = i
#     return ox > ix and oy > iy and ox + ow < ix + iw and oy + oh < iy + ih


# # 框出人 传入图片 矩形参数 BGR
# # def draw_person(image, person, bgr):
# #     x, y, w, h = person
# #     cv2.rectangle(image, (x, y), (x + w, y + h), bgr, 2)


# # 筛选识别出的人矩形数据
# def screen_found(found):
#     for ri, r in enumerate(found):
#         for qi, q, in enumerate(found):
#             if ri != qi and is_inside(r, q):
#                 break
#             else:
#                 found_filtered.append(r)


# # 等比缩放 参考：https://blog.csdn.net/JulyLi2019/article/details/120720752
# def resize_keep_aspectratio(image_src, dst_size):
#     src_h, src_w = image_src.shape[:2]
#     # print(src_h, src_w)
#     dst_h, dst_w = dst_size

#     # 判断应该按哪个边做等比缩放
#     h = dst_w * (float(src_h) / src_w)  # 按照ｗ做等比缩放
#     w = dst_h * (float(src_w) / src_h)  # 按照h做等比缩放

#     h = int(h)
#     w = int(w)

#     if h <= dst_h:
#         image_dst = cv2.resize(image_src, (dst_w, int(h)))
#     else:
#         image_dst = cv2.resize(image_src, (int(w), dst_h))

#     h_, w_ = image_dst.shape[:2]
#     # print(h_, w_)
#     print('等比缩放完毕')

#     return image_dst


# # cascade图片人体识别和绘制边框 参数 需要识别的图片 输出绘制的图片 xml路径 bgr颜色 目标的最小尺寸 目标的最大尺寸
# def cascade_img_person_detect_draw(src_img, dst_img, xml_path, bgr, min_size, max_size):
#     detector = cv2.CascadeClassifier(xml_path)
     
#     found = detector.detectMultiScale(src_img, 1.1, 3, cv2.CASCADE_SCALE_IMAGE, (0, 0), (500, 500))

#     # 筛选识别出的人矩形数据
#     screen_found(found)

#     for person in found_filtered:
#         x, y, w, h = person
#         img = cv2.rectangle(img, (x, y), (x + w, y + h), bgr, 2)
        
#     cv2.imwrite('./person_res.png', img)

#     found_filtered.clear()

#     print(xml_path + " 识别出:" + str(len(found)) + "个结果。")


if __name__ == '__main__':
    

#     img = cv2.imread('data/templates/template.jpg')
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # # 存储所有识别出的坐标集
#     # found_filtered = []

#     # hog = cv2.HOGDescriptor()
#     # # 加载SVM模型 行人识别
#     # hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

#     # # 对图像进行多尺度目标检测 返回检测到区域的坐标
#     # found, w = hog.detectMultiScale(gray)
#     # # print(found)

#     # # 筛选识别出的人矩形数据
#     # screen_found(found)

#     # # 在原图上绘出识别出的所有矩形 蓝色
#     # for person in found_filtered:
#     #     # draw_person(img, person, (255, 0, 0))
#     #     x, y, w, h = person
#     #     img = cv2.rectangle(img, (x, y), (x + w, y + h), (255,0,0), 2)
        
#     # cv2.imwrite('./person_res.png', img)


#     # # 清空列表
#     # found_filtered.clear()

#     # print("HOGDescriptor_getDefaultPeopleDetector 识别出:" + str(len(found)) + "个结果。")


#     # # 全身识别 青色
#     cascade_img_person_detect_draw(gray, img, "data/haarcascade_fullbody.xml", (255, 255, 0), (0, 0), (500, 500))

#     # # 上半身识别 洋红
#     # cascade_img_person_detect_draw(gray, img, "data/haarcascade_upperbody.xml", (255, 0, 255), (0, 0), (500, 500))

#     # # 下半身识别 黄色
#     # cascade_img_person_detect_draw(gray, img, "data/haarcascade_lowerbody.xml", (0, 255, 255), (0, 0), (500, 500))
    
    img = cv2.imread('../1.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(gray.shape)
    otsuThe, maxValue = 0, 255  # 76
    otsuThe, dst_Otsu = cv2.threshold(gray, 20, maxValue, cv2.THRESH_OTSU)
    # dst_Otsu = cv2.bitwise_not(dst_Otsu)
    img[dst_Otsu==255] = 255
    cv2.imwrite('./data/templates/res.png', img)

