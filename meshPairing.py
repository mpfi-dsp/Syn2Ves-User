"""


:author:
:contact: 
:email: jordan.anderson.jra@gmail.com
:organization: EM Core Facility, Max Planck Florida Institute for Neuroscience
:address: 
:copyright: 
:date: Feb 13 2023 11:37
:dragonflyVersion: 2022.2.0.1367
:UUID: e85751dcabba11edab3b44032c94bd8b
"""

__version__ = '1.1.0'

# Action log Mon Feb 13 11:37:29 2023

# Macro name: Syn/Ves Mesh Pairing with Measures 04-24-2023 19:28

# ********** BEGIN MACRO ********** #
"""
:name: Syn/Ves Mesh Pairing with Measures 04-24-2023 19:28
:execution: execute
"""

# blockly xml: %3Cxml%3E%3Cvariables%3E%3Cvariable%20type%3D%22orsMultiROI%22%20id%3D%22%29.e%7ERAsd%3Bl.ym%7E-SuYge%22%3EmyMultiROI%3C/variable%3E%3Cvariable%20type%3D%22int%22%20id%3D%22y%21%3Ao3%7Cp%21B3HdamKF9lZG%22%3EaInt%3C/variable%3E%3C/variables%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22@f4%3Dt08%3DW+x@Ecs%29Kimr%22%20x%3D%2226%22%20y%3D%22175%22%3E%3Cmutation%20output_type_at_creation%3D%22orsMultiROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%29.e%7ERAsd%3Bl.ym%7E-SuYge%22%20variabletype%3D%22orsMultiROI%22%3EmyMultiROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsMultiROI%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22ors_lists_getIndex%22%20id%3D%22C4hB*GH%5DZECAr3%60%3FxLh/%22%3E%3Cmutation%20statement%3D%22false%22%20at%3D%22false%22%3E%3C/mutation%3E%3Cfield%20name%3D%22MODE%22%3EGET%3C/field%3E%3Cfield%20name%3D%22WHERE%22%3EFIRST%3C/field%3E%3Cvalue%20name%3D%22VALUE%22%3E%3Cblock%20type%3D%22working_context_selected%22%20id%3D%22D0%3DR%28E%7C%21TGw%5BJG6KVGn%7B%22%3E%3Cmutation%20type%3D%22list_of_orsMultiROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22type%22%3EMultiROI%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22select_all_mr_labels%22%20id%3D%22%28t45udukB7BSSZuP_JMN%22%3E%3Cvalue%20name%3D%22MR%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22JA+-%29KQ4%25%242%5D0h@DhCXW%22%3E%3Cmutation%20output_type_at_creation%3D%22orsMultiROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%29.e%7ERAsd%3Bl.ym%7E-SuYge%22%20variabletype%3D%22orsMultiROI%22%3EmyMultiROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsMultiROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22set_ors_variable%22%20id%3D%22aovQj6umM2@-W%7BIF6UX%3A%22%3E%3Cmutation%20output_type_at_creation%3D%22int%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22y%21%3Ao3%7Cp%21B3HdamKF9lZG%22%20variabletype%3D%22int%22%3EaInt%3C/field%3E%3Cfield%20name%3D%22type%22%3Eint%3C/field%3E%3Cvalue%20name%3D%22NAME%22%3E%3Cblock%20type%3D%22orsmodel_method%22%20id%3D%22-%60Hgy%28tFbwG_j*V%24ee%25t%22%20inline%3D%22false%22%3E%3Cmutation%20class%3D%22orsMultiROI%22%20method%3D%22getLabelCount%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22GUID%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22JT%28*i/bSuEeKgtE%3AthoT%22%3E%3Cmutation%20output_type_at_creation%3D%22orsMultiROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%29.e%7ERAsd%3Bl.ym%7E-SuYge%22%20variabletype%3D%22orsMultiROI%22%3EmyMultiROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsMultiROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22orsmodel_method_selector%22%20id%3D%22De%5DnkZ%7Dx%23S%24%2C_*M_AP%7Cm%22%3E%3Cfield%20name%3D%22method%22%3EgetLabelCount%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/value%3E%3Cnext%3E%3Cblock%20type%3D%22message_prompt%22%20id%3D%22%251%3F/l2UZn3%21oh.73%5D%3DPJ%22%3E%3Cvalue%20name%3D%22TITLE%22%3E%3Cblock%20type%3D%22text%22%20id%3D%22q*k.Qq5%21o9j%3D79u%28XvkF%22%3E%3Cfield%20name%3D%22TEXT%22%3E%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22CAPTION%22%3E%3Cblock%20type%3D%22text%22%20id%3D%22VPx%5DXzPG%3BM_%5Bk7%7B%5D%5BTe1%22%3E%3Cfield%20name%3D%22TEXT%22%3E%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22INPUT%22%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22%3Fg%3DDZv%25%7E%60dI4%7CdC9%28qIN%22%3E%3Cmutation%20output_type_at_creation%3D%22int%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22y%21%3Ao3%7Cp%21B3HdamKF9lZG%22%20variabletype%3D%22int%22%3EaInt%3C/field%3E%3Cfield%20name%3D%22type%22%3Eint%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3C/next%3E%3C/block%3E%3Cblock%20type%3D%22ors_interface_method%22%20id%3D%22%3D8f%3FO3cidtT%2C%21LJp@/aY%22%20inline%3D%22false%22%20disabled%3D%22true%22%20x%3D%2295%22%20y%3D%22452%22%3E%3Cmutation%20module%3D%22OrsHelpers.multiroilabelhelper%22%20method%3D%22MultiROILabelHelper.extractSelectedLabelsToROIs%22%3E%3C/mutation%3E%3Cvalue%20name%3D%22module%22%3E%3Cblock%20type%3D%22ors_interface_module_selector%22%20id%3D%22%29Z%3DGN.Xm9ljh%60H5J@dPo%22%3E%3Cfield%20name%3D%22module%22%3EOrsHelpers.multiroilabelhelper%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22method%22%3E%3Cblock%20type%3D%22ors_interface_method_selector%22%20id%3D%22k%5E2GKeJYIr%5BP*7sWI%25PN%22%3E%3Cfield%20name%3D%22method%22%3EMultiROILabelHelper.extractSelectedLabelsToROIs%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22multiroi%22%3E%3Cshadow%20type%3D%22PyNone%22%20id%3D%22wQhnJ%7E%29*W27*b%7E4%5Dm%5EU2%22%3E%3C/shadow%3E%3Cblock%20type%3D%22variables_get_orsVar%22%20id%3D%22%5BW%2CScMO%5Di%3DtI%7Bq%23%247Arl%22%3E%3Cmutation%20output_type_at_creation%3D%22orsMultiROI%22%3E%3C/mutation%3E%3Cfield%20name%3D%22VAR%22%20id%3D%22%29.e%7ERAsd%3Bl.ym%7E-SuYge%22%20variabletype%3D%22orsMultiROI%22%3EmyMultiROI%3C/field%3E%3Cfield%20name%3D%22type%22%3EorsMultiROI%3C/field%3E%3C/block%3E%3C/value%3E%3Cvalue%20name%3D%22tIndex%22%3E%3Cblock%20type%3D%22value_chooser%22%20id%3D%22%29-%21%5B9_xp7Et/+vzj%5D228%22%3E%3Cfield%20name%3D%22TYPE%22%3EInteger%3A%3C/field%3E%3Cfield%20name%3D%22VALUE%22%3ESelect%20T%20Index%3C/field%3E%3Cfield%20name%3D%22DEFAULT%22%3E1%3C/field%3E%3C/block%3E%3C/value%3E%3C/block%3E%3C/xml%3E

