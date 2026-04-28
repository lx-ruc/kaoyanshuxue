#### 矩阵的秩

**2025年第7题 | 选择题 | 5分 | 答案: A**

7. 设 n阶矩阵 A,B,C满足<equation>r ( A )+r ( B )+r ( C )=r ( A B )+2 n</equation>，给出下列四个结论：

I.<equation>r ( A B )+n=r ( A B )+r ( C )</equation>II.<equation>r ( A B )+n=r ( A )+r ( B )</equation>III.<equation>r ( A )=r ( B )=r ( C )=n</equation>IV.<equation>r ( A B )=r ( B C )=n</equation>其中正确的选项是（    ）

A. I、II B. I、III C. II、IV D. III、IV

答案: A

**解析:**解下面说明<equation>\textcircled{3}</equation><equation>\textcircled{4}</equation>不正确.

取 n=2，<equation>A=C=E,B=O</equation>，则<equation>AB=BC=ABC=O,r(A)=r(C)=2,r(B)=r(ABC)= 0</equation>，满足<equation>r(A)+r(B)+r(C)=r(ABC)+4=4.</equation>但此时，<equation>\textcircled{3},\textcircled{4}</equation>均不成立.

由排除法可知，应选A.

下面说明<equation>\textcircled{1}</equation><equation>\textcircled{2}</equation>正确.

首先，<equation>r ( A ) + r ( B ) = r \left( \begin{array}{cc} A & O \\ O & B \end{array} \right) \leqslant r \left( \begin{array}{cc} A & O \\ E & B \end{array} \right).</equation>另一方面，<equation>\left( \begin{array}{c c} E & - A \\ O & E \end{array} \right) \left( \begin{array}{c c} A & O \\ E & B \end{array} \right) \left( \begin{array}{c c} O & E \\ E & O \end{array} \right) = \left( \begin{array}{c c} O & - A B \\ E & B \end{array} \right) \left( \begin{array}{c c} O & E \\ E & O \end{array} \right) = \left( \begin{array}{c c} - A B & O \\ B & E \end{array} \right).</equation>于是，<equation>r \left( \begin{array}{c c} A & O \\ E & B \end{array} \right) = r \left( \begin{array}{c c} - A B & O \\ B & E \end{array} \right) = r (A B) + n</equation>，进一步可得<equation>r (A) + r (B)\leqslant r (A B) + n.</equation>对该式两端同时加上<equation>r (C)</equation>并结合<equation>r (A B C) + 2 n = r (A) + r (B) + r (C)</equation>可得<equation>r (\mathbf {A B C}) + 2 n = r (\mathbf {A}) + r (\mathbf {B}) + r (\mathbf {C}) \leqslant r (\mathbf {A B}) + r (\mathbf {C}) + n,</equation>即<equation>r(\mathbf{ABC}) + n \leqslant r(\mathbf{AB}) + r(\mathbf{C})</equation>令<equation>P=A B</equation>，则由<equation>r(A)+r(B)\leqslant r(A B)+n</equation>可得<equation>r(P)+r(C)\leqslant r(P C)+n</equation>，即<equation>r(A B)+r(C)\leqslant r(A B C)+n.</equation>因此，<equation>r ( A B C ) + n = r ( A B ) + r ( C )</equation><equation>\textcircled{1}</equation>正确.

