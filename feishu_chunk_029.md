II. 求<equation>A</equation>的列向量组的一个极大线性无关组<equation>\alpha, \beta</equation>，并求矩阵<equation>H</equation>，使得<equation>A = GH</equation>，其中<equation>G = (\alpha ,\beta)</equation>

**答案:**（ I ）<equation>a=1;</equation>（Ⅱ）<equation>A</equation>的前两列<equation>\alpha=\left( \begin{array}{c}1\\ -1\\ 1 \end{array} \right),\beta=\left( \begin{array}{c}-1\\ 0\\ 1 \end{array} \right)</equation>构成A的列向量组的一个极大线性无关组.令<equation>H=</equation><equation>\left( \begin{array}{c c c c}1&0&2&1&1\\ 0&1&-1&1&2 \end{array} \right)</equation>，则<equation>A=GH</equation>，其中<equation>G=(\alpha ,\beta).</equation>

**解析:**解（I）对矩阵A做初等行变换.<equation>\begin{array}{l} A = \left( \begin{array}{c c c c c} 1 & - 1 & 3 & 0 & - 1 \\ - 1 & 0 & - 2 & - a & - 1 \\ 1 & 1 & a & 2 & 3 \end{array} \right) \xrightarrow [ r _ {3} - r _ {1} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c c} 1 & - 1 & 3 & 0 & - 1 \\ 0 & - 1 & 1 & - a & - 2 \\ 0 & 2 & a - 3 & 2 & 4 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c} 1 & - 1 & 3 & 0 & - 1 \\ 0 & - 1 & 1 & - a & - 2 \\ 0 & 0 & a - 1 & 2 - 2 a & 0 \end{array} \right). \\ \end{array}</equation>由上式可得，当且仅当<equation>a = 1</equation>时，<equation>r(A) = 2.</equation>因此，<equation>a = 1</equation>（Ⅱ）由第（I）问可知，<equation>A=\left( \begin{array}{c c c c c} 1 & -1 & 3 & 0 & -1 \\ -1 & 0 & -2 & -1 & -1 \\ 1 & 1 & 1 & 2 & 3 \end{array} \right).</equation>由于<equation>r(A)=2</equation>，故A的列秩为2又因为A的第一列与第二列线性无关，所以A的第一列与第二列构成A的列向量组的一个极大线性无关组，其余列向量均可由该极大线性无关组线性表示.

由第（Ⅰ）问的计算可得<equation>A \rightarrow \left(\begin{array}{c c c c c}1&- 1&3&0&- 1\\0&- 1&1&- 1&- 2\\0&0&0&0&0\end{array}\right)\rightarrow \left(\begin{array}{c c c c c}1&0&2&1&1\\0&1&- 1&1&2\\0&0&0&0&0\end{array}\right).</equation>记矩阵<equation>A = (\alpha ,\beta ,\gamma_1,\gamma_2,\gamma_3) = (A_1,A_2)</equation>，其中<equation>A_{1}</equation>为<equation>A</equation>的前两列<equation>(\alpha ,\beta),A_{2}</equation>为<equation>A</equation>的后三列<equation>(\gamma_{1},\gamma_{2},\gamma_{3})</equation>，则<equation>A</equation>为矩阵方程<equation>A_{1}X = A_{2}</equation>的增广矩阵.由（1）式可得<equation>\gamma_ {1} = 2 \alpha - \beta , \quad \gamma_ {2} = \alpha + \beta , \quad \gamma_ {3} = \alpha + 2 \beta .</equation>于是，<equation>A = \left(\alpha , \beta , \gamma_ {1}, \gamma_ {2}, \gamma_ {3}\right) = \left(\alpha , \beta\right) \left( \begin{array}{c c c c c} 1 & 0 & 2 & 1 & 1 \\ 0 & 1 & - 1 & 1 & 2 \end{array} \right).</equation>令<equation>H = \left( \begin{array}{c c c c c} 1 & 0 & 2 & 1 & 1 \\ 0 & 1 & -1 & 1 & 2 \end{array} \right)</equation>，则<equation>A = GH</equation>，其中<equation>G = (\alpha ,\beta)</equation>.

---

**2023年第7题 | 选择题 | 5分 | 答案: D**

7. 已知向量<equation>\alpha_{1}=\left( \begin{array}{c}1\\ 2\\ 3 \end{array} \right),\alpha_{2}=\left( \begin{array}{c}2\\ 1\\ 1 \end{array} \right),\beta_{1}=\left( \begin{array}{c}2\\ 5\\ 9 \end{array} \right),\beta_{2}=\left( \begin{array}{c}1\\ 0\\ 1 \end{array} \right)</equation>若<equation>\gamma</equation>既可由<equation>\alpha_{1},\alpha_{2}</equation>线性表示，也可由<equation>\beta_{1},\beta_{2}</equation>线性表示，则<equation>\gamma=(\quad)</equation>A. k<equation>\left( \begin{array}{c}3\\ 3\\ 4 \end{array} \right),k \in \mathbf{R}</equation>B. k<equation>\left( \begin{array}{c}3\\ 5\\ 10 \end{array} \right),k \in \mathbf{R}</equation>C. k<equation>\left( \begin{array}{c}-1\\ 1\\ 2 \end{array} \right),k \in \mathbf{R}</equation>D. k<equation>\left( \begin{array}{c}1\\ 5\\ 8 \end{array} \right),k \in \mathbf{R}</equation>

答案: D

**解析:**解 由于<equation>\boldsymbol{\gamma}</equation>既可由<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2}</equation>线性表示，也可由<equation>\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2}</equation>线性表示，故存在<equation>k_{1},k_{2},l_{1},l_{2}</equation>，使得<equation>\boldsymbol{\gamma}=k_{1}\boldsymbol{\alpha}_{1}</equation><equation>+ k_{2}\boldsymbol{\alpha}_{2}=l_{1}\boldsymbol{\beta}_{1}+l_{2}\boldsymbol{\beta}_{2}</equation>.于是，<equation>\left(k_{1},-l_{1},k_{2},-l_{2}\right)^{\mathrm{T}}</equation>是齐次线性方程组<equation>\left(\boldsymbol{\alpha}_{1},\boldsymbol{\beta}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\beta}_{2}\right)\boldsymbol{x}=\mathbf{0}</equation>的解.

记<equation>A=(\alpha_{1},\beta_{1},\alpha_{2},\beta_{2})</equation>，对A作初等行变换.<equation>\begin{array}{l} \boldsymbol {A} = \left( \begin{array}{c c c c} 1 & 2 & 2 & 1 \\ 2 & 5 & 1 & 0 \\ 3 & 9 & 1 & 1 \end{array} \right) \xrightarrow {r _ {2} - 2 r _ {1}} \frac {r _ {2} - 2 r _ {1}}{r _ {3} - 3 r _ {1}} \left( \begin{array}{c c c c} 1 & 2 & 2 & 1 \\ 0 & 1 & - 3 & - 2 \\ 0 & 3 & - 5 & - 2 \end{array} \right) \xrightarrow {r _ {1} - 2 r _ {2} ^ {*}} \left( \begin{array}{c c c c} 1 & 0 & 8 & 5 \\ 0 & 1 & - 3 & - 2 \\ 0 & 0 & 4 & 4 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {* *} \times \frac {1}{4}} \left( \begin{array}{c c c c} 1 & 0 & 8 & 5 \\ 0 & 1 & - 3 & - 2 \\ 0 & 0 & 1 & 1 \end{array} \right) \xrightarrow {r _ {1} ^ {*} - 8 r _ {3} ^ {* * *}} \left( \begin{array}{c c c c} 1 & 0 & 0 & - 3 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 \end{array} \right). \\ \end{array}</equation>（<equation>r_{t}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

取<equation>x_{4}=1</equation>，可得<equation>\boldsymbol{\xi}=(3,-1,-1,1)^{\mathrm{T}}</equation>为该方程组的一个基础解系，从而<equation>(k_{1},-l_{1},k_{2},-l_{2})^{\mathrm{T}}= k(3,-1,-1,1)^{\mathrm{T}}</equation>，其中 k<equation>\in\mathbf{R}.</equation>因此，<equation>\boldsymbol {\gamma} = k _ {1} \boldsymbol {\alpha} _ {1} + k _ {2} \boldsymbol {\alpha} _ {2} = 3 k \binom {1} {2} - k \binom {2} {1} = k \binom {1} {5}, \quad k \in \mathbf {R}.</equation>应选 D.

---

**2022年第7题 | 选择题 | 5分 | 答案: C**

7. 设<equation>\alpha_{1}=(\lambda,1,1)^{\mathrm{T}},\alpha_{2}=(1,\lambda,1)^{\mathrm{T}},\alpha_{3}=(1,1,\lambda)^{\mathrm{T}},\alpha_{4}=(1,\lambda,\lambda^{2})^{\mathrm{T}}</equation>. 若<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>等价，则<equation>\lambda</equation>的取值范围是（    )

A.<equation>\{0,1\}</equation>B.<equation>\{\lambda \mid \lambda \in \mathbf{R},\lambda \neq -2\}</equation>C.<equation>\{\lambda \mid \lambda \in \mathbf{R},\lambda \neq -1,\lambda \neq -2\}</equation>D.<equation>\{\lambda \mid \lambda \in \mathbf{R},\lambda \neq -1\}</equation>

答案: C

**解析:**解（法一）当<equation>\lambda=1</equation>时，<equation>\alpha_{1}=\alpha_{2}=\alpha_{3}=\alpha_{4}=\left( \begin{array}{c}1\\ 1\\ 1 \end{array} \right)</equation>.此时<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>显然等价当<equation>\lambda\neq1</equation>时，考虑矩阵<equation>A=(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4})</equation><equation>\begin{array}{l} A = \left( \begin{array}{c c c c} \lambda & 1 & 1 & 1 \\ 1 & \lambda & 1 & \lambda \\ 1 & 1 & \lambda & \lambda^ {2} \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 1 & 1 & \lambda & \lambda^ {2} \\ \lambda & 1 & 1 & 1 \end{array} \right) \xrightarrow {r _ {2} - r _ {1}} \frac {r _ {2} - r _ {1}}{r _ {3} - \lambda r _ {1}} \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 0 & 1 - \lambda & \lambda - 1 & \lambda^ {2} - \lambda \\ 0 & 1 - \lambda^ {2} & 1 - \lambda & 1 - \lambda^ {2} \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} \times \frac {1}{1 - \lambda}} \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 0 & 1 & - 1 & - \lambda \\ 0 & 1 + \lambda & 1 & 1 + \lambda \end{array} \right) \xrightarrow {r _ {3} ^ {* *} - (1 + \lambda) r _ {2} ^ {* *}} \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 0 & 1 & - 1 & - \lambda \\ 0 & 0 & \lambda + 2 & (\lambda + 1) ^ {2} \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

由于 A有2阶非零子式<equation>\left| \begin{array}{cc} \lambda & 1 \\ 1 & \lambda \end{array} \right|</equation>，故<equation>r(A)\geqslant 2</equation>另一方面，因为不存在<equation>\lambda</equation>满足<equation>\lambda +2=(\lambda+1)^{2}=</equation>0，所以<equation>r(A)=3.</equation><equation>r(\alpha_{1},\alpha_{2},\alpha_{3})=3</equation>当且仅当<equation>\lambda\neq-2.</equation><equation>r(\alpha_{1},\alpha_{2},\alpha_{4})=3</equation>当且仅当<equation>\lambda\neq-1.</equation>因此，当<equation>\lambda\neq1</equation>时，<equation>r(A)=r(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4})=r(\alpha_{1},\alpha_{2},\alpha_{3})=r(\alpha_{1},\alpha_{2},\alpha_{4})</equation>当且仅当<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1.</equation>注意到<equation>\lambda=1</equation>也包含在条件<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1</equation>中，故<equation>r(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4})=r(\alpha_{1},\alpha_{2},\alpha_{3})= r(\alpha_{1},\alpha_{2},\alpha_{4})</equation>当且仅当<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1.</equation>综上所述，应选C.

（法二）分别计算<equation>|\alpha_{1},\alpha_{2},\alpha_{3}|</equation>，<equation>|\alpha_{1},\alpha_{2},\alpha_{4}|</equation><equation>\left| \alpha_ {1}, \alpha_ {2}, \alpha_ {3} \right| = \left| \begin{array}{c c c} \lambda & 1 & 1 \\ 1 & \lambda & 1 \\ 1 & 1 & \lambda \end{array} \right| = \left| \begin{array}{c c c} \lambda & 1 - \lambda & 1 - \lambda^ {2} \\ 1 & \lambda - 1 & 1 - \lambda \\ 1 & 0 & 0 \end{array} \right| = (1 - \lambda) ^ {2} (\lambda + 2).</equation><equation>\left| \alpha_ {1}, \alpha_ {2}, \alpha_ {4} \right| = \left| \begin{array}{c c c} \lambda & 1 & 1 \\ 1 & \lambda & \lambda \\ 1 & 1 & \lambda^ {2} \end{array} \right| = \left| \begin{array}{c c c} \lambda & 1 - \lambda & 1 - \lambda^ {3} \\ 1 & \lambda - 1 & \lambda - \lambda^ {2} \\ 1 & 0 & 0 \end{array} \right| = (1 - \lambda) ^ {2} (1 + \lambda) ^ {2}.</equation>当<equation>\lambda\neq1,-2,-1</equation>时，<equation>|\alpha_{1},\alpha_{2},\alpha_{3}|</equation>与<equation>|\alpha_{1},\alpha_{2},\alpha_{4}|</equation>均不为0.此时，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>和<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>均为3维列向量组的极大无关组，从而等价.

