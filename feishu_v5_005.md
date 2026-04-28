---

**2013年第13题 | 填空题 | 4分**

13. 设<equation>A=\left(a_{ij}\right)</equation>是3阶非零矩阵，<equation>|A|</equation>为 A的行列式，<equation>A_{ij}</equation>为<equation>a_{ij}</equation>的代数余子式. 若<equation>a_{ij}+A_{ij}=0</equation>（i,j=1,2,3），则<equation>|A|=</equation>___

**解析:**首先，由题设可知<equation>\boldsymbol {A} ^ {*} = \left( \begin{array}{c c c} A _ {1 1} & A _ {2 1} & A _ {3 1} \\ A _ {1 2} & A _ {2 2} & A _ {3 2} \\ A _ {1 3} & A _ {2 3} & A _ {3 3} \end{array} \right) \xlongequal {\text {a} _ {i j} + A _ {i j} = 0} \left( \begin{array}{c c c} - a _ {1 1} & - a _ {2 1} & - a _ {3 1} \\ - a _ {1 2} & - a _ {2 2} & - a _ {3 2} \\ - a _ {1 3} & - a _ {2 3} & - a _ {3 3} \end{array} \right) = - \boldsymbol {A} ^ {\mathrm {T}},</equation>故<equation>|\mathbf{A}|^3 = |\mathbf{A}\mathbf{A}^*| = |-\mathbf{A}\mathbf{A}^{\mathrm{T}}| = -|\mathbf{A}|^2.</equation>因此可以得到<equation>|\mathbf{A}| = 0,</equation>或<equation>|\mathbf{A}| = -1.</equation>另一方面，由于<equation>A</equation>为非零矩阵，故不妨假设<equation>a_{11} \neq 0</equation>，则<equation>| \boldsymbol {A} | = a _ {1 1} A _ {1 1} + a _ {1 2} A _ {1 2} + a _ {1 3} A _ {1 3} = - \left(a _ {1 1} ^ {2} + a _ {1 2} ^ {2} + a _ {1 3} ^ {2}\right) < 0.</equation>因此，<equation>|A| = -1.</equation>

---

**2011年第6题 | 选择题 | 4分 | 答案: D**

6. 设<equation>A=\left( \alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4} \right)</equation>是4阶矩阵，<equation>A^{*}</equation>为A的伴随矩阵.若<equation>(1,0,1,0)^{\mathrm{T}}</equation>是方程组<equation>A x=0</equation>的一个基础解系，则<equation>A^{*} x=0</equation>的基础解系可为（    ）

A.<equation>\alpha_{1},\alpha_{3}</equation>B.<equation>\alpha_{1},\alpha_{2}</equation>C.<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>D.<equation>\alpha_{2},\alpha_{3},\alpha_{4}</equation>

答案: D

**解析:**解 由于<equation>( 1, 0, 1, 0 )^{\mathrm{T}}</equation>为<equation>A x=0</equation>的一个基础解系，故该方程组的解集的秩为1，从而<equation>r ( A )=3.</equation>由<equation>r ( A )</equation>与<equation>r ( A^{*} )</equation>的关系可得<equation>r ( A^{*} )=1.</equation>于是<equation>A^{*} x=0</equation>的解集的秩为3，基础解系应包含3个线性无关的向量.因此，可以排除选项A、B.

由于<equation>r ( \mathbf{A})=3</equation><equation>| \mathbf{A} |=0</equation><equation>A^{*} A=| A | E=O</equation>，故 A的列向量均为<equation>A^{*} x=0</equation>的解.又因为<equation>r ( \mathbf{A})=3</equation>，所以可以从 A的列向量组中找出3个线性无关的列向量作为<equation>A^{*} x=0</equation>的一个基础解系.另一方面，由于<equation>( 1,0,1,0 )^{\mathrm{T}}</equation>是方程组<equation>A x=0</equation>的一个基础解系，故<equation>\left( \alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4}\right) \left( 1,0,1,0\right)^{\mathrm{T}}=\alpha_{1}+\alpha_{3}=0.</equation>于是<equation>\alpha_{1}</equation>与<equation>\alpha_{2}</equation>线性相关，因此可以排除选项C.由排除法知，应选D：

