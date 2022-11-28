clear all
clc

I0 = imread('data/第二次数据/RGB_IR_head/IR/standard_binary.png');

I1 = imread('data/第二次数据/RGB_IR_head/IR/right90_binary.png');%读取左右图片
I2 = imread('data/第二次数据/RGB_IR_head/cut_RGB/right90_rgb.png');
I3 = imread('data/第二次数据/RGB_IR_head/IR/right45_binary.png');%读取左右图片
I4 = imread('data/第二次数据/RGB_IR_head/cut_RGB/right45_rgb.png');
I5 = imread('data/第二次数据/RGB_IR_head/IR/front_binary.png');%读取左右图片
I6 = imread('data/第二次数据/RGB_IR_head/cut_RGB/front_rgb.png');
I7 = imread('data/第二次数据/RGB_IR_head/IR/left45_binary.png');%读取左右图片
I8 = imread('data/第二次数据/RGB_IR_head/cut_RGB/left45_rgb.png');
I9 = imread('data/第二次数据/RGB_IR_head/IR/left90_binary.png');%读取左右图片
I10 = imread('data/第二次数据/RGB_IR_head/cut_RGB/left90_rgb.png');
% figure
% imshowpair(I1, I2, 'montage');
% title('Original Images');

%加载stereoParameters对象。
load('data/第一次数据/新标定结果/stereoParams.mat');%加载你保存的相机标定的mat

[J0, Jany] = rectifyStereoImages(I0, I2, stereoParams);

[J1, J2] = rectifyStereoImages(I1, I2, stereoParams);
[J3, J4] = rectifyStereoImages(I3, I4, stereoParams);
[J5, J6] = rectifyStereoImages(I5, I6, stereoParams);
[J7, J8] = rectifyStereoImages(I7, I8, stereoParams);
[J9, J10] = rectifyStereoImages(I9, I10, stereoParams);
% figure
imwrite(J0, 'data/第二次数据/RGB_IR_head/IR_RGB_pair/IR/standard.png');

imwrite(J1, 'data/第二次数据/RGB_IR_head/IR_RGB_pair/IR/right90.png');
imwrite(J2, 'data/第二次数据/RGB_IR_head/IR_RGB_pair/RGB/right90.png');
imwrite(J3, 'data/第二次数据/RGB_IR_head/IR_RGB_pair/IR/right45.png');
imwrite(J4, 'data/第二次数据/RGB_IR_head/IR_RGB_pair/RGB/right45.png');
imwrite(J5, 'data/第二次数据/RGB_IR_head/IR_RGB_pair/IR/front.png');
imwrite(J6, 'data/第二次数据/RGB_IR_head/IR_RGB_pair/RGB/front.png');
imwrite(J7, 'data/第二次数据/RGB_IR_head/IR_RGB_pair/IR/left45.png');
imwrite(J8, 'data/第二次数据/RGB_IR_head/IR_RGB_pair/RGB/left45.png');
imwrite(J9, 'data/第二次数据/RGB_IR_head/IR_RGB_pair/IR/left90.png');
imwrite(J10, 'data/第二次数据/RGB_IR_head/IR_RGB_pair/RGB/left90.png');
% imshowpair(J1, J2, 'montage');
% title('Undistorted Images');
