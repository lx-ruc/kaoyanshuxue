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

**2021年第15题 | 填空题 | 5分**

15. 设<equation>A=\left(a_{ij}\right)</equation>为3阶矩阵，<equation>A_{ij}</equation>为元素<equation>a_{ij}</equation>的代数余子式，若 A的每行元素之和均为2，且<equation>|A|=3</equation>，则<equation>A_{11}+A_{21}+</equation><equation>A_{31}=</equation>___

**答案:**## 3 2.

**解析:**解（法一）由于<equation>A</equation>的每行元素之和均为2，故<equation>\begin{aligned} | \boldsymbol {A} | &= \left| \begin{array}{l l l} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3}  \right| \xlongequal {c _ {1} + c _ {2} + c _ {3}} \left| \begin{array}{l l l} a _ {1 1} + a _ {1 2} + a _ {1 3} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} + a _ {2 2} + a _ {2 3} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} + a _ {3 2} + a _ {3 3} & a _ {3 2} & a _ {3 3}  \right| &= \left| \begin{array}{l l l} 2 & a _ {1 2} & a _ {1 3} \\ 2 & a _ {2 2} & a _ {2 3} \\ 2 & a _ {3 2} & a _ {3 3}  \right| \\ &= 2 \left| \begin{array}{c c c} 1 & a _ {1 2} & a _ {1 3} \\ 1 & a _ {2 2} & a _ {2 3} \\ 1 & a _ {3 2} & a _ {3 3}  \right| &= 2 \left(A _ {1 1} + A _ {2 1} + A _ {3 1}\right). \end{aligned}</equation>又因为<equation>|A| = 3</equation>，所以<equation>A_{11} + A_{21} + A_{31} = \frac{3}{2}</equation>（法二）由于 A的每行元素之和均为2，故<equation>A\binom{1}{1}=\binom{2}{2},\binom{1}{1}</equation>为 A的属于特征值2的特征向量.于是，<equation>\binom{1}{1}</equation>也是<equation>A^{*}</equation>的属于特征值<equation>\frac{|A|}{2}=\frac{3}{2}</equation>的特征向量，即<equation>\begin{aligned} \boldsymbol {A} ^ {*} \left(  1 \\ 1 \\ 1  \right) &= \left( \begin{array}{c c c} A _ {1 1} & A _ {2 1} & A _ {3 1} \\ A _ {1 2} & A _ {2 2} & A _ {3 2} \\ A _ {1 3} & A _ {2 3} & A _ {3 3}  \right) \left(  1 \\ 1 \\ 1  \right) &= \frac {3}{2} \left(  1 \\ 1 \\ 1  \right). \end{aligned}</equation>因此，<equation>A_{11}+A_{21}+A_{31}=\frac{3}{2}.</equation>

---

**2020年第13题 | 填空题 | 4分**

13. 行列式<equation>\left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a \end{array} \right| = \underline {{\quad}}</equation>

**答案:**<equation>a^{4}-4 a^{2}.</equation>

**解析:**解（法一）利用行列式的性质对所求行列式进行转化.

若<equation>a = 0</equation>，则将第二行加到第一行可得零行，从而行列式为0.

若 a≠0，则<equation>\begin{aligned} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a  \right| \xlongequal {r _ {4} + r _ {3}} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 0 & 0 & a & a  \right| \xlongequal {r _ {3} + \frac {1}{a} r _ {1}} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ 0 & 1 & a - \frac {1}{a} & \frac {1}{a} \\ 0 & 0 & a & a  \right| \\ \xlongequal {r _ {3} - \frac {1}{a} r _ {2}} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ 0 & 0 & a - \frac {2}{a} & \frac {2}{a} \\ 0 & 0 & a & a  \right| &= \left| \begin{array}{c c} a & 0 \\ 0 & a  \right| \cdot \left| \begin{array}{c c} a - \frac {2}{a} & \frac {2}{a} \\ a & a  \right| \\ &= a ^ {2} \left[ \left(a - \frac {2}{a}\right) a - 2 \right] = a ^ {2} \left(a ^ {2} - 4\right) = a ^ {4} - 4 a ^ {2}. \end{aligned}</equation>不论是哪种情况，所求行列式均为<equation>a^4 - 4a^2</equation>.

