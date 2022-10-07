import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

def change(src, dst):
    img = plt.imread(src)
    print(img.shape)

    sample = img[0][0][:3].copy()

    h, w = img.shape[:2]

    for hidx in range(h):
        for widx in range(h):
            if np.sum(np.abs(img[hidx][widx][:3] - sample))<=0.1:
                img[hidx][widx][0] = 1
                img[hidx][widx][1] = 1
                img[hidx][widx][2] = 1
                img[hidx][widx][3] = 0

    plt.imsave(dst, img)

change('./CVPR19_inv_crop.png', './CVPR19_inv_crop_t.png')
change('./ICML18_inv.png', './ICML18_inv_t.png')
