**解析:**解（法一）不妨设<equation>\lambda</equation>为 A的特征值，<equation>\alpha</equation>为其对应的特征向量.由<equation>A^{2}+A=O</equation>得，<equation>(A^{2}+A)\alpha=0.</equation>代入<equation>A\alpha=\lambda\alpha</equation>得，<equation>(\lambda^{2}+\lambda)\alpha=0.</equation>又由于<equation>\alpha</equation>非零，故<equation>\lambda^{2}+\lambda=0, \lambda=0</equation>或<equation>\lambda=-1.</equation>由于 A为实对称矩阵，故 A相似于对角矩阵.又因为<equation>r ( A )=3</equation>，所以对角矩阵的秩也为3，<equation>\lambda=-1</equation>是 A的三重特征值，A相似于<equation>\left( \begin{array}{c c c c} - 1 & & & \\ & - 1 & & \\ & & - 1 & \\ & & & 0 \end{array} \right)</equation>.应选D.

（法二）由于 A为实对称矩阵，故存在可逆矩阵 P使得<equation>P^{-1} A P=\left( \begin{array}{c c c c} \lambda_{1} & & & \\ & \lambda_{2} & & \\ & & \lambda_{3} & \\ & & & \lambda_{4} \end{array} \right).</equation>从而<equation>\begin{aligned} \boldsymbol {O} &= \boldsymbol {A} ^ {2} + \boldsymbol {A} = \boldsymbol {P} \left( \begin{array}{c c c c} \lambda_ {1} ^ {2} & & & \\ & \lambda_ {2} ^ {2} & & \\ & & \lambda_ {3} ^ {2} & \\ & & & \lambda_ {4} ^ {2}  \right) \boldsymbol {P} ^ {- 1} + \boldsymbol {P} \left( \begin{array}{c c c c} \lambda_ {1} & & & \\ & \lambda_ {2} & & \\ & & \lambda_ {3} & \\ & & & \lambda_ {4}  \right) \boldsymbol {P} ^ {- 1} \\ &= \boldsymbol {P} \left( \begin{array}{c c c c} \lambda_ {1} ^ {2} + \lambda_ {1} & & & \\ & \lambda_ {2} ^ {2} + \lambda_ {2} & & \\ & & \lambda_ {3} ^ {2} + \lambda_ {3} & \\ & & & \lambda_ {4} ^ {2} + \lambda_ {4}  \right) \boldsymbol {P} ^ {- 1}. \end{aligned}</equation>因此<equation>\lambda_{i}^{2}+\lambda_{i}=0 ( i=1,2,3,4).</equation>解得<equation>\lambda_{i}=0</equation>或<equation>\lambda_{i}=-1 ( i=1,2,3,4).</equation>又由于 r（A）=3，故A相似于<equation>\left( \begin{array}{c c c c} - 1 & & & \\ & - 1 & & \\ & & - 1 & \\ & & & 0 \end{array} \right).</equation>应选D.

---

**2009年第13题 | 填空题 | 4分**

13. 设<equation>\alpha=(1,1,1)^{\mathrm{T}}</equation><equation>\beta=(1,0,k)^{\mathrm{T}}</equation>，若矩阵<equation>\alpha\beta^{\mathrm{T}}</equation>相似于<equation>\left( \begin{array}{c c c} {3} & {0} & {0} \\ {0} & {0} & {0} \\ {0} & {0} & {0} \end{array} \right)</equation>，则 k=___

**解析:**解（法一）计算得<equation>\boldsymbol{\alpha}\boldsymbol{\beta}^{\mathrm{T}}=\left( \begin{array}{c c c} 1 & 0 & k \\ 1 & 0 & k \\ 1 & 0 & k \end{array} \right).</equation>由于相似矩阵的迹相等，即其主对角线上元素之和相等，故<equation>1+0+k=3+0+0.</equation>因此，<equation>k = 2</equation>（法二）由于相似矩阵的特征值相等，故3是<equation>\alpha \beta^{\mathrm{T}} = \left( \begin{array}{c c c} 1 & 0 & k \\ 1 & 0 & k \\ 1 & 0 & k \end{array} \right)</equation>的特征值. 从而，<equation>\left| 3 E - \alpha \beta^ {\mathrm {T}} \right| = \left| \begin{array}{c c c} 2 & 0 & - k \\ - 1 & 3 & - k \\ - 1 & 0 & 3 - k \end{array} \right| = 3 \left| \begin{array}{c c} 2 & - k \\ - 1 & 3 - k \end{array} \right| = 3 (6 - 3 k) = 0.</equation>因此，<equation>k = 2</equation>（法三）计算<equation>\alpha\beta^{\mathrm{T}}</equation>的特征值.<equation>| \lambda E - \alpha \boldsymbol {\beta} ^ {\mathrm {T}} | = \left| \begin{array}{c c c} \lambda - 1 & 0 & - k \\ - 1 & \lambda & - k \\ - 1 & 0 & \lambda - k \end{array} \right| = \lambda \left| \begin{array}{c c} \lambda - 1 & - k \\ - 1 & \lambda - k \end{array} \right| = \lambda^ {2} [ \lambda - (k + 1) ].</equation>特征值为0,0,k+1.又由相似矩阵的特征值相等可知<equation>k + 1 = 3</equation>.因此，<equation>k = 2.</equation>

---


#### 特征值与特征向量

**2024年第15题 | 填空题 | 5分**

15. 设 A为3阶矩阵，<equation>A^{*}</equation>为的 A伴随矩阵，E为3阶单位矩阵，若<equation>r(2 E-A)=1,r(E+A)=2</equation>，则<equation>|A^{*}|=</equation>___

**答案:**## 16

**解析:**解 由于<equation>r ( 2 E-A )=1</equation>，故由系数矩阵的秩与解集的秩的关系可知，方程组<equation>( 2 E-A ) x=0</equation>有3-1=2个线性无关的解，从而矩阵A有两个线性无关的属于特征值2的特征向量.

同理，由于<equation>r ( E+A) = 2</equation>即<equation>r (-E-A)=2</equation>故由系数矩阵的秩与解集的秩的关系可知，方程组<equation>(-E-A) x=0</equation>有3-2=1个线性无关的解，从而矩阵A有一个线性无关的属于特征值-1的特征向量.

由于属于不同特征值的特征向量线性无关，故矩阵<equation>A</equation>至少有三个线性无关的特征向量.结合<equation>A</equation>是3阶矩阵可得，<equation>A</equation>共有三个线性无关的特征向量，从而<equation>A</equation>相似于对角矩阵<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & - 1 \end{array} \right)</equation><equation>A</equation>的特征值为2，2，-1，<equation>|A|=-4.</equation>由<equation>AA^{*} = |A|E</equation>可得，<equation>|AA^{*}| = |A| |A^{*}| = |A|^{3}</equation>，故<equation>|A^{*}| = |A|^{2} = 16.</equation>或者，由伴随矩阵与矩阵的特征值的关系可知，<equation>A^{*}</equation>的特征值为<equation>\frac{|A|}{2},\frac{|A|}{2},\frac{|A|}{-1}</equation>即-2，-2，

4. 因此，<equation>|A^{*}| = (-2)\times(-2)\times 4 = 16.</equation>

---

**2020年第6题 | 选择题 | 4分 | 答案: D**

6. 设 A为3阶矩阵，<equation>\alpha_{1},\alpha_{2}</equation>为 A的属于特征值1的线性无关的特征向量，<equation>\alpha_{3}</equation>为 A的属于特征值-1的特征向量，则满足<equation>P^{-1}AP=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>的可逆矩阵 P为（    ）

A.<equation>\left( \alpha_{1}+\alpha_{3},\alpha_{2},-\alpha_{3} \right)</equation>B.<equation>\left( \alpha_{1}+\alpha_{2},\alpha_{2},-\alpha_{3} \right)</equation>C.<equation>\left( \alpha_{1}+\alpha_{3},-\alpha_{3},\alpha_{2} \right)</equation>D.<equation>\left( \alpha_{1}+\alpha_{2},-\alpha_{3},\alpha_{2} \right)</equation>

答案: D

**解析:**解 由于<equation>P^{-1} A P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，故 P的列向量应分别为属于特征值1，-1，1的特征向量，且

第1列与第3列为属于特征值1的线性无关的特征向量.

由已知条件，<equation>\alpha_{3}</equation>为 A的属于特征值-1的特征向量，故 P的第2列可取为<equation>k\alpha_{3}</equation>其中 k为任意非零常数.

由于<equation>\alpha_{1},\alpha_{2}</equation>为 A的属于特征值1的线性无关的特征向量，且<equation>\left(\alpha_{1}+\alpha_{2},\alpha_{2}\right)=\left(\alpha_{1},\alpha_{2}\right)\left( \begin{array}{cc}1&0\\ 1&1 \end{array} \right)</equation>故<equation>\alpha_{1}+\alpha_{2}</equation>也为 A的属于特征值1的特征向量，且与<equation>\alpha_{2}</equation>线性无关.

因此，<equation>P</equation>可取为<equation>\left(\alpha_{1}+\alpha_{2},-\alpha_{3},\alpha_{2}\right).</equation>应选D.

---

**2018年第13题 | 填空题 | 4分**

13. 设 A为3阶矩阵，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>是线性无关的向量组. 若<equation>A\alpha_{1}=\alpha_{1}+\alpha_{2},A\alpha_{2}=\alpha_{2}+\alpha_{3},A\alpha_{3}=\alpha_{1}+\alpha_{3}</equation>，则<equation>|A|=</equation>

