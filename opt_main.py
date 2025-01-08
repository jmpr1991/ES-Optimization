import constants
import initialization
import statistics_plots

import numpy as np

def main():

    # Initialization of the population
    initial_population = initialization.initialization_function()

    # print 2d plots to have an image of the reference functions
    if constants.PLOT_2D is True:
        statistics_plots.graphics_2d()

if __name__ == "__main__":
    main()
