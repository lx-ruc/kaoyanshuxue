#### 矩阵的运算与变换

**2025年第9题 | 选择题 | 5分 | 答案: B**
9. 下列矩阵中，可以经过若干初等行变换得到矩阵<equation>\left( \begin{array}{c c c c} 1 & 1 & 0 & 1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{array} \right)</equation>的是（    ）

A.

B.<equation>\left( \begin{array}{c c c c} 1 & 1 & 0 & 1 \\ 1 & 2 & 1 & 3 \\ 2 & 3 & 1 & 4 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c c} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 3 \\ 0 & 0 & 0 & 0 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c c} 1 & 1 & 2 & 3 \\ 1 & 2 & 2 & 3 \\ 2 & 3 & 4 & 6 \end{array} \right)</equation>
答案: B
**解析: **解（法一）由于对矩阵做初等行变换不改变矩阵的列向量组的线性相关性，且注意到矩阵<equation>\left( \begin{array}{c c c c} 1 & 1 & 0 & 1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{array} \right)</equation>的第一列与第二列线性相关，而除了选项B中<equation>\left( \begin{array}{c c c c} 1 & 1 & 0 & 1 \\ 1 & 1 & 2 & 5 \\ 1 & 1 & 1 & 3 \end{array} \right)</equation>的第一列与第二列线性相关外，其余选项的第一列与第二列均线性无关，故可以排除选项A、C、D.

由排除法可知，应选B.

（法二）依次分析各选项.<equation>\left( \begin{array}{c c c c} 1 & 1 & 0 & 1 \\ 1 & 2 & 1 & 3 \\ 2 & 3 & 1 & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & 0 & 1 \\ 0 & 1 & 1 & 2 \\ 0 & 1 & 1 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & 0 & 1 \\ 0 & 1 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{array} \right).</equation>对选项A，

由此可得，选项A不正确.

对选项B，<equation>\left( \begin{array}{c c c c} 1 & 1 & 0 & 1 \\ 1 & 1 & 2 & 5 \\ 1 & 1 & 1 & 3 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & 0 & 1 \\ 0 & 0 & 2 & 4 \\ 0 & 0 & 1 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & 0 & 1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{array} \right).</equation>由此可得，选项B正确.

注意到选项C的矩阵<equation>\left( \begin{array}{c c c c} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 3 \\ 0 & 1 & 0 & 0 \end{array} \right)</equation>有3阶非零子式<equation>\left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 1 & 0 \end{array} \right)</equation>，故该矩阵的秩为3，不可能与矩阵<equation>\left( \begin{array}{c c c c} 1 & 1 & 0 & 1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{array} \right)</equation>行等价.由此可得，选项C不正确.

对选项D，<equation>\left( \begin{array}{c c c c} 1 & 1 & 2 & 3 \\ 1 & 2 & 2 & 3 \\ 2 & 3 & 4 & 6 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & 2 & 3 \\ 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 0 & 2 & 3 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{array} \right).</equation>由此可得，选项D不正确.

因此，应选B.

---

**2024年第8题 | 选择题 | 5分 | 答案: C**
8. 设 A为3阶矩阵，<equation>P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right)</equation>，若<equation>P^{\mathrm{T}} A P^{2}=\left( \begin{array}{c c c} a+2 c & 0 & c \\ 0 & b & 0 \\ 2 c & 0 & c \end{array} \right)</equation>，则 A=（    )