---

**2009年第6题 | 选择题 | 4分 | 答案: B**

5. 设 A,B均为2阶矩阵，<equation>A^{*}，B^{*}</equation>分别为 A,B的伴随矩阵，若<equation>|A|=2,|B|=3</equation>，则分块矩阵<equation>\left( \begin{array}{cc} O&A \\ B/O \end{array} \right)</equation>的伴随矩阵为（    ）

A.<equation>\left( \begin{array}{cc} O&3 B^{*} \\ 2 A^{*}&O \end{array} \right)</equation>B.<equation>\left( \begin{array}{cc} O&2 B^{*} \\ 3 A^{*}&O \end{array} \right)</equation>C.<equation>\left( \begin{array}{cc} O&3 A^{*} \\ 2 B^{*}&O \end{array} \right)</equation>D.<equation>\left( \begin{array}{cc} O&2 A^{*} \\ 3 B^{*}&O \end{array} \right)</equation>

答案: B

**解析:**解 （法一）先求<equation>\left| \begin{array}{ll}O&A\\ B/O \end{array} \right|.</equation>记<equation>C=\left( \begin{array}{cc}O&A\\ B/O \end{array} \right), C</equation>为4阶矩阵，A位于它的第1，2行和第3，4列，可按照以下步骤把C变为<equation>\left( \begin{array}{cc}A&O\\ O&B \end{array} \right).</equation>把C的第3列与第1列对换，第4列与第2列对换.

因此，<equation>\left| \begin{array}{c c} O & A \\ B & O \end{array} \right| = (- 1) ^ {2} \left| \begin{array}{c c} A & O \\ O & B \end{array} \right| = | A | | B | = 6.</equation><equation>\left( \begin{array}{cc}O&A\\ BO\end{array} \right)</equation>可逆.

由可逆矩阵与其伴随矩阵的关系可知，<equation>\left( \begin{array}{c c} \boldsymbol {O} & \boldsymbol {A} \\ \boldsymbol {B} & \boldsymbol {O} \end{array} \right) ^ {*} = \left| \begin{array}{c c} \boldsymbol {O} & \boldsymbol {A} \\ \boldsymbol {B} & \boldsymbol {O} \end{array} \right| \left( \begin{array}{c c} \boldsymbol {O} & \boldsymbol {A} \\ \boldsymbol {B} & \boldsymbol {O} \end{array} \right) ^ {- 1} = 6 \left( \begin{array}{c c} \boldsymbol {O} & \boldsymbol {A} \\ \boldsymbol {B} & \boldsymbol {O} \end{array} \right) ^ {- 1}.</equation>不妨设<equation>\left( \begin{array}{cc}O&A\\ B/O \end{array} \right)^{-1} = \left( \begin{array}{cc}X_1 & X_2\\ X_3 & X_4 \end{array} \right)</equation>，则<equation>\left( \begin{array}{c c} O & A \\ B & O \end{array} \right) \left( \begin{array}{c c} X _ {1} & X _ {2} \\ X _ {3} & X _ {4} \end{array} \right) = \left( \begin{array}{c c} A X _ {3} & A X _ {4} \\ B X _ {1} & B X _ {2} \end{array} \right) = \left( \begin{array}{c c} E & O \\ O & E \end{array} \right).</equation>由于 A,B均为可逆矩阵，故由<equation>AX_{4} = O, BX_{1} = O</equation>可知，<equation>X_{1} = X_{4} = O</equation>；由<equation>AX_{3} = E, BX_{2} = E</equation>得，<equation>X_{3} = A^{-1}, X_{2} = B^{-1}</equation>.

