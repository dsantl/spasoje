import time
import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 1000, 0, 1])
plt.ion()
plt.show()

for i in range(1000):
    y = [1, np.random.random()]
    x = [1, 1]
    plt.clf()
    plt.plot(x, y)
    plt.draw()
    time.sleep(0.05)


#   capture imageR and imageL
#   find laser on imageR and imageL
#   convert images where black color is laser
#   convert laser lines in z
#   show plot where x is z and y is y