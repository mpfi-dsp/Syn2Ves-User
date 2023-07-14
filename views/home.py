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

HEADER = "Synapse-Vesicle Cloud Offset Analysis"
DESC = "Upload all files, and click \"Start\" to begin!"

class HomePage(QWidget):
    """
    MAIN PAGE
    ________________
    @start: begins running selected workflows and display all subpages
    """
    def __init__(self, start: partial, pair: partial):
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

        self.mesh_uploads_header = QLabel("Select Mesh Folders")
        _h_bl = QHBoxLayout()
        _h_bl.addWidget(self.mesh_uploads_header)
        layout.addRow(_h_bl)
        self.mesh_uploads_desc = QLabel("Required for Both Workflows")
        self.mesh_uploads_desc.setStyleSheet("font-size: 17px; font-weight: 400; padding-top: 3px; padding-bottom: 10px;")
        _d_bl = QHBoxLayout()
        _d_bl.addWidget(self.mesh_uploads_desc)
        layout.addRow(_d_bl)
        # synapse mesh folder btn
        synMesh_btn = QPushButton('Set Synapse Folder', self)
        synMesh_btn.setCursor(QCursor(Qt.PointingHandCursor))
        synMesh_btn.setToolTip('Must be folder of .STL format files...')
        synMesh_btn.clicked.connect(partial(self.open_file_picker, FileType.SYNPASE))
        # synapse mesh folder input
        self.synMesh_le = QLineEdit()
        self.synMesh_le.setPlaceholderText("None Selected (Folder of STL Files)") 
        # add synapse mesh row
        layout.addRow(synMesh_btn, self.synMesh_le)
        # vesicle mesh folder btn
        vesMesh_btn = QPushButton('Set Vesicle Folder', self)
        vesMesh_btn.setCursor(QCursor(Qt.PointingHandCursor))
        vesMesh_btn.setToolTip('Must be folder of .STL format files...')
        vesMesh_btn.clicked.connect(partial(self.open_file_picker,  FileType.VESICLE))
        # vesicle mesh folder input
        self.vesMesh_le = QLineEdit()
        self.vesMesh_le.setPlaceholderText("None Selected (Folder of STL Files)")
        # add vesicle mesh row
        layout.addRow(vesMesh_btn, self.vesMesh_le)

        spacer = QSpacerItem(15, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        self.more_uploads_header = QLabel("Select Pairing Inputs")
        _h_bl = QHBoxLayout()
        _h_bl.addWidget(self.more_uploads_header)
        layout.addRow(_h_bl)

        # csv btn
        synCsv_btn = QPushButton('Set Synapse CSV', self)
        synCsv_btn.setCursor(QCursor(Qt.PointingHandCursor))
        synCsv_btn.setToolTip('Synapse and Vesicle Paits. CSV must have synLabel and vesLabel columns with no spaces.')
        synCsv_btn.clicked.connect(partial(self.open_file_picker, FileType.CSV_2))
        # csv input
        self.synCsv_le = QLineEdit()
        self.synCsv_le.setPlaceholderText("None Selected (CSV)")
        # add csv row
        layout.addRow(synCsv_btn, self.synCsv_le)
        # csv btn
        vesCsv_btn = QPushButton('Set Vesicle CSV', self)
        vesCsv_btn.setCursor(QCursor(Qt.PointingHandCursor))
        vesCsv_btn.setToolTip('Synapse and Vesicle Paits. CSV must have synLabel and vesLabel columns with no spaces.')
        vesCsv_btn.clicked.connect(partial(self.open_file_picker, FileType.CSV_3))
        # csv input
        self.vesCsv_le = QLineEdit()
        self.vesCsv_le.setPlaceholderText("None Selected (CSV)")
        # add csv row
        layout.addRow(vesCsv_btn, self.vesCsv_le)

        comRad_lbl = QLabel("COM Search Radius")
        comRad_lbl.setStyleSheet("font-size: 17px; font-weight: 400;")
        self.comRad_le = QLineEdit()
        self.comRad_le.setPlaceholderText("Synapse COM Search Radius")
        # self.csvs_ip_i.setStyleSheet(
            # "font-size: 16px; padding: 8px;  font-weight: 400; background: #ddd; border-radius: 7px;  margin-bottom: 5px; max-width: 150px; ")
        layout.addRow(comRad_lbl, self.comRad_le)

        # analysis start btn
        self.pair_btn = QPushButton('Run Mesh Pairing', self)
        self.pair_btn.setStyleSheet(
            "font-size: 16px; font-weight: 600; padding: 8px; margin-top: 15px; margin-right: 150px; margin-left: 150px; background: #E89C12; color: white; border-radius: 7px; ")
        self.pair_btn.clicked.connect(pair)
        self.pair_btn.setCursor(QCursor(Qt.PointingHandCursor))
        layout.addRow(self.pair_btn)
        
        spacer = QSpacerItem(15, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        # upload header
        self.upload_header = QLabel("Select Alignment Inputs")
        # file btns widget
        h_bl = QHBoxLayout()
        h_bl.addWidget(self.upload_header)
        layout.addRow(h_bl)
        # csv btn
        csv_btn = QPushButton('Set Pairing CSV', self)
        csv_btn.setCursor(QCursor(Qt.PointingHandCursor))
        csv_btn.setToolTip('Synapse and Vesicle Paits. CSV must have synLabel and vesLabel columns with no spaces.')
        csv_btn.clicked.connect(partial(self.open_file_picker, FileType.CSV))
        # csv input
        self.csv_le = QLineEdit()
        self.csv_le.setPlaceholderText("None Selected (CSV)")
        # add csv row
        layout.addRow(csv_btn, self.csv_le)

        # analysis start btn
        self.start_btn = QPushButton('Run Align Analysis', self)
        self.start_btn.setStyleSheet(
            "font-size: 16px; font-weight: 600; padding: 8px; margin-top: 15px; margin-right: 150px; margin-left: 150px; background: #E89C12; color: white; border-radius: 7px; ")
        self.start_btn.clicked.connect(start)
        self.start_btn.setCursor(QCursor(Qt.PointingHandCursor))
        layout.addRow(self.start_btn)
        
        spacer = QSpacerItem(15, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        self.more_uploads_header = QLabel("Select Output Location")
        _h_bl = QHBoxLayout()
        _h_bl.addWidget(self.more_uploads_header)
        layout.addRow(_h_bl)

        # TODO: output folder header
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

        # self.synMesh_le.setText("C:/Users/Arman/Documents/2023-05-01_12-34-29/Final Synapses (as Multi-ROI)")
        # self.vesMesh_le.setText("C:/Users/Arman/Documents/2023-05-01_12-34-29/Final Vesicles (as Multi-ROI)")
        # self.csv_le.setText()
        # self.synCsv_le.setText("C:/Users/Arman/Documents/2023-05-01_12-34-29/Final Synapses (as Multi-ROI) Measurements.csv")
        # self.vesCsv_le.setText("C:/Users/Arman/Documents/2023-05-01_12-34-29/Final Vesicles (as Multi-ROI) Measurements.csv")

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

    def reset_file_selection(self):
        self.synMesh_le.setText("")
        self.vesMesh_le.setText("")
        self.csv_le.setText("")
        self.synCsv_le.setText("")
        self.vesCsv_le.setText("")
        self.vesMesh_le.setText("")
        self.folder_count = 1
        self.run_idx = 0

    def open_file_picker(self, btn_type: FileType):
        """ OPEN FILE PICKER """
        try:
            path = str(Path.home())
            if len(self.synMesh_le.text()) > 0:
                path = os.path.dirname(self.synMesh_le.text())
            elif len(self.vesMesh_le.text()) > 0:
                path = os.path.dirname(self.vesMesh_le.text())
            elif len(self.csv_le.text()) > 0:
                path = os.path.dirname(self.csv_le.text())
            elif len(self.synCsv_le.text()) > 0:
                path = os.path.dirname(self.csv_le.text())
            elif len(self.vesCsv_le.text()) > 0:
                path = os.path.dirname(self.csv_le.text())

            if btn_type == FileType.SYNPASE or btn_type == FileType.VESICLE:
                filename = QFileDialog.getExistingDirectory(self, 'Select Folder')
            elif btn_type == FileType.CSV or btn_type == FileType.CSV_2 or btn_type == FileType.CSV_3:
                file = QFileDialog.getOpenFileName(self, 'Open file', path)
                filename = file[0]
            
            if (len(filename)) > 0:
                if btn_type == FileType.SYNPASE:
                    self.synMesh_le.setText(filename)
                elif btn_type == FileType.VESICLE:
                    self.vesMesh_le.setText(filename)
                elif btn_type == FileType.CSV:
                    self.csv_le.setText(filename)
                elif btn_type == FileType.CSV_2:
                    self.synCsv_le.setText(filename)
                elif btn_type == FileType.CSV_3:
                    self.vesCsv_le.setText(filename)
        except Exception as e:
            print(e, traceback.format_exc())

    def open_output_folder_picker(self):
        self.output_dir_le.setText(QFileDialog.getExistingDirectory(self, 'Select Output Folder'))
