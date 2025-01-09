import constants

import numpy as np

def mutation_function(offspring_vector):

    mutated_vector = np.nan

    # initialize the offspring vector for the non correlated 1-step mutation
    if constants.MUTATION_TYPE == 'NON_CORR_1':
        mutated_vector = np.full(shape=(constants.DIM + 1, constants.OFFSPRING_SIZE), fill_value=np.nan)

        # start the mutation
        for i in range(constants.POPULATION_SIZE):
            # strategic parameter mutation
            mutated_vector[-1, i] = offspring_vector[-1, i] * np.exp(constants.TAU_1 * np.random.normal())

            # check the size of the updated parameter
            if mutated_vector[-1, i] < constants.EPSILON:
                mutated_vector[-1, i] = constants.EPSILON

            # mutation of variables
            for j in range(constants.DIM):
                mutated_vector[j, i] = offspring_vector[j, i] + mutated_vector[-1, i] * np.random.normal()


    # initialize the offspring vector for the non correlated N-step mutation
    if constants.MUTATION_TYPE == 'NON_CORR_N':
        mutated_vector = np.full(shape=(constants.DIM * 2, constants.OFFSPRING_SIZE), fill_value=np.nan)

        # mutation of variables
        for i in range(constants.POPULATION_SIZE):
            random_value_i = np.random.normal()

            for j in reversed(range(constants.DIM * 2)):

                # strategic parameter mutation
                if j >= constants.DIM:
                    mutated_vector[j, i] = offspring_vector[j, i] * np.exp(constants.TAU_2 * random_value_i + constants.TAU_3 * np.random.normal())

                    # check the size of the updated parameter
                    if mutated_vector[j, i] < constants.EPSILON:
                        mutated_vector[j, i] = constants.EPSILON

                #variable mutation
                else:
                    mutated_vector[j, i] = offspring_vector[j, i] + mutated_vector[j + constants.DIM, i] * np.random.normal()

    return mutated_vector