### Cost Function and Rgression with Multiple Variables(Multivariate Linear Regression)

#### Use Matrix to solve multiple variables problems, and a row is a sample.<br>

#### Feature Scaling
Contour of theta(i) and J(theta), for the variables must be the similar scale for less calculations(few interating)<br>
![](https://github.com/edonyM/pyexer/blob/master/ml/andrewNg/pic/scaleofvariables.PNG)<br>

To summary, all the feature variables should be in the similar scale for a effeciency.<br>

And some time we also replace feature variables, for example x[i], with mean normalization.<br>
Mean Normalization:<br>
        x[i] = (x[i] - mu[i])/s[i]<br>
        mu[i] is the mean of variables of feature x[i]<br>
        s[i] is the range of the x[i]

#### Learning Rate
This issue is for making gradient descent working correctly.<br>
To do this, Mr.Ng recommend that we plot J(theta)-interations.<br>
And this plotted figure can be helpful to pick a better learning rate alpha.<br>
When I am not sure the value of alpha, try alpha = 0.001,0.01,0.1,1...<br>
                                        or alpha = 0.003,0.03,0.3,1...<br>
#### Polynominal Regression
The same way to set the matrix x and theta.<br>
And one notable thing is the scale of each x[i].<br>

#### Normal Equation
Normal equation: Method to solve for theta analytically.<br>
* Design the matrix of nornal equation
* Derivate the Matrix eqaution of theta and get the minimize cost function theta.
* There is no need to care about the scale of features.
* This algrithms is alternative for the numbers of features is not too large(normally,not large than 1000, well that depends on the fact and enviroment).<br>
* For more comparision, take a look the following picture:<br>
![](https://github.com/edonyM/pyexer/blob/master/ml/andrewNg/pic/comparedtwoalg.PNG)
