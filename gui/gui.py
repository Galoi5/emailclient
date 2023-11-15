from typing import Optional
from PySide6.QtWidgets import (QMainWindow, QToolBar, QWidget, QSizePolicy,
                               QStackedWidget, QToolButton, QMenu, QDialog, QGridLayout,
                               QLabel, QLineEdit, QPushButton, QScrollArea, QVBoxLayout, QCheckBox)
from PySide6.QtGui import (QAction, QIcon)
from PySide6.QtCore import (Qt, QCoreApplication, QSize, Slot, Signal)

#categories imports
from gui.ui.categories.forums.forums import ForumsGui
from gui.ui.categories.promotions.promotions import PromotionsGui
from gui.ui.categories.social.social import ScoialGui
from gui.ui.categories.updates.updates import UpdatesGui
#rest of the imports
from gui.ui.drafts.drafts import DraftsGui
from gui.ui.important.important import ImportantGui
from gui.ui.inbox.inbox import InboxGui
from gui.ui.labels.labels import LabelsGui
from gui.ui.sent.sent import SentGui
from gui.ui.spam.spam import SpamGui
from gui.ui.starred.starred import StarredGui
from gui.ui.trash.trash import TrashGui

class RemoveLabelDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.labels = LabelsGui().labels # list of labels from text file read line by line

        self.dialog_layout = QVBoxLayout()
        self.scroll_area = QScrollArea()
        self.scroll_widget = QWidget()
        self.scroll_layout = QGridLayout()

        for u in range(len(self.labels)):
            label = QLabel(self.labels[u])
            check = QCheckBox()
            check.toggled.connect(self.label_selected(self.labels[u]))
            self.scroll_layout.addWidget(label, u, 0)
            self.scroll_layout.addWidget(check, u, 1)
            
        self.scroll_widget.setLayout(self.scroll_layout)

        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.scroll_widget)

        self.remove_selected_button_icon = QIcon("gui/assets/icons/trash.svg")
        self.remove_selected_button = QPushButton(self.remove_selected_button_icon, "Remove selected")
        self.remove_selected_button.clicked.connect(self.remove_label)
        self.dialog_layout.addWidget(self.scroll_area)
        self.dialog_layout.addWidget(self.remove_selected_button)

        self.setWindowTitle("Remove a label")
        self.setLayout(self.dialog_layout)

    @Slot()
    def label_selected(self, label):
        print(label) # want to get the name of the label
    @Slot()
    def remove_label(self, index):
        LabelsGui().RemoveLabel(index) # here this wont work obviously but we want to get the label index so we know what to remove...
        self.deleteLater()

class LabelNameDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.dialog_layout = QGridLayout()
        self.label_name_label = QLabel("Label name:")
        self.label_name_edit = QLineEdit()
        self.label_name_label.setBuddy(self.label_name_edit)
        self.label_name_add_button_icon = QIcon("gui/assets/icons/add.svg")
        self.label_name_add_button = QPushButton(self.label_name_add_button_icon, "Add label")
        self.label_name_add_button.clicked.connect(self.write_label)

        self.dialog_layout.addWidget(self.label_name_label, 0, 0)
        self.dialog_layout.addWidget(self.label_name_edit, 0, 1)
        self.dialog_layout.addWidget(self.label_name_add_button, 1, 0, 1, 2)
        self.setWindowTitle("Add a label")
        self.setLayout(self.dialog_layout)

    @Slot()
    def write_label(self):
        LabelsGui().AddLabel(self.label_name_edit.text())
        self.deleteLater()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("Email Client")
        self.tool_bar = QToolBar(self)
        self.tool_bar.setObjectName(u"toolBar")
        self.addToolBar(Qt.LeftToolBarArea, self.tool_bar)
        self.tool_bar.setMovable(False)
        self._add_toolbar_actions()

        self._slate = QStackedWidget()
        self.setCentralWidget(self._slate)

        self.forums     = ForumsGui()
        self.promotions = PromotionsGui()
        self.social     = ScoialGui()
        self.updates    = UpdatesGui()
        self.drafts     = DraftsGui()
        self.important  = ImportantGui()
        self.inbox      = InboxGui()
        self.labels     = LabelsGui()
        self.sent       = SentGui()
        self.spam       = SpamGui()
        self.starred    = StarredGui()
        self.trash      = TrashGui()
        # categories :

        self._slate.addWidget(self.forums)
        self._slate.addWidget(self.promotions)
        self._slate.addWidget(self.social)
        self._slate.addWidget(self.updates)
        self._slate.addWidget(self.drafts)
        self._slate.addWidget(self.important)
        self._slate.addWidget(self.inbox)
        self._slate.addWidget(self.labels)
        self._slate.addWidget(self.sent)
        self._slate.addWidget(self.spam)
        self._slate.addWidget(self.starred)
        self._slate.addWidget(self.trash)

        self._slate.setCurrentWidget(self.inbox)
    
    def _add_toolbar_actions(self):
        self.inbox_toolbar_button = QToolButton()
        self.inbox_toolbar_icon = QIcon("gui/assets/icons/inbox.svg")
        self.inbox_toolbar_button.setIcon(self.inbox_toolbar_icon)
        self.inbox_toolbar_button.setToolTip("Inbox")
        self.inbox_toolbar_button.clicked.connect(self.show_inbox_widget)

        self.starred_toolbar_button = QToolButton()
        self.starred_toolbar_icon = QIcon("gui/assets/icons/starred.svg")
        self.starred_toolbar_button.setIcon(self.starred_toolbar_icon)
        self.starred_toolbar_button.setToolTip("Starred")
        self.starred_toolbar_button.clicked.connect(self.show_starred_widget)

        self.sent_toolbar_button = QToolButton()
        self.sent_toolbar_icon = QIcon("gui/assets/icons/sent.svg")
        self.sent_toolbar_button.setIcon(self.sent_toolbar_icon)
        self.sent_toolbar_button.setToolTip("Sent")
        self.sent_toolbar_button.clicked.connect(self.show_sent_widget)

        self.drafts_toolbar_button = QToolButton()
        self.drafts_toolbar_icon = QIcon("gui/assets/icons/drafts.svg")
        self.drafts_toolbar_button.setIcon(self.drafts_toolbar_icon)
        self.drafts_toolbar_button.setToolTip("Drafts")
        self.drafts_toolbar_button.clicked.connect(self.show_drafts_widget)
        

        self.important_toolbar_button = QToolButton()
        self.important_toolbar_icon = QIcon("gui/assets/icons/important.svg")
        self.important_toolbar_button.setIcon(self.important_toolbar_icon)
        self.important_toolbar_button.setToolTip("Important")
        self.important_toolbar_button.clicked.connect(self.show_important_widget)

        self.spam_toolbar_button = QToolButton()
        self.spam_toolbar_icon = QIcon("gui/assets/icons/spam.svg")
        self.spam_toolbar_button.setIcon(self.spam_toolbar_icon)
        self.spam_toolbar_button.setToolTip("Spam")
        self.spam_toolbar_button.clicked.connect(self.show_spam_widget)

        self.categories_toolbar_button = QToolButton()
        self.categories_menu = QMenu(self.categories_toolbar_button)
        self.categories_toolbar_icon = QIcon("gui/assets/icons/categories.svg")
        self.categories_toolbar_button.setIcon(self.categories_toolbar_icon)
        self.categories_toolbar_button.setToolTip("Categories")
        self.categories_toolbar_button.setPopupMode(QToolButton.InstantPopup)

        self.forums_category_icon = QIcon("gui/assets/icons/forums.svg")
        self.forums_category = self.categories_menu.addAction(self.forums_category_icon, "Forums")
        self.forums_category.triggered.connect(self.show_forums_widget)
        self.promotions_category_icon = QIcon("gui/assets/icons/promotions.svg")
        self.promotions_category = self.categories_menu.addAction(self.promotions_category_icon, "Promotions")
        self.promotions_category.triggered.connect(self.show_promotions_widget)
        self.social_category_icon = QIcon("gui/assets/icons/social.svg")
        self.social_category = self.categories_menu.addAction(self.social_category_icon, "Social")
        self.social_category.triggered.connect(self.show_social_widget)
        self.updates_category_icon = QIcon("gui/assets/icons/updates.svg")
        self.updates_category = self.categories_menu.addAction(self.updates_category_icon, "Updates")
        self.updates_category.triggered.connect(self.show_updates_widget)

        self.categories_toolbar_button.setMenu(self.categories_menu)

        self.labels_toolbar_button = QToolButton()
        self.labels_menu = QMenu(self.labels_toolbar_button)
        self.labels_toolbar_icon = QIcon("gui/assets/icons/labels.svg")
        self.labels_toolbar_button.setIcon(self.labels_toolbar_icon)
        self.labels_toolbar_button.setToolTip("Labels")
        self.labels_toolbar_button.setPopupMode(QToolButton.InstantPopup)

        self.add_label_icon = QIcon("gui/assets/icons/add.svg")
        self.add_label = self.labels_menu.addAction(self.add_label_icon, "Add a label")
        self.add_label.triggered.connect(self.show_add_label_dialog)
        self.remove_label_icon = QIcon("gui/assets/icons/trash.svg")
        self.remove_label = self.labels_menu.addAction(self.remove_label_icon, "Remove a label")
        self.remove_label.triggered.connect(self.show_remove_label_dialog)
        self.labels_menu.addSeparator()
        
        self.label_icon = QIcon("gui/assets/icons/label_filled.svg")
        for label in LabelsGui().labels:
            self.labels_menu.addAction(self.label_icon, label)

        self.labels_toolbar_button.setMenu(self.labels_menu)

        self.trash_toolbar_button = QToolButton()
        self.trash_toolbar_icon = QIcon("gui/assets/icons/trash.svg")
        self.trash_toolbar_button.setIcon(self.trash_toolbar_icon)
        self.trash_toolbar_button.setToolTip("Trash")
        self.trash_toolbar_button.clicked.connect(self.show_trash_widget)
        
        self.tool_bar.addWidget(self.inbox_toolbar_button)
        self.tool_bar.addWidget(self.starred_toolbar_button)
        self.tool_bar.addWidget(self.sent_toolbar_button)
        self.tool_bar.addWidget(self.drafts_toolbar_button)
        self.tool_bar.addWidget(self.important_toolbar_button)
        self.tool_bar.addWidget(self.spam_toolbar_button)
        self.tool_bar.addWidget(self.categories_toolbar_button)
        self.tool_bar.addWidget(self.labels_toolbar_button)
        self.tool_bar.addWidget(self.trash_toolbar_button)

        

    @Slot()
    def show_inbox_widget(self):
        self._slate.setCurrentWidget(self.inbox)
    @Slot()
    def show_starred_widget(self):
        self._slate.setCurrentWidget(self.starred)
    @Slot()
    def show_sent_widget(self):
        self._slate.setCurrentWidget(self.sent)
    @Slot()
    def show_important_widget(self):
        self._slate.setCurrentWidget(self.important)
    @Slot()
    def show_drafts_widget(self):
        self._slate.setCurrentWidget(self.drafts)
    @Slot()
    def show_spam_widget(self):
        self._slate.setCurrentWidget(self.spam)
    # important group
    @Slot()
    def show_social_widget(self):
        self._slate.setCurrentWidget(self.social)
    @Slot()
    def show_forums_widget(self):
        self._slate.setCurrentWidget(self.forums)
    @Slot()
    def show_promotions_widget(self):
        self._slate.setCurrentWidget(self.promotions)
    @Slot()
    def show_updates_widget(self):
        self._slate.setCurrentWidget(self.updates)
    # labels group
    # @Slot()
    # def show_inbox_widget(self):
    #     self._slate.setCurrentWidget(self.inbox)
    #   gotta get working for all and every label...
    #
    
    @Slot()
    def show_trash_widget(self):
        self._slate.setCurrentWidget(self.trash)

    @Slot()
    def show_add_label_dialog(self):
        global dialog
        dialog = LabelNameDialog()
        dialog.show()
    @Slot()
    def show_remove_label_dialog(self):
        global dialog2
        dialog2 = RemoveLabelDialog()
        dialog2.show()
        

        
    



    

       


