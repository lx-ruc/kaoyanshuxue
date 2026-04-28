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

**2025年第10题 | 选择题 | 5分 | 答案: D**
10. 设3阶矩阵 A,B满足<equation>r( A B)=r( B A)+1</equation>，则（    )

A. 方程组<equation>( A+B) x=0</equation>只有零解

B. 方程组<equation>A x=0</equation>与方程组<equation>B x=0</equation>均只有零解

C. 方程组<equation>A x=0</equation>与方程组<equation>B x=0</equation>没有公共非零解

D. 方程组<equation>A B A x=0</equation>与方程组<equation>B A B x=0</equation>有公共非零
答案: D
**解析: **解 若矩阵 A,B 中有一个为可逆矩阵，则<equation>r(AB)=r(BA)=\min \{r(A),r(B)\}</equation>，这与<equation>r(AB)</equation><equation>= r(BA) + 1</equation>矛盾.同理，若矩阵 A,B 中有一个为零矩阵，则<equation>r(AB)=r(BA)=0</equation>，这也与<equation>r(AB)</equation><equation>= r(BA) + 1</equation>矛盾.由此可得，<equation>1\leqslant r(A),r(B)\leqslant 2.</equation>进一步可得方程组<equation>Ax=0</equation>与方程组<equation>Bx=0</equation>均有非零解.选项B不正确.

