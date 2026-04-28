#### 向量组的线性相关性

**2024年第6题 | 选择题 | 5分 | 答案: D**
6. 设向量<equation>\alpha_{1}=\left( \begin{array}{c} a \\ 1 \\ -1 \\ 1 \end{array} \right),\alpha_{2}=\left( \begin{array}{c} 1 \\ 1 \\ b \\ a \end{array} \right),\alpha_{3}=\left( \begin{array}{c} 1 \\ a \\ -1 \\ 1 \end{array} \right)</equation>若<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性相关，且其中任意两个向量均线性无关，则（    ）

A. a=1,b≠-1 B. a=1,b=-1 C. a≠-2,b=2 D. a=-2,b=2
答案: D
**解析: **解（法一）由于<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性相关，故该向量组的秩小于3，从而<equation>r(\alpha_{1},\alpha_{2},\alpha_{3})\leqslant 2.</equation>又因为该向量组中任意两个向量均线性无关，所以该向量组的秩不小于2，从而<equation>r(\alpha_{1},\alpha_{2},\alpha_{3})\geqslant 2.</equation>于是，<equation>r(\alpha_{1},\alpha_{2},\alpha_{3})=2.</equation>由<equation>r(\alpha_{1},\alpha_{2},\alpha_{3}) = 2</equation>可得，矩阵<equation>(\alpha_{1},\alpha_{2},\alpha_{3})</equation>的任意一个3阶子式均为0.于是，<equation>\begin{aligned} \left| \begin{array}{l l l} a & 1 & 1 \\ 1 & 1 & a \\ 1 & a & 1  \right| \xlongequal {c _ {1} + c _ {2} + c _ {3}} \left| \begin{array}{l l l} a + 2 & 1 & 1 \\ a + 2 & 1 & a \\ a + 2 & a & 1  \right| &= (a + 2) \left| \begin{array}{l l l} 1 & 1 & 1 \\ 1 & 1 & a \\ 1 & a & 1  \right| &= (a + 2) \left| \begin{array}{l l l} 1 & 0 & 0 \\ 1 & 0 & a - 1 \\ 1 & a - 1 & 0  \right| \\ &= - (a + 2) \left(a - 1\right) ^ {2} = 0. \end{aligned}</equation>由此可得<equation>a = -2</equation>或<equation>a = 1</equation>. 但是当<equation>a = 1</equation>时，<equation>\alpha_{1} = \alpha_{3}</equation>，从而<equation>\alpha_{1},\alpha_{3}</equation>线性相关，不符合题意.于是，<equation>a = -2</equation>代入<equation>a=-2</equation>，再由矩阵（<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>）的任意一个3阶子式均为0可得<equation>\left| \begin{array}{c c c} 1 & 1 & - 2 \\ - 1 & b & - 1 \\ 1 & - 2 & 1 \end{array} \right| \frac {c _ {2} - c _ {1}}{c _ {3} + 2 c _ {1}} \left| \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & b + 1 & - 3 \\ 1 & - 3 & 3 \end{array} \right| = 3 (b + 1) - 9 = 0.</equation>解得 b=2.

因此，<equation>a=-2,b=2</equation>，应选D.

（法二）同法一可得<equation>r(\alpha_{1},\alpha_{2},\alpha_{3}) = 2.</equation>对矩阵<equation>(\alpha_{1},\alpha_{2},\alpha_{3})</equation>作初等行变换<equation>\begin{array}{l} \left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) = \left( \begin{array}{c c c} a & 1 & 1 \\ 1 & 1 & a \\ - 1 & b & - 1 \\ 1 & a & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & a \\ 1 & a & 1 \\ - 1 & b & - 1 \\ a & 1 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & a \\ 0 & a - 1 & 1 - a \\ 0 & b + 1 & a - 1 \\ 0 & 1 - a & 1 - a ^ {2} \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c} 1 & 1 & a \\ 0 & a - 1 & 1 - a \\ 0 & b + 1 & a - 1 \\ 0 & 0 & 2 - a - a ^ {2} \end{array} \right). \\ \end{array}</equation>当<equation>a = -2</equation>或<equation>a = 1</equation>时，<equation>2 - a - a^{2} = -(a + 2)(a - 1) = 0.</equation>当<equation>a = 1</equation>时，<equation>(\alpha_{1},\alpha_{2},\alpha_{3})\rightarrow \left( \begin{array}{c c c}1&1&1\\ 0&0&0\\ 0&b + 1&0\\ 0&0&0 \end{array} \right)\rightarrow \left( \begin{array}{c c c}1&1&1\\ 0&b + 1&0\\ 0&0&0\\ 0&0&0 \end{array} \right)</equation>.由此可得<equation>\alpha_{1},\alpha_{3}</equation>线性相关，不符合题意.

