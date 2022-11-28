import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import package.func as func

num_plot_onerow = 3
outputpath = 'data/第二次数据/headResult/'
standard_distance = 600

if __name__ == '__main__':
    # 载入二值化数据
    img1 = cv2.imread('data/第二次数据/head/standard.png', 0)
    img2 = cv2.imread('data/第二次数据/head/front.png', 0)
    img3 = cv2.imread('data/第二次数据/head/left.png', 0)
    img4 = cv2.imread('data/第二次数据/head/right.png', 0)
    limg = [img1, img2, img3, img4]
    func.myplot(limg[1:], num_plot_onerow, outputpath + 'Binary.png')

    # 对二值化数据做半全局块匹配算法
    stereo = cv2.StereoSGBM_create(numDisparities=32, blockSize=11, P1=968, P2=3872)
    disparity = []
    standard_img = limg[0]
    for i in range(1, len(limg)):
        disparity_curr = stereo.compute(np.uint8(limg[i]), np.uint8(standard_img))
        disparity.append(disparity_curr)
    func.myplot(disparity, num_plot_onerow, outputpath + 'Binary_SGBM.png')

    # 去除噪声点，保留散斑点
    print('去除噪声点，保留散斑点------------------------------------')
    for i in range(len(limg)):
        limg[i] = func.ExcludeNoise(limg[i])

    # 对二值化去躁数据做半全局块匹配算法
    disparity = []
    standard_img = limg[0]
    for i in range(1, len(limg)):
        disparity_curr = stereo.compute(np.uint8(limg[i]), np.uint8(standard_img))
        disparity.append(disparity_curr)
    func.myplot(disparity, num_plot_onerow, outputpath + 'BinaryDenoise_SGBM.png')

    # 缩小点
    print('缩小点----------------------------------------------------')
    for i in range(len(limg)):
        limg[i] = func.reduce2point(limg[i])

    # 对缩小点数据做半全局块匹配算法
    disparity = []
    standard_img = limg[0]
    for i in range(1, len(limg)):
        disparity_curr = stereo.compute(np.uint8(limg[i]), np.uint8(standard_img))
        disparity.append(disparity_curr)
    func.myplot(disparity, num_plot_onerow, outputpath + 'BinaryReduce2Point_SGBM.png')

    # scipy.io.savemat('file_name.mat', {'data1':img1})
    # scipy.io.savemat('file_name2.mat', {'data2':img2})
    # cv2.imwrite('data/第一次数据/binary/838_thr.jpg', re1)
    # cv2.imwrite('data/第一次数据/binary/incline_thr.jpg', re2)
