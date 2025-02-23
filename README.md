# Graphing CSV
A simple tool to graph CSV files.

## Features
- Graph CSV files (with a header row)
- Supports multiple columns
- Supports multiple rows

## Usage
To use the tool:
1. Open Command Prompt or PowerShell
2. Navigate to the directory where the tool is located (`cd path\to\tool`)
3. There is a run.cmd in the directory. Using Command Prompt or PowerShell, run the command `run.cmd` to start the tool.

Edit the `run.cmd` file to change the arguments passed to the tool. The arguments are passed to the tool using the `run.cmd` file. The `run.cmd` file is a batch file that runs the tool with the specified arguments.
The command line arguments currently supported are:
- `--file` or `-f`: The path to the CSV file to graph (relative or absolute path) (required)
- `--mode` or `-m`: The mode to use for the graph. Currently supported modes are: (required)
  - `physics`: Plots the data formatted as a physics graph (velocity, acceleration, etc. on the y-axis and time on the x-axis)
  - `static`: Plots the data formatted as a static graph (not implemented yet)
- `--experiment`: The name of the experiment (if physics mode is selected required)
- `--object`: The name of the object being measured (if physics mode is selected required)
- `--question`: The question being answered by the graph if applicable (if physics mode is selected required)
- `--single_plot`: If set, the graph will be plotted on a single plot (optional, default is false)
- `--output_folder`: The folder to save the graph to (optional, default is the name of the experiment)

All arguments that are marked as required must be provided for the tool to run. If they are not provided, the tool will raise an error.
Some arguments are optional and have default values. If they are not provided, the tool will use the default values.
Other arguments are only if a specific mode is selected. If they are not provided, the tool will raise an error.
The tool will generate a graph based on the data in the CSV file and save it to the output folder.