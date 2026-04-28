---

**2010年第14题 | 填空题 | 4分**
14. 设<equation>A, B</equation>为3阶矩阵，且<equation>|A| = 3, |B| = 2, |A^{-1} + B| = 2</equation>，则<equation>|A + B^{-1}</equation>
**解析: **由于<equation>A, B</equation>的行列式均不为零，故它们均可逆.因为<equation>\boldsymbol {A} \left(\boldsymbol {A} ^ {- 1} + \boldsymbol {B}\right) \boldsymbol {B} ^ {- 1} = \boldsymbol {B} ^ {- 1} + \boldsymbol {A} = \boldsymbol {A} + \boldsymbol {B} ^ {- 1},</equation>所以<equation>| A + B ^ {- 1} | = | A | \cdot | A ^ {- 1} + B | \cdot | B ^ {- 1} | \frac {| B ^ {- 1} | = \frac {1}{| B |}}{\underline {{}}} 3 \times 2 \times \frac {1}{2} = 3.</equation>

---

**2009年第8题 | 选择题 | 4分**
8. 设<equation>A, P</equation>均为3阶矩阵，<equation>P^{\mathrm{T}}</equation>为<equation>P</equation>的转置矩阵，且<equation>P^{\mathrm{T}}AP = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>. 若<equation>P = \left(\alpha_{1}, \alpha_{2}, \alpha_{3}\right)</equation>，<equation>Q = \left(\alpha_{1} + \alpha_{2}, \alpha_{2}, \alpha_{3}\right)</equation>，

则<equation>Q^{\mathrm{T}} A Q</equation>为（    ）

A.<equation>\left( \begin{array}{c c c} 2 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>3.<equation>\left( \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>B.

C.<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>
**解析: **解 由题设知，<equation>Q</equation>为把<equation>P</equation>的第2列加到第1列的结果，故<equation>Q=P\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>.从<equation>\begin{aligned} Q ^ {\mathrm {T}} A Q &= \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1  \right) P ^ {\mathrm {T}} A P \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1  \right) &= \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1  \right) \\ &= \left( \begin{array}{c c c} 2 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 2  \right). \end{aligned}</equation>应选A.

---


#### 矩阵的秩


**2024年第9题 | 选择题 | 5分 | 答案: D**
9. 设 A为4阶矩阵，<equation>A^{*}</equation>为 A的伴随矩阵. 若<equation>A(A-A^{*})=O</equation>，且<equation>A\neq A^{*}</equation>，则 r(A)的取值为（

A.0或1 B.1或3 C.2或3 D.1或2
答案: D
**解析: **解由<equation>A(A - A^{*}) = O</equation>可得，<equation>r(A) + r(A - A^{*})\leqslant 4.</equation>结合<equation>A - A^{*}\neq O</equation>，从而<equation>r(A - A^{*})\geqslant</equation>1可得，<equation>r(A)\leqslant 3.</equation>于是，<equation>|A| = 0,AA^{*} = O.</equation>进一步由<equation>A(A - A^{*}) = O</equation>可得，<equation>A^{2} = O.</equation>由<equation>A^{2} = O</equation>可得，<equation>2r(A)\leqslant 4</equation>，即<equation>r(A)\leqslant 2</equation>.当<equation>r(A)\leqslant 2</equation>时，<equation>r(A^{*}) = 0</equation>，即<equation>A^{*} = O.</equation>由于<equation>A\neq A^{*}</equation>，故<equation>A\neq O</equation>，从而<equation>r(A)\geqslant 1.</equation>因此，<equation>r(\mathbf{A})</equation>的取值为1或2，应选D.

下面举例说明<equation>r(A) = 1</equation>与<equation>r(A) = 2</equation>均可能实现.

取<equation>A = \left( \begin{array}{cccc} 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{array} \right)</equation>，则<equation>r(A) = 1, A^{*} = O, A \neq A^{*}</equation>，且<equation>A^{2} = O.</equation>取<equation>A = \left( \begin{array}{cccc} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{array} \right)</equation>，则<equation>r(A) = 2, A^{*} = O, A \neq A^{*}</equation>，且<equation>A^{2} = O.</equation>

---

**2018年第8题 | 选择题 | 4分 | 答案: A**
8. 设 A,B为 n阶矩阵，记 r(X)为矩阵 X的秩，(X,Y)表示分块矩阵，则（    ）

A.<equation>r ( A, A B )=r ( A )</equation>B.<equation>r ( A, B A )=r ( A )</equation>C.<equation>r ( A, B )=\max \{ r ( A ) , r ( B ) \}</equation>D.<equation>r ( A, B )=r \left( A^{\mathrm{T}}, B^{\mathrm{T}} \right)</equation>
答案: A
**解析: **解记 C=AB.由于右乘矩阵表示对矩阵作列变换，故 C的列向量可由 A的列向量线性表示.于是，<equation>r ( A, C )=r ( A, A B )=r ( A ).</equation>因此，应选A.

下面分别说明选项B、C、D不正确.

选项B：<equation>r ( A, B A ) \geqslant r ( A )</equation>.但是，<equation>r ( A, B A ) = r ( A )</equation>并不成立.

取<equation>A=\left( \begin{array}{ll}1&0\\ 0&0 \end{array} \right), B=\left( \begin{array}{ll}1&0\\ 1&1 \end{array} \right)</equation>，则<equation>B A=\left( \begin{array}{ll}1&0\\ 1&0 \end{array} \right), (A, B A)=\left( \begin{array}{lll}1&0&1&0\\ 0&0&1&0 \end{array} \right). r(A, B A)=2</equation>，但<equation>r(A)=1.</equation>选项 C：<equation>r ( A, B ) \geqslant\max \left\{r ( A ) , r ( B ) \right\}</equation>.但是，<equation>r ( A, B )=\max \left\{r ( A ) , r ( B ) \right\}</equation>并不成立.

取<equation>A = \left( \begin{array}{ll}1 & 0\\ 0 & 0 \end{array} \right),B = \left( \begin{array}{ll}0 & 0\\ 1 & 0 \end{array} \right)</equation>，则<equation>(A,B) = \left( \begin{array}{lll}1 & 0 & 0 & 0\\ 0 & 0 & 1 & 0 \end{array} \right),r(A,B) = 2</equation>，但<equation>r(A) = r(B) = 1.</equation>选项D：由于<equation>r(\mathbf{P})=r(\mathbf{P}^{\mathrm{T}})</equation>，而<equation>(\mathbf{A},\mathbf{B})^{\mathrm{T}}=\binom{\mathbf{A}^{\mathrm{T}}}{\mathbf{B}^{\mathrm{T}}}</equation>，故<equation>r(\mathbf{A},\mathbf{B})=r\binom{\mathbf{A}^{\mathrm{T}}}{\mathbf{B}^{\mathrm{T}}}</equation>.但是，<equation>r(\mathbf{A},\mathbf{B})= r(\mathbf{A}^{\mathrm{T}},\mathbf{B}^{\mathrm{T}})</equation>并不成立.

取<equation>A=\left( \begin{array}{cc}1&0\\ 0&0 \end{array} \right), B=\left( \begin{array}{cc}0&0\\ 1&0 \end{array} \right)</equation>，则<equation>(\mathbf{A},\mathbf{B})=\left( \begin{array}{cccc}1&0&0&0\\ 0&0&1&0 \end{array} \right),(\mathbf{A}^{\mathrm{T}},\mathbf{B}^{\mathrm{T}})=\left( \begin{array}{cccc}1&0&0&1\\ 0&0&0&0 \end{array} \right). r(\mathbf{A},\mathbf{B})=2</equation>但<equation>r(\mathbf{A}^{\mathrm{T}},\mathbf{B}^{\mathrm{T}})=1.</equation>

---

**2016年第14题 | 填空题 | 4分**
14. 设矩阵<equation>\left( \begin{array}{c c c} a & - 1 & - 1 \\ - 1 & a & - 1 \\ - 1 & - 1 & a \end{array} \right)</equation>与矩阵<equation>\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & - 1 & 1 \\ 1 & 0 & 1 \end{array} \right)</equation>等价，则 a = ___
**解析: **解（法一）记<equation>A=\left( \begin{array}{c c c} a & -1 & -1 \\ -1 & a & -1 \\ -1 & -1 & a \end{array} \right), B=\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & -1 & 1 \\ 1 & 0 & 1 \end{array} \right).</equation><equation>\boldsymbol {B} = \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & - 1 & 1 \\ 1 & 0 & 1 \end{array} \right) \xrightarrow {r _ {1} + r _ {2}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & - 1 & 1 \\ 1 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} - r _ {1} ^ {*}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & - 1 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个 *.）于是<equation>r(B)=2.</equation>由于<equation>A, B</equation>等价，故<equation>r(A) = r(B) = 2</equation>，从而<equation>|A| = 0.</equation>另一方面，计算<equation>|A|</equation>得，<equation>| A | = \left| \begin{array}{c c c} a & - 1 & - 1 \\ - 1 & a & - 1 \\ - 1 & - 1 & a \end{array} \right| = (a + 1) ^ {2} (a - 2).</equation>| A | = 0当且仅当 a=-1或 a=2.当 a=-1时，<equation>r ( A )=1</equation>，不符合题意.因此， a=2. （法二）由法一知，<equation>r ( B )=2.</equation>对A作初等行变换，<equation>\boldsymbol {A} = \left( \begin{array}{c c c} a & - 1 & - 1 \\ - 1 & a & - 1 \\ - 1 & - 1 & a \end{array} \right) \xrightarrow [ r _ {1} \leftrightarrow r _ {3} ^ {*} ]{r _ {3} \times (- 1)} \left( \begin{array}{c c c} 1 & 1 & - a \\ - 1 & a & - 1 \\ a & - 1 & - 1 \end{array} \right) \xrightarrow [ r _ {3} ^ {* *} - a r _ {1} ^ {*} ]{r _ {2} + r _ {1} ^ {*}} \left( \begin{array}{c c c} 1 & 1 & - a \\ 0 & a + 1 & - a - 1 \\ 0 & - a - 1 & a ^ {2} - 1 \end{array} \right)</equation><equation>\xrightarrow {r _ {3} ^ {* * *} + r _ {2} ^ {*}} \left( \begin{array}{c c c} 1 & 1 & - a \\ 0 & a + 1 & - a - 1 \\ 0 & 0 & a ^ {2} - a - 2 \end{array} \right).</equation>当<equation>a^{2}-a-2=0</equation>，即 a=-1或 a=2时，<equation>r(A)<3.</equation>又由于当 a=-1时，<equation>r(A)=1\neq r(B)</equation>，故舍去.

因此，<equation>a = 2</equation>

---


#### 伴随矩阵与可逆矩阵


**2023年第8题 | 选择题 | 5分 | 答案: D**

3. 设 A,B为 n阶可逆矩阵，E为 n阶单位矩阵，<equation>M^{*}</equation>为矩阵 M的伴随矩阵，则<equation>\left( \begin{array}{cc} A & E \\ O & B \end{array} \right)^{*}=(\quad)</equation>A.<equation>\left( \begin{array}{c c} | A | B^{*} & - B^{*} A^{*} \\ O & | B | A^{*} \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c} | A | B^{*} & - A^{*} B^{*} \\ O & | B | A^{*} \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c} | B | A^{*} & - B^{*} A^{*} \\ O & | A | B^{*} \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c} | B | A^{*} & - A^{*} B^{*} \\ O & | A | B^{*} \end{array} \right)</equation>

答案: D

**解析:**解（法一）由于 A,B都可逆，故可以作初等行变换来求<equation>\left( \begin{array}{cc} A & E \\ O & B \end{array} \right)^{-1}.</equation><equation>\left( \begin{array}{c c c c} A & E & E & O \\ O & B & O & E \end{array} \right) \xrightarrow {\textcircled{1}} \left( \begin{array}{c c c c} E & A ^ {- 1} & A ^ {- 1} & O \\ O & E & O & B ^ {- 1} \end{array} \right) \xrightarrow {\textcircled{2}} \left( \begin{array}{c c c c} E & O & A ^ {- 1} & - A ^ {- 1} B ^ {- 1} \\ O & E & O & B ^ {- 1} \end{array} \right),</equation>其中操作<equation>\textcircled{1}</equation>对应左乘可逆矩阵<equation>\left( \begin{array}{cc} A^{-1} & O \\ O & B^{-1} \end{array} \right)</equation>，操作<equation>\textcircled{2}</equation>对应左乘可逆矩阵<equation>\left( \begin{array}{cc} E & -A^{-1} \\ O & E \end{array} \right)</equation>.于是，<equation>\left( \begin{array}{c c} A & E \\ O & B \end{array} \right) ^ {- 1} = \left( \begin{array}{c c} A ^ {- 1} & - A ^ {- 1} B ^ {- 1} \\ O & B ^ {- 1} \end{array} \right).</equation>对于任意 n阶方阵 M，都有<equation>M M^{*} = | M | E</equation>，从而当 M可逆时，<equation>M^{*} = | M | M^{-1}.</equation>又因为<equation>\left| \begin{array}{l l} A & E \\ O & B \end{array} \right| = | A | | B |</equation>，所以<equation>\left( \begin{array}{c c} A & E \\ O & B \end{array} \right) ^ {*} = \left| \begin{array}{c c} A & E \\ O & B \end{array} \right| \left( \begin{array}{c c} A & E \\ O & B \end{array} \right) ^ {- 1} = | A | | B | \left( \begin{array}{c c} A ^ {- 1} & - A ^ {- 1} B ^ {- 1} \\ O & B ^ {- 1} \end{array} \right) = \left( \begin{array}{c c} | B | A ^ {*} & - A ^ {*} B ^ {*} \\ O & | A | B ^ {*} \end{array} \right).</equation>因此，应选D.

