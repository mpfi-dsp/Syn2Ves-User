"""


:author: 
:contact: 
:email: 
:organization: 
:address: 
:copyright: 
:date: May 01 2023 12:32
:dragonflyVersion: 2022.2.0.1367
:UUID: c2469264e83d11ed973f44032c94bd8e
"""

__version__ = '1.4.0'

# Action log Mon Feb 13 11:37:29 2023

# Macro name: Multi ROI To Mesh 04252023

# ********** BEGIN MACRO ********** #
"""
:name: Multi ROI To Mesh 04252023
:execution: execute
"""

# blockly xml: %3Cxml%3E%3Cvariables%3E%3Cvariable%20type%3D%22orsMultiROI%22%20id%3D%22%29.e%7ERAsd%3Bl.ym%7E-SuYge%22%3EmyMultiROI%3C/variable%3E%3Cvariable%20type%3D%22int%22%20id%3D%22y%21%3Ao3%7Cp%21B3HdamKF9lZG%22%3EaInt%3C/variable%3E%3C/variables%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22@f4%3Dt08%3DW+x@Ecs%29Kimr%22%20x%3D%2226%22%20y%3D%22175%22%3E%3Cmutation%20output_type_at_creation%3D%22orsMultiROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%29.e%7ERAsd%3Bl.ym%7E-SuYge%22%20variabletype%3D%22orsMultiROI%22%3EmyMultiROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsMultiROI%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22ors_lists_getIndex%22%20id%3D%22C4hB*GH%5DZECAr3%60%3FxLh/%22%3E%3Cmutation%20statement%3D%22false%22%20at%3D%22false%22%3E%3C/mutation%3E%3Cfield%20name%3D%22MODE%22%3EGET%3C/field%3E%3Cfield%20name%3D%22WHERE%22%3EFIRST%3C/field%3E%3Cvalue%20name%3D%22VALUE%22%3E%3Cblock%20type%3D%22working_context_selected%22%20id%3D%22D0%3DR%28E%7C%21TGw%5BJG6KVGn%7B%22%3E%3Cmutation%20type%3D%22list_of_orsMultiROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22type%22%3EMultiROI%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22select_all_mr_labels%22%20id%3D%22%28t45udukB7BSSZuP_JMN%22%3E%3Cvalue%20name%3D%22MR%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22JA+-%29KQ4%25%242%5D0h@DhCXW%22%3E%3Cmutation%20output_type_at_creation%3D%22orsMultiROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%29.e%7ERAsd%3Bl.ym%7E-SuYge%22%20variabletype%3D%22orsMultiROI%22%3EmyMultiROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsMultiROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22aovQj6umM2@-W%7BIF6UX%3A%22%3E%3Cmutation%20output_type_at_creation%3D%22int%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22y%21%3Ao3%7Cp%21B3HdamKF9lZG%22%20variabletype%3D%22int%22%3EaInt%3C/field%3E%3Cfield%20name%3D%22type%22%3Eint%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%22-%60Hgy%28tFbwG_j*V%24ee%25t%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsMultiROI%22%20method%3D%22getLabelCount%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22JT%28*i/bSuEeKgtE%3AthoT%22%3E%3Cmutation%20output_type_at_creation%3D%22orsMultiROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%29.e%7ERAsd%3Bl.ym%7E-SuYge%22%20variabletype%3D%22orsMultiROI%22%3EmyMultiROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsMultiROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%22De%5DnkZ%7Dx%23S%24%2C_*M_AP%7Cm%22%3E%3Cfield%20name%3D%22method%22%3EgetLabelCount%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22message_prompt%22%20id%3D%22%251%3F/l2UZn3%21oh.73%5D%3DPJ%22%3E%3Cvalue%20name%3D%22TITLE%22%3E%3Cblock%20type%3D%22text%22%20id%3D%22q*k.Qq5%21o9j%3D79u%28XvkF%22%3E%3Cfield%20name%3D%22TEXT%22%3E%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22CAPTION%22%3E%3Cblock%20type%3D%22text%22%20id%3D%22VPx%5DXzPG%3BM_%5Bk7%7B%5D%5BTe1%22%3E%3Cfield%20name%3D%22TEXT%22%3E%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22INPUT%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22%3Fg%3DDZv%25%7E%60dI4%7CdC9%28qIN%22%3E%3Cmutation%20output_type_at_creation%3D%22int%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22y%21%3Ao3%7Cp%21B3HdamKF9lZG%22%20variabletype%3D%22int%22%3EaInt%3C/field%3E%3Cfield%20name%3D%22type%22%3Eint%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3Cblock%20type%3D%22ors_interface_method%22%20id%3D%22%3D8f%3FO3cidtT%2C%21LJp@/aY%22%20inline%3D%22false%22%20disabled%3D%22true%22%20x%3D%2295%22%20y%3D%22452%22%3E%3Cmutation%20module%3D%22OrsHelpers.multiroilabelhelper%22%20method%3D%22MultiROILabelHelper.extractSelectedLabelsToROIs%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22module%22%3E%3Cblock%20type%3D%22ors_interface_module_selector%22%20id%3D%22%29Z%3DGN.Xm9ljh%60H5J@dPo%22%3E%3Cfield%20name%3D%22module%22%3EOrsHelpers.multiroilabelhelper%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22ors_interface_method_selector%22%20id%3D%22k%5E2GKeJYIr%5BP*7sWI%25PN%22%3E%3Cfield%20name%3D%22method%22%3EMultiROILabelHelper.extractSelectedLabelsToROIs%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22multiroi%22%3E%3Cshadow%20type%3D%22PyNone%22%20id%3D%22wQhnJ%7E%29*W27*b%7E4%5Dm%5EU2%22%3E%3C/shadow%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22%5BW%2CScMO%5Di%3DtI%7Bq%23%247Arl%22%3E%3Cmutation%20output_type_at_creation%3D%22orsMultiROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%29.e%7ERAsd%3Bl.ym%7E-SuYge%22%20variabletype%3D%22orsMultiROI%22%3EmyMultiROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsMultiROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22tIndex%22%3E%3Cblock%20type%3D%22value_chooser%22%20id%3D%22%29-%21%5B9_xp7Et/+vzj%5D228%22%3E%3Cfield%20name%3D%22TYPE%22%3EInteger%3A%3C/field%3E%3Cfield%20name%3D%22VALUE%22%3ESelect%20T%20Index%3C/field%3E%3Cfield%20name%3D%22DEFAULT%22%3E1%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/xml%3E
##### START OF BLOCKLY DEFINITIONS #####
from OrsLibraries.workingcontext import WorkingContext
import ORSModel
from ORSModel.ors import ROI, Managed, DimensionUnit
from ORSModel import OrsSelectedObjects
from ORSServiceClass.messagebox.orsMessageBox import OrsTMessageBox
from OrsPythonPlugins.OrsVolumeROITools.OrsVolumeROITools import OrsVolumeROITools
from ORSServiceClass.ORSWidget.SimpleEntryDialog.simpleEntryDialog import SimpleEntryDialog
from PyQt5.QtWidgets import QFileDialog
import numpy as np
import pandas as pd
import os
import datetime
import time

