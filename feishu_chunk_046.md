#### 曲线的凹凸性、拐点及渐近线

**2025年第1题 | 选择题 | 5分 | 答案: B**

1. 已知函数<equation>f ( x )=\int_{0}^{x} \mathrm{e}^{t^{2}} \sin t \mathrm{d} t,g ( x )=\int_{0}^{x} \mathrm{e}^{t^{2}} \mathrm{d} t \cdot \sin^{2} x</equation>，则（    )

A. x=0是 f(x)的极值点，也是 g(x)的极值点

B. x=0是 f(x)的极值点，(0,0)是曲线 y=g(x)的拐点

C. x=0是 f(x)的极值点，(0,0)是曲线 y=f(x)的拐点

D. (0,0)是曲线 y=f(x)的拐点，也是曲线 y=g(x)的拐点

答案: B

**解析:**解 先分析<equation>f(x)</equation>的性质，分别计算<equation>f^{\prime}(x)</equation>，<equation>f^{\prime \prime}(x)</equation>. 根据链式法则，<equation>f ^ {\prime} (x) = \sin x \mathrm {e} ^ {x ^ {2}},</equation><equation>f ^ {\prime \prime} (x) = 2 x \sin x \mathrm {e} ^ {x ^ {2}} + \cos x \mathrm {e} ^ {x ^ {2}} = \left(2 x \sin x + \cos x\right) \mathrm {e} ^ {x ^ {2}}.</equation>取<equation>\delta</equation>为充分小的正数，当<equation>x\in(-\delta,0)</equation>时，<equation>f^{\prime}(x)<0,f(x)</equation>单调减少，当<equation>x\in(0,\delta)</equation>时，<equation>f^{\prime}(x) > 0,f(x)</equation>单调增加.于是，<equation>x=0</equation>是<equation>f(x)</equation>的极小值点.或者，也可以由<equation>f^{\prime}(0)=0,f^{\prime\prime}(0)=1>0</equation>以及极值的第二充分条件得到<equation>x=0</equation>是<equation>f(x)</equation>的极小值点.

当<equation>x \in(-\delta ,\delta)</equation>时，<equation>x\sin x\geqslant0,\cos x > 0,f^{\prime \prime}(x)</equation>在<equation>(-\delta ,\delta)</equation>内恒大于0，<equation>y=f(x)</equation>是凹曲线。于是，点（0，0）不是曲线<equation>y=f(x)</equation>的拐点.

再分析<equation>g(x)</equation>的性质，分别计算<equation>g^{\prime}(x), g^{\prime \prime}(x)</equation>.根据链式法则，<equation>g ^ {\prime} (x) = \sin^ {2} x \mathrm {e} ^ {x ^ {2}} + 2 \sin x \cos x \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = \sin^ {2} x \mathrm {e} ^ {x ^ {2}} + \sin 2 x \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t,</equation><equation>\begin{aligned} g ^ {\prime \prime} (x) &= 2 \sin x \cos x \mathrm {e} ^ {x ^ {2}} + 2 x \sin^ {2} x \mathrm {e} ^ {x ^ {2}} + \sin 2 x \mathrm {e} ^ {x ^ {2}} + 2 \cos 2 x \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t \\ &= 2 \left(\sin 2 x + x \sin^ {2} x\right) \mathrm {e} ^ {x ^ {2}} + 2 \cos 2 x \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t. \end{aligned}</equation>取<equation>\delta</equation>为充分小的正数，由于<equation>\mathrm{e}^{t^2}</equation>恒大于0，故当<equation>x\in(-\delta,0)</equation>时，<equation>\int_0^x\mathrm{e}^{t^2}\mathrm{d}t < 0</equation>，结合<equation>\sin 2x < 0</equation>可得，<equation>g^{\prime}(x) > 0,g(x)</equation>单调增加，当<equation>x\in(0,\delta)</equation>时，<equation>\int_0^x\mathrm{e}^{t^2}\mathrm{d}t > 0</equation>，结合<equation>\sin 2x > 0</equation>可得，<equation>g^{\prime}(x) > 0,g(x)</equation>单调增加.于是，<equation>x = 0</equation>不是<equation>g(x)</equation>的极值点.

当<equation>x \in(-\delta,0)</equation>时，<equation>\sin 2x+x\sin^{2}x<0,\int_{0}^{x}\mathrm{e}^{t^{2}}\mathrm{d}t<0,\cos 2x>0,g^{\prime \prime}(x)<0,y=g(x)</equation>是凸曲线，当<equation>x \in(0,\delta)</equation>时，<equation>\sin 2x+x\sin^{2}x>0,\int_{0}^{x}\mathrm{e}^{t^{2}}\mathrm{d}t>0,\cos 2x>0,g^{\prime \prime}(x)>0,y=g(x)</equation>是凹曲线.于是，点（0,0）是曲线<equation>y=g(x)</equation>的拐点.

