# Simulation of the Peter principle with individual learning

## An agent based simulation showing the effects of learning in the Peter principle simulation

This project can be considered a continuation of https://github.com/bazotimatheus/Peter-principle-with-global-learning.
This is a cotinuation of the model developed at https://www.sciencedirect.com/science/article/abs/pii/S0378437121002958.
More information on the mathematical formalities and dynamics of the model can be showned at the work mentioned above.

Here we show the effects of individual learning at the efficiency of the hierarchycal structure.

This readme, however, will focus on how to set up and run the simulation.

## How to setup and run the simulation

First will be necessary to create the folders in which the output files will be stored.
Inside de data/ folder is a shell script named 'create_folder.sh'.
It will create all the folders with the parameters that was analyzed at the work done by Farias et al.
To run the script

> ./create_folders.sh

Before running the program I recommend you change the max number of iterations and executions at the peter/config.py file, but not other parameters.
The folders created by the previous script have a defined set of parameters, if you run the program with different ones it can crash.
Once you set the iterations and executions you can run the program manually by

> python3 main.py

or via the script 'run_all.sh'. It will run every combination of interest.

> ./run_all.sh

After running everything you can calculate the mean of the output files via the 'data/calculate_means.sh'.

> ./calculate_means.sh

## The competence analysis

This program can calculate the frequency of competences but I decided to keep it commented since, in the paper, is done with very specific parameters and not that important for the analysis because the focus is on the effects of learning in the efficiency.