当<equation>\lambda=1</equation>时，<equation>\alpha_{1}=\alpha_{2}=\alpha_{3}=\alpha_{4}=\left( \begin{array}{c}1\\ 1\\ 1 \end{array} \right).</equation>此时<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>显然等价.

当<equation>\lambda=-2</equation>或<equation>\lambda=-1</equation>时，<equation>|\alpha_{1},\alpha_{2},\alpha_{3}| \neq |\alpha_{1},\alpha_{2},\alpha_{4}|</equation>，且其中一个为0，另一个不为0，说明两向量组的秩不相等，从而不等价.

综上所述，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>等价当且仅当<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1.</equation>应选C.

---

**2019年第20题 | 解答题 | 11分**

20. (本题满分11分)<equation>\text {已 知 向 量 组 I}: \alpha_ {1} = \left( \begin{array}{c} 1 \\ 1 \\ 4 \end{array} \right), \alpha_ {2} = \left( \begin{array}{c} 1 \\ 0 \\ 4 \end{array} \right), \alpha_ {3} = \left( \begin{array}{c} 1 \\ 2 \\ a ^ {2} + 3 \end{array} \right) \text {与 II}: \beta_ {1} = \left( \begin{array}{c} 1 \\ 1 \\ a + 3 \end{array} \right), \beta_ {2} = \left( \begin{array}{c} 0 \\ 2 \\ 1 - a \end{array} \right), \beta_ {3} = \left( \begin{array}{c} 1 \\ 3 \\ a ^ {2} + 3 \end{array} \right).</equation>若向

量组 I 与 II 等价，求<equation>a</equation>的取值，并将<equation>\beta_{3}</equation>用<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性表示.

**答案:**当 a≠-1时，向量组Ⅰ与向量组Ⅱ等价.当 a=1时，<equation>\beta_{3}=(3-2k)\alpha_{1}+(-2+k)\alpha_{2}+ k\alpha_{3}</equation>，其中k为任意常数；当 a≠±1时，<equation>\beta_{3}=\alpha_{1}-\alpha_{2}+\alpha_{3}.</equation>

**解析:**解记<equation>A=(\alpha_{1},\alpha_{2},\alpha_{3}),B=(\beta_{1},\beta_{2},\beta_{3})</equation>，则由向量组Ⅰ与向量组Ⅱ等价可知<equation>r(A)=r(B)</equation><equation>= r(A,B).</equation>对（A,B）作初等行变换.<equation>\begin{array}{l} (A, B) = \left( \begin{array}{c c c c c c} 1 & 1 & 1 & 1 & 0 & 1 \\ 1 & 0 & 2 & 1 & 2 & 3 \\ 4 & 4 & a ^ {2} + 3 & a + 3 & 1 - a & a ^ {2} + 3 \end{array} \right) \\ \xrightarrow {r _ {2} - r _ {1}} \frac {1}{r _ {3} - 4 r _ {1}} \left( \begin{array}{c c c c c c} 1 & 1 & 1 & 1 & 0 & 1 \\ 0 & - 1 & 1 & 0 & 2 & 2 \\ 0 & 0 & a ^ {2} - 1 & a - 1 & 1 - a & a ^ {2} - 1 \end{array} \right). \\ \end{array}</equation>由上式可知<equation>r(A)\geqslant 2</equation>，故<equation>r(A) = 2</equation>或<equation>r(A) = 3.</equation>当<equation>a^{2}-1=0</equation>时，<equation>a=1</equation>或<equation>a=-1</equation><equation>r(A)=2</equation>.又由于当<equation>a=-1</equation>时，<equation>r(A,B)=3</equation>，故<equation>a=-1</equation>不符合题意，而当<equation>a=1</equation>时，<equation>r(A)=r(B)=r(A,B)=2</equation>，此时向量组 I与向量组Ⅱ等价.

当 a = 1时，<equation>\left(A, \boldsymbol {\beta} _ {3}\right)\rightarrow \left(\begin{array}{c c c c}1&1&1&1\\0&- 1&1&2\\0&0&0&0\end{array}\right) \xrightarrow {r _ {2} \times (- 1)} \left(\begin{array}{c c c c}1&1&1&1\\0&1&- 1&- 2\\0&0&0&0\end{array}\right) \xrightarrow {r _ {1} - r _ {2} ^ {*}} \left(\begin{array}{c c c c}1&0&2&3\\0&1&- 1&- 2\\0&0&0&0\end{array}\right).</equation>取<equation>x_{3}</equation>为自由变元，令<equation>x_{3}=1</equation>，可得<equation>(-2,1,1)^{\mathrm{T}}</equation>为<equation>A x=0</equation>的一个基础解系.又因为<equation>(3,-2,0)^{\mathrm{T}}</equation>为<equation>A x=\beta_{3}</equation>的一个特解，所以<equation>A x=\beta_{3}</equation>的通解为<equation>k(-2,1,1)^{\mathrm{T}}+(3,-2,0)^{\mathrm{T}}</equation>其中k为任意常数因此，<equation>\boldsymbol {\beta} _ {3} = (3 - 2 k) \boldsymbol {\alpha} _ {1} + (- 2 + k) \boldsymbol {\alpha} _ {2} + k \boldsymbol {\alpha} _ {3},</equation>其中 k为任意常数.

当 a<equation>\neq\pm1</equation>时，<equation>a^{2}-1\neq0,r(A)=r(B)=r(A,B)=3</equation>，向量组Ⅰ与向量组Ⅱ等价，且它们相互之间的线性表示唯一.<equation>\left(A, \boldsymbol {\beta} _ {3}\right)\rightarrow \left(\begin{array}{c c c c}1&1&1&1\\0&- 1&1&2\\0&0&1&1\end{array}\right) \xrightarrow [ r _ {1} - r _ {2} ^ {*} ]{r _ {2} \times (- 1)} \left(\begin{array}{c c c c}1&0&2&3\\0&1&- 1&- 2\\0&0&1&1\end{array}\right) \xrightarrow [ r _ {2} ^ {*} + r _ {3} ]{r _ {1} ^ {*} - 2 r _ {3}} \left(\begin{array}{c c c c}1&0&0&1\\0&1&0&- 1\\0&0&1&1\end{array}\right).</equation>因此，<equation>A x=\beta_{3}</equation>的唯一解为<equation>(1,-1,1)^{\mathrm{T}}.</equation><equation>\boldsymbol {\beta} _ {3} = \boldsymbol {\alpha} _ {1} - \boldsymbol {\alpha} _ {2} + \boldsymbol {\alpha} _ {3}.</equation>综上所述，当<equation>a\neq -1</equation>时，向量组 I与向量组Ⅱ等价。当<equation>a = 1</equation>时，<equation>\beta_{3} = (3 - 2k)\alpha_{1} + (-2 + k)\alpha_{2}</equation><equation>+ k\alpha_{3}</equation>，其中<equation>k</equation>为任意常数；当<equation>a\neq \pm 1</equation>时，<equation>\beta_{3} = \alpha_{1} - \alpha_{2} + \alpha_{3}</equation>.

---

**2013年第5题 | 选择题 | 4分 | 答案: B**

5. 设 A,B,C均为 n阶矩阵. 若 AB=C，且 B可逆，则（    ）

A. 矩阵 C的行向量组与矩阵 A的行向量组等价

B. 矩阵 C的列向量组与矩阵 A的列向量组等价

C. 矩阵 C的行向量组与矩阵 B的行向量组等价

D. 矩阵 C的列向量组与矩阵 B的列向量组等价

答案: B

**解析:**我们证明 C的列向量组与 A的列向量组能相互线性表示.

不妨设<equation>A = \left(\alpha_{1},\alpha_{2},\dots ,\alpha_{n}\right),C = \left(\gamma_{1},\gamma_{2},\dots ,\gamma_{n}\right),B = \left(b_{ij}\right)_{n\times n}</equation>，则<equation>\boldsymbol {A B} = \left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\alpha} _ {2}, \dots , \boldsymbol {\alpha} _ {n}\right) \left(b _ {i j}\right) _ {n \times n} = \boldsymbol {C} = \left(\boldsymbol {\gamma} _ {1}, \boldsymbol {\gamma} _ {2}, \dots , \boldsymbol {\gamma} _ {n}\right),</equation><equation>\left\{ \begin{array}{l} \boldsymbol {\gamma} _ {1} = b _ {1 1} \boldsymbol {\alpha} _ {1} + b _ {2 1} \boldsymbol {\alpha} _ {2} + \dots + b _ {n 1} \boldsymbol {\alpha} _ {n}, \\ \boldsymbol {\gamma} _ {2} = b _ {1 2} \boldsymbol {\alpha} _ {1} + b _ {2 2} \boldsymbol {\alpha} _ {2} + \dots + b _ {n 2} \boldsymbol {\alpha} _ {n}, \\ \dots , \\ \boldsymbol {\gamma} _ {n} = b _ {1 n} \boldsymbol {\alpha} _ {1} + b _ {2 n} \boldsymbol {\alpha} _ {2} + \dots + b _ {n n} \boldsymbol {\alpha} _ {n}. \end{array} \right.</equation>因此，C的列向量组<equation>\left( \gamma_{1},\gamma_{2},\dots,\gamma_{n}\right)</equation>能由A的列向量组<equation>\left( \alpha_{1},\alpha_{2},\dots,\alpha_{n}\right)</equation>线性表示。同理，由于B可逆，故A的列向量组也能由C的列向量组线性表示.应选B.

下面我们说明选项 A、C、D不正确.

选项A：令<equation>A=\left( \begin{array}{cc}1&1\\ 0&0 \end{array} \right), B=\left( \begin{array}{cc}1&1\\ 0&1 \end{array} \right)</equation>，则<equation>C=AB=\left( \begin{array}{cc}1&2\\ 0&0 \end{array} \right).</equation>但A的行向量组<equation>\{(1,1),(0,0)\}</equation>与C的行向量组<equation>\{(1,2),(0,0)\}</equation>不等价.

选项C、D：取B为单位矩阵E，C为一个非满秩矩阵.于是 A=C. B的行（列）向量组线性无关， C的行（列）向量组线性相关，因此不等价.

---

**2011年第20题 | 解答题 | 11分**


设向量组<equation>\alpha_{1}=(1,0,1)^{\mathrm{T}},\alpha_{2}=(0,1,1)^{\mathrm{T}},\alpha_{3}=(1,3,5)^{\mathrm{T}}</equation>不能由向量组<equation>\beta_{1}=(1,1,1)^{\mathrm{T}},\beta_{2}=(1,2,3)^{\mathrm{T}},\beta_{3}=(3,4,a)^{\mathrm{T}}</equation>线性表示.

I. 求 a的值；

II. 将<equation>\beta_{1},\beta_{2},\beta_{3}</equation>用<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性表示.

**答案:**(20) （I）<equation>a=5;</equation>（Ⅱ）<equation>\boldsymbol{\beta}_{1}=2\boldsymbol{\alpha}_{1}+4\boldsymbol{\alpha}_{2}-\boldsymbol{\alpha}_{3},\boldsymbol{\beta}_{2}=\boldsymbol{\alpha}_{1}+2\boldsymbol{\alpha}_{2},\boldsymbol{\beta}_{3}=5\boldsymbol{\alpha}_{1}+10\boldsymbol{\alpha}_{2}-2\boldsymbol{\alpha}_{3}.</equation>

**解析:**解（I）记<equation>A=(\alpha_{1},\alpha_{2},\alpha_{3})</equation><equation>B=(\beta_{1},\beta_{2},\beta_{3})</equation><equation>A,B</equation>的列向量组分别记为<equation>A,B.</equation>首先，<equation>|A| = \left| \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 1 & 1 & 5 \end{array} \right| = 1</equation>，故<equation>r(A) = 3</equation>，A满秩.

由于向量组 B不能线性表示 A，故<equation>r(\mathbf{B})<3</equation>；否则 B也满秩，从而 B能线性表示 A，矛盾.

由于<equation>r(\boldsymbol{B}) < 3</equation>，故<equation>| \boldsymbol {B} | = \left| \begin{array}{c c c} 1 & 1 & 3 \\ 1 & 2 & 4 \\ 1 & 3 & a \end{array} \right| \frac {c _ {2} - c _ {1}}{c _ {3} - 3 c _ {1}} \left| \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 1 \\ 1 & 2 & a - 3 \end{array} \right| = a - 5 = 0.</equation>因此，<equation>a = 5</equation>（Ⅱ）（法一）求B用A的线性表示的系数，相当于求<equation>A X=B</equation>的解. X的列向量的坐标为线性表示的系数，即<equation>\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)\left(x_{1i},x_{2i},x_{3i}\right)^{\mathrm{T}}=\boldsymbol{\beta}_{i}(i=1,2,3).</equation><equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {B}) = \left( \begin{array}{c c c c c c} 1 & 0 & 1 & 1 & 1 & 3 \\ 0 & 1 & 3 & 1 & 2 & 4 \\ 1 & 1 & 5 & 1 & 3 & 5 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c c c c} 1 & 0 & 1 & 1 & 1 & 3 \\ 0 & 1 & 3 & 1 & 2 & 4 \\ 0 & 1 & 4 & 0 & 2 & 2 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {*} - r _ {2}} \left( \begin{array}{c c c c c c} 1 & 0 & 1 & 1 & 1 & 3 \\ 0 & 1 & 3 & 1 & 2 & 4 \\ 0 & 0 & 1 & - 1 & 0 & - 2 \end{array} \right) \xrightarrow {r _ {1} - r _ {3} ^ {* *}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 2 & 1 & 5 \\ 0 & 1 & 0 & 4 & 2 & 1 0 \\ 0 & 0 & 1 & - 1 & 0 & - 2 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每做一次初等行变换，加一个*.）

因此，<equation>Ax = \beta_{1}</equation>的解为<equation>(2,4,-1)^{\mathrm{T}},\beta_{1} = 2\alpha_{1} + 4\alpha_{2} - \alpha_{3};Ax = \beta_{2}</equation>的解为<equation>(1,2,0)^{\mathrm{T}},\beta_{2} = \alpha_{1} + 2\alpha_{2};Ax = \beta_{3}</equation>的解为<equation>(5,10,-2)^{\mathrm{T}},\beta_{3} = 5\alpha_{1} + 10\alpha_{2} - 2\alpha_{3}.</equation>（法二）用克拉默法则分别求<equation>A x=\beta_{1},</equation><equation>A x=\beta_{2},</equation><equation>A x=\beta_{3}</equation>的解. x的分量为线性表示的系数，即<equation>\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)\left(x_{1},x_{2},x_{3}\right)^{\mathrm{T}}=\beta_{i}(i=1,2,3).</equation>首先，根据第（I）问可得<equation>|A| = 1.</equation>由克拉默法则知，<equation>Ax = \beta_{1}</equation>的解为<equation>x _ {1} = \left| \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 3 \\ 1 & 1 & 5 \end{array} \right| = 2, \quad x _ {2} = \left| \begin{array}{c c c} 1 & 1 & 1 \\ 0 & 1 & 3 \\ 1 & 1 & 5 \end{array} \right| = 4, \quad x _ {3} = \left| \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 1 \end{array} \right| = - 1.</equation>因此，<equation>\pmb{\beta}_{1} = 2\pmb{\alpha}_{1} + 4\pmb{\alpha}_{2} - \pmb{\alpha}_{3}</equation>. 同理可得<equation>\pmb{\beta}_{2} = \pmb{\alpha}_{1} + 2\pmb{\alpha}_{2}, \pmb{\beta}_{3} = 5\pmb{\alpha}_{1} + 10\pmb{\alpha}_{2} - 2\pmb{\alpha}_{3}</equation>.

