#### 特征值与特征向量

**2025年第8题 | 选择题 | 5分 | 答案: D**
8. 设矩阵<equation>\left( \begin{array}{c c c} {1} & {2} & {0} \\ {2} & {a} & {0} \\ {0} & {0} & {b} \end{array} \right)</equation>有一个正特征值和两个负特征值，则（    ）

A. a > 4,b > 0 B. a < 4,b > 0 C. a > 4,b < 0 D. a < 4,b < 0
答案: D
**解析: **解（法一）记<equation>A = \left( \begin{array}{c c c} 1 & 2 & 0 \\ 2 & a & 0 \\ 0 & 0 & b \end{array} \right)</equation>，由<equation>A</equation>有一个正特征值和两个负特征值可得<equation>A</equation>所对应的二次型<equation>f\left(x_{1}, x_{2}, x_{3}\right)</equation>的正、负惯性指数分别为1,2.

对<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>配方可得<equation>f\left(x_{1}, x_{2}, x_{3}\right) = x_{1}^{2} + a x_{2}^{2} + b x_{3}^{2} + 4 x_{1} x_{2} = \left(x_{1} + 2 x_{2}\right)^{2} + (a - 4) x_{2}^{2} + b x_{3}^{2}.</equation>由于<equation>\left(x_{1} + 2 x_{2}\right)^{2}</equation>的系数为正数1，故<equation>a - 4, b</equation>均为负数，即<equation>\left\{ \begin{array}{l} a - 4 < 0, \\ b < 0. \end{array} \right.</equation>因此，<equation>a < 4,b < 0</equation>，应选D.

（法二）记<equation>A = \left( \begin{array}{c c c} 1 & 2 & 0 \\ 2 & a & 0 \\ 0 & 0 & b \end{array} \right)</equation>，由<equation>A</equation>有一个正特征值和两个负特征值可得<equation>|A| > 0.</equation>计算<equation>|A|</equation>可得<equation>|A| = b(a - 4)</equation>. 由<equation>|A| > 0</equation>可得b与a-4同号，即<equation>a > 4,b > 0</equation>或<equation>a < 4,b < 0.</equation>计算 A的特征多项式.<equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda - 1 & - 2 & 0 \\ - 2 & \lambda - a & 0 \\ 0 & 0 & \lambda - b \end{array} \right| = (\lambda - b) \left[ \lambda^ {2} - (a + 1) \lambda + a - 4 \right].</equation>若<equation>a > 4, b > 0</equation>，则<equation>a + 1 > 0, a - 4 > 0</equation>，由根与系数的关系可知<equation>\lambda^2 - (a + 1)\lambda + a - 4 = 0</equation>的两根均大于0，加上<equation>b > 0, A</equation>的三个特征值均为正数，不符合题意.

若<equation>a < 4, b < 0</equation>，则<equation>a - 4 < 0</equation>，由根与系数的关系可知<equation>\lambda^2 - (a + 1)\lambda + a - 4 = 0</equation>的两根一正、一负，加上<equation>b < 0, A</equation>的三个特征值为一正、两负，符合题意.

因此，应选D.

---

**2020年第8题 | 选择题 | 4分 | 答案: D**
8. 设 A为3阶矩阵，<equation>\alpha_{1},\alpha_{2}</equation>为 A的属于特征值1的线性无关的特征向量，<equation>\alpha_{3}</equation>为 A的属于特征值-1的特征向量，则满足<equation>P^{-1}AP=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>的可逆矩阵 P可为（    ）

A.<equation>\left( \alpha_{1}+\alpha_{3},\alpha_{2},-\alpha_{3} \right)</equation>B.<equation>\left( \alpha_{1}+\alpha_{2},\alpha_{2},-\alpha_{3} \right)</equation>C.<equation>\left( \alpha_{1}+\alpha_{3},-\alpha_{3},\alpha_{2} \right)</equation>D.<equation>\left( \alpha_{1}+\alpha_{2},-\alpha_{3},\alpha_{2} \right)</equation>
答案: D
**解析: **解 由于<equation>P^{-1} A P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，故 P的列向量应分别为属于特征值1，-1，1的特征向量，且

第1列与第3列为属于特征值1的线性无关的特征向量.

由已知条件，<equation>\alpha_{3}</equation>为 A的属于特征值-1的特征向量，故 P的第2列可取为<equation>k\alpha_{3}</equation>其中 k为任意非零常数.

由于<equation>\alpha_{1},\alpha_{2}</equation>为 A的属于特征值1的线性无关的特征向量，且<equation>\left(\alpha_{1}+\alpha_{2},\alpha_{2}\right)=\left(\alpha_{1},\alpha_{2}\right)\left( \begin{array}{cc}1&0\\ 1&1 \end{array} \right)</equation>故<equation>\alpha_{1}+\alpha_{2}</equation>也为 A的属于特征值1的特征向量，且与<equation>\alpha_{2}</equation>线性无关.

因此，<equation>P</equation>可取为<equation>\left(\alpha_{1}+\alpha_{2},-\alpha_{3},\alpha_{2}\right).</equation>应选D.

---

**2018年第14题 | 填空题 | 4分**
14. 设 A为3阶矩阵，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>为线性无关的向量组. 若<equation>A\alpha_{1}=2\alpha_{1}+\alpha_{2}+\alpha_{3},A\alpha_{2}=\alpha_{2}+2\alpha_{3},A\alpha_{3}=-\alpha_{2}+\alpha_{3}</equation>，则 A的实特征值为___
**解析: **解记 P=（<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>）. 由于<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关，故 P可逆由题设可知，<equation>A P = A \left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) = \left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) \left( \begin{array}{c c c} 2 & 0 & 0 \\ 1 & 1 & - 1 \\ 1 & 2 & 1 \end{array} \right) = P \left( \begin{array}{c c c} 2 & 0 & 0 \\ 1 & 1 & - 1 \\ 1 & 2 & 1 \end{array} \right).</equation>于是，<equation>P^{-1} A P=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 1 & 1 & -1 \\ 1 & 2 & 1 \end{array} \right)=B.</equation>由矩阵相似的定义可知，A与B相似.