def show_msgbox(message, caption, title):
        message = str(caption) + str(message)
        OrsTMessageBox.message(None, message, str(title), OrsTMessageBox.Information, OrsTMessageBox.Ok)

def create_mesh(roi, type, factor):
    if type == "CUBIC":
        mesh, _ = OrsVolumeROITools.exportROIAsCubicMesh(roi, 0)
    elif type == "NORMAL":
        mesh, _ = OrsVolumeROITools.exportROIAsSampledMesh(roi, factor, factor, factor)
    else:
        if factor > 1:
            mesh, _ = OrsVolumeROITools.exportROIAsThicknessMeshSample(roi, factor, factor, factor, 0)
        else:
            mesh, _ = OrsVolumeROITools.exportROIAsThicknessMesh(roi)
    return mesh

def get_value(title: str, default: int):
    value = SimpleEntryDialog.prompt(None, "Integer", title, default)
    try:
        return int(value)
    except ValueError:
        return default

def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

##### END OF BLOCKLY DEFINITIONS #####

start_time = time.time()

aFolder = os.path.join(QFileDialog.getExistingDirectory(WorkingContext.getCurrentContextWindow(), caption="Select folder ", options=QFileDialog.ShowDirsOnly), '')
aFolder = os.path.join(aFolder, datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
os.makedirs(aFolder, exist_ok=True)

listOfMultiROIs = (WorkingContext.getEntitiesOfClassAsObjects(None, OrsSelectedObjects, MultiROI.getClassNameStatic()))

dm = DimensionUnit
reg_key = dm.getRegistrationKeyFromCxvDimensionUniverse(1)
dm = dm.getRegisteredUnit(reg_key)

# 1 = Mirometer SURFACE
# List of Dimension IDs: https://dev.theobjects.com/dragonfly_2022_2_release/COMWrapper/sphinxIndexCOMWrapper.html?highlight=cxvuniverse_dimension_type#cxvuniverse-dimension

for myMultiROI in listOfMultiROIs:

    comX = []
    comY = []
    comZ = [] 
    vol = []
    SA = []
    halfSA = []
    sphericity = []   

    myMultiTitle = myMultiROI.getTitle()

    saveFolder = os.path.join(aFolder, myMultiTitle)
    os.makedirs(saveFolder, exist_ok=True)

    labels = myMultiROI.getNonEmptyLabels(None)
    _max = len(labels)

    for i in range(1, (_max + 1)):

        batch = ORSModel.ors.ArrayUnsignedLong()

        batch.atPut(0, i)

        myMultiROI.setSelectedLabels(iTIndex = 0,
                                    labels = batch,
                                    selected = True)

        selectedLabels = myMultiROI.getSelectedLabels(0)

        guid = MultiROILabelHelper.extractSelectedLabelsToROIs(multiroi=myMultiROI, tIndex=0)[0]

        guidROI = Managed.getObjectWithGUID(guid)
        guidROI.publish(logging=True)

        guidMesh = create_mesh(guidROI, 'NORMAL', 1)
        guidMesh.publish()

        meshTitle = str(selectedLabels[0])

        exportOutInt = OrsMeshSaver.exportMeshToFile(mesh=guidMesh,
                                                        lut=None,
                                                        filename=(str(saveFolder) + str((str('\\') + str((str(meshTitle) + str('.stl')))))),
                                                        centerAtOrigin=False, outputUnit=None, exportAsASCII=False, exportColors=False, showProgress=True)

        comX.append((ROI.getCenterOfMass(guidROI, pTimeStep = 0))[0])
        comY.append((ROI.getCenterOfMass(guidROI, pTimeStep = 0))[1])
        comZ.append((ROI.getCenterOfMass(guidROI, pTimeStep = 0))[2])
        volume = ROI.getVolume(guidROI, timeStep = 0)
        vol.append(volume)
        surfaceArea = (ROI.getSurfaceFromWeightedVoxelEstimation(guidROI, timeStep = 0, progressBar = None)) ### Linblad 2005 Method
        SA.append(surfaceArea)
        halfSA.append(0.5*surfaceArea)
        sphericity.append( (np.pi)**(1/3) * (6 * (volume))**(2/3) / surfaceArea)

        guidMesh.deleteObject()
        guidROI.deleteObject()

    multiRoiAnalyzer = myMultiROI.generateAnalyzer(inputChannel = None, pROI = None, aTimeStep = 0, pStats = 1024, pCompute2DStats = False, IProgress = None)
    maxFeretLengths = multiRoiAnalyzer.getFeretLengthMax()
    minFeretLengths = multiRoiAnalyzer.getFeretLengthMin()

    multiRoiAnalyzer1 = myMultiROI.generateAnalyzer(inputChannel = None, pROI = None, aTimeStep = 0, pStats = 16, pCompute2DStats = False, IProgress = None)
    aspectRatio = multiRoiAnalyzer1.getLabelsAspectRatio()

    array = np.column_stack((labels, comX, comY, comZ, vol, SA, halfSA, sphericity, maxFeretLengths[1:], minFeretLengths[1:], aspectRatio[1:]))
    df = pd.DataFrame(array, columns = ['labels', 'comX', 'comY', 'comZ', 'vol', 'SA', 'halfSA', 'sphericity', 'maxFeretLength', 'minFeretLength', 'aspectRatio'])
    
    measuresDir = (str(saveFolder) + str('\\') + myMultiTitle + ' Measurements.csv').replace("\\","/")
    df.to_csv(measuresDir, encoding = 'utf-8-sig', index = False) 

    with open(f'{saveFolder}/meshExportRuntime.txt', 'w') as f:
        f.write(str(time.time() - start_time))

# ********** END MACRO ********** #