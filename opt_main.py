import constants
import initialization
import Recombination
import mutation
import survival_selection

import statistics_plots

import numpy as np

def main():

    # initialize success rate and success mean evaluations number (pex) parameters
    success_rate = 0
    pex = []
    best_adaptation_value_vector = []

    # Initialization of variables
    best_adaptation_value = np.full(shape=constants.N_GENERATIONS, fill_value=np.nan)

    # Initialization of the population
    parent_population = initialization.initialization_function()

    # Evolution Strategy loop
    gen = 0
    while gen < constants.N_GENERATIONS:

        # Parent selection and recombination
        offspring_population = Recombination.recombination_function(parent_population)

        # Mutation
        mutated_population = mutation.mutation_function(offspring_population)

        # Survival selection
        parent_population, sorted_adaptation_value = survival_selection.survival_selection_function(mutated_population, parent_population)

        #save the best adaptation value
        best_adaptation_value[gen] = sorted_adaptation_value[0]

        # break the while loop since accuracy has been achieved
        if abs(best_adaptation_value[gen] - best_adaptation_value[gen - 1]) < constants.ERROR:
            success_rate = success_rate + 1
            best_adaptation_value_vector.append(best_adaptation_value[gen])
            pex.append(gen)
            break

        gen = gen + 1

    # print 2d plots to have an image of the reference functions
    if constants.PLOT_2D is True:
        statistics_plots.graphics_2d()

    print(best_adaptation_value)

if __name__ == "__main__":
    main()
