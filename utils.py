from PyQt5.QtCore import QThread, pyqtSignal
from PIL import Image
from typings import Unit, Workflow
from typing import List, Tuple
import seaborn as sns
from matplotlib import pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import traceback
import io

class Progress(QThread):
    """ PROGRESS BAR/THREADING  """
    prog = pyqtSignal(int)

    def update_progress(self, count):
        self.prog.emit(count)

def create_color_pal(n_bins: int = 10, palette_type: str ="mako") -> List[Tuple[int, int, int]]:
    """ GENERATE COLOR PALETTE USING SEABORN """
    palette = sns.color_palette(palette_type, n_colors=n_bins)
    color_palette = []
    for i in range(n_bins):
        color = palette[i]
        for value in color:
            value *= 255
        color_palette.append(color)
    color_palette.reverse()
    return color_palette


def get_complimentary_color(hexcode):
    """ GENERATE COMPLIMENTARY COLOR PALETTE """
    color = int(hexcode[1:], 16)
    comp_color = 0xFFFFFF ^ color
    comp_color = "#%06X" % comp_color
    return comp_color


def figure_to_img(fig: plt.Figure) -> Image:
    """ CONVERT FIGURE TO IMG """
    matplotlib.use('agg')
    buf = io.BytesIO()
    # convert Matplotlib figure to PIL Image
    fig.savefig(buf)
    buf.seek(0)
    img = Image.open(buf)
    return img


def pixels_conversion(data: pd.DataFrame, unit: Unit = Unit.PIXEL, scalar: float = 1, r: int = 3) -> pd.DataFrame:
    """ UPLOAD CSV AND CONVERT DF FROM ONE METRIC UNIT TO ANOTHER """
    ignored_cols = ['cluster_id', 'cluster_size', '%_gp_captured',
                    '%_img_covered', 'LCPI', 'total_gp', 'goldstar_dist', 'astar_dist', 'smoothed_dist', 'Path', 'num']  # 'radius',
    i = 0
    df = data.copy()
    if df.columns[0] == '' or df.columns[0] == ' ' or df.columns[0] == 'ID' or df.columns[0] == 'id':
        df.reset_index(drop=True, inplace=True)
    # drop empty rows
    df = df.dropna()
    for col in df:
        # print(df.columns[i])
        if df.columns[i] not in ignored_cols:
            # print(data[col].head())
            if type(df[col][0]) == tuple:
                new_col = []
                for tup in df[col]:
                    if unit == Unit.PIXEL:
                        new_col.append(tuple([round((x * scalar), r) for x in tup]))
                    else:
                        new_col.append(tuple([round((x / scalar), r) for x in tup]))
                df[col] = new_col
            elif unit == Unit.PIXEL:
                # handle scalar to unit^2 for cluster area
                if df.columns[i] == 'cluster_area':
                    df[col] = round((df[col] * (scalar * scalar)), 4)
                else: 
                    df[col] = round((df[col] * scalar), r)
            else:
                df[col] = round(df[col].div(scalar), r)
        i += 1
    # print('converted:', df.head())
    return df


def unit_to_enum(val):
    """ TURN UNIT STRING INTO ENUM """
    if val == 'px':
        return Unit.PIXEL
    elif val == 'nm':
        return Unit.NANOMETER
    elif val == 'μm':
        return Unit.MICRON
    elif val == 'metric':
        return Unit.METRIC


def enum_to_unit(val):
    """ TURN ENUM INTO UNIT STRING """
    if val == Unit.PIXEL:
        return 'px'
    elif val == Unit.NANOMETER:
        return 'nm'
    elif val == Unit.MICRON:
        return 'μm'
    elif val == Unit.METRIC:
        return 'metric'
    else:
        return 'undefined'


def to_pair_list(df: pd.DataFrame) -> List[Tuple[float, float]]:
    # turn df into coordinate list
    df = df.sort_values(by=['synLabel'])

    syn_labels = np.array(df['synLabel'])
    ves_labels = np.array(df['vesLabel'])

    coords = []
    for i in range(len(syn_labels)):
        coords.append([int(syn_labels[i]), int(ves_labels[i])])

    return coords


def to_df(coords: List[Tuple[float, float]]) -> pd.DataFrame:
    # turn coordinate list into df
    x_coords = []
    y_coords = []
    for coord in coords:
        x_coords.append(coord[1])
        y_coords.append(coord[0])
    df = pd.DataFrame(data={'X': x_coords, 'Y': y_coords})
    return df