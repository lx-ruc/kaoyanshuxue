取<equation>x_{4}=1</equation>，可得<equation>\boldsymbol{\xi}=(3,-1,-1,1)^{\mathrm{T}}</equation>为该方程组的一个基础解系，从而<equation>(k_{1},-l_{1},k_{2},-l_{2})^{\mathrm{T}}= k(3,-1,-1,1)^{\mathrm{T}}</equation>，其中<equation>k\in\mathbf{R}.</equation>因此，<equation>\boldsymbol {\gamma} = k _ {1} \boldsymbol {\alpha} _ {1} + k _ {2} \boldsymbol {\alpha} _ {2} = 3 k \binom {1} {2} - k \binom {2} {1} = k \binom {1} {5}, \quad k \in \mathbf {R}.</equation>应选 D.

（法二）由<equation>\alpha_{1},\alpha_{2}</equation>可以生成一个平面<equation>S_{1}</equation>，由<equation>\beta_{1},\beta_{2}</equation>可以生成一个平面<equation>S_{2}</equation>，而<equation>\gamma</equation>既可由<equation>\alpha_{1},\alpha_{2}</equation>线性表示，也可由<equation>\beta_{1},\beta_{2}</equation>线性表示，这说明<equation>\gamma</equation>既在平面<equation>S_{1}</equation>上，又在平面<equation>S_{2}</equation>上。于是，<equation>\gamma</equation>既垂直于平面<equation>S_{1}</equation>的法向量<equation>n_{1}</equation>，又垂直于平面<equation>S_{2}</equation>的法向量<equation>n_{2}</equation>，从而垂直于<equation>n_{1},n_{2}</equation>生成的平面。因此<equation>\gamma</equation>与<equation>n_{1} \times n_{2}</equation>共线.

取<equation>n_{1} = \alpha_{1}\times \alpha_{2},n_{2} = \beta_{1}\times \beta_{2}</equation><equation>\boldsymbol {n} _ {1} = \boldsymbol {\alpha} _ {1} \times \boldsymbol {\alpha} _ {2} = \left| \begin{array}{c c c} \boldsymbol {i} & \boldsymbol {j} & \boldsymbol {k} \\ 1 & 2 & 3 \\ 2 & 1 & 1 \end{array} \right| = - \boldsymbol {i} + 5 \boldsymbol {j} - 3 \boldsymbol {k},</equation><equation>\boldsymbol {n} _ {2} = \boldsymbol {\beta} _ {1} \times \boldsymbol {\beta} _ {2} = \left| \begin{array}{c c c} \boldsymbol {i} & \boldsymbol {j} & \boldsymbol {k} \\ 2 & 5 & 9 \\ 1 & 0 & 1 \end{array} \right| = 5 \boldsymbol {i} + 7 \boldsymbol {j} - 5 \boldsymbol {k}.</equation><equation>\boldsymbol {n} _ {1} \times \boldsymbol {n} _ {2} = \left| \begin{array}{c c c} \boldsymbol {i} & \boldsymbol {j} & \boldsymbol {k} \\ - 1 & 5 & - 3 \\ 5 & 7 & - 5 \end{array} \right| = - 4 \boldsymbol {i} - 2 0 \boldsymbol {j} - 3 2 \boldsymbol {k}.</equation>因此，<equation>\gamma</equation>与<equation>\left( \begin{array}{c} - 4 \\ - 20 \\ - 32 \end{array} \right)</equation>共线，即<equation>\gamma = k \left( \begin{array}{c} 1 \\ 5 \\ 8 \end{array} \right)</equation>，其中<equation>k \in \mathbf{R}</equation>.

---

**2022年第7题 | 选择题 | 5分 | 答案: C**

7. 设<equation>\alpha_{1}=(\lambda,1,1)^{\mathrm{T}},\alpha_{2}=(1,\lambda,1)^{\mathrm{T}},\alpha_{3}=(1,1,\lambda)^{\mathrm{T}},\alpha_{4}=\left(1,\lambda,\lambda^{2}\right)^{\mathrm{T}}</equation>，若向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>等价，则<equation>\lambda</equation>的取值范围是（    ）

A.<equation>\{0,1\}</equation>B.<equation>\{\lambda \mid \lambda \in \mathbf{R},\lambda \neq -2\}</equation>C.<equation>\{\lambda \mid \lambda \in \mathbf{R},\lambda \neq -1,\lambda \neq -2\}</equation>D.<equation>\{\lambda \mid \lambda \in \mathbf{R},\lambda \neq -1\}</equation>

答案: C

**解析:**解（法一）当<equation>\lambda=1</equation>时，<equation>\alpha_{1}=\alpha_{2}=\alpha_{3}=\alpha_{4}=\left( \begin{array}{c}1\\ 1\\ 1 \end{array} \right).</equation>此时<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>显然等价当<equation>\lambda\neq1</equation>时，考虑矩阵<equation>A=(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4}).</equation><equation>\begin{array}{l} \boldsymbol {A} = \left( \begin{array}{c c c c} \lambda & 1 & 1 & 1 \\ 1 & \lambda & 1 & \lambda \\ 1 & 1 & \lambda & \lambda^ {2} \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 1 & 1 & \lambda & \lambda^ {2} \\ \lambda & 1 & 1 & 1 \end{array} \right) \xrightarrow {r _ {2} - r _ {1}} \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 0 & 1 - \lambda & \lambda - 1 & \lambda^ {2} - \lambda \\ 0 & 1 - \lambda^ {2} & 1 - \lambda & 1 - \lambda^ {2} \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} \times \frac {1}{1 - \lambda}} \frac {r _ {3} ^ {*} \times \frac {1}{1 - \lambda}}{r _ {3} ^ {*} \times \frac {1}{1 - \lambda}} \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 0 & 1 & - 1 & - \lambda \\ 0 & 1 + \lambda & 1 & 1 + \lambda \end{array} \right) \xrightarrow {r _ {3} ^ {* *} - (1 + \lambda) r _ {2} ^ {* *}} \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 0 & 1 & - 1 & - \lambda \\ 0 & 0 & \lambda + 2 & (\lambda + 1) ^ {2} \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每作一次初等行变换，加一个*.）

由于 A有2阶非零子式<equation>\left| \begin{array}{cc}\lambda & 1\\ 1 & \lambda \end{array} \right|</equation>，故<equation>r(A)\geqslant 2</equation>另一方面，因为不存在<equation>\lambda</equation>满足<equation>\lambda +2=(\lambda+1)^{2}=0</equation>所以<equation>r(A)=3.</equation><equation>r(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}) = 3</equation>当且仅当<equation>\lambda \neq -2.</equation><equation>r(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{4}) = 3</equation>当且仅当<equation>\lambda \neq -1.</equation>因此，当<equation>\lambda \neq 1</equation>时，<equation>r(A) = r(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4}) = r(\alpha_{1},\alpha_{2},\alpha_{3}) = r(\alpha_{1},\alpha_{2},\alpha_{4})</equation>当且仅当<equation>\lambda \neq -2</equation>且<equation>\lambda \neq -1</equation>注意到<equation>\lambda=1</equation>也包含在条件<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1</equation>中，故<equation>r(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4})=r(\alpha_{1},\alpha_{2},\alpha_{3})= r(\alpha_{1},\alpha_{2},\alpha_{4})</equation>当且仅当<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1.</equation>综上所述，应选C.

（法二）分别计算<equation>|\alpha_{1},\alpha_{2},\alpha_{3}|</equation>，<equation>|\alpha_{1},\alpha_{2},\alpha_{4}|</equation><equation>\left| \alpha_ {1}, \alpha_ {2}, \alpha_ {3} \right| = \left| \begin{array}{c c c} \lambda & 1 & 1 \\ 1 & \lambda & 1 \\ 1 & 1 & \lambda \end{array} \right| = \left| \begin{array}{c c c} \lambda & 1 - \lambda & 1 - \lambda^ {2} \\ 1 & \lambda - 1 & 1 - \lambda \\ 1 & 0 & 0 \end{array} \right| = (1 - \lambda) ^ {2} (\lambda + 2).</equation><equation>\left| \alpha_ {1}, \alpha_ {2}, \alpha_ {4} \right| = \left| \begin{array}{c c c} \lambda & 1 & 1 \\ 1 & \lambda & \lambda \\ 1 & 1 & \lambda^ {2} \end{array} \right| = \left| \begin{array}{c c c} \lambda & 1 - \lambda & 1 - \lambda^ {3} \\ 1 & \lambda - 1 & \lambda - \lambda^ {2} \\ 1 & 0 & 0 \end{array} \right| = (1 - \lambda) ^ {2} (1 + \lambda) ^ {2}.</equation>当<equation>\lambda\neq1</equation>，-2，-1时，<equation>|\alpha_{1},\alpha_{2},\alpha_{3}|</equation>与<equation>|\alpha_{1},\alpha_{2},\alpha_{4}|</equation>均不为0.此时，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>和<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>均为3维列向量组的极大无关组，从而等价.

当<equation>\lambda = 1</equation>时，<equation>\alpha_{1} = \alpha_{2} = \alpha_{3} = \alpha_{4} = \left( \begin{array}{c} 1 \\ 1 \\ 1 \end{array} \right)</equation>.此时<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>显然等价.

当<equation>\lambda = -2</equation>或<equation>\lambda = -1</equation>时，<equation>|\alpha_{1},\alpha_{2},\alpha_{3}| \neq |\alpha_{1},\alpha_{2},\alpha_{4}|</equation>，且其中一个为0，另一个不为0，说明两向量组的秩不相等，从而不等价.

综上所述，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>等价当且仅当<equation>\lambda \neq -2</equation>且<equation>\lambda \neq -1.</equation>应选C.

---

**2020年第6题 | 选择题 | 4分 | 答案: C**

6. 已知直线<equation>L_{1}:\frac{x-a_{2}}{a_{1}}=\frac{y-b_{2}}{b_{1}}=\frac{z-c_{2}}{c_{1}}</equation>与直线<equation>L_{2}:\frac{x-a_{3}}{a_{2}}=\frac{y-b_{3}}{b_{2}}=\frac{z-c_{3}}{c_{2}}</equation>相交于一点，记向量<equation>\alpha_{i}=\left( \begin{array}{c} a_{i} \\ b_{i} \\ c_{i} \end{array} \right), (i=</equation>1,2,3)，则（    ）

A.<equation>\alpha_{1}</equation>可由<equation>\alpha_{2},\alpha_{3}</equation>线性表示 B.<equation>\alpha_{2}</equation>可由<equation>\alpha_{1},\alpha_{3}</equation>线性表示

C.<equation>\alpha_{3}</equation>可由<equation>\alpha_{1},\alpha_{2}</equation>线性表示 D.<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关

答案: C

**解析:**解（法一）由<equation>l_{1}</equation>与<equation>l_{2}</equation>的方程可知，点（<equation>a_{2}, b_{2}, c_{2}</equation>）位于直线<equation>l_{1}</equation>上，点（<equation>a_{3}, b_{3}, c_{3}</equation>）位于直线<equation>l_{2}</equation>上，且<equation>\alpha_{1}</equation>为直线<equation>l_{1}</equation>的方向向量，<equation>\alpha_{2}</equation>为直线<equation>l_{2}</equation>的方向向量.

由于<equation>l_{1}</equation>与<equation>l_{2}</equation>相交于一点，故它们的方向向量<equation>\alpha_{1},\alpha_{2}</equation>不共线，从而<equation>\alpha_{1},\alpha_{2}</equation>线性无关.此外，<equation>l_{1}</equation>与<equation>l_{2}</equation>相交于一点说明它们共面.

记<equation>\boldsymbol{\beta}^{\mathrm{T}}=\left(a_{3}-a_{2},b_{3}-b_{2},c_{3}-c_{2}\right)</equation>，则直线<equation>l_{3}:\frac{x-a_{2}}{a_{3}-a_{2}}=\frac{y-b_{2}}{b_{3}-b_{2}}=\frac{z-c_{2}}{c_{3}-c_{2}}</equation>位于<equation>l_{1}</equation>与<equation>l_{2}</equation>所在平面，<equation>\boldsymbol{\beta}</equation>为<equation>l_{3}</equation>的方向向量.

由于三向量共面的充分必要条件是它们的混合积为零，故<equation>\left| \begin{array}{c c c} a_{1} & b_{1} & c_{1} \\ a_{2} & b_{2} & c_{2} \\ a_{3}-a_{2} & b_{3}-b_{2} & c_{3}-c_{2} \end{array} \right|=0.</equation>由行列式的性质可知<equation>\left| \begin{array}{c c c} a_{1} & b_{1} & c_{1} \\ a_{2} & b_{2} & c_{2} \\ a_{3} & b_{3} & c_{3} \end{array} \right|=0</equation>，从而<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性相关.

又因为<equation>\alpha_{1},\alpha_{2}</equation>线性无关，所以<equation>\alpha_{3}</equation>可由<equation>\alpha_{1},\alpha_{2}</equation>线性表示.应选C.

（法二）不妨认为<equation>a_{1}b_{1}c_{1}\neq 0,a_{2}b_{2}c_{2}\neq 0.a_{i},b_{i},c_{i}(i = 1,2)</equation>中存在0的情况不影响讨论.设<equation>l_{1}</equation>与<equation>l_{2}</equation>相交于点<equation>M(x_{0},y_{0},z_{0})</equation>，则点M的坐标既满足<equation>l_{1}</equation>的方程，又满足<equation>l_{2}</equation>的方程.于是，<equation>\frac {x _ {0} - a _ {2}}{a _ {1}} = \frac {y _ {0} - b _ {2}}{b _ {1}} = \frac {z _ {0} - c _ {2}}{c _ {1}} = k _ {1}, \quad \frac {x _ {0} - a _ {3}}{a _ {2}} = \frac {y _ {0} - b _ {3}}{b _ {2}} = \frac {z _ {0} - c _ {3}}{c _ {2}} = k _ {2}.</equation>由（1）式可得<equation>\begin{aligned} x _ {0} &= a _ {2} + k _ {1} a _ {1} = a _ {3} + k _ {2} a _ {2}, \\ y _ {0} &= b _ {2} + k _ {1} b _ {1} = b _ {3} + k _ {2} b _ {2}, \\ z _ {0} &= c _ {2} + k _ {1} c _ {1} = c _ {3} + k _ {2} c _ {2}. \end{aligned}</equation>整理可得<equation>\begin{aligned} a _ {3} &= k _ {1} a _ {1} + \left(1 - k _ {2}\right) a _ {2}, \\ b _ {3} &= k _ {1} b _ {1} + \left(1 - k _ {2}\right) b _ {2}, \\ c _ {3} &= k _ {1} c _ {1} + \left(1 - k _ {2}\right) c _ {2}, \end{aligned}</equation>即<equation>\boldsymbol{\alpha}_{3} = k_{1}\boldsymbol{\alpha}_{1} + (1 - k_{2})\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>可由<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2}</equation>线性表示. 应选C.

