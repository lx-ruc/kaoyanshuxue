---


## 线性代数

### 线性方程组

### 矩阵的特征值和特征向量

#### 矩阵的相似与相似对角化


**2025年第6题 | 选择题 | 5分 | 答案: B**

6. 设 A为三阶矩阵，则“<equation>A^{3}-A^{2}</equation>”可对角化是“ A可对角化”的（    ）

A. 充分但不必要条件 B. 必要但不充分条件

C. 充分必要条件 D. 既不充分也不必要条件

答案: B

**解析:**解 若 A可相似对角化，则存在可逆矩阵 P，使得<equation>P^{-1} A P=A</equation>，其中 A为对角矩阵.由此可得 A = P A P^{-1} ，进一步可得<equation>A^{2}=P A^{2} P^{-1}, A^{3}=P A^{3} P^{-1}</equation>，从而<equation>A ^ {3} - A ^ {2} = P A ^ {3} P ^ {- 1} - P A ^ {2} P ^ {- 1} = P \left(A ^ {3} - A ^ {2}\right) P ^ {- 1},</equation>即<equation>P^{-1}\left(A^{3} - A^{2}\right)P = A^{3} - A^{2}</equation>.

因此，<equation>A^{3}-A^{2}</equation>可相似对角化，“<equation>A^{3}-A^{2}</equation>可对角化”是“<equation>A</equation>可对角化”的必要条件.

但是由“<equation>A^{3}-A^{2}</equation>可对角化”却不能推出“<equation>A</equation>可对角化”.

若<equation>\alpha</equation>为矩阵 A的属于特征值<equation>\lambda</equation>的特征向量，即<equation>A\alpha=\lambda\alpha</equation>，则<equation>A^{k}\alpha=\lambda^{k}\alpha</equation>，即<equation>\alpha</equation>也是<equation>A^{k}</equation>的属于特征值<equation>\lambda^{k}</equation>的特征向量.但反之并不成立.

例如，取<equation>A = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>，则<equation>A^{3} = A^{2} = O, A^{3} - A^{2}</equation>有3个线性无关的特征向量，从而可相似对

角化. 但是 A的特征值0是三重特征值，而<equation>r ( A )=1</equation>，故 A只有 3-1=2个线性无关的属于0的特征向量，从而不能相似对角化.

因此，“<equation>A^{3}-A^{2}</equation>可对角化”不是“<equation>A</equation>可对角化”的充分条件.

综上所述，应选B.

---

**2023年第21题 | 解答题 | 12分**

21. (本题满分12分)

设矩阵 A满足：对任意<equation>x_{1}, x_{2}, x_{3}</equation>均有<equation>A\left( \begin{array}{c} x_{1} \\ x_{2} \\ x_{3} \end{array} \right)=\left( \begin{array}{c} x_{1}+x_{2}+x_{3} \\ 2 x_{1}-x_{2}+x_{3} \\ x_{2}-x_{3} \end{array} \right)</equation>I. 求 A;

II. 求可逆矩阵<equation>P</equation>与对角矩阵<equation>\Lambda</equation>, 使得<equation>P^{-1}AP = \Lambda</equation>.

**答案:**<equation>\begin{aligned} (\mathrm {I}) \boldsymbol {A} &= \left( \begin{array}{c c c} 1 & 1 & 1 \\ 2 & - 1 & 1 \\ 0 & 1 & - 1  \right); \\ (\mathrm {I I}) \boldsymbol {P} &= \left( \begin{array}{c c c} 0 & - 1 & 4 \\ - 1 & 0 & 3 \\ 1 & 2 & 1  \right), \boldsymbol {A} &= \left( \begin{array}{c c c} - 2 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 2  \right). \end{aligned}</equation>

**解析:**（ I ）因为<equation>\begin{aligned} \mathbf {A} \left(  x _ {1} \\ x _ {2} \\ x _ {3}  \right) &= \left(  x _ {1} + x _ {2} + x _ {3} \\ 2 x _ {1} - x _ {2} + x _ {3} \\ x _ {2} - x _ {3}  \right) &= \left( \begin{array}{c c c} 1 & 1 & 1 \\ 2 & - 1 & 1 \\ 0 & 1 & - 1  \right) \left(  x _ {1} \\ x _ {2} \\ x _ {3}  \right) \end{aligned}</equation>对任意<equation>x_{1}, x_{2}, x_{3}</equation>均成立，所以方程组<equation>\left[ A-\left( \begin{array}{c c c} 1 & 1 & 1 \\ 2 & -1 & 1 \\ 0 & 1 & -1 \end{array} \right) \right] \left( \begin{array}{l} x_{1} \\ x_{2} \\ x_{3} \end{array} \right)=\mathbf{0}</equation>的解为全体3维列向量.于是该方程组的系数矩阵的秩为0，从而<equation>A-\left( \begin{array}{c c c} 1 & 1 & 1 \\ 2 & -1 & 1 \\ 0 & 1 & -1 \end{array} \right)=\mathbf{0}</equation>即<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & 1 & 1 \\ 2 & - 1 & 1 \\ 0 & 1 & - 1 \end{array} \right).</equation>（Ⅱ）计算 A的特征值. A的特征多项式为<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - 1 & - 1 & - 1 \\ - 2 & \lambda + 1 & - 1 \\ 0 & - 1 & \lambda + 1  \right| \xlongequal {\text {按 第三 行 展开}} \left| \begin{array}{c c} \lambda - 1 & - 1 \\ - 2 & - 1  \right| + (\lambda + 1) \left| \begin{array}{c c} \lambda - 1 & - 1 \\ - 2 & \lambda + 1  \right| \\ &= - (\lambda + 1) + (\lambda + 1) \left(\lambda^ {2} - 3\right) = (\lambda + 1) \left(\lambda^ {2} - 4\right) \\ &= (\lambda + 1) (\lambda + 2) (\lambda - 2). \end{aligned}</equation>于是，A的特征值为-2，-1，2.

计算 A的属于特征值-2的特征向量.考虑方程组<equation>(-2 E-A) x=0.</equation><equation>- 2 E - A = \left( \begin{array}{c c c} - 3 & - 1 & - 1 \\ - 2 & - 1 & - 1 \\ 0 & - 1 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} - 3 & 0 & 0 \\ - 2 & 0 & 0 \\ 0 & 1 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>解方程组<equation>(-2 E-A) x=0</equation>可得<equation>\left( \begin{array}{c}0\\ -1\\ 1 \end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c}0\\ -1\\ 1 \end{array} \right)</equation>为A的属于特征值 -2的一个特征向量.

计算 A的属于特征值-1的特征向量.考虑方程组<equation>(- E-A) x=0.</equation><equation>- \boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} - 2 & - 1 & - 1 \\ - 2 & 0 & - 1 \\ 0 & - 1 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 2 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>解方程组<equation>(- E-A) x=0</equation>可得<equation>\left( \begin{array}{c}-1\\0\\2 \end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c}-1\\0\\2 \end{array} \right)</equation>为 A的属于特征值 -1的一个特征向量.

计算 A的属于特征值2的特征向量.考虑方程组（2E-A）<equation>x=0.</equation><equation>2 E - A = \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ - 2 & 3 & - 1 \\ 0 & - 1 & 3 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ 0 & 1 & - 3 \\ 0 & - 1 & 3 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & - 4 \\ 0 & 1 & - 3 \\ 0 & 0 & 0 \end{array} \right).</equation>解方程组<equation>( 2 E-A ) x=0</equation>可得<equation>\left( \begin{array}{c c c} 4 \\ 3 \\ 1 \end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c} 4 \\ 3 \\ 1 \end{array} \right)</equation>为A的属于特征值2的一个特征向量.

令<equation>P=\left( \begin{array}{c c c} 0 & -1 & 4 \\ -1 & 0 & 3 \\ 1 & 2 & 1 \end{array} \right).</equation>由于属于不同特征值的特征向量线性无关，故P的列向量组线性无关，从而P可逆.由特征向量的性质可得<equation>P^{-1} A P=A</equation>其中<equation>\Lambda=\left( \begin{array}{c c c} -2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>

---

**2022年第5题 | 选择题 | 5分 | 答案: B**

5. 设 A为3阶矩阵，<equation>\Lambda=\left( \begin{array}{c c c} {1} & {0} & {0} \\ {0} & {-1} & {0} \\ {0} & {0} & {0} \end{array} \right)</equation>，则 A的特征值为1，-1，0的充分必要条件是（    )

A. 存在可逆矩阵 P,Q，使得<equation>A=P\Lambda Q</equation>B. 存在可逆矩阵 P，使得<equation>A=P\Lambda P^{-1}</equation>C. 存在正交矩阵 Q，使得<equation>A=Q\Lambda Q^{-1}</equation>D. 存在可逆矩阵 P，使得<equation>A=P\Lambda P^{\mathrm{T}}</equation>

答案: B

**解析:**解3阶矩阵 A的特征值为1，-1，0意味着 A有3个不同的特征值，从而 A相似于与它具有相同特征值的对角矩阵，即<equation>\Lambda</equation>.于是，A的特征值为1，-1，0的充分必要条件即 A与<equation>\Lambda</equation>相似的充分必要条件.

选项B实际上为 A与<equation>\Lambda</equation>相似的定义，即存在可逆矩阵 P，使得<equation>\Lambda = P^{-1}AP</equation>，也即<equation>A=P\Lambda P^{-1}</equation>因此，应选B.

下面说明选项A、C、D不正确.

选项A是A与A等价的定义.若两矩阵相似，则它们必等价，但两个等价的矩阵不一定相似，如<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>和<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>，故选项A是A与A相似的必要不充分条件.

因为正交矩阵也是可逆矩阵，所以选项C是A与A相似的充分条件.但选项C并不是A与A相似的必要条件，因为A不一定能找到一组相互正交的特征向量，这一要求对实对称矩阵成立，对一般矩阵不成立.

取<equation>\boldsymbol{\xi}_{1}=\left( \begin{array}{c}1\\ 0\\ 0 \end{array} \right),\boldsymbol{\xi}_{2}=\left( \begin{array}{c}1\\ 1\\ 0 \end{array} \right),\boldsymbol{\xi}_{3}=\left( \begin{array}{c}1\\ 0\\ 1 \end{array} \right)</equation>，则<equation>\boldsymbol{\xi}_{1},\boldsymbol{\xi}_{2},\boldsymbol{\xi}_{3}</equation>相互均不正交.令<equation>P=(\boldsymbol{\xi}_{1},\boldsymbol{\xi}_{2},\boldsymbol{\xi}_{3})</equation>，<equation>\Lambda=</equation><equation>\left( \begin{array}{c c c}1&0&0\\ 0&-1&0\\ 0&0&0 \end{array} \right)</equation>，则<equation>A=P \Lambda P^{-1}=\left( \begin{array}{lll} 1 & 1 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)\left( \begin{array}{lll} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 0 \end{array} \right)\left( \begin{array}{lll} 1 & -1 & -1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)=\left( \begin{array}{lll} 1 & -2 & -1 \\ 0 & -1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>A与对角矩阵 A相似，但是 A的线性无关的特征向量均不正交.

选项D是A与A合同的定义.对一般矩阵而言，相似与合同之间并无相互蕴含的关系.

考虑选项A的反例<equation>\left( \begin{array}{c c c}1&0&0\\ 0&0&0\\ 0&0&0 \end{array} \right)</equation>和<equation>\left( \begin{array}{c c c}2&0&0\\ 0&0&0\\ 0&0&0 \end{array} \right)</equation>，这两个矩阵具有相同的正、负惯性指数，从而合同，但它们并不相似.

考虑选项C的反例<equation>A=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 0 \end{array} \right), A=\left( \begin{array}{c c c} 1 & -2 & -1 \\ 0 & -1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>由前面的分析可知，A与A相似又因为A是实对称矩阵，而与实对称矩阵合同的矩阵一定是实对称矩阵，但A不是实对称矩阵，所以A与A不合同.

因此，选项D既不是A与A相似的充分条件，也不是A与A相似的必要条件.

---

**2021年第21题 | 解答题 | 12分**

21. (本题满分12分)

设矩阵<equation>A = \left( \begin{array}{c c c} 2 & 1 & 0 \\ 1 & 2 & 0 \\ 1 & a & b \end{array} \right)</equation>仅有两个不同的特征值，若 A相似于对角矩阵，求 a,b的值，并求可逆矩阵 P，使<equation>P^{-1} A P</equation>为对角矩阵.

**答案:**当 a = 1,b = 1时，<equation>P=\left( \begin{array}{c c c} - 1 & 0 & 1 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right), P^{-1} A P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 3 \end{array} \right)</equation>为对角矩阵.

当 a = -1,b = 3时，<equation>P=\left( \begin{array}{c c c} 1 & 0 & - 1 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right), P^{-1} A P=\left( \begin{array}{c c c} 3 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>为对角矩阵.

**解析:**计算 A的特征多项式.<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - 2 & - 1 & 0 \\ - 1 & \lambda - 2 & 0 \\ - 1 & - a & \lambda - b  \right| \xlongequal {\text {按 第三 列 展 开}} (\lambda - b) \left| \begin{array}{c c} \lambda - 2 & - 1 \\ - 1 & \lambda - 2  \right| \\ &= (\lambda - b) \left[ (\lambda - 2) ^ {2} - 1 \right] = (\lambda - 1) (\lambda - 3) (\lambda - b). \end{aligned}</equation>A的所有特征值为1,3,b.

若 A仅有两个不同的特征值，则 b只可能为1或者3.

下面分情况讨论.

(1) 若 b=1，则 A的特征值为1,1,3.

计算 A的属于特征值1的特征向量.考虑 （E-A）x=0.<equation>\boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} - 1 & - 1 & 0 \\ - 1 & - 1 & 0 \\ - 1 & - a & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 - a & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>若 A可相似对角化，则方程组<equation>( E-A ) x=0</equation>有两个线性无关的解. r(E-A) =1.于是，a=1解方程组<equation>( E-A ) x=0</equation>可得<equation>\left( \begin{array}{c}-1\\1\\0\end{array} \right)</equation>与<equation>\left( \begin{array}{c}0\\0\\1\end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c}-1\\1\\0\end{array} \right)</equation>与<equation>\left( \begin{array}{c}0\\0\\1\end{array} \right)</equation>为 A的属于特征值1的两个线性无关的特征向量.

计算 A的属于特征值3的特征向量.考虑<equation>( 3 E-A ) x=0.</equation><equation>3 E - A = \left( \begin{array}{c c c} 1 & - 1 & 0 \\ - 1 & 1 & 0 \\ - 1 & - 1 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & - 1 & 0 \\ 0 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right).</equation>解方程组<equation>( 3 E-A ) x=0</equation>可得<equation>\left( \begin{array}{c c c} 1 \\ 1 \\ 1 \end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c} 1 \\ 1 \\ 1 \end{array} \right)</equation>为A的属于特征值3的一个特征向量.

令<equation>P=\left( \begin{array}{c c c} -1 & 0 & 1 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right)</equation>，则<equation>P^{-1} A P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 3 \end{array} \right)</equation>为对角矩阵.

(2) 若 b=3，则 A的特征值为1,3,3.