由<equation>1 \leqslant r(A), r(B) \leqslant 2</equation>可得<equation>r(AB) \leqslant 2, r(BA) \leqslant 2.</equation>由<equation>r(\mathbf{AB}) = r(\mathbf{BA}) + 1</equation>可得，<equation>\left\{ \begin{array}{l l} r(\mathbf{AB}) = 2, \\ r(\mathbf{BA}) = 1 \end{array} \right.</equation>或<equation>\left\{ \begin{array}{l l} r(\mathbf{AB}) = 1, \\ r(\mathbf{BA}) = 0. \end{array} \right.</equation>若<equation>\left\{ \begin{array}{l l} r ( A B ) = 1, \\ r ( B A ) = 0, \end{array} \right.</equation>则<equation>A B A=B A B=O</equation>方程组ABAx=0与方程组BABx=0的解均为全体3维列向量，从而存在公共非零解.

若<equation>\left\{ \begin{array}{l} r(AB) = 2, \\ r(BA) = 1, \end{array} \right.</equation>则<equation>r(ABA) \leqslant \min \{r(A), r(BA)\} = 1, r(BAB) \leqslant \min \{r(B), r(BA)\} = 1,</equation>从而<equation>r(ABA) + r(BAB) \leqslant 2 < 3.</equation>考虑方程组<equation>\left\{ \begin{array}{l l} A B A x = 0, \\ B A B x = 0. \end{array} \right.</equation>下面我们证明<equation>r \binom {A B A}{B A B} < 3.</equation><equation>\begin{aligned} r \binom {A B A} {B A B} &= r \left(\left(\mathrm {A B A}\right) ^ {\mathrm {T}}, \left(\mathrm {B A B}\right) ^ {\mathrm {T}}\right) \leqslant r \left(\left(\mathrm {A B A}\right) ^ {\mathrm {T}}\right) + r \left(\left(\mathrm {B A B}\right) ^ {\mathrm {T}}\right) \\ &= r \left(\mathrm {A B A}\right) + r \left(\mathrm {B A B}\right) < 3. \end{aligned}</equation>由于方程组<equation>\left\{\begin{array}{l l} A B A x=0, \\ B A B x=0 \end{array} \right.</equation>的系数矩阵的秩小于3，故该方程组有非零解，从而方程组<equation>A B A x=0</equation>与方程组<equation>B A B x=0</equation>有公共非零解.选项D正确.

因此，应选D.

下面我们说明选项A、C不正确.

注意到若方程组<equation>A x=0</equation>与方程组<equation>B x=0</equation>有公共非零解，则该非零解也是方程组（<equation>A+B ) x= 0</equation>的解.

取<equation>A=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right), B=\left( \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>，则<equation>A B=\left( \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right), B A=\left( \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>，满足<equation>r( A B)=</equation><equation>r( B A )+1</equation>，但（0，0，1）<equation>^{\mathrm{T}}</equation>是方程组<equation>A x=0</equation>与<equation>B x=0</equation>的公共非零解，也是方程组（A+B）x=0的非零解.

---

**2025年第16题 | 填空题 | 5分**
16. 设矩阵<equation>A=\left( \alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4}\right)</equation>，若<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关，且<equation>\alpha_{1}+\alpha_{2}=\alpha_{3}+\alpha_{4}</equation>，则方程组<equation>A x=\alpha_{1}+4 \alpha_{4}</equation>的通解为 x=
**答案: **<equation>k \left( \begin{array}{c} 1 \\ 1 \\ - 1 \\ - 1 \end{array} \right) + \left( \begin{array}{c} 1 \\ 0 \\ 0 \\ 4 \end{array} \right)</equation>
**解析: **解 由于<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关，故<equation>r(A)\geqslant 3.</equation>又因为<equation>\alpha_{1} + \alpha_{2} = \alpha_{3} + \alpha_{4}</equation>，所以<equation>\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4}</equation>线性相关，从而<equation>r(A)\leqslant 3.</equation>由此可得<equation>r(A) = 3</equation>，进一步可得方程组<equation>Ax = 0</equation>的基础解系中仅包含4-3=1个向量.

由<equation>\alpha_{1}+\alpha_{2}=\alpha_{3}+\alpha_{4}</equation>可得<equation>\alpha_{1}+\alpha_{2}-\alpha_{3}-\alpha_{4}=0</equation>即<equation>\left( \alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4}\right)\left( \begin{array}{c}1\\ 1\\ -1\\ -1 \end{array}\right)=0</equation>于是<equation>\left( \begin{array}{c}1\\ 1\\ -1\\ -1 \end{array}\right)</equation>是方

程组<equation>Ax = 0</equation>的一个解，且构成<equation>Ax = 0</equation>的一个基础解系.

由于<equation>A\left( \begin{array}{c}1\\ 0\\ 0\\ 4 \end{array} \right)=(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4})\left( \begin{array}{c}1\\ 0\\ 0\\ 4 \end{array} \right)=\alpha_{1}+4\alpha_{4}</equation>，故<equation>\left( \begin{array}{c}1\\ 0\\ 0\\ 4 \end{array} \right)</equation>是方程组<equation>Ax = \alpha_{1} + 4\alpha_{4}</equation>的一个特解.

因此，方程组<equation>A x=\alpha_{1}+4 \alpha_{4}</equation>的通解为<equation>k ( 1,1,-1,-1 )^{\mathrm{T}}+(1,0,0,4)^{\mathrm{T}}</equation>，其中 k为任意常数.

---

**2023年第16题 | 填空题 | 5分**
16. 已知线性方程组<equation>\left\{ \begin{array}{l l} a x _ {1} + x _ {3} = 1 \\ x _ {1} + a x _ {2} + x _ {3} = 0 \\ x _ {1} + 2 x _ {2} + a x _ {3} = 0 \\ a x _ {1} + b x _ {2} = 2 \end{array} \right. \mathrm {有 解}, \mathrm {其 中} a, b \mathrm {为 常 数}, \mathrm {若} \left| \begin{array}{c c c} a & 0 & 1 \\ 1 & a & 1 \\ 1 & 2 & a \end{array} \right| = 4, \mathrm {则} \left| \begin{array}{c c c} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right| = \underline {{\quad}}.</equation>
**解析: **解（法一）记方程组<equation>\left\{ \begin{array}{l l} a x_{1}+x_{3}=1, \\ x_{1}+a x_{2}+x_{3}=0, \\ x_{1}+2 x_{2}+a x_{3}=0, \\ a x_{1}+b x_{2}=2 \end{array} \right.</equation>的系数矩阵为A，增广矩阵为（A,b），则<equation>(\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} a & 0 & 1 & 1 \\ 1 & a & 1 & 0 \\ 1 & 2 & a & 0 \\ a & b & 0 & 2 \end{array} \right).</equation>由方程组有解可知<equation>r ( A )=r ( A , b ).</equation>因为A为<equation>4\times 3</equation>矩阵，所以<equation>r ( A )\leqslant 3</equation>从而<equation>r ( A )=r ( A , b )\leqslant 3</equation>进一步可得<equation>| A,b|=0.</equation>于是，<equation>0 = \left| \begin{array}{c c c c} a & 0 & 1 & 1 \\ 1 & a & 1 & 0 \\ 1 & 2 & a & 0 \\ a & b & 0 & 2 \end{array} \right| \xlongequal {\text {按 第四 列 展开}} - \left| \begin{array}{c c c} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right| + 2 \left| \begin{array}{c c c} a & 0 & 1 \\ 1 & a & 1 \\ 1 & 2 & a \end{array} \right| = - \left| \begin{array}{c c c} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right| + 8.</equation>因此，<equation>\left| \begin{array}{c c c} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right|=8.</equation>（法二）记方程组<equation>\left\{ \begin{array}{l l} a x_{1}+x_{3}=1, \\ x_{1}+a x_{2}+x_{3}=0, \\ x_{1}+2 x_{2}+a x_{3}=0, \\ a x_{1}+b x_{2}=2 \end{array} \right.</equation>的系数矩阵为 A，增广矩阵为（A,b）.由方程组有解可知<equation>r ( \mathbf{A})=r ( \mathbf{A},\mathbf{b})</equation>注意到<equation>\left| \begin{array}{c c c} a & 0 & 1 \\ 1 & a & 1 \\ 1 & 2 & a \end{array} \right|=4</equation>为 A的一个3阶非零子式，故<equation>r ( \mathbf{A})\geqslant 3.</equation>又因为 A为<equation>4 \times 3</equation>矩阵，所以<equation>r ( \mathbf{A})\leqslant 3</equation>从而<equation>r ( \mathbf{A})=3.</equation>由<equation>r ( A )=r ( A , b )</equation>可得，<equation>r ( A , b )=3</equation>.于是<equation>r ( A )=r ( A , b )=3</equation>，该方程组有唯一解.

考虑方程组 I：<equation>\left\{\begin{array}{l l} a x_{1}+x_{3}=1, \\ x_{1}+a x_{2}+x_{3}=0, \\ x_{1}+2 x_{2}+a x_{3}=0 \end{array} \right.</equation>，和方程组Ⅱ：<equation>\left\{\begin{array}{l l} x_{1}+a x_{2}+x_{3}=0, \\ x_{1}+2 x_{2}+a x_{3}=0, \\ a x_{1}+b x_{2}=2. \end{array} \right.</equation>，由原方程组有唯一解

可知方程组 I和方程组Ⅱ有唯一公共解.

由于方程组Ⅰ的系数矩阵行列式等于4，故由克拉默法则知其仅有唯一解，进一步可得其增广矩阵的秩为3，行向量组线性无关。由此可知方程组Ⅱ的增广矩阵<equation>\left( \begin{array}{c c c c} {1} & {a} & {1} & {0} \\ {1} & {2} & {a} & {0} \\ {a} & {b} & {0} & {2} \end{array} \right)</equation>的前两行线性无关。又因为该增广矩阵的第三行为（a,b，0，2），最后一个元素非零，所以第三行与前两行线性无关。于是，方程组Ⅱ的增广矩阵的秩为3。由方程组Ⅱ有解可知，其系数矩阵的秩也为3，从而行列式非零.

记该公共解为<equation>\left( x_{1}, x_{2}, x_{3}\right)^{\mathrm{T}}</equation><equation>\left| \begin{array}{lll} a & 0 & 1 \\ 1 & a & 1 \\ 1 & 2 & a \end{array} \right|=A_{1}=4</equation><equation>\left| \begin{array}{lll} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right|=A_{2}\neq0.</equation>对方程组 I 使用克拉默法则可得<equation>x_{1}=\frac{\left| \begin{array}{lll} 1 & 0 & 1 \\ 0 & a & 1 \\ 0 & 2 & a \end{array} \right|}{A_{1}}=\frac{\left| \begin{array}{lll} 1 & 0 & 1 \\ 0 & a & 1 \\ 0 & 2 & a \end{array} \right|}{4}</equation>，对方程组Ⅱ使用克拉默法则可得<equation>x_{1}=\frac{\left| \begin{array}{lll} 0 & a & 1 \\ 0 & 2 & a \\ 2 & b & 0 \end{array} \right|}{A_{2}}.</equation>由此可得<equation>x _ {1} = \frac {\left| \begin{array}{c c} a & 1 \\ 2 & a \end{array} \right|}{4} = \frac {2 \left| \begin{array}{c c} a & 1 \\ 2 & a \end{array} \right|}{A _ {2}}.</equation>若<equation>\left| \begin{array}{ll} a & 1 \\ 2 & a \end{array} \right|=0</equation>，则 a =<equation>\pm \sqrt{2}</equation>.但将 a =<equation>\pm \sqrt{2}</equation>代入<equation>\left| \begin{array}{lll} a & 0 & 1 \\ 1 & a & 1 \\ 1 & 2 & a \end{array} \right|</equation>所得行列式并不等于4，故<equation>\left| \begin{array}{ll} a & 1 \\ 2 & a \end{array} \right| \neq</equation>0. 因此，由（1）式可得<equation>A_{2}=8</equation>，即<equation>\left| \begin{array}{lll} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right|=8.</equation>

---

**2022年第9题 | 选择题 | 5分 | 答案: D**
9. 设矩阵<equation>A=\left( \begin{array}{c c c} {1} & {1} & {1} \\ {1} & {a} & a^{2} \\ {1} & {b} & b^{2} \end{array} \right), b=\left( \begin{array}{c} {1} \\ {2} \\ {4} \end{array} \right),</equation>则线性方程组<equation>A x=b</equation>的解的情况为（    )

A. 无解 B. 有解 C. 有无穷多解或无解 D. 有唯一解或无解
答案: D
**解析: **解 （法一）注意到<equation>| A | = \left| \begin{array}{c c c} 1 & 1 & 1 \\ 1 & a & a ^ {2} \\ 1 & b & b ^ {2} \end{array} \right| = \left| \begin{array}{c c c} 1 & 1 & 1 \\ 1 & a & b \\ 1 & a ^ {2} & b ^ {2} \end{array} \right| = (b - a) (b - 1) (a - 1).</equation>当 a≠1,b≠1，且 a≠b时，<equation>|A| \neq 0.</equation>由克拉默法则可知，此时方程组<equation>A x=b</equation>有唯一解.

当 a=1时，<equation>(\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 2 \\ 1 & b & b ^ {2} & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 0 & 0 & 0 & 1 \\ 1 & b & b ^ {2} & 4 \end{array} \right).</equation><equation>r ( \mathbf{A}, \mathbf{b} ) \neq r ( \mathbf{A} )</equation>，方程组无解.同理可得，当<equation>b=1</equation>时，<equation>r ( \mathbf{A}, \mathbf{b} ) \neq r ( \mathbf{A} )</equation>，方程组无解.

当 a = b时，<equation>(\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 1 & a & a ^ {2} & 2 \\ 1 & b & b ^ {2} & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 1 & a & a ^ {2} & 2 \\ 0 & 0 & 0 & 2 \end{array} \right).</equation><equation>r ( \mathbf{A}, \mathbf{b}) \neq r (\mathbf{A})</equation>，方程组无解.

综上所述，方程组<equation>A x=b</equation>的解的情况只有两种可能，有唯一解或无解.应选D.

（法二）直接对增广矩阵（A,b）作初等行变换.<equation>(\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 1 & a & a ^ {2} & 2 \\ 1 & b & b ^ {2} & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 0 & a - 1 & a ^ {2} - 1 & 1 \\ 0 & b - 1 & b ^ {2} - 1 & 3 \end{array} \right).</equation>当 a = b = 1时，<equation>r ( \mathbf{A} )=1, r ( \mathbf{A}, \mathbf{b} )=2</equation>，方程组无解.

当<equation>a = 1,b\neq 1</equation>或<equation>a\neq 1,b = 1</equation>时，<equation>r(A) = 2,r(A,b) = 3</equation>，方程组无解.

当 a = b，但均不等于1时，<equation>r(\mathbf{A})=2,r(\mathbf{A},\mathbf{b})=3</equation>，方程组无解.

当<equation>a\neq 1,b\neq 1</equation>，且<equation>a\neq b</equation>时，<equation>r(A) = r(A,b) = 3.</equation>方程组有唯一解.

综上所述，方程组<equation>A x=b</equation>的解的情况只有两种可能，有唯一解或无解.应选D.

---

**2021年第9题 | 选择题 | 5分 | 答案: D**
9. 设3阶矩阵<equation>A=(\alpha_{1},\alpha_{2},\alpha_{3}),B=(\beta_{1},\beta_{2},\beta_{3})</equation>，若向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>可以由向量组<equation>\beta_{1},\beta_{2},\beta_{3}</equation>线性表示，则（    )

A.<equation>A x=0</equation>的解均为<equation>B x=0</equation>解 B.<equation>A^{\mathrm{T}} x=0</equation>的解均为<equation>B^{\mathrm{T}} x=0</equation>解

C.<equation>B x=0</equation>的解均为<equation>A x=0</equation>解 D.<equation>B^{\mathrm{T}} x=0</equation>的解均为<equation>A^{\mathrm{T}} x=0</equation>解
答案: D
**解析: **解（法一）由已知条件可知 A的列向量组可由 B的列向量组线性表示，故<equation>A^{\mathrm{T}}</equation>的行向量组可由<equation>B^{\mathrm{T}}</equation>的行向量组线性表示.若<equation>x_{0}</equation>为<equation>B^{\mathrm{T}} x=0</equation>的解，则<equation>x_{0}</equation>与<equation>B^{\mathrm{T}}</equation>的行向量均正交，从而与<equation>A^{\mathrm{T}}</equation>的行向量均正交.根据分析中的结论，可得<equation>A^{\mathrm{T}} x_{0}=0.</equation>因此，<equation>\mathbf{B}^{\mathrm{T}}\mathbf{x}=\mathbf{0}</equation>的解均为<equation>\mathbf{A}^{\mathrm{T}}\mathbf{x}=\mathbf{0}</equation>的解.应选D.

（法二）由于向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>可由向量组<equation>\beta_{1},\beta_{2},\beta_{3}</equation>线性表示，故存在矩阵<equation>P</equation>，使得<equation>A = BP</equation>由<equation>A=B P</equation>可得<equation>A^{\mathrm{T}}=P^{\mathrm{T}}B^{\mathrm{T}}</equation>.于是，若<equation>B^{\mathrm{T}}x=0</equation>，则<equation>A^{\mathrm{T}}x=P^{\mathrm{T}}B^{\mathrm{T}}x=P^{\mathrm{T}}(B^{\mathrm{T}}x)=0</equation>，即<equation>B^{\mathrm{T}}x=0</equation>的解均为<equation>A^{\mathrm{T}}x=0</equation>的解.

因此，应选D.

---

**2018年第23题 | 解答题 | 11分**
23. （本题满分11分）

已知 a是常数，且矩阵<equation>A=\left( \begin{array}{c c c}1&2&a\\ 1&3&0\\ 2&7&-a \end{array} \right)</equation>可经初等列变换化为矩阵<equation>B=\left( \begin{array}{c c c}1&a&2\\ 0&1&1\\ -1&1&1 \end{array} \right).</equation>I. 求 a;

II. 求满足<equation>A P=B</equation>的可逆矩阵<equation>P.</equation>
**答案: **(I)<equation>a=2;</equation>（Ⅱ）满足<equation>A P=B</equation>的可逆矩阵为<equation>\boldsymbol {P} = \left( \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right),</equation>其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数，且<equation>k_{2} \neq k_{3}</equation>.
**解析: **解（I）由于 A可经初等列变换化为 B，故矩阵方程 AX=B有解.于是，<equation>r(A)=r(A,B).</equation>对（A,B）作初等行变换.<equation>\begin{array}{l} (A, B) = \left( \begin{array}{c c c c c c} 1 & 2 & a & 1 & a & 2 \\ 1 & 3 & 0 & 0 & 1 & 1 \\ 2 & 7 & - a & - 1 & 1 & 1 \end{array} \right) \xrightarrow [ r _ {3} - 2 r _ {1} ]{r _ {2} - r _ {1}} \left( \begin{array}{c c c c c c} 1 & 2 & a & 1 & a & 2 \\ 0 & 1 & - a & - 1 & 1 - a & - 1 \\ 0 & 3 & - 3 a & - 3 & 1 - 2 a & - 3 \end{array} \right) \\ \xrightarrow [ r _ {3} ^ {*} - 3 r _ {2} ^ {*} ]{r _ {1} - 2 r _ {2} ^ {*}} \left( \begin{array}{c c c c c c} 1 & 0 & 3 a & 3 & 3 a - 2 & 4 \\ 0 & 1 & - a & - 1 & 1 - a & - 1 \\ 0 & 0 & 0 & 0 & a - 2 & 0 \end{array} \right). \\ \end{array}</equation>当且仅当 a = 2时，<equation>r(\mathbf{A})=r(\mathbf{A},\mathbf{B})=2.</equation>或者，由矩阵<equation>A</equation>可经初等列变换化为矩阵<equation>B</equation>可知，<equation>A</equation>的列秩等于<equation>B</equation>的列秩，从而<equation>r(A) = r(B)</equation>.同上面的计算可知<equation>r(A) = 2</equation>，当且仅当<equation>a = 2</equation>时，<equation>r(A) = r(B)</equation>.

因此，<equation>a=2.</equation>（Ⅱ）当 a=2时，<equation>(\boldsymbol {A}, \boldsymbol {B}) \rightarrow \left(\begin{array}{c c c c c c}1&0&6&3&4&4\\0&1&- 2&- 1&- 1&- 1\\0&0&0&0&0&0\end{array}\right).</equation><equation>A X=B</equation>等价于<equation>\left( \begin{array}{c c c} 1 & 0 & 6 \\ 0 & 1 & -2 \\ 0 & 0 & 0 \end{array} \right) X=\left( \begin{array}{c c c} 3 & 4 & 4 \\ -1 & -1 & -1 \\ 0 & 0 & 0 \end{array} \right).</equation>记<equation>\left( \begin{array}{c c c} 1 & 0 & 6 \\ 0 & 1 & -2 \\ 0 & 0 & 0 \end{array} \right)=A^{\prime}.</equation>方程组<equation>A^{\prime} x=0</equation>的一个基础解系为<equation>(-6,2,1)^{\mathrm{T}}.</equation>于是，方程组<equation>A^{\prime} x=(3,-1,0)^{\mathrm{T}}</equation>的通解为<equation>x_{1}=k_{1}(-6,2,1)^{\mathrm{T}}+</equation><equation>(3,-1,0)^{\mathrm{T}}</equation>其中<equation>k_{1}</equation>为任意常数；方程组<equation>A^{\prime} x=(4,-1,0)^{\mathrm{T}}</equation>的通解为<equation>x_{2}=k_{2}(-6,2,1)^{\mathrm{T}}+</equation><equation>(4,-1,0)^{\mathrm{T}}</equation>其中<equation>k_{2}</equation>为任意常数；方程组<equation>A^{\prime} x=(4,-1,0)^{\mathrm{T}}</equation>的通解为<equation>x_{3}=k_{3}(-6,2,1)^{\mathrm{T}}+</equation><equation>(4,-1,0)^{\mathrm{T}}</equation>其中<equation>k_{3}</equation>为任意常数.

因此，矩阵方程 AX=B的通解为<equation>\boldsymbol {X} = \left( \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right),</equation>其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数.

若可逆矩阵 P满足 AP=B，则<equation>\boldsymbol {P} = \left( \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right),</equation>且<equation>| P | \neq 0.</equation>由于<equation>| P | = \left| \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right| = \left| \begin{array}{c c c} 0 & 1 & 1 \\ - 1 & - 1 & - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right| = \left| \begin{array}{c c c} 0 & 1 & 1 \\ - 1 & 0 & 0 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right| = k _ {3} - k _ {2},</equation>故当<equation>k_{2}\neq k_{3}</equation>时，P可逆.

因此，满足 AP=B的可逆矩阵为<equation>\boldsymbol {P} = \left( \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right),</equation>其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数，且<equation>k_{2} \neq k_{3}</equation>.

---

**2017年第22题 | 解答题 | 11分**
22. (本题满分11分)

设3阶矩阵<equation>A=(\alpha_{1},\alpha_{2},\alpha_{3})</equation>有3个不同的特征值，且<equation>\alpha_{3}=\alpha_{1}+2\alpha_{2}</equation>I. 证明<equation>r(A)=2;</equation>II. 若<equation>\beta=\alpha_{1}+\alpha_{2}+\alpha_{3}</equation>，求方程组<equation>A x=\beta</equation>的通解.
**答案: **（I）证明略；

（Ⅱ）<equation>k ( 1, 2, - 1 )^{\mathrm{T}}+( 1, 1, 1 )^{\mathrm{T}}</equation>为线性方程组<equation>A x=\beta</equation>的通解，其中 k为任意常数.
**解析: **解（I）（法一）由于 A有3个不同的特征值<equation>\lambda_{1},\lambda_{2},\lambda_{3}</equation>，故 A相似于对角矩阵，且至多仅有一个零特征值.该对角矩阵的秩<equation>\geqslant 2</equation>，于是<equation>r(A)\geqslant 2.</equation>又因为<equation>\boldsymbol{\alpha}_{3}=\boldsymbol{\alpha}_{1}+2\boldsymbol{\alpha}_{2}</equation>，所以<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性相关，<equation>|A|=0.</equation>由于<equation>| A| = \lambda_{1}\lambda_{2}\lambda_{3}</equation>，故A有一个特征值为零.

因此，<equation>r ( A ) = 2.</equation>（法二）也可以如下证明0是A的一个特征值.

由<equation>\boldsymbol{\alpha}_{3}=\boldsymbol{\alpha}_{1}+2\boldsymbol{\alpha}_{2}</equation>知<equation>\left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) \left( \begin{array}{c} 1 \\ 2 \\ - 1 \end{array} \right) = \mathbf {0} = 0 \left( \begin{array}{c} 1 \\ 2 \\ - 1 \end{array} \right).</equation>于是，0是 A的一个特征值，<equation>( 1, 2, - 1 )^{\mathrm{T}}</equation>是 A的属于特征值0的一个特征向量.

其余同法一.

（Ⅱ）考虑<equation>A x=0</equation>. 由于<equation>r(A)=2</equation>，故<equation>A x=0</equation>的基础解系中只包含一个向量. 又因为<equation>\alpha_{3}=\alpha_{1}+2\alpha_{2}</equation>，所以<equation>\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)\left(1,2,-1\right)^{\mathrm{T}}=0</equation>，即<equation>\left(1,2,-1\right)^{\mathrm{T}}</equation>是该齐次线性方程组的一个基础解系.

由于<equation>\beta = \alpha_{1} + \alpha_{2} + \alpha_{3}</equation>，即<equation>(\alpha_{1},\alpha_{2},\alpha_{3}) (1,1,1)^{\mathrm{T}} = \beta</equation>，故<equation>(1,1,1)^{\mathrm{T}}</equation>是<equation>A x = \beta</equation>的一个特解.

因此，<equation>k ( 1, 2, - 1 )^{\mathrm{T}}+( 1, 1, 1 )^{\mathrm{T}}</equation>为线性方程组<equation>A x=\beta</equation>的通解，其中k为任意常数.

---

**2016年第22题 | 解答题 | 11分**
22. （本题满分11分）

设矩阵<equation>A = \left( \begin{array}{c c c} 1 & 1 & 1 - a \\ 1 & 0 & a \\ a + 1 & 1 & a + 1 \end{array} \right),\beta = \left( \begin{array}{c} 0 \\ 1 \\ 2a - 2 \end{array} \right),</equation>且方程组<equation>A x=\beta</equation>无解.

I. 求 a的值；

II. 求方程组<equation>A^{\mathrm{T}} A x=A^{\mathrm{T}} \beta</equation>的通解.
**答案: **（ I ）<equation>a=0;</equation>（ II ）<equation>k(0,-1,1)^{\mathrm{T}}+(1,-2,0)^{\mathrm{T}}</equation>，其中 k为任意常数.
**解析: **解（I）由于<equation>A x=\beta</equation>无解，故由非齐次线性方程组有解的充分必要条件可知，<equation>r(A,\beta)\neq r(A).</equation><equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c} 1 & 1 & 1 - a & 0 \\ 1 & 0 & a & 1 \\ a + 1 & 1 & a + 1 & 2 a - 2 \end{array} \right) \xrightarrow {r _ {2} - r _ {1}} \frac {r _ {2} - r _ {1}}{r _ {3} - (a + 1) r _ {1}} \left( \begin{array}{c c c c} 1 & 1 & 1 - a & 0 \\ 0 & - 1 & 2 a - 1 & 1 \\ 0 & - a & a ^ {2} + a & 2 a - 2 \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} \times (- 1)} \left( \begin{array}{c c c c} 1 & 1 & 1 - a & 0 \\ 0 & 1 & 1 - 2 a & - 1 \\ 0 & - a & a ^ {2} + a & 2 a - 2 \end{array} \right) \xrightarrow {r _ {1} - r _ {2} ^ {* *}} \left( \begin{array}{c c c c} 1 & 0 & a & 1 \\ 0 & 1 & 1 - 2 a & - 1 \\ 0 & 0 & - a ^ {2} + 2 a & a - 2 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个 *.）

由上面的式子可知，<equation>r ( A ) \geqslant 2</equation>. 从而，<equation>A x=\beta</equation>无解当且仅当<equation>r ( A )=2</equation>且<equation>r ( A,\beta)=3.</equation>此时，<equation>- a^{2}+2 a=0</equation>，且 a-2<equation>\neq0</equation>，解得 a=0.

（Ⅱ）当<equation>a = 0</equation>时，<equation>A^{\mathrm{T}} = \left( \begin{array}{lll}1&1&1\\ 1&0&1\\ 1&0&1 \end{array} \right), A^{\mathrm{T}}A = \left( \begin{array}{lll}3&2&2\\ 2&2&2\\ 2&2&2 \end{array} \right), A^{\mathrm{T}}\boldsymbol {\beta} = \left( \begin{array}{c}-1\\ -2\\ -2 \end{array} \right).</equation><equation>\begin{array}{l} \left(\boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {A}, \boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {\beta}\right) = \left( \begin{array}{c c c c} 3 & 2 & 2 & - 1 \\ 2 & 2 & 2 & - 2 \\ 2 & 2 & 2 & - 2 \end{array} \right) \xrightarrow [ r _ {2} \times \frac {1}{2} ]{r _ {3} - r _ {2}} \left( \begin{array}{c c c c} 3 & 2 & 2 & - 1 \\ 1 & 1 & 1 & - 1 \\ 0 & 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {1} - 2 r _ {2} ^ {*} ]{r _ {1} - 2 r _ {2} ^ {*}} \left( \begin{array}{c c c c} 1 & 0 & 0 & 1 \\ 1 & 1 & 1 & - 1 \\ 0 & 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} - r _ {1} ^ {*}} \left( \begin{array}{c c c c} 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & - 2 \\ 0 & 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation><equation>A^{\mathrm{T}} A x=A^{\mathrm{T}} \beta</equation>对应的齐次线性方程组等价于<equation>\left\{ \begin{array}{l l} x_{1}=0, \\ x_{2}+x_{3}=0. \end{array} \right.</equation>（0，-1，1）<equation>^{\mathrm{T}}</equation>为该方程组的一个基础解系.又因为<equation>(1,-2,0)^{\mathrm{T}}</equation>是<equation>A^{\mathrm{T}} A x=A^{\mathrm{T}} \beta</equation>的一个特解，所以<equation>A^{\mathrm{T}} A x=A^{\mathrm{T}} \beta</equation>的通解为<equation>k(0,-1,1)^{\mathrm{T}}+</equation>（1，-2，0）<equation>^{\mathrm{T}}</equation>，其中k为任意常数.

---

**2015年第7题 | 选择题 | 4分 | 答案: D**
7. 设矩阵<equation>A=\left( \begin{array}{c c c} {1} & {1} & {1} \\ {1} & {2} & {a} \\ {1} & {4} & {a^{2}} \\ \end{array} \right), b=\left( \begin{array}{c} {1} \\ {d} \\ {d^{2}} \\ \end{array} \right).</equation>若集合<equation>\Omega=\{1,2\}</equation>，则线性方程组<equation>A x=b</equation>有无穷多解的充分必要条件为（    ）

A. a<equation>\notin\Omega, d\notin\Omega</equation>B. a<equation>\notin\Omega, d\in\Omega</equation>C. a<equation>\in\Omega, d\notin\Omega</equation>D. a<equation>\in\Omega, d\in\Omega</equation>
答案: D
**解析: **解（法一）当 a<equation>\in\Omega</equation>，d<equation>\in\Omega</equation>时，r（A）=r（A，b）=2<3，故 a<equation>\in\Omega</equation>，d<equation>\in\Omega</equation>是 Ax=b有无穷多解的充分条件.

当<equation>A x=b</equation>有无穷多解时，<equation>r(A)=r(A,b)<3</equation>，从而<equation>r(A)<3</equation><equation>|A|=0</equation>.由于<equation>|A|</equation>为范德蒙德行列式，故<equation>|A|=0</equation>当且仅当 a=1或 a=2，即 a<equation>\in\Omega</equation>.此时，若<equation>r(A,b)=r(A)<3</equation>，则<equation>(1,d,d^{2})^{\mathrm{T}}</equation>与<equation>(1,1,1)^{\mathrm{T}}</equation>和<equation>(1,2,4)^{\mathrm{T}}</equation>线性相关，从而<equation>\left| \begin{array}{c c c} {1} & {1} & {1} \\ {1} & {2} & {d} \\ {1} & {4} & {d^{2}} \end{array} \right|=0</equation>.再次由范德蒙德行列式的性质可推出 d=1或 d=2，即 d<equation>\in\Omega.</equation>因此，<equation>a\in \Omega</equation>，<equation>d\in \Omega</equation>是<equation>Ax = b</equation>有无穷多解的充分必要条件.应选D.

（法二）对（A，b）作初等行变换.<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 1 & 2 & a & d \\ 1 & 4 & a ^ {2} & d ^ {2} \end{array} \right) \xrightarrow [ r _ {3} - r _ {1} ]{r _ {2} - r _ {1}} \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 0 & 1 & a - 1 & d - 1 \\ 0 & 3 & a ^ {2} - 1 & d ^ {2} - 1 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {*} - 3 r _ {2} ^ {*}} \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 0 & 1 & a - 1 & d - 1 \\ 0 & 0 & a ^ {2} - 3 a + 2 & d ^ {2} - 3 d + 2 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每作一次初等行变换，加一个<equation>*.</equation>）