**解析:**解记<equation>P=(\alpha_{1},\alpha_{2},\alpha_{3})</equation>.由于<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关，故P可逆由题设可知，<equation>A P = A \left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) = \left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) \left( \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{array} \right) = P \left( \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{array} \right).</equation>记<equation>B=\left( \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{array} \right).</equation>.于是，<equation>A=P B P^{-1}.</equation>因此，<equation>| A | = | P | \cdot | B | \cdot | P ^ {- 1} | = | B | = \left| \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{array} \right| = 2.</equation>

---

**2015年第13题 | 填空题 | 4分**

13. 设 3 阶矩阵<equation>\boldsymbol{A}</equation>的特征值为 2,-2,1,<equation>\boldsymbol{B}=\boldsymbol{A}^{2}-\boldsymbol{A}+\boldsymbol{E}</equation>,其中<equation>\boldsymbol{E}</equation>为 3 阶单位矩阵,则行列式<equation>|\boldsymbol{B}|=</equation>___.

**解析:**解（法一）由于 A有3个不同的特征值，故 A有3个线性无关的特征向量，从而存在可逆矩阵 P使得<equation>P^{-1} A P=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>.于是<equation>\boldsymbol {A} = \boldsymbol {P} \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & - 2 & 0 \\ 0 & 0 & 1 \end{array} \right) \boldsymbol {P} ^ {- 1}, \quad \boldsymbol {A} ^ {2} = \boldsymbol {P} \left( \begin{array}{c c c} 2 ^ {2} & 0 & 0 \\ 0 & (- 2) ^ {2} & 0 \\ 0 & 0 & 1 ^ {2} \end{array} \right) \boldsymbol {P} ^ {- 1},</equation><equation>\boldsymbol {B} = \boldsymbol {P} \left( \begin{array}{c c c} 2 ^ {2} - 2 + 1 & 0 & 0 \\ 0 & (- 2) ^ {2} - (- 2) + 1 & 0 \\ 0 & 0 & 1 ^ {2} - 1 + 1 \end{array} \right) \boldsymbol {P} ^ {- 1} = \boldsymbol {P} \left( \begin{array}{c c c} 3 & 0 & 0 \\ 0 & 7 & 0 \\ 0 & 0 & 1 \end{array} \right) \boldsymbol {P} ^ {- 1}.</equation>因此，<equation>|\boldsymbol{B}| = 21\cdot |\boldsymbol{P}| \cdot |\boldsymbol{P}^{-1}| = 21.</equation>（法二）设<equation>\alpha</equation>为矩阵<equation>A</equation>的属于特征值<equation>\lambda</equation>的特征向量，即<equation>A\alpha = \lambda \alpha</equation>，则<equation>\boldsymbol {B} \alpha = \left(\boldsymbol {A} ^ {2} - \boldsymbol {A} + \boldsymbol {E}\right) \alpha = \left(\lambda^ {2} - \lambda + 1\right) \alpha .</equation>由上可见，若<equation>\alpha</equation>为<equation>A</equation>的属于特征值<equation>\lambda</equation>的特征向量，则<equation>\alpha</equation>为<equation>B</equation>的属于特征值<equation>\lambda^2 - \lambda +1</equation>的特征向量.<equation>A</equation>的3个线性无关的特征向量也是<equation>B</equation>的3个线性无关的特征向量，对应的特征值为<equation>\lambda^2 - \lambda +1</equation>（<equation>\lambda = 2,-2,1</equation>）.由此可求得<equation>B</equation>的特征值为3,7,1.

因此，<equation>|B| = 3\times 7\times 1 = 21.</equation>

---

**2011年第21题 | 解答题 | 11分**


设<equation>A</equation>为3阶实对称矩阵，<equation>A</equation>的秩为2，且<equation>1 \left( \begin{array}{c c} 1 & 1 \\ 0 & 0 \\ - 1 & 1 \end{array} \right) = \left( \begin{array}{c c} - 1 & 1 \\ 0 & 0 \\ 1 & 1 \end{array} \right)</equation>I. 求 A的所有特征值与特征向量；

II. 求矩阵 A.

**答案:**(21) （I）特征值-1，1，0，分别对应特征向量<equation>k_{1}(1,0,-1)^{\mathrm{T}}, k_{2}(1,0,1)^{\mathrm{T}}, k_{3}(0,1,0)^{\mathrm{T}}</equation>，其中<equation>k_{1}, k_{2},</equation><equation>k_{3}</equation>为任意非零常数；（Ⅱ）<equation>\left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{array} \right).</equation>

**解析:**解（I）由于<equation>A\left( \begin{array}{c c} 1 & 1 \\ 0 & 0 \\ - 1 & 1 \end{array} \right)=\left( \begin{array}{c c} - 1 & 1 \\ 0 & 0 \\ 1 & 1 \end{array} \right)</equation>，故<equation>\alpha_{1}=(1,0,-1)^{\mathrm{T}}</equation>，<equation>\alpha_{2}=(1,0,1)^{\mathrm{T}}</equation>满足<equation>A\alpha_{1}=</equation><equation>-\alpha_{1},A\alpha_{2}=\alpha_{2}</equation>，从而<equation>\alpha_{1}</equation>为A的属于特征值-1的一个特征向量，<equation>\alpha_{2}</equation>为A的属于特征值1的一个特征向量.

又因为<equation>r(\mathbf{A}) = 2</equation>，<equation>|\mathbf{A}| = 0</equation>，所以<equation>\mathbf{A}</equation>还有一个特征值为零.

因为实对称矩阵属于不同特征值的特征向量相互正交，所以 A的属于特征值0的特征向量<equation>\boldsymbol{\alpha}_{3}=(x_{1},x_{2},x_{3})^{\mathrm{T}}</equation>满足<equation>\boldsymbol{\alpha}_{1}^{\mathrm{T}}\boldsymbol{\alpha}_{3}=0</equation><equation>\boldsymbol{\alpha}_{2}^{\mathrm{T}}\boldsymbol{\alpha}_{3}=0</equation>从而得<equation>\left\{ \begin{array}{l l} x_{1}-x_{3}=0, \\ x_{1}+x_{3}=0. \end{array} \right.</equation>由此可得<equation>\boldsymbol{\alpha}_{3}=k_{3}(0,1,0)^{\mathrm{T}}</equation>其中<equation>k_{3}</equation>为任意非零常数.

因此，<equation>\mathbf{A}</equation>的特征值为-1,1,0.对应的特征向量分别为<equation>k_{1}(1,0,-1)^{\mathrm{T}}</equation><equation>k_{2}(1,0,1)^{\mathrm{T}}</equation><equation>k_{3}(0,1,0)^{\mathrm{T}}</equation>其中<equation>k_{1},k_{2},k_{3}</equation>为任意非零常数.

（Ⅱ）（法一）由第（I）问可知，取<equation>P=\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)=\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \\ -1 & 1 & 0 \end{array} \right)</equation>，可得<equation>P^{-1}AP=</equation><equation>\left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>于是<equation>A=P\left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right) P^{-1}.</equation>利用初等变换法计算<equation>P^{-1}.</equation><equation>\begin{array}{l} (P, E) = \left( \begin{array}{c c c c c c} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 1 & 0 \\ - 1 & 1 & 0 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} + r _ {1}} \left( \begin{array}{c c c c c c} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 1 & 0 \\ 0 & 2 & 0 & 1 & 0 & 1 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {*} \times \frac {1}{2}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & \frac {1}{2} & 0 & - \frac {1}{2} \\ 0 & 0 & 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & \frac {1}{2} & 0 & \frac {1}{2} \end{array} \right) \xrightarrow {r _ {2} \leftrightarrow r _ {3} ^ {* *}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & \frac {1}{2} & 0 & - \frac {1}{2} \\ 0 & 1 & 0 & \frac {1}{2} & 0 & \frac {1}{2} \\ 0 & 0 & 1 & 0 & 1 & 0 \end{array} \right). \\ \end{array}</equation>于是，<equation>P^{-1} = \left( \begin{array}{c c c} \frac{1}{2} & 0 & -\frac{1}{2} \\ \frac{1}{2} & 0 & \frac{1}{2} \\ 0 & 1 & 0 \end{array} \right).</equation>因此，<equation>\begin{aligned} \boldsymbol {A} &= \boldsymbol {P} \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \boldsymbol {P} ^ {- 1} &= \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \\ - 1 & 1 & 0  \right) \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \left( \begin{array}{c c c} \frac {1}{2} & 0 & - \frac {1}{2} \\ \frac {1}{2} & 0 & \frac {1}{2} \\ 0 & 1 & 0  \right) \\ &= \left( \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & 0 & 0 \\ 1 & 1 & 0  \right) \left( \begin{array}{c c c} \frac {1}{2} & 0 & - \frac {1}{2} \\ \frac {1}{2} & 0 & \frac {1}{2} \\ 0 & 1 & 0  \right) &= \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0  \right). \end{aligned}</equation>或者，由<equation>A P = \left(A \alpha_ {1}, A \alpha_ {2}, A \alpha_ {3}\right) = \left(- \alpha_ {1}, \alpha_ {2}, 0\right)</equation>可得，<equation>\boldsymbol {A} = \left(- \alpha_ {1}, \alpha_ {2}, 0\right) \boldsymbol {P} ^ {- 1} = - \frac {1}{2} \left( \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & 0 & 0 \\ 1 & 1 & 0 \end{array} \right) \left( \begin{array}{c c c} - 1 & 0 & 1 \\ - 1 & 0 & - 1 \\ 0 & - 2 & 0 \end{array} \right) = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{array} \right).</equation>（法二）将<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>单位化，组成一正交矩阵<equation>Q = \left( \begin{array}{c c c} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0 \\ 0 & 0 & 1 \\ -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0 \end{array} \right)</equation>，则<equation>Q^{\mathrm{T}}AQ = \left( \begin{array}{c c c} -1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>.

因此，<equation>\begin{aligned} \boldsymbol {A} &= \boldsymbol {Q} \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \boldsymbol {Q} ^ {\mathrm {T}} &= \left( \begin{array}{c c c} \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {2}} & 0 \\ 0 & 0 & 1 \\ - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {2}} & 0  \right) \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \left( \begin{array}{c c c} \frac {1}{\sqrt {2}} & 0 & - \frac {1}{\sqrt {2}} \\ \frac {1}{\sqrt {2}} & 0 & \frac {1}{\sqrt {2}} \\ 0 & 1 & 0  \right) \\ &= \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0  \right). \end{aligned}</equation>

