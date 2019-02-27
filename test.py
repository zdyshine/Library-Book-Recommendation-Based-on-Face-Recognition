import sys
import tempfile
import subprocess
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal

from mainwindow import Ui_MainWindow


class CloneThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self):
        QThread.__init__(self)
        self.git_url = ""

    # run method gets called when we start the thread
    def run(self):
        tmpdir = tempfile.mkdtemp()
        cmd = "git clone {0} {1}".format(self.git_url, tmpdir)
        subprocess.check_output(cmd.split())
        # git clone done, now inform the main thread with the output
        self.signal.emit(tmpdir)


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.setText("Git clone with Thread")
        # Here we are telling to call git_clone method when
        # someone clicks on the pushButton.
        self.pushButton.clicked.connect(self.git_clone)
        self.git_thread = CloneThread()  # This is the thread object
        # Connect the signal from the thread to the finished method
        self.git_thread.signal.connect(self.finished)

    def git_clone(self):
        self.git_thread.git_url = self.lineEdit.text()  # Get the git URL
        self.pushButton.setEnabled(False)  # Disables the pushButton
        self.textEdit.setText("Started git clone operation.")  # Updates the UI
        self.git_thread.start()  # Finally starts the thread

    def finished(self, result):
        self.textEdit.setText("Cloned at {0}".format(result))  # Show the output to the user
        self.pushButton.setEnabled(True)  # Enable the pushButton


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
