clear all
clc

I0 = imread('data/�ڶ�������/RGB_IR_head/IR/standard_binary.png');

I1 = imread('data/�ڶ�������/RGB_IR_head/IR/right90_binary.png');%��ȡ����ͼƬ
I2 = imread('data/�ڶ�������/RGB_IR_head/cut_RGB/right90_rgb.png');
I3 = imread('data/�ڶ�������/RGB_IR_head/IR/right45_binary.png');%��ȡ����ͼƬ
I4 = imread('data/�ڶ�������/RGB_IR_head/cut_RGB/right45_rgb.png');
I5 = imread('data/�ڶ�������/RGB_IR_head/IR/front_binary.png');%��ȡ����ͼƬ
I6 = imread('data/�ڶ�������/RGB_IR_head/cut_RGB/front_rgb.png');
I7 = imread('data/�ڶ�������/RGB_IR_head/IR/left45_binary.png');%��ȡ����ͼƬ
I8 = imread('data/�ڶ�������/RGB_IR_head/cut_RGB/left45_rgb.png');
I9 = imread('data/�ڶ�������/RGB_IR_head/IR/left90_binary.png');%��ȡ����ͼƬ
I10 = imread('data/�ڶ�������/RGB_IR_head/cut_RGB/left90_rgb.png');
% figure
% imshowpair(I1, I2, 'montage');
% title('Original Images');

%����stereoParameters����
load('data/��һ������/�±궨���/stereoParams.mat');%�����㱣�������궨��mat

[J0, Jany] = rectifyStereoImages(I0, I2, stereoParams);

[J1, J2] = rectifyStereoImages(I1, I2, stereoParams);
[J3, J4] = rectifyStereoImages(I3, I4, stereoParams);
[J5, J6] = rectifyStereoImages(I5, I6, stereoParams);
[J7, J8] = rectifyStereoImages(I7, I8, stereoParams);
[J9, J10] = rectifyStereoImages(I9, I10, stereoParams);
% figure
imwrite(J0, 'data/�ڶ�������/RGB_IR_head/IR_RGB_pair/IR/standard.png');

imwrite(J1, 'data/�ڶ�������/RGB_IR_head/IR_RGB_pair/IR/right90.png');
imwrite(J2, 'data/�ڶ�������/RGB_IR_head/IR_RGB_pair/RGB/right90.png');
imwrite(J3, 'data/�ڶ�������/RGB_IR_head/IR_RGB_pair/IR/right45.png');
imwrite(J4, 'data/�ڶ�������/RGB_IR_head/IR_RGB_pair/RGB/right45.png');
imwrite(J5, 'data/�ڶ�������/RGB_IR_head/IR_RGB_pair/IR/front.png');
imwrite(J6, 'data/�ڶ�������/RGB_IR_head/IR_RGB_pair/RGB/front.png');
imwrite(J7, 'data/�ڶ�������/RGB_IR_head/IR_RGB_pair/IR/left45.png');
imwrite(J8, 'data/�ڶ�������/RGB_IR_head/IR_RGB_pair/RGB/left45.png');
imwrite(J9, 'data/�ڶ�������/RGB_IR_head/IR_RGB_pair/IR/left90.png');
imwrite(J10, 'data/�ڶ�������/RGB_IR_head/IR_RGB_pair/RGB/left90.png');
% imshowpair(J1, J2, 'montage');
% title('Undistorted Images');