由此可见，<equation>r(\mathbf{A}) = r(\mathbf{A},\mathbf{b}) < 3</equation>当且仅当<equation>a^{2} - 3a + 2 = 0</equation>且<equation>d^{2} - 3d + 2 = 0</equation>，即<equation>a = 1</equation>或<equation>a = 2</equation>且<equation>d = 1</equation>或<equation>d = 2</equation>，也即<equation>a\in \Omega</equation>，<equation>d\in \Omega</equation>因此，<equation>a\in \Omega</equation>，<equation>d\in \Omega</equation>是<equation>Ax = b</equation>有无穷多解的充分必要条件.应选D.

（法三）排除法.我们可以把简单的值代入各选项，然后根据<equation>A x=b</equation>是否有无穷多解来排除错误选项.

选项A：代入<equation>a=0</equation>，<equation>d=0</equation>，<equation>r(\mathbf{A})=r(\mathbf{A},\mathbf{b})=3</equation>，不符合题意.

选项B：代入<equation>a=0</equation><equation>d\in\{1,2\}</equation><equation>r(A)=r(A,b)=3</equation>，不符合题意.

选项C：代入<equation>a\in\{1,2\}</equation>，<equation>d=0</equation>，<equation>r(\mathbf{A},\mathbf{b})=3</equation>，<equation>r(\mathbf{A})=2</equation>，不符合题意.