综上所述，应选B.

---

**2023年第1题 | 选择题 | 5分 | 答案: B**

1. 曲线<equation>y=x\ln \left(\mathrm{e}+\frac{1}{x-1}\right)</equation>的斜渐近线方程为（    )

A.<equation>y=x+\mathrm{e}</equation>B.<equation>y=x+\frac{1}{\mathrm{e}}</equation>C.<equation>y=x</equation>D.<equation>y=x-\frac{1}{\mathrm{e}}</equation>

答案: B

**解析:**先计算<equation>\lim_{x\to \infty}\frac{y}{x}</equation>.<equation>\lim _ {x \rightarrow \infty} \frac {y}{x} = \lim _ {x \rightarrow \infty} \frac {x \ln \left(\mathrm {e} + \frac {1}{x - 1}\right)}{x} = \lim _ {x \rightarrow \infty} \ln \left(\mathrm {e} + \frac {1}{x - 1}\right) = 1.</equation>由此可得斜渐近线的斜率为1.

下面计算<equation>\lim_{x\to \infty}(y-x).</equation>

<equation>\begin{aligned} \lim_{x \rightarrow \infty} (y - x) &= \lim_{x \rightarrow \infty}

  \left[ x \ln \left(\mathrm{e} + \frac{1}{x - 1}\right) - x \right] \\ &= \lim_{x
  \rightarrow \infty} x \left[ \ln \left(\mathrm{e} + \frac{1}{x - 1}\right) - 1 \right]
   \\ &= \lim_{x \rightarrow \infty} x \left[ \ln \left(\mathrm{e} + \frac{1}{x -
  1}\right) - \ln \mathrm{e} \right] \\ &= \lim_{x \rightarrow \infty} x \ln \left[ 1 +
  \frac{1}{\mathrm{e}(x - 1)} \right] \\ &= \underline{\underline{\ln \left[ 1 +
  \frac{1}{\mathrm{e}(x - 1)} \right] \sim \frac{1}{\mathrm{e}(x - 1)}}} \lim_{x
  \rightarrow \infty} x \cdot \frac{1}{\mathrm{e}(x - 1)} \\ &= \frac{1}{\mathrm{e}}.
  \end{aligned}

</equation>

因此，曲线<equation>y=x\ln \left(\mathrm{e}+\frac{1}{x-1}\right)</equation>的斜渐近线方程为<equation>y=x+\frac{1}{\mathrm{e}}.</equation>应选B.

---

**2022年第20题 | 解答题 | 12分**

20. (本题满分12分）

设函数 f(x)在<equation>(-\infty,+\infty)</equation>上有二阶连续导数，证明：<equation>f^{\prime \prime}(x)\geqslant0</equation>的充分必要条件是对任意不同的实数 a,b，都有<equation>f\left(\frac{a+b}{2}\right)\leqslant\frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x</equation>成立.

**解析:**先证明必要性，即证明，若<equation>f^{\prime \prime}(x)\geqslant 0</equation>，则对不同的实数a,b，有<equation>f \left(\frac {a + b}{2}\right) \leqslant \frac {1}{b - a} \int_ {a} ^ {b} f (x) \mathrm {d} x.</equation>（法一）不妨设<equation>b > a</equation>. 在区间<equation>[a,b]</equation>上，使用<equation>f(x)</equation>在点<equation>\frac{a + b}{2}</equation>处的一阶泰勒公式.<equation>f (x) = f \left(\frac {a + b}{2}\right) + f ^ {\prime} \left(\frac {a + b}{2}\right) \left(x - \frac {a + b}{2}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a + b}{2}\right) ^ {2},</equation>其中<equation>\xi_{x}</equation>介于 x与<equation>\frac{a+b}{2}</equation>之间.

将（1）式代入<equation>\int_{a}^{b} f(x)\mathrm{d}x</equation>，可得

<equation>\begin{aligned} \int_{a}^{b} f(x) \mathrm{d}x &= \int_{a}^{b} \left[ f\left(\frac{a +

  b}{2}\right) + f^{\prime}\left(\frac{a + b}{2}\right)\left(x - \frac{a + b}{2}\right)
  + \frac{1}{2} f^{\prime \prime}\left(\xi_{x}\right)\left(x - \frac{a +
  b}{2}\right)^{2} \right] \mathrm{d}x \\ &= f\left(\frac{a + b}{2}\right)(b - a) +
  f^{\prime}\left(\frac{a + b}{2}\right) \int_{a}^{b} \left(x - \frac{a + b}{2}\right)
  \mathrm{d}x \\ &\quad + \frac{1}{2} \int_{a}^{b} f^{\prime
  \prime}\left(\xi_{x}\right)\left(x - \frac{a + b}{2}\right)^{2} \mathrm{d}x.
  \end{aligned}

