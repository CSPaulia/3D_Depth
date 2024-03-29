# 三维深度感知

$resize.py$：由于采集到的RGB数据和IR数据大小是不一样的，所以需要裁剪较大的图像并放缩至和另一份图像相同大小。这里选择的是将较大的RGB图像进行裁剪并放缩至和IR图像相同大小。

$plane\_depth.py$：运行此文件可以得到平面深度图。注意输入和输出，输入为二值化图像，第一张图像为参考平面。也可以取消二值化注释，这样可以输入原始散斑图。

$complexscene\_depth.py$：运行此文件可以得到复杂场景深度图。注意输入和输出，输入为二值化图像，第一张图像为参考平面。

$head\_depth.py$：运行此文件可以得到人脸模型深度图。注意输入和输出，输入为二值化图像，第一张图像为参考平面。

$rectifyStereoImage.m$：配准RGB图像和IR图像。

$Matlab\_Remapping\_Plot.py$：将$rectifyStereoImage.m$配准的RGB图像和深度图交叠在一起，观察配准效果。

$3D\_ICP.py$：运行此文件可以得到3D人脸模型。注意输入，输入为RGB图像和深度图像。

$package/func.py$：这里包含了去噪函数、缩小点函数、打印图片函数、精度分析函数。

其他：标定主要用的是$data/第一次数据$，散斑图、深度图、RGB图主要用的是$data/第二次数据$。