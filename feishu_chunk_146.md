#### 线性微分方程的解的结构

**2010年第2题 | 选择题 | 4分 | 答案: A**

2. 设<equation>y_{1}, y_{2}</equation>是一阶线性非齐次微分方程<equation>y^{\prime}+p(x)y=q(x)</equation>的两个特解，若常数<equation>\lambda,\mu</equation>使<equation>\lambda y_{1}+\mu y_{2}</equation>是该方程的解，<equation>\lambda y_{1}-\mu y_{2}</equation>是该方程对应的齐次方程的解，则（    )

A.<equation>\lambda=\frac{1}{2},\mu=\frac{1}{2}</equation>B.<equation>\lambda=-\frac{1}{2},\mu=-\frac{1}{2}</equation>C.<equation>\lambda=\frac{2}{3},\mu=\frac{1}{3}</equation>D.<equation>\lambda=\frac{2}{3},\mu=\frac{2}{3}</equation>

答案: A

**解析:**由题设知，<equation>y _ {1} ^ {\prime} + p (x) y _ {1} = q (x), \quad y _ {2} ^ {\prime} + p (x) y _ {2} = q (x).</equation>又由题设知，<equation>\lambda y_{1} + \mu y_{2}</equation>也是<equation>y^{\prime} + p(x)y = q(x)</equation>的解，故<equation>\left(\lambda y _ {1} + \mu y _ {2}\right) ^ {\prime} + p (x) \left(\lambda y _ {1} + \mu y _ {2}\right) = q (x).</equation>整理（1）式，得<equation>\lambda \left[ y _ {1} ^ {\prime} + p (x) y _ {1} \right] + \mu \left[ y _ {2} ^ {\prime} + p (x) y _ {2} \right] = q (x),</equation>即<equation>(\lambda +\mu)q(x) = q(x)</equation>. 由于<equation>q(x)\neq 0</equation>，故<equation>\lambda +\mu = 1.</equation>又由<equation>\lambda y_{1} - \mu y_{2}</equation>是<equation>y^{\prime} + p(x)y = 0</equation>的解知<equation>\left(\lambda y _ {1} - \mu y _ {2}\right) ^ {\prime} + p (x) \left(\lambda y _ {1} - \mu y _ {2}\right) = 0.</equation>整理（2）式，得<equation>\lambda \left[ y _ {1} ^ {\prime} + p (x) y _ {1} \right] - \mu \left[ y _ {2} ^ {\prime} + p (x) y _ {2} \right] = 0,</equation>即<equation>(\lambda -\mu)q(x) = 0.</equation>由于<equation>q(x)\neq 0</equation>，故<equation>\lambda -\mu = 0.</equation>联立<equation>\left\{ \begin{array}{l l} \lambda +\mu =1, \\ \lambda -\mu =0, \end{array} \right.</equation>解得<equation>\lambda =\frac{1}{2},\mu =\frac{1}{2}</equation>.应选A.

---


## 线性代数


### 线性方程组

**2025年第5题 | 选择题 | 5分 | 答案: A**

5. 设 A是 m×n矩阵，<equation>\beta</equation>是 m维非零列向量，若 A有 k阶非零子式，则（    ）

A. 当 k=m时，<equation>A x=\beta</equation>有解 B. 当 k=m时，<equation>A x=\beta</equation>无解

C. 当 k<m时，<equation>A x=\beta</equation>有解 D. 当 k<m时，<equation>A x=\beta</equation>无解

答案: A

**解析:**解由 A有k阶非零子式可知<equation>r ( A ) \geqslant k</equation>当<equation>k=m</equation>时，<equation>r ( A ) \geqslant m</equation>另一方面，由 A是<equation>m \times n</equation>矩阵可知<equation>r ( A ) \leqslant \min \{ m, n \} \leqslant m</equation>于是，<equation>r ( A )=m</equation>从而<equation>r ( A , \beta) \geqslant m</equation>又因为（A，<equation>\beta</equation>）是<equation>m \times(n+1)</equation>矩阵，<equation>r ( A , \beta) \leqslant m</equation>所以<equation>r ( A , \beta) = m</equation>由此可得，<equation>r ( A )=r ( A , \beta)=m</equation>方程组<equation>A x=\beta</equation>有解.选项 A正确，选项B不正确.

因此，应选A.

下面说明选项C、D不正确.

取<equation>m = 2,n = 1,k = 1.</equation>对选项C，取<equation>A=\binom{1}{0},\beta=\binom{0}{1}</equation>，则方程组<equation>Ax=\beta</equation>无解.

对选项D，取<equation>A=\binom{1}{0},\beta=\binom{1}{0}</equation>，则方程组<equation>Ax=\beta</equation>有解.

---

**2024年第21题 | 解答题 | 12分**

21. （本题满分12分）

设矩阵<equation>A = \left( \begin{array}{c c c c} 1 & -1 & 0 & -1 \\ 1 & 1 & 0 & 3 \\ 2 & 1 & 2 & 6 \end{array} \right), B = \left( \begin{array}{c c c c} 1 & 0 & 1 & 2 \\ 1 & -1 & a & a - 1 \\ 2 & -3 & 2 & -2 \end{array} \right)</equation>，向量<equation>\alpha = \left( \begin{array}{c} 0 \\ 2 \\ 3 \end{array} \right), \beta = \left( \begin{array}{c} 1 \\ 0 \\ -1 \end{array} \right).</equation>I. 证明：方程组<equation>A x=\alpha</equation>的解均为方程组<equation>B x=\beta</equation>的解；

II. 若方程组<equation>Ax = \alpha</equation>与方程组<equation>Bx = \beta</equation>不同解，求<equation>a</equation>的值.

**答案:**(1) 证明略

(2) a=1.

**解析:**解（I）（法一）分别对（A，<equation>\alpha</equation>）和（B，<equation>\beta</equation>）作初等行变换<equation>\begin{array}{l} (A, \alpha) = \left( \begin{array}{c c c c c} 1 & - 1 & 0 & - 1 & 0 \\ 1 & 1 & 0 & 3 & 2 \\ 2 & 1 & 2 & 6 & 3 \end{array} \right) \xrightarrow {r _ {1} + r _ {2}} \left( \begin{array}{c c c c c} 2 & 0 & 0 & 2 & 2 \\ 1 & 1 & 0 & 3 & 2 \\ 2 & 1 & 2 & 6 & 3 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c} 1 & 0 & 0 & 1 & 1 \\ 1 & 1 & 0 & 3 & 2 \\ 2 & 1 & 2 & 6 & 3 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c} 1 & 0 & 0 & 1 & 1 \\ 0 & 1 & 0 & 2 & 1 \\ 0 & 1 & 2 & 4 & 1 \end{array}\right)\rightarrow \left( \begin{array}{c c c c c} 1 & 0 & 0 & 1 & 1 \\ 0 & 1 & 0 & 2 & 1 \\ 0 & 0 & 2 & 2 & 0 \end{array}\right)\rightarrow \left( \begin{array}{c c c c c} 1 & 0 & 0 & 1 & 1 \\ 0 & 1 & 0 & 2 & 1 \\ 0 & 0 & 1 & 1 & 0 \end{array}\right). \\ \end{array}</equation><equation>\begin{array}{l} (\boldsymbol {B}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 1 & 0 & 1 & 2 & 1 \\ 1 & - 1 & a & a - 1 & 0 \\ 2 & - 3 & 2 & - 2 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c} 1 & 0 & 1 & 2 & 1 \\ 0 & - 1 & a - 1 & a - 3 & - 1 \\ 0 & - 3 & 0 & - 6 & - 3 \end{array} \right) \\ \rightarrow \left(\begin{array}{c c c c c}1&0&1&2&1\\0&1&0&2&1\\0&- 1&a - 1&a - 3&- 1\end{array}\right)\rightarrow \left(\begin{array}{c c c c c}1&0&1&2&1\\0&1&0&2&1\\0&0&a - 1&a - 1&0\end{array}\right). \\ \end{array}</equation>注意到<equation>(1,0,1,2,1) = (1,0,0,1,1) + (0,0,1,1,0)</equation>，故无论<equation>\alpha</equation>取何值，<equation>(A,\alpha)</equation>的行向量组均能线性表示<equation>(B,\beta)</equation>的行向量组，从而方程组<equation>Ax = \alpha</equation>的解均为方程组<equation>Bx = \beta</equation>的解.

（法二）先求<equation>A x=\alpha</equation>的解.

同法一可得<equation>(A, \alpha) \rightarrow \left( \begin{array}{cccc} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 1 & 1 \\ 0 \end{array} \right)</equation>. 令<equation>x_{4} = 1</equation>, 则<equation>Ax = 0</equation>的一个基础解系可取为<equation>\left( \begin{array}{c} - 1 \\ - 2 \\ - 1 \\ 1 \end{array} \right)</equation>.

