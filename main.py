from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QMainWindow, QApplication
from pygame import mixer
import sys
import os
from mutagen.mp3 import MP3

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        mixer.init()

    # Main Window
        self.setObjectName("MainWindow")
        self.resize(801, 610)
        self.setWindowTitle('DmMusic')
        self.setWindowIcon(QtGui.QIcon('main.png'))
        self.setFixedSize(self.size())
        image = QtGui.QImage("fon4.png")
        sImage = image.scaled(QtCore.QSize(801, 610))
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(sImage))
        self.setPalette(palette)


    # music slider
        self.horizontalSlider = QtWidgets.QSlider(self)
        self.horizontalSlider.setGeometry(QtCore.QRect(300, 360, 401, 21))
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.valueChanged.connect(self.slider_value)
        self.horizontalSlider.setStyleSheet("""
                    QSlider{
                        background: 0;
                    }
                    QSlider::groove:horizontal {  
                        height: 10px;
                        margin: 0px;
                        border-radius: 5px;
                        background: white;
                    }
                    QSlider::handle:horizontal {
                        background: #FDE910;
                        border: 3px solid #FDE910;
                        width: 6px;
                        margin: -2px 0; 
                        border-radius: 6px;
                    }
                    QSlider::sub-page:qlineargradient {
                        background:  #F80000;
                        border-radius: 3px;
                    }
                """)

    # playlist
        self.play_list_2 = QtWidgets.QListWidget(self)
        self.play_list_2.setGeometry(QtCore.QRect(10, 40, 256, 561))
        self.play_list_2.setObjectName("play_list_2")
        self.play_list_2.itemClicked.connect(self.item_click)
        self.play_list_2.setStyleSheet("QListWidget {background-color: rgba(47, 4, 4, 0.69); }")

    # widget for photo
        self.music_photo = QtWidgets.QLabel(self)
        self.music_photo.setGeometry(QtCore.QRect(300, 40, 401, 291))
        self.music_photo.setObjectName("music_photo")
        image = "000001.png"
        self.music_photo.setPixmap(QtGui.QPixmap(image))
        self.music_photo.setStyleSheet("border: 1px solid black;")
        self.music_photo.setScaledContents(True)

    # button back
        self.back = QtWidgets.QPushButton(self)
        self.back.setGeometry(QtCore.QRect(390, 390, 61, 61))
        self.back.setObjectName("Back")
        self.back.clicked.connect(self.Back)
        self.back.setIconSize(QtCore.QSize(105, 105))
        self.back.setIcon(QtGui.QIcon('back.png'))
        self.back.setStyleSheet("QPushButton {background-color: 0; color: White; border-radius: 18px;}"
                              "QPushButton:pressed {background-color:rgb(31,101,163) ; }")

    # button play
        self.play = QtWidgets.QPushButton(self)
        self.play.setGeometry(QtCore.QRect(470, 390, 61, 61))
        self.play.setObjectName("Play")
        self.play.setIcon(QtGui.QIcon('play.png'))
        self.play.setIconSize(QtCore.QSize(105, 105))
        self.play.clicked.connect(self.Play)
        self.play.setStyleSheet("QPushButton {background-color: 0; color: White; border-radius: 18px;}"
                                "QPushButton:pressed {background-color:rgb(31,101,163) ; }")
    # button onwards
        self.onwards = QtWidgets.QPushButton(self)
        self.onwards.setGeometry(QtCore.QRect(550, 390, 61, 61))
        self.onwards.setObjectName("onwards")
        self.onwards.clicked.connect(self.Onward)
        self.onwards.setIconSize(QtCore.QSize(105, 105))
        self.onwards.setIcon(QtGui.QIcon('onward.png'))
        self.onwards.setStyleSheet("QPushButton {background-color: 0; color: White; border-radius: 18px;}"
                                "QPushButton:pressed {background-color:rgb(31,101,163) ; }")
    # button open file
        self.openfile = QtWidgets.QPushButton(self)
        self.openfile.setGeometry(QtCore.QRect(460, 10, 75, 23))
        self.openfile.setObjectName("openfile")
        self.openfile.setText("Open File")
        self.openfile.clicked.connect(self.OpenFile)
        self.openfile.setStyleSheet("QPushButton {background-color: rgb(31,101,163); color: White; border-radius: 5px;}"
                                "QPushButton:pressed {background-color:rgb(31,101,163) ; }")

    # label for text 'My music'
        self.text_play = QtWidgets.QLabel(self)
        self.text_play.setGeometry(QtCore.QRect(85, 15, 100, 20))
        self.text_play.setFont(QtGui.QFont('Arial', 15))
        self.text_play.setTextFormat(QtCore.Qt.AutoText)
        self.text_play.setObjectName("text_play")
        self.text_play.setText('MY MUSIC')
        self.text_play.setStyleSheet('QLabel {background-color: 0; color: white;}')

    # volume: slider
        self.volume_slider = QtWidgets.QSlider(self)
        self.volume_slider.setGeometry(QtCore.QRect(330, 480, 350, 20))
        self.volume_slider.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setProperty("value", 50)
        self.volume_slider.setOrientation(QtCore.Qt.Horizontal)
        self.volume_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.volume_slider.setObjectName("volume_slider")
        self.volume_slider.setTickInterval(10)
        self.volume_slider.valueChanged.connect(self.ChangedValue)
        self.volume_slider.setStyleSheet("""
                           QSlider{
                               background: 0;
                           }
                           QSlider::groove:horizontal {  
                               height: 10px;
                               margin: 0px;
                               border-radius: 5px;
                               background: white;
                           }
                           QSlider::handle:horizontal {
                               background: #FDE910;
                               border: 3px solid #FDE910;
                               width: 6px;
                               margin: -2px 0; 
                               border-radius: 6px;
                           }
                           QSlider::sub-page:qlineargradient {
                               background:  #F80000;
                               border-radius: 3px;
                           }
                       """)

    # volume: text = 0%
        self.volume_0 = QtWidgets.QLabel(self)
        self.volume_0.setGeometry(QtCore.QRect(330, 500, 50, 10))
        self.volume_0.setObjectName("label0")
        self.volume_0.setText("0%")
        self.volume_0.setStyleSheet('QLabel {background-color: 0; color: white;}')
    # volume: text = 50%
        self.volume_50 = QtWidgets.QLabel(self)
        self.volume_50.setGeometry(QtCore.QRect(495, 500, 50, 15))
        self.volume_50.setObjectName("label50")
        self.volume_50.setText("50%")
        self.volume_50.setStyleSheet('QLabel {background-color: 0; color: white;}')
    # volume: text = 100%
        self.volume_100 = QtWidgets.QLabel(self)
        self.volume_100.setGeometry(QtCore.QRect(660, 500, 50, 10))
        self.volume_100.setObjectName("label100")
        self.volume_100.setText("100%")
        self.volume_100.setStyleSheet('QLabel {background-color: 0; color: white;}')
    # volume: text = volume
        self.text_volume = QtWidgets.QLabel(self)
        self.text_volume.setGeometry(QtCore.QRect(485, 465, 47, 13))
        self.text_volume.setObjectName("label_volume")
        self.text_volume.setText("Volume")
        self.text_volume.setStyleSheet('QLabel {background-color: 0; color: white;}')
        self.text_volume.setFont(QtGui.QFont('Arial', 9))
    # music name
        self.musicname = QtWidgets.QLabel(self)
        self.musicname.setGeometry(QtCore.QRect(395, 340, 261, 16))
        self.musicname.setObjectName("musicname")
        self.musicname.setFont(QtGui.QFont('Arial', 10))
        self.musicname.setStyleSheet('QLabel {color: white;}')


    # file selection function
    def OpenFile(self):
        self.filepath = QtWidgets.QFileDialog.getOpenFileName(self, 'open file')[0]
        self.filename = os.path.basename(self.filepath)
        with open('PlayList.txt', 'a') as file:
            file.write(self.filepath + '\n')
        self.play_list_2.addItem(self.filename.strip())

    #
    def item_click(self):
        self.horizontalSlider.setSliderPosition(0)
        self.tmr0 = QtCore.QTimer()
        self.tmr0.timeout.connect(self.on_timer)
        self.tmr0.start(1000)
        self.tmr0.stop()
        self.item_name = self.play_list_2.currentItem().text()
        self.musicname.setText(self.item_name)
        self.string = 0
        with open('PlayList.txt', 'r') as file:
            for line in file:
                self.string = self.string + 1
                if self.item_name in line:
                    self.music_path = line
                    break
        self.play.clicked.connect(self.Play)

    # play function
    def Play(self):
        self.tmr0.start()
        mixer.music.load(self.music_path.strip())
        self.audio_time = MP3(self.music_path.strip()).info.length
        self.music_slider_create(round(self.audio_time))
        mixer.music.play()
        self.play.deleteLater()
        self.Pause = QtWidgets.QPushButton(self)
        self.Pause.setGeometry(QtCore.QRect(470, 390, 61, 61))
        self.Pause.setObjectName("PlayPause")
        self.Pause.setIcon(QtGui.QIcon('pause.png'))
        self.Pause.setIconSize(QtCore.QSize(105, 105))
        self.Pause.setStyleSheet("QPushButton {background-color: 0; color: White; border-radius: 18px;}"
                                "QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.Pause.show()
        self.Pause.clicked.connect(self.paus)

    # unpause function
    def unpaus(self):
        mixer.music.unpause()
        self.tmr0.start()
        self.play.deleteLater()
        self.Pause = QtWidgets.QPushButton(self)
        self.Pause.setGeometry(QtCore.QRect(470, 390, 61, 61))
        self.Pause.setObjectName("PlayPause")
        self.Pause.setIcon(QtGui.QIcon('pause.png'))
        self.Pause.setIconSize(QtCore.QSize(105, 105))
        self.Pause.setStyleSheet("QPushButton {background-color: 0; color: White; border-radius: 18px;}"
        "QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.Pause.clicked.connect(self.paus)

    # pause function
    def paus(self):
        self.Pause.deleteLater()
        self.tmr0.stop()
        mixer.music.pause()
        self.Pause.deleteLater()
        self.play = QtWidgets.QPushButton(self)
        self.play.setGeometry(QtCore.QRect(470, 390, 61, 61))
        self.play.setObjectName("Play")
        self.play.setIcon(QtGui.QIcon('play.png'))
        self.play.setIconSize(QtCore.QSize(105, 105))
        self.play.setStyleSheet("QPushButton {background-color: 0; color: White; border-radius: 18px;}"
                                "QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.play.show()
        self.play.clicked.connect(self.unpaus)

    # get volume slider value
    def ChangedValue(self):
        size = self.volume_slider.value()
        size = size / 100
        mixer.music.set_volume(size)
    # music time
    def playlist_download(self):
        with open('PlayList.txt', 'r') as file:
            for line in file:
                self.play_list_2.addItem(os.path.basename(line).strip())
                self.play_list_2.setStyleSheet('color: white; background-color: rgba(47, 4, 4, 0.69);')
                self.play_list_2.setFont(QtGui.QFont('Arial', 10))

    #buttron back
    def Back(self):
        with open('PlayList.txt', 'r') as file:
            lines = file.readlines()
            count = 0
            for line in lines:
                if line == self.music_path:
                    self.music_path = lines[count - 1]
                    filename = os.path.basename(self.music_path)
                    break
                else:
                    count += 1
        mixer.music.stop()
        mixer.music.load(self.music_path.strip())
        self.musicname.setText(filename.strip())
        self.audio_time = MP3(self.music_path.strip()).info.length
        self.music_slider_create(round(self.audio_time))
        mixer.music.stop()

    #button onwerds
    def Onward(self):
        with open('PlayList.txt', 'r') as file:
            lines = file.readlines()
            count = 0
            for line in lines:
                if line == self.music_path:
                    self.music_path = lines[count + 1]
                    filename = os.path.basename(self.music_path)
                    break
                else:
                    count += 1
        mixer.music.stop()
        mixer.music.load(self.music_path.strip())
        self.musicname.setText(filename.strip())
        self.audio_time = MP3(self.music_path.strip()).info.length
        self.music_slider_create(round(self.audio_time))
        mixer.music.stop()

    def music_slider_create(self, music_time):
        self.horizontalSlider.setMaximum(music_time)
        self.horizontalSlider.setSliderPosition(0)

    def slider_value(self):
        size = self.horizontalSlider.value()
        mixer.music.play(loops=0, start=size)

    def on_timer(self):
        val = self.horizontalSlider.value()
        val += 1
        self.horizontalSlider.setValue(val)

def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    window.playlist_download()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()

