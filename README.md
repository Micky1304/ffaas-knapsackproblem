## Feature-Free Automated Algorithm Selection for the 0-1 Knapsack Problem

This repository contains the project that was conducted as part of my bachelor's thesis "Deep Learning as a Feature-Free Approach for Automated Algorithm Selection on the 0-1 Knapsack Problem".

The files that were created for this project are: All files outside "knapsacksolver" as well as the directories "dataset", "hardInstancesScores",  and "scores" within "knapsacksolver". In addition, the instances in "knapsacksolver/hardInstancesPI" were converted to the format Pisinger and originate from https://github.com/JorikJooken/knapsackProblemInstances. The remaining files are clones from https://github.com/fontanf/knapsacksolver.

# The Jupyter Notebooks are structures as follows:

InstanceGenerator.ipynb: Definition of the generation rules. Creation of 20,300 instances saved in the folder "knapsacksolver/dataset"

FinalizeInstances.ipynb: Function to solve the instances with the algorithm combo. Read and overwrite the max_profit and time of the instances

Par10Solver.ipynb: Parallel calculation of the PAR10 scores for the three algorithms: greedy, dynamic programming, and branch and bound. In the directory "knapsacksolver/scores" the scores for every algorithm for each of the ten runs is documented. The scores are averaged and combined to the file "knapsacksolver/scores/scores.csv".

ScoreOverview.ipynb: Visualizations of the PAR10 scores. Calculation of the amount of instances that were best solved with each algorithm. Illustration of the seven generation classes.

ConcatInstancesToCsv.ipynb: Creation of a single csv-file that contains the information for each instance. Based on two different scaling approaches, two instance files are created and saved to "AAS/instances(to_c_z).csv".

In the directory "AAS", the Machine Learning (ML) models are used and evaluated:

Structure of Tests.ipynb: Definition of the way in which the ML structures are tested. With different hyperparameter settings, many ML models are trained and their results are saved in csv-files.

ResultDiscussion: Visulization of the best performing model. Tables with the performances of each generation.

The csv-files named MLstructure_results_generation.csv contain the results of the ML models.  

Contents of the directories:
"knapsacksolver/dataset": All 20,300 instances generated for this project
"knapsacksolver/scores": The scores of the ten runs for each of the three algorithms as well as the combinations.
"figures/": All figures used in the thesis.

# Structure for the Hard Instances

ConvertHardInstancesToPisinger.py: Locally created and executed file. It transforms the hard instances from https://github.com/JorikJooken/knapsackProblemInstances to match the format Pisinger in order to use the algorithms.

HardInstanceSolver.ipynb: Calculation of the PAR10 scores for the algorithms: greedy, dynamic programming, and branch and bound on the hard instances. The results are saved to "knapsacksolver/hardInstancesScores".

Contents of the directories:
"knapsacksolver/hardInstancesPI": Directory that contains the hard instances in the Pisinger format. 
"knapsacksolver/hardInstancesScores": Scores of the three algorithms on the hard instances.