又令<equation>x_{4} = 0</equation>, 可得<equation>Ax = \alpha</equation>的一个特解为<equation>\left( \begin{array}{c} 1 \\ 1 \\ 0 \\ 0 \end{array} \right)</equation>, 从而<equation>Ax = \alpha</equation>的通解为<equation>k\left( \begin{array}{c} - 1 \\ - 2 \\ - 1 \\ 1 \end{array} \right) + \left( \begin{array}{c} 1 \\ 1 \\ 0 \\ 0 \end{array} \right)</equation>, 即<equation>\left( \begin{array}{c} - k + 1 \\ - 2k + 1 \\ - k \\ k \end{array} \right)</equation>, 其中<equation>k</equation>为任意常数.

计算<equation>B\left( \begin{array}{c} - k + 1 \\ - 2k + 1 \\ - k \\ k \end{array} \right)</equation>可得<equation>\left( \begin{array}{c c c c} 1 & 0 & 1 & 2 \\ 1 & - 1 & a & a - 1 \\ 2 & - 3 & 2 & - 2 \end{array} \right)\left( \begin{array}{c} - k + 1 \\ - 2k + 1 \\ - k \\ k \end{array} \right) = \left( \begin{array}{c} - k + 1 - k + 2k \\ - k + 1 + 2k - 1 - ak + (a - 1)k \\ - 2k + 2 + 6k - 3 - 2k - 2k \end{array} \right) = \left( \begin{array}{c} 1 \\ 0 \\ - 1 \end{array} \right)</equation>.

于是,<equation>\left( \begin{array}{c} - k + 1 \\ - 2k + 1 \\ - k \\ k \end{array} \right)</equation>是<equation>Bx = \beta</equation>的解.

因此，方程组<equation>A x=\alpha</equation>的解均为方程组<equation>B x=\beta</equation>的解.

