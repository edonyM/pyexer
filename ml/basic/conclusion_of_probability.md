### Conclusion of Probability Theory

* Definition of Covariance
        random variable X,Y
        simultaneous distribution P(X,Y)
        covariance of distr-P cov(X,Y)
        
        definition of cov:
        E((x-E(x))(y-E(y))) = E(xy-xE(y)-yE(x)+E(x)E(y))
                            = E(xy)-2E(x)E(y)+E(E(x)E(y))
                            = E(xy)-E(x)E(y)

* P.S. <br>
`x,y now is vector. For better calculating of Gauss-Dis, tranpose x,y into Matrix X,Y`<br>
`covariance represent the correlation between two variables.`<br>
> if the covariance is positive and larger, it means that these variables are positive correlation.
> if the covariance is negative and smaller, it means that these variables are negative correlation.
> if the covariance equals zero, it means that coefficient of correlation is zero.

* The Definition of Covariance Matrix cov
        cov = E((X-E(Y)).T*(X-E(Y)))

* P.S. <br>
`协方差矩阵计算的是不同维度之间的协方差，而不是不同样本之间的。`
`计算协方差需要计算均值，那是按行计算均值还是按列呢，我一开始就老是困扰这个问题。前面我们也特别强调了，协方差矩阵是计算不同维度间的协方差，要时刻牢记这一点。样本矩阵的每行是一个样本，每列为一个维度，所以我们要按列计算均值。`

* Properties of [Covariance Matrix](http://en.wikipedia.org/wiki/Covariance_matrix)<br>
        1. cov is DXD matrix and D equals the colums of X.<br>
        2. cov is real symmetric matrix and it can be orthogonally diagonalizable.<br>
        ```py
        "there is a upper triangular matrix U and diagonal matrix V and U.T*V*U = cov
        U.T*(V**0.5)*(V**0.5)*U = cov
        (((V**0.5)*U).T*((V**0.5)*U)) = cov
        C.T*C = cov (C = (V**0.5)*U)
        "Cholesky Decomposition can get matrix C from cov
        ```

