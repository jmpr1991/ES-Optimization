import constants

import numpy as np

def initialization_function():
    """
    This function initializes the first population to start with the evolution strategy
    :return: initial_population: initial population vector
    """
    # vector initialization, depends on the mutation type
    if constants.MUTATION_TYPE == 'NON_CORR_1':
        initial_population = np.full(shape=(constants.DIM + 1, constants.POPULATION_SIZE), fill_value=np.nan)

    if constants.MUTATION_TYPE == 'NON_CORR_N':
        initial_population = np.full(shape=(constants.DIM * 2, constants.POPULATION_SIZE), fill_value=np.nan)

    # initialization of the population depending on the function to analyze
    for i in range(constants.POPULATION_SIZE):
        for j in range(constants.DIM):
            if constants.FUNCTION == 'SPHERE':
                initial_population[j, i] = np.random.uniform(constants.SHIFTED_SPH_START, constants.SHIFTED_SPH_STOP)

            if constants.FUNCTION == 'SCHWEFEL':
                initial_population[j, i] = np.random.uniform(constants.SCHWEFEL_START, constants.SCHWEFEL_STOP)

    # initialization of the sigma
    if constants.MUTATION_TYPE == 'NON_CORR_1':
        for i in range(constants.POPULATION_SIZE):
            initial_population[constants.DIM, i] = np.random.uniform(0,1)

    if constants.MUTATION_TYPE == 'NON_CORR_N':
        for i in range(constants.POPULATION_SIZE):
            for j in range(constants.DIM):
                initial_population[constants.DIM + j, i] = np.random.uniform(0,1)

    return initial_population