（法三）由于方程组<equation>Ax = \alpha</equation>的解均为方程组<equation>Bx = \beta</equation>的解等价于方程组<equation>\left\{ \begin{array}{l}Ax = \alpha ,\\ Bx = \beta \end{array} \right.</equation>与方程组<equation>Ax = \alpha</equation>同解（见注），故要证明方程组<equation>Ax = \alpha</equation>的解均为方程组<equation>Bx = \beta</equation>的解，只需证明方程组<equation>\left\{ \begin{array}{l}Ax = \alpha ,\\ Bx = \beta \end{array} \right.</equation>与方程组<equation>Ax = \alpha</equation>同解.

对<equation>\left( \begin{array}{cc}A&\alpha \\ B&\beta \end{array} \right)</equation>作初等行变换.<equation>\left( \begin{array}{c c} A & \alpha \\ B & \beta \end{array} \right) \xrightarrow {\text {同 法 一}} \left( \begin{array}{c c c c c} 1 & 0 & 0 & 1 & 1 \\ 0 & 1 & 0 & 2 & 1 \\ 0 & 0 & 1 & 1 & 0 \\ 1 & 0 & 1 & 2 & 1 \\ 0 & 1 & 0 & 2 & 1 \\ 0 & 0 & a - 1 & a - 1 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c} 1 & 0 & 0 & 1 & 1 \\ 0 & 1 & 0 & 2 & 1 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>\left( \begin{array}{cc}A&\alpha \\ B&\beta \end{array} \right)</equation>的行向量组与（A，<equation>\alpha</equation>）的行向量组等价.由此可得，方程组<equation>\left\{ \begin{array}{l l}Ax = \alpha ,\\ Bx = \beta \end{array} \right.</equation>与方程组<equation>A x = \alpha</equation>同解，从而方程组<equation>A x = \alpha</equation>的解均为方程组<equation>B x = \beta</equation>的解.

（Ⅱ）（法一）由第（I）问的法一可知，当<equation>a\neq 1</equation>时，<equation>(A,\alpha)</equation>的行向量组与<equation>(B,\beta)</equation>的行向量组等价，从而<equation>A x=\alpha</equation>与<equation>B x=\beta</equation>同解.当<equation>a=1</equation>时，<equation>(A,\alpha)</equation>的行向量组能线性表示<equation>(B,\beta)</equation>的行向量组，但<equation>(B,\beta)</equation>的行向量组不能线性表示<equation>(A,\alpha)</equation>的行向量组，从而<equation>A x=\alpha</equation>与<equation>B x=\beta</equation>不同解.

因此，<equation>a = 1</equation>（法二）由第（I）问可知，方程组<equation>A x=\alpha</equation>的解均为方程组<equation>B x=\beta</equation>的解，而方程组<equation>A x=\alpha</equation>与方程组<equation>B x=\beta</equation>不同解，故<equation>A x=\alpha</equation>的解集是<equation>B x=\beta</equation>的解集的真子集.进一步可得<equation>A x=0</equation>的解集是<equation>B x=0</equation>的解集的真子集.

由第（I）问可知，<equation>r ( A )=3</equation>，故结合<equation>A x=0</equation>的解集是Bx=0的解集的真子集可得，<equation>r ( B )<</equation>3. 又因为B有2阶非零子式<equation>\left| \begin{array}{c c} {1} & {0} \\ {1} & {-1} \end{array} \right|</equation>，所以<equation>r ( B )\geqslant 2</equation>.于是，<equation>r ( B )=2.</equation>对矩阵 B作初等行变换<equation>\begin{array}{l} \boldsymbol {B} = \left( \begin{array}{c c c c} 1 & 0 & 1 & 2 \\ 1 & - 1 & a & a - 1 \\ 2 & - 3 & 2 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 0 & 1 & 2 \\ 0 & - 1 & a - 1 & a - 3 \\ 0 & - 3 & 0 & - 6 \end{array} \right) \\ \rightarrow \left(\begin{array}{c c c c}1&0&1&2\\0&- 1&a - 1&a - 3\\0&1&0&2\end{array}\right)\rightarrow \left(\begin{array}{c c c c}1&0&1&2\\0&- 1&a - 1&a - 3\\0&0&a - 1&a - 1\end{array}\right). \\ \end{array}</equation><equation>r(\boldsymbol{B}) = 2</equation>当且仅当<equation>a - 1 = 0</equation>，即<equation>a = 1</equation>因此，<equation>a=1.</equation>

---

**2023年第15题 | 填空题 | 5分**

15. 已知线性方程组<equation>\left| \begin{array}{l l l} a x _ {1} + x _ {3} = 1, \\ x _ {1} + a x _ {2} + x _ {3} = 0, \\ x _ {1} + 2 x _ {2} + a x _ {3} = 0, \\ a x _ {1} + b x _ {2} = 2 \end{array} \right. \mathrm {有 解}, \mathrm {其 中} a, b \mathrm {为 常 数 . 若} \left| \begin{array}{c c c} a & 0 & 1 \\ 1 & a & 1 \\ 1 & 2 & a \end{array} \right| = 4, \mathrm {则} \left| \begin{array}{c c c} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right| = \underline {{\quad}}.</equation>

**解析:**解（法一）记方程组<equation>\left\{ \begin{array}{l l} a x_{1}+x_{3}=1, \\ x_{1}+a x_{2}+x_{3}=0, \\ x_{1}+2 x_{2}+a x_{3}=0, \\ a x_{1}+b x_{2}=2 \end{array} \right.</equation>的系数矩阵为A，增广矩阵为（A,b），则<equation>(\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} a & 0 & 1 & 1 \\ 1 & a & 1 & 0 \\ 1 & 2 & a & 0 \\ a & b & 0 & 2 \end{array} \right).</equation>由方程组有解可知<equation>r ( \mathbf{A})=r ( \mathbf{A},\mathbf{b})</equation>.因为 A为<equation>4\times 3</equation>矩阵，所以<equation>r ( \mathbf{A})\leqslant 3</equation>，从而<equation>r ( \mathbf{A})=r ( \mathbf{A},\mathbf{b})\leqslant 3</equation>进一步可得<equation>| \mathbf{A},\mathbf{b} |=0</equation>.于是，<equation>0 = \left| \begin{array}{c c c c} a & 0 & 1 & 1 \\ 1 & a & 1 & 0 \\ 1 & 2 & a & 0 \\ a & b & 0 & 2 \end{array} \right| \xlongequal {\text {按 第四 列 展开}} - \left| \begin{array}{c c c} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right| + 2 \left| \begin{array}{c c c} a & 0 & 1 \\ 1 & a & 1 \\ 1 & 2 & a \end{array} \right| = - \left| \begin{array}{c c c} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right| + 8.</equation>因此，<equation>\left| \begin{array}{c c c} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right| = 8.</equation>（法二）记方程组<equation>\left\{\begin{array}{l l}a x_{1}+x_{3}=1,\\x_{1}+a x_{2}+x_{3}=0,\\x_{1}+2 x_{2}+a x_{3}=0,\\a x_{1}+b x_{2}=2\end{array}\right.</equation>的系数矩阵为 A，增广矩阵为（A,b）.由方程组有解可知<equation>r(A)=r(A,b).</equation>注意到<equation>\left| \begin{array}{c c c} a & 0 & 1 \\ 1 & a & 1 \\ 1 & 2 & a \end{array} \right|=4</equation>为 A的一个3阶非零子式，故<equation>r(A)\geqslant 3.</equation>又因为 A为<equation>4\times 3</equation>矩阵，所以<equation>r(A)\leqslant 3.</equation>从而<equation>r(A)=3.</equation>由<equation>r ( \mathbf{A} )=r ( \mathbf{A},\mathbf{b} )</equation>可得，<equation>r ( \mathbf{A},\mathbf{b} )=3.</equation>于是<equation>r ( \mathbf{A} )=r ( \mathbf{A},\mathbf{b} )=3</equation>，该方程组有唯一解.

考虑方程组 I：<equation>\left\{\begin{array}{l l}a x_{1}+x_{3}=1,\\x_{1}+a x_{2}+x_{3}=0,\\x_{1}+2 x_{2}+a x_{3}=0\end{array}\right.</equation>和方程组 II：<equation>\left\{\begin{array}{l l}x_{1}+a x_{2}+x_{3}=0,\\x_{1}+2 x_{2}+a x_{3}=0,\\a x_{1}+b x_{2}=2.\end{array}\right.</equation>由原方程组有唯一解

可知方程组 I 和方程组 II 有唯一公共解.

由于方程组 I的系数矩阵行列式等于4，故由克拉默法则知其仅有唯一解，进一步可得其增广矩阵的秩为3，行向量组线性无关。由此可知方程组Ⅱ的增广矩阵<equation>\left( \begin{array}{c c c c} {1} & {a} & {1} & {0} \\ {1} & {2} & {a} & {0} \\ {a} & {b} & {0} & {2} \end{array} \right)</equation>的前两行线性无关。又因为该增广矩阵的第三行为（a,b，0，2），最后一个元素非零，所以第三行与前两行线性无关。于是，方程组Ⅱ的增广矩阵的秩为3.由方程组Ⅱ有解可知，其系数矩阵的秩也为3，从而行列式非零.

记该公共解为<equation>\left(x_{1},x_{2},x_{3}\right)^{\mathrm{T}}</equation><equation>\left| \begin{array}{lll} a & 0 & 1 \\ 1 & a & 1 \\ 1 & 2 & a \end{array} \right|=A_{1}=4</equation><equation>\left| \begin{array}{lll} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right|=A_{2}\neq0.</equation>对方程组 I 使用克拉默法则可得<equation>x_{1}=\frac{\left| \begin{array}{lll}1&0&1\\ 0&a&1\\ 0&2&a \end{array} \right|}{A_{1}}=\frac{\left| \begin{array}{lll}1&0&1\\ 0&a&1\\ 0&2&a \end{array} \right|}{4}</equation>，对方程组Ⅱ使用克拉默法则可得<equation>x_{1}=\frac{\left| \begin{array}{lll}0&a&1\\ 0&2&a\\ 2&b&0 \end{array} \right|}{A_{2}}.</equation>由此可得<equation>x _ {1} = \frac {\left| \begin{array}{c c} a & 1 \\ 2 & a \end{array} \right|}{4} = \frac {2 \left| \begin{array}{c c} a & 1 \\ 2 & a \end{array} \right|}{A _ {2}}.</equation>若<equation>\left| \begin{array}{ll} a & 1 \\ 2 & a \end{array} \right|=0</equation>，则 a =<equation>\pm \sqrt{2}</equation>.但将 a =<equation>\pm \sqrt{2}</equation>代入<equation>\left| \begin{array}{lll} a & 0 & 1 \\ 1 & a & 1 \\ 1 & 2 & a \end{array} \right|</equation>所得行列式并不等于4，故<equation>\left| \begin{array}{ll} a & 1 \\ 2 & a \end{array} \right| \neq</equation>0. 因此，由（1）式可得<equation>A_{2}=8</equation>，即<equation>\left| \begin{array}{lll} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right|=8.</equation>

---

**2022年第6题 | 选择题 | 5分 | 答案: D**

6. 设矩阵<equation>A=\left( \begin{array}{c c c} {1} & {1} & {1} \\ {1} & {a} & a^{2} \\ {1} & {b} & b^{2} \end{array} \right), b=\left( \begin{array}{c} {1} \\ {2} \\ {4} \end{array} \right),</equation>则线性方程组<equation>A x=b</equation>的解的情况为（    )

A. 无解 B. 有解 C. 有无穷多解或无解 D. 有唯一解或无解

答案: D

**解析:**解 （法一）注意到<equation>| \mathbf {A} | = \left| \begin{array}{l l l} 1 & 1 & 1 \\ 1 & a & a ^ {2} \\ 1 & b & b ^ {2} \end{array} \right| = \left| \begin{array}{l l l} 1 & 1 & 1 \\ 1 & a & b \\ 1 & a ^ {2} & b ^ {2} \end{array} \right| = (b - a) (b - 1) (a - 1).</equation>当 a≠1,b≠1，且 a≠b时，<equation>|A| \neq 0.</equation>由克拉默法则可知，此时方程组<equation>A x=b</equation>有唯一解.

当 a = 1时，<equation>(A, b) = \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 2 \\ 1 & b & b ^ {2} & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 0 & 0 & 0 & 1 \\ 1 & b & b ^ {2} & 4 \end{array} \right).</equation>r（A,b）<equation>\neq r(A)</equation>，方程组无解.同理可得，当b=1时，r（A,b）<equation>\neq r(A)</equation>，方程组无解.

当 a = b时，<equation>(\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 1 & a & a ^ {2} & 2 \\ 1 & b & b ^ {2} & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 1 & a & a ^ {2} & 2 \\ 0 & 0 & 0 & 2 \end{array} \right).</equation><equation>r ( \mathbf{A}, \mathbf{b}) \neq r (\mathbf{A})</equation>，方程组无解.

综上所述，方程组<equation>A x=b</equation>的解的情况只有两种可能，有唯一解或无解.应选D.

（法二）直接对增广矩阵（A,b）作初等行变换.<equation>(\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 1 & a & a ^ {2} & 2 \\ 1 & b & b ^ {2} & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 0 & a - 1 & a ^ {2} - 1 & 1 \\ 0 & b - 1 & b ^ {2} - 1 & 3 \end{array} \right).</equation>当 a = b = 1时，<equation>r(\mathbf{A})=1, r(\mathbf{A},\mathbf{b})=2</equation>，方程组无解.

当<equation>a = 1,b\neq 1</equation>或<equation>a\neq 1,b = 1</equation>时，<equation>r(A) = 2,r(A,b) = 3</equation>，方程组无解.

当 a = b ，但均不等于1时，<equation>r(\mathbf{A})=2,r(\mathbf{A},\mathbf{b})=3</equation>，方程组无解.

当<equation>a\neq 1,b\neq 1</equation>，且<equation>a\neq b</equation>时，<equation>r(A) = r(A,b) = 3.</equation>方程组有唯一解.

综上所述，方程组<equation>A x=b</equation>的解的情况只有两种可能，有唯一解或无解.应选D.

---

**2021年第6题 | 选择题 | 5分 | 答案: D**

6. 设<equation>A=\left(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4}\right)</equation>为4阶正交矩阵，若矩阵<equation>B=\left( \begin{array}{c}\alpha_{1}^{\mathrm{T}}\\ \alpha_{2}^{\mathrm{T}}\\ \alpha_{3}^{\mathrm{T}} \end{array} \right),\beta=\left( \begin{array}{c}1\\ 1\\ 1 \end{array} \right),k</equation>表示任意常数，则线性方程组<equation>Bx=\beta</equation>的通解 x=（    ）

A.<equation>\alpha_{2}+\alpha_{3}+\alpha_{4}+k\alpha_{1}</equation>B.<equation>\alpha_{1}+\alpha_{3}+\alpha_{4}+k\alpha_{2}</equation>C.<equation>\alpha_{1}+\alpha_{2}+\alpha_{4}+k\alpha_{3}</equation>D.<equation>\alpha_{1}+\alpha_{2}+\alpha_{3}+k\alpha_{4}</equation>

答案: D

**解析:**解 由于 A为正交矩阵，故<equation>\boldsymbol{\alpha}_{i}^{\mathrm{T}}\boldsymbol{\alpha}_{i}=1, \boldsymbol{\alpha}_{i}^{\mathrm{T}}\boldsymbol{\alpha}_{j}=0 ( i \neq j )</equation>，i，j=1,2,3,4.

先求<equation>Bx=0</equation>的解. B是<equation>3\times 4</equation>矩阵，<equation>r(B)=3</equation>，故<equation>Bx=0</equation>的基础解系中包含4-3=1个解向量.<equation>B x=0</equation>即<equation>\left( \begin{array}{l} \boldsymbol{\alpha}_{1}^{\mathrm{T}} \\ \boldsymbol{\alpha}_{2}^{\mathrm{T}} \\ \boldsymbol{\alpha}_{3}^{\mathrm{T}} \end{array} \right) x=0</equation>，也即<equation>\left( \begin{array}{l} \boldsymbol{\alpha}_{1}^{\mathrm{T}} x \\ \boldsymbol{\alpha}_{2}^{\mathrm{T}} x \\ \boldsymbol{\alpha}_{3}^{\mathrm{T}} x \end{array} \right)=\left( \begin{array}{l} 0 \\ 0 \\ 0 \end{array} \right).</equation>因为<equation>\alpha_{4}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>均正交，所以<equation>\alpha_{4}</equation>是<equation>B x=0</equation>的解.<equation>Bx = 0</equation>的通解为<equation>k\alpha_{4}</equation>，其中<equation>k</equation>为任意常数.

再求<equation>B x=\beta</equation>的一个特解.

由于<equation>\boldsymbol{\alpha}_{i}^{\mathrm{T}}\boldsymbol{\alpha}_{i}=1, \boldsymbol{\alpha}_{i}^{\mathrm{T}}\boldsymbol{\alpha}_{j}=0 ( i \neq j ) , i,j=1,2,3,4</equation>，故<equation>\begin{aligned} \left(  \boldsymbol {\alpha} _ {1} ^ {\mathrm {T}} \\ \boldsymbol {\alpha} _ {2} ^ {\mathrm {T}} \\ \boldsymbol {\alpha} _ {3} ^ {\mathrm {T}}  \right) \left(\boldsymbol {\alpha} _ {1} + \boldsymbol {\alpha} _ {2} + \boldsymbol {\alpha} _ {3}\right) &= \left(  \boldsymbol {\alpha} _ {1} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {1} + \boldsymbol {\alpha} _ {1} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {2} + \boldsymbol {\alpha} _ {1} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {3} \\ \boldsymbol {\alpha} _ {2} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {1} + \boldsymbol {\alpha} _ {2} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {2} + \boldsymbol {\alpha} _ {2} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {3} \\ \boldsymbol {\alpha} _ {3} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {1} + \boldsymbol {\alpha} _ {3} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {2} + \boldsymbol {\alpha} _ {3} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {3}  \right) &= \left(  1 \\ 1 \\ 1  \right). \end{aligned}</equation><equation>\alpha_{1} + \alpha_{2} + \alpha_{3}</equation>是<equation>Bx = \beta</equation>的一个特解.

因此，<equation>B x=\beta</equation>的通解为<equation>\alpha_{1}+\alpha_{2}+\alpha_{3}+k\alpha_{4}</equation>其中k为任意常数.应选D.

---

**2020年第5题 | 选择题 | 4分 | 答案: C**

5. 设4阶矩阵<equation>A=(a_{ij})</equation>不可逆，<equation>a_{12}</equation>的代数余子式<equation>A_{12}\neq0,\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4}</equation>为矩阵 A的列向量组，<equation>A^{*}</equation>为 A的伴随矩阵，则方程组<equation>A^{*}x=0</equation>的通解为（    )

A.<equation>x=k_{1}\alpha_{1}+k_{2}\alpha_{2}+k_{3}\alpha_{3}</equation>其中<equation>k_{1},k_{2},k_{3}</equation>为任意常数

B.<equation>x=k_{1}\alpha_{1}+k_{2}\alpha_{2}+k_{3}\alpha_{4}</equation>其中<equation>k_{1},k_{2},k_{3}</equation>为任意常数

C.<equation>x=k_{1}\alpha_{1}+k_{2}\alpha_{3}+k_{3}\alpha_{4}</equation>其中<equation>k_{1},k_{2},k_{3}</equation>为任意常数

D.<equation>x=k_{1}\alpha_{2}+k_{2}\alpha_{3}+k_{3}\alpha_{4}</equation>其中<equation>k_{1},k_{2},k_{3}</equation>为任意常数

答案: C

**解析:**解 由 A不可逆可知，<equation>|A|=0</equation>.于是，<equation>A^{*}A=|A|E=O</equation>.从而， A的列向量均为<equation>A^{*}x=0</equation>的解.

另一方面，<equation>A_{12}\neq0</equation>，说明<equation>A^{*}</equation>中有非零元素，<equation>r(A^{*})\geqslant1.</equation>又因为 A不可逆，所以<equation>r(A)\leqslant3.</equation>但是当<equation>r(A)<3</equation>时，<equation>r(A^{*})=0.</equation>因此，<equation>r(A)=3, r(A^{*})=1.</equation><equation>A^{*}x=0</equation>的基础解系中包含3个解向量.

由<equation>A_{12}\neq0</equation>可知，<equation>\left( \begin{array}{c c c} a_{21} & a_{23} & a_{24} \\ a_{31} & a_{33} & a_{34} \\ a_{41} & a_{43} & a_{44} \end{array} \right)\neq0.</equation>.于是，<equation>\left( \begin{array}{c} a_{21} \\ a_{31} \\ a_{41} \end{array} \right), \left( \begin{array}{c} a_{23} \\ a_{33} \\ a_{43} \end{array} \right), \left( \begin{array}{c} a_{24} \\ a_{34} \\ a_{44} \end{array} \right)</equation>线性无关.由分析中的结论可知，<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>线性无关，从而构成<equation>A^{*}x=0</equation>的一个基础解系.

因此，<equation>A^{*}x=0</equation>的通解可写为<equation>x=k_{1}\alpha_{1}+k_{2}\alpha_{3}+k_{3}\alpha_{4}</equation>，其中<equation>k_{1},k_{2},k_{3}</equation>为任意常数.应选C.

---

**2019年第13题 | 填空题 | 4分**

13. 已知矩阵<equation>A=\left( \begin{array}{c c c} 1 & 0 & -1 \\ 1 & 1 & -1 \\ 0 & 1 & a^{2}-1 \end{array} \right), b=\left( \begin{array}{c} 0 \\ 1 \\ a \end{array} \right),</equation>若线性方程组<equation>A x=b</equation>有无穷多解，则 a=___

**解析:**由<equation>A x=b</equation>有无穷多解可得，<equation>r ( A )=r ( A , b ) < 3.</equation>对（A，b）作初等行变换.<equation>(\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} 1 & 0 & - 1 & 0 \\ 1 & 1 & - 1 & 1 \\ 0 & 1 & a ^ {2} - 1 & a \end{array} \right) \xrightarrow {r _ {2} - r _ {1}} \left( \begin{array}{c c c c} 1 & 0 & - 1 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 1 & a ^ {2} - 1 & a \end{array} \right) \xrightarrow {r _ {3} - r _ {2} ^ {*}} \left( \begin{array}{c c c c} 1 & 0 & - 1 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & a ^ {2} - 1 & a - 1 \end{array} \right).</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