也可以如下计算<equation>\left( \begin{array}{cc}A&E\\ O&B \end{array} \right)^{-1}</equation>.

设<equation>\left( \begin{array}{cc} A & E \\ O & B \end{array} \right)^{-1}=\left( \begin{array}{cc} X_{1} & X_{2} \\ X_{3} & X_{4} \end{array} \right),</equation>则<equation>\left( \begin{array}{c c} A & E \\ O & B \end{array} \right) \left( \begin{array}{c c} X _ {1} & X _ {2} \\ X _ {3} & X _ {4} \end{array} \right) = \left( \begin{array}{c c} A X _ {1} + X _ {3} & A X _ {2} + X _ {4} \\ B X _ {3} & B X _ {4} \end{array} \right) = \left( \begin{array}{c c} E & O \\ O & E \end{array} \right).</equation>于是，<equation>\left\{ \begin{array}{l l} A X_{1}+X_{3}=E, \\ A X_{2}+X_{4}=O, \\ B X_{3}=O, \\ B X_{4}=E. \end{array} \right.</equation>由A，B均为可逆矩阵可得<equation>\left\{ \begin{array}{l l} X_{1}=A^{-1}, \\ X_{2}=-A^{-1}B^{-1}, \\ X_{3}=O, \\ X_{4}=B^{-1}. \end{array} \right.</equation>从而<equation>\left( \begin{array}{c c} A & E \\ O & B \end{array} \right) ^ {- 1} = \left( \begin{array}{c c} A ^ {- 1} & - A ^ {- 1} B ^ {- 1} \\ O & B ^ {- 1} \end{array} \right).</equation>（法二）分别记选项A、B、C、D中的矩阵为<equation>M_{1}, M_{2}, M_{3}, M_{4}</equation>，记<equation>\left( \begin{array}{cc} A & E \\ O & B \end{array} \right)=M.</equation>考虑<equation>M_{i}M (i=1,</equation>2,3,4). 若<equation>M_{i}=M^{*}</equation>，则<equation>M_{i}M=|A||B|E_{2n}.</equation>观察可得<equation>M_{1}M</equation>与<equation>M_{2}M</equation>的“第一列”均为<equation>\left( \begin{array}{c c} {| A | B^{*} A} \\ {O} \end{array} \right)</equation>，故<equation>M _ {1} M \neq | A | | B | E _ {2 n}, \quad M _ {2} M \neq | A | | B | E _ {2 n}.</equation>选项A、B均不正确.

又因为<equation>\begin{aligned} \left( \begin{array}{c c c} | B | A ^ {*} & - B ^ {*} A ^ {*} \\ O & | A | B ^ {*}  \right) \left( \begin{array}{c c} A & E \\ O & B  \right) &= \left( \begin{array}{c c c} | A | | B | E & | B | A ^ {*} - B ^ {*} A ^ {*} B \\ O & | A | | B | E  \right) \neq | A | | B | E _ {2 n}, \\ \left( \begin{array}{c c c} | B | A ^ {*} & - A ^ {*} B ^ {*} \\ O & | A | B ^ {*}  \right) \left( \begin{array}{c c} A & E \\ O & B  \right) &= \left( \begin{array}{c c c} | A | | B | E & | B | A ^ {*} - A ^ {*} B ^ {*} B \\ O & | A | | B | E  \right) &= | A | | B | E _ {2 n}, \end{aligned}</equation>所以选项C不正确，选项D正确. 应选D.

---

**2020年第7题 | 选择题 | 4分 | 答案: C**

7. 设4阶矩阵<equation>A=(a_{ij})</equation>不可逆，<equation>a_{12}</equation>代数余子式<equation>A_{12}\neq0,\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4}</equation>为矩阵 A的列向量组，<equation>A^{*}</equation>为 A伴随矩阵，则方程组<equation>A^{*}x=0</equation>通解为（    )

A.<equation>x=k_{1}\alpha_{1}+k_{2}\alpha_{2}+k_{3}\alpha_{3}</equation>，其中<equation>k_{1},k_{2},k_{3}</equation>为任意常数

B.<equation>x=k_{1}\alpha_{1}+k_{2}\alpha_{2}+k_{3}\alpha_{4}</equation>，其中<equation>k_{1},k_{2},k_{3}</equation>为任意常数

C.<equation>x=k_{1}\alpha_{1}+k_{2}\alpha_{3}+k_{3}\alpha_{4}</equation>，其中<equation>k_{1},k_{2},k_{3}</equation>为任意常数

D.<equation>x=k_{1}\alpha_{2}+k_{2}\alpha_{3}+k_{3}\alpha_{4}</equation>，其中<equation>k_{1},k_{2},k_{3}</equation>为任意常数

答案: C

**解析:**解 由 A不可逆可知，<equation>|A|=0</equation>.于是，<equation>A^{*}A=|A|E=0</equation>.从而， A的列向量均为<equation>A^{*}x=0</equation>的解.另一方面，<equation>A_{12}\neq0</equation>，说明<equation>A^{*}</equation>中有非零元素，<equation>r(A^{*})\geqslant1</equation>.又因为 A不可逆，所以<equation>r(A)\leqslant3</equation>.但是当<equation>r(A)<3</equation>时，<equation>r(A^{*})=0</equation>.因此，<equation>r(A)=3</equation><equation>r(A^{*})=1</equation><equation>A^{*}x=0</equation>的基础解系中包含3个解向量.

由<equation>A_{12}\neq0</equation>可知，<equation>\left| \begin{array}{c c c} a_{21} & a_{23} & a_{24} \\ a_{31} & a_{33} & a_{34} \\ a_{41} & a_{43} & a_{44} \end{array} \right| \neq0</equation>.于是，<equation>\left( \begin{array}{l} a_{21} \\ a_{31} \\ a_{41} \end{array} \right), \left( \begin{array}{l} a_{23} \\ a_{33} \\ a_{43} \end{array} \right), \left( \begin{array}{l} a_{24} \\ a_{34} \\ a_{44} \end{array} \right)</equation>线性无关.由分析中的结论可知，<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>线性无关，从而构成<equation>A^{*}x = 0</equation>的一个基础解系.

因此，<equation>A^{*}x=0</equation>的通解可写为<equation>x=k_{1}\alpha_{1}+k_{2}\alpha_{3}+k_{3}\alpha_{4}</equation>其中<equation>k_{1},k_{2},k_{3}</equation>为任意常数.应选C.

---

**2019年第7题 | 选择题 | 4分 | 答案: A**

7. 假设 A是4阶矩阵，<equation>A^{*}</equation>是 A的伴随矩阵，若线性方程组<equation>A x=0</equation>的基础解系中只有2个向量，则<equation>r \left( A^{*} \right)=</equation>(    )

A.0 B.1 C.2 D.3

答案: A

**解析:**解 由于<equation>A x=0</equation>的基础解系中只含有2个向量，故<equation>r(A)=4-2=2</equation>又因为<equation>r(A)=2< 4-1</equation>所以<equation>r(A^{*})=0.</equation>因此，应选A.

---

**2013年第14题 | 填空题 | 4分**

14. 设<equation>A=(a_{ij})</equation>是3阶非零矩阵，<equation>|A|</equation>为 A的行列式，<equation>A_{ij}</equation>为<equation>a_{ij}</equation>的代数余子式. 若<equation>a_{ij}+A_{ij}=0</equation>（i,j=1,2,3），则<equation>|A|=</equation>___

**解析:**首先，由题设可知<equation>\boldsymbol {A} ^ {*} = \left( \begin{array}{c c c} A _ {1 1} & A _ {2 1} & A _ {3 1} \\ A _ {1 2} & A _ {2 2} & A _ {3 2} \\ A _ {1 3} & A _ {2 3} & A _ {3 3} \end{array} \right) \xlongequal {\text {一}} \frac {a _ {i j} + A _ {i j} = 0}{\text {一}} \left( \begin{array}{c c c} - a _ {1 1} & - a _ {2 1} & - a _ {3 1} \\ - a _ {1 2} & - a _ {2 2} & - a _ {3 2} \\ - a _ {1 3} & - a _ {2 3} & - a _ {3 3} \end{array} \right) = - \boldsymbol {A} ^ {\mathrm {T}},</equation>故<equation>|\mathbf{A}|^3 = |\mathbf{A}\mathbf{A}^*| = |-\mathbf{A}\mathbf{A}^{\mathrm{T}}| = -|\mathbf{A}|^2.</equation>因此可以得到<equation>|\mathbf{A}| = 0,</equation>或<equation>|\mathbf{A}| = -1.</equation>另一方面，由于<equation>A</equation>为非零矩阵，故不妨假设<equation>a_{11} \neq 0</equation>，则<equation>| \boldsymbol {A} | = a _ {1 1} A _ {1 1} + a _ {1 2} A _ {1 2} + a _ {1 3} A _ {1 3} = - \left(a _ {1 1} ^ {2} + a _ {1 2} ^ {2} + a _ {1 3} ^ {2}\right) < 0.</equation>因此，<equation>|A| = -1.</equation>

---

**2012年第14题 | 填空题 | 4分**

14. 设<equation>A</equation>为3阶矩阵，<equation>|A|=3</equation><equation>A^{*}</equation>为<equation>A</equation>的伴随矩阵，若交换<equation>A</equation>的第1行与第2行得矩阵<equation>B</equation>，则<equation>|BA^{*}|=</equation>___.

**解析:**解（法一）由于<equation>B</equation>为交换<equation>A</equation>的第1行与第2行所得，故<equation>B = E(1,2)A.</equation>从而<equation>\boldsymbol {B} \boldsymbol {A} ^ {*} = \boldsymbol {E} (1, 2) \boldsymbol {A} \boldsymbol {A} ^ {*} = \boldsymbol {E} (1, 2) | \boldsymbol {A} | \boldsymbol {E} = 3 \boldsymbol {E} (1, 2).</equation>因此，<equation>\left| B A ^ {*} \right| = \left| 3 E (1, 2) \right| = 3 ^ {3} \left| \begin{array}{c c c} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right| = - 2 7.</equation>（法二）由于<equation>A A^{*} = |A|E</equation>，故当A为3阶矩阵时，<equation>| \boldsymbol {A} | \cdot | \boldsymbol {A} ^ {*} | = | \boldsymbol {A A} ^ {*} | = \left| \begin{array}{c c c} | \boldsymbol {A} | & 0 & 0 \\ 0 & | \boldsymbol {A} | & 0 \\ 0 & 0 & | \boldsymbol {A} | \end{array} \right| = | \boldsymbol {A} | ^ {3}.</equation>从而<equation>|A^{*}| = |A|^{2}.</equation>另一方面，由于<equation>B</equation>为交换<equation>A</equation>的第1行与第2行所得矩阵，故<equation>|B| = -|A|</equation>.因此，<equation>| B A ^ {*} | = | B | \cdot | A ^ {*} | = - | A | \cdot | A | ^ {2} = - 2 7.</equation>

---

**2011年第8题 | 选择题 | 4分 | 答案: D**

8. 设<equation>A=\left( \alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4} \right)</equation>是4阶矩阵，<equation>A^{*}</equation>为A的伴随矩阵.若<equation>(1,0,1,0)^{\mathrm{T}}</equation>是方程组<equation>A x=0</equation>的一个基础解系，则<equation>A^{*} x=0</equation>的基础解系可为（    ）

A.<equation>\alpha_{1},\alpha_{3}</equation>B.<equation>\alpha_{1},\alpha_{2}</equation>C.<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>D.<equation>\alpha_{2},\alpha_{3},\alpha_{4}</equation>

答案: D

**解析:**解 由于<equation>( 1,0,1,0 )^{\mathrm{T}}</equation>为<equation>A x=0</equation>的一个基础解系，故该方程组的解集的秩为1，从而<equation>r ( A )=3.</equation>由<equation>r ( A )</equation>与<equation>r ( A^{*} )</equation>的关系可得<equation>r ( A^{*} )=1.</equation>于是<equation>A^{*} x=0</equation>的解集的秩为3，基础解系应包含3个线性无关的向量.因此，可以排除选项A、B.

由于<equation>r(A) = 3, |A| = 0, A^{*}A = |A|E = O</equation>，故<equation>A</equation>的列向量均为<equation>A^{*}x = 0</equation>的解。又因为<equation>r(A) = 3</equation>，所以可以从<equation>A</equation>的列向量组中找出3个线性无关的列向量作为<equation>A^{*}x = 0</equation>的一个基础解系.

另一方面，由于<equation>(1,0,1,0)^{\mathrm{T}}</equation>是方程组<equation>Ax = 0</equation>的一个基础解系，故<equation>\left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\alpha} _ {2}, \boldsymbol {\alpha} _ {3}, \boldsymbol {\alpha} _ {4}\right) (1, 0, 1, 0) ^ {\mathrm {T}} = \boldsymbol {\alpha} _ {1} + \boldsymbol {\alpha} _ {3} = \mathbf {0}.</equation>于是<equation>\alpha_{1}</equation>与<equation>\alpha_{3}</equation>线性相关，因此可以排除选项C.由排除法知，应选D.