---

**2013年第5题 | 选择题 | 4分 | 答案: B**

5. 设 A,B,C均为 n阶矩阵，若 AB=C，且 B可逆，则（    ）

A. 矩阵 C的行向量组与矩阵 A的行向量组等价

B. 矩阵 C的列向量组与矩阵 A的列向量组等价

C. 矩阵 C的行向量组与矩阵 B的行向量组等价

D. 矩阵 C的列向量组与矩阵 B的列向量组等价

答案: B

**解析:**我们证明 C的列向量组与 A的列向量组能相互线性表示.

不妨设<equation>A = \left(\alpha_{1},\alpha_{2},\dots ,\alpha_{n}\right),C = \left(\gamma_{1},\gamma_{2},\dots ,\gamma_{n}\right),B = \left(b_{ij}\right)_{n\times n}</equation>，则<equation>\boldsymbol {A B} = \left(\alpha_ {1}, \alpha_ {2}, \dots , \alpha_ {n}\right) \left(b _ {i j}\right) _ {n \times n} = \boldsymbol {C} = \left(\gamma_ {1}, \gamma_ {2}, \dots , \gamma_ {n}\right),</equation><equation>\left\{ \begin{array}{l} \boldsymbol {\gamma} _ {1} = b _ {1 1} \boldsymbol {\alpha} _ {1} + b _ {2 1} \boldsymbol {\alpha} _ {2} + \dots + b _ {n 1} \boldsymbol {\alpha} _ {n}, \\ \boldsymbol {\gamma} _ {2} = b _ {1 2} \boldsymbol {\alpha} _ {1} + b _ {2 2} \boldsymbol {\alpha} _ {2} + \dots + b _ {n 2} \boldsymbol {\alpha} _ {n}, \\ \dots , \\ \boldsymbol {\gamma} _ {n} = b _ {1 n} \boldsymbol {\alpha} _ {1} + b _ {2 n} \boldsymbol {\alpha} _ {2} + \dots + b _ {n n} \boldsymbol {\alpha} _ {n}. \end{array} \right.</equation>因此，C的列向量组<equation>\left( \gamma_{1},\gamma_{2},\dots,\gamma_{n}\right)</equation>能由A的列向量组<equation>\left( \alpha_{1},\alpha_{2},\dots,\alpha_{n}\right)</equation>线性表示。同理，由于B可逆，故A的列向量组也能由C的列向量组线性表示.应选B.

下面我们说明选项 A、C、D不正确.

令<equation>A=\left( \begin{array}{cc}1&1\\ 0&0 \end{array} \right), B=\left( \begin{array}{cc}1&1\\ 0&1 \end{array} \right)</equation>，则<equation>C=A B=\left( \begin{array}{cc}1&2\\ 0&0 \end{array} \right).</equation>但A的行向量组<equation>\{(1,1),(0,0)\}</equation>与C的行向量组<equation>\{(1,2),(0,0)\}</equation>不等价.选项A不正确.

取 B为单位矩阵 E，C为一个非满秩矩阵. B的行（列）向量组线性无关，C的行（列）向量组线性相关. 选项C、D不正确.

---

**2011年第20题 | 解答题 | 11分**


设向量组<equation>\alpha_{1}=(1,0,1)^{\mathrm{T}},\alpha_{2}=(0,1,1)^{\mathrm{T}},\alpha_{3}=(1,3,5)^{\mathrm{T}}</equation>不能由向量组<equation>\beta_{1}=(1,1,1)^{\mathrm{T}},\beta_{2}=(1,2,3)^{\mathrm{T}},\beta_{3}=(3,4,a)^{\mathrm{T}}</equation>线性表示.

I. 求 a的值；

II. 将<equation>\beta_{1},\beta_{2},\beta_{3}</equation>用<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性表示.

**答案:**(20) ( I )<equation>a=5;</equation>( II )<equation>\boldsymbol{\beta}_{1}=2\boldsymbol{\alpha}_{1}+4\boldsymbol{\alpha}_{2}-\boldsymbol{\alpha}_{3},\boldsymbol{\beta}_{2}=\boldsymbol{\alpha}_{1}+2\boldsymbol{\alpha}_{2},\boldsymbol{\beta}_{3}=5\boldsymbol{\alpha}_{1}+10\boldsymbol{\alpha}_{2}-2\boldsymbol{\alpha}_{3}.</equation>

**解析:**解（ I ）记<equation>A=\left(\alpha_{1},\alpha_{2},\alpha_{3}\right),B=\left(\beta_{1},\beta_{2},\beta_{3}\right),A,B</equation>的列向量组分别记为 A,B.

首先，<equation>|A|=\left| \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 1 & 1 & 5 \end{array} \right|=1</equation>，故<equation>r(A)=3</equation>，A满秩.

由于向量组 B不能线性表示 A，故<equation>r(\mathbf{B})<3</equation>；否则 B也满秩，从而 B能线性表示 A，矛盾.由于<equation>r(\mathbf{B})<3</equation>，故<equation>| \boldsymbol {B} | = \left| \begin{array}{c c c} 1 & 1 & 3 \\ 1 & 2 & 4 \\ 1 & 3 & a \end{array} \right| \frac {c _ {2} - c _ {1}}{c _ {3} - 3 c _ {1}} \left| \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 1 \\ 1 & 2 & a - 3 \end{array} \right| = a - 5 = 0.</equation>因此，<equation>a=5.</equation>（Ⅱ）（法一）求<equation>B</equation>用<equation>A</equation>的线性表示，相当于求<equation>AX = B</equation>的解.<equation>X</equation>的列向量的坐标为线性表示的系数，即<equation>(\alpha_{1},\alpha_{2},\alpha_{3})\left(x_{1i},x_{2i},x_{3i}\right)^{\mathrm{T}} = \beta_{i}(i = 1,2,3)</equation>.<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {B}) = \left( \begin{array}{c c c c c c} 1 & 0 & 1 & 1 & 1 & 3 \\ 0 & 1 & 3 & 1 & 2 & 4 \\ 1 & 1 & 5 & 1 & 3 & 5 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c c c c} 1 & 0 & 1 & 1 & 1 & 3 \\ 0 & 1 & 3 & 1 & 2 & 4 \\ 0 & 1 & 4 & 0 & 2 & 2 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {*} - r _ {2}} \left( \begin{array}{c c c c c c} 1 & 0 & 1 & 1 & 1 & 3 \\ 0 & 1 & 3 & 1 & 2 & 4 \\ 0 & 0 & 1 & - 1 & 0 & - 2 \end{array} \right) \xrightarrow {r _ {1} - r _ {3} ^ {* *}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 2 & 1 & 5 \\ 0 & 1 & 0 & 4 & 2 & 1 0 \\ 0 & 0 & 1 & - 1 & 0 & - 2 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每做一次初等行变换，加一个*.）

因此，<equation>Ax = \beta_{1}</equation>的解为<equation>(2,4,-1)^{\mathrm{T}},\beta_{1} = 2\alpha_{1} + 4\alpha_{2} - \alpha_{3};Ax = \beta_{2}</equation>的解为<equation>(1,2,0)^{\mathrm{T}},\beta_{2} = \alpha_{1} + 2\alpha_{2};Ax = \beta_{3}</equation>的解为<equation>(5,10,-2)^{\mathrm{T}},\beta_{3} = 5\alpha_{1} + 10\alpha_{2} - 2\alpha_{3}.</equation>（法二）用克拉默法则分别求<equation>A x=\beta_{1}, A x=\beta_{2}, A x=\beta_{3}</equation>的解. x的分量为线性表示的系数，即<equation>\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)\left(x_{1},x_{2},x_{3}\right)^{\mathrm{T}}=\beta_{i}(i=1,2,3).</equation>首先，可计算得<equation>|A| = 1</equation>. 由克拉默法则知，<equation>Ax = \beta_{1}</equation>的解为<equation>x _ {1} = \left| \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 3 \\ 1 & 1 & 5 \end{array} \right| = 2, \quad x _ {2} = \left| \begin{array}{c c c} 1 & 1 & 1 \\ 0 & 1 & 3 \\ 1 & 1 & 5 \end{array} \right| = 4, \quad x _ {3} = \left| \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 1 \end{array} \right| = - 1.</equation>因此，<equation>\pmb{\beta}_{1} = 2\pmb{\alpha}_{1} + 4\pmb{\alpha}_{2} - \pmb{\alpha}_{3}</equation>。同理可得<equation>\pmb{\beta}_{2} = \pmb{\alpha}_{1} + 2\pmb{\alpha}_{2},\pmb{\beta}_{3} = 5\pmb{\alpha}_{1} + 10\pmb{\alpha}_{2} - 2\pmb{\alpha}_{3}</equation>。

---


#### 向量内积与向量正交

**2023年第15题 | 填空题 | 5分**

15. 已知向量<equation>\alpha_{1}=\left( \begin{array}{c}1\\ 0\\ 1\\ 1 \end{array} \right),\alpha_{2}=\left( \begin{array}{c}-1\\ -1\\ 0\\ 1 \end{array} \right),\alpha_{3}=\left( \begin{array}{c}0\\ 1\\ -1\\ 1 \end{array} \right),\beta=\left( \begin{array}{c}1\\ 1\\ 1\\ -1 \end{array} \right),\gamma=k_{1}\alpha_{1}+k_{2}\alpha_{2}+k_{3}\alpha_{3}</equation>，若<equation>\gamma^{\mathrm{T}}\alpha_{i}=\beta^{\mathrm{T}}\alpha_{i}</equation>（i=1,2,3），

则<equation>k_{1}^{2}+k_{2}^{2}+k_{3}^{2}=</equation>___

**答案:**# 11 9.

**解析:**注意到<equation>\alpha_{1}^{\mathrm{T}}\alpha_{2} = \alpha_{2}^{\mathrm{T}}\alpha_{3} = \alpha_{3}^{\mathrm{T}}\alpha_{1} = 0</equation>，故<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>相互正交，从而<equation>\begin{aligned} \boldsymbol {\gamma} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {1} &= \left(k _ {1} \boldsymbol {\alpha} _ {1} + k _ {2} \boldsymbol {\alpha} _ {2} + k _ {3} \boldsymbol {\alpha} _ {3}\right) ^ {\mathrm {T}} \boldsymbol {\alpha} _ {1} = k _ {1} \| \boldsymbol {\alpha} _ {1} \| ^ {2} = 3 k _ {1}, \\ \boldsymbol {\gamma} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {2} &= \left(k _ {1} \boldsymbol {\alpha} _ {1} + k _ {2} \boldsymbol {\alpha} _ {2} + k _ {3} \boldsymbol {\alpha} _ {3}\right) ^ {\mathrm {T}} \boldsymbol {\alpha} _ {2} = k _ {2} \| \boldsymbol {\alpha} _ {2} \| ^ {2} = 3 k _ {2}, \\ \boldsymbol {\gamma} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {3} &= \left(k _ {1} \boldsymbol {\alpha} _ {1} + k _ {2} \boldsymbol {\alpha} _ {2} + k _ {3} \boldsymbol {\alpha} _ {3}\right) ^ {\mathrm {T}} \boldsymbol {\alpha} _ {3} = k _ {3} \| \boldsymbol {\alpha} _ {3} \| ^ {2} = 3 k _ {3}. \end{aligned}</equation>计算可得<equation>\boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {1} = 1, \quad \boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {2} = - 3, \quad \boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {3} = - 1.</equation>由<equation>\boldsymbol{\gamma}^{\mathrm{T}}\boldsymbol{\alpha}_{i} = \boldsymbol{\beta}^{\mathrm{T}}\boldsymbol{\alpha}_{i}(i = 1,2,3)</equation>可得，<equation>3 k _ {1} = 1, \quad 3 k _ {2} = - 3, \quad 3 k _ {3} = - 1.</equation>解得<equation>k_{1} = \frac{1}{3}, k_{2} = -1, k_{3} = -\frac{1}{3}</equation>.

因此，<equation>k_{1}^{2}+k_{2}^{2}+k_{3}^{2}=\frac{1}{9}+1+\frac{1}{9}=\frac{11}{9}.</equation>

---

**2021年第6题 | 选择题 | 5分 | 答案: A**

6. 已知<equation>\alpha_{1}=\left( \begin{array}{c}1\\ 0\\ 1 \end{array} \right),\alpha_{2}=\left( \begin{array}{c}1\\ 2\\ 1 \end{array} \right),\alpha_{3}=\left( \begin{array}{c}3\\ 1\\ 2 \end{array} \right),\beta_{1}=\alpha_{1},\beta_{2}=\alpha_{2}-k\beta_{1},\beta_{3}=\alpha_{3}-l_{1}\beta_{1}-l_{2}\beta_{2}</equation>，若<equation>\beta_{1},\beta_{2},\beta_{3}</equation>两两正交，则<equation>l_{1},l_{2}</equation>依次为（    )

A.<equation>\frac{5}{2},\frac{1}{2}</equation>B.<equation>-\frac{5}{2},\frac{1}{2}</equation>C.<equation>\frac{5}{2},-\frac{1}{2}</equation>D.<equation>-\frac{5}{2},-\frac{1}{2}</equation>

答案: A

**解析:**将<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>施密特正交化.<equation>\boldsymbol {\beta} _ {1} = \boldsymbol {\alpha} _ {1} = \left( \begin{array}{c} 1 \\ 0 \\ 1 \end{array} \right),</equation><equation>\boldsymbol {\beta} _ {2} = \boldsymbol {\alpha} _ {2} - \frac {\left(\boldsymbol {\beta} _ {1} , \boldsymbol {\alpha} _ {2}\right)}{\| \boldsymbol {\beta} _ {1} \| ^ {2}} \boldsymbol {\beta} _ {1} = \left( \begin{array}{c} 1 \\ 2 \\ 1 \end{array} \right) - \frac {2}{2} \left( \begin{array}{c} 1 \\ 0 \\ 1 \end{array} \right) = \left( \begin{array}{c} 0 \\ 2 \\ 0 \end{array} \right),</equation><equation>\boldsymbol {\beta} _ {3} = \boldsymbol {\alpha} _ {3} - \frac {\left(\boldsymbol {\beta} _ {1} , \boldsymbol {\alpha} _ {3}\right)}{\| \boldsymbol {\beta} _ {1} \| ^ {2}} \boldsymbol {\beta} _ {1} - \frac {\left(\boldsymbol {\beta} _ {2} , \boldsymbol {\alpha} _ {3}\right)}{\| \boldsymbol {\beta} _ {2} \| ^ {2}} \boldsymbol {\beta} _ {2} = \boldsymbol {\alpha} _ {3} - \frac {5}{2} \boldsymbol {\beta} _ {1} - \frac {1}{2} \boldsymbol {\beta} _ {2}.</equation>因此，<equation>l_{1}=\frac{5}{2}, l_{2}=\frac{1}{2}.</equation>应选A.