---

**2010年第5题 | 选择题 | 4分 | 答案: A**

5. 设向量组 I:<equation>\alpha_{1},\alpha_{2},\cdots,\alpha_{r}</equation>可由向量组 II:<equation>\beta_{1},\beta_{2},\cdots,\beta_{s}</equation>线性表示.下列命题正确的是（    ）

A. 若向量组 I 线性无关，则<equation>r\leqslant s</equation>B. 若向量组 I 线性相关，则<equation>r>s</equation>C. 若向量组 II 线性无关，则<equation>r\leqslant s</equation>D. 若向量组 II 线性相关，则<equation>r>s</equation>

答案: A

**解析:**解 由于向量组 I 能被向量组Ⅱ线性表示，故<equation>r_{\mathrm{I}} \leqslant r_{\mathrm{II}}</equation>.又由题设，有<equation>r_{\mathrm{I}} \leqslant r, r_{\mathrm{II}} \leqslant s.</equation>若向量组 I 线性无关，则<equation>r_{\mathrm{I}}=r</equation>，从而有<equation>r = r _ {\mathrm {I}} \leqslant r _ {\mathrm {I I}} \leqslant s,</equation>即<equation>r\leqslant s.</equation>应选A.

下面我们说明选项B、C、D不正确.

考虑 I = {<equation>\left( \begin{array}{c} 1 \\ 0 \end{array} \right), \left( \begin{array}{c} 2 \\ 0 \end{array} \right)</equation>，Ⅱ = {<equation>\left( \begin{array}{c} 1 \\ 0 \end{array} \right), \left( \begin{array}{c} 0 \\ 1 \end{array} \right), \left( \begin{array}{c} 2 \\ 0 \end{array} \right)</equation>}.Ⅱ能表示 I，且向量组 I，Ⅱ均线性相关，但 2 = r < s = 3.选项B、D不正确.

考虑 I =<equation>\left\{\begin{array}{l l}1\\0\end{array}\right.,\left(\begin{array}{l}2\\0\end{array}\right.,\left(\begin{array}{l}3\\0\end{array}\right)</equation>，Ⅱ<equation>= \left\{\begin{array}{l l}1\\0\end{array}\right.,\left(\begin{array}{l}0\\1\end{array}\right)</equation>.Ⅱ能表示Ⅰ，且向量组Ⅱ线性无关，但<equation>3=r></equation>s=2.选项C不正确.

---


#### 向量组的线性相关性

**2014年第6题 | 选择题 | 4分 | 答案: A**

6. 设<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>均为3维向量，则对任意常数 k,l，向量组<equation>\alpha_{1}+k\alpha_{3},\alpha_{2}+l\alpha_{3}</equation>线性无关是向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关的（    ）

A. 必要非充分条件 B. 充分非必要条件

C. 充分必要条件 D. 既非充分也非必要条件

答案: A

**解析:**解<equation>(\alpha_{1} + k\alpha_{3},\alpha_{2} + l\alpha_{3}) = (\alpha_{1},\alpha_{2},\alpha_{3})\left( \begin{array}{c c}1 & 0\\ 0 & 1\\ k & l \end{array} \right).</equation>若向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关，则<equation>r \left(\left(\boldsymbol {\alpha} _ {1} + k \boldsymbol {\alpha} _ {3}, \boldsymbol {\alpha} _ {2} + l \boldsymbol {\alpha} _ {3}\right)\right) = r \left(\left( \begin{array}{c c} 1 & 0 \\ 0 & 1 \\ k & l \end{array} \right)\right) = 2.</equation>因此，<equation>\alpha_{1} + k\alpha_{3},\alpha_{2} + l\alpha_{3}</equation>线性无关.

令<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2}</equation>为线性无关的两个向量，<equation>\boldsymbol{\alpha}_{3}=\mathbf{0}</equation>，则对任意常数 k，l，向量组<equation>\boldsymbol{\alpha}_{1}+k\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{2}+l\boldsymbol{\alpha}_{3}</equation>线性无关，但向量组<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性相关.

综上所述，对任意常数 k，l，向量组<equation>\boldsymbol{\alpha}_{1}+k\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{2}+l\boldsymbol{\alpha}_{3}</equation>线性无关是向量组<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性无关的必要非充分条件.应选A.

---

**2012年第5题 | 选择题 | 4分 | 答案: C**

5. 设<equation>\alpha_{1}=\left( \begin{array}{c}0\\ 0\\ c_{1}\end{array} \right),\alpha_{2}=\left( \begin{array}{c}0\\ 1\\ c_{2}\end{array} \right),\alpha_{3}=\left( \begin{array}{c}1\\ -1\\ c_{3}\end{array} \right),\alpha_{4}=\left( \begin{array}{c}-1\\ 1\\ c_{4}\end{array} \right),</equation>其中<equation>c_{1},c_{2},c_{3},c_{4}</equation>为任意常数，则下列向量组线性相关

为（    ）

A.<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>B.<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>C.<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>D.<equation>\alpha_{2},\alpha_{3},\alpha_{4}</equation>

答案: C

**解析:**解（法一）由题设可得，<equation>\boldsymbol{\alpha}_{3}+\boldsymbol{\alpha}_{4}=\left( \begin{array}{c}0\\ 0\\ c_{3}+c_{4} \end{array} \right)</equation><equation>\boldsymbol{\alpha}_{1}=\left( \begin{array}{c}0\\ 0\\ c_{1} \end{array} \right).</equation>当<equation>c_{3} + c_{4}\neq 0</equation>时，<equation>\alpha_{1} = \frac{c_{1}}{c_{3} + c_{4}} \left(\alpha_{3} + \alpha_{4}\right)</equation>，<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>线性相关；当<equation>c_{3} + c_{4} = 0</equation>时，<equation>\alpha_{3} + \alpha_{4} = 0</equation>，<equation>\alpha_{3},\alpha_{4}</equation>线性相关.从而<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>线性相关.

综上所述，<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}</equation>线性相关，应选C.

（法二）由于<equation>n</equation>个<equation>n</equation>维列向量<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{n}</equation>线性相关等价于<equation>|\alpha_{1},\alpha_{2},\dots ,\alpha_{n}| = 0</equation>，而<equation>\left| \alpha_ {1}, \alpha_ {3}, \alpha_ {4} \right| = \left| \begin{array}{c c c} 0 & 1 & - 1 \\ 0 & - 1 & 1 \\ c _ {1} & c _ {3} & c _ {4} \end{array} \right| = c _ {1} \left| \begin{array}{c c} 1 & - 1 \\ - 1 & 1 \end{array} \right| = 0,</equation>故<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}</equation>线性相关.应选C.

同理可计算其他选项中的3个向量组成的矩阵的行列式，可知它们均不恒为零.

---

**2009年第20题 | 解答题 | 11分**

20. (本题满分11分)<equation>\text {设} \boldsymbol {A} = \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ - 1 & 1 & 1 \\ 0 & - 4 & - 2 \end{array} \right), \boldsymbol {\xi} _ {1} = \left( \begin{array}{c} - 1 \\ 1 \\ - 2 \end{array} \right).</equation>I. 求满足<equation>A\xi_{2}=\xi_{1}, A^{2}\xi_{3}=\xi_{1}</equation>的所有向量<equation>\xi_{2},\xi_{3}</equation>；

II. 对第一问中的任意向量<equation>\xi_{2},\xi_{3}</equation>，证明<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

**答案:**（20）（I）满足<equation>A\xi_{2}=\xi_{1}</equation>的所有向量为<equation>\xi_{2}=k_{1}(1,-1,2)^{\mathrm{T}}+(0,0,1)^{\mathrm{T}}</equation>，其中<equation>k_{1}</equation>为任意常数；满足<equation>A^{2}\xi_{3}=\xi_{1}</equation>的所有向量<equation>\xi_{3}=k_{2}(1,-1,0)^{\mathrm{T}}+k_{3}(0,0,1)^{\mathrm{T}}+\left(-\frac{1}{2},0,0\right)^{\mathrm{T}}</equation>，其中<equation>k_{2},k_{3}</equation>为任意常数.

（Ⅱ）证明略.

