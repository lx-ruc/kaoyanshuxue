#### 矩阵的相似与相似对角化

**2025年第22题 | 解答题 | 12分**
22. （本题满分12分）

已知矩阵<equation>A = \left( \begin{array}{c c c} 4 & 1 & -2 \\ 1 & 1 & 1 \\ -2 & 1 & a \end{array} \right)</equation>与<equation>B = \left( \begin{array}{c c c} k & 0 & 0 \\ 0 & 6 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>合同.

I. 求 a的值及 k的范围.

II. 若存在正交矩阵<equation>Q</equation>，使得<equation>Q^{\mathrm{T}}AQ = B</equation>，求<equation>k</equation>及<equation>Q</equation>
**答案: **<equation>(1) a = 4, k > 0; (2) k = 3, Q = \left[ \begin{array}{c c c} \frac {1}{\sqrt {3}} & - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {6}} \\ \frac {1}{\sqrt {3}} & 0 & - \frac {2}{\sqrt {6}} \\ \frac {1}{\sqrt {3}} & \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {6}} \end{array} \right]</equation>
**解析: **解（I）由于矩阵A，B合同，故A，B的正、负特征值个数均相等。又因为B是对角矩阵，对角元为k，6，0，所以A也有零特征值，<equation>|A|=0.</equation>计算<equation>|A|</equation>可得<equation>| A | = \left| \begin{array}{c c c} 4 & 1 & - 2 \\ 1 & 1 & 1 \\ - 2 & 1 & a \end{array} \right| \frac {c _ {1} - c _ {2}}{c _ {3} - c _ {2}} \left| \begin{array}{c c c} 3 & 1 & - 3 \\ 0 & 1 & 0 \\ - 3 & 1 & a - 1 \end{array} \right| = (- 1) ^ {2 + 2} \cdot 1 \cdot \left| \begin{array}{c c} 3 & - 3 \\ - 3 & a - 1 \end{array} \right| = 3 (a - 4).</equation>由<equation>|A| = 0</equation>可得<equation>a = 4.</equation>于是，<equation>A = \left( \begin{array}{c c c} 4 & 1 & -2 \\ 1 & 1 & 1 \\ -2 & 1 & 4 \end{array} \right).</equation>计算 A的特征值.<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - 4 & - 1 & 2 \\ - 1 & \lambda - 1 & - 1 \\ 2 & - 1 & \lambda - 4  \right| \xlongequal {r _ {1} - r _ {3}} \left| \begin{array}{c c c} \lambda - 6 & 0 & 6 - \lambda \\ - 1 & \lambda - 1 & - 1 \\ 2 & - 1 & \lambda - 4  \right| \\ &= (\lambda - 6) \left| \begin{array}{c c c} 1 & 0 & - 1 \\ - 1 & \lambda - 1 & - 1 \\ 2 & - 1 & \lambda - 4  \right| \xlongequal {c _ {3} + c _ {1}} (\lambda - 6) \left| \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & \lambda - 1 & - 2 \\ 2 & - 1 & \lambda - 2  \right| \\ &= (\lambda - 6) \left(\lambda^ {2} - 3 \lambda\right) = \lambda (\lambda - 3) (\lambda - 6). \end{aligned}</equation>于是，<equation>A</equation>的特征值为3，6，0. A有两个正特征值，一个零特征值.

由 A,B的正、负特征值个数均相等可得，B也有两个正特征值.结合B的特征值为k,6,0可得， k的取值范围是（0，<equation>+\infty).</equation>（Ⅱ）若存在正交矩阵Q，使得<equation>Q^{\mathrm{T}}AQ=B</equation>，则A，B相似，从而A，B的特征值相同，由此可得 k=3. 由于B为对角矩阵，故满足<equation>Q^{\mathrm{T}}AQ=B</equation>的正交矩阵Q的列向量即A的单位正交化后的属于特征值3,6,0的特征向量.

分别计算<equation>A</equation>的属于特征值3,6,0的特征向量

考虑（3E-A）x=0.<equation>3 E - A = \left( \begin{array}{c c c} - 1 & - 1 & 2 \\ - 1 & 2 & - 1 \\ 2 & - 1 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} - 1 & - 1 & 2 \\ 0 & 3 & - 3 \\ 0 & - 3 & 3 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & - 2 \\ 0 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right).</equation><equation>\xi_{1} = \left( \begin{array}{c}1\\ 1\\ 1 \end{array} \right)</equation>为 A 的属于特征值3的一个线性无关的特征向量.

考虑（6E-A）x=0.<equation>6 E - A = \left( \begin{array}{c c c} 2 & - 1 & 2 \\ - 1 & 5 & - 1 \\ 2 & - 1 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 2 & - 1 & 2 \\ - 1 & 5 & - 1 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 0 & 9 & 0 \\ - 1 & 5 & - 1 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation><equation>\xi_{2} = \left( \begin{array}{c} - 1 \\ 0 \\ 1 \end{array} \right)</equation>为<equation>A</equation>的属于特征值6的一个线性无关的特征向量.

考虑（0E-A）x=0.<equation>- A = \left( \begin{array}{c c c} - 4 & - 1 & 2 \\ - 1 & - 1 & - 1 \\ 2 & - 1 & - 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 0 & 3 & 6 \\ 1 & 1 & 1 \\ 0 & - 3 & - 6 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{array} \right).</equation><equation>\xi_3 = \left( \begin{array}{c}1\\ -2\\ 1 \end{array} \right)</equation>为 A 的属于特征值0的一个线性无关的特征向量.

或者，由实对称矩阵属于不同特征值的特征向量相互正交可得，<equation>A</equation>的属于特征值0的特征向量<equation>\xi_{3}</equation>与<equation>\xi_{1},\xi_{2}</equation>均正交，即<equation>\xi_3^{\mathrm{T}}\xi_1 = 0,\xi_3^{\mathrm{T}}\xi_2 = 0.</equation>于是，<equation>\xi_{3} = (x_{1},x_{2},x_{3})^{\mathrm{T}}</equation>满足<equation>\left\{ \begin{array}{l}x_{1} + x_{2} + x_{3} = 0,\\ -x_{1} + x_{3} = 0, \end{array} \right.</equation>解得<equation>\left( \begin{array}{c}x_{1}\\ x_{2}\\ x_{3} \end{array} \right) = k\left( \begin{array}{c}1\\ -2\\ 1 \end{array} \right)</equation>，其中<equation>k</equation>为任意非零常数.

由于<equation>\xi_{1},\xi_{2},\xi_{3}</equation>已经相互正交，故只需将它们单位化即可得到 A的一组相互正交的单位特征向量.令<equation>Q = \left(\frac {\xi_ {1}}{\| \xi_ {1} \|}, \frac {\xi_ {2}}{\| \xi_ {2} \|}, \frac {\xi_ {3}}{\| \xi_ {3} \|}\right) = \left( \begin{array}{c c c} \frac {1}{\sqrt {3}} & - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {6}} \\ \frac {1}{\sqrt {3}} & 0 & - \frac {2}{\sqrt {6}} \\ \frac {1}{\sqrt {3}} & \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {6}} \end{array} \right),</equation>则<equation>Q^{\mathrm{T}} A Q=B, Q</equation>为所求矩阵

---

**2024年第10题 | 选择题 | 5分 | 答案: B**
10. 设 A,B为2阶矩阵，且<equation>A B=B A</equation>，则“ A有两个不相等的特征值”是“ B可对角化”的（    ）

A. 充分必要条件 B. 充分不必要条件

C. 必要不充分条件 D. 既不充分也不必要条件
答案: B
**解析: **解设<equation>\lambda_{1},\lambda_{2}</equation>是A的两个不同的特征值，非零向量<equation>\alpha_{1},\alpha_{2}</equation>满足<equation>A\alpha_{1} = \lambda_{1}\alpha_{1},A\alpha_{2} = \lambda_{2}\alpha_{2}</equation>.由于<equation>\lambda_{1}</equation><equation>\neq \lambda_{2}</equation>，故<equation>\alpha_{1},\alpha_{2}</equation>线性无关.进一步可得，<equation>AB\alpha_{1} = BA\alpha_{1} = \lambda_{1}B\alpha_{1},AB\alpha_{2} = BA\alpha_{2} = \lambda_{2}B\alpha_{2}</equation>.