A.<equation>\left( \begin{array}{c c c} c & 0 & 0 \\ 0 & a & 0 \\ 0 & 0 & b \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c} b & 0 & 0 \\ 0 & c & 0 \\ 0 & 0 & a \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c} a & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & c \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} c & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & a \end{array} \right)</equation>
答案: C
**解析: **解 由于<equation>P = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right)</equation>，故<equation>\boldsymbol {P} ^ {- 1} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ - 1 & 0 & 1 \end{array} \right), \quad \boldsymbol {P} ^ {\mathrm {T}} = \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right), \quad \left(\boldsymbol {P} ^ {\mathrm {T}}\right) ^ {- 1} = \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>进一步可得，<equation>\begin{aligned} \boldsymbol {A} &= \left(\boldsymbol {P} ^ {\mathrm {T}}\right) ^ {- 1} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} ^ {2} \left(\boldsymbol {P} ^ {2}\right) ^ {- 1} = \left(\boldsymbol {P} ^ {\mathrm {T}}\right) ^ {- 1} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} ^ {2} \left(\boldsymbol {P} ^ {- 1}\right) ^ {2} \\ &= \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1  \right) \left( \begin{array}{c c c} a + 2 c & 0 & c \\ 0 & b & 0 \\ 2 c & 0 & c  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ - 1 & 0 & 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ - 1 & 0 & 1  \right) \\ &= \left( \begin{array}{c c c} a & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & c  \right). \end{aligned}</equation>因此，应选C.

---

**2022年第16题 | 填空题 | 5分**
16. 设 A为3阶矩阵，交换 A的第2行和第3行，再将第2列的-1倍加到第1列，得到矩阵<equation>A^{-1}</equation>的迹<equation>\operatorname{tr}\left(A^{-1}\right)=</equation>___
**答案: **-1.
**解析: **解 交换第2行和第3行对应左乘初等矩阵<equation>P_{1}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{array} \right)</equation>，将第2列的-1倍加到第1列对应右乘初等矩阵<equation>P_{2}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>.记<equation>B=\left( \begin{array}{c c c} -2 & 1 & -1 \\ 1 & -1 & 0 \\ -1 & 0 & 0 \end{array} \right)</equation>.于是，<equation>P_{1}AP_{2}=B</equation>，从而<equation>A= P_{1}^{-1}BP_{2}^{-1}</equation>.由此可得，<equation>A^{-1}=P_{2}B^{-1}P_{1}.</equation>下面利用初等行变换计算<equation>B^{-1}.</equation><equation>\begin{array}{l} (\boldsymbol {B}, \boldsymbol {E}) = \left( \begin{array}{c c c c c c} - 2 & 1 & - 1 & 1 & 0 & 0 \\ 1 & - 1 & 0 & 0 & 1 & 0 \\ - 1 & 0 & 0 & 0 & 0 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 0 & 0 & - 1 \\ 1 & - 1 & 0 & 0 & 1 & 0 \\ - 2 & 1 & - 1 & 1 & 0 & 0 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 0 & 0 & - 1 \\ 0 & - 1 & 0 & 0 & 1 & 1 \\ 0 & 1 & - 1 & 1 & 0 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 0 & 0 & - 1 \\ 0 & - 1 & 0 & 0 & 1 & 1 \\ 0 & 0 & - 1 & 1 & 1 & - 1 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 0 & 0 & - 1 \\ 0 & 1 & 0 & 0 & - 1 & - 1 \\ 0 & 0 & 1 & - 1 & - 1 & 1 \end{array} \right). \\ \end{array}</equation>于是，<equation>B^{-1}=\left( \begin{array}{c c c} 0 & 0 & -1 \\ 0 & -1 & -1 \\ -1 & -1 & 1 \end{array} \right).</equation>因此，<equation>\boldsymbol {A} ^ {- 1} = \boldsymbol {P} _ {2} \boldsymbol {B} ^ {- 1} \boldsymbol {P} _ {1} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \left( \begin{array}{c c c} 0 & 0 & - 1 \\ 0 & - 1 & - 1 \\ - 1 & - 1 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{array} \right) = \left( \begin{array}{c c c} 0 & - 1 & 0 \\ 0 & 0 & - 1 \\ - 1 & 1 & - 1 \end{array} \right).</equation>进一步可得<equation>\operatorname{tr}(A^{-1}) = -1.</equation>

---

