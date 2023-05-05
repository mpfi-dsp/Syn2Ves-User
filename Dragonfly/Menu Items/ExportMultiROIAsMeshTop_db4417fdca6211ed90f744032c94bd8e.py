"""


:author: 
:contact: 
:email: 
:organization: 
:address: 
:copyright: 
:date: Mar 24 2023 12:42
:dragonflyVersion: 2022.2.0.1367
:UUID: db4417fdca6211ed90f744032c94bd8e
"""

__version__ = '1.0.0'

import os
import datetime
import time

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

from OrsPythonPlugins.OrsMacroPlayer.OrsMacroPlayer import OrsMacroPlayer

class ExportMultiROIAsMeshTop_db4417fdca6211ed90f744032c94bd8e(UserDefinedMenuItem):

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
        aMenuItem = Menu(title='Export MultiROI Labels as Meshes',
                         id_='ExportMultiROIAsMeshTop_db4417fdca6211ed90f744032c94bd8e',
                         section='',
                         action='ExportMultiROIAsMeshTop_db4417fdca6211ed90f744032c94bd8e.menuItemEntryPoint()')
        return aMenuItem

    @classmethod
    def menuItemEntryPoint(cls):
        """
        Will be executed when the menu item is selected.
        """

        cls._runMacro()

        # MultiToExport = cls._selectMultiROI("Select a MultiROI to Export")
        #
        # if MultiToExport == None:
        #     return
        #
        # start_time = time.time()
        #
        # aFolder = os.path.join(
        #     QFileDialog.getExistingDirectory(WorkingContext.getCurrentContextWindow(), caption="Select folder ",
        #                                      options=QFileDialog.ShowDirsOnly), '')
        # aFolder = os.path.join(aFolder, datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
        # os.makedirs(aFolder, exist_ok=True)

        # Put your code here
        pass

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
        return ChooseObjectAndNewName.prompt([class_object], parent=WorkingContext.getCurrentContextWindow(), dialog_title=dialog, allowNone=True, getNewTitle=False)

    @classmethod
    @interfaceMethod
    def _runMacro(cls):

        mcrPly = OrsMacroPlayer()
        path = "C:/Users/AlexisA/AppData/Local/ORS/Dragonfly2022.2/pythonUserExtensions/Macros/Jordan_Mesh_Export_c2469264e83d11ed973f44032c94bd8e.py"
        mcrPly.setMacroFromPath(path)
        mcrPly.executeMacro(True, False)