因此，<equation>\left( \begin{array}{c c} \boldsymbol {O} & \boldsymbol {A} \\ \boldsymbol {B} & \boldsymbol {O} \end{array} \right) ^ {- 1} = \left( \begin{array}{c c} \boldsymbol {O} & \boldsymbol {B} ^ {- 1} \\ \boldsymbol {A} ^ {- 1} & \boldsymbol {O} \end{array} \right).</equation><equation>\left( \begin{array}{c c} O & A \\ B & O \end{array} \right) ^ {*} = 6 \left( \begin{array}{c c} O & B ^ {- 1} \\ A ^ {- 1} & O \end{array} \right) = 6 \left( \begin{array}{c c} O & \frac {B ^ {*}}{| B |} \\ \frac {A ^ {*}}{| A |} & O \end{array} \right) = \left( \begin{array}{c c} O & 2 B ^ {*} \\ 3 A ^ {*} & O _ {1} \end{array} \right).</equation>应选B.

（法二）不妨设<equation>\left( \begin{array}{cc}O&A\\ B/O \end{array} \right)^{*} = \left( \begin{array}{cc}X_{1} & X_{2}\\ X_{3} & X_{4} \end{array} \right).</equation>由法一知，<equation>\left| \begin{array}{cc}O&A\\ BO\end{array}\right|=6</equation>故<equation>\left( \begin{array}{c c} \boldsymbol {O} & \boldsymbol {A} \\ \boldsymbol {B} & \boldsymbol {O} \end{array} \right) \left( \begin{array}{c c} X _ {1} & X _ {2} \\ X _ {3} & X _ {4} \end{array} \right) = \left( \begin{array}{c c} \boldsymbol {A X} _ {3} & \boldsymbol {A X} _ {4} \\ \boldsymbol {B X} _ {1} & \boldsymbol {B X} _ {2} \end{array} \right) = \left( \begin{array}{c c} 6 \boldsymbol {E} & \boldsymbol {O} \\ \boldsymbol {O} & 6 \boldsymbol {E} \end{array} \right).</equation>从而，<equation>\boldsymbol {A} \boldsymbol {X} _ {3} = 6 \boldsymbol {E}, \quad \boldsymbol {B} \boldsymbol {X} _ {2} = 6 \boldsymbol {E}, \quad \boldsymbol {A} \boldsymbol {X} _ {4} = \boldsymbol {B} \boldsymbol {X} _ {1} = \boldsymbol {O}.</equation>由此可推出，<equation>X_{3}=6 A^{-1}=6 \frac{A^{*}}{\mid A\mid}=3 A^{*}, X_{2}=6 B^{-1}=6 \frac{B^{*}}{\mid B\mid}=2 B^{*}, X_{1}=X_{4}=O.</equation>因此，<equation>\left( \begin{array}{cc} O & A \\ B & O \end{array} \right)^{*} = \left( \begin{array}{cc} O & 2 B^{*} \\ 3 A^{*} & O \end{array} \right).</equation>应选B.

（法三）特殊值法.

取<equation>A=\sqrt{2} E, B=\sqrt{3} E</equation>满足<equation>| A |=2, | B |=3</equation>，则<equation>A^{*} = | A | A^{-1} = \sqrt{2} E, B^{*} = | B | B^{-1} =</equation><equation>\sqrt{3} E.</equation>因此，<equation>\begin{aligned} \binom {O} {B} \frac {A}{O}) ^ {*} &= \binom {O} {\sqrt {3} E} \frac {\sqrt {2} E}{O}) ^ {*} = \left| \begin{array}{c c} O & \sqrt {2} E \\ \sqrt {3} E & O  \right| \left( \begin{array}{c c} O & \sqrt {2} E \\ \sqrt {3} E & O  \right) ^ {- 1} &= 6 \cdot \left( \begin{array}{c c} O & \frac {1}{\sqrt {3}} E \\ \frac {1}{\sqrt {2}} E & O  \right) \\ &= \left( \begin{array}{c c} O & 2 \sqrt {3} E \\ 3 \sqrt {2} E & O  \right) &= \left( \begin{array}{c c} O & 2 B ^ {*} \\ 3 A ^ {*} & O  \right). \end{aligned}</equation>应选B.

