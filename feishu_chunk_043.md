#### 向量组之间的线性表示

**2023年第10题 | 选择题 | 5分 | 答案: D**

10. 已知向量<equation>\alpha_{1}=\left( \begin{array}{c}1\\ 2\\ 3 \end{array} \right),\alpha_{2}=\left( \begin{array}{c}2\\ 1\\ 1 \end{array} \right),\beta_{1}=\left( \begin{array}{c}2\\ 5\\ 9 \end{array} \right),\beta_{2}=\left( \begin{array}{c}1\\ 0\\ 1 \end{array} \right)</equation>若<equation>\gamma</equation>既可由<equation>\alpha_{1},\alpha_{2}</equation>线性表示，也可由<equation>\beta_{1},\beta_{2}</equation>线性表示，则<equation>\gamma=(\quad)</equation>A. k<equation>\left( \begin{array}{c}3\\ 3\\ 4 \end{array} \right),k \in \mathbf{R}</equation>B. k<equation>\left( \begin{array}{c}3\\ 5\\ 10 \end{array} \right),k \in \mathbf{R}</equation>C. k<equation>\left( \begin{array}{c}-1\\ 1\\ 2 \end{array} \right),k \in \mathbf{R}</equation>D. k<equation>\left( \begin{array}{c}1\\ 5\\ 8 \end{array} \right),k \in \mathbf{R}</equation>

答案: D

**解析:**解 由于<equation>\boldsymbol{\gamma}</equation>既可由<equation>\alpha_{1},\alpha_{2}</equation>线性表示，也可由<equation>\beta_{1},\beta_{2}</equation>线性表示，故存在<equation>k_{1},k_{2},l_{1},l_{2}</equation>，使得<equation>\boldsymbol{\gamma}=k_{1}\boldsymbol{\alpha}_{1}</equation><equation>+ k_{2}\boldsymbol{\alpha}_{2}=l_{1}\boldsymbol{\beta}_{1}+l_{2}\boldsymbol{\beta}_{2}</equation>.于是，<equation>\left(k_{1},-l_{1},k_{2},-l_{2}\right)^{\mathrm{T}}</equation>是齐次线性方程组<equation>\left(\alpha_{1},\beta_{1},\alpha_{2},\beta_{2}\right)\boldsymbol{x}=\mathbf{0}</equation>的解.

记<equation>A=(\alpha_{1},\beta_{1},\alpha_{2},\beta_{2})</equation>，对A作初等行变换.

---<equation>\begin{array}{l} \boldsymbol {A} = \left( \begin{array}{c c c c} 1 & 2 & 2 & 1 \\ 2 & 5 & 1 & 0 \\ 3 & 9 & 1 & 1 \end{array} \right) \xrightarrow [ r _ {3} - 3 r _ {1} ]{r _ {2} - 2 r _ {1}} \left( \begin{array}{c c c c} 1 & 2 & 2 & 1 \\ 0 & 1 & - 3 & - 2 \\ 0 & 3 & - 5 & - 2 \end{array} \right) \xrightarrow [ r _ {3} ^ {*} - 3 r _ {2} ^ {*} ]{r _ {1} - 2 r _ {2} ^ {*}} \left( \begin{array}{c c c c} 1 & 0 & 8 & 5 \\ 0 & 1 & - 3 & - 2 \\ 0 & 0 & 4 & 4 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {* *} \times \frac {1}{4}} \left( \begin{array}{c c c c} 1 & 0 & 8 & 5 \\ 0 & 1 & - 3 & - 2 \\ 0 & 0 & 1 & 1 \end{array} \right) \xrightarrow {r _ {1} ^ {*} - 8 r _ {3} ^ {* * *}} \left( \begin{array}{c c c c} 1 & 0 & 0 & - 3 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 \end{array} \right). \\ \end{array}</equation>（<equation>r_{t}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

取<equation>x_{4}=1</equation>，可得<equation>\boldsymbol{\xi}=(3,-1,-1,1)^{\mathrm{T}}</equation>为该方程组的一个基础解系，从而<equation>\left(k_{1},-l_{1},k_{2},-l_{2}\right)^{\mathrm{T}}= k \left(3,-1,-1,1\right)^{\mathrm{T}}</equation>，其中<equation>k \in \mathbf{R}.</equation>因此，<equation>\gamma = k _ {1} \alpha_ {1} + k _ {2} \alpha_ {2} = 3 k \binom {1} {2} - k \binom {2} {1} = k \binom {1} {5}, \quad k \in \mathbf {R}.</equation>应选 D.

---

**2022年第10题 | 选择题 | 5分 | 答案: C**

10. 设<equation>\alpha_{1}=(\lambda,1,1)^{\mathrm{T}},\alpha_{2}=(1,\lambda,1)^{\mathrm{T}},\alpha_{3}=(1,1,\lambda)^{\mathrm{T}},\alpha_{4}=(1,\lambda, \lambda^{2})^{\mathrm{T}}</equation>，若<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>等价，则<equation>\lambda</equation>的取值范围是（    ）

A.<equation>\{0,1\}</equation>B.<equation>\{\lambda \mid \lambda \in \mathbf{R},\lambda \neq -2\}</equation>C.<equation>\{\lambda \mid \lambda \in \mathbf{R},\lambda \neq -1,\lambda \neq -2\}</equation>D.<equation>\{\lambda \mid \lambda \in \mathbf{R},\lambda \neq -1\}</equation>

答案: C

**解析:**解（法一）当<equation>\lambda=1</equation>时，<equation>\alpha_{1}=\alpha_{2}=\alpha_{3}=\alpha_{4}=\left( \begin{array}{c}1\\ 1\\ 1 \end{array} \right).</equation>此时<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>显然等价当<equation>\lambda\neq1</equation>时，考虑矩阵<equation>A=(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4}).</equation><equation>\begin{array}{l} A = \left( \begin{array}{c c c c} \lambda & 1 & 1 & 1 \\ 1 & \lambda & 1 & \lambda \\ 1 & 1 & \lambda & \lambda^ {2} \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 1 & 1 & \lambda & \lambda^ {2} \\ \lambda & 1 & 1 & 1 \end{array} \right) \xrightarrow {r _ {2} - r _ {1}} \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 0 & 1 - \lambda & \lambda - 1 & \lambda^ {2} - \lambda \\ 0 & 1 - \lambda^ {2} & 1 - \lambda & 1 - \lambda^ {2} \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} \times \frac {1}{1 - \lambda}} \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 0 & 1 & - 1 & - \lambda \\ 0 & 1 + \lambda & 1 & 1 + \lambda \end{array} \right) \xrightarrow {r _ {3} ^ {* *} - (1 + \lambda) r _ {2} ^ {* *}} \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 0 & 1 & - 1 & - \lambda \\ 0 & 0 & \lambda + 2 & (\lambda + 1) ^ {2} \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

由于 A有2阶非零子式<equation>\left| \begin{array}{ll} \lambda & 1 \\ 1 & \lambda \end{array} \right|</equation>，故<equation>r(A)\geqslant 2</equation>另一方面，因为不存在<equation>\lambda</equation>满足<equation>\lambda +2=(\lambda+1)^{2}=</equation>0，所以<equation>r(A)=3.</equation><equation>r(\alpha_{1},\alpha_{2},\alpha_{3})=3</equation>当且仅当<equation>\lambda\neq-2.</equation><equation>r(\alpha_{1},\alpha_{2},\alpha_{4})=3</equation>当且仅当<equation>\lambda\neq-1.</equation>因此，当<equation>\lambda\neq1</equation>时，<equation>r(A)=r(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4})=r(\alpha_{1},\alpha_{2},\alpha_{3})=r(\alpha_{1},\alpha_{2},\alpha_{4})</equation>当且仅当<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1.</equation>注意到<equation>\lambda=1</equation>也包含在条件<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1</equation>中，故<equation>r(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4})=r(\alpha_{1},\alpha_{2},\alpha_{3})= r(\alpha_{1},\alpha_{2},\alpha_{4})</equation>当且仅当<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1.</equation>综上所述，应选C.