（i）若<equation>B\alpha_{i}\neq 0(i = 1,2)</equation>，则<equation>B\alpha_{i}</equation>是A的属于<equation>\lambda_{i}</equation>的一个特征向量。又因为A有两个不同的特征值且为2阶矩阵，所以这两个特征值均只有一个线性无关的特征向量，从而<equation>B\alpha_{i} = k_{i}\alpha_{i}(k_{i}\neq 0)</equation>，<equation>\alpha_{i}</equation>是B的属于特征值<equation>k_{i}</equation>的一个特征向量.

（ii）若<equation>B\alpha_{i} = 0</equation>，则<equation>\alpha_{i}</equation>是B的属于特征值0的一个特征向量.

不论是哪种情况，<equation>\alpha_{i} ( i=1,2 )</equation>均为B的两个线性无关的特征向量，故B能相似对角化.因此，“A有两个不相等的特征值”是“B可对角化”的充分条件.

但是，“A有两个不相等的特征值”不是“B可对角化”的必要条件.取 A=B=E，则 AB= BA，且B是对角矩阵，但是A没有两个不同的特征值.

综上所述，“<equation>\mathbf{A}</equation>有两个不相等的特征值”是“<equation>\mathbf{B}</equation>可对角化”的充分不必要条件，应选B.

---

**2023年第22题 | 解答题 | 12分**
22. (本题满分12分)

设矩阵 A满足：对任意<equation>x_{1}, x_{2}, x_{3}</equation>均有<equation>A\left( \begin{array}{c} x_{1} \\ x_{2} \\ x_{3} \end{array} \right)=\left( \begin{array}{c} x_{1}+x_{2}+x_{3} \\ 2 x_{1}-x_{2}+x_{3} \\ x_{2}-x_{3} \end{array} \right)</equation>I. 求 A；

II. 求可逆矩阵<equation>P</equation>与对角矩阵<equation>\Lambda</equation>，使得<equation>P^{-1}AP = \Lambda</equation>
**答案: **<equation>\begin{aligned} (\mathrm {I}) \boldsymbol {A} &= \left( \begin{array}{c c c} 1 & 1 & 1 \\ 2 & - 1 & 1 \\ 0 & 1 & - 1  \right); \\ (\mathrm {I I}) \boldsymbol {P} &= \left( \begin{array}{c c c} 0 & - 1 & 4 \\ - 1 & 0 & 3 \\ 1 & 2 & 1  \right), \boldsymbol {A} &= \left( \begin{array}{c c c} - 2 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 2  \right). \end{aligned}</equation>
**解析: **（ I ）因为<equation>\begin{aligned} \mathbf {A} \left(  x _ {1} \\ x _ {2} \\ x _ {3}  \right) &= \left( \begin{array}{c} x _ {1} + x _ {2} + x _ {3} \\ 2 x _ {1} - x _ {2} + x _ {3} \\ x _ {2} - x _ {3}  \right) &= \left( \begin{array}{c c c} 1 & 1 & 1 \\ 2 & - 1 & 1 \\ 0 & 1 & - 1  \right) \left(  x _ {1} \\ x _ {2} \\ x _ {3}  \right) \end{aligned}</equation>对任意<equation>x_{1}, x_{2}, x_{3}</equation>均成立，所以方程组<equation>\left[ A-\left( \begin{array}{c c c} 1 & 1 & 1 \\ 2 & -1 & 1 \\ 0 & 1 & -1 \end{array} \right) \right] \left( \begin{array}{l} x_{1} \\ x_{2} \\ x_{3} \end{array} \right)=\mathbf{0}</equation>的解为全体3维列向量.于是该方程组的系数矩阵的秩为0，从而<equation>A-\left( \begin{array}{c c c} 1 & 1 & 1 \\ 2 & -1 & 1 \\ 0 & 1 & -1 \end{array} \right)=\mathbf{0}</equation>，即<equation>A=\left( \begin{array}{c c c} 1 & 1 & 1 \\ 2 & -1 & 1 \\ \end{array} \right).</equation>（Ⅱ）计算 A的特征值. A的特征多项式为<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - 1 & - 1 & - 1 \\ - 2 & \lambda + 1 & - 1 \\ 0 & - 1 & \lambda + 1  \right| \xlongequal {\text {按 第三 行 展开}} \left| \begin{array}{c c} \lambda - 1 & - 1 \\ - 2 & - 1  \right| + (\lambda + 1) \left| \begin{array}{c c} \lambda - 1 & - 1 \\ - 2 & \lambda + 1  \right| \\ &= - (\lambda + 1) + (\lambda + 1) \left(\lambda^ {2} - 3\right) = (\lambda + 1) \left(\lambda^ {2} - 4\right) \\ &= (\lambda + 1) (\lambda + 2) (\lambda - 2). \end{aligned}</equation>于是，A的特征值为-2，-1，2.

计算 A的属于特征值-2的特征向量.考虑方程组<equation>(-2 E-A) x=0.</equation><equation>- 2 E - A = \left( \begin{array}{c c c} - 3 & - 1 & - 1 \\ - 2 & - 1 & - 1 \\ 0 & - 1 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} - 3 & 0 & 0 \\ - 2 & 0 & 0 \\ 0 & 1 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>解方程组<equation>(-2 E-A) x=0</equation>可得<equation>\left( \begin{array}{c}0\\ -1\\ 1 \end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c}0\\ -1\\ 1 \end{array} \right)</equation>为A的属于特征值 -2的一个特征向量.

计算 A的属于特征值-1的特征向量.考虑方程组<equation>(- E-A) x=0.</equation><equation>- E - A = \left( \begin{array}{c c c} - 2 & - 1 & - 1 \\ - 2 & 0 & - 1 \\ 0 & - 1 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 2 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>解方程组<equation>(- E-A) x=0</equation>可得<equation>\left( \begin{array}{c}-1\\ 0\\ 2 \end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c}-1\\ 0\\ 2 \end{array} \right)</equation>为 A的属于特征值 1的一个特征向量.

计算 A的属于特征值2的特征向量.考虑方程组（2E-A）x=0.<equation>2 E - A = \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ - 2 & 3 & - 1 \\ 0 & - 1 & 3 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ 0 & 1 & - 3 \\ 0 & - 1 & 3 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & - 4 \\ 0 & 1 & - 3 \\ 0 & 0 & 0 \end{array} \right).</equation>解方程组<equation>( 2 E-A ) x=0</equation>可得<equation>\left( \begin{array}{c c c} 4 \\ 3 \\ 1 \end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c} 4 \\ 3 \\ 1 \end{array} \right)</equation>为A的属于特征值2的一个特征向量.

令<equation>P=\left( \begin{array}{c c c} 0 & -1 & 4 \\ -1 & 0 & 3 \\ 1 & 2 & 1 \end{array} \right).</equation>由于属于不同特征值的特征向量线性无关，故P的列向量组线性无关，从而P可逆.由特征向量的性质可得<equation>P^{-1} A P=A</equation>其中<equation>\Lambda=\left( \begin{array}{c c c} -2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>

---

**2022年第8题 | 选择题 | 5分 | 答案: B**
8. 设 A为3阶矩阵，<equation>\Lambda=\left( \begin{array}{c c c} {1} & {0} & {0} \\ {0} & {-1} & {0} \\ {0} & {0} & {0} \end{array} \right)</equation>，则 A的特征值为1，-1，0的充分必要条件是（    )

A. 存在可逆矩阵 P,Q，使得<equation>A=P\Lambda Q</equation>B. 存在可逆矩阵 P，使得<equation>A=P\Lambda P^{-1}</equation>C. 存在正交矩阵 Q，使得<equation>A=Q\Lambda Q^{-1}</equation>D. 存在可逆矩阵 P，使得<equation>A=P\Lambda P^{\mathrm{T}}</equation>
答案: B
**解析: **解3阶矩阵 A的特征值为1，-1，0意味着 A有3个不同的特征值，从而 A相似于与它具有相同特征值的对角矩阵，即<equation>\Lambda</equation>.于是，A的特征值为1，-1，0的充分必要条件即 A与<equation>\Lambda</equation>相似的充分必要条件.

选项B实际上为 A与<equation>\Lambda</equation>相似的定义，即存在可逆矩阵 P，使得<equation>\Lambda = P^{-1}AP</equation>，也即<equation>A=P\Lambda P^{-1}</equation>因此，应选B.

