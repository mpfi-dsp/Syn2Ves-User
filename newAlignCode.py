import matplotlib.pyplot as plt
import pyvista as pv
from typing import List, Tuple
import pandas as pd
import numpy as np
from PIL import Image, ImageEnhance, ImageOps
import os
import cv2
import math
import time
from datetime import datetime
from surface_area import getWhiteVals, maxmin_tuple
import re
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QThread, QSize, QByteArray
import logging

def destroyPlot(plotter: pv.Plotter):
    plotter.close()
    plotter._theme = None
    del plotter

def num_sort(sortList):
    sortList.sort(key=lambda test_string : list(map(int, re.findall(r'\d+', test_string)))[0])
    return(sortList)

def brightnessLines(images_arr, low, high, step, _low = [], _high = [], _step = []):
    degree_nums = range(low, high, step)

    if _low == []:
        _low = low
    if _high == []:
        _high = high
    if _step == []:
        _step = step

    for idx, x in enumerate(images_arr):
        whites = getWhiteVals(x)
        plt.plot(degree_nums, whites, label=str(range(_low, _high, _step)[idx]))
        _max, _min = maxmin_tuple(degree_nums, whites)
        plt.scatter(_max[0], _max[1])
    plt.legend(loc="upper right")
    plt.xticks(np.arange(-90, 135, 45))
    plt.show()

def brightnessGraph(values_arr, images_arr, start = 0.25, end = 1):
    brightArr = np.empty_like(images_arr)

    width = end - start
    norm_values = (values_arr-np.min(values_arr))/(np.max(values_arr)-np.min(values_arr)) * width + start

    for i in range(len(images_arr)):
        for j in range(len(images_arr[i])):
            img = images_arr[i][j]
            bright_img = Image.fromarray(img.astype('uint8'), 'RGB')
            # bright_img = bright_img.convert('L')
            enhancer = ImageEnhance.Brightness(bright_img)
            bright_img = enhancer.enhance(norm_values[i][j])

            if(norm_values[i][j] == np.amax(norm_values)):
                bright_img = bright_img.convert('L')
                bright_img = ImageOps.colorize(bright_img, black="black", white="green")

            brightArr[i][j] = np.array(bright_img)

    brightTile = concat_tile(brightArr)

    # plt.imshow(brightTile)
    # plt.show()
    return(brightTile)

def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])

def arccos(adj, hyp, opp, mult = 1):

    if(adj != 0):
        _arccos = mult * 57.2958 * np.arccos(((adj**2 + hyp**2) - opp**2) / (2 * adj * hyp))
    else:
        _arccos = 180

    return(_arccos)

def getTriangle(p1, center, p3): 
    p4 = ((p1[0]+p3[0])/2, (p1[1]+p3[1])/2)

    opp = math.dist((p1[0], p1[1]), p4)
    adj = math.dist((center[0], center[1]), p4)
    hyp = math.dist((center[0], center[1]), (p1[0], p1[1]))

    return(opp, adj, hyp, p3, p4)

def surfaceAreaAngle(path: str, camScales: list, x_range: list, y_range: list, z_og: float = 0, y_og: float = 0, center_og: tuple = (0, 0, 0)):
    surfAreaImgs = []
    surfAreaVals = []

    p = pv.Plotter(off_screen=True, window_size=[200, 200])

    for i in x_range:

        iterImgs = []
        iterVals = []

        for j in y_range:
            p.clear()

            sy_reader = pv.get_reader(path)
            synapse = sy_reader.read()

            synapse.rotate_z(z_og, center_og, inplace=True)
            synapse.rotate_y(y_og, center_og, inplace=True)

            synapse.rotate_x(i, synapse.center, inplace=True)
            synapse.rotate_y(j, synapse.center, inplace=True)

            p.add_mesh(synapse, lighting=False)

            p.camera.SetParallelProjection(True)
            p.camera_position = 'xy'
            p.camera.parallel_scale = max(camScales)

            ss = p.screenshot()

            iterImgs.append(ss)

            _ss = cv2.cvtColor(ss, cv2.COLOR_BGR2GRAY)
            ret, binary = cv2.threshold(_ss,76,255,cv2.THRESH_BINARY)
            pixel_count = _ss.shape[0] * _ss.shape[1]
            white_count = np.sum(binary == 255)
            whiteRatio = round(100*white_count / pixel_count, 2)
            iterVals.append(whiteRatio)
        
        surfAreaImgs.append(iterImgs)
        surfAreaVals.append(iterVals)

    destroyPlot(p)
    
    return(surfAreaVals, surfAreaImgs)