联立<equation>\left\{ \begin{array}{l l} r ( A B C ) + 2 n = r ( A ) + r ( B ) + r ( C ) \\ r ( A B C ) + n = r ( A B ) + r ( C ) , \end{array} \right.</equation>两式相减可得 n = r(A) + r(B) - r(AB)，即<equation>r ( A B ) + n = r ( A ) + r ( B ).</equation>因此，<equation>\textcircled{2}</equation>正确.

也可以用下面的方法证明<equation>r(A) + r(B) \leqslant r(AB) + n.</equation>考虑方程组<equation>Ax = 0, Bx = 0, ABx = 0, Ax = 0</equation>的解空间的维数为<equation>r_{1} = n - r(A), Bx = 0</equation>的解空间的维数为<equation>r_{2} = n - r(B), ABx = 0</equation>的解空间的维数为<equation>r_{3} = n - r(AB)</equation>. 若能证明<equation>r_{3} \leqslant r_{1} + r_{2}</equation>即<equation>n - r(AB) \leqslant n - r(A) + n - r(B)</equation>, 则可得<equation>r(A) + r(B) \leqslant r(AB) + n</equation>.

记<equation>r = r_{3} - r_{2}</equation>，则<equation>r_{2} + r = r_{3}</equation>.取<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{r_{2}}</equation>为方程组<equation>Bx = 0</equation>的一个基础解系.由于<equation>Bx = 0</equation>的解均为<equation>ABx = 0</equation>的解，故可设<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{r_{2}},\beta_{1},\beta_{2},\dots ,\beta_{r}</equation>为方程组<equation>ABx = 0</equation>的一个基础解系.

由于<equation>\beta_{i} ( i=1,2,\dots,r)</equation>均满足<equation>A B x=0</equation>，故<equation>B \beta_{i} ( i=1,2,\dots,r)</equation>均为方程组<equation>A x=0</equation>的解。若能证明<equation>B \beta_{1},B \beta_{2},\dots,B \beta_{r}</equation>线性无关，则由<equation>B \beta_{1},B \beta_{2},\dots,B \beta_{r}</equation>的秩不超过<equation>A x=0</equation>的解空间的维数可得<equation>r=r_{3}-r_{2}\leqslant r_{1}</equation>即<equation>r_{3}\leqslant r_{1}+r_{2}.</equation>设<equation>k_{1}, k_{2}, \dots , k_{r}</equation>满足<equation>k _ {1} \boldsymbol {B} \boldsymbol {\beta} _ {1} + k _ {2} \boldsymbol {B} \boldsymbol {\beta} _ {2} + \dots + k _ {r} \boldsymbol {B} \boldsymbol {\beta} _ {r} = \mathbf {0}.</equation>整理可得<equation>B \left(k_{1}\boldsymbol{\beta}_{1}+k_{2}\boldsymbol{\beta}_{2}+\dots+k_{r}\boldsymbol{\beta}_{r}\right)=0</equation>，由此可知<equation>k_{1}\boldsymbol{\beta}_{1}+k_{2}\boldsymbol{\beta}_{2}+\dots+k_{r}\boldsymbol{\beta}_{r}</equation>是方程组<equation>B x=0</equation>的解，从而存在<equation>l_{1},l_{2},\dots,l_{r_{2}}</equation>，使得<equation>k _ {1} \boldsymbol {\beta} _ {1} + k _ {2} \boldsymbol {\beta} _ {2} + \dots + k _ {r} \boldsymbol {\beta} _ {r} = l _ {1} \boldsymbol {\alpha} _ {1} + l _ {2} \boldsymbol {\alpha} _ {2} + \dots + l _ {r _ {2}} \boldsymbol {\alpha} _ {r _ {2}},</equation>即<equation>k_{1}\boldsymbol{\beta}_{1} + k_{2}\boldsymbol{\beta}_{2} + \dots + k_{r}\boldsymbol{\beta}_{r} - l_{1}\boldsymbol{\alpha}_{1} - l_{2}\boldsymbol{\alpha}_{2} - \dots - l_{r_{2}}\boldsymbol{\alpha}_{r_{2}} = 0.</equation>由于<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{r_2},\beta_1,\beta_2,\dots ,\beta_r</equation>线性无关，故<equation>k_{1} = k_{2} = \dots = k_{r} = l_{1} = l_{2} = \dots = l_{r_2} = 0</equation>，进一步可得<equation>B\beta_{1},B\beta_{2},\dots ,B\beta_{r}</equation>线性无关.

由前面的分析可知，<equation>r ( A ) + r ( B ) \leqslant r ( A B ) + n.</equation>

---

**2023年第5题 | 选择题 | 5分 | 答案: B**

5. 已知 n阶矩阵 A,B,C满足<equation>A B C=O, E</equation>为 n阶单位矩阵，记矩阵<equation>\left( \begin{array}{c c} O & A \\ B C & E \end{array} \right), \left( \begin{array}{c c} A B & C \\ O & E \end{array} \right), \left( \begin{array}{c c} E & A B \\ A B & O \end{array} \right)</equation>的秩分别为<equation>r_{1}, r_{2}, r_{3}</equation>，则（    ）

A.<equation>r_{1}\leqslant r_{2}\leqslant r_{3}</equation>B.<equation>r_{1}\leqslant r_{3}\leqslant r_{2}</equation>C.<equation>r_{3}\leqslant r_{1}\leqslant r_{2}</equation>D.<equation>r_{2}\leqslant r_{1}\leqslant r_{3}</equation>

答案: B

**解析:**解记<equation>M_{1} = \left( \begin{array}{cc}O&A\\ BC&E \end{array} \right), M_{2} = \left( \begin{array}{cc}AB&C\\ O&E \end{array} \right), M_{3} = \left( \begin{array}{cc}E&AB\\ AB&O \end{array} \right).</equation>分别对<equation>M_{1}, M_{2}, M_{3}</equation>作初等变换.<equation>M _ {1} = \left( \begin{array}{c c} O & A \\ B C & E \end{array} \right) \xrightarrow {\textcircled{1}} \left( \begin{array}{c c} - A B C & O \\ B C & E \end{array} \right) \xlongequal {A B C = O} \left( \begin{array}{c c} O & O \\ B C & E \end{array} \right).</equation><equation>M _ {2} = \left( \begin{array}{c c} A B & C \\ O & E \end{array} \right) \xrightarrow {\textcircled{2}} \left( \begin{array}{c c} A B & O \\ O & E \end{array} \right).</equation><equation>M _ {3} = \left( \begin{array}{c c} E & A B \\ A B & O \end{array} \right) \xrightarrow {\textcircled{3}} \left( \begin{array}{c c} E & A B \\ O & - A B A B \end{array} \right) \xrightarrow {\textcircled{4}} \left( \begin{array}{c c} E & O \\ O & - A B A B \end{array} \right).</equation>操作<equation>\textcircled{1}</equation>对应左乘可逆矩阵<equation>\left( \begin{array}{cc} E & -A \\ O & E \end{array} \right)</equation>，操作<equation>\textcircled{2}</equation>对应左乘可逆矩阵<equation>\left( \begin{array}{cc} E & -C \\ O & E \end{array} \right)</equation>，操作<equation>\textcircled{3}</equation>对应左乘可逆矩阵<equation>\left( \begin{array}{cc} E & O \\ -AB & E \end{array} \right)</equation>，操作<equation>\textcircled{4}</equation>对应右乘可逆矩阵<equation>\left( \begin{array}{cc} E & -AB \\ O & E \end{array} \right)</equation>由前面的计算可得<equation>r _ {1} = r \left(\boldsymbol {M} _ {1}\right) = r (\boldsymbol {E}) = n,</equation><equation>r _ {2} = r \left(\boldsymbol {M} _ {2}\right) = r (\boldsymbol {E}) + r (\boldsymbol {A B}) \geqslant n,</equation><equation>r _ {3} = r \left(\boldsymbol {M} _ {3}\right) = r (\boldsymbol {E}) + r \left(\boldsymbol {A B A B}\right) \geqslant n.</equation>由此可得，<equation>r_{1}\leqslant r_{2},r_{1}\leqslant r_{3}</equation>. 又因为<equation>r(\mathbf{ABAB})\leqslant r(\mathbf{AB})</equation>，所以<equation>r_{3}\leqslant r_{2}</equation>综上所述，<equation>r_{1}\leqslant r_{3}\leqslant r_{2}</equation>，应选B.

---

**2021年第7题 | 选择题 | 5分 | 答案: C**

7. 设 A,B为 n阶实矩阵，下列结论不成立的是（    )