**2021年第10题 | 选择题 | 5分 | 答案: C**
10. 已知矩阵<equation>A=\left( \begin{array}{c c c}1&0&-1\\ 2&-1&1\\ -1&2&-5 \end{array} \right)</equation>，若存在下三角可逆矩阵 P与上三角可逆矩阵 Q，使得 PAQ为对角矩阵，则

P和Q分别为（    ）

A.<equation>\begin{array}{l} \left. \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right), \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right) \right. \\ \left(\left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right), \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right) \right. \\ \end{array}</equation>B.

C.<equation>\begin{array}{l} \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right), \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \\ \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 3 & 1 \end{array} \right), \left( \begin{array}{c c c} 1 & 2 & - 3 \\ 0 & - 1 & 2 \\ 0 & 0 & 1 \end{array} \right) \\ \end{array}</equation>D.
答案: C
**解析: **解（法一）对（A，E）作初等行变换.<equation>\begin{array}{l} (A, E) = \left( \begin{array}{c c c c c c} 1 & 0 & - 1 & 1 & 0 & 0 \\ 2 & - 1 & 1 & 0 & 1 & 0 \\ - 1 & 2 & - 5 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {2} - 2 r _ {1}} \left( \begin{array}{c c c c c c} 1 & 0 & - 1 & 1 & 0 & 0 \\ 0 & - 1 & 3 & - 2 & 1 & 0 \\ 0 & 2 & - 6 & 1 & 0 & 1 \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} \times (- 1)} \left( \begin{array}{c c c c c c} 1 & 0 & - 1 & 1 & 0 & 0 \\ 0 & 1 & - 3 & 2 & - 1 & 0 \\ 0 & 2 & - 6 & 1 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} ^ {*} - 2 r _ {2} ^ {* *}} \left( \begin{array}{c c c c c c} 1 & 0 & - 1 & 1 & 0 & 0 \\ 0 & 1 & - 3 & 2 & - 1 & 0 \\ 0 & 0 & 0 & - 3 & 2 & 1 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个 *.）

取<equation>P = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & -1 & 0 \\ -3 & 2 & 1 \end{array} \right).</equation>记<equation>U=\left( \begin{array}{c c c}1&0&-1\\ 0&1&-3\\ 0&0&0 \end{array} \right)</equation>，对<equation>\binom{U}{E}</equation>作初等列变换.<equation>\binom {U} {E} = \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & - 3 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow {c _ {3} + c _ {1} + 3 c _ {2}} \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right).</equation>取<equation>Q = \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right).</equation>此时，PAQ =<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>为对角矩阵.因此，应选C.

（法二）代人法.

观察选项A、B发现，其中各有一个单位矩阵。

由于左乘矩阵相当于对原矩阵作行变换，右乘矩阵相当于对原矩阵作列变换，故<equation>\boldsymbol {A} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 2 & - 1 & 1 \\ - 1 & 2 & - 5 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right)</equation>的第一列为 A的第一列，即<equation>\left( \begin{array}{c c c} 1 \\ 2 \\ - 1 \end{array} \right),</equation><equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right) A = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 2 & - 1 & 1 \\ - 1 & 2 & - 5 \end{array} \right)</equation>的第一行为 A的第一行，即（1，0，-1），而任何矩阵与单位矩阵相乘所得结果均为原矩阵，于是选项A、B所给 P，Q均不能使得 PAQ为对角矩阵。由此可排除选项A、B.

将选项C中的两个矩阵代入计算，可得<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 2 & - 1 & 1 \\ - 1 & 2 & - 5 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 1 & 2 & 0 \end{array} \right) = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>由此可见选项C正确. 应选C.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 3 & 1 \end{array} \right) A</equation>的第一行、第二行与A的第一行、第二行相同，即<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 3 & 1 \end{array} \right) A=\left( \begin{array}{c c c} 1 & 0 & -1 \\ 2 & -1 & 1 \\ * & * & * \end{array} \right),</equation>记为B.B再右乘<equation>\left( \begin{array}{c c c} 1 & 2 & -3 \\ 0 & -1 & 2 \\ 0 & 0 & 1 \end{array} \right),</equation>则新矩阵的第一列为<equation>\left( \begin{array}{c} 1 \\ 2 \\ * \end{array} \right).</equation>于是，所得结果不是对角矩阵.

