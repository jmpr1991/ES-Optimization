"""
This file contain the constants of the tsp problem
"""

# random seed
import numpy as np
np.random.seed(2) #seed of the random function to avoid errors in the vector generator

# function constants
PLOT_2D = False

SHIFTED_SPH_CTE = 10 # shifter sphere constant
SHIFTED_SPH_START = -100 # shifted sphere function limits
SHIFTED_SPH_STOP = 100 # shifted sphere function limits

SCHWEFEL_CTE = 418.9829 # Schwefel constant
SCHWEFEL_START = -500 # Schwefel function limits
SCHWEFEL_STOP = 500 # Schwefel function limits

MIN = 0 # Minimum of the function. The minimum is shared by Sphere and Schwefel functions with this configuration

#problem characteristics
FUNCTION = 'SCHWEFEL' # parameter to indicate the function to optimize 'SPHERE' or 'SCHWEFEL'
MUTATION_TYPE = 'NON_CORR_1' # type of mutation 'NON_CORR_1' or 'NON_CORR_N'
RECOMBINATION_TYPE = 'COMBINED' # type of recombination 'GLOBAL_DISCRETE', 'GLOBAL_INTERMEDIATE' or 'COMBINED'
SELECTION_TYPE = 'NO_ELITISM' # type of recombination 'ELITISM', 'NO_ELITISM'

# constant parameters
N_EXECUTIONS = 10 # number of executions
N_GENERATIONS = 1200 # maximum number of generations
DIM = 10 # function dimension
POPULATION_SIZE = 30 # population size
OFFSPRING_SIZE = 200 # offspring size
NUM_PARENTS = 20 # number of parents
TAU_1 = 1 / np.sqrt(DIM) # mutation parameter used in non correlated 1 step method
TAU_2 = 1 / np.sqrt(2 * DIM) # mutation parameter used in non correlated n step method
TAU_3 = 1 / np.sqrt(2 * np.sqrt(DIM)) # mutation parameter used in non correlated n step method
EPSILON = 1e-3 # minimum value sigma sigma mutation parameter can take
ERROR = 1e-6 # delta difference used to break execution because the algo has converged in a local minimum