（法二）分别计算<equation>|\alpha_{1},\alpha_{2},\alpha_{3}|</equation>，<equation>|\alpha_{1},\alpha_{2},\alpha_{4}|</equation><equation>\left| \alpha_ {1}, \alpha_ {2}, \alpha_ {3} \right| = \left| \begin{array}{c c c} \lambda & 1 & 1 \\ 1 & \lambda & 1 \\ 1 & 1 & \lambda \end{array} \right| = \left| \begin{array}{c c c} \lambda & 1 - \lambda & 1 - \lambda^ {2} \\ 1 & \lambda - 1 & 1 - \lambda \\ 1 & 0 & 0 \end{array} \right| = (1 - \lambda) ^ {2} (\lambda + 2).</equation><equation>\left| \alpha_ {1}, \alpha_ {2}, \alpha_ {4} \right| = \left| \begin{array}{c c c} \lambda & 1 & 1 \\ 1 & \lambda & \lambda \\ 1 & 1 & \lambda^ {2} \end{array} \right| = \left| \begin{array}{c c c} \lambda & 1 - \lambda & 1 - \lambda^ {3} \\ 1 & \lambda - 1 & \lambda - \lambda^ {2} \\ 1 & 0 & 0 \end{array} \right| = (1 - \lambda) ^ {2} (1 + \lambda) ^ {2}.</equation>当<equation>\lambda\neq1,-2,-1</equation>时，<equation>|\alpha_{1},\alpha_{2},\alpha_{3}|</equation>与<equation>|\alpha_{1},\alpha_{2},\alpha_{4}|</equation>均不为0.此时，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>和<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>均为3维列向量组的极大无关组，从而等价.

当<equation>\lambda=1</equation>时，<equation>\alpha_{1}=\alpha_{2}=\alpha_{3}=\alpha_{4}=\left( \begin{array}{c}1\\ 1\\ 1 \end{array} \right).</equation>此时<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>显然等价.

当<equation>\lambda=-2</equation>或<equation>\lambda=-1</equation>时，<equation>|\alpha_{1},\alpha_{2},\alpha_{3}| \neq |\alpha_{1},\alpha_{2},\alpha_{4}|</equation>，且其中一个为0，另一个不为0，说明两向量组的秩不相等，从而不等价.

综上所述，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>等价当且仅当<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1.</equation>应选C.

---

**2019年第22题 | 解答题 | 11分**

22. （本题满分11分）

2. (本题满分11分)

已知向量组 I：<equation>\alpha_{1}=\left( \begin{array}{c}1\\ 1\\ 4 \end{array} \right),\alpha_{2}=\left( \begin{array}{c}1\\ 0\\ 4 \end{array} \right),\alpha_{3}=\left( \begin{array}{c}1\\ 2\\ a^{2}+3 \end{array} \right)</equation>与向量组 II：<equation>\beta_{1}=\left( \begin{array}{c}1\\ 1\\ a+3 \end{array} \right),\beta_{2}=\left( \begin{array}{c}0\\ 2\\ 1-a \end{array} \right),</equation><equation>\beta_{3}=\left( \begin{array}{c}1\\ 3\\ a^{2}+3 \end{array} \right).</equation>若向量组 I与Ⅱ等价，求 a的取值，并将<equation>\beta_{3}</equation>用<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性表示.

**答案:**当 a≠-1时，向量组Ⅰ与向量组Ⅱ等价。当 a=1时，<equation>\boldsymbol{\beta}_{3}=(3-2k)\boldsymbol{\alpha}_{1}+(-2+k)\boldsymbol{\alpha}_{2}+k\boldsymbol{\alpha}_{3}</equation>其中 k为任意常数；当 a≠±1时，<equation>\boldsymbol{\beta}_{3}=\boldsymbol{\alpha}_{1}-\boldsymbol{\alpha}_{2}+\boldsymbol{\alpha}_{3}.</equation>

**解析:**解记<equation>A=(\alpha_{1},\alpha_{2},\alpha_{3}),B=(\beta_{1},\beta_{2},\beta_{3})</equation>，则由向量组Ⅰ与向量组Ⅱ等价可知<equation>r(A)= r(B)=r(A,B).</equation>对（A,B）作初等行变换.<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {B}) = \left( \begin{array}{c c c c c c} 1 & 1 & 1 & 1 & 0 & 1 \\ 1 & 0 & 2 & 1 & 2 & 3 \\ 4 & 4 & a ^ {2} + 3 & a + 3 & 1 - a & a ^ {2} + 3 \end{array} \right) \\ \xrightarrow {r _ {2} - r _ {1}} \frac {1}{r _ {3} - 4 r _ {1}} \left( \begin{array}{c c c c c c} 1 & 1 & 1 & 1 & 0 & 1 \\ 0 & - 1 & 1 & 0 & 2 & 2 \\ 0 & 0 & a ^ {2} - 1 & a - 1 & 1 - a & a ^ {2} - 1 \end{array} \right). \\ \end{array}</equation>由上式可知<equation>r(A)\geqslant 2</equation>，故<equation>r(A) = 2</equation>或<equation>r(A) = 3.</equation>当<equation>a^{2}-1=0</equation>时，<equation>a=1</equation>或<equation>a=-1</equation><equation>r(A)=2</equation>.又由于当<equation>a=-1</equation>时，<equation>r(A,B)=3</equation>，故<equation>a=-1</equation>不符合题意，而当<equation>a=1</equation>时，<equation>r(A)=r(B)=r(A,B)=2</equation>，此时向量组 I与向量组Ⅱ等价.

当 a = 1时，<equation>\left(\boldsymbol {A}, \boldsymbol {\beta} _ {3}\right)\rightarrow \left(\begin{array}{c c c c}1&1&1&1\\0&- 1&1&2\\0&0&0&0\end{array}\right) \xrightarrow {r _ {2} \times (- 1)} \left(\begin{array}{c c c c}1&1&1&1\\0&1&- 1&- 2\\0&0&0&0\end{array}\right) \xrightarrow {r _ {1} - r _ {2} ^ {*}} \left(\begin{array}{c c c c}1&0&2&3\\0&1&- 1&- 2\\0&0&0&0\end{array}\right).</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

取<equation>x_{3}</equation>为自由变元，令<equation>x_{3} = 1</equation>，可得<equation>(-2,1,1)^{\mathrm{T}}</equation>为<equation>Ax = 0</equation>的一个基础解系。又因为<equation>(3,-2,0)^{\mathrm{T}}</equation>为<equation>Ax = \beta_{3}</equation>的一个特解，所以<equation>Ax = \beta_{3}</equation>的通解为<equation>k(-2,1,1)^{\mathrm{T}} + (3,-2,0)^{\mathrm{T}}</equation>，其中<equation>k</equation>为任意常数.

因此，<equation>\boldsymbol {\beta} _ {3} = (3 - 2 k) \boldsymbol {\alpha} _ {1} + (- 2 + k) \boldsymbol {\alpha} _ {2} + k \boldsymbol {\alpha} _ {3},</equation>其中 k为任意常数.

当 a<equation>\neq\pm1</equation>时，<equation>a^{2}-1\neq0,r(A)=r(B)=r(A,B)=3</equation>，向量组Ⅰ与向量组Ⅱ等价，且它们相互之间的线性表示唯一.<equation>\left(\boldsymbol {A}, \boldsymbol {\beta} _ {3}\right)\rightarrow \left(\begin{array}{c c c c}1&1&1&1\\0&- 1&1&2\\0&0&1&1\end{array}\right) \xrightarrow [ r _ {1} - r _ {2} ^ {*} ]{r _ {2} \times (- 1)} \left(\begin{array}{c c c c}1&0&2&3\\0&1&- 1&- 2\\0&0&1&1\end{array}\right) \xrightarrow [ r _ {2} ^ {*} + r _ {3} ]{r _ {1} ^ {*} - 2 r _ {3}} \left(\begin{array}{c c c c}1&0&0&1\\0&1&0&- 1\\0&0&1&1\end{array}\right).</equation>因此，<equation>A x=\beta_{3}</equation>的唯一解为<equation>(1,-1,1)^{\mathrm{T}}.</equation><equation>\boldsymbol {\beta} _ {3} = \boldsymbol {\alpha} _ {1} - \boldsymbol {\alpha} _ {2} + \boldsymbol {\alpha} _ {3}.</equation>综上所述，当<equation>a\neq -1</equation>时，向量组I与向量组Ⅱ等价。当<equation>a = 1</equation>时，<equation>\beta_{3} = (3 - 2k)\alpha_{1} + (-2 + k)\alpha_{2} + k\alpha_{3}</equation>，其中k为任意常数；当<equation>a\neq \pm 1</equation>时，<equation>\beta_{3} = \alpha_{1} - \alpha_{2} + \alpha_{3}</equation>.

