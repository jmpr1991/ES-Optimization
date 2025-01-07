import constants

import numpy as np

def shifted_sph_fun(x_vector):
    """
    Shifted sphere function
    :param x_vector: input vector
    :return: f(x_vector)
    """

    sph = 0
    for i in range(len(x_vector)):
        sph = sph + (x_vector[i] - constants.SHIFTED_SPH_CTE)**2

    return sph

def schwefel_fun(x_vector):
    """
    schwefel function
    :param x_vector: input vector
    :return: f(x_vector)
    """

    schwefel = 0
    for i in range(len(x_vector)):
        schwefel = schwefel + (-x_vector[i] * np.sin(np.sqrt(abs(x_vector[i]))))

    return schwefel
