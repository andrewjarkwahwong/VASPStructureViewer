# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:02:50 2024
Visualizer of POSCAR or CONTCAR vasp files (optimized files)

@author: Andrew Wong
Date: 10/16/2024
"""
# Import Packages from the Atomic Simulation Environment
from ase.io import read
from ase.visualize import view

# Input: Define the File path
file_path = "C:/Users/dreww/Downloads/Ph.D. AJW/AMS/PdGe/Pd111/OH_H_FCC/CONTCAR"  # Update this with your actual file path

# Read the CONTCAR file using ASE
atoms = read(file_path)

# Visualize the structure in the ASE GUI
view(atoms)