---


### 矩阵的特征值与特征向量

#### 特征值与特征向量


**2025年第21题 | 解答题 | 12分**
21. 设矩阵<equation>A=\left( \begin{array}{c c c} 0 & -1 & 2 \\ -1 & 0 & 2 \\ -1 & -1 & a \end{array} \right)</equation>，已知1是A的特征多项式的重根.

I. 求 a的值；

II. 求所有满足<equation>A\alpha = \alpha + \beta ,A^{2}\alpha = \alpha + 2\beta</equation>的非零向量<equation>\alpha ,\beta .</equation>
**答案: **（Ⅱ）<equation>\begin{aligned} \alpha &= c_{1}\left( 2 \\ 0 \\ 1  \right)+c_{2}\left( 0 \\ 2 \\ 1  \right)+\left( \begin{array}{c}-k \\ 0 \\ 0  \right),\beta &= k\left( 1 \\ 1 \\ 1  \right) \end{aligned}</equation>，其中<equation>c_{1},c_{2}</equation>为任意常数，<equation>k</equation>为任意非零常数.
**解析: **解（I）计算 A的特征多项式.<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda & 1 & - 2 \\ 1 & \lambda & - 2 \\ 1 & 1 & \lambda - a  \right| \xlongequal {r _ {1} - r _ {2}} \left| \begin{array}{c c c} \lambda - 1 & 1 - \lambda & 0 \\ 1 & \lambda & - 2 \\ 1 & 1 & \lambda - a  \right| &= (\lambda - 1) \left| \begin{array}{c c c} 1 & - 1 & 0 \\ 1 & \lambda & - 2 \\ 1 & 1 & \lambda - a  \right| \\ &= (\lambda - 1) \left| \begin{array}{c c c} 1 & 0 & 0 \\ 1 & \lambda + 1 & - 2 \\ 1 & 2 & \lambda - a  \right| &= (\lambda - 1) \left[ \lambda^ {2} + (1 - a) \lambda - a + 4 \right]. \end{aligned}</equation>由于1是A的特征多项式的重根，故<equation>\lambda=1</equation>是<equation>\lambda^{2}+(1-a)\lambda-a+4=0</equation>的一个根.将<equation>\lambda=1</equation>代入该式得<equation>1+1-a-a+4=0</equation>，解得 a=3.