</equation>

注意到<equation>\int_ {a} ^ {b} \left(x - \frac {a + b}{2}\right) \mathrm {d} x = \frac {x ^ {2}}{2} \Big | _ {a} ^ {b} - \frac {(a + b) (b - a)}{2} = \frac {b ^ {2} - a ^ {2}}{2} - \frac {b ^ {2} - a ^ {2}}{2} = 0,</equation>故<equation>\int_ {a} ^ {b} f (x) \mathrm {d} x = f \left(\frac {a + b}{2}\right) (b - a) + \frac {1}{2} \int_ {a} ^ {b} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a + b}{2}\right) ^ {2} \mathrm {d} x.</equation>结合<equation>f^{\prime \prime}(x)\geqslant 0</equation>可得<equation>\int_{a}^{b}f(x)\mathrm{d}x\geqslant f\left(\frac{a+b}{2}\right)(b-a)</equation>，即<equation>f\left(\frac{a+b}{2}\right)\leqslant \frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x.</equation>法二）不妨设<equation>b > a.</equation><equation>f\left(\frac{a + b}{2}\right)\leqslant \frac{1}{b - a}\int_{a}^{b}f(x)\mathrm{d}x</equation>等价于<equation>f\left(\frac{a + b}{2}\right)(b - a) - \int_{a}^{b}f(x)\mathrm{d}x\leqslant 0</equation>令<equation>F ( x ) = \int_{a}^{x} f ( t ) \mathrm{d} t - f \left( \frac{a + x}{2} \right) ( x - a ) , x \in [ a, b ]</equation>，则<equation>F ( a ) = 0</equation>，且<equation>\begin{aligned} F ^ {\prime} (x) &= f (x) - f \left(\frac {a + x}{2}\right) - f ^ {\prime} \left(\frac {a + x}{2}\right) \frac {x - a}{2} \frac {\text {拉 格 朗 日}}{\text {中 值 定 理}} f ^ {\prime} \left(\eta_ {x}\right) \frac {x - a}{2} - f ^ {\prime} \left(\frac {a + x}{2}\right) \frac {x - a}{2} \\ &= \left[ f ^ {\prime} \left(\eta_ {x}\right) - f ^ {\prime} \left(\frac {a + x}{2}\right) \right] \frac {x - a}{2}, \end{aligned}</equation>其中<equation>\eta_{x}\in \left(\frac{a + x}{2},x\right)</equation>由于<equation>f^{\prime \prime}(x)\geqslant 0</equation>，故<equation>f^{\prime}(x)</equation>单调不减，从而<equation>f^{\prime}(\eta_{x})\geqslant f^{\prime}\left(\frac{a+x}{2}\right)</equation>即<equation>f^{\prime}(\eta_{x})-f^{\prime}\left(\frac{a+x}{2}\right)\geqslant 0.</equation>于是，对<equation>x\in(a,b),F^{\prime}(x)\geqslant 0,F(x)</equation>在<equation>[a,b]</equation>上单调不减.

又因为<equation>F(a) = 0</equation>，所以<equation>F(b)\geqslant F(a) = 0</equation>，即<equation>\int_{a}^{b}f(x)\mathrm{d}x\geqslant f\left(\frac{a + b}{2}\right)(b - a)</equation>.

下面证明充分性，即证明，若对不同的实数 a,b,f<equation>\left(\frac{a+b}{2}\right)\leqslant\frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x</equation>，则<equation>f^{\prime\prime}(x)\geqslant0.</equation>（法一）反证法.