A.<equation>r \left( \begin{array}{c c} A & O \\ O & A^{\mathrm{T}} A \end{array} \right)=2 r (A)</equation>B.<equation>r \left( \begin{array}{c c} A & A B \\ O & A^{\mathrm{T}} \end{array} \right)=2 r (A)</equation>C.<equation>r \left( \begin{array}{c c} A & B A \\ O & A A^{\mathrm{T}} \end{array} \right)=2 r (A)</equation>D.<equation>r \left( \begin{array}{c c} A & O \\ B A & A^{\mathrm{T}} \end{array} \right)=2 r (A)</equation>

答案: C

**解析:**依次分析4个选项.

选项A：由矩阵的秩的结论，<equation>r ( \mathbf{A}^{ \mathrm{T}} \mathbf{A} )=r ( \mathbf{A} )</equation>.因此，<equation>r \left( \begin{array}{cc} \mathbf{A} & \mathbf{O} \\ \mathbf{O} & \mathbf{A}^{ \mathrm{T}} \mathbf{A} \end{array} \right)=r ( \mathbf{A} )+r ( \mathbf{A} )=2 r ( \mathbf{A} ).</equation>选项 A成立.

选项B：由于<equation>\left( \begin{array}{c c} A & A B \\ O & A ^ {\mathrm {T}} \end{array} \right) = \left( \begin{array}{c c} A & O \\ O & A ^ {\mathrm {T}} \end{array} \right) \left( \begin{array}{c c} E & B \\ O & E \end{array} \right),</equation>故<equation>r \left( \begin{array}{cc} A & A B \\ O & A^{\mathrm{T}} \end{array} \right) = r \left( \begin{array}{cc} A & O \\ O & A^{\mathrm{T}} \end{array} \right) = 2 r (A).</equation>选项B成立.

