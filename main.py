from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os
from layout import*
from PIL import Image, ImageEnhance

class ImageProcessor:
    
    def __init__(self, filename = None,image = None, folder = None):
        self.image = image
        self.filename = filename
        self.folder = folder
    
    def LoadImage(self,filename):
        self.filename = filename
        file_path = os.path.join(workdir, filename)
        self.image = Image.open(file_path)
    
    def showImage(self, path):
        picture_LB.hide()
        pixmap = QPixmap(path)
        w, h = picture_LB.width(), picture_LB.height()
        pixmap = pixmap.scaled(w, h, Qt.KeepAspectRatio)
        picture_LB.setPixmap(pixmap)
        
        picture_LB.show

    def do_bw():
        self.image = self.image.convert('L')
        self.saveImage()
        path = os.path.join(workdir,self.folder,self.filename)
        self.showImage(path)

    def do_left():
        self.image = self.image.transpose(image.ROTATE_90)
        self.saveImage()
        path = os.path.join(workdir,self.folder,self.filename)
        self.showImage(path)

    def do_right():
        pass

    def do_mirror():
        self.image = self.image.transpose(image.FLIP_LEFT_RIGHT)
        self.saveImage()
        path = os.path.join(workdir,self.folder,self.filename)
        self.showImage(path)

    def saveImage():
        save_path = os.path.join(workdir,self.folder)
        if not os.path.exists(save_path) and not os.path.isdir(save_path):
            os.mkdir(save_path)
        im_path = os.path.join(save_path, self.filename)
        self.image.save(im_path)
    
    def do_contrast(self):
            self.image = ImageEnhance.Contrast(self.image)
            self.image.enhance(1.5)
            self.saveImage()
            path = os.path.join(workdir,self.folder,self.filename)
            self.showImage(path)

main_okoshko = QWidget()
main_okoshko.resize(1200,700)
main_okoshko.setWindowTitle('Easy Editor')
main_okoshko.setLayout(Lmain)

exteptions = ['.jfif','.png','.jpg',]
workdir = ""
imageProc = ImageProcessor(folder="Pythonimag")

def open_papka():
    global workdir
    spysok.clear()
    workdir = QFileDialog.getExistingDirectory()
#   spysok.addItems(os.listdir(workdir))
    felter(os.listdir(workdir))


def showChoosenImage():
    if spysok.currentItem():
        filename = spysok.currentItem().text()
        print(filename, 'jhfdffjfk;fkfhlhflhdsf') 
        print(workdir) 
        imageProc.LoadImage(filename)
        file_path = os.path.join(workdir, filename)
        print(file_path, 'jhfdffjfk;fkfhlhflhdsf')
        imageProc.showImage(file_path)


def felter(file_names):
    for i in file_names:
        for j in exteptions:
            if i.endswith(j):
                spysok.addItem(i)
  

knopka_papka.clicked.connect(open_papka)
spysok.currentRowChanged.connect(showChoosenImage)
knopka_chb.clicked.connect(imageProc.do_bw)
knopka_livo.clicked.connect(imageProc.do_left)
knopka_pravo.clicked.connect(imageProc.do_right)
knopka_rizkist.clicked.connect(imageProc.do_contrast)

main_okoshko.show()
app.exec_()