因此，<equation>a=3.</equation>（Ⅱ）由第（I）问可知，<equation>A=\left( \begin{array}{c c c} 0 & -1 & 2 \\ -1 & 0 & 2 \\ -1 & -1 & 3 \end{array} \right).</equation>由<equation>A\alpha = \alpha +\beta ,A^{2}\alpha = \alpha +2\beta</equation>可得，<equation>A ^ {2} \alpha = A (A \alpha) = A \alpha + A \beta = \alpha + \beta + A \beta = \alpha + 2 \beta .</equation>由此可得<equation>A\beta = \beta .</equation>考虑方程组（A-E）x=0.<equation>A - E = \left( \begin{array}{c c c} - 1 & - 1 & 2 \\ - 1 & - 1 & 2 \\ - 1 & - 1 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & - 2 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>\beta = k_{1}\left( \begin{array}{c}2\\ 0\\ 1 \end{array} \right)+k_{2}\left( \begin{array}{c}0\\ 2\\ 1 \end{array} \right)=\left( \begin{array}{c}2k_{1}\\ 2k_{2}\\ k_{1}+k_{2} \end{array} \right)</equation>，其中<equation>k_{1},k_{2}</equation>是不全为零的任意常数.

由<equation>A\alpha = \alpha +\beta</equation>可得<equation>(A - E)\alpha = \beta</equation>，即<equation>\alpha</equation>是方程组<equation>(A - E)x = \beta</equation>的非零解.<equation>(A - E, \beta) = \left( \begin{array}{c c c c} - 1 & - 1 & 2 & 2 k _ {1} \\ - 1 & - 1 & 2 & 2 k _ {2} \\ - 1 & - 1 & 2 & k _ {1} + k _ {2} \end{array} \right) \xrightarrow [ r _ {3} - r _ {1} ]{r _ {2} - r _ {1}} \left( \begin{array}{c c c c} - 1 & - 1 & 2 & 2 k _ {1} \\ 0 & 0 & 0 & 2 \left(k _ {2} - k _ {1}\right) \\ 0 & 0 & 0 & k _ {2} - k _ {1} \end{array} \right).</equation>由此可得，当且仅当<equation>k_{1} = k_{2}</equation>时，方程组<equation>(A - E)x = \beta</equation>有解. 从而，<equation>\beta = 2 k_{1}\left( \begin{array}{c}1\\ 1\\ 1 \end{array} \right) = k\left( \begin{array}{c}1\\ 1\\ 1 \end{array} \right)</equation>其中<equation>k=2 k_{1}</equation>为任意非零常数.

进一步可得方程组<equation>( A - E ) x = \beta</equation>的通解<equation>\alpha = c_{1}\left( \begin{array}{c} 2 \\ 0 \\ 1 \end{array} \right) + c_{2}\left( \begin{array}{c} 0 \\ 2 \\ 1 \end{array} \right) + \left( \begin{array}{c} - k \\ 0 \\ 0 \end{array} \right)</equation>，其中<equation>c_{1}, c_{2}</equation>为任意常数.又因为<equation>\beta\neq0</equation>，所以<equation>\alpha\neq0.</equation>因此，<equation>\alpha = c_{1}\left( \begin{array}{c}2\\ 0\\ 1 \end{array} \right) + c_{2}\left( \begin{array}{c}0\\ 2\\ 1 \end{array} \right) + \left( \begin{array}{c}-k\\ 0\\ 0 \end{array} \right),\beta = k\left( \begin{array}{c}1\\ 1\\ 1 \end{array} \right)</equation>，其中<equation>c_{1},c_{2}</equation>为任意常数，<equation>k</equation>为任意非零常数.

---

**2024年第7题 | 选择题 | 5分 | 答案: A**
7. 设 A是秩为2的3阶矩阵，<equation>\alpha</equation>是满足<equation>A\alpha=0</equation>的非零向量. 若对满足<equation>\beta^{\mathrm{T}}\alpha=0</equation>的3维列向量<equation>\beta</equation>，均有<equation>A\beta=\beta</equation>则（    )

A.<equation>A^{3}</equation>的迹为2 B.<equation>A^{3}</equation>的迹为5 C.<equation>A^{2}</equation>的迹为8 D.<equation>A^{2}</equation>的迹为9
答案: A
**解析: **由<equation>\alpha</equation>是满足<equation>A\alpha=0</equation>的非零向量可知，A有一个属于特征值0的特征向量<equation>\alpha.</equation>满足<equation>\beta^{\mathrm{T}}\alpha = 0</equation>的向量<equation>\beta</equation>也满足<equation>\alpha^{\mathrm{T}}\beta = 0</equation>，从而是<equation>\alpha^{\mathrm{T}}x = 0</equation>的解。由于该方程组的系数矩阵的秩为1，故该方程组有两个线性无关的解。于是，存在两个线性无关的向量<equation>\beta_{1},\beta_{2}</equation>，使得<equation>\alpha^{\mathrm{T}}\beta_{i} = 0(i = 1,2)</equation>，即<equation>\beta_{i}^{\mathrm{T}}\alpha = 0(i = 1,2)</equation>。结合满足<equation>\beta^{\mathrm{T}}\alpha = 0</equation>的向量均满足<equation>A\beta = \beta</equation>可知，<equation>A\beta_{1} = \beta_{1},A\beta_{2} = \beta_{2}</equation>，故<equation>\beta_{1},\beta_{2}</equation>是A的属于特征值1的两个线性无关的特征向量.

