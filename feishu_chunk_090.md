#### 线性微分方程的解的结构

**2013年第10题 | 填空题 | 4分**

10. 已知<equation>y_{1}=\mathrm{e}^{3 x}-x \mathrm{e}^{2 x}, y_{2}=\mathrm{e}^{x}-x \mathrm{e}^{2 x}, y_{3}=-x \mathrm{e}^{2 x}</equation>是某二阶常系数非齐次线性微分方程的3个解，则该方程的通解为 y=___

**答案:**<equation>C_{1}\mathrm{e}^{3x} + C_{2}\mathrm{e}^{x} - x\mathrm{e}^{2x}</equation>，其中<equation>C_{1}, C_{2}</equation>为任意常数.

**解析:**解 由题设知，<equation>y_{1}-y_{3}=\mathrm{e}^{3 x}, y_{2}-y_{3}=\mathrm{e}^{x}</equation>是对应的齐次线性微分方程的两个线性无关的解。又<equation>y_{3}=-x\mathrm{e}^{2 x}</equation>是非齐次线性微分方程的解，故所求通解为<equation>y = C _ {1} \mathrm {e} ^ {3 x} + C _ {2} \mathrm {e} ^ {x} - x \mathrm {e} ^ {2 x},</equation>其中<equation>C_{1}, C_{2}</equation>为任意常数.

---


## 线性代数


### 二次型

**2025年第5题 | 选择题 | 5分 | 答案: B**

5. 二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=x_{1}^{2}+2 x_{1} x_{2}+2 x_{1} x_{3}</equation>的正惯性指数为（    )

A.0 B.1 C.2 D.3

答案: B

**解析:**解 （法一）配方法.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= x _ {1} ^ {2} + 2 x _ {1} x _ {2} + 2 x _ {1} x _ {3} = \left(x _ {1} + x _ {2} + x _ {3}\right) ^ {2} - x _ {2} ^ {2} - x _ {3} ^ {2} - 2 x _ {2} x _ {3} \\ &= \left(x _ {1} + x _ {2} + x _ {3}\right) ^ {2} - \left(x _ {2} + x _ {3}\right) ^ {2}. \end{aligned}</equation>令<equation>\left\{ \begin{array}{l l} y_{1}=x_{1}+x_{2}+x_{3}, \\ y_{2}=x_{2}+x_{3}, \\ y_{3}=x_{3}, \end{array} \right.</equation>则该变换为可逆线性变换，在该变换下 f（<equation>x_{1}, x_{2}, x_{3}</equation>）化为标准形<equation>y_{1}^{2}-y_{2}^{2}.</equation>因此，<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>的正惯性指数为1，应选B.

（法二）特征值法.<equation>f\left(x_{1}, x_{2}, x_{3}\right)</equation>对应的实对称矩阵<equation>A = \left( \begin{array}{c c c} 1 & 1 & 1 \\ 1 & 0 & 0 \\ 1 & 0 & 0 \end{array} \right)</equation>.

计算 A的特征值.<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - 1 & - 1 & - 1 \\ - 1 & \lambda & 0 \\ - 1 & 0 & \lambda  \right| \xlongequal {c _ {3} + \lambda c _ {1}} \left| \begin{array}{c c c} \lambda - 1 & - 1 & \lambda^ {2} - \lambda - 1 \\ - 1 & \lambda & - \lambda \\ - 1 & 0 & 0  \right| &= (- 1) \cdot \left| \begin{array}{c c} - 1 & \lambda^ {2} - \lambda - 1 \\ \lambda & - \lambda  \right| \\ &= - \lambda \left| \begin{array}{c c} - 1 & \lambda^ {2} - \lambda - 1 \\ 1 & - 1  \right| &= \lambda \left(\lambda^ {2} - \lambda - 2\right) = \lambda (\lambda - 2) (\lambda + 1). \end{aligned}</equation>A的特征值为2，-1,0,A共有一个正特征值因此，<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>的正惯性指数为1，应选B.

---

**2024年第15题 | 填空题 | 5分**

15. 设实矩阵<equation>A=\left( \begin{array}{cc} a+1 & a \\ a & a \end{array} \right)</equation>，若对任意实向量<equation>\alpha=\binom{x_{1}}{x_{2}}</equation><equation>\beta=\binom{y_{1}}{y_{2}}</equation><equation>(\alpha^{\mathrm{T}}A\beta)^{2}\leqslant\alpha^{\mathrm{T}}A\alpha\cdot\beta^{\mathrm{T}}A\beta</equation>都成立，则 a的取值范围是___

**解析:**解（法一）先将 A通过合同变换化为对角矩阵.令<equation>P=\left( \begin{array}{c c}1&0\\ -1&1 \end{array} \right)</equation>，则<equation>\boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} = \left( \begin{array}{c c} 1 & - 1 \\ 0 & 1 \end{array} \right) \left( \begin{array}{c c} a + 1 & a \\ a & a \end{array} \right) \left( \begin{array}{c c} 1 & 0 \\ - 1 & 1 \end{array} \right) = \left( \begin{array}{c c} 1 & 0 \\ 0 & a \end{array} \right).</equation>令<equation>\gamma_{1}=\binom{w_{1}}{w_{2}}</equation>满足<equation>P\gamma_{1}=\alpha, \gamma_{2}=\binom{z_{1}}{z_{2}}</equation>满足<equation>P\gamma_{2}=\beta.</equation>由于<equation>\alpha, \beta</equation>为任意实向量，故<equation>\gamma_{1},\gamma_{2}</equation>也为任意实向量.于是，<equation>\boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {\beta} = \gamma_ {1} ^ {\mathrm {T}} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} \gamma_ {2} = \left(w _ {1}, w _ {2}\right) \binom {1} {0} \binom {z _ {1}} {z _ {2}} = w _ {1} z _ {1} + a w _ {2} z _ {2},</equation><equation>\boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {\alpha} = \gamma_ {1} ^ {\mathrm {T}} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} \boldsymbol {\gamma} _ {1} = \left(w _ {1}, w _ {2}\right) \binom {1} {0} \binom {0} {a} \binom {w _ {1}} {w _ {2}} = w _ {1} ^ {2} + a w _ {2} ^ {2},</equation><equation>\boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {\beta} = \gamma_ {2} ^ {\mathrm {T}} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} \gamma_ {2} = \left(z _ {1}, z _ {2}\right) \binom {1} {0} \binom {0} {a} \binom {z _ {1}} {z _ {2}} = z _ {1} ^ {2} + a z _ {2} ^ {2}.</equation><equation>\left(\boldsymbol{\alpha}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{\beta}\right)^{2} \leqslant \boldsymbol{\alpha}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{\alpha} \cdot \boldsymbol{\beta}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{\beta}</equation>对任意实向量<equation>\alpha, \beta</equation>恒成立等价于<equation>\left(w_{1}z_{1}+aw_{2}z_{2}\right)^{2} \leqslant \left(w_{1}^{2}+aw_{2}^{2}\right)\left(z_{1}^{2}+az_{2}^{2}\right)</equation>对任意<equation>w_{1}, w_{2}, z_{1}, z_{2}</equation>恒成立.

展开<equation>(w_{1}z_{1} + aw_{2}z_{2})^{2}\leqslant (w_{1}^{2} + aw_{2}^{2})(z_{1}^{2} + az_{2}^{2})</equation>可得，<equation>w _ {1} ^ {2} z _ {1} ^ {2} + a ^ {2} w _ {2} ^ {2} z _ {2} ^ {2} + 2 a w _ {1} z _ {1} w _ {2} z _ {2} \leqslant w _ {1} ^ {2} z _ {1} ^ {2} + a ^ {2} w _ {2} ^ {2} z _ {2} ^ {2} + a w _ {1} ^ {2} z _ {2} ^ {2} + a w _ {2} ^ {2} z _ {1} ^ {2}.</equation>整理（1）式可得<equation>a \left(w_{1} z_{2}-w_{2} z_{1}\right)^{2} \geqslant 0.</equation>对任意<equation>w_{1}, w_{2}, z_{1}, z_{2}</equation>，该式恒成立当且仅当<equation>a \geqslant 0.</equation>因此，<equation>a</equation>的取值范围是<equation>[0, +\infty)</equation>.

