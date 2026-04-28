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