假设存在<equation>x_{0}</equation>，使得<equation>f^{\prime \prime}(x_{0})<0</equation>，由二阶导数连续可得<equation>\lim_{x\to x_{0}}f^{\prime \prime}(x)=f^{\prime \prime}(x_{0})<0</equation>，结合极限的局部保号性可知，存在<equation>\delta >0</equation>，在区间<equation>(x_{0}-\delta,x_{0}+\delta)</equation>内，均有<equation>f^{\prime \prime}(x)<0</equation>.从而取<equation>[a_{0},b_{0}]\subset(x_{0}-\delta,x_{0}+\delta)</equation>可得在<equation>[a_{0},b_{0}]</equation>上，均有<equation>f^{\prime \prime}(x)<0.</equation>在区间<equation>[ a_{0}, b_{0} ]</equation>上重复必要性中的做法.<equation>\begin{aligned} \int_ {a _ {0}} ^ {b _ {0}} f (x) \mathrm {d} x &= \int_ {a _ {0}} ^ {b _ {0}} \left[ f \left(\frac {a _ {0} + b _ {0}}{2}\right) + f ^ {\prime} \left(\frac {a _ {0} + b _ {0}}{2}\right) \left(x - \frac {a _ {0} + b _ {0}}{2}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a _ {0} + b _ {0}}{2}\right) ^ {2} \right] \mathrm {d} x \\ &= f \left(\frac {a _ {0} + b _ {0}}{2}\right) \left(b _ {0} - a _ {0}\right) + f ^ {\prime} \left(\frac {a _ {0} + b _ {0}}{2}\right) \int_ {a _ {0}} ^ {b _ {0}} \left(x - \frac {a _ {0} + b _ {0}}{2}\right) \mathrm {d} x \\ + \frac {1}{2} \int_ {a _ {0}} ^ {b _ {0}} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a _ {0} + b _ {0}}{2}\right) ^ {2} \mathrm {d} x, \end{aligned}</equation>其中<equation>\xi_{x}</equation>介于 x与<equation>\frac{a_{0}+b_{0}}{2}</equation>之间.

于是，<equation>\int_ {a _ {0}} ^ {b _ {0}} f (x) \mathrm {d} x = f \left(\frac {a _ {0} + b _ {0}}{2}\right) \left(b _ {0} - a _ {0}\right) + \frac {1}{2} \int_ {a _ {0}} ^ {b _ {0}} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a _ {0} + b _ {0}}{2}\right) ^ {2} \mathrm {d} x.</equation>结合<equation>f^{\prime \prime}(x) < 0</equation>可得<equation>\int_{a_0}^{b_0} f(x)\mathrm{d}x < f\left(\frac{a_0 + b_0}{2}\right)\left(b_0 - a_0\right)</equation>，即<equation>f\left(\frac{a_0 + b_0}{2}\right) > \frac{1}{b_0 - a_0}\int_{a_0}^{b_0} f(x)\mathrm{d}x.</equation>这与前提矛盾.

因此，假设不正确.<equation>f^{\prime \prime}(x)</equation>在<equation>(-\infty , +\infty)</equation>上恒非负.

（法二）若对不同的实数<equation>a,b,f\left(\frac{a + b}{2}\right)\leqslant \frac{1}{b - a}\int_{a}^{b}f(x)\mathrm{d}x</equation>，则对任意实数<equation>x_0</equation>以及任意<equation>\delta > 0</equation>，均有<equation>\int_{x_0 - \delta}^{x_0 + \delta}f(x)\mathrm{d}x - 2\delta f(x_0)\geqslant 0</equation>，从而<equation>\frac{\int_{x_0 - \delta}^{x_0 + \delta}f(x)\mathrm{d}x - 2\delta f(x_0)}{\delta^3}\geqslant 0.</equation>而<equation>\begin{aligned} \lim _ {\delta \rightarrow 0 ^ {+}} \frac {\int_ {x _ {0} - \delta} ^ {x _ {0} + \delta} f (x) \mathrm {d} x - 2 \delta f \left(x _ {0}\right)}{\delta^ {3}} \stackrel {\text {洛必达}} {=} \lim _ {\delta \rightarrow 0 ^ {+}} \frac {f \left(x _ {0} + \delta\right) + f \left(x _ {0} - \delta\right) - 2 f \left(x _ {0}\right)}{3 \delta^ {2}} \\ \stackrel {\text {洛必达}} {=} \lim _ {\delta \rightarrow 0 ^ {+}} \frac {f ^ {\prime} \left(x _ {0} + \delta\right) - f ^ {\prime} \left(x _ {0} - \delta\right)}{6 \delta} \\ \stackrel {\text {洛必达}} {=} \lim _ {\delta \rightarrow 0 ^ {+}} \frac {f ^ {\prime \prime} \left(x _ {0} + \delta\right) + f ^ {\prime \prime} \left(x _ {0} - \delta\right)}{6} \\ \stackrel {f ^ {\prime \prime} \text {连 续}} {=} \frac {1}{3} f ^ {\prime \prime} \left(x _ {0}\right), \end{aligned}</equation>故由极限的保号性可知，<equation>f^{\prime \prime}\left(x_{0}\right)\geqslant 0.</equation>由<equation>x_0</equation>的任意性可知，对不同的实数<equation>a,b,f\left(\frac{a + b}{2}\right)\leqslant \frac{1}{b - a}\int_{a}^{b}f(x)\mathrm{d}x</equation>是<equation>f^{\prime \prime}(x)\geqslant 0</equation>的充分条件.

综上所述，<equation>f^{\prime \prime}(x)\geqslant 0</equation>的充分必要条件是对不同的实数a,b，<equation>f\left(\frac{a+b}{2}\right)\leqslant \frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x.</equation>

