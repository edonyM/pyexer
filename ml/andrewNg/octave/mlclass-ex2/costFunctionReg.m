function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

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
tmp = X * theta;
tmp = -1 .* tmp;
h = 1.0 ./ (1 .+ exp(tmp));
ONE = ones(size(y));
theta_new = theta(2:length(theta));
reg = (lambda/(2.0*m)) * sum(theta_new.^2);
J = (-1.0) * (y .* log(h) + (ONE - y) .* log(ONE - h));
J = J + reg * ones(size(J));
reg_grad = (lambda/m) .* theta;
reg_grad(1) = 0;
grad = (1.0/m) * transpose(X) * (h - y) - reg_grad;
% =============================================================

end