下面计算矩阵 B的特征多项式.<equation>| \lambda E - B | = \left| \begin{array}{c c c} \lambda - 2 & 0 & 0 \\ - 1 & \lambda - 1 & 1 \\ - 1 & - 2 & \lambda - 1 \end{array} \right| = (\lambda - 2) \left(\lambda^ {2} - 2 \lambda + 3\right).</equation>由于<equation>\lambda^{2}-2\lambda+3=(\lambda-1)^{2}+2>0</equation>，故<equation>|\lambda E-B|=0</equation>仅有一个实根，即<equation>\lambda=2</equation>.于是，B仅有一个实特征值2.

又因为 A与B相似，而相似的矩阵具有相同的特征值，所以 A的实特征值为2.

---

**2017年第7题 | 选择题 | 4分 | 答案: B**
7. 设 A为3阶矩阵，<equation>P=(\alpha_{1},\alpha_{2},\alpha_{3})</equation>为可逆矩阵，使得<equation>P^{-1}AP=\left( \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>，则<equation>A(\alpha_{1}+\alpha_{2}+\alpha_{3})=</equation>(    )

A.<equation>\alpha_{1}+\alpha_{2}</equation>B.<equation>\alpha_{2}+2\alpha_{3}</equation>C.<equation>\alpha_{2}+\alpha_{3}</equation>D.<equation>\alpha_{1}+2\alpha_{2}</equation>
答案: B
**解析: **解（法一）由于<equation>P^{-1} A P=\left( \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>，故<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>分别为 A的属于特征值0,1,2的特征向量.于是，<equation>A\alpha_{1}=0</equation><equation>A\alpha_{2}=\alpha_{2}</equation><equation>A\alpha_{3}=2\alpha_{3}</equation>因此，<equation>A(\alpha_{1}+\alpha_{2}+\alpha_{3})=\alpha_{2}+2\alpha_{3}</equation>应选B.

（法二）由于<equation>P^{-1} A P=\left( \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>，故<equation>A \left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) = A P = P \left( \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right) = \left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) \left( \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right) = \left(0, \alpha_ {2}, 2 \alpha_ {3}\right).</equation>因此，应选B.<equation>\boldsymbol {A} \left(\boldsymbol {\alpha} _ {1} + \boldsymbol {\alpha} _ {2} + \boldsymbol {\alpha} _ {3}\right) = \boldsymbol {\alpha} _ {2} + 2 \boldsymbol {\alpha} _ {3}.</equation>

---

**2017年第14题 | 填空题 | 4分**
14. 设矩阵<equation>A=\left( \begin{array}{c c c} 4 & 1 & -2 \\ 1 & 2 & a \\ 3 & 1 & -1 \end{array} \right)</equation>的一个特征向量为<equation>\left( \begin{array}{c} 1 \\ 1 \\ 2 \end{array} \right)</equation>，则 a=___
**答案: **<equation>- 1.</equation>
**解析: **设（1，1，2）<equation>^{\mathrm{T}}</equation>对应的特征值为<equation>\lambda</equation>，则<equation>\left( \begin{array}{c c c} 4 & 1 & - 2 \\ 1 & 2 & a \\ 3 & 1 & - 1 \end{array} \right) \left( \begin{array}{c} 1 \\ 1 \\ 2 \end{array} \right) = \left( \begin{array}{c} 1 \\ 3 + 2 a \\ 2 \end{array} \right) = \lambda \left( \begin{array}{c} 1 \\ 1 \\ 2 \end{array} \right)</equation>因此，<equation>\lambda=1</equation>，<equation>3+2a=1</equation>，<equation>a=-1.</equation>

---

**2015年第14题 | 填空题 | 4分**
14. 设 3 阶矩阵<equation>\mathbf{A}</equation>的特征值为 2,-2,1,<equation>\mathbf{B}=\mathbf{A}^{2}-\mathbf{A}+\mathbf{E}</equation>,其中<equation>\mathbf{E}</equation>为 3 阶单位矩阵,则行列式<equation>|\mathbf{B}|=</equation>___.
**解析: **解（法一）由于 A有3个不同的特征值，故 A有3个线性无关的特征向量，从而存在可逆矩阵 P使得<equation>P^{-1} A P=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>.于是<equation>\boldsymbol {A} = \boldsymbol {P} \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & - 2 & 0 \\ 0 & 0 & 1 \end{array} \right) \boldsymbol {P} ^ {- 1}, \quad \boldsymbol {A} ^ {2} = \boldsymbol {P} \left( \begin{array}{c c c} 2 ^ {2} & 0 & 0 \\ 0 & (- 2) ^ {2} & 0 \\ 0 & 0 & 1 ^ {2} \end{array} \right) \boldsymbol {P} ^ {- 1},</equation><equation>\boldsymbol {B} = \boldsymbol {P} \left( \begin{array}{c c c} 2 ^ {2} - 2 + 1 & 0 & 0 \\ 0 & (- 2) ^ {2} - (- 2) + 1 & 0 \\ 0 & 0 & 1 ^ {2} - 1 + 1 \end{array} \right) \boldsymbol {P} ^ {- 1} = \boldsymbol {P} \left( \begin{array}{c c c} 3 & 0 & 0 \\ 0 & 7 & 0 \\ 0 & 0 & 1 \end{array} \right) \boldsymbol {P} ^ {- 1}.</equation>因此，<equation>|B| = 21\cdot |P| \cdot |P^{-1}| = 21.</equation>（法二）设<equation>\alpha</equation>为矩阵<equation>A</equation>的属于特征值<equation>\lambda</equation>的特征向量，即<equation>A\alpha = \lambda \alpha</equation>，则<equation>\boldsymbol {B} \boldsymbol {\alpha} = \left(\boldsymbol {A} ^ {2} - \boldsymbol {A} + \boldsymbol {E}\right) \boldsymbol {\alpha} = \left(\lambda^ {2} - \lambda + 1\right) \boldsymbol {\alpha}.</equation>由上可见，若<equation>\alpha</equation>为A的属于特征值<equation>\lambda</equation>的特征向量，则<equation>\alpha</equation>为B的属于特征值<equation>\lambda^{2}-\lambda+1</equation>的特征向量.A的3个线性无关的特征向量也是B的3个线性无关的特征向量，对应的特征值为<equation>\lambda^{2}-\lambda+1</equation><equation>(\lambda=2,-2,1)</equation>.由此可求得B的特征值为3,7,1.

