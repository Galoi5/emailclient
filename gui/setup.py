from enum import IntEnum
from PySide6.QtCore import QRegularExpression, QSize
from PySide6.QtWidgets import (QWizard, QWizardPage, QMessageBox,
                               QLabel, QRadioButton, QVBoxLayout, QLineEdit,
                               QGridLayout, QCheckBox, QPushButton)
from PySide6.QtGui import (QIcon)
from PySide6.QtGui import QPixmap, QRegularExpressionValidator
import json
from gui.login import LoginGui


LICENSE_LINK = "https://youtu.be/dQw4w9WgXcQ"



class Pages(IntEnum):
    INTRO_PAGE = 0
    ACCOUNTS_PAGE = 1
    LICENSE_PAGE = 2
    CONCLUSION_PAGE = 3

class IntroPage(QWizardPage):
    def __init__(self) -> None:
        super().__init__()

        self.setPixmap(QWizard.WatermarkPixmap, QPixmap("gui/assets/watermark.png"))
        self.setTitle("Welcome to the Email Client Setup Wizard")

        self.top_label = QLabel(
            "This setup wizard will allow you to install and connect "
            "one or multiple email accounts from different email providers. "
        )
        self.top_label.setWordWrap(True)

        layout = QVBoxLayout()
        layout.addWidget(self.top_label)

        self.setLayout(layout)

    def nextId(self) -> int:
        return Pages.ACCOUNTS_PAGE       

class AccountsPage(QWizardPage):
    def __init__(self) -> None:
        super().__init__()

        self.setTitle("Add accounts")
        self.setSubTitle("Choose whether you want to add email accounts to Email Client.")
        
        self.no_accounts_to_add = QRadioButton("I do not wish to add any accounts right now to Email Client.")
        self.no_accounts_to_add.setChecked(True)
        self.no_accounts_to_add.toggled.connect(self.hide_add_account)

        self.add_accounts = QRadioButton("I wish to add one or more accounts to Email Client.")
        self.no_accounts_to_add.toggled.connect(self.show_add_account)

        self.account_email_label = QLabel("Email:")
        self.account_email_edit = QLineEdit()
        self.account_email_edit.setPlaceholderText("example@example.com")
        self.account_email_label.setBuddy(self.account_email_edit)
        self.password_label = QLabel("Password:")
        self.password_edit = QLineEdit()
        self.password_label.setBuddy(self.password_edit)
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.toggle_password_echo_checkbox = QCheckBox("Show")
        self.toggle_password_echo_checkbox.toggled.connect(self.toggle_password_echo_mode)
        self.add_icon = QIcon()
        self.add_icon.addFile("gui/assets/icons/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_another_account_button = QPushButton()
        self.add_another_account_button.setText("Add another account")
        self.add_another_account_button.setIcon(self.add_icon)

        self.account_email_label.hide()
        self.account_email_edit.hide()
        self.password_label.hide()
        self.password_edit.hide()
        self.toggle_password_echo_checkbox.hide()
        self.add_another_account_button.hide()

        self.account_add_layout = QGridLayout()
        self.account_add_layout.addWidget(self.account_email_label, 1, 0)
        self.account_add_layout.addWidget(self.account_email_edit, 1, 1)
        self.account_add_layout.addWidget(self.password_label, 2, 0)
        self.account_add_layout.addWidget(self.password_edit, 2, 1)
        self.account_add_layout.addWidget(self.toggle_password_echo_checkbox, 2, 2)
        self.account_add_layout.addWidget(self.add_another_account_button, 3, 0, 1, 2 )

        self.account_layout = QGridLayout()
        self.account_layout.addWidget(self.no_accounts_to_add, 0, 0)
        self.account_layout.addWidget(self.add_accounts, 1,0)
        self.account_layout.addLayout(self.account_add_layout, 2, 0)

        self.setLayout(self.account_layout)
    
    def toggle_password_echo_mode(self):
        if self.toggle_password_echo_checkbox.isChecked():
            self.password_edit.setEchoMode(QLineEdit.Normal)
        else:
            self.password_edit.setEchoMode(QLineEdit.Password)

    def add_another_account(self):
        self.account_layout.addLayout(self.account_add_layout)

    def hide_add_account(self):
        self.account_email_label.hide()
        self.account_email_edit.hide()
        self.password_label.hide()
        self.password_edit.hide()
        self.toggle_password_echo_checkbox.hide()
        self.add_another_account_button.hide()

    def show_add_account(self):
        self.account_email_label.show()
        self.account_email_edit.show()
        self.password_label.show()
        self.password_edit.show()
        self.toggle_password_echo_checkbox.show()
        self.add_another_account_button.show()

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
        self.setTitle("Email Client is done being setup.")
        self.setPixmap(QWizard.WatermarkPixmap, QPixmap("gui/assets/watermark.png"))

        self.setFinalPage(True)

        self.conclusion_label = QLabel("Click \"Finish\" to exit the setup wizard.")
        self.conclusion_label.setWordWrap(True)

        layout = QVBoxLayout()
        layout.addWidget(self.conclusion_label)

        self.setLayout(layout)

class SetupWizard(QWizard):
    def __init__(self) -> None:
        super().__init__()

        self._pages = [
            IntroPage(),
            AccountsPage(),
            LicensePage(),
            ConclusionPage()
        ]

        for page in self._pages:
            self.addPage(page)

        self.setStartId(Pages.INTRO_PAGE)
        self.setWizardStyle(QWizard.ModernStyle)
        self.setOption(QWizard.HaveHelpButton, True)
        self.setWindowTitle("Email Client Setup Wizard")

        self.helpRequested.connect(self.show_help)

        self.accepted.connect(self.on_accepted)

    def show_help(self):
        if self.currentId() == Pages.INTRO_PAGE:
            message = ('Click "Next" to setup Email Client.')

        elif self.currentId() == Pages.ACCOUNTS_PAGE:
            message = (
                "Choose whether to add one or multiple accounts now and save their login information, "
                "or not to and login manually later on..."
            )


        elif self.currentId() == Pages.LICENSE_PAGE:
            message = (
                "Click the link in order to be redirected to the terms and conditions. "
                "Tick the checkbox in order to confirm your agreement to said terms and conditions."
            )

        elif self.currentId() == Pages.CONCLUSION_PAGE:
            message = "Thank you, you can now exit this wizard."


        QMessageBox.information(self, "License Wizard Help", message)

    def on_accepted(self):
        with open("config.json", "r") as json_file:
            data = json.load(json_file)

        data["setup"] = True

        with open("config.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        global login
        login = LoginGui()
        login.setFixedSize(QSize(400, login.sizeHint().height()))
        login.show()    
        self.deleteLater()        






        