下面说明选项A、C、D不正确.

选项A是A与A等价的定义.若两矩阵相似，则它们必等价，但两个等价的矩阵不一定相似，如<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>和<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>，故选项A是A与A相似的必要不充分条件.

因为正交矩阵也是可逆矩阵，所以选项C是A与A相似的充分条件.但选项C并不是A与A相似的必要条件，因为A不一定能找到一组相互正交的特征向量，这一要求对实对称矩阵成立，对一般矩阵不成立.

取<equation>\boldsymbol{\xi}_{1}=\left( \begin{array}{c}1\\ 0\\ 0 \end{array} \right),\boldsymbol{\xi}_{2}=\left( \begin{array}{c}1\\ 1\\ 0 \end{array} \right),\boldsymbol{\xi}_{3}=\left( \begin{array}{c}1\\ 0\\ 1 \end{array} \right)</equation>，则<equation>\boldsymbol{\xi}_{1},\boldsymbol{\xi}_{2},\boldsymbol{\xi}_{3}</equation>相互均不正交.令<equation>P=(\boldsymbol{\xi}_{1},\boldsymbol{\xi}_{2},\boldsymbol{\xi}_{3})</equation>，<equation>\boldsymbol{A}=</equation><equation>\left( \begin{array}{c c c}1&0&0\\ 0&-1&0\\ 0&0&0 \end{array} \right)</equation>，则<equation>\boldsymbol {A} = \boldsymbol {P} \boldsymbol {\Lambda} \boldsymbol {P} ^ {- 1} = \left( \begin{array}{c c c} 1 & 1 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right) \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} 1 & - 2 & - 1 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>A与对角矩阵 A相似，但是 A的线性无关的特征向量均不正交.

选项D是A与A合同的定义.对一般矩阵而言，相似与合同之间并无相互蕴含的关系.

考虑选项A的反例<equation>\left( \begin{array}{c c c} {1} & {0} & {0} \\ {0} & {0} & {0} \\ {0} & {0} & {0} \end{array} \right)</equation>和<equation>\left( \begin{array}{c c c} {2} & {0} & {0} \\ {0} & {0} & {0} \\ {0} & {0} & {0} \end{array} \right)</equation>，这两个矩阵具有相同的正、负惯性指数，从而合同，但它们并不相似.

考虑选项C的反例<equation>A=\left( \begin{array}{c c c}1&0&0\\ 0&-1&0\\ 0&0&0 \end{array} \right), A=\left( \begin{array}{c c c}1&-2&-1\\ 0&-1&0\\ 0&0&0 \end{array} \right).</equation>由前面的分析可知，A与A相似又因为A是实对称矩阵，而与实对称矩阵合同的矩阵一定是实对称矩阵，但A不是实对称矩阵，所以A与A不合同.

因此，选项D既不是A与A相似的充分条件，也不是A与A相似的必要条件.

---

**2021年第22题 | 解答题 | 12分**
22. (本题满分12分)

设矩阵<equation>A = \left( \begin{array}{c c c} 2 & 1 & 0 \\ 1 & 2 & 0 \\ 1 & a & b \end{array} \right)</equation>仅有两个不同的特征值，若 A相似于对角矩阵，求 a,b的值，并求可逆矩阵 P，使得<equation>P^{-1} A P</equation>为对角矩阵.
**答案: **当<equation>a = 1,b = 1</equation>时，<equation>P = \left( \begin{array}{c c c} - 1 & 0 & 1 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right),P^{-1} A P = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 3 \end{array} \right)</equation>为对角矩阵；

当<equation>a = -1,b = 3</equation>时，<equation>P = \left( \begin{array}{c c c} 1 & 0 & -1 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right),P^{-1} A P = \left( \begin{array}{c c c} 3 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>为对角矩阵
**解析: **计算 A的特征多项式.<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - 2 & - 1 & 0 \\ - 1 & \lambda - 2 & 0 \\ - 1 & - a & \lambda - b  \right| \xlongequal {\text {按 第三 列 展 开}} (\lambda - b) \left| \begin{array}{c c} \lambda - 2 & - 1 \\ - 1 & \lambda - 2  \right| \\ &= (\lambda - b) \left[ (\lambda - 2) ^ {2} - 1 \right] = (\lambda - 1) (\lambda - 3) (\lambda - b). \end{aligned}</equation>A的所有特征值为1,3,b.

若 A仅有两个不同的特征值，则 b只可能为1或者3.

下面分情况讨论.

(1) 若 b=1，则 A的特征值为1，1，3.

计算 A的属于特征值1的特征向量.考虑 （E-A）x=0.<equation>\boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} - 1 & - 1 & 0 \\ - 1 & - 1 & 0 \\ - 1 & - a & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 - a & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>若 A可相似对角化，则方程组 （E-A）x=0有两个线性无关的解. r（E-A）=1.于是，a=1.

解方程组（<equation>E-A ) x=0</equation>可得<equation>\left( \begin{array}{c}-1\\1\\0\end{array} \right)</equation>与<equation>\left( \begin{array}{c}0\\0\\1\end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c}-1\\1\\0\end{array} \right)</equation>与<equation>\left( \begin{array}{c}0\\0\\1\end{array} \right)</equation>为 A的属于特征值1的两个线性无关的特征向量.

计算 A的属于特征值3的特征向量.考虑<equation>( 3 E-A ) x=0.</equation><equation>3 E - A = \left( \begin{array}{c c c} 1 & - 1 & 0 \\ - 1 & 1 & 0 \\ - 1 & - 1 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & - 1 & 0 \\ 0 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right).</equation>解方程组<equation>( 3 E-A ) x=0</equation>可得<equation>\left( \begin{array}{c} 1 \\ 1 \\ 1 \end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c} 1 \\ 1 \\ 1 \end{array} \right)</equation>为A的属于特征值3的一个特征向量.

令<equation>P=\left( \begin{array}{c c c} -1 & 0 & 1 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right)</equation>，则<equation>P^{-1} A P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 3 \end{array} \right)</equation>为对角矩阵.

(2) 若 b=3，则 A的特征值为1，3，3.

计算 A的属于特征值3的特征向量.考虑（<equation>3 E-A ) x=0.</equation><equation>3 E - A = \left( \begin{array}{c c c} 1 & - 1 & 0 \\ - 1 & 1 & 0 \\ - 1 & - a & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & - 1 & 0 \\ 0 & - 1 - a & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>若 A可相似对角化，则方程组<equation>( 3 E-A ) x=0</equation>有两个线性无关的解. r（3E-A）=1.于是，a=-1.解方程组<equation>( 3 E-A ) x=0</equation>可得<equation>\left( \begin{array}{l} 1 \\ 1 \\ 0 \end{array} \right)</equation>与<equation>\left( \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{l} 1 \\ 1 \\ 0 \end{array} \right)</equation>与<equation>\left( \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right)</equation>为 A的属于特征值3的两个线性无关的特征向量.

计算 A的属于特征值1的特征向量.考虑 （E-A）x=0.<equation>E - A = \left( \begin{array}{c c c} - 1 & - 1 & 0 \\ - 1 & - 1 & 0 \\ - 1 & 1 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right)</equation>解方程组<equation>( E-A ) x=0</equation>可得<equation>\left( \begin{array}{c}-1\\1\\1\end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c}-1\\1\\1\end{array} \right)</equation>为 A的属于特征值1的一个特征向量.

令<equation>P=\left( \begin{array}{c c c}1&0&-1\\1&0&1\\0&1&1\end{array} \right)</equation>，则<equation>P^{-1} A P=\left( \begin{array}{c c c}3&0&0\\0&3&0\\0&0&1\end{array} \right)</equation>为对角矩阵.

---

**2020年第23题 | 解答题 | 11分**
23. (本题满分11分)

设 A为2阶矩阵，<equation>P=(\alpha ,A\alpha)</equation>，其中<equation>\alpha</equation>是非零向量且不是 A的特征向量.

I. 证明 P为可逆矩阵

II. 若<equation>A^{2}\alpha+A\alpha-6\alpha=0</equation>.求<equation>P^{-1}AP</equation>，并判断 A是否相似于对角矩阵.
**答案: **（I）证明略；