计算 A的属于特征值3的特征向量.考虑<equation>( 3 E-A ) x=0.</equation><equation>3 E - A = \left( \begin{array}{c c c} 1 & - 1 & 0 \\ - 1 & 1 & 0 \\ - 1 & - a & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & - 1 & 0 \\ 0 & - 1 - a & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>若 A可相似对角化，则方程组（3E-A）<equation>x=0</equation>有两个线性无关的解. r（3E-A）=1.于是，a=-1.解方程组（3E-A）<equation>x=0</equation>可得<equation>\left( \begin{array}{l} 1 \\ 1 \\ 0 \end{array} \right)</equation>与<equation>\left( \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{l} 1 \\ 1 \\ 0 \end{array} \right)</equation>与<equation>\left( \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right)</equation>为 A的属于特征值3的两个线性无关的特征向量.

计算 A的属于特征值1的特征向量.考虑 （E-A）x=0.<equation>\boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} - 1 & - 1 & 0 \\ - 1 & - 1 & 0 \\ - 1 & 1 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right).</equation>解方程组<equation>( E-A ) x=0</equation>可得<equation>\left( \begin{array}{c c c} - 1 \\ 1 \\ 1 \end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c c} - 1 \\ 1 \\ 1 \end{array} \right)</equation>为 A的属于特征值1的一个特征向量.

令<equation>P=\left( \begin{array}{c c c} 1 & 0 & - 1 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right)</equation>，则<equation>P^{-1} A P=\left( \begin{array}{c c c} 3 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>为对角矩阵.

---

**2020年第21题 | 解答题 | 11分**

21. (本题满分11分)

设 A为2阶矩阵，<equation>P=(\alpha ,A\alpha)</equation>，其中<equation>\alpha</equation>是非零向量且不是 A的特征向量.

I. 证明 P为可逆矩阵；

II. 若<equation>A^{2}\alpha+A\alpha-6\alpha=0</equation>，求<equation>P^{-1}AP</equation>，并判断 A是否相似于对角矩阵.

**答案:**（I）证明略；

（Ⅱ）<equation>P^{-1} A P=\left( \begin{array}{cc} 0 & 6 \\ 1 & -1 \end{array} \right)</equation>，A相似于对角矩阵<equation>\left( \begin{array}{c c} 2 & 0 \\ 0 & -3 \end{array} \right)</equation>

**解析:**解（I）要证明 P为可逆矩阵，可证明<equation>\alpha, A\alpha</equation>线性无关.

假设<equation>\alpha, A\alpha</equation>线性相关，则存在不全为零的常数<equation>k_{1}, k_{2}</equation>，使得<equation>k_{1}\alpha+k_{2}A\alpha=0.</equation>若<equation>k_{2}=0</equation>，则<equation>k_{1}\alpha=0</equation>.但<equation>\alpha</equation>为非零向量，故<equation>k_{1}=0</equation>.这与假设矛盾.

若<equation>k_{2}\neq 0</equation>，则<equation>A\alpha=-\frac{k_{1}}{k_{2}}\alpha</equation>.由特征向量的定义可知<equation>\alpha</equation>为A的特征向量.这与<equation>\alpha</equation>不是A的特征向量矛盾.

因此，<equation>\alpha, A\alpha</equation>线性无关.P为可逆矩阵.

（Ⅱ）考虑AP.<equation>\begin{aligned} A P &= \left(A \alpha , A ^ {2} \alpha\right) \xlongequal {A ^ {2} \alpha + A \alpha - 6 \alpha = 0} \left(A \alpha , 6 \alpha - A \alpha\right) = (\alpha , A \alpha) \left( \begin{array}{c c} 0 & 6 \\ 1 & - 1  \right) \\ &= P \left( \begin{array}{c c} 0 & 6 \\ 1 & - 1  \right). \end{aligned}</equation>由第（I）问可知，P可逆.上式两端同时左乘<equation>P^{-1}</equation>可得<equation>P^{-1} A P=\left( \begin{array}{cc}0&6\\ 1&-1 \end{array} \right).</equation>记<equation>B=\left( \begin{array}{cc}0&6\\ 1&-1 \end{array} \right)</equation>，则A与B相似.A与对角矩阵相似等价于B与对角矩阵相似.

计算 B的特征多项式.<equation>| \lambda E - B | = \left| \begin{array}{c c} \lambda & - 6 \\ - 1 & \lambda + 1 \end{array} \right| = \lambda^ {2} + \lambda - 6 = (\lambda + 3) (\lambda - 2).</equation>2与-3是B的两个不同特征值.于是，B相似于对角矩阵<equation>\left( \begin{array}{cc}2&0\\ 0&-3 \end{array} \right).</equation>由相似关系的传递性可知，A相似于对角矩阵<equation>\left( \begin{array}{cc}2&0\\ 0&-3 \end{array} \right).</equation>

---

**2019年第21题 | 解答题 | 11分**

21. （本题满分11分）

已知矩阵<equation>A = \left( \begin{array}{c c c} - 2 & - 2 & 1 \\ 2 & x & - 2 \\ 0 & 0 & - 2 \end{array} \right)</equation>与<equation>B = \left( \begin{array}{c c c} 2 & 1 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & y \end{array} \right)</equation>相似.

I. 求 x,y;

II. 求可逆矩阵<equation>P</equation>，使得<equation>P^{-1}AP = B</equation>.

**答案:**（ I ）<equation>x=3, y=-2;</equation>（Ⅱ）满足<equation>P^{-1} A P=B</equation>的可逆矩阵为<equation>\boldsymbol {P} = \left( \begin{array}{c c c} - 1 & - 1 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right).</equation>

**解析:**解（ I ）由于 A,B相似，故它们的迹与行列式均相同.

由 A,B有相同的迹可得<equation>- 4+x=1+y</equation>，即 x-y=5.

计算<equation>| A |, | B |. B</equation>为上三角矩阵，故易得<equation>| B |=-2 y.</equation><equation>| A | \xlongequal {\text {按 第三 行 展 开}} (- 2) \cdot \left| \begin{array}{c c} - 2 & - 2 \\ 2 & x \end{array} \right| = 4 x - 8.</equation>由<equation>| A | = | B |</equation>可得 4x-8=-2y，即 2x+y=4.

联立<equation>\left\{ \begin{array}{l l} x-y=5, \\ 2-y=-2. \end{array} \right.</equation>解得 x=3,y=-2.<equation>2 x + y = 4,</equation>（Ⅱ）由于 A,B相似，故它们有相同的特征值.

计算 B的特征多项式.<equation>| \lambda E - B | = \left| \begin{array}{c c c} \lambda - 2 & - 1 & 0 \\ 0 & \lambda + 1 & 0 \\ 0 & 0 & \lambda + 2 \end{array} \right| = (\lambda - 2) (\lambda + 1) (\lambda + 2).</equation>于是，B的特征值为2，-1，-2. 从而A的特征值也为2，-1，-2.

由于 A,B具有3个不同的特征值2，-1，-2，故存在可逆矩阵<equation>P_{1}, P_{2}</equation>，使得<equation>P_{1}^{-1} A P_{1}=</equation><equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -2 \end{array} \right), P_{2}^{-1} B P_{2}=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -2 \end{array} \right).</equation>令<equation>P=P_{1} P_{2}^{-1}</equation>，则<equation>P^{-1} A P=P_{2} P_{1}^{-1} A P_{1} P_{2}^{-1}=P_{2}\left(P_{1}^{-1} A P_{1}\right) P_{2}^{-1}=B.</equation><equation>P_{1}</equation>的列向量为A的属于特征值2，-1，-2的特征向量，<equation>P_{2}</equation>的列向量为B的属于特征值2，-1，-2的特征向量。下面分别计算A，B的特征向量.

