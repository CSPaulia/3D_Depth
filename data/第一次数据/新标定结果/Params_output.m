rowName = cell(1,10);
rowName{1,1} = '平移矩阵';
rowName{1,2} = '旋转矩阵';
rowName{1,3} = '相机1内参矩阵';
rowName{1,4} = '相机1径向畸变';
rowName{1,5} = '相机1切向畸变';
rowName{1,6} = '相机2内参矩阵';
rowName{1,7} = '相机2径向畸变';
rowName{1,8} = '相机2切向畸变';
rowName{1,9} = '相机1畸变向量';
rowName{1,10} = '相机2畸变向量';
xlswrite('out.xlsx',rowName(1,1),1,'A1');
xlswrite('out.xlsx',rowName(1,2),1,'A2');
xlswrite('out.xlsx',rowName(1,3),1,'A5');
xlswrite('out.xlsx',rowName(1,4),1,'A8');
xlswrite('out.xlsx',rowName(1,5),1,'A9');
xlswrite('out.xlsx',rowName(1,6),1,'A10');
xlswrite('out.xlsx',rowName(1,7),1,'A13');
xlswrite('out.xlsx',rowName(1,8),1,'A14');
xlswrite('out.xlsx',rowName(1,9),1,'A15');
xlswrite('out.xlsx',rowName(1,10),1,'A16');
xlswrite('out.xlsx',stereoParams.TranslationOfCamera2,1,'B1');  % 平移矩阵
xlswrite('out.xlsx',stereoParams.RotationOfCamera2.',1,'B2');  % 旋转矩阵
xlswrite('out.xlsx',stereoParams.CameraParameters1.IntrinsicMatrix.',1,'B5');  % 相机1内参矩阵
xlswrite('out.xlsx',stereoParams.CameraParameters1.RadialDistortion,1,'B8');  % 相机1径向畸变(1,2,5)
xlswrite('out.xlsx',stereoParams.CameraParameters1.TangentialDistortion,1,'B9');  % 相机1切向畸变(3,4)
xlswrite('out.xlsx',stereoParams.CameraParameters2.IntrinsicMatrix.',1,'B10');  % 相机2内参矩阵
xlswrite('out.xlsx',stereoParams.CameraParameters2.RadialDistortion,1,'B13');  % 相机2径向畸变(1,2,5)
xlswrite('out.xlsx',stereoParams.CameraParameters2.TangentialDistortion,1,'B14');  % 相机2切向畸变(3,4)
xlswrite('out.xlsx',[stereoParams.CameraParameters1.RadialDistortion(1:2), stereoParams.CameraParameters1.TangentialDistortion,...
    stereoParams.CameraParameters1.RadialDistortion(3)],1,'B15');  % 相机1畸变向量
xlswrite('out.xlsx',[stereoParams.CameraParameters2.RadialDistortion(1:2), stereoParams.CameraParameters2.TangentialDistortion,...
    stereoParams.CameraParameters2.RadialDistortion(3)],1,'B16');  % 相机2畸变向量

