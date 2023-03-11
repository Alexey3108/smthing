from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QListWidget, QVBoxLayout, QHBoxLayout

app = QApplication([])

Lmain = QHBoxLayout()
L1 = QHBoxLayout()
L2 = QVBoxLayout()
L3 = QVBoxLayout()

picture_LB = QLabel('картинка')
spysok = QListWidget()
knopka_papka = QPushButton('выбор папки')
knopka_livo = QPushButton('влево')
knopka_pravo = QPushButton('вправо')
knopka_dserkalo = QPushButton('зеркало')
knopka_rizkist = QPushButton('резкость')
knopka_chb = QPushButton('Ч/б')

L2.addWidget(knopka_papka)
L2.addWidget(spysok)
L1.addWidget(knopka_livo)
L1.addWidget(knopka_pravo)
L1.addWidget(knopka_dserkalo)
L1.addWidget(knopka_rizkist)
L1.addWidget(knopka_chb)
L3.addWidget(picture_LB)

Lmain.addLayout(L2)
Lmain.addLayout(L3,stretch=3)
L3.addLayout(L1)
