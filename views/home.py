# pyQT5
import os
import traceback
import logging
import cv2
from PyQt5.QtGui import QCursor, QMovie, QPixmap, QImage
from PyQt5.QtWidgets import (QLabel, QFileDialog, QSpacerItem, QCheckBox, QHBoxLayout, QPushButton, QWidget,
                             QSizePolicy, QFormLayout, QLineEdit, QColorDialog, QComboBox, QProgressBar, QVBoxLayout)
from PyQt5.QtCore import Qt, QByteArray, QPropertyAnimation, QAbstractAnimation, QVariantAnimation
# general
from pathlib import Path
from functools import partial
# utils
from globals import UNIT_OPS, WORKFLOWS, MAX_DIRS_PRUNE, UNIT_PX_SCALARS, DEFAULT_OUTPUT_DIR, PROG_COLOR_1, PROG_COLOR_2
from typings import FileType
from utils import get_complimentary_color

HEADER = "Synapse and Vescile Offset Analysis"
DESC = "Upload all files, and click \"Start\" to begin!"

class HomePage(QWidget):
    """
    MAIN PAGE
    ________________
    @start: begins running selected workflows and display all subpages
    """
    def __init__(self, start: partial):
        super().__init__()
        self.folder_count = 0
        self.run_idx = 0
        # init layout
        layout = QFormLayout()
        # header
        header = QLabel(HEADER)
        header.setStyleSheet("font-size: 24px; font-weight: bold; padding-top: 8px; ")
        layout.addRow(header)
        desc = QLabel(DESC)
        desc.setStyleSheet("font-size: 17px; font-weight: 400; padding-top: 3px; padding-bottom: 10px;")
        desc.setWordWrap(True)
        layout.addRow(desc)
        # upload header
        self.upload_header = QLabel("Select Input & Output")
        # file btns widget
        h_bl = QHBoxLayout()
        h_bl.addWidget(self.upload_header)
        layout.addRow(h_bl)
        # img btn
        img_btn = QPushButton('Set Synapse Folder', self)
        img_btn.setCursor(QCursor(Qt.PointingHandCursor))
        img_btn.setToolTip('Must be folder of .STL format files...')
        img_btn.clicked.connect(partial(self.open_file_picker, FileType.SYNPASE))
        # img input
        self.img_le = QLineEdit()
        self.img_le.setPlaceholderText("None Selected (Folder of STL Files)") 
        # add img row
        layout.addRow(img_btn, self.img_le)
        # mask btn
        mask_btn = QPushButton('Set Vesicle Folder', self)
        mask_btn.setCursor(QCursor(Qt.PointingHandCursor))
        mask_btn.setToolTip('Must be folder of .STL format files...')
        mask_btn.clicked.connect(partial(self.open_file_picker,  FileType.VESICLE))
        # mask input
        self.mask_le = QLineEdit()
        self.mask_le.setPlaceholderText("None Selected (Folder of STL Files)")
        # add mask row
        layout.addRow(mask_btn, self.mask_le)
        # csv btn
        csv_btn = QPushButton('Set Pairing CSV', self)
        csv_btn.setCursor(QCursor(Qt.PointingHandCursor))
        csv_btn.setToolTip('Synapse and Vesicle Paits. CSV must have synLabel and vesLabel columns with no spaces.')
        csv_btn.clicked.connect(partial(self.open_file_picker, FileType.CSV))
        # csv input
        self.csv_le = QLineEdit()
        self.csv_le.setPlaceholderText("None Selected (CSV)")
        
        self.img_le.setText("C:/Users/Arman/Downloads/SD3 5/Synapse Meshes")
        self.mask_le.setText("C:/Users/Arman/Downloads/SD3 5/Vesicle Meshes")
        self.csv_le.setText("C:/Users/Arman/Downloads/SD3_5_synVesPairsFromMesh.csv")
        
        # add csv row
        layout.addRow(csv_btn, self.csv_le)

        spacer = QSpacerItem(15, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        # TODO: output folder header
        # workflows_header = QLabel("Output Folder")
        # layout.addRow(workflows_header)
        # output folder btn
        out_btn = QPushButton('Set Output Folder', self)
        out_btn.setCursor(QCursor(Qt.PointingHandCursor))
        out_btn.clicked.connect(partial(self.open_output_folder_picker))
        # output folder input
        self.output_dir_le = QLineEdit()
        self.output_dir_le.setPlaceholderText(DEFAULT_OUTPUT_DIR)
        self.output_dir_le.setText(DEFAULT_OUTPUT_DIR)
        layout.addRow(out_btn, self.output_dir_le)
        layout.addItem(spacer)

        props_header = QLabel("Global Parameters")
        # folder btn
        self.show_logs_btn = QPushButton('Display Logger', self)
        self.show_logs_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_logs_btn.setToolTip('Open in new window')
        self.show_logs_btn.setGeometry(0, 0, 300, 25)
        # props header
        p_bl = QHBoxLayout()
        # p_bl.addWidget(props_header)
        p_bl.addWidget(self.show_logs_btn)
        layout.addRow(p_bl)
        # homepage progress bar
        self.progress = QProgressBar(self)
        self.progress.setGeometry(0, 0, 300, 25)
        self.progress.setMaximum(100)
        layout.addRow(self.progress)
        # start btn
        self.start_btn = QPushButton('Start', self)
        self.start_btn.setStyleSheet(
            "font-size: 16px; font-weight: 600; padding: 8px; margin-top: 10px; margin-right: 150px; margin-left: 150px; background: #E89C12; color: white; border-radius: 7px; ")
            # "font-size: 16px; font-weight: 600; padding: 8px; margin-top: 10px; background: #E89C12; color: white; border-radius: 7px; ")
        self.start_btn.clicked.connect(start)
        self.start_btn.setCursor(QCursor(Qt.PointingHandCursor))
        layout.addRow(self.start_btn)
        # progress bar animation
        self.prog_animation = QVariantAnimation(  # QPropertyAnimation(
            self,
            valueChanged=self._animate_prog,
            startValue=0.00001,
            endValue=0.9999,
            duration=2000
        )
        self.prog_animation.setDirection(QAbstractAnimation.Forward)
        self.prog_animation.finished.connect(
            self.prog_animation.start if self.progress.value() < 100 else self.prog_animation.stop)
        # self.prog_animation.finished.connect(self.prog_animation.deleteLater)
        self.prog_animation.start()

        # assign layout
        self.setLayout(layout)

    def _animate_prog(self, value):
        # print('prog', self.progress.value())
        if not self.start_btn.isEnabled():
            if self.progress.value() < 100:
                qss = """
                    text-align: center;
                    border: solid grey;
                    border-radius: 7px;
                    color: white;
                    font-size: 20px;
                """
                bg = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 {color1}, stop:{value} {color2}, stop: 1.0 {color1});".format(
                    color1=PROG_COLOR_1.name(), color2=PROG_COLOR_2.name(), value=value
                )
                qss += bg
                self.progress.setStyleSheet(qss)

    def on_input_changed(self, value: str):
        if value == "px":
            self.csvs_lb_i.setHidden(True)
            self.csvs_ip_i.setHidden(True)
        else:
            self.csvs_lb_i.setHidden(False)
            self.csvs_ip_i.setHidden(False)
        self.csvs_lb_i.setText(f"(in) 1px=__{value}")
        self.csvs_ip_i.setText(str(UNIT_PX_SCALARS[value]))
        self.simplify_input(value)

    def on_output_changed(self, value):
        if value == "px":
            self.csvs_lb_o.setHidden(True)
            self.csvs_ip_o.setHidden(True)
        else:
            self.csvs_lb_o.setHidden(False)
            self.csvs_ip_o.setHidden(False)
        self.csvs_lb_o.setText(f"(out) 1px=__{value}")
        self.csvs_ip_o.setText(str(UNIT_PX_SCALARS[value]))
        self.simplify_input(value)

    def simplify_input(self, value):
        if self.ip_scalar_type.currentText() == self.op_scalar_type.currentText():
            self.csvs_lb_i.setText(f"(in&out) 1px=__{value}")
            self.csvs_lb_o.setHidden(True)
            self.csvs_ip_o.setHidden(True)
        else:
            self.csvs_lb_i.setText(
                f"(in) 1px=__{self.ip_scalar_type.currentText()}")
            if self.op_scalar_type.currentText() != "px":
                self.csvs_lb_o.setHidden(False)
                self.csvs_ip_o.setHidden(False)

    def reset_file_selection(self):
        self.img_le.setText("")
        self.mask_le.setText("")
        self.csv_le.setText("")
        self.ip_scalar_type.setCurrentIndex(0)
        self.op_scalar_type.setCurrentIndex(0)
        self.csvs_ip_i.setText("")
        self.csvs_ip_o.setText("")
        self.folder_count = 1
        self.run_idx = 0

    def open_file_picker(self, btn_type: FileType):
        """ OPEN FILE PICKER """
        try:
            path = str(Path.home())
            if len(self.img_le.text()) > 0:
                path = os.path.dirname(self.img_le.text())
            elif len(self.mask_le.text()) > 0:
                path = os.path.dirname(self.mask_le.text())
            elif len(self.csv_le.text()) > 0:
                path = os.path.dirname(self.csv_le.text())

            if btn_type == FileType.SYNPASE or btn_type == FileType.VESICLE:
                filename = QFileDialog.getExistingDirectory(self, 'Select Output Folder')
            elif btn_type == FileType.CSV:
                file = QFileDialog.getOpenFileName(self, 'Open file', path)
                filename = file[0]
            
            if (len(filename)) > 0:
                if btn_type == FileType.SYNPASE:
                    self.img_le.setText(filename)
                elif btn_type == FileType.VESICLE:
                    self.mask_le.setText(filename)
                elif btn_type == FileType.CSV:
                    self.csv_le.setText(filename)
        except Exception as e:
            print(e, traceback.format_exc())

    def open_output_folder_picker(self):
        self.output_dir_le.setText(QFileDialog.getExistingDirectory(self, 'Select Output Folder'))