因此，<equation>|B| = 3\times 7\times 1 = 21.</equation>

---

**2011年第23题 | 解答题 | 11分**

设<equation>A</equation>为3阶实对称矩阵，<equation>A</equation>的秩为2，且<equation>\left( \begin{array}{c c} 1 & 1 \\ 0 & 0 \\ - 1 & 1 \end{array} \right) = \left( \begin{array}{c c} - 1 & 1 \\ 0 & 0 \\ 1 & 1 \end{array} \right)</equation>I. 求 A的所有特征值与特征向量；

II. 求矩阵 A.
**答案: **23) （I）特征值-1，1，0，分别对应特征向量<equation>k_{1}\left(1,0,-1\right)^{\mathrm{T}}, k_{2}\left(1,0,1\right)^{\mathrm{T}}, k_{3}\left(0,1,0\right)^{\mathrm{T}}</equation>，其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意非零常数；

（Ⅱ）<equation>\left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{array} \right).</equation>
**解析: **解（I）由于<equation>A\left( \begin{array}{c c} 1 & 1 \\ 0 & 0 \\ -1 & 1 \end{array} \right)=\left( \begin{array}{c c} -1 & 1 \\ 0 & 0 \\ 1 & 1 \end{array} \right)</equation>，故<equation>\alpha_{1}=(1,0,-1)^{\mathrm{T}},\alpha_{2}=(1,0,1)^{\mathrm{T}}</equation>满足<equation>A\alpha_{1}=</equation><equation>-\alpha_{1},A\alpha_{2}=\alpha_{2}</equation>，从而<equation>\alpha_{1}</equation>为A的属于特征值-1的特征向量，<equation>\alpha_{2}</equation>为A的属于特征值1的特征向量又因为<equation>r(A)=2,|A|=0</equation>，所以A还有一个特征值为零.