**解析:**解（I）解<equation>A x=\xi_{1}</equation>，这是一个非齐次线性方程组.<equation>\left(\boldsymbol {A}, \boldsymbol {\xi} _ {1}\right) = \left( \begin{array}{c c c c} 1 & - 1 & - 1 & - 1 \\ - 1 & 1 & 1 & 1 \\ 0 & - 4 & - 2 & - 2 \end{array} \right) \xrightarrow [ r _ {2} ^ {*} \leftrightarrow r _ {3} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c} 1 & - 1 & - 1 & - 1 \\ 0 & - 4 & - 2 & - 2 \\ 0 & 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {1} + r _ {2} ^ {* * *} ]{r _ {2} ^ {* *} \times \left(- \frac {1}{2}\right)} \left( \begin{array}{c c c c} 1 & 1 & 0 & 0 \\ 0 & 2 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{array} \right).</equation>(<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每做一次初等行变换，加一个*.）

于是<equation>r(A) = r(A, \xi_1) = 2.Ax = \xi_1</equation>有无穷多解.其对应的齐次方程组等价于<equation>\left\{ \begin{array}{l}x_{1} + x_{2} = 0,\\ 2x_{2} + x_{3} = 0, \end{array} \right.</equation>故可取<equation>(1, - 1, 2)^{\mathrm{T}}</equation>为该方程组的一个基础解系.另外，<equation>\left\{ \begin{array}{l}x_{1} + x_{2} = 0,\\ 2x_{2} + x_{3} = 1 \end{array} \right.</equation>的一个特解为<equation>(0,0,1)^{\mathrm{T}}.</equation>因此，<equation>Ax = \xi_{1}</equation>的通解为<equation>\xi_{2} = k_{1}(1, -1, 2)^{\mathrm{T}} + (0, 0, 1)^{\mathrm{T}}</equation>，其中<equation>k_{1}</equation>为任意常数.<equation>\left(\boldsymbol {A} ^ {2}, \boldsymbol {\xi} _ {1}\right) = \left( \begin{array}{c c c c} 2 & 2 & 0 & - 1 \\ - 2 & - 2 & 0 & 1 \\ 4 & 4 & 0 & - 2 \end{array} \right) \xrightarrow [ r _ {3} - 2 r _ {1} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c} 2 & 2 & 0 & - 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{array} \right).</equation>于是<equation>r(A^{2}) = r(A^{2},\xi_{1}) = 1.A^{2}x = \xi_{1}</equation>有无穷多解.其对应的齐次方程组等价于<equation>2(x_{1} + x_{2}) = 0</equation>，故可取<equation>(1, - 1,0)^{\mathrm{T}}</equation>和<equation>(0,0,1)^{\mathrm{T}}</equation>为该方程组的一个基础解系.另外，<equation>2(x_{1} + x_{2}) = -1</equation>的一个特解为<equation>\left(-\frac{1}{2},0;0\right)^{\mathrm{T}}.</equation>因此，<equation>A^{2}x = \xi_{1}</equation>的通解为<equation>\xi_{3} = k_{2}(1, - 1,0)^{\mathrm{T}} + k_{3}(0,0,1)^{\mathrm{T}} + \left(-\frac{1}{2},0,0\right)^{\mathrm{T}}</equation>，其中<equation>k_{2},k_{3}</equation>为任意常数.

（Ⅱ）（法一）通过计算可知，<equation>\boldsymbol {A} \boldsymbol {\xi} _ {1} = \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ - 1 & 1 & 1 \\ 0 & - 4 & - 2 \end{array} \right) \left( \begin{array}{c} - 1 \\ 1 \\ - 2 \end{array} \right) = \left( \begin{array}{c} 0 \\ 0 \\ 0 \end{array} \right).</equation>从而<equation>A^{3}\xi_{3} = A^{2}\xi_{2} = A\xi_{1} = 0.</equation>我们可以利用该性质推出<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

不妨设<equation>a\boldsymbol{\xi}_1 + b\boldsymbol{\xi}_2 + c\boldsymbol{\xi}_3 = \mathbf{0}</equation>. 该等式两端同时左乘<equation>A^2</equation><equation>a A ^ {2} \xi_ {1} + b A ^ {2} \xi_ {2} + c A ^ {2} \xi_ {3} = c A ^ {2} \xi_ {3} = c \xi_ {1} = 0.</equation>由于<equation>\boldsymbol{\xi}_{1}</equation>为非零向量，故<equation>c=0.</equation>于是<equation>a\boldsymbol{\xi}_{1}+b\boldsymbol{\xi}_{2}=\mathbf{0}.</equation>再在<equation>a\boldsymbol{\xi}_{1}+b\boldsymbol{\xi}_{2}=\mathbf{0}</equation>两端同时左乘 A，得<equation>aA\boldsymbol{\xi}_{1}+bA\boldsymbol{\xi}_{2}=bA\boldsymbol{\xi}_{2}=b\boldsymbol{\xi}_{1}=\mathbf{0}.</equation>同理得<equation>b = 0</equation>. 由于<equation>b = c = 0</equation>，故<equation>a\boldsymbol{\xi}_1 = \mathbf{0}</equation>. 从而<equation>a = 0</equation>.

因此，<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

（法二）由第（I）问，我们知道了<equation>\xi_{1},\xi_{2},\xi_{3}</equation>的表达式，从而我们可以通过计算行列式<equation>|\xi_{1},\xi_{2},\xi_{3}|</equation>来说明<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.<equation>\begin{array}{l} \left| \xi_ {1}, \xi_ {2}, \xi_ {3} \right| = \left| \begin{array}{c c c} - 1 & k _ {1} & k _ {2} - \frac {1}{2} \\ 1 & - k _ {1} & - k _ {2} \\ - 2 & 2 k _ {1} + 1 & k _ {3} \end{array} \right| \xlongequal {r _ {1} + r _ {2}} \left| \begin{array}{c c c} 0 & 0 & - \frac {1}{2} \\ 1 & - k _ {1} & - k _ {2} \\ - 2 & 2 k _ {1} + 1 & k _ {3} \end{array} \right| \\ \underline {{\underline {{\text {按 第一 行 展开}}}}} \left(- \frac {1}{2}\right) \left| \begin{array}{c c} 1 & - k _ {1} \\ - 2 & 2 k _ {1} + 1 \end{array} \right| = - \frac {1}{2} \neq 0. \\ \end{array}</equation>因此，<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

---


### 矩阵


#### 矩阵的运算与变换

**2024年第6题 | 选择题 | 5分 | 答案: C**

6. 设 A为3阶矩阵，<equation>P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right)</equation>，若<equation>P^{\mathrm{T}} A P^{2}=\left( \begin{array}{c c c} a+2 c & 0 & c \\ 0 & b & 0 \\ 2 c & 0 & c \end{array} \right)</equation>，则 A=（    )

A.<equation>\left( \begin{array}{c c c} c & 0 & 0 \\ 0 & a & 0 \\ 0 & 0 & b \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c} b & 0 & 0 \\ 0 & c & 0 \\ 0 & 0 & a \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c} a & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & c \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} c & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & a \end{array} \right)</equation>

答案: C

**解析:**）由于<equation>P = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right)</equation>，故<equation>\boldsymbol {P} ^ {- 1} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ - 1 & 0 & 1 \end{array} \right), \quad \boldsymbol {P} ^ {\mathrm {T}} = \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right), \quad \left(\boldsymbol {P} ^ {\mathrm {T}}\right) ^ {- 1} = \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>进一步可得，<equation>\begin{aligned} \boldsymbol {A} &= \left(\boldsymbol {P} ^ {\mathrm {T}}\right) ^ {- 1} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} ^ {2} \left(\boldsymbol {P} ^ {2}\right) ^ {- 1} = \left(\boldsymbol {P} ^ {\mathrm {T}}\right) ^ {- 1} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} ^ {2} \left(\boldsymbol {P} ^ {- 1}\right) ^ {2} \\ &= \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1  \right) \left( \begin{array}{c c c} a + 2 c & 0 & c \\ 0 & b & 0 \\ 2 c & 0 & c  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ - 1 & 0 & 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ - 1 & 0 & 1  \right) \\ &= \left( \begin{array}{c c c} a & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & c  \right). \end{aligned}</equation>因此，应选C.

---

**2022年第15题 | 填空题 | 5分**

15. 设 A为3阶矩阵，交换 A的第2行和第3行，再将第2列的-1倍加到第1列，得到矩阵<equation>A^{-1}</equation>的迹<equation>\operatorname{tr}(A^{-1}) =</equation>___

**答案:**-1.

**解析:**解 交换第2行和第3行对应左乘初等矩阵<equation>P_{1}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{array} \right)</equation>，将第2列的-1倍加到第1列对应右乘初等矩阵<equation>P_{2}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>.记<equation>B=\left( \begin{array}{c c c} -2 & 1 & -1 \\ 1 & -1 & 0 \\ -1 & 0 & 0 \end{array} \right)</equation>.于是，<equation>P_{1}AP_{2}=B</equation>，从而<equation>A= P_{1}^{-1}BP_{2}^{-1}</equation>.由此可得，<equation>A^{-1}=P_{2}B^{-1}P_{1}.</equation>下面利用初等行变换计算<equation>B^{-1}.</equation><equation>\begin{array}{l} (B, E) = \left( \begin{array}{c c c c c c} - 2 & 1 & - 1 & 1 & 0 & 0 \\ 1 & - 1 & 0 & 0 & 1 & 0 \\ - 1 & 0 & 0 & 0 & 0 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 0 & 0 & - 1 \\ 1 & - 1 & 0 & 0 & 1 & 0 \\ - 2 & 1 & - 1 & 1 & 0 & 0 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 0 & 0 & - 1 \\ 0 & - 1 & 0 & 0 & 1 & 1 \\ 0 & 1 & - 1 & 1 & 0 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 0 & 0 & - 1 \\ 0 & - 1 & 0 & 0 & 1 & 1 \\ 0 & 0 & - 1 & 1 & 1 & - 1 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 0 & 0 & - 1 \\ 0 & 1 & 0 & 0 & - 1 & - 1 \\ 0 & 0 & 1 & - 1 & - 1 & 1 \end{array} \right). \\ \end{array}</equation>于是，<equation>B^{-1}=\left( \begin{array}{c c c} 0 & 0 & -1 \\ 0 & -1 & -1 \\ -1 & -1 & 1 \end{array} \right).</equation>因此，<equation>\boldsymbol {A} ^ {- 1} = \boldsymbol {P} _ {2} \boldsymbol {B} ^ {- 1} \boldsymbol {P} _ {1} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \left( \begin{array}{c c c} 0 & 0 & - 1 \\ 0 & - 1 & - 1 \\ - 1 & - 1 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{array} \right) = \left( \begin{array}{c c c} 0 & - 1 & 0 \\ 0 & 0 & - 1 \\ - 1 & 1 & - 1 \end{array} \right).</equation>进一步可得<equation>\operatorname{tr}(A^{-1}) = -1.</equation>

---

**2021年第7题 | 选择题 | 5分 | 答案: C**

7. 已知矩阵<equation>A=\left( \begin{array}{c c c}1&0&-1\\ 2&-1&1\\ -1&2&-5 \end{array} \right)</equation>，若存在下三角可逆矩阵 P和上三角可逆矩阵 Q，使 PAQ为对角矩阵，则

P,Q可以分别取（    ）

A.<equation>\begin{array}{l} \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right), \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right) \\ \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right), \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right) \\ \end{array}</equation>C.

B.<equation>\begin{array}{l} \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right), \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \\ \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 3 & 1 \end{array} \right), \left( \begin{array}{c c c} 1 & 2 & - 3 \\ 0 & - 1 & 2 \\ 0 & 0 & 1 \end{array} \right) \\ \end{array}</equation>D.

答案: C

**解析:**解（法一）对（A，E）作初等行变换.<equation>\begin{array}{l} (A, E) = \left( \begin{array}{c c c c c c} 1 & 0 & - 1 & 1 & 0 & 0 \\ 2 & - 1 & 1 & 0 & 1 & 0 \\ - 1 & 2 & - 5 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {2} - 2 r _ {1}} \left( \begin{array}{c c c c c c} 1 & 0 & - 1 & 1 & 0 & 0 \\ 0 & - 1 & 3 & - 2 & 1 & 0 \\ 0 & 2 & - 6 & 1 & 0 & 1 \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} \times (- 1)} \left( \begin{array}{c c c c c c} 1 & 0 & - 1 & 1 & 0 & 0 \\ 0 & 1 & - 3 & 2 & - 1 & 0 \\ 0 & 2 & - 6 & 1 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} ^ {*} - 2 r _ {2} ^ {* *}} \left( \begin{array}{c c c c c c} 1 & 0 & - 1 & 1 & 0 & 0 \\ 0 & 1 & - 3 & 2 & - 1 & 0 \\ 0 & 0 & 0 & - 3 & 2 & 1 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

取<equation>P = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & -1 & 0 \\ -3 & 2 & 1 \end{array} \right).</equation>记<equation>U=\left( \begin{array}{c c c}1&0&-1\\ 0&1&-3\\ 0&0&0 \end{array} \right)</equation>，对<equation>\binom{U}{E}</equation>作初等列变换.<equation>\binom {U} {E} = \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & - 3 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow {c _ {3} + c _ {1} + 3 c _ {2}} \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right).</equation>取<equation>Q = \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right).</equation>此时，PAQ =<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>为对角矩阵.因此，应选C.

（法二）代人法.

观察选项A、B发现，其中各有一个单位矩阵。

由于左乘矩阵相当于对原矩阵作行变换，右乘矩阵相当于对原矩阵作列变换，故<equation>\boldsymbol {A} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 2 & - 1 & 1 \\ - 1 & 2 & - 5 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right)</equation>的第一列为 A的第一列，即<equation>\left( \begin{array}{c}1\\ 2\\ -1 \end{array} \right)</equation><equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right) A = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 2 & - 1 & 1 \\ - 1 & 2 & - 5 \end{array} \right)</equation>的第一行为 A的第一行，即（1，0，-1），而任何矩阵与单位矩阵相乘所得结果均为原矩阵，于是选项A、B所给 P，Q均不能使得 PAQ为对角矩阵。由此可排除选项A、B.