由上可见，选项A、B、C均不是正确选项.由排除法知，应选D.

---

**2014年第22题 | 解答题 | 11分**
22. （本题满分11分）

设矩阵<equation>A = \left( \begin{array}{c c c c} 1 & -2 & 3 & -4 \\ 0 & 1 & -1 & 1 \\ 1 & 2 & 0 & -3 \end{array} \right), E</equation>为3阶单位矩阵.

I. 求方程组<equation>A x=0</equation>的一个基础解系；

II. 求满足<equation>A B=E</equation>的所有矩阵 B.
**答案: **(22) ( I )<equation>(-1, 2, 3, 1)^{\mathrm{T}};</equation><equation>(\mathrm {I I}) \boldsymbol {B} = \left( \begin{array}{c c c} 2 - k _ {1} & 6 - k _ {2} & - 1 - k _ {3} \\ - 1 + 2 k _ {1} & - 3 + 2 k _ {2} & 1 + 2 k _ {3} \\ - 1 + 3 k _ {1} & - 4 + 3 k _ {2} & 1 + 3 k _ {3} \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right), \text {其 中} k _ {1}, k _ {2}, k _ {3} \text {为 任 意 常 数}</equation>
**解析: **解（I）考察系数矩阵 A.<equation>\begin{array}{l} \boldsymbol {A} = \left( \begin{array}{c c c c} 1 & - 2 & 3 & - 4 \\ 0 & 1 & - 1 & 1 \\ 1 & 2 & 0 & - 3 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c c} 1 & - 2 & 3 & - 4 \\ 0 & 1 & - 1 & 1 \\ 0 & 4 & - 3 & 1 \end{array} \right) \xrightarrow {r _ {1} + 2 r _ {2}} \left( \begin{array}{c c c c} 1 & 0 & 1 & - 2 \\ 0 & 1 & - 1 & 1 \\ 0 & 0 & 1 & - 3 \end{array} \right) \\ \xrightarrow {r _ {1} ^ {*} - r _ {3} ^ {* *}} \frac {1}{r _ {2} + r _ {3} ^ {* *}} \left( \begin{array}{c c c c} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & - 2 \\ 0 & 0 & 1 & - 3 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每作一次初等行变换，加一个 *.）<equation>Ax = 0</equation>可化为方程组<equation>\left\{ \begin{array}{l} x_{1} + x_{4} = 0, \\ x_{2} - 2x_{4} = 0, \\ x_{3} - 3x_{4} = 0. \end{array} \right.</equation>由此可得<equation>\xi = (-1,2,3,1)^{\mathrm{T}}</equation>为<equation>Ax = 0</equation>的一个基础解系.

（Ⅱ）实际上我们要求的是三个非齐次线性方程组<equation>A x=(1,0,0)^{\mathrm{T}}</equation>，<equation>A x=(0,1,0)^{\mathrm{T}}</equation>，<equation>A x=(0,0,1)^{\mathrm{T}}</equation>的解.由于它们的系数矩阵都是A，故可考虑对（A，E）作初等行变换，同第（I）问中的步骤可得<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {E}) = \left( \begin{array}{c c c c c c c} 1 & - 2 & 3 & - 4 & 1 & 0 & 0 \\ 0 & 1 & - 1 & 1 & 0 & 1 & 0 \\ 1 & 2 & 0 & - 3 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c c c c c} 1 & - 2 & 3 & - 4 & 1 & 0 & 0 \\ 0 & 1 & - 1 & 1 & 0 & 1 & 0 \\ 0 & 4 & - 3 & 1 & - 1 & 0 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} + 2 r _ {2}} \frac {r _ {1} ^ {*} - 4 r _ {2}}{r _ {3} ^ {*} - 4 r _ {2}} \left( \begin{array}{c c c c c c c} 1 & 0 & 1 & - 2 & 1 & 2 & 0 \\ 0 & 1 & - 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & 1 & - 3 & - 1 & - 4 & 1 \end{array} \right) \xrightarrow {r _ {1} ^ {*} - r _ {3} ^ {* *}} \left( \begin{array}{c c c c c c c} 1 & 0 & 0 & 1 & 2 & 6 & - 1 \\ 0 & 1 & 0 & - 2 & - 1 & - 3 & 1 \\ 0 & 0 & 1 & - 3 & - 1 & - 4 & 1 \end{array} \right). \\ \end{array}</equation>由于<equation>\mathbf{A}</equation>为<equation>3\times4</equation>矩阵，<equation>\mathbf{E}</equation>为3阶单位矩阵，<equation>\mathbf{B}</equation>应为<equation>4\times3</equation>矩阵，从而知，<equation>(2,-1,-1,0)^{\mathrm{T}}</equation><equation>(6,-3,-4,0)^{\mathrm{T}}</equation><equation>(-1,1,1,0)^{\mathrm{T}}</equation>分别为<equation>A x=(1,0,0)^{\mathrm{T}}</equation><equation>A x=(0,1,0)^{\mathrm{T}}</equation><equation>A x=(0,0,1)^{\mathrm{T}}</equation>的一个特解.