由于属于不同特征值的特征向量线性无关，故<equation>\alpha, \beta_{1}, \beta_{2}</equation>是A的三个线性无关的特征向量.又因为A是3阶矩阵，所以A的特征值为1，1，0.进一步可得<equation>A^{2}, A^{3}</equation>的特征值均为1，1，0，从而<equation>\operatorname{tr}(A^{2})=\operatorname{tr}(A^{3})=2.</equation>因此，应选A.

---

**2018年第13题 | 填空题 | 4分**
13. 设2阶矩阵 A有两个不同特征值，<equation>\alpha_{1},\alpha_{2}</equation>是 A的线性无关的特征向量，且满足<equation>A^{2}(\alpha_{1}+\alpha_{2})=\alpha_{1}+\alpha_{2}</equation>，则<equation>|A|=</equation>
**答案: **-1.
**解析: **解 由于<equation>\alpha_{1},\alpha_{2}</equation>是A的线性无关的特征向量，而A有两个不同的特征值，故不妨分别记A的两个特征值为<equation>\lambda_{1},\lambda_{2},\alpha_{1}</equation>为属于<equation>\lambda_{1}</equation>的特征向量，<equation>\alpha_{2}</equation>为属于<equation>\lambda_{2}</equation>的特征向量.

由特征值与特征向量的定义可知，<equation>A\alpha_{1} = \lambda_{1}\alpha_{1},A\alpha_{2} = \lambda_{2}\alpha_{2}</equation>，从而<equation>A^{2}\alpha_{1} = \lambda_{1}^{2}\alpha_{1},A^{2}\alpha_{2} = \lambda_{2}^{2}\alpha_{2}</equation>于是，<equation>\boldsymbol {\alpha} _ {1} + \boldsymbol {\alpha} _ {2} = \boldsymbol {A} ^ {2} \left(\boldsymbol {\alpha} _ {1} + \boldsymbol {\alpha} _ {2}\right) = \lambda_ {1} ^ {2} \boldsymbol {\alpha} _ {1} + \lambda_ {2} ^ {2} \boldsymbol {\alpha} _ {2}.</equation>由（1）式可得，<equation>\left(\lambda_{1}^{2}-1\right)\boldsymbol{\alpha}_{1}+\left(\lambda_{2}^{2}-1\right)\boldsymbol{\alpha}_{2}=\mathbf{0}</equation>. 由于<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2}</equation>线性无关，故<equation>\lambda_{1}^{2}-1=0,\lambda_{2}^{2}-1=0.</equation>于是，<equation>\lambda_{1}^{2}=\lambda_{2}^{2}=1.</equation>又因为<equation>\lambda_{1}\neq \lambda_{2}</equation>所以<equation>\lambda_{1}=1,\lambda_{2}=-1</equation>或<equation>\lambda_{1}=-1,\lambda_{2}=1.</equation>不论是哪种情况，都有<equation>|A| = \lambda_{1}\lambda_{2} = -1.</equation>

---

**2011年第21题 | 解答题 | 11分**

设<equation>A</equation>为3阶实对称矩阵，<equation>A</equation>的秩为2，且<equation>1 \left( \begin{array}{c c} 1 & 1 \\ 0 & 0 \\ - 1 & 1 \end{array} \right) = \left( \begin{array}{c c} - 1 & 1 \\ 0 & 0 \\ 1 & 1 \end{array} \right)</equation>I. 求 A的所有特征值与特征向量；