（Ⅱ）<equation>P^{-1} A P=\left( \begin{array}{cc} 0 & 6 \\ 1 & -1 \end{array} \right), A</equation>相似于对角矩阵<equation>\left( \begin{array}{c c} 2 & 0 \\ 0 & -3 \end{array} \right).</equation>
**解析: **解（I）要证明 P为可逆矩阵，可证明<equation>\alpha, A\alpha</equation>线性无关.

假设<equation>\alpha, A\alpha</equation>线性相关，则存在不全为零的常数<equation>k_{1}, k_{2}</equation>，使得<equation>k_{1}\alpha+k_{2}A\alpha=0.</equation>若<equation>k_{2}=0</equation>，则<equation>k_{1}\alpha=0</equation>.但<equation>\alpha</equation>为非零向量，故<equation>k_{1}=0</equation>.这与假设矛盾.

若<equation>k_{2}\neq0</equation>，则<equation>A\alpha=-\frac{k_{1}}{k_{2}}\alpha.</equation>由特征向量的定义可知<equation>\alpha</equation>为A的特征向量.这与<equation>\alpha</equation>不是A的特征向量矛盾.

因此，<equation>\alpha, A\alpha</equation>线性无关.P为可逆矩阵.

（Ⅱ）考虑AP.<equation>\begin{aligned} A P &= \left(A \alpha , A ^ {2} \alpha\right) \xlongequal {A ^ {2} \alpha + A \alpha - 6 \alpha = 0} \left(A \alpha , 6 \alpha - A \alpha\right) = (\alpha , A \alpha) \left( \begin{array}{c c} 0 & 6 \\ 1 & - 1  \right) \\ &= P \left( \begin{array}{c c} 0 & 6 \\ 1 & - 1  \right). \end{aligned}</equation>由第（I）问可知，P可逆.上式两端同时左乘<equation>P^{-1}</equation>可得<equation>P^{-1} A P=\left( \begin{array}{cc}0&6\\ 1&-1 \end{array} \right).</equation>记<equation>B=\left( \begin{array}{cc}0&6\\ 1&-1 \end{array} \right)</equation>，则A与B相似.A与对角矩阵相似等价于B与对角矩阵相似.

计算 B的特征多项式.<equation>| \lambda E - B | = \left| \begin{array}{c c} \lambda & - 6 \\ - 1 & \lambda + 1 \end{array} \right| = \lambda^ {2} + \lambda - 6 = (\lambda + 3) (\lambda - 2).</equation>2与-3是B的两个不同特征值.于是，B相似于对角矩阵<equation>\left( \begin{array}{cc}2&0\\ 0&-3 \end{array} \right).</equation>由相似关系的传递性可知，A相似于对角矩阵<equation>\left( \begin{array}{cc}2&0\\ 0&-3 \end{array} \right).</equation>

---

**2019年第23题 | 解答题 | 11分**
23. （本题满分11分）

已知矩阵<equation>A = \left( \begin{array}{c c c} - 2 & - 2 & 1 \\ 2 & x & - 2 \\ 0 & 0 & - 2 \end{array} \right)</equation>与<equation>B = \left( \begin{array}{c c c} 2 & 1 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & y \end{array} \right)</equation>相似.

I. 求 x,y;

II. 求可逆矩阵<equation>P</equation>，使得<equation>P^{-1}AP = B</equation>.
**答案: **（ I ）<equation>x=3,y=-2;</equation>（Ⅱ）满足<equation>P^{-1} A P=B</equation>的可逆矩阵为<equation>\boldsymbol {P} = \left( \begin{array}{c c c} - 1 & - 1 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right)</equation>
**解析: **解（I）由于 A,B相似，故它们的迹与行列式均相同.

由 A,B有相同的迹可得<equation>- 4+x=1+y</equation>，即 x-y=5.

计算<equation>| A |,| B |. B</equation>为上三角矩阵，故易得<equation>| B |=-2 y.</equation><equation>| A | \xlongequal {\mathrm {按 第三 行 展 开}} (- 2) \cdot \left| \begin{array}{c c} - 2 & - 2 \\ 2 & x \end{array} \right| = 4 x - 8.</equation>由<equation>| A | = | B |</equation>可得<equation>4 x-8=-2 y</equation>即<equation>2 x+y=4.</equation>联立<equation>\left\{ \begin{array}{l l} x-y=5, \\ 2 x+y-4 \end{array} \right.</equation>解得 x=3,y=-2.

（Ⅱ）由于 A,B相似，故它们有相同的特征值.

计算 B的特征多项式.<equation>| \lambda E - B | = \left| \begin{array}{c c c} \lambda - 2 & - 1 & 0 \\ 0 & \lambda + 1 & 0 \\ 0 & 0 & \lambda + 2 \end{array} \right| = (\lambda - 2) (\lambda + 1) (\lambda + 2).</equation>于是，B的特征值为2，-1，-2.从而A的特征值也为2，-1，-2.

由于 A,B具有3个不同的特征值2，-1，-2，故存在可逆矩阵<equation>P_{1}, P_{2}</equation>，使得<equation>P_{1}^{-1} A P_{1}=</equation><equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -2 \end{array} \right), P_{2}^{-1} B P_{2}=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -2 \end{array} \right).</equation>令<equation>P=P_{1} P_{2}^{-1}</equation>，则<equation>P^{-1} A P=P_{2} P_{1}^{-1} A P_{1} P_{2}^{-1}=P_{2}\left(P_{1}^{-1} A P_{1}\right) P_{2}^{-1}=B.</equation><equation>P_{1}</equation>的列向量为A的属于特征值2，-1，-2的特征向量，<equation>P_{2}</equation>的列向量为B的属于特征值2，-1，-2的特征向量.下面分别计算A，B的特征向量.

