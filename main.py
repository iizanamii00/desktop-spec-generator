from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import fetcher


class Ui_MainWindow(object):

    usecase = 'gaming'
    platform = 'intel'
    budget = 0
    cpuBudget = 0
    CPU = []
    OPString = 'CPU : '
    gpuBudget = 0
    GPU = []
    moboBudget = 0
    mobo = []
    ramBudget = 0
    ram = []
    caseBudget = 0
    case = []
    psuBudget = 0
    psu = []
    ssdBudget = 0
    ssd = []
    hddBudget = 0
    hdd = []


    def allocator(self):
        if self.budget == 30000:
            self.cpuBudget = self.budget * 0.3
            self.gpuBudget = 0
            self.moboBudget = self.budget * 0.2
            self.ramBudget = self.budget * 0.1
            self.caseBudget = self.budget * 0.1
            self.psuBudget = self.budget * 0.1
            self.ssdBudget = self.budget * 0.1
            self.hddBudget = self.budget * 0.1
            return

        elif self.usecase == 'gaming':
            self.cpuBudget = self.budget * 0.2
            self.gpuBudget = self.budget * 0.4
            self.moboBudget = self.budget * 0.1
            self.ramBudget = self.budget * 0.05
            self.caseBudget = self.budget * 0.1
            self.psuBudget = self.budget * 0.05
            self.ssdBudget = self.budget * 0.05
            self.hddBudget = self.budget * 0.05

        elif self.usecase == 'video':
            self.cpuBudget = self.budget * 0.4
            self.gpuBudget = self.budget * 0.2
            self.moboBudget = self.budget * 0.1
            self.ramBudget = self.budget * 0.05
            self.caseBudget = self.budget * 0.1
            self.psuBudget = self.budget * 0.05
            self.ssdBudget = self.budget * 0.05
            self.hddBudget = self.budget * 0.05

        elif self.usecase == 'media':
            self.cpuBudget = self.budget * 0.2
            self.gpuBudget = self.budget * 0.2
            self.moboBudget = self.budget * 0.1
            self.ramBudget = self.budget * 0.15
            self.caseBudget = self.budget * 0.15
            self.psuBudget = self.budget * 0.05
            self.ssdBudget = self.budget * 0.1
            self.hddBudget = self.budget * 0.05

        elif self.usecase == 'office':
            self.cpuBudget = self.budget * 0.3
            self.gpuBudget = self.budget * 0.1
            self.moboBudget = self.budget * 0.1
            self.ramBudget = self.budget * 0.15
            self.caseBudget = self.budget * 0.1
            self.psuBudget = self.budget * 0.05
            self.ssdBudget = self.budget * 0.15
            self.hddBudget = self.budget * 0.05

        print(self.caseBudget, self.cpuBudget, self.gpuBudget, self.moboBudget, self.hddBudget, self.psuBudget,
              self.ssdBudget, self.ramBudget)


    def usecase1(self):
        self.usecase = 'gaming'

    def usecase2(self):
        self.usecase = 'video'

    def usecase3(self):
        self.usecase = 'media'

    def usecase4(self):
        self.usecase = 'office'

    def platform1(self):
        self.platform = 'Intel'

    def platform2(self):
        self.platform = 'AMD'

    def budget30(self):
        self.budget = 30000

    def budget50(self):
        self.budget = 50000

    def budget75(self):
        self.budget = 75000

    def budget100(self):
        self.budget = 100000

    def budget150(self):
        self.budget = 150000


    def mainfunction(self):

        self.allocator()

        self.CPU = fetcher.getCPU(self.platform,self.cpuBudget)
        print(self.CPU)
        self.OPString = self.OPString + str(self.CPU[2]) + ' ' + str(self.CPU[0]) + '\nGPU : '
        self.output.setText(self.OPString)


        self.GPU = fetcher.getGPU(self.gpuBudget)
        print(self.GPU)
        self.OPString = self.OPString + str(self.GPU[1]) + ' ' + str(self.GPU[0]) + '\nMotherboard : '
        self.output.setText(self.OPString)


        self.mobo = fetcher.getMobo(self.CPU[1], self.moboBudget)
        print(self.mobo)
        self.OPString = self.OPString + str(self.mobo[1]) + ' ' + str(self.mobo[0]) + '\nRAM : '
        self.output.setText(self.OPString)

        self.ram = fetcher.getRAM(self.ramBudget)
        print(self.ram)
        self.OPString = self.OPString + str(self.ram[4]) + ' ' + str(self.ram[0]) + '\nCase : '
        self.output.setText(self.OPString)

        self.case = fetcher.getCase(self.mobo[5],self.caseBudget)
        print(self.case)
        self.OPString = self.OPString + str(self.case[1]) + ' ' + str(self.case[0]) + '\nPSU : '
        self.output.setText(self.OPString)

        self.psu = fetcher.getPSU(self.psuBudget)
        print(self.psu)
        self.OPString = self.OPString + str(self.psu[1]) + ' ' + str(self.psu[0]) + '\nSSD : '
        self.output.setText(self.OPString)

        self.ssd = fetcher.getSSD(self.ssdBudget)
        print(self.ssd)
        self.OPString = self.OPString + str(self.ssd[1]) + ' ' + str(self.psu[0]) + '\nHDD : '
        self.output.setText(self.OPString)

        self.hdd = fetcher.getHDD(self.hddBudget)
        print(self.hdd)
        self.OPString = self.OPString + str(self.hdd[1]) + ' ' + str(self.hdd[0])
        self.output.setText(self.OPString)
        self.OPString = 'CPU : '

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1115, 850)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gaming = QtWidgets.QPushButton(self.centralwidget)
        self.gaming.setGeometry(QtCore.QRect(40, 110, 241, 71))
        self.gaming.setObjectName("gaming")
        self.gaming.setStyleSheet("QPushButton"
                                  "{"
                                  "background-color : lightblue;"
                                  "}"
                                  "QPushButton::pressed"
                                  "{"
                                  "background-color : green;"
                                  "}"
                                  )
        self.gaming.clicked.connect(self.usecase1)
        self.video = QtWidgets.QPushButton(self.centralwidget)
        self.video.setGeometry(QtCore.QRect(300, 110, 241, 71))
        self.video.setObjectName("video")
        self.video.setStyleSheet("QPushButton"
                                 "{"
                                 "background-color : lightblue;"
                                 "}"
                                 "QPushButton::pressed"
                                 "{"
                                 "background-color : green;"
                                 "}"
                                 )
        self.video.clicked.connect(self.usecase2)
        self.media = QtWidgets.QPushButton(self.centralwidget)
        self.media.setGeometry(QtCore.QRect(560, 110, 241, 71))
        self.media.setObjectName("media")
        self.media.setStyleSheet("QPushButton"
                                 "{"
                                 "background-color : lightblue;"
                                 "}"
                                 "QPushButton::pressed"
                                 "{"
                                 "background-color : green;"
                                 "}"
                                 )
        self.media.clicked.connect(self.usecase3)
        self.office = QtWidgets.QPushButton(self.centralwidget)
        self.office.setGeometry(QtCore.QRect(820, 110, 241, 71))
        self.office.setObjectName("office")
        self.office.setStyleSheet("QPushButton"
                                  "{"
                                  "background-color : lightblue;"
                                  "}"
                                  "QPushButton::pressed"
                                  "{"
                                  "background-color : green;"
                                  "}"
                                  )
        self.office.clicked.connect(self.usecase4)
        self.intel = QtWidgets.QPushButton(self.centralwidget)
        self.intel.setGeometry(QtCore.QRect(210, 330, 271, 81))
        self.intel.setObjectName("intel")
        self.intel.setStyleSheet("QPushButton"
                                 "{"
                                 "background-color : lightblue;"
                                 "}"
                                 "QPushButton::pressed"
                                 "{"
                                 "background-color : green;"
                                 "}"
                                 )
        self.intel.clicked.connect(self.platform1)
        self.amd = QtWidgets.QPushButton(self.centralwidget)
        self.amd.setGeometry(QtCore.QRect(650, 330, 271, 81))
        self.amd.setObjectName("amd")
        self.amd.setStyleSheet("QPushButton"
                               "{"
                               "background-color : lightblue;"
                               "}"
                               "QPushButton::pressed"
                               "{"
                               "background-color : green;"
                               "}"
                               )
        self.amd.clicked.connect(self.platform2)
        self.platform = QtWidgets.QTextBrowser(self.centralwidget)
        self.platform.setGeometry(QtCore.QRect(20, 220, 1081, 81))
        self.platform.setObjectName("platform")
        self.budget = QtWidgets.QTextBrowser(self.centralwidget)
        self.budget.setGeometry(QtCore.QRect(20, 440, 1081, 81))
        self.budget.setObjectName("budget")
        self.usecase = QtWidgets.QTextBrowser(self.centralwidget)
        self.usecase.setGeometry(QtCore.QRect(20, 10, 1081, 81))
        self.usecase.setObjectName("usecase")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(470, 630, 171, 61))
        self.submit.setObjectName("submit")
        self.submit.setStyleSheet("QPushButton"
                                  "{"
                                  "background-color : lightblue;"
                                  "}"
                                  "QPushButton::pressed"
                                  "{"
                                  "background-color : green;"
                                  "}"
                                  )
        self.submit.clicked.connect(self.mainfunction)
        self.intel_2 = QtWidgets.QPushButton(self.centralwidget)
        self.intel_2.setGeometry(QtCore.QRect(30, 530, 181, 61))
        self.intel_2.setObjectName("intel_2")
        self.intel_2.setStyleSheet("QPushButton"
                                   "{"
                                   "background-color : lightblue;"
                                   "}"
                                   "QPushButton::pressed"
                                   "{"
                                   "background-color : green;"
                                   "}"
                                   )
        self.intel_2.clicked.connect(self.budget30)
        self.intel_3 = QtWidgets.QPushButton(self.centralwidget)
        self.intel_3.setGeometry(QtCore.QRect(240, 530, 181, 61))
        self.intel_3.setObjectName("intel_3")
        self.intel_3.setStyleSheet("QPushButton"
                                   "{"
                                   "background-color : lightblue;"
                                   "}"
                                   "QPushButton::pressed"
                                   "{"
                                   "background-color : green;"
                                   "}"
                                   )
        self.intel_3.clicked.connect(self.budget50)
        self.intel_4 = QtWidgets.QPushButton(self.centralwidget)
        self.intel_4.setGeometry(QtCore.QRect(460, 530, 181, 61))
        self.intel_4.setObjectName("intel_4")
        self.intel_4.setStyleSheet("QPushButton"
                                   "{"
                                   "background-color : lightblue;"
                                   "}"
                                   "QPushButton::pressed"
                                   "{"
                                   "background-color : green;"
                                   "}"
                                   )
        self.intel_4.clicked.connect(self.budget75)
        self.intel_5 = QtWidgets.QPushButton(self.centralwidget)
        self.intel_5.setGeometry(QtCore.QRect(680, 530, 181, 61))
        self.intel_5.setObjectName("intel_5")
        self.intel_5.setStyleSheet("QPushButton"
                                   "{"
                                   "background-color : lightblue;"
                                   "}"
                                   "QPushButton::pressed"
                                   "{"
                                   "background-color : green;"
                                   "}"
                                   )
        self.intel_5.clicked.connect(self.budget100)
        self.intel_6 = QtWidgets.QPushButton(self.centralwidget)
        self.intel_6.setGeometry(QtCore.QRect(910, 530, 181, 61))
        self.intel_6.setObjectName("intel_6")
        self.intel_6.setStyleSheet("QPushButton"
                                   "{"
                                   "background-color : lightblue;"
                                   "}"
                                   "QPushButton::pressed"
                                   "{"
                                   "background-color : green;"
                                   "}"
                                   )
        self.intel_6.clicked.connect(self.budget150)
        self.output = QtWidgets.QTextBrowser(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(20, 700, 1071, 121))
        self.output.setObjectName("output")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Desktop Spec Generator"))
        self.gaming.setText(_translate("MainWindow", "Gaming"))
        self.video.setText(_translate("MainWindow", "Video/Photo editing"))
        self.media.setText(_translate("MainWindow", "Multimedia Consumption"))
        self.office.setText(_translate("MainWindow", "Office Work"))
        self.intel.setText(_translate("MainWindow", "Intel"))
        self.amd.setText(_translate("MainWindow", "AMD"))
        self.platform.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Select a platform</span></p></body></html>"))
        self.budget.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Select a budget </span></p></body></html>"))
        self.usecase.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Select a usecase</span></p></body></html>"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.intel_2.setText(_translate("MainWindow", "30,000"))
        self.intel_3.setText(_translate("MainWindow", "50,000"))
        self.intel_4.setText(_translate("MainWindow", "75,000"))
        self.intel_5.setText(_translate("MainWindow", "1,00,000"))
        self.intel_6.setText(_translate("MainWindow", "1,50,000"))
        self.output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">CPU : </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GPU : </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Motherboard : </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">RAM : </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Case : </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PSU : </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">SSD : </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">HDD : </p></body></html>"))




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())


