import cv2
import matplotlib.pyplot as plt

img = cv2.imread('edge_detect_img.jfif')
edges = cv2.Canny(img, 100, 200, 3,
                  L2gradient=True)
plt.figure()
plt.title('dog')
plt.imsave('edge_detect_img.jfif', edges,
           cmap='gray', format='png')
plt.imshow(edges, cmap='gray')
plt.show()
