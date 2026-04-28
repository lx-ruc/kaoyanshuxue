# 数学一

## 线性代数

### 向量

#### 向量内积与向量正交

**2023年第15题 | 填空题 | 5分**

15. 已知向量<equation>\alpha_{1}=\left( \begin{array}{c}1\\ 0\\ 1\\ 1 \end{array} \right),\alpha_{2}=\left( \begin{array}{c}-1\\ -1\\ 0\\ 1 \end{array} \right),\alpha_{3}=\left( \begin{array}{c}0\\ 1\\ -1\\ 1 \end{array} \right),\beta=\left( \begin{array}{c}1\\ 1\\ 1\\ -1 \end{array} \right),\gamma=k_{1}\alpha_{1}+k_{2}\alpha_{2}+k_{3}\alpha_{3}</equation>，若<equation>\gamma^{\mathrm{T}}\alpha_{i}=\beta^{\mathrm{T}}\alpha_{i}</equation>（i=1,2,3），

则<equation>k_{1}^{2}+k_{2}^{2}+k_{3}^{2}=</equation>___

**答案:**# 11 9.

**解析:**注意到<equation>\alpha_{1}^{\mathrm{T}}\alpha_{2} = \alpha_{2}^{\mathrm{T}}\alpha_{3} = \alpha_{3}^{\mathrm{T}}\alpha_{1} = 0</equation>，故<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>相互正交，从而<equation>\begin{aligned} \boldsymbol {\gamma} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {1} &= \left(k _ {1} \boldsymbol {\alpha} _ {1} + k _ {2} \boldsymbol {\alpha} _ {2} + k _ {3} \boldsymbol {\alpha} _ {3}\right) ^ {\mathrm {T}} \boldsymbol {\alpha} _ {1} = k _ {1} \| \boldsymbol {\alpha} _ {1} \| ^ {2} = 3 k _ {1}, \\ \boldsymbol {\gamma} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {2} &= \left(k _ {1} \boldsymbol {\alpha} _ {1} + k _ {2} \boldsymbol {\alpha} _ {2} + k _ {3} \boldsymbol {\alpha} _ {3}\right) ^ {\mathrm {T}} \boldsymbol {\alpha} _ {2} = k _ {2} \| \boldsymbol {\alpha} _ {2} \| ^ {2} = 3 k _ {2}, \\ \boldsymbol {\gamma} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {3} &= \left(k _ {1} \boldsymbol {\alpha} _ {1} + k _ {2} \boldsymbol {\alpha} _ {2} + k _ {3} \boldsymbol {\alpha} _ {3}\right) ^ {\mathrm {T}} \boldsymbol {\alpha} _ {3} = k _ {3} \| \boldsymbol {\alpha} _ {3} \| ^ {2} = 3 k _ {3}. \end{aligned}</equation>计算可得<equation>\boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {1} = 1, \quad \boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {2} = - 3, \quad \boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {3} = - 1.</equation>由<equation>\boldsymbol{\gamma}^{\mathrm{T}}\boldsymbol{\alpha}_{i} = \boldsymbol{\beta}^{\mathrm{T}}\boldsymbol{\alpha}_{i}(i = 1,2,3)</equation>可得，<equation>3 k _ {1} = 1, \quad 3 k _ {2} = - 3, \quad 3 k _ {3} = - 1.</equation>解得<equation>k_{1} = \frac{1}{3}, k_{2} = -1, k_{3} = -\frac{1}{3}</equation>.

因此，<equation>k_{1}^{2}+k_{2}^{2}+k_{3}^{2}=\frac{1}{9}+1+\frac{1}{9}=\frac{11}{9}.</equation>

---

**2021年第6题 | 选择题 | 5分 | 答案: A**

6. 已知<equation>\alpha_{1}=\left( \begin{array}{c}1\\ 0\\ 1 \end{array} \right),\alpha_{2}=\left( \begin{array}{c}1\\ 2\\ 1 \end{array} \right),\alpha_{3}=\left( \begin{array}{c}3\\ 1\\ 2 \end{array} \right),\beta_{1}=\alpha_{1},\beta_{2}=\alpha_{2}-k\beta_{1},\beta_{3}=\alpha_{3}-l_{1}\beta_{1}-l_{2}\beta_{2}</equation>，若<equation>\beta_{1},\beta_{2},\beta_{3}</equation>两两正交，则<equation>l_{1},l_{2}</equation>依次为（    )

A.<equation>\frac{5}{2},\frac{1}{2}</equation>B.<equation>-\frac{5}{2},\frac{1}{2}</equation>C.<equation>\frac{5}{2},-\frac{1}{2}</equation>D.<equation>-\frac{5}{2},-\frac{1}{2}</equation>

答案: A

**解析:**将<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>施密特正交化.<equation>\boldsymbol {\beta} _ {1} = \boldsymbol {\alpha} _ {1} = \left( \begin{array}{c} 1 \\ 0 \\ 1 \end{array} \right),</equation><equation>\boldsymbol {\beta} _ {2} = \boldsymbol {\alpha} _ {2} - \frac {\left(\boldsymbol {\beta} _ {1} , \boldsymbol {\alpha} _ {2}\right)}{\| \boldsymbol {\beta} _ {1} \| ^ {2}} \boldsymbol {\beta} _ {1} = \left( \begin{array}{c} 1 \\ 2 \\ 1 \end{array} \right) - \frac {2}{2} \left( \begin{array}{c} 1 \\ 0 \\ 1 \end{array} \right) = \left( \begin{array}{c} 0 \\ 2 \\ 0 \end{array} \right),</equation><equation>\boldsymbol {\beta} _ {3} = \boldsymbol {\alpha} _ {3} - \frac {\left(\boldsymbol {\beta} _ {1} , \boldsymbol {\alpha} _ {3}\right)}{\| \boldsymbol {\beta} _ {1} \| ^ {2}} \boldsymbol {\beta} _ {1} - \frac {\left(\boldsymbol {\beta} _ {2} , \boldsymbol {\alpha} _ {3}\right)}{\| \boldsymbol {\beta} _ {2} \| ^ {2}} \boldsymbol {\beta} _ {2} = \boldsymbol {\alpha} _ {3} - \frac {5}{2} \boldsymbol {\beta} _ {1} - \frac {1}{2} \boldsymbol {\beta} _ {2}.</equation>因此，<equation>l_{1}=\frac{5}{2}, l_{2}=\frac{1}{2}.</equation>应选A.

---

**2019年第20题 | 解答题 | 11分**

20. (本题满分11分)

设向量组<equation>\alpha_{1}=(1,2,1)^{\mathrm{T}},\alpha_{2}=(1,3,2)^{\mathrm{T}},\alpha_{3}=(1,a,3)^{\mathrm{T}}</equation>为<equation>\mathbf{R}^{3}</equation>的一个基，<equation>\beta=(1,1,1)^{\mathrm{T}}</equation>在这个基下的坐标为<equation>(b,c,1)^{\mathrm{T}}</equation>.

I. 求 a,b,c ;

II. 证明<equation>\alpha_{2},\alpha_{3},\beta</equation>为<equation>\mathbf{R}^{3}</equation>的一个基，并求<equation>\alpha_{2},\alpha_{3},\beta</equation>到<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>的过渡矩阵.

**答案:**（ I ）<equation>a=3,b=2,c=-2;</equation>（Ⅱ）证明略，过渡矩阵为<equation>\left( \begin{array}{c c c}1&1&0\\ -\frac{1}{2}&0&1\\ \frac{1}{2}&0&0 \end{array} \right).</equation>

**解析:**解（I）（法一）由于<equation>\beta</equation>在<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>作为基时的坐标为<equation>(b,c,1)^{\mathrm{T}}</equation>，故<equation>\beta = b\alpha_{1} + c\alpha_{2} + \alpha_{3}</equation>将<equation>\alpha_{1},\alpha_{2},\alpha_{3},\beta</equation>的表达式代入，可得方程组<equation>b + c + 1 = 1,</equation><equation>\left\{2 b + 3 c + a = 1, \right.</equation><equation>b + 2 c + 3 = 1.</equation>(3) 式 - (1) 式可得<equation>c = -2</equation>，再由（1）式可得<equation>b = 2</equation>，然后代入（2）式可得<equation>a = 3</equation>因此，<equation>a=3,b=2,c=-2.</equation>（法二）记<equation>A=(\alpha_{1},\alpha_{2},\alpha_{3})</equation>，则由题意可知（b，c，1）<equation>^{\mathrm{T}}</equation>是<equation>A x=\beta</equation>的唯一解.于是，<equation>r(A)= r(A,\beta)=3.</equation>对（A,<equation>\beta</equation>）作初等行变换.<equation>(\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 2 & 3 & a & 1 \\ 1 & 2 & 3 & 1 \end{array} \right) \xrightarrow [ r _ {3} - r _ {1} ]{r _ {2} - 2 r _ {1}} \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 0 & 1 & a - 2 & - 1 \\ 0 & 1 & 2 & 0 \end{array} \right) \xrightarrow [ r _ {3} - r _ {2} ^ {*} ]{r _ {1} - r _ {2} ^ {*}} \left( \begin{array}{c c c c} 1 & 0 & 3 - a & 2 \\ 0 & 1 & a - 2 & - 1 \\ 0 & 0 & 4 - a & 1 \end{array} \right).</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每作一次初等行变换，加一个*.）

由于<equation>r(\mathbf{A}) = r(\mathbf{A},\boldsymbol{\beta}) = 3</equation>，故<equation>4 - a\neq 0.</equation>进一步对所得矩阵作初等行变换.<equation>(\boldsymbol {A}, \boldsymbol {\beta}) \rightarrow \left(\begin{array}{c c c c}1&0&3 - a&2\\0&1&a - 2&- 1\\0&0&1&\frac {1}{4 - a}\end{array}\right).</equation>因为<equation>(b, c, 1)^{\mathrm{T}}</equation>是<equation>Ax = \beta</equation>的唯一解，所以<equation>\frac{1}{4 - a} = 1</equation>，解得<equation>a = 3</equation>代入 a=3，可得<equation>(\boldsymbol {A}, \boldsymbol {\beta}) \rightarrow \left(\begin{array}{c c c c}1&0&0&2\\0&1&1&- 1\\0&0&1&1\end{array}\right)\rightarrow \left(\begin{array}{c c c c}1&0&0&2\\0&1&0&- 2\\0&0&1&1\end{array}\right).</equation>于是，<equation>b=2,c=-2.</equation>因此，<equation>a=3,b=2,c=-2.</equation>（Ⅱ）由于<equation>\mathbf{R}^{3}</equation>的维数是3，故要证明<equation>\alpha_{2},\alpha_{3},\beta</equation>为<equation>\mathbf{R}^{3}</equation>的一个基，只需证明<equation>\alpha_{2},\alpha_{3},\beta</equation>线性无关计算<equation>|\alpha_{2},\alpha_{3},\beta|.</equation><equation>\left| \alpha_ {2}, \alpha_ {3}, \beta \right| = \left| \begin{array}{c c c} 1 & 1 & 1 \\ 3 & 3 & 1 \\ 2 & 3 & 1 \end{array} \right| \xlongequal {c _ {2} - c _ {1}} \left| \begin{array}{c c c} 1 & 0 & 1 \\ 3 & 0 & 1 \\ 2 & 1 & 1 \end{array} \right| \xlongequal {\text {按 第二 列 展 开}} 2 \neq 0.</equation>因此，<equation>\alpha_{2},\alpha_{3},\beta</equation>线性无关，<equation>r(\alpha_{2},\alpha_{3},\beta) = 3,\alpha_{2},\alpha_{3},\beta</equation>为<equation>\mathbf{R}^{3}</equation>的一个基.

要计算从<equation>\alpha_{2},\alpha_{3},\beta</equation>到<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>的过渡矩阵，即求可逆矩阵<equation>P</equation>，使得<equation>(\alpha_{1},\alpha_{2},\alpha_{3}) = (\alpha_{2},\alpha_{3},\beta)P.</equation>对<equation>(\alpha_{2},\alpha_{3},\beta ,\alpha_{1},\alpha_{2},\alpha_{3})</equation>作初等行变换.<equation>\begin{array}{l} \left(\alpha_ {2}, \alpha_ {3}, \boldsymbol {\beta}, \alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) = \left( \begin{array}{c c c c c} 1 & 1 & 1 & 1 & 1 \\ 3 & 3 & 1 & 2 & 3 \\ 2 & 3 & 1 & 1 & 2 \\ 3 \end{array} \right) \xrightarrow [ r _ {2} ^ {*} \leftrightarrow r _ {3} ^ {*} ]{r _ {2} - 3 r _ {1}} \left( \begin{array}{c c c c c} 1 & 1 & 1 & 1 & 1 \\ 0 & 1 & - 1 & - 1 & 0 \\ 0 & 0 & - 2 & - 1 & 0 \\ 0 \end{array} \right) \\ \xrightarrow {r _ {1} - r _ {2} ^ {* *}} \frac {r _ {1} - r _ {2} ^ {* *}}{r _ {3} ^ {* *} \times \left(- \frac {1}{2}\right)} \left( \begin{array}{c c c c c} 1 & 0 & 2 & 2 & 1 & 0 \\ 0 & 1 & - 1 & - 1 & 0 & 1 \\ 0 & 0 & 1 & \frac {1}{2} & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} ^ {*} - 2 r _ {3} ^ {* * *}} \left( \begin{array}{c c c c c} 1 & 0 & 0 & 1 & 1 & 0 \\ 0 & 1 & 0 & - \frac {1}{2} & 0 & 1 \\ 0 & 0 & 1 & \frac {1}{2} & 0 & 0 \end{array} \right). \\ \end{array}</equation>因此，所求过渡矩阵<equation>P</equation>为<equation>\left( \begin{array}{c c c} 1 & 1 & 0 \\ -\frac{1}{2} & 0 & 1 \\ \frac{1}{2} & 0 & 0 \end{array} \right).</equation>

---

**2015年第20题 | 解答题 | 11分**

20. 设向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>为<equation>\mathbf{R}^{3}</equation>的一个基，<equation>\beta_{1}=2\alpha_{1}+2k\alpha_{3},\beta_{2}=2\alpha_{2},\beta_{3}=\alpha_{1}+(k+1)\alpha_{3}</equation>I. 证明向量组<equation>\beta_{1},\beta_{2},\beta_{3}</equation>为<equation>\mathbf{R}^{3}</equation>的一个基；

II. 当 k为何值时，存在非零向量<equation>\xi</equation>在基<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与基<equation>\beta_{1},\beta_{2},\beta_{3}</equation>下的坐标相同，并求所有的<equation>\xi.</equation>

