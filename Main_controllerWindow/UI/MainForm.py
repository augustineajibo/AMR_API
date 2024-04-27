# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainForm.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        if not MainForm.objectName():
            MainForm.setObjectName(u"MainForm")
        MainForm.setWindowModality(Qt.WindowModal)
        MainForm.resize(1363, 863)
        font = QFont()
        font.setPointSize(12)
        MainForm.setFont(font)
        MainForm.setStyleSheet(u"background-color: rgb(89, 89, 89);")
        self.verticalLayout_2 = QVBoxLayout(MainForm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Frame_Title = QFrame(MainForm)
        self.Frame_Title.setObjectName(u"Frame_Title")
        self.Frame_Title.setMaximumSize(QSize(16777215, 50))
        self.Frame_Title.setStyleSheet(u"background-color: rgb(84, 84, 84);")
        self.Frame_Title.setFrameShape(QFrame.StyledPanel)
        self.Frame_Title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Frame_Title)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_LexxPluss = QLabel(self.Frame_Title)
        self.lb_LexxPluss.setObjectName(u"lb_LexxPluss")
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(14)
        self.lb_LexxPluss.setFont(font1)
        self.lb_LexxPluss.setStyleSheet(u"color: rgb(232, 232, 232);")

        self.horizontalLayout.addWidget(self.lb_LexxPluss)


        self.verticalLayout_2.addWidget(self.Frame_Title)

        self.frame_2 = QFrame(MainForm)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(118, 118, 118);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"color: rgb(52, 52, 52);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(106, 106, 106);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.label)

        self.lb_Map = QLabel(self.frame_6)
        self.lb_Map.setObjectName(u"lb_Map")
        self.lb_Map.setStyleSheet(u"background-color: rgb(74, 74, 74);")

        self.verticalLayout_5.addWidget(self.lb_Map)

        self.widget_2 = QWidget(self.frame_6)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(30, 16777215))
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)


        self.verticalLayout_5.addWidget(self.widget_2)


        self.horizontalLayout_3.addWidget(self.frame_6)

        self.line = QFrame(self.frame_4)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"color: rgb(22, 22, 22);\n"
