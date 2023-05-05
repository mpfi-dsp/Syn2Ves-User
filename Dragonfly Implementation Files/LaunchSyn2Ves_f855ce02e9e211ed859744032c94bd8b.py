"""


:author: 
:contact: 
:email: 
:organization: 
:address: 
:copyright: 
:date: May 03 2023 14:47
:dragonflyVersion: 2022.2.0.1367
:UUID: f855ce02e9e211ed859744032c94bd8b
"""

__version__ = '1.0.0'

from ORSServiceClass.menuItems.userDefinedMenuItem import UserDefinedMenuItem
from ORSServiceClass.actionAndMenu.menu import Menu
from ORSServiceClass.decorators.infrastructure import interfaceMethod


class LaunchSyn2Ves_f855ce02e9e211ed859744032c94bd8b(UserDefinedMenuItem):

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
        aMenuItem = Menu(title='Launch Syn2Ves Program',
                         id_='LaunchSyn2Ves_f855ce02e9e211ed859744032c94bd8b',
                         section='',
                         action='LaunchSyn2Ves_f855ce02e9e211ed859744032c94bd8b.menuItemEntryPoint()')
        return aMenuItem

    @classmethod
    def menuItemEntryPoint(cls):
        """
        Will be executed when the menu item is selected.
        """

        import os
        os.system(r'"C:/Users/AlexisA/Documents/GitHub/Syn2Ves-User/dist/Syn2Ves 1.2.0.exe"')

        pass
        
        # If logging is relevant (used for macro recording and playing), a call to an interface methods is mandatory.
        # A prototype of such an interface method is written below (method "execute").
        # A full example is given in the demonstration file:
        # %ORSPYTHON%/OrsPythonPlugins/OrsGenericMenuItems/menuItems/demo_c18408e83c9511e7a502448a5b5d70c0.py

    # This is the prototype of an interface method:
    # @classmethod
    # @interfaceMethod
    # def execute(cls):
    #     """
    #     Doing this and that.
    #     """
    #     
    #     # Put your code here
    #     pass

