<div id="user-content-toc">
  <ul>
    <summary><h1 style="display: inline-block;">Syn2Ves Program Documentation 🧠🔍📊</h1></summary>
  </ul>
</div>

## Introduction

Welcome to the Syn2Ves Program Documentation! 🎉

**Syn2Ves** is a program designed to pair synapses with vesicle clouds based on position, and quantify the alignment of these pairings.


## Installation for use in Dragonfly

While the software can be used on it's own, Syn2Ves was intended to be used as a part of the ORS Dragonfly software. This section will give a brief overview of how to install files from the repository such that our tools appear as menu items.

### Installing Menu Items

1)  Download all of the files in the **Menu Items** folder (inside [“Dragonfly”](/Dragonfly)) and **main.exe** (under releases) 
2)  Click Windows Key + R to open the run command
3)	Type %AppData% and click OK
4)	Go to Local\ORS\Dragonfly(newest version)\pythonUserExtensions\GenericMenuItems
5)	In this folder, drag in all of the downloaded files (Put each of the files into here individually, not the entire folder)
6)	Open the **config.ini** file, and set the paths to the appropriate locations (make sure all slashes are back slashes)

### Installing Macros

1)  Download all of the files in the **Macro** folder (inside [“Dragonfly”](/Dragonfly)) 
2)  Click Windows Key + R to open the run command
3)	Type %AppData% and click OK
4)	Go to Local\ORS\Dragonfly(newest version)\pythonUserExtensions\Macros
5)	In this folder, drag in the .py file

## Using the Menu

### "Export MultiROI Labels as Meshes"

1) Select 1 or more MultiROIs that you'd like to fully export in the Properties tab on Dragonfly
2) Run the Menu Item
3) Select where you'd like your meshes exported (Each MultiROI will get its own folder within the directory you choose)

### "Launch Syn2Ves Program"

1) Run the menu item to launch the program
2) Select the two mesh folders. These are the exports of the "Export MultiROI Labels as Meshes" menu we just ran
3) Select your Synapse and Vesicle CSVs, which are also exports of the previous menu
4) Run Pairing
5) Select the "paired" CSV exported from the Pairing workflow as your Pairing CSV for Alignment Analysis
6) Run Alignment Analysis

#### Mesh Pairing Inputs 📂

**Synapse CSV 🔬**
A CSV file containing center of mass data for the synapses. The file must be formatted with the following column names: `labels`, `comX`, `comY`, `comZ`, `vol`, `SA`, `halfSA`, `sphericity`, `maxFeretLength`, `minFeretLength`, `aspectRatio`. These columns should contain numerical labels for each synapse, followed by its center of mass coordinates (x, y, z), volume, surface area, half surface area, sphericity, maximum Feret length, minimum Feret length, and aspect ratio, respectively. 

**Vesicle CSV 🔬**
Same as Synapse CSV but for Vesicles.

**COM Search Radius 🔍**
The search radius from a synapses' center of mass. The program will only pair a vesicle cloud with a synapse if its center of mass falls within the cubic volume with this radius.

#### Alignment Inputs 📂

**Synapse Folder 🧠**
A folder containing STL files of synapses, named numerically (example: 1.stl, 2.stl, etc). The program will only consider files with the ".stl" extension.

**Vesicle Folder 🧠**
A folder containing STL files of vesicles, named numerically (example: 1.stl, 2.stl, etc). The program will only consider files with the ".stl" extension.

**Pairing CSV 🧩**
A CSV file containing the pairing information of the synapses and vesicles. The file must be formatted with the following column names: `synLabel` and `vesLabel`. These columns should contain numerical labels for each synapse and vesicle, respectively. 

#### Alignment Output

Outputs a CSV file named `syn2ves_output.csv` containing the following columns:

- `synLabel`: numerical label of the synapse
- `vesLabel`: numerical label of the vesicle
- `Og_Ves_X`: x value of camera position in nm
- `Og_Ves_Y`: y value of camera position in nm
- `Og_Ves_Z`: z value of camera position in nm
- `Ves_X`: x value of vesicle position after rotations in nm
- `Ves_Y`: y value of vesicle position after rotations in nm
- `Ves_Z`: z value of vesicle position after rotations in nm
- `Syn_X`: x value of synapse position after rotations in nm
- `Syn_Y`: y value of synapse position after rotations in nm
- `Syn_Z`: z value of synapse position after rotations in nm
- `VectorAngle`: the vector angle, in degrees, between the center of mass of the original vesicle (Og_Ves) and the center of mass of the maximum surface area adjusted vesicle (Ves), with the synapse center of mass (Syn) at the center
- `Intersect`: a value representing the amount of intersecting pixels when projections of the synapse and vesicle are aligned
- `IOU`: intersection over union of the synapse and vesicle projections
- `IOS`: intersection over synapse area of the synapse and vesicle projections

Center of mass positions in this data will differ from the positions reported in other outputs for two reasons. First, other outputs are using Dragonfly's center of mass calculation rather than PyVista's mesh.center(). Second, the meshes have been manipulated such that their centers of mass maintain relative position, but not their original coordinates. 

### "Launch Syn2Ves Visualizer"**

1) Run the menu item to launch the program
2) Select the two mesh folders. These are the exports of the "Export MultiROI Labels as Meshes" menu we just ran
3) Use the "paired.csv" output from the pairing step to find IDs for a synapse-vesicle cloud pair. Enter these IDs in the appropriate prompt

## For Developers

### Installation 🚀

Before installing, you will need to install pip and git. 

```
conda install pip

conda install git
```

To run the program, clone this repository and execute the following commands:

```
cd Syn2Ves-User

pip install -r requirements.txt

python -u main.py
```

### Compiling To Executable 🚀

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
