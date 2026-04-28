---

**2014年第20题 | 解答题 | 11分**

20. (本题满分11分)

设<equation>A = \left( \begin{array}{c c c c} 1 & -2 & 3 & -4 \\ 0 & 1 & -1 & 1 \\ 1 & 2 & 0 & -3 \end{array} \right), E</equation>为3阶单位矩阵.

I. 求方程组<equation>A x=0</equation>的一个基础解系；

II. 求满足<equation>A B=E</equation>的所有矩阵 B.

**答案:**(20) ( I )<equation>(-1,2,3,1)^{\mathrm{T}};</equation><equation>\text {I I)} \boldsymbol {B} = \left( \begin{array}{c c c} 2 - k _ {1} & 6 - k _ {2} & - 1 - k _ {3} \\ - 1 + 2 k _ {1} & - 3 + 2 k _ {2} & 1 + 2 k _ {3} \\ - 1 + 3 k _ {1} & - 4 + 3 k _ {2} & 1 + 3 k _ {3} \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right), \text {其 中} k _ {1}, k _ {2}, k _ {3} \text {为 任 意 常 数}.</equation>

**解析:**解（I）考察系数矩阵A.<equation>\begin{array}{l} \boldsymbol {A} = \left( \begin{array}{c c c c} 1 & - 2 & 3 & - 4 \\ 0 & 1 & - 1 & 1 \\ 1 & 2 & 0 & - 3 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c c} 1 & - 2 & 3 & - 4 \\ 0 & 1 & - 1 & 1 \\ 0 & 4 & - 3 & 1 \end{array} \right) \xrightarrow {r _ {1} + 2 r _ {2}} \left( \begin{array}{c c c c} 1 & 0 & 1 & - 2 \\ 0 & 1 & - 1 & 1 \\ 0 & 0 & 1 & - 3 \end{array} \right) \\ \xrightarrow {r _ {1} ^ {*} - r _ {3} ^ {* *}} \frac {1}{r _ {2} + r _ {3} ^ {* *}} \left( \begin{array}{c c c c} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & - 2 \\ 0 & 0 & 1 & - 3 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每作一次初等行变换，加一个<equation>*.</equation>）<equation>Ax = 0</equation>可化为方程组<equation>\left\{ \begin{array}{l} x_{1} + x_{4} = 0, \\ x_{2} - 2x_{4} = 0, \\ x_{3} - 3x_{4} = 0. \end{array} \right.</equation>由此可得<equation>\xi = (-1, 2, 3, 1)^{\mathrm{T}}</equation>为<equation>Ax = 0</equation>的一个基础解系.

（Ⅱ）实际上我们要求的是三个非齐次线性方程组<equation>A x=(1,0,0)^{\mathrm{T}}</equation>，<equation>A x=(0,1,0)^{\mathrm{T}}</equation>，<equation>A x=(0,0,1)^{\mathrm{T}}</equation>的解.由于它们的系数矩阵都是A，故可考虑对（A，E）作初等行变换，同第（I）问中的步骤可得<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {E}) = \left( \begin{array}{c c c c c c c} 1 & - 2 & 3 & - 4 & 1 & 0 & 0 \\ 0 & 1 & - 1 & 1 & 0 & 1 & 0 \\ 1 & 2 & 0 & - 3 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c c c c c} 1 & - 2 & 3 & - 4 & 1 & 0 & 0 \\ 0 & 1 & - 1 & 1 & 0 & 1 & 0 \\ 0 & 4 & - 3 & 1 & - 1 & 0 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} + 2 r _ {2}} \frac {1}{r _ {3} ^ {*} - 4 r _ {2}} \left( \begin{array}{c c c c c c c} 1 & 0 & 1 & - 2 & 1 & 2 & 0 \\ 0 & 1 & - 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & 1 & - 3 & - 1 & - 4 & 1 \end{array} \right) \xrightarrow {r _ {1} ^ {*} - r _ {3} ^ {* *}} \left( \begin{array}{c c c c c c c} 1 & 0 & 0 & 1 & 2 & 6 & - 1 \\ 0 & 1 & 0 & - 2 & - 1 & - 3 & 1 \\ 0 & 0 & 1 & - 3 & - 1 & - 4 & 1 \end{array} \right). \\ \end{array}</equation>由于<equation>\mathbf{A}</equation>为<equation>3\times4</equation>矩阵，<equation>\mathbf{E}</equation>为3阶单位矩阵，<equation>\mathbf{B}</equation>应为<equation>4\times3</equation>矩阵，从而知，<equation>(2,-1,-1,0)^{\mathrm{T}}</equation><equation>(6,-3,-4,0)^{\mathrm{T}}</equation><equation>(-1,1,1,0)^{\mathrm{T}}</equation>分别为<equation>\mathbf{Ax}=(1,0,0)^{\mathrm{T}}</equation><equation>\mathbf{Ax}=(0,1,0)^{\mathrm{T}}</equation><equation>\mathbf{Ax}=(0,0,1)^{\mathrm{T}}</equation>的一个特解.

