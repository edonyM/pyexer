### Conclusion about usage of the numpy, scipy and matplotlib packages.

For I am familiar with MATLAB script, I prefer to do some comparision.<br>

1. In MATLAB, there is no remarkable difference between vector and matrix.But in numpy they are definitly different.(`np.array` for vector and `np.matrix` for matrix)

2. vector and matrix some basic operation:
* a.flatten() transpose a into one-dimension array(a.ravel())
* a.reshape() reshape the array
* a.size() resize the array (a=np.array([[1,3],[0,2]]),b=a.resize((2,1),b=[[1],[0]]))
* a.sort() sort the elements in a
* to check a variable is np.array or np.matrix,type(a)
* to stack arrays np.vstack and np.hstack and np.dstack and np.concatenate
* to split arrays np.split and np.vsplit and np.hsplit and np.dsplit
* add element into an array(np.append,np.insert)
* delete element in array(np.delete)
