import sys, time
import traceback

from micstream import Streaming
from PyQt4 import QtGui, uic

from PyQt4.QtCore import *

qtCreatorFile = "MainWindow2.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class Start(QRunnable):
    '''
    Worker thread
    '''

    def __init__(self, fn, *args, **kwargs):
        super(Start, self).__init__()

        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.stream = Streaming()

        self.pushButtonStart.clicked.connect(self.mulai)
        self.pushButtonStop.clicked.connect(self.stop)
        self.progressBar.setValue(0)

        # Set the threads
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.timer = QTimer()

    def progress_fn(self, n):
        print("%d%% done" % n)

    def thread_complete(self):
        print("THREAD COMPLETE!")
        self.progressBar.setRange(0, 1)

    def check_button(self, button):
        if button.isDown():
            print("STOP IS CLICKED")
            state_button = True
        elif not button.isDown():
            state_button = False
        return state_button

    def transcribe(self):
        stateStop = self.check_button(self.pushButtonStop)
        print("State button stop: ", stateStop)

        while not stateStop:
            self.label.setText("Say a number")
            signal = self.stream.record()
            self.progressBar.setRange(0, 0)
            self.label.setText("Processing...")
            response = self.stream.listening(signal)
            print("Your response: ")

            if response == "nol":
                new_resp = response[0] + ""
            elif response == "satu":
                new_resp = response[0] + ""
            elif response == "dua":
                new_resp = response[0] + ""
                # self.textEdit.setText(str(response) + " ")
            elif response == "tiga":
                new_resp = response[0] + ""
                # self.textEdit.setText(str(response) + " ")
            elif response == "empat":
                new_resp = response[0] + ""
                # self.textEdit.setText(str(response) + " ")
            elif response == "lima":
                new_resp = response[0] + ""
                # self.textEdit.setText(str(response) + " ")
            elif response == "enam":
                new_resp = response[0] + ""
                # self.textEdit.setText(str(response) + " ")
            elif response == "tujuh":
                new_resp = response[0] + ""
                # self.textEdit.setText(str(response) + " ")
            elif response == "delapan":
                new_resp = response[0] + ""
                # self.textEdit.setText(str(response) + " ")
            elif response == "sembilan":
                new_resp = response[0] + ""
                # self.textEdit.setText(str(response) + " ")
            elif response == "unknown":
                new_resp = response[0] + ""
                # self.label.setText("Unknown voice, please try again")
                time.sleep(1)
            print("new resp: ", new_resp)
            self.label_2.setText(new_resp)
            stateStop = self.check_button(self.pushButtonStop)
            print("State button stop: ", stateStop)

        print("STOP THE PROCESS")

    def mulai(self):
        start = Start(self.transcribe)

        start.signals.finished.connect(self.thread_complete)
        start.signals.progress.connect(self.progress_fn)

        # Execute
        self.threadpool.start(start)

    def stop(self):
        self.label.setText("Stop Processing..")
        self.progressBar.setRange(0, 1)
        self.check_button(self.pushButtonStop)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = MyApp()
    form.show()
    sys.exit(app.exec_())