与第（I）问中<equation>A x=0</equation>的通解相结合，得到<equation>A x=(1,0,0)^{\mathrm{T}}</equation><equation>A x=(0,1,0)^{\mathrm{T}}</equation><equation>A x=(0,0,1)^{\mathrm{T}}</equation>的通解分别为<equation>\begin{aligned} \boldsymbol {\alpha} _ {1} &= k _ {1} (- 1, 2, 3, 1) ^ {\mathrm {T}} + (2, - 1, - 1, 0) ^ {\mathrm {T}}, \\ \boldsymbol {\alpha} _ {2} &= k _ {2} (- 1, 2, 3, 1) ^ {\mathrm {T}} + (6, - 3, - 4, 0) ^ {\mathrm {T}}, \\ \boldsymbol {\alpha} _ {3} &= k _ {3} (- 1, 2, 3, 1) ^ {\mathrm {T}} + (- 1, 1, 1, 0) ^ {\mathrm {T}}, \end{aligned}</equation>其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数.

因此，<equation>B = \left( \begin{array}{c c c} 2 - k_1 & 6 - k_2 & -1 - k_3 \\ -1 + 2k_1 & -3 + 2k_2 & 1 + 2k_3 \\ -1 + 3k_1 & -4 + 3k_2 & 1 + 3k_3 \\ k_1 & k_2 & k_3 \end{array} \right)</equation>，其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数.

---

**2013年第20题 | 解答题 | 11分**

20. (本题满分11分)

设<equation>A = \left( \begin{array}{c c} 1 & a \\ 1 & 0 \end{array} \right), B = \left( \begin{array}{c c} 0 & 1 \\ 1 & b \end{array} \right)</equation>当<equation>a,b</equation>为何值时，存在矩阵<equation>C</equation>使得<equation>AC - CA = B</equation>，并求所有矩阵<equation>C</equation>

**答案:**(20)<equation>a = -1, b = 0</equation>时，<equation>C = \left( \begin{array}{c c} k_{1} + k_{2} + 1 & -k_{2} \\ k_{2} & k_{1} \end{array} \right)</equation>，其中<equation>k_{1}, k_{2}</equation>为任意常数.

