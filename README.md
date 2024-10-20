# Rafi.ipynb

## Description:

Rafi.ipynb is a Jupyter notebook that generates all permutations of a given set of colors and applies them to an image using K-means clustering. The colors are represented as RGB values normalized to the range 0-1.

## Prerequisites:

Before you begin, ensure you have met the following requirements:

- You have installed Python 3. If not, follow the Python installation guide below.
- You have installed Jupyter Notebook. If not, follow the Jupyter installation guide below.

## Python Installation Guide:

1. Visit the official Python website at https://www.python.org/.
2. Hover over the 'Downloads' tab and click on the version that corresponds to your operating system (Windows, macOS, or Other Platforms).
3. Once the installer is downloaded, run it. In the first screen of the installation wizard, check the box that says 'Add Python to PATH', then click 'Install Now'.
4. Wait for the installation to complete, then click 'Close'.
5. To confirm that Python was installed correctly, open a new command prompt window and type python --version. You should see the version of Python that you installed.

## Jupyter Installation Guide:

1. Open a command prompt.
2. Type pip install notebook and press Enter.
3. Wait for the installation to complete.
4. To confirm that Jupyter was installed correctly, type jupyter --version. You should see the version of Jupyter that you installed.

## Installing Dependencies:

This notebook requires numpy, sklearn, PIL, and IPython. You can install them using pip, which is a package manager for Python. Open a command prompt and type the following command:

pip install numpy sklearn pillow ipython

## Running Rafi.ipynb:

To run Rafi.ipynb, follow these steps:

1. Open a command prompt.
2. Navigate to the directory where Rafi.ipynb is located using the cd command. For example, if Rafi.ipynb is in a folder called 'notebooks' on your desktop, you would type cd Desktop/notebooks.
3. Type jupyter notebook and press Enter. This will start the Jupyter Notebook server and open a new tab in your web browser with the Jupyter Notebook interface.
4. Click on Rafi.ipynb to open the notebook.

## Output:

The notebook displays all permutations of the colors applied to the image. The number of permutations is also printed. The modified images are saved in the "RGB/Output" directory.

## Customization:

You can customize the colors by modifying the new_colors array in the notebook. Each color is represented as a 1D numpy array of shape (3,) with values in the range 0-1.

## Functions:

- replace_nearest_color_rgb(img_arr: np.array, centers: np.array, colors): Replaces each pixel in img_arr with the nearest color in centers, using the colors in colors.
- arr2img(arr): Converts a numpy array to an image.
- create_model(img_arr: np.array): Creates a KMeans model and fits it to the data in img_arr.
- swap(arr, i, j): Returns a new array that is a copy of arr with the elements at indices i and j swapped.
- all_permutations(arr): Returns a list of all permutations of arr. Each permutation is a 2D numpy array with the same shape as arr.