---

**2015年第1题 | 选择题 | 4分 | 答案: C**

1. 设函数 f(x)在<equation>(-\infty,+\infty)</equation>上连续，其2阶导函数<equation>f^{\prime\prime}(x)</equation>的图形如图所示，则曲线 y=f(x)的拐点个数为（    ）

A. 0 B. 1 C. 2 D. 3

答案: C

**解析:**图可知，在<equation>(-\infty, +\infty)</equation>上，<equation>f^{\prime \prime}(x) = 0</equation>有两个实根<equation>x_{1}, x_{2}</equation>，且<equation>f^{\prime \prime}(x)</equation>在<equation>x=0</equation>处无定义.

下面我们分别讨论点<equation>(x_{1}, f(x_{1}))</equation>，<equation>(0, f(0))</equation>和<equation>(x_{2}, f(x_{2}))</equation>是否为拐点.

在<equation>x = x_{1}</equation>的左、右邻域内，<equation>f^{\prime \prime}(x)</equation>均大于零.<equation>f^{\prime \prime}(x)</equation>在该点两侧不变号，故点<equation>(x_{1}, f(x_{1}))</equation>不是曲线<equation>y = f(x)</equation>的拐点.

在<equation>x = 0</equation>的左侧邻域内，<equation>f^{\prime \prime}(x) > 0</equation>；在<equation>x = 0</equation>的右侧邻域内，<equation>f^{\prime \prime}(x) < 0</equation><equation>f^{\prime \prime}(x)</equation>在该点两侧变号，故点（0，<equation>f(0)</equation>）是曲线<equation>y = f(x)</equation>的拐点.

在<equation>x = x_{2}</equation>的左侧邻域内，<equation>f^{\prime \prime}(x) < 0</equation>；在<equation>x = x_{2}</equation>的右侧邻域内，<equation>f^{\prime \prime}(x) > 0</equation>.<equation>f^{\prime \prime}(x)</equation>在该点两侧变号，故点<equation>(x_{2}, f(x_{2}))</equation>是曲线<equation>y = f(x)</equation>的拐点.

综上所述，曲线<equation>y=f(x)</equation>共有2个拐点，应选C.

---

**2014年第1题 | 选择题 | 4分 | 答案: C**

1. 下列曲线中有渐近线的是（    ）

A. y=x+<equation>\sin x</equation>B. y=x²+<equation>\sin x</equation>C. y=x+<equation>\sin \frac{1}{x}</equation>D. y=x²+<equation>\sin \frac{1}{x}</equation>

答案: C

**解析:**解 先考察各曲线是否具有铅直渐近线.<equation>y = x + \sin x, y = x^{2} + \sin x</equation>在<equation>(-\infty , +\infty)</equation>上均无间断点，故不存在铅直渐近线；<equation>y = x + \sin \frac{1}{x}</equation>和<equation>y = x^{2} + \sin \frac{1}{x}</equation>在<equation>x = 0</equation>处无定义，但<equation>\lim_{x\to 0}\sin \frac{1}{x}</equation>不存在，从而也没有铅直渐近线.

再考察它们是否具有水平渐近线.

由于选项A、B、C、D中的曲线在<equation>x\to +\infty</equation>和<equation>x\to -\infty</equation>时均趋于<equation>\infty</equation>，故它们均没有水平渐近线最后考察它们是否具有斜渐近线.

对选项C，<equation>\lim\limits_{x\to \infty}\frac{x+\sin \frac{1}{x}}{x}=1</equation>，且<equation>\lim\limits_{x\to \infty}\left(x+\sin \frac{1}{x}-x\right)=\lim\limits_{x\to \infty}\sin \frac{1}{x}=0</equation>，故<equation>y=x+\sin \frac{1}{x}</equation>有斜渐近线<equation>y=x</equation>.应选C.

下面我们说明选项A、B、D没有斜渐近线.

对选项 A，<equation>\lim_{x\to \infty}\frac{x+\sin x}{x}=1</equation>，但<equation>\lim_{x\to \infty}\left(x+\sin x-x\right)=\lim_{x\to \infty}\sin x</equation>，而<equation>\lim_{x\to \infty}\sin x</equation>不存在，故选项 A 没有斜渐近线.

对选项B，<equation>\lim_{x\to \infty}\frac{x^{2}+\sin x}{x}=\infty</equation>；对选项D，<equation>\lim_{x\to \infty}\frac{x^{2}+\sin \frac{1}{x}}{x}=\infty</equation>，故选项B和选项D都没有斜渐近线.

---

**2014年第2题 | 选择题 | 4分 | 答案: D**