由上式可知<equation>r(A)\geqslant 2</equation>，故<equation>r(A) = r(A,b) = 2.</equation>于是，<equation>a^{2} - 1 = 0</equation>且<equation>a - 1 = 0</equation>，解得<equation>a = 1.</equation>

---

**2018年第21题 | 解答题 | 11分**

21. (本题满分11分)

已知 a是常数，且矩阵<equation>A=\left( \begin{array}{c c c} 1 & 2 & a \\ 1 & 3 & 0 \\ 2 & 7 & -a \end{array} \right)</equation>可经初等列变换化为矩阵<equation>B=\left( \begin{array}{c c c} 1 & a & 2 \\ 0 & 1 & 1 \\ -1 & 1 & 1 \end{array} \right).</equation>I. 求 a;

II. 求满足<equation>A P=B</equation>的可逆矩阵<equation>P.</equation>

**答案:**（ I ）<equation>a=2;</equation>（Ⅱ）满足<equation>A P=B</equation>的可逆矩阵为<equation>\boldsymbol {P} = \left( \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right),</equation>其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数，且<equation>k_{2} \neq k_{3}</equation>.

**解析:**解（I）由于 A可经初等列变换化为 B，故矩阵方程 AX=B有解.于是，<equation>r(A)=r(A,B).</equation>对（A,B）作初等行变换.<equation>\begin{array}{l} (A, B) = \left( \begin{array}{c c c c c c} 1 & 2 & a & 1 & a & 2 \\ 1 & 3 & 0 & 0 & 1 & 1 \\ 2 & 7 & - a & - 1 & 1 & 1 \end{array} \right) \xrightarrow [ r _ {3} - 2 r _ {1} ]{r _ {2} - r _ {1}} \left( \begin{array}{c c c c c c} 1 & 2 & a & 1 & a & 2 \\ 0 & 1 & - a & - 1 & 1 - a & - 1 \\ 0 & 3 & - 3 a & - 3 & 1 - 2 a & - 3 \end{array} \right) \\ \xrightarrow [ r _ {3} ^ {*} - 3 r _ {2} ^ {*} ]{r _ {1} - 2 r _ {2} ^ {*}} \left( \begin{array}{c c c c c c} 1 & 0 & 3 a & 3 & 3 a - 2 & 4 \\ 0 & 1 & - a & - 1 & 1 - a & - 1 \\ 0 & 0 & 0 & 0 & a - 2 & 0 \end{array} \right). \\ \end{array}</equation>当且仅当 a=2时，<equation>r(\mathbf{A})=r(\mathbf{A},\mathbf{B})=2.</equation>或者，由矩阵 A可经初等列变换化为矩阵 B可知，A的列秩等于 B的列秩，从而<equation>r ( \mathbf{A})=r (\mathbf{B})</equation>.同上面的计算可知<equation>r ( \mathbf{A})=2</equation>，当且仅当 a=2时，<equation>r ( \mathbf{A})=r ( \mathbf{B})</equation>.

