"""


:author: 
:contact: 
:email: 
:organization: 
:address: 
:copyright: 
:date: Mar 22 2023 12:27
:dragonflyVersion: 2022.2.0.1367
:UUID: 7c090460c8ce11edaf9c44032c94bd8e
"""

__version__ = '1.0.0'

import pandas as pd
import openpyxl

from PyQt5.QtWidgets import QFileDialog

import ORSModel
from ORSModel import MultiROI
from ORSModel import Managed
from ORSModel import ROI
from ORSModel import VisualRuler
from ORSModel import Vector3

# Import stack below this may be outdated, check l8r
from ORSServiceClass.actionAndMenu.menu import Menu
from ORSServiceClass.decorators.infrastructure import interfaceMethod
from ORSServiceClass.menuItems.contextualMenuItem import ContextualMenuItem
from ORSServiceClass.ORSWidget.chooseObjectAndNewName.chooseObjectAndNewName import ChooseObjectAndNewName
from ORSServiceClass.ORSWidget.SimpleEntryDialog.simpleEntryDialog import SimpleEntryDialog

from ORSServiceClass.menuItems.userDefinedMenuItem import UserDefinedMenuItem
from ORSServiceClass.actionAndMenu.menu import Menu
from ORSServiceClass.decorators.infrastructure import interfaceMethod

from OrsHelpers.ListHelper import ListHelper
from OrsHelpers.multiroilabelhelper import MultiROILabelHelper
from OrsHelpers.primitivehelper import PrimitiveHelper

from OrsLibraries.workingcontext import WorkingContext


class VisualizePairingWithRulersTop_7c090460c8ce11edaf9c44032c94bd8e(UserDefinedMenuItem):

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
        aMenuItem = Menu(title='Visualize Pairing with Rulers',
                         id_='VisualizePairingWithRulersTop_7c090460c8ce11edaf9c44032c94bd8e',
                         section='',
                         action='VisualizePairingWithRulersTop_7c090460c8ce11edaf9c44032c94bd8e.menuItemEntryPoint()')
        return aMenuItem

    @classmethod
    def menuItemEntryPoint(cls):
        """
        Will be executed when the menu item is selected.
        """
        # Put your code here
        synMROI = cls._selectMultiROI("Select the Synapse MultiROI")
        vesMROI = cls._selectMultiROI("Select the Vesicle MultiROI")

        if synMROI == None or vesMROI == None:
            return

        selectedFilename, filter = QFileDialog.getOpenFileName(caption="Please select a CSV with your COM information")

        if selectedFilename == '':
            return

        df = pd.read_excel(selectedFilename, engine='openpyxl')
        df1 = df[['synLabel', 'vesLabel']]
        print(df1.head())

        synIndex = cls._getIndexValue()
        vesIndex = int(df1.iloc[synIndex-1]['vesLabel'])

        synROI = cls._exportLabelToROI(synMROI, synIndex)
        vesROI = cls._exportLabelToROI(vesMROI, vesIndex)

        aLayoutName = 'toplayout\\scene_0\\0\\3D'
        associatedState = 'OrsStateRulerEdit'
        t1 = 0
        t2 = 0
        p1 = synROI.getCenterOfMass(pTimeStep=0)
        p2 = vesROI.getCenterOfMass(pTimeStep=0)
        cls._createPrimitive(aLayoutName, associatedState, t1, p1, t2, p2)

    @classmethod
    @interfaceMethod
    def _selectMultiROI(cls, dialog):
        """
        Select a MultiROI from all MultiROIs in the project

        :param dialog: Dialog to be shown with selection window
        :type dialog: str
        """
        class_name = "MultiROI"
        class_object = getattr(ORSModel, class_name)
        return ChooseObjectAndNewName.prompt([class_object], parent=WorkingContext.getCurrentContextWindow(), dialog_title=dialog, allowNone=False, getNewTitle=False)

    @classmethod
    @interfaceMethod
    def _getIndexValue(cls):
        value = SimpleEntryDialog.prompt(None, "Integer", "Select Index", 1)
        try:
            return int(value)
        except ValueError:
            return 1

    @classmethod
    @interfaceMethod
    def _exportLabelToROI(cls, multiROI, index):
        """
        Exports a selected label from a MultiROI as an ROI

        :param multiROI: multiROI to use
        :type multiROI: ORSModel.ors.MultiROI
        :param index: label index to export
        :type index: int
        """

        _idx = ORSModel.ors.ArrayUnsignedLong()
        _idx.insertAt(index=0, pValue=index)

        multiROI.setSelectedLabels(iTIndex=0, labels=_idx, selected=True)
        guid = MultiROILabelHelper.extractSelectedLabelsToROIs(multiroi=multiROI, tIndex=0)[0]
        guidROI = Managed.getObjectWithGUID(guid)
        guidROI.publish(logging=True)
        return(guidROI)

    @classmethod
    @interfaceMethod
    def _createPrimitive(cls, aLayoutName, associatedState, t1, p1, t2, p2):
        """
        Creates and publishes a Ruler

        :param aLayoutName: Name of Layout
        :type aLayoutName: str
        :param associatedState: State to be used
        :type associatedState: str
        :param t1: TimeStep for point 1
        :type t1: int
        :param p1: Position for point 1
        :type p1: ORSModel.ors.Vector3
        :param t2: TimeStep for point 2
        :type t2: int
        :param p2: Position for point 1
        :type p2: ORSModel.ors.Vector3
        """

        # Creating a blank ruler primitive
        newAnnotation = PrimitiveHelper.createPrimitive(primitiveClass=ORSModel.ors.VisualRuler, aLayoutName=aLayoutName,
                                                        associatedState=associatedState)

        # Create and move the ruler points
        success = PrimitiveHelper.addControlPoint(anAnnotation=newAnnotation,
                                                  timeStep=t1,
                                                  position=p1)

        success1 = PrimitiveHelper.addControlPoint(anAnnotation=newAnnotation,
                                                  timeStep=t2,
                                                  position=p2)

        # Publishing the ruler
        newAnnotation.setIsRepresentable(isRepresentable=True, logging=True)
        newAnnotation.publish(logging=True)
        newAnnotation.setDataDirty(logging=True)
