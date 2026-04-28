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