**解析:**解（法一）设<equation>C = \left( \begin{array}{cc} x_{1} & x_{2} \\ x_{3} & x_{4} \end{array} \right)</equation>，则由<equation>AC-CA=B</equation>可得<equation>\left( \begin{array}{c c} 1 & a \\ 1 & 0 \end{array} \right) \left( \begin{array}{c c} x _ {1} & x _ {2} \\ x _ {3} & x _ {4} \end{array} \right) - \left( \begin{array}{c c} x _ {1} & x _ {2} \\ x _ {3} & x _ {4} \end{array} \right) \left( \begin{array}{c c} 1 & a \\ 1 & 0 \end{array} \right) = \left( \begin{array}{c c} 0 & 1 \\ 1 & b \end{array} \right).</equation>写成线性方程组的形式：<equation>\left\{ \begin{array}{l} - x _ {2} + a x _ {3} = 0, \\ - a x _ {1} + x _ {2} + a x _ {4} = 1, \\ x _ {1} - x _ {3} - x _ {4} = 1, \\ x _ {2} - a x _ {3} = b. \end{array} \right.</equation>记该线性方程组为<equation>Px = \beta ,\beta = (0,1,1,b)^{\mathrm{T}}</equation>，则<equation>Px = \beta</equation>有解当且仅当<equation>r(P,\beta) = r(P)</equation><equation>(P, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 0 & - 1 & a & 0 & 0 \\ - a & 1 & 0 & a & 1 \\ 1 & 0 & - 1 & - 1 & 1 \\ 0 & 1 & - a & 0 & b \end{array} \right) \xrightarrow {r _ {2} + a r _ {3}} \left( \begin{array}{c c c c c} 0 & - 1 & a & 0 & 0 \\ 0 & 1 & - a & 0 & a + 1 \\ 1 & 0 & - 1 & - 1 & 1 \\ 0 & 1 & - a & 0 & b \end{array} \right)</equation><equation>\xrightarrow [ r _ {4} + r _ {1} ]{r _ {2} ^ {*} + r _ {1}} \left( \begin{array}{c c c c c} 0 & - 1 & a & 0 & 0 \\ 0 & 0 & 0 & 0 & a + 1 \\ 1 & 0 & - 1 & - 1 & 1 \\ 0 & 0 & 0 & 0 & b \end{array} \right) \rightarrow \left( \begin{array}{c c c c c} 1 & 0 & - 1 & - 1 & 1 \\ 0 & 1 & - a & 0 & 0 \\ 0 & 0 & 0 & 0 & a + 1 \\ 0 & 0 & 0 & 0 & b \end{array} \right).</equation><equation>r_2^*</equation>表示对<equation>r_2</equation>作初等行变换后所得新的第二行. 由上可见，若<equation>r(\boldsymbol{P},\boldsymbol{\beta}) = r(\boldsymbol{P})</equation>，则必有<equation>a + 1 = b = 0</equation>从而<equation>a = -1</equation>，<equation>b = 0</equation>.

当 a = -1，b = 0时，<equation>(\boldsymbol {P}, \boldsymbol {\beta}) \rightarrow \left(\begin{array}{c c c c c}1&0&- 1&- 1&1\\0&1&1&0&0\\0&0&0&0&0\\0&0&0&0&0\end{array}\right),</equation>即<equation>\left\{ \begin{array}{l l} x_{2}+x_{3}=0, \\ x_{1}-x_{3}-x_{4}=1. \end{array} \right.</equation>（1,0,0,1）<equation>^{\mathrm{T}}</equation>和（1,-1,1,0）<equation>^{\mathrm{T}}</equation>为该方程组对应的齐次线性方程组的一个基础解系.又（1,0,0,0）<equation>^{\mathrm{T}}</equation>为<equation>P x=\beta</equation>的一个特解，故<equation>P x=\beta</equation>的通解为<equation>k _ {1} \left(1, 0, 0, 1\right) ^ {\mathrm {T}} + k _ {2} \left(1, - 1, 1, 0\right) ^ {\mathrm {T}} + \left(1, 0, 0, 0\right) ^ {\mathrm {T}},</equation>其中<equation>k_{1}, k_{2}</equation>为任意常数.

因此，当<equation>a = -1</equation>，<equation>b = 0</equation>时，存在C使得AC-CA=B.此时的C形如<equation>\left( \begin{array}{c c} k_{1}+k_{2}+1 & -k_{2} \\ k_{2} & k_{1} \end{array} \right)</equation>其中<equation>k_{1}, k_{2}</equation>为任意常数.

（法二）由于AC的迹等于CA的迹，故AC-CA的迹等于零.因此<equation>b=0.</equation><equation>B=\left( \begin{array}{ll}0&1\\ 1&0\end{array} \right)</equation>设<equation>C = \left( \begin{array}{cc} x_{1} & x_{2} \\ x_{3} & x_{4} \end{array} \right)</equation>，则由<equation>A C-C A=B</equation>可得<equation>\left\{ \begin{array}{l} - x _ {2} + a x _ {3} = 0, \\ - a x _ {1} + x _ {2} + a x _ {4} = 1, \\ x _ {1} - x _ {3} - x _ {4} = 1, \\ x _ {2} - a x _ {3} = 0. \end{array} \right.</equation>将<equation>x_{2}=a x_{3}</equation>代入<equation>- a x_{1}+x_{2}+a x_{4}=1</equation>可得<equation>- a \left(x_{1}-x_{3}-x_{4}\right)=1</equation>与<equation>x_{1}-x_{3}-x_{4}=1</equation>比较得，a=-1. 从而 a=-1，b=0.

其余同法一.

---

**2012年第20题 | 解答题 | 11分**

20. (本题满分11分)

设<equation>\therefore = \left( \begin{array}{c c c c} 1 & a & 0 & 0 \\ 0 & 1 & a & 0 \\ 0 & 0 & 1 & a \\ a & 0 & 0 & 1 \end{array} \right)</equation><equation>\beta = \left( \begin{array}{c} 1 \\ - 1 \\ 0 \\ 0 \end{array} \right).</equation>I. 计算行列式<equation>|A|</equation>；

II. 当实数<equation>a</equation>为何值时，方程组<equation>Ax = \beta</equation>有无穷多解，并求其通解.

**答案:**（Ⅱ）当 a=-1时，方程组<equation>A x=\beta</equation>有无穷多解，其通解为<equation>k(1,1,1,1)^{\mathrm{T}}+(0,-1,0,0)^{\mathrm{T}}</equation>其中 k为任意常数.

**解析:**（ I ）按第一行展开<equation>|A|</equation>，得<equation>| \boldsymbol {A} | = \left| \begin{array}{c c c} 1 & a & 0 \\ 0 & 1 & a \\ 0 & 0 & 1 \end{array} \right| - a \left| \begin{array}{c c c} 0 & a & 0 \\ 0 & 1 & a \\ a & 0 & 1 \end{array} \right| = 1 - a ^ {4}.</equation>（Ⅱ）（法一）<equation>A x=\beta</equation>有无穷多解的充要条件为<equation>r(A)=r(A,\beta) < 4.</equation>由<equation>r(A) < 4</equation>可得，<equation>|A| = 0</equation>，从而<equation>a = \pm 1.</equation>当 a = 1时，<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 1 & 0 & 0 & 1 & 0 \end{array} \right) \xrightarrow {r _ {4} - r _ {1}} \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & - 1 & 0 & 1 & - 1 \end{array} \right) \xrightarrow {r _ {4} ^ {*} + r _ {2}} \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1 & - 2 \end{array} \right) \\ \xrightarrow {r _ {4} ^ {* *} - r _ {3}} \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 & - 2 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）由上可知，<equation>r ( \mathbf{A}, \mathbf{\beta})=4</equation>，而<equation>r ( \mathbf{A})=3</equation>，<equation>\mathbf{Ax}=\boldsymbol{\beta}</equation>无解. a=1不符合题意.