##### START OF BLOCKLY DEFINITIONS #####

### Import

# Science Stack
import numpy as np
import pandas as pd

# Mesh analysis
import pyvista as pv

# File handling
from PyQt5.QtWidgets import QFileDialog
import os
import time

### Definitions

def show_msgbox(message, caption, title):
        message = str(caption) + str(message)
        OrsTMessageBox.message(None, message, str(title), OrsTMessageBox.Information, OrsTMessageBox.Ok)

##### END OF BLOCKLY DEFINITIONS #####

start_time = time.time()

### User input

# Get directory for folders containing meshes

# synMeshDir = os.path.join(QFileDialog.getExistingDirectory(WorkingContext.getCurrentContextWindow(), caption="Select the Folder with Synapse Meshes", options=QFileDialog.ShowDirsOnly), '').replace("\\","/")
# vesMeshDir = os.path.join(QFileDialog.getExistingDirectory(WorkingContext.getCurrentContextWindow(), caption="Select the Folder with Vesicle Meshes", options=QFileDialog.ShowDirsOnly), '').replace("\\","/")

# Get the data for synapses and vesicle clouds

# synComFile = str(QFileDialog.getOpenFileName(WorkingContext.getCurrentContextWindow(), 'Open CSV with Synapse Data', 'c:\\')[0])
# vesComFile = str(QFileDialog.getOpenFileName(WorkingContext.getCurrentContextWindow(), 'Open CSV with Vesicle Data', 'c:\\')[0])