---

**2013年第7题 | 选择题 | 4分 | 答案: B**

7. 设 A,B,C均为 n阶矩阵. 若 AB=C，且 B可逆，则（    ）

A. 矩阵 C的行向量组与矩阵 A的行向量组等价

B. 矩阵 C的列向量组与矩阵 A的列向量组等价

C. 矩阵 C的行向量组与矩阵 B的行向量组等价

D. 矩阵 C的列向量组与矩阵 B的列向量组等价

答案: B

**解析:**我们证明 C的列向量组与 A的列向量组能相互线性表示.

不妨设<equation>A = \left(\alpha_{1},\alpha_{2},\dots ,\alpha_{n}\right),C = \left(\gamma_{1},\gamma_{2},\dots ,\gamma_{n}\right),B = \left(b_{ij}\right)_{n\times n}</equation>，则<equation>\boldsymbol {A B} = \left(\alpha_ {1}, \alpha_ {2}, \dots , \alpha_ {n}\right) \left(b _ {i j}\right) _ {n \times n} = C = \left(\gamma_ {1}, \gamma_ {2}, \dots , \gamma_ {n}\right),</equation><equation>\left\{ \begin{array}{l} \boldsymbol {\gamma} _ {1} = b _ {1 1} \boldsymbol {\alpha} _ {1} + b _ {2 1} \boldsymbol {\alpha} _ {2} + \dots + b _ {n 1} \boldsymbol {\alpha} _ {n}, \\ \boldsymbol {\gamma} _ {2} = b _ {1 2} \boldsymbol {\alpha} _ {1} + b _ {2 2} \boldsymbol {\alpha} _ {2} + \dots + b _ {n 2} \boldsymbol {\alpha} _ {n}, \\ \dots , \\ \boldsymbol {\gamma} _ {n} = b _ {1 n} \boldsymbol {\alpha} _ {1} + b _ {2 n} \boldsymbol {\alpha} _ {2} + \dots + b _ {n n} \boldsymbol {\alpha} _ {n}. \end{array} \right.</equation>因此，C的列向量组<equation>\left( \gamma_{1},\gamma_{2},\dots ,\gamma_{n}\right)</equation>能由A的列向量组<equation>\left( \alpha_{1},\alpha_{2},\dots ,\alpha_{n}\right)</equation>线性表示。同理，由于B可逆，故A的列向量组也能由C的列向量组线性表示.应选B.

下面我们说明选项A、C、D不正确.

选项A：令<equation>A=\left( \begin{array}{cc}1&1\\ 0&0 \end{array} \right), B=\left( \begin{array}{cc}1&1\\ 0&1 \end{array} \right)</equation>，则<equation>C=A B=\left( \begin{array}{cc}1&2\\ 0&0 \end{array} \right).</equation>但A的行向量组<equation>\{(1,1),(0,0)\}</equation>与C的行向量组<equation>\{(1,2),(0,0)\}</equation>不等价.

选项C、D：取B为单位矩阵E，C为一个非满秩矩阵. B的行（列）向量组线性无关，C的行（列）向量组线性相关.

---

**2011年第22题 | 解答题 | 11分**


设向量组<equation>\alpha_{1}=(1,0,1)^{\mathrm{T}},\alpha_{2}=(0,1,1)^{\mathrm{T}},\alpha_{3}=(1,3,5)^{\mathrm{T}}</equation>不能由向量组<equation>\beta_{1}=(1,1,1)^{\mathrm{T}},\beta_{2}=(1,2,3)^{\mathrm{T}},\beta_{3}=(3,4,a)^{\mathrm{T}}</equation>线性表示.

I. 求 a的值；

II. 将<equation>\beta_{1},\beta_{2},\beta_{3}</equation>用<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性表示.

**答案:**22) ( I )<equation>a=5;</equation>( II )<equation>\boldsymbol{\beta}_{1}=2\boldsymbol{\alpha}_{1}+4\boldsymbol{\alpha}_{2}-\boldsymbol{\alpha}_{3},\boldsymbol{\beta}_{2}=\boldsymbol{\alpha}_{1}+2\boldsymbol{\alpha}_{2},\boldsymbol{\beta}_{3}=5\boldsymbol{\alpha}_{1}+10\boldsymbol{\alpha}_{2}-2\boldsymbol{\alpha}_{3}.</equation>

**解析:**解（I）记<equation>A=\left(\alpha_{1},\alpha_{2},\alpha_{3}\right),B=\left(\beta_{1},\beta_{2},\beta_{3}\right),A,B</equation>的列向量组分别记为 A,B.

首先，<equation>|A|=\left| \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 1 & 1 & 5 \end{array} \right|=1</equation>，故<equation>r(A)=3</equation>，A满秩.

由于向量组 B不能线性表示 A，故<equation>r(\mathbf{B})<3</equation>；否则 B也满秩，从而 B能线性表示 A，矛盾.由于<equation>r(\mathbf{B})<3</equation>，故<equation>| \boldsymbol {B} | = \left| \begin{array}{c c c} 1 & 1 & 3 \\ 1 & 2 & 4 \\ 1 & 3 & a \end{array} \right| \frac {c _ {2} - c _ {1}}{c _ {3} - 3 c _ {1}} \left| \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 1 \\ 1 & 2 & a - 3 \end{array} \right| = a - 5 = 0.</equation>因此，<equation>a=5.</equation>（Ⅱ）（法一）求B用A的线性表示，相当于求<equation>A X=B</equation>的解. X的列向量的坐标为线性表示的系数，即<equation>\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)\left(x_{1i},x_{2i},x_{3i}\right)^{\mathrm{T}}=\boldsymbol{\beta}_{i}(i=1,2,3).</equation><equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {B}) = \left( \begin{array}{c c c c c c} 1 & 0 & 1 & 1 & 1 & 3 \\ 0 & 1 & 3 & 1 & 2 & 4 \\ 1 & 1 & 5 & 1 & 3 & 5 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c c c c} 1 & 0 & 1 & 1 & 1 & 3 \\ 0 & 1 & 3 & 1 & 2 & 4 \\ 0 & 1 & 4 & 0 & 2 & 2 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {*} - r _ {2}} \left( \begin{array}{c c c c c c} 1 & 0 & 1 & 1 & 1 & 3 \\ 0 & 1 & 3 & 1 & 2 & 4 \\ 0 & 0 & 1 & - 1 & 0 & - 2 \end{array} \right) \xrightarrow {r _ {1} - r _ {3} ^ {* *}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 2 & 1 & 5 \\ 0 & 1 & 0 & 4 & 2 & 1 0 \\ 0 & 0 & 1 & - 1 & 0 & - 2 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每做一次初等行变换，加一个*.）

因此，<equation>A x=\beta_{1}</equation>的解为<equation>(2,4,-1)^{\mathrm{T}},\beta_{1}=2\alpha_{1}+4\alpha_{2}-\alpha_{3};A x=\beta_{2}</equation>的解为<equation>(1,2,0)^{\mathrm{T}},\beta_{2}=\alpha_{1}+2\alpha_{2};A x=\beta_{3}</equation>的解为<equation>(5,10,-2)^{\mathrm{T}},\beta_{3}=5\alpha_{1}+10\alpha_{2}-2\alpha_{3}.</equation>（法二）用克拉默法则分别求<equation>A x=\beta_{1}, A x=\beta_{2}, A x=\beta_{3}</equation>的解. x的分量为线性表示的系数，即<equation>\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)\left(x_{1},x_{2},x_{3}\right)^{\mathrm{T}}=\beta_{i}(i=1,2,3).</equation>首先，可计算得<equation>|A| = 1</equation>. 由克拉默法则知，<equation>Ax = \beta_{1}</equation>的解为<equation>x _ {1} = \left| \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 3 \\ 1 & 1 & 5 \end{array} \right| = 2, \quad x _ {2} = \left| \begin{array}{c c c} 1 & 1 & 1 \\ 0 & 1 & 3 \\ 1 & 1 & 5 \end{array} \right| = 4, \quad x _ {3} = \left| \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 1 \end{array} \right| = - 1.</equation>因此，<equation>\pmb{\beta}_{1} = 2\pmb{\alpha}_{1} + 4\pmb{\alpha}_{2} - \pmb{\alpha}_{3}</equation>。同理可得<equation>\pmb{\beta}_{2} = \pmb{\alpha}_{1} + 2\pmb{\alpha}_{2},\pmb{\beta}_{3} = 5\pmb{\alpha}_{1} + 10\pmb{\alpha}_{2} - 2\pmb{\alpha}_{3}</equation>。

