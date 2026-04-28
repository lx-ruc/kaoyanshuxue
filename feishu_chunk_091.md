---

**2016年第6题 | 选择题 | 4分 | 答案: B**

6. 设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=x_{1}^{2}+x_{2}^{2}+x_{3}^{2}+4 x_{1} x_{2}+4 x_{1} x_{3}+4 x_{2} x_{3}</equation>，则<equation>f \left( x_{1}, x_{2}, x_{3} \right)=2</equation>在空间直角坐标下表示的二次曲面为（    ）

A. 单叶双曲面 B. 双叶双曲面 C. 椭球面 D. 柱面

答案: B

**解析:**解 二次型<equation>f</equation>对应的矩阵为<equation>A = \left( \begin{array}{lll}1 & 2 & 2\\ 2 & 1 & 2\\ 2 & 2 & 1 \end{array} \right)</equation>，则矩阵<equation>A</equation>的特征多项式为<equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda - 1 & - 2 & - 2 \\ - 2 & \lambda - 1 & - 2 \\ - 2 & - 2 & \lambda - 1 \end{array} \right| = (\lambda + 1) ^ {2} (\lambda - 5),</equation>从而矩阵 A的特征值为<equation>\lambda_{1}=\lambda_{2}=-1,\lambda_{3}=5</equation>.于是<equation>f(x_{1},x_{2},x_{3})=2</equation>在空间直角坐标下表示的二次曲面在坐标系的正交变换下可化为二次曲面<equation>-y_{1}^{2}-y_{2}^{2}+5y_{3}^{2}=2</equation>即<equation>\frac{5y_{3}^{2}}{2}-\frac{y_{1}^{2}}{2}-\frac{y_{2}^{2}}{2}=1.</equation>对照上述表格可知，所求二次曲面为双叶双曲面，应选B.

---

**2015年第6题 | 选择题 | 4分 | 答案: A**

6. 设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>在正交变换<equation>x=P y</equation>下的标准形为<equation>2 y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>其中<equation>P=(e_{1}, e_{2}, e_{3})</equation>.若<equation>Q=(e_{1},-e_{3},e_{2})</equation>则<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>在正交变换<equation>x=Q y</equation>下的标准形为（    )

A.<equation>2 y_{1}^{2}-y_{2}^{2}+y_{3}^{2}</equation>B.<equation>2 y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>C.<equation>2 y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>D.<equation>2 y_{1}^{2}+y_{2}^{2}+y_{3}^{2}</equation>

答案: A

**解析:**解（法一）由题设知，二次型<equation>f ( x_{1}, x_{2}, x_{3} )</equation>对应的对称矩阵 A满足<equation>P^{\mathrm{T}} A P=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -1 \end{array} \right).</equation>又由题设，<equation>Q=P\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{array} \right)</equation>，故<equation>Q^{\mathrm{T}} A Q=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{array} \right)\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -1 \end{array} \right)\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{array} \right)=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>因此，<equation>f \left(x_{1}, x_{2}, x_{3}\right)</equation>在<equation>\mathbf{x}=Q\mathbf{y}</equation>下的标准形为<equation>f=2y_{1}^{2}-y_{2}^{2}+y_{3}^{2}</equation>应选A.

（法二）由题设知，二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>在正交变换<equation>\boldsymbol{x}=\boldsymbol{P}\boldsymbol{y}</equation>下的标准形为<equation>f=2 y_{1}^{2}+y_{2}^{2}-y_{3}^{2}.</equation>因此，该二次型所对应的对称矩阵A的特征值为2，1，-1，而<equation>e_{1}, e_{2}, e_{3}</equation>分别为属于特征值2，1，-1的特征向量.

若<equation>Q=\left(e_{1},-e_{3},e_{2}\right)</equation>，则由<equation>A\left(-e_{3}\right)=-Ae_{3}=-\left(-e_{3}\right)</equation>可知<equation>-e_{3}</equation>也为属于特征值-1的特征向量，故<equation>Q^{\mathrm{T}}AQ=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{array} \right). f \left( x_{1}, x_{2}, x_{3} \right)</equation>在<equation>\boldsymbol{x}=Q\boldsymbol{y}</equation>下的标准形为<equation>f=2 y_{1}^{2}-y_{2}^{2}+y_{3}^{2}.</equation>应选A.

---

**2014年第13题 | 填空题 | 4分**

13. 设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=x_{1}^{2}-x_{2}^{2}+2 a x_{1} x_{3}+4 x_{2} x_{3}</equation>的负惯性指数为1，则 a的取值范围是 ___.

**解析:**解 （法一）用配方法将原二次型化为标准形.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= \left(x _ {1} + a x _ {3}\right) ^ {2} - a ^ {2} x _ {3} ^ {2} - \left(x _ {2} - 2 x _ {3}\right) ^ {2} + 4 x _ {3} ^ {2} \\ &= \left(x _ {1} + a x _ {3}\right) ^ {2} - \left(x _ {2} - 2 x _ {3}\right) ^ {2} + \left(4 - a ^ {2}\right) x _ {3} ^ {2}. \end{aligned}</equation>因此，若二次型<equation>f(x_{1},x_{2},x_{3})</equation>的负惯性指数为1，则<equation>4 - a^{2}\geqslant 0</equation>，即<equation>a\in [-2,2]</equation>（法二）写出二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>对应的对称矩阵<equation>A.</equation><equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & 0 & a \\ 0 & - 1 & 2 \\ a & 2 & 0 \end{array} \right).</equation>计算<equation>A</equation>的行列式得，<equation>|A| = a^{2} - 4.</equation>A的迹等于零，说明A的特征值之和为零.

下面我们证明，当3阶非零实对称矩阵<equation>A</equation>的迹为零时，<equation>A</equation>的负惯性指数为1等价于<equation>|A| \leqslant 0.</equation>当3阶非零实对称矩阵<equation>A</equation>的迹为零时，由<equation>A</equation>的负惯性指数为1可知，<equation>A</equation>的特征值可能为两正、一负，或者一正、一零、一负.在这两种情形下，<equation>|A| \leqslant 0.</equation>若<equation>A</equation>为3阶非零实对称矩阵，且<equation>|A| \leqslant 0</equation>，则<equation>A</equation>的特征值的符号有五种可能：（1）两正、一负；（2）一正、一零、一负；（3）两零、一负；（4）三负；（5）全为零.两个零特征值、一个负特征值与三个负特征值的情形与<equation>A</equation>的迹为零矛盾.特征值全为零的情形与<equation>A</equation>是非零实对称矩阵矛盾，因为若<equation>A</equation>的特征值全为零，则<equation>A</equation>相似于零矩阵，从而<equation>A</equation>为零矩阵.因此，<equation>A</equation>的特征值仅可能为两正、一负，或一正、一零、一负.在这两种情形下，<equation>A</equation>的负惯性指数都为1.

综上所述，<equation>A</equation>的负惯性指数为1等价于<equation>|A| \leqslant 0</equation>，即<equation>a \in [-2, 2]</equation>

---

**2013年第21题 | 解答题 | 11分**


设二次型<equation>f\left(x_{1},x_{2},x_{3}\right)=2\left(a_{1}x_{1}+a_{2}x_{2}+a_{3}x_{3}\right)^{2}+\left(b_{1}x_{1}+b_{2}x_{2}+b_{3}x_{3}\right)^{2}</equation>，记<equation>\begin{aligned} \alpha &= \left(  a _ {1} \\ a _ {2} \\ a _ {3}  \right), \quad \beta &= \left(  b _ {1} \\ b _ {2} \\ b _ {3}  \right) \end{aligned}</equation>I. 证明二次型 f对应的矩阵为<equation>2\alpha\alpha^{\mathrm{T}}+\beta\beta^{\mathrm{T}}</equation>；

II. 若<equation>\alpha, \beta</equation>正交且均为单位向量，证明 f在正交变换下的标准形为<equation>2y_{1}^{2}+y_{2}^{2}.</equation>

**答案:**(21) （ I ）证明略；（ II ）证明略

