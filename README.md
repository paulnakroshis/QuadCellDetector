# QuadCellDetector

[![Documentation Status](https://readthedocs.org/projects/quadcelldetector/badge/?version=latest)](https://quadcelldetector.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/university-of-southern-maine-physics/QuadCellDetector.svg?branch=master)](https://travis-ci.org/university-of-southern-maine-physics/QuadCellDetector)

A Python package designed to simulate the electronic response of a quadrant cell photodiode to the passage of a gaussian profile laser beam across its surface.

## Overview

The package simulates circular quadrant cell detectors, where the quadrant cell is characterized by a radius, and a gap that separates the four active photocell quadrants. This code allows the user to specify the beam shape, the path the beam takes across the detector, and it will output the signals produced by the photodiode: the sum of all four quadrants, the top two minus the bottom two, and the left two minus the right two.

## Installation

Clone this repository and install with `pip install .`

## Examples

To see a complete demonstration of the library features, see the [DetectorDemo][0] Jupyter notebook.

[0]: https://github.com/university-of-southern-maine-physics/QuadCellDetector/blob/master/demos/DetectorDemo.ipynb

## Contributors

+ [Paul Nakroshis](https://github.com/paulnakroshis)
+ [Ben Montgomery](https://github.com/Nyctanthous)