与第（I）问中<equation>A x=0</equation>的通解相结合，得到<equation>A x=(1,0,0)^{\mathrm{T}}</equation><equation>A x=(0,1,0)^{\mathrm{T}}</equation><equation>A x=(0,0,1)^{\mathrm{T}}</equation>的通解分别为<equation>\boldsymbol {\alpha} _ {1} = k _ {1} \left(- 1, 2, 3, 1\right) ^ {\mathrm {T}} + \left(2, - 1, - 1, 0\right) ^ {\mathrm {T}},</equation><equation>\boldsymbol {\alpha} _ {2} = k _ {2} \left(- 1, 2, 3, 1\right) ^ {\mathrm {T}} + \left(6, - 3, - 4, 0\right) ^ {\mathrm {T}},</equation><equation>\boldsymbol {\alpha} _ {3} = k _ {3} (- 1, 2, 3, 1) ^ {\mathrm {T}} + (- 1, 1, 1, 0) ^ {\mathrm {T}},</equation>其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数.

因此，<equation>B = \left( \begin{array}{c c c} 2 - k_1 & 6 - k_2 & -1 - k_3 \\ -1 + 2k_1 & -3 + 2k_2 & 1 + 2k_3 \\ -1 + 3k_1 & -4 + 3k_2 & 1 + 3k_3 \\ k_1 & k_2 & k_3 \end{array} \right)</equation>，其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数.