**解析:**证 （I）记<equation>\boldsymbol{x}=\left(x_{1},x_{2},x_{3}\right)^{\mathrm{T}}</equation><equation>f</equation>对应的矩阵为A,A为对称矩阵，则<equation>a _ {1} x _ {1} + a _ {2} x _ {2} + a _ {3} x _ {3} = \boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\alpha} = \boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {x}, \quad b _ {1} x _ {1} + b _ {2} x _ {2} + b _ {3} x _ {3} = \boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\beta} = \boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {x}.</equation><equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = 2 \left(\boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\alpha}\right) \left(\boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {x}\right) + \left(\boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\beta}\right) \left(\boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {x}\right) = \boldsymbol {x} ^ {\mathrm {T}} \left(2 \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}\right) \boldsymbol {x}.</equation>又由于<equation>(2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}})^{\mathrm{T}} = 2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>，故<equation>2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>是对称矩阵.于是<equation>2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>为所求A.

（Ⅱ）（法一）由<equation>A = 2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>且<equation>\alpha</equation>与<equation>\beta</equation>相互正交<equation>(\alpha^{\mathrm{T}}\beta = 0, \beta^{\mathrm{T}}\alpha = 0)</equation>得，<equation>A \alpha = \left(2 \alpha \alpha^ {\mathrm {T}} + \beta \beta^ {\mathrm {T}}\right) \alpha = 2 \alpha , \quad A \beta = \left(2 \alpha \alpha^ {\mathrm {T}} + \beta \beta^ {\mathrm {T}}\right) \beta = \beta .</equation>因此，2,1均为<equation>A</equation>的特征值，而<equation>\alpha ,\beta</equation>分别为属于特征值2,1的特征向量.

下面还需确定 A的另一个特征值.

考虑 A的秩.

由于对任何非零<equation>n</equation>维列向量<equation>\alpha ,\beta ,</equation>矩阵<equation>\beta \alpha^{\mathrm{T}}</equation>的秩均为1，故<equation>r (\boldsymbol {A}) = r \left(2 \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}\right) \leqslant r \left(2 \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}}\right) + r \left(\boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}\right) = 2.</equation>于是，<equation>\mathbf{A}</equation>不满秩，0也是<equation>\mathbf{A}</equation>的特征值.

因此，存在正交矩阵<equation>P</equation>使得<equation>P^{\mathrm{T}}AP = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).f</equation>在正交变换<equation>x = Py</equation>下的标准形为<equation>f = 2y_{1}^{2} + y_{2}^{2}</equation>.

（法二）取<equation>\gamma</equation>为与<equation>\alpha ,\beta</equation>均正交的单位向量，可取<equation>\gamma = \frac{\alpha \times \beta}{\| \alpha \times \beta \|} (\alpha \times \beta</equation>为向量<equation>\alpha ,\beta</equation>的向量积，<equation>\| \alpha \times \beta \|</equation>是向量<equation>\alpha \times \beta</equation>的模），则<equation>P = (\alpha ,\beta ,\gamma)</equation>为正交矩阵.<equation>\begin{aligned} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} &= \left(  \boldsymbol {\alpha} ^ {\mathrm {T}} \\ \boldsymbol {\beta} ^ {\mathrm {T}} \\ \boldsymbol {\gamma} ^ {\mathrm {T}}  \right) \left(2 \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}\right) (\boldsymbol {\alpha}, \boldsymbol {\beta}, \gamma) &= \left(  2 \boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}} \\ 2 \boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}} \\ 2 \boldsymbol {\gamma} ^ {\mathrm {T}} \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\gamma} ^ {\mathrm {T}} \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}  \right) (\boldsymbol {\alpha}, \boldsymbol {\beta}, \gamma). \end{aligned}</equation>由于<equation>\alpha, \beta, \gamma</equation>相互正交，故<equation>\alpha^{\mathrm{T}}\boldsymbol{\beta} = \beta^{\mathrm{T}}\alpha = \gamma^{\mathrm{T}}\alpha = \gamma^{\mathrm{T}}\boldsymbol{\beta} = 0, \alpha^{\mathrm{T}}\alpha = \beta^{\mathrm{T}}\boldsymbol{\beta} = 1.</equation><equation>\boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} = \left( \begin{array}{c} 2 \boldsymbol {\alpha} ^ {\mathrm {T}} \\ \boldsymbol {\beta} ^ {\mathrm {T}} \\ \mathbf {0} \end{array} \right) (\boldsymbol {\alpha}, \boldsymbol {\beta}, \gamma) = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>因此，<equation>f</equation>在正交变换<equation>x = Py</equation>下的标准形为<equation>f = 2y_{1}^{2} + y_{2}^{2}</equation>.

---

**2012年第21题 | 解答题 | 11分**

21. (本题满分11分)

已知<equation>A=\left( \begin{array}{c c c}1&0&1\\ 0&1&1\\ -1&0&a\\ 0&a&-1 \end{array} \right),</equation>二次型<equation>f \left( x_{1}, x_{2}, x_{3}\right)=\boldsymbol{x}^{\mathrm{T}}\left( \boldsymbol{A}^{\mathrm{T}}\boldsymbol{A}\right)\boldsymbol{x}</equation>的秩为2.

I. 求实数 a的值；

II. 求正交变换<equation>x=Q y</equation>将二次型 f化为标准形.

**答案:**(21) ( I ) a = -1;

（Ⅱ）<equation>Q=\left( \begin{array}{c c c} {\frac{1}{\sqrt{6}}} & {-\frac{1}{\sqrt{2}}} & {-\frac{1}{\sqrt{3}}} \\ {\frac{1}{\sqrt{6}}} & {\frac{1}{\sqrt{2}}} & {-\frac{1}{\sqrt{3}}} \\ {\frac{2}{\sqrt{6}}} & {0} & {\frac{1}{\sqrt{3}}} \end{array} \right)</equation>正交变换<equation>x=Q y</equation>将二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>变成标准形<equation>f = 6 y _ {1} ^ {2} + 2 y _ {2} ^ {2}.</equation>

**解析:**（I）（法一）二次型<equation>f</equation>的秩等于它所对应的实对称矩阵<equation>A^{\mathrm{T}}A</equation>的秩，于是<equation>r(A^{\mathrm{T}}A) = 2.</equation>下面我们证明<equation>r(\mathbf{A}^{\mathrm{T}}\mathbf{A}) = r(\mathbf{A})</equation>由于<equation>A^{\mathrm{T}}A</equation>与 A的列数相等，故证明<equation>r(A^{\mathrm{T}}A)=r(A)</equation>只需要证明<equation>A^{\mathrm{T}}Ax=0</equation>与<equation>Ax=0</equation>同解.若 x满足<equation>Ax=0</equation>，则<equation>A^{\mathrm{T}}(Ax)=0</equation>，即<equation>(A^{\mathrm{T}}A)x=0.</equation>另一方面，若<equation>\boldsymbol{x}</equation>满足<equation>\left( A^{\mathrm{T}} A \right) \boldsymbol{x}=\mathbf{0}</equation>，则<equation>\boldsymbol{x}^{\mathrm{T}} \left( A^{\mathrm{T}} A \right) \boldsymbol{x}=\mathbf{0}</equation>，即<equation>\left( A \boldsymbol{x} \right)^{\mathrm{T}} \left( A \boldsymbol{x} \right)=\mathbf{0}</equation>.由于<equation>\boldsymbol{\alpha}^{\mathrm{T}}\boldsymbol{\alpha}=\mathbf{0}</equation>当且仅当<equation>\boldsymbol{\alpha}=\mathbf{0}</equation>，故<equation>A \boldsymbol{x}=\mathbf{0}.</equation>因此，<equation>r(\mathbf{A}) = r(\mathbf{A}^{\mathrm{T}}\mathbf{A}) = 2.</equation>我们可以对<equation>A</equation>作初等行变换，求得<equation>r(A) = 2</equation>时的<equation>a</equation>的值.<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ - 1 & 0 & a \\ 0 & a & - 1 \end{array} \right) \xrightarrow [ r _ {4} - a r _ {2} ]{r _ {3} + r _ {1}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & a + 1 \\ 0 & 0 & - a - 1 \end{array} \right) \xrightarrow [ r _ {4} ^ {*} + r _ {3} ^ {*} ]{r _ {4} ^ {*} + r _ {3} ^ {*}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & a + 1 \\ 0 & 0 & 0 \end{array} \right).</equation>由此看出，仅当<equation>a + 1 = 0</equation>时，<equation>r(A) = 2</equation>，故<equation>a = -1.</equation>（法二）由于<equation>r(\mathbf{A}^{\mathrm{T}}\mathbf{A}) = 2</equation>，而<equation>\mathbf{A}^{\mathrm{T}}\mathbf{A}</equation>为<equation>3\times 3</equation>矩阵，故<equation>|\mathbf{A}^{\mathrm{T}}\mathbf{A}| = 0.</equation><equation>\boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {A} = \left( \begin{array}{c c c c} 1 & 0 & - 1 & 0 \\ 0 & 1 & 0 & a \\ 1 & 1 & a & - 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ - 1 & 0 & a \\ 0 & a & - 1 \end{array} \right) = \left( \begin{array}{c c c} 2 & 0 & 1 - a \\ 0 & 1 + a ^ {2} & 1 - a \\ 1 - a & 1 - a & 3 + a ^ {2} \end{array} \right).</equation>求得<equation>|\mathbf{A}^{\mathrm{T}}\mathbf{A}| = (a^{2} + 3)(a + 1)^{2}</equation>. 因此，由<equation>|\mathbf{A}^{\mathrm{T}}\mathbf{A}| = 0</equation>可得<equation>a = -1</equation>（Ⅱ）由第（I）问可得，<equation>A^{\mathrm{T}}A = \left( \begin{array}{c c c} 2 & 0 & 2 \\ 0 & 2 & 2 \\ 2 & 2 & 4 \end{array} \right)</equation>从而<equation>A^{\mathrm{T}}A</equation>的特征多项式为<equation>| \lambda E - A ^ {\mathrm {T}} A | = \left| \begin{array}{c c c} \lambda - 2 & 0 & - 2 \\ 0 & \lambda - 2 & - 2 \\ - 2 & - 2 & \lambda - 4 \end{array} \right| = \lambda (\lambda - 2) (\lambda - 6).</equation><equation>A^{\mathrm{T}}A</equation>的特征值为6,2,0.

