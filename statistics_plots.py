import constants
import functions

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def graphics_2d():

    if constants.SHIFTED_SPH_FUN is True:
        x_vector = np.zeros((constants.DIM, constants.VECTOR_LEN))
        for i in range(constants.DIM):
            x_vector[i] = np.linspace(constants.SHIFTED_SPH_START,constants.SHIFTED_SPH_STOP,num=constants.VECTOR_LEN)

        X, Y = np.meshgrid(x_vector[0], x_vector[1])
        Z = functions.shifted_sph_fun([X,Y])

        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot_trisurf(X, Y, Z, rstride=1, cstride=1,
                        cmap='viridis', edgecolor='none')
        ax.set_title('surface')
        ax.contour3D(X, Y, Z, 50, cmap='binary')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')