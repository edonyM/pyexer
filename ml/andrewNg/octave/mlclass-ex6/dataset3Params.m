function [C, sigma] = dataset3Params(X, y, Xval, yval)
%EX6PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = EX6PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%
tmp = [0.01;0.03;0.1;0.3;1;3;10;30];
error_pred = zeros(8,8);
for i=1:8
    for j=1:8
        model = svmTrain(X,y,tmp(i),@(x1, x2) gaussianKernel(x1, x2, tmp(j)));
        predictions = svmPredict(model, Xval);
        error_pred(i,j) = mean(double(predictions ~= yval));
    end
end
min_pred = error_pred(1,1);
min_i = 1;
min_j = 1;
for i=1:8
    for j=1:8
        if error_pred(i,j)<min_pred
            min_pred = error_pred(i,j);
            min_i = i;
            min_j = j;
        end
    end
end
C = tmp(min_i);
sigma = tmp(min_j);
% =========================================================================

end
