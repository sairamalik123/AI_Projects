import numpy as np
import matplotlib.pyplot as plot

values = np.random.randint(10, size=(100))
plot.plot(values)

plot.title('Random Noise using Test Program')
plot.xlabel('x-axis')
plot.ylabel('y-axis')
plot.show()