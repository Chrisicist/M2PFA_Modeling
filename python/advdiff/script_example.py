# -*- coding: utf-8 -*-
__author__ = "Guillaume Fuhr"

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Get the absolute path to the advdiff directory
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(current_dir))  # Add parent directory to path

try:
    from utils.plotting import figformat, animated_plot_2d, animated_plot_1d
except ModuleNotFoundError:
    sys.path.append(os.path.normpath(os.path.realpath(__file__)))
    from utils.plotting import figformat, animated_plot_2d, animated_plot_1d

# Simple pyximport setup with explicit paths
import pyximport
pyximport.install(setup_args={
    'include_dirs': [np.get_include(), current_dir],
    'build_dir': current_dir
})

if int(sys.version[0]) != 3:
    sys.exit("This script requires Python 3")

# Print some debug information
print(f"Current directory: {current_dir}")
print(f"Python path: {sys.path}")

import advdiff

if __name__ == '__main__':
    tout, data1d, _ = advdiff.simulate_1d()
    anim = animated_plot_1d(data1d)
    plt.plot(data1d[-1])
    plt.show()
