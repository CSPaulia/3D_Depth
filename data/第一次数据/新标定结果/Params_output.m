rowName = cell(1,10);
rowName{1,1} = 'ƽ�ƾ���';
rowName{1,2} = '��ת����';
rowName{1,3} = '���1�ڲξ���';
rowName{1,4} = '���1�������';
rowName{1,5} = '���1�������';
rowName{1,6} = '���2�ڲξ���';
rowName{1,7} = '���2�������';
rowName{1,8} = '���2�������';
rowName{1,9} = '���1��������';
rowName{1,10} = '���2��������';
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
xlswrite('out.xlsx',stereoParams.TranslationOfCamera2,1,'B1');  % ƽ�ƾ���
xlswrite('out.xlsx',stereoParams.RotationOfCamera2.',1,'B2');  % ��ת����
xlswrite('out.xlsx',stereoParams.CameraParameters1.IntrinsicMatrix.',1,'B5');  % ���1�ڲξ���
xlswrite('out.xlsx',stereoParams.CameraParameters1.RadialDistortion,1,'B8');  % ���1�������(1,2,5)
xlswrite('out.xlsx',stereoParams.CameraParameters1.TangentialDistortion,1,'B9');  % ���1�������(3,4)
xlswrite('out.xlsx',stereoParams.CameraParameters2.IntrinsicMatrix.',1,'B10');  % ���2�ڲξ���
xlswrite('out.xlsx',stereoParams.CameraParameters2.RadialDistortion,1,'B13');  % ���2�������(1,2,5)
xlswrite('out.xlsx',stereoParams.CameraParameters2.TangentialDistortion,1,'B14');  % ���2�������(3,4)
xlswrite('out.xlsx',[stereoParams.CameraParameters1.RadialDistortion(1:2), stereoParams.CameraParameters1.TangentialDistortion,...
    stereoParams.CameraParameters1.RadialDistortion(3)],1,'B15');  % ���1��������
xlswrite('out.xlsx',[stereoParams.CameraParameters2.RadialDistortion(1:2), stereoParams.CameraParameters2.TangentialDistortion,...
    stereoParams.CameraParameters2.RadialDistortion(3)],1,'B16');  % ���2��������

