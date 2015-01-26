### Cost Function

1. J(theta0,theta1) = 1/(2*m)*least_square(y - y(theta0,theta1))
This function is for the least error of the predected value of y according personal hypothesis.<br>
And we hope that we can get the theta0 and theta1 to minimize the J. To do this, try Gradient descent algorithm.

2. Gradient descent algorithm
repeat until convergence<br>
{<br>
theta(i) = theta(i)-alpha*(derivative(J) with theta(i))<br>
(for i=0 and i= 1)<br>
}<br>
Personally, this algorithm has some drawbacks for it gets locally optimal solution. And for linear problem the cost function is convex function, there is no need to worry about this.

3. Generalize Gradient Descent Algorithm
Linear Algebra Review(Matrix and Vector)