（法二）注意到所求行列式的各行元素之和均为 a，故可将各列均加到第1列，然后计算行列式.<equation>\begin{array}{l} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a \end{array} \right| \frac {c _ {1} + c _ {2} + c _ {3} + c _ {4}}{\hline} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ a & a & 1 & - 1 \\ a & 1 & a & 0 \\ a & - 1 & 0 & a \end{array} \right| = a \left| \begin{array}{c c c c} 1 & 0 & - 1 & 1 \\ 1 & a & 1 & - 1 \\ 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a \end{array} \right| \\ \frac {c _ {3} + c _ {1}}{c _ {4} - c _ {1}} a \left| \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 1 & a & 2 & - 2 \\ 1 & 1 & a + 1 & - 1 \\ 1 & - 1 & 1 & a - 1 \end{array} \right| \frac {c _ {3} + c _ {4}}{\hline} a \left| \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 1 & a & 0 & - 2 \\ 1 & 1 & a & - 1 \\ 1 & - 1 & a & a - 1 \end{array} \right| \\ \frac {\text {按第一行展开}}{\mathrm {=} a ^ {4} - 4 a ^ {2}} a \left\{a \left[ a (a - 1) + a \right] - 2 (a + a) \right\} = a \left(a ^ {3} - 4 a\right) \\ \end{array}</equation>

---

**2016年第13题 | 填空题 | 4分**

13. 行列式<equation>\left| \begin{array}{c c c c} \lambda & - 1 & 0 & 0 \\ 0 & \lambda & - 1 & 0 \\ 0 & 0 & \lambda & - 1 \\ 4 & 3 & 2 & \lambda + 1 \end{array} \right| = \underline {{\quad}}</equation>

**答案:**<equation>\lambda^{4}+\lambda^{3}+2\lambda^{2}+3\lambda+4.</equation>

**解析:**解 （法一）按第一列展开.<equation>\begin{aligned} \left| \begin{array}{c c c c} \lambda & - 1 & 0 & 0 \\ 0 & \lambda & - 1 & 0 \\ 0 & 0 & \lambda & - 1 \\ 4 & 3 & 2 & \lambda + 1  \right| &= \lambda \left| \begin{array}{c c c} \lambda & - 1 & 0 \\ 0 & \lambda & - 1 \\ 3 & 2 & \lambda + 1  \right| - 4 \left| \begin{array}{c c c} - 1 & 0 & 0 \\ \lambda & - 1 & 0 \\ 0 & \lambda & - 1  \right| \\ &= \lambda \left(\lambda \left| \begin{array}{c c} \lambda & - 1 \\ 2 & \lambda + 1  \right| + 3 \left| \begin{array}{c c} - 1 & 0 \\ \lambda & - 1  \right|\right) - 4 \times (- 1) ^ {3} \\ &= \lambda \left[ \lambda \left(\lambda^ {2} + \lambda + 2\right) + 3 \right] + 4 \\ &= \lambda^ {4} + \lambda^ {3} + 2 \lambda^ {2} + 3 \lambda + 4. \end{aligned}</equation>（法二）利用行列式的性质.<equation>\begin{aligned} \left| \begin{array}{c c c c} \lambda & - 1 & 0 & 0 \\ 0 & \lambda & - 1 & 0 \\ 0 & 0 & \lambda & - 1 \\ 4 & 3 & 2 & \lambda + 1  \right| \xlongequal {c _ {1} + \lambda c _ {2}} \left| \begin{array}{c c c c} 0 & - 1 & 0 & 0 \\ \lambda^ {2} & \lambda & - 1 & 0 \\ 0 & 0 & \lambda & - 1 \\ 4 + 3 \lambda & 3 & 2 & \lambda + 1  \right| \\ \xlongequal {c _ {1} + \lambda^ {2} c _ {3}} \left| \begin{array}{c c c c} 0 & - 1 & 0 & 0 \\ 0 & \lambda & - 1 & 0 \\ \lambda^ {3} & 0 & \lambda & - 1 \\ 4 + 3 \lambda + 2 \lambda^ {2} & 3 & 2 & \lambda + 1  \right| \\ \xlongequal {c _ {1} + \lambda^ {3} c _ {4}} \left| \begin{array}{c c c c} 0 & - 1 & 0 & 0 \\ 0 & \lambda & - 1 & 0 \\ 0 & 0 & \lambda & - 1 \\ 4 + 3 \lambda + 2 \lambda^ {2} + \lambda^ {3} (\lambda + 1) & 3 & 2 & \lambda + 1  \right| \\ &= (- 1) ^ {4 + 1} \left[ 4 + 3 \lambda + 2 \lambda^ {2} + \lambda^ {3} (\lambda + 1) \right] (- 1) ^ {3} \\ &= \lambda^ {4} + \lambda^ {3} + 2 \lambda^ {2} + 3 \lambda + 4. \end{aligned}</equation>