def Syn2Ves(syn_path: str, ves_path: str, pairing: List[Tuple[int, int]], pb: pyqtSignal, outFilePath: str = ""):
    camVesPos_x = []
    camVesPos_y = []
    camVesPos_z = []

    synPos_x = []
    synPos_y = []
    synPos_z = []

    sfaVesPos_x = []
    sfaVesPos_y = []
    sfaVesPos_z = []

    vesAngle = []
    intersectVals = []
    iouVals = []
    iosVals = []

    synFiles = num_sort(os.listdir(syn_path))
    vesFiles = num_sort(os.listdir(ves_path))

    pairing = pairing[:5]
    
    for i in range(len(pairing)):

        print(i/len(pairing) * 100)
        pb.emit(int(i/len(pairing) * 100))

        syn = os.path.join(syn_path, synFiles[pairing[i][0]-1])
        ves = os.path.join(ves_path, vesFiles[pairing[i][1]-1])

        print(f"SYN: {pairing[i][0]}, VES: {pairing[i][1]}")
        logging.info(f"SYN: {pairing[i][0]}, VES: {pairing[i][1]}")

        sy_reader = pv.get_reader(syn)
        ves_reader = pv.get_reader(ves)

        synapse = sy_reader.read()
        vesicle = ves_reader.read()

        p = pv.Plotter(off_screen=True)

        p1 = tuple(synapse.center)
        p2 = tuple(vesicle.center)

        # ===========================================================

        center = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2, (p1[2]+p2[2])/2)
        radius = math.sqrt(pow((p1[0] - center[0]), 2) + pow((p1[1] - center[1]), 2))
        p3 = (center[0] - radius, center[1])

        opp, adj, hyp, p3, p4 = getTriangle(p1, center, p3)

        if(p1[1] > p3[1]):
            z_arccos = arccos(adj, hyp, opp, 2)
        else:
            z_arccos = -arccos(adj, hyp, opp, 2)

        synRot = synapse.rotate_z(z_arccos, center, inplace=False)
        vesRot = vesicle.rotate_z(z_arccos, center, inplace=False)

        # ===========================================================

        p1 = tuple(synRot.center)
        p2 = tuple(vesRot.center)

        center = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2, (p1[2]+p2[2])/2)
        radius = math.sqrt(pow((p1[0] - center[0]), 2) + pow((p1[2] - center[2]), 2))
        p3 = (center[0], center[2] - radius)

        opp, adj, hyp, p3, p4 = getTriangle((p1[0], p1[2]), (center[0], center[2]), p3)

        if(p1[0] < p3[0] and p1[2] < p3[1]):
            y_arccos = arccos(adj, hyp, opp, 2)
        elif(p1[0] > p3[0] and p1[2] > p3[1]):
            y_arccos = arccos(adj, hyp, opp, 2)
        else:
            y_arccos = -arccos(adj, hyp, opp, 2)

        synRot = synRot.rotate_y(y_arccos, center, inplace=False)
        vesRot = vesRot.rotate_y(y_arccos, center, inplace=False)

        # ===========================================================

        p.add_mesh(synRot, color="Blue", opacity = 0.5, lighting=False)
        p.add_mesh(vesRot, color="Red", opacity = 0.5, lighting=False)

        quickCamPos = p.camera.position

        p.camera.SetParallelProjection(True)
        p.camera_position = 'xy'

        synVesCamScale = p.camera.parallel_scale
        startRot = (0, y_arccos, z_arccos)

        v0 = vesRot.center
        synapse_origin = synRot.center

        destroyPlot(p)

        # ===========================================================

        x_min, x_max, x_step = -90, 135, 45
        x_range = range(x_min, x_max, x_step)
        y_min, y_max, y_step = -90, 135, 45
        y_range = range(y_min, y_max, y_step)
        
        camScales = []

        for i in x_range:
            for j in y_range:
                sy_reader = pv.get_reader(syn)
                synapse = sy_reader.read()
                p = pv.Plotter(off_screen=True)

                synapse.rotate_z(z_arccos, center, inplace=True)
                synapse.rotate_y(y_arccos, center, inplace=True)

                synapse.rotate_x(i, center, inplace=True)
                synapse.rotate_y(j, center, inplace=True)

                p.add_mesh(synapse, lighting=False)

                p.camera.SetParallelProjection(True)
                p.camera_position = 'xy'

                camScales.append(p.camera.parallel_scale)

                destroyPlot(p)

        start_time = time.time()
        surfAreaVals, surfAreaImgs = surfaceAreaAngle(syn, camScales, x_range, y_range, z_arccos, y_arccos, center)
        surfAreaVals = np.array(surfAreaVals)
        maxSurfRot = np.max(surfAreaVals)
        rot_x_idx = int(np.where(surfAreaVals == maxSurfRot)[0][0])
        rot_y_idx = int(np.where(surfAreaVals == maxSurfRot)[1][0])
        surface_area_x = x_range[rot_x_idx]
        surface_area_y = y_range[rot_y_idx]
        print("%s seconds..." % (round(time.time() - start_time, 2)))

        x_min, x_max, x_step = surface_area_x - 45, surface_area_x + 45, 15
        x_range = range(x_min, x_max, x_step)
        y_min, y_max, y_step = surface_area_y - 45, surface_area_y + 45, 15
        y_range = range(y_min, y_max, y_step)

        start_time = time.time()
        _surfAreaVals, _surfAreaImgs = surfaceAreaAngle(syn, camScales, x_range, y_range, z_arccos, y_arccos, center)
        _surfAreaVals = np.array(_surfAreaVals)
        _maxSurfRot = np.max(_surfAreaVals)
        _rot_x_idx = int(np.where(_surfAreaVals == _maxSurfRot)[0][0])
        _rot_y_idx = int(np.where(_surfAreaVals == _maxSurfRot)[1][0])
        _surface_area_x = x_range[_rot_x_idx]
        _surface_area_y = y_range[_rot_y_idx]
        print("%s seconds..." % (round(time.time() - start_time, 2)))

        # print(f"SurfX: {_surface_area_x}, SurfY: {_surface_area_y}")

        # rotArrImg = concat_tile(_surfAreaImgs)
        # plt.imshow(rotArrImg)
        # plt.show()

        # iter1Graph = brightnessGraph(surfAreaVals, surfAreaImgs)
        # iter2Graph = brightnessGraph(_surfAreaVals, _surfAreaImgs)

        # cv2.imwrite(f"output/BrightGraphs/ITER1_{synIdx}_{vesIdx}.png", iter1Graph)
        # cv2.imwrite(f"output/BrightGraphs/ITER2_{synIdx}_{vesIdx}.png", iter2Graph)

        ves_reader = pv.get_reader(ves)
        vesicle = ves_reader.read()

        sy_reader = pv.get_reader(syn)
        synapse = sy_reader.read()

        vesicle.rotate_z(z_arccos, center, inplace=True)
        vesicle.rotate_y(y_arccos, center, inplace=True)
        vesicle.rotate_x(_surface_area_x, synapse_origin, inplace=True)
        vesicle.rotate_y(_surface_area_y, synapse_origin, inplace=True)

        synapse.rotate_z(z_arccos, center, inplace=True)
        synapse.rotate_y(y_arccos, center, inplace=True)
        synapse.rotate_x(_surface_area_x, synapse_origin, inplace=True)
        synapse.rotate_y(_surface_area_y, synapse_origin, inplace=True)

        vesPlot = pv.Plotter(off_screen=True)
        synPlot = pv.Plotter(off_screen=True)

        '''
        visPlot = pv.Plotter(off_screen=False, window_size=[800,800])

        visPlot.set_background('white')


        visPlot.camera_position = 'xy'
        visPlot.camera.SetParallelProjection(True)
        visPlot.camera.focal_point = center
        visPlot.camera.parallel_scale = synVesCamScale
    
        visPlot.add_mesh(synapse, show_scalar_bar=False, lighting=False)
        visPlot.add_mesh(synapse, color="r", show_scalar_bar=False, lighting=True, opacity = 0.5)
        visPlot.add_mesh(vesicle, color="b", show_scalar_bar=False, lighting=True, opacity = 0.5)
        visPlot.add_mesh(synRot, color="r", show_scalar_bar=False, lighting=True, opacity=.2)
        visPlot.add_mesh(vesRot, color="g", show_scalar_bar=False, lighting=True, opacity=.2)
        
        v_p1 = [vesRot.center[0], vesRot.center[1], vesRot.center[2]]
        v_p2 = [vesicle.center[0], vesicle.center[1], vesicle.center[2]]
        s_p1 = [synapse.center[0], synapse.center[1], synapse.center[2]]

        vesLine = pv.Line(v_p1, v_p2)
        synLine = pv.Line(s_p1, v_p1)
        _synLine = pv.Line(s_p1, v_p2)

        s1 = pv.Sphere(0.00000005, v_p1)
        s2 = pv.Sphere(0.00000005, v_p2)

        visPlot.add_mesh(s1)
        visPlot.add_mesh(s2)

        visPlot.add_mesh(vesLine, color="r")
        visPlot.add_mesh(synLine, color="r")
        visPlot.add_mesh(_synLine, color="r")

        visPlot.show()
        '''

        # == Flattening ==

        synPlot.camera_position = 'xy'
        synPlot.camera.SetParallelProjection(True)
        synPlot.camera.focal_point = center
        synPlot.camera.parallel_scale = synVesCamScale
        synPlot.add_mesh(synapse, show_scalar_bar=False, lighting=False)
        synImg = synPlot.screenshot()


        vesPlot.camera_position = 'xy'
        vesPlot.camera.SetParallelProjection(True)
        vesPlot.camera.focal_point = center
        vesPlot.camera.parallel_scale = synVesCamScale
        vesPlot.add_mesh(vesicle, show_scalar_bar=False, lighting=False)
        vesImg = vesPlot.screenshot()

        destroyPlot(synPlot)
        destroyPlot(vesPlot)

        synapseOverlay = cv2.cvtColor(synImg, cv2.COLOR_BGR2GRAY)
        vesicleOverlay = cv2.cvtColor(vesImg, cv2.COLOR_BGR2GRAY)

        # == Intersection ==

        thresh=76
        syn_bw = cv2.threshold(synapseOverlay, thresh, 255, cv2.THRESH_BINARY)[1]
        ves_bw = cv2.threshold(vesicleOverlay, thresh, 255, cv2.THRESH_BINARY)[1]

        mergedOverlay = cv2.addWeighted(syn_bw, 0.5, ves_bw, 0.5, 0)
        intersectionImg = cv2.threshold(mergedOverlay, 128, 255, cv2.THRESH_BINARY)[1]

        # allious = cv2.hconcat([syn_bw, ves_bw, mergedOverlay, intersectionImg])
        '''
        fig, ax = plt.subplots(2,2)

        ax[0,0].imshow(synapseOverlay, cmap='Greys_r')
        ax[0,0].set_title("Synapse")
        ax[0,0].axis('off')

        ax[0,1].imshow(vesicleOverlay, cmap='Greys_r')
        ax[0,1].set_title("Vesicle")
        ax[0,1].axis('off')

        ax[1,0].imshow(mergedOverlay, cmap='Greys_r')
        ax[1,0].set_title("Union")
        ax[1,0].axis('off')

        ax[1,1].imshow(intersectionImg, cmap='Greys_r')
        ax[1,1].set_title("Intersection")
        ax[1,1].axis('off')

        plt.suptitle(f"Synapse {synIdx}, Vesicle {vesIdx}")
        plt.show()
        # # plt.savefig(f"output/Figs/IOU_{synIdx}_{vesIdx}.png")
        plt.close()
        '''

        # plt.imshow(mergedOverlay, cmap = 'Greys_r')
        # plt.show()

        syn_mask = np.count_nonzero( syn_bw )
        ves_mask = np.count_nonzero( ves_bw )
        intersection = np.count_nonzero( np.logical_and( syn_bw, ves_bw ) )
        union = syn_mask + ves_mask - intersection
        iou = intersection/(union)
        ios = intersection/(syn_mask)

        v1 = vesicle.center
        s0 = synapse.center
        
        vectorAngle = math.degrees(np.arccos(
            ((v0[0] - s0[0]) * (v1[0] - s0[0]) + (v0[1] - s0[1]) * (v1[1] - s0[1]) + (v0[2] - s0[2]) * (v1[2] - s0[2])) / 
            (((v0[0] - s0[0])**2 + (v0[1] - s0[1])**2 + (v0[2] - s0[2])**2)**0.5 * ((v1[0] - s0[0])**2 + (v1[1] - s0[1])**2 + (v1[2] - s0[2])**2)**0.5)
            ))

        camVesPos_x.append(v0[0])
        camVesPos_y.append(v0[1])
        camVesPos_z.append(v0[2])

        sfaVesPos_x.append(v1[0])
        sfaVesPos_y.append(v1[1])
        sfaVesPos_z.append(v1[2])

        synPos_x.append(s0[0])
        synPos_y.append(s0[1])
        synPos_z.append(s0[2])

        vesAngle.append(vectorAngle)
        intersectVals.append(intersection)
        iouVals.append(iou)
        iosVals.append(ios)

    all_syn = [row[0] for row in pairing]
    all_ves = [row[1] for row in pairing]

    print(all_syn)
    print(all_ves)



    d = {'synLabel': all_syn, 'vesLabel': all_ves, 'OG_Ves_X': camVesPos_x, 'OG_Ves_Y': camVesPos_y, 'OG_Ves_Z': camVesPos_z, 'Ves_X': sfaVesPos_x, 'Ves_Y': sfaVesPos_y, 'Ves_Z': sfaVesPos_z, 'Syn_X': synPos_x, 'Syn_Y': synPos_y, 'Syn_Z': synPos_z, 'VectorAngle': vesAngle, 'Intersect': intersectVals, 'IOU': iouVals, 'IOS': iosVals}
    df = pd.DataFrame(data=d)
    print(df)
    return(df)