当 a = -1时，<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 1 & - 1 & 0 & 0 & 1 \\ 0 & 1 & - 1 & 0 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ - 1 & 0 & 0 & 1 & 0 \end{array} \right) \xrightarrow {r _ {4} + r _ {1}} \left( \begin{array}{c c c c c} 1 & - 1 & 0 & 0 & 1 \\ 0 & 1 & - 1 & 0 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ 0 & - 1 & 0 & 1 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} + r _ {2}} \frac {r _ {4} ^ {*} + r _ {2}}{\left( \begin{array}{c c c c c} 1 & 0 & - 1 & 0 & 0 \\ 0 & 1 & - 1 & 0 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ 0 & 0 & - 1 & 1 & 0 \end{array} \right)} \xrightarrow {r _ {1} ^ {*} + r _ {3}} \frac {r _ {2} + r _ {3}}{r _ {4} ^ {* *} + r _ {3}} \left( \begin{array}{c c c c c} 1 & 0 & 0 & - 1 & 0 \\ 0 & 1 & 0 & - 1 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>由上可知，<equation>r(\mathbf{A},\boldsymbol{\beta}) = r(\mathbf{A}) = 3 < 4, \mathbf{Ax} = \boldsymbol{\beta}</equation>有无穷多解.

齐次方程<equation>Ax = 0</equation>的通解为<equation>k(1,1,1,1)^{\mathrm{T}}</equation>，其中<equation>k</equation>为任意常数。又因为<equation>(0,-1,0,0)^{\mathrm{T}}</equation>为<equation>Ax = \beta</equation>的一个特解，所以<equation>Ax = \beta</equation>的通解为<equation>k(1,1,1,1)^{\mathrm{T}} + (0,-1,0,0)^{\mathrm{T}}</equation>，其中<equation>k</equation>为任意常数综上所述，当<equation>a = -1</equation>时，方程组<equation>Ax = \beta</equation>有无穷多解，其通解为<equation>k(1,1,1,1)^{\mathrm{T}} + (0,-1,0,0)^{\mathrm{T}}</equation>其中<equation>k</equation>为任意常数.

（法二）对含有参数<equation>a</equation>的增广矩阵<equation>(\mathbf{A},\boldsymbol{\beta})</equation>作初等行变换.<equation>(\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ a & 0 & 0 & 1 & 0 \end{array} \right) \xrightarrow {r _ {4} - a r _ {1}} \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ 0 & - a ^ {2} & 0 & 1 & - a \end{array} \right)</equation><equation>\xrightarrow {r _ {4} ^ {*} + a ^ {2} r _ {2}} \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ 0 & 0 & a ^ {3} & 1 & - a - a ^ {2} \end{array} \right) \xrightarrow {r _ {4} ^ {* *} - a ^ {3} r _ {3}} \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ 0 & 0 & 0 & 1 - a ^ {4} & - a - a ^ {2} \end{array} \right).</equation>由于<equation>A x= \beta</equation>有无穷多解，故<equation>r ( A )=r ( A,\beta) < 4.</equation>因此，<equation>1-a^{4}=0,-a-a^{2}=0</equation>解得<equation>a=-1.</equation>其余同法一.

