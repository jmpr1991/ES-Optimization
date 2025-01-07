import constants

import numpy as np

def initialization_function():

    # vector initialization
    initial_population = np.full(shape=(constants.DIM + 1, constants.POPULATION_SIZE), fill_value=np.nan)

    # initialization of the population
    for i in range(constants.POPULATION_SIZE):
        for j in range(constants.DIM):
            if constants.FUNCTION is 'SPHERE':
                initial_population[j, i] = np.random.uniform(constants.SHIFTED_SPH_START, constants.SHIFTED_SPH_STOP)

            if constants.FUNCTION is 'SCHWEFEL':
                initial_population[j, i] = np.random.uniform(constants.SCHWEFEL_START, constants.SCHWEFEL_STOP)

    # initialization of the sigma
    for i in range(constants.POPULATION_SIZE):
        initial_population[constants.DIM, i] = np.random.uniform()