下面分别计算属于特征值6，2，0的特征向量.

当<equation>\lambda=6</equation>时，<equation>\begin{array}{l} 6 \boldsymbol {E} - \boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {A} = \left( \begin{array}{c c c} 4 & 0 & - 2 \\ 0 & 4 & - 2 \\ - 2 & - 2 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 0 & 2 & - 1 \\ 1 & 1 & - 1 \end{array} \right) \xrightarrow {r _ {3} - r _ {2}} \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 0 & 2 & - 1 \\ 1 & - 1 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} - r _ {1} + 2 r _ {3} ^ {*}} \binom {2} {r _ {2} ^ {*} \leftrightarrow r _ {3} ^ {*}} \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 1 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right), \\ \end{array}</equation>得<equation>\left\{ \begin{array}{l} 2x_{1} - x_{3} = 0, \\ x_{1} - x_{2} = 0. \end{array} \right.</equation>解得<equation>\xi_{1} = (1,1,2)^{\mathrm{T}}</equation>为该方程组的一个基础解系.

当<equation>\lambda=2</equation>时，<equation>2 E - A ^ {\mathrm {T}} A = \left( \begin{array}{c c c} 0 & 0 & - 2 \\ 0 & 0 & - 2 \\ - 2 & - 2 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right),</equation>得<equation>\left\{ \begin{array}{l} x_{1} + x_{2} = 0, \\ x_{3} = 0. \end{array} \right.</equation>解得<equation>\xi_{2} = (-1,1,0)^{\mathrm{T}}</equation>为该方程组的一个基础解系.

当<equation>\lambda=0</equation>时，<equation>0 \boldsymbol {E} - \boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {A} = \left( \begin{array}{c c c} - 2 & 0 & - 2 \\ 0 & - 2 & - 2 \\ - 2 & - 2 & - 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 2 \end{array} \right) \xrightarrow {r _ {3} - r _ {1} - r _ {2}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right),</equation>得<equation>\left\{ \begin{array}{l} x_{1} + x_{3} = 0, \\ x_{2} + x_{3} = 0. \end{array} \right.</equation>解得<equation>\xi_{3} = (-1, -1, 1)^{\mathrm{T}}</equation>为该方程组的一个基础解系.

由于实对称矩阵属于不同特征值的特征向量相互正交，故<equation>\xi_{1},\xi_{2},\xi_{3}</equation>相互正交.将<equation>\xi_{1},\xi_{2},\xi_{3}</equation>单位化，得<equation>\boldsymbol {\alpha} _ {1} = \frac {1}{\sqrt {6}} \left( \begin{array}{c} 1 \\ 1 \\ 2 \end{array} \right), \quad \boldsymbol {\alpha} _ {2} = \frac {1}{\sqrt {2}} \left( \begin{array}{c} - 1 \\ 1 \\ 0 \end{array} \right), \quad \boldsymbol {\alpha} _ {3} = \frac {1}{\sqrt {3}} \left( \begin{array}{c} - 1 \\ - 1 \\ 1 \end{array} \right).</equation>取<equation>Q = \left(\alpha_{1},\alpha_{2},\alpha_{3}\right)</equation>，则<equation>Q</equation>为正交矩阵，且<equation>Q^{\mathrm{T}} \left(A^{\mathrm{T}} A\right) Q = \left( \begin{array}{c c c} 6 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>因此，正交变换<equation>x = Qy</equation>将二次型<equation>f(x_{1},x_{2},x_{3})</equation>变成标准形<equation>f = 6y_{1}^{2} + 2y_{2}^{2}</equation>.

---

**2011年第13题 | 填空题 | 4分**

13. 若二次曲面的方程<equation>x^{2}+3y^{2}+z^{2}+2axy+2xz+2yz=4</equation>经正交变换化为<equation>y_{1}^{2}+4z_{1}^{2}=4</equation>, 则<equation>a=</equation>___.

**解析:**解设<equation>f=x^{2}+3 y^{2}+z^{2}+2 a x y+2 x z+2 y z</equation>.由题设知，二次型f在正交变换下的标准形为<equation>y_{1}^{2}+4 z_{1}^{2}</equation>从而二次型f的矩阵<equation>\left( \begin{array}{lll}1&a&1\\ a&3&1\\ 1&1&1 \end{array} \right)</equation>的特征值为0，1，4.因此，<equation>0 = \left| \begin{array}{c c c} 1 & a & 1 \\ a & 3 & 1 \\ 1 & 1 & 1 \end{array} \right| = - (a - 1) ^ {2}.</equation>解得 a=1.

---

**2010年第21题 | 解答题 | 11分**

21. (本题满分11分)

已知二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=\boldsymbol{x}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{x}</equation>在正交变换<equation>\boldsymbol{x}=\boldsymbol{Q} \boldsymbol{y}</equation>下的标准形为<equation>y_{1}^{2}+y_{2}^{2}</equation>，且Q的第三列为<equation>\left( \frac{\sqrt{2}}{2}, 0, \frac{\sqrt{2}}{2} \right)^{\mathrm{T}}</equation>I. 求矩阵 A；

II. 证明<equation>\boldsymbol{A}+\boldsymbol{E}</equation>为正定矩阵，其中E为3阶单位矩阵.

**答案:**<equation>(2 1) (\mathrm {I}) \boldsymbol {A} = \left( \begin{array}{c c c} \frac {1}{2} & 0 & - \frac {1}{2} \\ 0 & 1 & 0 \\ - \frac {1}{2} & 0 & \frac {1}{2} \end{array} \right);</equation>（Ⅱ）证明略.

**解析:**解（I）由于二次型在正交变换下的标准形的系数是二次型的矩阵的全部特征值，且<equation>f \left( x_{1}, x_{2}, x_{3} \right) = \boldsymbol{x}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{x} = \left( Q \boldsymbol{y} \right)^{\mathrm{T}} \boldsymbol{A} \boldsymbol{Q} \boldsymbol{y} = \boldsymbol{y}^{\mathrm{T}} \boldsymbol{Q}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{Q} \boldsymbol{y} = y_{1}^{2} + y_{2}^{2}</equation>，故A的特征值为1，1，0，且<equation>Q ^ {- 1} A Q = Q ^ {\mathrm {T}} A Q = \left( \begin{array}{c c c} 1 & & \\ & 1 & \\ & & 0 \end{array} \right).</equation>由上式可知<equation>Q</equation>的第三列<equation>\xi_{3}=\left(\frac{\sqrt{2}}{2},0,\frac{\sqrt{2}}{2}\right)^{\mathrm{T}}</equation>为A的对应于0的特征向量.由于实对称矩阵的对应于不同特征值的特征向量正交，故A的对应于特征值1的特征向量即为下面方程的非零解，<equation>\left(\frac {\sqrt {2}}{2}, 0, \frac {\sqrt {2}}{2}\right) \binom {x _ {1}} {x _ {2}} = 0,</equation>即<equation>x_{1}+x_{3}=0.</equation>解得 A的对应于特征值1的特征向量为<equation>x=k_{1}\left( \begin{array}{c}0\\ 1\\ 0 \end{array} \right)+k_{2}\left( \begin{array}{c}-1\\ 0\\ 1 \end{array} \right), k_{1}, k_{2}</equation>为不全为零的任意常数.

下面用两种方法求矩阵 A.

（法一）令<equation>\xi_{1} = (0,1,0)^{\mathrm{T}},\xi_{2} = \frac{\sqrt{2}}{2} (-1,0,1)^{\mathrm{T}}</equation>，则<equation>(\xi_{1},\xi_{2},\xi_{3})</equation>为正交矩阵且<equation>A(\xi_{1},\xi_{2},\xi_{3}) = (\xi_{1},\xi_{2},0)</equation>，于是<equation>\begin{aligned} \boldsymbol {A} &= \left(\boldsymbol {\xi} _ {1}, \boldsymbol {\xi} _ {2}, \mathbf {0}\right) \left(\boldsymbol {\xi} _ {1}, \boldsymbol {\xi} _ {2}, \boldsymbol {\xi} _ {3}\right) ^ {- 1} = \left(\boldsymbol {\xi} _ {1}, \boldsymbol {\xi} _ {2}, \mathbf {0}\right) \left(\boldsymbol {\xi} _ {1}, \boldsymbol {\xi} _ {2}, \boldsymbol {\xi} _ {3}\right) ^ {\mathrm {T}} \\ &= \left( \begin{array}{c c c} 0 & - \frac {\sqrt {2}}{2} & 0 \\ 1 & 0 & 0 \\ 0 & \frac {\sqrt {2}}{2} & 0  \right) \left( \begin{array}{c c c} 0 & 1 & 0 \\ - \frac {\sqrt {2}}{2} & 0 & \frac {\sqrt {2}}{2} \\ \frac {\sqrt {2}}{2} & 0 & \frac {\sqrt {2}}{2}  \right) &= \left( \begin{array}{c c c} \frac {1}{2} & 0 & - \frac {1}{2} \\ 0 & 1 & 0 \\ - \frac {1}{2} & 0 & \frac {1}{2}  \right). \end{aligned}</equation>（法二）令<equation>\alpha_{1} = (0,1,0)^{\mathrm{T}},\alpha_{2} = (-1,0,1)^{\mathrm{T}},\alpha_{3} = \sqrt{2}\xi_{3} = (1,0,1)^{\mathrm{T}}</equation>，则<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关且<equation>A(\alpha_{1},\alpha_{2},\alpha_{3}) = (\alpha_{1},\alpha_{2},0)</equation>，从而<equation>(\alpha_{1},\alpha_{2},\alpha_{3})</equation>可逆，且<equation>\begin{aligned} \boldsymbol {A} &= \left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\alpha} _ {2}, \mathbf {0}\right) \left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\alpha} _ {2}, \boldsymbol {\alpha} _ {3}\right) ^ {- 1} = \left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\alpha} _ {2}, \mathbf {0}\right) \left( \begin{array}{c c c} 0 & - 1 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 1  \right) ^ {- 1} \\ &= \left( \begin{array}{c c c} 0 & - 1 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0  \right) \left( \begin{array}{c c c} 0 & 1 & 0 \\ - \frac {1}{2} & 0 & \frac {1}{2} \\ \frac {1}{2} & 0 & \frac {1}{2}  \right) &= \left( \begin{array}{c c c} \frac {1}{2} & 0 & - \frac {1}{2} \\ 0 & 1 & 0 \\ - \frac {1}{2} & 0 & \frac {1}{2}  \right). \end{aligned}</equation>（Ⅱ）由于 A为实对称矩阵，即<equation>A^{\mathrm{T}}=A</equation>，故<equation>(A+E)^{\mathrm{T}}=A^{\mathrm{T}}+E^{\mathrm{T}}=A+E</equation>，从而 A+E为实对称矩阵.又<equation>Q ^ {- 1} (A + E) Q = Q ^ {- 1} A Q + E = \left( \begin{array}{c c c} 1 & & \\ & 1 & \\ & & 0 \end{array} \right) + \left( \begin{array}{c c c} 1 & & \\ & 1 & \\ & & 1 \end{array} \right) = \left( \begin{array}{c c c} 2 & & \\ & 2 & \\ & & 1 \end{array} \right),</equation>故 A+E的全部特征值为2，2，1.由实对称矩阵为正定矩阵的一个充要条件是其所有特征值都为正数知，A+E为正定矩阵，结论得证.

