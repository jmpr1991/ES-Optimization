"""
This file contain the constants of the tsp problem
"""

# random seed
import numpy as np
np.random.seed(2) #seed of the random function to avoid errors in the vector generator

# function constants
PLOT_2D = False

SHIFTED_SPH_FUN = True
SHIFTED_SPH_CTE = 10 # shifter sphere constant
SHIFTED_SPH_START = -100 # shifted sphere function limits
SHIFTED_SPH_STOP = 100 # shifted sphere function limits

SCHWEFEL_FUN = True
SCHWEFEL_CTE = 418.9829 # Schwefel constant
SCHWEFEL_START = -500 # shifter sphere function limits
SCHWEFEL_STOP = 500 # shifter sphere function limits

VECTOR_LEN = 1000 # vector length

#problem constants
FUNCTION = 'SPHERE' # parameter to indicate the function to optimize 'SPHERE' or 'SCHWEFEL'
MUTATION_TYPE = 'NON_CORR_1' # type of mutation 'CORR_1' or 'NON_CORR_N'
RECOMBINATION_TYPE = 'GLOBAL_DISCRETE' # type of recombination
DIM = 10 # function dimension
POPULATION_SIZE = 30 # population size
OFFSPRING_SIZE = 200 # offspring size
NUM_PARENTS = 3 # number of parents