---

**2010年第7题 | 选择题 | 4分 | 答案: A**

7. 设向量组 I:<equation>\alpha_{1},\alpha_{2},\cdots,\alpha_{r}</equation>可由向量组 II:<equation>\beta_{1},\beta_{2},\cdots,\beta_{s}</equation>线性表示.下列命题正确的是（    ）

A. 若向量组 I 线性无关，则<equation>r\leqslant s</equation>B. 若向量组 I 线性相关，则<equation>r>s</equation>C. 若向量组 II 线性无关，则<equation>r\leqslant s</equation>D. 若向量组 II 线性相关，则<equation>r>s</equation>

答案: A

**解析:**解 由于向量组 I 能被向量组Ⅱ线性表示，故<equation>r_{\mathrm{I}}\leqslant r_{\mathrm{II}}</equation>. 又由题设，有<equation>r_{\mathrm{I}}\leqslant r, r_{\mathrm{II}}\leqslant s.</equation>若向量组 I 线性无关，则<equation>r_{\mathrm{I}}=r</equation>，从而有<equation>r = r _ {\mathrm {I}} \leqslant r _ {\mathrm {I I}} \leqslant s,</equation>即<equation>r\leqslant s</equation>应选A.

下面我们说明选项B、C、D不正确.

考虑 I = {<equation>\left( \begin{array}{c} 1 \\ 0 \end{array} \right),\left( \begin{array}{c} 2 \\ 0 \end{array} \right)</equation>，<equation>\mathrm {I I}=\left\{ \left( \begin{array}{c} 1 \\ 0 \end{array} \right),\left( \begin{array}{c} 0 \\ 1 \end{array} \right),\left( \begin{array}{c} 2 \\ 0 \end{array} \right) \right\}</equation>.<equation>\mathrm {I I}</equation>能表示 I，且向量组 I，<equation>\mathrm {I I}</equation>均线性相关，但<equation>2=r<s=3</equation>.选项B、D不正确.

考虑 I = {<equation>\left\{\begin{array}{l l}1\\0\end{array}\right\},\left(\begin{array}{l l}2\\0\end{array}\right),\left(\begin{array}{l l}3\\0\end{array}\right)</equation>，<equation>\mathrm {II}=\left\{\left(\begin{array}{l l}1\\0\end{array}\right),\left(\begin{array}{l l}0\\1\end{array}\right)\right\}</equation>. II能表示 I，且向量组Ⅱ线性无关，但 3 = r > s=2.选项C不正确.

---


### 二次型

**2024年第22题 | 解答题 | 12分**

22. （本题满分12分）

设矩阵<equation>A=\left( \begin{array}{c c c} 0 & 1 & a \\ 1 & 0 & 1 \end{array} \right), B=\left( \begin{array}{c c} 1 & 1 \\ 1 & 1 \\ b & 2 \end{array} \right),</equation>二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=\boldsymbol{x}^{\mathrm{T}} \boldsymbol{B} \boldsymbol{A} \boldsymbol{x},</equation>已知方程组<equation>A\boldsymbol{x}=\boldsymbol{0}</equation>的解均是<equation>B^{\mathrm{T}} \boldsymbol{x}=\boldsymbol{0}</equation>的解，但两个方程组不同解.

I. 求 a,b的值；

II. 求正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>，将<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>化为标准形.

**答案:**(1)<equation>a=1,b=2</equation>(2)<equation>f=\boldsymbol{x}^{\mathrm{T}}\boldsymbol{C}\boldsymbol{x}^{x=Qy}=6\boldsymbol{y}_{3}^{2}</equation>

**解析:**解（I）（法一）由于A有2阶非零子式，且A为<equation>2 \times3</equation>矩阵，故<equation>r ( A )=2, A x=0</equation>的基础解系中有3-2=1个解向量.又因为<equation>A x=0</equation>的解均是<equation>B^{\mathrm{T}} x=0</equation>的解，但这两个方程组不同解，所以<equation>B^{\mathrm{T}} x=0</equation>的基础解系中至少有两个解向量，从而<equation>r ( B^{\mathrm{T}} )\leqslant 3-2=1.</equation>结合B为非零矩阵可知<equation>r ( B^{\mathrm{T}} )=r ( B )\geqslant 1</equation>，于是<equation>r ( B^{\mathrm{T}} )=1.</equation>由于<equation>\boldsymbol {B} ^ {\mathrm {T}} = \left( \begin{array}{c c c} 1 & 1 & b \\ 1 & 1 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 2 \\ 0 & 0 & b - 2 \end{array} \right),</equation>故由<equation>r(\mathbf{B}^{\mathrm{T}}) = 1</equation>可得<equation>b = 2</equation>设<equation>( x_{1}, x_{2}, x_{3} )^{\mathrm{T}}</equation>为<equation>A x=0</equation>的解，令<equation>x_{3}=1</equation>可得<equation>(-1,-a,1)^{\mathrm{T}}</equation>为<equation>A x=0</equation>的一个基础解系.将其代入<equation>B^{\mathrm{T}} x=0</equation>即<equation>x_{1}+x_{2}+2 x_{3}=0</equation>可得，<equation>-1-a+2=0</equation>，解得 a=1.

因此，<equation>a=1,b=2.</equation>（法二）由于方程组<equation>Ax = 0</equation>的解均是<equation>B^{\mathrm{T}}x = 0</equation>的解，故方程组<equation>\binom{A}{B^{\mathrm{T}}}x = 0</equation>与<equation>Ax = 0</equation>同解（见注）.由此可得<equation>r\left( \begin{array}{c} A \\ B^{\mathrm{T}} \end{array} \right) = r(A)</equation>.又因为A有2阶非零子式，且A为<equation>2\times 3</equation>矩阵，所以<equation>r(A) = 2</equation>，从而<equation>r\left( \begin{array}{c} A \\ B^{\mathrm{T}} \end{array} \right) = 2.</equation>对<equation>\left( \begin{array}{c}A\\ B^{\mathrm{T}} \end{array} \right)</equation>作初等行变换.<equation>\binom {A} {B ^ {\mathrm {T}}} = \left( \begin{array}{c c c} 0 & 1 & a \\ 1 & 0 & 1 \\ 1 & 1 & b \\ 1 & 1 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 2 \\ 1 & 1 & b \\ 0 & 1 & a \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 1 & b - 1 \\ 0 & 1 & a \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & b - 2 \\ 0 & 0 & a - 1 \end{array} \right).</equation>由于<equation>r \binom{A}{B^{\mathrm{T}}} = 2</equation>，故<equation>a - 1 = 0, b - 2 = 0</equation>，即<equation>a = 1, b = 2</equation>（Ⅱ）由第（I）问可得<equation>A = \left( \begin{array}{lll}0 & 1 & 1\\ 1 & 0 & 1 \end{array} \right),B = \left( \begin{array}{ll}1 & 1\\ 1 & 1\\ 2 & 2 \end{array} \right)</equation>，则<equation>BA = \left( \begin{array}{lll}1 & 1 & 2\\ 1 & 1 & 2\\ 2 & 2 & 4 \end{array} \right).</equation>由于BA是一个实对称矩阵，且秩为1，迹为6，故BA相似于秩为1，迹为6的对角矩阵，特征值为6，0，0.

分别计算 BA的属于特征值6和0的特征向量.

考虑（6E-BA）x=0.<equation>\begin{array}{l} 6 E - B A = \left( \begin{array}{c c c} 5 & - 1 & - 2 \\ - 1 & 5 & - 2 \\ - 2 & - 2 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & - 5 & 2 \\ - 2 & - 2 & 2 \\ 5 & - 1 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & - 5 & 2 \\ 0 & - 1 2 & 6 \\ 0 & 2 4 & - 1 2 \end{array} \right) \\ \rightarrow \left(\begin{array}{c c c}1&- 5&2\\0&1&- \frac {1}{2}\\0&0&0\end{array}\right)\rightarrow \left(\begin{array}{c c c}1&0&- \frac {1}{2}\\0&1&- \frac {1}{2}\\0&0&0\end{array}\right). \\ \end{array}</equation><equation>\xi_{1} = \left( \begin{array}{l}1\\ 1\\ 2 \end{array} \right)</equation>为BA的属于特征值6的一个线性无关的特征向量.

考虑（0E-BA）x=0.<equation>- B A = \left( \begin{array}{c c c} - 1 & - 1 & - 2 \\ - 1 & - 1 & - 2 \\ - 2 & - 2 & - 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 2 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation><equation>\xi_{2} = \left( \begin{array}{c} - 1 \\ 1 \\ 0 \end{array} \right)</equation>和<equation>\xi_{3} = \left( \begin{array}{c} - 2 \\ 0 \\ 1 \end{array} \right)</equation>为BA的属于特征值0的两个线性无关的特征向量.

将<equation>\xi_{1},\xi_{2},\xi_{3}</equation>单位正交.由于<equation>\xi_{2},\xi_{3}</equation>已经与<equation>\xi_{1}</equation>正交，故只需将<equation>\xi_{2},\xi_{3}</equation>正交.<equation>\eta_ {2} = \xi_ {2}</equation><equation>\eta_ {3} = \xi_ {3} - \frac {\left(\eta_ {2} , \xi_ {3}\right)}{\left(\eta_ {2} , \eta_ {2}\right)} \eta_ {2} = \left( \begin{array}{c} - 2 \\ 0 \\ 1 \end{array} \right) - \left( \begin{array}{c} - 1 \\ 1 \\ 0 \end{array} \right) = \left( \begin{array}{c} - 1 \\ - 1 \\ 1 \end{array} \right).</equation>令<equation>\varepsilon_ {1} = \frac {\xi_ {1}}{\| \xi_ {1} \|} = \frac {1}{\sqrt {6}} \binom {1} {2}, \quad \varepsilon_ {2} = \frac {\eta_ {2}}{\| \eta_ {2} \|} = \frac {1}{\sqrt {2}} \binom {- 1} {1}, \quad \varepsilon_ {3} = \frac {\eta_ {3}}{\| \eta_ {3} \|} = \frac {1}{\sqrt {3}} \binom {- 1} {- 1},</equation>则<equation>Q=(\varepsilon_{1},\varepsilon_{2},\varepsilon_{3})=\left( \begin{array}{c c c} \frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{6}} & \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{3}} \\ \frac{2}{\sqrt{6}} & 0 & \frac{1}{\sqrt{3}} \end{array} \right)</equation>为正交矩阵，正交变换<equation>x=Qy</equation>将<equation>f(x_{1},x_{2},x_{3})</equation>化为标准形<equation>6 y _ {1} ^ {2}.</equation>

---

**2023年第9题 | 选择题 | 5分 | 答案: B**

9. 二次型<equation>f \left(x_{1}, x_{2}, x_{3}\right)=\left(x_{1}+x_{2}\right)^{2}+\left(x_{1}+x_{3}\right)^{2}-4\left(x_{2}-x_{3}\right)^{2}</equation>的规范形为（    )