---

**2009年第7题 | 选择题 | 4分 | 答案: B**

7. 设 A,B均为2阶方阵，<equation>A^{*}，B^{*}</equation>分别为 A,B的伴随矩阵.若<equation>|A|=2,|B|=3</equation>，则分块矩阵<equation>\left( \begin{array}{cc} O&A \\ B/O \end{array} \right)</equation>的伴随矩阵为（    )

A.<equation>\left( \begin{array}{cc} O&3 B^{*} \\ 2 A^{*}&O \end{array} \right)</equation>B.<equation>\left( \begin{array}{cc} O&2 B^{*} \\ 3 A^{*}&O \end{array} \right)</equation>C.<equation>\left( \begin{array}{cc} O&3 A^{*} \\ 2 B^{*}&O \end{array} \right)</equation>D.<equation>\left( \begin{array}{cc} O&2 A^{*} \\ 3 B^{*}&O \end{array} \right)</equation>

答案: B

**解析:**解 （法一）先求<equation>\left| \begin{array}{ll}O&A\\ BO\end{array} \right|.</equation>记<equation>C=\left( \begin{array}{cc}O&A\\ B/O \end{array} \right), C</equation>为4阶矩阵，A位于它的第1，2行和第3，4列，可按照以下步骤把C变为<equation>\left( \begin{array}{cc}A&O\\ O&B \end{array} \right).</equation>把C的第3列与第1列对换，第4列与第2列对换.

因此，<equation>\left| \begin{array}{c c} O & A \\ B & O \end{array} \right| = (- 1) ^ {2} \left| \begin{array}{c c} A & O \\ O & B \end{array} \right| = | A | \cdot | B | = 6.</equation><equation>\left( \begin{array}{cc}O&A\\ BO\end{array} \right)</equation>可逆.

由可逆矩阵与其伴随矩阵的关系可知，<equation>\left( \begin{array}{c c} O & A \\ B & O \end{array} \right) ^ {*} = \left| \begin{array}{c c} O & A \\ B & O \end{array} \right| \left( \begin{array}{c c} O & A \\ B & O \end{array} \right) ^ {- 1} = 6 \left( \begin{array}{c c} O & A \\ B & O \end{array} \right) ^ {- 1}.</equation>不妨设<equation>\left( \begin{array}{cc}O&A\\ B/O \end{array} \right)^{-1} = \left( \begin{array}{cc}X_1 & X_2\\ X_3 & X_4 \end{array} \right)</equation>，则<equation>\left( \begin{array}{c c} O & A \\ B & O \end{array} \right) \left( \begin{array}{c c} X _ {1} & X _ {2} \\ X _ {3} & X _ {4} \end{array} \right) = \left( \begin{array}{c c} A X _ {3} & A X _ {4} \\ B X _ {1} & B X _ {2} \end{array} \right) = \left( \begin{array}{c c} E & O \\ O & E \end{array} \right).</equation>由于 A,B均为可逆矩阵，故由<equation>A X_{4}=O</equation><equation>B X_{1}=O</equation>可知，<equation>X_{1}=X_{4}=O</equation>；由<equation>A X_{3}=E</equation><equation>B X_{2}=E</equation>得，<equation>X_{3}=A^{-1}</equation><equation>X_{2}=B^{-1}</equation>因此，<equation>\left( \begin{array}{c c} \boldsymbol {O} & \boldsymbol {A} \\ \boldsymbol {B} & \boldsymbol {O} \end{array} \right) ^ {- 1} = \left( \begin{array}{c c} \boldsymbol {O} & \boldsymbol {B} ^ {- 1} \\ \boldsymbol {A} ^ {- 1} & \boldsymbol {O} \end{array} \right).</equation><equation>\left( \begin{array}{c c} O & A \\ B & O \end{array} \right) ^ {*} = 6 \left( \begin{array}{c c} O & B ^ {- 1} \\ A ^ {- 1} & O \end{array} \right) = 6 \left( \begin{array}{c c} O & \frac {B ^ {*}}{| B |} \\ \frac {A ^ {*}}{| A |} & O \end{array} \right) = \left( \begin{array}{c c} O & 2 B ^ {*} \\ 3 A ^ {*} & O \end{array} \right).</equation>应选B.

（法二）不妨设<equation>\left( \begin{array}{cc}O&A\\ B/O \end{array} \right)^{*} = \left( \begin{array}{cc}X_{1} & X_{2}\\ X_{3} & X_{4} \end{array} \right)</equation>由法一知，<equation>\left| \begin{array}{cc}O&A\\ BO\end{array}\right|=6</equation>故<equation>\left( \begin{array}{c c} O & A \\ B & O \end{array} \right) \left( \begin{array}{c c} X _ {1} & X _ {2} \\ X _ {3} & X _ {4} \end{array} \right) = \left( \begin{array}{c c} A X _ {3} & A X _ {4} \\ B X _ {1} & B X _ {2} \end{array} \right) = \left( \begin{array}{c c} 6 E & O \\ O & 6 E \end{array} \right).</equation>从而，<equation>A X _ {3} = 6 E, \quad B X _ {2} = 6 E, \quad A X _ {4} = B X _ {1} = O.</equation>由此可推出，<equation>X_{3}=6 A^{-1}=6 \cdot \frac{A^{*}}{\mid A\mid}=3 A^{*}, X_{2}=6 B^{-1}=6 \cdot \frac{B^{*}}{\mid B\mid}=2 B^{*}, X_{1}=X_{4}=O.</equation>因此，<equation>\left( \begin{array}{cc} O & A \\ B & O \end{array} \right)^{*} = \left( \begin{array}{cc} O & 2 B^{*} \\ 3 A^{*} & O \end{array} \right).</equation>应选B.

（法三）特殊值法.

取<equation>A=\sqrt{2} E, B=\sqrt{3} E</equation>满足<equation>| A |=2, | B |=3</equation>，则<equation>A^{*} = | A | A^{-1} = \sqrt{2} E, B^{*} = | B | B^{-1} = \sqrt{3} E.</equation>因此，<equation>\begin{aligned} \left( \begin{array}{c c} O & A \\ B & O  \right) ^ {*} &= \left( \begin{array}{c c} O & \sqrt {2} E \\ \sqrt {3} E & O  \right) ^ {*} &= \left| \begin{array}{c c} O & \sqrt {2} E \\ \sqrt {3} E & O  \right| \left( \begin{array}{c c} O & \sqrt {2} E \\ \sqrt {3} E & O  \right) ^ {- 1} &= 6 \left( \begin{array}{c c} O & \frac {1}{\sqrt {3}} E \\ \frac {1}{\sqrt {2}} E & O  \right) \\ &= \left( \begin{array}{c c} O & 2 \sqrt {3} E \\ 3 \sqrt {2} E & O  \right) &= \left( \begin{array}{c c} O & 2 B ^ {*} \\ 3 A ^ {*} & O  \right). \end{aligned}</equation>应选B.

---


### 线性方程组

### 向量

#### 向量组的线性相关性


**2024年第16题 | 填空题 | 5分**
16. 设向量<equation>\alpha_{1}=\left( \begin{array}{c} a \\ 1 \\ -1 \\ 1 \end{array} \right),\alpha_{2}=\left( \begin{array}{c} 1 \\ 1 \\ b \\ a \end{array} \right),\alpha_{3}=\left( \begin{array}{c} 1 \\ a \\ -1 \\ 1 \end{array} \right)</equation>若<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性相关，且其中任意两个向量均线性无关，则

ab = ___
**答案: **```latex
-4
```

**解析:**解（法一）由于<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性相关，故该向量组的秩小于3，从而<equation>r(\alpha_{1},\alpha_{2},\alpha_{3})\leqslant 2.</equation>又因为该向量组中任意两个向量均线性无关，所以该向量组的秩不小于2，从而<equation>r(\alpha_{1},\alpha_{2},\alpha_{3})\geqslant 2.</equation>于是，<equation>r(\alpha_{1},\alpha_{2},\alpha_{3})=2.</equation>由<equation>r(\alpha_{1},\alpha_{2},\alpha_{3}) = 2</equation>可得，矩阵<equation>(\alpha_{1},\alpha_{2},\alpha_{3})</equation>的任意一个3阶子式均为0.于是，<equation>\begin{aligned} \left| \begin{array}{l l l} a & 1 & 1 \\ 1 & 1 & a \\ 1 & a & 1  \right| \xlongequal {c _ {1} + c _ {2} + c _ {3}} \left| \begin{array}{l l l} a + 2 & 1 & 1 \\ a + 2 & 1 & a \\ a + 2 & a & 1  \right| &= (a + 2) \left| \begin{array}{l l l} 1 & 1 & 1 \\ 1 & 1 & a \\ 1 & a & 1  \right| &= (a + 2) \left| \begin{array}{l l l} 1 & 0 & 0 \\ 1 & 0 & a - 1 \\ 1 & a - 1 & 0  \right| \\ &= - (a + 2) (a - 1) ^ {2} = 0. \end{aligned}</equation>由此可得 a=-2或a=1. 但是当 a=1时，<equation>\alpha_{1}=\alpha_{3}</equation>，从而<equation>\alpha_{1},\alpha_{3}</equation>线性相关，不符合题意.于是，a=-2.

代入<equation>a = -2</equation>，再由矩阵<equation>(\alpha_{1},\alpha_{2},\alpha_{3})</equation>的任意一个3阶子式均为0可得<equation>\left| \begin{array}{c c c} 1 & 1 & - 2 \\ - 1 & b & - 1 \\ 1 & - 2 & 1 \end{array} \right| \frac {c _ {2} - c _ {1}}{c _ {3} + 2 c _ {1}} \left| \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & b + 1 & - 3 \\ 1 & - 3 & 3 \end{array} \right| = 3 (b + 1) - 9 = 0.</equation>解得 b=2.

因此，<equation>a=-2,b=2,ab=-4.</equation>（法二）同法一可得<equation>r(\alpha_{1},\alpha_{2},\alpha_{3}) = 2.</equation>对矩阵<equation>(\alpha_{1},\alpha_{2},\alpha_{3})</equation>作初等行变换.<equation>\begin{array}{l} \left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) = \left( \begin{array}{c c c} a & 1 & 1 \\ 1 & 1 & a \\ - 1 & b & - 1 \\ 1 & a & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & a \\ 1 & a & 1 \\ - 1 & b & - 1 \\ a & 1 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & a \\ 0 & a - 1 & 1 - a \\ 0 & b + 1 & a - 1 \\ 0 & 1 - a & 1 - a ^ {2} \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c} 1 & 1 & a \\ 0 & a - 1 & 1 - a \\ 0 & b + 1 & a - 1 \\ 0 & 0 & 2 - a - a ^ {2} \end{array} \right). \\ \end{array}</equation>当<equation>a = -2</equation>或<equation>a = 1</equation>时，<equation>2 - a - a^{2} = -(a + 2)(a - 1) = 0.</equation>当 a =1时，<equation>\left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) \rightarrow \left(\begin{array}{c c c}1&1&1\\0&0&0\\0&b + 1&0\\0&0&0\end{array}\right)\rightarrow \left(\begin{array}{c c c}1&1&1\\0&b + 1&0\\0&0&0\\0&0&0\end{array}\right).</equation>由此可得<equation>\alpha_{1},\alpha_{3}</equation>线性相关，不符合题意.

当 a = -2时，<equation>\left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right)\rightarrow \left(\begin{array}{c c c}1&1&- 2\\0&- 3&3\\0&b + 1&- 3\\0&0&0\end{array}\right)\rightarrow \left(\begin{array}{c c c}1&1&- 2\\0&1&- 1\\0&b - 2&0\\0&0&0\end{array}\right).</equation>由<equation>r(\alpha_{1},\alpha_{2},\alpha_{3}) = 2</equation>可得<equation>b - 2 = 0</equation>，即<equation>b = 2</equation>因此，<equation>a=-2,b=2,ab=-4.</equation>

---

**2014年第8题 | 选择题 | 4分 | 答案: A**

8. 设<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>均为3维向量，则对任意常数 k,l，向量组<equation>\alpha_{1}+k\alpha_{3},\alpha_{2}+l\alpha_{3}</equation>线性无关是向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关的（    )

A. 必要非充分条件 B. 充分非必要条件

C. 充分必要条件 D. 既非充分也非必要条件

答案: A

**解析:**假设<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性无关.考虑向量组<equation>\boldsymbol{\alpha}_{1}+k\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{2}+l\boldsymbol{\alpha}_{3}.</equation>由于<equation>a\left(\boldsymbol{\alpha}_{1} + k\boldsymbol{\alpha}_{3}\right) + b\left(\boldsymbol{\alpha}_{2} + l\boldsymbol{\alpha}_{3}\right) = a\boldsymbol{\alpha}_{1} + b\boldsymbol{\alpha}_{2} + (ak + bl)\boldsymbol{\alpha}_{3} = 0</equation>，故由<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性无关可知，<equation>a=b=ak+bl=0.</equation>因此，<equation>\boldsymbol{\alpha}_{1} + k\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{2} + l\boldsymbol{\alpha}_{3}</equation>线性无关.向量组<equation>\boldsymbol{\alpha}_{1} + k\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{2} + l\boldsymbol{\alpha}_{3}</equation>线性无关是向量组<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性无关的必要条件.