---

**2010年第21题 | 解答题 | 11分**

21. (本题满分11分)

设<equation>A=\left( \begin{array}{c c c} 0 & -1 & 4 \\ -1 & 3 & a \\ 4 & a & 0 \end{array} \right)</equation>，正交矩阵Q使<equation>Q^{\mathrm{T}}AQ</equation>为对角矩阵，若Q的第1列为<equation>\frac{1}{\sqrt{6}}(1,2,1)^{\mathrm{T}}</equation>，求a和Q.

**答案:**<equation>a = - 1, Q = \left( \begin{array}{c c c} \frac {1}{\sqrt {6}} & - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {3}} \\ \frac {2}{\sqrt {6}} & 0 & - \frac {1}{\sqrt {3}} \\ \frac {1}{\sqrt {6}} & \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {3}} \end{array} \right), Q ^ {\mathrm {T}} A Q = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & - 4 & 0 \\ 0 & 0 & 5 \end{array} \right).</equation>

**解析:**解 由题设知，<equation>\alpha_{1}=\frac{1}{\sqrt{6}}(1,2,1)^{\mathrm{T}}</equation>为 A的一个特征向量.不妨设<equation>\alpha_{1}</equation>对应的特征值为 k，则<equation>\begin{aligned} \boldsymbol {A} \boldsymbol {\alpha} _ {1} &= \frac {1}{\sqrt {6}} \left( \begin{array}{c c c} 0 & - 1 & 4 \\ - 1 & 3 & a \\ 4 & a & 0  \right) \left(  1 \\ 2 \\ 1  \right) &= \frac {1}{\sqrt {6}} \left( \begin{array}{c} 2 \\ 5 + a \\ 4 + 2 a  \right) &= \frac {k}{\sqrt {6}} \left(  1 \\ 2 \\ 1  \right). \end{aligned}</equation>从而<equation>\left\{ \begin{array}{l}2 = k,\\ 5 + a = 2k,\\ 4 + 2a = k, \end{array} \right.</equation>解得<equation>a = -1</equation>，<equation>k = 2.</equation>于是，<equation>A = \left( \begin{array}{c c c}0 & -1 & 4\\ -1 & 3 & -1\\ 4 & -1 & 0 \end{array} \right).</equation>计算 A的特征多项式得<equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda & 1 & - 4 \\ 1 & \lambda - 3 & 1 \\ - 4 & 1 & \lambda \end{array} \right| = (\lambda - 2) (\lambda - 5) (\lambda + 4).</equation>因此，<equation>A</equation>的特征值为2，5，-4.<equation>\alpha_{1}</equation>是<equation>A</equation>的属于特征值2的特征向量.

先求属于特征值-4的单位特征向量<equation>\alpha_{2}</equation>.由特征向量的定义可知，<equation>(-4E - A)x = 0.</equation><equation>\begin{array}{l} - 4 E - A = \left( \begin{array}{c c c} - 4 & 1 & - 4 \\ 1 & - 7 & 1 \\ - 4 & 1 & - 4 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c} - 4 & 1 & - 4 \\ 1 & - 7 & 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} + 4 r _ {2}} \left( \begin{array}{c c c} 0 & 1 & 0 \\ 1 & - 7 & 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} + 7 r _ {1} ^ {* *}} \binom {1} {r _ {1} ^ {* *} \leftrightarrow r _ {2} ^ {*}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>由此可得<equation>\left\{\begin{array}{l l}x_{1}+x_{3}=0,\\ x_{2}=0,\end{array}\right.</equation>故<equation>\boldsymbol{\xi}_{2}=(-1,0,1)^{\mathrm{T}}</equation>为该方程组的一个基础解系.将<equation>\boldsymbol{\xi}_{2}</equation>单位化得<equation>\boldsymbol{\alpha}_{2}=</equation><equation>\frac{1}{\sqrt{2}}(-1,0,1)^{\mathrm{T}}.</equation>同理，解（5E-A）<equation>x=0.</equation><equation>\begin{array}{l} 5 E - A = \left( \begin{array}{c c c} 5 & 1 & - 4 \\ 1 & 2 & 1 \\ - 4 & 1 & 5 \end{array} \right) \xrightarrow {r _ {3} + r _ {1} - r _ {2}} \left( \begin{array}{c c c} 5 & 1 & - 4 \\ 1 & 2 & 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} - 5 r _ {2}} \left( \begin{array}{c c c} 0 & 1 & 1 \\ 1 & 2 & 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} - r _ {1} ^ {* *}} \frac {1}{r _ {1} ^ {* *} \leftrightarrow r _ {2} ^ {*}} \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>由此可得<equation>\left\{\begin{array}{l l}x_{1}+x_{2}=0,\\ x_{2}+x_{3}=0,\end{array} \right.</equation>故<equation>\boldsymbol{\xi}_{3}=(1,-1,1)^{\mathrm{T}}</equation>为该方程组的一个基础解系.将<equation>\boldsymbol{\xi}_{3}</equation>单位化得<equation>\boldsymbol{\alpha}_{3}=</equation><equation>\frac{1}{\sqrt{3}}(1,-1,1)^{\mathrm{T}}.</equation>或者也可以如下求<equation>\boldsymbol{\alpha}_{3}.</equation>由于<equation>\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2}</equation>为属于不同特征值的特征向量，故它们相互正交.于是<equation>\boldsymbol {\alpha} _ {3} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {1} = 0, \quad \boldsymbol {\alpha} _ {3} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {2} = 0.</equation><equation>\pmb{\alpha}_{3}</equation>的坐标<equation>(x_{1}, x_{2}, x_{3})^{\mathrm{T}}</equation>满足<equation>\left\{ \begin{array}{l} x_{1} + 2x_{2} + x_{3} = 0, \\ x_{1} - x_{3} = 0. \end{array} \right.</equation>因此可得<equation>\pmb{\xi}_{3} = (1, -1, 1)^{\mathrm{T}}</equation>为该方程组的一个基础解系.将<equation>\pmb{\xi}_{3}</equation>单位化得<equation>\pmb{\alpha}_{3} = \frac{1}{\sqrt{3}} (1, -1, 1)^{\mathrm{T}}.</equation>综上所述，<equation>a = -1</equation>，<equation>Q = \left( \begin{array}{c c c} \frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} \\ \frac{2}{\sqrt{6}} & 0 & -\frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{6}} & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} \end{array} \right)</equation>，<equation>Q^{\mathrm{T}}AQ = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -4 & 0 \\ 0 & 0 & 5 \end{array} \right)</equation>

---


### 二次型

**2025年第7题 | 选择题 | 5分 | 答案: B**

7. 设矩阵<equation>A=\left( \begin{array}{c c}1&2\\ -2&-a \end{array} \right), B=\left( \begin{array}{c c}1&0\\ 1&a \end{array} \right),</equation>若 f(x,y) =<equation>| x A+y B |</equation>是正定二次型，则 a的取值范围是（    )

A.<equation>( 0,2-\sqrt{3} )</equation>B.<equation>( 2-\sqrt{3},2+\sqrt{3} )</equation>C.<equation>( 2+\sqrt{3},4 )</equation>D.<equation>( 0,4 )</equation>

答案: B

**解析:**解 由于<equation>A=\left( \begin{array}{cc}1&2\\ -2&-a \end{array} \right), B=\left( \begin{array}{cc}1&0\\ 1&a \end{array} \right),</equation>故<equation>xA+yB=\left( \begin{array}{cc}x+y&2x\\ -2x+y&a(y-x) \end{array} \right).</equation>进一步可得<equation>\mid xA+yB\mid =\left| \begin{array}{cc}x+y&2x\\ -2x+y&a(y-x) \end{array} \right|=a\left(y^{2}-x^{2}\right)+4x^{2}-2xy=(4-a)x^{2}+ay^{2}-2xy.</equation>于是，二次型<equation>f(x,y)</equation>对应的对称矩阵<equation>C=\left( \begin{array}{cc}4-a&-1\\ -1&a \end{array} \right).</equation>由于<equation>f(x,y)</equation>是正定二次型，故C的各阶顺序主子式均为正数，即<equation>4-a>0, |C|=4a-a^{2}-1</equation>>0.联立<equation>\left\{ \begin{array}{l l}4-a>0,\\ a^{2}-4a+1<0, \end{array} \right.</equation>解<equation>a^{2}-4a+1<0</equation>可得<equation>2-\sqrt{3}<a<2+\sqrt{3},</equation>与a<4取交集可得a<equation>\in(2-\sqrt{3},2+\sqrt{3}).</equation>因此，应选B.

---

**2024年第5题 | 选择题 | 5分 | 答案: C**

5. 设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=\boldsymbol{x}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{x}</equation>在正交变换下可化成<equation>y_{1}^{2}-2 y_{2}^{2}+3 y_{3}^{2}</equation>，则二次型 f的矩阵 A的行列式与迹分别为（    ）

A. -6,-2 B. 6,-2 C. -6,2 D. 6,2

答案: C

**解析:**解 由于二次型<equation>f ( x_{1}, x_{2}, x_{3} )=x^{\mathrm{T}} A x</equation>在正交变换下可化为<equation>y_{1}^{2}-2 y_{2}^{2}+3 y_{3}^{2}</equation>故其对应的对称矩阵 A的特征值为1，-2，3，从而 A的行列式<equation>| A |=1 \times(-2) \times 3=-6</equation>，迹<equation>\operatorname{t r} ( A )=1-2+3=2.</equation>因此，应选C.

---

**2023年第6题 | 选择题 | 5分 | 答案: B**

6. 二次型<equation>f \left(x_{1}, x_{2}, x_{3}\right)=\left(x_{1}+x_{2}\right)^{2}+\left(x_{1}+x_{3}\right)^{2}-4\left(x_{2}-x_{3}\right)^{2}</equation>的规范形为（    )