（法二）整理<equation>(\alpha^{\mathrm{T}}A\beta)^{2}\leqslant \alpha^{\mathrm{T}}A\alpha \cdot \beta^{\mathrm{T}}A\beta</equation>可得<equation>\alpha^ {\mathrm {T}} A \beta \alpha^ {\mathrm {T}} A \beta - \alpha^ {\mathrm {T}} A \alpha \beta^ {\mathrm {T}} A \beta \leqslant 0, \quad \text {即} \alpha^ {\mathrm {T}} A \left(\beta \alpha^ {\mathrm {T}} - \alpha \beta^ {\mathrm {T}}\right) A \beta \leqslant 0.</equation>计算可得<equation>\boldsymbol {\beta} \boldsymbol {\alpha} ^ {\mathrm {T}} - \alpha \boldsymbol {\beta} ^ {\mathrm {T}} = \left( \begin{array}{c c} x _ {1} y _ {1} & x _ {2} y _ {1} \\ x _ {1} y _ {2} & x _ {2} y _ {2} \end{array} \right) - \left( \begin{array}{c c} x _ {1} y _ {1} & x _ {1} y _ {2} \\ x _ {2} y _ {1} & x _ {2} y _ {2} \end{array} \right) = \left( \begin{array}{c c} 0 & x _ {2} y _ {1} - x _ {1} y _ {2} \\ x _ {1} y _ {2} - x _ {2} y _ {1} & 0 \end{array} \right).</equation>记<equation>z = x_{2}y_{1} - x_{1}y_{2}</equation>，则<equation>\beta \alpha^{\mathrm{T}} - \alpha \beta^{\mathrm{T}} = \left( \begin{array}{cc}0 & z\\ -z & 0 \end{array} \right)</equation>.

计算<equation>A(\beta\alpha^{\mathrm{T}}-\alpha\beta^{\mathrm{T}})A</equation>可得<equation>\begin{aligned} \boldsymbol {A} \left(\boldsymbol {\beta} \boldsymbol {\alpha} ^ {\mathrm {T}} - \boldsymbol {\alpha} \boldsymbol {\beta} ^ {\mathrm {T}}\right) \boldsymbol {A} &= \left( \begin{array}{c c} a + 1 & a \\ a & a  \right) \left( \begin{array}{c c} 0 & z \\ - z & 0  \right) \left( \begin{array}{c c} a + 1 & a \\ a & a  \right) \\ &= \left( \begin{array}{c c} - a z & (a + 1) z \\ - a z & a z  \right) \left( \begin{array}{c c} a + 1 & a \\ a & a  \right) &= \left( \begin{array}{c c} 0 & a z \\ - a z & 0  \right). \end{aligned}</equation>于是，<equation>\begin{aligned} \boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {A} \left(\boldsymbol {\beta} \boldsymbol {\alpha} ^ {\mathrm {T}} - \boldsymbol {\alpha} \boldsymbol {\beta} ^ {\mathrm {T}}\right) \boldsymbol {A} \boldsymbol {\beta} &= \left(x _ {1}, x _ {2}\right) \binom {0} {- a z} \binom {a z} {0} \binom {y _ {1}} {y _ {2}} = \left(- a x _ {2} z, a x _ {1} z\right) \binom {y _ {1}} {y _ {2}} \\ &= a x _ {1} y _ {2} z - a x _ {2} y _ {1} z = - a z ^ {2}. \end{aligned}</equation>对任意<equation>z = x_{2}y_{1} - x_{1}y_{2}, - a z^{2}\leqslant 0</equation>恒成立当且仅当<equation>a\geqslant 0.</equation>因此，<equation>a</equation>的取值范围是<equation>[0, +\infty)</equation>.

---

**2023年第21题 | 解答题 | 12分**

21. (本题满分12分)

已知二次型<equation>f \left(x_{1}, x_{2}, x_{3}\right)=x_{1}^{2}+2 x_{2}^{2}+2 x_{3}^{2}+2 x_{1} x_{2}-2 x_{1} x_{3},</equation><equation>g \left(y_{1}, y_{2}, y_{3}\right)=y_{1}^{2}+y_{2}^{2}+y_{3}^{2}+2 y_{2} y_{3}</equation>I. 求可逆变换<equation>\boldsymbol{x}=\boldsymbol{P}\boldsymbol{y}</equation>，将<equation>f \left(x_{1}, x_{2}, x_{3}\right)</equation>化为<equation>g \left(y_{1}, y_{2}, y_{3}\right)</equation>；

II. 是否存在正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>，将<equation>f \left(x_{1}, x_{2}, x_{3}\right)</equation>化为<equation>g \left(y_{1}, y_{2}, y_{3}\right).</equation>