计算 A的属于特征值2的特征向量.考虑（2E-A）x=0.<equation>2 E - A = \left( \begin{array}{c c c} 4 & 2 & - 1 \\ - 2 & - 1 & 2 \\ 0 & 0 & 4 \end{array} \right) \xrightarrow [ r _ {1} + r _ {3} ^ {*} ]{r _ {3} \times \frac {1}{4}} \left( \begin{array}{c c c} 4 & 2 & 0 \\ - 2 & - 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {2} ^ {*} \times (- 1) ]{r _ {1} ^ {*} + 2 r _ {2} ^ {*}} \left( \begin{array}{c c c} 0 & 0 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>于是，<equation>r ( 2 E-A )=2</equation>，求得<equation>\boldsymbol{\xi}_{1}=(-1,2,0)^{\mathrm{T}}</equation>为<equation>( 2 E-A ) x=0</equation>的一个基础解系.<equation>(-1,2,0)^{\mathrm{T}}</equation>为 A的属于特征值2的特征向量.

计算 A的属于特征值-1的特征向量.考虑<equation>(- E-A) x=0.</equation><equation>- E - A = \left( \begin{array}{c c c} 1 & 2 & - 1 \\ - 2 & - 4 & 2 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {1} + r _ {3} ]{r _ {2} + 2 r _ {1}} \left( \begin{array}{c c c} 1 & 2 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>于是，<equation>r(-E-A)=2</equation>，求得<equation>\xi_{2}=(-2,1,0)^{\mathrm{T}}</equation>为<equation>(-E-A)x=0</equation>的一个基础解系.<equation>(-2,1,0)^{\mathrm{T}}</equation>为 A的属于特征值-1的特征向量.

计算 A的属于特征值-2的特征向量.考虑<equation>(-2 E-A) x=0.</equation><equation>- 2 E - A = \left( \begin{array}{c c c} 0 & 2 & - 1 \\ - 2 & - 5 & 2 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {2} + 2 r _ {1}} \left( \begin{array}{c c c} 0 & 2 & - 1 \\ - 2 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {2} ^ {*} \times (- 2) - r _ {1}} \left( \begin{array}{c c c} 0 & 2 & - 1 \\ 4 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r(-2 E-A)=2</equation>，求得<equation>\xi_{3}=(-1,2,4)^{\mathrm{T}}</equation>为<equation>(-2 E-A) x=0</equation>的一个基础解系.<equation>(-1,2,4)^{\mathrm{T}}</equation>为 A的属于特征值-2的特征向量.<equation>P _ {1}</equation><equation>\left( \begin{array}{c c c} - 1 & - 2 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right)</equation>计算 B的属于特征值2的特征向量.考虑（2E-B）x=0.<equation>2 E - B = \left( \begin{array}{c c c} 0 & - 1 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r ( 2 E-B)=2</equation>，求得<equation>\boldsymbol{\eta}_{1}^{\prime}=(1,0,0)^{\mathrm{T}}</equation>为（2E-B）<equation>\boldsymbol{x}=\mathbf{0}</equation>的一个基础解系. （1，0，0）<equation>^{\mathrm{T}}</equation>为B的属于特征值2的特征向量.

计算 B的属于特征值-1的特征向量.考虑<equation>(- E-B) x=0.</equation><equation>- \boldsymbol {E} - \boldsymbol {B} = \left( \begin{array}{c c c} - 3 & - 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {2} \leftrightarrow r _ {3} ]{r _ {1} \times (- 1)} \left( \begin{array}{c c c} 3 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r(-E-B)=2</equation>，求得<equation>\eta_{2}=(-1,3,0)^{\mathrm{T}}</equation>为<equation>(-E-B)x=0</equation>的一个基础解系.<equation>(-1,3,0)^{\mathrm{T}}</equation>为 B的属于特征值-1的特征向量.

计算 B的属于特征值-2的特征向量.考虑<equation>(-2 E-B) x=0.</equation><equation>- 2 E - B = \left( \begin{array}{c c c} - 4 & - 1 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {2} \times (- 1) ]{r _ {1} \times (- 1)} \left( \begin{array}{c c c} 4 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r(-2 E-B)=2</equation>，求得<equation>\eta_{3}=(0,0,1)^{\mathrm{T}}</equation>为<equation>(-2 E-B) x=0</equation>的一个基础解系.<equation>(0,0,1)^{\mathrm{T}}</equation>为 B的属于特征值-2的特征向量.

因此，<equation>P_{2}</equation>可取为<equation>\left( \begin{array}{c c c} 1 & -1 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>利用初等变换法计算<equation>P_{2}^{-1}</equation><equation>\left(\boldsymbol {P} _ {2}, \boldsymbol {E}\right) = \left( \begin{array}{c c c c c c} 1 & - 1 & 0 & 1 & 0 & 0 \\ 0 & 3 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {1} + r _ {2} ^ {*} ]{r _ {2} \times \frac {1}{3}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 1 & \frac {1}{3} & 0 \\ 0 & 1 & 0 & 0 & \frac {1}{3} & 0 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right).</equation>于是，<equation>P_{2}^{-1}=\left( \begin{array}{c c c} 1 & \frac{1}{3} & 0 \\ 0 & \frac{1}{3} & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>综上所述，<equation>\boldsymbol {P} = \boldsymbol {P} _ {1} \boldsymbol {P} _ {2} ^ {- 1} = \left( \begin{array}{c c c} - 1 & - 2 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right) \left( \begin{array}{c c c} 1 & \frac {1}{3} & 0 \\ 0 & \frac {1}{3} & 0 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} - 1 & - 1 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right).</equation>

---

**2018年第5题 | 选择题 | 4分 | 答案: A**

5. 下列矩阵中，与矩阵<equation>\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>A.

相似的为（    ）<equation>\left( \begin{array}{c c c} 1 & 1 & - 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c} 1 & 1 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>

答案: A

**解析:**解 已知矩阵与四个选项中的矩阵的特征多项式均为<equation>( x-1 )^{3}</equation>，故1为这五个矩阵的三重特征值.

记<equation>A=\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E-A=\left( \begin{array}{c c c} 0 & -1 & 0 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{array} \right).</equation>.于是<equation>r(E-A)=2.</equation>记<equation>B_{1}=\left( \begin{array}{c c c} 1 & 1 & -1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E-B_{1}=\left( \begin{array}{c c c} 0 & -1 & 1 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r \left( E-B_{1}\right) = 2.</equation>记<equation>B_{2}=\left( \begin{array}{c c c} 1 & 0 & -1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E-B_{2}=\left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r \left( E-B_{2}\right)=1.</equation>记<equation>B_{3}=\left( \begin{array}{c c c} 1 & 1 & -1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E-B_{3}=\left( \begin{array}{c c c} 0 & -1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r \left( E-B_{3}\right)=1.</equation>记<equation>B_{4} = \left( \begin{array}{c c c} 1 & 0 & -1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E - B_{4} = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r(\boldsymbol{E} - \boldsymbol{B}_4) = 1.</equation>由上可见，只有<equation>E - B_{1}</equation>与<equation>E - A</equation>的秩相等，而<equation>E - B_{i} ( i=2,3,4)</equation>与<equation>E - A</equation>的秩均不相等，故<equation>E - B_{i} ( i=2,3,4)</equation>与<equation>E - A</equation>不相似，从而A与<equation>B_{i} ( i=2,3,4)</equation>不相似.

由排除法可知，应选A.

---

**2017年第6题 | 选择题 | 4分 | 答案: B**

6. 已知矩阵<equation>A = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 1 \end{array} \right), B = \left( \begin{array}{c c c} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right), C = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{array} \right),</equation>则（    ）

A. A与 C相似，B与 C相似 B. A与 C相似，B与 C不相似

C. A与 C不相似，B与 C相似 D. A与 C不相似，B与 C不相似

答案: B

**解析:**解求得 A,B,C的特征多项式均为<equation>(\lambda-2)^{2} (\lambda-1)</equation>，故A,B,C具有相同的特征值，其中2是二重特征值.

矩阵 C是对角矩阵，故其相似于其自身.

考虑属于特征值2的特征向量.<equation>2 E - A = \left( \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 0 & - 1 \\ 0 & 0 & 1 \end{array} \right), \quad 2 E - B = \left( \begin{array}{c c c} 0 & - 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>由上可知，<equation>r ( 2 E-A )=1</equation><equation>r ( 2 E-B )=2</equation>.于是，<equation>( 2 E-A ) x=0</equation>的基础解系包含两个向量，故A有2个线性无关的属于特征值2的特征向量；而<equation>( 2 E-B ) x=0</equation>的基础解系只包含一个向量，故B只有1个属于特征值2的特征向量.

因此，加上属于特征值1的特征向量，A共有3个线性无关的特征向量，A与C相似；B只有2个线性无关的特征向量，B与C不相似.应选B.

---

**2016年第5题 | 选择题 | 4分 | 答案: C**

5. 设 A,B是可逆矩阵，且 A与 B相似，则下列结论错误的是（    )

A.<equation>A^{\mathrm{T}}</equation>与<equation>B^{\mathrm{T}}</equation>相似 B.<equation>A^{-1}</equation>与<equation>B^{-1}</equation>相似

C.<equation>A+A^{\mathrm{T}}</equation>与<equation>B+B^{\mathrm{T}}</equation>相似 D.<equation>A+A^{-1}</equation>与<equation>B+B^{-1}</equation>相似

答案: C

**解析:**由于 A与B相似，故存在可逆矩阵 P，使得<equation>B=P^{-1} A P.</equation>-<equation>\boldsymbol{B}^{\mathrm{T}}=\boldsymbol{P}^{\mathrm{T}}\boldsymbol{A}^{\mathrm{T}}(\boldsymbol{P}^{-1})^{\mathrm{T}}=\boldsymbol{P}^{\mathrm{T}}\boldsymbol{A}^{\mathrm{T}}(\boldsymbol{P}^{\mathrm{T}})^{-1}</equation>，选项A中的结论正确.

-<equation>B^{-1}=P^{-1} A^{-1} \left(P^{-1}\right)^{-1}=P^{-1} A^{-1} P</equation>，选项B中的结论正确.

- 由<equation>B=P^{-1} A P</equation>和<equation>B^{-1}=P^{-1} A^{-1} P</equation>可知，<equation>B+B^{-1}=P^{-1}(A+A^{-1}) P</equation>，选项D中的结论正确由排除法可知，应选C.

下面我们举例说明选项C不正确.

设<equation>A = \left( \begin{array}{cc}1 & 0\\ 0 & -1 \end{array} \right), P = \left( \begin{array}{cc}1 & 1\\ 2 & 1 \end{array} \right)</equation>，则<equation>P^{-1} = \left( \begin{array}{cc}-1 & 1\\ 2 & -1 \end{array} \right)</equation>. 令<equation>\boldsymbol {B} = \boldsymbol {P} ^ {- 1} \boldsymbol {A P} = \left( \begin{array}{c c} - 1 & 1 \\ 2 & - 1 \end{array} \right) \left( \begin{array}{c c} 1 & 0 \\ 0 & - 1 \end{array} \right) \left( \begin{array}{c c} 1 & 1 \\ 2 & 1 \end{array} \right) = \left( \begin{array}{c c} - 3 & - 2 \\ 4 & 3 \end{array} \right),</equation>则<equation>\boldsymbol {A} + \boldsymbol {A} ^ {\mathrm {T}} = \left( \begin{array}{c c} 2 & 0 \\ 0 & - 2 \end{array} \right), \quad \boldsymbol {B} + \boldsymbol {B} ^ {\mathrm {T}} = \left( \begin{array}{c c} - 6 & 2 \\ 2 & 6 \end{array} \right).</equation>计算<equation>A+A^{\mathrm{T}}</equation>的特征多项式得<equation>\lambda^{2}-4</equation>，计算<equation>B+B^{\mathrm{T}}</equation>的特征多项式得<equation>\lambda^{2}-40.</equation>因此<equation>\mathbf{A}+\mathbf{A}^{\mathrm{T}}</equation>和<equation>\mathbf{B}+\mathbf{B}^{\mathrm{T}}</equation>不相似.

---

**2016年第21题 | 解答题 | 11分**

21. （本题满分11分）

已知矩阵<equation>A = \left( \begin{array}{c c c} 0 & -1 & 1 \\ 2 & -3 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>I. 求<equation>A^{99}</equation>;

II. 设3阶矩阵<equation>B=(\alpha_{1},\alpha_{2},\alpha_{3})</equation>满足<equation>B^{2}=B A</equation>记<equation>B^{100}=(\beta_{1},\beta_{2},\beta_{3})</equation>将<equation>\beta_{1},\beta_{2},\beta_{3}</equation>分别表示为<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>的线性组合.

**答案:**(I)<equation>A^{99}=\left( \begin{array}{c c c} 2^{99}-2 & 1-2^{99} & 2-2^{98} \\ 2^{100}-2 & 1-2^{100} & 2-2^{99} \\ 0 & 0 & 0 \end{array} \right)</equation>（Ⅱ）<equation>\boldsymbol{\beta}_{1}=(2^{99}-2)\boldsymbol{\alpha}_{1}+(2^{100}-2)\boldsymbol{\alpha}_{2},\boldsymbol{\beta}_{2}=(1-2^{99})\boldsymbol{\alpha}_{1}+(1-2^{100})\boldsymbol{\alpha}_{2},\boldsymbol{\beta}_{3}=(2-2^{98})\boldsymbol{\alpha}_{1}</equation><equation>+ (2-2^{99})\boldsymbol{\alpha}_{2}.</equation>

**解析:**解（I）计算 A的特征多项式<equation>|\lambda E - A|</equation>.<equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda & 1 & - 1 \\ - 2 & \lambda + 3 & 0 \\ 0 & 0 & \lambda \end{array} \right| \xlongequal {\text {按 第三 行 展开}} \lambda \left(\lambda^ {2} + 3 \lambda + 2\right) = \lambda (\lambda + 1) (\lambda + 2).</equation>因此，A有3个不同的特征值：-2，-1，0.

由于属于不同特征值的特征向量线性无关，故A有3个线性无关的特征向量，A相似于对角矩阵<equation>\left( \begin{array}{c c c} - 2 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>分别计算 A的属于特征值-2，-1，0的特征向量.

当<equation>\lambda=-2</equation>时，解<equation>(-2 E-A) x=0</equation>.由于<equation>- 2 E - A = \left( \begin{array}{c c c} - 2 & 1 & - 1 \\ - 2 & 1 & 0 \\ 0 & 0 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} - 2 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right),</equation>故可取<equation>( 1, 2, 0 )^{\mathrm{T}}</equation>为 A的属于特征值-2的一个特征向量.

当<equation>\lambda=-1</equation>时，解<equation>(-E-A)x=0.</equation>由于<equation>- E - A = \left( \begin{array}{c c c} - 1 & 1 & - 1 \\ - 2 & 2 & 0 \\ 0 & 0 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right),</equation>故可取<equation>(1,1,0)^{\mathrm{T}}</equation>为<equation>A</equation>的属于特征值-1的一个特征向量.

当<equation>\lambda=0</equation>时，解（0E-A）x=0.由于<equation>0 E - A = \left( \begin{array}{c c c} 0 & 1 & - 1 \\ - 2 & 3 & 0 \\ 0 & 0 & 0 \end{array} \right),</equation>故可取（3，2，2）<equation>^{\mathrm{T}}</equation>为 A的属于特征值0的一个特征向量.

令<equation>P = \left( \begin{array}{c c c} 1 & 1 & 3 \\ 2 & 1 & 2 \\ 0 & 0 & 2 \end{array} \right)</equation>，则<equation>P^{-1}AP = \left( \begin{array}{c c c} - 2 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>.

计算<equation>P^{-1}</equation>得，<equation>P^{-1} = \left( \begin{array}{c c c} - 1 & 1 & \frac{1}{2} \\ 2 & - 1 & - 2 \\ 0 & 0 & \frac{1}{2} \end{array} \right).</equation><equation>\begin{aligned} \boldsymbol {A} ^ {9 9} &= \boldsymbol {P} \left( \begin{array}{c c c} (- 2) ^ {9 9} & 0 & 0 \\ 0 & (- 1) ^ {9 9} & 0 \\ 0 & 0 & 0  \right) \boldsymbol {P} ^ {- 1} &= \left( \begin{array}{c c c} 1 & 1 & 3 \\ 2 & 1 & 2 \\ 0 & 0 & 2  \right) \left( \begin{array}{c c c} - 2 ^ {9 9} & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0  \right) \left( \begin{array}{c c c} - 1 & 1 & \frac {1}{2} \\ 2 & - 1 & - 2 \\ 0 & 0 & \frac {1}{2}  \right) \\ &= \left( \begin{array}{c c c} 2 ^ {9 9} - 2 & 1 - 2 ^ {9 9} & 2 - 2 ^ {9 8} \\ 2 ^ {1 0 0} - 2 & 1 - 2 ^ {1 0 0} & 2 - 2 ^ {9 9} \\ 0 & 0 & 0  \right). \end{aligned}</equation>（Ⅱ）先求<equation>B^{100}.</equation>由于<equation>B^{2}=B A</equation>，故<equation>\boldsymbol {B} ^ {3} = \boldsymbol {B} \left(\boldsymbol {B} ^ {2}\right) = \boldsymbol {B} (\boldsymbol {B A}) = \boldsymbol {B} ^ {2} \boldsymbol {A} = (\boldsymbol {B A}) \boldsymbol {A} = \boldsymbol {B A} ^ {2}.</equation>下面我们用数学归纳法证明<equation>B^{n}=B A^{n-1}, n=2, 3, \dots</equation>当<equation>n = 2</equation>时，<equation>B^{2} = BA</equation>假设该命题对 n = k 成立，下面证明该命题对 n = k +1 也成立.<equation>\boldsymbol {B} ^ {n} = \boldsymbol {B} ^ {k + 1} = \boldsymbol {B} \boldsymbol {B} ^ {k} \xlongequal {\text {归 纳 假 设}} \boldsymbol {B} \left(\boldsymbol {B} \boldsymbol {A} ^ {k - 1}\right) = \boldsymbol {B} ^ {2} \boldsymbol {A} ^ {k - 1} = (\boldsymbol {B} \boldsymbol {A}) \boldsymbol {A} ^ {k - 1} = \boldsymbol {B} \boldsymbol {A} ^ {k} = \boldsymbol {B} \boldsymbol {A} ^ {n - 1}.</equation>于是，该命题对 n=k+1也成立，从而由数学归纳法可知，该命题对所有大于等于2的正整数均成立.

因此，<equation>\left(\boldsymbol {\beta} _ {1}, \boldsymbol {\beta} _ {2}, \boldsymbol {\beta} _ {3}\right) = \boldsymbol {B} ^ {1 0 0} = \boldsymbol {B A} ^ {9 9} = \left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\alpha} _ {2}, \boldsymbol {\alpha} _ {3}\right) \left( \begin{array}{c c c} 2 ^ {9 9} - 2 & 1 - 2 ^ {9 9} & 2 - 2 ^ {9 8} \\ 2 ^ {1 0 0} - 2 & 1 - 2 ^ {1 0 0} & 2 - 2 ^ {9 9} \\ 0 & 0 & 0 \end{array} \right).</equation>综上所述，<equation>\boldsymbol {\beta} _ {1} = \left(2 ^ {9 9} - 2\right) \boldsymbol {\alpha} _ {1} + \left(2 ^ {1 0 0} - 2\right) \boldsymbol {\alpha} _ {2},</equation><equation>\boldsymbol {\beta} _ {2} = \left(1 - 2 ^ {9 9}\right) \boldsymbol {\alpha} _ {1} + \left(1 - 2 ^ {1 0 0}\right) \boldsymbol {\alpha} _ {2},</equation><equation>\boldsymbol {\beta} _ {3} = \left(2 - 2 ^ {9 8}\right) \boldsymbol {\alpha} _ {1} + \left(2 - 2 ^ {9 9}\right) \boldsymbol {\alpha} _ {2}.</equation>

---

**2015年第21题 | 解答题 | 11分**

21. (本题满分11分)

设矩阵<equation>A = \left( \begin{array}{c c c} 0 & 2 & -3 \\ -1 & 3 & -3 \\ 1 & -2 & a \end{array} \right)</equation>相似于矩阵<equation>B = \left( \begin{array}{c c c} 1 & -2 & 0 \\ 0 & b & 0 \\ 0 & 3 & 1 \end{array} \right).</equation>I. 求 a,b的值；

II. 求可逆矩阵<equation>P</equation>，使<equation>P^{-1}AP</equation>为对角矩阵.

**答案:**(21) （I）<equation>a=4,b=5;</equation><equation>(\mathrm {I I}) \boldsymbol {P} = \left( \begin{array}{c c c} - 1 & 2 & - 3 \\ - 1 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right), \boldsymbol {P} ^ {- 1} \boldsymbol {A} \boldsymbol {P} = \left( \begin{array}{c c c} 5 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>

**解析:**解（I）由于A,B相似，故存在可逆矩阵Q使得<equation>Q^{-1} A Q=B</equation>，从而<equation>|B|=|Q^{-1}|\cdot|A|\cdot|Q|=|A|.</equation>计算得<equation>|A|=2 a-3,|B|=b.</equation>另一方面，A与B相似，故它们具有相同的迹，从而<equation>3+a=2+b.</equation>联立得<equation>\left\{\begin{array}{l l}a+3=b+2,\\2 a-3=b,\end{array}\right.</equation>解得<equation>\left\{\begin{array}{l l}a=4,\\b=5.\end{array}\right.</equation>（Ⅱ）由题设和第（Ⅰ）问得，<equation>| \lambda E - B | = \left| \begin{array}{c c c} \lambda - 1 & 2 & 0 \\ 0 & \lambda - 5 & 0 \\ 0 & - 3 & \lambda - 1 \end{array} \right| = (\lambda - 1) ^ {2} (\lambda - 5).</equation>从而<equation>B</equation>的特征值为1，1，5.由于<equation>A</equation>和<equation>B</equation>相似，故<equation>A</equation>的特征值也为1，1，5.

由第（I）问可得，<equation>A = \left( \begin{array}{c c c} 0 & 2 & -3 \\ -1 & 3 & -3 \\ 1 & -2 & 4 \end{array} \right).</equation>考虑<equation>A</equation>的属于特征值5的特征向量.<equation>\begin{array}{l} 5 E - A = \left( \begin{array}{c c c} 5 & - 2 & 3 \\ 1 & 2 & 3 \\ - 1 & 2 & 1 \end{array} \right) \xrightarrow {r _ {2} - r _ {3}} \frac {r _ {2} ^ {*} \times \frac {1}{2}}{r _ {2} ^ {*}} \left( \begin{array}{c c c} 5 & - 2 & 3 \\ 1 & 0 & 1 \\ - 1 & 2 & 1 \end{array} \right) \xrightarrow {r _ {3} + r _ {2} ^ {* *}} \frac {r _ {3} ^ {*} \times \frac {1}{2}}{r _ {3} ^ {*}} \left( \begin{array}{c c c} 5 & - 2 & 3 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} - 5 r _ {2} ^ {* *} + 2 r _ {3} ^ {* *}} \left( \begin{array}{c c c} 0 & 0 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right). \quad \text {关 注 公 众 号： 小 小 考 研} \quad \text {获 取 更 多 考 研 资 料} \\ \end{array}</equation>于是，<equation>r ( 5 E - A ) = 2</equation>，求得<equation>\xi_{1}=(-1,-1,1)^{\mathrm{T}}</equation>为<equation>( 5 E - A ) x = 0</equation>的一个基础解系.<equation>(-1,-1,1)^{\mathrm{T}}</equation>为A的属于特征值5的一个特征向量.

考虑<equation>A</equation>的属于特征值1的特征向量.<equation>\boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} 1 & - 2 & 3 \\ 1 & - 2 & 3 \\ - 1 & 2 & - 3 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & - 2 & 3 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r ( E - A ) = 1</equation>，求得<equation>\boldsymbol{\xi}_{2} = ( 2,1,0 )^{\mathrm{T}}</equation>和<equation>\boldsymbol{\xi}_{3} = (-3,0,1)^{\mathrm{T}}</equation>为<equation>( E - A ) x = 0</equation>的一个基础解系<equation>( 2,1,0 )^{\mathrm{T}}</equation>和<equation>(-3,0,1)^{\mathrm{T}}</equation>为A的属于特征值1的两个线性无关的特征向量.

取<equation>P = \left( \begin{array}{c c c} - 1 & 2 & - 3 \\ - 1 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right)</equation>，则<equation>P^{-1}AP = \left( \begin{array}{c c c} 5 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>.

---

**2014年第21题 | 解答题 | 11分**

21. (本题满分11分)

证明 n阶矩阵

相似.

**答案:**## (21) 证明略.

**解析:**证（法一）记<equation>A=\left( \begin{array}{c c c c} 1 & 1 & \dots & 1 \\ 1 & 1 & \dots & 1 \\ \vdots & \vdots & & \vdots \\ 1 & 1 & \dots & 1 \end{array} \right), B=\left( \begin{array}{c c c c} 0 & \dots & 0 & 1 \\ 0 & \dots & 0 & 2 \\ \vdots & & \vdots & \vdots \\ 0 & \dots & 0 & n \end{array} \right).</equation>由观察可知，<equation>r ( \mathbf{A} )=1</equation>，<equation>\operatorname{t r} ( \mathbf{A} )=n</equation>.又由于 A为实对称矩阵，故必相似于对角矩阵.由相似的矩阵具有相同的秩和迹可知， A相似于秩为1，迹为 n的对角矩阵，不妨记为<equation>\left( \begin{array}{c c c c} n & & & \\ & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right).</equation>另一方面，计算<equation>B</equation>的特征多项式得，<equation>| \lambda E - B | = \left| \begin{array}{c c c c} \lambda & 0 & \dots & - 1 \\ 0 & \lambda & & - 2 \\ \vdots & & \ddots & \vdots \\ 0 & \dots & 0 & \lambda - n \end{array} \right| = \lambda^ {n - 1} (\lambda - n).</equation>B的特征值为<equation>n,0,\dots ,0</equation>，其中0为<equation>n - 1</equation>重特征值.

由于<equation>0 E-B=\left( \begin{array}{c c c c} 0 & & -1 \\ 0 & & -2 \\ & \ddots & \vdots \\ & & -n \end{array} \right)</equation>，故<equation>r(0 E-B)=1. ( 0 E-B ) x=0</equation>有 n-1个线性无关的解.

B有 n-1个属于特征值0的线性无关的特征向量，再加上B的属于n的特征向量，B共有n个线性无关的特征向量.从而B也相似于<equation>\left( \begin{array}{c c c c} n & & \\ 0 & & \\ & \ddots & \\ & & 0 \end{array} \right).</equation>因此，存在可逆矩阵 P,Q，使得<equation>P^{-1} A P=Q^{-1} B Q=\left( \begin{array}{c c c c} n & & \\ 0 & & \\ & \ddots & \\ & & 0 \end{array} \right).</equation>于是<equation>Q P^{-1} A P Q^{-1}=B.</equation>令<equation>U=P Q^{-1}</equation>，则<equation>B=U^{-1} A U</equation>即A和B相似.

（法二）计算 A的特征多项式.<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c c c} \lambda - 1 & - 1 & \dots & \dots & - 1 \\ - 1 & \lambda - 1 & - 1 & \dots & - 1 \\ \vdots & \ddots & \ddots & \ddots & \vdots \\ \vdots & \ddots & \ddots & \ddots & - 1 \\ - 1 & \dots & \dots & - 1 & \lambda - 1  \right| \frac {c _ {1} + \left(c _ {2} + c _ {3} + \dots + c _ {n}\right)}{\hbar} \left| \begin{array}{c c c c c} \lambda - n & - 1 & \dots & \dots & - 1 \\ \lambda - n & \lambda - 1 & - 1 & \dots & - 1 \\ \lambda - n & \ddots & \ddots & \ddots & \vdots \\ \vdots & \ddots & \ddots & \ddots & - 1 \\ \lambda - n & - 1 & \dots & - 1 & \lambda - 1  \right| \\ &= (\lambda - n) \left| \begin{array}{c c c c c} 1 & - 1 & \dots & \dots & - 1 \\ 1 & \lambda - 1 & - 1 & \dots & - 1 \\ 1 & \ddots & \ddots & \ddots & \vdots \\ \vdots & \ddots & \ddots & \ddots & - 1 \\ 1 & - 1 & \dots & - 1 & \lambda - 1  \right| \frac {c _ {i} + c _ {1}}{i = 2 , \dots , n} (\lambda - n) \left| \begin{array}{c c c c c} 1 & 0 & \dots & \dots & 0 \\ 1 & \lambda & 0 & \dots & 0 \\ 1 & \ddots & \ddots & \ddots & \vdots \\ \vdots & \ddots & \ddots & \ddots & 0 \\ 1 & 0 & \dots & 0 & \lambda  \right| \\ &= \lambda^ {n - 1} (\lambda - n). \end{aligned}</equation>由于 A为实对称矩阵，故由 A的特征多项式为<equation>\lambda^{n-1} (\lambda-n)</equation>可知 A相似于对角矩阵<equation>\left( \begin{array}{c c c c} n & & & \\ & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right).</equation>其余同法一.

---

**2013年第6题 | 选择题 | 4分 | 答案: B**

6. 矩阵

相似的充分必要条件为（    ）

A. a=0,b=2 B. a=0,b为任意常数 C. a=2,b=0 D. a=2,b为任意常数

答案: B

**解析:**解 矩阵<equation>\left( \begin{array}{lll}1&a&1\\ a&b&a\\ 1&a&1 \end{array} \right)</equation>与<equation>\left( \begin{array}{lll}2&0&0\\ 0&b&0\\ 0&0&0 \end{array} \right)</equation>均为实对称矩阵，故它们相似等价于它们有相同的特征多项式.

矩阵<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>的特征多项式为<equation>f (\lambda)=\lambda(\lambda-2)(\lambda-b).</equation>考虑矩阵<equation>A = \left( \begin{array}{c c c} 1 & a & 1 \\ a & b & a \\ 1 & a & 1 \end{array} \right)</equation>的特征多项式<equation>g(\lambda)</equation>.<equation>g (\lambda) = | \lambda E - A | = \left| \begin{array}{c c c} \lambda - 1 & - a & - 1 \\ - a & \lambda - b & - a \\ - 1 & - a & \lambda - 1 \end{array} \right| = \lambda \left[ (\lambda - 2) (\lambda - b) - 2 a ^ {2} \right].</equation>由于<equation>f(\lambda)-g(\lambda)=2 a^{2} \lambda</equation>，故<equation>f(\lambda)=g(\lambda)</equation>当且仅当 a=0.由于上述论证不涉及到b，故b取任意常数均不影响结果.应选B.

---

**2010年第6题 | 选择题 | 4分 | 答案: D**

6. 设 A为4阶实对称矩阵，且<equation>A^{2}+A=O</equation>. 若 A的秩为3，则 A相似于（    ）

A.<equation>\left( \begin{array}{c c c c} 1 & & \\ & 1 & \\ & & 1 \\ & & 0 \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c c} 1 & & \\ & 1 & \\ & & - 1 \\ & & 0 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c c} 1 & & \\ & - 1 & \\ & & - 1 \\ & & 0 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c c} - 1 & & \\ & - 1 & \\ & & - 1 \\ & & 0 \end{array} \right)</equation>

答案: D

**解析:**解（法一）不妨设<equation>\lambda</equation>为 A的特征值，<equation>\alpha</equation>为其对应的特征向量.由<equation>A^{2}+A=O</equation>得，<equation>(A^{2}+A)\alpha=0.</equation>代入<equation>A\alpha=\lambda\alpha</equation>得，<equation>(\lambda^{2}+\lambda)\alpha=0.</equation>又由于<equation>\alpha</equation>非零，故<equation>\lambda^{2}+\lambda=0, \lambda=0</equation>或<equation>\lambda=-1.</equation>由于 A为实对称矩阵，故 A相似于对角矩阵.又因为<equation>r ( A )=3</equation>，所以对角矩阵的秩也为3，<equation>\lambda=-1</equation>是 A的三重特征值，A相似于<equation>\left( \begin{array}{c c c c} - 1 & & & \\ & - 1 & & \\ & & - 1 & \\ & & & 0 \end{array} \right)</equation>.应选D.

（法二）由于 A为实对称矩阵，故存在可逆矩阵 P使得<equation>P^{-1} A P=\left( \begin{array}{c c c c} \lambda_{1} & & & \\ & \lambda_{2} & & \\ & & \lambda_{3} & \\ & & & \lambda_{4} \end{array} \right).</equation>从而<equation>\begin{aligned} \boldsymbol {O} &= \boldsymbol {A} ^ {2} + \boldsymbol {A} = \boldsymbol {P} \left( \begin{array}{c c c c} \lambda_ {1} ^ {2} & & & \\ & \lambda_ {2} ^ {2} & & \\ & & \lambda_ {3} ^ {2} & \\ & & & \lambda_ {4} ^ {2}  \right) \boldsymbol {P} ^ {- 1} + \boldsymbol {P} \left( \begin{array}{c c c c} \lambda_ {1} & & & \\ & \lambda_ {2} & & \\ & & \lambda_ {3} & \\ & & & \lambda_ {4}  \right) \boldsymbol {P} ^ {- 1} \\ &= \boldsymbol {P} \left( \begin{array}{c c c c} \lambda_ {1} ^ {2} + \lambda_ {1} & & & \\ & \lambda_ {2} ^ {2} + \lambda_ {2} & & \\ & & \lambda_ {3} ^ {2} + \lambda_ {3} & \\ & & & \lambda_ {4} ^ {2} + \lambda_ {4}  \right) \boldsymbol {P} ^ {- 1}. \end{aligned}</equation>因此<equation>\lambda_{i}^{2}+\lambda_{i}=0 ( i=1,2,3,4).</equation>解得<equation>\lambda_{i}=0</equation>或<equation>\lambda_{i}=-1 ( i=1,2,3,4).</equation>又由于 r（A）=3，故A相似于<equation>\left( \begin{array}{c c c c} - 1 & & & \\ & - 1 & & \\ & & - 1 & \\ & & & 0 \end{array} \right).</equation>应选D.

---

**2009年第13题 | 填空题 | 4分**

13. 设<equation>\alpha=(1,1,1)^{\mathrm{T}}</equation><equation>\beta=(1,0,k)^{\mathrm{T}}</equation>，若矩阵<equation>\alpha\beta^{\mathrm{T}}</equation>相似于<equation>\left( \begin{array}{c c c} {3} & {0} & {0} \\ {0} & {0} & {0} \\ {0} & {0} & {0} \end{array} \right)</equation>，则 k=___

**解析:**解（法一）计算得<equation>\boldsymbol{\alpha}\boldsymbol{\beta}^{\mathrm{T}}=\left( \begin{array}{c c c} 1 & 0 & k \\ 1 & 0 & k \\ 1 & 0 & k \end{array} \right).</equation>由于相似矩阵的迹相等，即其主对角线上元素之和相等，故<equation>1+0+k=3+0+0.</equation>因此，<equation>k = 2</equation>（法二）由于相似矩阵的特征值相等，故3是<equation>\alpha \beta^{\mathrm{T}} = \left( \begin{array}{c c c} 1 & 0 & k \\ 1 & 0 & k \\ 1 & 0 & k \end{array} \right)</equation>的特征值. 从而，<equation>\left| 3 E - \alpha \beta^ {\mathrm {T}} \right| = \left| \begin{array}{c c c} 2 & 0 & - k \\ - 1 & 3 & - k \\ - 1 & 0 & 3 - k \end{array} \right| = 3 \left| \begin{array}{c c} 2 & - k \\ - 1 & 3 - k \end{array} \right| = 3 (6 - 3 k) = 0.</equation>因此，<equation>k = 2</equation>（法三）计算<equation>\alpha\beta^{\mathrm{T}}</equation>的特征值.<equation>| \lambda E - \alpha \boldsymbol {\beta} ^ {\mathrm {T}} | = \left| \begin{array}{c c c} \lambda - 1 & 0 & - k \\ - 1 & \lambda & - k \\ - 1 & 0 & \lambda - k \end{array} \right| = \lambda \left| \begin{array}{c c} \lambda - 1 & - k \\ - 1 & \lambda - k \end{array} \right| = \lambda^ {2} [ \lambda - (k + 1) ].</equation>特征值为0,0,k+1.又由相似矩阵的特征值相等可知<equation>k + 1 = 3</equation>.因此，<equation>k = 2.</equation>

---


#### 特征值与特征向量


**2024年第15题 | 填空题 | 5分**

15. 设 A为3阶矩阵，<equation>A^{*}</equation>为的 A伴随矩阵，E为3阶单位矩阵，若<equation>r(2 E-A)=1,r(E+A)=2</equation>，则<equation>|A^{*}|=</equation>___

**答案:**## 16

**解析:**解 由于<equation>r ( 2 E-A )=1</equation>，故由系数矩阵的秩与解集的秩的关系可知，方程组<equation>( 2 E-A ) x=0</equation>有3-1=2个线性无关的解，从而矩阵A有两个线性无关的属于特征值2的特征向量.

同理，由于<equation>r ( E+A) = 2</equation>即<equation>r (-E-A)=2</equation>故由系数矩阵的秩与解集的秩的关系可知，方程组<equation>(-E-A) x=0</equation>有3-2=1个线性无关的解，从而矩阵A有一个线性无关的属于特征值-1的特征向量.

由于属于不同特征值的特征向量线性无关，故矩阵<equation>A</equation>至少有三个线性无关的特征向量.结合<equation>A</equation>是3阶矩阵可得，<equation>A</equation>共有三个线性无关的特征向量，从而<equation>A</equation>相似于对角矩阵<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & - 1 \end{array} \right)</equation><equation>A</equation>的特征值为2，2，-1，<equation>|A|=-4.</equation>由<equation>AA^{*} = |A|E</equation>可得，<equation>|AA^{*}| = |A| |A^{*}| = |A|^{3}</equation>，故<equation>|A^{*}| = |A|^{2} = 16.</equation>或者，由伴随矩阵与矩阵的特征值的关系可知，<equation>A^{*}</equation>的特征值为<equation>\frac{|A|}{2},\frac{|A|}{2},\frac{|A|}{-1}</equation>即-2，-2，

4. 因此，<equation>|A^{*}| = (-2)\times(-2)\times 4 = 16.</equation>

---

**2020年第6题 | 选择题 | 4分 | 答案: D**

6. 设 A为3阶矩阵，<equation>\alpha_{1},\alpha_{2}</equation>为 A的属于特征值1的线性无关的特征向量，<equation>\alpha_{3}</equation>为 A的属于特征值-1的特征向量，则满足<equation>P^{-1}AP=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>的可逆矩阵 P为（    ）

A.<equation>\left( \alpha_{1}+\alpha_{3},\alpha_{2},-\alpha_{3} \right)</equation>B.<equation>\left( \alpha_{1}+\alpha_{2},\alpha_{2},-\alpha_{3} \right)</equation>C.<equation>\left( \alpha_{1}+\alpha_{3},-\alpha_{3},\alpha_{2} \right)</equation>D.<equation>\left( \alpha_{1}+\alpha_{2},-\alpha_{3},\alpha_{2} \right)</equation>

答案: D

**解析:**解 由于<equation>P^{-1} A P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，故 P的列向量应分别为属于特征值1，-1，1的特征向量，且

第1列与第3列为属于特征值1的线性无关的特征向量.

由已知条件，<equation>\alpha_{3}</equation>为 A的属于特征值-1的特征向量，故 P的第2列可取为<equation>k\alpha_{3}</equation>其中 k为任意非零常数.

由于<equation>\alpha_{1},\alpha_{2}</equation>为 A的属于特征值1的线性无关的特征向量，且<equation>\left(\alpha_{1}+\alpha_{2},\alpha_{2}\right)=\left(\alpha_{1},\alpha_{2}\right)\left( \begin{array}{cc}1&0\\ 1&1 \end{array} \right)</equation>故<equation>\alpha_{1}+\alpha_{2}</equation>也为 A的属于特征值1的特征向量，且与<equation>\alpha_{2}</equation>线性无关.

因此，<equation>P</equation>可取为<equation>\left(\alpha_{1}+\alpha_{2},-\alpha_{3},\alpha_{2}\right).</equation>应选D.

---

**2018年第13题 | 填空题 | 4分**

13. 设 A为3阶矩阵，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>是线性无关的向量组. 若<equation>A\alpha_{1}=\alpha_{1}+\alpha_{2},A\alpha_{2}=\alpha_{2}+\alpha_{3},A\alpha_{3}=\alpha_{1}+\alpha_{3}</equation>，则<equation>|A|=</equation>

**解析:**解记<equation>P=(\alpha_{1},\alpha_{2},\alpha_{3})</equation>.由于<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关，故P可逆由题设可知，<equation>A P = A \left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) = \left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) \left( \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{array} \right) = P \left( \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{array} \right).</equation>记<equation>B=\left( \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{array} \right).</equation>.于是，<equation>A=P B P^{-1}.</equation>因此，<equation>| A | = | P | \cdot | B | \cdot | P ^ {- 1} | = | B | = \left| \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{array} \right| = 2.</equation>

---

**2015年第13题 | 填空题 | 4分**

13. 设 3 阶矩阵<equation>\boldsymbol{A}</equation>的特征值为 2,-2,1,<equation>\boldsymbol{B}=\boldsymbol{A}^{2}-\boldsymbol{A}+\boldsymbol{E}</equation>,其中<equation>\boldsymbol{E}</equation>为 3 阶单位矩阵,则行列式<equation>|\boldsymbol{B}|=</equation>___.

**解析:**解（法一）由于 A有3个不同的特征值，故 A有3个线性无关的特征向量，从而存在可逆矩阵 P使得<equation>P^{-1} A P=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>.于是<equation>\boldsymbol {A} = \boldsymbol {P} \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & - 2 & 0 \\ 0 & 0 & 1 \end{array} \right) \boldsymbol {P} ^ {- 1}, \quad \boldsymbol {A} ^ {2} = \boldsymbol {P} \left( \begin{array}{c c c} 2 ^ {2} & 0 & 0 \\ 0 & (- 2) ^ {2} & 0 \\ 0 & 0 & 1 ^ {2} \end{array} \right) \boldsymbol {P} ^ {- 1},</equation><equation>\boldsymbol {B} = \boldsymbol {P} \left( \begin{array}{c c c} 2 ^ {2} - 2 + 1 & 0 & 0 \\ 0 & (- 2) ^ {2} - (- 2) + 1 & 0 \\ 0 & 0 & 1 ^ {2} - 1 + 1 \end{array} \right) \boldsymbol {P} ^ {- 1} = \boldsymbol {P} \left( \begin{array}{c c c} 3 & 0 & 0 \\ 0 & 7 & 0 \\ 0 & 0 & 1 \end{array} \right) \boldsymbol {P} ^ {- 1}.</equation>因此，<equation>|\boldsymbol{B}| = 21\cdot |\boldsymbol{P}| \cdot |\boldsymbol{P}^{-1}| = 21.</equation>（法二）设<equation>\alpha</equation>为矩阵<equation>A</equation>的属于特征值<equation>\lambda</equation>的特征向量，即<equation>A\alpha = \lambda \alpha</equation>，则<equation>\boldsymbol {B} \alpha = \left(\boldsymbol {A} ^ {2} - \boldsymbol {A} + \boldsymbol {E}\right) \alpha = \left(\lambda^ {2} - \lambda + 1\right) \alpha .</equation>由上可见，若<equation>\alpha</equation>为<equation>A</equation>的属于特征值<equation>\lambda</equation>的特征向量，则<equation>\alpha</equation>为<equation>B</equation>的属于特征值<equation>\lambda^2 - \lambda +1</equation>的特征向量.<equation>A</equation>的3个线性无关的特征向量也是<equation>B</equation>的3个线性无关的特征向量，对应的特征值为<equation>\lambda^2 - \lambda +1</equation>（<equation>\lambda = 2,-2,1</equation>）.由此可求得<equation>B</equation>的特征值为3,7,1.

因此，<equation>|B| = 3\times 7\times 1 = 21.</equation>

---

**2011年第21题 | 解答题 | 11分**


设<equation>A</equation>为3阶实对称矩阵，<equation>A</equation>的秩为2，且<equation>1 \left( \begin{array}{c c} 1 & 1 \\ 0 & 0 \\ - 1 & 1 \end{array} \right) = \left( \begin{array}{c c} - 1 & 1 \\ 0 & 0 \\ 1 & 1 \end{array} \right)</equation>I. 求 A的所有特征值与特征向量；

II. 求矩阵 A.

**答案:**(21) （I）特征值-1，1，0，分别对应特征向量<equation>k_{1}(1,0,-1)^{\mathrm{T}}, k_{2}(1,0,1)^{\mathrm{T}}, k_{3}(0,1,0)^{\mathrm{T}}</equation>，其中<equation>k_{1}, k_{2},</equation><equation>k_{3}</equation>为任意非零常数；（Ⅱ）<equation>\left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{array} \right).</equation>

**解析:**解（I）由于<equation>A\left( \begin{array}{c c} 1 & 1 \\ 0 & 0 \\ - 1 & 1 \end{array} \right)=\left( \begin{array}{c c} - 1 & 1 \\ 0 & 0 \\ 1 & 1 \end{array} \right)</equation>，故<equation>\alpha_{1}=(1,0,-1)^{\mathrm{T}}</equation>，<equation>\alpha_{2}=(1,0,1)^{\mathrm{T}}</equation>满足<equation>A\alpha_{1}=</equation><equation>-\alpha_{1},A\alpha_{2}=\alpha_{2}</equation>，从而<equation>\alpha_{1}</equation>为A的属于特征值-1的一个特征向量，<equation>\alpha_{2}</equation>为A的属于特征值1的一个特征向量.

又因为<equation>r(\mathbf{A}) = 2</equation>，<equation>|\mathbf{A}| = 0</equation>，所以<equation>\mathbf{A}</equation>还有一个特征值为零.

因为实对称矩阵属于不同特征值的特征向量相互正交，所以 A的属于特征值0的特征向量<equation>\boldsymbol{\alpha}_{3}=(x_{1},x_{2},x_{3})^{\mathrm{T}}</equation>满足<equation>\boldsymbol{\alpha}_{1}^{\mathrm{T}}\boldsymbol{\alpha}_{3}=0</equation><equation>\boldsymbol{\alpha}_{2}^{\mathrm{T}}\boldsymbol{\alpha}_{3}=0</equation>从而得<equation>\left\{ \begin{array}{l l} x_{1}-x_{3}=0, \\ x_{1}+x_{3}=0. \end{array} \right.</equation>由此可得<equation>\boldsymbol{\alpha}_{3}=k_{3}(0,1,0)^{\mathrm{T}}</equation>其中<equation>k_{3}</equation>为任意非零常数.

因此，<equation>\mathbf{A}</equation>的特征值为-1,1,0.对应的特征向量分别为<equation>k_{1}(1,0,-1)^{\mathrm{T}}</equation><equation>k_{2}(1,0,1)^{\mathrm{T}}</equation><equation>k_{3}(0,1,0)^{\mathrm{T}}</equation>其中<equation>k_{1},k_{2},k_{3}</equation>为任意非零常数.

（Ⅱ）（法一）由第（I）问可知，取<equation>P=\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)=\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \\ -1 & 1 & 0 \end{array} \right)</equation>，可得<equation>P^{-1}AP=</equation><equation>\left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>于是<equation>A=P\left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right) P^{-1}.</equation>利用初等变换法计算<equation>P^{-1}.</equation><equation>\begin{array}{l} (P, E) = \left( \begin{array}{c c c c c c} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 1 & 0 \\ - 1 & 1 & 0 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} + r _ {1}} \left( \begin{array}{c c c c c c} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 1 & 0 \\ 0 & 2 & 0 & 1 & 0 & 1 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {*} \times \frac {1}{2}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & \frac {1}{2} & 0 & - \frac {1}{2} \\ 0 & 0 & 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & \frac {1}{2} & 0 & \frac {1}{2} \end{array} \right) \xrightarrow {r _ {2} \leftrightarrow r _ {3} ^ {* *}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & \frac {1}{2} & 0 & - \frac {1}{2} \\ 0 & 1 & 0 & \frac {1}{2} & 0 & \frac {1}{2} \\ 0 & 0 & 1 & 0 & 1 & 0 \end{array} \right). \\ \end{array}</equation>于是，<equation>P^{-1} = \left( \begin{array}{c c c} \frac{1}{2} & 0 & -\frac{1}{2} \\ \frac{1}{2} & 0 & \frac{1}{2} \\ 0 & 1 & 0 \end{array} \right).</equation>因此，<equation>\begin{aligned} \boldsymbol {A} &= \boldsymbol {P} \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \boldsymbol {P} ^ {- 1} &= \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \\ - 1 & 1 & 0  \right) \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \left( \begin{array}{c c c} \frac {1}{2} & 0 & - \frac {1}{2} \\ \frac {1}{2} & 0 & \frac {1}{2} \\ 0 & 1 & 0  \right) \\ &= \left( \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & 0 & 0 \\ 1 & 1 & 0  \right) \left( \begin{array}{c c c} \frac {1}{2} & 0 & - \frac {1}{2} \\ \frac {1}{2} & 0 & \frac {1}{2} \\ 0 & 1 & 0  \right) &= \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0  \right). \end{aligned}</equation>或者，由<equation>A P = \left(A \alpha_ {1}, A \alpha_ {2}, A \alpha_ {3}\right) = \left(- \alpha_ {1}, \alpha_ {2}, 0\right)</equation>可得，<equation>\boldsymbol {A} = \left(- \alpha_ {1}, \alpha_ {2}, 0\right) \boldsymbol {P} ^ {- 1} = - \frac {1}{2} \left( \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & 0 & 0 \\ 1 & 1 & 0 \end{array} \right) \left( \begin{array}{c c c} - 1 & 0 & 1 \\ - 1 & 0 & - 1 \\ 0 & - 2 & 0 \end{array} \right) = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{array} \right).</equation>（法二）将<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>单位化，组成一正交矩阵<equation>Q = \left( \begin{array}{c c c} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0 \\ 0 & 0 & 1 \\ -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0 \end{array} \right)</equation>，则<equation>Q^{\mathrm{T}}AQ = \left( \begin{array}{c c c} -1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>.

因此，<equation>\begin{aligned} \boldsymbol {A} &= \boldsymbol {Q} \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \boldsymbol {Q} ^ {\mathrm {T}} &= \left( \begin{array}{c c c} \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {2}} & 0 \\ 0 & 0 & 1 \\ - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {2}} & 0  \right) \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \left( \begin{array}{c c c} \frac {1}{\sqrt {2}} & 0 & - \frac {1}{\sqrt {2}} \\ \frac {1}{\sqrt {2}} & 0 & \frac {1}{\sqrt {2}} \\ 0 & 1 & 0  \right) \\ &= \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0  \right). \end{aligned}</equation>