---

**2015年第22题 | 解答题 | 11分**
22. (本题满分11分)

设矩阵<equation>A=\left( \begin{array}{c c c} a & 1 & 0 \\ 1 & a & -1 \\ 0 & 1 & a \end{array} \right)</equation>，且<equation>A^{3}=O.</equation>I. 求 a的值；

II. 若矩阵<equation>X</equation>满足<equation>X - XA^{2} - AX + AXA^{2} = E</equation>，其中<equation>E</equation>为3阶单位矩阵，求<equation>X</equation>
**答案: **(22) （I）<equation>a=0;</equation><equation>(\mathrm {I I}) X = \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1 \end{array} \right)</equation>
**解析: **解（I）（法一）由<equation>A^{3}=O</equation>知<equation>|A^{3}|=0.</equation>又因为<equation>|A^{3}|=|A|^{3},</equation>所以<equation>|A|=0.</equation>由题设可计算得<equation>|A|=a^{3},</equation>从而<equation>a^{3}=0, a=0.</equation>（法二）设<equation>\lambda</equation>为<equation>A</equation>的一个特征值，则由<equation>A^{3}=O</equation>可知<equation>\lambda^{3}=0</equation>.于是，<equation>A</equation>的特征值均为零。由矩阵的迹等于其特征值之和，可知<equation>\operatorname{tr}(A)=3 a=0</equation>即<equation>a=0.</equation>（Ⅱ）由第（I）问知，<equation>A=\left( \begin{array}{c c c} 0 & 1 & 0 \\ 1 & 0 & -1 \\ 0 & 1 & 0 \end{array} \right).</equation>由<equation>X - X A^{2} - A X + A X A^{2} = E</equation>可得，<equation>X \left(E - A ^ {2}\right) - A X \left(E - A ^ {2}\right) = E.</equation>化简得（E-A）X（E-A²）=E.

由此可知，<equation>E - A, E - A^{2}</equation>均为可逆矩阵，且<equation>\boldsymbol {X} = \left(\boldsymbol {E} - \boldsymbol {A}\right) ^ {- 1} \left(\boldsymbol {E} - \boldsymbol {A} ^ {2}\right) ^ {- 1}.</equation>下面用三种方法计算 X.