**答案:**（I）<equation>P=\left( \begin{array}{c c c} 1 & -1 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，可逆变换<equation>\boldsymbol{x}=\boldsymbol{P}\boldsymbol{y}</equation>将<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>化为<equation>g \left( y_{1}, y_{2}, y_{3} \right)</equation>；

（Ⅱ）不存在正交变换<equation>\boldsymbol{x}=Q\boldsymbol{y}</equation>将<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>化为<equation>g \left( y_{1}, y_{2}, y_{3} \right).</equation>

**解析:**解（I）（法一）记<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>对应的对称矩阵为 A，<equation>g \left( y_{1}, y_{2}, y_{3} \right)</equation>对应的对称矩阵为 B，则<equation>f \left( x_{1}, x_{2}, x_{3} \right) = \mathbf{x}^{\mathrm{T}} \mathbf{A} \mathbf{x}, g \left( y_{1}, y_{2}, y_{3} \right) = \mathbf{y}^{\mathrm{T}} \mathbf{B} \mathbf{y}.</equation>由<equation>f(x_{1},x_{2},x_{3})</equation>与<equation>g(y_{1},y_{2},y_{3})</equation>的表达式可知，<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & 1 & - 1 \\ 1 & 2 & 0 \\ - 1 & 0 & 2 \end{array} \right), \quad \boldsymbol {B} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 1 & 1 \end{array} \right).</equation>对A作合同变换，将其化为B.<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & 1 & - 1 \\ 1 & 2 & 0 \\ - 1 & 0 & 2 \end{array} \right) \xrightarrow [ r _ {2} - r _ {1} ]{\text {行 变 换}} \left( \begin{array}{c c c} 1 & 1 & - 1 \\ 0 & 1 & 1 \\ - 1 & 0 & 2 \end{array} \right) \xrightarrow [ c _ {2} - c _ {1} ]{\text {列 变 换}} \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 1 \\ - 1 & 1 & 2 \end{array} \right)</equation><equation>\xrightarrow [ r _ {3} + r _ {1} ]{\text {行 变 换}} \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 1 \\ 0 & 1 & 1 \end{array} \right) \xrightarrow [ c _ {3} + c _ {1} ]{\text {列 变 换}} \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 1 & 1 \end{array} \right) = \boldsymbol {B}.</equation>记录每一次初等列变换所对应的初等矩阵，分别记为<equation>P_{1}, P_{2}</equation><equation>\boldsymbol {P} _ {1} = \left( \begin{array}{c c c} 1 & - 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right), \quad \boldsymbol {P} _ {2} = \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation><equation>\boldsymbol {P} = \boldsymbol {P} _ {1} \boldsymbol {P} _ {2} = \left( \begin{array}{c c c} 1 & - 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} 1 & - 1 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>因此，<equation>\mathbf{P}^{\mathrm{T}}\mathbf{A}\mathbf{P} = \mathbf{B}</equation>，即<equation>\mathbf{x} = \mathbf{P}\mathbf{y}</equation>将<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>化为<equation>g\left(y_{1},y_{2},y_{3}\right).</equation>（法二）由配方法可得<equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = \left(x _ {1} + x _ {2} - x _ {3}\right) ^ {2} + x _ {2} ^ {2} + x _ {3} ^ {2} + 2 x _ {2} x _ {3} = \left(x _ {1} + x _ {2} - x _ {3}\right) ^ {2} + \left(x _ {2} + x _ {3}\right) ^ {2},</equation><equation>g \left(y _ {1}, y _ {2}, y _ {3}\right) = y _ {1} ^ {2} + \left(y _ {2} + y _ {3}\right) ^ {2}.</equation><equation>\text {令} \left\{ \begin{array}{l l} z _ {1} = x _ {1} + x _ {2} - x _ {3}, \\ z _ {2} = x _ {2} + x _ {3}, \\ z _ {3} = x _ {3}, \end{array} \right. \quad \text {则} \left( \begin{array}{l} z _ {1} \\ z _ {2} \\ z _ {3} \end{array} \right) = \left( \begin{array}{c c c} 1 & 1 & - 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right) \left( \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right). \text {由 于} \left| \begin{array}{c c c} 1 & 1 & - 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right| = 1, \text {故} \left( \begin{array}{c c c} 1 & 1 & - 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right) \text {可}</equation>逆.记<equation>P_{1}^{-1}=\left( \begin{array}{c c c}1&1&-1\\ 0&1&1\\ 0&0&1 \end{array} \right),</equation>则可逆变换<equation>\boldsymbol{x}=\boldsymbol{P}_{1}\boldsymbol{z}</equation>将<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>化为规范形<equation>h\left(z_{1},z_{2},z_{3}\right)=z_{1}^{2}+z_{2}^{2},</equation>即<equation>\boldsymbol {P} _ {1} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} _ {1} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>令<equation>\left\{ \begin{array}{l} z_{1}=y_{1},\\ z_{2}=y_{2}+y_{3},\\ z_{3}=y_{3}, \end{array} \right.</equation>则<equation>\left( \begin{array}{l} z_{1} \\ z_{2} \\ z_{3} \end{array} \right)=\left( \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)\left( \begin{array}{l} y_{1} \\ y_{2} \\ y_{3} \end{array} \right).</equation>由于<equation>\left| \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right|=1</equation>故<equation>\left( \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>可逆.记<equation>P_{2}^{-1}=</equation><equation>\left( \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>则可逆变换<equation>\mathbf{y}=\mathbf{P}_{2}\mathbf{z}</equation>将<equation>g(y_{1},y_{2},y_{3})</equation>化为规范形<equation>h(z_{1},z_{2},z_{3})=z_{1}^{2}+z_{2}^{2}</equation>即<equation>\boldsymbol {P} _ {2} ^ {\mathrm {T}} \boldsymbol {B} \boldsymbol {P} _ {2} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>记<equation>\Lambda = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>. 由于<equation>P_{1}^{\mathrm{T}}A P_{1} = \Lambda , P_{2}^{\mathrm{T}}B P_{2} = \Lambda</equation>，故<equation>\boldsymbol {B} = \left(\boldsymbol {P} _ {2} ^ {\mathrm {T}}\right) ^ {- 1} \boldsymbol {\Lambda} \boldsymbol {P} _ {2} ^ {- 1} \xlongequal {\left(\boldsymbol {P} _ {2} ^ {\mathrm {T}}\right) ^ {- 1} = \left(\boldsymbol {P} _ {2} ^ {- 1}\right) ^ {\mathrm {T}}} \left(\boldsymbol {P} _ {2} ^ {- 1}\right) ^ {\mathrm {T}} \boldsymbol {P} _ {1} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} _ {1} \boldsymbol {P} _ {2} ^ {- 1},</equation>即<equation>x = P_{1}P_{2}^{-1}y</equation>将<equation>f(x_{1},x_{2},x_{3})</equation>化为<equation>g(y_{1},y_{2},y_{3})</equation>下面计算<equation>P_{1}</equation><equation>\begin{array}{l} \left(\boldsymbol {P} _ {1} ^ {- 1}, \boldsymbol {E}\right) = \left( \begin{array}{c c c c c c} 1 & 1 & - 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {2} - r _ {3} ]{r _ {1} + r _ {3}} \left( \begin{array}{c c c c c c} 1 & 1 & 0 & 1 & 0 & 1 \\ 0 & 1 & 0 & 0 & 1 & - 1 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} ^ {*} - r _ {2} ^ {*}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 1 & - 1 & 2 \\ 0 & 1 & 0 & 0 & 1 & - 1 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right). \\ \end{array}</equation>于是，<equation>P_{1} = \left( \begin{array}{c c c} 1 & -1 & 2 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{array} \right).</equation>记<equation>P=P_{1} P_{2}^{-1}</equation>，则<equation>\boldsymbol {P} = \left( \begin{array}{c c c} 1 & - 1 & 2 \\ 0 & 1 & - 1 \\ 0 & 0 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} 1 & - 1 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>矩阵<equation>P</equation>即为所求可逆矩阵，使得可逆变换<equation>x = P y</equation>将<equation>f\left(x_{1}, x_{2}, x_{3}\right)</equation>化为<equation>g\left(y_{1}, y_{2}, y_{3}\right)</equation>（Ⅱ）若正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>将<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>化为<equation>g \left( y_{1}, y_{2}, y_{3} \right)</equation>，则<equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = \boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {x} \xlongequal {\boldsymbol {x} = \boldsymbol {Q} \boldsymbol {y}} \boldsymbol {y} ^ {\mathrm {T}} \boldsymbol {Q} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {Q} \boldsymbol {y} = \boldsymbol {y} ^ {\mathrm {T}} \boldsymbol {B} \boldsymbol {y} = g \left(y _ {1}, y _ {2}, y _ {3}\right).</equation>由此可得<equation>B = Q^{1}AQ</equation>. 又因为<equation>Q</equation>为正交矩阵，<equation>Q^{1} = Q^{-1}</equation>，所以<equation>B = Q^{-1}AQ</equation>. 于是，<equation>A</equation>与<equation>B</equation>相似.

由于<equation>\operatorname{tr}(A) = 5, \operatorname{tr}(B) = 3, A</equation>与<equation>B</equation>的迹不相等，故<equation>A</equation>与<equation>B</equation>不相似，从而不存在正交变换<equation>x = Qy</equation>将<equation>f(x_{1}, x_{2}, x_{3})</equation>化为<equation>g(y_{1}, y_{2}, y_{3})</equation>.

---

**2022年第21题 | 解答题 | 12分**

21. （本题满分12分）

设二次型<equation>f(x_{1},x_{2},x_{3}) = \sum_{i=1}^{3}\sum_{j=1}^{3}ijx_{i}x_{j}</equation>.

I. 写出<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>对应的矩阵；

II. 求正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>将<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>化为标准形；

III. 求<equation>f \left( x_{1}, x_{2}, x_{3} \right)=0</equation>的解.

**答案:**（I）<equation>A=\left( \begin{array}{c c c} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 3 & 6 & 9 \end{array} \right) ;</equation>（Ⅱ）<equation>Q=\left( \begin{array}{c c c} \frac{1}{\sqrt{14}} & -\frac{2}{\sqrt{5}} & -\frac{3}{\sqrt{70}} \\ \frac{2}{\sqrt{14}} & \frac{1}{\sqrt{5}} & -\frac{6}{\sqrt{70}} \\ \frac{3}{\sqrt{14}} & 0 & \frac{5}{\sqrt{70}} \end{array} \right)</equation>正交变换<equation>x=Qy</equation>将二次型 f化为标准形<equation>1 4 y_{1}^{2}</equation>；

（Ⅲ）<equation>f\left(x_{1},x_{2},x_{3}\right)=0</equation>的通解可以取为<equation>k_{1}\left( \begin{array}{c}-2\\ 1\\ 0 \end{array} \right)+k_{2}\left( \begin{array}{c}-3\\ 0\\ 1 \end{array} \right)</equation>或<equation>k_{1}\left( \begin{array}{c}-2\\ 1\\ 0 \end{array} \right)+k_{2}\left( \begin{array}{c}-3\\ -6\\ 5 \end{array} \right)</equation>其中<equation>k_{1},k_{2}</equation>为任意常数.

**解析:**解（I）根据二次型<equation>f</equation>的表达式，其对应的对称矩阵<equation>A</equation>的<equation>(i, j)</equation>元<equation>a_{ij} = ij(i, j = 1, 2, 3)</equation>.

因此，<equation>A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 3 & 6 & 9 \end{pmatrix}</equation>.

（II）由第（I）问可知，<equation>A</equation>是一个秩为1，且迹为14的实对称矩阵。由于实对称矩阵必能相似对角化，且相似的矩阵具有相同的秩与迹，故<equation>A</equation>相似于对角矩阵<equation>\begin{pmatrix} 14 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}</equation>.<equation>A</equation>的特征值为<equation>14, 0, 0</equation>.

下面分别计算<equation>A</equation>的属于特征值0和14的特征向量.

考虑<equation>(0E - A)x = 0</equation>.<equation>-A = \begin{pmatrix} -1 & -2 & -3 \\ -2 & -4 & -6 \\ -3 & -6 & -9 \end{pmatrix} \rightarrow \begin{pmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}</equation>.

于是，<equation>-Ax = 0</equation>等价于方程组<equation>x_1 + 2x_2 + 3x_3 = 0</equation>. 分别令<equation>\begin{pmatrix} x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix}</equation>, 可得<equation>\xi_2 = \begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix}, \xi_3 = \begin{pmatrix} -3 \\ 0 \\ 1 \end{pmatrix}</equation>.