A.<equation>y_{1}^{2}+y_{2}^{2}</equation>B.<equation>y_{1}^{2}-y_{2}^{2}</equation>C.<equation>y_{1}^{2}+y_{2}^{2}-4 y_{3}^{2}</equation>D.<equation>y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>

答案: B

**解析:**解 （法一）将<equation>f ( x_{1}, x_{2}, x_{3} )</equation>展开可得<equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = 2 x _ {1} ^ {2} - 3 x _ {2} ^ {2} - 3 x _ {3} ^ {2} + 2 x _ {1} x _ {2} + 2 x _ {1} x _ {3} + 8 x _ {2} x _ {3}.</equation>该二次型对应的矩阵为<equation>A=\left( \begin{array}{c c c} 2 & 1 & 1 \\ 1 & -3 & 4 \\ 1 & 4 & -3 \end{array} \right).</equation>计算可得<equation>| A | = \left| \begin{array}{c c c} 2 & 1 & 1 \\ 1 & - 3 & 4 \\ 1 & 4 & - 3 \end{array} \right| \xlongequal {r _ {2} + r _ {3}} \left| \begin{array}{c c c} 2 & 1 & 1 \\ 2 & 1 & 1 \\ 1 & 4 & - 3 \end{array} \right| = 0.</equation>由于<equation>| A|=0</equation>，故 A有零特征值，从而<equation>r(A)\leqslant 2</equation>，f的正、负惯性指数之和不超过2.

若 f的负惯性指数为0，则 f非负，即对任意<equation>\left(x_{1},x_{2},x_{3}\right)</equation>，均有<equation>f\left(x_{1},x_{2},x_{3}\right)\geqslant 0</equation>.但是，<equation>f(0,0,1)=0+1-4=-3<0</equation>，矛盾.同理，若 f的正惯性指数为0，则 f非正，即对任意<equation>\left(x_{1},x_{2},x_{3}\right)</equation>，均有<equation>f\left(x_{1},x_{2},x_{3}\right)\leqslant 0</equation>.但是，<equation>f(1,0,0)=1+1-0=2>0</equation>，矛盾.

由于 f的正、负惯性指数之和不超过2，而正、负惯性指数又均大于0，故其正、负惯性指数均为 1. 应选B.

（法二）记<equation>\left\{ \begin{array}{l l l} y_{1} = x_{1} + x_{2}, \\ y_{2} = x_{1} + x_{3}, \\ y_{3} = x_{2} - x_{3}, \end{array} \right.</equation><equation>P = \left( \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & -1 \end{array} \right)</equation>，则<equation>\left( \begin{array}{l} y_{1} \\ y_{2} \\ y_{3} \end{array} \right) = P \left( \begin{array}{l} x_{1} \\ x_{2} \\ x_{3} \end{array} \right)</equation>.

记<equation>\boldsymbol{\Lambda}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & - 4 \end{array} \right)</equation>，则由<equation>f \left( x_{1}, x_{2}, x_{3}\right) = \left(x_{1}+x_{2}\right)^{2}+\left(x_{1}+x_{3}\right)^{2}-4\left(x_{2}-x_{3}\right)^{2}</equation>可知，<equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = y ^ {\mathrm {T}} \Lambda y \xlongequal {y = P x} x ^ {\mathrm {T}} P ^ {\mathrm {T}} \Lambda P x.</equation>于是，<equation>A=P^{\mathrm{T}}\Lambda P</equation>为二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>对应的对称矩阵.

又因为<equation>| P | = \left| \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & - 1 \end{array} \right| = 0</equation>，所以<equation>| A | = 0</equation>，从而A有零特征值.

其余同法一.