（法一）由<equation>(AB)^{-1} = B^{-1}A^{-1}</equation>得，<equation>X = \left(E - A\right) ^ {- 1} \left(E - A ^ {2}\right) ^ {- 1} = \left[ \left(E - A ^ {2}\right) \left(E - A\right) \right] ^ {- 1} \xlongequal {A ^ {3} = O} \left(E - A - A ^ {2}\right) ^ {- 1}.</equation>计算得<equation>A^{2} = \left( \begin{array}{c c c} 1 & 0 & -1 \\ 0 & 0 & 0 \\ 1 & 0 & -1 \end{array} \right)</equation>，故<equation>E - A - A^{2} = \left( \begin{array}{c c c} 0 & -1 & 1 \\ -1 & 1 & 1 \\ -1 & -1 & 2 \end{array} \right)</equation>，再计算得<equation>|E - A - A^{2}| = 1.</equation>因此，<equation>\boldsymbol {X} = \left(\boldsymbol {E} - \boldsymbol {A} - \boldsymbol {A} ^ {2}\right) ^ {- 1} = \left(\boldsymbol {E} - \boldsymbol {A} - \boldsymbol {A} ^ {2}\right) ^ {*} = \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1 \end{array} \right).</equation>或利用初等变换法计算 X.<equation>\begin{array}{l} \left(\boldsymbol {E} - \boldsymbol {A} - \boldsymbol {A} ^ {2}, \boldsymbol {E}\right) = \left( \begin{array}{c c c c c c} 0 & - 1 & 1 & 1 & 0 & 0 \\ - 1 & 1 & 1 & 0 & 1 & 0 \\ - 1 & - 1 & 2 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {2} + r _ {1}} \left( \begin{array}{c c c c c c} 0 & - 1 & 1 & 1 & 0 & 0 \\ - 1 & 0 & 2 & 1 & 1 & 0 \\ 0 & - 1 & 0 & - 1 & - 1 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} - r _ {3} ^ {*}} \binom {0} {r _ {2} ^ {*} - 2 r _ {1} ^ {*}} \rightarrow \binom {1} {0} \binom {0} {1} \binom {3} {0} \binom {1} {- 2} \\ \end{array}</equation>因此，<equation>\boldsymbol {X} = \left(\boldsymbol {E} - \boldsymbol {A} - \boldsymbol {A} ^ {2}\right) ^ {- 1} = \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1 \end{array} \right).</equation>（法二）由于<equation>A^{3} = O</equation>，故<equation>A^{4} = O</equation>，从而<equation>\left(E - A\right) \left(E + A + A ^ {2}\right) = E - A ^ {3} = E, \quad \left(E - A ^ {2}\right) \left(E + A ^ {2}\right) = E - A ^ {4} = E.</equation>于是，<equation>(E - A)^{-1} = E + A + A^{2},(E - A^{2})^{-1} = E + A^{2}</equation>因此，<equation>\begin{aligned} \boldsymbol {X} &= \left(\boldsymbol {E} - \boldsymbol {A}\right) ^ {- 1} \left(\boldsymbol {E} - \boldsymbol {A} ^ {2}\right) ^ {- 1} = \left(\boldsymbol {E} + \boldsymbol {A} + \boldsymbol {A} ^ {2}\right) \left(\boldsymbol {E} + \boldsymbol {A} ^ {2}\right) \stackrel {A ^ {3} = O} {=} \boldsymbol {E} + \boldsymbol {A} + 2 \boldsymbol {A} ^ {2} \\ &= \boldsymbol {E} + \left( \begin{array}{c c c} 0 & 1 & 0 \\ 1 & 0 & - 1 \\ 0 & 1 & 0  \right) + 2 \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 0 & 0 \\ 1 & 0 & - 1  \right) &= \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1  \right). \end{aligned}</equation>（法三）分别计算<equation>(E - A)^{-1}, (E - A^{2})^{-1}</equation>.<equation>\boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} 1 & - 1 & 0 \\ - 1 & 1 & 1 \\ 0 & - 1 & 1 \end{array} \right), \quad \boldsymbol {E} - \boldsymbol {A} ^ {2} = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 1 & 0 \\ - 1 & 0 & 2 \end{array} \right).</equation>利用初等变换法计算<equation>(E - A)^{-1}, (E - A^{2})^{-1}</equation>.<equation>\begin{array}{l} (E - A, E) = \left( \begin{array}{c c c c c c} 1 & - 1 & 0 & 1 & 0 & 0 \\ - 1 & 1 & 1 & 0 & 1 & 0 \\ 0 & - 1 & 1 & 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {3} - r _ {2} ^ {*} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c c c} 1 & - 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 & 1 & 0 \\ 0 & - 1 & 0 & - 1 & - 1 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} - r _ {3} ^ {*}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 2 & 1 & - 1 \\ 0 & 0 & 1 & 1 & 1 & 0 \\ 0 & - 1 & 0 & - 1 & - 1 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 2 & 1 & - 1 \\ 0 & 1 & 0 & 1 & 1 & - 1 \\ 0 & 0 & 1 & 1 & 1 & 0 \end{array} \right), \\ \end{array}</equation><equation>\begin{array}{l} \left(\boldsymbol {E} - \boldsymbol {A} ^ {2}, \boldsymbol {E}\right) = \left( \begin{array}{c c c c c c} 0 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ - 1 & 0 & 2 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} - 2 r _ {1}} \left( \begin{array}{c c c c c c} 0 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ - 1 & 0 & 0 & - 2 & 0 & 1 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 2 & 0 & - 1 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 1 & 0 & 0 \end{array} \right). \\ \end{array}</equation>因此，<equation>\left(\boldsymbol {E} - \boldsymbol {A}\right) ^ {- 1} = \left( \begin{array}{c c c} 2 & 1 & - 1 \\ 1 & 1 & - 1 \\ 1 & 1 & 0 \end{array} \right), \quad \left(\boldsymbol {E} ^ {-} - \boldsymbol {A} ^ {2}\right) ^ {- 1} = \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{array} \right).</equation>综上所述，<equation>\boldsymbol {X} = \left(\boldsymbol {E} - \boldsymbol {A}\right) ^ {- 1} \left(\boldsymbol {E} - \boldsymbol {A} ^ {2}\right) ^ {- 1} = \left( \begin{array}{c c c} 2 & 1 & - 1 \\ 1 & 1 & - 1 \\ 1 & 1 & 0 \end{array} \right) \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{array} \right) = \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1 \end{array} \right).</equation>

