# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginForm.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
import Icons_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        icon = QIcon()
        icon.addFile(u":/Main/chizu.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"background-color: rgb(135, 193, 255);")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.AppLoginForm = QGroupBox(Form)
        self.AppLoginForm.setObjectName(u"AppLoginForm")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.AppLoginForm.setFont(font)
        self.AppLoginForm.setStyleSheet(u"")
        self.AppLoginForm.setAlignment(Qt.AlignCenter)
        self.formLayout = QFormLayout(self.AppLoginForm)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.AppLoginForm)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_UserID = QLineEdit(self.AppLoginForm)
        self.le_UserID.setObjectName(u"le_UserID")
        self.le_UserID.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_UserID)

        self.label_2 = QLabel(self.AppLoginForm)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.le_Password = QLineEdit(self.AppLoginForm)
        self.le_Password.setObjectName(u"le_Password")
        self.le_Password.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.le_Password.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_Password)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(2, QFormLayout.SpanningRole, self.verticalSpacer)


        self.gridLayout.addWidget(self.AppLoginForm, 0, 0, 1, 2)

        self.pb_OK = QPushButton(Form)
        self.pb_OK.setObjectName(u"pb_OK")
        self.pb_OK.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/tick.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_OK.setIcon(icon1)

        self.gridLayout.addWidget(self.pb_OK, 1, 0, 1, 1)

        self.pb_Cancel = QPushButton(Form)
        self.pb_Cancel.setObjectName(u"pb_Cancel")
        self.pb_Cancel.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_Cancel.setIcon(icon2)

        self.gridLayout.addWidget(self.pb_Cancel, 1, 1, 1, 1)

        self.lb_Message = QLabel(Form)
        self.lb_Message.setObjectName(u"lb_Message")

        self.gridLayout.addWidget(self.lb_Message, 2, 0, 1, 2)

        QWidget.setTabOrder(self.le_UserID, self.le_Password)
        QWidget.setTabOrder(self.le_Password, self.pb_OK)
        QWidget.setTabOrder(self.pb_OK, self.pb_Cancel)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.AppLoginForm.setTitle(QCoreApplication.translate("Form", u"Welcome! Please Login", None))
        self.label.setText(QCoreApplication.translate("Form", u"User ID", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Password", None))
        self.pb_OK.setText(QCoreApplication.translate("Form", u"OK", None))
        self.pb_Cancel.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.lb_Message.setText(QCoreApplication.translate("Form", u"Message", None))
    # retranslateUi

