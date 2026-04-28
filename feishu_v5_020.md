---


### 矩阵

#### 矩阵的运算与变换


**2024年第6题 | 选择题 | 5分 | 答案: C**

6. 设 A为3阶矩阵，<equation>P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right)</equation>，若<equation>P^{\mathrm{T}} A P^{2}=\left( \begin{array}{c c c} a+2 c & 0 & c \\ 0 & b & 0 \\ 2 c & 0 & c \end{array} \right)</equation>，则 A=（    )

A.<equation>\left( \begin{array}{c c c} c & 0 & 0 \\ 0 & a & 0 \\ 0 & 0 & b \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c} b & 0 & 0 \\ 0 & c & 0 \\ 0 & 0 & a \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c} a & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & c \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} c & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & a \end{array} \right)</equation>

答案: C

**解析:**）由于<equation>P = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right)</equation>，故<equation>\boldsymbol {P} ^ {- 1} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ - 1 & 0 & 1 \end{array} \right), \quad \boldsymbol {P} ^ {\mathrm {T}} = \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right), \quad \left(\boldsymbol {P} ^ {\mathrm {T}}\right) ^ {- 1} = \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>进一步可得，<equation>\begin{aligned} \boldsymbol {A} &= \left(\boldsymbol {P} ^ {\mathrm {T}}\right) ^ {- 1} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} ^ {2} \left(\boldsymbol {P} ^ {2}\right) ^ {- 1} = \left(\boldsymbol {P} ^ {\mathrm {T}}\right) ^ {- 1} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} ^ {2} \left(\boldsymbol {P} ^ {- 1}\right) ^ {2} \\ &= \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1  \right) \left( \begin{array}{c c c} a + 2 c & 0 & c \\ 0 & b & 0 \\ 2 c & 0 & c  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ - 1 & 0 & 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ - 1 & 0 & 1  \right) \\ &= \left( \begin{array}{c c c} a & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & c  \right). \end{aligned}</equation>因此，应选C.

---

**2022年第15题 | 填空题 | 5分**

15. 设 A为3阶矩阵，交换 A的第2行和第3行，再将第2列的-1倍加到第1列，得到矩阵<equation>A^{-1}</equation>的迹<equation>\operatorname{tr}(A^{-1}) =</equation>___

**答案:**-1.

**解析:**解 交换第2行和第3行对应左乘初等矩阵<equation>P_{1}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{array} \right)</equation>，将第2列的-1倍加到第1列对应右乘初等矩阵<equation>P_{2}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>.记<equation>B=\left( \begin{array}{c c c} -2 & 1 & -1 \\ 1 & -1 & 0 \\ -1 & 0 & 0 \end{array} \right)</equation>.于是，<equation>P_{1}AP_{2}=B</equation>，从而<equation>A= P_{1}^{-1}BP_{2}^{-1}</equation>.由此可得，<equation>A^{-1}=P_{2}B^{-1}P_{1}.</equation>下面利用初等行变换计算<equation>B^{-1}.</equation><equation>\begin{array}{l} (B, E) = \left( \begin{array}{c c c c c c} - 2 & 1 & - 1 & 1 & 0 & 0 \\ 1 & - 1 & 0 & 0 & 1 & 0 \\ - 1 & 0 & 0 & 0 & 0 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 0 & 0 & - 1 \\ 1 & - 1 & 0 & 0 & 1 & 0 \\ - 2 & 1 & - 1 & 1 & 0 & 0 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 0 & 0 & - 1 \\ 0 & - 1 & 0 & 0 & 1 & 1 \\ 0 & 1 & - 1 & 1 & 0 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 0 & 0 & - 1 \\ 0 & - 1 & 0 & 0 & 1 & 1 \\ 0 & 0 & - 1 & 1 & 1 & - 1 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 0 & 0 & - 1 \\ 0 & 1 & 0 & 0 & - 1 & - 1 \\ 0 & 0 & 1 & - 1 & - 1 & 1 \end{array} \right). \\ \end{array}</equation>于是，<equation>B^{-1}=\left( \begin{array}{c c c} 0 & 0 & -1 \\ 0 & -1 & -1 \\ -1 & -1 & 1 \end{array} \right).</equation>因此，<equation>\boldsymbol {A} ^ {- 1} = \boldsymbol {P} _ {2} \boldsymbol {B} ^ {- 1} \boldsymbol {P} _ {1} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \left( \begin{array}{c c c} 0 & 0 & - 1 \\ 0 & - 1 & - 1 \\ - 1 & - 1 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{array} \right) = \left( \begin{array}{c c c} 0 & - 1 & 0 \\ 0 & 0 & - 1 \\ - 1 & 1 & - 1 \end{array} \right).</equation>进一步可得<equation>\operatorname{tr}(A^{-1}) = -1.</equation>

---

**2021年第7题 | 选择题 | 5分 | 答案: C**

7. 已知矩阵<equation>A=\left( \begin{array}{c c c}1&0&-1\\ 2&-1&1\\ -1&2&-5 \end{array} \right)</equation>，若存在下三角可逆矩阵 P和上三角可逆矩阵 Q，使 PAQ为对角矩阵，则

P,Q可以分别取（    ）

A.<equation>\begin{array}{l} \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right), \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right) \\ \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right), \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right) \\ \end{array}</equation>C.

B.<equation>\begin{array}{l} \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right), \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \\ \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 3 & 1 \end{array} \right), \left( \begin{array}{c c c} 1 & 2 & - 3 \\ 0 & - 1 & 2 \\ 0 & 0 & 1 \end{array} \right) \\ \end{array}</equation>D.

答案: C

**解析:**解（法一）对（A，E）作初等行变换.<equation>\begin{array}{l} (A, E) = \left( \begin{array}{c c c c c c} 1 & 0 & - 1 & 1 & 0 & 0 \\ 2 & - 1 & 1 & 0 & 1 & 0 \\ - 1 & 2 & - 5 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {2} - 2 r _ {1}} \left( \begin{array}{c c c c c c} 1 & 0 & - 1 & 1 & 0 & 0 \\ 0 & - 1 & 3 & - 2 & 1 & 0 \\ 0 & 2 & - 6 & 1 & 0 & 1 \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} \times (- 1)} \left( \begin{array}{c c c c c c} 1 & 0 & - 1 & 1 & 0 & 0 \\ 0 & 1 & - 3 & 2 & - 1 & 0 \\ 0 & 2 & - 6 & 1 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} ^ {*} - 2 r _ {2} ^ {* *}} \left( \begin{array}{c c c c c c} 1 & 0 & - 1 & 1 & 0 & 0 \\ 0 & 1 & - 3 & 2 & - 1 & 0 \\ 0 & 0 & 0 & - 3 & 2 & 1 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

取<equation>P = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & -1 & 0 \\ -3 & 2 & 1 \end{array} \right).</equation>记<equation>U=\left( \begin{array}{c c c}1&0&-1\\ 0&1&-3\\ 0&0&0 \end{array} \right)</equation>，对<equation>\binom{U}{E}</equation>作初等列变换.<equation>\binom {U} {E} = \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & - 3 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow {c _ {3} + c _ {1} + 3 c _ {2}} \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right).</equation>取<equation>Q = \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right).</equation>此时，PAQ =<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>为对角矩阵.因此，应选C.

（法二）代人法.

观察选项A、B发现，其中各有一个单位矩阵。

由于左乘矩阵相当于对原矩阵作行变换，右乘矩阵相当于对原矩阵作列变换，故<equation>\boldsymbol {A} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 2 & - 1 & 1 \\ - 1 & 2 & - 5 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right)</equation>的第一列为 A的第一列，即<equation>\left( \begin{array}{c}1\\ 2\\ -1 \end{array} \right)</equation><equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right) A = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 2 & - 1 & 1 \\ - 1 & 2 & - 5 \end{array} \right)</equation>的第一行为 A的第一行，即（1，0，-1），而任何矩阵与单位矩阵相乘所得结果均为原矩阵，于是选项A、B所给 P，Q均不能使得 PAQ为对角矩阵。由此可排除选项A、B.

将选项C中的两个矩阵代入计算，可得<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 2 & - 1 & 1 \\ - 1 & 2 & - 5 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 1 & 2 & 0 \end{array} \right) = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>由此可见选项C正确. 应选C.简单计算可验证选项D不正确.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 3 & 1 \end{array} \right) A</equation>的第一行、第二行与A的第一行、第二行相同，即<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 3 & 1 \end{array} \right) A = \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 2 & - 1 & 1 \\ * & * & * \end{array} \right),</equation>记为B.B再右乘<equation>\left( \begin{array}{c c c} 1 & 2 & - 3 \\ 0 & - 1 & 2 \\ 0 & 0 & 1 \end{array} \right),</equation>则新矩阵的第一列为<equation>\left( \begin{array}{c} 1 \\ 2 \\ * \end{array} \right).</equation>于是，所得结果不是对角矩阵.

---

**2015年第20题 | 解答题 | 11分**

20. (本题满分11分)

设矩阵<equation>A=\left( \begin{array}{c c c} a & 1 & 0 \\ 1 & a & -1 \\ 0 & 1 & a \end{array} \right)</equation>，且<equation>A^{3}=O.</equation>I. 求 a的值；

II. 若矩阵<equation>X</equation>满足<equation>X - XA^{2} - AX + AXA^{2} = E</equation>，其中<equation>E</equation>为3阶单位矩阵，求<equation>X</equation>

**答案:**(20) （I）<equation>a=0;</equation><equation>(\mathrm {I I}) \boldsymbol {X} = \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1 \end{array} \right).</equation>

**解析:**解（I）（法一）由<equation>A^{3}=O</equation>知<equation>|A^{3}|=0</equation>又因为<equation>|A^{3}|=|A|^{3}</equation>所以<equation>|A|=0</equation>由题设可计算得<equation>|A|=a^{3}</equation>从而<equation>a^{3}=0</equation>，<equation>a=0.</equation>（法二）设<equation>\lambda</equation>为A的一个特征值，则由<equation>A^{3}=O</equation>可知<equation>\lambda^{3}=0.</equation>于是，A的特征值均为零.由矩阵的迹等于其特征值之和，可知<equation>\operatorname{tr}(A)=3 a=0</equation>即<equation>a=0.</equation>（Ⅱ）由第（I）问知，<equation>A=\left( \begin{array}{c c c} 0 & 1 & 0 \\ 1 & 0 & -1 \\ 0 & 1 & 0 \end{array} \right).</equation>由<equation>X - X A^{2} - A X + A X A^{2} = E</equation>可得，<equation>X \left(E - A ^ {2}\right) - A X \left(E - A ^ {2}\right) = E.</equation>化简得<equation>(E - A)X(E - A^{2}) = E.</equation>由此可知，<equation>E - A, E - A^{2}</equation>均为可逆矩阵，且<equation>\boldsymbol {X} = \left(\boldsymbol {E} - \boldsymbol {A}\right) ^ {- 1} \left(\boldsymbol {E} - \boldsymbol {A} ^ {2}\right) ^ {- 1}.</equation>下面用三种方法计算 X.