将选项C中的两个矩阵代入计算，可得<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 2 & - 1 & 1 \\ - 1 & 2 & - 5 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 1 & 2 & 0 \end{array} \right) = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>由此可见选项C正确. 应选C.简单计算可验证选项D不正确.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 3 & 1 \end{array} \right) A</equation>的第一行、第二行与A的第一行、第二行相同，即<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 3 & 1 \end{array} \right) A = \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 2 & - 1 & 1 \\ * & * & * \end{array} \right),</equation>记为B.B再右乘<equation>\left( \begin{array}{c c c} 1 & 2 & - 3 \\ 0 & - 1 & 2 \\ 0 & 0 & 1 \end{array} \right),</equation>则新矩阵的第一列为<equation>\left( \begin{array}{c} 1 \\ 2 \\ * \end{array} \right).</equation>于是，所得结果不是对角矩阵.

---

**2015年第20题 | 解答题 | 11分**

20. (本题满分11分)

设矩阵<equation>A=\left( \begin{array}{c c c} a & 1 & 0 \\ 1 & a & -1 \\ 0 & 1 & a \end{array} \right)</equation>，且<equation>A^{3}=O.</equation>I. 求 a的值；

II. 若矩阵<equation>X</equation>满足<equation>X - XA^{2} - AX + AXA^{2} = E</equation>，其中<equation>E</equation>为3阶单位矩阵，求<equation>X</equation>

**答案:**(20) （I）<equation>a=0;</equation><equation>(\mathrm {I I}) \boldsymbol {X} = \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1 \end{array} \right).</equation>

**解析:**解（I）（法一）由<equation>A^{3}=O</equation>知<equation>|A^{3}|=0</equation>又因为<equation>|A^{3}|=|A|^{3}</equation>所以<equation>|A|=0</equation>由题设可计算得<equation>|A|=a^{3}</equation>从而<equation>a^{3}=0</equation>，<equation>a=0.</equation>（法二）设<equation>\lambda</equation>为A的一个特征值，则由<equation>A^{3}=O</equation>可知<equation>\lambda^{3}=0.</equation>于是，A的特征值均为零.由矩阵的迹等于其特征值之和，可知<equation>\operatorname{tr}(A)=3 a=0</equation>即<equation>a=0.</equation>（Ⅱ）由第（I）问知，<equation>A=\left( \begin{array}{c c c} 0 & 1 & 0 \\ 1 & 0 & -1 \\ 0 & 1 & 0 \end{array} \right).</equation>由<equation>X - X A^{2} - A X + A X A^{2} = E</equation>可得，<equation>X \left(E - A ^ {2}\right) - A X \left(E - A ^ {2}\right) = E.</equation>化简得<equation>(E - A)X(E - A^{2}) = E.</equation>由此可知，<equation>E - A, E - A^{2}</equation>均为可逆矩阵，且<equation>\boldsymbol {X} = \left(\boldsymbol {E} - \boldsymbol {A}\right) ^ {- 1} \left(\boldsymbol {E} - \boldsymbol {A} ^ {2}\right) ^ {- 1}.</equation>下面用三种方法计算 X.

（法一）由<equation>(AB)^{-1} = B^{-1}A^{-1}</equation>得，<equation>X = (E - A)^{-1}(E - A^2)^{-1} = [(E - A^2)(E - A)]^{-1}\underline{\underline{A^3 = O}}(E - A - A^2)^{-1}.</equation>计算得<equation>A^{2} = \left( \begin{array}{c c c} 1 & 0 & -1 \\ 0 & 0 & 0 \\ 1 & 0 & -1 \end{array} \right)</equation>，故<equation>E - A - A^{2} = \left( \begin{array}{c c c} 0 & -1 & 1 \\ -1 & 1 & 1 \\ -1 & -1 & 2 \end{array} \right)</equation>，再计算得<equation>|E - A - A^2| = 1.</equation>因此<equation>\boldsymbol {X} = \left(\boldsymbol {E} - \boldsymbol {A} - \boldsymbol {A} ^ {2}\right) ^ {- 1} = \left(\boldsymbol {E} - \boldsymbol {A} - \boldsymbol {A} ^ {2}\right) ^ {*} = \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1 \end{array} \right).</equation>或利用初等变换法计算 X.<equation>\begin{array}{l} \left(\boldsymbol {E} - \boldsymbol {A} - \boldsymbol {A} ^ {2}, \boldsymbol {E}\right) = \left( \begin{array}{c c c c c c} 0 & - 1 & 1 & 1 & 0 & 0 \\ - 1 & 1 & 1 & 0 & 1 & 0 \\ - 1 & - 1 & 2 & 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {3} - r _ {2} ^ {*} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c c c} 0 & - 1 & 1 & 1 & 0 & 0 \\ - 1 & 0 & 2 & 1 & 1 & 0 \\ 0 & - 1 & 0 & - 1 & - 1 & 1 \end{array} \right) \\ \xrightarrow [ r _ {2} ^ {*} - 2 r _ {1} ^ {*} ]{r _ {1} - r _ {3} ^ {*}} \left( \begin{array}{c c c c c c} 0 & 0 & 1 & 2 & 1 & - 1 \\ - 1 & 0 & 0 & - 3 & - 1 & 2 \\ 0 & - 1 & 0 & - 1 & - 1 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 3 & 1 & - 2 \\ 0 & 1 & 0 & 1 & 1 & - 1 \\ 0 & 0 & 1 & 2 & 1 & - 1 \end{array} \right). \\ \end{array}</equation>因此，<equation>\boldsymbol {X} = \left(\boldsymbol {E} - \boldsymbol {A} - \boldsymbol {A} ^ {2}\right) ^ {- 1} = \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1 \end{array} \right).</equation>（法二）由于<equation>A^{3}=O</equation>，故<equation>A^{4}=O</equation>，从而<equation>(E - A)(E + A + A^{2}) = E - A^{3} = E, (E - A^{2})(E + A^{2}) = E - A^{4} = E.</equation>于是，<equation>(E - A)^{-1} = E + A + A^{2}, (E - A^{2})^{-1} = E + A^{2}.</equation>因此，<equation>\begin{aligned} X &= \left(E - A\right) ^ {- 1} \left(E - A ^ {2}\right) ^ {- 1} = \left(E + A + A ^ {2}\right) \left(E + A ^ {2}\right) \xlongequal {A ^ {2} = O} E + A + 2 A ^ {2} \\ &= E + \left( \begin{array}{c c c} 0 & 1 & 0 \\ 1 & 0 & - 1 \\ 0 & 1 & 0  \right) + 2 \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 0 & 0 \\ 1 & 0 & - 1  \right) &= \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1  \right). \end{aligned}</equation>（法三）分别计算<equation>(E - A)^{-1}, (E - A^{2})^{-1}</equation>.<equation>\boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} 1 & - 1 & 0 \\ - 1 & 1 & 1 \\ 0 & - 1 & 1 \end{array} \right), \quad \boldsymbol {E} - \boldsymbol {A} ^ {2} = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 1 & 0 \\ - 1 & 0 & 2 \end{array} \right).</equation>利用初等变换法计算<equation>(E - A)^{-1}, (E - A^{2})^{-1}</equation>.<equation>\begin{array}{l} (E - A, E) = \left( \begin{array}{c c c c c c} 1 & - 1 & 0 & 1 & 0 & 0 \\ - 1 & 1 & 1 & 0 & 1 & 0 \\ 0 & - 1 & 1 & 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {3} - r _ {2} ^ {*} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c c c} 1 & - 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 & 1 & 0 \\ 0 & - 1 & 0 & - 1 & - 1 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} - r _ {3} ^ {*}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 2 & 1 & - 1 \\ 0 & 0 & 1 & 1 & 1 & 0 \\ 0 & - 1 & 0 & - 1 & - 1 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 2 & 1 & - 1 \\ 0 & 1 & 0 & 1 & 1 & - 1 \\ 0 & 0 & 1 & 1 & 1 & 0 \end{array} \right), \\ \end{array}</equation><equation>\begin{array}{l} \left(\boldsymbol {E} - \boldsymbol {A} ^ {2}, \boldsymbol {E}\right) = \left( \begin{array}{c c c c c c} 0 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ - 1 & 0 & 2 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} - 2 r _ {1}} \left( \begin{array}{c c c c c c} 0 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ - 1 & 0 & 0 & - 2 & 0 & 1 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 2 & 0 & - 1 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 1 & 0 & 0 \end{array} \right). \\ \end{array}</equation>因此，<equation>\left(\boldsymbol {E} - \boldsymbol {A}\right) ^ {- 1} = \left( \begin{array}{c c c} 2 & 1 & - 1 \\ 1 & 1 & - 1 \\ 1 & 1 & 0 \end{array} \right), \quad \left(\boldsymbol {E} - \boldsymbol {A} ^ {2}\right) ^ {- 1} = \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{array} \right).</equation>综上所述，<equation>\boldsymbol {X} = \left(\boldsymbol {E} - \boldsymbol {A}\right) ^ {- 1} \left(\boldsymbol {E} - \boldsymbol {A} ^ {2}\right) ^ {- 1} = \left( \begin{array}{c c c} 2 & 1 & - 1 \\ 1 & 1 & - 1 \\ 1 & 1 & 0 \end{array} \right) \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{array} \right) = \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1 \end{array} \right).</equation>

---

**2012年第6题 | 选择题 | 4分 | 答案: B**

6. 设 A为3阶矩阵，P为3阶可逆矩阵，且<equation>P^{-1} A P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>若<equation>P=(\alpha_{1},\alpha_{2},\alpha_{3}), Q=(\alpha_{1}+\alpha_{2},\alpha_{2},\alpha_{3}),</equation>则<equation>Q^{-1} A Q=</equation>(    )

A.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>

答案: B

**解析:**解（法一）由题设知，<equation>Q=P\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，故<equation>Q^{-1}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) P^{-1}</equation>.从而<equation>\begin{aligned} Q ^ {- 1} A Q &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 0 & 0 & 1  \right) P ^ {- 1} A P \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1  \right) \\ &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 0 & 0 & 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1  \right) &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2  \right). \end{aligned}</equation>应选B.

（法二）由题设知，1，1，2是A的特征值，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>分别是属于特征值1，1，2的特征向量，即<equation>A\alpha_{1}=\alpha_{1},</equation><equation>A\alpha_{2}=\alpha_{2},</equation><equation>A\alpha_{3}=2\alpha_{3}.</equation>从而<equation>A\left(\alpha_{1} + \alpha_{2}\right) = \alpha_{1} + \alpha_{2},\alpha_{1} + \alpha_{2}</equation>也是<equation>A</equation>的属于特征值1的一个特征向量.<equation>A Q = A \left(\alpha_ {1} + \alpha_ {2}, \alpha_ {2}, \alpha_ {3}\right) = \left(\alpha_ {1} + \alpha_ {2}, \alpha_ {2}, 2 \alpha_ {3}\right) = Q \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>又由于 Q由 P作初等变换得到，P可逆，故Q可逆.于是<equation>Q^{-1} A Q=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>应选B.

---

**2011年第5题 | 选择题 | 4分 | 答案: D**

5. 设 A为3阶矩阵，将 A的第2列加到第1列得矩阵 B，再交换 B的第2行与第3行得单位矩阵，记<equation>P_{1}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right), P_{2}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{array} \right),</equation>则 A=（    )

A.<equation>P_{1} P_{2}</equation>B.<equation>P_{1}^{-1} P_{2}</equation>C.<equation>P_{2} P_{1}</equation>D.<equation>P_{2} P_{1}^{-1}</equation>

答案: D

**解析:**解 将 A的第2列加到第1列对应 A右乘矩阵<equation>P_{1}</equation>，得<equation>B=A P_{1}</equation>.交换 B的第2行与第3行对应 B左乘矩阵<equation>P_{2}</equation>，得<equation>E=P_{2} A P_{1}</equation>.于是<equation>A=P_{2}^{-1} P_{1}^{-1}.</equation>又因为<equation>P_{2}^{-1}=P_{2}</equation>，所以<equation>A=P_{2} P_{1}^{-1}.</equation>应选 D.

---

**2010年第13题 | 填空题 | 4分**

13. 设<equation>A, B</equation>为3阶矩阵，且<equation>|A| = 3, |B| = 2, |A^{-1} + B| = 2</equation>，则<equation>|A + B^{-1}</equation>

**解析:**由于<equation>A, B</equation>的行列式均不为零，故它们均可逆.因为

所以<equation>\boldsymbol {A} \left(\boldsymbol {A} ^ {- 1} + \boldsymbol {B}\right) \boldsymbol {B} ^ {- 1} = \boldsymbol {B} ^ {- 1} + \boldsymbol {A} = \boldsymbol {A} + \boldsymbol {B} ^ {- 1},</equation><equation>| A + B ^ {- 1} | = | A | \cdot | A ^ {- 1} + B | \cdot | B ^ {- 1} | \frac {| B ^ {- 1} | = \frac {1}{| B |}} {3 \times 2 \times \frac {1}{2}} = 3.</equation>

---

**2009年第6题 | 选择题 | 4分 | 答案: A**

