import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

lines_one_rows = 3.0

if __name__ == '__main__':
    img0 = cv2.imread('data/第二次数据/RGB_IR_head/IR_RGB_pair/IR/standard.png', 0)
    img1 = cv2.imread('data/第二次数据/RGB_IR_head/IR_RGB_pair/IR/front.png', 0)
    img2 = cv2.imread('data/第二次数据/RGB_IR_head/IR_RGB_pair/IR/left45.png', 0)
    img3 = cv2.imread('data/第二次数据/RGB_IR_head/IR_RGB_pair/IR/left90.png', 0)
    img4 = cv2.imread('data/第二次数据/RGB_IR_head/IR_RGB_pair/IR/right45.png', 0)
    img5 = cv2.imread('data/第二次数据/RGB_IR_head/IR_RGB_pair/IR/right90.png', 0)
    IRimg = [img0, img1, img2, img3, img4, img5]
    name = ['front', 'left45', 'left90', 'right45', 'right90']

    # 对二值化数据做半全局块匹配算法
    stereo = cv2.StereoSGBM_create(numDisparities=32, blockSize=11, P1=968, P2=3872)
    disparity = []
    standard_img = IRimg[0]
    for i in range(1, len(IRimg)):
        disparity_curr = stereo.compute(np.uint8(IRimg[i]), np.uint8(standard_img))
        disparity_curr = np.column_stack((disparity_curr[:, 32:], disparity_curr[:, :32]))
        disparity_curr = disparity_curr / 2
        for r in range(disparity_curr.shape[0]):
            for c in range(disparity_curr.shape[1]):
                if disparity_curr[r][c] < 144:
                    disparity_curr[r][c] = 0
        # plt.imshow(disparity_curr, 'gray')
        # plt.show()
        # plt.close()
        disparity.append(disparity_curr)
        cv2.imwrite('data/第二次数据/RGB_IR_head/IR_RGB_pair/IR_Disparity/' + name[i-1] + '_disparity.png', disparity_curr)

    img1 = cv2.imread('data/第二次数据/RGB_IR_head/IR_RGB_pair/RGB/front.png', 0)
    img2 = cv2.imread('data/第二次数据/RGB_IR_head/IR_RGB_pair/RGB/left45.png', 0)
    img3 = cv2.imread('data/第二次数据/RGB_IR_head/IR_RGB_pair/RGB/left90.png', 0)
    img4 = cv2.imread('data/第二次数据/RGB_IR_head/IR_RGB_pair/RGB/right45.png', 0)
    img5 = cv2.imread('data/第二次数据/RGB_IR_head/IR_RGB_pair/RGB/right90.png', 0)
    RGBimg = [img1, img2, img3, img4, img5]

    # 将RGB和深度图打印在一起，观察配准结果
    for i in range(len(disparity)):
        plt.subplot(math.ceil(len(name)/lines_one_rows), lines_one_rows, i+1)
        plt.imshow(disparity[i])
        plt.title(name[i])
        plt.imshow(RGBimg[i], alpha=0.5)
    plt.savefig('data/第二次数据/RGB_IR_head/IR_RGB_pair/pair.png', dpi=300)
    plt.close()

    # rgbd = []
    # for i in range(len(name)):
    #     rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(RGBimg[i], disparity[i], convert_rgb_to_intensity=False)
    #     print(rgbd_image)

    #     inter = o3d.camera.PinholeCameraIntrinsic()
    #     inter.set_intrinsics(1280, 720, 599.795593, 599.633118, 645.792786, 372.238983)
    #     pcd = o3d.geometry.PointCloud().create_from_rgbd_image(
    #         rgbd_image, inter)

    #     # Flip it, otherwise the pointcloud will be upside down
    #     pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    #     o3d.visualization.draw_geometries([pcd])