---

**2010年第21题 | 解答题 | 11分**

21. (本题满分11分)

设<equation>A=\left( \begin{array}{c c c} 0 & -1 & 4 \\ -1 & 3 & a \\ 4 & a & 0 \end{array} \right)</equation>，正交矩阵Q使<equation>Q^{\mathrm{T}}AQ</equation>为对角矩阵，若Q的第1列为<equation>\frac{1}{\sqrt{6}}(1,2,1)^{\mathrm{T}}</equation>，求a和Q.

**答案:**<equation>a = - 1, Q = \left( \begin{array}{c c c} \frac {1}{\sqrt {6}} & - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {3}} \\ \frac {2}{\sqrt {6}} & 0 & - \frac {1}{\sqrt {3}} \\ \frac {1}{\sqrt {6}} & \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {3}} \end{array} \right), Q ^ {\mathrm {T}} A Q = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & - 4 & 0 \\ 0 & 0 & 5 \end{array} \right).</equation>

**解析:**解 由题设知，<equation>\alpha_{1}=\frac{1}{\sqrt{6}}(1,2,1)^{\mathrm{T}}</equation>为 A的一个特征向量.不妨设<equation>\alpha_{1}</equation>对应的特征值为 k，则<equation>\begin{aligned} \boldsymbol {A} \boldsymbol {\alpha} _ {1} &= \frac {1}{\sqrt {6}} \left( \begin{array}{c c c} 0 & - 1 & 4 \\ - 1 & 3 & a \\ 4 & a & 0  \right) \left(  1 \\ 2 \\ 1  \right) &= \frac {1}{\sqrt {6}} \left( \begin{array}{c} 2 \\ 5 + a \\ 4 + 2 a  \right) &= \frac {k}{\sqrt {6}} \left(  1 \\ 2 \\ 1  \right). \end{aligned}</equation>从而<equation>\left\{ \begin{array}{l}2 = k,\\ 5 + a = 2k,\\ 4 + 2a = k, \end{array} \right.</equation>解得<equation>a = -1</equation>，<equation>k = 2.</equation>于是，<equation>A = \left( \begin{array}{c c c}0 & -1 & 4\\ -1 & 3 & -1\\ 4 & -1 & 0 \end{array} \right).</equation>计算 A的特征多项式得<equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda & 1 & - 4 \\ 1 & \lambda - 3 & 1 \\ - 4 & 1 & \lambda \end{array} \right| = (\lambda - 2) (\lambda - 5) (\lambda + 4).</equation>因此，<equation>A</equation>的特征值为2，5，-4.<equation>\alpha_{1}</equation>是<equation>A</equation>的属于特征值2的特征向量.

先求属于特征值-4的单位特征向量<equation>\alpha_{2}</equation>.由特征向量的定义可知，<equation>(-4E - A)x = 0.</equation><equation>\begin{array}{l} - 4 E - A = \left( \begin{array}{c c c} - 4 & 1 & - 4 \\ 1 & - 7 & 1 \\ - 4 & 1 & - 4 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c} - 4 & 1 & - 4 \\ 1 & - 7 & 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} + 4 r _ {2}} \left( \begin{array}{c c c} 0 & 1 & 0 \\ 1 & - 7 & 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} + 7 r _ {1} ^ {* *}} \binom {1} {r _ {1} ^ {* *} \leftrightarrow r _ {2} ^ {*}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>由此可得<equation>\left\{\begin{array}{l l}x_{1}+x_{3}=0,\\ x_{2}=0,\end{array}\right.</equation>故<equation>\boldsymbol{\xi}_{2}=(-1,0,1)^{\mathrm{T}}</equation>为该方程组的一个基础解系.将<equation>\boldsymbol{\xi}_{2}</equation>单位化得<equation>\boldsymbol{\alpha}_{2}=</equation><equation>\frac{1}{\sqrt{2}}(-1,0,1)^{\mathrm{T}}.</equation>同理，解（5E-A）<equation>x=0.</equation><equation>\begin{array}{l} 5 E - A = \left( \begin{array}{c c c} 5 & 1 & - 4 \\ 1 & 2 & 1 \\ - 4 & 1 & 5 \end{array} \right) \xrightarrow {r _ {3} + r _ {1} - r _ {2}} \left( \begin{array}{c c c} 5 & 1 & - 4 \\ 1 & 2 & 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} - 5 r _ {2}} \left( \begin{array}{c c c} 0 & 1 & 1 \\ 1 & 2 & 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} - r _ {1} ^ {* *}} \frac {1}{r _ {1} ^ {* *} \leftrightarrow r _ {2} ^ {*}} \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>由此可得<equation>\left\{\begin{array}{l l}x_{1}+x_{2}=0,\\ x_{2}+x_{3}=0,\end{array} \right.</equation>故<equation>\boldsymbol{\xi}_{3}=(1,-1,1)^{\mathrm{T}}</equation>为该方程组的一个基础解系.将<equation>\boldsymbol{\xi}_{3}</equation>单位化得<equation>\boldsymbol{\alpha}_{3}=</equation><equation>\frac{1}{\sqrt{3}}(1,-1,1)^{\mathrm{T}}.</equation>或者也可以如下求<equation>\boldsymbol{\alpha}_{3}.</equation>由于<equation>\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2}</equation>为属于不同特征值的特征向量，故它们相互正交.于是<equation>\boldsymbol {\alpha} _ {3} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {1} = 0, \quad \boldsymbol {\alpha} _ {3} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {2} = 0.</equation><equation>\pmb{\alpha}_{3}</equation>的坐标<equation>(x_{1}, x_{2}, x_{3})^{\mathrm{T}}</equation>满足<equation>\left\{ \begin{array}{l} x_{1} + 2x_{2} + x_{3} = 0, \\ x_{1} - x_{3} = 0. \end{array} \right.</equation>因此可得<equation>\pmb{\xi}_{3} = (1, -1, 1)^{\mathrm{T}}</equation>为该方程组的一个基础解系.将<equation>\pmb{\xi}_{3}</equation>单位化得<equation>\pmb{\alpha}_{3} = \frac{1}{\sqrt{3}} (1, -1, 1)^{\mathrm{T}}.</equation>综上所述，<equation>a = -1</equation>，<equation>Q = \left( \begin{array}{c c c} \frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} \\ \frac{2}{\sqrt{6}} & 0 & -\frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{6}} & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} \end{array} \right)</equation>，<equation>Q^{\mathrm{T}}AQ = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -4 & 0 \\ 0 & 0 & 5 \end{array} \right)</equation>

