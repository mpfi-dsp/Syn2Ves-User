<div id="user-content-toc">
  <ul>
    <summary><h1 style="display: inline-block;">Syn2Ves Program Documentation 🧠🔍📊</h1></summary>
  </ul>
</div>

## Introduction

Welcome to the Syn2Ves Program Documentation! 🎉

**Syn2Ves** is a program designed to pair synapses with vesicle clouds based on position, and quantify the alignment of these pairings.

## Installation for use in ORS Dragonfly

While the software can be used on it's own, Syn2Ves was intended to be used as a part of the ORS Dragonfly software. This section will give a brief overview of how to install repository files such that our tools appear as menu items.

### Collect your files
First, download all of the necessary files for this project. 

1) Clone the GitHub repository
   - Click on the green **Code** button at the top of the page
   - Select **Download Zip**
   - Extract all files from the **Syn2Ves** folder to your computer. Later instructions will refer to this directory as **...\Syn2Ves**
2) Download the Syn2Ves app
   - Under **Releases**, to the right of the file list, select **Syn2Ves Application**
   - Select **syn2ves.exe**
   - After syn2ves.exe has finished downloading, move it to the **Syn2Ves** folder

Next, we need to make some of these files discoverable by ORS Dragonfly. 

### Macro

1)  Navigate to **...\Syn2Ves\Dragonfly\Macros** on your computer
2)  Click **Windows Key + R** to open the run command
3)	Type **%AppData%** and click **OK**
4)	This brings you to **...\AppData\Roaming**. Navigate back ot the **AppData** folder, then **...\AppData\Local\ORS\Dragonfly\pythonUserExtensions\Macros**. Make sure that you selected the newest version of ORS Dragonfly
6)	Drag **multiRoiToMesh.py** from **...\Syn2Ves\Dragonfly\Macros** into the **...\pythonUserExtensions\Macros** folder. Leave this folder open for easy access

### Menu Items

1)  Navigate to **...\Syn2Ves\Dragonfly\Menu Items** on your computer
2)  Click **Windows Key + R** to open the run command
3)	Type **%AppData%** and click **OK**
4)	This brings you to **...\AppData\Roaming**. Navigate back ot the **AppData** folder, then **...\AppData\Local\ORS\Dragonfly\pythonUserExtensions\GenericMenuItems**. Make sure that you selected the newest version of ORS Dragonfly
6)	Individually drag each of files from **...\Syn2Ves\Dragonfly\Menu Items** into the **GenericMenuItems** folder
7)	Open the **config.ini** file
    - After **dragonfly_macro_path =**, replace the placeholder text with the directory for the new macro. It should look something like this: **...\AppData\Local\ORS\Dragonfly\pythonUserExtensions\Macros\multiRoiToMesh.py**
    - After **syn2ves_exe_path =**, replace the placeholder text with the directory for the **Syn2Ves Application** file. It should look somehting like this: **...\Syn2Ves\syn2ves.exe**

## Using the Menu

Start by opening Dragonfly. The menu items should appear at the top of the window under the heading **Synapse-Vesicle Tools**. 

Load your ORS session of interest. This session must contain segmented synapses and vesicle clouds. Synapses should be saved as classes in a MultiROI with other synapses. Vesicle clouds should be saved as classes in a MultiROI with other vesicle clouds.  

### Export MultiROI Labels as Meshes

1) Using **ctrl + L-click**, select the synapses and vesicle cloud MultiROIs under the **Properties** section
2) Open the **Synapse-Vesicle Tools** dropdown menu and select **Export MultiROI Labels as Meshes**
3) Select a folder for output. Each MultiROI will get its own folder within the directory you choose
4) This step varies in duration. Roughly, it takes tens of minutes to export hundreds of classes. You may not use ORS Dragonfly for anything else while running the macro. 

Output: 

- Folders containing meshes
- CSVs with measurements for each MultiROI class

### Launch Syn2Ves Program

1) Open the **Synapse-Vesicle Tools** dropdown menu and select **Launch Syn2Ves Program**. A new window will appear 
2) Select the two mesh folders for synapses and vesicle clouds as prompted. These are outputs from the **Export MultiROI Labels as Meshes** macro

#### For Pairing
1) Select your Synapse and Vesicle CSV. These are outputs from the **Export MultiROI Labels as Meshes** macro
2) Enter a **center of mass (CoM) search radius** in microns (E.g. "2"). The program will only pair a vesicle cloud with a synapse if its CoM falls within the cubic volume with this radius. We have found that a search radius of 2 microns leads to near-perfect (~99%) pairing accuracy.
3) **Set Output Folder**
4) **Run Mesh Pairing**

Output: 

- **paired.csv**: A CSV file containing the pairing information of the synapses and vesicles
- **unpaired.csv**: A CSV file containing the measurements of unpaired vesicle clouds

#### For Alignment
1) Click on **Set Pairing CSV**, then select **paired.csv**
2) **Set Output Folder**
3) **Run Alignment Analysis**

Outputs a CSV file named **align.csv** containing the following columns:

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

### Launch Syn2Ves Visualizer

1) Open the **Synapse-Vesicle Tools** dropdown menu and select **Launch Syn2Ves Visualizer**
2) Select the two mesh folders as prompted. These are outputs from the **Export MultiROI Labels as Meshes** menu we just ran
3) Use **paired.csv** to find IDs for a synapse-vesicle cloud pair. Enter these IDs as prompted
4) A window will appear with an interactive 3D plotter

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
pyi-makespec main.py

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