因此，<equation>a=2.</equation>（Ⅱ）当 a=2时，<equation>(\boldsymbol {A}, \boldsymbol {B}) \rightarrow \left(\begin{array}{c c c c c c}1&0&6&3&4&4\\0&1&- 2&- 1&- 1&- 1\\0&0&0&0&0&0\end{array}\right).</equation><equation>A X=B</equation>等价于<equation>\left( \begin{array}{c c c} 1 & 0 & 6 \\ 0 & 1 & -2 \\ 0 & 0 & 0 \end{array} \right) X=\left( \begin{array}{c c c} 3 & 4 & 4 \\ -1 & -1 & -1 \\ 0 & 0 & 0 \end{array} \right).</equation>记<equation>\left( \begin{array}{c c c} 1 & 0 & 6 \\ 0 & 1 & -2 \\ 0 & 0 & 0 \end{array} \right)=A^{\prime}.</equation>方程组<equation>A^{\prime} x=0</equation>的一个基础解系为<equation>(-6,2,1)^{\mathrm{T}}.</equation>于是，方程组<equation>A^{\prime} x=(3,-1,0)^{\mathrm{T}}</equation>的通解为<equation>x_{1}=k_{1}(-6,2,1)^{\mathrm{T}}+</equation><equation>(3,-1,0)^{\mathrm{T}}</equation>其中<equation>k_{1}</equation>为任意常数；方程组<equation>A^{\prime} x=(4,-1,0)^{\mathrm{T}}</equation>的通解为<equation>x_{2}=k_{2}(-6,2,1)^{\mathrm{T}}+</equation><equation>(4,-1,0)^{\mathrm{T}}</equation>其中<equation>k_{2}</equation>为任意常数；方程组<equation>A^{\prime} x=(4,-1,0)^{\mathrm{T}}</equation>的通解为<equation>x_{3}=k_{3}(-6,2,1)^{\mathrm{T}}+</equation><equation>(4,-1,0)^{\mathrm{T}}</equation>其中<equation>k_{3}</equation>为任意常数.

因此，矩阵方程 AX=B的通解为<equation>\boldsymbol {X} = \left( \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right),</equation>其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数.

若可逆矩阵 P满足 AP=B，则<equation>\boldsymbol {P} = \left( \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right),</equation>且<equation>| P | \neq 0.</equation>由于<equation>| P | = \left| \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right| = \left| \begin{array}{c c c} 0 & 1 & 1 \\ - 1 & - 1 & - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right| = \left| \begin{array}{c c c} 0 & 1 & 1 \\ - 1 & 0 & 0 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right| = k _ {3} - k _ {2},</equation>故当<equation>k_{2}\neq k_{3}</equation>时，P可逆.

因此，满足 AP=B的可逆矩阵为<equation>\boldsymbol {P} = \left( \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right),</equation>其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数，且<equation>k_{2} \neq k_{3}</equation>.

---

**2017年第20题 | 解答题 | 11分**

20. (本题满分11分)

设3阶矩阵<equation>A=(\alpha_{1},\alpha_{2},\alpha_{3})</equation>有3个不同的特征值，且<equation>\alpha_{3}=\alpha_{1}+2\alpha_{2}.</equation>I. 证明<equation>r(A)=2;</equation>II. 若<equation>\beta=\alpha_{1}+\alpha_{2}+\alpha_{3}</equation>，求方程组<equation>A x=\beta</equation>的通解.

**答案:**（I）证明略；

（Ⅱ）<equation>k ( 1, 2,-1 )^{\mathrm{T}}+( 1, 1, 1 )^{\mathrm{T}}</equation>为线性方程组<equation>A x=\beta</equation>的通解，其中 k为任意常数.

**解析:**解（I）（法一）由于 A有3个不同的特征值<equation>\lambda_{1},\lambda_{2},\lambda_{3}</equation>，故 A相似于对角矩阵，且至多仅有一个零特征值.该对角矩阵的秩<equation>\geqslant 2</equation>.又因为相似的矩阵有相同的秩，所以<equation>r(A)\geqslant 2.</equation>另一方面，<equation>\alpha_{3} = \alpha_{1} + 2\alpha_{2}</equation>，故<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性相关，<equation>|A| = 0.</equation>由于<equation>| A| = \lambda_{1}\lambda_{2}\lambda_{3}</equation>，故A有一个特征值为零.

因此，<equation>r ( \mathbf{A} )=2.</equation>（法二）也可以如下证明0是A的一个特征值.

由<equation>\boldsymbol{\alpha}_{3}=\boldsymbol{\alpha}_{1}+2\boldsymbol{\alpha}_{2}</equation>知，<equation>\left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) \left( \begin{array}{c} 1 \\ 2 \\ - 1 \end{array} \right) = \mathbf {0} = 0 \left( \begin{array}{c} 1 \\ 2 \\ - 1 \end{array} \right).</equation>于是，0是 A的一个特征值，<equation>( 1, 2, - 1 )^{\mathrm{T}}</equation>是 A的属于特征值0的一个特征向量.

其余同法一.

（Ⅱ）考虑<equation>A x=0</equation>.由于<equation>r(A)=2</equation>，故<equation>A x=0</equation>的基础解系中只包含一个向量.又因为<equation>\alpha_{3}=\alpha_{1}+2\alpha_{2}</equation>，所以<equation>(\alpha_{1},\alpha_{2},\alpha_{3})(1,2,-1)^{\mathrm{T}}=0</equation>，即<equation>(1,2,-1)^{\mathrm{T}}</equation>是该齐次线性方程组的一个基础解系.由于<equation>\beta =\alpha_{1}+\alpha_{2}+\alpha_{3}</equation>，即<equation>(\alpha_{1},\alpha_{2},\alpha_{3})(1,1,1)^{\mathrm{T}}=\beta</equation>，故<equation>(1,1,1)^{\mathrm{T}}</equation>是<equation>A x=\beta</equation>的一个特解.因此，<equation>k(1,2,-1)^{\mathrm{T}}+(1,1,1)^{\mathrm{T}}</equation>为线性方程组<equation>A x=\beta</equation>的通解，其中<equation>k</equation>为任意常数.

---

**2016年第20题 | 解答题 | 11分**

20. （本题满分11分）

设矩阵<equation>A = \left( \begin{array}{c c c} 1 & 1 & 1 - a \\ 1 & 0 & a \\ a + 1 & 1 & a + 1 \end{array} \right),\beta = \left( \begin{array}{c} 0 \\ 1 \\ 2a - 2 \end{array} \right),</equation>且方程组<equation>A x=\beta</equation>无解.

I. 求 a的值；

II. 求方程组<equation>A^{\mathrm{T}} A x=A^{\mathrm{T}} \beta</equation>的通解.

**答案:**（ I ）<equation>a=0</equation>； （ II ）通解为<equation>k(0,-1,1)^{\mathrm{T}}+(1,-2,0)^{\mathrm{T}}</equation>，其中 k为任意常数.

