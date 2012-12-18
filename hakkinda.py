# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hakkinda.ui'
#
# Created: Wed Jun 22 15:08:05 2011
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 169)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 331, 81))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(290, 130, 101, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Hakkında", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Bu program Berat Alp Erbil tarafından yazılmıştır. \n"
" \n"
" Teşekkürler: \n"
" @fortran \n"
" @YVZ_61", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "LinFreeze 1.0", None, QtGui.QApplication.UnicodeUTF8))

app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
ui = Ui_Form()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())