6. 设<equation>A, P</equation>均为3阶矩阵，<equation>P^{\mathrm{T}}</equation>为<equation>P</equation>的转置矩阵，且<equation>P^{\mathrm{T}}AP = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>. 若<equation>P = \left(\alpha_{1}, \alpha_{2}, \alpha_{3}\right)</equation>，<equation>Q = \left(\alpha_{1} + \alpha_{2}, \alpha_{2}, \alpha_{3}\right)</equation>，

则<equation>Q^{\mathrm{T}} A Q</equation>为（    ）

A.<equation>\left( \begin{array}{c c c} 2 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>.<equation>\left( \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>B.

C.<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>

答案: A

**解析:**由题设知，<equation>Q</equation>为把 P的第2列加到第1列的结果，故<equation>Q=P\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>从而<equation>Q^{\mathrm{T}}A Q=\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) P^{\mathrm{T}} A P\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)=\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation><equation>=\left( \begin{array}{c c c} 2 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>应选A.

---


#### 伴随矩阵与可逆矩阵

**2023年第5题 | 选择题 | 5分 | 答案: B**

5. 设 A,B为 n阶可逆矩阵，E为 n阶单位矩阵，<equation>M^{*}</equation>为矩阵 M的伴随矩阵，则<equation>\left( \begin{array}{cc} A & E \\ O & B \end{array} \right)^{*}=(\quad)</equation>A.<equation>\left( \begin{array}{c c} | A | B^{*} & - B^{*} A^{*} \\ O & | B | A^{*} \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c} | B | A^{*} & - A^{*} B^{*} \\ O & | A | B^{*} \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c} | B | A^{*} & - B^{*} A^{*} \\ O & | A | B^{*} \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c} | A | B^{*} & - A^{*} B^{*} \\ O & | B | A^{*} \end{array} \right)</equation>

答案: B

**解析:**解（法一）由于 A,B都可逆，故可以作初等行变换来求<equation>\left( \begin{array}{cc} A & E \\ O & B \end{array} \right)^{-1}.</equation><equation>\left( \begin{array}{c c c c} A & E & E & O \\ O & B & O & E \end{array} \right) \xrightarrow {\textcircled{1}} \left( \begin{array}{c c c c} E & A ^ {- 1} & A ^ {- 1} & O \\ O & E & O & B ^ {- 1} \end{array} \right) \xrightarrow {\textcircled{2}} \left( \begin{array}{c c c c} E & O & A ^ {- 1} & - A ^ {- 1} B ^ {- 1} \\ O & E & O & B ^ {- 1} \end{array} \right),</equation>其中操作<equation>\textcircled{1}</equation>对应左乘可逆矩阵<equation>\left( \begin{array}{cc} A^{-1} & O \\ O & B^{-1} \end{array} \right)</equation>，操作<equation>\textcircled{2}</equation>对应左乘可逆矩阵<equation>\left( \begin{array}{cc} E & -A^{-1} \\ O & E \end{array} \right)</equation>.于是，<equation>\left( \begin{array}{c c} A & E \\ O & B \end{array} \right) ^ {- 1} = \left( \begin{array}{c c} A ^ {- 1} & - A ^ {- 1} B ^ {- 1} \\ O & B ^ {- 1} \end{array} \right).</equation>对于任意 n阶方阵 M，都有<equation>M M^{*} = | M | E</equation>，从而当 M可逆时，<equation>M^{*} = | M | M^{-1}.</equation>又因为<equation>\left| \begin{array}{l l} A & E \\ O & B \end{array} \right| = | A | | B |</equation>，所以<equation>\left( \begin{array}{c c} A & E \\ O & B \end{array} \right) ^ {*} = \left| \begin{array}{c c} A & E \\ O & B \end{array} \right| \left( \begin{array}{c c} A & E \\ O & B \end{array} \right) ^ {- 1} = | A | | B | \left( \begin{array}{c c} A ^ {- 1} & - A ^ {- 1} B ^ {- 1} \\ O & B ^ {- 1} \end{array} \right) = \left( \begin{array}{c c} | B | A ^ {*} & - A ^ {*} B ^ {*} \\ O & | A | B ^ {*} \end{array} \right).</equation>因此，应选B.

也可以如下计算<equation>\left( \begin{array}{cc} A & E \\ O & B \end{array} \right)^{-1}.</equation>设<equation>\left( \begin{array}{cc} A & E \\ O & B \end{array} \right)^{-1}=\left( \begin{array}{cc} X_{1} & X_{2} \\ X_{3} & X_{4} \end{array} \right),</equation>则<equation>\left( \begin{array}{c c} A & E \\ O & B \end{array} \right) \left( \begin{array}{c c} X _ {1} & X _ {2} \\ X _ {3} & X _ {4} \end{array} \right) = \left( \begin{array}{c c} A X _ {1} + X _ {3} & A X _ {2} + X _ {4} \\ B X _ {3} & B X _ {4} \end{array} \right) = \left( \begin{array}{c c} E & O \\ O & E \end{array} \right).</equation>于是，<equation>\left\{ \begin{array}{l l} A X_{1}+X_{3}=E, \\ A X_{2}+X_{4}=O, \\ B X_{3}=O, \\ B X_{4}=E. \end{array} \right.</equation>由A，B均为可逆矩阵可得<equation>\left\{ \begin{array}{l l} X_{1}=A^{-1}, \\ X_{2}=-A^{-1}B^{-1}, \\ X_{3}=O, \\ X_{4}=B^{-1}. \end{array} \right.</equation>从而<equation>\left( \begin{array}{c c} A & E \\ O & B \end{array} \right) ^ {- 1} = \left( \begin{array}{c c} A ^ {- 1} & - A ^ {- 1} B ^ {- 1} \\ O & B ^ {- 1} \end{array} \right).</equation>（法二）分别记选项A、B、C、D中的矩阵为<equation>M_{1}, M_{2}, M_{3}, M_{4}</equation>，记<equation>\left( \begin{array}{cc} A & E \\ O & B \end{array} \right)=M.</equation>考虑<equation>M_{i}M (i=1,</equation>2,3,4). 若<equation>M_{i}=M^{*}</equation>，则<equation>M_{i}M=|A||B|E_{2n}.</equation>观察可得<equation>M_{1}M</equation>与<equation>M_{4}M</equation>的“第一列”均为<equation>\left( \begin{array}{c c} {| A | B^{*} A} \\ {O} \end{array} \right)</equation>，故<equation>M _ {1} M \neq | A | | B | E _ {2 n}, \quad M _ {4} M \neq | A | | B | E _ {2 n}.</equation>选项A、D均不正确.

又因为<equation>\left( \begin{array}{c c} | B | A ^ {*} & - B ^ {*} A ^ {*} \\ O & | A | B ^ {*} \end{array} \right) \left( \begin{array}{c c} A & E \\ O & B \end{array} \right) = \left( \begin{array}{c c} | A | | B | E & | B | A ^ {*} - B ^ {*} A ^ {*} B \\ O & | A | | B | E \end{array} \right) \neq | A | | B | E _ {2 n},</equation><equation>\left( \begin{array}{c c} | B | A ^ {*} & - A ^ {*} B ^ {*} \\ O & | A | B ^ {*} \end{array} \right) \left( \begin{array}{c c} A & E \\ O & B \end{array} \right) = \left( \begin{array}{c c} | A | | B | E & | B | A ^ {*} - A ^ {*} B ^ {*} B \\ O & | A | | B | E \end{array} \right) = | A | | B | E _ {2 n},</equation>所以选项C不正确，选项B正确. 应选B.

---

**2019年第5题 | 选择题 | 4分 | 答案: A**

5. 设 A是4阶矩阵，<equation>A^{*}</equation>是 A的伴随矩阵，若线性方程组<equation>A x=0</equation>的基础解系中只有2个向量，则<equation>r \left( A^{*} \right)=</equation>(    )

A.0 B.1 C.2 D.3

答案: A

**解析:**解 由于<equation>A x=0</equation>的基础解系中只含有2个向量，故<equation>r(A)=4-2=2</equation>又因为<equation>r(A)=2< 4-1</equation>所以<equation>r(A^{*})=0.</equation>因此，应选A.

---

**2017年第5题 | 选择题 | 4分 | 答案: A**

5. 设<equation>\alpha</equation>为 n维单位列向量，<equation>E</equation>为 n阶单位矩阵，则（    ）

A.<equation>E-\alpha\alpha^{\mathrm{T}}</equation>不可逆 B.<equation>E+\alpha\alpha^{\mathrm{T}}</equation>不可逆 C.<equation>E+2\alpha\alpha^{\mathrm{T}}</equation>不可逆 D.<equation>E-2\alpha\alpha^{\mathrm{T}}</equation>不可逆

答案: A

**解析:**解（法一）由于<equation>\alpha</equation>是n维单位列向量，故<equation>\operatorname{tr}(\alpha\alpha^{\mathrm{T}})=\alpha^{\mathrm{T}}\alpha=1</equation>因为<equation>\alpha</equation>非零，所以<equation>r(\alpha\alpha^{\mathrm{T}})\geqslant 1.</equation>又由于<equation>r(\alpha\alpha^{\mathrm{T}})\leqslant r(\alpha)=1</equation>故<equation>r(\alpha\alpha^{\mathrm{T}})=1.</equation>于是矩阵<equation>\alpha\alpha^{\mathrm{T}}</equation>的全部特征值为1，0，…，0，从而<equation>E-\alpha\alpha^{\mathrm{T}}</equation>的全部特征值为0，1，…，1.因此，<equation>E-\alpha\alpha^{\mathrm{T}}</equation>不可逆.应选A.

同理可得，<equation>E+\alpha\alpha^{\mathrm{T}}</equation>的全部特征值为2，1，…，1；<equation>E+2\alpha\alpha^{\mathrm{T}}</equation>的全部特征值为3，1，…，1；<equation>E-2\alpha\alpha^{\mathrm{T}}</equation>的全部特征值为-1，1，…，1.因此它们均可逆.

（法二）由于<equation>(\alpha\alpha^{\mathrm{T}})\alpha = \alpha(\alpha^{\mathrm{T}}\alpha) = \alpha</equation>，故<equation>(E - \alpha \alpha^ {\mathrm {T}}) \alpha = \alpha - \left(\alpha \alpha^ {\mathrm {T}}\right) \alpha = \alpha - \alpha = 0 = 0 \alpha .</equation>于是，0是<equation>E-\alpha\alpha^{\mathrm{T}}</equation>的一个特征值（或<equation>( E-\alpha\alpha^{\mathrm{T}} ) x=0</equation>有非零解<equation>\alpha ).</equation>因此，<equation>E-\alpha\alpha^{\mathrm{T}}</equation>不可逆.应选A.

（法三）排除法.

令<equation>\boldsymbol{\alpha} = (1,0,\cdots ,0)^{\mathrm{T}}</equation>，则<equation>\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}}=\left( \begin{array}{c c c c} 1 & & & \\ & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right).</equation>可以验证，<equation>E+\alpha\alpha^{\mathrm{T}},E+2\alpha\alpha^{\mathrm{T}},E-2\alpha\alpha^{\mathrm{T}}</equation>均可逆，从而可以排除选项B、C、D.因此，应选A.

---

**2012年第13题 | 填空题 | 4分**

13. 设<equation>A</equation>为3阶矩阵，<equation>|A|=3</equation><equation>A^{*}</equation>为<equation>A</equation>的伴随矩阵，若交换<equation>A</equation>的第1行与第2行得矩阵<equation>B</equation>，则<equation>|BA^{*}|=</equation>___.

**解析:**解（法一）由于 B为交换 A的第1行与第2行所得，故<equation>B=E(1,2)A</equation>从而<equation>\boldsymbol {B} \boldsymbol {A} ^ {*} = \boldsymbol {E} (1, 2) \boldsymbol {A} \boldsymbol {A} ^ {*} = \boldsymbol {E} (1, 2) | \boldsymbol {A} | \boldsymbol {E} = 3 \boldsymbol {E} (1, 2).</equation>因此，<equation>\left| B A ^ {*} \right| = \left| 3 E (1, 2) \right| = 3 ^ {3} \left| \begin{array}{c c c} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right| = - 2 7.</equation>（法二）由于<equation>A A^{*} = |A|E</equation>，故当A为3阶矩阵时，<equation>| \boldsymbol {A} | \cdot | \boldsymbol {A} ^ {*} | = | \boldsymbol {A A} ^ {*} | = \left| \begin{array}{c c c} | \boldsymbol {A} | & 0 & 0 \\ 0 & | \boldsymbol {A} | & 0 \\ 0 & 0 & | \boldsymbol {A} | \end{array} \right| = | \boldsymbol {A} | ^ {3}.</equation>从而<equation>|A^{*}| = |A|^{2}</equation>.

另一方面，由于<equation>B</equation>为交换<equation>A</equation>的第1行与第2行所得矩阵，故<equation>|B| = -|A|</equation>.因此，<equation>| B A ^ {*} | = | B | \cdot | A ^ {*} | = - | A | \cdot | A | ^ {2} = - 2 7.</equation>

---

**2009年第5题 | 选择题 | 4分 | 答案: B**