---

**2013年第22题 | 解答题 | 11分**
22. (本题满分11分)

设<equation>A = \left( \begin{array}{c c} 1 & a \\ 1 & 0 \end{array} \right), B = \left( \begin{array}{c c} 0 & 1 \\ 1 & b \end{array} \right).</equation>当<equation>a,b</equation>为何值时，存在矩阵<equation>C</equation>使得<equation>AC - CA = B</equation>，并求所有矩阵<equation>C</equation>
**答案: **(22)<equation>a=-1,b=0</equation>时，<equation>C=\left( \begin{array}{c c} k_{1}+k_{2}+1 & -k_{2} \\ k_{2} & k_{1} \end{array} \right)</equation>其中<equation>k_{1},k_{2}</equation>为任意常数.
**解析: **解（法一）设<equation>C=\left( \begin{array}{cc}x_{1}&x_{2}\\ x_{3}&x_{4}\end{array} \right)</equation>，则由AC-CA=B可得<equation>\binom {1} {1} \begin{array}{l l} a \\ 0 \end{array} \binom {x _ {1}} {x _ {3}} \begin{array}{l l} x _ {2} \\ x _ {4} \end{array} - \binom {x _ {1}} {x _ {3}} \begin{array}{l l} x _ {2} \\ x _ {4} \end{array} \binom {1} {1} \begin{array}{l l} a \\ 0 \end{array} = \binom {0} {1} \binom {1} {b}.</equation>写成线性方程组的形式：<equation>\left\{ \begin{array}{l} - x _ {2} + a x _ {3} = 0, \\ - a x _ {1} + x _ {2} + a x _ {4} = 1, \\ x _ {1} - x _ {3} - x _ {4} = 1, \\ x _ {2} - a x _ {3} = b. \end{array} \right.</equation>记该线性方程组为<equation>Px = \beta ,\beta = (0,1,1,b)^{\mathrm{T}}</equation>，则<equation>Px = \beta</equation>有解当且仅当<equation>r(P,\beta) = r(P)</equation>.<equation>\begin{array}{l} (P, \beta) = \left( \begin{array}{c c c c c} 0 & - 1 & a & 0 & 0 \\ - a & 1 & 0 & a & 1 \\ 1 & 0 & - 1 & - 1 & 1 \\ 0 & 1 & - a & 0 & b \end{array} \right) \xrightarrow {r _ {2} + a r _ {3}} \left( \begin{array}{c c c c c} 0 & - 1 & a & 0 & 0 \\ 0 & 1 & - a & 0 & a + 1 \\ 1 & 0 & - 1 & - 1 & 1 \\ 0 & 1 & - a & 0 & b \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} + r _ {1}} \left( \begin{array}{c c c c c} 0 & - 1 & a & 0 & 0 \\ 0 & 0 & 0 & 0 & a + 1 \\ 1 & 0 & - 1 & - 1 & 1 \\ 0 & 0 & 0 & 0 & b \end{array} \right) \rightarrow \left( \begin{array}{c c c c c} 1 & 0 & - 1 & - 1 & 1 \\ 0 & 1 & - a & 0 & 0 \\ 0 & 0 & 0 & 0 & a + 1 \\ 0 & 0 & 0 & 0 & b \end{array} \right). \\ \end{array}</equation><equation>r_{2}^{*}</equation>表示对<equation>r_{2}</equation>作初等行变换后所得新的第二行.由上可见，若<equation>r ( \boldsymbol{P}, \boldsymbol{\beta})=r ( \boldsymbol{P})</equation>，则必有<equation>a+1=b=0</equation>从而<equation>a=-1,b=0.</equation>当 a = -1，b = 0时，<equation>(\boldsymbol {P}, \boldsymbol {\beta}) \rightarrow \left(\begin{array}{c c c c c}1&0&- 1&- 1&1\\0&1&1&0&0\\0&0&0&0&0\\0&0&0&0&0\end{array}\right),</equation>即<equation>\left\{ \begin{array}{l l} x_{2}+x_{3}=0, \\ x_{1}-x_{3}-x_{4}=1. \end{array} \right.</equation>（1，0，0，1）<equation>^{\mathrm{T}}</equation>和（1，-1，1，0）<equation>^{\mathrm{T}}</equation>为该方程组对应的齐次线性方程组的一个基础解系.又（1，0，0，0）<equation>^{\mathrm{T}}</equation>为<equation>P x=\beta</equation>的一个特解，故<equation>P x=\beta</equation>的通解为<equation>k _ {1} \left(1, 0, 0, 1\right) ^ {\mathrm {T}} + k _ {2} \left(1, - 1, 1, 0\right) ^ {\mathrm {T}} + \left(1, 0, 0, 0\right) ^ {\mathrm {T}},</equation>其中<equation>k_{1}, k_{2}</equation>为任意常数.

因此，当<equation>a = -1</equation>，<equation>b = 0</equation>时，存在C使得AC-CA=B.此时的C形如<equation>\left( \begin{array}{c c} k_{1}+k_{2}+1 & -k_{2} \\ k_{2} & k_{1} \end{array} \right)</equation>其中<equation>k_{1}, k_{2}</equation>为任意常数.

（法二）由于AC的迹等于CA的迹，故AC-CA的迹等于零.因此 b=0. B =<equation>\left( \begin{array}{c c} 0 & 1 \\ 1 & 0 \end{array} \right).</equation>设 C =<equation>\left( \begin{array}{c c} x_{1} & x_{2} \\ x_{3} & x_{4} \end{array} \right)</equation>，则由 AC-CA=B可得<equation>\left\{ \begin{array}{l} - x _ {2} + a x _ {3} = 0, \\ - a x _ {1} + x _ {2} + a x _ {4} = 1, \\ x _ {1} - x _ {3} - x _ {4} = 1, \\ x _ {2} - a x _ {3} = 0. \end{array} \right.</equation>将<equation>x_{2}=a x_{3}</equation>代入<equation>- a x_{1}+x_{2}+a x_{4}=1</equation>可得<equation>- a \left(x_{1}-x_{3}-x_{4}\right)=1.</equation>与<equation>x_{1}-x_{3}-x_{4}=1</equation>比较得，<equation>a=-1.</equation>从而<equation>a=-1</equation>，<equation>b=0.</equation>其余同法一.

---

**2012年第22题 | 解答题 | 11分**
22. （本题满分11分）

设<equation>\text {设} A = \left( \begin{array}{c c c c} 1 & a & 0 & 0 \\ 0 & 1 & a & 0 \\ 0 & 0 & 1 & a \\ a & 0 & 0 & 1 \end{array} \right), \beta = \left( \begin{array}{c} 1 \\ - 1 \\ 0 \\ 0 \end{array} \right).</equation>I. 计算行列式<equation>|A|</equation>;

II. 当实数<equation>a</equation>为何值时，方程组<equation>Ax = \beta</equation>有无穷多解，并求其通解.
**答案: **（22）（I）<equation>| A |=1-a^{4}</equation>；

（Ⅱ）当 a=-1时，方程组<equation>A x=\beta</equation>有无穷多解，其通解为<equation>k(1,1,1,1)^{\mathrm{T}}+(0,-1,0,0)^{\mathrm{T}}</equation>其中 k为任意常数.
**解析: **（I）按第一行展开<equation>|A|</equation>，得<equation>| \boldsymbol {A} | = \left| \begin{array}{c c c} 1 & a & 0 \\ 0 & 1 & a \\ 0 & 0 & 1 \end{array} \right| - a \left| \begin{array}{c c c} 0 & a & 0 \\ 0 & 1 & a \\ a & 0 & 1 \end{array} \right| = 1 - a ^ {4}.</equation>（Ⅱ）（法一）<equation>A x=\beta</equation>有无穷多解的充要条件为<equation>r(A)=r(A,\beta)<4.</equation>由<equation>r(A)<4</equation>可得，<equation>|A|=0</equation>从而<equation>a=\pm 1.</equation>当 a = 1时，<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 1 & 0 & 0 & 1 & 0 \end{array} \right) \xrightarrow {r _ {4} - r _ {1}} \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & - 1 & 0 & 1 & - 1 \end{array} \right) \xrightarrow {r _ {4} ^ {*} + r _ {2}} \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1 & - 2 \end{array} \right) \\ \xrightarrow {r _ {4} ^ {* *} - r _ {3}} \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 & - 2 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每作一次初等行变换，加一个 *.）由上可知，<equation>r(\mathbf{A},\boldsymbol{\beta})=4</equation>，而<equation>r(\mathbf{A})=3</equation>，<equation>\mathbf{Ax}=\boldsymbol{\beta}</equation>无解. a=1不符合题意.