但是向量组<equation>\boldsymbol{\alpha}_{1}+k\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{2}+l\boldsymbol{\alpha}_{3}</equation>线性无关不是向量组<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性无关的充分条件.

下面我们给出反例.令<equation>\alpha_{1},\alpha_{2}</equation>线性无关，而<equation>\alpha_{3}=0</equation>，则此时<equation>\alpha_{1}+k\alpha_{3}=\alpha_{1},\alpha_{2}+l\alpha_{3}=\alpha_{2}</equation>线性无关.对任意非零常数k，有<equation>0\alpha_{1}+0\alpha_{2}+k\alpha_{3}=0</equation>，从而<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性相关.

因此，<equation>\alpha_{1} + k\alpha_{3},\alpha_{2} + l\alpha_{3}</equation>线性无关是向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关的必要非充分条件.应选A.

---

**2012年第7题 | 选择题 | 4分 | 答案: C**

7. 设<equation>\alpha_{1}=\left( \begin{array}{c}0\\ 0\\ c_{1}\end{array} \right),\alpha_{2}=\left( \begin{array}{c}0\\ 1\\ c_{2}\end{array} \right),\alpha_{3}=\left( \begin{array}{c}1\\ -1\\ c_{3}\end{array} \right),\alpha_{4}=\left( \begin{array}{c}-1\\ 1\\ c_{4}\end{array} \right),</equation>其中<equation>c_{1},c_{2},c_{3},c_{4}</equation>为任意常数，则下列向量组线性相关

为（    ）

A.<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>B.<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>C.<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>D.<equation>\alpha_{2},\alpha_{3},\alpha_{4}</equation>

答案: C

**解析:**解（法一）由题设可得，<equation>\alpha_{3} + \alpha_{4} = \left( \begin{array}{c} 0 \\ 0 \\ c_{3} + c_{4} \end{array} \right),\alpha_{1} = \left( \begin{array}{c} 0 \\ 0 \\ c_{1} \end{array} \right).</equation>当<equation>c_{3} + c_{4}\neq 0</equation>时，<equation>\boldsymbol{\alpha}_{1} = \frac{c_{1}}{c_{3} + c_{4}} \left( \boldsymbol{\alpha}_{3} + \boldsymbol{\alpha}_{4} \right), \boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{3}, \boldsymbol{\alpha}_{4}</equation>线性相关；当<equation>c_{3} + c_{4} = 0</equation>时，<equation>\boldsymbol{\alpha}_{3} + \boldsymbol{\alpha}_{4} = 0</equation><equation>\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}</equation>线性相关.从而<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}</equation>线性相关.

综上所述，<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>线性相关，应选C.

（法二）由于<equation>n</equation>个<equation>n</equation>维列向量<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{n}</equation>线性相关等价于<equation>|\alpha_{1},\alpha_{2},\dots ,\alpha_{n}| = 0</equation>，而<equation>\left| \alpha_ {1}, \alpha_ {3}, \alpha_ {4} \right| = \left| \begin{array}{c c c} 0 & 1 & - 1 \\ 0 & - 1 & 1 \\ c _ {1} & c _ {3} & c _ {4} \end{array} \right| = c _ {1} \left| \begin{array}{c c} 1 & - 1 \\ - 1 & 1 \end{array} \right| = 0,</equation>故<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>线性相关.应选C.

同理可计算其他选项中的3个向量组成的矩阵的行列式，可知它们均不恒为零

---


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

### 行列式

# 数学三

## 高等数学

### 函数、极限、连续

#### 无穷小量


**2025年第1题 | 选择题 | 5分 | 答案: C**
1. 在<equation>x \rightarrow 0^{+}</equation>时，下列无穷小量中与 x等价的是（    )

A.<equation>\mathrm{e}^{-\sin x}-1</equation>B.<equation>\sqrt{x+1}-\cos x</equation>C.<equation>1-\cos \sqrt{2 x}</equation>D.<equation>1-\frac{\ln(1+x)}{x}</equation>
答案: C
**解析: **解分别记四个选项中的函数为<equation>f_{i}(x)(i = 1,2,3,4)</equation>，计算<equation>\lim_{x\to 0^{+}}\frac{f_{i}(x)}{x}</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {f _ {1} (x)}{x} = \lim _ {x \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {- \sin x} - 1}{x} \xlongequal {\mathrm {e} ^ {- \sin x} - 1 \sim - \sin x} \lim _ {x \rightarrow 0 ^ {+}} \frac {- \sin x}{x} = - 1.</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {f _ {2} (x)}{x} = \lim _ {x \rightarrow 0 ^ {+}} \frac {\sqrt {x + 1} - \cos x}{x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0 ^ {+}} \left(\frac {1}{2 \sqrt {x + 1}} + \sin x\right) = \frac {1}{2}.</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {f _ {3} (x)}{x} = \lim _ {x \rightarrow 0 ^ {+}} \frac {1 - \cos \sqrt {2 x}}{x} \xlongequal {\frac {1 - \cos \sqrt {2 x} \sim \frac {1}{2} (\sqrt {2 x}) ^ {2}}{x}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {1}{2} (\sqrt {2 x}) ^ {2}}{x} = 1.</equation><equation>\begin{aligned} \lim _ {x \rightarrow 0 ^ {+}} \frac {f _ {4} (x)}{x} &= \lim _ {x \rightarrow 0 ^ {+}} \frac {1 - \frac {\ln (1 + x)}{x}}{x} = \lim _ {x \rightarrow 0 ^ {+}} \frac {x - \ln (1 + x)}{x ^ {2}} \\ \frac {\ln (1 + x) = x - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right)}{\hline} \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {1}{2} x ^ {2} + o \left(x ^ {2}\right)}{x ^ {2}} &= \frac {1}{2}. \end{aligned}</equation>由此可得，仅有选项C的函数<equation>f_{3}(x)</equation>满足<equation>\lim_{x\rightarrow 0^{+}}\frac{f_{3}(x)}{x}=1</equation>，其余选项的函数均不符合要求因此，应选C.

---

**2024年第11题 | 填空题 | 5分**
11. 当<equation>x\to 0</equation>时，<equation>\frac {\left(1 + t ^ {2}\right) \sin t ^ {2}}{1 + \cos^ {2} t}</equation><equation>\mathrm{d}t</equation>与<equation>x^{k}</equation>是同阶无穷小，则<equation>k =</equation>___
**答案: **```latex
3
```

**解析:**解记<equation>f ( x )=\int_{0}^{x}\frac{(1+t^{2})\sin t^{2}}{1+\cos^{2}t}\mathrm{d} t</equation>，则<equation>f ( 0 )=0</equation>，且由变限积分的求导公式可得<equation>f^{\prime}(x)=</equation><equation>\frac{(1+x^{2})\sin x^{2}}{1+\cos^{2}x}.</equation>由于<equation>\lim _ {x \rightarrow 0} \frac {f ^ {\prime} (x)}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\left(1 + x ^ {2}\right) \sin x ^ {2}}{\left(1 + \cos^ {2} x\right) x ^ {2}} = \frac {1}{2} \lim _ {x \rightarrow 0} \frac {\sin x ^ {2}}{x ^ {2}} = \frac {1}{2},</equation>故当<equation>x\to0</equation>时，<equation>f^{\prime}(x)</equation>与<equation>x^{2}</equation>是同阶无穷小，且<equation>f^{\prime}(x)\sim \frac{1}{2} x^{2}.</equation>于是，<equation>f (x) = f (x) - f (0) = \int_ {0} ^ {x} f ^ {\prime} (t) \mathrm {d} t \sim \int_ {0} ^ {x} \frac {t ^ {2}}{2} \mathrm {d} t = \frac {t ^ {3}}{6} \Big | _ {0} ^ {x} = \frac {x ^ {3}}{6}. \quad (x \rightarrow 0)</equation>因此，当<equation>x\to 0</equation>时，<equation>f(x)</equation>与<equation>x^{3}</equation>同阶，<equation>k = 3.</equation>

---

**2022年第1题 | 选择题 | 5分 | 答案: C**

1. 若当<equation>x \rightarrow 0</equation>时，<equation>\alpha (x),\beta (x)</equation>是非零无穷小量，则以下四个命题：<equation>\textcircled{1}</equation>若<equation>\alpha (x)\sim \beta (x)</equation>，则<equation>\alpha^{2}(x)\sim \beta^{2}(x);</equation><equation>\textcircled{2}</equation>若<equation>\alpha^{2}(x)\sim \beta^{2}(x)</equation>，则<equation>\alpha (x)\sim \beta (x);</equation><equation>\textcircled{3}</equation>若<equation>\alpha (x)\sim \beta (x)</equation>，则<equation>\alpha (x)-\beta (x)=o(\alpha (x));</equation><equation>\textcircled{4}</equation>若<equation>\alpha (x)-\beta (x)=o(\alpha (x))</equation>，则<equation>\alpha (x)\sim \beta (x).</equation>其中所有真命题的序号是（    ）

A.<equation>\textcircled{1}\textcircled{3}</equation>B.<equation>\textcircled{1}\textcircled{4}</equation>C.<equation>\textcircled{1}\textcircled{3}\textcircled{4}</equation>D.<equation>\textcircled{2}\textcircled{3}\textcircled{4}</equation>

答案: C

**解析:**## 依次分析四个命题.

若<equation>\alpha(x)\sim\beta(x)</equation>，则<equation>\lim_{x\to0}\frac{\alpha(x)}{\beta(x)}=1</equation>，从而<equation>\lim_{x\to0}\frac{\alpha^{2}(x)}{\beta^{2}(x)}=1</equation>，即<equation>\alpha^{2}(x)\sim\beta^{2}(x).</equation>命题<equation>\textcircled{1}</equation>是真命题.

由<equation>\alpha^{2}(x)\sim\beta^{2}(x)</equation>并不能得到<equation>\alpha(x)\sim\beta(x).</equation>考虑<equation>\beta(x)=-\alpha(x)</equation>，则<equation>\lim_{x\to0}\frac{\alpha^{2}(x)}{\beta^{2}(x)}=\lim_{x\to0}\frac{\alpha^{2}(x)}{\alpha^{2}(x)}= 1</equation>，即<equation>\alpha^{2}(x)\sim\beta^{2}(x)</equation>，但<equation>\lim_{x\to0}\frac{\alpha(x)}{\beta(x)}=\lim_{x\to0}\frac{\alpha(x)}{- \alpha(x)}=-1, \alpha(x)</equation>与<equation>\beta(x)</equation>只是同阶但并不等价的无穷小量.

命题<equation>\textcircled{2}</equation>不是真命题.

要说明<equation>\alpha ( x )-\beta ( x )=o( \dot{\alpha} ( x ) )</equation>，只需说明<equation>\lim_{x\to 0}\frac{\alpha ( x )-\beta ( x )}{\alpha ( x )}=0.</equation><equation>\lim _ {x \rightarrow 0} \frac {\alpha (x) - \beta (x)}{\alpha (x)} = 1 - \lim _ {x \rightarrow 0} \frac {\beta (x)}{\alpha (x)} \frac {\alpha (x) \sim \beta (x)}{1 - 1} = 0.</equation>命题<equation>\textcircled{3}</equation>是真命题.

要说明<equation>\alpha (x)\sim \beta (x)</equation>，只需说明<equation>\lim_{x\to 0}\frac{\beta (x)}{\alpha (x)} = 1.</equation><equation>\lim _ {x \rightarrow 0} \frac {\beta (x)}{\alpha (x)} = \lim _ {x \rightarrow 0} \frac {\alpha (x) - [ \alpha (x) - \beta (x) ]}{\alpha (x)} = 1 - \lim _ {x \rightarrow 0} \frac {\alpha (x) - \beta (x)}{\alpha (x)} = 1 - 0 = 1.</equation>命题<equation>\textcircled{4}</equation>是真命题.

综上所述，应选C.

---

**2021年第1题 | 选择题 | 5分 | 答案: C**

1. 当<equation>x \rightarrow 0</equation>时，<equation>\int_{0}^{x^{2}}(\mathrm{e}^{t^{3}}-1)\mathrm{d}t</equation>是<equation>x^{7}</equation>的（    ）

A. 低阶无穷小 B. 等价无穷小

C. 高阶无穷小 D. 同阶但非等价无穷小

答案: C

**解析:**解 计算<equation>\lim_{x\rightarrow 0}\frac{\int_{0}^{x^{2}}(\mathrm{e}^{t^{3}}-1)\mathrm{d}t}{x^{7}}</equation>来比较这两个无穷小量的阶.<equation>\lim _ {x \rightarrow 0} \frac {\int_ {0} ^ {x ^ {2}} \left(\mathrm {e} ^ {t ^ {3}} - 1\right) \mathrm {d} t}{x ^ {7}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\left(\mathrm {e} ^ {x ^ {6}} - 1\right) \cdot 2 x}{7 x ^ {6}} \xlongequal {\text {e} ^ {x ^ {6}} - 1 \sim x ^ {6}} \lim _ {x \rightarrow 0} \frac {x ^ {6} \cdot 2 x}{7 x ^ {6}} = 0.</equation>因此，<equation>\int_{0}^{x^{2}}(\mathrm{e}^{t^{3}}-1)\mathrm{d}t</equation>是<equation>x^{7}</equation>的高阶无穷小.应选C.