因为实对称矩阵属于不同特征值的特征向量相互正交，所以 A的属于特征值0的特征向量<equation>\boldsymbol{\alpha}_{3}=(x_{1},x_{2},x_{3})^{\mathrm{T}}</equation>满足<equation>\boldsymbol{\alpha}_{1}^{\mathrm{T}}\boldsymbol{\alpha}_{3}=0,\boldsymbol{\alpha}_{2}^{\mathrm{T}}\boldsymbol{\alpha}_{3}=0</equation>从而得<equation>\left\{ \begin{array}{l l} x_{1}-x_{3}=0, \\ x_{1}+x_{3}=0. \end{array} \right.</equation>由此可得<equation>\boldsymbol{\alpha}_{3}=k_{3}(0,1,0)^{\mathrm{T}},k_{3}</equation>为任意非零常数.

因此，<equation>\mathbf{A}</equation>的特征值为-1，1，0.对应的特征向量分别为<equation>k_{1}(1,0,-1)^{\mathrm{T}}</equation><equation>k_{2}(1,0,1)^{\mathrm{T}}</equation><equation>k_{3}(0,1,0)^{\mathrm{T}}</equation>其中<equation>k_{1},k_{2},k_{3}</equation>为任意非零常数.

（Ⅱ）（法一）由第（I）问可知，取<equation>P=\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)=\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \\ -1 & 1 & 0 \end{array} \right)</equation>，可得<equation>P^{-1}AP=</equation><equation>\left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>，于是<equation>A=P\left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right) P^{-1}.</equation>利用初等变换法计算<equation>P^{-1}.</equation><equation>\begin{array}{l} (P, E) = \left( \begin{array}{c c c c c c} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 1 & 0 \\ - 1 & 1 & 0 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} + r _ {1}} \left( \begin{array}{c c c c c c} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 1 & 0 \\ 0 & 2 & 0 & 1 & 0 & 1 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {*} \times \frac {1}{2}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & \frac {1}{2} & 0 & - \frac {1}{2} \\ 0 & 0 & 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & \frac {1}{2} & 0 & \frac {1}{2} \end{array} \right) \xrightarrow {r _ {2} \leftrightarrow r _ {3} ^ {* *}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & \frac {1}{2} & 0 & - \frac {1}{2} \\ 0 & 1 & 0 & \frac {1}{2} & 0 & \frac {1}{2} \\ 0 & 0 & 1 & 0 & 1 & 0 \end{array} \right). \\ \end{array}</equation>于是，<equation>P^{-1}=\left( \begin{array}{c c c} \frac{1}{2} & 0 & -\frac{1}{2} \\ \frac{1}{2} & 0 & \frac{1}{2} \\ 0 & 1 & 0 \end{array} \right).</equation>因此，<equation>\begin{aligned} \boldsymbol {A} &= \boldsymbol {P} \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \boldsymbol {P} ^ {- 1} &= \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \\ - 1 & 1 & 0  \right) \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \left( \begin{array}{c c c} \frac {1}{2} & 0 & - \frac {1}{2} \\ \frac {1}{2} & 0 & \frac {1}{2} \\ 0 & 1 & 0  \right) \\ &= \left( \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & 0 & 0 \\ 1 & 1 & 0  \right) \left( \begin{array}{c c c} \frac {1}{2} & 0 & - \frac {1}{2} \\ \frac {1}{2} & 0 & \frac {1}{2} \\ 0 & 1 & 0  \right) &= \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0  \right). \end{aligned}</equation>或者，由<equation>A P = \left(A \alpha_ {1}, A \alpha_ {2}, A \alpha_ {3}\right) = \left(- \alpha_ {1}, \alpha_ {2}, 0\right)</equation>可得，<equation>\boldsymbol {A} = \left(- \alpha_ {1}, \alpha_ {2}, 0\right) \boldsymbol {P} ^ {- 1} = - \frac {1}{2} \left( \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & 0 & 0 \\ 1 & 1 & 0 \end{array} \right) \left( \begin{array}{c c c} - 1 & 0 & 1 \\ - 1 & 0 & - 1 \\ 0 & - 2 & 0 \end{array} \right) = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{array} \right).</equation>（法二）将<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>单位化，组成一正交矩阵<equation>Q=\left( \begin{array}{c c c} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0 \\ 0 & 0 & 1 \\ -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0 \end{array} \right)</equation>，则<equation>Q^{\mathrm{T}}AQ=\left( \begin{array}{c c c} -1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>因此，<equation>\begin{aligned} \boldsymbol {A} &= \boldsymbol {Q} \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \boldsymbol {Q} ^ {\mathrm {T}} &= \left( \begin{array}{c c c} \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {2}} & 0 \\ 0 & 0 & 1 \\ - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {2}} & 0  \right) \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \left( \begin{array}{c c c} \frac {1}{\sqrt {2}} & 0 & - \frac {1}{\sqrt {2}} \\ \frac {1}{\sqrt {2}} & 0 & \frac {1}{\sqrt {2}} \\ 0 & 1 & 0  \right) \\ &= \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0  \right). \end{aligned}</equation>