**解析:**解（I）由于<equation>A x=\beta</equation>无解，故由非齐次线性方程组有解的充分必要条件可知，<equation>r(A,\beta)\neq r(A).</equation><equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c} 1 & 1 & 1 - a & 0 \\ 1 & 0 & a & 1 \\ a + 1 & 1 & a + 1 & 2 a - 2 \end{array} \right) \xrightarrow {r _ {2} - r _ {1}} \frac {r _ {2} - r _ {1}}{r _ {3} - (a + 1) r _ {1}} \left( \begin{array}{c c c c} 1 & 1 & 1 - a & 0 \\ 0 & - 1 & 2 a - 1 & 1 \\ 0 & - a & a ^ {2} + a & 2 a - 2 \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} \times (- 1)} \left( \begin{array}{c c c c} 1 & 1 & 1 - a & 0 \\ 0 & 1 & 1 - 2 a & - 1 \\ 0 & - a & a ^ {2} + a & 2 a - 2 \end{array} \right) \xrightarrow {r _ {1} - r _ {2} ^ {* *}} \left( \begin{array}{c c c c} 1 & 0 & a & 1 \\ 0 & 1 & 1 - 2 a & - 1 \\ 0 & 0 & - a ^ {2} + 2 a & a - 2 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

由上面的式子可知，<equation>r ( A ) \geqslant 2</equation>. 从而，<equation>A x=\beta</equation>无解当且仅当<equation>r ( A )=2</equation>且<equation>r ( A,\beta)=3.</equation>此时，<equation>- a^{2}+2 a=0</equation>，且<equation>a-2\neq0</equation>，解得 a=0.<equation>\begin{aligned} (\mathrm {I I}) \mathrm {当} a &= 0 \mathrm {时}, \boldsymbol {A} = \left( \begin{array}{l l l} 1 & 1 & 1 \\ 1 & 0 & 0 \\ 1 & 1 & 1  \right), \boldsymbol {A} ^ {\mathrm {T}} &= \left( \begin{array}{l l l} 1 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 0 & 1  \right), \boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {A} &= \left( \begin{array}{l l l} 3 & 2 & 2 \\ 2 & 2 & 2 \\ 2 & 2 & 2  \right), \boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {\beta} &= \left(  - 1 \\ - 2 \\ - 2  \right). \end{aligned}</equation><equation>\begin{array}{l} \left(\boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {A}, \boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {\beta}\right) = \left( \begin{array}{c c c c} 3 & 2 & 2 & - 1 \\ 2 & 2 & 2 & - 2 \\ 2 & 2 & 2 & - 2 \end{array} \right) \xrightarrow [ r _ {2} \times \frac {1}{2} ]{r _ {3} - r _ {2}} \left( \begin{array}{c c c c} 3 & 2 & 2 & - 1 \\ 1 & 1 & 1 & - 1 \\ 0 & 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {1} - 2 r _ {2} ^ {*} ]{r _ {1} - 2 r _ {2} ^ {*}} \left( \begin{array}{c c c c} 1 & 0 & 0 & 1 \\ 1 & 1 & 1 & - 1 \\ 0 & 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} - r _ {1} ^ {*}} \left( \begin{array}{c c c c} 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & - 2 \\ 0 & 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation><equation>A^{\mathrm{T}} A x=A^{\mathrm{T}} \beta</equation>对应的齐次线性方程组等价于<equation>\left\{ \begin{array}{l l} x_{1}=0, \\ x_{2}+x_{3}=0. \end{array} \right.</equation>（0，-1，1）<equation>^{\mathrm{T}}</equation>为该方程组的一个基础解系.又因为<equation>(1,-2,0)^{\mathrm{T}}</equation>是<equation>A^{\mathrm{T}} A x=A^{\mathrm{T}} \beta</equation>的一个特解，所以<equation>A^{\mathrm{T}} A x=A^{\mathrm{T}} \beta</equation>的通解为<equation>k(0,-1,1)^{\mathrm{T}}+</equation>（1，-2，0）<equation>^{\mathrm{T}}</equation>，其中k为任意常数.

---

**2015年第5题 | 选择题 | 4分 | 答案: D**

5. 设矩阵<equation>A=\left( \begin{array}{c c c} {1} & {1} & {1} \\ {1} & {2} & {a} \\ {1} & {4} & {a^{2}} \\ \end{array} \right), b=\left( \begin{array}{c} {1} \\ {d} \\ {d^{2}} \\ \end{array} \right).</equation>若集合<equation>\Omega=\{1,2\}</equation>，则线性方程组<equation>A x=b</equation>有无穷多解的充分必要条件为（    ）

A. a<equation>\notin\Omega, d\notin\Omega</equation>B. a<equation>\notin\Omega, d\in\Omega</equation>C. a<equation>\in\Omega, d\notin\Omega</equation>D. a<equation>\in\Omega, d\in\Omega</equation>

答案: D

**解析:**解 （法一）对（A，b）作初等行变换.<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 1 & 2 & a & d \\ 1 & 4 & a ^ {2} & d ^ {2} \end{array} \right) \xrightarrow [ r _ {3} - r _ {1} ]{r _ {2} - r _ {1}} \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 0 & 1 & a - 1 & d - 1 \\ 0 & 3 & a ^ {2} - 1 & d ^ {2} - 1 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {*} - 3 r _ {2} ^ {*}} \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 0 & 1 & a - 1 & d - 1 \\ 0 & 0 & a ^ {2} - 3 a + 2 & d ^ {2} - 3 d + 2 \end{array} \right). \\ \end{array}</equation>(<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每作一次初等行变换，加一个*.）

由此可见，<equation>r ( \mathbf{A})=r ( \mathbf{A},\mathbf{b})<3</equation>当且仅当<equation>a^{2}-3 a+2=0</equation>且<equation>d^{2}-3 d+2=0</equation>即 a=1或a=2，且 d=1或d=2，也即 a<equation>\in\Omega</equation><equation>d \in\Omega.</equation>因此，<equation>a\in \Omega</equation>，<equation>d\in \Omega</equation>是<equation>Ax = b</equation>有无穷多解的充分必要条件.应选D.

（法二）当 a<equation>\in\Omega</equation>，d<equation>\in\Omega</equation>时，r（A）=r（A,b）=2<3，故 a<equation>\in\Omega</equation>，d<equation>\in\Omega</equation>是 Ax=b有无穷多解的充分条件.

当<equation>Ax = b</equation>有无穷多解时，<equation>r(A) = r(A,b) < 3</equation>，从而<equation>r(A) < 3</equation>，<equation>|A| = 0.</equation>由于<equation>|A|</equation>为范德蒙德行列式，故<equation>|A| = 0</equation>当且仅当<equation>a = 1</equation>或<equation>a = 2</equation>，即<equation>a \in \Omega .</equation>由于<equation>r(A,b) = r(A) < 3</equation>，故<equation>(1,d,d^{2})^{\mathrm{T}}</equation>与<equation>(1,1,1)^{\mathrm{T}}</equation>和<equation>(1,2,4)^{\mathrm{T}}</equation>线性相关，从而<equation>\left| \begin{array}{c c c} 1 & 1 & 1 \\ 1 & 2 & d \\ 1 & 4 & d^{2} \end{array} \right| = 0.</equation>再次由范德蒙德行列式的性质可推出<equation>d = 1</equation>或<equation>d = 2</equation>，即<equation>d \in \Omega .</equation>因此，<equation>a\in \Omega</equation>，<equation>d\in \Omega</equation>是<equation>Ax = b</equation>有无穷多解的充分必要条件.应选D.

（法三）排除法.我们可以把简单的值代入各选项，然后根据<equation>A x=b</equation>是否有无穷多解来排除错误选项.

选项A：代入<equation>a=0</equation>，<equation>d=0</equation>，<equation>r(\mathbf{A})=r(\mathbf{A},\mathbf{b})=3</equation>，不符合题意.

选项B：代入<equation>a=0</equation>，<equation>d\in\{1,2\}</equation>，<equation>r(\mathbf{A})=r(\mathbf{A},\mathbf{b})=3</equation>，不符合题意.

选项C：代入<equation>a\in\{1,2\}</equation>，<equation>d=0</equation>，<equation>r(\mathbf{A},\mathbf{b})=3</equation>，<equation>r(\mathbf{A})=2</equation>，不符合题意.

由上可见，选项A、B、C均不是正确选项.由排除法知，应选D.

---

**2014年第20题 | 解答题 | 11分**

20. (本题满分11分)

设矩阵<equation>A = \left( \begin{array}{c c c c} 1 & -2 & 3 & -4 \\ 0 & 1 & -1 & 1 \\ 1 & 2 & 0 & -3 \end{array} \right), E</equation>为3阶单位矩阵.

I. 求方程组<equation>A x=0</equation>的一个基础解系；

II. 求满足<equation>A B=E</equation>的所有矩阵 B.

**答案:**(20) (I)<equation>(-1,2,3,1)^{\mathrm{T}};</equation><equation>(\mathrm {I I}) \boldsymbol {B} = \left( \begin{array}{c c c} 2 - k _ {1} & 6 - k _ {2} & - 1 - k _ {3} \\ - 1 + 2 k _ {1} & - 3 + 2 k _ {2} & 1 + 2 k _ {3} \\ - 1 + 3 k _ {1} & - 4 + 3 k _ {2} & 1 + 3 k _ {3} \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right)</equation>其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数.

**解析:**解（I）考察系数矩阵 A.<equation>\begin{array}{l} \boldsymbol {A} = \left( \begin{array}{c c c c} 1 & - 2 & 3 & - 4 \\ 0 & 1 & - 1 & 1 \\ 1 & 2 & 0 & - 3 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c c} 1 & - 2 & 3 & - 4 \\ 0 & 1 & - 1 & 1 \\ 0 & 4 & - 3 & 1 \end{array} \right) \xrightarrow {r _ {1} + 2 r _ {2}} \left( \begin{array}{c c c c} 1 & 0 & 1 & - 2 \\ 0 & 1 & - 1 & 1 \\ 0 & 0 & 1 & - 3 \end{array} \right) \\ \xrightarrow {r _ {1} ^ {*} - r _ {3} ^ {* *}} \frac {1}{r _ {2} + r _ {3} ^ {* *}} \left( \begin{array}{c c c c} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & - 2 \\ 0 & 0 & 1 & - 3 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每作一次初等行变换，加一个*.）<equation>Ax = 0</equation>可化为方程组<equation>\left\{ \begin{array}{l} x_{1} + x_{4} = 0, \\ x_{2} - 2x_{4} = 0, \\ x_{3} - 3x_{4} = 0. \end{array} \right.</equation>由此可得<equation>\xi = (-1, 2, 3, 1)^{\mathrm{T}}</equation>为<equation>Ax = 0</equation>的一个基础解系.

（Ⅱ）实际上我们要求的是三个非齐次线性方程组<equation>A x=(1,0,0)^{\mathrm{T}}</equation><equation>A x=(0,1,0)^{\mathrm{T}}</equation><equation>A x=(0,0,1)^{\mathrm{T}}</equation>的解.由于它们的系数矩阵都是A，故可考虑对（A，E）作初等行变换，同第（I）问中的步骤可得<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {E}) = \left( \begin{array}{c c c c c c c} 1 & - 2 & 3 & - 4 & 1 & 0 & 0 \\ 0 & 1 & - 1 & 1 & 0 & 1 & 0 \\ 1 & 2 & 0 & - 3 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c c c c c} 1 & - 2 & 3 & - 4 & 1 & 0 & 0 \\ 0 & 1 & - 1 & 1 & 0 & 1 & 0 \\ 0 & 4 & - 3 & 1 & - 1 & 0 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} + 2 r _ {2}} \frac {1}{r _ {3} ^ {*} - 4 r _ {2}} \left( \begin{array}{c c c c c c c} 1 & 0 & 1 & - 2 & 1 & 2 & 0 \\ 0 & 1 & - 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & 1 & - 3 & - 1 & - 4 & 1 \end{array} \right) \xrightarrow {r _ {1} ^ {*} - r _ {3} ^ {* *}} \left( \begin{array}{c c c c c c c} 1 & 0 & 0 & 1 & 2 & 6 & - 1 \\ 0 & 1 & 0 & - 2 & - 1 & - 3 & 1 \\ 0 & 0 & 1 & - 3 & - 1 & - 4 & 1 \end{array} \right). \\ \end{array}</equation>由于 A为<equation>3 \times4</equation>矩阵，B为3阶单位矩阵，B应为<equation>4 \times3</equation>矩阵，从而知，<equation>Ax=(1,0,0)^{\mathrm{T}}</equation><equation>Ax=(0,1,0)^{\mathrm{T}}</equation><equation>Ax=(0,0,1)^{\mathrm{T}}</equation>的一个特解分别为<equation>(2,-1,-1,0)^{\mathrm{T}}</equation><equation>(6,-3,-4,0)^{\mathrm{T}}</equation><equation>(-1,1,1,0)^{\mathrm{T}}.</equation>与第（I）问中<equation>Ax=0</equation>的一个基础解系相结合，得到<equation>Ax=(1,0,0)^{\mathrm{T}}</equation><equation>Ax=(0,1,0)^{\mathrm{T}}</equation><equation>Ax=(0,0,1)^{\mathrm{T}}</equation>的通解分别为<equation>\begin{aligned} \boldsymbol {\alpha} _ {1} &= k _ {1} (- 1, 2, 3, 1) ^ {\mathrm {T}} + (2, - 1, - 1, 0) ^ {\mathrm {T}}, \\ \boldsymbol {\alpha} _ {2} &= k _ {2} (- 1, 2, 3, 1) ^ {\mathrm {T}} + (6, - 3, - 4, 0) ^ {\mathrm {T}}, \\ \boldsymbol {\alpha} _ {3} &= k _ {3} (- 1, 2, 3, 1) ^ {\mathrm {T}} + (- 1, 1, 1, 0) ^ {\mathrm {T}}, \end{aligned}</equation>其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数.

