"""UNUSED FILE WILL BE DELETED LATER"""




import scipy.io.wavfile

sample_rate, signal2 = scipy.io.wavfile.read('temp1.wav')
print(sample_rate)

# D:\Zaky\CapstoneProject\ASR\conda-asrenv\lib\site-packages\PyQt4\pyuic4.bat -x MainWindow2.ui -o mainwindow_label.py

# #
# # if __name__ == "__main__":
# #     app = QApplication(sys.argv)
# #     MainWindow = QtWidgets.QMainWindow()
# #     ui = Ui_MainWindow()
# #     ui.setupUi(MainWindow)
# #     MainWindow.show()
# #     sys.exit(app.exec_())
#
# import pyaudio
# import wave
#
# CHUNK = 1024
# FORMAT = pyaudio.paInt16
# CHANNELS = 2
# RATE = 44100
# RECORD_SECONDS = 5
# WAVE_OUTPUT_FILENAME = "output.wav"
#
# p = pyaudio.PyAudio()
#
# stream = p.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK)
#
# print("* recording")
#
# frames = []
#
# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)
#
# print("* done recording")
#
# stream.stop_stream()
# stream.close()
# p.terminate()
#
# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()