---

**2010年第20题 | 解答题 | 11分**

20. (本题满分11分)

设<equation>A=\left( \begin{array}{c c c} \lambda & 1 & 1 \\ 0 & \lambda-1 & 0 \\ 1 & 1 & \lambda \end{array} \right), b=\left( \begin{array}{c} a \\ 1 \\ 1 \end{array} \right).</equation>已知线性方程组<equation>A x=b</equation>存在2个不同的解.

I. 求<equation>\lambda, a</equation>;

II. 求方程组<equation>A x=b</equation>的通解.

**答案:**(20) （I）<equation>\lambda=-1,a=-2;</equation>（Ⅱ）<equation>\boldsymbol{A}\boldsymbol{x}=\boldsymbol{b}</equation>的通解为<equation>k(1,0,1)^{\mathrm{T}}+\left(\frac{3}{2},-\frac{1}{2},0\right)^{\mathrm{T}}</equation>，其中 k为任意常数.

**解析:**解（I）<equation>A x=b</equation>有两个不同的解意味着<equation>A x=b</equation>有解但不唯一，故<equation>r(A)=r(A,b)<3.</equation><equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} \lambda & 1 & 1 & a \\ 0 & \lambda - 1 & 0 & 1 \\ 1 & 1 & \lambda & 1 \end{array} \right) \xrightarrow {r _ {1} \leftrightarrow r _ {3}} \left( \begin{array}{c c c c} 1 & 1 & \lambda & 1 \\ 0 & \lambda - 1 & 0 & 1 \\ \lambda & 1 & 1 & a \end{array} \right) \xrightarrow {r _ {3} ^ {*} - \lambda r _ {1} ^ {*}} \left( \begin{array}{c c c c} 1 & 1 & \lambda & 1 \\ 0 & \lambda - 1 & 0 & 1 \\ 0 & 1 - \lambda & 1 - \lambda^ {2} & a - \lambda \end{array} \right) \\ \xrightarrow {r _ {3} ^ {* *} + r _ {2}} \left( \begin{array}{c c c c} 1 & 1 & \lambda & 1 \\ 0 & \lambda - 1 & 0 & 1 \\ 0 & 0 & 1 - \lambda^ {2} & a - \lambda + 1 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每做一次初等行变换，加一个*.）

由于<equation>r(A) < 3</equation>，故<equation>1 - \lambda^2 = 0, \lambda = \pm 1.</equation>当<equation>\lambda = 1</equation>时，<equation>r(\mathbf{A},\mathbf{b}) = 2</equation>，<equation>r(\mathbf{A}) = 1</equation>，方程组无解，舍去.

当<equation>\lambda=-1</equation>时，<equation>(A,b)\rightarrow \left( \begin{array}{c c c c}1&1&-1&1\\ 0&-2&0&1\\ 0&0&0&a+2 \end{array} \right).</equation>此时<equation>r(A)=2.</equation>若<equation>r(A)=r(A,b),</equation>则<equation>r(A,b)=2, a+2=0</equation>即<equation>a=-2.</equation>（Ⅱ）由第（I）问知，当<equation>\lambda=-1</equation>a=-2时，<equation>(\boldsymbol {A}, \boldsymbol {b}) \rightarrow \left(\begin{array}{c c c c}1&1&- 1&1\\0&- 2&0&1\\0&0&0&0\end{array}\right) \xrightarrow [ r _ {1} - r _ {2} ^ {*} ]{r _ {2} \times \left(- \frac {1}{2}\right)} \left(\begin{array}{c c c c}1&0&- 1&\frac {3}{2}\\\0&1&0&- \frac {1}{2}\\\0&0&0&0\end{array}\right).</equation>其对应的齐次方程组等价于<equation>\left\{ \begin{array}{l l} x_{1}-x_{3}=0, \\ x_{2}=0, \end{array} \right.</equation>故可取<equation>(1,0,1)^{\mathrm{T}}</equation>为该方程组的一个基础解系。又<equation>\left(\frac{3}{2},-\frac{1}{2},0\right)^{\mathrm{T}}</equation>为原方程组的一个特解，故<equation>A x=b</equation>的通解为<equation>k(1,0,1)^{\mathrm{T}}+\left(\frac{3}{2},-\frac{1}{2},0\right)^{\mathrm{T}}</equation>其中k为任意常数.

---


### 矩阵


