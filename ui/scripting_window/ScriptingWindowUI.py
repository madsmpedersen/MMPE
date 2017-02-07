# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mmpe\ui\scripting_window\ScriptingWindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(624, 526)
        Form.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.menuBar = QtWidgets.QMenuBar(Form)
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuRun = QtWidgets.QMenu(self.menuBar)
        self.menuRun.setObjectName("menuRun")
        self.gridLayout_2.addWidget(self.menuBar, 0, 0, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.textEditOutput = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.textEditOutput.setFont(font)
        self.textEditOutput.setAcceptDrops(False)
        self.textEditOutput.setReadOnly(True)
        self.textEditOutput.setObjectName("textEditOutput")
        self.verticalLayout_3.addWidget(self.textEditOutput)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.webView = QtWebKitWidgets.QWebView(self.splitter_2)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.gridLayout_2.addWidget(self.splitter_2, 1, 0, 1, 1)
        self.labelLineNumber = QtWidgets.QLabel(Form)
        self.labelLineNumber.setText("")
        self.labelLineNumber.setObjectName("labelLineNumber")
        self.gridLayout_2.addWidget(self.labelLineNumber, 2, 0, 1, 1)
        self.actionSaveAs = QtWidgets.QAction(Form)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionRunScript = QtWidgets.QAction(Form)
        self.actionRunScript.setObjectName("actionRunScript")
        self.actionSave = QtWidgets.QAction(Form)
        self.actionSave.setObjectName("actionSave")
        self.actionNew = QtWidgets.QAction(Form)
        self.actionNew.setObjectName("actionNew")
        self.actionImportPlugin = QtWidgets.QAction(Form)
        self.actionImportPlugin.setEnabled(False)
        self.actionImportPlugin.setVisible(False)
        self.actionImportPlugin.setObjectName("actionImportPlugin")
        self.actionExportPlugin = QtWidgets.QAction(Form)
        self.actionExportPlugin.setObjectName("actionExportPlugin")
        self.actionOpen = QtWidgets.QAction(Form)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionImportPlugin)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExportPlugin)
        self.menuRun.addAction(self.actionRunScript)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuRun.menuAction())

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Scripting"))
        self.menuFile.setTitle(_translate("Form", "File"))
        self.menuRun.setTitle(_translate("Form", "Run"))
        self.label_2.setText(_translate("Form", "Output"))
        self.textEditOutput.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.actionSaveAs.setText(_translate("Form", "Save as ..."))
        self.actionRunScript.setText(_translate("Form", "Run script"))
        self.actionRunScript.setShortcut(_translate("Form", "F5"))
        self.actionSave.setText(_translate("Form", "Save"))
        self.actionSave.setShortcut(_translate("Form", "Ctrl+S"))
        self.actionNew.setText(_translate("Form", "New"))
        self.actionNew.setShortcut(_translate("Form", "Ctrl+N"))
        self.actionImportPlugin.setText(_translate("Form", "Import plugin"))
        self.actionExportPlugin.setText(_translate("Form", "Export as plugin"))
        self.actionOpen.setText(_translate("Form", "Open"))
        self.actionOpen.setToolTip(_translate("Form", "Open script"))
        self.actionOpen.setShortcut(_translate("Form", "Ctrl+O"))

from PyQt5 import QtWebKitWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

