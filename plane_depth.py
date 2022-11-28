# 下面就是对以上三种设置阈值方式的一个例子
import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import package.func as func

num_plot_onerow = 3
outputpath = 'data/第二次数据/PlaneDepthResult/'

if __name__ == '__main__':
    # 载入二值化数据
    img1 = cv2.imread('data/第二次数据/PlaneDepthData/300.png', 0)
    img2 = cv2.imread('data/第二次数据/PlaneDepthData/400.png', 0)
    img3 = cv2.imread('data/第二次数据/PlaneDepthData/500.png', 0)
    img4 = cv2.imread('data/第二次数据/PlaneDepthData/600.png', 0)
    img5 = cv2.imread('data/第二次数据/PlaneDepthData/700.png', 0)
    img6 = cv2.imread('data/第二次数据/PlaneDepthData/800.png', 0)
    img7 = cv2.imread('data/第二次数据/PlaneDepthData/900.png', 0)
    limg = [img1, img2, img3, img4, img5, img6, img7]
    func.myplot(limg[1:], num_plot_onerow, outputpath + 'Binary.png')

    # # 自适应二值化
    # print('自适应二值化----------------------------------------------')
    # th1 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    # th2 = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    # # ret1, th1 = cv2.threshold(img1, 30, 255, cv2.THRESH_BINARY)
    # # ret2, th2 = cv2.threshold(img2, 20, 255, cv2.THRESH_BINARY)
    # plt.subplot(1,2,1)
    # plt.imshow(th1)
    # plt.subplot(1,2,2)
    # plt.imshow(th2)
    # plt.show()

    # 对二值化数据做半全局块匹配算法
    stereo = cv2.StereoSGBM_create(numDisparities=128, blockSize=11, P1=121, P2=484)
    disparity = []
    standard_img = limg[0]
    for i in range(1, len(limg)):
        disparity_curr = stereo.compute(np.uint8(standard_img), np.uint8(limg[i]))
        disparity.append(disparity_curr)
    func.MSEanalyse(disparity, outputpath=outputpath, filename='Binary_Analysis.png')
    func.myplot(disparity, num_plot_onerow, outputpath + 'Binary_SGBM_300standard.png')

    # 去除噪声点，保留散斑点
    print('去除噪声点，保留散斑点------------------------------------')
    ex_noise = func.ExcludeNoise(limg[0])
    plt.subplot(1,2,1)
    plt.imshow(limg[0][400:450, 512:562])
    plt.title('With Noise')
    plt.subplot(1,2,2)
    plt.imshow(ex_noise[400:450, 512:562])
    plt.title('Denoised')
    plt.savefig('data/第二次数据/PlaneDepthResult/BinaryDenoise.png')
    for i in range(len(limg)):
        limg[i] = func.ExcludeNoise(limg[i])

    # 对二值化去躁数据做半全局块匹配算法
    disparity = []
    standard_img = limg[0]
    for i in range(1, len(limg)):
        disparity_curr = stereo.compute(np.uint8(standard_img), np.uint8(limg[i]))
        disparity.append(disparity_curr)
    func.MSEanalyse(disparity, outputpath=outputpath, filename='BinaryDenoise_Analysis.png')
    func.myplot(disparity, num_plot_onerow, outputpath + 'BinaryDenoise_SGBM_300standard.png')

    # 缩小点
    print('缩小点----------------------------------------------------')
    re1 = func.reduce2point(img1)
    plt.subplot(1,2,1)
    plt.imshow(img1[400:450, 512:562])
    plt.title('Without Suppressing')
    plt.subplot(1,2,2)
    plt.imshow(re1[400:450, 512:562])
    plt.title('Suppressed')
    plt.savefig('data/第二次数据/PlaneDepthResult/BinaryReduce2Point.png')
    for i in range(len(limg)):
        limg[i] = func.reduce2point(limg[i])

    # 对缩小点数据做半全局块匹配算法
    disparity = []
    standard_img = limg[0]
    for i in range(1, len(limg)):
        disparity_curr = stereo.compute(np.uint8(standard_img), np.uint8(limg[i]))
        disparity.append(disparity_curr)
    func.MSEanalyse(disparity, outputpath=outputpath, filename='BinaryReduce2Point_Analysis.png')
    func.myplot(disparity, num_plot_onerow, outputpath + 'BinaryReduce2Point_SGBM_300standard.png')

    # scipy.io.savemat('file_name.mat', {'data1':img1})
    # scipy.io.savemat('file_name2.mat', {'data2':img2})
    # cv2.imwrite('data/第一次数据/binary/838_thr.jpg', re1)
    # cv2.imwrite('data/第一次数据/binary/incline_thr.jpg', re2)