"background-color: rgb(38, 38, 38);")
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.label_2)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(58, 58, 58);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_AMR = QFrame(self.frame_7)
        self.frame_AMR.setObjectName(u"frame_AMR")
        self.frame_AMR.setStyleSheet(u"background-color: rgb(120, 120, 120);")
        self.frame_AMR.setFrameShape(QFrame.StyledPanel)
        self.frame_AMR.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_AMR)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_14 = QFrame(self.frame_AMR)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(700, 16777215))
        self.frame_14.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_14)

        self.line_13 = QFrame(self.frame_AMR)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.line_13.setFrameShape(QFrame.VLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_10.addWidget(self.line_13)

        self.frame_13 = QFrame(self.frame_AMR)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(300, 16777215))
        self.frame_13.setStyleSheet(u"background-color: rgb(173, 173, 173);")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_13)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_19 = QLabel(self.frame_18)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_13.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_18)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_13.addWidget(self.label_20)


        self.verticalLayout_11.addWidget(self.frame_18)

        self.line_6 = QFrame(self.frame_13)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"color: rgb(21, 21, 21);")
        self.line_6.setLineWidth(2)
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line_6)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_16 = QLabel(self.frame_15)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_11.addWidget(self.label_16)

        self.label_15 = QLabel(self.frame_15)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_11.addWidget(self.label_15)


        self.verticalLayout_11.addWidget(self.frame_15)

        self.line_5 = QFrame(self.frame_13)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"color: rgb(29, 29, 29);")
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line_5)

        self.frame_17 = QFrame(self.frame_13)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_18 = QLabel(self.frame_17)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_12.addWidget(self.label_18)

        self.label_17 = QLabel(self.frame_17)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_12.addWidget(self.label_17)


        self.verticalLayout_11.addWidget(self.frame_17)


        self.horizontalLayout_10.addWidget(self.frame_13)


        self.verticalLayout_7.addWidget(self.frame_AMR)

        self.line_3 = QFrame(self.frame_7)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_3)

        self.widget_Robot = QWidget(self.frame_7)
        self.widget_Robot.setObjectName(u"widget_Robot")
        self.widget_Robot.setMaximumSize(QSize(16777215, 200))
        self.widget_Robot.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.verticalLayout_8 = QVBoxLayout(self.widget_Robot)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_8 = QFrame(self.widget_Robot)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_frontLeft = QLabel(self.frame_8)
        self.lb_frontLeft.setObjectName(u"lb_frontLeft")

        self.horizontalLayout_5.addWidget(self.lb_frontLeft)

        self.line_17 = QFrame(self.frame_8)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.VLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_17)

        self.lb_frontLeft_value = QLabel(self.frame_8)
        self.lb_frontLeft_value.setObjectName(u"lb_frontLeft_value")

        self.horizontalLayout_5.addWidget(self.lb_frontLeft_value)


        self.verticalLayout_8.addWidget(self.frame_8)

        self.line_14 = QFrame(self.widget_Robot)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setStyleSheet(u"color: rgb(127, 127, 127);\n"
"background-color: rgb(127, 127, 127);")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_14)

        self.lb_left_value = QFrame(self.widget_Robot)
        self.lb_left_value.setObjectName(u"lb_left_value")
        self.lb_left_value.setFrameShape(QFrame.StyledPanel)
        self.lb_left_value.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.lb_left_value)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lb_left = QLabel(self.lb_left_value)
        self.lb_left.setObjectName(u"lb_left")

        self.horizontalLayout_7.addWidget(self.lb_left)

        self.line_18 = QFrame(self.lb_left_value)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.VLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line_18)

        self.lb_left_value_2 = QLabel(self.lb_left_value)
        self.lb_left_value_2.setObjectName(u"lb_left_value_2")

        self.horizontalLayout_7.addWidget(self.lb_left_value_2)


        self.verticalLayout_8.addWidget(self.lb_left_value)

        self.line_15 = QFrame(self.widget_Robot)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setStyleSheet(u"color: rgb(127, 127, 127);\n"
"background-color: rgb(127, 127, 127);")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_15)

        self.frame_11 = QFrame(self.widget_Robot)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lb_right = QLabel(self.frame_11)
        self.lb_right.setObjectName(u"lb_right")

        self.horizontalLayout_8.addWidget(self.lb_right)

        self.line_19 = QFrame(self.frame_11)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.VLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_19)

        self.lb_right_value = QLabel(self.frame_11)
        self.lb_right_value.setObjectName(u"lb_right_value")

        self.horizontalLayout_8.addWidget(self.lb_right_value)


        self.verticalLayout_8.addWidget(self.frame_11)

        self.line_16 = QFrame(self.widget_Robot)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setStyleSheet(u"color: rgb(127, 127, 127);\n"
"background-color: rgb(127, 127, 127);")
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_16)

        self.lb_rear = QFrame(self.widget_Robot)
        self.lb_rear.setObjectName(u"lb_rear")
        self.lb_rear.setFrameShape(QFrame.StyledPanel)
        self.lb_rear.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.lb_rear)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lb_rear_2 = QLabel(self.lb_rear)
        self.lb_rear_2.setObjectName(u"lb_rear_2")

        self.horizontalLayout_9.addWidget(self.lb_rear_2)

        self.line_20 = QFrame(self.lb_rear)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.VLine)
        self.line_20.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_9.addWidget(self.line_20)

        self.lb_rear_2_value = QLabel(self.lb_rear)
        self.lb_rear_2_value.setObjectName(u"lb_rear_2_value")

        self.horizontalLayout_9.addWidget(self.lb_rear_2_value)


        self.verticalLayout_8.addWidget(self.lb_rear)


        self.verticalLayout_7.addWidget(self.widget_Robot)


        self.verticalLayout_6.addWidget(self.frame_7)

        self.line_2 = QFrame(self.frame_5)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_2)


        self.horizontalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.widget = QWidget(self.frame_3)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 150))
        self.widget.setStyleSheet(u"background-color: rgb(70, 70, 70);")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lb_sysLogs = QLabel(self.widget)
        self.lb_sysLogs.setObjectName(u"lb_sysLogs")
        self.lb_sysLogs.setMaximumSize(QSize(16777215, 20))
        self.lb_sysLogs.setStyleSheet(u"color: rgb(255, 255, 0);")

        self.verticalLayout_4.addWidget(self.lb_sysLogs)

        self.lb_Logs = QLabel(self.widget)
        self.lb_Logs.setObjectName(u"lb_Logs")
        self.lb_Logs.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.lb_Logs)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_StatCtrlPanel = QFrame(self.frame_2)
        self.frame_StatCtrlPanel.setObjectName(u"frame_StatCtrlPanel")
        self.frame_StatCtrlPanel.setMaximumSize(QSize(300, 16777215))
        self.frame_StatCtrlPanel.setStyleSheet(u"background-color: rgb(124, 124, 124);")
        self.frame_StatCtrlPanel.setFrameShape(QFrame.StyledPanel)
        self.frame_StatCtrlPanel.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_StatCtrlPanel)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_pb = QFrame(self.frame_StatCtrlPanel)
        self.frame_pb.setObjectName(u"frame_pb")
        self.frame_pb.setStyleSheet(u"background-color: rgb(156, 156, 156);\n"
"color: rgb(21, 21, 21);")
        self.frame_pb.setFrameShape(QFrame.StyledPanel)
        self.frame_pb.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_pb)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_16 = QFrame(self.frame_pb)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_16)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_7 = QLabel(self.frame_16)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 40))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_7)

        self.frame_26 = QFrame(self.frame_16)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(16777215, 40))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_21 = QLabel(self.frame_26)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_19.addWidget(self.label_21)

        self.label_8 = QLabel(self.frame_26)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_19.addWidget(self.label_8)


        self.verticalLayout_12.addWidget(self.frame_26)

        self.frame_20 = QFrame(self.frame_16)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 40))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.comboBox_4 = QComboBox(self.frame_20)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_6.addWidget(self.comboBox_4)

        self.line_7 = QFrame(self.frame_20)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line_7)

        self.comboBox = QComboBox(self.frame_20)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setAcceptDrops(False)

        self.horizontalLayout_6.addWidget(self.comboBox)


        self.verticalLayout_12.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_16)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 40))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.comboBox_8 = QComboBox(self.frame_21)
        self.comboBox_8.setObjectName(u"comboBox_8")

        self.horizontalLayout_14.addWidget(self.comboBox_8)

        self.line_8 = QFrame(self.frame_21)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_14.addWidget(self.line_8)

        self.comboBox_2 = QComboBox(self.frame_21)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_14.addWidget(self.comboBox_2)


        self.verticalLayout_12.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_16)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(16777215, 40))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.comboBox_9 = QComboBox(self.frame_22)
        self.comboBox_9.setObjectName(u"comboBox_9")

        self.horizontalLayout_15.addWidget(self.comboBox_9)

        self.line_9 = QFrame(self.frame_22)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_15.addWidget(self.line_9)

        self.comboBox_3 = QComboBox(self.frame_22)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMaximumSize(QSize(16777215, 40))
        self.comboBox_3.setEditable(False)

        self.horizontalLayout_15.addWidget(self.comboBox_3)


        self.verticalLayout_12.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_16)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(16777215, 40))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.comboBox_10 = QComboBox(self.frame_23)
        self.comboBox_10.setObjectName(u"comboBox_10")

        self.horizontalLayout_16.addWidget(self.comboBox_10)

        self.line_10 = QFrame(self.frame_23)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_16.addWidget(self.line_10)

        self.comboBox_5 = QComboBox(self.frame_23)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.horizontalLayout_16.addWidget(self.comboBox_5)


        self.verticalLayout_12.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_16)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(16777215, 40))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.comboBox_11 = QComboBox(self.frame_24)
        self.comboBox_11.setObjectName(u"comboBox_11")

        self.horizontalLayout_17.addWidget(self.comboBox_11)

        self.line_11 = QFrame(self.frame_24)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_17.addWidget(self.line_11)

        self.comboBox_6 = QComboBox(self.frame_24)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.horizontalLayout_17.addWidget(self.comboBox_6)


        self.verticalLayout_12.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.frame_16)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(16777215, 40))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.comboBox_12 = QComboBox(self.frame_25)
        self.comboBox_12.setObjectName(u"comboBox_12")

        self.horizontalLayout_18.addWidget(self.comboBox_12)

        self.line_12 = QFrame(self.frame_25)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_18.addWidget(self.line_12)

        self.comboBox_7 = QComboBox(self.frame_25)
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.horizontalLayout_18.addWidget(self.comboBox_7)


        self.verticalLayout_12.addWidget(self.frame_25)


        self.verticalLayout_10.addWidget(self.frame_16)

        self.line_4 = QFrame(self.frame_pb)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"color: rgb(17, 17, 17);\n"