---

**2013年第1题 | 选择题 | 4分 | 答案: D**

1. 当<equation>x \to0</equation>时，用“<equation>o(x)</equation>”表示比 x高阶的无穷小量，则下列式子中错误的是（    )

A.<equation>x \cdot o \left( x^{2} \right)=o \left( x^{3} \right)</equation>B.<equation>o(x)\cdot o \left( x^{2} \right)=o \left( x^{3} \right)</equation>C.<equation>o \left( x^{2} \right)+o \left( x^{2} \right)=o \left( x^{2} \right)</equation>D.<equation>o(x)+o \left( x^{2} \right)=o \left( x^{2} \right)</equation>

答案: D

**解析:**由于<equation>\lim _ {x \rightarrow 0} \frac {x \cdot o \left(x ^ {2}\right)}{x ^ {3}} = \lim _ {x \rightarrow 0} \frac {o \left(x ^ {2}\right)}{x ^ {2}} = 0,</equation><equation>\lim _ {x \rightarrow 0} \frac {o (x) \cdot o \left(x ^ {2}\right)}{x ^ {3}} = \lim _ {x \rightarrow 0} \frac {o (x)}{x} \cdot \lim _ {x \rightarrow 0} \frac {o \left(x ^ {2}\right)}{x ^ {2}} = 0,</equation><equation>\lim _ {x \rightarrow 0} \frac {o \left(x ^ {2}\right) + o \left(x ^ {2}\right)}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {o \left(x ^ {2}\right)}{x ^ {2}} + \lim _ {x \rightarrow 0} \frac {o \left(x ^ {2}\right)}{x ^ {2}} = 0 + 0 = 0,</equation>故选项A、B、C均正确.应选D.

对选项D，若令<equation>f ( x )=x^{2}, g ( x )=x^{3}</equation>，则当<equation>x\to 0</equation>时，<equation>x^{2}+x^{3}</equation>形如<equation>o ( x )+o \left( x^{2}\right)</equation>，但<equation>\lim_{x\to 0}\frac{x^{2}+x^{3}}{x^{2}}=1.</equation>因此，当<equation>x\to 0</equation>时，<equation>x^{2}+x^{3}</equation>不是<equation>x^{2}</equation>的高阶无穷小量.

---


#### 函数的连续性与间断点的类型


**2024年第1题 | 选择题 | 5分 | 答案: D**

1. 设函数<equation>f ( x )=\lim_{n \to \infty} \frac{1+x}{1+n x^{2 n}},</equation>则 f(x)，（    ）

A. 在 x=1,x=-1处都连续 B. 在 x=1处连续，在 x=-1处不连续

C. 在 x=1,x=-1处都不连续 D. 在 x=1处不连续，在 x=-1处连续

答案: D

**解析:**解 由于<equation>\lim_{n\to \infty}x^{2n}=\left\{\begin{array}{ll}0,&|x|<1,\\ 1,&|x|=1,\text{故当}|x|<1\text{时},\lim_{n\to \infty}\frac{1+x}{1+nx^{2n}}=\lim_{n\to \infty}\frac{1+x}{1}=1+x,\text{当} \\ +\infty,&|x|>1,\end{array} \right.</equation><equation>|x| = 1</equation>时，<equation>\lim_{n\to \infty}\frac{1 + x}{1 + nx^{2n}} = \lim_{n\to \infty}\frac{1 + x}{1 + n} = 0</equation>，当<equation>|x| > 1</equation>时，<equation>\lim_{n\to \infty}\frac{1 + x}{1 + nx^{2n}} = 0.</equation>于是，<equation>f (x) = \left\{ \begin{array}{l l} 1 + x, & | x | < 1, \\ 0, & | x | \geqslant 1. \end{array} \right.</equation>由于<equation>\lim_{x\to -1^{+}}f(x) = \lim_{x\to -1^{+}}(1 + x) = 0,\lim_{x\to -1^{-}}f(x) = 0 = f(-1),\lim_{x\to -1^{-}}f(x) = \lim_{x\to -1^{+}}(1 + x) = 2,</equation><equation>\lim_{x\to 1^{+}}f(x) = 0</equation>，故<equation>f(x)</equation>在<equation>x = -1</equation>处连续，<equation>x = 1</equation>处不连续.因此，应选D.

---

**2020年第2题 | 选择题 | 4分 | 答案: C**

2. 函数<equation>f(x)=\frac{\mathrm{e}^{\frac{1}{x-1}}\ln|1+x|}{(\mathrm{e}^{x}-1)(x-2)}</equation>的第二类间断点的个数为（    )

A.1 B.2 C.3 D.4

答案: C

**解析:**解从 f(x)的表达式可以看出，<equation>x=-1,x=0,x=1,x=2</equation>为 f(x)的间断点.下面分别计算这些点处的左、右极限.<equation>\lim _ {x \rightarrow - 1} f (x) = \lim _ {x \rightarrow - 1} \frac {\mathrm {e} ^ {\frac {1}{x - 1}} \ln | 1 + x |}{\left(\mathrm {e} ^ {x} - 1\right) (x - 2)} = \frac {\mathrm {e} ^ {- \frac {1}{2}}}{\left(\mathrm {e} ^ {- 1} - 1\right) \cdot (- 3)} \lim _ {x \rightarrow - 1} \ln | 1 + x | = \infty .</equation><equation>\lim _ {x \rightarrow 0} f (x) = \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {\frac {1}{x - 1}} \ln | 1 + x |}{\left(\mathrm {e} ^ {x} - 1\right) (x - 2)} = \frac {\mathrm {e} ^ {- 1}}{- 2} \lim _ {x \rightarrow 0} \frac {\ln | 1 + x |}{\mathrm {e} ^ {x} - 1} \frac {\ln | 1 + x | \sim x}{\mathrm {e} ^ {x} - 1 \sim x} - \frac {1}{2 \mathrm {e}} \lim _ {x \rightarrow 0} \frac {x}{x} = - \frac {1}{2 \mathrm {e}}.</equation><equation>\lim _ {x \rightarrow 1 ^ {+}} f (x) = \lim _ {x \rightarrow 1 ^ {+}} \frac {\mathrm {e} ^ {\frac {1}{x - 1}} \ln | 1 + x |}{\left(\mathrm {e} ^ {x} - 1\right) (x - 2)} = - \frac {\ln 2}{\mathrm {e} - 1} \lim _ {x \rightarrow 1 ^ {+}} \mathrm {e} ^ {\frac {1}{x - 1}} = \infty .</equation><equation>\lim _ {x \rightarrow 2} f (x) = \lim _ {x \rightarrow 2} \frac {\mathrm {e} ^ {\frac {1}{x - 1}} \ln | 1 + x |}{\left(\mathrm {e} ^ {x} - 1\right) (x - 2)} = \frac {\mathrm {e} \ln 3}{\mathrm {e} ^ {2} - 1} \lim _ {x \rightarrow 2} \frac {1}{x - 2} = \infty .</equation>因此，<equation>x=-1,x=1</equation>和 x=2均为 f(x)的无穷间断点，从而也是第二类间断点. f(x)共有3个第二类间断点.应选C.

---

**2017年第1题 | 选择题 | 4分 | 答案: A**

1. 若函数 f(x)<equation>\left\{\begin{array}{l l}{\frac{1-\cos \sqrt{x}}{ax},}&{x>0,}\\ {b,}&{x\leqslant 0}\end{array}\right.</equation>在 x=0处连续，则（   ）

A.<equation>a b=\frac{1}{2}</equation>B.<equation>a b=-\frac{1}{2}</equation>C.<equation>a b=0</equation>D.<equation>a b=2</equation>

答案: A

**解析:**解 f(x)是分段函数.代入 f(x)在<equation>(-\infty, 0]</equation>和（0，<equation>+\infty</equation>）上的表达式，分别计算<equation>\lim_{x\to 0^{-}}f(x),</equation><equation>\lim_{x\to 0^{+}}f(x).</equation><equation>\lim _ {x \rightarrow 0 ^ {-}} f (x) = f (0) = b,</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} f (x) = \lim _ {x \rightarrow 0 ^ {+}} \frac {1 - \cos \sqrt {x}}{a x} \frac {1 - \cos \sqrt {x} \sim \frac {1}{2} (\sqrt {x}) ^ {2}}{\overline {{=}}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {x}{2}}{a x} = \frac {1}{2 a}.</equation>因此，<equation>b=\frac{1}{2a}</equation>即<equation>a b=\frac{1}{2}</equation>应选A.

---

**2013年第2题 | 选择题 | 4分 | 答案: C**

2. 函数<equation>f ( x )=\frac{| x |^{x}-1}{x ( x+1 ) \ln| x |}</equation>的可去间断点的个数为（    ）

A.0 B.1 C.2 D.3

答案: C

**解析:**解 由于 f(x)在 x=-1,0,1处没有定义且在其他点处连续，故 f(x)的间断点为 x=-1,0,1. 由于<equation>\lim _ {x \rightarrow 0} | x | ^ {x} = \lim _ {x \rightarrow 0} \mathrm {e} ^ {x \ln | x |} = \mathrm {e} ^ {\lim _ {x \rightarrow 0} x \ln | x |} = \mathrm {e} ^ {\lim _ {x \rightarrow 0} \frac {\ln | x |}{x ^ {- 1}} \xlongequal {\text {洛 必达}}} \mathrm {e} ^ {\lim _ {x \rightarrow 0} (- x)} = 1,</equation><equation>\lim _ {x \rightarrow 1} | x | ^ {x} = 1, \quad \lim _ {x \rightarrow - 1} | x | ^ {x} = 1,</equation>故<equation>\lim _ {x \rightarrow 0} \frac {\left| x \right| ^ {x} - 1}{x (x + 1) \ln | x |} = \lim _ {x \rightarrow 0} \frac {\left| x \right| ^ {x} - 1}{(x + 1) \ln (1 + \left| x \right| ^ {x} - 1)} = \lim _ {x \rightarrow 0} \frac {\left| x \right| ^ {x} - 1}{(x + 1) \left(\left| x \right| ^ {x} - 1\right)} = \lim _ {x \rightarrow 0} \frac {1}{x + 1} = 1,</equation><equation>\lim _ {x \rightarrow 1} \frac {\left| x \right| ^ {x} - 1}{x (x + 1) \ln | x |} \stackrel {\text {同 上}} {=} \lim _ {x \rightarrow 1} \frac {1}{x + 1} = \frac {1}{2},</equation><equation>\lim _ {x \rightarrow - 1} \frac {\left| x \right| ^ {x} - 1}{x (x + 1) \ln | x |} \stackrel {\text {同 上}} {=} \lim _ {x \rightarrow - 1} \frac {1}{x + 1} = \infty .</equation>因此，<equation>f ( x )</equation>的可去间断点为<equation>x=0,1. f ( x )</equation>共有2个可去间断点.应选C.

---

**2009年第1题 | 选择题 | 4分 | 答案: C**

1. 函数<equation>f(x)=\frac{x-x^{3}}{\sin \pi x}</equation>的可去间断点的个数为（    ）

A.1 B.2 C.3 D.无穷多个

答案: C