---

**2009年第21题 | 解答题 | 11分**

21. (本题满分11分)

设二次型<equation>f \left(x_{1}, x_{2}, x_{3}\right)=a x_{1}^{2}+a x_{2}^{2}+(a-1) x_{3}^{2}+2 x_{1} x_{3}-2 x_{2} x_{3}</equation>I. 求二次型 f的矩阵的所有特征值；

II. 若二次型 f的规范形为<equation>y_{1}^{2}+y_{2}^{2}</equation>，求 a的值.

**答案:**(21) ( I ) a, a - 2, a + 1; ( II ) a = 2.

**解析:**解（I）二次型<equation>f</equation>的矩阵为<equation>A=\left( \begin{array}{c c c} a & 0 & 1 \\ 0 & a & -1 \\ 1 & -1 & a-1 \end{array} \right).</equation>计算<equation>A</equation>的特征多项式<equation>|\lambda E - A|</equation>，得<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - a & 0 & - 1 \\ 0 & \lambda - a & 1 \\ - 1 & 1 & \lambda - a + 1  \right| \xlongequal {\text {按 第一 行 展 开}} (\lambda - a) \left[ (\lambda - a) (\lambda - a + 1) - 1 \right] - (\lambda - a) \\ &= (\lambda - a) (\lambda - a + 2) (\lambda - a - 1). \end{aligned}</equation>因此，<equation>A</equation>的特征值为<equation>a, a - 2, a + 1.</equation>（Ⅱ）由<equation>f</equation>的规范形为<equation>y_{1}^{2} + y_{2}^{2}</equation>知，<equation>A</equation>的特征值有两个正数，一个为零.0为最小的特征值.

由于<equation>a - 2 < a < a + 1</equation>，故可知<equation>a - 2 = 0</equation>，即<equation>a = 2</equation>

---


### 线性方程组

**2025年第6题 | 选择题 | 5分 | 答案: D**

6. 设<equation>\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4}</equation>是 n维向量，<equation>\alpha_{1},\alpha_{2}</equation>线性无关，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性相关，且<equation>\alpha_{1}+\alpha_{2}+\alpha_{4}=0</equation>在空间直角坐标系 Oxyz中，关于 x,y,z的方程组<equation>x\alpha_{1}+y\alpha_{2}+z\alpha_{3}=\alpha_{4}</equation>的几何图形是（    ）

A. 过原点的一个平面 B. 过原点的一条直线

C. 不过原点的一个平面 D. 不过原点的一条直线

答案: D

**解析:**解记<equation>A=\left(\alpha_{1},\alpha_{2},\alpha_{3}\right),w=\left(x,y,z\right)^{\mathrm{T}}</equation>，则方程组<equation>x\alpha_{1}+y\alpha_{2}+z\alpha_{3}=\alpha_{4}</equation>即<equation>A w=\alpha_{4}.</equation>由<equation>\alpha_{1},\alpha_{2}</equation>线性无关可得<equation>r(A)\geqslant 2</equation>，再由<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性相关可得<equation>r(A)\leqslant 2.</equation>由此可得<equation>r(A)=</equation>2.于是，方程组<equation>A w=0</equation>的基础解系中包含3-2=1个解向量.

由<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性相关可得，存在不全为零的数 a,b,c，使得<equation>a\alpha_{1}+b\alpha_{2}+c\alpha_{3}=\mathbf{0}</equation>即<equation>\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)\left( \begin{array}{c} a \\ b \\ c \end{array} \right)=\mathbf{0}.</equation>另一方面，由<equation>\alpha_{1}+\alpha_{2}+\alpha_{4}=0</equation>可得，<equation>-\alpha_{1}-\alpha_{2}=\alpha_{4}</equation>，于是，<equation>(\alpha_{1},\alpha_{2},\alpha_{3})\left( \begin{array}{c}-1\\ -1\\ 0\end{array} \right)=\alpha_{4},(-1,-1,0)^{\mathrm{T}}</equation>为方程组<equation>A w=\alpha_{4}</equation>的一个特解.

