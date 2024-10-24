# Distributor's Pallet Loading Problem Instance Generator
This repository contains Python script for generating instances of the Distributor's Pallet Loading Problem (DPLP), focusing on the optimal loading of boxes onto 3D pallets.
## [Solving a Real-Life Distributor’s Pallet Loading Problem](https://www.mdpi.com/2297-8747/26/3/53)
_Overview_

The provided code allows you to generate instances of the DPLP from an Excel dataset.
1) Flexible input through a customizable Excel dataset (Original_dataset.xlsx).
2) Generation of multiple instances with varying item quantities and distributions.
3) Automated saving of results to Excel, making it easy to analyze the generated instances.

_Requirements_

No requirement needed

_Input Data_

Before running the script, ensure that you have a properly formatted Excel file (Original_dataset.xlsx) with at least the following columns:

- _Box_: The type of box.
- _Quantity_: The number of boxes of each type.
  
Each sheet in this Excel file represents a different dataset that can be used to generate instances.

## How to Use the Code
_Step 1: Set Parameters_

In the main script, you can adjust the following parameters to control instance generation:
- _n_min_box_: Minimum number of boxes per instance (e.g., 100).
- _n_max_box_: Maximum number of boxes per instance (e.g., 500).
- _box_step_: Step size for box quantities (e.g., 50).
  
These parameters allow you to create multiple instances with varying complexities.

_Step 2: Running the Script_

Run the script by running the script. This will:

- Generate instances based on the dataset in Original_dataset.xlsx.
- Create variations of each instance (original, sorted, and unsorted distributions).
- Save the results in an output Excel file (New_instance.xlsx), with separate sheets for each distribution type.

The output Excel file will contain the following for each generated instance:

1) _Orig_: Original distribution based on the input dataset, with same box types.
2) _Distr_: Original distribution based on the input dataset, with random box types.
3) _Rand_: Random distribution, with random box types.

Each sheet contains two columns:
- _Box_: The type of box.
- _Weight_: Weight of box, measured in kilograms (kg).
- _Length_: Length of the box, measured in millimeters (mm).
- _Width_: Width of the box, measured in millimeters (mm).
- _Height_: Height of the box, measured in millimeters (mm).
- _Compression_: The compression factor, which is the maximum sustainable weight that the box can bear, measured per square millimeter (mm²). This indicates how fragile or durable the box is with respect to stacking. If a box can not sustain other boxes, then the compression is equal to 0.
- _Quantity_: The assigned quantity for each item in the instance.



## Customization
You can customize:

Input file: Modify the Original_dataset.xlsx to experiment with different datasets.

Instance complexity: Adjust the parameters (n_min_box, n_max_box) to control the size and complexity of the generated instances.

## Contribution
Feel free to fork the repository and submit pull requests to improve the scripts or add new features. If you encounter any issues or have questions, please open an issue.

For more details on the problem itself, please refer to the paper: Solving a Real-Life Distributor’s Pallet Loading Problem.

With these scripts, you can efficiently generate instances of the Distributor's Pallet Loading Problem.