A.<equation>y_{1}^{2}+y_{2}^{2}</equation>B.<equation>y_{1}^{2}-y_{2}^{2}</equation>C.<equation>y_{1}^{2}+y_{2}^{2}-4y_{3}^{2}</equation>D.<equation>y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>

答案: B

**解析:**解 （法一）将<equation>f ( x_{1}, x_{2}, x_{3} )</equation>展开可得<equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = 2 x _ {1} ^ {2} - 3 x _ {2} ^ {2} - 3 x _ {3} ^ {2} + 2 x _ {1} x _ {2} + 2 x _ {1} x _ {3} + 8 x _ {2} x _ {3}.</equation>该二次型对应的矩阵为<equation>A=\left( \begin{array}{c c c} 2 & 1 & 1 \\ 1 & -3 & 4 \\ 1 & 4 & -3 \end{array} \right).</equation>计算可得<equation>| A | = \left| \begin{array}{c c c} 2 & 1 & 1 \\ 1 & - 3 & 4 \\ 1 & 4 & - 3 \end{array} \right| \xlongequal {r _ {2} + r _ {3}} \left| \begin{array}{c c c} 2 & 1 & 1 \\ 2 & 1 & 1 \\ 1 & 4 & - 3 \end{array} \right| = 0.</equation>由于<equation>| A|=0</equation>，故 A有零特征值，从而<equation>r(A)\leqslant 2</equation>，f的正、负惯性指数之和不超过2.

若 f的负惯性指数为0，则f非负，即对任意<equation>\left(x_{1},x_{2},x_{3}\right)</equation>，均有<equation>f\left(x_{1},x_{2},x_{3}\right)\geqslant 0</equation>.但是，<equation>f(0,0,1)=0+1-4=-3<0</equation>，矛盾.同理，若 f的正惯性指数为0，则f非正，即对任意<equation>\left(x_{1},x_{2},x_{3}\right)</equation>，均有<equation>f\left(x_{1},x_{2},x_{3}\right)\leqslant 0</equation>.但是，<equation>f(1,0,0)=1+1-0=2>0</equation>，矛盾.

由于 f的正、负惯性指数之和不超过2，而正、负惯性指数又均大于0，故其正、负惯性指数均为 1. 应选B.<equation>(\mathrm {法 二}) \mathrm {记} \left\{ \begin{array}{l l l} y _ {1} = x _ {1} + x _ {2}, \\ y _ {2} = x _ {1} + x _ {3}, \\ y _ {3} = x _ {2} - x _ {3}, \end{array} \right. P = \left( \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & - 1 \end{array} \right), \mathrm {则} \left( \begin{array}{l} y _ {1} \\ y _ {2} \\ y _ {3} \end{array} \right) = P \left( \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right).</equation>记<equation>\boldsymbol{\Lambda}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & - 4 \end{array} \right)</equation>，则由<equation>f \left( x_{1}, x_{2}, x_{3}\right) = \left(x_{1} + x_{2}\right)^{2}+\left(x_{1} + x_{3}\right)^{2}-4\left(x_{2}-x_{3}\right)^{2}</equation>可知，<equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = y ^ {\mathrm {T}} \Lambda y \xlongequal {y = P x} x ^ {\mathrm {T}} P ^ {\mathrm {T}} \Lambda P x.</equation>于是，<equation>A=P^{\mathrm{T}}\Lambda P</equation>为二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>对应的对称矩阵.

又因为<equation>| P | = \left| \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & - 1 \end{array} \right| = 0</equation>，所以<equation>| A | = 0</equation>，从而A有零特征值.