由<equation>\xi_2, \xi_3</equation>满足的方程也可知，<equation>\xi_2, \xi_3</equation>均与向量<equation>\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}</equation>正交. 并且，在三维向量空间中，<equation>k \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}</equation>(<equation>k</equation>为任意非零常数) 代表与<equation>\xi_2, \xi_3</equation>均正交的唯一方向. 由于实对称矩阵属于不同特征值的特征向量相互正交，故向量<equation>\xi_1 = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}</equation>即矩阵<equation>A</equation>的属于特征值14的一个特征向量.

将<equation>\xi_1, \xi_2, \xi_3</equation>单位正交. 实际上，由于<equation>\xi_1</equation>与<equation>\xi_2, \xi_3</equation>均正交，故正交的过程只需将<equation>\xi_2, \xi_3</equation>正交.<equation>\beta_1 = \xi_1</equation>,<equation>\beta_2 = \xi_2</equation>,<equation>\beta_3 = \xi_3 - \frac{(\beta_2, \xi_3)}{\|\beta_2\|^2}\beta_2 = \begin{pmatrix} -3 \\ 0 \\ 1 \end{pmatrix} - \frac{6}{5}\begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} -\frac{3}{5} \\ -\frac{6}{5} \\ 1 \end{pmatrix}</equation>.

或者，也可以通过计算<equation>\beta_1 \times \beta_2</equation>得到与<equation>\beta_1, \beta_2</equation>均正交的向量<equation>\beta_3</equation>.<equation>\beta_3 = \beta_1 \times \beta_2 = \begin{pmatrix} i & j & k \\ 1 & 2 & 3 \\ -2 & 1 & 0 \end{pmatrix} = -3i - 6j + 5k</equation>.

将<equation>\beta_1, \beta_2, \beta_3</equation>单位化，可得<equation>\varepsilon_1 = \frac{\beta_1}{\|\beta_1\|} = \frac{1}{\sqrt{14}}\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}, \varepsilon_2 = \frac{\beta_2}{\|\beta_2\|} = \frac{1}{\sqrt{5}}\begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix}, \varepsilon_3 = \frac{\beta_3}{\|\beta_3\|} = \frac{1}{\sqrt{70}}\begin{pmatrix} -3 \\ -6 \\ 5 \end{pmatrix}</equation>.

令<equation>Q = (\varepsilon_1, \varepsilon_2, \varepsilon_3)</equation>，可得<equation>Q^{-1}AQ = Q^T AQ = \begin{pmatrix} 14 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}</equation>，即正交变换<equation>x = Qy</equation>将二次型<equation>f</equation>化为标准形<equation>14y_1^2</equation>.

（III）（法一）由二次型<equation>f(x_1, x_2, x_3)</equation>的表达式可知,<equation>f(x_1, x_2, x_3) = x_1^2 + 4x_2^2 + 9x_3^2 + 4x_1x_2 + 6x_1x_3 + 12x_2x_3 = (x_1 + 2x_2 + 3x_3)^2</equation>.

因此，<equation>f(x_1, x_2, x_3) = 0</equation>当且仅当<equation>x_1 + 2x_2 + 3x_3 = 0</equation>. 由第（II）问的结果可知，该方程组的通解可取为<equation>k_1 \begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix} + k_2 \begin{pmatrix} -3 \\ 0 \\ 1 \end{pmatrix} + k_1 \begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix} + k_2 \begin{pmatrix} -3 \\ -6 \\ 5 \end{pmatrix}</equation>，其中<equation>k_1, k_2</equation>为任意常数.

（法二）根据第（II）问的结果，<equation>f</equation>在正交变换<equation>x = Qy</equation>下的标准形为<equation>14y_1^2</equation>，故当<equation>y_1 = 0</equation>时，<equation>14y_1^2 = 0</equation>. 从而，当<equation>\begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = Q \begin{pmatrix} 0 \\ y_2 \\ y_3 \end{pmatrix}</equation>时，<equation>f(x_1, x_2, x_3) = 0</equation>.

将<equation>\begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} \frac{1}{\sqrt{14}} & -\frac{2}{\sqrt{5}} & -\frac{3}{\sqrt{70}} \\ \frac{2}{\sqrt{14}} & \frac{1}{\sqrt{5}} & -\frac{6}{\sqrt{70}} \\ \frac{3}{\sqrt{14}} & 0 & \frac{5}{\sqrt{70}} \end{pmatrix} \begin{pmatrix} 0 \\ y_2 \\ y_3 \end{pmatrix}</equation>展开可得，<equation>\begin{pmatrix} x_1 = -\frac{2}{\sqrt{5}}y_2 - \frac{3}{\sqrt{70}}y_3, \\ x_2 = \frac{1}{\sqrt{5}}y_2 - \frac{6}{\sqrt{70}}y_3, \\ x_3 = \frac{5}{\sqrt{70}}y_3 \end{pmatrix}</equation>，其中<equation>k_1, k_2</equation>为任意常数.

不妨令<equation>k_1 = \frac{y_2}{\sqrt{5}}, k_2 = \frac{y_3}{\sqrt{70}}</equation>，则<equation>f(x_1, x_2, x_3) = 0</equation>的解可以取为<equation>\begin{pmatrix} x_1 = -2k_1 - 3k_2, \\ x_2 = k_1 - 6k_2, \\ x_3 = 5k_2 \end{pmatrix}</equation>.

---

**2021年第5题 | 选择题 | 5分 | 答案: B**

5. 设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=\left( x_{1}+x_{2} \right)^{2}+\left( x_{2}+x_{3} \right)^{2}-\left( x_{3}-x_{1} \right)^{2}</equation>的正惯性指数与负惯性指数依次为（    ）

A. 2,0 B. 1,1 C. 2,1 D. 1,2

答案: B

