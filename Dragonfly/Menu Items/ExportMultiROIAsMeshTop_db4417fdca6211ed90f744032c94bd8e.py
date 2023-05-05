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
from ORSServiceClass.ORSWidget.chooseObjectAndNewName.chooseObjectAndNewName import ChooseObjectAndNewName
from ORSServiceClass.menuItems.userDefinedMenuItem import UserDefinedMenuItem
from ORSServiceClass.actionAndMenu.menu import Menu
from ORSServiceClass.decorators.infrastructure import interfaceMethod
from OrsLibraries.workingcontext import WorkingContext
from OrsPythonPlugins.OrsMacroPlayer.OrsMacroPlayer import OrsMacroPlayer

import configparser
import pathlib
import os

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

        # Get path of current script, and config file
        current_path = pathlib.Path(__file__).parent.resolve()
        config_path = os.path.join(current_path, "config.ini")

        # Read the config
        config = configparser.ConfigParser()
        config.read(config_path)

        # Get the values of the path variables
        dragonfly_macro_path = config.get('DEFAULT', 'dragonfly_macro_path')

        # Use the variables to run macro
        print(f"Dragonfly plugin path: {dragonfly_macro_path}")

        cls._runMacro(dragonfly_macro_path)

        pass

    @classmethod
    @interfaceMethod
    def _runMacro(cls, macroPath):
        """
        :param macroPath: Math to Macro for Exporting
        :type macroPath: str
        """

        mcrPly = OrsMacroPlayer()
        mcrPly.setMacroFromPath(macroPath)
        mcrPly.executeMacro(True, False)