"background-color: rgb(74, 74, 74);")
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.line_4)

        self.frame_9 = QFrame(self.frame_pb)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_19 = QFrame(self.frame_9)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_19)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.pb_Start = QPushButton(self.frame_19)
        self.pb_Start.setObjectName(u"pb_Start")
        self.pb_Start.setMaximumSize(QSize(1677215, 16777215))
        font2 = QFont()
        font2.setPointSize(36)
        self.pb_Start.setFont(font2)
        self.pb_Start.setCursor(QCursor(Qt.OpenHandCursor))
        self.pb_Start.setLayoutDirection(Qt.LeftToRight)
        self.pb_Start.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(209, 209, 209);\n"
"border-radius: 25px;\n"
"\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(149, 149, 149);")

        self.verticalLayout_14.addWidget(self.pb_Start)

        self.pb_Pause = QPushButton(self.frame_19)
        self.pb_Pause.setObjectName(u"pb_Pause")
        self.pb_Pause.setMaximumSize(QSize(16777215, 16777215))
        self.pb_Pause.setFont(font2)
        self.pb_Pause.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_Pause.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 25px;\n"
"\n"
"background-color: rgba(221, 135, 135, 1);\n"
"color: rgb(240, 240, 240);")

        self.verticalLayout_14.addWidget(self.pb_Pause)

        self.pb_Stop = QPushButton(self.frame_19)
        self.pb_Stop.setObjectName(u"pb_Stop")
        self.pb_Stop.setFont(font2)
        self.pb_Stop.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_Stop.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 25px;\n"