**解析:**解（法一）令<equation>\left\{ \begin{array}{l l} y_{1}=x_{1}+x_{2}, \\ y_{2}=x_{2}+x_{3}, \\ y_{3}=x_{3}, \end{array} \right.</equation>则<equation>x_{3}-x_{1}=y_{2}-y_{1}</equation>，且该变换为可逆线性变换.在该变换下，二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>化为<equation>g \left(y _ {1}, y _ {2}, y _ {3}\right) = y _ {1} ^ {2} + y _ {2} ^ {2} - \left(y _ {2} - y _ {1}\right) ^ {2} = 2 y _ {1} y _ {2}.</equation>再令<equation>\left\{ \begin{array}{l l} y_{1} = z_{1} + z_{2}, \\ y_{2} = z_{1} - z_{2}, \\ y_{3} = z_{3}, \end{array} \right.</equation>则<equation>g\left(y_{1}, y_{2}, y_{3}\right)</equation>化为<equation>h \left(z _ {1}, z _ {2}, z _ {3}\right) = 2 \left(z _ {1} + z _ {2}\right) \left(z _ {1} - z _ {2}\right) = 2 z _ {1} ^ {2} - 2 z _ {2} ^ {2}.</equation>因此，<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>的一个标准形为<equation>2z_{1}^{2}-2z_{2}^{2}</equation>，其正、负惯性指数分别为1，1.应选B.

（法二）将<equation>f(x_{1},x_{2},x_{3})</equation>展开可得<equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = 2 x _ {2} ^ {2} + 2 x _ {1} x _ {2} + 2 x _ {2} x _ {3} + 2 x _ {1} x _ {3}.</equation>该二次型对应的矩阵为<equation>A = \left( \begin{array}{c c c} 0 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 0 \end{array} \right)</equation>. 不难发现，<equation>A</equation>的第二行为第一行与第三行的和，故<equation>r(A)\leqslant 2.</equation>又因为<equation>A</equation>有一个2阶非零子式<equation>\left| \begin{array}{c c} 0 & 1 \\ 1 & 2 \end{array} \right|</equation>，所以<equation>r(A)\geqslant 2.</equation>于是，<equation>r(A) = 2.</equation>由于二次型的正、负惯性指数之和等于其对应矩阵的秩，而选项C、D的两数之和均为3，故可排除选项C、D.

另一方面，若 f的负惯性指数为0，则 f非负，即对任意<equation>\left(x_{1},x_{2},x_{3}\right)</equation>，均有<equation>f\left(x_{1},x_{2},x_{3}\right)\geqslant0</equation>但是，<equation>f(1,0,-1)=1+1-4<0</equation>，矛盾.因此，选项A不正确.

根据排除法，应选B.

---

**2021年第21题 | 解答题 | 12分**

21. （本题满分12分）

已知<equation>A = \left( \begin{array}{c c c} a & 1 & -1 \\ 1 & a & -1 \\ -1 & -1 & a \end{array} \right).</equation>I. 求正交矩阵<equation>P</equation>，使得<equation>P^{\mathrm{T}}AP</equation>为对角矩阵；

II. 求正定矩阵<equation>C</equation>，使得<equation>C^{2} = (a + 3)E - A</equation>，其中<equation>E</equation>为3阶单位矩阵.

**答案:**( I )<equation>P=\left( \begin{array}{c c c} -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{3}} \\ 0 & \frac{2}{\sqrt{6}} & \frac{1}{\sqrt{3}} \end{array} \right), P^{\mathrm{T}} A P=\left( \begin{array}{c c c} a-1 & 0 & 0 \\ 0 & a-1 & 0 \\ 0 & 0 & a+2 \end{array} \right);</equation>( II )<equation>C=\left( \begin{array}{c c c} \frac{5}{3} & -\frac{1}{3} & \frac{1}{3} \\ -\frac{1}{3} & \frac{5}{3} & \frac{1}{3} \\ \frac{1}{3} & \frac{1}{3} & \frac{5}{3} \end{array} \right).</equation>

**解析:**解（ I ）计算 A的特征多项式.<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - a & - 1 & 1 \\ - 1 & \lambda - a & 1 \\ 1 & 1 & \lambda - a  \right| \xlongequal {r _ {1} - r _ {2}} \left| \begin{array}{c c c} \lambda - a + 1 & - \lambda + a - 1 & 0 \\ - 1 & \lambda - a & 1 \\ 1 & 1 & \lambda - a  \right| \\ &= (\lambda - a + 1) \left| \begin{array}{c c c} 1 & - 1 & 0 \\ - 1 & \lambda - a & 1 \\ 1 & 1 & \lambda - a  \right| &= (\lambda - a + 1) \left| \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & \lambda - a - 1 & 1 \\ 1 & 2 & \lambda - a  \right| \\ &= (\lambda - a + 1) \left[ (\lambda - a - 1) (\lambda - a) - 2 \right] = (\lambda - a + 1) \left[ (\lambda - a) ^ {2} - (\lambda - a) - 2 \right] \\ &= (\lambda - a + 1) (\lambda - a - 2) (\lambda - a + 1) = (\lambda - a + 1) ^ {2} (\lambda - a - 2). \end{aligned}</equation>A的特征值为<equation>a - 1,a - 1,a + 2</equation>.

分别计算<equation>A</equation>的属于特征值<equation>a - 1, a + 2</equation>的特征向量.

考虑<equation>[(a - 1)E - A]x = 0.</equation><equation>(a - 1) \boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} - 1 & - 1 & 1 \\ - 1 & - 1 & 1 \\ 1 & 1 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & - 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>分别令<equation>\left\{\begin{array}{l l}x_{2}=1,\\ x_{3}=0,\end{array}\right.</equation><equation>\left\{\begin{array}{l l}x_{2}=0,\\ x_{3}=1,\end{array}\right.</equation>可得<equation>\boldsymbol{\xi}_{1}=\left( \begin{array}{c}-1\\ 1\\ 0 \end{array} \right)</equation>与<equation>\boldsymbol{\xi}_{2}=\left( \begin{array}{c}1\\ 0\\ 1 \end{array} \right)</equation>为<equation>[(a-1)\boldsymbol{E}-\boldsymbol{A}]\boldsymbol{x}=\boldsymbol{0}</equation>的两个线性

无关的解，从而<equation>\xi_{1},\xi_{2}</equation>为<equation>A</equation>的属于特征值<equation>a - 1</equation>的两个线性无关的特征向量.

考虑<equation>[(a + 2)E - A]x = 0.</equation><equation>(a + 2) \boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} 2 & - 1 & 1 \\ - 1 & 2 & 1 \\ 1 & 1 & 2 \end{array} \right) \xrightarrow [ r _ {2} + r _ {1} ^ {*} ]{r _ {1} \leftrightarrow r _ {3}} \left( \begin{array}{c c c} 1 & 1 & 2 \\ 0 & 3 & 3 \\ 0 & - 3 & - 3 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 2 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

令<equation>x_{3} = 1</equation>，可得<equation>\xi_{3} = \left( \begin{array}{c} - 1 \\ - 1 \\ 1 \end{array} \right)</equation>为<equation>[(a + 2)E - A]x = 0</equation>的一个解，从而<equation>\xi_{3}</equation>为A的属于特征值<equation>a + 2</equation>的一个特征向量.

将<equation>\boldsymbol{\xi}_{1},\boldsymbol{\xi}_{2},\boldsymbol{\xi}_{3}</equation>施密特正交.由于<equation>\boldsymbol{\xi}_{3}</equation>与<equation>\boldsymbol{\xi}_{1},\boldsymbol{\xi}_{2}</equation>为属于不同特征值的特征向量，<equation>\boldsymbol{\xi}_{3}</equation>与<equation>\boldsymbol{\xi}_{i} ( i=1,2)</equation>相互正交，故只需将<equation>\boldsymbol{\xi}_{1},\boldsymbol{\xi}_{2}</equation>正交.<equation>\boldsymbol {\beta} _ {1} = \boldsymbol {\xi} _ {1} = \left( \begin{array}{c} - 1 \\ 1 \\ 0 \end{array} \right),</equation><equation>\boldsymbol {\beta} _ {2} = \boldsymbol {\xi} _ {2} - \frac {\left(\boldsymbol {\beta} _ {1} , \boldsymbol {\xi} _ {2}\right)}{\| \boldsymbol {\beta} _ {1} \| ^ {2}} \boldsymbol {\beta} _ {1} = \left( \begin{array}{c} 1 \\ 0 \\ 1 \end{array} \right) - \frac {(- 1)}{2} \left( \begin{array}{c} - 1 \\ 1 \\ 0 \end{array} \right) = \frac {1}{2} \left( \begin{array}{c} 1 \\ 1 \\ 2 \end{array} \right),</equation><equation>\boldsymbol {\beta} _ {3} = \boldsymbol {\xi} _ {3} = \left( \begin{array}{c} - 1 \\ - 1 \\ 1 \end{array} \right).</equation>将<equation>\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3}</equation>单位化.<equation>\boldsymbol {\varepsilon} _ {1} = \frac {\boldsymbol {\beta} _ {1}}{\| \boldsymbol {\beta} _ {1} \|} = \frac {1}{\sqrt {2}} \left( \begin{array}{c} - 1 \\ 1 \\ 0 \end{array} \right), \quad \boldsymbol {\varepsilon} _ {2} = \frac {\boldsymbol {\beta} _ {2}}{\| \boldsymbol {\beta} _ {2} \|} = \frac {1}{\sqrt {6}} \left( \begin{array}{c} 1 \\ 1 \\ 2 \end{array} \right), \quad \boldsymbol {\varepsilon} _ {3} = \frac {\boldsymbol {\beta} _ {3}}{\| \boldsymbol {\beta} _ {3} \|} = \frac {1}{\sqrt {3}} \left( \begin{array}{c} - 1 \\ - 1 \\ 1 \end{array} \right).</equation><equation>\text {令} \boldsymbol {P} = \left(\varepsilon_ {1}, \varepsilon_ {2}, \varepsilon_ {3}\right) = \left( \begin{array}{c c c} - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {6}} & - \frac {1}{\sqrt {3}} \\ \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {6}} & - \frac {1}{\sqrt {3}} \\ 0 & \frac {2}{\sqrt {6}} & \frac {1}{\sqrt {2}} \end{array} \right), \text {则} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} = \left( \begin{array}{c c c} a - 1 & 0 & 0 \\ 0 & a - 1 & 0 \\ 0 & 0 & a + 2 \end{array} \right).</equation>（Ⅱ）由第（I）问可得，<equation>P^{\mathrm{T}} A P=\left( \begin{array}{c c c} a-1 & 0 & 0 \\ 0 & a-1 & 0 \\ 0 & 0 & a+2 \end{array} \right)</equation>，则<equation>A=P\left( \begin{array}{c c c} a-1 & 0 & 0 \\ 0 & a-1 & 0 \\ 0 & 0 & a+2 \end{array} \right) P^{\mathrm{T}}.</equation><equation>\begin{aligned} (a + 3) \boldsymbol {E} - \boldsymbol {A} &= \boldsymbol {P} (a + 3) \boldsymbol {E P} ^ {\mathrm {T}} - \boldsymbol {P} \left( \begin{array}{c c c} a - 1 & 0 & 0 \\ 0 & a - 1 & 0 \\ 0 & 0 & a + 2  \right) \boldsymbol {P} ^ {\mathrm {T}} \\ &= \boldsymbol {P} \left[ \left( \begin{array}{c c c} a + 3 & 0 & 0 \\ 0 & a + 3 & 0 \\ 0 & 0 & a + 3  \right) - \left( \begin{array}{c c c} a - 1 & 0 & 0 \\ 0 & a - 1 & 0 \\ 0 & 0 & a + 2  \right) \right] \boldsymbol {P} ^ {\mathrm {T}} \\ &= \boldsymbol {P} \left( \begin{array}{c c c} 4 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 1  \right) \boldsymbol {P} ^ {\mathrm {T}} &= \boldsymbol {P} \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1  \right) \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {P} \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1  \right) \boldsymbol {P} ^ {\mathrm {T}}. \end{aligned}</equation>取<equation>C = P\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right) P^{\mathrm{T}}</equation>，则<equation>C</equation>的特征值均为正，从而正定，且<equation>C^{2} = (a + 3)E - A.</equation><equation>\begin{aligned} \boldsymbol {C} &= \left( \begin{array}{c c c} - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {6}} & - \frac {1}{\sqrt {3}} \\ \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {6}} & - \frac {1}{\sqrt {3}} \\ 0 & \frac {2}{\sqrt {6}} & \frac {1}{\sqrt {3}}  \right) \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1  \right) \left( \begin{array}{c c c} - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {2}} & 0 \\ \frac {1}{\sqrt {6}} & \frac {1}{\sqrt {6}} & \frac {2}{\sqrt {6}} \\ - \frac {1}{\sqrt {3}} & - \frac {1}{\sqrt {3}} & \frac {1}{\sqrt {3}}  \right) \\ &= \left( \begin{array}{c c c} - \sqrt {2} & \frac {2}{\sqrt {6}} & - \frac {1}{\sqrt {3}} \\ \sqrt {2} & \frac {2}{\sqrt {6}} & - \frac {1}{\sqrt {3}} \\ 0 & \frac {4}{\sqrt {6}} & \frac {1}{\sqrt {3}}  \right) \left( \begin{array}{c c c} - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {2}} & 0 \\ \frac {1}{\sqrt {6}} & \frac {1}{\sqrt {6}} & \frac {2}{\sqrt {6}} \\ - \frac {1}{\sqrt {3}} & - \frac {1}{\sqrt {3}} & \frac {1}{\sqrt {3}}  \right) &= \left( \begin{array}{c c c} \frac {5}{3} & - \frac {1}{3} & \frac {1}{3} \\ - \frac {1}{3} & \frac {5}{3} & \frac {1}{3} \\ \frac {1}{3} & \frac {1}{3} & \frac {5}{3}  \right). \end{aligned}</equation>