2. 设函数 f(x)具有2阶导数，<equation>g ( x )=f ( 0 ) ( 1-x )+f ( 1 ) x</equation>，则在区间[0,1]上（    ）

A. 当<equation>f^{\prime}(x)\geqslant0</equation>时，<equation>f(x)\geqslant g(x)</equation>B. 当<equation>f^{\prime}(x)\geqslant0</equation>时，<equation>f(x)\leqslant g(x)</equation>C. 当<equation>f^{\prime\prime}(x)\geqslant0</equation>时，<equation>f(x)\geqslant g(x)</equation>D. 当<equation>f^{\prime\prime}(x)\geqslant0</equation>时，<equation>f(x)\leqslant g(x)</equation>

答案: D

**解析:**分析 本题主要考查曲线的凹凸性. 对此类题，常用数形结合的方法.

(a)

(b)

设<equation>f(x)</equation>在区间 I上连续，<equation>x_{1}, x_{2}</equation>为 I中任意两点.不妨设<equation>x_{1} < x_{2}</equation>.

- 若恒有<equation>f\left(\frac{x_{1} + x_{2}}{2}\right) < \frac{f\left(x_{1}\right) + f\left(x_{2}\right)}{2}</equation>，则称曲线<equation>y = f(x)</equation>在区间I上凹，如图（a）；

- 若恒有<equation>f\left(\frac{x_{1} + x_{2}}{2}\right) > \frac{f\left(x_{1}\right) + f\left(x_{2}\right)}{2}</equation>，则称曲线<equation>y = f(x)</equation>在区间I上凸，如图(b).

从图形上看，过凹曲线<equation>y=f(x)</equation>上的任意两点的弦<equation>y=g(x)</equation>均位于该曲线之上，即<equation>f(x)\leqslant g(x)</equation>；过凸曲线<equation>y=f(x)</equation>上的任意两点的弦<equation>y=g(x)</equation>均位于该曲线之下，即<equation>f(x)\geqslant g(x).</equation>解 由于<equation>g ( x )=\frac{f ( 1 )-f ( 0 )}{1-0} x+f ( 0 ) , g ( 0 )=f ( 0 )</equation><equation>g ( 1 )=f ( 1 )</equation>，故<equation>y=g ( x )</equation>表示的曲线是过点（0，f(0)），（1，f(1)）的弦.

由分析知，若<equation>y=f(x)</equation>在[0，1]上凹，则<equation>f(x)\leqslant g(x)</equation>；若<equation>y=f(x)</equation>在[0，1]上凸，则<equation>f(x)\geqslant g(x).</equation>由于f(x）具有2阶导数，故曲线的凹凸性可以由<equation>f^{\prime \prime}(x)</equation>确定.当<equation>f^{\prime \prime}(x)\geqslant 0</equation>时，<equation>y=f(x)</equation>在[0，1]上凹，从而<equation>f(x)\leqslant g(x).</equation>应选D.

一阶导数的符号与曲线的凹凸性没有直接关系。作为选项A的反例，可以考虑曲线<equation>y=x^{2}</equation>；作为选项B的反例，可以考虑曲线<equation>y=\sqrt{x}.</equation>

---

**2012年第1题 | 选择题 | 4分 | 答案: C**

1. 曲线<equation>y=\frac{x^{2}+x}{x^{2}-1}</equation>的渐近线的条数为（    ）

A.0 B.1 C.2 D.3

答案: C

**解析:**先判断曲线的铅直渐近线

由于<equation>y = \frac{x^2 + x}{x^2 - 1}</equation>在<equation>x = \pm 1</equation>时间断，故可以分别考虑<equation>\lim_{x\to -1}\frac{x^2 + x}{x^2 - 1}</equation>和<equation>\lim_{x\to 1}\frac{x^2 + x}{x^2 - 1}</equation>.

由于<equation>\lim_{x\to -1}\frac{x^2 + x}{x^2 - 1} = \lim_{x\to -1}\frac{x}{x - 1} = \frac{1}{2}</equation>，故<equation>x = -1</equation>为<equation>y(x)</equation>的可去间断点.

由于<equation>\lim_{x\to 1}\frac{x^{2}+x}{x^{2}-1}=\lim_{x\to 1}\frac{x}{x-1}=\infty</equation>，故 x=1为 y(x)的无穷间断点.直线 x=1为曲线的铅直渐近线.

再判断曲线的水平渐近线

由于<equation>\lim_{x\to \infty}\frac{x^2 + x}{x^2 - 1} = 1</equation>，故直线<equation>y = 1</equation>为曲线的水平渐近线最后，由于<equation>\lim _ {\substack {x \rightarrow \infty \\ (x \rightarrow + \infty \text{ 或 } x \rightarrow - \infty)}} \frac {y (x)}{x} = \lim _ {\substack {x \rightarrow \infty \\ (x \rightarrow +\infty \text{ 或 } x \rightarrow -\infty)}} \frac {x + 1}{x ^ {2} - 1} = \lim _ {\substack {x \rightarrow \infty \\ (x \rightarrow +\infty \text{ 或 } x \rightarrow -\infty)}} \frac {1}{x - 1} = 0,</equation>故曲线没有斜渐近线

综上所述，曲线共有2条渐近线，如图所示. 应选C.

---

**2011年第1题 | 选择题 | 4分 | 答案: C**

1. 曲线<equation>y=(x-1)(x-2)^{2}(x-3)^{3}(x-4)^{4}</equation>的拐点是（    )