---

**2010年第23题 | 解答题 | 11分**
23. (本题满分11分)

设<equation>A=\left( \begin{array}{c c c} 0 & -1 & 4 \\ -1 & 3 & a \\ 4 & a & 0 \end{array} \right)</equation>，正交矩阵Q使<equation>Q^{\mathrm{T}}AQ</equation>为对角矩阵，若Q的第1列为<equation>\frac{1}{\sqrt{6}}(1,2,1)^{\mathrm{T}}</equation>求a,Q.
**答案: **<equation>a = - 1, Q = \left( \begin{array}{c c c} \frac {1}{\sqrt {6}} & - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {3}} \\ \frac {2}{\sqrt {6}} & 0 & - \frac {1}{\sqrt {3}} \\ \frac {1}{\sqrt {6}} & \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {3}} \end{array} \right), Q ^ {\mathrm {T}} A Q = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & - 4 & 0 \\ 0 & 0 & 5 \end{array} \right).</equation>
**解析: **解 由题设知，<equation>\alpha_{1}=\frac{1}{\sqrt{6}}(1,2,1)^{\mathrm{T}}</equation>为 A的特征向量.不妨设<equation>\alpha_{1}</equation>对应的特征值为 k，则<equation>\begin{aligned} \boldsymbol {A} \boldsymbol {\alpha} _ {1} &= \frac {1}{\sqrt {6}} \left( \begin{array}{c c c} 0 & - 1 & 4 \\ - 1 & 3 & a \\ 4 & a & 0  \right) \left(  1 \\ 2 \\ 1  \right) &= \frac {1}{\sqrt {6}} \left( \begin{array}{c} 2 \\ 5 + a \\ 4 + 2 a  \right) &= \frac {k}{\sqrt {6}} \left(  1 \\ 2 \\ 1  \right). \end{aligned}</equation>从而有<equation>\left\{ \begin{array}{l}2 = k,\\ 5 + a = 2k,\\ 4 + 2a = k, \end{array} \right.</equation>解得<equation>a = -1, k = 2.</equation>于是，<equation>A = \left( \begin{array}{c c c}0 & -1 & 4\\ -1 & 3 & -1\\ 4 & -1 & 0 \end{array} \right).</equation>计算 A的特征多项式得<equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda & 1 & - 4 \\ 1 & \lambda - 3 & 1 \\ - 4 & 1 & \lambda \end{array} \right| = (\lambda - 2) (\lambda - 5) (\lambda + 4).</equation>因此，<equation>A</equation>的特征值为2，5，-4.<equation>\alpha_{1}</equation>是<equation>A</equation>的属于特征值2的特征向量.

先求属于特征值-4的特征向量<equation>\alpha_{2}</equation>.由特征向量的定义可知，<equation>(-4E - A)x = 0.</equation><equation>\begin{array}{l} - 4 E - A = \left( \begin{array}{c c c} - 4 & 1 & - 4 \\ 1 & - 7 & 1 \\ - 4 & 1 & - 4 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c} - 4 & 1 & - 4 \\ 1 & - 7 & 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} + 4 r _ {2}} \left( \begin{array}{c c c} 0 & 1 & 0 \\ 1 & - 7 & 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} + 7 r _ {1} ^ {* *}} \frac {1}{r _ {1} ^ {* *} \leftrightarrow r _ {2} ^ {*}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>由此可得<equation>\left\{\begin{array}{l l}x_{1}+x_{3}=0,\\ x_{2}=0,\end{array}\right.</equation>故<equation>\boldsymbol{\xi}_{2}=(-1,0,1)^{\mathrm{T}}</equation>为它的一个基础解系.将<equation>\boldsymbol{\xi}_{2}</equation>单位化得<equation>\boldsymbol{\alpha}_{2}=\frac{1}{\sqrt{2}}(-1,0,1)^{\mathrm{T}}.</equation>同理，解（5E-A）<equation>x=0.</equation><equation>5 E - A = \left( \begin{array}{c c c} 5 & 1 & - 4 \\ 1 & 2 & 1 \\ - 4 & 1 & 5 \end{array} \right) \xrightarrow [ r _ {1} ^ {*} \times \left(- \frac {1}{9}\right) ]{r _ {1} - 5 r _ {2}} \left( \begin{array}{c c c} 0 & 1 & 1 \\ 1 & 2 & 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {1} ^ {* *} \leftrightarrow r _ {2} ^ {*} ]{r _ {2} - r _ {1} ^ {* *}} \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>由此可得<equation>\left\{ \begin{array}{l}x_{1} + x_{2} = 0,\\ x_{2} + x_{3} = 0, \end{array} \right.</equation>故<equation>\xi_3 = (1, -1, 1)^{\mathrm{T}}</equation>为它的一个基础解系.将<equation>\xi_3</equation>单位化得<equation>\alpha_{3} = \frac{1}{\sqrt{3}} (1, -1, 1)^{\mathrm{T}}.</equation>或者也可以如下求<equation>\alpha_{3}</equation>由于<equation>\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2}</equation>为属于不同特征值的特征向量，故它们相互正交。于是<equation>\boldsymbol {\alpha} _ {3} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {1} = 0, \quad \boldsymbol {\alpha} _ {3} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {2} = 0.</equation><equation>\pmb{\alpha}_{3}</equation>的坐标<equation>(x_{1}, x_{2}, x_{3})^{\mathrm{T}}</equation>满足<equation>\left\{ \begin{array}{l} x_{1} + 2x_{2} + x_{3} = 0, \\ x_{1} - x_{3} = 0. \end{array} \right.</equation>因此可得<equation>\pmb{\xi}_{3} = (1, -1, 1)^{\mathrm{T}}</equation>为此方程组的一个基础解系.将<equation>\pmb{\xi}_{3}</equation>单位化得<equation>\pmb{\alpha}_{3} = \frac{1}{\sqrt{3}} (1, -1, 1)^{\mathrm{T}}.</equation>因此，

---