---

**2020年第20题 | 解答题 | 11分**

20. (本题满分11分)

设二次型<equation>f \left( x_{1}, x_{2} \right)=x_{1}^{2}-4 x_{1} x_{2}+4 x_{2}^{2}</equation>经正交变换<equation>\binom{x_{1}}{x_{2}}=Q \binom{y_{1}}{y_{2}}</equation>化为二次型<equation>g \left( y_{1}, y_{2} \right)=a y_{1}^{2}+4 y_{1} y_{2}+b y_{2}^{2}</equation>其中<equation>a \geqslant b</equation>.

I. 求 a,b的值;

II. 求正交矩阵 Q.

**答案:**（ I ）<equation>a=4,b=1;</equation>（Ⅱ）<equation>Q = \left( \begin{array}{c c} - \frac{4}{5} & \frac{3}{5} \\ \frac{3}{5} & \frac{4}{5} \end{array} \right), f \left( x_{1}, x_{2} \right)</equation>经过正交变换<equation>\binom{x_1}{x_2} = Q\binom{y_1}{y_2}</equation>化为二次型<equation>g \left( y_{1}, y_{2} \right).</equation>

**解析:**解（I）写出二次型<equation>f ( x_{1}, x_{2} )=x_{1}^{2}-4 x_{1} x_{2}+4 x_{2}^{2}</equation>对应的矩阵A，二次型<equation>g ( y_{1}, y_{2} )=a y_{1}^{2}+</equation><equation>4 y_{1} y_{2}+b y_{2}^{2}</equation>对应的矩阵B.<equation>\boldsymbol {A} = \left( \begin{array}{c c} 1 & - 2 \\ - 2 & 4 \end{array} \right), \quad \boldsymbol {B} = \left( \begin{array}{c c} a & 2 \\ 2 & b \end{array} \right).</equation>由于正交变换也是相似变换，故<equation>A</equation>与<equation>B</equation>相似。又因为相似的矩阵具有相同的迹与行列式，所以<equation>\left\{ \begin{array}{l} a + b = 5, \\ a b = 4. \end{array} \right.</equation>由<equation>a\geqslant b</equation>可确定<equation>\left\{ \begin{array}{l l} a = 4, \\ b = 1. \end{array} \right.</equation>（Ⅱ）由第（I）问可知，<equation>A=\left( \begin{array}{c c}1&-2\\ -2&4 \end{array} \right), B=\left( \begin{array}{c c}4&2\\ 2&1 \end{array} \right).</equation>计算 A和B的特征多项式可得<equation>|\lambda E - A| = \left| \begin{array}{cc}\lambda -1 & 2\\ 2 & \lambda -4 \end{array} \right| = \lambda (\lambda -5)</equation>.于是A和B的特征值为5和0.分别计算A，B的特征向量.

计算<equation>A</equation>的属于特征值5的特征向量.

考虑（5E-A）x=0.<equation>5 E - A = \left( \begin{array}{c c} 4 & 2 \\ 2 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c} 2 & 1 \\ 0 & 0 \end{array} \right).</equation>于是，<equation>r ( 5 E - A ) = 1</equation>，求得<equation>\boldsymbol{\xi}_{1}=(-1,2)^{\mathrm{T}}</equation>为<equation>( 5 E-A ) x=0</equation>的一个基础解系.<equation>(-1,2)^{\mathrm{T}}</equation>为A的属于特征值5的一个特征向量.

计算<equation>A</equation>的属于特征值0的特征向量.

考虑（0E-A）x=0.<equation>- \boldsymbol {A} = \left( \begin{array}{c c} - 1 & 2 \\ 2 & - 4 \end{array} \right) \rightarrow \left( \begin{array}{c c} - 1 & 2 \\ 0 & 0 \end{array} \right).</equation>于是，<equation>r ( 0 E - A ) = 1</equation>，求得<equation>\boldsymbol{\xi}_{2}=(2,1)^{\mathrm{T}}</equation>为<equation>( 0 E-A ) x=0</equation>的一个基础解系.<equation>( 2,1)^{\mathrm{T}}</equation>为A的属于特征值0的一个特征向量.

取<equation>P_{1} = \left( \begin{array}{cc} -1 & 2 \\ 2 & 1 \end{array} \right)</equation>，则<equation>P_{1}^{-1} A P_{1} = \left( \begin{array}{cc} 5 & 0 \\ 0 & 0 \end{array} \right)</equation>.

计算<equation>B</equation>的属于特征值5的特征向量.

考虑（5E-B）x=0.<equation>5 E - B = \left( \begin{array}{c c} 1 & - 2 \\ - 2 & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c} 1 & - 2 \\ 0 & 0 \end{array} \right).</equation>于是，<equation>r ( 5 E-B )=1</equation>，求得<equation>\boldsymbol{\eta}_{1}=(2,1)^{\mathrm{T}}</equation>为（5E-B）<equation>\boldsymbol{x}=\mathbf{0}</equation>的一个基础解系. （2，1）<equation>^{\mathrm{T}}</equation>为B的属于特征值5的一个特征向量.

计算<equation>B</equation>的属于特征值0的特征向量.

考虑（0E-B）x=0.<equation>- \boldsymbol {B} = \left( \begin{array}{c c} - 4 & - 2 \\ - 2 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c} 2 & 1 \\ 0 & 0 \end{array} \right).</equation>于是，<equation>r ( 0 E-B )=1</equation>，求得<equation>\boldsymbol{\eta}_{2}=(-1,2)^{\mathrm{T}}</equation>为<equation>( 0 E-B ) \boldsymbol{x}=\mathbf{0}</equation>的一个基础解系.<equation>(-1,2)^{\mathrm{T}}</equation>为B的属于特征值0的一个特征向量.

