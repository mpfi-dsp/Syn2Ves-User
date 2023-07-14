"""


:author: 
:contact: 
:email: 
:organization: 
:address: 
:copyright: 
:date: May 03 2023 14:47
:dragonflyVersion: 2022.2.0.1367
:UUID: f855ce02e9e211ed859744032c94bd8b1
"""

__version__ = '1.0.0'

from ORSServiceClass.menuItems.userDefinedMenuItem import UserDefinedMenuItem
from ORSServiceClass.actionAndMenu.menu import Menu
from ORSServiceClass.decorators.infrastructure import interfaceMethod

import configparser
import pathlib
import os
import subprocess

import numpy as np
import cv2
import math
import time
import re
from typing import List
from PyQt5.QtWidgets import QFileDialog
import pyvista as pv
from PIL import Image, ImageEnhance, ImageOps
from ORSServiceClass.ORSWidget.SimpleEntryDialog.simpleEntryDialog import SimpleEntryDialog
from OrsLibraries.workingcontext import WorkingContext

class LaunchSyn2Ves_f855ce02e9e211ed859744032c94bd8b1(UserDefinedMenuItem):

    @classmethod
    def getTopLevelName(cls):
        """
        Defines the top level menu name where the menu item will appear.
        """
        return 'Synapse Vesicle Tools'

    @classmethod
    def getMenuItem(cls):
        """
        :return: Menu item
        """
        aMenuItem = Menu(title='Launch Syn2Ves Visualizer',
                         id_='LaunchSyn2Ves_f855ce02e9e211ed859744032c94bd8b1',
                         section='',
                         action='LaunchSyn2Ves_f855ce02e9e211ed859744032c94bd8b1.menuItemEntryPoint()')
        return aMenuItem

    @classmethod
    def menuItemEntryPoint(cls):
        """
        Will be executed when the menu item is selected.
        """
        
        def destroyPlot(plotter: pv.Plotter):
            """ SAFELY DESTROY PYVISTA PLOTTER """
            plotter.close()
            plotter._theme = None
            del plotter

        def num_sort(sortList: List[int]):
            """ SORTS A LIST OF INTEGERS """
            sortList.sort(key=lambda test_string : list(map(int, re.findall(r'\d+', test_string)))[0])
            return(sortList)

        def brightnessGraph(values_arr, images_arr, start = 0.25, end = 1):
            brightArr = np.empty_like(images_arr)

            width = end - start
            norm_values = (values_arr-np.min(values_arr))/(np.max(values_arr)-np.min(values_arr)) * width + start

            for i in range(len(images_arr)):
                for j in range(len(images_arr[i])):
                    img = images_arr[i][j]
                    bright_img = Image.fromarray(img.astype('uint8'), 'RGB')
                    enhancer = ImageEnhance.Brightness(bright_img)
                    bright_img = enhancer.enhance(norm_values[i][j])

                    if(norm_values[i][j] == np.amax(norm_values)):
                        bright_img = bright_img.convert('L')
                        bright_img = ImageOps.colorize(bright_img, black="black", white="green")

                    brightArr[i][j] = np.array(bright_img)

            brightTile = concat_tile(brightArr)

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
            """ RETURNS ROTATIONAL SURFACE AREA DATA FOR A MESH """

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

        # def Syn2Ves(syn_path: str, ves_path: str, pairing: List[Tuple[int, int]], pb: pyqtSignal, outFilePath: str = ""):
            
        syn_path = os.path.join(QFileDialog.getExistingDirectory(WorkingContext.getCurrentContextWindow(), caption="Select the Folder with Synapse Meshes", options=QFileDialog.ShowDirsOnly), '').replace("\\","/")
        ves_path = os.path.join(QFileDialog.getExistingDirectory(WorkingContext.getCurrentContextWindow(), caption="Select the Folder with Vesicle Meshes", options=QFileDialog.ShowDirsOnly), '').replace("\\","/")
        synID = int(SimpleEntryDialog.prompt(None, "Enter synapse ID"))
        vesID = int(SimpleEntryDialog.prompt(None, "Enter vesicle cloud ID"))
            
        """ MAIN ALIGNMENT CODE"""

        # Sort all our meshes numerically
        synFiles = num_sort(os.listdir(syn_path))
        vesFiles = num_sort(os.listdir(ves_path))

        # Get our current pairing
        syn = os.path.join(syn_path, synFiles[synID - 1])
        ves = os.path.join(ves_path, vesFiles[vesID - 1])

        # print(f"SYN: {pairing[i][0]}, VES: {pairing[i][1]}")
        # logging.info(f"SYN: {pairing[i][0]}, VES: {pairing[i][1]}")

        print(f"{syn}, {ves}")

        sy_reader = pv.get_reader(syn)
        ves_reader = pv.get_reader(ves)

        synapse = sy_reader.read()
        vesicle = ves_reader.read()

        p = pv.Plotter(off_screen=True)

        p1 = tuple(synapse.center)
        p2 = tuple(vesicle.center)

        """
        ALIGNMENT OF SYNAPSE AND VESICLE WITH X AXIS:

            - Creating a midpoint between synapse and vesicle
            - Rotate both around that midpoint to align with X axis
            - We do this twice, for the X and Y axis, so they line up directly on both dimensions

        """

        # Alignment on X axis:
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

        # Alignment on Y axis:
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

        """

        STORING IMPORTANT VALUES:

            - Here we are saving some important values to use later
            - synVesCamScale: represents the parallel scale when both meshes are displayer in the plotter (we need this for projection)
            - v0: represents the original position of our vesicle
            - synapse_origin: represents our synapses position

        """

        p.add_mesh(synRot, color="Blue", opacity = 0.5, lighting=False)
        p.add_mesh(vesRot, color="Red", opacity = 0.5, lighting=False)

        p.camera.SetParallelProjection(True)
        p.camera_position = 'xy'

        synVesCamScale = p.camera.parallel_scale

        v0 = vesRot.center
        synapse_origin = synRot.center

        destroyPlot(p)

        """

        FINDING THE MAX CAMERA SCALE:

            - When rotating our synapse, the camera scale will change automatically as the shown area of the synapse changes
            - This is bad, because we need a consistent camera size if we want to compare all of our images
            - In this code, we quickly iterate through all rotations, and pick the maximum camera scale used
            - We can then assign this value as our camera scale when collecting our images to have a consistent value

        """

        # Setting the range of values we plan to rotate to
        x_min, x_max, x_step = -90, 135, 45
        x_range = range(x_min, x_max, x_step)
        y_min, y_max, y_step = -90, 135, 45
        y_range = range(y_min, y_max, y_step)

        camScales = []

        # Rotate to each value, store camera scale
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

        """

        SURFACE AREA ITERATIVE ROTATION:

            - Here, we begin to rotate around our synapse, storing images at each specified step.
            - We do this twice, once with large steps to get a rough estimate, and a second time with smaller steps to fine tine our value

        """

        # Interation 1 of SA Rotation:
        start_time = time.time()
        surfAreaVals, surfAreaImgs = surfaceAreaAngle(syn, camScales, x_range, y_range, z_arccos, y_arccos, center)
        surfAreaVals = np.array(surfAreaVals)
        maxSurfRot = np.max(surfAreaVals)
        rot_x_idx = int(np.where(surfAreaVals == maxSurfRot)[0][0])
        rot_y_idx = int(np.where(surfAreaVals == maxSurfRot)[1][0])
        surface_area_x = x_range[rot_x_idx]
        surface_area_y = y_range[rot_y_idx]
        print("%s seconds..." % (round(time.time() - start_time, 2)))

        # Specifying new rotation steps
        x_min, x_max, x_step = surface_area_x - 45, surface_area_x + 45, 15
        x_range = range(x_min, x_max, x_step)
        y_min, y_max, y_step = surface_area_y - 45, surface_area_y + 45, 15
        y_range = range(y_min, y_max, y_step)

        # Iteration 2 of SA Rotation:
        start_time = time.time()
        _surfAreaVals, _surfAreaImgs = surfaceAreaAngle(syn, camScales, x_range, y_range, z_arccos, y_arccos, center)
        _surfAreaVals = np.array(_surfAreaVals)
        _maxSurfRot = np.max(_surfAreaVals)
        _rot_x_idx = int(np.where(_surfAreaVals == _maxSurfRot)[0][0])
        _rot_y_idx = int(np.where(_surfAreaVals == _maxSurfRot)[1][0])
        _surface_area_x = x_range[_rot_x_idx]
        _surface_area_y = y_range[_rot_y_idx]
        print("%s seconds..." % (round(time.time() - start_time, 2)))

        """

        FLATTENING AND PROJECTION:

            - Here we import our Synapse and Vesicle into individual plotters
            - We rotate them with the maximum surface area value we just obtained
            - Then we take individual images of both
            - These can be used to calculate IOU and IOS

        """

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

        # Setting plotter values to be identical for both plots, then storing a screenshot
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

        # Destroying Plots
        destroyPlot(synPlot)
        destroyPlot(vesPlot)

        # Converting screenshots to graysclae
        synapseOverlay = cv2.cvtColor(synImg, cv2.COLOR_BGR2GRAY)
        vesicleOverlay = cv2.cvtColor(vesImg, cv2.COLOR_BGR2GRAY)

        """

        IOU and IOS:

            - Here, using the images we just processed, we calculate the intersection over union and intersection over synapse area
            - We binarize the images, and overlay them on top of each other
            - Then we can count how many pixels are touching (the intersection) and compare that either to the total of pixels (union) or just the pixels of our synapse (IOS)

        """

        thresh=76
        syn_bw = cv2.threshold(synapseOverlay, thresh, 255, cv2.THRESH_BINARY)[1]
        ves_bw = cv2.threshold(vesicleOverlay, thresh, 255, cv2.THRESH_BINARY)[1]

        mergedOverlay = cv2.addWeighted(syn_bw, 0.5, ves_bw, 0.5, 0)
        intersectionImg = cv2.threshold(mergedOverlay, 128, 255, cv2.THRESH_BINARY)[1]

        syn_mask = np.count_nonzero( syn_bw )
        ves_mask = np.count_nonzero( ves_bw )
        intersection = np.count_nonzero( np.logical_and( syn_bw, ves_bw ) )
        union = syn_mask + ves_mask - intersection

        """

            iou: Intersection over Union
            ios: Intersection over Synapse Area
            v1: Rotated Vesicle Position
            s0: Synapse Position

        """

        ios = intersection/(syn_mask)
        v1 = vesicle.center
        s0 = synapse.center

        # Calculating vector angle from Vesicle positions
        vectorAngle = math.degrees(np.arccos(
            ((v0[0] - s0[0]) * (v1[0] - s0[0]) + (v0[1] - s0[1]) * (v1[1] - s0[1]) + (v0[2] - s0[2]) * (v1[2] - s0[2])) / 
            (((v0[0] - s0[0])**2 + (v0[1] - s0[1])**2 + (v0[2] - s0[2])**2)**0.5 * ((v1[0] - s0[0])**2 + (v1[1] - s0[1])**2 + (v1[2] - s0[2])**2)**0.5)
            ))

        vectorAngle = round(vectorAngle, 3)
        ios = round(ios, 3)
        
        plot = pv.Plotter(off_screen=False)
        
        plot.camera_position = 'xy'
        plot.camera.SetParallelProjection(True)
        plot.camera.focal_point = center
        plot.camera.parallel_scale = synVesCamScale
        plot.add_mesh(synapse, color = "blue", opacity = 0.32, show_scalar_bar=False, lighting=False)
        plot.add_mesh(vesicle, color = "red", opacity = 0.32, show_scalar_bar=False, lighting=False)
        
        
        vesLine = pv.Line((s0[0], s0[1], s0[2]),(v1[0], v1[1], v1[2]))
        plot.add_mesh(vesLine, line_width = 3, color = 'yellow')
        
        normLine = pv.Line((s0[0], s0[1], s0[2]),(v0[0], v0[1], v0[2]))
        plot.add_mesh(normLine, line_width = 3, color = 'yellow')
        
        synComPoint = pv.Sphere(radius = (.00000002), center = (s0[0], s0[1], s0[2]))
        plot.add_mesh(synComPoint, color = 'yellow')
        
        vesComPoint = pv.Sphere(radius = (.00000002), center = (v1[0], v1[1], v1[2]))
        plot.add_mesh(vesComPoint, color = 'yellow')
        
        plot.set_background("gray", top = "white")
        
        plot.add_text("Vesicle Cloud", position = "upper_left", color = "red", font_size = 12)
        plot.add_text("Synapse        ", position = "left_edge", color = "blue", font_size = 12)
        plot.add_text(text = "Vector Angle: " + str(vectorAngle) + " Degrees \nIntersection Over Synapse Area: " + str(ios), position = "lower_left", color = "yellow", font_size = 12)
        
        plot.show(title = 'Syn2Ves Visualizer', before_close_callback = plot.clear) ### This only works if def close in def show is edited such that self.before_close_callback(self) is changed to self_before_close_callback()
        
        exit() ### Otherwise, Dragonfly will not close completely 