---

**2019年第20题 | 解答题 | 11分**

20. (本题满分11分)

设向量组<equation>\alpha_{1}=(1,2,1)^{\mathrm{T}},\alpha_{2}=(1,3,2)^{\mathrm{T}},\alpha_{3}=(1,a,3)^{\mathrm{T}}</equation>为<equation>\mathbf{R}^{3}</equation>的一个基，<equation>\beta=(1,1,1)^{\mathrm{T}}</equation>在这个基下的坐标为<equation>(b,c,1)^{\mathrm{T}}</equation>.

I. 求 a,b,c ;

II. 证明<equation>\alpha_{2},\alpha_{3},\beta</equation>为<equation>\mathbf{R}^{3}</equation>的一个基，并求<equation>\alpha_{2},\alpha_{3},\beta</equation>到<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>的过渡矩阵.

**答案:**（ I ）<equation>a=3,b=2,c=-2;</equation>（Ⅱ）证明略，过渡矩阵为<equation>\left( \begin{array}{c c c}1&1&0\\ -\frac{1}{2}&0&1\\ \frac{1}{2}&0&0 \end{array} \right).</equation>

**解析:**解（I）（法一）由于<equation>\beta</equation>在<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>作为基时的坐标为<equation>(b,c,1)^{\mathrm{T}}</equation>，故<equation>\beta = b\alpha_{1} + c\alpha_{2} + \alpha_{3}</equation>将<equation>\alpha_{1},\alpha_{2},\alpha_{3},\beta</equation>的表达式代入，可得方程组<equation>b + c + 1 = 1,</equation><equation>\left\{2 b + 3 c + a = 1, \right.</equation><equation>b + 2 c + 3 = 1.</equation>(3) 式 - (1) 式可得<equation>c = -2</equation>，再由（1）式可得<equation>b = 2</equation>，然后代入（2）式可得<equation>a = 3</equation>因此，<equation>a=3,b=2,c=-2.</equation>（法二）记<equation>A=(\alpha_{1},\alpha_{2},\alpha_{3})</equation>，则由题意可知（b，c，1）<equation>^{\mathrm{T}}</equation>是<equation>A x=\beta</equation>的唯一解.于是，<equation>r(A)= r(A,\beta)=3.</equation>对（A,<equation>\beta</equation>）作初等行变换.<equation>(\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 2 & 3 & a & 1 \\ 1 & 2 & 3 & 1 \end{array} \right) \xrightarrow [ r _ {3} - r _ {1} ]{r _ {2} - 2 r _ {1}} \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 0 & 1 & a - 2 & - 1 \\ 0 & 1 & 2 & 0 \end{array} \right) \xrightarrow [ r _ {3} - r _ {2} ^ {*} ]{r _ {1} - r _ {2} ^ {*}} \left( \begin{array}{c c c c} 1 & 0 & 3 - a & 2 \\ 0 & 1 & a - 2 & - 1 \\ 0 & 0 & 4 - a & 1 \end{array} \right).</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每作一次初等行变换，加一个*.）

由于<equation>r(\mathbf{A}) = r(\mathbf{A},\boldsymbol{\beta}) = 3</equation>，故<equation>4 - a\neq 0.</equation>进一步对所得矩阵作初等行变换.<equation>(\boldsymbol {A}, \boldsymbol {\beta}) \rightarrow \left(\begin{array}{c c c c}1&0&3 - a&2\\0&1&a - 2&- 1\\0&0&1&\frac {1}{4 - a}\end{array}\right).</equation>因为<equation>(b, c, 1)^{\mathrm{T}}</equation>是<equation>Ax = \beta</equation>的唯一解，所以<equation>\frac{1}{4 - a} = 1</equation>，解得<equation>a = 3</equation>代入 a=3，可得<equation>(\boldsymbol {A}, \boldsymbol {\beta}) \rightarrow \left(\begin{array}{c c c c}1&0&0&2\\0&1&1&- 1\\0&0&1&1\end{array}\right)\rightarrow \left(\begin{array}{c c c c}1&0&0&2\\0&1&0&- 2\\0&0&1&1\end{array}\right).</equation>于是，<equation>b=2,c=-2.</equation>因此，<equation>a=3,b=2,c=-2.</equation>（Ⅱ）由于<equation>\mathbf{R}^{3}</equation>的维数是3，故要证明<equation>\alpha_{2},\alpha_{3},\beta</equation>为<equation>\mathbf{R}^{3}</equation>的一个基，只需证明<equation>\alpha_{2},\alpha_{3},\beta</equation>线性无关计算<equation>|\alpha_{2},\alpha_{3},\beta|.</equation><equation>\left| \alpha_ {2}, \alpha_ {3}, \beta \right| = \left| \begin{array}{c c c} 1 & 1 & 1 \\ 3 & 3 & 1 \\ 2 & 3 & 1 \end{array} \right| \xlongequal {c _ {2} - c _ {1}} \left| \begin{array}{c c c} 1 & 0 & 1 \\ 3 & 0 & 1 \\ 2 & 1 & 1 \end{array} \right| \xlongequal {\text {按 第二 列 展 开}} 2 \neq 0.</equation>因此，<equation>\alpha_{2},\alpha_{3},\beta</equation>线性无关，<equation>r(\alpha_{2},\alpha_{3},\beta) = 3,\alpha_{2},\alpha_{3},\beta</equation>为<equation>\mathbf{R}^{3}</equation>的一个基.

要计算从<equation>\alpha_{2},\alpha_{3},\beta</equation>到<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>的过渡矩阵，即求可逆矩阵<equation>P</equation>，使得<equation>(\alpha_{1},\alpha_{2},\alpha_{3}) = (\alpha_{2},\alpha_{3},\beta)P.</equation>对<equation>(\alpha_{2},\alpha_{3},\beta ,\alpha_{1},\alpha_{2},\alpha_{3})</equation>作初等行变换.<equation>\begin{array}{l} \left(\alpha_ {2}, \alpha_ {3}, \boldsymbol {\beta}, \alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) = \left( \begin{array}{c c c c c} 1 & 1 & 1 & 1 & 1 \\ 3 & 3 & 1 & 2 & 3 \\ 2 & 3 & 1 & 1 & 2 \\ 3 \end{array} \right) \xrightarrow [ r _ {2} ^ {*} \leftrightarrow r _ {3} ^ {*} ]{r _ {2} - 3 r _ {1}} \left( \begin{array}{c c c c c} 1 & 1 & 1 & 1 & 1 \\ 0 & 1 & - 1 & - 1 & 0 \\ 0 & 0 & - 2 & - 1 & 0 \\ 0 \end{array} \right) \\ \xrightarrow {r _ {1} - r _ {2} ^ {* *}} \frac {r _ {1} - r _ {2} ^ {* *}}{r _ {3} ^ {* *} \times \left(- \frac {1}{2}\right)} \left( \begin{array}{c c c c c} 1 & 0 & 2 & 2 & 1 & 0 \\ 0 & 1 & - 1 & - 1 & 0 & 1 \\ 0 & 0 & 1 & \frac {1}{2} & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} ^ {*} - 2 r _ {3} ^ {* * *}} \left( \begin{array}{c c c c c} 1 & 0 & 0 & 1 & 1 & 0 \\ 0 & 1 & 0 & - \frac {1}{2} & 0 & 1 \\ 0 & 0 & 1 & \frac {1}{2} & 0 & 0 \end{array} \right). \\ \end{array}</equation>因此，所求过渡矩阵<equation>P</equation>为<equation>\left( \begin{array}{c c c} 1 & 1 & 0 \\ -\frac{1}{2} & 0 & 1 \\ \frac{1}{2} & 0 & 0 \end{array} \right).</equation>

---

**2015年第20题 | 解答题 | 11分**

20. 设向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>为<equation>\mathbf{R}^{3}</equation>的一个基，<equation>\beta_{1}=2\alpha_{1}+2k\alpha_{3},\beta_{2}=2\alpha_{2},\beta_{3}=\alpha_{1}+(k+1)\alpha_{3}</equation>I. 证明向量组<equation>\beta_{1},\beta_{2},\beta_{3}</equation>为<equation>\mathbf{R}^{3}</equation>的一个基；

II. 当 k为何值时，存在非零向量<equation>\xi</equation>在基<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与基<equation>\beta_{1},\beta_{2},\beta_{3}</equation>下的坐标相同，并求所有的<equation>\xi.</equation>

**答案:**（Ⅱ）当 k=0时，存在非零向量<equation>\boldsymbol{\xi}</equation>在基<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>与基<equation>\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3}</equation>下的坐标相同，满足上述条件的所有<equation>\boldsymbol{\xi}=c\boldsymbol{\alpha}_{1}-c\boldsymbol{\alpha}_{3}</equation>，其中c为任意非零常数.

**解析:**解（I）（法一）由题设知<equation>(\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3}) = (\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3})\left( \begin{array}{c c c} 2 & 0 & 1 \\ 0 & 2 & 0 \\ 2k & 0 & k + 1 \end{array} \right)</equation>. 由于<equation>\left| \begin{array}{c c c} 2 & 0 & 1 \\ 0 & 2 & 0 \\ 2 k & 0 & k + 1 \end{array} \right| = 2 \left| \begin{array}{c c} 2 & 1 \\ 2 k & k + 1 \end{array} \right| = 4 \neq 0,</equation>故<equation>\left( \begin{array}{c c c} 2 & 0 & 1 \\ 0 & 2 & 0 \\ 2 k & 0 & k + 1 \end{array} \right)</equation>为可逆矩阵.又<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>为<equation>\mathbf{R}^{3}</equation>的基，故<equation>r(\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3})=r(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{2})=\dim \mathbf{R}^{3}</equation>从而<equation>\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3}</equation>为<equation>\mathbf{R}^{3}</equation>的一个基，结论得证.

（法二）设常数<equation>k_{1},k_{2},k_{3}</equation>满足<equation>k_{1}\boldsymbol{\beta}_{1} + k_{2}\boldsymbol{\beta}_{2} + k_{3}\boldsymbol{\beta}_{3} = \mathbf{0}</equation>，即<equation>k_{1}\left(2\boldsymbol{\alpha}_{1} + 2k\boldsymbol{\alpha}_{3}\right) + 2k_{2}\boldsymbol{\alpha}_{2} + k_{3}\left[\boldsymbol{\alpha}_{1} + (k + 1)\boldsymbol{\alpha}_{3}\right] = \mathbf{0},</equation>整理得到<equation>(2k_{1} + k_{3})\boldsymbol{\alpha}_{1} + 2k_{2}\boldsymbol{\alpha}_{2} + \left[(2k_{1} + k_{3})k + k_{3}\right]\boldsymbol{\alpha}_{3} = \mathbf{0}.</equation>由于<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>为<equation>\mathbf{R}^{3}</equation>的一个基，故它们线性无关，从而<equation>2 k _ {1} + k _ {3} = 0, \quad 2 k _ {2} = 0, \quad \left(2 k _ {1} + k _ {3}\right) k + k _ {3} = 0,</equation>解得<equation>k_{1}=0,k_{2}=0,k_{3}=0</equation>因此<equation>\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3}</equation>线性无关.于是<equation>r(\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3})=3=\dim \mathbf{R}^{3}</equation>从而<equation>\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},</equation><equation>\boldsymbol{\beta}_{3}</equation>为<equation>\mathbf{R}^{3}</equation>的一个基，结论得证.

（Ⅱ）设<equation>\pmb{\xi} = x_{1}\pmb{\alpha}_{1} + x_{2}\pmb{\alpha}_{2} + x_{3}\pmb{\alpha}_{3} = x_{1}\pmb{\beta}_{1} + x_{2}\pmb{\beta}_{2} + x_{3}\pmb{\beta}_{3}</equation>，则<equation>\left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\alpha} _ {2}, \boldsymbol {\alpha} _ {3}\right) \binom {x _ {1}} {x _ {2}} = \left(\boldsymbol {\beta} _ {1}, \boldsymbol {\beta} _ {2}, \boldsymbol {\beta} _ {3}\right) \binom {x _ {1}} {x _ {2}} = \left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\alpha} _ {2}, \boldsymbol {\alpha} _ {3}\right) \binom {2 0 1} {0 2 0} \binom {x _ {1}} {x _ {2}}.</equation>由<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>为<equation>\mathbf{R}^{3}</equation>的一个基以及坐标表示的唯一性知，<equation>\begin{aligned} \left( \begin{array}{c c c} 2 & 0 & 1 \\ 0 & 2 & 0 \\ 2 k & 0 & k + 1  \right) \left(  x _ {1} \\ x _ {2} \\ x _ {3}  \right) &= \left(  x _ {1} \\ x _ {2} \\ x _ {3}  \right), \quad \text {即} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 2 k & 0 & k  \right) \left(  x _ {1} \\ x _ {2} \\ x _ {3}  \right) &= \mathbf {0}. \end{aligned}</equation>因此存在非零向量<equation>\boldsymbol{\xi}</equation>在基<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与基<equation>\beta_{1},\beta_{2},\beta_{3}</equation>下的坐标相同当且仅当方程组（1）有非零解.该条件等价于<equation>\left| \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 2 k & 0 & k \end{array} \right| = - k = 0</equation>即<equation>k=0</equation>此时，方程组（1）的所有非零解为（c，0，<equation>- c )^{\mathrm{T}}</equation>其中c为任意非零常数.

综上所述，当<equation>k = 0</equation>时，存在非零向量<equation>\boldsymbol{\xi}</equation>在基<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>与基<equation>\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3}</equation>下的坐标相同，满足上述条件的所有<equation>\boldsymbol{\xi}=c\boldsymbol{\alpha}_{1}-c\boldsymbol{\alpha}_{3}</equation>，其中c为任意非零常数.

---

**2010年第13题 | 填空题 | 4分**

13. 设<equation>\alpha_{1}=(1,2,-1,0)^{\mathrm{T}},\alpha_{2}=(1,1,0,2)^{\mathrm{T}},\alpha_{3}=(2,1,1,a)^{\mathrm{T}}</equation>. 若由<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>生成的向量空间的维数为2，则 a=

**解析:**解（法一）由于由<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>生成的向量空间的维数为2，故向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>的秩为2，从而矩阵<equation>\left( \alpha_{1},\alpha_{2},\alpha_{3}\right)=\left( \begin{array}{c c c}1&1&2\\2&1&1\\-1&0&1\\0&2&a\end{array}\right)</equation>的秩为2.于是矩阵<equation>\left( \alpha_{1},\alpha_{2},\alpha_{3}\right)</equation>中任意3阶子式均为0，因此<equation>\left| \begin{array}{c c c}1&1&2\\-1&0&1\\0&2&a\end{array}\right|=0</equation>，解得 a=6.