---

**2012年第8题 | 选择题 | 4分 | 答案: B**
8. 设 A为3阶矩阵，P为3阶可逆矩阵，且<equation>P^{-1} A P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>若<equation>P=(\alpha_{1},\alpha_{2},\alpha_{3}), Q=(\alpha_{1}+\alpha_{2},\alpha_{2},\alpha_{3}),</equation>则<equation>Q^{-1} A Q=</equation>(    )

A.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>
答案: B
**解析: **解（法一）由题设知，<equation>Q=P\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，故<equation>Q^{-1}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) P^{-1}</equation>. 从而<equation>\begin{aligned} Q ^ {- 1} A Q &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 0 & 0 & 1  \right) P ^ {- 1} A P \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1  \right) \\ &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 0 & 0 & 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1  \right) &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2  \right). \end{aligned}</equation>应选B.

（法二）由题设知，1，1，2是A的特征值，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>分别是属于特征值1，1，2的特征向量，即<equation>A\alpha_{1}=\alpha_{1},</equation><equation>A\alpha_{2}=\alpha_{2},</equation><equation>A\alpha_{3}=2\alpha_{3}.</equation>从而<equation>A\left(\alpha_{1} + \alpha_{2}\right) = \alpha_{1} + \alpha_{2},\alpha_{1} + \alpha_{2}</equation>也是<equation>A</equation>的属于特征值1的特征向量.<equation>A Q = A \left(\alpha_ {1} + \alpha_ {2}, \alpha_ {2}, \alpha_ {3}\right) = \left(\alpha_ {1} + \alpha_ {2}, \alpha_ {2}, 2 \alpha_ {3}\right) = Q \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>又由于<equation>Q</equation>由<equation>P</equation>作初等变换得到，<equation>P</equation>可逆，故<equation>Q</equation>可逆.于是<equation>Q^{-1}AQ = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>.应选B.

---

**2011年第7题 | 选择题 | 4分 | 答案: D**
7. 设 A为3阶矩阵，将 A的第2列加到第1列得矩阵 B，再交换 B的第2行与第3行得单位矩阵.记<equation>P_{1}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right), P_{2}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{array} \right),</equation>则 A=（    )

A.<equation>P_{1} P_{2}</equation>B.<equation>P_{1}^{-1} P_{2}</equation>C.<equation>P_{2} P_{1}</equation>D.<equation>P_{2} P_{1}^{-1}</equation>
答案: D
**解析: **解 将 A的第2列加到第1列对应 A右乘矩阵<equation>P_{1}</equation>，得<equation>B=A P_{1}</equation>.交换 B的第2行与第3行对应 B左乘矩阵<equation>P_{2}</equation>，得<equation>E=P_{2} A P_{1}</equation>.于是<equation>A=P_{2}^{-1} P_{1}^{-1}.</equation>又因为<equation>P_{2}^{-1}=P_{2}</equation>，所以 A=P<equation>P_{2}^{-1}.</equation>应选 D.

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


