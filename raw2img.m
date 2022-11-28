clear
close all

row = 800;%172;
col = 1280;%224;

rawpath = 'data/第一次数据/1/';
rawfiles = dir(rawpath);
outputpath = 'data/第一次数据/new1/';

for num = 1:length(rawfiles)
    filename = rawfiles(num).name;
    
    houzhui = split(filename, '.');
    houzhui = houzhui{length(houzhui), 1};
    if length(houzhui) ~= length('raw')
        continue
    else
        if houzhui ~= 'raw'
            continue
        end
    end
    
    filefullpath = [rawpath, filename];
    
    fid = fopen(filefullpath,'r');%DepthRawData153216.raw

    X1 = fread(fid,[col row],'uint16');

    fclose(fid);

    X1 = X1';        
    img = zeros(row,col);

    for i = 1 : row
        for j = 1 : col

            u = X1(i,j);
            u_tmp1 = u;
            u_tmp2 = bitand(255,u_tmp1);
            img(i,j) = u_tmp2;

        end
    end

%     figure
%     imshow(img/max(img(:)))

    outputname = split(filename, '.');
    outputname = [outputpath, outputname{1, 1}, '.jpg'];
    imwrite(uint8(img),outputname);
end