**解析:**解 因为当 k为整数时，<equation>\sin k\pi=0</equation>，所以 f(x）在 x=k（k为整数）时无定义，在其余点连续.当<equation>k-k^{3}\neq0</equation>时，即 k≠0，<equation>\pm1</equation>时，<equation>\lim _ {x \rightarrow k} \frac {x - x ^ {3}}{\sin \pi x} = \infty .</equation>x=k为f（x）的无穷间断点.

当<equation>k - k^{3} = 0</equation>时，即<equation>k = 0, \pm 1</equation>时，<equation>\lim_{x\to k}f(x)</equation>为<equation>\frac{0}{0}</equation>型未定式极限，可用洛必达法则求极限.<equation>\lim _ {x \rightarrow 0} \frac {x - x ^ {3}}{\sin \pi x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - 3 x ^ {2}}{\pi \cos \pi x} = \frac {1}{\pi},</equation><equation>\lim _ {x \rightarrow 1} \frac {x - x ^ {3}}{\sin \pi x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 1} \frac {1 - 3 x ^ {2}}{\pi \cos \pi x} = \frac {- 2}{- \pi} = \frac {2}{\pi},</equation><equation>\lim _ {x \rightarrow - 1} \frac {x - x ^ {3}}{\sin \pi x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow - 1} \frac {1 - 3 x ^ {2}}{\pi \cos \pi x} = \frac {- 2}{- \pi} = \frac {2}{\pi}.</equation>因此，<equation>f ( x )</equation>共有3个可去间断点，<equation>x=0</equation>，<equation>\pm 1.</equation>应选C.

---


#### 函数极限的计算


**2023年第11题 | 填空题 | 5分**

<equation>\lim _ {x \rightarrow \infty} x ^ {2} \left(2 - x \sin \frac {1}{x} - \cos \frac {1}{x}\right) = \underline {{}}</equation>

**答案:**# 2 3.

**解析:**考虑<equation>\sin x, \cos x</equation>在 x=0处的泰勒公式.当 x<equation>\to\infty</equation>时，<equation>\frac{1}{x}\to0,</equation><equation>\sin \frac {1}{x} = \frac {1}{x} - \frac {1}{6 x ^ {3}} + o \left(\frac {1}{x ^ {3}}\right),</equation><equation>\cos \frac {1}{x} = 1 - \frac {1}{2 x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right).</equation>于是，<equation>\begin{array}{l} x ^ {2} \left(2 - x \sin \frac {1}{x} - \cos \frac {1}{x}\right) = x ^ {2} \left[ 2 - 1 + \frac {1}{6 x ^ {2}} - 1 + \frac {1}{2 x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right) \right] \\ = x ^ {2} \left[ \frac {2}{3 x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right) \right] = \frac {2}{3} + o (1). \\ \end{array}</equation>因此，<equation>\lim _ {x \rightarrow \infty} x ^ {2} \left(2 - x \sin \frac {1}{x} - \cos \frac {1}{x}\right) = \frac {2}{3}.</equation>

---

**2022年第11题 | 填空题 | 5分**

<equation>1. \lim _ {x \rightarrow 0} \left(\frac {1 + \mathrm {e} ^ {x}}{2}\right) ^ {\cot x} = \underline {{}}</equation>

**解析:**取对数再求极限.<equation>\lim _ {x \rightarrow 0} \left(\frac {1 + \mathrm {e} ^ {x}}{2}\right) ^ {\cot x} = \lim _ {x \rightarrow 0} \mathrm {e} ^ {\cot x \ln \frac {1 + \mathrm {e} ^ {x}}{2}} = \mathrm {e} _ {x \rightarrow 0} ^ {\lim _ {x \rightarrow 0} \cot x \ln \frac {1 + \mathrm {e} ^ {x}}{2}}.</equation>下面计算<equation>\lim_{x\to 0}\cot x\ln \frac{1 + \mathrm{e}^{x}}{2}</equation>.<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \cot x \ln \frac {1 + e ^ {x}}{2} = \lim _ {x \rightarrow 0} \frac {\ln \frac {1 + e ^ {x}}{2}}{\tan x} \xlongequal {\tan x \sim x} \lim _ {x \rightarrow 0} \frac {\ln \left(1 + \frac {e ^ {x} - 1}{2}\right)}{x} \\ \frac {\ln \left(1 + \frac {e ^ {x} - 1}{2}\right) \sim \frac {e ^ {x} - 1}{2}}{\lim _ {x \rightarrow 0} \frac {e ^ {x} - 1}{2 x}} \lim _ {x \rightarrow 0} \frac {x}{2 x} \\ = \frac {1}{2}. \\ \end{array}</equation>因此，原极限<equation>= \mathrm{e}^{\frac{1}{2}} = \sqrt{\mathrm{e}}.</equation>

---

**2020年第1题 | 选择题 | 4分 | 答案: B**

1. 设<equation>\lim_{x\rightarrow a}\frac{f(x)-a}{x-a}=b</equation>，则<equation>\lim_{x\rightarrow a}\frac{\sin f(x)-\sin a}{x-a}=</equation>(    )

A.<equation>b\sin a</equation>B.<equation>b\cos a</equation>C.<equation>b\sin f(a)</equation>D.<equation>b\cos f(a)</equation>

答案: B

**解析:**解 由<equation>\lim_{x\to a}\frac{f(x)-a}{x-a}=b</equation>可得，<equation>\lim_{x\to a}[f(x)-a]=0</equation>，即<equation>\lim_{x\to a}f(x)=a.</equation>对<equation>[ f ( x ) , a ]</equation>或<equation>[ a,f ( x ) ]</equation>上的<equation>\sin z</equation>应用拉格朗日中值定理可得，<equation>\sin f (x) - \sin a = \cos \xi_ {x} [ f (x) - a ],</equation>其中<equation>\xi_{x}</equation>介于<equation>f(x)</equation>与<equation>a</equation>之间. 由于<equation>\lim_{x\to a}f(x) = a</equation>，故<equation>\lim_{x\to a}\xi_x = a.</equation><equation>\lim _ {x \rightarrow a} \frac {\sin f (x) - \sin a}{x - a} = \lim _ {x \rightarrow a} \frac {\cos \xi_ {x} [ f (x) - a ]}{x - a} = \lim _ {x \rightarrow a} \cos \xi_ {x} \cdot \lim _ {x \rightarrow a} \frac {f (x) - a}{x - a} = b \cos a.</equation>因此，应选B.

---

**2017年第15题 | 解答题 | 10分**

15. (本题满分10分)

**答案:**# 2 3.

**解析:**解（法一）令<equation>u=x-t</equation>，则<equation>t=x-u,\mathrm{d}u=-\mathrm{d}t,</equation><equation>\int_ {0} ^ {x} \sqrt {x - t} \mathrm {e} ^ {t} \mathrm {d} t = - \int_ {x} ^ {0} \sqrt {u} \mathrm {e} ^ {x - u} \mathrm {d} u = \mathrm {e} ^ {x} \int_ {0} ^ {x} \sqrt {u} \mathrm {e} ^ {- u} \mathrm {d} u.</equation>于是，<equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {x} \int_ {0} ^ {x} \sqrt {u} \mathrm {e} ^ {- u} \mathrm {d} u}{\sqrt {x ^ {3}}} \xlongequal {\lim _ {x \rightarrow 0 ^ {+}} \mathrm {e} ^ {x} = 1} \lim _ {x \rightarrow 0 ^ {+}} \frac {\int_ {0} ^ {x} \sqrt {u} \mathrm {e} ^ {- u} \mathrm {d} u}{\sqrt {x ^ {3}}} \xlongequal {\text {洛 必 达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sqrt {x} \mathrm {e} ^ {- x}}{\frac {3}{2} \sqrt {x}} = \frac {2}{3}.</equation>因此，原极限<equation>= \frac{2}{3}.</equation>（法二）由于<equation>\mathrm{e}^{t}</equation>和<equation>\sqrt{x-t}</equation>均为关于 t的连续函数，且<equation>\sqrt{x-t}</equation>在[0,x]上不变号，故由积分中值定理可得，存在<equation>\xi_{x}\in[0,x]</equation>，使得<equation>\int_ {0} ^ {x} \sqrt {x - t} \mathrm {e} ^ {t} \mathrm {d} t = \mathrm {e} ^ {\xi_ {x}} \int_ {0} ^ {x} \sqrt {x - t} \mathrm {d} t.</equation>因此，<equation>\begin{aligned} \lim _ {x \rightarrow 0 ^ {+}} \frac {\int_ {0} ^ {x} \sqrt {x - t} \mathrm {e} ^ {t} \mathrm {d} t}{\sqrt {x ^ {3}}} &= \lim _ {x \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {\xi_ {x}} \int_ {0} ^ {x} \sqrt {x - t} \mathrm {d} t}{\sqrt {x ^ {3}}} = \lim _ {\substack {x \rightarrow 0 ^ {+} \\ 0 \leqslant \xi_ {x} \leqslant x}} \mathrm {e} ^ {\xi_ {x}} \cdot \lim _ {x \rightarrow 0 ^ {+}} \frac {- \frac {2}{3} (x - t) ^ {\frac {3}{2}} \Big| _ {0} ^ {x}}{\sqrt {x ^ {3}}} \\ &= 1 \cdot \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {2}{3} x ^ {\frac {3}{2}}}{\sqrt {x ^ {3}}} = \frac {2}{3}. \end{aligned}</equation>

---

**2016年第9题 | 填空题 | 4分**

9. 已知函数 f(x)满足<equation>\lim_{x\rightarrow 0}\frac{\sqrt{1+f(x)\sin 2x}-1}{\mathrm{e}^{3x}-1}=2</equation>，则<equation>\lim_{x\rightarrow 0}f(x)=</equation>___.

**解析:**解（法一）由极限的四则运算法则知，<equation>\lim _ {x \rightarrow 0} (\sqrt {1 + f (x) \sin 2 x} - 1) = \lim _ {x \rightarrow 0} \frac {\sqrt {1 + f (x) \sin 2 x} - 1}{\mathrm {e} ^ {3 x} - 1} \cdot \lim _ {x \rightarrow 0} \left(\mathrm {e} ^ {3 x} - 1\right)=2 \times 0=0.</equation>从而<equation>\lim_{x\to 0}\sqrt{1+f(x)\sin 2x}=1</equation>，故<equation>\lim_{x\to 0}f(x)\sin 2x=\lim_{x\to 0}[\left(\sqrt{1+f(x)\sin 2x}\right)^{2}-1]=0.</equation>，当 x→0时，<equation>\sqrt{1+f(x)\sin 2x}-1\sim \frac{1}{2} f(x)\sin 2x.</equation>因此，<equation>\begin{array}{l} 2 = \lim _ {x \rightarrow 0} \frac {\sqrt {1 + f (x) \sin 2 x} - 1}{\mathrm {e} ^ {3 x} - 1} \xlongequal {\mathrm {e} ^ {3 x} - 1 \sim 3 x} \lim _ {x \rightarrow 0} \frac {\frac {1}{2} f (x) \sin 2 x}{3 x} \\ = \frac {1}{3} \lim _ {x \rightarrow 0} \frac {f (x) \sin 2 x}{2 x} \xlongequal {\sin x \sim x} \frac {1}{3} \lim _ {x \rightarrow 0} f (x), \\ \end{array}</equation>即<equation>\lim_{x\to 0}f(x) = 6.</equation>（法二）同法一可得<equation>\lim_{x\rightarrow 0}f(x)\sin 2x=0</equation>.于是<equation>\lim_{x\rightarrow 0}\sqrt{1+f(x)\sin 2x}+1=2.</equation>从而<equation>\begin{array}{l} 2 = \lim _ {x \rightarrow 0} \frac {\sqrt {1 + f (x) \sin 2 x} - 1}{\mathrm {e} ^ {3 x} - 1} \xlongequal {\text {分 子 有 理 化}} \lim _ {x \rightarrow 0} \frac {f (x) \sin 2 x}{\left[ \sqrt {1 + f (x) \sin 2 x} + 1 \right]\left(\mathrm {e} ^ {3 x} - 1\right)} \\ = \lim _ {x \rightarrow 0} \frac {f (x) \sin 2 x}{2 \left(\mathrm {e} ^ {3 x} - 1\right)} = \lim _ {x \rightarrow 0} \frac {f (x) \cdot 2 x}{2 \cdot 3 x} = \frac {1}{3} \lim _ {x \rightarrow 0} f (x), \\ \end{array}</equation>即<equation>\lim_{x\to 0}f(x) = 6.</equation>

---

**2016年第15题 | 解答题 | 10分**

15. (本题满分10分）

求极限<equation>\lim_{x\to 0}(\cos 2x+2x\sin x)^{\frac{1}{x^{4}}}.</equation>

**解析:**记原极限为 I.

（法一）凑重要极限<equation>\lim_{x\to 0}(1 + x)^{\frac{1}{x}} = \mathrm{e}.</equation>由于<equation>x\to0</equation>时，<equation>\cos 2x+2x\sin x-1\to0</equation>，故<equation>\lim_{x\to0}(1+\cos 2x+2x\sin x-1)^{\frac{1}{\cos 2x+2x\sin x-1}}=e.</equation><equation>I = \lim _ {x \rightarrow 0} \left(1 + \cos 2 x + 2 x \sin x - 1\right) ^ {\frac {1}{\cos 2 x + 2 x \sin x - 1}} \cdot \frac {\cos 2 x + 2 x \sin x - 1}{x ^ {4}}.</equation>下面求<equation>\lim_{x\to 0}\frac{\cos 2x+2x\sin x-1}{x^{4}}.</equation><equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\cos 2 x + 2 x \sin x - 1}{x ^ {4}} \xlongequal {\cos 2 x - 1 = - 2 \sin^ {2} x} \lim _ {x \rightarrow 0} \frac {2 x \sin x - 2 \sin^ {2} x}{x ^ {4}} = \lim _ {x \rightarrow 0} \frac {2 \sin x (x - \sin x)}{x ^ {4}} \\ \frac {\sin x - x}{2 \lim _ {x \rightarrow 0} \frac {x - \sin x}{x ^ {3}}} = 2 \lim _ {x \rightarrow 0} \frac {x - x + \frac {x ^ {3}}{3 !} - o \left(x ^ {3}\right)}{x ^ {3}} = \frac {1}{3}. \\ \end{array}</equation>因此，<equation>I = \mathrm{e}^{\frac{1}{3}}.</equation>下面我们用另外两种方法计算<equation>\lim_{x\to 0}\frac{\cos 2x+2x\sin x-1}{x^{4}}.</equation>(1) 利用泰勒公式.<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\cos 2 x + 2 x \sin x - 1}{x ^ {4}} = \lim _ {x \rightarrow 0} \frac {1 - \frac {(2 x) ^ {2}}{2 !} + \frac {(2 x) ^ {4}}{4 !} + o \left(x ^ {4}\right) + 2 x \left[x - \frac {x ^ {3}}{3 !} + o \left(x ^ {3}\right)\right] - 1}{x ^ {4}} \\ = \lim _ {x \rightarrow 0} \frac {\frac {1}{3} x ^ {4} + o \left(x ^ {4}\right)}{x ^ {4}} = \frac {1}{3}. \\ \end{array}</equation>(2) 利用洛必达法则.<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\cos 2 x + 2 x \sin x - 1}{x ^ {4}} \xlongequal {\mathrm {洛必达}} \lim _ {x \rightarrow 0} \frac {- \sin 2 x + \sin x + x \cos x}{2 x ^ {3}} \\ \xlongequal {\mathrm {洛必达}} \lim _ {x \rightarrow 0} \frac {- 2 \cos 2 x + 2 \cos x - x \sin x}{6 x ^ {2}} \\ \xlongequal {\mathrm {洛必达}} \lim _ {x \rightarrow 0} \frac {4 \sin 2 x - 3 \sin x - x \cos x}{1 2 x} \\ \xlongequal {\mathrm {洛必达}} \lim _ {x \rightarrow 0} \frac {8 \cos 2 x - 4 \cos x + x \sin x}{1 2} = \frac {1}{3}. \\ \end{array}</equation>（法二）因为<equation>\lim_{x\to 0} (\cos 2x+2x\sin x)=1</equation>，从而我们可以对<equation>\cos 2x+2x\sin x</equation>取对数，所以 I =<equation>\mathrm{e}^{\lim_{x\to 0}\frac{\ln(\cos 2x+2x\sin x)}{x^{4}}}.</equation>下面求<equation>\lim_{x\to 0}\frac{\ln(\cos 2x+2x\sin x)}{x^{4}}.</equation><equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {\ln (\cos 2 x + 2 x \sin x)}{x ^ {4}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\frac {1}{\cos 2 x + 2 x \sin x} \cdot (- 2 \sin 2 x + 2 \sin x + 2 x \cos x)}{4 x ^ {3}} \\ &= - \frac {1}{2} \lim _ {x \rightarrow 0} \frac {\sin 2 x - \sin x - x \cos x}{x ^ {3}} \\ &= - \frac {1}{2} \lim _ {x \rightarrow 0} \frac {2 x - \frac {(2 x) ^ {3}}{3 !} + o \left(x ^ {3}\right) - x + \frac {x ^ {3}}{3 !} - o \left(x ^ {3}\right) - x \left[ 1 - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right)\right]}{x ^ {3}} \\ &= - \frac {1}{2} \lim _ {x \rightarrow 0} \frac {\left(- \frac {8}{6} + \frac {1}{6} + \frac {1}{2}\right) x ^ {3} + o \left(x ^ {3}\right)}{x ^ {3}} = \frac {1}{3}. \end{aligned}</equation>因此，<equation>I=\mathrm{e}^{\frac{1}{3}}.</equation>

