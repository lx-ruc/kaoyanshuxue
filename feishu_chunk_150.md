---

**2013年第21题 | 解答题 | 11分**


设二次型<equation>f(x_{1},x_{2},x_{3}) = 2\left(a_{1}x_{1} + a_{2}x_{2} + a_{3}x_{3}\right)^{2} + \left(b_{1}x_{1} + b_{2}x_{2} + b_{3}x_{3}\right)^{2}</equation>，记<equation>\begin{aligned} \alpha &= \left(  a _ {1} \\ a _ {2} \\ a _ {3}  \right), \quad \beta &= \left(  b _ {1} \\ b _ {2} \\ b _ {3}  \right) \end{aligned}</equation>I. 证明二次型 f对应的矩阵为<equation>2\alpha\alpha^{\mathrm{T}}+\beta\beta^{\mathrm{T}};</equation>II. 若<equation>\alpha, \beta</equation>正交且均为单位向量，证明 f在正交变换下的标准形为<equation>2y_{1}^{2}+y_{2}^{2}.</equation>

**答案:**（21）（I）证明略；

（Ⅱ）证明略.

**解析:**证（I）记<equation>\boldsymbol{x} = (x_{1},x_{2},x_{3})^{\mathrm{T}}</equation>，f对应的矩阵为A，A为对称矩阵，则<equation>\begin{aligned} a _ {1} x _ {1} + a _ {2} x _ {2} + a _ {3} x _ {3} &= \boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\alpha} = \boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {x}, \quad b _ {1} x _ {1} + b _ {2} x _ {2} + b _ {3} x _ {3} = \boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\beta} = \boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {x}. \\ f \left(x _ {1}, x _ {2}, x _ {3}\right) &= 2 \left(\boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\alpha}\right) \left(\boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {x}\right) + \left(\boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\beta}\right) \left(\boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {x}\right) = \boldsymbol {x} ^ {\mathrm {T}} \left(2 \alpha \boldsymbol {\alpha} ^ {\mathrm {T}} + \beta \boldsymbol {\beta} ^ {\mathrm {T}}\right) \boldsymbol {x}. \end{aligned}</equation>又由于<equation>(2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}})^{\mathrm{T}} = 2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>，故<equation>2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>是对称矩阵.于是<equation>2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>为所求A.

（Ⅱ）（法一）由<equation>A = 2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>且<equation>\alpha</equation>与<equation>\beta</equation>相互正交<equation>(\alpha^{\mathrm{T}}\beta = 0, \beta^{\mathrm{T}}\alpha = 0)</equation>得，<equation>A \alpha = \left(2 \alpha \alpha^ {\mathrm {T}} + \beta \beta^ {\mathrm {T}}\right) \alpha = 2 \alpha , \quad A \beta = \left(2 \alpha \alpha^ {\mathrm {T}} + \beta \beta^ {\mathrm {T}}\right) \beta = \beta .</equation>因此，2,1均为<equation>A</equation>的特征值，而<equation>\alpha ,\beta</equation>分别为属于特征值2,1的特征向量.

下面还需确定 A的另一个特征值.

考虑 A的秩.

由于对任何非零<equation>n</equation>维列向量<equation>\alpha ,\beta ,</equation>矩阵<equation>\beta \alpha^{\mathrm{T}}</equation>的秩均为1，故<equation>r (\boldsymbol {A}) = r \left(2 \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}\right) \leqslant r \left(2 \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}}\right) + r \left(\boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}\right) = 2.</equation>于是，<equation>A</equation>不满秩，0也是<equation>A</equation>的一个特征值.

因此，存在正交矩阵<equation>P</equation>使得<equation>P^{\mathrm{T}}AP = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).f</equation>在正交变换<equation>x = Py</equation>下的标准形为<equation>f = 2y_{1}^{2} + y_{2}^{2}</equation>.