II. 求矩阵 A.
**答案: **(21) （I）矩阵 A的特征值为-1，1，0.对应的特征向量分别为<equation>k_{1}(1,0,-1)^{\mathrm{T}}</equation><equation>k_{2}(1,0,1)^{\mathrm{T}}</equation><equation>k_{3}(0,1,0)^{\mathrm{T}}</equation>，其中<equation>k_{1},k_{2},k_{3}</equation>为任意非零常数；<equation>(\mathrm {I I}) \boldsymbol {A} = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{array} \right)</equation>
**解析: **解（I）由于<equation>A\left( \begin{array}{c c} 1 & 1 \\ 0 & 0 \\ -1 & 1 \end{array} \right)=\left( \begin{array}{c c} -1 & 1 \\ 0 & 0 \\ 1 & 1 \end{array} \right)</equation>，故<equation>\alpha_{1}=(1,0,-1)^{\mathrm{T}},\alpha_{2}=(1,0,1)^{\mathrm{T}}</equation>满足<equation>A\alpha_{1}=</equation><equation>-\alpha_{1},A\alpha_{2}=\alpha_{2}</equation>，从而<equation>\alpha_{1}</equation>为A的属于特征值-1的特征向量，<equation>\alpha_{2}</equation>为A的属于特征值1的特征向量.又因为<equation>r(A)=2,|A|=0</equation>，所以A还有一个特征值为零.

因为实对称矩阵属于不同特征值的特征向量相互正交，所以A的属于特征值0的特征向量<equation>\boldsymbol{\alpha}_{3} = (x_{1},x_{2},x_{3})^{\mathrm{T}}</equation>满足<equation>\boldsymbol{\alpha}_{1}^{\mathrm{T}}\boldsymbol{\alpha}_{3} = 0, \boldsymbol{\alpha}_{2}^{\mathrm{T}}\boldsymbol{\alpha}_{3} = 0</equation>从而得<equation>\left\{ \begin{array}{l l} x_{1} - x_{3} = 0, \\ x_{1} + x_{3} = 0. \end{array} \right.</equation>由此可得<equation>\boldsymbol{\alpha}_{3} = k_{3}(0,1,0)^{\mathrm{T}}, k_{3}</equation>为任意非零常数.

因此，<equation>\mathbf{A}</equation>的特征值为-1,1,0.对应的特征向量分别为<equation>k_{1}(1,0,-1)^{\mathrm{T}}</equation><equation>k_{2}(1,0,1)^{\mathrm{T}}</equation><equation>k_{3}(0,1,0)^{\mathrm{T}}</equation>其中<equation>k_{1},k_{2},k_{3}</equation>为任意非零常数.

（Ⅱ）（法一）由第（I）问可知，取<equation>P=\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)=\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \\ -1 & 1 & 0 \end{array} \right)</equation>，可得<equation>P^{-1}AP=</equation><equation>\left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>.于是<equation>A=P\left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right) P^{-1}.</equation>利用初等变换法计算<equation>P^{-1}</equation><equation>\begin{array}{l} (\boldsymbol {P}, \boldsymbol {E}) = \left( \begin{array}{c c c c c c} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 1 & 0 \\ - 1 & 1 & 0 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} + r _ {1}} \left( \begin{array}{c c c c c c} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 1 & 0 \\ 0 & 2 & 0 & 1 & 0 & 1 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {*} \times \frac {1}{2}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & \frac {1}{2} & 0 & - \frac {1}{2} \\ 0 & 0 & 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & \frac {1}{2} & 0 & \frac {1}{2} \end{array} \right) \xrightarrow {r _ {2} \leftrightarrow r _ {3} ^ {* *}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & \frac {1}{2} & 0 & - \frac {1}{2} \\ 0 & 1 & 0 & \frac {1}{2} & 0 & \frac {1}{2} \\ 0 & 0 & 1 & 0 & 1 & 0 \end{array} \right). \\ \end{array}</equation>于是，<equation>P^{-1}=\left( \begin{array}{c c c} \frac{1}{2} & 0 & -\frac{1}{2} \\ \frac{1}{2} & 0 & \frac{1}{2} \\ 0 & 1 & 0 \end{array} \right).</equation>因此，<equation>\begin{aligned} \boldsymbol {A} &= \boldsymbol {P} \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \boldsymbol {P} ^ {- 1} &= \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \\ - 1 & 1 & 0  \right) \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \left( \begin{array}{c c c} \frac {1}{2} & 0 & - \frac {1}{2} \\ \frac {1}{2} & 0 & \frac {1}{2} \\ 0 & 1 & 0  \right) \\ &= \left( \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & 0 & 0 \\ 1 & 1 & 0  \right) \left( \begin{array}{c c c} \frac {1}{2} & 0 & - \frac {1}{2} \\ \frac {1}{2} & 0 & \frac {1}{2} \\ 0 & 1 & 0  \right) &= \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0  \right). \end{aligned}</equation>或者，由<equation>\boldsymbol {A P} = \left(\boldsymbol {A} \alpha_ {1}, \boldsymbol {A} \alpha_ {2}, \boldsymbol {A} \alpha_ {3}\right) = \left(- \alpha_ {1}, \alpha_ {2}, 0\right)</equation>可得，<equation>\boldsymbol {A} = \left(- \alpha_ {1}, \alpha_ {2}, 0\right) \boldsymbol {P} ^ {- 1} = - \frac {1}{2} \left( \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & 0 & 0 \\ 1 & 1 & 0 \end{array} \right) \left( \begin{array}{c c c} - 1 & 0 & 1 \\ - 1 & 0 & - 1 \\ 0 & - 2 & 0 \end{array} \right) = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{array} \right).</equation>（法二）将<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>单位化，组成一正交矩阵<equation>Q = \left( \begin{array}{c c c} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0 \\ 0 & 0 & 1 \\ -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0 \end{array} \right)</equation>，则<equation>Q^{\mathrm{T}}AQ = \left( \begin{array}{c c c} -1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>.

因此，<equation>\begin{aligned} \boldsymbol {A} &= \boldsymbol {Q} \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \boldsymbol {Q} ^ {\mathrm {T}} &= \left( \begin{array}{c c c} \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {2}} & 0 \\ 0 & 0 & 1 \\ - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {2}} & 0  \right) \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \left( \begin{array}{c c c} \frac {1}{\sqrt {2}} & 0 & - \frac {1}{\sqrt {2}} \\ \frac {1}{\sqrt {2}} & 0 & \frac {1}{\sqrt {2}} \\ 0 & 1 & 0  \right) \\ &= \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0  \right). \end{aligned}</equation>

