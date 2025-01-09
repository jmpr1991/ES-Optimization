import constants
import functions

import numpy as np

def survival_selection_function(mutated_vector, parent_vector):

    #initialize adaptation value
    adaptation_value = np.full(shape=(constants.POPULATION_SIZE + constants.OFFSPRING_SIZE, 2), fill_value=np.nan)
    sorted_adaptation_value = np.full(shape=(constants.POPULATION_SIZE + constants.OFFSPRING_SIZE, 2), fill_value=np.nan)

    #evaluate mutated vector
    for i in range(constants.OFFSPRING_SIZE):

        # save the index to support on the sort process
        adaptation_value[i, 1] = i

        if constants.SHIFTED_SPH_FUN is True:
            adaptation_value[i, 0] = functions.shifted_sph_fun(mutated_vector[0:constants.DIM, i])

        if constants.SCHWEFEL_FUN is True:
            adaptation_value[i, 0] = functions.schwefel_fun(mutated_vector[0:constants.DIM, i])

    if constants.SELECTION_TYPE == 'NO_ELITISM':
        sorted_adaptation_value = adaptation_value[np.argsort(adaptation_value[:,0]), :]

        survival_population = mutated_vector[:, sorted_adaptation_value[0:constants.POPULATION_SIZE, 1].astype(int)]

        return survival_population

    # evaluate parent vector
    for i in range(constants.OFFSPRING_SIZE, constants.OFFSPRING_SIZE + constants.NUM_PARENTS, 1):

        # save the index to support on the sort process
        adaptation_value[i, 1] = i

        if constants.SHIFTED_SPH_FUN is True:
            adaptation_value[i, 0] = functions.shifted_sph_fun(mutated_vector[0:constants.DIM - 1, i])

        if constants.SCHWEFEL_FUN is True:
            adaptation_value[i, 0] = functions.schwefel_fun(mutated_vector[0:constants.DIM - 1, i])

    if constants.SELECTION_TYPE == 'ELITISM':
        survival_vector = sorted()