（法一）由<equation>(AB)^{-1} = B^{-1}A^{-1}</equation>得，<equation>X = (E - A)^{-1}(E - A^2)^{-1} = [(E - A^2)(E - A)]^{-1}\underline{\underline{A^3 = O}}(E - A - A^2)^{-1}.</equation>计算得<equation>A^{2} = \left( \begin{array}{c c c} 1 & 0 & -1 \\ 0 & 0 & 0 \\ 1 & 0 & -1 \end{array} \right)</equation>，故<equation>E - A - A^{2} = \left( \begin{array}{c c c} 0 & -1 & 1 \\ -1 & 1 & 1 \\ -1 & -1 & 2 \end{array} \right)</equation>，再计算得<equation>|E - A - A^2| = 1.</equation>因此<equation>\boldsymbol {X} = \left(\boldsymbol {E} - \boldsymbol {A} - \boldsymbol {A} ^ {2}\right) ^ {- 1} = \left(\boldsymbol {E} - \boldsymbol {A} - \boldsymbol {A} ^ {2}\right) ^ {*} = \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1 \end{array} \right).</equation>或利用初等变换法计算 X.<equation>\begin{array}{l} \left(\boldsymbol {E} - \boldsymbol {A} - \boldsymbol {A} ^ {2}, \boldsymbol {E}\right) = \left( \begin{array}{c c c c c c} 0 & - 1 & 1 & 1 & 0 & 0 \\ - 1 & 1 & 1 & 0 & 1 & 0 \\ - 1 & - 1 & 2 & 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {3} - r _ {2} ^ {*} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c c c} 0 & - 1 & 1 & 1 & 0 & 0 \\ - 1 & 0 & 2 & 1 & 1 & 0 \\ 0 & - 1 & 0 & - 1 & - 1 & 1 \end{array} \right) \\ \xrightarrow [ r _ {2} ^ {*} - 2 r _ {1} ^ {*} ]{r _ {1} - r _ {3} ^ {*}} \left( \begin{array}{c c c c c c} 0 & 0 & 1 & 2 & 1 & - 1 \\ - 1 & 0 & 0 & - 3 & - 1 & 2 \\ 0 & - 1 & 0 & - 1 & - 1 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 3 & 1 & - 2 \\ 0 & 1 & 0 & 1 & 1 & - 1 \\ 0 & 0 & 1 & 2 & 1 & - 1 \end{array} \right). \\ \end{array}</equation>因此，<equation>\boldsymbol {X} = \left(\boldsymbol {E} - \boldsymbol {A} - \boldsymbol {A} ^ {2}\right) ^ {- 1} = \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1 \end{array} \right).</equation>（法二）由于<equation>A^{3}=O</equation>，故<equation>A^{4}=O</equation>，从而<equation>(E - A)(E + A + A^{2}) = E - A^{3} = E, (E - A^{2})(E + A^{2}) = E - A^{4} = E.</equation>于是，<equation>(E - A)^{-1} = E + A + A^{2}, (E - A^{2})^{-1} = E + A^{2}.</equation>因此，<equation>\begin{aligned} X &= \left(E - A\right) ^ {- 1} \left(E - A ^ {2}\right) ^ {- 1} = \left(E + A + A ^ {2}\right) \left(E + A ^ {2}\right) \xlongequal {A ^ {2} = O} E + A + 2 A ^ {2} \\ &= E + \left( \begin{array}{c c c} 0 & 1 & 0 \\ 1 & 0 & - 1 \\ 0 & 1 & 0  \right) + 2 \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 0 & 0 \\ 1 & 0 & - 1  \right) &= \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1  \right). \end{aligned}</equation>（法三）分别计算<equation>(E - A)^{-1}, (E - A^{2})^{-1}</equation>.<equation>\boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} 1 & - 1 & 0 \\ - 1 & 1 & 1 \\ 0 & - 1 & 1 \end{array} \right), \quad \boldsymbol {E} - \boldsymbol {A} ^ {2} = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 1 & 0 \\ - 1 & 0 & 2 \end{array} \right).</equation>利用初等变换法计算<equation>(E - A)^{-1}, (E - A^{2})^{-1}</equation>.<equation>\begin{array}{l} (E - A, E) = \left( \begin{array}{c c c c c c} 1 & - 1 & 0 & 1 & 0 & 0 \\ - 1 & 1 & 1 & 0 & 1 & 0 \\ 0 & - 1 & 1 & 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {3} - r _ {2} ^ {*} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c c c} 1 & - 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 & 1 & 0 \\ 0 & - 1 & 0 & - 1 & - 1 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} - r _ {3} ^ {*}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 2 & 1 & - 1 \\ 0 & 0 & 1 & 1 & 1 & 0 \\ 0 & - 1 & 0 & - 1 & - 1 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 2 & 1 & - 1 \\ 0 & 1 & 0 & 1 & 1 & - 1 \\ 0 & 0 & 1 & 1 & 1 & 0 \end{array} \right), \\ \end{array}</equation><equation>\begin{array}{l} \left(\boldsymbol {E} - \boldsymbol {A} ^ {2}, \boldsymbol {E}\right) = \left( \begin{array}{c c c c c c} 0 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ - 1 & 0 & 2 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} - 2 r _ {1}} \left( \begin{array}{c c c c c c} 0 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ - 1 & 0 & 0 & - 2 & 0 & 1 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 2 & 0 & - 1 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 1 & 0 & 0 \end{array} \right). \\ \end{array}</equation>因此，<equation>\left(\boldsymbol {E} - \boldsymbol {A}\right) ^ {- 1} = \left( \begin{array}{c c c} 2 & 1 & - 1 \\ 1 & 1 & - 1 \\ 1 & 1 & 0 \end{array} \right), \quad \left(\boldsymbol {E} - \boldsymbol {A} ^ {2}\right) ^ {- 1} = \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{array} \right).</equation>综上所述，<equation>\boldsymbol {X} = \left(\boldsymbol {E} - \boldsymbol {A}\right) ^ {- 1} \left(\boldsymbol {E} - \boldsymbol {A} ^ {2}\right) ^ {- 1} = \left( \begin{array}{c c c} 2 & 1 & - 1 \\ 1 & 1 & - 1 \\ 1 & 1 & 0 \end{array} \right) \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{array} \right) = \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1 \end{array} \right).</equation>

---

**2012年第6题 | 选择题 | 4分 | 答案: B**

6. 设 A为3阶矩阵，P为3阶可逆矩阵，且<equation>P^{-1} A P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>若<equation>P=(\alpha_{1},\alpha_{2},\alpha_{3}), Q=(\alpha_{1}+\alpha_{2},\alpha_{2},\alpha_{3}),</equation>则<equation>Q^{-1} A Q=</equation>(    )

A.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>

答案: B

**解析:**解（法一）由题设知，<equation>Q=P\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，故<equation>Q^{-1}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) P^{-1}</equation>.从而<equation>\begin{aligned} Q ^ {- 1} A Q &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 0 & 0 & 1  \right) P ^ {- 1} A P \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1  \right) \\ &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 0 & 0 & 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1  \right) &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2  \right). \end{aligned}</equation>应选B.

（法二）由题设知，1，1，2是A的特征值，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>分别是属于特征值1，1，2的特征向量，即<equation>A\alpha_{1}=\alpha_{1},</equation><equation>A\alpha_{2}=\alpha_{2},</equation><equation>A\alpha_{3}=2\alpha_{3}.</equation>从而<equation>A\left(\alpha_{1} + \alpha_{2}\right) = \alpha_{1} + \alpha_{2},\alpha_{1} + \alpha_{2}</equation>也是<equation>A</equation>的属于特征值1的一个特征向量.<equation>A Q = A \left(\alpha_ {1} + \alpha_ {2}, \alpha_ {2}, \alpha_ {3}\right) = \left(\alpha_ {1} + \alpha_ {2}, \alpha_ {2}, 2 \alpha_ {3}\right) = Q \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>又由于 Q由 P作初等变换得到，P可逆，故Q可逆.于是<equation>Q^{-1} A Q=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>应选B.

---

**2011年第5题 | 选择题 | 4分 | 答案: D**

5. 设 A为3阶矩阵，将 A的第2列加到第1列得矩阵 B，再交换 B的第2行与第3行得单位矩阵，记<equation>P_{1}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right), P_{2}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{array} \right),</equation>则 A=（    )

A.<equation>P_{1} P_{2}</equation>B.<equation>P_{1}^{-1} P_{2}</equation>C.<equation>P_{2} P_{1}</equation>D.<equation>P_{2} P_{1}^{-1}</equation>

答案: D

**解析:**解 将 A的第2列加到第1列对应 A右乘矩阵<equation>P_{1}</equation>，得<equation>B=A P_{1}</equation>.交换 B的第2行与第3行对应 B左乘矩阵<equation>P_{2}</equation>，得<equation>E=P_{2} A P_{1}</equation>.于是<equation>A=P_{2}^{-1} P_{1}^{-1}.</equation>又因为<equation>P_{2}^{-1}=P_{2}</equation>，所以<equation>A=P_{2} P_{1}^{-1}.</equation>应选 D.

---

**2010年第13题 | 填空题 | 4分**

13. 设<equation>A, B</equation>为3阶矩阵，且<equation>|A| = 3, |B| = 2, |A^{-1} + B| = 2</equation>，则<equation>|A + B^{-1}</equation>

**解析:**由于<equation>A, B</equation>的行列式均不为零，故它们均可逆.因为

所以<equation>\boldsymbol {A} \left(\boldsymbol {A} ^ {- 1} + \boldsymbol {B}\right) \boldsymbol {B} ^ {- 1} = \boldsymbol {B} ^ {- 1} + \boldsymbol {A} = \boldsymbol {A} + \boldsymbol {B} ^ {- 1},</equation><equation>| A + B ^ {- 1} | = | A | \cdot | A ^ {- 1} + B | \cdot | B ^ {- 1} | \frac {| B ^ {- 1} | = \frac {1}{| B |}} {3 \times 2 \times \frac {1}{2}} = 3.</equation>

---

**2009年第6题 | 选择题 | 4分 | 答案: A**

6. 设<equation>A, P</equation>均为3阶矩阵，<equation>P^{\mathrm{T}}</equation>为<equation>P</equation>的转置矩阵，且<equation>P^{\mathrm{T}}AP = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>. 若<equation>P = \left(\alpha_{1}, \alpha_{2}, \alpha_{3}\right)</equation>，<equation>Q = \left(\alpha_{1} + \alpha_{2}, \alpha_{2}, \alpha_{3}\right)</equation>，

则<equation>Q^{\mathrm{T}} A Q</equation>为（    ）

A.<equation>\left( \begin{array}{c c c} 2 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>.<equation>\left( \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>B.

C.<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>

答案: A

**解析:**由题设知，<equation>Q</equation>为把 P的第2列加到第1列的结果，故<equation>Q=P\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>从而<equation>Q^{\mathrm{T}}A Q=\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) P^{\mathrm{T}} A P\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)=\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation><equation>=\left( \begin{array}{c c c} 2 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>应选A.

---


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


#### 矩阵的秩


**2018年第6题 | 选择题 | 4分 | 答案: A**

6. 设 A,B为 n阶矩阵，记 r(X)为矩阵 X的秩，(X,Y)表示分块矩阵，则（    ）

A.<equation>r ( A, A B )=r ( A )</equation>B.<equation>r ( A, B A )=r ( A )</equation>C.<equation>r ( A, B )=\max \{ r ( A ) , r ( B ) \}</equation>D.<equation>r ( A, B )=r \left( A^{\mathrm{T}}, B^{\mathrm{T}} \right)</equation>

答案: A

**解析:**解记 C=AB.由于右乘矩阵表示对矩阵作列变换，故 C的列向量可由 A的列向量线性表示.于是，<equation>r ( A, C )=r ( A, A B )=r ( A ).</equation>因此，应选A.

下面分别说明选项B、C、D不正确.

选项B：<equation>r ( \mathbf{A}, \mathbf{B A})\geqslant r (\mathbf{A})</equation>.但是，<equation>r (\mathbf{A}, \mathbf{B A})=r (\mathbf{A})</equation>并不成立.

取<equation>A = \left( \begin{array}{ll}1 & 0\\ 0 & 0 \end{array} \right),B = \left( \begin{array}{ll}1 & 0\\ 1 & 1 \end{array} \right)</equation>，则<equation>BA = \left( \begin{array}{ll}1 & 0\\ 1 & 0 \end{array} \right),(A,BA) = \left( \begin{array}{lll}1 & 0 & 1 & 0\\ 0 & 0 & 1 & 0 \end{array} \right).r(A,BA) = 2</equation>但<equation>r(A) = 1.</equation>选项C：<equation>r ( A, B ) \geqslant\max \left\{r ( A ) , r ( B ) \right\}</equation>.但是，<equation>r ( A, B )=\max \left\{r ( A ) , r ( B ) \right\}</equation>并不成立.

取<equation>A = \left( \begin{array}{ll}1 & 0\\ 0 & 0 \end{array} \right),B = \left( \begin{array}{ll}0 & 0\\ 1 & 0 \end{array} \right)</equation>，则<equation>(A,B) = \left( \begin{array}{lll}1 & 0 & 0 & 0\\ 0 & 0 & 1 & 0 \end{array} \right),r(A,B) = 2</equation>，但<equation>r(A) = r(B) = 1.</equation>选项D：由于<equation>r(\mathbf{P})=r(\mathbf{P}^{\mathrm{T}})</equation>，而<equation>(\mathbf{A},\mathbf{B})^{\mathrm{T}}=\binom{\mathbf{A}^{\mathrm{T}}}{\mathbf{B}^{\mathrm{T}}}</equation>，故<equation>r(\mathbf{A},\mathbf{B})=r\binom{\mathbf{A}^{\mathrm{T}}}{\mathbf{B}^{\mathrm{T}}}</equation>.但是，<equation>r(\mathbf{A},\mathbf{B})=r(\mathbf{A}^{\mathrm{T}},\mathbf{B}^{\mathrm{T}})</equation>并不成立.

取<equation>A=\left( \begin{array}{ll}1&0\\ 0&0 \end{array} \right), B=\left( \begin{array}{ll}0&0\\ 1&0 \end{array} \right)</equation>，则<equation>(\mathbf{A},\mathbf{B})=\left( \begin{array}{llll}1&0&0&0\\ 0&0&1&0 \end{array} \right),(\mathbf{A}^{\mathrm{T}},\mathbf{B}^{\mathrm{T}})=\left( \begin{array}{llll}1&0&0&1\\ 0&0&0&0 \end{array} \right). r(\mathbf{A},\mathbf{B})=2,</equation>但<equation>r(\mathbf{A}^{\mathrm{T}},\mathbf{B}^{\mathrm{T}})=1.</equation>

---

**2017年第13题 | 填空题 | 4分**

13. 设矩阵<equation>A=\left( \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 2 \\ 0 & 1 & 1 \end{array} \right), \alpha_{1},\alpha_{2},\alpha_{3}</equation>为线性无关的3维列向量组，则向量组<equation>A\alpha_{1},A\alpha_{2},A\alpha_{3}</equation>的秩为 ___.

**解析:**由于<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关，故矩阵<equation>\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)</equation>可逆，从而<equation>r \left(A \alpha_ {1}, A \alpha_ {2}, A \alpha_ {3}\right) = r \left(A \left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right)\right) = r (A).</equation>下面我们用三种方法计算<equation>r(A)</equation>.

（法一）计算<equation>| A |</equation>得<equation>| A |=0</equation>，故<equation>r(A)\leqslant 2</equation>.又因为矩阵 A含有一个非零2阶子式，例如<equation>\left| \begin{array}{ll} 1 & 0 \\ 1 & 1 \end{array} \right|=1</equation>，所以<equation>r(A)\geqslant 2</equation>.因此，<equation>r(A)=2</equation>，从而向量组<equation>A\alpha_{1},A\alpha_{2},A\alpha_{3}</equation>的秩为2.

（法二）对矩阵 A作初等行变换将其化为阶梯形矩阵，进而求得其秩.<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 2 \\ 0 & 1 & 1 \end{array} \right) \xrightarrow {r _ {2} - r _ {1}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 1 & 1 \end{array} \right) \xrightarrow {r _ {3} - r _ {2} ^ {*}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）因此，<equation>r ( A ) = 2.</equation>（法三）令<equation>\boldsymbol{\beta}_{1}=(1,1,0)^{\mathrm{T}}</equation><equation>\boldsymbol{\beta}_{2}=(0,1,1)^{\mathrm{T}}</equation><equation>\boldsymbol{\beta}_{3}=(1,2,1)^{\mathrm{T}}</equation>，则<equation>A=(\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3})</equation>.由于<equation>\boldsymbol{\beta}_{1}+\boldsymbol{\beta}_{2}=</equation><equation>\boldsymbol{\beta}_{3}</equation>，故<equation>r(A)\leqslant 2</equation>.又因为<equation>\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2}</equation>线性无关，所以<equation>r(A)\geqslant 2</equation>.因此，<equation>r(A)=2.</equation>

