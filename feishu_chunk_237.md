#### 1. 分块矩阵的定义

<equation>\textcircled{2} r ( A_{m \times n} ) \leqslant\min \{ m,n \} ;</equation>

<equation>\textcircled{3}</equation><equation>r(\mathbf{A}) = 0 \Leftrightarrow \mathbf{A} = \mathbf{O}</equation>;

<equation>\textcircled{4}</equation><equation>r(k\mathbf{A}) = \left\{ \begin{array}{ll} r(\mathbf{A}), & k \neq 0, \\ 0, & k = 0; \end{array} \right.</equation>

<equation>\textcircled{5} r(\mathbf{A} + \mathbf{B}) \leqslant r(\mathbf{A}) + r(\mathbf{B})</equation>;

<equation>\textcircled{6} r ( \mathbf{A B} ) \leqslant\min \{ r ( \mathbf{A} ) , r ( \mathbf{B} ) \} ;</equation>

<equation>\textcircled{7}</equation>若有矩阵<equation>A_{m\times n}, B_{n\times s}</equation>，且<equation>AB = O</equation>，且<equation>r(A) + r(B) \leqslant n</equation>；

<equation>\textcircled{8}</equation>若<equation>P, Q</equation>为满秩方阵，则

<equation>r (P A) = r (A) = r (A Q) = r (P A Q);</equation>

<equation>\textcircled{9}</equation>初等变换不改变矩阵的秩. 若<equation>B</equation>是阶梯形矩阵，则<equation>r(B)</equation>等于<equation>B</equation>中非零行的个数；

<equation>\textcircled{10}</equation>关于伴随矩阵<equation>A^{*}</equation>的秩：

<equation>r \left(\boldsymbol {A} ^ {*}\right) = \left\{ \begin{array}{l l} n, r (\boldsymbol {A}) = n, \\ 1, r (\boldsymbol {A}) = n - 1, \\ 0, r (\boldsymbol {A}) \leqslant n - 2. \end{array} \right.</equation>


用贯穿矩阵的横线和纵线（称为分划线）把一个矩阵分成若干小块，每一小块称为原矩阵的子块，一般记作<equation>A_{ij}</equation>，分为子块的矩阵叫做分块矩阵。由于不同的需要，同一矩阵可以有不同的分块方法。例如：

---