（法二）由于由<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>生成的向量空间的维数为2，故<equation>r(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3})=2</equation>.又因为<equation>\left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\alpha} _ {2}, \boldsymbol {\alpha} _ {3}\right) = \left( \begin{array}{c c c} 1 & 1 & 2 \\ 2 & 1 & 1 \\ - 1 & 0 & 1 \\ 0 & 2 & a \end{array} \right) \xrightarrow [ r _ {3} + r _ {1} ]{r _ {2} - 2 r _ {1}} \left( \begin{array}{c c c} 1 & 1 & 2 \\ 0 & - 1 & - 3 \\ 0 & 1 & 3 \\ 0 & 2 & a \end{array} \right) \xrightarrow [ r _ {4} + 2 r _ {2} ]{r _ {3} + r _ {2}} \left( \begin{array}{c c c} 1 & 1 & 2 \\ 0 & - 1 & - 3 \\ 0 & 0 & 0 \\ 0 & 0 & a - 6 \end{array} \right),</equation>所以 a=6.

---

**2009年第5题 | 选择题 | 4分 | 答案: A**

5. 设<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>是3维向量空间<equation>\mathbf{R}^{3}</equation>的一组基，则由基<equation>\alpha_{1},\frac{1}{2}\alpha_{2},\frac{1}{3}\alpha_{3}</equation>到基<equation>\alpha_{1}+\alpha_{2},\alpha_{2}+\alpha_{3},\alpha_{3}+\alpha_{1}</equation>的过渡矩阵为（    ）

A.<equation>\left( \begin{array}{c c c} 1 & 0 & 1 \\ 2 & 2 & 0 \\ 0 & 3 & 3 \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c} 1 & 2 & 0 \\ 0 & 2 & 3 \\ 1 & 0 & 3 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c} \frac {1}{2} & \frac {1}{4} & - \frac {1}{6} \\ - \frac {1}{2} & \frac {1}{4} & \frac {1}{6} \\ \frac {1}{2} & - \frac {1}{4} & \frac {1}{6} \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} \frac {1}{2} & - \frac {1}{2} & \frac {1}{2} \\ \frac {1}{4} & \frac {1}{4} & - \frac {1}{4} \\ - \frac {1}{6} & \frac {1}{6} & \frac {1}{6} \end{array} \right)</equation>

答案: A

---


### 行列式

**2021年第15题 | 填空题 | 5分**

15. 设<equation>A=\left(a_{ij}\right)</equation>为3阶矩阵，<equation>A_{ij}</equation>为元素<equation>a_{ij}</equation>的代数余子式，若 A的每行元素之和均为2，且<equation>|A|=3</equation>，则<equation>A_{11}+A_{21}+</equation><equation>A_{31}=</equation>___

**答案:**## 3 2.

**解析:**解（法一）由于<equation>A</equation>的每行元素之和均为2，故<equation>\begin{aligned} | \boldsymbol {A} | &= \left| \begin{array}{l l l} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3}  \right| \xlongequal {c _ {1} + c _ {2} + c _ {3}} \left| \begin{array}{l l l} a _ {1 1} + a _ {1 2} + a _ {1 3} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} + a _ {2 2} + a _ {2 3} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} + a _ {3 2} + a _ {3 3} & a _ {3 2} & a _ {3 3}  \right| &= \left| \begin{array}{l l l} 2 & a _ {1 2} & a _ {1 3} \\ 2 & a _ {2 2} & a _ {2 3} \\ 2 & a _ {3 2} & a _ {3 3}  \right| \\ &= 2 \left| \begin{array}{c c c} 1 & a _ {1 2} & a _ {1 3} \\ 1 & a _ {2 2} & a _ {2 3} \\ 1 & a _ {3 2} & a _ {3 3}  \right| &= 2 \left(A _ {1 1} + A _ {2 1} + A _ {3 1}\right). \end{aligned}</equation>又因为<equation>|A| = 3</equation>，所以<equation>A_{11} + A_{21} + A_{31} = \frac{3}{2}</equation>（法二）由于 A的每行元素之和均为2，故<equation>A\binom{1}{1}=\binom{2}{2},\binom{1}{1}</equation>为 A的属于特征值2的特征向量.于是，<equation>\binom{1}{1}</equation>也是<equation>A^{*}</equation>的属于特征值<equation>\frac{|A|}{2}=\frac{3}{2}</equation>的特征向量，即<equation>\begin{aligned} \boldsymbol {A} ^ {*} \left(  1 \\ 1 \\ 1  \right) &= \left( \begin{array}{c c c} A _ {1 1} & A _ {2 1} & A _ {3 1} \\ A _ {1 2} & A _ {2 2} & A _ {3 2} \\ A _ {1 3} & A _ {2 3} & A _ {3 3}  \right) \left(  1 \\ 1 \\ 1  \right) &= \frac {3}{2} \left(  1 \\ 1 \\ 1  \right). \end{aligned}</equation>因此，<equation>A_{11}+A_{21}+A_{31}=\frac{3}{2}.</equation>

---

**2020年第13题 | 填空题 | 4分**

13. 行列式<equation>\left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a \end{array} \right| = \underline {{\quad}}</equation>

**答案:**<equation>a^{4}-4 a^{2}.</equation>

**解析:**解（法一）利用行列式的性质对所求行列式进行转化.

若<equation>a = 0</equation>，则将第二行加到第一行可得零行，从而行列式为0.

若 a≠0，则<equation>\begin{aligned} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a  \right| \xlongequal {r _ {4} + r _ {3}} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 0 & 0 & a & a  \right| \xlongequal {r _ {3} + \frac {1}{a} r _ {1}} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ 0 & 1 & a - \frac {1}{a} & \frac {1}{a} \\ 0 & 0 & a & a  \right| \\ \xlongequal {r _ {3} - \frac {1}{a} r _ {2}} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ 0 & 0 & a - \frac {2}{a} & \frac {2}{a} \\ 0 & 0 & a & a  \right| &= \left| \begin{array}{c c} a & 0 \\ 0 & a  \right| \cdot \left| \begin{array}{c c} a - \frac {2}{a} & \frac {2}{a} \\ a & a  \right| \\ &= a ^ {2} \left[ \left(a - \frac {2}{a}\right) a - 2 \right] = a ^ {2} \left(a ^ {2} - 4\right) = a ^ {4} - 4 a ^ {2}. \end{aligned}</equation>不论是哪种情况，所求行列式均为<equation>a^4 - 4a^2</equation>.

（法二）注意到所求行列式的各行元素之和均为 a，故可将各列均加到第1列，然后计算行列式.<equation>\begin{array}{l} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a \end{array} \right| \frac {c _ {1} + c _ {2} + c _ {3} + c _ {4}}{\hline} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ a & a & 1 & - 1 \\ a & 1 & a & 0 \\ a & - 1 & 0 & a \end{array} \right| = a \left| \begin{array}{c c c c} 1 & 0 & - 1 & 1 \\ 1 & a & 1 & - 1 \\ 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a \end{array} \right| \\ \frac {c _ {3} + c _ {1}}{c _ {4} - c _ {1}} a \left| \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 1 & a & 2 & - 2 \\ 1 & 1 & a + 1 & - 1 \\ 1 & - 1 & 1 & a - 1 \end{array} \right| \frac {c _ {3} + c _ {4}}{\hline} a \left| \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 1 & a & 0 & - 2 \\ 1 & 1 & a & - 1 \\ 1 & - 1 & a & a - 1 \end{array} \right| \\ \frac {\text {按第一行展开}}{\mathrm {=} a ^ {4} - 4 a ^ {2}} a \left\{a \left[ a (a - 1) + a \right] - 2 (a + a) \right\} = a \left(a ^ {3} - 4 a\right) \\ \end{array}</equation>

---

**2016年第13题 | 填空题 | 4分**

13. 行列式<equation>\left| \begin{array}{c c c c} \lambda & - 1 & 0 & 0 \\ 0 & \lambda & - 1 & 0 \\ 0 & 0 & \lambda & - 1 \\ 4 & 3 & 2 & \lambda + 1 \end{array} \right| = \underline {{\quad}}</equation>

**答案:**<equation>\lambda^{4}+\lambda^{3}+2\lambda^{2}+3\lambda+4.</equation>

**解析:**解 （法一）按第一列展开.<equation>\begin{aligned} \left| \begin{array}{c c c c} \lambda & - 1 & 0 & 0 \\ 0 & \lambda & - 1 & 0 \\ 0 & 0 & \lambda & - 1 \\ 4 & 3 & 2 & \lambda + 1  \right| &= \lambda \left| \begin{array}{c c c} \lambda & - 1 & 0 \\ 0 & \lambda & - 1 \\ 3 & 2 & \lambda + 1  \right| - 4 \left| \begin{array}{c c c} - 1 & 0 & 0 \\ \lambda & - 1 & 0 \\ 0 & \lambda & - 1  \right| \\ &= \lambda \left(\lambda \left| \begin{array}{c c} \lambda & - 1 \\ 2 & \lambda + 1  \right| + 3 \left| \begin{array}{c c} - 1 & 0 \\ \lambda & - 1  \right|\right) - 4 \times (- 1) ^ {3} \\ &= \lambda \left[ \lambda \left(\lambda^ {2} + \lambda + 2\right) + 3 \right] + 4 \\ &= \lambda^ {4} + \lambda^ {3} + 2 \lambda^ {2} + 3 \lambda + 4. \end{aligned}</equation>（法二）利用行列式的性质.<equation>\begin{aligned} \left| \begin{array}{c c c c} \lambda & - 1 & 0 & 0 \\ 0 & \lambda & - 1 & 0 \\ 0 & 0 & \lambda & - 1 \\ 4 & 3 & 2 & \lambda + 1  \right| \xlongequal {c _ {1} + \lambda c _ {2}} \left| \begin{array}{c c c c} 0 & - 1 & 0 & 0 \\ \lambda^ {2} & \lambda & - 1 & 0 \\ 0 & 0 & \lambda & - 1 \\ 4 + 3 \lambda & 3 & 2 & \lambda + 1  \right| \\ \xlongequal {c _ {1} + \lambda^ {2} c _ {3}} \left| \begin{array}{c c c c} 0 & - 1 & 0 & 0 \\ 0 & \lambda & - 1 & 0 \\ \lambda^ {3} & 0 & \lambda & - 1 \\ 4 + 3 \lambda + 2 \lambda^ {2} & 3 & 2 & \lambda + 1  \right| \\ \xlongequal {c _ {1} + \lambda^ {3} c _ {4}} \left| \begin{array}{c c c c} 0 & - 1 & 0 & 0 \\ 0 & \lambda & - 1 & 0 \\ 0 & 0 & \lambda & - 1 \\ 4 + 3 \lambda + 2 \lambda^ {2} + \lambda^ {3} (\lambda + 1) & 3 & 2 & \lambda + 1  \right| \\ &= (- 1) ^ {4 + 1} \left[ 4 + 3 \lambda + 2 \lambda^ {2} + \lambda^ {3} (\lambda + 1) \right] (- 1) ^ {3} \\ &= \lambda^ {4} + \lambda^ {3} + 2 \lambda^ {2} + 3 \lambda + 4. \end{aligned}</equation>

---

**2015年第13题 | 填空题 | 4分**

13. n阶行列式<equation>\left| \begin{array}{c c c c c} 2 & 0 & \dots & 0 & 2 \\ - 1 & 2 & \dots & 0 & 2 \\ \vdots & \vdots & & \vdots & \vdots \\ 0 & 0 & \dots & 2 & 2 \\ 0 & 0 & \dots & - 1 & 2 \end{array} \right| = \underline {{\quad}}</equation>

**解析:**解（法一）记<equation>D_{n}=\left| \begin{array}{cccccc}2&0&\dots&0&2\\ -1&2&\dots&0&2\\ \vdots &\vdots & &\vdots &\vdots \\ 0&0&\dots&2&2\\ 0&0&\dots&-1&2 \end{array} \right|_{n\times n}</equation>，将<equation>D_{n}</equation>按第一行展开得到<equation>\begin{aligned} D _ {n} &= 2 D _ {n - 1} + (- 1) ^ {n + 1} \cdot 2 \left| \begin{array}{c c c c c} - 1 & 2 & & & \\ & - 1 & 2 & & \\ & & \ddots & \ddots & \\ & & & \ddots & 2 \\ & & & & - 1  \right| _ {(n - 1) \times (n - 1)} \\ &= 2 D _ {n - 1} + 2 (- 1) ^ {n + 1} \cdot (- 1) ^ {n - 1} = 2 D _ {n - 1} + 2. \end{aligned}</equation>于是<equation>\begin{aligned} D _ {n} &= 2 D _ {n - 1} + 2 = 2 \left(2 D _ {n - 2} + 2\right) + 2 = 2 ^ {2} D _ {n - 2} + 2 ^ {2} + 2 \\ &= \dots \\ &= 2 ^ {n - 1} D _ {1} + 2 ^ {n - 1} + 2 ^ {n - 2} + \dots + 2 \\ &= 2 ^ {n} + 2 ^ {n - 1} + \dots + 2 = 2 ^ {n + 1} - 2. \end{aligned}</equation>（法二）对行列式作如下行变换.<equation>\begin{aligned} \left| \begin{array}{c c c c c} 2 & 0 & \dots & 0 & 2 \\ - 1 & 2 & \dots & 0 & 2 \\ \vdots & \vdots & & \vdots & \vdots \\ 0 & 0 & \dots & 2 & 2 \\ 0 & 0 & \dots & - 1 & 2  \right| \underline {{r _ {2} + \frac {1}{2} r _ {1}}} \left| \begin{array}{c c c c c c} 2 & 0 & 0 & \dots & 0 & 2 \\ 0 & 2 & 0 & \dots & 0 & 2 + 1 \\ 0 & - 1 & 2 & \dots & 0 & 2 \\ \vdots & \vdots & \vdots & & \vdots & \vdots \\ 0 & 0 & 0 & \dots & 2 & 2 \\ 0 & 0 & 0 & \dots & - 1 & 2  \right| \\ \underline {{r _ {3} + \frac {1}{2} r _ {2}}} \left| \begin{array}{c c c c c c} 2 & 0 & 0 & \dots & 0 & 2 \\ 0 & 2 & 0 & \dots & 0 & 2 + 1 \\ 0 & 0 & 2 & \dots & 0 & \frac {2 ^ {2} + 2 + 1}{2} \\ \vdots & \vdots & \vdots & & \vdots & \vdots \\ 0 & 0 & 0 & \dots & 2 & 2 \\ 0 & 0 & 0 & \dots & - 1 & 2  \right| \\ \underline {{r _ {4} + \frac {1}{2} r _ {3}}} \dots \\ \underline {{r _ {n} + \frac {1}{2} r _ {n - 1}}} \left| \begin{array}{c c c c c c} 2 & & & & 2 \\ & 2 & & & 2 + 1 \\ & & \ddots & & \vdots \\ & & & 2 & \frac {2 ^ {n - 2} + 2 ^ {n - 3} + \dots + 2 + 1}{2 ^ {n - 3}} \\ & & & & \frac {2 ^ {n - 1} + \dots + 2 + 1}{2 ^ {n - 2}}  \right| \\ &= 2 ^ {n - 1} \cdot \frac {2 ^ {n - 1} + \dots + 2 + 1}{2 ^ {n - 2}} \\ &= 2 \cdot \frac {1 - 2 ^ {n}}{1 - 2} = 2 ^ {n + 1} - 2. \end{aligned}</equation>