---

**2015年第13题 | 填空题 | 4分**

13. n阶行列式<equation>\left| \begin{array}{c c c c c} 2 & 0 & \dots & 0 & 2 \\ - 1 & 2 & \dots & 0 & 2 \\ \vdots & \vdots & & \vdots & \vdots \\ 0 & 0 & \dots & 2 & 2 \\ 0 & 0 & \dots & - 1 & 2 \end{array} \right| = \underline {{\quad}}</equation>

**解析:**解（法一）记<equation>D_{n}=\left| \begin{array}{cccccc}2&0&\dots&0&2\\ -1&2&\dots&0&2\\ \vdots &\vdots & &\vdots &\vdots \\ 0&0&\dots&2&2\\ 0&0&\dots&-1&2 \end{array} \right|_{n\times n}</equation>，将<equation>D_{n}</equation>按第一行展开得到<equation>\begin{aligned} D _ {n} &= 2 D _ {n - 1} + (- 1) ^ {n + 1} \cdot 2 \left| \begin{array}{c c c c c} - 1 & 2 & & & \\ & - 1 & 2 & & \\ & & \ddots & \ddots & \\ & & & \ddots & 2 \\ & & & & - 1  \right| _ {(n - 1) \times (n - 1)} \\ &= 2 D _ {n - 1} + 2 (- 1) ^ {n + 1} \cdot (- 1) ^ {n - 1} = 2 D _ {n - 1} + 2. \end{aligned}</equation>于是<equation>\begin{aligned} D _ {n} &= 2 D _ {n - 1} + 2 = 2 \left(2 D _ {n - 2} + 2\right) + 2 = 2 ^ {2} D _ {n - 2} + 2 ^ {2} + 2 \\ &= \dots \\ &= 2 ^ {n - 1} D _ {1} + 2 ^ {n - 1} + 2 ^ {n - 2} + \dots + 2 \\ &= 2 ^ {n} + 2 ^ {n - 1} + \dots + 2 = 2 ^ {n + 1} - 2. \end{aligned}</equation>（法二）对行列式作如下行变换.<equation>\begin{aligned} \left| \begin{array}{c c c c c} 2 & 0 & \dots & 0 & 2 \\ - 1 & 2 & \dots & 0 & 2 \\ \vdots & \vdots & & \vdots & \vdots \\ 0 & 0 & \dots & 2 & 2 \\ 0 & 0 & \dots & - 1 & 2  \right| \underline {{r _ {2} + \frac {1}{2} r _ {1}}} \left| \begin{array}{c c c c c c} 2 & 0 & 0 & \dots & 0 & 2 \\ 0 & 2 & 0 & \dots & 0 & 2 + 1 \\ 0 & - 1 & 2 & \dots & 0 & 2 \\ \vdots & \vdots & \vdots & & \vdots & \vdots \\ 0 & 0 & 0 & \dots & 2 & 2 \\ 0 & 0 & 0 & \dots & - 1 & 2  \right| \\ \underline {{r _ {3} + \frac {1}{2} r _ {2}}} \left| \begin{array}{c c c c c c} 2 & 0 & 0 & \dots & 0 & 2 \\ 0 & 2 & 0 & \dots & 0 & 2 + 1 \\ 0 & 0 & 2 & \dots & 0 & \frac {2 ^ {2} + 2 + 1}{2} \\ \vdots & \vdots & \vdots & & \vdots & \vdots \\ 0 & 0 & 0 & \dots & 2 & 2 \\ 0 & 0 & 0 & \dots & - 1 & 2  \right| \\ \underline {{r _ {4} + \frac {1}{2} r _ {3}}} \dots \\ \underline {{r _ {n} + \frac {1}{2} r _ {n - 1}}} \left| \begin{array}{c c c c c c} 2 & & & & 2 \\ & 2 & & & 2 + 1 \\ & & \ddots & & \vdots \\ & & & 2 & \frac {2 ^ {n - 2} + 2 ^ {n - 3} + \dots + 2 + 1}{2 ^ {n - 3}} \\ & & & & \frac {2 ^ {n - 1} + \dots + 2 + 1}{2 ^ {n - 2}}  \right| \\ &= 2 ^ {n - 1} \cdot \frac {2 ^ {n - 1} + \dots + 2 + 1}{2 ^ {n - 2}} \\ &= 2 \cdot \frac {1 - 2 ^ {n}}{1 - 2} = 2 ^ {n + 1} - 2. \end{aligned}</equation>

