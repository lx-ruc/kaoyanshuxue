#### 伴随矩阵与可逆矩阵

**2017年第5题 | 选择题 | 4分 | 答案: A**

5. 设<equation>\alpha</equation>为 n维单位列向量，<equation>E</equation>为 n阶单位矩阵，则（    ）

A.<equation>E-\alpha\alpha^{\mathrm{T}}</equation>不可逆 B.<equation>E+\alpha\alpha^{\mathrm{T}}</equation>不可逆 C.<equation>E+2\alpha\alpha^{\mathrm{T}}</equation>不可逆 D.<equation>E-2\alpha\alpha^{\mathrm{T}}</equation>不可逆

答案: A

**解析:**解（法一）由于<equation>\boldsymbol{\alpha}</equation>是n维单位列向量，故<equation>\operatorname{tr}(\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}})=\boldsymbol{\alpha}^{\mathrm{T}}\boldsymbol{\alpha}=1</equation>因为<equation>\boldsymbol{\alpha}</equation>非零，所以<equation>r(\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}})\geqslant 1.</equation>又由于<equation>r(\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}})\leqslant r(\boldsymbol{\alpha})=1</equation>故<equation>r(\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}})=1.</equation>于是矩阵<equation>\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}}</equation>的全部特征值为1，0，…，0，从而<equation>E-\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}}</equation>的全部特征值为0，1，…，1.因此，<equation>E-\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}}</equation>不可逆.应选A.

同理可得，<equation>\boldsymbol{E} +\alpha\boldsymbol{\alpha}^{\mathrm{T}}</equation>的全部特征值为2，1，…，1；<equation>\boldsymbol{E} +2\alpha\boldsymbol{\alpha}^{\mathrm{T}}</equation>的全部特征值为3，1，…，1；<equation>\boldsymbol{E} -2\alpha\boldsymbol{\alpha}^{\mathrm{T}}</equation>的全部特征值为-1，1，…，1.因此它们均可逆.

（法二）由于<equation>(\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}})\boldsymbol{\alpha} = \boldsymbol{\alpha} \left( \boldsymbol{\alpha}^{\mathrm{T}}\boldsymbol{\alpha} \right) = \boldsymbol{\alpha}</equation>，故<equation>\left(\boldsymbol {E} - \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}}\right) \boldsymbol {\alpha} = \boldsymbol {\alpha} - \left(\boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}}\right) \boldsymbol {\alpha} = \boldsymbol {\alpha} - \boldsymbol {\alpha} = \mathbf {0} = 0 \boldsymbol {\alpha}.</equation>于是，0是<equation>E-\alpha\alpha^{\mathrm{T}}</equation>的一个特征值（或<equation>( E-\alpha\alpha^{\mathrm{T}} ) x=0</equation>有非零解<equation>\alpha).</equation>因此，<equation>E-\alpha\alpha^{\mathrm{T}}</equation>不可逆.应选A. （法三）排除法.

令<equation>\alpha = (1,0,\dots ,0)^{\mathrm{T}}</equation>，则<equation>\alpha \alpha^{\mathrm{T}} = \left( \begin{array}{c c c c} 1 & & & \\ & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right)</equation>.

可以验证，<equation>\mathbf{E} + \alpha \alpha^{\mathrm{T}},\mathbf{E} + 2\alpha \alpha^{\mathrm{T}},\mathbf{E} - 2\alpha \alpha^{\mathrm{T}}</equation>均可逆，从而可以排除选项B、C、D.因此，应选A.

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