选项C：BA的列向量均可由B的列向量表示，但不一定可由A的列向量表示。由此出发考虑选项C的反例.

令<equation>A = \left( \begin{array}{cc}0 & 1\\ 0 & 0 \end{array} \right),B = \left( \begin{array}{cc}0 & 1\\ 1 & 0 \end{array} \right),B A = \left( \begin{array}{cc}0 & 0\\ 0 & 1 \end{array} \right),A A^{\mathrm{T}} = \left( \begin{array}{cc}0 & 1\\ 0 & 0 \end{array} \right)\left( \begin{array}{cc}0 & 0\\ 1 & 0 \end{array} \right) = \left( \begin{array}{cc}1 & 0\\ 0 & 0 \end{array} \right)</equation>.于是，<equation>\left( \begin{array}{c c} \boldsymbol {A} & \boldsymbol {B A} \\ \boldsymbol {O} & \boldsymbol {A A} ^ {\mathrm {T}} \end{array} \right) = \left( \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{array} \right).</equation><equation>r \left( \begin{array}{cc} A & B A \\ O & A A^{\mathrm{T}} \end{array} \right) = 3</equation>，而<equation>2 r ( \mathbf{A} )=2.</equation>两者不相等.选项C不成立.

选项D：由于<equation>\left( \begin{array}{c c} A & O \\ B A & A ^ {\mathrm {T}} \end{array} \right) = \left( \begin{array}{c c} E & O \\ B & E \end{array} \right) \left( \begin{array}{c c} A & O \\ O & A ^ {\mathrm {T}} \end{array} \right),</equation>故<equation>r \left( \begin{array}{cc} \boldsymbol{A} & \boldsymbol{O} \\ \boldsymbol{B A} & \boldsymbol{A}^{\mathrm{T}} \end{array} \right) = r \left( \begin{array}{cc} \boldsymbol{A} & \boldsymbol{O} \\ \boldsymbol{O} & \boldsymbol{A}^{\mathrm{T}} \end{array} \right) = 2 r (\boldsymbol{A}).</equation>选项D成立.

综上所述，应选C.

---

**2018年第6题 | 选择题 | 4分 | 答案: A**

6. 设 A,B为 n阶矩阵，记 r(X)为矩阵 X的秩，(X,Y)表示分块矩阵，则（    ）

A.<equation>r ( A, A B )=r ( A )</equation>B.<equation>r ( A, B A )=r ( A )</equation>C.<equation>r ( A, B )=\max \{ r ( A ) , r ( B ) \}</equation>D.<equation>r ( A, B )=r \left( A^{\mathrm{T}}, B^{\mathrm{T}} \right)</equation>

答案: A

**解析:**解记 C=AB.由于右乘矩阵表示对矩阵作列变换，故 C的列向量可由 A的列向量线性表示.于是，<equation>r ( A, C )=r ( A, A B )=r ( A ).</equation>因此，应选A.

下面分别说明选项B、C、D不正确.

选项B：<equation>r(\mathbf{A},\mathbf{B}\mathbf{A})\geqslant r(\mathbf{A}).</equation>.但是，<equation>r(\mathbf{A},\mathbf{B}\mathbf{A})=r(\mathbf{A})</equation>并不成立.

取<equation>A = \left( \begin{array}{ll}1 & 0\\ 0 & 0 \end{array} \right),B = \left( \begin{array}{ll}1 & 0\\ 1 & 1 \end{array} \right)</equation>，则<equation>BA = \left( \begin{array}{ll}1 & 0\\ 1 & 0 \end{array} \right),(A,BA) = \left( \begin{array}{lll}1 & 0 & 1 & 0\\ 0 & 0 & 1 & 0 \end{array} \right).r(A,BA) = 2</equation>，但<equation>r(A) = 1.</equation>选项C：<equation>r(\mathbf{A},\mathbf{B})\geqslant \max \{r(\mathbf{A}),r(\mathbf{B})\}</equation>.但是，<equation>r(\mathbf{A},\mathbf{B})=\max \{r(\mathbf{A}),r(\mathbf{B})\}</equation>并不成立.

