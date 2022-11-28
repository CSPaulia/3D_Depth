import cv2
import matplotlib.pyplot as plt
import numpy as np
import open3d as o3d

# 相机的各项参数
camera1distortion = np.array([0.116722801, -1.343375256, -0.00142143, -0.010576243, 6.821516253], dtype=np.float32)
camera2distortion = np.array([0.032348072, -2.204192406, 0.004165376, 0.006963582, 15.14635052], dtype=np.float32)
camera1intrinsic = np.array([[858.1827298, 0, 390.7019938], [0, 856.6768172, 660.320222], [0, 0, 1]], dtype=np.float32)
camera2intrinsic = np.array([[1107.406514, 0, 419.2635608], [0, 1110.734518, 645.1954891], [0, 0, 1]], dtype=np.float32)
Translation = [-18.01092415, -0.633399715, -1.668213293]
Rotation = [[0.999518296, 0.000945023, -0.031020683], [-0.00113284, 0.999981132, -0.006037569], [0.031014392, 0.006069802, 0.999500508]]

if __name__ == '__main__':
    # img_ir = cv2.imread('data/第二次数据/RGB_IR_head/IR/front_binary.png')
    # img_rgb = cv2.imread('data/第二次数据/RGB_IR_head/cut_RGB/front_rgb.png')
    # h1, w1 = img_ir.shape[:2]
    # h2, w2 = img_rgb.shape[:2]
    # dst1 = cv2.undistort(img_ir, camera1intrinsic, camera1distortion)
    # dst2 = cv2.undistort(img_rgb, camera2intrinsic, camera2distortion)
    # r = np.dot(Rotation, camera2intrinsic)
    # r = np.dot(np.linalg.inv(camera1intrinsic), r)
    # dst2 = cv2.perspectiveTransform(dst2)
    # plt.imshow(dst1)
    # plt.show()
    # plt.close()
    # plt.imshow(dst2)
    # plt.show()
    # plt.close()

    # 读入面部RGB数据以及深度数据，通过函数得到RGBD图像
    color_raw = o3d.io.read_image("data/第二次数据/RGB_IR_head/IR_RGB_pair/RGB/front.png")
    depth_raw = o3d.io.read_image("data/第二次数据/RGB_IR_head/IR_RGB_pair/IR_Disparity/front_disparity.png")
    rgbd_image_front = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw, convert_rgb_to_intensity=True)
    color_raw = o3d.io.read_image("data/第二次数据/RGB_IR_head/IR_RGB_pair/RGB/right45.png")
    depth_raw = o3d.io.read_image("data/第二次数据/RGB_IR_head/IR_RGB_pair/IR_Disparity/right45_disparity.png")
    rgbd_image_right45 = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw, convert_rgb_to_intensity=True)
    color_raw = o3d.io.read_image("data/第二次数据/RGB_IR_head/IR_RGB_pair/RGB/right90.png")
    depth_raw = o3d.io.read_image("data/第二次数据/RGB_IR_head/IR_RGB_pair/IR_Disparity/right90_disparity.png")
    rgbd_image_right90 = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw, convert_rgb_to_intensity=True)
    color_raw = o3d.io.read_image("data/第二次数据/RGB_IR_head/IR_RGB_pair/RGB/left45.png")
    depth_raw = o3d.io.read_image("data/第二次数据/RGB_IR_head/IR_RGB_pair/IR_Disparity/left45_disparity.png")
    rgbd_image_left45 = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw, convert_rgb_to_intensity=True)
    color_raw = o3d.io.read_image("data/第二次数据/RGB_IR_head/IR_RGB_pair/RGB/left90.png")
    depth_raw = o3d.io.read_image("data/第二次数据/RGB_IR_head/IR_RGB_pair/IR_Disparity/left90_disparity.png")
    rgbd_image_left90 = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw, convert_rgb_to_intensity=True)
    
    print(rgbd_image_front)

    # 查看RGBD图像
    # plt.subplot(1, 2, 1)
    # plt.title('Redwood grayscale image')
    # plt.imshow(rgbd_image.color)
    # plt.subplot(1, 2, 2)
    # plt.title('Redwood depth image')
    # plt.imshow(rgbd_image.depth)
    # plt.show()

    # 根据相机内参和RGBD图像得到3D点云
    inter = o3d.camera.PinholeCameraIntrinsic()
    inter.set_intrinsics(1280, 800, 858.1827298/4, 856.6768172/4, 390.7019938/4, 660.320222/4)
    pcd_front = o3d.geometry.PointCloud().create_from_rgbd_image(rgbd_image_front, inter)
    pcd_right45 = o3d.geometry.PointCloud().create_from_rgbd_image(rgbd_image_right45, inter)
    pcd_left45 = o3d.geometry.PointCloud().create_from_rgbd_image(rgbd_image_left45, inter)
    # pcd_left90 = o3d.geometry.PointCloud().create_from_rgbd_image(rgbd_image_left90, inter)

    # 对点云数据进行降采样以及边界去除
    pcd_front = pcd_front.uniform_down_sample(every_k_points=5)
    pcd_right45 = pcd_right45.uniform_down_sample(every_k_points=5)
    pcd_left45 = pcd_left45.uniform_down_sample(every_k_points=5)
    # pcd_left90 = pcd_left90.uniform_down_sample(every_k_points=5)
    print(pcd_front.points) 
    # pcd_front, _ = pcd_front.remove_radius_outlier(nb_points=100, radius=0.00008, print_progress=True)
    pcd_front, _ = pcd_front.remove_radius_outlier(nb_points=100, radius=0.00008, print_progress=True)
    # pcd_right90, _ = pcd_right90.remove_radius_outlier(nb_points=100, radius=0.00003, print_progress=True)
    # pcd_right45, _ = pcd_right45.remove_radius_outlier(nb_points=100, radius=0.000025, print_progress=True)
    pcd_right45, _ = pcd_right45.remove_radius_outlier(nb_points=100, radius=0.00008, print_progress=True)
    pcd_left45, _ = pcd_left45.remove_radius_outlier(nb_points=100, radius=0.0001, print_progress=True)
    # pcd_left90, _ = pcd_left90.remove_radius_outlier(nb_points=100, radius=0.00007, print_progress=True)

    print(pcd_front.points)

    # 设置初始矩阵以及阈值
    threshold = 0.00001  #移动范围的阀值
    trans_init = np.asarray([[0.574,0,0.819,-0.0003],   # 4x4 identity matrix，这是一个转换矩阵，
                            [0,1,0,0],   # 象征着没有任何位移，没有任何旋转，我们输入
                            [-0.819,0,0.574,0.000325],   # 这个矩阵为初始变换
                            [0,0,0,1]])
    trans_init2 = np.asarray([[0.799,0,-0.602,0.00035],   # 4x4 identity matrix，这是一个转换矩阵，
                            [0,1,0,0.00003],   # 象征着没有任何位移，没有任何旋转，我们输入
                            [0.602,0,0.799,0.000025],   # 这个矩阵为初始变换
                            [0,0,0,1]])
    # trans_init2 = np.asarray([[0.5,0,-0.866,0.00035],   # 4x4 identity matrix，这是一个转换矩阵，
    #                         [0,1,0,-0.00003],   # 象征着没有任何位移，没有任何旋转，我们输入
    #                         [0.866,0,0.5,0],   # 这个矩阵为初始变换
    #                         [0,0,0,1]])

    # 运行icp
    reg_p2p = o3d.pipelines.registration.registration_icp(pcd_front, pcd_right45, threshold, trans_init, o3d.pipelines.registration.TransformationEstimationPointToPoint())
    reg_p2p2 = o3d.pipelines.registration.registration_icp(pcd_front, pcd_left45, threshold, trans_init2, o3d.pipelines.registration.TransformationEstimationPointToPoint())
    # reg_p2p2 = o3d.pipelines.registration.registration_icp(pcd_front, pcd_left90, threshold, trans_init2, o3d.pipelines.registration.TransformationEstimationPointToPoint())
    print(reg_p2p)
    print("Transformation is:")
    print(reg_p2p.transformation)

    pcd_right45.transform(reg_p2p.transformation)
    pcd_left45.transform(reg_p2p2.transformation)
    # pcd_left90.transform(reg_p2p2.transformation)

    vis = o3d.visualization.Visualizer()
    vis.create_window()

    #将三个点云放入visualizer
    vis.add_geometry(pcd_front)
    vis.add_geometry(pcd_right45)
    vis.add_geometry(pcd_left45)
    # vis.add_geometry(pcd_left90)

    # #让visualizer渲染点云
    # vis.update_geometry()
    # vis.poll_events()
    # vis.update_renderer()

    vis.run()

    # # Flip it, otherwise the pointcloud will be upside down
    # pcd_front.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    # o3d.visualization.draw_geometries([processed_pcd_front])