---

**2014年第5题 | 选择题 | 4分 | 答案: B**

5. 行列式<equation>\left| \begin{array}{c c c c} 0 & a & b & 0 \\ a & 0 & 0 & b \\ 0 & c & d & 0 \\ c & 0 & 0 & d \end{array} \right|</equation>A.<equation>( a d-b c )^{2}</equation>B.<equation>-( a d-b c )^{2}</equation>C.<equation>a^{2} d^{2}-b^{2} c^{2}</equation>D.<equation>b^{2} c^{2}-a^{2} d^{2}</equation>

答案: B

**解析:**解（法一）将原行列式作初等变换使之与分块对角矩阵的行列式建立联系.根据行列式的性质，交换两行或两列，所得新行列式为原行列式的负值.<equation>\left| \begin{array}{c c c c} 0 & a & b & 0 \\ a & 0 & 0 & b \\ 0 & c & d & 0 \\ c & 0 & 0 & d \end{array} \right| = - \left| \begin{array}{c c c c} 0 & a & b & 0 \\ 0 & c & d & 0 \\ a & 0 & 0 & b \\ c & 0 & 0 & d \end{array} \right| = \left| \begin{array}{c c c c} a & 0 & b & 0 \\ c & 0 & d & 0 \\ 0 & a & 0 & b \\ 0 & c & 0 & d \end{array} \right| = - \left| \begin{array}{c c c c} a & b & 0 & 0 \\ c & d & 0 & 0 \\ 0 & 0 & a & b \\ 0 & 0 & c & d \end{array} \right| = - (a d - b c) ^ {2}.</equation>应选B.

（法二）按第一行展开.<equation>\left| \begin{array}{c c c c} 0 & a & b & 0 \\ a & 0 & 0 & b \\ 0 & c & d & 0 \\ c & 0 & 0 & d \end{array} \right| = (- a) \left| \begin{array}{c c c} a & 0 & b \\ 0 & d & 0 \\ c & 0 & d \end{array} \right| + b \left| \begin{array}{c c c} a & 0 & b \\ 0 & c & 0 \\ c & 0 & d \end{array} \right| = - a ^ {2} d ^ {2} + a b c d + a b c d - b ^ {2} c ^ {2} = - (a d - b c) ^ {2}.</equation>应选B.

---


## 概率论与数理统计


### 随机变量的数字特征


#### 数学期望与方差

**2025年第8题 | 选择题 | 5分 | 答案: C**
8. 设二维随机变量 (X,Y) 服从正态分布 N(0,0;1,1;<equation>\rho</equation>), 其中<equation>\rho \in(-1,1)</equation>, 若 a,b为满足<equation>a^{2}+b^{2}=1</equation>的任意实数，则 D(aX+bY) 的最大值为（    )