（法二）取<equation>\gamma</equation>为与<equation>\alpha, \beta</equation>均正交的单位向量，可取<equation>\gamma = \frac{\alpha \times \beta}{\| \alpha \times \beta \|}</equation>（<equation>\alpha \times \beta</equation>为向量<equation>\alpha, \beta</equation>的向量积，<equation>\| \alpha \times \beta \|</equation>为向量<equation>\alpha \times \beta</equation>的模），则<equation>P = (\alpha ,\beta ,\gamma)</equation>为正交矩阵.<equation>\begin{aligned} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} &= \left(  \boldsymbol {\alpha} ^ {\mathrm {T}} \\ \boldsymbol {\beta} ^ {\mathrm {T}} \\ \boldsymbol {\gamma} ^ {\mathrm {T}}  \right) \left(2 \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}\right) (\boldsymbol {\alpha}, \boldsymbol {\beta}, \gamma) &= \left(  2 \boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}} \\ 2 \boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}} \\ 2 \gamma^ {\mathrm {T}} \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \gamma^ {\mathrm {T}} \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}  \right) (\boldsymbol {\alpha}, \boldsymbol {\beta}, \gamma). \end{aligned}</equation>由于<equation>\alpha ,\beta ,\gamma</equation>相互正交，且均为单位向量，故<equation>\alpha^{\mathrm{T}}\boldsymbol{\beta} = \beta^{\mathrm{T}}\alpha = \gamma^{\mathrm{T}}\alpha = \gamma^{\mathrm{T}}\boldsymbol{\beta} = 0,</equation><equation>\alpha^{\mathrm{T}}\alpha = \beta^{\mathrm{T}}\beta = 1.</equation><equation>\boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} = \left( \begin{array}{c} 2 \boldsymbol {\alpha} ^ {\mathrm {T}} \\ \boldsymbol {\beta} ^ {\mathrm {T}} \\ \mathbf {0} \end{array} \right) (\boldsymbol {\alpha}, \boldsymbol {\beta}, \gamma) = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>因此，<equation>f</equation>在正交变换<equation>x = P y</equation>下的标准形为<equation>f = 2y_{1}^{2} + y_{2}^{2}</equation>.

---

**2012年第21题 | 解答题 | 11分**

21. (本题满分11分)

已知<equation>A=\left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ -1 & 0 & a \\ 0 & a & -1 \end{array} \right)</equation>，二次型<equation>f(x_{1},x_{2},x_{3})=\boldsymbol{x}^{\mathrm{T}}(\boldsymbol{A}^{\mathrm{T}}\boldsymbol{A})\boldsymbol{x}</equation>的秩为2.

I. 求实数 a 的值；

II. 求正交变换<equation>x = Qy</equation>将<equation>f</equation>化为标准形.

**答案:**(21) （I）<equation>a=-1;</equation>（Ⅱ）<equation>Q=\left( \begin{array}{c c c} \frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{6}} & \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{3}} \\ \frac{2}{\sqrt{6}} & 0 & \frac{1}{\sqrt{3}} \end{array} \right)</equation>，正交变换<equation>x=Qy</equation>将二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>变成标准

形<equation>f=6 y_{1}^{2}+2 y_{2}^{2}.</equation>

**解析:**解（I）（法一）二次型 f的秩等于它所对应的实对称矩阵<equation>A^{\mathrm{T}}A</equation>的秩，于是<equation>r(A^{\mathrm{T}}A)=2.</equation>下面我们证明<equation>r(A^{\mathrm{T}}A)=r(A).</equation>由于<equation>A^{\mathrm{T}}A</equation>与A的列数相等，故证明<equation>r( A^{\mathrm{T}}A)=r(A)</equation>只需要证明<equation>A^{\mathrm{T}}Ax=0</equation>与<equation>Ax=0</equation>同解.若 x满足<equation>Ax=0</equation>，则<equation>A^{\mathrm{T}}(Ax)=0</equation>即<equation>( A^{\mathrm{T}}A ) x=0.</equation>另一方面，若 x满足<equation>\left( A^{\mathrm{T}} A \right) x=0</equation>，则<equation>x^{\mathrm{T}} \left( A^{\mathrm{T}} A \right) x=0</equation>，即<equation>\left( A x \right)^{\mathrm{T}} \left( A x \right)=0</equation>.由于<equation>\alpha^{\mathrm{T}} \alpha=0</equation>当且仅当<equation>\alpha=0</equation>，故<equation>A x=0.</equation>因此，<equation>r(\mathbf{A})=r(\mathbf{A}^{\mathrm{T}}\mathbf{A})=2.</equation>我们可以对<equation>A</equation>作初等行变换，求得<equation>r(A) = 2</equation>时的<equation>a</equation>的值.<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ - 1 & 0 & a \\ 0 & a & - 1 \end{array} \right) \xrightarrow [ r _ {4} - a r _ {2} ]{r _ {3} + r _ {1}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & a + 1 \\ 0 & 0 & - a - 1 \end{array} \right) \xrightarrow [ r _ {4} ^ {*} + r _ {3} ^ {*} ]{r _ {4} ^ {*} + r _ {3} ^ {*}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & a + 1 \\ 0 & 0 & 0 \end{array} \right).</equation>由此可见，仅当<equation>a + 1 = 0</equation>时，<equation>r(A) = 2</equation>，故<equation>a = -1</equation>（法二）由于<equation>r(\mathbf{A}^{\mathrm{T}}\mathbf{A})=2</equation>，而<equation>\mathbf{A}^{\mathrm{T}}\mathbf{A}</equation>为<equation>3\times 3</equation>矩阵，故<equation>|\mathbf{A}^{\mathrm{T}}\mathbf{A}|=0.</equation><equation>\boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {A} = \left( \begin{array}{c c c c} 1 & 0 & - 1 & 0 \\ 0 & 1 & 0 & a \\ 1 & 1 & a & - 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ - 1 & 0 & a \\ 0 & a & - 1 \end{array} \right) = \left( \begin{array}{c c c} 2 & 0 & 1 - a \\ 0 & 1 + a ^ {2} & 1 - a \\ 1 - a & 1 - a & 3 + a ^ {2} \end{array} \right).</equation>求得<equation>|\mathbf{A}^{\mathrm{T}}\mathbf{A}| = (a^{2} + 3)(a + 1)^{2}</equation>. 因此，由<equation>|\mathbf{A}^{\mathrm{T}}\mathbf{A}| = 0</equation>可得<equation>a = -1</equation>（Ⅱ）由第（I）问可得，<equation>A^{\mathrm{T}}A = \left( \begin{array}{c c c} 2 & 0 & 2 \\ 0 & 2 & 2 \\ 2 & 2 & 4 \end{array} \right)</equation>，从而<equation>A^{\mathrm{T}}A</equation>的特征多项式为<equation>| \lambda E - A ^ {\mathrm {T}} A | = \left| \begin{array}{c c c} \lambda - 2 & 0 & - 2 \\ 0 & \lambda - 2 & - 2 \\ - 2 & - 2 & \lambda - 4 \end{array} \right| = \lambda (\lambda - 2) (\lambda - 6).</equation><equation>A^{\mathrm{T}}A</equation>的特征值为6,2,0.