因此，<equation>B = \left( \begin{array}{c c c} 2 - k_{1} & 6 - k_{2} & -1 - k_{3} \\ -1 + 2k_{1} & -3 + 2k_{2} & 1 + 2k_{3} \\ -1 + 3k_{1} & -4 + 3k_{2} & 1 + 3k_{3} \\ k_{1} & k_{2} & k_{3} \end{array} \right)</equation>，其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数.

---

**2013年第20题 | 解答题 | 11分**

20. (本题满分11分)

设<equation>A = \left( \begin{array}{c c} 1 & a \\ 1 & 0 \end{array} \right), B = \left( \begin{array}{c c} 0 & 1 \\ 1 & b \end{array} \right).</equation>当<equation>a,b</equation>为何值时，存在矩阵<equation>C</equation>使得<equation>AC - CA = B</equation>，并求所有矩阵<equation>C</equation>

**答案:**(20)<equation>a=-1,b=0</equation>时，<equation>C=\left( \begin{array}{c c} k_{1}+k_{2}+1 & -k_{2} \\ k_{2} & k_{1} \end{array} \right)</equation>，其中<equation>k_{1},k_{2}</equation>为任意常数.

**解析:**解（法一）设<equation>C = \left( \begin{array}{ll} x_{1} & x_{2} \\ x_{3} & x_{4} \end{array} \right)</equation>，则由<equation>AC - CA = B</equation>可得<equation>\left( \begin{array}{c c} 1 & a \\ 1 & 0 \end{array} \right) \left( \begin{array}{c c} x _ {1} & x _ {2} \\ x _ {3} & x _ {4} \end{array} \right) - \left( \begin{array}{c c} x _ {1} & x _ {2} \\ x _ {3} & x _ {4} \end{array} \right) \left( \begin{array}{c c} 1 & a \\ 1 & 0 \end{array} \right) = \left( \begin{array}{c c} 0 & 1 \\ 1 & b \end{array} \right).</equation>写成线性方程组的形式：<equation>\left\{ \begin{array}{l} - x _ {2} + a x _ {3} = 0, \\ - a x _ {1} + x _ {2} + a x _ {4} = 1, \\ x _ {1} - x _ {3} - x _ {4} = 1, \\ x _ {2} - a x _ {3} = b. \end{array} \right.</equation>记该线性方程组为<equation>Px = \beta ,\beta = (0,1,1,b)^{\mathrm{T}}</equation>，则<equation>Px = \beta</equation>有解当且仅当<equation>r(P,\beta) = r(P)</equation><equation>\begin{array}{l} (\boldsymbol {P}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 0 & - 1 & a & 0 & 0 \\ - a & 1 & 0 & a & 1 \\ 1 & 0 & - 1 & - 1 & 1 \\ 0 & 1 & - a & 0 & b \end{array} \right) \xrightarrow {r _ {2} + a r _ {3}} \left( \begin{array}{c c c c c} 0 & - 1 & a & 0 & 0 \\ 0 & 1 & - a & 0 & a + 1 \\ 1 & 0 & - 1 & - 1 & 1 \\ 0 & 1 & - a & 0 & b \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} + r _ {1}} \binom {0} {r _ {4} + r _ {1}} \left( \begin{array}{c c c c c} 0 & - 1 & a & 0 & 0 \\ 0 & 0 & 0 & 0 & a + 1 \\ 1 & 0 & - 1 & - 1 & 1 \\ 0 & 0 & 0 & 0 & b \end{array} \right) \rightarrow \left( \begin{array}{c c c c c} 1 & 0 & - 1 & - 1 & 1 \\ 0 & 1 & - a & 0 & 0 \\ 0 & 0 & 0 & 0 & a + 1 \\ 0 & 0 & 0 & 0 & b \end{array} \right). \\ \end{array}</equation><equation>r_{2}^{*}</equation>表示对<equation>r_{2}</equation>作初等行变换后所得新的第二行.由上可见，若<equation>r ( \boldsymbol{P}, \boldsymbol{\beta})=r ( \boldsymbol{P})</equation>，则必有<equation>a+1=b=0</equation>从而<equation>a=-1</equation><equation>b=0.</equation>当 a=-1，b=0时，<equation>(\boldsymbol {P}, \boldsymbol {\beta}) \rightarrow \left(\begin{array}{c c c c c}1&0&- 1&- 1&1\\0&1&1&0&0\\0&0&0&0&0\\0&0&0&0&0\end{array}\right),</equation>即<equation>\left\{ \begin{array}{l l} x_{1}-x_{3}-x_{4}=1, \\ x_{2}+x_{3}=0. \end{array} \right.</equation>（1，0，0，1）<equation>^{\mathrm{T}}</equation>和（1，-1，1，0）<equation>^{\mathrm{T}}</equation>为该方程组对应的齐次线性方程组的一个基础解系.又（1，0，0，0）<equation>^{\mathrm{T}}</equation>为<equation>P x=\beta</equation>的一个特解，故<equation>P x=\beta</equation>的通解为<equation>k _ {1} \left(1, 0, 0, 1\right) ^ {\mathrm {T}} + k _ {2} \left(1, - 1, 1, 0\right) ^ {\mathrm {T}} + \left(1, 0, 0, 0\right) ^ {\mathrm {T}},</equation>其中<equation>k_{1}, k_{2}</equation>为任意常数.

因此，当 a=-1，b=0时，存在C使得AC-CA=B.此时的C形如<equation>\left( \begin{array}{c c} k_{1}+k_{2}+1 & -k_{2} \\ k_{2} & k_{1} \end{array} \right)</equation>，其中<equation>k_{1}, k_{2}</equation>为任意常数.

（法二）由于AC的迹等于CA的迹，故AC-CA的迹等于零.因此<equation>b=0.</equation><equation>B=\left( \begin{array}{cc}0&1\\ 1&0\end{array} \right).</equation>设<equation>C=\left( \begin{array}{cc}x_{1}&x_{2}\\ x_{3}&x_{4}\end{array} \right)</equation>，则由<equation>AC-CA=B</equation>可得<equation>\left\{ \begin{array}{l} - x _ {2} + a x _ {3} = 0, \\ - a x _ {1} + x _ {2} + a x _ {4} = 1, \\ x _ {1} - x _ {3} - x _ {4} = 1, \\ x _ {2} - a x _ {3} = 0. \end{array} \right.</equation>将<equation>x_{2}=a x_{3}</equation>代入<equation>- a x_{1}+x_{2}+a x_{4}=1</equation>可得<equation>- a \left(x_{1}-x_{3}-x_{4}\right)=1</equation>与<equation>x_{1}-x_{3}-x_{4}=1</equation>比较得，<equation>a=-1.</equation>从而得，<equation>a=-1</equation>，<equation>b=0.</equation>其余同法一.

---

**2012年第20题 | 解答题 | 11分**

20. (本题满分11分)

设<equation>\text {设} A = \left( \begin{array}{c c c c} 1 & a & 0 & 0 \\ 0 & 1 & a & 0 \\ 0 & 0 & 1 & a \\ a & 0 & 0 & 1 \end{array} \right), \beta = \left( \begin{array}{c} 1 \\ - 1 \\ 0 \\ 0 \end{array} \right).</equation>I. 计算行列式<equation>|A|</equation>;

II. 当实数<equation>a</equation>为何值时，方程组<equation>Ax = \beta</equation>有无穷多解，并求其通解.

**答案:**<equation>(\mathrm {I}) | \boldsymbol {A} | = 1 - a ^ {4};</equation>（Ⅱ）当 a=-1时，方程组<equation>A x=\beta</equation>有无穷多解，其通解为<equation>k(1,1,1,1)^{\mathrm{T}}+(0,-1,0,0)^{\mathrm{T}}</equation>，其中 k为任意常数.

**解析:**（ I ）按第一行展开<equation>|A|</equation>，得<equation>| \boldsymbol {A} | = \left| \begin{array}{c c c} 1 & a & 0 \\ 0 & 1 & a \\ 0 & 0 & 1 \end{array} \right| - a \left| \begin{array}{c c c} 0 & a & 0 \\ 0 & 1 & a \\ a & 0 & 1 \end{array} \right| = 1 - a ^ {4}.</equation>（Ⅱ）（法一）<equation>A x=\beta</equation>有无穷多解的充要条件为<equation>r(A)=r(A,\beta) < 4.</equation>由<equation>r(A) < 4</equation>可得，<equation>|A| = 0</equation>，从而<equation>a=\pm 1.</equation>当 a=1时，<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 1 & 0 & 0 & 1 & 0 \end{array} \right) \xrightarrow {r _ {4} - r _ {1}} \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & - 1 & 0 & 1 & - 1 \end{array} \right) \xrightarrow {r _ {4} ^ {*} + r _ {2}} \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1 & - 2 \end{array} \right) \\ \xrightarrow {r _ {4} ^ {* *} - r _ {3}} \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 & - 2 \end{array} \right). \\ \end{array}</equation><equation>(r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每作一次初等行变换，加一个<equation>*.</equation>）由上可知，<equation>r(A,\beta) = 4</equation>，而<equation>r(A) = 3</equation>，<equation>Ax = \beta</equation>无解.<equation>a = 1</equation>不符合题意.

当 a=-1时，<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 1 & - 1 & 0 & 0 & 1 \\ 0 & 1 & - 1 & 0 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ - 1 & 0 & 0 & 1 & 0 \end{array} \right) \xrightarrow {r _ {4} + r _ {1}} \left( \begin{array}{c c c c c} 1 & - 1 & 0 & 0 & 1 \\ 0 & 1 & - 1 & 0 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ 0 & - 1 & 0 & 1 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} + r _ {2}} \frac {r _ {4} ^ {*} + r _ {2}}{r _ {4} ^ {*} + r _ {2}} \left( \begin{array}{c c c c c} 1 & 0 & - 1 & 0 & 0 \\ 0 & 1 & - 1 & 0 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ 0 & 0 & - 1 & 1 & 0 \end{array} \right) \xrightarrow {r _ {1} ^ {*} + r _ {3}} \frac {r _ {2} + r _ {3}}{r _ {4} ^ {* *} + r _ {3}} \left( \begin{array}{c c c c c} 1 & 0 & 0 & - 1 & 0 \\ 0 & 1 & 0 & - 1 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>由上可知，<equation>r(\mathbf{A},\boldsymbol{\beta}) = r(\mathbf{A}) = 3 < 4</equation>，<equation>Ax = \boldsymbol{\beta}</equation>有无穷多解.

齐次方程组<equation>Ax = 0</equation>的通解为<equation>k(1,1,1,1)^{\mathrm{T}}</equation>，其中<equation>k</equation>为任意常数。又因为<equation>(0,-1,0,0)^{\mathrm{T}}</equation>为<equation>Ax = \beta</equation>的一个特解，所以<equation>Ax = \beta</equation>的通解为<equation>k(1,1,1,1)^{\mathrm{T}} + (0,-1,0,0)^{\mathrm{T}}</equation>，其中<equation>k</equation>为任意常数综上所述，当<equation>a = -1</equation>时，方程组<equation>Ax = \beta</equation>有无穷多解，其通解为<equation>k(1,1,1,1)^{\mathrm{T}} + (0,-1,0,0)^{\mathrm{T}}</equation>其中<equation>k</equation>为任意常数.

（法二）对含有参数<equation>a</equation>的增广矩阵<equation>(A, \beta)</equation>作初等行变换.<equation>(\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ a & 0 & 0 & 1 & 0 \end{array} \right) \xrightarrow {r _ {4} - a r _ {1}} \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ 0 & - a ^ {2} & 0 & 1 & - a \end{array} \right)</equation><equation>\xrightarrow {r _ {4} ^ {*} + a ^ {2} r _ {2}} \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ 0 & 0 & a ^ {3} & 1 & - a - a ^ {2} \end{array} \right) \xrightarrow {r _ {4} ^ {* *} - a ^ {3} r _ {3}} \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ 0 & 0 & 0 & 1 - a ^ {4} & - a - a ^ {2} \end{array} \right).</equation>由于<equation>A x=\beta</equation>有无穷多解，故<equation>r(A)=r(A,\beta) < 4.</equation>因此，<equation>1-a^{4}=0,-a-a^{2}=0</equation>解得 a=-1其余同法一.