取<equation>P_{2} = \left( \begin{array}{cc}2 & -1\\ 1 & 2 \end{array} \right)</equation>，则<equation>P_{2}^{-1}B P_{2} = \left( \begin{array}{cc}5 & 0\\ 0 & 0 \end{array} \right).</equation>由于<equation>B = P_{2}P_{1}^{-1}AP_{1}P_{2}^{-1}</equation>，故取<equation>Q = P_{1}P_{2}^{-1}</equation>，则<equation>Q^{-1}AQ = B.</equation>计算得<equation>P_{2}^{-1}=\frac{1}{5}\left( \begin{array}{cc}2&1\\ -1&2 \end{array} \right)</equation>，则<equation>Q=\frac{1}{5}\left( \begin{array}{cc}-1&2\\ 2&1 \end{array} \right)\left( \begin{array}{cc}2&1\\ -1&2 \end{array} \right)=\left( \begin{array}{cc}-\frac{4}{5}&\frac{3}{5}\\ \frac{3}{5}&\frac{4}{5} \end{array} \right).</equation>并且，Q已经是正交矩阵，无需再单位正交化.

因此，<equation>Q = \left( \begin{array}{c c} - \frac{4}{5} & \frac{3}{5} \\ \frac{3}{5} & \frac{4}{5} \end{array} \right), f(x_{1}, x_{2})</equation>经过正交变换<equation>\binom{x_1}{x_2} = Q\binom{y_1}{y_2}</equation>化为二次型<equation>g(y_1, y_2)</equation>.

---

**2019年第5题 | 选择题 | 4分 | 答案: C**

5. 设 A是3阶实对称矩阵，E是3阶单位矩阵.若<equation>A^{2}+A=2 E</equation>，且<equation>|A|=4</equation>，则二次型<equation>x^{\mathrm{T}} A x</equation>的规范形为（    )

A.<equation>y_{1}^{2}+y_{2}^{2}+y_{3}^{2}</equation>B.<equation>y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>C.<equation>y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>D.<equation>-y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>

答案: C

**解析:**解 设<equation>\lambda</equation>为 A的一个特征值，<equation>\alpha</equation>为属于特征值<equation>\lambda</equation>的特征向量.

由<equation>A^{2}+A=2 E</equation>可得<equation>\left(\lambda^{2}+\lambda-2\right)\alpha=0</equation>. 由于<equation>\alpha</equation>为非零向量，故<equation>\lambda^{2}+\lambda-2=0</equation>. 解得<equation>\lambda=1</equation>或<equation>\lambda=-2</equation>. A的特征值只能取1和-2.

又因为<equation>| A |=4</equation>，所以 A的特征值应为-2，-2，1.因此，二次型<equation>x^{\mathrm{T}} A x</equation>的正惯性指数为1，负惯性指数为2.四个选项中，只有<equation>y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>满足该性质.应选C.

---

**2018年第20题 | 解答题 | 11分**

20. (本题满分11分)

设实二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=\left( x_{1}-x_{2}+x_{3} \right)^{2}+\left( x_{2}+x_{3} \right)^{2}+\left( x_{1}+a x_{3} \right)^{2}</equation>其中 a是参数.

I. 求<equation>f \left( x_{1}, x_{2}, x_{3} \right)=0</equation>的解；

II. 求<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>的规范形.

**答案:**（I）当 a≠2时，<equation>f ( x_{1}, x_{2}, x_{3} )=0</equation>的解为<equation>\left( x_{1}, x_{2}, x_{3}\right)^{\mathrm{T}}=\left( 0,0,0\right)^{\mathrm{T}}</equation>；当 a=2时，<equation>f \left( x_{1}, x_{2}, x_{3}\right)=0</equation>的解为<equation>\left( x_{1}, x_{2}, x_{3}\right)^{\mathrm{T}}=k \left( -2,-1,1\right)^{\mathrm{T}}</equation>其中 k为任意常数.

（Ⅱ）当 a≠2时，f的规范形为<equation>f=y_{1}^{2}+y_{2}^{2}+y_{3}^{2}</equation>；当 a=2时，f的规范形为<equation>f=z_{1}^{2}+z_{2}^{2}.</equation>

**解析:**解（I）<equation>f \left(x_{1}, x_{2}, x_{3}\right)=0</equation>当且仅当<equation>\left\{ \begin{array}{l l} x_{1}-x_{2}+x_{3}=0, \\ x_{2}+x_{3}=0, \\ x_{1}+a x_{3}=0. \end{array} \right.</equation>记<equation>A</equation>为该方程组的系数矩阵. 对<equation>A</equation>作初等行变换.<equation>A = \left( \begin{array}{c c c} 1 & - 1 & 1 \\ 0 & 1 & 1 \\ 1 & 0 & a \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c} 1 & - 1 & 1 \\ 0 & 1 & 1 \\ 0 & 1 & a - 1 \end{array} \right) \xrightarrow {r _ {1} + r _ {2}} \left( \begin{array}{c c c} 1 & 0 & 2 \\ 0 & 1 & 1 \\ 0 & 0 & a - 2 \end{array} \right).</equation><equation>\left(r _ {i} ^ {*}\right)</equation>当<equation>a\neq 2</equation>时，<equation>r(\mathbf{A}) = 3</equation>，方程组只有零解.

当<equation>a = 2</equation>时，<equation>r(A) = 2.</equation>方程组的基础解系仅包含一个向量.取<equation>x_{3}</equation>为自由变元，令<equation>x_{3} = 1</equation>，解得<equation>(x_{1},x_{2},x_{3})^{\mathrm{T}} = (-2,-1,1)^{\mathrm{T}}</equation>为该方程组的一个基础解系.

因此，当<equation>a\neq 2</equation>时，<equation>f ( x_{1}, x_{2}, x_{3} )=0</equation>的解为<equation>( x_{1}, x_{2}, x_{3} )^{\mathrm{T}}=(0,0,0)^{\mathrm{T}}</equation>；当<equation>a=2</equation>时，<equation>f ( x_{1}, x_{2}, x_{3} )=0</equation>的解为<equation>( x_{1}, x_{2}, x_{3} )^{\mathrm{T}}=k (-2,-1,1)^{\mathrm{T}}</equation>，其中k为任意常数.

（Ⅱ）由<equation>f(x_{1},x_{2},x_{3})</equation>的表达式知，<equation>f(x_{1},x_{2},x_{3})\geqslant 0.</equation>当 a≠2时，由第（I）问可知，<equation>f ( x_{1}, x_{2}, x_{3} )=0</equation>只有零解，f为正定二次型.因此，当 a≠2时， f的规范形为<equation>f=y_{1}^{2}+y_{2}^{2}+y_{3}^{2}.</equation>当 a = 2时，f不满秩.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= \left(x _ {1} - x _ {2} + x _ {3}\right) ^ {2} + \left(x _ {2} + x _ {3}\right) ^ {2} + \left(x _ {1} + 2 x _ {3}\right) ^ {2} \\ &= 2 x _ {1} ^ {2} + 2 x _ {2} ^ {2} + 6 x _ {3} ^ {2} - 2 x _ {1} x _ {2} + 6 x _ {1} x _ {3}. \end{aligned}</equation>记<equation>f</equation>对应的对称矩阵为<equation>B = \left( \begin{array}{c c c} 2 & -1 & 3 \\ -1 & 2 & 0 \\ 3 & 0 & 6 \end{array} \right)</equation>.

下面用三种方法求 f的规范形.

（法一）由<equation>f(x_{1},x_{2},x_{3})\geqslant 0</equation>可知<equation>f</equation>的负惯性指数为0（否则，若规范形有负系数，不妨设规范形为<equation>f = y_{1}^{2} + y_{2}^{2} - y_{3}^{2}</equation>，取<equation>(y_{1},y_{2},y_{3}) = (0,0,1)</equation>，则<equation>f(y_{1},y_{2},y_{3}) = -1 < 0</equation>，矛盾).由于B的秩等于f的正、负惯性指数之和，故<equation>f</equation>的正惯性指数等于<equation>r(B)</equation>.

计算<equation>| B |</equation>得<equation>| B |=0</equation>，故<equation>r ( B ) \leqslant2</equation>.又因为B有一个2阶子式<equation>\left| \begin{array}{c c} {2} & {-1} \\ {-1} & {2} \end{array} \right|=3\neq0</equation>，所以<equation>r ( B ) \geqslant2.</equation>因此，<equation>r ( B )=2.</equation>综上所述，<equation>f</equation>的正惯性指数为2，负惯性指数为0.<equation>f</equation>的规范形为<equation>f = z_{1}^{2} + z_{2}^{2}</equation>.