---

**2009年第13题 | 填空题 | 4分**
13. 若 3 维列向量<equation>\alpha, \beta</equation>满足<equation>\alpha^{\mathrm{T}}\beta=2</equation>, 其中<equation>\alpha^{\mathrm{T}}</equation>为<equation>\alpha</equation>的转置, 则矩阵<equation>\beta\alpha^{\mathrm{T}}</equation>的非零特征值为 ___
**解析: **解 由于<equation>r(\beta\alpha^{\mathrm{T}})\leqslant r(\beta)=1</equation>且<equation>\alpha, \beta</equation>均为非零向量，故<equation>r(\beta\alpha^{\mathrm{T}})=1.</equation>由分析中所给结论知，矩阵<equation>\beta\alpha^{\mathrm{T}}</equation>的所有特征值为<equation>\operatorname{tr}(\beta\alpha^{\mathrm{T}}),0,0.</equation>又<equation>\operatorname{tr}(\beta\alpha^{\mathrm{T}})=\operatorname{tr}(\alpha^{\mathrm{T}}\beta)=2</equation>（这里利用了<equation>\operatorname{tr}(AB)=\operatorname{tr}(BA)</equation>或者直接根据定义得<equation>\operatorname{tr}(\beta\alpha^{\mathrm{T}})=\alpha^{\mathrm{T}}\beta=2)</equation>，故矩阵<equation>\beta\alpha^{\mathrm{T}}</equation>的非零特征值为2.

---


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