当 a = -1时，<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 1 & - 1 & 0 & 0 & 1 \\ 0 & 1 & - 1 & 0 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ - 1 & 0 & 0 & 1 & 0 \end{array} \right) \xrightarrow {r _ {4} + r _ {1}} \left( \begin{array}{c c c c c} 1 & - 1 & 0 & 0 & 1 \\ 0 & 1 & - 1 & 0 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ 0 & - 1 & 0 & 1 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} + r _ {2}} \frac {r _ {4} ^ {*} + r _ {2}} {r _ {4} ^ {*} + r _ {2}} \left( \begin{array}{c c c c c} 1 & 0 & - 1 & 0 & 0 \\ 0 & 1 & - 1 & 0 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ 0 & 0 & - 1 & 1 & 0 \end{array} \right) \xrightarrow {r _ {1} ^ {*} + r _ {3}} \frac {r _ {2} + r _ {3}}{r _ {4} ^ {* *} + r _ {3}} \left( \begin{array}{c c c c c} 1 & 0 & 0 & - 1 & 0 \\ 0 & 1 & 0 & - 1 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>由上可知，<equation>r(\mathbf{A},\boldsymbol{\beta})=r(\mathbf{A})=3<4, A\boldsymbol{x}=\boldsymbol{\beta}</equation>有无穷多解.

齐次方程<equation>A x=0</equation>的通解为<equation>k ( 1,1,1,1 )^{\mathrm{T}}</equation>，其中<equation>k</equation>为任意常数。又因为<equation>( 0,-1,0,0 )^{\mathrm{T}}</equation>为<equation>A x=\beta</equation>的一个特解，所以<equation>A x=\beta</equation>的通解为<equation>k ( 1,1,1,1 )^{\mathrm{T}}+( 0,-1,0,0 )^{\mathrm{T}}</equation>，其中<equation>k</equation>为任意常数综上所述，当<equation>a=-1</equation>时，方程组<equation>A x=\beta</equation>有无穷多解，其通解为<equation>k ( 1,1,1,1 )^{\mathrm{T}}+( 0,-1,0,0 )^{\mathrm{T}}</equation>其中<equation>k</equation>为任意常数.

（法二）对含有参数<equation>a</equation>的增广矩阵<equation>(A, \beta)</equation>作初等行变换.<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ a & 0 & 0 & 1 & 0 \end{array} \right) \xrightarrow {r _ {4} - a r _ {1}} \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ 0 & - a ^ {2} & 0 & 1 & - a \end{array} \right) \\ \xrightarrow {r _ {4} ^ {*} + a ^ {2} r _ {2}} \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ 0 & 0 & a ^ {3} & 1 & - a - a ^ {2} \end{array} \right) \xrightarrow {r _ {4} ^ {* *} - a ^ {3} r _ {3}} \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ 0 & 0 & 0 & 1 - a ^ {4} & - a - a ^ {2} \end{array} \right). \\ \end{array}</equation>由于<equation>A x=\beta</equation>有无穷多解，故<equation>r(A)=r(A,\beta)<4.</equation>因此，<equation>1-a^{4}=0,-a-a^{2}=0</equation>解得 a=-1其余同法一.

---

**2010年第22题 | 解答题 | 11分**
22. (本题满分11分)

设<equation>A=\left( \begin{array}{c c c} \lambda & 1 & 1 \\ 0 & \lambda-1 & 0 \\ 1 & 1 & \lambda \end{array} \right), b=\left( \begin{array}{c} a \\ 1 \\ 1 \end{array} \right).</equation>已知线性方程组<equation>A x=b</equation>存在两个不同的解.

I. 求<equation>\lambda, a;</equation>II. 求方程组<equation>A x=b</equation>的通解.
**答案: **(22) （I）<equation>\lambda=-1</equation><equation>a=-2;</equation>（Ⅱ）<equation>k(1,0,1)^{\mathrm{T}}+\left(\frac{3}{2},-\frac{1}{2},0\right)^{\mathrm{T}}</equation>为<equation>A x=b</equation>的通解，其中k为任意常数.