综合前面的分析，方程组<equation>A w=\alpha_{4}</equation>的通解为<equation>w=\left( \begin{array}{c} x \\ y \\ z \end{array} \right)=k\left( \begin{array}{c} a \\ b \\ c \end{array} \right)+\left( \begin{array}{c}-1 \\ -1 \\ 0 \end{array} \right)</equation>其中k为任意常数.该通解对应的几何图形为一条不过原点的直线，该直线的点向式方程为<equation>\frac{x+1}{a}=\frac{y+1}{b}=\frac{z}{c}</equation>参数方程为<equation>\left\{ \begin{array}{l l} x=a k-1, \\ y=b k-1, \\ z=c k. \end{array} \right.</equation>因此，应选D.

---

**2025年第15题 | 填空题 | 5分**

15. 设矩阵<equation>A=\left( \begin{array}{c c c} 4 & 2 & -3 \\ a & 3 & -4 \\ b & 5 & -7 \end{array} \right)</equation>，若方程组<equation>A^{2} x=0</equation>与<equation>A x=0</equation>不同解，则 a-b=___

**解析:**解 由于方程组<equation>A^{2}x=0</equation>与<equation>A x=0</equation>不同解，故A不可逆，否则A与<equation>A^{2}</equation>均可逆，从而方程组<equation>A^{2}x=0</equation>与<equation>A x=0</equation>均只有零解.进一步可得<equation>|A|=0.</equation>计算<equation>|A|</equation>可得<equation>| A | = \left| \begin{array}{c c c} 4 & 2 & - 3 \\ a & 3 & - 4 \\ b & 5 & - 7 \end{array} \right| \xlongequal {r _ {3} - r _ {1} - r _ {2}} \left| \begin{array}{c c c} 4 & 2 & - 3 \\ a & 3 & - 4 \\ b - 4 - a & 0 & 0 \end{array} \right| = (b - 4 - a) \left| \begin{array}{c c} 2 & - 3 \\ 3 & - 4 \end{array} \right| = b - 4 - a.</equation>又因为<equation>| A | = 0</equation>，所以<equation>a - b = -4.</equation>

---

**2024年第5题 | 选择题 | 5分 | 答案: B**

5. 在空间直角坐标系<equation>Oxyz</equation>中，三张平面<equation>\pi_{i}:a_{i}x + b_{i}y + c_{i}z = d_{i}</equation>（<equation>i = 1,2,3</equation>）的位置关系如图所示，记<equation>\alpha_{i} =</equation>（<equation>a_{i}, b_{i}, c_{i}</equation>）,<equation>\beta_{i}=(a_{i}, b_{i}, c_{i}, d_{i})</equation>，若<equation>\begin{aligned} r\left(  \alpha_{1} \\ \alpha_{2} \\ \alpha_{3}  \right)&=m, r\left(  \beta_{1} \\ \beta_{2} \\ \beta_{3}  \right)&=n \end{aligned}</equation>，则（    ）

A. m=1,n=2 B. m=n=2 C. m=2,n=3 D. m=n=3

答案: B

**解析:**解 联立三平面对应的平面方程，可得<equation>\left\{ \begin{array}{l} a_{1}x + b_{1}y + c_{1}z = d_{1}, \\ a_{2}x + b_{2}y + c_{2}z = d_{2}, \\ a_{3}x + b_{3}y + c_{3}z = d_{3}, \end{array} \right.</equation>该方程组的系数矩阵为<equation>\left( \begin{array}{l} \boldsymbol{\alpha}_{1} \\ \boldsymbol{\alpha}_{2} \\ \boldsymbol{\alpha}_{3} \end{array} \right)</equation>增广矩阵为<equation>\left( \begin{array}{l} \boldsymbol{\beta}_{1} \\ \boldsymbol{\beta}_{2} \\ \boldsymbol{\beta}_{3} \end{array} \right)</equation>.

由于三平面相交于一条直线，故联立所得线性方程组有无穷多解，从而<equation>r \left( \begin{array}{l} \boldsymbol {\alpha} _ {1} \\ \boldsymbol {\alpha} _ {2} \\ \boldsymbol {\alpha} _ {3} \end{array} \right) = r \left( \begin{array}{l} \boldsymbol {\beta} _ {1} \\ \boldsymbol {\beta} _ {2} \\ \boldsymbol {\beta} _ {3} \end{array} \right) < 3.</equation>又因为三个平面互不平行，所以三个平面的法向量两两线性无关，从而<equation>r \left( \begin{array}{l} \boldsymbol{\alpha}_{1} \\ \boldsymbol{\alpha}_{2} \\ \boldsymbol{\alpha}_{3} \end{array} \right) \geqslant 2.</equation>因此，<equation>\begin{aligned} r \left(  \boldsymbol{\alpha}_{1} \\ \boldsymbol{\alpha}_{2} \\ \boldsymbol{\alpha}_{3}  \right) &= r \left(  \boldsymbol{\beta}_{1} \\ \boldsymbol{\beta}_{2} \\ \boldsymbol{\beta}_{3}  \right) &= 2 \end{aligned}</equation>即<equation>m=n=2</equation>，应选B.

---

**2022年第6题 | 选择题 | 5分 | 答案: C**

6. 设 A,B为 n阶矩阵，E为单位矩阵，若方程组<equation>A x=0</equation>与<equation>B x=0</equation>同解，则（    ）

A. 方程组<equation>\left( \begin{array}{c c} A & O \\ E & B \end{array} \right) y=0</equation>只有零解

B. 方程组<equation>\left( \begin{array}{c c} E & A \\ O & A B \end{array} \right) y=0</equation>只有零解

C. 方程组<equation>\left( \begin{array}{c c} A & B \\ O & B \end{array} \right) y=0</equation>与<equation>\left( \begin{array}{c c} B & A \\ O & A \end{array} \right) y=0</equation>同解

D. 方程组<equation>\left( \begin{array}{c c} A B & B \\ O & A \end{array} \right) y=0</equation>与<equation>\left( \begin{array}{c c} B A & A \\ O & B \end{array} \right) y=0</equation>同解

答案: C

**解析:**解设<equation>y_{1}, y_{2}</equation>均为 n维列向量，<equation>y=\left( \begin{array}{c} y_{1} \\ y_{2} \end{array} \right).</equation>对<equation>\left( \begin{array}{cc} A & B \\ O & B \end{array} \right)</equation>和<equation>\left( \begin{array}{cc} B & A \\ O & A \end{array} \right)</equation>分别作初等行变换.

于是，<equation>\left( \begin{array}{ll}A&B\\ O&B \end{array} \right)y = 0</equation>等价于<equation>\left( \begin{array}{ll}A&O\\ O&B \end{array} \right)y = 0</equation>，即<equation>\left\{ \begin{array}{l l}Ay_{1} = 0,\\ By_{2} = 0. \end{array} \right.</equation>该方程组的解<equation>y</equation>满足<equation>y = \left( \begin{array}{l}y_{1}\\ y_{2} \end{array} \right)</equation>，其中<equation>y_{1}</equation>为<equation>Ax = 0</equation>的解，<equation>y_{2}</equation>为<equation>Bx = 0</equation>的解.

同理，<equation>\left( \begin{array}{cc}B&A\\ O&A \end{array} \right) y=0</equation>等价于<equation>\left( \begin{array}{cc}B&O\\ O&A \end{array} \right) y=0</equation>即<equation>\left\{ \begin{array}{l l} B y_{1}=0, \\ A y_{2}=0. \end{array} \right.</equation>该方程组的解y满足<equation>y=\left( \begin{array}{c}y_{1}\\ y_{2}\end{array} \right)</equation>其中<equation>y_{1}</equation>为Bx=0的解，<equation>y_{2}</equation>为Ax=0的解.

由于<equation>Ax = 0</equation>与<equation>Bx = 0</equation>同解，故选项C中的两个方程组同解.应选C.

下面说明选项A、B、D均不正确.

由于两方程组同解虽然能反映这两个方程组的系数矩阵的秩的大小关系，但并不能反映系数矩阵的秩的大小，故选项A、B的反例比较好找。要说明这两个方程组并不是只有零解，可以取<equation>A = B = O</equation>，则选项A、B中方程组的系数矩阵均不满秩，当然不可能只有零解.

同选项C的分析，选项D中的第一个方程组可化为<equation>\begin{aligned} \left( \begin{array}{c c} A B & B \\ O & A  \right) \left(  y _ {1} \\ y _ {2}  \right) &= \left( \begin{array}{c} A B y _ {1} + B y _ {2} \\ A y _ {2}  \right) &= \left( \begin{array}{c} 0 \\ 0  \right). \end{aligned}</equation>展开可得<equation>\left\{\begin{array}{l l}A B y_{1}+B y_{2}=0,\\ A y_{2}=0.\end{array}\right.</equation>由于<equation>A x=0</equation>与<equation>B x=0</equation>同解，故该方程组等价于<equation>\left\{\begin{array}{l l}A B y_{1}=0,\\ A y_{2}=0.\end{array}\right.</equation>同理可得，<equation>\left( \begin{array}{c c} B A & A \\ O & B \end{array} \right) y=0</equation>等价于<equation>\left\{\begin{array}{l l}B A y_{1}=0,\\ B y_{2}=0.\end{array}\right.</equation>但是，<equation>ABx = 0</equation>与<equation>BAx = 0</equation>并不一定同解.

取<equation>A = \left( \begin{array}{cc}0 & 1\\ 0 & 0 \end{array} \right),B = \left( \begin{array}{cc}0 & 1\\ 0 & 1 \end{array} \right)</equation>，则<equation>AB = \left( \begin{array}{cc}0 & 1\\ 0 & 0 \end{array} \right),BA = \left( \begin{array}{cc}0 & 0\\ 0 & 0 \end{array} \right).ABx = 0</equation>与<equation>BAx = 0</equation>不同解.

---

**2019年第6题 | 选择题 | 4分 | 答案: A**

6. 如图所示，有3张平面两两相交，交线相互平行，它们的方程<equation>a_{i1}x+a_{i2}y+a_{i3}z=d_{i}</equation>（<equation>i=1,2,3</equation>）组成的线性方程组的系数矩阵和增广矩阵分别记为<equation>\mathbf{A},\overline{\mathbf{A}}</equation>，则（    ）

A.<equation>r ( \mathbf{A})=2, r (\overline{{\mathbf{A}}})=3</equation>B.<equation>r ( \mathbf{A})=2, r (\overline{{\mathbf{A}}})=2</equation>C.<equation>r ( \mathbf{A})=1, r (\overline{{\mathbf{A}}})=2</equation>D.<equation>r ( \mathbf{A})=1, r (\overline{{\mathbf{A}}})=1</equation>

答案: A

**解析:**解 由于三平面两两相交，故线性方程组无解。又因为存在两个相交的平面，所以系数矩阵的秩等于2.方程组无解说明增广矩阵的秩等于3.

因此，应选A.

注 空间中三平面的位置关系（相交、平行、重合）与三元线性方程组的解的情况有如下对应关系.

<table border="1"><tr><td>秩的情况</td><td>解的情况</td><td>位置关系</td></tr><tr><td>r(系数矩阵)=1,r(增广矩阵)=1</td><td>有无穷多解</td><td>三平面重合</td></tr><tr><td>r(系数矩阵)=1,r(增广矩阵)=2</td><td>无解</td><td>三平面平行且三平面互异;或者两平面重合,第三个平面与它们平行</td></tr><tr><td>r(系数矩阵)=2,r(增广矩阵)=2</td><td>有无穷多解</td><td>两平面相交,第三个平面与其中一个平面重合;或者三平面互异,相交于一条直线</td></tr><tr><td>r(系数矩阵)=2,r(增广矩阵)=3</td><td>无解</td><td>两平面平行,第三个平面与这两个平面分别相交;或者三平面互不平行,两两相交</td></tr><tr><td>r(系数矩阵)=3,r(增广矩阵)=3</td><td>有唯一解</td><td>三平面相交于一点</td></tr></table>

---

**2019年第13题 | 填空题 | 4分**

13. 设<equation>A=\left( \alpha_{1},\alpha_{2},\alpha_{3} \right)</equation>为3阶矩阵. 若<equation>\alpha_{1},\alpha_{2}</equation>线性无关，且<equation>\alpha_{3}=-\alpha_{1}+2\alpha_{2}</equation>，则线性方程组<equation>A x=0</equation>的通解为___

**答案:**<equation>k(-1,2,-1)^{\mathrm{T}}</equation>，其中<equation>k</equation>为任意常数.

**解析:**解由<equation>\alpha_{1},\alpha_{2}</equation>线性无关可得<equation>r(A)\geqslant 2.</equation>由<equation>\alpha_{3}=-\alpha_{1}+2\alpha_{2}</equation>可得<equation>-\alpha_{1}+2\alpha_{2}-\alpha_{3}=0</equation>从而<equation>\alpha_{1},</equation><equation>\alpha_{2},\alpha_{3}</equation>线性相关，于是<equation>r(A)\leqslant 2.</equation>因此，<equation>r(A)=2.</equation>由系数矩阵的秩与解集的秩的关系可知，<equation>Ax=</equation>0的基础解系中只包含3-2=1个解向量.

又因为<equation>-\alpha_{1} + 2\alpha_{2} - \alpha_{3} = 0</equation>可写为<equation>\left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) \left( \begin{array}{c} - 1 \\ 2 \\ - 1 \end{array} \right) = \mathbf {0},</equation>所以<equation>(-1,2,-1)^{\mathrm{T}}</equation>是<equation>Ax = 0</equation>的一个解，也是<equation>Ax = 0</equation>的一个基础解系.

综上所述，<equation>Ax = 0</equation>的通解为<equation>k(-1,2,-1)^{\mathrm{T}}</equation>，其中<equation>k</equation>为任意常数.

---

**2018年第21题 | 解答题 | 11分**

21. （本题满分11分）

已知 a是常数，且矩阵<equation>A=\left( \begin{array}{c c c}1&2&a\\ 1&3&0\\ 2&7&-a \end{array} \right)</equation>可经初等列变换化为矩阵<equation>B=\left( \begin{array}{c c c}1&a&2\\ 0&1&1\\ -1&1&1 \end{array} \right).</equation>I. 求 a；

II. 求满足<equation>A P=B</equation>的可逆矩阵<equation>P.</equation>

**答案:**( I ) a = 2;

（Ⅱ）满足<equation>A P=B</equation>的可逆矩阵为<equation>\boldsymbol {P} = \left( \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right),</equation>其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数，且<equation>k_{2} \neq k_{3}</equation>.

**解析:**解（I）由于矩阵 A可经初等列变换化为矩阵 B，故矩阵方程 AX=B有解.于是，<equation>r(A)= r(A,B).</equation>对（A,B）作初等行变换.<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {B}) = \left( \begin{array}{c c c c c c} 1 & 2 & a & 1 & a & 2 \\ 1 & 3 & 0 & 0 & 1 & 1 \\ 2 & 7 & - a & - 1 & 1 & 1 \end{array} \right) \xrightarrow {r _ {2} - r _ {1}} \left( \begin{array}{c c c c c c} 1 & 2 & a & 1 & a & 2 \\ 0 & 1 & - a & - 1 & 1 - a & - 1 \\ 0 & 3 & - 3 a & - 3 & 1 - 2 a & - 3 \end{array} \right) \\ \xrightarrow {r _ {1} - 2 r _ {2} ^ {*}} \frac {1}{r _ {3} ^ {*} - 3 r _ {2} ^ {*}} \left( \begin{array}{c c c c c c} 1 & 0 & 3 a & 3 & 3 a - 2 & 4 \\ 0 & 1 & - a & - 1 & 1 - a & - 1 \\ 0 & 0 & 0 & 0 & a - 2 & 0 \end{array} \right). \\ \end{array}</equation>当且仅当<equation>a = 2</equation>时，<equation>r(\mathbf{A}) = r(\mathbf{A},\mathbf{B}) = 2.</equation>或者，由矩阵<equation>\mathbf{A}</equation>可经初等列变换化为矩阵<equation>\mathbf{B}</equation>可知，<equation>\mathbf{A}</equation>的列秩等于<equation>\mathbf{B}</equation>的列秩，从而<equation>r(\mathbf{A})=r(\mathbf{B})</equation>同上面的计算可知<equation>r(\mathbf{A})=2</equation>，当且仅当<equation>a=2</equation>时，<equation>r(\mathbf{A})=r(\mathbf{B}).</equation>因此，<equation>a=2.</equation>（Ⅱ）当 a=2时，<equation>(\boldsymbol {A}, \boldsymbol {B}) \rightarrow \left(\begin{array}{c c c c c c}1&0&6&3&4&4\\0&1&- 2&- 1&- 1&- 1\\0&0&0&0&0&0\end{array}\right).</equation><equation>AX = B</equation>等价于<equation>\left( \begin{array}{c c c} 1 & 0 & 6 \\ 0 & 1 & -2 \\ 0 & 0 & 0 \end{array} \right) X = \left( \begin{array}{c c c} 3 & 4 & 4 \\ -1 & -1 & -1 \\ 0 & 0 & 0 \end{array} \right)</equation>.记<equation>\left( \begin{array}{c c c} 1 & 0 & 6 \\ 0 & 1 & -2 \\ 0 & 0 & 0 \end{array} \right) = A^{\prime}</equation>.方程组<equation>A^{\prime}x = 0</equation>的一个基础解系为<equation>(-6,2,1)^{\mathrm{T}}</equation>.于是，方程组<equation>A^{\prime}x = (3, -1,0)^{\mathrm{T}}</equation>的通解为<equation>x_{1} = k_{1}(-6,2,1)^{\mathrm{T}} + (3, -1,0)^{\mathrm{T}}</equation>，其中<equation>k_{1}</equation>为任意常数；方程组<equation>A^{\prime}x = (4, -1,0)^{\mathrm{T}}</equation>的通解为<equation>x_{2} = k_{2}(-6,2,1)^{\mathrm{T}} + (4, -1,0)^{\mathrm{T}}</equation>，其中<equation>k_{2}</equation>为任意常数；方程组<equation>A^{\prime}x = (4, -1,0)^{\mathrm{T}}</equation>的通解为<equation>x_{3} = k_{3}(-6,2,1)^{\mathrm{T}} + (4, -1,0)^{\mathrm{T}}</equation>，其中<equation>k_{3}</equation>为任意常数.

因此，矩阵方程<equation>A X=B</equation>的通解为<equation>\boldsymbol {X} = \left( \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right),</equation>其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数.

若可逆矩阵 P满足 AP=B，则<equation>\boldsymbol {P} = \left( \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right),</equation>且<equation>| P| \neq 0.</equation>由于<equation>| \boldsymbol {P} | = \left| \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right| = \left| \begin{array}{c c c} 0 & 1 & 1 \\ - 1 & - 1 & - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right| = \left| \begin{array}{c c c} 0 & 1 & 1 \\ - 1 & 0 & 0 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right| = k _ {3} - k _ {2},</equation>故当<equation>k_{2}\neq k_{3}</equation>时，<equation>P</equation>可逆.

因此，满足<equation>A P=B</equation>的可逆矩阵为<equation>\boldsymbol {P} = \left( \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right),</equation>其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数，且<equation>k_{2} \neq k_{3}</equation>

---

**2017年第20题 | 解答题 | 11分**

20. (本题满分11分)

设3阶矩阵<equation>A=\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)</equation>有3个不同的特征值，且<equation>\alpha_{3}=\alpha_{1}+2\alpha_{2}.</equation>I. 证明<equation>r(A)=2;</equation>II. 设<equation>\beta=\alpha_{1}+\alpha_{2}+\alpha_{3}</equation>，求方程组<equation>A x=\beta</equation>的通解.

**答案:**（I）证明略；

（Ⅱ）<equation>k ( 1, 2,-1 )^{\mathrm{T}}+( 1, 1, 1 )^{\mathrm{T}}</equation>为线性方程组<equation>A x=\beta</equation>的通解，其中 k为任意常数.

**解析:**解（I）（法一）由于 A有3个不同的特征值<equation>\lambda_{1},\lambda_{2},\lambda_{3}</equation>，故 A相似于对角矩阵，且至多仅有一个零特征值.该对角矩阵的秩<equation>\geqslant 2</equation>，于是<equation>r(A)\geqslant 2.</equation>又因为<equation>\alpha_{3} = \alpha_{1} + 2\alpha_{2}</equation>，所以<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性相关，<equation>|A| = 0.</equation>由于<equation>|A| = \lambda_{1}\lambda_{2}\lambda_{3}</equation>，故<equation>A</equation>有一个特征值为零.

因此，<equation>r ( A ) = 2.</equation>（法二）也可以如下证明0是<equation>A</equation>的一个特征值.

由<equation>\boldsymbol{\alpha}_{3}=\boldsymbol{\alpha}_{1}+2\boldsymbol{\alpha}_{2}</equation>知<equation>\left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\alpha} _ {2}, \boldsymbol {\alpha} _ {3}\right) \left( \begin{array}{c} 1 \\ 2 \\ - 1 \end{array} \right) = \mathbf {0} = 0 \left( \begin{array}{c} 1 \\ 2 \\ - 1 \end{array} \right).</equation>于是，0是<equation>A</equation>的一个特征值，<equation>(1,2,-1)^{\mathrm{T}}</equation>是<equation>A</equation>的属于特征值0的一个特征向量.

其余同法一.

（Ⅱ）考虑<equation>Ax = 0</equation>. 由于<equation>r(A) = 2</equation>，故<equation>Ax = 0</equation>的基础解系中只包含一个向量. 又因为<equation>\alpha_{3} = \alpha_{1} + 2\alpha_{2}</equation>，所以<equation>(\alpha_{1},\alpha_{2},\alpha_{3})(1,2, - 1)^{\mathrm{T}} = 0</equation>，即<equation>(1,2, - 1)^{\mathrm{T}}</equation>是该齐次线性方程组的一个基础解系.

由于<equation>\boldsymbol{\beta} = \boldsymbol{\alpha}_1 + \boldsymbol{\alpha}_2 + \boldsymbol{\alpha}_3</equation>，即<equation>(\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2, \boldsymbol{\alpha}_3)(1, 1, 1)^{\mathrm{T}} = \boldsymbol{\beta}</equation>，故<equation>(1, 1, 1)^{\mathrm{T}}</equation>是<equation>Ax = \boldsymbol{\beta}</equation>的一个特解.

因此，<equation>k(1,2, - 1)^{\mathrm{T}} + (1,1,1)^{\mathrm{T}}</equation>为线性方程组<equation>Ax = \beta</equation>的通解，其中<equation>k</equation>为任意常数.

---

**2016年第20题 | 解答题 | 11分**

20. （本题满分11分）

设矩阵<equation>A=\left( \begin{array}{c c c}1&-1&-1\\ 2&a&1\\ -1&1&a \end{array} \right), B=\left( \begin{array}{c c}2&2\\ 1&a\\ -a-1&-2 \end{array} \right).</equation>当 a为何值时，方程<equation>AX=B</equation>无解、有唯一解、有无穷多

解？在有解时，求解此方程.

**答案:**当 a = -2时，<equation>A X=B</equation>无解；

当 a=1时，<equation>A X=B</equation>有无穷多解，<equation>X=\left( \begin{array}{c c}1&1\\ -1&-1\\ 0&0 \end{array} \right)+\left( \begin{array}{c c}0&0\\ -c_{1}&-c_{2}\\ c_{1}&c_{2} \end{array} \right)</equation>其中<equation>c_{1}, c_{2}</equation>为任意常数；当 a≠-2且 a≠1时，<equation>A X=B</equation>有唯一解<equation>X=\left( \begin{array}{c c}1&\frac{3 a}{a+2}\\ 0&\frac{a-4}{a+2}\\ -1&0 \end{array} \right).</equation>

**解析:**对矩阵（A,B）作如下行变换<equation>(\boldsymbol {A}, \boldsymbol {B}) = \left( \begin{array}{c c c c c} 1 & - 1 & - 1 & 2 & 2 \\ 2 & a & 1 & 1 & a \\ - 1 & 1 & a & - a - 1 & - 2 \end{array} \right) \xrightarrow [ r _ {3} + r _ {1} ]{r _ {2} - 2 r _ {1}} \left( \begin{array}{c c c c c} 1 & - 1 & - 1 & 2 & 2 \\ 0 & a + 2 & 3 & - 3 & a - 4 \\ 0 & 0 & a - 1 & 1 - a & 0 \end{array} \right). (*)</equation>当<equation>a = -2</equation>时，<equation>r(\mathbf{A}) = 2, r(\mathbf{A},\mathbf{B}) = 3</equation>，此时<equation>\mathbf{AX} = \mathbf{B}</equation>无解.

当 a=1时，<equation>r(\mathbf{A})=r(\mathbf{A},\mathbf{B})=2</equation>，此时<equation>AX=B</equation>有无穷多解，其解即方程组<equation>\left\{ \begin{array}{l l} A x_{1}=b_{1}, \\ A x_{2}=b_{2} \end{array} \right.</equation>的解，其中<equation>x_{k}</equation>和<equation>b_{k}</equation>分别为X和B的第k列（ k=1,2）.将 a=1代入（<equation>\ast</equation>）式，得到<equation>(\boldsymbol {A}, \boldsymbol {B}) \xrightarrow [ r _ {3} + r _ {1} ]{r _ {2} - 2 r _ {1}} \left( \begin{array}{c c c c c} 1 & - 1 & - 1 & 2 & 2 \\ 0 & 3 & 3 & - 3 & - 3 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {1} + r _ {2} ]{r _ {2} \times \frac {1}{3}} \left( \begin{array}{c c c c c} 1 & 0 & 0 & 1 & 1 \\ 0 & 1 & 1 & - 1 & - 1 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right).</equation>于是<equation>x_{1}=c_{1}\left( \begin{array}{c}0\\ -1\\ 1 \end{array} \right)+\left( \begin{array}{c}1\\ -1\\ 0 \end{array} \right)</equation>，其中<equation>c_{1}</equation>为任意常数；<equation>x_{2}=c_{2}\left( \begin{array}{c}0\\ -1\\ 1 \end{array} \right)+\left( \begin{array}{c}1\\ -1\\ 0 \end{array} \right)</equation>，其中<equation>c_{2}</equation>为任意常数.因此<equation>A X=B</equation>的解为<equation>X = \left( \begin{array}{c c} 1 & 1 \\ -1 & -1 \\ 0 & 0 \end{array} \right) + \left( \begin{array}{c c} 0 & 0 \\ -c_1 & -c_2 \\ c_1 & c_2 \end{array} \right),</equation>其中<equation>c_{1}, c_{2}</equation>为任意常数，

或者写为<equation>X = \left( \begin{array}{c c} 1 & 1 \\ - c_{1} - 1 & - c_{2} - 1 \\ c_{1} & c_{2} \end{array} \right),</equation>其中<equation>c_{1}, c_{2}</equation>为任意常数.

当<equation>a \neq -2</equation>且<equation>a \neq 1</equation>时，<equation>r(\mathbf{A}) = r(\mathbf{A},\mathbf{B}) = 3</equation>，此时<equation>AX = B</equation>有唯一解.由（\*）式可知，<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {B}) \xrightarrow [ r _ {3} + r _ {1} ]{r _ {2} - 2 r _ {1}} \left( \begin{array}{c c c c c} 1 & - 1 & - 1 & 2 & 2 \\ 0 & a + 2 & 3 & - 3 & a - 4 \\ 0 & 0 & a - 1 & 1 - a & 0 \end{array} \right) \xrightarrow [ r _ {2} - \frac {3}{a + 2} r _ {3} ]{r _ {2} \times \frac {1}{a + 2}} \left( \begin{array}{c c c c c} 1 & - 1 & - 1 & 2 & 2 \\ 0 & 1 & 0 & 0 & \frac {a - 4}{a + 2} \\ 0 & 0 & 1 & - 1 & 0 \end{array} \right) \\ \xrightarrow [ r _ {1} + r _ {2} ]{r _ {1} + r _ {3}} \left( \begin{array}{c c c c c} 1 & 0 & 0 & 1 & \frac {3 a}{a + 2} \\ 0 & 1 & 0 & 0 & \frac {a - 4}{a + 2} \\ 0 & 0 & 1 & - 1 & 0 \end{array} \right). \\ \end{array}</equation>解得<equation>\boldsymbol {X} = \left( \begin{array}{c c} 1 & \frac {3 a}{a + 2} \\ 0 & \frac {a - 4}{a + 2} \\ - 1 & 0 \end{array} \right).</equation>

---

**2015年第5题 | 选择题 | 4分 | 答案: D**

5. 设矩阵<equation>A=\left( \begin{array}{c c c} {1} & {1} & {1} \\ {1} & {2} & {a} \\ {1} & {4} & {a^{2}} \\ \end{array} \right), b=\left( \begin{array}{c} {1} \\ {d} \\ {d^{2}} \\ \end{array} \right).</equation>若集合<equation>\Omega =\{1,2\}</equation>，则线性方程组<equation>A x=b</equation>有无穷多解的充分必要条件为（    ）

A. a<equation>\notin \Omega</equation>, d<equation>\notin \Omega</equation>B. a<equation>\notin \Omega</equation>, d<equation>\in \Omega</equation>C. a<equation>\in \Omega</equation>, d<equation>\notin \Omega</equation>D. a<equation>\in \Omega</equation>, d<equation>\in \Omega</equation>

答案: D

**解析:**解 （法一）对（A，b）作初等行变换.<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 1 & 2 & a & d \\ 1 & 4 & a ^ {2} & d ^ {2} \end{array} \right) \xrightarrow [ r _ {3} - r _ {1} ]{r _ {2} - r _ {1}} \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 0 & 1 & a - 1 & d - 1 \\ 0 & 3 & a ^ {2} - 1 & d ^ {2} - 1 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {*} - 3 r _ {2} ^ {*}} \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 0 & 1 & a - 1 & d - 1 \\ 0 & 0 & a ^ {2} - 3 a + 2 & d ^ {2} - 3 d + 2 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每作一次初等行变换，加一个<equation>*.</equation>）