# Get directory for the folder that will contain macro outputs

# synVesPairsDir = os.path.join(QFileDialog.getExistingDirectory(WorkingContext.getCurrentContextWindow(), caption="Select Folder for List of Pairs", options=QFileDialog.ShowDirsOnly), '').replace("\\","/")

# Get the half-height of a cube centered around the CoM of a synapse. 
# Vesicles with CoMs inside this cube will be loaded as meshes to check for the distance between their surface and the synapse's surface

searchVolRad = float(SimpleEntryDialog.prompt(None, "Specify the search radius from a synapses' center of mass. The macro will only pair a vesicle cloud with a synapse if its center of mass falls within the cubic volume with this radius."))

def MakePairs(synCom: pd.DataFrame, vesCom: pd.DataFrame, searchVolRad: float, synMeshDir: str, vesMeshDir: str):   
    ### CoM Pairing

    candidatePairs = pd.DataFrame({'synLabel': [], 'synX': [], 'synY': [], 'synZ': [], 'vesLabel':[], 'vesX': [], 'vesY': [], 'vesZ': [], 'comDist': []})

    # Load the coordinates for each synapse

    for synLabel in synCom.index:    
        synX = float(synCom.loc[synLabel,'comX'])
        synY = float(synCom.loc[synLabel,'comY'])
        synZ = float(synCom.loc[synLabel,'comZ'])

        # Load the coordinates for each vesicle cloud  

        for vesLabel in vesCom.index:

            vesX = float(vesCom.loc[vesLabel, 'comX'])
            vesY = float(vesCom.loc[vesLabel, 'comY'])
            vesZ = float(vesCom.loc[vesLabel, 'comZ'])

            # If the vesicle cloud has a CoM within the search radius of the synapse, calculate the distance between them and add a row the dataframe of candidate pairs

            if ((vesX >= (synX - searchVolRad)) and (vesX <= (synX + searchVolRad))) and ((vesY >= (synY - searchVolRad)) and (vesY <= (synY + searchVolRad))) and ((vesZ >= (synZ - searchVolRad)) and (vesZ <= (synZ + searchVolRad))):
                
                comDist = np.sqrt((synX - vesX)**2 + (synY - vesY)**2 + (synZ - vesZ)**2)
                
                newRow = {'synLabel': synLabel, 'synX': synX, 'synY': synY, 'synZ': synZ, 'vesLabel': vesLabel, 'vesX': vesX, 'vesY': vesY, 'vesZ': vesZ, 'comDist': comDist}
                
                candidatePairs = candidatePairs.append(newRow, ignore_index = True)

    # Convert labels to integers

    candidatePairs = candidatePairs.astype({'synLabel':'int'})
    candidatePairs = candidatePairs.astype({'vesLabel':'int'})

    # Save the list of candidate pairs as a csv

    # candidatePairsDir = synVesPairsDir + 'synVesCandidatePairsFromCom.csv'
    # candidatePairs.to_csv(candidatePairsDir, encoding = 'utf-8-sig', index = False)

    ### Calculate minimum distance for each candidate mesh pair

    # Prepare a dataframe containing information about each candidate pair and the shortest distance between their meshes

    meshNND_candidates = pd.DataFrame({'synLabel': [], 'synX': [], 'synY': [], 'synZ': [], 'synHalfSA': [], 'synVol': [], 'synSphere': [], 'synMaxFeret': [], 'synMinFeret': [], 'synAspectRatio': [],
                'vesLabel': [], 'vesX': [], 'vesY': [], 'vesZ': [], 'vesSA': [], 'vesVol': [], 'vesSphere': [], 'vesMaxFeret': [], 'vesMinFeret': [], 'vesAspectRatio': [], 'comDist': [],
                'synVertX': [], 'synVertY': [], 'synVertZ': [],
                'vesVertX': [], 'vesVertY': [], 'vesVertZ': [],'meshNND': []})

    # Go through each row of the candidate pairs dataframe

    for i in candidatePairs.index: 

        # Load labels for the synapse and the vesicle cloud in the candidate pair

        synLabel = int(candidatePairs.synLabel[i])
        vesLabel = int(candidatePairs.vesLabel[i])
        
        # Load the distance between CoMs for the pair

        comDist = candidatePairs.comDist[i]

        # Write directories for each mesh

        synMeshFile = synMeshDir + str(synLabel)+ '.stl'
        vesMeshFile = vesMeshDir + str(vesLabel)+ '.stl'
        
        # with open(f'{synVesPairsDir}/pairingUpdates.txt', 'w') as f:
            # f.write('syn' + str(synLabel) + ' ves' + str(vesLabel))
        
        # Use PyVista to read the meshes

        reader = pv.get_reader(synMeshFile) 
        synMesh = reader.read()

        reader1 = pv.get_reader(vesMeshFile)
        vesMesh = reader1.read()

        # For each point on the synapse mesh, find the nearest point on the vesicle cloud mesh
        # Calculate the distance between these points and record the minimum distance between any two points

        closest_cells, closest_points = vesMesh.find_closest_cell(synMesh.points, return_closest_point=True)
        d_exact = np.linalg.norm(synMesh.points - closest_points, axis=1)
        meshNND = np.min(d_exact)

        # Make an array of coordinates for each point on the synapse mesh
        # In the same row, add the coordinates for the closest point on the vesicle mesh and the distance between points
        # Convert the array to a dataframe

        synPointsPaired = np.hstack((synMesh.points, closest_points))
        synPointsPaired = np.hstack((synPointsPaired, np.atleast_2d(d_exact).T))
        synPointsPaired = pd.DataFrame(synPointsPaired)
        synPointsPaired.columns = ['svx', 'svy', 'svz', 'vvx', 'vvy', 'vvz', 'dist']

        # Find the points that have the shortest distance bewteen them and make a dataframe of their coordinates

        synPointsPairedMin = pd.DataFrame(synPointsPaired.loc[synPointsPaired.dist == meshNND])

        # Synapse meshes may have multiple points where they are the minimum distance from the vesicle mesh
        # We need these coordinates to visualize the nearest neighbor distance, but only one is necessary
        # Arbitrarily select the first pair of vertices listed with minimum distance between them

        synVertX = synPointsPairedMin.iloc[0, 0] 
        synVertY = synPointsPairedMin.iloc[0, 1]
        synVertZ = synPointsPairedMin.iloc[0, 2]
        
        vesVertX = synPointsPairedMin.iloc[0, 3] 
        vesVertY = synPointsPairedMin.iloc[0, 4]
        vesVertZ = synPointsPairedMin.iloc[0, 5]

        # Lookup voxel measurements for each syn/ves

        synHalfSA = synCom.loc[synLabel, 'halfSA']
        synVol = synCom.loc[synLabel, 'vol']
        synSphere = synCom.loc[synLabel, 'sphericity']
        synMaxFeret = synCom.loc[synLabel, 'maxFeretLength']
        synMinFeret = synCom.loc[synLabel, 'minFeretLength']
        synAspectRatio = synCom.loc[synLabel, 'aspectRatio']
        
        vesSA = vesCom.loc[vesLabel, 'SA']
        vesVol = vesCom.loc[vesLabel, 'vol']
        vesSphere = vesCom.loc[vesLabel, 'sphericity']
        vesMaxFeret = vesCom.loc[vesLabel, 'maxFeretLength']
        vesMinFeret = vesCom.loc[vesLabel, 'minFeretLength']
        vesAspectRatio = vesCom.loc[vesLabel, 'aspectRatio']

        # Add a new row to the dataframe containing candidate pairs and the distances between their meshes

        newRow = {'synLabel': synLabel, 'synX': candidatePairs.synX[i], 'synY': candidatePairs.synY[i], 'synZ': candidatePairs.synZ[i], 'synHalfSA': synHalfSA, 'synVol': synVol, 'synSphere': synSphere, 'synMaxFeret': synMaxFeret, 'synMinFeret': synMinFeret, 'synAspectRatio': synAspectRatio,
                    'vesLabel': vesLabel, 'vesX': candidatePairs.vesX[i], 'vesY': candidatePairs.vesY[i], 'vesZ': candidatePairs.vesZ[i], 'vesSA': vesSA, 'vesVol': vesVol, 'vesSphere': vesSphere, 'vesMaxFeret': vesMaxFeret, 'vesMinFeret': vesMinFeret, 'vesAspectRatio': vesAspectRatio, 'comDist': comDist,
                    'synVertX': synVertX, 'synVertY': synVertY, 'synVertZ': synVertZ,
                    'vesVertX': vesVertX, 'vesVertY': vesVertY, 'vesVertZ': vesVertZ,'meshNND': meshNND}
        
        meshNND_candidates = meshNND_candidates.append(newRow, ignore_index = True)

    # Make a list of synapse labels

    uniqueSynLabels = meshNND_candidates.synLabel.unique()
    uniqueSynLabels = uniqueSynLabels.tolist()

    # Prepare a dataframe of synapse-vesicle cloud pairs with the shortest distance between meshes

    synVesPairs = pd.DataFrame({'synLabel': [], 'synX': [], 'synY': [], 'synZ': [], 'synHalfSA': [], 'synVol': [], 'synSphere': [], 'synMaxFeret': [], 'synMinFeret': [], 'synAspectRatio': [],
                'vesLabel': [], 'vesX': [], 'vesY': [], 'vesZ': [], 'vesSA': [], 'vesVol': [], 'vesSphere': [], 'vesMaxFeret': [], 'vesMinFeret': [], 'vesAspectRatio': [], 'comDist': [],
                'synVertX': [], 'synVertY': [], 'synVertZ': [],
                'vesVertX': [], 'vesVertY': [], 'vesVertZ': [],'meshNND': []})

    for label in uniqueSynLabels: 
    
        tempDF = meshNND_candidates[meshNND_candidates['synLabel'] == label]
        synVesPairs = synVesPairs.append(tempDF[tempDF.meshNND == tempDF.meshNND.min()])

    # Convert labels to integers

    synVesPairs = synVesPairs.astype({'synLabel':'int'})
    synVesPairs = synVesPairs.astype({'vesLabel':'int'})

    # Save dataframe as csv file

    # synVesPairsDir1 = synVesPairsDir + 'synVesPairsFromMesh.csv'
    # synVesPairs.to_csv(synVesPairsDir1, encoding = 'utf-8-sig', index = False) 

    # Make a dataframe of unpaired vesicle pools and their measurements

    unpairedVes = pd.DataFrame({'label': [], 'comX': [], 'comY': [], 'comZ': [], 'SA': [], 'vol': [], 'sphericity': [], 'maxFeret': [], 'minFeret': [], 'aspectRatio': []})

    for label in vesCom['labels']: 

        if label in synVesPairs.vesLabel:
        
            continue
    
        else: 

            comX = vesCom.loc[label, 'comX']
            comY = vesCom.loc[label, 'SA']
            comZ = vesCom.loc[label, 'SA']
            SA = vesCom.loc[label, 'SA']
            vol = vesCom.loc[label, 'vol']
            sphere = vesCom.loc[label, 'sphericity']
            maxFeret = vesCom.loc[vesLabel, 'maxFeret']
            minFeret = vesCom.loc[vesLabel, 'minFeret']
            aspectRatio = vesCom.loc[vesLabel, 'aspectRatio']

            newRow = {'label': label, 'comX': comX, 'comY': comY, 'comZ': comZ, 'SA': SA, 'vol': vol, 'sphericity': sphere, 'maxFeret': maxFeret, 'minFeret': minFeret, 'aspectRatio': aspectRatio}

            unpairedVes = unpairedVes.append(newRow, ignore_index = True)
        
    # unpairedVesDir = synVesPairsDir + 'unpairedVes.csv'
    # unpairedVes.to_csv(unpairedVesDir, encoding = 'utf-8-sig', index = False) 

    # Save runtime

    # with open(f'{synVesPairsDir}/pairingRuntime.txt', 'w') as f:
        # f.write(str(time.time() - start_time))

    # ********** END MACRO ********** #