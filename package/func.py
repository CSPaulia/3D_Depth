import numpy as np
import matplotlib.pyplot as plt
import math

# 去除噪声点，保留散斑点
def ExcludeNoise(image):
    newimg = np.zeros(image.shape)
    for row in range(image.shape[0]):
        for line in range(image.shape[1]):
            if row == 0 or row == image.shape[0]-1:
                newimg[row][line] = image[row][line]
            elif line == 0 or line == image.shape[1]-1:
                newimg[row][line] = image[row][line]
            else:
                if image[row][line] == 255:
                    neibour = image[row-1][line]/255 + image[row][line-1]/255 + image[row+1][line]/255 + image[row][line+1]/255
                    if (neibour == 2 and ((image[row-1][line]/255 + image[row+1][line]/255) == 1 or (image[row][line-1]/255 + image[row][line+1]/255) == 1)) or neibour >= 3:
                        newimg[row][line] = 255
    return newimg

# 缩小点
def reduce2point(image):
    newimg = image.copy()
    for row in range(newimg.shape[0]):
        for line in range(newimg.shape[1]):
            if newimg[row][line] == 255:
                stack = [(row, line)]
                record = [(row, line)]
                while len(stack) != 0:
                    r, l = stack.pop(0)
                    if r > 0:
                        if image[r-1][l] == 255:
                            if (r-1, l) not in record:
                                record.append((r-1, l))
                                stack.append((r-1, l))
                                newimg[r-1][l] = 0
                    if r < newimg.shape[0]-1:
                        if image[r+1][l] == 255:
                            if (r+1, l) not in record:
                                record.append((r+1, l))
                                stack.append((r+1, l))
                                newimg[r+1][l] = 0
                    if l > 0:
                        if image[r][l-1] == 255:
                            if (r, l-1) not in record:
                                record.append((r, l-1))
                                stack.append((r, l-1))
                                newimg[r][l-1] = 0
                    if l < newimg.shape[1]-1:
                        if image[r][l+1] == 255:
                            if (r, l+1) not in record:
                                record.append((r, l+1))
                                stack.append((r, l+1))
                                newimg[r][l+1] = 0
    return newimg

# 打印图片
def myplot(imgset, lines, filename):
    rows = math.ceil(len(imgset) / lines)
    fig, ax = plt.subplots(rows, lines)
    if rows == 1:
        for j in range(lines):
            if 1*(j+1) <= len(imgset):
                ax_last = ax[j].imshow(imgset[j])
    else:
        for i in range(rows):
            for j in range(lines):
                if (i+1)*(j+1) <= len(imgset):
                    ax_last = ax[i][j].imshow(imgset[i*lines + j])
    plt.colorbar(ax_last, ax=ax)
    plt.savefig(filename, dpi=300)
    plt.close()

# 分析精度/均方差误差
def MSEanalyse(arrset, outputpath, filename):
    meanset = [300]
    mseset = []
    for arr in arrset:
        newarr = arr[:int(0.6*arr.shape[0]), int(0.2*arr.shape[1]):]
        rows = newarr.shape[0]
        lines = newarr.shape[1]
        mean = np.sum(newarr) / 16 / (rows * lines) + 1
        error_sum = 0
        for r in range(rows):
            for l in range(lines):
                error_sum += (newarr[r][l] / 16 + 1 - mean) ** 2
        mse = error_sum / (rows * lines)
        meanset.append(- 49200 / (mean - 164))
        mseset.append(mse)
    x = list(np.arange(len(meanset)) * 100 + 300)
    y = list(np.arange(len(meanset)) * 100 + 300)
    plt.subplot(211)
    plt.title('Mean')
    plt.plot(x, y, ls='--', marker='o')
    plt.plot(x, meanset, marker='x')
    for i in range(len(y)):
        plt.text(x[i], y[i], round(y[i], 1), fontsize=9, color="black", style="italic", weight="light", verticalalignment='center',horizontalalignment='right')
    for i in range(len(meanset)):
        plt.text(x[i], meanset[i], round(meanset[i], 1), fontsize=9, color="black", style="italic", weight="light", verticalalignment='center',horizontalalignment='right')
    plt.xlabel('Distance(mm)')
    plt.ylabel('disparity')
    plt.legend(['Truth', 'Predicted'])
    plt.subplot(212)
    plt.title('MSE')
    plt.bar(x[1:], mseset, width = 50)
    for i in range(len(mseset)):
        plt.text(x[i+1]+25, mseset[i], round(mseset[i], 1), fontsize=9, color="black", style="italic", weight="light", verticalalignment='center',horizontalalignment='right')
    plt.xlabel('Distance(mm)')
    plt.ylabel('MSE Value')
    plt.savefig(outputpath + filename, dpi=300, bbox_inches='tight')
    plt.close()