---

**2015年第9题 | 填空题 | 4分**

（无内容）

**答案:**# -<equation>\frac{1}{2}.</equation>

**解析:**（法一）利用洛必达法则.<equation>\lim _ {x \rightarrow 0} \frac {\ln (\cos x)}{x ^ {2}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\frac {1}{\cos x} \cdot (- \sin x)}{2 x} = \lim _ {x \rightarrow 0} \left(- \frac {\sin x}{2 x}\right) = - \frac {1}{2}.</equation>（法二）利用等价无穷小替换.

当<equation>x\to0</equation>时，<equation>\cos x-1\to0,\ln(1+\cos x-1)\sim\cos x-1</equation>，于是<equation>\lim _ {x \rightarrow 0} \frac {\ln (\cos x)}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\ln (1 + \cos x - 1)}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\cos x - 1}{x ^ {2}} \xlongequal {1 - \cos x \sim \frac {1}{2} x ^ {2}} \lim _ {x \rightarrow 0} \frac {- \frac {1}{2} x ^ {2}}{x ^ {2}} = - \frac {1}{2}.</equation>

---

**2014年第15题 | 解答题 | 10分**

15. (本题满分10分)<equation>\mathrm {m} _ {\infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t \right] \mathrm {d} t}{x ^ {2} \ln \left(1 + \frac {1}{x}\right)}.</equation>

**答案:**<equation>(1 5) \frac {1}{2}.</equation>

**解析:**解 由于<equation>\mathrm{e}^{x}</equation>在 x=0处的带拉格朗日余项的2阶泰勒公式为<equation>\mathrm{e}^{x}=1+x+\frac{x^{2}}{2}+\frac{\mathrm{e}^{\theta x}}{3!} x^{3}</equation>其中<equation>0<\theta <1</equation>，故当 x > 0时，<equation>\mathrm{e}^{x}>1+x+\frac{x^{2}}{2}.</equation>于是，<equation>\mathrm{e}^{\frac{1}{t}}-1>\frac{1}{t}+\frac{1}{2t^{2}}(t>0),</equation><equation>t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t > t ^ {2} \left(\frac {1}{t} + \frac {1}{2 t ^ {2}}\right) - t = \frac {1}{2}.</equation>从而<equation>\int_1^{+\infty}[t^2(\mathrm{e}^{\frac{1}{t}} - 1) - t]\mathrm{d}t\to +\infty .</equation>另一方面，<equation>\lim _ {x \rightarrow + \infty} \left[ x ^ {2} \ln \left(1 + \frac {1}{x}\right)\right] \xlongequal {\ln \left(1 + \frac {1}{x}\right) - \frac {1}{x}} \lim _ {x \rightarrow + \infty} x = + \infty .</equation>因此，原极限为<equation>\frac{\infty}{\infty}</equation>型未定式.

当<equation>x\to +\infty</equation>时，<equation>\frac{1}{x}\rightarrow 0,\ln (1 + \frac{1}{x})\sim \frac{1}{x}</equation>，故<equation>\begin{array}{l} \lim _ {x \rightarrow + \infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t \right] \mathrm {d} t}{x ^ {2} \ln \left(1 + \frac {1}{x}\right)} \xlongequal {\ln \left(1 + \frac {1}{x}\right) - \frac {1}{x}} \lim _ {x \rightarrow + \infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t \right] \mathrm {d} t}{x} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow + \infty} \frac {x ^ {2} \left(\mathrm {e} ^ {\frac {1}{x}} - 1\right) - x}{1} = \lim _ {x \rightarrow + \infty} \frac {\mathrm {e} ^ {\frac {1}{x}} - 1 - \frac {1}{x}}{\frac {1}{x ^ {2}}} \\ \xlongequal {u = \frac {1}{x}} \lim _ {u \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {u} - u - 1}{u ^ {2}} \xlongequal {\text {洛必达}} \lim _ {u \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {u} - 1}{2 u} \\ \xlongequal {\mathrm {e} ^ {u} - 1 \sim u} \lim _ {u \rightarrow 0 ^ {+}} \frac {u}{2 u} = \frac {1}{2}. \\ \end{array}</equation>因此，原极限<equation>= \frac{1}{2}.</equation>将原极限化简为<equation>\lim_{x\to +\infty}[x^{2}(\mathrm{e}^{\frac{1}{x}} - 1) - x]</equation>后，也可以用泰勒公式来求该极限.

当<equation>x\to +\infty</equation>时，<equation>\frac{1}{x}\rightarrow 0^{+}</equation>.由<equation>e^{u}</equation>在<equation>u = 0</equation>处的泰勒公式得，<equation>\mathrm {e} ^ {\frac {1}{x}} = 1 + \frac {1}{x} + \frac {1}{2 !} \cdot \frac {1}{x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right).</equation>从而，<equation>\begin{array}{l} \lim _ {x \rightarrow + \infty} \left[ x ^ {2} \left(\mathrm {e} ^ {\frac {1}{x}} - 1\right) - x \right] = \lim _ {x \rightarrow + \infty} \left\{x ^ {2} \left[ \frac {1}{x} + \frac {1}{2 !} \cdot \frac {1}{x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right)\right] - x \right\} \\ = \lim _ {x \rightarrow + \infty} \left[ \frac {1}{2} + x ^ {2} \cdot o \left(\frac {1}{x ^ {2}}\right)\right] = \frac {1}{2}. \\ \end{array}</equation>

---

**2012年第9题 | 填空题 | 4分**

（无内容）

**解析:**解（法一）取对数和利用洛必达法则.<equation>\lim _ {x \rightarrow \frac {\pi}{4}} (\tan x) ^ {\frac {1}{\cos x - \sin x}} = \lim _ {x \rightarrow \frac {\pi}{4}} \mathrm {e} ^ {\frac {\ln (\tan x)}{\cos x - \sin x}} = \mathrm {e} ^ {\lim _ {x \rightarrow \frac {\pi}{4}} \frac {\ln (\tan x)}{\cos x - \sin x}} \xlongequal {\text {洛必达}} \mathrm {e} ^ {\lim _ {x \rightarrow \frac {\pi}{4}} \frac {\frac {1}{\tan x} \cdot \sec^ {2} x}{-\sin x - \cos x}} = \mathrm {e} ^ {\frac {1 \times 2}{- \sqrt {2}}} = \mathrm {e} ^ {- \sqrt {2}}.</equation>（法二）取对数和利用等价无穷小替换.<equation>\begin{array}{l} \lim _ {x \rightarrow \frac {\pi}{4}} (\tan x) ^ {\frac {1}{\cos x - \sin x}} = \lim _ {x \rightarrow \frac {\pi}{4}} e ^ {\frac {\ln (\tan x)}{\cos x - \sin x}} = e ^ {\lim _ {x \rightarrow \frac {\pi}{4}} \frac {\ln (\tan x)}{\cos x - \sin x}} = e ^ {\lim _ {x \rightarrow \frac {\pi}{4}} \frac {\ln (1 + \tan x - 1)}{\cos x - \sin x}} \\ \underline {{\frac {\ln (1 + \tan x - 1) \sim \tan x - 1}{e}}} e ^ {\lim _ {x \rightarrow \frac {\pi}{4}} \frac {\tan x - 1}{- \cos x (\tan x - 1)}} \\ = e ^ {\lim _ {x \rightarrow \frac {\pi}{4}} \frac {1}{- \cos x}} = e ^ {- \sqrt {2}}. \\ \end{array}</equation>（法三）凑重要极限.<equation>\lim _ {x \rightarrow \frac {\pi}{4}} (\tan x) ^ {\frac {1}{\cos x - \sin x}} = \lim _ {x \rightarrow \frac {\pi}{4}} (1 + \tan x - 1) ^ {\frac {1}{\cos x - \sin x}} = \lim _ {x \rightarrow \frac {\pi}{4}} (1 + \tan x - 1) ^ {\frac {1}{\tan x - 1} \cdot \frac {\tan x - 1}{\cos x - \sin x}}.</equation>由于<equation>\lim _ {x \rightarrow \frac {\pi}{4}} \frac {\tan x - 1}{\cos x - \sin x} = \lim _ {x \rightarrow \frac {\pi}{4}} \frac {\tan x - 1}{- \cos x (\tan x - 1)} = \lim _ {x \rightarrow \frac {\pi}{4}} \left(- \frac {1}{\cos x}\right) = - \sqrt {2},</equation>故原极限等于<equation>\mathrm{e}^{- \sqrt{2}}.</equation>

---

**2012年第15题 | 解答题 | 10分**

15. (本题满分10分)

**答案:**## (15)<equation>\frac{1}{1 2}.</equation>

**解析:**<equation>\begin{array}{l} \frac {\mathrm {e} ^ {2 - 2 \cos x - x ^ {2}} - 1 - 2 - 2 \cos x - x ^ {2}}{\lim _ {x \rightarrow 0} \left(2 - 2 \cos x - x ^ {2}\right)} \lim _ {x \rightarrow 0} 1 \cdot \frac {- \left(2 - 2 \cos x - x ^ {2}\right)}{x ^ {4}} \\ = \lim _ {x \rightarrow 0} \frac {x ^ {2} - 2 + 2 \left[ 1 - \frac {x ^ {2}}{2 !} + \frac {x ^ {4}}{4 !} + o \left(x ^ {4}\right)\right]}{x ^ {4}} = \lim _ {x \rightarrow 0} \frac {\frac {1}{1 2} x ^ {4}}{x ^ {4}} = \frac {1}{1 2}. \\ \end{array}</equation><equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x ^ {2}} - \mathrm {e} ^ {2 - 2 \cos x}}{x ^ {4}} \frac {\mathrm {拉 格 朗 日}}{\mathrm {中 值 定 值}} \lim _ {x \rightarrow 0} \mathrm {e} ^ {\xi_ {x}} \cdot \frac {x ^ {2} - (2 - 2 \cos x)}{x ^ {4}} \\ = \lim _ {x \rightarrow 0} \frac {x ^ {2} - (2 - 2 \cos x)}{x ^ {4}} \frac {\mathrm {同 法 一}}{\mathrm {同 法 一}} \frac {1}{1 2}. \\ \end{array}</equation>

---

**2011年第9题 | 填空题 | 4分**

**答案:**##<equation>(1 + 3x)\mathrm{e}^{3x}.</equation>

**解析:**由<equation>\lim_{t\to 0}(1 + t)^{\frac{1}{t}} = \mathrm{e}</equation>知，<equation>f(x) = x\lim_{t\to 0}\left[(1 + 3t)^{\frac{1}{3t}}\right]^{3x} = x\mathrm{e}^{3x}</equation>. 因此，<equation>f ^ {\prime} (x) = \mathrm {e} ^ {3 x} + 3 x \mathrm {e} ^ {3 x} = (1 + 3 x) \mathrm {e} ^ {3 x}.</equation>也可以用另一种方法来计算 f(x).把 x看作常数，t看作变量，极限为<equation>1^{\infty}</equation>型.采用改写成指数形式的方法.<equation>\begin{array}{l} f (x) = \lim _ {t \rightarrow 0} x \left(1 + 3 t\right) ^ {\frac {x}{t}} = \lim _ {t \rightarrow 0} x \mathrm {e} ^ {\frac {x}{t} \ln (1 + 3 t)} = x \cdot \mathrm {e} ^ {\lim _ {t \rightarrow 0} \frac {x}{t} \ln (1 + 3 t)} \\ \underline {{\ln (1 + 3 t) - 3 t}} x \cdot \mathrm {e} ^ {\lim _ {t \rightarrow 0} \frac {x}{t} \cdot 3 t} = x \mathrm {e} ^ {3 x}. \\ \end{array}</equation>