当 a = -2时，<equation>\left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right)\rightarrow \left(\begin{array}{c c c}1&1&- 2\\0&- 3&3\\0&b + 1&- 3\\0&0&0\end{array}\right)\rightarrow \left(\begin{array}{c c c}1&1&- 2\\0&1&- 1\\0&b - 2&0\\0&0&0\end{array}\right).</equation>由<equation>r(\alpha_{1},\alpha_{2},\alpha_{3}) = 2</equation>可得<equation>b - 2 = 0</equation>，即<equation>b = 2.</equation>因此，<equation>a=-2,b=2</equation>，应选D.

---

**2014年第6题 | 选择题 | 4分 | 答案: A**
6. 设<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>均为3维向量，则对任意常数 k,l，向量组<equation>\alpha_{1}+k\alpha_{3},\alpha_{2}+l\alpha_{3}</equation>线性无关是向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关的（    ）

A. 必要非充分条件 B. 充分非必要条件

C. 充分必要条件 D. 既非充分也非必要条件
答案: A
**解析: **解<equation>\left( \boldsymbol{\alpha}_{1}+k\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{2}+l\boldsymbol{\alpha}_{3}\right)=\left( \boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}\right)\left( \begin{array}{ll}1&0\\ 0&1\\ k&l \end{array} \right).</equation>若向量组<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性无关，则<equation>r \left(\boldsymbol {\alpha} _ {1} + k \boldsymbol {\alpha} _ {3}, \boldsymbol {\alpha} _ {2} + l \boldsymbol {\alpha} _ {3}\right) = r \left(\left( \begin{array}{c c} 1 & 0 \\ 0 & 1 \\ k & l \end{array} \right)\right) = 2.</equation>因此，<equation>\alpha_{1} + k\alpha_{3},\alpha_{2} + l\alpha_{3}</equation>线性无关.

令<equation>\alpha_{1},\alpha_{2}</equation>为线性无关的两个向量，<equation>\alpha_{3} = 0</equation>，则对任意常数<equation>k,l</equation>，向量组<equation>\alpha_{1} + k\alpha_{3},\alpha_{2} + l\alpha_{3}</equation>线性无关，但向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性相关.

综上所述，对任意常数 k，l，向量组<equation>\boldsymbol{\alpha}_{1}+k\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{2}+l\boldsymbol{\alpha}_{3}</equation>线性无关是向量组<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性无关的必要非充分条件.应选A.

---

**2012年第5题 | 选择题 | 4分 | 答案: C**
5. 设<equation>\alpha_{1}=\left( \begin{array}{c}0\\ 0\\ c_{1}\end{array} \right),\alpha_{2}=\left( \begin{array}{c}0\\ 1\\ c_{2}\end{array} \right),\alpha_{3}=\left( \begin{array}{c}1\\ -1\\ c_{3}\end{array} \right),\alpha_{4}=\left( \begin{array}{c}-1\\ 1\\ c_{4}\end{array} \right)</equation>其中<equation>c_{1},c_{2},c_{3},c_{4}</equation>为任意常数，则下列向量组线性相关的为（    ）

A.<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>B.<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>C.<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>D.<equation>\alpha_{2},\alpha_{3},\alpha_{4}</equation>
答案: C
**解析: **解（法一）由题设可得，<equation>\alpha_{3} + \alpha_{4} = \left( \begin{array}{c} 0 \\ 0 \\ c_{3} + c_{4} \end{array} \right),\alpha_{1} = \left( \begin{array}{c} 0 \\ 0 \\ c_{1} \end{array} \right).</equation>当<equation>c_{3} + c_{4}\neq 0</equation>时，<equation>\alpha_{1} = \frac{c_{1}}{c_{3} + c_{4}} \left(\alpha_{3} + \alpha_{4}\right)</equation>，<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>线性相关；当<equation>c_{3} + c_{4} = 0</equation>时，<equation>\alpha_{3} + \alpha_{4} = 0</equation>，<equation>\alpha_{3},\alpha_{4}</equation>线性相关.从而<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>线性相关.

