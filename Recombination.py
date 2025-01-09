import constants

import numpy as np

def recombination_function(parent_vector):

    # initialize the offspring vector depending on the mutation type
    if constants.MUTATION_TYPE == 'NON_CORR_1':
        offspring_vector = np.full(shape=(constants.DIM + 1, constants.OFFSPRING_SIZE), fill_value=np.nan)

    if constants.MUTATION_TYPE == 'NON_CORR_N':
        offspring_vector = np.full(shape=(constants.DIM * 2, constants.OFFSPRING_SIZE), fill_value=np.nan)

    # initialize the recombination
    for i in range(constants.OFFSPRING_SIZE):

        # random selection of parents
        random_parents = np.random.randint(0, high=constants.DIM , size=constants.NUM_PARENTS)

        # parent reproduction and offspring creation
        for j in range(np.shape(offspring_vector)[0]):

            # Global discrete recombination
            if constants.RECOMBINATION_TYPE == 'GLOBAL_DISCRETE':
                random_parent = random_parents[np.random.randint(0, constants.NUM_PARENTS)]
                offspring_vector[j, i] = parent_vector[j, random_parent]

            # Global intermediate recombination
            elif constants.RECOMBINATION_TYPE == 'GLOBAL_INTERMEDIATE':
                offspring_vector[j, i] = np.sum(parent_vector[j, random_parents]) / constants.NUM_PARENTS

            # Combined recombination
            elif constants.RECOMBINATION_TYPE == 'COMBINED':
                if j < constants.DIM:
                    random_parent = random_parents[np.random.randint(0, constants.NUM_PARENTS)]
                    offspring_vector[j, i] = parent_vector[j, random_parent]
                else:
                    offspring_vector[j, i] = np.sum(parent_vector[j, random_parents]) / constants.NUM_PARENTS

    return offspring_vector