取<equation>A = \left( \begin{array}{ll}1 & 0\\ 0 & 0 \end{array} \right),B = \left( \begin{array}{ll}0 & 0\\ 1 & 0 \end{array} \right)</equation>，则<equation>(A,B) = \left( \begin{array}{lll}1 & 0 & 0 & 0\\ 0 & 0 & 1 & 0 \end{array} \right),r(A,B) = 2</equation>，但<equation>r(A) = r(B) = 1.</equation>选项D：由于<equation>r(\mathbf{P})=r(\mathbf{P}^{\mathrm{T}})</equation>，而<equation>\left( \mathbf{A},\mathbf{B}\right)^{\mathrm{T}}=\binom{\mathbf{A}^{\mathrm{T}}}{\mathbf{B}^{\mathrm{T}}}</equation>，故<equation>r(\mathbf{A},\mathbf{B})=r\binom{\mathbf{A}^{\mathrm{T}}}{\mathbf{B}^{\mathrm{T}}}</equation>.但是，<equation>r(\mathbf{A},\mathbf{B})=r(\mathbf{A}^{\mathrm{T}},\mathbf{B}^{\mathrm{T}})</equation>并不成立.

取<equation>A=\left( \begin{array}{cc}1&0\\ 0&0 \end{array} \right), B=\left( \begin{array}{cc}0&0\\ 1&0 \end{array} \right),</equation>则<equation>\left( A,B\right)=\left( \begin{array}{c c c c}1&0&0&0\\ 0&0&1&0 \end{array} \right), \left( A^{\mathrm{T}},B^{\mathrm{T}}\right)=\left( \begin{array}{c c c c}1&0&0&1\\ 0&0&0&0 \end{array} \right). r \left( A,B\right)</equation>=2，但<equation>r \left( A^{\mathrm{T}},B^{\mathrm{T}}\right)=1.</equation>

---

**2017年第13题 | 填空题 | 4分**

13. 设矩阵<equation>A=\left( \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 2 \\ 0 & 1 & 1 \end{array} \right), \alpha_{1},\alpha_{2},\alpha_{3}</equation>为线性无关的3维列向量组，则向量组<equation>A\alpha_{1},A\alpha_{2},A\alpha_{3}</equation>的秩为 ___.

**答案:**```latex

2.
```
**解析: **由于<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性无关，故矩阵<equation>\left(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}\right)</equation>可逆，从而<equation>r \left(\boldsymbol {A} \boldsymbol {\alpha} _ {1}, \boldsymbol {A} \boldsymbol {\alpha} _ {2}, \boldsymbol {A} \boldsymbol {\alpha} _ {3}\right) = r \left(\boldsymbol {A} \left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\alpha} _ {2}, \boldsymbol {\alpha} _ {3}\right)\right) = r (\boldsymbol {A}).</equation>下面我们用三种方法计算<equation>r ( \mathbf{A} ).</equation>（法一）计算<equation>|A|</equation>得<equation>|A|=0</equation>，故<equation>r(A)\leqslant 2</equation>.又因为矩阵 A含有一个非零2阶子式，例如<equation>\left| \begin{array}{ll} 1 & 0 \\ 1 & 1 \end{array} \right|=1</equation>，所以<equation>r(A)\geqslant 2</equation>.因此，<equation>r(A)=2</equation>，从而向量组<equation>A\alpha_{1},A\alpha_{2},A\alpha_{3}</equation>的秩为2.

（法二）对矩阵<equation>A</equation>作初等行变换将其化为阶梯形矩阵，进而求得其秩.<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 2 \\ 0 & 1 & 1 \end{array} \right) \xrightarrow {r _ {2} - r _ {1}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 1 & 1 \end{array} \right) \xrightarrow {r _ {3} - r _ {2} ^ {*}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每作一次初等行变换，加一个 *.）

因此，<equation>r(\mathbf{A}) = 2.</equation>（法三）令<equation>\boldsymbol{\beta}_{1}=(1,1,0)^{\mathrm{T}},\boldsymbol{\beta}_{2}=(0,1,1)^{\mathrm{T}},\boldsymbol{\beta}_{3}=(1,2,1)^{\mathrm{T}}</equation>，则<equation>\boldsymbol{A}=(\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3})</equation>.由于<equation>\boldsymbol{\beta}_{1}+\boldsymbol{\beta}_{2}=\boldsymbol{\beta}_{3}</equation>，故<equation>r(A)\leqslant 2</equation>.又因为<equation>\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2}</equation>线性无关，所以<equation>r(A)\geqslant 2</equation>.因此，<equation>r(A)=2.</equation>