综上所述，<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}</equation>线性相关，应选C.

（法二）由于<equation>n</equation>个<equation>n</equation>维列向量<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{n}</equation>线性相关等价于<equation>|\alpha_{1},\alpha_{2},\dots ,\alpha_{n}| = 0</equation>，而<equation>\left| \alpha_ {1}, \alpha_ {3}, \alpha_ {4} \right| = \left| \begin{array}{c c c} 0 & 1 & - 1 \\ 0 & - 1 & 1 \\ c _ {1} & c _ {3} & c _ {4} \end{array} \right| = c _ {1} \left| \begin{array}{c c} 1 & - 1 \\ - 1 & 1 \end{array} \right| = 0,</equation>故<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}</equation>线性相关.应选C.

同理可计算其他选项中的3个向量组成的矩阵的行列式，可知它们均不恒为零.

---

**2009年第20题 | 解答题 | 11分**
20. (本题满分11分)<equation>\text {设} \boldsymbol {A} = \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ - 1 & 1 & 1 \\ 0 & - 4 & - 2 \end{array} \right), \boldsymbol {\xi} _ {1} = \left( \begin{array}{c} - 1 \\ 1 \\ - 2 \end{array} \right).</equation>I. 求满足<equation>A\xi_{2}=\xi_{1}, A^{2}\xi_{3}=\xi_{1}</equation>的所有向量<equation>\xi_{2},\xi_{3}</equation>；

II. 对（I）中的任意向量<equation>\xi_{2},\xi_{3}</equation>，证明<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.
**答案: **（20）（I）满足<equation>A\xi_{2}=\xi_{1}</equation>的所有向量为<equation>\xi_{2}=k_{1}(1,-1,2)^{\mathrm{T}}+(0,0,1)^{\mathrm{T}}</equation>，其中<equation>k_{1}</equation>为任意常数满足<equation>A^{2}\xi_{3}=\xi_{1}</equation>的所有向量为<equation>\xi_{3}=k_{2}(1,-1,0)^{\mathrm{T}}+k_{3}(0,0,1)^{\mathrm{T}}+\left(-\frac{1}{2},0,0\right)^{\mathrm{T}}</equation>，其中<equation>k_{2},k_{3}</equation>为任意常数.

（Ⅱ）证明略.
**解析: **解（ I ）解<equation>A x=\xi_{1}</equation>，这是一个非齐次线性方程组.<equation>\left(\boldsymbol {A}, \boldsymbol {\xi} _ {1}\right) = \left( \begin{array}{c c c c} 1 & - 1 & - 1 & - 1 \\ - 1 & 1 & 1 & 1 \\ 0 & - 4 & - 2 & - 2 \end{array} \right) \xrightarrow [ r _ {2} ^ {*} \leftrightarrow r _ {3} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c} 1 & - 1 & - 1 & - 1 \\ 0 & - 4 & - 2 & - 2 \\ 0 & 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {1} + r _ {2} ^ {* * *} ]{r _ {2} ^ {* *} \times \left(- \frac {1}{2}\right)} \left( \begin{array}{c c c c} 1 & 1 & 0 & 0 \\ 0 & 2 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{array} \right).</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每做一次初等行变换，加一个 *.）