计算 A的属于特征值2的特征向量.考虑（2E-A）x=0.<equation>2 E - A = \left( \begin{array}{c c c} 4 & 2 & - 1 \\ - 2 & - 1 & 2 \\ 0 & 0 & 4 \end{array} \right) \xrightarrow [ r _ {1} + r _ {3} ^ {*} ]{r _ {3} \times \frac {1}{4}} \left( \begin{array}{c c c} 4 & 2 & 0 \\ - 2 & - 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {2} ^ {*} \times (- 1) ]{r _ {1} ^ {*} + 2 r _ {2} ^ {*}} \left( \begin{array}{c c c} 0 & 0 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>于是，<equation>r ( 2 E-A)=2</equation>，求得<equation>\xi_{1}=(-1,2,0)^{\mathrm{T}}</equation>为（2E-A）x=0的一个基础解系.<equation>(-1,2,0)^{\mathrm{T}}</equation>为 A的属于特征值2的特征向量.

计算 A的属于特征值-1的特征向量.考虑<equation>(- E-A) x=0.</equation><equation>- E - A = \left( \begin{array}{c c c} 1 & 2 & - 1 \\ - 2 & - 4 & 2 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {1} + r _ {3} ]{r _ {2} + 2 r _ {1}} \left( \begin{array}{c c c} 1 & 2 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>于是，<equation>r(-E-A)=2</equation>，求得<equation>\xi_{2}=(-2,1,0)^{\mathrm{T}}</equation>为<equation>(-E-A)x=0</equation>的一个基础解系.<equation>(-2,1,0)^{\mathrm{T}}</equation>为 A的属于特征值-1的特征向量.

计算 A的属于特征值-2的特征向量.考虑<equation>(-2 E-A) x=0.</equation><equation>- 2 E - A = \left( \begin{array}{c c c} 0 & 2 & - 1 \\ - 2 & - 5 & 2 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {2} + 2 r _ {1}} \left( \begin{array}{c c c} 0 & 2 & - 1 \\ - 2 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {2} ^ {*} \times (- 2) - r _ {1}} \left( \begin{array}{c c c} 0 & 2 & - 1 \\ 4 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r(-2 E-A)=2</equation>，求得<equation>\xi_{3}=(-1,2,4)^{\mathrm{T}}</equation>为<equation>(-2 E-A) x=0</equation>的一个基础解系.<equation>(-1,2,4)^{\mathrm{T}}</equation>为 A的属于特征值-2的特征向量.

因此，<equation>P_{1}</equation>可取为<equation>\left( \begin{array}{c c c} - 1 & - 2 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right).</equation>计算 B的属于特征值2的特征向量.考虑（2E-B）x=0.<equation>2 E - B = \left( \begin{array}{c c c} 0 & - 1 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r ( 2 E-B)=2</equation>，求得<equation>\boldsymbol{\eta}_{1}=(1,0,0)^{\mathrm{T}}</equation>为（2E-B）<equation>\boldsymbol{x}=\mathbf{0}</equation>的一个基础解系. （1，0，0）<equation>^{\mathrm{T}}</equation>为B的属于特征值2的特征向量.

计算 B的属于特征值-1的特征向量.考虑<equation>(- E-B) x=0.</equation><equation>- \boldsymbol {E} - \boldsymbol {B} = \left( \begin{array}{c c c} - 3 & - 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {2} \leftrightarrow r _ {3} ]{r _ {1} \times (- 1)} \left( \begin{array}{c c c} 3 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r(-E-B)=2</equation>，求得<equation>\eta_{2}=(-1,3,0)^{\mathrm{T}}</equation>为<equation>(-E-B)x=0</equation>的一个基础解系.<equation>(-1,3,0)^{\mathrm{T}}</equation>为 B的属于特征值-1的特征向量.

计算 B的属于特征值-2的特征向量.考虑<equation>(-2 E-B) x=0.</equation><equation>- 2 E - B = \left( \begin{array}{c c c} - 4 & - 1 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {2} \times (- 1) ]{r _ {1} \times (- 1)} \left( \begin{array}{c c c} 4 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r(-2 E-B)=2</equation>，求得<equation>\boldsymbol{\eta}_{3}=(0,0,1)^{\mathrm{T}}</equation>为<equation>(-2 E-B) x=0</equation>的一个基础解系.<equation>(0,0,1)^{\mathrm{T}}</equation>为 B的属于特征值-2的特征向量.

因此，<equation>P_{2}</equation>可取为<equation>\left( \begin{array}{c c c} 1 & -1 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>利用初等变换法计算<equation>P_{2}^{-1}</equation><equation>\left(\boldsymbol {P} _ {2}, \boldsymbol {E}\right) = \left( \begin{array}{c c c c c c} 1 & - 1 & 0 & 1 & 0 & 0 \\ 0 & 3 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {1} + r _ {2} ^ {*} ]{r _ {2} \times \frac {1}{3}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 1 & \frac {1}{3} & 0 \\ 0 & 1 & 0 & 0 & \frac {1}{3} & 0 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right).</equation>于是，<equation>P_{2}^{-1}=\left( \begin{array}{c c c} 1 & \frac{1}{3} & 0 \\ 0 & \frac{1}{3} & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>综上所述，<equation>\boldsymbol {P} = \boldsymbol {P} _ {1} \boldsymbol {P} _ {2} ^ {- 1} = \left( \begin{array}{c c c} - 1 & - 2 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right) \left( \begin{array}{c c c} 1 & \frac {1}{3} & 0 \\ 0 & \frac {1}{3} & 0 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} - 1 & - 1 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right).</equation>

---

**2018年第7题 | 选择题 | 4分 | 答案: A**
7. 下列矩阵中，与矩阵<equation>\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>A.

相似的是（    ）<equation>\left( \begin{array}{c c c} 1 & 1 & - 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c} 1 & 1 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>
答案: A
**解析: **解已知矩阵与四个选项中的矩阵的特征多项式均为<equation>( x-1 )^{3}</equation>，故1为这五个矩阵的三重特征值记<equation>A=\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E-A=\left( \begin{array}{c c c} 0 & -1 & 0 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r ( E-A )=2.</equation>记<equation>B_{1}=\left( \begin{array}{c c c} 1 & 1 & -1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E-B_{1}=\left( \begin{array}{c c c} 0 & -1 & 1 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r \left( E-B_{1}\right)=2.</equation>记<equation>B_{2}=\left( \begin{array}{c c c} 1 & 0 & -1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E-B_{2}=\left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r \left( E-B_{2}\right) =1.</equation>记<equation>B_{3}=\left( \begin{array}{c c c} 1 & 1 & -1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E-B_{3}=\left( \begin{array}{c c c} 0 & -1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r \left( E-B_{3}\right)=1.</equation>记<equation>B_{4}=\left( \begin{array}{c c c} 1 & 0 & -1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E-B_{4}=\left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r \left( E-B_{4}\right)=1.</equation>由上可见，只有<equation>E-B_{1}</equation>与<equation>E-A</equation>的秩相等，而<equation>E-B_{i}(i=2,3,4)</equation>与<equation>E-A</equation>的秩均不相等，故<equation>E-B_{i}(i=2,3,4)</equation>与<equation>E-A</equation>不相似，从而A与<equation>B_{i}(i=2,3,4)</equation>不相似.

由排除法可知，应选A.

---

**2017年第8题 | 选择题 | 4分 | 答案: B**
8. 已知矩阵<equation>A = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 1 \end{array} \right), B = \left( \begin{array}{c c c} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right), C = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{array} \right),</equation>则（    ）

A. A与 C相似，B与 C相似 B. A与 C相似，B与 C不相似

C. A与 C不相似，B与 C相似 D. A与 C不相似，B与 C不相似
答案: B
**解析: **解分别计算 A,B,C的特征多项式，均为<equation>(\lambda-2)^{2}</equation><equation>(\lambda-1)</equation>，故 A,B,C具有相同的特征值，其中2是二重特征值.

矩阵 C是对角矩阵，故其相似于其自身.

考虑属于特征值2的特征向量.<equation>2 E - A = \left( \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 0 & - 1 \\ 0 & 0 & 1 \end{array} \right), \quad 2 E - B = \left( \begin{array}{c c c} 0 & - 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>由上可知，<equation>r ( 2 E-A )=1</equation><equation>r ( 2 E-B )=2</equation>.于是，<equation>( 2 E-A ) x=0</equation>的基础解系包含两个向量，A有2个线性无关的属于特征值2的特征向量；而<equation>( 2 E-B ) x=0</equation>的基础解系只包含一个向量，B只有1个线性无关的属于特征值2的特征向量.

因此，加上属于特征值1的特征向量，A共有3个线性无关的特征向量，A与C相似；B只有2个线性无关的特征向量，B与C不相似.应选B.

---

**2016年第7题 | 选择题 | 4分 | 答案: C**
7. 设 A,B是可逆矩阵，且 A与 B相似，则下列结论错误的是（    )

A.<equation>A^{\mathrm{T}}</equation>与<equation>B^{\mathrm{T}}</equation>相似 B.<equation>A^{-1}</equation>与<equation>B^{-1}</equation>相似

C.<equation>A+A^{\mathrm{T}}</equation>与<equation>B+B^{\mathrm{T}}</equation>相似 D.<equation>A+A^{-1}</equation>与<equation>B+B^{-1}</equation>相似
答案: C
**解析: **解 由于 A与B相似，故存在可逆矩阵 P，使得<equation>B=P^{-1} A P.</equation>-<equation>B^{\mathrm{T}}=P^{\mathrm{T}}A^{\mathrm{T}}(P^{-1})^{\mathrm{T}}=P^{\mathrm{T}}A^{\mathrm{T}}(P^{\mathrm{T}})^{-1}</equation>，选项A中的结论正确.

-<equation>B^{-1}=P^{-1} A^{-1} \left(P^{-1}\right)^{-1}=P^{-1} A^{-1} P</equation>，选项B中的结论正确.

- 由<equation>B=P^{-1} A P</equation>和<equation>B^{-1}=P^{-1} A^{-1} P</equation>可知，<equation>B+B^{-1}=P^{-1} \left(A+A^{-1}\right) P</equation>，选项D中的结论正确由排除法可知，应选C.

下面我们举例说明选项C不正确.

设<equation>A=\left( \begin{array}{c c}1&0\\ 0&-1 \end{array} \right), P=\left( \begin{array}{c c}1&1\\ 2&1 \end{array} \right),</equation>则<equation>P^{-1}=\left( \begin{array}{c c}-1&1\\ 2&-1 \end{array} \right).</equation>令<equation>\boldsymbol {B} = \boldsymbol {P} ^ {- 1} \boldsymbol {A P} = \left( \begin{array}{c c} - 1 & 1 \\ 2 & - 1 \end{array} \right) \left( \begin{array}{c c} 1 & 0 \\ 0 & - 1 \end{array} \right) \left( \begin{array}{c c} 1 & 1 \\ 2 & 1 \end{array} \right) = \left( \begin{array}{c c} - 3 & - 2 \\ 4 & 3 \end{array} \right),</equation>则<equation>\boldsymbol {A} + \boldsymbol {A} ^ {\mathrm {T}} = \left( \begin{array}{c c} 2 & 0 \\ 0 & - 2 \end{array} \right), \quad \boldsymbol {B} + \boldsymbol {B} ^ {\mathrm {T}} = \left( \begin{array}{c c} - 6 & 2 \\ 2 & 6 \end{array} \right).</equation>计算<equation>A+A^{\mathrm{T}}</equation>的特征多项式得<equation>\lambda^{2}-4</equation>，计算<equation>B+B^{\mathrm{T}}</equation>的特征多项式得<equation>\lambda^{2}-40.</equation>因此<equation>A+A^{\mathrm{T}}</equation>和<equation>B+B^{\mathrm{T}}</equation>不相似.

---

**2016年第23题 | 解答题 | 11分**
23. （本题满分11分）

已知矩阵<equation>A = \left( \begin{array}{c c c} 0 & -1 & 1 \\ 2 & -3 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>I. 求<equation>A^{99};</equation>II. 设3阶矩阵<equation>B=\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)</equation>满足<equation>B^{2}=B A</equation>记<equation>B^{100}=\left(\beta_{1},\beta_{2},\beta_{3}\right)</equation>将<equation>\beta_{1},\beta_{2},\beta_{3}</equation>分别表示为<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>的线性组合.
**答案: **（Ⅱ）<equation>\boldsymbol{\beta}_{1}=(2^{99}-2)\boldsymbol{\alpha}_{1}+(2^{100}-2)\boldsymbol{\alpha}_{2},\boldsymbol{\beta}_{2}=(1-2^{99})\boldsymbol{\alpha}_{1}+(1-2^{100})\boldsymbol{\alpha}_{2},\boldsymbol{\beta}_{3}=(2-2^{98})\boldsymbol{\alpha}_{1}+</equation>（2-2<equation>^{99}</equation>）<equation>\boldsymbol{\alpha}_{2}.</equation>
**解析: **解（I）计算 A的特征多项式<equation>|\lambda E - A|.</equation><equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda & 1 & - 1 \\ - 2 & \lambda + 3 & 0 \\ 0 & 0 & \lambda \end{array} \right| \xlongequal {\text {按 第三 行 展开}} \lambda \left(\lambda^ {2} + 3 \lambda + 2\right) = \lambda (\lambda + 1) (\lambda + 2).</equation>因此，A有3个不同的特征值：-2，-1，0.

由于属于不同特征值的特征向量线性无关，故A有3个线性无关的特征向量，A相似于对角矩阵<equation>\left( \begin{array}{c c c} - 2 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>分别计算 A的属于特征值-2，-1，0的特征向量.

当<equation>\lambda=-2</equation>时，解<equation>(-2E-A)x=0</equation>.由于<equation>- 2 E - A = \left( \begin{array}{c c c} - 2 & 1 & - 1 \\ - 2 & 1 & 0 \\ 0 & 0 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} - 2 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right),</equation>故<equation>( 1, 2, 0 )^{\mathrm{T}}</equation>为 A的属于特征值-2的一个特征向量.

当<equation>\lambda=-1</equation>时，解<equation>(-E-A)x=0</equation>.由于<equation>- E - A = \left( \begin{array}{c c c} - 1 & 1 & - 1 \\ - 2 & 2 & 0 \\ 0 & 0 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right),</equation>故<equation>( 1,1,0 )^{\mathrm{T}}</equation>为 A的属于特征值-1的一个特征向量.

当<equation>\lambda=0</equation>时，解（0E-A）x=0.由于<equation>0 E - A = \left( \begin{array}{c c c} 0 & 1 & - 1 \\ - 2 & 3 & 0 \\ 0 & 0 & 0 \end{array} \right),</equation>故（3，2，2）<equation>^{\mathrm{T}}</equation>为 A的属于特征值0的一个特征向量.

令<equation>P=\left( \begin{array}{c c c} 1 & 1 & 3 \\ 2 & 1 & 2 \\ 0 & 0 & 2 \end{array} \right)</equation>，则<equation>P^{-1} A P=\left( \begin{array}{c c c} - 2 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>计算<equation>P^{-1}</equation>得，<equation>P^{-1}=\left( \begin{array}{c c c} - 1 & 1 & \frac{1}{2} \\ 2 & - 1 & - 2 \\ 0 & 0 & \frac{1}{2} \end{array} \right).</equation><equation>\begin{aligned} \boldsymbol {A} ^ {9 9} &= \boldsymbol {P} \left( \begin{array}{c c c} (- 2) ^ {9 9} & 0 & 0 \\ 0 & (- 1) ^ {9 9} & 0 \\ 0 & 0 & 0  \right) \boldsymbol {P} ^ {- 1} &= \left( \begin{array}{c c c} 1 & 1 & 3 \\ 2 & 1 & 2 \\ 0 & 0 & 2  \right) \left( \begin{array}{c c c} - 2 ^ {9 9} & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0  \right) \left( \begin{array}{c c c} - 1 & 1 & \frac {1}{2} \\ 2 & - 1 & - 2 \\ 0 & 0 & \frac {1}{2}  \right) \\ &= \left( \begin{array}{c c c} 2 ^ {9 9} - 2 & 1 - 2 ^ {9 9} & 2 - 2 ^ {9 8} \\ 2 ^ {1 0 0} - 2 & 1 - 2 ^ {1 0 0} & 2 - 2 ^ {9 9} \\ 0 & 0 & 0  \right). \end{aligned}</equation>（Ⅱ）先求<equation>B^{100}.</equation>由于<equation>B^{2}=BA</equation>，故<equation>\boldsymbol {B} ^ {3} = \boldsymbol {B} \left(\boldsymbol {B} ^ {2}\right) = \boldsymbol {B} (\boldsymbol {B} \boldsymbol {A}) = \boldsymbol {B} ^ {2} \boldsymbol {A} = (\boldsymbol {B} \boldsymbol {A}) \boldsymbol {A} = \boldsymbol {B} \boldsymbol {A} ^ {2}.</equation>下面我们用数学归纳法证明<equation>B^{n}=B A^{n-1}, n=2, 3, \dots</equation>当 n = 2时，<equation>B^{2}=BA.</equation>假设该命题对 n = k 成立，下面证明该命题对 n = k +1 也成立.<equation>\boldsymbol {B} ^ {n} = \boldsymbol {B} ^ {k + 1} = \boldsymbol {B} \boldsymbol {B} ^ {k} \xlongequal {\text {归 纳 假 设}} \boldsymbol {B} \left(\boldsymbol {B} \boldsymbol {A} ^ {k - 1}\right) = \boldsymbol {B} ^ {2} \boldsymbol {A} ^ {k - 1} = (\boldsymbol {B} \boldsymbol {A}) \boldsymbol {A} ^ {k - 1} = \boldsymbol {B} \boldsymbol {A} ^ {k} = \boldsymbol {B} \boldsymbol {A} ^ {n - 1}.</equation>于是，该命题对 n=k+1也成立，从而由数学归纳法可知，该命题对所有<equation>\geqslant2</equation>的正整数均成立因此，<equation>\left(\boldsymbol {\beta} _ {1}, \boldsymbol {\beta} _ {2}, \boldsymbol {\beta} _ {3}\right) = \boldsymbol {B} ^ {1 0 0} = \boldsymbol {B A} ^ {9 9} = \left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\alpha} _ {2}, \boldsymbol {\alpha} _ {3}\right) \left( \begin{array}{c c c} 2 ^ {9 9} - 2 & 1 - 2 ^ {9 9} & 2 - 2 ^ {9 8} \\ 2 ^ {1 0 0} - 2 & 1 - 2 ^ {1 0 0} & 2 - 2 ^ {9 9} \\ 0 & 0 & 0 \end{array} \right).</equation>综上所述，<equation>\begin{aligned} \boldsymbol {\beta} _ {1} &= \left(2 ^ {9 9} - 2\right) \boldsymbol {\alpha} _ {1} + \left(2 ^ {1 0 0} - 2\right) \boldsymbol {\alpha} _ {2}, \\ \boldsymbol {\beta} _ {2} &= \left(1 - 2 ^ {9 9}\right) \boldsymbol {\alpha} _ {1} + \left(1 - 2 ^ {1 0 0}\right) \boldsymbol {\alpha} _ {2}, \\ \boldsymbol {\beta} _ {3} &= \left(2 - 2 ^ {9 8}\right) \boldsymbol {\alpha} _ {1} + \left(2 - 2 ^ {9 9}\right) \boldsymbol {\alpha} _ {2}. \end{aligned}</equation>

---

**2015年第23题 | 解答题 | 11分**
23. (本题满分11分)

设矩阵<equation>A = \left( \begin{array}{c c c} 0 & 2 & -3 \\ -1 & 3 & -3 \\ 1 & -2 & a \end{array} \right)</equation>相似于矩阵<equation>B = \left( \begin{array}{c c c} 1 & -2 & 0 \\ 0 & b & 0 \\ 0 & 3 & 1 \end{array} \right).</equation>I. 求 a,b的值；

II. 求可逆矩阵<equation>P</equation>，使<equation>P^{-1}AP</equation>为对角矩阵.
**答案: **(23) ( I ) a = 4, b = 5;<equation>(\mathrm {I I}) \boldsymbol {P} = \left( \begin{array}{c c c} - 1 & 2 & - 3 \\ - 1 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right), \boldsymbol {P} ^ {- 1} \boldsymbol {A} \boldsymbol {P} = \left( \begin{array}{c c c} 5 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>
**解析: **解（I）由于A,B相似，故存在可逆矩阵Q使得<equation>Q^{-1}AQ=B</equation>，从而<equation>|B|=|Q^{-1}|\cdot|A|\cdot|Q|=|A|.</equation>计算得<equation>|A|=2a-3, |B|=b.</equation>另一方面，A和B具有相同的迹，故<equation>3+a=2+b.</equation>联立得<equation>\left\{ \begin{array}{l l} a+3=b+2, \\ 2a-3=b, \end{array} \right.</equation>解得<equation>\left\{ \begin{array}{l l} a=4, \\ b=5. \end{array} \right.</equation>（Ⅱ）由题设和第（Ⅰ）问得，<equation>| \lambda E - B | = \left| \begin{array}{c c c} \lambda - 1 & 2 & 0 \\ 0 & \lambda - 5 & 0 \\ 0 & - 3 & \lambda - 1 \end{array} \right| = (\lambda - 1) ^ {2} (\lambda - 5).</equation>从而<equation>B</equation>的特征值为1，1，5.由于<equation>A</equation>和<equation>B</equation>相似，故<equation>A</equation>的特征值也为1，1，5.

由第（I）问可得，<equation>A = \left( \begin{array}{c c c} 0 & 2 & -3 \\ -1 & 3 & -3 \\ 1 & -2 & 4 \end{array} \right).</equation>考虑<equation>A</equation>的属于特征值5的特征向量.<equation>\begin{array}{l} 5 E - A = \left( \begin{array}{c c c} 5 & - 2 & 3 \\ 1 & 2 & 3 \\ - 1 & 2 & 1 \end{array} \right) \xrightarrow [ r _ {2} ^ {*} \times \frac {1}{2} ]{r _ {2} - r _ {3}} \left( \begin{array}{c c c} 5 & - 2 & 3 \\ 1 & 0 & 1 \\ - 1 & 2 & 1 \end{array} \right) \xrightarrow [ r _ {3} ^ {*} \times \frac {1}{2} ]{r _ {3} + r _ {2} ^ {* *}} \left( \begin{array}{c c c} 5 & - 2 & 3 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} - 5 r _ {2} ^ {* *} + 2 r _ {3} ^ {* *}} \left( \begin{array}{c c c} 0 & 0 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right). \\ \end{array}</equation>于是，<equation>r(5E - A) = 2</equation>，求得<equation>\xi_{1} = (-1, -1, 1)^{\mathrm{T}}</equation>为<equation>(5E - A)x = 0</equation>的一个基础解系.<equation>(-1, -1, 1)^{\mathrm{T}}</equation>为<equation>A</equation>的属于特征值5的特征向量.

考虑<equation>A</equation>的属于特征值1的特征向量.<equation>\boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} 1 & - 2 & 3 \\ 1 & - 2 & 3 \\ - 1 & 2 & - 3 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & - 2 & 3 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r ( E - A ) = 1</equation>，求得<equation>\boldsymbol{\xi}_{2} = ( 2,1,0 )^{\mathrm{T}}</equation>和<equation>\boldsymbol{\xi}_{3} = (-3,0,1)^{\mathrm{T}}</equation>为<equation>( E - A ) x = 0</equation>的一个基础解系<equation>( 2,1,0 )^{\mathrm{T}}</equation>和<equation>(-3,0,1)^{\mathrm{T}}</equation>为 A的属于特征值1的两个线性无关的特征向量.

取<equation>P = \left( \begin{array}{c c c} - 1 & 2 & - 3 \\ - 1 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right)</equation>，则<equation>P^{-1}AP = \left( \begin{array}{c c c} 5 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>.

---

**2014年第23题 | 解答题 | 11分**
23. (本题满分11分)

证明 n阶矩阵

相似.
**答案: **## （23）证明略.
**解析: **证（法一）记<equation>A=\left( \begin{array}{c c c c} 1 & 1 & \dots & 1 \\ 1 & 1 & \dots & 1 \\ \vdots & \vdots & & \vdots \\ 1 & 1 & \dots & 1 \end{array} \right), B=\left( \begin{array}{c c c c} 0 & \dots & 0 & 1 \\ 0 & \dots & 0 & 2 \\ \vdots & & \vdots & \vdots \\ 0 & \dots & 0 & n \end{array} \right).</equation>由观察可知，<equation>r ( \mathbf{A} )=1</equation>，<equation>\operatorname{t r} ( \mathbf{A} )=n</equation>. 又由于A为实对称矩阵，故必相似于对角矩阵.由相似的矩阵具有相同的秩和迹可知，A相似于秩为1，迹为 n的对角矩阵，不妨记为<equation>\left( \begin{array}{c c c c} n & & & \\ & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right).</equation>另一方面，计算<equation>B</equation>的特征多项式得，<equation>| \lambda E - B | = \left| \begin{array}{c c c c} \lambda & 0 & \dots & - 1 \\ 0 & \lambda & \dots & - 2 \\ \vdots & \vdots & & \vdots \\ 0 & 0 & \dots & \lambda - n \end{array} \right| = \lambda^ {n - 1} (\lambda - n).</equation>B的特征值为<equation>n,0,\dots ,0</equation>，其中0为<equation>n - 1</equation>重特征值.

由于<equation>0E - B = \left( \begin{array}{c c c} 0 & & -1 \\ & 0 & -2 \\ & \ddots & \vdots \\ & & -n \end{array} \right)</equation>，故<equation>r(0E - B) = 1</equation>，从而<equation>(0E - B)x = 0</equation>的解集的秩为<equation>n - 1</equation><equation>0E - B)x = 0</equation>有<equation>n - 1</equation>个线性无关的解.

B有 n-1个属于特征值0的线性无关的特征向量，再加上B的属于n的特征向量，B共有n个线性无关的特征向量. 从而B也相似于<equation>\left( \begin{array}{c c c c} n & & & \\ & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right).</equation>因此，存在可逆矩阵 P，Q，使得<equation>P^{-1} A P=Q^{-1} B Q=\left( \begin{array}{c c c c} n & & & \\ & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right)</equation>，于是<equation>Q P^{-1} A P Q^{-1}=B.</equation>令 U = PQ<equation>^{-1}</equation>，则 B = U<equation>^{-1}</equation>AU，A和B相似.

（法二）计算 A的特征多项式.<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c c} \lambda - 1 & - 1 & \dots & - 1 \\ - 1 & \lambda - 1 & \dots & - 1 \\ \vdots & \vdots & & \vdots \\ - 1 & - 1 & \dots & \lambda - 1  \right| \frac {c _ {1} + \left(c _ {2} + c _ {3} + \dots + c _ {n}\right)}{\hline} \left| \begin{array}{c c c c} \lambda - n & - 1 & \dots & - 1 \\ \lambda - n & \lambda - 1 & \dots & - 1 \\ \vdots & \vdots & & \vdots \\ \lambda - n & - 1 & \dots & \lambda - 1  \right| \\ &= (\lambda - n) \left| \begin{array}{c c c c} 1 & - 1 & \dots & - 1 \\ 1 & \lambda - 1 & \dots & - 1 \\ \vdots & \vdots & & \vdots \\ 1 & - 1 & \dots & \lambda - 1  \right| \frac {c _ {i} + c _ {1}}{i = 2 , \dots , n} (\lambda - n) \left| \begin{array}{c c c c} 1 & 0 & \dots & 0 \\ 1 & \lambda & \dots & 0 \\ \vdots & \vdots & & \vdots \\ 1 & 0 & \dots & \lambda  \right| \\ &= \lambda^ {n - 1} (\lambda - n). \end{aligned}</equation>由于 A为实对称矩阵，故由 A的特征多项式为<equation>\lambda^{n-1} (\lambda-n)</equation>可知 A相似于对角矩阵<equation>= \left( \begin{array}{c c c c} n & & & \\ & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right).</equation>其全同法一

---

**2013年第8题 | 选择题 | 4分 | 答案: B**
8. 矩阵

相似的充分必要条件为（    ）

A. a=0,b=2 B. a=0,b为任意常数 C. a=2,b=0 D. a=2,b为任意常数
答案: B
**解析: **解 矩阵<equation>\left( \begin{array}{lll}1&a&1\\ a&b&a\\ 1&a&1 \end{array} \right)</equation>与<equation>\left( \begin{array}{lll}2&0&0\\ 0&b&0\\ 0&0&0 \end{array} \right)</equation>均为实对称矩阵，故它们相似等价于它们有相同的特征多项式.

项式.

矩阵<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>的特征多项式为<equation>f (\lambda) = \lambda (\lambda - 2) (\lambda - b).</equation>考虑<equation>A = \left( \begin{array}{c c c} 1 & a & 1 \\ a & b & a \\ 1 & a & 1 \end{array} \right)</equation>的特征多项式<equation>g(\lambda)</equation>.<equation>g (\lambda) = | \lambda E - A | = \left| \begin{array}{c c c} \lambda - 1 & - a & - 1 \\ - a & \lambda - b & - a \\ - 1 & - a & \lambda - 1 \end{array} \right| = \lambda \left[ (\lambda - 2) (\lambda - b) - 2 a ^ {2} \right].</equation>由于<equation>f(\lambda)-g(\lambda)=2 a^{2}\lambda</equation>，故<equation>f(\lambda)=g(\lambda)</equation>当且仅当 a=0.由于上述论证不涉及到b，故b取任意常数均不影响结果.应选B.

---

**2010年第8题 | 选择题 | 4分 | 答案: D**
8. 设 A为4阶实对称矩阵，则<equation>A^{2}+A=O</equation>. 若 A的秩为3，则 A相似于（    ）

A.<equation>\left( \begin{array}{c c c c} 1 & & \\ & 1 & \\ & & 1 \\ & & 0 \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c c} 1 & & \\ & 1 & \\ & & - 1 \\ & & 0 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c c} 1 & & \\ & - 1 & \\ & & - 1 \\ & & 0 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c c} - 1 & & \\ & - 1 & \\ & & - 1 \\ & & 0 \end{array} \right)</equation>
答案: D
**解析: **解（法一）不妨设<equation>\lambda</equation>为 A的特征值，<equation>\alpha</equation>为其相应的特征向量.由<equation>A^{2}+A=O</equation>得<equation>(A^{2}+A)\alpha=0.</equation>代入<equation>A\alpha=\lambda\alpha</equation>得，<equation>(\lambda^{2}+\lambda)\alpha=0.</equation>又由于<equation>\alpha</equation>非零，故<equation>\lambda^{2}+\lambda=0,\lambda=0</equation>或<equation>\lambda=-1.</equation>由于 A为实对称矩阵，故 A相似于对角矩阵.又因为<equation>r ( A )=3</equation>，所以对角矩阵的秩也为3，<equation>\lambda=-1</equation>是 A的三重特征值， A相似于<equation>\left( \begin{array}{c c c c} - 1 & & & \\ & - 1 & & \\ & & - 1 & \\ & & & 0 \end{array} \right)</equation>.应选 D.

（法二）由于 A为实对称矩阵，故存在可逆矩阵 P使得<equation>P^{-1} A P=\left( \begin{array}{c c c c} \lambda_{1} & & & \\ & \lambda_{2} & & \\ & & \lambda_{3} & \\ & & & \lambda_{4} \end{array} \right).</equation>从而<equation>\begin{aligned} \boldsymbol {O} &= \boldsymbol {A} ^ {2} + \boldsymbol {A} = \boldsymbol {P} \left( \begin{array}{c c c c} \lambda_ {1} ^ {2} & & & \\ & \lambda_ {2} ^ {2} & & \\ & & \lambda_ {3} ^ {2} & \\ & & & \lambda_ {4} ^ {2}  \right) \boldsymbol {P} ^ {- 1} + \boldsymbol {P} \left( \begin{array}{c c c c} \lambda_ {1} & & & \\ & \lambda_ {2} & & \\ & & \lambda_ {3} & \\ & & & \lambda_ {4}  \right) \boldsymbol {P} ^ {- 1} \\ &= \boldsymbol {P} \left( \begin{array}{c c c c} \lambda_ {1} ^ {2} + \lambda_ {1} & & & \\ & \lambda_ {2} ^ {2} + \lambda_ {2} & & \\ & & \lambda_ {3} ^ {2} + \lambda_ {3} & \\ & & & \lambda_ {4} ^ {2} + \lambda_ {4}  \right) \boldsymbol {P} ^ {- 1}. \end{aligned}</equation>因此<equation>\lambda_{i}^{2}+\lambda_{i}=0 ( i=1,2,3,4).</equation>解得<equation>\lambda_{i}=0</equation>或<equation>\lambda_{i}=-1 ( i=1,2,3,4).</equation>又由于<equation>r ( A )=3</equation>，故 A相似于<equation>\left( \begin{array}{c c c c} - 1 & & & \\ & - 1 & & \\ & & - 1 & \\ & & & 0 \end{array} \right).</equation>应选D.

---

**2009年第14题 | 填空题 | 4分**
14. 设<equation>\alpha, \beta</equation>为3维列向量，<equation>\beta^{\mathrm{T}}</equation>为<equation>\beta</equation>的转置. 若矩阵<equation>\alpha\beta^{\mathrm{T}}</equation>相似于<equation>\left( \begin{array}{c c c} {2} & {0} & {0} \\ {0} & {0} & {0} \\ {0} & {0} & {0} \end{array} \right)</equation>，则<equation>\beta^{\mathrm{T}}\alpha=</equation>___
**解析: **解设<equation>\pmb{\alpha} = (a_{1}, a_{2}, a_{3})^{\mathrm{T}},\pmb {\beta} = (b_{1}, b_{2}, b_{3})^{\mathrm{T}}</equation>，则<equation>\begin{aligned} \boldsymbol {\alpha} \boldsymbol {\beta} ^ {\mathrm {T}} &= \left(  a _ {1} \\ a _ {2} \\ a _ {3}  \right) \left(b _ {1}, b _ {2}, b _ {3}\right) &= \left( \begin{array}{l l l} a _ {1} b _ {1} & a _ {1} b _ {2} & a _ {1} b _ {3} \\ a _ {2} b _ {1} & a _ {2} b _ {2} & a _ {2} b _ {3} \\ a _ {3} b _ {1} & a _ {3} b _ {2} & a _ {3} b _ {3}  \right), \end{aligned}</equation><equation>\begin{aligned} \boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {\alpha} &= \left(b _ {1}, b _ {2}, b _ {3}\right) \left(  a _ {1} \\ a _ {2} \\ a _ {3}  \right) &= a _ {1} b _ {1} + a _ {2} b _ {2} + a _ {3} b _ {3} = \operatorname {t r} \left(\boldsymbol {\alpha} \boldsymbol {\beta} ^ {\mathrm {T}}\right). \end{aligned}</equation>由于<equation>\alpha \beta^{\mathrm{T}}</equation>相似于<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>，故<equation>\operatorname{tr}(\alpha \beta^{\mathrm{T}}) = \operatorname{tr}(\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)) = 2.</equation>因此，<equation>\beta^{\mathrm{T}}\alpha = 2.</equation>

---


### 矩阵


