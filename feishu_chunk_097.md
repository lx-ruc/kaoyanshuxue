#### 矩阵的相似与相似对角化

**2024年第21题 | 解答题 | 12分**

21. (本题满分12分)

已知数列<equation>\{x_{n}\} ,\{y_{n}\} ,\{z_{n}\}</equation>满足<equation>x_{0}=-1,y_{0}=0,z_{0}=2</equation>，且<equation>\left\{ \begin{array}{l l} x_{n}=-2x_{n-1}+2z_{n-1}, \\ y_{n}=-2y_{n-1}-2z_{n-1}, \\ z_{n}=-6x_{n-1}-3y_{n-1}+3z_{n-1}. \end{array} \right.</equation>记<equation>\alpha_{n}=\left( \begin{array}{l} x_{n} \\ y_{n} \\ z_{n} \end{array} \right)</equation>，写出满

足<equation>\alpha_{n} = A\alpha_{n - 1}</equation>的矩阵<equation>A</equation>，并求<equation>A^{n}</equation>及<equation>x_{n},y_{n},z_{n}</equation>（<equation>n = 1,2,\dots</equation>）.

**答案:**<equation>A = \left( \begin{array}{c c c} - 2 & 0 & 2 \\ 0 & - 2 & - 2 \\ - 6 & - 3 & 3 \end{array} \right)</equation>(2)<equation>\mathbf {A} ^ {n} = \left[ \begin{array}{c c c} - 4 - (- 2) ^ {n} & - 2 - (- 2) ^ {n} & 2 \\ 4 - (- 2) ^ {n + 1} & 2 - (- 2) ^ {n + 1} & - 2 \\ - 6 & - 3 & 3 \end{array} \right].</equation><equation>x _ {n} = 8 + (- 2) ^ {n}, y _ {n} = - 8 + (- 2) ^ {n + 1}, z _ {n} = 1 2 (n = 1, 2, \dots).</equation>

**解析:**21 已知数列<equation>\{x_{n}\}</equation>，<equation>\{y_{n}\}</equation>，<equation>\{z_{n}\}</equation>满足<equation>x_{0}=-1,y_{0}=0,z_{0}=2</equation>，且<equation>\left\{ \begin{array}{l l} x_{n}=-2x_{n-1}+2z_{n-1}, \\ y_{n}=-2y_{n-1}-2z_{n-1}, \\ z_{n}=-6x_{n-1}-3y_{n-1}+3z_{n-1}. \end{array} \right.</equation>记<equation>\boldsymbol{\alpha}_{n}=\left( \begin{array}{c}x_{n}\\ y_{n}\\ z_{n} \end{array} \right)</equation>，写出满足<equation>\boldsymbol{\alpha}_{n}=A\boldsymbol{\alpha}_{n-1}</equation>的矩阵A，并求<equation>A^{n}</equation>及<equation>x_{n},y_{n},z_{n} ( n=1,2,\dots).</equation>分析 本题主要考查矩阵的高次幂的计算.

由<equation>\left\{ \begin{array}{l l} x_{n}=-2x_{n-1}+2z_{n-1}, \\ y_{n}=-2y_{n-1}-2z_{n-1}, \\ z_{n}=-6x_{n-1}-3y_{n-1}+3z_{n-1} \end{array} \right.</equation>可以得到 A的表达式，计算 A的特征值与特征向量，并且将 A

相似对角化得到对角矩阵<equation>\boldsymbol{A}</equation>，即找到可逆矩阵 P，使得<equation>\boldsymbol{A}=\boldsymbol{P}^{-1}\boldsymbol{A}\boldsymbol{P}</equation>，则<equation>\boldsymbol{A}=\boldsymbol{P}\boldsymbol{\Lambda}\boldsymbol{P}^{-1},\boldsymbol{A}^{n}=\boldsymbol{P}\boldsymbol{\Lambda}^{n}\boldsymbol{P}^{-1}.</equation>进一步通过<equation>\alpha_{n}=A\alpha_{n}</equation>，可得<equation>\alpha_{n}=A^{n}\alpha_{0}</equation>，从而可计算出<equation>\alpha_{n}.</equation>解 由<equation>\left\{ \begin{array}{l l} x_{n}=-2 x_{n-1}+2 z_{n-1}, \\ y_{n}=-2 y_{n-1}-2 z_{n-1}, \\ z_{n}=-6 x_{n-1}-3 y_{n-1}+3 z_{n-1} \end{array} \right.</equation>可得<equation>\left( \begin{array}{c} x_{n} \\ y_{n} \\ z_{n} \end{array} \right)=\left( \begin{array}{c c c} -2 & 0 & 2 \\ 0 & -2 & -2 \\ -6 & -3 & 3 \end{array} \right)\left( \begin{array}{c} x_{n-1} \\ y_{n-1} \\ z_{n-1} \end{array} \right),</equation>即<equation>\boldsymbol{\alpha}_{n}=</equation><equation>\left( \begin{array}{c c c} -2 & 0 & 2 \\ 0 & -2 & -2 \\ -6 & -3 & 3 \end{array} \right)\boldsymbol{\alpha}_{n-1}.</equation>于是，<equation>A=\left( \begin{array}{c c c} -2 & 0 & 2 \\ 0 & -2 & -2 \\ -6 & -3 & 3 \end{array} \right).</equation>计算 A的特征值.<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda + 2 & 0 & - 2 \\ 0 & \lambda + 2 & 2 \\ 6 & 3 & \lambda - 3  \right| &= \left| \begin{array}{c c c} \lambda + 2 & \lambda + 2 & 0 \\ 0 & \lambda + 2 & 2 \\ 6 & 3 & \lambda - 3  \right| &= (\lambda + 2) \left| \begin{array}{c c c} 1 & 1 & 0 \\ 0 & \lambda + 2 & 2 \\ 6 & 3 & \lambda - 3  \right| \\ &= (\lambda + 2) \left| \begin{array}{c c c} 1 & 0 & 0 \\ 0 & \lambda + 2 & 2 \\ 6 & - 3 & \lambda - 3  \right| &= (\lambda + 2) \left[ (\lambda + 2) (\lambda - 3) + 6 \right] = \lambda (\lambda - 1) (\lambda + 2). \end{aligned}</equation>A的特征值为-2,1,0.

考虑<equation>(-2 E-A) x=0.</equation><equation>- 2 E-A=\left( \begin{array}{c c c} 0 & 0 & - 2 \\ 0 & 0 & 2 \\ 6 & 3 & - 5 \end{array} \right)\rightarrow\left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 6 & 3 & 0 \end{array} \right)\rightarrow\left( \begin{array}{c c c} 2 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation><equation>\xi_{1}=\left( \begin{array}{c}-1\\ 2\\ 0 \end{array} \right)</equation>为 A的属于特征值-2的一个特征向量.

考虑（<equation>E-A ) x=0.</equation><equation>E - A = \left( \begin{array}{c c c} 3 & 0 & - 2 \\ 0 & 3 & 2 \\ 6 & 3 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 3 & 0 & - 2 \\ 0 & 3 & 2 \\ 0 & 3 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 3 & 0 & - 2 \\ 0 & 3 & 2 \\ 0 & 0 & 0 \end{array} \right).</equation><equation>\xi_{2} = \left( \begin{array}{c}2\\ -2\\ 3 \end{array} \right)</equation>为A的属于特征值1的一个特征向量.

考虑<equation>(0E - A)x = 0</equation>.<equation>-A = \left( \begin{array}{c c c}2&0&-2\\0&2&2\\6&3&-3 \end{array} \right)\rightarrow \left( \begin{array}{c c c}1&0&-1\\0&1&1\\2&1&-1 \end{array} \right)\rightarrow \left( \begin{array}{c c c}1&0&-1\\0&1&1\\0&1&1 \end{array} \right)\rightarrow \left( \begin{array}{c c c}1&0&-1\\0&1&1\\0&0&0 \end{array} \right).</equation><equation>\xi_{3}=\left( \begin{array}{c}1\\ -1\\ 1 \end{array} \right)</equation>为 A的属于特征值0的一个特征向量.

令<equation>P=\left( \begin{array}{c c c} -1 & 2 & 1 \\ 2 & -2 & -1 \\ 0 & 3 & 1 \end{array} \right)</equation>，则<equation>P^{-1} A P=\left( \begin{array}{c c c} -2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right)=A.</equation><equation>P ^ {- 1}</equation><equation>\begin{array}{l} (P, E) = \left( \begin{array}{c c c c c c} - 1 & 2 & 1 & 1 & 0 & 0 \\ 2 & - 2 & - 1 & 0 & 1 & 0 \\ 0 & 3 & 1 & 0 & 0 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 1 & 1 & 0 \\ 2 & - 2 & - 1 & 0 & 1 & 0 \\ 0 & 3 & 1 & 0 & 0 & 1 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 1 & 1 & 0 \\ 0 & - 2 & - 1 & - 2 & - 1 & 0 \\ 0 & 3 & 1 & 0 & 0 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 1 & 1 & 0 \\ 0 & 1 & 0 & - 2 & - 1 & 1 \\ 0 & 3 & 1 & 0 & 0 & 1 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 1 & 1 & 0 \\ 0 & 1 & 0 & - 2 & - 1 & 1 \\ 0 & 0 & 1 & 6 & 3 & - 2 \end{array} \right). \\ \end{array}</equation>于是，<equation>P^{-1}=\left( \begin{array}{c c c} 1 & 1 & 0 \\ -2 & -1 & 1 \\ 6 & 3 & -2 \end{array} \right).</equation>由此可得，<equation>\begin{aligned} \boldsymbol {A} ^ {n} &= \boldsymbol {P} \boldsymbol {A} ^ {n} \boldsymbol {P} ^ {- 1} = \left( \begin{array}{c c c} - 1 & 2 & 1 \\ 2 & - 2 & - 1 \\ 0 & 3 & 1  \right) \left( \begin{array}{c c c} (- 2) ^ {n} & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \left( \begin{array}{c c c} 1 & 1 & 0 \\ - 2 & - 1 & 1 \\ 6 & 3 & - 2  \right) \\ &= \left( \begin{array}{c c c} (- 1) ^ {n - 1} \cdot 2 ^ {n} & 2 & 0 \\ (- 1) ^ {n} \cdot 2 ^ {n + 1} & - 2 & 0 \\ 0 & 3 & 0  \right) \left( \begin{array}{c c c} 1 & 1 & 0 \\ - 2 & - 1 & 1 \\ 6 & 3 & - 2  \right) \\ &= \left( \begin{array}{c c c} (- 1) ^ {n - 1} 2 ^ {n} - 4 & (- 1) ^ {n - 1} 2 ^ {n} - 2 & 2 \\ (- 1) ^ {n} 2 ^ {n + 1} + 4 & (- 1) ^ {n} 2 ^ {n + 1} + 2 & - 2 \\ - 6 & - 3 & 3  \right). \end{aligned}</equation>由<equation>\alpha_{n} = A\alpha_{n - 1}</equation>可得<equation>\alpha_{n} = A^{n}\alpha_{0}</equation>. 因此，<equation>\boldsymbol {\alpha} _ {n} = \left( \begin{array}{c c c} (- 1) ^ {n - 1} 2 ^ {n} - 4 & (- 1) ^ {n - 1} 2 ^ {n} - 2 & 2 \\ (- 1) ^ {n} 2 ^ {n + 1} + 4 & (- 1) ^ {n} 2 ^ {n + 1} + 2 & - 2 \\ - 6 & - 3 & 3 \end{array} \right) \left( \begin{array}{c} - 1 \\ 0 \\ 2 \end{array} \right) = \left( \begin{array}{c} (- 2) ^ {n} + 8 \\ (- 2) ^ {n + 1} - 8 \\ 1 2 \end{array} \right).</equation>从而<equation>x_{n} = (-2)^{n} + 8, y_{n} = (-2)^{n + 1} - 8, z_{n} = 12.</equation>

---

**2023年第6题 | 选择题 | 5分 | 答案: D**

6. 下列矩阵中不能相似于对角矩阵的是（    ）

A.

B.

C.

D.

答案: D

**解析:**<equation>\mathrm {已} A _ {1} = \left( \begin{array}{c c c} 1 & 1 & a \\ 0 & 2 & 2 \\ 0 & 0 & 3 \end{array} \right), A _ {2} = \left( \begin{array}{c c c} 1 & 1 & a \\ 1 & 2 & 0 \\ a & 0 & 3 \end{array} \right), A _ {3} = \left( \begin{array}{c c c} 1 & 1 & a \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{array} \right), A _ {4} = \left( \begin{array}{c c c} 1 & 1 & a \\ 0 & 2 & 2 \\ 0 & 0 & 2 \end{array} \right).</equation>注意到<equation>A_{2}</equation>为实对称矩阵，故必然相似于一个对角矩阵.

由于<equation>A_{1}, A_{3}, A_{4}</equation>均为上三角矩阵，故特征值即它们的对角线元素，从而<equation>A_{1}</equation>的特征值为1，2，3，<equation>A_{3}, A_{4}</equation>的特征值为1，2，2.

由<equation>A_{1}</equation>有3个不同的特征值可知，<equation>A_{1}</equation>相似于一个对角矩阵.

下面我们考虑<equation>A_{3}, A_{4}</equation>是否能相似于对角矩阵.<equation>A_{3}, A_{4}</equation>都有属于特征值1的特征向量<equation>(1,0,0)^{\mathrm{T}}.</equation>由于属于不同特征值的特征向量线性无关，故我们只需判定<equation>A_{3}, A_{4}</equation>的二重特征值2是否具有两个线性无关的特征向量即可确定它们是否一共具有3个线性无关的特征向量，从而相似于对角矩阵.

考虑方程组<equation>(2E - A_{3})x = 0,(2E - A_{4})x = 0.</equation><equation>2 \boldsymbol {E} - \boldsymbol {A} _ {3} = \left( \begin{array}{c c c} 1 & - 1 & - a \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right), \quad 2 \boldsymbol {E} - \boldsymbol {A} _ {4} = \left( \begin{array}{c c c} 1 & - 1 & - a \\ 0 & 0 & - 2 \\ 0 & 0 & 0 \end{array} \right).</equation>由于<equation>r(2E - A_{3}) = 1,r(2E - A_{4}) = 2</equation>，故方程组<equation>(2E - A_{3})x = 0</equation>有两个线性无关的解，从而<equation>A_{3}</equation>有两个线性无关的属于特征值2的特征向量，<equation>A_{3}</equation>相似于对角矩阵，方程组<equation>(2E - A_{4})x = 0</equation>只有一个线性无关的解，从而<equation>A_{4}</equation>只有一个线性无关的属于特征值2的特征向量，<equation>A_{4}</equation>不能相似于对角矩阵因此，应选D.

---

**2022年第5题 | 选择题 | 5分 | 答案: A**

5. 下列四个条件中，3阶矩阵 A可相似对角化的一个充分但不必要条件是（    ）

A. A有3个互不相等的特征值 B. A有3个线性无关的特征向量

C. A有3个两两线性无关的特征向量 D. A的属于不同特征值的特征向量相互正交

答案: A

**解析:**## 解 依次分析四个选项.

选项A是充分非必要条件.若矩阵A具有3个互不相等的特征值，则A有3个线性无关的特征向量，从而能够相似对角化.但是A能相似对角化并不意味着A一定有3个互不相等的特征值.例如3阶单位矩阵E，该矩阵自身即为对角矩阵，但仅有一个三重特征值1，没有不同的特征值.应选A.

选项B是充分必要条件.

选项C是必要非充分条件.若 A能相似对角化，则 A必然有3个线性无关的特征向量，从而有 3个两两线性无关的特征向量.

但反之并不成立，因为3个向量两两线性无关并不意味着3个向量线性无关。要举选项C不充分的例子，可以找到一个具有3重特征值，但却只有两个线性无关的特征向量的3阶矩阵.

取<equation>A = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>，则0是A的3重特征值，<equation>\xi_{1} = \left( \begin{array}{c} 1 \\ 0 \\ 0 \end{array} \right)</equation>和<equation>\xi_{2} = \left( \begin{array}{c} 0 \\ 1 \\ 0 \end{array} \right)</equation>是A的属于特征值0的两个线性无关的特征向量.取<equation>\xi_{3} = \left( \begin{array}{c} 1 \\ 1 \\ 0 \end{array} \right)</equation>，则<equation>\xi_{3}</equation>也是A的属于特征值0的一个特征向量，<equation>\xi_{1},\xi_{2},\xi_{3}</equation>两两线性无关，但是<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性相关，A也不能相似对角化.

选项D既不是充分条件，也不是必要条件。事实上，属于不同特征值的特征向量相互正交是实对称矩阵的性质，与是否可对角化没有直接联系。

下面说明选项D的不必要性.

取<equation>\xi_{1} = \left( \begin{array}{c}1\\ 0\\ 0 \end{array} \right),\xi_{2} = \left( \begin{array}{c}1\\ 1\\ 0 \end{array} \right),\xi_{3} = \left( \begin{array}{c}1\\ 0\\ 1 \end{array} \right)</equation>，则<equation>\xi_{1},\xi_{2},\xi_{3}</equation>两两不正交.令<equation>P = (\xi_{1},\xi_{2},\xi_{3}),A = \left( \begin{array}{c c c}1&0&0\\ 0&-1&0\\ 0&0&0 \end{array} \right)</equation>，则<equation>\boldsymbol {A} = \boldsymbol {P} \boldsymbol {\Lambda} \boldsymbol {P} ^ {- 1} = \left( \begin{array}{c c c} 1 & 1 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right) \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} 1 & - 2 & - 1 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>A与对角矩阵A相似，但是A的属于不同特征值的特征向量均不正交.

若 A是具有3个互不相等的特征值的3阶矩阵，则 A必然可相似对角化，故选项D不充分的例子，可以找只有两个不同特征值，且属于这两个不同特征值的特征向量相互正交，但是却不可以相似对角化的矩阵.

取<equation>A=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right)</equation>. 通过计算可发现该矩阵的特征值为0,1，其中0为二重特征值，但0没有两个线性无关的特征向量，从而 A不能相似对角化.

解<equation>( E-A ) x=0</equation>可得<equation>\xi_{1}=\left( \begin{array}{c} 1 \\ 0 \\ 0 \end{array} \right)</equation>为 A的属于特征值1的一个特征向量. 解<equation>( 0 E-A ) x=0</equation>可得<equation>\xi_{2}=\left( \begin{array}{c} 0 \\ 1 \\ 0 \end{array} \right)</equation>为 A的属于特征值0的一个特征向量.<equation>\xi_{1}</equation>与<equation>\xi_{2}</equation>为 A的属于不同特征值的特征向量，它们正交，且 A的任意属于不同特征值的特征向<equation>\xi_{1}</equation>与<equation>\xi_{2}</equation>为 A的属于不同特征值的特征向量，它们正交，且 A的任意属于不同特征值的特征向量均正交，但是 A不能相似对角化.

---

**2020年第21题 | 解答题 | 11分**

21. (本题满分11分)

设 A为2阶矩阵，<equation>P=(\alpha ,A\alpha)</equation>，其中<equation>\alpha</equation>是非零向量且不是 A的特征向量.

I. 证明 P为可逆矩阵；

II. 若<equation>A^{2}\alpha+A\alpha-6\alpha=0</equation>，求<equation>P^{-1}AP</equation>，并判断 A是否相似于对角矩阵.

**答案:**（I）证明略；

（Ⅱ）<equation>P^{-1} A P=\left( \begin{array}{cc} 0 & 6 \\ 1 & -1 \end{array} \right). A</equation>相似于对角矩阵<equation>\left( \begin{array}{c c} 2 & 0 \\ 0 & -3 \end{array} \right).</equation>

**解析:**解（I）要证明<equation>P</equation>为可逆矩阵，可证明<equation>\alpha, A\alpha</equation>线性无关.

假设<equation>\boldsymbol{\alpha},\boldsymbol{A}\boldsymbol{\alpha}</equation>线性相关，则存在不全为零的常数<equation>k_{1},k_{2}</equation>，使得<equation>k_{1}\boldsymbol{\alpha}+k_{2}\boldsymbol{A}\boldsymbol{\alpha}=\mathbf{0}.</equation>若<equation>k_{2}=0</equation>，则<equation>k_{1}\boldsymbol{\alpha}=\mathbf{0}.</equation>但<equation>\boldsymbol{\alpha}</equation>为非零向量，故<equation>k_{1}=0.</equation>这与假设矛盾.

若<equation>k_{2}\neq 0</equation>，则<equation>A\alpha=-\frac{k_{1}}{k_{2}}\alpha</equation>.由特征向量的定义可知<equation>\alpha</equation>为A的特征向量.这与<equation>\alpha</equation>不是A的特征向量矛盾.

因此，<equation>\alpha ,A\alpha</equation>线性无关.<equation>P</equation>为可逆矩阵.

（Ⅱ）考虑AP.<equation>\begin{aligned} A P &= \left(A \alpha , A ^ {2} \alpha\right) \xlongequal {A ^ {2} \alpha + A \alpha - 6 \alpha = 0} \left(A \alpha , 6 \alpha - A \alpha\right) = (\alpha , A \alpha) \left( \begin{array}{c c} 0 & 6 \\ 1 & - 1  \right) \\ &= P \left( \begin{array}{c c} 0 & 6 \\ 1 & - 1  \right). \end{aligned}</equation>由第（I）问可知，<equation>P</equation>可逆.上式两端同时左乘<equation>P^{-1}</equation>可得<equation>P^{-1} A P=\left( \begin{array}{c c} 0 & 6 \\ 1 & -1 \end{array} \right).</equation>记<equation>B=\left( \begin{array}{c c} 0 & 6 \\ 1 & -1 \end{array} \right)</equation>，则A与B相似.A与对角矩阵相似等价于B与对角矩阵相似计算B的特征多项式.<equation>| \lambda E - B | = \left| \begin{array}{c c} \lambda & - 6 \\ - 1 & \lambda + 1 \end{array} \right| = \lambda^ {2} + \lambda - 6 = (\lambda + 3) (\lambda - 2).</equation>2与-3是B的两个不同特征值.于是，B相似于对角矩阵<equation>\left( \begin{array}{cc}2&0\\ 0&-3 \end{array} \right).</equation>由相似关系的传递性可知，A相似于对角矩阵<equation>\left( \begin{array}{cc}2&0\\ 0&-3 \end{array} \right).</equation>

---

**2019年第21题 | 解答题 | 11分**

21. （本题满分11分）

已知矩阵<equation>A = \left( \begin{array}{c c c} - 2 & - 2 & 1 \\ 2 & x & - 2 \\ 0 & 0 & - 2 \end{array} \right)</equation>与<equation>B = \left( \begin{array}{c c c} 2 & 1 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & y \end{array} \right)</equation>相似.

I. 求 x,y;

II. 求可逆矩阵<equation>P</equation>使得<equation>P^{-1}AP = B</equation>.

**答案:**（I）<equation>x=3,y=-2;</equation>（Ⅱ）满足<equation>P^{-1} A P=B</equation>的可逆矩阵为<equation>P=\left( \begin{array}{c c c} - 1 & - 1 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right).</equation>

**解析:**解（I）由于<equation>A,B</equation>相似，故它们的迹与行列式均相同.

由 A,B有相同的迹可得<equation>- 4 + x = 1 + y</equation>即<equation>x - y = 5.</equation>计算<equation>|A|, |B|</equation>.<equation>B</equation>为上三角矩阵，故易得<equation>|B| = -2y.</equation><equation>| A | \xlongequal {\text {按 第三 行 展 开}} (- 2) \cdot \left| \begin{array}{c c} - 2 & - 2 \\ 2 & x \end{array} \right| = 4 x - 8.</equation>由<equation>|A| = |B|</equation>可得<equation>4x - 8 = -2y</equation>，即<equation>2x + y = 4.</equation>联立<equation>\left\{ \begin{array}{l l} x - y = 5, \\ 2x + y = 4 \end{array} \right.</equation>解得<equation>x = 3,y = -2.</equation>（Ⅱ）由于<equation>A, B</equation>相似，故它们有相同的特征值.

计算 B的特征多项式.<equation>| \lambda E - B | = \left| \begin{array}{c c c} \lambda - 2 & - 1 & 0 \\ 0 & \lambda + 1 & 0 \\ 0 & 0 & \lambda + 2 \end{array} \right| = (\lambda - 2) (\lambda + 1) (\lambda + 2).</equation>于是，<equation>\boldsymbol{B}</equation>的特征值为2，-1，-2.从而<equation>\boldsymbol{A}</equation>的特征值也为2，-1，-2.

由于 A,B具有3个不同的特征值2，-1，-2，故存在可逆矩阵<equation>P_{1}, P_{2}</equation>，使得<equation>P_{1}^{-1} A P_{1}=</equation><equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -2 \end{array} \right), P_{2}^{-1} B P_{2}=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -2 \end{array} \right).</equation><equation>\text {令} \boldsymbol {P} = \boldsymbol {P} _ {1} \boldsymbol {P} _ {2} ^ {- 1}, \text {则} \boldsymbol {P} ^ {- 1} \boldsymbol {A P} = \boldsymbol {P} _ {2} \boldsymbol {P} _ {1} ^ {- 1} \boldsymbol {A P} _ {1} \boldsymbol {P} _ {2} ^ {- 1} = \boldsymbol {P} _ {2} \left(\boldsymbol {P} _ {1} ^ {- 1} \boldsymbol {A P} _ {1}\right) \boldsymbol {P} _ {2} ^ {- 1} = \boldsymbol {B}.</equation><equation>P_{1}</equation>的列向量为A的属于特征值2，-1，-2的特征向量，<equation>P_{2}</equation>的列向量为B的属于特征值2，-1， -2的特征向量.下面分别计算A，B的特征向量.

计算<equation>A</equation>的属于特征值2的特征向量.考虑<equation>(2E - A)x = 0.</equation><equation>2 \boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} 4 & 2 & - 1 \\ - 2 & - 1 & 2 \\ 0 & 0 & 4 \end{array} \right) \xrightarrow [ r _ {1} + r _ {3} ^ {*} ]{r _ {3} \times \frac {1}{4}} \left( \begin{array}{c c c} 4 & 2 & 0 \\ - 2 & - 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {2} ^ {*} \times (- 1) ]{r _ {1} ^ {*} + 2 r _ {2} ^ {*}} \left( \begin{array}{c c c} 0 & 0 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>于是，<equation>r ( 2 E - A ) = 2</equation>，求得<equation>\boldsymbol{\xi}_{1}=(-1,2,0)^{\mathrm{T}}</equation>为<equation>( 2 E-A ) x=0</equation>的一个基础解系.<equation>(-1,2,0)^{\mathrm{T}}</equation>为 A的属于特征值2的特征向量.

计算<equation>A</equation>的属于特征值-1的特征向量.考虑<equation>(- E - A) x = 0.</equation><equation>- \boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} 1 & 2 & - 1 \\ - 2 & - 4 & 2 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {1} + r _ {3} ]{r _ {2} + 2 r _ {1}} \left( \begin{array}{c c c} 1 & 2 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>于是，<equation>r(-E-A)=2</equation>，求得<equation>\boldsymbol{\xi}_{2}=(-2,1,0)^{\mathrm{T}}</equation>为<equation>(-E-A)\boldsymbol{x}=\mathbf{0}</equation>的一个基础解系.<equation>(-2,1,0)^{\mathrm{T}}</equation>为 A的属于特征值-1的特征向量.

计算<equation>A</equation>的属于特征值-2的特征向量.考虑<equation>(-2E - A)x = 0.</equation><equation>- 2 \boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} 0 & 2 & - 1 \\ - 2 & - 5 & 2 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {2} + 2 r _ {1}} \left( \begin{array}{c c c} 0 & 2 & - 1 \\ - 2 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {2} ^ {*} \times (- 2) - r _ {1}} \left( \begin{array}{c c c} 0 & 2 & - 1 \\ 4 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r(-2 E-A)=2</equation>，求得<equation>\boldsymbol{\xi}_{3}=(-1,2,4)^{\mathrm{T}}</equation>为<equation>(-2 E-A) x=0</equation>的一个基础解系.<equation>(-1,2,4)^{\mathrm{T}}</equation>为 A的属于特征值-2的特征向量.<equation>\left( \begin{array}{c c c} - 1 & - 2 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right)</equation>计算 B的属于特征值2的特征向量.考虑<equation>( 2 E-B ) x=0.</equation><equation>2 \boldsymbol {E} - \boldsymbol {B} = \left( \begin{array}{c c c} 0 & - 1 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r ( 2 E-B )=2</equation>，求得<equation>\boldsymbol{\eta}_{1}=(1,0,0)^{\mathrm{T}}</equation>为<equation>( 2 E-B ) x=0</equation>的一个基础解系.<equation>( 1,0,0)^{\mathrm{T}}</equation>为B的属于特征值2的特征向量.

计算<equation>B</equation>的属于特征值-1的特征向量.考虑<equation>(-E - B)x = 0.</equation><equation>- \boldsymbol {E} - \boldsymbol {B} = \left( \begin{array}{c c c} - 3 & - 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {2} \leftrightarrow r _ {3} ]{r _ {1} \times (- 1)} \left( \begin{array}{c c c} 3 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r(-E-B)=2</equation>，求得<equation>\boldsymbol{\eta}_{2}=(-1,3,0)^{\mathrm{T}}</equation>为<equation>(-E-B)\boldsymbol{x}=\mathbf{0}</equation>的一个基础解系.<equation>(-1,3,0)^{\mathrm{T}}</equation>为 B的属于特征值-1的特征向量.

计算<equation>B</equation>的属于特征值-2的特征向量.考虑<equation>(-2E - B)x = 0.</equation><equation>- 2 \boldsymbol {E} - \boldsymbol {B} = \left( \begin{array}{c c c} - 4 & - 1 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {2} \times (- 1) ]{r _ {1} \times (- 1)} \left( \begin{array}{c c c} 4 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r(-2 E-B)=2</equation>，求得<equation>\boldsymbol{\eta}_{3}=(0,0,1)^{\mathrm{T}}</equation>为<equation>(-2 E-B) x=0</equation>的一个基础解系.<equation>(0,0,1)^{\mathrm{T}}</equation>为 B的属于特征值-2的特征向量.

因此，<equation>P_{2}</equation>可取为<equation>\left( \begin{array}{c c c} 1 & -1 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>利用初等变换法计算<equation>P_{2}^{-1}</equation><equation>\left(\boldsymbol {P} _ {2}, \boldsymbol {E}\right) = \left( \begin{array}{c c c c c c} 1 & - 1 & 0 & 1 & 0 & 0 \\ 0 & 3 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {1} + r _ {2} ^ {*} ]{r _ {2} \times \frac {1}{3}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 1 & \frac {1}{3} & 0 \\ 0 & 1 & 0 & 0 & \frac {1}{3} & 0 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right).</equation>于是，<equation>P_{2}^{-1} = \left( \begin{array}{c c c} 1 & \frac{1}{3} & 0 \\ 0 & \frac{1}{3} & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>综上所述，<equation>\boldsymbol {P} = \boldsymbol {P} _ {1} \boldsymbol {P} _ {2} ^ {- 1} = \left( \begin{array}{c c c} - 1 & - 2 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right) \left( \begin{array}{c c c} 1 & \frac {1}{3} & 0 \\ 0 & \frac {1}{3} & 0 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} - 1 & - 1 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right).</equation>

---

**2018年第5题 | 选择题 | 4分 | 答案: A**

5. 下列矩阵中，与矩阵<equation>\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>A.

相似的为（    ）<equation>\left( \begin{array}{c c c} 1 & 1 & - 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c} 1 & 1 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>

答案: A

**解析:**解 已知矩阵与四个选项中的矩阵的特征多项式均为<equation>( x-1 )^{3}</equation>，故1为这五个矩阵的三重特征值.

记<equation>A = \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E - A = \left( \begin{array}{c c c} 0 & -1 & 0 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r(E - A) = 2.</equation>记<equation>B_{1} = \left( \begin{array}{c c c} 1 & 1 & -1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E - B_{1} = \left( \begin{array}{c c c} 0 & -1 & 1 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r(E - B_{1}) = 2.</equation>记<equation>B_{2} = \left( \begin{array}{c c c} 1 & 0 & -1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E - B_{2} = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r(E - B_{2}) = 1.</equation>记<equation>B_{3} = \left( \begin{array}{c c c} 1 & 1 & -1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E - B_{3} = \left( \begin{array}{c c c} 0 & -1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r(E - B_{3}) = 1.</equation>记<equation>B_{4} = \left( \begin{array}{c c c} 1 & 0 & -1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E - B_{4} = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r(E - B_{4}) = 1.</equation>由上可见，只有<equation>E - B_{1}</equation>与<equation>E - A</equation>的秩相等，而<equation>E - B_{i} ( i = 2,3,4)</equation>与<equation>E - A</equation>的秩均不相等，故<equation>E - B_{i} ( i = 2,3,4)</equation>与<equation>E - A</equation>不相似，从而A与<equation>B_{i} ( i = 2,3,4)</equation>不相似.

由排除法可知，应选A.

---

**2017年第6题 | 选择题 | 4分 | 答案: B**

6. 已知矩阵<equation>A = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 1 \end{array} \right), B = \left( \begin{array}{c c c} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right), C = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{array} \right),</equation>则（    ）

A. A与C相似，B与C相似 B. A与C相似，B与C不相似

C. A与C不相似，B与C相似 D. A与C不相似，B与C不相似

答案: B

**解析:**解求得 A,B,C的特征多项式，均为<equation>(\lambda-2)^{2} (\lambda-1)</equation>，故 A,B,C具有相同的特征值，其中2是二重特征值.

矩阵<equation>C</equation>是对角矩阵，故其相似于其自身.

考虑属于特征值2的特征向量.<equation>2 \boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 0 & - 1 \\ 0 & 0 & 1 \end{array} \right), \quad 2 \boldsymbol {E} - \boldsymbol {B} = \left( \begin{array}{c c c} 0 & - 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>由上可知，<equation>r ( 2 E-A )=1</equation><equation>r ( 2 E-B )=2</equation>.于是，<equation>( 2 E-A ) x=0</equation>的基础解系包含两个向量，A有2个线性无关的属于特征值2的特征向量；而<equation>( 2 E-B ) x=0</equation>的基础解系只包含一个向量，B只有1个线性无关的属于特征值2的特征向量.

因此，加上属于特征值1的特征向量，A共有3个线性无关的特征向量，A与C相似；B只有2个线性无关的特征向量，B与C不相似.应选B.

---

**2016年第5题 | 选择题 | 4分 | 答案: C**

5. 设 A,B是可逆矩阵，且 A与 B相似，则下列结论错误的是（    ）

A.<equation>A^{\mathrm{T}}</equation>与<equation>B^{\mathrm{T}}</equation>相似 B.<equation>A^{-1}</equation>与<equation>B^{-1}</equation>相似

C.<equation>A+A^{\mathrm{T}}</equation>与<equation>B+B^{\mathrm{T}}</equation>相似 D.<equation>A+A^{-1}</equation>与<equation>B+B^{-1}</equation>相似

答案: C

**解析:**解 由于<equation>A</equation>与<equation>B</equation>相似，故存在可逆矩阵<equation>P</equation>，使得<equation>B = P^{-1}AP</equation>-<equation>\boldsymbol{B}^{\mathrm{T}}=\boldsymbol{P}^{\mathrm{T}}\boldsymbol{A}^{\mathrm{T}}(\boldsymbol{P}^{-1})^{\mathrm{T}}=\boldsymbol{P}^{\mathrm{T}}\boldsymbol{A}^{\mathrm{T}}(\boldsymbol{P}^{\mathrm{T}})^{-1}</equation>，选项A中的结论正确.

-<equation>B^{-1}=P^{-1} A^{-1} \left(P^{-1}\right)^{-1}=P^{-1} A^{-1} P</equation>，选项B中的结论正确.

- 由<equation>B=P^{-1} A P</equation>和<equation>B^{-1}=P^{-1} A^{-1} P</equation>可知，<equation>B+B^{-1}=P^{-1}(A+A^{-1}) P</equation>，选项D中的结论正确由排除法可知，应选C.

下面我们举例说明选项C不正确.

设<equation>A = \left( \begin{array}{cc}1 & 0\\ 0 & -1 \end{array} \right),P = \left( \begin{array}{cc}1 & 1\\ 2 & 1 \end{array} \right)</equation>，则<equation>P^{-1} = \left( \begin{array}{c c} - 1 & 1\\ 2 & -1 \end{array} \right)</equation>. 令<equation>\boldsymbol {B} = \boldsymbol {P} ^ {- 1} \boldsymbol {A P} = \left( \begin{array}{c c} - 1 & 1 \\ 2 & - 1 \end{array} \right) \left( \begin{array}{c c} 1 & 0 \\ 0 & - 1 \end{array} \right) \left( \begin{array}{c c} 1 & 1 \\ 2 & 1 \end{array} \right) = \left( \begin{array}{c c} - 3 & - 2 \\ 4 & 3 \end{array} \right),</equation>则<equation>\boldsymbol {A} + \boldsymbol {A} ^ {\mathrm {T}} = \left( \begin{array}{c c} 2 & 0 \\ 0 & - 2 \end{array} \right), \quad \boldsymbol {B} + \boldsymbol {B} ^ {\mathrm {T}} = \left( \begin{array}{c c} - 6 & 2 \\ 2 & 6 \end{array} \right).</equation>计算<equation>A + A^{\mathrm{T}}</equation>的特征多项式得<equation>\lambda^2 - 4</equation>，计算<equation>B + B^{\mathrm{T}}</equation>的特征多项式得<equation>\lambda^2 - 40</equation>因此，<equation>A + A^{\mathrm{T}}</equation>和<equation>B + B^{\mathrm{T}}</equation>不相似.

---

**2016年第21题 | 解答题 | 11分**

21. （本题满分11分）

已知矩阵<equation>A = \left( \begin{array}{c c c} 0 & -1 & 1 \\ 2 & -3 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>I. 求<equation>A^{99}</equation>;

II. 设3阶矩阵<equation>B=(\alpha_{1},\alpha_{2},\alpha_{3})</equation>满足<equation>B^{2}=B A</equation>记<equation>B^{100}=(\beta_{1},\beta_{2},\beta_{3})</equation>将<equation>\beta_{1},\beta_{2},\beta_{3}</equation>分别表示为<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>的线性组合.

**答案:**<equation>\begin{aligned} (\mathrm {I}) \boldsymbol {A} ^ {9 9} &= \left( \begin{array}{c c c} 2 ^ {9 9} - 2 & 1 - 2 ^ {9 9} & 2 - 2 ^ {9 8} \\ 2 ^ {1 0 0} - 2 & 1 - 2 ^ {1 0 0} & 2 - 2 ^ {9 9} \\ 0 & 0 & 0  \right). \\ (\mathrm {I I}) \boldsymbol {\beta} _ {1} &= \left(2 ^ {9 9} - 2\right) \boldsymbol {\alpha} _ {1} + \left(2 ^ {1 0 0} - 2\right) \boldsymbol {\alpha} _ {2}, \boldsymbol {\beta} _ {2} = \left(1 - 2 ^ {9 9}\right) \boldsymbol {\alpha} _ {1} + \left(1 - 2 ^ {1 0 0}\right) \boldsymbol {\alpha} _ {2}, \boldsymbol {\beta} _ {3} = \left(2 - 2 ^ {9 8}\right) \boldsymbol {\alpha} _ {1} + \left(2 - 2 ^ {9 9}\right) \boldsymbol {\alpha} _ {2}. \end{aligned}</equation>

**解析:**（I）计算<equation>A</equation>的特征多项式<equation>|\lambda E - A|</equation>.<equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda & 1 & - 1 \\ - 2 & \lambda + 3 & 0 \\ 0 & 0 & \lambda \end{array} \right| \xlongequal {\text {按 第三 行 展开}} \lambda \left(\lambda^ {2} + 3 \lambda + 2\right) = \lambda (\lambda + 1) (\lambda + 2).</equation>因此，<equation>\mathbf{A}</equation>有3个不同的特征值：-2，-1，0.

由于属于不同特征值的特征向量线性无关，故A有3个线性无关的特征向量，A相似于对角矩阵<equation>\left( \begin{array}{c c c} - 2 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>分别计算 A的属于特征值-2，-1，0的特征向量.

当<equation>\lambda=-2</equation>时，解<equation>(-2 E-A) x=0.</equation>由于<equation>- 2 \boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} - 2 & 1 & - 1 \\ - 2 & 1 & 0 \\ 0 & 0 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} - 2 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right),</equation>故<equation>(1,2,0)^{\mathrm{T}}</equation>为<equation>A</equation>的属于特征值-2的一个特征向量.

当<equation>\lambda=-1</equation>时，解<equation>(-E-A)x=0.</equation>由于<equation>- \boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} - 1 & 1 & - 1 \\ - 2 & 2 & 0 \\ 0 & 0 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right),</equation>故<equation>(1,1,0)^{\mathrm{T}}</equation>为<equation>A</equation>的属于特征值-1的一个特征向量.

当<equation>\lambda=0</equation>时，解<equation>( 0 E-A ) x=0</equation>.由于<equation>0 E - A = \left( \begin{array}{c c c} 0 & 1 & - 1 \\ - 2 & 3 & 0 \\ 0 & 0 & 0 \end{array} \right),</equation>故<equation>(3,2,2)^{\mathrm{T}}</equation>为<equation>A</equation>的属于特征值0的一个特征向量.

令<equation>P = \left( \begin{array}{c c c} 1 & 1 & 3 \\ 2 & 1 & 2 \\ 0 & 0 & 2 \end{array} \right)</equation>，则<equation>P^{-1} A P = \left( \begin{array}{c c c} - 2 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>.

计算<equation>P^{-1}</equation>得，<equation>P^{-1} = \left( \begin{array}{c c c} - 1 & 1 & \frac{1}{2} \\ 2 & - 1 & - 2 \\ 0 & 0 & \frac{1}{2} \end{array} \right).</equation><equation>\begin{aligned} \boldsymbol {A} ^ {9 9} &= \boldsymbol {P} \left( \begin{array}{c c c} (- 2) ^ {9 9} & 0 & 0 \\ 0 & (- 1) ^ {9 9} & 0 \\ 0 & 0 & 0  \right) \boldsymbol {P} ^ {- 1} &= \left( \begin{array}{c c c} 1 & 1 & 3 \\ 2 & 1 & 2 \\ 0 & 0 & 2  \right) \left( \begin{array}{c c c} - 2 ^ {9 9} & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0  \right) \left( \begin{array}{c c c} - 1 & 1 & \frac {1}{2} \\ 2 & - 1 & - 2 \\ 0 & 0 & \frac {1}{2}  \right) \\ &= \left( \begin{array}{c c c} 2 ^ {9 9} - 2 & 1 - 2 ^ {9 9} & 2 - 2 ^ {9 8} \\ 2 ^ {1 0 0} - 2 & 1 - 2 ^ {1 0 0} & 2 - 2 ^ {9 9} \\ 0 & 0 & 0  \right). \end{aligned}</equation>（Ⅱ）先求<equation>B^{100}.</equation>由于<equation>B^{2}=B A</equation>，故<equation>\boldsymbol {B} ^ {3} = \boldsymbol {B} \left(\boldsymbol {B} ^ {2}\right) = \boldsymbol {B} (\boldsymbol {B A}) = \boldsymbol {B} ^ {2} \boldsymbol {A} = (\boldsymbol {B A}) \boldsymbol {A} = \boldsymbol {B A} ^ {2}.</equation>下面我们用数学归纳法证明<equation>B^{n}=B A^{n-1}, n=2, 3, \dots .</equation>当<equation>n = 2</equation>时，<equation>B^{2} = BA</equation>假设该命题对<equation>n = k</equation>成立，下面证明该命题对<equation>n = k + 1</equation>也成立.<equation>\boldsymbol {B} ^ {n} = \boldsymbol {B} ^ {k + 1} = \boldsymbol {B} \boldsymbol {B} ^ {k} \xlongequal {\text {归 纳 假 设}} \boldsymbol {B} \left(\boldsymbol {B} \boldsymbol {A} ^ {k - 1}\right) = \boldsymbol {B} ^ {2} \boldsymbol {A} ^ {k - 1} = (\boldsymbol {B} \boldsymbol {A}) \boldsymbol {A} ^ {k - 1} = \boldsymbol {B} \boldsymbol {A} ^ {k} = \boldsymbol {B} \boldsymbol {A} ^ {n - 1}.</equation>于是，该命题对 n=k+1也成立，从而由数学归纳法可知，该命题对所有<equation>\geqslant2</equation>的正整数均成立因此，<equation>\left(\boldsymbol {\beta} _ {1}, \boldsymbol {\beta} _ {2}, \boldsymbol {\beta} _ {3}\right) = \boldsymbol {B} ^ {1 0 0} = \boldsymbol {B A} ^ {9 9} = \left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\alpha} _ {2}, \boldsymbol {\alpha} _ {3}\right) \left( \begin{array}{c c c} 2 ^ {9 9} - 2 & 1 - 2 ^ {9 9} & 2 - 2 ^ {9 8} \\ 2 ^ {1 0 0} - 2 & 1 - 2 ^ {1 0 0} & 2 - 2 ^ {9 9} \\ 0 & 0 & 0 \end{array} \right).</equation>综上所述，<equation>\boldsymbol {\beta} _ {1} = \left(2 ^ {9 9} - 2\right) \boldsymbol {\alpha} _ {1} + \left(2 ^ {1 0 0} - 2\right) \boldsymbol {\alpha} _ {2},</equation><equation>\begin{aligned} \boldsymbol {\beta} _ {2} &= \left(1 - 2 ^ {9 9}\right) \boldsymbol {\alpha} _ {1} + \left(1 - 2 ^ {1 0 0}\right) \boldsymbol {\alpha} _ {2}, \\ \boldsymbol {\beta} _ {3} &= \left(2 - 2 ^ {9 8}\right) \boldsymbol {\alpha} _ {1} + \left(2 - 2 ^ {9 9}\right) \boldsymbol {\alpha} _ {2}. \end{aligned}</equation>

---

**2015年第21题 | 解答题 | 11分**

21. (本题满分11分)

设矩阵<equation>A = \left( \begin{array}{c c c} 0 & 2 & -3 \\ -1 & 3 & -3 \\ 1 & -2 & a \end{array} \right)</equation>相似于矩阵<equation>B = \left( \begin{array}{c c c} 1 & -2 & 0 \\ 0 & b & 0 \\ 0 & 3 & 1 \end{array} \right).</equation>I. 求 a,b的值；

II. 求可逆矩阵<equation>P</equation>，使<equation>P^{-1}AP</equation>为对角矩阵.

**答案:**(21) （I）<equation>a=4,b=5;</equation><equation>(\mathrm {I I}) \boldsymbol {P} = \left( \begin{array}{c c c} - 1 & 2 & - 3 \\ - 1 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right), \boldsymbol {P} ^ {- 1} \boldsymbol {A} \boldsymbol {P} = \left( \begin{array}{c c c} 5 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>

**解析:**解（I）由于 A,B相似，故存在可逆矩阵Q使得<equation>Q^{-1} A Q=B</equation>，从而<equation>|B|=|Q^{-1}| \cdot |A| \cdot</equation><equation>|Q|=|A|.</equation>计算得<equation>|A|=2 a-3,|B|=b.</equation>另一方面，A和B具有相同的迹，故<equation>3+a=2+b.</equation>联立得<equation>\left\{ \begin{array}{l l} a+3=b+2, \\ 2 a-3=b, \end{array} \right.</equation>解得<equation>\left\{ \begin{array}{l l} a=4, \\ b=5. \end{array} \right.</equation>（Ⅱ）由题设和第（Ⅰ）问得，<equation>| \lambda E - B | = \left| \begin{array}{c c c} \lambda - 1 & 2 & 0 \\ 0 & \lambda - 5 & 0 \\ 0 & - 3 & \lambda - 1 \end{array} \right| = (\lambda - 1) ^ {2} (\lambda - 5).</equation>从而<equation>B</equation>的特征值为1,1,5.由于<equation>A</equation>和<equation>B</equation>相似，故<equation>A</equation>的特征值也为1,1,5.

由第（I）问可得，<equation>A = \left( \begin{array}{c c c} 0 & 2 & -3 \\ -1 & 3 & -3 \\ 1 & -2 & 4 \end{array} \right).</equation>考虑<equation>A</equation>的属于特征值5的特征向量.<equation>\begin{array}{l} 5 E - A = \left( \begin{array}{c c c} 5 & - 2 & 3 \\ 1 & 2 & 3 \\ - 1 & 2 & 1 \end{array} \right) \xrightarrow [ r _ {2} ^ {*} \times \frac {1}{2} ]{r _ {2} - r _ {3}} \left( \begin{array}{c c c} 5 & - 2 & 3 \\ 1 & 0 & 1 \\ - 1 & 2 & 1 \end{array} \right) \xrightarrow [ r _ {3} ^ {*} \times \frac {1}{2} ]{r _ {3} + r _ {2} ^ {* *}} \left( \begin{array}{c c c} 5 & - 2 & 3 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} - 5 r _ {2} ^ {* *} + 2 r _ {3} ^ {* *}} \left( \begin{array}{c c c} 0 & 0 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right). \\ \end{array}</equation>于是，<equation>r ( 5 E - A ) = 2</equation>，求得<equation>\boldsymbol{\xi}_{1}=(-1,-1,1)^{\mathrm{T}}</equation>为<equation>( 5 E - A ) x = 0</equation>的一个基础解系<equation>(-1,-1,1)^{\mathrm{T}}</equation>为A的属于特征值5的一个特征向量.

考虑<equation>A</equation>的属于特征值1的特征向量.<equation>\boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} 1 & - 2 & 3 \\ 1 & - 2 & 3 \\ - 1 & 2 & - 3 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & - 2 & 3 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r ( E - A ) = 1</equation>，求得<equation>\boldsymbol{\xi}_{2} = ( 2,1,0 )^{\mathrm{T}}</equation>和<equation>\boldsymbol{\xi}_{3} = (-3,0,1)^{\mathrm{T}}</equation>为<equation>( E - A ) x = 0</equation>的一个基础解系<equation>( 2,1,0 )^{\mathrm{T}}</equation>和<equation>(-3,0,1)^{\mathrm{T}}</equation>为A的属于特征值1的两个线性无关的特征向量.

取<equation>P = \left( \begin{array}{c c c} - 1 & 2 & - 3 \\ - 1 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right)</equation>，则<equation>P^{-1}AP = \left( \begin{array}{c c c} 5 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>.

---

**2014年第21题 | 解答题 | 11分**

21. (本题满分11分)

证明 n阶矩阵

相似.

**答案:**(21) 证明略

**解析:**证（法一）记<equation>A=\left( \begin{array}{c c c c} 1 & 1 & \dots & 1 \\ 1 & 1 & \dots & 1 \\ \vdots & \vdots & & \vdots \\ 1 & 1 & \dots & 1 \end{array} \right), B=\left( \begin{array}{c c c c} 0 & \dots & 0 & 1 \\ 0 & \dots & 0 & 2 \\ \vdots & & \vdots & \vdots \\ 0 & \dots & 0 & n \end{array} \right).</equation>由观察可知，<equation>r ( \mathbf{A} )=1</equation>，<equation>\operatorname{t r} ( \mathbf{A} )=n</equation>. 又由于 A为实对称矩阵，故必相似于对角矩阵.由相似的矩阵具有相同的秩和迹可知，A相似于秩为1，迹为 n的对角矩阵，不妨记为<equation>\left( \begin{array}{c c c c} n & & & \\ & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right).</equation>另一方面，计算<equation>B</equation>的特征多项式得，<equation>| \lambda E - B | = \left| \begin{array}{c c c c} \lambda & 0 & \dots & - 1 \\ 0 & \lambda & & - 2 \\ \vdots & & \ddots & \vdots \\ 0 & \dots & 0 & \lambda - n \end{array} \right| = \lambda^ {n - 1} (\lambda - n).</equation>B的特征值为<equation>n,0,\dots ,0</equation>，其中0为<equation>n - 1</equation>重特征值.

由于<equation>0 E - B = \left( \begin{array}{c c c c} 0 & & & - 1 \\ & 0 & & - 2 \\ & & \ddots & \vdots \\ & & & - n \end{array} \right)</equation>，故<equation>r(0 E - B) = 1</equation>，从而<equation>(0 E - B) x = 0</equation>的解集的秩为<equation>n - 1</equation><equation>(0 E - B) x = 0</equation>有 n-1个线性无关的解.

B有 n-1个属于特征值0的线性无关的特征向量，再加上B的属于n的特征向量，B共有n个线性无关的特征向量.从而B也相似于<equation>\left( \begin{array}{c c c c} n & & & \\ & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right).</equation>因此，存在可逆矩阵 P，Q，使得<equation>P^{-1} A P=Q^{-1} B Q=\left( \begin{array}{c c c c} n & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right).</equation>于是<equation>Q P^{-1} A P Q^{-1}=B.</equation>令<equation>U=P Q^{-1}</equation>，则<equation>B=U^{-1} A U,A</equation>和B相似.

（法二）计算 A的特征多项式.<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c c} \lambda - 1 & - 1 & \dots & - 1 \\ - 1 & \lambda - 1 & \dots & - 1 \\ \vdots & \vdots & & \vdots \\ - 1 & - 1 & \dots & \lambda - 1  \right| \frac {c _ {1} + \left(c _ {2} + c _ {3} + \dots + c _ {n}\right)}{\overline {{}}} \left| \begin{array}{c c c c} \lambda - n & - 1 & \dots & - 1 \\ \lambda - n & \lambda - 1 & \dots & - 1 \\ \vdots & \vdots & & \vdots \\ \lambda - n & - 1 & \dots & \lambda - 1  \right| \\ &= (\lambda - n) \left| \begin{array}{c c c c} 1 & - 1 & \dots & - 1 \\ 1 & \lambda - 1 & \dots & - 1 \\ \vdots & \vdots & & \vdots \\ 1 & - 1 & \dots & \lambda - 1  \right| \frac {c _ {i} + c _ {1}}{i = 2 , \dots , n} (\lambda - n) \left| \begin{array}{c c c c} 1 & 0 & \dots & 0 \\ 1 & \lambda & \dots & 0 \\ \vdots & \vdots & & \vdots \\ 1 & 0 & \dots & \lambda  \right| \\ &= \lambda^ {n - 1} (\lambda - n). \end{aligned}</equation>由于 A为实对称矩阵，故由 A的特征多项式为<equation>\lambda^{n-1} (\lambda-n)</equation>可知 A相似于对角矩阵<equation>\left( \begin{array}{c c c c} n & & & \\ & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right).</equation>其余同法一.

---

**2013年第6题 | 选择题 | 4分 | 答案: B**

6. 矩阵

相似的充分必要条件为（    ）

A. a=0,b=2 B. a=0,b为任意常数 C. a=2,b=0 D. a=2,b为任意常数

答案: B

**解析:**解 矩阵<equation>\left( \begin{array}{c c c}1&a&1\\ a&b&a\\ 1&a&1 \end{array} \right)</equation>与<equation>\left( \begin{array}{c c c}2&0&0\\ 0&b&0\\ 0&0&0 \end{array} \right)</equation>均为实对称矩阵，故它们相似等价于它们有相同的特征多项式.

矩阵<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>的特征多项式为<equation>f (\lambda) = \lambda (\lambda - 2) (\lambda - b).</equation>考虑<equation>A = \left( \begin{array}{c c c} 1 & a & 1 \\ a & b & a \\ 1 & a & 1 \end{array} \right)</equation>的特征多项式<equation>g(\lambda)</equation>.<equation>g (\lambda) = | \lambda E - A | = \left| \begin{array}{c c c} \lambda - 1 & - a & - 1 \\ - a & \lambda - b & - a \\ - 1 & - a & \lambda - 1 \end{array} \right| = \lambda \left[ (\lambda - 2) (\lambda - b) - 2 a ^ {2} \right].</equation>由于<equation>f(\lambda)-g(\lambda)=2 a^{2}\lambda</equation>，故<equation>f(\lambda)=g(\lambda)</equation>当且仅当 a=0.由于上述论证不涉及到b，故b取任意常数均不影响结果.应选B.

---

**2010年第6题 | 选择题 | 4分 | 答案: D**

6. 设 A为4阶实对称矩阵，且<equation>A^{2}+A=O</equation>. 若 A的秩为3，则 A相似于（    ）

A.<equation>\left( \begin{array}{c c c c} 1 & & \\ & 1 & \\ & & 1 \\ & & 0 \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c c} 1 & & \\ & 1 & \\ & & - 1 \\ & & 0 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c c} 1 & & \\ & - 1 & \\ & & - 1 \\ & & 0 \end{array} \right).</equation>D.<equation>\left( \begin{array}{c c c c} - 1 & & \\ & - 1 & \\ & & - 1 \\ & & 0 \end{array} \right)</equation>

答案: D

**解析:**解（法一）不妨设<equation>\lambda</equation>为 A的特征值，<equation>\alpha</equation>为其相应的特征向量.由<equation>A^{2}+A=O</equation>得<equation>(A^{2}+A)\alpha=0.</equation>代入<equation>A\alpha=\lambda\alpha</equation>得，<equation>(\lambda^{2}+\lambda)\alpha=0.</equation>又由于<equation>\alpha</equation>非零，故<equation>\lambda^{2}+\lambda=0,\lambda=0</equation>或<equation>\lambda=-1.</equation>由于<equation>A</equation>为实对称矩阵，故<equation>A</equation>相似于对角矩阵.又因为<equation>r(A) = 3</equation>，所以对角矩阵的秩也为3，<equation>\lambda = -1</equation>是<equation>A</equation>的三重特征值，<equation>A</equation>相似于<equation>\left( \begin{array}{c c c c} - 1 & & & \\ & - 1 & & \\ & & - 1 & \\ & & & 0 \end{array} \right)</equation>.应选D.

（法二）由于 A为实对称矩阵，故存在可逆矩阵 P使得<equation>P^{-1} A P=\left( \begin{array}{c c c c} \lambda_{1} & & & \\ & \lambda_{2} & & \\ & & \lambda_{3} & \\ & & & \lambda_{4} \end{array} \right)</equation>从而<equation>\begin{aligned} \boldsymbol {O} &= \boldsymbol {A} ^ {2} + \boldsymbol {A} = \boldsymbol {P} \left( \begin{array}{c c c c} \lambda_ {1} ^ {2} & & & \\ & \lambda_ {2} ^ {2} & & \\ & & \lambda_ {3} ^ {2} & \\ & & & \lambda_ {4} ^ {2}  \right) \boldsymbol {P} ^ {- 1} + \boldsymbol {P} \left( \begin{array}{c c c c} \lambda_ {1} & & & \\ & \lambda_ {2} & & \\ & & \lambda_ {3} & \\ & & & \lambda_ {4}  \right) \boldsymbol {P} ^ {- 1} \\ &= \boldsymbol {P} \left( \begin{array}{c c c c} \lambda_ {1} ^ {2} + \lambda_ {1} & & & \\ & \lambda_ {2} ^ {2} + \lambda_ {2} & & \\ & & \lambda_ {3} ^ {2} + \lambda_ {3} & \\ & & & \lambda_ {4} ^ {2} + \lambda_ {4}  \right) \boldsymbol {P} ^ {- 1}. \end{aligned}</equation>因此<equation>\lambda_{i}^{2}+\lambda_{i}=0 ( i=1,2,3,4).</equation>解得<equation>\lambda_{i}=0</equation>或<equation>\lambda_{i}=-1 ( i=1,2,3,4).</equation>又由于<equation>r ( A )=3</equation>故 A相似于<equation>\left( \begin{array}{c c c c} - 1 & & & \\ & - 1 & & \\ & & - 1 & \\ & & & 0 \end{array} \right).</equation>应选D.

---


### 向量