于是<equation>r(A) = r(A, \xi_1) = 2.Ax = \xi_1</equation>有无穷多解.其对应的齐次方程组等价于<equation>\left\{ \begin{array}{l} x_{1} + x_{2} = 0, \\ 2x_{2} + x_{3} = 0, \end{array} \right.</equation>故可取<equation>(1, -1, 2)^{\mathrm{T}}</equation>为它的一个基础解系.另外，<equation>\left\{ \begin{array}{l} x_{1} + x_{2} = 0, \\ 2x_{2} + x_{3} = 1 \end{array} \right.</equation>的一个特解为<equation>(0,0,1)^{\mathrm{T}}.</equation>因此，<equation>Ax = \xi_{1}</equation>的通解为<equation>\xi_{2} = k_{1}(1, -1, 2)^{\mathrm{T}} + (0, 0, 1)^{\mathrm{T}}</equation>，其中<equation>k_{1}</equation>为任意常数.<equation>\left(\boldsymbol {A} ^ {2}, \boldsymbol {\xi} _ {1}\right) = \left( \begin{array}{c c c c} 2 & 2 & 0 & - 1 \\ - 2 & - 2 & 0 & 1 \\ 4 & 4 & 0 & - 2 \end{array} \right) \xrightarrow [ r _ {3} - 2 r _ {1} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c} 2 & 2 & 0 & - 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{array} \right).</equation>于是<equation>r(A^{2}) = r(A^{2},\xi_{1}) = 1.A^{2}x = \xi_{1}</equation>有无穷多解.其对应的齐次方程组等价于<equation>2(x_{1} + x_{2}) = 0</equation>，故可取<equation>(1, - 1,0)^{\mathrm{T}}</equation>和<equation>(0,0,1)^{\mathrm{T}}</equation>为它的一个基础解系.另外，<equation>2(x_{1} + x_{2}) = -1</equation>的一个特解为<equation>\left(-\frac{1}{2},0,0\right)^{\mathrm{T}}.</equation>因此，<equation>A^{2}x = \xi_{1}</equation>的通解为<equation>\xi_{3} = k_{2}(1, -1, 0)^{\mathrm{T}} + k_{3}(0, 0, 1)^{\mathrm{T}} + \left(-\frac{1}{2}, 0, 0\right)^{\mathrm{T}}</equation>，其中<equation>k_{2}, k_{3}</equation>为任意常数.

（Ⅱ）（法一）通过计算可知，<equation>\boldsymbol {A} \boldsymbol {\xi} _ {1} = \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ - 1 & 1 & 1 \\ 0 & - 4 & - 2 \end{array} \right) \left( \begin{array}{c} - 1 \\ 1 \\ - 2 \end{array} \right) = \left( \begin{array}{c} 0 \\ 0 \\ 0 \end{array} \right).</equation>从而<equation>A^{3}\xi_{3} = A^{2}\xi_{2} = A\xi_{1} = 0.</equation>我们可以利用该性质推出<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

不妨设<equation>a\boldsymbol{\xi}_1 + b\boldsymbol{\xi}_2 + c\boldsymbol{\xi}_3 = \mathbf{0}</equation>. 该等式两端同时左乘<equation>A^2</equation>，得<equation>a A ^ {2} \xi_ {1} + b A ^ {2} \xi_ {2} + c A ^ {2} \xi_ {3} = c A ^ {2} \xi_ {3} = c \xi_ {1} = 0.</equation>由于<equation>\boldsymbol{\xi}_1</equation>为非零向量，故<equation>c = 0</equation>. 于是<equation>a\boldsymbol{\xi}_1 + b\boldsymbol{\xi}_2 = \mathbf{0}</equation>. 再在<equation>a\boldsymbol{\xi}_1 + b\boldsymbol{\xi}_2 = \mathbf{0}</equation>两端同时左乘<equation>A</equation>，得<equation>a A \xi_ {1} + b A \xi_ {2} = b A \xi_ {2} = b \xi_ {1} = 0.</equation>同理得<equation>b = 0</equation>. 由于<equation>b = c = 0</equation>, 故<equation>a\xi_{1} = 0</equation>. 从而<equation>a = 0</equation>.

因此，<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

（法二）由第（I）问，我们得到<equation>\xi_{1},\xi_{2},\xi_{3}</equation>的表达式，从而可以通过计算<equation>|\xi_{1},\xi_{2},\xi_{3}|</equation>来说明<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.<equation>\begin{aligned} \left| \xi_ {1}, \xi_ {2}, \xi_ {3} \right| &= \left| \begin{array}{c c c} - 1 & k _ {1} & k _ {2} - \frac {1}{2} \\ 1 & - k _ {1} & - k _ {2} \\ - 2 & 2 k _ {1} + 1. & k _ {3}  \right| \frac {c _ {2} + k _ {1} c _ {1}}{c _ {3} + k _ {2} c _ {1}} \left| \begin{array}{c c c} - 1 & 0 & - \frac {1}{2} \\ 1 & 0 & 0 \\ - 2 & 1 & k _ {3} - 2 k _ {2}  \right| \\ \underline {{\text {按 第二 行 展 开}}} (- 1) \left| \begin{array}{c c} 0 & - \frac {1}{2} \\ 1 & k _ {3} - 2 k _ {2}  \right| &= - \frac {1}{2} \neq 0. \end{aligned}</equation>因此，<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

---


