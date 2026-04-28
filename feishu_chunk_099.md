#### 向量组之间的线性表示

**2023年第7题 | 选择题 | 5分 | 答案: D**

7. 已知向量<equation>\alpha_{1}=\left( \begin{array}{c}1\\ 2\\ 3 \end{array} \right),\alpha_{2}=\left( \begin{array}{c}2\\ 1\\ 1 \end{array} \right),\beta_{1}=\left( \begin{array}{c}2\\ 5\\ 9 \end{array} \right),\beta_{2}=\left( \begin{array}{c}1\\ 0\\ 1 \end{array} \right),</equation>若<equation>\gamma</equation>既可由<equation>\alpha_{1},\alpha_{2}</equation>线性表示，也可由<equation>\beta_{1},\beta_{2}</equation>线性表示，则<equation>\gamma=</equation>（    ）

A.<equation>k\left( \begin{array}{c}3\\ 3\\ 4 \end{array} \right),k \in \mathbf{R}</equation>B.<equation>k\left( \begin{array}{c}3\\ 5\\ 10 \end{array} \right),k \in \mathbf{R}</equation>C.<equation>k\left( \begin{array}{c}-1\\ 1\\ 2 \end{array} \right),k \in \mathbf{R}</equation>D.<equation>k\left( \begin{array}{c}1\\ 5\\ 8 \end{array} \right),k \in \mathbf{R}</equation>

答案: D

**解析:**解（法一）由于<equation>\boldsymbol{\gamma}</equation>既可由<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2}</equation>线性表示，也可由<equation>\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2}</equation>线性表示，故存在<equation>k_{1},k_{2},l_{1},l_{2}</equation>，使得<equation>\boldsymbol{\gamma}=k_{1}\boldsymbol{\alpha}_{1}+k_{2}\boldsymbol{\alpha}_{2}=l_{1}\boldsymbol{\beta}_{1}+l_{2}\boldsymbol{\beta}_{2}</equation>.于是，<equation>\left(k_{1},-l_{1},k_{2},-l_{2}\right)^{\mathrm{T}}</equation>是齐次线性方程组<equation>\left(\boldsymbol{\alpha}_{1},\boldsymbol{\beta}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\beta}_{2}\right)\boldsymbol{x}=\mathbf{0}</equation>的解.

记<equation>A = \left(\alpha_{1},\beta_{1},\alpha_{2},\beta_{2}\right)</equation>，对A作初等行变换.<equation>\begin{array}{l} \boldsymbol {A} = \left( \begin{array}{c c c c} 1 & 2 & 2 & 1 \\ 2 & 5 & 1 & 0 \\ 3 & 9 & 1 & 1 \end{array} \right) \xrightarrow {r _ {2} - 2 r _ {1}} \frac {r _ {2} - 2 r _ {1}}{r _ {3} - 3 r _ {1}} \left( \begin{array}{c c c c} 1 & 2 & 2 & 1 \\ 0 & 1 & - 3 & - 2 \\ 0 & 3 & - 5 & - 2 \end{array} \right) \xrightarrow {r _ {1} - 2 r _ {2} ^ {*}} \left( \begin{array}{c c c c} 1 & 0 & 8 & 5 \\ 0 & 1 & - 3 & - 2 \\ 0 & 0 & 4 & 4 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {* *} \times \frac {1}{4}} \left( \begin{array}{c c c c} 1 & 0 & 8 & 5 \\ 0 & 1 & - 3 & - 2 \\ 0 & 0 & 1 & 1 \end{array} \right) \xrightarrow {r _ {1} ^ {*} - 8 r _ {3} ^ {* * *}} \left( \begin{array}{c c c c} 1 & 0 & 0 & - 3 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 \end{array} \right). \\ \end{array}</equation>（<equation>r_{t}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每作一次初等行变换，加一个<equation>*.</equation>）

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