"\n"
"background-color:rgba(201, 67, 67, 1);\n"
"color: rgb(240, 240, 240);")

        self.verticalLayout_14.addWidget(self.pb_Stop)

        self.progBar_Battery = QProgressBar(self.frame_19)
        self.progBar_Battery.setObjectName(u"progBar_Battery")
        self.progBar_Battery.setMaximumSize(QSize(16777215, 40))
        self.progBar_Battery.setFont(font)
        self.progBar_Battery.setMouseTracking(False)
        self.progBar_Battery.setTabletTracking(True)
        self.progBar_Battery.setContextMenuPolicy(Qt.NoContextMenu)
        self.progBar_Battery.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.progBar_Battery.setValue(24)
        self.progBar_Battery.setInvertedAppearance(False)
        self.progBar_Battery.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_14.addWidget(self.progBar_Battery)


        self.verticalLayout_13.addWidget(self.frame_19)


        self.verticalLayout_10.addWidget(self.frame_9)


        self.verticalLayout_9.addWidget(self.frame_pb)


        self.horizontalLayout_2.addWidget(self.frame_StatCtrlPanel)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_subscript = QFrame(MainForm)
        self.frame_subscript.setObjectName(u"frame_subscript")
        self.frame_subscript.setMaximumSize(QSize(16777215, 50))
        self.frame_subscript.setStyleSheet(u"background-color: rgb(44, 44, 44);")
        self.frame_subscript.setFrameShape(QFrame.StyledPanel)
        self.frame_subscript.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_subscript)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_subscript = QLabel(self.frame_subscript)
        self.lb_subscript.setObjectName(u"lb_subscript")
        font3 = QFont()
        font3.setBold(False)
        self.lb_subscript.setFont(font3)
        self.lb_subscript.setStyleSheet(u"color: rgb(85, 255, 0);")
        self.lb_subscript.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lb_subscript)


        self.verticalLayout_2.addWidget(self.frame_subscript)


        self.retranslateUi(MainForm)

        QMetaObject.connectSlotsByName(MainForm)
    # setupUi

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QCoreApplication.translate("MainForm", u"Form", None))
        self.lb_LexxPluss.setText(QCoreApplication.translate("MainForm", u"LexxPluss 1.0", None))
        self.label.setText(QCoreApplication.translate("MainForm", u"Map", None))
        self.lb_Map.setText("")
        self.label_5.setText(QCoreApplication.translate("MainForm", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainForm", u"0.85", None))
        self.label_2.setText(QCoreApplication.translate("MainForm", u"STATUS", None))
        self.label_19.setText(QCoreApplication.translate("MainForm", u"ROBOT STATUS:", None))
        self.label_20.setText(QCoreApplication.translate("MainForm", u"Charging", None))
        self.label_16.setText(QCoreApplication.translate("MainForm", u"STATUS:", None))
        self.label_15.setText(QCoreApplication.translate("MainForm", u"Awaiting instructions", None))
        self.label_18.setText(QCoreApplication.translate("MainForm", u"TASKS:", None))
        self.label_17.setText(QCoreApplication.translate("MainForm", u"Awaiting instructions", None))
        self.lb_frontLeft.setText(QCoreApplication.translate("MainForm", u"FRONT_LEFT", None))
        self.lb_frontLeft_value.setText(QCoreApplication.translate("MainForm", u"0.018", None))
        self.lb_left.setText(QCoreApplication.translate("MainForm", u"LEFT", None))
        self.lb_left_value_2.setText(QCoreApplication.translate("MainForm", u"0.01", None))
        self.lb_right.setText(QCoreApplication.translate("MainForm", u"RIGHT", None))
        self.lb_right_value.setText(QCoreApplication.translate("MainForm", u"0.02", None))
        self.lb_rear_2.setText(QCoreApplication.translate("MainForm", u"REAR", None))
        self.lb_rear_2_value.setText(QCoreApplication.translate("MainForm", u"0.05", None))
        self.lb_sysLogs.setText(QCoreApplication.translate("MainForm", u"System Logs", None))
        self.lb_Logs.setText(QCoreApplication.translate("MainForm", u"The system log go in here.....", None))
        self.label_7.setText(QCoreApplication.translate("MainForm", u"Select execution order", None))
        self.label_21.setText(QCoreApplication.translate("MainForm", u"Forward motion", None))
        self.label_8.setText(QCoreApplication.translate("MainForm", u"Backward motion", None))
        self.comboBox.setCurrentText("")
        self.comboBox_2.setCurrentText("")
        self.pb_Start.setText(QCoreApplication.translate("MainForm", u"Start", None))
        self.pb_Pause.setText(QCoreApplication.translate("MainForm", u"Pause", None))
        self.pb_Stop.setText(QCoreApplication.translate("MainForm", u"Stop", None))
        self.lb_subscript.setText(QCoreApplication.translate("MainForm", u"Powered by Chizu Denki Co., Ltd.", None))
    # retranslateUi

