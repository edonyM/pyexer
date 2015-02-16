function [J, grad] = costFunction(theta, X, y)
%COSTFUNCTION Compute cost and gradient for logistic regression
%   J = COSTFUNCTION(theta, X, y) computes the cost of using theta as the
%   parameter for logistic regression and the gradient of the cost
%   w.r.t. to the parameters.

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta
%
% Note: grad should have the same dimensions as theta
%
tmp = X * theta;
tmp = -1 * tmp;
h = 1.0/(1 + exp(tmp));
h = transpose(h);
tmplog = log(h);
fprintf('logh %d,%d',size(tmplog)(1),size(tmplog)(2));
ONE = ones(size(y));
J = (1.0/m) * (y .* log(h) + (ONE - y) .* log(ONE - h));
grad = (1.0/m) * transpose(X) * (h - y);

% =============================================================

end
