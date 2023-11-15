
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import(QPushButton, QWidget, QVBoxLayout, QGroupBox,
                              QLineEdit, QHBoxLayout, QCheckBox, QToolButton,
                              QMenu, QComboBox)
from PySide6.QtGui import QIcon
from PySide6.QtCore import (Qt, QCoreApplication, QSize, Slot, Signal)

class AbstractMailBox(QWidget):
    def __init__(self) -> None:
        super().__init__()

    def SearchBar(self):
        self.searchbar_groupbox = QGroupBox()
        self.searchbar_layout = QHBoxLayout()

        self.searchbar_lineedit = QLineEdit()
        self.searchbar_lineedit.setToolTip("Search emails")
        self.searchbar_lineedit.setPlaceholderText("Search for words in an email, a sender...")
        self.searchbar_lineedit.returnPressed.connect(self.Search)

        self.searchbar_search_button_icon = QIcon("gui/assets/icons/search.svg")
        self.searchbar_search_button = QPushButton(self.searchbar_search_button_icon, "")
        self.searchbar_search_button.setToolTip("Search")
        self.searchbar_search_button.clicked.connect(self.Search)

        self.searchbar_settings_button_icon = QIcon("gui/assets/icons/settings.svg")
        self.searchbar_settings_button = QPushButton(self.searchbar_settings_button_icon, "")
        self.searchbar_settings_button.setToolTip("Filter settings")
        self.searchbar_settings_button.clicked.connect(self.FilterSettings)

        self.searchbar_layout.addWidget(self.searchbar_lineedit)
        self.searchbar_layout.addWidget(self.searchbar_search_button)
        self.searchbar_layout.addWidget(self.searchbar_settings_button)

        self.searchbar_groupbox.setLayout(self.searchbar_layout)
        self.searchbar_groupbox.setFixedHeight(self.searchbar_groupbox.sizeHint().height())

        return self.searchbar_groupbox
    
    @Slot()
    def Search(self):
        pass
    @Slot()
    def FilterSettings(self):
        pass

    def ConfigBar(self):
        self.configbar_groupbox = QGroupBox()
        self.configbar_layout = QHBoxLayout()

        self.configbar_select_all_checkbox = QCheckBox()
        self.configbar_select_all_checkbox.setToolTip("Select all emails")
        self.configbar_select_all_checkbox.toggled.connect(self.SelectAll)
        self.configbar_refresh_button_icon = QIcon("gui/assets/icons/refresh.svg")
        self.configbar_refresh_button = QPushButton(self.configbar_refresh_button_icon, "")
        self.configbar_refresh_button.setToolTip("Refresh")
        self.configbar_refresh_button.clicked.connect(self.Refresh)

        self.configbar_moreoptions_button = QToolButton()
        self.configbar_moreoptions_button.setToolTip("More options")
        self.configbar_moreoptions_button.setIcon(QIcon("gui/assets/icons/more_options.svg"))
        self.moreoptions_menu = QMenu(self.configbar_moreoptions_button)
        self.configbar_moreoptions_button.setPopupMode(QToolButton.InstantPopup)

        self.mark_all_as_read = self.moreoptions_menu.addAction(QIcon("gui/assets/icons/mark_email_read.svg"), "Mark all as read")
        self.mark_all_as_read.toggled.connect(self.MarkAllAsRead)
        self.mark_selected_as_unread = self.moreoptions_menu.addAction(QIcon("gui/assets/icons/mark_email_unread.svg"), "Mark selected as unread")
        self.mark_selected_as_unread.toggled.connect(self.MarkSelectedAsUnread)
        self.mark_selected_as_unread.setEnabled(False)
        self.mark_selected_as_important = self.moreoptions_menu.addAction(QIcon("gui/assets/icons/important.svg"), "Mark selected as important")
        self.mark_selected_as_important.toggled.connect(self.MarkSelectedAsImportant)
        self.mark_selected_as_important.setEnabled(False)
        self.mark_selected_as_starred = self.moreoptions_menu.addAction(QIcon("gui/assets/icons/starred.svg"), "Add star to selected")
        self.mark_selected_as_starred.toggled.connect(self.MarkSelectedAsStarred)
        self.mark_selected_as_starred.setEnabled(False)
        self.forward_selected_as_starred = self.moreoptions_menu.addAction(QIcon("gui/assets/icons/attachment.svg"), "Forward as attachment")
        self.forward_selected_as_starred.toggled.connect(self.ForwardAsAttachment)
        self.forward_selected_as_starred.setEnabled(False)

        self.email_amount_combobox = QComboBox()
        self.email_amount_combobox.addItems(["1-50", "51-100", "101-150", "151-200", "201-250", "250+"])
        self.email_amount_combobox.currentTextChanged.connect(self.UpdateEmailPage)
        self.email_page_backward_button = QPushButton(QIcon("gui/assets/icons/arrow_back.svg"), "")
        self.email_page_backward_button.clicked.connect(self.EmailPageBackwards)
        self.email_page_forward_button = QPushButton(QIcon("gui/assets/icons/arrow_forward.svg"), "")
        self.email_page_forward_button.clicked.connect(self.EmailPageForwards)
        
        
        self.configbar_moreoptions_button.setMenu(self.moreoptions_menu)

        self.configbar_layout.addWidget(self.configbar_select_all_checkbox)
        self.configbar_layout.addWidget(self.configbar_refresh_button)
        self.configbar_layout.addWidget(self.configbar_moreoptions_button)
        self.configbar_layout.addStretch(0)
        self.configbar_layout.addWidget(self.email_amount_combobox)
        self.configbar_layout.addWidget(self.email_page_backward_button)
        self.configbar_layout.addWidget(self.email_page_forward_button)
        
        self.configbar_groupbox.setLayout(self.configbar_layout)
        self.configbar_groupbox.setFixedHeight(self.configbar_groupbox.sizeHint().height())

        return self.configbar_groupbox

    @Slot()
    def SelectAll(self):
        pass
    @Slot()
    def Refresh(self):
        pass
    @Slot()
    def MarkAllAsRead(self):
        pass
    @Slot()
    def MarkSelectedAsUnread(self):
        pass
    @Slot()
    def MarkSelectedAsImportant(self):
        pass
    @Slot()
    def MarkSelectedAsStarred(self):
        pass
    @Slot()
    def ForwardAsAttachment(self):
        pass
    @Slot()
    def UpdateEmailPage(self):
        pass
    @Slot()
    def EmailPageBackwards(self):
        pass
    @Slot()
    def EmailPageForwards(self):
        pass

    def EmailSlate(self):
        self.emailslate_groupbox = QGroupBox()
        self.emailslate_layout = QHBoxLayout()

        self.emailslate_groupbox.setLayout(self.emailslate_layout)
        return self.emailslate_groupbox