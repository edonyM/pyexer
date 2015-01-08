This folder is the exercise about the book 'A First Course in Machine Learning'
* NO.1 Leave-One-Out Cross Validation('k_fold_CV.py')

![Results](https://github.com/edonyM/pyexer/blob/master/ml/basic/figure_1.png)

> according to the png,I will do some analyse.

1. we should not overfit the model and also get a good generalization

2. absolutely, the degree of 4,5,6 are not the good one for a huge loss and their tendency

3. other degrees can not be judged by CV for the model is not ensure, I need other algorithms to find the best model

* NO.2 Regularization Least Square('regular_ls.py')

![Results](https://github.com/edonyM/pyexer/blob/master/ml/basic/regularization_least-square_fitting.png)

> another way to solve the overfitting and generalization problem. CV methon is used to get the value of lamda

details are as follows:

1. assuming the model functions, lamda range from 0 to 1

2. the step of lamda depends on the models which means that it needs test

3. compute the cv-loss of the regularization least sqaure model

4. according to the cv-loss of each model, the loss should be smaller but not the smalleat and the lamda is the same
