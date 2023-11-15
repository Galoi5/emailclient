import json
import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSize

from gui.setup import SetupWizard
from gui.login import LoginGui
from gui.updater import UpdateWizard

from gui.themes.themes import gui_default_palette

class EmailClient():
    def __init__(self) -> None:
        self._file = open('config.json', 'r')
        self._data = json.load(self._file)

    def _is_setup(self) -> bool:
        if self._data['setup'] == True:
            return True
        else:
            return False
    
    def _is_latest_version(self) -> bool:
        _version = self._data['version']

        # check whether is the latest version
        # make request to central server and wait for a response
        # if response is 200, then return True
        # else return False
        return True

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setPalette(gui_default_palette(app=app))
    app.setWindowIcon(QIcon("gui/assets/logos/emailclient.svg"))

    if EmailClient()._is_latest_version():

        if EmailClient()._is_setup():
            login = LoginGui()
            login.setFixedSize(QSize(400, login.sizeHint().height()))
            login.show()

        else:
            wizard = SetupWizard()
            wizard.setFixedSize(wizard.sizeHint())
            wizard.show()

    else:
        update_wizard = UpdateWizard()
        update_wizard.setFixedSize(update_wizard.sizeHint())
        update_wizard.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()