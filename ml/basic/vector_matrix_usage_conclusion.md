### Conclusion about usage of the numpy, scipy and matplotlib packages.

For I am familiar with MATLAB script, I prefer to do some comparision.<br>

1. In MATLAB, there is no remarkable difference between vector and matrix.But in numpy they are definitly different.(`np.array` for vector and `np.matrix` for matrix)

2. Vector and matrix some basic operation:<br>
* `a.flatten()` transpose a into one-dimension array(`a.ravel()`)
* `a.reshape()` reshape the array
* `a.size()` resize the array `(a=np.array([[1,3],[0,2]]),b=a.resize((2,1),b=[[1],[0]]))`
* `a.sort()` sort the elements in a
* to check a variable is `np.array` or `np.matrix`,`type(a)`
* to stack arrays `np.vstack` and `np.hstack` and `np.dstack` and `np.concatenate`
* to split arrays `np.split` and `np.vsplit` and `np.hsplit` and `np.dsplit`
* add element into an array(`np.append`,`np.insert`)
* delete element in array(`np.delete`)

3. Plot figure with matplotlib packages(`import matplotlib as mpl`)<br>
* plot figure with matplotlib `import matplotlib.pyplot as plt`
* plot 2-D figure use `plt.plot()`
* plot 3-D figure use `from mpl_toolkits.plot3d import Axes3D as Ax3`<br>
        `fig = plt.figure(1)`<br>
        `ax = Ax3(fig)`<br>
        `ax.plot_surface()(or ax.plot_wireframe()...)`<br>
* plot errorbar use `plt.errorbar()`
* plot figure labels setting use `plt.set_xlabel() and plt.set_ylabel()`
* plot figure adding some comments or text use `plt.text()`
* plot figure setting the axis range use `plt.axis()`
* plot the contour of the figure use `plt.contour()` 
