---

**2011年第6题 | 选择题 | 4分 | 答案: C**

6. 设 A为<equation>4 \times3</equation>矩阵，<equation>\eta_{1},\eta_{2},\eta_{3}</equation>是非齐次线性方程组<equation>A x=\beta</equation>的3个线性无关的解，<equation>k_{1},k_{2}</equation>为任意常数，则<equation>A x=\beta</equation>的通解为（    )

A.<equation>\frac{\eta_{2}+\eta_{3}}{2}+k_{1}(\eta_{2}-\eta_{1})</equation>B.<equation>\frac{\eta_{2}-\eta_{3}}{2}+k_{1}(\eta_{2}-\eta_{1})</equation>C.<equation>\frac{\eta_{2}+\eta_{3}}{2}+k_{1}(\eta_{2}-\eta_{1})+k_{2}(\eta_{3}-\eta_{1})</equation>D.<equation>\frac{\eta_{2}-\eta_{3}}{2}+k_{1}(\eta_{2}-\eta_{1})+k_{2}(\eta_{3}-\eta_{1})</equation>

答案: C

**解析:**解 由于<equation>Ax = \beta</equation>为非齐次线性方程组，故<equation>\beta \neq 0</equation>，从而<equation>A\neq O</equation>，即<equation>r(A)\geqslant 1.</equation>于是<equation>Ax = 0</equation>的基础解系里最多只含有2个线性无关的解。又由于<equation>\eta_{1},\eta_{2},\eta_{3}</equation>是<equation>Ax = \beta</equation>的3个线性无关的解，故<equation>\eta_{2} - \eta_{1}</equation><equation>\eta_{3} - \eta_{1}</equation>为<equation>Ax = 0</equation>的解且线性无关（证明见注<equation>\textcircled{2}</equation>），从而<equation>r(A)\leqslant 1.</equation>因此，<equation>r(A) = 1</equation>，<equation>Ax = 0</equation>的通解为<equation>k_{1}(\eta_{2} - \eta_{1}) + k_{2}(\eta_{3} - \eta_{1})</equation>，其中<equation>k_{1},k_{2}</equation>为任意常数.

又因为<equation>A\cdot \frac{\eta_{2}+\eta_{3}}{2}=\frac{A\eta_{2}+A\eta_{3}}{2}=\frac{\beta+\beta}{2}=\beta</equation>，即<equation>\frac{\eta_{2}+\eta_{3}}{2}</equation>为<equation>A x=\beta</equation>的解，所以<equation>A x=\beta</equation>的通解为<equation>\frac{\eta_{2}+\eta_{3}}{2}+k_{1}(\eta_{2}-\eta_{1})+k_{2}(\eta_{3}-\eta_{1})</equation>，其中<equation>k_{1},k_{2}</equation>为任意常数.应选C.

下面我们说明选项A、B、D均不正确.

由于<equation>A x=0</equation>的基础解系中包含2个向量，故选项A、B均不正确.

对选项D，<equation>\frac{\eta_{2}-\eta_{3}}{2}</equation>是<equation>A x=0</equation>的解，却不是<equation>A x=\beta</equation>的解，故选项D也不正确.

---

**2010年第20题 | 解答题 | 11分**

20. (本题满分11分)

设<equation>A=\left( \begin{array}{c c c} \lambda & 1 & 1 \\ 0 & \lambda-1 & 0 \\ 1 & 1 & \lambda \end{array} \right), b=\left( \begin{array}{c} a \\ 1 \\ 1 \end{array} \right).</equation>已知线性方程组<equation>A x=b</equation>存在两个不同的解.

I. 求<equation>\lambda, a;</equation>II. 求方程组<equation>A x=b</equation>的通解.

**答案:**（20）（I<equation>\lambda=-1</equation><equation>a=-2;</equation>（Ⅱ）<equation>k(1,0,1)^{\mathrm{T}}+\left(\frac{3}{2},-\frac{1}{2},0\right)^{\mathrm{T}}</equation>为<equation>A x=b</equation>的通解，其中k为任意常数.

