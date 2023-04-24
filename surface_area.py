import matplotlib.pyplot as plt
import pyvista as pv
from pyvista import examples
from pyvista.core.pointset import PolyData
from pyvista.utilities.reader import STLReader
from typing import List, Tuple
import numpy as np
from PIL import Image
import cv2
import math

def rotateObj(reader: STLReader, rotList: Tuple[int, int, int], camScale: int):
    p = pv.Plotter(off_screen=True)
    obj = reader.read()

    rot = obj.rotate_x(rotList[0], point=obj.center, inplace=True)
    rot = obj.rotate_y(rotList[1], point=obj.center, inplace=True)
    rot = obj.rotate_z(rotList[2], point=obj.center, inplace=True)

    normal = (0, 0, 1)
    projected = rot.project_points_to_plane(origin=rot.center, normal=normal)
    
    p.add_mesh(projected, show_scalar_bar=False)
    
    p.camera_position = 'xy'
    p.camera.SetParallelProjection(True)
    p.window_size = (max(p.window_size), max(p.window_size))
    p.camera.parallel_scale = camScale

    # p.show()

    screenshot = p.screenshot()
    # p.close()
    
    return(screenshot)

def rotate_get_scale(reader: STLReader, rotList: Tuple[int, int, int]):
    p = pv.Plotter(off_screen=True)
    obj = reader.read()

    rot = obj.rotate_x(rotList[0], point=obj.center, inplace=True)
    rot = obj.rotate_y(rotList[1], point=obj.center, inplace=True)
    rot = obj.rotate_z(rotList[2], point=obj.center, inplace=True)
    
    normal = (1, 0, 0)
    projected = rot.project_points_to_plane(origin=rot.center, normal=normal)
    
    p.add_mesh(projected, show_scalar_bar=False)
    
    p.camera_position = 'yz'
    p.camera.SetParallelProjection(True)
    p.window_size = (max(p.window_size), max(p.window_size))
    camScale = p.camera.parallel_scale

    p.close()
    
    return(camScale)

def getWhiteVals(imarray):
    percent_vals = []
    
    for idx, x in enumerate(imarray):
        x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)

        ret, binary = cv2.threshold(x,76,255,cv2.THRESH_BINARY)
        pixel_count = x.shape[0] * x.shape[1]
        white_count = np.sum(binary == 255)

        # print(f"{pixel_count}, {white_count}")
        # print(round(100*white_count / pixel_count, 2))

        percent_vals.append(round(100*white_count / pixel_count, 2))
    
    return(percent_vals)

def maxmin_tuple(x, y):
    ymax = max(y)
    xpos = y.index(ymax)
    xmax = x[xpos]
    
    ymin = min(y)
    _xpos = y.index(ymin)
    xmin = x[_xpos]
    
    return([xmax, ymax], [xmin, ymin])

def itr_rotate(y_min: int, y_max: int, y_step: int, z_min: int, z_max: int, z_step: int, path: str, camScale: int = 0.25):
    synapse_name = (path.split("/")[-1]).split(".")[0]
    syn_reader = pv.get_reader(path)

    circ_Imgs = []
    maxSurfaceArea = [0, 0, 0] #X, Y, Value
    surfaceAreaVals = []

    for i in range(y_min, y_max, y_step):
        itr_arr = []

        for j in range(z_min, z_max, z_step):
            screenshot = rotateObj(syn_reader, (0, i, j), camScale)        
            itr_arr.append(screenshot)

            ss_w = getWhiteVals([screenshot])
            
            surfaceAreaVals.append(ss_w[0])

            if(ss_w[0] > maxSurfaceArea[2]):
                maxSurfaceArea[0], maxSurfaceArea[1], maxSurfaceArea[2] = i, j, ss_w[0]

        circ_Imgs.append(itr_arr)
        # circ_ar = cv2.hconcat(itr_arr)
        # plt.imshow(circ_ar)
        # plt.axis('off')
        # plt.show()
    
    return(circ_Imgs, maxSurfaceArea, surfaceAreaVals)

def find_scale(y_min: int, y_max: int, y_step: int, z_min: int, z_max: int, z_step: int, path: str):
    synapse_name = (path.split("/")[-1]).split(".")[0]
    syn_reader = pv.get_reader(path)

    camScales = []

    for i in range(y_min, y_max, y_step):

        for j in range(z_min, z_max, z_step):
            camScale = rotate_get_scale(syn_reader, (0, i, j))        
            camScales.append(camScale)
    
    # print(f"Max: {max(camScales)}")
    return(max(camScales))