A. (1,0) B. (2,0) C. (3,0) D. (4,0)

答案: C

**解析:**解（法一）令<equation>f ( x ) = ( x - 1 ) ( x - 2 )^{2} ( x - 3 )^{3} ( x - 4 )^{4}</equation>，则<equation>x = 2,3,4</equation>作为<equation>f ( x ) = 0</equation>的根的重数分别为2，3，4，从而由分析中的性质知，<equation>f ^ {\prime \prime} (2) \neq 0, \quad f ^ {\prime \prime} (3) = 0, \quad f ^ {\prime \prime \prime} (3) \neq 0, \quad f ^ {\prime \prime} (4) = f ^ {\prime \prime \prime} (4) = 0, \quad f ^ {(4)} (4) \neq 0.</equation>再由拐点的判别法3知，点（3，0）是拐点，故选C.

对于其他选项，由拐点的判别法1知，点（2,0）不是拐点；由拐点的判别法4知，点（4,0）不是拐点.

对于<equation>x = 1</equation>，令<equation>g(x) = (x - 2)^{2}(x - 3)^{3}(x - 4)^{4}</equation>，则<equation>f(x) = (x - 1)g(x)</equation>，从而<equation>f ^ {\prime} (x) = g (x) + (x - 1) g ^ {\prime} (x), \quad f ^ {\prime \prime} (x) = 2 g ^ {\prime} (x) + (x - 1) g ^ {\prime \prime} (x),</equation>故<equation>\begin{aligned} f ^ {\prime \prime} (1) &= 2 g ^ {\prime} (1) = 2 \left[ 2 (x - 2) (x - 3) ^ {3} (x - 4) ^ {4} + 3 (x - 2) ^ {2} (x - 3) ^ {2} (x - 4) ^ {4} \right. \\ + 4 (x - 2) ^ {2} (x - 3) ^ {3} (x - 4) ^ {3} ] \mid_ {x = 1} \\ &= 2 \left[ 2 (- 1) \cdot (- 2) ^ {3} \cdot (- 3) ^ {4} + 3 (- 1) ^ {2} \cdot (- 2) ^ {2} \cdot (- 3) ^ {4} \right. \\ + 4 (- 1) ^ {2} \cdot (- 2) ^ {3} \cdot (- 3) ^ {3} ] \\ &= 2 \left(2 ^ {4} \cdot 3 ^ {4} + 2 ^ {2} \cdot 3 ^ {5} + 2 ^ {5} \cdot 3 ^ {3}\right) > 0. \end{aligned}</equation>由拐点的判别法1知，点（1，0）不是拐点.

（法二）排除法.

穿针引线法 设多项式的最高次项系数大于零。从数轴上最右边的根的右上方开始穿根，根据零点的重数的奇偶性决定穿或者不穿，即奇穿偶不穿，或奇穿偶回.

由穿针引线法可得曲线<equation>y = (x - 1) (x - 2)^{2} (x - 3)^{3} (x - 4)^{4}</equation>的图像大致如右图.

对于多项式函数或存在任意阶导数的函数<equation>f(x)</equation>，设点<equation>(x_{0}, f(x_{0}))</equation>为曲线<equation>y = f(x)</equation>上一点，则有如下结论.

(1) 若<equation>x_{0}</equation>是<equation>f(x)</equation>的极值点，则点<equation>\left(x_{0},f\left(x_{0}\right)\right)</equation>一定不是曲线<equation>y=f(x)</equation>的拐点.

(2) 若点<equation>(x_0,f(x_0))</equation>是曲线<equation>y = f(x)</equation>的拐点，则<equation>x_0</equation>也一定不是<equation>f(x)</equation>的极值点.

计算<equation>f^{\prime \prime}(1)</equation>可得<equation>f^{\prime \prime}(1) \neq 0</equation>，故点（1,0）不是<equation>y = f(x)</equation>的拐点.