（法三）令<equation>\left\{\begin{array}{l l}y_{1}=x_{1}+x_{2},\\ y_{2}=x_{1}+x_{3},\\ y_{3}=x_{3},\end{array} \right.</equation>则<equation>x_{2}-x_{3}=y_{1}-y_{2}</equation>，且该变换为可逆线性变换.在该变换下，二次型<equation>f \left(x_{1}, x_{2}, x_{3}\right)</equation>化为

其余同法一.<equation>\begin{aligned} g \left(y _ {1}, y _ {2}, y _ {3}\right) &= y _ {1} ^ {2} + y _ {2} ^ {2} - 4 \left(y _ {1} - y _ {2}\right) ^ {2} = - 3 y _ {1} ^ {2} - 3 y _ {2} ^ {2} + 8 y _ {1} y _ {2} \\ &= - 3 y _ {1} ^ {2} + 3 \cdot \frac {8}{3} y _ {1} y _ {2} - 3 y _ {2} ^ {2} = - 3 \left(y _ {1} - \frac {4}{3} y _ {2}\right) ^ {2} - 3 y _ {2} ^ {2} + \frac {1 6}{3} y _ {2} ^ {2} \\ &= - 3 \left(y _ {1} - \frac {4}{3} y _ {2}\right) ^ {2} + \frac {7}{3} y _ {2} ^ {2}. \end{aligned}</equation>再令<equation>\left\{ \begin{array}{l l} z_{1}=y_{1}-\frac{4}{3} y_{2}, \\ z_{2}=y_{2}, \\ z_{3}=y_{3}, \end{array} \right.</equation>该变换为可逆线性变换.在该变换下，二次型<equation>g \left( y_{1}, y_{2}, y_{3} \right)</equation>化为<equation>h \left(z _ {1}, z _ {2}, z _ {3}\right) = - 3 z _ {1} ^ {2} + \frac {7}{3} z _ {2} ^ {2}.</equation>因此，<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>的一个标准形为<equation>- 3 z_{1}^{2}+\frac{7}{3} z_{2}^{2}</equation>其正、负惯性指数均为1.应选B.

---

**2022年第22题 | 解答题 | 12分**

22. (本题满分12分)

已知二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=3 x_{1}^{2}+4 x_{2}^{2}+3 x_{3}^{2}+2 x_{1} x_{3}</equation>.

I. 求正交矩阵 Q，使正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>将二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>化为标准形；

II. 证明<equation>\min_{x\neq 0} \frac{f(x)}{x^{\mathrm{T}}x}=2.</equation>

**答案:**（I）<equation>Q=\left( \begin{array}{c c c} {\frac{1}{\sqrt{2}}} & {0} & {-\frac{1}{\sqrt{2}}} \\ {0} & {1} & {0} \\ {\frac{1}{\sqrt{2}}} & {0} & {\frac{1}{\sqrt{2}}} \end{array} \right)</equation>正交变换<equation>x=Qy</equation>将二次型f化为标准形<equation>4y_{1}^{2}+4y_{2}^{2}+2y_{3}^{2}</equation>；

（Ⅱ）证明略.

**解析:**解（I）由 f的表达式可得 f对应的矩阵 A =<equation>\left( \begin{array}{c c c} 3 & 0 & 1 \\ 0 & 4 & 0 \\ 1 & 0 & 3 \end{array} \right).</equation>计算 A的特征多项式.<equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda - 3 & 0 & - 1 \\ 0 & \lambda - 4 & 0 \\ - 1 & 0 & \lambda - 3 \end{array} \right| = (\lambda - 4) \left[ (\lambda - 3) ^ {2} - 1 \right] = (\lambda - 4) ^ {2} (\lambda - 2).</equation>A的特征值为4,4,2.

分别计算 A的属于特征值4和2的特征向量.

考虑（4E-A）x=0.<equation>4 E - A = \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 0 & 0 \\ - 1 & 0 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation><equation>\boldsymbol{\xi}_{1}=\left( \begin{array}{c}1\\ 0\\ 1 \end{array} \right)</equation>和<equation>\boldsymbol{\xi}_{2}=\left( \begin{array}{c}0\\ 1\\ 0 \end{array} \right)</equation>为 A的属于特征值4的两个线性无关的特征向量考虑<equation>( 2 E-A ) x=0.</equation><equation>2 E - A = \left( \begin{array}{c c c} - 1 & 0 & - 1 \\ 0 & - 2 & 0 \\ - 1 & 0 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation><equation>\xi_{3}=\left( \begin{array}{c}-1\\ 0\\ 1 \end{array} \right)</equation>为 A的属于特征值2的一个特征向量.

由于<equation>\xi_{1},\xi_{2},\xi_{3}</equation>相互正交，故只需将它们各自单位化即可得一组相互正交的单位特征向量.<equation>\boldsymbol {\varepsilon} _ {1} = \frac {\boldsymbol {\xi} _ {1}}{\| \boldsymbol {\xi} _ {1} \|} = \frac {1}{\sqrt {2}} \left( \begin{array}{c} 1 \\ 0 \\ 1 \end{array} \right), \quad \boldsymbol {\varepsilon} _ {2} = \frac {\boldsymbol {\xi} _ {2}}{\| \boldsymbol {\xi} _ {2} \|} = \left( \begin{array}{c} 0 \\ 1 \\ 0 \end{array} \right), \quad \boldsymbol {\varepsilon} _ {3} = \frac {\boldsymbol {\xi} _ {3}}{\| \boldsymbol {\xi} _ {3} \|} = \frac {1}{\sqrt {2}} \left( \begin{array}{c} - 1 \\ 0 \\ 1 \end{array} \right).</equation>令<equation>Q=(\varepsilon_{1},\varepsilon_{2},\varepsilon_{3})</equation>，可得<equation>Q^{-1}AQ=Q^{\mathrm{T}}AQ=\left( \begin{array}{c c c} 4 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>，即正交变换<equation>x=Qy</equation>将二次型f化为标准形<equation>4y_{1}^{2}+4y_{2}^{2}+2y_{3}^{2}.</equation>（Ⅱ）由第（I）问可知，在正交变换<equation>x=Q y</equation>下，<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>的标准形为<equation>4 y_{1}^{2}+4 y_{2}^{2}+2 y_{3}^{2}.</equation>又因为<equation>\boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {x} = \left(Q \boldsymbol {y}\right) ^ {\mathrm {T}} Q \boldsymbol {y} = \boldsymbol {y} ^ {\mathrm {T}} Q ^ {\mathrm {T}} Q \boldsymbol {y} \xlongequal {Q ^ {\mathrm {T}} Q = E} \boldsymbol {y} ^ {\mathrm {T}} \boldsymbol {y} = y _ {1} ^ {2} + y _ {2} ^ {2} + y _ {3} ^ {2},</equation>所以对<equation>x\neq 0</equation><equation>\frac {f (\boldsymbol {x})}{\boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {x}} \xlongequal {\boldsymbol {x} = Q \boldsymbol {y}} \frac {4 y _ {1} ^ {2} + 4 y _ {2} ^ {2} + 2 y _ {3} ^ {2}}{y _ {1} ^ {2} + y _ {2} ^ {2} + y _ {3} ^ {2}} \geqslant \frac {2 y _ {1} ^ {2} + 2 y _ {2} ^ {2} + 2 y _ {3} ^ {2}}{y _ {1} ^ {2} + y _ {2} ^ {2} + y _ {3} ^ {2}} = 2.</equation>取<equation>y_{0}</equation>满足<equation>y_{1}=y_{2}=0,y_{3}\neq 0,x_{0}=Qy_{0}</equation>即<equation>x_{0}=y_{3}\varepsilon_{3}</equation>时，可得<equation>\frac{f(\boldsymbol{x}_{0})}{\boldsymbol{x}_{0}^{\mathrm{T}}\boldsymbol{x}_{0}}=2.</equation>因此，<equation>\min_{x\neq0}\frac{f(x)}{x^{\mathrm{T}}x}=2.</equation>

---

**2021年第8题 | 选择题 | 5分 | 答案: B**

8. 二次型<equation>f \left(x_{1}, x_{2}, x_{3}\right)=\left(x_{1}+x_{2}\right)^{2}+\left(x_{2}+x_{3}\right)^{2}-\left(x_{3}-x_{1}\right)^{2}</equation>的正惯性指数和负惯性指数分别为（    ）

A. 2,0 B. 1,1 C. 2,1 D. 1,2

答案: B

**解析:**解（法一）令<equation>\left\{ \begin{array}{l l} y_{1}=x_{1}+x_{2}, \\ y_{2}=x_{2}+x_{3}, \\ y_{3}=x_{3}, \end{array} \right.</equation>则<equation>x_{3}-x_{1}=y_{2}-y_{1}</equation>，且该变换为可逆线性变换.在该变换下，二次型<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>化为<equation>g \left(y _ {1}, y _ {2}, y _ {3}\right) = y _ {1} ^ {2} + y _ {2} ^ {2} - \left(y _ {2} - y _ {1}\right) ^ {2} = 2 y _ {1} y _ {2}.</equation>再令<equation>\left\{ \begin{array}{l l} y_{1}=z_{1}+z_{2}, \\ y_{2}=z_{1}-z_{2}, \\ y_{3}=z_{3}, \end{array} \right.</equation>则<equation>g \left( y_{1}, y_{2}, y_{3} \right)</equation>化为<equation>h \left(z _ {1}, z _ {2}, z _ {3}\right) = 2 \left(z _ {1} + z _ {2}\right) \left(z _ {1} - z _ {2}\right) = 2 z _ {1} ^ {2} - 2 z _ {2} ^ {2}.</equation>因此，<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>的一个标准形为<equation>2z_{1}^{2}-2z_{2}^{2}</equation>其正、负惯性指数分别为1，1.应选B.

（法二）将<equation>f(x_{1},x_{2},x_{3})</equation>展开可得<equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = 2 x _ {2} ^ {2} + 2 x _ {1} x _ {2} + 2 x _ {2} x _ {3} + 2 x _ {1} x _ {3}.</equation>该二次型对应的矩阵为<equation>A=\left( \begin{array}{c c c} 0 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 0 \end{array} \right)</equation>. 不难发现，A的第二行为第一行与第三行的和，故<equation>r(A)\leqslant 2</equation>. 又因为A有一个2阶非零子式<equation>\left| \begin{array}{c c} 0 & 1 \\ 1 & 2 \end{array} \right|</equation>，所以<equation>r(A)\geqslant 2</equation>. 于是，<equation>r(A)=2.</equation>由于二次型的正、负惯性指数之和等于其对应矩阵的秩，而选项C、D的两数之和均为3，故可排除选项C、D.

另一方面，若 f的负惯性指数为0，则f非负，即对任意<equation>\left(x_{1},x_{2},x_{3}\right)</equation>，均有<equation>f\left(x_{1},x_{2},x_{3}\right)\geqslant 0.</equation>但是，<equation>f(1,0,-1)=1+1-4<0</equation>矛盾.因此，选项A不正确.

根据排除法，应选B.

---

**2020年第22题 | 解答题 | 11分**

22. （本题满分11分）

2. (本题满分11分)

设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=x_{1}^{2}+x_{2}^{2}+x_{3}^{2}+2 a x_{1} x_{2}+2 a x_{1} x_{3}+2 a x_{2} x_{3}</equation>经可逆线性变换<equation>\left( \begin{array}{c} x_{1} \\ x_{2} \\ x_{3} \end{array} \right)=P \left( \begin{array}{c} y_{1} \\ y_{2} \\ y_{3} \end{array} \right)</equation>化为二次型<equation>g \left( y_{1}, y_{2}, y_{3} \right)=y_{1}^{2}+y_{2}^{2}+4 y_{3}^{2}+2 y_{1} y_{2}</equation>I. 求 a的值；

II. 求可逆矩阵 P.

**答案:**( I )<equation>a=-\frac{1}{2}</equation>;

( II )<equation>P=\left( \begin{array}{c c c} 1 & 2 & \frac{2}{\sqrt{3}} \\ 0 & 1 & \frac{4}{\sqrt{3}} \\ 0 & 1 & 0 \end{array} \right)</equation>，可逆线性变换<equation>\left( \begin{array}{c} x_{1} \\ x_{2} \\ x_{3} \end{array} \right)=P\left( \begin{array}{c} y_{1} \\ y_{2} \\ y_{3} \end{array} \right)</equation>可将二次型<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>化为二次型

**解析:**解（I）<equation>f ( x_{1}, x_{2}, x_{3} )=x_{1}^{2}+x_{2}^{2}+x_{3}^{2}+2 a x_{1} x_{2}+2 a x_{1} x_{3}+2 a x_{2} x_{3}</equation>对应的矩阵<equation>A=\left( \begin{array}{c c c} 1 & a & a \\ a & 1 & a \\ a & a & 1 \end{array} \right),</equation><equation>g ( y_{1}, y_{2}, y_{3} )=y_{1}^{2}+y_{2}^{2}+4 y_{3}^{2}+2 y_{1} y_{2}</equation>对应的矩阵<equation>B=\left( \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 4 \end{array} \right).</equation>易知<equation>r ( B )=2</equation>从而由合同变换不改变矩阵的秩可知<equation>r ( A )=2, | A |=0.</equation><equation>| A | = \left| \begin{array}{l l l} 1 & a & a \\ a & 1 & a \\ a & a & 1 \end{array} \right| = (2 a + 1) \left| \begin{array}{l l l} 1 & a & a \\ 1 & 1 & a \\ 1 & a & 1 \end{array} \right| = (2 a + 1) \left| \begin{array}{l l l} 1 & 0 & 0 \\ 1 & 1 - a & 0 \\ 1 & 0 & 1 - a \end{array} \right| = (2 a + 1) (1 - a) ^ {2}.</equation>由<equation>|A| = 0</equation>可得<equation>a = 1</equation>或<equation>a = -\frac{1}{2}</equation>. 但是当<equation>a = 1</equation>时，<equation>r(A) = 1</equation>，不符合题意，故<equation>a = -\frac{1}{2}</equation>.

将<equation>a=-\frac{1}{2}</equation>代入<equation>f \left(x_{1}, x_{2}, x_{3}\right)</equation>，并将其化为规范形.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= x _ {1} ^ {2} + x _ {2} ^ {2} + x _ {3} ^ {2} - x _ {1} x _ {2} - x _ {1} x _ {3} - x _ {2} x _ {3} \\ &= \left(x _ {1} - \frac {1}{2} x _ {2} - \frac {1}{2} x _ {3}\right) ^ {2} + \frac {3}{4} x _ {2} ^ {2} + \frac {3}{4} x _ {3} ^ {2} - \frac {3}{2} x _ {2} x _ {3} \\ &= \left(x _ {1} - \frac {1}{2} x _ {2} - \frac {1}{2} x _ {3}\right) ^ {2} + \frac {3}{4} \left(x _ {2} - x _ {3}\right) ^ {2}. \end{aligned}</equation>令<equation>\left\{ \begin{array}{l l} z_{1}=x_{1}-\frac{1}{2} x_{2}-\frac{1}{2} x_{3}, \\ z_{2}=\frac{\sqrt{3}}{2}(x_{2}-x_{3}), \\ z_{3}=x_{3}, \end{array} \right.</equation>则可得<equation>z_{1}^{2}+z_{2}^{2}</equation>即<equation>f(x_{1},x_{2},x_{3})</equation>的规范形.<equation>\begin{array}{l} \left(P _ {1} ^ {- 1}, E\right) = \left( \begin{array}{c c c c c c} 1 & - \frac {1}{2} & - \frac {1}{2} & 1 & 0 & 0 \\ 0 & \frac {\sqrt {3}}{2} & - \frac {\sqrt {3}}{2} & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {2} + \frac {\sqrt {3}}{2} r _ {3} ]{r _ {1} + \frac {1}{2} r _ {3}} \left( \begin{array}{c c c c c c} 1 & - \frac {1}{2} & 0 & 1 & 0 & \frac {1}{2} \\ 0 & \frac {\sqrt {3}}{2} & 0 & 0 & 1 & \frac {\sqrt {3}}{2} \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} \times \frac {2}{\sqrt {3}}} \left( \begin{array}{c c c c c c} 1 & - \frac {1}{2} & 0 & 1 & 0 & \frac {1}{2} \\ 0 & 1 & 0 & 0 & \frac {2}{\sqrt {3}} & 1 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {1} ^ {*} + \frac {1}{2} r _ {2} ^ {* *}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 1 & \frac {1}{\sqrt {3}} & 1 \\ 0 & 1 & 0 & 0 & \frac {2}{\sqrt {3}} & 1 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

于是，<equation>P_{1}=\left( \begin{array}{c c c} 1 & \frac{1}{\sqrt{3}} & 1 \\ 0 & \frac{2}{\sqrt{3}} & 1 \\ 0 & 0 & 1 \end{array} \right), P_{1}^{\mathrm{T}} A P_{1}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>再将<equation>g(y_{1},y_{2},y_{3})</equation>化为规范形.<equation>g(y_{1},y_{2},y_{3})=y_{1}^{2}+y_{2}^{2}+4y_{3}^{2}+2y_{1}y_{2}=(y_{1}+y_{2})^{2}+4y_{3}^{2}.</equation>令<equation>\left\{ \begin{array}{l l l} z_{1}=y_{1}+y_{2}, \\ z_{2}=2y_{3}, \\ z_{3}=y_{2}, \end{array} \right.</equation>则<equation>\left( \begin{array}{l} z_{1} \\ z_{2} \\ z_{3} \end{array} \right)=\left( \begin{array}{l l l} 1 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 1 & 0 \end{array} \right)\left( \begin{array}{l} y_{1} \\ y_{2} \\ y_{3} \end{array} \right).</equation>记<equation>P_{2}^{-1}=\left( \begin{array}{l l l} 1 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 1 & 0 \end{array} \right),</equation>则<equation>\left( \begin{array}{l} z_{1} \\ z_{2} \\ z_{3} \end{array} \right)=P_{2}^{-1}\left( \begin{array}{l} y_{1} \\ y_{2} \\ y_{3} \end{array} \right),</equation>且<equation>P_{2}^{\mathrm{T}} B P_{2}=\left( \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>记<equation>\Lambda=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>由于<equation>P_{1}^{\mathrm{T}} A P_{1}=\Lambda, P_{2}^{\mathrm{T}} B P_{2}=\Lambda,</equation>故<equation>\boldsymbol{B}=(P_{2}^{\mathrm{T}})^{-1}\boldsymbol{\Lambda}P_{2}^{-1}\frac{(P_{2}^{\mathrm{T}})^{-1}=(P_{2}^{-1})^{\mathrm{T}}}{(P_{2}^{-1})^{\mathrm{T}}P_{1}^{\mathrm{T}} A P_{1} P_{2}^{-1}}.</equation>因此，<equation>P=P_{1} P_{2}^{-1}=\left( \begin{array}{c c c} 1 & \frac{1}{\sqrt{3}} & 1 \\ 0 & \frac{2}{\sqrt{3}} & 1 \\ 0 & 0 & 1 \end{array} \right)\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 1 & 0 \end{array} \right)=\left( \begin{array}{c c c} 1 & 2 & \frac{2}{\sqrt{3}} \\ 0 & 1 & \frac{4}{\sqrt{3}} \\ 0 & 1 & 0 \end{array} \right).</equation><equation>\left( \begin{array}{l} x_{1} \\ x_{2} \end{array} \right)=P\left( \begin{array}{l} y_{1} \\ y_{2} \end{array} \right)</equation>可将二次型<equation>f(x_{1},x_{2},x_{3})</equation>化为二次型<equation>g(y_{1},y_{2},y_{3}).</equation><equation>\binom{x_1}{x_2} = P\binom{y_1}{y_2}</equation>可将二次型<equation>f ( x_{1}, x_{2}, x_{3} )</equation>化为二次型<equation>g ( y_{1}, y_{2}, y_{3} ).</equation>（法二）对A做合同变换，将其化为B.<equation>\begin{aligned} A &= \left( \begin{array}{c c c} 1 & - \frac {1}{2} & - \frac {1}{2} \\ - \frac {1}{2} & 1 & - \frac {1}{2} \\ - \frac {1}{2} & - \frac {1}{2} & 1  \right) \xrightarrow {\mathrm {行 变换}} \frac {1}{r _ {3} - r _ {2}} \left( \begin{array}{c c c} 1 & - \frac {1}{2} & - \frac {1}{2} \\ - \frac {1}{2} & 1 & - \frac {1}{2} \\ 0 & - \frac {3}{2} & \frac {3}{2}  \right) \xrightarrow {\mathrm {列 变换}} \frac {1}{c _ {3} - c _ {2}} \left( \begin{array}{c c c} 1 & - \frac {1}{2} & 0 \\ - \frac {1}{2} & 1 & - \frac {3}{2} \\ 0 & - \frac {3}{2} & 3  \right) \\ \xrightarrow {\mathrm {行 变换}} \frac {1}{r _ {2} + \frac {1}{2} r _ {3}} \left( \begin{array}{c c c} 1 & - \frac {1}{2} & 0 \\ - \frac {1}{2} & \frac {1}{4} & 0 \\ 0 & - \frac {3}{2} & 3  \right) \xrightarrow {\mathrm {列 变换}} \frac {1}{c _ {2} + \frac {1}{2} c _ {3}} \left( \begin{array}{c c c} 1 & - \frac {1}{2} & 0 \\ - \frac {1}{2} & \frac {1}{4} & 0 \\ 0 & 0 & 3  \right) \\ \xrightarrow {\mathrm {行 变换}} \frac {1}{r _ {2} + \frac {3}{2} r _ {1}} \left( \begin{array}{c c c} 1 & - \frac {1}{2} & 0 \\ 1 & - \frac {1}{2} & 0 \\ 0 & 0 & 3  \right) \xrightarrow {\mathrm {列 变换}} \frac {1}{c _ {2} + \frac {3}{2} c _ {1}} \left( \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 3  \right) \\ \xrightarrow {\mathrm {行 变换}} \frac {1}{r _ {3} \times \frac {2}{\sqrt {3}}} \left( \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 2 \sqrt {3}  \right) \xrightarrow {\mathrm {列 变换}} \frac {1}{c _ {3} \times \frac {2}{\sqrt {3}}} \left( \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 4  \right) &= B. \end{aligned}</equation>记录每一次初等列变换所对应的初等矩阵，分别记为<equation>P_{1}, P_{2}, P_{3}, P_{4}</equation><equation>\begin{aligned} P _ {1} &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & - 1 \\ 0 & 0 & 1  \right), \quad P _ {2} &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & \frac {1}{2} & 1  \right), \quad P _ {3} &= \left( \begin{array}{c c c} 1 & \frac {3}{2} & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1  \right), \quad P _ {4} &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & \frac {2}{\sqrt {3}}  \right). \\ P &= P _ {1} P _ {2} P _ {3} P _ {4} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & - 1 \\ 0 & 0 & 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & \frac {1}{2} & 1  \right) \left( \begin{array}{c c c} 1 & \frac {3}{2} & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & \frac {2}{\sqrt {3}}  \right) \\ &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & \frac {1}{2} & - 1 \\ 0 & \frac {1}{2} & 1  \right) \left( \begin{array}{c c c} 1 & \frac {3}{2} & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & \frac {2}{\sqrt {3}}  \right) \\ &= \left( \begin{array}{c c c} 1 & \frac {3}{2} & 0 \\ 0 & \frac {1}{2} & - 1 \\ 0 & \frac {1}{2} & 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & \frac {2}{\sqrt {3}}  \right) &= \left( \begin{array}{c c c} 1 & \frac {3}{2} & 0 \\ 0 & \frac {1}{2} & - \frac {2}{\sqrt {3}} \\ 0 & \frac {1}{2} & \frac {2}{\sqrt {3}}  \right). \end{aligned}</equation>因此，<equation>P^{\mathrm{T}} A P=B</equation>，即<equation>\left( \begin{array}{c}x_{1}\\ x_{2}\\ x_{3}\end{array} \right)=P\left( \begin{array}{c}y_{1}\\ y_{2}\\ y_{3} \end{array} \right)</equation>可将二次型<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>化为二次型<equation>g\left(y_{1},y_{2},y_{3}\right).</equation>

---

**2019年第8题 | 选择题 | 4分 | 答案: C**

8. 设 A是3阶实对称矩阵，E是3阶单位矩阵.若<equation>A^{2}+A=2 E</equation>，且<equation>|A|=4</equation>，则二次型<equation>x^{\mathrm{T}} A x</equation>的规范形为（    )

A.<equation>y_{1}^{2}+y_{2}^{2}+y_{3}^{2}</equation>B.<equation>y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>C.<equation>y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>D.<equation>-y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>

答案: C

**解析:**设<equation>\lambda</equation>为 A的一个特征值，<equation>\alpha</equation>为属于特征值<equation>\lambda</equation>的特征向量.

由<equation>A^{2}+A=2 E</equation>可得<equation>(\lambda^{2}+\lambda-2)\alpha=0</equation>. 由于<equation>\alpha</equation>为非零向量，故<equation>\lambda^{2}+\lambda-2=0</equation>. 解得<equation>\lambda=1</equation>或<equation>\lambda=-2</equation>. A的特征值只能取1和-2.

又因为<equation>| A |=4</equation>，所以 A的特征值应为-2，-2，1. 因此，二次型<equation>x^{\mathrm{T}} A x</equation>的正惯性指数为1，负惯性指数为2. 四个选项中，只有<equation>y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>满足该性质. 应选C.

