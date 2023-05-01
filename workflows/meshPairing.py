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


start_time = time.time()

### User input

def MakePairs(synCom: pd.DataFrame, vesCom: pd.DataFrame, searchVolRad: float, synMeshDir: str, vesMeshDir: str):
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

    vesComList = vesCom.index.tolist()
    vesLabelList = synVesPairs.vesLabel.tolist()

    for label in vesComList: 

        if label not in vesLabelList: 

            comX = vesCom.loc[label, 'comX']
            comY = vesCom.loc[label, 'comY']
            comZ = vesCom.loc[label, 'comZ']
            SA = vesCom.loc[label, 'SA']
            vol = vesCom.loc[label, 'vol']
            sphere = vesCom.loc[label, 'sphericity']
            maxFeret = vesCom.loc[label, 'maxFeretLength']
            minFeret = vesCom.loc[label, 'minFeretLength']
            aspectRatio = vesCom.loc[label, 'aspectRatio']

            newRow = {'label': label, 'comX': comX, 'comY': comY, 'comZ': comZ, 'SA': SA, 'vol': vol, 'sphericity': sphere, 'maxFeret': maxFeret, 'minFeret': minFeret, 'aspectRatio': aspectRatio}

            unpairedVes = unpairedVes.append(newRow, ignore_index = True)
        
    # unpairedVesDir = synVesPairsDir + 'unpairedVes.csv'
    # unpairedVes.to_csv(unpairedVesDir, encoding = 'utf-8-sig', index = False) 
    # Save runtime

    # with open(f'{synVesPairsDir}/pairingRuntime.txt', 'w') as f:
        # f.write(str(time.time() - start_time))

    return(candidatePairs, synVesPairs, unpairedVes)

    # ********** END MACRO ********** #