由此可见，<equation>r ( \mathbf{A})=r ( \mathbf{A},\mathbf{b})<3</equation>当且仅当<equation>a^{2}-3 a+2=0</equation>且<equation>d^{2}-3 d+2=0</equation>即 a=1或a=2，且 d=1或d=2，也即 a<equation>\in\Omega</equation>，d<equation>\in\Omega.</equation>因此，<equation>a\in \Omega</equation>，<equation>d\in \Omega</equation>是<equation>Ax = b</equation>有无穷多解的充分必要条件.应选D.

（法二）当 a<equation>\in\Omega</equation>，d<equation>\in\Omega</equation>时，<equation>r ( \mathbf{A} )=r ( \mathbf{A},\mathbf{b} )=2<3</equation>，故 a<equation>\in\Omega</equation>，d<equation>\in\Omega</equation>是<equation>A x=b</equation>有无穷多解的充分条件.

当<equation>Ax = b</equation>有无穷多解时，<equation>r(A) = r(A, b) < 3</equation>，从而<equation>r(A) < 3</equation>，<equation>|A| = 0</equation>. 由于<equation>|A|</equation>为范德蒙德行列式，故<equation>|A| = 0</equation>当且仅当<equation>a = 1</equation>或<equation>a = 2</equation>，即<equation>a \in \Omega</equation>.此时，若<equation>r(A, b) = r(A) < 3</equation>，则<equation>(1, d, d^{2})^{\mathrm{T}}</equation>与<equation>(1, 1, 1)^{\mathrm{T}}</equation>和<equation>(1, 2, 4)^{\mathrm{T}}</equation>线性相关，从而<equation>\left| \begin{array}{c c c} 1 & 1 & 1 \\ 1 & 2 & d \\ 1 & 4 & d^{2} \end{array} \right| = 0</equation>.再次由范德蒙德行列式的性质可推出<equation>d = 1</equation>或<equation>d = 2</equation>，即<equation>d \in \Omega</equation>.

因此，<equation>a\in \Omega</equation>，<equation>d\in \Omega</equation>是<equation>Ax = b</equation>有无穷多解的充分必要条件.应选D.

（法三）排除法.我们可以把简单的值代入各选项，然后根据<equation>A x=b</equation>是否有无穷多解来排除错误选项.

选项A：代入<equation>a=0</equation>，<equation>d=0</equation>，<equation>r(\mathbf{A})=r(\mathbf{A},\mathbf{b})=3</equation>，不符合题意.

选项B：代入<equation>a=0</equation>，<equation>d\in\{1,2\}</equation>，<equation>r(\mathbf{A})=r(\mathbf{A},\mathbf{b})=3</equation>，不符合题意.

选项C：代入<equation>a \in \{1,2\}</equation>，<equation>d=0</equation>，<equation>r(\mathbf{A},\mathbf{b})=3</equation>，<equation>r(\mathbf{A})=2</equation>，不符合题意.

由上可见，选项A、B、C均不是正确选项.由排除法知，应选D.