---

**2011年第15题 | 解答题 | 10分**

15. (本题满分10分)

求极限 lim<equation>\frac {\sqrt {1 + 2 \sin x} - x - 1}{x \ln (1 + x)}.</equation>

**答案:**<equation>(1 5) - \frac {1}{2}.</equation>

**解析:**解 （法一）利用等价无穷小替换和洛必达法则.<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\sqrt {1 + 2 \sin x} - x - 1}{x \ln (1 + x)} \xlongequal {\ln (1 + x) \sim x} \lim _ {x \rightarrow 0} \frac {\sqrt {1 + 2 \sin x} - x - 1}{x ^ {2}} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\left(1 + 2 \sin x\right) ^ {- \frac {1}{2}} \cdot \cos x - 1}{2 x} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {- \frac {1}{2} \left(1 + 2 \sin x\right) ^ {- \frac {3}{2}} \cdot 2 \cos^ {2} x - \left(1 + 2 \sin x\right) ^ {- \frac {1}{2}} \cdot \sin x}{2} \\ = \frac {- \frac {1}{2} \times 1 \times 2 - 0}{2} = - \frac {1}{2}. \\ \end{array}</equation>（法二）利用分子有理化对极限式进行转化.<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\sqrt {1 + 2 \sin x} - x - 1}{x \ln (1 + x)} \xlongequal {\ln (1 + x) \sim x} \lim _ {x \rightarrow 0} \frac {\sqrt {1 + 2 \sin x} - x - 1}{x ^ {2}} \\ \xlongequal {\mathrm {分 子 有 理 化}} \lim _ {x \rightarrow 0} \frac {1 + 2 \sin x - (x + 1) ^ {2}}{x ^ {2} \left(\sqrt {1 + 2 \sin x} + x + 1\right)} = \lim _ {x \rightarrow 0} \frac {2 \sin x - x ^ {2} - 2 x}{2 x ^ {2}} \\ \xlongequal {\sin x = x - \frac {x ^ {3}}{3 !} + o \left(x ^ {3}\right)} \lim _ {x \rightarrow 0} \frac {- x ^ {2} - \frac {x ^ {3}}{3} + o \left(x ^ {3}\right)}{2 x ^ {2}} = - \frac {1}{2}. \\ \end{array}</equation>（法三）当<equation>x\to 0</equation>时，<equation>(1+x)^{\alpha}</equation>的二阶泰勒公式为<equation>(1+x)^{\alpha}=1+\alpha x+\frac{\alpha(\alpha-1)}{2} x^{2}+o\left(x^{2}\right).</equation>由于<equation>x\to 0</equation>时，<equation>\sin x\to 0</equation>，故<equation>(1 + 2 \sin x) ^ {\frac {1}{2}} = 1 + \sin x - \frac {1}{2} \sin^ {2} x + o \left(4 \sin^ {2} x\right) = 1 + \sin x - \frac {1}{2} \sin^ {2} x + o \left(x ^ {2}\right),</equation>这里<equation>o\left(4\sin^{2}x\right) = o\left(x^{2}\right)</equation>是因为<equation>\sin^{2}x</equation>与<equation>x^{2}</equation>是<equation>x\to 0</equation>时的等价无穷小量.因此，<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\sqrt {1 + 2 \sin x} - x - 1}{x \ln (1 + x)} \xlongequal {\ln (1 + x) - x} \lim _ {x \rightarrow 0} \frac {\sqrt {1 + 2 \sin x} - x - 1}{x ^ {2}} \\ = \lim _ {x \rightarrow 0} \frac {1 + \sin x - \frac {1}{2} \sin^ {2} x + o \left(x ^ {2}\right) - x - 1}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\sin x - x - \frac {1}{2} \sin^ {2} x}{x ^ {2}} \\ = \lim _ {x \rightarrow 0} \left(\frac {\sin x - x}{x ^ {2}} - \frac {\sin^ {2} x}{2 x ^ {2}}\right) = \lim _ {x \rightarrow 0} \frac {\sin x - x}{x ^ {2}} - \frac {1}{2} \\ \end{array}</equation><equation>\frac {\sin x = x - \frac {x ^ {3}}{3 !} + o \left(x ^ {3}\right)}{\lim _ {x \rightarrow 0} \frac {- \frac {x ^ {3}}{6} + o \left(x ^ {3}\right)}{x ^ {2}} - \frac {1}{2}} = 0 - \frac {1}{2} = - \frac {1}{2}.</equation>

---

**2010年第15题 | 解答题 | 10分**

15. (本题满分10分)

求极限<equation>\lim_{x\to +\infty}\left(x^{\frac{1}{x}} - 1\right)^{\frac{1}{\ln x}}.</equation>

**答案:**(15)<equation>\mathrm{e}^{-1}.</equation>

**解析:**解（法一）记<equation>y = \left(x^{\frac{1}{x}} - 1\right)^{\frac{1}{\ln x}}</equation>，则<equation>\ln y = \frac {\ln \left(x ^ {\frac {1}{x}} - 1\right)}{\ln x}.</equation>利用洛必达法则计算<equation>\lim \ln y</equation>得，<equation>\begin{array}{l} \lim _ {x \rightarrow + \infty} \frac {\ln \left(x ^ {\frac {1}{x}} - 1\right)}{\ln x} = \lim _ {x \rightarrow + \infty} \frac {\ln \left(\mathrm {e} ^ {\frac {\ln x}{x}} - 1\right)}{\ln x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow + \infty} \frac {\mathrm {e} ^ {\frac {\ln x}{x}} \cdot \frac {1 - \ln x}{x ^ {2}}}{\frac {1}{x} \left(\mathrm {e} ^ {\frac {\ln x}{x}} - 1\right)} \xlongequal {\lim _ {x \rightarrow + \infty} \mathrm {e} ^ {\frac {\ln x}{x}} = 1} \lim _ {x \rightarrow + \infty} \frac {\frac {1 - \ln x}{x}}{\frac {\ln x}{x}} \\ = \lim _ {x \rightarrow + \infty} \frac {1 - \ln x}{\ln x} = \lim _ {x \rightarrow + \infty} \left(\frac {1}{\ln x} - 1\right) = - 1. \\ \end{array}</equation>因此，原极限<equation>= \mathrm{e}^{-1}</equation>或者也可以这样计算.<equation>\begin{array}{l} \lim _ {x \rightarrow + \infty} \frac {\ln \left(x ^ {\frac {1}{x}} - 1\right)}{\ln x} = \lim _ {x \rightarrow + \infty} \frac {\ln \left(\mathrm {e} ^ {\frac {\ln x}{x}} - 1\right)}{\ln x} \stackrel {\text {洛必达}} {=} \lim _ {x \rightarrow + \infty} \frac {\frac {\mathrm {e} ^ {\frac {\ln x}{x}} \cdot \frac {1 - \ln x}{x ^ {2}}}{\frac {1}{x} \left(\mathrm {e} ^ {\frac {\ln x}{x}} - 1\right)}}{\frac {\lim _ {x \rightarrow + \infty} \mathrm {e} ^ {\frac {\ln x}{x}} = 1}{\lim _ {x \rightarrow + \infty} \frac {1 - \ln x}{x}}} \\ \underline {{\mathrm {洛必达}}} \lim _ {x \rightarrow + \infty} \frac {\frac {- 2 + \ln x}{x ^ {2}}}{\mathrm {e} ^ {\frac {\ln x}{x}} \cdot \frac {1 - \ln x}{x ^ {2}}} = \lim _ {x \rightarrow + \infty} \frac {- 2 + \ln x}{1 - \ln x} = - 1. \\ \end{array}</equation>（法二）注意到<equation>\lim_{u\to 0^{+}}\frac{\ln(\mathrm{e}^{u}-1)}{\ln u}\xlongequal{\text{洛必达}}\lim_{u\to 0^{+}}\frac{u\mathrm{e}^{u}}{\mathrm{e}^{u}-1}\xlongequal{\text{e}^{u}-1\sim u}\lim_{u\to 0^{+}}\frac{u\mathrm{e}^{u}}{u}=1</equation>，故<equation>\frac {\ln \left(\mathrm {e} ^ {\frac {\ln x}{x}} - 1\right)}{\ln \frac {\ln x}{x}} \cdot \ln \frac {\ln x}{x}</equation><equation>\begin{array}{l} \lim _ {x \rightarrow + \infty} \frac {\ln \left(x ^ {\frac {1}{x}} - 1\right)}{\ln x} = \lim _ {x \rightarrow + \infty} \frac {\ln \left(\mathrm {e} ^ {\frac {\ln x}{x}} - 1\right)}{\ln x} = \lim _ {x \rightarrow + \infty} \frac {\ln \frac {\ln x}{x} ^ {x}}{\ln x} \\ = \lim _ {x \rightarrow + \infty} \frac {\ln \frac {\ln x}{x}}{\ln x} = \lim _ {x \rightarrow + \infty} \frac {\ln \ln x - \ln x}{\ln x} \\ \underline {{\underline {{\text {洛必达}}}}} \lim _ {x \rightarrow + \infty} \left(\frac {1}{\ln x} - 1\right) = - 1. \\ \end{array}</equation>因此，原极限<equation>= \mathrm{e}^{-1}</equation>

---

**2009年第9题 | 填空题 | 4分**

（无内容）

**解析:**（法三）<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\mathrm {e} - \mathrm {e} ^ {\cos x}}{\sqrt {3} \sqrt {1 + x ^ {2}} - 1} = \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {1} - \mathrm {e} ^ {\cos x}}{\frac {1}{3} x ^ {2}} \\ \frac {\mathrm {拉 格 朗 日}}{\mathrm {中 值 定 值}} \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {\xi_ {x}} (1 - \cos x)}{\frac {1}{3} x ^ {2}} (\xi_ {x} \mathrm {在} 1 \mathrm {与} \cos x \mathrm {之间}, \mathrm {当} x \rightarrow 0 \mathrm {时}, \xi_ {x} \rightarrow 1) \\ = \lim _ {x \rightarrow 0} \mathrm {e} \cdot \frac {\frac {1}{2} x ^ {2}}{\frac {1}{3} x ^ {2}} = \frac {3}{2} \mathrm {e}. \\ \end{array}</equation>（法四）<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\mathrm {e} - \mathrm {e} ^ {\cos x}}{\sqrt {3} \left(1 + x ^ {2}\right) - 1} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {\cos x} \cdot \sin x}{\frac {1}{3} \left(1 + x ^ {2}\right) ^ {- \frac {2}{3}} \cdot 2 x} = \lim _ {x \rightarrow 0} \frac {3}{2} \left(1 + x ^ {2}\right) ^ {\frac {2}{3}} \cdot \frac {\mathrm {e} ^ {\cos x} \cdot \sin x}{x} \\ = \frac {3}{2} \times 1 \times \mathrm {e} = \frac {3}{2} \mathrm {e}. \\ \end{array}</equation>解（法一）<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\mathrm {e} - \mathrm {e} ^ {\cos x}}{\sqrt {3} \left(1 + x ^ {2}\right) - 1} \equiv \frac {(1 + x) ^ {\alpha} - 1 \sim \alpha x}{\overline {{\quad}}} \lim _ {x \rightarrow 0} \frac {\mathrm {e} - \mathrm {e} ^ {\cos x}}{\frac {1}{3} x ^ {2}} \equiv \frac {\text {洛必达}}{\overline {{\quad}}} \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {\cos x} \cdot \sin x}{\frac {2}{3} x} \\ = \lim _ {x \rightarrow 0} \frac {3}{2} \mathrm {e} ^ {\cos x} = \frac {3}{2} \mathrm {e}. \\ \end{array}</equation>（法二）<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\mathrm {e} - \mathrm {e} ^ {\cos x}}{\sqrt {3} \sqrt {1 + x ^ {2}} - 1} \xlongequal {(1 + x) ^ {\alpha} - 1 \sim \alpha x} \lim _ {x \rightarrow 0} \frac {\mathrm {e} \left(1 - \mathrm {e} ^ {\cos x - 1}\right)}{\frac {1}{3} x ^ {2}} \\ \xlongequal {\mathrm {e} ^ {\cos x - 1} - 1 \sim \cos x - 1} \lim _ {x \rightarrow 0} \frac {\mathrm {e} [ - (\cos x - 1) ]}{\frac {1}{3} x ^ {2}} \\ \xlongequal {1 - \cos x \sim \frac {1}{2} x ^ {2}} \lim _ {x \rightarrow 0} \frac {\frac {1}{2} \mathrm {e} x ^ {2}}{\frac {1}{3} x ^ {2}} = \frac {3}{2} \mathrm {e}. \\ \end{array}</equation>
