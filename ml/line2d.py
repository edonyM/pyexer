import matplotlib.pyplot as mpl
import numpy as np

t = np.arange(0, 5, 0.2)
line, = mpl.plot(t, t**2, 'b--')
line.set_antialiased(False)
lines = mpl.plot(t, t**3, 'rs')
mpl.setp(lines, color='g', linewidth=2.0)
mpl.show()