---

**2014年第5题 | 选择题 | 4分 | 答案: B**

5. 行列式<equation>\left| \begin{array}{c c c c} 0 & a & b & 0 \\ a & 0 & 0 & b \\ 0 & c & d & 0 \\ c & 0 & 0 & d \end{array} \right|</equation>A.<equation>( a d-b c )^{2}</equation>B.<equation>-( a d-b c )^{2}</equation>C.<equation>a^{2} d^{2}-b^{2} c^{2}</equation>D.<equation>b^{2} c^{2}-a^{2} d^{2}</equation>

答案: B

**解析:**解（法一）将原行列式作初等变换使之与分块对角矩阵的行列式建立联系.根据行列式的性质，交换两行或两列，所得新行列式为原行列式的负值.<equation>\left| \begin{array}{c c c c} 0 & a & b & 0 \\ a & 0 & 0 & b \\ 0 & c & d & 0 \\ c & 0 & 0 & d \end{array} \right| = - \left| \begin{array}{c c c c} 0 & a & b & 0 \\ 0 & c & d & 0 \\ a & 0 & 0 & b \\ c & 0 & 0 & d \end{array} \right| = \left| \begin{array}{c c c c} a & 0 & b & 0 \\ c & 0 & d & 0 \\ 0 & a & 0 & b \\ 0 & c & 0 & d \end{array} \right| = - \left| \begin{array}{c c c c} a & b & 0 & 0 \\ c & d & 0 & 0 \\ 0 & 0 & a & b \\ 0 & 0 & c & d \end{array} \right| = - (a d - b c) ^ {2}.</equation>应选B.

（法二）按第一行展开.<equation>\left| \begin{array}{c c c c} 0 & a & b & 0 \\ a & 0 & 0 & b \\ 0 & c & d & 0 \\ c & 0 & 0 & d \end{array} \right| = (- a) \left| \begin{array}{c c c} a & 0 & b \\ 0 & d & 0 \\ c & 0 & d \end{array} \right| + b \left| \begin{array}{c c c} a & 0 & b \\ 0 & c & 0 \\ c & 0 & d \end{array} \right| = - a ^ {2} d ^ {2} + a b c d + a b c d - b ^ {2} c ^ {2} = - (a d - b c) ^ {2}.</equation>应选B.

---


## 概率论与数理统计


### 随机变量的数字特征