5. 设 A,B均为2阶方阵，<equation>A^{*}，B^{*}</equation>分别为 A,B的伴随矩阵.若<equation>|A|=2,|B|=3</equation>，则分块矩阵<equation>\left( \begin{array}{cc} O&A \\ B/O \end{array} \right)</equation>的伴随矩阵为（    )

A.<equation>\left( \begin{array}{c c} O & 3 B^{*} \\ 2 A^{*} & O \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c} O & 2 B^{*} \\ 3 A^{*} & O \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c} O & 3 A^{*} \\ 2 B^{*} & O \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c} O & 2 A^{*} \\ 3 B^{*} & O \end{array} \right)</equation>

答案: B

**解析:**解 （法一）先求<equation>\left| \begin{array}{cc}O&A\\ B/O \end{array} \right|.</equation>记<equation>C=\left( \begin{array}{cc}O&A\\ B/O \end{array} \right), C</equation>为4阶矩阵，A位于它的第1，2行和第3，4列，可按照以下步骤把C变为<equation>\left( \begin{array}{cc}A&O\\ O&B \end{array} \right).</equation>把C的第3列与第1列对换，第4列与第2列对换.因此，<equation>\left| \begin{array}{c c} O & A \\ B & O \end{array} \right| = (- 1) ^ {2} \left| \begin{array}{c c} A & O \\ O & B \end{array} \right| = | A | \cdot | B | = 6.</equation><equation>\left( \begin{array}{cc}O&A\\ B/O \end{array} \right)</equation>可逆.

由可逆矩阵与其伴随矩阵的关系可知，<equation>\left( \begin{array}{c c} O & A \\ B & O \end{array} \right) ^ {*} = \left| \begin{array}{c c} O & A \\ B & O \end{array} \right| \left( \begin{array}{c c} O & A \\ B & O \end{array} \right) ^ {- 1} = 6 \left( \begin{array}{c c} O & A \\ B & O \end{array} \right) ^ {- 1}.</equation>不妨设<equation>\left( \begin{array}{cc}O&A\\ B/O \end{array} \right)^{-1} = \left( \begin{array}{cc}X_1 & X_2\\ X_3 & X_4 \end{array} \right)</equation>，则<equation>\left( \begin{array}{c c} O & A \\ B & O \end{array} \right) \left( \begin{array}{c c} X _ {1} & X _ {2} \\ X _ {3} & X _ {4} \end{array} \right) = \left( \begin{array}{c c} A X _ {3} & A X _ {4} \\ B X _ {1} & B X _ {2} \end{array} \right) = \left( \begin{array}{c c} E & O \\ O & E \end{array} \right).</equation>由于 A,B均为可逆矩阵，故由<equation>A X_{4}=O</equation>，<equation>B X_{1}=O</equation>可知，<equation>X_{1}=X_{4}=O</equation>；由<equation>A X_{3}=E</equation>，<equation>B X_{2}=E</equation>得，<equation>X_{3}=A^{-1}</equation>，<equation>X_{2}=B^{-1}</equation>.因此，<equation>\left( \begin{array}{c c} \boldsymbol {O} & \boldsymbol {A} \\ \boldsymbol {B} & \boldsymbol {O} \end{array} \right) ^ {- 1} = \left( \begin{array}{c c} \boldsymbol {O} & \boldsymbol {B} ^ {- 1} \\ \boldsymbol {A} ^ {- 1} & \boldsymbol {O} \end{array} \right).</equation><equation>\left( \begin{array}{c c} O & A \\ B & O \end{array} \right) ^ {*} = 6 \left( \begin{array}{c c} O & B ^ {- 1} \\ A ^ {- 1} & O \end{array} \right) = 6 \left( \begin{array}{c c} O & \frac {B ^ {*}}{| B |} \\ \frac {A ^ {*}}{| A |} & O \end{array} \right) = \left( \begin{array}{c c} O & 2 B ^ {*} \\ 3 A ^ {*} & O \end{array} \right).</equation>应选B.

（法二）特殊值法.

取<equation>A=\sqrt{2} E, B=\sqrt{3} E</equation>满足<equation>|A|=2,|B|=3</equation>，则<equation>A^{*} = |A|A^{-1} = \sqrt{2} E, B^{*} = |B|B^{-1} = \sqrt{3} E.</equation>因此，<equation>\begin{aligned} \left( \begin{array}{c c} O & A \\ B & O  \right) ^ {*} &= \left( \begin{array}{c c} O & \sqrt {2} E \\ \sqrt {3} E & O  \right) ^ {*} &= \left| \begin{array}{c c} O & \sqrt {2} E \\ \sqrt {3} E & O  \right| \left( \begin{array}{c c} O & \sqrt {2} E \\ \sqrt {3} E & O  \right) ^ {- 1} &= 6 \left( \begin{array}{c c} O & \frac {1}{\sqrt {3}} E \\ \frac {1}{\sqrt {2}} E & O  \right) \\ &= \left( \begin{array}{c c} O & 2 \sqrt {3} E \\ 3 \sqrt {2} E & O  \right) &= \left( \begin{array}{c c} O & 2 B ^ {*} \\ 3 A ^ {*} & O  \right). \end{aligned}</equation>应选B.

---


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


#### 协方差与相关系数

**2025年第8题 | 选择题 | 5分 | 答案: D**

8. 设随机变量 X服从正态分布 N(-1,1), Y服从正态分布 N(1,2), 若 X与 X+2Y不相关，则 X与 X-Y的相关系数为（    ）

A.<equation>\frac{1}{3}</equation>B.<equation>\frac{1}{2}</equation>C.<equation>\frac{2}{3}</equation>D.<equation>\frac{3}{4}</equation>

答案: D

**解析:**解 由于 X服从正态分布 N（-1，1），Y服从正态分布 N（1，2），故 D（X）=1，D（Y）=2. 又因为 X与 X+2Y不相关，所以<equation>\operatorname{Cov}(X, X + 2 Y) = \operatorname{Cov}(X, X) + 2 \operatorname{Cov}(X, Y) = D (X) + 2 \operatorname{Cov}(X, Y) = 1 + 2 \operatorname{Cov}(X, Y) = 0.</equation>于是，<equation>\operatorname{Cov}(X, Y) = -\frac{1}{2}.</equation>进一步可得<equation>\operatorname {C o v} (X, X - Y) = \operatorname {C o v} (X, X) - \operatorname {C o v} (X, Y) = D (X) - \operatorname {C o v} (X, Y) = 1 - \left(- \frac {1}{2}\right) = \frac {3}{2}.</equation><equation>D (X - Y) = D (X) + D (Y) - 2 \operatorname {C o v} (X, Y) = 1 + 2 - 2 \cdot \left(- \frac {1}{2}\right) = 4.</equation>因此，X与X-Y的相关系数<equation>\rho = \frac {\operatorname {C o v} (X , X - Y)}{\sqrt {D (X)} \sqrt {D (X - Y)}} = \frac {\frac {3}{2}}{1 \cdot 2} = \frac {3}{4}.</equation>应选 D.

---

**2023年第16题 | 填空题 | 5分**

16. 设随机变量 X 与 Y 相互独立，且<equation>X \sim B ( 1, p )</equation><equation>Y \sim B ( 2, p )</equation><equation>p \in( 0, 1 )</equation>，则<equation>X+Y</equation>与<equation>X-Y</equation>的相关系数为___.

**答案:**<equation>- \frac {1}{3}.</equation>

**解析:**解 由<equation>X\sim B(1,p)</equation>可知，<equation>D ( X )=p ( 1-p ).</equation>由<equation>Y\sim B ( 2,p)</equation>可知，<equation>D ( Y )=2 p ( 1-p ).</equation><equation>X+Y</equation>与<equation>X-Y</equation>的相关系数<equation>\rho=\frac{\operatorname{Cov}(X+Y,X-Y)}{\sqrt{D(X+Y)}\sqrt{D(X-Y)}}.</equation>由于 X与 Y相互独立，故<equation>D (X + Y) = D (X) + D (Y) = 3 p (1 - p),</equation><equation>D (X - Y) = D (X) + D (Y) = 3 p (1 - p).</equation>由协方差的性质可得，<equation>\begin{aligned} \operatorname {C o v} (X + Y, X - Y) &= \operatorname {C o v} (X, X) - \operatorname {C o v} (X, Y) + \operatorname {C o v} (Y, X) - \operatorname {C o v} (Y, Y) \\ &= D (X) - D (Y) = - p (1 - p). \end{aligned}</equation>因此，<equation>\rho = \frac {- p (1 - p)}{\sqrt {3 p (1 - p)} \sqrt {3 p (1 - p)}} = - \frac {1}{3}.</equation>

---

**2022年第8题 | 选择题 | 5分 | 答案: D**

8. 设随机变量<equation>X\sim N(0,4)</equation>，随机变量<equation>Y\sim B\left(3,\frac{1}{3}\right)</equation>，且 X，Y不相关，则<equation>D(X-3Y+1)=</equation>(    )

A.2 B.4 C.6 D.10

答案: D

**解析:**解 由于 X~ N（0,4），Y~ B<equation>\left( 3, \frac{1}{3} \right)</equation>，故 X的方差 D（X）=4，Y的方差<equation>D (Y) = 3 \times \frac {1}{3} \times \left(1 - \frac {1}{3}\right) = \frac {2}{3}.</equation>又因为<equation>X, Y</equation>不相关，所以<equation>\operatorname{Cov}(X, Y) = 0.</equation>由方差的性质，<equation>\begin{aligned} D (X - 3 Y + 1) &= D (X - 3 Y) = D (X) + D (3 Y) - 2 \operatorname {C o v} (X, 3 Y) \\ &= D (X) + 9 D (Y) - 6 \operatorname {C o v} (X, Y) = 4 + 9 \times \frac {2}{3} - 0 = 1 0. \end{aligned}</equation>因此，应选D.

---

**2022年第10题 | 选择题 | 5分 | 答案: B**

10. 设二维随机变量（X，Y）的概率分布为

<table border="1"><tr><td>X\ Y</td><td>0</td><td>1</td><td>2</td></tr><tr><td>-1</td><td>0.1</td><td>0.1</td><td>b</td></tr><tr><td>1</td><td>a</td><td>0.1</td><td>0.1</td></tr></table>

若事件<equation>\{\max \{X,Y\}=2\}</equation>与事件<equation>\{\min \{X,Y\}=1\}</equation>相互独立，则<equation>\operatorname{Cov}(X,Y)=</equation>(    )

A. -0.6 B. -0.36 C. 0 D. 0.48

答案: B

**解析:**解记事件 A = {<equation>\max \{ X, Y \}=2</equation>} ，事件 B = {<equation>\min \{ X, Y \}=1</equation>} .由于事件 A与B相互独立，故 P（AB）=P(A)P(B).

分别计算 P（A），P（B），P（AB）.<equation>P (A) = P \left\{\max \left\{X, Y \right\} = 2 \right\} = P \left\{Y = 2 \right\} = b + 0. 1.</equation><equation>P (B) = P \left\{\min \left\{X, Y \right\} = 1 \right\} = P \left\{X = 1, Y = 1 \right\} + P \left\{X = 1, Y = 2 \right\} = 0. 1 + 0. 1 = 0. 2.</equation><equation>P (A B) = P \left\{\max \left\{X, Y \right\} = 2, \min \left\{X, Y \right\} = 1 \right\} = P \left\{X = 1, Y = 2 \right\} = 0. 1.</equation>于是，<equation>0. 1 = ( b + 0. 1 ) \times 0. 2</equation>，解得 b=0.4. 进一步，由联合分布律中各概率之和为1，即<equation>0. 1 + 0. 1</equation><equation>+ b + a + 0. 1 + 0. 1 = 1</equation>可得，a=0.2.

XY的可能取值为-2，-1，0，1，2.<equation>P \{X Y = - 2 \} = P \{X = - 1, Y = 2 \} = 0. 4.</equation><equation>P \left\{X Y = - 1 \right\} = P \left\{X = - 1, Y = 1 \right\} = 0. 1.</equation><equation>P \{X Y = 1 \} = P \{X = 1, Y = 1 \} = 0. 1.</equation><equation>P \{X Y = 2 \} = P \{X = 1, Y = 2 \} = 0. 1.</equation><equation>P \{X Y = 0 \} = 1 - 0. 4 - 0. 1 - 0. 1 - 0. 1 = 0. 3.</equation>分别计算 E（X），E（Y），E（XY）.<equation>E (X) = - 1 \times (0. 1 + 0. 1 + 0. 4) + 1 \times (0. 2 + 0. 1 + 0. 1) = - 0. 2.</equation><equation>E (Y) = 0 \times (0. 1 + 0. 2) + 1 \times (0. 1 + 0. 1) + 2 \times (0. 4 + 0. 1) = 1. 2.</equation><equation>E (X Y) = (- 2) \times 0. 4 + (- 1) \times 0. 1 + 0 \times 0. 3 + 1 \times 0. 1 + 2 \times 0. 1 = - 0. 6.</equation>因此，<equation>\operatorname {C o v} (X, Y) = E (X Y) - E (X) E (Y) = - 0. 6 - (- 0. 2) \times 1. 2 = - 0. 3 6.</equation>应选B.

