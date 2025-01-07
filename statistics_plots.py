import constants
import functions

import numpy as np
import matplotlib.pyplot as plt

def graphics_2d():
    """
    This function plot shifted sphere and Schwefel functions
    :return:n/a
    """
    # Plot shifted sphere function using matplotlib
    if constants.SHIFTED_SPH_FUN is True:
        x_vector = np.zeros((2, constants.VECTOR_LEN))
        for i in range(2):
            x_vector[i] = np.linspace(constants.SHIFTED_SPH_START,constants.SHIFTED_SPH_STOP,num=constants.VECTOR_LEN)

        x, y = np.meshgrid(x_vector[0], x_vector[1])
        z = functions.shifted_sph_fun([x,y])

        plt.figure('figure 1')
        ax = plt.axes(projection='3d')
        ax.set_title('Shifted Sphere Function')
        ax.contour3D(x, y, z, 50, cmap='viridis')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')

    # Plot schwefel function using matplotlib
    if constants.SCHWEFEL_FUN is True:
        x_vector = np.zeros((2, constants.VECTOR_LEN))
        for i in range(2):
            x_vector[i] = np.linspace(constants.SCHWEFEL_START,constants.SCHWEFEL_STOP,num=constants.VECTOR_LEN)

        x, y = np.meshgrid(x_vector[0], x_vector[1])
        z = functions.schwefel_fun([x,y])

        plt.figure('figure 2')
        ax = plt.axes(projection='3d')
        ax.set_title('Schwefel function')
        ax.contour3D(x, y, z, 50, cmap='viridis')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.show()