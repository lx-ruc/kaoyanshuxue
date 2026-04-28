#### 矩阵的秩

**2018年第6题 | 选择题 | 4分 | 答案: A**

6. 设 A,B为 n阶矩阵，记 r(X)为矩阵 X的秩，(X,Y)表示分块矩阵，则（    ）

A.<equation>r ( A, A B )=r ( A )</equation>B.<equation>r ( A, B A )=r ( A )</equation>C.<equation>r ( A, B )=\max \{ r ( A ) , r ( B ) \}</equation>D.<equation>r ( A, B )=r \left( A^{\mathrm{T}}, B^{\mathrm{T}} \right)</equation>

答案: A

**解析:**解记 C=AB.由于右乘矩阵表示对矩阵作列变换，故 C的列向量可由 A的列向量线性表示.于是，<equation>r ( A, C )=r ( A, A B )=r ( A ).</equation>因此，应选A.

下面分别说明选项B、C、D不正确.

选项B：<equation>r ( \mathbf{A}, \mathbf{B A})\geqslant r (\mathbf{A})</equation>.但是，<equation>r (\mathbf{A}, \mathbf{B A})=r (\mathbf{A})</equation>并不成立.

取<equation>A = \left( \begin{array}{ll}1 & 0\\ 0 & 0 \end{array} \right),B = \left( \begin{array}{ll}1 & 0\\ 1 & 1 \end{array} \right)</equation>，则<equation>BA = \left( \begin{array}{ll}1 & 0\\ 1 & 0 \end{array} \right),(A,BA) = \left( \begin{array}{lll}1 & 0 & 1 & 0\\ 0 & 0 & 1 & 0 \end{array} \right).r(A,BA) = 2</equation>但<equation>r(A) = 1.</equation>选项C：<equation>r ( A, B ) \geqslant\max \left\{r ( A ) , r ( B ) \right\}</equation>.但是，<equation>r ( A, B )=\max \left\{r ( A ) , r ( B ) \right\}</equation>并不成立.

取<equation>A = \left( \begin{array}{ll}1 & 0\\ 0 & 0 \end{array} \right),B = \left( \begin{array}{ll}0 & 0\\ 1 & 0 \end{array} \right)</equation>，则<equation>(A,B) = \left( \begin{array}{lll}1 & 0 & 0 & 0\\ 0 & 0 & 1 & 0 \end{array} \right),r(A,B) = 2</equation>，但<equation>r(A) = r(B) = 1.</equation>选项D：由于<equation>r(\mathbf{P})=r(\mathbf{P}^{\mathrm{T}})</equation>，而<equation>(\mathbf{A},\mathbf{B})^{\mathrm{T}}=\binom{\mathbf{A}^{\mathrm{T}}}{\mathbf{B}^{\mathrm{T}}}</equation>，故<equation>r(\mathbf{A},\mathbf{B})=r\binom{\mathbf{A}^{\mathrm{T}}}{\mathbf{B}^{\mathrm{T}}}</equation>.但是，<equation>r(\mathbf{A},\mathbf{B})=r(\mathbf{A}^{\mathrm{T}},\mathbf{B}^{\mathrm{T}})</equation>并不成立.

取<equation>A=\left( \begin{array}{ll}1&0\\ 0&0 \end{array} \right), B=\left( \begin{array}{ll}0&0\\ 1&0 \end{array} \right)</equation>，则<equation>(\mathbf{A},\mathbf{B})=\left( \begin{array}{llll}1&0&0&0\\ 0&0&1&0 \end{array} \right),(\mathbf{A}^{\mathrm{T}},\mathbf{B}^{\mathrm{T}})=\left( \begin{array}{llll}1&0&0&1\\ 0&0&0&0 \end{array} \right). r(\mathbf{A},\mathbf{B})=2,</equation>但<equation>r(\mathbf{A}^{\mathrm{T}},\mathbf{B}^{\mathrm{T}})=1.</equation>

---

**2017年第13题 | 填空题 | 4分**

13. 设矩阵<equation>A=\left( \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 2 \\ 0 & 1 & 1 \end{array} \right), \alpha_{1},\alpha_{2},\alpha_{3}</equation>为线性无关的3维列向量组，则向量组<equation>A\alpha_{1},A\alpha_{2},A\alpha_{3}</equation>的秩为 ___.

**解析:**由于<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关，故矩阵<equation>\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)</equation>可逆，从而<equation>r \left(A \alpha_ {1}, A \alpha_ {2}, A \alpha_ {3}\right) = r \left(A \left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right)\right) = r (A).</equation>下面我们用三种方法计算<equation>r(A)</equation>.

（法一）计算<equation>| A |</equation>得<equation>| A |=0</equation>，故<equation>r(A)\leqslant 2</equation>.又因为矩阵 A含有一个非零2阶子式，例如<equation>\left| \begin{array}{ll} 1 & 0 \\ 1 & 1 \end{array} \right|=1</equation>，所以<equation>r(A)\geqslant 2</equation>.因此，<equation>r(A)=2</equation>，从而向量组<equation>A\alpha_{1},A\alpha_{2},A\alpha_{3}</equation>的秩为2.

（法二）对矩阵 A作初等行变换将其化为阶梯形矩阵，进而求得其秩.<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 2 \\ 0 & 1 & 1 \end{array} \right) \xrightarrow {r _ {2} - r _ {1}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 1 & 1 \end{array} \right) \xrightarrow {r _ {3} - r _ {2} ^ {*}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）因此，<equation>r ( A ) = 2.</equation>（法三）令<equation>\boldsymbol{\beta}_{1}=(1,1,0)^{\mathrm{T}}</equation><equation>\boldsymbol{\beta}_{2}=(0,1,1)^{\mathrm{T}}</equation><equation>\boldsymbol{\beta}_{3}=(1,2,1)^{\mathrm{T}}</equation>，则<equation>A=(\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3})</equation>.由于<equation>\boldsymbol{\beta}_{1}+\boldsymbol{\beta}_{2}=</equation><equation>\boldsymbol{\beta}_{3}</equation>，故<equation>r(A)\leqslant 2</equation>.又因为<equation>\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2}</equation>线性无关，所以<equation>r(A)\geqslant 2</equation>.因此，<equation>r(A)=2.</equation>

---


## 概率论与数理统计


### 随机变量的数字特征