A.1 B.2 C.<equation>1+|\rho|</equation>D.<equation>1+\rho^{2}</equation>
答案: C
**解析: **解 由于<equation>(X, Y)</equation>服从正态分布<equation>N(0, 0; 1, 1; \rho)</equation>，故<equation>D (X) = D (Y) = 1, \quad \operatorname {C o v} (X, Y) = \rho \sqrt {D (X)} \sqrt {D (Y)} = \rho .</equation>根据方差的性质，<equation>\begin{aligned} D (a X + b Y) &= D (a X) + D (b Y) + 2 \operatorname {C o v} (a X, b Y) = a ^ {2} D (X) + b ^ {2} D (Y) + 2 a b \operatorname {C o v} (X, Y) \\ &= a ^ {2} + b ^ {2} + 2 a b \rho \xlongequal {a ^ {2} + b ^ {2} = 1} 1 + 2 a b \rho . \end{aligned}</equation>又因为<equation>a^2 + b^2 = 1 \geqslant 2 |ab|</equation>，所以<equation>1 + 2ab\rho \leqslant 1 + 2|ab\rho| \leqslant 1 + |\rho|</equation>，从而<equation>D(aX + bY) \leqslant</equation>1+<equation>| \rho |</equation>. 若<equation>\rho > 0</equation>，则 D（aX+bY）的最大值为1+<equation>\rho</equation>，最大值在<equation>\left\{ \begin{array}{l l} a=\pm \frac{\sqrt{2}}{2}, \\ b=\pm \frac{\sqrt{2}}{2} \end{array} \right.</equation>时取得；若<equation>\rho < 0</equation>，则 D（aX+

bY）的最大值为<equation>1 - \rho</equation>，最大值在时取得；若<equation>\rho = 0</equation>，则<equation>D(aX + bY)\equiv 1.</equation>因此，<equation>D ( a X+b Y )</equation>的最大值为<equation>1+|\rho|</equation>，应选C.

---

**2023年第8题 | 选择题 | 5分 | 答案: C**
8. 设随机变量 X服从参数为1的泊松分布，则<equation>E[|X - E(X)|] =</equation>（    ）

A.<equation>\frac{1} {\mathrm{e}}</equation>B.<equation>\frac{1}{2}</equation>C.<equation>\frac{2} {\mathrm{e}}</equation>D. 1
答案: C
**解析: **归于 X服从参数为1的泊松分布，故<equation>E ( X )=1.</equation>从而<equation>| X - E (X) | = | X - 1 | = \left\{ \begin{array}{l l} 1, & X = 0, \\ X - 1, & X = 1, 2, \dots . \end{array} \right.</equation>由参数为1的泊松分布的分布律可知，<equation>P\{X = 0\} = \frac{1^{0}\cdot\mathrm{e}^{-1}}{0!} = \frac{1}{\mathrm{e}}.</equation>根据数学期望的定义，<equation>\begin{aligned} E [ \mid X - E (X) \mid ] &= 1 \cdot P \{X = 0 \} + \sum_ {k = 1} ^ {\infty} (k - 1) P \{X = k \} \\ &= \frac {1}{\mathrm {e}} + \sum_ {k = 0} ^ {\infty} (k - 1) P \{X = k \} - (0 - 1) P \{X = 0 \} \\ &= \frac {1}{\mathrm {e}} + E (X - 1) + \frac {1}{\mathrm {e}} = \frac {1}{\mathrm {e}} + E (X) - 1 + \frac {1}{\mathrm {e}} \\ \underline {{\underline {{E (X) = 1}}}} \frac {2}{\mathrm {e}}. \end{aligned}</equation>因此，应选C.

---

**2021年第22题 | 解答题 | 12分**
2. (本题满分12分)

在区间（0,2）上随机取一点，将该区间分成两段，较短一段的长度为 X，较长一段的长度为 Y，令<equation>Z=\frac{Y}{X}</equation>.

I. 求 X的概率密度；

II. 求 Z的概率密度；

III. 求<equation>E\left(\frac{X}{Y}\right).</equation>
**答案: **（I）<equation>X</equation>的概率密度为<equation>f_{X}(x)=\left\{\begin{array}{ll}1,&0<x<1,\\ 0,&\text{其他};\end{array} \right.</equation>（Ⅱ）<equation>Z</equation>的概率密度为<equation>f_{Z}(z)=\left\{\begin{array}{ll}0,&z<1,\\ \frac{2}{(z+1)^{2}},&z\geqslant 1; \end{array} \right.</equation>（Ⅲ）<equation>2\ln 2-1.</equation>
**解析: **解（I）根据分析，在区间（0，2）上随机取一点，将该点位置记为 W，则 W服从（0，2）上的均匀分布.<equation>X=\min \{ W,2-W\}</equation>由于<equation>X</equation>为较短一段的长度，故<equation>X</equation>的取值范围为（0,1].

记<equation>X</equation>的分布函数为<equation>F_{X}(x)</equation>当<equation>x < 0</equation>时，<equation>F_{X}(x) = P\{X\leqslant x\} = 0.</equation>当<equation>0\leqslant x < 1</equation>时，<equation>\begin{array}{l} F _ {X} (x) = P \{X \leqslant x \} = 1 - P \{X > x \} = 1 - P \{W > x, 2 - W > x \} \\ = 1 - P \left\{x < W < 2 - x \right\} = 1 - P \left\{W < 2 - x \right\} + P \left\{W \leqslant x \right\} \\ = 1 - \frac {2 - x}{2} + \frac {x}{2} = x. \\ \end{array}</equation>当<equation>x\geqslant 1</equation>时，<equation>F_{X}(x) = P\{X\leqslant x\} = 1.</equation>因此，<equation>F_{X}(x) = \left\{ \begin{array}{ll}0, & x < 0,\\ x, & 0\leqslant x < 1, f_{X}(x) = \left\{ \begin{array}{ll}1, & 0 < x < 1,\\ 0, & \text{其他}. \end{array} \right. X</equation>服从区间（0,1）上的均匀分布.<equation>1, x \geqslant 1,</equation>（Ⅱ）<equation>Z=\frac{Y}{X}=\frac{2-X}{X}=\frac{2}{X}-1.</equation>记Z的分布函数为<equation>F_{Z}(z).</equation>由于<equation>X</equation>的取值范围为<equation>(0,1]</equation>，故<equation>Z</equation>的取值范围为<equation>[1, + \infty)</equation>.

当<equation>z < 1</equation>时，<equation>F_{Z}(z) = P\{Z\leqslant z\} = 0.</equation>当<equation>z\geqslant 1</equation>时，<equation>\begin{array}{l} F _ {Z} (z) = P \left\{\frac {2}{X} - 1 \leqslant z \right\} = P \left\{\frac {2}{X} \leqslant z + 1 \right\} = P \left\{X \geqslant \frac {2}{z + 1} \right\} \\ = 1 - P \left\{X < \frac {2}{z + 1} \right\}. \\ \end{array}</equation>由于<equation>P\left\{X < \frac{2}{z + 1}\right\} = \frac{2}{z + 1}</equation>，故<equation>F_{Z}(z) = 1 - \frac{2}{z + 1}</equation>因此，<equation>F_{Z}(z) = \left\{ \begin{array}{ll} 0, & z < 1, \\ 1 - \frac{2}{z + 1}, & z \geqslant 1. \end{array} \right. f_{Z}(z) = \left\{ \begin{array}{ll} 0, & z < 1, \\ \frac{2}{(z + 1)^{2}}, & z \geqslant 1. \end{array} \right.</equation>（Ⅲ）（法一）注意到<equation>\frac{X}{Y}=\frac{X}{2-X}.</equation><equation>\begin{aligned} E \left(\frac {X}{Y}\right) &= E \left(\frac {X}{2 - X}\right) = \int_ {- \infty} ^ {+ \infty} \frac {x}{2 - x} \cdot f _ {X} (x) \mathrm {d} x = \int_ {0} ^ {1} \frac {x}{2 - x} \mathrm {d} x = \int_ {0} ^ {1} \left(- 1 + \frac {2}{2 - x}\right) \mathrm {d} x \\ &= \left[ - x - 2 \ln (2 - x) \right] \Bigg | _ {0} ^ {1} = 2 \ln 2 - 1. \end{aligned}</equation>（法二）由于<equation>Z = \frac{Y}{X}</equation>，故<equation>\frac{X}{Y} = \frac{1}{Z}</equation>.于是，<equation>E \left(\frac {X}{Y}\right) = E \left(\frac {1}{Z}\right) = \int_ {- \infty} ^ {+ \infty} \frac {1}{z} \cdot f _ {Z} (z) \mathrm {d} z = 2 \int_ {1} ^ {+ \infty} \frac {1}{z} \cdot \frac {1}{(z + 1) ^ {2}} \mathrm {d} z.</equation>设<equation>\frac{1}{z(z + 1)^2} = \frac{A}{z} +\frac{B}{z + 1} +\frac{C}{(z + 1)^2}</equation>，则<equation>\frac {1}{z (z + 1) ^ {2}} = \frac {A (z + 1) ^ {2} + B z (z + 1) + C z}{z (z + 1) ^ {2}} = \frac {(A + B) z ^ {2} + (2 A + B + C) z + A}{z (z + 1) ^ {2}}.</equation>比较系数可得<equation>\left\{ \begin{array}{l l} A+B=0, \\ 2 A+B+C=0, \\ A=1. \end{array} \right.</equation>解得<equation>\left\{ \begin{array}{l l} A=1, \\ B=-1, \\ C=-1. \end{array} \right.</equation>从而<equation>\frac{1}{z(z+1)^2}=\frac{1}{z}-\frac{1}{z+1}-\frac{1}{(z+1)^2}.</equation><equation>\begin{aligned} E \left(\frac {X}{Y}\right) &= 2 \int_ {1} ^ {+ \infty} \left[ \frac {1}{z} - \frac {1}{z + 1} - \frac {1}{(z + 1) ^ {2}} \right] \mathrm {d} z = 2 \left(\ln \frac {z}{z + 1} + \frac {1}{z + 1}\right) \Bigg | _ {1} ^ {+ \infty} \\ &= 2 \left(0 - \ln \frac {1}{2} - \frac {1}{2}\right) = 2 \ln 2 - 1. \end{aligned}</equation>

---

**2019年第14题 | 填空题 | 4分**
14. 设随机变量 X的概率密度为 f(x)<equation>\left\{\begin{array}{ll}\frac{x}{2},&0<x<2,\\0,&\text{其他},\end{array}\right.</equation>F(x)为 X的分布函数，E(X)为 X的数学期望，则<equation>P\{F(X)>E(X)-1\}=</equation>___
**解析: **解（法一）分别计算<equation>E ( X )</equation>，<equation>F ( x )</equation><equation>E (X) = \int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \int_ {0} ^ {2} \frac {x ^ {2}}{2} \mathrm {d} x = \left. \frac {x ^ {3}}{6} \right| _ {0} ^ {2} = \frac {4}{3}.</equation>当<equation>x < 0</equation>时，<equation>F ( x )=0.</equation>当<equation>0 \leqslant x < 2</equation>时，<equation>F(x) = \int_{-\infty}^{x} f(t)\mathrm{d}t = \int_{0}^{x}\frac{t}{2}\mathrm{d}t = \frac{x^2}{4}</equation>.

当<equation>x\geqslant 2</equation>时，<equation>F(x) = 1.</equation>于是，<equation>F ( x ) = \left\{ \begin{array}{ll} 0, & x < 0, \\ \frac{x^{2}}{4}, & 0 \leqslant x < 2, \\ 1, & x \geqslant 2. \end{array} \right.</equation>因此，<equation>\begin{array}{l} P \left\{F (X) > E (X) - 1 \right\} = P \left\{F (X) > \frac {1}{3} \right\} = P \left\{\frac {X ^ {2}}{4} > \frac {1}{3}, 0 \leqslant X < 2 \right\} + P \left\{X \geqslant 2 \right\} \\ = P \left\{\frac {2}{\sqrt {3}} < X < 2 \right\} + \int_ {2} ^ {+ \infty} f (x) \mathrm {d} x = 1 - \int_ {0} ^ {\frac {2}{\sqrt {3}}} \frac {x}{2} \mathrm {d} x + 0 \\ = 1 - \frac {x ^ {2}}{4} \Bigg | _ {0} ^ {\frac {2}{\sqrt {3}}} = \frac {2}{3}. \\ \end{array}</equation>（法二）我们先证明<equation>Y = F(X)</equation>服从（0，1）上的均匀分布.

注意到<equation>F ( x )</equation>在（0，2）上严格单调增加，其值域为（0，1），故可定义<equation>F^{-1}(y)</equation>，<equation>y\in(0,1).</equation>考虑Y的分布函数<equation>F_{Y}(y).</equation>当<equation>y < 0</equation>时，由于<equation>F(X)</equation>仅在<equation>[0,1]</equation>上取值，故<equation>F_{Y}(y) = 0.</equation>当<equation>0\leqslant y < 1</equation>时，<equation>F _ {Y} (y) = P \left\{Y \leqslant y \right\} = P \left\{F (X) \leqslant y \right\} = P \left\{X \leqslant F ^ {- 1} (y) \right\} = F \left(F ^ {- 1} (y)\right) = y.</equation>当<equation>y \geqslant 1</equation>时，<equation>P\{Y \leqslant y\} = 1</equation>，即<equation>F_{Y}(y) = 1.</equation>因此，<equation>F_{Y}(y) = \left\{ \begin{array}{ll}0, & y < 0,\\ y, & 0\leqslant y < 1,\\ 1, & y\geqslant 1. \end{array} \right.</equation>这说明<equation>Y = F(X)</equation>服从（0，1）上的均匀分布.

由法一可知<equation>E ( X )=\frac{4}{3}</equation>故<equation>P \left\{F (X) > E (X) - 1 \right\} = P \left\{F (X) > \frac {1}{3} \right\} = 1 - P \left\{F (X) \leqslant \frac {1}{3} \right\} = 1 - \frac {1}{3} = \frac {2}{3}.</equation>

---


#### 协方差与相关系数

**2024年第9题 | 选择题 | 5分 | 答案: D**
9. 设随机变量 X的概率密度为<equation>f ( x )=\left\{\begin{array}{ll}2(1-x),&0<x<1,\\ 0,&\text{其他}.\end{array}\right.</equation>在 X=x(0<x<1)的条件下，随机变量 Y服从区间 (x,1)上的均匀分布，则<equation>\operatorname{C o v} ( X, Y )=</equation>(    )

A.<equation>-\frac{1}{36}</equation>B.<equation>-\frac{1}{72}</equation>C.<equation>\frac{1}{72}</equation>D.<equation>\frac{1}{36}</equation>
答案: D
**解析: **解 由于在<equation>X=x(0<x<1)</equation>的条件下，随机变量Y服从区间（x，1）上的均匀分布，故<equation>f_{Y \mid X}(y \mid x)=\frac{1}{1-x}.</equation>记区域<equation>D=\{(x,y)\mid x<y<1,0<x<1\}</equation>，则在区域D上，<equation>(X,Y)</equation>的联合概率密度<equation>\varphi (x, y) = f _ {Y \mid X} (y \mid x) f (x) = \frac {1}{1 - x} \cdot 2 (1 - x) = 2.</equation>注意到区域 D是一个直角边长为1的等腰直角三角形区域，面积为<equation>\frac{1}{2}</equation>，故<equation>\iint_ {D} \varphi (x, y) \mathrm {d} x \mathrm {d} y = 2 \iint_ {D} \mathrm {d} x \mathrm {d} y = 1,</equation>从而可认为在<equation>D</equation>以外的区域上，<equation>\varphi (x,y) = 0.</equation>进一步可得，当<equation>0 < y < 1</equation>时，<equation>Y</equation>的边缘概率密度<equation>f _ {Y} (y) = \int_ {- \infty} ^ {+ \infty} \varphi (x, y) \mathrm {d} x = \int_ {0} ^ {y} 2 \mathrm {d} x = 2 y.</equation>当<equation>y \leqslant 0</equation>或<equation>y \geqslant 1</equation>时，<equation>f_{Y}(y) = \int_{-\infty}^{+\infty}\varphi(x,y)\mathrm{d}x = 0.</equation>由数学期望的定义可得，<equation>E (X) = \int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \int_ {0} ^ {1} x \cdot 2 (1 - x) \mathrm {d} x = \int_ {0} ^ {1} \left(2 x - 2 x ^ {2}\right) \mathrm {d} x = \left(x ^ {2} - \frac {2 x ^ {3}}{3}\right) \Bigg | _ {0} ^ {1} = \frac {1}{3},</equation><equation>E (Y) = \int_ {- \infty} ^ {+ \infty} y f _ {Y} (y) \mathrm {d} y = \int_ {0} ^ {1} y \cdot 2 y \mathrm {d} y = \left. \frac {2 y ^ {3}}{3} \right| _ {0} ^ {1} = \frac {2}{3},</equation><equation>\begin{aligned} E (X Y) &= \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} x y \varphi (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {D} 2 x y \mathrm {d} x \mathrm {d} y = 2 \int_ {0} ^ {1} y \mathrm {d} y \int_ {0} ^ {y} x \mathrm {d} x = 2 \int_ {0} ^ {1} y \cdot \frac {y ^ {2}}{2} \mathrm {d} y \\ &= \left. \frac {y ^ {4}}{4} \right| _ {0} ^ {1} = \frac {1}{4}. \end{aligned}</equation>因此，<equation>\operatorname {C o v} (X, Y) = E (X Y) - E (X) E (Y) = \frac {1}{4} - \frac {1}{3} \times \frac {2}{3} = \frac {1}{3 6}.</equation>应选 D.

---

**2023年第22题 | 解答题 | 12分**
. (本题满分12分)

设二维随机变量（X，Y）的概率密度为<equation>f ( x, y )=\left\{\begin{array}{ll}\frac{2}{\pi} \left(x^{2}+y^{2}\right),&x^{2}+y^{2}\leqslant 1\\ 0,&\text{其它}\end{array} \right.</equation>I. 求 X与 Y的斜方差；

II. 求 X与 Y是否相互独立；

III. 求<equation>Z=X^{2}+Y^{2}</equation>的概率密度.
**答案: **(I) Cov(X,Y) = 0;

（Ⅱ）X与Y不相互独立；

（Ⅲ）Z的概率密度<equation>f_{Z}(z)=\left\{ \begin{array}{ll} 2z, & 0<z<1, \\ 0, & \text{其他}. \end{array} \right.</equation>
**解析: **解（I）由<equation>f ( x,y )</equation>的定义可知，当<equation>| x | > 1</equation>时，<equation>f ( x,y ) = 0</equation>，当<equation>| x | \leqslant 1</equation>时，<equation>f ( x,y )</equation>仅在<equation>- \sqrt{1-x^{2}}\leqslant y\leqslant \sqrt{1-x^{2}}</equation>时非零.<equation>\begin{aligned} f _ {X} (x) &= \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} y = \frac {2}{\pi} \int_ {- \sqrt {1 - x ^ {2}}} ^ {\sqrt {1 - x ^ {2}}} \left(x ^ {2} + y ^ {2}\right) \mathrm {d} y = \frac {4}{\pi} \int_ {0} ^ {\sqrt {1 - x ^ {2}}} \left(x ^ {2} + y ^ {2}\right) \mathrm {d} y \\ &= \frac {4}{\pi} \left[ x ^ {2} \sqrt {1 - x ^ {2}} + \frac {\left(1 - x ^ {2}\right) ^ {\frac {3}{2}}}{3} \right] = \frac {4}{3 \pi} \sqrt {1 - x ^ {2}} \left(1 + 2 x ^ {2}\right), \end{aligned}</equation>即<equation>f_{X}(x) = \left\{ \begin{array}{ll}\frac{4}{3\pi}\sqrt{1 - x^{2}}(1 + 2x^{2}), & |x|\leqslant 1,\\ 0, & |x| > 1. \end{array} \right.</equation>同理可得<equation>f _ {Y} (y) = \left\{ \begin{array}{l l} \frac {4}{3 \pi} \sqrt {1 - y ^ {2}} \left(1 + 2 y ^ {2}\right), & | y | \leqslant 1, \\ 0, & | y | > 1. \end{array} \right.</equation>(a)

(b)

记<equation>D = \{(x,y)\mid x^{2} + y^{2}\leqslant 1\} .</equation>如图（a）所示，区域D关于x轴，y轴均对称.进一步计算可得<equation>E (X) = \int_ {- \infty} ^ {+ \infty} x f _ {X} (x) \mathrm {d} x = \int_ {- 1} ^ {1} \frac {4 x}{3 \pi} \sqrt {1 - x ^ {2}} \left(1 + 2 x ^ {2}\right) \mathrm {d} x \stackrel {\text {对称性}} {=} 0,</equation><equation>E (Y) \stackrel {\text {同 理}} {=} 0,</equation><equation>E (X Y) = \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} x y f (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {D} x y \cdot \frac {2}{\pi} \left(x ^ {2} + y ^ {2}\right) \mathrm {d} x \mathrm {d} y \stackrel {\text {对称 性}} {=} 0,</equation>从而<equation>\operatorname{Cov}(X, Y) = E(XY) - E(X)E(Y) = 0.</equation>（Ⅱ）由第（I）问可知，<equation>f_{X}(x)f_{Y}(y)\neq f(x,y)</equation>，故X与Y不相互独立.

（Ⅲ）记<equation>Z = X^{2} + Y^{2}</equation>的分布函数为<equation>F_{Z}(z), D_{z} = \{(x,y)|x^{2} + y^{2}\leqslant z\} .</equation>当<equation>z < 0</equation>时，<equation>F_{Z}(z) = P\{Z\leqslant z\} = 0.</equation>当<equation>0 \leqslant z < 1</equation>时，<equation>D \cap D_{z} = D_{z}</equation>，如图（b）所示.<equation>\begin{array}{l} F _ {Z} (z) = P \left\{Z \leqslant z \right\} = \iint_ {D _ {z}} \frac {2}{\pi} \left(x ^ {2} + y ^ {2}\right) \mathrm {d} x \mathrm {d} y = \frac {2}{\pi} \int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {0} ^ {\sqrt {z}} r ^ {2} \cdot r \mathrm {d} r \\ = \frac {2}{\pi} \cdot 2 \pi \cdot \frac {r ^ {4}}{4} \Bigg | _ {0} ^ {\sqrt {z}} = z ^ {2}. \\ \end{array}</equation>当<equation>z \geqslant 1</equation>时，<equation>F_{Z}(z) = P\{Z \leqslant z\} = 1.</equation>因此，<equation>Z</equation>的分布函数<equation>F_{Z}(z) = \left\{ \begin{array}{ll}0, & z < 0,\\ z^{2}, & 0\leqslant z < 1,\\ 1, & z\geqslant 1, \end{array} \right.</equation>概率密度<equation>f_{Z}(z) = F_{Z}^{\prime}(z) = \left\{ \begin{array}{ll}2z, & 0 < z < 1,\\ 0, & \text{其他}. \end{array} \right.</equation>

---

**2022年第8题 | 选择题 | 5分 | 答案: C**
8. 设随机变量 X服从区间（0,3）上的均匀分布，随机变量 Y服从参数为2的泊松分布，且 X与 Y的协方差为 -1，则<equation>D(2X-Y+1)=</equation>(    )

A.1 B.5 C.9 D.12
答案: C
**解析: **解 由于 X服从区间（0,3）上的均匀分布，故 X的方差<equation>D ( X )=\frac{(3-0)^{2}}{1 2}=\frac{3}{4}.</equation>又由于 Y服从参数为2的泊松分布，故 Y的方差<equation>D ( Y )=2.</equation>由方差的性质，<equation>\begin{aligned} D (2 X - Y + 1) &= D (2 X - Y) = D (2 X) + D (Y) - 2 \operatorname {C o v} (2 X, Y) \\ &= 4 D (X) + D (Y) - 4 \operatorname {C o v} (X, Y) = 4 \times \frac {3}{4} + 2 - 4 \times (- 1) = 9. \end{aligned}</equation>因此，应选C.

---

**2022年第10题 | 选择题 | 5分 | 答案: D**
10. 设随机变量<equation>X\sim N(0,1)</equation>，若在<equation>X=x</equation>的条件下，随机变量<equation>Y\sim N(x,1)</equation>，则 X与Y的相关系数为（    ）

A.<equation>\frac{1}{4}</equation>B.<equation>\frac{1}{2}</equation>C.<equation>\frac{\sqrt{3}}{3}</equation>D.<equation>\frac{\sqrt{2}}{2}</equation>
答案: D
**解析: **解（法一）由于<equation>X\sim N(0,1)</equation>，故<equation>X</equation>的概率密度函数为<equation>f _ {X} (x) = \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {x ^ {2}}{2}}.</equation>由于在<equation>X = x</equation>的条件下，<equation>Y\sim N(x,1)</equation>，故在<equation>X = x</equation>的条件下，<equation>Y</equation>的条件概率密度为<equation>f _ {Y \mid X} (y \mid x) = \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {(y - x) ^ {2}}{2}}.</equation>于是，二维随机变量<equation>(X, Y)</equation>的联合概率密度为<equation>f (x, y) = f _ {X} (x) f _ {Y \mid X} (y \mid x) = \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \cdot \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {(y - x) ^ {2}}{2}} = \frac {1}{2 \pi} \mathrm {e} ^ {- x ^ {2} + x y - \frac {y ^ {2}}{2}}.</equation>计算<equation>Y</equation>的边缘概率密度<equation>f_{Y}(y)</equation>. 对<equation>y \in (-\infty, +\infty)</equation>，<equation>\begin{aligned} f _ {Y} (y) &= \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} x = \int_ {- \infty} ^ {+ \infty} \frac {1}{2 \pi} \mathrm {e} ^ {- x ^ {2} + x y - \frac {y ^ {2}}{2}} \mathrm {d} x = \frac {1}{2 \sqrt {\pi}} \mathrm {e} ^ {- \frac {y ^ {2}}{4}} \int_ {- \infty} ^ {+ \infty} \frac {1}{\sqrt {2 \pi} \cdot \frac {\sqrt {2}}{2}} \mathrm {e} ^ {- (x - \frac {y}{2}) ^ {2}} \mathrm {d} x \\ &= \frac {1}{2 \sqrt {\pi}} \mathrm {e} ^ {- \frac {y ^ {2}}{4}} = \frac {1}{\sqrt {2 \pi} \cdot \sqrt {2}} \mathrm {e} ^ {- \frac {y ^ {2}}{2 (\sqrt {2}) ^ {2}}}. \end{aligned}</equation>于是，<equation>(X,Y)</equation>关于<equation>Y</equation>的边缘分布是正态分布<equation>N(0,2)</equation>.

结合<equation>f(x,y)</equation>与二维正态分布的概率密度的形式，取<equation>\mu_{1} = 0,\mu_{2} = 0,\sigma_{1} = 1,\sigma_{2} = \sqrt{2}</equation><equation>\frac {1}{2 \pi} \mathrm {e} ^ {- x ^ {2} + x y - \frac {y ^ {2}}{2}} = \frac {1}{2 \pi \cdot 1 \cdot \sqrt {2} \cdot \frac {\sqrt {2}}{2}} \cdot \mathrm {e} ^ {- \frac {1}{2} \cdot \frac {1}{2}} \left[ \frac {(x - 0) ^ {2}}{1 ^ {2}} - 2 \cdot \frac {\sqrt {2}}{2} \frac {(x - 0) (y - 0)}{1 \cdot \sqrt {2}} + \frac {(y - 0) ^ {2}}{(\sqrt {2}) ^ {2}} \right].</equation>因此，取<equation>\rho = \frac{\sqrt{2}}{2}</equation>，则<equation>(X,Y)</equation>服从二维正态分布<equation>N\left(0,0;1,2;\frac{\sqrt{2}}{2}\right)</equation>.

由二维正态分布的概率密度的参数的含义可知，<equation>\rho_{X Y}=\frac{\sqrt{2}}{2}</equation>，应选D.

（法二）计算<equation>\rho_{X Y}.</equation>先计算 E(XY).

由法一可得<equation>f(x,y) = \frac{1}{2\pi}\mathrm{e}^{-x^2 + xy - \frac{y^2}{2}}.</equation>于是，<equation>\begin{aligned} E (X Y) &= \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} x y f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {- \infty} ^ {+ \infty} x \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \mathrm {d} x \int_ {- \infty} ^ {+ \infty} y \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {(y - x) ^ {2}}{2}} \mathrm {d} y \\ &= \int_ {- \infty} ^ {+ \infty} x \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \mathrm {d} x \left[ \int_ {- \infty} ^ {+ \infty} \frac {1}{\sqrt {2 \pi}} (y - x) \mathrm {e} ^ {- \frac {(y - x) ^ {2}}{2}} \mathrm {d} y + x \int_ {- \infty} ^ {+ \infty} \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {(y - x) ^ {2}}{2}} \mathrm {d} (y - x) \right] \\ &= \int_ {- \infty} ^ {+ \infty} x \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {x ^ {2}}{2}} (0 + x) \mathrm {d} x = \int_ {- \infty} ^ {+ \infty} x ^ {2} \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \mathrm {d} x. \end{aligned}</equation>又因为<equation>\int_{-\infty}^{+\infty}x^{2}\frac{1}{\sqrt{2\pi}}\mathrm{e}^{-\frac{x^{2}}{2}}\mathrm{d}x = E(X^{2})</equation>，而<equation>X\sim N(0,1)</equation>，所以<equation>E(X^{2}) = D(X) + [E(X)]^{2} = 1.</equation>从而，<equation>E(XY) = 1.</equation>又由法一可得<equation>Y\sim N(0,2)</equation>，故<equation>E(Y)=0,D(Y)=2.</equation>因此，<equation>\rho_ {X Y} = \frac {\operatorname {C o v} (X , Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {1 - 0}{\sqrt {2}} = \frac {\sqrt {2}}{2}.</equation>

---

**2021年第16题 | 填空题 | 5分**
16. 甲、乙两个盒子中各装有2个红球和2个白球，先从甲盒中任取一球，观察颜色后放入乙盒中，再从乙盒中任取一球，令 X, Y分别表示从甲盒和乙盒中取到的红球个数，则 X与 Y的相关系数为 ___.
**答案: **# 1 5.
**解析: **根据相关系数的计算公式，X与Y的相关系数为<equation>\rho = \frac {\operatorname {C o v} (X , Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}}.</equation>下面分别计算<equation>X, Y</equation>的分布律与数字特征.

取球模型为等可能模型.<equation>X</equation>的可能取值为0，1. 取到白球，则<equation>X = 0</equation>；取到红球，则<equation>X = 1</equation><equation>P \{X = 0 \} = \frac {1}{2}, \quad P \{X = 1 \} = \frac {1}{2}.</equation>于是，<equation>E ( X ) = \frac {1}{2}, E \left( X^{2}\right) = \frac {1}{2}, D ( X ) = \frac {1}{2} - \left(\frac {1}{2}\right)^{2} = \frac {1}{4}.</equation>Y的可能取值为0，1.若从甲盒中取出的是白球，则后来乙盒中共有2个红球和3个白球，取到红球的概率为<equation>\frac{2}{5}</equation>即在X=0发生的条件下Y=1发生的概率为<equation>\frac{2}{5}</equation>；若从甲盒中取出的是红球，则后来乙盒中共有3个红球和2个白球，取到红球的概率为<equation>\frac{3}{5}</equation>即在X=1发生的条件下Y=1发生的概率为<equation>\frac{3}{5}.</equation><equation>\begin{aligned} P \{Y = 1 \} &= P \{Y = 1 \mid X = 0 \} P \{X = 0 \} + P \{Y = 1 \mid X = 1 \} P \{X = 1 \} \\ &= \frac {2}{5} \times \frac {1}{2} + \frac {3}{5} \times \frac {1}{2} = \frac {1}{2}. \end{aligned}</equation><equation>P \{Y = 0 \} = 1 - P \{Y = 1 \} = 1 - \frac {1}{2} = \frac {1}{2}.</equation>于是，<equation>E ( Y ) = \frac {1}{2}, E ( Y^{2} ) = \frac {1}{2}, D ( Y ) = \frac {1}{2} - \left(\frac {1}{2}\right)^{2} = \frac {1}{4}.</equation>XY的可能取值为0,1.<equation>P \{X Y = 1 \} = P \{X = 1, Y = 1 \} = P \{Y = 1 \mid X = 1 \} P \{X = 1 \} = \frac {3}{5} \times \frac {1}{2} = \frac {3}{1 0}.</equation><equation>P \left\{X Y = 0 \right\} = 1 - \frac {3}{1 0} = \frac {7}{1 0}.</equation>于是，<equation>E ( X Y ) = P \{ X Y = 1 \} \times 1 + P \{ X Y = 0 \} \times 0 = \frac {3}{1 0}.</equation>因此，<equation>\rho = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {\frac {3}{1 0} - \frac {1}{2} \times \frac {1}{2}}{\frac {1}{2} \times \frac {1}{2}} = \frac {\frac {1}{2 0}}{\frac {1}{4}} = \frac {1}{5}.</equation>

---

**2020年第14题 | 填空题 | 4分**
14. 设 X 服从区间<equation>\left(-\frac{\pi}{2},\frac{\pi}{2}\right)</equation>上的均匀分布，<equation>Y=\sin X</equation>，则<equation>\operatorname{Cov}(X,Y)=</equation>___
**答案: **# 2 π.
**解析: **解 由 X服从<equation>\left(-\frac{\pi}{2},\frac{\pi}{2}\right)</equation>上的均匀分布可知，<equation>f(x)=\left\{\begin{array}{ll}\frac{1}{\pi},&x\in\left(-\frac{\pi}{2},\frac{\pi}{2}\right),\\ 0,&\text{其他}.\end{array}\right.</equation><equation>E (X) = \int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \frac {1}{\pi} \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} x \mathrm {d} x = 0.</equation>根据协方差的计算公式，<equation>\begin{aligned} \operatorname {C o v} (X, Y) &= \operatorname {C o v} (X, \sin X) = E (X \sin X) - E (X) E (\sin X) \xlongequal {E (X) = 0} \int_ {- \infty} ^ {+ \infty} x \sin x f (x) \mathrm {d} x - 0 \\ &= \frac {1}{\pi} \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} x \sin x \mathrm {d} x \xlongequal {\text {对称性}} \frac {2}{\pi} \int_ {0} ^ {\frac {\pi}{2}} x \sin x \mathrm {d} x = - \frac {2}{\pi} \int_ {0} ^ {\frac {\pi}{2}} x \mathrm {d} (\cos x) \\ &= - \frac {2}{\pi} \left(x \cos x \Big | _ {0} ^ {\frac {\pi}{2}} - \int_ {0} ^ {\frac {\pi}{2}} \cos x \mathrm {d} x\right) = - \frac {2}{\pi} \times (0 - 1) = \frac {2}{\pi}. \end{aligned}</equation>

---

**2018年第22题 | 解答题 | 11分**
22. (本题满分11分)

设随机变量 X与 Y相互独立，X的概率分布为<equation>P\{X=1\}=P\{X=-1\}=\frac{1}{2},</equation>Y服从参数为<equation>\lambda</equation>的泊松分布.令<equation>Z=XY.</equation>I. 求<equation>\operatorname{Cov}(X,Z)</equation>;

II. 求 Z的概率分布.
**答案: **（ I ）<equation>\operatorname{C o v} ( X, Z ) = \lambda</equation>（Ⅱ）Z的分布律为<equation>P\{Z = i\} = \left\{ \begin{array}{ll}\frac{1}{2}\cdot \frac{\lambda^{i}\mathrm{e}^{-\lambda}}{i!}, & i > 0,\\ \mathrm{e}^{-\lambda}, & i = 0,\\ \frac{1}{2}\cdot \frac{\lambda^{-i}\mathrm{e}^{-\lambda}}{(-i)!}, & i < 0. \end{array} \right.</equation>
**解析: **解（I）（法一）注意到<equation>X</equation>与Y相互独立，故<equation>X^{2}</equation>与Y也相互独立.

根据协方差的计算公式，<equation>\begin{aligned} \operatorname {C o v} (X, Z) &= E (X Z) - E (X) E (Z) \stackrel {Z = X Y} {=} E \left(X ^ {2} Y\right) - E (X) E (X Y) \\ \stackrel {\text {独立 性}} {=} E \left(X ^ {2}\right) E (Y) - \left[ E (X) \right] ^ {2} E (Y). \end{aligned}</equation>由于 X的概率分布为<equation>P \{ X=1 \} = P \{ X=-1 \} = \frac{1}{2}</equation>，故<equation>E (X) = 1 \times \frac {1}{2} + (- 1) \times \frac {1}{2} = 0, \quad E \left(X ^ {2}\right) = 1 ^ {2} \times \frac {1}{2} + (- 1) ^ {2} \times \frac {1}{2} = 1.</equation>又因为<equation>Y</equation>服从参数为<equation>\lambda</equation>的泊松分布，所以<equation>E(Y) = \lambda</equation>因此，<equation>\operatorname {C o v} (X, Z) = E \left(X ^ {2}\right) E (Y) - \left[ E (X) \right] ^ {2} E (Y) = 1 \times \lambda - 0 = \lambda .</equation>（法二）由于<equation>X^{2}=1</equation>，故<equation>XZ=X(XY)=X^{2}Y=Y</equation>，而Y服从参数为<equation>\lambda</equation>的泊松分布，于是，<equation>E(XZ)=E(Y)=\lambda.</equation>由法一可知，<equation>E ( X ) = 0</equation>因此，<equation>\operatorname {C o v} (X, Z) = E (X Z) - E (X) E (Z) = \lambda - 0 = \lambda .</equation>（Ⅱ）由于<equation>Z = XY</equation>，故<equation>Z</equation>的所有可能的取值为<equation>i</equation>，其中<equation>i</equation>为整数.

当 i > 0时，<equation>\begin{aligned} P \{Z = i \} &= P \{X Y = i \} = P \{X = 1, Y = i \} \xlongequal {\text {独立 性}} P \{X = 1 \} P \{Y = i \} \\ &= \frac {1}{2} \cdot \frac {\lambda^ {i} \mathrm {e} ^ {- \lambda}}{i !}. \end{aligned}</equation>当 i = 0时，<equation>P \{Z = 0 \} = P \{X Y = 0 \} \xlongequal {X \text {不 为} 0} P \{Y = 0 \} = \mathrm {e} ^ {- \lambda}.</equation>当 i < 0时，<equation>\begin{aligned} P \{Z = i \} &= P \{X Y = i \} = P \{X = - 1, Y = - i \} \xlongequal {\text {独立性}} P \{X = - 1 \} P \{Y = - i \} \\ &= \frac {1}{2} \cdot \frac {\lambda^ {- i} \mathrm {e} ^ {- \lambda}}{(- i) !}. \end{aligned}</equation>因此，Z的分布律为<equation>P\{Z = i\} = \left\{ \begin{array}{ll}\frac{1}{2}\cdot \frac{\lambda^{i}\mathrm{e}^{-\lambda}}{i!}, & i > 0,\\ \mathrm{e}^{-\lambda}, & i = 0,\\ \frac{1}{2}\cdot \frac{\lambda^{-i}\mathrm{e}^{-\lambda}}{(-i)!}, & i < 0. \end{array} \right.</equation>

---

**2016年第8题 | 选择题 | 4分 | 答案: A**
8. 随机试验 E有三种两两不相容的结果<equation>A_{1}, A_{2}, A_{3}</equation>，且三种结果发生的概率均为<equation>\frac{1}{3}</equation>，将试验 E独立重复做2次， X表示2次试验中结果<equation>A_{1}</equation>发生的次数，Y表示2次试验中结果<equation>A_{2}</equation>发生的次数，则 X与 Y的相关系数为（    )

A.<equation>-\frac{1}{2}</equation>B.<equation>-\frac{1}{3}</equation>C.<equation>\frac{1}{3}</equation>D.<equation>\frac{1}{2}</equation>
答案: A
**解析: **解（法一）由题设知，<equation>X\sim B\left(2,\frac{1}{3}\right),Y\sim B\left(2,\frac{1}{3}\right)</equation>，从而<equation>E (X) = E (Y) = 2 \times \frac {1}{3} = \frac {2}{3}, \quad D (X) = D (Y) = 2 \times \frac {1}{3} \times \left(1 - \frac {1}{3}\right) = \frac {4}{9}.</equation>又 XY所有可能的取值为0，1，故<equation>E ( X Y ) = 0 \cdot P \{ X Y = 0 \} + 1 \cdot P \{ X Y = 1 \} = P \{ X = 1, Y = 1 \} = \mathrm {C} _ {2} ^ {1} \times \frac {1}{3} \times \frac {1}{3} = \frac {2}{9},</equation>从而<equation>\rho_{X Y}=\frac{E(X Y)-E(X)E(Y)}{\sqrt{D(X)}\sqrt{D(Y)}}=\frac{\frac{2}{9}-\frac{2}{3}\times \frac{2}{3}}{\frac{4}{9}}=-\frac{1}{2}.</equation>应选A.

（法二）记Z表示2次试验中结果<equation>A_{3}</equation>发生的次数，则<equation>X+Y+Z=2</equation>从而<equation>D (Z) = D (2 - X - Y) = D (X + Y) = D (X) + D (Y) + 2 \operatorname {C o v} (X, Y).</equation>又由题设知，<equation>D ( X )=D ( Y )=D ( Z )</equation>，故<equation>D ( X )=-2\operatorname{C o v} ( X , Y )</equation>，从而<equation>\rho_ {X Y} = \frac {\operatorname {C o v} (X , Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {\operatorname {C o v} (X , Y)}{D (X)} = - \frac {1}{2}.</equation>应选A.

---

**2015年第8题 | 选择题 | 4分 | 答案: D**
8. 设随机变量 X,Y不相关，且<equation>E ( X )=2, E ( Y )=1, D ( X )=3</equation>，则<equation>E [ X ( X+Y-2) ]=</equation>(    )

A. -3 B. 3 C. -5 D. 5
答案: D
**解析: **解 由题设知，<equation>\rho_{XY}=\frac{\operatorname{Cov}(X,Y)}{\sqrt{D(X)}\sqrt{D(Y)}}=\frac{E(XY)-E(X)E(Y)}{\sqrt{D(X)}\sqrt{D(Y)}}=0</equation>，从而<equation>E(XY)=E(X)E(Y)</equation>于是<equation>\begin{aligned} E [ X (X + Y - 2) ] &= E \left(X ^ {2}\right) + E (X Y) - 2 E (X) \\ &= D (X) + \left[ E (X) \right] ^ {2} + E (X) E (Y) - 2 E (X) \\ &= 3 + 4 + 2 - 4 = 5. \end{aligned}</equation>应选 D.

---

**2012年第8题 | 选择题 | 4分 | 答案: D**
8. 将长度为1m的木棒随机地截成两段，则两段长度的相关系数为（    ）

A. 1 B.<equation>\frac{1}{2}</equation>C.<equation>-\frac{1}{2}</equation>D. -1
答案: D
**解析: **解（法一）设木棒被截成两段的长度分别为 X，Y，则有 X+Y=1，即 Y=1-X.于是<equation>D(Y)=D(1-X)=D(X),</equation><equation>\operatorname{Cov}(X,Y)=\operatorname{Cov}(X,1-X)=-\operatorname{Cov}(X,X)=-D(X),</equation>从而<equation>\rho_ {X Y} = \frac {\operatorname {C o v} (X , Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {- D (X)}{\sqrt {D (X)} \sqrt {D (X)}} = - 1.</equation>应选 D.

（法二）由于<equation>|\rho_{XY}|=1</equation>的充要条件是存在常数 a,b，使得<equation>P\{Y=a+bX\}=1</equation>，且此时<equation>\rho_{XY}=\frac{b}{|b|}</equation>由于 Y=1-X，故<equation>\rho_{XY}=-1</equation>从而选D.

---

**2012年第22题 | 解答题 | 11分**

设二维离散型随机变量<equation>(X, Y)</equation>的概率分布为

<table border="1"><tr><td>X\ Y</td><td>0</td><td>1</td><td>2</td></tr><tr><td>0</td><td>1/4</td><td>0</td><td>1/4</td></tr><tr><td>1</td><td>0</td><td>1/3</td><td>0</td></tr><tr><td>2</td><td>1/12</td><td>0</td><td>1/12</td></tr></table>

I. 求<equation>P\{X = 2Y\}</equation>;

II. 求<equation>\operatorname{Cov}(X - Y, Y)</equation>.
**答案: **(22) （ I )<equation>P \{ X=2 Y \}=\frac{1}{4}</equation>；

（Ⅱ）<equation>\operatorname{C o v} ( X-Y, Y)=-\frac{2}{3}.</equation>
**解析: **（ I ）由题设知，<equation>P \{X = 2 Y \} = P \{X = 0, Y = 0 \} + P \{X = 2, Y = 1 \} = \frac {1}{4} + 0 = \frac {1}{4}.</equation>（Ⅱ）由<equation>(X,Y)</equation>的概率分布知，<equation>X,Y</equation>的概率分布分别为

<table border="1"><tr><td>X</td><td>0</td><td>1</td><td>2</td></tr><tr><td>P</td><td><equation>\frac{1}{2}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{6}</equation></td></tr></table>

<table border="1"><tr><td>Y</td><td>0</td><td>1</td><td>2</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td></tr></table>

又由于随机变量 XY可能的值为0，1，2，4，故XY的概率分布为<equation>\begin{aligned} P \{X Y = 0 \} &= P \{X = 0, Y = 0 \} + P \{X = 0, Y = 1 \} + P \{X = 0, Y = 2 \} \\ + P \{X = 1, Y = 0 \} + P \{X = 2, Y = 0 \} \\ &= \frac {1}{4} + 0 + \frac {1}{4} + 0 + \frac {1}{1 2} = \frac {7}{1 2}, \end{aligned}</equation><equation>P \left\{X Y = 1 \right\} = P \left\{X = 1, Y = 1 \right\} = \frac {1}{3},</equation><equation>P \left\{X Y = 2 \right\} = P \left\{X = 1, Y = 2 \right\} + P \left\{X = 2, Y = 1 \right\} = 0 + 0 = 0,</equation><equation>P \{X Y = 4 \} = P \{X = 2, Y = 2 \} = \frac {1}{1 2},</equation>即

<table border="1"><tr><td>XY</td><td>0</td><td>1</td><td>4</td></tr><tr><td>P</td><td><equation>\frac{7}{12}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{12}</equation></td></tr></table>

于是，<equation>E (X) = 0 \times \frac {1}{2} + 1 \times \frac {1}{3} + 2 \times \frac {1}{6} = \frac {2}{3},</equation><equation>E (Y) = 0 \times \frac {1}{3} + 1 \times \frac {1}{3} + 2 \times \frac {1}{3} = 1,</equation><equation>E \left(Y ^ {2}\right) = 0 ^ {2} \times \frac {1}{3} + 1 ^ {2} \times \frac {1}{3} + 2 ^ {2} \times \frac {1}{3} = \frac {5}{3},</equation><equation>E (X Y) = 0 \times \frac {7}{1 2} + 1 \times \frac {1}{3} + 4 \times \frac {1}{1 2} = \frac {2}{3}.</equation>因此，<equation>\begin{aligned} \operatorname {C o v} (X - Y, Y) &= \operatorname {C o v} (X, Y) - \operatorname {C o v} (Y, Y) = \left[ E (X Y) - E (X) E (Y) \right] - \left[ E \left(Y ^ {2}\right) - \left[ E (Y) \right] ^ {2} \right] \\ &= \left(\frac {2}{3} - \frac {2}{3} \times 1\right) - \left(\frac {5}{3} - 1 ^ {2}\right) = - \frac {2}{3}. \end{aligned}</equation>

---

**2011年第14题 | 填空题 | 4分**
14. 设二维随机变量<equation>(X, Y)</equation>服从正态分布<equation>N\left(\mu, \mu; \sigma^2, \sigma^2; 0\right)</equation>, 则<equation>E(XY^2) =</equation>___
**答案: **##<equation>\mu\sigma^{2}+\mu^{3}.</equation>
**解析: **解由（X，Y）服从正态分布<equation>N(\mu ,\mu ;\sigma^{2},\sigma^{2};0)</equation>知，<equation>X\sim N(\mu ,\sigma^{2}),Y\sim N(\mu ,\sigma^{2})</equation>且<equation>\rho_{XY}=0.</equation>由于对二维正态随机变量，不相关与相互独立等价，故X与Y相互独立，从而X与<equation>Y^{2}</equation>相互独立.于是<equation>E(XY^{2})=E(X)E(Y^{2})=E(X)[D(Y)+[E(Y)]^{2}]</equation><equation>=\mu(\sigma^{2}+\mu^{2})=\mu\sigma^{2}+\mu^{3}.</equation>

---

**2011年第22题 | 解答题 | 11分**

设随机变量<equation>X</equation>与<equation>Y</equation>的概率分布分别为

<table border="1"><tr><td>X</td><td>0</td><td>1</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{2}{3}</equation></td></tr></table>

<table border="1"><tr><td>Y</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td></tr></table>

且<equation>P \left\{X^{2}=Y^{2}\right\}=1.</equation>I. 求二维随机变量（X,Y）的概率分布；

II. 求<equation>Z=XY</equation>的概率分布；

III. 求 X与Y的相关系数<equation>\rho_{XY}</equation>.
**答案: **(22) （I）

<table border="1"><tr><td rowspan="2">X\ Y</td><td colspan="3">-1</td></tr><tr><td>0</td><td>1/3</td><td>0</td></tr><tr><td>1</td><td>1/3</td><td>0</td><td>1/3</td></tr><tr><td>Z</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>P</td><td>1/3</td><td>1/3</td><td>1/3</td></tr></table>

(Ⅱ)

( III ) 0.
**解析: **（I）由<equation>P\{X^{2} = Y^{2}\} = 1</equation>知，<equation>P\{X^{2}\neq Y^{2}\} = 0.</equation>于是，<equation>P \{X = 0, Y = - 1 \} = P \{X = 0, Y = 1 \} = P \{X = 1, Y = 0 \} = 0.</equation>从而<equation>P \{X = 0, Y = 0 \} = P \{Y = 0 \} - P \{X = 1, Y = 0 \} = \frac {1}{3} - 0 = \frac {1}{3},</equation><equation>P \{X = 1, Y = 1 \} = P \{Y = 1 \} - P \{X = 0, Y = 1 \} = \frac {1}{3} - 0 = \frac {1}{3},</equation><equation>P \{X = 1, Y = - 1 \} = P \{Y = - 1 \} - P \{X = 0, Y = - 1 \} = \frac {1}{3} - 0 = \frac {1}{3}.</equation>因此，<equation>( X, Y )</equation>的概率分布为

<table border="1"><tr><td>X\ Y</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>0</td><td><equation>\frac{1}{3}</equation></td><td>0</td></tr><tr><td>1</td><td><equation>\frac{1}{3}</equation></td><td>0</td><td><equation>\frac{1}{3}</equation></td></tr></table>

（Ⅱ）由于<equation>Z=XY</equation>可能的取值为-1，0，1，且<equation>P \{Z = - 1 \} = P \{X = 1, Y = - 1 \} = \frac {1}{3},</equation><equation>P \{Z = 1 \} = P \{X = 1, Y = 1 \} = \frac {1}{3},</equation><equation>P \{Z = 0 \} = 1 - P \{Z = - 1 \} - P \{Z = 1 \} = \frac {1}{3},</equation>故 Z = XY的概率分布为

<table border="1"><tr><td>Z</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td></tr></table>

（Ⅲ）由于<equation>E (X) = 0 \times \frac {1}{3} + 1 \times \frac {2}{3} = \frac {2}{3}, \quad E \left(X ^ {2}\right) = 0 ^ {2} \times \frac {1}{3} + 1 ^ {2} \times \frac {2}{3} = \frac {2}{3},</equation><equation>D (X) = E \left(X ^ {2}\right) - \left[ E (X) \right] ^ {2} = \frac {2}{9},</equation><equation>E (Y) = (- 1) \times \frac {1}{3} + 0 \times \frac {1}{3} + 1 \times \frac {1}{3} = 0, \quad E \left(Y ^ {2}\right) = (- 1) ^ {2} \times \frac {1}{3} + 0 ^ {2} \times \frac {1}{3} + 1 ^ {2} \times \frac {1}{3} = \frac {2}{3},</equation><equation>D (Y) = E \left(Y ^ {2}\right) - \left[ E (Y) \right] ^ {2} = \frac {2}{3},</equation><equation>E (X Y) = E (Z) = (- 1) \times \frac {1}{3} + 0 \times \frac {1}{3} + 1 \times \frac {1}{3} = 0,</equation>故<equation>\rho_ {X Y} = \frac {\operatorname {C o v} (X , Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = 0.</equation>

---


### 随机变量及其分布

**2025年第9题 | 选择题 | 5分 | 答案: C**
9. 设<equation>X_{1}, X_{2}, \dots , X_{2 0}</equation>是来自总体B(1,0.1)的简单随机样本，令<equation>T=\sum_{i=1}^{2 0} X_{i}</equation>利用泊松分布近似表示二项分布的方法可得<equation>P\{ T\leqslant 1\}\approx</equation>(    )

A.<equation>\frac{1} {\mathrm{e}^{2}}</equation>B.<equation>\frac{2} {\mathrm{e}^{2}}</equation>C.<equation>\frac{3} {\mathrm{e}^{2}}</equation>D.<equation>\frac{4} {\mathrm{e}^{2}}</equation>
答案: C
**解析: **解 由<equation>X_{i}(i = 1,2,\dots ,20)\sim B(1,0.1)</equation>可知，<equation>X_{i}</equation>可看作一次随机试验的结果，试验成功的概率为0.1，<equation>T = \sum_{i = 1}^{20}X_{i}</equation>可看作20次独立重复试验中试验成功的次数，服从<equation>B(20,0.1)</equation>.根据泊松定理，<equation>n = 20,p_{n} = 0.1,\lambda = 2,T</equation>近似服从参数为2的泊松分布.

因此，<equation>P \{T \leqslant 1 \} = P \{T = 0 \} + P \{T = 1 \} \approx \frac {2 ^ {0} \cdot \mathrm {e} ^ {- 2}}{1} + \frac {2 ^ {1} \cdot \mathrm {e} ^ {- 2}}{1} = \frac {3}{\mathrm {e} ^ {2}}.</equation>应选C.

---

**2024年第8题 | 选择题 | 5分 | 答案: B**
8. 设随机变量 X,Y相互独立，且 X服从正态分布 N(0,2),Y服从正态分布 N(-2,2).若<equation>P\{2 X+Y< a \}=P\{X>Y\}</equation>，则 a=（    )