**解析:**解（I）（法一）<equation>A x=b</equation>有两个不同的解意味着<equation>A x=b</equation>有解但不唯一，故<equation>r ( A )=r ( A , b ) < 3.</equation><equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} \lambda & 1 & 1 & a \\ 0 & \lambda - 1 & 0 & 1 \\ 1 & 1 & \lambda & 1 \end{array} \right) \xrightarrow {r _ {1} \leftrightarrow r _ {3}} \left( \begin{array}{c c c c} 1 & 1 & \lambda & 1 \\ 0 & \lambda - 1 & 0 & 1 \\ \lambda & 1 & 1 & a \end{array} \right) \xrightarrow {r _ {3} ^ {*} - \lambda r _ {1} ^ {*}} \left( \begin{array}{c c c c} 1 & 1 & \lambda & 1 \\ 0 & \lambda - 1 & 0 & 1 \\ 0 & 1 - \lambda & 1 - \lambda^ {2} & a - \lambda \end{array} \right) \\ \xrightarrow {r _ {3} ^ {* *} + r _ {2}} \left( \begin{array}{c c c c} 1 & 1 & \lambda & 1 \\ 0 & \lambda - 1 & 0 & 1 \\ 0 & 0 & 1 - \lambda^ {2} & a - \lambda + 1 \end{array} \right). \\ \end{array}</equation>(<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每做一次初等行变换，加一个*.）

由于<equation>r(A) < 3</equation>，故<equation>(\lambda -1)(1 - \lambda^2) = 0, \lambda = \pm 1.</equation>当<equation>\lambda = 1</equation>时，<equation>r(A,b) = 2</equation>，<equation>r(A) = 1</equation>，方程组无解，舍去.

当<equation>\lambda=-1</equation>时，<equation>(A,b)\rightarrow \left( \begin{array}{c c c c}1&1&-1&1\\ 0&-2&0&1\\ 0&0&0&a+2 \end{array} \right).</equation>此时<equation>r(A)=2.</equation>若<equation>r(A)=r(A,b)</equation>，则<equation>r(A,b)=2, a+2=0</equation>即<equation>a=-2.</equation>因此，<equation>\lambda=-1</equation>a=-2.

（法二）<equation>A x=b</equation>有两个不同的解意味着<equation>A x=b</equation>有解但不唯一，故<equation>r(A)=r(A,b)<3</equation>从而<equation>|A|=0.</equation><equation>| A | = \left| \begin{array}{c c c} \lambda & 1 & 1 \\ 0 & \lambda - 1 & 0 \\ 1 & 1 & \lambda \end{array} \right| = (\lambda - 1) ^ {2} (\lambda + 1) = 0.</equation>因此，<equation>\lambda=\pm1.</equation>当<equation>\lambda=1</equation>时，<equation>(\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} 1 & 1 & 1 & a \\ 0 & 0 & 0 & 1 \\ 1 & 1 & 1 & 1 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c c} 1 & 1 & 1 & a \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 1 - a \end{array} \right).</equation><equation>r(\mathbf{A}) = 1 < r(\mathbf{A},\mathbf{b}) = 2</equation>，原方程组无解.

当<equation>\lambda = -1</equation>时，同法一的方法对<equation>(A, b)</equation>作初等行变换可得<equation>(\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} - 1 & 1 & 1 & a \\ 0 & - 2 & 0 & 1 \\ 1 & 1 & - 1 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & - 1 & 1 \\ 0 & - 2 & 0 & 1 \\ 0 & 0 & 0 & a + 2 \end{array} \right).</equation>当<equation>a + 2 = 0</equation>，即<equation>a = -2</equation>时，<equation>r(\mathbf{A}) = r(\mathbf{A},\mathbf{b}) = 2 < 3</equation>，原方程组有无穷多解.

因此，<equation>\lambda=-1</equation>，a=-2.

（Ⅱ）由第（I）问知，当<equation>\lambda=-1</equation>a=-2时，<equation>(A, b) \rightarrow \left(\begin{array}{c c c c}1&1&- 1&1\\0&- 2&0&1\\0&0&0&0\end{array}\right) \xrightarrow {r _ {2} \times \left(- \frac {1}{2}\right)} \frac {r _ {2} \times \left(- \frac {1}{2}\right)}{r _ {1} - r _ {2} ^ {*}} \left(\begin{array}{c c c c}1&0&- 1&\frac {3}{2}\\\0&1&0&- \frac {1}{2}\\\0&0&0&0\end{array}\right).</equation>其对应的齐次方程组等价于<equation>\left\{\begin{array}{l l}x_{1}-x_{3}=0,\\ x_{2}=0,\end{array}\right.</equation>故可取（1，0，1）<equation>^{\mathrm{T}}</equation>为该方程组的一个基础解系.又<equation>\left(\frac{3}{2},-\frac{1}{2},0\right)^{\mathrm{T}}</equation>为原方程组的一个特解，故<equation>A x=b</equation>的通解为<equation>k(1,0,1)^{\mathrm{T}}+\left(\frac{3}{2},-\frac{1}{2},0\right)^{\mathrm{T}}</equation>其中k为任意常数.

---


### 矩阵的特征值和特征向量


