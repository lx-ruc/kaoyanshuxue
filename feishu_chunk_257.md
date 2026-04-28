#### (2) 施密特正交化方法

<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\dots ,\boldsymbol{\alpha}_{s}</equation>为一个正交向量组

正交向量组<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\dots \boldsymbol{\alpha}_{s}</equation>用内积表示为：

<equation>(\boldsymbol{\alpha}_i, \boldsymbol{\alpha}_j) = 0 (i, j = 1, 2, \dots s; i \neq j)</equation>且<equation>(\boldsymbol{\alpha}_i, \boldsymbol{\alpha}_i) \neq 0 (i = 1, 2, \dots , s)</equation>.


每个向量都是单位向量的正交向量组称为标准正交向量组（或规范正交向量组），即

<equation>\left(\boldsymbol {\alpha} _ {i}, \boldsymbol {\alpha} _ {j}\right) = \left\{ \begin{array}{l l} 0, & \text {当} i \neq j \text {时}, \\ 1, & \text {当} i = j \text {时} \end{array} \right. (i, j = 1, 2, \dots , s).</equation>


用施密特正交化方法可将任意一组线性无关的向量组改造成为标准正交向量组（先正交化再单位化）。若<equation>\alpha_{1}, \alpha_{2}, \dots, \alpha_{n}</equation>是一组线性无关的向量组，令

<equation>\begin{array}{l} \boldsymbol {\beta} _ {1} = \boldsymbol {\alpha} _ {1}, \\ \boldsymbol {\beta} _ {2} = - \frac {\left(\boldsymbol {\alpha} _ {2} , \boldsymbol {\beta} _ {1}\right)}{\left(\boldsymbol {\beta} _ {1} , \boldsymbol {\beta} _ {1}\right)} \boldsymbol {\beta} _ {1} + \boldsymbol {\alpha} _ {2}, \\ \boldsymbol {\beta} _ {3} = - \frac {\left(\boldsymbol {\alpha} _ {3} , \boldsymbol {\beta} _ {1}\right)}{\left(\boldsymbol {\beta} _ {1}, \boldsymbol {\beta} _ {1}\right)} \boldsymbol {\beta} _ {1} - \frac {\left(\boldsymbol {\alpha} _ {3} , \boldsymbol {\beta} _ {2}\right)}{\left(\boldsymbol {\beta} _ {2}, \boldsymbol {\beta} _ {2}\right)} \boldsymbol {\beta} _ {2} + \boldsymbol {\alpha} _ {3}, \dots , \\ \boldsymbol {\beta} _ {n} = \frac {\left(\boldsymbol {\alpha} _ {n} , \boldsymbol {\beta} _ {1}\right)}{\left(\boldsymbol {\beta} _ {1}, \boldsymbol {\beta} _ {1}\right)} \boldsymbol {\beta} _ {1} - \frac {\left(\boldsymbol {\alpha} _ {n} , \boldsymbol {\beta} _ {2}\right)}{\left(\boldsymbol {\beta} _ {2}, \boldsymbol {\beta} _ {2}\right)} \boldsymbol {\beta} _ {2} - \dots - \\ \frac {\left(\boldsymbol {\alpha} _ {n} , \boldsymbol {\beta} _ {n - 1}\right)}{\left(\boldsymbol {\beta} _ {n - 1}, \boldsymbol {\beta} _ {n - 1}\right)} \boldsymbol {\beta} _ {n - 1} + \boldsymbol {\alpha} _ {n}, \\ \end{array}</equation>

则<equation>\beta_{1},\beta_{2},\dots ,\beta_{n}</equation>是一组两两正交的向量组.

---


