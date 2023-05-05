# Syn2Ves Program Documentation 🧠🔍📊

## Introduction

Welcome to the Syn2Ves Program Documentation! 🎉

**Syn2Ves** is a program designed to pair synapses with vesicles based on position, and quanitfy the alignment of these pairings.

The program takes the following inputs:

## Alignment Inputs 📂

### Synapse Folder 🧠
A folder containing STL files of synapses, named numerically (example: 1.stl, 2.stl, etc). The program will only consider files with the ".stl" extension.

### Vesicle Folder 🧠
A folder containing STL files of vesicles, named numerically (example: 1.stl, 2.stl, etc). The program will only consider files with the ".stl" extension.

### Pairing CSV 🧩
A CSV file containing the pairing information of the synapses and vesicles. The file must be formatted with the following column names: `synLabel` and `vesLabel`. These columns should contain numerical labels for each synapse and vesicle, respectively. 

## Mesh Pairing Inputs 📂

### Synapse CSV 🔬
A CSV file containing center of mass data for the synapses. The file must be formatted with the following column names: `labels`, `comX`, `comY`, `comZ`, `vol`, `SA`, `halfSA`, `sphericity`, `maxFeretLength`, `minFeretLength`, `aspectRatio`. These columns should contain numerical labels for each synapse, followed by its center of mass coordinates (x, y, z), volume, surface area, half surface area, sphericity, maximum Feret length, minimum Feret length, and aspect ratio, respectively. 

### Vesicle CSV 🔬
Same as Synapse CSV but for Vesicles.

### COM Search Radius 🔍
The search radius from a synapses' center of mass. The program will only pair a vesicle cloud with a synapse if its center of mass falls within the cubic volume with this radius.

## Installation 🚀

To run the program, clone this repository and execute the following commands:

```
cd Syn2Ves-User

pip install -r requirements.txt

python -u main.py
```


## Compiling To Executable 🚀

We are using [pyinstaller](https://www.pyinstaller.org/#) to compile Syn2Ves into a finished application. The steps differ based on your platform, but the following instructions are for windows (10-11).

First, ensure you have a `main.spec` and `resources.qrc` file. If you don't, run the following commands:

```
pyinstaller main.spec

pyrcc5 resources.qrc -o resources.py
```

Then to compile to exe enter the directory with `main.py` and run the following command:

WINDOWS:
```
pyinstaller.exe --onefile --windowed --icon=logo.ico main.py
```

MACOS:
```
pyinstaller --onefile --windowed --icon=logo.ico --codesign-identity=YOUR_APPLE_DEVELOPER_CERT_CODESIGN_IDENTITY --target-arch [x86_64|universal2] main.py
```

This will spew output in the console and may take a while. The final exe file can be found in the `/dist` directory.

I recommend reading through this handy article for more details regarding the specifics of compilation, particularly if you're having trouble getting icons to load: [Packaging PyQt5 applications for Windows, with PyInstaller](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/)

*Pyinstaller should be capable of building for MacOS, but I have yet to test it. If you're trying to compile for Linux, you're capable of figuring out how (or you can just use wine).*

## Output 📊

The program has two different functionalities, each outputting a different set of files.

### Alignment Output

Outputs a CSV file named `syn2ves_output.csv` containing the following columns:

- `synLabel`: numerical label of the synapse
- `vesLabel`: numerical label of the vesicle
- `Og_Ves_X`: x value of the original vesicle position
- `Og_Ves_Y`: y value of the original vesicle position
- `Og_Ves_Z`: z value of the original vesicle position
- `Ves_X`: x value of the rotated vesicle position
- `Ves_Y`: y value of the rotated vesicle position
- `Ves_Z`: z value of the rotated vesicle position
- `Syn_X`: x value of the synapse position
- `Syn_Y`: y value of the synapse position
- `Syn_Z`: z value of the synapse position
- `VectorAngle`: the vector angle between the center of mass of the original vesicle (Og_Ves) and the center of mass of the maximum surface area adjusted vesicle (Ves), with the synapse center of mass (Syn) at the center
- `Intersect`: a value representing the amount of intersecting pixels when projections of the synapse and vesicle are aligned
- `IOU`: intersection over union of the synapse and vesicle projections
- `IOS`: intersection over synapse area of the synapse and vesicle projections

### Mesh Pairing Output

## Dragonfly Implementation

While the software can be used on it's own, Syn2Ves was intended to be used as a part of the ORS dragonfly software. This section will give a brief overview of how to install all of the neccessary dragonfly files in order to have it run correctly.

All Dragonfly Files to download are in the [“Dragonfly Implementation Files”](Dragonfly Implementation Files/config.ini) folder.