（法三）令<equation>\left\{ \begin{array}{l l} y_{1}=x_{1}+x_{2}, \\ y_{2}=x_{1}+x_{3}, \\ y_{3}=x_{3}, \end{array} \right.</equation>则<equation>x_{2}-x_{3}=y_{1}-y_{2}</equation>，且该变换为可逆线性变换.在该变换下，二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>化为<equation>\begin{aligned} g \left(y _ {1}, y _ {2}, y _ {3}\right) &= y _ {1} ^ {2} + y _ {2} ^ {2} - 4 \left(y _ {1} - y _ {2}\right) ^ {2} = - 3 y _ {1} ^ {2} - 3 y _ {2} ^ {2} + 8 y _ {1} y _ {2} \\ &= - 3 y _ {1} ^ {2} + 3 \cdot \frac {8}{3} y _ {1} y _ {2} - 3 y _ {2} ^ {2} = - 3 \left(y _ {1} - \frac {4}{3} y _ {2}\right) ^ {2} - 3 y _ {2} ^ {2} + \frac {1 6}{3} y _ {2} ^ {2} \\ &= - 3 \left(y _ {1} - \frac {4}{3} y _ {2}\right) ^ {2} + \frac {7}{3} y _ {2} ^ {2}. \end{aligned}</equation>再令<equation>\left\{ \begin{array}{l l} z_{1}=y_{1}-\frac{4}{3} y_{2}, \\ z_{2}=y_{2}, \\ z_{3}=y_{3}, \end{array} \right.</equation>该变换为可逆线性变换.在该变换下，二次型<equation>g(y_{1},y_{2},y_{3})</equation>化为<equation>h \left(z _ {1}, z _ {2}, z _ {3}\right) = - 3 z _ {1} ^ {2} + \frac {7}{3} z _ {2} ^ {2}.</equation>因此，<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>的一个标准形为<equation>- 3 z_{1}^{2}+\frac{7}{3} z_{2}^{2}</equation>，其正、负惯性指数均为1.应选B.

---

**2022年第21题 | 解答题 | 12分**

（本题满分12分）

已知二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=3 x_{1}^{2}+4 x_{2}^{2}+3 x_{3}^{2}+2 x_{1} x_{3}</equation>.

I. 求正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>将<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>化为标准形；

II. 证明：<equation>\min_{x\neq0}\frac{f(x)}{x^{\mathrm{T}}x}=2.</equation>

**答案:**（I）<equation>Q=\left( \begin{array}{c c c} \frac{1}{\sqrt{2}} & 0 & -\frac{1}{\sqrt{2}} \\ 0 & 1 & 0 \\ \frac{1}{\sqrt{2}} & 0 & \frac{1}{\sqrt{2}} \end{array} \right)</equation>，正交变换<equation>x=Qy</equation>将二次型f化为标准形<equation>4y_{1}^{2}+4y_{2}^{2}+2y_{3}^{2};</equation>（Ⅱ）证明略.

**解析:**解（I）由 f的表达式可得 f对应的矩阵 A =<equation>\left( \begin{array}{c c c} 3 & 0 & 1 \\ 0 & 4 & 0 \\ 1 & 0 & 3 \end{array} \right).</equation>计算 A的特征多项式.<equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda - 3 & 0 & - 1 \\ 0 & \lambda - 4 & 0 \\ - 1 & 0 & \lambda - 3 \end{array} \right| = (\lambda - 4) \left[ (\lambda - 3) ^ {2} - 1 \right] = (\lambda - 4) ^ {2} (\lambda - 2).</equation>A的特征值为4,4,2.

分别计算 A的属于特征值4和2的特征向量.

考虑（4E-A）x=0.<equation>4 E - A = \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 0 & 0 \\ - 1 & 0 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation><equation>\xi_{1}=\left( \begin{array}{c}1\\ 0\\ 1 \end{array} \right)</equation>和<equation>\xi_{2}=\left( \begin{array}{c}0\\ 1\\ 0 \end{array} \right)</equation>为 A的属于特征值4的两个线性无关的特征向量.考虑<equation>( 2 E-A ) x=0</equation>考虑（2E-A）x=0.<equation>2 E - A = \left( \begin{array}{c c c} - 1 & 0 & - 1 \\ 0 & - 2 & 0 \\ - 1 & 0 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation><equation>\xi_{3}=\left( \begin{array}{c}-1\\ 0\\ 1 \end{array} \right)</equation>为 A的属于特征值2的一个特征向量.

由于<equation>\xi_{1},\xi_{2},\xi_{3}</equation>相互正交，故只需将它们各自单位化即可得一组相互正交的单位特征向量.<equation>\boldsymbol {\varepsilon} _ {1} = \frac {\boldsymbol {\xi} _ {1}}{\| \boldsymbol {\xi} _ {1} \|} = \frac {1}{\sqrt {2}} \binom {1} {1}, \quad \boldsymbol {\varepsilon} _ {2} = \frac {\boldsymbol {\xi} _ {2}}{\| \boldsymbol {\xi} _ {2} \|} = \binom {0} {1}, \quad \boldsymbol {\varepsilon} _ {3} = \frac {\boldsymbol {\xi} _ {3}}{\| \boldsymbol {\xi} _ {3} \|} = \frac {1}{\sqrt {2}} \binom {- 1} {0}</equation>令<equation>Q=(\varepsilon_{1},\varepsilon_{2},\varepsilon_{3})</equation>，可得<equation>Q^{-1}AQ=Q^{\mathrm{T}}AQ=\left( \begin{array}{c c c} 4 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>，即正交变换<equation>x=Qy</equation>将二次型f化为标准形<equation>4y_{1}^{2}+4y_{2}^{2}+2y_{3}^{2}.</equation>（Ⅱ）由第（Ⅰ）问可知，在正交变换<equation>x=Q y</equation>下，<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>的标准形为<equation>4 y_{1}^{2}+4 y_{2}^{2}+2 y_{3}^{2}.</equation>又因为<equation>\boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {x} = \left(Q \boldsymbol {y}\right) ^ {\mathrm {T}} Q \boldsymbol {y} = \boldsymbol {y} ^ {\mathrm {T}} Q ^ {\mathrm {T}} Q \boldsymbol {y} \xlongequal {Q ^ {\mathrm {T}} Q = E} \boldsymbol {y} ^ {\mathrm {T}} \boldsymbol {y} = y _ {1} ^ {2} + y _ {2} ^ {2} + y _ {3} ^ {2},</equation>所以对<equation>x\neq 0</equation><equation>\frac {f (\boldsymbol {x})}{\boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {x}} \xlongequal {\boldsymbol {x} = Q \boldsymbol {y}} \frac {4 y _ {1} ^ {2} + 4 y _ {2} ^ {2} + 2 y _ {3} ^ {2}}{y _ {1} ^ {2} + y _ {2} ^ {2} + y _ {3} ^ {2}} \geqslant \frac {2 y _ {1} ^ {2} + 2 y _ {2} ^ {2} + 2 y _ {3} ^ {2}}{y _ {1} ^ {2} + y _ {2} ^ {2} + y _ {3} ^ {2}} = 2.</equation>取<equation>y_{0}</equation>满足<equation>y_{1} = y_{2} = 0, y_{3} \neq 0, x_{0} = Qy_{0}</equation>，即<equation>x_{0} = y_{3}\varepsilon_{3}</equation>时，可得<equation>\frac{f\left(x_0\right)}{x_0^{\mathrm{T}}x_0} = 2.</equation>因此，<equation>\min_{x\neq0}\frac{f(x)}{x^{\mathrm{T}}x}=2.</equation>

---

**2021年第5题 | 选择题 | 5分 | 答案: B**

5. 二次型<equation>f \left(x_{1}, x_{2}, x_{3}\right)=\left(x_{1}+x_{2}\right)^{2}+\left(x_{2}+x_{3}\right)^{2}-\left(x_{3}-x_{1}\right)^{2}</equation>的正惯性指数与负惯性指数依次为（    )

A. 2,0 B. 1,1 C. 2,1 D. 1,2

答案: B

**解析:**解（法一）令<equation>\left\{ \begin{array}{l l} y_{1}=x_{1}+x_{2}, \\ y_{2}=x_{2}+x_{3}, \\ y_{3}=x_{3}, \end{array} \right.</equation>则<equation>x_{3}-x_{1}=y_{2}-y_{1}</equation>，且该变换为可逆线性变换.在该变换下，二次型<equation>f(x_{1},x_{2},x_{3})</equation>化为<equation>g \left(y _ {1}, y _ {2}, y _ {3}\right) = y _ {1} ^ {2} + y _ {2} ^ {2} - \left(y _ {2} - y _ {1}\right) ^ {2} = 2 y _ {1} y _ {2}.</equation>再令<equation>\left\{ \begin{array}{l l} y_{1}=z_{1}+z_{2}, \\ y_{2}=z_{1}-z_{2}, \\ y_{3}=z_{3}, \end{array} \right.</equation>则<equation>g \left( y_{1}, y_{2}, y_{3} \right)</equation>化为<equation>h \left(z _ {1}, z _ {2}, z _ {3}\right) = 2 \left(z _ {1} + z _ {2}\right) \left(z _ {1} - z _ {2}\right) = 2 z _ {1} ^ {2} - 2 z _ {2} ^ {2}.</equation>因此，<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>的一个标准形为<equation>2z_{1}^{2}-2z_{2}^{2}</equation>其正、负惯性指数分别为1，1.应选B.

（法二）将<equation>f(x_{1},x_{2},x_{3})</equation>展开可得<equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = 2 x _ {2} ^ {2} + 2 x _ {1} x _ {2} + 2 x _ {2} x _ {3} + 2 x _ {1} x _ {3}.</equation>该二次型对应的矩阵为<equation>A=\left( \begin{array}{c c c} 0 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 0 \end{array} \right)</equation>. 不难发现，A的第二行为第一行与第三行的和，故<equation>r(A)\leqslant 2</equation>. 又因为A有一个2阶非零子式<equation>\left| \begin{array}{c c} 0 & 1 \\ 1 & 2 \end{array} \right|</equation>，所以<equation>r(A)\geqslant 2</equation>. 于是，<equation>r(A)=2.</equation>由于二次型的正、负惯性指数之和等于其对应矩阵的秩，而选项C、D的两数之和均为3，故可排除选项C、D.

另一方面，若 f的负惯性指数为0，则 f非负，即对任意<equation>\left(x_{1},x_{2},x_{3}\right)</equation>，均有<equation>f\left(x_{1},x_{2},x_{3}\right)\geqslant 0.</equation>但是，<equation>f(1,0,-1)=1+1-4<0</equation>矛盾.因此，选项A不正确.

根据排除法，应选B.

---

**2020年第20题 | 解答题 | 11分**

20. (本题满分11分)

设二次型<equation>f \left( x_{1}, x_{2} \right)=x_{1}^{2}-4 x_{1} x_{2}+4 x_{2}^{2}</equation>经正交变换<equation>\binom{x_{1}}{x_{2}}=Q \binom{y_{1}}{y_{2}}</equation>化为二次型<equation>g \left( y_{1}, y_{2} \right)=a y_{1}^{2}+4 y_{1} y_{2}+b y_{2}^{2}</equation>其中 a≥b.

I. 求 a,b的值;

II. 求正交矩阵 Q.

**答案:**（ I ）<equation>a=4,b=1;</equation>（Ⅱ）<equation>Q = \left( \begin{array}{c c} - \frac{4}{5} & \frac{3}{5} \\ \frac{3}{5} & \frac{4}{5} \end{array} \right), f \left(x_{1}, x_{2}\right)</equation>经过正交变换<equation>\binom{x_1}{x_2} = Q \binom{y_1}{y_2}</equation>化为二次型<equation>g \left(y_{1}, y_{2}\right).</equation>

**解析:**解（I）写出二次型<equation>f ( x_{1}, x_{2} )=x_{1}^{2}-4 x_{1} x_{2}+4 x_{2}^{2}</equation>对应的矩阵 A，二次型<equation>g ( y_{1}, y_{2} )=a y_{1}^{2}+</equation><equation>4 y_{1} y_{2}+b y_{2}^{2}</equation>对应的矩阵 B.<equation>\boldsymbol {A} = \left( \begin{array}{c c} 1 & - 2 \\ - 2 & 4 \end{array} \right), \quad \boldsymbol {B} = \left( \begin{array}{c c} a & 2 \\ 2 & b \end{array} \right).</equation>由于正交变换也是相似变换，故 A与 B相似。又因为相似的矩阵具有相同的迹与行列式，所以<equation>\left\{ \begin{array}{l} a + b = 5, \\ a b = 4. \end{array} \right.</equation>由 a<equation>\geqslant b</equation>可确定<equation>\left\{ \begin{array}{l l} a=4, \\ b=1. \end{array} \right.</equation>（Ⅱ）由第（Ⅰ）问可知，<equation>A=\left( \begin{array}{cc}1&-2\\ -2&4 \end{array} \right), B=\left( \begin{array}{cc}4&2\\ 2&1 \end{array} \right).</equation>计算 A和B的特征多项式可得<equation>|\lambda E - A| = \left| \begin{array}{cc}\lambda -1 & 2\\ 2 & \lambda -4 \end{array} \right| = \lambda (\lambda -5).</equation>于是 A和B的特征值为5和0.分别计算 A,B的特征向量.

计算 A的属于特征值5的特征向量.

考虑（5E-A）x=0.<equation>5 E - A = \left( \begin{array}{c c} 4 & 2 \\ 2 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c} 2 & 1 \\ 0 & 0 \end{array} \right).</equation>于是，<equation>r ( 5 E-A )=1</equation>，求得<equation>\xi_{1}=(-1,2)^{\mathrm{T}}</equation>为（5E-A）<equation>\boldsymbol{x}=\mathbf{0}</equation>的一个基础解系.<equation>(-1,2)^{\mathrm{T}}</equation>为A的属于特征值5的一个特征向量.

计算 A的属于特征值0的特征向量.

考虑（0E-A）x=0.<equation>- \boldsymbol {A} = \left( \begin{array}{c c} - 1 & 2 \\ 2 & - 4 \end{array} \right) \rightarrow \left( \begin{array}{c c} - 1 & 2 \\ 0 & 0 \end{array} \right).</equation>于是，<equation>r ( 0 E-A)=1</equation>，求得<equation>\boldsymbol{\xi}_{2}=(2,1)^{\mathrm{T}}</equation>为<equation>( 0 E-A ) x=0</equation>的一个基础解系.<equation>( 2,1)^{\mathrm{T}}</equation>为 A的属于特征值0的一个特征向量.

取<equation>P_{1} = \left( \begin{array}{cc} -1 & 2 \\ 2 & 1 \end{array} \right)</equation>，则<equation>P_{1}^{-1}AP_{1} = \left( \begin{array}{cc} 5 & 0 \\ 0 & 0 \end{array} \right)</equation>.

计算 B的属于特征值5的特征向量.

考虑（5E-B）x=0.<equation>5 E - B = \left( \begin{array}{c c} 1 & - 2 \\ - 2 & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c} 1 & - 2 \\ 0 & 0 \end{array} \right).</equation>于是，<equation>r ( 5 E-B )=1</equation>，求得<equation>\eta_{1}=(2,1)^{\mathrm{T}}</equation>为（5E-B）<equation>x=0</equation>的一个基础解系.<equation>(2,1)^{\mathrm{T}}</equation>为B的属于特征值5的一个特征向量.

计算 B的属于特征值0的特征向量.

考虑（0E-B）x=0.<equation>- \boldsymbol {B} = \left( \begin{array}{c c} - 4 & - 2 \\ - 2 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c} 2 & 1 \\ 0 & 0 \end{array} \right).</equation>于是，<equation>r ( 0 E-B )=1</equation>，求得<equation>\eta_{2}=(-1,2)^{\mathrm{T}}</equation>为<equation>( 0 E-B ) x=0</equation>的一个基础解系.<equation>(-1,2)^{\mathrm{T}}</equation>为B的属于特征值0的一个特征向量.

取<equation>P_{2} = \left( \begin{array}{cc}2 & -1\\ 1 & 2 \end{array} \right)</equation>，则<equation>P_{2}^{-1}BP_{2} = \left( \begin{array}{cc}5 & 0\\ 0 & 0 \end{array} \right)</equation>.

由于<equation>B=P_{2} P_{1}^{-1} A P_{1} P_{2}^{-1}</equation>，故取<equation>Q=P_{1} P_{2}^{-1}</equation>，则<equation>Q^{-1} A Q=B.</equation>计算得<equation>P_{2}^{-1}=\frac{1}{5}\left( \begin{array}{cc}2&1\\ -1&2 \end{array} \right)</equation>，则<equation>Q=\frac{1}{5}\left( \begin{array}{cc}-1&2\\ 2&1 \end{array} \right)\left( \begin{array}{cc}2&1\\ -1&2 \end{array} \right)=\left( \begin{array}{cc}-\frac{4}{5}&\frac{3}{5}\\ \frac{3}{5}&\frac{4}{5} \end{array} \right).</equation>并且，Q已经是正交矩阵，无需再单位正交化.

因此，<equation>Q = \left( \begin{array}{cc} - \frac{4}{5} & \frac{3}{5} \\ \frac{3}{5} & \frac{4}{5} \end{array} \right), f \left(x_{1}, x_{2}\right)</equation>经过正交变换<equation>\binom{x_1}{x_2} = Q\binom{y_1}{y_2}</equation>化为二次型<equation>g \left(y_{1}, y_{2}\right).</equation>

---

**2019年第6题 | 选择题 | 4分 | 答案: C**

6. 设 A是3阶实对称矩阵，E是3阶单位矩阵.若<equation>A^{2}+A=2 E</equation>，且<equation>|A|=4</equation>，则二次型<equation>x^{\mathrm{T}} A x</equation>的规范形为（    ）

A.<equation>y_{1}^{2}+y_{2}^{2}+y_{3}^{2}</equation>B.<equation>y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>C.<equation>y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>D.<equation>-y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>

答案: C

**解析:**设<equation>\lambda</equation>为 A的一个特征值，<equation>\alpha</equation>为属于特征值<equation>\lambda</equation>的特征向量.

由<equation>A^{2}+A=2 E</equation>可得<equation>(\lambda^{2}+\lambda-2)\alpha=0</equation>. 由于<equation>\alpha</equation>为非零向量，故<equation>\lambda^{2}+\lambda-2=0</equation>. 解得<equation>\lambda=1</equation>或<equation>\lambda=-2</equation>. A的特征值只能取1和-2.

又因为<equation>| A |=4</equation>，所以 A的特征值应为-2，-2，1. 因此，二次型<equation>x^{\mathrm{T}} A x</equation>的正惯性指数为1，负惯性指数为2. 四个选项中，只有<equation>y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>满足该性质. 应选C.

---

**2018年第20题 | 解答题 | 11分**

20. (本题满分11分)

设实二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=\left( x_{1}-x_{2}+x_{3} \right)^{2}+\left( x_{2}+x_{3} \right)^{2}+\left( x_{1}+a x_{3} \right)^{2}</equation>其中 a是参数.

I. 求<equation>f \left( x_{1}, x_{2}, x_{3} \right)=0</equation>的解；

II. 求<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>的规范形.

**答案:**（I）当 a≠2时，<equation>f ( x_{1}, x_{2}, x_{3} )=0</equation>的解为<equation>( x_{1}, x_{2}, x_{3} )^{\mathrm{T}}=(0,0,0)^{\mathrm{T}}</equation>；当 a=2时，<equation>f ( x_{1}, x_{2}, x_{3} )=0</equation>的解为<equation>( x_{1}, x_{2}, x_{3} )^{\mathrm{T}}=k (-2,-1,1)^{\mathrm{T}}</equation>其中 k为任意常数.

（Ⅱ）当 a≠2时， f的规范形为<equation>f=y_{1}^{2}+y_{2}^{2}+y_{3}^{2}</equation>；当 a=2时， f的规范形为<equation>f=z_{1}^{2}+z_{2}^{2}.</equation>

**解析:**解（I）<equation>f \left( x_{1}, x_{2}, x_{3} \right)=0</equation>当且仅当<equation>\left\{ \begin{array}{l l} x_{1}-x_{2}+x_{3}=0, \\ x_{2}+x_{3}=0, \\ x_{1}+a x_{3}=0. \end{array} \right.</equation>记A为该方程组的系数矩阵.对A作初等行变换.<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & - 1 & 1 \\ 0 & 1 & 1 \\ 1 & 0 & a \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c} 1 & - 1 & 1 \\ 0 & 1 & 1 \\ 0 & 1 & a - 1 \end{array} \right) \xrightarrow {r _ {1} + r _ {2}} \frac {r _ {3} ^ {*} - r _ {2}}{r _ {3} ^ {*}} \left( \begin{array}{c c c} 1 & 0 & 2 \\ 0 & 1 & 1 \\ 0 & 0 & a - 2 \end{array} \right).</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

当 a≠2时，<equation>r(A)=3</equation>，方程组只有零解.

当 a=2时，<equation>r ( \mathbf{A} )=2.</equation>方程组的基础解系仅包含一个向量.取<equation>x_{3}</equation>为自由变元，令<equation>x_{3}=1</equation>解得<equation>\left(x_{1},x_{2},x_{3}\right)^{\mathrm{T}}=\left(-2,-1,1\right)^{\mathrm{T}}</equation>为该方程组的一个基础解系.

因此，当<equation>a\neq 2</equation>时，<equation>f(x_{1},x_{2},x_{3})=0</equation>的解为<equation>(x_{1},x_{2},x_{3})^{\mathrm{T}}=(0,0,0)^{\mathrm{T}}</equation>；当<equation>a=2</equation>时，<equation>f(x_{1},x_{2},x_{3})=0</equation>的解为<equation>(x_{1},x_{2},x_{3})^{\mathrm{T}}=k(-2,-1,1)^{\mathrm{T}}</equation>，其中k为任意常数.

（Ⅱ）由<equation>f(x_{1},x_{2},x_{3})</equation>的表达式知，<equation>f(x_{1},x_{2},x_{3})\geqslant 0.</equation>当<equation>a\neq 2</equation>时，由第（I）问可知，<equation>f(x_{1},x_{2},x_{3}) = 0</equation>只有零解，<equation>f</equation>为正定二次型.因此，当<equation>a\neq 2</equation>时，<equation>f</equation>的规范形为<equation>f = y_{1}^{2} + y_{2}^{2} + y_{3}^{2}</equation>.

当 a=2时，f不满秩.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= \left(x _ {1} - x _ {2} + x _ {3}\right) ^ {2} + \left(x _ {2} + x _ {3}\right) ^ {2} + \left(x _ {1} + 2 x _ {3}\right) ^ {2} \\ &= 2 x _ {1} ^ {2} + 2 x _ {2} ^ {2} + 6 x _ {3} ^ {2} - 2 x _ {1} x _ {2} + 6 x _ {1} x _ {3}. \end{aligned}</equation>记f对应的对称矩阵为<equation>B=\left( \begin{array}{c c c} 2 & -1 & 3 \\ -1 & 2 & 0 \\ 3 & 0 & 6 \end{array} \right).</equation>下面用三种方法求求 f的规范形.

（法一）由<equation>f ( x_{1}, x_{2}, x_{3} ) \geqslant0</equation>可知 f的负惯性指数为0（否则，若规范形有负系数，不妨设规范形为<equation>f=y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>，取<equation>( y_{1}, y_{2}, y_{3} )=(0,0,1)</equation>，则<equation>f ( y_{1}, y_{2}, y_{3} )=-1<0</equation>，矛盾).由于 B的秩等于 f的正、负惯性指数之和，故 f的正惯性指数等于 r（B）.

计算<equation>| B |</equation>得<equation>| B |=0</equation>，故<equation>r ( B ) \leqslant 2</equation>.又因为B有一个2阶子式<equation>\left| \begin{array}{c c} {2} & {-1} \\ {-1} & {2} \end{array} \right|=3\neq0</equation>，所以<equation>r ( B ) \geqslant2</equation>因此，<equation>r ( B )=2.</equation>综上所述，<equation>f</equation>的正惯性指数为2，负惯性指数为0.<equation>f</equation>的规范形为<equation>f=z_{1}^{2}+z_{2}^{2}.</equation>（法二）计算 B的特征值，从而得到 f的正、负惯性指数.

计算 B的特征多项式.<equation>| \lambda E - B | = \left| \begin{array}{c c c} \lambda - 2 & 1 & - 3 \\ 1 & \lambda - 2 & 0 \\ - 3 & 0 & \lambda - 6 \end{array} \right| = \lambda \left(\lambda^ {2} - 1 0 \lambda + 1 8\right).</equation>解<equation>\lambda^{2}-1 0 \lambda+1 8=0</equation>可得<equation>\lambda_{1,2}=\frac{1 0 \pm \sqrt{1 0 0-7 2}}{2}=5 \pm \sqrt{7}.</equation>由于<equation>5+\sqrt{7}>0, 5-\sqrt{7}>0</equation>，故f有两个正特征值，一个零特征值，从而 f的正惯性指数为2，负惯性指数为0.

因此，<equation>f</equation>的规范形为<equation>f = z_{1}^{2} + z_{2}^{2}</equation>.

（法三）配方法.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= 2 x _ {1} ^ {2} + 2 x _ {2} ^ {2} + 6 x _ {3} ^ {2} - 2 x _ {1} x _ {2} + 6 x _ {1} x _ {3} = 2 \left(x _ {1} ^ {2} - x _ {1} x _ {2} + 3 x _ {1} x _ {3}\right) + 2 x _ {2} ^ {2} + 6 x _ {3} ^ {2} \\ &= 2 \left(x _ {1} - \frac {x _ {2}}{2} + \frac {3}{2} x _ {3}\right) ^ {2} + \frac {3}{2} x _ {2} ^ {2} - \frac {9}{2} x _ {3} ^ {2} + 3 x _ {2} x _ {3} + 6 x _ {3} ^ {2} \\ &= 2 \left(x _ {1} - \frac {x _ {2}}{2} + \frac {3}{2} x _ {3}\right) ^ {2} + \frac {3}{2} \left(x _ {2} + x _ {3}\right) ^ {2}. \end{aligned}</equation>令<equation>\left\{ \begin{array}{l l} z_{1}=\sqrt{2}\left(x_{1}-\frac{x_{2}}{2}+\frac{3}{2} x_{3}\right), \\ z_{2}=\sqrt{\frac{3}{2}}\left(x_{2}+x_{3}\right), \\ z_{3}=x_{3}, \end{array} \right.</equation>则<equation>f \left(z_{1}, z_{2}, z_{3}\right)=z_{1}^{2}+z_{2}^{2}.</equation>因此，<equation>f</equation>的规范形为<equation>f = z_{1}^{2} + z_{2}^{2}</equation>.

---

**2017年第21题 | 解答题 | 11分**

21. (本题满分11分)

设二次型<equation>f \left(x_{1}, x_{2}, x_{3}\right)=2 x_{1}^{2}-x_{2}^{2}+a x_{3}^{2}+2 x_{1} x_{2}-8 x_{1} x_{3}+2 x_{2} x_{3}</equation>在正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>下的标准形为<equation>\lambda_{1} y_{1}^{2}+\lambda_{2} y_{2}^{2}</equation>求 a的值及一个正交矩阵 Q.

**答案:**<equation>a = 2, Q = \left( \begin{array}{c c c} - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {3}} & \frac {1}{\sqrt {6}} \\ 0 & - \frac {1}{\sqrt {3}} & \frac {2}{\sqrt {6}} \\ \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {3}} & \frac {1}{\sqrt {6}} \end{array} \right), \text {且} Q ^ {\mathrm {T}} A Q = \left( \begin{array}{c c c} 6 & 0 & 0 \\ 0 & - 3 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>

**解析:**记二次型 f对应的实对称矩阵为 A，则<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 2 & 1 & - 4 \\ 1 & - 1 & 1 \\ - 4 & 1 & a \end{array} \right).</equation>由于 f在正交变换<equation>x=Q y</equation>下的标准形为<equation>\lambda_{1} y_{1}^{2}+\lambda_{2} y_{2}^{2}</equation>，故 A的特征值为<equation>\lambda_{1},\lambda_{2},0.</equation>从而<equation>|A|=0.</equation>计算 A的行列式得<equation>| A | = - 3 a + 6.</equation>因此，<equation>a = 2</equation>，<equation>A = \left( \begin{array}{c c c} 2 & 1 & -4 \\ 1 & -1 & 1 \\ -4 & 1 & 2 \end{array} \right)</equation>计算 A的特征多项式得<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - 2 & - 1 & 4 \\ - 1 & \lambda + 1 & - 1 \\ 4 & - 1 & \lambda - 2  \right| \xlongequal {r _ {1} - r _ {3}} \left| \begin{array}{c c c} \lambda - 6 & 0 & 6 - \lambda \\ - 1 & \lambda + 1 & - 1 \\ 4 & - 1 & \lambda - 2  \right| \\ \underline {{\underline {{c _ {3} + c _ {1}}}}} \left| \begin{array}{c c c} \lambda - 6 & 0 & 0 \\ - 1 & \lambda + 1 & - 2 \\ 4 & - 1 & \lambda + 2  \right| &= \lambda (\lambda - 6) (\lambda + 3). \end{aligned}</equation>于是，A的3个特征值分别为6，-3，0.

当<equation>\lambda=6</equation>时，<equation>\begin{array}{l} 6 E - A = \left( \begin{array}{c c c} 4 & - 1 & 4 \\ - 1 & 7 & - 1 \\ 4 & - 1 & 4 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c} 4 & - 1 & 4 \\ - 1 & 7 & - 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} + 4 r _ {2}} \left( \begin{array}{c c c} 0 & 1 & 0 \\ - 1 & 7 & - 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} - 7 r _ {1} ^ {* *}} r _ {2} ^ {*} \times (- 1) \left( \begin{array}{c c c} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>因此，<equation>\boldsymbol{\eta}_{1}=(-1,0,1)^{\mathrm{T}}</equation>为（6E-A）<equation>\boldsymbol{x}=\mathbf{0}</equation>的一个基础解系.

当<equation>\lambda=-3</equation>时，<equation>\begin{array}{l} - 3 E - A = \left( \begin{array}{c c c} - 5 & - 1 & 4 \\ - 1 & - 2 & - 1 \\ 4 & - 1 & - 5 \end{array} \right) \xrightarrow [ r _ {3} ^ {*} - r _ {2} ]{r _ {3} + r _ {1}} \left( \begin{array}{c c c} - 5 & - 1 & 4 \\ - 1 & - 2 & - 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {2} \times (- 1) ]{r _ {1} - 5 r _ {2}} \left( \begin{array}{c c c} 0 & 9 & 9 \\ 1 & 2 & 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow [ r _ {2} ^ {*} - r _ {1} ^ {* *} ]{r _ {1} ^ {*} \times \frac {1}{9}} \left( \begin{array}{c c c} 0 & 1 & 1 \\ 1 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>因此，<equation>\boldsymbol{\eta}_{2} = (1, - 1, 1)^{\mathrm{T}}</equation>为<equation>(-3E-A)x=0</equation>的一个基础解系.

当<equation>\lambda = 0</equation>时，<equation>\begin{array}{l} 0 E - A = \left( \begin{array}{c c c} - 2 & - 1 & 4 \\ - 1 & 1 & - 1 \\ 4 & - 1 & - 2 \end{array} \right) \xrightarrow {r _ {3} + r _ {1}} r _ {3} ^ {*} + 2 r _ {2} \left( \begin{array}{c c c} - 2 & - 1 & 4 \\ - 1 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} - 2 r _ {2}} r _ {1} ^ {*} \times \left(- \frac {1}{3}\right) \left( \begin{array}{c c c} 0 & 1 & - 2 \\ - 1 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} \times (- 1) + r _ {1} ^ {* *}} \left( \begin{array}{c c c} 0 & 1 & - 2 \\ 1 & 0 & - 1 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>因此，<equation>\boldsymbol{\eta}_{3} = (1,2,1)^{\mathrm{T}}</equation>为<equation>(0 E - A) x = 0</equation>的一个基础解系.

由于实对称矩阵对应于不同特征值的特征向量相互正交，故只需将所得特征向量单位化

将<equation>\boldsymbol{\eta}_{1},\boldsymbol{\eta}_{2},\boldsymbol{\eta}_{3}</equation>分别单位化，作为Q的列向量，得正交矩阵<equation>Q=\left( \begin{array}{c c c} -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \\ 0 & -\frac{1}{\sqrt{3}} & \frac{2}{\sqrt{6}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \end{array} \right)</equation>，且<equation>Q^{\mathrm{T}}AQ=</equation><equation>\left( \begin{array}{c c c} 6 & 0 & 0 \\ 0 & - 3 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>即f在正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>下的标准形为<equation>f=6 y_{1}^{2}-3 y_{2}^{2}.</equation>

---

**2016年第6题 | 选择题 | 4分 | 答案: C**

6. 设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=a \left( x_{1}^{2}+x_{2}^{2}+x_{3}^{2} \right)+2 x_{1} x_{2}+2 x_{2} x_{3}+2 x_{1} x_{3}</equation>的正、负惯性指数分别为1，2，则（    )

A. a > 1 B. a < -2 C.<equation>- 2 < a < 1</equation>D. a =1或a=-2

答案: C

**解析:**解（法一）f对应的对称矩阵为<equation>A=\left( \begin{array}{c c c} a & 1 & 1 \\ 1 & a & 1 \\ 1 & 1 & a \end{array} \right).</equation>A正交相似于一个对角矩阵，该矩阵的主对角元为 A的特征值.

计算 A的特征多项式，得<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - a & - 1 & - 1 \\ - 1 & \lambda - a & - 1 \\ - 1 & - 1 & \lambda - a  \right| \xlongequal {c _ {2} - c _ {3}} \left| \begin{array}{c c c} \lambda - a & 0 & - 1 \\ - 1 & \lambda - a + 1 & - 1 \\ - 1 & - (\lambda - a + 1) & \lambda - a  \right| \\ \underline {{\text {按 第一 行 展 开}}} (\lambda - a) (\lambda - a + 1) (\lambda - a - 1) - 2 (\lambda - a + 1) \\ &= (\lambda - a + 1) ^ {2} (\lambda - a - 2). \end{aligned}</equation>因此，A的特征值为 a-1，a-1，a+2.

由于 a+2>a-1，故若 f的正、负惯性指数分别为1，2，则<equation>\left\{\begin{array}{l l}a-1<0,\\ a+2>0.\end{array}\right.</equation>解得-2<a<1.应选C.

（法二）如法一，写出 A.

由于二次型 f的正、负惯性指数分别为1，2，故 A的特征值有一个为正值，两个为负值，从而<equation>| A | > 0.</equation>计算 A的行列式.<equation>| A | = \left| \begin{array}{c c c} a & 1 & 1 \\ 1 & a & 1 \\ 1 & 1 & a \end{array} \right| = (a - 1) ^ {2} (a + 2).</equation>由于<equation>|A| > 0</equation>，故<equation>a+2 > 0</equation>，即<equation>a > -2</equation>.由此可以排除选项B和选项D.

另一方面，若 a > 1，则 a > 0，<equation>a^{2}-1 > 0</equation><equation>| A | > 0</equation>A的各阶顺序主子式皆为正.由正定矩阵的判别法可知，A为正定矩阵，从而 f的正惯性指数为3.这与 f的正、负惯性指数分别为1，2矛盾，故可排除选项A.

因此，应选C.

---

**2015年第6题 | 选择题 | 4分 | 答案: A**

6. 设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>在正交变换<equation>x=P y</equation>下的标准形为<equation>2 y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>其中<equation>P=\left( e_{1}, e_{2}, e_{3} \right)</equation>若<equation>Q=\left( e_{1},-e_{3}, e_{2} \right)</equation>则<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>在正交变换<equation>x=Q y</equation>下的标准形为（    )

A.<equation>2 y_{1}^{2}-y_{2}^{2}+y_{3}^{2}</equation>B.<equation>2 y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>C.<equation>2 y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>D.<equation>2 y_{1}^{2}+y_{2}^{2}+y_{3}^{2}</equation>

答案: A

**解析:**解（法一）设<equation>f=x^{\mathrm{T}}Ax</equation>，则由题设知，<equation>f = \left(\boldsymbol {P} \boldsymbol {y}\right) ^ {\mathrm {T}} \boldsymbol {A} \left(\boldsymbol {P} \boldsymbol {y}\right) = \boldsymbol {y} ^ {\mathrm {T}} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} \boldsymbol {y} = 2 y _ {1} ^ {2} + y _ {2} ^ {2} - y _ {3} ^ {2}.</equation>从而<equation>P^{\mathrm{T}}A P = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -1 \end{array} \right).</equation>又由于<equation>Q = \left(e_{1}, - e_{3}, e_{2}\right) = \left(e_{1}, e_{2}, e_{3}\right)\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{array} \right) = P\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{array} \right)</equation>，故<equation>\begin{aligned} f &= \boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {x} = \left(\boldsymbol {Q} \boldsymbol {y}\right) ^ {\mathrm {T}} \boldsymbol {A} \left(\boldsymbol {Q} \boldsymbol {y}\right) = \boldsymbol {y} ^ {\mathrm {T}} \boldsymbol {Q} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {Q} \boldsymbol {y} = \boldsymbol {y} ^ {\mathrm {T}} \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & - 1 & 0  \right) ^ {\mathrm {T}} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & - 1 & 0  \right) \boldsymbol {y} \\ &= \boldsymbol {y} ^ {\mathrm {T}} \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & - 1 \\ 0 & 1 & 0  \right) \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & - 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & - 1 & 0  \right) \boldsymbol {y} \\ &= \boldsymbol {y} ^ {\mathrm {T}} \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 1  \right) \boldsymbol {y} &= 2 y _ {1} ^ {2} - y _ {2} ^ {2} + y _ {3} ^ {2}. \end{aligned}</equation>因此，<equation>f ( x_{1}, x_{2}, x_{3} )</equation>在<equation>\mathbf{x}=\mathbf{Q y}</equation>的标准形为<equation>f=2 y_{1}^{2}-y_{2}^{2}+y_{3}^{2}.</equation>应选A.

