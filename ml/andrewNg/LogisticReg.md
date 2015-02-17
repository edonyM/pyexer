### Logistic Regression Problem

`This is a classification problem rather than a  regression problem!`

1. Attributes of Classification Problem

2. Sigmod Function of Classification Problem<br>
![](https://github.com/edonyM/pyexer/blob/master/ml/andrewNg/pic/sigmodfunction.png)

3. Decision boundary of Hypothesis Function(the relation between the decision boundary and the parameter of model)

4. Cost Function J(theta) for Fitting the parameter theta.(Convex function analysis for a cost function for classification problem)<br>
![](https://github.com/edonyM/pyexer/blob/master/ml/andrewNg/pic/LinearCostFunction2Classification.png)<br>
![](https://github.com/edonyM/pyexer/blob/master/ml/andrewNg/pic/logisticregressioncostfunc1.png)<br>
![](https://github.com/edonyM/pyexer/blob/master/ml/andrewNg/pic/logisticregressioncostfunc2.png)

5. Calculate the theta to get the minimize J(theta) with gradient descent algorithm.
![](https://github.com/edonyM/pyexer/blob/master/ml/andrewNg/pic/derivativeofcostfunc.JPG)

6. Advanced Optimization Algorithm For Non-linear Optimization Problems.
 > Grandient Descent Alg<br>
 > Conjugate Gradient Alg<br>
 > BFGS(Broyden–Fletcher–Goldfarb–Shanno) Alg<br>
 > L-BFGS(Limited-memory BFGS) Alg<br>
 `There are lots of program libraries for these algorithms, if you are major in Numeric Computing, you can code it youself`<br>

7. Over-fitting: If we have too many features, the learned hypothesis may fit the training set very well(cost function almost equals zero), but fail to generalize to new examples (predict prices on new examples).
 > There are two options to solve over-fitting.
 >> 1. Reduce number of features.
 >> 2. Regularization.