---


### 二次型

### 行列式

### 向量

#### 向量组之间的线性表示


**2025年第21题 | 解答题 | 12分**

21. 设矩阵<equation>A = \left( \begin{array}{c c c c c} 1 & -1 & 3 & 0 & -1 \\ -1 & 0 & -2 & -a & -1 \\ 1 & 1 & a & 2 & 3 \end{array} \right)</equation>的秩为2.

I. 求 a的值；

II. 求<equation>A</equation>的列向量组的一个极大线性无关组<equation>\alpha, \beta</equation>，并求矩阵<equation>H</equation>，使得<equation>A = GH</equation>，其中<equation>G = (\alpha ,\beta)</equation>

**答案:**（ I ）<equation>a=1;</equation>（Ⅱ）<equation>A</equation>的前两列<equation>\alpha=\left( \begin{array}{c}1\\ -1\\ 1 \end{array} \right),\beta=\left( \begin{array}{c}-1\\ 0\\ 1 \end{array} \right)</equation>构成A的列向量组的一个极大线性无关组.令<equation>H=</equation><equation>\left( \begin{array}{c c c c}1&0&2&1&1\\ 0&1&-1&1&2 \end{array} \right)</equation>，则<equation>A=GH</equation>，其中<equation>G=(\alpha ,\beta).</equation>

