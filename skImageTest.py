
import  skimage as sk
from skimage import io
import matplotlib.pyplot as plt
import skimage.transform as tr


c = io.imread('result.jpg')
io.imshow(c)

bps=[(c>>i)%2 for i in range(8)]
for i in range(8):
    plt.subplot(3,3,i+1)
    sk.io.imshow(bps[i],cmap='gray')
    plt.axis('off')

x4 = tr.rescale(tr.rescale(c,0.25),4,order =0)
sk.io.imshow(x4)


