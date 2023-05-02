from PyQt5.QtCore import Qt, pyqtSignal, QObject, QThread, QSize, QByteArray
from PyQt5.QtGui import QImage
from utils import pixels_conversion, enum_to_unit, to_pair_list
from globals import MAX_DIRS_PRUNE
import os
import traceback
import logging
from views.logger import Logger
from typings import Unit, Workflow, DataObj, OutputOptions, WorkflowObj
from typing import List, Tuple
import numpy as np
import datetime
import pandas as pd
import shutil
from workflows.meshAlignment import Syn2Ves
from workflows.meshPairing import MakePairs

class DataLoadWorker(QObject):
    finished = pyqtSignal(list)

    def run(self, csv_path: str = ""):
        try:
            data = pd.read_csv(csv_path)
            COORDS = to_pair_list(data)
            self.finished.emit(COORDS)
            logging.info("Finished loading in and converting data")
        except Exception as e:
            self.dlg = Logger()
            self.dlg.show()
            logging.error(traceback.format_exc())
            self.finished.emit([])

class PairDataLoadWorker(QObject):
    finished = pyqtSignal(list)

    def run(self, csv1_path: str = "", csv2_path: str = ""):
        print(csv1_path)
        print(csv2_path)
        try:
            SYN_DATA = pd.read_csv(csv1_path)
            # SYN_DATA = pd.read_csv(csv1_path, index_col = 'labels')
            VES_DATA = pd.read_csv(csv2_path)
            # VES_DATA = pd.read_csv(csv2_path, index_col = 'labels')

            print(SYN_DATA)

            self.finished.emit([SYN_DATA, VES_DATA])
            logging.info("Finished loading in and converting data")
        except Exception as e:
            print("test2")
            self.dlg = Logger()
            self.dlg.show()
            logging.error(traceback.format_exc())
            self.finished.emit([])

class DownloadWorker(QObject):
    finished = pyqtSignal()

    def run(self, data: DataObj, output_ops: OutputOptions):
        """ DOWNLOAD FILES """
        dl_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        try:
            out_start = output_ops.output_dir if output_ops.output_dir is not None else './output'
        except Exception as e:
            self.dlg = Logger()
            self.dlg.show()
            logging.error(traceback.format_exc())
            self.finished.emit()

        # download files
        try:
            logging.info(
                'Prepare to download output')
            
            if(data.to_dl == 0):
                out_dir = f'{out_start}/Alignment_Out'
                os.makedirs(out_dir, exist_ok=True)
                logging.info('attempting to save cleaned dfs')

                data.analysis_df.to_csv(f'{out_dir}/{dl_time}.csv',
                                    index=False, header=True)
            elif(data.to_dl == 1):
                out_dir = f'{out_start}/Pairing_Out'
                os.makedirs(out_dir, exist_ok=True)
                logging.info('attempting to save cleaned dfs')

                out_dir = f'{out_dir}/{dl_time}'
                os.makedirs(out_dir, exist_ok=True)

                data.pair_df1.to_csv(f'{out_dir}/candidates.csv',
                                    index=False, header=True)
                data.pair_df2.to_csv(f'{out_dir}/paired.csv',
                                    index=False, header=True)
                data.pair_df3.to_csv(f'{out_dir}/unpaired.csv',
                                    index=False, header=True)

            self.finished.emit()
            logging.info("Downloaded output, closing thread")
        except Exception as e:
            self.dlg = Logger()
            self.dlg.show()
            logging.error(traceback.format_exc())
            self.finished.emit()

class RotationAnalysisWorker(QObject):
    finished = pyqtSignal(object)
    progress = pyqtSignal(int)

    def run(self, pairs: List[Tuple[int, int]], synFiles: str, vesFiles: str):
        try:
            analysis_df = pair_df1 = pair_df2 = pair_df3 = pd.DataFrame()
            
            # Run Align Code
            analysis_df = Syn2Ves(synFiles, vesFiles, pairs, pb=self.progress)

            self.output_data = DataObj(analysis_df, pair_df1, pair_df2, pair_df3, 0)
            self.finished.emit(self.output_data)
            logging.info('finished analysis')
        except Exception as e:
            self.dlg = Logger()
            self.dlg.show()
            logging.error(traceback.format_exc())
            self.finished.emit({})
            
class MeshPairingWorker(QObject):
    finished = pyqtSignal(object)
    progress = pyqtSignal(int)

    def run(self, synData: pd.DataFrame, vesData: pd.DataFrame, searchRad: float, synFiles: str, vesFiles: str):
        try:
            analysis_df = pair_df1 = pair_df2 = pair_df3 = pd.DataFrame()
            
            # Run Align Code
            pair_df1, pair_df2, pair_df3 = MakePairs(synCom=synData, vesCom=vesData, searchVolRad=searchRad, synMeshDir=synFiles, vesMeshDir=vesFiles, pb=self.progress)

            self.output_data = DataObj(analysis_df, pair_df1, pair_df2, pair_df3, 1)
            self.finished.emit(self.output_data)
            logging.info('finished analysis')
        except Exception as e:
            self.dlg = Logger()
            self.dlg.show()
            logging.error(traceback.format_exc())
            self.finished.emit({})