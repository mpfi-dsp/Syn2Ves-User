from enum import Enum
from typing_extensions import TypedDict
from typing import List
import pandas as pd

class Workflow(Enum):
    NND = 1
    CLUST = 2
    SEPARATION = 3
    RIPPLER = 4
    GOLDSTAR = 5
    ASTAR = 6

class Unit(Enum):
    PIXEL = 1
    NANOMETER = 2
    MICRON = 3
    METRIC = 4

class FileType(Enum):
    SYNPASE = 1
    VESICLE = 2
    CSV = 3
    CSV_2 = 4
    CSV_3 = 5

class WorkflowGraph(TypedDict):
    type: str
    title: str
    x_label: str
    y_label: str
    x_type: str


class WorkflowProps(TypedDict):
    title: str
    placeholder: str



class WorkflowObj(TypedDict):
   name: str
   type: Workflow
   header: str
   desc: str
   checked: bool
   graph: WorkflowGraph
   props: List[WorkflowProps]


class DataObj:
    analysis_df: pd.DataFrame
    pair_df1: pd.DataFrame
    pair_df2: pd.DataFrame
    pair_df3: pd.DataFrame
    final_real: pd.DataFrame
    final_rand: pd.DataFrame
    to_dl: int

    def __init__(self, analysis_df: pd.DataFrame, pair_df1: pd.DataFrame, pair_df2: pd.DataFrame, pair_df3: pd.DataFrame, to_dl: int):
        self.analysis_df = analysis_df
        self.pair_df1 = pair_df1
        self.pair_df2 = pair_df2
        self.pair_df3 = pair_df3
        self.final_real = pd.DataFrame()
        self.final_rand = pd.DataFrame()
        self.to_dl = to_dl
    

class OutputOptions:
    # output_unit: Unit
    # output_scalar: str
    output_dir: str
    # delete_old: bool

    # def __init__(self, output_scalar: str, output_unit: Unit = Unit.PIXEL, output_dir: str = "./output", delete_old: bool = False):
    def __init__(self, output_dir: str = "./output"):
        # self.output_unit = output_unit
        # self.output_scalar = output_scalar
        self.output_dir = output_dir
        # self.delete_old = delete_old