由图可知，<equation>x=2</equation>是 f(x)的极大值点，<equation>x=4</equation>是 f(x)的极小值点，故点（2，0），点（4，0）均不是曲线<equation>y=f(x)</equation>的拐点.

由排除法知，应选C.

（法三）令<equation>f ( x ) = ( x - 1 ) ( x - 2 )^{2} ( x - 3 )^{3} ( x - 4 )^{4}</equation><equation>f_{1}(x) = (x - 2)^{2}(x - 3)^{3}(x - 4)^{4},</equation><equation>f_{2}(x) = (x - 1)(x - 3)^{3}(x - 4)^{4}, f_{3}(x) = (x - 1)(x - 2)^{2}(x - 4)^{4}, f_{4}(x) = (x - 1)(x - 2)^{2}(x - 3)^{3},</equation>易知<equation>f_{1}(1), f_{2}(2), f_{3}(3), f_{4}(4)\neq 0</equation>，且<equation>f ( x )</equation>在<equation>x = 1, 2, 3, 4</equation>处的泰勒公式分别为<equation>\begin{aligned} f (x) &= (x - 1) f _ {1} (x) = (x - 1) \left[ f _ {1} (1) + f _ {1} ^ {\prime} (1) (x - 1) + \dots + \frac {f _ {1} ^ {(9)} (1)}{9 !} (x - 1) ^ {9} \right] \\ &= f _ {1} (1) (x - 1) + f _ {1} ^ {\prime} (1) (x - 1) ^ {2} + \dots + \frac {f _ {1} ^ {(9)} (1)}{9 !} (x - 1) ^ {1 0}, \end{aligned}</equation><equation>f (x) = (x - 2) ^ {2} f _ {2} (x) = f _ {2} (2) (x - 2) ^ {2} + f _ {2} ^ {\prime} (2) (x - 2) ^ {3} + \dots + \frac {f _ {2} ^ {(8)} (2)}{8 !} (x - 2) ^ {1 0},</equation><equation>f_{1}(x)</equation>为9次多项式，故<equation>f_{1}(x)</equation>在<equation>x=</equation>1处的泰勒公式中 x-1的最高幂次为9.<equation>f (x) = (x - 3) ^ {3} f _ {3} (x) = f _ {3} (3) (x - 3) ^ {3} + f _ {3} ^ {\prime} (3) (x - 3) ^ {4} + \dots + \frac {f _ {3} ^ {(7)} (3)}{7 !} (x - 3) ^ {1 0},</equation><equation>f (x) = (x - 4) ^ {4} f _ {4} (x) = f _ {4} (4) (x - 4) ^ {4} + f _ {4} ^ {\prime} (4) (x - 4) ^ {5} + \dots + \frac {f _ {4} ^ {(6)} (4)}{6 !} (x - 4) ^ {1 0}.</equation>由<equation>f(x)</equation>在<equation>x = 3</equation>处的泰勒公式知，<equation>(x - 3)^{2}</equation>的系数为0，<equation>(x - 3)^{3}</equation>的系数为<equation>f_{3}(3)</equation>. 再由泰勒公式的唯一性知，<equation>\frac{f^{\prime \prime}(3)}{2!} = 0,\frac{f^{\prime \prime \prime}(3)}{3!} = f_{3}(3)</equation>，从而<equation>f ^ {\prime \prime} (3) = 0, f ^ {\prime \prime \prime} (3) = 3! \cdot f _ {3} (3) \neq 0.</equation>由拐点的判别法3知，点（3,0）是曲线<equation>y=f(x)</equation>的拐点.因此，应选C.

对于其他选项，由泰勒公式的唯一性知，<equation>f ^ {\prime \prime} (1) = 2! \cdot f _ {1} ^ {\prime} (1) = 2 \left[ 2 (x - 2) (x - 3) ^ {3} (x - 4) ^ {4} + 3 (x - 2) ^ {2} (x - 3) ^ {2} (x - 4) ^ {4} + \right.</equation><equation>4 (x - 2) ^ {2} (x - 3) ^ {3} (x - 4) ^ {3} \big ] \mid_ {x = 1} = 2 \left(2 ^ {4} \cdot 3 ^ {4} + 2 ^ {2} \cdot 3 ^ {5} + 2 ^ {5} \cdot 3 ^ {3}\right) > 0,</equation><equation>f ^ {\prime \prime} (2) = 2! \cdot f _ {2} (2) \neq 0,</equation><equation>f ^ {\prime \prime} (4) = f ^ {\prime \prime \prime} (4) = 0, f ^ {(4)} (4) = 4! \cdot f _ {4} (4) \neq 0,</equation>于是由拐点的判别法1知，点（1,0），（2,0）都不是拐点；由拐点的判别法4知，点（4,0）也不是拐点.

---


