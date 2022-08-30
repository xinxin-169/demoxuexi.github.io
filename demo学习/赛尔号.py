from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from PyQt5.QtGui import QMouseEvent, QScreen, QGuiApplication, QDesktopServices
from PyQt5.QtCore import Qt, QProcess, QMetaType, QVariant, pyqtSignal, QJsonDocument, QUrl, QSettings
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

#必要依赖
from pycaw.pycaw import AudioUtilities
import os
saxWidget = QApplication()
saxWidget.setControl("{8856F961-340A-11D0-A96B-00C04FD705A2}")
saxWidget.setProperty("DisplayAlerts", False)
saxWidget.setProperty("DisplayScrollBars", True)
saxWidget.dynamicCall("Navigate(const QString&)",
                          "http://seer.61.com/play.shtml")  # 此处替换你的网页地址就可以，必须是服务器地址，本地服务也