---

**2012年第13题 | 填空题 | 4分**
13. 设<equation>\alpha</equation>为 3 维单位列向量,<equation>E</equation>为 3 阶单位矩阵, 则矩阵<equation>E - \alpha \alpha^{\mathrm{T}}</equation>的秩为 ___
**解析: **解 由于<equation>\boldsymbol{\alpha}</equation>为3维单位列向量，故<equation>\boldsymbol{\alpha}^{\mathrm{T}}\boldsymbol{\alpha}=\| \boldsymbol{\alpha}\|^{2}=1</equation>，从而<equation>(\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}})\boldsymbol{\alpha}=\boldsymbol{\alpha}(\boldsymbol{\alpha}^{\mathrm{T}}\boldsymbol{\alpha})=\boldsymbol{\alpha}</equation>，于是1为矩阵<equation>\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}}</equation>的非零特征值.又<equation>r(\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}})\leqslant r(\boldsymbol{\alpha})\leqslant1</equation>且<equation>\boldsymbol{\alpha}</equation>为非零向量，故<equation>r(\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}})=1</equation>，再由<equation>\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}}</equation>为实对称矩阵知，存在正交矩阵<equation>Q</equation>，使得<equation>Q^{-1}\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}}Q=\left( \begin{array}{c c c} 1 & & \\ & 0 & \\ & & 0 \end{array} \right)</equation>.于是<equation>Q ^ {- 1} \left(E - \alpha \alpha^ {\mathrm {T}}\right) Q = E - \left( \begin{array}{c c c} 1 & & \\ & 0 & \\ & & 0 \end{array} \right) = \left( \begin{array}{c c c} 0 & & \\ & 1 & \\ & & 1 \end{array} \right).</equation>因此，<equation>r(\boldsymbol{E} - \boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}}) = 2.</equation>

---

**2010年第5题 | 选择题 | 4分 | 答案: A**
5. 设 A为<equation>m \times n</equation>矩阵，B为<equation>n \times m</equation>矩阵，E为m阶单位矩阵，若<equation>A B=E</equation>，则（    )

A. 秩<equation>r ( A )=m</equation>，秩<equation>r ( B )=m</equation>B. 秩<equation>r ( A )=m</equation>，秩<equation>r ( B )=n</equation>C. 秩<equation>r ( A )=n</equation>，秩<equation>r ( B )=m</equation>D. 秩<equation>r ( A )=n</equation>，秩<equation>r ( B )=n</equation>
答案: A
**解析: **（法一）由于<equation>m = r (\boldsymbol {E}) = r (\boldsymbol {A B}) \leqslant r (\boldsymbol {A}) \leqslant \min \{m, n \} \leqslant m,</equation><equation>m = r (\boldsymbol {E}) = r (\boldsymbol {A B}) \leqslant r (\boldsymbol {B}) \leqslant \min \{m, n \} \leqslant m,</equation>故<equation>r(\mathbf{A})=m,r(\mathbf{B})=m.</equation>应选A.

（法二）由<equation>AB=E</equation>知，B是矩阵方程<equation>AX=E</equation>的解.又矩阵方程<equation>AX=E</equation>有解的充要条件是秩<equation>r(A)=r(A,E)</equation>，故<equation>r (\boldsymbol {A}) = r (\boldsymbol {A}, \boldsymbol {E}) = m.</equation>同理由<equation>\mathbf{B}^{\mathrm{T}}\mathbf{A}^{\mathrm{T}}=\mathbf{E}^{\mathrm{T}}=\mathbf{E}</equation>知，<equation>r(\mathbf{B}^{\mathrm{T}})=r(\mathbf{B}^{\mathrm{T}},\mathbf{E})=m</equation>从而<equation>r(\mathbf{B})=r(\mathbf{B}^{\mathrm{T}})=m.</equation>应选A.

（法三）由于<equation>m=r(\mathbf{A B})\leqslant r(\mathbf{A})\leqslant n</equation>，故取<equation>m=1,n=2,\mathbf{A}=(1,0),\mathbf{B}=(1,0)^{\mathrm{T}}</equation>满足AB<equation>= E</equation>，此时<equation>r(\mathbf{A})=r(\mathbf{B})=1.</equation>由排除法可知，应选A.

---