（法二）计算<equation>B</equation>的特征值，从而得到<equation>f</equation>的正、负惯性指数.

计算 B的特征多项式.<equation>| \lambda E - B | = \left| \begin{array}{c c c} \lambda - 2 & 1 & - 3 \\ 1 & \lambda - 2 & 0 \\ - 3 & 0 & \lambda - 6 \end{array} \right| = \lambda \left(\lambda^ {2} - 1 0 \lambda + 1 8\right).</equation>解<equation>\lambda^{2}-1 0 \lambda+1 8=0</equation>可得<equation>\lambda_{1,2}=\frac{1 0 \pm \sqrt{1 0 0}-7 2}{2}=5 \pm \sqrt{7}.</equation>由于<equation>5+\sqrt{7}>0, 5-\sqrt{7}>0</equation>故f有两个正特征值，一个零特征值，从而f的正惯性指数为2，负惯性指数为0.

因此，<equation>f</equation>的规范形为<equation>f = z_{1}^{2} + z_{2}^{2}</equation>.

（法三）配方法.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= 2 x _ {1} ^ {2} + 2 x _ {2} ^ {2} + 6 x _ {3} ^ {2} - 2 x _ {1} x _ {2} + 6 x _ {1} x _ {3} = 2 \left(x _ {1} ^ {2} - x _ {1} x _ {2} + 3 x _ {1} x _ {3}\right) + 2 x _ {2} ^ {2} + 6 x _ {3} ^ {2} \\ &= 2 \left(x _ {1} - \frac {x _ {2}}{2} + \frac {3}{2} x _ {3}\right) ^ {2} + \frac {3}{2} x _ {2} ^ {2} - \frac {9}{2} x _ {3} ^ {2} + 3 x _ {2} x _ {3} + 6 x _ {3} ^ {2} \\ &= 2 \left(x _ {1} - \frac {x _ {2}}{2} + \frac {3}{2} x _ {3}\right) ^ {2} + \frac {3}{2} \left(x _ {2} + x _ {3}\right) ^ {2}. \end{aligned}</equation>令<equation>\left\{ \begin{array}{l l} z_{1}=\sqrt{2}\left(x_{1}-\frac{x_{2}}{2}+\frac{3}{2} x_{3}\right), \\ z_{2}=\sqrt{\frac{3}{2}}\left(x_{2}+x_{3}\right), \\ z_{3}=x_{3}, \end{array} \right.</equation>则<equation>f\left(z_{1},z_{2},z_{3}\right)=z_{1}^{2}+z_{2}^{2}.</equation>因此 f的规范形为<equation>f=z_{1}^{2}+z_{2}^{2}.</equation>因此，<equation>f</equation>的规范形为<equation>f = z_{1}^{2} + z_{2}^{2}</equation>.

---

**2017年第21题 | 解答题 | 11分**

21. (本题满分11分)

设二次型<equation>f \left(x_{1}, x_{2}, x_{3}\right)=2 x_{1}^{2}-x_{2}^{2}+a x_{3}^{2}+2 x_{1} x_{2}-8 x_{1} x_{3}+2 x_{2} x_{3}</equation>在正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>下的标准形为<equation>\lambda_{1} y_{1}^{2}+\lambda_{2} y_{2}^{2}</equation>求 a的值及一个正交矩阵 Q.

**答案:**a=2，<equation>Q=\left( \begin{array}{c c c} -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \\ 0 & -\frac{1}{\sqrt{3}} & \frac{2}{\sqrt{6}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \end{array} \right)</equation>，且<equation>Q^{\mathrm{T}}AQ=\left( \begin{array}{c c c} 6 & 0 & 0 \\ 0 & -3 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>，即f在正交变换 x = Qy下的标准

形为<equation>f = 6y_{1}^{2} - 3y_{2}^{2}</equation>.

**解析:**记二次型<equation>f</equation>对应的实对称矩阵为<equation>A</equation>，则<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 2 & 1 & - 4 \\ 1 & - 1 & 1 \\ - 4 & 1 & a \end{array} \right).</equation>由于f在正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>下的标准形为<equation>\lambda_{1}y_{1}^{2}+\lambda_{2}y_{2}^{2}</equation>，故A的特征值为<equation>\lambda_{1},\lambda_{2},0.</equation>从而<equation>|\boldsymbol{A}|=0.</equation>计算A的行列式得<equation>| A | = - 3 a + 6.</equation>因此，<equation>a = 2</equation>，<equation>A = \left( \begin{array}{c c c} 2 & 1 & -4 \\ 1 & -1 & 1 \\ -4 & 1 & 2 \end{array} \right)</equation>计算 A的特征多项式得<equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda - 2 & - 1 & 4 \\ - 1 & \lambda + 1 & - 1 \\ 4 & - 1 & \lambda - 2 \end{array} \right| = \lambda^ {3} - 3 \lambda^ {2} - 1 8 \lambda = \lambda (\lambda - 6) (\lambda + 3).</equation>于是，<equation>\boldsymbol{A}</equation>的3个特征值分别为6，-3，0.

当<equation>\lambda=6</equation>时，<equation>\begin{array}{l} 6 E - A = \left( \begin{array}{c c c} 4 & - 1 & 4 \\ - 1 & 7 & - 1 \\ 4 & - 1 & 4 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c} 4 & - 1 & 4 \\ - 1 & 7 & - 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} + 4 r _ {2}} \left( \begin{array}{c c c} 0 & 1 & 0 \\ - 1 & 7 & - 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} - 7 r _ {1} ^ {* *}} \frac {1}{r _ {2} ^ {*} \times (- 1)} \left( \begin{array}{c c c} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）<equation>(6E - A)x = 0</equation>的一个基础解系为<equation>\eta_1 = (-1,0,1)^{\mathrm{T}}.</equation>当<equation>\lambda=-3</equation>时，<equation>\begin{array}{l} - 3 E - A = \left( \begin{array}{c c c} - 5 & - 1 & 4 \\ - 1 & - 2 & - 1 \\ 4 & - 1 & - 5 \end{array} \right) \xrightarrow [ r _ {3} ^ {*} - r _ {2} ]{r _ {3} + r _ {1}} \left( \begin{array}{c c c} - 5 & - 1 & 4 \\ - 1 & - 2 & - 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {2} \times (- 1) ]{r _ {1} - 5 r _ {2}} \left( \begin{array}{c c c} 0 & 9 & 9 \\ 1 & 2 & 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow [ r _ {2} ^ {*} - r _ {1} ^ {* *} ]{r _ {1} ^ {*} \times \frac {1}{9}} \left( \begin{array}{c c c} 0 & 1 & 1 \\ 1 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation><equation>(-3E - A)x = 0</equation>的一个基础解系为<equation>\eta_2 = (1, -1, 1)^{\mathrm{T}}.</equation>当<equation>\lambda=0</equation>时，<equation>\begin{array}{l} 0 E - A = \left( \begin{array}{c c c} - 2 & - 1 & 4 \\ - 1 & 1 & - 1 \\ 4 & - 1 & - 2 \end{array} \right) \xrightarrow {r _ {3} + r _ {1}} \frac {r _ {3} ^ {*} + 2 r _ {2}}{r _ {3} ^ {*} + 2 r _ {2}} \left( \begin{array}{c c c} - 2 & - 1 & 4 \\ - 1 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} - 2 r _ {2}} \left( \begin{array}{c c c} 0 & 1 & - 2 \\ - 1 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} \times (- 1) + r _ {1} ^ {* *}} \left( \begin{array}{c c c} 0 & 1 & - 2 \\ 1 & 0 & - 1 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation><equation>(0E - A)x = 0</equation>的一个基础解系为<equation>\eta_3 = (1,2,1)^{\mathrm{T}}.</equation>由于实对称矩阵对应于不同特征值的特征向量相互正交，故只需要将所得特征向量单位化.<equation>\boldsymbol{\eta}_{1},\boldsymbol{\eta}_{2},\boldsymbol{\eta}_{3}</equation>分别单位化，作为Q的列向量，得正交矩阵<equation>Q=\left( \begin{array}{c c c} -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \\ 0 & -\frac{1}{\sqrt{3}} & \frac{2}{\sqrt{6}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \end{array} \right)</equation>，且<equation>Q^{\mathrm{T}}AQ=</equation><equation>\left( \begin{array}{c c c} 6 & 0 & 0 \\ 0 & -3 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>，即<equation>f</equation>在正交变换<equation>\boldsymbol{x} = Q\boldsymbol{y}</equation>下的标准形为<equation>f = 6y_{1}^{2} - 3y_{2}^{2}</equation>.