下面分别计算属于特征值6,2,0的特征向量.

当<equation>\lambda=6</equation>时，<equation>\begin{array}{l} 6 E - A ^ {\mathrm {T}} A = \left( \begin{array}{c c c} 4 & 0 & - 2 \\ 0 & 4 & - 2 \\ - 2 & - 2 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 0 & 2 & - 1 \\ 1 & 1 & - 1 \end{array} \right) \xrightarrow {r _ {3} - r _ {2}} \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 0 & 2 & - 1 \\ 1 & - 1 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} - r _ {1} + 2 r _ {3} ^ {*}} \binom {2} {r _ {2} ^ {*} \leftrightarrow r _ {3} ^ {*}} \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 1 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right), \\ \end{array}</equation>得<equation>\left\{ \begin{array}{l} 2x_{1} - x_{3} = 0, \\ x_{1} - x_{2} = 0. \end{array} \right.</equation>解得该方程组的一个基础解系<equation>\xi_{1} = (1,1,2)^{\mathrm{T}}.</equation>当<equation>\lambda=2</equation>时，<equation>2 \boldsymbol {E} - \boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {A} = \left( \begin{array}{c c c} 0 & 0 & - 2 \\ 0 & 0 & - 2 \\ - 2 & - 2 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 1 \\ 0 & 0 & 1 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {3} - r _ {2} ]{r _ {1} - r _ {2}} \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right),</equation>得<equation>\left\{ \begin{array}{l}x_{1} + x_{2} = 0,\\ x_{3} = 0. \end{array} \right.</equation>解得该方程组的一个基础解系<equation>\xi_{2} = (-1,1,0)^{\mathrm{T}}.</equation>当<equation>\lambda=0</equation>时，<equation>0 \boldsymbol {E} - \boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {A} = \left( \begin{array}{c c c} - 2 & 0 & - 2 \\ 0 & - 2 & - 2 \\ - 2 & - 2 & - 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 2 \end{array} \right) \xrightarrow {r _ {3} - r _ {1} - r _ {2}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right),</equation>得<equation>\left\{ \begin{array}{l}x_{1} + x_{3} = 0,\\ x_{2} + x_{3} = 0. \end{array} \right.</equation>解得该方程组的一个基础解系<equation>\xi_{3} = (-1, -1, 1)^{\mathrm{T}}.</equation>由于实对称矩阵属于不同特征值的特征向量相互正交，故<equation>\xi_{1},\xi_{2},\xi_{3}</equation>相互正交.将<equation>\xi_{1},\xi_{2},\xi_{3}</equation>单位化，得<equation>\boldsymbol {\alpha} _ {1} = \frac {1}{\sqrt {6}} \left( \begin{array}{c} 1 \\ 1 \\ 2 \end{array} \right), \quad \boldsymbol {\alpha} _ {2} = \frac {1}{\sqrt {2}} \left( \begin{array}{c} - 1 \\ 1 \\ 0 \end{array} \right), \quad \boldsymbol {\alpha} _ {3} = \frac {1}{\sqrt {3}} \left( \begin{array}{c} - 1 \\ - 1 \\ 1 \end{array} \right).</equation>取<equation>Q = \left(\alpha_{1},\alpha_{2},\alpha_{3}\right)</equation>，则<equation>Q</equation>为正交矩阵，且<equation>Q^{\mathrm{T}} \left(A^{\mathrm{T}} A\right) Q = \left( \begin{array}{c c c} 6 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>因此，当<equation>Q=\left( \begin{array}{c c c} {\frac{1}{\sqrt{6}}} & {-\frac{1}{\sqrt{2}}} & {-\frac{1}{\sqrt{3}}} \\ {\frac{1}{\sqrt{6}}} & {\frac{1}{\sqrt{2}}} & {-\frac{1}{\sqrt{3}}} \\ {\frac{2}{\sqrt{6}}} & {0} & {\frac{1}{\sqrt{3}}} \end{array} \right)</equation>时，正交变换<equation>x=Qy</equation>将二次型<equation>f(x_{1},x_{2},x_{3})</equation>变成标准

形<equation>f=6 y_{1}^{2}+2 y_{2}^{2}.</equation>

---

**2011年第13题 | 填空题 | 4分**

13. 设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=\boldsymbol{x}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{x}</equation>的秩为1，A的各行元素之和为3，则 f在正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>下的标准形为

**解析:**解 设矩阵<equation>A = \left( \begin{array}{l l l} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{array} \right)</equation>.由已知条件知<equation>\left\{ \begin{array}{l l l} a_{11} + a_{12} + a_{13} = 3, \\ a_{21} + a_{22} + a_{23} = 3, \\ a_{31} + a_{32} + a_{33} = 3, \end{array} \right.</equation>即<equation>\left( \begin{array}{l l l} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{array} \right)\left( \begin{array}{l} 1 \\ 1 \\ 1 \end{array} \right) = 3\left( \begin{array}{l} 1 \\ 1 \\ 1 \end{array} \right)</equation>于是3是<equation>A</equation>的特征值.又因为<equation>r(A) = 1</equation>，且实对称矩阵<equation>A</equation>相似于以其特征值为主对角元的对角矩阵，所以0是<equation>A</equation>的2重特征值.因此，<equation>A</equation>的所有特征值为3，0，0，<equation>f</equation>在正交变换<equation>x = Qy</equation>下的标准形为<equation>3y_{1}^{2}</equation>

---

**2009年第21题 | 解答题 | 11分**

21. (本题满分11分)

设二次型<equation>f \left(x_{1}, x_{2}, x_{3}\right)=a x_{1}^{2}+a x_{2}^{2}+(a-1) x_{3}^{2}+2 x_{1} x_{3}-2 x_{2} x_{3}</equation>I. 求二次型 f的矩阵的所有特征值；

II. 若二次型 f的规范形为<equation>y_{1}^{2}+y_{2}^{2}</equation>，求 a的值.

**答案:**(21) ( I ) a, a-2, a+1;

( II ) a=2.

**解析:**（I）二次型<equation>f</equation>的矩阵为<equation>A=\left( \begin{array}{c c c} a & 0 & 1 \\ 0 & a & -1 \\ 1 & -1 & a-1 \end{array} \right).</equation>计算<equation>A</equation>的特征多项式<equation>|\lambda E - A|</equation>，得<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - a & 0 & - 1 \\ 0 & \lambda - a & 1 \\ - 1 & 1 & \lambda - a + 1  \right| \xlongequal {\text {按 第一 行 展 开}} (\lambda - a) \left[ (\lambda - a) (\lambda - a + 1) - 1 \right] - (\lambda - a) \\ &= (\lambda - a) \left[ (\lambda - a) ^ {2} + (\lambda - a) - 2 \right] = (\lambda - a) (\lambda - a + 2) (\lambda - a - 1). \end{aligned}</equation>因此，<equation>A</equation>的特征值为<equation>a, a - 2, a + 1.</equation>（Ⅱ）由<equation>f</equation>的规范形为<equation>y_{1}^{2} + y_{2}^{2}</equation>知，<equation>A</equation>的特征值有两个正数，一个为零.0为最小的特征值.

由于<equation>a - 2 < a < a + 1</equation>，故可知<equation>a - 2 = 0</equation>，即<equation>a = 2</equation>

---


### 行列式

**2025年第15题 | 填空题 | 5分**

<equation>1 5. f (x) = \left| \begin{array}{c c c c} 2 x + 1 & 3 & 2 x + 1 & 1 \\ 2 x & - 3 & 4 x & - 2 \\ 2 x + 1 & 2 & 2 x + 1 & 1 \\ 2 x & - 4 & 4 x & - 2 \end{array} \right|, g (x) = \left| \begin{array}{c c c c} 2 x + 1 & 1 & 2 x + 1 & 3 \\ 5 x + 1 & - 2 & 4 x & - 3 \\ 0 & 1 & 2 x + 1 & 2 \\ 2 x & - 2 & 4 x & - 4 \end{array} \right|</equation>则方程 f(x）=g(x）的不同的根的个数

为___

**解析:**解 由于交换两列，行列式变号，故<equation>- g ( x ) = \left| \begin{array}{c c c c} 2 x + 1 & 3 & 2 x + 1 & 1 \\ 5 x + 1 & - 3 & 4 x & - 2 \\ 0 & 2 & 2 x + 1 & 1 \\ 2 x & - 4 & 4 x & - 2 \end{array} \right|</equation>从而<equation>\begin{aligned} f (x) - g (x) &= \left| \begin{array}{c c c c} 2 x + 1 & 3 & 2 x + 1 & 1 \\ 2 x & - 3 & 4 x & - 2 \\ 2 x + 1 & 2 & 2 x + 1 & 1 \\ 2 x & - 4 & 4 x & - 2  \right| + \left| \begin{array}{c c c c} 2 x + 1 & 3 & 2 x + 1 & 1 \\ 5 x + 1 & - 3 & 4 x & - 2 \\ 0 & 2 & 2 x + 1 & 1 \\ 2 x & - 4 & 4 x & - 2  \right| \\ &= \left| \begin{array}{c c c c} 4 x + 2 & 3 & 2 x + 1 & 1 \\ 7 x + 1 & - 3 & 4 x & - 2 \\ 2 x + 1 & 2 & 2 x + 1 & 1 \\ 4 x & - 4 & 4 x & - 2  \right| \frac {c _ {1} - c _ {3}}{\frac {c _ {2} - 2 c _ {4}}{2}} \left| \begin{array}{c c c c} 2 x + 1 & 1 & 2 x + 1 & 1 \\ 3 x + 1 & 1 & 4 x & - 2 \\ 0 & 0 & 2 x + 1 & 1 \\ 0 & 0 & 4 x & - 2  \right| \\ &= \left| \begin{array}{c c} 2 x + 1 & 1 \\ 3 x + 1 & 1  \right| \cdot \left| \begin{array}{c c} 2 x + 1 & 1 \\ 4 x & - 2  \right| &= (- x) \cdot (- 8 x - 2) = x (8 x + 2). \end{aligned}</equation>因此，方程<equation>f ( x )=g ( x )</equation>即<equation>x ( 8 x+2 )=0</equation>，该方程的根共有2个：<equation>x_{1}=0,x_{2}=-\frac{1}{4}.</equation>

---

**2024年第7题 | 选择题 | 5分 | 答案: B**

7. 设矩阵<equation>A=\left( \begin{array}{c c c} a+1 & b & 3 \\ a & \frac{b}{2} & 1 \\ 1 & 1 & 2 \end{array} \right), M_{ij}</equation>表示 A的 i行 j列元素的余子式，若<equation>|A|=-\frac{1}{2}</equation>且<equation>-M_{21}+M_{22}-M_{23}=0.</equation>则（    ）

A. a=0或<equation>a=-\frac{3}{2}</equation>B. a=0或<equation>a=\frac{3}{2}</equation>C. b=1或<equation>b=-\frac{1}{2}</equation>D. b=-1或<equation>b=\frac{1}{2}</equation>

答案: B

**解析:**解 由<equation>- M_{21}+M_{22}-M_{23}=0</equation>实际上可以得到<equation>A_{21}+A_{22}+A_{23}=0</equation>，故由行列式的按行展开定理可得将矩阵 A的第二行元素全换成1所得矩阵的行列式等于0，即<equation>\left| \begin{array}{c c c} a + 1 & b & 3 \\ 1 & 1 & 1 \\ 1 & 1 & 2 \end{array} \right| \xlongequal {r _ {3} - r _ {2}} \left| \begin{array}{c c c} a + 1 & b & 3 \\ 1 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right| \xlongequal {\text {按 第三 行 展开}} a + 1 - b = 0.</equation>于是，<equation>b=a+1.</equation>由<equation>|A| = -\frac{1}{2}</equation>以及<equation>b=a+1</equation>可得<equation>\left| \begin{array}{c c c} b & b & 3 \\ b - 1 & \frac {b}{2} & 1 \\ 1 & 1 & 2 \end{array} \right| \xlongequal {c _ {1} - c _ {2}} \left| \begin{array}{c c c} 0 & b & 3 \\ \frac {b}{2} - 1 & \frac {b}{2} & 1 \\ 0 & 1 & 2 \end{array} \right| \xlongequal {\text {按 第一 列 展 开}} \left(1 - \frac {b}{2}\right) (2 b - 3) = - \frac {1}{2}.</equation>整理可得<equation>(b - 2)(2b - 3) = 1</equation>，即<equation>2b^{2} - 7b + 5 = 0.</equation>解得<equation>b = 1</equation>或<equation>b = \frac{5}{2}</equation>，从而<equation>a = 0</equation>或<equation>a = \frac{3}{2}</equation>因此，应选B.

---

**2021年第15题 | 填空题 | 5分**

15. 多项式 f(x) =<equation>\left| \begin{array}{c c c c} x & x & 1 & 2 x \\ 1 & x & 2 & - 1 \\ 2 & 1 & x & 1 \\ 2 & - 1 & 1 & x \end{array} \right|</equation>中<equation>x^{3}</equation>项的系数为 ___

**解析:**解 由于所给行列式的元素均为常数或 x的倍数，故根据行列式的定义，要出现<equation>x^{3}</equation>项，必须从不同行、不同列中取出3个含 x的项相乘.

将行列式记为<equation>\det ( a_{ij} ).</equation><equation>\textcircled{1} a_{11}=x</equation>不能取.若取<equation>a_{11}</equation>，则第一行中的 x与 2x不能取.于是，剩下的2个含 x的元素必来自主对角线上的3个 x.无论从<equation>a_{22},a_{33},a_{44}</equation>中取哪两个，第四个元素都只能来自主对角线，从而这种取法最终将得到<equation>x^{4}</equation>，而不是<equation>x^{3}.</equation><equation>\left| \begin{array}{c c c c} \underline {{x}} & x & 1 & 2 x \\ 1 & \underline {{x}} & 2 & - 1 \\ 2 & 1 & \underline {{x}} & 1 \\ 2 & - 1 & 1 & \underline {{x}} \end{array} \right|.</equation><equation>\textcircled{2}</equation>由于<equation>x^{3}</equation>项必来自于不同列的含x元素的乘积，故确定<equation>a_{11}</equation>不取后，x必来自后三列，而第三列中仅<equation>a_{33}=x</equation>，从而必取.

下面分情况讨论.

(1) 若第二列中取<equation>a_{12}=x</equation>，则组合应为<equation>a_{12}a_{21}a_{33}a_{44}</equation>.该组合对应排列2，1，3，4，逆序数为1.于是，所得<equation>x^{3}</equation>项为<equation>(-1)^{1}\cdot 1\cdot x^{3}=-x^{3}.</equation>(2) 若第二列中取<equation>a_{22}=x</equation>，则组合应为<equation>a_{14}a_{22}a_{33}a_{41}</equation>.该组合对应排列4，2，3，1，逆序数为5.于是，所得<equation>x^{3}</equation>项为<equation>(-1)^{5}\cdot 2\cdot 2x^{3}=-4x^{3}.</equation><equation>\left| \begin{array}{c c c c} x & \underline {{x}} & 1 & 2 x \\ 1 & x & 2 & - 1 \\ 2 & 1 & \underline {{x}} & 1 \\ 2 & - 1 & 1 & \underline {{x}} \end{array} \right|, \quad \left| \begin{array}{c c c c} x & x & 1 & 2 x \\ 1 & \underline {{x}} & 2 & - 1 \\ 2 & 1 & \underline {{x}} & 1 \\ 2 & - 1 & 1 & x \end{array} \right|</equation>因此，<equation>f ( x )</equation>的<equation>x^{3}</equation>项为<equation>- x^{3}-4 x^{3}=-5 x^{3}, x^{3}</equation>的系数为-5.

---

**2020年第13题 | 填空题 | 4分**

13. 行列式<equation>\left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a \end{array} \right| = \underline {{\quad}}</equation>

**答案:**<equation>a^{4}-4 a^{2}.</equation>

**解析:**解（法一）利用行列式的性质对所求行列式进行转化.

若 a=0 ，则将第二行加到第一行可得零行，从而行列式为0.

若 a≠0，则<equation>\begin{aligned} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a  \right| \frac {r _ {4} + r _ {3}}{\hline} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 0 & 0 & a & a  \right| \frac {r _ {3} + \frac {1}{a} r _ {1}}{\hline} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ 0 & 1 & a - \frac {1}{a} & \frac {1}{a} \\ 0 & 0 & a & a  \right| \\ \frac {r _ {3} - \frac {1}{a} r _ {2}}{\hline} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ 0 & 0 & a - \frac {2}{a} & \frac {2}{a} \\ 0 & 0 & a & a  \right| &= \left| \begin{array}{c c} a & 0 \\ 0 & a  \right| \cdot \left| \begin{array}{c c} a - \frac {2}{a} & \frac {2}{a} \\ a & a  \right| \\ &= a ^ {2} \left[ \left(a - \frac {2}{a}\right) a - 2 \right] = a ^ {2} \left(a ^ {2} - 4\right) = a ^ {4} - 4 a ^ {2}. \end{aligned}</equation>不论是哪种情况，所求行列式均为<equation>a^{4}-4 a^{2}.</equation>（法二）注意到所求行列式的各行元素之和均为 a，故可将各列均加到第1列，然后计算行列式.<equation>\left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a \end{array} \right| \frac {c _ {1} + c _ {2} + c _ {3} + c _ {4}}{\hline} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ a & a & 1 & - 1 \\ a & 1 & a & 0 \\ a & - 1 & 0 & a \end{array} \right| = a \left| \begin{array}{c c c c} 1 & 0 & - 1 & 1 \\ 1 & a & 1 & - 1 \\ 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a \end{array} \right|</equation><equation>\begin{array}{l} \frac {c _ {3} + c _ {1}}{c _ {4} - c _ {1}} a \left| \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 1 & a & 2 & - 2 \\ 1 & 1 & a + 1 & - 1 \\ 1 & - 1 & 1 & a - 1 \end{array} \right| \frac {c _ {3} + c _ {4}}{c _ {4}} a \left| \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 1 & a & 0 & - 2 \\ 1 & 1 & a & - 1 \\ 1 & - 1 & a & a - 1 \end{array} \right| \\ \frac {\text {按第一行展开}} {= a ^ {4} - 4 a ^ {2}} a \left\{a \left[ a (a - 1) + a \right] - 2 (a + a) \right\} = a \left(a ^ {3} - 4 a\right) \\ \end{array}</equation>

---

**2016年第13题 | 填空题 | 4分**

13. 行列式<equation>\left| \begin{array}{c c c c} \lambda & - 1 & 0 & 0 \\ 0 & \lambda & - 1 & 0 \\ 0 & 0 & \lambda & - 1 \\ 4 & 3 & 2 & \lambda + 1 \end{array} \right| = \underline {{\quad}}</equation>

**答案:**##<equation>\lambda^{4}+\lambda^{3}+2\lambda^{2}+3\lambda+4.</equation>

**解析:**（法一）按第一列展开.<equation>\begin{aligned} \left| \begin{array}{c c c c} \lambda & - 1 & 0 & 0 \\ 0 & \lambda & - 1 & 0 \\ 0 & 0 & \lambda & - 1 \\ 4 & 3 & 2 & \lambda + 1  \right| &= \lambda \left| \begin{array}{c c c} \lambda & - 1 & 0 \\ 0 & \lambda & - 1 \\ 3 & 2 & \lambda + 1  \right| - 4 \left| \begin{array}{c c c} - 1 & 0 & 0 \\ \lambda & - 1 & 0 \\ 0 & \lambda & - 1  \right| \\ &= \lambda \left(\lambda \left| \begin{array}{c c} \lambda & - 1 \\ 2 & \lambda + 1  \right| + 3 \left| \begin{array}{c c} - 1 & 0 \\ \lambda & - 1  \right|\right) - 4 \times (- 1) ^ {3} \\ &= \lambda \left[ \lambda \left(\lambda^ {2} + \lambda + 2\right) + 3 \right] + 4 \\ &= \lambda^ {4} + \lambda^ {3} + 2 \lambda^ {2} + 3 \lambda + 4. \end{aligned}</equation>（法二）利用行列式的性质.<equation>\begin{aligned} \left| \begin{array}{c c c c} \lambda & - 1 & 0 & 0 \\ 0 & \lambda & - 1 & 0 \\ 0 & 0 & \lambda & - 1 \\ 4 & 3 & 2 & \lambda + 1  \right| \frac {c _ {1} + \lambda c _ {2}}{\hline} \left| \begin{array}{c c c c} 0 & - 1 & 0 & 0 \\ \lambda^ {2} & \lambda & - 1 & 0 \\ 0 & 0 & \lambda & - 1 \\ 4 + 3 \lambda & 3 & 2 & \lambda + 1  \right| \\ \frac {c _ {1} + \lambda^ {2} c _ {3}}{\hline} \left| \begin{array}{c c c c} 0 & - 1 & 0 & 0 \\ 0 & \lambda & - 1 & 0 \\ \lambda^ {3} & 0 & \lambda & - 1 \\ 4 + 3 \lambda + 2 \lambda^ {2} & 3 & 2 & \lambda + 1  \right| \\ \frac {c _ {1} + \lambda^ {3} c _ {4}}{\hline} \left| \begin{array}{c c c c} 0 & & - 1 & 0 & 0 \\ 0 & & \lambda & - 1 & 0 \\ 0 & & 0 & \lambda & - 1 \\ 4 + 3 \lambda + 2 \lambda^ {2} + \lambda^ {3} (\lambda + 1) & 3 & 2 & \lambda + 1  \right| \\ &= (- 1) ^ {4 + 1} \left[ 4 + 3 \lambda + 2 \lambda^ {2} + \lambda^ {3} (\lambda + 1) \right] (- 1) ^ {3} \\ &= \lambda^ {4} + \lambda^ {3} + 2 \lambda^ {2} + 3 \lambda + 4. \end{aligned}</equation>

---

**2014年第5题 | 选择题 | 4分 | 答案: B**

5. 行列式<equation>\left| \begin{array}{c c c c} 0 & a & b & 0 \\ a & 0 & 0 & b \\ 0 & c & d & 0 \\ c & 0 & 0 & d \end{array} \right|.</equation>A.<equation>( a d-b c )^{2}</equation>B.<equation>-( a d-b c )^{2}</equation>C.<equation>a^{2} d^{2}-b^{2} c^{2}</equation>D.<equation>b^{2} c^{2}-a^{2} d^{2}</equation>

答案: B

**解析:**解（法一）对原行列式作初等变换.根据行列式的性质，交换两行或两列，所得新行列式为原行列式的负值.<equation>\left| \begin{array}{c c c c} 0 & a & b & 0 \\ a & 0 & 0 & b \\ 0 & c & d & 0 \\ c & 0 & 0 & d \end{array} \right| = - \left| \begin{array}{c c c c} 0 & a & b & 0 \\ 0 & c & d & 0 \\ a & 0 & 0 & b \\ c & 0 & 0 & d \end{array} \right| = \left| \begin{array}{c c c c} a & 0 & b & 0 \\ c & 0 & d & 0 \\ 0 & a & 0 & b \\ 0 & c & 0 & d \end{array} \right| = - \left| \begin{array}{c c c c} a & b & 0 & 0 \\ c & d & 0 & 0 \\ 0 & 0 & a & b \\ 0 & 0 & c & d \end{array} \right| = - (a d - b c) ^ {2}.</equation>应选B.

（法二）按第一行展开.<equation>\left| \begin{array}{c c c c} 0 & a & b & 0 \\ a & 0 & 0 & b \\ 0 & c & d & 0 \\ c & 0 & 0 & d \end{array} \right| = (- a) \left| \begin{array}{c c c} a & 0 & b \\ 0 & d & 0 \\ c & 0 & d \end{array} \right| + b \left| \begin{array}{c c c} a & 0 & b \\ 0 & c & 0 \\ c & 0 & d \end{array} \right| = - a ^ {2} d ^ {2} + a b c d + a b c d - b ^ {2} c ^ {2} = - (a d - b c) ^ {2}.</equation>应选B.

---

**2013年第13题 | 填空题 | 4分**

13. 设<equation>A=(a_{ij})</equation>是3阶非零矩阵，<equation>|A|</equation>为 A的行列式，<equation>A_{ij}</equation>为<equation>a_{ij}</equation>的代数余子式. 若<equation>a_{ij}+A_{ij}=0</equation>（i,j=1,2,3），则<equation>|A|=</equation>___

**解析:**首先，由题设可知<equation>\boldsymbol {A} ^ {*} = \left( \begin{array}{c c c} A _ {1 1} & A _ {2 1} & A _ {3 1} \\ A _ {1 2} & A _ {2 2} & A _ {3 2} \\ A _ {1 3} & A _ {2 3} & A _ {3 3} \end{array} \right) \xlongequal {a _ {i j} + A _ {i j} = 0} \left( \begin{array}{c c c} - a _ {1 1} & - a _ {2 1} & - a _ {3 1} \\ - a _ {1 2} & - a _ {2 2} & - a _ {3 2} \\ - a _ {1 3} & - a _ {2 3} & - a _ {3 3} \end{array} \right) = - \boldsymbol {A} ^ {\mathrm {T}},</equation>故<equation>|\mathbf{A}|^3 = |\mathbf{A}\mathbf{A}^*| = |-\mathbf{A}\mathbf{A}^{\mathrm{T}}| = -|\mathbf{A}|^2.</equation>因此可以得到<equation>|\mathbf{A}| = 0</equation>，或<equation>|\mathbf{A}| = -1.</equation>另一方面，由于<equation>A</equation>为非零矩阵，故不妨假设<equation>a_{11} \neq 0</equation>，则<equation>| \boldsymbol {A} | = a _ {1 1} A _ {1 1} + a _ {1 2} A _ {1 2} + a _ {1 3} A _ {1 3} = - \left(a _ {1 1} ^ {2} + a _ {1 2} ^ {2} + a _ {1 3} ^ {2}\right) < 0.</equation>因此，<equation>|A| = -1.</equation>

---


### 向量