**解析:**解（I）对矩阵A做初等行变换.<equation>\begin{array}{l} A = \left( \begin{array}{c c c c c} 1 & - 1 & 3 & 0 & - 1 \\ - 1 & 0 & - 2 & - a & - 1 \\ 1 & 1 & a & 2 & 3 \end{array} \right) \xrightarrow [ r _ {3} - r _ {1} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c c} 1 & - 1 & 3 & 0 & - 1 \\ 0 & - 1 & 1 & - a & - 2 \\ 0 & 2 & a - 3 & 2 & 4 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c} 1 & - 1 & 3 & 0 & - 1 \\ 0 & - 1 & 1 & - a & - 2 \\ 0 & 0 & a - 1 & 2 - 2 a & 0 \end{array} \right). \\ \end{array}</equation>由上式可得，当且仅当<equation>a = 1</equation>时，<equation>r(A) = 2.</equation>因此，<equation>a = 1</equation>（Ⅱ）由第（I）问可知，<equation>A=\left( \begin{array}{c c c c c} 1 & -1 & 3 & 0 & -1 \\ -1 & 0 & -2 & -1 & -1 \\ 1 & 1 & 1 & 2 & 3 \end{array} \right).</equation>由于<equation>r(A)=2</equation>，故A的列秩为2又因为A的第一列与第二列线性无关，所以A的第一列与第二列构成A的列向量组的一个极大线性无关组，其余列向量均可由该极大线性无关组线性表示.

由第（Ⅰ）问的计算可得<equation>A \rightarrow \left(\begin{array}{c c c c c}1&- 1&3&0&- 1\\0&- 1&1&- 1&- 2\\0&0&0&0&0\end{array}\right)\rightarrow \left(\begin{array}{c c c c c}1&0&2&1&1\\0&1&- 1&1&2\\0&0&0&0&0\end{array}\right).</equation>记矩阵<equation>A = (\alpha ,\beta ,\gamma_1,\gamma_2,\gamma_3) = (A_1,A_2)</equation>，其中<equation>A_{1}</equation>为<equation>A</equation>的前两列<equation>(\alpha ,\beta),A_{2}</equation>为<equation>A</equation>的后三列<equation>(\gamma_{1},\gamma_{2},\gamma_{3})</equation>，则<equation>A</equation>为矩阵方程<equation>A_{1}X = A_{2}</equation>的增广矩阵.由（1）式可得<equation>\gamma_ {1} = 2 \alpha - \beta , \quad \gamma_ {2} = \alpha + \beta , \quad \gamma_ {3} = \alpha + 2 \beta .</equation>于是，<equation>A = \left(\alpha , \beta , \gamma_ {1}, \gamma_ {2}, \gamma_ {3}\right) = \left(\alpha , \beta\right) \left( \begin{array}{c c c c c} 1 & 0 & 2 & 1 & 1 \\ 0 & 1 & - 1 & 1 & 2 \end{array} \right).</equation>令<equation>H = \left( \begin{array}{c c c c c} 1 & 0 & 2 & 1 & 1 \\ 0 & 1 & -1 & 1 & 2 \end{array} \right)</equation>，则<equation>A = GH</equation>，其中<equation>G = (\alpha ,\beta)</equation>.

---

**2023年第7题 | 选择题 | 5分 | 答案: D**

7. 已知向量<equation>\alpha_{1}=\left( \begin{array}{c}1\\ 2\\ 3 \end{array} \right),\alpha_{2}=\left( \begin{array}{c}2\\ 1\\ 1 \end{array} \right),\beta_{1}=\left( \begin{array}{c}2\\ 5\\ 9 \end{array} \right),\beta_{2}=\left( \begin{array}{c}1\\ 0\\ 1 \end{array} \right)</equation>若<equation>\gamma</equation>既可由<equation>\alpha_{1},\alpha_{2}</equation>线性表示，也可由<equation>\beta_{1},\beta_{2}</equation>线性表示，则<equation>\gamma=(\quad)</equation>A. k<equation>\left( \begin{array}{c}3\\ 3\\ 4 \end{array} \right),k \in \mathbf{R}</equation>B. k<equation>\left( \begin{array}{c}3\\ 5\\ 10 \end{array} \right),k \in \mathbf{R}</equation>C. k<equation>\left( \begin{array}{c}-1\\ 1\\ 2 \end{array} \right),k \in \mathbf{R}</equation>D. k<equation>\left( \begin{array}{c}1\\ 5\\ 8 \end{array} \right),k \in \mathbf{R}</equation>

答案: D

**解析:**解 由于<equation>\boldsymbol{\gamma}</equation>既可由<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2}</equation>线性表示，也可由<equation>\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2}</equation>线性表示，故存在<equation>k_{1},k_{2},l_{1},l_{2}</equation>，使得<equation>\boldsymbol{\gamma}=k_{1}\boldsymbol{\alpha}_{1}</equation><equation>+ k_{2}\boldsymbol{\alpha}_{2}=l_{1}\boldsymbol{\beta}_{1}+l_{2}\boldsymbol{\beta}_{2}</equation>.于是，<equation>\left(k_{1},-l_{1},k_{2},-l_{2}\right)^{\mathrm{T}}</equation>是齐次线性方程组<equation>\left(\boldsymbol{\alpha}_{1},\boldsymbol{\beta}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\beta}_{2}\right)\boldsymbol{x}=\mathbf{0}</equation>的解.

记<equation>A=(\alpha_{1},\beta_{1},\alpha_{2},\beta_{2})</equation>，对A作初等行变换.<equation>\begin{array}{l} \boldsymbol {A} = \left( \begin{array}{c c c c} 1 & 2 & 2 & 1 \\ 2 & 5 & 1 & 0 \\ 3 & 9 & 1 & 1 \end{array} \right) \xrightarrow {r _ {2} - 2 r _ {1}} \frac {r _ {2} - 2 r _ {1}}{r _ {3} - 3 r _ {1}} \left( \begin{array}{c c c c} 1 & 2 & 2 & 1 \\ 0 & 1 & - 3 & - 2 \\ 0 & 3 & - 5 & - 2 \end{array} \right) \xrightarrow {r _ {1} - 2 r _ {2} ^ {*}} \left( \begin{array}{c c c c} 1 & 0 & 8 & 5 \\ 0 & 1 & - 3 & - 2 \\ 0 & 0 & 4 & 4 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {* *} \times \frac {1}{4}} \left( \begin{array}{c c c c} 1 & 0 & 8 & 5 \\ 0 & 1 & - 3 & - 2 \\ 0 & 0 & 1 & 1 \end{array} \right) \xrightarrow {r _ {1} ^ {*} - 8 r _ {3} ^ {* * *}} \left( \begin{array}{c c c c} 1 & 0 & 0 & - 3 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 \end{array} \right). \\ \end{array}</equation>（<equation>r_{t}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

取<equation>x_{4}=1</equation>，可得<equation>\boldsymbol{\xi}=(3,-1,-1,1)^{\mathrm{T}}</equation>为该方程组的一个基础解系，从而<equation>(k_{1},-l_{1},k_{2},-l_{2})^{\mathrm{T}}= k(3,-1,-1,1)^{\mathrm{T}}</equation>，其中 k<equation>\in\mathbf{R}.</equation>因此，<equation>\boldsymbol {\gamma} = k _ {1} \boldsymbol {\alpha} _ {1} + k _ {2} \boldsymbol {\alpha} _ {2} = 3 k \binom {1} {2} - k \binom {2} {1} = k \binom {1} {5}, \quad k \in \mathbf {R}.</equation>应选 D.

---

**2022年第7题 | 选择题 | 5分 | 答案: C**

7. 设<equation>\alpha_{1}=(\lambda,1,1)^{\mathrm{T}},\alpha_{2}=(1,\lambda,1)^{\mathrm{T}},\alpha_{3}=(1,1,\lambda)^{\mathrm{T}},\alpha_{4}=(1,\lambda,\lambda^{2})^{\mathrm{T}}</equation>. 若<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>等价，则<equation>\lambda</equation>的取值范围是（    )

A.<equation>\{0,1\}</equation>B.<equation>\{\lambda \mid \lambda \in \mathbf{R},\lambda \neq -2\}</equation>C.<equation>\{\lambda \mid \lambda \in \mathbf{R},\lambda \neq -1,\lambda \neq -2\}</equation>D.<equation>\{\lambda \mid \lambda \in \mathbf{R},\lambda \neq -1\}</equation>

答案: C

**解析:**解（法一）当<equation>\lambda=1</equation>时，<equation>\alpha_{1}=\alpha_{2}=\alpha_{3}=\alpha_{4}=\left( \begin{array}{c}1\\ 1\\ 1 \end{array} \right)</equation>.此时<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>显然等价当<equation>\lambda\neq1</equation>时，考虑矩阵<equation>A=(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4})</equation><equation>\begin{array}{l} A = \left( \begin{array}{c c c c} \lambda & 1 & 1 & 1 \\ 1 & \lambda & 1 & \lambda \\ 1 & 1 & \lambda & \lambda^ {2} \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 1 & 1 & \lambda & \lambda^ {2} \\ \lambda & 1 & 1 & 1 \end{array} \right) \xrightarrow {r _ {2} - r _ {1}} \frac {r _ {2} - r _ {1}}{r _ {3} - \lambda r _ {1}} \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 0 & 1 - \lambda & \lambda - 1 & \lambda^ {2} - \lambda \\ 0 & 1 - \lambda^ {2} & 1 - \lambda & 1 - \lambda^ {2} \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} \times \frac {1}{1 - \lambda}} \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 0 & 1 & - 1 & - \lambda \\ 0 & 1 + \lambda & 1 & 1 + \lambda \end{array} \right) \xrightarrow {r _ {3} ^ {* *} - (1 + \lambda) r _ {2} ^ {* *}} \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 0 & 1 & - 1 & - \lambda \\ 0 & 0 & \lambda + 2 & (\lambda + 1) ^ {2} \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

由于 A有2阶非零子式<equation>\left| \begin{array}{cc} \lambda & 1 \\ 1 & \lambda \end{array} \right|</equation>，故<equation>r(A)\geqslant 2</equation>另一方面，因为不存在<equation>\lambda</equation>满足<equation>\lambda +2=(\lambda+1)^{2}=</equation>0，所以<equation>r(A)=3.</equation><equation>r(\alpha_{1},\alpha_{2},\alpha_{3})=3</equation>当且仅当<equation>\lambda\neq-2.</equation><equation>r(\alpha_{1},\alpha_{2},\alpha_{4})=3</equation>当且仅当<equation>\lambda\neq-1.</equation>因此，当<equation>\lambda\neq1</equation>时，<equation>r(A)=r(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4})=r(\alpha_{1},\alpha_{2},\alpha_{3})=r(\alpha_{1},\alpha_{2},\alpha_{4})</equation>当且仅当<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1.</equation>注意到<equation>\lambda=1</equation>也包含在条件<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1</equation>中，故<equation>r(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4})=r(\alpha_{1},\alpha_{2},\alpha_{3})= r(\alpha_{1},\alpha_{2},\alpha_{4})</equation>当且仅当<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1.</equation>综上所述，应选C.