**答案:**（Ⅱ）当 k=0时，存在非零向量<equation>\boldsymbol{\xi}</equation>在基<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>与基<equation>\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3}</equation>下的坐标相同，满足上述条件的所有<equation>\boldsymbol{\xi}=c\boldsymbol{\alpha}_{1}-c\boldsymbol{\alpha}_{3}</equation>，其中c为任意非零常数.

**解析:**解（I）（法一）由题设知<equation>(\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3}) = (\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3})\left( \begin{array}{c c c} 2 & 0 & 1 \\ 0 & 2 & 0 \\ 2k & 0 & k + 1 \end{array} \right)</equation>. 由于<equation>\left| \begin{array}{c c c} 2 & 0 & 1 \\ 0 & 2 & 0 \\ 2 k & 0 & k + 1 \end{array} \right| = 2 \left| \begin{array}{c c} 2 & 1 \\ 2 k & k + 1 \end{array} \right| = 4 \neq 0,</equation>故<equation>\left( \begin{array}{c c c} 2 & 0 & 1 \\ 0 & 2 & 0 \\ 2 k & 0 & k + 1 \end{array} \right)</equation>为可逆矩阵.又<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>为<equation>\mathbf{R}^{3}</equation>的基，故<equation>r(\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3})=r(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{2})=\dim \mathbf{R}^{3}</equation>从而<equation>\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3}</equation>为<equation>\mathbf{R}^{3}</equation>的一个基，结论得证.

（法二）设常数<equation>k_{1},k_{2},k_{3}</equation>满足<equation>k_{1}\boldsymbol{\beta}_{1} + k_{2}\boldsymbol{\beta}_{2} + k_{3}\boldsymbol{\beta}_{3} = \mathbf{0}</equation>，即<equation>k_{1}\left(2\boldsymbol{\alpha}_{1} + 2k\boldsymbol{\alpha}_{3}\right) + 2k_{2}\boldsymbol{\alpha}_{2} + k_{3}\left[\boldsymbol{\alpha}_{1} + (k + 1)\boldsymbol{\alpha}_{3}\right] = \mathbf{0},</equation>整理得到<equation>(2k_{1} + k_{3})\boldsymbol{\alpha}_{1} + 2k_{2}\boldsymbol{\alpha}_{2} + \left[(2k_{1} + k_{3})k + k_{3}\right]\boldsymbol{\alpha}_{3} = \mathbf{0}.</equation>由于<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>为<equation>\mathbf{R}^{3}</equation>的一个基，故它们线性无关，从而<equation>2 k _ {1} + k _ {3} = 0, \quad 2 k _ {2} = 0, \quad \left(2 k _ {1} + k _ {3}\right) k + k _ {3} = 0,</equation>解得<equation>k_{1}=0,k_{2}=0,k_{3}=0</equation>因此<equation>\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3}</equation>线性无关.于是<equation>r(\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3})=3=\dim \mathbf{R}^{3}</equation>从而<equation>\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},</equation><equation>\boldsymbol{\beta}_{3}</equation>为<equation>\mathbf{R}^{3}</equation>的一个基，结论得证.

（Ⅱ）设<equation>\pmb{\xi} = x_{1}\pmb{\alpha}_{1} + x_{2}\pmb{\alpha}_{2} + x_{3}\pmb{\alpha}_{3} = x_{1}\pmb{\beta}_{1} + x_{2}\pmb{\beta}_{2} + x_{3}\pmb{\beta}_{3}</equation>，则<equation>\left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\alpha} _ {2}, \boldsymbol {\alpha} _ {3}\right) \binom {x _ {1}} {x _ {2}} = \left(\boldsymbol {\beta} _ {1}, \boldsymbol {\beta} _ {2}, \boldsymbol {\beta} _ {3}\right) \binom {x _ {1}} {x _ {2}} = \left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\alpha} _ {2}, \boldsymbol {\alpha} _ {3}\right) \binom {2 0 1} {0 2 0} \binom {x _ {1}} {x _ {2}}.</equation>由<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>为<equation>\mathbf{R}^{3}</equation>的一个基以及坐标表示的唯一性知，<equation>\begin{aligned} \left( \begin{array}{c c c} 2 & 0 & 1 \\ 0 & 2 & 0 \\ 2 k & 0 & k + 1  \right) \left(  x _ {1} \\ x _ {2} \\ x _ {3}  \right) &= \left(  x _ {1} \\ x _ {2} \\ x _ {3}  \right), \quad \text {即} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 2 k & 0 & k  \right) \left(  x _ {1} \\ x _ {2} \\ x _ {3}  \right) &= \mathbf {0}. \end{aligned}</equation>因此存在非零向量<equation>\boldsymbol{\xi}</equation>在基<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与基<equation>\beta_{1},\beta_{2},\beta_{3}</equation>下的坐标相同当且仅当方程组（1）有非零解.该条件等价于<equation>\left| \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 2 k & 0 & k \end{array} \right| = - k = 0</equation>即<equation>k=0</equation>此时，方程组（1）的所有非零解为（c，0，<equation>- c )^{\mathrm{T}}</equation>其中c为任意非零常数.

综上所述，当<equation>k = 0</equation>时，存在非零向量<equation>\boldsymbol{\xi}</equation>在基<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>与基<equation>\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3}</equation>下的坐标相同，满足上述条件的所有<equation>\boldsymbol{\xi}=c\boldsymbol{\alpha}_{1}-c\boldsymbol{\alpha}_{3}</equation>，其中c为任意非零常数.

---

**2010年第13题 | 填空题 | 4分**

13. 设<equation>\alpha_{1}=(1,2,-1,0)^{\mathrm{T}},\alpha_{2}=(1,1,0,2)^{\mathrm{T}},\alpha_{3}=(2,1,1,a)^{\mathrm{T}}</equation>. 若由<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>生成的向量空间的维数为2，则 a=

**解析:**解（法一）由于由<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>生成的向量空间的维数为2，故向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>的秩为2，从而矩阵<equation>\left( \alpha_{1},\alpha_{2},\alpha_{3}\right)=\left( \begin{array}{c c c}1&1&2\\2&1&1\\-1&0&1\\0&2&a\end{array}\right)</equation>的秩为2.于是矩阵<equation>\left( \alpha_{1},\alpha_{2},\alpha_{3}\right)</equation>中任意3阶子式均为0，因此<equation>\left| \begin{array}{c c c}1&1&2\\-1&0&1\\0&2&a\end{array}\right|=0</equation>，解得 a=6.

（法二）由于由<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>生成的向量空间的维数为2，故<equation>r(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3})=2</equation>.又因为<equation>\left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\alpha} _ {2}, \boldsymbol {\alpha} _ {3}\right) = \left( \begin{array}{c c c} 1 & 1 & 2 \\ 2 & 1 & 1 \\ - 1 & 0 & 1 \\ 0 & 2 & a \end{array} \right) \xrightarrow [ r _ {3} + r _ {1} ]{r _ {2} - 2 r _ {1}} \left( \begin{array}{c c c} 1 & 1 & 2 \\ 0 & - 1 & - 3 \\ 0 & 1 & 3 \\ 0 & 2 & a \end{array} \right) \xrightarrow [ r _ {4} + 2 r _ {2} ]{r _ {3} + r _ {2}} \left( \begin{array}{c c c} 1 & 1 & 2 \\ 0 & - 1 & - 3 \\ 0 & 0 & 0 \\ 0 & 0 & a - 6 \end{array} \right),</equation>所以 a=6.

---

**2009年第5题 | 选择题 | 4分 | 答案: A**

5. 设<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>是3维向量空间<equation>\mathbf{R}^{3}</equation>的一组基，则由基<equation>\alpha_{1},\frac{1}{2}\alpha_{2},\frac{1}{3}\alpha_{3}</equation>到基<equation>\alpha_{1}+\alpha_{2},\alpha_{2}+\alpha_{3},\alpha_{3}+\alpha_{1}</equation>的过渡矩阵为（    ）

A.<equation>\left( \begin{array}{c c c} 1 & 0 & 1 \\ 2 & 2 & 0 \\ 0 & 3 & 3 \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c} 1 & 2 & 0 \\ 0 & 2 & 3 \\ 1 & 0 & 3 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c} \frac {1}{2} & \frac {1}{4} & - \frac {1}{6} \\ - \frac {1}{2} & \frac {1}{4} & \frac {1}{6} \\ \frac {1}{2} & - \frac {1}{4} & \frac {1}{6} \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} \frac {1}{2} & - \frac {1}{2} & \frac {1}{2} \\ \frac {1}{4} & \frac {1}{4} & - \frac {1}{4} \\ - \frac {1}{6} & \frac {1}{6} & \frac {1}{6} \end{array} \right)</equation>

答案: A

---


### 行列式
## 概率论与数理统计
### 随机变量的数字特征
#### 数学期望与方差

**2025年第8题 | 选择题 | 5分 | 答案: C**
8. 设二维随机变量 (X,Y) 服从正态分布 N(0,0;1,1;<equation>\rho</equation>), 其中<equation>\rho \in(-1,1)</equation>, 若 a,b为满足<equation>a^{2}+b^{2}=1</equation>的任意实数，则 D(aX+bY) 的最大值为（    )

