from enum import IntEnum
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (QWizard, QWizardPage, QMessageBox,
                               QLabel, QRadioButton, QVBoxLayout, QLineEdit,
                               QGridLayout, QCheckBox, QGroupBox, QTextBrowser)
from PySide6.QtGui import QPixmap, QRegularExpressionValidator
import json
from gui.login import LoginGui

LICENSE_LINK = "https://youtu.be/dQw4w9WgXcQ"

def get_latest_version() -> str:
    #add code to get version
    return "0.0.2"

class Pages(IntEnum):
    UPDATE_PAGE         = 0 # let user know that there is an update available
    CHANGELOG_PAGE      = 1
    LICENSE_PAGE        = 2
    CONCLUSION_PAGE     = 3

class UpdatePage(QWizardPage):
    def __init__(self) -> None:
        super().__init__()

        self.setPixmap(QWizard.WatermarkPixmap, QPixmap("gui/assets/watermark.png"))
        self.setTitle("Welcome to the Red Horse Update Wizard")

        self.top_label = QLabel(
            "This update wizard will allow you to update "
            "your version of <b>Red Horse</b>."
        )
        self.top_label.setWordWrap(True)

        layout = QVBoxLayout()
        layout.addWidget(self.top_label)

        self.setLayout(layout)

    def nextId(self) -> int:
        return Pages.CHANGELOG_PAGE      

class ChangelogPage(QWizardPage):
    def __init__(self) -> None:
        super().__init__()

        self.setTitle("Change Log")
        self.setSubTitle(f"Here are the changes made to Red Horse version <b>{get_latest_version()}</b>.")
        
        self.changelog_groupbox = QGroupBox()
        self.groupbox_layout = QVBoxLayout()
        self.changelog_groupbox.setLayout(self.groupbox_layout)

        self.changelog_text_browser = QTextBrowser()
        #
        # add qtextbrowser functionality
        #

        self.groupbox_layout.addWidget(self.changelog_text_browser)

        layout = QGridLayout()
        layout.addWidget(self.changelog_groupbox)
        
        self.setLayout(layout)
    

    def nextId(self) -> int:
        return Pages.LICENSE_PAGE
    
class LicensePage(QWizardPage):
    def __init__(self) -> None:
        super().__init__()
        self.setTitle("License Agreement")
        self.setSubTitle("Please read the following license agreement carefully.")
        self.license_agreement_link = QLabel("Please refer to this link in order to view the <a href=" + LICENSE_LINK + "> Terms & Conditions</a>. "
                                             "By clicking the checkbox below, you agree to the terms and conditions."
                                             )
        self.license_agreement_link.setWordWrap(True)
        self.license_agreement_link.setOpenExternalLinks(True)
        self.agree_to_license_checkbox = QCheckBox("I Agree to the Terms && Conditions")
        self.agree_to_license_checkbox.setChecked(False)

        self.registerField("license.agree*", self.agree_to_license_checkbox)

        layout = QVBoxLayout()
        layout.addWidget(self.license_agreement_link)
        layout.addSpacing(20)
        layout.addWidget(self.agree_to_license_checkbox)
        
        self.setLayout(layout)

    def nextId(self) -> int:
        return Pages.CONCLUSION_PAGE

class ConclusionPage(QWizardPage):
    def __init__(self) -> None:
        super().__init__()
        self.setTitle("Red Horse is done being setup.")
        self.setPixmap(QWizard.WatermarkPixmap, QPixmap("gui/assets/watermark.png"))

        self.setFinalPage(True)
    
        self.conclusion_label = QLabel("Thank you for using Cicada. Click \"Finish\" to exit the setup wizard.")
        self.conclusion_label.setWordWrap(True)

        layout = QVBoxLayout()
        layout.addWidget(self.conclusion_label)

        self.setLayout(layout)

class UpdateWizard(QWizard):
    def __init__(self) -> None:
        super().__init__()
        self.version = ""

        self._pages = [
            UpdatePage(),
            ChangelogPage(),
            LicensePage(),
            ConclusionPage()
        ]

        for page in self._pages:
            self.addPage(page)

        self.setStartId(Pages.UPDATE_PAGE)
        self.setWizardStyle(QWizard.ModernStyle)
        self.setOption(QWizard.HaveHelpButton, True)
        self.setWindowTitle("Cicada Setup Wizard")

        self.helpRequested.connect(self.show_help)

        self.accepted.connect(self.on_accepted)

    def show_help(self):
        if self.currentId() == Pages.UPDATE_PAGE:
            message = ("An update is available, please click next to download it.")

        elif self.currentId() == Pages.CHANGELOG_PAGE:
            message = (
                "Here is the changelog. Everything that has changed will be here."
            )

        elif self.currentId() == Pages.LICENSE_PAGE:
            message = (
                "Click the link in order to be redirected to the terms and conditions. "
                "Tick the checkbox in order to confirm your agreement to said terms and conditions."
            )

        elif self.currentId() == Pages.CONCLUSION_PAGE:
            message = "Thank you for updating Red Horse, you can now exit this wizard."


        QMessageBox.information(self, "Help", message)

    def on_accepted(self):
        with open("config.json", "r") as json_file:
            data = json.load(json_file)

        data["version"] = get_latest_version()

        with open("config.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        global login
        login = LoginGui()
        login.setFixedSize(QSize(400, login.sizeHint().height()))
        login.show()    
        self.deleteLater() 