（法二）由题设知，二次型<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>在正交变换<equation>\boldsymbol{x}=\boldsymbol{P}\boldsymbol{y}</equation>下的标准形为<equation>f=2y_{1}^{2}+y_{2}^{2}-y_{3}^{2}.</equation>因此，该二次型所对应的对称矩阵A的特征值为2，1，-1，而<equation>e_{1},e_{2},e_{3}</equation>分别为属于特征值2，1，-1的特征向量.

若<equation>Q=(\boldsymbol{e}_1,-\boldsymbol{e}_3,\boldsymbol{e}_2)</equation>，则由<equation>A(-e_{3})=-Ae_{3}=-(-e_{3})</equation>可知<equation>-e_{3}</equation>也为属于特征值-1的特征向量，故<equation>Q^{\mathrm{T}}AQ=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{array} \right). f(x_{1},x_{2},x_{3})</equation>在<equation>\boldsymbol{x}=Q\boldsymbol{y}</equation>下的标准形为<equation>f=2y_{1}^{2}-y_{2}^{2}+y_{3}^{2}.</equation>应选A.

---

**2014年第13题 | 填空题 | 4分**

13. 设二次型<equation>f(x_{1},x_{2},x_{3})=x_{1}^{2}-x_{2}^{2}+2a x_{1} x_{3}+4 x_{2} x_{3}</equation>的负惯性指数为1，则 a的取值范围是 ___

