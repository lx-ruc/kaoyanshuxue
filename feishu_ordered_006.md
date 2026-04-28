# 数学一

## 线性代数

### 矩阵

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


#### 矩阵的运算与变换

**2022年第15题 | 填空题 | 5分**

15. 已知矩阵 A和 E-A可逆，其中 E为单位矩阵，若矩阵 B满足<equation>[ E-( E-A)^{-1} ] B=A</equation>，则 B-A=___

**答案:**<equation>- E.</equation>

**解析:**解（法一）在<equation>[E - (E - A)^{-1}]B = A</equation>两端同时左乘<equation>E - A</equation>，可得<equation>[ \boldsymbol {E} - \boldsymbol {A} - (\boldsymbol {E} - \boldsymbol {A}) (\boldsymbol {E} - \boldsymbol {A}) ^ {- 1} ] \boldsymbol {B} = (\boldsymbol {E} - \boldsymbol {A}) \boldsymbol {A}.</equation>展开整理，可得<equation>- AB=A-A^{2}.</equation>由于<equation>A</equation>可逆，故上式两端同时左乘<equation>A^{-1}</equation>可得<equation>-B = E - A</equation>，即<equation>B - A = -E</equation>（法二）注意到<equation>[E - (E - A)^{-1}](E - A) = E - A - E = -A</equation>，故由A可逆可得，<equation>[E - (E - A)^{-1}](E - A)(-A^{-1}) = E</equation>即<equation>[E - (E - A)^{-1}](E - A^{-1}) = E.</equation>于是，<equation>E - (E - A)^{-1}</equation>与<equation>E - A^{-1}</equation>互为逆矩阵.

在<equation>[E - (E - A)^{-1}]B = A</equation>两端同时左乘<equation>E - A^{-1}</equation>，可得<equation>B = (E - A^{-1})A = A - E.</equation>因此，<equation>B - A = -E.</equation>

---

**2020年第5题 | 选择题 | 4分 | 答案: B**

5. 若矩阵 A经过初等列变换化成 B，则（    ）

A. 存在矩阵 P，使得<equation>P A=B</equation>B. 存在矩阵 P，使得<equation>B P=A</equation>C. 存在矩阵 P，使得<equation>P B=A</equation>D. 方程组<equation>A x=0</equation>与<equation>B x=0</equation>同解

答案: B

**解析:**解 若矩阵 A经过初等列变换化成 B，则存在初等矩阵<equation>Q_{1}, Q_{2}, \dots , Q_{n}</equation>，使得<equation>A Q_{1} Q_{2}\cdots Q_{n}=B.</equation>令<equation>Q=Q_{1} Q_{2}\cdots Q_{n}</equation>，则 Q为可逆矩阵，且<equation>A Q=B.</equation>令 P=<equation>Q^{-1}</equation>，则 BP=A.

因此，应选B.

若矩阵 A经过初等行变换化成 B，则选项 A、C、D正确.

---

**2012年第6题 | 选择题 | 4分 | 答案: B**

6. 设 A为3阶矩阵，P为3阶可逆矩阵，且<equation>P^{-1} A P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>若<equation>P=(\alpha_{1},\alpha_{2},\alpha_{3})</equation><equation>Q=(\alpha_{1}+\alpha_{2},\alpha_{2},\alpha_{3})</equation>，则<equation>Q ^ {- 1} A Q = (\quad)</equation>A.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>

答案: B

**解析:**解（法一）由题设知，<equation>Q=P\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，故<equation>Q^{-1}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) P^{-1}</equation>. 从而<equation>\begin{aligned} Q ^ {- 1} A Q &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 0 & 0 & 1  \right) P ^ {- 1} A P \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1  \right) \\ &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 0 & 0 & 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1  \right) &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2  \right). \end{aligned}</equation>应选B.

（法二）由题设知，1，1，2是<equation>\boldsymbol{A}</equation>的特征值，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>分别是属于特征值1，1，2的特征向量，即<equation>A \alpha_ {1} = \alpha_ {1}, \quad A \alpha_ {2} = \alpha_ {2}, \quad A \alpha_ {3} = 2 \alpha_ {3}.</equation>从而<equation>A\left(\alpha_{1} + \alpha_{2}\right) = \alpha_{1} + \alpha_{2},\alpha_{1} + \alpha_{2}</equation>也是<equation>A</equation>的属于特征值1的特征向量.<equation>A Q = A \left(\alpha_ {1} + \alpha_ {2}, \alpha_ {2}, \alpha_ {3}\right) = \left(\alpha_ {1} + \alpha_ {2}, \alpha_ {2}, 2 \alpha_ {3}\right) = Q \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>又由于<equation>Q</equation>由<equation>P</equation>作初等变换得到，<equation>P</equation>可逆，故<equation>Q</equation>可逆.于是<equation>Q^{-1}AQ=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>应选B.

---

**2011年第5题 | 选择题 | 4分 | 答案: D**

5. 设 A为3阶矩阵，将 A的第2列加到第1列得矩阵 B，再交换 B的第2行与第3行得单位矩阵.记<equation>\boldsymbol {P} _ {1} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right), \boldsymbol {P} _ {2} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{array} \right), \mathrm {则} \boldsymbol {A} = (\quad)</equation>A.<equation>P_{1} P_{2}</equation>B.<equation>P_{1}^{-1} P_{2}</equation>C.<equation>P_{2} P_{1}</equation>D.<equation>P_{2} P_{1}^{-1}</equation>

答案: D

**解析:**解 将 A的第2列加到第1列对应 A右乘矩阵<equation>P_{1}</equation>，得<equation>B=A P_{1}</equation>.交换 B的第2行与第3行对应 B左乘矩阵<equation>P_{2}</equation>，得<equation>E=P_{2} A P_{1}</equation>.于是<equation>A=P_{2}^{-1} P_{1}^{-1}.</equation>又因为<equation>P_{2}^{-1}=P_{2}</equation>，所以<equation>A=P_{2} P_{1}^{-1}</equation>.应选 D.

---


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

