import constants
import initialization
import Recombination
import mutation
import survival_selection

import statistics_plots

import numpy as np

def main():

    # print 2d plots to have an image of the reference functions
    if constants.PLOT_2D is False:
        statistics_plots.graphics_2d()

    # raise an error in case some of these constants are not properly set
    assert 'SPHERE' or 'SCHWEFEL' == constants.FUNCTION
    assert 'NON_CORR_1' or 'NON_CORR_N' ==constants.MUTATION_TYPE
    assert 'GLOBAL_DISCRETE' or 'GLOBAL_INTERMEDIATE' or 'COMBINED' == constants.RECOMBINATION_TYPE
    assert 'ELITISM' or 'NO_ELITISM' == constants.SELECTION_TYPE

    # initialize success rate and success mean evaluations number (pex) parameters
    success_rate = 0
    pex = []
    gen_converge= []
    best_adaptation_value_vector = []

    for execution_i in range(constants.N_EXECUTIONS):

        print("execution {}".format(execution_i+1), "on going")

        # Initialization of variables
        best_adaptation_value = np.full(shape=constants.N_GENERATIONS, fill_value=np.nan)
        mean_adaptation_value = np.full(shape=constants.N_GENERATIONS, fill_value=np.nan)
        std_adaptation_value = np.full(shape=constants.N_GENERATIONS, fill_value=np.nan)

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
            mean_adaptation_value[gen] = np.mean(sorted_adaptation_value)
            std_adaptation_value[gen] = np.std(sorted_adaptation_value)

            # compute the first termination condition (optimum found)
            if abs(best_adaptation_value[gen] - constants.MIN) < constants.EPSILON:
                success_rate = success_rate + 1
                best_adaptation_value_vector.append(best_adaptation_value[gen])
                pex.append(gen)
                gen_converge.append(gen)
                break

            # compute the second termination condition (algorithm blocked in a local minimum)
            if (abs(best_adaptation_value[gen] - best_adaptation_value[gen-1]) < constants.ERROR and
                    abs(best_adaptation_value[gen] - best_adaptation_value[gen-1]) != 0): #this termination condition is injected to avoid false terminations when elitism is applied
                best_adaptation_value_vector.append(best_adaptation_value[gen])
                gen_converge.append(gen)
                break

            # jump to next generation
            gen = gen + 1

    # print statistics and plots
    statistics_plots.statistics(success_rate, pex, best_adaptation_value_vector, gen_converge)
    statistics_plots.graphics(best_adaptation_value, mean_adaptation_value, std_adaptation_value)



if __name__ == "__main__":
    main()