---


## 概率论与数理统计

### 随机变量的数字特征

#### 协方差与相关系数


**2025年第8题 | 选择题 | 5分 | 答案: D**

8. 设随机变量 X服从正态分布 N(-1,1), Y服从正态分布 N(1,2), 若 X与 X+2Y不相关，则 X与 X-Y的相关系数为（    ）

A.<equation>\frac{1}{3}</equation>B.<equation>\frac{1}{2}</equation>C.<equation>\frac{2}{3}</equation>D.<equation>\frac{3}{4}</equation>

答案: D

**解析:**解 由于 X服从正态分布 N（-1，1），Y服从正态分布 N（1，2），故 D（X）=1，D（Y）=2. 又因为 X与 X+2Y不相关，所以<equation>\operatorname{Cov}(X, X + 2 Y) = \operatorname{Cov}(X, X) + 2 \operatorname{Cov}(X, Y) = D (X) + 2 \operatorname{Cov}(X, Y) = 1 + 2 \operatorname{Cov}(X, Y) = 0.</equation>于是，<equation>\operatorname{Cov}(X, Y) = -\frac{1}{2}.</equation>进一步可得<equation>\operatorname {C o v} (X, X - Y) = \operatorname {C o v} (X, X) - \operatorname {C o v} (X, Y) = D (X) - \operatorname {C o v} (X, Y) = 1 - \left(- \frac {1}{2}\right) = \frac {3}{2}.</equation><equation>D (X - Y) = D (X) + D (Y) - 2 \operatorname {C o v} (X, Y) = 1 + 2 - 2 \cdot \left(- \frac {1}{2}\right) = 4.</equation>因此，X与X-Y的相关系数<equation>\rho = \frac {\operatorname {C o v} (X , X - Y)}{\sqrt {D (X)} \sqrt {D (X - Y)}} = \frac {\frac {3}{2}}{1 \cdot 2} = \frac {3}{4}.</equation>应选 D.

---

**2023年第16题 | 填空题 | 5分**

16. 设随机变量 X 与 Y 相互独立，且<equation>X \sim B ( 1, p )</equation><equation>Y \sim B ( 2, p )</equation><equation>p \in( 0, 1 )</equation>，则<equation>X+Y</equation>与<equation>X-Y</equation>的相关系数为___.

**答案:**<equation>- \frac {1}{3}.</equation>

**解析:**解 由<equation>X\sim B(1,p)</equation>可知，<equation>D ( X )=p ( 1-p ).</equation>由<equation>Y\sim B ( 2,p)</equation>可知，<equation>D ( Y )=2 p ( 1-p ).</equation><equation>X+Y</equation>与<equation>X-Y</equation>的相关系数<equation>\rho=\frac{\operatorname{Cov}(X+Y,X-Y)}{\sqrt{D(X+Y)}\sqrt{D(X-Y)}}.</equation>由于 X与 Y相互独立，故<equation>D (X + Y) = D (X) + D (Y) = 3 p (1 - p),</equation><equation>D (X - Y) = D (X) + D (Y) = 3 p (1 - p).</equation>由协方差的性质可得，<equation>\begin{aligned} \operatorname {C o v} (X + Y, X - Y) &= \operatorname {C o v} (X, X) - \operatorname {C o v} (X, Y) + \operatorname {C o v} (Y, X) - \operatorname {C o v} (Y, Y) \\ &= D (X) - D (Y) = - p (1 - p). \end{aligned}</equation>因此，<equation>\rho = \frac {- p (1 - p)}{\sqrt {3 p (1 - p)} \sqrt {3 p (1 - p)}} = - \frac {1}{3}.</equation>

---

**2022年第8题 | 选择题 | 5分 | 答案: D**

8. 设随机变量<equation>X\sim N(0,4)</equation>，随机变量<equation>Y\sim B\left(3,\frac{1}{3}\right)</equation>，且 X，Y不相关，则<equation>D(X-3Y+1)=</equation>(    )

A.2 B.4 C.6 D.10

答案: D

**解析:**解 由于 X~ N（0,4），Y~ B<equation>\left( 3, \frac{1}{3} \right)</equation>，故 X的方差 D（X）=4，Y的方差<equation>D (Y) = 3 \times \frac {1}{3} \times \left(1 - \frac {1}{3}\right) = \frac {2}{3}.</equation>又因为<equation>X, Y</equation>不相关，所以<equation>\operatorname{Cov}(X, Y) = 0.</equation>由方差的性质，<equation>\begin{aligned} D (X - 3 Y + 1) &= D (X - 3 Y) = D (X) + D (3 Y) - 2 \operatorname {C o v} (X, 3 Y) \\ &= D (X) + 9 D (Y) - 6 \operatorname {C o v} (X, Y) = 4 + 9 \times \frac {2}{3} - 0 = 1 0. \end{aligned}</equation>因此，应选D.

---

**2022年第10题 | 选择题 | 5分 | 答案: B**

10. 设二维随机变量（X，Y）的概率分布为

<table border="1"><tr><td>X\ Y</td><td>0</td><td>1</td><td>2</td></tr><tr><td>-1</td><td>0.1</td><td>0.1</td><td>b</td></tr><tr><td>1</td><td>a</td><td>0.1</td><td>0.1</td></tr></table>

若事件<equation>\{\max \{X,Y\}=2\}</equation>与事件<equation>\{\min \{X,Y\}=1\}</equation>相互独立，则<equation>\operatorname{Cov}(X,Y)=</equation>(    )

A. -0.6 B. -0.36 C. 0 D. 0.48

答案: B

**解析:**解记事件 A = {<equation>\max \{ X, Y \}=2</equation>} ，事件 B = {<equation>\min \{ X, Y \}=1</equation>} .由于事件 A与B相互独立，故 P（AB）=P(A)P(B).

分别计算 P（A），P（B），P（AB）.<equation>P (A) = P \left\{\max \left\{X, Y \right\} = 2 \right\} = P \left\{Y = 2 \right\} = b + 0. 1.</equation><equation>P (B) = P \left\{\min \left\{X, Y \right\} = 1 \right\} = P \left\{X = 1, Y = 1 \right\} + P \left\{X = 1, Y = 2 \right\} = 0. 1 + 0. 1 = 0. 2.</equation><equation>P (A B) = P \left\{\max \left\{X, Y \right\} = 2, \min \left\{X, Y \right\} = 1 \right\} = P \left\{X = 1, Y = 2 \right\} = 0. 1.</equation>于是，<equation>0. 1 = ( b + 0. 1 ) \times 0. 2</equation>，解得 b=0.4. 进一步，由联合分布律中各概率之和为1，即<equation>0. 1 + 0. 1</equation><equation>+ b + a + 0. 1 + 0. 1 = 1</equation>可得，a=0.2.

XY的可能取值为-2，-1，0，1，2.<equation>P \{X Y = - 2 \} = P \{X = - 1, Y = 2 \} = 0. 4.</equation><equation>P \left\{X Y = - 1 \right\} = P \left\{X = - 1, Y = 1 \right\} = 0. 1.</equation><equation>P \{X Y = 1 \} = P \{X = 1, Y = 1 \} = 0. 1.</equation><equation>P \{X Y = 2 \} = P \{X = 1, Y = 2 \} = 0. 1.</equation><equation>P \{X Y = 0 \} = 1 - 0. 4 - 0. 1 - 0. 1 - 0. 1 = 0. 3.</equation>分别计算 E（X），E（Y），E（XY）.<equation>E (X) = - 1 \times (0. 1 + 0. 1 + 0. 4) + 1 \times (0. 2 + 0. 1 + 0. 1) = - 0. 2.</equation><equation>E (Y) = 0 \times (0. 1 + 0. 2) + 1 \times (0. 1 + 0. 1) + 2 \times (0. 4 + 0. 1) = 1. 2.</equation><equation>E (X Y) = (- 2) \times 0. 4 + (- 1) \times 0. 1 + 0 \times 0. 3 + 1 \times 0. 1 + 2 \times 0. 1 = - 0. 6.</equation>因此，<equation>\operatorname {C o v} (X, Y) = E (X Y) - E (X) E (Y) = - 0. 6 - (- 0. 2) \times 1. 2 = - 0. 3 6.</equation>应选B.

---

**2021年第16题 | 填空题 | 5分**

16. 甲，乙两个盒子中各装有2个红球和2个白球，先从甲盒中任取一球，观察颜色后放入乙盒中，再从乙盒中任取一个球，令 X, Y分别表示从甲盒和乙盒中取到的红球个数，则 X与 Y的相关系数为___

**答案:**# 1 5.

**解析:**解 根据相关系数的计算公式，X与Y的相关系数为<equation>\rho = \frac {\operatorname {C o v} (X , Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}}.</equation>下面分别计算 X, Y的分布律与数字特征.

取球模型为等可能模型.

X的可能取值为0，1.取到白球，则<equation>X=0</equation>，取到红球，则<equation>X=1.</equation><equation>P \{X = 0 \} = \frac {1}{2}, \quad P \{X = 1 \} = \frac {1}{2}.</equation>于是，<equation>E ( X ) = \frac {1}{2}, E \left( X^{2}\right) = \frac {1}{2}, D ( X ) = \frac {1}{2} - \left(\frac {1}{2}\right)^{2} = \frac {1}{4}.</equation>Y的可能取值为0，1. 若从甲盒中取出的是白球，则后来乙盒中共有2个红球和3个白球，取到红球的概率为<equation>\frac{2}{5}</equation>即在 X=0发生的条件下 Y=1发生的概率为<equation>\frac{2}{5}</equation>；若从甲盒中取出的是红球，则后来乙盒中共有3个红球和2个白球，取到红球的概率为<equation>\frac{3}{5}</equation>即在 X=1发生的条件下 Y=1发生的概率为<equation>\frac{3}{5}.</equation><equation>\begin{aligned} P \{Y = 1 \} &= P \{Y = 1 \mid X = 0 \} P \{X = 0 \} + P \{Y = 1 \mid X = 1 \} P \{X = 1 \} \\ &= \frac {2}{5} \times \frac {1}{2} + \frac {3}{5} \times \frac {1}{2} = \frac {1}{2}. \end{aligned}</equation><equation>P \{Y = 0 \} = 1 - P \{Y = 1 \} = 1 - \frac {1}{2} = \frac {1}{2}.</equation>于是，<equation>E ( Y )=\frac{1}{2}, E ( Y^{2} )=\frac{1}{2}, D ( Y )=\frac{1}{2}-\left(\frac{1}{2}\right)^{2}=\frac{1}{4}.</equation>XY的可能取值为0,1.<equation>P \{X Y = 1 \} = P \{X = 1, Y = 1 \} = P \{Y = 1 \mid X = 1 \} P \{X = 1 \} = \frac {3}{5} \times \frac {1}{2} = \frac {3}{1 0}.</equation><equation>P \{X Y = 0 \} = 1 - \frac {3}{1 0} = \frac {7}{1 0}.</equation>于是，<equation>E ( X Y ) = P \{ X Y = 1 \} \times 1 + P \{ X Y = 0 \} \times 0 = \frac {3}{1 0}.</equation>因此，<equation>\rho = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {\frac {3}{1 0} - \frac {1}{2} \times \frac {1}{2}}{\frac {1}{2} \times \frac {1}{2}} = \frac {\frac {1}{2 0}}{\frac {1}{4}} = \frac {1}{5}.</equation>

---


#### 数学期望与方差


**2024年第8题 | 选择题 | 5分 | 答案: B**

