import sys
import tensorflow as tf
import numpy as np 
import pydicom
from PIL import Image
import weights

#takes the root folder path and returns a list of pictures
def collect_pictures(path):
    pic_list = []
    full_path_list = []
    for dirName, subdirList, fileList in os.walk(path):
    # print('test')
    for filename in file_list:
        if ".png" in filename.lower() or ".jpg" in filename.lower():  
            full_path_list.append(os.path.join(dirName,filename))

    for im in full_path_list:
        pic_list.append(imageio.imread(im))

    return pic_list

#takes a list of pictures and returns a list of matrices
def flip_to_mat(images):
    matrix_list = []
    for im in images:
        arr = np.array(im)
        arr = arr.reshape(1, -1)
        matrix_list.append(arr)

    return matrix_list


if __name__ == "__main__":
    return flip_to_mat(collect_pictures(sys.argv[1]))