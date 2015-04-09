function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%
X = [ones(size(X,1),1) X];
z2 = X * transpose(Theta1);
a2 = sigmoid(z2);
a2 = [ones(size(a2,1),1) a2];
z3 = a2 * transpose(Theta2);
h = sigmoid(z3);
y_tmp = zeros(size(h));
for i=1:m
    for label=1:num_labels
       if y(i)== label
           y_tmp(i,label) = 1;
       else
           y_tmp(i,label) = 0;
       end
    end
end
J = (-1/m) * sum(sum(y_tmp .* log(h) + (ones(size(y_tmp)) - y_tmp).*log(ones(size(h))-h)));
Theta1_tmp = Theta1;
Theta1_tmp(:,1) = 0;
Theta2_tmp = Theta2;
Theta2_tmp(:,1) = 0;
J_R = lambda/(2*m) * (sum(sum(Theta1_tmp.^2)) + sum(sum(Theta2_tmp.^2)));
J = J + J_R;
% -------------------------------------------------------------
for t=1:m
    z2_t = X(t,:) * transpose(Theta1);%1X401 401X25
    a2_t = sigmoid(z2_t);%1X25
    a2_t = [1 a2_t];%1X26
    z3_t = a2_t * transpose(Theta2);%1X26 T(10X26)
    a3_t = sigmoid(z3_t);%1X10
    delta3 = a3_t .- y_tmp(t,:);%1X10
    delta2 = delta3 * Theta2 .* sigmoidGradient([1 z2_t]);%10X1 10X26 1X26
    delta2 = delta2(2:end);%1X25
    Theta2_grad= Theta2_grad + transpose(delta3) * a2_t;%1X10 1X26
    Theta1_grad= Theta1_grad + transpose(delta2) * X(t,:);%1X401 1X25
end
Theta2_grad = (1/m) .* Theta2_grad;
Theta1_grad = (1/m) .* Theta1_grad;
% =========================================================================
for i=1:size(Theta2_grad,1)
    for j=2:size(Theta2_grad,2)
        Theta2_grad(i,j) = Theta2_grad(i,j) + (lambda/m)*Theta2(i,j);
    end
end
for i=1:size(Theta1_grad,1)
    for j=2:size(Theta1_grad,2)
        Theta1_grad(i,j) = Theta1_grad(i,j) + (lambda/m)*Theta1(i,j);
    end
end
% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