（法二）分别计算<equation>|\alpha_{1},\alpha_{2},\alpha_{3}|</equation>，<equation>|\alpha_{1},\alpha_{2},\alpha_{4}|</equation><equation>\left| \alpha_ {1}, \alpha_ {2}, \alpha_ {3} \right| = \left| \begin{array}{c c c} \lambda & 1 & 1 \\ 1 & \lambda & 1 \\ 1 & 1 & \lambda \end{array} \right| = \left| \begin{array}{c c c} \lambda & 1 - \lambda & 1 - \lambda^ {2} \\ 1 & \lambda - 1 & 1 - \lambda \\ 1 & 0 & 0 \end{array} \right| = (1 - \lambda) ^ {2} (\lambda + 2).</equation><equation>\left| \alpha_ {1}, \alpha_ {2}, \alpha_ {4} \right| = \left| \begin{array}{c c c} \lambda & 1 & 1 \\ 1 & \lambda & \lambda \\ 1 & 1 & \lambda^ {2} \end{array} \right| = \left| \begin{array}{c c c} \lambda & 1 - \lambda & 1 - \lambda^ {3} \\ 1 & \lambda - 1 & \lambda - \lambda^ {2} \\ 1 & 0 & 0 \end{array} \right| = (1 - \lambda) ^ {2} (1 + \lambda) ^ {2}.</equation>当<equation>\lambda\neq1,-2,-1</equation>时，<equation>|\alpha_{1},\alpha_{2},\alpha_{3}|</equation>与<equation>|\alpha_{1},\alpha_{2},\alpha_{4}|</equation>均不为0.此时，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>和<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>均为3维列向量组的极大无关组，从而等价.

当<equation>\lambda=1</equation>时，<equation>\alpha_{1}=\alpha_{2}=\alpha_{3}=\alpha_{4}=\left( \begin{array}{c}1\\ 1\\ 1 \end{array} \right).</equation>此时<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>显然等价.

当<equation>\lambda=-2</equation>或<equation>\lambda=-1</equation>时，<equation>|\alpha_{1},\alpha_{2},\alpha_{3}| \neq |\alpha_{1},\alpha_{2},\alpha_{4}|</equation>，且其中一个为0，另一个不为0，说明两向量组的秩不相等，从而不等价.

综上所述，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>等价当且仅当<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1.</equation>应选C.

---

**2019年第20题 | 解答题 | 11分**

20. (本题满分11分)<equation>\text {已 知 向 量 组 I}: \alpha_ {1} = \left( \begin{array}{c} 1 \\ 1 \\ 4 \end{array} \right), \alpha_ {2} = \left( \begin{array}{c} 1 \\ 0 \\ 4 \end{array} \right), \alpha_ {3} = \left( \begin{array}{c} 1 \\ 2 \\ a ^ {2} + 3 \end{array} \right) \text {与 II}: \beta_ {1} = \left( \begin{array}{c} 1 \\ 1 \\ a + 3 \end{array} \right), \beta_ {2} = \left( \begin{array}{c} 0 \\ 2 \\ 1 - a \end{array} \right), \beta_ {3} = \left( \begin{array}{c} 1 \\ 3 \\ a ^ {2} + 3 \end{array} \right).</equation>若向

量组 I 与 II 等价，求<equation>a</equation>的取值，并将<equation>\beta_{3}</equation>用<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性表示.

**答案:**当 a≠-1时，向量组Ⅰ与向量组Ⅱ等价.当 a=1时，<equation>\beta_{3}=(3-2k)\alpha_{1}+(-2+k)\alpha_{2}+ k\alpha_{3}</equation>，其中k为任意常数；当 a≠±1时，<equation>\beta_{3}=\alpha_{1}-\alpha_{2}+\alpha_{3}.</equation>

**解析:**解记<equation>A=(\alpha_{1},\alpha_{2},\alpha_{3}),B=(\beta_{1},\beta_{2},\beta_{3})</equation>，则由向量组Ⅰ与向量组Ⅱ等价可知<equation>r(A)=r(B)</equation><equation>= r(A,B).</equation>对（A,B）作初等行变换.<equation>\begin{array}{l} (A, B) = \left( \begin{array}{c c c c c c} 1 & 1 & 1 & 1 & 0 & 1 \\ 1 & 0 & 2 & 1 & 2 & 3 \\ 4 & 4 & a ^ {2} + 3 & a + 3 & 1 - a & a ^ {2} + 3 \end{array} \right) \\ \xrightarrow {r _ {2} - r _ {1}} \frac {1}{r _ {3} - 4 r _ {1}} \left( \begin{array}{c c c c c c} 1 & 1 & 1 & 1 & 0 & 1 \\ 0 & - 1 & 1 & 0 & 2 & 2 \\ 0 & 0 & a ^ {2} - 1 & a - 1 & 1 - a & a ^ {2} - 1 \end{array} \right). \\ \end{array}</equation>由上式可知<equation>r(A)\geqslant 2</equation>，故<equation>r(A) = 2</equation>或<equation>r(A) = 3.</equation>当<equation>a^{2}-1=0</equation>时，<equation>a=1</equation>或<equation>a=-1</equation><equation>r(A)=2</equation>.又由于当<equation>a=-1</equation>时，<equation>r(A,B)=3</equation>，故<equation>a=-1</equation>不符合题意，而当<equation>a=1</equation>时，<equation>r(A)=r(B)=r(A,B)=2</equation>，此时向量组 I与向量组Ⅱ等价.

当 a = 1时，<equation>\left(A, \boldsymbol {\beta} _ {3}\right)\rightarrow \left(\begin{array}{c c c c}1&1&1&1\\0&- 1&1&2\\0&0&0&0\end{array}\right) \xrightarrow {r _ {2} \times (- 1)} \left(\begin{array}{c c c c}1&1&1&1\\0&1&- 1&- 2\\0&0&0&0\end{array}\right) \xrightarrow {r _ {1} - r _ {2} ^ {*}} \left(\begin{array}{c c c c}1&0&2&3\\0&1&- 1&- 2\\0&0&0&0\end{array}\right).</equation>取<equation>x_{3}</equation>为自由变元，令<equation>x_{3}=1</equation>，可得<equation>(-2,1,1)^{\mathrm{T}}</equation>为<equation>A x=0</equation>的一个基础解系.又因为<equation>(3,-2,0)^{\mathrm{T}}</equation>为<equation>A x=\beta_{3}</equation>的一个特解，所以<equation>A x=\beta_{3}</equation>的通解为<equation>k(-2,1,1)^{\mathrm{T}}+(3,-2,0)^{\mathrm{T}}</equation>其中k为任意常数因此，<equation>\boldsymbol {\beta} _ {3} = (3 - 2 k) \boldsymbol {\alpha} _ {1} + (- 2 + k) \boldsymbol {\alpha} _ {2} + k \boldsymbol {\alpha} _ {3},</equation>其中 k为任意常数.

当 a<equation>\neq\pm1</equation>时，<equation>a^{2}-1\neq0,r(A)=r(B)=r(A,B)=3</equation>，向量组Ⅰ与向量组Ⅱ等价，且它们相互之间的线性表示唯一.<equation>\left(A, \boldsymbol {\beta} _ {3}\right)\rightarrow \left(\begin{array}{c c c c}1&1&1&1\\0&- 1&1&2\\0&0&1&1\end{array}\right) \xrightarrow [ r _ {1} - r _ {2} ^ {*} ]{r _ {2} \times (- 1)} \left(\begin{array}{c c c c}1&0&2&3\\0&1&- 1&- 2\\0&0&1&1\end{array}\right) \xrightarrow [ r _ {2} ^ {*} + r _ {3} ]{r _ {1} ^ {*} - 2 r _ {3}} \left(\begin{array}{c c c c}1&0&0&1\\0&1&0&- 1\\0&0&1&1\end{array}\right).</equation>因此，<equation>A x=\beta_{3}</equation>的唯一解为<equation>(1,-1,1)^{\mathrm{T}}.</equation><equation>\boldsymbol {\beta} _ {3} = \boldsymbol {\alpha} _ {1} - \boldsymbol {\alpha} _ {2} + \boldsymbol {\alpha} _ {3}.</equation>综上所述，当<equation>a\neq -1</equation>时，向量组 I与向量组Ⅱ等价。当<equation>a = 1</equation>时，<equation>\beta_{3} = (3 - 2k)\alpha_{1} + (-2 + k)\alpha_{2}</equation><equation>+ k\alpha_{3}</equation>，其中<equation>k</equation>为任意常数；当<equation>a\neq \pm 1</equation>时，<equation>\beta_{3} = \alpha_{1} - \alpha_{2} + \alpha_{3}</equation>.

---

**2013年第5题 | 选择题 | 4分 | 答案: B**

5. 设 A,B,C均为 n阶矩阵. 若 AB=C，且 B可逆，则（    ）

A. 矩阵 C的行向量组与矩阵 A的行向量组等价

B. 矩阵 C的列向量组与矩阵 A的列向量组等价

C. 矩阵 C的行向量组与矩阵 B的行向量组等价

D. 矩阵 C的列向量组与矩阵 B的列向量组等价

答案: B

**解析:**我们证明 C的列向量组与 A的列向量组能相互线性表示.

不妨设<equation>A = \left(\alpha_{1},\alpha_{2},\dots ,\alpha_{n}\right),C = \left(\gamma_{1},\gamma_{2},\dots ,\gamma_{n}\right),B = \left(b_{ij}\right)_{n\times n}</equation>，则<equation>\boldsymbol {A B} = \left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\alpha} _ {2}, \dots , \boldsymbol {\alpha} _ {n}\right) \left(b _ {i j}\right) _ {n \times n} = \boldsymbol {C} = \left(\boldsymbol {\gamma} _ {1}, \boldsymbol {\gamma} _ {2}, \dots , \boldsymbol {\gamma} _ {n}\right),</equation><equation>\left\{ \begin{array}{l} \boldsymbol {\gamma} _ {1} = b _ {1 1} \boldsymbol {\alpha} _ {1} + b _ {2 1} \boldsymbol {\alpha} _ {2} + \dots + b _ {n 1} \boldsymbol {\alpha} _ {n}, \\ \boldsymbol {\gamma} _ {2} = b _ {1 2} \boldsymbol {\alpha} _ {1} + b _ {2 2} \boldsymbol {\alpha} _ {2} + \dots + b _ {n 2} \boldsymbol {\alpha} _ {n}, \\ \dots , \\ \boldsymbol {\gamma} _ {n} = b _ {1 n} \boldsymbol {\alpha} _ {1} + b _ {2 n} \boldsymbol {\alpha} _ {2} + \dots + b _ {n n} \boldsymbol {\alpha} _ {n}. \end{array} \right.</equation>因此，C的列向量组<equation>\left( \gamma_{1},\gamma_{2},\dots,\gamma_{n}\right)</equation>能由A的列向量组<equation>\left( \alpha_{1},\alpha_{2},\dots,\alpha_{n}\right)</equation>线性表示。同理，由于B可逆，故A的列向量组也能由C的列向量组线性表示.应选B.

下面我们说明选项 A、C、D不正确.

选项A：令<equation>A=\left( \begin{array}{cc}1&1\\ 0&0 \end{array} \right), B=\left( \begin{array}{cc}1&1\\ 0&1 \end{array} \right)</equation>，则<equation>C=AB=\left( \begin{array}{cc}1&2\\ 0&0 \end{array} \right).</equation>但A的行向量组<equation>\{(1,1),(0,0)\}</equation>与C的行向量组<equation>\{(1,2),(0,0)\}</equation>不等价.

选项C、D：取B为单位矩阵E，C为一个非满秩矩阵.于是 A=C. B的行（列）向量组线性无关， C的行（列）向量组线性相关，因此不等价.

---

**2011年第20题 | 解答题 | 11分**


设向量组<equation>\alpha_{1}=(1,0,1)^{\mathrm{T}},\alpha_{2}=(0,1,1)^{\mathrm{T}},\alpha_{3}=(1,3,5)^{\mathrm{T}}</equation>不能由向量组<equation>\beta_{1}=(1,1,1)^{\mathrm{T}},\beta_{2}=(1,2,3)^{\mathrm{T}},\beta_{3}=(3,4,a)^{\mathrm{T}}</equation>线性表示.

I. 求 a的值；

II. 将<equation>\beta_{1},\beta_{2},\beta_{3}</equation>用<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性表示.

**答案:**(20) （I）<equation>a=5;</equation>（Ⅱ）<equation>\boldsymbol{\beta}_{1}=2\boldsymbol{\alpha}_{1}+4\boldsymbol{\alpha}_{2}-\boldsymbol{\alpha}_{3},\boldsymbol{\beta}_{2}=\boldsymbol{\alpha}_{1}+2\boldsymbol{\alpha}_{2},\boldsymbol{\beta}_{3}=5\boldsymbol{\alpha}_{1}+10\boldsymbol{\alpha}_{2}-2\boldsymbol{\alpha}_{3}.</equation>

**解析:**解（I）记<equation>A=(\alpha_{1},\alpha_{2},\alpha_{3})</equation><equation>B=(\beta_{1},\beta_{2},\beta_{3})</equation><equation>A,B</equation>的列向量组分别记为<equation>A,B.</equation>首先，<equation>|A| = \left| \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 1 & 1 & 5 \end{array} \right| = 1</equation>，故<equation>r(A) = 3</equation>，A满秩.

由于向量组 B不能线性表示 A，故<equation>r(\mathbf{B})<3</equation>；否则 B也满秩，从而 B能线性表示 A，矛盾.

由于<equation>r(\boldsymbol{B}) < 3</equation>，故<equation>| \boldsymbol {B} | = \left| \begin{array}{c c c} 1 & 1 & 3 \\ 1 & 2 & 4 \\ 1 & 3 & a \end{array} \right| \frac {c _ {2} - c _ {1}}{c _ {3} - 3 c _ {1}} \left| \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 1 \\ 1 & 2 & a - 3 \end{array} \right| = a - 5 = 0.</equation>因此，<equation>a = 5</equation>（Ⅱ）（法一）求B用A的线性表示的系数，相当于求<equation>A X=B</equation>的解. X的列向量的坐标为线性表示的系数，即<equation>\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)\left(x_{1i},x_{2i},x_{3i}\right)^{\mathrm{T}}=\boldsymbol{\beta}_{i}(i=1,2,3).</equation><equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {B}) = \left( \begin{array}{c c c c c c} 1 & 0 & 1 & 1 & 1 & 3 \\ 0 & 1 & 3 & 1 & 2 & 4 \\ 1 & 1 & 5 & 1 & 3 & 5 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c c c c} 1 & 0 & 1 & 1 & 1 & 3 \\ 0 & 1 & 3 & 1 & 2 & 4 \\ 0 & 1 & 4 & 0 & 2 & 2 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {*} - r _ {2}} \left( \begin{array}{c c c c c c} 1 & 0 & 1 & 1 & 1 & 3 \\ 0 & 1 & 3 & 1 & 2 & 4 \\ 0 & 0 & 1 & - 1 & 0 & - 2 \end{array} \right) \xrightarrow {r _ {1} - r _ {3} ^ {* *}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 2 & 1 & 5 \\ 0 & 1 & 0 & 4 & 2 & 1 0 \\ 0 & 0 & 1 & - 1 & 0 & - 2 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每做一次初等行变换，加一个*.）

因此，<equation>Ax = \beta_{1}</equation>的解为<equation>(2,4,-1)^{\mathrm{T}},\beta_{1} = 2\alpha_{1} + 4\alpha_{2} - \alpha_{3};Ax = \beta_{2}</equation>的解为<equation>(1,2,0)^{\mathrm{T}},\beta_{2} = \alpha_{1} + 2\alpha_{2};Ax = \beta_{3}</equation>的解为<equation>(5,10,-2)^{\mathrm{T}},\beta_{3} = 5\alpha_{1} + 10\alpha_{2} - 2\alpha_{3}.</equation>（法二）用克拉默法则分别求<equation>A x=\beta_{1},</equation><equation>A x=\beta_{2},</equation><equation>A x=\beta_{3}</equation>的解. x的分量为线性表示的系数，即<equation>\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)\left(x_{1},x_{2},x_{3}\right)^{\mathrm{T}}=\beta_{i}(i=1,2,3).</equation>首先，根据第（I）问可得<equation>|A| = 1.</equation>由克拉默法则知，<equation>Ax = \beta_{1}</equation>的解为<equation>x _ {1} = \left| \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 3 \\ 1 & 1 & 5 \end{array} \right| = 2, \quad x _ {2} = \left| \begin{array}{c c c} 1 & 1 & 1 \\ 0 & 1 & 3 \\ 1 & 1 & 5 \end{array} \right| = 4, \quad x _ {3} = \left| \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 1 \end{array} \right| = - 1.</equation>因此，<equation>\pmb{\beta}_{1} = 2\pmb{\alpha}_{1} + 4\pmb{\alpha}_{2} - \pmb{\alpha}_{3}</equation>. 同理可得<equation>\pmb{\beta}_{2} = \pmb{\alpha}_{1} + 2\pmb{\alpha}_{2}, \pmb{\beta}_{3} = 5\pmb{\alpha}_{1} + 10\pmb{\alpha}_{2} - 2\pmb{\alpha}_{3}</equation>.