A.1 B.2 C.<equation>1+|\rho|</equation>D.<equation>1+\rho^{2}</equation>
答案: C
**解析: **解 由于<equation>(X, Y)</equation>服从正态分布<equation>N(0, 0; 1, 1; \rho)</equation>，故<equation>D (X) = D (Y) = 1, \quad \operatorname {C o v} (X, Y) = \rho \sqrt {D (X)} \sqrt {D (Y)} = \rho .</equation>根据方差的性质，<equation>\begin{aligned} D (a X + b Y) &= D (a X) + D (b Y) + 2 \operatorname {C o v} (a X, b Y) = a ^ {2} D (X) + b ^ {2} D (Y) + 2 a b \operatorname {C o v} (X, Y) \\ &= a ^ {2} + b ^ {2} + 2 a b \rho \xlongequal {a ^ {2} + b ^ {2} = 1} 1 + 2 a b \rho . \end{aligned}</equation>又因为<equation>a^2 + b^2 = 1 \geqslant 2 |ab|</equation>，所以<equation>1 + 2ab\rho \leqslant 1 + 2|ab\rho| \leqslant 1 + |\rho|</equation>，从而<equation>D(aX + bY) \leqslant</equation>1+<equation>| \rho |</equation>. 若<equation>\rho > 0</equation>，则 D（aX+bY）的最大值为1+<equation>\rho</equation>，最大值在<equation>\left\{ \begin{array}{l l} a=\pm \frac{\sqrt{2}}{2}, \\ b=\pm \frac{\sqrt{2}}{2} \end{array} \right.</equation>时取得；若<equation>\rho < 0</equation>，则 D（aX+

bY）的最大值为<equation>1 - \rho</equation>，最大值在时取得；若<equation>\rho = 0</equation>，则<equation>D(aX + bY)\equiv 1.</equation>因此，<equation>D ( a X+b Y )</equation>的最大值为<equation>1+|\rho|</equation>，应选C.

---

**2023年第8题 | 选择题 | 5分 | 答案: C**
8. 设随机变量 X服从参数为1的泊松分布，则<equation>E[|X - E(X)|] =</equation>（    ）

A.<equation>\frac{1} {\mathrm{e}}</equation>B.<equation>\frac{1}{2}</equation>C.<equation>\frac{2} {\mathrm{e}}</equation>D. 1
答案: C
**解析: **归于 X服从参数为1的泊松分布，故<equation>E ( X )=1.</equation>从而<equation>| X - E (X) | = | X - 1 | = \left\{ \begin{array}{l l} 1, & X = 0, \\ X - 1, & X = 1, 2, \dots . \end{array} \right.</equation>由参数为1的泊松分布的分布律可知，<equation>P\{X = 0\} = \frac{1^{0}\cdot\mathrm{e}^{-1}}{0!} = \frac{1}{\mathrm{e}}.</equation>根据数学期望的定义，<equation>\begin{aligned} E [ \mid X - E (X) \mid ] &= 1 \cdot P \{X = 0 \} + \sum_ {k = 1} ^ {\infty} (k - 1) P \{X = k \} \\ &= \frac {1}{\mathrm {e}} + \sum_ {k = 0} ^ {\infty} (k - 1) P \{X = k \} - (0 - 1) P \{X = 0 \} \\ &= \frac {1}{\mathrm {e}} + E (X - 1) + \frac {1}{\mathrm {e}} = \frac {1}{\mathrm {e}} + E (X) - 1 + \frac {1}{\mathrm {e}} \\ \underline {{\underline {{E (X) = 1}}}} \frac {2}{\mathrm {e}}. \end{aligned}</equation>因此，应选C.

---

**2021年第22题 | 解答题 | 12分**
2. (本题满分12分)

在区间（0,2）上随机取一点，将该区间分成两段，较短一段的长度为 X，较长一段的长度为 Y，令<equation>Z=\frac{Y}{X}</equation>.

I. 求 X的概率密度；

II. 求 Z的概率密度；

III. 求<equation>E\left(\frac{X}{Y}\right).</equation>
**答案: **（I）<equation>X</equation>的概率密度为<equation>f_{X}(x)=\left\{\begin{array}{ll}1,&0<x<1,\\ 0,&\text{其他};\end{array} \right.</equation>（Ⅱ）<equation>Z</equation>的概率密度为<equation>f_{Z}(z)=\left\{\begin{array}{ll}0,&z<1,\\ \frac{2}{(z+1)^{2}},&z\geqslant 1; \end{array} \right.</equation>（Ⅲ）<equation>2\ln 2-1.</equation>
**解析: **解（I）根据分析，在区间（0，2）上随机取一点，将该点位置记为 W，则 W服从（0，2）上的均匀分布.<equation>X=\min \{ W,2-W\}</equation>由于<equation>X</equation>为较短一段的长度，故<equation>X</equation>的取值范围为（0,1].

记<equation>X</equation>的分布函数为<equation>F_{X}(x)</equation>当<equation>x < 0</equation>时，<equation>F_{X}(x) = P\{X\leqslant x\} = 0.</equation>当<equation>0\leqslant x < 1</equation>时，<equation>\begin{array}{l} F _ {X} (x) = P \{X \leqslant x \} = 1 - P \{X > x \} = 1 - P \{W > x, 2 - W > x \} \\ = 1 - P \left\{x < W < 2 - x \right\} = 1 - P \left\{W < 2 - x \right\} + P \left\{W \leqslant x \right\} \\ = 1 - \frac {2 - x}{2} + \frac {x}{2} = x. \\ \end{array}</equation>当<equation>x\geqslant 1</equation>时，<equation>F_{X}(x) = P\{X\leqslant x\} = 1.</equation>因此，<equation>F_{X}(x) = \left\{ \begin{array}{ll}0, & x < 0,\\ x, & 0\leqslant x < 1, f_{X}(x) = \left\{ \begin{array}{ll}1, & 0 < x < 1,\\ 0, & \text{其他}. \end{array} \right. X</equation>服从区间（0,1）上的均匀分布.<equation>1, x \geqslant 1,</equation>（Ⅱ）<equation>Z=\frac{Y}{X}=\frac{2-X}{X}=\frac{2}{X}-1.</equation>记Z的分布函数为<equation>F_{Z}(z).</equation>由于<equation>X</equation>的取值范围为<equation>(0,1]</equation>，故<equation>Z</equation>的取值范围为<equation>[1, + \infty)</equation>.

当<equation>z < 1</equation>时，<equation>F_{Z}(z) = P\{Z\leqslant z\} = 0.</equation>当<equation>z\geqslant 1</equation>时，<equation>\begin{array}{l} F _ {Z} (z) = P \left\{\frac {2}{X} - 1 \leqslant z \right\} = P \left\{\frac {2}{X} \leqslant z + 1 \right\} = P \left\{X \geqslant \frac {2}{z + 1} \right\} \\ = 1 - P \left\{X < \frac {2}{z + 1} \right\}. \\ \end{array}</equation>由于<equation>P\left\{X < \frac{2}{z + 1}\right\} = \frac{2}{z + 1}</equation>，故<equation>F_{Z}(z) = 1 - \frac{2}{z + 1}</equation>因此，<equation>F_{Z}(z) = \left\{ \begin{array}{ll} 0, & z < 1, \\ 1 - \frac{2}{z + 1}, & z \geqslant 1. \end{array} \right. f_{Z}(z) = \left\{ \begin{array}{ll} 0, & z < 1, \\ \frac{2}{(z + 1)^{2}}, & z \geqslant 1. \end{array} \right.</equation>（Ⅲ）（法一）注意到<equation>\frac{X}{Y}=\frac{X}{2-X}.</equation><equation>\begin{aligned} E \left(\frac {X}{Y}\right) &= E \left(\frac {X}{2 - X}\right) = \int_ {- \infty} ^ {+ \infty} \frac {x}{2 - x} \cdot f _ {X} (x) \mathrm {d} x = \int_ {0} ^ {1} \frac {x}{2 - x} \mathrm {d} x = \int_ {0} ^ {1} \left(- 1 + \frac {2}{2 - x}\right) \mathrm {d} x \\ &= \left[ - x - 2 \ln (2 - x) \right] \Bigg | _ {0} ^ {1} = 2 \ln 2 - 1. \end{aligned}</equation>（法二）由于<equation>Z = \frac{Y}{X}</equation>，故<equation>\frac{X}{Y} = \frac{1}{Z}</equation>.于是，<equation>E \left(\frac {X}{Y}\right) = E \left(\frac {1}{Z}\right) = \int_ {- \infty} ^ {+ \infty} \frac {1}{z} \cdot f _ {Z} (z) \mathrm {d} z = 2 \int_ {1} ^ {+ \infty} \frac {1}{z} \cdot \frac {1}{(z + 1) ^ {2}} \mathrm {d} z.</equation>设<equation>\frac{1}{z(z + 1)^2} = \frac{A}{z} +\frac{B}{z + 1} +\frac{C}{(z + 1)^2}</equation>，则<equation>\frac {1}{z (z + 1) ^ {2}} = \frac {A (z + 1) ^ {2} + B z (z + 1) + C z}{z (z + 1) ^ {2}} = \frac {(A + B) z ^ {2} + (2 A + B + C) z + A}{z (z + 1) ^ {2}}.</equation>比较系数可得<equation>\left\{ \begin{array}{l l} A+B=0, \\ 2 A+B+C=0, \\ A=1. \end{array} \right.</equation>解得<equation>\left\{ \begin{array}{l l} A=1, \\ B=-1, \\ C=-1. \end{array} \right.</equation>从而<equation>\frac{1}{z(z+1)^2}=\frac{1}{z}-\frac{1}{z+1}-\frac{1}{(z+1)^2}.</equation><equation>\begin{aligned} E \left(\frac {X}{Y}\right) &= 2 \int_ {1} ^ {+ \infty} \left[ \frac {1}{z} - \frac {1}{z + 1} - \frac {1}{(z + 1) ^ {2}} \right] \mathrm {d} z = 2 \left(\ln \frac {z}{z + 1} + \frac {1}{z + 1}\right) \Bigg | _ {1} ^ {+ \infty} \\ &= 2 \left(0 - \ln \frac {1}{2} - \frac {1}{2}\right) = 2 \ln 2 - 1. \end{aligned}</equation>

---

**2019年第14题 | 填空题 | 4分**
14. 设随机变量 X的概率密度为 f(x)<equation>\left\{\begin{array}{ll}\frac{x}{2},&0<x<2,\\0,&\text{其他},\end{array}\right.</equation>F(x)为 X的分布函数，E(X)为 X的数学期望，则<equation>P\{F(X)>E(X)-1\}=</equation>___
**解析: **解（法一）分别计算<equation>E ( X )</equation>，<equation>F ( x )</equation><equation>E (X) = \int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \int_ {0} ^ {2} \frac {x ^ {2}}{2} \mathrm {d} x = \left. \frac {x ^ {3}}{6} \right| _ {0} ^ {2} = \frac {4}{3}.</equation>当<equation>x < 0</equation>时，<equation>F ( x )=0.</equation>当<equation>0 \leqslant x < 2</equation>时，<equation>F(x) = \int_{-\infty}^{x} f(t)\mathrm{d}t = \int_{0}^{x}\frac{t}{2}\mathrm{d}t = \frac{x^2}{4}</equation>.

当<equation>x\geqslant 2</equation>时，<equation>F(x) = 1.</equation>于是，<equation>F ( x ) = \left\{ \begin{array}{ll} 0, & x < 0, \\ \frac{x^{2}}{4}, & 0 \leqslant x < 2, \\ 1, & x \geqslant 2. \end{array} \right.</equation>因此，<equation>\begin{array}{l} P \left\{F (X) > E (X) - 1 \right\} = P \left\{F (X) > \frac {1}{3} \right\} = P \left\{\frac {X ^ {2}}{4} > \frac {1}{3}, 0 \leqslant X < 2 \right\} + P \left\{X \geqslant 2 \right\} \\ = P \left\{\frac {2}{\sqrt {3}} < X < 2 \right\} + \int_ {2} ^ {+ \infty} f (x) \mathrm {d} x = 1 - \int_ {0} ^ {\frac {2}{\sqrt {3}}} \frac {x}{2} \mathrm {d} x + 0 \\ = 1 - \frac {x ^ {2}}{4} \Bigg | _ {0} ^ {\frac {2}{\sqrt {3}}} = \frac {2}{3}. \\ \end{array}</equation>（法二）我们先证明<equation>Y = F(X)</equation>服从（0，1）上的均匀分布.

注意到<equation>F ( x )</equation>在（0，2）上严格单调增加，其值域为（0，1），故可定义<equation>F^{-1}(y)</equation>，<equation>y\in(0,1).</equation>考虑Y的分布函数<equation>F_{Y}(y).</equation>当<equation>y < 0</equation>时，由于<equation>F(X)</equation>仅在<equation>[0,1]</equation>上取值，故<equation>F_{Y}(y) = 0.</equation>当<equation>0\leqslant y < 1</equation>时，<equation>F _ {Y} (y) = P \left\{Y \leqslant y \right\} = P \left\{F (X) \leqslant y \right\} = P \left\{X \leqslant F ^ {- 1} (y) \right\} = F \left(F ^ {- 1} (y)\right) = y.</equation>当<equation>y \geqslant 1</equation>时，<equation>P\{Y \leqslant y\} = 1</equation>，即<equation>F_{Y}(y) = 1.</equation>因此，<equation>F_{Y}(y) = \left\{ \begin{array}{ll}0, & y < 0,\\ y, & 0\leqslant y < 1,\\ 1, & y\geqslant 1. \end{array} \right.</equation>这说明<equation>Y = F(X)</equation>服从（0，1）上的均匀分布.

由法一可知<equation>E ( X )=\frac{4}{3}</equation>故<equation>P \left\{F (X) > E (X) - 1 \right\} = P \left\{F (X) > \frac {1}{3} \right\} = 1 - P \left\{F (X) \leqslant \frac {1}{3} \right\} = 1 - \frac {1}{3} = \frac {2}{3}.</equation>

---


#### 协方差与相关系数

**2024年第9题 | 选择题 | 5分 | 答案: D**
9. 设随机变量 X的概率密度为<equation>f ( x )=\left\{\begin{array}{ll}2(1-x),&0<x<1,\\ 0,&\text{其他}.\end{array}\right.</equation>在 X=x(0<x<1)的条件下，随机变量 Y服从区间 (x,1)上的均匀分布，则<equation>\operatorname{C o v} ( X, Y )=</equation>(    )

A.<equation>-\frac{1}{36}</equation>B.<equation>-\frac{1}{72}</equation>C.<equation>\frac{1}{72}</equation>D.<equation>\frac{1}{36}</equation>
答案: D
**解析: **解 由于在<equation>X=x(0<x<1)</equation>的条件下，随机变量Y服从区间（x，1）上的均匀分布，故<equation>f_{Y \mid X}(y \mid x)=\frac{1}{1-x}.</equation>记区域<equation>D=\{(x,y)\mid x<y<1,0<x<1\}</equation>，则在区域D上，<equation>(X,Y)</equation>的联合概率密度<equation>\varphi (x, y) = f _ {Y \mid X} (y \mid x) f (x) = \frac {1}{1 - x} \cdot 2 (1 - x) = 2.</equation>注意到区域 D是一个直角边长为1的等腰直角三角形区域，面积为<equation>\frac{1}{2}</equation>，故<equation>\iint_ {D} \varphi (x, y) \mathrm {d} x \mathrm {d} y = 2 \iint_ {D} \mathrm {d} x \mathrm {d} y = 1,</equation>从而可认为在<equation>D</equation>以外的区域上，<equation>\varphi (x,y) = 0.</equation>进一步可得，当<equation>0 < y < 1</equation>时，<equation>Y</equation>的边缘概率密度<equation>f _ {Y} (y) = \int_ {- \infty} ^ {+ \infty} \varphi (x, y) \mathrm {d} x = \int_ {0} ^ {y} 2 \mathrm {d} x = 2 y.</equation>当<equation>y \leqslant 0</equation>或<equation>y \geqslant 1</equation>时，<equation>f_{Y}(y) = \int_{-\infty}^{+\infty}\varphi(x,y)\mathrm{d}x = 0.</equation>由数学期望的定义可得，<equation>E (X) = \int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \int_ {0} ^ {1} x \cdot 2 (1 - x) \mathrm {d} x = \int_ {0} ^ {1} \left(2 x - 2 x ^ {2}\right) \mathrm {d} x = \left(x ^ {2} - \frac {2 x ^ {3}}{3}\right) \Bigg | _ {0} ^ {1} = \frac {1}{3},</equation><equation>E (Y) = \int_ {- \infty} ^ {+ \infty} y f _ {Y} (y) \mathrm {d} y = \int_ {0} ^ {1} y \cdot 2 y \mathrm {d} y = \left. \frac {2 y ^ {3}}{3} \right| _ {0} ^ {1} = \frac {2}{3},</equation><equation>\begin{aligned} E (X Y) &= \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} x y \varphi (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {D} 2 x y \mathrm {d} x \mathrm {d} y = 2 \int_ {0} ^ {1} y \mathrm {d} y \int_ {0} ^ {y} x \mathrm {d} x = 2 \int_ {0} ^ {1} y \cdot \frac {y ^ {2}}{2} \mathrm {d} y \\ &= \left. \frac {y ^ {4}}{4} \right| _ {0} ^ {1} = \frac {1}{4}. \end{aligned}</equation>因此，<equation>\operatorname {C o v} (X, Y) = E (X Y) - E (X) E (Y) = \frac {1}{4} - \frac {1}{3} \times \frac {2}{3} = \frac {1}{3 6}.</equation>应选 D.

---

**2023年第22题 | 解答题 | 12分**
. (本题满分12分)

设二维随机变量（X，Y）的概率密度为<equation>f ( x, y )=\left\{\begin{array}{ll}\frac{2}{\pi} \left(x^{2}+y^{2}\right),&x^{2}+y^{2}\leqslant 1\\ 0,&\text{其它}\end{array} \right.</equation>I. 求 X与 Y的斜方差；

II. 求 X与 Y是否相互独立；

III. 求<equation>Z=X^{2}+Y^{2}</equation>的概率密度.
**答案: **(I) Cov(X,Y) = 0;

（Ⅱ）X与Y不相互独立；

（Ⅲ）Z的概率密度<equation>f_{Z}(z)=\left\{ \begin{array}{ll} 2z, & 0<z<1, \\ 0, & \text{其他}. \end{array} \right.</equation>
**解析: **解（I）由<equation>f ( x,y )</equation>的定义可知，当<equation>| x | > 1</equation>时，<equation>f ( x,y ) = 0</equation>，当<equation>| x | \leqslant 1</equation>时，<equation>f ( x,y )</equation>仅在<equation>- \sqrt{1-x^{2}}\leqslant y\leqslant \sqrt{1-x^{2}}</equation>时非零.<equation>\begin{aligned} f _ {X} (x) &= \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} y = \frac {2}{\pi} \int_ {- \sqrt {1 - x ^ {2}}} ^ {\sqrt {1 - x ^ {2}}} \left(x ^ {2} + y ^ {2}\right) \mathrm {d} y = \frac {4}{\pi} \int_ {0} ^ {\sqrt {1 - x ^ {2}}} \left(x ^ {2} + y ^ {2}\right) \mathrm {d} y \\ &= \frac {4}{\pi} \left[ x ^ {2} \sqrt {1 - x ^ {2}} + \frac {\left(1 - x ^ {2}\right) ^ {\frac {3}{2}}}{3} \right] = \frac {4}{3 \pi} \sqrt {1 - x ^ {2}} \left(1 + 2 x ^ {2}\right), \end{aligned}</equation>即<equation>f_{X}(x) = \left\{ \begin{array}{ll}\frac{4}{3\pi}\sqrt{1 - x^{2}}(1 + 2x^{2}), & |x|\leqslant 1,\\ 0, & |x| > 1. \end{array} \right.</equation>同理可得<equation>f _ {Y} (y) = \left\{ \begin{array}{l l} \frac {4}{3 \pi} \sqrt {1 - y ^ {2}} \left(1 + 2 y ^ {2}\right), & | y | \leqslant 1, \\ 0, & | y | > 1. \end{array} \right.</equation>(a)

(b)

记<equation>D = \{(x,y)\mid x^{2} + y^{2}\leqslant 1\} .</equation>如图（a）所示，区域D关于x轴，y轴均对称.进一步计算可得<equation>E (X) = \int_ {- \infty} ^ {+ \infty} x f _ {X} (x) \mathrm {d} x = \int_ {- 1} ^ {1} \frac {4 x}{3 \pi} \sqrt {1 - x ^ {2}} \left(1 + 2 x ^ {2}\right) \mathrm {d} x \stackrel {\text {对称性}} {=} 0,</equation><equation>E (Y) \stackrel {\text {同 理}} {=} 0,</equation><equation>E (X Y) = \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} x y f (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {D} x y \cdot \frac {2}{\pi} \left(x ^ {2} + y ^ {2}\right) \mathrm {d} x \mathrm {d} y \stackrel {\text {对称 性}} {=} 0,</equation>从而<equation>\operatorname{Cov}(X, Y) = E(XY) - E(X)E(Y) = 0.</equation>（Ⅱ）由第（I）问可知，<equation>f_{X}(x)f_{Y}(y)\neq f(x,y)</equation>，故X与Y不相互独立.

（Ⅲ）记<equation>Z = X^{2} + Y^{2}</equation>的分布函数为<equation>F_{Z}(z), D_{z} = \{(x,y)|x^{2} + y^{2}\leqslant z\} .</equation>当<equation>z < 0</equation>时，<equation>F_{Z}(z) = P\{Z\leqslant z\} = 0.</equation>当<equation>0 \leqslant z < 1</equation>时，<equation>D \cap D_{z} = D_{z}</equation>，如图（b）所示.<equation>\begin{array}{l} F _ {Z} (z) = P \left\{Z \leqslant z \right\} = \iint_ {D _ {z}} \frac {2}{\pi} \left(x ^ {2} + y ^ {2}\right) \mathrm {d} x \mathrm {d} y = \frac {2}{\pi} \int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {0} ^ {\sqrt {z}} r ^ {2} \cdot r \mathrm {d} r \\ = \frac {2}{\pi} \cdot 2 \pi \cdot \frac {r ^ {4}}{4} \Bigg | _ {0} ^ {\sqrt {z}} = z ^ {2}. \\ \end{array}</equation>当<equation>z \geqslant 1</equation>时，<equation>F_{Z}(z) = P\{Z \leqslant z\} = 1.</equation>因此，<equation>Z</equation>的分布函数<equation>F_{Z}(z) = \left\{ \begin{array}{ll}0, & z < 0,\\ z^{2}, & 0\leqslant z < 1,\\ 1, & z\geqslant 1, \end{array} \right.</equation>概率密度<equation>f_{Z}(z) = F_{Z}^{\prime}(z) = \left\{ \begin{array}{ll}2z, & 0 < z < 1,\\ 0, & \text{其他}. \end{array} \right.</equation>

---

**2022年第8题 | 选择题 | 5分 | 答案: C**
8. 设随机变量 X服从区间（0,3）上的均匀分布，随机变量 Y服从参数为2的泊松分布，且 X与 Y的协方差为 -1，则<equation>D(2X-Y+1)=</equation>(    )

A.1 B.5 C.9 D.12
答案: C
**解析: **解 由于 X服从区间（0,3）上的均匀分布，故 X的方差<equation>D ( X )=\frac{(3-0)^{2}}{1 2}=\frac{3}{4}.</equation>又由于 Y服从参数为2的泊松分布，故 Y的方差<equation>D ( Y )=2.</equation>由方差的性质，<equation>\begin{aligned} D (2 X - Y + 1) &= D (2 X - Y) = D (2 X) + D (Y) - 2 \operatorname {C o v} (2 X, Y) \\ &= 4 D (X) + D (Y) - 4 \operatorname {C o v} (X, Y) = 4 \times \frac {3}{4} + 2 - 4 \times (- 1) = 9. \end{aligned}</equation>因此，应选C.

---

**2022年第10题 | 选择题 | 5分 | 答案: D**
10. 设随机变量<equation>X\sim N(0,1)</equation>，若在<equation>X=x</equation>的条件下，随机变量<equation>Y\sim N(x,1)</equation>，则 X与Y的相关系数为（    ）

A.<equation>\frac{1}{4}</equation>B.<equation>\frac{1}{2}</equation>C.<equation>\frac{\sqrt{3}}{3}</equation>D.<equation>\frac{\sqrt{2}}{2}</equation>
答案: D
**解析: **解（法一）由于<equation>X\sim N(0,1)</equation>，故<equation>X</equation>的概率密度函数为<equation>f _ {X} (x) = \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {x ^ {2}}{2}}.</equation>由于在<equation>X = x</equation>的条件下，<equation>Y\sim N(x,1)</equation>，故在<equation>X = x</equation>的条件下，<equation>Y</equation>的条件概率密度为<equation>f _ {Y \mid X} (y \mid x) = \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {(y - x) ^ {2}}{2}}.</equation>于是，二维随机变量<equation>(X, Y)</equation>的联合概率密度为<equation>f (x, y) = f _ {X} (x) f _ {Y \mid X} (y \mid x) = \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \cdot \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {(y - x) ^ {2}}{2}} = \frac {1}{2 \pi} \mathrm {e} ^ {- x ^ {2} + x y - \frac {y ^ {2}}{2}}.</equation>计算<equation>Y</equation>的边缘概率密度<equation>f_{Y}(y)</equation>. 对<equation>y \in (-\infty, +\infty)</equation>，<equation>\begin{aligned} f _ {Y} (y) &= \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} x = \int_ {- \infty} ^ {+ \infty} \frac {1}{2 \pi} \mathrm {e} ^ {- x ^ {2} + x y - \frac {y ^ {2}}{2}} \mathrm {d} x = \frac {1}{2 \sqrt {\pi}} \mathrm {e} ^ {- \frac {y ^ {2}}{4}} \int_ {- \infty} ^ {+ \infty} \frac {1}{\sqrt {2 \pi} \cdot \frac {\sqrt {2}}{2}} \mathrm {e} ^ {- (x - \frac {y}{2}) ^ {2}} \mathrm {d} x \\ &= \frac {1}{2 \sqrt {\pi}} \mathrm {e} ^ {- \frac {y ^ {2}}{4}} = \frac {1}{\sqrt {2 \pi} \cdot \sqrt {2}} \mathrm {e} ^ {- \frac {y ^ {2}}{2 (\sqrt {2}) ^ {2}}}. \end{aligned}</equation>于是，<equation>(X,Y)</equation>关于<equation>Y</equation>的边缘分布是正态分布<equation>N(0,2)</equation>.

结合<equation>f(x,y)</equation>与二维正态分布的概率密度的形式，取<equation>\mu_{1} = 0,\mu_{2} = 0,\sigma_{1} = 1,\sigma_{2} = \sqrt{2}</equation><equation>\frac {1}{2 \pi} \mathrm {e} ^ {- x ^ {2} + x y - \frac {y ^ {2}}{2}} = \frac {1}{2 \pi \cdot 1 \cdot \sqrt {2} \cdot \frac {\sqrt {2}}{2}} \cdot \mathrm {e} ^ {- \frac {1}{2} \cdot \frac {1}{2}} \left[ \frac {(x - 0) ^ {2}}{1 ^ {2}} - 2 \cdot \frac {\sqrt {2}}{2} \frac {(x - 0) (y - 0)}{1 \cdot \sqrt {2}} + \frac {(y - 0) ^ {2}}{(\sqrt {2}) ^ {2}} \right].</equation>因此，取<equation>\rho = \frac{\sqrt{2}}{2}</equation>，则<equation>(X,Y)</equation>服从二维正态分布<equation>N\left(0,0;1,2;\frac{\sqrt{2}}{2}\right)</equation>.

由二维正态分布的概率密度的参数的含义可知，<equation>\rho_{X Y}=\frac{\sqrt{2}}{2}</equation>，应选D.

（法二）计算<equation>\rho_{X Y}.</equation>先计算 E(XY).

由法一可得<equation>f(x,y) = \frac{1}{2\pi}\mathrm{e}^{-x^2 + xy - \frac{y^2}{2}}.</equation>于是，<equation>\begin{aligned} E (X Y) &= \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} x y f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {- \infty} ^ {+ \infty} x \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \mathrm {d} x \int_ {- \infty} ^ {+ \infty} y \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {(y - x) ^ {2}}{2}} \mathrm {d} y \\ &= \int_ {- \infty} ^ {+ \infty} x \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \mathrm {d} x \left[ \int_ {- \infty} ^ {+ \infty} \frac {1}{\sqrt {2 \pi}} (y - x) \mathrm {e} ^ {- \frac {(y - x) ^ {2}}{2}} \mathrm {d} y + x \int_ {- \infty} ^ {+ \infty} \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {(y - x) ^ {2}}{2}} \mathrm {d} (y - x) \right] \\ &= \int_ {- \infty} ^ {+ \infty} x \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {x ^ {2}}{2}} (0 + x) \mathrm {d} x = \int_ {- \infty} ^ {+ \infty} x ^ {2} \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \mathrm {d} x. \end{aligned}</equation>又因为<equation>\int_{-\infty}^{+\infty}x^{2}\frac{1}{\sqrt{2\pi}}\mathrm{e}^{-\frac{x^{2}}{2}}\mathrm{d}x = E(X^{2})</equation>，而<equation>X\sim N(0,1)</equation>，所以<equation>E(X^{2}) = D(X) + [E(X)]^{2} = 1.</equation>从而，<equation>E(XY) = 1.</equation>又由法一可得<equation>Y\sim N(0,2)</equation>，故<equation>E(Y)=0,D(Y)=2.</equation>因此，<equation>\rho_ {X Y} = \frac {\operatorname {C o v} (X , Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {1 - 0}{\sqrt {2}} = \frac {\sqrt {2}}{2}.</equation>

---

**2021年第16题 | 填空题 | 5分**
16. 甲、乙两个盒子中各装有2个红球和2个白球，先从甲盒中任取一球，观察颜色后放入乙盒中，再从乙盒中任取一球，令 X, Y分别表示从甲盒和乙盒中取到的红球个数，则 X与 Y的相关系数为 ___.
**答案: **# 1 5.
**解析: **根据相关系数的计算公式，X与Y的相关系数为<equation>\rho = \frac {\operatorname {C o v} (X , Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}}.</equation>下面分别计算<equation>X, Y</equation>的分布律与数字特征.

取球模型为等可能模型.<equation>X</equation>的可能取值为0，1. 取到白球，则<equation>X = 0</equation>；取到红球，则<equation>X = 1</equation><equation>P \{X = 0 \} = \frac {1}{2}, \quad P \{X = 1 \} = \frac {1}{2}.</equation>于是，<equation>E ( X ) = \frac {1}{2}, E \left( X^{2}\right) = \frac {1}{2}, D ( X ) = \frac {1}{2} - \left(\frac {1}{2}\right)^{2} = \frac {1}{4}.</equation>Y的可能取值为0，1.若从甲盒中取出的是白球，则后来乙盒中共有2个红球和3个白球，取到红球的概率为<equation>\frac{2}{5}</equation>即在X=0发生的条件下Y=1发生的概率为<equation>\frac{2}{5}</equation>；若从甲盒中取出的是红球，则后来乙盒中共有3个红球和2个白球，取到红球的概率为<equation>\frac{3}{5}</equation>即在X=1发生的条件下Y=1发生的概率为<equation>\frac{3}{5}.</equation><equation>\begin{aligned} P \{Y = 1 \} &= P \{Y = 1 \mid X = 0 \} P \{X = 0 \} + P \{Y = 1 \mid X = 1 \} P \{X = 1 \} \\ &= \frac {2}{5} \times \frac {1}{2} + \frac {3}{5} \times \frac {1}{2} = \frac {1}{2}. \end{aligned}</equation><equation>P \{Y = 0 \} = 1 - P \{Y = 1 \} = 1 - \frac {1}{2} = \frac {1}{2}.</equation>于是，<equation>E ( Y ) = \frac {1}{2}, E ( Y^{2} ) = \frac {1}{2}, D ( Y ) = \frac {1}{2} - \left(\frac {1}{2}\right)^{2} = \frac {1}{4}.</equation>XY的可能取值为0,1.<equation>P \{X Y = 1 \} = P \{X = 1, Y = 1 \} = P \{Y = 1 \mid X = 1 \} P \{X = 1 \} = \frac {3}{5} \times \frac {1}{2} = \frac {3}{1 0}.</equation><equation>P \left\{X Y = 0 \right\} = 1 - \frac {3}{1 0} = \frac {7}{1 0}.</equation>于是，<equation>E ( X Y ) = P \{ X Y = 1 \} \times 1 + P \{ X Y = 0 \} \times 0 = \frac {3}{1 0}.</equation>因此，<equation>\rho = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {\frac {3}{1 0} - \frac {1}{2} \times \frac {1}{2}}{\frac {1}{2} \times \frac {1}{2}} = \frac {\frac {1}{2 0}}{\frac {1}{4}} = \frac {1}{5}.</equation>

---

**2020年第14题 | 填空题 | 4分**
14. 设 X 服从区间<equation>\left(-\frac{\pi}{2},\frac{\pi}{2}\right)</equation>上的均匀分布，<equation>Y=\sin X</equation>，则<equation>\operatorname{Cov}(X,Y)=</equation>___
**答案: **# 2 π.
**解析: **解 由 X服从<equation>\left(-\frac{\pi}{2},\frac{\pi}{2}\right)</equation>上的均匀分布可知，<equation>f(x)=\left\{\begin{array}{ll}\frac{1}{\pi},&x\in\left(-\frac{\pi}{2},\frac{\pi}{2}\right),\\ 0,&\text{其他}.\end{array}\right.</equation><equation>E (X) = \int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \frac {1}{\pi} \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} x \mathrm {d} x = 0.</equation>根据协方差的计算公式，<equation>\begin{aligned} \operatorname {C o v} (X, Y) &= \operatorname {C o v} (X, \sin X) = E (X \sin X) - E (X) E (\sin X) \xlongequal {E (X) = 0} \int_ {- \infty} ^ {+ \infty} x \sin x f (x) \mathrm {d} x - 0 \\ &= \frac {1}{\pi} \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} x \sin x \mathrm {d} x \xlongequal {\text {对称性}} \frac {2}{\pi} \int_ {0} ^ {\frac {\pi}{2}} x \sin x \mathrm {d} x = - \frac {2}{\pi} \int_ {0} ^ {\frac {\pi}{2}} x \mathrm {d} (\cos x) \\ &= - \frac {2}{\pi} \left(x \cos x \Big | _ {0} ^ {\frac {\pi}{2}} - \int_ {0} ^ {\frac {\pi}{2}} \cos x \mathrm {d} x\right) = - \frac {2}{\pi} \times (0 - 1) = \frac {2}{\pi}. \end{aligned}</equation>

---

**2018年第22题 | 解答题 | 11分**
22. (本题满分11分)

设随机变量 X与 Y相互独立，X的概率分布为<equation>P\{X=1\}=P\{X=-1\}=\frac{1}{2},</equation>Y服从参数为<equation>\lambda</equation>的泊松分布.令<equation>Z=XY.</equation>I. 求<equation>\operatorname{Cov}(X,Z)</equation>;

II. 求 Z的概率分布.
**答案: **（ I ）<equation>\operatorname{C o v} ( X, Z ) = \lambda</equation>（Ⅱ）Z的分布律为<equation>P\{Z = i\} = \left\{ \begin{array}{ll}\frac{1}{2}\cdot \frac{\lambda^{i}\mathrm{e}^{-\lambda}}{i!}, & i > 0,\\ \mathrm{e}^{-\lambda}, & i = 0,\\ \frac{1}{2}\cdot \frac{\lambda^{-i}\mathrm{e}^{-\lambda}}{(-i)!}, & i < 0. \end{array} \right.</equation>
**解析: **解（I）（法一）注意到<equation>X</equation>与Y相互独立，故<equation>X^{2}</equation>与Y也相互独立.

根据协方差的计算公式，<equation>\begin{aligned} \operatorname {C o v} (X, Z) &= E (X Z) - E (X) E (Z) \stackrel {Z = X Y} {=} E \left(X ^ {2} Y\right) - E (X) E (X Y) \\ \stackrel {\text {独立 性}} {=} E \left(X ^ {2}\right) E (Y) - \left[ E (X) \right] ^ {2} E (Y). \end{aligned}</equation>由于 X的概率分布为<equation>P \{ X=1 \} = P \{ X=-1 \} = \frac{1}{2}</equation>，故<equation>E (X) = 1 \times \frac {1}{2} + (- 1) \times \frac {1}{2} = 0, \quad E \left(X ^ {2}\right) = 1 ^ {2} \times \frac {1}{2} + (- 1) ^ {2} \times \frac {1}{2} = 1.</equation>又因为<equation>Y</equation>服从参数为<equation>\lambda</equation>的泊松分布，所以<equation>E(Y) = \lambda</equation>因此，<equation>\operatorname {C o v} (X, Z) = E \left(X ^ {2}\right) E (Y) - \left[ E (X) \right] ^ {2} E (Y) = 1 \times \lambda - 0 = \lambda .</equation>（法二）由于<equation>X^{2}=1</equation>，故<equation>XZ=X(XY)=X^{2}Y=Y</equation>，而Y服从参数为<equation>\lambda</equation>的泊松分布，于是，<equation>E(XZ)=E(Y)=\lambda.</equation>由法一可知，<equation>E ( X ) = 0</equation>因此，<equation>\operatorname {C o v} (X, Z) = E (X Z) - E (X) E (Z) = \lambda - 0 = \lambda .</equation>（Ⅱ）由于<equation>Z = XY</equation>，故<equation>Z</equation>的所有可能的取值为<equation>i</equation>，其中<equation>i</equation>为整数.

当 i > 0时，<equation>\begin{aligned} P \{Z = i \} &= P \{X Y = i \} = P \{X = 1, Y = i \} \xlongequal {\text {独立 性}} P \{X = 1 \} P \{Y = i \} \\ &= \frac {1}{2} \cdot \frac {\lambda^ {i} \mathrm {e} ^ {- \lambda}}{i !}. \end{aligned}</equation>当 i = 0时，<equation>P \{Z = 0 \} = P \{X Y = 0 \} \xlongequal {X \text {不 为} 0} P \{Y = 0 \} = \mathrm {e} ^ {- \lambda}.</equation>当 i < 0时，<equation>\begin{aligned} P \{Z = i \} &= P \{X Y = i \} = P \{X = - 1, Y = - i \} \xlongequal {\text {独立性}} P \{X = - 1 \} P \{Y = - i \} \\ &= \frac {1}{2} \cdot \frac {\lambda^ {- i} \mathrm {e} ^ {- \lambda}}{(- i) !}. \end{aligned}</equation>因此，Z的分布律为<equation>P\{Z = i\} = \left\{ \begin{array}{ll}\frac{1}{2}\cdot \frac{\lambda^{i}\mathrm{e}^{-\lambda}}{i!}, & i > 0,\\ \mathrm{e}^{-\lambda}, & i = 0,\\ \frac{1}{2}\cdot \frac{\lambda^{-i}\mathrm{e}^{-\lambda}}{(-i)!}, & i < 0. \end{array} \right.</equation>

---

**2016年第8题 | 选择题 | 4分 | 答案: A**
8. 随机试验 E有三种两两不相容的结果<equation>A_{1}, A_{2}, A_{3}</equation>，且三种结果发生的概率均为<equation>\frac{1}{3}</equation>，将试验 E独立重复做2次， X表示2次试验中结果<equation>A_{1}</equation>发生的次数，Y表示2次试验中结果<equation>A_{2}</equation>发生的次数，则 X与 Y的相关系数为（    )

A.<equation>-\frac{1}{2}</equation>B.<equation>-\frac{1}{3}</equation>C.<equation>\frac{1}{3}</equation>D.<equation>\frac{1}{2}</equation>
答案: A
**解析: **解（法一）由题设知，<equation>X\sim B\left(2,\frac{1}{3}\right),Y\sim B\left(2,\frac{1}{3}\right)</equation>，从而<equation>E (X) = E (Y) = 2 \times \frac {1}{3} = \frac {2}{3}, \quad D (X) = D (Y) = 2 \times \frac {1}{3} \times \left(1 - \frac {1}{3}\right) = \frac {4}{9}.</equation>又 XY所有可能的取值为0，1，故<equation>E ( X Y ) = 0 \cdot P \{ X Y = 0 \} + 1 \cdot P \{ X Y = 1 \} = P \{ X = 1, Y = 1 \} = \mathrm {C} _ {2} ^ {1} \times \frac {1}{3} \times \frac {1}{3} = \frac {2}{9},</equation>从而<equation>\rho_{X Y}=\frac{E(X Y)-E(X)E(Y)}{\sqrt{D(X)}\sqrt{D(Y)}}=\frac{\frac{2}{9}-\frac{2}{3}\times \frac{2}{3}}{\frac{4}{9}}=-\frac{1}{2}.</equation>应选A.

（法二）记Z表示2次试验中结果<equation>A_{3}</equation>发生的次数，则<equation>X+Y+Z=2</equation>从而<equation>D (Z) = D (2 - X - Y) = D (X + Y) = D (X) + D (Y) + 2 \operatorname {C o v} (X, Y).</equation>又由题设知，<equation>D ( X )=D ( Y )=D ( Z )</equation>，故<equation>D ( X )=-2\operatorname{C o v} ( X , Y )</equation>，从而<equation>\rho_ {X Y} = \frac {\operatorname {C o v} (X , Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {\operatorname {C o v} (X , Y)}{D (X)} = - \frac {1}{2}.</equation>应选A.

---

**2015年第8题 | 选择题 | 4分 | 答案: D**
8. 设随机变量 X,Y不相关，且<equation>E ( X )=2, E ( Y )=1, D ( X )=3</equation>，则<equation>E [ X ( X+Y-2) ]=</equation>(    )

A. -3 B. 3 C. -5 D. 5
答案: D
**解析: **解 由题设知，<equation>\rho_{XY}=\frac{\operatorname{Cov}(X,Y)}{\sqrt{D(X)}\sqrt{D(Y)}}=\frac{E(XY)-E(X)E(Y)}{\sqrt{D(X)}\sqrt{D(Y)}}=0</equation>，从而<equation>E(XY)=E(X)E(Y)</equation>于是<equation>\begin{aligned} E [ X (X + Y - 2) ] &= E \left(X ^ {2}\right) + E (X Y) - 2 E (X) \\ &= D (X) + \left[ E (X) \right] ^ {2} + E (X) E (Y) - 2 E (X) \\ &= 3 + 4 + 2 - 4 = 5. \end{aligned}</equation>应选 D.

---

**2012年第8题 | 选择题 | 4分 | 答案: D**
8. 将长度为1m的木棒随机地截成两段，则两段长度的相关系数为（    ）

A. 1 B.<equation>\frac{1}{2}</equation>C.<equation>-\frac{1}{2}</equation>D. -1
答案: D
**解析: **解（法一）设木棒被截成两段的长度分别为 X，Y，则有 X+Y=1，即 Y=1-X.于是<equation>D(Y)=D(1-X)=D(X),</equation><equation>\operatorname{Cov}(X,Y)=\operatorname{Cov}(X,1-X)=-\operatorname{Cov}(X,X)=-D(X),</equation>从而<equation>\rho_ {X Y} = \frac {\operatorname {C o v} (X , Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {- D (X)}{\sqrt {D (X)} \sqrt {D (X)}} = - 1.</equation>应选 D.

（法二）由于<equation>|\rho_{XY}|=1</equation>的充要条件是存在常数 a,b，使得<equation>P\{Y=a+bX\}=1</equation>，且此时<equation>\rho_{XY}=\frac{b}{|b|}</equation>由于 Y=1-X，故<equation>\rho_{XY}=-1</equation>从而选D.

---

**2012年第22题 | 解答题 | 11分**

设二维离散型随机变量<equation>(X, Y)</equation>的概率分布为

<table border="1"><tr><td>X\ Y</td><td>0</td><td>1</td><td>2</td></tr><tr><td>0</td><td>1/4</td><td>0</td><td>1/4</td></tr><tr><td>1</td><td>0</td><td>1/3</td><td>0</td></tr><tr><td>2</td><td>1/12</td><td>0</td><td>1/12</td></tr></table>

I. 求<equation>P\{X = 2Y\}</equation>;

II. 求<equation>\operatorname{Cov}(X - Y, Y)</equation>.
**答案: **(22) （ I )<equation>P \{ X=2 Y \}=\frac{1}{4}</equation>；

（Ⅱ）<equation>\operatorname{C o v} ( X-Y, Y)=-\frac{2}{3}.</equation>
**解析: **（ I ）由题设知，<equation>P \{X = 2 Y \} = P \{X = 0, Y = 0 \} + P \{X = 2, Y = 1 \} = \frac {1}{4} + 0 = \frac {1}{4}.</equation>（Ⅱ）由<equation>(X,Y)</equation>的概率分布知，<equation>X,Y</equation>的概率分布分别为

<table border="1"><tr><td>X</td><td>0</td><td>1</td><td>2</td></tr><tr><td>P</td><td><equation>\frac{1}{2}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{6}</equation></td></tr></table>

<table border="1"><tr><td>Y</td><td>0</td><td>1</td><td>2</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td></tr></table>

又由于随机变量 XY可能的值为0，1，2，4，故XY的概率分布为<equation>\begin{aligned} P \{X Y = 0 \} &= P \{X = 0, Y = 0 \} + P \{X = 0, Y = 1 \} + P \{X = 0, Y = 2 \} \\ + P \{X = 1, Y = 0 \} + P \{X = 2, Y = 0 \} \\ &= \frac {1}{4} + 0 + \frac {1}{4} + 0 + \frac {1}{1 2} = \frac {7}{1 2}, \end{aligned}</equation><equation>P \left\{X Y = 1 \right\} = P \left\{X = 1, Y = 1 \right\} = \frac {1}{3},</equation><equation>P \left\{X Y = 2 \right\} = P \left\{X = 1, Y = 2 \right\} + P \left\{X = 2, Y = 1 \right\} = 0 + 0 = 0,</equation><equation>P \{X Y = 4 \} = P \{X = 2, Y = 2 \} = \frac {1}{1 2},</equation>即

<table border="1"><tr><td>XY</td><td>0</td><td>1</td><td>4</td></tr><tr><td>P</td><td><equation>\frac{7}{12}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{12}</equation></td></tr></table>

于是，<equation>E (X) = 0 \times \frac {1}{2} + 1 \times \frac {1}{3} + 2 \times \frac {1}{6} = \frac {2}{3},</equation><equation>E (Y) = 0 \times \frac {1}{3} + 1 \times \frac {1}{3} + 2 \times \frac {1}{3} = 1,</equation><equation>E \left(Y ^ {2}\right) = 0 ^ {2} \times \frac {1}{3} + 1 ^ {2} \times \frac {1}{3} + 2 ^ {2} \times \frac {1}{3} = \frac {5}{3},</equation><equation>E (X Y) = 0 \times \frac {7}{1 2} + 1 \times \frac {1}{3} + 4 \times \frac {1}{1 2} = \frac {2}{3}.</equation>因此，<equation>\begin{aligned} \operatorname {C o v} (X - Y, Y) &= \operatorname {C o v} (X, Y) - \operatorname {C o v} (Y, Y) = \left[ E (X Y) - E (X) E (Y) \right] - \left[ E \left(Y ^ {2}\right) - \left[ E (Y) \right] ^ {2} \right] \\ &= \left(\frac {2}{3} - \frac {2}{3} \times 1\right) - \left(\frac {5}{3} - 1 ^ {2}\right) = - \frac {2}{3}. \end{aligned}</equation>

---

**2011年第14题 | 填空题 | 4分**
14. 设二维随机变量<equation>(X, Y)</equation>服从正态分布<equation>N\left(\mu, \mu; \sigma^2, \sigma^2; 0\right)</equation>, 则<equation>E(XY^2) =</equation>___
**答案: **##<equation>\mu\sigma^{2}+\mu^{3}.</equation>
**解析: **解由（X，Y）服从正态分布<equation>N(\mu ,\mu ;\sigma^{2},\sigma^{2};0)</equation>知，<equation>X\sim N(\mu ,\sigma^{2}),Y\sim N(\mu ,\sigma^{2})</equation>且<equation>\rho_{XY}=0.</equation>由于对二维正态随机变量，不相关与相互独立等价，故X与Y相互独立，从而X与<equation>Y^{2}</equation>相互独立.于是<equation>E(XY^{2})=E(X)E(Y^{2})=E(X)[D(Y)+[E(Y)]^{2}]</equation><equation>=\mu(\sigma^{2}+\mu^{2})=\mu\sigma^{2}+\mu^{3}.</equation>

---

**2011年第22题 | 解答题 | 11分**

设随机变量<equation>X</equation>与<equation>Y</equation>的概率分布分别为

<table border="1"><tr><td>X</td><td>0</td><td>1</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{2}{3}</equation></td></tr></table>

<table border="1"><tr><td>Y</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td></tr></table>

且<equation>P \left\{X^{2}=Y^{2}\right\}=1.</equation>I. 求二维随机变量（X,Y）的概率分布；

II. 求<equation>Z=XY</equation>的概率分布；

III. 求 X与Y的相关系数<equation>\rho_{XY}</equation>.
**答案: **(22) （I）

<table border="1"><tr><td rowspan="2">X\ Y</td><td colspan="3">-1</td></tr><tr><td>0</td><td>1/3</td><td>0</td></tr><tr><td>1</td><td>1/3</td><td>0</td><td>1/3</td></tr><tr><td>Z</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>P</td><td>1/3</td><td>1/3</td><td>1/3</td></tr></table>

(Ⅱ)

( III ) 0.
**解析: **（I）由<equation>P\{X^{2} = Y^{2}\} = 1</equation>知，<equation>P\{X^{2}\neq Y^{2}\} = 0.</equation>于是，<equation>P \{X = 0, Y = - 1 \} = P \{X = 0, Y = 1 \} = P \{X = 1, Y = 0 \} = 0.</equation>从而<equation>P \{X = 0, Y = 0 \} = P \{Y = 0 \} - P \{X = 1, Y = 0 \} = \frac {1}{3} - 0 = \frac {1}{3},</equation><equation>P \{X = 1, Y = 1 \} = P \{Y = 1 \} - P \{X = 0, Y = 1 \} = \frac {1}{3} - 0 = \frac {1}{3},</equation><equation>P \{X = 1, Y = - 1 \} = P \{Y = - 1 \} - P \{X = 0, Y = - 1 \} = \frac {1}{3} - 0 = \frac {1}{3}.</equation>因此，<equation>( X, Y )</equation>的概率分布为

<table border="1"><tr><td>X\ Y</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>0</td><td><equation>\frac{1}{3}</equation></td><td>0</td></tr><tr><td>1</td><td><equation>\frac{1}{3}</equation></td><td>0</td><td><equation>\frac{1}{3}</equation></td></tr></table>

（Ⅱ）由于<equation>Z=XY</equation>可能的取值为-1，0，1，且<equation>P \{Z = - 1 \} = P \{X = 1, Y = - 1 \} = \frac {1}{3},</equation><equation>P \{Z = 1 \} = P \{X = 1, Y = 1 \} = \frac {1}{3},</equation><equation>P \{Z = 0 \} = 1 - P \{Z = - 1 \} - P \{Z = 1 \} = \frac {1}{3},</equation>故 Z = XY的概率分布为

<table border="1"><tr><td>Z</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td></tr></table>

（Ⅲ）由于<equation>E (X) = 0 \times \frac {1}{3} + 1 \times \frac {2}{3} = \frac {2}{3}, \quad E \left(X ^ {2}\right) = 0 ^ {2} \times \frac {1}{3} + 1 ^ {2} \times \frac {2}{3} = \frac {2}{3},</equation><equation>D (X) = E \left(X ^ {2}\right) - \left[ E (X) \right] ^ {2} = \frac {2}{9},</equation><equation>E (Y) = (- 1) \times \frac {1}{3} + 0 \times \frac {1}{3} + 1 \times \frac {1}{3} = 0, \quad E \left(Y ^ {2}\right) = (- 1) ^ {2} \times \frac {1}{3} + 0 ^ {2} \times \frac {1}{3} + 1 ^ {2} \times \frac {1}{3} = \frac {2}{3},</equation><equation>D (Y) = E \left(Y ^ {2}\right) - \left[ E (Y) \right] ^ {2} = \frac {2}{3},</equation><equation>E (X Y) = E (Z) = (- 1) \times \frac {1}{3} + 0 \times \frac {1}{3} + 1 \times \frac {1}{3} = 0,</equation>故<equation>\rho_ {X Y} = \frac {\operatorname {C o v} (X , Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = 0.</equation>

---


### 随机变量及其分布
### 参数估计与假设检验
#### 假设检验

**2025年第10题 | 选择题 | 5分 | 答案: D**

10. 设<equation>X_{1}, X_{2}, \cdots, X_{n}</equation>为来自正态总体<equation>N (\mu ,2)</equation>的简单随机样本，记<equation>\bar{X}=\frac{1}{n}\sum_{i=1}^{n} X_{i}, Z_{\alpha}</equation>表示标准正态分布的上侧<equation>\alpha</equation>分位数，假设检验问题：<equation>H_{0}:\mu \leqslant 1, H_{1}:\mu >1</equation>的显著性水平为<equation>\alpha</equation>的检验的拒绝域为（    )

A.<equation>\left\{(X_{1},X_{2},\cdots,X_{n})\mid \bar{X}>1+\frac{2}{n}Z_{\alpha}\right\}</equation>B.<equation>\left\{(X_{1},X_{2},\cdots,X_{n})\mid \bar{X}>1+\frac{\sqrt{2}}{n}Z_{\alpha}\right\}</equation>C.<equation>\left\{(X_{1},X_{2},\cdots,X_{n})\mid \bar{X}>1+\frac{2}{\sqrt{n}}Z_{\alpha}\right\}</equation>D.<equation>\left\{(X_{1},X_{2},\cdots,X_{n})\mid \bar{X}>1+\sqrt{\frac{2}{n}}Z_{\alpha}\right\}</equation>

答案: D

**解析:**解 由已知条件可知，总体方差<equation>\sigma^{2}=2.</equation>根据分析，方差为2的单个正态总体对均值<equation>\mu</equation>的假设检验问题：<equation>H_{0}:\mu\leqslant1,H_{1}:\mu>1</equation>的显著性水平为<equation>\alpha</equation>的检验的拒绝域为<equation>\overline{x}>1+\sqrt{\frac{2}{n}}z_{\alpha}</equation>其中<equation>z_{\alpha}</equation>为标准正态分布的上侧<equation>\alpha</equation>分位数.

因此，应选D.

---

**2021年第10题 | 选择题 | 5分 | 答案: B**

10. 设<equation>X_{1}, X_{2}, \cdots , X_{1 6}</equation>是来自总体<equation>N (\mu , 4)</equation>的简单随机样本，考虑假设检验问题：<equation>H_{0}:\mu \leqslant 1 0, H_{1}:\mu > 1 0, \Phi (x)</equation>表示标准正态分布函数，若该检验问题的拒绝域为<equation>W=\{\bar{X}>1 1 \}</equation>，其中<equation>\bar{X}=\frac{1}{1 6} \sum_{i=1}^{1 6} X_{i}</equation>，则<equation>\mu =1 1. 5</equation>时，该检验犯第二类错误的概率为（    ）

A. 1-<equation>\Phi (0. 5)</equation>B. 1-<equation>\Phi (1)</equation>C. 1-<equation>\Phi (1. 5)</equation>D. 1-<equation>\Phi (2)</equation>

答案: B

**解析:**解 根据已知条件，<equation>\mu=1 1. 5</equation>，原假设<equation>H_{0}:\mu\leqslant1 0</equation>不为真.由于该检验问题的拒绝域为<equation>W=\left\{\overline{X}>11\right\}</equation>，故当<equation>\overline{X}\leqslant1 1</equation>时，不拒绝<equation>H_{0}</equation>.此时，该检验犯了第二类错误，其概率为<equation>P\{\overline{X}\leqslant11\}</equation>下面我们计算<equation>P\{\overline{X}\leqslant11\}</equation>由已知条件可得<equation>n=1 6</equation>，故<equation>\overline{X}\sim N\left(\mu ,\frac{4}{1 6}\right)</equation>，即<equation>\overline{X}\sim N\left(1 1. 5 , \frac{1}{4}\right)</equation>.标准化可得，<equation>\frac{\overline{X}-1 1. 5}{\frac{1}{2}}\sim N(0,1).</equation><equation>P\{\overline{X}\leqslant11\}=P\left\{\frac{\overline{X}-1 1. 5}{\frac{1}{2}}\leqslant\frac{1 1-1 1. 5}{\frac{1}{2}}\right\}=\Phi(-1)=1-\Phi(1).</equation>因此，应选B.

---

**2018年第8题 | 选择题 | 4分 | 答案: D**

8. 设总体 X服从正态分布<equation>N\left(\mu ,\sigma^{2}\right).</equation><equation>X_{1},X_{2},\cdots,X_{n}</equation>是来自总体 X的简单随机样本，据此样本检验假设：<equation>H_{0}:\mu=\mu_{0},H_{1}:\mu\neq\mu_{0}</equation>，则（    )

A. 如果在检验水平<equation>\alpha=0. 0 5</equation>下拒绝<equation>H_{0}</equation>，那么<equation>\alpha=0. 0 1</equation>下必拒绝<equation>H_{0}</equation>B. 如果在检验水平<equation>\alpha=0. 0 5</equation>下拒绝<equation>H_{0}</equation>，那么<equation>\alpha=0. 0 1</equation>下必接受<equation>H_{0}</equation>C. 如果在检验水平<equation>\alpha=0. 0 5</equation>下接受<equation>H_{0}</equation>，那么<equation>\alpha=0. 0 1</equation>下必拒绝<equation>H_{0}</equation>D. 如果在检验水平<equation>\alpha=0. 0 5</equation>下接受<equation>H_{0}</equation>，那么<equation>\alpha=0. 0 1</equation>下必接受<equation>H_{0}</equation>

答案: D

**解析:**解 由于<equation>\sigma^2</equation>未知，故应采用<equation>t</equation>检验法，检验统计量可取为<equation>Z = \frac{\bar{X} - \mu_0}{S / \sqrt{n}}</equation>（注：<equation>S^{2}</equation>为样本方差，为方差<equation>\sigma^2</equation>的无偏估计量）.<equation>\bar{X} = \frac{1}{n}\sum_{i = 1}^{n}X_{i},\bar{X}\sim N\left(\mu ,\frac{\sigma^{2}}{n}\right)</equation>，故当假设<equation>H_{0}</equation>为真时，<equation>Z\sim t(n - 1)</equation>.

当<equation>\alpha = 0.05</equation>时，拒绝域为<equation>\left|\frac{\bar{x} - \mu_0}{S / \sqrt{n}}\right| > t_{\frac{\alpha}{2}} = t_{0.025}</equation>，其中<equation>t_{0.025}</equation>为上0.025分位点.<equation>\alpha = 0.05</equation>对应的接受域为<equation>\left(\mu_0 - t_{0.025}\frac{S}{\sqrt{n}},\mu_0 + t_{0.025}\frac{S}{\sqrt{n}}\right)</equation>.

当<equation>\alpha=0.01</equation>时，拒绝域为<equation>\left| \frac{\overline{{x}}-\mu_{0}}{S / \sqrt{n}} \right| > t_{\frac{\alpha}{2}}=t_{0.005}</equation>，其中<equation>t_{0.005}</equation>为上0.005分位点.<equation>\alpha=0.01</equation>对应的接受域为<equation>\left(\mu_{0}-t_{0.005}\frac{S}{\sqrt{n}},\mu_{0}+t_{0.005}\frac{S}{\sqrt{n}}\right).</equation>因为<equation>t_{0.025}<t_{0.005}</equation>，所以<equation>\alpha=0.05</equation>对应的接受域包含于<equation>\alpha=0.01</equation>对应的接受域.若当检验水平<equation>\alpha=0.05</equation>时，接受<equation>H_{0}</equation>，则当检验水平<equation>\alpha=0.01</equation>时，必接受<equation>H_{0}.</equation>因此，应选D.

---


#### 矩估计和最大似然估计

**2022年第22题 | 解答题 | 12分**


设<equation>X_{1}, X_{2}, \dots, X_{n}</equation>为来自均值为<equation>\theta</equation>的指数分布总体的简单随机样本，<equation>Y_{1}, Y_{2}, \dots, Y_{m}</equation>为来自均值为2<equation>\theta</equation>的指数分布总体的简单随机样本，且两样本相互独立，其中<equation>\theta(\theta>0)</equation>是未知参数。利用样本<equation>X_{1}, X_{2}, \dots, X_{n}, Y_{1}, Y_{2}, \dots, Y_{m}</equation>求<equation>\theta</equation>的最大似然估计量<equation>\hat{\theta}</equation>，并求<equation>D(\hat{\theta})</equation>

**答案:**<equation>\hat {\theta} = \frac {2 \sum_ {i = 1} ^ {n} X _ {i} + \sum_ {j = 1} ^ {m} Y _ {j}}{2 (m + n)}, D (\hat {\theta}) = \frac {\theta^ {2}}{m + n}.</equation>

**解析:**解<equation>X_{1}, X_{2}, \dots , X_{n}</equation>是来自总体X的简单随机样本.由于<equation>E ( X )=\theta</equation>，故X服从参数为<equation>\frac{1}{\theta}</equation>的指数分布.于是，X的概率密度函数为<equation>f _ {X} (x) = \left\{ \begin{array}{l l} \frac {1}{\theta} \mathrm {e} ^ {- \frac {x}{\theta}}, & x > 0, \\ 0, & x \leqslant 0. \end{array} \right.</equation><equation>Y_{1}, Y_{2}, \dots , Y_{m}</equation>是来自总体<equation>Y</equation>的简单随机样本.由于<equation>E(Y)=2\theta</equation>，故Y服从参数为<equation>\frac{1}{2\theta}</equation>的指数分布.于是，<equation>Y</equation>的概率密度函数为<equation>f _ {Y} (y) = \left\{ \begin{array}{l l} \frac {1}{2 \theta} \mathrm {e} ^ {- \frac {y}{2 \theta}}, & y > 0, \\ 0, & y \leqslant 0. \end{array} \right.</equation>设<equation>x_{1}, x_{2}, \dots , x_{n}, y_{1}, y_{2}, \dots , y_{m}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots , X_{n}, Y_{1}, Y_{2}, \dots , Y_{m}</equation>的一组样本值，则似然函数<equation>L (\theta) = \left\{ \begin{array}{l l} \frac {1}{2 ^ {m} \theta^ {m + n}} \mathrm {e} ^ {- \frac {\sum_ {i = 1} ^ {n} x _ {i}}{\theta} - \frac {\sum_ {j = 1} ^ {m} y _ {j}}{2 \theta}}, & x _ {i} > 0, y _ {j} > 0, i = 1, 2, \dots , n, j = 1, 2, \dots , m, \\ 0, & \text {其 他}. \end{array} \right.</equation>当<equation>x_{i} > 0, y_{j} > 0, i = 1, 2, \dots , n, j = 1, 2, \dots , m</equation>时，取对数得<equation>\ln L (\theta) = - m \ln 2 - (m + n) \ln \theta - \frac {\sum_ {i = 1} ^ {n} x _ {i}}{\theta} - \frac {\sum_ {j = 1} ^ {m} y _ {j}}{2 \theta}.</equation>令<equation>\frac{\mathrm{d}\left[\ln L(\theta)\right]}{\mathrm{d}\theta}=0</equation>即<equation>-\frac{m+n}{\theta}+\frac{\sum_{i=1}^{n}x_{i}}{\theta^{2}}+\frac{\sum_{j=1}^{m}y_{j}}{2\theta^{2}}=0</equation>解得<equation>\theta =\frac{2\sum_{i=1}^{n}x_{i}+\sum_{j=1}^{m}y_{j}}{2(m+n)}.</equation>因此，<equation>\theta</equation>的最大似然估计量<equation>\hat{\theta}=\frac{2\sum_{i=1}^{n}X_{i}+\sum_{j=1}^{m}Y_{j}}{2(m+n)}.</equation>下面计算<equation>D(\hat{\theta}).</equation><equation>\begin{aligned} D (\hat {\theta}) &= D \left[ \frac {2 \sum_ {i = 1} ^ {n} X _ {i} + \sum_ {j = 1} ^ {m} Y _ {j}}{2 (m + n)} \right] = \frac {1}{(m + n) ^ {2}} D \left(\sum_ {i = 1} ^ {n} X _ {i}\right) + \frac {1}{4 (m + n) ^ {2}} D \left(\sum_ {j = 1} ^ {m} Y _ {j}\right) \\ &= \frac {1}{(m + n) ^ {2}} \sum_ {i = 1} ^ {n} D \left(X _ {i}\right) + \frac {1}{4 (m + n) ^ {2}} \sum_ {j = 1} ^ {m} D \left(Y _ {j}\right) = \frac {n D (X)}{(m + n) ^ {2}} + \frac {m D (Y)}{4 (m + n) ^ {2}} \\ &= \frac {n \theta^ {2}}{(m + n) ^ {2}} + \frac {m \cdot 4 \theta^ {2}}{4 (m + n) ^ {2}} = \frac {\theta^ {2}}{m + n}. \end{aligned}</equation>或者，注意到<equation>\hat{\theta} = \frac{2\sum_{i=1}^{n}X_{i} + \sum_{j=1}^{m}Y_{j}}{2(m + n)} = \frac{2n\bar{X} + m\bar{Y}}{2(m + n)}</equation>，利用<equation>D(\bar{X}) = \frac{D(X)}{n}, D(\bar{Y}) = \frac{D(Y)}{m}</equation>可得，<equation>D(\hat{\theta}) = D\left[\frac{2n\bar{X} + m\bar{Y}}{2(m + n)}\right] = \frac{n^{2}D(\bar{X})}{(m + n)^{2}} + \frac{m^{2}D(\bar{Y})}{4(m + n)^{2}} = \frac{n^{2}}{(m + n)^{2}}\cdot \frac{D(X)}{n} + \frac{m^{2}}{4(m + n)^{2}}\cdot \frac{D(Y)}{m}</equation><equation>= \frac{n\theta^{2}}{(m + n)^{2}} + \frac{m\cdot 4\theta^{2}}{4(m + n)^{2}} = \frac{\theta^{2}}{m + n}.</equation>

---


#### 区间估计和置信区间

**2016年第14题 | 填空题 | 4分**

14. 设<equation>X_{1}, X_{2}, \cdots, X_{n}</equation>为来自总体<equation>N\left(\mu ,\sigma^{2}\right)</equation>的简单随机样本，样本均值<equation>\bar{X}=9. 5</equation>，参数<equation>\mu</equation>的置信度为0.95的双侧置信区间的置信上限为10.8，则<equation>\mu</equation>的置信度为0.95的双侧置信区间为 ___.

**答案:**## (8.2,10.8)

**解析:**解 由上述表格知，无论<equation>\sigma^{2}</equation>已知还是未知，参数<equation>\mu</equation>的置信度为1<equation>- \alpha</equation>的置信区间的置信上限和置信下限都关于样本均值对称，即<equation>\frac{\mathrm{置信上限}+\mathrm{置信下限}}{2}=\bar{X}</equation>从而置信下限<equation>= 2\overline{X}</equation>-置信上限<equation>= 2\times 9.5-10.8=8.2</equation>于是<equation>\mu</equation>的置信度为0.95的双侧置信区间为（8.2，10.8）.

---


### 随机事件和概率
### 多维随机变量及其分布
#### 边缘分布和条件分布

**2025年第22题 | 解答题 | 12分**
22. 投保人的损失事件发生时，保险公司的赔付额 Y与投保人的损失额 X的关系为<equation>Y=\left\{\begin{array}{ll}0,&X\leqslant 100\\ X-100,&X>100\end{array} \right.</equation>. 设定损事件发生时，投保人的损失额 X的概率密度为<equation>f(x)=\left\{\begin{array}{ll}\frac{2\times 100^{2}}{(100+x)^{3}},&x>0\\ 0,&x\leqslant 0\end{array} \right.</equation>I. 求<equation>P\{Y>0\}</equation>及 EY.

Ⅱ. 这种损失事件在一年内发生的次数记为 N，保险公司在一年内就这种损失事件产生的理赔次数记为 M，假设 N服从参数为8的泊松分布，在<equation>N=n</equation>（<equation>n\geqslant1</equation>）的条件下，M服从二项分布<equation>B(n,p)</equation>，其中<equation>p=P\{Y>0\}</equation>，求 M的概率分布.
**答案: **（I）<equation>P \{ Y > 0 \} = \frac{1}{4}, E ( Y ) = 5 0;</equation>（Ⅱ）M服从参数为2的泊松分布.
**解析: **解（I）根据 Y的定义，<equation>\begin{aligned} P \{Y > 0 \} &= P \{X > 1 0 0 \} = \int_ {1 0 0} ^ {+ \infty} f (x) \mathrm {d} x = \int_ {1 0 0} ^ {+ \infty} \frac {2 \times 1 0 0 ^ {2}}{(1 0 0 + x) ^ {3}} \mathrm {d} x = - \frac {2 \times 1 0 0 ^ {2}}{2} (1 0 0 + x) ^ {- 2} \Bigg | _ {1 0 0} ^ {+ \infty} \\ &= - \frac {1 0 0 ^ {2}}{(1 0 0 + x) ^ {2}} \Bigg | _ {1 0 0} ^ {+ \infty} = \frac {1}{4}. \end{aligned}</equation>由于随机变量<equation>Y</equation>是随机变量<equation>X</equation>的函数，故根据数学期望的定义，<equation>\begin{aligned} E (Y) &= \int_ {- \infty} ^ {+ \infty} y f (x) \mathrm {d} x = \int_ {1 0 0} ^ {+ \infty} (x - 1 0 0) f (x) \mathrm {d} x = \int_ {1 0 0} ^ {+ \infty} \frac {2 \times 1 0 0 ^ {2} (x - 1 0 0)}{(1 0 0 + x) ^ {3}} \mathrm {d} x \\ &= - 1 0 0 ^ {2} \int_ {1 0 0} ^ {+ \infty} (x - 1 0 0) \mathrm {d} \left[ (1 0 0 + x) ^ {- 2} \right] = - 1 0 0 ^ {2} \left[ \frac {x - 1 0 0}{(1 0 0 + x) ^ {2}} \right| _ {1 0 0} ^ {+ \infty} - \int_ {1 0 0} ^ {+ \infty} \frac {\mathrm {d} x}{(1 0 0 + x) ^ {2}} ] \\ &= \frac {- 1 0 0 ^ {2}}{1 0 0 + x} \Big | _ {1 0 0} ^ {+ \infty} = 0 - \left(- \frac {1 0 0 ^ {2}}{2 0 0}\right) = 5 0. \end{aligned}</equation>（Ⅱ）由于<equation>N</equation>服从参数为8的泊松分布，故<equation>P\{N = n\} = \frac{8^{n}\mathrm{e}^{-8}}{n!}</equation>，进一步可得<equation>P\{N = 0\} = \mathrm{e}^{-8}</equation>由于当<equation>N = 0</equation>时，<equation>M</equation>必然等于0，故<equation>P\{M = 0\mid N = 0\} = 1</equation>，从而<equation>P \{M = 0, N = 0 \} = P \{M = 0 \mid N = 0 \} P \{N = 0 \} = 1 \cdot P \{N = 0 \} = \mathrm {e} ^ {- 8}.</equation>由 M的定义可知，当<equation>M=k</equation>时，<equation>N=n\geqslant k</equation>由在<equation>N=n(n\geqslant 1)</equation>的条件下，M服从二项分布<equation>B(n,p)</equation>可得，<equation>P \left\{M = k \mid N = n \right\} = \mathrm {C} _ {n} ^ {k} p ^ {k} (1 - p) ^ {n - k}, \quad k = 0, 1, \dots , n, n = 1, 2, \dots .</equation>由条件概率公式以及 p=<equation>\frac{1}{4}</equation>可得<equation>\begin{aligned} P \{M = k, N = n \} &= P \{M = k \mid N = n \} P \{N = n \} = C _ {n} ^ {k} p ^ {k} (1 - p) ^ {n - k} \frac {8 ^ {n} \mathrm {e} ^ {- 8}}{n !} \\ &= \frac {n !}{k ! (n - k) !} \cdot \left(\frac {1}{4}\right) ^ {k} \cdot \left(\frac {3}{4}\right) ^ {n - k} \cdot \frac {8 ^ {n} \mathrm {e} ^ {- 8}}{n !} = \frac {3 ^ {n - k} 2 ^ {n} \mathrm {e} ^ {- 8}}{k ! (n - k) !} \\ &= \frac {6 ^ {n - k} 2 ^ {k} \mathrm {e} ^ {- 8}}{k ! (n - k) !}. \end{aligned}</equation>由此可得，当<equation>k\neq 0</equation>时，<equation>\begin{aligned} P \{M = k \} &= \sum_ {n = k} ^ {\infty} P \{M = k, N = n \} = \sum_ {n = k} ^ {\infty} \frac {6 ^ {n - k} 2 ^ {k} \mathrm {e} ^ {- 8}}{k ! (n - k) !} = \frac {2 ^ {k} \mathrm {e} ^ {- 2}}{k !} \sum_ {n = k} ^ {\infty} \frac {6 ^ {n - k} \mathrm {e} ^ {- 6}}{(n - k) !} \\ &= \frac {2 ^ {k} \mathrm {e} ^ {- 2}}{k !} \sum_ {n = 0} ^ {\infty} \frac {6 ^ {n} \mathrm {e} ^ {- 6}}{n !}. \end{aligned}</equation><equation>\begin{aligned} P \{M = 0 \} &= \sum_ {n = 0} ^ {\infty} P \{M = 0, N = n \} = \mathrm {e} ^ {- 8} + \sum_ {n = 1} ^ {\infty} P \{M = 0, N = n \} = \mathrm {e} ^ {- 8} + \sum_ {n = 1} ^ {\infty} \frac {6 ^ {n} \mathrm {e} ^ {- 6}}{n !} \cdot \mathrm {e} ^ {- 2} \\ &= \mathrm {e} ^ {- 2} \sum_ {n = 0} ^ {\infty} \frac {6 ^ {n} \mathrm {e} ^ {- 6}}{n !}. \end{aligned}</equation>由泊松分布的定义可知，服从参数为6的泊松分布的随机变量Z的分布律为<equation>P\{Z=n\}=\frac{6^{n}\mathrm{e}^{-6}}{n!}.</equation>由分布律的性质可得，<equation>\sum_{n=0}^{\infty}\frac{6^{n}\mathrm{e}^{-6}}{n!}=1.</equation>于是，<equation>P\{M=k\}=\frac{2^{k}\mathrm{e}^{-2}}{k!}, k=0,1,2,\dots.</equation>因此，M服从参数为2的泊松分布.

---

**2010年第22题 | 解答题 | 11分**
22. (本题满分11分)

设二维随机变量<equation>(X, Y)</equation>的概率密度为<equation>f (x, y) = A \mathrm {e} ^ {- 2 x ^ {2} + 2 x y - y ^ {2}}, (- \infty < x < + \infty , - \infty < y < + \infty).</equation>求常数<equation>A</equation>及条件概率密度<equation>f_{Y|X}(y|x)</equation>.
**答案: **<equation>(2 2) A = \frac {1}{\pi}, f _ {Y \mid X} (y \mid x) = \frac {1}{\sqrt {\pi}} \mathrm {e} ^ {- (x - y) ^ {2}}, y \in (- \infty , + \infty)</equation>
**解析: **解 由概率密度的性质可知，<equation>\int_{- \infty}^{+ \infty}\int_{- \infty}^{+ \infty}f(x,y)\mathrm{d}x\mathrm{d}y=1.</equation>由于<equation>\begin{aligned} \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} x \mathrm {d} y &= \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} A \mathrm {e} ^ {- 2 x ^ {2} + 2 x y - y ^ {2}} \mathrm {d} x \mathrm {d} y = \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} A \mathrm {e} ^ {- x ^ {2} - (y - x) ^ {2}} \mathrm {d} x \mathrm {d} y \\ &= A \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- x ^ {2}} \mathrm {d} x \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- (y - x) ^ {2}} \mathrm {d} y = A \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- x ^ {2}} \mathrm {d} x \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- (y - x) ^ {2}} \mathrm {d} (y - x) \\ &= A \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- x ^ {2}} \mathrm {d} x \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t \frac {\int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t = \sqrt {\pi}}{A \pi}, \end{aligned}</equation>故<equation>A\pi = 1</equation>，从而<equation>A = \frac{1}{\pi}.</equation>由条件概率密度的定义可知，<equation>f_{Y \mid X}(y \mid x) = \frac{f(x,y)}{f_X(x)}.</equation>又由于<equation>f_{X}(x)=\int_{-\infty}^{+\infty} f(x,y)\mathrm{d} y=\frac{1}{\pi}\int_{-\infty}^{+\infty}\mathrm{e}^{-2x^{2}+2xy-y^{2}}\mathrm{d} y=\frac{1}{\pi}\mathrm{e}^{-x^{2}}\int_{-\infty}^{+\infty}\mathrm{e}^{-(y-x)^{2}}\mathrm{d} y=\frac{1}{\pi}\mathrm{e}^{-x^{2}}\cdot \sqrt{\pi}=\frac{1}{\sqrt{\pi}}\mathrm{e}^{-x^{2}},</equation>故对任意给定的<equation>x\in(-\infty,+\infty)</equation>，在 X=x的条件下，Y的条件概率密度为<equation>f _ {Y \mid X} (y \mid x) = \frac {f (x , y)}{f _ {X} (x)} = \frac {\frac {1}{\pi} \mathrm {e} ^ {- 2 x ^ {2} + 2 x y - y ^ {2}}}{\frac {1}{\sqrt {\pi}} \mathrm {e} ^ {- x ^ {2}}} = \frac {1}{\sqrt {\pi}} \mathrm {e} ^ {- x ^ {2} + 2 x y - y ^ {2}} = \frac {1}{\sqrt {\pi}} \mathrm {e} ^ {- (x - y) ^ {2}}, y \in (- \infty , + \infty).</equation>

---

**2009年第22题 | 解答题 | 11分**

袋中有1个红球、2个黑球与3个白球.现有放回地从袋中取两次，每次取一个球.以 X，Y，Z分别表示两次取球所取得的红球、黑球与白球的个数.

I. 求<equation>P\{X=1\mid Z=0\}</equation>；

II. 求二维随机变量（X，Y）的概率分布.
**答案: **(22) ( I )<equation>P \{ X = 1 \mid Z = 0 \} = \frac{4}{9};</equation>（Ⅱ）二维随机变量<equation>(X, Y)</equation>的概率分布为

<table border="1"><tr><td rowspan="2">Y
X</td><td>0</td><td>1</td><td>2</td></tr><tr><td><equation>\frac{1}{4}</equation></td><td><equation>\frac{1}{6}</equation></td><td><equation>\frac{1}{36}</equation></td></tr><tr><td>1</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{9}</equation></td><td>0</td></tr><tr><td>2</td><td><equation>\frac{1}{9}</equation></td><td>0</td><td>0</td></tr></table>
**解析: **解（I）（法一）由条件概率的定义知，<equation>P \{X = 1 \mid Z = 0 \} = \frac {P \{X = 1 , Z = 0 \}}{P \{Z = 0 \}} = \frac {P \{X = 1 , Y = 1 \}}{P \{Z = 0 \}} = \frac {\mathrm {C} _ {2} ^ {1} \cdot \frac {1}{6} \cdot \frac {2}{6}}{\frac {3}{6} \cdot \frac {3}{6}} = \frac {4}{9}.</equation>（法二）<equation>P \{ X=1 \mid Z=0 \}</equation>是指在 Z=0即两次所取的球中没有白球的条件下，两次取球为一黑一红的概率，即为在1个红球、2个黑球中有放回地取得一黑一红的概率，于是<equation>P \left\{X = 1 \mid Z = 0 \right\} = \mathrm {C} _ {2} ^ {1} \cdot \frac {1}{3} \cdot \frac {2}{3} = \frac {4}{9}.</equation>（Ⅱ）由于<equation>X, Y</equation>所有可能的取值均为0,1,2，故二维随机变量<equation>(X, Y)</equation>的概率分布为，<equation>P \{X = 0, Y = 0 \} = P \{Z = 2 \} = \frac {3}{6} \cdot \frac {3}{6} = \frac {1}{4},</equation><equation>P \left\{X = 0, Y = 1 \right\} = P \left\{Y = 1, Z = 1 \right\} = C _ {2} ^ {1} \cdot \frac {2}{6} \cdot \frac {3}{6} = \frac {1}{3},</equation><equation>P \{X = 0, Y = 2 \} = \frac {2}{6} \cdot \frac {2}{6} = \frac {1}{9},</equation><equation>P \{X = 1, Y = 0 \} = P \{X = 1, Z = 1 \} = C _ {2} ^ {1} \cdot \frac {1}{6} \cdot \frac {3}{6} = \frac {1}{6},</equation><equation>P \{X = 1, Y = 1 \} = \mathrm {C} _ {2} ^ {1} \cdot \frac {1}{6} \cdot \frac {2}{6} = \frac {1}{9}, \quad P \{X = 1, Y = 2 \} = 0,</equation><equation>P \{X = 2, Y = 0 \} = \frac {1}{6} \cdot \frac {1}{6} = \frac {1}{3 6}, \quad P \{X = 2, Y = 1 \} = 0, \quad P \{X = 2, Y = 2 \} = 0.</equation>从而 X和 Y的联合分布律为

<table border="1"><tr><td rowspan="2">Y
X</td><td>0</td><td>1</td><td>2</td></tr><tr><td><equation>\frac{1}{4}</equation></td><td><equation>\frac{1}{6}</equation></td><td><equation>\frac{1}{36}</equation></td></tr><tr><td>1</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{9}</equation></td><td>0</td></tr><tr><td>2</td><td><equation>\frac{1}{9}</equation></td><td>0</td><td>0</td></tr></table>

---


#### 二维随机变量及其分布

**2024年第10题 | 选择题 | 5分 | 答案: D**
10. 设随机变量 X，Y相互独立，且均服从参数为<equation>\lambda</equation>的指数分布.令<equation>Z=|X-Y|</equation>，则下列随机变量与 Z同分布的是（    )

A.<equation>X+Y</equation>B.<equation>\frac{X+Y}{2}</equation>C. 2X D. X
答案: D
**解析: **解 由于<equation>X, Y</equation>相互独立，且均服从参数为<equation>\lambda</equation>的指数分布，故<equation>(X, Y)</equation>的联合概率密度为<equation>f (x, y) = \left\{ \begin{array}{l l} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)}, & x > 0, y > 0, \\ 0, & \text {其 他}. \end{array} \right.</equation>记<equation>F_{z}(z)</equation>为<equation>Z=|X-Y|</equation>的分布函数，<equation>D_{z}=\{(x,y)|-z\leq x-y\leq z\}</equation>，则<equation>F _ {z} (z) = P \left\{Z \leqslant z \right\} = P \left\{| X - Y | \leqslant z \right\} = P \left\{- z \leqslant X - Y \leqslant z \right\} = \iint_ {D.} f (x, y) \mathrm {d} x \mathrm {d} y.</equation>当<equation>z < 0</equation>时，<equation>D_{z} = \varnothing , F_{Z}(z) = 0.</equation>当<equation>z \geqslant 0</equation>时，记<equation>D = \{(x,y)|x \geqslant 0,y \geqslant 0\}</equation>，则<equation>D \cap D_{z} \neq \emptyset</equation>，为图（a）中的灰色区域.

(a)

(b)

(c)

下面用两种方法计算<equation>z\geqslant 0</equation>时的<equation>F_{z}(z)</equation>.

（法一）如图（a）所示，由于<equation>D \cap D_{z}</equation>关于直线<equation>y=x</equation>对称，故记其位于直线<equation>y=x</equation>下方的部分为<equation>D_{0}.</equation>将<equation>D_{0}</equation>写成Y型区域，<equation>D_{0}=\left\{(x,y)\mid y\leqslant x\leqslant y+z,0\leqslant y<+\infty\right\}.</equation><equation>\begin{aligned} F _ {Z} (z) &= \iint_ {D _ {z}} f (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {D \cap D _ {z}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y \xlongequal {\text {轮 换 对称 性}} 2 \iint_ {D _ {0}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y \\ &= 2 \lambda^ {2} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \mathrm {d} y \int_ {y} ^ {y + z} \mathrm {e} ^ {- \lambda x} \mathrm {d} x = - 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \cdot \mathrm {e} ^ {- \lambda x} \Bigg | _ {x = y} ^ {x = y + z} \mathrm {d} y \\ &= - 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \left(\mathrm {e} ^ {- \lambda y - \lambda z} - \mathrm {e} ^ {- \lambda y}\right) \mathrm {d} y = - 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- 2 \lambda y} \left(\mathrm {e} ^ {- \lambda z} - 1\right) \mathrm {d} y \\ &= \left(\mathrm {e} ^ {- \lambda z} - 1\right) \int_ {0} ^ {+ \infty} \left(- 2 \lambda \mathrm {e} ^ {- 2 \lambda y}\right) \mathrm {d} y = \left(\mathrm {e} ^ {- \lambda z} - 1\right) \mathrm {e} ^ {- 2 \lambda y} \Bigg | _ {0} ^ {+ \infty} \\ &= \left(\mathrm {e} ^ {- \lambda z} - 1\right) \cdot (- 1) = 1 - \mathrm {e} ^ {- \lambda z}. \end{aligned}</equation>（法二）如图(b)所示，<equation>D_{1}=D\backslash D_{z}</equation>关于直线<equation>y=x</equation>对称，记其位于直线<equation>y=x</equation>下方的部分为<equation>D_{2}.</equation>将<equation>D_{2}</equation>写成Y型区域，<equation>D_{2}=\left\{(x,y)\mid y+z\leqslant x<+\infty ,0\leqslant y<+\infty \right\}.</equation><equation>\begin{aligned} F _ {Z} (z) &= \iint_ {D _ {z}} f (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {D \cap D _ {z}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y = 1 - \iint_ {D _ {1}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y \\ \underline {{\text {轮换 对称性}}} 1 - 2 \iint_ {D _ {2}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y &= 1 - 2 \lambda^ {2} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \mathrm {d} y \int_ {y + z} ^ {+ \infty} \mathrm {e} ^ {- \lambda x} \mathrm {d} x \\ &= 1 + 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \cdot \mathrm {e} ^ {- \lambda x} \left| _ {x = y + z} ^ {+ \infty} \mathrm {d} y = 1 - 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \cdot \mathrm {e} ^ {- \lambda (y + z)} \mathrm {d} y \right. \\ &= 1 - 2 \lambda \mathrm {e} ^ {- \lambda z} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- 2 \lambda y} \mathrm {d} y = 1 + \mathrm {e} ^ {- \lambda z} \cdot \mathrm {e} ^ {- 2 \lambda y} \Big | _ {0} ^ {+ \infty} = 1 - \mathrm {e} ^ {- \lambda z}. \end{aligned}</equation>因此，<equation>F_{z}(z)=\left\{ \begin{array}{ll}1-\mathrm{e}^{-\lambda z},& z\geqslant 0,\\ 0,& \text{其他}, \end{array} \right. f_{z}(z)=\left\{ \begin{array}{ll}\lambda \mathrm{e}^{-\lambda z},& z\geqslant 0,\\ 0,& \text{其他}, \end{array} \right. Z</equation>服从参数为<equation>\lambda</equation>的指数分布.进一步可得，Z与X同分布.选项D正确，选项C错误.

下面说明选项A、B不正确.

对选项A，当<equation>z \geqslant 0</equation>时，由于<equation>D_{3} = \{(x,y) \mid x + y \leqslant z, x \geqslant 0, y \geqslant 0\}</equation>真包含于<equation>D \cap D_{z}</equation>，故<equation>X + Y</equation>的分布函数<equation>F_{1}(z)</equation>满足，对任意<equation>z > 0, F_{1}(z) < F_{Z}(z)</equation>. 从而<equation>X + Y</equation>与<equation>Z</equation>不同分布.

对选项B，当<equation>z\geqslant 0</equation>时，记<equation>D_{4} = \{(x,y)|x + y\leqslant 2z,x\geqslant 0,y\geqslant 0\}</equation>，则<equation>\frac{X+Y}{2}</equation>的分布函数<equation>\begin{array}{l} F _ {2} (z) = \iint_ {D _ {4}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y = \lambda^ {2} \int_ {0} ^ {2 x} \mathrm {e} ^ {- \lambda x} \mathrm {d} x \int_ {0} ^ {2 z - x} \mathrm {e} ^ {- \lambda y} \mathrm {d} y = 1 - (2 \lambda z + 1) \mathrm {e} ^ {- 2 \lambda z} \\ \neq F _ {z} (z). \\ \end{array}</equation>从而<equation>\frac{X+Y}{2}</equation>与Z不同分布.

综上所述，应选D.

---


### 数理统计的基本概念
### 大数定律和中心极限定理
# 数学二
## 高等数学
### 常微分方程
#### 可分离变量的微分方程

**2014年第16题 | 解答题 | 10分**

16. (本题满分10分）

已知函数 y=y(x)满足微分方程<equation>x^{2}+y^{2} y^{\prime}=1-y^{\prime}</equation>，且 y(2)=0，求 y(x)的极大值与极小值.

**答案:**(16) 极大值<equation>y ( 1 ) = 1</equation>，极小值<equation>y (- 1 ) = 0.</equation>

**解析:**整理原微分方程得，<equation>(1 + y ^ {2}) \mathrm {d} y = (1 - x ^ {2}) \mathrm {d} x.</equation>这是可分离变量的微分方程. 方程两端积分得<equation>y + \frac {y ^ {3}}{3} = x - \frac {x ^ {3}}{3} + C.</equation>代入<equation>x = 2</equation>，<equation>y(2) = 0</equation>，得<equation>C = \frac{2}{3}</equation>，从而得到关于<equation>x,y</equation>的一个隐函数方程：<equation>x^{3} + y^{3} - 3x + 3y = 2.</equation>要求<equation>y(x)</equation>的极大值与极小值，可先求<equation>y^{\prime}(x)</equation>. 由（1）式可得<equation>y ^ {\prime} = \frac {1 - x ^ {2}}{1 + y ^ {2}}.</equation>由此可知，当<equation>x=\pm1</equation>时，<equation>y^{\prime}=0</equation>；当<equation>x>1</equation>或<equation>x<-1</equation>时，<equation>y^{\prime}<0</equation>，<equation>y(x)</equation>单调减少；当<equation>-1<x<1</equation>时，<equation>y^{\prime}>0</equation>，<equation>y(x)</equation>单调增加.

于是，<equation>y ( x )</equation>在<equation>x=1</equation>处取到极大值，在<equation>x=-1</equation>处取到极小值.由<equation>x^{3}+y^{3}-3 x+3 y=2</equation>可计算得，当<equation>x=-1</equation>时，<equation>y=0</equation>；当<equation>x=1</equation>时，<equation>y=1</equation>因此，<equation>y ( x )</equation>的极大值为<equation>y ( 1 )=1</equation>，极小值为<equation>y (-1)=0.</equation>

---

**2014年第16题 | 解答题 | 10分**
16. (本题满分10分）

已知函数 y=y(x)满足微分方程<equation>x^{2}+y^{2} y^{\prime}=1-y^{\prime}</equation>，且 y(2)=0，求 y(x)的极大值与极小值.
**答案: **(16) 极大值<equation>y ( 1 ) = 1</equation>，极小值<equation>y (- 1 ) = 0.</equation>
**解析: **整理原微分方程得，<equation>(1 + y ^ {2}) \mathrm {d} y = (1 - x ^ {2}) \mathrm {d} x.</equation>这是可分离变量的微分方程. 方程两端积分得<equation>y + \frac {y ^ {3}}{3} = x - \frac {x ^ {3}}{3} + C.</equation>代入<equation>x = 2</equation>，<equation>y(2) = 0</equation>，得<equation>C = \frac{2}{3}</equation>，从而得到关于<equation>x,y</equation>的一个隐函数方程：<equation>x^{3} + y^{3} - 3x + 3y = 2.</equation>要求<equation>y(x)</equation>的极大值与极小值，可先求<equation>y^{\prime}(x)</equation>. 由（1）式可得<equation>y ^ {\prime} = \frac {1 - x ^ {2}}{1 + y ^ {2}}.</equation>由此可知，当<equation>x=\pm1</equation>时，<equation>y^{\prime}=0</equation>；当<equation>x>1</equation>或<equation>x<-1</equation>时，<equation>y^{\prime}<0</equation>，<equation>y(x)</equation>单调减少；当<equation>-1<x<1</equation>时，<equation>y^{\prime}>0</equation>，<equation>y(x)</equation>单调增加.

于是，<equation>y ( x )</equation>在<equation>x=1</equation>处取到极大值，在<equation>x=-1</equation>处取到极小值.由<equation>x^{3}+y^{3}-3 x+3 y=2</equation>可计算得，当<equation>x=-1</equation>时，<equation>y=0</equation>；当<equation>x=1</equation>时，<equation>y=1</equation>因此，<equation>y ( x )</equation>的极大值为<equation>y ( 1 )=1</equation>，极小值为<equation>y (-1)=0.</equation>

---