---

**2021年第16题 | 填空题 | 5分**

16. 甲，乙两个盒子中各装有2个红球和2个白球，先从甲盒中任取一球，观察颜色后放入乙盒中，再从乙盒中任取一个球，令 X, Y分别表示从甲盒和乙盒中取到的红球个数，则 X与 Y的相关系数为___

**答案:**# 1 5.

**解析:**解 根据相关系数的计算公式，X与Y的相关系数为<equation>\rho = \frac {\operatorname {C o v} (X , Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}}.</equation>下面分别计算 X, Y的分布律与数字特征.

取球模型为等可能模型.

X的可能取值为0，1.取到白球，则<equation>X=0</equation>，取到红球，则<equation>X=1.</equation><equation>P \{X = 0 \} = \frac {1}{2}, \quad P \{X = 1 \} = \frac {1}{2}.</equation>于是，<equation>E ( X ) = \frac {1}{2}, E \left( X^{2}\right) = \frac {1}{2}, D ( X ) = \frac {1}{2} - \left(\frac {1}{2}\right)^{2} = \frac {1}{4}.</equation>Y的可能取值为0，1. 若从甲盒中取出的是白球，则后来乙盒中共有2个红球和3个白球，取到红球的概率为<equation>\frac{2}{5}</equation>即在 X=0发生的条件下 Y=1发生的概率为<equation>\frac{2}{5}</equation>；若从甲盒中取出的是红球，则后来乙盒中共有3个红球和2个白球，取到红球的概率为<equation>\frac{3}{5}</equation>即在 X=1发生的条件下 Y=1发生的概率为<equation>\frac{3}{5}.</equation><equation>\begin{aligned} P \{Y = 1 \} &= P \{Y = 1 \mid X = 0 \} P \{X = 0 \} + P \{Y = 1 \mid X = 1 \} P \{X = 1 \} \\ &= \frac {2}{5} \times \frac {1}{2} + \frac {3}{5} \times \frac {1}{2} = \frac {1}{2}. \end{aligned}</equation><equation>P \{Y = 0 \} = 1 - P \{Y = 1 \} = 1 - \frac {1}{2} = \frac {1}{2}.</equation>于是，<equation>E ( Y )=\frac{1}{2}, E ( Y^{2} )=\frac{1}{2}, D ( Y )=\frac{1}{2}-\left(\frac{1}{2}\right)^{2}=\frac{1}{4}.</equation>XY的可能取值为0,1.<equation>P \{X Y = 1 \} = P \{X = 1, Y = 1 \} = P \{Y = 1 \mid X = 1 \} P \{X = 1 \} = \frac {3}{5} \times \frac {1}{2} = \frac {3}{1 0}.</equation><equation>P \{X Y = 0 \} = 1 - \frac {3}{1 0} = \frac {7}{1 0}.</equation>于是，<equation>E ( X Y ) = P \{ X Y = 1 \} \times 1 + P \{ X Y = 0 \} \times 0 = \frac {3}{1 0}.</equation>因此，<equation>\rho = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {\frac {3}{1 0} - \frac {1}{2} \times \frac {1}{2}}{\frac {1}{2} \times \frac {1}{2}} = \frac {\frac {1}{2 0}}{\frac {1}{4}} = \frac {1}{5}.</equation>

---


#### 数学期望与方差

**2024年第8题 | 选择题 | 5分 | 答案: B**

8. 设随机变量 X的概率密度为<equation>f ( x )=\left\{\begin{array}{ll}6 x(1-x),&0<x<1,\\0,&\text{其他},\end{array}\right.</equation>则 X的三阶中心矩<equation>E \left\{ \left[ X-E ( X ) \right]^{3} \right\}=(\quad)</equation>A.<equation>-\frac{1}{3 2}</equation>B.0 C.<equation>\frac{1}{1 6}</equation>D.<equation>\frac{1}{2}</equation>

答案: B

**解析:**解 根据数学期望的定义，<equation>\begin{aligned} E (X) &= \int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \int_ {0} ^ {1} x \cdot 6 x (1 - x) \mathrm {d} x = \int_ {0} ^ {1} \left(6 x ^ {2} - 6 x ^ {3}\right) \mathrm {d} x = \left. \left(2 x ^ {3} - \frac {3 x ^ {4}}{2}\right) \right| _ {0} ^ {1} \\ &= 2 - \frac {3}{2} = \frac {1}{2}. \end{aligned}</equation>进一步可得，<equation>\begin{array}{l} E \left\{\left[ X - E (X) \right] ^ {3} \right\} = \int_ {- \infty} ^ {+ \infty} \left(x - \frac {1}{2}\right) ^ {3} f (x) \mathrm {d} x = \int_ {0} ^ {1} \left(x - \frac {1}{2}\right) ^ {3} \cdot 6 x (1 - x) \mathrm {d} x \\ \underline {{=}} t = x - \frac {1}{2} 6 \int_ {- \frac {1}{2}} ^ {\frac {1}{2}} t ^ {3} \cdot \left(t + \frac {1}{2}\right) \left(\frac {1}{2} - t\right) \mathrm {d} t = 6 \int_ {- \frac {1}{2}} ^ {\frac {1}{2}} t ^ {3} \left(\frac {1}{4} - t ^ {2}\right) \mathrm {d} t \\ = 6 \int_ {- \frac {1}{2}} ^ {\frac {1}{2}} \left(\frac {1}{4} t ^ {3} - t ^ {5}\right) \mathrm {d} t \stackrel {\text {对称性}} {=} 0. \\ \end{array}</equation>因此，应选B.

---


### 随机变量及其分布

**2025年第9题 | 选择题 | 5分 | 答案: C**

9. 设<equation>X_{1}, X_{2}, \dots , X_{2 0}</equation>是来自总体B(1,0.1)的简单随机样本，令<equation>T=\sum_{i=1}^{2 0} X_{i}</equation>利用泊松分布近似表示二项分布的方法可得<equation>P\{ T\leqslant 1\}\approx</equation>(    )

A.<equation>\frac{1} {\mathrm{e}^{2}}</equation>B.<equation>\frac{2} {\mathrm{e}^{2}}</equation>C.<equation>\frac{3} {\mathrm{e}^{2}}</equation>D.<equation>\frac{4} {\mathrm{e}^{2}}</equation>

答案: C

**解析:**解 由<equation>X_{i}(i = 1,2,\dots ,20)\sim B(1,0.1)</equation>可知，<equation>X_{i}</equation>可看作一次随机试验的结果，试验成功的概率为0.1，<equation>T = \sum_{i = 1}^{20}X_{i}</equation>可看作20次独立重复试验中试验成功的次数，服从<equation>B(20,0.1)</equation>.根据泊松定理，<equation>n = 20,p_{n} = 0.1,\lambda = 2,T</equation>近似服从参数为2的泊松分布.

因此，<equation>P \{T \leqslant 1 \} = P \{T = 0 \} + P \{T = 1 \} \approx \frac {2 ^ {0} \cdot \mathrm {e} ^ {- 2}}{1} + \frac {2 ^ {1} \cdot \mathrm {e} ^ {- 2}}{1} = \frac {3}{\mathrm {e} ^ {2}}.</equation>应选C.

---

**2025年第10题 | 选择题 | 5分 | 答案: C**

10. 设总体 X的分布函数为 F(x),<equation>X_{1}, X_{2}, \dots, X_{n}</equation>为来自总体 X的简单随机样本，样本的经验分布函数为<equation>F_{n}(x)</equation>对于给定的 x(0 < F(x) < 1), D(F_{n}(x))=（    )

A. F(x)[1-F(x)] B.<equation>[F(x)]^{2}</equation>C.<equation>\frac{1}{n} F(x)[1-F(x)]</equation>D.<equation>\frac{1}{n}[F(x)]^{2}</equation>

答案: C

**解析:**解记<equation>X_{i}</equation>的分布函数为<equation>F_{X_{i}}(x).</equation>由于<equation>X_{i} ( i=1,2,\dots,n)</equation>与X同分布，故<equation>F_{X_{i}}(x)=F(x).</equation>令<equation>Y_{i}=\left\{\begin{array}{ll}1,&X_{i}\leqslant x,\\ 0,&X_{i}>x,\end{array}\right. i=1,2,\dots,n</equation>则<equation>Y_{i}</equation>的分布律满足<equation>P \left\{Y _ {i} = 1 \right\} = P \left\{X _ {i} \leqslant x \right\} = F _ {X _ {i}} (x) = F (x),</equation><equation>P \left\{Y _ {i} = 0 \right\} = P \left\{X _ {i} > x \right\} = 1 - F _ {X _ {i}} (x) = 1 - F (x).</equation>由此可得<equation>Y_{i}\sim B(1,F(x))</equation>.于是，<equation>E \left(Y _ {i}\right) = F (x), \quad D \left(Y _ {i}\right) = F (x) [ 1 - F (x) ].</equation>注意到<equation>F_{n}(x)=\frac{1}{n}\sum_{i=1}^{n} Y_{i}</equation>，且<equation>Y_{1},Y_{2},\dots ,Y_{n}</equation>独立同分布，故<equation>D \left[ F _ {n} (x) \right] = D \left(\frac {1}{n} \sum_ {i = 1} ^ {n} Y _ {i}\right) = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} D \left(Y _ {i}\right) = \frac {1}{n} D \left(Y _ {i}\right) = \frac {1}{n} F (x) [ 1 - F (x) ].</equation>因此，应选C.

---

**2024年第9题 | 选择题 | 5分 | 答案: B**

9. 设随机变量 X, Y相互独立，且<equation>X\sim N(0,2),Y\sim N(-1,1)</equation>，设<equation>p_{1}=P\{2X>Y\}, p_{2}=P\{X-2Y>1\}</equation>，则（    )

A.<equation>p_{1}>p_{2}>\frac{1}{2}</equation>B.<equation>p_{2}>p_{1}>\frac{1}{2}</equation>C.<equation>p_{1}<p_{2}<\frac{1}{2}</equation>D.<equation>p_{2}<p_{1}<\frac{1}{2}</equation>

答案: B

**解析:**解 由于<equation>X\sim N(0,2),Y\sim N(-1,1)</equation>，故<equation>E(X) = 0,D(X) = 2,E(Y) = -1,D(Y) = 1</equation>，从而<equation>E (Y - 2 X) = E (Y) - 2 E (X) = - 1 - 0 = - 1,</equation><equation>D (Y - 2 X) = D (Y) + 4 D (X) = 1 + 4 \times 2 = 9,</equation><equation>E (2 Y - X) = 2 E (Y) - E (X) = 2 \times (- 1) - 0 = - 2,</equation><equation>D (2 Y - X) = 4 D (Y) + D (X) = 4 \times 1 + 2 = 6.</equation>于是，<equation>Y - 2 X\sim N(-1,9), 2 Y - X\sim N(-2,6).</equation>将它们标准化可得<equation>\frac{Y - 2 X + 1}{3}\sim N(0,1),</equation><equation>\frac{2 Y - X + 2}{\sqrt{6}}\sim N(0,1).</equation>由此可得，<equation>\begin{array}{l} p _ {1} = P | 2 X - Y > 0 | = P | Y - 2 X < 0 | = P \left\{\frac {Y - 2 X + 1}{3} < \frac {1}{3} \right\} \\ = P \left\{\frac {Y - 2 X + 1}{3} \leqslant \frac {1}{3} \right\} = \Phi \left(\frac {1}{3}\right), \\ \end{array}</equation><equation>\begin{array}{l} p _ {2} = P \left| X - 2 Y > 1 \right| = P \left| 2 Y - X < - 1 \right| = P \left\{\frac {2 Y - X + 2}{\sqrt {6}} < \frac {1}{\sqrt {6}} \right\} \\ = P \left\{\frac {2 Y - X + 2}{\sqrt {6}} \leqslant \frac {1}{\sqrt {6}} \right\} = \Phi \left(\frac {1}{\sqrt {6}}\right), \\ \end{array}</equation>其中<equation>\varPhi(x)</equation>是标准正态分布的分布函数.

由于<equation>\varPhi(x)</equation>单调增加，且<equation>0 < \frac{1}{3} < \frac{1}{\sqrt{6}}</equation>，故<equation>\frac{1}{2}=\varPhi(0)<\varPhi\left(\frac{1}{3}\right)<\varPhi\left(\frac{1}{\sqrt{6}}\right).</equation>因此，<equation>p_{2}>p_{1}> \frac{1}{2}</equation>应选B.

---

**2024年第16题 | 填空题 | 5分**

16. 设随机试验每次成功的概率为 p，现进行3次独立重复试验，在至少成功1次的条件下，3次试验全部成功的概率为<equation>\frac{4}{1 3}</equation>，则 p=___

**答案:**# p=2/3
