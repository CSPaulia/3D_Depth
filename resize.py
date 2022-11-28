import cv2
import os

# img = cv2.imread('/Users/apple/Desktop/三维深度感知/data/新标定/ir/ir_frame_2021_04_29_17_15_55.png')
# img2 = cv2.imread('/Users/apple/Desktop/三维深度感知/data/新标定/rgb/color_frame_2021_04_29_17_15_55.png')

# shape1 = img.shape
# shape2 = img2.shape
# newh = shape1[0] / shape1[1] * shape2[1]

# for imgname in os.listdir('/Users/apple/Desktop/三维深度感知/data/新标定/rgb'):
#     if imgname != '.DS_Store':
#         img = cv2.imread('/Users/apple/Desktop/三维深度感知/data/新标定/rgb/' + imgname)
#         newimg = img[int((shape2[0]-newh)/2):int(shape2[0]-(shape2[0]-newh)/2), :, :]
#         if newimg.shape[0] / newimg.shape[1] == shape1[0] / shape1[1]:
#             newimg = cv2.resize(newimg, (shape1[1], shape1[0]))
#         print(newimg.shape)
#         cv2.imwrite('/Users/apple/Desktop/三维深度感知/data/新标定/rgb/' + imgname, newimg)

# 将RGBD图像进行裁剪和放缩
img = cv2.imread('data/第二次数据/RGB_IR_head/IR/front_binary.png')
img2 = cv2.imread('data/第二次数据/RGB_IR_head/RGB/front_rgb.png')

shape1 = img.shape
shape2 = img2.shape
newh = shape1[0] / shape1[1] * shape2[1]

for imgname in os.listdir('data/第二次数据/RGB_IR_head/RGB/'):
    if imgname != '.DS_Store':
        img = cv2.imread('data/第二次数据/RGB_IR_head/RGB/' + imgname)
        newimg = img[int((shape2[0]-newh)/2):int(shape2[0]-(shape2[0]-newh)/2), :, :]
        if newimg.shape[0] / newimg.shape[1] == shape1[0] / shape1[1]:
            newimg = cv2.resize(newimg, (shape1[1], shape1[0]))
        print(newimg.shape)
        cv2.imwrite('data/第二次数据/RGB_IR_head/cut_RGB/' + imgname, newimg)