8. 设随机变量 X的概率密度为<equation>f ( x )=\left\{\begin{array}{ll}6 x(1-x),&0<x<1,\\0,&\text{其他},\end{array}\right.</equation>则 X的三阶中心矩<equation>E \left\{ \left[ X-E ( X ) \right]^{3} \right\}=(\quad)</equation>A.<equation>-\frac{1}{3 2}</equation>B.0 C.<equation>\frac{1}{1 6}</equation>D.<equation>\frac{1}{2}</equation>

答案: B

**解析:**解 根据数学期望的定义，<equation>\begin{aligned} E (X) &= \int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \int_ {0} ^ {1} x \cdot 6 x (1 - x) \mathrm {d} x = \int_ {0} ^ {1} \left(6 x ^ {2} - 6 x ^ {3}\right) \mathrm {d} x = \left. \left(2 x ^ {3} - \frac {3 x ^ {4}}{2}\right) \right| _ {0} ^ {1} \\ &= 2 - \frac {3}{2} = \frac {1}{2}. \end{aligned}</equation>进一步可得，<equation>\begin{array}{l} E \left\{\left[ X - E (X) \right] ^ {3} \right\} = \int_ {- \infty} ^ {+ \infty} \left(x - \frac {1}{2}\right) ^ {3} f (x) \mathrm {d} x = \int_ {0} ^ {1} \left(x - \frac {1}{2}\right) ^ {3} \cdot 6 x (1 - x) \mathrm {d} x \\ \underline {{=}} t = x - \frac {1}{2} 6 \int_ {- \frac {1}{2}} ^ {\frac {1}{2}} t ^ {3} \cdot \left(t + \frac {1}{2}\right) \left(\frac {1}{2} - t\right) \mathrm {d} t = 6 \int_ {- \frac {1}{2}} ^ {\frac {1}{2}} t ^ {3} \left(\frac {1}{4} - t ^ {2}\right) \mathrm {d} t \\ = 6 \int_ {- \frac {1}{2}} ^ {\frac {1}{2}} \left(\frac {1}{4} t ^ {3} - t ^ {5}\right) \mathrm {d} t \stackrel {\text {对称性}} {=} 0. \\ \end{array}</equation>因此，应选B.

---


### 随机变量及其分布

### 随机事件和概率

### 多维随机变量及其分布

#### 边缘分布与条件分布


**2025年第22题 | 解答题 | 12分**

22. 投保人的损失事件发生时，保险公司的赔付额 Y与投保人的损失额 X的关系为<equation>Y=\left\{\begin{array}{ll}0,&X\leqslant 100\\ X-100,&X>100\end{array} \right.</equation>. 设定损事件发生时，投保人的损失额 X的概率密度为<equation>f(x)=\left\{\begin{array}{ll}\frac{2\times 100^{2}}{(100+x)^{3}},&x>0\\ 0,&x\leqslant 0\end{array} \right.</equation>I. 求<equation>P\{Y>0\}</equation>及 EY.

Ⅱ. 这种损失事件在一年内发生的次数记为 N，保险公司在一年内就这种损失事件产生的理赔次数记为 M，假设 N服从参数为8的泊松分布，在<equation>N=n</equation>（<equation>n\geqslant1</equation>）的条件下，M服从二项分布<equation>B(n,p)</equation>，其中<equation>p=P\{Y>0\}</equation>，求 M的概率分布.

**答案:**（I）<equation>P \left\{Y > 0\right\}=\frac{1}{4}, E (Y)=50;</equation>（Ⅱ）M服从参数为2的泊松分布.

**解析:**解（I）根据 Y的定义，<equation>\begin{aligned} P \{Y > 0 \} &= P \{X > 1 0 0 \} = \int_ {1 0 0} ^ {+ \infty} f (x) \mathrm {d} x = \int_ {1 0 0} ^ {+ \infty} \frac {2 \times 1 0 0 ^ {2}}{(1 0 0 + x) ^ {3}} \mathrm {d} x = - \frac {2 \times 1 0 0 ^ {2}}{2} (1 0 0 + x) ^ {- 2} \Bigg | _ {1 0 0} ^ {+ \infty} \\ &= - \frac {1 0 0 ^ {2}}{(1 0 0 + x) ^ {2}} \Bigg | _ {1 0 0} ^ {+ \infty} = \frac {1}{4}. \end{aligned}</equation>由于随机变量<equation>Y</equation>是随机变量<equation>X</equation>的函数，故根据数学期望的定义，<equation>\begin{aligned} E (Y) &= 0 \cdot P \{Y = 0 \} + \int_ {1 0 0} ^ {+ \infty} (x - 1 0 0) f (x) \mathrm {d} x = \int_ {1 0 0} ^ {+ \infty} \frac {2 \times 1 0 0 ^ {2} (x - 1 0 0)}{\left(1 0 0 + x\right) ^ {3}} \mathrm {d} x \\ &= - 1 0 0 ^ {2} \int_ {1 0 0} ^ {+ \infty} (x - 1 0 0) \mathrm {d} \left[ (1 0 0 + x) ^ {- 2} \right] = - 1 0 0 ^ {2} \left[ \frac {x - 1 0 0}{(1 0 0 + x) ^ {2}} \right| _ {1 0 0} ^ {+ \infty} - \int_ {1 0 0} ^ {+ \infty} \frac {\mathrm {d} x}{(1 0 0 + x) ^ {2}} ] \\ &= \frac {- 1 0 0 ^ {2}}{1 0 0 + x} \Bigg | _ {1 0 0} ^ {+ \infty} = 0 - \left(- \frac {1 0 0 ^ {2}}{2 0 0}\right) = 5 0. \end{aligned}</equation>（Ⅱ）由于<equation>N</equation>服从参数为8的泊松分布，故<equation>P\{N = n\} = \frac{8^n\mathrm{e}^{-8}}{n!}</equation>，进一步可得<equation>P\{N = 0\} = \mathrm{e}^{-8}</equation>由于当<equation>N = 0</equation>时，<equation>M</equation>必然等于0，故<equation>P\{M = 0\mid N = 0\} = 1</equation>，从而<equation>P \{M = 0, N = 0 \} = P \{M = 0 \mid N = 0 \} P \{N = 0 \} = 1 \cdot P \{N = 0 \} = \mathrm {e} ^ {- 8}.</equation>由 M的定义可知，当<equation>M=k</equation>时，<equation>N=n\geqslant k</equation>由在<equation>N=n(n\geqslant 1)</equation>的条件下，M服从二项分布 B(n,p）可得，<equation>P \left\{M = k \mid N = n \right\} = \mathrm {C} _ {n} ^ {k} p ^ {k} (1 - p) ^ {n - k}, \quad k = 0, 1, \dots , n, n = 1, 2, \dots .</equation>由条件概率公式以及<equation>p=\frac{1}{4}</equation>可得<equation>\begin{aligned} P \{M = k, N = n \} &= P \{M = k \mid N = n \} P \{N = n \} = C _ {n} ^ {k} p ^ {k} (1 - p) ^ {n - k} \frac {8 ^ {n} \mathrm {e} ^ {- 8}}{n !} \\ &= \frac {n !}{k ! (n - k) !} \cdot \left(\frac {1}{4}\right) ^ {k} \cdot \left(\frac {3}{4}\right) ^ {n - k} \cdot \frac {8 ^ {n} \mathrm {e} ^ {- 8}}{n !} = \frac {3 ^ {n - k} 2 ^ {n} \mathrm {e} ^ {- 8}}{k ! (n - k) !} \\ &= \frac {6 ^ {n - k} 2 ^ {k} \mathrm {e} ^ {- 8}}{k ! (n - k) !}. \end{aligned}</equation>由此可得，当<equation>k\neq 0</equation>时，<equation>\begin{aligned} P \{M = k \} &= \sum_ {n = k} ^ {\infty} P \{M = k, N = n \} = \sum_ {n = k} ^ {\infty} \frac {6 ^ {n - k} 2 ^ {k} \mathrm {e} ^ {- 8}}{k ! (n - k) !} = \frac {2 ^ {k} \mathrm {e} ^ {- 2}}{k !} \sum_ {n = k} ^ {\infty} \frac {6 ^ {n - k} \mathrm {e} ^ {- 6}}{(n - k) !} \\ &= \frac {2 ^ {k} \mathrm {e} ^ {- 2}}{k !} \sum_ {n = 0} ^ {\infty} \frac {6 ^ {n} \mathrm {e} ^ {- 6}}{n !}. \end{aligned}</equation><equation>\begin{aligned} P \{M = 0 \} &= \sum_ {n = 0} ^ {\infty} P \{M = 0, N = n \} = \mathrm {e} ^ {- 8} + \sum_ {n = 1} ^ {\infty} P \{M = 0, N = n \} = \mathrm {e} ^ {- 8} + \sum_ {n = 1} ^ {\infty} \frac {6 ^ {n} \mathrm {e} ^ {- 6}}{n !} \cdot \mathrm {e} ^ {- 2} \\ &= \mathrm {e} ^ {- 2} \sum_ {n = 0} ^ {\infty} \frac {6 ^ {n} \mathrm {e} ^ {- 6}}{n !}. \end{aligned}</equation>由泊松分布的定义可知，服从参数为6的泊松分布的随机变量Z的分布律为<equation>P\{Z = n\} = \frac{6^{n}\mathrm{e}^{-6}}{n!}</equation>.由分布律的性质可得，<equation>\sum_{n = 0}^{\infty}\frac{6^{n}\mathrm{e}^{-6}}{n!} = 1.</equation>于是，<equation>P\{M = k\} = \frac{2^{k}\mathrm{e}^{-2}}{k!},k = 0,1,2,\dots .</equation>因此，M服从参数为2的泊松分布

---

**2013年第22题 | 解答题 | 11分**


设 (X,Y)是二维随机变量，X的边缘概率密度为<equation>f_{X}(x)=\left\{ \begin{array}{ll} 3x^{2}, & 0<x<1, \\ 0, & \text{其他.} \end{array} \right.</equation>在给定 X=x(0<x<1)的条件下 Y的条件概率密度为<equation>f_{Y|X}(y\mid x)=\left\{ \begin{array}{ll} \frac{3y^{2}}{x^{3}}, & 0<y<x, \\ 0, & \text{其他.} \end{array} \right.</equation>I. 求 (X,Y)的概率密度 f(x,y);

II. 求 Y的边缘概率密度<equation>f_{Y}(y)</equation>III. 求<equation>P\{X>2Y\}</equation>

**答案:**(22) (I)<equation>f ( x,y)=\left\{\begin{array}{ll}\frac{9 y^{2}}{x},&0<y<x,0<x<1,\\ 0,&\text{其他};\end{array} \right.</equation>(Ⅱ)<equation>f_{Y}(y)=\left\{\begin{array}{ll}-9 y^{2}\ln y,&0<y<1,\\ 0,&\text{其他};\end{array} \right.</equation>(Ⅲ)<equation>\frac{1}{8}.</equation>

**解析:**解（I）当<equation>0 < x < 1</equation>时，<equation>f_{X}(x)=3x^{2},f_{Y\mid X}(y\mid x)=\frac{f(x,y)}{f_{X}(x)}=\left\{ \begin{array}{ll}\frac{3y^{2}}{x^{3}},&0<y<x,\\ 0,&\text{其他}, \end{array} \right.</equation>故当<equation>0 < x < 1</equation>时，<equation>f (x, y) = \left\{ \begin{array}{l l} \frac {9 y ^ {2}}{x}, & 0 < y < x, \\ 0, & y \leqslant 0 \text {或} y \geqslant x. \end{array} \right.</equation>下面求当<equation>x \leqslant 0</equation>或<equation>x \geqslant 1</equation>时<equation>f(x,y)</equation>的取值.

由于<equation>\int_ {0} ^ {1} \mathrm {d} x \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {x} \frac {9 y ^ {2}}{x} \mathrm {d} y = \int_ {0} ^ {1} 3 x ^ {2} \mathrm {d} x = 1,</equation>故可以认为在<equation>\left\{(x,y)\mid 0 < x < 1,-\infty < y < +\infty\right\}</equation>以外的平面上，即<equation>x\leqslant 0</equation>或<equation>x\geqslant 1</equation>时，<equation>f(x,y)=0.</equation>综上所述，<equation>(X,Y)</equation>的概率密度<equation>f(x,y) = \left\{ \begin{array}{ll}\frac{9y^2}{x}, & 0 < y < x,0 < x < 1,\\ 0, & \text{其他}. \end{array} \right.</equation>（Ⅱ）由第（I）问知<equation>Y</equation>的边缘概率密度为<equation>f _ {Y} (y) = \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} x = \left\{ \begin{array}{l l} \int_ {y} ^ {1} \frac {9 y ^ {2}}{x} \mathrm {d} x, & 0 < y < 1, \\ 0, & \text {其 他} \end{array} = \left\{ \begin{array}{l l} - 9 y ^ {2} \ln y, & 0 < y < 1, \\ 0, & \text {其 他}. \end{array} \right. \right.</equation>或者，将上述积分次序改为先对<equation>x</equation>积分，再对<equation>y</equation>积分，可得<equation>\begin{array}{l} P \left\{X > 2 Y \right\} = \iint_ {| (x, y) | x > 2 y |} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {\frac {1}{2}} \mathrm {d} y \int_ {2 y} ^ {1} \frac {9 y ^ {2}}{x} \mathrm {d} x = \int_ {0} ^ {\frac {1}{2}} \left(- 9 y ^ {2} \ln 2 y\right) \mathrm {d} y \\ = - 3 y ^ {3} \ln 2 y \left| _ {0} ^ {\frac {1}{2}} + \int_ {0} ^ {\frac {1}{2}} \frac {6 y ^ {3}}{2 y} \mathrm {d} y = \int_ {0} ^ {\frac {1}{2}} 3 y ^ {2} \mathrm {d} y = \frac {1}{8}. \right. \\ \end{array}</equation>

---


#### 二维随机变量及其分布


**2024年第10题 | 选择题 | 5分 | 答案: D**

10. 设随机变量 X，Y相互独立，且均服从参数为<equation>\lambda</equation>的指数分布. 令<equation>Z=|X-Y|</equation>，则下列随机变量中与 Z同分布的是（    ）

A.<equation>X+Y</equation>B.<equation>\frac{X+Y}{2}</equation>C. 2X D. X

答案: D

**解析:**解 由于 X, Y相互独立，且均服从参数为<equation>\lambda</equation>的指数分布，故（X，Y）的联合概率密度为<equation>f (x, y) = \left\{ \begin{array}{l l} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)}, & x > 0, y > 0, \\ 0, & \text {其 他}. \end{array} \right.</equation>记<equation>F_{Z}(z)</equation>为<equation>Z=|X-Y|</equation>的分布函数，<equation>D_{z}=\left\{(x,y)\right|-z\leq x-y\leq z\}</equation>，则<equation>F _ {Z} (z) = P \left\{Z \leqslant z \right\} = P \left\{\left| X - Y \right| \leqslant z \right\} = P \left\{- z \leqslant X - Y \leqslant z \right\} = \iint_ {D.} f (x, y) \mathrm {d} x \mathrm {d} y.</equation>当<equation>z < 0</equation>时，<equation>D_{z} = \varnothing , F_{Z}(z) = 0.</equation>当<equation>z \geqslant 0</equation>时，记<equation>D = \{(x,y) \mid x \geqslant 0, y \geqslant 0\}</equation>，则<equation>D \cap D_z \neq \emptyset</equation>，为图（a）中的灰色区域.

(a)

(b)

下面用两种方法计算<equation>z \geqslant 0</equation>时的<equation>F_{z}(z)</equation>.

(c)

（法一）如图（a）所示，由于<equation>D \cap D_{z}</equation>关于直线<equation>y=x</equation>对称，故记其位于直线<equation>y=x</equation>下方的部分为<equation>D_{0}.</equation>将<equation>D_{0}</equation>写成Y型区域，<equation>D_{0}=\left|(x,y)\right| \mid y \leqslant x \leqslant y+z,0 \leqslant y < +\infty \mid.</equation><equation>\begin{array}{l} F _ {z} (z) = \iint_ {D _ {z}} f (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {D \cap D _ {z}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y \xlongequal {\text {轮 换 对称 性}} 2 \iint_ {D _ {0}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y \\ = 2 \lambda^ {2} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \mathrm {d} y \int_ {y} ^ {y + z} \mathrm {e} ^ {- \lambda x} \mathrm {d} x = - 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \cdot \mathrm {e} ^ {- \lambda x} \Bigg | _ {x = y} ^ {x = y + z} \mathrm {d} y \\ = - 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \left(\mathrm {e} ^ {- \lambda y - \lambda z} - \mathrm {e} ^ {- \lambda y}\right) \mathrm {d} y = - 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- 2 \lambda y} \left(\mathrm {e} ^ {- \lambda z} - 1\right) \mathrm {d} y \\ = \left(\mathrm {e} ^ {- \lambda z} - 1\right) \int_ {0} ^ {+ \infty} \left(- 2 \lambda \mathrm {e} ^ {- 2 \lambda y}\right) \mathrm {d} y = \left(\mathrm {e} ^ {- \lambda z} - 1\right) \mathrm {e} ^ {- 2 \lambda y} \Bigg | _ {0} ^ {+ \infty} \\ = \left(\mathrm {e} ^ {- \lambda z} - 1\right) \cdot (- 1) = 1 - \mathrm {e} ^ {- \lambda z}. \\ \end{array}</equation>（法二）如图（b）所示，<equation>D_{1}=D\backslash D_{z}</equation>关于直线<equation>y=x</equation>对称，记其位于直线<equation>y=x</equation>下方的部分为<equation>D_{2}.</equation>将<equation>D_{2}</equation>写成Y型区域，<equation>D_{2}=\{(x,y)\mid y+z\leqslant x<+\infty ,0\leqslant y<+\infty \}.</equation><equation>\begin{array}{l} F _ {Z} (z) = \iint_ {D _ {z}} f (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {D \cap D _ {z}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y = 1 - \iint_ {D _ {1}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y \\ \underline {{\text {轮换 对称性}}} 1 - 2 \iint_ {D _ {2}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y = 1 - 2 \lambda^ {2} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \mathrm {d} y \int_ {y + z} ^ {+ \infty} \mathrm {e} ^ {- \lambda x} \mathrm {d} x \\ = 1 + 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \cdot \mathrm {e} ^ {- \lambda x} \Bigg | _ {x = y + z} ^ {+ \infty} \mathrm {d} y = 1 - 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \cdot \mathrm {e} ^ {- \lambda (y + z)} \mathrm {d} y \\ = 1 - 2 \lambda \mathrm {e} ^ {- \lambda z} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- 2 \lambda y} \mathrm {d} y = 1 + \mathrm {e} ^ {- \lambda z} \cdot \mathrm {e} ^ {- 2 \lambda y} \Bigg | _ {0} ^ {+ \infty} = 1 - \mathrm {e} ^ {- \lambda z}. \\ \end{array}</equation>因此，<equation>F_{z}(z)=\left\{ \begin{array}{ll}1-\mathrm{e}^{-\lambda z},& z\geqslant 0,\\ 0,& \text{其他}, \end{array} \right. f_{z}(z)=\left\{ \begin{array}{ll}\lambda \mathrm{e}^{-\lambda z},& z\geqslant 0,\\ 0,& \text{其他}, \end{array} \right. Z</equation>服从参数为<equation>\lambda</equation>的指数分布.进一步可得，Z与X同分布.选项D正确，选项C错误.

下面说明选项A、B不正确.

对选项A，当<equation>z\geqslant 0</equation>时，由于<equation>D_{3} = \{(x,y)|x + y\leqslant z,x\geqslant 0,y\geqslant 0\}</equation>真包含于<equation>D\cap D_{z}</equation>，故<equation>X + Y</equation>的分布函数<equation>F_{1}(z)</equation>满足，对任意<equation>z > 0,F_{1}(z) < F_{Z}(z)</equation>.从而<equation>X + Y</equation>与Z不同分布.

对选项B，当<equation>z\geqslant 0</equation>时，记<equation>D_{4} = \left| (x,y)\right| x + y\leqslant 2z,x\geqslant 0,y\geqslant 0\}</equation>，则<equation>\frac{X+Y}{2}</equation>的分布函数<equation>\begin{array}{l} F _ {2} (z) = \iint_ {D _ {4}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y = \lambda^ {2} \int_ {0} ^ {2 x} \mathrm {e} ^ {- \lambda x} \mathrm {d} x \int_ {0} ^ {2 x - x} \mathrm {e} ^ {- \lambda y} \mathrm {d} y = 1 - (2 \lambda z + 1) \mathrm {e} ^ {- 2 \lambda z} \\ \neq F _ {Z} (z). \\ \end{array}</equation>从而<equation>\frac{X+Y}{2}</equation>与Z不同分布.

综上所述，应选D.

---

**2020年第8题 | 选择题 | 4分 | 答案: C**

8. 设随机变量（X，Y）服从二维正态分布<equation>N \left( 0,0;1,4;-\frac{1}{2} \right)</equation>，则下列随机变量中服从标准正态分布且与 X相互独立的是（    )

A.<equation>\frac{\sqrt{5}}{5} ( X+Y )</equation>B.<equation>\frac{\sqrt{5}}{5} ( X-Y )</equation>C.<equation>\frac{\sqrt{3}}{3} ( X+Y )</equation>D.<equation>\frac{\sqrt{3}}{3} ( X-Y )</equation>

答案: C

**解析:**解 由（X，Y）服从二维正态分布<equation>N \left( 0,0;1,4;-\frac{1}{2} \right)</equation>可知，<equation>X\sim N (0,1), Y\sim N (0,4)</equation>，且<equation>\rho_{X Y}=-\frac{1}{2}.</equation><equation>E ( X )=0,D ( X )=1,E ( Y )=0,D ( Y )=4.</equation>由此可计算<equation>\operatorname{C o v} ( X, Y ).</equation>由协方差的计算公式，可得<equation>\operatorname {C o v} (X, Y) = \rho_ {X Y} \sqrt {D (X)} \sqrt {D (Y)} = - \frac {1}{2} \times 1 \times 2 = - 1.</equation>由选项设置，分别考虑<equation>\operatorname{Cov}(X,X+Y),\operatorname{Cov}(X,X-Y)</equation>（由注可知，<equation>(X,X+Y),(X,X-Y)</equation>均服从二维正态分布）.<equation>\operatorname {C o v} (X, X + Y) = \operatorname {C o v} (X, X) + \operatorname {C o v} (X, Y) = 1 - 1 = 0.</equation><equation>\operatorname {C o v} (X, X - Y) = \operatorname {C o v} (X, X) - \operatorname {C o v} (X, Y) = 1 - (- 1) = 2.</equation>X与X-Y相关，从而不独立，故可以排除选项B、D.

又因为所求随机变量应服从标准正态分布，所以考虑将 X+Y标准化.<equation>E (X + Y) = 0, \quad D (X + Y) = D (X) + D (Y) + 2 \operatorname {C o v} (X, Y) = 1 + 4 - 2 = 3.</equation>由于<equation>D \left[ \frac{\sqrt{5}}{5} (X+Y) \right]=\frac{1}{5} D (X+Y)=\frac{3}{5} \neq 1,D \left[ \frac{\sqrt{3}}{3} (X+Y) \right]=\frac{1}{3} D (X+Y)=1</equation>，故可排除选项A，应选C.

---

**2019年第22题 | 解答题 | 11分**

2. (本题满分11分)

设随机变量 X与 Y相互独立，X服从参数为1的指数分布，Y的概率分布为<equation>P\{Y=-1\}=p,P\{Y=1\}=</equation><equation>1-p \left( 0<p<1 \right).</equation>令<equation>Z=XY</equation>.

I. 求 Z的概率密度；

II. p为何值时，X与 Z不相关；

III. X与 Z是否相互独立？

**答案:**（I）<equation>Z</equation>的概率密度为<equation>f_{Z}(z)=\left\{\begin{array}{ll}p\mathrm{e}^{z},&z\leqslant 0,\\ (1-p)\mathrm{e}^{-z},&z>0; \end{array} \right.</equation>（Ⅱ）当<equation>p=\frac{1}{2}</equation>时，X与Z不相关；

（Ⅲ）X与Z不相互独立.

**解析:**（I）先计算 Z的分布函数<equation>F_{Z}(z).</equation><equation>\begin{array}{l} F _ {Z} (z) = P \left\{X Y \leqslant z \right\} = P \left\{X \geqslant - z, Y = - 1 \right\} + P \left\{X \leqslant z, Y = 1 \right\} \\ \underline {{\text {独立性}}} P \left\{X \geqslant - z \right\} P \left\{Y = - 1 \right\} + P \left\{X \leqslant z \right\} P \left\{Y = 1 \right\} \\ = p \left[ 1 - F _ {X} (- z) \right] + (1 - p) F _ {X} (z), \\ \end{array}</equation>其中<equation>F_{X}(x)</equation>是X的分布函数.

于是，Z的概率密度为<equation>f _ {Z} (z) = F _ {Z} ^ {\prime} (z) = \left\{p \left[ 1 - F _ {X} (- z) \right] + (1 - p) F _ {X} (z) \right\} ^ {\prime} = p f _ {X} (- z) + (1 - p) f _ {X} (z).</equation>由于<equation>X</equation>服从参数为1的指数分布，故<equation>X</equation>的概率密度为<equation>f_{X}(x) = \left\{ \begin{array}{ll} \mathrm{e}^{-x}, & x > 0, \\ 0, & x \leqslant 0. \end{array} \right.</equation>当<equation>z\leqslant0</equation>时，<equation>-z\geqslant0,f_{X}(-z)=\mathrm{e}^{z},f_{X}(z)=0</equation>；当<equation>z > 0</equation>时，<equation>-z < 0,f_{X}(z)=\mathrm{e}^{-z},f_{X}(-z)=0.</equation><equation>f _ {Z} (z) = \left\{ \begin{array}{l l} p \mathrm {e} ^ {z}, & z \leqslant 0, \\ (1 - p) \mathrm {e} ^ {- z}, & z > 0. \end{array} \right.</equation>（Ⅱ）计算<equation>\operatorname{Cov}(X,Z).</equation><equation>\begin{array}{l} \operatorname {C o v} (X, Z) = E (X Z) - E (X) E (Z) = E \left(X ^ {2} Y\right) - E (X) E (X Y) \\ \underline {{\mathrm {独立性}}} E \left(X ^ {2}\right) E (Y) - \left[ E (X) \right] ^ {2} E (Y) \\ = D (X) E (Y). \\ \end{array}</equation>下面分别计算 D（X），E（Y）.

由于 X服从参数为1的指数分布，故<equation>D ( X )=1.</equation><equation>E (Y) = 1 \times (1 - p) + (- 1) \times p = 1 - 2 p.</equation>因此，<equation>\operatorname{Cov}(X,Z) = E(Y) = 1 - 2p.</equation>当<equation>p=\frac{1}{2}</equation>时，<equation>\operatorname{Cov}(X,Z)=0</equation>，X与Z不相关.

（Ⅲ）由第（Ⅱ）问可知，当<equation>p\neq \frac{1}{2}</equation>时，X与Z相关，从而不相互独立.

下面只需考虑 p =<equation>\frac{1}{2}</equation>的情况.

（法一）当<equation>p=\frac{1}{2}</equation>时，检验<equation>P\{X < 1,Z < 1\} = P\{X < 1\} P\{Z < 1\}</equation>是否成立.<equation>P \{X < 1 \} = \int_ {0} ^ {1} \mathrm {e} ^ {- x} \mathrm {d} x = 1 - \mathrm {e} ^ {- 1}.</equation><equation>\begin{aligned} P \{Z < 1 \} &= P \{X Y < 1 \} = F _ {Z} (1) = \frac {1}{2} \left[ 1 - F _ {X} (- 1) \right] + \frac {1}{2} F _ {X} (1) \\ &= \frac {1}{2} \times (1 - 0) + \frac {1}{2} \int_ {0} ^ {1} \mathrm {e} ^ {- x} \mathrm {d} x = \frac {1}{2} + \frac {1}{2} \left(1 - \mathrm {e} ^ {- 1}\right). \end{aligned}</equation><equation>\begin{aligned} P \{X < 1, Z < 1 \} &= P \{X < 1, X Y < 1 \} = P \{X \leqslant 0, X Y < 1 \} + P \{0 < X < 1, X Y < 1 \} \\ &= P \{0 < X < 1, X Y < 1 \} = P \{0 < X < 1, Y = 1 \} + P \{0 < X < 1, Y = - 1 \} \\ &= P \{0 < X < 1 \} = P \{X < 1 \} = 1 - \mathrm {e} ^ {- 1}. \end{aligned}</equation>由于<equation>1-\mathrm{e}^{-1}\neq(1-\mathrm{e}^{-1})\cdot\left[\frac{1}{2}+\frac{1}{2}(1-\mathrm{e}^{-1})\right]</equation>，故X，Z不相互独立.

（法二）当<equation>p=\frac{1}{2}</equation>时，检验<equation>P\{X > 1,Z < 1\} = P\{X > 1\} P\{Z < 1\}</equation>是否成立.

当 X > 1时，XY < 1等价于<equation>Y < \frac{1}{X}.</equation>又因为此时<equation>\frac{1}{X} < 1</equation>，而Y只可能取1和-1两个值，所以<equation>Y < \frac{1}{X}</equation>能推出 Y=-1.于是，<equation>P \{X > 1 \} = \int_ {1} ^ {+ \infty} \mathrm {e} ^ {- x} \mathrm {d} x = \mathrm {e} ^ {- 1}.</equation><equation>P \{Z < 1 \} \xlongequal {\text {同 法 一}} \frac {1}{2} + \frac {1}{2} \left(1 - \mathrm {e} ^ {- 1}\right).</equation><equation>\begin{array}{l} P \{X > 1, Z < 1 \} = P \{X > 1, X Y < 1 \} = P \left\{X > 1, Y < \frac {1}{X} \right\} = P \{X > 1, Y = - 1 \} \\ \underline {{\mathrm {独立 性}}} P \{X > 1 \} P \{Y = - 1 \} = \frac {1}{2} \mathrm {e} ^ {- 1}. \\ \end{array}</equation>由于<equation>\frac{1}{2}\mathrm{e}^{-1}\neq \mathrm{e}^{-1}\cdot \left[\frac{1}{2}+\frac{1}{2}\left(1-\mathrm{e}^{-1}\right)\right]</equation>，故X，Z不相互独立.

综上所述，X，Z不相互独立.

---

**2016年第22题 | 解答题 | 11分**

（本题满分11分）

设二维随机变量 (X,Y)在区域 D = {(x,y) | 0 < x < 1, x² < y <<equation>\sqrt{x}</equation>}上服从均匀分布，令<equation>U=\left\{\begin{array}{l l}1,&X\leqslant Y,\\ 0,&X>Y. \end{array} \right.</equation>I. 写出 (X,Y)的概率密度；

II. 问 U与 X是否相互独立？并说明理由；

III. 求 Z=U+X的分布函数 F(z).

**答案:**（I）<equation>f ( x,y)=\left\{ \begin{array}{ll} 3, & 0 < x < 1, x^{2} < y < \sqrt{x}, \\ 0, & \text{其他}; \end{array} \right.</equation>（Ⅱ）<equation>U</equation>与X不相互独立，理由略；

(Ⅲ)<equation>F (z) = \left\{ \begin{array}{ll} 0, & z < 0, \\ \frac{3}{2} z^{2} - z^{3}, & 0 \leqslant z < 1, \\ 2 (z - 1)^{\frac{3}{2}} - \frac{3}{2} z^{2} + 3 z - 1, & 1 \leqslant z < 2, \\ 1, & z \geqslant 2. \end{array} \right.</equation>

**解析:**（I）区域 D如图（a）所示，其面积为<equation>S = \int_ {0} ^ {1} \sqrt {x} \mathrm {d} x - \int_ {0} ^ {1} x ^ {2} \mathrm {d} x = \frac {2}{3} x ^ {\frac {3}{2}} \left| _ {0} ^ {1} - \frac {x ^ {3}}{3} \right| _ {0} ^ {1} = \frac {2}{3} - \frac {1}{3} = \frac {1}{3}.</equation>又由于（X，Y）在区域 D上服从均匀分布，故（X，Y）的概率密度为<equation>f (x, y) = \left\{ \begin{array}{l l} 3, & 0 < x < 1, x ^ {2} < y < \sqrt {x}, \\ 0, & \text {其 他}. \end{array} \right.</equation>(a)

(b)

（Ⅱ）考虑<equation>P\{U = 0, X\leqslant t\}</equation><equation>P \{U = 0 \} = P \{X > Y \} = \iint_ {\{(x, y) | x > x \}} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {x ^ {2}} ^ {x} 3 \mathrm {d} y = \int_ {0} ^ {1} 3 \left(x - x ^ {2}\right) \mathrm {d} x = \frac {1}{2}.</equation>对<equation>t \leqslant 0</equation>，<equation>P\{X \leqslant t\} = 0</equation>，<equation>P\{U = 0, X \leqslant t\} = 0.</equation>于是，<equation>P \left\{U = 0, X \leqslant t \right\} = P \left\{U = 0 \right\} \cdot P \left\{X \leqslant t \right\}.</equation>对<equation>t \geqslant 1</equation><equation>P\{X \leqslant t\} = 1,P\{U = 0,X \leqslant t\} = P\{U = 0\}</equation>.于是，<equation>P \{U = 0, X \leqslant t \} = P \{U = 0 \} \cdot P \{X \leqslant t \}.</equation>对 0 < t < 1，有效积分区域为图（b）中的蓝色区域.<equation>P \left\{U = 0, X \leqslant t \right\} = P \left\{X > Y, X \leqslant t \right\} = \int_ {0} ^ {t} \mathrm {d} x \int_ {x ^ {2}} ^ {x} 3 \mathrm {d} y = \int_ {0} ^ {t} 3 \left(x - x ^ {2}\right) \mathrm {d} x = \frac {3}{2} t ^ {2} - t ^ {3},</equation><equation>P \left\{X \leqslant t \right\} = \int_ {0} ^ {t} \mathrm {d} x \int_ {x ^ {2}} ^ {\sqrt {x}} 3 \mathrm {d} y = \int_ {0} ^ {t} 3 \left(\sqrt {x} - x ^ {2}\right) \mathrm {d} x = 2 t ^ {\frac {3}{2}} - t ^ {3}.</equation>于是，<equation>\begin{aligned} P \{U = 0, X \leqslant t \} - P \{U = 0 \} \cdot P \{X \leqslant t \} &= \frac {3}{2} t ^ {2} - t ^ {3} - \frac {1}{2} \left(2 t ^ {\frac {3}{2}} - t ^ {3}\right) \\ &= \frac {3}{2} t ^ {2} - \frac {1}{2} t ^ {3} - t ^ {\frac {3}{2}} \neq 0. (\mathrm {见 注} \textcircled{1}) \end{aligned}</equation>因此，当 0 < t < 1时，U与X不相互独立.

（Ⅲ）由题设知，<equation>\begin{array}{l} F (z) = P \left\{Z \leqslant z \right\} = P \left\{U + X \leqslant z \right\} \\ = P \left\{U + X \leqslant z, U = 0 \right\} + P \left\{U + X \leqslant z, U = 1 \right\} \\ = P \left\{X \leqslant z, U = 0 \right\} + P \left\{X \leqslant z - 1, U = 1 \right\} \\ = P \left\{X \leqslant z, X > Y \right\} + P \left\{X \leqslant z - 1, X \leqslant Y \right\}. \\ \end{array}</equation>当 z < 0时，z-1<0，于是<equation>P\{X\leqslant z,X > Y\}=0,P\{X\leqslant z-1,X\leqslant Y\}=0</equation>从而 F（z）=0.当 0≤z<1时，z-1<0，于是 P<equation>\{X\leqslant z-1,X\leqslant Y\}=0</equation>从而<equation>F (z) = P \left\{X \leqslant z, X > Y \right\} = \int_ {0} ^ {z} \mathrm {d} x \int_ {x ^ {2}} ^ {x} 3 \mathrm {d} y = \int_ {0} ^ {z} 3 \left(x - x ^ {2}\right) \mathrm {d} x = \frac {3}{2} z ^ {2} - z ^ {3}.</equation>当<equation>1\leqslant z < 2</equation>时，<equation>0\leqslant z - 1 < 1</equation><equation>\begin{array}{l} F (z) = P \left\{X \leqslant z, X > Y \right\} + P \left\{X \leqslant z - 1, X \leqslant Y \right\} \\ = P \left\{X \leqslant 1, X > Y \right\} + P \left\{X \leqslant z - 1, X \leqslant Y \right\} \\ = \frac {1}{2} + \int_ {0} ^ {z - 1} \mathrm {d} x \int_ {x} ^ {\sqrt {x}} 3 \mathrm {d} y = \frac {1}{2} + \int_ {0} ^ {z - 1} 3 (\sqrt {x} - x) \mathrm {d} x \\ = \frac {1}{2} + 2 (z - 1) ^ {\frac {3}{2}} - \frac {3}{2} (z - 1) ^ {2} = 2 (z - 1) ^ {\frac {3}{2}} - \frac {3}{2} z ^ {2} + 3 z - 1. \\ \end{array}</equation>当<equation>z\geqslant 2</equation>时，<equation>z - 1\geqslant 1,F(z) = 1.</equation>综上所述，<equation>F ( z ) = \left\{ \begin{array}{ll} 0, & z < 0, \\ \frac{3}{2} z^{2} - z^{3}, & 0 \leqslant z < 1, \\ 2 ( z - 1 )^{\frac{3}{2}} - \frac{3}{2} z^{2} + 3 z - 1, & 1 \leqslant z < 2, \\ 1, & z \geqslant 2. \end{array} \right.</equation>

---

**2015年第14题 | 填空题 | 4分**

14. 设二维随机变量<equation>(X, Y)</equation>服从正态分布<equation>N(1, 0; 1, 1; 0)</equation>, 则<equation>P\{XY - Y < 0\} =</equation>___

**解析:**由题设知，X，Y不相关。又由于（X，Y）服从正态分布，故X，Y相互独立.从而<equation>\begin{aligned} P \{X Y - Y < 0 \} &= P \{(X - 1) Y < 0 \} = P \{X < 1, Y > 0 \} + P \{X > 1, Y < 0 \} \\ &= P \{X < 1 \} \cdot P \{Y > 0 \} + P \{X > 1 \} \cdot P \{Y < 0 \}. \end{aligned}</equation>由<equation>( X, Y ) \sim N ( 1, 0 ; 1, 1 ; 0 )</equation>可知，<equation>X\sim N ( 1, 1 )</equation><equation>Y\sim N ( 0, 1 )</equation>从而X，Y的概率密度的图像分别关于<equation>x=1</equation>，<equation>x=0</equation>对称，于是<equation>P \{ X < 1 \} = P \{ X > 1 \} = \frac{1}{2}</equation><equation>P \{ Y < 0 \} = P \{ Y > 0 \} = \frac{1}{2}.</equation>因此，<equation>P \left\{X Y - Y < 0 \right\} = \frac {1}{2} \times \frac {1}{2} + \frac {1}{2} \times \frac {1}{2} = \frac {1}{2}.</equation>

---

**2013年第8题 | 选择题 | 4分 | 答案: C**

8. 设随机变量 X和 Y相互独立，且 X和 Y的概率分布分别为（    ）

<table border="1"><tr><td>X</td><td>0</td><td>1</td><td>2</td><td>3</td></tr><tr><td>P</td><td><equation>\frac{1}{2}</equation></td><td><equation>\frac{1}{4}</equation></td><td><equation>\frac{1}{8}</equation></td><td><equation>\frac{1}{8}</equation></td></tr></table>

<table border="1"><tr><td>Y</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td></tr></table>

则<equation>P\{X+Y=2\}=(\quad)</equation>A.<equation>\frac{1}{1 2}</equation>B.<equation>\frac{1}{8}</equation>C.<equation>\frac{1}{6}</equation>D.<equation>\frac{1}{2}</equation>

答案: C

**解析:**由题设知<equation>\begin{array}{l} P \{X + Y = 2 \} = P \{X = 1, Y = 1 \} + P \{X = 2, Y = 0 \} + P \{X = 3, Y = - 1 \} \\ \underline {{\underline {{X , Y}} \mathrm {相 互 独立}}} P \{X = 1 \} \cdot P \{Y = 1 \} + P \{X = 2 \} \cdot P \{Y = 0 \} + P \{X = 3 \} \cdot P \{Y = - 1 \} \\ = \frac {1}{4} \times \frac {1}{3} + \frac {1}{8} \times \frac {1}{3} + \frac {1}{8} \times \frac {1}{3} = \frac {1}{6}. \\ \end{array}</equation>应选C.

---

**2012年第7题 | 选择题 | 4分 | 答案: D**

7. 设随机变量 X与 Y相互独立，且都服从区间（0,1）上的均匀分布，则<equation>P\{ X^{2}+Y^{2}\leqslant1\}=</equation>A.<equation>\frac{1}{4}</equation>B.<equation>\frac{1}{2}</equation>C.<equation>\frac{\pi}{8}</equation>D.<equation>\frac{\pi}{4}</equation>

答案: D

**解析:**解 由题设知<equation>f_{X}(x) = \left\{ \begin{array}{ll}1, & 0 < x < 1,\\ 0, & \text{其他}, \end{array} \right.</equation><equation>f_{Y}(y) = \left\{ \begin{array}{ll}1, & 0 < y < 1,\\ 0, & \text{其他}. \end{array} \right.</equation>由于X与Y相互独立，故

（X，Y）的概率密度为<equation>f (x, y) = f _ {X} (x) f _ {Y} (y) = \left\{ \begin{array}{l l} 1, & 0 < x < 1, 0 < y < 1, \\ 0, & \text {其 他}. \end{array} \right.</equation>记<equation>D = \{(x,y)\mid 0\leqslant x\leqslant 1,0\leqslant y\leqslant 1\}</equation>，<equation>P \left\{X ^ {2} + Y ^ {2} \leqslant 1 \right\} = \iint_ {\left\{(x, y) \mid x ^ {2} + y ^ {2} \leqslant 1 \right\} \cap D} f (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {\left\{(x, y) \mid x ^ {2} + y ^ {2} \leqslant 1, x \geqslant 0, y \geqslant 0 \right\}} 1 \mathrm {d} x \mathrm {d} y = \frac {\pi}{4}.</equation>应选 D.

---

**2009年第8题 | 选择题 | 4分 | 答案: B**

8. 设随机变量 X与 Y相互独立，且 X服从标准正态分布 N(0,1), Y的概率分布为<equation>P\{Y=0\}=P\{Y=1\}=\frac{1}{2}</equation>. 记<equation>F_{Z}(z)</equation>为随机变量 Z=XY的分布函数，则函数<equation>F_{Z}(z)</equation>的间断点个数为（    )

A.0 B.1 C.2 D.3

答案: B

**解析:**解 先用两种方法求<equation>F_{Z}(z).</equation>（法一）由定义知<equation>\begin{array}{l} F _ {Z} (z) = P \left\{Z \leqslant z \right\} = P \left\{X Y \leqslant z \right\} = P \left\{X Y \leqslant z, Y = 0 \right\} + P \left\{X Y \leqslant z, Y = 1 \right\} \\ = P \left\{z \geqslant 0, Y = 0 \right\} + P \left\{X \leqslant z, Y = 1 \right\} \\ \xlongequal {X, Y \text {相 互 独立}} P \left\{z \geqslant 0, Y = 0 \right\} + P \left\{X \leqslant z \right\} \cdot P \left\{Y = 1 \right\} \\ = P \left\{z \geqslant 0, Y = 0 \right\} + \frac {1}{2} \Phi (z), \\ \end{array}</equation>其中<equation>\varPhi(z)</equation>为标准正态分布函数.

当<equation>z < 0</equation>时，<equation>P\{z\geqslant 0, Y = 0\} = P(\varnothing) = 0</equation>，故<equation>F_{Z}(z) = \frac{1}{2}\Phi (z).</equation>当<equation>z \geqslant 0</equation>时，<equation>P\{z \geqslant 0, Y = 0\} = P\{Y = 0\} = \frac{1}{2}</equation>，故<equation>F_{Z}(z) = \frac{1}{2} +\frac{1}{2}\Phi (z).</equation>（法二）由全概率公式知<equation>\begin{array}{l} F _ {Z} (z) = P \left\{Z \leqslant z \right\} = P \left\{X Y \leqslant z \right\} \\ = P \left\{X Y \leqslant z \mid Y = 0 \right\} \cdot P \left\{Y = 0 \right\} + P \left\{X Y \leqslant z \mid Y = 1 \right\} \cdot P \left\{Y = 1 \right\} \\ = \frac {1}{2} P \left\{z \geqslant 0 \mid Y = 0 \right\} + \frac {1}{2} P \left\{X \leqslant z \mid Y = 1 \right\} \\ \underline {{\underline {{X , Y}} \text {相 互 独 立}}} \frac {1}{2} P \left\{z \geqslant 0 \right\} + \frac {1}{2} P \left\{X \leqslant z \right\} \\ = \left\{ \begin{array}{l l} \frac {1}{2} \Phi (z), & z < 0, \\ \frac {1}{2} + \frac {1}{2} \Phi (z), & z \geqslant 0. \end{array} \right. \\ \end{array}</equation>由于<equation>\varPhi(z)</equation>连续，故<equation>F_{z}(z)</equation>仅在<equation>z = 0</equation>处间断.应选B.

---

**2009年第23题 | 解答题 | 11分**


袋中有1个红球、2个黑球与3个白球.现有放回地从袋中取两次，每次取一个球.以 X，Y，Z分别表示两次取球所取得的红球、黑球与白球的个数.

I. 求<equation>P\{X=1\mid Z=0\}</equation>；

II. 求二维随机变量（X，Y）的概率分布.

**答案:**(23) (I)<equation>\frac{4}{9}</equation>;

（Ⅱ）X和Y的联合分布律为

<table border="1"><tr><td rowspan="2">X

Y</td><td>0</td><td>1</td><td>2</td></tr><tr><td><equation>\frac{1}{4}</equation></td><td><equation>\frac{1}{6}</equation></td><td><equation>\frac{1}{36}</equation></td></tr><tr><td>1</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{9}</equation></td><td>0</td></tr><tr><td>2</td><td><equation>\frac{1}{9}</equation></td><td>0</td><td>0</td></tr></table>

**解析:**解（I）（法一）由条件概率的定义知，<equation>P \{X = 1 \mid Z = 0 \} = \frac {P \{X = 1 , Z = 0 \}}{P \{Z = 0 \}} = \frac {P \{X = 1 , Y = 1 \}}{P \{Z = 0 \}} = \frac {\mathrm {C} _ {2} ^ {1} \times \frac {1}{6} \times \frac {2}{6}}{\frac {3}{6} \times \frac {3}{6}} = \frac {4}{9}.</equation>（法二）<equation>P \{ X=1 \mid Z=0 \}</equation>是指在 Z=0，即两次所取的球中没有白球的条件下，两次取球为一黑一红的概率，即在1个红球、2个黑球中有放回地取得一黑一红的概率.因此，<equation>P \left\{X = 1 \mid Z = 0 \right\} = C _ {2} ^ {1} \times \frac {1}{3} \times \frac {2}{3} = \frac {4}{9}.</equation>（Ⅱ）由于是有放回地取球，故 X，Y所有可能的取值均为0，1，2.于是二维随机变量（X，Y）的概率分布为，<equation>P \{X = 0, Y = 0 \} = P \{Z = 2 \} = \frac {3}{6} \times \frac {3}{6} = \frac {1}{4},</equation><equation>P \{X = 0, Y = 1 \} = P \{Y = 1, Z = 1 \} = C _ {2} ^ {1} \times \frac {2}{6} \times \frac {3}{6} = \frac {1}{3},</equation><equation>P \{X = 0, Y = 2 \} = \frac {2}{6} \times \frac {2}{6} = \frac {1}{9},</equation><equation>P \{X = 1, Y = 0 \} = P \{X = 1, Z = 1 \} = C _ {2} ^ {1} \times \frac {1}{6} \times \frac {3}{6} = \frac {1}{6},</equation><equation>P \{X = 1, Y = 1 \} = \mathrm {C} _ {2} ^ {1} \times \frac {1}{6} \times \frac {2}{6} = \frac {1}{9}, \quad P \{X = 1, Y = 2 \} = 0,</equation><equation>P \{X = 2, Y = 0 \} = \frac {1}{6} \times \frac {1}{6} = \frac {1}{3 6}, \quad P \{X = 2, Y = 1 \} = 0, \quad P \{X = 2, Y = 2 \} = 0.</equation>因此，X和Y的联合分布律为

<table border="1"><tr><td rowspan="2">Y

X</td><td>0</td><td>1</td><td>2</td></tr><tr><td><equation>\frac{1}{4}</equation></td><td><equation>\frac{1}{6}</equation></td><td><equation>\frac{1}{36}</equation></td></tr><tr><td>1</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{9}</equation></td><td>0</td></tr><tr><td>2</td><td><equation>\frac{1}{9}</equation></td><td>0</td><td>0</td></tr></table>

---


### 数理统计的基本概念

### 大数定律和中心极限定理

### 参数估计

# 张宇数学公式手册

## 第一部分 高等数学

### 第三章 一元函数积分学

### 第七章 级 数

## 第二部分 线性代数

### 第二章 矩 阵 91

## 第三部分 概率论与数理统计

### 第一章 随机事件和概率

### 第四章 随机变量的数字特征

#### 附录 和等数学


第五章 大数定律和中心极限定理

一、切比雪夫不等式

二、大数定律

三、中心极限定理

第六章 数理统计的基本概念

一、统计量的样本数字特征及极限

二、统计分布与抽样分布定理

第七章 参数估计

一、矩估计法

二、最大似然估计法

三、置信区间

四、常用单个正态总体参数的置信区间表


初等代数

初等几何

三角函数

平面解析几何

---


## 第一部分高等数学

### 第一章 函数、极限、连续

#### (2)有界性


设在某个过程中有两个变量 x和 y，对变量 x在允许范围内的每一个确定的值，变量 y按照某一确定的法则总有相应的值与之对应，则称 y为 x的函数，记为<equation>y = f(x)</equation>.


设函数<equation>y = f(x)</equation>的定义区间<equation>I</equation>关于原点对称，如果对于<equation>I</equation>内任意一点<equation>x</equation>，恒有<equation>f(-x) = f(x)</equation>，则称<equation>f(x)</equation>为区间<equation>I</equation>内的偶函数；如果恒有<equation>f(-x) = -f(x)</equation>，则称<equation>f(x)</equation>为区间<equation>I</equation>内的奇函数.


设函数<equation>f(x)</equation>在<equation>I</equation>上有定义，如果存在常数<equation>M</equation>，当<equation>x \in I</equation>时，恒有<equation>f(x) \leqslant M</equation>，则称<equation>f(x)</equation>在<equation>I</equation>上有上界；设函数<equation>f(x)</equation>在<equation>I</equation>上有定义，如果存在常数<equation>m</equation>，当<equation>x \in I</equation>时，恒有<equation>f(x) \geqslant m</equation>，则称<equation>f(x)</equation>在<equation>I</equation>上有下界；设函数

---


#### （3）初等函数


<equation>f(x)</equation>在<equation>I</equation>上有定义，如果存在常数<equation>M > 0</equation>，当<equation>x\in I</equation>时，恒有<equation>|f(x)|\leqslant M</equation>，则称<equation>f(x)</equation>在<equation>I</equation>上有界.


设函数<equation>f(x)</equation>在区间<equation>I</equation>上有定义，若存在<equation>T > 0</equation>，对任意的<equation>x\in I</equation>，必有<equation>x\pm T\in I</equation>，并且<equation>f(x + T) = f(x)</equation>，则称<equation>f(x)</equation>为周期函数.使得上述关系式成立的最小正数<equation>T</equation>称为<equation>f(x)</equation>的最小正周期，简称为函数<equation>f(x)</equation>的周期.


设函数<equation>f(x)</equation>在区间<equation>I</equation>内有定义，如果对于该区间内的任意两点<equation>x_{1} < x_{2}</equation>，恒有<equation>f(x_{1}) < f(x_{2})</equation>（或<equation>f(x_{1}) > f(x_{2})</equation>），则称<equation>f(x)</equation>在区间<equation>I</equation>内单调增加（或单调减少）。


设函数<equation>y = f(x)</equation>的定义域为<equation>D</equation>，值域为<equation>R</equation>.若对任意<equation>y\in R</equation>，有唯一确定的<equation>x\in D</equation>，使得<equation>y = f(x)</equation>，则记为<equation>x = f^{-1}(y)</equation>，称其为<equation>y = f(x)</equation>的反函数.


若函数<equation>u = \varphi (x)</equation>在<equation>x_{0}</equation>处有定义，函数<equation>y = f(u)</equation>在<equation>u_{0} = \varphi (x_{0})</equation>处有定义，则函数<equation>y = f[\varphi (x)]</equation>在<equation>x_{0}</equation>处有定义，称<equation>y = f[\varphi (x)]</equation>是由函数<equation>y = f(u)</equation>和<equation>u = \varphi (x)</equation>复合而成的复合函数，<equation>u</equation>为中间变量.


由六类基本初等函数经过有限次四则运算及有限

---


#### （5）隐函数


次复合运算得到的，并能用一个数学表达式表示的函数，称为初等函数.

注 六类基本初等函数为：

<equation>y=C</equation>（常数）；

<equation>y=x^{n}</equation>；

<equation>y=a^{x}</equation>（<equation>a>0</equation>且<equation>a\neq1)</equation>；

<equation>y=\log_{a} x</equation>（<equation>a>0</equation>且<equation>a\neq1)</equation>；

<equation>y=\sin x,\cos x,\tan x,\cot x,\sec x,\csc x;</equation>

<equation>y=\arcsin x,\arccos x,\arctan x,\arccot x.</equation>


在定义域内的不同范围用不同表达式表示的函数称为分段函数.

注 常见的分段函数有：

<equation>\textcircled{1}</equation>绝对值函数<equation>|x|=\left\{ \begin{array}{ll} x, & x\geqslant 0, \\ -x, & x<0. \end{array} \right.</equation>

<equation>\textcircled{2}</equation>符号函数<equation>\operatorname{sgn} x=\left\{ \begin{array}{ll} 1, & x>0, \\ 0, & x=0, \\ -1, & x<0. \end{array} \right.</equation>

<equation>\textcircled{3}</equation>取整函数<equation>[x]</equation>表示不超过 x的最大整；


如果在方程<equation>F(x,y) = 0</equation>中，当<equation>x</equation>取某区间内的任一值时，相应地总有满足这一方程的唯一的<equation>y</equation>值存在，

---


#### (1)唯一性


那么就说方程 F(x,y)=0在该区间内确定了一个隐函数 y=y(x).


若对于任意给定的正数<equation>\varepsilon</equation>，总存在正整数<equation>N</equation>，当<equation>n > N</equation>时，恒有<equation>|x_{n} - A| < \varepsilon</equation>，则称常数<equation>A</equation>为当<equation>n\to \infty</equation>时数列<equation>x_{n}</equation>的极限，记为<equation>\lim x_n = A</equation>


设函数<equation>f(x)</equation>在<equation>|x|</equation>充分大时都有定义，若对于任意给定的正数<equation>\varepsilon</equation>，总存在正数<equation>X</equation>，当<equation>|x| > X</equation>时，恒有<equation>|f(x) - A| < \varepsilon</equation>，则称常数<equation>A</equation>为当<equation>x\to \infty</equation>时函数<equation>f(x)</equation>的极限，记为<equation>\lim f(x) = A</equation>。


设函数<equation>f(x)</equation>在<equation>x_0</equation>的某个去心邻域内有定义，若对于任意给定的正数<equation>\varepsilon</equation>，总存在正数<equation>\delta</equation>，当<equation>0 < |x - x_0| < \delta</equation>时，恒有<equation>|f(x) - A| < \varepsilon</equation>，则称常数<equation>A</equation>为当<equation>x \rightarrow x_0</equation>时函数<equation>f(x)</equation>的极限，记为<equation>\lim f(x) = A</equation>。


设<equation>\lim_{x\to x_0}f(x) = A,</equation><equation>\lim_{x\to x_0}f(x) = B,</equation>则<equation>A = B.</equation>

---


#### （1）极限的四则运算法则


若<equation>\lim_{x\to x_0}f(x)</equation>存在，则存在<equation>\delta > 0</equation>，使<equation>f(x)</equation>在<equation>U = \{x|0\leqslant |x - x_0| < \delta \}</equation>内有界.


<equation>\textcircled{1}</equation>若<equation>\lim_{x\to x_0}f(x) = A > 0</equation>，则存在<equation>x_0</equation>的一个去心邻域，在该邻域内恒有<equation>f(x) > 0.</equation>

<equation>\textcircled{2}</equation>若存在<equation>x_0</equation>的一个去心邻域，在该邻域内<equation>f(x) > 0</equation>且<equation>\lim_{x\to x_0}f(x)</equation>存在，则<equation>\lim_{x\to x_0}f(x)\geqslant 0.</equation>


设在<equation>x_0</equation>的某个去心邻域内恒有<equation>g(x)\leqslant f(x)\leqslant h(x)</equation>，且<equation>\lim_{x\to x_0}g(x) = \lim_{x\to x_0}h(x) = A</equation>，则<equation>\lim_{x\to x_0}f(x) = A.</equation>

同理，若存在<equation>M > 0</equation>，使得<equation>|x| > M</equation>时，恒有<equation>g(x)\leqslant f(x)\leqslant h(x)</equation>，且<equation>\lim_{x\to \infty}g(x) = \lim_{x\to \infty}h(x) = A</equation>，则<equation>\lim_{x\to \infty}f(x) = A.</equation>


单调有界数列（函数）必有极限


(1)<equation>\lim_{x\to 0}\frac{\sin x}{x}=1.</equation>

(2)<equation>\lim_{x\to 0}(1+x)^{\frac{1}{x}}=\mathrm{e}.</equation>

---

设<equation>\lim_{x\to x_1}f(x)\stackrel{\text{存在}}{=}A,\lim_{x\to x_1}g(x)\stackrel{\text{存在}}{=}B</equation>，则

<equation>\textcircled{2}</equation><equation>\lim_{x\to x_0}[f(x)g(x)]=A\cdot B.</equation>

<equation>\textcircled{3} \lim_{x \to x_-} \frac{f(x)}{g(x)} = \frac{A}{B}</equation><equation>(B \neq 0).</equation>

(2) 一些特殊情形下的运算结论

<equation>\textcircled{1}</equation>若<equation>\lim_{x\to x}f(x) = +\infty ,\lim_{x\to x}g(x) = +\infty</equation>，则

<equation>\lim _ {x \rightarrow x _ {0}} [ f (x) + g (x) ] = + \infty .</equation>

<equation>\textcircled{2}</equation>若<equation>\lim_{x\to x_0}f(x) = -\infty ,\lim_{x\to x_0}g(x) = -\infty</equation>，则

<equation>\lim _ {x \rightarrow x _ {1}} [ f (x) + g (x) ] = - \infty .</equation>

<equation>\textcircled{3}</equation>若<equation>\lim_{x\to x_{0}}f(x)=0,g(x)</equation>在<equation>x_{0}</equation>的某个去心邻域内有界，则

<equation>\lim _ {x \rightarrow x _ {1}} [ f (x) g (x) ] = 0.</equation>

<equation>\textcircled{4}</equation>若<equation>\lim_{x\to x_{0}}f(x)=\infty</equation>，g(x)在<equation>x_{0}</equation>的某个去心邻域内有界，则

<equation>\lim _ {x \rightarrow x _ {0}} [ f (x) \pm g (x) ] = \infty .</equation>

<equation>\textcircled{5}</equation>若<equation>\lim_{x\to x_0}f(x)\stackrel{\text{存在}}{=}A\neq 0,\lim_{x\to x_0}g(x)=0</equation>，则

<equation>\lim _ {x \rightarrow x _ {0}} \frac {f (x)}{g (x)} = \infty .</equation>

---


#### 4. 无穷小量的比较


如果<equation>\lim_{x\to x_{0}}f(x)=0</equation>，则称函数 f(x)是<equation>x\to x_{0}</equation>时的无穷小量.


<equation>\textcircled{1}</equation>有限多个无穷小量的和、差、积仍然是无穷小量.

<equation>\textcircled{2}</equation>有界函数与无穷小量的乘积还是无穷小量.


<equation>\lim_{x\to x_0}f(x) = A</equation>的充分必要条件为<equation>f(x) = A + \alpha (x)</equation>其中<equation>\lim_{x\to x_0}\alpha (x) = 0.</equation>


设<equation>\alpha (x),\beta (x)</equation>是同一自变量变化过程中的无穷小量，<equation>\beta (x)\neq 0</equation>，且<equation>\lim \frac{\alpha (x)}{\beta (x)}</equation>也是此变化过程中的极限，则

<equation>\textcircled{1}</equation>若<equation>\lim \frac{\alpha (x)}{\beta (x)} = C (C</equation>为常数，且<equation>C\neq 0)</equation>，则称<equation>\alpha (x)</equation>与<equation>\beta (x)</equation>为同阶无穷小量；

<equation>\textcircled{2}</equation>若<equation>\lim \frac{\alpha(x)}{\beta(x)} = 1</equation>，则称<equation>\alpha(x)</equation>与<equation>\beta(x)</equation>为等价无穷小量，记作<equation>\alpha(x)\sim \beta(x)</equation>；

---


#### 7. 无穷大量的定义


<equation>\textcircled{3}</equation>若<equation>\lim\frac{\alpha (x)}{\beta (x)}=0</equation>，则称<equation>\alpha (x)</equation>是比<equation>\beta (x)</equation>高阶的无穷小量，记作<equation>\alpha (x)=o(\beta (x))</equation>；

<equation>\textcircled{4}</equation>若<equation>\lim\frac{\alpha (x)}{\beta (x)}=\infty</equation>，则称<equation>\alpha (x)</equation>是比<equation>\beta (x)</equation>低阶的无穷小量.


设<equation>\alpha (x),\beta (x),\tilde{\alpha}(x),\tilde{\beta}(x)</equation>都是同一自变量变化过程中的无穷小量，且<equation>\alpha (x)\sim \tilde{\alpha}(x),\beta (x)\sim \tilde{\beta}(x)</equation>，则

<equation>\begin{array}{l} \lim \frac {\alpha (x) f (x)}{\beta (x) g (x)} = \lim \frac {\tilde {\alpha} (x) f (x)}{\beta (x) g (x)} = \lim \frac {\alpha (x) f (x)}{\tilde {\beta} (x) g (x)} \\ = \lim \frac {\tilde {\alpha} (x) f (x)}{\tilde {\beta} (x) g (x)}. \\ \end{array}</equation>


设<equation>\alpha ,\beta</equation>都是同一自变量变化过程中的无穷小量，若存在<equation>k > 0</equation>，使得<equation>\lim \frac{\alpha}{\beta^k} = C(C</equation>为非零的常数），则称在同一自变量变化过程中<equation>\alpha</equation>是<equation>\beta</equation>的<equation>k</equation>阶无穷小量.


任给<equation>M > 0</equation>，存在正数<equation>\delta</equation>，当<equation>0 < |x - x_0| < \delta</equation>时，恒有<equation>|f(x)| > M</equation>，则称<equation>x\to x_0</equation>时<equation>f(x)</equation>是无穷大量，记为<equation>\lim_{x\to x_0} f(x) = \infty</equation>.

---


#### (2)左、右连续的定义


在自变量的同一变化过程中，如果<equation>f(x)</equation>为无穷大量，则<equation>\frac{1}{f(x)}</equation>为无穷小量；反之，如果<equation>f(x)</equation>为无穷小量，且<equation>f(x)\neq 0</equation>，则<equation>\frac{1}{f(x)}</equation>为无穷大量.


(1) 连续的定义

<equation>\textcircled{1}</equation>设函数<equation>f(x)</equation>在点<equation>x_{0}</equation>的某个邻域内有定义，若

<equation>\lim _ {\Delta x \rightarrow 0} \Delta y = \lim _ {\Delta x \rightarrow 0} \left[ f \left(x _ {0} + \Delta x\right) - f \left(x _ {0}\right)\right] = 0,</equation>

则称<equation>f(x)</equation>在点<equation>x_{0}</equation>处连续.

<equation>\textcircled{2}</equation>设函数<equation>f(x)</equation>在点<equation>x_{0}</equation>的某个邻域内有定义，若

<equation>\lim _ {x \rightarrow x _ {0}} f (x) = f \left(x _ {0}\right),</equation>

则称<equation>f ( x )</equation>在点<equation>x_{0}</equation>处连续.


设<equation>f ( x )</equation>在点<equation>x_{0}</equation>的左侧（或右侧）某邻域（包括点<equation>x_{0}</equation>）有定义，并且

<equation>\lim _ {x \rightarrow x _ {0}} f (x) = f \left(x _ {0}\right),</equation>

则称<equation>f ( x )</equation>在点<equation>x_{0}</equation>处左连续（或右连续）.

函数<equation>f(x)</equation>在点<equation>x_{0}</equation>处连续的充要条件是<equation>f(x)</equation>在点

---


#### (2) 间断点的分类


<equation>x_{0}</equation>处既左连续又右连续


若函数<equation>f(x), g(x)</equation>在点<equation>x_0</equation>处连续，则<equation>f(x)\pm g(x), f(x)\cdot g(x), \frac{f(x)}{g(x)} (g(x_0)\neq 0)</equation>在点<equation>x_0</equation>处也连续.


若函数<equation>u = \varphi (x)</equation>在点<equation>x_0</equation>处连续，函数<equation>y = f(u)</equation>在点<equation>u_0 = \varphi (x_0)</equation>处连续，则函数<equation>y = f[\varphi (x)]</equation>在点<equation>x_0</equation>处连续.


设函数<equation>y = f(x)</equation>在区间<equation>(a,b)</equation>内为单调的连续函数，其值域为<equation>(m,n)</equation>，则其反函数<equation>x = f^{-1}(y)</equation>在区间<equation>(m,n)</equation>内也是连续的.

一切初等函数在其定义区间内都是连续的.


若函数<equation>f(x)</equation>在点<equation>x_{0}</equation>的任何邻域内总有异于<equation>x_{0}</equation>而属于函数<equation>f(x)</equation>定义域内的点，且函数<equation>f(x)</equation>在点<equation>x_{0}</equation>处不连续，则称<equation>x_{0}</equation>是<equation>f(x)</equation>的一个间断点.


左、右极限都存在的间断点称为第一类间断点.其

---


#### (3)零点定理


中，左、右极限都存在且相等的间断点称为可去间断点；左、右极限都存在且不相等的间断点称为跳跃间断点.

左、右极限至少有一个不存在的间断点称为第二类间断点. 若<equation>x\to x_0^{-}</equation>或<equation>x\to x_0^{+}</equation>时，<equation>f(x)\rightarrow \infty</equation>，则称<equation>x_0</equation>为<equation>f(x)</equation>的无穷间断点.


如果函数<equation>f(x)</equation>在闭区间<equation>[a,b]</equation>上连续，则在该区间上至少存在两点<equation>x_{1}, x_{2}</equation>，使得对于任意的<equation>x \in [a,b]</equation>，恒有<equation>f(x_{1}) \leqslant f(x) \leqslant f(x_{2})</equation>。


如果函数<equation>f(x)</equation>在闭区间<equation>[a,b]</equation>上连续，<equation>m,M</equation>是<equation>f(x)</equation>在该区间上的最小值与最大值，则对任意的<equation>\mu \in [m,M]</equation>在<equation>[a,b]</equation>上至少存在一点<equation>\xi</equation>，满足<equation>f(\xi) = \mu</equation>


如果<equation>f(x)</equation>在闭区间<equation>[a,b]</equation>上连续，且满足<equation>f(a)\cdot f(b) < 0</equation>，则在开区间（a,b）内至少存在一点<equation>\xi</equation>，使得<equation>f(\xi) = 0.</equation>

---


### 第二章 一元函数微分学

#### 一、导数与微分


1. 导数的定义式

<equation>\begin{array}{l} f ^ {\prime} \left(x _ {0}\right) = \frac {\mathrm {d} y}{\mathrm {d} x} \Bigg | _ {x = x _ {0}} = \lim _ {\Delta x \rightarrow 0} \frac {f \left(x _ {0} + \Delta x\right) - f \left(x _ {0}\right)}{\Delta x} \\ = \lim _ {x \rightarrow x _ {0}} \frac {f (x) - f \left(x _ {0}\right)}{x - x _ {0}}. \\ \end{array}</equation>

2. 微分的定义式

若<equation>\Delta y = A\Delta x + o(\Delta x)</equation>，则<equation>\mathrm{d}y = A\Delta x.</equation>

3. 可微的充要条件

可导<equation>\Leftrightarrow</equation>可微，<equation>\mathrm{d}y = f^{\prime}(x)\mathrm{d}x.</equation>

4. 可导与连续的关系

<equation>f(x)</equation>在<equation>x_{0}</equation>点可导<equation>\Rightarrow f(x)</equation>在<equation>x_{0}</equation>点处连续.

5. 可导、可微、连续等的关系

可微<equation>\Leftrightarrow</equation>可导<equation>\Rightarrow</equation>函数连续<equation>\Rightarrow \lim_{x\to x_0} f(x)</equation>存在<equation>\Rightarrow f(x)</equation>在<equation>x_0</equation>点的某邻域内有界.

---


#### 1. 基本初等函数的导数公式


<equation>\textcircled{1}</equation><equation>( C )^{\prime}=0</equation>（C为常数）；

<equation>\textcircled{2}</equation><equation>( x^{a} )^{\prime}=\alpha x^{a-1}</equation>（<equation>\alpha</equation>为实数）；

<equation>\textcircled{3}</equation><equation>( a^{x} )^{\prime}=a^{x} \ln a</equation><equation>( a>0,a\neq1)</equation>

<equation>\textcircled{4} \left( \mathrm{e}^{x} \right)^{\prime}=\mathrm{e}^{x};</equation>

<equation>\textcircled{5}</equation><equation>(\log_{a} x)^{\prime} = \frac{1}{x \ln a}</equation>（<equation>a > 0,a\neq 1</equation>）；

<equation>\textcircled{6}</equation><equation>(\ln x)^{\prime}=\frac{1}{x};</equation>

<equation>\textcircled{7}</equation><equation>(\sin x)^{\prime}=\cos x;</equation>

<equation>\textcircled{8}</equation><equation>(\cos x)^{\prime}=-\sin x;</equation>

<equation>\textcircled{9}</equation><equation>(\tan x)^{\prime}=\frac{1}{\cos^{2} x}</equation>;

<equation>\textcircled{1 0} \left( \cot x \right)^{\prime}=-\frac{1}{\sin^{2} x};</equation>

<equation>\textcircled{11}</equation><equation>(\sec x)^{\prime}=\sec x\tan x;</equation>

<equation>\textcircled{12} (\csc x)^{\prime} = -\csc x\cot x;</equation>

<equation>\textcircled{1 3}</equation><equation>\operatorname{a r c s i n} x )^{\prime}=\frac{1}{\sqrt{1-x^{2}}}</equation>

<equation>\textcircled{14} (\arccos x)^{\prime} = -\frac{1}{\sqrt{1-x^{2}}}</equation>;