---

**2010年第5题 | 选择题 | 4分 | 答案: A**

5. 设向量组 I:<equation>\alpha_{1},\alpha_{2},\cdots,\alpha_{r}</equation>可由向量组 II:<equation>\beta_{1},\beta_{2},\cdots,\beta_{s}</equation>线性表示.下列命题正确的是（    ）

A. 若向量组 I 线性无关，则<equation>r\leqslant s</equation>B. 若向量组 I 线性相关，则<equation>r>s</equation>C. 若向量组 II 线性无关，则<equation>r\leqslant s</equation>D. 若向量组 II 线性相关，则<equation>r>s</equation>

答案: A

**解析:**解 由于向量组 I 能被向量组Ⅱ线性表示，故<equation>r_{\mathrm{I}} \leqslant r_{\mathrm{II}}</equation>.又由题设，有<equation>r_{\mathrm{I}} \leqslant r, r_{\mathrm{II}} \leqslant s.</equation>若向量组 I 线性无关，则<equation>r_{\mathrm{I}}=r</equation>，从而有<equation>r = r _ {\mathrm {I}} \leqslant r _ {\mathrm {I I}} \leqslant s,</equation>即<equation>r\leqslant s.</equation>应选A.

下面我们说明选项B、C、D不正确.

考虑 I = {<equation>\left( \begin{array}{c} 1 \\ 0 \end{array} \right), \left( \begin{array}{c} 2 \\ 0 \end{array} \right)</equation>，Ⅱ = {<equation>\left( \begin{array}{c} 1 \\ 0 \end{array} \right), \left( \begin{array}{c} 0 \\ 1 \end{array} \right), \left( \begin{array}{c} 2 \\ 0 \end{array} \right)</equation>}.Ⅱ能表示 I，且向量组 I，Ⅱ均线性相关，但 2 = r < s = 3.选项B、D不正确.

考虑 I =<equation>\left\{\begin{array}{l l}1\\0\end{array}\right.,\left(\begin{array}{l}2\\0\end{array}\right.,\left(\begin{array}{l}3\\0\end{array}\right)</equation>，Ⅱ<equation>= \left\{\begin{array}{l l}1\\0\end{array}\right.,\left(\begin{array}{l}0\\1\end{array}\right)</equation>.Ⅱ能表示Ⅰ，且向量组Ⅱ线性无关，但<equation>3=r></equation>s=2.选项C不正确.

---


#### 向量组的线性相关性


**2014年第6题 | 选择题 | 4分 | 答案: A**

6. 设<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>均为3维向量，则对任意常数 k,l，向量组<equation>\alpha_{1}+k\alpha_{3},\alpha_{2}+l\alpha_{3}</equation>线性无关是向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关的（    ）

A. 必要非充分条件 B. 充分非必要条件

C. 充分必要条件 D. 既非充分也非必要条件

答案: A

**解析:**解<equation>(\alpha_{1} + k\alpha_{3},\alpha_{2} + l\alpha_{3}) = (\alpha_{1},\alpha_{2},\alpha_{3})\left( \begin{array}{c c}1 & 0\\ 0 & 1\\ k & l \end{array} \right).</equation>若向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关，则<equation>r \left(\left(\boldsymbol {\alpha} _ {1} + k \boldsymbol {\alpha} _ {3}, \boldsymbol {\alpha} _ {2} + l \boldsymbol {\alpha} _ {3}\right)\right) = r \left(\left( \begin{array}{c c} 1 & 0 \\ 0 & 1 \\ k & l \end{array} \right)\right) = 2.</equation>因此，<equation>\alpha_{1} + k\alpha_{3},\alpha_{2} + l\alpha_{3}</equation>线性无关.

令<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2}</equation>为线性无关的两个向量，<equation>\boldsymbol{\alpha}_{3}=\mathbf{0}</equation>，则对任意常数 k，l，向量组<equation>\boldsymbol{\alpha}_{1}+k\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{2}+l\boldsymbol{\alpha}_{3}</equation>线性无关，但向量组<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性相关.

综上所述，对任意常数 k，l，向量组<equation>\boldsymbol{\alpha}_{1}+k\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{2}+l\boldsymbol{\alpha}_{3}</equation>线性无关是向量组<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性无关的必要非充分条件.应选A.

---

**2012年第5题 | 选择题 | 4分 | 答案: C**

5. 设<equation>\alpha_{1}=\left( \begin{array}{c}0\\ 0\\ c_{1}\end{array} \right),\alpha_{2}=\left( \begin{array}{c}0\\ 1\\ c_{2}\end{array} \right),\alpha_{3}=\left( \begin{array}{c}1\\ -1\\ c_{3}\end{array} \right),\alpha_{4}=\left( \begin{array}{c}-1\\ 1\\ c_{4}\end{array} \right),</equation>其中<equation>c_{1},c_{2},c_{3},c_{4}</equation>为任意常数，则下列向量组线性相关

为（    ）

A.<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>B.<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>C.<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>D.<equation>\alpha_{2},\alpha_{3},\alpha_{4}</equation>

答案: C

**解析:**解（法一）由题设可得，<equation>\boldsymbol{\alpha}_{3}+\boldsymbol{\alpha}_{4}=\left( \begin{array}{c}0\\ 0\\ c_{3}+c_{4} \end{array} \right)</equation><equation>\boldsymbol{\alpha}_{1}=\left( \begin{array}{c}0\\ 0\\ c_{1} \end{array} \right).</equation>当<equation>c_{3} + c_{4}\neq 0</equation>时，<equation>\alpha_{1} = \frac{c_{1}}{c_{3} + c_{4}} \left(\alpha_{3} + \alpha_{4}\right)</equation>，<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>线性相关；当<equation>c_{3} + c_{4} = 0</equation>时，<equation>\alpha_{3} + \alpha_{4} = 0</equation>，<equation>\alpha_{3},\alpha_{4}</equation>线性相关.从而<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>线性相关.

综上所述，<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}</equation>线性相关，应选C.

（法二）由于<equation>n</equation>个<equation>n</equation>维列向量<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{n}</equation>线性相关等价于<equation>|\alpha_{1},\alpha_{2},\dots ,\alpha_{n}| = 0</equation>，而<equation>\left| \alpha_ {1}, \alpha_ {3}, \alpha_ {4} \right| = \left| \begin{array}{c c c} 0 & 1 & - 1 \\ 0 & - 1 & 1 \\ c _ {1} & c _ {3} & c _ {4} \end{array} \right| = c _ {1} \left| \begin{array}{c c} 1 & - 1 \\ - 1 & 1 \end{array} \right| = 0,</equation>故<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}</equation>线性相关.应选C.

同理可计算其他选项中的3个向量组成的矩阵的行列式，可知它们均不恒为零.

---

**2009年第20题 | 解答题 | 11分**

20. (本题满分11分)<equation>\text {设} \boldsymbol {A} = \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ - 1 & 1 & 1 \\ 0 & - 4 & - 2 \end{array} \right), \boldsymbol {\xi} _ {1} = \left( \begin{array}{c} - 1 \\ 1 \\ - 2 \end{array} \right).</equation>I. 求满足<equation>A\xi_{2}=\xi_{1}, A^{2}\xi_{3}=\xi_{1}</equation>的所有向量<equation>\xi_{2},\xi_{3}</equation>；

II. 对第一问中的任意向量<equation>\xi_{2},\xi_{3}</equation>，证明<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

**答案:**（20）（I）满足<equation>A\xi_{2}=\xi_{1}</equation>的所有向量为<equation>\xi_{2}=k_{1}(1,-1,2)^{\mathrm{T}}+(0,0,1)^{\mathrm{T}}</equation>，其中<equation>k_{1}</equation>为任意常数；满足<equation>A^{2}\xi_{3}=\xi_{1}</equation>的所有向量<equation>\xi_{3}=k_{2}(1,-1,0)^{\mathrm{T}}+k_{3}(0,0,1)^{\mathrm{T}}+\left(-\frac{1}{2},0,0\right)^{\mathrm{T}}</equation>，其中<equation>k_{2},k_{3}</equation>为任意常数.

（Ⅱ）证明略.

**解析:**解（I）解<equation>A x=\xi_{1}</equation>，这是一个非齐次线性方程组.<equation>\left(\boldsymbol {A}, \boldsymbol {\xi} _ {1}\right) = \left( \begin{array}{c c c c} 1 & - 1 & - 1 & - 1 \\ - 1 & 1 & 1 & 1 \\ 0 & - 4 & - 2 & - 2 \end{array} \right) \xrightarrow [ r _ {2} ^ {*} \leftrightarrow r _ {3} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c} 1 & - 1 & - 1 & - 1 \\ 0 & - 4 & - 2 & - 2 \\ 0 & 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {1} + r _ {2} ^ {* * *} ]{r _ {2} ^ {* *} \times \left(- \frac {1}{2}\right)} \left( \begin{array}{c c c c} 1 & 1 & 0 & 0 \\ 0 & 2 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{array} \right).</equation>(<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每做一次初等行变换，加一个*.）

于是<equation>r(A) = r(A, \xi_1) = 2.Ax = \xi_1</equation>有无穷多解.其对应的齐次方程组等价于<equation>\left\{ \begin{array}{l}x_{1} + x_{2} = 0,\\ 2x_{2} + x_{3} = 0, \end{array} \right.</equation>故可取<equation>(1, - 1, 2)^{\mathrm{T}}</equation>为该方程组的一个基础解系.另外，<equation>\left\{ \begin{array}{l}x_{1} + x_{2} = 0,\\ 2x_{2} + x_{3} = 1 \end{array} \right.</equation>的一个特解为<equation>(0,0,1)^{\mathrm{T}}.</equation>因此，<equation>Ax = \xi_{1}</equation>的通解为<equation>\xi_{2} = k_{1}(1, -1, 2)^{\mathrm{T}} + (0, 0, 1)^{\mathrm{T}}</equation>，其中<equation>k_{1}</equation>为任意常数.<equation>\left(\boldsymbol {A} ^ {2}, \boldsymbol {\xi} _ {1}\right) = \left( \begin{array}{c c c c} 2 & 2 & 0 & - 1 \\ - 2 & - 2 & 0 & 1 \\ 4 & 4 & 0 & - 2 \end{array} \right) \xrightarrow [ r _ {3} - 2 r _ {1} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c} 2 & 2 & 0 & - 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{array} \right).</equation>于是<equation>r(A^{2}) = r(A^{2},\xi_{1}) = 1.A^{2}x = \xi_{1}</equation>有无穷多解.其对应的齐次方程组等价于<equation>2(x_{1} + x_{2}) = 0</equation>，故可取<equation>(1, - 1,0)^{\mathrm{T}}</equation>和<equation>(0,0,1)^{\mathrm{T}}</equation>为该方程组的一个基础解系.另外，<equation>2(x_{1} + x_{2}) = -1</equation>的一个特解为<equation>\left(-\frac{1}{2},0;0\right)^{\mathrm{T}}.</equation>因此，<equation>A^{2}x = \xi_{1}</equation>的通解为<equation>\xi_{3} = k_{2}(1, - 1,0)^{\mathrm{T}} + k_{3}(0,0,1)^{\mathrm{T}} + \left(-\frac{1}{2},0,0\right)^{\mathrm{T}}</equation>，其中<equation>k_{2},k_{3}</equation>为任意常数.

（Ⅱ）（法一）通过计算可知，<equation>\boldsymbol {A} \boldsymbol {\xi} _ {1} = \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ - 1 & 1 & 1 \\ 0 & - 4 & - 2 \end{array} \right) \left( \begin{array}{c} - 1 \\ 1 \\ - 2 \end{array} \right) = \left( \begin{array}{c} 0 \\ 0 \\ 0 \end{array} \right).</equation>从而<equation>A^{3}\xi_{3} = A^{2}\xi_{2} = A\xi_{1} = 0.</equation>我们可以利用该性质推出<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

不妨设<equation>a\boldsymbol{\xi}_1 + b\boldsymbol{\xi}_2 + c\boldsymbol{\xi}_3 = \mathbf{0}</equation>. 该等式两端同时左乘<equation>A^2</equation><equation>a A ^ {2} \xi_ {1} + b A ^ {2} \xi_ {2} + c A ^ {2} \xi_ {3} = c A ^ {2} \xi_ {3} = c \xi_ {1} = 0.</equation>由于<equation>\boldsymbol{\xi}_{1}</equation>为非零向量，故<equation>c=0.</equation>于是<equation>a\boldsymbol{\xi}_{1}+b\boldsymbol{\xi}_{2}=\mathbf{0}.</equation>再在<equation>a\boldsymbol{\xi}_{1}+b\boldsymbol{\xi}_{2}=\mathbf{0}</equation>两端同时左乘 A，得<equation>aA\boldsymbol{\xi}_{1}+bA\boldsymbol{\xi}_{2}=bA\boldsymbol{\xi}_{2}=b\boldsymbol{\xi}_{1}=\mathbf{0}.</equation>同理得<equation>b = 0</equation>. 由于<equation>b = c = 0</equation>，故<equation>a\boldsymbol{\xi}_1 = \mathbf{0}</equation>. 从而<equation>a = 0</equation>.

因此，<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

（法二）由第（I）问，我们知道了<equation>\xi_{1},\xi_{2},\xi_{3}</equation>的表达式，从而我们可以通过计算行列式<equation>|\xi_{1},\xi_{2},\xi_{3}|</equation>来说明<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.<equation>\begin{array}{l} \left| \xi_ {1}, \xi_ {2}, \xi_ {3} \right| = \left| \begin{array}{c c c} - 1 & k _ {1} & k _ {2} - \frac {1}{2} \\ 1 & - k _ {1} & - k _ {2} \\ - 2 & 2 k _ {1} + 1 & k _ {3} \end{array} \right| \xlongequal {r _ {1} + r _ {2}} \left| \begin{array}{c c c} 0 & 0 & - \frac {1}{2} \\ 1 & - k _ {1} & - k _ {2} \\ - 2 & 2 k _ {1} + 1 & k _ {3} \end{array} \right| \\ \underline {{\underline {{\text {按 第一 行 展开}}}}} \left(- \frac {1}{2}\right) \left| \begin{array}{c c} 1 & - k _ {1} \\ - 2 & 2 k _ {1} + 1 \end{array} \right| = - \frac {1}{2} \neq 0. \\ \end{array}</equation>因此，<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.