**解析:**解 （法一）用配方法将原二次型化为标准形.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= \left(x _ {1} + a x _ {3}\right) ^ {2} - a ^ {2} x _ {3} ^ {2} - \left(x _ {2} - 2 x _ {3}\right) ^ {2} + 4 x _ {3} ^ {2} \\ &= \left(x _ {1} + a x _ {3}\right) ^ {2} - \left(x _ {2} - 2 x _ {3}\right) ^ {2} + \left(4 - a ^ {2}\right) x _ {3} ^ {2}. \end{aligned}</equation>因此，若二次型<equation>f(x_{1},x_{2},x_{3})</equation>的负惯性指数为1，则<equation>4 - a^{2}\geqslant 0</equation>，即<equation>a\in[-2,2]</equation>（法二）写出二次型<equation>f(x_{1},x_{2},x_{3})</equation>对应的对称矩阵<equation>A.</equation><equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & 0 & a \\ 0 & - 1 & 2 \\ a & 2 & 0 \end{array} \right).</equation>计算<equation>A</equation>的行列式得，<equation>|A| = a^2 - 4.</equation>A的迹等于零，说明A的特征值之和为零.

下面我们证明，当3阶非零实对称矩阵<equation>A</equation>的迹为零时，<equation>A</equation>的负惯性指数为1等价于<equation>|A| \leqslant 0.</equation>当3阶非零实对称矩阵<equation>A</equation>的迹为零时，由<equation>A</equation>的负惯性指数为1可知，<equation>A</equation>的特征值可能为两正、一负，或者一正、一零、一负.在这两种情形下，<equation>|A| \leqslant 0.</equation>若<equation>A</equation>为3阶非零实对称矩阵，且<equation>|A| \leqslant 0</equation>，则<equation>A</equation>的特征值的符号有五种可能：（1）两正、一负；（2）一正、一零、一负；（3）两零、一负；（4）三负；（5）全为零.两个零特征值、一个负特征值和三个负特征值的情形与<equation>A</equation>的迹为零矛盾.特征值全为零的情形与<equation>A</equation>是非零实对称矩阵矛盾，因为若<equation>A</equation>的特征值全为零，则<equation>A</equation>相似于零矩阵，从而<equation>A</equation>为零矩阵.因此，<equation>A</equation>的特征值仅可能为两正、一负，或一正、一零、一负.在这两种情形下，<equation>A</equation>的负惯性指数都为1.

综上所述，<equation>A</equation>的负惯性指数为1等价于<equation>|A| \leqslant 0</equation>，即<equation>a \in [-2,2]</equation>

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


#### 向量组之间的线性表示

**2025年第21题 | 解答题 | 12分**

21. 设矩阵<equation>A = \left( \begin{array}{c c c c c} 1 & -1 & 3 & 0 & -1 \\ -1 & 0 & -2 & -a & -1 \\ 1 & 1 & a & 2 & 3 \end{array} \right)</equation>的秩为2.

I. 求 a的值；
