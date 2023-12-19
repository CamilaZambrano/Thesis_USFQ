import os
import logging
import numpy as np
from imageio import imread
from matplotlib import pyplot as plt
from PIL import Image

import morphsnakes as ms

def visual_callback_2d(background, fig=None):
    """
    Returns a callback than can be passed as the argument `iter_callback`
    of `morphological_geodesic_active_contour` and
    `morphological_chan_vese` for visualizing the evolution
    of the levelsets. Only works for 2D images.

    Parameters
    ----------
    background : (M, N) array
        Image to be plotted as the background of the visual evolution.
    fig : matplotlib.figure.Figure
        Figure where results will be drawn. If not given, a new figure
        will be created.

    Returns
    -------
    callback : Python function
        A function that receives a levelset and updates the current plot
        accordingly. This can be passed as the `iter_callback` argument of
        `morphological_geodesic_active_contour` and
        `morphological_chan_vese`.

    """

    # Prepare the visual environment.
    if fig is None:
        fig = plt.figure()
    fig.clf()
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.imshow(background, cmap=plt.cm.gray)

    ax2 = fig.add_subplot(1, 2, 2)
    ax_u = ax2.imshow(np.zeros_like(background), vmin=0, vmax=1)
    plt.pause(0.001)

    def callback(levelset):

        if ax1.collections:
            del ax1.collections[0]
        ax1.contour(levelset, [0.5], colors='r')
        ax_u.set_data(levelset)
        fig.canvas.draw()
        plt.pause(0.001)

    return callback


def visual_callback_3d(fig=None, plot_each=1):
    """
    Returns a callback than can be passed as the argument `iter_callback`
    of `morphological_geodesic_active_contour` and
    `morphological_chan_vese` for visualizing the evolution
    of the levelsets. Only works for 3D images.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure where results will be drawn. If not given, a new figure
        will be created.
    plot_each : positive integer
        The plot will be updated once every `plot_each` calls to the callback
        function.

    Returns
    -------
    callback : Python function
        A function that receives a levelset and updates the current plot
        accordingly. This can be passed as the `iter_callback` argument of
        `morphological_geodesic_active_contour` and
        `morphological_chan_vese`.

    """

    from mpl_toolkits.mplot3d import Axes3D
    # PyMCubes package is required for `visual_callback_3d`
    try:
        import mcubes
    except ImportError:
        raise ImportError("PyMCubes is required for 3D `visual_callback_3d`")

    # Prepare the visual environment.
    if fig is None:
        fig = plt.figure()
    fig.clf()
    ax = fig.add_subplot(111, projection='3d')
    plt.pause(0.001)

    counter = [-1]

    def callback(levelset):

        counter[0] += 1
        if (counter[0] % plot_each) != 0:
            return

        if ax.collections:
            del ax.collections[0]

        coords, triangles = mcubes.marching_cubes(levelset, 0.5)
        ax.plot_trisurf(coords[:, 0], coords[:, 1], coords[:, 2],
                        triangles=triangles)
        plt.pause(0.1)

    return callback


def rgb2gray(img):
    """Convert a RGB image to gray scale."""
    return 0.2989 * img[..., 0] + 0.587 * img[..., 1] + 0.114 * img[..., 2]


def GAC_active_contour(x, y, input_path, BWoutput_pathGAC):
    logging.info('Running: active_contour (MorphGAC)...')

    # Load the image.
    img = imread(input_path)[..., 0] / 255.0

    # g(I)
    gimg = ms.inverse_gaussian_gradient(img, alpha=1000, sigma=5.48)

    # Initialization of the level-set.
    init_ls = ms.circle_level_set(img.shape, (y, x), 50)

    # Callback for visual plotting
    callback = visual_callback_2d(img)

    # MorphGAC.
    array = ms.morphological_geodesic_active_contour(gimg, iterations=88,
                                             init_level_set=init_ls,
                                             smoothing=1, threshold=0.31,
                                             balloon=1, iter_callback=callback)
    # Save masks
    for i, element in enumerate(array):
        image_u = Image.fromarray((element * 255).astype(np.uint8), mode='L')
        image_u.save(BWoutput_pathGAC + '_iteration' + str(i) + '.jpg')

def CV_active_contour(x, y, input_path, BWoutput_pathCV):
    logging.info('Running: active_contour (MorphACWE)...')

    # Load the image.
    img = imread(input_path)[..., 0] / 255.0

    # Initialization of the level-set.
    init_ls = ms.circle_level_set(img.shape, (y, x), 40)

    # Callback for visual plotting
    callback = visual_callback_2d(img)

    # Morphological Chan-Vese (or ACWE)
    array = ms.morphological_chan_vese(img, iterations=436,
                               init_level_set=init_ls,
                               smoothing=3, lambda1=1, lambda2=1,
                               iter_callback=callback)

    #Save masks
    for i, element in enumerate(array):
        image_u = Image.fromarray((element * 255).astype(np.uint8), mode='L')
        image_u.save(BWoutput_pathCV + '_iteration' + str(i) + '.jpg')

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    input_folder = "Crop/CenterPoints"
    txtFiles = os.listdir(input_folder)

    for txt in txtFiles:
        input_file = os.path.join(input_folder, txt)
        with open(input_file, 'r') as file:
            # Eliminar espacios en blanco y separar por comas
            data = file.readline().strip().split(',')

            # Asignar los datos a variables
            file_name = data[0]
            x = float(data[1])
            y = float(data[2])

            image_name = file_name + '_F.jpg'

            input_path = 'Crop/Filtered/' + image_name
            BWoutput_pathCV = 'acResultsMasks/CV/mask_CVBWC_' + file_name
            BWoutput_pathGAC = 'acResultsMasks/GAC/mask_GACBWC_' + file_name

            GAC_active_contour(x, y, input_path, BWoutput_pathGAC)
            CV_active_contour(x, y, input_path, BWoutput_pathCV)

    logging.info("Done.")
    plt.show()
