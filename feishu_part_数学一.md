# 数学一


## 高等数学


### 一元函数微分学


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


#### 导数与微分的概念

**2025年第3题 | 选择题 | 5分 | 答案: D**

3. 设函数 f(x)在区间<equation>[0,+\infty)</equation>上可导，则（    )

A. 当<equation>\lim_{x\rightarrow+\infty}f(x)</equation>存在时，<equation>\lim_{x\rightarrow+\infty}f^{\prime}(x)</equation>存在

B. 当<equation>\lim_{x\rightarrow+\infty}f^{\prime}(x)</equation>存在时，<equation>\lim_{x\rightarrow+\infty}f(x)</equation>存在

C. 当<equation>\lim_{x\rightarrow+\infty}\frac{\int_{0}^{x}f(t)\mathrm{d}t}{x}</equation>存在时，<equation>\lim_{x\rightarrow+\infty}f(x)</equation>存在

D. 当<equation>\lim_{x\rightarrow+\infty}f(x)</equation>存在时，<equation>\lim_{x\rightarrow+\infty}\frac{\int_{0}^{x}f(t)\mathrm{d}t}{x}</equation>存在

答案: D

**解析:**解 对选项D，由于<equation>\lim_{x\rightarrow +\infty}f(x)</equation>存在，故可对<equation>\lim_{x\rightarrow +\infty}\frac{\int_{0}^{x}f(t)\mathrm{d}t}{x}</equation>应用洛必达法则得到<equation>\lim_{x\rightarrow +\infty}\frac{\int_{0}^{x}f(t)\mathrm{d}t}{x}\overset{\mathrm{洛必达}}{=}\lim_{x\rightarrow +\infty}\frac{f(x)}{1}=\lim_{x\rightarrow +\infty}f(x).</equation>由<equation>\lim_{x\to +\infty}f(x)</equation>存在可得<equation>\lim_{x\to +\infty}\frac{\int_0^x f(t)\mathrm{d}t}{x}</equation>存在.选项D正确.

因此，应选D.

下面说明选项A、B、C不正确.

对选项A，取<equation>f ( x )=\left\{\begin{array}{ll}\frac{\sin x^{2}}{x},&x\neq 0,\\ 0,&x=0,\end{array} \right.</equation>则<equation>\lim_{x\to 0}f(x)=\lim_{x\to 0}\frac{\sin x^{2}}{x^{2}}\cdot x=0=f(0),f^{\prime}(0)=</equation><equation>\lim_{x\to 0}\frac{\frac{\sin x^{2}}{x}-0}{x-0}=\lim_{x\to 0}\frac{\sin x^{2}}{x^{2}}=1,f(x)</equation>在<equation>x=0</equation>处可导，<equation>\lim_{x\to +\infty}f(x)=\lim_{x\to +\infty}\frac{\sin x^{2}}{x}=0</equation>，但当<equation>x\neq 0</equation>时，<equation>f^{\prime}(x)=\frac{x\cdot\cos x^{2}\cdot 2x-\sin x^{2}}{x^{2}}=2\cos x^{2}-\frac{\sin x^{2}}{x^{2}},\lim_{x\to +\infty}f^{\prime}(x)</equation>不存在. 对选项B，取<equation>f ( x )=x</equation>，则<equation>f^{\prime}(x)=1</equation>，<equation>\lim_{x\to +\infty}f^{\prime}(x)=1</equation>，但<equation>\lim_{x\to +\infty}f(x)</equation>不存在.

对选项C，取<equation>f ( x )=\cos x</equation>，则<equation>\int_{0}^{x} f ( t ) \mathrm{d} t=\sin x</equation><equation>\lim_{x\rightarrow+\infty}\frac{\int_{0}^{x} f ( t ) \mathrm{d} t}{x}=\lim_{x\rightarrow+\infty}\frac{\sin x}{x}=0</equation>，但<equation>\lim_{x\rightarrow+\infty}f ( x )</equation>不存在.

---

**2024年第4题 | 选择题 | 5分 | 答案: B**

4. 设函数 f(x)在区间（-1，1）上有定义，且<equation>\lim_{x\rightarrow 0}f(x)=0</equation>，则（    )

A. 当<equation>\lim_{x\rightarrow 0}\frac{f(x)}{x}=m</equation>时，<equation>f^{\prime}(0)=m</equation>B. 当<equation>f^{\prime}(0)=m</equation>时，<equation>\lim_{x\rightarrow 0}\frac{f(x)}{x}=m</equation>C. 当<equation>\lim_{x\rightarrow 0}f^{\prime}(x)=m</equation>时，<equation>f^{\prime}(0)=m</equation>D. 当<equation>f^{\prime}(0)=m</equation>时，<equation>\lim_{x\rightarrow 0}f^{\prime}(x)=m</equation>

答案: B

**解析:**解 若<equation>f^{\prime}(0)=m</equation>，则 f(x)在 x=0处连续.结合<equation>\lim_{x\to 0}f(x)=0</equation>可得 f(0)=0.由导数的定义可知<equation>\lim_{x\to 0}\frac{f(x)}{x}=\lim_{x\to 0}\frac{f(x)-f(0)}{x-0}=f^{\prime}(0)=m.</equation>因此，选项B正确.

下面说明选项A、C、D不正确.

对选项A、C，取<equation>f ( x )=\left\{\begin{array}{ll}m x,&x\neq 0\\ 1,&x=0\end{array} \right.</equation>则<equation>\lim_{x\to 0}\frac{f(x)}{x}=m</equation>，且<equation>\lim_{x\to 0}f^{\prime}(x)=m</equation>，但<equation>f ( x )</equation>在<equation>x=0</equation>处不连续，从而<equation>f^{\prime}(0)</equation>不存在.

对选项D，取<equation>f(x) = \left\{ \begin{array}{ll} m x + x^{2}\sin \frac{1}{x}, & x\neq 0, \\ 0, & x = 0, \end{array} \right.</equation>则<equation>f ^ {\prime} (0) = \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0} \frac {m x + x ^ {2} \sin \frac {1}{x}}{x} = m.</equation>但当<equation>x\neq 0</equation>时，<equation>f^{\prime}(x) = m + 2x\sin \frac{1}{x} -\cos \frac{1}{x},\lim_{x\to 0}f^{\prime}(x)</equation>不存在.

综上所述，应选B.

---

**2023年第3题 | 选择题 | 5分 | 答案: C**

3. 设函数 y=f(x)由<equation>\left\{\begin{array}{l l}x=2 t+|t|\\y=|t|\sin t\end{array}\right.</equation>确定，则（    )

A. f(x)连续，<equation>f^{\prime}(0)</equation>不存在 B.<equation>f^{\prime}(0)</equation>存在，<equation>f^{\prime}(x)</equation>在 x=0处不连续

C.<equation>f^{\prime}(x)</equation>连续，<equation>f^{\prime\prime}(0)</equation>不存在 D.<equation>f^{\prime\prime}(0)</equation>存在，<equation>f^{\prime\prime}(x)</equation>在 x=0处不连续

答案: C

**解析:**解 由于<equation>x=2 t+|t|=\left\{\begin{array}{ll}3 t,& t\geqslant 0\\ t,& t<0\end{array}\right.</equation>在<equation>(-\infty ,+\infty)</equation>上单调增加，且值域为<equation>(-\infty ,+\infty)</equation>，

故其存在反函数<equation>t=\left\{\begin{array}{ll}\frac{x}{3},& x\geqslant 0\\ x,& x<0.\end{array}\right.</equation>当<equation>x\geqslant 0</equation>时，<equation>t\geqslant 0</equation>；当<equation>x<0</equation>时，<equation>t<0</equation>．于是，<equation>f(x)=</equation>由其表达式可知，<equation>f(x)</equation>在<equation>x\neq0</equation>处连续．又由于<equation>\lim_{x\to 0}f(x)=0=f(0)</equation>，故<equation>f(x)</equation>在<equation>x=0</equation>处亦连续．因此<equation>f(x)</equation>连续.

计算可得<equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {f (x) - f (0)}{x - 0} \xlongequal {f (0) = 0} \lim _ {x \rightarrow 0 ^ {-}} \frac {- x \sin x}{x} = 0,</equation><equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x - 0} \xlongequal {f (0) = 0} \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {x}{3} \sin \frac {x}{3}}{x} = 0.</equation><equation>f(x)</equation>在<equation>x = 0</equation>处的左、右导数均存在且相等，故<equation>f^{\prime}(0)</equation>存在，且<equation>f^{\prime}(0) = 0.</equation>选项A不正确.

当 x < 0时，<equation>f ^ {\prime} (x) = \left(- x \sin x\right) ^ {\prime} = - \sin x - x \cos x.</equation>当 x > 0时，<equation>f ^ {\prime} (x) = \left(\frac {x}{3} \sin \frac {x}{3}\right) ^ {\prime} = \frac {1}{3} \left(\sin \frac {x}{3} + \frac {x}{3} \cos \frac {x}{3}\right).</equation>由此可知<equation>f^{\prime}(x)</equation>在<equation>x\neq0</equation>处连续.又由于<equation>\lim_{x\to0^{-}}f^{\prime}(x)=\lim_{x\to0^{+}}f^{\prime}(x)=0=f^{\prime}(0)</equation>，故<equation>f^{\prime}(x)</equation>在<equation>x=0</equation>处亦连续.因此<equation>f^{\prime}(x)</equation>连续.选项B不正确.

进一步计算可得，<equation>\begin{aligned} f _ {-} ^ {\prime \prime} (0) &= \lim _ {x \rightarrow 0 ^ {-}} \frac {f ^ {\prime} (x) - f ^ {\prime} (0)}{x - 0} \xlongequal {f ^ {\prime} (0) = 0} \lim _ {x \rightarrow 0 ^ {-}} \frac {- \sin x - x \cos x}{x} \\ &= - \lim _ {x \rightarrow 0 ^ {-}} \left(\frac {\sin x}{x} + \cos x\right) = - (1 + 1) = - 2, \end{aligned}</equation><equation>\begin{aligned} f _ {+} ^ {\prime \prime} (0) &= \lim _ {x \rightarrow 0 ^ {+}} \frac {f ^ {\prime} (x) - f ^ {\prime} (0)}{x - 0} \xlongequal {f ^ {\prime} (0) = 0} \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {1}{3} \left(\sin \frac {x}{3} + \frac {x}{3} \cos \frac {x}{3}\right)}{x} \\ &= \frac {1}{3} \lim _ {x \rightarrow 0 ^ {+}} \left(\frac {1}{3} \cdot \frac {\sin \frac {x}{3}}{\frac {x}{3}} + \frac {1}{3} \cos \frac {x}{3}\right) = \frac {1}{3} \times \left(\frac {1}{3} + \frac {1}{3}\right) = \frac {2}{9}. \end{aligned}</equation>由于<equation>f_{+}^{\prime \prime}(0)\neq f_{+}^{\prime \prime}(0),</equation>故<equation>f^{\prime \prime}(0)</equation>不存在.选项C正确，选项D不正确.

综上所述，应选C.

---

**2022年第1题 | 选择题 | 5分 | 答案: B**

1. 设函数 f(x)满足<equation>\lim_{x\to 1}\frac{f(x)}{\ln x}=1</equation>，则（    ）

A. f(1)=0 B.<equation>\lim_{x\to 1}f(x)=0</equation>C.<equation>f^{\prime}(1)=1</equation>D.<equation>\lim_{x\to 1}f^{\prime}(x)=1</equation>

答案: B

**解析:**解 当 x→1时，<equation>\lim_{x\rightarrow 1}\ln x=0</equation>，而<equation>\lim_{x\rightarrow 1}\frac{f(x)}{\ln x}=1</equation>，故分子 f(x)满足<equation>\lim_{x\rightarrow 1}f(x)=0</equation>.应选B.下面说明选项A、C、D不正确.

对选项A、C，可以举函数<equation>f(x)</equation>在<equation>x=1</equation>处不连续，从而也不可导的例子.

对选项D，若<equation>f(x)</equation>在<equation>x=1</equation>的某去心邻域内可导，且<equation>\lim_{x\to 1}f^{\prime}(x)</equation>存在，则由洛必达法则，<equation>\lim _ {x \rightarrow 1} \frac {f (x)}{\ln x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 1} \frac {f ^ {\prime} (x)}{\frac {1}{x}} = \lim _ {x \rightarrow 1} f ^ {\prime} (x).</equation>于是，<equation>\lim_{x\to 1}f^{\prime}(x)=\lim_{x\to 1}\frac{f(x)}{\ln x}=1.</equation>因此，要举出选项D的反例，需考虑 f(x)在 x=1的某去心邻域内不可导或者<equation>\lim_{x\to 1}f^{\prime}(x)</equation>不存在的例子.

考虑<equation>f ( x )=\left\{\begin{array}{ll}x-1+2(x-1)^{2}\sin \frac{1}{x-1},&x\neq 1,\\ 1,&x=1,\end{array} \right.</equation>则<equation>\lim_{x\to 1}f(x)=0</equation>，但<equation>f ( 1 )=1</equation><equation>f ( x )</equation>在<equation>x=1</equation>处不连续，也就不可导.

当<equation>x\neq 1</equation>时，<equation>f^{\prime}(x) = 1 + 4(x - 1)\sin \frac{1}{x - 1} - 2\cos \frac{1}{x - 1}</equation>. 不难发现，<equation>x = 1</equation>是<equation>f^{\prime}(x)</equation>的振荡间断点，<equation>\lim_{x\to 1}f^{\prime}(x)</equation>不存在.

---

**2021年第1题 | 选择题 | 5分 | 答案: D**

1. 函数 f(x) =<equation>\left\{\begin{array}{l l}{\frac{\mathrm{e}^{x}-1}{x},}&{x\neq0,}\\ {1,}&{x=0}\end{array} \right.</equation>在 x=0处（    ）

A. 连续且取得极大值 B. 连续且取得极小值 C. 可导且导数等于零 D. 可导且导数不为零

答案: D

**解析:**解 首先考虑 f(x)在 x=0处的连续性.<equation>\lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x} - 1}{x} \xlongequal {\mathrm {e} ^ {x} - 1 \sim x} \lim _ {x \rightarrow 0} \frac {x}{x} = 1 = f (0).</equation>于是，<equation>f ( x )</equation>在<equation>x=0</equation>处连续

下面考虑<equation>f ( x )</equation>在<equation>x=0</equation>处的可导性.<equation>f ^ {\prime} (0) = \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0} \frac {\frac {\mathrm {e} ^ {x} - 1}{x} - 1}{x} = \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x} - 1 - x}{x ^ {2}} \frac {\mathrm {e} ^ {x} = 1 + x + \frac {x ^ {2}}{2} + o \left(x ^ {2}\right)}{\frac {1}{2} \neq 0}.</equation>于是，<equation>f ( x )</equation>在<equation>x=0</equation>处可导且导数不为0.

因此，应选D.

下面说明选项A、B不正确.

由于<equation>f^{\prime}(0)\neq 0</equation>，故<equation>x = 0</equation>不满足成为极值点的必要条件，从而选项A、B均不正确.

---

**2020年第2题 | 选择题 | 4分 | 答案: C**

2. 设函数 f(x)在区间（-1，1）内有定义，且<equation>\lim_{x\rightarrow 0}f(x)=0</equation>，则（    )

A. 当<equation>\lim_{x\rightarrow 0}\frac{f(x)}{\sqrt{|x|}}=0</equation>时，f(x)在 x=0处可导 B. 当<equation>\lim_{x\rightarrow 0}\frac{f(x)}{x^{2}}=0</equation>时，f(x)在 x=0处可导

C. 当 f(x)在 x=0处可导时，<equation>\lim_{x\rightarrow 0}\frac{f(x)}{\sqrt{|x|}}=0</equation>D. 当 f(x)在 x=0处可导时，<equation>\lim_{x\rightarrow 0}\frac{f(x)}{x^{2}}=0</equation>

答案: C

**解析:**解 若 f(x)在 x=0处可导，则 f(x)在 x=0处连续.由<equation>\lim_{x\rightarrow 0}f(x)=0</equation>可得 f(0)=0.并且，由 f(x)在 x=0处可导可得<equation>f ^ {\prime} (0) = \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0} \xlongequal {f (0) = 0} \lim _ {x \rightarrow 0} \frac {f (x)}{x}.</equation>计算<equation>\lim_{x\to 0}\frac{f(x)}{\sqrt{|x|}}.</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {f (x)}{\sqrt {| x |}} = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x)}{\sqrt {x}} = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x)}{x} \cdot \sqrt {x} = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x)}{x} \cdot \lim _ {x \rightarrow 0 ^ {+}} \sqrt {x} = 0.</equation><equation>\lim _ {x \rightarrow 0 ^ {-}} \frac {f (x)}{\sqrt {| x |}} = \lim _ {x \rightarrow 0 ^ {-}} \frac {f (x)}{\sqrt {- x}} = \lim _ {x \rightarrow 0 ^ {-}} \frac {f (x)}{- x} \cdot \sqrt {- x} = - \lim _ {x \rightarrow 0 ^ {-}} \frac {f (x)}{x} \cdot \lim _ {x \rightarrow 0 ^ {-}} \sqrt {- x} = 0.</equation><equation>\lim_{x\to 0^{+}}\frac{f(x)}{\sqrt{|x|}} = \lim_{x\to 0^{-}}\frac{f(x)}{\sqrt{|x|}} = 0</equation>，即<equation>\lim_{x\to 0}\frac{f(x)}{\sqrt{|x|}} = 0.</equation>选项C正确.应选C.

下面说明其余选项均不正确.

选项A、B：取<equation>f ( x )=\left\{\begin{array}{ll}x^{3},&x\neq 0\\ 1,&x=0\end{array} \right.</equation>则<equation>\lim_{x\to 0}\frac{f(x)}{\sqrt{|x|}}=0,\lim_{x\to 0}\frac{f(x)}{x^{2}}=0</equation>，但<equation>f ( x )</equation>在<equation>x=0</equation>处不连续，当然也不可导.

选项D：取<equation>f ( x ) = x</equation>，则<equation>f ( x )</equation>在<equation>x=0</equation>处可导，但<equation>\lim_{x\to 0}\frac{f(x)}{x^{2}}</equation>不存在.

---

**2018年第1题 | 选择题 | 4分 | 答案: D**

1. 下列函数中，在 x=0处不可导的是（    ）

A. f(x）=|x|<equation>\sin |x|</equation>B. f(x)=|x|<equation>\sin \sqrt{|x|}</equation>C. f(x)=<equation>\cos |x|</equation>D. f(x)=<equation>\cos \sqrt{|x|}</equation>

答案: D

**解析:**考虑选项D.<equation>f (x) = \left\{ \begin{array}{l l} \cos \sqrt {x}, & x \geqslant 0, \\ \cos \sqrt {- x}, & x < 0. \end{array} \right.</equation><equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {\cos \sqrt {- x} - 1}{x - 0} \frac {\cos \sqrt {- x} - 1 \sim - \frac {\left(\sqrt {- x}\right) ^ {2}}{2}}{\lim _ {x \rightarrow 0 ^ {-}} \frac {x}{x}} = \frac {1}{2},</equation><equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {\cos \sqrt {x} - 1}{x - 0} \xlongequal {\cos \sqrt {x} - 1 \sim - \frac {(\sqrt {x}) ^ {2}}{2}} \lim _ {x \rightarrow 0 ^ {+}} \frac {- \frac {x}{2}}{x} = - \frac {1}{2}.</equation>由于<equation>f_{-}^{\prime}(0)\neq f_{+}^{\prime}(0)</equation>，故<equation>f(x) = \cos \sqrt{|x|}</equation>在<equation>x = 0</equation>处不可导.应选D.

下面分别说明选项A、B、C不正确.

选项A：<equation>f ( x )=\left\{\begin{array}{ll}x\sin x,&x\geqslant 0,\\ -x\sin(-x),&x<0.\end{array} \right.</equation>又因为<equation>- x\sin(-x)=-x\cdot(-\sin x)=x\sin x</equation>，所以<equation>f ( x )=x\sin x,f ( x )</equation>在 x=0处可导.

选项B：<equation>f ( x ) = \left\{ \begin{array}{ll} x \sin \sqrt{x}, & x \geqslant 0, \\ - x \sin \sqrt{-x}, & x < 0. \end{array} \right.</equation><equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {- x \sin \sqrt {- x} - 0}{x - 0} = \lim _ {x \rightarrow 0 ^ {-}} (- \sin \sqrt {- x}) = 0,</equation><equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {x \sin \sqrt {x} - 0}{x - 0} = \lim _ {x \rightarrow 0 ^ {+}} \sin \sqrt {x} = 0.</equation>由于<equation>f_{-}^{\prime}(0) = f_{+}^{\prime}(0)</equation>，故<equation>f(x) = |x|\sin \sqrt{|x|}</equation>在<equation>x = 0</equation>处可导.

选项C：<equation>f ( x )=\left\{\begin{array}{ll}\cos x,&x\geqslant 0,\\ \cos(-x),&x<0.\end{array} \right.</equation>又因为<equation>\cos(-x)=\cos x</equation>，所以<equation>f ( x )=\cos x,f ( x )</equation>在<equation>x=0</equation>处可导.

---

**2016年第4题 | 选择题 | 4分 | 答案: D**

4. 已知函数 f(x) =<equation>\left\{\begin{array}{l l}{x,}&{x \leqslant 0,}\\ {\frac{1}{n},}&{\frac{1}{n+1}<x \leqslant \frac{1}{n},(n=1,2,\cdots),}\end{array} \right.</equation>则（    )

A. x=0是 f(x) 的第一类间断点 B. x=0是 f(x) 的第二类间断点

C. f(x)在 x=0处连续但不可导 D. f(x)在 x=0处可导

答案: D

**解析:**解 由题设知，<equation>f(0)=0</equation>，于是<equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0 ^ {-}} \frac {x}{x} = 1,</equation><equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x)}{x}.</equation>当<equation>\frac{1}{n+1}<x\leqslant \frac{1}{n}</equation>时，<equation>f(x)=\frac{1}{n}</equation>从而<equation>1\leqslant \frac{f(x)}{x}=\frac{\frac{1}{n}}{x}<\frac{n+1}{n}</equation>当<equation>x\to 0^{+}</equation>时，<equation>n\to \infty</equation><equation>\frac{n+1}{n}\to 1</equation>由夹逼准则知，<equation>\lim_{x\to 0^{+}}\frac{f(x)}{x}=1</equation>即<equation>f_{+}^{\prime}(0)=1</equation>于是<equation>f_{+}^{\prime}(0)=f_{-}^{\prime}(0)</equation>从而f(x)在x=0处可导.应选D.

---

**2015年第18题 | 解答题 | 10分**

18. (本题满分10分)

I. 设函数<equation>u ( x ) , v ( x )</equation>可导，利用导数定义证明<equation>[ u ( x ) v ( x ) ]^{\prime}=u^{\prime} ( x ) v ( x )+u ( x ) v^{\prime} ( x )</equation>；

II. 设函数<equation>u_{1} ( x ) , u_{2} ( x ) , \cdots , u_{n} ( x )</equation>可导，<equation>f ( x )=u_{1} ( x ) u_{2} ( x ) \cdots u_{n} ( x )</equation>，写出 f(x)的求导公

**答案:**(18) （I）证明略；<equation>(\mathrm {I I}) [ f (x) ] ^ {\prime} = \sum_ {i = 1} ^ {n} \left[ u _ {i} ^ {\prime} (x) \prod_ {\substack {j \neq i, \\ 1 \leqslant j \leqslant n}} u _ {j} (x) \right].</equation>

**解析:**解（I）（法一）由导数的定义知，<equation>\begin{aligned} [ u (x) v (x) ] ^ {\prime} &= \lim _ {h \rightarrow 0} \frac {u (x + h) v (x + h) - u (x) v (x)}{h} \\ &= \lim _ {h \rightarrow 0} \frac {u (x + h) v (x + h) - u (x) v (x + h) + u (x) v (x + h) - u (x) v (x)}{h} \\ &= \lim _ {h \rightarrow 0} \frac {u (x + h) - u (x)}{h} \cdot v (x + h) + \lim _ {h \rightarrow 0} u (x) \cdot \frac {v (x + h) - v (x)}{h} \\ \underline {{= \frac {u (x) , v (x) \text {均 可 导}}{2}}} u ^ {\prime} (x) v (x) + u (x) v ^ {\prime} (x). \end{aligned}</equation>（法二）由导数的定义知，<equation>\begin{aligned} [ u (x) v (x) ] ^ {\prime} &= \lim _ {h \rightarrow 0} \frac {u (x + h) v (x + h) - u (x) v (x)}{h} \\ &= \lim _ {h \rightarrow 0} \frac {u (x + h) v (x + h) - u (x + h) v (x) + u (x + h) v (x) - u (x) v (x)}{h} \\ &= \lim _ {h \rightarrow 0} u (x + h) \cdot \frac {v (x + h) - v (x)}{h} + \lim _ {h \rightarrow 0} \frac {u (x + h) - u (x)}{h} \cdot v (x) \\ \underline {{= \frac {u (x) , v (x) \text {均 可 导}}{2}}} u (x) v ^ {\prime} (x) + u ^ {\prime} (x) v (x). \end{aligned}</equation>（Ⅱ）由第（Ⅰ）问知，<equation>\begin{array}{l} [ f (x) ] ^ {\prime} = \left\{u _ {1} (x) \left[ u _ {2} (x) \dots u _ {n} (x) \right] \right\} ^ {\prime} \\ = u _ {1} ^ {\prime} (x) u _ {2} (x) \dots u _ {n} (x) + u _ {1} (x) \left[ u _ {2} (x) \dots u _ {n} (x) \right] ^ {\prime} \\ = u _ {1} ^ {\prime} (x) u _ {2} (x) \dots u _ {n} (x) + u _ {1} (x) \left\{u _ {2} (x) \cdot \left[ u _ {3} (x) \dots u _ {n} (x) \right] \right\} ^ {\prime} \\ = u _ {1} ^ {\prime} (x) u _ {2} (x) \dots u _ {n} (x) + u _ {1} (x) \left\{u _ {2} ^ {\prime} (x) u _ {3} (x) \dots u _ {n} (x) + u _ {2} (x) \left[ u _ {3} (x) \dots u _ {n} (x) \right] ^ {\prime} \right\} \\ = u _ {1} ^ {\prime} (x) u _ {2} (x) \dots u _ {n} (x) + u _ {1} (x) u _ {2} ^ {\prime} (x) u _ {3} (x) \dots u _ {n} (x) + u _ {1} (x) u _ {2} (x) \left[ u _ {3} (x) \dots u _ {n} (x) \right] ^ {\prime} \\ = \dots \\ = u _ {1} ^ {\prime} (x) u _ {2} (x) \dots u _ {n} (x) + u _ {1} (x) u _ {2} ^ {\prime} (x) \dots u _ {n} (x) + \dots + u _ {1} (x) u _ {2} (x) \dots u _ {n} ^ {\prime} (x) \\ = \sum_ {i = 1} ^ {n} \left[ u _ {i} ^ {\prime} (x) \prod_ {\substack {j \neq i, \\ 1 \leqslant j \leqslant n}} u _ {j} (x) \right]. \\ \end{array}</equation>

---


#### 微分中值定理

**2025年第19题 | 解答题 | 12分**
19. 设函数 f(x)在区间（a,b）内可导，证明导函数<equation>f^{\prime}(x)</equation>在（a,b）内严格单调增加的充分必要条件是：对（a,b）内任意的<equation>x_{1},x_{2},x_{3}</equation>，当<equation>x_{1}<x_{2}<x_{3}</equation>时，<equation>\frac{f(x_{2})-f(x_{1})}{x_{2}-x_{1}}<\frac{f(x_{3})-f(x_{2})}{x_{3}-x_{2}}.</equation>
**解析: **证 先证明必要性.

对（a,b）内任意的<equation>x_{1}, x_{2}, x_{3}</equation>，当<equation>x_{1} < x_{2} < x_{3}</equation>时，由拉格朗日中值定理可得存在<equation>\xi_{1}\in(x_{1},x_{2})</equation><equation>\xi_{2}\in(x_{2},x_{3})</equation>，使得<equation>f^{\prime}(\xi_{1})=\frac{f(x_{2})-f(x_{1})}{x_{2}-x_{1}},f^{\prime}(\xi_{2})=\frac{f(x_{3})-f(x_{2})}{x_{3}-x_{2}}.</equation>由<equation>f^{\prime}(x)</equation>单调增加以及<equation>\xi_{1} <</equation><equation>\xi_{2}</equation>可得<equation>f^{\prime}(\xi_{1}) < f^{\prime}(\xi_{2})</equation>即<equation>\frac{f(x_{2})-f(x_{1})}{x_{2}-x_{1}} < \frac{f(x_{3})-f(x_{2})}{x_{3}-x_{2}}.</equation>再证明充分性.

任取<equation>x_{0}, x_{1}, x_{2}\in(a,b)</equation>满足<equation>x_{1} < x_{0} < x_{2}</equation>，由已知条件可得<equation>\frac{f(x_{0})-f(x_{1})}{x_{0}-x_{1}} < \frac{f(x_{2})-f(x_{0})}{x_{2}-x_{0}}.</equation>取 s,t满足<equation>x_{1} < s < x_{0} < t < x_{2}</equation>，由已知条件可得<equation>\frac {f (s) - f \left(x _ {1}\right)}{s - x _ {1}} < \frac {f \left(x _ {0}\right) - f (s)}{x _ {0} - s}, \quad \frac {f (t) - f \left(x _ {0}\right)}{t - x _ {0}} < \frac {f \left(x _ {2}\right) - f (t)}{x _ {2} - t}.</equation>在<equation>\frac{f(s)-f(x_{1})}{s-x_{1}}<\frac{f(x_{0})-f(s)}{x_{0}-s}</equation>中令 s<equation>\rightarrow x_{1}^{+}</equation>可得<equation>f ^ {\prime} \left(x _ {1}\right) = f _ {+} ^ {\prime} \left(x _ {1}\right) = \lim _ {s \rightarrow x _ {1} ^ {+}} \frac {f (s) - f \left(x _ {1}\right)}{s - x _ {1}} \leqslant \lim _ {s \rightarrow x _ {1} ^ {+}} \frac {f \left(x _ {0}\right) - f (s)}{x _ {0} - s} = \frac {f \left(x _ {0}\right) - f \left(x _ {1}\right)}{x _ {0} - x _ {1}}.</equation>在<equation>\frac{f(t) - f(x_0)}{t - x_0} < \frac{f(x_2) - f(t)}{x_2 - t}</equation>中令<equation>t\to x_2^{-}</equation>可得<equation>\frac {f \left(x _ {2}\right) - f \left(x _ {0}\right)}{x _ {2} - x _ {0}} = \lim _ {t \rightarrow x _ {2} ^ {-}} \frac {f (t) - f \left(x _ {0}\right)}{t - x _ {0}} \leqslant \lim _ {t \rightarrow x _ {2} ^ {-}} \frac {f \left(x _ {2}\right) - f (t)}{x _ {2} - t} = f _ {-} ^ {\prime} \left(x _ {2}\right) = f ^ {\prime} \left(x _ {2}\right).</equation>由(1)式，(2)式以及<equation>\frac{f(x_0) - f(x_1)}{x_0 - x_1} < \frac{f(x_2) - f(x_0)}{x_2 - x_0}</equation>可得<equation>f^{\prime}(x_{1}) < f^{\prime}(x_{2})</equation>由<equation>x_{1}, x_{2}</equation>的任意性可得<equation>f^{\prime}(x)</equation>在<equation>(a,b)</equation>内严格单调增加.

---

**2020年第19题 | 解答题 | 10分**
19. (本题满分10分)

设函数 f(x)在区间[0,2]上具有连续导数，<equation>f(0)=f(2)=0</equation><equation>M=\max_{x\in[0,2]}\{|f(x)|\}</equation>，证明：

I. 存在<equation>\xi\in(0,2)</equation>，使得<equation>|f^{\prime}(\xi)|\geqslant M</equation>;

II. 若对任意的<equation>x\in(0,2),|f^{\prime}(x)|\leqslant M</equation>，则 M=0.
**答案: **（I）证明略；（Ⅱ）证明略.
**解析: **证（I）若<equation>M=0</equation>，则<equation>f(x)\equiv 0,f^{\prime}(x)\equiv 0</equation>，所证命题成立.

若<equation>M \neq 0</equation>，则<equation>\max_{[0,2]}\left\{|f(x)|\right\}</equation>在区间（0,2）内取得，不妨设<equation>|f(c)| = M,0 < c < 2.</equation>由拉格朗日中值定理可得，存在<equation>\xi_{1}\in (0,c)</equation>，使得<equation>|f(c)| \stackrel{f(0) = 0}{\cong} |f(c) - f(0)| = |f^{\prime}(\xi_{1})c|</equation>, 即<equation>|f^{\prime}(\xi_{1})| = \frac{|f(c)|}{c} = \frac{M}{c}</equation>.

存在<equation>\xi_{2}\in(c,2)</equation>，使得<equation>|f(c)| \stackrel{f(2) = 0}{\cong} |f(2) - f(c)| = |f'(\xi_2)(2 - c)|</equation>，即<equation>|f^{\prime}(\xi_{2})| = \frac{|f(c)|}{2 - c} = \frac{M}{2 - c}</equation>.

- 若<equation>c < 1</equation>，则<equation>\frac{M}{c} > M</equation>，即<equation>|f^{\prime}(\xi_{1})| > M.</equation>取<equation>\xi = \xi_{1}</equation>.

- 若<equation>c = 1</equation>，则<equation>|f^{\prime}(\xi_{1})| = |f^{\prime}(\xi_{2})| = M.</equation>取<equation>\xi = \xi_{1}</equation>或<equation>\xi = \xi_{2}</equation>均可.

- 若<equation>c > 1</equation>，则<equation>\frac{M}{2 - c} > M</equation>，即<equation>|f^{\prime}(\xi_{2})| > M.</equation>取<equation>\xi = \xi_{2}</equation>.

不论哪种情况，都存在<equation>\xi \in (0,2)</equation>，使得<equation>|f^{\prime}(\xi)| \geqslant M.</equation>（Ⅱ）若<equation>M=0</equation>，则<equation>f(x)\equiv 0</equation>，结论自然成立.

下面假设<equation>M > 0.</equation>c如第（I）问中所设.分情况讨论.

若<equation>c\neq 1</equation>，则由第（I）问可知，区间（0,2）中至少存在一个点<equation>(\xi_{1}</equation>或<equation>\xi_{2})</equation>，满足<equation>|f^{\prime}(\xi_{1})| > M</equation>或<equation>|f^{\prime}(\xi_{2})| > M.</equation>矛盾.

下面用两种方法说明<equation>c = 1</equation>的情况.

若<equation>c = 1</equation>，则<equation>|f(1)| = M</equation>，<equation>x = 1</equation>为<equation>f(x)</equation>的极值点.

（法一）不妨设<equation>f(1)=M.</equation>由极值的必要条件可知，<equation>f^{\prime}(1)=0.</equation>考虑<equation>g ( x ) = f ( x ) - M x</equation>，则<equation>g^{\prime} ( x )=f^{\prime} ( x )-M.</equation>由<equation>|f^{\prime}(x)|\leqslant M</equation>可得<equation>g^{\prime}(x)\leqslant 0</equation>从而<equation>g ( x )</equation>单调减少.又因为<equation>g ( 0 )=g ( 1 )=0</equation>所以当<equation>x\in(0,1)</equation>时，<equation>g ( x )\equiv0</equation>即<equation>f ( x )=M x.</equation>于是，<equation>f^{\prime}(x)=M.</equation>结合<equation>f^{\prime}(1)=0</equation>与<equation>f^{\prime}(x)</equation>连续可得，<equation>M=\lim f^{\prime}(x)=f^{\prime}(1)=0.</equation><equation>f(1) = -M</equation>的情形类似，考虑<equation>g(x) = f(x) + Mx</equation>即可.

（法二）由<equation>f^{\prime}(x)</equation>连续以及牛顿-莱布尼茨公式可得，<equation>M = | f (1) | \xlongequal {f (0) = 0} | f (1) - f (0) | = \left| \int_ {0} ^ {1} f ^ {\prime} (x) \mathrm {d} x \right| \leqslant \int_ {0} ^ {1} | f ^ {\prime} (x) | \mathrm {d} x \leqslant \int_ {0} ^ {1} M \mathrm {d} x = M.</equation>于是，<equation>\int_{0}^{1}|f^{\prime}(x)|\mathrm{d}x=M</equation>，从而<equation>\int_{0}^{1}(|f^{\prime}(x)|-M)\mathrm{d}x=0.</equation>由于<equation>|f^{\prime}(x)|\leqslant M</equation>，故<equation>|f^{\prime}(x)|-M\leqslant 0.</equation>由定积分的性质（见注）可知，当<equation>x\in(0,1)</equation>时，<equation>|f^{\prime}(x)|\equiv M.</equation>同理可得当<equation>x\in (1,2)</equation>时，<equation>|f^{\prime}(x)|\equiv M.</equation>

---

**2013年第18题 | 解答题 | 10分**
18. (本题满分10分)

设奇函数 f(x)在<equation>[-1,1]</equation>上具有二阶导数，且 f(1)=1.证明：

I. 存在<equation>\xi \in(0,1)</equation>，使得<equation>f^{\prime}(\xi)=1</equation>；

II. 存在<equation>\eta \in(-1,1)</equation>，使得<equation>f^{\prime\prime}(\eta)+f^{\prime}(\eta)=1.</equation>
**答案: **(18) （I）证明略；（Ⅱ）证明略.
**解析: **证（I）由 f(x)为奇函数得 f(0) = 0.由于 f(1) = 1，且 f(x)在[-1,1]上可导，故由拉格朗日中值定理得，存在<equation>\xi\in(0,1)</equation>，使得<equation>f(1)-f(0)=f^{\prime}(\xi)</equation>，即<equation>f^{\prime}(\xi)=1.</equation>（Ⅱ）（法一）构造辅助函数<equation>g ( x ) = f^{\prime} ( x ) + f ( x ) - x. g ( x )</equation>在[-1，1]上可导.

若能在<equation>[-1,1]</equation>上找到两个点<equation>x_{1}, x_{2}</equation>，使得<equation>g(x_{1}) = g(x_{2})</equation>，则由罗尔定理可得，存在<equation>\eta \in(-1,1), g^{\prime}(\eta)=0</equation>，即<equation>f^{\prime \prime}(\eta)+f^{\prime}(\eta)=1.</equation>由于 f(x）是<equation>[-1,1]</equation>上的奇函数，故<equation>f(x)=-f(-x).</equation>该等式两端同时关于 x求导得<equation>f^{\prime}(x)=</equation><equation>f^{\prime}(-x).</equation>于是<equation>f^{\prime}(x)</equation>是<equation>[-1,1]</equation>上的偶函数.从而，

g(1) = f'(1) + f(1) - 1, g(-1) = f'(-1) + f(-1) - (-1) = f'(1) - f(1) + 1.由于 f(1)-1=0，故 g(1) = g(-1).

由罗尔定理可知，存在<equation>\eta \in (-1,1)</equation>，<equation>g^{\prime}(\eta) = 0</equation>，即<equation>f^{\prime \prime}(\eta) + f^{\prime}(\eta) = 1.</equation>（法二）构造辅助函数<equation>G ( x )=\mathrm{e}^{x} \left[ f^{\prime} ( x )-1 \right]. G ( x )</equation>在<equation>[-1,1]</equation>上可导.<equation>G ^ {\prime} (x) = \mathrm {e} ^ {x} \left[ f ^ {\prime} (x) - 1 \right] + \mathrm {e} ^ {x} f ^ {\prime \prime} (x) = \mathrm {e} ^ {x} \left[ f ^ {\prime \prime} (x) + f ^ {\prime} (x) - 1 \right].</equation>由于 f(x）是<equation>[-1,1]</equation>上的奇函数，同法一中的论证可知<equation>f^{\prime}(x)</equation>是<equation>[-1,1]</equation>上的偶函数.<equation>\xi</equation>为第（I）问中所得，满足<equation>f^{\prime}(\xi)=1</equation>，从而<equation>f^{\prime}(-\xi)=f^{\prime}(\xi)=1.</equation>因此<equation>G(\xi)=G(-\xi)=0.</equation>由罗尔定理，存在<equation>\eta\in(-1,1)</equation>，使得<equation>G^{\prime}(\eta)=0</equation>.又因为<equation>\mathrm{e}^{\eta}>0</equation>，所以<equation>f^{\prime\prime}(\eta)+f^{\prime}(\eta)-1=0</equation>，即<equation>f^{\prime\prime}(\eta)+f^{\prime}(\eta)=1.</equation>

---

**2009年第18题 | 解答题 | 10分**
18. (本题满分11分)

I. 证明拉格朗日中值定理：若函数 f(x)在<equation>[a,b]</equation>上连续，在（a,b）内可导，则存在<equation>\xi\in(a,b)</equation>，使得<equation>f(b)- f(a)=f^{\prime}(\xi)(b-a).</equation>II. 证明：若函数 f(x)在 x=0处连续，在（0，<equation>\delta )(\delta>0)</equation>内可导，且<equation>\lim_{x\rightarrow 0^{+}}f^{\prime}(x)=A</equation>，则<equation>f_{+}^{\prime}(0)</equation>存在，且<equation>f_{+}^{\prime}(0)=A.</equation>
**解析: **分析 本题主要考查拉格朗日中值定理的证明和应用.它的几何解释为，在一条除端点外处处有不平行于 y轴的切线的曲线<equation>\widehat{A B}</equation>上，至少有一点处的切线平行于弦 AB，如右图.

证（I）构造函数<equation>F ( x )=f ( x )-\left[ f ( a )+\frac{f ( b )-f ( a )}{b-a} ( x-a ) \right]</equation>，则由题设知，<equation>F ( x )</equation>在<equation>[ a,b]</equation>上连续，在（a,b）内可导，且有<equation>F (a) = 0, \quad F (b) = 0.</equation>于是由罗尔定理知，存在<equation>\xi \in (a,b)</equation>，使得<equation>F^{\prime}(\xi) = 0</equation>，即有<equation>f ^ {\prime} (\xi) - \frac {f (b) - f (a)}{b - a} = 0,</equation>从而<equation>f(b) - f(a) = f^{\prime}(\xi)(b - a)</equation>. 结论得证.

（Ⅱ）（法一）当<equation>x\in(0,\delta)</equation>时，由题设知<equation>f(x)</equation>在<equation>[0,x]</equation>上连续，在（0,x）内可导，故由拉格朗日中值定理知，存在<equation>\xi_{x}\in(0,x)</equation>，使得<equation>f (x) - f (0) = f ^ {\prime} \left(\xi_ {x}\right) x.</equation>由于<equation>\xi_{x}\in (0,x)</equation>，故当<equation>x\to 0^{+}</equation>时<equation>\xi_{x}\rightarrow 0^{+}</equation>，从而<equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x} = \lim _ {x \rightarrow 0 ^ {+}} \frac {f ^ {\prime} \left(\xi_ {x}\right) x}{x} = \lim _ {x \rightarrow 0 ^ {+}} f ^ {\prime} \left(\xi_ {x}\right) = \lim _ {x \rightarrow 0 ^ {+}} f ^ {\prime} (x) = A.</equation>由右导数定义知，<equation>f_{+}^{\prime}(0)</equation>存在且<equation>f_{+}^{\prime}(0) = A</equation>，结论得证.

（法二）由<equation>f(x)</equation>在<equation>x = 0</equation>处连续知，<equation>\lim_{x\to 0^{+}}[f(x) - f(0)] = 0.</equation>又<equation>f(x)</equation>在<equation>(0,\delta)</equation>内可导，故<equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {f ^ {\prime} (x)}{1} = A.</equation>由右导数定义知，<equation>f_{+}^{\prime}(0)</equation>存在且<equation>f_{+}^{\prime}(0) = A.</equation>

---


#### 泰勒公式

**2024年第19题 | 解答题 | 12分**

9. (本题满分12分)

设函数 f(x)具有2阶导数，且<equation>f^{\prime}(0)=f^{\prime}(1),\left| f^{\prime\prime}(x)\right| \leqslant 1</equation>.证明：

I. 当 x<equation>\in(0,1)</equation>时，<equation>|f(x)-f(0)(1-x)-f(1)x|\leqslant \frac{x(1-x)}{2}</equation>II.<equation>\left|\int_{0}^{1} f(x)\mathrm{d}x-\frac{f(0)+f(1)}{2}\right|\leqslant \frac{1}{12}.</equation>

**解析:**（I）（法一）分别写出 f(x)在 x=0与 x=1处的一阶泰勒公式.<equation>f (x) = f (0) + f ^ {\prime} (0) x + \frac {f ^ {\prime \prime} \left(\xi_ {1}\right) x ^ {2}}{2},</equation><equation>f (x) = f (1) + f ^ {\prime} (1) (x - 1) + \frac {f ^ {\prime \prime} \left(\xi_ {2}\right) \left(x - 1\right) ^ {2}}{2},</equation>其中<equation>\xi_{1}</equation>介于0与<equation>x</equation>之间，<equation>\xi_{2}</equation>介于1与<equation>x</equation>之间.

(2) 式<equation>\times x-（1）</equation>式<equation>\times (x-1)</equation>，并结合<equation>f^{\prime}(0)=f^{\prime}(1)</equation>可得<equation>f (x) = f (0) (1 - x) + f (1) x + \frac {x (x - 1)}{2} \left[ f ^ {\prime \prime} \left(\xi_ {2}\right) (x - 1) - f ^ {\prime \prime} \left(\xi_ {1}\right) x \right].</equation>由（3）式可得，当<equation>x\in(0,1)</equation>时，<equation>\left| f (x) - f (0) (1 - x) - f (1) x \right| = \frac {x (1 - x)}{2} \left| f ^ {\prime \prime} \left(\xi_ {2}\right) (x - 1) - f ^ {\prime \prime} \left(\xi_ {1}\right) x \right|.</equation>由于<equation>|f^{\prime \prime}(\xi_{2})(x - 1) - f^{\prime \prime}(\xi_{1})x| \leqslant |f^{\prime \prime}(\xi_{2})|(1 - x) + |f^{\prime \prime}(\xi_{1})|x,</equation>故结合<equation>|f^{\prime \prime}(x)| \leqslant 1</equation>以及（4）式可得<equation>| f (x) - f (0) (1 - x) - f (1) x | \leqslant \frac {x (1 - x)}{2} \cdot [ (1 - x) + x ] = \frac {x (1 - x)}{2}.</equation>（法二）所证命题等价于当<equation>x\in (0,1)</equation>时，<equation>- \frac {x (1 - x)}{2} \leqslant f (x) - f (0) (1 - x) - f (1) x \leqslant \frac {x (1 - x)}{2}.</equation>令<equation>F ( x )=f ( x )-f ( 0 ) ( 1-x )-f ( 1 ) x-\frac{x(1-x)}{2}</equation>，则<equation>F ( 0 )=F ( 1 )=0</equation>，且<equation>F^{\prime \prime}(x)=f^{\prime \prime}(x)</equation>+1. 由于<equation>|f^{\prime \prime}(x)| \leqslant 1</equation>，故<equation>F^{\prime \prime}(x) \geqslant 0.</equation>下面证明当<equation>x\in (0,1)</equation>时，<equation>F(x)\leqslant 0.</equation>若存在<equation>c\in (0,1)</equation>，使得<equation>F(c) > 0</equation>，则分别对<equation>[0,c],[c,1]</equation>上的<equation>F(x)</equation>使用拉格朗日中值定理可得，存在<equation>\xi_{1}\in (0,c),\xi_{2}\in (c,1)</equation>，使得<equation>F ^ {\prime} \left(\xi_ {1}\right) = \frac {F (c) - F (0)}{c - 0} > 0, \quad F ^ {\prime} \left(\xi_ {2}\right) = \frac {F (1) - F (c)}{1 - c} < 0.</equation>再对<equation>[\xi_{1},\xi_{2} ]</equation>上的<equation>F^{\prime}(x)</equation>使用拉格朗日中值定理可得，存在<equation>\xi\in(\xi_{1},\xi_{2})</equation>，使得<equation>F ^ {\prime \prime} (\xi) = \frac {F ^ {\prime} \left(\xi_ {2}\right) - F ^ {\prime} \left(\xi_ {1}\right)}{\xi_ {2} - \xi_ {1}} < 0.</equation>这与<equation>F^{\prime \prime}(x)\geqslant0</equation>矛盾.

因此，当<equation>x\in (0,1)</equation>时，<equation>F(x)\leqslant 0</equation>，即<equation>f(x) - f(0)(1 - x) - f(1)x\leqslant \frac{x(1 - x)}{2}.</equation>令<equation>G ( x ) = f ( x ) - f ( 0 ) ( 1 - x ) - f ( 1 ) x + \frac { x ( 1 - x ) } { 2 }</equation>，同理可得<equation>G^{\prime \prime}(x)\leqslant 0</equation>，且进一步可得当<equation>x\in</equation>（0,1）时，<equation>G ( x ) \geqslant 0</equation>，即<equation>f ( x ) - f ( 0 ) ( 1 - x ) - f ( 1 ) x \geqslant - \frac { x ( 1 - x ) } { 2 } .</equation>综上所述，所证命题成立.

（Ⅱ）由第（Ⅰ）问可得<equation>\left| f (x) - f (0) (1 - x) - f (1) x \right| \leqslant \frac {x (1 - x)}{2}.</equation>对（5）式两端从0到1积分可得，<equation>\begin{aligned} \int_ {0} ^ {1} | f (x) - f (0) (1 - x) - f (1) x | \mathrm {d} x \leqslant \int_ {0} ^ {1} \frac {x (1 - x)}{2} \mathrm {d} x &= \frac {1}{2} \int_ {0} ^ {1} \left(x - x ^ {2}\right) \mathrm {d} x \\ &= \frac {1}{2} \left(\frac {x ^ {2}}{2} - \frac {x ^ {3}}{3}\right) \Big | _ {0} ^ {1} = \frac {1}{1 2}. \end{aligned}</equation>进一步由定积分的性质可得<equation>\begin{array}{l} \left| \int_ {0} ^ {1} f (x) \mathrm {d} x - f (0) \int_ {0} ^ {1} (1 - x) \mathrm {d} x - f (1) \int_ {0} ^ {1} x \mathrm {d} x \right| = \left| \int_ {0} ^ {1} f (x) \mathrm {d} x - \frac {f (0) + f (1)}{2} \right| \\ \leqslant \int_ {0} ^ {1} | f (x) - f (0) (1 - x) - f (1) x | \mathrm {d} x \leqslant \frac {1}{1 2}. \\ \end{array}</equation>

---

**2023年第20题 | 解答题 | 12分**

20. (本题满分12分)

设函数 f(x)在<equation>[-a,a]</equation>上具有二阶连续导数，证明：

I. 若 f(0)=0，则存在<equation>\xi\in(-a,a)</equation>，使得<equation>f^{\prime\prime}(\xi)=\frac{1}{a^{2}}[f(a)+f(-a)]</equation>；

II. 若 f(x)在<equation>(-a,a)</equation>内取得极值，则存在<equation>\eta\in(-a,a)</equation>使得<equation>|f^{\prime\prime}(\eta)|\geqslant\frac{1}{2a^{2}}|f(a)-f(-a)|.</equation>

**答案:**# （I）证明略；

（Ⅱ）证明略.

**解析:**证 （ I ）由<equation>f ( x )</equation>的泰勒公式可得<equation>f (a) = f (0) + f ^ {\prime} (0) a + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {1}\right) a ^ {2} \xlongequal {f (0) = 0} f ^ {\prime} (0) a + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {1}\right) a ^ {2},</equation><equation>f (- a) = f (0) + f ^ {\prime} (0) \cdot (- a) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {2}\right) a ^ {2} \stackrel {f (0) = 0} {=} f ^ {\prime} (0) \cdot (- a) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {2}\right) a ^ {2},</equation>其中<equation>\xi_{1}\in (0,a),\xi_{2}\in (-a,0)</equation>.两式相加可得<equation>f (a) + f (- a) = \frac {a ^ {2}}{2} \left[ f ^ {\prime \prime} \left(\xi_ {1}\right) + f ^ {\prime \prime} \left(\xi_ {2}\right) \right].</equation>记<equation>\max \left\{f^{\prime \prime}\left(\xi_{1}\right), f^{\prime \prime}\left(\xi_{2}\right)\right\} = M,</equation><equation>\min \left\{f^{\prime \prime}\left(\xi_{1}\right), f^{\prime \prime}\left(\xi_{2}\right)\right\} = m,</equation>则由（1）式可得<equation>m \leqslant \frac {f (a) + f (- a)}{a ^ {2}} = \frac {1}{2} \left[ f ^ {\prime \prime} \left(\xi_ {1}\right) + f ^ {\prime \prime} \left(\xi_ {2}\right) \right] \leqslant M.</equation>由于<equation>f ( x )</equation>在<equation>[ - a,a]</equation>上有二阶连续导数，故由连续函数的介值定理可知，存在<equation>\xi \in[ \xi_{2},\xi_{1} ]\subset(-a,a)</equation>，使得<equation>f^{\prime \prime}(\xi)=\frac{1}{a^{2}}[f(a)+f(-a)]</equation>.

（Ⅱ）设<equation>f(x)</equation>在<equation>(-a,a)</equation>内的极值点为<equation>x_{0}</equation>，则<equation>f^{\prime}(x_{0})=0.</equation>由<equation>f(x)</equation>的泰勒公式可得<equation>\begin{aligned} f (a) &= f \left(x _ {0}\right) + f ^ {\prime} \left(x _ {0}\right) \left(a - x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {1}\right) \left(a - x _ {0}\right) ^ {2} \\ \underline {{=}} f ^ {\prime \prime} \left(x _ {0}\right) &= 0 f \left(x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {1}\right) \left(a - x _ {0}\right) ^ {2}, \\ f (- a) &= f \left(x _ {0}\right) + f ^ {\prime} \left(x _ {0}\right) \left(- a - x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {2}\right) \left(- a - x _ {0}\right) ^ {2} \\ \underline {{=}} f ^ {\prime \prime} \left(x _ {0}\right) &= 0 f \left(x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {2}\right) \left(a + x _ {0}\right) ^ {2}, \end{aligned}</equation>其中<equation>\eta_{1}\in (x_{0},a),\eta_{2}\in (-a,x_{0})</equation>. 两式相减可得<equation>f (a) - f (- a) = \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {1}\right) \left(a - x _ {0}\right) ^ {2} - \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {2}\right) \left(a + x _ {0}\right) ^ {2}.</equation>记<equation>\max \{|f''(\eta_1)|, |f''(\eta_2)|\} = M</equation>，则由（2）式可得<equation>\left| f (a) - f (- a) \right| \leqslant \frac {M}{2} \left[ \left(a - x _ {0}\right) ^ {2} + \left(a + x _ {0}\right) ^ {2} \right] = \frac {M}{2} \left(2 a ^ {2} + 2 x _ {0} ^ {2}\right) \leqslant \frac {M}{2} \cdot 4 a ^ {2} = 2 a ^ {2} M.</equation>因此，<equation>M\geqslant \frac{1}{2a^{2}}|f(a) - f(-a)|.</equation>取<equation>\eta \in \{\eta_1, \eta_2\}</equation>使得<equation>|f''(\eta)| = M</equation>，则<equation>\eta \in (-a, a)</equation>满足<equation>|f''(\eta)| \geqslant \frac{1}{2a^2}|f(a) - f(-a)|</equation>.

---

**2021年第3题 | 选择题 | 5分 | 答案: A**

3. 设函数<equation>f(x)=\frac{\sin x}{1+x^{2}}</equation>在 x=0处的3次泰勒多项式为<equation>ax+bx^{2}+cx^{3}</equation>，则（    )

A. a=1,b=0,c=-<equation>\frac{7}{6}</equation>B. a=1,b=0,c=<equation>\frac{7}{6}</equation>C. a=-1,b=-1,c=-<equation>\frac{7}{6}</equation>D. a=-1,b=-1,c=<equation>\frac{7}{6}</equation>

答案: A

**解析:**解 由于<equation>\sin x=x-\frac{x^{3}}{6}+o\left(x^{3}\right),\frac{1}{1+x^{2}}=1-x^{2}+o\left(x^{2}\right)</equation>，故<equation>\frac{\sin x}{1+x^{2}}=\left[x-\frac{x^{3}}{6}+o\left(x^{3}\right)\right]\left[1-x^{2}+o\left(x^{2}\right)\right]=x-x^{3}-\frac{x^{3}}{6}+o\left(x^{3}\right)</equation><equation>= x-\frac{7x^{3}}{6}+o\left(x^{3}\right).</equation>因此，<equation>\frac{\sin x}{1+x^{2}}</equation>在 x=0处的3次泰勒多项式为<equation>x-\frac{7 x^{3}}{6}.</equation>a=1,b=0,c=-<equation>\frac{7}{6}.</equation>应选A.

---


#### 导数与微分的计算

**2021年第12题 | 填空题 | 5分**

12. 设函数<equation>y=y(x)</equation>由参数方程<equation>\left\{ \begin{array}{l} x = 2 \mathrm {e} ^ {t} + t + 1, \\ y = 4 (t - 1) \mathrm {e} ^ {t} + t ^ {2} \end{array} \right.</equation>确定，则<equation>\left.\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\right|_{t=0}=</equation>___

**答案:**# 2 3.

**解析:**解 根据由参数方程确定的函数的导数计算公式，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {4 \mathrm {e} ^ {t} + 4 (t - 1) \mathrm {e} ^ {t} + 2 t}{2 \mathrm {e} ^ {t} + 1} = \frac {4 t \mathrm {e} ^ {t} + 2 t}{2 \mathrm {e} ^ {t} + 1} = 2 t.</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\mathrm {d} \left(\frac {\mathrm {d} y}{\mathrm {d} x}\right)}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {2}{2 \mathrm {e} ^ {t} + 1}.</equation>代入<equation>t = 0</equation>，可得<equation>\frac{\mathrm{d}^2y}{\mathrm{d}x^2}\bigg|_{t = 0} = \frac{2}{3}</equation>.

---

**2020年第10题 | 填空题 | 4分**

10. 设<equation>\left\{ \begin{array}{l l} x = \sqrt {t ^ {2} + 1}, \\ y = \ln \left(t + \sqrt {t ^ {2} + 1}\right), \end{array} \right. \quad \text {则} \left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {t = 1} = \underline {{}}.</equation>

**答案:**<equation>- \sqrt {2}.</equation>

**解析:**解 根据由参数方程确定的函数的求导公式，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {1 + \frac {t}{\sqrt {t ^ {2} + 1}}}{t + \sqrt {t ^ {2} + 1}} / \frac {t}{\sqrt {t ^ {2} + 1}} = \frac {1}{\sqrt {t ^ {2} + 1}} / \frac {t}{\sqrt {t ^ {2} + 1}} = \frac {1}{t}.</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\mathrm {d} \left(\frac {\mathrm {d} y}{\mathrm {d} x}\right)}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = - \frac {1}{t ^ {2}} / \frac {t}{\sqrt {t ^ {2} + 1}} = - \frac {\sqrt {t ^ {2} + 1}}{t ^ {3}}.</equation>代入<equation>t = 1</equation>，可得<equation>\frac{\mathrm{d}^2y}{\mathrm{d}x^2}\bigg|_{t = 1} = -\sqrt{2}</equation>.

---

**2017年第9题 | 填空题 | 4分**

9. 已知函数<equation>f ( x )=\frac{1}{1+x^{2}}</equation>，则<equation>f^{(3)}(0)=</equation>___

**解析:**解（法一）由泰勒公式<equation>\frac{1}{1+x}=1-x+x^{2}+o\left(x^{2}\right)\left(x\rightarrow 0\right)</equation>知，<equation>f (x) = \frac {1}{1 + x ^ {2}} = 1 - x ^ {2} + x ^ {4} + o \left(x ^ {4}\right) (x \rightarrow 0).</equation>再由泰勒公式的唯一性知，<equation>\frac{f^{(3)}(0)}{3!}=f(x)</equation>在0处的泰勒公式中<equation>x^{3}</equation>的系数=0，从而<equation>f^{(3)}(0)=0.</equation>（法二）<equation>f ( x )=\frac{1}{1+x^{2}}</equation>为偶函数，由偶函数的导函数为奇函数，而奇函数的导函数为偶函数知，<equation>f^{\prime}(x)</equation>为奇函数，<equation>f^{\prime\prime}(x)</equation>为偶函数，<equation>f^{(3)}(x)</equation>为奇函数，从而<equation>f^{(3)}(0)=0.</equation>（法三）<equation>f ^ {\prime} (x) = \left[ \left(1 + x ^ {2}\right) ^ {- 1} \right] ^ {\prime} = - 2 x \left(1 + x ^ {2}\right) ^ {- 2},</equation><equation>f ^ {\prime \prime} (x) = - 2 \left(1 + x ^ {2}\right) ^ {- 2} + 8 x ^ {2} \left(1 + x ^ {2}\right) ^ {- 3},</equation>注意这里不需要展开，因为只要求<equation>f^{(3)}(0).</equation><equation>f ^ {(3)} (x) = 8 x \left(1 + x ^ {2}\right) ^ {- 3} + 1 6 x \left(1 + x ^ {2}\right) ^ {- 3} + 8 x ^ {2} \left[ \left(1 + x ^ {2}\right) ^ {- 3} \right] ^ {\prime},</equation>从而<equation>f^{(3)}(0) = 0.</equation>

---

**2016年第12题 | 填空题 | 4分**

12. 设函数<equation>f(x)=\arctan x-\frac{x}{1+a x^{2}}</equation>，且<equation>f^{\prime\prime\prime}(0)=1</equation>，则 a=___

**答案:**# 1 2.

**解析:**解 应用泰勒公式，当<equation>x\to 0</equation>时，<equation>\arctan x = x - \frac{x^3}{3} + o(x^3),\frac{1}{1 + x} = 1 - x + o(x)</equation>，从而<equation>\frac {x}{1 + a x ^ {2}} = x \left[ 1 - a x ^ {2} + o \left(x ^ {2}\right) \right] = x - a x ^ {3} + o \left(x ^ {3}\right).</equation>于是，<equation>f (x) = \arctan x - \frac {x}{1 + a x ^ {2}} = \left(a - \frac {1}{3}\right) x ^ {3} + o \left(x ^ {3}\right) \quad (x \rightarrow 0).</equation>由泰勒公式的唯一性知，<equation>\frac {f ^ {\prime \prime \prime} (0)}{3 !} = a - \frac {1}{3}.</equation>又<equation>f^{\prime \prime \prime}(0) = 1</equation>，故<equation>a = \frac{1}{2}.</equation>

---

**2013年第9题 | 填空题 | 4分**

9. 设函数 y=f(x)由方程 y-x=<equation>\mathrm{e}^{x(1-y)}</equation>确定，则<equation>\lim_{n\to\infty}n\left[ f\left(\frac{1}{n}\right)-1\right]=\underline{___}</equation>

**解析:**解 将 x=0 代入原方程中得到<equation>f(0)=\mathrm{e}^{0}=1</equation>. 对方程 y-x=<equation>\mathrm{e}^{x(1-y)}</equation>两端关于 x求导，得到<equation>y^{\prime}-1=\mathrm{e}^{x(1-y)}(1-y-xy^{\prime}).</equation>将 x=0,y=1 代入上式得到<equation>y^{\prime}(0)=1</equation>，即<equation>f^{\prime}(0)=1</equation>，从而<equation>\lim _ {n \rightarrow \infty} n \left[ f \left(\frac {1}{n}\right) - 1 \right] = \lim _ {n \rightarrow \infty} \frac {f \left(\frac {1}{n}\right) - f (0)}{\frac {1}{n} - 0} = f ^ {\prime} (0) = 1.</equation>

---

**2013年第11题 | 填空题 | 4分**

11. 设<equation>\left\{ \begin{array}{l} x = \sin t, \\ y = t \sin t + \cos t \end{array} \right.</equation>（t为参数），则<equation>\left.\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}\right|_{t=\frac{\pi}{4}}=</equation>___

**解析:**<equation>\begin{array}{l} \left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {t = \frac {\pi}{4}} = \frac {1}{\cos \frac {\pi}{4}} = \sqrt {2}. \\ \end{array}</equation>

---

**2012年第2题 | 选择题 | 4分 | 答案: A**

2. 设函数<equation>f(x)=\left(\mathrm{e}^{x}-1\right)\left(\mathrm{e}^{2x}-2\right)\cdots\left(\mathrm{e}^{nx}-n\right)</equation>，其中 n为正整数，则<equation>f^{\prime}(0)=</equation>(    )

A.<equation>(-1)^{n-1}(n-1)!</equation>B.<equation>(-1)^{n}(n-1)!</equation>C.<equation>(-1)^{n-1}n!</equation>D.<equation>(-1)^{n}n!</equation>

答案: A

**解析:**解（法一）利用求导的乘法法则来计算<equation>f^{\prime}(0)</equation>.

令<equation>g(x) = \left(\mathrm{e}^{2x} - 2\right)\dots \left(\mathrm{e}^{nx} - n\right)</equation>，则<equation>f(x) = \left(\mathrm{e}^{x} - 1\right)g(x)</equation>. 由求导的乘法法则可得，<equation>f ^ {\prime} (x) = \mathrm {e} ^ {x} g (x) + \left(\mathrm {e} ^ {x} - 1\right) g ^ {\prime} (x).</equation>由于<equation>\mathrm{e}^{0}-1=0</equation>，故<equation>f ^ {\prime} (0) = \mathrm {e} ^ {0} g (0) = (- 1) (- 2) \dots [ - (n - 1) ] = (- 1) ^ {n - 1} (n - 1)!</equation>因此，应选A.

（法二）从导数的定义出发来计算<equation>f^{\prime}(0)</equation>.

由于<equation>f(0)=0</equation>，故<equation>\begin{aligned} f ^ {\prime} (0) &= \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0} \frac {f (x)}{x} = \lim _ {x \rightarrow 0} \frac {\left(\mathrm {e} ^ {x} - 1\right)\left(\mathrm {e} ^ {2 x} - 2\right) \dots \left(\mathrm {e} ^ {n x} - n\right)}{x} \\ \underline {{\mathrm {e} ^ {x} - 1 \sim x}} \lim _ {x \rightarrow 0} \left[ \left(\mathrm {e} ^ {2 x} - 2\right) \dots \left(\mathrm {e} ^ {n x} - n\right)\right] \cdot 1 &= (- 1) (- 2) \dots [ - (n - 1) ] \cdot 1 \\ &= (- 1) ^ {n - 1} (n - 1)!. \end{aligned}</equation>因此，应选A.

（法三）排除法.

我们可以尝试代入 n值，排除不符合题意的选项.由于当 n=2时，四个选项的取值均不同，故可选择 n=2.

当<equation>n = 2</equation>时，<equation>f(x) = \left(\mathrm{e}^{x} - 1\right)\left(\mathrm{e}^{2x} - 2\right), f^{\prime}(0) = -1</equation>，故可排除选项B、C、D.

因此，应选A.

---

**2010年第9题 | 填空题 | 4分**

<equation>9. \mathrm {设} \left\{ \begin{array}{l l} x = \mathrm {e} ^ {- t}, \\ y = \int_ {0} ^ {t} \ln \left(1 + u ^ {2}\right) \mathrm {d} u, \end{array} \right. \mathrm {则} \left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {t = 0} = \underline {{}}</equation>

**解析:**<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\frac {\mathrm {d} y}{\mathrm {d} t}}{\frac {\mathrm {d} x}{\mathrm {d} t}} = \frac {\ln \left(1 + t ^ {2}\right)}{- \mathrm {e} ^ {- t}} = - \mathrm {e} ^ {t} \ln \left(1 + t ^ {2}\right),</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\frac {\mathrm {d} \left(\frac {\mathrm {d} y}{\mathrm {d} x}\right)}{\mathrm {d} t}}{\frac {\mathrm {d} x}{\mathrm {d} t}} = - \frac {\frac {2 t}{1 + t ^ {2}} \cdot \mathrm {e} ^ {t} + \ln \left(1 + t ^ {2}\right) \cdot \mathrm {e} ^ {t}}{- \mathrm {e} ^ {- t}} = \mathrm {e} ^ {2 t} \left[ \frac {2 t}{1 + t ^ {2}} + \ln \left(1 + t ^ {2}\right) \right].</equation>因此，<equation>\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}\bigg|_{t=0}=0.</equation>

---


#### 函数的单调性、极值与最值

**2019年第2题 | 选择题 | 4分 | 答案: B**

2. 设函数 f(x) =<equation>\left\{\begin{array}{l l}{x|x|,}&{x\leqslant0,}\\ {x\ln x,}&{x>0,}\end{array} \right.</equation>则 x=0是 f(x)的（    ）

A. 可导点，极值点 B. 不可导点，极值点 C. 可导点，非极值点 D. 不可导点，非极值点

答案: B

**解析:**解 由于 x≤0时，<equation>|x|=-x</equation>，故<equation>f(x)=\left\{\begin{array}{ll}-x^{2},&x\leqslant 0,\\ x\ln x,&x>0.\end{array} \right.</equation>由 f(x）的定义可知，<equation>f(0)=0.</equation>分别计算 f(x)在 x=0处的左、右导数.<equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {- x ^ {2} - 0}{x - 0} = \lim _ {x \rightarrow 0 ^ {-}} (- x) = 0,</equation><equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {x \ln x - 0}{x - 0} = \lim _ {x \rightarrow 0 ^ {+}} \ln x = - \infty .</equation>于是，<equation>f ( x )</equation>在<equation>x=0</equation>处的右导数不存在，从而<equation>x=0</equation>是<equation>f ( x )</equation>的不可导点.

由于当<equation>x\leqslant 0</equation>时，<equation>f(x) = -x^{2}</equation>，故在0的任意左侧去心邻域内，<equation>f(x) < 0</equation>.又因为当<equation>0 < x < 1</equation>时，<equation>\ln x < 0</equation>，所以在（0,1）内，<equation>f(x) < 0</equation>.于是，存在<equation>x = 0</equation>的一个去心邻域<equation>(-1,0)\cup (0,1)</equation>，使得在该邻域内<equation>f(x) < f(0) = 0</equation>.根据极值点的定义，<equation>x = 0</equation>是<equation>f(x)</equation>的极大值点.

因此，应选B.

---

**2017年第2题 | 选择题 | 4分 | 答案: C**

2. 设函数 f(x)可导，且 f(x)f'(x)>0，则（    ）

A. f(1)>f(-1) B. f(1)<f(-1) C.<equation>|f(1)|>|f(-1)|</equation>D.<equation>|f(1)|<|f(-1)|</equation>

答案: C

**解析:**解（法一）令<equation>F ( x )=f^{2} ( x ).</equation>由题设知，<equation>F^{\prime}(x)=2 f(x) f^{\prime}(x)>0</equation>，故<equation>f^{2}(x)</equation>单调增加，于是<equation>f^{2}(1)>f^{2}(-1)</equation>即<equation>|f(1)|>|f(-1)|</equation>应选C.

（法二）由于<equation>f ( x ) f^{\prime} ( x ) > 0</equation>，即恒大于零，故<equation>f ( x )</equation>恒大于零或<equation>f ( x )</equation>恒小于零（否则由<equation>f ( x )</equation>的连续性可知<equation>f ( x )</equation>存在零点，从而<equation>f ( x ) f^{\prime} ( x )</equation>不恒大于零).

若<equation>f ( x ) > 0</equation>，则<equation>f^{\prime}(x) > 0</equation>，故<equation>f ( x )</equation>单调增加. 因此<equation>f ( 1 ) > f (- 1 ) > 0.</equation>若<equation>f(x) < 0</equation>，则<equation>f^{\prime}(x) < 0</equation>，故<equation>f(x)</equation>单调减少．因此<equation>f(1) < f(-1) < 0</equation>综上所述，<equation>|f(1)| > |f(-1)|</equation>应选C.

（法三）排除法.

取<equation>f(x) = \mathrm{e}^{x}</equation>，则<equation>f(x)</equation>满足<equation>f(x)f^{\prime}(x) = \mathrm{e}^{x}\cdot \mathrm{e}^{x} > 0</equation>，且<equation>f (1) > f (- 1) > 0, \quad | f (1) | > | f (- 1) |,</equation>故可以排除选项B、D.

取<equation>f ( x )=-\mathrm{e}^{x}</equation>，则<equation>f ( x )</equation>满足<equation>f ( x ) f^{\prime} ( x )=(-\mathrm{e}^{x})\cdot(-\mathrm{e}^{x})>0</equation>，且<equation>f ( 1 ) < f ( - 1 ) < 0</equation>，故可以排除选项A.

因此，应选C.

---

**2017年第17题 | 解答题 | 10分**

17. (本题满分10分）

已知函数 y(x)由方程<equation>x^{3}+y^{3}-3 x+3 y-2=0</equation>确定，求 y(x）的极值.

**答案:**## 极大值为<equation>y ( 1 ) = 1</equation>，极小值为<equation>y (- 1 ) = 0.</equation>

**解析:**解 对方程两端关于 x求导，得<equation>3 x ^ {2} + 3 y ^ {2} y ^ {\prime} - 3 + 3 y ^ {\prime} = 0.</equation>整理得<equation>\left(y ^ {2} + 1\right) y ^ {\prime} = 1 - x ^ {2}.</equation>由于<equation>y^{2} + 1 > 0</equation>，故<equation>y(x)</equation>的全部驻点为<equation>x = 1</equation>和<equation>x = -1</equation>将 x=1代入方程<equation>x^{3}+y^{3}-3 x+3 y-2=0</equation>，得<equation>y^{3}+3 y-4=0</equation>. 通过观察发现 y=1是该方程的一个根.由于<equation>\frac{\mathrm{d}\left(y^{3}+3 y-4\right)}{\mathrm{d} y}=3 y^{2}+3>0</equation>，故<equation>y^{3}+3 y-4</equation>关于 y单调增加. y=1是<equation>y^{3}+3 y-4=0</equation>的唯

将 x=-1代入方程<equation>x^{3}+y^{3}-3x+3y-2=0</equation>，得<equation>y^{3}+3y=0</equation>，即<equation>y(y^{2}+3)=0. y=0</equation>是该方程的唯一实根，<equation>y(-1)=0.</equation>下面用两种方法来判断驻点的极值点类型.

（法一）对（1）式两端关于<equation>x</equation>求导，得<equation>\left(y ^ {2} + 1\right) y ^ {\prime \prime} + 2 y \left(y ^ {\prime}\right) ^ {2} = - 2 x.</equation>利用（2）式计算驻点<equation>x = \pm 1</equation>处的二阶导数.

由于在驻点处<equation>y^{\prime} = 0</equation>，故当<equation>x = \pm 1</equation>时，<equation>\left(y ^ {2} + 1\right) y ^ {\prime \prime} = - 2 x.</equation>当 x=1时，(3)式化为<equation>2 y^{\prime \prime}(1)=-2,y^{\prime \prime}(1)=-1<0</equation>；当 x=-1时，(3)式化为<equation>y^{\prime \prime}(-1)=2>0.</equation>因此，<equation>y(1)=1</equation>为极大值，<equation>y(-1)=0</equation>为极小值.

（法二）由（1）式可得<equation>y^{\prime} = \frac{1 - x^{2}}{y^{2} + 1}</equation>.注意到<equation>y^{2} + 1</equation>恒大于零，故<equation>y^{\prime}(x)</equation>与<equation>y(x)</equation>的性质如下表.

<table border="1"><tr><td>x</td><td>(-∞,-1)</td><td>-1</td><td>(-1,1)</td><td>1</td><td>(1,+∞)</td></tr><tr><td>y&#x27;(x)</td><td>-</td><td>0</td><td>+</td><td>0</td><td>-</td></tr><tr><td>y(x)</td><td>单调减少</td><td>极小值</td><td>单调增加</td><td>极大值</td><td>单调减少</td></tr></table>

因此，<equation>y ( 1 ) = 1</equation>为极大值，<equation>y (- 1 ) = 0</equation>为极小值.

---

**2014年第16题 | 解答题 | 10分**

16. (本题满分10分）

设函数<equation>y=f(x)</equation>由方程<equation>y^{3}+xy^{2}+x^{2}y+6=0</equation>确定，求 f(x)的极值.

**答案:**16) 极小值为 f（1）=-2.

**解析:**方程<equation>y^{3}+xy^{2}+x^{2}y+6=0</equation>两端关于 x求导，得<equation>3 y ^ {2} y ^ {\prime} + y ^ {2} + 2 x y y ^ {\prime} + 2 x y + x ^ {2} y ^ {\prime} = 0.</equation>令<equation>y^{\prime}=0</equation>，则有<equation>y^{2}+2 x y=0</equation>，从而<equation>y=0</equation>或<equation>y=-2 x</equation>.将<equation>y=0</equation>代入原方程得到6=0，矛盾，故<equation>y\neq</equation>0，从而<equation>y=-2 x</equation>.将其代入到原方程得到<equation>6 x^{3}=6</equation>，解得<equation>x=1, y=-2</equation>，于是<equation>f(1)=-2, f^{\prime}(1)=0.</equation>对（1）式两端关于 x求导，整理得到<equation>6 y \left(y ^ {\prime}\right) ^ {2} + 3 y ^ {2} y ^ {\prime \prime} + 4 y y ^ {\prime} + 2 x \left(y ^ {\prime}\right) ^ {2} + 2 x y y ^ {\prime \prime} + 2 y + 4 x y ^ {\prime} + x ^ {2} y ^ {\prime \prime} = 0.</equation>将 x=1，f（1）=-2及<equation>f^{\prime} ( 1 )=0</equation>代入上式，得到<equation>f^{\prime\prime} ( 1 )=\frac{4}{9}>0.</equation>因此 x=1是 f(x)的极小值点，极小值为 f（1）=-2.

---

**2010年第16题 | 解答题 | 10分**

16. (本题满分10分)

求函数<equation>f ( x )=\int_{1}^{x^{2}}(x^{2}-t)\mathrm{e}^{-t^{2}}\mathrm{d} t</equation>的单调区间与极值.

**答案:**(16)<equation>f ( x )</equation>的单调增加区间为<equation>(-1,0)</equation>和<equation>( 1,+\infty)</equation>；<equation>f ( x )</equation>的单调减少区间为<equation>(-\infty,-1)</equation>和(0,1)；<equation>f ( x )</equation>的极小值为<equation>f (\pm1)=0</equation>，极大值为<equation>f ( 0 )=\frac{1}{2}\left( 1-\frac{1} {\mathrm{e}} \right).</equation>

**解析:**解 先求<equation>f^{\prime}(x).</equation>由于在变限积分<equation>\int_{1}^{x^{2}}(x^{2}-t)\mathrm{e}^{-t^{2}}\mathrm{d}t</equation>中，x不是积分变量，故可以把它提到积分号外.<equation>f (x) = \int_ {1} ^ {x ^ {2}} \left(x ^ {2} - t\right) \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t = x ^ {2} \int_ {1} ^ {x ^ {2}} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t - \int_ {1} ^ {x ^ {2}} t \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t.</equation>根据变限积分函数的求导公式以及求导的乘法法则，<equation>f ^ {\prime} (x) = 2 x \int_ {1} ^ {x ^ {2}} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t + 2 x ^ {3} \mathrm {e} ^ {- x ^ {4}} - 2 x ^ {3} \mathrm {e} ^ {- x ^ {4}} = 2 x \int_ {1} ^ {x ^ {2}} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t.</equation><equation>f^{\prime}(x) = 0</equation>当且仅当<equation>x = 0</equation>或<equation>\int_{1}^{x^{2}}\mathrm{e}^{-t^{2}}\mathrm{d}t = 0.</equation>由于<equation>\mathrm{e}^{-t^{2}}</equation>恒大于零，故当且仅当<equation>x^{2} = 1</equation>，即<equation>x = \pm 1</equation>时，<equation>\int_{1}^{x^{2}}\mathrm{e}^{-t^{2}}\mathrm{d}t = 0.</equation>因此，<equation>x = 0,\pm 1</equation>为<equation>f(x)</equation>的驻点.

对<equation>\int_{1}^{x^{2}}\mathrm{e}^{-t^{2}}\mathrm{d}t</equation>来说，当<equation>x^{2} < 1</equation>时，<equation>\int_{1}^{x^{2}}\mathrm{e}^{-t^{2}}\mathrm{d}t < 0</equation>；当<equation>x^{2} > 1</equation>时，<equation>\int_{1}^{x^{2}}\mathrm{e}^{-t^{2}}\mathrm{d}t > 0</equation>因此有下表.

<table border="1"><tr><td>x</td><td>(-∞,-1)</td><td>-1</td><td>(-1,0)</td><td>0</td><td>(0,1)</td><td>1</td><td>(1,+∞)</td></tr><tr><td><equation>f^{\prime}(x)</equation></td><td>-</td><td>0</td><td>+</td><td>0</td><td>-</td><td>0</td><td>+</td></tr><tr><td>f(x)</td><td>单调减少</td><td>极小值</td><td>单调增加</td><td>极大值</td><td>单调减少</td><td>极小值</td><td>单调增加</td></tr></table>

由此可知，<equation>f ( x )</equation>的单调增加区间为<equation>(-1,0)</equation>和<equation>( 1,+\infty)</equation>；<equation>f ( x )</equation>的单调减少区间为<equation>(-\infty,-1)</equation>和(0，1)；<equation>f (-1)</equation>和f(1)为<equation>f ( x )</equation>的极小值，<equation>f (- 1) = f (1) = \int_ {1} ^ {1} (1 - t) \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t = 0;</equation>f（0）为f（x）的极大值，<equation>f (0) = \int_ {1} ^ {0} (- t) \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t = \frac {1}{2} \left(1 - \frac {1}{\mathrm {e}}\right).</equation>

---


#### 导数的几何意义

**2018年第10题 | 填空题 | 4分**

10. 设函数 f(x)具有2阶连续导数.若曲线 y=f(x)过点(0,0)且与曲线 y=2<equation>^{x}</equation>在点(1,2)处相切，则<equation>\int_{0}^{1} x f^{\prime\prime}(x) \mathrm{d} x=</equation>___

**答案:**## 2ln2-2.

**解析:**解 由于曲线<equation>y=2^{x}</equation>与曲线<equation>y=f(x)</equation>在点（1,2）处相切，故曲线<equation>y=f(x)</equation>过点（1,2).于是，<equation>f(1)=2.</equation>又因为曲线<equation>y=f(x)</equation>过点（0,0），所以<equation>f(0)=0.</equation>根据导数的几何意义，曲线<equation>y=f(x)</equation>在点（1,2）处的斜率为<equation>f^{\prime}(1)</equation>，而由于两条曲线相切，故<equation>f^{\prime}(1)=\left(2^{x}\right)^{\prime}\big|_{x=1}=2\ln 2.</equation>下面计算<equation>\int_0^1 xf^{\prime \prime}(x)\mathrm{d}x.</equation><equation>\begin{aligned} \int_ {0} ^ {1} x f ^ {\prime \prime} (x) \mathrm {d} x \xlongequal {\text {分 部 积 分}} \int_ {0} ^ {1} x \mathrm {d} \left[ f ^ {\prime} (x) \right] &= x f ^ {\prime} (x) \left| _ {0} ^ {1} - \int_ {0} ^ {1} f ^ {\prime} (x) \mathrm {d} x \right. \\ &= f ^ {\prime} (1) - \left[ f (1) - f (0) \right] = 2 \ln 2 - (2 - 0) = 2 \ln 2 - 2. \end{aligned}</equation>

---


#### 方程根的存在性与个数

**2017年第18题 | 解答题 | 10分**

18. (本题满分10分)

设函数 f(x)在区间[0,1]上具有2阶导数，且<equation>f(1)>0,\lim_{x\rightarrow 0^{+}}\frac{f(x)}{x}<0.</equation>证明：

I. 方程 f(x)=0在区间（0,1）内至少存在一个实根；

II. 方程<equation>f(x)f^{\prime \prime}(x)+[f^{\prime}(x)]^{2}=0</equation>在区间（0,1）内至少存在两个不同实根.

**答案:**## （ I ）证明略；（ II ）证明略.

**解析:**证（I）由于<equation>\lim_{x\to 0^{+}}\frac{f(x)}{x}<0</equation>，故由函数极限的局部保号性可知，存在<equation>\theta >0</equation>，在（0，<equation>\theta</equation>）内，<equation>\frac{f(x)}{x}<0</equation>从而<equation>f(x) < 0</equation>.取<equation>0 < \delta < \theta</equation>，则<equation>f(\delta) < 0.</equation>又因为<equation>f ( 1 ) > 0</equation>，所以由连续函数的零点定理知，存在<equation>\xi \in (\delta,1)\subseteq(0,1)</equation>使得<equation>f (\xi)=0.</equation>因此，<equation>f ( x )=0</equation>在区间（0,1）内至少存在一个实根.

（Ⅱ）考虑<equation>F ( x )=f ( x ) f^{\prime} ( x )</equation>，则<equation>F ^ {\prime} (x) = f (x) f ^ {\prime \prime} (x) + \left[ f ^ {\prime} (x) \right] ^ {2}.</equation>第（Ⅱ）问等价于证明<equation>F^{\prime}(x)=0</equation>在区间（0,1）内至少存在两个不同实根.

若能找到三个点 a < b < c，使得<equation>F ( a )=F ( b )=F ( c )</equation>，则由罗尔定理知，存在<equation>\eta_{1}\in(a,b),</equation><equation>\eta_{2}\in(b,c)</equation>，满足<equation>F^{\prime}(\eta_{1})=0,F^{\prime}(\eta_{2})=0.</equation>由<equation>\lim_{x\rightarrow 0^{+}}\frac{f(x)}{x}<0</equation>知，分母趋于零，而极限仍存在，故<equation>f (0) \xlongequal {\text {连 续 性}} \lim _ {x \rightarrow 0 ^ {+}} f (x) = 0, \quad F (0) = f (0) f ^ {\prime} (0) = 0.</equation>由第（I）问的结论知，存在<equation>x_{1}\in(0,1)</equation>，满足<equation>f \left( x_{1} \right)=0</equation>，从而<equation>F \left( x_{1} \right)=f \left( x_{1} \right) f^{\prime} \left( x_{1} \right)=0.</equation>另一方面，由于<equation>f ( 0 )=0</equation><equation>f \left(x_{1}\right)=0</equation>，故由罗尔定理知，存在<equation>x_{2}\in\left(0,x_{1}\right)</equation>，使得<equation>f^{\prime}\left(x_{2}\right)=0</equation>，从而<equation>F \left(x_{2}\right)=f \left(x_{2}\right) f^{\prime}\left(x_{2}\right)=0.</equation>如图所示，<equation>0 < x_{2} < x_{1}, F(0) = F(x_{2}) = F(x_{1}) = 0.</equation>由罗尔定理知，存

在<equation>\eta_{1}\in (0,x_{2})</equation>，使得<equation>F^{\prime}(\eta_{1}) = 0</equation>；存在<equation>\eta_{2}\in (x_{2},x_{1})</equation>，使得<equation>F^{\prime}(\eta_{2}) = 0</equation>。命题得证.

---

**2011年第17题 | 解答题 | 10分**

17. (本题满分10分）

求方程<equation>k \arctan x-x=0</equation>不同实根的个数，其中 k为参数.

**答案:**## (17) 当<equation>k \leqslant 1</equation>时，原方程有1个实根；当<equation>k > 1</equation>时，原方程有3个不同的实根.

**解析:**解 令<equation>f ( x ) = k \arctan x - x</equation>，显然<equation>f ( 0 ) = 0</equation>且<equation>f ( x ) = - f (- x )</equation>即<equation>f ( x )</equation>为奇函数，故只需讨论<equation>x > 0</equation>时<equation>f ( x )</equation>零点的情况.又<equation>f^{\prime} ( x )=\frac{k}{1+x^{2}}-1=\frac{(k-1)-x^{2}}{1+x^{2}}</equation>我们对k分情况讨论如下若<equation>k \leqslant 1</equation>当<equation>x \in(0,+\infty)</equation>时，<equation>f^{\prime} ( x ) < 0</equation>从而<equation>f ( x )</equation>在<equation>[ 0,+\infty)</equation>上单调减少，又<equation>f ( 0 ) = 0</equation>故<equation>f ( x )</equation>在<equation>( 0,+\infty)</equation>内没有零点，从而<equation>f ( x )</equation>在R上只有1个零点<equation>x=0.</equation>若<equation>k > 1</equation>，当<equation>x\in(0,\sqrt{k-1})</equation>时，<equation>f^{\prime}(x)>0</equation>，从而<equation>f(x)</equation>在<equation>[0,\sqrt{k-1}]</equation>上单调增加，又<equation>f(0)=0</equation>，故<equation>f(x)</equation>在<equation>(0,\sqrt{k-1}]</equation>上无零点；当<equation>x\in(\sqrt{k-1},+\infty)</equation>时，<equation>f^{\prime}(x)<0</equation>从而<equation>f(x)</equation>在<equation>[\sqrt{k-1},+\infty)</equation>上单调减少，又<equation>f(\sqrt{k-1})>f(0)</equation><equation>= 0</equation>，且<equation>\lim_{x\to +\infty}f(x) = -\infty</equation>，故由连续函数的零点定理及<equation>f(x)</equation>的单调性可知，<equation>f(x)</equation>在<equation>(\sqrt{k-1},+\infty)</equation>内恰好只有1个零点，记为a.

因此，<equation>f ( x )</equation>在<equation>( 0, + \infty)</equation>内只有1个零点a，再由对称性可知，<equation>f ( x )</equation>在<equation>(-\infty , 0)</equation>内也只有1个零点一a，从而<equation>f ( x )</equation>在R上有3个零点，分别为一a,0,a，如图所示.

综上所述，当<equation>k \leqslant 1</equation>时，原方程有1个实根；当<equation>k > 1</equation>时，原方程有3个不同的实根.

---


#### 不等式的证明

**2012年第15题 | 解答题 | 10分**

15. (本题满分10分)

证明：<equation>x\ln \frac{1+x}{1-x}+\cos x\geqslant 1+\frac{x^{2}}{2},(-1<x<1).</equation>

**答案:**15) 证明略.

**解析:**证（法一）考虑辅助函数<equation>f ( x )=x \ln \frac{1+x}{1-x}+\cos x-1-\frac{x^{2}}{2}.</equation><equation>f (- x) = (- x) \ln \frac {1 - x}{1 + x} + \cos x - 1 - \frac {x ^ {2}}{2} = f (x),</equation>故 f(x)为偶函数.如果能证明当 x<equation>\in[0,1)</equation>时，<equation>f(x)\geqslant0</equation>，那么当 x<equation>\in(-1,1)</equation>时，也有 f(x)<equation>\geqslant0</equation>从而题给不等式成立.

计算<equation>f^{\prime}(x)</equation><equation>f ^ {\prime} (x) = \left(x \ln \frac {1 + x}{1 - x} + \cos x - 1 - \frac {x ^ {2}}{2}\right) ^ {\prime} = \frac {2 x}{1 - x ^ {2}} + \ln \frac {1 + x}{1 - x} - \sin x - x.</equation>由于当<equation>x\in [0,1)</equation>时，<equation>\frac{x}{1 - x^2}\geqslant x\geqslant \sin x</equation>，故<equation>\frac {2 x}{1 - x ^ {2}} \geqslant 2 x \geqslant \sin x + x,</equation>等号在<equation>x=0</equation>时取得.又因为<equation>\frac{1+x}{1-x}\geqslant 1</equation>，所以<equation>\ln \frac{1+x}{1-x}\geqslant 0</equation>，等号在<equation>x=0</equation>时取得.

因此，当<equation>x\in(0,1)</equation>时，<equation>f ^ {\prime} (x) = \frac {2 x}{1 - x ^ {2}} + \ln \frac {1 + x}{1 - x} - \sin x - x > 0.</equation>综上所述，<equation>f ( x )</equation>在[0,1)上单调增加，<equation>f ( 0 )</equation>为<equation>f ( x )</equation>在[0,1)上的最小值.又由<equation>f ( x )</equation>为偶函数可知，在(-1，1)上，<equation>f ( x ) \geqslant f ( 0 ) = 0</equation>即<equation>x \ln \frac{1+x}{1-x} +\cos x\geqslant 1+\frac{x^{2}}{2}(-1<x<1).</equation>（法二）在法一中求得<equation>f^{\prime}(x)=\frac{2x}{1-x^{2}}+\ln \frac{1+x}{1-x}-\sin x-x</equation>后，继续求<equation>f^{\prime\prime}(x)</equation>以判断<equation>f^{\prime}(x)</equation>的性质.<equation>f ^ {\prime \prime} (x) = \frac {2 \left(1 + x ^ {2}\right)}{\left(1 - x ^ {2}\right) ^ {2}} + \frac {1}{1 + x} - \frac {(- 1)}{1 - x} - \cos x - 1 = \frac {4}{\left(1 - x ^ {2}\right) ^ {2}} - \cos x - 1.</equation>由于当 x<equation>\in[0,1)</equation>时，<equation>\frac {4}{\left(1 - x ^ {2}\right) ^ {2}} \geqslant 4, \quad 1 + \cos x \leqslant 2,</equation>故<equation>f^{\prime \prime}(x) > 0. f^{\prime}(x)</equation>在[0，1）上单调增加，<equation>f^{\prime}(x)\geqslant f^{\prime}(0)=0,f(x)</equation>在[0，1）上单调增加.

（法三）首先，<equation>f ( x ) = x \ln \frac { 1 + x } { 1 - x } + \cos x</equation>为偶函数，<equation>g ( x ) = 1 + \frac { x^{2}}{2}</equation>也为偶函数，故我们只需证明，在（0，1）上，<equation>f ( x ) \geqslant g ( x )</equation>，并且<equation>f ( 0 ) = g ( 0 )</equation>，便能得到在（-1，1）上，<equation>f ( x ) \geqslant g ( x )</equation>由泰勒中值定理，<equation>\cos x=1-\frac{x^{2}}{2!}+\frac{\cos \xi}{4!} x^{4},\xi</equation>为介于0和x之间的某个值.于是，当<equation>x\in(0,1)</equation>时，<equation>\cos x\geqslant 1-\frac{x^{2}}{2}.</equation>从而<equation>f (x) = x \ln \frac {1 + x}{1 - x} + \cos x \geqslant x \ln \frac {1 + x}{1 - x} + 1 - \frac {x ^ {2}}{2}.</equation>若能证明<equation>x\ln \frac{1+x}{1-x}+1-\frac{x^{2}}{2}\geqslant 1+\frac{x^{2}}{2}</equation>，则由不等号的传递性可知原不等式得证.

由于当 x<equation>\in(0,1)</equation>时，<equation>x \ln \frac {1 + x}{1 - x} + 1 - \frac {x ^ {2}}{2} \geqslant 1 + \frac {x ^ {2}}{2} \Leftrightarrow x \ln \frac {1 + x}{1 - x} \geqslant x ^ {2} \Leftrightarrow \ln \frac {1 + x}{1 - x} \geqslant x,</equation>故我们只需要证明<equation>\ln \frac{1+x}{1-x}\geqslant x.</equation>考虑<equation>\varphi(x)=\ln \frac{1+x}{1-x}-x.</equation><equation>\varphi^ {\prime} (x) = \frac {1}{1 + x} - \frac {(- 1)}{1 - x} - 1 = \frac {2}{1 - x ^ {2}} - 1.</equation>当 x<equation>\in(0,1)</equation>时，<equation>\frac{2}{1-x^{2}}\geqslant2</equation>从而<equation>\varphi^{\prime}(x)=\frac{2}{1-x^{2}}-1>0, \varphi(x)</equation>在（0，1）上单调增加，<equation>\varphi(x)\geqslant\varphi(0)=0.</equation>综上所述，原不等式成立.

---


### 无穷级数


#### 常数项级数敛散性的判定

**2025年第2题 | 选择题 | 5分 | 答案: B**

2. 已知级数：<equation>\textcircled{1} \sum_{n=1}^{\infty} \sin \frac{n^{3} \pi}{n^{2}+1}</equation><equation>\textcircled{2} \sum_{n=1}^{\infty}(-1)^{n}\left(\frac{1}{\sqrt[3]{n^{2}}}-\tan \frac{1}{\sqrt[3]{n^{2}}}\right)</equation>，则（    )

A.<equation>\textcircled{1}</equation>与<equation>\textcircled{2}</equation>均条件收敛 B.<equation>\textcircled{1}</equation>条件收敛，<equation>\textcircled{2}</equation>绝对收敛

C.<equation>\textcircled{1}</equation>绝对收敛，<equation>\textcircled{2}</equation>条件收敛 D.<equation>\textcircled{1}</equation>与<equation>\textcircled{2}</equation>均绝对收敛

答案: B

**解析:**解 对级数<equation>\textcircled{1}</equation>注意到<equation>\sin \frac{n^{3}\pi}{n^{2}+1}=\sin \frac{\left(n^{3}+n-n\right)\pi}{n^{2}+1}=\sin \left(n\pi-\frac{n\pi}{n^{2}+1}\right)=(-1)^{n-1}\sin \frac{n\pi}{n^{2}+1},</equation>故<equation>\left| \sin \frac{n^{3}\pi}{n^{2}+1}\right|=\sin \frac{n\pi}{n^{2}+1}.</equation>又因为<equation>\lim _ {n \rightarrow \infty} \frac {\sin \frac {n \pi}{n ^ {2} + 1}}{\frac {1}{n}} \xlongequal {\text {对 应}} \frac {\sin \frac {n \pi}{n ^ {2} + 1} - \frac {n \pi}{n ^ {2} + 1}}{\frac {1}{n}} \lim _ {n \rightarrow \infty} \frac {\frac {n \pi}{n ^ {2} + 1}}{\frac {1}{n}} = \lim _ {n \rightarrow \infty} \frac {n ^ {2} \pi}{n ^ {2} + 1} = \pi ,</equation>所以<equation>\sum_{n=1}^{\infty}\sin \frac{n\pi}{n^{2}+1}</equation>与<equation>\sum_{n=1}^{\infty}\frac{1}{n}</equation>同敛散，而<equation>\sum_{n=1}^{\infty}\frac{1}{n}</equation>发散，于是<equation>\sum_{n=1}^{\infty}\sin \frac{n\pi}{n^{2}+1}</equation>发散，即<equation>\sum_{n=1}^{\infty}\left|\sin \frac{n^{3}\pi}{n^{2}+1}\right|</equation>发散另一方面，对正整数<equation>n,\frac{n\pi}{n^{2}+1}\in\left(0,\frac{\pi}{2}\right]</equation>，而<equation>\frac{n\pi}{n^{2}+1}</equation>关于n单调减少趋于0，从而<equation>\sin \frac{n\pi}{n^{2}+1}</equation>关于n单调减少趋于0.由交错级数的莱布尼茨定理可知，<equation>\sum_{n=1}^{\infty}(-1)^{n-1}\sin \frac{n\pi}{n^{2}+1}</equation>收敛，即<equation>\sum_{n=1}^{\infty}\sin \frac{n^{3}\pi}{n^{2}+1}</equation>收敛因此，级数<equation>\textcircled{1}</equation>条件收敛.

对级数<equation>\textcircled{2}</equation>，考虑<equation>\tan x</equation>在<equation>x=0</equation>处带佩亚诺余项的三阶泰勒公式：<equation>\tan x=x+\frac{1}{3} x^{3}+o\left(x^{3}\right).</equation>由此可得<equation>\tan \frac{1}{\sqrt[3]{n^{2}}}=\frac{1}{\sqrt[3]{n^{2}}}+\frac{1}{3}\cdot \frac{1}{n^{2}}+o\left(\frac{1}{n^{2}}\right)</equation>，进一步可得当<equation>n\to\infty</equation>时，<equation>\tan \frac{1}{\sqrt[3]{n^{2}}}-\frac{1}{\sqrt[3]{n^{2}}}\sim \frac{1}{3n^{2}}.</equation>于是，<equation>\sum_{n=1}^{\infty}\left(\tan \frac{1}{\sqrt[3]{n^{2}}}-\frac{1}{\sqrt[3]{n^{2}}}\right)</equation>与<equation>\sum_{n=1}^{\infty}\frac{1}{n^{2}}</equation>同敛散，而<equation>\sum_{n=1}^{\infty}\frac{1}{n^{2}}</equation>收敛，从而<equation>\sum_{n=1}^{\infty}\left(\tan \frac{1}{\sqrt[3]{n^{2}}}-\frac{1}{\sqrt[3]{n^{2}}}\right)</equation>收敛. 又由于<equation>\left| (- 1) ^ {n} \left(\frac {1}{\sqrt [ 3 ]{n ^ {2}}} - \tan \frac {1}{\sqrt [ 3 ]{n ^ {2}}}\right) \right| = \tan \frac {1}{\sqrt [ 3 ]{n ^ {2}}} - \frac {1}{\sqrt [ 3 ]{n ^ {2}}},</equation>故<equation>\sum_{n=1}^{\infty}(-1)^{n}\left(\frac{1}{\sqrt[3]{n^{2}}}-\tan \frac{1}{\sqrt[3]{n^{2}}}\right)</equation>绝对收敛.

因此，级数<equation>\textcircled{2}</equation>绝对收敛综上所述，应选B.

---

**2023年第4题 | 选择题 | 5分 | 答案: A**

4. 已知<equation>a_{n} < b_{n} ( n=1,2,\cdots)</equation>，若级数<equation>\sum_{n=1}^{\infty} a_{n}</equation>与<equation>\sum_{n=1}^{\infty} b_{n}</equation>均收敛，则“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的（    ）

A. 充分必要条件 B. 充分不必要条件

C. 必要不充分条件 D. 既不充分也不必要条件

答案: A

**解析:**解（法一）由<equation>a_{n} < b_{n}</equation>可知，<equation>\sum_{n = 1}^{\infty}\left(b_{n} - a_{n}\right)</equation>为正项级数.进一步，由<equation>\sum_{n = 1}^{\infty}a_{n}</equation>与<equation>\sum_{n = 1}^{\infty}b_{n}</equation>均收敛以及收敛级数的性质可知，<equation>\sum_ {n = 1} ^ {\infty} \left(b _ {n} - a _ {n}\right) = \sum_ {n = 1} ^ {\infty} b _ {n} - \sum_ {n = 1} ^ {\infty} a _ {n}.</equation>于是，<equation>\sum_{n=1}^{\infty} \left(b_{n}-a_{n}\right)</equation>为收敛的正项级数，从而<equation>\sum_{n=1}^{\infty} \left(b_{n}-a_{n}\right)</equation>绝对收敛.

由三角不等式可得<equation>\left| b _ {n} \right| = \left| b _ {n} - a _ {n} + a _ {n} \right| \leqslant \left| b _ {n} - a _ {n} \right| + \left| a _ {n} \right|,</equation><equation>\left| a _ {n} \right| = \left| a _ {n} - b _ {n} + b _ {n} \right| \leqslant \left| b _ {n} - a _ {n} \right| + \left| b _ {n} \right|.</equation>若<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛，即<equation>\sum_{n=1}^{\infty} \mid a_{n} \mid</equation>收敛，则由（1）式以及正项级数的比较审敛法可知<equation>\sum_{n=1}^{\infty} \mid b_{n} \mid</equation>收敛，从而<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛.“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的充分条件.

若<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛，即<equation>\sum_{n=1}^{\infty} \mid b_{n} \mid</equation>收敛，则由（2）式以及正项级数的比较审敛法可知<equation>\sum_{n=1}^{\infty} \mid a_{n} \mid</equation>收敛，从而<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛.“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的必要条件.

综上所述，“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的充分必要条件，应选A.

（法二）先考虑充分性.

设<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛，即<equation>\sum_{n=1}^{\infty} \mid a_{n}\mid</equation>收敛.

考虑正项级数<equation>\sum_{n=1}^{\infty} \frac{\mid b_{n}\mid -b_{n}}{2}.</equation>对<equation>\{b_{n}\}</equation>中小于0的项，<equation>a_{n} < b_{n} < 0</equation>，于是<equation>\left| a _ {n} \right| = - a _ {n} > - b _ {n} = \frac {\left| b _ {n} \right| - b _ {n}}{2} > 0.</equation>对<equation>\{b_{n}\}</equation>中大于等于0的项，<equation>\left| a _ {n} \right| \geqslant 0 = \frac {\left| b _ {n} \right| - b _ {n}}{2}.</equation>从而，对所有正整数 n，都有<equation>|a_{n}| \geqslant \frac{|b_{n}| - b_{n}}{2} \geqslant 0.</equation>由正项级数的比较审敛法可知，级数<equation>\sum_{n=1}^{\infty} \frac{\mid b_{n}\mid -b_{n}}{2}</equation>收敛. 进一步，<equation>\sum_ {n = 1} ^ {\infty} \left| b _ {n} \right| = \sum_ {n = 1} ^ {\infty} \left[ 2 \left(\frac {\left| b _ {n} \right| - b _ {n}}{2}\right) + b _ {n} \right] = 2 \sum_ {n = 1} ^ {\infty} \frac {\left| b _ {n} \right| - b _ {n}}{2} + \sum_ {n = 1} ^ {\infty} b _ {n}.</equation>由<equation>\sum_{n=1}^{\infty}b_{n}</equation>收敛以及收敛级数的性质可知，<equation>\sum_{n=1}^{\infty}|\boldsymbol{b}_{n}|</equation>收敛，从而<equation>\sum_{n=1}^{\infty}b_{n}</equation>绝对收敛.

因此，“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的充分条件.

再考虑必要性.

由<equation>a_{n} < b_{n}</equation>可得<equation>-b_{n} < -a_{n}</equation>. 由<equation>\sum_{n=1}^{\infty} a_{n}</equation>与<equation>\sum_{n=1}^{\infty} b_{n}</equation>均收敛可知<equation>\sum_{n=1}^{\infty} (-a_{n})</equation>与<equation>\sum_{n=1}^{\infty} (-b_{n})</equation>均收敛.于是，同充分性的证明可知<equation>\sum_{n=1}^{\infty} (-b_{n})</equation>绝对收敛蕴含<equation>\sum_{n=1}^{\infty} (-a_{n})</equation>绝对收敛，即<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛蕴含<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛.

因此，“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的必要条件.

综上所述，“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的充分必要条件，应选A.

---

**2019年第3题 | 选择题 | 4分 | 答案: D**

3. 设<equation>\{u_{n}\}</equation>是单调增加的有界数列，则下列级数中收敛的是（    ）

A.<equation>\sum_{n=1}^{\infty}\frac{u_{n}}{n}</equation>B.<equation>\sum_{n=1}^{\infty}(-1)^{n}\frac{1}{u_{n}}</equation>C.<equation>\sum_{n=1}^{\infty}\left(1-\frac{u_{n}}{u_{n+1}}\right)</equation>D.<equation>\sum_{n=1}^{\infty}\left(u_{n+1}^{2}-u_{n}^{2}\right)</equation>

答案: D

**解析:**解（法一）由于<equation>u_{n+1}^{2}-u_{n}^{2}=(u_{n+1}+u_{n})(u_{n+1}-u_{n})</equation>，而<equation>\{u_{n}\}</equation>有界，故存在正数M，使得<equation>|u_{n+1}^{2}-u_{n}^{2}| \leqslant 2M|u_{n+1}-u_{n}| \frac{u_{n}}{2M(u_{n+1}-u_{n})}.</equation>单调增加考虑正项级数<equation>\sum_{n=1}^{\infty}(u_{n+1}-u_{n}).</equation>该级数的部分和为<equation>s _ {n} = \sum_ {k = 1} ^ {n} \left(u _ {k + 1} - u _ {k}\right) = \left(u _ {2} - u _ {1}\right) + \left(u _ {3} - u _ {2}\right) + \dots + \left(u _ {n + 1} - u _ {n}\right) = u _ {n + 1} - u _ {1}.</equation>由于<equation>\{u_{n}\}</equation>是单调增加的有界数列，故<equation>\lim_{n\to \infty}u_{n+1}</equation>存在，从而<equation>\lim_{n\to \infty}s_{n}</equation>存在，级数<equation>\sum_{n=1}^{\infty}\left(u_{n+1}-u_{n}\right)</equation>收敛由比较审敛法可知，<equation>\sum_{n=1}^{\infty}\left|u_{n+1}^{2}-u_{n}^{2}\right|</equation>收敛，从而<equation>\sum_{n=1}^{\infty}\left(u_{n+1}^{2}-u_{n}^{2}\right)</equation>收敛.应选D.

（法二）排除法.

选项A：取<equation>u_{n}=1-\frac{1}{n}</equation>，则<equation>\frac{u_{n}}{n}=\frac{1}{n}-\frac{1}{n^{2}}.</equation>由于<equation>\sum_{n=1}^{\infty}\frac{1}{n}</equation>发散，<equation>\sum_{n=1}^{\infty}\frac{1}{n^{2}}</equation>收敛，故<equation>\sum_{n=1}^{\infty}\left(\frac{1}{n}-\frac{1}{n^{2}}\right)</equation>发散.选项A不正确.

选项B、C：取<equation>u_{n}=-\frac{1}{n}</equation>，则<equation>(-1)^{n}\frac{1}{u_{n}}=(-1)^{n+1}n,\sum_{n=1}^{\infty}(-1)^{n}\frac{1}{u_{n}}</equation>发散；<equation>1-\frac{u_{n}}{u_{n+1}}=1-\frac{n+1}{n}=</equation><equation>-\frac{1}{n},\sum_{n=1}^{\infty}\left(1-\frac{u_{n}}{u_{n+1}}\right)</equation>发散. 选项B、C不正确.

由排除法可知，应选D.

---

**2016年第19题 | 解答题 | 10分**

19. (本题满分10分)

已知函数 f(x)可导，且<equation>f(0)=1</equation><equation>0<f^{\prime}(x)<\frac{1}{2}</equation>.设数列<equation>\{x_{n}\}</equation>满足<equation>x_{n+1}=f\left(x_{n}\right)\left(n=1,2,\cdots\right)</equation>.证明：

I. 级数<equation>\sum_{n=1}^{\infty}\left(x_{n+1}-x_{n}\right)</equation>绝对收敛；

II.<equation>\lim_{n\to\infty}x_{n}</equation>存在，且<equation>0<\lim_{n\to\infty}x_{n}<2.</equation>

**答案:**## （I）证明略；（Ⅱ）证明略.

**解析:**证（I）由题设知，<equation>\left| x _ {n + 1} - x _ {n} \right| = \left| f \left(x _ {n}\right) - f \left(x _ {n - 1}\right) \right| \frac {\text {拉 格朗 日}}{\text {中 值 定 理}} \left| f ^ {\prime} \left(\xi_ {n}\right) \left(x _ {n} - x _ {n - 1}\right) \right| \leqslant \frac {1}{2} \left| x _ {n} - x _ {n - 1} \right|,</equation>其中<equation>\xi_{n}</equation>介于<equation>x_{n}</equation>与<equation>x_{n - 1}</equation>之间（若<equation>x_{n} = x_{n - 1}</equation>，则取<equation>\xi_{n} = x_{n}</equation>，本题均作类似处理).递推得到<equation>\left| x _ {n + 1} - x _ {n} \right| \leqslant \frac {1}{2} \left| x _ {n} - x _ {n - 1} \right| \leqslant \frac {1}{2} \cdot \frac {1}{2} \left| x _ {n - 1} - x _ {n - 2} \right| \leqslant \dots \leqslant \frac {1}{2 ^ {n - 1}} \left| x _ {2} - x _ {1} \right|.</equation>又级数<equation>\sum_{n=1}^{\infty}\frac{1}{2^{n-1}} \mid x_{2}-x_{1}\mid = \mid x_{2}-x_{1}\mid \sum_{n=1}^{\infty}\frac{1}{2^{n-1}} = 2 \mid x_{2}-x_{1}\mid</equation>收敛，故由比较审敛法知，级数<equation>\sum_{n=1}^{\infty}\mid x_{n+1}-x_{n}\mid</equation>收敛，即<equation>\sum_{n=1}^{\infty}\left(x_{n+1}-x_{n}\right)</equation>绝对收敛，结论得证.

（Ⅱ）首先证明<equation>\lim x_{n}</equation>存在.


令<equation>S_{n} = \sum_{k = 1}^{n}\left(x_{k + 1} - x_{k}\right) = x_{n + 1} - x_{1}</equation>. 由（I）中结论知，级数<equation>\sum_{n = 1}^{\infty}\left(x_{n + 1} - x_{n}\right)</equation>绝对收敛，从而收敛，即<equation>\lim_{n\to \infty}S_n</equation>存在. 又<equation>x_{n + 1} = S_n + x_1</equation>，故<equation>\lim_{n\to \infty}x_{n + 1}</equation>存在，即<equation>\lim_{n\to \infty}x_n</equation>存在，结论得证.

（法二）单调有界准则.

若<equation>x_{1} < x_{2}</equation>，则由<equation>f^{\prime}(x) > 0</equation>知，<equation>x _ {3} - x _ {2} = f \left(x _ {2}\right) - f \left(x _ {1}\right) \frac {\text {拉 格 朗 日}}{\text {中 值 定 理}} f ^ {\prime} \left(\xi_ {2}\right) \left(x _ {2} - x _ {1}\right) > 0,</equation>其中<equation>x_{1} < \xi_{2} < x_{2}</equation>，于是<equation>x_{2} < x_{3}</equation>。假设<equation>x_{k} < x_{k + 1}</equation>，则由<equation>f^{\prime}(x) > 0</equation>知，<equation>x _ {k + 2} - x _ {k + 1} = f \left(x _ {k + 1}\right) - f \left(x _ {k}\right) \frac {\text {拉 格 朗 日}}{\text {中 值 定 理}} f ^ {\prime} \left(\xi_ {k + 1}\right) \left(x _ {k + 1} - x _ {k}\right) > 0,</equation>其中<equation>x_{k} < \xi_{k + 1} < x_{k + 1}</equation>，即<equation>x_{k + 1} < x_{k + 2}</equation>.由数学归纳法知，数列<equation>\{x_{n}\}</equation>单调增加.

由于<equation>f^{\prime}(x) > 0</equation>，故<equation>x _ {n + 1} - 1 = f \left(x _ {n}\right) - f (0) \frac {\text {拉 格 朗 日}}{\text {中 值 定 理}} f ^ {\prime} \left(\eta_ {n}\right) x _ {n} < f ^ {\prime} \left(\eta_ {n}\right) x _ {n + 1},</equation>其中<equation>\eta_{n}</equation>介于<equation>x_{n}</equation>与0之间，从而<equation>[1-f^{\prime}(\eta_{n})]x_{n+1} < 1.</equation>由<equation>0 < f^{\prime}(\eta_{n}) < \frac{1}{2}</equation>知，<equation>1-f^{\prime}(\eta_{n}) > \frac{1}{2} > 0.</equation>因此，<equation>x _ {n + 1} < \frac {1}{1 - f ^ {\prime} \left(\eta_ {n}\right)} < 2.</equation>综上所述，数列<equation>\{x_{n}\}</equation>单调增加且有上界.由单调有界准则知，<equation>\lim x_{n}</equation>存在.

若<equation>x_{1} > x_{2}</equation>，同理可证，数列<equation>\{x_{n}\}</equation>单调减少且有下界.由单调有界准则知，<equation>\lim x_{n}</equation>存在.

若<equation>x_{1} = x_{2}</equation>，则<equation>\forall n\in \mathbf{N}_{+},x_{n} = x_{1}</equation>，此时<equation>\lim_{n\to \infty}x_{n}</equation>显然存在.

再证明<equation>0 < \lim_{n\to \infty}x_{n} < 2.</equation>设<equation>\lim_{n\to \infty}x_{n} = a</equation>，对等式<equation>x_{n + 1} = f(x_n)</equation>两端令<equation>n\to \infty</equation>，由<equation>f(x)</equation>可导从而连续得到<equation>a = f(a).</equation>下面用两种方法证明<equation>0 < a < 2.</equation>（法一）由拉格朗日中值定理知，存在<equation>\xi</equation>介于a与0之间，使得<equation>f(a)-f(0)=f^{\prime}(\xi)a</equation>又<equation>f(a)=a</equation><equation>f(0)=1</equation>，故有<equation>a-1=f^{\prime}(\xi)a</equation>，解得<equation>a=\frac{1}{1-f^{\prime}(\xi)}.</equation>由题设知，<equation>0 < f^{\prime}(\xi) < \frac{1}{2}</equation>，于是<equation>\frac{1}{2} < 1-f^{\prime}(\xi) < 1</equation>，从而<equation>0 < 1 < a=\frac{1}{1-f^{\prime}(\xi)} < 2</equation>，结论得证.

（法二）令 F(x）=f(x）-x，则 F(a）=f(a）-a=0.又 f(x)可导且 0 < f'(x) <<equation>\frac{1}{2}</equation>，故<equation>F^{\prime}(x)=f^{\prime}(x)-1<0</equation>，从而 F(x)单调减少.因此要证 0 < a < 2，只需证明 F(0)>F(a)= 0 > F(2).

显然 F（0）=f（0）=1>0.又<equation>F (2) = f (2) - 2 = f (2) - f (0) - 1 \frac {\text {拉 格 朗 日}}{\text {中 值 定 理}} 2 f ^ {\prime} (\eta) - 1 < 0,</equation>其中<equation>0 < \eta < 2</equation>，故<equation>F(0) > F(a) = 0 > F(2)</equation>，结论得证.

---

**2014年第19题 | 解答题 | 10分**

19. (本题满分10分)

9. (本题满分10分)

设数列<equation>\{a_{n}\}</equation><equation>\{b_{n}\}</equation>满足<equation>0 < a_{n} < \frac{\pi}{2}, 0 < b_{n} < \frac{\pi}{2}, \cos a_{n}-a_{n}=\cos b_{n}</equation>，且级数<equation>\sum_{n=1}^{\infty} b_{n}</equation>收敛.

I. 证明<equation>\lim_{n\rightarrow \infty} a_{n}=0;</equation>II. 证明级数<equation>\sum_{n=1}^{\infty}\frac{a_{n}}{b_{n}}</equation>收敛.

**解析:**证（I）（法一）由于<equation>0 < a_{n} < \frac{\pi}{2}, 0 < b_{n} < \frac{\pi}{2}, \cos b_{n} = \cos a_{n} - a_{n} < \cos a_{n}</equation>，且<equation>\cos x</equation>在<equation>\left( 0, \frac{\pi}{2} \right)</equation>上单调减少，故<equation>0 < a_{n} < b_{n} < \frac{\pi}{2}.</equation>又级数<equation>\sum_{n=1}^{\infty} b_{n}</equation>收敛，故<equation>\lim_{n\to \infty}b_{n}=0</equation>，从而由夹逼准则知<equation>\lim_{n\to \infty}a_{n}=0</equation>，结论得证.

（法二）当<equation>x\in \left(0,\frac{\pi}{2}\right)</equation>时，<equation>\cos x > 1 - \frac{x^2}{2}</equation>，从而<equation>-\cos x < \frac{x^2}{2} -1.</equation>由于<equation>b_{n}\in \left(0,\frac{\pi}{2}\right)</equation>，故<equation>a _ {n} = \cos a _ {n} - \cos b _ {n} < 1 + \frac {b _ {n} ^ {2}}{2} - 1 = \frac {b _ {n} ^ {2}}{2},</equation>即<equation>0 < a_{n} < \frac{b_{n}^{2}}{2}</equation>. 又级数<equation>\sum_{n = 1}^{\infty}b_{n}</equation>收敛，故<equation>\lim_{n\to \infty}b_n = 0</equation>，从而由夹逼准则知<equation>\lim_{n\to \infty}a_n = 0</equation>，结论得证.

（Ⅱ）（法一）由（I）中法一知，<equation>0 < a_{n} < b_{n} < \frac{\pi}{2}</equation>从而<equation>\begin{aligned} \frac {a _ {n}}{b _ {n}} &= \frac {\cos a _ {n} - \cos b _ {n}}{b _ {n}} = \frac {2 \sin \frac {a _ {n} + b _ {n}}{2} \sin \frac {b _ {n} - a _ {n}}{2}}{b _ {n}} \\ < \frac {2 \cdot \frac {a _ {n} + b _ {n}}{2} \cdot \frac {b _ {n} - a _ {n}}{2}}{b _ {n}} \quad (x > 0 \text {时}, \sin x < x) \\ &= \frac {b _ {n} ^ {2} - a _ {n} ^ {2}}{2 b _ {n}} < \frac {b _ {n} ^ {2}}{2 b _ {n}} = \frac {1}{2} b _ {n}. \end{aligned}</equation>又<equation>\sum_{n = 1}^{\infty}b_{n}</equation>收敛，故由比较审敛法知，<equation>\sum_{n = 1}^{\infty}\frac{a_n}{b_n}</equation>收敛，结论得证.

（法二）由（I）中法一知，<equation>0 < a_{n} < b_{n} < \frac{\pi}{2}</equation>从而由拉格朗日中值定理知，存在<equation>\xi_{n}\in\left(a_{n},b_{n}\right)\subset\left(0,\frac{\pi}{2}\right)</equation>，使得<equation>\frac{a_{n}}{b_{n}}=\frac{\cos a_{n}-\cos b_{n}}{b_{n}}=\frac{-\sin \xi_{n}\cdot\left(a_{n}-b_{n}\right)}{b_{n}}=\frac{\sin \xi_{n}}{b_{n}}\left(b_{n}-a_{n}\right)<\frac{\sin \xi_{n}}{b_{n}}\cdot b_{n}=\sin \xi_{n}<\xi_{n}<b_{n}.</equation>又<equation>\sum_{n=1}^{\infty}b_{n}</equation>收敛，故由比较审敛法知，<equation>\sum_{n=1}^{\infty}\frac{a_{n}}{b_{n}}</equation>收敛，结论得证.

（法三）同（I）中法二得到<equation>0 < a_{n} < \frac{b_{n}^{2}}{2}</equation>，于是由<equation>b_{n} > 0</equation>知，<equation>0 < \frac{a_{n}}{b_{n}} < \frac{1}{2} b_{n}</equation>. 又<equation>\sum_{n = 1}^{\infty}b_{n}</equation>收敛，故由比较审敛法知<equation>\sum_{n = 1}^{\infty}\frac{a_n}{b_n}</equation>收敛，结论得证.

（法四）由（I）知，<equation>\lim_{n\to \infty}a_n = \lim_{n\to \infty}b_n = 0.</equation>又<equation>\cos b_{n} = \cos a_{n} - a_{n}</equation>，故<equation>\begin{aligned} \lim _ {n \rightarrow \infty} \frac {\frac {a _ {n}}{b _ {n}}}{b _ {n}} &= \lim _ {n \rightarrow \infty} \frac {a _ {n}}{b _ {n} ^ {2}} = \lim _ {n \rightarrow \infty} \left(\frac {1 - \cos b _ {n}}{b _ {n} ^ {2}} \cdot \frac {a _ {n}}{1 - \cos b _ {n}}\right) = \frac {1}{2} \lim _ {n \rightarrow \infty} \frac {a _ {n}}{1 - \cos b _ {n}} \\ &= \frac {1}{2} \lim _ {n \rightarrow \infty} \frac {a _ {n}}{1 - \left(\cos a _ {n} - a _ {n}\right)} = \frac {1}{2} \lim _ {n \rightarrow \infty} \frac {1}{\frac {1 - \cos a _ {n}}{a _ {n}} + 1} = \frac {1}{2}. \end{aligned}</equation>再由<equation>\sum_{n = 1}^{\infty}b_{n}</equation>收敛及比较审敛法的极限形式知，<equation>\sum_{n = 1}^{\infty}\frac{a_n}{b_n}</equation>收敛，结论得证.

---

**2009年第4题 | 选择题 | 4分 | 答案: C**

4. 设有两个数列<equation>\{a_{n}\} ,\{b_{n}\}</equation>，若<equation>\lim_{n\to\infty}a_{n}=0</equation>，则（    ）

A. 当<equation>\sum_{n=1}^{\infty}b_{n}</equation>收敛时，<equation>\sum_{n=1}^{\infty}a_{n}b_{n}</equation>收敛

C. 当<equation>\sum_{n=1}^{\infty} \left| b_{n} \right|</equation>收敛时，<equation>\sum_{n=1}^{\infty} a_{n}^{2} b_{n}^{2}</equation>收敛

B. 当<equation>\sum_{n=1}^{\infty}b_{n}</equation>发散时，<equation>\sum_{n=1}^{\infty}a_{n}b_{n}</equation>发散

D. 当<equation>\sum_{n=1}^{\infty}|\boldsymbol{b}_{n}|</equation>发散时，<equation>\sum_{n=1}^{\infty}a_{n}^{2}b_{n}^{2}</equation>发散

答案: C

**解析:**解 令<equation>a_{n}=\frac{(-1)^{n+1}}{\sqrt{n}}, b_{n}=\frac{(-1)^{n+1}}{\sqrt{n}}</equation>，则<equation>\lim_{n\to\infty}a_{n}=0</equation><equation>\sum_{n=1}^{\infty}b_{n}</equation>收敛，但<equation>\sum_{n=1}^{\infty}a_{n}b_{n}=\sum_{n=1}^{\infty}\frac{1}{n}</equation>发散.选项 A不正确.

令<equation>a_{n}=\frac{1}{n}, b_{n}=\frac{1}{n}</equation>，则<equation>\lim_{n\to\infty}a_{n}=0</equation><equation>\sum_{n=1}^{\infty}b_{n}</equation>发散，但<equation>\sum_{n=1}^{\infty}a_{n}b_{n}=\sum_{n=1}^{\infty}\frac{1}{n^{2}}</equation>收敛.选项B不正确.

令<equation>a_{n}=\frac{1}{n}, b_{n}=\frac{1}{n}</equation>，则<equation>\lim_{n\to\infty}a_{n}=0</equation><equation>\sum_{n=1}^{\infty}|\boldsymbol{b}_{n}|</equation>发散，但<equation>\sum_{n=1}^{\infty}a_{n}^{2}b_{n}^{2}=\sum_{n=1}^{\infty}\frac{1}{n^{4}}</equation>收敛.选项D不正确.

由排除法可知，应选C.

下面证明选项C正确.

由<equation>\sum_{n=1}^{\infty} \mid b_{n}\mid</equation>收敛知，<equation>\lim_{n\rightarrow \infty} \mid b_{n}\mid =0</equation>，于是存在<equation>N_{1}</equation>，使得当 n > N1时，<equation>\mid b_{n}\mid <1</equation>，从而<equation>b_{n}^{2}\leqslant \mid b_{n}\mid</equation>又<equation>\lim_{n\rightarrow \infty} a_{n}=0</equation>，故存在<equation>N_{2}</equation>，使得当 n > N2时，<equation>\mid a_{n}\mid <1</equation>，从而<equation>a_{n}^{2}<1</equation>.令 N =<equation>\max \{N_{1},N_{2}\}</equation>，则当 n > N时，<equation>0\leqslant a_{n}^{2}b_{n}^{2}\leqslant \mid b_{n}\mid</equation>，再由比较审敛法知，<equation>\sum_{n=1}^{\infty} a_{n}^{2}b_{n}^{2}</equation>收敛.

---


#### 傅里叶级数

**2025年第12题 | 填空题 | 5分**
12. 已知函数 f(x)<equation>\left\{\begin{array}{l l}0,&0 \leqslant x < \frac{1}{2}\\ x^{2},&\frac{1}{2} \leqslant x \leqslant 1\end{array} \right.</equation>，的傅里叶级数为<equation>\sum_{n=1}^{\infty} b_{n} \sin n \pi x</equation>，S(x)为<equation>\sum_{n=1}^{\infty} b_{n} \sin n \pi x</equation>的和函数，则<equation>S\left(-\frac{7}{2}\right)=</equation>
**解析: **解 由 S(x)为正弦级数的和函数可知，<equation>S ( x )</equation>为[0,1]上的 f(x)作奇延拓后再作周期为2的周期延拓所得函数的傅里叶级数.

由于 S（x）是周期为2的奇函数，故<equation>S \left(- \frac {7}{2}\right) = S \left(- 4 + \frac {1}{2}\right) = S \left(\frac {1}{2}\right).</equation>又因为<equation>x=\frac{1}{2}</equation>是<equation>f(x)</equation>的间断点，所以由狄利克雷收敛定理可得<equation>S \left(\frac {1}{2}\right) = \frac {1}{2} \left[ \lim _ {x \rightarrow \frac {1}{2} ^ {-}} f (x) + \lim _ {x \rightarrow \frac {1}{2} ^ {+}} f (x) \right] = \frac {1}{2} \left(0 + \frac {1}{4}\right) = \frac {1}{8}.</equation>因此，<equation>S\left(-\frac{7}{2}\right)=\frac{1}{8}.</equation>

---

**2024年第13题 | 填空题 | 5分**
13. 已知函数 f(x)=x+1，若 f(x)<equation>\frac{a_{0}}{2}+\sum_{n=1}^{\infty} a_{n} \cos n x,x \in[0,\pi]</equation>，则<equation>\lim_{n \to \infty} n^{2} \sin a_{2n-1}=</equation>___.
**答案: **\[ -\frac{1}{\pi} \]
**解析: **解 由于 f(x)的傅里叶级数展开式为余弦级数，故 f(x)为偶函数.由余弦级数的系数公式可知，当 n≥1时，<equation>\begin{aligned} a _ {n} &= \frac {2}{\pi} \int_ {0} ^ {\pi} (x + 1) \cos n x d x = \frac {2}{\pi} \left(\int_ {0} ^ {\pi} \cos n x d x + \int_ {0} ^ {\pi} x \cos n x d x\right) \\ &= \frac {2}{\pi} \left[ \frac {1}{n} \sin n x \Big | _ {0} ^ {\pi} + \frac {1}{n} \int_ {0} ^ {\pi} x d (\sin n x) \right] = \frac {2}{n \pi} \int_ {0} ^ {\pi} x d (\sin n x) \\ &= \frac {2}{n \pi} \left(x \sin n x \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} \sin n x d x\right) = - \frac {2}{n \pi} \int_ {0} ^ {\pi} \sin n x d x \\ &= \frac {2}{n \pi} \cdot \frac {\cos n x}{n} \Big | _ {0} ^ {\pi} = \frac {2}{n ^ {2} \pi} (\cos n \pi - 1) = \frac {2}{n ^ {2} \pi} [ (- 1) ^ {n} - 1 ]. \end{aligned}</equation>于是，<equation>a _ {2 n - 1} = \frac {2}{(2 n - 1) ^ {2} \pi} [ (- 1) ^ {2 n - 1} - 1 ] = \frac {2}{(2 n - 1) ^ {2} \pi} (- 1 - 1) = \frac {- 4}{(2 n - 1) ^ {2} \pi}.</equation>因此，<equation>\lim _ {n \rightarrow \infty} n ^ {2} \sin a _ {2 n - 1} = \lim _ {n \rightarrow \infty} n ^ {2} \sin \frac {- 4}{(2 n - 1) ^ {2} \pi} = \lim _ {n \rightarrow \infty} \frac {- 4 n ^ {2}}{(2 n - 1) ^ {2} \pi} = - \frac {1}{\pi}.</equation>

---

**2023年第13题 | 填空题 | 5分**
13. 设 f(x)为周期为2的周期函数，且 f(x)=1-x,x∈[0,1]，若 f(x)<equation>\frac{a_{0}}{2}+\sum_{n=1}^{\infty} a_{n} \cos n \pi x</equation>，则<equation>\sum_{n=1}^{\infty} a_{2n}=</equation>___.
**解析: **解 由于 f(x) 的傅里叶级数展开式为余弦级数，故 f(x)为偶函数.由余弦级数的系数计算公式可知，当 n≥1时，<equation>\begin{aligned} a _ {n} &= 2 \int_ {0} ^ {1} (1 - x) \cos n \pi x \mathrm {d} x = 2 \left(\int_ {0} ^ {1} \cos n \pi x \mathrm {d} x - \int_ {0} ^ {1} x \cos n \pi x \mathrm {d} x\right) \\ &= 2 \left[ \frac {1}{n \pi} \sin n \pi x \Big | _ {0} ^ {1} - \frac {1}{n \pi} \int_ {0} ^ {1} x \mathrm {d} (\sin n \pi x) \right] = - \frac {2}{n \pi} \int_ {0} ^ {1} x \mathrm {d} (\sin n \pi x) \\ &= - \frac {2}{n \pi} \left(x \sin n \pi x \Big | _ {0} ^ {1} - \int_ {0} ^ {1} \sin n \pi x \mathrm {d} x\right) = \frac {2}{n \pi} \int_ {0} ^ {1} \sin n \pi x \mathrm {d} x \\ &= \frac {2}{n \pi} \cdot \left(- \frac {\cos n \pi x}{n \pi}\right) \Big | _ {0} ^ {1} = \frac {- 2}{n ^ {2} \pi^ {2}} (\cos n \pi - 1). \end{aligned}</equation>于是，<equation>a _ {2 n} = \frac {- 2}{(2 n) ^ {2} \pi^ {2}} \left(\cos 2 n \pi - 1\right) = \frac {- 1}{2 n ^ {2} \pi^ {2}} (1 - 1) = 0.</equation>因此，<equation>\sum_{n=1}^{\infty} a_{2n}=0.</equation>

---

**2013年第3题 | 选择题 | 4分 | 答案: C**
3. 设<equation>f(x)=\left| x-\frac{1}{2}\right|, b_{n}=2\int_{0}^{1} f(x)\sin(n\pi x)\mathrm{d}x(n=1,2,\cdots).</equation>令<equation>S(x)=\sum_{n=1}^{\infty}b_{n}\sin(n\pi x),</equation>则<equation>S\left(-\frac{9}{4}\right)=</equation>(    )

A.<equation>\frac{3}{4}</equation>B.<equation>\frac{1}{4}</equation>C.<equation>-\frac{1}{4}</equation>D.<equation>-\frac{3}{4}</equation>
答案: C
**解析: **解设<equation>F ( x )</equation>是以2为周期的奇函数，且当<equation>- 1 \leqslant x \leqslant 1</equation>时，<equation>F (x) = \left\{ \begin{array}{l l} f (x), & 0 < x < 1, \\ - f (- x), & - 1 < x < 0, \\ 0, & x = 0, \pm 1. \end{array} \right.</equation>如右图所示，<equation>F ( x )</equation>的傅里叶系数为<equation>\widetilde {a} _ {n} = \int_ {- 1} ^ {1} F (x) \cos n \pi x \mathrm {d} x = 0, n = 0, 1, 2, \dots ,</equation>

---


#### 幂级数的和函数及幂级数展开式

**2024年第3题 | 选择题 | 5分 | 答案: A**
3. 已知幂级数<equation>\sum_{n=0}^{\infty} a_{n} x^{n}</equation>的和函数为<equation>\ln(2+x)</equation>，则<equation>\sum_{n=0}^{\infty} n a_{2n}=</equation>(    )

A.<equation>-\frac{1}{6}</equation>B.<equation>-\frac{1}{3}</equation>C.<equation>\frac{1}{6}</equation>D.<equation>\frac{1}{3}</equation>
答案: A
**解析: **解（法一）由<equation>\ln(1+x)=\sum_{n=1}^{\infty}(-1)^{n-1}\frac{x^{n}}{n}(-1<x\leqslant 1)</equation>可得<equation>\ln (2 + x) = \ln \left[ 2 \cdot \left(1 + \frac {x}{2}\right) \right] = \ln 2 + \ln \left(1 + \frac {x}{2}\right) = \ln 2 + \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1}}{n} \left(\frac {x}{2}\right) ^ {n}.</equation>由此可得，当<equation>n > 0</equation>时，<equation>x^{2n}</equation>的系数为<equation>a_{2n} = \frac{(-1)^{2n - 1}}{2n2^{2n}} = \frac{-1}{2n2^{2n}}.</equation>因此，<equation>\sum_ {n = 0} ^ {\infty} n a _ {2 n} = \sum_ {n = 1} ^ {\infty} n a _ {2 n} = \sum_ {n = 1} ^ {\infty} \frac {- n}{2 n 2 ^ {2 n}} = \sum_ {n = 1} ^ {\infty} \frac {- 1}{2 ^ {2 n + 1}} = \frac {- \frac {1}{8}}{1 - \frac {1}{4}} = - \frac {1}{6}.</equation>应选 A.

（法二）由<equation>\sum_{n = 0}^{\infty}a_nx^n = \ln (2 + x)</equation>可得<equation>\sum_{n = 0}^{\infty}a_n(-x)^n = \sum_{n = 0}^{\infty}(-1)^n a_nx^n = \ln (2 - x)</equation>.由此可得<equation>\sum_{n = 0}^{\infty}[1 + (-1)^n]a_nx^n = \ln (2 + x) + \ln (2 - x)</equation>，即<equation>2 \sum_ {n = 0} ^ {\infty} a _ {2 n} x ^ {2 n} = \ln (2 + x) + \ln (2 - x).</equation>对（1）式两端关于<equation>x</equation>求导可得，<equation>4 \sum_ {n = 1} ^ {\infty} n a _ {2 n} x ^ {2 n - 1} = \frac {1}{2 + x} - \frac {1}{2 - x}.</equation>在(2)式中令<equation>x = 1</equation>，可得<equation>4\sum_{n = 1}^{\infty}na_{2n} = \frac{1}{3} -1 = -\frac{2}{3}</equation>，进一步可得<equation>\sum_{n = 0}^{\infty}na_{2n} = -\frac{1}{6}</equation>因此，应选A.

（法三）注意到<equation>\left[ \ln (2 + x) \right] ^ {\prime} = \frac {1}{2 + x} = \frac {1}{2 \left(1 + \frac {x}{2}\right)} = \frac {1}{2} \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} \left(\frac {x}{2}\right) ^ {n},</equation>该幂级数的收敛半径为2，故在（-2，2）上，由牛顿一莱布尼茨公式可得<equation>\begin{aligned} \ln (2 + x) - \ln 2 &= \int_ {0} ^ {x} \left[ \ln (2 + t) \right] ^ {\prime} \mathrm {d} t = \int_ {0} ^ {x} \frac {1}{2} \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} \left(\frac {t}{2}\right) ^ {n} \mathrm {d} t \\ \frac {\text {逐 项 积 分}}{} \frac {1}{2} \sum_ {n = 0} ^ {\infty} \int_ {0} ^ {x} (- 1) ^ {n} \left(\frac {t}{2}\right) ^ {n} \mathrm {d} t &= \frac {1}{2} \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{n + 1} \cdot \frac {x ^ {n + 1}}{2 ^ {n}} \\ &= \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1} x ^ {n}}{n 2 ^ {n}}. \end{aligned}</equation>因此，<equation>\ln (2 + x) = \ln 2 + \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1} x ^ {n}}{n 2 ^ {n}}.</equation>其余同法一.

---

**2021年第18题 | 解答题 | 12分**
18. (本题满分12分)

设<equation>u_{n}(x)=\mathrm{e}^{-nx}+\frac{x^{n+1}}{n(n+1)}</equation>（<equation>n=1,2,\cdots</equation>），求级数<equation>\sum_{n=1}^{\infty}u_{n}(x)</equation>的收敛域及和函数.
**答案: **收敛域为（0，1]，和函数 s（x）=<equation>\left\{\begin{array}{l l} \frac{1}{e^{x}-1}+(1-x)\ln(1-x)+x,&x\in(0,1),\\ \frac{1}{e-1}+1,&x=1. \end{array} \right.</equation>
**解析: **解记<equation>s ( x )=\sum_{n=1}^{\infty} u_{n} ( x ).</equation>记<equation>s_{1}(x)=\sum_{n=1}^{\infty}\mathrm{e}^{-nx}.</equation>当<equation>|\mathrm{e}^{-x}|<1</equation>即<equation>x>0</equation>时，由几何级数的求和公式可得<equation>s_{1}(x)=\frac{\mathrm{e}^{-x}}{1-\mathrm{e}^{-x}}=\frac{1}{\mathrm{e}^{x}-1}</equation>该级数收敛.<equation>s_{1}(x)</equation>的收敛域为（0，<equation>+\infty).</equation>记<equation>s_{2}(x) = \sum_{n = 1}^{\infty}\frac{x^{n + 1}}{n(n + 1)}</equation>，其系数<equation>a_{n} = \frac{1}{n(n + 1)}</equation><equation>\lim _ {n \rightarrow \infty} \left| \frac {a _ {n + 1}}{a _ {n}} \right| = \lim _ {n \rightarrow \infty} \frac {n (n + 1)}{(n + 1) (n + 2)} = 1.</equation>于是，<equation>s_{2}(x)</equation>的收敛半径为1，收敛区间为<equation>(-1,1).</equation><equation>s_{2}(x)</equation>在<equation>x=-1</equation>处为<equation>\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n(n+1)}</equation>由莱布尼茨定理可知该级数收敛.<equation>s_{2}(x)</equation>在<equation>x=1</equation>处为<equation>\sum_{n=1}^{\infty}\frac{1}{n(n+1)}</equation>由极限审敛法可知该级数收敛.因此，<equation>s_{2}(x)</equation>的收敛域为<equation>[-1,1].</equation>取<equation>(0, + \infty)</equation>与<equation>[-1,1]</equation>的交集，可得<equation>(0,1]</equation>为<equation>s(x)</equation>的收敛域.

下面用两种方法计算<equation>s_{2}(x).</equation>（法一）整理<equation>s_{2}(x).</equation>当 x<equation>\in</equation>（0,1）时，<equation>\begin{aligned} s _ {2} (x) &= \sum_ {n = 1} ^ {\infty} \left(\frac {x ^ {n + 1}}{n} - \frac {x ^ {n + 1}}{n + 1}\right) = x \sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n} - \sum_ {n = 1} ^ {\infty} \frac {x ^ {n + 1}}{n + 1} = x \sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n} - \sum_ {n = 2} ^ {\infty} \frac {x ^ {n}}{n} \\ &= (x - 1) \sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n} + x. \end{aligned}</equation>记<equation>t(x) = \sum_{n = 1}^{\infty}\frac{x^n}{n}</equation>，则<equation>s_2(x) = (x - 1)t(x) + x.</equation><equation>t ^ {\prime} (x) = \left(\sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n}\right) ^ {\prime} \stackrel {\text {逐 项 求 导}} {=} \sum_ {n = 1} ^ {\infty} \left(\frac {x ^ {n}}{n}\right) ^ {\prime} = \sum_ {n = 1} ^ {\infty} x ^ {n - 1} = \frac {1}{1 - x}.</equation>注意到 t（0）=0，故<equation>t (x) = t (x) - t (0) = \int_ {0} ^ {x} \frac {1}{1 - t} \mathrm {d} t = - \ln (1 - x).</equation>因此，当<equation>x\in(0,1)</equation>时，<equation>s _ {2} (x) = (1 - x) \ln (1 - x) + x.</equation>当<equation>x = 1</equation>时，<equation>s_{2}(1) = \sum_{n = 1}^{\infty}\frac{1}{n(n + 1)}</equation>.

计算<equation>\sum_{n=1}^{\infty} \frac{1}{n(n+1)}</equation>的部分和<equation>\sum_{n=1}^{k} \frac{1}{n(n+1)}</equation>得<equation>s (x) = \left\{ \begin{array}{l l} \frac {1}{\mathrm {e} ^ {x} - 1} + (1 - x) \ln (1 - x) + x, & x \in (0, 1), \\ \frac {\mathrm {e}}{\mathrm {e} - 1}, & x = 1. \end{array} \right.</equation>（法二）当<equation>x\in (0,1)</equation>时，<equation>s _ {2} ^ {\prime} (x) = \left[ \sum_ {n = 1} ^ {\infty} \frac {x ^ {n + 1}}{n (n + 1)} \right] ^ {\prime} \xlongequal {\text {逐 项 求 导}} \sum_ {n = 1} ^ {\infty} \left[ \frac {x ^ {n + 1}}{n (n + 1)} \right] ^ {\prime} = \sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n}.</equation><equation>s _ {2} ^ {\prime \prime} (x) = \left(\sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n}\right) ^ {\prime} \stackrel {\text {逐 项 求 导}} {=} \sum_ {n = 1} ^ {\infty} \left(\frac {x ^ {n}}{n}\right) ^ {\prime} = \sum_ {n = 1} ^ {\infty} x ^ {n - 1} = \frac {1}{1 - x}.</equation>注意到<equation>s_{2}^{\prime}(0)=0</equation>，故<equation>s _ {2} ^ {\prime} (x) = s _ {2} ^ {\prime} (x) - s _ {2} ^ {\prime} (0) = \int_ {0} ^ {x} \frac {1}{1 - t} \mathrm {d} t = - \ln (1 - t) \Big | _ {0} ^ {x} = - \ln (1 - x).</equation>又因为<equation>s_{2}(0)=0</equation>，所以<equation>\begin{aligned} s _ {2} (x) &= s _ {2} (x) - s _ {2} (0) = \int_ {0} ^ {x} \left[ - \ln (1 - t) \right] \mathrm {d} t = - \left[ t \ln (1 - t) \left| _ {0} ^ {x} - \int_ {0} ^ {x} \frac {- t}{1 - t} \mathrm {d} t \right. \right] \\ &= - x \ln (1 - x) - \int_ {0} ^ {x} \frac {t}{1 - t} \mathrm {d} t = - x \ln (1 - x) - \int_ {0} ^ {x} \left(- 1 + \frac {1}{1 - t}\right) \mathrm {d} t \\ &= - x \ln (1 - x) - \left[ - t - \ln (1 - t) \right] \left| _ {0} ^ {x} = - x \ln (1 - x) + \left[ t + \ln (1 - t) \right] \right| _ {0} ^ {x} \\ &= - x \ln (1 - x) + x + \ln (1 - x) = (1 - x) \ln (1 - x) + x. \end{aligned}</equation>其余同法一.

---

**2020年第17题 | 解答题 | 10分**
17. (本题满分10分)

设数列<equation>\{a_{n}\}</equation>满足：<equation>a_{1}=1,(n+1)a_{n+1}=\left(n+\frac{1}{2}\right)a_{n}</equation>，证明：当<equation>|x|<1</equation>时，幂级数<equation>\sum_{n=1}^{\infty}a_{n}x^{n}</equation>收敛，并求其和函数.
**答案: **证明略，和函数为<equation>S ( x )=\frac{2}{\sqrt{1-x}}-2, x \in(-1,1).</equation>
**解析: **解 计算幂级数的收敛半径 R.由<equation>(n + 1)a_{n + 1} = \left(n + \frac{1}{2}\right)a_n</equation>可得，<equation>\frac{a_n}{a_{n + 1}} = \frac{n + 1}{n + \frac{1}{2}}.</equation><equation>R = \lim _ {n \rightarrow \infty} \left| \frac {a _ {n}}{a _ {n + 1}} \right| = \lim _ {n \rightarrow \infty} \frac {n + 1}{n + \frac {1}{2}} = 1.</equation>因此，幂级数的收敛半径<equation>R=1</equation>当<equation>|x| < 1</equation>时，幂级数<equation>\sum_{n=1}^{\infty} a_{n} x^{n}</equation>收敛下面用两种方法计算和函数<equation>S(x).</equation>（法一）令<equation>S ( x )=\sum_{n=1}^{\infty} a_{n} x^{n}, x\in(-1,1),</equation>，则<equation>\begin{aligned} S ^ {\prime} (x) &= \left(\sum_ {n = 1} ^ {\infty} a _ {n} x ^ {n}\right) ^ {\prime} \xlongequal {\text {逐 项 求 导}} \sum_ {n = 1} ^ {\infty} \left(a _ {n} x ^ {n}\right) ^ {\prime} = \sum_ {n = 1} ^ {\infty} a _ {n} n x ^ {n - 1} = \sum_ {n = 0} ^ {\infty} a _ {n + 1} (n + 1) x ^ {n} \\ &= 1 + \sum_ {n = 1} ^ {\infty} (n + 1) a _ {n + 1} x ^ {n} \xlongequal {(n + 1) a _ {n + 1} = \left(n + \frac {1}{2}\right) a _ {n}} 1 + \sum_ {n = 1} ^ {\infty} \left(n + \frac {1}{2}\right) a _ {n} x ^ {n} \\ &= 1 + x \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n - 1} + \frac {1}{2} \sum_ {n = 1} ^ {\infty} a _ {n} x ^ {n} = 1 + x S ^ {\prime} (x) + \frac {1}{2} S (x). \end{aligned}</equation>于是，<equation>S ( x )</equation>满足微分方程<equation>y^{\prime}=1+xy^{\prime}+\frac{1}{2} y</equation>即<equation>( 1-x)y^{\prime}-\frac{1}{2} y=1.</equation>整理可得<equation>y^{\prime}-\frac{1}{2(1-x)}y</equation><equation>= \frac{1}{1 - x}.</equation>这是一个一阶非齐次线性微分方程.由求解公式可得<equation>\begin{aligned} S (x) &= \mathrm {e} ^ {\int \frac {1}{2 (1 - x)} \mathrm {d} x} \left[ \int \frac {1}{1 - x} \cdot \mathrm {e} ^ {\int \frac {1}{2 (x - 1)} \mathrm {d} x} \mathrm {d} x + C \right] \xlongequal {\mid x - 1 \mid = 1 - x} \mathrm {e} ^ {- \frac {1}{2} \ln (1 - x)} \left[ \int \frac {1}{1 - x} \cdot \mathrm {e} ^ {\frac {1}{2} \ln (1 - x)} \mathrm {d} x + C \right] \\ &= \frac {1}{\sqrt {1 - x}} \left(\int \frac {1}{1 - x} \cdot \sqrt {1 - x} \mathrm {d} x + C\right) = \frac {1}{\sqrt {1 - x}} \left(\int \frac {1}{\sqrt {1 - x}} \mathrm {d} x + C\right) \\ &= \frac {1}{\sqrt {1 - x}} (- 2 \sqrt {1 - x} + C) = \frac {C}{\sqrt {1 - x}} - 2, \end{aligned}</equation>其中 C为待定常数.

当<equation>x = 0</equation>时，<equation>S(0) = 0</equation>，故<equation>0 = \frac{C}{1} -2.</equation>解得<equation>C = 2.</equation>因此，<equation>S ( x ) = \frac { 2 } { \sqrt { 1 - x } } - 2 , x \in (- 1, 1 ) .</equation>（法二）由<equation>(n + 1)a_{n + 1} = \left(n + \frac{1}{2}\right)a_n</equation>可得<equation>\frac{a_{n + 1}}{a_n} = \frac{n + \frac{1}{2}}{n + 1} = \frac{2(n + 1) - 1}{2(n + 1)}</equation>，且<equation>a_2 = \frac{3}{4}</equation>. 于是，<equation>a _ {n} = \frac {a _ {n}}{a _ {n - 1}} \cdot \frac {a _ {n - 1}}{a _ {n - 2}} \dots \frac {a _ {2}}{a _ {1}} = \frac {2 n - 1}{2 n} \cdot \frac {2 n - 3}{2 n - 2} \dots \frac {3}{4} = 2 \cdot \frac {(2 n - 1) ! !}{(2 n) ! !}.</equation>记<equation>S(x) = \sum_{n = 1}^{\infty} a_n x^n, x \in (-1, 1)</equation>，则<equation>S(x) = 2\sum_{n = 1}^{\infty} \frac{(2n - 1)!!}{(2n)!!} x^n.</equation><equation>\begin{aligned} S ^ {\prime} (x) &= \sum_ {n = 1} ^ {\infty} \frac {(2 n - 1) ! !}{(2 n) ! !} \cdot 2 n x ^ {n - 1} = \sum_ {n = 1} ^ {\infty} \frac {(2 n - 1) ! !}{(2 n - 2) ! !} x ^ {n - 1} = \sum_ {n = 0} ^ {\infty} \frac {(2 n + 1) ! !}{(2 n) ! !} x ^ {n} \\ &= 1 + \sum_ {n = 1} ^ {\infty} \frac {(2 n + 1) ! !}{(2 n) ! !} x ^ {n} = 1 + \sum_ {n = 1} ^ {\infty} \frac {(2 n - 1) ! ! \cdot (2 n + 1)}{(2 n) ! !} x ^ {n} \\ &= 1 + \sum_ {n = 1} ^ {\infty} \frac {(2 n - 1) ! !}{(2 n) ! !} \cdot 2 n x ^ {n} + \sum_ {n = 1} ^ {\infty} \frac {(2 n - 1) ! !}{(2 n) ! !} x ^ {n} \\ &= 1 + x \sum_ {n = 1} ^ {\infty} \frac {(2 n - 1) ! !}{(2 n - 2) ! !} x ^ {n - 1} + \frac {1}{2} S (x) = 1 + x S ^ {\prime} (x) + \frac {1}{2} S (x). \end{aligned}</equation>其余同法一.

---

**2019年第11题 | 填空题 | 4分**
11. 幂级数<equation>\sum_{n=0}^{\infty} \frac{(-1)^{n}}{(2 n)!} x^{n}</equation>在<equation>(0,+\infty)</equation>内的和函数<equation>S(x)=</equation>___
**答案: **cos<equation>\sqrt{x}.</equation>
**解析: **解 由于<equation>\sum_{n=0}^{\infty} \frac{(-1)^{n}}{(2n)!} x^{n}=\sum_{n=0}^{\infty} \frac{(-1)^{n}}{(2n)!} (\sqrt{x})^{2n}</equation>，而<equation>\cos x</equation>的幂级数展开式为<equation>\cos x=\sum_{n=0}^{\infty} \frac{(-1)^{n}}{(2n)!} x^{2n}(-\infty < x < +\infty)</equation>，故幂级数<equation>\sum_{n=0}^{\infty} \frac{(-1)^{n}}{(2n)!} x^{n}</equation>在（0，<equation>+\infty</equation>）内的和函数<equation>S(x)=\cos \sqrt{x}.</equation>

---

**2018年第3题 | 选择题 | 4分 | 答案: B**
3.<equation>\sum_{n=0}^{\infty}(-1)^{n}\frac{2n+3}{(2n+1)!}=</equation>(    )

A.<equation>\sin 1+\cos 1</equation>B.<equation>2\sin 1+\cos 1</equation>C.<equation>2\sin 1+2\cos 1</equation>D.<equation>2\sin 1+3\cos 1</equation>
答案: B
**解析: **解 由于在<equation>(-\infty, +\infty)</equation>上，<equation>\sin x=\sum_{n=0}^{\infty}\frac{(-1)^{n}}{(2n+1)!}x^{2n+1},\cos x=\sum_{n=0}^{\infty}\frac{(-1)^{n}}{(2n)!}x^{2n}</equation>，故<equation>\sin 1=\sum_{n=0}^{\infty}\frac{(-1)^{n}}{(2n+1)!},\cos 1=\sum_{n=0}^{\infty}\frac{(-1)^{n}}{(2n)!}.</equation>因此，<equation>\sum_{n=0}^{\infty}(-1)^{n}\frac{2n+3}{(2n+1)!}=\sum_{n=0}^{\infty}(-1)^{n}\frac{2+2n+1}{(2n+1)!}=2\sum_{n=0}^{\infty}\frac{(-1)^{n}}{(2n+1)!}+\sum_{n=0}^{\infty}\frac{(-1)^{n}}{(2n)!}</equation><equation>= 2\sin 1+\cos 1.</equation>应选B.

---

**2017年第12题 | 填空题 | 4分**
12. 幂级数<equation>\sum_{n=1}^{\infty} (-1)^{n-1} nx^{n-1}</equation>在区间<equation>(-1, 1)</equation>内的和函数<equation>S(x) =</equation>___
**答案: **<equation>\frac {1}{(1 + x) ^ {2}}.</equation>
**解析: **解幂级数<equation>\sum_{n=1}^{\infty}(-1)^{n-1} n x^{n-1}</equation>的收敛域为<equation>(-1,1).</equation>当<equation>-1 < x < 1</equation>时，<equation>\int_{0}^{x} S(t)\mathrm{d} t=\int_{0}^{x}\sum_{n=1}^{\infty}(-1)^{n-1} n t^{n-1}\mathrm{d} t=\sum_{n=1}^{\infty}\int_{0}^{x}(-1)^{n-1} n t^{n-1}\mathrm{d} t=\sum_{n=1}^{\infty}(-1)^{n-1} x^{n}=\frac{x}{1+x},</equation>从而<equation>S(x)=\left(\frac{x}{1+x}\right)^{\prime}=\frac{1}{(1+x)^{2}}.</equation>

---

**2013年第16题 | 解答题 | 10分**
16. (本题满分10分)

设数列<equation>\{a_{n}\}</equation>满足条件：<equation>a_{0}=3,a_{1}=1,a_{n-2}-n(n-1)a_{n}=0(n\geqslant2),S(x)</equation>是幂级数<equation>\sum_{n=0}^{\infty}a_{n}x^{n}</equation>的和函数.

I. 证明<equation>S^{\prime\prime}(x)-S(x)=0;</equation>II. 求 S(x)的表达式.
**答案: **(16) （I）证明略；

（Ⅱ）<equation>S ( x )=2 \mathrm{e}^{x}+\mathrm{e}^{-x}.</equation>
**解析: **解（I）由题设知，<equation>a_{n}=\frac{1}{n(n-1)}a_{n-2}, n\geqslant 2</equation>递推得到<equation>a _ {2 n} = \frac {1}{(2 n) !} a _ {0} = \frac {3}{(2 n) !}, \quad a _ {2 n + 1} = \frac {1}{(2 n + 1) !} a _ {1} = \frac {1}{(2 n + 1) !}, \quad n = 0, 1, 2, \dots .</equation>当<equation>n = 2m,m\in \mathbf{N}</equation>时，<equation>\frac{a_{n + 1}}{a_n} = \frac{a_{2m + 1}}{a_{2m}} = \frac{1}{3(2m + 1)} = \frac{1}{3(n + 1)}</equation>；

当<equation>n = 2m + 1,m\in \mathbf{N}</equation>时，<equation>\frac{a_{n+1}}{a_n}=\frac{a_{2m+2}}{a_{2m+1}}=\frac{3}{2m+2}=\frac{3}{n+1}.</equation>因此<equation>\lim_{n\to \infty}\frac{a_{n + 1}}{a_n} = 0</equation>，从而<equation>\sum_{n = 0}^{\infty}a_nx^n</equation>的收敛半径为<equation>+\infty</equation>. 于是在<equation>(-\infty , + \infty)</equation>上可对<equation>\sum_{n = 0}^{\infty}a_nx^n</equation>逐项求导，即<equation>S ^ {\prime} (x) = \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n - 1},</equation><equation>S ^ {\prime \prime} (x) = \sum_ {n = 2} ^ {\infty} n (n - 1) a _ {n} x ^ {n - 2} = \sum_ {n = 0} ^ {\infty} (n + 2) (n + 1) a _ {n + 2} x ^ {n}.</equation>由<equation>a_{n - 2} - n(n - 1)a_n = 0(n\geqslant 2)</equation>知，<equation>a_{n} - (n + 2)(n + 1)a_{n + 2} = 0(n\in \mathbf{N})</equation>，从而<equation>\begin{aligned} S ^ {\prime \prime} (x) - S (x) &= \sum_ {n = 0} ^ {\infty} (n + 2) (n + 1) a _ {n + 2} x ^ {n} - \sum_ {n = 0} ^ {\infty} a _ {n} x ^ {n} \\ &= \sum_ {n = 0} ^ {\infty} \left[ (n + 2) (n + 1) a _ {n + 2} - a _ {n} \right] x ^ {n} = 0. \end{aligned}</equation>结论得证.

（Ⅱ）二阶常系数齐次线性微分方程<equation>S^{\prime \prime}(x)-S(x)=0</equation>的特征方程为<equation>\lambda^{2}-1=0</equation>，解得<equation>\lambda=\pm1</equation>从而<equation>S (x) = C _ {1} \mathrm {e} ^ {x} + C _ {2} \mathrm {e} ^ {- x}, \quad C _ {1}, C _ {2} \text {为待定常数}.</equation>将<equation>S (0)=a_{0}=3,S^{\prime}(0)=a_{1}=1</equation>代入上式，得到<equation>C_{1}+C_{2}=3,C_{1}-C_{2}=1</equation>解得<equation>C_{1}=2,C_{2}=1.</equation>因此<equation>S (x) = 2 \mathrm {e} ^ {x} + \mathrm {e} ^ {- x}.</equation>

---

**2012年第17题 | 解答题 | 10分**
17. (本题满分10分)

求幂级数<equation>\sum_ {n = 0} ^ {\infty} \frac {4 n ^ {2} + 4 n + 3}{2 n + 1} x ^ {2}</equation>的收敛域及和函数.
**答案: **(17) 收敛域为（-1，1），和函数为<equation>S(x) = \left\{\begin{array}{ll}\frac{1+x^{2}}{(1-x^{2})^{2}}+\frac{1}{x}\ln\frac{1+x}{1-x}, & -1<x<1 \text{且} x\neq 0, \\ 3, & x=0.\end{array}\right.</equation>
**解析: **解 令<equation>u_{n}(x)=\frac{4 n^{2}+4 n+3}{2 n+1} x^{2 n}</equation>，则<equation>u_{n+1}(x)=\frac{4(n+1)^{2}+4(n+1)+3}{2(n+1)+1} x^{2(n+1)}</equation>，从而<equation>\lim_{n\to \infty}\left| \frac{u_{n+1}(x)}{u_{n}(x)} \right|=x^{2}.</equation>由比值审敛法知，当<equation>|x| < 1</equation>时，原幂级数收敛；当<equation>|x| > 1</equation>时，原幂级数发散，从而收敛半径为1.

当<equation>x=\pm 1</equation>时，<equation>\sum_{n=0}^{\infty}\frac{4n^{2}+4n+3}{2n+1}x^{2n}=\sum_{n=0}^{\infty}\frac{4n^{2}+4n+3}{2n+1}.</equation>又<equation>\lim_{n\to\infty}\frac{4n^{2}+4n+3}{2n+1}=\infty\neq0</equation>，故原幂级数发散.

综上所述，幂级数<equation>\sum_{n=0}^{\infty} \frac{4 n^{2}+4 n+3}{2 n+1} x^{2 n}</equation>的收敛域为（-1，1）.

令<equation>S ( x )=\sum_{n=0}^{\infty}\frac{4 n^{2}+4 n+3}{2 n+1} x^{2 n}(-1<x<1)</equation>，则<equation>S (x) = \sum_ {n = 0} ^ {\infty} \frac {\left(2 n + 1\right) ^ {2} + 2}{2 n + 1} x ^ {2 n} = \sum_ {n = 0} ^ {\infty} (2 n + 1) x ^ {2 n} + \sum_ {n = 0} ^ {\infty} \frac {2}{2 n + 1} x ^ {2 n}.</equation>当<equation>- 1 < x < 1</equation>时，<equation>\sum_ {n = 0} ^ {\infty} (2 n + 1) x ^ {2 n} = \sum_ {n = 0} ^ {\infty} \left(x ^ {2 n + 1}\right) ^ {\prime} = \left(\sum_ {n = 0} ^ {\infty} x ^ {2 n + 1}\right) ^ {\prime} = \left(\frac {x}{1 - x ^ {2}}\right) ^ {\prime} = \frac {1 + x ^ {2}}{\left(1 - x ^ {2}\right) ^ {2}}.</equation>当<equation>- 1 < x < 1</equation>且<equation>x\neq 0</equation>时，<equation>\sum_ {n = 0} ^ {\infty} \frac {2}{2 n + 1} x ^ {2 n} = \frac {2}{x} \sum_ {n = 0} ^ {\infty} \frac {1}{2 n + 1} x ^ {2 n + 1}.</equation>注意这里 x要作分母，故需分情况 x≠0与 x=0来讨论.

又<equation>\left(\sum_{n = 0}^{\infty}\frac{1}{2n + 1} x^{2n + 1}\right)^{\prime} = \sum_{n = 0}^{\infty}\left(\frac{1}{2n + 1} x^{2n + 1}\right)^{\prime} = \sum_{n = 0}^{\infty}x^{2n} = \frac{1}{1 - x^2}</equation>，故<equation>\sum_ {n = 0} ^ {\infty} \frac {1}{2 n + 1} x ^ {2 n + 1} = \int_ {0} ^ {x} \frac {1}{1 - t ^ {2}} \mathrm {d} t = \frac {1}{2} \ln \frac {1 + x}{1 - x}.</equation>从而<equation>\sum_ {n = 0} ^ {\infty} \frac {2}{2 n + 1} x ^ {2 n} = \frac {1}{x} \ln \frac {1 + x}{1 - x}, - 1 < x < 1 \text {且} x \neq 0.</equation>当<equation>x = 0</equation>时，<equation>\sum_{n = 0}^{\infty}\frac{2}{2n + 1} x^{2n} = 2,\sum_{n = 0}^{\infty}(2n + 1)x^{2n} = 1</equation>，故<equation>S(0) = 3.</equation>综上所述，<equation>S(x) = \left\{ \begin{array}{ll} \frac{1 + x^{2}}{(1 - x^{2})^{2}} + \frac{1}{x} \ln \frac{1 + x}{1 - x}, & -1 < x < 1 \text{且} x \neq 0, \\ 3, & x = 0. \end{array}\right.</equation>

---

**2010年第18题 | 解答题 | 10分**
18. (本题满分10分）

求幂级数<equation>\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{2 n-1} x^{2 n}</equation>的收敛域及和函数.
**答案: **(18) 收敛域为<equation>[-1,1]</equation>，和函数为<equation>x\arctan x(-1\leqslant x\leqslant 1)</equation>
**解析: **解 令<equation>u_{n}(x) = \frac{(-1)^{n - 1}}{2n - 1} x^{2n}</equation>，则<equation>\lim _ {n \rightarrow \infty} \left| \frac {u _ {n + 1} (x)}{u _ {n} (x)} \right| = \lim _ {n \rightarrow \infty} \left| \frac {\frac {(- 1) ^ {n}}{2 n + 1} x ^ {2 n + 2}}{\frac {(- 1) ^ {n - 1}}{2 n - 1} x ^ {2 n}} \right| = \lim _ {n \rightarrow \infty} \left| \frac {2 n - 1}{2 n + 1} x ^ {2} \right| = x ^ {2}.</equation>由比值审敛法可知，当<equation>|x| < 1</equation>时，<equation>\sum_{n = 1}^{\infty}u_n(x)</equation>收敛；当<equation>|x| > 1</equation>时，<equation>\sum_{n = 1}^{\infty}u_n(x)</equation>发散，于是<equation>\sum_{n = 1}^{\infty}u_n(x)</equation>的收敛半径为1.又当<equation>x = \pm 1</equation>时，由莱布尼茨定理知，<equation>\sum_{n = 1}^{\infty}u_n(\pm 1) = \sum_{n = 1}^{\infty}\frac{(-1)^{n - 1}}{2n - 1}</equation>收敛.因此幂级数<equation>\sum_{n = 1}^{\infty}\frac{(-1)^{n - 1}}{2n - 1} x^{2n}</equation>的收敛域为<equation>[-1,1]</equation>令<equation>S(x) = \sum_{n = 1}^{\infty}\frac{(-1)^{n - 1}}{2n - 1} x^{2n}, S_{1}(x) = \sum_{n = 1}^{\infty}\frac{(-1)^{n - 1}}{2n - 1} x^{2n - 1}, -1\leqslant x\leqslant 1</equation>，则<equation>S(x) = xS_{1}(x)</equation>下面用两种方法求<equation>S_{1}(x)</equation>（法一）由<equation>\arctan x</equation>的麦克劳林展开式知，<equation>S _ {1} (x) = \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1}}{2 n - 1} x ^ {2 n - 1} = \arctan x, - 1 \leqslant x \leqslant 1.</equation>（法二）当<equation>- 1 < x < 1</equation>时，<equation>\begin{aligned} S _ {1} ^ {\prime} (x) &= \left[ \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1}}{2 n - 1} x ^ {2 n - 1} \right] ^ {\prime} = \sum_ {n = 1} ^ {\infty} \left[ \frac {(- 1) ^ {n - 1}}{2 n - 1} x ^ {2 n - 1} \right] ^ {\prime} \\ &= \sum_ {n = 1} ^ {\infty} (- 1) ^ {n - 1} x ^ {2 n - 2} = \frac {1}{1 + x ^ {2}}. \end{aligned}</equation>注意逐项求导后所得幂级数的收敛半径不变，但在端点处的敛散性可能会发生变化，所以在收敛区间（-1，1）上进行讨论.

由于<equation>S_{1}(0) = 0</equation>，故<equation>S_{1}(x) = \int_{0}^{x}\frac{1}{1 + t^{2}}\mathrm{d}t = \arctan x, - 1 < x < 1.</equation>又和函数<equation>S_{1}(x)</equation>在其收敛域[-1,1]上连续，且<equation>\arctan x</equation>在[-1,1]上连续，故<equation>S_{1}(x) = \arctan x, - 1\leqslant x\leqslant 1.</equation>综上所述，<equation>S ( x ) = x S_{1} ( x ) = x \arctan x, - 1 \leqslant x \leqslant 1.</equation>

---

**2009年第16题 | 解答题 | 10分**
16. (本题满分9分)

设 a n为曲线 y=x n与 y=x<equation>^{n+1}</equation>（ n=1,2,<equation>\cdots</equation>）所围成区域的面积，记<equation>S_{1}=\sum_{n=1}^{\infty} a_{n}, S_{2}=\sum_{n=1}^{\infty} a_{2n-1}</equation>，求<equation>S_{1}</equation>与<equation>S_{2}</equation>的值.
**解析: **解曲线<equation>y=x^{n}</equation>与<equation>y=x^{n+1}</equation>交于两点（0，0），（1，1），它们所围成区域的面积为<equation>a _ {n} = \int_ {0} ^ {1} \left(x ^ {n} - x ^ {n + 1}\right) \mathrm {d} x = \left. \left(\frac {x ^ {n + 1}}{n + 1} - \frac {x ^ {n + 2}}{n + 2}\right) \right| _ {0} ^ {1} = \frac {1}{n + 1} - \frac {1}{n + 2}.</equation>级数<equation>\sum_{n=1}^{\infty} a_{n}</equation>的前k项和为<equation>\sum_ {n = 1} ^ {k} a _ {n} = \left(\frac {1}{2} - \frac {1}{3}\right) + \left(\frac {1}{3} - \frac {1}{4}\right) + \dots + \left(\frac {1}{k + 1} - \frac {1}{k + 2}\right) = \frac {1}{2} - \frac {1}{k + 2},</equation>于是<equation>S_{1}=\lim_{k\to \infty}\sum_{n=1}^{k}a_{n}=\lim_{k\to \infty}\left(\frac{1}{2}-\frac{1}{k+2}\right)=\frac{1}{2}.</equation>又<equation>S _ {2} = \sum_ {n = 1} ^ {\infty} a _ {2 n - 1} = \sum_ {n = 1} ^ {\infty} \left(\frac {1}{2 n} - \frac {1}{2 n + 1}\right) = \frac {1}{2} - \frac {1}{3} + \frac {1}{4} - \frac {1}{5} + \dots + \frac {1}{2 n} - \frac {1}{2 n + 1} + \dots ,</equation>而<equation>\ln (1 + x)</equation>的麦克劳林展开式为<equation>\ln (1 + x) = \sum_{n = 1}^{\infty}\frac{(-1)^{n - 1}}{n} x^n,x\in(-1,1]</equation>，故令<equation>x = 1</equation>，得<equation>\ln 2 = 1 - \frac {1}{2} + \frac {1}{3} - \frac {1}{4} + \dots - \frac {1}{2 n} + \frac {1}{2 n + 1} - \dots ,</equation>从而<equation>S_{2}=-(\ln 2-1)=1-\ln 2.</equation>综上所述，<equation>S_{1}=\frac{1}{2}, S_{2}=1-\ln 2.</equation>

---


#### 求幂级数的收敛半径、收敛区间和收敛域

**2022年第14题 | 填空题 | 5分**

14. 已知级数<equation>\sum_{n=1}^{\infty} \frac{n!}{n^{n}} \mathrm{e}^{-nx}</equation>的收敛域为<equation>(a,+\infty)</equation>, 则 a= ___

**答案:**<equation>- 1.</equation>

**解析:**解（法一）令<equation>u_{n}=\frac{n!}{n^{n}} \mathrm{e}^{-n x}</equation>，则原级数为<equation>\sum_{n=1}^{\infty} u_{n}.</equation><equation>\lim_{n\to \infty}\left|\frac{u_{n+1}}{u_{n}}\right|=\lim_{n\to \infty}\frac{(n+1)!}{(n+1)^{n+1}}\cdot \frac{n^{n}}{n!}\mathrm{e}^{-x}=\mathrm{e}^{-x}\lim_{n\to \infty}\frac{n^{n}}{(n+1)^{n}}=\mathrm{e}^{-x}\lim_{n\to \infty}\frac{1}{\left(1+\frac{1}{n}\right)^{n}}=\mathrm{e}^{-1-x}.</equation>由比值审敛法可知，当<equation>\mathrm{e}^{-1-x}<1</equation>时，<equation>\sum_{n=1}^{\infty} u_{n}</equation>收敛，当<equation>\mathrm{e}^{-1-x}>1</equation>时，<equation>\sum_{n=1}^{\infty} u_{n}</equation>发散.由于指数函数单调增加，故<equation>\mathrm{e}^{-1-x}<1</equation>等价于<equation>-1-x<0</equation>即<equation>x>-1</equation>因此，当<equation>x>-1</equation>时，函数项级数<equation>\sum_{n=1}^{\infty}\frac{n!}{n^{n}} \mathrm{e}^{-nx}</equation>收敛，当<equation>x<-1</equation>时，函数项级数<equation>\sum_{n=1}^{\infty}\frac{n!}{n^{n}} \mathrm{e}^{-nx}</equation>发散.

当<equation>x = -1</equation>时，<equation>\mathrm{e}^{-1 - x} = 1.</equation>此时利用比值审敛法无法判定<equation>\sum_{n = 1}^{\infty} u_n</equation>的收敛性. 但是，将<equation>x = -1</equation>代回原级数可得原级数为<equation>\sum_{n = 1}^{\infty}\frac{n!}{n^n}\mathrm{e}^n.</equation>该级数的一般项极限不为0，从而发散（见注）.

因此，函数项级数<equation>\sum_{n = 1}^{\infty}\frac{n!}{n^n}\mathrm{e}^{-nx}</equation>的收敛域为<equation>(-1, +\infty)</equation>，<equation>a = -1.</equation>（法二）令<equation>t = \mathrm{e}^{-x}</equation>，则<equation>\sum_{n = 1}^{\infty}\frac{n!}{n^n}\mathrm{e}^{-nx} = \sum_{n = 1}^{\infty}\frac{n!}{n^n}t^n.</equation><equation>\lim _ {n \rightarrow \infty} \frac {(n + 1) !}{(n + 1) ^ {n + 1}} \cdot \frac {n ^ {n}}{n !} = \lim _ {n \rightarrow \infty} \frac {n ^ {n}}{(n + 1) ^ {n}} = \lim _ {n \rightarrow \infty} \frac {1}{\left(1 + \frac {1}{n}\right) ^ {n}} = \frac {1}{\mathrm {e}}.</equation>于是，<equation>\sum_{n = 1}^{\infty}\frac{n!}{n^n} t^n</equation>的收敛半径为e，收敛区间为<equation>(-\mathrm{e},\mathrm{e})</equation>解<equation>- \mathrm{e} < \mathrm{e}^{-x} < \mathrm{e}</equation>可得，<equation>x > - 1</equation>因此，当<equation>x > - 1</equation>时，函数项级数<equation>\sum_{n=1}^{\infty} \frac{n!}{n^{n}} \mathrm{e}^{-n x}</equation>收敛。并且，当<equation>x < - 1</equation>时，<equation>\mathrm{e}^{-x} > \mathrm{e}</equation>函数项级数<equation>\sum_{n=1}^{\infty} \frac{n!}{n^{n}} \mathrm{e}^{-n x}</equation>发散.

其余同法一.

---

**2020年第4题 | 选择题 | 4分 | 答案: A**

4. 设 R为幂级数<equation>\sum_{n=1}^{\infty} a_{n} x^{n}</equation>的收敛半径，r是实数，则（    )

A. 当<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>发散时，<equation>|r|\geqslant R</equation>B. 当<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>收敛时，<equation>|r|\leqslant R</equation>C. 当<equation>|r|\geqslant R</equation>时，<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>发散 D. 当<equation>|r|\leqslant R</equation>时，<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>收敛

答案: A

**解析:**解 由幂级数的收敛半径的定义可知，当<equation>| r | < R</equation>时，级数<equation>\sum_{n=1}^{\infty} a_{n} r^{n}</equation>绝对收敛.又因为<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>为<equation>\sum_{n=1}^{\infty} a_{n} r^{n}</equation>的偶数项子级数，所以此时由<equation>\sum_{n=1}^{\infty} a_{n} r^{n}</equation>收敛可得<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>收敛.

若<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>发散，则<equation>\sum_{n=1}^{\infty} a_{n} r^{n}</equation>不可能绝对收敛.因此，<equation>| r | \geqslant R</equation>或者，由<equation>| r | < R \Rightarrow \sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>收敛的逆否命题为<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>发散<equation>\Rightarrow | r | \geqslant R</equation>可知，<equation>| r | \geqslant R</equation>应选A.

下面说明其余选项均不正确.

选项B、C：取<equation>a_{n}=\left\{ \begin{array}{ll}1,&n=2k-1,\\ 0,&n=2k, \end{array} \right. k=1,2,3,\dots</equation>，则<equation>\sum_{n=1}^{\infty}a_{n}x^{n}=\sum_{n=1}^{\infty}x^{2n-1}.</equation>该级数为缺项幂级数，易求得其收敛半径为1. 对任何实数<equation>r,\sum_{n=1}^{\infty}a_{2n}r^{2n}</equation>均收敛.因此，选项C不正确.任取<equation>|r| > 1</equation>即可否定选项B.

选项D：当<equation>|r| < R</equation>时，级数<equation>\sum_{n=1}^{\infty} a_{n} r^{n}</equation>绝对收敛.于是由<equation>\sum_{n=1}^{\infty} a_{n} r^{n}</equation>收敛可得<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>收敛.但是，当<equation>|r|=R</equation>时，<equation>\sum_{n=1}^{\infty} a_{n} r^{n}</equation>可能收敛，也可能发散.此时，无法确定<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>的收敛性.

例如：取<equation>a_{n}=1,n=1,2,3,\dots</equation>，则<equation>\sum_{n=1}^{\infty}a_{n}x^{n}=\sum_{n=1}^{\infty}x^{n}</equation>.该幂级数的收敛半径为1.取<equation>r=1</equation>，则<equation>\sum_{n=1}^{\infty}1^{2n}</equation>发散.<equation>|r|=R</equation>时，<equation>\sum_{n=1}^{\infty}a_{2n}r^{2n}</equation>收敛的例子同选项B、C.

---

**2015年第3题 | 选择题 | 4分 | 答案: B**

3. 若级数<equation>\sum_{n=1}^{\infty} a_{n}</equation>条件收敛，则<equation>x=\sqrt{3}</equation>与 x=3依次为幂级数<equation>\sum_{n=1}^{\infty} n a_{n} ( x-1 )^{n}</equation>的（    ）

A. 收敛点，收敛点 B. 收敛点，发散点 C. 发散点，收敛点 D. 发散点，发散点

答案: B

**解析:**解（法一）由<equation>\sum_{n=1}^{\infty} a_{n}</equation>条件收敛知，<equation>\sum_{n=1}^{\infty} a_{n}</equation>收敛，<equation>\sum_{n=1}^{\infty} |a_{n}|</equation>发散.于是幂级数<equation>\sum_{n=1}^{\infty} a_{n} x^{n}</equation>在<equation>x=1</equation>处收敛，从而由阿贝尔定理知，<equation>\sum_{n=1}^{\infty} a_{n} x^{n}</equation>的收敛半径R满足<equation>R\geqslant 1</equation>假设<equation>R > 1</equation>，则由阿贝尔定理知，<equation>\sum_{n=1}^{\infty} |a_{n}|</equation>收敛，矛盾，故假设不成立，从而<equation>R=1.</equation>幂级数<equation>\sum_{n=1}^{\infty} a_{n}(x-1)^{n}</equation>与<equation>\sum_{n=1}^{\infty} a_{n}x^{n}</equation>的收敛半径相同，均为1.又逐项求导不改变收敛半径，故<equation>\sum_{n=1}^{\infty} n a_{n}(x-1)^{n-1}</equation>的收敛半径为1，从而<equation>\sum_{n=1}^{\infty} n a_{n}(x-1)^{n}</equation>的收敛半径为1.因此<equation>\sum_{n=1}^{\infty} n a_{n}(x-1)^{n}</equation>当<equation>|x-1| < 1</equation>即<equation>x\in(0,2)</equation>时收敛；当<equation>|x-1| > 1</equation>即<equation>x\in(-\infty ,0)\cup(2,+\infty)</equation>时发散.由于<equation>0 < \sqrt{3} < 2 < 3</equation>故<equation>\sum_{n=1}^{\infty} n a_{n}(x-1)^{n}</equation>在<equation>x=\sqrt{3}</equation>处收敛，在<equation>x=3</equation>处发散，从而选B.

（法二）特殊值法.

令<equation>a_{n}=\frac{(-1)^{n}}{n}</equation>满足<equation>\sum_{n=1}^{\infty} a_{n}</equation>条件收敛.又<equation>\sum_{n=1}^{\infty} n a_{n}(x-1)^{n}=\sum_{n=1}^{\infty}(-1)^{n}(x-1)^{n}</equation>的收敛域为 (0,2)，故该幂级数在<equation>x=\sqrt{3}</equation>处收敛，在<equation>x=3</equation>处发散，从而选B.

---

**2011年第2题 | 选择题 | 4分 | 答案: C**

2. 设数列<equation>\{a_{n}\}</equation>单调减少，<equation>\lim_{n\to \infty}a_{n}=0,S_{n}=\sum_{k=1}^{n}a_{k}</equation>（ n=1，2，<equation>\cdots</equation>）无界，则幂级数<equation>\sum_{n=1}^{\infty}a_{n}(x-1)^{n}</equation>的收敛域为（    ）

A. (-1,1] B. [-1,1) C. [0,2) D. (0,2]

答案: C

**解析:**解（法一）由于数列<equation>\left\{a_{n}\right\}</equation>单调减少且<equation>\lim_{n\to \infty}a_{n}=0</equation>，故<equation>a_{n}>0,n=1,2,\dots</equation>由莱布尼茨定理知，<equation>\sum_{n=1}^{\infty}a_{n}(-1)^{n}</equation>收敛，即<equation>\sum_{n=1}^{\infty}a_{n}x^{n}</equation>在<equation>x=-1</equation>处收敛，由阿贝尔定理知，<equation>\sum_{n=1}^{\infty}a_{n}x^{n}</equation>的收敛半径<equation>R\geqslant 1</equation>又<equation>S_{n}</equation>无界，故<equation>\sum_{n=1}^{\infty}a_{n}</equation>发散，即<equation>\sum_{n=1}^{\infty}a_{n}x^{n}</equation>在<equation>x=1</equation>处发散，由阿贝尔定理知，<equation>R\leqslant 1</equation>，于是<equation>R=1.</equation>因此<equation>\sum_{n=1}^{\infty} a_{n} x^{n}</equation>的收敛域为[-1,1)，从而<equation>\sum_{n=1}^{\infty} a_{n} (x-1)^{n}</equation>的收敛点满足<equation>- 1\leqslant x-1<1</equation>即收敛域为[0,2).应选C.


幂级数<equation>\sum_{n=1}^{\infty} a_{n} ( x-1 )^{n}</equation>的收敛域是以 x=1为中心，故排除选项A、B.又当 x=2时，<equation>\sum_{n=1}^{\infty} a_{n} ( x-1 )^{n}</equation><equation>= \sum_{n=1}^{\infty} a_{n}</equation>发散，故 x=2不在其收敛域中，从而排除选项D.应选C.

---


### 多元函数积分学


#### 交换积分次序与坐标系之间的转化

**2025年第4题 | 选择题 | 5分 | 答案: A**

4. 设函数 f(x,y) 连续，则<equation>\int_{-2}^{2}\mathrm{d}x\int_{4-x^{2}}^{4}f(x,y)\mathrm{d}y=</equation>(    )

A.<equation>\int_{0}^{4}\left[\int_{-2}^{-\sqrt{4-y}}f(x,y)\mathrm{d}x+\int_{\sqrt{4-y}}^{2}f(x,y)\mathrm{d}x\right]\mathrm{d}y</equation>B.<equation>\int_{0}^{4}\left[\int_{-2}^{\sqrt{4-y}}f(x,y)\mathrm{d}x+\int_{\sqrt{4-y}}^{2}f(x,y)\mathrm{d}x\right]\mathrm{d}y</equation>C.<equation>\int_{0}^{4}\left[\int_{-2}^{-\sqrt{4-y}}f(x,y)\mathrm{d}x+\int_{2}^{\sqrt{4-y}}f(x,y)\mathrm{d}x\right]\mathrm{d}y</equation>D.<equation>2\int_{0}^{4}\mathrm{d}y\int_{\sqrt{4-y}}^{2}f(x,y)\mathrm{d}x</equation>

答案: A

**解析:**解 如图所示，二次积分<equation>\int_{-2}^{2}\mathrm{d}x\int_{4-x^{2}}^{4}f(x,y)\mathrm{d}y</equation>对应的二重积分的积分区域 D为图中灰色区域.<equation>D = \left\{(x, y) \mid 4 - x ^ {2} \leqslant y \leqslant 4, - 2 \leqslant x \leqslant 2 \right\}.</equation>当 x < 0时，解 y = 4 - x²可得 x = -<equation>\sqrt{4-y}</equation>，当 x > 0时，解 y = 4 - x²可得 x =<equation>\sqrt{4-y}</equation>.于是，将 D写成 Y型区域需要将其分块，<equation>D=\{(x,y)\mid-2\leqslant x\leqslant-\sqrt{4-y},0\leqslant y\leqslant 4\} \cup \{(x,y)\mid\sqrt{4-y}\leqslant x\leqslant 2,0\leqslant y\leqslant 4\}</equation>从而，<equation>\int_ {- 2} ^ {2} \mathrm {d} x \int_ {4 - x ^ {2}} ^ {4} f (x, y) \mathrm {d} y = \iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {4} \left[ \int_ {- 2} ^ {- \sqrt {4 - y}} f (x, y) \mathrm {d} x + \int_ {\sqrt {4 - y}} ^ {2} f (x, y) \mathrm {d} x \right] \mathrm {d} y.</equation>选项A正确，选项B、C不正确.

对选项D，该选项正确意味着<equation>\iint_{D} f(x,y)\mathrm{d}x\mathrm{d}y = 2\iint_{D_1} f(x,y)\mathrm{d}x\mathrm{d}y</equation>，其中<equation>D_{1}</equation>为D位于y轴右边的部分，而该式成立需要<equation>f(x,y)</equation>是关于x的偶函数，但题干条件中并没有这一信息，故该选项不正确.例如，取<equation>f(x,y) = x</equation>，则<equation>\iint_{D} f(x,y)\mathrm{d}x\mathrm{d}y = 0</equation>，而<equation>\iint_{D_1} f(x,y)\mathrm{d}x\mathrm{d}y > 0.</equation>因此，应选A.

---

**2015年第4题 | 选择题 | 4分 | 答案: B**

4. 设 D是第一象限中的曲线<equation>2 x y=1, 4 x y=1</equation>与直线 y=x,y=<equation>\sqrt{3} x</equation>围成的平面区域，函数 f(x,y)在 D上连续，则<equation>\iint \limits_{D} f(x,y)\mathrm{d} x\mathrm{d} y=</equation>(    )

A.<equation>\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \mathrm{d} \theta \int_{\frac{1}{2 \sin 2 \theta}}^{\frac{1}{\sin 2 \theta}} f ( r \cos \theta,r \sin \theta ) r \mathrm{d} r</equation>B.<equation>\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \mathrm{d} \theta \int_{\frac{1}{\sqrt{2 \sin 2 \theta}}}^{\frac{1}{\sqrt{\sin 2 \theta}}} f ( r \cos \theta,r \sin \theta ) r \mathrm{d} r</equation>C.<equation>\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \mathrm{d} \theta \int_{\frac{1}{2 \sin 2 \theta}}^{\frac{1}{\sin 2 \theta}} f ( r \cos \theta,r \sin \theta ) \mathrm{d} r</equation>D.<equation>\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \mathrm{d} \theta \int_{\frac{1}{\sqrt{2 \sin 2 \theta}}}^{\frac{1}{\sqrt{\sin 2 \theta}}} f ( r \cos \theta,r \sin \theta ) \mathrm{d} r</equation>

答案: B

**解析:**解 将曲线<equation>2 x y=1</equation>，<equation>4 x y=1</equation>，直线<equation>y=x</equation>，<equation>y=\sqrt{3} x</equation>改写为极坐标形式.积分区域如图所示.<equation>2 x y = 1 \Rightarrow r ^ {2} \sin 2 \theta = 1 \Rightarrow r = \frac {1}{\sqrt {\sin 2 \theta}},</equation><equation>4 x y = 1 \Rightarrow 2 r ^ {2} \sin 2 \theta = 1 \Rightarrow r = \frac {1}{\sqrt {2 \sin 2 \theta}},</equation><equation>y = x \Rightarrow \theta = \frac {\pi}{4},</equation><equation>y = \sqrt {3} x \Rightarrow \theta = \frac {\pi}{3},</equation><equation>\mathrm {d} x \mathrm {d} y = r \mathrm {d} r \mathrm {d} \theta .</equation>于是，积分区域<equation>D</equation>在极坐标系下表示为<equation>D = \left\{(r, \theta) \mid \frac {1}{\sqrt {2 \sin 2 \theta}} \leqslant r \leqslant \frac {1}{\sqrt {\sin 2 \theta}}, \frac {\pi}{4} \leqslant \theta \leqslant \frac {\pi}{3} \right\}.</equation>因此，<equation>\iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{3}} \mathrm {d} \theta \int_ {\frac {1}{\sqrt {2 \sin 2 \theta}}} ^ {\frac {1}{\sqrt {\sin 2 \theta}}} f (r \cos \theta , r \sin \theta) r \mathrm {d} r.</equation>应选B.

---

**2014年第3题 | 选择题 | 4分 | 答案: D**

3. 设 f(x,y)是连续函数，则<equation>\int_{0}^{1}\mathrm{d}y\int_{-\sqrt{1-y^{2}}}^{1-y}f(x,y)\mathrm{d}x=</equation>(    )

A.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{x-1}f(x,y)\mathrm{d}y+\int_{-1}^{0}\mathrm{d}x\int_{0}^{\sqrt{1-x^{2}}}f(x,y)\mathrm{d}y</equation>B.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{1-x}f(x,y)\mathrm{d}y+\int_{-1}^{0}\mathrm{d}x\int_{-\sqrt{1-x^{2}}}^{0}f(x,y)\mathrm{d}y</equation>C.<equation>\int_{0}^{\frac{\pi}{2}}\mathrm{d}\theta \int_{0}^{\frac{1}{\cos \theta+\sin \theta}}f(r\cos \theta,r\sin \theta)\mathrm{d}r+\int_{\frac{\pi}{2}}^{\pi}\mathrm{d}\theta \int_{0}^{1}f(r\cos \theta,r\sin \theta)\mathrm{d}r</equation>D.<equation>\int_{0}^{\frac{\pi}{2}}\mathrm{d}\theta \int_{0}^{\frac{1}{\cos \theta+\sin \theta}}f(r\cos \theta,r\sin \theta)r\mathrm{d}r+\int_{\frac{\pi}{2}}^{\pi}\mathrm{d}\theta \int_{0}^{1}f(r\cos \theta,r\sin \theta)r\mathrm{d}r</equation>

答案: D

**解析:**分析本题主要考查二次积分的积分次序交换和换元法.观察选项A、B，是将先x后y的二次积分化为先y后x的二次积分，结合积分区域的图形来转化会比较方便；观察选项C、D，是将原二次积分化为极坐标系下的二次积分，需要用到换元公式<equation>\iint_{D} f(x,y)\mathrm{d}x\mathrm{d}y=\iint_{D} f(r\cos \theta ,r\sin \theta )r\mathrm{d}r\mathrm{d}\theta.</equation>解题设中二次积分的积分区域为<equation>D=\{(x,y)\mid 0\leqslant y\leqslant 1,-\sqrt{1-y^{2}}\leqslant x\leqslant 1-y\}</equation>，将区域D分成两部分<equation>D_{1}</equation>和<equation>D_{2}</equation>（如上图所示），其中<equation>\begin{array}{l} D _ {1} = \left\{(x, y) \mid 0 \leqslant y \leqslant \sqrt {1 - x ^ {2}}, - 1 \leqslant x \leqslant 0 \right\}, \\ D _ {2} = \left\{(x, y) \mid 0 \leqslant y \leqslant 1 - x, 0 \leqslant x \leqslant 1 \right\}. \\ \end{array}</equation>于是<equation>\int_0^1\mathrm{d}y\int_{- \sqrt{1 - y^2}}^{1 - y}f(x,y)\mathrm{d}x = \int_{-1}^0\mathrm{d}x\int_0^{\sqrt{1 - x^2}}f(x,y)\mathrm{d}y + \int_0^1\mathrm{d}x\int_0^{1 - x}f(x,y)\mathrm{d}y</equation>，从而选项A、B均不正确.

在极坐标变换下，区域<equation>D_{1}</equation>的边界方程为<equation>\theta = \frac{\pi}{2},\theta = \pi,r = 1</equation>；区域<equation>D_{2}</equation>的边界方程为<equation>\theta = 0,\theta = \frac{\pi}{2},r = \frac{1}{\cos \theta + \sin \theta}</equation>设区域<equation>D_{1},D_{2}</equation>在极坐标变换下对应于直角坐标平面<equation>rO\theta</equation>上的区域为<equation>D_{1}^{\prime},D_{2}^{\prime}</equation>，则<equation>D _ {1} ^ {\prime} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 1, \frac {\pi}{2} \leqslant \theta \leqslant \pi \right\},</equation><equation>D _ {2} ^ {\prime} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \frac {1}{\cos \theta + \sin \theta}, 0 \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation>从而<equation>\int_ {0} ^ {1} \mathrm {d} y \int_ {- \sqrt {1 - y ^ {2}}} ^ {1 - y} f (x, y) \mathrm {d} x = \int_ {0} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {\frac {1}{\cos \theta + \sin \theta}} f (r \cos \theta , r \sin \theta) r \mathrm {d} r + \int_ {\frac {\pi}{2}} ^ {\pi} \mathrm {d} \theta \int_ {0} ^ {1} f (r \cos \theta , r \sin \theta) r \mathrm {d} r.</equation>应选 D.

选项C错误的原因是少了雅可比式<equation>r</equation>

---


#### 第二类曲线积分

**2025年第14题 | 填空题 | 5分**
14. 已知有向曲线 L是沿抛物线<equation>y=1-x^{2}</equation>从点（1,0）到点（-1,0）的一段，则曲线积分<equation>\int_{L}(y+\cos x)\mathrm{d}x+(2x+\cos y)\mathrm{d}y=</equation>___
**答案: **<equation>\frac {4}{3} - 2 \sin 1.</equation>
**解析: **解（法一）如图所示，添加一条有向线段<equation>L_{1}</equation>，使之起点为<equation>(-1,0)</equation>，终点为（1，0），则<equation>L + L_{1}</equation>围成一个平面封闭区域<equation>D,L + L_{1}</equation>为<equation>D</equation>的正向边界.

注意到区域 D关于 y轴对称，记<equation>D_{1}</equation>为 D位于 y轴右边的部分.将<equation>D_{1}</equation>写成 X型区域.<equation>D _ {1} = \left\{(x, y) \mid 0 \leqslant y \leqslant 1 - x ^ {2}, 0 \leqslant x \leqslant 1 \right\}.</equation>记<equation>P ( x,y)=y+\cos x, Q ( x,y)=2 x+\cos y</equation>，则<equation>\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}=2-1=1.</equation>根据格林公式，<equation>\begin{aligned} \oint_ {L + L _ {1}} (y + \cos x) \mathrm {d} x + (2 x + \cos y) \mathrm {d} y &= \iint_ {D} \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} \mathrm {d} x \mathrm {d} y = 2 \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {1 - x ^ {2}} \mathrm {d} y \\ &= 2 \int_ {0} ^ {1} \left(1 - x ^ {2}\right) \mathrm {d} x = 2 \left(1 - \frac {x ^ {3}}{3} \Big | _ {0} ^ {1}\right) = \frac {4}{3}. \end{aligned}</equation>另一方面，<equation>\int_ {L _ {1}} \left(y + \cos x\right) \mathrm {d} x + \left(2 x + \cos y\right) \mathrm {d} y \stackrel {y = 0} {=} \int_ {L _ {1}} \cos x \mathrm {d} x = \int_ {- 1} ^ {1} \cos x \mathrm {d} x = 2 \int_ {0} ^ {1} \cos x \mathrm {d} x = 2 \sin 1.</equation>因此，<equation>\int_{L}(y + \cos x)\mathrm{d}x + (2x + \cos y)\mathrm{d}y = \frac{4}{3} - 2\sin 1.</equation>（法二）曲线 L的参数方程为<equation>\left\{\begin{array}{l}x=x,\\ y=1-x^{2},\end{array}\right.</equation>x从1变到-1.将参数方程代入曲线积分可得<equation>\int_{L}(y+\cos x)\mathrm{d}x+(2x+\cos y)\mathrm{d}y=\int_{1}^{-1}\left\{(1-x^{2}+\cos x)+[2x+\cos(1-x^{2})]\cdot(-2x)\right\}\mathrm{d}x</equation><equation>= \int_{1}^{-1}\left[1-5x^{2}+\cos x-2x\cos \left(1-x^{2}\right)\right]\mathrm{d}x</equation><equation>\frac{\mathrm{对称性}}{}2\int_{0}^{1}\left(5x^{2}-1-\cos x\right)\mathrm{d}x=2\left(\frac{5x^{3}}{3}-x-\sin x\right)\Bigg|_{0}^{1}</equation><equation>= 2\left(\frac{2}{3}-\sin 1\right)=\frac{4}{3}-2\sin 1.</equation>

---

**2024年第20题 | 解答题 | 12分**
20. (本题满分12分)

已知有向曲线 L为球面<equation>x^{2}+y^{2}+z^{2}=2x</equation>与平面 2x-z-1=0的交线，从z轴正向往z轴负向看去为逆时针方向，计算曲线积分<equation>\int_{L}(6xyz-yz^{2})\mathrm{d}x+2x^{2}z\mathrm{d}y+xyz\mathrm{d}z.</equation>
**答案: **##<equation>\frac{4\sqrt{5}}{25}\pi.</equation>
**解析: **分析 本题主要考查第二类曲线积分的计算.

本题中的曲线 L是一条封闭曲线，可以考虑利用斯托克斯公式将曲线积分转化为曲面积分.

解 曲线<equation>L</equation>的方程为<equation>\left\{ \begin{array}{l l} x^{2} + y^{2} + z^{2} = 2x, \\ 2x - z - 1 = 0. \end{array} \right.</equation>如图所示，<equation>L</equation>为封闭曲线，其所围平面<equation>2x - z - 1 = 0</equation>上的有界部分为<equation>\Sigma</equation>，取上侧.

记所求曲线积分为<equation>I</equation>，由于曲线<equation>L</equation>的方向和曲面<equation>\Sigma</equation>的方向符合右手法则，故根据斯托克斯公式，<equation>\begin{aligned} I &= \oint_ {L} \left(6 x y z - y z ^ {2}\right) \mathrm {d} x + 2 x ^ {2} z \mathrm {d} y + x y z \mathrm {d} z = \iint_ {\Sigma} \left| \begin{array}{c c c} \mathrm {d} y \mathrm {d} z & \mathrm {d} z \mathrm {d} x & \mathrm {d} x \mathrm {d} y \\ \frac {\partial}{\partial x} & \frac {\partial}{\partial y} & \frac {\partial}{\partial z} \\ 6 x y z - y z ^ {2} & 2 x ^ {2} z & x y z  \right| \\ &= \iint_ {\Sigma} \left(x z - 2 x ^ {2}\right) \mathrm {d} y \mathrm {d} z + \left(6 x y - 3 y z\right) \mathrm {d} z \mathrm {d} x + \left(z ^ {2} - 2 x z\right) \mathrm {d} x \mathrm {d} y \\ &= \iint_ {\Sigma} (2 x - z) \cdot (- x) \mathrm {d} y \mathrm {d} z + (2 x - z) \cdot 3 y \mathrm {d} z \mathrm {d} x + (2 x - z) \cdot (- z) \mathrm {d} x \mathrm {d} y \\ \frac {2 x - z = 1}{\sim} \iint_ {\Sigma} (- x) \mathrm {d} y \mathrm {d} z + 3 y \mathrm {d} z \mathrm {d} x + (- z) \mathrm {d} x \mathrm {d} y. \end{aligned}</equation>利用两类曲面积分之间的联系将<equation>\iint_{\Sigma} (-x)\mathrm{d}y\mathrm{d}z + 3y\mathrm{d}z\mathrm{d}x + (-z)\mathrm{d}x\mathrm{d}y</equation>转化为关于坐标<equation>x,y</equation>的积分再计算

令<equation>F ( x,y,z) = z - 2 x + 1</equation>，则曲面<equation>\varSigma</equation>的方程为<equation>F ( x,y,z) = 0</equation>，法向量 n可取为<equation>\left(F_{x}^{\prime},F_{y}^{\prime},F_{z}^{\prime}\right) =</equation>（-2,0,1).于是，<equation>\varSigma</equation>的法向量 n的方向余弦为<equation>\cos \alpha = \frac {- 2}{\sqrt {5}}, \quad \cos \beta = 0, \quad \cos \gamma = \frac {1}{\sqrt {5}}.</equation>由此可得<equation>\mathrm{d}y\mathrm{d}z = \frac{\cos \alpha}{\cos \gamma}\mathrm{d}x\mathrm{d}y = -2\mathrm{d}x\mathrm{d}y,\mathrm{d}z\mathrm{d}x = 0\mathrm{d}x\mathrm{d}y = 0.</equation>进一步可得<equation>I = \iint_{\Sigma} (-x)\mathrm{d}y\mathrm{d}z + 3y\mathrm{d}z\mathrm{d}x + (-z)\mathrm{d}x\mathrm{d}y = \iint_{\Sigma} [(-x)\cdot(-2) + (-z)\cdot 1]\mathrm{d}x\mathrm{d}y = \iint_{D}\mathrm{d}x\mathrm{d}y,</equation>其中<equation>D</equation>为<equation>\varSigma</equation>在<equation>xOy</equation>面上的投影区域.于是，<equation>I</equation>的值等于区域D的面积.

将<equation>z = 2x - 1</equation>代入<equation>x^{2} + y^{2} + z^{2} = 2x</equation>可得<equation>x^{2} + y^{2} + (2x - 1)^{2} - 2x = 0</equation>，整理可得<equation>5x^{2} - 6x + y^{2} + 1 = 0</equation>，即<equation>5\left(x - \frac{3}{5}\right)^{2} + y^{2} = \frac{4}{5}</equation>，也即<equation>\frac{\left(x - \frac{3}{5}\right)^{2}}{\frac{4}{25}} + \frac{y^{2}}{\frac{4}{5}} = 1.</equation>这是<equation>xOy</equation>面上以点<equation>\left(\frac{3}{5},0\right)</equation>为中心，长半轴长为<equation>\sqrt{\frac{4}{5}}</equation>，短半轴长为<equation>\sqrt{\frac{4}{25}}</equation>的椭圆，从而区域 D为由该椭圆所围成的椭圆盘，其面积为<equation>\pi \cdot \sqrt{\frac{4}{5}}\cdot \sqrt{\frac{4}{25}} = \frac{4\pi}{5\sqrt{5}} = \frac{4\sqrt{5}\pi}{25}.</equation>因此，<equation>I=\frac{4\sqrt{5}\pi}{25}.</equation>

---

**2022年第19题 | 解答题 | 12分**
19. (本题满分12分)

已知曲线 L是曲面<equation>\Sigma: 4 x^{2}+y^{2}+z^{2}=1, x\geqslant0, y\geqslant0, z\geqslant0</equation>的边界，曲面<equation>\Sigma</equation>方向朝上，曲线 L的方向和曲面<equation>\Sigma</equation>的方向符合右手法则，计算<equation>I=\oint_{L}(y z^{2}-\cos z) \mathrm{d} x+2 x z^{2} \mathrm{d} y+(2 x y z+x \sin z) \mathrm{d} z.</equation>
**解析: **（法一）根据右手法则，曲线<equation>L</equation>应取逆时针方向.

(a)

(b)

如图（a）所示，记<equation>L_{1}, L_{2}, L_{3}</equation>分别为 L在 xOy面，yOz面，zOx面的部分在<equation>L_{1}</equation>上，<equation>z=0,\int_{L_{1}}\mathrm{d}z=0.</equation>起点为<equation>\left(\frac{1}{2},0,0\right)</equation>终点为（0，1，0）.在<equation>L_{2}</equation>上，<equation>x=0,\int_{L_{2}}\mathrm{d}x=0.</equation>起点为（0，1，0），终点为（0，0，1）.在<equation>L_{3}</equation>上，<equation>y=0,\int_{L_{3}}\mathrm{d}y=0.</equation>起点为（0，0，1），终点为<equation>\left(\frac{1}{2},0,0\right).</equation>因此，<equation>\begin{aligned} I &= \oint_ {L} \left(y z ^ {2} - \cos z\right) \mathrm {d} x + 2 x z ^ {2} \mathrm {d} y + \left(2 x y z + x \sin z\right) \mathrm {d} z \\ &= \int_ {L _ {1}} (- \cos 0) \mathrm {d} x + 0 + \int_ {L _ {3}} (- \cos z) \mathrm {d} x + x \sin z \mathrm {d} z \\ &= (- 1) \times \left(0 - \frac {1}{2}\right) + \int_ {L _ {3}} \mathrm {d} (- x \cos z) = \frac {1}{2} + (- x \cos z) \Big | _ {(0, 0, 1)} ^ {\left(\frac {1}{2}, 0, 0\right)} \\ &= \frac {1}{2} - \frac {1}{2} = 0. \end{aligned}</equation>由于曲线<equation>L</equation>的方向和曲面<equation>\Sigma</equation>的方向符合右手法则，故根据斯托克斯公式，<equation>\begin{aligned} I &= \iint_ {\Sigma} \left| \begin{array}{c c c} \mathrm {d} y \mathrm {d} z & \mathrm {d} z \mathrm {d} x & \mathrm {d} x \mathrm {d} y \\ \frac {\partial}{\partial x} & \frac {\partial}{\partial y} & \frac {\partial}{\partial z} \\ y z ^ {2} - \cos z & 2 x z ^ {2} & 2 x y z + x \sin z  \right| \\ &= \iint_ {\Sigma} \left(2 x z - 4 x z\right) \mathrm {d} y \mathrm {d} z + (- 1) \left(2 y z + \sin z - 2 y z - \sin z\right) \mathrm {d} z \mathrm {d} x + \left(2 z ^ {2} - z ^ {2}\right) \mathrm {d} x \mathrm {d} y \\ &= \iint_ {\Sigma} (- 2 x z) \mathrm {d} y \mathrm {d} z + z ^ {2} \mathrm {d} x \mathrm {d} y. \end{aligned}</equation>如图（b）所示，添加平面<equation>\varSigma_{1}:z=0(4x^{2}+y^{2}\leqslant 1)</equation>，取下侧，<equation>\varSigma_{2}:x=0(y^{2}+z^{2}\leqslant 1)</equation>，取后侧，<equation>\varSigma_{3}:y=0(4x^{2}+z^{2}\leqslant 1)</equation>，取左侧，则<equation>\varSigma_{1},\varSigma_{2},\varSigma_{3}</equation>与<equation>\varSigma</equation>共同围成一个空间封闭区域<equation>\varOmega</equation>，且法向量指向外侧.<equation>\oiint_ {\Sigma + \Sigma_ {1} + \Sigma_ {2} + \Sigma_ {3}} (- 2 x z) \mathrm {d} y \mathrm {d} z + z ^ {2} \mathrm {d} x \mathrm {d} y = \iiint_ {\Omega} (- 2 z + 2 z) \mathrm {d} v = 0.</equation>另一方面，由于<equation>\varSigma_{1}</equation>和<equation>\varSigma_{3}</equation>均垂直于yOz面，故在这两个面上关于坐标y,z的积分为0.由于<equation>\varSigma_{2}</equation>和<equation>\varSigma_{3}</equation>均垂直于xOy面，故在这两个面上关于坐标x,y的积分为0.从而在<equation>\varSigma_{3}</equation>上，关于坐标y,z和关于坐标x,y的积分均为0.于是，<equation>\iint_ {\Sigma_ {3}} (- 2 x z) \mathrm {d} y \mathrm {d} z + z ^ {2} \mathrm {d} x \mathrm {d} y = 0.</equation>再分别代入<equation>\varSigma_{1}</equation>和<equation>\varSigma_{2}</equation>的方程可得<equation>\begin{aligned} \iint_ {\Sigma_ {1}} (- 2 x z) \mathrm {d} y \mathrm {d} z + z ^ {2} \mathrm {d} x \mathrm {d} y \stackrel {z = 0} {=} 0. \\ \iint_ {\Sigma_ {2}} (- 2 x z) \mathrm {d} y \mathrm {d} z + z ^ {2} \mathrm {d} x \mathrm {d} y \stackrel {x = 0} {=} 0. \end{aligned}</equation>因此，<equation>I = \oiint_ {\Sigma + \Sigma_ {1} + \Sigma_ {2} + \Sigma_ {3}} (- 2 x z) \mathrm {d} y \mathrm {d} z + z ^ {2} \mathrm {d} x \mathrm {d} y - \oiint_ {\Sigma_ {1} + \Sigma_ {2} + \Sigma_ {3}} (- 2 x z) \mathrm {d} y \mathrm {d} z + z ^ {2} \mathrm {d} x \mathrm {d} y = 0 - 0 = 0.</equation>

---

**2021年第20题 | 解答题 | 12分**
20. （本题满分12分）

设<equation>D\subset \mathbf{R}^{2}</equation>是有界单连通闭区域，<equation>I(D)=\iint_{D}(4-x^{2}-y^{2})\mathrm{d}x\mathrm{d}y</equation>取得最大值的积分区域为<equation>D_{1}.</equation>I. 求<equation>I ( D_{1} )</equation>的值；

II. 计算<equation>\int_{\partial D_1}\frac{(x\mathrm{e}^{x^2 + 4y^2} + y)\mathrm{d}x + (4y\mathrm{e}^{x^2 + 4y^2} - x)\mathrm{d}y}{x^2 + 4y^2}</equation>，其中<equation>\partial D_{1}</equation>是<equation>D_{1}</equation>的正向边界.
**答案: **( I )<equation>I ( D_{1} )=8 \pi;</equation>( II )<equation>-\pi.</equation>
**解析: **解（I）取区域<equation>D_{1}</equation>，使其包含所有使得被积函数非负的点，且不包含使得被积函数小于零的点，则在<equation>D_{1}</equation>上<equation>I(D)</equation>取得最大值. 可取<equation>D_{1}</equation>为<equation>4 - x^{2} - y^{2}\geqslant 0</equation>的区域，即圆盘域<equation>D_{1} = \{(x,y)|x^{2} + y^{2}\leqslant 4\}</equation>.<equation>\begin{aligned} I \left(D _ {1}\right) &= \iint_ {D _ {1}} \left(4 - x ^ {2} - y ^ {2}\right) \mathrm {d} x \mathrm {d} y \xlongequal {\text {极 坐 标}} \iint_ {D _ {1}} \left(4 - r ^ {2}\right) r \mathrm {d} r \mathrm {d} \theta = \int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {0} ^ {2} \left(4 r - r ^ {3}\right) \mathrm {d} r \\ &= 2 \pi \left(2 r ^ {2} - \frac {r ^ {4}}{4}\right) \Bigg | _ {0} ^ {2} = 2 \pi \times (8 - 4) = 8 \pi . \end{aligned}</equation>（Ⅱ）记所求积分为<equation>I, P(x,y) = \frac{x\mathrm{e}^{x^2 + 4y^2} + y}{x^2 + 4y^2}, Q(x,y) = \frac{4y\mathrm{e}^{x^2 + 4y^2} - x}{x^2 + 4y^2}</equation>，则当<equation>(x,y)\neq (0,0)</equation>时，<equation>\begin{aligned} \frac {\partial Q}{\partial x} &= \frac {\left(8 x y \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} - 1\right) \left(x ^ {2} + 4 y ^ {2}\right) - \left(4 y \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} - x\right) \cdot 2 x}{\left(x ^ {2} + 4 y ^ {2}\right) ^ {2}} \\ &= \frac {8 x y \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} \left(x ^ {2} + 4 y ^ {2} - 1\right) + x ^ {2} - 4 y ^ {2}}{\left(x ^ {2} + 4 y ^ {2}\right) ^ {2}}, \end{aligned}</equation><equation>\begin{aligned} \frac {\partial P}{\partial y} &= \frac {\left(8 x y \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} + 1\right) \left(x ^ {2} + 4 y ^ {2}\right) - \left(x \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} + y\right) \cdot 8 y}{\left(x ^ {2} + 4 y ^ {2}\right) ^ {2}} \\ &= \frac {8 x y \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} \left(x ^ {2} + 4 y ^ {2} - 1\right) + x ^ {2} - 4 y ^ {2}}{\left(x ^ {2} + 4 y ^ {2}\right) ^ {2}}. \end{aligned}</equation>于是，<equation>\frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y}</equation>原点为被积函数的奇点，且包含在<equation>D_{1}</equation>内.

记<equation>\partial D_{1}=L</equation>作辅助曲线<equation>L^{\prime}:x^{2}+4y^{2}=\varepsilon^{2}</equation>并使<equation>\varepsilon</equation>足够小，使<equation>L^{\prime}</equation>围成的椭圆包含在 L围成的圆中，其参数方程为<equation>\left\{ \begin{array}{l l} x=\varepsilon\cos t, \\ y=\frac{\varepsilon}{2}\sin t, \end{array} \right.</equation>t从0变到<equation>2\pi</equation>如图所示，<equation>L^{\prime}</equation>的正向为逆时针方向，<equation>L^{\prime}</equation>所围成的区域记为<equation>D_{0}, L+L^{\prime}-</equation>围成区域<equation>D_{1}\backslash D_{0}</equation>被积函数在<equation>D_{1}\backslash D_{0}</equation>上没有奇点.

由格林公式，<equation>\oint_ {L + L ^ {\prime} -} \frac {\left(x \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} + y\right) \mathrm {d} x + \left(4 y \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} - x\right) \mathrm {d} y}{x ^ {2} + 4 y ^ {2}} \xlongequal {\text {格 林 公 式}} \iint_ {D _ {1} \backslash D _ {0}} 0 \mathrm {d} x \mathrm {d} y = 0,</equation>因此，<equation>\begin{aligned} I &= \oint_ {L} \frac {\left(x \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} + y\right) \mathrm {d} x + \left(4 y \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} - x\right) \mathrm {d} y}{x ^ {2} + 4 y ^ {2}} = \oint_ {L ^ {\prime}} \frac {\left(x \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} + y\right) \mathrm {d} x + \left(4 y \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} - x\right) \mathrm {d} y}{x ^ {2} + 4 y ^ {2}} \\ \xlongequal {x ^ {2} + 4 y ^ {2} = \varepsilon^ {2}} \frac {1}{\varepsilon^ {2}} \oint_ {L ^ {\prime}} \left(x \mathrm {e} ^ {\varepsilon^ {2}} + y\right) \mathrm {d} x + \left(4 y \mathrm {e} ^ {\varepsilon^ {2}} - x\right) \mathrm {d} y \\ \xlongequal {\text {格 林 公 式}} \frac {1}{\varepsilon^ {2}} \iint_ {D _ {0}} \left[ \frac {\partial \left(4 y \mathrm {e} ^ {\varepsilon^ {2}} - x\right)}{\partial x} - \frac {\partial \left(x \mathrm {e} ^ {\varepsilon^ {2}} + y\right)}{\partial y} \right] \mathrm {d} x \mathrm {d} y &= \frac {1}{\varepsilon^ {2}} \iint_ {D _ {0}} (- 1 - 1) \mathrm {d} x \mathrm {d} y \\ &= - \frac {2}{\varepsilon^ {2}} \cdot D _ {0} \text {的 面 积} = - \frac {2}{\varepsilon^ {2}} \times \pi \times \varepsilon \times \frac {\varepsilon}{2} = - \pi . \end{aligned}</equation>

---

**2020年第16题 | 解答题 | 10分**
16. (本题满分10分)

计算曲线积分<equation>I=\oint_{L}\frac{4x-y}{4x^{2}+y^{2}}\mathrm{d}x+\frac{x+y}{4x^{2}+y^{2}}\mathrm{d}y</equation>，其中 L为<equation>x^{2}+y^{2}=2</equation>，方向为逆时针方向.
**解析: **解记 L围成的封闭区域为 D.记<equation>P ( x,y)=\frac{4 x-y}{4 x^{2}+y^{2}}, Q ( x,y)=\frac{x+y}{4 x^{2}+y^{2}}</equation>，则当（x,y）<equation>\neq</equation>（0,0）时，<equation>\frac {\partial Q}{\partial x} = \frac {4 x ^ {2} + y ^ {2} - (x + y) 8 x}{\left(4 x ^ {2} + y ^ {2}\right) ^ {2}} = \frac {y ^ {2} - 4 x ^ {2} - 8 x y}{\left(4 x ^ {2} + y ^ {2}\right) ^ {2}},</equation><equation>\frac {\partial P}{\partial y} = \frac {- \left(4 x ^ {2} + y ^ {2}\right) - (4 x - y) 2 y}{\left(4 x ^ {2} + y ^ {2}\right) ^ {2}} = \frac {y ^ {2} - 4 x ^ {2} - 8 x y}{\left(4 x ^ {2} + y ^ {2}\right) ^ {2}}.</equation>于是，<equation>\frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y}</equation>原点为被积函数的奇点，且包含在由 L围成的封闭区域 D内.

作辅助曲线<equation>L^{\prime}:4x^{2} + y^{2} = \varepsilon^{2}</equation>，并使<equation>\varepsilon</equation>足够小，使<equation>L^{\prime}</equation>围成的椭圆包含在<equation>L</equation>围成的圆中，其参数方程为<equation>\left\{ \begin{array}{l l} x = \frac{\varepsilon}{2}\cos t, t \text{ 从} 0 \\ y = \varepsilon \sin t, \end{array} \right.</equation>变到<equation>2\pi</equation>.如图所示，<equation>L^{\prime}</equation>的正向为逆时针方向，<equation>L^{\prime}</equation>所围成的区域记为<equation>D^{\prime}, L + L^{\prime}^{-}</equation>围成区域<equation>D\backslash D^{\prime}</equation>.被积函数在<equation>D\backslash D^{\prime}</equation>上没有奇点.

由格林公式，<equation>\oint_ {L + L ^ {\prime} -} \frac {4 x - y}{4 x ^ {2} + y ^ {2}} \mathrm {d} x + \frac {x + y}{4 x ^ {2} + y ^ {2}} \mathrm {d} y \xlongequal {\text {格 林 公 式}} \iint_ {D \backslash D ^ {\prime}} 0 \mathrm {d} x \mathrm {d} y = 0,</equation>因此，<equation>\begin{aligned} I &= \oint_ {L} \frac {4 x - y}{4 x ^ {2} + y ^ {2}} \mathrm {d} x + \frac {x + y}{4 x ^ {2} + y ^ {2}} \mathrm {d} y = \oint_ {L ^ {\prime}} \frac {4 x - y}{4 x ^ {2} + y ^ {2}} \mathrm {d} x + \frac {x + y}{4 x ^ {2} + y ^ {2}} \mathrm {d} y \\ \frac {4 x ^ {2} + y ^ {2} = \varepsilon^ {2}}{\varepsilon^ {2}} \frac {1}{\varepsilon^ {2}} \oint_ {L ^ {\prime}} (4 x - y) \mathrm {d} x + (x + y) \mathrm {d} y \xlongequal {\text {格 林 公 式}} \frac {1}{\varepsilon^ {2}} \iint_ {D ^ {\prime}} 2 \mathrm {d} x \mathrm {d} y \\ &= \frac {2}{\varepsilon^ {2}} \cdot D ^ {\prime} \text {的 面 积} = \frac {2}{\varepsilon^ {2}} \times \pi \times \frac {\varepsilon}{2} \times \varepsilon = \pi . \end{aligned}</equation>

---

**2019年第4题 | 选择题 | 4分 | 答案: D**
4. 设函数<equation>Q ( x,y )=\frac{x}{y^{2}}</equation>. 如果对上半平面（<equation>y>0</equation>）内的任意有向光滑封闭曲线 C都有<equation>\oint_{C}P(x,y)\mathrm{d}x+Q(x,y)\mathrm{d}y=0</equation>，那么函数 P(x,y)可取为（    ）

A.<equation>y-\frac{x^{2}}{y^{3}}</equation>B.<equation>\frac{1}{y}-\frac{x^{2}}{y^{3}}</equation>C.<equation>\frac{1}{x}-\frac{1}{y}</equation>D.<equation>x-\frac{1}{y}</equation>
答案: D
**解析: **解 由 Q(x,y)的表达式可知该函数在上半平面 y > 0内具有一阶连续偏导数，故若 P(x,y)满足在上半平面内具有一阶连续偏导数且<equation>\frac{\partial Q}{\partial x}\equiv \frac{\partial P}{\partial y}</equation>，则曲线积分<equation>\oint_{C}P(x,y)\mathrm{d}x+Q(x,y)\mathrm{d}y</equation>在单连通区域 y > 0内与路径无关，即对上半平面 y > 0内的任意分段光滑闭曲线 C都有<equation>\oint_{C}P(x,y)\mathrm{d}x+</equation><equation>Q(x,y)\mathrm{d}y=0.</equation>由于<equation>\frac{\partial Q}{\partial x}=\frac{1}{y^{2}}</equation>，故<equation>\frac{\partial P}{\partial y}</equation>应等于<equation>\frac{1}{y^{2}}</equation>. 选项C与选项D的函数均满足该要求. 但是选项C的函数<equation>\frac{1}{x}-\frac{1}{y}</equation>在 x = 0处无定义，从而也就不满足曲线积分与路径无关的条件.

因此，应选D.

---

**2017年第11题 | 填空题 | 4分**
11. 若曲线积分<equation>\int_ {L} \frac {x \mathrm {d} x - a y \mathrm {d} y}{x ^ {2} + y ^ {2} - 1}</equation>在区域<equation>D=\{(x,y)\mid x^{2}+y^{2}<1\}</equation>内与路径无关，则 a=___
**答案: **<equation>- 1.</equation>
**解析: **解 令<equation>P=\frac{x}{x^{2}+y^{2}-1}, Q=\frac{-ay}{x^{2}+y^{2}-1}</equation>，则<equation>\frac{\partial P}{\partial y}=\frac{-2xy}{\left(x^{2}+y^{2}-1\right)^{2}},</equation><equation>\frac{\partial Q}{\partial x}=\frac{2axy}{\left(x^{2}+y^{2}-1\right)^{2}}.</equation>又 D为单连通区域，且曲线积分与路径无关，故<equation>\frac{\partial P}{\partial y}=\frac{\partial Q}{\partial x}</equation>即<equation>\frac{-2xy}{\left(x^{2}+y^{2}-1\right)^{2}}=\frac{2axy}{\left(x^{2}+y^{2}-1\right)^{2}}</equation>从而 a=-1.

---

**2016年第17题 | 解答题 | 10分**
17. (本题满分10分）

设函数 f(x,y)满足<equation>\frac{\partial f(x,y)}{\partial x}=(2 x+1) \mathrm{e}^{2 x-y}</equation>，且 f(0,y)=y+1，<equation>L_{t}</equation>是从点（0，0）到点（1,t）的光滑曲线.计算曲线积分<equation>I(t)=\int_{L_{t}} \frac{\partial f(x,y)}{\partial x} \mathrm{d} x+\frac{\partial f(x,y)}{\partial y} \mathrm{d} y</equation>，并求 I(t)的最小值.
**答案: **##<equation>I ( t ) = \mathrm {e} ^ {2 - t} + t, I ( t )</equation>的最小值为3.
**解析: **解由<equation>\frac{\partial f(x,y)}{\partial x} = (2x+1)\mathrm{e}^{2x-y}</equation>知，<equation>\begin{aligned} f (x, y) &= \int (2 x + 1) \mathrm {e} ^ {2 x - y} \mathrm {d} x = \mathrm {e} ^ {- y} \int (2 x + 1) \mathrm {e} ^ {2 x} \mathrm {d} x \\ &= \mathrm {e} ^ {- y} \left[ \frac {1}{2} \mathrm {e} ^ {2 x} (2 x + 1) - \int \mathrm {e} ^ {2 x} \mathrm {d} x \right] \\ &= \mathrm {e} ^ {- y} \left[ \frac {1}{2} \mathrm {e} ^ {2 x} (2 x + 1) - \frac {1}{2} \mathrm {e} ^ {2 x} + \varphi_ {1} (y) \right] \\ &= x \mathrm {e} ^ {2 x - y} + \varphi_ {2} (y), \end{aligned}</equation>这里<equation>\varphi_{1}(y),\varphi_{2}(y)</equation>都是以<equation>y</equation>为自变量的待定函数，且<equation>\varphi_{2}(y) = \mathrm{e}^{-y}\varphi_{1}(y)</equation>. 由<equation>f(0,y) = y + 1</equation>得到<equation>\varphi_{2}(y) = y + 1</equation>，从而<equation>f (x, y) = x \mathrm {e} ^ {2 x - y} + y + 1.</equation>下面用两种方法求<equation>I ( t )</equation>（法一）<equation>\frac{\partial f}{\partial x} = (2x + 1)\mathrm{e}^{2x - y},\frac{\partial f}{\partial y} = -x\mathrm{e}^{2x - y} + 1</equation>在整个平面上都连续，故由定理1知，<equation>I (t) = \int_ {L _ {t}} \frac {\partial f (x , y)}{\partial x} \mathrm {d} x + \frac {\partial f (x , y)}{\partial y} \mathrm {d} y = f (1, t) - f (0, 0) = \mathrm {e} ^ {2 - t} + t.</equation>（法二）<equation>\frac{\partial^2 f}{\partial x\partial y} = \frac{\partial^2 f}{\partial y\partial x} = -(2x + 1)\mathrm{e}^{2x - y}</equation>在整个平面上连续，故由定理2知，曲线积分<equation>I(t)</equation>与路径无关.下面我们选择两条不同的路径来计算<equation>I(t)</equation>.

（a）如图，令<equation>L_{1}</equation>是从点（0,0）到点（1,0），再到点（1,t）的折线段，于是<equation>\begin{aligned} I (t) &= \int_ {L _ {1}} \frac {\partial f (x , y)}{\partial x} \mathrm {d} x + \frac {\partial f (x , y)}{\partial y} \mathrm {d} y \\ &= \int_ {0} ^ {1} \frac {\partial f (x , 0)}{\partial x} \mathrm {d} x + \int_ {0} ^ {t} \frac {\partial f (1 , y)}{\partial y} \mathrm {d} y \\ &= f (x, 0) \left| _ {x = 0} ^ {x = 1} + f (1, y) \right| _ {y = 0} ^ {y = t} \\ &= f (1, 0) - f (0, 0) + f (1, t) - f (1, 0) \\ &= f (1, t) - f (0, 0) = \mathrm {e} ^ {2 - t} + t. \end{aligned}</equation>（b）如图，令<equation>L_{2}</equation>是从点<equation>(0,0)</equation>到点<equation>(0,t)</equation>，再到点<equation>(1,t)</equation>的折线段，于是<equation>\begin{aligned} I (t) &= \int_ {L _ {2}} \frac {\partial f (x , y)}{\partial x} \mathrm {d} x + \frac {\partial f (x , y)}{\partial y} \mathrm {d} y \\ &= \int_ {0} ^ {t} \frac {\partial f (0 , y)}{\partial y} \mathrm {d} y + \int_ {0} ^ {1} \frac {\partial f (x , t)}{\partial x} \mathrm {d} x \\ &= f (0, y) \left| _ {y = 0} ^ {y = t} + f (x, t) \right| _ {x = 0} ^ {x = 1} \\ &= f (0, t) - f (0, 0) + f (1, t) - f (0, t) \\ &= f (1, t) - f (0, 0) = \mathrm {e} ^ {2 - t} + t. \end{aligned}</equation>下面求 I（t）的最小值.<equation>I^{\prime}(t) = 1 - \mathrm{e}^{2 - t}.</equation>令<equation>I^{\prime}(t) = 0</equation>，解得<equation>t = 2</equation>当<equation>t > 2</equation>时，<equation>I^{\prime}(t) > 0</equation>，于是<equation>I(t)</equation>在<equation>[2, +\infty)</equation>上单调增加；当<equation>t < 2</equation>时，<equation>I^{\prime}(t) < 0</equation>，于是<equation>I(t)</equation>在<equation>(-\infty ,2]</equation>上单调减少，从而<equation>t = 2</equation>为<equation>I(t)</equation>的最小值点，最小值为<equation>I (2) = \mathrm {e} ^ {2 - 2} + 2 = 3.</equation>

---

**2015年第19题 | 解答题 | 10分**
19. (本题满分10分)

已知曲线 L的方程为<equation>\left\{\begin{array}{l l}z=\sqrt{2-x^{2}-y^{2}},\\ z=x, \end{array} \right.</equation>起点为 A(0,<equation>\sqrt{2},0)</equation>，终点为 B(0，<equation>-\sqrt{2},0)</equation>，请计算曲线积分 I=<equation>\int_{L}(y+z)\mathrm{d}x+(z^{2}-x^{2}+y)\mathrm{d}y+x^{2}y^{2}\mathrm{d}z.</equation>
**答案: **<equation>(1 9) I = \frac {\sqrt {2}}{2} \pi .</equation>
**解析: **解（法一）<equation>L</equation>的方程<equation>\left\{\begin{array}{l l}z=\sqrt{2-x^{2}-y^{2}},\\ z=x\end{array}\right.</equation>可化为<equation>\left\{\begin{array}{l l}x^{2}+\frac{y^{2}}{2}=1,\\ z=x\geqslant 0, \end{array}\right.</equation>于是参数方程为<equation>\left\{\begin{array}{l l}x=\cos \theta ,\\ y=\sqrt{2}\sin \theta ,\\ z=\cos \theta , \end{array}\right.</equation><equation>\theta \in\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>且L的起点A对应<equation>\theta =\frac{\pi}{2}</equation>终点对应参数<equation>\theta=-\frac{\pi}{2}</equation>从而<equation>\begin{aligned} I &= \int_ {- \frac {\pi}{2}} ^ {- \frac {\pi}{2}} \left[ (\sqrt {2} \sin \theta + \cos \theta) \cdot (- \sin \theta) + \sqrt {2} \sin \theta \cdot \sqrt {2} \cos \theta + 2 \sin^ {2} \theta \cos^ {2} \theta \cdot (- \sin \theta) \right] d \theta \\ &= \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \left(\sqrt {2} \sin^ {2} \theta - \sin \theta \cos \theta + 2 \sin^ {3} \theta \cos^ {2} \theta\right) d \theta \\ \underline {{\text {对称性}}} 2 \sqrt {2} \int_ {0} ^ {\frac {\pi}{2}} \sin^ {2} \theta \mathrm {d} \theta - 0 + 0 \\ &= \sqrt {2} \int_ {0} ^ {\frac {\pi}{2}} (1 - \cos 2 \theta) \mathrm {d} \theta = \frac {\sqrt {2}}{2} \pi . \end{aligned}</equation>（法二）利用斯托克斯公式.

设<equation>L_{1}</equation>是从点B到点A的直线段，<equation>\Sigma</equation>为平面<equation>z=x</equation>上由L与<equation>L_{1}</equation>围成的半圆面下侧，其面积为<equation>\pi</equation>单位法向量为<equation>\left(\frac{1}{\sqrt{2}},0,-\frac{1}{\sqrt{2}}\right).</equation>由斯托克斯公式知，<equation>\begin{aligned} \oint_ {L + L _ {1}} (y + z) \mathrm {d} x + \left(z ^ {2} - x ^ {2} + y\right) \mathrm {d} y + x ^ {2} y ^ {2} \mathrm {d} z &= \iint_ {\Sigma} \left| \begin{array}{c c c} \frac {1}{\sqrt {2}} & 0 & - \frac {1}{\sqrt {2}} \\ \frac {\partial}{\partial x} & \frac {\partial}{\partial y} & \frac {\partial}{\partial z} \\ y + z & z ^ {2} - x ^ {2} + y & x ^ {2} y ^ {2}  \right| \mathrm {d} S \\ &= \frac {1}{\sqrt {2}} \iint_ {\Sigma} \left(2 x ^ {2} y + 1\right) \mathrm {d} S. \end{aligned}</equation>由于曲面<equation>\varSigma</equation>关于 xOz平面对称，且函数<equation>2x^{2}y</equation>是关于 y的奇函数，故<equation>\iint\limits_{S}2x^{2}y\mathrm{d}S=0</equation>从而<equation>\oint_ {L + L _ {1}} (y + z) \mathrm {d} x + \left(z ^ {2} - x ^ {2} + y\right) \mathrm {d} y + x ^ {2} y ^ {2} \mathrm {d} z = \frac {1}{\sqrt {2}} \iint_ {\Sigma} \mathrm {d} S = \frac {1}{\sqrt {2}} \cdot \Sigma \text {的 面 积} = \frac {\sqrt {2}}{2} \pi .</equation>又在<equation>L_{1}</equation>上，<equation>x = 0,z = 0,y</equation>从<equation>-\sqrt{2}</equation>变到<equation>\sqrt{2}</equation>，故<equation>\int_ {L _ {1}} (y + z) \mathrm {d} x + \left(z ^ {2} - x ^ {2} + y\right) \mathrm {d} y + x ^ {2} y ^ {2} \mathrm {d} z = \int_ {- \sqrt {2}} ^ {\sqrt {2}} y \mathrm {d} y = 0.</equation>因此，<equation>I=\frac{\sqrt{2}}{2}\pi -0=\frac{\sqrt{2}}{2}\pi.</equation>

---

**2014年第12题 | 填空题 | 4分**
12. 设 L是柱面<equation>x^{2}+y^{2}=1</equation>与平面 y+z=0的交线，从 z轴正向往 z轴负向看去为逆时针方向，则曲线积分<equation>\oint_{L} z \mathrm{d} x+y \mathrm{d} z=</equation>___
**解析: **解（法一）<equation>L</equation>的方程为<equation>\left\{ \begin{array}{l l} x^{2} + y^{2} = 1, \\ y + z = 0, \end{array} \right.</equation>其参数方程为<equation>\left\{ \begin{array}{l l} x = \cos \theta , \\ y = \sin \theta , \theta \text {从} 0 \text {变到} 2 \pi . \text {于是} \\ z = -\sin \theta , \end{array} \right.</equation><equation>\begin{aligned} \oint_ {L} z \mathrm {d} x + y \mathrm {d} z &= \int_ {0} ^ {2 \pi} \left[ (- \sin \theta) \cdot (- \sin \theta) + \sin \theta \cdot (- \cos \theta) \right] \mathrm {d} \theta \\ &= \int_ {0} ^ {2 \pi} \left(\sin^ {2} \theta - \sin \theta \cos \theta\right) \mathrm {d} \theta = \int_ {0} ^ {2 \pi} \left(\frac {1 - \cos 2 \theta}{2} - \frac {\sin 2 \theta}{2}\right) \mathrm {d} \theta = \pi . \end{aligned}</equation>（法二）设曲面<equation>\varSigma</equation>是平面<equation>y+z=0</equation>上由L围成的区域的内侧，即<equation>\varSigma=\{(x,y,z)\mid x^{2}+y^{2}\leqslant1,</equation><equation>y+z=0\}</equation><equation>\varSigma</equation>的单位法向量为<equation>(\cos \alpha ,\cos \beta ,\cos \gamma)=\frac{1}{\sqrt{2}}(0,1,1),\varSigma</equation>在xOy面上的投影区域为<equation>D_{xy}=\{(x,y)\mid x^{2}+y^{2}\leqslant 1\}</equation>，其面积为<equation>\pi</equation>.由斯托克斯公式知，<equation>\oint_ {L} z \mathrm {d} x + y \mathrm {d} z = \iint_ {\Sigma} \left| \begin{array}{c c c} 0 & \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {2}} \\ \frac {\partial}{\partial x} & \frac {\partial}{\partial y} & \frac {\partial}{\partial z} \\ z & 0 & y \end{array} \right| \mathrm {d} S = \iint_ {\Sigma} \frac {1}{\sqrt {2}} \mathrm {d} S = \iint_ {\Sigma} \cos \gamma \mathrm {d} S = \iint_ {D _ {x y}} \mathrm {d} x \mathrm {d} y = \pi .</equation>

---

**2013年第4题 | 选择题 | 4分 | 答案: D**
4. 设<equation>L_{1}:x^{2}+y^{2}=1</equation><equation>L_{2}:x^{2}+y^{2}=2</equation><equation>L_{3}:x^{2}+2y^{2}=2</equation><equation>L_{4}:2x^{2}+y^{2}=2</equation>为四条逆时针方向的平面曲线.记<equation>I_{i}=\oint_{L_{i}}\left(y+\frac{y^{3}}{6}\right)\mathrm{d}x+\left(2x-\frac{x^{3}}{3}\right)\mathrm{d}y(i=1,2,3,4)</equation>，则<equation>\max \left\{ I_{1}, I_{2}, I_{3}, I_{4} \right\}=</equation>(    )

A.<equation>I_{1}</equation>B.<equation>I_{2}</equation>C.<equation>I_{3}</equation>D.<equation>I_{4}</equation>
答案: D
**解析: **解（法一）题设中所给的积分弧段均为闭曲线，由格林公式可知，<equation>\begin{aligned} I _ {i} &= \oint_ {L _ {i}} \left(y + \frac {y ^ {3}}{6}\right) \mathrm {d} x + \left(2 x - \frac {x ^ {3}}{3}\right) \mathrm {d} y = \iint_ {D _ {i}} \left(1 - x ^ {2} - \frac {y ^ {2}}{2}\right) \mathrm {d} x \mathrm {d} y \\ &= \frac {1}{2} \iint_ {D _ {i}} \left(2 - 2 x ^ {2} - y ^ {2}\right) \mathrm {d} x \mathrm {d} y, \end{aligned}</equation>其中<equation>D_{i}</equation>为<equation>L_{i}</equation>围成的区域.显然在<equation>D_{4}</equation>内<equation>2-2 x^{2}-y^{2}>0</equation>，在<equation>D_{4}</equation>外<equation>2-2 x^{2}-y^{2}<0</equation>，由重积分对积分区域的可加性及重积分的保号性知，<equation>\begin{array}{l} I _ {4} - I _ {1} = \frac {1}{2} \iint_ {D _ {4} - D _ {1}} \left(2 - 2 x ^ {2} - y ^ {2}\right) \mathrm {d} x \mathrm {d} y > 0 \quad \left(D _ {4} \supset D _ {1}\right), \\ I _ {4} - I _ {2} = - \frac {1}{2} \iint_ {D _ {2} - D _ {4}} \left(2 - 2 x ^ {2} - y ^ {2}\right) \mathrm {d} x \mathrm {d} y > 0 \quad \left(D _ {2} \supset D _ {4}\right), \\ I _ {4} - I _ {3} = \frac {1}{2} \left[ \iint_ {D _ {4} - D _ {3}} \left(2 - 2 x ^ {2} - y ^ {2}\right) \mathrm {d} x \mathrm {d} y - \iint_ {D _ {3} - D _ {4}} \left(2 - 2 x ^ {2} - y ^ {2}\right) \mathrm {d} x \mathrm {d} y \right] > 0 \quad (\text {第一 项 大 于} 0, \text {第二 项 小 于} 0). \\ \text {因此}, \max \left\{I _ {1}, I _ {2}, I _ {3}, I _ {4} \right\} = I _ {4}, \text {选} D. \\ \end{array}</equation>（法二）利用圆与椭圆的参数方程将第二类曲线积分直接化为定积分后再计算，其中<equation>L_{1}</equation>的参数方程为<equation>\left\{ \begin{array}{l l} x = \cos \theta , \\ y = \sin \theta \end{array} \right.</equation><equation>(0 \leqslant \theta \leqslant 2\pi), L_{2}</equation>的参数方程为<equation>\left\{ \begin{array}{l l} x = \sqrt{2}\cos \theta , \\ y = \sqrt{2}\sin \theta \end{array} \right.</equation><equation>(0 \leqslant \theta \leqslant 2\pi), L_{3}</equation>的参数方程为<equation>\left\{ \begin{array}{l l} x = \sqrt{2}\cos \theta , \\ y = \sin \theta \end{array} \right.</equation><equation>(0 \leqslant \theta \leqslant 2\pi), L_{4}</equation>的参数方程为<equation>\left\{ \begin{array}{l l} x = \cos \theta , \\ y = \sqrt{2}\sin \theta \end{array} \right.</equation><equation>(0 \leqslant \theta \leqslant 2\pi)</equation>.

将参数方程代入曲线积分，计算得到<equation>I_{1}=\frac{5}{8}\pi, I_{2}=\frac{1}{2}\pi, I_{3}=\frac{3\sqrt{2}}{8}\pi, I_{4}=\frac{\sqrt{2}}{2}\pi.</equation>故<equation>\max \left\{ I_{1}, I_{2}, I_{3}, I_{4} \right\}=I_{4}</equation>，选D.

---

**2012年第19题 | 解答题 | 10分**
19. (本题满分10分)

已知 L是第一象限中从点（0,0）沿圆周<equation>x^{2}+y^{2}=2 x</equation>到点（2,0），再沿圆周<equation>x^{2}+y^{2}=4</equation>到点（0,2）的曲线段，计算曲线积分<equation>I=\int_{L}3x^{2}y\mathrm{d}x+(x^{3}+x-2y)\mathrm{d}y.</equation>
**解析: **解记<equation>L_{3}</equation>为y轴上从点（0,2）到点（0,0）的有向线段.<equation>D = \{(x,y) \mid 0 \leqslant x \leqslant 2, \sqrt{2x - x^2} \leqslant y \leqslant \sqrt{4 - x^2}\}</equation>，则由格林公式知，<equation>\begin{aligned} \int_ {L + L _ {3}} 3 x ^ {2} y \mathrm {d} x + \left(x ^ {3} + x - 2 y\right) \mathrm {d} y &= \iint_ {D} \left(3 x ^ {2} + 1 - 3 x ^ {2}\right) \mathrm {d} x \mathrm {d} y \\ &= \iint_ {D} \mathrm {d} x \mathrm {d} y = \frac {\pi \cdot 2 ^ {2}}{4} - \frac {\pi \cdot 1 ^ {2}}{2} = \frac {\pi}{2}. \end{aligned}</equation><equation>I = \frac {\pi}{2} - 4.</equation>

---

**2011年第12题 | 填空题 | 4分**
12. 设 L是柱面<equation>x^{2}+y^{2}=1</equation>与平面 z=x+y的交线，从 z轴正向往 z轴负向看去为逆时针方向，则曲线积分<equation>\oint_{L} x z \mathrm{d} x+x \mathrm{d} y+\frac{y^{2}}{2} \mathrm{d} z=</equation>___
**解析: **解（法一）曲线 L的参数方程为<equation>\left\{ \begin{array}{l l} x=\cos \theta , \\ y=\sin \theta , \\ z=\sin \theta +\cos \theta \end{array} \right.</equation>（<equation>0\leqslant \theta \leqslant 2\pi</equation>），于是<equation>\begin{aligned} \oint_ {L} x z \mathrm {d} x + x \mathrm {d} y + \frac {y ^ {2}}{2} \mathrm {d} z &= \int_ {0} ^ {2 \pi} \left[ \cos \theta (\sin \theta + \cos \theta) (- \sin \theta) + \cos^ {2} \theta + \frac {\sin^ {2} \theta}{2} (\cos \theta - \sin \theta) \right] \mathrm {d} \theta \\ &= \int_ {0} ^ {2 \pi} \left(\cos^ {2} \theta - \frac {1}{2} \sin^ {2} \theta \cos \theta - \cos^ {2} \theta \sin \theta - \frac {\sin^ {3} \theta}{2}\right) \mathrm {d} \theta \\ &= \int_ {0} ^ {2 \pi} \frac {1 + \cos 2 \theta}{2} \mathrm {d} \theta - \frac {1}{2} \int_ {0} ^ {2 \pi} \sin^ {2} \theta \mathrm {d} (\sin \theta) + \int_ {0} ^ {2 \pi} \cos^ {2} \theta \mathrm {d} (\cos \theta) \\ + \frac {1}{2} \int_ {0} ^ {2 \pi} \left(1 - \cos^ {2} \theta\right) \mathrm {d} (\cos \theta) \\ &= \pi - \frac {1}{2} \cdot \frac {\sin^ {3} \theta}{3} \Big | _ {0} ^ {2 \pi} + \frac {\cos^ {3} \theta}{3} \Big | _ {0} ^ {2 \pi} + \frac {1}{2} \left(\cos \theta - \frac {\cos^ {3} \theta}{3}\right) \Big | _ {0} ^ {2 \pi} \\ &= \pi - 0 + 0 + 0 = \pi . \end{aligned}</equation>（法二）如图所示，记<equation>\Sigma</equation>为<equation>L</equation>围成的平面区域的上侧，即<equation>\Sigma = \{(x,y,z) \mid z = x + y, x^2 + y^2 \leqslant 1\}</equation>，则<equation>\Sigma</equation>在<equation>xOy</equation>面上的投影区域为<equation>D_{xy} = \{(x,y) \mid x^2 + y^2 \leqslant 1\}</equation>，<equation>\Sigma</equation>的单位法向量为<equation>(\cos \alpha ,\cos \beta ,\cos \gamma) =</equation><equation>\left(-\frac{1}{\sqrt{3}},-\frac{1}{\sqrt{3}},\frac{1}{\sqrt{3}}\right).</equation>由斯托克斯公式知<equation>\begin{aligned} \oint_ {L} x z \mathrm {d} x + x \mathrm {d} y + \frac {y ^ {2}}{2} \mathrm {d} z &= \iint_ {\Sigma} \left| \begin{array}{c c c} - \frac {1}{\sqrt {3}} & - \frac {1}{\sqrt {3}} & \frac {1}{\sqrt {3}} \\ \frac {\partial}{\partial x} & \frac {\partial}{\partial y} & \frac {\partial}{\partial z} \\ x z & x & \frac {y ^ {2}}{2}  \right| \mathrm {d} S &= \iint_ {\Sigma} \frac {1}{\sqrt {3}} (1 - x - y) \mathrm {d} S \\ &= \iint_ {\Sigma} (1 - x - y) \cos \gamma \mathrm {d} S = \iint_ {D _ {x y}} (1 - x - y) \mathrm {d} x \mathrm {d} y \\ \frac {\text {对称 性}}{} \iint_ {D _ {x y}} \mathrm {d} x \mathrm {d} y - 0 - 0 \\ &= \pi . \end{aligned}</equation>

---

**2010年第11题 | 填空题 | 4分**
11. 已知曲线 L的方程为<equation>y=1-|x|</equation><equation>x\in[-1,1]</equation>，起点是（-1，0），终点为（1，0），则曲线积分<equation>\int_{L} xy\mathrm{d}x+x^{2}\mathrm{d}y=</equation>
**解析: **<equation>\begin{aligned} \int_ {L} x y \mathrm {d} x + x ^ {2} \mathrm {d} y &= \int_ {L _ {2}} x y \mathrm {d} x + x ^ {2} \mathrm {d} y + \int_ {L _ {3}} x y \mathrm {d} x + x ^ {2} \mathrm {d} y \\ &= \int_ {- 1} ^ {0} \left[ x (1 + x) + x ^ {2} \right] \mathrm {d} x + \int_ {0} ^ {1} \left[ x (1 - x) - x ^ {2} \right] \mathrm {d} x \\ &= \int_ {- 1} ^ {0} \left(x + 2 x ^ {2}\right) \mathrm {d} x + \int_ {0} ^ {1} \left(x - 2 x ^ {2}\right) \mathrm {d} x = \frac {1}{6} - \frac {1}{6} = 0. \end{aligned}</equation>分析 本题主要考查第二类曲线积分的计算. 可以先补线再利用格林公式，也可以直接将曲线 L的方程代入被积函数进行计算.

格林公式 设闭区域 D由分段光滑的曲线 L围成，若函数 P（x,y）及 Q（x,y）在 D上具有一阶连续偏导数，则有<equation>\iint_ {D} \left(\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y}\right) \mathrm {d} x \mathrm {d} y = \oint_ {L} P \mathrm {d} x + Q \mathrm {d} y,</equation>其中 L是 D的取正向的边界曲线.（一定要注意 L的方向，若方向相反，则多一个负号.）

参数法 若曲线 L的参数方程为<equation>\left\{\begin{array}{l l}x=\varphi (t),\\ y=\psi (t),\end{array}\right.</equation>起点A对应参数<equation>\alpha</equation>，终点B对应参数<equation>\beta</equation>（注意<equation>\beta</equation>不一定大于<equation>\alpha</equation>），如果<equation>P(x,y),Q(x,y)</equation>均在 L上连续，<equation>\varphi^{\prime}(t),\psi^{\prime}(t)</equation>也连续且<equation>[\varphi^{\prime}(t)]^{2}+[ \psi^{\prime}(t)]^{2}\neq 0</equation>则<equation>\begin{aligned} \int_ {L = \widehat {A B}} P (x, y) \mathrm {d} x + Q (x, y) \mathrm {d} y \\ &= \int_ {\alpha} ^ {\beta} \left[ P \left(\varphi (t), \psi (t)\right) \varphi^ {\prime} (t) + Q \left(\varphi (t), \psi (t)\right) \psi^ {\prime} (t) \right] \mathrm {d} t. \end{aligned}</equation>解（法一）如图所示，记<equation>L_{1}:y=0(-1\leqslant x\leqslant 1)</equation>，起点是（1，0），终点是（-1，0），D为L和<equation>L_{1}</equation>围成的区域，则由格林公式知<equation>\begin{aligned} \int_ {L + L _ {1}} x y \mathrm {d} x + x ^ {2} \mathrm {d} y &= - \iint_ {D} \left[ \frac {\partial \left(x ^ {2}\right)}{\partial x} - \frac {\partial \left(x y\right)}{\partial y} \right] \mathrm {d} x \mathrm {d} y \\ \frac {\mathrm {对称 性}}{} - \iint_ {D} x \mathrm {d} x \mathrm {d} y &= 0. \end{aligned}</equation>因此，<equation>\int_ {L} x y \mathrm {d} x + x ^ {2} \mathrm {d} y = - \int_ {L _ {1}} x y \mathrm {d} x + x ^ {2} \mathrm {d} y = - \int_ {1} ^ {- 1} 0 \mathrm {d} x + 0 = 0.</equation>（法二）如图所示，记<equation>L_{2}:y=1+x(-1\leqslant x\leqslant 0)</equation>，起点是（-1，0），终点是（0，1），<equation>L_{3}:y=1-x(0\leqslant</equation><equation>x\leqslant 1)</equation>，起点是（0，1），终点是（1，0），则

---


#### 第二类曲面积分

**2025年第20题 | 解答题 | 12分**
20. 设<equation>\Sigma</equation>是由直线<equation>\left\{\begin{array}{l l}x=0\\ y=0\end{array}\right.</equation>，绕直线<equation>\left\{\begin{array}{l l}x=t\\ y=t\\ z=t\end{array}\right.</equation>（t为参数）旋转一周得到的曲面，<equation>\Sigma_{1}</equation>是<equation>\Sigma</equation>介于平面 x+y+z=0与平面 x+y+z=1之间部分的外侧，计算曲面积分<equation>I=\iint_{\Sigma_{1}}x\mathrm{d}y\mathrm{d}z+(y+1)\mathrm{d}z\mathrm{d}x+(z+2)\mathrm{d}x\mathrm{d}y.</equation>
**解析: **解直线<equation>\left\{\begin{array}{l l}x=0\\ y=0\end{array}\right.</equation>可视为z轴，直线<equation>\left\{\begin{array}{l l}x=t,\\ y=t,\\ z=t\end{array}\right.</equation>（t为参数）是以（1，1，1）为方向向量且过原点的直

线，故<equation>\varSigma</equation>是以原点为顶点，直线<equation>\frac{x}{1}=\frac{y}{1}=\frac{z}{1}</equation>为轴（圆锥底面上的高所在直线），且过点（1，0，0），（0，1，0），（0，0，1）的圆锥面.

如图所示，记<equation>\Sigma_{2}</equation>为平面<equation>x + y + z = 1</equation>被<equation>\Sigma</equation>所截得的有限部分，取上侧，则<equation>\Sigma_{1}</equation>与<equation>\Sigma_{2}</equation>共同围成一个圆锥体<equation>\Omega ,\Sigma_{1}\cup \Sigma_{2}</equation>构成<equation>\Omega</equation>的外侧.

圆锥体的底面圆心为平面<equation>x + y + z = 1</equation>与直线<equation>x = y = z</equation>的交点，解得<equation>x = y = z = \frac{1}{3}</equation>，即底面圆心为<equation>\left(\frac{1}{3}, \frac{1}{3}, \frac{1}{3}\right)</equation>. 底面圆的半径为点(0,0,1)

到点<equation>\left(\frac{1}{3},\frac{1}{3},\frac{1}{3}\right)</equation>的距离，即<equation>\sqrt{\frac{1}{9} + \frac{1}{9} + \frac{4}{9}} = \sqrt{\frac{2}{3}}.</equation>圆锥体的高为点（0,0,0）到点<equation>\left(\frac{1}{3},\frac{1}{3},\frac{1}{3}\right)</equation>的距离，即<equation>\sqrt{\frac{1}{9} + \frac{1}{9} + \frac{1}{9}} = \sqrt{\frac{1}{3}}.</equation>于是，<equation>\varOmega</equation>的体积<equation>V = \frac{1}{3}\cdot \frac{2\pi}{3}\cdot \sqrt{\frac{1}{3}} = \frac{2\sqrt{3}\pi}{27}.</equation>根据高斯公式，<equation>\iint_ {\Sigma_ {1} \cup \Sigma_ {2}} x \mathrm {d} y \mathrm {d} z + (y + 1) \mathrm {d} z \mathrm {d} x + (z + 2) \mathrm {d} x \mathrm {d} y = 3 \iiint_ {\Omega} \mathrm {d} v = \frac {2 \sqrt {3} \pi}{9}.</equation>于是，<equation>\iint_ {\Sigma_ {1}} x \mathrm {d} y \mathrm {d} z + (y + 1) \mathrm {d} z \mathrm {d} x + (z + 2) \mathrm {d} x \mathrm {d} y = \frac {2 \sqrt {3} \pi}{9} - \iint_ {\Sigma_ {2}} x \mathrm {d} y \mathrm {d} z + (y + 1) \mathrm {d} z \mathrm {d} x + (z + 2) \mathrm {d} x \mathrm {d} y.</equation>下面计算<equation>\iint\limits_{\Sigma_{2}}x\mathrm{d}y\mathrm{d}z+(y+1)\mathrm{d}z\mathrm{d}x+(z+2)\mathrm{d}x\mathrm{d}y.</equation>由于<equation>\varSigma_{2}</equation>的法向量（1，1，1）的方向余弦<equation>\cos \alpha=\cos \beta=\cos \gamma=\frac{1}{\sqrt{3}}</equation>，故<equation>\mathrm{d}y\mathrm{d}z=\mathrm{d}z\mathrm{d}x=\mathrm{d}x\mathrm{d}y</equation><equation>\begin{aligned} \iint_ {\Sigma_ {2}} x \mathrm {d} y \mathrm {d} z + (y + 1) \mathrm {d} z \mathrm {d} x + (z + 2) \mathrm {d} x \mathrm {d} y \xlongequal {z = 1 - x - y} \iint_ {\Sigma_ {2}} x \mathrm {d} y \mathrm {d} z + (y + 1) \mathrm {d} z \mathrm {d} x + (3 - x - y) \mathrm {d} x \mathrm {d} y \\ &= \iint_ {\Sigma_ {2}} 4 \mathrm {d} x \mathrm {d} y = \frac {4}{\sqrt {3}} \iint_ {\Sigma_ {2}} \mathrm {d} S = \frac {4}{\sqrt {3}} \Sigma_ {2} \text {的 面 积}. \end{aligned}</equation>又因为<equation>\varSigma_{2}</equation>的面积即圆锥体的底面圆面积，所以<equation>\iint_ {\Sigma_ {2}} x \mathrm {d} y \mathrm {d} z + (y + 1) \mathrm {d} z \mathrm {d} x + (z + 2) \mathrm {d} x \mathrm {d} y = \frac {4}{\sqrt {3}} \cdot \frac {2 \pi}{3} = \frac {8 \sqrt {3} \pi}{9}.</equation>因此，<equation>\iint_ {\Sigma_ {1}} x \mathrm {d} y \mathrm {d} z + (y + 1) \mathrm {d} z \mathrm {d} x + (z + 2) \mathrm {d} x \mathrm {d} y = \frac {2 \sqrt {3} \pi}{9} - \frac {8 \sqrt {3} \pi}{9} = - \frac {2 \sqrt {3} \pi}{3}.</equation>

---

**2024年第2题 | 选择题 | 5分 | 答案: A**
2. 设<equation>P=P(x,y,z), Q=Q(x,y,z)</equation>均为连续函数，<equation>\Sigma</equation>为曲面<equation>z=\sqrt{1-x^{2}-y^{2}}</equation><equation>( x \leqslant0, y \geqslant0)</equation>的上侧，则<equation>\iint\limits_{\Sigma} P\mathrm{d}y\mathrm{d}z+ Q\mathrm{d}z\mathrm{d}x=</equation>(    )

A.<equation>\iint\limits_{\Sigma} \left( \frac{x}{z} P+\frac{y}{z} Q \right) \mathrm{d}x\mathrm{d}y</equation>B.<equation>\iint\limits_{\Sigma} \left( -\frac{x}{z} P+\frac{y}{z} Q \right) \mathrm{d}x\mathrm{d}y</equation>C.<equation>\iint\limits_{\Sigma} \left( \frac{x}{z} P-\frac{y}{z} Q \right) \mathrm{d}x\mathrm{d}y</equation>D.<equation>\iint\limits_{\Sigma} \left( -\frac{x}{z} P-\frac{y}{z} Q \right) \mathrm{d}x\mathrm{d}y</equation>
答案: A
**解析: **解 由于曲面<equation>\varSigma</equation>取上侧，故<equation>\varSigma</equation>的法向量与z轴正向成锐角，从而<equation>\varSigma</equation>的法向量<equation>n=(-z_{x}^{\prime},-z_{y}^{\prime},1)</equation>的方向余弦为<equation>\cos \alpha = \frac {- z _ {x} ^ {\prime}}{\sqrt {1 + z _ {x} ^ {\prime 2} + z _ {y} ^ {\prime 2}}}, \quad \cos \beta = \frac {- z _ {y} ^ {\prime}}{\sqrt {1 + z _ {x} ^ {\prime 2} + z _ {y} ^ {\prime 2}}}, \quad \cos \gamma = \frac {1}{\sqrt {1 + z _ {x} ^ {\prime 2} + z _ {y} ^ {\prime 2}}}.</equation>由方向余弦的表达式可得，<equation>\cos \alpha=-z_{x}^{\prime}\cos \gamma, \cos \beta=-z_{y}^{\prime}\cos \gamma</equation>，从而<equation>\mathrm {d} y \mathrm {d} z = \cos \alpha \mathrm {d} S = - z _ {x} ^ {\prime} \cos \gamma \mathrm {d} S = - z _ {x} ^ {\prime} \mathrm {d} x \mathrm {d} y, \mathrm {d} z \mathrm {d} x = \cos \beta \mathrm {d} S = - z _ {y} ^ {\prime} \cos \gamma \mathrm {d} S = - z _ {y} ^ {\prime} \mathrm {d} x \mathrm {d} y.</equation>计算得<equation>z _ {x} ^ {\prime} = \frac {- x}{\sqrt {1 - x ^ {2} - y ^ {2}}} = - \frac {x}{z}, \quad z _ {y} ^ {\prime} = \frac {- y}{\sqrt {1 - x ^ {2} - y ^ {2}}} = - \frac {y}{z}.</equation>于是，<equation>\iint_ {\Sigma} P \mathrm {d} y \mathrm {d} z + Q \mathrm {d} z \mathrm {d} x = \iint_ {\Sigma} \left[ P \cdot \left(- z _ {x} ^ {\prime}\right) + Q \cdot \left(- z _ {y} ^ {\prime}\right) \right] \mathrm {d} x \mathrm {d} y = \iint_ {\Sigma} \left(\frac {x}{z} P + \frac {y}{z} Q\right) \mathrm {d} x \mathrm {d} y.</equation>因此，应选A.

---

**2023年第19题 | 解答题 | 12分**
19. (本题满分12分)

设空间有界区域<equation>\Omega</equation>由柱面<equation>x^{2}+y^{2}=1</equation>与平面 z=0和 x+z=1围成，<equation>\Sigma</equation>为<equation>\Omega</equation>边界曲面的外侧，计算曲面积分<equation>I=\iint_{\Sigma}2xz\mathrm{d}y\mathrm{d}z+xz\cos y\mathrm{d}z\mathrm{d}x+3yz\sin x\mathrm{d}x\mathrm{d}y.</equation>
**答案: **#<equation>I = \frac{5\pi}{4}.</equation>
**解析: **由于<equation>\varSigma</equation>为封闭曲面，且被积函数在<equation>\varOmega</equation>上具有一阶连续偏导数，故可以考虑直接利用高斯公式将第二类曲面积分转化为三重积分.

解 由高斯公式可知，<equation>I = \iiint_ {\Omega} \left(2 z - x z \sin y + 3 y \sin x\right) \mathrm {d} v.</equation>区域<equation>\varOmega</equation>如图所示.注意到<equation>\varOmega</equation>关于zOx面对称，而<equation>xz\sin y</equation>和3ysin x均为关于y的奇函数，故由对称性的结论可知，<equation>\iiint_ {\Omega} \left(2 z - x z \sin y + 3 y \sin x\right) \mathrm {d} v \xlongequal {\text {对称性}} \iiint_ {\Omega} 2 z \mathrm {d} v.</equation>采用先单后重的积分次序.由于<equation>\varOmega</equation>在 xOy面上的投影区域<equation>D=\{(x,y)\mid x^{2}+y^{2}\leqslant 1\}</equation>，D关于坐标轴均对称，且关于变量x,y具有轮换对称性，故<equation>\begin{aligned} \iiint_ {\Omega} 2 z \mathrm {d} v &= \iint_ {D} \mathrm {d} x \mathrm {d} y \int_ {0} ^ {1 - x} 2 z \mathrm {d} z = \iint_ {D} (1 - x) ^ {2} \mathrm {d} x \mathrm {d} y \xlongequal {\text {对称性}} \iint_ {D} \left(1 + x ^ {2}\right) \mathrm {d} x \mathrm {d} y \\ &= \pi + \iint_ {D} x ^ {2} \mathrm {d} x \mathrm {d} y \xlongequal {\text {轮换对称性}} \pi + \frac {1}{2} \iint_ {D} \left(x ^ {2} + y ^ {2}\right) \mathrm {d} x \mathrm {d} y \\ \xlongequal {\text {极 坐 标}} \pi + \frac {1}{2} \int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {0} ^ {1} r ^ {2} \cdot r \mathrm {d} r &= \pi + \frac {\pi}{4} = \frac {5 \pi}{4}. \end{aligned}</equation>

---

**2021年第14题 | 填空题 | 5分**
14. 设<equation>\Sigma</equation>为空间区域<equation>\left\{(x,y,z)\mid x^{2}+4 y^{2}\leqslant 4,0\leqslant z\leqslant 2\right\}</equation>表面的外侧，则曲面积分<equation>\iint\limits_{\Sigma} x^{2}\mathrm{d}y\mathrm{d}z+y^{2}\mathrm{d}z\mathrm{d}x+z\mathrm{d}x\mathrm{d}y=</equation>
**解析: **解空间区域<equation>\varOmega=\left\{(x,y,z)\mid x^{2}+4 y^{2}\leqslant 4,0\leqslant z\leqslant 2\right\}</equation>为椭圆柱面<equation>x^{2}+4 y^{2}=4</equation>，平面z=0以及z=2围成的区域，是一个椭圆柱体.该柱体的底面为椭圆区域<equation>\left\{(x,y)\left| \frac{x^{2}}{4}+y^{2}\leqslant 1\right.\right\}</equation>，面积为<equation>2\pi</equation>，柱体的高为2.<equation>\varSigma</equation>为<equation>\varOmega</equation>的外侧边界.

对曲面积分<equation>\iint_{\Sigma} x^{2}\mathrm{d}y\mathrm{d}z + y^{2}\mathrm{d}z\mathrm{d}x + z\mathrm{d}x\mathrm{d}y</equation>使用高斯公式可得，<equation>\iint_ {\Sigma} x ^ {2} \mathrm {d} y \mathrm {d} z + y ^ {2} \mathrm {d} z \mathrm {d} x + z \mathrm {d} x \mathrm {d} y = \iiint_ {\Omega} (2 x + 2 y + 1) \mathrm {d} v.</equation>由于<equation>\varOmega</equation>关于<equation>yOz</equation>面，<equation>zOx</equation>面均对称，故<equation>\iiint_{\varOmega} x\mathrm{d}v = 0,</equation><equation>\iiint_{\varOmega} y\mathrm{d}v = 0.</equation><equation>\iiint_ {\Omega} (2 x + 2 y + 1) \mathrm {d} v = \iiint_ {\Omega} \mathrm {d} v = \Omega \text {的 体 积} = 2 \pi \times 2 = 4 \pi .</equation>

---

**2020年第18题 | 解答题 | 10分**
18. (本题满分10分)

设<equation>\Sigma</equation>为曲面<equation>z=\sqrt{x^{2}+y^{2}}</equation><equation>(1\leqslant x^{2}+y^{2}\leqslant 4)</equation>的下侧，f(x)是连续函数，计算<equation>I=\iint\limits_{\Sigma}[xf(xy)+2x-y]\mathrm{d}y\mathrm{d}z+[yf(xy)+2y+x]\mathrm{d}z\mathrm{d}x+[zf(xy)+z]\mathrm{d}x\mathrm{d}y.</equation>
**答案: **<equation>I = \frac {1 4 \pi}{3}.</equation>
**解析: **解<equation>\varSigma</equation>如图（a）所示.由于曲面<equation>\varSigma</equation>取下侧，故<equation>\varSigma</equation>的法向量n与z轴正向成钝角.记<equation>F(x,y,z)=</equation><equation>\sqrt{x^{2}+y^{2}}-z</equation>，可得<equation>n=(F_{x}^{\prime},F_{y}^{\prime},F_{z}^{\prime})=\left(\frac{x}{\sqrt{x^{2}+y^{2}}},\frac{y}{\sqrt{x^{2}+y^{2}}},-1\right)=\left(\frac{x}{z},\frac{y}{z},-1\right).</equation>由此可知，<equation>\frac{\cos \alpha}{\cos \gamma}=-\frac{x}{z},\frac{\cos \beta}{\cos \gamma}=-\frac{y}{z}.</equation>(a)

(b)

记<equation>D</equation>为<equation>\Sigma</equation>在<equation>xOy</equation>面的投影区域. 利用两类曲面积分之间的联系，可得<equation>\begin{array}{l} I = \iint_ {\Sigma} \left\{\left[ x f (x y) + 2 x - y \right] \cdot \frac {\cos \alpha}{\cos \gamma} \cdot \cos \gamma + \left[ y f (x y) + 2 y + x \right] \cdot \frac {\cos \beta}{\cos \gamma} \cdot \cos \gamma + \left[ z f (x y) + z \right] \cos \gamma \right\} d S \\ \underline {{\cos \gamma \mathrm {d} S = \mathrm {d} x \mathrm {d} y}} \iint_ {\Sigma} \left\{\left[ x f (x y) + 2 x - y \right] \cdot \left(- \frac {x}{z}\right) + \left[ y f (x y) + 2 y + x \right] \cdot \left(- \frac {y}{z}\right) + \left[ z f (x y) + z \right] \right\} \mathrm {d} x \mathrm {d} y \\ = \iint_ {\Sigma} \left[ \left(- \frac {x ^ {2} + y ^ {2}}{z} + z\right) f (x y) - \frac {2 \left(x ^ {2} + y ^ {2}\right)}{z} + z \right] \mathrm {d} x \mathrm {d} y \underline {{= \frac {z = \sqrt {x ^ {2} + y ^ {2}}}{\Sigma}}} \iint_ {\Sigma} (z - 2 z) \mathrm {d} x \mathrm {d} y \\ = - \iint_ {\Sigma} z \mathrm {d} x \mathrm {d} y \underline {{\underline {{\Sigma}} \text {取 下 侧}}} \iint_ {D} \sqrt {x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y. \\ \end{array}</equation>如图（b）所示，<equation>D</equation>为一个圆环区域.<equation>D=\{(x,y)\mid 1\leqslant x^{2}+y^{2}\leqslant 4\}</equation>在极坐标系下计算<equation>\iint_{D}\sqrt{x^{2}+y^{2}}\mathrm{d}x\mathrm{d}y.</equation><equation>\iint_ {D} \sqrt {x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y \xlongequal {\text {极 坐 标}} \int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {1} ^ {2} r ^ {2} \mathrm {d} r = 2 \pi \cdot \frac {r ^ {3}}{3} \Big | _ {1} ^ {2} = \frac {1 4 \pi}{3}.</equation>因此，<equation>I=\frac{14\pi}{3}</equation>

---

**2019年第12题 | 填空题 | 4分**
12. 设<equation>\Sigma</equation>设为曲面<equation>x^{2}+y^{2}+4 z^{2}=4 ( z \geqslant0 )</equation>的上侧，则<equation>\iint\limits_{\Sigma} \sqrt{4-x^{2}-4 z^{2}} \mathrm{d} x \mathrm{d} y=</equation>___
**答案: **# 32 3.
**解析: **解 将曲面方程代入被积函数，可得<equation>\iint\limits_{\Sigma}\sqrt{4-x^{2}-4z^{2}}\mathrm{d}x\mathrm{d}y=\iint\limits_{\Sigma}\sqrt{y^{2}}\mathrm{d}x\mathrm{d}y=\iint\limits_{\Sigma}|y|\mathrm{d}x\mathrm{d}y.</equation>如图所示，令<equation>z = 0</equation>，可得曲面<equation>\Sigma</equation>在<equation>xOy</equation>面上的投影区域为<equation>D_{xy} = \{(x,y)|x^2 + y^2\leqslant 4\}</equation>.注意到<equation>D_{xy}</equation>关于<equation>x</equation>轴对称，记<equation>D</equation>为<equation>D_{xy}</equation>位于<equation>x</equation>轴上方的部分.<equation>D</equation>在极坐标系下的表示为<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2, 0 \leqslant \theta \leqslant \pi \right\}.</equation>又因为<equation>\sum</equation>取上侧，所以<equation>\begin{aligned} \iint_ {\Sigma} | y | \mathrm {d} x \mathrm {d} y &= \iint_ {D _ {x y}} | y | \mathrm {d} x \mathrm {d} y \xlongequal {\text {对称性}} 2 \iint_ {D} y \mathrm {d} x \mathrm {d} y \\ \xlongequal {\text {极 坐 标}} 2 \int_ {0} ^ {\pi} \mathrm {d} \theta \int_ {0} ^ {2} r \sin \theta \cdot r \mathrm {d} r \\ &= 2 \int_ {0} ^ {\pi} \sin \theta \mathrm {d} \theta \int_ {0} ^ {2} r ^ {2} \mathrm {d} r \\ &= 2 \cdot 2 \cdot \left. \frac {r ^ {3}}{3} \right| _ {0} ^ {2} = \frac {3 2}{3}. \end{aligned}</equation>

---

**2018年第17题 | 解答题 | 10分**
17. (本题满分10分）

设<equation>\Sigma</equation>是曲面<equation>x=\sqrt{1-3 y^{2}-3 z^{2}}</equation>的前侧，计算曲面积分<equation>I=\iint_{\Sigma} x \mathrm{d} y \mathrm{d} z+(y^{3}+2) \mathrm{d} z \mathrm{d} x+z^{3} \mathrm{d} x \mathrm{d} y.</equation>
**解析: **解如图所示，添加辅助平面<equation>\varSigma^{\prime}</equation>：<equation>x=0(3y^{2}+3z^{2}\leqslant 1)</equation>，取后侧，即法向量指向 x轴负向，则<equation>\varSigma</equation>与<equation>\varSigma^{\prime}</equation>围成一个半椭球体<equation>\varOmega</equation>，且法向量指向外侧.

根据高斯公式，

根据高斯公式，<equation>\iint_{\Sigma+\Sigma^{\prime}}x\mathrm{d}y\mathrm{d}z+(y^{3}+2)\mathrm{d}z\mathrm{d}x+z^{3}\mathrm{d}x\mathrm{d}y=\iiint_{\Omega}(1+3y^{2}+3z^{2})\mathrm{d}v.</equation>采用先重后单的积分次序计算<equation>\iiint_{\Omega}(1+3y^{2}+3z^{2})\mathrm{d}v.</equation>沿平行于 yOz面的方向作<equation>\varOmega</equation>的横截面，得<equation>D _ {x} = \left\{(y, z) \mid 3 y ^ {2} + 3 z ^ {2} \leqslant 1 - x ^ {2} \right\}.</equation><equation>D_{x}</equation>是半径为<equation>\sqrt{\frac{1-x^{2}}{3}}</equation>的圆盘.于是，<equation>\Omega = \left\{(x, y, z) \mid (y, z) \in D _ {x}, 0 \leqslant x \leqslant 1 \right\}.</equation><equation>\begin{aligned} \iiint_ {\Omega} \left(1 + 3 y ^ {2} + 3 z ^ {2}\right) \mathrm {d} v &= \int_ {0} ^ {1} \mathrm {d} x \iint_ {D _ {x}} \left(1 + 3 y ^ {2} + 3 z ^ {2}\right) \mathrm {d} y \mathrm {d} z \stackrel {\text {极 坐 标}} {=} \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {0} ^ {\sqrt {\frac {1 - x ^ {2}}{3}}} \left(1 + 3 r ^ {2}\right) \cdot r \mathrm {d} r \\ &= 2 \pi \int_ {0} ^ {1} \left(\frac {r ^ {2}}{2} + \frac {3 r ^ {4}}{4}\right) \Bigg | _ {0} ^ {\sqrt {\frac {1 - x ^ {2}}{3}}} \mathrm {d} x = 2 \pi \int_ {0} ^ {1} \left[ \frac {1 - x ^ {2}}{6} + \frac {3}{4} \cdot \frac {\left(1 - x ^ {2}\right) ^ {2}}{3 ^ {2}} \right] \mathrm {d} x \\ &= \frac {\pi}{6} \int_ {0} ^ {1} \left(x ^ {4} - 4 x ^ {2} + 3\right) \mathrm {d} x = \frac {\pi}{6} \times \left(\frac {1}{5} - \frac {4}{3} + 3\right) = \frac {1 4 \pi}{4 5}. \end{aligned}</equation>因为<equation>\Sigma^{\prime}</equation>垂直于<equation>zOx</equation>面与<equation>xOy</equation>面，且<equation>\Sigma^{\prime}</equation>的方程为<equation>x = 0(3y^{2} + 3z^{2}\leqslant 1)</equation>，所以<equation>\iint_ {\Sigma^ {\prime}} x \mathrm {d} y \mathrm {d} z + \left(y ^ {3} + 2\right) \mathrm {d} z \mathrm {d} x + z ^ {3} \mathrm {d} x \mathrm {d} y = \iint_ {\Sigma^ {\prime}} x \mathrm {d} y \mathrm {d} z \stackrel {x = 0} {=} \iint_ {\Sigma^ {\prime}} 0 \mathrm {d} y \mathrm {d} z = 0.</equation>因此，<equation>I=\frac{14\pi}{45}-0=\frac{14\pi}{45}.</equation>

---

**2016年第18题 | 解答题 | 10分**

设有界区域<equation>\Omega</equation>由平面<equation>2x+y+2z=2</equation>与三个坐标平面围成，<equation>\Sigma</equation>为<equation>\Omega</equation>整个表面的外侧，计算曲面积分 I =<equation>\iint\limits_{\Sigma} ( x^{2}+1 ) \mathrm{d} y \mathrm{d} z-2 y \mathrm{d} z \mathrm{d} x+3 z \mathrm{d} x \mathrm{d} y.</equation>
**答案: **# 1 2
**解析: **解 由题设知，<equation>\varOmega=\left\{(x,y,z)\mid0\leqslant z\leqslant\frac{2-2x-y}{2},0\leqslant y\leqslant 2-2x,0\leqslant x\leqslant 1\right\}</equation>，则<equation>\varOmega</equation>的体积为<equation>V_{\varOmega}=\frac{1}{3}\times \frac{1\times 2}{2}\times 1=\frac{1}{3}</equation>.再由高斯公式知，<equation>\begin{aligned} I &= \iint_ {\Sigma} \left(x ^ {2} + 1\right) \mathrm {d} y \mathrm {d} z - 2 y \mathrm {d} z \mathrm {d} x + 3 z \mathrm {d} x \mathrm {d} y = \iiint_ {\Omega} \left(2 x - 2 + 3\right) \mathrm {d} x \mathrm {d} y \mathrm {d} z \\ &= 2 \iiint_ {\Omega} x \mathrm {d} x \mathrm {d} y \mathrm {d} z + \iiint_ {\Omega} \mathrm {d} x \mathrm {d} y \mathrm {d} z = 2 \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {2 - 2 x} \mathrm {d} y \int_ {0} ^ {\frac {2 - 2 x - y}{2}} x \mathrm {d} z + V _ {\Omega} \\ &= \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {2 - 2 x} x (2 - 2 x - y) \mathrm {d} y + \frac {1}{3} = \int_ {0} ^ {1} x \left[ (2 - 2 x) ^ {2} - \frac {(2 - 2 x) ^ {2}}{2} \right] \mathrm {d} x + \frac {1}{3} \\ &= \int_ {0} ^ {1} 2 \left(x - 2 x ^ {2} + x ^ {3}\right) \mathrm {d} x + \frac {1}{3} = \left(x ^ {2} - \frac {4}{3} x ^ {3} + \frac {x ^ {4}}{2}\right) \Bigg | _ {0} ^ {1} + \frac {1}{3} = \frac {1}{2}. \end{aligned}</equation>

---

**2014年第18题 | 解答题 | 10分**
18. (本题满分10分）

设<equation>\Sigma</equation>为曲面<equation>z=x^{2}+y^{2}</equation>（<equation>z\leqslant1</equation>）的上侧，计算曲面积分<equation>I=\iint\limits_{\Sigma} ( x-1 )^{3} \mathrm{d} y \mathrm{d} z+( y-1 )^{3} \mathrm{d} z \mathrm{d} x+( z-1 ) \mathrm{d} x \mathrm{d} y.</equation>
**解析: **解记<equation>\varSigma_{1}</equation>为面<equation>\left\{ \begin{array}{l} z=1, \\ x^{2}+y^{2}\leqslant 1 \end{array} \right.</equation>的下侧，即其法向量与z轴负向同向，记<equation>\varOmega</equation>为<equation>\varSigma_{1}</equation>与<equation>\varSigma</equation>围成的区域，则<equation>\varOmega=\{(x,y,z)\mid(x,y)\in D_{z},0\leqslant z\leqslant 1\}</equation>，其中<equation>D_{z}=\{(x,y)\mid x^{2}+y^{2}\leqslant z\}</equation>.由高斯公式知，<equation>\iint_{\varSigma+\varSigma_{1}}(x-1)^{3}\mathrm{d}y\mathrm{d}z+(y-1)^{3}\mathrm{d}z\mathrm{d}x+(z-1)\mathrm{d}x\mathrm{d}y=-\iiint_{\varOmega}[3(x-1)^{2}+3(y-1)^{2}+1]\mathrm{d}x\mathrm{d}y\mathrm{d}z</equation><equation>= -\int_{0}^{1}\mathrm{d}z\iint_{D_{z}}[3(x-1)^{2}+3(y-1)^{2}+1]\mathrm{d}x\mathrm{d}y=-\int_{0}^{1}\mathrm{d}z\iint_{D_{z}}[3(x^{2}+y^{2})-6x-6y+7]\mathrm{d}x\mathrm{d}y</equation>对称性<equation>-\int_{0}^{1}\mathrm{d}z\iint_{D_{z}}[3(x^{2}+y^{2})+7]\mathrm{d}x\mathrm{d}y\frac{x=r\cos \theta}{y=r\sin \theta}-\int_{0}^{1}\mathrm{d}z\int_{0}^{2\pi}\mathrm{d}\theta \int_{0}^{\sqrt{z}}(3r^{2}+7)r\mathrm{d}r</equation><equation>= -\int_{0}^{1}\left(\frac{3}{2}\pi z^{2}+7\pi z\right)\mathrm{d}z=-4\pi.</equation>又在<equation>\Sigma_{1}</equation>上，<equation>z = 1</equation>，故<equation>\iint_{\Sigma_1} (x - 1)^3\mathrm{d}y\mathrm{d}z + (y - 1)^3\mathrm{d}z\mathrm{d}x + (z - 1)\mathrm{d}x\mathrm{d}y = 0 + 0 + 0 = 0</equation>，从而

---

**2009年第19题 | 解答题 | 10分**
19. (本题满分10分)<equation>I = \iint_ {\Sigma} \frac {x \mathrm {d} y \mathrm {d} z + y \mathrm {d} z \mathrm {d} x + z \mathrm {d} x \mathrm {d} y}{\left(x ^ {2} + y ^ {2} + z ^ {2}\right) ^ {\frac {3}{2}}}</equation>其中<equation>\Sigma</equation>是曲面<equation>2x^{2}+2y^{2}+z^{2}=4</equation>的外侧.
**解析: **<equation>P (x, y, z) = \frac {x}{\left(x ^ {2} + y ^ {2} + z ^ {2}\right) ^ {\frac {3}{2}}}, \quad Q (x, y, z) = \frac {y}{\left(x ^ {2} + y ^ {2} + z ^ {2}\right) ^ {\frac {3}{2}}}, \quad R (x, y, z) = \frac {z}{\left(x ^ {2} + y ^ {2} + z ^ {2}\right) ^ {\frac {3}{2}}}.</equation>当（x,y,z）<equation>\neq (0,0,0)</equation>时，有<equation>\frac {\partial P}{\partial x} = \frac {y ^ {2} + z ^ {2} - 2 x ^ {2}}{\left(x ^ {2} + y ^ {2} + z ^ {2}\right) ^ {\frac {5}{2}}}, \quad \frac {\partial Q}{\partial y} = \frac {x ^ {2} + z ^ {2} - 2 y ^ {2}}{\left(x ^ {2} + y ^ {2} + z ^ {2}\right) ^ {\frac {5}{2}}}, \quad \frac {\partial R}{\partial z} = \frac {x ^ {2} + y ^ {2} - 2 z ^ {2}}{\left(x ^ {2} + y ^ {2} + z ^ {2}\right) ^ {\frac {5}{2}}}.</equation>记<equation>\Sigma_{1}</equation>是曲面<equation>x^{2} + y^{2} + z^{2} = 1</equation>的内侧，则<equation>\Sigma_{1}</equation>包含在<equation>\Sigma</equation>内.记<equation>\Omega</equation>为<equation>\Sigma_{1}</equation>与<equation>\Sigma</equation>围成的闭区域，则<equation>\Sigma_{1} + \Sigma</equation>为<equation>\Omega</equation>的整个边界曲面的外侧，且<equation>P(x,y,z),Q(x,y,z),R(x,y,z)</equation>在<equation>\Omega</equation>上有一阶连续偏导数.由高斯公式知，<equation>\iint_ {\Sigma + \Sigma_ {1}} \frac {x \mathrm {d} y \mathrm {d} z + y \mathrm {d} z \mathrm {d} x + z \mathrm {d} x \mathrm {d} y}{\left(x ^ {2} + y ^ {2} + z ^ {2}\right) ^ {\frac {3}{2}}} = \iiint_ {\Omega} \left(\frac {\partial P}{\partial x} + \frac {\partial Q}{\partial y} + \frac {\partial R}{\partial z}\right) \mathrm {d} x \mathrm {d} y \mathrm {d} z = \iiint_ {\Omega} 0 \mathrm {d} x \mathrm {d} y \mathrm {d} z = 0.</equation>记<equation>\Omega_{1}</equation>为闭曲面<equation>\Sigma_{1}</equation>围成的闭区域，即<equation>\Omega_{1} = \{(x,y,z) | x^{2} + y^{2} + z^{2} \leqslant 1\}</equation>，则<equation>\begin{aligned} I &= \iint_ {\Sigma + \Sigma_ {1}} \frac {x \mathrm {d} y \mathrm {d} z + y \mathrm {d} z \mathrm {d} x + z \mathrm {d} x \mathrm {d} y}{\left(x ^ {2} + y ^ {2} + z ^ {2}\right) ^ {\frac {3}{2}}} - \iint_ {\Sigma_ {1}} \frac {x \mathrm {d} y \mathrm {d} z + y \mathrm {d} z \mathrm {d} x + z \mathrm {d} x \mathrm {d} y}{\left(x ^ {2} + y ^ {2} + z ^ {2}\right) ^ {\frac {3}{2}}} \\ &= 0 - \iint_ {\Sigma_ {1}} x \mathrm {d} y \mathrm {d} z + y \mathrm {d} z \mathrm {d} x + z \mathrm {d} x \mathrm {d} y \quad (\text {在} \Sigma_ {1} \text {上 有} x ^ {2} + y ^ {2} + z ^ {2} = 1) \\ \frac {\text {高斯公式}}{\Omega_ {1}} \iiint_ {\Omega_ {1}} (1 + 1 + 1) \mathrm {d} x \mathrm {d} y \mathrm {d} z &= 3 \iiint_ {\Omega_ {1}} \mathrm {d} x \mathrm {d} y \mathrm {d} z \\ &= 3 \cdot \frac {4}{3} \pi \cdot 1 ^ {3} = 4 \pi . \end{aligned}</equation>

---


#### 重积分的计算

**2024年第17题 | 解答题 | 10分**

17. (本题满分10分）

已知平面区域<equation>D=\{(x,y)\mid \sqrt{1-y^{2}}\leqslant x\leqslant 1,-1\leqslant y\leqslant 1\}</equation>，计算<equation>\iint_{D}\frac{x}{\sqrt{x^{2}+y^{2}}}\mathrm{d}x\mathrm{d}y.</equation>

**答案:**<equation>\ln(\sqrt{2}+1)+\sqrt{2}-2</equation>

**解析:**解（法一）如图（a）所示，区域 D关于 x轴对称，而<equation>\frac{x}{\sqrt{x^{2}+y^{2}}}</equation>为关于 y的偶函数，故<equation>\iint_{D}\frac{x}{\sqrt{x^{2}+y^{2}}}\mathrm{d}x\mathrm{d}y=</equation><equation>2\iint_{D_{1}}\frac{x}{\sqrt{x^{2}+y^{2}}}\mathrm{d}x\mathrm{d}y</equation>，其中<equation>D_{1}</equation>为D位于x轴上方的部分.

注意到<equation>D_{1}</equation>关于直线<equation>y=x</equation>对称，如图（b）所示，记<equation>D_{0}</equation>为<equation>D_{1}</equation>位于直线<equation>y=x</equation>下方的部分，则由轮换对称性的结论可知，

(a)

(b)<equation>\iint_ {D _ {1}} \frac {x}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y = \iint_ {D _ {0}} \frac {x}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y + \iint_ {D _ {1} \backslash D _ {0}} \frac {x}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y = \iint_ {D _ {0}} \frac {x + y}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y.</equation><equation>D_{0}</equation>在极坐标系下的表示为<equation>D_{0} = \left\{(r,\theta)\mid 1\leqslant r\leqslant \sec \theta ,0\leqslant \theta \leqslant \frac{\pi}{4}\right\}</equation>. 因此，<equation>\begin{aligned} \iint_ {D} \frac {x}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y &= 2 \iint_ {D _ {1}} \frac {x}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {0}} \frac {x + y}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y \\ \xlongequal {\text {极 坐 标}} 2 \iint_ {D _ {0}} (\cos \theta + \sin \theta) \cdot r \mathrm {d} r \mathrm {d} \theta &= 2 \int_ {0} ^ {\frac {\pi}{4}} (\cos \theta + \sin \theta) \mathrm {d} \theta \int_ {1} ^ {\sec \theta} r \mathrm {d} r \\ &= 2 \int_ {0} ^ {\frac {\pi}{4}} (\cos \theta + \sin \theta) \cdot \frac {1}{2} \left(\sec^ {2} \theta - 1\right) \mathrm {d} \theta = \int_ {0} ^ {\frac {\pi}{4}} (\cos \theta + \sin \theta) \left(\sec^ {2} \theta - 1\right) \mathrm {d} \theta \\ &= \int_ {0} ^ {\frac {\pi}{4}} \left(\sec \theta - \cos \theta + \frac {\sin \theta}{\cos^ {2} \theta} - \sin \theta\right) \mathrm {d} \theta = \left[ \ln \left(\sec \theta + \tan \theta\right) - \sin \theta + \frac {1}{\cos \theta} + \cos \theta \right] \Bigg | _ {0} ^ {\frac {\pi}{4}} \\ &= \ln (\sqrt {2} + 1) + \sqrt {2} - 2. \end{aligned}</equation>（法二）也可以在直角坐标系下计算<equation>\iint_{D} \frac{x}{\sqrt{x^{2}+y^{2}}} \mathrm{d}x \mathrm{d}y.</equation><equation>\begin{aligned} \iint_ {D} \frac {x}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y &= 2 \iint_ {D _ {1}} \frac {x}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y = 2 \int_ {0} ^ {1} \mathrm {d} y \int_ {\sqrt {1 - y ^ {2}}} ^ {1} \frac {x}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \\ &= 2 \int_ {0} ^ {1} \sqrt {x ^ {2} + y ^ {2}} \Big | _ {x = \sqrt {1 - y ^ {2}}} ^ {x = 1} \mathrm {d} y = 2 \int_ {0} ^ {1} \left(\sqrt {1 + y ^ {2}} - 1\right) \mathrm {d} y \\ \underline {{\underline {{y = \tan u}}}} 2 \int_ {0} ^ {\frac {\pi}{4}} \sec^ {3} u \mathrm {d} u - 2. \end{aligned}</equation>下面计算<equation>\int_{0}^{\frac{\pi}{4}}\sec^{3}u\mathrm{d}u.</equation><equation>\begin{aligned} \int_ {0} ^ {\frac {\pi}{4}} \sec^ {3} u \mathrm {d} u &= \int_ {0} ^ {\frac {\pi}{4}} \sec u \mathrm {d} (\tan u) = \sec u \tan u \left| _ {0} ^ {\frac {\pi}{4}} - \int_ {0} ^ {\frac {\pi}{4}} \tan u \cdot \sec u \tan u \mathrm {d} u \right. \\ &= \sqrt {2} - \int_ {0} ^ {\frac {\pi}{4}} \left(\sec^ {2} u - 1\right) \sec u \mathrm {d} u = \sqrt {2} - \int_ {0} ^ {\frac {\pi}{4}} \sec^ {3} u \mathrm {d} u + \int_ {0} ^ {\frac {\pi}{4}} \sec u \mathrm {d} u \\ &= \sqrt {2} - \int_ {0} ^ {\frac {\pi}{4}} \sec^ {3} u \mathrm {d} u + \ln (\sec u + \tan u) \Bigg | _ {0} ^ {\frac {\pi}{4}} \\ &= \sqrt {2} - \int_ {0} ^ {\frac {\pi}{4}} \sec^ {3} u \mathrm {d} u + \ln (\sqrt {2} + 1). \end{aligned}</equation>由此可得<equation>2\int_{0}^{\frac{\pi}{4}} \sec^{3} u \mathrm{d} u=\ln(\sqrt{2}+1)+\sqrt{2}.</equation>因此，<equation>\iint_{D}\frac{x}{\sqrt{x^{2}+y^{2}}}\mathrm{d}x\mathrm{d}y=\ln(\sqrt{2}+1)+\sqrt{2}-2.</equation>

---

**2022年第18题 | 解答题 | 12分**

18. (本题满分12分）

已知平面区域 D = {（x,y）| y-2≤x≤<equation>\sqrt{4-y^{2}}</equation>, 0≤y≤2} ，计算 I =<equation>\iint_{D} \frac{(x-y)^{2}}{x^{2}+y^{2}} \mathrm{d} x \mathrm{d} y.</equation>

**答案:**## I = 2<equation>\pi</equation>- 2.

**解析:**解 在极坐标系下计算.

由<equation>D</equation>的表达式可知，如图（a）所示，<equation>D</equation>是由直线<equation>y = x + 2</equation>，圆<equation>x^{2} + y^{2} = 4</equation>以及<equation>x</equation>轴围成的部分.直线<equation>y = x + 2</equation>在极坐标系下的表示为<equation>r = \frac{2}{\sin \theta - \cos \theta}</equation>，圆<equation>x^{2} + y^{2} = 4</equation>在极坐标系下的表示为<equation>r = 2</equation>.

(a)

(b)

如图（b）所示，将<equation>D</equation>分为两部分<equation>D_{1}</equation>和<equation>D_{2}</equation>.<equation>D _ {1} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2, 0 \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation><equation>D _ {2} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \frac {2}{\sin \theta - \cos \theta}, \frac {\pi}{2} \leqslant \theta \leqslant \pi \right\}.</equation>因此，<equation>\begin{aligned} \iint_ {D} \frac {(x - y) ^ {2}}{x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \iint_ {D} \frac {r ^ {2} (\cos \theta - \sin \theta) ^ {2}}{r ^ {2}} \cdot r \mathrm {d} r \mathrm {d} \theta &= \iint_ {D} (\cos \theta - \sin \theta) ^ {2} \cdot r \mathrm {d} r \mathrm {d} \theta \\ &= \int_ {0} ^ {\frac {\pi}{2}} (\cos \theta - \sin \theta) ^ {2} \mathrm {d} \theta \int_ {0} ^ {2} r \mathrm {d} r + \int_ {\frac {\pi}{2}} ^ {\pi} (\cos \theta - \sin \theta) ^ {2} \mathrm {d} \theta \int_ {0} ^ {\frac {2}{\sin \theta - \cos \theta}} r \mathrm {d} r \\ &= 2 \int_ {0} ^ {\frac {\pi}{2}} (1 - 2 \sin \theta \cos \theta) \mathrm {d} \theta + \int_ {\frac {\pi}{2}} ^ {\pi} (\cos \theta - \sin \theta) ^ {2} \cdot \frac {r ^ {2}}{2} \Bigg | _ {0} ^ {\frac {2}{\sin \theta - \cos \theta}} \mathrm {d} \theta \\ &= 2 \left(\frac {\pi}{2} - \sin^ {2} \theta \Big | _ {0} ^ {\frac {\pi}{2}}\right) + \int_ {\frac {\pi}{2}} ^ {\pi} (\cos \theta - \sin \theta) ^ {2} \cdot \frac {2}{(\sin \theta - \cos \theta) ^ {2}} \mathrm {d} \theta \\ &= \pi - 2 + 2 \times \left(\pi - \frac {\pi}{2}\right) = 2 \pi - 2. \end{aligned}</equation>

---

**2016年第15题 | 解答题 | 10分**

15. (本题满分10分）已知平面区域<equation>D=\left\{(r,\theta)\mid 2\leqslant r\leqslant 2(1+\cos \theta),-\frac{\pi}{2}\leqslant \theta \leqslant \frac{\pi}{2}\right\}</equation>，计算二重积分<equation>\iint_{D}x\mathrm{d}x\mathrm{d}y.</equation>

**答案:**#<equation>5 \pi +\frac{3 2}{3}</equation>

**解析:**<equation>x=r\cos \theta ,y=r\sin \theta</equation>则<equation>\begin{aligned} \iint_ {D} x \mathrm {d} x \mathrm {d} y &= \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {2} ^ {2 (1 + \cos \theta)} r ^ {2} \cos \theta \mathrm {d} r = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \cos \theta \cdot \frac {8 (1 + \cos \theta) ^ {3} - 8}{3} \mathrm {d} \theta \\ &= \frac {8}{3} \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \left(\cos^ {4} \theta + 3 \cos^ {3} \theta + 3 \cos^ {2} \theta\right) \mathrm {d} \theta \\ &= \frac {1 6}{3} \int_ {0} ^ {\frac {\pi}{2}} \cos^ {4} \theta \mathrm {d} \theta + 1 6 \int_ {0} ^ {\frac {\pi}{2}} \cos^ {3} \theta \mathrm {d} \theta + 1 6 \int_ {0} ^ {\frac {\pi}{2}} \cos^ {2} \theta \mathrm {d} \theta \\ \frac {\text {华 里 士公 式}}{} \frac {1 6}{3} \times \frac {3}{4} \times \frac {1}{2} \times \frac {\pi}{2} + 1 6 \times \frac {2}{3} + 1 6 \times \frac {1}{2} \times \frac {\pi}{2} \\ &= 5 \pi + \frac {3 2}{3}. \end{aligned}</equation>

---

**2015年第12题 | 填空题 | 4分**

12. 设<equation>\Omega</equation>是由平面<equation>x+y+z=1</equation>与三个坐标平面所围成的空间区域，则<equation>\iiint\limits_{\Omega} ( x+2 y+3 z ) \mathrm{d} x \mathrm{d} y \mathrm{d} z=</equation>___

**解析:**解 （法一）由轮换对称性知，<equation>\iiint_ {\Omega} x \mathrm {d} x \mathrm {d} y \mathrm {d} z = \iiint_ {\Omega} y \mathrm {d} x \mathrm {d} y \mathrm {d} z = \iiint_ {\Omega} z \mathrm {d} x \mathrm {d} y \mathrm {d} z.</equation>又<equation>\varOmega=\{(x,y,z)\mid(y,z)\in D_{x},0\leqslant x\leqslant 1\}</equation>，其中<equation>D_{x}=\{(y,z)\mid y+z\leqslant 1-x,y\geqslant 0,z\geqslant 0\}</equation>，其面积为<equation>\frac{(1-x)^{2}}{2}</equation>，故<equation>\begin{aligned} \iiint_ {\Omega} (x + 2 y + 3 z) \mathrm {d} x \mathrm {d} y \mathrm {d} z &= 6 \iiint_ {\Omega} x \mathrm {d} x \mathrm {d} y \mathrm {d} z = 6 \int_ {0} ^ {1} x \mathrm {d} x \iint_ {D _ {x}} \mathrm {d} y \mathrm {d} z \\ &= 6 \int_ {0} ^ {1} x \cdot \frac {(1 - x) ^ {2}}{2} \mathrm {d} x \\ &= 3 \int_ {0} ^ {1} \left(x ^ {3} - 2 x ^ {2} + x\right) \mathrm {d} x = \frac {1}{4}. \end{aligned}</equation>（法二）由题设知，<equation>\Omega = \left\{(x, y, z) \mid 0 \leqslant z \leqslant 1 - x - y, 0 \leqslant y \leqslant 1 - x, 0 \leqslant x \leqslant 1 \right\}.</equation>因此，<equation>\begin{aligned} \iiint_ {\Omega} (x + 2 y + 3 z) \mathrm {d} v \xlongequal {\text {轮 换 对称 性}} 6 \iiint_ {\Omega} z \mathrm {d} v &= 6 \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {1 - x} \mathrm {d} y \int_ {0} ^ {1 - x - y} z \mathrm {d} z \\ &= 6 \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {1 - x} \frac {\left(1 - x - y\right) ^ {2}}{2} \mathrm {d} y = 6 \int_ {0} ^ {1} \frac {\left(y + x - 1\right) ^ {3}}{6} \Big | _ {0} ^ {1 - x} \mathrm {d} x \\ &= 6 \int_ {0} ^ {1} \frac {\left(1 - x\right) ^ {3}}{6} \mathrm {d} x = \int_ {0} ^ {1} (1 - x) ^ {3} \mathrm {d} x \xlongequal {t = 1 - x} \int_ {0} ^ {1} t ^ {3} \mathrm {d} t = \frac {1}{4}. \end{aligned}</equation>

---

**2011年第19题 | 解答题 | 10分**

19. (本题满分11分)

已知函数 f(x,y)具有二阶连续偏导数，且<equation>f ( 1, y )=0, f ( x, 1 )=0, \iint_{D} f ( x, y ) \mathrm{d} x \mathrm{d} y=a</equation>，其中 D={（x,y）|0≤x≤ 1,0≤y≤1}，计算二重积分<equation>I=\iint_{D} x y f_{xy}^{\prime \prime}(x,y)\mathrm{d} x \mathrm{d} y.</equation>

**解析:**由于<equation>f_{xy}^{\prime \prime}(x,y)</equation>是<equation>f_x^{\prime}(x,y)</equation>对<equation>y</equation>的偏导数，故对每个固定的<equation>x,f_{xy}^{\prime \prime}(x,y)\mathrm{d}y = \mathrm{d}[f_x^{\prime}(x,y)]</equation><equation>\begin{aligned} I &= \iint_ {D} x y f _ {x y} ^ {\prime \prime} (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} x \mathrm {d} x \int_ {0} ^ {1} y f _ {x y} ^ {\prime \prime} (x, y) \mathrm {d} y = \int_ {0} ^ {1} x \mathrm {d} x \int_ {0} ^ {1} y \mathrm {d} \left[ f _ {x} ^ {\prime} (x, y) \right] \\ \underline {{\text {分 部 积 分}}} \int_ {0} ^ {1} x \left[ y f _ {x} ^ {\prime} (x, y) \right| _ {y = 0} ^ {y = 1} - \int_ {0} ^ {1} f _ {x} ^ {\prime} (x, y) \mathrm {d} y \Bigg ] \mathrm {d} x &= \int_ {0} ^ {1} x f _ {x} ^ {\prime} (x, 1) \mathrm {d} x - \int_ {0} ^ {1} x \mathrm {d} x \int_ {0} ^ {1} f _ {x} ^ {\prime} (x, y) \mathrm {d} y. \end{aligned}</equation>由于<equation>f ( x, 1 ) = 0</equation>，即一元函数<equation>f ( x, 1 )</equation>是关于 x的常函数，故<equation>f_{x}^{\prime}(x,1)=0.</equation>又由于 D为矩形区域，故交换二次积分的积分次序可得，<equation>\int_ {0} ^ {1} x \mathrm {d} x \int_ {0} ^ {1} f _ {x} ^ {\prime} (x, y) \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {1} x f _ {x} ^ {\prime} (x, y) \mathrm {d} x.</equation>从而，<equation>\begin{aligned} I &= 0 - \int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {1} x f _ {x} ^ {\prime} (x, y) \mathrm {d} x = - \int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {1} x \mathrm {d} [ f (x, y) ] \\ \frac {\mathrm {分 部 积 分}}{} - \int_ {0} ^ {1} \left[ x f (x, y) \mid_ {x = 0} ^ {x = 1} - \int_ {0} ^ {1} f (x, y) \mathrm {d} x \right] \mathrm {d} y &= - \int_ {0} ^ {1} f (1, y) \mathrm {d} y + \int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {1} f (x, y) \mathrm {d} x \\ \frac {f (1 , y) = 0}{\mathrm {一}} \int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {1} f (x, y) \mathrm {d} x &= \iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = a. \end{aligned}</equation>

---

**2009年第12题 | 填空题 | 4分**

12. 设<equation>\Omega=\{(x,y,z)\mid x^{2}+y^{2}+z^{2}\leqslant1\}</equation>，则<equation>\iiint\limits_{\Omega}z^{2}\mathrm{d}x\mathrm{d}y\mathrm{d}z=</equation>___

**答案:**##<equation>\frac{4}{1 5}\pi.</equation>

**解析:**解 （法一）由轮换对称性知，<equation>\iiint_ {\Omega} z ^ {2} \mathrm {d} x \mathrm {d} y \mathrm {d} z = \iiint_ {\Omega} y ^ {2} \mathrm {d} x \mathrm {d} y \mathrm {d} z = \iiint_ {\Omega} x ^ {2} \mathrm {d} x \mathrm {d} y \mathrm {d} z,</equation>于是<equation>\begin{aligned} \iiint_ {\Omega} z ^ {2} \mathrm {d} x \mathrm {d} y \mathrm {d} z &= \frac {1}{3} \iiint_ {\Omega} \left(x ^ {2} + y ^ {2} + z ^ {2}\right) \mathrm {d} x \mathrm {d} y \mathrm {d} z \\ &= \frac {1}{3} \int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {0} ^ {\pi} \mathrm {d} \varphi \int_ {0} ^ {1} r ^ {2} \cdot r ^ {2} \sin \varphi \mathrm {d} r \quad \mathrm {注 意 这里 利用 换 元 公 式 时}, \\ &= \frac {2 \pi}{3} \int_ {0} ^ {\pi} \sin \varphi \mathrm {d} \varphi \int_ {0} ^ {1} r ^ {4} \mathrm {d} r = \frac {2 \pi}{3} \cdot 2 \cdot \frac {1}{5} = \frac {4}{1 5} \pi . \end{aligned}</equation>（法二）令<equation>\left\{ \begin{array}{l}x = r\sin \varphi \cos \theta ,\\ y = r\sin \varphi \sin \theta ,0\leqslant \varphi \leqslant \pi ,0\leqslant \theta \leqslant 2\pi ,0\leqslant r\leqslant 1,\\ z = r\cos \varphi , \end{array} \right.</equation>则<equation>\begin{aligned} \iiint_ {\Omega} z ^ {2} \mathrm {d} x \mathrm {d} y \mathrm {d} z &= \int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {0} ^ {\pi} \mathrm {d} \varphi \int_ {0} ^ {1} \left(r ^ {2} \cos^ {2} \varphi \cdot r ^ {2} \sin \varphi\right) \mathrm {d} r \\ &= 2 \pi \cdot \left[ - \int_ {0} ^ {\pi} \cos^ {2} \varphi \mathrm {d} (\cos \varphi) \right] \cdot \int_ {0} ^ {1} r ^ {4} \mathrm {d} r \\ &= 2 \pi \cdot \left(\left. - \frac {\cos^ {3} \varphi}{3} \right| _ {0} ^ {\pi}\right) \cdot \frac {1}{5} = \frac {4}{1 5} \pi . \end{aligned}</equation>

---


#### 重积分的应用

**2019年第19题 | 解答题 | 10分**

19. (本题满分10分）

设<equation>\Omega</equation>是由锥面<equation>x^{2}+(y-z)^{2}=(1-z)^{2}(0\leqslant z\leqslant 1)</equation>与平面 z=0围成的锥体，求<equation>\Omega</equation>的形心坐标.

**答案:**<equation>\varOmega</equation>的形心坐标为<equation>\left( 0,\frac{1}{4},\frac{1}{4}\right).</equation>

**解析:**解 由锥面方程可知，<equation>\varOmega</equation>是一个介于 xOy面与平面 z=1之间的锥体，且<equation>\varOmega</equation>关于 yOz面对称，故由对称性可知，<equation>\overline{x}=0.</equation>下面计算<equation>\varOmega</equation>的体积V.

令<equation>z = 0</equation>，可得锥面与<equation>xOy</equation>面的交线为<equation>x^{2} + y^{2} = 1</equation>，故<equation>\varOmega</equation>的底面为一个圆心在原点、半径为1的圆，面积为<equation>\pi</equation>.又因为<equation>0\leqslant z\leqslant 1,\varOmega</equation>的高为1，所以由锥体的体积公式可知，<equation>\varOmega</equation>的体积<equation>V = \frac{1}{3}\pi</equation>下面分别计算<equation>\bar{z},\bar{y}。</equation>沿平行于<equation>x O y</equation>面的方向作<equation>\varOmega</equation>的截面，即以平面<equation>Z=z</equation>截<equation>\varOmega</equation>，所得截面记为<equation>D_{z}.</equation><equation>D_{z}</equation>为圆心在（0，z，z）、半径为1-z的圆盘区域.写出<equation>Z=z</equation>上的<equation>D_{z}</equation>的表示.<equation>D _ {z} = \left\{(x, y) \mid x ^ {2} + (y - z) ^ {2} \leqslant (1 - z) ^ {2} \right\}.</equation>于是，<equation>\Omega = \left\{(x, y, z) \mid (x, y) \in D _ {z}, 0 \leqslant z \leqslant 1 \right\}.</equation>利用“先重后单”的次序计算积分.<equation>\begin{aligned} \iiint_ {\Omega} z \mathrm {d} x \mathrm {d} y \mathrm {d} z &= \int_ {0} ^ {1} z \mathrm {d} z \iint_ {D _ {z}} \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} z \cdot \left(D _ {z} \text {的 面 积}\right) \mathrm {d} z = \pi \int_ {0} ^ {1} z (1 - z) ^ {2} \mathrm {d} z \\ &= \pi \cdot \int_ {0} ^ {1} \left(z ^ {3} - 2 z ^ {2} + z\right) \mathrm {d} z = \pi \cdot \left(\frac {1}{4} - \frac {2}{3} + \frac {1}{2}\right) = \frac {\pi}{1 2}. \end{aligned}</equation><equation>\begin{aligned} \iiint_ {\Omega} y \mathrm {d} x \mathrm {d} y \mathrm {d} z &= \int_ {0} ^ {1} \mathrm {d} z \iint_ {D _ {z}} y \mathrm {d} x \mathrm {d} y \frac {x = r \cos \theta}{y = z + r \sin \theta} \int_ {0} ^ {1} \mathrm {d} z \int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {0} ^ {1 - z} (z + r \sin \theta) \cdot r \mathrm {d} r \\ &= \int_ {0} ^ {1} \mathrm {d} z \int_ {0} ^ {2 \pi} \left(z \cdot \frac {r ^ {2}}{2} + \frac {r ^ {3}}{3} \cdot \sin \theta\right) \Bigg | _ {0} ^ {1 - z} \mathrm {d} \theta = \int_ {0} ^ {1} 2 \pi \cdot z \cdot \frac {(1 - z) ^ {2}}{2} \mathrm {d} z \\ &= \pi \int_ {0} ^ {1} z (1 - z) ^ {2} \mathrm {d} z = \frac {\pi}{1 2}. \end{aligned}</equation>因此，<equation>\bar{y} = \frac{\frac{\pi}{12}}{\frac{\pi}{3}} = \frac{1}{4},\bar{z} = \frac{\frac{\pi}{12}}{\frac{\pi}{3}} = \frac{1}{4}.</equation>综上所述，<equation>\varOmega</equation>的形心坐标为<equation>\left(0,\frac{1}{4},\frac{1}{4}\right)</equation>

---

**2013年第19题 | 解答题 | 10分**

19. (本题满分10分)

19. (本题满分10分)

设直线 L过 A(1,0,0),B(0,1,1)两点，将 L绕 z轴旋转一周得到曲面<equation>\Sigma</equation><equation>\Sigma</equation>与平面<equation>z=0,z=2</equation>所围成的立体为<equation>\Omega</equation>.

I. 求曲面<equation>\Sigma</equation>的方程;

II. 求<equation>\Omega</equation>的形心坐标.

**答案:**(19) ( I )<equation>x^{2}+y^{2}=2 z^{2}-2 z+1;</equation>

**解析:**解（I）直线 L的方程为<equation>\frac{x-1}{-1}=\frac{y}{1}=\frac{z}{1}</equation>即<equation>\left\{ \begin{array}{l} x = 1 - z, \\ y = z, \end{array} \right.</equation>从而曲面<equation>\Sigma</equation>的方程为<equation>x^{2} + y^{2} = (1 - z)^{2} + z^{2}</equation>，即<equation>x^{2} + y^{2} = 2z^{2} - 2z + 1.</equation>（Ⅱ）设<equation>\varOmega</equation>的形心坐标为<equation>(\bar{x},\bar{y},\bar{z})</equation>.由曲面<equation>\Sigma</equation>的方程知，<equation>\varOmega</equation>关于<equation>xOz,yOz</equation>面对称，从而<equation>\bar {x} = \frac {\iiint_ {\Omega} x \mathrm {d} x \mathrm {d} y \mathrm {d} z}{\iiint_ {\Omega} \mathrm {d} x \mathrm {d} y \mathrm {d} z} = 0, \quad \bar {y} = \frac {\iiint_ {\Omega} y \mathrm {d} x \mathrm {d} y \mathrm {d} z}{\iiint_ {\Omega} \mathrm {d} x \mathrm {d} y \mathrm {d} z} = 0.</equation>记<equation>D_{z} = \{(x,y)\mid x^{2} + y^{2}\leqslant 2z^{2} - 2z + 1\}</equation>，则<equation>\iiint_ {\Omega} z \mathrm {d} x \mathrm {d} y \mathrm {d} z = \int_ {0} ^ {2} z \mathrm {d} z \iint_ {D _ {z}} \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {2} z \cdot \pi \left(2 z ^ {2} - 2 z + 1\right) \mathrm {d} z = \frac {1 4}{3} \pi ,</equation><equation>\iiint_ {\Omega} \mathrm {d} x \mathrm {d} y \mathrm {d} z = \int_ {0} ^ {2} \mathrm {d} z \iint_ {D _ {z}} \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {2} \pi \left(2 z ^ {2} - 2 z + 1\right) \mathrm {d} z = \frac {1 0}{3} \pi .</equation>于是<equation>\bar{z} = \frac{\iiint \Omega z\mathrm{d}x\mathrm{d}y\mathrm{d}z}{\iiint \Omega \mathrm{d}x\mathrm{d}y\mathrm{d}z} = \frac{7}{5}</equation>. 因此<equation>\varOmega</equation>的形心坐标为<equation>\left(0,0,\frac{7}{5}\right)</equation>.

---

**2010年第12题 | 填空题 | 4分**

12. 设<equation>\varOmega = \{(x,y,z) \mid x^2 + y^2 \leqslant z \leqslant 1\}</equation>, 则<equation>\varOmega</equation>的形心的坚坐标<equation>\bar{z} =</equation>___

**解析:**解（法一）由题设知，<equation>\varOmega=\{(x,y,z)\mid(x,y)\in D_{z},0\leqslant z\leqslant 1\}</equation>，其中<equation>D_{z}=\{(x,y)\mid x^{2}+y^{2}\leqslant z\}</equation>且<equation>D_{z}</equation>的面积为<equation>\pi z</equation>，从而<equation>\bar {z} = \frac {\iiint_ {\Omega} z \mathrm {d} x \mathrm {d} y \mathrm {d} z}{\iiint_ {\Omega} \mathrm {d} x \mathrm {d} y \mathrm {d} z} = \frac {\int_ {0} ^ {1} z \mathrm {d} z \iint_ {D _ {z}} \mathrm {d} x \mathrm {d} y}{\int_ {0} ^ {1} \mathrm {d} z \iint_ {D _ {z}} \mathrm {d} x \mathrm {d} y} = \frac {\int_ {0} ^ {1} \left(z \cdot \pi z\right) \mathrm {d} z}{\int_ {0} ^ {1} \pi z \mathrm {d} z} = \frac {\frac {\pi}{3}}{\frac {\pi}{2}} = \frac {2}{3}.</equation>（法二）由题设知，<equation>\varOmega=\{(x,y,z)\mid(x,y)\in D_{xy},x^{2}+y^{2}\leqslant z\leqslant 1\}</equation>，其中<equation>D_{xy}=\{(x,y)\mid x^{2}+y^{2}\leqslant 1\}</equation>，从而<equation>\begin{aligned} \bar {z} &= \frac {\iiint_ {\Omega} z \mathrm {d} x \mathrm {d} y \mathrm {d} z}{\iiint_ {\Omega} \mathrm {d} x \mathrm {d} y \mathrm {d} z} = \frac {\iint_ {D _ {x y}} \mathrm {d} x \mathrm {d} y \int_ {x ^ {2} + y ^ {2}} ^ {1} z \mathrm {d} z}{\iint_ {D _ {x y}} \mathrm {d} x \mathrm {d} y \int_ {x ^ {2} + y ^ {2}} ^ {1} \mathrm {d} z} = \frac {\frac {1}{2} \iint_ {D _ {x y}} \left[ 1 - \left(x ^ {2} + y ^ {2}\right) ^ {2} \right] \mathrm {d} x \mathrm {d} y}{\iint_ {D _ {x y}} \left(1 - x ^ {2} - y ^ {2}\right) \mathrm {d} x \mathrm {d} y} \\ \frac {x = r \cos \theta}{y = r \sin \theta} \frac {\frac {1}{2} \int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {0} ^ {1} \left(1 - r ^ {4}\right) r \mathrm {d} r}{\int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {0} ^ {1} \left(1 - r ^ {2}\right) r \mathrm {d} r} &= \frac {\frac {\pi}{3}}{\frac {\pi}{2}} = \frac {2}{3}. \end{aligned}</equation>

---


#### 旋度的定义

**2018年第11题 | 填空题 | 4分**

11. 设<equation>F(x,y,z)= xy i-yz j+z x k</equation>, 则<equation>\mathbf{rot} F(1,1,0)=</equation>___

**答案:**i-k.

**解析:**根据旋度的定义，<equation>\operatorname {r o t} F (x, y, z) = \left| \begin{array}{c c c} i & j & k \\ \frac {\partial}{\partial x} & \frac {\partial}{\partial y} & \frac {\partial}{\partial z} \\ x y & - y z & z x \end{array} \right| = y i - z j - x k.</equation>代入<equation>(x,y,z) = (1,1,0)</equation>，可得<equation>\mathbf{rot} F(1,1,0) = i - k.</equation>

---

**2016年第10题 | 填空题 | 4分**

10. 向量场<equation>A(x,y,z) = (x+y+z)i+xyj+zk</equation>的旋度<equation>\mathbf{rot}A =</equation>___

**答案:**j + (y-1) k.

**解析:**令<equation>P= x+y+z, Q= x y, R=z</equation>，由旋度的定义知<equation>\mathbf{r o t} A=\left(\frac{\partial R}{\partial y}-\frac{\partial Q}{\partial z}\right) i+\left(\frac{\partial P}{\partial z}-\frac{\partial R}{\partial x}\right) j+\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right) k=j+(y-1) k.</equation>

---


#### 第一类曲线积分

**2018年第12题 | 填空题 | 4分**

12. 设 L为球面<equation>x^{2}+y^{2}+z^{2}=1</equation>与平面<equation>x+y+z=0</equation>的交线，则<equation>\oint_{L} xy\mathrm{d}s=</equation>___

**解析:**本题中，曲线<equation>L</equation>具有轮换对称性，故应利用轮换对称性来简化计算.

解 曲线 L如图所示.

由曲线<equation>L</equation>的方程可知，该曲线对变量<equation>x, y, z</equation>具有轮换对称性.于是，<equation>\oint_ {L} x y \mathrm {d} s = \oint_ {L} y z \mathrm {d} s = \oint_ {L} z x \mathrm {d} s = \frac {1}{3} \oint_ {L} (x y + y z + z x) \mathrm {d} s.</equation>又因为<equation>x y+y z+z x=\frac{1}{2} \left[ \left(x+y+z\right)^{2}-\left(x^{2}+y^{2}+z^{2}\right) \right]</equation>，所以<equation>\begin{aligned} \oint_ {L} x y \mathrm {d} s &= \frac {1}{3} \oint_ {L} \left(x y + y z + z x\right) \mathrm {d} s = \frac {1}{6} \oint_ {L} \left[ \left(x + y + z\right) ^ {2} - \left(x ^ {2} + y ^ {2} + z ^ {2}\right) \right] \mathrm {d} s \\ \frac {x + y + z = 0}{x ^ {2} + y ^ {2} + z ^ {2} = 1} \frac {1}{6} \oint_ {L} (0 - 1) \mathrm {d} s &= - \frac {1}{6} \oint_ {L} \mathrm {d} s. \end{aligned}</equation>由于 L为单位球面上的一个大圆，即以球心为圆心，且半径等于球半径的一个圆，故<equation>\oint_{L}\mathrm{d}s=L</equation>的周长<equation>= 2\pi.</equation>因此，原积分<equation>= -\frac{1}{6}\times 2\pi = -\frac{\pi}{3}.</equation>

---

**2009年第11题 | 填空题 | 4分**

11. 已知曲线<equation>L: y=x^{2}(0\leqslant x\leqslant\sqrt{2})</equation>，则<equation>\int_{L}x\mathrm{d}s=</equation>___

**答案:**# 13 6.

**解析:**由题设知，<equation>\begin{aligned} \int_ {L} x \mathrm {d} s &= \int_ {0} ^ {\sqrt {2}} x \sqrt {1 + \left[ y ^ {\prime} (x) \right] ^ {2}} \mathrm {d} x = \int_ {0} ^ {\sqrt {2}} x \sqrt {1 + 4 x ^ {2}} \mathrm {d} x \\ &= \frac {1}{8} \int_ {0} ^ {\sqrt {2}} \sqrt {1 + 4 x ^ {2}} \mathrm {d} \left(4 x ^ {2} + 1\right) = \frac {1}{8} \cdot \frac {2}{3} \left(1 + 4 x ^ {2}\right) ^ {\frac {3}{2}} \Bigg | _ {0} ^ {\sqrt {2}} = \frac {1 3}{6}. \end{aligned}</equation>

---


#### 第一类曲面积分

**2017年第19题 | 解答题 | 10分**

19. (本题满分10分)

设薄片型物体 S是圆雉面<equation>z=\sqrt{x^{2}+y^{2}}</equation>被柱面<equation>z^{2}=2 x</equation>割下的有限部分，其上任一点的密度为<equation>\mu(x,y,z)=</equation><equation>9 \sqrt{x^{2}+y^{2}+z^{2}}.</equation>记圆雉面与柱面的交线为 C.

I. 求 C在 xOy平面上的投影曲线的方程；

II. 求 S的质量 M.

**答案:**<equation>\begin{array}{l} (\mathrm {I}) \left\{ \begin{array}{l} x ^ {2} + y ^ {2} = 2 x, \\ z = 0; \end{array} \right. \\ (\mathrm {I I}) 6 4. \\ \end{array}</equation>

**解析:**解（I）由题设知，圆锥面与柱面的交线 C的方程为<equation>\left\{\begin{array}{l l}z=\sqrt{x^{2}+y^{2}},\\ z^{2}=2 x, \end{array} \right.</equation>消去 z得到<equation>x^{2}+y^{2}= 2 x</equation>，于是 C在 xOy平面上的投影曲线的方程为<equation>\left\{ \begin{array}{l} x ^ {2} + y ^ {2} = 2 x, \\ z = 0. \end{array} \right.</equation>（Ⅱ）设<equation>D_{xy}=\{(x,y)|x^{2}+y^{2}\leqslant 2x\}</equation>，则曲面 S的方程为<equation>z=\sqrt{x^{2}+y^{2}},(x,y)\in D_{xy}</equation>，从而 S的质量为<equation>\begin{aligned} M &= \iint_ {S} \mu (x, y, z) \mathrm {d} S = \iint_ {S} 9 \sqrt {x ^ {2} + y ^ {2} + z ^ {2}} \mathrm {d} S \xlongequal {z = \sqrt {x ^ {2} + y ^ {2}}} \iint_ {S} 9 \sqrt {2 \left(x ^ {2} + y ^ {2}\right)} \mathrm {d} S \\ &= \iint_ {D _ {x y}} 9 \sqrt {2 \left(x ^ {2} + y ^ {2}\right)} \cdot \sqrt {1 + \left(\frac {\partial z}{\partial x}\right) ^ {2} + \left(\frac {\partial z}{\partial y}\right) ^ {2}} \mathrm {d} x \mathrm {d} y \\ &= \iint_ {D _ {x y}} 9 \sqrt {2 \left(x ^ {2} + y ^ {2}\right)} \cdot \sqrt {1 + \left(\frac {x}{\sqrt {x ^ {2} + y ^ {2}}}\right) ^ {2} + \left(\frac {y}{\sqrt {x ^ {2} + y ^ {2}}}\right) ^ {2}} \mathrm {d} x \mathrm {d} y \\ &= 1 8 \iint_ {D _ {x y}} \sqrt {x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y. \end{aligned}</equation>令<equation>x = r\cos \theta ,y = r\sin \theta</equation>，由<equation>x^{2} + y^{2}\leqslant 2x</equation>知，<equation>r^{2}\leqslant 2r\cos \theta</equation>，即<equation>r\leqslant 2\cos \theta</equation>.如下图，<equation>D_{xy}</equation>在极坐标

变换下对应区域<equation>D = \left\{(r,\theta)\mid 0\leqslant r\leqslant 2\cos \theta , - \frac{\pi}{2}\leqslant \theta \leqslant \frac{\pi}{2}\right\}</equation>，从而<equation>\begin{aligned} M &= 1 8 \iint_ {D _ {x y}} \sqrt {x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y = 1 8 \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {2 \cos \theta} r \cdot r \mathrm {d} r \\ &= 4 8 \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \cos^ {3} \theta \mathrm {d} \theta = 9 6 \int_ {0} ^ {\frac {\pi}{2}} \cos^ {3} \theta \mathrm {d} \theta \\ &= 9 6 \times \frac {2}{3} = 6 4. \end{aligned}</equation>

---

**2012年第12题 | 填空题 | 4分**

12. 设<equation>\Sigma=\{(x,y,z)\mid x+y+z=1,x\geqslant0,y\geqslant0,z\geqslant0\}</equation>，则<equation>\iint\limits_{\Sigma}y^{2}\mathrm{d}S=</equation>___

**答案:**#<equation>\frac{\sqrt{3}}{12}</equation>

**解析:**分析 本题主要考查第一类曲面积分的计算. 一般将其化为重积分后再计算.

若曲面<equation>\Sigma</equation>的方程为<equation>z = z(x,y),(x,y)\in D_{xy}</equation>，且<equation>z(x,y)</equation>在<equation>D_{xy}</equation>上有连续偏导数，<equation>f(x,y,z)</equation>在<equation>\Sigma</equation>上连续，则<equation>\iint_ {\Sigma} f (x, y, z) \mathrm {d} S = \iint_ {D _ {x y}} f (x, y, z (x, y)) \sqrt {1 + \left(\frac {\partial z}{\partial x}\right) ^ {2} + \left(\frac {\partial z}{\partial y}\right) ^ {2}} \mathrm {d} x \mathrm {d} y.</equation>解 曲面<equation>\varSigma=\{(x,y,z)\mid z=1-x-y,x\geqslant0,y\geqslant0,z\geqslant0\}</equation>在 xOy平面上的投影区域为<equation>D_{xy}=\{(x,y)\mid 0\leqslant y\leqslant1,0\leqslant x\leqslant1-y\}</equation>，于是<equation>\begin{aligned} \iint_ {\Sigma} y ^ {2} \mathrm {d} S &= \iint_ {D _ {x y}} y ^ {2} \sqrt {1 + \left(\frac {\partial z}{\partial x}\right) ^ {2} + \left(\frac {\partial z}{\partial y}\right) ^ {2}} \mathrm {d} x \mathrm {d} y \\ &= \iint_ {D _ {x y}} y ^ {2} \sqrt {1 + 1 + 1} \mathrm {d} x \mathrm {d} y = \sqrt {3} \iint_ {D _ {x y}} y ^ {2} \mathrm {d} x \mathrm {d} y \\ &= \sqrt {3} \int_ {0} ^ {1} y ^ {2} \mathrm {d} y \int_ {0} ^ {1 - y} \mathrm {d} x = \sqrt {3} \int_ {0} ^ {1} y ^ {2} (1 - y) \mathrm {d} y = \frac {\sqrt {3}}{1 2}. \end{aligned}</equation>

---

**2010年第19题 | 解答题 | 10分**

19. (本题满分10分)

设 P为椭球面 S：<equation>x^{2}+y^{2}+z^{2}-yz=1</equation>上的动点，若 S在点 P处的切平面与 xOy面垂直，求点 P的轨迹 C，并计算曲面积分 I =<equation>\iint\limits_{\Sigma}\frac{(x+\sqrt{3})|y-2z|}{\sqrt{4+y^{2}+z^{2}-4yz}} \mathrm{d} S</equation>，其中<equation>\varSigma</equation>是椭球面 S位于曲线 C上方的部分.

**答案:**(19) 点P的轨迹C为<equation>\left\{\begin{array}{l l}x^{2}+y^{2}+z^{2}-yz=1\\ y=2z,\end{array}\right.</equation>或者<equation>\left\{\begin{array}{l l}x^{2}+\frac{3}{4} y^{2}=1\\ y=2z,\end{array}\right.</equation>曲面积分为<equation>I=2\pi.</equation>

**解析:**解设点 P的坐标为（x,y,z），则椭球面 S在点 P处的法向量为（2x，2y-z，2z-y）.又 xOy面的法向量可取为（0,0,1），故由 S在点 P处的切平面与 xOy面垂直知，<equation>(2 x, 2 y - z, 2 z - y) \cdot (0, 0, 1) = 0,</equation>即有<equation>y = 2z</equation>. 由于点<equation>P</equation>在椭球面<equation>S</equation>上，故点<equation>P</equation>的轨迹<equation>C</equation>为<equation>\left\{ \begin{array}{l l} x ^ {2} + y ^ {2} + z ^ {2} - y z = 1, \\ y = 2 z, \end{array} \right. \text {或 者} \left\{ \begin{array}{l l} x ^ {2} + \frac {3}{4} y ^ {2} = 1, \\ y = 2 z. \end{array} \right.</equation>下面用两种方法求曲面积分 I.

（法一）<equation>\varSigma</equation>在xOy面上的投影区域为<equation>D_{xy}=\left\{(x,y)\mid x^{2}+\frac{3}{4} y^{2}\leqslant 1\right\}</equation>，其面积为<equation>\pi \cdot 1\cdot \frac{2}{\sqrt{3}}=\frac{2}{\sqrt{3}}\pi.</equation>对方程<equation>x^{2}+y^{2}+z^{2}-yz=1</equation>两边关于x,y分别求偏导数，得<equation>2 x + 2 z \frac {\partial z}{\partial x} - y \frac {\partial z}{\partial x} = 0, \quad 2 y + 2 z \frac {\partial z}{\partial y} - z - y \frac {\partial z}{\partial y} = 0,</equation>解得<equation>\frac{\partial z}{\partial x} = \frac{2x}{y - 2z},\frac{\partial z}{\partial y} = \frac{2y - z}{y - 2z}</equation>. 在<equation>\varSigma</equation>上，<equation>x^{2}+y^{2}+z^{2}-yz=1</equation>，故<equation>\begin{aligned} \sqrt {1 + \left(\frac {\partial z}{\partial x}\right) ^ {2} + \left(\frac {\partial z}{\partial y}\right) ^ {2}} &= \frac {\sqrt {4 x ^ {2} + 5 y ^ {2} + 5 z ^ {2} - 8 y z}}{| y - 2 z |} = \frac {\sqrt {4 \left(x ^ {2} + y ^ {2} + z ^ {2} - y z\right) + y ^ {2} + z ^ {2} - 4 y z}}{| y - 2 z |} \\ &= \frac {\sqrt {4 + y ^ {2} + z ^ {2} - 4 y z}}{| y - 2 z |}. \end{aligned}</equation>从而<equation>\begin{aligned} I &= \iint_ {\Sigma} \frac {\left(x + \sqrt {3}\right) \mid y - 2 z \mid}{\sqrt {4 + y ^ {2} + z ^ {2}} - 4 y z} \mathrm {d} S = \iint_ {D _ {x y}} \frac {\left(x + \sqrt {3}\right) \mid y - 2 z \mid}{\sqrt {4 + y ^ {2} + z ^ {2}} - 4 y z} \cdot \sqrt {1 + \left(\frac {\partial z}{\partial x}\right) ^ {2} + \left(\frac {\partial z}{\partial y}\right) ^ {2}} \mathrm {d} x \mathrm {d} y \\ &= \iint_ {D _ {x y}} \left(x + \sqrt {3}\right) \mathrm {d} x \mathrm {d} y \stackrel {\text {对 称 性}} {=} 0 + \iint_ {D _ {x y}} \sqrt {3} \mathrm {d} x \mathrm {d} y = \sqrt {3} \cdot \frac {2}{\sqrt {3}} \pi = 2 \pi . \end{aligned}</equation>（法二）<equation>\varSigma</equation>在 xOy面上的投影区域为<equation>D_{xy}=\left\{(x,y)\left|x^{2}+\frac{3}{4} y^{2}\leqslant 1\right.\right\}</equation>，其面积为<equation>\pi\cdot1\cdot\frac{2}{\sqrt{3}}=\frac{2}{\sqrt{3}}\pi.</equation><equation>\varSigma</equation>上任一点的法向量为（2x，2y-z，2z-y），其方向余弦<equation>\cos \gamma</equation>满足<equation>| \cos \gamma | = \frac {\left| 2 z - y \right|}{\sqrt {\left(2 x\right) ^ {2} + \left(2 y - z\right) ^ {2} + \left(2 z - y\right) ^ {2}}} = \frac {\left| 2 z - y \right|}{\sqrt {4 x ^ {2} + 5 y ^ {2} + 5 z ^ {2} - 8 y z}}.</equation>又<equation>\Sigma</equation>上的点满足<equation>x^{2}+y^{2}+z^{2}-yz=1</equation>，故有<equation>|\cos \gamma |=\frac{|2z-y|}{\sqrt{4+y^{2}+z^{2}-4yz}}</equation>，从而<equation>\begin{aligned} I &= \iint_ {\Sigma} \frac {(x + \sqrt {3}) | y - 2 z |}{\sqrt {4 + y ^ {2} + z ^ {2}} - 4 y z} \mathrm {d} S = \iint_ {\Sigma} (x + \sqrt {3}) | \cos \gamma | \mathrm {d} S \\ &= \iint_ {D _ {x y}} (x + \sqrt {3}) \mathrm {d} x \mathrm {d} y \xlongequal {\text {对称性}} 0 + \iint_ {D _ {x y}} \sqrt {3} \mathrm {d} x \mathrm {d} y \\ &= \sqrt {3} \cdot \frac {2}{\sqrt {3}} \pi = 2 \pi . \end{aligned}</equation>

---


#### 重积分的概念与性质

**2010年第4题 | 选择题 | 4分 | 答案: D**

4.<equation>\lim_{n\rightarrow \infty}\sum_{i=1}^{n}\sum_{j=1}^{n}\frac{n}{(n+i)(n^{2}+j^{2})}=</equation>(    )

A.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{x}\frac{1}{(1+x)(1+y^{2})}\mathrm{d}y</equation>B.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{x}\frac{1}{(1+x)(1+y)}\mathrm{d}y</equation>C.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{1}\frac{1}{(1+x)(1+y)}\mathrm{d}y</equation>D.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{1}\frac{1}{(1+x)(1+y^{2})}\mathrm{d}y</equation>

答案: D

**解析:**解 （法一）考虑将原极限写成二重积分.

令<equation>\Delta \sigma_{ij} = \left[\frac{i - 1}{n},\frac{i}{n}\right]\times \left[\frac{j - 1}{n},\frac{j}{n}\right](i,j = 1,2,\dots ,n)</equation>，则<equation>\{\Delta \sigma_{ij}\}_{1\leqslant i,j\leqslant n}</equation>为<equation>D = [0,1]\times [0,1]</equation>上的一个划分，<equation>\Delta \sigma_{ij}</equation>的面积为<equation>\frac{1}{n^2}</equation>.取<equation>\Delta \sigma_{ij}</equation>上的一点<equation>\left(\frac{i}{n},\frac{j}{n}\right)</equation>.

由于<equation>\sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {n}{(n + i) \left(n ^ {2} + j ^ {2}\right)} = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {1}{\left(1 + \frac {i}{n}\right) \left(1 + \frac {j ^ {2}}{n ^ {2}}\right)} \cdot \frac {1}{n ^ {2}},</equation>故<equation>\begin{aligned} \text {原 极 限} &= \lim _ {n \rightarrow \infty} \left[ \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {1}{\left(1 + \frac {i}{n}\right)\left(1 + \frac {j ^ {2}}{n ^ {2}}\right)} \right] = \iint_ {D} \frac {1}{(1 + x) \left(1 + y ^ {2}\right)} \mathrm {d} \sigma \\ &= \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {1} \frac {1}{(1 + x) \left(1 + y ^ {2}\right)} \mathrm {d} y. \end{aligned}</equation>应选 D.

（法二）由于所求极限的表达式中 i，j无关，故可以考虑将原极限写成定积分的乘积.由于<equation>\begin{aligned} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {n}{(n + i) \left(n ^ {2} + j ^ {2}\right)} &= \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \left(\frac {1}{1 + \frac {i}{n}} \cdot \frac {1}{n}\right) \left(\frac {1}{1 + \frac {j ^ {2}}{n ^ {2}}} \cdot \frac {1}{n}\right) \\ \underline {{i , j \text {无关}}} \sum_ {i = 1} ^ {n} \left(\frac {1}{1 + \frac {i}{n}} \cdot \frac {1}{n}\right) \sum_ {j = 1} ^ {n} \left(\frac {1}{1 + \frac {j ^ {2}}{n ^ {2}}} \cdot \frac {1}{n}\right), \end{aligned}</equation>故<equation>\begin{aligned} &= \lim _ {n \rightarrow \infty} \sum_ {i = 1} ^ {n} \left(\frac {1}{1 + \frac {i}{n}} \cdot \frac {1}{n}\right) \cdot \lim _ {n \rightarrow \infty} \sum_ {j = 1} ^ {n} \left(\frac {1}{1 + \frac {j ^ {2}}{n ^ {2}}} \cdot \frac {1}{n}\right) = \left(\int_ {0} ^ {1} \frac {1}{1 + x} \mathrm {d} x\right)\left(\int_ {0} ^ {1} \frac {1}{1 + y ^ {2}} \mathrm {d} y\right) \\ &= \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {1} \frac {1}{(1 + x) \left(1 + y ^ {2}\right)} \mathrm {d} y. \end{aligned}</equation>应选 D.

---

**2009年第2题 | 选择题 | 4分 | 答案: A**

2. 如图，正方形<equation>\{(x,y)\mid|x|\leqslant1,|y|\leqslant1\}</equation>被其对角线划分为四个区域<equation>D_{k}(k=1,2,3,4),I_{k}=\iint_{D_{k}}y\cos x\mathrm{d}x\mathrm{d}y</equation>则<equation>\max_{1\leqslant k\leqslant4}\{I_{k}\}=</equation>（    ）

A.<equation>I_{1}</equation>B.<equation>I_{2}</equation>C.<equation>I_{3}</equation>D.<equation>I_{4}</equation>

答案: A

**解析:**解 令<equation>f ( x,y)=y \cos x</equation>，由于<equation>D_{4}</equation>关于x轴对称，且<equation>f ( x,y)=-f ( x,-y)</equation>，故<equation>I_{4}=0</equation>.同理得到<equation>I_{2}=0</equation>.又<equation>f ( x,y)</equation>在<equation>D_{1}</equation>内部恒大于0，在<equation>D_{3}</equation>内部恒小于0，故由重积分的保号性知，<equation>I_{1}>0, I_{3}<0.</equation>综上所述，<equation>\max_{1\leq k\leq 4}\left\{I_{k}\right\}=I_{1}</equation>应选A.

---


### 函数、极限、连续


#### 函数极限的计算

**2025年第11题 | 填空题 | 5分**

<equation>1 1. \lim _ {x \rightarrow 0 ^ {+}} \frac {x ^ {x} - 1}{\ln x \cdot \ln (1 - x)} = \underline {{}}</equation>

**解析:**解 由于<equation>x^{x}=\mathrm{e}^{x\ln x}</equation>，且当<equation>x\to0</equation>时，<equation>\mathrm{e}^{x}-1\sim x</equation>，故<equation>\lim_{x\to0^{+}}\frac{x^{x}-1}{\ln x\cdot\ln(1-x)}=\lim_{x\to0^{+}}\frac{\mathrm{e}^{x\ln x}-1}{\ln x\cdot\ln(1-x)} \frac{\mathrm{e}^{x\ln x}-1\sim x\ln x}{\ln(1-x)\sim-x} \lim_{x\to0^{+}}\frac{x\ln x}{\ln x\cdot(-x)}=-1.</equation>

---

**2021年第17题 | 解答题 | 10分**

17. (本题满分10分)

求极限 lim<equation>\left(\frac {1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t}{\mathrm {e} ^ {x} - 1} - \frac {1}{\sin x}\right)</equation>

**解析:**解 （法一）先整理原极限再计算.<equation>\begin{array}{l} \frac {\mathrm {e} ^ {x} - 1 \sim x}{\sin x \sim x} \lim _ {x \rightarrow 0} \frac {\int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t}{x} + \lim _ {x \rightarrow 0} \frac {\sin x - \mathrm {e} ^ {x} + 1}{x ^ {2}} \\ \frac {\text {洛必达}}{} \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x ^ {2}}}{1} + \lim _ {x \rightarrow 0} \frac {x - \frac {x ^ {3}}{6} - 1 - x - \frac {x ^ {2}}{2} + 1 + o \left(x ^ {2}\right)}{x ^ {2}} \\ = 1 + \lim _ {x \rightarrow 0} \frac {- \frac {x ^ {2}}{2} + o \left(x ^ {2}\right)}{x ^ {2}} = 1 - \frac {1}{2} = \frac {1}{2}. \\ \end{array}</equation>因此，原极限<equation>= \frac{1}{2}</equation>（法二）将原极限通分整理，化为<equation>\frac{0}{0}</equation>型未定式后再应用洛必达法则.<equation>\begin{aligned} \mathrm {原 极 限} &= \lim _ {x \rightarrow 0} \frac {\sin x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) - \mathrm {e} ^ {x} + 1}{\left(\mathrm {e} ^ {x} - 1\right) \sin x} \\ \frac {\mathrm {e} ^ {x} - 1 \sim x}{\sin x \sim x} \lim _ {x \rightarrow 0} \frac {\sin x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) - \mathrm {e} ^ {x} + 1}{x ^ {2}} \\ \underline {{\text {洛必达}}} \lim _ {x \rightarrow 0} \frac {\cos x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) + \sin x \cdot \mathrm {e} ^ {x ^ {2}} - \mathrm {e} ^ {x}}{2 x} \\ \underline {{\text {洛必达}}} \lim _ {x \rightarrow 0} \frac {- \sin x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) + \cos x \cdot \mathrm {e} ^ {x ^ {2}} + \cos x \cdot \mathrm {e} ^ {x ^ {2}} + 2 x \cdot \sin x \cdot \mathrm {e} ^ {x ^ {2}} - \mathrm {e} ^ {x}}{2} &= \frac {1}{2}. \\ \mathrm {因 此 , 原 极 限} &= \frac {1}{2}. \end{aligned}</equation>

---

**2020年第9题 | 填空题 | 4分**

9. lim

**答案:**```latex

-1.
```
**解析: **解 通分整理原极限.<equation>\lim _ {x \rightarrow 0} \left[ \frac {1}{\mathrm {e} ^ {x} - 1} - \frac {1}{\ln (1 + x)} \right] = \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - \mathrm {e} ^ {x} + 1}{\left(\mathrm {e} ^ {x} - 1\right) \ln (1 + x)} \frac {\mathrm {e} ^ {x} - 1 \sim x}{\ln (1 + x) \sim x} \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - \mathrm {e} ^ {x} + 1}{x ^ {2}}.</equation>下面用两种方法计算<equation>\lim_{x\to 0}\frac{\ln(1 + x) - \mathrm{e}^{x} + 1}{x^{2}}.</equation>（法一）利用泰勒公式.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - \mathrm {e} ^ {x} + 1}{x ^ {2}} &= \lim _ {x \rightarrow 0} \frac {x - \frac {x ^ {2}}{2} + o \left(x ^ {2}\right) - \left[ 1 + x + \frac {x ^ {2}}{2} + o \left(x ^ {2}\right)\right] + 1}{x ^ {2}} \\ &= \lim _ {x \rightarrow 0} \frac {- x ^ {2} + o \left(x ^ {2}\right)}{x ^ {2}} = - 1. \end{aligned}</equation>（法二）利用洛必达法则.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - \mathrm {e} ^ {x} + 1}{x ^ {2}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\frac {1}{1 + x} - \mathrm {e} ^ {x}}{2 x} &= \lim _ {x \rightarrow 0} \frac {1 - \mathrm {e} ^ {x} (1 + x)}{2 x (1 + x)} = \frac {1}{2} \lim _ {x \rightarrow 0} \frac {1 - \mathrm {e} ^ {x} - x \mathrm {e} ^ {x}}{x} \\ &= \frac {1}{2} \lim _ {x \rightarrow 0} \left(\frac {1 - \mathrm {e} ^ {x}}{x} - \mathrm {e} ^ {x}\right) \xlongequal {\text {洛必达}} \frac {1 - \mathrm {e} ^ {x} \sim - x}{2} \frac {1}{2} \times (- 1 - 1) = - 1. \end{aligned}</equation>

---

**2016年第9题 | 填空题 | 4分**
9. lim
**答案: **# 1 2.
**解析: **解 当<equation>x\to0</equation>时，<equation>1-\cos x^{2}\sim\frac{1}{2} x^{4},\ln(1+x\sin x)\sim x\sin x</equation>从而<equation>\lim _ {x \rightarrow 0} \frac {\int_ {0} ^ {x} t \ln (1 + t \sin t) \mathrm {d} t}{1 - \cos x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\int_ {0} ^ {x} t \ln (1 + t \sin t) \mathrm {d} t}{\frac {1}{2} x ^ {4}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {x \ln (1 + x \sin x)}{2 x ^ {3}} = \lim _ {x \rightarrow 0} \frac {x \cdot x \sin x}{2 x ^ {3}} = \frac {1}{2}.</equation>

---

**2015年第9题 | 填空题 | 4分**
（无内容）
**解析: **解 （法一）利用洛必达法则.<equation>\lim _ {x \rightarrow 0} \frac {\ln (\cos x)}{x ^ {2}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\frac {1}{\cos x} \cdot (- \sin x)}{2 x} = \lim _ {x \rightarrow 0} \left(- \frac {\sin x}{2 x}\right) = - \frac {1}{2}.</equation>（法二）利用等价无穷小替换.

当<equation>x\to 0</equation>时，<equation>\cos x - 1\to 0,\ln (1 + \cos x - 1)\sim \cos x - 1</equation>，于是<equation>\lim _ {x \rightarrow 0} \frac {\ln (\cos x)}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\ln (1 + \cos x - 1)}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\cos x - 1}{x ^ {2}} \frac {1 - \cos x - \frac {1}{2} x ^ {2}}{\overline {{=}}} \lim _ {x \rightarrow 0} \frac {- \frac {1}{2} x ^ {2}}{x ^ {2}} = - \frac {1}{2}.</equation>

---

**2014年第15题 | 解答题 | 10分**
15. (本题满分10分)

求极限<equation>\lim _ {x \rightarrow + \infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right)-t \right] \mathrm {d} t}{x ^ {2} \ln \left(1 + \frac {1}{x}\right)}.</equation>
**答案: **<equation>(1 5) \frac {1}{2}.</equation>
**解析: **解 由于<equation>\mathrm{e}^{x}</equation>在 x=0处的带拉格朗日余项的2阶泰勒公式为<equation>\mathrm{e}^{x}=1+x+\frac{x^{2}}{2}+\frac{\mathrm{e}^{\theta x}}{3!} x^{3}</equation>其中<equation>0 < \theta < 1</equation>，故当 x > 0时，<equation>\mathrm{e}^{x}>1+x+\frac{x^{2}}{2}.</equation>于是，<equation>\mathrm{e}^{\frac{1}{t}}-1 > \frac{1}{t}+\frac{1}{2t^{2}}(t > 0),</equation><equation>t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t > t ^ {2} \left(\frac {1}{t} + \frac {1}{2 t ^ {2}}\right) - t = \frac {1}{2}.</equation>从而<equation>\int_{1}^{+\infty}\left[ t^{2}\left(\mathrm{e}^{\frac{1}{t}} - 1\right) - t\right]\mathrm{d}t\to +\infty .</equation>另一方面，<equation>\lim _ {x \rightarrow + \infty} \left[ x ^ {2} \ln \left(1 + \frac {1}{x}\right)\right] \xlongequal {\ln \left(1 + \frac {1}{x}\right) \sim \frac {1}{x}} \lim _ {x \rightarrow + \infty} x = + \infty .</equation>因此，原极限为<equation>\frac{\infty}{\infty}</equation>型未定式.

当<equation>x\to +\infty</equation>时，<equation>\ln \left(1 + \frac{1}{x}\right)\sim \frac{1}{x}</equation>，故<equation>\begin{aligned} \lim _ {x \rightarrow + \infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t \right] \mathrm {d} t}{x ^ {2} \ln \left(1 + \frac {1}{x}\right)} \xlongequal {\ln \left(1 + \frac {1}{x}\right) \sim \frac {1}{x}} \lim _ {x \rightarrow + \infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t \right] \mathrm {d} t}{x} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow + \infty} \frac {x ^ {2} \left(\mathrm {e} ^ {\frac {1}{x}} - 1\right) - x}{1} &= \lim _ {x \rightarrow + \infty} \frac {\mathrm {e} ^ {\frac {1}{x}} - 1 - \frac {1}{x}}{\frac {1}{x ^ {2}}} \\ \xlongequal {u = \frac {1}{x}} \lim _ {u \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {u} - u - 1}{u ^ {2}} \xlongequal {\text {洛必达}} \lim _ {u \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {u} - 1}{2 u} \\ \xlongequal {\mathrm {e} ^ {u} - 1 \sim u} \lim _ {u \rightarrow 0 ^ {+}} \frac {u}{2 u} &= \frac {1}{2}. \end{aligned}</equation>因此，原极限<equation>= \frac{1}{2}.</equation>将原极限化简为<equation>\lim_{x\to +\infty}[x^{2}(\mathrm{e}^{\frac{1}{x}} -1) - x]</equation>后，也可以用泰勒公式来求该极限.

当<equation>x\to +\infty</equation>时，<equation>\frac{1}{x}\rightarrow 0^{+}</equation>.由<equation>\mathrm{e}^{u}</equation>在<equation>u = 0</equation>处的泰勒公式得，<equation>\mathrm {e} ^ {\frac {1}{x}} = 1 + \frac {1}{x} + \frac {1}{2 !} \cdot \frac {1}{x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right).</equation>从而，<equation>\begin{array}{l} \lim _ {x \rightarrow + \infty} \left[ x ^ {2} \left(\mathrm {e} ^ {\frac {1}{x}} - 1\right) - x \right] = \lim _ {x \rightarrow + \infty} \left\{x ^ {2} \left[ \frac {1}{x} + \frac {1}{2 !} \cdot \frac {1}{x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right)\right] - x \right\} \\ = \lim _ {x \rightarrow + \infty} \left[ \frac {1}{2} + x ^ {2} \cdot o \left(\frac {1}{x ^ {2}}\right)\right] = \frac {1}{2}. \\ \end{array}</equation>

---

**2011年第15题 | 解答题 | 10分**
15. (本题满分10分)
**解析: **解（法一）由于当<equation>x\to 0</equation>时，<equation>\frac{\ln(1+x)}{x}>0</equation>，故可以对函数<equation>\left[\frac{\ln(1+x)}{x}\right]^{\frac{1}{e^{x}-1}}</equation>取对数.又<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {1}{\mathrm {e} ^ {x} - 1} \ln \frac {\ln (1 + x)}{x} \xlongequal {\mathrm {e} ^ {x} - 1 \sim x} \lim _ {x \rightarrow 0} \frac {\ln \left[ 1 + \frac {\ln (1 + x) - x}{x} \right]}{x} \\ \xlongequal {\ln (1 + t) - t} \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - x}{x ^ {2}} \\ = \lim _ {x \rightarrow 0} \frac {x - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right) - x}{x ^ {2}} = - \frac {1}{2}, \\ \end{array}</equation>故<equation>\lim_{x\to 0}\left[\frac{\ln(1 + x)}{x}\right]^{\frac{1}{e^x - 1}} = \mathrm{e}^{-\frac{1}{2}}.</equation>(法二)<equation>\lim_{x\to 0}\left[\frac{\ln(1 + x)}{x}\right]^{\frac{1}{e^x - 1}} = \lim_{x\to 0}\left[1 + \frac{\ln(1 + x) - x}{x}\right]^{\frac{x}{\ln(1 + x) - x} \cdot \frac{\ln(1 + x) - x}{x} \cdot \frac{1}{e^x - 1}}.</equation>由于<equation>\lim _ {x \rightarrow 0} \left[ \frac {\ln (1 + x) - x}{x} \cdot \frac {1}{\mathrm {e} ^ {x} - 1} \right] = \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - x}{x ^ {2}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\frac {1}{1 + x} - 1}{2 x} = \lim _ {x \rightarrow 0} \frac {- 1}{2 (1 + x)} = - \frac {1}{2},</equation><equation>= \mathrm {e} ^ {- \frac {1}{2}}</equation>（法三）由于

注意该技巧！添加绝对值后不用分情况讨论.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {1}{\mathrm {e} ^ {x} - 1} \ln \frac {\ln (1 + x)}{x} &= \lim _ {x \rightarrow 0} \frac {\ln \left| \frac {\ln (1 + x)}{x} \right|}{\mathrm {e} ^ {x} - 1} = \lim _ {x \rightarrow 0} \frac {\ln | \ln (1 + x) | - \ln | x |}{x} \\ \underline {{\text {洛必达}}} \lim _ {x \rightarrow 0} \left[ \frac {\frac {1}{1 + x}}{\ln (1 + x)} - \frac {1}{x} \right] &= \lim _ {x \rightarrow 0} \frac {x - (1 + x) \ln (1 + x)}{x (1 + x) \ln (1 + x)} \\ \underline {{\frac {\ln (1 + x) - x}{\lim _ {x \rightarrow 0} (1 + x) = 1}}} \lim _ {x \rightarrow 0} \frac {x - (1 + x) \ln (1 + x)}{x ^ {2}} \\ \underline {{\text {洛必达}}} \lim _ {x \rightarrow 0} \frac {- \ln (1 + x)}{2 x} &= - \frac {1}{2}, \end{aligned}</equation>故<equation>\lim_{x\to 0}\left[\frac{\ln(1 + x)}{x}\right]^{\frac{1}{e^x - 1}} = \mathrm{e}^{-\frac{1}{2}}.</equation>

---

**2010年第1题 | 选择题 | 4分 | 答案: C**
1. 极限<equation>\lim_{x\to \infty}\left[\frac{x^{2}}{(x-a)(x+b)}\right]^{x}=(\quad)</equation>A. 1 B. e C.<equation>e^{a-b}</equation>D.<equation>e^{b-a}</equation>
答案: C
**解析: **解（法一）若 a,b 不同时为0，则<equation>( a-b) x+a b\neq0</equation>由<equation>\lim_{x\to\infty}\frac{(a-b)x+ab}{(x-a)(x+b)}=0</equation>以及重要极限<equation>\lim_{x\to\infty}\left(1+\frac{1}{x}\right)^{x}=e</equation>的复合形式可知，<equation>\begin{aligned} \lim _ {x \rightarrow \infty} \left[ \frac {x ^ {2}}{(x - a) (x + b)} \right] ^ {x} &= \lim _ {x \rightarrow \infty} \left[ 1 + \frac {(a - b) x + a b}{(x - a) (x + b)} \right] ^ {x} \\ &= \lim _ {x \rightarrow \infty} \left[ \left[ 1 + \frac {(a - b) x + a b}{(x - a) (x + b)} \right] ^ {\frac {(x - a) (x + b)}{(a - b) x + a b}} \right] ^ {\left[ \frac {(a - b) x + a b}{(x - a) (x + b)} \cdot x \right]} \\ &= \mathrm {e} ^ {\lim _ {x \rightarrow \infty} \frac {(a - b) x ^ {2} + a b x}{x ^ {2} - (a - b) x - a b}} = \mathrm {e} ^ {\lim _ {x \rightarrow \infty} \frac {(a - b) + \frac {a b}{x}}{- \frac {a - b}{x} - \frac {a b}{x ^ {2}}}} = \mathrm {e} ^ {a - b}. \end{aligned}</equation>若<equation>a = b = 0</equation>，则原式<equation>= \lim_{x\to \infty}1^{x} = 1 = \mathrm{e}^{a - b}</equation>.

综上所述，应选C.

（法二）当<equation>x\to \infty</equation>时（无论是<equation>+\infty</equation>还是<equation>-\infty</equation>），<equation>\frac{x^{2}}{(x-a)(x+b)}>0</equation>，故可以对<equation>\left[ \frac{x^{2}}{(x-a)(x+b)} \right]^{x}</equation>取对数.又<equation>\begin{aligned} \lim _ {x \rightarrow \infty} \ln \left[ \frac {x ^ {2}}{(x - a) (x + b)} \right] ^ {x} &= \lim _ {x \rightarrow \infty} x \ln \frac {x ^ {2}}{(x - a) (x + b)} = \lim _ {x \rightarrow \infty} x \ln \left[ 1 + \frac {(a - b) x + a b}{(x - a) (x + b)} \right] \\ &= \lim _ {x \rightarrow \infty} \left[ x \cdot \frac {(a - b) x + a b}{(x - a) (x + b)} \right] = \lim _ {x \rightarrow \infty} \frac {(a - b) x ^ {2} + a b x}{(x - a) (x + b)} = a - b, \end{aligned}</equation>故原式<equation>= \mathrm{e}^{a - b}.</equation>应选C.

---


#### 确定极限中的参数

**2024年第11题 | 填空题 | 5分**
<equation>. \mathrm {若} \lim _ {x \rightarrow 0} \frac {\left(1 + a x ^ {2}\right) ^ {\sin x} - 1}{x ^ {3}} = 6, \mathrm {则} a = \underline {{}}</equation>
**答案: **## a=6.
**解析: **<equation>\begin{aligned} 6 &= \lim _ {x \rightarrow 0} \frac {\left(1 + a x ^ {2}\right) ^ {\sin x} - 1}{x ^ {3}} = \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {\sin x \ln \left(1 + a x ^ {2}\right)} - 1}{x ^ {3}} = \lim _ {x \rightarrow 0} \frac {\sin x \ln \left(1 + a x ^ {2}\right)}{x ^ {3}} \\ &= \lim _ {x \rightarrow 0} \frac {x \cdot a x ^ {2}}{x ^ {3}} = a. \end{aligned}</equation>因此，<equation>a=6.</equation>

---

**2023年第11题 | 填空题 | 5分**
11. 当<equation>x \to0</equation>时，函数<equation>f(x)=ax+bx^{2}+\ln(1+x)</equation>与<equation>g(x)=\mathrm{e}^{x^{2}}-\cos x</equation>是等价无穷小，则 ab=___
**答案: **<equation>- 2.</equation>
**解析: **解分别写出<equation>f ( x )</equation>与<equation>g ( x )</equation>在<equation>x=0</equation>处的二阶泰勒公式.当<equation>x\to0</equation>时，<equation>f (x) = a x + b x ^ {2} + x - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right) = (a + 1) x + \left(b - \frac {1}{2}\right) x ^ {2} + o \left(x ^ {2}\right),</equation><equation>g (x) = 1 + x ^ {2} + o \left(x ^ {2}\right) - \left[ 1 - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right) \right] = \frac {3}{2} x ^ {2} + o \left(x ^ {2}\right).</equation>由于<equation>f(x)</equation>与<equation>g(x)</equation>是<equation>x\to 0</equation>时的等价无穷小，故<equation>1 = \lim _ {x \rightarrow 0} \frac {f (x)}{g (x)} = \lim _ {x \rightarrow 0} \frac {(a + 1) x + \left(b - \frac {1}{2}\right) x ^ {2} + o \left(x ^ {2}\right)}{\frac {3}{2} x ^ {2} + o \left(x ^ {2}\right)}.</equation>由（1）式成立可得<equation>a+1=0,b-\frac{1}{2}=\frac{3}{2}.</equation>解得<equation>a=-1,b=2.</equation>因此，<equation>ab=-2.</equation>

---

**2019年第1题 | 选择题 | 4分 | 答案: C**
1. 当 x→0时，若 x-tanx与<equation>x^{k}</equation>是同阶无穷小，则 k=（    ）

A.1 B.2 C.3 D.4
答案: C
**解析: **解 首先，由于当<equation>x\to0</equation>时，<equation>x-\tan x\to0</equation>，而<equation>\lim_{x\to0}\frac{x-\tan x}{x^{k}}</equation>为非零常数，故 k > 0.下面用两种方法讨论<equation>\lim_{x\to0}\frac{x-\tan x}{x^{k}}.</equation>（法一）由于<equation>\tan x=x+\frac{x^{3}}{3}+o\left(x^{3}\right)</equation>，故<equation>\lim _ {x \rightarrow 0} \frac {x - \tan x}{x ^ {k}} = \lim _ {x \rightarrow 0} \frac {- \frac {x ^ {3}}{3} + o \left(x ^ {3}\right)}{x ^ {k}}.</equation>当 k > 3时，该极限为<equation>\infty</equation>；当0 < k < 3时，该极限为0；当 k=3时，该极限为<equation>-\frac{1}{3}.</equation>于是，<equation>x-\tan x</equation>与<equation>x^{3}</equation>是同阶无穷小，k=3.

因此，应选C.

（法二）利用洛必达法则讨论<equation>\lim_{x\to 0}\frac{x - \tan x}{x^k}</equation>.<equation>\lim _ {x \rightarrow 0} \frac {x - \tan x}{x ^ {k}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - \sec^ {2} x}{k x ^ {k - 1}} = \lim _ {x \rightarrow 0} \frac {- \tan^ {2} x}{k x ^ {k - 1}} \xlongequal {\tan x \sim x} \lim _ {x \rightarrow 0} \frac {- x ^ {2}}{k x ^ {k - 1}}.</equation>当 k > 3时，该极限为<equation>\infty</equation>；当0 < k < 3时，该极限为0；当 k=3时，该极限为<equation>-\frac{1}{3}.</equation>于是，<equation>x-\tan x</equation>与<equation>x^{3}</equation>是同阶无穷小， k=3.

因此，应选C.

---

**2018年第9题 | 填空题 | 4分**
9. 若<equation>\lim_{x\rightarrow 0}\left(\frac{1-\tan x}{1+\tan x}\right)^{\frac{1}{\sin k x}}=\mathrm{e}</equation>，则 k= ___
**解析: **解（法一）对原极限进行恒等变形，再凑重要极限.<equation>\lim _ {x \rightarrow 0} \left(\frac {1 - \tan x}{1 + \tan x}\right) ^ {\frac {1}{\sin k x}} = \lim _ {x \rightarrow 0} \left(1 - \frac {2 \tan x}{1 + \tan x}\right) ^ {\frac {1}{\sin k x}} = \lim _ {x \rightarrow 0} \left(1 - \frac {2 \tan x}{1 + \tan x}\right) ^ {\frac {1 + \tan x}{- 2 \tan x} \cdot \frac {- 2 \tan x}{1 + \tan x} \cdot \frac {1}{\sin k x}}.</equation>因为<equation>\lim _ {x \rightarrow 0} \left(\frac {- 2 \tan x}{1 + \tan x} \cdot \frac {1}{\sin k x}\right) = \lim _ {x \rightarrow 0} \frac {- 2 \tan x}{\sin k x} \frac {\tan x \sim x}{\sin k x \sim k x} \lim _ {x \rightarrow 0} \frac {- 2 x}{k x} = - \frac {2}{k},</equation>所以原极限<equation>= \mathrm{e}^{-\frac{2}{k}} = \mathrm{e}.</equation>因此，<equation>-\frac{2}{k} = 1,k = -2.</equation>（法二）取对数，再求极限.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \left(\frac {1 - \tan x}{1 + \tan x}\right) ^ {\frac {1}{\sin k x}} &= \lim _ {x \rightarrow 0} \mathrm {e} ^ {\frac {1}{\sin k x} \cdot \ln \left(\frac {1 - \tan x}{1 + \tan x}\right)} = \mathrm {e} ^ {\lim _ {x \rightarrow 0} \frac {1}{\sin k x} \cdot \ln \left(1 - \frac {2 \tan x}{1 + \tan x}\right)} \\ \frac {\ln \left(1 - \frac {2 \tan x}{1 + \tan x}\right) \sim \frac {- 2 \tan x}{1 + \tan x}}{\frac {\tan x \sim x}{\sin k x \sim k x}} \mathrm {e} ^ {\lim _ {x \rightarrow 0} \frac {- 2 x}{k x}} &= \mathrm {e} ^ {- \frac {2}{k}}. \end{aligned}</equation>由于原极限<equation>= \mathrm{e}</equation>，故<equation>-\frac{2}{k} = 1</equation>，即<equation>k = -2.</equation>

---

**2015年第15题 | 解答题 | 10分**
15. (本题满分10分)

设函数<equation>f(x)=x+a\ln(1+x)+bx\sin x,g(x)=kx^{3}.</equation>若 f(x)与 g(x)在<equation>x\rightarrow0</equation>时是等价无穷小，求 a,b,k的值.
**解析: **由于 g(x）中 x的次数为3，故可考虑写出 f(x)在 x=0处的3阶泰勒公式.

由<equation>\ln (1 + x) = x - \frac {x ^ {2}}{2} + \frac {x ^ {3}}{3} + o \left(x ^ {3}\right), \quad \sin x = x - \frac {x ^ {3}}{3 !} + o \left(x ^ {3}\right),</equation>可得<equation>f (x) = x + a x - \frac {a x ^ {2}}{2} + \frac {a x ^ {3}}{3} + b x ^ {2} + o \left(x ^ {3}\right) = (a + 1) x + \left(b - \frac {a}{2}\right) x ^ {2} + \frac {a}{3} x ^ {3} + o \left(x ^ {3}\right).</equation>记<equation>I=\lim_{x\to 0}\frac{f(x)}{g(x)}=\lim_{x\to 0}\frac{(a+1)x+\left(b-\frac{a}{2}\right)x^{2}+\frac{a}{3}x^{3}+o\left(x^{3}\right)}{kx^{3}}.</equation>由等价无穷小量的定义知<equation>I=1.</equation>首先，<equation>k\neq 0</equation>当 k≠0时，若 I存在，则必有<equation>\left\{\begin{array}{l l}a+1=0,\\ b-\frac{a}{2}=0,\end{array}\right.</equation>否则<equation>I=\infty.</equation>解得 a=-1，b=-<equation>\frac{1}{2}.</equation>又因为 I=1，所以<equation>\frac{a}{3}=k,k=-\frac{1}{3}.</equation>综上所述，<equation>a = -1</equation>，<equation>b = -\frac{1}{2}</equation>，<equation>k = -\frac{1}{3}</equation>

---

**2013年第1题 | 选择题 | 4分 | 答案: D**
1. 已知极限<equation>\lim_{x\rightarrow 0}\frac{x-\arctan x}{x^{k}}=c</equation>，其中 k,c为常数，且<equation>c\neq 0</equation>，则（    )

A. k=2, c=-<equation>\frac{1}{2}</equation>B. k=2, c=<equation>\frac{1}{2}</equation>C. k=3, c=-<equation>\frac{1}{3}</equation>D. k=3, c=<equation>\frac{1}{3}</equation>
答案: D
**解析: **解（法一）当<equation>x\to0</equation>时，<equation>\arctan x=x-\frac{x^{3}}{3}+o\left(x^{3}\right)</equation>，于是<equation>0 \neq c = \lim _ {x \rightarrow 0} \frac {x - \arctan x}{x ^ {k}} = \lim _ {x \rightarrow 0} \frac {\frac {x ^ {3}}{3} + o \left(x ^ {3}\right)}{x ^ {k}}.</equation>当<equation>k > 3</equation>时，<equation>\lim_{x\to 0}\frac{\frac{x^3}{3} + o(x^3)}{x^k} = \lim_{x\to 0}\frac{\frac{1}{3} + \frac{o(x^3)}{x^3}}{x^{k - 3}} = \lim_{x\to 0}\frac{\frac{1}{3}}{x^{k - 3}} = \infty .</equation>当 k < 3时，<equation>\lim_{x\to 0}\frac{\frac{x^{3}}{3}+o\left(x^{3}\right)}{x^{k}}=\lim_{x\to 0}\left[\frac{x^{3-k}}{3}+\frac{o\left(x^{3}\right)}{x^{3}}\cdot x^{3-k}\right]=\lim_{x\to 0}\frac{x^{3-k}}{3}=0.</equation>因此，k=3，此时<equation>c=\frac{1}{3}</equation>应选D.

（法二）由于<equation>c\neq 0</equation>且<equation>\lim_{x\to 0} \left(x-\arctan x\right)=0</equation>，故<equation>\lim_{x\to 0} x^{k}=0</equation>，从而 k>0，于是题设中极限为<equation>\frac{0}{0}</equation>型.根据洛必达法则，<equation>\lim _ {x \rightarrow 0} \frac {x - \arctan x}{x ^ {k}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - \frac {1}{1 + x ^ {2}}}{k x ^ {k - 1}} = \lim _ {x \rightarrow 0} \left(\frac {1}{1 + x ^ {2}} \cdot \frac {x ^ {2}}{k x ^ {k - 1}}\right) = \lim _ {x \rightarrow 0} \frac {1}{k x ^ {k - 3}} = c.</equation>又<equation>c\neq 0</equation>，故<equation>k=3</equation>，从而<equation>c=\frac{1}{3}</equation>应选D.

---

**2009年第1题 | 选择题 | 4分 | 答案: A**
1. 当<equation>x\to0</equation>时，<equation>f(x)=x-\sin ax</equation>与<equation>g(x)=x^{2}\ln(1-bx)</equation>是等价无穷小量，则（    )

A. a=1,b=-<equation>\frac{1}{6}</equation>B. a=1,b=<equation>\frac{1}{6}</equation>C. a=-1,b=-<equation>\frac{1}{6}</equation>D. a=-1,b=<equation>\frac{1}{6}</equation>
答案: A
**解析: **由于<equation>x\to0</equation>时，<equation>f(x)</equation>与<equation>g(x)</equation>是等价无穷小量，故<equation>\begin{aligned} 1 &= \lim _ {x \rightarrow 0} \frac {f (x)}{g (x)} = \lim _ {x \rightarrow 0} \frac {x - \sin a x}{x ^ {2} \ln (1 - b x)} \xlongequal {\ln (1 - b x) \sim (- b x)} \lim _ {x \rightarrow 0} \frac {x - \sin a x}{- b x ^ {3}} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - a \cos a x}{- 3 b x ^ {2}} &= I _ {1}. \end{aligned}</equation>由于<equation>\lim_{x\to 0}(-3bx^2) = 0</equation>，故若<equation>I_{1}</equation>存在，则<equation>\lim_{x\to 0}(1 - a\cos ax) = 0</equation>，从而<equation>a = 1.</equation>代人 a=1，得<equation>I _ {1} = \lim _ {x \rightarrow 0} \frac {1 - \cos x}{- 3 b x ^ {2}} \xlongequal {1 - \cos x \sim \frac {x ^ {2}}{2}} \lim _ {x \rightarrow 0} \frac {\frac {x ^ {2}}{2}}{- 3 b x ^ {2}} = - \frac {1}{6 b}.</equation>当<equation>b = -\frac{1}{6}</equation>时，<equation>I_{1}</equation>存在且等于1.

因此，当<equation>a = 1,b = -\frac{1}{6}</equation>时，<equation>\lim_{x\to 0}\frac{f(x)}{g(x)} = 1,f(x)</equation>与<equation>g(x)</equation>是<equation>x\to 0</equation>时的等价无穷小量.应选A.

---


#### 数列敛散性的判定

**2022年第3题 | 选择题 | 5分 | 答案: D**

3. 已知数列<equation>\{x_{n}\}</equation>满足<equation>-\frac{\pi}{2}\leqslant x_{n}\leqslant \frac{\pi}{2}</equation>，则（    )

A. 若<equation>\lim_{n\to\infty}\cos(\sin x_{n})</equation>存在，则<equation>\lim_{n\to\infty}x_{n}</equation>存在

B. 若<equation>\lim_{n\to\infty}\sin(\cos x_{n})</equation>存在，则<equation>\lim_{n\to\infty}x_{n}</equation>存在

C. 若<equation>\lim_{n\to\infty}\cos(\sin x_{n})</equation>存在，则<equation>\lim_{n\to\infty}\sin x_{n}</equation>存在，但<equation>\lim_{n\to\infty}x_{n}</equation>不一定存在

D. 若<equation>\lim_{n\to\infty}\sin(\cos x_{n})</equation>存在，则<equation>\lim_{n\to\infty}\cos x_{n}</equation>存在，但<equation>\lim_{n\to\infty}x_{n}</equation>不一定存在

答案: D

**解析:**解 若<equation>\lim_{n\rightarrow \infty}\sin(\cos x_{n})</equation>存在，则将其记为 a.由于<equation>\sin x</equation>在<equation>\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>上存在反函数<equation>\arcsin x</equation>，故<equation>\lim_{n\rightarrow \infty}\cos x_{n}=\lim_{n\rightarrow \infty}\arcsin(\sin(\cos x_{n}))=\arcsin(\lim_{n\rightarrow \infty}\sin(\cos x_{n}))=\arcsin a.</equation>但是<equation>\lim_{n\rightarrow \infty}\cos x_{n}</equation>存在并不能保证<equation>\lim_{n\rightarrow \infty}x_{n}</equation>存在.例如取<equation>x_{n}=(-1)^{n}\frac{\pi}{2}</equation>，则<equation>\lim_{n\rightarrow \infty}\cos x_{n}=0</equation>，但<equation>\lim_{n\rightarrow \infty}x_{n}</equation>不存在.选项B错误，选项D正确.应选D.

由于<equation>\cos x</equation>在<equation>\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]</equation>上并不单调，故由<equation>\lim_{n\to \infty}\cos (\sin x_n)</equation>存在并不能保证<equation>\lim_{n\to \infty}\sin x_n</equation>存在。同样取<equation>x_{n} = (-1)^{n}\frac{\pi}{2}</equation>，则<equation>\lim_{n\to \infty}\cos (\sin x_n) = \cos 1</equation>，但<equation>\lim_{n\to \infty}\sin x_n</equation>和<equation>\lim_{n\to \infty}x_n</equation>均不存在。选项A、C不正确。

---

**2019年第18题 | 解答题 | 10分**

18. (本题满分10分)

设<equation>a_{n}=\int_{0}^{1} x^{n}\sqrt{1-x^{2}}\mathrm{d}x(n=0,1,2,\dots).</equation>I. 证明数列<equation>\{a_{n}\}</equation>单调递减，且<equation>a_{n}=\frac{n-1}{n+2} a_{n-2}(n=2,3,\cdots)</equation>；

II. 求<equation>\lim_{n\to\infty}\frac{a_{n}}{a_{n-1}}.</equation>

**答案:**（I）证明略；（Ⅱ）<equation>\lim_{n\to \infty}\frac{a_{n}}{a}=1.</equation>

**解析:**解（I）考虑<equation>a_{n+1}-a_{n}</equation>由于在（0，1）内，<equation>x^{n+1}-x^{n}<0,\sqrt{1-x^{2}}>0</equation>故由定积分的保号性可知，<equation>a _ {n + 1} - a _ {n} = \int_ {0} ^ {1} \left(x ^ {n + 1} - x ^ {n}\right) \sqrt {1 - x ^ {2}} \mathrm {d} x < 0.</equation>因此，<equation>\{a_{n}\}</equation>单调递减.

下面用两种方法证明<equation>a_{n} = \frac{n - 1}{n + 2} a_{n - 2}(n = 2,3,\dots)</equation>.

（法一）先三角换元，再分部分分.

令<equation>x=\sin t</equation>，则<equation>\mathrm{d}x=\cos t\mathrm{d}t.</equation><equation>\begin{aligned} a _ {n} &= \int_ {0} ^ {1} x ^ {n} \sqrt {1 - x ^ {2}} \mathrm {d} x \xlongequal {x = \sin t} \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \cos t \cdot \cos t \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \cos^ {2} t \mathrm {d} t \\ &= \int_ {0} ^ {\frac {\pi}{2}} \left(\sin^ {n} t - \sin^ {n + 2} t\right) \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t + \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n + 1} t \mathrm {d} (\cos t) \\ &= \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t + \sin^ {n + 1} t \cos t \left| _ {0} ^ {\frac {\pi}{2}} - \int_ {0} ^ {\frac {\pi}{2}} \cos t \cdot (n + 1) \sin^ {n} t \cdot \cos t \mathrm {d} t \right. \\ &= \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t - (n + 1) \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \cos^ {2} t \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t - (n + 1) a _ {n}. \end{aligned}</equation>由上可得，<equation>(n + 2)a_{n} = \int_{0}^{\frac{\pi}{2}}\sin^{n}t\mathrm{d}t.</equation>另一方面，<equation>\begin{aligned} \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t &= - \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n - 1} t \mathrm {d} (\cos t) = - \left[ \sin^ {n - 1} t \cos t \left| _ {0} ^ {\frac {\pi}{2}} - \int_ {0} ^ {\frac {\pi}{2}} \cos t \cdot (n - 1) \sin^ {n - 2} t \cdot \cos t \mathrm {d} t \right] \right. \\ &= (n - 1) \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n - 2} t \cos^ {2} t \mathrm {d} t = (n - 1) a _ {n - 2}. \end{aligned}</equation>因此，<equation>(n + 2)a_{n} = (n - 1)a_{n - 2}</equation>，即<equation>a_{n} = \frac{n - 1}{n + 2} a_{n - 2}(n = 2,3,\dots)</equation>.

（法二）直接分部积分.注意到<equation>[ ( 1 - x^{2} )^{\frac{3}{2}} ]^{\prime} = - 3 x \sqrt{1 - x^{2}}</equation>，故<equation>\begin{array}{l} a _ {n} = \int_ {0} ^ {1} x ^ {n} \sqrt {1 - x ^ {2}} \mathrm {d} x = - \frac {1}{3} \int_ {0} ^ {1} x ^ {n - 1} \mathrm {d} \left(1 - x ^ {2}\right) ^ {\frac {3}{2}} \\ = - \frac {1}{3} \left\{\left[ x ^ {n - 1} \left(1 - x ^ {2}\right) ^ {\frac {3}{2}} \right] \Bigg | _ {0} ^ {1} - \int_ {0} ^ {1} \left(1 - x ^ {2}\right) ^ {\frac {3}{2}} \cdot (n - 1) x ^ {n - 2} \mathrm {d} x \right\} \\ = \frac {n - 1}{3} \int_ {0} ^ {1} \left(1 - x ^ {2}\right) \sqrt {1 - x ^ {2}} x ^ {n - 2} \mathrm {d} x = \frac {n - 1}{3} \int_ {0} ^ {1} \left(x ^ {n - 2} - x ^ {n}\right) \sqrt {1 - x ^ {2}} \mathrm {d} x \\ = \frac {n - 1}{3} \left(\int_ {0} ^ {1} x ^ {n - 2} \sqrt {1 - x ^ {2}} \mathrm {d} x - \int_ {0} ^ {1} x ^ {n} \sqrt {1 - x ^ {2}} \mathrm {d} x\right) \\ = \frac {n - 1}{3} \left(a _ {n - 2} - a _ {n}\right). \\ \end{array}</equation>因此，<equation>a_{n} = \frac{n - 1}{n + 2} a_{n - 2}(n = 2,3,\dots)</equation>（Ⅱ）由第（I）问可知<equation>\{a_{n}\}</equation>单调递减，故<equation>a_{n} < a_{n-1} < a_{n-2}</equation>又由<equation>a_{n}</equation>的表达式可知<equation>a_{n} > 0 (n= 0,1,\dots)</equation>，故<equation>\frac {n - 1}{n + 2} = \frac {a _ {n}}{a _ {n - 2}} < \frac {a _ {n}}{a _ {n - 1}} < \frac {a _ {n}}{a _ {n}} = 1.</equation>对（1）式中各项同时取极限，令<equation>n\to \infty</equation>，可得<equation>1 = \lim _ {n \rightarrow \infty} \frac {n - 1}{n + 2} \leqslant \lim _ {n \rightarrow \infty} \frac {a _ {n}}{a _ {n - 1}} \leqslant 1.</equation>由夹逼准则可知，<equation>\lim_{n\to \infty}\frac{a_n}{a_{n-1}} = 1.</equation>

---

**2018年第19题 | 解答题 | 10分**

19. (本题满分10分）

设数列<equation>\{x_{n}\}</equation>满足：<equation>x_{1}>0,x_{n}\mathrm{e}^{x_{n+1}}=\mathrm{e}^{x_{n}}-1(n=1,2,\cdots).</equation>证明数列<equation>\{x_{n}\}</equation>收敛，并求<equation>\lim_{n\rightarrow \infty}x_{n}.</equation>

**答案:**证明略，<equation>\lim x_{n}=0.</equation>n->infty

**解析:**解 由<equation>x_{n}\mathrm{e}^{x_{n + 1}} = \mathrm{e}^{x_{n}} - 1(n = 1,2,\dots)</equation>可得，<equation>x _ {n + 1} = \ln \left(\frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n}}\right).</equation>先用数学归纳法证明对所有的正整数<equation>n</equation>，都有<equation>x_{n} > 0</equation>首先，<equation>x_{1} > 0.</equation>假设当<equation>n = k</equation>时，<equation>x_{k} > 0.</equation>注意到当<equation>x > 0</equation>时，<equation>\mathrm{e}^{x} - 1 > x</equation>，从而<equation>\frac{\mathrm{e}^{x} - 1}{x} > 1.</equation>于是，<equation>x _ {k + 1} = \ln \left(\frac {\mathrm {e} ^ {x _ {k}} - 1}{x _ {k}}\right) > \ln 1 = 0.</equation>由数学归纳法可知，对所有的正整数<equation>n</equation>，都有<equation>x_{n} > 0</equation>因此，数列<equation>\{x_{n}\}</equation>有下界.

下面用两种方法证明数列<equation>\{x_{n}\}</equation>单调减少，即<equation>x_{n + 1} < x_n(n = 1,2,\dots)</equation>.

（法一）由<equation>x_{n}\mathrm{e}^{x_{n + 1}} = \mathrm{e}^{x_{n}} - 1</equation>可知，<equation>\mathrm {e} ^ {x _ {n + 1}} = \frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n}} = \frac {\mathrm {e} ^ {x _ {n}} - \mathrm {e} ^ {0}}{x _ {n} - 0} \frac {\text {拉 格 朗 日}}{\text {中 值 定 理}} \mathrm {e} ^ {\xi_ {n}},</equation>其中<equation>\xi_{n}\in (0,x_{n})</equation>由于<equation>\mathrm{e}^x</equation>单调增加，故由<equation>\mathrm{e}^{x_{n+1}} = \mathrm{e}^{\xi_n} < \mathrm{e}^{x_n}</equation>可得<equation>x_{n+1} < x_n</equation>，即数列<equation>\{x_n\}</equation>单调减少.

（法二）<equation>x _ {n + 1} - x _ {n} = \ln \left(\frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n}}\right) - x _ {n} = \ln \left(\frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n} \mathrm {e} ^ {x _ {n}}}\right).</equation>记<equation>f(x) = \mathrm{e}^{x} - 1 - x\mathrm{e}^{x}</equation>，则<equation>f^{\prime}(x) = \mathrm{e}^{x} - \mathrm{e}^{x} - x\mathrm{e}^{x} = -x\mathrm{e}^{x}</equation>.

当<equation>x > 0</equation>时，<equation>f^{\prime}(x) < 0,f(x)</equation>在<equation>[0, + \infty)</equation>上单调减少，于是，<equation>f(x) < f(0) = 0.</equation>从而，当<equation>x > 0</equation>时，<equation>\frac {\mathrm {e} ^ {x} - 1}{x \mathrm {e} ^ {x}} - 1 = \frac {\mathrm {e} ^ {x} - 1 - x \mathrm {e} ^ {x}}{x \mathrm {e} ^ {x}} < 0,</equation>即<equation>\frac{\mathrm{e}^x - 1}{x\mathrm{e}^x} < 1.</equation>又因为对所有的正整数<equation>n</equation>，都有<equation>x_{n} > 0</equation>，所以<equation>\ln \left(\frac{\mathrm{e}^{x_n} - 1}{x_n\mathrm{e}^{x_n}}\right) < \ln 1 = 0</equation>，即<equation>x_{n + 1} - x_n < 0.</equation>因此，数列<equation>\{x_{n}\}</equation>单调减少.

由单调有界准则可知，数列<equation>\{x_{n}\}</equation>收敛.由于对所有的正整数<equation>n</equation>，都有<equation>x_{n} > 0</equation>，故<equation>\lim_{n\to \infty}x_n = a\geqslant 0.</equation>对<equation>x_{n}\mathrm{e}^{x_{n + 1}} = \mathrm{e}^{x_{n}} - 1</equation>两端同时令<equation>n\to \infty</equation>，可得<equation>a\mathrm{e}^{a} = \mathrm{e}^{a} - 1.</equation>由前面的结果可知，<equation>x=0</equation>是<equation>f(x)=\mathrm{e}^{x}-1-x\mathrm{e}^{x}</equation>在<equation>[0,+\infty)</equation>上的唯一零点.因此，<equation>a=0</equation>即<equation>\lim_{n\to \infty}x_{n}=0.</equation>

---

**2011年第18题 | 解答题 | 10分**

18. (本题满分10分)

I. 证明：对任意的正整数 n, 都有<equation>\frac{1}{n+1}<\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}</equation>成立；

II. 设<equation>a_{n}=1+\frac{1}{2}+\cdots+\frac{1}{n}-\ln n</equation>（<equation>n=1,2,\cdots</equation>），证明数列<equation>\left\{a_{n}\right\}</equation>收敛.

**解析:**证（I）（法一）考虑函数<equation>f ( x )=\ln x</equation>，则<equation>f^{\prime}(x)=\frac{1}{x}</equation>由拉格朗日中值定理，对任意的正整数n，都存在<equation>\xi_{n}\in(n,n+1)</equation>，使得<equation>\ln \left(1 + \frac {1}{n}\right) = f (n + 1) - f (n) = f ^ {\prime} \left(\xi_ {n}\right) = \frac {1}{\xi_ {n}}.</equation>又因为<equation>\xi_{n}\in (n,n + 1)</equation>，所以<equation>\frac{1}{n + 1} < \frac{1}{\xi_n} < \frac{1}{n}</equation>因此，对任意的正整数 n，都有<equation>\frac{1}{n+1}<\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}</equation>成立.

（法二）分别证明<equation>\frac{1}{n+1}<\ln \left(1+\frac{1}{n}\right)</equation>和<equation>\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}.</equation>为证明<equation>\ln \left(1 + \frac{1}{n}\right) < \frac{1}{n}</equation>，可考虑函数<equation>f(x) = \ln (1 + x) - x.</equation><equation>f^{\prime}(x)=\frac{1}{1+x}-1</equation>当 x > 0时，<equation>f^{\prime}(x)<0</equation>，故 f(x)在<equation>[0,+\infty)</equation>上单调减少.又由于 f(0) = 0，故对任意的正整数 n，<equation>f\left(\frac{1}{n}\right)<f(0)=0</equation>即<equation>\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}.</equation>为证明<equation>\frac{1}{n+1} < \ln \left( 1+\frac{1}{n} \right)</equation>，可考虑函数<equation>g(x)=\ln(1+x)-\frac{x}{1+x}.</equation><equation>g ^ {\prime} (x) = \frac {1}{1 + x} - \frac {(1 + x) - x}{(1 + x) ^ {2}} = \frac {x}{(1 + x) ^ {2}}.</equation>当 x > 0时，<equation>g^{\prime}(x) > 0</equation>，故 g(x)在<equation>[0,+\infty)</equation>上单调增加.又由于<equation>g(0)=0</equation>，故对任意的正整数n，<equation>g\left(\frac{1}{n}\right) > g(0) = 0</equation>，即<equation>\frac{1}{n+1} < \ln \left(1+\frac{1}{n}\right).</equation>综上所述，对任意的正整数 n，都有<equation>\frac{1}{n+1}<\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}</equation>成立.

（法三）注意到<equation>\ln \left( 1+\frac{1}{n} \right)=\int_{n}^{n+1} \frac{1}{x} \mathrm{d} x.</equation>由于<equation>\int_ {n} ^ {n + 1} \frac {1}{n + 1} \mathrm {d} x < \int_ {n} ^ {n + 1} \frac {1}{x} \mathrm {d} x < \int_ {n} ^ {n + 1} \frac {1}{n} \mathrm {d} x,</equation>故<equation>\frac {1}{n + 1} < \ln \left(1 + \frac {1}{n}\right) < \frac {1}{n}.</equation>（Ⅱ）若能证明数列<equation>\{a_{n}\}</equation>单调且有界，则由单调有界准则知其收敛.

先证<equation>\left\{a_{n}\right\}</equation>单调.

对任意的正整数<equation>n = 1,2,3,\dots</equation><equation>a _ {n + 1} - a _ {n} = \frac {1}{n + 1} + \ln \frac {n}{n + 1} = \frac {1}{n + 1} - \ln \left(1 + \frac {1}{n}\right).</equation>由第（I）问知，<equation>a_{n+1}-a_{n}<0</equation>，故<equation>\left\{a_{n}\right\}</equation>单调减少.

下面证明<equation>\left\{a_{n}\right\}</equation>有下界.

由第（Ⅰ）问知，<equation>\ln 2 - \ln 1 < 1,</equation><equation>\ln 3 - \ln 2 < \frac {1}{2},</equation><equation>\ln (n + 1) - \ln n < \frac {1}{n}.</equation>将上述不等式左端和右端分别相加，得<equation>\ln (n + 1) - \ln 1 < 1 + \frac {1}{2} + \dots + \frac {1}{n}.</equation>同时减去<equation>\ln n</equation>，得<equation>a _ {n} > \ln (n + 1) - \ln n > 0.</equation>因此，<equation>\{a_{n}\}</equation>有下界.

综上所述，数列<equation>\left\{a_{n}\right\}</equation>收敛.

---


#### 无穷小量的比较

**2020年第1题 | 选择题 | 4分 | 答案: D**

1. 当<equation>x \to 0^{+}</equation>时，下列无穷小量中最高阶的是（    )

A.<equation>\int_{0}^{x} \left( \mathrm{e}^{t^{2}}-1 \right) \mathrm{d} t</equation>B.<equation>\int_{0}^{x} \ln(1+\sqrt{t^{3}}) \mathrm{d} t</equation>C.<equation>\int_{0}^{\sin x} \sin t^{2} \mathrm{d} t</equation>D.<equation>\int_{0}^{1-\cos x} \sqrt{\sin^{3} t} \mathrm{d} t</equation>

答案: D

**解析:**解 由于求一次导，无穷小量的阶数降低1，且选项A、B的积分上、下限相同，故比较这两项的无穷小量的阶的大小，可以转化为比较它们的被积函数的阶。又因为<equation>t\to 0^{+}</equation>时，<equation>\mathrm{e}^{t^{2}}-1\sim t^{2},</equation><equation>\ln(1+\sqrt{t^{3}})\sim t^{\frac{3}{2}}</equation>，所以<equation>\int_{0}^{x}\left(\mathrm{e}^{t^{2}}-1\right)\mathrm{d}t</equation>与<equation>x^{3}</equation>同阶，比<equation>\int_{0}^{x}\ln(1+\sqrt{t^{3}})\mathrm{d}t</equation>高阶.

比较<equation>\int_{0}^{\sin x}\sin t^{2}\mathrm{d}t</equation>与<equation>x^{3}</equation>的阶.<equation>\begin{aligned} \lim _ {x \rightarrow 0 ^ {+}} \frac {\int_ {0} ^ {\sin x} \sin t ^ {2} \mathrm {d} t}{x ^ {3}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sin (\sin x) ^ {2} \cdot \cos x}{3 x ^ {2}} &= \frac {1}{3} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sin (\sin x) ^ {2}}{x ^ {2}} \xlongequal {\text {s i n} u \sim u} \frac {1}{3} \lim _ {x \rightarrow 0 ^ {+}} \frac {(\sin x) ^ {2}}{x ^ {2}} \\ &= \frac {1}{3} \lim _ {x \rightarrow 0 ^ {+}} \left(\frac {\sin x}{x}\right) ^ {2} \xlongequal {\sin x \sim x} \frac {1}{3}. \end{aligned}</equation>于是，<equation>\int_{0}^{\sin x}\sin t^{2}\mathrm{d}t</equation>也与<equation>x^{3}</equation>同阶.

比较<equation>\int_{0}^{1-\cos x}\sqrt{\sin^{3}t}\mathrm{d}t</equation>与<equation>x^{3}</equation>的阶.<equation>\begin{aligned} \lim _ {x \rightarrow 0 ^ {+}} \frac {\int_ {0} ^ {1 - \cos x} \sqrt {\sin^ {3} t} \mathrm {d} t}{x ^ {3}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sqrt {\sin^ {3} (1 - \cos x)} \sin x}{3 x ^ {2}} \xlongequal {\text {s i n} x \sim x} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sin^ {\frac {3}{2}} (1 - \cos x)}{3 x} \\ &= \lim _ {x \rightarrow 0 ^ {+}} \frac {\sin^ {\frac {3}{2}} (1 - \cos x)}{(1 - \cos x) ^ {\frac {3}{2}}} \cdot \frac {(1 - \cos x) ^ {\frac {3}{2}}}{3 x} \\ \frac {1 - \cos x \sim \frac {x ^ {2}}{2}}{} \lim _ {x \rightarrow 0 ^ {+}} \left[ \frac {\sin (1 - \cos x)}{1 - \cos x} \right] ^ {\frac {3}{2}} \cdot \frac {\left(\frac {x ^ {2}}{2}\right) ^ {\frac {3}{2}}}{3 x} \\ &= 1 \times 0 = 0. \end{aligned}</equation>因此，<equation>\int_0^{1 - \cos x}\sqrt{\sin^3t}\mathrm{d}t</equation>比<equation>x^{3}</equation>高阶，从而比选项A、B、C中的无穷小量均高阶.应选D.

---


#### 函数的连续性

**2017年第1题 | 选择题 | 4分 | 答案: A**

1. 若函数 f(x)<equation>\left\{\begin{array}{l l}{\frac{1-\cos \sqrt{x}}{ax},}&{x>0,}\\ {b,}&{x\leqslant 0}\end{array}\right.</equation>在 x=0处连续，则（    )

A.<equation>a b=\frac{1}{2}</equation>B.<equation>a b=-\frac{1}{2}</equation>C.<equation>a b=0</equation>D.<equation>a b=2</equation>

答案: A

**解析:**解<equation>f(x)</equation>是分段函数. 代入<equation>f(x)</equation>在<equation>(-\infty ,0]</equation>和<equation>(0, + \infty)</equation>上的表达式, 分别计算<equation>\lim_{x\to 0^{-}}f(x)</equation>,<equation>\lim_{x\to 0^{+}}f(x)</equation>.<equation>\lim _ {x \rightarrow 0 ^ {-}} f (x) = f (0) = b,</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} f (x) = \lim _ {x \rightarrow 0 ^ {+}} \frac {1 - \cos \sqrt {x}}{a x} \frac {1 - \cos \sqrt {x} \sim \frac {1}{2} (\sqrt {x}) ^ {2}}{\underline {{=}}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {x}{2}}{a x} = \frac {1}{2 a}.</equation>因此，<equation>b=\frac{1}{2a}</equation>即<equation>ab=\frac{1}{2}</equation>应选A.

---


### 多元函数微分学


#### 方向导数和梯度

**2025年第13题 | 填空题 | 5分**
13. 已知函数<equation>u ( x,y,z)= x y^{2} z^{3}</equation>，向量<equation>\boldsymbol{n}=(2,2,-1)</equation>，则<equation>\left. \frac{\partial u}{\partial \boldsymbol{n}} \right|_{(1,1,1)}=</equation>___
**答案: **1.
**解析: **的方向余弦为<equation>\cos \alpha = \cos \beta = \frac {2}{\sqrt {2 ^ {2} + 2 ^ {2} + (- 1) ^ {2}}} = \frac {2}{3}, \cos \gamma = \frac {- 1}{\sqrt {2 ^ {2} + 2 ^ {2} + (- 1) ^ {2}}} = - \frac {1}{3}.</equation>计算<equation>\frac{\partial u}{\partial x},\frac{\partial u}{\partial y},\frac{\partial u}{\partial z}</equation>得，<equation>\frac {\partial u}{\partial x} = y ^ {2} z ^ {3}, \quad \frac {\partial u}{\partial y} = 2 x y z ^ {3}, \quad \frac {\partial u}{\partial z} = 3 x y ^ {2} z ^ {2}.</equation>因此，在点（1,1,1）处沿方向<equation>n = (2,2, - 1)</equation>的方向导数为<equation>\left. \frac {\partial u}{\partial n} \right| _ {(1, 1, 1)} = 1 \times \frac {2}{3} + 2 \times \frac {2}{3} + 3 \times \left(- \frac {1}{3}\right) = 1.</equation>

---

**2022年第11题 | 填空题 | 5分**
11. 函数<equation>f(x,y)=x^{2}+2y^{2}</equation>在点 (0,1) 处的最大方向导数为 ___
**解析: **解 由于<equation>\mathbf{g r a d} f(x,y)=(2x,4y),</equation>故 f(x,y)在点（0,1）处的梯度为（0,4）.又因为函数在一点处的最大方向导数等于该点处的梯度的模，所以 f(x,y)在点（0,1）处的最大方向导数为4.

---

**2019年第16题 | 解答题 | 10分**
16. (本题满分10分)

设 a,b为实数，函数<equation>z=2+a x^{2}+b y^{2}</equation>在点（3,4）处的方向导数中，沿方向 l=-3i-4j的方向导数最大，最大值为10.

I. 求 a,b;

II. 求曲面<equation>z = 2 + ax^{2} + by^{2}(z\geqslant 0)</equation>的面积.
**答案: **（ I ）<equation>a=-1,b=-1;</equation>（ II ）<equation>\frac{1 3 \pi}{3}.</equation>
**解析: **解（I）计算函数<equation>z=2+ax^{2}+by^{2}</equation>在点（3，4）处的梯度.<equation>\operatorname {g r a d} z (x, y) \mid_ {(3, 4)} = \left(z _ {x} ^ {\prime}, z _ {y} ^ {\prime}\right) \mid_ {(3, 4)} = \left(2 a x, 2 b y\right) \mid_ {(3, 4)} = (6 a, 8 b).</equation>由于函数沿方向<equation>l=-3 i-4 j</equation>的方向导数最大，最大值为10，故<equation>6 a i+8 b j</equation>与<equation>-3 i-4 j</equation>同向，且<equation>\sqrt{(6 a)^{2}+(8 b)^{2}}=10.</equation>由<equation>6 a i+8 b j</equation>与<equation>- 3 i-4 j</equation>同向可得<equation>\frac{6 a}{-3}=\frac{8 b}{-4}>0</equation>，从而<equation>a=b<0</equation>.代入<equation>\sqrt{(6 a)^{2}+(8 b)^{2}}=1 0</equation>可得<equation>a=b=-1.</equation>（Ⅱ）由第（I）问可知曲面<equation>\varSigma</equation>为<equation>z=2-x^{2}-y^{2}(z\geqslant0)</equation>，由第一类曲面积分的几何意义可知其面积等于<equation>\iint\limits_{\Sigma}\mathrm{d}S.</equation><equation>z _ {x} ^ {\prime} = - 2 x, z _ {y} ^ {\prime} = - 2 y, \mathrm {d} S = \sqrt {1 + 4 x ^ {2} + 4 y ^ {2}} \mathrm {d} x \mathrm {d} y.</equation>令<equation>z = 0</equation>，可得<equation>\Sigma</equation>在<equation>xOy</equation>面的投影区域为<equation>D_{xy} = \{(x,y)|x^2 + y^2\leqslant 2\}</equation><equation>\begin{aligned} \iint_ {\Sigma} \mathrm {d} S &= \iint_ {D _ {x y}} \sqrt {1 + \left(z _ {x} ^ {\prime}\right) ^ {2} + \left(z _ {y} ^ {\prime}\right) ^ {2}} \mathrm {d} x \mathrm {d} y = \iint_ {D _ {x y}} \sqrt {1 + 4 x ^ {2} + 4 y ^ {2}} \mathrm {d} x \mathrm {d} y \\ \xlongequal {\text {极 坐 标}} \int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {0} ^ {\sqrt {2}} \sqrt {1 + 4 r ^ {2}} \cdot r \mathrm {d} r &= 2 \pi \cdot \frac {1}{8} \int_ {0} ^ {\sqrt {2}} \sqrt {1 + 4 r ^ {2}} \mathrm {d} \left(1 + 4 r ^ {2}\right) \\ &= \frac {\pi}{4} \cdot \frac {2}{3} \left(1 + 4 r ^ {2}\right) ^ {\frac {3}{2}} \Bigg | _ {0} ^ {\sqrt {2}} = \frac {\pi}{4} \times \frac {2}{3} \times (2 7 - 1) = \frac {1 3 \pi}{3}. \end{aligned}</equation>

---

**2017年第3题 | 选择题 | 4分 | 答案: D**
3. 函数<equation>f(x,y,z)=x^{2} y+z^{2}</equation>在点（1，2，0）处沿向量 n =（1，2，2）的方向导数为（    )

A. 12 B. 6 C. 4 D. 2
答案: D
**解析: **由方向导数的计算公式知，<equation>\begin{aligned} \left. \frac {\partial f}{\partial n} \right| _ {(1, 2, 0)} &= \operatorname {g r a d} f (1, 2, 0) \cdot e _ {n} = \left(\frac {\partial f}{\partial x}, \frac {\partial f}{\partial y}, \frac {\partial f}{\partial z}\right) \Big | _ {(1, 2, 0)} \cdot \frac {n}{\| n \|} \\ &= \left(2 x y, x ^ {2}, 2 z\right) \mid_ {(1, 2, 0)} \cdot \frac {1}{3} n = (4, 1, 0) \cdot \left(\frac {1}{3}, \frac {2}{3}, \frac {2}{3}\right) \\ &= \frac {4}{3} + \frac {2}{3} = 2. \end{aligned}</equation>因此，应选D.

---

**2012年第11题 | 填空题 | 4分**
11. grad<equation>\left(x y+\frac{z}{y}\right)\bigg|_{(2,1,1)}=</equation>___
**答案: **## i+j+k.
**解析: **解 令<equation>f ( x,y,z)= x y+\frac{z}{y}</equation>，则<equation>\left(f_{x}^{\prime},f_{y}^{\prime},f_{z}^{\prime}\right)\big|_{(2,1,1)}=\left(y,x-\frac{z}{y^{2}},\frac{1}{y}\right)\big|_{(2,1,1)}=(1,1,1)</equation>，从而<equation>\operatorname{grad}\left(x y+\frac{z}{y}\right)\big|_{(2,1,1)}=i+j+k.</equation>

---


#### 偏导数的概念与计算

**2024年第12题 | 填空题 | 5分**
12. 设函数 f(u,v)具有2阶连续偏导数，且<equation>\mathrm{d} f|_{(1,1)}=3 \mathrm{d} u+4 \mathrm{d} v</equation>. 令 y=f（<equation>\cos x,1+x^{2}</equation>），则<equation>\left.\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\right|_{x=0}=</equation>___.
**答案: **```latex
5
```

**解析:**解 由全微分的定义以及<equation>\mathrm{d}f|_{(1,1)}=3\mathrm{d}u+4\mathrm{d}v</equation>可知，<equation>f_{1}^{\prime}(1,1)=3,f_{2}^{\prime}(1,1)=4.</equation>根据链式法则，<equation>\begin{aligned} \frac {\mathrm {d} y}{\mathrm {d} x} &= f _ {1} ^ {\prime} (\cos x, 1 + x ^ {2}) \cdot (- \sin x) + f _ {2} ^ {\prime} (\cos x, 1 + x ^ {2}) \cdot 2 x, \\ \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} &= f _ {1 1} ^ {\prime \prime} (\cos x, 1 + x ^ {2}) \cdot (- \sin x) ^ {2} + f _ {1 2} ^ {\prime \prime} (\cos x, 1 + x ^ {2}) \cdot 2 x \cdot (- \sin x) \\ + f _ {1} ^ {\prime} (\cos x, 1 + x ^ {2}) \cdot (- \cos x) + f _ {2 1} ^ {\prime \prime} (\cos x, 1 + x ^ {2}) \cdot 2 x \cdot (- \sin x) + f _ {2 2} ^ {\prime \prime} (\cos x, 1 + x ^ {2}) \cdot (2 x) ^ {2} \\ + f _ {2} ^ {\prime} (\cos x, 1 + x ^ {2}) \cdot 2. \end{aligned}</equation>将<equation>x=0</equation>代入<equation>\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}</equation>的表达式可得<equation>\left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {x = 0} = - f _ {1} ^ {\prime} (1, 1) + 2 f _ {2} ^ {\prime} (1, 1) = - 3 + 2 \times 4 = 5.</equation>

---

**2022年第2题 | 选择题 | 5分 | 答案: B**

2. 设函数<equation>z=xyf\left(\frac{y}{x}\right)</equation>，其中 f(u)可导，若<equation>x\frac{\partial z}{\partial x}+y\frac{\partial z}{\partial y}=y^{2}(\ln y-\ln x)</equation>，则（    )

A.<equation>f(1)=\frac{1}{2},f^{\prime}(1)=0</equation>B.<equation>f(1)=0,f^{\prime}(1)=\frac{1}{2}</equation>C.<equation>f(1)=\frac{1}{2},f^{\prime}(1)=1</equation>D.<equation>f(1)=0,f^{\prime}(1)=1</equation>

答案: B

**解析:**解分别求<equation>\frac{\partial z}{\partial x}</equation>和<equation>\frac{\partial z}{\partial y}</equation>利用链式法则，<equation>\frac {\partial z}{\partial x} = y f \left(\frac {y}{x}\right) + x y f ^ {\prime} \left(\frac {y}{x}\right) \cdot \left(- \frac {y}{x ^ {2}}\right) = y f \left(\frac {y}{x}\right) - \frac {y ^ {2}}{x} f ^ {\prime} \left(\frac {y}{x}\right),</equation><equation>\frac {\partial z}{\partial y} = x f \left(\frac {y}{x}\right) + x y f ^ {\prime} \left(\frac {y}{x}\right) \cdot \frac {1}{x} = x f \left(\frac {y}{x}\right) + y f ^ {\prime} \left(\frac {y}{x}\right).</equation>于是，<equation>x\frac{\partial z}{\partial x}+y\frac{\partial z}{\partial y}=2xyf\left(\frac{y}{x}\right).</equation>与<equation>x\frac{\partial z}{\partial x}+y\frac{\partial z}{\partial y}=y^{2}(\ln y-\ln x)=y^{2}\ln \frac{y}{x}</equation>比较可得，<equation>f\left(\frac{y}{x}\right)=\frac{y}{2x}\ln \frac{y}{x}.</equation>从而，<equation>f(u)=\frac{1}{2} u \ln u,</equation><equation>f^{\prime}(u)=\frac{1}{2}(\ln u+1).</equation>因此，<equation>f ( 1 ) = 0</equation><equation>f^{\prime}(1)=\frac{1}{2}</equation>应选B.

---

**2020年第12题 | 填空题 | 4分**

12. 设函数<equation>f(x,y)=\int_{0}^{xy}\mathrm{e}^{xt^{2}}\mathrm{d}t</equation>，则<equation>\left.\frac{\partial^{2}f}{\partial x\partial y}\right|_{(1,1)}=</equation>___

**答案:**## 4e.

**解析:**解（法一）注意到 f(x,y)的二阶偏导数连续，故可以交换求导次序.先对 y求偏导，再对 x求偏导.

根据变限积分求导公式，<equation>\frac {\partial f}{\partial y} = \mathrm {e} ^ {x (x y) ^ {2}} \cdot x = x \mathrm {e} ^ {x ^ {3} y ^ {2}},</equation><equation>\frac {\partial^ {2} f}{\partial y \partial x} = \mathrm {e} ^ {x ^ {3} y ^ {2}} + x \cdot \mathrm {e} ^ {x ^ {3} y ^ {2}} \cdot 3 x ^ {2} y ^ {2} = \left(3 x ^ {3} y ^ {2} + 1\right) \mathrm {e} ^ {x ^ {3} y ^ {2}}.</equation>代入<equation>x = 1,y = 1</equation>，可得<equation>\frac{\partial^2f}{\partial x\partial y}\bigg|_{(1,1)} = \frac{\partial^2f}{\partial y\partial x}\bigg|_{(1,1)} = 4\mathrm{e}.</equation>（法二）若直接对<equation>x</equation>求偏导，则需先对变限积分换元，将<equation>x</equation>移出积分号.令<equation>\sqrt{x} t = u</equation>，则<equation>\mathrm{d}t = \frac{\mathrm{d}u}{\sqrt{x}}.</equation><equation>\int_ {0} ^ {x y} \mathrm {e} ^ {x t ^ {2}} \mathrm {d} t \xlongequal {\sqrt {x} t = u} \int_ {0} ^ {x ^ {\frac {3}{2}} y} \frac {\mathrm {e} ^ {u ^ {2}}}{\sqrt {x}} \mathrm {d} u = \frac {1}{\sqrt {x}} \int_ {0} ^ {x ^ {\frac {3}{2}} y} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t.</equation>依次计算<equation>\frac{\partial f}{\partial x}, \frac{\partial^2 f}{\partial x \partial y}</equation>.<equation>\frac {\partial f}{\partial x} = - \frac {1}{2} x ^ {- \frac {3}{2}} \int_ {0} ^ {x ^ {\frac {3}{2}} y} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t + \frac {1}{\sqrt {x}} \cdot \mathrm {e} ^ {x ^ {3} y ^ {2}} \cdot \frac {3}{2} \sqrt {x} y = - \frac {1}{2} x ^ {- \frac {3}{2}} \int_ {0} ^ {x ^ {\frac {3}{2}} y} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t + \frac {3}{2} y \mathrm {e} ^ {x ^ {3} y ^ {2}}.</equation><equation>\frac {\partial^ {2} f}{\partial x \partial y} = - \frac {1}{2} x ^ {- \frac {3}{2}} \mathrm {e} ^ {x ^ {3} y ^ {2}} \cdot x ^ {\frac {3}{2}} + \frac {3}{2} \mathrm {e} ^ {x ^ {3} y ^ {2}} + 3 x ^ {3} y ^ {2} \mathrm {e} ^ {x ^ {3} y ^ {2}} = \left(3 x ^ {3} y ^ {2} + 1\right) \mathrm {e} ^ {x ^ {3} y ^ {2}}.</equation>代入<equation>x = 1,y = 1</equation>，可得<equation>\frac{\partial^2f}{\partial x\partial y}\bigg|_{(1,1)} = 4\mathrm{e}.</equation>

---

**2019年第9题 | 填空题 | 4分**

9. 设函数 f(u)可导，<equation>z=f(\sin y-\sin x)+xy</equation>，则

**答案:**<equation>\frac {y}{\cos x} + \frac {x}{\cos y}.</equation>

**解析:**解分别计算<equation>\frac{\partial z}{\partial x},\frac{\partial z}{\partial y}.</equation><equation>\frac {\partial z}{\partial x} = f ^ {\prime} (\sin y - \sin x) \cdot (- \cos x) + y, \quad \frac {\partial z}{\partial y} = f ^ {\prime} (\sin y - \sin x) \cdot \cos y + x.</equation>代入<equation>\frac{1}{\cos x}\cdot \frac{\partial z}{\partial x} +\frac{1}{\cos y}\cdot \frac{\partial z}{\partial y}</equation>可得，<equation>\begin{aligned} \frac {1}{\cos x} \cdot \frac {\partial z}{\partial x} + \frac {1}{\cos y} \cdot \frac {\partial z}{\partial y} &= - f ^ {\prime} (\sin y - \sin x) + \frac {y}{\cos x} + f ^ {\prime} (\sin y - \sin x) + \frac {x}{\cos y} \\ &= \frac {y}{\cos x} + \frac {x}{\cos y}. \end{aligned}</equation>

---

**2017年第15题 | 解答题 | 10分**

15. (本题满分10分）

设函数<equation>f ( u,v )</equation>具有2阶连续偏导数，<equation>y=f(\mathrm{e}^{x},\cos x)</equation>，求<equation>\left.\frac{\mathrm{d} y}{\mathrm{d} x}\right|_{x=0},\left.\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\right|_{x=0}.</equation>

**答案:**<equation>\frac{\mathrm{d} y}{\mathrm{d} x}\bigg|_{x=0}=f_{1}^{\prime}(1,1),\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\bigg|_{x=0}=f_{1}^{\prime}(1,1)+f_{11}^{\prime\prime}(1,1)-f_{2}^{\prime}(1,1).</equation>

**解析:**解分别记 f（u,v）关于第一个变量、第二个变量的偏导数为<equation>f_{1}^{\prime}, f_{2}^{\prime}. f_{1}^{\prime}, f_{2}^{\prime}</equation>具有与f相同的复合结构根据链式法则，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = f _ {1} ^ {\prime} \frac {\mathrm {d} \left(\mathrm {e} ^ {x}\right)}{\mathrm {d} x} + f _ {2} ^ {\prime} \frac {\mathrm {d} (\cos x)}{\mathrm {d} x} = f _ {1} ^ {\prime} \mathrm {e} ^ {x} - f _ {2} ^ {\prime} \sin x.</equation>代入 x=0，得<equation>\left. \frac {\mathrm {d} y}{\mathrm {d} x} \right| _ {x = 0} = f _ {1} ^ {\prime} (1, 1) - 0 = f _ {1} ^ {\prime} (1, 1).</equation>对（1）式两端关于 x求导，得<equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = f _ {1} ^ {\prime} \mathrm {e} ^ {x} + \mathrm {e} ^ {x} \left(f _ {1 1} ^ {\prime \prime} \mathrm {e} ^ {x} - f _ {1 2} ^ {\prime \prime} \sin x\right) - f _ {2} ^ {\prime} \cos x - \sin x \left(f _ {2 1} ^ {\prime \prime} \mathrm {e} ^ {x} - f _ {2 2} ^ {\prime \prime} \sin x\right).</equation>代入 x=0，得<equation>\left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {x = 0} = f _ {1} ^ {\prime} (1, 1) + f _ {1 1} ^ {\prime \prime} (1, 1) - f _ {2} ^ {\prime} (1, 1).</equation>

---

**2011年第11题 | 填空题 | 4分**

11. 设函数 F(x,y)<equation>= \int_{0}^{x y}\frac{\sin t}{1+t^{2}}\mathrm{d}t</equation>，则<equation>\left.\frac{\partial^{2}F}{\partial x^{2}}\right|_{x=0,y=2}</equation> =___

**解析:**因此，<equation>\frac{\partial^{2}F}{\partial x^{2}}\bigg|_{x=0 \atop y=2}=4.</equation>解（法一）令<equation>f ( u )=\int_{0}^{u} \frac{\sin t}{1+t^{2}} \mathrm{d} t</equation>，则<equation>f^{\prime}(u)=\frac{\sin u}{1+u^{2}}</equation>，且<equation>F(x,y)=f(xy)</equation>.于是<equation>\frac{\partial F(x,y)}{\partial x}=f^{\prime}(xy)\cdot \frac{\partial(xy)}{\partial x}=\frac{\sin(xy)}{1+x^{2}y^{2}}\cdot y,</equation><equation>\frac{\partial^{2}F(x,y)}{\partial x^{2}}=y\cdot \frac{y\cos(xy)\cdot(1+x^{2}y^{2})-\sin(xy)\cdot 2xy^{2}}{(1+x^{2}y^{2})^{2}}.</equation>因此，<equation>\left. \frac{\partial^{2}F}{\partial x^{2}} \right|_{x=0, y=2}=4.</equation>（法二）先代值再求导.

由于<equation>F ( x, 2 ) = \int_{0}^{2 x} \frac{\sin t}{1 + t^{2}} \mathrm{d} t</equation>，故<equation>\left. \frac {\partial F}{\partial x} \right| _ {y = 2} = 2 \cdot \frac {\sin (2 x)}{1 + 4 x ^ {2}}, \quad \left. \frac {\partial^ {2} F}{\partial x ^ {2}} \right| _ {y = 2} = 2 \cdot \frac {2 \cos (2 x) \cdot \left(1 + 4 x ^ {2}\right) - \sin (2 x) \cdot 8 x}{\left(1 + 4 x ^ {2}\right) ^ {2}}.</equation>

---

**2011年第16题 | 解答题 | 10分**

16. (本题满分9分)

设函数 z = f(xy, yg(x))，其中函数 f具有二阶连续偏导数，函数 g(x)可导，且在 x=1处取得极值 g(1)=1.

求<equation>\left.\frac{\partial^{2} z}{\partial x \partial y}\right|_{x=1}</equation>y=1.

**解析:**由链式法则，<equation>\begin{array}{l} \frac {\partial z}{\partial x} = f _ {1} ^ {\prime} \frac {\partial (x y)}{\partial x} + f _ {2} ^ {\prime} \frac {\partial [ y g (x) ]}{\partial x} = y f _ {1} ^ {\prime} + y g ^ {\prime} (x) f _ {2} ^ {\prime}, \\ \frac {\partial^ {2} z}{\partial x \partial y} = \frac {\partial \left[ y \left(f _ {1} ^ {\prime} + g ^ {\prime} (x) f _ {2} ^ {\prime}\right) \right]}{\partial y} \\ = f _ {1} ^ {\prime} + g ^ {\prime} (x) f _ {2} ^ {\prime} + y \left\{f _ {1 1} ^ {\prime \prime} \frac {\partial (x y)}{\partial y} + f _ {1 2} ^ {\prime \prime} \frac {\partial [ y g (x) ]}{\partial y} + g ^ {\prime} (x) f _ {2 1} ^ {\prime \prime} \frac {\partial (x y)}{\partial y} + g ^ {\prime} (x) f _ {2 2} ^ {\prime \prime} \frac {\partial [ y g (x) ]}{\partial y} \right\} \\ = f _ {1} ^ {\prime} + g ^ {\prime} (x) f _ {2} ^ {\prime} + y \left[ x f _ {1 1} ^ {\prime \prime} + g (x) f _ {1 2} ^ {\prime \prime} + x g ^ {\prime} (x) f _ {2 1} ^ {\prime \prime} + g (x) g ^ {\prime} (x) f _ {2 2} ^ {\prime \prime} \right]. \\ \end{array}</equation>由<equation>g ( x )</equation>可导且在<equation>x=1</equation>处取得极值<equation>g ( 1 )=1</equation>知，<equation>g^{\prime}(1)=0.</equation>将<equation>x=1, y=1, g ( 1 )=1,</equation><equation>g^{\prime}(1)=0</equation>代入<equation>\frac{\partial^{2} z}{\partial x \partial y}</equation>，得<equation>\left. \frac {\partial^ {2} z}{\partial x \partial y} \right| _ {x = 1 \atop y = 1} = f _ {1} ^ {\prime} (1, 1) + f _ {1 1} ^ {\prime \prime} (1, 1) + f _ {1 2} ^ {\prime \prime} (1, 1).</equation>

---

**2010年第2题 | 选择题 | 4分 | 答案: B**

2. 设函数 z=z(x,y)由方程<equation>F\left( \frac{y}{x},\frac{z}{x} \right)=0</equation>确定，其中 F为可微函数，且<equation>F_{2}^{\prime}\neq0</equation>，则<equation>x\frac{\partial z}{\partial x}+y\frac{\partial z}{\partial y}=</equation>(    )

A. x B. z C. -x D. -z

答案: B

**解析:**解 对方程<equation>F\left(\frac{y}{x},\frac{z}{x}\right)=0</equation>两端同时关于x，y求偏导数，可得<equation>- \frac {y}{x ^ {2}} F _ {1} ^ {\prime} + \left(- \frac {z}{x ^ {2}} + \frac {1}{x} \cdot \frac {\partial z}{\partial x}\right) F _ {2} ^ {\prime} = 0, \quad \frac {F _ {1} ^ {\prime}}{x} + \frac {F _ {2} ^ {\prime}}{x} \cdot \frac {\partial z}{\partial y} = 0.</equation>由上面两个方程解得，<equation>\frac {\partial z}{\partial x} = \frac {\frac {y}{x} F _ {1} ^ {\prime} + \frac {z}{x} F _ {2} ^ {\prime}}{F _ {2} ^ {\prime}}, \quad \frac {\partial z}{\partial y} = - \frac {F _ {1} ^ {\prime}}{F _ {2} ^ {\prime}}.</equation>因此，<equation>x \frac {\partial z}{\partial x} + y \frac {\partial z}{\partial y} = \frac {y F _ {1} ^ {\prime} + z F _ {2} ^ {\prime} - y F _ {1} ^ {\prime}}{F _ {2} ^ {\prime}} = z.</equation>应选B.

---

**2009年第9题 | 填空题 | 4分**

9. 设函数 f(u,v)具有二阶连续偏导数，z=f(x,xy)，则<equation>\frac{\partial^{2} z}{\partial x \partial y}=</equation>___

**答案:**<equation>x f_{12}^{\prime \prime}+f_{2}^{\prime}+ x y f_{22}^{\prime \prime}.</equation>

**解析:**由二元复合函数求导的链式法则知<equation>\begin{aligned} \frac {\partial z}{\partial x} &= f ^ {\prime} _ {1} (x, x y) + y f ^ {\prime} _ {2} (x, x y), \\ \frac {\partial^ {2} z}{\partial x \partial y} &= x f _ {1 2} ^ {\prime \prime} (x, x y) + f _ {2} ^ {\prime} (x, x y) + x y f _ {2 2} ^ {\prime \prime} (x, x y). \end{aligned}</equation>

---


#### 多元函数的极值问题

**2024年第18题 | 解答题 | 12分**

8. (本题满分12分)

已知函数<equation>f ( x, y )=x^{3}+y^{3}-( x+y )^{2}+3</equation>，设 T是曲面<equation>z=f(x,y)</equation>在点（1，1，1）处的切平面，D为T与坐标平面所围成的有界区域在 xOy面上的投影.

I. 求 T的方程；

II. 求 f(x,y)在 D上的最大值和最小值.

**答案:**(1)<equation>\varGamma</equation>的方程为<equation>x+y+z=3</equation>(2) 最大值<equation>f(3,0)=f(0,3)=21</equation>，最小值为<equation>f\left(\frac{4}{3},\frac{4}{3}\right)=\frac{17}{27}.</equation>

**解析:**解（I）记<equation>F ( x,y,z) = z - f ( x,y),</equation>，则<equation>F_{x}^{\prime}(x,y,z) = -3x^{2} + 2(x + y),\quad F_{y}^{\prime}(x,y,z) = -3y^{2} + 2(x + y),\quad F_{z}^{\prime}(x,y,z) = 1.</equation>代入<equation>x=1,y=1,z=1</equation>，可得<equation>F_{x}^{\prime}(1,1,1)=1, F_{y}^{\prime}(1,1,1)=1, F_{z}^{\prime}(1,1,1)=1.</equation>于是，曲面<equation>F(x,y,z)</equation><equation>= 0</equation>（即<equation>z = f(x,y)</equation>）在点（1,1,1）处的切平面T的点法式方程为<equation>(x - 1) + (y - 1) + (z - 1) = 0</equation>，即<equation>x + y + z = 3.</equation>（Ⅱ）T与坐标平面所围有界区域在 xOy面上的投影 D = {（x,y）| x+y≤3,x≥0,y≥0} .先求区域 D内部的驻点.

解<equation>\left\{\begin{array}{l l}f_{x}^{\prime}(x,y)=3x^{2}-2(x+y)=0,\\ f_{y}^{\prime}(x,y)=3y^{2}-2(x+y)=0,\end{array} \right.</equation>两式相减并整理可得<equation>x^{2}-y^{2}=0</equation>，解得 x=y或 x=-y. 由于 x≥0,y≥0，故在区域内部不可能有 x=-y.将 x=y代入<equation>3x^{2}-2(x+y)=0</equation>可得<equation>3x^{2}-4x</equation>=0，解得 x<equation>=\frac{4}{3}</equation>（舍去 x=0）.进一步可得驻点坐标为<equation>\left(\frac{4}{3},\frac{4}{3}\right).</equation>计算可得<equation>f \left(\frac {4}{3}, \frac {4}{3}\right) = 2 \cdot \left(\frac {4}{3}\right) ^ {3} - \left(\frac {8}{3}\right) ^ {2} + 3 = \frac {1 7}{2 7}.</equation>下面求边界上的最值.

（i）在边界<equation>y=0,0\leqslant x\leqslant 3</equation>上，<equation>f(x,y)=x^{3}-x^{2}+3.</equation>记<equation>\varphi(x)=x^{3}-x^{2}+3</equation>，则<equation>\varphi^{\prime}(x)=3x^{2}-2x=x(3x-2),x=\frac{2}{3}</equation>是<equation>\varphi(x)</equation>在（0,3）内的驻点，<equation>\varphi\left(\frac{2}{3}\right)=\left(\frac{2}{3}\right)^{3}-\left(\frac{2}{3}\right)^{2}+3=\frac{77}{27}.</equation>在端点 x=0和x=3处，<equation>\varphi(0)=3, \varphi(3)=21.</equation>（ii）在边界<equation>x=0,0\leqslant y\leqslant 3</equation>上，<equation>f(x,y)=y^{3}-y^{2}+3.</equation>最值情况与（i）相同.

（iii）在边界<equation>x + y = 3,0\leqslant x\leqslant 3</equation>上，<equation>f(x,y) = x^{3} + (3 - x)^{3} - 3^{2} + 3.</equation>记<equation>\psi(x)=x^{3}+(3-x)^{3}-6</equation>，则<equation>\psi^{\prime}(x)=3x^{2}-3(3-x)^{2}=18x-27=9(2x-3),x=\frac{3}{2}</equation>是<equation>\psi(x)</equation>在（0,3）内的驻点，<equation>\psi\left(\frac{3}{2}\right)=2\left(\frac{3}{2}\right)^{3}-6=\frac{3}{4}.</equation>在端点 x=0和x=3处，<equation>\psi(0)=21, \psi(3)=21.</equation>比较可得，<equation>f ( 3, 0 ) = f ( 0, 3 ) = 2 1</equation>是<equation>f ( x, y )</equation>在区域D上的最大值，<equation>f \left( \frac{4}{3}, \frac{4}{3} \right) = \frac{1 7}{2 7}</equation>是<equation>f ( x, y )</equation>在区域D上的最小值.

---

**2023年第18题 | 解答题 | 12分**

18. (本题满分12分)

求函数<equation>f ( x,y)=(y-x^{2})(y-x^{3})</equation>的极值.

**答案:**f(x,y)有极小值，极小值为<equation>f\left(\frac{2}{3},\frac{10}{27}\right)=-\frac{4}{729}.</equation>

**解析:**解<equation>\textcircled{1}</equation>计算 f(x,y)的驻点.<equation>\begin{aligned} f _ {x} ^ {\prime} (x, y) &= - 2 x \left(y - x ^ {3}\right) - 3 x ^ {2} \left(y - x ^ {2}\right) = 2 x ^ {4} - 2 x y + 3 x ^ {4} - 3 x ^ {2} y = 5 x ^ {4} - 3 x ^ {2} y - 2 x y \\ &= x \left(5 x ^ {3} - 3 x y - 2 y\right), \end{aligned}</equation><equation>f _ {y} ^ {\prime} (x, y) = y - x ^ {3} + y - x ^ {2} = 2 y - x ^ {3} - x ^ {2}.</equation>令<equation>\left\{\begin{array}{l l}x(5x^{3}-3xy-2y)=0,\\ 2y-x^{3}-x^{2}=0.\end{array} \right.</equation>由<equation>2y-x^{3}-x^{2}=0</equation>可得<equation>y=\frac{x^{2}(x+1)}{2}</equation>将<equation>y=\frac{x^{2}(x+1)}{2}</equation>代入<equation>x(5x^{3}-3xy-2y)=0</equation>可得<equation>x\left[5x^{3}-\frac{3x^{3}(x+1)}{2}-x^{2}(x+1)\right]=0.</equation>整理可得<equation>x^{3}(3x^{2}-5x+2)=</equation>0，即<equation>x^{3}(x-1)(3x-2)=0.</equation>解得<equation>x=0,x=1</equation>或<equation>x=\frac{2}{3}.</equation>由此可得f(x,y)的全部驻点为（0，0）， (1,1），<equation>\left(\frac{2}{3},\frac{10}{27}\right).</equation><equation>\textcircled{2}</equation>计算 f(x,y)的二阶偏导数.<equation>f _ {x x} ^ {\prime \prime} (x, y) = 5 x ^ {3} - 3 x y - 2 y + x \left(1 5 x ^ {2} - 3 y\right) = 2 0 x ^ {3} - 6 x y - 2 y = 2 \left(1 0 x ^ {3} - 3 x y - y\right),</equation><equation>f _ {x y} ^ {\prime \prime} (x, y) = x (- 3 x - 2) = - 3 x ^ {2} - 2 x,</equation><equation>f _ {y y} ^ {\prime \prime} (x, y) = 2.</equation><equation>\textcircled{3}</equation>计算<equation>AC-B^{2}.</equation>（i）对点（0,0），<equation>A=f_{xx}^{\prime \prime}(0,0)=0,B=f_{xy}^{\prime \prime}(0,0)=0,C=f_{yy}^{\prime \prime}(0,0)=2,AC-B^{2}=0.</equation>我们无法由二元函数极值存在的充分条件判断该点是否为极值点.

由<equation>f ( x,y )</equation>的表达式可知，<equation>f ( 0,0 )=0.</equation>取<equation>y=2 x^{2}</equation>，当x为充分小的正数时，<equation>f (x, y) = \left(2 x ^ {2} - x ^ {2}\right) \left(2 x ^ {2} - x ^ {3}\right) = x ^ {4} (2 - x) > 0.</equation>取<equation>y=2 x^{3}</equation>，当x为充分小的正数时，<equation>f (x, y) = \left(2 x ^ {3} - x ^ {2}\right) \left(2 x ^ {3} - x ^ {3}\right) = x ^ {5} (2 x - 1) < 0.</equation>因此，不论在点（0，0）的多么小的邻域内，均既有<equation>f ( x,y)>0</equation>的点，也有<equation>f ( x,y)<0</equation>的点.根据极值点的定义，点（0，0）不是<equation>f ( x,y)</equation>的极值点.

（ii）对点（1，1），<equation>A=f_{xx}^{\prime \prime}(1,1)=1 2, B=f_{xy}^{\prime \prime}(1,1)=-5, C=f_{yy}^{\prime \prime}(1,1)=2, A C-B^{2}=-1<</equation>0.由二元函数极值存在的充分条件可知，点（1，1）不是<equation>f(x,y)</equation>的极值点.

（iii）对点<equation>\left(\frac{2}{3},\frac{10}{27}\right),A=f_{xx}^{\prime \prime}\left(\frac{2}{3},\frac{10}{27}\right)=\frac{100}{27},B=f_{xy}^{\prime \prime}\left(\frac{2}{3},\frac{10}{27}\right)=-\frac{8}{3},C=f_{yy}^{\prime \prime}\left(\frac{2}{3},\frac{10}{27}\right)=2,</equation><equation>AC-B^{2}=\frac{8}{27}>0</equation>，且 A > 0.由二元函数极值存在的充分条件可知，点<equation>\left(\frac{2}{3},\frac{10}{27}\right)</equation>是 f(x,y)的极小值点.极小值为<equation>f \left(\frac {2}{3}, \frac {1 0}{2 7}\right) = \left(\frac {1 0}{2 7} - \frac {4}{9}\right) \times \left(\frac {1 0}{2 7} - \frac {8}{2 7}\right) = - \frac {4}{7 2 9}.</equation>

---

**2022年第13题 | 填空题 | 5分**

13. 当<equation>x \geqslant 0, y \geqslant 0</equation>时，<equation>x^{2}+y^{2} \leqslant k \mathrm{e}^{x+y}</equation>恒成立，则<equation>k</equation>的取值范围是 ___

**答案:**[<equation>4 \mathrm{e}^{-2},+\infty)</equation>.

**解析:**解不等式<equation>x^{2}+y^{2}\leqslant k \mathrm{e}^{x+y}</equation>等价于<equation>\left(x^{2}+y^{2}\right)\mathrm{e}^{-(x+y)}\leqslant k.</equation>记<equation>f(x,y) = (x^{2} + y^{2})\mathrm{e}^{-(x + y)}, D = \{(x,y) \mid x \geqslant 0, y \geqslant 0\}</equation>.

计算 f(x,y)在 D 内的驻点.<equation>f _ {x} ^ {\prime} (x, y) = 2 x \mathrm {e} ^ {- (x + y)} - \left(x ^ {2} + y ^ {2}\right) \mathrm {e} ^ {- (x + y)} = \left(2 x - x ^ {2} - y ^ {2}\right) \mathrm {e} ^ {- (x + y)},</equation><equation>f _ {y} ^ {\prime} (x, y) = 2 y \mathrm {e} ^ {- (x + y)} - \left(x ^ {2} + y ^ {2}\right) \mathrm {e} ^ {- (x + y)} = \left(2 y - x ^ {2} - y ^ {2}\right) \mathrm {e} ^ {- (x + y)}.</equation>解<equation>\left\{ \begin{array}{l} 2x - x^2 - y^2 = 0, \\ 2y - x^2 - y^2 = 0. \end{array} \right.</equation>两式相减得<equation>x = y</equation>，将<equation>x = y</equation>代入<equation>2x - x^2 - y^2 = 0</equation>可得<equation>2x - 2x^2 = 0</equation>，从而<equation>x = 0</equation>或<equation>x = 1.</equation><equation>\left\{ \begin{array}{l} x = 0, \\ y = 0 \end{array} \right.</equation>和<equation>\left\{ \begin{array}{l} x = 1, \\ y = 1 \end{array} \right.</equation>为该方程组的两组解.由于所求为区域D内部的驻点，故舍去点(0,0).点(1,1)为<equation>f(x,y)</equation>在区域D内部的唯一驻点.<equation>f(1,1) = 2\mathrm{e}^{-2}.</equation>下面计算<equation>f(x,y)</equation>在区域<equation>D</equation>的边界<equation>x = 0</equation>与<equation>y = 0</equation>上的最大值.

当<equation>x = 0</equation>时，<equation>f(0,y) = y^{2}\mathrm{e}^{-y}</equation>.记<equation>f_{1}(y) = y^{2}\mathrm{e}^{-y}</equation>，则<equation>f_{1}^{\prime}(y) = (2y - y^{2})\mathrm{e}^{-y}</equation>.解<equation>2y - y^{2} = 0</equation>得<equation>y = 0</equation>或<equation>y = 2</equation>.当<equation>0 < y < 2</equation>时，<equation>f_{1}^{\prime}(y) > 0</equation>，<equation>f_{1}(y)</equation>单调增加，当<equation>y > 2</equation>时，<equation>f_{1}^{\prime}(y) < 0</equation>，<equation>f_{1}(y)</equation>单调减少.于是，<equation>f(0,2) = 4\mathrm{e}^{-2}</equation>为<equation>f(x,y)</equation>在边界<equation>x = 0</equation>上的最大值.

同理可得，<equation>f ( 2, 0 ) = 4 \mathrm{e}^{-2}</equation>为<equation>f ( x,y )</equation>在边界<equation>y=0</equation>上的最大值.

比较<equation>f ( 1,1), f ( 0,2), f ( 2,0)</equation>可得，<equation>f ( 0,2)=f ( 2,0)=4 \mathrm{e}^{-2}</equation>为<equation>f ( x,y)</equation>在区域D上的最大值综上所述，<equation>k</equation>的取值范围为<equation>[ 4 \mathrm{e}^{-2},+\infty).</equation>

---

**2021年第19题 | 解答题 | 12分**

19. (本题满分12分)

已知曲线 C：<equation>\left\{ \begin{array}{l l} x^{2}+2 y^{2}-z=6, \\ 4 x+2 y+z=3 0, \end{array} \right.</equation>求 C上的点到 xOy坐标面距离的最大值.

**答案:**## 最大值为66.

**解析:**解设目标函数为<equation>f ( x,y,z) = z^{2}.</equation>记<equation>\varphi ( x,y,z) = x^{2}+2 y^{2}-z-6,\psi ( x,y,z) = 4 x+2 y+z-3 0</equation>则约束条件为<equation>\varphi ( x,y,z) = 0,\psi ( x,y,z) = 0.</equation>建立拉格朗日函数<equation>L (x, y, z, \lambda , \mu) = z ^ {2} + \lambda \left(x ^ {2} + 2 y ^ {2} - z - 6\right) + \mu \left(4 x + 2 y + z - 3 0\right).</equation>对拉格朗日函数的各个变量分别求偏导，并令其为零，可得如下方程组.<equation>\left[ L _ {x} ^ {\prime} (x, y, z, \lambda , \mu) \right] = 2 \lambda x + 4 \mu = 0,</equation><equation>L _ {y} ^ {\prime} (x, y, z, \lambda , \mu) = 4 \lambda y + 2 \mu = 0,</equation><equation>L _ {z} ^ {\prime} (x, y, z, \lambda , \mu) = 2 z - \lambda + \mu = 0,</equation><equation>L _ {\lambda} ^ {\prime} (x, y, z, \lambda , \mu) = x ^ {2} + 2 y ^ {2} - z - 6 = 0,</equation><equation>L _ {\mu} ^ {\prime} (x, y, z, \lambda , \mu) = 4 x + 2 y + z - 3 0 = 0.</equation>(2) 式<equation>\times2-（1）</equation>式，并整理可得<equation>\lambda(4 y-x)=0.</equation>（i）若<equation>\lambda=0</equation>，则由（1）式，（2）式可得<equation>\mu=0</equation>，再由（3）式可得 z=0.此时，由（4）式，（5）式可得<equation>\left\{\begin{array}{l l}x^{2}+2 y^{2}=6\\2 x+y=1 5.\end{array}\right.</equation>椭圆<equation>x^{2}+2 y^{2}=6</equation>的长轴为x轴，短轴为y轴，长、短半轴长分别为<equation>\sqrt{6},\sqrt{3}</equation>，而直线<equation>2 x+y=1 5</equation>在x轴，y轴上的截距分别为<equation>\frac{1 5}{2}</equation>，15.从而直线<equation>2 x+y=1 5</equation>位于椭圆<equation>x^{2}+2 y^{2}=6</equation>上方，该方程无解.

（ii）若<equation>4 y - x = 0</equation>，则先由（4）式，（5）式消去变量<equation>z</equation>再代入该关系.

(4) 式 +（5）式可得<equation>x^{2}+4 x+2 y^{2}+2 y=3 6</equation>代入<equation>x=4 y</equation>可得，<equation>1 6 y^{2}+1 6 y+2 y^{2}+2 y=3 6</equation>整理可得<equation>y^{2}+y-2=0</equation>解得<equation>y=-2</equation>或<equation>y=1.</equation>当<equation>y = -2, x = -8</equation>时，由（5）式可得<equation>z = 66</equation>；当<equation>y = 1, x = 4</equation>时，由（5）式可得<equation>z = 12</equation>.

比较可得，在曲线 C上，点（-8，-2，66）到<equation>x O y</equation>面的距离最大，最大值为66.

---

**2020年第15题 | 解答题 | 10分**

15. (本题满分10分）

求函数<equation>f ( x,y)=x^{3}+8 y^{3}-x y</equation>的极值.

**答案:**<equation>\text {极 小 值} f \left(\frac {1}{6}, \frac {1}{1 2}\right) = - \frac {1}{2 1 6}.</equation>

**解析:**解<equation>\textcircled{1}</equation>计算 f(x,y)的驻点.

解<equation>\left\{ \begin{array}{l l} f_{x}^{\prime}(x,y)=3x^{2}-y=0, \\ f_{y}^{\prime}(x,y)=24y^{2}-x=0. \end{array} \right.</equation>将 y=3x²代入24y²-x=0可得216x⁴=x，解得x=0或x<equation>=\frac{1}{6}.</equation>于是，<equation>\left\{ \begin{array}{l l} x=0, \\ y=0 \end{array} \right.</equation>或<equation>\left\{ \begin{array}{l l} x=\frac{1}{6}, \\ y=\frac{1}{12}. \end{array} \right.</equation><equation>f(x,y)</equation>有两个驻点(0,0)，<equation>\left(\frac{1}{6},\frac{1}{12}\right).</equation><equation>\textcircled{2}</equation>计算 f(x,y)的二阶偏导数.<equation>f_{xx}^{\prime\prime}(x,y)=6x,</equation><equation>f_{xy}^{\prime\prime}(x,y)=-1,</equation><equation>f_{yy}^{\prime\prime}(x,y)=48y.</equation><equation>\textcircled{3}</equation>判断驻点是否为极值点以及确定极值点类型.

• 考虑驻点(0,0).<equation>A=f_{xx}^{\prime\prime}(0,0)=0,</equation><equation>B=f_{xy}^{\prime\prime}(0,0)=-1,</equation><equation>C=f_{yy}^{\prime\prime}(0,0)=0.</equation><equation>AC-B^{2}=0-1=-1<0</equation>，故点(0,0)不是极值点.

• 考虑驻点<equation>\left(\frac{1}{6},\frac{1}{12}\right).</equation><equation>A=f_{xx}^{\prime\prime}\left(\frac{1}{6},\frac{1}{12}\right)=1,</equation><equation>B=f_{xy}^{\prime\prime}\left(\frac{1}{6},\frac{1}{12}\right)=-1,</equation><equation>C=f_{yy}^{\prime\prime}\left(\frac{1}{6},\frac{1}{12}\right)=4.</equation><equation>AC-B^{2}=4-1=3>0</equation>，且 A>0，故点<equation>\left(\frac{1}{6},\frac{1}{12}\right)</equation>为极小值点，极小值为<equation>f\left(\frac{1}{6},\frac{1}{12}\right)=\frac{1}{6^{3}}+\frac{8}{12^{3}}-\frac{1}{6 \times 12}=-\frac{1}{216}.</equation>

---

**2018年第16题 | 解答题 | 10分**

16. (本题满分10分)

将长为 2m的铁丝分成三段，依次围成圆、正方形与正三角形. 三个图形的面积之和是否存在最小值？若存在，求出最小值.

**答案:**三个图形的面积之和存在最小值，最小值为<equation>\frac{1}{\pi+4+3\sqrt{3}}.</equation>

**解析:**解设圆、正方形、正三角形的周长分别为 x,y,z，则圆的半径<equation>r=\frac{x}{2\pi}</equation>正方形的边长 a<equation>=\frac{y}{4}</equation>正三角形的边长 b<equation>=\frac{z}{3}</equation>.于是，三个图形的面积之和为<equation>S (x, y, z) = \pi \cdot \left(\frac {x}{2 \pi}\right) ^ {2} + \left(\frac {y}{4}\right) ^ {2} + \frac {1}{2} \cdot \left(\frac {z}{3}\right) ^ {2} \cdot \sin \frac {\pi}{3} = \frac {x ^ {2}}{4 \pi} + \frac {y ^ {2}}{1 6} + \frac {\sqrt {3}}{3 6} z ^ {2}.</equation>由于三段铁丝的周长之和为2，故<equation>x+y+z=2.</equation>建立拉格朗日函数<equation>L(x,y,z,\lambda) = \frac{x^{2}}{4\pi} +\frac{y^{2}}{16} +\frac{\sqrt{3}}{36} z^{2} +\lambda (x + y + z - 2).</equation>令<equation>\left\{ \begin{array}{l} L _ {x} ^ {\prime} = \frac {1}{2 \pi} x + \lambda = 0, \\ L _ {y} ^ {\prime} = \frac {1}{8} y + \lambda = 0, \\ L _ {z} ^ {\prime} = \frac {\sqrt {3}}{1 8} z + \lambda = 0, \\ L _ {\lambda} ^ {\prime} = x + y + z - 2 = \end{array} \right.</equation>由前三个方程可得<equation>x = -2\pi \lambda ,y = -8\lambda ,z = -6\sqrt{3}\lambda .</equation>代入 x+y+z-2=0可得<equation>\lambda = - \frac {2}{2 \pi + 8 + 6 \sqrt {3}} = - \frac {1}{\pi + 4 + 3 \sqrt {3}}.</equation>于是，<equation>x=\frac{2\pi}{\pi+4+3\sqrt{3}}, y=\frac{8}{\pi+4+3\sqrt{3}}, z=\frac{6\sqrt{3}}{\pi+4+3\sqrt{3}}.</equation>将所得<equation>x,y,z</equation>的值代入<equation>S(x,y,z)</equation>可得<equation>S (x, y, z) = \frac {\pi + 4 + 3 \sqrt {3}}{(\pi + 4 + 3 \sqrt {3}) ^ {2}} = \frac {1}{\pi + 4 + 3 \sqrt {3}}.</equation>为了判定所求得可能的极值点是否为最小值点，我们把问题转化为目标函数<equation>S ( x, y, z )</equation>在有界闭区域<equation>D=\{(x,y,z)\mid x+y+z=2,x\geqslant0,y\geqslant0,z\geqslant0\}</equation>上的最值问题.

由于连续函数在有界闭区域上一定能取到最值，故若我们能分别计算出<equation>S ( x, y, z )</equation>在边界<equation>y + z = 2, z + x = 2, x + y = 2</equation>上的最值，再与<equation>\frac{1}{\pi+4+3\sqrt{3}}</equation>比较，则所得最小值即为区域D上的最小值.

当<equation>x = 0</equation>时，<equation>S(0,y,z)</equation>在<equation>y + z = 2</equation>下的最小值为<equation>S\left(0,\frac{8}{4 + 3\sqrt{3}},\frac{6\sqrt{3}}{4 + 3\sqrt{3}}\right) = \frac{1}{4 + 3\sqrt{3}}.</equation>当<equation>y=0</equation>时，<equation>S ( x, 0, z )</equation>在<equation>x+z=2</equation>下的最小值为<equation>S \left( \frac{2 \pi}{\pi+3 \sqrt{3}}, 0, \frac{6 \sqrt{3}}{\pi+3 \sqrt{3}} \right)=\frac{1}{\pi+3 \sqrt{3}}.</equation>当<equation>z = 0</equation>时，<equation>S(x,y,0)</equation>在<equation>x + y = 2</equation>下的最小值为<equation>S\left(\frac{2\pi}{\pi + 4},\frac{8}{\pi + 4},0\right) = \frac{1}{\pi + 4}</equation>4个值比较可得，<equation>\frac{1}{\pi+4+3\sqrt{3}}</equation>为整个区域D上的最小值，也为<equation>x+y+z=2,x>0,y>0,z>0</equation>时的<equation>S(x,y,z)</equation>的最小值.三个图形的面积之和存在最小值，最小值为<equation>\frac{1}{\pi+4+3\sqrt{3}}.</equation>

---

**2015年第17题 | 解答题 | 10分**

17. (本题满分10分）

已知函数<equation>f ( x,y)=x+y+ x y</equation>，曲线 C：<equation>x^{2}+y^{2}+ x y=3</equation>，求 f(x,y)在曲线 C上的最大方向导数.

**解析:**解 由于函数在一点处的方向导数的最大值等于函数在该点的梯度的模，故求<equation>f ( x,y )</equation>在曲线 C上的最大方向导数等价于求<equation>f ( x,y )</equation>在曲线C上梯度的模的最大值.为了计算方便，考虑梯度模的平方函数.令<equation>g ( x,y ) = f_{x}^{\prime 2}+f_{y}^{\prime 2}=(1+y)^{2}+(1+x)^{2}</equation>，下面求<equation>g ( x,y )</equation>在条件<equation>x^{2}+y^{2}+xy=3</equation>下的最值.作拉格朗日函数<equation>L (x, y, \lambda) = (1 + y) ^ {2} + (1 + x) ^ {2} + \lambda \left(x ^ {2} + y ^ {2} + x y - 3\right).</equation>令<equation>\left[ L _ {x} ^ {\prime} = 2 (1 + x) + \lambda (2 x + y) = 0, \right.</equation><equation>\left\{L _ {y} ^ {\prime} = 2 (1 + y) + \lambda (2 y + x) = 0, \right.</equation><equation>L _ {\lambda} ^ {\prime} = x ^ {2} + y ^ {2} + x y - 3 = 0.</equation>由（1）、(2）消去<equation>\lambda</equation>得到<equation>(x - y)(x + y - 1) = 0</equation>，从而<equation>x = y</equation>或<equation>x + y = 1</equation>若 x = y，代入（3）式，解得 x = y =<equation>\pm 1</equation>；若 x+y=1，代入（3）式，解得 x=2，y=-1或 x=-1， y=2.于是（1，1），（-1，-1），（2，-1），（-1，2）都是可能的最值点.又<equation>g (1, 1) = 8, \quad g (- 1, - 1) = 0, \quad g (2, - 1) = g (- 1, 2) = 9,</equation>故<equation>g ( x,y )</equation>在条件<equation>x^{2}+y^{2}+xy=3</equation>下的最大值为9，从而<equation>f ( x,y )</equation>在曲线C上的最大方向导数为3.

---

**2013年第17题 | 解答题 | 10分**

17. (本题满分10分）

求函数<equation>f ( x,y)=\left(y+\frac{x^{3}}{3}\right)\mathrm{e}^{x+y}</equation>的极值.

**解析:**解 由题设知，<equation>f _ {x} ^ {\prime} (x, y) = x ^ {2} \mathrm {e} ^ {x + y} + \left(y + \frac {x ^ {3}}{3}\right) \mathrm {e} ^ {x + y} = \left(x ^ {2} + y + \frac {x ^ {3}}{3}\right) \mathrm {e} ^ {x + y},</equation><equation>f _ {y} ^ {\prime} (x, y) = \mathrm {e} ^ {x + y} + \left(y + \frac {x ^ {3}}{3}\right) \mathrm {e} ^ {x + y} = \left(1 + y + \frac {x ^ {3}}{3}\right) \mathrm {e} ^ {x + y}.</equation>令<equation>\left\{ \begin{array}{l} f_x^{\prime}(x,y) = 0, \\ f_y^{\prime}(x,y) = 0, \end{array} \right.</equation>即<equation>\left\{ \begin{array}{l} x^{2} + y + \frac{x^{3}}{3} = 0, \\ 1 + y + \frac{x^{3}}{3} = 0, \end{array} \right.</equation>解得驻点为<equation>\left(1, - \frac{4}{3}\right), \left(-1, - \frac{2}{3}\right).</equation>计算 f(x,y)的二阶偏导数.<equation>f _ {x x} ^ {\prime \prime} = \left(\frac {x ^ {3}}{3} + 2 x ^ {2} + 2 x + y\right) \mathrm {e} ^ {x + y},</equation><equation>f _ {x y} ^ {\prime \prime} = \left(\frac {x ^ {3}}{3} + x ^ {2} + y + 1\right) \mathrm {e} ^ {x + y},</equation><equation>f _ {y y} ^ {\prime \prime} = \left(\frac {x ^ {3}}{3} + y + 2\right) \mathrm {e} ^ {x + y}.</equation>在驻点<equation>\left( 1,-\frac{4}{3} \right)</equation>处，<equation>A = f _ {x x} ^ {\prime \prime} \left(1, - \frac {4}{3}\right) = 3 \mathrm {e} ^ {- \frac {1}{3}}, \quad B = f _ {x y} ^ {\prime \prime} \left(1, - \frac {4}{3}\right) = \mathrm {e} ^ {- \frac {1}{3}}, \quad C = f _ {y y} ^ {\prime \prime} \left(1, - \frac {4}{3}\right) = \mathrm {e} ^ {- \frac {1}{3}},</equation>于是<equation>AC - B^{2} = 2\mathrm{e}^{-\frac{2}{3}} > 0,A > 0</equation>，故点<equation>\left(1, - \frac{4}{3}\right)</equation>为<equation>f(x,y)</equation>的极小值点，极小值为<equation>f\left(1, - \frac{4}{3}\right) = -\mathrm{e}^{-\frac{1}{3}}.</equation>在驻点<equation>\left(-1,-\frac{2}{3}\right)</equation>处，<equation>A = f _ {x x} ^ {\prime \prime} \left(- 1, - \frac {2}{3}\right) = - \mathrm {e} ^ {- \frac {5}{3}}, \quad B = f _ {x y} ^ {\prime \prime} \left(- 1, - \frac {2}{3}\right) = \mathrm {e} ^ {- \frac {5}{3}}, \quad C = f _ {y y} ^ {\prime \prime} \left(- 1, - \frac {2}{3}\right) = \mathrm {e} ^ {- \frac {5}{3}},</equation>于是<equation>AC-B^{2}=-2\mathrm{e}^{-\frac{10}{3}}<0</equation>，故点<equation>\left(-1,-\frac{2}{3}\right)</equation>不是极值点.

综上所述，<equation>f ( x,y)</equation>只在点<equation>\left( 1,-\frac{4}{3} \right)</equation>处取得极值<equation>f\left( 1,-\frac{4}{3}\right)=-\mathrm{e}^{-\frac{1}{3}}</equation>，且为极小值.

---

**2012年第16题 | 解答题 | 10分**

16. (本题满分10分）

求函数<equation>f ( x,y)=x \mathrm{e}^{- \frac{x^{2}+y^{2}}{2}}</equation>的极值.

**答案:**(16) 极大值<equation>f(1,0) = \mathrm{e}^{-\frac{1}{2}}</equation>，极小值<equation>f(-1,0) = -\mathrm{e}^{-\frac{1}{2}}.</equation>

**解析:**解<equation>\textcircled{1}</equation>先找到 f(x,y)的全部驻点.

记<equation>g ( x,y) = \mathrm{e}^{- \frac{x^{2}+y^{2}}{2}}.</equation>由于<equation>f _ {x} ^ {\prime} (x, y) = \mathrm {e} ^ {- \frac {x ^ {2} + y ^ {2}}{2}} + x \cdot \mathrm {e} ^ {- \frac {x ^ {2} + y ^ {2}}{2}} \cdot (- x) = \left(1 - x ^ {2}\right) \mathrm {e} ^ {- \frac {x ^ {2} + y ^ {2}}{2}} = \left(1 - x ^ {2}\right) g (x, y),</equation><equation>f _ {y} ^ {\prime} (x, y) = - x y \mathrm {e} ^ {- \frac {x ^ {2} + y ^ {2}}{2}} = (- x y) g (x, y).</equation>由于 g(x,y) > 0，故满足<equation>\left\{\begin{array}{l l}1-x^{2}=0\\-xy=0\end{array}\right.</equation>的点（x，y）为 f(x，y）的驻点.解该方程组得（x，y）= （<equation>\pm1,0).</equation>因此，点（1，0）和点（-1，0）为<equation>f ( x,y)</equation>的全部驻点.<equation>\textcircled{2}</equation>计算二阶偏导数.<equation>f _ {x x} ^ {\prime \prime} (x, y) = (- 2 x) g (x, y) + \left(1 - x ^ {2}\right) g _ {x} ^ {\prime} (x, y),</equation><equation>f _ {x y} ^ {\prime \prime} (x, y) = \left(1 - x ^ {2}\right) g _ {y} ^ {\prime} (x, y),</equation><equation>f _ {y y} ^ {\prime \prime} (x, y) = (- x) g (x, y) + (- x y) g _ {y} ^ {\prime} (x, y).</equation><equation>\textcircled{3}</equation>计算<equation>A C-B^{2}.</equation>由于<equation>f(x,y)</equation>的驻点<equation>(x_0,y_0)</equation>均满足<equation>1 - x_0^2 = 0, - x_0y_0 = 0</equation>，而<equation>g(x,y)</equation>恒大于零，故在驻点 (1,0) 处，<equation>f_{xx}^{\prime \prime}(1,0) = -2g(1,0) < 0, f_{xy}^{\prime \prime}(1,0) = 0, f_{yy}^{\prime \prime}(1,0) = -g(1,0)</equation>.因此，<equation>f _ {x x} ^ {\prime \prime} (1, 0) f _ {y y} ^ {\prime \prime} (1, 0) - \left[ f _ {x y} ^ {\prime \prime} (1, 0) \right] ^ {2} = 2 g ^ {2} (1, 0) > 0.</equation>由于<equation>f_{xx}^{\prime \prime}(1,0)=-2 g(1,0)<0</equation>，故点（1，0）为<equation>f(x,y)</equation>的极大值点，<equation>f(1,0)=\mathrm{e}^{-\frac{1}{2}}</equation>为<equation>f(x,y)</equation>的极大值.同理可得，点（-1，0）为<equation>f(x,y)</equation>的极小值点，<equation>f(-1,0)=-\mathrm{e}^{-\frac{1}{2}}</equation>为<equation>f(x,y)</equation>的极小值.

因此，函数<equation>f ( x,y) = x \mathrm{e}^{- \frac{x^{2}+y^{2}}{2}}</equation>的极大值为<equation>\mathrm{e}^{- \frac{1}{2}}</equation>，极小值为<equation>- \mathrm{e}^{- \frac{1}{2}}.</equation>

---

**2011年第3题 | 选择题 | 4分 | 答案: A**

3. 设函数 f(x)具有二阶连续导数，且 f(x) > 0，<equation>f^{\prime}(0)=0</equation>，则函数 z=f(x)<equation>\ln f(y)</equation>在点 (0,0)处取得极小值的一个充分条件是（    ）

A.<equation>f(0)>1,f^{\prime\prime}(0)>0</equation>B.<equation>f(0)>1,f^{\prime\prime}(0)<0</equation>C.<equation>f(0)<1,f^{\prime\prime}(0)>0</equation>D.<equation>f(0)<1,f^{\prime\prime}(0)<0</equation>

答案: A

**解析:**由题设知，<equation>\left. \frac {\partial z}{\partial x} \right| _ {(0, 0)} = f ^ {\prime} (x) \ln f (y) \Big | _ {(0, 0)} = f ^ {\prime} (0) \ln f (0) = 0,</equation><equation>\left. \frac {\partial z}{\partial y} \right| _ {(0, 0)} = \frac {f (x) f ^ {\prime} (y)}{f (y)} \Bigg | _ {(0, 0)} = \frac {f (0) f ^ {\prime} (0)}{f (0)} = 0.</equation>从而点（0，0）为函数<equation>z ( x,y)</equation>的驻点.又<equation>A = \left. \frac {\partial^ {2} z}{\partial x ^ {2}} \right| _ {(0, 0)} = f ^ {\prime \prime} (x) \ln f (y) \Big | _ {(0, 0)} = f ^ {\prime \prime} (0) \ln f (0),</equation><equation>B = \left. \frac {\partial^ {2} z}{\partial x \partial y} \right| _ {(0, 0)} = \left. \frac {f ^ {\prime} (x) f ^ {\prime} (y)}{f (y)} \right| _ {(0, 0)} = \frac {f ^ {\prime} (0) f ^ {\prime} (0)}{f (0)} = 0,</equation><equation>C = \left. \frac {\partial^ {2} z}{\partial y ^ {2}} \right| _ {(0, 0)} = f (x) \cdot \frac {f ^ {\prime \prime} (y) f (y) - \left[ f ^ {\prime} (y) \right] ^ {2}}{f ^ {2} (y)} \Bigg | _ {(0, 0)} = \frac {f ^ {2} (0) f ^ {\prime \prime} (0) - f (0) \left[ f ^ {\prime} (0) \right] ^ {2}}{f ^ {2} (0)} = f ^ {\prime \prime} (0).</equation>令<equation>A=f^{\prime \prime}(0)\ln f(0)>0, A C-B^{2}=[f^{\prime \prime}(0)]^{2}\ln f(0)>0</equation>，解得<equation>f(0)>1,f^{\prime \prime}(0)>0.</equation>因此，<equation>f(0)>1,f^{\prime \prime}(0)>0</equation>为函数<equation>z(x,y)</equation>在点（0,0）处取得极小值的一个充分条件.应选A.

---

**2009年第15题 | 解答题 | 10分**

15. (本题满分9分）

求二元函数<equation>f ( x,y)=x^{2}\left( 2+y^{2}\right)+y\ln y</equation>的极值.

**答案:**(15) 极小值<equation>f\left(0,\frac{1}{\mathrm{e}}\right) = -\frac{1}{\mathrm{e}}.</equation>

**解析:**解 令<equation>\left\{\begin{array}{l l}f_{x}^{\prime}(x,y)=2 x(2+y^{2})=0,\\ f_{y}^{\prime}(x,y)=2 x^{2} y+\ln y+1=0,\end{array} \right.</equation>解得驻点为<equation>\left(0,\frac{1}{e}\right).</equation>f(x,y)的二阶偏导数为<equation>f_{xx}^{\prime \prime}(x,y)=2(2+y^{2}),</equation><equation>f_{xy}^{\prime \prime}(x,y)=4 x y,</equation><equation>f_{yy}^{\prime \prime}(x,y)=2 x^{2}+\frac{1}{y},</equation>于是<equation>A=f_{xx}^{\prime \prime}\left(0,\frac{1}{e}\right)=2\left(2+\frac{1}{e^{2}}\right),</equation><equation>B=f_{xy}^{\prime \prime}\left(0,\frac{1}{e}\right)=0,</equation><equation>C=f_{yy}^{\prime \prime}\left(0,\frac{1}{e}\right)=\mathrm{e}.</equation>由于<equation>AC-B^{2}>0,</equation><equation>A>0</equation>，故f(x,y)在<equation>\left(0,\frac{1}{e}\right)</equation>处取得极小值<equation>f\left(0,\frac{1}{e}\right)=-\frac{1}{e}.</equation>

---


#### 多元函数微分学的几何应用

**2023年第12题 | 填空题 | 5分**

12. 曲面<equation>z=x+2y+\ln(1+x^2+y^2)</equation>在点<equation>(0,0,0)</equation>处的切平面方程为 ___

**答案:**<equation>x + 2 y - z = 0.</equation>

**解析:**解记曲面<equation>z = x + 2y + \ln (1 + x^{2} + y^{2})</equation>为<equation>\varSigma, F(x,y,z) = x + 2y + \ln (1 + x^{2} + y^{2}) - z</equation>，则曲面<equation>\varSigma</equation>的方程为<equation>F(x,y,z) = 0</equation>，其在点（x,y,z）处的一个法向量为<equation>\left(\frac {\partial F}{\partial x}, \frac {\partial F}{\partial y}, \frac {\partial F}{\partial z}\right) = \left(1 + \frac {2 x}{1 + x ^ {2} + y ^ {2}}, 2 + \frac {2 y}{1 + x ^ {2} + y ^ {2}}, - 1\right).</equation>代入点（0，0，0）的坐标可得曲面<equation>\varSigma</equation>在点（0，0，0）处的法向量为（1，2，-1）.因此，曲面<equation>\varSigma</equation>在点 （0，0，0）处的切平面方程为<equation>(x - 0) + 2 (y - 0) - (z - 0) = 0,</equation>即<equation>x+2y-z=0.</equation>

---

**2018年第2题 | 选择题 | 4分 | 答案: B**

2. 过点（1,0,0），（0,1,0），且与曲面<equation>z=x^{2}+y^{2}</equation>相切的平面为（    )

A.<equation>z=0</equation>与<equation>x+y-z=1</equation>B.<equation>z=0</equation>与<equation>2 x+2 y-z=2</equation>C.<equation>x=y</equation>与<equation>x+y-z=1</equation>D.<equation>x=y</equation>与<equation>2 x+2 y-z=2</equation>

答案: B

**解析:**解（法一）记<equation>F ( x,y,z) = z - x^{2} - y^{2}</equation>，则曲面<equation>z = x^{2} + y^{2}</equation>的方程为<equation>F ( x,y,z) = 0.</equation>根据曲面的切平面的定义，曲面<equation>F ( x,y,z) = 0</equation>在点（x,y,z）处的切平面的一个法向量为<equation>(-2x,-2y,1)</equation>（也可以取作（2x,2y，-1）).于是，该点处的切平面的点法式方程为<equation>- 2 x (X - x) - 2 y (Y - y) + (Z - z) = 0.</equation>由于所求切平面过点（1，0，0），（0，1，0），故将这两点的坐标分别代入（1）式可得，<equation>- 2 x (1 - x) + 2 y ^ {2} - z \frac {x ^ {2} + y ^ {2} = z}{- 2 x + z} - 2 x + z = 0,</equation><equation>2 x ^ {2} - 2 y (1 - y) - z \xlongequal {x ^ {2} + y ^ {2} = z} - 2 y + z = 0.</equation>联立<equation>\left\{ \begin{array}{l l} z = 2x, \\ z = 2y, \\ z = x^{2} + y^{2}. \end{array} \right.</equation>由前两个方程可得<equation>x = y</equation>，代入第三个方程可得<equation>2x = 2x^{2}</equation>，解得<equation>x = 0</equation>或<equation>x = 1</equation>. 当<equation>x = 0</equation>时，<equation>y = 0, z = 0</equation>；当<equation>x = 1</equation>时，<equation>y = 1, z = 2</equation>. 从而切点坐标为（0,0,0）或（1,1,2）.

将这两个切点的坐标分别代入（1）式，可得所求切平面的方程分别为 Z=0与<equation>2 X+2 Y-Z=2</equation>因此，应选B.

（法二）排除法.

由于点（1，0，0）和点（0，1，0）均位于所求切平面上，而这两点均不满足方程 x=y，故可排除选项C和选项D.

另一方面，曲面<equation>z=x^{2}+y^{2}</equation>上点（x,y,z）处的切平面的法向量应与（2x，2y，-1）共线.平面<equation>x+y-z=1</equation>的一个法向量为（1，1，-1).若其为切平面，则<equation>\frac{2x}{1}=\frac{2y}{1}=\frac{-1}{-1}</equation>，切点坐标应满足<equation>x=\frac{1}{2}</equation><equation>y=\frac{1}{2}</equation>.代入<equation>z=x^{2}+y^{2}</equation>得<equation>z=\frac{1}{2}</equation>.但是<equation>\left(\frac{1}{2},\frac{1}{2},\frac{1}{2}\right)</equation>并不满足方程<equation>x+y-z=1</equation>.于是，选项A也不正确.

由排除法可知，应选B.

---

**2014年第9题 | 填空题 | 4分**

9. 曲面<equation>z=x^{2}(1-\sin y)+y^{2}(1-\sin x)</equation>在点（1,0,1）处的切平面方程为 ___

**答案:**<equation>2 x - y - z - 1 = 0.</equation>

**解析:**从而切平面的方程为<equation>2 ( x - 1 ) - ( y - 0 ) - ( z - 1 ) = 0</equation>即<equation>2 x - y - z - 1 = 0.</equation>

---

**2013年第2题 | 选择题 | 4分 | 答案: A**

2. 曲面<equation>x^{2}+\cos(xy)+yz+x=0</equation>在点（0，1，-1）处的切平面方程为（    ）

A.<equation>x-y+z=-2</equation>B.<equation>x+y+z=0</equation>C.<equation>x-2y+z=-3</equation>D.<equation>x-y-z=0</equation>

答案: A

**解析:**解 令<equation>F ( x,y,z) = x^{2} + \cos ( x y ) + y z + x</equation>，则曲面在点（0，1，-1）处的法向量为<equation>\left. \left(\frac {\partial F}{\partial x}, \frac {\partial F}{\partial y}, \frac {\partial F}{\partial z}\right) \right| _ {(0, 1, - 1)} = \left(2 x - y \sin (x y) + 1, - x \sin (x y) + z, y\right) \Big | _ {(0, 1, - 1)} = (1, - 1, 1).</equation>从而曲面在点（0,1，-1）处的切平面方程为<equation>x - ( y - 1 ) + ( z + 1 ) = 0</equation>，即<equation>x - y + z = - 2</equation>，选A.

---


#### 全微分的概念与计算

**2021年第2题 | 选择题 | 5分 | 答案: C**

2. 设函数 f(x,y)可微，且<equation>f \left( x+1, \mathrm{e}^{x} \right)=x \left( x+1 \right)^{2}, f \left( x, x^{2} \right)=2 x^{2} \ln x</equation>，则<equation>\mathrm{d} f \left( 1, 1 \right)=</equation>(    )

A.<equation>\mathrm{d} x+\mathrm{d} y</equation>B.<equation>\mathrm{d} x-\mathrm{d} y</equation>C.<equation>\mathrm{d} y</equation>D.<equation>-\mathrm{d} y</equation>

答案: C

**解析:**根据全微分的定义，<equation>\mathrm {d} f (1, 1) = f _ {1} ^ {\prime} (1, 1) \mathrm {d} x + f _ {2} ^ {\prime} (1, 1) \mathrm {d} y.</equation>对<equation>f(x + 1,\mathrm{e}^{x}) = x(x + 1)^{2},f(x,x^{2}) = 2x^{2}\ln x</equation>两端均关于<equation>x</equation>求导，可得<equation>f _ {1} ^ {\prime} \left(x + 1, \mathrm {e} ^ {x}\right) + f _ {2} ^ {\prime} \left(x + 1, \mathrm {e} ^ {x}\right) \cdot \mathrm {e} ^ {x} = (x + 1) ^ {2} + x \cdot 2 (x + 1) = (x + 1) (3 x + 1).</equation><equation>f _ {1} ^ {\prime} \left(x, x ^ {2}\right) + f _ {2} ^ {\prime} \left(x, x ^ {2}\right) \cdot 2 x = 4 x \ln x + 2 x ^ {2} \cdot \frac {1}{x} = 2 x \left(2 \ln x + 1\right).</equation>在（1）式中令<equation>x=0</equation>，可得<equation>f_{1}^{\prime}(1,1)+f_{2}^{\prime}(1,1)=1.</equation>在（2）式中令<equation>x=1</equation>，可得<equation>f_{1}^{\prime}(1,1)+ 2 f_{2}^{\prime}(1,1)=2.</equation>联立两式解得<equation>f_{1}^{\prime}(1,1)=0,f_{2}^{\prime}(1,1)=1.</equation>因此，<equation>\mathrm{d}f(1,1)=\mathrm{d}y.</equation>应选C.

---

**2020年第3题 | 选择题 | 4分 | 答案: A**

3. 设函数 f(x,y)在点(0,0)处可微，<equation>f(0,0)=0,\boldsymbol{n}=\left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y},-1\right)\bigg|_{(0,0)},</equation>非零向量<equation>\alpha</equation>与n垂直，则（    )

A.<equation>\lim_{(x,y)\to(0,0)}\frac{\left|\boldsymbol{n}\cdot(x,y,f(x,y))\right|}{\sqrt{x^{2}+y^{2}}}</equation>存在

B.<equation>\lim_{(x,y)\to(0,0)}\frac{\left|\boldsymbol{n}\times(x,y,f(x,y))\right|}{\sqrt{x^{2}+y^{2}}}</equation>存在

C.<equation>\lim_{(x,y)\to(0,0)}\frac{\left|\alpha\cdot(x,y,f(x,y))\right|}{\sqrt{x^{2}+y^{2}}}</equation>存在

D.<equation>\lim_{(x,y)\to(0,0)}\frac{\left|\alpha\times(x,y,f(x,y))\right|}{\sqrt{x^{2}+y^{2}}}</equation>存在

答案: A

**解析:**由函数<equation>f ( x,y )</equation>在点（0，0）处可微，且<equation>f ( 0,0 )=0</equation>可知，<equation>\begin{aligned} 0 &= \lim _ {(x, y) \rightarrow (0, 0)} \frac {f (x , y) - f (0 , 0) - f _ {x} ^ {\prime} (0 , 0) x - f _ {y} ^ {\prime} (0 , 0) y}{\sqrt {x ^ {2} + y ^ {2}}} \\ \underline {{f (0 , 0) = 0}} \lim _ {(x, y) \rightarrow (0, 0)} \frac {f (x , y) - f _ {x} ^ {\prime} (0 , 0) x - f _ {y} ^ {\prime} (0 , 0) y}{\sqrt {x ^ {2} + y ^ {2}}} \\ &= - \lim _ {(x, y) \rightarrow (0, 0)} \frac {f _ {x} ^ {\prime} (0 , 0) x + f _ {y} ^ {\prime} (0 , 0) y - f (x , y)}{\sqrt {x ^ {2} + y ^ {2}}} \\ &= - \lim _ {(x, y) \rightarrow (0, 0)} \frac {\boldsymbol {n} \cdot (x , y , f (x , y))}{\sqrt {x ^ {2} + y ^ {2}}}. \end{aligned}</equation>因此，<equation>\lim_{(x,y)\to (0,0)}\frac{|\boldsymbol{n}\cdot(x,y,f(x,y))|}{\sqrt{x^2 + y^2}} = \lim_{(x,y)\to (0,0)}\frac{\boldsymbol{n}\cdot(x,y,f(x,y))}{\sqrt{x^2 + y^2}} = 0</equation>，应选A.

下面说明其余选项均不正确.<equation>\begin{array}{l} + y k, | n \times (x, y, x) | = \sqrt {4 x ^ {2} + 2 y ^ {2}}. \\ \end{array}</equation><equation>\lim _ {(x, y) \rightarrow (0, 0)} \frac {\left| \boldsymbol {n} \times (x , y , x) \right|}{\sqrt {x ^ {2} + y ^ {2}}} = \lim _ {(x, y) \rightarrow (0, 0)} \frac {\sqrt {4 x ^ {2} + 2 y ^ {2}}}{\sqrt {x ^ {2} + y ^ {2}}} = \lim _ {(x, y) \rightarrow (0, 0)} \sqrt {2 + \frac {2 x ^ {2}}{x ^ {2} + y ^ {2}}}.</equation>取<equation>y=x</equation>与<equation>y=\sqrt{3} x</equation>两条不同路径，可得沿这两条路径所得极限不一样，从而该二重极限不存在.

---

**2016年第11题 | 填空题 | 4分**

11. 设函数 f(u,v) 可微，z=z(x,y) 由方程<equation>( x+1 ) z-y^{2}=x^{2} f ( x-z,y )</equation>确定，则<equation>\mathrm{d} z |_{(0,1)}=</equation>___

**答案:**-<equation>\mathrm{d} x+2 \mathrm{d} y.</equation>

**解析:**解（法一）对已知方程两端分别关于<equation>x,y</equation>求偏导数，可得<equation>z + (x + 1) \frac {\partial z}{\partial x} = 2 x f (x - z, y) + x ^ {2} \left[ f _ {1} ^ {\prime} (x - z, y) \cdot \left(1 - \frac {\partial z}{\partial x}\right) \right].</equation><equation>(x + 1) \frac {\partial z}{\partial y} - 2 y = x ^ {2} \left[ f _ {1} ^ {\prime} (x - z, y) \cdot \left(- \frac {\partial z}{\partial y}\right) + f _ {2} ^ {\prime} (x - z, y) \right].</equation>将<equation>(x,y) = (0,1)</equation>代入已知方程，可得<equation>z - 1 = 0</equation>，从而<equation>z(0,1) = 1.</equation>再将<equation>(x,y,z) = (0,1,1)</equation>代入（1）、（2）两式，可得<equation>\frac{\partial z}{\partial x}\bigg|_{(0,1)} = -1,\frac{\partial z}{\partial y}\bigg|_{(0,1)} = 2.</equation>因此，<equation>\mathrm {d} z \mid_ {(0, 1)} = - \mathrm {d} x + 2 \mathrm {d} y.</equation>（法二）对已知方程两端微分，可得<equation>\mathrm{d}[ ( x + 1 ) z ] - \mathrm{d} ( y^{2} ) = \mathrm{d}[ x^{2} f ( x - z , y ) ]</equation>.进一步可得，<equation>\begin{aligned} (x + 1) \mathrm {d} z + z \mathrm {d} x - 2 y \mathrm {d} y &= f (x - z, y) \mathrm {d} \left(x ^ {2}\right) + x ^ {2} \mathrm {d} \left[ f (x - z, y) \right] \\ &= 2 x f (x - z, y) \mathrm {d} x + x ^ {2} \mathrm {d} \left[ f (x - z, y) \right]. \end{aligned}</equation>将<equation>(x,y) = (0,1)</equation>代入已知方程，可得<equation>z - 1 = 0</equation>，从而<equation>z(0,1) = 1.</equation>代入上式可得<equation>\mathrm {d} z + \mathrm {d} x - 2 \mathrm {d} y = 0,</equation>即<equation>\mathrm{d}z\mid_{(0,1)} = -\mathrm{d}x + 2\mathrm{d}y.</equation>

---

**2015年第11题 | 填空题 | 4分**

11. 若函数<equation>z = z(x,y)</equation>由方程<equation>\mathrm{e}^{z} + xyz + x + \cos x = 2</equation>确定，则<equation>\mathrm{d}z|_{(0,1)} =</equation>___

**解析:**<equation>\mathrm {e} ^ {z} \frac {\partial z}{\partial y} + x z + x y \frac {\partial z}{\partial y} = 0.</equation>将<equation>( x,y)=(0,1)</equation>代入原方程，得到<equation>z ( 0,1 )=0.</equation>再将<equation>( x,y,z)=(0,1,0)</equation>代入方程（1）、（2），得到<equation>\left. \frac{\partial z}{\partial x}\right|_{(0,1)}=-1,\left. \frac{\partial z}{\partial y}\right|_{(0,1)}=0.</equation>于是<equation>\mathrm {d} z \mid_ {(0, 1)} = \frac {\partial z}{\partial x} \Big | _ {(0, 1)} \mathrm {d} x + \frac {\partial z}{\partial y} \Big | _ {(0, 1)} \mathrm {d} y = - \mathrm {d} x.</equation>（法二）对方程<equation>\mathrm{e}^{z}+xyz+x+\cos x=2</equation>两端微分，得到<equation>\mathrm {e} ^ {z} \mathrm {d} z + x y \mathrm {d} z + x z \mathrm {d} y + y z \mathrm {d} x + \mathrm {d} x - \sin x \mathrm {d} x = 0,</equation>整理得<equation>\left(\mathrm {e} ^ {z} + x y\right) \mathrm {d} z = (\sin x - 1 - y z) \mathrm {d} x - x z \mathrm {d} y.</equation>将<equation>(x,y) = (0,1)</equation>代入原方程，得到<equation>z(0,1) = 0</equation>，再代入上式得到<equation>\mathrm{d}z|_{(0,1)} = -\mathrm{d}x.</equation>## （法三）利用隐函数存在定理.

令<equation>F ( x,y,z) = \mathrm{e}^{z}+ x y z+x+\cos x-2.</equation>将（x,y）=（0,1）代入原方程，得到<equation>z ( 0,1 )=0</equation>从而<equation>F ( 0,1,0 )=0.</equation>又<equation>F _ {x} ^ {\prime} (x, y, z) = y z + 1 - \sin x, \quad F _ {y} ^ {\prime} (x, y, z) = x z, \quad F _ {z} ^ {\prime} (0, 1, 0) = \left(\mathrm {e} ^ {z} + x y\right) | _ {(0, 1, 0)} = 1 \neq 0,</equation>故由隐函数存在定理知，<equation>\left. \frac {\partial z}{\partial x} \right| _ {(0, 1)} = - \frac {F _ {x} ^ {\prime} (0 , 1 , 0)}{F _ {z} ^ {\prime} (0 , 1 , 0)} = - 1, \quad \left. \frac {\partial z}{\partial y} \right| _ {(0, 1)} = - \frac {F _ {y} ^ {\prime} (0 , 1 , 0)}{F _ {z} ^ {\prime} (0 , 1 , 0)} = 0,</equation>从而<equation>\mathrm{d}z\mid_{(0,1)} = \frac{\partial z}{\partial x}\bigg|_{(0,1)}\mathrm{d}x + \frac{\partial z}{\partial y}\bigg|_{(0,1)}\mathrm{d}y = -\mathrm{d}x.</equation>解（法一）对方程<equation>\mathrm{e}^{z}+xyz+x+\cos x=2</equation>两端分别关于 x,y求偏导数，得到<equation>\mathrm {e} ^ {z} \frac {\partial z}{\partial x} + y z + x y \frac {\partial z}{\partial x} + 1 - \sin x = 0,</equation>

---

**2012年第3题 | 选择题 | 4分 | 答案: B**

3. 如果函数 f(x,y)在点(0,0)处连续，那么下列命题正确的是（    )

A. 若极限<equation>\lim_{x\rightarrow 0}\frac{f(x,y)}{|x|+|y|}</equation>存在，则 f(x,y)在点(0,0)处可微

B. 若极限<equation>\lim_{x\rightarrow 0}\frac{f(x,y)}{x^{2}+y^{2}}</equation>存在，则 f(x,y)在点(0,0)处可微

C. 若 f(x,y)在点(0,0)处可微，则极限<equation>\lim_{x\rightarrow 0}\frac{f(x,y)}{|x|+|y|}</equation>存在

D. 若 f(x,y)在点(0,0)处可微，则极限<equation>\lim_{x\rightarrow 0}\frac{f(x,y)}{x^{2}+y^{2}}</equation>存在

答案: B

**解析:**解 对于选项A，取<equation>f ( x,y)=| x |+| y |</equation>，则<equation>f ( x,y)</equation>在点（0,0）处连续，且<equation>\lim_{x\to 0}\frac{f(x,y)}{|x|+|y|}=1</equation>但<equation>f ( x,y)</equation>在点（0,0）处的偏导数都不存在，故<equation>f ( x,y)</equation>在点（0,0）处不可微，从而选项A不正确.

对于选项C、D，取<equation>f ( x,y)\equiv 1</equation>，可知选项C、D不正确.

由排除法选B.下面证明选项B.

设<equation>\lim_{x\to 0}\frac{f(x,y)}{x^2 + y^2} = a</equation>，由于<equation>f(x,y)</equation>在（0,0）处连续，故<equation>f (0, 0) = \lim _ {\substack {x \rightarrow 0 \\ y \rightarrow 0}} f (x, y) = \lim _ {\substack {x \rightarrow 0 \\ y \rightarrow 0}} \left[ \frac {f (x , y)}{x ^ {2} + y ^ {2}} \cdot \left(x ^ {2} + y ^ {2}\right)\right] = a \cdot 0 = 0,</equation>从而<equation>\lim _ {\Delta x \rightarrow 0 \atop \Delta y \rightarrow 0} \frac {f (\Delta x , \Delta y) - f (0 , 0)}{\sqrt {(\Delta x) ^ {2} + (\Delta y) ^ {2}}} = \lim _ {\Delta x \rightarrow 0 \atop \Delta y \rightarrow 0} \left[ \frac {f (\Delta x , \Delta y)}{(\Delta x) ^ {2} + (\Delta y) ^ {2}} \cdot \sqrt {(\Delta x) ^ {2} + (\Delta y) ^ {2}} \right] = a \lim _ {\Delta x \rightarrow 0 \atop \Delta y \rightarrow 0} \sqrt {(\Delta x) ^ {2} + (\Delta y) ^ {2}} = 0,</equation>即有<equation>f \left(\Delta x, \Delta y\right) - f (0, 0) = 0 \cdot \Delta x + 0 \cdot \Delta y + o \left(\sqrt {\left(\Delta x\right) ^ {2} + \left(\Delta y\right) ^ {2}}\right).</equation>由可微的定义知，<equation>f(x,y)</equation>在点（0,0）处可微.

---


### 一元函数积分学


#### 定积分的计算

**2025年第17题 | 解答题 | 10分**
17. 计算<equation>\int_ {0} ^ {1} \frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} \mathrm {d} x.</equation>
**答案: **#<equation>\frac{3\ln 2+\pi}{10}.</equation>
**解析: **解设<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {A}{x + 1} + \frac {B x + C}{x ^ {2} - 2 x + 2}.</equation>通分并整理可得，<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {(A + B) x ^ {2} + (B + C - 2 A) x + 2 A + C}{(x + 1) \left(x ^ {2} - 2 x + 2\right)}.</equation>比较<equation>x^{2}, x</equation>的系数以及常数项可得，<equation>A + B = 0,</equation><equation>\left\{B + C - 2 A = 0, \right.</equation><equation>2 A + C = 1.</equation>由（1）式可得 B=-A.将 B=-A 代入（2）式可得 C=3A.将 C=3A 代入（3）式可得 5A=1，即<equation>A=\frac{1}{5}.</equation>进一步可得 B=-<equation>\frac{1}{5},</equation>C<equation>=\frac{3}{5}.</equation>由此可得，<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {1}{5} \left(\frac {1}{x + 1} - \frac {x - 3}{x ^ {2} - 2 x + 2}\right).</equation>下面分别计算<equation>\int_{0}^{1}\frac{1}{x+1}\mathrm{d}x</equation>与<equation>\int_{0}^{1}\frac{x-3}{x^{2}-2x+2}\mathrm{d}x.</equation><equation>\int_ {0} ^ {1} \frac {1}{x + 1} \mathrm {d} x = \ln (x + 1) \Big | _ {0} ^ {1} = \ln 2.</equation><equation>\begin{aligned} \int_ {0} ^ {1} \frac {x - 3}{x ^ {2} - 2 x + 2} \mathrm {d} x &= \int_ {0} ^ {1} \frac {x - 1}{x ^ {2} - 2 x + 2} \mathrm {d} x - \int_ {0} ^ {1} \frac {2}{x ^ {2} - 2 x + 2} \mathrm {d} x \\ &= \frac {1}{2} \int_ {0} ^ {1} \frac {\mathrm {d} \left(x ^ {2} - 2 x + 2\right)}{x ^ {2} - 2 x + 2} - 2 \int_ {0} ^ {1} \frac {1}{1 + (x - 1) ^ {2}} \mathrm {d} x \\ &= \frac {1}{2} \ln \left(x ^ {2} - 2 x + 2\right) \left| _ {0} ^ {1} - 2 \arctan (x - 1) \right| _ {0} ^ {1} \\ &= - \frac {1}{2} \ln 2 - 2 [ 0 - \arctan (- 1) ] = - \frac {1}{2} \ln 2 - \frac {\pi}{2}. \end{aligned}</equation>因此，<equation>\int_ {0} ^ {1} \frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} \mathrm {d} x = \frac {1}{5} \left[ \ln 2 - \left(- \frac {1}{2} \ln 2 - \frac {\pi}{2}\right) \right] = \frac {3 \ln 2 + \pi}{1 0}.</equation>

---

**2023年第14题 | 填空题 | 5分**
14. 设连续函数 f(x)满足<equation>f(x+2)-f(x)=x,\int_{0}^{2} f(x)\mathrm{d} x=0</equation>，则<equation>\int_{1}^{3} f(x)\mathrm{d} x=</equation>___
**解析: **解注意到<equation>\int_{2}^{3} f(x)\mathrm{d}x=\int_{0}^{1} f(x+2)\mathrm{d}x</equation>，故由<equation>f(x+2)-f(x)=x</equation>可得，<equation>\int_{2}^{3} f(x)\mathrm{d}x-\int_{0}^{1} f(x)\mathrm{d}x=\int_{0}^{1} f(x+2)\mathrm{d}x-\int_{0}^{1} f(x)\mathrm{d}x=\int_{0}^{1} x\mathrm{d}x=\frac{1}{2}.</equation>(1)

又因为<equation>\int_{0}^{1} f(x)\mathrm{d}x+\int_{1}^{2} f(x)\mathrm{d}x=\int_{0}^{2} f(x)\mathrm{d}x=0</equation>，所以<equation>-\int_{0}^{1} f(x)\mathrm{d}x=\int_{1}^{2} f(x)\mathrm{d}x.</equation>从而由（1）式可得<equation>\int_{2}^{3} f(x)\mathrm{d}x+\int_{1}^{2} f(x)\mathrm{d}x=\frac{1}{2},</equation>即<equation>\int_{1}^{3} f(x)\mathrm{d}x=\frac{1}{2}.</equation>

---

**2022年第12题 | 填空题 | 5分**
<equation>1 2. \int_ {1} ^ {\mathrm {e} ^ {2}} \frac {\ln x}{\sqrt {x}} \mathrm {d} x = \underline {{}}</equation>
**解析: **解（法一）利用根式代换.

令<equation>t = \sqrt{x}</equation>，则<equation>x = t^{2}</equation>，<equation>\mathrm{d}x = 2t\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {1} ^ {e ^ {2}} \frac {\ln x}{\sqrt {x}} \mathrm {d} x \xlongequal {t = \sqrt {x}} \int_ {1} ^ {e} \frac {2 \ln t}{t} \cdot 2 t \mathrm {d} t &= 4 \int_ {1} ^ {e} \ln t \mathrm {d} t = 4 \left(t \ln t \Big | _ {1} ^ {e} - \int_ {1} ^ {e} t \cdot \frac {1}{t} \mathrm {d} t\right) \\ &= 4 \left[ \mathrm {e} - (\mathrm {e} - 1) \right] = 4. \end{aligned}</equation>（法二）利用分部积分法.<equation>\begin{aligned} \int_ {1} ^ {\mathrm {e} ^ {2}} \frac {\ln x}{\sqrt {x}} \mathrm {d} x &= 2 \int_ {1} ^ {\mathrm {e} ^ {2}} \ln x \mathrm {d} (\sqrt {x}) = 2 \left(\sqrt {x} \ln x \Big | _ {1} ^ {\mathrm {e} ^ {2}} - \int_ {1} ^ {\mathrm {e} ^ {2}} \sqrt {x} \cdot \frac {1}{x} \mathrm {d} x\right) = 2 \left(2 \mathrm {e} - \int_ {1} ^ {\mathrm {e} ^ {2}} \frac {1}{\sqrt {x}} \mathrm {d} x\right) \\ &= 4 \mathrm {e} - 4 \sqrt {x} \Big | _ {1} ^ {\mathrm {e} ^ {2}} = 4 \mathrm {e} - (4 \mathrm {e} - 4) = 4. \end{aligned}</equation>

---

**2015年第10题 | 填空题 | 4分**
10.<equation>\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \left(\frac {\sin x}{1 + \cos x} + | x |\right) \mathrm {d} x = \underline {{}}</equation>
**解析: **由于<equation>\frac{\sin x}{1 + \cos x}</equation>是奇函数，<equation>|x|</equation>是偶函数，故<equation>\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {\sin x}{1 + \cos x} \mathrm {d} x = 0, \quad \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} | x | \mathrm {d} x = 2 \int_ {0} ^ {\frac {\pi}{2}} x \mathrm {d} x = \frac {\pi^ {2}}{4}.</equation>因此，<equation>\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \left(\frac {\sin x}{1 + \cos x} + | x |\right) \mathrm {d} x = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {\sin x}{1 + \cos x} \mathrm {d} x + \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} | x | \mathrm {d} x = 0 + \frac {\pi^ {2}}{4} = \frac {\pi^ {2}}{4}.</equation>

---

**2014年第4题 | 选择题 | 4分 | 答案: A**
4. 若<equation>\int_{-\pi}^{\pi} \left(x-a_{1}\cos x-b_{1}\sin x\right)^{2}\mathrm{d}x=\min_{a,b\in\mathbf{R}}\left\{\int_{-\pi}^{\pi}\left(x-a\cos x-b\sin x\right)^{2}\mathrm{d}x\right\}</equation>，则<equation>a_{1}\cos x+b_{1}\sin x=</equation>(    )

A. 2sinx B. 2cosx C. 2<equation>\pi\sin x</equation>D. 2<equation>\pi\cos x</equation>
答案: A
**解析: **解（法一）<equation>\begin{aligned} \int_ {- \pi} ^ {\pi} \left(x - a \cos x - b \sin x\right) ^ {2} \mathrm {d} x &= \int_ {- \pi} ^ {\pi} \left(x ^ {2} + a ^ {2} \cos^ {2} x + b ^ {2} \sin^ {2} x - 2 a x \cos x - 2 b x \sin x + 2 a b \sin x \cos x\right) \mathrm {d} x \\ \xlongequal {\text {对称性}} 2 \int_ {0} ^ {\pi} x ^ {2} \mathrm {d} x + 2 \int_ {0} ^ {\pi} \left(a ^ {2} \cos^ {2} x + b ^ {2} \sin^ {2} x - 2 b x \sin x\right) \mathrm {d} x \\ &= \frac {2}{3} \pi^ {3} + \left(a ^ {2} + b ^ {2} - 4 b\right) \pi . \end{aligned}</equation>当 a=0时，<equation>a^{2}</equation>最小；当 b=2时，<equation>b^{2}-4b</equation>最小，从而当 a=0，b=2时，<equation>\int_{- \pi}^{\pi} \left(x-a\cos x-b\sin x\right)^{2}\mathrm{d}x</equation>最小.因此<equation>a_{1}=0,b_{1}=2</equation>，从而<equation>a_{1}\cos x+b_{1}\sin x=2\sin x</equation>，应选A.

（法二）看作二元函数的最值问题求解.

令<equation>f ( a,b)=\int_{-\pi}^{\pi} \left(x-a\cos x-b\sin x\right)^{2}\mathrm{d}x</equation>，则<equation>\frac {\partial f (a , b)}{\partial a} = \int_ {- \pi} ^ {\pi} \left[ - 2 (x - a \cos x - b \sin x) \cos x \right] \mathrm {d} x = 2 a \int_ {- \pi} ^ {\pi} \cos^ {2} x \mathrm {d} x = 2 a \pi ,</equation><equation>\frac {\partial f (a , b)}{\partial b} = \int_ {- \pi} ^ {\pi} \left[ - 2 \left(x - a \cos x - b \sin x\right) \sin x \right] \mathrm {d} x = 2 \int_ {- \pi} ^ {\pi} \left(b \sin^ {2} x - x \sin x\right) \mathrm {d} x = 2 \left(b \pi - 2 \pi\right).</equation>令<equation>\frac{\partial f(a,b)}{\partial a} = 0,\frac{\partial f(a,b)}{\partial b} = 0</equation>，解得<equation>a = 0,b = 2</equation>，从而<equation>a_1 = 0,b_1 = 2</equation>.应选A.

（法三）将选项A、B、C、D的值分别代入<equation>\int_{-\pi}^{\pi} \left(x-a\cos x-b\sin x\right)^{2}\mathrm{d}x</equation>，得到<equation>\int_ {- \pi} ^ {\pi} (x - 2 \sin x) ^ {2} \mathrm {d} x = \frac {2}{3} \pi^ {3} - 4 \pi ,</equation><equation>\int_ {- \pi} ^ {\pi} \left(x - 2 \cos x\right) ^ {2} \mathrm {d} x = \frac {2}{3} \pi^ {3} + 4 \pi ,</equation><equation>\int_ {- \pi} ^ {\pi} \left(x - 2 \pi \sin x\right) ^ {2} \mathrm {d} x = \frac {2}{3} \pi^ {3} + 4 \pi^ {2} (\pi - 2),</equation><equation>\int_ {- \pi} ^ {\pi} \left(x - 2 \pi \cos x\right) ^ {2} \mathrm {d} x = \frac {2}{3} \pi^ {3} + 4 \pi^ {3}.</equation>由于<equation>\frac{2}{3}\pi^{3}-4\pi<\frac{2}{3}\pi^{3}+4\pi<\frac{2}{3}\pi^{3}+4\pi^{2}(\pi-2)<\frac{2}{3}\pi^{3}+4\pi^{3}</equation>，故选A.

---

**2014年第10题 | 填空题 | 4分**
10. 设<equation>f(x)</equation>是周期为4的可导奇函数,且<equation>f^{\prime}(x)=2(x-1),x\in[0,2]</equation>,则<equation>f(7)=</equation>___.
**解析: **由于<equation>f ( x )</equation>是周期为4的函数，且<equation>7=2\times4-1</equation>，故<equation>f ( 7 ) = f (-1).</equation>(a)

(b)

（法一）由 f(x)为奇函数可得<equation>f(0)=0</equation>.由当<equation>x\in[0,2]</equation>时，<equation>f^{\prime}(x)=2(x-1)</equation>可得， f(x)在 [0,2]上的表达式为<equation>f (x) = \int_ {0} ^ {x} 2 (t - 1) \mathrm {d} t + f (0) = x ^ {2} - 2 x = (x - 1) ^ {2} - 1.</equation>于是<equation>f(1) = -1.</equation>由<equation>f(x)</equation>为奇函数得，<equation>f(-1) = -f(1) = 1</equation>，即<equation>f(7) = 1.</equation>（法二）由 f(x)为奇函数可知，<equation>f(x)=-f(-x).</equation>在等式两端求导得<equation>f^{\prime}(x)=f^{\prime}(-x),</equation>从而<equation>f^{\prime}(x)</equation>为偶函数，<equation>f^{\prime}(x)</equation>的图像关于y轴对称.在[0，2]上，<equation>f^{\prime}(x)=2(x-1),</equation>为一条过点（0，-2）和点（1，0）的直线。由此可知，在[-2，0]上，<equation>y=f^{\prime}(x)</equation>为过点（0，-2）和点（-1，0）的直线，可求得<equation>f^{\prime}(x)=-2(x+1).</equation>从而，<equation>f(x)</equation>在[-2，0]上为<equation>f (x) = \int_ {0} ^ {x} - 2 (t + 1) \mathrm {d} t + f (0) = - x ^ {2} - 2 x = - (x + 1) ^ {2} + 1.</equation>因此，<equation>f(-1)=1</equation>，即<equation>f(7)=1.</equation>

---

**2013年第15题 | 解答题 | 10分**
15. (本题满分10分)

计算<equation>\int_ {0} ^ {1} \frac {f (x)}{\sqrt {x}} \mathrm {d} x, \text {其 中} f (x) = \int_ {1} ^ {x} \frac {\ln (t + 1)}{t} \mathrm {d} t.</equation>
**解析: **解（法一）由题设知，<equation>f^{\prime}(x) = \frac{\ln(x + 1)}{x}, x\in(0,1],</equation>且<equation>f(1)=0</equation>，于是<equation>\begin{aligned} \int_ {0} ^ {1} \frac {f (x)}{\sqrt {x}} \mathrm {d} x &= 2 \int_ {0} ^ {1} f (x) \mathrm {d} (\sqrt {x}) = 2 \left[ \sqrt {x} f (x) \left| _ {0} ^ {1} - \int_ {0} ^ {1} \sqrt {x} f ^ {\prime} (x) \mathrm {d} x \right] \right. \\ &= 0 - 2 \int_ {0} ^ {1} \sqrt {x} \cdot \frac {\ln (x + 1)}{x} \mathrm {d} x = - 2 \int_ {0} ^ {1} \frac {\ln (x + 1)}{\sqrt {x}} \mathrm {d} x \\ &= - 4 \int_ {0} ^ {1} \ln (x + 1) \mathrm {d} (\sqrt {x}) \\ &= - 4 \left[ \sqrt {x} \ln (x + 1) \left| _ {0} ^ {1} - \int_ {0} ^ {1} \frac {\sqrt {x}}{x + 1} \mathrm {d} x \right] \right. \\ \underline {{= - 4}} \left[ \sqrt {x} \ln (x + 1) \left| _ {0} ^ {1} - \int_ {0} ^ {1} \frac {\sqrt {x}}{x + 1} \mathrm {d} x \right] \right. \\ &= - 4 \ln 2 + 4 \int_ {0} ^ {1} \frac {t}{t ^ {2} + 1} \cdot 2 t \mathrm {d} t \\ &= - 4 \ln 2 + 8 \int_ {0} ^ {1} \left(1 - \frac {1}{t ^ {2} + 1}\right) \mathrm {d} t \\ &= - 4 \ln 2 + 8 \left(t - \arctan t\right) \Bigg | _ {0} ^ {1} \\ &= - 4 \ln 2 + 8 - 2 \pi . \end{aligned}</equation><equation>\begin{array}{l} \frac {\text {交换 积 分}}{\text {次 序}} - \int_ {0} ^ {1} \mathrm {d} t \int_ {0} ^ {t} \frac {\ln (t + 1)}{t} \cdot \frac {1}{\sqrt {x}} \mathrm {d} x = - 2 \int_ {0} ^ {1} \frac {\ln (t + 1)}{\sqrt {t}} \mathrm {d} t \\ \underline {{\text {同 法 一}}} - 4 \ln 2 + 8 - 2 \pi . \\ \end{array}</equation>

---

**2012年第10题 | 填空题 | 4分**
<equation>1 0. \int_ {0} ^ {2} x \sqrt {2 x - x ^ {2}} \mathrm {d} x = \underline {{}}</equation>
**解析: **解<equation>\sqrt{2 x-x^{2}}=\sqrt{1-(x-1)^{2}}.</equation>令 t=x-1，则有<equation>\begin{aligned} \int_ {0} ^ {2} x \sqrt {2 x - x ^ {2}} \mathrm {d} x &= \int_ {- 1} ^ {1} (t + 1) \sqrt {1 - t ^ {2}} \mathrm {d} t = \int_ {- 1} ^ {1} t \sqrt {1 - t ^ {2}} \mathrm {d} t + \int_ {- 1} ^ {1} \sqrt {1 - t ^ {2}} \mathrm {d} t \\ \underline {{\text {对称性}}} 0 + 2 \int_ {0} ^ {1} \sqrt {1 - t ^ {2}} \mathrm {d} t \\ \underline {{\underline {{t = \sin \theta}}}} 2 \int_ {0} ^ {\frac {\pi}{2}} \cos^ {2} \theta \mathrm {d} \theta &= \int_ {0} ^ {\frac {\pi}{2}} (1 + \cos 2 \theta) \mathrm {d} \theta = \frac {\pi}{2}. \end{aligned}</equation>

---

**2010年第10题 | 填空题 | 4分**
10.
**解析: **<equation>\begin{aligned} \int_ {0} ^ {\pi^ {2}} \sqrt {x} \cos \sqrt {x} \mathrm {d} x \stackrel {t = \sqrt {x}} {=} \int_ {0} ^ {\pi} t \cos t \mathrm {d} \left(t ^ {2}\right) \\ &= \int_ {0} ^ {\pi} 2 t ^ {2} \cos t \mathrm {d} t = \int_ {0} ^ {\pi} 2 t ^ {2} \mathrm {d} (\sin t) \\ \underline {{\mathrm {分 部 积 分}}} (\sin t \cdot 2 t ^ {2}) \left| _ {0} ^ {\pi} - \int_ {0} ^ {\pi} 4 t \sin t \mathrm {d} t &= \int_ {0} ^ {\pi} 4 t \mathrm {d} (\cos t) \right. \\ \underline {{\mathrm {分 部 积 分}}} (\cos t \cdot 4 t) \left| _ {0} ^ {\pi} - \int_ {0} ^ {\pi} 4 \cos t \mathrm {d} t &= - 4 \pi . \right. \end{aligned}</equation>

---


#### 变限积分

**2024年第1题 | 选择题 | 5分 | 答案: C**
1. 已知函数<equation>f ( x )=\int_{0}^{x} \mathrm{e}^{\cos t} \mathrm{d} t,g ( x )=\int_{0}^{\sin x} \mathrm{e}^{t^{2}} \mathrm{d} t</equation>，则（    )

A. f(x)是奇函数，g(x)是偶函数 B. f(x)是偶函数，g(x)是奇函数

C. f(x)与 g(x)均为奇函数 D. f(x)与 g(x)均为周期函数
答案: C
**解析: **解 由于<equation>\mathrm{e}^{\cos t}</equation>是偶函数，且<equation>f(0)=0</equation>，故由分析中的结论可得<equation>f(x)=\int_{0}^{x}\mathrm{e}^{\cos t}\mathrm{d}t</equation>是奇函数.同理，<equation>h(x)=\int_{0}^{x}\mathrm{e}^{t^{2}}\mathrm{d}t</equation>也是奇函数.

注意到<equation>g ( x )=h (\sin x)</equation>，故<equation>g (- x) = h (\sin (- x)) = h (- \sin x) = - h (\sin x) = - g (x).</equation>于是，<equation>g ( x )</equation>也是奇函数.

因此，应选C.

下面说明选项 D 不正确.

由于<equation>\sin x</equation>是周期为<equation>2\pi</equation>的周期函数，故<equation>g (x + 2 \pi) = \int_ {0} ^ {\sin (x + 2 \pi)} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = \int_ {0} ^ {\sin x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = g (x).</equation>于是，<equation>g ( x )</equation>也是周期为<equation>2 \pi</equation>的周期函数.但是，由于<equation>f^{\prime}(x)=\mathrm{e}^{\cos x}>0</equation>，故f(x）单调增加，从而f(x)不可能为周期函数.

也可以直接验证<equation>f(-x)=-f(x), g(-x)=-g(x)</equation>，从而得到它们均为奇函数.<equation>f (- x) = \int_ {0} ^ {- x} \mathrm {e} ^ {\cos t} \mathrm {d} t \underline {{= u = - t}} - \int_ {0} ^ {x} \mathrm {e} ^ {\cos (- u)} \mathrm {d} u = - \int_ {0} ^ {x} \mathrm {e} ^ {\cos u} \mathrm {d} u = - f (x),</equation><equation>g (- x) = \int_ {0} ^ {\sin (- x)} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = \int_ {0} ^ {- \sin x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t \xlongequal {u = - t} - \int_ {0} ^ {\sin x} \mathrm {e} ^ {(- u) ^ {2}} \mathrm {d} u = - \int_ {0} ^ {\sin x} \mathrm {e} ^ {u ^ {2}} \mathrm {d} u = - g (x).</equation>

---

**2009年第3题 | 选择题 | 4分 | 答案: D**
3. 设函数 y=f(x)在区间[-1,3]上的图形如图所示，则函数<equation>F ( x )=\int_{0}^{x} f ( t ) \mathrm{d} t</equation>的图形为（    ）

A.

B.

C.

D.
答案: D
**解析: **解（法一）我们可以从<equation>f(x)</equation>出发具体分析<equation>F(x)</equation>的性质.

因为<equation>f ( x )</equation>分段连续，所以由变上限积分函数的性质可知，在<equation>[-1,0)</equation>，（0，2），（2，3]上，均有<equation>F^{\prime}(x)=f(x).</equation><equation>\textcircled{1}</equation>由于 f(x)在[-1,3]上有界且只有两个间断点，故 f(x)可积.又因为<equation>F(x)=\int_{0}^{x} f(t)\mathrm{d}t</equation>所以 F(x)连续.<equation>\textcircled{2}</equation>在[-1,0）上，<equation>f ( x ) > 0</equation>，故 F(x)单调增加；在（0，1）上，<equation>f ( x ) < 0</equation>，故 F(x)单调减少；在（1，2）上，<equation>f ( x ) > 0</equation>，故 F(x)单调增加；在（2，3]上，<equation>f ( x ) = 0</equation>，故 F(x)为常函数.<equation>\textcircled{3} F ( 0 )=\int_{0}^{0} f ( t ) \mathrm{d} t=0.</equation>在<equation>[-1,1]</equation>上，<equation>F ( x )</equation>均小于等于零.<equation>\textcircled{4}</equation><equation>f(1) = 0, x = 1</equation>为<equation>F(x)</equation>的驻点及极小值点.

同时满足以上要求的图形只有选项D. 应选D.

（法二）通过图形考察<equation>f(x)</equation>在<equation>[-1,0)</equation>上的性质，可知当<equation>x\in[-1,0)</equation>时，<equation>f(x)\equiv 1</equation>，故<equation>F (- 1) = \int_ {0} ^ {- 1} 1 \mathrm {d} x = - 1, \quad F (0) = \int_ {0} ^ {0} 1 \mathrm {d} x = 0,</equation>从而可排除选项A和选项C.

又由于 f(x)在[-1，3]上有界且只有两个间断点，f(x)在[-1，3]上可积，而 F(x) =<equation>\int_{0}^{x} f(t)\mathrm{d}t</equation>，故 F(x)必连续，从而可以排除选项B.

综上所述，应选D.

---


#### 定积分的概念、性质及几何意义

**2022年第4题 | 选择题 | 5分 | 答案: A**

4. 若<equation>I_{1}=\int_{0}^{1}\frac{x}{2(1+\cos x)}\mathrm{d}x,I_{2}=\int_{0}^{1}\frac{\ln(1+x)}{1+\cos x}\mathrm{d}x,I_{3}=\int_{0}^{1}\frac{2x}{1+\sin x}\mathrm{d}x</equation>，则（    )

A.<equation>I_{1}<I_{2}<I_{3}</equation>B.<equation>I_{2}<I_{1}<I_{3}</equation>C.<equation>I_{1}<I_{3}<I_{2}</equation>D.<equation>I_{3}<I_{2}<I_{1}</equation>

答案: A

**解析:**解 通过观察可发现，要比较<equation>I_{1}</equation>与<equation>I_{2}</equation>的大小，只需比较<equation>\frac{x}{2}</equation>与<equation>\ln(1+x)</equation>的大小.

令<equation>f(x)=\ln(1+x)-\frac{x}{2}</equation>，则<equation>f(0)=0</equation><equation>f^{\prime}(x)=\frac{1}{1+x}-\frac{1}{2}</equation>当<equation>x\in(0,1)</equation>时，<equation>f^{\prime}(x)>0</equation><equation>f(x)</equation>单调增加，从而<equation>f(x)>f(0)=0</equation>即<equation>\ln(1+x)>\frac{x}{2},\frac{\ln(1+x)}{1+\cos x}>\frac{x}{2(1+\cos x)}</equation>因此，<equation>I_{2}>I_{1}</equation>.

此外，同样的方法不难证明在(0,1)内，<equation>\ln(1+x)<x.</equation>另一方面，由于在(0,1)内，<equation>0<\sin x,\cos x<1,1<1+\sin x<2</equation>故<equation>I_{3}</equation>的被积函数<equation>\frac{2x}{1+\sin x} > x.</equation>结合<equation>\ln(1+x)<x</equation>可得，<equation>\frac{\ln(1+x)}{1+\cos x}<\frac{x}{1+\cos x}<x.</equation>于是，<equation>\frac{2x}{1+\sin x}>x>\frac{\ln(1+x)}{1+\cos x}.</equation>因此，<equation>I_{3}>I_{2}.</equation>综上所述，应选A.

---

**2021年第4题 | 选择题 | 5分 | 答案: B**

4. 设函数 f(x)在区间[0,1]上连续，则<equation>\int_{0}^{1} f(x)\mathrm{d}x=</equation>(    )

A.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{n}f\left(\frac{2k-1}{2n}\right)\frac{1}{2n}</equation>B.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{n}f\left(\frac{2k-1}{2n}\right)\frac{1}{n}</equation>C.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{2n}f\left(\frac{k-1}{2n}\right)\frac{1}{n}</equation>D.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{2n}f\left(\frac{k}{2n}\right)\frac{2}{n}</equation>

答案: B

**解析:**解 由于 f(x)连续，故<equation>\int_{0}^{1} f(x)\mathrm{d}x</equation>存在，从而可对区间[0，1]进行划分，将该积分写为 n项和式的极限.

将[0，1]分为n等份，每个小区间为<equation>\left[ \frac{k-1}{n},\frac{k}{n}\right]</equation><equation>k=1,2,\dots,n</equation>从<equation>\left[ \frac{k-1}{n},\frac{k}{n}\right]</equation>中取点<equation>\frac{2k-1}{2n}</equation>故由<equation>\int_{0}^{1} f(x)\mathrm{d}x</equation>存在以及定积分的定义可得<equation>\int_ {0} ^ {1} f (x) \mathrm {d} x = \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} f \left(\frac {2 k - 1}{2 n}\right) \cdot \frac {1}{n}.</equation>因此，应选B.

下面说明选项A、C、D均不正确.

选项A：<equation>\lim_{n\to \infty}\sum_{k = 1}^{n}f\left(\frac{2k - 1}{2n}\right)\frac{1}{2n} = \frac{1}{2}\lim_{n\to \infty}\sum_{k = 1}^{n}f\left(\frac{2k - 1}{2n}\right)\frac{1}{n} = \frac{1}{2}\int_{0}^{1}f(x)\mathrm{d}x.</equation>选项C：<equation>\lim_{n\to \infty}\sum_{k = 1}^{2n}f\left(\frac{k - 1}{2n}\right)\frac{1}{n} = 2\lim_{n\to \infty}\sum_{k = 1}^{2n}f\left(\frac{k - 1}{2n}\right)\frac{1}{2n} = 2\int_{0}^{1}f(x)\mathrm{d}x.</equation>选项D：<equation>\lim_{n\to \infty}\sum_{k = 1}^{2n}f\left(\frac{k}{2n}\right)\frac{2}{n} = 4\lim_{n\to \infty}\sum_{k = 1}^{2n}f\left(\frac{k}{2n}\right)\frac{1}{2n} = 4\int_{0}^{1}f(x)\mathrm{d}x.</equation>

---

**2018年第4题 | 选择题 | 4分 | 答案: C**

4. 设<equation>M=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{(1+x)^{2}}{1+x^{2}}\mathrm{d}x</equation>，<equation>N=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{1+x}{\mathrm{e}^{x}}\mathrm{d}x</equation>，<equation>K=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}(1+\sqrt{\cos x})\mathrm{d}x</equation>，则（    )

A.<equation>M>N>K</equation>B.<equation>M>K>N</equation>C.<equation>K>M>N</equation>D.<equation>K>N>M</equation>

答案: C

**解析:**解分别计算 M,N,K.

由于<equation>\frac{2x}{1 + x^2}</equation>是奇函数，故<equation>\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{2x}{1 + x^2}\mathrm{d}x = 0.</equation>于是，<equation>M = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {(1 + x) ^ {2}}{1 + x ^ {2}} \mathrm {d} x = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {1 + x ^ {2} + 2 x}{1 + x ^ {2}} \mathrm {d} x \xlongequal {\frac {\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {2 x}{1 + x ^ {2}} \mathrm {d} x = 0}{}} \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \mathrm {d} x = \pi .</equation>注意到当<equation>x\neq 0</equation>时，<equation>\mathrm{e}^{x} > 1 + x.</equation>于是，在<equation>\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>上，<equation>\frac{1+x}{\mathrm{e}^{x}}\leqslant 1</equation>且等号仅在<equation>x=0</equation>处成立.<equation>N = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {1 + x}{\mathrm {e} ^ {x}} \mathrm {d} x < \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \mathrm {d} x = \pi .</equation>由于<equation>\sqrt{\cos x}</equation>是偶函数，且当 x<equation>\in\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>时，<equation>\cos x\geqslant0</equation>且等号仅在端点处成立，故<equation>\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\sqrt{\cos x}\mathrm{d}x=2\int_{0}^{\frac{\pi}{2}}\sqrt{\cos x}\mathrm{d}x>0.</equation>于是，<equation>K = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \left(1 + \sqrt {\cos x}\right) \mathrm {d} x = \pi + \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \sqrt {\cos x} \mathrm {d} x > \pi .</equation>综上所述，<equation>K > M > N</equation>应选C.

---

**2017年第16题 | 解答题 | 10分**

16. (本题满分10分)<equation>\text {求} \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n ^ {2}} \ln \left(1 + \frac {k}{n}\right)</equation>

**解析:**解 根据定积分的定义，提出因子<equation>\frac{1}{n}</equation>，可得<equation>\begin{aligned} \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n ^ {2}} \ln \left(1 + \frac {k}{n}\right) &= \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n} \ln \left(1 + \frac {k}{n}\right) \cdot \frac {1}{n} = \int_ {0} ^ {1} x \ln (1 + x) d x \\ &= \frac {1}{2} \int_ {0} ^ {1} \ln (1 + x) d \left(x ^ {2}\right) \xlongequal {\text {分 部 积 分}} \frac {x ^ {2}}{2} \ln (1 + x) \left| _ {0} ^ {1} - \int_ {0} ^ {1} \frac {x ^ {2}}{2 (1 + x)} d x \right. \\ &= \frac {\ln 2}{2} - \frac {1}{2} \int_ {0} ^ {1} \frac {x ^ {2} - 1 + 1}{1 + x} d x = \frac {\ln 2}{2} - \frac {1}{2} \int_ {0} ^ {1} \left(x - 1 + \frac {1}{1 + x}\right) d x \\ &= \frac {\ln 2}{2} - \frac {1}{2} \left[ \frac {x ^ {2}}{2} - x + \ln (1 + x) \right] \Bigg | _ {0} ^ {1} = \frac {1}{4}. \end{aligned}</equation>因此，原极限<equation>= \frac{1}{4}.</equation>

---

**2012年第4题 | 选择题 | 4分 | 答案: D**

4. 设<equation>I_{k}=\int_{0}^{k\pi}\mathrm{e}^{x^{2}}\sin x\mathrm{d}x(k=1,2,3)</equation>，则有（    ）

A.<equation>I_{1}<I_{2}<I_{3}</equation>B.<equation>I_{3}<I_{2}<I_{1}</equation>C.<equation>I_{2}<I_{3}<I_{1}</equation>D.<equation>I_{2}<I_{1}<I_{3}</equation>

答案: D

**解析:**解（法一）记<equation>J_{k}=\int_{(k-1)\pi}^{k\pi}\mathrm{e}^{x^{2}}\sin x\mathrm{d}x(k=1,2,3)</equation>，则<equation>I _ {1} = J _ {1}, \quad I _ {2} = J _ {1} + J _ {2}, \quad I _ {3} = J _ {1} + J _ {2} + J _ {3}.</equation>由于<equation>\mathrm{e}^{x^{2}} > 0</equation>，且在（0，<equation>\pi</equation>）上，<equation>\sin x > 0</equation>；在（<equation>\pi,2\pi</equation>）上，<equation>\sin x < 0</equation>；在（<equation>2\pi,3\pi</equation>）上，<equation>\sin x > 0</equation>，故<equation>J_{1}>0</equation>，<equation>J_{2}<0</equation>，<equation>J_{3}>0</equation>.由此可得，<equation>I_{1}>I_{2}</equation>，<equation>I_{3}>I_{2}</equation>.

下面比较<equation>I_{1}</equation>和<equation>I_{3}.</equation><equation>I _ {3} - I _ {1} = J _ {2} + J _ {3}.</equation><equation>J _ {3} = \int_ {2 \pi} ^ {3 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x > \mathrm {e} ^ {(2 \pi) ^ {2}} \int_ {2 \pi} ^ {3 \pi} \sin x \mathrm {d} x,</equation><equation>\left| J _ {2} \right| = \left| \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x \right| < \mathrm {e} ^ {(2 \pi) ^ {2}} \left| \int_ {\pi} ^ {2 \pi} \sin x \mathrm {d} x \right|, \quad J _ {2} > - \mathrm {e} ^ {(2 \pi) ^ {2}} \left| \int_ {\pi} ^ {2 \pi} \sin x \mathrm {d} x \right|.</equation>由定积分的几何意义可知，<equation>\int_{2\pi}^{3\pi}\sin x\mathrm{d}x</equation>和<equation>|\int_{\pi}^{2\pi}\sin x\mathrm{d}x|</equation>分别为<equation>\sin x</equation>在<equation>(2\pi ,3\pi)</equation>上以及在<equation>(\pi ,2\pi)</equation>上的部分与<equation>x</equation>轴围成的图形面积.根据<equation>\sin x</equation>的图形，这两部分面积相等，即<equation>\int_{2\pi}^{3\pi}\sin x\mathrm{d}x = \left|\int_{\pi}^{2\pi}\sin x\mathrm{d}x\right|.</equation>于是，

于是，<equation>J _ {2} + J _ {3} > \mathrm {e} ^ {(2 \pi) ^ {2}} \left(\int_ {2 \pi} ^ {3 \pi} \sin x \mathrm {d} x - \left| \int_ {\pi} ^ {2 \pi} \sin x \mathrm {d} x \right|\right) = 0,</equation>即<equation>I_{3} > I_{1}.</equation>因此，<equation>I_{2} < I_{1} < I_{3}</equation>应选D.

（法二）在法一中，证明<equation>J_{2} + J_{3} > 0</equation>，也可以使用如下方法.<equation>J _ {3} = \int_ {2 \pi} ^ {3 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x \xlongequal {u = x - \pi} \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {(u + \pi) ^ {2}} \sin (u + \pi) \mathrm {d} u = - \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {(u + \pi) ^ {2}} \sin u \mathrm {d} u,</equation><equation>J _ {2} + J _ {3} = \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x - \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {(x + \pi) ^ {2}} \sin x \mathrm {d} x = \int_ {\pi} ^ {2 \pi} \sin x \left[ \mathrm {e} ^ {x ^ {2}} - \mathrm {e} ^ {(x + \pi) ^ {2}} \right] \mathrm {d} x.</equation>当<equation>x\in (\pi ,2\pi)</equation>时，<equation>\sin x < 0,\mathrm{e}^{x^2} - \mathrm{e}^{(x + \pi)^2} < 0,\sin x[\mathrm{e}^{x^2} - \mathrm{e}^{(x + \pi)^2}] > 0</equation>，从而<equation>J_{2} + J_{3} > 0.</equation>其余同法一.

---

**2011年第4题 | 选择题 | 4分 | 答案: B**

4. 设<equation>I=\int_{0}^{\frac{\pi}{4}}\ln(\sin x)\mathrm{d}x, J=\int_{0}^{\frac{\pi}{4}}\ln(\cot x)\mathrm{d}x, K=\int_{0}^{\frac{\pi}{4}}\ln(\cos x)\mathrm{d}x</equation>，则 I,J,K的大小关系为（    )

A. I<J<K B. I<K<J C. J<I<K D. K<J<I

答案: B

**解析:**解 当 0 < x <<equation>\frac{\pi}{4}</equation>时，0 < sin x < cos x < 1 < cot x.又 f(t) = ln t在（0，+<equation>\infty</equation>）上单调增加，故当 0 < x <<equation>\frac{\pi}{4}</equation>时，<equation>\ln(\sin x) < \ln(\cos x) < \ln(\cot x)</equation>，从而由积分的保号性可知， I < K < J ，选B.

---

**2010年第17题 | 解答题 | 10分**

17. (本题满分10分)

17. (本题满分10分)

I. 比较<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>与<equation>\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t</equation>（ n=1,2，<equation>\cdots</equation>）的大小，说明理由；

II. 记<equation>u_{n}=\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>（ n=1,2，<equation>\cdots</equation>），求极限<equation>\lim_{n\to\infty}u_{n}.</equation>

**答案:**(17) （I）<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t<\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t</equation>，理由略；（Ⅱ）<equation>\lim_{n\to\infty}u_{n}=0.</equation>

**解析:**解（I）在（0，1]上，<equation>|\ln t|</equation><equation>\ln(1+t)</equation>与 t均非负，故比较<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>与<equation>\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t(n=1,2,\cdots)</equation>的大小，只需比较<equation>\ln(1+t)</equation>与 t的大小.

考虑 f（t）=<equation>\ln(1+t)-t.</equation><equation>f ^ {\prime} (t) = \frac {1}{1 + t} - 1.</equation>当<equation>t\in (0,1]</equation>时，<equation>f^{\prime}(t) < 0,f(t)\leqslant f(0) = 0.</equation>因此，当<equation>t \in [0,1]</equation>时，<equation>\ln (1 + t) \leqslant t.</equation>由于两被积函数仅在<equation>t = 1</equation>处相等，故<equation>\int_ {0} ^ {1} | \ln t | [ \ln (1 + t) ] ^ {n} \mathrm {d} t < \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t (n = 1, 2, \dots).</equation>（Ⅱ）（法一）由第（I）问知，<equation>0 < u_{n} < \int_{0}^{1} t^{n}|\ln t|\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {0} ^ {1} t ^ {n} \mid \ln t \mid \mathrm {d} t &= \frac {- 1}{n + 1} \int_ {0} ^ {1} \ln t \mathrm {d} \left(t ^ {n + 1}\right) = \frac {- 1}{n + 1} \left(t ^ {n + 1} \ln t \mid_ {0} ^ {1} - \int_ {0} ^ {1} t ^ {n + 1} \cdot \frac {1}{t} \mathrm {d} t\right) \\ \frac {\lim _ {t \rightarrow 0 ^ {+}} t ^ {n + 1} \ln t = 0}{\overline {{\quad}}} \frac {1}{n + 1} \int_ {0} ^ {1} t ^ {n} \mathrm {d} t &= \frac {1}{(n + 1) ^ {2}}. \end{aligned}</equation>因此，<equation>\lim _ {n \rightarrow \infty} \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t = \lim _ {n \rightarrow \infty} \frac {1}{(n + 1) ^ {2}} = 0.</equation>由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>（法二）由第（I）问知，<equation>0 < u_{n} < \int_{0}^{1} t^{n}|\ln t|\mathrm{d}t.</equation>又因为<equation>\lim_{t\to 0^{+}}(t\ln t) = 0</equation>，所以存在<equation>M > 0</equation>，使得对任意的<equation>t\in (0,1]</equation>，有<equation>t|\ln t|\leqslant M</equation>，从而<equation>0 < u _ {n} < \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t \leqslant M \int_ {0} ^ {1} t ^ {n - 1} \mathrm {d} t = \frac {M}{n}.</equation>由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>（法三）由于<equation>t\in[0,1]</equation>时，<equation>\ln(1 + t)\leqslant \ln 2 < 1</equation>，故<equation>u_{n}\leqslant (\ln 2)^{n}\int_{0}^{1}|\ln t|\mathrm{d}t.</equation>计算<equation>\int_{0}^{1}|\ln t| \mathrm{d} t</equation>得，<equation>\int_ {0} ^ {1} | \ln t | \mathrm {d} t = - \int_ {0} ^ {1} \ln t \mathrm {d} t = - \left(t \ln t \left| _ {0} ^ {1} - \int_ {0} ^ {1} 1 \mathrm {d} t\right)\right) \xlongequal {\lim _ {t \rightarrow 0 ^ {+}} t \ln t = 0} 1.</equation>从而<equation>0 < u_{n}\leqslant (\ln 2)^{n}</equation>因为<equation>\lim_{n\to \infty}(\ln 2)^n = 0</equation>，所以由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>

---


#### 反常积分的计算与敛散性

**2021年第11题 | 填空题 | 5分**

<equation>\int_ {0} ^ {+ \infty} \frac {1}{x ^ {2} + 2 x + 2} \mathrm {d} x = \underline {{}}</equation>

**答案:**##<equation>\frac{\pi}{4}</equation>

**解析:**将<equation>x^{2}+2 x+2</equation>配方.<equation>\begin{aligned} \int_ {0} ^ {+ \infty} \frac {\mathrm {d} x}{x ^ {2} + 2 x + 2} &= \int_ {0} ^ {+ \infty} \frac {\mathrm {d} x}{(x + 1) ^ {2} + 1} = \int_ {0} ^ {+ \infty} \frac {\mathrm {d} (x + 1)}{(x + 1) ^ {2} + 1} = \arctan (x + 1) \Big | _ {0} ^ {+ \infty} \\ &= \frac {\pi}{2} - \arctan 1 = \frac {\pi}{2} - \frac {\pi}{4} = \frac {\pi}{4}. \end{aligned}</equation>

---

**2016年第1题 | 选择题 | 4分 | 答案: C**

1. 若反常积分<equation>\int_{0}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x</equation>收敛，则（    )

A. a < 1且b > 1 B. a > 1且b > 1 C. a < 1且a+b > 1 D. a > 1且a+b > 1

答案: C

**解析:**解 由于被积函数<equation>\frac{1}{x^{a}(1+x)^{b}}</equation>在<equation>[0,+\infty)</equation>上可能的瑕点为<equation>x=0</equation>，故将反常积分分为两部分，即<equation>\int_{0}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x=\int_{0}^{1}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x+\int_{1}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x.</equation>对于积分<equation>\int_{0}^{1}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x</equation>，若<equation>a\leqslant0</equation>，则该积分为正常的定积分；若<equation>a>0</equation>，则<equation>x=0</equation>为被积函数的瑕点.

由于<equation>\lim_{x\rightarrow 0^{+}}\frac{\frac{1}{x^{a}(1+x)^{b}}}{\frac{1}{x^{a}}}=\lim_{x\rightarrow 0^{+}}\frac{1}{(1+x)^{b}}=1</equation>，故当<equation>x\rightarrow 0^{+}</equation>时，<equation>\frac{1}{x^{a}(1+x)^{b}}</equation>与<equation>\frac{1}{x^{a}}</equation>等价. 瑕积分<equation>\int_{0}^{1}\frac{1}{x^{a}}\mathrm{d}x</equation>当且仅当<equation>0<a<1</equation>时收敛，加上<equation>a\leqslant0</equation>时的情况，<equation>\int_{0}^{1}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x</equation>当且仅当<equation>a<1</equation>时收敛.

对于反常积分<equation>\int_{1}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x</equation>，由于<equation>\lim_{x\rightarrow+\infty}\frac{\frac{1}{x^{a}(1+x)^{b}}}{\frac{1}{x^{a+b}}}=\lim_{x\rightarrow+\infty}\left(\frac{x}{1+x}\right)^{b}=1</equation>，故当<equation>x\rightarrow+\infty</equation>时，<equation>\frac{1}{x^{a}(1+x)^{b}}</equation>与<equation>\frac{1}{x^{a+b}}</equation>等价. 反常积分<equation>\int_{1}^{+\infty}\frac{1}{x^{a+b}}\mathrm{d}x</equation>当且仅当<equation>a+b>1</equation>时收敛，故<equation>\int_{1}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x</equation>当且仅当<equation>a+b>1</equation>时收敛.

综上所述，反常积分<equation>\int_{0}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}</equation>收敛当且仅当 a,b满足 a < 1 且 a+b > 1，应选 C.

---

**2013年第12题 | 填空题 | 4分**

<equation>2. \int_ {1} ^ {+ \infty} \frac {\ln x}{(1 + x) ^ {2}} \mathrm {d} x = \underline {{}}</equation>

**答案:**## ln 2.

**解析:**<equation>\begin{aligned} { } ^ { + \infty } \frac {\ln x}{( 1 + x ) ^ { 2 } } \mathrm { d } x &= - \int _ { 1 } ^ { + \infty } \ln x \mathrm { d } \left( \frac { 1 } { 1 + x } \right) = - \left[ \left. \frac {\ln x}{1 + x} \right| _ { 1 } ^ { + \infty } - \int _ { 1 } ^ { + \infty } \frac { 1 } { x ( 1 + x ) } \mathrm { d } x \right] \\ &= - \lim _ {x \rightarrow + \infty} \frac {\ln x}{1 + x} + \int_ {1} ^ {+ \infty} \left(\frac {1}{x} - \frac {1}{x + 1}\right) \mathrm {d} x \\ \underline {{\text {洛必达}}} - \lim _ {x \rightarrow + \infty} \frac {1}{x} + \ln \frac {x}{x + 1} \Bigg | _ {1} ^ {+ \infty} \\ &= 0 + \ln 1 - \ln \frac {1}{2} = \ln 2. \end{aligned}</equation>

---

**2010年第3题 | 选择题 | 4分 | 答案: D**

3. 设 m,n均是正整数，则反常积分<equation>\int_{0}^{1}\frac{\sqrt[m]{\ln^{2}(1-x)}}{\sqrt[n]{x}} \mathrm{d} x</equation>的收敛性（    ）

A. 仅与 m的取值有关 B. 仅与 n的取值有关

C. 与 m,n的取值都有关 D. 与 m,n的取值都无关

答案: D

**解析:**由于被积函数有两个可能的瑕点，<equation>x=0</equation>和<equation>x=1</equation>，故将原积分拆成两部分进行考虑.<equation>\int_ {0} ^ {1} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} \mathrm {d} x = \int_ {0} ^ {\frac {1}{2}} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} \mathrm {d} x + \int_ {\frac {1}{2}} ^ {1} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} \mathrm {d} x.</equation>先讨论<equation>\int_0^{\frac{1}{2}}\frac{[\ln(1 - x)]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>的收敛性.考虑<equation>\lim_{x\to 0^{+}}\frac{[\ln(1 - x)]^{\frac{2}{m}}}{x^{\frac{1}{n}}}</equation>.<equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} \xlongequal {\ln (1 - x) \sim (- x)} \lim _ {x \rightarrow 0 ^ {+}} x ^ {\frac {2}{m} - \frac {1}{n}} = \left\{\begin{array}{l l}0,&\frac {2}{m} - \frac {1}{n} > 0,\\1,&\frac {2}{m} - \frac {1}{n} = 0,\\\infty ,&\frac {2}{m} - \frac {1}{n} < 0.\end{array}\right.</equation>当 m，n为正整数时，<equation>\frac{2}{m} -\frac{1}{n}\geqslant \frac{2}{m} -1 > -1.</equation>- 当<equation>\frac{2}{m}-\frac{1}{n}\geqslant0</equation>时，<equation>x=0</equation>是被积函数的可去间断点，<equation>\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}</equation>在<equation>\left[0,\frac{1}{2}\right]</equation>上可积，<equation>\int_{0}^{\frac{1}{2}}\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>存在且有限.

- 当<equation>- 1 < \frac{2}{m} - \frac{1}{n} < 0</equation>时，<equation>x=0</equation>是被积函数的瑕点.取<equation>p=\frac{1}{n}-\frac{2}{m}</equation>则<equation>0 < p < 1</equation><equation>\lim_{x\rightarrow 0^{+}}\frac{x^{p}\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}=1.</equation>由极限审敛法可知反常积分<equation>\int_{0}^{\frac{1}{2}}\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>收敛.

因此，不论 m，n 取何正整数，积分<equation>\int_{0}^{\frac{1}{2}}\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>均收敛.

下面讨论<equation>\int_{\frac{1}{2}}^{1}\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>的收敛性. x=1为被积函数的瑕点.

考虑极限<equation>\lim _ {x \rightarrow 1 ^ {-}} \sqrt {1 - x} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} = \lim _ {x \rightarrow 1 ^ {-}} \sqrt {1 - x} \left[ \ln (1 - x) \right] ^ {\frac {2}{m}}.</equation>记<equation>I _ {0} = \lim _ {x \rightarrow 1 ^ {-}} \sqrt {1 - x} \left[ \ln (1 - x) \right] ^ {\frac {2}{m}} \xlongequal {u = 1 - x} \lim _ {u \rightarrow 0 ^ {+}} u ^ {\frac {1}{2}} (\ln u) ^ {\frac {2}{m}}.</equation>若 m=1，则<equation>I _ {0} = \lim _ {u \rightarrow 0 ^ {+}} \frac {\left(\ln u\right) ^ {2}}{u ^ {- \frac {1}{2}}} \xlongequal {\text {洛必达}} \lim _ {u \rightarrow 0 ^ {+}} \frac {- 4 \ln u}{u ^ {- \frac {1}{2}}} \xlongequal {\text {洛必达}} \lim _ {u \rightarrow 0 ^ {+}} 8 u ^ {\frac {1}{2}} = 0.</equation>若 m=2，则<equation>I _ {0} = \lim _ {u \rightarrow 0 ^ {+}} \frac {\ln u}{u ^ {- \frac {1}{2}}} \xlongequal {\text {洛 必达}} \lim _ {u \rightarrow 0 ^ {+}} (- 2) u ^ {\frac {1}{2}} = 0.</equation>若<equation>m > 2</equation>，则<equation>0 < \frac{2}{m} < 1</equation>，同理使用洛必达法则可计算得<equation>I_0 = 0.</equation>因此，由极限审敛法知，不论 m，n 取何正整数，积分<equation>\int_{\frac{1}{2}}^{1} \frac{\left[ \ln(1 - x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>均收敛综上所述，不论 m，n 取何正整数，积分<equation>\int_{0}^{1} \frac{\left[ \ln(1 - x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>均收敛.应选D.

---


#### 定积分的应用

**2019年第17题 | 解答题 | 10分**

17. (本题满分10分）

求曲线<equation>y=\mathrm{e}^{-x}\sin x(x\geqslant 0)</equation>与x轴之间图形的面积.

**答案:**<equation>\frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}.</equation>

**解析:**解（法一）注意到<equation>\mathrm{e}^{-x}</equation>恒大于零.根据定积分的几何意义，曲线位于<equation>(k\pi ,(k + 1)\pi)</equation>的部分与<equation>x</equation>轴之间的图形面积等于<equation>\int_{k\pi}^{(k + 1)\pi}\mathrm{e}^{-x}|\sin x|\mathrm{d}x.</equation>计算<equation>S_{n}。</equation><equation>\begin{aligned} S _ {n} &= \sum_ {k = 0} ^ {n - 1} \int_ {k \pi} ^ {(k + 1) \pi} \mathrm {e} ^ {- x} | \sin x | \mathrm {d} x \xlongequal {t = x - k \pi} \sum_ {k = 0} ^ {n - 1} \int_ {0} ^ {\pi} \mathrm {e} ^ {- (t + k \pi)} | \sin (t + k \pi) | \mathrm {d} t \\ &= \sum_ {k = 0} ^ {n - 1} \mathrm {e} ^ {- k \pi} \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t. \end{aligned}</equation>下面计算<equation>\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t &= - \int_ {0} ^ {\pi} \sin t \mathrm {d} \left(\mathrm {e} ^ {- t}\right) = - \left(\sin t \mathrm {e} ^ {- t} \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \cos t \mathrm {d} t\right) \\ &= \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \cos t \mathrm {d} t = - \int_ {0} ^ {\pi} \cos t \mathrm {d} \left(\mathrm {e} ^ {- t}\right) \\ &= - \cos t \mathrm {e} ^ {- t} \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t \\ &= \mathrm {e} ^ {- \pi} + 1 - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t. \end{aligned}</equation>由上式可得<equation>2\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t = \mathrm{e}^{-\pi} + 1</equation>，于是<equation>\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t = \frac{1}{2}\left(\mathrm{e}^{-\pi} + 1\right)</equation>.

因此，<equation>S = \lim _ {n \rightarrow \infty} S _ {n} = \frac {1}{2} \left(\mathrm {e} ^ {- \pi} + 1\right) \lim _ {n \rightarrow \infty} \frac {1 - \mathrm {e} ^ {- n \pi}}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} \cdot \frac {\mathrm {e} ^ {- \pi} + 1}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}.</equation>（法二）注意到<equation>\mathrm{e}^{-x}</equation>恒大于零.当<equation>x\in(2n\pi,(2n+1)\pi)</equation>时，<equation>\sin x > 0</equation>；当<equation>x\in((2n+1)\pi,</equation><equation>(2n+2)\pi)</equation>时，<equation>\sin x < 0</equation>因此，根据定积分的几何意义，曲线位于<equation>(2n\pi, (2n+1)\pi)</equation>的部分与x轴之间的图形面积等于<equation>\int_{2n\pi}^{(2n+1)\pi}\mathrm{e}^{-x}\sin x\mathrm{d}x</equation>；曲线位于<equation>((2n+1)\pi, (2n+2)\pi)</equation>的部分与x轴之间的图形面积等于<equation>-\int_{(2n+1)\pi}^{(2n+2)\pi}\mathrm{e}^{-x}\sin x\mathrm{d}x.</equation>记所求面积为 S，则<equation>S = \sum_ {n = 0} ^ {\infty} \int_ {2 n \pi} ^ {(2 n + 1) \pi} \mathrm {e} ^ {- x} \sin x \mathrm {d} x - \sum_ {n = 0} ^ {\infty} \int_ {(2 n + 1) \pi} ^ {(2 n + 2) \pi} \mathrm {e} ^ {- x} \sin x \mathrm {d} x.</equation>下面计算<equation>\int \mathrm{e}^{-x}\sin x\mathrm{d}x.</equation><equation>\begin{aligned} \int \mathrm {e} ^ {- x} \sin x \mathrm {d} x &= - \int \sin x \mathrm {d} \left(\mathrm {e} ^ {- x}\right) = - \left(\sin x \mathrm {e} ^ {- x} - \int \mathrm {e} ^ {- x} \cos x \mathrm {d} x\right) \\ &= - \sin x \mathrm {e} ^ {- x} + \int \mathrm {e} ^ {- x} \cos x \mathrm {d} x = - \sin x \mathrm {e} ^ {- x} - \int \cos x \mathrm {d} \left(\mathrm {e} ^ {- x}\right) \\ &= - \sin x \mathrm {e} ^ {- x} - \left(\cos x \mathrm {e} ^ {- x} + \int \mathrm {e} ^ {- x} \sin x \mathrm {d} x\right). \end{aligned}</equation>由上式可得<equation>2\int \mathrm{e}^{-x}\sin x\mathrm{d}x = -\mathrm{e}^{-x}(\sin x + \cos x) - C</equation>，于是<equation>\int \mathrm {e} ^ {- x} \sin x \mathrm {d} x = - \frac {1}{2} \left[ \mathrm {e} ^ {- x} \left(\sin x + \cos x\right) + C \right],</equation>其中 C为任意常数.

因此，<equation>\begin{aligned} S &= \sum_ {n = 0} ^ {\infty} \left[ - \frac {1}{2} \mathrm {e} ^ {- x} (\sin x + \cos x) \right] \Bigg | _ {2 n \pi} ^ {(2 n + 1) \pi} + \sum_ {n = 0} ^ {\infty} \left[ \frac {1}{2} \mathrm {e} ^ {- x} (\sin x + \cos x) \right] \Bigg | _ {(2 n + 1) \pi} ^ {(2 n + 2) \pi} \\ &= \frac {1}{2} \sum_ {n = 0} ^ {\infty} \left[ \mathrm {e} ^ {- (2 n + 1) \pi} + \mathrm {e} ^ {- 2 n \pi} \right] + \frac {1}{2} \sum_ {n = 0} ^ {\infty} \left[ \mathrm {e} ^ {- (2 n + 2) \pi} + \mathrm {e} ^ {- (2 n + 1) \pi} \right] \\ &= \frac {1}{2} \left[ \sum_ {n = 0} ^ {\infty} \mathrm {e} ^ {- 2 n \pi} + 2 \sum_ {n = 0} ^ {\infty} \mathrm {e} ^ {- (2 n + 1) \pi} + \sum_ {n = 1} ^ {\infty} \mathrm {e} ^ {- 2 n \pi} \right] \\ &= \frac {1}{2} \left(\frac {1}{1 - \mathrm {e} ^ {- 2 \pi}} + \frac {2 \mathrm {e} ^ {- \pi}}{1 - \mathrm {e} ^ {- 2 \pi}} + \frac {\mathrm {e} ^ {- 2 \pi}}{1 - \mathrm {e} ^ {- 2 \pi}}\right) = \frac {1}{2} \cdot \frac {\left(1 + \mathrm {e} ^ {- \pi}\right) ^ {2}}{\left(1 + \mathrm {e} ^ {- \pi}\right) \left(1 - \mathrm {e} ^ {- \pi}\right)} \\ &= \frac {1}{2} \cdot \frac {1 + \mathrm {e} ^ {- \pi}}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}. \end{aligned}</equation>

---

**2017年第4题 | 选择题 | 4分 | 答案: C**

4. 甲、乙两人赛跑，计时开始时，甲在乙前方10（单位：m）处，图中，实线表示甲的速度曲线<equation>v=v_{1}(t)</equation>（单位： m/s），虚线表示乙的速度曲线<equation>v=v_{2}(t)</equation>，三块阴影部分面积的数值依次是10，20，3. 计时开始后乙追上甲的时刻记为<equation>t_{0}</equation>（单位：s），则（    ）

A.<equation>t_{0}=1 0</equation>B.<equation>1 5<t_{0}<2 0</equation>C.<equation>t_{0}=2 5</equation>D.<equation>t_{0}>2 5</equation>

答案: C

**解析:**解 根据定积分的物理意义，从0s到10s这段时间内，实线位于虚线之上，于是甲跑过的路程比乙跑过的路程多10m；从10s到25s这段时间内，虚线位于实线之上，于是乙跑过的路程比甲跑过的路程多20m.

---

**2012年第18题 | 解答题 | 10分**

18. (本题满分10分)

已知曲线 L：<equation>\left\{\begin{array}{l l}x=f(t),\\ y=\cos t\end{array}\right.</equation><equation>(0\leqslant t<\frac{\pi}{2})</equation>，其中函数 f(t)具有连续导数，且 f(0)=0，<equation>f^{\prime}(t)>0</equation><equation>(0<t<\frac{\pi}{2})</equation>. 若曲线 L的切线与 x轴的交点到切点的距离恒为1，求函数 f(t)的表达式，并求以曲线 L及 x轴和 y轴为边界的区域的面积.

**答案:**(18)<equation>f ( t )=\ln | \sec t+\tan t |-\sin t, 0\leqslant t < \frac{\pi}{2}</equation>; 面积为<equation>\frac{\pi}{4}</equation>

**解析:**解曲线 L在点（ f(t），cos t）处的切线的斜率为<equation>\frac{\mathrm{d} y}{\mathrm{d} x}=\frac{\frac{\mathrm{d} y}{\mathrm{d} t}}{\frac{\mathrm{d} x}{\mathrm{d} t}}=-\frac{\sin t}{f^{\prime}(t)},</equation>从而切线方程为<equation>y - \cos t = \frac {- \sin t}{f ^ {\prime} (t)} [ x - f (t) ],</equation>于是切线与<equation>x</equation>轴的交点为<equation>\left(f(t) + \frac{\cos t}{\sin t} f^{\prime}(t),0\right)</equation>.由已知条件可得<equation>\left[ f (t) + \frac {\cos t}{\sin t} f ^ {\prime} (t) - f (t) \right] ^ {2} + \left(0 - \cos t\right) ^ {2} = 1,</equation>化简得<equation>[f^{\prime}(t)]^{2} = \left(\frac{\sin^{2}t}{\cos t}\right)^{2}</equation>.

由于当<equation>0 < t < \frac{\pi}{2}</equation>时，<equation>f^{\prime}(t) > 0</equation>，故<equation>f^{\prime}(t) = \frac{\sin^{2}t}{\cos t}</equation>. 又<equation>f(0) = 0</equation>，故<equation>\forall 0\leqslant t < \frac{\pi}{2}</equation>，有<equation>f (t) = \int_ {0} ^ {t} \frac {\sin^ {2} x}{\cos x} \mathrm {d} x = \int_ {0} ^ {t} \frac {1 - \cos^ {2} x}{\cos x} \mathrm {d} x = \int_ {0} ^ {t} \sec x \mathrm {d} x - \int_ {0} ^ {t} \cos x \mathrm {d} x = \ln | \sec t + \tan t | - \sin t,</equation>设以曲线<equation>L</equation>及<equation>x</equation>轴和<equation>y</equation>轴为边界的区域的面积为<equation>S</equation>，则<equation>\begin{aligned} S &= \int_ {0} ^ {\frac {\pi}{2}} y (t) \mathrm {d} \left(x (t)\right) = \int_ {0} ^ {\frac {\pi}{2}} \cos t \cdot x ^ {\prime} (t) \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \cos t \cdot f ^ {\prime} (t) \mathrm {d} t \\ &= \int_ {0} ^ {\frac {\pi}{2}} \cos t \cdot \frac {\sin^ {2} t}{\cos t} \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {2} t \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \frac {1 - \cos 2 t}{2} \mathrm {d} t = \frac {\pi}{4}. \end{aligned}</equation>

---

**2011年第9题 | 填空题 | 4分**

9. 曲线<equation>y=\int_{0}^{x}\tan t\mathrm{d}t \left( 0\leqslant x\leqslant\frac{\pi}{4} \right)</equation>的弧长 s = ___

**答案:**##<equation>\ln(\sqrt{2}+1).</equation>

**解析:**<equation>\begin{aligned} s &= \int_ {0} ^ {\frac {\pi}{4}} \sqrt {1 + \left[ y ^ {\prime} (x) \right] ^ {2}} \mathrm {d} x = \int_ {0} ^ {\frac {\pi}{4}} \sqrt {1 + \tan^ {2} x} \mathrm {d} x \\ &= \int_ {0} ^ {\frac {\pi}{4}} \sec x \mathrm {d} x = \ln | \sec x + \tan x | \Bigg | _ {0} ^ {\frac {\pi}{4}} = \ln (\sqrt {2} + 1). \end{aligned}</equation>

---

**2009年第17题 | 解答题 | 10分**

17. (本题满分11分)

椭球面<equation>S_{1}</equation>是椭圆<equation>\frac{x^{2}}{4}+\frac{y^{2}}{3}=1</equation>绕 x轴旋转而成，圆雉面<equation>S_{2}</equation>是由过点(4,0)且与椭圆<equation>\frac{x^{2}}{4}+\frac{y^{2}}{3}=1</equation>相切的直线绕 x轴旋转而成.

I. 求<equation>S_{1}</equation>及<equation>S_{2}</equation>的方程；

II. 求<equation>S_{1}</equation>与<equation>S_{2}</equation>之间的立体的体积.

**答案:**(17) （I）椭球面<equation>S_{1}</equation>的方程为<equation>\frac{x^{2}}{4}+\frac{y^{2}+z^{2}}{3}=1</equation>，圆锥面<equation>S_{2}</equation>的方程为<equation>y^{2}+z^{2}=\frac{1}{4}(x-4)^{2}</equation>； （Ⅱ）<equation>V=\pi.</equation>

**解析:**解（I）由椭圆<equation>\frac{x^{2}}{4}+\frac{y^{2}}{3}=1</equation>绕 x轴旋转得到的椭球面<equation>S_{1}</equation>的方程为<equation>\frac {x ^ {2}}{4} + \frac {\left(\pm \sqrt {y ^ {2} + z ^ {2}}\right) ^ {2}}{3} = 1,</equation>即为<equation>\frac{x^2}{4} +\frac{y^2 + z^2}{3} = 1.</equation>设椭圆<equation>\frac{x^{2}}{4}+\frac{y^{2}}{3}=1</equation>上任一点为（<equation>2\cos \theta ,\sqrt{3}\sin \theta )</equation>，则过该点且与椭圆相切的直线的斜率为<equation>\frac{\mathrm{d}y}{\mathrm{d}x}=</equation><equation>\frac{\frac{\mathrm{d}y}{\mathrm{d}\theta}}{\frac{\mathrm{d}x}{\mathrm{d}\theta}}=\frac{(\sqrt{3}\sin \theta)^{\prime}}{(2\cos \theta)^{\prime}}=\frac{\sqrt{3}\cos \theta}{-2\sin \theta}</equation>，从而切线方程为<equation>y = - \frac {\sqrt {3} \cos \theta}{2 \sin \theta} (x - 2 \cos \theta) + \sqrt {3} \sin \theta .</equation>将<equation>( x,y)=(4,0)</equation>代入上式得<equation>\cos \theta=\frac{1}{2},\sin \theta=\pm \frac{\sqrt{3}}{2}</equation>，于是切线方程为<equation>y=\pm \frac{1}{2} ( x-4 )</equation>，切点为<equation>\left( 1,\pm \frac{3}{2} \right).</equation>又圆锥面<equation>S_{2}</equation>是由直线<equation>y=\frac{1}{2} ( x-4 )</equation>绕x轴旋转得到，故<equation>S_{2}</equation>的方程为<equation>\pm \sqrt{y^{2}+z^{2}}=\frac{1}{2} ( x-4 )</equation>即为<equation>y^{2}+z^{2}=\frac{1}{4} ( x-4 )^{2}.</equation>（Ⅱ）记<equation>V_{1}</equation>为椭球面<equation>S_{1}</equation>所围成的椭球体在平面<equation>x=1</equation>与<equation>x=2</equation>之间的部分的体积，则由旋转体体积公式知，<equation>V_{1}=\pi \int_{1}^{2} y^{2}\mathrm{d}x=\pi \int_{1}^{2} 3 \left( 1-\frac{x^{2}}{4} \right) \mathrm{d}x=\frac{5}{4} \pi</equation>；记<equation>V_{2}</equation>为圆锥面<equation>S_{2}</equation>与平面<equation>x=1</equation>所围成的区域的体积，即底面半径为<equation>\frac{3}{2}</equation>，高为3的圆锥体体积，则<equation>V_{2}=\frac{1}{3}\pi r^{2} h=\frac{1}{3}\pi \cdot \left( \frac{3}{2} \right)^{2} \cdot 3=\frac{9}{4}\pi.</equation>因此，<equation>S_{1}</equation>与<equation>S_{2}</equation>之间的立体的体积为<equation>V=V_{2}-V_{1}=\frac{9}{4}\pi -\frac{5}{4}\pi =\pi.</equation>

---


#### 不定积分的计算

**2018年第15题 | 解答题 | 10分**

15. (本题满分10分)

求不定积分

**答案:**<equation>\frac{\mathrm{e}^{2x}\arctan \sqrt{\mathrm{e}^{x} - 1}}{2} -\frac{1}{6}\left(\mathrm{e}^{x} - 1\right)^{\frac{3}{2}} - \frac{1}{2}\sqrt{\mathrm{e}^{x} - 1} + C</equation>，其中C为任意常数.

**解析:**解 利用分部积分法.<equation>\begin{aligned} \int \mathrm {e} ^ {2 x} \arctan \sqrt {\mathrm {e} ^ {x} - 1} \mathrm {d} x \stackrel {\text {分 部 积 分}} {=} \frac {1}{2} \int \arctan \sqrt {\mathrm {e} ^ {x} - 1} \mathrm {d} \left(\mathrm {e} ^ {2 x}\right) \\ &= \frac {\mathrm {e} ^ {2 x}}{2} \cdot \arctan \sqrt {\mathrm {e} ^ {x} - 1} - \frac {1}{2} \int \mathrm {e} ^ {2 x} \cdot \frac {1}{1 + \mathrm {e} ^ {x} - 1} \cdot \frac {\mathrm {e} ^ {x}}{2 \sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x \\ &= \frac {\mathrm {e} ^ {2 x} \arctan \sqrt {\mathrm {e} ^ {x} - 1}}{2} - \frac {1}{4} \int \frac {\mathrm {e} ^ {2 x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x. \end{aligned}</equation>下面用两种方法计算<equation>\int \frac{\mathrm{e}^{2x}}{\sqrt{\mathrm{e}^{x} - 1}}\mathrm{d}x.</equation>（法一）令<equation>u = \sqrt{\mathrm{e}^{x} - 1}</equation>，则<equation>x = \ln (u^{2} + 1)</equation>，<equation>\mathrm{d}x = \frac{2u}{u^{2} + 1}\mathrm{d}u.</equation><equation>\begin{aligned} \int \frac {\mathrm {e} ^ {2 x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x &= \int \frac {\left(u ^ {2} + 1\right) ^ {2}}{u} \cdot \frac {2 u}{u ^ {2} + 1} \mathrm {d} u = 2 \int \left(u ^ {2} + 1\right) \mathrm {d} u = \frac {2}{3} u ^ {3} + 2 u + C _ {1} \\ &= \frac {2}{3} \left(\mathrm {e} ^ {x} - 1\right) ^ {\frac {3}{2}} + 2 \sqrt {\mathrm {e} ^ {x} - 1} + C _ {1}, \end{aligned}</equation>其中<equation>C_{1}</equation>为任意常数.

（法二）令<equation>t = \mathrm{e}^{x}</equation>，则<equation>\mathrm{d}t = \mathrm{e}^{x}\mathrm{d}x.</equation><equation>\begin{aligned} \int \frac {\mathrm {e} ^ {2 x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x &= \int \frac {\mathrm {e} ^ {x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} \left(\mathrm {e} ^ {x}\right) = \int \frac {t}{\sqrt {t - 1}} \mathrm {d} t = \int \frac {t - 1 + 1}{\sqrt {t - 1}} \mathrm {d} t = \int \left(\sqrt {t - 1} + \frac {1}{\sqrt {t - 1}}\right) \mathrm {d} t \\ &= \frac {2}{3} (t - 1) ^ {\frac {3}{2}} + 2 \sqrt {t - 1} + C _ {1} = \frac {2}{3} \left(\mathrm {e} ^ {x} - 1\right) ^ {\frac {3}{2}} + 2 \sqrt {\mathrm {e} ^ {x} - 1} + C _ {1}, \end{aligned}</equation>其中<equation>C_{1}</equation>为任意常数.

因此，<equation>\text {原 积 分} = \frac {\mathrm {e} ^ {2 x} \arctan \sqrt {\mathrm {e} ^ {x} - 1}}{2} - \frac {1}{6} \left(\mathrm {e} ^ {x} - 1\right) ^ {\frac {3}{2}} - \frac {1}{2} \sqrt {\mathrm {e} ^ {x} - 1} + C,</equation>其中 C为任意常数.

---

**2016年第2题 | 选择题 | 4分 | 答案: D**

2. 已知函数<equation>f(x)=\left\{\begin{array}{l l}2(x-1),&x<1,\\ \ln x,&x\geqslant 1,\end{array} \right.</equation>则 f(x)的一个原函数是（    ）

A.<equation>F(x)=\left\{\begin{array}{l l}{(x-1)^{2},}&{x<1,}\\ {x(\ln x-1),}&{x\geqslant 1.}\\ \end{array} \right.</equation>B.<equation>F(x)=\left\{\begin{array}{l l}{(x-1)^{2},}&{x<1,}\\ {x(\ln x+1)-1,}&{x\geqslant 1.}\\ \end{array} \right.</equation>C.<equation>F(x)=\left\{\begin{array}{l l}{(x-1)^{2},}&{x<1,}\\ {x(\ln x+1)+1,}&{x\geqslant 1.}\\ \end{array} \right.</equation>D.<equation>F(x)=\left\{\begin{array}{l l}{(x-1)^{2},}&{x<1,}\\ {x(\ln x-1)+1,}&{x\geqslant 1.}\\ \end{array} \right.</equation>

答案: D

**解析:**解（法一）当 x < 1时，<equation>F (x) = \int 2 (x - 1) \mathrm {d} x = (x - 1) ^ {2} + C _ {1};</equation>当 x≥1时，<equation>F (x) = \int \ln x \mathrm {d} x = x (\ln x - 1) + C _ {2},</equation>其中<equation>C_{1}, C_{2}</equation>均为任意常数.

进一步，由于<equation>F(x)</equation>是<equation>f(x)</equation>在<equation>(-\infty , + \infty)</equation>上的一个原函数，故<equation>F(x)</equation>在<equation>x = 1</equation>处应连续.<equation>\lim _ {x \rightarrow 1 ^ {-}} F (x) = \lim _ {x \rightarrow 1 ^ {-}} \left(x - 1\right) ^ {2} + C _ {1} = C _ {1}, \quad \lim _ {x \rightarrow 1 ^ {+}} F (x) = \lim _ {x \rightarrow 1 ^ {+}} x \left(\ln x - 1\right) + C _ {2} = C _ {2} - 1.</equation>若<equation>F ( x )</equation>连续，则<equation>C_{1}=C_{2}-1.</equation>选项D中，<equation>C_{1}=0, C_{2}=1, F(x)</equation>连续，应选D.

（法二）首先，由于<equation>F ( x )</equation>是<equation>f ( x )</equation>的原函数，故必连续，而四个选项中的<equation>F ( x )</equation>均是分段函数，于是我们可以分别考察<equation>F ( x )</equation>在分界点处的连续性.

选项A：<equation>\lim_{x\to 1^{-}}F(x)=0,\lim_{x\to 1^{+}}F(x)=-1.F(x)</equation>不连续.

选项B：<equation>\lim_{x\to 1^{-}}F(x)=\lim_{x\to 1^{+}}F(x)=0=F(1). F(x)</equation>连续.

选项C：<equation>\lim_{x\to 1^{-}}F(x) = 0</equation>，<equation>\lim_{x\to 1^{+}}F(x) = 2.F(x)</equation>不连续.

选项D：<equation>\lim_{x\to 1^{-}}F(x) = \lim_{x\to 1^{+}}F(x) = 0 = F(1).F(x)</equation>连续.

由上可排除选项A与选项C.

选项B与选项D的差别在于函数表达式.

计算<equation>f(x)</equation>在<equation>[1, +\infty)</equation>上的原函数，得<equation>\int f (x) \mathrm {d} x = \int \ln x \mathrm {d} x = x (\ln x - 1) + C,</equation>其中 C为任意常数.比较（1）式与选项B、选项D，可排除选项B.应选D.

---


### 常微分方程


#### 一阶非齐次线性微分方程

**2025年第18题 | 解答题 | 12分**
18. 已知函数 f(u)在区间 （0，<equation>+ \infty</equation>）内具有2阶导数，记<equation>g ( x,y)=f\left(\frac{x}{y}\right)</equation>，若 g(x,y)满足<equation>x ^ {2} \frac {\partial^ {2} g}{\partial x ^ {2}} + x y \frac {\partial^ {2} g}{\partial x \partial y} + y ^ {2} \frac {\partial^ {2} g}{\partial y ^ {2}} = 1,</equation>且<equation>g ( x,x)=1,\frac{\partial g}{\partial x}\bigg|_{(x,x)}=\frac{2}{x}</equation>，求 f(u).
**答案: **<equation>f ( u ) = \frac { 1 } { 2 } \left( \ln u \right)^{2}+2 \ln u+1.</equation>
**解析: **解 根据链式法则，<equation>\frac {\partial g}{\partial x} = f ^ {\prime} \left(\frac {x}{y}\right) \cdot \frac {1}{y}, \quad \frac {\partial g}{\partial y} = f ^ {\prime} \left(\frac {x}{y}\right) \cdot \left(- \frac {x}{y ^ {2}}\right),</equation><equation>\frac {\partial^ {2} g}{\partial x ^ {2}} = f ^ {\prime \prime} \left(\frac {x}{y}\right) \cdot \frac {1}{y ^ {2}},</equation><equation>\frac {\partial^ {2} g}{\partial x \partial y} = f ^ {\prime \prime} \left(\frac {x}{y}\right) \cdot \left(- \frac {x}{y ^ {2}}\right) \cdot \frac {1}{y} - \frac {1}{y ^ {2}} f ^ {\prime} \left(\frac {x}{y}\right) = - \frac {x}{y ^ {3}} f ^ {\prime \prime} \left(\frac {x}{y}\right) - \frac {1}{y ^ {2}} f ^ {\prime} \left(\frac {x}{y}\right),</equation><equation>\frac {\partial^ {2} g}{\partial y ^ {2}} = f ^ {\prime \prime} \left(\frac {x}{y}\right) \cdot \left(- \frac {x}{y ^ {2}}\right) \cdot \left(- \frac {x}{y ^ {2}}\right) + \frac {2 x}{y ^ {3}} f ^ {\prime} \left(\frac {x}{y}\right) = \frac {x ^ {2}}{y ^ {4}} f ^ {\prime \prime} \left(\frac {x}{y}\right) + \frac {2 x}{y ^ {3}} f ^ {\prime} \left(\frac {x}{y}\right).</equation>代入<equation>x^{2}\frac{\partial^{2}g}{\partial x^{2}}+xy\frac{\partial^{2}g}{\partial x\partial y}+y^{2}\frac{\partial^{2}g}{\partial y^{2}}=1</equation>可得<equation>\frac {x ^ {2}}{y ^ {2}} f ^ {\prime \prime} \left(\frac {x}{y}\right) - \frac {x ^ {2}}{y ^ {2}} f ^ {\prime \prime} \left(\frac {x}{y}\right) - \frac {x}{y} f ^ {\prime} \left(\frac {x}{y}\right) + \frac {x ^ {2}}{y ^ {2}} f ^ {\prime \prime} \left(\frac {x}{y}\right) + \frac {2 x}{y} f ^ {\prime} \left(\frac {x}{y}\right) = 1.</equation>整理可得<equation>\frac{x^2}{y^2} f^{\prime \prime}\left(\frac{x}{y}\right) + \frac{x}{y} f^{\prime}\left(\frac{x}{y}\right) = 1.</equation>令<equation>u=\frac{x}{y}</equation>，可得<equation>u^{2}f^{\prime \prime}(u)+u f^{\prime}(u)=1.</equation>下面用两种方法解该方程

（法一）整理<equation>u^{2}f^{\prime \prime}(u)+u f^{\prime}(u)=1</equation>可得<equation>f^{\prime \prime}(u)+\frac{1}{u} f^{\prime}(u)=\frac{1}{u^{2}}.</equation>这是一个可降阶微分方程.令<equation>p=f^{\prime}(u)</equation>，则该方程化为<equation>p^{\prime}+\frac{p}{u}=\frac{1}{u^{2}}.</equation>由一阶非齐次线性微分方程的通解公式可得<equation>p = \mathrm {e} ^ {\int \left(- \frac {1}{u}\right) \mathrm {d} u} \left(\int \frac {1}{u ^ {2}} \cdot \mathrm {e} ^ {\int \frac {1}{u} \mathrm {d} u} \mathrm {d} u + C _ {1}\right) = \frac {1}{u} \left(\int \frac {1}{u} \mathrm {d} u + C _ {1}\right) = \frac {1}{u} \left(\ln u + C _ {1}\right),</equation>其中<equation>C_{1}</equation>为待定常数.

由<equation>\frac{\partial g}{\partial x}=f^{\prime}\left(\frac{x}{y}\right)\cdot \frac{1}{y}</equation>可得<equation>\frac{\partial g}{\partial x}\bigg|_{(x,x)}=\frac{1}{x} f^{\prime}(1),</equation>结合<equation>\frac{\partial g}{\partial x}\bigg|_{(x,x)}=\frac{2}{x}</equation>可得<equation>f^{\prime}(1)=2.</equation>代入<equation>f^{\prime}(u)</equation><equation>= \frac{1}{u} (\ln u + C_1)</equation>可得<equation>C_{1}=2.</equation>于是，<equation>f^{\prime}(u)=\frac{1}{u}(\ln u+2).</equation>进一步积分可得<equation>f (u) = \int \frac {1}{u} (\ln u + 2) \mathrm {d} u = \int \ln u \mathrm {d} (\ln u) + \int \frac {2}{u} \mathrm {d} u = \frac {1}{2} (\ln u) ^ {2} + 2 \ln u + C _ {2},</equation>其中<equation>C_{2}</equation>为待定常数.

由<equation>g(x,x) = 1</equation>可得<equation>f(1) = 1</equation>，代入<equation>f(u) = \frac{1}{2} (\ln u)^{2} + 2\ln u + C_{2}</equation>可得<equation>C_{2} = 1.</equation>因此，<equation>f(u)=\frac{1}{2} (\ln u)^{2}+2\ln u+1.</equation>（法二）注意到<equation>u^{2} f^{\prime \prime}(u) + uf^{\prime}(u) = 1</equation>是欧拉方程

令<equation>u=\mathrm{e}^{\prime}.</equation>于是，<equation>\frac {\mathrm {d} f}{\mathrm {d} t} = \frac {\mathrm {d} f}{\mathrm {d} u} \cdot \frac {\mathrm {d} u}{\mathrm {d} t} = \frac {\mathrm {d} f}{\mathrm {d} u} \cdot \mathrm {e} ^ {t}.</equation><equation>\frac {\mathrm {d} ^ {2} f}{\mathrm {d} t ^ {2}} = \frac {\mathrm {d} \left(\frac {\mathrm {d} f}{\mathrm {d} u} \cdot \mathrm {e} ^ {t}\right)}{\mathrm {d} t} = \frac {\mathrm {d} ^ {2} f}{\mathrm {d} u ^ {2}} \cdot \frac {\mathrm {d} u}{\mathrm {d} t} \cdot \mathrm {e} ^ {t} + \frac {\mathrm {d} f}{\mathrm {d} u} \cdot \mathrm {e} ^ {t} = \frac {\mathrm {d} ^ {2} f}{\mathrm {d} u ^ {2}} \cdot \mathrm {e} ^ {2 t} + \frac {\mathrm {d} f}{\mathrm {d} u} \cdot \mathrm {e} ^ {t} = \frac {\mathrm {d} ^ {2} f}{\mathrm {d} u ^ {2}} \cdot \mathrm {e} ^ {2 t} + \frac {\mathrm {d} f}{\mathrm {d} t}.</equation>由此可得<equation>\frac{\mathrm{d}f}{\mathrm{d}u} = \mathrm{e}^{-t}\frac{\mathrm{d}f}{\mathrm{d}t},\frac{\mathrm{d}^2f}{\mathrm{d}u^2} = \mathrm{e}^{-2t}\left(\frac{\mathrm{d}^2f}{\mathrm{d}t^2} -\frac{\mathrm{d}f}{\mathrm{d}t}\right)</equation>，于是<equation>u^{2}f^{\prime \prime}(u) = \frac{\mathrm{d}^2f}{\mathrm{d}t^2} -\frac{\mathrm{d}f}{\mathrm{d}t},uf^{\prime}(u) = \frac{\mathrm{d}f}{\mathrm{d}t}</equation>代入<equation>u^{2}f^{\prime \prime}(u)</equation><equation>+uf^{\prime}(u) = 1</equation>可得<equation>\frac{\mathrm{d}^2f}{\mathrm{d}t^2} = 1.</equation>这是一个二阶常系数非齐次线性微分方程，其对应的齐次方程的特征方程为<equation>\lambda^2 = 0</equation>，特征根为<equation>\lambda_{1,2} = 0</equation>.于是，该齐次方程的解为<equation>y = C_{1} + C_{2} t</equation>，其中<equation>C_{1}, C_{2}</equation>为待定常数.

由于0是特征方程的二重根，故可设<equation>\frac{\mathrm{d}^2f}{\mathrm{d}t^2} = 1</equation>的特解<equation>y^{*} = At^{2}</equation>. 将<equation>y^{*} = At^{2}</equation>代入<equation>\frac{\mathrm{d}^2f}{\mathrm{d}t^2} = 1</equation>可得2A<equation>= 1</equation>，即<equation>A = \frac{1}{2}</equation>.由此可得<equation>y^{*} = \frac{1}{2} t^{2}</equation>，进一步可得<equation>\frac{\mathrm{d}^2f}{\mathrm{d}t^2} = 1</equation>的解为<equation>y = C_{1} + C_{2}t + \frac{1}{2} t^{2}</equation>.由<equation>u = \mathrm{e}^{t}</equation>可得<equation>t = \ln u</equation>，从而<equation>f(u) = C_{1} + C_{2}\ln u + \frac{1}{2}(\ln u)^{2}</equation>.计算可得<equation>f^{\prime}(u) = \frac{1}{u}(\ln u + C_{2})</equation>同法一可得<equation>f(1) = 1,f^{\prime}(1) = 2</equation>，代入<equation>f(u),f^{\prime}(u)</equation>的表达式解得<equation>\left\{ \begin{array}{l} C_{1} = 1, \\ C_{2} = 2 \end{array} \right.</equation>因此，<equation>f ( u ) = \frac { 1 } { 2 } \left( \ln u \right)^{2}+2 \ln u+1.</equation>

---

**2022年第17题 | 解答题 | 10分**
17. (本题满分10分）

设函数 y(x)是微分方程<equation>y^{\prime}+\frac{1}{2\sqrt{x}} y=2+\sqrt{x}</equation>的满足条件 y(1)=3的解，求曲线 y=y(x)的渐近线.
**答案: **<equation>y=2 x</equation>为曲线<equation>y=2 x+\mathrm{e}^{1-\sqrt{x}}</equation>的斜渐近线，也是唯一的渐近线.
**解析: **解 根据求解公式，<equation>y = \mathrm {e} ^ {- \int \frac {1}{2 \sqrt {x}} \mathrm {d} x} \left[ \int (2 + \sqrt {x}) \mathrm {e} ^ {\int \frac {1}{2 \sqrt {x}} \mathrm {d} x} \mathrm {d} x + C _ {0} \right] = \mathrm {e} ^ {- \sqrt {x}} \left[ \int (2 + \sqrt {x}) \mathrm {e} ^ {\sqrt {x}} \mathrm {d} x + C _ {0} \right].</equation>下面计算<equation>\int (2 + \sqrt{x})\mathrm{e}^{\sqrt{x}}\mathrm{d}x.</equation>令<equation>u=\sqrt{x}</equation>，则<equation>x=u^{2}</equation>，<equation>\mathrm{d}x=2u\mathrm{d}u.</equation><equation>\begin{aligned} \int (2 + \sqrt {x}) \mathrm {e} ^ {\sqrt {x}} \mathrm {d} x \xlongequal {u = \sqrt {x}} 2 \int (2 + u) u \mathrm {e} ^ {u} \mathrm {d} u &= 2 \left(\int u ^ {2} \mathrm {e} ^ {u} \mathrm {d} u + \int 2 u \mathrm {e} ^ {u} \mathrm {d} u\right) \\ &= 2 \left[ \int u ^ {2} \mathrm {d} \left(\mathrm {e} ^ {u}\right) + \int 2 u \mathrm {e} ^ {u} \mathrm {d} u \right] = 2 \left(u ^ {2} \mathrm {e} ^ {u} - \int 2 u \mathrm {e} ^ {u} \mathrm {d} u + \int 2 u \mathrm {e} ^ {u} \mathrm {d} u\right) \\ &= 2 u ^ {2} \mathrm {e} ^ {u} + C _ {1} = 2 x \mathrm {e} ^ {\sqrt {x}} + C _ {1}. \end{aligned}</equation>将该结果代入（1）式，可得<equation>y = \mathrm {e} ^ {- \sqrt {x}} \left(2 x \mathrm {e} ^ {\sqrt {x}} + C\right) = 2 x + C \mathrm {e} ^ {- \sqrt {x}},</equation>其中<equation>C</equation>为待定常数. 代入<equation>y(1) = 3</equation>，可得<equation>3 = 2 + C \cdot \mathrm{e}^{-1}</equation>，解得<equation>C = \mathrm{e}</equation>.

因此，<equation>y ( x ) = 2 x + \mathrm {e} ^ {1 - \sqrt {x}} , x \in ( 0, + \infty).</equation>由于函数<equation>y(x) = 2x + \mathrm{e}^{1 - \sqrt{x}}</equation>在<equation>(0, +\infty)</equation>内连续，且<equation>\lim_{x\to 0^{+}}y(x) = \mathrm{e}</equation>，故曲线<equation>y = 2x + \mathrm{e}^{1 - \sqrt{x}}</equation>没有铅直渐近线.

又因为<equation>\lim_{x\to +\infty}y(x) = \lim_{x\to +\infty}\left(2x + \mathrm{e}^{1 - \sqrt{x}}\right) = +\infty</equation>，所以曲线<equation>y = 2x + \mathrm{e}^{1 - \sqrt{x}}</equation>没有水平渐近线.

下面计算斜渐近线.<equation>\lim _ {x \rightarrow + \infty} \frac {y (x)}{x} = \lim _ {x \rightarrow + \infty} \frac {2 x + \mathrm {e} ^ {1 - \sqrt {x}}}{x} = 2,</equation><equation>\lim _ {x \rightarrow + \infty} [ y (x) - 2 x ] = \lim _ {x \rightarrow + \infty} \mathrm {e} ^ {1 - \sqrt {x}} = 0.</equation>因此，<equation>y=2x</equation>为曲线<equation>y=2x+\mathrm{e}^{1-\sqrt{x}}</equation>的斜渐近线，也是唯一的渐近线.

---

**2019年第15题 | 解答题 | 10分**
15. (本题满分10分)

设函数 y(x)是微分方程<equation>y^{\prime}+xy=\mathrm{e}^{-\frac{x^{2}}{2}}</equation>满足条件 y(0)=0的特解.

I. 求 y(x) ;

II. 求曲线 y=y(x)的凹凸区间及拐点.
**答案: **（I）<equation>y ( x )=x \mathrm{e}^{- \frac{x^{2}}{2}};</equation>（Ⅱ）凹区间为<equation>(-\sqrt{3},0)</equation>和<equation>(\sqrt{3},+\infty)</equation>，凸区间为<equation>(-\infty,-\sqrt{3})</equation>和<equation>(0,\sqrt{3})</equation>，拐点为<equation>(-\sqrt{3},-\sqrt{3} \mathrm{e}^{- \frac{3}{2}}),(0,0)</equation>和<equation>(\sqrt{3},\sqrt{3} \mathrm{e}^{- \frac{3}{2}}).</equation>
**解析: **（I）由一阶非齐次线性微分方程的求解公式可得，<equation>y = \mathrm {e} ^ {\int (- x) \mathrm {d} x} \left(\int \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \cdot \mathrm {e} ^ {\int x \mathrm {d} x} \mathrm {d} x + C\right) = \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \left(\int 1 \mathrm {d} x + C\right) = x \mathrm {e} ^ {- \frac {x ^ {2}}{2}} + C \mathrm {e} ^ {- \frac {x ^ {2}}{2}},</equation>其中 C为待定常数.

代入<equation>x = 0</equation>，<equation>y(0) = 0</equation>可得，<equation>C = 0.</equation>因此，<equation>y = x\mathrm{e}^{-\frac{x^2}{2}}.</equation>（Ⅱ）分别计算<equation>y^{\prime}, y^{\prime\prime}.</equation><equation>y ^ {\prime} = \mathrm {e} ^ {- \frac {x ^ {2}}{2}} + x \cdot \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \cdot (- x) = \left(1 - x ^ {2}\right) \mathrm {e} ^ {- \frac {x ^ {2}}{2}},</equation><equation>y ^ {\prime \prime} = (- 2 x) \mathrm {e} ^ {- \frac {x ^ {2}}{2}} + \left(1 - x ^ {2}\right) \cdot \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \cdot (- x) = \left(x ^ {3} - 3 x\right) \mathrm {e} ^ {- \frac {x ^ {2}}{2}}.</equation>令<equation>y^{\prime \prime}=0</equation>，可得<equation>x=0</equation><equation>x=\pm \sqrt{3}</equation>.当<equation>x < -\sqrt{3}</equation>时，<equation>y^{\prime \prime} < 0</equation>；当<equation>-\sqrt{3} < x < 0</equation>时，<equation>y^{\prime \prime} > 0</equation>；当<equation>0 < x < \sqrt{3}</equation>时，<equation>y^{\prime \prime} < 0</equation>；当<equation>x > \sqrt{3}</equation>时，<equation>y^{\prime \prime} > 0.</equation>因此，<equation>y=y(x)</equation>的凹区间为<equation>(-\sqrt{3},0)</equation>和<equation>(\sqrt{3},+\infty)</equation>，凸区间为<equation>(-\infty,-\sqrt{3})</equation>和<equation>(0,\sqrt{3})</equation>。拐点共有3个：<equation>(-\sqrt{3},-\sqrt{3}\mathrm{e}^{-\frac{3}{2}}),(0,0),(\sqrt{3},\sqrt{3}\mathrm{e}^{-\frac{3}{2}}).</equation>

---

**2018年第18题 | 解答题 | 10分**
18. (本题满分10分)

已知微分方程<equation>y^{\prime}+y=f(x)</equation>，其中 f(x)是 R上的连续函数.

I. 若 f(x)=x，求方程的通解;

II. 若 f(x)是周期为 T的函数，证明：方程存在唯一的以 T为周期的解.
**答案: **（I）<equation>y=x-1+C\mathrm{e}^{-x}</equation>，其中C为任意常数； （Ⅱ）证明略.
**解析: **解（I）若<equation>f ( x )=x</equation>，则<equation>y^{\prime}+y=f ( x )</equation>是一阶非齐次线性微分方程根据求解公式，可得已知方程的通解为<equation>\begin{aligned} y &= \mathrm {e} ^ {- \int \mathrm {d} x} \left(\int x \cdot \mathrm {e} ^ {\int \mathrm {d} x} \mathrm {d} x + C\right) = \mathrm {e} ^ {- x} \left(\int x \cdot \mathrm {e} ^ {x} \mathrm {d} x + C\right) \\ &= \mathrm {e} ^ {- x} \left[ (x - 1) \mathrm {e} ^ {x} + C \right] = x - 1 + C \mathrm {e} ^ {- x}, \end{aligned}</equation>其中 C为任意常数.

（Ⅱ）下面证明方程<equation>y^{\prime} + y = f(x)</equation>的以<equation>T</equation>为周期的解存在.

根据求解公式，可得已知方程的通解为<equation>y (x) = \mathrm {e} ^ {- x} \left[ \int f (x) \mathrm {e} ^ {x} \mathrm {d} x + C ^ {\prime} \right] = \mathrm {e} ^ {- x} \left[ \int_ {0} ^ {x} f (t) \mathrm {e} ^ {t} \mathrm {d} t + C \right],</equation>其中 C为任意常数.

于是，<equation>\begin{aligned} y (x + T) &= \mathrm {e} ^ {- x - T} \left[ \int_ {0} ^ {x + T} f (t) \mathrm {e} ^ {t} \mathrm {d} t + C \right] = \mathrm {e} ^ {- x - T} \left[ \int_ {0} ^ {T} f (t) \mathrm {e} ^ {t} \mathrm {d} t + \int_ {T} ^ {x + T} f (t) \mathrm {e} ^ {t} \mathrm {d} t + C \right] \\ \underline {{= u = t - T}} \mathrm {e} ^ {- x - T} \left[ \int_ {0} ^ {T} f (t) \mathrm {e} ^ {t} \mathrm {d} t + \int_ {0} ^ {x} f (u + T) \mathrm {e} ^ {u + T} \mathrm {d} u + C \right] \\ \underline {{= \frac {f (u + T) = f (u)}{2}}} \mathrm {e} ^ {- x - T} \left[ \int_ {0} ^ {T} f (t) \mathrm {e} ^ {t} \mathrm {d} t + \mathrm {e} ^ {T} \int_ {0} ^ {x} f (u) \mathrm {e} ^ {u} \mathrm {d} u + C \right] \\ &= \mathrm {e} ^ {- x} \left[ \mathrm {e} ^ {- T} \int_ {0} ^ {T} f (t) \mathrm {e} ^ {t} \mathrm {d} t + \int_ {0} ^ {x} f (u) \mathrm {e} ^ {u} \mathrm {d} u + C \mathrm {e} ^ {- T} \right]. \end{aligned}</equation>比较 y(x)与 y(x+T).若<equation>\mathrm{e}^{-x}\left[ \mathrm{e}^{-T}\int_{0}^{T}f(t)\mathrm{e}^{t}\mathrm{d}t+\int_{0}^{x}f(u)\mathrm{e}^{u}\mathrm{d}u+C\mathrm{e}^{-T}\right]=\mathrm{e}^{-x}\left[ \int_{0}^{x}f(t)\mathrm{e}^{t}\mathrm{d}t+C\right]</equation>即<equation>\mathrm {e} ^ {- T} \int_ {0} ^ {T} f (t) \mathrm {e} ^ {t} \mathrm {d} t + G \mathrm {e} ^ {- T} = C,</equation>则<equation>y ( x+T)=y ( x ), y ( x )</equation>是以T为周期的解.解（1）式得<equation>C=\frac{\int_{0}^{T} f ( t ) \mathrm{e}^{t} \mathrm{d} t}{\mathrm{e}^{T}-1}.</equation>由于T为一常数，故C为一确定常数.

因此，若<equation>f(x)</equation>是周期为<equation>T</equation>的函数，则方程<equation>y^{\prime} + y = f(x)</equation>存在以<equation>T</equation>为周期的解.

下面证明方程<equation>y^{\prime} + y = f(x)</equation>的以<equation>T</equation>为周期的解唯一.

假设<equation>y_{1}, y_{2}</equation>是方程<equation>y^{\prime} + y = f(x)</equation>的两个不同的以<equation>T</equation>为周期的解，则<equation>y_{1} - y_{2}</equation>为齐次线性微分方程<equation>y^{\prime} + y = 0</equation>的解，且<equation>y_{1} - y_{2}</equation>也是以<equation>T</equation>为周期的函数. 解<equation>y^{\prime} + y = 0</equation>可得<equation>y = C_{0}\mathrm{e}^{-x}</equation>，其中<equation>C_{0}</equation>为任意常数. 于是，<equation>y_{1} - y_{2} = C_{0}\mathrm{e}^{-x}</equation>，但是该函数不是以<equation>T</equation>为周期的函数. 矛盾.

综上所述，若<equation>f ( x )</equation>是周期为<equation>T</equation>的函数，则方程<equation>y^{\prime}+y=f ( x )</equation>存在唯一的以<equation>T</equation>为周期的解.

---

**2016年第3题 | 选择题 | 4分 | 答案: A**
3. 若<equation>y=(1+x^{2})^{2}-\sqrt{1+x^{2}},</equation><equation>y=(1+x^{2})^{2}+\sqrt{1+x^{2}}</equation>是微分方程<equation>y^{\prime}+p(x)y=q(x)</equation>的两个解，则 q(x) =（    )

A.<equation>3 x(1+x^{2})</equation>B.<equation>- 3 x(1+x^{2})</equation>C.<equation>\frac{x}{1+x^{2}}</equation>D.<equation>- \frac{x}{1+x^{2}}</equation>
答案: A
**解析: **解 令<equation>y_{1}=(1+x^{2})^{2}-\sqrt{1+x^{2}}, y_{2}=(1+x^{2})^{2}+\sqrt{1+x^{2}}.</equation>由于<equation>y_{1}, y_{2}</equation>均是微分方程<equation>y^{\prime}+p(x)y=q(x)</equation>的解，故<equation>y_{2}-y_{1}=2\sqrt{1+x^{2}}</equation>是对应的齐次线性方程<equation>y^{\prime}+p(x)y=0</equation>的解.将解代入方程中得到<equation>\frac {2 x}{\sqrt {1 + x ^ {2}}} + 2 p (x) \sqrt {1 + x ^ {2}} = 0,</equation>从而<equation>p ( x ) = - \frac { x } { 1 + x ^ { 2 } } .</equation>由于<equation>y_{1}, y_{2}</equation>是微分方程<equation>y^{\prime}+p(x)y=q(x)</equation>的解，故<equation>\frac{y_{1}+y_{2}}{2}=(1+x^{2})^{2}</equation>也是该微分方程的解.将解代入方程中得到<equation>4 x \left(1 + x ^ {2}\right) - \frac {x}{1 + x ^ {2}} \cdot \left(1 + x ^ {2}\right) ^ {2} = q (x),</equation>即<equation>q ( x ) = 3 x \left( 1+x^{2} \right).</equation>应选A.

---

**2011年第10题 | 填空题 | 4分**
10. 微分方程<equation>y' + y = \mathrm{e}^{-x}\cos x</equation>满足条件<equation>y(0) = 0</equation>的解为<equation>y = \underline{\quad}</equation>
**解析: **利用求解公式可得，<equation>y=\mathrm{e}^{-\int\mathrm{d} x}\left(\int\mathrm{e}^{-x}\cos x\mathrm{e}^{\int\mathrm{d} x}\mathrm{d} x+C\right)=\mathrm{e}^{-x}\left(\int\cos x\mathrm{d} x+C\right)=\mathrm{e}^{-x}(\sin x+C).</equation>将 y(0) = 0 代入上式得到 C = 0，于是所求解为 y =<equation>\mathrm{e}^{-x}\sin x.</equation>

---


#### 其他方程

**2024年第14题 | 填空题 | 5分**

14. 微分方程<equation>y^{\prime}=\frac{1}{(x+y)^{2}}</equation>满足条件 y(1)=0的解为 ___

**答案:**<equation>\arctan (x + y) = y + \frac {\pi}{4}</equation>

**解析:**解 令<equation>u=x+y</equation>，则<equation>\frac{\mathrm{d}u}{\mathrm{d}x}=1+\frac{\mathrm{d}y}{\mathrm{d}x}</equation>，原方程化为<equation>\frac{\mathrm{d}u}{\mathrm{d}x}-1=\frac{1}{u^{2}}</equation>，即<equation>\frac{\mathrm{d}u}{\mathrm{d}x}=\frac{1+u^{2}}{u^{2}}.</equation>这是一个可分离变量的微分方程，分离变量可得<equation>\left(1-\frac{1}{1+u^{2}}\right)\mathrm{d}u=\mathrm{d}x.</equation>方程两端同时积分可得<equation>u-\arctan u=x+C.</equation>由<equation>y(1)=0</equation>可得，<equation>u(1)=1.</equation>代入<equation>u-\arctan u=x+C</equation>可得<equation>1-\frac{\pi}{4}=1+C,</equation>解得<equation>C=-\frac{\pi}{4}.</equation>于是，<equation>u-\arctan u=x-\frac{\pi}{4}.</equation>将<equation>u=x+y</equation>代回<equation>u-\arctan u=x-\frac{\pi}{4}</equation>并整理可得<equation>y-\arctan(x+y)+\frac{\pi}{4}=0.</equation>

---

**2021年第13题 | 填空题 | 5分**

13. 欧拉方程<equation>x^{2} y^{\prime \prime}+x y^{\prime}-4 y=0</equation>满足条件<equation>y(1)=1, y^{\prime}(1)=2</equation>的解为<equation>y=</equation>___.

**答案:**<equation>x^{2}.</equation>

**解析:**解 由初始条件<equation>y ( 1 ) = 1, y^{\prime} ( 1 ) = 2</equation>可知应在<equation>x > 0</equation>的范围内求解.

令<equation>x = \mathrm{e}^{t}</equation>. 于是，<equation>\frac {\mathrm {d} y}{\mathrm {d} t} = \frac {\mathrm {d} y}{\mathrm {d} x} \cdot \mathrm {e} ^ {t}.</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} t ^ {2}} = \frac {\mathrm {d} \left(\frac {\mathrm {d} y}{\mathrm {d} x} \cdot \mathrm {e} ^ {t}\right)}{\mathrm {d} t} = \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \cdot \frac {\mathrm {d} x}{\mathrm {d} t} \cdot \mathrm {e} ^ {t} + \frac {\mathrm {d} y}{\mathrm {d} x} \cdot \mathrm {e} ^ {t} = \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \cdot \mathrm {e} ^ {2 t} + \frac {\mathrm {d} y}{\mathrm {d} x} \cdot \mathrm {e} ^ {t} = \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \cdot \mathrm {e} ^ {2 t} + \frac {\mathrm {d} y}{\mathrm {d} t}.</equation>从而，<equation>y^{\prime} = \mathrm{e}^{-t}\frac{\mathrm{d}y}{\mathrm{d}t}, y^{\prime \prime} = \mathrm{e}^{-2t}\left(\frac{\mathrm{d}^{2}y}{\mathrm{d}t^{2}} - \frac{\mathrm{d}y}{\mathrm{d}t}\right).</equation>因此，<equation>xy^{\prime} = \frac{\mathrm{d}y}{\mathrm{d}t}, x^{2}y^{\prime \prime} = \frac{\mathrm{d}^{2}y}{\mathrm{d}t^{2}} - \frac{\mathrm{d}y}{\mathrm{d}t}.</equation>代入<equation>x^{2} y^{\prime \prime}+x y^{\prime}-4 y=0</equation>可得<equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} t ^ {2}} - \frac {\mathrm {d} y}{\mathrm {d} t} + \frac {\mathrm {d} y}{\mathrm {d} t} - 4 y = \frac {\mathrm {d} ^ {2} y}{\mathrm {d} t ^ {2}} - 4 y = 0.</equation><equation>\frac{\mathrm{d}^2y}{\mathrm{d}t^2} - 4y = 0</equation>是一个二阶常系数齐次线性微分方程，其特征方程为<equation>r^2 - 4 = 0</equation>，特征根为<equation>r_{1,2} = \pm 2.</equation>于是，该方程的解为<equation>y = C_{1}\mathrm{e}^{2t} + C_{2}\mathrm{e}^{-2t} = C_{1}x^{2} + C_{2}x^{-2}</equation>，其中<equation>C_{1},C_{2}</equation>为待定常数. 从而，<equation>y^{\prime} = 2C_{1}x - 2C_{2}x^{-3}.</equation>代入 y（1）=1可得<equation>1=C_{1}+C_{2}</equation>代入<equation>y^{\prime}(1)=2</equation>可得<equation>2=2 C_{1}-2 C_{2}</equation>解得<equation>C_{1}=1,C_{2}=0.</equation>综上所述，原方程的解为<equation>y=x^{2}.</equation>

---


#### 常系数齐次线性微分方程

**2023年第2题 | 选择题 | 5分 | 答案: C**

2. 若微分方程<equation>y^{\prime \prime}+ay^{\prime}+by=0</equation>的解在<equation>(-\infty,+\infty)</equation>上有界，则（    )

A. a < 0,b > 0 B. a > 0,b > 0 C. a = 0,b > 0 D. a = 0,b < 0

答案: C

**解析:**解 由于二阶常系数齐次线性微分方程必有零解，而零解为有界解，故微分方程<equation>y^{\prime \prime}+ay^{\prime}+by=0</equation>必然存在<equation>(-\infty , +\infty)</equation>上的有界解.本题实际上是要求此方程的所有解都有界.

微分方程<equation>y^{\prime \prime} + a y^{\prime} + b y = 0</equation>的特征方程为<equation>\lambda^{2} + a \lambda + b = 0.</equation>- 若<equation>\Delta=a^{2}-4 b>0</equation>，则特征方程有两个不同实根<equation>\lambda_{1},\lambda_{2}</equation>，从而至少有一个实根非零.此时，微分方程的解为<equation>y=C_{1}\mathrm{e}^{\lambda_{1}x}+C_{2}\mathrm{e}^{\lambda_{2}x}.</equation>取<equation>C_{1} = C_{2} = 1</equation>，则<equation>\lim_{x\to -\infty}\left(\mathrm{e}^{\lambda_{1}x} + \mathrm{e}^{\lambda_{2}x}\right) = +\infty</equation>或<equation>\lim_{x\to +\infty}\left(\mathrm{e}^{\lambda_{1}x} + \mathrm{e}^{\lambda_{2}x}\right) = +\infty</equation>. 该解在<equation>(-\infty , +\infty)</equation>上无界.

- 若<equation>\Delta=a^{2}-4 b=0</equation>，则特征方程有两个相同实根<equation>\lambda</equation>.此时，微分方程的解为<equation>y=(C_{1}+ C_{2} x) \mathrm{e}^{\lambda x}.</equation>取<equation>C_{1} = 0, C_{2} = 1</equation>，则<equation>\lim_{x\to -\infty}x\mathrm{e}^{\lambda x} = \infty</equation>或<equation>\lim_{x\to +\infty}x\mathrm{e}^{\lambda x} = \infty</equation>. 该解在<equation>(-\infty , +\infty)</equation>上无界.

- 若<equation>\Delta=a^{2}-4 b<0</equation>，则特征方程有一对共轭复根<equation>\lambda_{1,2}=\alpha\pm\beta\mathrm{i}</equation>.此时，微分方程的解为<equation>y=\mathrm{e}^{\alpha x}\left(C_{1}\cos \beta x+C_{2}\sin \beta x\right).</equation>当<equation>\alpha \neq 0</equation>时，取<equation>C_{1} = 1, C_{2} = 0</equation>，所得解<equation>y = \mathrm{e}^{\alpha x}\cos \beta x</equation>是<equation>(-\infty , + \infty)</equation>上的无界函数.

当<equation>\alpha=0</equation>时，微分方程的解为<equation>y=C_{1}\cos \beta x+C_{2}\sin \beta x</equation>.对任意常数<equation>C_{1},C_{2}</equation>，该解在<equation>(-\infty, +\infty)</equation>上均有界.根据求根公式，<equation>\lambda_{1,2}=-\frac{a}{2}\pm \frac{\sqrt{4b-a^{2}}}{2}\mathrm{i}</equation>，即<equation>\alpha=-\frac{a}{2}.</equation>于是，<equation>a=0.</equation>结合<equation>a^{2}-4b<0</equation>可知，<equation>b>0.</equation>因此，<equation>a=0,b>0.</equation>应选C.

---

**2020年第11题 | 填空题 | 4分**

11. 设函数 f(x)满足<equation>f^{\prime\prime}(x)+af^{\prime}(x)+f(x)=0(a>0)</equation>，且 f(0)=m，<equation>f^{\prime}(0)=n</equation>，则<equation>\int_{0}^{+\infty}f(x)\mathrm{d}x=</equation>___

**答案:**## n+am.

**解析:**解 原方程的特征方程为<equation>r^{2}+ar+1=0</equation>. 该方程的判别式<equation>\Delta=a^{2}-4</equation>. 下面根据 a 的取值讨论解的情况.<equation>\textcircled{1}</equation>a > 2.<equation>r^{2}+ar+1=0</equation>有两个不同实根<equation>r_{1,2}=\frac{-a\pm \sqrt{a^{2}-4}}{2}, r_{1}, r_{2}</equation>均小于零. 原方程的解为<equation>f(x)=</equation><equation>C_{1}\mathrm{e}^{r_{1}x}+C_{2}\mathrm{e}^{r_{2}x}</equation>，其中<equation>C_{1},C_{2}</equation>为待定常数.<equation>f^{\prime}(x)=C_{1}r_{1}\mathrm{e}^{r_{1}x}+C_{2}r_{2}\mathrm{e}^{r_{2}x}.</equation><equation>\textcircled{2}</equation>a=2.<equation>r^{2}+2 r+1=0</equation>有两个相同实根<equation>r_{1,2}=-1</equation>. 原方程的解为<equation>f(x)=\left(C_{1}+C_{2}x\right)\mathrm{e}^{-x}</equation>，其中<equation>C_{1},C_{2}</equation>为待定常数.<equation>f^{\prime}(x)=\left(C_{2}-C_{1}-C_{2}x\right)\mathrm{e}^{-x}.</equation><equation>\textcircled{3}</equation>0 < a < 2.<equation>r^{2}+ar+1=0</equation>有一对共轭复根<equation>r_{1,2}=-\frac{a}{2}\pm b\mathrm{i}</equation>，其中<equation>b=\frac{\sqrt{4-a^{2}}}{2}</equation>原方程的解为<equation>f(x)=</equation><equation>\mathrm{e}^{-\frac{a}{2}x}\left(C_{1}\cos bx+C_{2}\sin bx\right)</equation>，其中<equation>C_{1},C_{2}</equation>为待定常数.<equation>f^{\prime}(x)</equation>的形式与f(x)的形式相同.

不论是哪种情况，由<equation>a > 0</equation>均可得<equation>\lim_{x\to +\infty}f(x) = 0,\lim_{x\to +\infty}f^{\prime}(x) = 0.</equation>由<equation>f^{\prime \prime}(x) + af^{\prime}(x) + f(x) = 0</equation>可得，<equation>f(x) = -f^{\prime \prime}(x) - af^{\prime}(x)</equation>. 因此，<equation>\begin{aligned} \int_ {0} ^ {+ \infty} f (x) \mathrm {d} x &= \int_ {0} ^ {+ \infty} \left[ - f ^ {\prime \prime} (x) - a f ^ {\prime} (x) \right] \mathrm {d} x = \left[ - f ^ {\prime} (x) - a f (x) \right] \Bigg | _ {0} ^ {+ \infty} \\ &= \lim _ {x \rightarrow + \infty} \left[ - f ^ {\prime} (x) - a f (x) \right] - \left[ - f ^ {\prime} (0) - a f (0) \right] \\ &= f ^ {\prime} (0) + a f (0) = n + a m. \end{aligned}</equation>

---

**2017年第10题 | 填空题 | 4分**

10. 微分方程<equation>y'' + 2y' + 3y = 0</equation>的通解为<equation>y = \_\_\_</equation>

**答案:**<equation>\mathrm{e}^{-x}\left(C_1\cos \sqrt{2} x + C_2\sin \sqrt{2} x\right)</equation>，其中<equation>C_{1}, C_{2}</equation>为任意常数.

**解析:**解 原方程的特征方程为<equation>\lambda^{2}+2\lambda+3=0</equation>，解得<equation>\lambda_{1,2}=-1\pm \sqrt{2}\mathrm{i}</equation>，于是所求通解为<equation>y=\mathrm{e}^{-x}\left(C_{1}\cos \sqrt{2} x+C_{2}\sin \sqrt{2} x\right)</equation>其中<equation>C_{1}, C_{2}</equation>为任意常数.

---

**2016年第16题 | 解答题 | 10分**

16. (本题满分10分)

设函数 y(x)满足方程<equation>y^{\prime\prime}+2 y^{\prime}+k y=0</equation>，其中 0 < k < 1.

I. 证明：反常积分<equation>\int_{0}^{+\infty} y(x)\mathrm{d}x</equation>收敛；

II. 若 y(0)=1，<equation>y^{\prime}(0)=1</equation>，求<equation>\int_{0}^{+\infty} y(x)\mathrm{d}x</equation>的值.

**答案:**（ I ）证明略. （ II ）<equation>\frac{3}{k}</equation>

**解析:**解（I）原方程的特征方程为<equation>\lambda^{2}+2\lambda+k=0</equation>.由于<equation>0 < k < 1</equation>，故<equation>\Delta = 4 - 4 k > 0</equation>，从而解得<equation>\lambda_{1,2}=-1\pm \sqrt{1-k}<0</equation>.于是<equation>y (x) = C _ {1} \mathrm {e} ^ {\lambda_ {1} x} + C _ {2} \mathrm {e} ^ {\lambda_ {2} x},</equation><equation>\begin{aligned} \int_ {0} ^ {+ \infty} y (x) \mathrm {d} x &= \int_ {0} ^ {+ \infty} \left(C _ {1} \mathrm {e} ^ {\lambda_ {1} x} + C _ {2} \mathrm {e} ^ {\lambda_ {2} x}\right) \mathrm {d} x = \left. \left(\frac {C _ {1}}{\lambda_ {1}} \mathrm {e} ^ {\lambda_ {1} x} + \frac {C _ {2}}{\lambda_ {2}} \mathrm {e} ^ {\lambda_ {2} x}\right) \right| _ {0} ^ {+ \infty} \\ &= 0 - \frac {C _ {1}}{\lambda_ {1}} + 0 - \frac {C _ {2}}{\lambda_ {2}} = - \left(\frac {C _ {1}}{\lambda_ {1}} + \frac {C _ {2}}{\lambda_ {2}}\right). \end{aligned}</equation>因此，<equation>\int_{0}^{+\infty} y ( x ) \mathrm{d} x</equation>收敛，结论得证.

（Ⅱ）（法一）由<equation>y^{\prime \prime}+2y^{\prime}+ky=0</equation>可得，<equation>\begin{array}{l} \int_ {0} ^ {+ \infty} y (x) \mathrm {d} x = \int_ {0} ^ {+ \infty} \frac {- \left[ y ^ {\prime \prime} (x) + 2 y ^ {\prime} (x) \right]}{k} \mathrm {d} x = - \frac {1}{k} \left[ y ^ {\prime} (x) + 2 y (x) \right] \Bigg | _ {0} ^ {+ \infty} \\ = - \frac {1}{k} \left\{\lim _ {x \rightarrow + \infty} \left[ y ^ {\prime} (x) + 2 y (x) \right] - \left[ y ^ {\prime} (0) + 2 y (0) \right]\right\}. \\ \end{array}</equation>由第（Ⅰ）问知，<equation>\lim _ {x \rightarrow + \infty} y (x) = \lim _ {x \rightarrow + \infty} \left(C _ {1} \mathrm {e} ^ {\lambda_ {1} x} + C _ {2} \mathrm {e} ^ {\lambda_ {2} x}\right) = 0,</equation><equation>\lim _ {x \rightarrow + \infty} y ^ {\prime} (x) = \lim _ {x \rightarrow + \infty} \left(C _ {1} \lambda_ {1} \mathrm {e} ^ {\lambda_ {1} x} + C _ {2} \lambda_ {2} \mathrm {e} ^ {\lambda_ {2} x}\right) = 0.</equation>代入<equation>y (0) = 1, y^{\prime} (0) = 1</equation>，可得<equation>\int_0^{+\infty} y (x)\mathrm{d}x = -\frac{1}{k} (0 - 1 - 2) = \frac{3}{k}.</equation>（法二）由<equation>y(x) = C_{1}\mathrm{e}^{\lambda_{1}x} + C_{2}\mathrm{e}^{\lambda_{2}x}</equation>知，<equation>y ^ {\prime} (x) = C _ {1} \lambda_ {1} \mathrm {e} ^ {\lambda_ {1} x} + C _ {2} \lambda_ {2} \mathrm {e} ^ {\lambda_ {2} x}.</equation>将<equation>y(0) = 1, y^{\prime}(0) = 1</equation>代入<equation>y(x)</equation>与<equation>y^{\prime}(x)</equation>的表达式中，得到<equation>\left\{ \begin{array}{l} C _ {1} + C _ {2} = 1, \\ C _ {1} \lambda_ {1} + C _ {2} \lambda_ {2} = 1. \end{array} \right.</equation>将<equation>C_{2} = 1 - C_{1}</equation>代入<equation>C_{1}\lambda_{1} + C_{2}\lambda_{2} = 1</equation>，解得<equation>C_{1} = \frac{1 - \lambda_{2}}{\lambda_{1} - \lambda_{2}}</equation>，从而<equation>C_{2} = 1 - C_{1} = \frac{\lambda_{1} - \lambda_{2} - 1 + \lambda_{2}}{\lambda_{1} - \lambda_{2}} = \frac{\lambda_{1} - 1}{\lambda_{1} - \lambda_{2}}</equation>.于是，<equation>\begin{aligned} \int_ {0} ^ {+ \infty} y (x) \mathrm {d} x &= - \frac {C _ {1}}{\lambda_ {1}} - \frac {C _ {2}}{\lambda_ {2}} = \frac {\lambda_ {2} - 1}{\lambda_ {1} - \lambda_ {2}} \cdot \frac {1}{\lambda_ {1}} + \frac {1 - \lambda_ {1}}{\lambda_ {1} - \lambda_ {2}} \cdot \frac {1}{\lambda_ {2}} = \frac {\left(\lambda_ {2} - 1\right) \lambda_ {2} + \left(1 - \lambda_ {1}\right) \lambda_ {1}}{\lambda_ {1} \lambda_ {2} \left(\lambda_ {1} - \lambda_ {2}\right)} \\ &= \frac {\lambda_ {2} ^ {2} - \lambda_ {1} ^ {2} + \lambda_ {1} - \lambda_ {2}}{\lambda_ {1} \lambda_ {2} \left(\lambda_ {1} - \lambda_ {2}\right)} = \frac {1 - \left(\lambda_ {1} + \lambda_ {2}\right)}{\lambda_ {1} \lambda_ {2}}. \end{aligned}</equation>由于<equation>\lambda_{1},\lambda_{2}</equation>为特征方程<equation>\lambda^{2} + 2\lambda +k = 0</equation>的两个根，故<equation>\lambda_{1} + \lambda_{2} = -2,\lambda_{1}\lambda_{2} = k.</equation>因此，<equation>\int_0^{+\infty}y(x)\mathrm{d}x = \frac{1 - (-2)}{k} = \frac{3}{k}</equation>.

---

**2012年第9题 | 填空题 | 4分**

9. 若函数<equation>f(x)</equation>满足方程<equation>f^{\prime\prime}(x)+f^{\prime}(x)-2f(x)=0</equation>及<equation>f^{\prime\prime}(x)+f(x)=2\mathrm{e}^{x}</equation>，则<equation>f(x)=</equation>___.

**解析:**解（法一）由题设知，<equation>f(x)</equation>满足二阶常系数齐次线性微分方程<equation>y^{\prime \prime}+y^{\prime}-2y=0.</equation>其特征方程为<equation>\lambda^{2}+\lambda-2=0</equation>，解得<equation>\lambda_{1}=1,\lambda_{2}=-2</equation>，于是<equation>f(x)=C_{1}\mathrm{e}^{x}+C_{2}\mathrm{e}^{-2x}</equation>其中<equation>C_{1},C_{2}</equation>为待定常数.将<equation>f(x)</equation>的表达式代入<equation>f^{\prime \prime}(x)+f(x)=2\mathrm{e}^{x}</equation>中，得到<equation>C _ {1} \mathrm {e} ^ {x} + 4 C _ {2} \mathrm {e} ^ {- 2 x} + C _ {1} \mathrm {e} ^ {x} + C _ {2} \mathrm {e} ^ {- 2 x} = 2 \mathrm {e} ^ {x}.</equation>化简得<equation>2 C _ {1} \mathrm {e} ^ {x} + 5 C _ {2} \mathrm {e} ^ {- 2 x} = 2 \mathrm {e} ^ {x}.</equation>于是<equation>2C_{1} = 2,5C_{2} = 0</equation>，从而<equation>C_{1} = 1,C_{2} = 0.</equation>故<equation>f(x) = \mathrm{e}^{x}.</equation>（法二）由<equation>\left\{ \begin{array}{l} f^{\prime \prime}(x) + f^{\prime}(x) - 2f(x) = 0, \\ f^{\prime \prime}(x) + f(x) = 2\mathrm{e}^{x} \end{array} \right.</equation>得到<equation>f^{\prime}(x) - 3f(x) = -2\mathrm{e}^{x}</equation>. 由一阶非齐次线性微分方程的求解公式知，<equation>f (x) = \mathrm {e} ^ {\int 3 \mathrm {d} x} \left[ \int (- 2 \mathrm {e} ^ {x}) \mathrm {e} ^ {- \int 3 \mathrm {d} x} \mathrm {d} x + C \right] = \mathrm {e} ^ {3 x} \left(\mathrm {e} ^ {- 2 x} + C\right) = \mathrm {e} ^ {x} + C \mathrm {e} ^ {3 x}, C \text {为待 定 常 数}.</equation>将<equation>f ( x )</equation>的表达式代入<equation>f^{\prime \prime} ( x )+f^{\prime} ( x )-2 f ( x )=0</equation>中，得到<equation>1 0 C \mathrm{e}^{3 x}=0</equation>即有<equation>C=0</equation>（或者将<equation>f ( x )</equation>的表达式代入<equation>f^{\prime \prime} ( x )+f ( x )=2 \mathrm{e}^{x}</equation>中，同样可得<equation>C=0 )</equation>.于是<equation>f (x) = \mathrm {e} ^ {x}.</equation>

---


#### 微分方程的应用

**2023年第17题 | 解答题 | 10分**

17. (本题满分10分)

设曲线<equation>y=y(x)(x>0)</equation>经过点(1,2)，该曲线上任一点 P(x,y)到 y轴的距离等于该点处的切线在 y轴上的截距.

I. 求 y(x);

II. 求函数<equation>f(x)=\int_{1}^{x} y(t)\mathrm{d} t</equation>在（0，+∞）上的最大值.

**答案:**<equation>\begin{array}{l} (\mathrm {I}) y (x) = x (2 - \ln x); \\ (\mathrm {I I}) \frac {1}{4} \mathrm {e} ^ {4} - \frac {5}{4}. \\ \end{array}</equation>

**解析:**解（I）由导数的几何意义可知，点<equation>P(x,y)</equation>处的切线方程为<equation>Y-y=y^{\prime}(X-x).</equation>该点到y轴的距离为<equation>|x|\overset{x>0}{=}x.</equation>令<equation>X=0</equation>，可得<equation>Y=y-xy^{\prime}</equation>.由点<equation>P(x,y)</equation>到y轴的距离等于该点处的切线在y轴上的截距可得<equation>x=y-xy^{\prime}</equation>.整理可得<equation>y^{\prime}-\frac{y}{x}=-1</equation>.由一阶非齐次线性微分方程的通解公式可得<equation>\begin{aligned} y &= \mathrm {e} ^ {\int \frac {1}{x} \mathrm {d} x} \left[ \int (- 1) \mathrm {e} ^ {- \int \frac {1}{x} \mathrm {d} x} \mathrm {d} x + C \right] = \mathrm {e} ^ {\ln x} \left(- \int \mathrm {e} ^ {- \ln x} \mathrm {d} x + C\right) \\ &= x \left(- \int \frac {1}{x} \mathrm {d} x + C\right) = x (C - \ln x). \end{aligned}</equation>代入<equation>x = 1, y = 2</equation>可得<equation>C = 2</equation>. 因此，<equation>y(x) = x(2 - \ln x)</equation>.

（Ⅱ）由第（I）问的结果可知，<equation>f ( x ) = \int_{1}^{x} t ( 2 - \ln t ) \mathrm{d} t.</equation>由变限积分的求导公式可得<equation>f^{\prime}(x) = x(2 - \ln x)</equation>. 解<equation>2 - \ln x = 0</equation>可得<equation>x = \mathrm{e}^{2}</equation>. 于是，<equation>x = \mathrm{e}^{2}</equation>为<equation>f(x)</equation>在<equation>(0, + \infty)</equation>上的唯一驻点.当<equation>0 < x < \mathrm{e}^{2}</equation>时，<equation>f^{\prime}(x) > 0</equation>，<equation>f(x)</equation>单调增加；当<equation>x > \mathrm{e}^{2}</equation>时，<equation>f^{\prime}(x) < 0</equation>，<equation>f(x)</equation>单调减少.<equation>x = \mathrm{e}^{2}</equation>为<equation>f(x)</equation>在<equation>(0, + \infty)</equation>上的最大值点，最大值为<equation>\begin{aligned} f \left(\mathrm {e} ^ {2}\right) &= \int_ {1} ^ {\mathrm {e} ^ {2}} t (2 - \ln t) \mathrm {d} t = \frac {1}{2} \int_ {1} ^ {\mathrm {e} ^ {2}} (2 - \ln t) \mathrm {d} \left(t ^ {2}\right) = \frac {1}{2} t ^ {2} (2 - \ln t) \left| _ {1} ^ {\mathrm {e} ^ {2}} - \frac {1}{2} \int_ {1} ^ {\mathrm {e} ^ {2}} t ^ {2} \cdot \left(- \frac {1}{t}\right) \mathrm {d} t \right. \\ &= 0 - 1 + \frac {1}{2} \int_ {1} ^ {\mathrm {e} ^ {2}} t \mathrm {d} t = - 1 + \frac {1}{4} t ^ {2} \Bigg | _ {1} ^ {\mathrm {e} ^ {2}} = \frac {1}{4} \mathrm {e} ^ {4} - \frac {5}{4}. \end{aligned}</equation>

---

**2015年第16题 | 解答题 | 10分**

16. (本题满分10分)

设函数 f(x)在定义域 I上的导数大于零.若对任意的<equation>x_{0}\in I</equation>，曲线 y=f(x)在点<equation>\left(x_{0},f\left(x_{0}\right)\right)</equation>处的切线与直线<equation>x=x_{0}</equation>及 x轴所围成区域的面积恒为4，且 f(0)=2，求 f(x)的表达式.

**答案:**<equation>1 6) f (x) = \frac {8}{4 - x}, x \in I.</equation>

**解析:**解如图所示，曲线<equation>y=f(x)</equation>在点<equation>\left(x_{0},f\left(x_{0}\right)\right)</equation>处的切线为<equation>y - f \left(x _ {0}\right) = f ^ {\prime} \left(x _ {0}\right) \left(x - x _ {0}\right).</equation>令<equation>y = 0</equation>，注意到<equation>f^{\prime}(x) > 0</equation>，解得<equation>x = x_{0} - \frac{f(x_{0})}{f^{\prime}(x_{0})}</equation>，即该切线与<equation>x</equation>轴的交点为<equation>\left(x_0 - \frac{f(x_0)}{f^{\prime}(x_0)},0\right)</equation>.

曲线<equation>y=f(x)</equation>在点<equation>\left(x_{0},f\left(x_{0}\right)\right)</equation>处的切线与直线<equation>x=x_{0}</equation>及x轴所围成区域为三角形，底边长<equation>\left|x_{0}-\left[x_{0}-\frac{f\left(x_{0}\right)}{f^{\prime}\left(x_{0}\right)}\right]\right|</equation>，高<equation>|f(x_{0})-0|</equation>.于是，<equation>\frac {\left| f \left(x _ {0}\right) - 0 \right| \cdot \left| x _ {0} - \left[ x _ {0} - \frac {f \left(x _ {0}\right)}{f ^ {\prime} \left(x _ {0}\right)} \right] \right|}{2} = 4, \quad \text {即} \frac {\left| f \left(x _ {0}\right) \right| \cdot \left| \frac {f \left(x _ {0}\right)}{f ^ {\prime} \left(x _ {0}\right)} \right|}{2} = 4.</equation>由于<equation>f^{\prime}(x) > 0</equation>，故<equation>\frac {\left[ f \left(x _ {0}\right) \right] ^ {2}}{f ^ {\prime} \left(x _ {0}\right)} = 8, \quad x _ {0} \in I,</equation>即<equation>f(x)</equation>满足微分方程<equation>8y^{\prime} = y^{2}</equation>.

分离变量，得<equation>\frac{8}{y^{2}}\mathrm{d}y=\mathrm{d}x.</equation>方程两端积分，得<equation>-\frac{8}{y}=x+C</equation>其中C为待定常数.由于<equation>f(0)=2</equation>故C=-4，从而<equation>y=\frac{8}{4-x}.</equation>因此，<equation>f (x) = \frac {8}{4 - x}, \quad x \in I.</equation>

---


#### 可分离变量的微分方程与齐次方程

**2019年第10题 | 填空题 | 4分**

10. 微分方程<equation>2 y y^{\prime}-y^{2}-2=0</equation>满足条件<equation>y(0)=1</equation>的特解<equation>y=</equation>___

**解析:**解 整理原方程可得<equation>2 y \frac{\mathrm{d} y}{\mathrm{d} x}=y^{2}+2.</equation>分离变量可得<equation>\frac{2 y}{y^{2}+2}\mathrm{d} y=\mathrm{d} x.</equation>方程两端积分，<equation>\int \frac{2 y}{y^{2}+2}\mathrm{d} y=\int \frac{\mathrm{d}\left(y^{2}+2\right)}{y^{2}+2}=\ln \left(y^{2}+2\right)=x+C,</equation>其中 C为待定常数.

代入 x=0，<equation>y(0)=1</equation>可得，<equation>C=\ln 3</equation>.于是，<equation>y^{2}+2=3\mathrm{e}^{x}.</equation>又因为<equation>y(0)=1>0</equation>，所以<equation>y=\sqrt{3\mathrm{e}^{x}-2}.</equation>

---

**2014年第11题 | 填空题 | 4分**

11. 微分方程<equation>x y^{\prime}+y(\ln x-\ln y)=0</equation>满足条件<equation>y(1)=\mathrm{e}^{3}</equation>的解为<equation>y=</equation>___.

**答案:**##<equation>x \mathrm{e}^{2 x+1}.</equation>

**解析:**解 由题设中微分方程的表达式知 x > 0，y > 0，且原方程可化为<equation>y ^ {\prime} = \frac {y}{x} \ln \frac {y}{x},</equation>此为齐次方程. 令<equation>u=\frac{y}{x}</equation>，则<equation>y=ux,\frac{\mathrm{d}y}{\mathrm{d}x}=u+x\frac{\mathrm{d}u}{\mathrm{d}x}</equation>，于是方程（1）化为<equation>u + x \frac {\mathrm {d} u}{\mathrm {d} x} = u \ln u.</equation>分离变量，得到<equation>\frac {\mathrm {d} u}{u (\ln u - 1)} = \frac {\mathrm {d} x}{x},</equation>即<equation>\frac {\mathrm {d} (\ln u - 1)}{\ln u - 1} = \frac {\mathrm {d} x}{x}.</equation>对上式两端积分，得到于是<equation>\begin{aligned} \ln | \ln u - 1 | &= \ln x + C _ {1}, \\ \ln u - 1 &= C x, \end{aligned}</equation>其中<equation>C = \pm \mathrm{e}^{C_1}</equation>. 代回原变量<equation>u = \frac{y}{x}</equation>，得到原方程的通解为

注意这里由于 x > 0，y > 0，故 u > 0从而<equation>\int \frac{1}{u}=\ln u+C</equation>，但由于<equation>\ln u-1</equation>的正负无法判断，故<equation>\int \frac {\mathrm {d} (\ln u - 1)}{\ln u - 1} = \ln | \ln u - 1 | + C.</equation><equation>\ln \frac {y}{x} - 1 = C x.</equation>将<equation>y ( 1 ) = \mathrm{e}^{3}</equation>代入上式，得到<equation>C=2</equation>，于是<equation>\ln \frac{y}{x}=2x+1</equation>，从而所求初值问题的解为<equation>y = x \mathrm {e} ^ {2 x + 1}.</equation>

---


#### 常系数非齐次线性微分方程

**2015年第2题 | 选择题 | 4分 | 答案: A**

2. 设<equation>y=\frac{1}{2}\mathrm{e}^{2 x}+\left(x-\frac{1}{3}\right)\mathrm{e}^{x}</equation>是二阶常系数非齐次线性微分方程<equation>y^{\prime \prime}+ay^{\prime}+by=c\mathrm{e}^{x}</equation>的一个特解，则（    )

A. a=-3,b=2,c=-1 B. a=3,b=2,c=-1 C. a=-3,b=2,c=1 D. a=3,b=2,c=1

答案: A

**解析:**解（法一）将<equation>y=\frac{1}{2}\mathrm{e}^{2x}+\left(x-\frac{1}{3}\right)\mathrm{e}^{x}</equation>代入<equation>y^{\prime \prime}+ay^{\prime}+by=c\mathrm{e}^{x}</equation>中，整理得到<equation>\left(2+a+\frac{1}{2}b\right)\mathrm{e}^{2x}+\left(1+a+b\right)x\mathrm{e}^{x}+\left(\frac{5}{3}+\frac{2}{3}a-\frac{1}{3}b\right)\mathrm{e}^{x}=c\mathrm{e}^{x}.</equation>比较上式两端系数，得到<equation>\left\{ \begin{array}{l l} 2+a+\frac{1}{2}b=0, \\ 1+a+b=0, \\ \frac{5}{3}+\frac{2}{3}a-\frac{1}{3}b=c, \end{array} \right.</equation>解得<equation>\left\{ \begin{array}{l l} a=-3, \\ b=2, \\ c=-1, \end{array} \right.</equation>故选A.

（法二）方程<equation>y^{\prime \prime}+a y^{\prime}+b y=c \mathrm{e}^{x}</equation>的特解可设为<equation>y^{*} = a_{0} x^{l} \mathrm{e}^{x}</equation>，其中当1不是特征方程的根时，l取0；当1是特征方程的单根时，l取1；当1是特征方程的重根时，l取2，因此得到如下表格.

<table border="1"><tr><td colspan="2"></td><td>1不是特征方程的根</td><td>1是特征方程的单根</td><td>1是特征方程的重根</td></tr><tr><td rowspan="3">非齐次线性方程的通解</td><td><equation>\lambda_{1}\neq\lambda_{2}</equation></td><td><equation>C_{1}\mathrm{e}^{\lambda_{1}x}+C_{2}\mathrm{e}^{\lambda_{2}x}+a_{0}\mathrm{e}^{x}</equation><equation>\lambda_{1}\neq1,\lambda_{2}\neq1</equation></td><td><equation>C_{1}\mathrm{e}^{x}+C_{2}\mathrm{e}^{\lambda_{2}x}+a_{0}x\mathrm{e}^{x}</equation><equation>\lambda_{1}=1,\lambda_{2}\neq1</equation></td><td>-</td></tr><tr><td><equation>\lambda_{1}=\lambda_{2}</equation></td><td><equation>C_{1}\mathrm{e}^{\lambda_{1}x}+C_{2}x\mathrm{e}^{\lambda_{1}x}+a_{0}\mathrm{e}^{x}</equation><equation>\lambda_{1}\neq1</equation></td><td>-</td><td><equation>C_{1}\mathrm{e}^{x}+C_{2}x\mathrm{e}^{x}+a_{0}x^{2}\mathrm{e}^{x}</equation></td></tr><tr><td><equation>\lambda_{1,2}=\alpha\pm\beta\mathrm{i}</equation></td><td><equation>\mathrm{e}^{\alpha x}(C_{1}\cos\beta x+C_{2}\sin\beta x)+a_{0}\mathrm{e}^{x}</equation></td><td>-</td><td>-</td></tr></table>

又<equation>y=\frac{1}{2}\mathrm{e}^{2x}+\left(x-\frac{1}{3}\right)\mathrm{e}^{x}</equation>是非齐次线性方程的一个特解，对比上述表格可知，非齐次线性方程的通解应为<equation>y=C_{1}\mathrm{e}^{x}+C_{2}\mathrm{e}^{\lambda_{2}x}+a_{0}x\mathrm{e}^{x}</equation>的形式.再由特解的表达式可知，<equation>\lambda_{1}=1,\lambda_{2}=2,a_{0}=1</equation>从而<equation>a=-\left(\lambda_{1}+\lambda_{2}\right)=-3,b=\lambda_{1}\lambda_{2}=2.</equation>将<equation>y^{*} = x\mathrm{e}^{x}</equation>代入方程<equation>y^{\prime \prime}-3y^{\prime}+2y=c\mathrm{e}^{x}</equation>中，可得c=-1，故选A.

---

**2014年第17题 | 解答题 | 10分**

17. (本题满分10分）

设函数 f(u)具有二阶连续导数，<equation>z=f(\mathrm{e}^{x}\cos y)</equation>满足<equation>\frac{\partial^{2} z}{\partial x^{2}}+\frac{\partial^{2} z}{\partial y^{2}}=(4 z+\mathrm{e}^{x}\cos y)\mathrm{e}^{2 x}.</equation>若 f(0)=0，<equation>f^{\prime}(0)=0</equation>求 f(u)的表达式.

**答案:**17)<equation>f(u)</equation><equation>= \frac {1}{1 6} \mathrm {e} ^ {2 u} - \frac {1}{1 6} \mathrm {e} ^ {- 2 u} - \frac {1}{4} u.</equation>

**解析:**解分别计算<equation>\frac{\partial^{2} z}{\partial x^{2}}</equation>和<equation>\frac{\partial^{2} z}{\partial y^{2}}.</equation><equation>\frac {\partial z}{\partial x} = \cos y \mathrm {e} ^ {x} f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right), \quad \frac {\partial^ {2} z}{\partial x ^ {2}} = \cos y \mathrm {e} ^ {x} f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right) + \cos^ {2} y \mathrm {e} ^ {2 x} f ^ {\prime \prime} \left(\mathrm {e} ^ {x} \cos y\right),</equation><equation>\frac {\partial z}{\partial y} = - \sin y \mathrm {e} ^ {x} f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right), \quad \frac {\partial^ {2} z}{\partial y ^ {2}} = - \cos y \mathrm {e} ^ {x} f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right) + \sin^ {2} y \mathrm {e} ^ {2 x} f ^ {\prime \prime} \left(\mathrm {e} ^ {x} \cos y\right).</equation>由<equation>\frac{\partial^{2} z}{\partial x^{2}}+\frac{\partial^{2} z}{\partial y^{2}}=(4 z+ \mathrm{e}^{x} \cos y) \mathrm{e}^{2 x}</equation>可得<equation>\mathrm {e} ^ {2 x} f ^ {\prime \prime} \left(\mathrm {e} ^ {x} \cos y\right) = \left[ 4 f \left(\mathrm {e} ^ {x} \cos y\right) + \mathrm {e} ^ {x} \cos y \right] \mathrm {e} ^ {2 x},</equation>即<equation>f ^ {\prime \prime} \left(\mathrm {e} ^ {x} \cos y\right) = 4 f \left(\mathrm {e} ^ {x} \cos y\right) + \mathrm {e} ^ {x} \cos y.</equation>我们得到一个二阶常系数非齐次线性微分方程<equation>f^{\prime \prime}(u) - 4f(u) = u.</equation>该方程对应的齐次方程的特征方程为<equation>r^{2}-4=0</equation>，因而解为<equation>f(u)=C_{1}\mathrm{e}^{2u}+C_{2}\mathrm{e}^{-2u}</equation>，其中<equation>C_{1},C_{2}</equation>为待定常数.

由于0不是特征方程的根，故<equation>f^{\prime \prime}(u) - 4 f(u) = u</equation>有形如<equation>z^{*} = C_{3} u + C_{4}</equation>的特解.代入原方程得<equation>- 4 C_{3} u - 4 C_{4} = u.</equation>于是<equation>C_{3} = -\frac{1}{4}, C_{4} = 0.</equation>因此，原方程的解为<equation>f (u) = C _ {1} \mathrm {e} ^ {2 u} + C _ {2} \mathrm {e} ^ {- 2 u} - \frac {1}{4} u.</equation>代入初值以确定<equation>C_{1}, C_{2}</equation>的值.由<equation>f(0)=0</equation>得，<equation>C_{1}+C_{2}=0.</equation>由<equation>f^{\prime}(0)=0</equation>得，<equation>2 C_{1}-2 C_{2}-\frac{1}{4}=0.</equation>从而解得<equation>C_{1}=\frac{1}{1 6}, C_{2}=-\frac{1}{1 6}.</equation>因此，<equation>f ( u ) = \frac { 1 } { 1 6 } \mathrm { e } ^ { 2 u } - \frac { 1 } { 1 6 } \mathrm { e } ^ { - 2 u } - \frac { 1 } { 4 } u .</equation>

---

**2010年第15题 | 解答题 | 10分**

15. (本题满分10分）

求微分方程<equation>y^{\prime \prime}-3 y^{\prime}+2 y=2 x \mathrm{e}^{x}</equation>的通解.

**答案:**(15)<equation>y = C_{1}\mathrm{e}^{x} + C_{2}\mathrm{e}^{2x} - (x^{2} + 2x)\mathrm{e}^{x}</equation>，其中<equation>C_{1}, C_{2}</equation>为任意常数.

**解析:**应的齐次线性方程<equation>y^{\prime \prime}-3 y^{\prime}+2 y=0</equation>的特征方程为<equation>\lambda^{2}-3 \lambda+2=0</equation>，解得<equation>\lambda_{1}=1,\lambda_{2}=</equation>2，于是齐次线性方程的通解为<equation>Y = C_{1}\mathrm{e}^{x} + C_{2}\mathrm{e}^{2x}</equation>，其中<equation>C_{1}, C_{2}</equation>为任意常数.

设原方程的一个特解为<equation>y^{*} = (ax + b)x\mathrm{e}^{x}</equation>，代入原方程得到<equation>\left(a x ^ {2} + 4 a x + b x + 2 a + 2 b\right) \mathrm {e} ^ {x} - 3 \left(a x ^ {2} + 2 a x + b x + b\right) \mathrm {e} ^ {x} + 2 \left(a x ^ {2} + b x\right) \mathrm {e} ^ {x} = 2 x \mathrm {e} ^ {x}.</equation>化简得<equation>- 2 a x+2 a-b=2 x</equation>，于是<equation>- 2 a = 2, \quad 2 a - b = 0,</equation>

---

**2009年第10题 | 填空题 | 4分**

10. 若二阶常系数线性齐次微分方程<equation>y^{\prime \prime}+a y^{\prime}+b y=0</equation>的通解为<equation>y=( C_{1}+C_{2} x ) \mathrm{e}^{x}</equation>，则非齐次方程<equation>y^{\prime \prime}+a y^{\prime}+b y=x</equation>满足条件<equation>y ( 0 )=2, y^{\prime} ( 0 )=0</equation>的解为 y=___

**答案:**- xe<equation>^{x}</equation>+ x + 2.

**解析:**解 由题设及二阶常系数线性齐次微分方程通解的形式知，特征方程<equation>\lambda^{2}+a\lambda+b=0</equation>的根为<equation>\lambda_{1}=\lambda_{2}=1</equation>，从而 a=-2,b=1.设非齐次线性方程<equation>y^{\prime \prime}-2y^{\prime}+y=x</equation>的一个特解为<equation>y^{*} = cx+d</equation>代入该方程，整理得到<equation>c x + d - 2 c = x.</equation>于是<equation>c = 1,d = 2c = 2</equation>，从而非齐次线性方程的通解为<equation>y = \left(C _ {1} + C _ {2} x\right) \mathrm {e} ^ {x} + x + 2.</equation>进而<equation>y^{\prime} = \left(C_{1} + C_{2} + C_{2}x\right)\mathrm{e}^{x} + 1.</equation>将<equation>y(0) = 2,y^{\prime}(0) = 0</equation>代入，得到<equation>C _ {1} + 2 = 2, \quad C _ {1} + C _ {2} + 1 = 0.</equation>解得<equation>C_{1} = 0, C_{2} = -1.</equation>因此，所求解为<equation>y = -x\mathrm{e}^{x} + x + 2.</equation>

---


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

---

**2014年第20题 | 解答题 | 11分**

20. (本题满分11分)

设<equation>A = \left( \begin{array}{c c c c} 1 & -2 & 3 & -4 \\ 0 & 1 & -1 & 1 \\ 1 & 2 & 0 & -3 \end{array} \right), E</equation>为3阶单位矩阵.

I. 求方程组<equation>A x=0</equation>的一个基础解系；

II. 求满足<equation>A B=E</equation>的所有矩阵 B.

**答案:**(20) ( I )<equation>(-1,2,3,1)^{\mathrm{T}};</equation><equation>\text {I I)} \boldsymbol {B} = \left( \begin{array}{c c c} 2 - k _ {1} & 6 - k _ {2} & - 1 - k _ {3} \\ - 1 + 2 k _ {1} & - 3 + 2 k _ {2} & 1 + 2 k _ {3} \\ - 1 + 3 k _ {1} & - 4 + 3 k _ {2} & 1 + 3 k _ {3} \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right), \text {其 中} k _ {1}, k _ {2}, k _ {3} \text {为 任 意 常 数}.</equation>

**解析:**解（I）考察系数矩阵A.<equation>\begin{array}{l} \boldsymbol {A} = \left( \begin{array}{c c c c} 1 & - 2 & 3 & - 4 \\ 0 & 1 & - 1 & 1 \\ 1 & 2 & 0 & - 3 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c c} 1 & - 2 & 3 & - 4 \\ 0 & 1 & - 1 & 1 \\ 0 & 4 & - 3 & 1 \end{array} \right) \xrightarrow {r _ {1} + 2 r _ {2}} \left( \begin{array}{c c c c} 1 & 0 & 1 & - 2 \\ 0 & 1 & - 1 & 1 \\ 0 & 0 & 1 & - 3 \end{array} \right) \\ \xrightarrow {r _ {1} ^ {*} - r _ {3} ^ {* *}} \frac {1}{r _ {2} + r _ {3} ^ {* *}} \left( \begin{array}{c c c c} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & - 2 \\ 0 & 0 & 1 & - 3 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每作一次初等行变换，加一个<equation>*.</equation>）<equation>Ax = 0</equation>可化为方程组<equation>\left\{ \begin{array}{l} x_{1} + x_{4} = 0, \\ x_{2} - 2x_{4} = 0, \\ x_{3} - 3x_{4} = 0. \end{array} \right.</equation>由此可得<equation>\xi = (-1, 2, 3, 1)^{\mathrm{T}}</equation>为<equation>Ax = 0</equation>的一个基础解系.

（Ⅱ）实际上我们要求的是三个非齐次线性方程组<equation>A x=(1,0,0)^{\mathrm{T}}</equation>，<equation>A x=(0,1,0)^{\mathrm{T}}</equation>，<equation>A x=(0,0,1)^{\mathrm{T}}</equation>的解.由于它们的系数矩阵都是A，故可考虑对（A，E）作初等行变换，同第（I）问中的步骤可得<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {E}) = \left( \begin{array}{c c c c c c c} 1 & - 2 & 3 & - 4 & 1 & 0 & 0 \\ 0 & 1 & - 1 & 1 & 0 & 1 & 0 \\ 1 & 2 & 0 & - 3 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c c c c c} 1 & - 2 & 3 & - 4 & 1 & 0 & 0 \\ 0 & 1 & - 1 & 1 & 0 & 1 & 0 \\ 0 & 4 & - 3 & 1 & - 1 & 0 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} + 2 r _ {2}} \frac {1}{r _ {3} ^ {*} - 4 r _ {2}} \left( \begin{array}{c c c c c c c} 1 & 0 & 1 & - 2 & 1 & 2 & 0 \\ 0 & 1 & - 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & 1 & - 3 & - 1 & - 4 & 1 \end{array} \right) \xrightarrow {r _ {1} ^ {*} - r _ {3} ^ {* *}} \left( \begin{array}{c c c c c c c} 1 & 0 & 0 & 1 & 2 & 6 & - 1 \\ 0 & 1 & 0 & - 2 & - 1 & - 3 & 1 \\ 0 & 0 & 1 & - 3 & - 1 & - 4 & 1 \end{array} \right). \\ \end{array}</equation>由于<equation>\mathbf{A}</equation>为<equation>3\times4</equation>矩阵，<equation>\mathbf{E}</equation>为3阶单位矩阵，<equation>\mathbf{B}</equation>应为<equation>4\times3</equation>矩阵，从而知，<equation>(2,-1,-1,0)^{\mathrm{T}}</equation><equation>(6,-3,-4,0)^{\mathrm{T}}</equation><equation>(-1,1,1,0)^{\mathrm{T}}</equation>分别为<equation>\mathbf{Ax}=(1,0,0)^{\mathrm{T}}</equation><equation>\mathbf{Ax}=(0,1,0)^{\mathrm{T}}</equation><equation>\mathbf{Ax}=(0,0,1)^{\mathrm{T}}</equation>的一个特解.

与第（I）问中<equation>A x=0</equation>的通解相结合，得到<equation>A x=(1,0,0)^{\mathrm{T}}</equation><equation>A x=(0,1,0)^{\mathrm{T}}</equation><equation>A x=(0,0,1)^{\mathrm{T}}</equation>的通解分别为<equation>\begin{aligned} \boldsymbol {\alpha} _ {1} &= k _ {1} (- 1, 2, 3, 1) ^ {\mathrm {T}} + (2, - 1, - 1, 0) ^ {\mathrm {T}}, \\ \boldsymbol {\alpha} _ {2} &= k _ {2} (- 1, 2, 3, 1) ^ {\mathrm {T}} + (6, - 3, - 4, 0) ^ {\mathrm {T}}, \\ \boldsymbol {\alpha} _ {3} &= k _ {3} (- 1, 2, 3, 1) ^ {\mathrm {T}} + (- 1, 1, 1, 0) ^ {\mathrm {T}}, \end{aligned}</equation>其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数.

因此，<equation>B = \left( \begin{array}{c c c} 2 - k_1 & 6 - k_2 & -1 - k_3 \\ -1 + 2k_1 & -3 + 2k_2 & 1 + 2k_3 \\ -1 + 3k_1 & -4 + 3k_2 & 1 + 3k_3 \\ k_1 & k_2 & k_3 \end{array} \right)</equation>，其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数.

---

**2013年第20题 | 解答题 | 11分**

20. (本题满分11分)

设<equation>A = \left( \begin{array}{c c} 1 & a \\ 1 & 0 \end{array} \right), B = \left( \begin{array}{c c} 0 & 1 \\ 1 & b \end{array} \right)</equation>当<equation>a,b</equation>为何值时，存在矩阵<equation>C</equation>使得<equation>AC - CA = B</equation>，并求所有矩阵<equation>C</equation>

**答案:**(20)<equation>a = -1, b = 0</equation>时，<equation>C = \left( \begin{array}{c c} k_{1} + k_{2} + 1 & -k_{2} \\ k_{2} & k_{1} \end{array} \right)</equation>，其中<equation>k_{1}, k_{2}</equation>为任意常数.

**解析:**解（法一）设<equation>C = \left( \begin{array}{cc} x_{1} & x_{2} \\ x_{3} & x_{4} \end{array} \right)</equation>，则由<equation>AC-CA=B</equation>可得<equation>\left( \begin{array}{c c} 1 & a \\ 1 & 0 \end{array} \right) \left( \begin{array}{c c} x _ {1} & x _ {2} \\ x _ {3} & x _ {4} \end{array} \right) - \left( \begin{array}{c c} x _ {1} & x _ {2} \\ x _ {3} & x _ {4} \end{array} \right) \left( \begin{array}{c c} 1 & a \\ 1 & 0 \end{array} \right) = \left( \begin{array}{c c} 0 & 1 \\ 1 & b \end{array} \right).</equation>写成线性方程组的形式：<equation>\left\{ \begin{array}{l} - x _ {2} + a x _ {3} = 0, \\ - a x _ {1} + x _ {2} + a x _ {4} = 1, \\ x _ {1} - x _ {3} - x _ {4} = 1, \\ x _ {2} - a x _ {3} = b. \end{array} \right.</equation>记该线性方程组为<equation>Px = \beta ,\beta = (0,1,1,b)^{\mathrm{T}}</equation>，则<equation>Px = \beta</equation>有解当且仅当<equation>r(P,\beta) = r(P)</equation><equation>(P, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 0 & - 1 & a & 0 & 0 \\ - a & 1 & 0 & a & 1 \\ 1 & 0 & - 1 & - 1 & 1 \\ 0 & 1 & - a & 0 & b \end{array} \right) \xrightarrow {r _ {2} + a r _ {3}} \left( \begin{array}{c c c c c} 0 & - 1 & a & 0 & 0 \\ 0 & 1 & - a & 0 & a + 1 \\ 1 & 0 & - 1 & - 1 & 1 \\ 0 & 1 & - a & 0 & b \end{array} \right)</equation><equation>\xrightarrow [ r _ {4} + r _ {1} ]{r _ {2} ^ {*} + r _ {1}} \left( \begin{array}{c c c c c} 0 & - 1 & a & 0 & 0 \\ 0 & 0 & 0 & 0 & a + 1 \\ 1 & 0 & - 1 & - 1 & 1 \\ 0 & 0 & 0 & 0 & b \end{array} \right) \rightarrow \left( \begin{array}{c c c c c} 1 & 0 & - 1 & - 1 & 1 \\ 0 & 1 & - a & 0 & 0 \\ 0 & 0 & 0 & 0 & a + 1 \\ 0 & 0 & 0 & 0 & b \end{array} \right).</equation><equation>r_2^*</equation>表示对<equation>r_2</equation>作初等行变换后所得新的第二行. 由上可见，若<equation>r(\boldsymbol{P},\boldsymbol{\beta}) = r(\boldsymbol{P})</equation>，则必有<equation>a + 1 = b = 0</equation>从而<equation>a = -1</equation>，<equation>b = 0</equation>.

当 a = -1，b = 0时，<equation>(\boldsymbol {P}, \boldsymbol {\beta}) \rightarrow \left(\begin{array}{c c c c c}1&0&- 1&- 1&1\\0&1&1&0&0\\0&0&0&0&0\\0&0&0&0&0\end{array}\right),</equation>即<equation>\left\{ \begin{array}{l l} x_{2}+x_{3}=0, \\ x_{1}-x_{3}-x_{4}=1. \end{array} \right.</equation>（1,0,0,1）<equation>^{\mathrm{T}}</equation>和（1,-1,1,0）<equation>^{\mathrm{T}}</equation>为该方程组对应的齐次线性方程组的一个基础解系.又（1,0,0,0）<equation>^{\mathrm{T}}</equation>为<equation>P x=\beta</equation>的一个特解，故<equation>P x=\beta</equation>的通解为<equation>k _ {1} \left(1, 0, 0, 1\right) ^ {\mathrm {T}} + k _ {2} \left(1, - 1, 1, 0\right) ^ {\mathrm {T}} + \left(1, 0, 0, 0\right) ^ {\mathrm {T}},</equation>其中<equation>k_{1}, k_{2}</equation>为任意常数.

因此，当<equation>a = -1</equation>，<equation>b = 0</equation>时，存在C使得AC-CA=B.此时的C形如<equation>\left( \begin{array}{c c} k_{1}+k_{2}+1 & -k_{2} \\ k_{2} & k_{1} \end{array} \right)</equation>其中<equation>k_{1}, k_{2}</equation>为任意常数.

（法二）由于AC的迹等于CA的迹，故AC-CA的迹等于零.因此<equation>b=0.</equation><equation>B=\left( \begin{array}{ll}0&1\\ 1&0\end{array} \right)</equation>设<equation>C = \left( \begin{array}{cc} x_{1} & x_{2} \\ x_{3} & x_{4} \end{array} \right)</equation>，则由<equation>A C-C A=B</equation>可得<equation>\left\{ \begin{array}{l} - x _ {2} + a x _ {3} = 0, \\ - a x _ {1} + x _ {2} + a x _ {4} = 1, \\ x _ {1} - x _ {3} - x _ {4} = 1, \\ x _ {2} - a x _ {3} = 0. \end{array} \right.</equation>将<equation>x_{2}=a x_{3}</equation>代入<equation>- a x_{1}+x_{2}+a x_{4}=1</equation>可得<equation>- a \left(x_{1}-x_{3}-x_{4}\right)=1</equation>与<equation>x_{1}-x_{3}-x_{4}=1</equation>比较得，a=-1. 从而 a=-1，b=0.

其余同法一.

---

**2012年第20题 | 解答题 | 11分**

20. (本题满分11分)

设<equation>\therefore = \left( \begin{array}{c c c c} 1 & a & 0 & 0 \\ 0 & 1 & a & 0 \\ 0 & 0 & 1 & a \\ a & 0 & 0 & 1 \end{array} \right)</equation><equation>\beta = \left( \begin{array}{c} 1 \\ - 1 \\ 0 \\ 0 \end{array} \right).</equation>I. 计算行列式<equation>|A|</equation>；

II. 当实数<equation>a</equation>为何值时，方程组<equation>Ax = \beta</equation>有无穷多解，并求其通解.

**答案:**（Ⅱ）当 a=-1时，方程组<equation>A x=\beta</equation>有无穷多解，其通解为<equation>k(1,1,1,1)^{\mathrm{T}}+(0,-1,0,0)^{\mathrm{T}}</equation>其中 k为任意常数.

**解析:**（ I ）按第一行展开<equation>|A|</equation>，得<equation>| \boldsymbol {A} | = \left| \begin{array}{c c c} 1 & a & 0 \\ 0 & 1 & a \\ 0 & 0 & 1 \end{array} \right| - a \left| \begin{array}{c c c} 0 & a & 0 \\ 0 & 1 & a \\ a & 0 & 1 \end{array} \right| = 1 - a ^ {4}.</equation>（Ⅱ）（法一）<equation>A x=\beta</equation>有无穷多解的充要条件为<equation>r(A)=r(A,\beta) < 4.</equation>由<equation>r(A) < 4</equation>可得，<equation>|A| = 0</equation>，从而<equation>a = \pm 1.</equation>当 a = 1时，<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 1 & 0 & 0 & 1 & 0 \end{array} \right) \xrightarrow {r _ {4} - r _ {1}} \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & - 1 & 0 & 1 & - 1 \end{array} \right) \xrightarrow {r _ {4} ^ {*} + r _ {2}} \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1 & - 2 \end{array} \right) \\ \xrightarrow {r _ {4} ^ {* *} - r _ {3}} \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 & - 2 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）由上可知，<equation>r ( \mathbf{A}, \mathbf{\beta})=4</equation>，而<equation>r ( \mathbf{A})=3</equation>，<equation>\mathbf{Ax}=\boldsymbol{\beta}</equation>无解. a=1不符合题意.

当 a = -1时，<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 1 & - 1 & 0 & 0 & 1 \\ 0 & 1 & - 1 & 0 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ - 1 & 0 & 0 & 1 & 0 \end{array} \right) \xrightarrow {r _ {4} + r _ {1}} \left( \begin{array}{c c c c c} 1 & - 1 & 0 & 0 & 1 \\ 0 & 1 & - 1 & 0 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ 0 & - 1 & 0 & 1 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} + r _ {2}} \frac {r _ {4} ^ {*} + r _ {2}}{\left( \begin{array}{c c c c c} 1 & 0 & - 1 & 0 & 0 \\ 0 & 1 & - 1 & 0 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ 0 & 0 & - 1 & 1 & 0 \end{array} \right)} \xrightarrow {r _ {1} ^ {*} + r _ {3}} \frac {r _ {2} + r _ {3}}{r _ {4} ^ {* *} + r _ {3}} \left( \begin{array}{c c c c c} 1 & 0 & 0 & - 1 & 0 \\ 0 & 1 & 0 & - 1 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>由上可知，<equation>r(\mathbf{A},\boldsymbol{\beta}) = r(\mathbf{A}) = 3 < 4, \mathbf{Ax} = \boldsymbol{\beta}</equation>有无穷多解.

齐次方程<equation>Ax = 0</equation>的通解为<equation>k(1,1,1,1)^{\mathrm{T}}</equation>，其中<equation>k</equation>为任意常数。又因为<equation>(0,-1,0,0)^{\mathrm{T}}</equation>为<equation>Ax = \beta</equation>的一个特解，所以<equation>Ax = \beta</equation>的通解为<equation>k(1,1,1,1)^{\mathrm{T}} + (0,-1,0,0)^{\mathrm{T}}</equation>，其中<equation>k</equation>为任意常数综上所述，当<equation>a = -1</equation>时，方程组<equation>Ax = \beta</equation>有无穷多解，其通解为<equation>k(1,1,1,1)^{\mathrm{T}} + (0,-1,0,0)^{\mathrm{T}}</equation>其中<equation>k</equation>为任意常数.

（法二）对含有参数<equation>a</equation>的增广矩阵<equation>(\mathbf{A},\boldsymbol{\beta})</equation>作初等行变换.<equation>(\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ a & 0 & 0 & 1 & 0 \end{array} \right) \xrightarrow {r _ {4} - a r _ {1}} \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ 0 & - a ^ {2} & 0 & 1 & - a \end{array} \right)</equation><equation>\xrightarrow {r _ {4} ^ {*} + a ^ {2} r _ {2}} \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ 0 & 0 & a ^ {3} & 1 & - a - a ^ {2} \end{array} \right) \xrightarrow {r _ {4} ^ {* *} - a ^ {3} r _ {3}} \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ 0 & 0 & 0 & 1 - a ^ {4} & - a - a ^ {2} \end{array} \right).</equation>由于<equation>A x= \beta</equation>有无穷多解，故<equation>r ( A )=r ( A,\beta) < 4.</equation>因此，<equation>1-a^{4}=0,-a-a^{2}=0</equation>解得<equation>a=-1.</equation>其余同法一.

---

**2010年第20题 | 解答题 | 11分**

20. (本题满分11分)

设<equation>A=\left( \begin{array}{c c c} \lambda & 1 & 1 \\ 0 & \lambda-1 & 0 \\ 1 & 1 & \lambda \end{array} \right), b=\left( \begin{array}{c} a \\ 1 \\ 1 \end{array} \right).</equation>已知线性方程组<equation>A x=b</equation>存在2个不同的解.

I. 求<equation>\lambda, a</equation>;

II. 求方程组<equation>A x=b</equation>的通解.

**答案:**(20) （I）<equation>\lambda=-1,a=-2;</equation>（Ⅱ）<equation>\boldsymbol{A}\boldsymbol{x}=\boldsymbol{b}</equation>的通解为<equation>k(1,0,1)^{\mathrm{T}}+\left(\frac{3}{2},-\frac{1}{2},0\right)^{\mathrm{T}}</equation>，其中 k为任意常数.

**解析:**解（I）<equation>A x=b</equation>有两个不同的解意味着<equation>A x=b</equation>有解但不唯一，故<equation>r(A)=r(A,b)<3.</equation><equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} \lambda & 1 & 1 & a \\ 0 & \lambda - 1 & 0 & 1 \\ 1 & 1 & \lambda & 1 \end{array} \right) \xrightarrow {r _ {1} \leftrightarrow r _ {3}} \left( \begin{array}{c c c c} 1 & 1 & \lambda & 1 \\ 0 & \lambda - 1 & 0 & 1 \\ \lambda & 1 & 1 & a \end{array} \right) \xrightarrow {r _ {3} ^ {*} - \lambda r _ {1} ^ {*}} \left( \begin{array}{c c c c} 1 & 1 & \lambda & 1 \\ 0 & \lambda - 1 & 0 & 1 \\ 0 & 1 - \lambda & 1 - \lambda^ {2} & a - \lambda \end{array} \right) \\ \xrightarrow {r _ {3} ^ {* *} + r _ {2}} \left( \begin{array}{c c c c} 1 & 1 & \lambda & 1 \\ 0 & \lambda - 1 & 0 & 1 \\ 0 & 0 & 1 - \lambda^ {2} & a - \lambda + 1 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每做一次初等行变换，加一个*.）

由于<equation>r(A) < 3</equation>，故<equation>1 - \lambda^2 = 0, \lambda = \pm 1.</equation>当<equation>\lambda = 1</equation>时，<equation>r(\mathbf{A},\mathbf{b}) = 2</equation>，<equation>r(\mathbf{A}) = 1</equation>，方程组无解，舍去.

当<equation>\lambda=-1</equation>时，<equation>(A,b)\rightarrow \left( \begin{array}{c c c c}1&1&-1&1\\ 0&-2&0&1\\ 0&0&0&a+2 \end{array} \right).</equation>此时<equation>r(A)=2.</equation>若<equation>r(A)=r(A,b),</equation>则<equation>r(A,b)=2, a+2=0</equation>即<equation>a=-2.</equation>（Ⅱ）由第（I）问知，当<equation>\lambda=-1</equation>a=-2时，<equation>(\boldsymbol {A}, \boldsymbol {b}) \rightarrow \left(\begin{array}{c c c c}1&1&- 1&1\\0&- 2&0&1\\0&0&0&0\end{array}\right) \xrightarrow [ r _ {1} - r _ {2} ^ {*} ]{r _ {2} \times \left(- \frac {1}{2}\right)} \left(\begin{array}{c c c c}1&0&- 1&\frac {3}{2}\\\0&1&0&- \frac {1}{2}\\\0&0&0&0\end{array}\right).</equation>其对应的齐次方程组等价于<equation>\left\{ \begin{array}{l l} x_{1}-x_{3}=0, \\ x_{2}=0, \end{array} \right.</equation>故可取<equation>(1,0,1)^{\mathrm{T}}</equation>为该方程组的一个基础解系。又<equation>\left(\frac{3}{2},-\frac{1}{2},0\right)^{\mathrm{T}}</equation>为原方程组的一个特解，故<equation>A x=b</equation>的通解为<equation>k(1,0,1)^{\mathrm{T}}+\left(\frac{3}{2},-\frac{1}{2},0\right)^{\mathrm{T}}</equation>其中k为任意常数.

---


### 矩阵


#### 矩阵的秩

**2025年第7题 | 选择题 | 5分 | 答案: A**

7. 设 n阶矩阵 A,B,C满足<equation>r ( A )+r ( B )+r ( C )=r ( A B )+2 n</equation>，给出下列四个结论：

I.<equation>r ( A B )+n=r ( A B )+r ( C )</equation>II.<equation>r ( A B )+n=r ( A )+r ( B )</equation>III.<equation>r ( A )=r ( B )=r ( C )=n</equation>IV.<equation>r ( A B )=r ( B C )=n</equation>其中正确的选项是（    ）

A. I、II B. I、III C. II、IV D. III、IV

答案: A

**解析:**解下面说明<equation>\textcircled{3}</equation><equation>\textcircled{4}</equation>不正确.

取 n=2，<equation>A=C=E,B=O</equation>，则<equation>AB=BC=ABC=O,r(A)=r(C)=2,r(B)=r(ABC)= 0</equation>，满足<equation>r(A)+r(B)+r(C)=r(ABC)+4=4.</equation>但此时，<equation>\textcircled{3},\textcircled{4}</equation>均不成立.

由排除法可知，应选A.

下面说明<equation>\textcircled{1}</equation><equation>\textcircled{2}</equation>正确.

首先，<equation>r ( A ) + r ( B ) = r \left( \begin{array}{cc} A & O \\ O & B \end{array} \right) \leqslant r \left( \begin{array}{cc} A & O \\ E & B \end{array} \right).</equation>另一方面，<equation>\left( \begin{array}{c c} E & - A \\ O & E \end{array} \right) \left( \begin{array}{c c} A & O \\ E & B \end{array} \right) \left( \begin{array}{c c} O & E \\ E & O \end{array} \right) = \left( \begin{array}{c c} O & - A B \\ E & B \end{array} \right) \left( \begin{array}{c c} O & E \\ E & O \end{array} \right) = \left( \begin{array}{c c} - A B & O \\ B & E \end{array} \right).</equation>于是，<equation>r \left( \begin{array}{c c} A & O \\ E & B \end{array} \right) = r \left( \begin{array}{c c} - A B & O \\ B & E \end{array} \right) = r (A B) + n</equation>，进一步可得<equation>r (A) + r (B)\leqslant r (A B) + n.</equation>对该式两端同时加上<equation>r (C)</equation>并结合<equation>r (A B C) + 2 n = r (A) + r (B) + r (C)</equation>可得<equation>r (\mathbf {A B C}) + 2 n = r (\mathbf {A}) + r (\mathbf {B}) + r (\mathbf {C}) \leqslant r (\mathbf {A B}) + r (\mathbf {C}) + n,</equation>即<equation>r(\mathbf{ABC}) + n \leqslant r(\mathbf{AB}) + r(\mathbf{C})</equation>令<equation>P=A B</equation>，则由<equation>r(A)+r(B)\leqslant r(A B)+n</equation>可得<equation>r(P)+r(C)\leqslant r(P C)+n</equation>，即<equation>r(A B)+r(C)\leqslant r(A B C)+n.</equation>因此，<equation>r ( A B C ) + n = r ( A B ) + r ( C )</equation><equation>\textcircled{1}</equation>正确.

联立<equation>\left\{ \begin{array}{l l} r ( A B C ) + 2 n = r ( A ) + r ( B ) + r ( C ) \\ r ( A B C ) + n = r ( A B ) + r ( C ) , \end{array} \right.</equation>两式相减可得 n = r(A) + r(B) - r(AB)，即<equation>r ( A B ) + n = r ( A ) + r ( B ).</equation>因此，<equation>\textcircled{2}</equation>正确.

也可以用下面的方法证明<equation>r(A) + r(B) \leqslant r(AB) + n.</equation>考虑方程组<equation>Ax = 0, Bx = 0, ABx = 0, Ax = 0</equation>的解空间的维数为<equation>r_{1} = n - r(A), Bx = 0</equation>的解空间的维数为<equation>r_{2} = n - r(B), ABx = 0</equation>的解空间的维数为<equation>r_{3} = n - r(AB)</equation>. 若能证明<equation>r_{3} \leqslant r_{1} + r_{2}</equation>即<equation>n - r(AB) \leqslant n - r(A) + n - r(B)</equation>, 则可得<equation>r(A) + r(B) \leqslant r(AB) + n</equation>.

记<equation>r = r_{3} - r_{2}</equation>，则<equation>r_{2} + r = r_{3}</equation>.取<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{r_{2}}</equation>为方程组<equation>Bx = 0</equation>的一个基础解系.由于<equation>Bx = 0</equation>的解均为<equation>ABx = 0</equation>的解，故可设<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{r_{2}},\beta_{1},\beta_{2},\dots ,\beta_{r}</equation>为方程组<equation>ABx = 0</equation>的一个基础解系.

由于<equation>\beta_{i} ( i=1,2,\dots,r)</equation>均满足<equation>A B x=0</equation>，故<equation>B \beta_{i} ( i=1,2,\dots,r)</equation>均为方程组<equation>A x=0</equation>的解。若能证明<equation>B \beta_{1},B \beta_{2},\dots,B \beta_{r}</equation>线性无关，则由<equation>B \beta_{1},B \beta_{2},\dots,B \beta_{r}</equation>的秩不超过<equation>A x=0</equation>的解空间的维数可得<equation>r=r_{3}-r_{2}\leqslant r_{1}</equation>即<equation>r_{3}\leqslant r_{1}+r_{2}.</equation>设<equation>k_{1}, k_{2}, \dots , k_{r}</equation>满足<equation>k _ {1} \boldsymbol {B} \boldsymbol {\beta} _ {1} + k _ {2} \boldsymbol {B} \boldsymbol {\beta} _ {2} + \dots + k _ {r} \boldsymbol {B} \boldsymbol {\beta} _ {r} = \mathbf {0}.</equation>整理可得<equation>B \left(k_{1}\boldsymbol{\beta}_{1}+k_{2}\boldsymbol{\beta}_{2}+\dots+k_{r}\boldsymbol{\beta}_{r}\right)=0</equation>，由此可知<equation>k_{1}\boldsymbol{\beta}_{1}+k_{2}\boldsymbol{\beta}_{2}+\dots+k_{r}\boldsymbol{\beta}_{r}</equation>是方程组<equation>B x=0</equation>的解，从而存在<equation>l_{1},l_{2},\dots,l_{r_{2}}</equation>，使得<equation>k _ {1} \boldsymbol {\beta} _ {1} + k _ {2} \boldsymbol {\beta} _ {2} + \dots + k _ {r} \boldsymbol {\beta} _ {r} = l _ {1} \boldsymbol {\alpha} _ {1} + l _ {2} \boldsymbol {\alpha} _ {2} + \dots + l _ {r _ {2}} \boldsymbol {\alpha} _ {r _ {2}},</equation>即<equation>k_{1}\boldsymbol{\beta}_{1} + k_{2}\boldsymbol{\beta}_{2} + \dots + k_{r}\boldsymbol{\beta}_{r} - l_{1}\boldsymbol{\alpha}_{1} - l_{2}\boldsymbol{\alpha}_{2} - \dots - l_{r_{2}}\boldsymbol{\alpha}_{r_{2}} = 0.</equation>由于<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{r_2},\beta_1,\beta_2,\dots ,\beta_r</equation>线性无关，故<equation>k_{1} = k_{2} = \dots = k_{r} = l_{1} = l_{2} = \dots = l_{r_2} = 0</equation>，进一步可得<equation>B\beta_{1},B\beta_{2},\dots ,B\beta_{r}</equation>线性无关.

由前面的分析可知，<equation>r ( A ) + r ( B ) \leqslant r ( A B ) + n.</equation>

---

**2023年第5题 | 选择题 | 5分 | 答案: B**

5. 已知 n阶矩阵 A,B,C满足<equation>A B C=O, E</equation>为 n阶单位矩阵，记矩阵<equation>\left( \begin{array}{c c} O & A \\ B C & E \end{array} \right), \left( \begin{array}{c c} A B & C \\ O & E \end{array} \right), \left( \begin{array}{c c} E & A B \\ A B & O \end{array} \right)</equation>的秩分别为<equation>r_{1}, r_{2}, r_{3}</equation>，则（    ）

A.<equation>r_{1}\leqslant r_{2}\leqslant r_{3}</equation>B.<equation>r_{1}\leqslant r_{3}\leqslant r_{2}</equation>C.<equation>r_{3}\leqslant r_{1}\leqslant r_{2}</equation>D.<equation>r_{2}\leqslant r_{1}\leqslant r_{3}</equation>

答案: B

**解析:**解记<equation>M_{1} = \left( \begin{array}{cc}O&A\\ BC&E \end{array} \right), M_{2} = \left( \begin{array}{cc}AB&C\\ O&E \end{array} \right), M_{3} = \left( \begin{array}{cc}E&AB\\ AB&O \end{array} \right).</equation>分别对<equation>M_{1}, M_{2}, M_{3}</equation>作初等变换.<equation>M _ {1} = \left( \begin{array}{c c} O & A \\ B C & E \end{array} \right) \xrightarrow {\textcircled{1}} \left( \begin{array}{c c} - A B C & O \\ B C & E \end{array} \right) \xlongequal {A B C = O} \left( \begin{array}{c c} O & O \\ B C & E \end{array} \right).</equation><equation>M _ {2} = \left( \begin{array}{c c} A B & C \\ O & E \end{array} \right) \xrightarrow {\textcircled{2}} \left( \begin{array}{c c} A B & O \\ O & E \end{array} \right).</equation><equation>M _ {3} = \left( \begin{array}{c c} E & A B \\ A B & O \end{array} \right) \xrightarrow {\textcircled{3}} \left( \begin{array}{c c} E & A B \\ O & - A B A B \end{array} \right) \xrightarrow {\textcircled{4}} \left( \begin{array}{c c} E & O \\ O & - A B A B \end{array} \right).</equation>操作<equation>\textcircled{1}</equation>对应左乘可逆矩阵<equation>\left( \begin{array}{cc} E & -A \\ O & E \end{array} \right)</equation>，操作<equation>\textcircled{2}</equation>对应左乘可逆矩阵<equation>\left( \begin{array}{cc} E & -C \\ O & E \end{array} \right)</equation>，操作<equation>\textcircled{3}</equation>对应左乘可逆矩阵<equation>\left( \begin{array}{cc} E & O \\ -AB & E \end{array} \right)</equation>，操作<equation>\textcircled{4}</equation>对应右乘可逆矩阵<equation>\left( \begin{array}{cc} E & -AB \\ O & E \end{array} \right)</equation>由前面的计算可得<equation>r _ {1} = r \left(\boldsymbol {M} _ {1}\right) = r (\boldsymbol {E}) = n,</equation><equation>r _ {2} = r \left(\boldsymbol {M} _ {2}\right) = r (\boldsymbol {E}) + r (\boldsymbol {A B}) \geqslant n,</equation><equation>r _ {3} = r \left(\boldsymbol {M} _ {3}\right) = r (\boldsymbol {E}) + r \left(\boldsymbol {A B A B}\right) \geqslant n.</equation>由此可得，<equation>r_{1}\leqslant r_{2},r_{1}\leqslant r_{3}</equation>. 又因为<equation>r(\mathbf{ABAB})\leqslant r(\mathbf{AB})</equation>，所以<equation>r_{3}\leqslant r_{2}</equation>综上所述，<equation>r_{1}\leqslant r_{3}\leqslant r_{2}</equation>，应选B.

---

**2021年第7题 | 选择题 | 5分 | 答案: C**

7. 设 A,B为 n阶实矩阵，下列结论不成立的是（    )

A.<equation>r \left( \begin{array}{c c} A & O \\ O & A^{\mathrm{T}} A \end{array} \right)=2 r (A)</equation>B.<equation>r \left( \begin{array}{c c} A & A B \\ O & A^{\mathrm{T}} \end{array} \right)=2 r (A)</equation>C.<equation>r \left( \begin{array}{c c} A & B A \\ O & A A^{\mathrm{T}} \end{array} \right)=2 r (A)</equation>D.<equation>r \left( \begin{array}{c c} A & O \\ B A & A^{\mathrm{T}} \end{array} \right)=2 r (A)</equation>

答案: C

**解析:**依次分析4个选项.

选项A：由矩阵的秩的结论，<equation>r ( \mathbf{A}^{ \mathrm{T}} \mathbf{A} )=r ( \mathbf{A} )</equation>.因此，<equation>r \left( \begin{array}{cc} \mathbf{A} & \mathbf{O} \\ \mathbf{O} & \mathbf{A}^{ \mathrm{T}} \mathbf{A} \end{array} \right)=r ( \mathbf{A} )+r ( \mathbf{A} )=2 r ( \mathbf{A} ).</equation>选项 A成立.

选项B：由于<equation>\left( \begin{array}{c c} A & A B \\ O & A ^ {\mathrm {T}} \end{array} \right) = \left( \begin{array}{c c} A & O \\ O & A ^ {\mathrm {T}} \end{array} \right) \left( \begin{array}{c c} E & B \\ O & E \end{array} \right),</equation>故<equation>r \left( \begin{array}{cc} A & A B \\ O & A^{\mathrm{T}} \end{array} \right) = r \left( \begin{array}{cc} A & O \\ O & A^{\mathrm{T}} \end{array} \right) = 2 r (A).</equation>选项B成立.

选项C：BA的列向量均可由B的列向量表示，但不一定可由A的列向量表示。由此出发考虑选项C的反例.

令<equation>A = \left( \begin{array}{cc}0 & 1\\ 0 & 0 \end{array} \right),B = \left( \begin{array}{cc}0 & 1\\ 1 & 0 \end{array} \right),B A = \left( \begin{array}{cc}0 & 0\\ 0 & 1 \end{array} \right),A A^{\mathrm{T}} = \left( \begin{array}{cc}0 & 1\\ 0 & 0 \end{array} \right)\left( \begin{array}{cc}0 & 0\\ 1 & 0 \end{array} \right) = \left( \begin{array}{cc}1 & 0\\ 0 & 0 \end{array} \right)</equation>.于是，<equation>\left( \begin{array}{c c} \boldsymbol {A} & \boldsymbol {B A} \\ \boldsymbol {O} & \boldsymbol {A A} ^ {\mathrm {T}} \end{array} \right) = \left( \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{array} \right).</equation><equation>r \left( \begin{array}{cc} A & B A \\ O & A A^{\mathrm{T}} \end{array} \right) = 3</equation>，而<equation>2 r ( \mathbf{A} )=2.</equation>两者不相等.选项C不成立.

选项D：由于<equation>\left( \begin{array}{c c} A & O \\ B A & A ^ {\mathrm {T}} \end{array} \right) = \left( \begin{array}{c c} E & O \\ B & E \end{array} \right) \left( \begin{array}{c c} A & O \\ O & A ^ {\mathrm {T}} \end{array} \right),</equation>故<equation>r \left( \begin{array}{cc} \boldsymbol{A} & \boldsymbol{O} \\ \boldsymbol{B A} & \boldsymbol{A}^{\mathrm{T}} \end{array} \right) = r \left( \begin{array}{cc} \boldsymbol{A} & \boldsymbol{O} \\ \boldsymbol{O} & \boldsymbol{A}^{\mathrm{T}} \end{array} \right) = 2 r (\boldsymbol{A}).</equation>选项D成立.

综上所述，应选C.

---

**2018年第6题 | 选择题 | 4分 | 答案: A**

6. 设 A,B为 n阶矩阵，记 r(X)为矩阵 X的秩，(X,Y)表示分块矩阵，则（    ）

A.<equation>r ( A, A B )=r ( A )</equation>B.<equation>r ( A, B A )=r ( A )</equation>C.<equation>r ( A, B )=\max \{ r ( A ) , r ( B ) \}</equation>D.<equation>r ( A, B )=r \left( A^{\mathrm{T}}, B^{\mathrm{T}} \right)</equation>

答案: A

**解析:**解记 C=AB.由于右乘矩阵表示对矩阵作列变换，故 C的列向量可由 A的列向量线性表示.于是，<equation>r ( A, C )=r ( A, A B )=r ( A ).</equation>因此，应选A.

下面分别说明选项B、C、D不正确.

选项B：<equation>r(\mathbf{A},\mathbf{B}\mathbf{A})\geqslant r(\mathbf{A}).</equation>.但是，<equation>r(\mathbf{A},\mathbf{B}\mathbf{A})=r(\mathbf{A})</equation>并不成立.

取<equation>A = \left( \begin{array}{ll}1 & 0\\ 0 & 0 \end{array} \right),B = \left( \begin{array}{ll}1 & 0\\ 1 & 1 \end{array} \right)</equation>，则<equation>BA = \left( \begin{array}{ll}1 & 0\\ 1 & 0 \end{array} \right),(A,BA) = \left( \begin{array}{lll}1 & 0 & 1 & 0\\ 0 & 0 & 1 & 0 \end{array} \right).r(A,BA) = 2</equation>，但<equation>r(A) = 1.</equation>选项C：<equation>r(\mathbf{A},\mathbf{B})\geqslant \max \{r(\mathbf{A}),r(\mathbf{B})\}</equation>.但是，<equation>r(\mathbf{A},\mathbf{B})=\max \{r(\mathbf{A}),r(\mathbf{B})\}</equation>并不成立.

取<equation>A = \left( \begin{array}{ll}1 & 0\\ 0 & 0 \end{array} \right),B = \left( \begin{array}{ll}0 & 0\\ 1 & 0 \end{array} \right)</equation>，则<equation>(A,B) = \left( \begin{array}{lll}1 & 0 & 0 & 0\\ 0 & 0 & 1 & 0 \end{array} \right),r(A,B) = 2</equation>，但<equation>r(A) = r(B) = 1.</equation>选项D：由于<equation>r(\mathbf{P})=r(\mathbf{P}^{\mathrm{T}})</equation>，而<equation>\left( \mathbf{A},\mathbf{B}\right)^{\mathrm{T}}=\binom{\mathbf{A}^{\mathrm{T}}}{\mathbf{B}^{\mathrm{T}}}</equation>，故<equation>r(\mathbf{A},\mathbf{B})=r\binom{\mathbf{A}^{\mathrm{T}}}{\mathbf{B}^{\mathrm{T}}}</equation>.但是，<equation>r(\mathbf{A},\mathbf{B})=r(\mathbf{A}^{\mathrm{T}},\mathbf{B}^{\mathrm{T}})</equation>并不成立.

取<equation>A=\left( \begin{array}{cc}1&0\\ 0&0 \end{array} \right), B=\left( \begin{array}{cc}0&0\\ 1&0 \end{array} \right),</equation>则<equation>\left( A,B\right)=\left( \begin{array}{c c c c}1&0&0&0\\ 0&0&1&0 \end{array} \right), \left( A^{\mathrm{T}},B^{\mathrm{T}}\right)=\left( \begin{array}{c c c c}1&0&0&1\\ 0&0&0&0 \end{array} \right). r \left( A,B\right)</equation>=2，但<equation>r \left( A^{\mathrm{T}},B^{\mathrm{T}}\right)=1.</equation>

---

**2017年第13题 | 填空题 | 4分**

13. 设矩阵<equation>A=\left( \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 2 \\ 0 & 1 & 1 \end{array} \right), \alpha_{1},\alpha_{2},\alpha_{3}</equation>为线性无关的3维列向量组，则向量组<equation>A\alpha_{1},A\alpha_{2},A\alpha_{3}</equation>的秩为 ___.

**答案:**```latex

2.
```
**解析: **由于<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性无关，故矩阵<equation>\left(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}\right)</equation>可逆，从而<equation>r \left(\boldsymbol {A} \boldsymbol {\alpha} _ {1}, \boldsymbol {A} \boldsymbol {\alpha} _ {2}, \boldsymbol {A} \boldsymbol {\alpha} _ {3}\right) = r \left(\boldsymbol {A} \left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\alpha} _ {2}, \boldsymbol {\alpha} _ {3}\right)\right) = r (\boldsymbol {A}).</equation>下面我们用三种方法计算<equation>r ( \mathbf{A} ).</equation>（法一）计算<equation>|A|</equation>得<equation>|A|=0</equation>，故<equation>r(A)\leqslant 2</equation>.又因为矩阵 A含有一个非零2阶子式，例如<equation>\left| \begin{array}{ll} 1 & 0 \\ 1 & 1 \end{array} \right|=1</equation>，所以<equation>r(A)\geqslant 2</equation>.因此，<equation>r(A)=2</equation>，从而向量组<equation>A\alpha_{1},A\alpha_{2},A\alpha_{3}</equation>的秩为2.

（法二）对矩阵<equation>A</equation>作初等行变换将其化为阶梯形矩阵，进而求得其秩.<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 2 \\ 0 & 1 & 1 \end{array} \right) \xrightarrow {r _ {2} - r _ {1}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 1 & 1 \end{array} \right) \xrightarrow {r _ {3} - r _ {2} ^ {*}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每作一次初等行变换，加一个 *.）

因此，<equation>r(\mathbf{A}) = 2.</equation>（法三）令<equation>\boldsymbol{\beta}_{1}=(1,1,0)^{\mathrm{T}},\boldsymbol{\beta}_{2}=(0,1,1)^{\mathrm{T}},\boldsymbol{\beta}_{3}=(1,2,1)^{\mathrm{T}}</equation>，则<equation>\boldsymbol{A}=(\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3})</equation>.由于<equation>\boldsymbol{\beta}_{1}+\boldsymbol{\beta}_{2}=\boldsymbol{\beta}_{3}</equation>，故<equation>r(A)\leqslant 2</equation>.又因为<equation>\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2}</equation>线性无关，所以<equation>r(A)\geqslant 2</equation>.因此，<equation>r(A)=2.</equation>

---

**2012年第13题 | 填空题 | 4分**
13. 设<equation>\alpha</equation>为 3 维单位列向量,<equation>E</equation>为 3 阶单位矩阵, 则矩阵<equation>E - \alpha \alpha^{\mathrm{T}}</equation>的秩为 ___
**解析: **解 由于<equation>\boldsymbol{\alpha}</equation>为3维单位列向量，故<equation>\boldsymbol{\alpha}^{\mathrm{T}}\boldsymbol{\alpha}=\| \boldsymbol{\alpha}\|^{2}=1</equation>，从而<equation>(\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}})\boldsymbol{\alpha}=\boldsymbol{\alpha}(\boldsymbol{\alpha}^{\mathrm{T}}\boldsymbol{\alpha})=\boldsymbol{\alpha}</equation>，于是1为矩阵<equation>\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}}</equation>的非零特征值.又<equation>r(\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}})\leqslant r(\boldsymbol{\alpha})\leqslant1</equation>且<equation>\boldsymbol{\alpha}</equation>为非零向量，故<equation>r(\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}})=1</equation>，再由<equation>\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}}</equation>为实对称矩阵知，存在正交矩阵<equation>Q</equation>，使得<equation>Q^{-1}\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}}Q=\left( \begin{array}{c c c} 1 & & \\ & 0 & \\ & & 0 \end{array} \right)</equation>.于是<equation>Q ^ {- 1} \left(E - \alpha \alpha^ {\mathrm {T}}\right) Q = E - \left( \begin{array}{c c c} 1 & & \\ & 0 & \\ & & 0 \end{array} \right) = \left( \begin{array}{c c c} 0 & & \\ & 1 & \\ & & 1 \end{array} \right).</equation>因此，<equation>r(\boldsymbol{E} - \boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}}) = 2.</equation>

---

**2010年第5题 | 选择题 | 4分 | 答案: A**
5. 设 A为<equation>m \times n</equation>矩阵，B为<equation>n \times m</equation>矩阵，E为m阶单位矩阵，若<equation>A B=E</equation>，则（    )

A. 秩<equation>r ( A )=m</equation>，秩<equation>r ( B )=m</equation>B. 秩<equation>r ( A )=m</equation>，秩<equation>r ( B )=n</equation>C. 秩<equation>r ( A )=n</equation>，秩<equation>r ( B )=m</equation>D. 秩<equation>r ( A )=n</equation>，秩<equation>r ( B )=n</equation>
答案: A
**解析: **（法一）由于<equation>m = r (\boldsymbol {E}) = r (\boldsymbol {A B}) \leqslant r (\boldsymbol {A}) \leqslant \min \{m, n \} \leqslant m,</equation><equation>m = r (\boldsymbol {E}) = r (\boldsymbol {A B}) \leqslant r (\boldsymbol {B}) \leqslant \min \{m, n \} \leqslant m,</equation>故<equation>r(\mathbf{A})=m,r(\mathbf{B})=m.</equation>应选A.

（法二）由<equation>AB=E</equation>知，B是矩阵方程<equation>AX=E</equation>的解.又矩阵方程<equation>AX=E</equation>有解的充要条件是秩<equation>r(A)=r(A,E)</equation>，故<equation>r (\boldsymbol {A}) = r (\boldsymbol {A}, \boldsymbol {E}) = m.</equation>同理由<equation>\mathbf{B}^{\mathrm{T}}\mathbf{A}^{\mathrm{T}}=\mathbf{E}^{\mathrm{T}}=\mathbf{E}</equation>知，<equation>r(\mathbf{B}^{\mathrm{T}})=r(\mathbf{B}^{\mathrm{T}},\mathbf{E})=m</equation>从而<equation>r(\mathbf{B})=r(\mathbf{B}^{\mathrm{T}})=m.</equation>应选A.

（法三）由于<equation>m=r(\mathbf{A B})\leqslant r(\mathbf{A})\leqslant n</equation>，故取<equation>m=1,n=2,\mathbf{A}=(1,0),\mathbf{B}=(1,0)^{\mathrm{T}}</equation>满足AB<equation>= E</equation>，此时<equation>r(\mathbf{A})=r(\mathbf{B})=1.</equation>由排除法可知，应选A.

---


#### 矩阵的运算与变换

**2022年第15题 | 填空题 | 5分**

15. 已知矩阵 A和 E-A可逆，其中 E为单位矩阵，若矩阵 B满足<equation>[ E-( E-A)^{-1} ] B=A</equation>，则 B-A=___

**答案:**<equation>- E.</equation>

**解析:**解（法一）在<equation>[E - (E - A)^{-1}]B = A</equation>两端同时左乘<equation>E - A</equation>，可得<equation>[ \boldsymbol {E} - \boldsymbol {A} - (\boldsymbol {E} - \boldsymbol {A}) (\boldsymbol {E} - \boldsymbol {A}) ^ {- 1} ] \boldsymbol {B} = (\boldsymbol {E} - \boldsymbol {A}) \boldsymbol {A}.</equation>展开整理，可得<equation>- AB=A-A^{2}.</equation>由于<equation>A</equation>可逆，故上式两端同时左乘<equation>A^{-1}</equation>可得<equation>-B = E - A</equation>，即<equation>B - A = -E</equation>（法二）注意到<equation>[E - (E - A)^{-1}](E - A) = E - A - E = -A</equation>，故由A可逆可得，<equation>[E - (E - A)^{-1}](E - A)(-A^{-1}) = E</equation>即<equation>[E - (E - A)^{-1}](E - A^{-1}) = E.</equation>于是，<equation>E - (E - A)^{-1}</equation>与<equation>E - A^{-1}</equation>互为逆矩阵.

在<equation>[E - (E - A)^{-1}]B = A</equation>两端同时左乘<equation>E - A^{-1}</equation>，可得<equation>B = (E - A^{-1})A = A - E.</equation>因此，<equation>B - A = -E.</equation>

---

**2020年第5题 | 选择题 | 4分 | 答案: B**

5. 若矩阵 A经过初等列变换化成 B，则（    ）

A. 存在矩阵 P，使得<equation>P A=B</equation>B. 存在矩阵 P，使得<equation>B P=A</equation>C. 存在矩阵 P，使得<equation>P B=A</equation>D. 方程组<equation>A x=0</equation>与<equation>B x=0</equation>同解

答案: B

**解析:**解 若矩阵 A经过初等列变换化成 B，则存在初等矩阵<equation>Q_{1}, Q_{2}, \dots , Q_{n}</equation>，使得<equation>A Q_{1} Q_{2}\cdots Q_{n}=B.</equation>令<equation>Q=Q_{1} Q_{2}\cdots Q_{n}</equation>，则 Q为可逆矩阵，且<equation>A Q=B.</equation>令 P=<equation>Q^{-1}</equation>，则 BP=A.

因此，应选B.

若矩阵 A经过初等行变换化成 B，则选项 A、C、D正确.

---

**2012年第6题 | 选择题 | 4分 | 答案: B**

6. 设 A为3阶矩阵，P为3阶可逆矩阵，且<equation>P^{-1} A P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>若<equation>P=(\alpha_{1},\alpha_{2},\alpha_{3})</equation><equation>Q=(\alpha_{1}+\alpha_{2},\alpha_{2},\alpha_{3})</equation>，则<equation>Q ^ {- 1} A Q = (\quad)</equation>A.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>

答案: B

**解析:**解（法一）由题设知，<equation>Q=P\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，故<equation>Q^{-1}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) P^{-1}</equation>. 从而<equation>\begin{aligned} Q ^ {- 1} A Q &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 0 & 0 & 1  \right) P ^ {- 1} A P \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1  \right) \\ &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 0 & 0 & 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1  \right) &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2  \right). \end{aligned}</equation>应选B.

（法二）由题设知，1，1，2是<equation>\boldsymbol{A}</equation>的特征值，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>分别是属于特征值1，1，2的特征向量，即<equation>A \alpha_ {1} = \alpha_ {1}, \quad A \alpha_ {2} = \alpha_ {2}, \quad A \alpha_ {3} = 2 \alpha_ {3}.</equation>从而<equation>A\left(\alpha_{1} + \alpha_{2}\right) = \alpha_{1} + \alpha_{2},\alpha_{1} + \alpha_{2}</equation>也是<equation>A</equation>的属于特征值1的特征向量.<equation>A Q = A \left(\alpha_ {1} + \alpha_ {2}, \alpha_ {2}, \alpha_ {3}\right) = \left(\alpha_ {1} + \alpha_ {2}, \alpha_ {2}, 2 \alpha_ {3}\right) = Q \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>又由于<equation>Q</equation>由<equation>P</equation>作初等变换得到，<equation>P</equation>可逆，故<equation>Q</equation>可逆.于是<equation>Q^{-1}AQ=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>应选B.

---

**2011年第5题 | 选择题 | 4分 | 答案: D**

5. 设 A为3阶矩阵，将 A的第2列加到第1列得矩阵 B，再交换 B的第2行与第3行得单位矩阵.记<equation>\boldsymbol {P} _ {1} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right), \boldsymbol {P} _ {2} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{array} \right), \mathrm {则} \boldsymbol {A} = (\quad)</equation>A.<equation>P_{1} P_{2}</equation>B.<equation>P_{1}^{-1} P_{2}</equation>C.<equation>P_{2} P_{1}</equation>D.<equation>P_{2} P_{1}^{-1}</equation>

答案: D

**解析:**解 将 A的第2列加到第1列对应 A右乘矩阵<equation>P_{1}</equation>，得<equation>B=A P_{1}</equation>.交换 B的第2行与第3行对应 B左乘矩阵<equation>P_{2}</equation>，得<equation>E=P_{2} A P_{1}</equation>.于是<equation>A=P_{2}^{-1} P_{1}^{-1}.</equation>又因为<equation>P_{2}^{-1}=P_{2}</equation>，所以<equation>A=P_{2} P_{1}^{-1}</equation>.应选 D.

---


#### 伴随矩阵与可逆矩阵

**2017年第5题 | 选择题 | 4分 | 答案: A**

5. 设<equation>\alpha</equation>为 n维单位列向量，<equation>E</equation>为 n阶单位矩阵，则（    ）

A.<equation>E-\alpha\alpha^{\mathrm{T}}</equation>不可逆 B.<equation>E+\alpha\alpha^{\mathrm{T}}</equation>不可逆 C.<equation>E+2\alpha\alpha^{\mathrm{T}}</equation>不可逆 D.<equation>E-2\alpha\alpha^{\mathrm{T}}</equation>不可逆

答案: A

**解析:**解（法一）由于<equation>\boldsymbol{\alpha}</equation>是n维单位列向量，故<equation>\operatorname{tr}(\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}})=\boldsymbol{\alpha}^{\mathrm{T}}\boldsymbol{\alpha}=1</equation>因为<equation>\boldsymbol{\alpha}</equation>非零，所以<equation>r(\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}})\geqslant 1.</equation>又由于<equation>r(\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}})\leqslant r(\boldsymbol{\alpha})=1</equation>故<equation>r(\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}})=1.</equation>于是矩阵<equation>\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}}</equation>的全部特征值为1，0，…，0，从而<equation>E-\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}}</equation>的全部特征值为0，1，…，1.因此，<equation>E-\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}}</equation>不可逆.应选A.

同理可得，<equation>\boldsymbol{E} +\alpha\boldsymbol{\alpha}^{\mathrm{T}}</equation>的全部特征值为2，1，…，1；<equation>\boldsymbol{E} +2\alpha\boldsymbol{\alpha}^{\mathrm{T}}</equation>的全部特征值为3，1，…，1；<equation>\boldsymbol{E} -2\alpha\boldsymbol{\alpha}^{\mathrm{T}}</equation>的全部特征值为-1，1，…，1.因此它们均可逆.

（法二）由于<equation>(\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}})\boldsymbol{\alpha} = \boldsymbol{\alpha} \left( \boldsymbol{\alpha}^{\mathrm{T}}\boldsymbol{\alpha} \right) = \boldsymbol{\alpha}</equation>，故<equation>\left(\boldsymbol {E} - \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}}\right) \boldsymbol {\alpha} = \boldsymbol {\alpha} - \left(\boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}}\right) \boldsymbol {\alpha} = \boldsymbol {\alpha} - \boldsymbol {\alpha} = \mathbf {0} = 0 \boldsymbol {\alpha}.</equation>于是，0是<equation>E-\alpha\alpha^{\mathrm{T}}</equation>的一个特征值（或<equation>( E-\alpha\alpha^{\mathrm{T}} ) x=0</equation>有非零解<equation>\alpha).</equation>因此，<equation>E-\alpha\alpha^{\mathrm{T}}</equation>不可逆.应选A. （法三）排除法.

令<equation>\alpha = (1,0,\dots ,0)^{\mathrm{T}}</equation>，则<equation>\alpha \alpha^{\mathrm{T}} = \left( \begin{array}{c c c c} 1 & & & \\ & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right)</equation>.

可以验证，<equation>\mathbf{E} + \alpha \alpha^{\mathrm{T}},\mathbf{E} + 2\alpha \alpha^{\mathrm{T}},\mathbf{E} - 2\alpha \alpha^{\mathrm{T}}</equation>均可逆，从而可以排除选项B、C、D.因此，应选A.

---

**2013年第13题 | 填空题 | 4分**

13. 设<equation>A=\left(a_{ij}\right)</equation>是3阶非零矩阵，<equation>|A|</equation>为 A的行列式，<equation>A_{ij}</equation>为<equation>a_{ij}</equation>的代数余子式. 若<equation>a_{ij}+A_{ij}=0</equation>（i,j=1,2,3），则<equation>|A|=</equation>___

**解析:**首先，由题设可知<equation>\boldsymbol {A} ^ {*} = \left( \begin{array}{c c c} A _ {1 1} & A _ {2 1} & A _ {3 1} \\ A _ {1 2} & A _ {2 2} & A _ {3 2} \\ A _ {1 3} & A _ {2 3} & A _ {3 3} \end{array} \right) \xlongequal {\text {a} _ {i j} + A _ {i j} = 0} \left( \begin{array}{c c c} - a _ {1 1} & - a _ {2 1} & - a _ {3 1} \\ - a _ {1 2} & - a _ {2 2} & - a _ {3 2} \\ - a _ {1 3} & - a _ {2 3} & - a _ {3 3} \end{array} \right) = - \boldsymbol {A} ^ {\mathrm {T}},</equation>故<equation>|\mathbf{A}|^3 = |\mathbf{A}\mathbf{A}^*| = |-\mathbf{A}\mathbf{A}^{\mathrm{T}}| = -|\mathbf{A}|^2.</equation>因此可以得到<equation>|\mathbf{A}| = 0,</equation>或<equation>|\mathbf{A}| = -1.</equation>另一方面，由于<equation>A</equation>为非零矩阵，故不妨假设<equation>a_{11} \neq 0</equation>，则<equation>| \boldsymbol {A} | = a _ {1 1} A _ {1 1} + a _ {1 2} A _ {1 2} + a _ {1 3} A _ {1 3} = - \left(a _ {1 1} ^ {2} + a _ {1 2} ^ {2} + a _ {1 3} ^ {2}\right) < 0.</equation>因此，<equation>|A| = -1.</equation>

---

**2011年第6题 | 选择题 | 4分 | 答案: D**

6. 设<equation>A=\left( \alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4} \right)</equation>是4阶矩阵，<equation>A^{*}</equation>为A的伴随矩阵.若<equation>(1,0,1,0)^{\mathrm{T}}</equation>是方程组<equation>A x=0</equation>的一个基础解系，则<equation>A^{*} x=0</equation>的基础解系可为（    ）

A.<equation>\alpha_{1},\alpha_{3}</equation>B.<equation>\alpha_{1},\alpha_{2}</equation>C.<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>D.<equation>\alpha_{2},\alpha_{3},\alpha_{4}</equation>

答案: D

**解析:**解 由于<equation>( 1, 0, 1, 0 )^{\mathrm{T}}</equation>为<equation>A x=0</equation>的一个基础解系，故该方程组的解集的秩为1，从而<equation>r ( A )=3.</equation>由<equation>r ( A )</equation>与<equation>r ( A^{*} )</equation>的关系可得<equation>r ( A^{*} )=1.</equation>于是<equation>A^{*} x=0</equation>的解集的秩为3，基础解系应包含3个线性无关的向量.因此，可以排除选项A、B.

由于<equation>r ( \mathbf{A})=3</equation><equation>| \mathbf{A} |=0</equation><equation>A^{*} A=| A | E=O</equation>，故 A的列向量均为<equation>A^{*} x=0</equation>的解.又因为<equation>r ( \mathbf{A})=3</equation>，所以可以从 A的列向量组中找出3个线性无关的列向量作为<equation>A^{*} x=0</equation>的一个基础解系.另一方面，由于<equation>( 1,0,1,0 )^{\mathrm{T}}</equation>是方程组<equation>A x=0</equation>的一个基础解系，故<equation>\left( \alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4}\right) \left( 1,0,1,0\right)^{\mathrm{T}}=\alpha_{1}+\alpha_{3}=0.</equation>于是<equation>\alpha_{1}</equation>与<equation>\alpha_{2}</equation>线性相关，因此可以排除选项C.由排除法知，应选D：

---

**2009年第6题 | 选择题 | 4分 | 答案: B**

5. 设 A,B均为2阶矩阵，<equation>A^{*}，B^{*}</equation>分别为 A,B的伴随矩阵，若<equation>|A|=2,|B|=3</equation>，则分块矩阵<equation>\left( \begin{array}{cc} O&A \\ B/O \end{array} \right)</equation>的伴随矩阵为（    ）

A.<equation>\left( \begin{array}{cc} O&3 B^{*} \\ 2 A^{*}&O \end{array} \right)</equation>B.<equation>\left( \begin{array}{cc} O&2 B^{*} \\ 3 A^{*}&O \end{array} \right)</equation>C.<equation>\left( \begin{array}{cc} O&3 A^{*} \\ 2 B^{*}&O \end{array} \right)</equation>D.<equation>\left( \begin{array}{cc} O&2 A^{*} \\ 3 B^{*}&O \end{array} \right)</equation>

答案: B

**解析:**解 （法一）先求<equation>\left| \begin{array}{ll}O&A\\ B/O \end{array} \right|.</equation>记<equation>C=\left( \begin{array}{cc}O&A\\ B/O \end{array} \right), C</equation>为4阶矩阵，A位于它的第1，2行和第3，4列，可按照以下步骤把C变为<equation>\left( \begin{array}{cc}A&O\\ O&B \end{array} \right).</equation>把C的第3列与第1列对换，第4列与第2列对换.

因此，<equation>\left| \begin{array}{c c} O & A \\ B & O \end{array} \right| = (- 1) ^ {2} \left| \begin{array}{c c} A & O \\ O & B \end{array} \right| = | A | | B | = 6.</equation><equation>\left( \begin{array}{cc}O&A\\ BO\end{array} \right)</equation>可逆.

由可逆矩阵与其伴随矩阵的关系可知，<equation>\left( \begin{array}{c c} \boldsymbol {O} & \boldsymbol {A} \\ \boldsymbol {B} & \boldsymbol {O} \end{array} \right) ^ {*} = \left| \begin{array}{c c} \boldsymbol {O} & \boldsymbol {A} \\ \boldsymbol {B} & \boldsymbol {O} \end{array} \right| \left( \begin{array}{c c} \boldsymbol {O} & \boldsymbol {A} \\ \boldsymbol {B} & \boldsymbol {O} \end{array} \right) ^ {- 1} = 6 \left( \begin{array}{c c} \boldsymbol {O} & \boldsymbol {A} \\ \boldsymbol {B} & \boldsymbol {O} \end{array} \right) ^ {- 1}.</equation>不妨设<equation>\left( \begin{array}{cc}O&A\\ B/O \end{array} \right)^{-1} = \left( \begin{array}{cc}X_1 & X_2\\ X_3 & X_4 \end{array} \right)</equation>，则<equation>\left( \begin{array}{c c} O & A \\ B & O \end{array} \right) \left( \begin{array}{c c} X _ {1} & X _ {2} \\ X _ {3} & X _ {4} \end{array} \right) = \left( \begin{array}{c c} A X _ {3} & A X _ {4} \\ B X _ {1} & B X _ {2} \end{array} \right) = \left( \begin{array}{c c} E & O \\ O & E \end{array} \right).</equation>由于 A,B均为可逆矩阵，故由<equation>AX_{4} = O, BX_{1} = O</equation>可知，<equation>X_{1} = X_{4} = O</equation>；由<equation>AX_{3} = E, BX_{2} = E</equation>得，<equation>X_{3} = A^{-1}, X_{2} = B^{-1}</equation>.

因此，<equation>\left( \begin{array}{c c} \boldsymbol {O} & \boldsymbol {A} \\ \boldsymbol {B} & \boldsymbol {O} \end{array} \right) ^ {- 1} = \left( \begin{array}{c c} \boldsymbol {O} & \boldsymbol {B} ^ {- 1} \\ \boldsymbol {A} ^ {- 1} & \boldsymbol {O} \end{array} \right).</equation><equation>\left( \begin{array}{c c} O & A \\ B & O \end{array} \right) ^ {*} = 6 \left( \begin{array}{c c} O & B ^ {- 1} \\ A ^ {- 1} & O \end{array} \right) = 6 \left( \begin{array}{c c} O & \frac {B ^ {*}}{| B |} \\ \frac {A ^ {*}}{| A |} & O \end{array} \right) = \left( \begin{array}{c c} O & 2 B ^ {*} \\ 3 A ^ {*} & O _ {1} \end{array} \right).</equation>应选B.

（法二）不妨设<equation>\left( \begin{array}{cc}O&A\\ B/O \end{array} \right)^{*} = \left( \begin{array}{cc}X_{1} & X_{2}\\ X_{3} & X_{4} \end{array} \right).</equation>由法一知，<equation>\left| \begin{array}{cc}O&A\\ BO\end{array}\right|=6</equation>故<equation>\left( \begin{array}{c c} \boldsymbol {O} & \boldsymbol {A} \\ \boldsymbol {B} & \boldsymbol {O} \end{array} \right) \left( \begin{array}{c c} X _ {1} & X _ {2} \\ X _ {3} & X _ {4} \end{array} \right) = \left( \begin{array}{c c} \boldsymbol {A X} _ {3} & \boldsymbol {A X} _ {4} \\ \boldsymbol {B X} _ {1} & \boldsymbol {B X} _ {2} \end{array} \right) = \left( \begin{array}{c c} 6 \boldsymbol {E} & \boldsymbol {O} \\ \boldsymbol {O} & 6 \boldsymbol {E} \end{array} \right).</equation>从而，<equation>\boldsymbol {A} \boldsymbol {X} _ {3} = 6 \boldsymbol {E}, \quad \boldsymbol {B} \boldsymbol {X} _ {2} = 6 \boldsymbol {E}, \quad \boldsymbol {A} \boldsymbol {X} _ {4} = \boldsymbol {B} \boldsymbol {X} _ {1} = \boldsymbol {O}.</equation>由此可推出，<equation>X_{3}=6 A^{-1}=6 \frac{A^{*}}{\mid A\mid}=3 A^{*}, X_{2}=6 B^{-1}=6 \frac{B^{*}}{\mid B\mid}=2 B^{*}, X_{1}=X_{4}=O.</equation>因此，<equation>\left( \begin{array}{cc} O & A \\ B & O \end{array} \right)^{*} = \left( \begin{array}{cc} O & 2 B^{*} \\ 3 A^{*} & O \end{array} \right).</equation>应选B.

（法三）特殊值法.

取<equation>A=\sqrt{2} E, B=\sqrt{3} E</equation>满足<equation>| A |=2, | B |=3</equation>，则<equation>A^{*} = | A | A^{-1} = \sqrt{2} E, B^{*} = | B | B^{-1} =</equation><equation>\sqrt{3} E.</equation>因此，<equation>\begin{aligned} \binom {O} {B} \frac {A}{O}) ^ {*} &= \binom {O} {\sqrt {3} E} \frac {\sqrt {2} E}{O}) ^ {*} = \left| \begin{array}{c c} O & \sqrt {2} E \\ \sqrt {3} E & O  \right| \left( \begin{array}{c c} O & \sqrt {2} E \\ \sqrt {3} E & O  \right) ^ {- 1} &= 6 \cdot \left( \begin{array}{c c} O & \frac {1}{\sqrt {3}} E \\ \frac {1}{\sqrt {2}} E & O  \right) \\ &= \left( \begin{array}{c c} O & 2 \sqrt {3} E \\ 3 \sqrt {2} E & O  \right) &= \left( \begin{array}{c c} O & 2 B ^ {*} \\ 3 A ^ {*} & O  \right). \end{aligned}</equation>应选B.

---


### 矩阵的特征值与特征向量


#### 特征值与特征向量

**2025年第21题 | 解答题 | 12分**
21. 设矩阵<equation>A=\left( \begin{array}{c c c} 0 & -1 & 2 \\ -1 & 0 & 2 \\ -1 & -1 & a \end{array} \right)</equation>，已知1是A的特征多项式的重根.

I. 求 a的值；

II. 求所有满足<equation>A\alpha = \alpha + \beta ,A^{2}\alpha = \alpha + 2\beta</equation>的非零向量<equation>\alpha ,\beta .</equation>
**答案: **（Ⅱ）<equation>\begin{aligned} \alpha &= c_{1}\left( 2 \\ 0 \\ 1  \right)+c_{2}\left( 0 \\ 2 \\ 1  \right)+\left( \begin{array}{c}-k \\ 0 \\ 0  \right),\beta &= k\left( 1 \\ 1 \\ 1  \right) \end{aligned}</equation>，其中<equation>c_{1},c_{2}</equation>为任意常数，<equation>k</equation>为任意非零常数.
**解析: **解（I）计算 A的特征多项式.<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda & 1 & - 2 \\ 1 & \lambda & - 2 \\ 1 & 1 & \lambda - a  \right| \xlongequal {r _ {1} - r _ {2}} \left| \begin{array}{c c c} \lambda - 1 & 1 - \lambda & 0 \\ 1 & \lambda & - 2 \\ 1 & 1 & \lambda - a  \right| &= (\lambda - 1) \left| \begin{array}{c c c} 1 & - 1 & 0 \\ 1 & \lambda & - 2 \\ 1 & 1 & \lambda - a  \right| \\ &= (\lambda - 1) \left| \begin{array}{c c c} 1 & 0 & 0 \\ 1 & \lambda + 1 & - 2 \\ 1 & 2 & \lambda - a  \right| &= (\lambda - 1) \left[ \lambda^ {2} + (1 - a) \lambda - a + 4 \right]. \end{aligned}</equation>由于1是A的特征多项式的重根，故<equation>\lambda=1</equation>是<equation>\lambda^{2}+(1-a)\lambda-a+4=0</equation>的一个根.将<equation>\lambda=1</equation>代入该式得<equation>1+1-a-a+4=0</equation>，解得 a=3.

因此，<equation>a=3.</equation>（Ⅱ）由第（I）问可知，<equation>A=\left( \begin{array}{c c c} 0 & -1 & 2 \\ -1 & 0 & 2 \\ -1 & -1 & 3 \end{array} \right).</equation>由<equation>A\alpha = \alpha +\beta ,A^{2}\alpha = \alpha +2\beta</equation>可得，<equation>A ^ {2} \alpha = A (A \alpha) = A \alpha + A \beta = \alpha + \beta + A \beta = \alpha + 2 \beta .</equation>由此可得<equation>A\beta = \beta .</equation>考虑方程组（A-E）x=0.<equation>A - E = \left( \begin{array}{c c c} - 1 & - 1 & 2 \\ - 1 & - 1 & 2 \\ - 1 & - 1 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & - 2 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>\beta = k_{1}\left( \begin{array}{c}2\\ 0\\ 1 \end{array} \right)+k_{2}\left( \begin{array}{c}0\\ 2\\ 1 \end{array} \right)=\left( \begin{array}{c}2k_{1}\\ 2k_{2}\\ k_{1}+k_{2} \end{array} \right)</equation>，其中<equation>k_{1},k_{2}</equation>是不全为零的任意常数.

由<equation>A\alpha = \alpha +\beta</equation>可得<equation>(A - E)\alpha = \beta</equation>，即<equation>\alpha</equation>是方程组<equation>(A - E)x = \beta</equation>的非零解.<equation>(A - E, \beta) = \left( \begin{array}{c c c c} - 1 & - 1 & 2 & 2 k _ {1} \\ - 1 & - 1 & 2 & 2 k _ {2} \\ - 1 & - 1 & 2 & k _ {1} + k _ {2} \end{array} \right) \xrightarrow [ r _ {3} - r _ {1} ]{r _ {2} - r _ {1}} \left( \begin{array}{c c c c} - 1 & - 1 & 2 & 2 k _ {1} \\ 0 & 0 & 0 & 2 \left(k _ {2} - k _ {1}\right) \\ 0 & 0 & 0 & k _ {2} - k _ {1} \end{array} \right).</equation>由此可得，当且仅当<equation>k_{1} = k_{2}</equation>时，方程组<equation>(A - E)x = \beta</equation>有解. 从而，<equation>\beta = 2 k_{1}\left( \begin{array}{c}1\\ 1\\ 1 \end{array} \right) = k\left( \begin{array}{c}1\\ 1\\ 1 \end{array} \right)</equation>其中<equation>k=2 k_{1}</equation>为任意非零常数.

进一步可得方程组<equation>( A - E ) x = \beta</equation>的通解<equation>\alpha = c_{1}\left( \begin{array}{c} 2 \\ 0 \\ 1 \end{array} \right) + c_{2}\left( \begin{array}{c} 0 \\ 2 \\ 1 \end{array} \right) + \left( \begin{array}{c} - k \\ 0 \\ 0 \end{array} \right)</equation>，其中<equation>c_{1}, c_{2}</equation>为任意常数.又因为<equation>\beta\neq0</equation>，所以<equation>\alpha\neq0.</equation>因此，<equation>\alpha = c_{1}\left( \begin{array}{c}2\\ 0\\ 1 \end{array} \right) + c_{2}\left( \begin{array}{c}0\\ 2\\ 1 \end{array} \right) + \left( \begin{array}{c}-k\\ 0\\ 0 \end{array} \right),\beta = k\left( \begin{array}{c}1\\ 1\\ 1 \end{array} \right)</equation>，其中<equation>c_{1},c_{2}</equation>为任意常数，<equation>k</equation>为任意非零常数.

---

**2024年第7题 | 选择题 | 5分 | 答案: A**
7. 设 A是秩为2的3阶矩阵，<equation>\alpha</equation>是满足<equation>A\alpha=0</equation>的非零向量. 若对满足<equation>\beta^{\mathrm{T}}\alpha=0</equation>的3维列向量<equation>\beta</equation>，均有<equation>A\beta=\beta</equation>则（    )

A.<equation>A^{3}</equation>的迹为2 B.<equation>A^{3}</equation>的迹为5 C.<equation>A^{2}</equation>的迹为8 D.<equation>A^{2}</equation>的迹为9
答案: A
**解析: **由<equation>\alpha</equation>是满足<equation>A\alpha=0</equation>的非零向量可知，A有一个属于特征值0的特征向量<equation>\alpha.</equation>满足<equation>\beta^{\mathrm{T}}\alpha = 0</equation>的向量<equation>\beta</equation>也满足<equation>\alpha^{\mathrm{T}}\beta = 0</equation>，从而是<equation>\alpha^{\mathrm{T}}x = 0</equation>的解。由于该方程组的系数矩阵的秩为1，故该方程组有两个线性无关的解。于是，存在两个线性无关的向量<equation>\beta_{1},\beta_{2}</equation>，使得<equation>\alpha^{\mathrm{T}}\beta_{i} = 0(i = 1,2)</equation>，即<equation>\beta_{i}^{\mathrm{T}}\alpha = 0(i = 1,2)</equation>。结合满足<equation>\beta^{\mathrm{T}}\alpha = 0</equation>的向量均满足<equation>A\beta = \beta</equation>可知，<equation>A\beta_{1} = \beta_{1},A\beta_{2} = \beta_{2}</equation>，故<equation>\beta_{1},\beta_{2}</equation>是A的属于特征值1的两个线性无关的特征向量.

由于属于不同特征值的特征向量线性无关，故<equation>\alpha, \beta_{1}, \beta_{2}</equation>是A的三个线性无关的特征向量.又因为A是3阶矩阵，所以A的特征值为1，1，0.进一步可得<equation>A^{2}, A^{3}</equation>的特征值均为1，1，0，从而<equation>\operatorname{tr}(A^{2})=\operatorname{tr}(A^{3})=2.</equation>因此，应选A.

---

**2018年第13题 | 填空题 | 4分**
13. 设2阶矩阵 A有两个不同特征值，<equation>\alpha_{1},\alpha_{2}</equation>是 A的线性无关的特征向量，且满足<equation>A^{2}(\alpha_{1}+\alpha_{2})=\alpha_{1}+\alpha_{2}</equation>，则<equation>|A|=</equation>
**答案: **-1.
**解析: **解 由于<equation>\alpha_{1},\alpha_{2}</equation>是A的线性无关的特征向量，而A有两个不同的特征值，故不妨分别记A的两个特征值为<equation>\lambda_{1},\lambda_{2},\alpha_{1}</equation>为属于<equation>\lambda_{1}</equation>的特征向量，<equation>\alpha_{2}</equation>为属于<equation>\lambda_{2}</equation>的特征向量.

由特征值与特征向量的定义可知，<equation>A\alpha_{1} = \lambda_{1}\alpha_{1},A\alpha_{2} = \lambda_{2}\alpha_{2}</equation>，从而<equation>A^{2}\alpha_{1} = \lambda_{1}^{2}\alpha_{1},A^{2}\alpha_{2} = \lambda_{2}^{2}\alpha_{2}</equation>于是，<equation>\boldsymbol {\alpha} _ {1} + \boldsymbol {\alpha} _ {2} = \boldsymbol {A} ^ {2} \left(\boldsymbol {\alpha} _ {1} + \boldsymbol {\alpha} _ {2}\right) = \lambda_ {1} ^ {2} \boldsymbol {\alpha} _ {1} + \lambda_ {2} ^ {2} \boldsymbol {\alpha} _ {2}.</equation>由（1）式可得，<equation>\left(\lambda_{1}^{2}-1\right)\boldsymbol{\alpha}_{1}+\left(\lambda_{2}^{2}-1\right)\boldsymbol{\alpha}_{2}=\mathbf{0}</equation>. 由于<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2}</equation>线性无关，故<equation>\lambda_{1}^{2}-1=0,\lambda_{2}^{2}-1=0.</equation>于是，<equation>\lambda_{1}^{2}=\lambda_{2}^{2}=1.</equation>又因为<equation>\lambda_{1}\neq \lambda_{2}</equation>所以<equation>\lambda_{1}=1,\lambda_{2}=-1</equation>或<equation>\lambda_{1}=-1,\lambda_{2}=1.</equation>不论是哪种情况，都有<equation>|A| = \lambda_{1}\lambda_{2} = -1.</equation>

---

**2011年第21题 | 解答题 | 11分**

设<equation>A</equation>为3阶实对称矩阵，<equation>A</equation>的秩为2，且<equation>1 \left( \begin{array}{c c} 1 & 1 \\ 0 & 0 \\ - 1 & 1 \end{array} \right) = \left( \begin{array}{c c} - 1 & 1 \\ 0 & 0 \\ 1 & 1 \end{array} \right)</equation>I. 求 A的所有特征值与特征向量；

II. 求矩阵 A.
**答案: **(21) （I）矩阵 A的特征值为-1，1，0.对应的特征向量分别为<equation>k_{1}(1,0,-1)^{\mathrm{T}}</equation><equation>k_{2}(1,0,1)^{\mathrm{T}}</equation><equation>k_{3}(0,1,0)^{\mathrm{T}}</equation>，其中<equation>k_{1},k_{2},k_{3}</equation>为任意非零常数；<equation>(\mathrm {I I}) \boldsymbol {A} = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{array} \right)</equation>
**解析: **解（I）由于<equation>A\left( \begin{array}{c c} 1 & 1 \\ 0 & 0 \\ -1 & 1 \end{array} \right)=\left( \begin{array}{c c} -1 & 1 \\ 0 & 0 \\ 1 & 1 \end{array} \right)</equation>，故<equation>\alpha_{1}=(1,0,-1)^{\mathrm{T}},\alpha_{2}=(1,0,1)^{\mathrm{T}}</equation>满足<equation>A\alpha_{1}=</equation><equation>-\alpha_{1},A\alpha_{2}=\alpha_{2}</equation>，从而<equation>\alpha_{1}</equation>为A的属于特征值-1的特征向量，<equation>\alpha_{2}</equation>为A的属于特征值1的特征向量.又因为<equation>r(A)=2,|A|=0</equation>，所以A还有一个特征值为零.

因为实对称矩阵属于不同特征值的特征向量相互正交，所以A的属于特征值0的特征向量<equation>\boldsymbol{\alpha}_{3} = (x_{1},x_{2},x_{3})^{\mathrm{T}}</equation>满足<equation>\boldsymbol{\alpha}_{1}^{\mathrm{T}}\boldsymbol{\alpha}_{3} = 0, \boldsymbol{\alpha}_{2}^{\mathrm{T}}\boldsymbol{\alpha}_{3} = 0</equation>从而得<equation>\left\{ \begin{array}{l l} x_{1} - x_{3} = 0, \\ x_{1} + x_{3} = 0. \end{array} \right.</equation>由此可得<equation>\boldsymbol{\alpha}_{3} = k_{3}(0,1,0)^{\mathrm{T}}, k_{3}</equation>为任意非零常数.

因此，<equation>\mathbf{A}</equation>的特征值为-1,1,0.对应的特征向量分别为<equation>k_{1}(1,0,-1)^{\mathrm{T}}</equation><equation>k_{2}(1,0,1)^{\mathrm{T}}</equation><equation>k_{3}(0,1,0)^{\mathrm{T}}</equation>其中<equation>k_{1},k_{2},k_{3}</equation>为任意非零常数.

（Ⅱ）（法一）由第（I）问可知，取<equation>P=\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)=\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \\ -1 & 1 & 0 \end{array} \right)</equation>，可得<equation>P^{-1}AP=</equation><equation>\left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>.于是<equation>A=P\left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right) P^{-1}.</equation>利用初等变换法计算<equation>P^{-1}</equation><equation>\begin{array}{l} (\boldsymbol {P}, \boldsymbol {E}) = \left( \begin{array}{c c c c c c} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 1 & 0 \\ - 1 & 1 & 0 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} + r _ {1}} \left( \begin{array}{c c c c c c} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 1 & 0 \\ 0 & 2 & 0 & 1 & 0 & 1 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {*} \times \frac {1}{2}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & \frac {1}{2} & 0 & - \frac {1}{2} \\ 0 & 0 & 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & \frac {1}{2} & 0 & \frac {1}{2} \end{array} \right) \xrightarrow {r _ {2} \leftrightarrow r _ {3} ^ {* *}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & \frac {1}{2} & 0 & - \frac {1}{2} \\ 0 & 1 & 0 & \frac {1}{2} & 0 & \frac {1}{2} \\ 0 & 0 & 1 & 0 & 1 & 0 \end{array} \right). \\ \end{array}</equation>于是，<equation>P^{-1}=\left( \begin{array}{c c c} \frac{1}{2} & 0 & -\frac{1}{2} \\ \frac{1}{2} & 0 & \frac{1}{2} \\ 0 & 1 & 0 \end{array} \right).</equation>因此，<equation>\begin{aligned} \boldsymbol {A} &= \boldsymbol {P} \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \boldsymbol {P} ^ {- 1} &= \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \\ - 1 & 1 & 0  \right) \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \left( \begin{array}{c c c} \frac {1}{2} & 0 & - \frac {1}{2} \\ \frac {1}{2} & 0 & \frac {1}{2} \\ 0 & 1 & 0  \right) \\ &= \left( \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & 0 & 0 \\ 1 & 1 & 0  \right) \left( \begin{array}{c c c} \frac {1}{2} & 0 & - \frac {1}{2} \\ \frac {1}{2} & 0 & \frac {1}{2} \\ 0 & 1 & 0  \right) &= \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0  \right). \end{aligned}</equation>或者，由<equation>\boldsymbol {A P} = \left(\boldsymbol {A} \alpha_ {1}, \boldsymbol {A} \alpha_ {2}, \boldsymbol {A} \alpha_ {3}\right) = \left(- \alpha_ {1}, \alpha_ {2}, 0\right)</equation>可得，<equation>\boldsymbol {A} = \left(- \alpha_ {1}, \alpha_ {2}, 0\right) \boldsymbol {P} ^ {- 1} = - \frac {1}{2} \left( \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & 0 & 0 \\ 1 & 1 & 0 \end{array} \right) \left( \begin{array}{c c c} - 1 & 0 & 1 \\ - 1 & 0 & - 1 \\ 0 & - 2 & 0 \end{array} \right) = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{array} \right).</equation>（法二）将<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>单位化，组成一正交矩阵<equation>Q = \left( \begin{array}{c c c} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0 \\ 0 & 0 & 1 \\ -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0 \end{array} \right)</equation>，则<equation>Q^{\mathrm{T}}AQ = \left( \begin{array}{c c c} -1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>.

因此，<equation>\begin{aligned} \boldsymbol {A} &= \boldsymbol {Q} \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \boldsymbol {Q} ^ {\mathrm {T}} &= \left( \begin{array}{c c c} \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {2}} & 0 \\ 0 & 0 & 1 \\ - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {2}} & 0  \right) \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \left( \begin{array}{c c c} \frac {1}{\sqrt {2}} & 0 & - \frac {1}{\sqrt {2}} \\ \frac {1}{\sqrt {2}} & 0 & \frac {1}{\sqrt {2}} \\ 0 & 1 & 0  \right) \\ &= \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0  \right). \end{aligned}</equation>

---

**2009年第13题 | 填空题 | 4分**
13. 若 3 维列向量<equation>\alpha, \beta</equation>满足<equation>\alpha^{\mathrm{T}}\beta=2</equation>, 其中<equation>\alpha^{\mathrm{T}}</equation>为<equation>\alpha</equation>的转置, 则矩阵<equation>\beta\alpha^{\mathrm{T}}</equation>的非零特征值为 ___
**解析: **解 由于<equation>r(\beta\alpha^{\mathrm{T}})\leqslant r(\beta)=1</equation>且<equation>\alpha, \beta</equation>均为非零向量，故<equation>r(\beta\alpha^{\mathrm{T}})=1.</equation>由分析中所给结论知，矩阵<equation>\beta\alpha^{\mathrm{T}}</equation>的所有特征值为<equation>\operatorname{tr}(\beta\alpha^{\mathrm{T}}),0,0.</equation>又<equation>\operatorname{tr}(\beta\alpha^{\mathrm{T}})=\operatorname{tr}(\alpha^{\mathrm{T}}\beta)=2</equation>（这里利用了<equation>\operatorname{tr}(AB)=\operatorname{tr}(BA)</equation>或者直接根据定义得<equation>\operatorname{tr}(\beta\alpha^{\mathrm{T}})=\alpha^{\mathrm{T}}\beta=2)</equation>，故矩阵<equation>\beta\alpha^{\mathrm{T}}</equation>的非零特征值为2.

---


#### 矩阵的相似与相似对角化

**2024年第21题 | 解答题 | 12分**

21. (本题满分12分)

已知数列<equation>\{x_{n}\} ,\{y_{n}\} ,\{z_{n}\}</equation>满足<equation>x_{0}=-1,y_{0}=0,z_{0}=2</equation>，且<equation>\left\{ \begin{array}{l l} x_{n}=-2x_{n-1}+2z_{n-1}, \\ y_{n}=-2y_{n-1}-2z_{n-1}, \\ z_{n}=-6x_{n-1}-3y_{n-1}+3z_{n-1}. \end{array} \right.</equation>记<equation>\alpha_{n}=\left( \begin{array}{l} x_{n} \\ y_{n} \\ z_{n} \end{array} \right)</equation>，写出满

足<equation>\alpha_{n} = A\alpha_{n - 1}</equation>的矩阵<equation>A</equation>，并求<equation>A^{n}</equation>及<equation>x_{n},y_{n},z_{n}</equation>（<equation>n = 1,2,\dots</equation>）.

**答案:**<equation>A = \left( \begin{array}{c c c} - 2 & 0 & 2 \\ 0 & - 2 & - 2 \\ - 6 & - 3 & 3 \end{array} \right)</equation>(2)<equation>\mathbf {A} ^ {n} = \left[ \begin{array}{c c c} - 4 - (- 2) ^ {n} & - 2 - (- 2) ^ {n} & 2 \\ 4 - (- 2) ^ {n + 1} & 2 - (- 2) ^ {n + 1} & - 2 \\ - 6 & - 3 & 3 \end{array} \right].</equation><equation>x _ {n} = 8 + (- 2) ^ {n}, y _ {n} = - 8 + (- 2) ^ {n + 1}, z _ {n} = 1 2 (n = 1, 2, \dots).</equation>

**解析:**21 已知数列<equation>\{x_{n}\}</equation>，<equation>\{y_{n}\}</equation>，<equation>\{z_{n}\}</equation>满足<equation>x_{0}=-1,y_{0}=0,z_{0}=2</equation>，且<equation>\left\{ \begin{array}{l l} x_{n}=-2x_{n-1}+2z_{n-1}, \\ y_{n}=-2y_{n-1}-2z_{n-1}, \\ z_{n}=-6x_{n-1}-3y_{n-1}+3z_{n-1}. \end{array} \right.</equation>记<equation>\boldsymbol{\alpha}_{n}=\left( \begin{array}{c}x_{n}\\ y_{n}\\ z_{n} \end{array} \right)</equation>，写出满足<equation>\boldsymbol{\alpha}_{n}=A\boldsymbol{\alpha}_{n-1}</equation>的矩阵A，并求<equation>A^{n}</equation>及<equation>x_{n},y_{n},z_{n} ( n=1,2,\dots).</equation>分析 本题主要考查矩阵的高次幂的计算.

由<equation>\left\{ \begin{array}{l l} x_{n}=-2x_{n-1}+2z_{n-1}, \\ y_{n}=-2y_{n-1}-2z_{n-1}, \\ z_{n}=-6x_{n-1}-3y_{n-1}+3z_{n-1} \end{array} \right.</equation>可以得到 A的表达式，计算 A的特征值与特征向量，并且将 A

相似对角化得到对角矩阵<equation>\boldsymbol{A}</equation>，即找到可逆矩阵 P，使得<equation>\boldsymbol{A}=\boldsymbol{P}^{-1}\boldsymbol{A}\boldsymbol{P}</equation>，则<equation>\boldsymbol{A}=\boldsymbol{P}\boldsymbol{\Lambda}\boldsymbol{P}^{-1},\boldsymbol{A}^{n}=\boldsymbol{P}\boldsymbol{\Lambda}^{n}\boldsymbol{P}^{-1}.</equation>进一步通过<equation>\alpha_{n}=A\alpha_{n}</equation>，可得<equation>\alpha_{n}=A^{n}\alpha_{0}</equation>，从而可计算出<equation>\alpha_{n}.</equation>解 由<equation>\left\{ \begin{array}{l l} x_{n}=-2 x_{n-1}+2 z_{n-1}, \\ y_{n}=-2 y_{n-1}-2 z_{n-1}, \\ z_{n}=-6 x_{n-1}-3 y_{n-1}+3 z_{n-1} \end{array} \right.</equation>可得<equation>\left( \begin{array}{c} x_{n} \\ y_{n} \\ z_{n} \end{array} \right)=\left( \begin{array}{c c c} -2 & 0 & 2 \\ 0 & -2 & -2 \\ -6 & -3 & 3 \end{array} \right)\left( \begin{array}{c} x_{n-1} \\ y_{n-1} \\ z_{n-1} \end{array} \right),</equation>即<equation>\boldsymbol{\alpha}_{n}=</equation><equation>\left( \begin{array}{c c c} -2 & 0 & 2 \\ 0 & -2 & -2 \\ -6 & -3 & 3 \end{array} \right)\boldsymbol{\alpha}_{n-1}.</equation>于是，<equation>A=\left( \begin{array}{c c c} -2 & 0 & 2 \\ 0 & -2 & -2 \\ -6 & -3 & 3 \end{array} \right).</equation>计算 A的特征值.<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda + 2 & 0 & - 2 \\ 0 & \lambda + 2 & 2 \\ 6 & 3 & \lambda - 3  \right| &= \left| \begin{array}{c c c} \lambda + 2 & \lambda + 2 & 0 \\ 0 & \lambda + 2 & 2 \\ 6 & 3 & \lambda - 3  \right| &= (\lambda + 2) \left| \begin{array}{c c c} 1 & 1 & 0 \\ 0 & \lambda + 2 & 2 \\ 6 & 3 & \lambda - 3  \right| \\ &= (\lambda + 2) \left| \begin{array}{c c c} 1 & 0 & 0 \\ 0 & \lambda + 2 & 2 \\ 6 & - 3 & \lambda - 3  \right| &= (\lambda + 2) \left[ (\lambda + 2) (\lambda - 3) + 6 \right] = \lambda (\lambda - 1) (\lambda + 2). \end{aligned}</equation>A的特征值为-2,1,0.

考虑<equation>(-2 E-A) x=0.</equation><equation>- 2 E-A=\left( \begin{array}{c c c} 0 & 0 & - 2 \\ 0 & 0 & 2 \\ 6 & 3 & - 5 \end{array} \right)\rightarrow\left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 6 & 3 & 0 \end{array} \right)\rightarrow\left( \begin{array}{c c c} 2 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation><equation>\xi_{1}=\left( \begin{array}{c}-1\\ 2\\ 0 \end{array} \right)</equation>为 A的属于特征值-2的一个特征向量.

考虑（<equation>E-A ) x=0.</equation><equation>E - A = \left( \begin{array}{c c c} 3 & 0 & - 2 \\ 0 & 3 & 2 \\ 6 & 3 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 3 & 0 & - 2 \\ 0 & 3 & 2 \\ 0 & 3 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 3 & 0 & - 2 \\ 0 & 3 & 2 \\ 0 & 0 & 0 \end{array} \right).</equation><equation>\xi_{2} = \left( \begin{array}{c}2\\ -2\\ 3 \end{array} \right)</equation>为A的属于特征值1的一个特征向量.

考虑<equation>(0E - A)x = 0</equation>.<equation>-A = \left( \begin{array}{c c c}2&0&-2\\0&2&2\\6&3&-3 \end{array} \right)\rightarrow \left( \begin{array}{c c c}1&0&-1\\0&1&1\\2&1&-1 \end{array} \right)\rightarrow \left( \begin{array}{c c c}1&0&-1\\0&1&1\\0&1&1 \end{array} \right)\rightarrow \left( \begin{array}{c c c}1&0&-1\\0&1&1\\0&0&0 \end{array} \right).</equation><equation>\xi_{3}=\left( \begin{array}{c}1\\ -1\\ 1 \end{array} \right)</equation>为 A的属于特征值0的一个特征向量.

令<equation>P=\left( \begin{array}{c c c} -1 & 2 & 1 \\ 2 & -2 & -1 \\ 0 & 3 & 1 \end{array} \right)</equation>，则<equation>P^{-1} A P=\left( \begin{array}{c c c} -2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right)=A.</equation><equation>P ^ {- 1}</equation><equation>\begin{array}{l} (P, E) = \left( \begin{array}{c c c c c c} - 1 & 2 & 1 & 1 & 0 & 0 \\ 2 & - 2 & - 1 & 0 & 1 & 0 \\ 0 & 3 & 1 & 0 & 0 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 1 & 1 & 0 \\ 2 & - 2 & - 1 & 0 & 1 & 0 \\ 0 & 3 & 1 & 0 & 0 & 1 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 1 & 1 & 0 \\ 0 & - 2 & - 1 & - 2 & - 1 & 0 \\ 0 & 3 & 1 & 0 & 0 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 1 & 1 & 0 \\ 0 & 1 & 0 & - 2 & - 1 & 1 \\ 0 & 3 & 1 & 0 & 0 & 1 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 1 & 1 & 0 \\ 0 & 1 & 0 & - 2 & - 1 & 1 \\ 0 & 0 & 1 & 6 & 3 & - 2 \end{array} \right). \\ \end{array}</equation>于是，<equation>P^{-1}=\left( \begin{array}{c c c} 1 & 1 & 0 \\ -2 & -1 & 1 \\ 6 & 3 & -2 \end{array} \right).</equation>由此可得，<equation>\begin{aligned} \boldsymbol {A} ^ {n} &= \boldsymbol {P} \boldsymbol {A} ^ {n} \boldsymbol {P} ^ {- 1} = \left( \begin{array}{c c c} - 1 & 2 & 1 \\ 2 & - 2 & - 1 \\ 0 & 3 & 1  \right) \left( \begin{array}{c c c} (- 2) ^ {n} & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \left( \begin{array}{c c c} 1 & 1 & 0 \\ - 2 & - 1 & 1 \\ 6 & 3 & - 2  \right) \\ &= \left( \begin{array}{c c c} (- 1) ^ {n - 1} \cdot 2 ^ {n} & 2 & 0 \\ (- 1) ^ {n} \cdot 2 ^ {n + 1} & - 2 & 0 \\ 0 & 3 & 0  \right) \left( \begin{array}{c c c} 1 & 1 & 0 \\ - 2 & - 1 & 1 \\ 6 & 3 & - 2  \right) \\ &= \left( \begin{array}{c c c} (- 1) ^ {n - 1} 2 ^ {n} - 4 & (- 1) ^ {n - 1} 2 ^ {n} - 2 & 2 \\ (- 1) ^ {n} 2 ^ {n + 1} + 4 & (- 1) ^ {n} 2 ^ {n + 1} + 2 & - 2 \\ - 6 & - 3 & 3  \right). \end{aligned}</equation>由<equation>\alpha_{n} = A\alpha_{n - 1}</equation>可得<equation>\alpha_{n} = A^{n}\alpha_{0}</equation>. 因此，<equation>\boldsymbol {\alpha} _ {n} = \left( \begin{array}{c c c} (- 1) ^ {n - 1} 2 ^ {n} - 4 & (- 1) ^ {n - 1} 2 ^ {n} - 2 & 2 \\ (- 1) ^ {n} 2 ^ {n + 1} + 4 & (- 1) ^ {n} 2 ^ {n + 1} + 2 & - 2 \\ - 6 & - 3 & 3 \end{array} \right) \left( \begin{array}{c} - 1 \\ 0 \\ 2 \end{array} \right) = \left( \begin{array}{c} (- 2) ^ {n} + 8 \\ (- 2) ^ {n + 1} - 8 \\ 1 2 \end{array} \right).</equation>从而<equation>x_{n} = (-2)^{n} + 8, y_{n} = (-2)^{n + 1} - 8, z_{n} = 12.</equation>

---

**2023年第6题 | 选择题 | 5分 | 答案: D**

6. 下列矩阵中不能相似于对角矩阵的是（    ）

A.

B.

C.

D.

答案: D

**解析:**<equation>\mathrm {已} A _ {1} = \left( \begin{array}{c c c} 1 & 1 & a \\ 0 & 2 & 2 \\ 0 & 0 & 3 \end{array} \right), A _ {2} = \left( \begin{array}{c c c} 1 & 1 & a \\ 1 & 2 & 0 \\ a & 0 & 3 \end{array} \right), A _ {3} = \left( \begin{array}{c c c} 1 & 1 & a \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{array} \right), A _ {4} = \left( \begin{array}{c c c} 1 & 1 & a \\ 0 & 2 & 2 \\ 0 & 0 & 2 \end{array} \right).</equation>注意到<equation>A_{2}</equation>为实对称矩阵，故必然相似于一个对角矩阵.

由于<equation>A_{1}, A_{3}, A_{4}</equation>均为上三角矩阵，故特征值即它们的对角线元素，从而<equation>A_{1}</equation>的特征值为1，2，3，<equation>A_{3}, A_{4}</equation>的特征值为1，2，2.

由<equation>A_{1}</equation>有3个不同的特征值可知，<equation>A_{1}</equation>相似于一个对角矩阵.

下面我们考虑<equation>A_{3}, A_{4}</equation>是否能相似于对角矩阵.<equation>A_{3}, A_{4}</equation>都有属于特征值1的特征向量<equation>(1,0,0)^{\mathrm{T}}.</equation>由于属于不同特征值的特征向量线性无关，故我们只需判定<equation>A_{3}, A_{4}</equation>的二重特征值2是否具有两个线性无关的特征向量即可确定它们是否一共具有3个线性无关的特征向量，从而相似于对角矩阵.

考虑方程组<equation>(2E - A_{3})x = 0,(2E - A_{4})x = 0.</equation><equation>2 \boldsymbol {E} - \boldsymbol {A} _ {3} = \left( \begin{array}{c c c} 1 & - 1 & - a \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right), \quad 2 \boldsymbol {E} - \boldsymbol {A} _ {4} = \left( \begin{array}{c c c} 1 & - 1 & - a \\ 0 & 0 & - 2 \\ 0 & 0 & 0 \end{array} \right).</equation>由于<equation>r(2E - A_{3}) = 1,r(2E - A_{4}) = 2</equation>，故方程组<equation>(2E - A_{3})x = 0</equation>有两个线性无关的解，从而<equation>A_{3}</equation>有两个线性无关的属于特征值2的特征向量，<equation>A_{3}</equation>相似于对角矩阵，方程组<equation>(2E - A_{4})x = 0</equation>只有一个线性无关的解，从而<equation>A_{4}</equation>只有一个线性无关的属于特征值2的特征向量，<equation>A_{4}</equation>不能相似于对角矩阵因此，应选D.

---

**2022年第5题 | 选择题 | 5分 | 答案: A**

5. 下列四个条件中，3阶矩阵 A可相似对角化的一个充分但不必要条件是（    ）

A. A有3个互不相等的特征值 B. A有3个线性无关的特征向量

C. A有3个两两线性无关的特征向量 D. A的属于不同特征值的特征向量相互正交

答案: A

**解析:**## 解 依次分析四个选项.

选项A是充分非必要条件.若矩阵A具有3个互不相等的特征值，则A有3个线性无关的特征向量，从而能够相似对角化.但是A能相似对角化并不意味着A一定有3个互不相等的特征值.例如3阶单位矩阵E，该矩阵自身即为对角矩阵，但仅有一个三重特征值1，没有不同的特征值.应选A.

选项B是充分必要条件.

选项C是必要非充分条件.若 A能相似对角化，则 A必然有3个线性无关的特征向量，从而有 3个两两线性无关的特征向量.

但反之并不成立，因为3个向量两两线性无关并不意味着3个向量线性无关。要举选项C不充分的例子，可以找到一个具有3重特征值，但却只有两个线性无关的特征向量的3阶矩阵.

取<equation>A = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>，则0是A的3重特征值，<equation>\xi_{1} = \left( \begin{array}{c} 1 \\ 0 \\ 0 \end{array} \right)</equation>和<equation>\xi_{2} = \left( \begin{array}{c} 0 \\ 1 \\ 0 \end{array} \right)</equation>是A的属于特征值0的两个线性无关的特征向量.取<equation>\xi_{3} = \left( \begin{array}{c} 1 \\ 1 \\ 0 \end{array} \right)</equation>，则<equation>\xi_{3}</equation>也是A的属于特征值0的一个特征向量，<equation>\xi_{1},\xi_{2},\xi_{3}</equation>两两线性无关，但是<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性相关，A也不能相似对角化.

选项D既不是充分条件，也不是必要条件。事实上，属于不同特征值的特征向量相互正交是实对称矩阵的性质，与是否可对角化没有直接联系。

下面说明选项D的不必要性.

取<equation>\xi_{1} = \left( \begin{array}{c}1\\ 0\\ 0 \end{array} \right),\xi_{2} = \left( \begin{array}{c}1\\ 1\\ 0 \end{array} \right),\xi_{3} = \left( \begin{array}{c}1\\ 0\\ 1 \end{array} \right)</equation>，则<equation>\xi_{1},\xi_{2},\xi_{3}</equation>两两不正交.令<equation>P = (\xi_{1},\xi_{2},\xi_{3}),A = \left( \begin{array}{c c c}1&0&0\\ 0&-1&0\\ 0&0&0 \end{array} \right)</equation>，则<equation>\boldsymbol {A} = \boldsymbol {P} \boldsymbol {\Lambda} \boldsymbol {P} ^ {- 1} = \left( \begin{array}{c c c} 1 & 1 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right) \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} 1 & - 2 & - 1 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>A与对角矩阵A相似，但是A的属于不同特征值的特征向量均不正交.

若 A是具有3个互不相等的特征值的3阶矩阵，则 A必然可相似对角化，故选项D不充分的例子，可以找只有两个不同特征值，且属于这两个不同特征值的特征向量相互正交，但是却不可以相似对角化的矩阵.

取<equation>A=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right)</equation>. 通过计算可发现该矩阵的特征值为0,1，其中0为二重特征值，但0没有两个线性无关的特征向量，从而 A不能相似对角化.

解<equation>( E-A ) x=0</equation>可得<equation>\xi_{1}=\left( \begin{array}{c} 1 \\ 0 \\ 0 \end{array} \right)</equation>为 A的属于特征值1的一个特征向量. 解<equation>( 0 E-A ) x=0</equation>可得<equation>\xi_{2}=\left( \begin{array}{c} 0 \\ 1 \\ 0 \end{array} \right)</equation>为 A的属于特征值0的一个特征向量.<equation>\xi_{1}</equation>与<equation>\xi_{2}</equation>为 A的属于不同特征值的特征向量，它们正交，且 A的任意属于不同特征值的特征向<equation>\xi_{1}</equation>与<equation>\xi_{2}</equation>为 A的属于不同特征值的特征向量，它们正交，且 A的任意属于不同特征值的特征向量均正交，但是 A不能相似对角化.

---

**2020年第21题 | 解答题 | 11分**

21. (本题满分11分)

设 A为2阶矩阵，<equation>P=(\alpha ,A\alpha)</equation>，其中<equation>\alpha</equation>是非零向量且不是 A的特征向量.

I. 证明 P为可逆矩阵；

II. 若<equation>A^{2}\alpha+A\alpha-6\alpha=0</equation>，求<equation>P^{-1}AP</equation>，并判断 A是否相似于对角矩阵.

**答案:**（I）证明略；

（Ⅱ）<equation>P^{-1} A P=\left( \begin{array}{cc} 0 & 6 \\ 1 & -1 \end{array} \right). A</equation>相似于对角矩阵<equation>\left( \begin{array}{c c} 2 & 0 \\ 0 & -3 \end{array} \right).</equation>

**解析:**解（I）要证明<equation>P</equation>为可逆矩阵，可证明<equation>\alpha, A\alpha</equation>线性无关.

假设<equation>\boldsymbol{\alpha},\boldsymbol{A}\boldsymbol{\alpha}</equation>线性相关，则存在不全为零的常数<equation>k_{1},k_{2}</equation>，使得<equation>k_{1}\boldsymbol{\alpha}+k_{2}\boldsymbol{A}\boldsymbol{\alpha}=\mathbf{0}.</equation>若<equation>k_{2}=0</equation>，则<equation>k_{1}\boldsymbol{\alpha}=\mathbf{0}.</equation>但<equation>\boldsymbol{\alpha}</equation>为非零向量，故<equation>k_{1}=0.</equation>这与假设矛盾.

若<equation>k_{2}\neq 0</equation>，则<equation>A\alpha=-\frac{k_{1}}{k_{2}}\alpha</equation>.由特征向量的定义可知<equation>\alpha</equation>为A的特征向量.这与<equation>\alpha</equation>不是A的特征向量矛盾.

因此，<equation>\alpha ,A\alpha</equation>线性无关.<equation>P</equation>为可逆矩阵.

（Ⅱ）考虑AP.<equation>\begin{aligned} A P &= \left(A \alpha , A ^ {2} \alpha\right) \xlongequal {A ^ {2} \alpha + A \alpha - 6 \alpha = 0} \left(A \alpha , 6 \alpha - A \alpha\right) = (\alpha , A \alpha) \left( \begin{array}{c c} 0 & 6 \\ 1 & - 1  \right) \\ &= P \left( \begin{array}{c c} 0 & 6 \\ 1 & - 1  \right). \end{aligned}</equation>由第（I）问可知，<equation>P</equation>可逆.上式两端同时左乘<equation>P^{-1}</equation>可得<equation>P^{-1} A P=\left( \begin{array}{c c} 0 & 6 \\ 1 & -1 \end{array} \right).</equation>记<equation>B=\left( \begin{array}{c c} 0 & 6 \\ 1 & -1 \end{array} \right)</equation>，则A与B相似.A与对角矩阵相似等价于B与对角矩阵相似计算B的特征多项式.<equation>| \lambda E - B | = \left| \begin{array}{c c} \lambda & - 6 \\ - 1 & \lambda + 1 \end{array} \right| = \lambda^ {2} + \lambda - 6 = (\lambda + 3) (\lambda - 2).</equation>2与-3是B的两个不同特征值.于是，B相似于对角矩阵<equation>\left( \begin{array}{cc}2&0\\ 0&-3 \end{array} \right).</equation>由相似关系的传递性可知，A相似于对角矩阵<equation>\left( \begin{array}{cc}2&0\\ 0&-3 \end{array} \right).</equation>

---

**2019年第21题 | 解答题 | 11分**

21. （本题满分11分）

已知矩阵<equation>A = \left( \begin{array}{c c c} - 2 & - 2 & 1 \\ 2 & x & - 2 \\ 0 & 0 & - 2 \end{array} \right)</equation>与<equation>B = \left( \begin{array}{c c c} 2 & 1 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & y \end{array} \right)</equation>相似.

I. 求 x,y;

II. 求可逆矩阵<equation>P</equation>使得<equation>P^{-1}AP = B</equation>.

**答案:**（I）<equation>x=3,y=-2;</equation>（Ⅱ）满足<equation>P^{-1} A P=B</equation>的可逆矩阵为<equation>P=\left( \begin{array}{c c c} - 1 & - 1 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right).</equation>

**解析:**解（I）由于<equation>A,B</equation>相似，故它们的迹与行列式均相同.

由 A,B有相同的迹可得<equation>- 4 + x = 1 + y</equation>即<equation>x - y = 5.</equation>计算<equation>|A|, |B|</equation>.<equation>B</equation>为上三角矩阵，故易得<equation>|B| = -2y.</equation><equation>| A | \xlongequal {\text {按 第三 行 展 开}} (- 2) \cdot \left| \begin{array}{c c} - 2 & - 2 \\ 2 & x \end{array} \right| = 4 x - 8.</equation>由<equation>|A| = |B|</equation>可得<equation>4x - 8 = -2y</equation>，即<equation>2x + y = 4.</equation>联立<equation>\left\{ \begin{array}{l l} x - y = 5, \\ 2x + y = 4 \end{array} \right.</equation>解得<equation>x = 3,y = -2.</equation>（Ⅱ）由于<equation>A, B</equation>相似，故它们有相同的特征值.

计算 B的特征多项式.<equation>| \lambda E - B | = \left| \begin{array}{c c c} \lambda - 2 & - 1 & 0 \\ 0 & \lambda + 1 & 0 \\ 0 & 0 & \lambda + 2 \end{array} \right| = (\lambda - 2) (\lambda + 1) (\lambda + 2).</equation>于是，<equation>\boldsymbol{B}</equation>的特征值为2，-1，-2.从而<equation>\boldsymbol{A}</equation>的特征值也为2，-1，-2.

由于 A,B具有3个不同的特征值2，-1，-2，故存在可逆矩阵<equation>P_{1}, P_{2}</equation>，使得<equation>P_{1}^{-1} A P_{1}=</equation><equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -2 \end{array} \right), P_{2}^{-1} B P_{2}=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -2 \end{array} \right).</equation><equation>\text {令} \boldsymbol {P} = \boldsymbol {P} _ {1} \boldsymbol {P} _ {2} ^ {- 1}, \text {则} \boldsymbol {P} ^ {- 1} \boldsymbol {A P} = \boldsymbol {P} _ {2} \boldsymbol {P} _ {1} ^ {- 1} \boldsymbol {A P} _ {1} \boldsymbol {P} _ {2} ^ {- 1} = \boldsymbol {P} _ {2} \left(\boldsymbol {P} _ {1} ^ {- 1} \boldsymbol {A P} _ {1}\right) \boldsymbol {P} _ {2} ^ {- 1} = \boldsymbol {B}.</equation><equation>P_{1}</equation>的列向量为A的属于特征值2，-1，-2的特征向量，<equation>P_{2}</equation>的列向量为B的属于特征值2，-1， -2的特征向量.下面分别计算A，B的特征向量.

计算<equation>A</equation>的属于特征值2的特征向量.考虑<equation>(2E - A)x = 0.</equation><equation>2 \boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} 4 & 2 & - 1 \\ - 2 & - 1 & 2 \\ 0 & 0 & 4 \end{array} \right) \xrightarrow [ r _ {1} + r _ {3} ^ {*} ]{r _ {3} \times \frac {1}{4}} \left( \begin{array}{c c c} 4 & 2 & 0 \\ - 2 & - 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {2} ^ {*} \times (- 1) ]{r _ {1} ^ {*} + 2 r _ {2} ^ {*}} \left( \begin{array}{c c c} 0 & 0 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>于是，<equation>r ( 2 E - A ) = 2</equation>，求得<equation>\boldsymbol{\xi}_{1}=(-1,2,0)^{\mathrm{T}}</equation>为<equation>( 2 E-A ) x=0</equation>的一个基础解系.<equation>(-1,2,0)^{\mathrm{T}}</equation>为 A的属于特征值2的特征向量.

计算<equation>A</equation>的属于特征值-1的特征向量.考虑<equation>(- E - A) x = 0.</equation><equation>- \boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} 1 & 2 & - 1 \\ - 2 & - 4 & 2 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {1} + r _ {3} ]{r _ {2} + 2 r _ {1}} \left( \begin{array}{c c c} 1 & 2 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>于是，<equation>r(-E-A)=2</equation>，求得<equation>\boldsymbol{\xi}_{2}=(-2,1,0)^{\mathrm{T}}</equation>为<equation>(-E-A)\boldsymbol{x}=\mathbf{0}</equation>的一个基础解系.<equation>(-2,1,0)^{\mathrm{T}}</equation>为 A的属于特征值-1的特征向量.

计算<equation>A</equation>的属于特征值-2的特征向量.考虑<equation>(-2E - A)x = 0.</equation><equation>- 2 \boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} 0 & 2 & - 1 \\ - 2 & - 5 & 2 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {2} + 2 r _ {1}} \left( \begin{array}{c c c} 0 & 2 & - 1 \\ - 2 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {2} ^ {*} \times (- 2) - r _ {1}} \left( \begin{array}{c c c} 0 & 2 & - 1 \\ 4 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r(-2 E-A)=2</equation>，求得<equation>\boldsymbol{\xi}_{3}=(-1,2,4)^{\mathrm{T}}</equation>为<equation>(-2 E-A) x=0</equation>的一个基础解系.<equation>(-1,2,4)^{\mathrm{T}}</equation>为 A的属于特征值-2的特征向量.<equation>\left( \begin{array}{c c c} - 1 & - 2 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right)</equation>计算 B的属于特征值2的特征向量.考虑<equation>( 2 E-B ) x=0.</equation><equation>2 \boldsymbol {E} - \boldsymbol {B} = \left( \begin{array}{c c c} 0 & - 1 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r ( 2 E-B )=2</equation>，求得<equation>\boldsymbol{\eta}_{1}=(1,0,0)^{\mathrm{T}}</equation>为<equation>( 2 E-B ) x=0</equation>的一个基础解系.<equation>( 1,0,0)^{\mathrm{T}}</equation>为B的属于特征值2的特征向量.

计算<equation>B</equation>的属于特征值-1的特征向量.考虑<equation>(-E - B)x = 0.</equation><equation>- \boldsymbol {E} - \boldsymbol {B} = \left( \begin{array}{c c c} - 3 & - 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {2} \leftrightarrow r _ {3} ]{r _ {1} \times (- 1)} \left( \begin{array}{c c c} 3 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r(-E-B)=2</equation>，求得<equation>\boldsymbol{\eta}_{2}=(-1,3,0)^{\mathrm{T}}</equation>为<equation>(-E-B)\boldsymbol{x}=\mathbf{0}</equation>的一个基础解系.<equation>(-1,3,0)^{\mathrm{T}}</equation>为 B的属于特征值-1的特征向量.

计算<equation>B</equation>的属于特征值-2的特征向量.考虑<equation>(-2E - B)x = 0.</equation><equation>- 2 \boldsymbol {E} - \boldsymbol {B} = \left( \begin{array}{c c c} - 4 & - 1 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {2} \times (- 1) ]{r _ {1} \times (- 1)} \left( \begin{array}{c c c} 4 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r(-2 E-B)=2</equation>，求得<equation>\boldsymbol{\eta}_{3}=(0,0,1)^{\mathrm{T}}</equation>为<equation>(-2 E-B) x=0</equation>的一个基础解系.<equation>(0,0,1)^{\mathrm{T}}</equation>为 B的属于特征值-2的特征向量.

因此，<equation>P_{2}</equation>可取为<equation>\left( \begin{array}{c c c} 1 & -1 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>利用初等变换法计算<equation>P_{2}^{-1}</equation><equation>\left(\boldsymbol {P} _ {2}, \boldsymbol {E}\right) = \left( \begin{array}{c c c c c c} 1 & - 1 & 0 & 1 & 0 & 0 \\ 0 & 3 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {1} + r _ {2} ^ {*} ]{r _ {2} \times \frac {1}{3}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 1 & \frac {1}{3} & 0 \\ 0 & 1 & 0 & 0 & \frac {1}{3} & 0 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right).</equation>于是，<equation>P_{2}^{-1} = \left( \begin{array}{c c c} 1 & \frac{1}{3} & 0 \\ 0 & \frac{1}{3} & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>综上所述，<equation>\boldsymbol {P} = \boldsymbol {P} _ {1} \boldsymbol {P} _ {2} ^ {- 1} = \left( \begin{array}{c c c} - 1 & - 2 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right) \left( \begin{array}{c c c} 1 & \frac {1}{3} & 0 \\ 0 & \frac {1}{3} & 0 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} - 1 & - 1 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right).</equation>

---

**2018年第5题 | 选择题 | 4分 | 答案: A**

5. 下列矩阵中，与矩阵<equation>\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>A.

相似的为（    ）<equation>\left( \begin{array}{c c c} 1 & 1 & - 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c} 1 & 1 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>

答案: A

**解析:**解 已知矩阵与四个选项中的矩阵的特征多项式均为<equation>( x-1 )^{3}</equation>，故1为这五个矩阵的三重特征值.

记<equation>A = \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E - A = \left( \begin{array}{c c c} 0 & -1 & 0 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r(E - A) = 2.</equation>记<equation>B_{1} = \left( \begin{array}{c c c} 1 & 1 & -1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E - B_{1} = \left( \begin{array}{c c c} 0 & -1 & 1 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r(E - B_{1}) = 2.</equation>记<equation>B_{2} = \left( \begin{array}{c c c} 1 & 0 & -1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E - B_{2} = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r(E - B_{2}) = 1.</equation>记<equation>B_{3} = \left( \begin{array}{c c c} 1 & 1 & -1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E - B_{3} = \left( \begin{array}{c c c} 0 & -1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r(E - B_{3}) = 1.</equation>记<equation>B_{4} = \left( \begin{array}{c c c} 1 & 0 & -1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E - B_{4} = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r(E - B_{4}) = 1.</equation>由上可见，只有<equation>E - B_{1}</equation>与<equation>E - A</equation>的秩相等，而<equation>E - B_{i} ( i = 2,3,4)</equation>与<equation>E - A</equation>的秩均不相等，故<equation>E - B_{i} ( i = 2,3,4)</equation>与<equation>E - A</equation>不相似，从而A与<equation>B_{i} ( i = 2,3,4)</equation>不相似.

由排除法可知，应选A.

---

**2017年第6题 | 选择题 | 4分 | 答案: B**

6. 已知矩阵<equation>A = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 1 \end{array} \right), B = \left( \begin{array}{c c c} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right), C = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{array} \right),</equation>则（    ）

A. A与C相似，B与C相似 B. A与C相似，B与C不相似

C. A与C不相似，B与C相似 D. A与C不相似，B与C不相似

答案: B

**解析:**解求得 A,B,C的特征多项式，均为<equation>(\lambda-2)^{2} (\lambda-1)</equation>，故 A,B,C具有相同的特征值，其中2是二重特征值.

矩阵<equation>C</equation>是对角矩阵，故其相似于其自身.

考虑属于特征值2的特征向量.<equation>2 \boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 0 & - 1 \\ 0 & 0 & 1 \end{array} \right), \quad 2 \boldsymbol {E} - \boldsymbol {B} = \left( \begin{array}{c c c} 0 & - 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>由上可知，<equation>r ( 2 E-A )=1</equation><equation>r ( 2 E-B )=2</equation>.于是，<equation>( 2 E-A ) x=0</equation>的基础解系包含两个向量，A有2个线性无关的属于特征值2的特征向量；而<equation>( 2 E-B ) x=0</equation>的基础解系只包含一个向量，B只有1个线性无关的属于特征值2的特征向量.

因此，加上属于特征值1的特征向量，A共有3个线性无关的特征向量，A与C相似；B只有2个线性无关的特征向量，B与C不相似.应选B.

---

**2016年第5题 | 选择题 | 4分 | 答案: C**

5. 设 A,B是可逆矩阵，且 A与 B相似，则下列结论错误的是（    ）

A.<equation>A^{\mathrm{T}}</equation>与<equation>B^{\mathrm{T}}</equation>相似 B.<equation>A^{-1}</equation>与<equation>B^{-1}</equation>相似

C.<equation>A+A^{\mathrm{T}}</equation>与<equation>B+B^{\mathrm{T}}</equation>相似 D.<equation>A+A^{-1}</equation>与<equation>B+B^{-1}</equation>相似

答案: C

**解析:**解 由于<equation>A</equation>与<equation>B</equation>相似，故存在可逆矩阵<equation>P</equation>，使得<equation>B = P^{-1}AP</equation>-<equation>\boldsymbol{B}^{\mathrm{T}}=\boldsymbol{P}^{\mathrm{T}}\boldsymbol{A}^{\mathrm{T}}(\boldsymbol{P}^{-1})^{\mathrm{T}}=\boldsymbol{P}^{\mathrm{T}}\boldsymbol{A}^{\mathrm{T}}(\boldsymbol{P}^{\mathrm{T}})^{-1}</equation>，选项A中的结论正确.

-<equation>B^{-1}=P^{-1} A^{-1} \left(P^{-1}\right)^{-1}=P^{-1} A^{-1} P</equation>，选项B中的结论正确.

- 由<equation>B=P^{-1} A P</equation>和<equation>B^{-1}=P^{-1} A^{-1} P</equation>可知，<equation>B+B^{-1}=P^{-1}(A+A^{-1}) P</equation>，选项D中的结论正确由排除法可知，应选C.

下面我们举例说明选项C不正确.

设<equation>A = \left( \begin{array}{cc}1 & 0\\ 0 & -1 \end{array} \right),P = \left( \begin{array}{cc}1 & 1\\ 2 & 1 \end{array} \right)</equation>，则<equation>P^{-1} = \left( \begin{array}{c c} - 1 & 1\\ 2 & -1 \end{array} \right)</equation>. 令<equation>\boldsymbol {B} = \boldsymbol {P} ^ {- 1} \boldsymbol {A P} = \left( \begin{array}{c c} - 1 & 1 \\ 2 & - 1 \end{array} \right) \left( \begin{array}{c c} 1 & 0 \\ 0 & - 1 \end{array} \right) \left( \begin{array}{c c} 1 & 1 \\ 2 & 1 \end{array} \right) = \left( \begin{array}{c c} - 3 & - 2 \\ 4 & 3 \end{array} \right),</equation>则<equation>\boldsymbol {A} + \boldsymbol {A} ^ {\mathrm {T}} = \left( \begin{array}{c c} 2 & 0 \\ 0 & - 2 \end{array} \right), \quad \boldsymbol {B} + \boldsymbol {B} ^ {\mathrm {T}} = \left( \begin{array}{c c} - 6 & 2 \\ 2 & 6 \end{array} \right).</equation>计算<equation>A + A^{\mathrm{T}}</equation>的特征多项式得<equation>\lambda^2 - 4</equation>，计算<equation>B + B^{\mathrm{T}}</equation>的特征多项式得<equation>\lambda^2 - 40</equation>因此，<equation>A + A^{\mathrm{T}}</equation>和<equation>B + B^{\mathrm{T}}</equation>不相似.

---

**2016年第21题 | 解答题 | 11分**

21. （本题满分11分）

已知矩阵<equation>A = \left( \begin{array}{c c c} 0 & -1 & 1 \\ 2 & -3 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>I. 求<equation>A^{99}</equation>;

II. 设3阶矩阵<equation>B=(\alpha_{1},\alpha_{2},\alpha_{3})</equation>满足<equation>B^{2}=B A</equation>记<equation>B^{100}=(\beta_{1},\beta_{2},\beta_{3})</equation>将<equation>\beta_{1},\beta_{2},\beta_{3}</equation>分别表示为<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>的线性组合.

**答案:**<equation>\begin{aligned} (\mathrm {I}) \boldsymbol {A} ^ {9 9} &= \left( \begin{array}{c c c} 2 ^ {9 9} - 2 & 1 - 2 ^ {9 9} & 2 - 2 ^ {9 8} \\ 2 ^ {1 0 0} - 2 & 1 - 2 ^ {1 0 0} & 2 - 2 ^ {9 9} \\ 0 & 0 & 0  \right). \\ (\mathrm {I I}) \boldsymbol {\beta} _ {1} &= \left(2 ^ {9 9} - 2\right) \boldsymbol {\alpha} _ {1} + \left(2 ^ {1 0 0} - 2\right) \boldsymbol {\alpha} _ {2}, \boldsymbol {\beta} _ {2} = \left(1 - 2 ^ {9 9}\right) \boldsymbol {\alpha} _ {1} + \left(1 - 2 ^ {1 0 0}\right) \boldsymbol {\alpha} _ {2}, \boldsymbol {\beta} _ {3} = \left(2 - 2 ^ {9 8}\right) \boldsymbol {\alpha} _ {1} + \left(2 - 2 ^ {9 9}\right) \boldsymbol {\alpha} _ {2}. \end{aligned}</equation>

**解析:**（I）计算<equation>A</equation>的特征多项式<equation>|\lambda E - A|</equation>.<equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda & 1 & - 1 \\ - 2 & \lambda + 3 & 0 \\ 0 & 0 & \lambda \end{array} \right| \xlongequal {\text {按 第三 行 展开}} \lambda \left(\lambda^ {2} + 3 \lambda + 2\right) = \lambda (\lambda + 1) (\lambda + 2).</equation>因此，<equation>\mathbf{A}</equation>有3个不同的特征值：-2，-1，0.

由于属于不同特征值的特征向量线性无关，故A有3个线性无关的特征向量，A相似于对角矩阵<equation>\left( \begin{array}{c c c} - 2 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>分别计算 A的属于特征值-2，-1，0的特征向量.

当<equation>\lambda=-2</equation>时，解<equation>(-2 E-A) x=0.</equation>由于<equation>- 2 \boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} - 2 & 1 & - 1 \\ - 2 & 1 & 0 \\ 0 & 0 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} - 2 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right),</equation>故<equation>(1,2,0)^{\mathrm{T}}</equation>为<equation>A</equation>的属于特征值-2的一个特征向量.

当<equation>\lambda=-1</equation>时，解<equation>(-E-A)x=0.</equation>由于<equation>- \boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} - 1 & 1 & - 1 \\ - 2 & 2 & 0 \\ 0 & 0 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right),</equation>故<equation>(1,1,0)^{\mathrm{T}}</equation>为<equation>A</equation>的属于特征值-1的一个特征向量.

当<equation>\lambda=0</equation>时，解<equation>( 0 E-A ) x=0</equation>.由于<equation>0 E - A = \left( \begin{array}{c c c} 0 & 1 & - 1 \\ - 2 & 3 & 0 \\ 0 & 0 & 0 \end{array} \right),</equation>故<equation>(3,2,2)^{\mathrm{T}}</equation>为<equation>A</equation>的属于特征值0的一个特征向量.

令<equation>P = \left( \begin{array}{c c c} 1 & 1 & 3 \\ 2 & 1 & 2 \\ 0 & 0 & 2 \end{array} \right)</equation>，则<equation>P^{-1} A P = \left( \begin{array}{c c c} - 2 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>.

计算<equation>P^{-1}</equation>得，<equation>P^{-1} = \left( \begin{array}{c c c} - 1 & 1 & \frac{1}{2} \\ 2 & - 1 & - 2 \\ 0 & 0 & \frac{1}{2} \end{array} \right).</equation><equation>\begin{aligned} \boldsymbol {A} ^ {9 9} &= \boldsymbol {P} \left( \begin{array}{c c c} (- 2) ^ {9 9} & 0 & 0 \\ 0 & (- 1) ^ {9 9} & 0 \\ 0 & 0 & 0  \right) \boldsymbol {P} ^ {- 1} &= \left( \begin{array}{c c c} 1 & 1 & 3 \\ 2 & 1 & 2 \\ 0 & 0 & 2  \right) \left( \begin{array}{c c c} - 2 ^ {9 9} & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0  \right) \left( \begin{array}{c c c} - 1 & 1 & \frac {1}{2} \\ 2 & - 1 & - 2 \\ 0 & 0 & \frac {1}{2}  \right) \\ &= \left( \begin{array}{c c c} 2 ^ {9 9} - 2 & 1 - 2 ^ {9 9} & 2 - 2 ^ {9 8} \\ 2 ^ {1 0 0} - 2 & 1 - 2 ^ {1 0 0} & 2 - 2 ^ {9 9} \\ 0 & 0 & 0  \right). \end{aligned}</equation>（Ⅱ）先求<equation>B^{100}.</equation>由于<equation>B^{2}=B A</equation>，故<equation>\boldsymbol {B} ^ {3} = \boldsymbol {B} \left(\boldsymbol {B} ^ {2}\right) = \boldsymbol {B} (\boldsymbol {B A}) = \boldsymbol {B} ^ {2} \boldsymbol {A} = (\boldsymbol {B A}) \boldsymbol {A} = \boldsymbol {B A} ^ {2}.</equation>下面我们用数学归纳法证明<equation>B^{n}=B A^{n-1}, n=2, 3, \dots .</equation>当<equation>n = 2</equation>时，<equation>B^{2} = BA</equation>假设该命题对<equation>n = k</equation>成立，下面证明该命题对<equation>n = k + 1</equation>也成立.<equation>\boldsymbol {B} ^ {n} = \boldsymbol {B} ^ {k + 1} = \boldsymbol {B} \boldsymbol {B} ^ {k} \xlongequal {\text {归 纳 假 设}} \boldsymbol {B} \left(\boldsymbol {B} \boldsymbol {A} ^ {k - 1}\right) = \boldsymbol {B} ^ {2} \boldsymbol {A} ^ {k - 1} = (\boldsymbol {B} \boldsymbol {A}) \boldsymbol {A} ^ {k - 1} = \boldsymbol {B} \boldsymbol {A} ^ {k} = \boldsymbol {B} \boldsymbol {A} ^ {n - 1}.</equation>于是，该命题对 n=k+1也成立，从而由数学归纳法可知，该命题对所有<equation>\geqslant2</equation>的正整数均成立因此，<equation>\left(\boldsymbol {\beta} _ {1}, \boldsymbol {\beta} _ {2}, \boldsymbol {\beta} _ {3}\right) = \boldsymbol {B} ^ {1 0 0} = \boldsymbol {B A} ^ {9 9} = \left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\alpha} _ {2}, \boldsymbol {\alpha} _ {3}\right) \left( \begin{array}{c c c} 2 ^ {9 9} - 2 & 1 - 2 ^ {9 9} & 2 - 2 ^ {9 8} \\ 2 ^ {1 0 0} - 2 & 1 - 2 ^ {1 0 0} & 2 - 2 ^ {9 9} \\ 0 & 0 & 0 \end{array} \right).</equation>综上所述，<equation>\boldsymbol {\beta} _ {1} = \left(2 ^ {9 9} - 2\right) \boldsymbol {\alpha} _ {1} + \left(2 ^ {1 0 0} - 2\right) \boldsymbol {\alpha} _ {2},</equation><equation>\begin{aligned} \boldsymbol {\beta} _ {2} &= \left(1 - 2 ^ {9 9}\right) \boldsymbol {\alpha} _ {1} + \left(1 - 2 ^ {1 0 0}\right) \boldsymbol {\alpha} _ {2}, \\ \boldsymbol {\beta} _ {3} &= \left(2 - 2 ^ {9 8}\right) \boldsymbol {\alpha} _ {1} + \left(2 - 2 ^ {9 9}\right) \boldsymbol {\alpha} _ {2}. \end{aligned}</equation>

---

**2015年第21题 | 解答题 | 11分**

21. (本题满分11分)

设矩阵<equation>A = \left( \begin{array}{c c c} 0 & 2 & -3 \\ -1 & 3 & -3 \\ 1 & -2 & a \end{array} \right)</equation>相似于矩阵<equation>B = \left( \begin{array}{c c c} 1 & -2 & 0 \\ 0 & b & 0 \\ 0 & 3 & 1 \end{array} \right).</equation>I. 求 a,b的值；

II. 求可逆矩阵<equation>P</equation>，使<equation>P^{-1}AP</equation>为对角矩阵.

**答案:**(21) （I）<equation>a=4,b=5;</equation><equation>(\mathrm {I I}) \boldsymbol {P} = \left( \begin{array}{c c c} - 1 & 2 & - 3 \\ - 1 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right), \boldsymbol {P} ^ {- 1} \boldsymbol {A} \boldsymbol {P} = \left( \begin{array}{c c c} 5 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>

**解析:**解（I）由于 A,B相似，故存在可逆矩阵Q使得<equation>Q^{-1} A Q=B</equation>，从而<equation>|B|=|Q^{-1}| \cdot |A| \cdot</equation><equation>|Q|=|A|.</equation>计算得<equation>|A|=2 a-3,|B|=b.</equation>另一方面，A和B具有相同的迹，故<equation>3+a=2+b.</equation>联立得<equation>\left\{ \begin{array}{l l} a+3=b+2, \\ 2 a-3=b, \end{array} \right.</equation>解得<equation>\left\{ \begin{array}{l l} a=4, \\ b=5. \end{array} \right.</equation>（Ⅱ）由题设和第（Ⅰ）问得，<equation>| \lambda E - B | = \left| \begin{array}{c c c} \lambda - 1 & 2 & 0 \\ 0 & \lambda - 5 & 0 \\ 0 & - 3 & \lambda - 1 \end{array} \right| = (\lambda - 1) ^ {2} (\lambda - 5).</equation>从而<equation>B</equation>的特征值为1,1,5.由于<equation>A</equation>和<equation>B</equation>相似，故<equation>A</equation>的特征值也为1,1,5.

由第（I）问可得，<equation>A = \left( \begin{array}{c c c} 0 & 2 & -3 \\ -1 & 3 & -3 \\ 1 & -2 & 4 \end{array} \right).</equation>考虑<equation>A</equation>的属于特征值5的特征向量.<equation>\begin{array}{l} 5 E - A = \left( \begin{array}{c c c} 5 & - 2 & 3 \\ 1 & 2 & 3 \\ - 1 & 2 & 1 \end{array} \right) \xrightarrow [ r _ {2} ^ {*} \times \frac {1}{2} ]{r _ {2} - r _ {3}} \left( \begin{array}{c c c} 5 & - 2 & 3 \\ 1 & 0 & 1 \\ - 1 & 2 & 1 \end{array} \right) \xrightarrow [ r _ {3} ^ {*} \times \frac {1}{2} ]{r _ {3} + r _ {2} ^ {* *}} \left( \begin{array}{c c c} 5 & - 2 & 3 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} - 5 r _ {2} ^ {* *} + 2 r _ {3} ^ {* *}} \left( \begin{array}{c c c} 0 & 0 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right). \\ \end{array}</equation>于是，<equation>r ( 5 E - A ) = 2</equation>，求得<equation>\boldsymbol{\xi}_{1}=(-1,-1,1)^{\mathrm{T}}</equation>为<equation>( 5 E - A ) x = 0</equation>的一个基础解系<equation>(-1,-1,1)^{\mathrm{T}}</equation>为A的属于特征值5的一个特征向量.

考虑<equation>A</equation>的属于特征值1的特征向量.<equation>\boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} 1 & - 2 & 3 \\ 1 & - 2 & 3 \\ - 1 & 2 & - 3 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & - 2 & 3 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r ( E - A ) = 1</equation>，求得<equation>\boldsymbol{\xi}_{2} = ( 2,1,0 )^{\mathrm{T}}</equation>和<equation>\boldsymbol{\xi}_{3} = (-3,0,1)^{\mathrm{T}}</equation>为<equation>( E - A ) x = 0</equation>的一个基础解系<equation>( 2,1,0 )^{\mathrm{T}}</equation>和<equation>(-3,0,1)^{\mathrm{T}}</equation>为A的属于特征值1的两个线性无关的特征向量.

取<equation>P = \left( \begin{array}{c c c} - 1 & 2 & - 3 \\ - 1 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right)</equation>，则<equation>P^{-1}AP = \left( \begin{array}{c c c} 5 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>.

---

**2014年第21题 | 解答题 | 11分**

21. (本题满分11分)

证明 n阶矩阵

相似.

**答案:**(21) 证明略

**解析:**证（法一）记<equation>A=\left( \begin{array}{c c c c} 1 & 1 & \dots & 1 \\ 1 & 1 & \dots & 1 \\ \vdots & \vdots & & \vdots \\ 1 & 1 & \dots & 1 \end{array} \right), B=\left( \begin{array}{c c c c} 0 & \dots & 0 & 1 \\ 0 & \dots & 0 & 2 \\ \vdots & & \vdots & \vdots \\ 0 & \dots & 0 & n \end{array} \right).</equation>由观察可知，<equation>r ( \mathbf{A} )=1</equation>，<equation>\operatorname{t r} ( \mathbf{A} )=n</equation>. 又由于 A为实对称矩阵，故必相似于对角矩阵.由相似的矩阵具有相同的秩和迹可知，A相似于秩为1，迹为 n的对角矩阵，不妨记为<equation>\left( \begin{array}{c c c c} n & & & \\ & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right).</equation>另一方面，计算<equation>B</equation>的特征多项式得，<equation>| \lambda E - B | = \left| \begin{array}{c c c c} \lambda & 0 & \dots & - 1 \\ 0 & \lambda & & - 2 \\ \vdots & & \ddots & \vdots \\ 0 & \dots & 0 & \lambda - n \end{array} \right| = \lambda^ {n - 1} (\lambda - n).</equation>B的特征值为<equation>n,0,\dots ,0</equation>，其中0为<equation>n - 1</equation>重特征值.

由于<equation>0 E - B = \left( \begin{array}{c c c c} 0 & & & - 1 \\ & 0 & & - 2 \\ & & \ddots & \vdots \\ & & & - n \end{array} \right)</equation>，故<equation>r(0 E - B) = 1</equation>，从而<equation>(0 E - B) x = 0</equation>的解集的秩为<equation>n - 1</equation><equation>(0 E - B) x = 0</equation>有 n-1个线性无关的解.

B有 n-1个属于特征值0的线性无关的特征向量，再加上B的属于n的特征向量，B共有n个线性无关的特征向量.从而B也相似于<equation>\left( \begin{array}{c c c c} n & & & \\ & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right).</equation>因此，存在可逆矩阵 P，Q，使得<equation>P^{-1} A P=Q^{-1} B Q=\left( \begin{array}{c c c c} n & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right).</equation>于是<equation>Q P^{-1} A P Q^{-1}=B.</equation>令<equation>U=P Q^{-1}</equation>，则<equation>B=U^{-1} A U,A</equation>和B相似.

（法二）计算 A的特征多项式.<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c c} \lambda - 1 & - 1 & \dots & - 1 \\ - 1 & \lambda - 1 & \dots & - 1 \\ \vdots & \vdots & & \vdots \\ - 1 & - 1 & \dots & \lambda - 1  \right| \frac {c _ {1} + \left(c _ {2} + c _ {3} + \dots + c _ {n}\right)}{\overline {{}}} \left| \begin{array}{c c c c} \lambda - n & - 1 & \dots & - 1 \\ \lambda - n & \lambda - 1 & \dots & - 1 \\ \vdots & \vdots & & \vdots \\ \lambda - n & - 1 & \dots & \lambda - 1  \right| \\ &= (\lambda - n) \left| \begin{array}{c c c c} 1 & - 1 & \dots & - 1 \\ 1 & \lambda - 1 & \dots & - 1 \\ \vdots & \vdots & & \vdots \\ 1 & - 1 & \dots & \lambda - 1  \right| \frac {c _ {i} + c _ {1}}{i = 2 , \dots , n} (\lambda - n) \left| \begin{array}{c c c c} 1 & 0 & \dots & 0 \\ 1 & \lambda & \dots & 0 \\ \vdots & \vdots & & \vdots \\ 1 & 0 & \dots & \lambda  \right| \\ &= \lambda^ {n - 1} (\lambda - n). \end{aligned}</equation>由于 A为实对称矩阵，故由 A的特征多项式为<equation>\lambda^{n-1} (\lambda-n)</equation>可知 A相似于对角矩阵<equation>\left( \begin{array}{c c c c} n & & & \\ & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right).</equation>其余同法一.

---

**2013年第6题 | 选择题 | 4分 | 答案: B**

6. 矩阵

相似的充分必要条件为（    ）

A. a=0,b=2 B. a=0,b为任意常数 C. a=2,b=0 D. a=2,b为任意常数

答案: B

**解析:**解 矩阵<equation>\left( \begin{array}{c c c}1&a&1\\ a&b&a\\ 1&a&1 \end{array} \right)</equation>与<equation>\left( \begin{array}{c c c}2&0&0\\ 0&b&0\\ 0&0&0 \end{array} \right)</equation>均为实对称矩阵，故它们相似等价于它们有相同的特征多项式.

矩阵<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>的特征多项式为<equation>f (\lambda) = \lambda (\lambda - 2) (\lambda - b).</equation>考虑<equation>A = \left( \begin{array}{c c c} 1 & a & 1 \\ a & b & a \\ 1 & a & 1 \end{array} \right)</equation>的特征多项式<equation>g(\lambda)</equation>.<equation>g (\lambda) = | \lambda E - A | = \left| \begin{array}{c c c} \lambda - 1 & - a & - 1 \\ - a & \lambda - b & - a \\ - 1 & - a & \lambda - 1 \end{array} \right| = \lambda \left[ (\lambda - 2) (\lambda - b) - 2 a ^ {2} \right].</equation>由于<equation>f(\lambda)-g(\lambda)=2 a^{2}\lambda</equation>，故<equation>f(\lambda)=g(\lambda)</equation>当且仅当 a=0.由于上述论证不涉及到b，故b取任意常数均不影响结果.应选B.

---

**2010年第6题 | 选择题 | 4分 | 答案: D**

6. 设 A为4阶实对称矩阵，且<equation>A^{2}+A=O</equation>. 若 A的秩为3，则 A相似于（    ）

A.<equation>\left( \begin{array}{c c c c} 1 & & \\ & 1 & \\ & & 1 \\ & & 0 \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c c} 1 & & \\ & 1 & \\ & & - 1 \\ & & 0 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c c} 1 & & \\ & - 1 & \\ & & - 1 \\ & & 0 \end{array} \right).</equation>D.<equation>\left( \begin{array}{c c c c} - 1 & & \\ & - 1 & \\ & & - 1 \\ & & 0 \end{array} \right)</equation>

答案: D

**解析:**解（法一）不妨设<equation>\lambda</equation>为 A的特征值，<equation>\alpha</equation>为其相应的特征向量.由<equation>A^{2}+A=O</equation>得<equation>(A^{2}+A)\alpha=0.</equation>代入<equation>A\alpha=\lambda\alpha</equation>得，<equation>(\lambda^{2}+\lambda)\alpha=0.</equation>又由于<equation>\alpha</equation>非零，故<equation>\lambda^{2}+\lambda=0,\lambda=0</equation>或<equation>\lambda=-1.</equation>由于<equation>A</equation>为实对称矩阵，故<equation>A</equation>相似于对角矩阵.又因为<equation>r(A) = 3</equation>，所以对角矩阵的秩也为3，<equation>\lambda = -1</equation>是<equation>A</equation>的三重特征值，<equation>A</equation>相似于<equation>\left( \begin{array}{c c c c} - 1 & & & \\ & - 1 & & \\ & & - 1 & \\ & & & 0 \end{array} \right)</equation>.应选D.

（法二）由于 A为实对称矩阵，故存在可逆矩阵 P使得<equation>P^{-1} A P=\left( \begin{array}{c c c c} \lambda_{1} & & & \\ & \lambda_{2} & & \\ & & \lambda_{3} & \\ & & & \lambda_{4} \end{array} \right)</equation>从而<equation>\begin{aligned} \boldsymbol {O} &= \boldsymbol {A} ^ {2} + \boldsymbol {A} = \boldsymbol {P} \left( \begin{array}{c c c c} \lambda_ {1} ^ {2} & & & \\ & \lambda_ {2} ^ {2} & & \\ & & \lambda_ {3} ^ {2} & \\ & & & \lambda_ {4} ^ {2}  \right) \boldsymbol {P} ^ {- 1} + \boldsymbol {P} \left( \begin{array}{c c c c} \lambda_ {1} & & & \\ & \lambda_ {2} & & \\ & & \lambda_ {3} & \\ & & & \lambda_ {4}  \right) \boldsymbol {P} ^ {- 1} \\ &= \boldsymbol {P} \left( \begin{array}{c c c c} \lambda_ {1} ^ {2} + \lambda_ {1} & & & \\ & \lambda_ {2} ^ {2} + \lambda_ {2} & & \\ & & \lambda_ {3} ^ {2} + \lambda_ {3} & \\ & & & \lambda_ {4} ^ {2} + \lambda_ {4}  \right) \boldsymbol {P} ^ {- 1}. \end{aligned}</equation>因此<equation>\lambda_{i}^{2}+\lambda_{i}=0 ( i=1,2,3,4).</equation>解得<equation>\lambda_{i}=0</equation>或<equation>\lambda_{i}=-1 ( i=1,2,3,4).</equation>又由于<equation>r ( A )=3</equation>故 A相似于<equation>\left( \begin{array}{c c c c} - 1 & & & \\ & - 1 & & \\ & & - 1 & \\ & & & 0 \end{array} \right).</equation>应选D.

---


### 向量


#### 向量组的线性相关性

**2024年第6题 | 选择题 | 5分 | 答案: D**
6. 设向量<equation>\alpha_{1}=\left( \begin{array}{c} a \\ 1 \\ -1 \\ 1 \end{array} \right),\alpha_{2}=\left( \begin{array}{c} 1 \\ 1 \\ b \\ a \end{array} \right),\alpha_{3}=\left( \begin{array}{c} 1 \\ a \\ -1 \\ 1 \end{array} \right)</equation>若<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性相关，且其中任意两个向量均线性无关，则（    ）

A. a=1,b≠-1 B. a=1,b=-1 C. a≠-2,b=2 D. a=-2,b=2
答案: D
**解析: **解（法一）由于<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性相关，故该向量组的秩小于3，从而<equation>r(\alpha_{1},\alpha_{2},\alpha_{3})\leqslant 2.</equation>又因为该向量组中任意两个向量均线性无关，所以该向量组的秩不小于2，从而<equation>r(\alpha_{1},\alpha_{2},\alpha_{3})\geqslant 2.</equation>于是，<equation>r(\alpha_{1},\alpha_{2},\alpha_{3})=2.</equation>由<equation>r(\alpha_{1},\alpha_{2},\alpha_{3}) = 2</equation>可得，矩阵<equation>(\alpha_{1},\alpha_{2},\alpha_{3})</equation>的任意一个3阶子式均为0.于是，<equation>\begin{aligned} \left| \begin{array}{l l l} a & 1 & 1 \\ 1 & 1 & a \\ 1 & a & 1  \right| \xlongequal {c _ {1} + c _ {2} + c _ {3}} \left| \begin{array}{l l l} a + 2 & 1 & 1 \\ a + 2 & 1 & a \\ a + 2 & a & 1  \right| &= (a + 2) \left| \begin{array}{l l l} 1 & 1 & 1 \\ 1 & 1 & a \\ 1 & a & 1  \right| &= (a + 2) \left| \begin{array}{l l l} 1 & 0 & 0 \\ 1 & 0 & a - 1 \\ 1 & a - 1 & 0  \right| \\ &= - (a + 2) \left(a - 1\right) ^ {2} = 0. \end{aligned}</equation>由此可得<equation>a = -2</equation>或<equation>a = 1</equation>. 但是当<equation>a = 1</equation>时，<equation>\alpha_{1} = \alpha_{3}</equation>，从而<equation>\alpha_{1},\alpha_{3}</equation>线性相关，不符合题意.于是，<equation>a = -2</equation>代入<equation>a=-2</equation>，再由矩阵（<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>）的任意一个3阶子式均为0可得<equation>\left| \begin{array}{c c c} 1 & 1 & - 2 \\ - 1 & b & - 1 \\ 1 & - 2 & 1 \end{array} \right| \frac {c _ {2} - c _ {1}}{c _ {3} + 2 c _ {1}} \left| \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & b + 1 & - 3 \\ 1 & - 3 & 3 \end{array} \right| = 3 (b + 1) - 9 = 0.</equation>解得 b=2.

因此，<equation>a=-2,b=2</equation>，应选D.

（法二）同法一可得<equation>r(\alpha_{1},\alpha_{2},\alpha_{3}) = 2.</equation>对矩阵<equation>(\alpha_{1},\alpha_{2},\alpha_{3})</equation>作初等行变换<equation>\begin{array}{l} \left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) = \left( \begin{array}{c c c} a & 1 & 1 \\ 1 & 1 & a \\ - 1 & b & - 1 \\ 1 & a & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & a \\ 1 & a & 1 \\ - 1 & b & - 1 \\ a & 1 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & a \\ 0 & a - 1 & 1 - a \\ 0 & b + 1 & a - 1 \\ 0 & 1 - a & 1 - a ^ {2} \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c} 1 & 1 & a \\ 0 & a - 1 & 1 - a \\ 0 & b + 1 & a - 1 \\ 0 & 0 & 2 - a - a ^ {2} \end{array} \right). \\ \end{array}</equation>当<equation>a = -2</equation>或<equation>a = 1</equation>时，<equation>2 - a - a^{2} = -(a + 2)(a - 1) = 0.</equation>当<equation>a = 1</equation>时，<equation>(\alpha_{1},\alpha_{2},\alpha_{3})\rightarrow \left( \begin{array}{c c c}1&1&1\\ 0&0&0\\ 0&b + 1&0\\ 0&0&0 \end{array} \right)\rightarrow \left( \begin{array}{c c c}1&1&1\\ 0&b + 1&0\\ 0&0&0\\ 0&0&0 \end{array} \right)</equation>.由此可得<equation>\alpha_{1},\alpha_{3}</equation>线性相关，不符合题意.

当 a = -2时，<equation>\left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right)\rightarrow \left(\begin{array}{c c c}1&1&- 2\\0&- 3&3\\0&b + 1&- 3\\0&0&0\end{array}\right)\rightarrow \left(\begin{array}{c c c}1&1&- 2\\0&1&- 1\\0&b - 2&0\\0&0&0\end{array}\right).</equation>由<equation>r(\alpha_{1},\alpha_{2},\alpha_{3}) = 2</equation>可得<equation>b - 2 = 0</equation>，即<equation>b = 2.</equation>因此，<equation>a=-2,b=2</equation>，应选D.

---

**2014年第6题 | 选择题 | 4分 | 答案: A**
6. 设<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>均为3维向量，则对任意常数 k,l，向量组<equation>\alpha_{1}+k\alpha_{3},\alpha_{2}+l\alpha_{3}</equation>线性无关是向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关的（    ）

A. 必要非充分条件 B. 充分非必要条件

C. 充分必要条件 D. 既非充分也非必要条件
答案: A
**解析: **解<equation>\left( \boldsymbol{\alpha}_{1}+k\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{2}+l\boldsymbol{\alpha}_{3}\right)=\left( \boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}\right)\left( \begin{array}{ll}1&0\\ 0&1\\ k&l \end{array} \right).</equation>若向量组<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性无关，则<equation>r \left(\boldsymbol {\alpha} _ {1} + k \boldsymbol {\alpha} _ {3}, \boldsymbol {\alpha} _ {2} + l \boldsymbol {\alpha} _ {3}\right) = r \left(\left( \begin{array}{c c} 1 & 0 \\ 0 & 1 \\ k & l \end{array} \right)\right) = 2.</equation>因此，<equation>\alpha_{1} + k\alpha_{3},\alpha_{2} + l\alpha_{3}</equation>线性无关.

令<equation>\alpha_{1},\alpha_{2}</equation>为线性无关的两个向量，<equation>\alpha_{3} = 0</equation>，则对任意常数<equation>k,l</equation>，向量组<equation>\alpha_{1} + k\alpha_{3},\alpha_{2} + l\alpha_{3}</equation>线性无关，但向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性相关.

综上所述，对任意常数 k，l，向量组<equation>\boldsymbol{\alpha}_{1}+k\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{2}+l\boldsymbol{\alpha}_{3}</equation>线性无关是向量组<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性无关的必要非充分条件.应选A.

---

**2012年第5题 | 选择题 | 4分 | 答案: C**
5. 设<equation>\alpha_{1}=\left( \begin{array}{c}0\\ 0\\ c_{1}\end{array} \right),\alpha_{2}=\left( \begin{array}{c}0\\ 1\\ c_{2}\end{array} \right),\alpha_{3}=\left( \begin{array}{c}1\\ -1\\ c_{3}\end{array} \right),\alpha_{4}=\left( \begin{array}{c}-1\\ 1\\ c_{4}\end{array} \right)</equation>其中<equation>c_{1},c_{2},c_{3},c_{4}</equation>为任意常数，则下列向量组线性相关的为（    ）

A.<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>B.<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>C.<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>D.<equation>\alpha_{2},\alpha_{3},\alpha_{4}</equation>
答案: C
**解析: **解（法一）由题设可得，<equation>\alpha_{3} + \alpha_{4} = \left( \begin{array}{c} 0 \\ 0 \\ c_{3} + c_{4} \end{array} \right),\alpha_{1} = \left( \begin{array}{c} 0 \\ 0 \\ c_{1} \end{array} \right).</equation>当<equation>c_{3} + c_{4}\neq 0</equation>时，<equation>\alpha_{1} = \frac{c_{1}}{c_{3} + c_{4}} \left(\alpha_{3} + \alpha_{4}\right)</equation>，<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>线性相关；当<equation>c_{3} + c_{4} = 0</equation>时，<equation>\alpha_{3} + \alpha_{4} = 0</equation>，<equation>\alpha_{3},\alpha_{4}</equation>线性相关.从而<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>线性相关.

综上所述，<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}</equation>线性相关，应选C.

（法二）由于<equation>n</equation>个<equation>n</equation>维列向量<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{n}</equation>线性相关等价于<equation>|\alpha_{1},\alpha_{2},\dots ,\alpha_{n}| = 0</equation>，而<equation>\left| \alpha_ {1}, \alpha_ {3}, \alpha_ {4} \right| = \left| \begin{array}{c c c} 0 & 1 & - 1 \\ 0 & - 1 & 1 \\ c _ {1} & c _ {3} & c _ {4} \end{array} \right| = c _ {1} \left| \begin{array}{c c} 1 & - 1 \\ - 1 & 1 \end{array} \right| = 0,</equation>故<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}</equation>线性相关.应选C.

同理可计算其他选项中的3个向量组成的矩阵的行列式，可知它们均不恒为零.

---

**2009年第20题 | 解答题 | 11分**
20. (本题满分11分)<equation>\text {设} \boldsymbol {A} = \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ - 1 & 1 & 1 \\ 0 & - 4 & - 2 \end{array} \right), \boldsymbol {\xi} _ {1} = \left( \begin{array}{c} - 1 \\ 1 \\ - 2 \end{array} \right).</equation>I. 求满足<equation>A\xi_{2}=\xi_{1}, A^{2}\xi_{3}=\xi_{1}</equation>的所有向量<equation>\xi_{2},\xi_{3}</equation>；

II. 对（I）中的任意向量<equation>\xi_{2},\xi_{3}</equation>，证明<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.
**答案: **（20）（I）满足<equation>A\xi_{2}=\xi_{1}</equation>的所有向量为<equation>\xi_{2}=k_{1}(1,-1,2)^{\mathrm{T}}+(0,0,1)^{\mathrm{T}}</equation>，其中<equation>k_{1}</equation>为任意常数满足<equation>A^{2}\xi_{3}=\xi_{1}</equation>的所有向量为<equation>\xi_{3}=k_{2}(1,-1,0)^{\mathrm{T}}+k_{3}(0,0,1)^{\mathrm{T}}+\left(-\frac{1}{2},0,0\right)^{\mathrm{T}}</equation>，其中<equation>k_{2},k_{3}</equation>为任意常数.

（Ⅱ）证明略.
**解析: **解（ I ）解<equation>A x=\xi_{1}</equation>，这是一个非齐次线性方程组.<equation>\left(\boldsymbol {A}, \boldsymbol {\xi} _ {1}\right) = \left( \begin{array}{c c c c} 1 & - 1 & - 1 & - 1 \\ - 1 & 1 & 1 & 1 \\ 0 & - 4 & - 2 & - 2 \end{array} \right) \xrightarrow [ r _ {2} ^ {*} \leftrightarrow r _ {3} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c} 1 & - 1 & - 1 & - 1 \\ 0 & - 4 & - 2 & - 2 \\ 0 & 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {1} + r _ {2} ^ {* * *} ]{r _ {2} ^ {* *} \times \left(- \frac {1}{2}\right)} \left( \begin{array}{c c c c} 1 & 1 & 0 & 0 \\ 0 & 2 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{array} \right).</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每做一次初等行变换，加一个 *.）

于是<equation>r(A) = r(A, \xi_1) = 2.Ax = \xi_1</equation>有无穷多解.其对应的齐次方程组等价于<equation>\left\{ \begin{array}{l} x_{1} + x_{2} = 0, \\ 2x_{2} + x_{3} = 0, \end{array} \right.</equation>故可取<equation>(1, -1, 2)^{\mathrm{T}}</equation>为它的一个基础解系.另外，<equation>\left\{ \begin{array}{l} x_{1} + x_{2} = 0, \\ 2x_{2} + x_{3} = 1 \end{array} \right.</equation>的一个特解为<equation>(0,0,1)^{\mathrm{T}}.</equation>因此，<equation>Ax = \xi_{1}</equation>的通解为<equation>\xi_{2} = k_{1}(1, -1, 2)^{\mathrm{T}} + (0, 0, 1)^{\mathrm{T}}</equation>，其中<equation>k_{1}</equation>为任意常数.<equation>\left(\boldsymbol {A} ^ {2}, \boldsymbol {\xi} _ {1}\right) = \left( \begin{array}{c c c c} 2 & 2 & 0 & - 1 \\ - 2 & - 2 & 0 & 1 \\ 4 & 4 & 0 & - 2 \end{array} \right) \xrightarrow [ r _ {3} - 2 r _ {1} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c} 2 & 2 & 0 & - 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{array} \right).</equation>于是<equation>r(A^{2}) = r(A^{2},\xi_{1}) = 1.A^{2}x = \xi_{1}</equation>有无穷多解.其对应的齐次方程组等价于<equation>2(x_{1} + x_{2}) = 0</equation>，故可取<equation>(1, - 1,0)^{\mathrm{T}}</equation>和<equation>(0,0,1)^{\mathrm{T}}</equation>为它的一个基础解系.另外，<equation>2(x_{1} + x_{2}) = -1</equation>的一个特解为<equation>\left(-\frac{1}{2},0,0\right)^{\mathrm{T}}.</equation>因此，<equation>A^{2}x = \xi_{1}</equation>的通解为<equation>\xi_{3} = k_{2}(1, -1, 0)^{\mathrm{T}} + k_{3}(0, 0, 1)^{\mathrm{T}} + \left(-\frac{1}{2}, 0, 0\right)^{\mathrm{T}}</equation>，其中<equation>k_{2}, k_{3}</equation>为任意常数.

（Ⅱ）（法一）通过计算可知，<equation>\boldsymbol {A} \boldsymbol {\xi} _ {1} = \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ - 1 & 1 & 1 \\ 0 & - 4 & - 2 \end{array} \right) \left( \begin{array}{c} - 1 \\ 1 \\ - 2 \end{array} \right) = \left( \begin{array}{c} 0 \\ 0 \\ 0 \end{array} \right).</equation>从而<equation>A^{3}\xi_{3} = A^{2}\xi_{2} = A\xi_{1} = 0.</equation>我们可以利用该性质推出<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

不妨设<equation>a\boldsymbol{\xi}_1 + b\boldsymbol{\xi}_2 + c\boldsymbol{\xi}_3 = \mathbf{0}</equation>. 该等式两端同时左乘<equation>A^2</equation>，得<equation>a A ^ {2} \xi_ {1} + b A ^ {2} \xi_ {2} + c A ^ {2} \xi_ {3} = c A ^ {2} \xi_ {3} = c \xi_ {1} = 0.</equation>由于<equation>\boldsymbol{\xi}_1</equation>为非零向量，故<equation>c = 0</equation>. 于是<equation>a\boldsymbol{\xi}_1 + b\boldsymbol{\xi}_2 = \mathbf{0}</equation>. 再在<equation>a\boldsymbol{\xi}_1 + b\boldsymbol{\xi}_2 = \mathbf{0}</equation>两端同时左乘<equation>A</equation>，得<equation>a A \xi_ {1} + b A \xi_ {2} = b A \xi_ {2} = b \xi_ {1} = 0.</equation>同理得<equation>b = 0</equation>. 由于<equation>b = c = 0</equation>, 故<equation>a\xi_{1} = 0</equation>. 从而<equation>a = 0</equation>.

因此，<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

（法二）由第（I）问，我们得到<equation>\xi_{1},\xi_{2},\xi_{3}</equation>的表达式，从而可以通过计算<equation>|\xi_{1},\xi_{2},\xi_{3}|</equation>来说明<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.<equation>\begin{aligned} \left| \xi_ {1}, \xi_ {2}, \xi_ {3} \right| &= \left| \begin{array}{c c c} - 1 & k _ {1} & k _ {2} - \frac {1}{2} \\ 1 & - k _ {1} & - k _ {2} \\ - 2 & 2 k _ {1} + 1. & k _ {3}  \right| \frac {c _ {2} + k _ {1} c _ {1}}{c _ {3} + k _ {2} c _ {1}} \left| \begin{array}{c c c} - 1 & 0 & - \frac {1}{2} \\ 1 & 0 & 0 \\ - 2 & 1 & k _ {3} - 2 k _ {2}  \right| \\ \underline {{\text {按 第二 行 展 开}}} (- 1) \left| \begin{array}{c c} 0 & - \frac {1}{2} \\ 1 & k _ {3} - 2 k _ {2}  \right| &= - \frac {1}{2} \neq 0. \end{aligned}</equation>因此，<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

---


#### 向量组之间的线性表示

**2023年第7题 | 选择题 | 5分 | 答案: D**

7. 已知向量<equation>\alpha_{1}=\left( \begin{array}{c}1\\ 2\\ 3 \end{array} \right),\alpha_{2}=\left( \begin{array}{c}2\\ 1\\ 1 \end{array} \right),\beta_{1}=\left( \begin{array}{c}2\\ 5\\ 9 \end{array} \right),\beta_{2}=\left( \begin{array}{c}1\\ 0\\ 1 \end{array} \right),</equation>若<equation>\gamma</equation>既可由<equation>\alpha_{1},\alpha_{2}</equation>线性表示，也可由<equation>\beta_{1},\beta_{2}</equation>线性表示，则<equation>\gamma=</equation>（    ）

A.<equation>k\left( \begin{array}{c}3\\ 3\\ 4 \end{array} \right),k \in \mathbf{R}</equation>B.<equation>k\left( \begin{array}{c}3\\ 5\\ 10 \end{array} \right),k \in \mathbf{R}</equation>C.<equation>k\left( \begin{array}{c}-1\\ 1\\ 2 \end{array} \right),k \in \mathbf{R}</equation>D.<equation>k\left( \begin{array}{c}1\\ 5\\ 8 \end{array} \right),k \in \mathbf{R}</equation>

答案: D

**解析:**解（法一）由于<equation>\boldsymbol{\gamma}</equation>既可由<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2}</equation>线性表示，也可由<equation>\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2}</equation>线性表示，故存在<equation>k_{1},k_{2},l_{1},l_{2}</equation>，使得<equation>\boldsymbol{\gamma}=k_{1}\boldsymbol{\alpha}_{1}+k_{2}\boldsymbol{\alpha}_{2}=l_{1}\boldsymbol{\beta}_{1}+l_{2}\boldsymbol{\beta}_{2}</equation>.于是，<equation>\left(k_{1},-l_{1},k_{2},-l_{2}\right)^{\mathrm{T}}</equation>是齐次线性方程组<equation>\left(\boldsymbol{\alpha}_{1},\boldsymbol{\beta}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\beta}_{2}\right)\boldsymbol{x}=\mathbf{0}</equation>的解.

记<equation>A = \left(\alpha_{1},\beta_{1},\alpha_{2},\beta_{2}\right)</equation>，对A作初等行变换.<equation>\begin{array}{l} \boldsymbol {A} = \left( \begin{array}{c c c c} 1 & 2 & 2 & 1 \\ 2 & 5 & 1 & 0 \\ 3 & 9 & 1 & 1 \end{array} \right) \xrightarrow {r _ {2} - 2 r _ {1}} \frac {r _ {2} - 2 r _ {1}}{r _ {3} - 3 r _ {1}} \left( \begin{array}{c c c c} 1 & 2 & 2 & 1 \\ 0 & 1 & - 3 & - 2 \\ 0 & 3 & - 5 & - 2 \end{array} \right) \xrightarrow {r _ {1} - 2 r _ {2} ^ {*}} \left( \begin{array}{c c c c} 1 & 0 & 8 & 5 \\ 0 & 1 & - 3 & - 2 \\ 0 & 0 & 4 & 4 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {* *} \times \frac {1}{4}} \left( \begin{array}{c c c c} 1 & 0 & 8 & 5 \\ 0 & 1 & - 3 & - 2 \\ 0 & 0 & 1 & 1 \end{array} \right) \xrightarrow {r _ {1} ^ {*} - 8 r _ {3} ^ {* * *}} \left( \begin{array}{c c c c} 1 & 0 & 0 & - 3 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 \end{array} \right). \\ \end{array}</equation>（<equation>r_{t}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每作一次初等行变换，加一个<equation>*.</equation>）

取<equation>x_{4}=1</equation>，可得<equation>\boldsymbol{\xi}=(3,-1,-1,1)^{\mathrm{T}}</equation>为该方程组的一个基础解系，从而<equation>(k_{1},-l_{1},k_{2},-l_{2})^{\mathrm{T}}= k(3,-1,-1,1)^{\mathrm{T}}</equation>，其中<equation>k\in\mathbf{R}.</equation>因此，<equation>\boldsymbol {\gamma} = k _ {1} \boldsymbol {\alpha} _ {1} + k _ {2} \boldsymbol {\alpha} _ {2} = 3 k \binom {1} {2} - k \binom {2} {1} = k \binom {1} {5}, \quad k \in \mathbf {R}.</equation>应选 D.

（法二）由<equation>\alpha_{1},\alpha_{2}</equation>可以生成一个平面<equation>S_{1}</equation>，由<equation>\beta_{1},\beta_{2}</equation>可以生成一个平面<equation>S_{2}</equation>，而<equation>\gamma</equation>既可由<equation>\alpha_{1},\alpha_{2}</equation>线性表示，也可由<equation>\beta_{1},\beta_{2}</equation>线性表示，这说明<equation>\gamma</equation>既在平面<equation>S_{1}</equation>上，又在平面<equation>S_{2}</equation>上。于是，<equation>\gamma</equation>既垂直于平面<equation>S_{1}</equation>的法向量<equation>n_{1}</equation>，又垂直于平面<equation>S_{2}</equation>的法向量<equation>n_{2}</equation>，从而垂直于<equation>n_{1},n_{2}</equation>生成的平面。因此<equation>\gamma</equation>与<equation>n_{1} \times n_{2}</equation>共线.

取<equation>n_{1} = \alpha_{1}\times \alpha_{2},n_{2} = \beta_{1}\times \beta_{2}</equation><equation>\boldsymbol {n} _ {1} = \boldsymbol {\alpha} _ {1} \times \boldsymbol {\alpha} _ {2} = \left| \begin{array}{c c c} \boldsymbol {i} & \boldsymbol {j} & \boldsymbol {k} \\ 1 & 2 & 3 \\ 2 & 1 & 1 \end{array} \right| = - \boldsymbol {i} + 5 \boldsymbol {j} - 3 \boldsymbol {k},</equation><equation>\boldsymbol {n} _ {2} = \boldsymbol {\beta} _ {1} \times \boldsymbol {\beta} _ {2} = \left| \begin{array}{c c c} \boldsymbol {i} & \boldsymbol {j} & \boldsymbol {k} \\ 2 & 5 & 9 \\ 1 & 0 & 1 \end{array} \right| = 5 \boldsymbol {i} + 7 \boldsymbol {j} - 5 \boldsymbol {k}.</equation><equation>\boldsymbol {n} _ {1} \times \boldsymbol {n} _ {2} = \left| \begin{array}{c c c} \boldsymbol {i} & \boldsymbol {j} & \boldsymbol {k} \\ - 1 & 5 & - 3 \\ 5 & 7 & - 5 \end{array} \right| = - 4 \boldsymbol {i} - 2 0 \boldsymbol {j} - 3 2 \boldsymbol {k}.</equation>因此，<equation>\gamma</equation>与<equation>\left( \begin{array}{c} - 4 \\ - 20 \\ - 32 \end{array} \right)</equation>共线，即<equation>\gamma = k \left( \begin{array}{c} 1 \\ 5 \\ 8 \end{array} \right)</equation>，其中<equation>k \in \mathbf{R}</equation>.

---

**2022年第7题 | 选择题 | 5分 | 答案: C**

7. 设<equation>\alpha_{1}=(\lambda,1,1)^{\mathrm{T}},\alpha_{2}=(1,\lambda,1)^{\mathrm{T}},\alpha_{3}=(1,1,\lambda)^{\mathrm{T}},\alpha_{4}=\left(1,\lambda,\lambda^{2}\right)^{\mathrm{T}}</equation>，若向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>等价，则<equation>\lambda</equation>的取值范围是（    ）

A.<equation>\{0,1\}</equation>B.<equation>\{\lambda \mid \lambda \in \mathbf{R},\lambda \neq -2\}</equation>C.<equation>\{\lambda \mid \lambda \in \mathbf{R},\lambda \neq -1,\lambda \neq -2\}</equation>D.<equation>\{\lambda \mid \lambda \in \mathbf{R},\lambda \neq -1\}</equation>

答案: C

**解析:**解（法一）当<equation>\lambda=1</equation>时，<equation>\alpha_{1}=\alpha_{2}=\alpha_{3}=\alpha_{4}=\left( \begin{array}{c}1\\ 1\\ 1 \end{array} \right).</equation>此时<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>显然等价当<equation>\lambda\neq1</equation>时，考虑矩阵<equation>A=(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4}).</equation><equation>\begin{array}{l} \boldsymbol {A} = \left( \begin{array}{c c c c} \lambda & 1 & 1 & 1 \\ 1 & \lambda & 1 & \lambda \\ 1 & 1 & \lambda & \lambda^ {2} \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 1 & 1 & \lambda & \lambda^ {2} \\ \lambda & 1 & 1 & 1 \end{array} \right) \xrightarrow {r _ {2} - r _ {1}} \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 0 & 1 - \lambda & \lambda - 1 & \lambda^ {2} - \lambda \\ 0 & 1 - \lambda^ {2} & 1 - \lambda & 1 - \lambda^ {2} \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} \times \frac {1}{1 - \lambda}} \frac {r _ {3} ^ {*} \times \frac {1}{1 - \lambda}}{r _ {3} ^ {*} \times \frac {1}{1 - \lambda}} \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 0 & 1 & - 1 & - \lambda \\ 0 & 1 + \lambda & 1 & 1 + \lambda \end{array} \right) \xrightarrow {r _ {3} ^ {* *} - (1 + \lambda) r _ {2} ^ {* *}} \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 0 & 1 & - 1 & - \lambda \\ 0 & 0 & \lambda + 2 & (\lambda + 1) ^ {2} \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每作一次初等行变换，加一个*.）

由于 A有2阶非零子式<equation>\left| \begin{array}{cc}\lambda & 1\\ 1 & \lambda \end{array} \right|</equation>，故<equation>r(A)\geqslant 2</equation>另一方面，因为不存在<equation>\lambda</equation>满足<equation>\lambda +2=(\lambda+1)^{2}=0</equation>所以<equation>r(A)=3.</equation><equation>r(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}) = 3</equation>当且仅当<equation>\lambda \neq -2.</equation><equation>r(\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{4}) = 3</equation>当且仅当<equation>\lambda \neq -1.</equation>因此，当<equation>\lambda \neq 1</equation>时，<equation>r(A) = r(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4}) = r(\alpha_{1},\alpha_{2},\alpha_{3}) = r(\alpha_{1},\alpha_{2},\alpha_{4})</equation>当且仅当<equation>\lambda \neq -2</equation>且<equation>\lambda \neq -1</equation>注意到<equation>\lambda=1</equation>也包含在条件<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1</equation>中，故<equation>r(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4})=r(\alpha_{1},\alpha_{2},\alpha_{3})= r(\alpha_{1},\alpha_{2},\alpha_{4})</equation>当且仅当<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1.</equation>综上所述，应选C.

（法二）分别计算<equation>|\alpha_{1},\alpha_{2},\alpha_{3}|</equation>，<equation>|\alpha_{1},\alpha_{2},\alpha_{4}|</equation><equation>\left| \alpha_ {1}, \alpha_ {2}, \alpha_ {3} \right| = \left| \begin{array}{c c c} \lambda & 1 & 1 \\ 1 & \lambda & 1 \\ 1 & 1 & \lambda \end{array} \right| = \left| \begin{array}{c c c} \lambda & 1 - \lambda & 1 - \lambda^ {2} \\ 1 & \lambda - 1 & 1 - \lambda \\ 1 & 0 & 0 \end{array} \right| = (1 - \lambda) ^ {2} (\lambda + 2).</equation><equation>\left| \alpha_ {1}, \alpha_ {2}, \alpha_ {4} \right| = \left| \begin{array}{c c c} \lambda & 1 & 1 \\ 1 & \lambda & \lambda \\ 1 & 1 & \lambda^ {2} \end{array} \right| = \left| \begin{array}{c c c} \lambda & 1 - \lambda & 1 - \lambda^ {3} \\ 1 & \lambda - 1 & \lambda - \lambda^ {2} \\ 1 & 0 & 0 \end{array} \right| = (1 - \lambda) ^ {2} (1 + \lambda) ^ {2}.</equation>当<equation>\lambda\neq1</equation>，-2，-1时，<equation>|\alpha_{1},\alpha_{2},\alpha_{3}|</equation>与<equation>|\alpha_{1},\alpha_{2},\alpha_{4}|</equation>均不为0.此时，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>和<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>均为3维列向量组的极大无关组，从而等价.

当<equation>\lambda = 1</equation>时，<equation>\alpha_{1} = \alpha_{2} = \alpha_{3} = \alpha_{4} = \left( \begin{array}{c} 1 \\ 1 \\ 1 \end{array} \right)</equation>.此时<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>显然等价.

当<equation>\lambda = -2</equation>或<equation>\lambda = -1</equation>时，<equation>|\alpha_{1},\alpha_{2},\alpha_{3}| \neq |\alpha_{1},\alpha_{2},\alpha_{4}|</equation>，且其中一个为0，另一个不为0，说明两向量组的秩不相等，从而不等价.

综上所述，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>等价当且仅当<equation>\lambda \neq -2</equation>且<equation>\lambda \neq -1.</equation>应选C.

---

**2020年第6题 | 选择题 | 4分 | 答案: C**

6. 已知直线<equation>L_{1}:\frac{x-a_{2}}{a_{1}}=\frac{y-b_{2}}{b_{1}}=\frac{z-c_{2}}{c_{1}}</equation>与直线<equation>L_{2}:\frac{x-a_{3}}{a_{2}}=\frac{y-b_{3}}{b_{2}}=\frac{z-c_{3}}{c_{2}}</equation>相交于一点，记向量<equation>\alpha_{i}=\left( \begin{array}{c} a_{i} \\ b_{i} \\ c_{i} \end{array} \right), (i=</equation>1,2,3)，则（    ）

A.<equation>\alpha_{1}</equation>可由<equation>\alpha_{2},\alpha_{3}</equation>线性表示 B.<equation>\alpha_{2}</equation>可由<equation>\alpha_{1},\alpha_{3}</equation>线性表示

C.<equation>\alpha_{3}</equation>可由<equation>\alpha_{1},\alpha_{2}</equation>线性表示 D.<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关

答案: C

**解析:**解（法一）由<equation>l_{1}</equation>与<equation>l_{2}</equation>的方程可知，点（<equation>a_{2}, b_{2}, c_{2}</equation>）位于直线<equation>l_{1}</equation>上，点（<equation>a_{3}, b_{3}, c_{3}</equation>）位于直线<equation>l_{2}</equation>上，且<equation>\alpha_{1}</equation>为直线<equation>l_{1}</equation>的方向向量，<equation>\alpha_{2}</equation>为直线<equation>l_{2}</equation>的方向向量.

由于<equation>l_{1}</equation>与<equation>l_{2}</equation>相交于一点，故它们的方向向量<equation>\alpha_{1},\alpha_{2}</equation>不共线，从而<equation>\alpha_{1},\alpha_{2}</equation>线性无关.此外，<equation>l_{1}</equation>与<equation>l_{2}</equation>相交于一点说明它们共面.

记<equation>\boldsymbol{\beta}^{\mathrm{T}}=\left(a_{3}-a_{2},b_{3}-b_{2},c_{3}-c_{2}\right)</equation>，则直线<equation>l_{3}:\frac{x-a_{2}}{a_{3}-a_{2}}=\frac{y-b_{2}}{b_{3}-b_{2}}=\frac{z-c_{2}}{c_{3}-c_{2}}</equation>位于<equation>l_{1}</equation>与<equation>l_{2}</equation>所在平面，<equation>\boldsymbol{\beta}</equation>为<equation>l_{3}</equation>的方向向量.

由于三向量共面的充分必要条件是它们的混合积为零，故<equation>\left| \begin{array}{c c c} a_{1} & b_{1} & c_{1} \\ a_{2} & b_{2} & c_{2} \\ a_{3}-a_{2} & b_{3}-b_{2} & c_{3}-c_{2} \end{array} \right|=0.</equation>由行列式的性质可知<equation>\left| \begin{array}{c c c} a_{1} & b_{1} & c_{1} \\ a_{2} & b_{2} & c_{2} \\ a_{3} & b_{3} & c_{3} \end{array} \right|=0</equation>，从而<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性相关.

又因为<equation>\alpha_{1},\alpha_{2}</equation>线性无关，所以<equation>\alpha_{3}</equation>可由<equation>\alpha_{1},\alpha_{2}</equation>线性表示.应选C.

（法二）不妨认为<equation>a_{1}b_{1}c_{1}\neq 0,a_{2}b_{2}c_{2}\neq 0.a_{i},b_{i},c_{i}(i = 1,2)</equation>中存在0的情况不影响讨论.设<equation>l_{1}</equation>与<equation>l_{2}</equation>相交于点<equation>M(x_{0},y_{0},z_{0})</equation>，则点M的坐标既满足<equation>l_{1}</equation>的方程，又满足<equation>l_{2}</equation>的方程.于是，<equation>\frac {x _ {0} - a _ {2}}{a _ {1}} = \frac {y _ {0} - b _ {2}}{b _ {1}} = \frac {z _ {0} - c _ {2}}{c _ {1}} = k _ {1}, \quad \frac {x _ {0} - a _ {3}}{a _ {2}} = \frac {y _ {0} - b _ {3}}{b _ {2}} = \frac {z _ {0} - c _ {3}}{c _ {2}} = k _ {2}.</equation>由（1）式可得<equation>\begin{aligned} x _ {0} &= a _ {2} + k _ {1} a _ {1} = a _ {3} + k _ {2} a _ {2}, \\ y _ {0} &= b _ {2} + k _ {1} b _ {1} = b _ {3} + k _ {2} b _ {2}, \\ z _ {0} &= c _ {2} + k _ {1} c _ {1} = c _ {3} + k _ {2} c _ {2}. \end{aligned}</equation>整理可得<equation>\begin{aligned} a _ {3} &= k _ {1} a _ {1} + \left(1 - k _ {2}\right) a _ {2}, \\ b _ {3} &= k _ {1} b _ {1} + \left(1 - k _ {2}\right) b _ {2}, \\ c _ {3} &= k _ {1} c _ {1} + \left(1 - k _ {2}\right) c _ {2}, \end{aligned}</equation>即<equation>\boldsymbol{\alpha}_{3} = k_{1}\boldsymbol{\alpha}_{1} + (1 - k_{2})\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>可由<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2}</equation>线性表示. 应选C.

---

**2013年第5题 | 选择题 | 4分 | 答案: B**

5. 设 A,B,C均为 n阶矩阵，若 AB=C，且 B可逆，则（    ）

A. 矩阵 C的行向量组与矩阵 A的行向量组等价

B. 矩阵 C的列向量组与矩阵 A的列向量组等价

C. 矩阵 C的行向量组与矩阵 B的行向量组等价

D. 矩阵 C的列向量组与矩阵 B的列向量组等价

答案: B

**解析:**我们证明 C的列向量组与 A的列向量组能相互线性表示.

不妨设<equation>A = \left(\alpha_{1},\alpha_{2},\dots ,\alpha_{n}\right),C = \left(\gamma_{1},\gamma_{2},\dots ,\gamma_{n}\right),B = \left(b_{ij}\right)_{n\times n}</equation>，则<equation>\boldsymbol {A B} = \left(\alpha_ {1}, \alpha_ {2}, \dots , \alpha_ {n}\right) \left(b _ {i j}\right) _ {n \times n} = \boldsymbol {C} = \left(\gamma_ {1}, \gamma_ {2}, \dots , \gamma_ {n}\right),</equation><equation>\left\{ \begin{array}{l} \boldsymbol {\gamma} _ {1} = b _ {1 1} \boldsymbol {\alpha} _ {1} + b _ {2 1} \boldsymbol {\alpha} _ {2} + \dots + b _ {n 1} \boldsymbol {\alpha} _ {n}, \\ \boldsymbol {\gamma} _ {2} = b _ {1 2} \boldsymbol {\alpha} _ {1} + b _ {2 2} \boldsymbol {\alpha} _ {2} + \dots + b _ {n 2} \boldsymbol {\alpha} _ {n}, \\ \dots , \\ \boldsymbol {\gamma} _ {n} = b _ {1 n} \boldsymbol {\alpha} _ {1} + b _ {2 n} \boldsymbol {\alpha} _ {2} + \dots + b _ {n n} \boldsymbol {\alpha} _ {n}. \end{array} \right.</equation>因此，C的列向量组<equation>\left( \gamma_{1},\gamma_{2},\dots,\gamma_{n}\right)</equation>能由A的列向量组<equation>\left( \alpha_{1},\alpha_{2},\dots,\alpha_{n}\right)</equation>线性表示。同理，由于B可逆，故A的列向量组也能由C的列向量组线性表示.应选B.

下面我们说明选项 A、C、D不正确.

令<equation>A=\left( \begin{array}{cc}1&1\\ 0&0 \end{array} \right), B=\left( \begin{array}{cc}1&1\\ 0&1 \end{array} \right)</equation>，则<equation>C=A B=\left( \begin{array}{cc}1&2\\ 0&0 \end{array} \right).</equation>但A的行向量组<equation>\{(1,1),(0,0)\}</equation>与C的行向量组<equation>\{(1,2),(0,0)\}</equation>不等价.选项A不正确.

取 B为单位矩阵 E，C为一个非满秩矩阵. B的行（列）向量组线性无关，C的行（列）向量组线性相关. 选项C、D不正确.

---

**2011年第20题 | 解答题 | 11分**


设向量组<equation>\alpha_{1}=(1,0,1)^{\mathrm{T}},\alpha_{2}=(0,1,1)^{\mathrm{T}},\alpha_{3}=(1,3,5)^{\mathrm{T}}</equation>不能由向量组<equation>\beta_{1}=(1,1,1)^{\mathrm{T}},\beta_{2}=(1,2,3)^{\mathrm{T}},\beta_{3}=(3,4,a)^{\mathrm{T}}</equation>线性表示.

I. 求 a的值；

II. 将<equation>\beta_{1},\beta_{2},\beta_{3}</equation>用<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性表示.

**答案:**(20) ( I )<equation>a=5;</equation>( II )<equation>\boldsymbol{\beta}_{1}=2\boldsymbol{\alpha}_{1}+4\boldsymbol{\alpha}_{2}-\boldsymbol{\alpha}_{3},\boldsymbol{\beta}_{2}=\boldsymbol{\alpha}_{1}+2\boldsymbol{\alpha}_{2},\boldsymbol{\beta}_{3}=5\boldsymbol{\alpha}_{1}+10\boldsymbol{\alpha}_{2}-2\boldsymbol{\alpha}_{3}.</equation>

**解析:**解（ I ）记<equation>A=\left(\alpha_{1},\alpha_{2},\alpha_{3}\right),B=\left(\beta_{1},\beta_{2},\beta_{3}\right),A,B</equation>的列向量组分别记为 A,B.

首先，<equation>|A|=\left| \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 1 & 1 & 5 \end{array} \right|=1</equation>，故<equation>r(A)=3</equation>，A满秩.

由于向量组 B不能线性表示 A，故<equation>r(\mathbf{B})<3</equation>；否则 B也满秩，从而 B能线性表示 A，矛盾.由于<equation>r(\mathbf{B})<3</equation>，故<equation>| \boldsymbol {B} | = \left| \begin{array}{c c c} 1 & 1 & 3 \\ 1 & 2 & 4 \\ 1 & 3 & a \end{array} \right| \frac {c _ {2} - c _ {1}}{c _ {3} - 3 c _ {1}} \left| \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 1 \\ 1 & 2 & a - 3 \end{array} \right| = a - 5 = 0.</equation>因此，<equation>a=5.</equation>（Ⅱ）（法一）求<equation>B</equation>用<equation>A</equation>的线性表示，相当于求<equation>AX = B</equation>的解.<equation>X</equation>的列向量的坐标为线性表示的系数，即<equation>(\alpha_{1},\alpha_{2},\alpha_{3})\left(x_{1i},x_{2i},x_{3i}\right)^{\mathrm{T}} = \beta_{i}(i = 1,2,3)</equation>.<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {B}) = \left( \begin{array}{c c c c c c} 1 & 0 & 1 & 1 & 1 & 3 \\ 0 & 1 & 3 & 1 & 2 & 4 \\ 1 & 1 & 5 & 1 & 3 & 5 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c c c c} 1 & 0 & 1 & 1 & 1 & 3 \\ 0 & 1 & 3 & 1 & 2 & 4 \\ 0 & 1 & 4 & 0 & 2 & 2 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {*} - r _ {2}} \left( \begin{array}{c c c c c c} 1 & 0 & 1 & 1 & 1 & 3 \\ 0 & 1 & 3 & 1 & 2 & 4 \\ 0 & 0 & 1 & - 1 & 0 & - 2 \end{array} \right) \xrightarrow {r _ {1} - r _ {3} ^ {* *}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 2 & 1 & 5 \\ 0 & 1 & 0 & 4 & 2 & 1 0 \\ 0 & 0 & 1 & - 1 & 0 & - 2 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每做一次初等行变换，加一个*.）

因此，<equation>Ax = \beta_{1}</equation>的解为<equation>(2,4,-1)^{\mathrm{T}},\beta_{1} = 2\alpha_{1} + 4\alpha_{2} - \alpha_{3};Ax = \beta_{2}</equation>的解为<equation>(1,2,0)^{\mathrm{T}},\beta_{2} = \alpha_{1} + 2\alpha_{2};Ax = \beta_{3}</equation>的解为<equation>(5,10,-2)^{\mathrm{T}},\beta_{3} = 5\alpha_{1} + 10\alpha_{2} - 2\alpha_{3}.</equation>（法二）用克拉默法则分别求<equation>A x=\beta_{1}, A x=\beta_{2}, A x=\beta_{3}</equation>的解. x的分量为线性表示的系数，即<equation>\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)\left(x_{1},x_{2},x_{3}\right)^{\mathrm{T}}=\beta_{i}(i=1,2,3).</equation>首先，可计算得<equation>|A| = 1</equation>. 由克拉默法则知，<equation>Ax = \beta_{1}</equation>的解为<equation>x _ {1} = \left| \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 3 \\ 1 & 1 & 5 \end{array} \right| = 2, \quad x _ {2} = \left| \begin{array}{c c c} 1 & 1 & 1 \\ 0 & 1 & 3 \\ 1 & 1 & 5 \end{array} \right| = 4, \quad x _ {3} = \left| \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 1 \end{array} \right| = - 1.</equation>因此，<equation>\pmb{\beta}_{1} = 2\pmb{\alpha}_{1} + 4\pmb{\alpha}_{2} - \pmb{\alpha}_{3}</equation>。同理可得<equation>\pmb{\beta}_{2} = \pmb{\alpha}_{1} + 2\pmb{\alpha}_{2},\pmb{\beta}_{3} = 5\pmb{\alpha}_{1} + 10\pmb{\alpha}_{2} - 2\pmb{\alpha}_{3}</equation>。

---


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

**2025年第9题 | 选择题 | 5分 | 答案: C**
9. 设<equation>X_{1}, X_{2}, \dots , X_{2 0}</equation>是来自总体B(1,0.1)的简单随机样本，令<equation>T=\sum_{i=1}^{2 0} X_{i}</equation>利用泊松分布近似表示二项分布的方法可得<equation>P\{ T\leqslant 1\}\approx</equation>(    )

A.<equation>\frac{1} {\mathrm{e}^{2}}</equation>B.<equation>\frac{2} {\mathrm{e}^{2}}</equation>C.<equation>\frac{3} {\mathrm{e}^{2}}</equation>D.<equation>\frac{4} {\mathrm{e}^{2}}</equation>
答案: C
**解析: **解 由<equation>X_{i}(i = 1,2,\dots ,20)\sim B(1,0.1)</equation>可知，<equation>X_{i}</equation>可看作一次随机试验的结果，试验成功的概率为0.1，<equation>T = \sum_{i = 1}^{20}X_{i}</equation>可看作20次独立重复试验中试验成功的次数，服从<equation>B(20,0.1)</equation>.根据泊松定理，<equation>n = 20,p_{n} = 0.1,\lambda = 2,T</equation>近似服从参数为2的泊松分布.

因此，<equation>P \{T \leqslant 1 \} = P \{T = 0 \} + P \{T = 1 \} \approx \frac {2 ^ {0} \cdot \mathrm {e} ^ {- 2}}{1} + \frac {2 ^ {1} \cdot \mathrm {e} ^ {- 2}}{1} = \frac {3}{\mathrm {e} ^ {2}}.</equation>应选C.

---

**2024年第8题 | 选择题 | 5分 | 答案: B**
8. 设随机变量 X,Y相互独立，且 X服从正态分布 N(0,2),Y服从正态分布 N(-2,2).若<equation>P\{2 X+Y< a \}=P\{X>Y\}</equation>，则 a=（    )

A.<equation>- 2-\sqrt{1 0}</equation>B.<equation>- 2+\sqrt{1 0}</equation>C.<equation>- 2-\sqrt{6}</equation>D.<equation>- 2+\sqrt{6}</equation>
答案: B
**解析: **由于<equation>X\sim N(0,2),Y\sim N(-2,2)</equation>，故<equation>E(X) = 0,D(X) = 2,E(Y) = -2,D(Y) = 2</equation>，从而<equation>E (2 X + Y) = E (2 X) + E (Y) = 2 E (X) + E (Y) = - 2,</equation><equation>D (2 X + Y) = D (2 X) + D (Y) = 4 D (X) + D (Y) = 4 \times 2 + 2 = 1 0,</equation><equation>E (Y - X) = E (Y) - E (X) = - 2,</equation><equation>D (Y - X) = D (Y) + D (X) = 4.</equation>于是，<equation>2 X+Y\sim N(-2,1 0), Y-X\sim N(-2,4).</equation>将它们标准化可得<equation>\frac{2 X+Y+2}{\sqrt{1 0}}\sim N(0,1), \frac{Y-X+2}{2}</equation><equation>\sim N(0,1).</equation>由此可得，<equation>P \left\{2 X + Y < a \right\} = P \left\{2 X + Y \leqslant a \right\} = P \left\{\frac {2 X + Y + 2}{\sqrt {1 0}} \leqslant \frac {a + 2}{\sqrt {1 0}} \right\} = \Phi \left(\frac {a + 2}{\sqrt {1 0}}\right),</equation><equation>P \{X > Y \} = P \{Y - X < 0 \} = P \{Y - X \leqslant 0 \} = P \left\{\frac {Y - X + 2}{2} \leqslant 1 \right\} = \Phi (1),</equation>其中<equation>\varPhi(x)</equation>是标准正态分布<equation>N(0,1)</equation>的分布函数.

由<equation>P\{2X + Y < a\} = P\{X > Y\}</equation>可得<equation>\varPhi\left(\frac{a + 2}{\sqrt{10}}\right) = \varPhi(1).</equation>又因为<equation>\varPhi(x)</equation>单调增加，所以<equation>\frac{a + 2}{\sqrt{10}} = 1</equation>，即<equation>a = -2 + \sqrt{10}.</equation>因此，应选B.

---

**2024年第16题 | 填空题 | 5分**
16. 设随机试验每次成功的概率为 p，现进行3次独立重复试验，在至少成功1次的条件下，3次试验全部成功的概率为<equation>\frac{4}{1 3}</equation>，则 p=___
**答案: **#<equation>p = \frac{2}{3}</equation>
**解析: **解设 X为3次独立重复试验中试验成功的次数，则<equation>X\sim B(3,p).</equation>在至少成功1次的条件下， 3次试验全部成功的概率为<equation>P\{X=3\mid X\geqslant 1\}=\frac{P\{X=3,X\geqslant 1\}}{P\{X\geqslant 1\}}=\frac{P\{X=3\}}{P\{X\geqslant 1\}}=\frac{C_{3}^{3} p^{3}}{1-C_{3}^{0}(1-p)^{3}}=\frac{4}{13}.</equation>于是，<equation>\frac{p^{3}}{1-(1-p)^{3}}=\frac{4}{13}.</equation>整理可得<equation>3 p^{3}+4 p^{2}-4 p=0</equation>即 p（p+2）(3p-2）=0.由于 p>0，故 p<equation>=\frac{2}{3}.</equation>

---

**2023年第16题 | 填空题 | 5分**
16. 设随机变量与 Y相互独立， X且<equation>X\sim B\left(1,\frac{1}{3}\right),Y\sim B\left(2,\frac{1}{2}\right)</equation>则<equation>P\{X=Y\}=</equation>___
**解析: **解 由于<equation>X\sim B\left(1,\frac{1}{3}\right)</equation>，故<equation>P \left\{X = 0 \right\} = \mathrm {C} _ {1} ^ {0} \left(\frac {1}{3}\right) ^ {0} \left(\frac {2}{3}\right) ^ {1} = \frac {2}{3},</equation><equation>P \{X = 1 \} = C _ {1} ^ {1} \left(\frac {1}{3}\right) ^ {1} \left(\frac {2}{3}\right) ^ {0} = \frac {1}{3}.</equation>由于<equation>Y\sim B\left(2,\frac{1}{2}\right)</equation>，故<equation>P \left\{Y = 0 \right\} = \mathrm {C} _ {2} ^ {0} \left(\frac {1}{2}\right) ^ {0} \left(\frac {1}{2}\right) ^ {2} = \frac {1}{4},</equation><equation>P \left\{Y = 1 \right\} = \mathrm {C} _ {2} ^ {1} \left(\frac {1}{2}\right) ^ {1} \left(\frac {1}{2}\right) ^ {1} = \frac {1}{2}.</equation>因此，<equation>\begin{aligned} P \{X = Y \} &= P \{X = 0, Y = 0 \} + P \{X = 1, Y = 1 \} \\ \underline {{\text {独立性}}} P \{X = 0 \} P \{Y = 0 \} + P \{X = 1 \} P \{Y = 1 \} \\ &= \frac {2}{3} \times \frac {1}{4} + \frac {1}{3} \times \frac {1}{2} = \frac {1}{3}. \end{aligned}</equation>

---

**2019年第8题 | 选择题 | 4分 | 答案: A**
8. 设随机变量 X与 Y相互独立，且都服从正态分布<equation>N\left(\mu ,\sigma^{2}\right)</equation>，则<equation>P\{|X-Y|<1\}</equation>(    )

A. 与<equation>\mu</equation>无关，而与<equation>\sigma^{2}</equation>有关 B. 与<equation>\mu</equation>有关，而与<equation>\sigma^{2}</equation>无关

C. 与<equation>\mu,\sigma^{2}</equation>都有关 D. 与<equation>\mu,\sigma^{2}</equation>都无关
答案: A
**解析: **解 由于 X，Y相互独立且都服从正态分布<equation>N(\mu, \sigma^{2})</equation>，故<equation>E(X-Y)=0,D(X-Y)=2\sigma^{2},</equation><equation>X-Y\sim N(0,2\sigma^{2}).</equation>将 X-Y标准化，可得<equation>\frac{X-Y}{\sqrt{2}\sigma}\sim N(0,1).</equation>，于是，<equation>\begin{array}{l} P \left\{\mid X - Y \mid < 1 \right\} = P \left\{- 1 < X - Y < 1 \right\} = P \left\{\frac {- 1}{\sqrt {2} \sigma} < \frac {X - Y}{\sqrt {2} \sigma} < \frac {1}{\sqrt {2} \sigma} \right\} \\ = \Phi \left(\frac {1}{\sqrt {2} \sigma}\right) - \Phi \left(\frac {- 1}{\sqrt {2} \sigma}\right) = 2 \Phi \left(\frac {1}{\sqrt {2} \sigma}\right) - 1. \\ \end{array}</equation>因此，<equation>P\{|X - Y| < 1\}</equation>仅与<equation>\sigma^2</equation>有关.应选A.

---

**2018年第7题 | 选择题 | 4分 | 答案: A**
7. 设随机变量 X的概率密度 f(x)满足<equation>f(1+x)=f(1-x)</equation>，且<equation>\int_{0}^{2} f(x)\mathrm{d}x=0.6</equation>，则<equation>P\{ X<0\}=</equation>(    )

A. 0.2 B. 0.3 C. 0.4 D. 0.5
答案: A
**解析: **解（法一）由于<equation>f(1+x)=f(1-x)</equation>，故 f(x)的图像关于 x=1对称.于是，<equation>P\{X<0\}= P\{X>2\}.</equation>又因为<equation>P \{0 \leqslant X \leqslant 2 \} = \int_{0}^{2} f ( x ) \mathrm{d} x = 0. 6</equation>，且<equation>P \{X < 0 \} + P \{0 \leqslant X \leqslant 2 \} + P \{X > 2 \} = 1,</equation>所以<equation>P \{ X < 0 \} = \frac {1 - P \{0 \leqslant X \leqslant 2 \}}{2} = \frac {1 - 0 . 6}{2} = 0. 2.</equation>因此，应选A.

（法二）利用换元法.

由于<equation>\begin{aligned} \int_ {- \infty} ^ {0} f (x) \mathrm {d} x \xlongequal {u = 1 - x} \int_ {+ \infty} ^ {1} f (1 - u) \mathrm {d} (1 - u) &= \int_ {1} ^ {+ \infty} f (1 - u) \mathrm {d} u \\ \frac {f (1 + u) = f (1 - u)}{\mathrm {二}} \int_ {1} ^ {+ \infty} f (1 + u) \mathrm {d} u &= \int_ {2} ^ {+ \infty} f (t) \mathrm {d} t, \end{aligned}</equation>故<equation>P\{X < 0\} = P\{X > 2\}</equation>.

其余同法一.

---

**2017年第14题 | 填空题 | 4分**
14. 设随机变量 X的分布函数为<equation>F ( x )=0. 5 \Phi ( x )+0. 5 \Phi \left( \frac{x-4}{2} \right)</equation>，其中<equation>\Phi ( x )</equation>为标准正态分布函数，则<equation>E ( X )=</equation>
**答案: **```latex
2
```

**解析:**解记<equation>\varphi(x)</equation>为标准正态分布的概率密度函数，则<equation>\int_{-\infty}^{+\infty}\varphi(x)\mathrm{d}x=1,\int_{-\infty}^{+\infty}x\varphi(x)\mathrm{d}x=0.</equation>由题设知，X的概率密度为<equation>f(x)=F^{\prime}(x)=0. 5 \varphi(x)+0. 2 5 \varphi \left( \frac{x-4}{2} \right)</equation>，于是<equation>\begin{aligned} E (X) &= \int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \int_ {- \infty} ^ {+ \infty} \left[ 0. 5 x \varphi (x) + 0. 2 5 x \varphi \left(\frac {x - 4}{2}\right) \right] \mathrm {d} x \\ &= 0 + 0. 2 5 \int_ {- \infty} ^ {+ \infty} x \varphi \left(\frac {x - 4}{2}\right) \mathrm {d} x \xlongequal {t = \frac {x - 4}{2}} 0. 5 \int_ {- \infty} ^ {+ \infty} (2 t + 4) \varphi (t) \mathrm {d} t \\ &= \int_ {- \infty} ^ {+ \infty} t \varphi (t) \mathrm {d} t + 2 \int_ {- \infty} ^ {+ \infty} \varphi (t) \mathrm {d} t = 0 + 2 = 2. \end{aligned}</equation>

---

**2016年第7题 | 选择题 | 4分 | 答案: B**

7. 设随机变量<equation>X\sim N(\mu,\sigma^{2})(\sigma>0)</equation>，记<equation>p=P\{X\leqslant\mu+\sigma^{2}\}</equation>，则（    )

A. p随着<equation>\mu</equation>的增加而增加 B. p随着<equation>\sigma</equation>的增加而增加

C. p随着<equation>\mu</equation>的增加而减少 D. p随着<equation>\sigma</equation>的增加而减少

答案: B

**解析:**解（法一）令<equation>Y=\frac{X-\mu}{\sigma}</equation>，则由<equation>X\sim N(\mu ,\sigma^{2})</equation>知，<equation>Y\sim N(0,1).</equation>又<equation>p = P \left\{X \leqslant \mu + \sigma^ {2} \right\} = P \left\{\frac {X - \mu}{\sigma} \leqslant \sigma \right\} = P \left\{Y \leqslant \sigma \right\}</equation>故 p与<equation>\mu</equation>的取值无关，且p随着<equation>\sigma</equation>的增加而增加.应选B.

（法二）由于<equation>X\sim N(\mu ,\sigma^2)</equation>，故<equation>\begin{array}{l} p = P \left\{X \leqslant \mu + \sigma^ {2} \right\} = \int_ {- \infty} ^ {\mu + \sigma^ {2}} \frac {1}{\sqrt {2 \pi} \sigma} \mathrm {e} ^ {- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}} \mathrm {d} x \\ = \int_ {- \infty} ^ {\mu} \frac {1}{\sqrt {2 \pi} \sigma} \mathrm {e} ^ {- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}} \mathrm {d} x + \int_ {\mu} ^ {\mu + \sigma^ {2}} \frac {1}{\sqrt {2 \pi} \sigma} \mathrm {e} ^ {- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}} \mathrm {d} x \\ = \frac {1}{2} + \int_ {\mu} ^ {\mu + \sigma^ {2}} \frac {1}{\sqrt {2 \pi} \sigma} \mathrm {e} ^ {- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}} \mathrm {d} x \xlongequal {t = \frac {x - \mu}{\sigma}} \frac {1}{2} + \int_ {0} ^ {\sigma} \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {t ^ {2}}{2}} \mathrm {d} t, \\ \end{array}</equation>从而<equation>p</equation>与<equation>\mu</equation>的取值无关，且<equation>p</equation>随着<equation>\sigma</equation>的增加而增加.应选B.

---

**2013年第7题 | 选择题 | 4分 | 答案: A**

7. 设<equation>X_{1}, X_{2}, X_{3}</equation>是随机变量，且<equation>X_{1}\sim N(0,1), X_{2}\sim N\left(0,2^{2}\right), X_{3}\sim N\left(5,3^{2}\right), p_{i}=P\left\{-2\leqslant X_{i}\leqslant 2\right\} (i=1,2,3)</equation>则（    ）

A.<equation>p_{1}>p_{2}>p_{3}</equation>B.<equation>p_{2}>p_{1}>p_{3}</equation>C.<equation>p_{3}>p_{1}>p_{2}</equation>D.<equation>p_{1}>p_{3}>p_{2}</equation>

答案: A

**解析:**解 由<equation>X_{2} \sim N(0,2^{2}), X_{3} \sim N(5,3^{2})</equation>知，<equation>\frac{X_2}{2} \sim N(0,1), \frac{X_3 - 5}{3} \sim N(0,1)</equation>.于是，<equation>p_{1} = P\{-2 \leqslant X_{1} \leqslant 2\} = \Phi (2) - \Phi (-2) = 1 - \Phi (-2) - \Phi (-2) = 1 - 2\Phi (-2),</equation><equation>p_{2} = P\{-2 \leqslant X_{2} \leqslant 2\} = P\{-1 \leqslant \frac{X_{2}}{2} \leqslant 1\} = \Phi (1) - \Phi (-1) = 1 - 2\Phi (-1),</equation><equation>p_{3} = P\{-2 \leqslant X_{3} \leqslant 2\} = P\{- \frac{7}{3} \leqslant \frac{X_3 - 5}{3} \leqslant -1\} = \Phi (-1) - \Phi \left(-\frac{7}{3}\right).</equation>于<equation>\Phi (-1) > \Phi (-2)</equation>，故<equation>p_{1} > p_{2}</equation>.

由于<equation>\varPhi(-1) > \varPhi(-2)</equation>，故<equation>p_1 > p_2</equation>。

设标准正态分布的概率密度为<equation>\varphi(x)</equation>，则<equation>\varphi(x)</equation>为偶函数，且在<equation>(-\infty ,0]</equation>上单调增加（如图所示）.又由于<equation>p_{2}=\int_{-1}^{1}\varphi(x)\mathrm{d}x, p_{3}=</equation><equation>\int_{-\frac{7}{3}}^{-1}\varphi(x)\mathrm{d}x</equation>，而<equation>\varphi(x)</equation>在（-1,1）上的取值都大于<equation>\varphi(x)</equation>在<equation>\left(-\frac{7}{3},-1\right)</equation>上的取值，且积分区间的长度满足<equation>|1-(-1)|> \left| -1-\left(-\frac{7}{3}\right) \right|</equation>，故<equation>p_{2}>p_{3}.</equation>综上所述，<equation>p_{1}>p_{2}>p_{3}.</equation>应选A.

---

**2013年第14题 | 填空题 | 4分**

14. 设随机变量<equation>Y</equation>服从参数为 1 的指数分布,<equation>a</equation>为常数且大于零, 则<equation>P\{Y \leqslant a+1 \mid Y > a\} =</equation>___

**解析:**解 由题设知，Y的概率密度为<equation>f_{Y}(y)=\left\{\begin{array}{ll}\mathrm{e}^{-y},&y>0,\\ 0,&y\leqslant 0.\end{array}\right.</equation>又 a > 0，故<equation>P \left\{Y \leqslant a + 1 \mid Y > a \right\} = \frac {P \left\{a < Y \leqslant a + 1 \right\}}{P \left\{Y > a \right\}} = \frac {\int_ {a} ^ {a + 1} \mathrm {e} ^ {- y} \mathrm {d} y}{\int_ {a} ^ {+ \infty} \mathrm {e} ^ {- y} \mathrm {d} y} = \frac {\mathrm {e} ^ {- a} - \mathrm {e} ^ {- a - 1}}{\mathrm {e} ^ {- a}} = 1 - \frac {1}{\mathrm {e}}.</equation>

---

**2011年第7题 | 选择题 | 4分 | 答案: D**

7. 设<equation>F_{1}(x)</equation>与<equation>F_{2}(x)</equation>为两个分布函数，其相应的概率密度<equation>f_{1}(x)</equation>与<equation>f_{2}(x)</equation>是连续函数，则必为概率密度的是（    )

A.<equation>f_{1}(x)f_{2}(x)</equation>B.<equation>2f_{2}(x)F_{1}(x)</equation>C.<equation>f_{1}(x)F_{2}(x)</equation>D.<equation>f_{1}(x)F_{2}(x)+f_{2}(x)F_{1}(x)</equation>

答案: D

**解析:**解 由分布函数和概率密度的性质知，<equation>f_{1}(x)F_{2}(x) + f_{2}(x)F_{1}(x)\geqslant 0</equation>，且<equation>\begin{aligned} \int_ {- \infty} ^ {+ \infty} \left[ f _ {1} (x) F _ {2} (x) + f _ {2} (x) F _ {1} (x) \right] \mathrm {d} x &= \int_ {- \infty} ^ {+ \infty} \left[ F _ {1} (x) F _ {2} (x) \right] ^ {\prime} \mathrm {d} x \\ &= F _ {1} (+ \infty) F _ {2} (+ \infty) - F _ {1} (- \infty) F _ {2} (- \infty) \\ &= 1 - 0 = 1. \end{aligned}</equation>因此，<equation>f_{1}(x)F_{2}(x) + f_{2}(x)F_{1}(x)</equation>为概率密度.应选D.

---

**2010年第7题 | 选择题 | 4分 | 答案: C**

7. 设随机变量 X的分布函数 F(x) =<equation>\left\{\begin{array}{l l}0,&x<0,\\ \frac{1}{2},&0\leqslant x<1,\\ 1-\mathrm{e}^{-x},&x\geqslant 1,\end{array} \right.</equation>则 P{X=1} =（    )

A. 0 B.<equation>\frac{1}{2}</equation>C.<equation>\frac{1}{2}-\mathrm{e}^{-1}</equation><equation>1 - \mathrm {e} ^ {- 1}</equation>

答案: C

**解析:**解<equation>P \{ X = 1 \} = P \{ X \leqslant 1 \} - P \{ X < 1 \} = F ( 1 ) - F ( 1^{-} ) = 1 - \frac{1} {\mathrm{e}} - \frac{1}{2} = \frac{1}{2} - \frac{1} {\mathrm{e}}</equation>，故选C.

---

**2010年第8题 | 选择题 | 4分 | 答案: A**

8. 设<equation>f_{1}(x)</equation>为标准正态分布的概率密度，<equation>f_{2}(x)</equation>为<equation>[-1,3]</equation>上均匀分布的概率密度，若<equation>f (x) = \left\{ \begin{array}{l l} a f _ {1} (x), & x \leqslant 0, \\ b f _ {2} (x), & x > 0 \end{array} \right. \quad (a > 0, b > 0)</equation>为概率密度，则 a,b应满足（    ）

A. 2a+3b=4 B. 3a+2b=4 C. a+b=1 D. a+b=2

答案: A

**解析:**解 由于标准正态分布的概率密度的图形关于 x=0对称，故<equation>\int_{0}^{+\infty} f_{1}(x)\mathrm{d}x=\int_{-\infty}^{0} f_{1}(x)\mathrm{d}x=\frac{1}{2}.</equation>又由题设知，<equation>f_{2}(x)=\left\{\begin{array}{ll}\frac{1}{4},&-1\leqslant x\leqslant 3,\\ 0,&\text{其他}.\end{array} \right.</equation>由于 f(x)为概率密度，故<equation>1=\int_{-\infty}^{+\infty} f(x)\mathrm{d}x=\int_{-\infty}^{0} a f_{1}(x)\mathrm{d}x+\int_{0}^{+\infty} b f_{2}(x)\mathrm{d}x=\frac{1}{2} a+\int_{0}^{3} \frac{b}{4}\mathrm{d}x=\frac{1}{2} a+\frac{3}{4} b,</equation>即<equation>\frac{1}{2} a+\frac{3}{4} b=1</equation>从而2a+3b=4.应选A.

---


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

**2025年第16题 | 填空题 | 5分**
16. 设 A,B为两个随机事件，且 A与 B相互独立，已知<equation>P ( A )=2 P ( B )</equation><equation>P ( A \cup B )=\frac{5}{8}</equation>，则在事件 A,B至少有一个发生的条件下，A,B中恰有一个发生的概率为___
**解析: **解 根据条件概率公式，A，B中至少有一个发生的条件下，A，B中恰好有一个发生的概率为<equation>\begin{aligned} P \left(A \bar {B} \cup \bar {A} B \mid A \cup B\right) &= \frac {P \left[ \left(A \bar {B} \cup \bar {A} B\right) \cap (A \cup B) \right]}{P (A \cup B)} = \frac {P \left(A \bar {B} \cup \bar {A} B\right)}{P (A \cup B)} \\ &= \frac {P \left(A \bar {B}\right) + P \left(\bar {A} B\right)}{P \left(A \cup B\right)} \xlongequal {\text {独立 性}} \frac {P (A) P (\bar {B}) + P (\bar {A}) P (B)}{P (A \cup B)}. \end{aligned}</equation>下面计算<equation>P ( A ) , P ( B )</equation>由于 A，B相互独立，故<equation>P ( A B )=P ( A ) P ( B )</equation>，结合<equation>P ( A )=2 P ( B )</equation>可得<equation>\frac{5}{8}=P(A\cup B)=P(A)+P(B)-P(AB)=P(A)+P(B)-P(A)P(B)=3P(B)-2[P(B)]^{2}.</equation>整理可得<equation>1 6 \left[ P (B) \right]^{2}-2 4 P (B)+5=0</equation>即<equation>\left[ 4 P (B)-1 \right] \left[ 4 P (B)-5 \right]=0.</equation>解得<equation>P (B)=\frac{1}{4}</equation>舍去<equation>P (B)=\frac{5}{4}).</equation>进一步可得<equation>P (A)=2 P (B)=\frac{1}{2}.</equation>因此<equation>P \left(A \bar {B} \cup \bar {A} B \mid A \cup B\right) = \frac {P (A) P (\bar {B}) + P (\bar {A}) P (B)}{P (A \cup B)} = \frac {\frac {1}{2} \cdot \frac {3}{4} + \frac {1}{2} \cdot \frac {1}{4}}{\frac {5}{8}} = \frac {4}{5}.</equation>

---

**2022年第16题 | 填空题 | 5分**
16. 设 A,B,C为随机事件，且 A与 B互不相容，A与 C互不相容，B与 C相互独立，<equation>P ( A )=P ( B )=P ( C )=\frac{1}{3}</equation>，则<equation>P ( B \cup C \mid A \cup B \cup C )=</equation>___
**解析: **由于<equation>A,B</equation>互不相容，<equation>A,C</equation>互不相容，<equation>B,C</equation>相互独立，故<equation>P (A B) = 0, \quad P (A C) = 0, \quad P (B C) = P (B) P (C) = \frac {1}{9}, \quad P (A B C) = 0.</equation>由条件概率公式，<equation>\begin{aligned} P (B \cup C \mid A \cup B \cup C) &= \frac {P [ (B \cup C) \cap (A \cup B \cup C) ]}{P (A \cup B \cup C)} = \frac {P (B \cup C)}{P (A \cup B \cup C)} \\ &= \frac {P (B) + P (C) - P (B C)}{P (A) + P (B) + P (C) - P (A B) - P (B C) - P (A C) + P (A B C)} \\ &= \frac {\frac {1}{3} + \frac {1}{3} - \frac {1}{9}}{\frac {1}{3} + \frac {1}{3} + \frac {1}{3} - \frac {1}{9}} = \frac {5}{8}. \end{aligned}</equation>

---

**2021年第8题 | 选择题 | 5分 | 答案: D**
8. 设 A,B为随机事件，且<equation>0 < P ( B ) < 1</equation>，下列命题中为假命题的是（    )

A. 若<equation>P ( A \mid B )=P ( A )</equation>，则<equation>P ( A \mid \bar{B})=P ( A )</equation>B. 若<equation>P ( A \mid B )>P ( A )</equation>，则<equation>P ( \bar{A} \mid \bar{B})>P ( \bar{A} )</equation>C. 若<equation>P ( A \mid B )>P ( A \mid \bar{B})</equation>，则<equation>P ( A \mid B )>P ( A )</equation>D. 若<equation>P ( A \mid A \cup B )>P ( \bar{A} \mid A \cup B)</equation>，则<equation>P ( A )>P ( B )</equation>
答案: D
**解析: **解 考虑选项 D.<equation>P (A \mid A \cup B) = \frac {P (A \cap (A \cup B))}{P (A \cup B)} = \frac {P (A)}{P (A) + P (B) - P (A B)},</equation><equation>P (\bar {A} \mid A \cup B) = \frac {P (\bar {A} \cap (A \cup B))}{P (A \cup B)} = \frac {P (\bar {A} B)}{P (A) + P (B) - P (A B)} = \frac {P (B) - P (A B)}{P (A) + P (B) - P (A B)}.</equation>若<equation>P(A \mid A \cup B) > P(\overline{A} \mid A \cup B)</equation>，则<equation>P(A) > P(B) - P(AB)</equation>. 但这并不能保证<equation>P(A) > P(B)</equation>.由此出发考虑选项D的反例.例如：<equation>A = B</equation>，则<equation>P(A \mid A \cup B) = 1 > 0 = P(\overline{A} \mid A \cup B)</equation>，但<equation>P(A) = P(B)</equation>.

因此，应选D.

下面说明选项A、B、C不正确.

选项A：由于<equation>P ( A )=P ( A \mid B )=\frac{P ( A B )}{P ( B )}</equation>，故<equation>P ( A B )=P ( A ) P ( B )</equation>，从而A，B独立.由A，B独立可得A，<equation>\overline{B}</equation>独立，故<equation>P ( A \mid \overline{B})=P ( A ).</equation>选项A成立.

选项B：若<equation>P ( A \mid B ) > P ( A )</equation>，即<equation>\frac{P ( A B )}{P ( B )} > P ( A )</equation>，则<equation>P ( A B ) > P ( A ) P ( B ).</equation><equation>\begin{aligned} P (\bar {A} \mid \bar {B}) &= \frac {P (\bar {A} \bar {B})}{P (\bar {B})} = \frac {1 - P (A \cup B)}{1 - P (B)} = \frac {1 - P (A) - P (B) + P (A B)}{1 - P (B)} \\ > \frac {1 - P (A) - P (B) + P (A) P (B)}{1 - P (B)} &= 1 - P (A) = P (\bar {A}). \end{aligned}</equation>选项B成立.

选项C：若<equation>P ( A \mid B ) > P ( A \mid \bar{B} )</equation>，即<equation>\frac{P ( A B )}{P ( B )} >\frac{P ( A B )}{P (\bar{B})}</equation>，则<equation>\frac{P ( A B )}{P ( B )} >\frac{P ( A ) - P ( A B )}{1 - P ( B )}.</equation>由此可得<equation>P ( A B ) - P ( B ) P ( A B ) > P ( A ) P ( B ) - P ( B ) P ( A B )</equation>即<equation>P ( A B ) > P ( A ) P ( B ).</equation>于是，<equation>P ( A ) < \frac { P ( A B ) } { P ( B ) } = P ( A \mid B ) .</equation>选项C成立.

---

**2020年第7题 | 选择题 | 4分 | 答案: D**
7. 设 A,B,C为三个随机事件，且<equation>P ( A )=P ( B )=P ( C )=\frac{1}{4}, P ( A B )=0, P ( A C )=P ( B C )=\frac{1}{1 2}</equation>，则 A,B,C中恰有一个事件发生的概率为（    ）

A.<equation>\frac{3}{4}</equation>B.<equation>\frac{2}{3}</equation>C.<equation>\frac{1}{2}</equation>D.<equation>\frac{5}{1 2}</equation>
答案: D
**解析: **<equation>\begin{aligned} P (A \cup B \cup C) &= P (A) + P (B) + P (C) - P (A B) - P (B C) - P (A C) + P (A B C) \\ &= \frac {1}{4} + \frac {1}{4} + \frac {1}{4} - 0 - \frac {1}{1 2} - \frac {1}{1 2} + 0 = \frac {7}{1 2}. \end{aligned}</equation><equation>\begin{aligned} P (A B \cup B C \cup A C) &= P (A B) + P (B C) + P (A C) - P (A B C) - P (A B C) + P (A B C) \\ &= 0 + \frac {1}{1 2} + \frac {1}{1 2} + 0 = \frac {1}{6}. \end{aligned}</equation>从而，<equation>p=\frac{7}{12}-\frac{1}{6}=\frac{5}{12}.</equation>因此，应选D.

（法二）A,B,C中恰有一个事件发生的概率为<equation>p=P(A\overline{B}\overline{C})+P(\overline{A}B\overline{C})+P(\overline{A}\overline{B}C).</equation><equation>P \left(A \bar {B} \bar {C}\right) = P \left(A \bar {B}\right) - P \left(A \bar {B} C\right) = P (A) - P (A B) - \left[ P (A C) - P (A C B) \right],</equation><equation>P (\bar {A} B \bar {C}) = P (\bar {A} B) - P (\bar {A} B C) = P (B) - P (A B) - [ P (B C) - P (B C A) ],</equation><equation>P (\bar {A} \bar {B} C) = P (\bar {B} C) - P (\bar {B} C A) = P (C) - P (C B) - [ P (C A) - P (C A B) ].</equation>由<equation>P ( A B ) = 0</equation>可得<equation>P ( A B C ) = 0.</equation>因此，<equation>p = P (A) + P (B) + P (C) - 2 \left[ P (A B) + P (B C) + P (A C) \right] = \frac {3}{4} - 4 \times \frac {1}{1 2} = \frac {5}{1 2}.</equation>应选 D.

解（法一）设 A,B,C中恰有一个事件发生的概率为 p. P（A U B U C）为至少发生一个事件的概率.“至少发生一个”可拆分为“恰好发生一个”，“至少发生两个”这样两个互不相容事件.于是，<equation>P (A \cup B \cup C) = p + P (A B \cup B C \cup A C).</equation>由<equation>P ( A B ) = 0</equation>可得<equation>P ( A B C ) = 0.</equation>由三个事件的加法公式可得

---

**2019年第7题 | 选择题 | 4分 | 答案: C**
7. 设 A,B为随机事件，则<equation>P ( A )=P ( B )</equation>的充分必要条件是（    ）

A.<equation>P ( A \cup B )=P ( A )+P ( B )</equation>B.<equation>P ( A B )=P ( A ) P ( B )</equation>C.<equation>P ( A \bar{B} )=P ( B \bar{A} )</equation>D.<equation>P ( A B )=P ( \bar{A} \bar{B} )</equation>
答案: C
**解析: **解 由于<equation>A\overline{B}=A-A\cap B, B\overline{A}=B-B\cap A</equation>，故<equation>P(A\overline{B})=P(A)-P(AB), P(B\overline{A})= P(B)-P(AB).</equation>因此，<equation>P ( A ) = P ( B )</equation>等价于<equation>P ( A \bar{B} ) = P ( B \bar{A} )</equation>应选C.

下面说明选项A、B、D不正确.

取<equation>A = B</equation>，且<equation>P(A) = P(B) = \frac{1}{3}</equation>.

选项 A：<equation>P ( A \cup B )=P ( A )=\frac{1}{3}, P ( A )+P ( B )=\frac{2}{3}.</equation>选项A不是<equation>P ( A )=P ( B )</equation>的必要条件.

选项B：<equation>P ( A B )=P ( A )=\frac{1}{3}, P ( A ) P ( B )=\frac{1}{9}.</equation>选项B不是<equation>P ( A )=P ( B )</equation>的必要条件.

选项D：<equation>P ( A B )=P ( A )=\frac{1}{3}, P ( \overline{{A}} \ \overline{{B}} )=P ( \overline{{A}} )=\frac{2}{3}.</equation>选项D不是<equation>P ( A )=P ( B )</equation>的必要条件.

---

**2018年第14题 | 填空题 | 4分**
14. 设随机事件 A与B相互独立，A与C相互独立，<equation>B C=\varnothing</equation>. 若<equation>P(A)=P(B)=\frac{1}{2}, P(AC\mid AB\cup C)=\frac{1}{4}</equation>，则 P(C)=
**解析: **解 由于事件 A与B相互独立，故<equation>P ( A B )=P ( A ) P ( B ).</equation>由于事件 A与C相互独立，故<equation>P ( A C )=P ( A ) P ( C ).</equation>根据事件运算的分配律，<equation>P ( A C \cap( A B \cup C) )=P((A C \cap A B)\cup( A C \cap C))\overset{B C=\varnothing}{=}P( A C ).</equation>根据条件概率的公式，<equation>\begin{aligned} P (A C \mid A B \cup C) &= \frac {P (A C \cap (A B \cup C))}{P (A B \cup C)} = \frac {P (A C)}{P (A B \cup C)} = \frac {P (A) P (C)}{P (A B) + P (C) - P (A B C)} \\ &= \frac {P (A) P (C)}{P (A) P (B) + P (C) - 0} = \frac {1}{4}. \end{aligned}</equation>代入<equation>P ( A )=P ( B )=\frac{1}{2}</equation>，可得<equation>\frac{\frac{1}{2} P ( C )}{\frac{1}{4}+P ( C )}=\frac{1}{4}.</equation>解得<equation>P ( C )=\frac{1}{4}.</equation>

---

**2017年第7题 | 选择题 | 4分 | 答案: A**
7. 设 A,B为随机事件.若<equation>0 < P ( A ) < 1, 0 < P ( B ) < 1</equation>，则<equation>P ( A \mid B ) > P ( A \mid \bar{B} )</equation>的充分必要条件是（    )

A.<equation>P ( B \mid A ) > P ( B \mid \bar{A} )</equation>B.<equation>P ( B \mid A ) < P ( B \mid \bar{A} )</equation>C.<equation>P ( \bar{B} \mid A ) > P ( B \mid \bar{A} )</equation>D.<equation>P ( \bar{B} \mid A ) < P ( B \mid \bar{A} )</equation>
答案: A
**解析: **解 （法一）由题设知，<equation>P (A \mid B) > P (A \mid \bar {B}) \Leftrightarrow \frac {P (A B)}{P (B)} > \frac {P (A \bar {B})}{P (\bar {B})} \Leftrightarrow \frac {P (A B)}{P (A B) + P (\bar {A} B)} > \frac {P (A \bar {B})}{P (A \bar {B}) + P (\bar {A} \bar {B})}.</equation>记<equation>P ( A B ) = a,P(\overline{A} B)=b,P(A\overline{B})=c,P(\overline{A}\overline{B})=d</equation>，则<equation>\frac{P(A B)}{P(A B)+P(\overline{A} B)} >\frac{P(A\overline{B})}{P(A\overline{B})+P(\overline{A}\overline{B})},</equation>即<equation>\frac{a}{a+b} >\frac{c}{c+d},</equation>由于 0 < P(A) < 1,0 < P(B) < 1，故 a+b=P(B),c+d=P<equation>\overline{{B}}</equation>, a+c=P(A),b+d=P<equation>\overline{{A}}</equation>均大于0.于是，<equation>\frac {a}{a + b} > \frac {c}{c + d} \Leftrightarrow a (c + d) > c (a + b) \Leftrightarrow a d > b c.</equation>ad > bc等价于<equation>a b + a d > a b + b c, \quad \text {即} \frac {a}{a + c} > \frac {b}{b + d}, \quad \text {也 即} P (B \mid A) > P (B \mid \bar {A}).</equation>因此，应选A.

（法二）由题设知，<equation>\begin{array}{l} P (A \mid B) > P (A \mid \bar {B}) \Leftrightarrow \frac {P (A B)}{P (B)} > \frac {P (A \bar {B})}{P (\bar {B})} = \frac {P (A) - P (A B)}{1 - P (B)} \\ \Leftrightarrow P (A B) [ 1 - P (B) ] > [ P (A) - P (A B) ] P (B) \\ \end{array}</equation><equation>\Leftrightarrow P (A B) > P (A) P (B).</equation>调换 A,B的位置，同上可得<equation>P (B \mid A) > P (B \mid \bar {A}) \Leftrightarrow P (B A) > P (B) P (A).</equation>又<equation>P ( A B ) = P ( B A )</equation>，故<equation>P (A \mid B) > P (A \mid \bar {B}) \Leftrightarrow P (B \mid A) > P (B \mid \bar {A}).</equation>因此，应选A.

---

**2015年第7题 | 选择题 | 4分 | 答案: C**
7. 若 A,B为任意两个随机事件，则（    ）

A.<equation>P ( A B ) \leqslant P ( A ) P ( B )</equation>B.<equation>P ( A B ) \geqslant P ( A ) P ( B )</equation>C.<equation>P ( A B ) \leqslant \frac { P ( A ) + P ( B ) } { 2 }</equation>D.<equation>P ( A B ) \geqslant \frac { P ( A ) + P ( B ) } { 2 }</equation>
答案: C
**解析: **解 由于 A<equation>\cap B \subseteq A</equation>，A<equation>\cap B \subseteq B</equation>，故<equation>P (A B) \leqslant P (A), \quad P (A B) \leqslant P (B).</equation>因此，<equation>2 P ( A B ) \leqslant P ( A )+P ( B )</equation>，即<equation>P ( A B ) \leqslant \frac { P ( A ) + P ( B ) } { 2 }</equation>应选C.

下面我们说明选项A、B、D不正确.

若 B<equation>\subseteq</equation>A,0 < P(A) < 1,0 < P(B) < 1<equation>，则 P(AB)=P(A</equation>\cap<equation>B）=P(B）>P(A)P(B).选项A不正确.

若 P(A) > 0，P(B) > 0且 A</equation>\cap<equation>B=</equation>\varnothing<equation>，则 P(AB) = P(A</equation>\cap<equation>B) = 0 < P(A)P(B)，P(AB) <</equation>\frac{P(A)+P(B)}{2} $ .选项B和选项D不正确.

---

**2014年第7题 | 选择题 | 4分 | 答案: B**
7. 设随机事件 A与 B相互独立，且<equation>P ( B )=0. 5, P ( A-B)=0. 3</equation>，则<equation>P ( B-A )=</equation>(    )

A. 0.1 B. 0.2 C. 0.3 D. 0.4
答案: B
**解析: **解（法一）由 A与B相互独立知，<equation>P ( A B ) = P ( A ) P ( B ).</equation>，于是，<equation>P (A - B) = P (A) - P (A B) = P (A) - P (A) P (B) = P (A) [ 1 - P (B) ] = 0. 5 P (A).</equation>从而<equation>P ( A ) = 2 P ( A - B ) = 0. 6.</equation>进一步可得，<equation>P (B - A) = P (B) - P (A B) = P (B) - P (A) P (B) = 0. 5 - 0. 6 \times 0. 5 = 0. 2.</equation>应选B.

（法二）由<equation>A</equation>与<equation>B</equation>相互独立知，<equation>A, B</equation>也相互独立.于是，<equation>0. 3 = P (A - B) = P (A \cap \bar {B}) = P (A \bar {B}) = P (A) P (\bar {B}) = 0. 5 P (A).</equation>因此，<equation>P ( A ) = 0. 6</equation>进一步可得，<equation>P (B - A) = P \left(B \bar {A}\right) = P (B) P (\bar {A}) = 0. 5 \times (1 - 0. 6) = 0. 2.</equation>应选B.

---

**2012年第14题 | 填空题 | 4分**
14. 设 A,B,C是随机事件，A与C互不相容，<equation>P ( A B )=\frac{1} {2}, P ( C )=\frac{1} {3}</equation>，则<equation>P ( A B \mid \bar{C})=</equation>___
**解析: **解 由条件概率的定义可知，<equation>P ( A B \mid \bar{C})=\frac{P ( A B \bar{C})}{P (\bar{C})}=\frac{P ( A B \bar{C})}{1-P(C)}.</equation>又 A与C互不相容，即<equation>A \cap C=\varnothing</equation>，故<equation>A \cap B \subset A \subset \bar{C}</equation>，从而<equation>A \cap B \cap \bar{C}=A \cap B.</equation>因此<equation>P ( A B \mid \bar{C})=\frac{P ( A B)}{1-P(C)}=\frac{\frac{1}{2}}{\frac{2}{3}}=\frac{3}{4}.</equation>

---


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

**2023年第9题 | 选择题 | 5分 | 答案: D**

9. 设<equation>X_{1}, X_{2}, \dots, X_{n}</equation>为来自总体<equation>N(\mu_{1},\sigma^{2})</equation>的简单随机样本，<equation>Y_{1}, Y_{2}, \dots, Y_{m}</equation>为来自总体<equation>N(\mu_{2},2\sigma^{2})</equation>的简单随机样本，且两样本相互独立，记<equation>\bar{X}=\frac{1}{n}\sum_{i=1}^{n}X_{i},\bar{Y}=\frac{1}{m}\sum_{i=1}^{m}Y_{i},S_{1}^{2}=\frac{1}{n-1}\sum_{i=1}^{n}(X_{i}-\bar{X})^{2},S_{2}^{2}=\frac{1}{m-1}\sum_{i=1}^{m}(Y_{i}-\bar{Y})^{2}</equation>，则（    )

A.<equation>\frac{S_{1}^{2}}{S_{2}^{2}}\sim F(n,m)</equation>B.<equation>\frac{S_{1}^{2}}{S_{2}^{2}}\sim F(n-1,m-1)</equation>C.<equation>\frac{2S_{1}^{2}}{S_{2}^{2}}\sim F(n,m)</equation>D.<equation>\frac{2S_{1}^{2}}{S_{2}^{2}}\sim F(n-1,m-1)</equation>

答案: D

**解析:**解<equation>S_{1}^{2}=\frac{1}{n-1}\sum_{i=1}^{n}\left(X_{i}-\overline{X}\right)^{2}</equation>为<equation>X_{1},X_{2},\dots,X_{n}</equation>的样本方差，<equation>S_{2}^{2}=\frac{1}{m-1}\sum_{i=1}^{m}\left(Y_{i}-\overline{Y}\right)^{2}</equation>为<equation>Y_{1},</equation><equation>Y_{2},\dots,Y_{m}</equation>的样本方差.由正态总体的抽样分布定理可知，<equation>\frac {(n - 1) S _ {1} ^ {2}}{\sigma^ {2}} \sim \chi^ {2} (n - 1), \quad \frac {(m - 1) S _ {2} ^ {2}}{2 \sigma^ {2}} \sim \chi^ {2} (m - 1).</equation>又因为两个样本相互独立，所以由<equation>F</equation>分布的定义可知<equation>\frac {\frac {(n - 1) S _ {1} ^ {2}}{\sigma^ {2}} / (n - 1)}{\frac {(m - 1) S _ {2} ^ {2}}{2 \sigma^ {2}} / (m - 1)} = \frac {S _ {1} ^ {2} / \sigma^ {2}}{S _ {2} ^ {2} / 2 \sigma^ {2}} = \frac {2 S _ {1} ^ {2}}{S _ {2} ^ {2}} \sim F (n - 1, m - 1).</equation>因此，应选D.

---

**2017年第8题 | 选择题 | 4分 | 答案: B**

8. 设<equation>X_{1}, X_{2}, \dots , X_{n} ( n \geqslant 2 )</equation>为来自总体<equation>N (\mu , 1)</equation>的简单随机样本，记<equation>\bar{X}=\frac{1}{n}\sum_{i=1}^{n} X_{i}</equation>，则下列结论中不正确的是（    )

A.<equation>\sum_{i=1}^{n} \left(X_{i}-\mu\right)^{2}</equation>服从<equation>\chi^{2}</equation>分布 B.<equation>2 \left(X_{n}-X_{1}\right)^{2}</equation>服从<equation>\chi^{2}</equation>分布

C.<equation>\sum_{i=1}^{n} \left(X_{i}-\bar{X}\right)^{2}</equation>服从<equation>\chi^{2}</equation>分布 D.<equation>n(\bar{X}-\mu)^{2}</equation>服从<equation>\chi^{2}</equation>分布

答案: B

**解析:**解 由题设知，<equation>X_{1},X_{2},\dots ,X_{n}</equation>相互独立且与总体同分布.

依次分析各选项.

由<equation>X_{i}\sim N(\mu ,1)</equation>知，<equation>X_{i} - \mu \sim N(0,1)</equation>，<equation>i = 1,2,\dots,n</equation>，故<equation>\sum_{i = 1}^{n}\left(X_{i} - \mu\right)^{2}\sim \chi^{2}(n)</equation>.选项A正确由<equation>X_{1}\sim N(\mu ,1)</equation>，<equation>X_{n}\sim N(\mu ,1)</equation>知，<equation>X_{n} - X_{1}\sim N(0,2)</equation>，故<equation>\frac{X_n - X_1}{\sqrt{2}}\sim N(0,1)</equation>，于是<equation>\frac{\left(X_n - X_1\right)^2}{2}\sim \chi^2(1)</equation>.但<equation>2\left(X_{n} - X_{1}\right)^{2}</equation>不服从<equation>\chi^2</equation>分布.选项B不正确.

事实上，若<equation>2 \left(X_{n}-X_{1}\right)^{2}\sim \chi^{2} (m)</equation>，则<equation>E \left[ 2 \left(X _ {n} - X _ {1}\right) ^ {2} \right] = m, \quad D \left[ 2 \left(X _ {n} - X _ {1}\right) ^ {2} \right] = 2 m.</equation>但由<equation>\frac{\left(X_{n}-X_{1}\right)^{2}}{2}\sim \chi^{2}(1)</equation>知，<equation>E \left[ \frac {\left(X _ {n} - X _ {1}\right) ^ {2}}{2} \right] = 1, \quad D \left[ \frac {\left(X _ {n} - X _ {1}\right) ^ {2}}{2} \right] = 2,</equation>从而<equation>E[2(X_{n}-X_{1})^{2}]=4,D[2(X_{n}-X_{1})^{2}]=32.</equation>这与<equation>D[2(X_{n}-X_{1})^{2}]=2E[2(X_{n}-X_{1})^{2}]</equation>矛盾，故<equation>2(X_{n}-X_{1})^{2}</equation>不服从<equation>\chi^{2}</equation>分布.

由性质(2）知，<equation>( n - 1 ) S^{2}\sim \chi^{2} ( n - 1 ).</equation>又因为<equation>S^{2}=\frac{1}{n-1}\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}</equation>，所以<equation>\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}\sim \chi^{2} ( n - 1 ).</equation>选项C正确.

由性质（2）知，<equation>\overline{X}=\frac{1}{n}\sum_{i=1}^{n}X_{i}\sim N\left(\mu ,\frac{1}{n}\right)</equation>，于是<equation>\sqrt{n} (\overline{X}-\mu)\sim N (0,1)</equation>，从而<equation>n(\overline{X}-\mu)^{2}\sim X^{2}(1).</equation>选项D正确.

综上所述，应选B.

---

**2013年第8题 | 选择题 | 4分 | 答案: C**

8. 设随机变量<equation>X\sim t(n),Y\sim F(1,n)</equation>，给定<equation>\alpha(0<\alpha<0.5)</equation>，常数c满足<equation>P\{X>c\}=\alpha</equation>，则<equation>P\left\{Y>c^{2}\right\}=(\quad)</equation>A.<equation>\alpha</equation>B.<equation>1-\alpha</equation>C.<equation>2\alpha</equation>D.<equation>1-2\alpha</equation>

答案: C

**解析:**解由 X ~ t(n)的定义可知，存在随机变量 U，V满足 U ~ N(0,1), V ~<equation>\chi^{2} (n)</equation>，且 U，V相互独立，使得<equation>X=\frac{U}{\sqrt{\frac{V}{n}}}</equation>，于是<equation>X^{2}=\frac{U^{2}}{\frac{V}{n}} \sim F(1,n)</equation>，从而

应选C.<equation>P \left\{ Y > c^{2} \right\}=P \left\{ X^{2}>c^{2} \right\}=P \left\{ X > c \right\}+P \left\{ X < - c \right\}=2 P \left\{ X > c \right\}=2 \alpha.</equation>

---


### 大数定律和中心极限定理

**2022年第9题 | 选择题 | 5分 | 答案: A**

9. 设随机变量<equation>X_{1}, X_{2}, \dots , X_{n}</equation>独立同分布，且<equation>X_{1}</equation>的4阶矩存在，记<equation>\mu_{k}=E \left( X_{1}^{k} \right) ( k=1, 2, 3, 4)</equation>，则根据切比雪夫不等式，对任意<equation>\varepsilon >0</equation>，都有<equation>P\left\{\left| \frac{1}{n}\sum_{i=1}^{n} X_{i}^{2}-\mu_{2} \right| \geqslant \varepsilon \right\} \leqslant</equation>(    )

A.<equation>\frac{\mu_{4}-\mu_{2}^{2}}{n\varepsilon^{2}}</equation>B.<equation>\frac{\mu_{4}-\mu_{2}^{2}}{\sqrt{n}\varepsilon^{2}}</equation>C.<equation>\frac{\mu_{2}-\mu_{1}^{2}}{n\varepsilon^{2}}</equation>D.<equation>\frac{\mu_{2}-\mu_{1}^{2}}{\sqrt{n}\varepsilon^{2}}</equation>

答案: A

**解析:**根据期望的性质，<equation>E \left(\frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} ^ {2}\right) = \frac {1}{n} E \left(\sum_ {i = 1} ^ {n} X _ {i} ^ {2}\right) = \frac {1}{n} \sum_ {i = 1} ^ {n} E \left(X _ {i} ^ {2}\right) \xlongequal {E \left(X _ {1} ^ {2}\right) = \mu_ {2}} \frac {1}{n} \cdot n \mu_ {2} = \mu_ {2}.</equation>根据切比雪夫不等式，对任意<equation>\varepsilon > 0</equation><equation>P \left\{\left| \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} ^ {2} - \mu_ {2} \right| \geqslant \varepsilon \right\} \leqslant \frac {D \left(\frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} ^ {2}\right)}{\varepsilon^ {2}}.</equation>由于随机变量<equation>X_{1}, X_{2}, \dots, X_{n}</equation>独立同分布，故<equation>X_{1}^{2}, X_{2}^{2}, \dots, X_{n}^{2}</equation>相互独立.<equation>\begin{array}{l} D \left(\frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} ^ {2}\right) = \frac {1}{n ^ {2}} D \left(\sum_ {i = 1} ^ {n} X _ {i} ^ {2}\right) = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} D \left(X _ {i} ^ {2}\right) = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} \left\{E \left(X _ {i} ^ {4}\right) - \left[ E \left(X _ {i} ^ {2}\right) \right] ^ {2} \right\} \\ = \frac {1}{n ^ {2}} \cdot n \left(\mu_ {4} - \mu_ {2} ^ {2}\right) = \frac {\mu_ {4} - \mu_ {2} ^ {2}}{n}. \\ \end{array}</equation>代入（1）式可得，<equation>P \left\{\left| \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} ^ {2} - \mu_ {2} \right| \geqslant \varepsilon \right\} \leqslant \frac {\mu_ {4} - \mu_ {2} ^ {2}}{n \varepsilon^ {2}}.</equation>因此，应选A.

---

**2020年第8题 | 选择题 | 4分 | 答案: B**

8. 设<equation>X_{1}, X_{2}, \dots , X_{1 0 0}</equation>为来自总体 X的简单随机样本，其中<equation>P\{X=0\}=P\{X=1\}=\frac{1}{2}, \Phi (x)</equation>表示标准正态分布函数，利用中心极限定理可得<equation>P\{\sum_{i=1}^{1 0 0} X_{i}\leqslant 5 5 \}</equation>的近似值为（    )

A. 1-<equation>\Phi (1)</equation>B.<equation>\Phi (1)</equation>C. 1-<equation>\Phi (0. 2)</equation>D.<equation>\Phi (0. 2)</equation>

答案: B

**解析:**解 计算 E（X），D（X）.<equation>E (X) = 0 \times \frac {1}{2} + 1 \times \frac {1}{2} = \frac {1}{2}.</equation><equation>E \left(X ^ {2}\right) = 0 ^ {2} \times \frac {1}{2} + 1 ^ {2} \times \frac {1}{2} = \frac {1}{2}.</equation><equation>D (X) = E \left(X ^ {2}\right) - \left[ E (X) \right] ^ {2} = \frac {1}{2} - \frac {1}{4} = \frac {1}{4}.</equation>由已知条件可知，<equation>n = 100</equation>根据列维-林德伯格中心极限定理，<equation>\sum_{i=1}^{1 0 0} X_{i}</equation>近似服从均值为<equation>1 0 0 \times \frac {1}{2}=5 0</equation>方差为<equation>1 0 0 \times \frac {1}{4}=</equation>25的正态分布，即N（50，25），从而<equation>\frac{\sum_{i=1}^{1 0 0} X_{i}-5 0}{5}</equation>近似服从N（0，1）.因此

因此，<equation>P \left\{\sum_ {i = 1} ^ {1 0 0} X _ {i} \leqslant 5 5 \right\} = P \left\{\frac {\sum_ {i = 1} ^ {1 0 0} X _ {i} - 5 0}{5} \leqslant \frac {5 5 - 5 0}{5} \right\} = \Phi (1).</equation>应选B.

---


**2017年第22题 | 解答题 | 11分**

设随机变量 X，Y相互独立，且 X的概率分布为<equation>P\{X=0\}=P\{X=2\}=\frac{1}{2},</equation>Y的概率密度为<equation>f (y) = \left\{ \begin{array}{l l} 2 y, & 0 < y < 1, \\ 0, & \text {其 他}. \end{array} \right.</equation>I. 求<equation>P\{Y\leqslant E(Y)\}</equation>；

II. 求<equation>Z=X+Y</equation>的概率密度
**答案: **（I）<equation>\frac{4}{9}</equation><equation>(\mathrm {I I}) f _ {Z} (z) = \left\{ \begin{array}{l l} z, & 0 < z < 1, \\ z - 2, & 2 < z < 3, \\ 0, & \text {其 他}. \end{array} \right.</equation>
**解析: **解（I）由题设知，<equation>E ( Y )=\int_{- \infty}^{+ \infty} y f ( y ) \mathrm{d} y=\int_{0}^{1} 2 y^{2} \mathrm{d} y=\frac{2}{3}.</equation>因此，<equation>P \left\{Y \leqslant E (Y) \right\} = P \left\{Y \leqslant \frac {2}{3} \right\} = \int_ {0} ^ {\frac {2}{3}} 2 y \mathrm {d} y = \frac {4}{9}.</equation>（Ⅱ）Z的分布函数为<equation>\begin{aligned} F _ {Z} (z) &= P \{Z \leqslant z \} = P \{X + Y \leqslant z \} \\ &= P \{X + Y \leqslant z, X = 0 \} + P \{X + Y \leqslant z, X = 2 \} \\ &= P \{Y \leqslant z, X = 0 \} + P \{Y \leqslant z - 2, X = 2 \} \\ \underline {{\underline {{X , Y \text {相 互 独立}}}}} P \{Y \leqslant z \} \cdot P \{X = 0 \} + P \{Y \leqslant z - 2 \} \cdot P \{X = 2 \} \\ &= \frac {1}{2} P \{Y \leqslant z \} + \frac {1}{2} P \{Y \leqslant z - 2 \}. \end{aligned}</equation>下面用两种方法求 Z的概率密度.

（法一）如图所示，当<equation>z\leqslant 0</equation>时，<equation>F_{Z}(z) = 0 + 0 = 0.</equation>当<equation>0 < z\leqslant 1</equation>时，<equation>F_{Z}(z) = \frac{1}{2}\int_{0}^{z}2y\mathrm{d}y + 0 = \frac{z^{2}}{2}</equation>.

当<equation>1 < z\leqslant 2</equation>时，<equation>F_{Z}(z) = \frac{1}{2}\int_{0}^{1}2y\mathrm{d}y + 0 = \frac{1}{2}.</equation>当<equation>2 < z\leqslant 3</equation>时，<equation>F_{Z}(z) = \frac{1}{2} +\frac{1}{2}\int_{0}^{z - 2}2y\mathrm{d}y = \frac{1}{2} +\frac{(z - 2)^{2}}{2}.</equation>当<equation>z > 3</equation>时，<equation>F_{Z}(z) = 1.</equation>综上所述，Z的概率密度为<equation>f _ {Z} (z) = F _ {Z} ^ {\prime} (z) = \left\{ \begin{array}{l l} z, & 0 < z < 1, \\ z - 2, & 2 < z < 3, \\ 0, & \text {其 他}. \end{array} \right.</equation>（法二）由<equation>Z</equation>的分布函数<equation>F_{Z}(z) = \frac{1}{2} P\{Y \leqslant z\} +\frac{1}{2} P\{Y \leqslant z - 2\}</equation>知，<equation>Z</equation>的概率密度为<equation>f _ {Z} (z) = F _ {Z} ^ {\prime} (z) = \frac {1}{2} f (z) + \frac {1}{2} f (z - 2).</equation>当<equation>z\leqslant 0</equation>时，<equation>z - 2\leqslant 0,f_Z(z) = 0 + 0 = 0.</equation>当<equation>0 < z < 1</equation>时，<equation>z - 2\leqslant 0,f_Z(z) = \frac{1}{2}\cdot 2z + 0 = z.</equation>当<equation>1\leqslant z\leqslant 2</equation>时，<equation>z - 2\leqslant 0,f_Z(z) = 0 + 0 = 0.</equation>当<equation>2 < z < 3</equation>时，<equation>0 < z - 2 < 1</equation>，<equation>f_{Z}(z) = 0 + \frac{1}{2}\cdot 2(z - 2) = z - 2.</equation>当<equation>z\geqslant 3</equation>时，<equation>z - 2\geqslant 1, f_Z(z) = 0 + 0 = 0.</equation>综上所述，<equation>f_{z}(z) = \left\{ \begin{array}{ll} z, & 0 < z < 1, \\ z - 2, & 2 < z < 3, \\ 0, & \text{其他}. \end{array} \right.</equation>

---

**2015年第22题 | 解答题 | 11分**

设随机变量 X的概率密度为<equation>f (x) = \left\{ \begin{array}{l l} 2 ^ {- x} \ln 2, & x > 0 \\ 0, & x \leqslant 0 \end{array} \right.</equation>对 X 进行独立重复的观测，直到第2个大于3的观测值出现时停止，记 Y为观测次数.

I. 求 Y的概率分布；

II. 求 E(Y).
**答案: **<equation>(2 2) (\mathrm {I}) P \{Y = k \} = \frac {1}{6 4} (k - 1) \left(\frac {7}{8}\right) ^ {k - 2}, k = 2, 3, \dots ;</equation><equation>(\mathrm {I I}) E (Y) = 1 6.</equation>
**解析: **解（I）由题设知，<equation>P \left\{X \leqslant 3 \right\} = \int_ {- \infty} ^ {3} f (x) \mathrm {d} x = \int_ {0} ^ {3} 2 ^ {- x} \ln 2 \mathrm {d} x = - 2 ^ {- x} \Big | _ {0} ^ {3} = - \frac {1}{8} - (- 1) = \frac {7}{8},</equation><equation>P \{X > 3 \} = 1 - P \{X \leqslant 3 \} = 1 - \frac {7}{8} = \frac {1}{8}.</equation>Y可能的取值为2，3，4，….又由于<equation>Y=k(k\geqslant 2)</equation>意味着前k-1次只有1次出现大于3的观测值，且第k次出现大于3的观测值，故Y的概率分布为<equation>P \left\{Y = k \right\} = \mathrm {C} _ {k - 1} ^ {1} \times \frac {1}{8} \times \left(\frac {7}{8}\right) ^ {k - 2} \times \frac {1}{8} = \frac {1}{6 4} (k - 1) \left(\frac {7}{8}\right) ^ {k - 2}, \quad k = 2, 3, \dots .</equation>（Ⅱ）（法一）由期望的定义知，<equation>E (Y) = \sum_ {k = 2} ^ {\infty} k \cdot P \{Y = k \} = \frac {1}{6 4} \sum_ {k = 2} ^ {\infty} k (k - 1) \left(\frac {7}{8}\right) ^ {k - 2}.</equation>考虑幂级数<equation>\sum_{k = 2}^{\infty}k(k - 1)x^{k - 2}</equation>，其收敛域为（-1，1），故该级数在<equation>x = \frac{7}{8}</equation>处收敛.当<equation>x\in(-1,1)</equation>时，<equation>\begin{aligned} \sum_ {k = 2} ^ {\infty} k (k - 1) x ^ {k - 2} &= \sum_ {k = 2} ^ {\infty} \left(x ^ {k}\right) ^ {\prime \prime} = \left(\sum_ {k = 2} ^ {\infty} x ^ {k}\right) ^ {\prime \prime} = \left(\frac {x ^ {2}}{1 - x}\right) ^ {\prime \prime} = \left(\frac {x ^ {2} - 1 + 1}{1 - x}\right) ^ {\prime \prime} \\ &= \left(- x - 1 + \frac {1}{1 - x}\right) ^ {\prime \prime} = \left(\frac {1}{1 - x}\right) ^ {\prime \prime} = \frac {2}{(1 - x) ^ {3}}. \end{aligned}</equation>因此，<equation>E (Y) = \frac {1}{6 4} \sum_ {k = 2} ^ {\infty} k (k - 1) \left(\frac {7}{8}\right) ^ {k - 2} = \frac {1}{6 4} \times \frac {2}{\left(1 - \frac {7}{8}\right) ^ {3}} = 1 6.</equation>（法二）利用几何分布的性质.

设<equation>Y_{1}</equation>表示出现第1个大于3的观测值时所需的观测次数，<equation>Y_{2}</equation>表示出现第1个大于3的观测值之后到出现第2个大于3的观测值时所需的观测次数，则<equation>Y = Y_{1} + Y_{2}</equation>，且<equation>Y_{1}, Y_{2}</equation>均服从参数为<equation>p = \frac{1}{8}</equation>的几何分布.于是<equation>E\left(Y_{1}\right) = E\left(Y_{2}\right) = \frac{1}{p} = 8.</equation>因此，<equation>E (Y) = E \left(Y _ {1}\right) + E \left(Y _ {2}\right) = 1 6.</equation>

---

**2014年第8题 | 选择题 | 4分 | 答案: D**
8. 设连续型随机变量<equation>X_{1}</equation>与<equation>X_{2}</equation>相互独立且方差均存在，<equation>X_{1}</equation>与<equation>X_{2}</equation>概率密度分别为<equation>f_{1}(x)</equation>与<equation>f_{2}(x)</equation>，随机变量<equation>Y_{1}</equation>的概率密度为<equation>f_{Y_{1}}(y)=\frac{1}{2}[f_{1}(y)+f_{2}(y)]</equation>，随机变量<equation>Y_{2}=\frac{1}{2}(X_{1}+X_{2})</equation>，则（    )

A.<equation>E \left( Y_{1} \right)>E \left( Y_{2} \right), D \left( Y_{1} \right)>D \left( Y_{2} \right)</equation>B.<equation>E \left( Y_{1} \right)=E \left( Y_{2} \right), D \left( Y_{1} \right)=D \left( Y_{2} \right)</equation>C.<equation>E \left( Y_{1} \right)=E \left( Y_{2} \right), D \left( Y_{1} \right)<D \left( Y_{2} \right)</equation>D.<equation>E \left( Y_{1} \right)=E \left( Y_{2} \right), D \left( Y_{1} \right)>D \left( Y_{2} \right)</equation>
答案: D
**解析: **解（法一）设<equation>E ( X_{1} )=\mu_{1}, E ( X_{2} )=\mu_{2}, D ( X_{1} )=\sigma_{1}^{2}, D ( X_{2} )=\sigma_{2}^{2}</equation>，则<equation>E ( X_{1}^{2} )=\mu_{1}^{2}+\sigma_{1}^{2},</equation><equation>E ( X_{2}^{2} )=\mu_{2}^{2}+\sigma_{2}^{2}</equation>，从而<equation>\begin{aligned} E \left(Y _ {1}\right) &= \int_ {- \infty} ^ {+ \infty} y f _ {Y _ {1}} (y) \mathrm {d} y = \frac {1}{2} \left[ \int_ {- \infty} ^ {+ \infty} y f _ {1} (y) \mathrm {d} y + \int_ {- \infty} ^ {+ \infty} y f _ {2} (y) \mathrm {d} y \right] \\ &= \frac {1}{2} \left[ E \left(X _ {1}\right) + E \left(X _ {2}\right) \right] = \frac {1}{2} \left(\mu_ {1} + \mu_ {2}\right), \end{aligned}</equation><equation>\begin{aligned} E \left(Y _ {1} ^ {2}\right) &= \int_ {- \infty} ^ {+ \infty} y ^ {2} f _ {Y _ {1}} (y) \mathrm {d} y = \frac {1}{2} \left[ \int_ {- \infty} ^ {+ \infty} y ^ {2} f _ {1} (y) \mathrm {d} y + \int_ {- \infty} ^ {+ \infty} y ^ {2} f _ {2} (y) \mathrm {d} y \right] \\ &= \frac {1}{2} \left[ E \left(X _ {1} ^ {2}\right) + E \left(X _ {2} ^ {2}\right) \right] = \frac {1}{2} \left(\mu_ {1} ^ {2} + \sigma_ {1} ^ {2} + \mu_ {2} ^ {2} + \sigma_ {2} ^ {2}\right), \end{aligned}</equation><equation>\begin{aligned} D \left(Y _ {1}\right) &= E \left(Y _ {1} ^ {2}\right) - \left[ E \left(Y _ {1}\right) \right] ^ {2} = \frac {1}{2} \left(\mu_ {1} ^ {2} + \sigma_ {1} ^ {2} + \mu_ {2} ^ {2} + \sigma_ {2} ^ {2}\right) - \frac {1}{4} \left(\mu_ {1} + \mu_ {2}\right) ^ {2} \\ &= \frac {1}{2} \left(\sigma_ {1} ^ {2} + \sigma_ {2} ^ {2}\right) + \frac {1}{4} \left(\mu_ {1} - \mu_ {2}\right) ^ {2}. \end{aligned}</equation>又<equation>E \left(Y _ {2}\right) = E \left[ \frac {1}{2} \left(X _ {1} + X _ {2}\right) \right] = \frac {1}{2} \left[ E \left(X _ {1}\right) + E \left(X _ {2}\right) \right] = \frac {1}{2} \left(\mu_ {1} + \mu_ {2}\right),</equation><equation>D \left(Y _ {2}\right) = D \left[ \frac {1}{2} \left(X _ {1} + X _ {2}\right) \right] \xlongequal {\text {X} _ {1}, X _ {2} \text {独 立}} \frac {1}{4} \left[ D \left(X _ {1}\right) + D \left(X _ {2}\right) \right] = \frac {1}{4} \left(\sigma_ {1} ^ {2} + \sigma_ {2} ^ {2}\right),</equation>故<equation>E \left(Y _ {1}\right) = E \left(Y _ {2}\right), \quad D \left(Y _ {1}\right) - D \left(Y _ {2}\right) = \frac {1}{4} \left(\sigma_ {1} ^ {2} + \sigma_ {2} ^ {2}\right) + \frac {1}{4} \left(\mu_ {1} - \mu_ {2}\right) ^ {2} \geqslant 0,</equation>等号成立当且仅当<equation>\sigma_{1} = \sigma_{2} = 0,\mu_{1} = \mu_{2}</equation>，但这与<equation>X_{1},X_{2}</equation>是连续型随机变量矛盾.因此，应选D.

（法二）特殊值法.

令<equation>X_{1}\sim N(0,1),X_{2}\sim N(0,1)</equation>，且<equation>X_{1}</equation>与<equation>X_{2}</equation>相互独立，则<equation>f_{1}(y) = f_{2}(y)</equation>，从而<equation>f _ {Y _ {1}} (y) = \frac {1}{2} \left[ f _ {1} (y) + f _ {2} (y) \right] = f _ {1} (y),</equation>于是<equation>Y_{1}\sim N(0,1).</equation>又<equation>Y_{2}=\frac{1}{2}\left(X_{1}+X_{2}\right)\sim N\left(0,\frac{1}{2}\right)</equation>，故<equation>E\left(Y_{1}\right)=E\left(Y_{2}\right)=0,D\left(Y_{1}\right)=1 > \frac{1}{2} = D\left(Y_{2}\right).</equation>因此，应选D.

---

**2014年第22题 | 解答题 | 11分**

22. (本题满分11分)

设随机变量 X的概率分布为<equation>P\{X=1\}=P\{X=2\}=\frac{1}{2}.</equation>在给定 X=i的条件下，随机变量 Y服从均匀分布<equation>U(0,i)\ (i=1,2).</equation>I. 求 Y的分布函数<equation>F_{Y}(y)</equation>；

II. 求 E(Y).
**答案: **(22) (I)<equation>F_{Y}(y)=\left\{ \begin{array}{ll}0,& y<0,\\ \frac{3}{4} y,& 0\leqslant y<1,\\ \frac{1}{2}+\frac{1}{4} y,& 1\leqslant y<2,\\ 1,& y\geqslant 2; \end{array} \right.</equation>（Ⅱ）<equation>\frac{3}{4}.</equation>
**解析: **解（I）由题设知，当<equation>X = 1</equation>时，<equation>Y\sim U(0,1)</equation>；当<equation>X = 2</equation>时，<equation>Y\sim U(0,2)</equation>.于是，<equation>\begin{array}{l} F _ {Y} (y) = P \left\{Y \leqslant y \right\} = P \left\{Y \leqslant y, X = 1 \right\} + P \left\{Y \leqslant y, X = 2 \right\} \\ = P \left\{Y \leqslant y \mid X = 1 \right\} P \left\{X = 1 \right\} + P \left\{Y \leqslant y \mid X = 2 \right\} P \left\{X = 2 \right\}. \\ \end{array}</equation>当<equation>y < 0</equation>时，<equation>F_{Y}(y)=0\times \frac{1}{2}+0\times \frac{1}{2}=0.</equation>当<equation>0 \leqslant y < 1</equation>时，<equation>F_{Y}(y) = \left(\int_{0}^{y}1\mathrm{d}y\right)\cdot \frac{1}{2} + \left(\int_{0}^{y}\frac{1}{2}\mathrm{d}y\right)\cdot \frac{1}{2} = \frac{3}{4} y.</equation>当<equation>1\leqslant y < 2</equation>时，<equation>F_{Y}(y) = \left(\int_{0}^{1}1\mathrm{d}y\right)\cdot \frac{1}{2} + \left(\int_{0}^{y}\frac{1}{2}\mathrm{d}y\right)\cdot \frac{1}{2} = \frac{1}{2} + \frac{1}{4} y.</equation>当<equation>y\geqslant 2</equation>时，<equation>F_{Y}(y) = 1\times \frac{1}{2} +1\times \frac{1}{2} = 1.</equation>因此，<equation>Y</equation>的分布函数为<equation>F_{Y}(y) = \left\{ \begin{array}{ll}0, & y < 0,\\ \frac{3}{4} y, & 0 \leqslant y < 1,\\ \frac{1}{2} +\frac{1}{4} y, & 1 \leqslant y < 2,\\ 1, & y \geqslant 2. \end{array} \right.</equation>（Ⅱ）由第（I）问中<equation>Y</equation>的分布函数的表达式知，<equation>Y</equation>的概率密度函数为<equation>f _ {Y} (y) = F _ {Y} ^ {\prime} (y) = \left\{ \begin{array}{l l} \frac {3}{4}, & 0 \leqslant y < 1, \\ \frac {1}{4}, & 1 \leqslant y < 2, \\ 0, & \text {其 他}. \end{array} \right.</equation>因此，<equation>E (Y) = \int_ {- \infty} ^ {+ \infty} y f _ {Y} (y) \mathrm {d} y = \int_ {0} ^ {1} \frac {3}{4} y \mathrm {d} y + \int_ {1} ^ {2} \frac {1}{4} y \mathrm {d} y = \frac {3}{8} + \frac {3}{8} = \frac {3}{4}.</equation>

---

**2011年第8题 | 选择题 | 4分 | 答案: B**
8. 设随机变量 X与 Y相互独立，且 E(X)与 E(Y)存在，记 U=<equation>\max \{ X, Y \}</equation><equation>V=\min \{ X, Y \}</equation>，则 E(UV) =（    )

A.<equation>E ( U ) \cdot E ( V )</equation>B.<equation>E ( X ) \cdot E ( Y )</equation>C.<equation>E ( U ) \cdot E ( Y )</equation>D.<equation>E ( X ) \cdot E ( V )</equation>
答案: B
**解析: **解（法一）由 U，V的定义知，<equation>U V=X Y</equation>.又 X与 Y相互独立，故<equation>E ( U V )=E ( X Y )=E ( X ) E ( Y )</equation>从而选B.

（法二）由于<equation>U=\max \{ X, Y \}=\frac{X+Y+\left| X-Y \right|}{2}, V=\min \{ X, Y \}=\frac{X+Y-\left| X-Y \right|}{2}</equation>，故<equation>U V=\frac{(X+Y)^{2}-\left| X-Y \right|^{2}}{4}=X Y</equation>.又 X与 Y相互独立，故<equation>E ( U V )=E ( X Y )=E ( X ) E ( Y )</equation>应选B.

---

**2010年第14题 | 填空题 | 4分**
14. 设随机变量<equation>X</equation>的概率分布为<equation>P\{X=k\}=\frac{C}{k!}, k=0,1,2,\cdots</equation>，则<equation>E(X^{2})=</equation>___
**解析: **由概率的性质可知，<equation>1 = \sum_ {k = 0} ^ {\infty} P \{X = k \} = \sum_ {k = 0} ^ {\infty} \frac {C}{k !} = C \mathrm {e},</equation>即<equation>C = \frac{1}{\mathrm{e}}</equation>. 于是<equation>X</equation>服从参数为1的泊松分布，<equation>E(X) = D(X) = 1</equation>，从而<equation>E \left(X ^ {2}\right) = D (X) + \left[ E (X) \right] ^ {2} = 1 + 1 = 2.</equation>

---

**2009年第7题 | 选择题 | 4分 | 答案: C**
7. 设随机变量 X的分布函数为<equation>F(x)=0. 3 \varPhi(x)+0. 7 \varPhi\left(\frac{x-1}{2}\right)</equation>，其中<equation>\varPhi(x)</equation>为标准正态分布的分布函数，则<equation>E(X)=</equation>(    )

A.0 B.0.3 C.0.7 D.1
答案: C
**解析: **解记<equation>\varphi(x)</equation>为标准正态分布的概率密度函数，则<equation>\int_{- \infty}^{+ \infty} \varphi(x)\mathrm{d}x=1, \int_{- \infty}^{+ \infty} x\varphi(x)\mathrm{d}x=0.</equation>由题设知，X的概率密度为<equation>f(x)=F^{\prime}(x)=0. 3 \varphi(x)+\frac{0. 7}{2} \varphi \left( \frac{x-1}{2} \right)</equation>，于是<equation>\begin{aligned} E (X) &= \int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \int_ {- \infty} ^ {+ \infty} \left[ 0. 3 x \varphi (x) + \frac {0 . 7}{2} x \varphi \left(\frac {x - 1}{2}\right) \right] \mathrm {d} x \\ &= 0 + \int_ {- \infty} ^ {+ \infty} \frac {0 . 7}{2} x \varphi \left(\frac {x - 1}{2}\right) \mathrm {d} x \xlongequal {t = \frac {x - 1}{2}} 0. 7 \int_ {- \infty} ^ {+ \infty} (2 t + 1) \varphi (t) \mathrm {d} t \\ &= 0. 7 \left[ 2 \int_ {- \infty} ^ {+ \infty} t \varphi (t) \mathrm {d} t + \int_ {- \infty} ^ {+ \infty} \varphi (t) \mathrm {d} t \right] = 0. 7. \end{aligned}</equation>因此，应选C.

---

**2020年第22题 | 解答题 | 11分**

设随机变量<equation>X_{1}, X_{2}, X_{3}</equation>相互独立，其中<equation>X_{1}</equation>与<equation>X_{2}</equation>均服从标准正态分布，<equation>X_{3}</equation>的概率分布为<equation>P\{X_{3}=0\}=</equation><equation>P\{X_{3}=1\}=\frac{1}{2}.</equation><equation>Y=X_{3}X_{1}+(1-X_{3})X_{2}.</equation>I. 求二维随机变量<equation>( X_{1}, Y )</equation>的分布函数，结果用标准正态分布函数<equation>\Phi ( x )</equation>表示；

II. 证明随机变量 Y服从标准正态分布.
**答案: **<equation>(\mathrm {I}) F (x, y) = \left\{ \begin{array}{l l} \frac {1}{2} \Phi (x) [ \Phi (y) + 1 ], & x \leqslant y, \\ \frac {1}{2} \Phi (y) [ \Phi (x) + 1 ], & x > y; \end{array} \right.</equation>（Ⅱ）证明略.
**解析: **（I）设<equation>(X_{1},Y)</equation>的分布函数为<equation>F(x,y)</equation>.根据定义，<equation>\begin{array}{l} F (x, y) = P \left\{X _ {1} \leqslant x, Y \leqslant y \right\} = P \left\{X _ {1} \leqslant x, X _ {3} X _ {1} + \left(1 - X _ {3}\right) X _ {2} \leqslant y \right\} \\ = P \left\{X _ {1} \leqslant x, X _ {2} \leqslant y, X _ {3} = 0 \right\} + P \left\{X _ {1} \leqslant x, X _ {1} \leqslant y, X _ {3} = 1 \right\} \\ \underline {{\text {独立性}}} P \left\{X _ {1} \leqslant x \right\} P \left\{X _ {2} \leqslant y \right\} P \left\{X _ {3} = 0 \right\} + P \left\{X _ {1} \leqslant x, X _ {1} \leqslant y \right\} P \left\{X _ {3} = 1 \right\} \\ = \frac {1}{2} P \left\{X _ {1} \leqslant x \right\} P \left\{X _ {2} \leqslant y \right\} + \frac {1}{2} P \left\{X _ {1} \leqslant x, X _ {1} \leqslant y \right\}. \\ \end{array}</equation>下面分情况讨论.

- 当<equation>x \leqslant y</equation>时，<equation>P\{X_{1} \leqslant x, X_{1} \leqslant y\} = P\{X_{1} \leqslant x\} = \varPhi(x).</equation><equation>\begin{array}{l} F (x, y) = \frac {1}{2} P \left\{X _ {1} \leqslant x \right\} P \left\{X _ {2} \leqslant y \right\} + \frac {1}{2} P \left\{X _ {1} \leqslant x, X _ {1} \leqslant y \right\} \\ = \frac {1}{2} \Phi (x) \Phi (y) + \frac {1}{2} \Phi (x) = \frac {1}{2} \Phi (x) [ \Phi (y) + 1 ]. \\ \end{array}</equation>- 当<equation>x > y</equation>时，<equation>P\{X_{1}\leqslant x,X_{1}\leqslant y\} = P\{X_{1}\leqslant y\} = \varPhi(y).</equation><equation>\begin{array}{l} F (x, y) = \frac {1}{2} P \left\{X _ {1} \leqslant x \right\} P \left\{X _ {2} \leqslant y \right\} + \frac {1}{2} P \left\{X _ {1} \leqslant x, X _ {1} \leqslant y \right\} \\ = \frac {1}{2} \Phi (x) \Phi (y) + \frac {1}{2} \Phi (y) = \frac {1}{2} \Phi (y) [ \Phi (x) + 1 ]. \\ \end{array}</equation>因此，<equation>F ( x,y) = \left\{ \begin{array}{l l} \frac{1}{2} \varPhi ( x ) [ \varPhi ( y ) + 1 ] , & x \leqslant y, \\ \frac{1}{2} \varPhi ( y ) [ \varPhi ( x ) + 1 ] , & x > y. \end{array} \right.</equation>（Ⅱ）计算 Y的边缘分布.<equation>F _ {Y} (y) = F (+ \infty , y) = \frac {1}{2} \Phi (y) [ \Phi (+ \infty) + 1 ] \xlongequal {\Phi (+ \infty) = 1} \Phi (y).</equation>由于<equation>Y</equation>的边缘分布函数为标准正态分布函数，故<equation>Y</equation>服从标准正态分布.

---

**2019年第22题 | 解答题 | 11分**
2. (本题满分11分)

设随机变量 X与 Y相互独立，X服从参数为1的指数分布，Y的概率分布为<equation>P\{Y=-1\}=p,P\{Y=1\}=</equation><equation>1-p(0<p<1).</equation>.令 Z=XY.

I. 求 Z的概率密度;

II. p为何值时，X与 Z不相关;

III. X与 Z是否相互独立?
**答案: **（I）<equation>Z</equation>的概率密度为<equation>f_{Z}(z)=\left\{\begin{array}{ll}p\mathrm{e}^{z},&z\leqslant 0,\\ (1-p)\mathrm{e}^{-z},&z>0;\end{array} \right.</equation>（Ⅱ）当<equation>p=\frac{1}{2}</equation>时，X与Z不相关；

（Ⅲ）X与Z不相互独立.
**解析: **（I）先计算<equation>Z</equation>的分布函数<equation>F_{Z}(z)</equation>.<equation>\begin{array}{l} F _ {Z} (z) = P \left\{X Y \leqslant z \right\} = P \left\{X \geqslant - z, Y = - 1 \right\} + P \left\{X \leqslant z, Y = 1 \right\} \\ \underline {{\text {独立 性}}} P \left\{X \geqslant - z \right\} P \left\{Y = - 1 \right\} + P \left\{X \leqslant z \right\} P \left\{Y = 1 \right\} \\ = p \left[ 1 - F _ {X} (- z) \right] + (1 - p) F _ {X} (z), \\ \end{array}</equation>其中<equation>F_{X}(x)</equation>是X的分布函数.

于是，Z的概率密度为<equation>f _ {Z} (z) = F _ {Z} ^ {\prime} (z) = \left\{p \left[ 1 - F _ {X} (- z) \right] + (1 - p) F _ {X} (z) \right\} ^ {\prime} = p f _ {X} (- z) + (1 - p) f _ {X} (z).</equation>由于<equation>X</equation>服从参数为1的指数分布，故<equation>X</equation>的概率密度为<equation>f_{X}(x) = \left\{ \begin{array}{ll} \mathrm{e}^{-x}, & x > 0, \\ 0, & x \leqslant 0. \end{array} \right.</equation>当<equation>z\leqslant 0</equation>时，<equation>-z\geqslant 0,f_{X}(-z) = \mathrm{e}^{z},f_{X}(z) = 0</equation>；当<equation>z > 0</equation>时，<equation>-z < 0,f_{X}(z) = \mathrm{e}^{-z},f_{X}(-z) = 0.</equation>因此，<equation>f _ {Z} (z) = \left\{ \begin{array}{l l} p \mathrm {e} ^ {z}, & z \leqslant 0, \\ (1 - p) \mathrm {e} ^ {- z}, & z > 0. \end{array} \right.</equation>（Ⅱ）计算<equation>\operatorname{Cov}(X, Z).</equation><equation>\begin{aligned} \operatorname {C o v} (X, Z) &= E (X Z) - E (X) E (Z) = E \left(X ^ {2} Y\right) - E (X) E (X Y) \\ \xlongequal {\text {独立性}} E \left(X ^ {2}\right) E (Y) - \left[ E (X) \right] ^ {2} E (Y) \\ &= D (X) E (Y). \end{aligned}</equation>下面分别计算 D（X），E（Y）.

由于<equation>X</equation>服从参数为1的指数分布，故<equation>D(X) = 1.</equation><equation>E (Y) = 1 \times (1 - p) + (- 1) \times p = 1 - 2 p.</equation>因此，<equation>\operatorname{Cov}(X,Z) = E(Y) = 1 - 2p.</equation>当<equation>p=\frac{1}{2}</equation>时，<equation>\operatorname{Cov}(X,Z)=0</equation>，X与Z不相关.

（Ⅲ）由第（Ⅱ）问可知，当<equation>p\neq \frac{1}{2}</equation>时，X与Z相关，从而不相互独立.

下面只需考虑 p =<equation>\frac{1}{2}</equation>的情况.

（法一）当<equation>p=\frac{1}{2}</equation>时，检验<equation>P\{X < 1,Z < 1\} = P\{X < 1\} P\{Z < 1\}</equation>是否成立.<equation>P \left\{X < 1 \right\} = \int_ {0} ^ {1} \mathrm {e} ^ {- x} \mathrm {d} x = 1 - \mathrm {e} ^ {- 1}.</equation><equation>\begin{aligned} P \{Z < 1 \} &= P \{X Y < 1 \} = F _ {Z} (1) = \frac {1}{2} \left[ 1 - F _ {X} (- 1) \right] + \frac {1}{2} F _ {X} (1) \\ &= \frac {1}{2} \times (1 - 0) + \frac {1}{2} \int_ {0} ^ {1} \mathrm {e} ^ {- x} \mathrm {d} x = \frac {1}{2} + \frac {1}{2} \left(1 - \mathrm {e} ^ {- 1}\right). \end{aligned}</equation><equation>\begin{aligned} P \{X < 1, Z < 1 \} &= P \{X < 1, X Y < 1 \} = P \{X \leqslant 0, X Y < 1 \} + P \{0 < X < 1, X Y < 1 \} \\ &= P \{0 < X < 1, X Y < 1 \} = P \{0 < X < 1, Y = 1 \} + P \{0 < X < 1, Y = - 1 \} \\ &= P \{0 < X < 1 \} = P \{X < 1 \} = 1 - \mathrm {e} ^ {- 1}. \end{aligned}</equation>由于<equation>1 - \mathrm{e}^{-1}\neq(1 - \mathrm{e}^{-1})\cdot\left[\frac{1}{2} +\frac{1}{2}(1 - \mathrm{e}^{-1})\right],</equation>故X，Z不相互独立.

（法二）当<equation>p=\frac{1}{2}</equation>时，检验<equation>P\{X > 1,Z < 1\} = P\{X > 1\} P\{Z < 1\}</equation>是否成立.

当 X > 1时，<equation>X Y < 1</equation>等价于<equation>Y < \frac{1}{X}.</equation>又因为此时<equation>\frac{1}{X} < 1</equation>，而Y只可能取1和-1两个值，所以<equation>Y < \frac{1}{X}</equation>能推出<equation>Y = -1.</equation>于是，<equation>P \left\{X > 1 \right\} = \int_ {1} ^ {+ \infty} \mathrm {e} ^ {- x} \mathrm {d} x = \mathrm {e} ^ {- 1}.</equation><equation>P \{Z < 1 \} \xlongequal {\text {同 法 一}} \frac {1}{2} + \frac {1}{2} \left(1 - \mathrm {e} ^ {- 1}\right).</equation><equation>P \{X > 1, Z < 1 \} = P \{X > 1, X Y < 1 \} = P \left\{X > 1, Y < \frac {1}{X} \right\} = P \{X > 1, Y = - 1 \}</equation><equation>\stackrel {\text {独立 性}} {=} P \left\{X > 1 \right\} P \left\{Y = - 1 \right\} = \frac {1}{2} \mathrm {e} ^ {- 1}.</equation>由于<equation>\frac{1}{2}\mathrm{e}^{-1}\neq \mathrm{e}^{-1}\cdot \left[\frac{1}{2}+\frac{1}{2}\left(1-\mathrm{e}^{-1}\right)\right]</equation>，故X，Z不相互独立.

综上所述，X，Z不相互独立.

---

**2016年第22题 | 解答题 | 11分**
. (本题满分11分)

设二维随机变量 (X,Y)在区域 D = {(x,y) | 0 < x < 1,<equation>x^{2} < y < \sqrt{x}</equation>}上服从均匀分布，令<equation>U=\left\{\begin{array}{l l}1,&X\leqslant Y,\\ 0,&X>Y. \end{array} \right.</equation>I. 写出 (X,Y)的概率密度；

II. 问 U与 X是否相互独立？并说明理由；

III. 求 Z=U+X的分布函数 F(z).
**答案: **（I）<equation>f ( x,y)=\left\{\begin{array}{ll}3,&0<x<1,x^{2}<y<\sqrt{x},\\ 0,&\text{其他};\end{array}\right.</equation>（Ⅱ）U与X不相互独立；

（Ⅲ）<equation>F ( z )=\left\{\begin{array}{ll}0,&z<0,\\ \frac{3}{2} z^{2}-z^{3},&0\leqslant z<1,\\ 2 ( z-1 )^{\frac{3}{2}}-\frac{3}{2} z^{2}+3 z-1,&1\leqslant z<2,\\ 1,&z\geqslant 2.\end{array}\right.</equation>
**解析: **（I）区域D如图（a）所示，其面积为<equation>S = \int_ {0} ^ {1} \sqrt {x} \mathrm {d} x - \int_ {0} ^ {1} x ^ {2} \mathrm {d} x = \frac {2}{3} x ^ {\frac {3}{2}} \left| _ {0} ^ {1} - \frac {x ^ {3}}{3} \right| _ {0} ^ {1} = \frac {2}{3} - \frac {1}{3} = \frac {1}{3}.</equation>又由于<equation>(X, Y)</equation>在区域<equation>D</equation>上服从均匀分布，故<equation>(X, Y)</equation>的概率密度为<equation>f (x, y) = \left\{ \begin{array}{l l} 3, & 0 < x < 1, x ^ {2} < y < \sqrt {x}, \\ 0, & \text {其 他}. \end{array} \right.</equation>(a)

(b)

（Ⅱ）考虑<equation>P\{U = 0, X\leqslant t\}</equation><equation>P \{U = 0 \} = P \{X > Y \} = \iint f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {x ^ {2}} ^ {x} 3 \mathrm {d} y = \int_ {0} ^ {1} 3 \left(x - x ^ {2}\right) \mathrm {d} x = \frac {1}{2}.</equation>对<equation>t \leqslant 0</equation>，<equation>P\{X \leqslant t\} = 0</equation>，<equation>P\{U = 0, X \leqslant t\} = 0.</equation>于是，<equation>P \left\{U = 0, X \leqslant t \right\} = P \left\{U = 0 \right\} \cdot P \left\{X \leqslant t \right\}.</equation>对<equation>t \geqslant 1</equation>，<equation>P\{X \leqslant t\} = 1, P\{U = 0, X \leqslant t\} = P\{U = 0\}</equation>.于是，<equation>P \left\{U = 0, X \leqslant t \right\} = P \left\{U = 0 \right\} \cdot P \left\{X \leqslant t \right\}.</equation>对<equation>0 < t < 1</equation>，有效积分区域为图（b）中的蓝色区域.<equation>P \left\{U = 0, X \leqslant t \right\} = P \left\{X > Y, X \leqslant t \right\} = \int_ {0} ^ {t} \mathrm {d} x \int_ {x ^ {2}} ^ {x} 3 \mathrm {d} y = \int_ {0} ^ {t} 3 \left(x - x ^ {2}\right) \mathrm {d} x = \frac {3}{2} t ^ {2} - t ^ {3},</equation><equation>P \left\{X \leqslant t \right\} = \int_ {0} ^ {t} \mathrm {d} x \int_ {x ^ {2}} ^ {\sqrt {x}} 3 \mathrm {d} y = \int_ {0} ^ {t} 3 \left(\sqrt {x} - x ^ {2}\right) \mathrm {d} x = 2 t ^ {\frac {3}{2}} - t ^ {3}.</equation>于是，<equation>\begin{aligned} P \{U = 0, X \leqslant t \} - P \{U = 0 \} \cdot P \{X \leqslant t \} &= \frac {3}{2} t ^ {2} - t ^ {3} - \frac {1}{2} \left(2 t ^ {\frac {3}{2}} - t ^ {3}\right) \\ &= \frac {3}{2} t ^ {2} - \frac {1}{2} t ^ {3} - t ^ {\frac {3}{2}} \neq 0. (\mathrm {见 注} \textcircled{1}) \end{aligned}</equation>因此，当<equation>0 < t < 1</equation>时，U与X不相互独立.

（Ⅲ）由题设知，<equation>\begin{array}{l} F (z) = P \left\{Z \leqslant z \right\} = P \left\{U + X \leqslant z \right\} \\ = P \left\{U + X \leqslant z, U = 0 \right\} + P \left\{U + X \leqslant z, U = 1 \right\} \\ = P \left\{X \leqslant z, U = 0 \right\} + P \left\{X \leqslant z - 1, U = 1 \right\} \\ = P \left\{X \leqslant z, X > Y \right\} + P \left\{X \leqslant z - 1, X \leqslant Y \right\}. \\ \end{array}</equation>当<equation>z < 0</equation>时，<equation>z - 1 < 0</equation>，于是<equation>P\{X\leqslant z,X > Y\} = 0,P\{X\leqslant z - 1,X\leqslant Y\} = 0.</equation>从而<equation>F(z) = 0.</equation><equation>0 \leqslant z < 1</equation><equation>z - 1 < 0</equation><equation>P \left\{X \leqslant z - 1, X \leqslant Y \right\} = 0</equation><equation>F (z) = P \left\{X \leqslant z, X > Y \right\} = \int_ {0} ^ {z} \mathrm {d} x \int_ {x ^ {2}} ^ {x} 3 \mathrm {d} y = \int_ {0} ^ {z} 3 \left(x - x ^ {2}\right) \mathrm {d} x = \frac {3}{2} z ^ {2} - z ^ {3}.</equation>当<equation>1\leqslant z < 2</equation>时，<equation>0\leqslant z - 1 < 1</equation><equation>\begin{array}{l} F (z) = P \left\{X \leqslant z, X > Y \right\} + P \left\{X \leqslant z - 1, X \leqslant Y \right\} \\ = P \left\{X \leqslant 1, X > Y \right\} + P \left\{X \leqslant z - 1, X \leqslant Y \right\} \\ = \frac {1}{2} + \int_ {0} ^ {z - 1} \mathrm {d} x \int_ {x} ^ {\sqrt {x}} 3 \mathrm {d} y = \frac {1}{2} + \int_ {0} ^ {z - 1} 3 (\sqrt {x} - x) \mathrm {d} x \\ = \frac {1}{2} + 2 (z - 1) ^ {\frac {3}{2}} - \frac {3}{2} (z - 1) ^ {2} = 2 (z - 1) ^ {\frac {3}{2}} - \frac {3}{2} z ^ {2} + 3 z - 1. \\ \end{array}</equation>当<equation>z\geqslant 2</equation>时，<equation>z - 1\geqslant 1,F(z) = 1.</equation>综上所述，<equation>F (z) = \left\{ \begin{array}{ll} 0, & z < 0, \\ \frac{3}{2} z^{2} - z^{3}, & 0 \leqslant z < 1, \\ 2 (z - 1)^{\frac{3}{2}} - \frac{3}{2} z^{2} + 3 z - 1, & 1 \leqslant z < 2, \\ 1, & z \geqslant 2. \end{array} \right.</equation>

---

**2015年第14题 | 填空题 | 4分**
14. 设二维随机变量<equation>(X, Y)</equation>服从正态分布<equation>N(1, 0; 1, 1; 0)</equation>, 则<equation>P\{XY - Y < 0\} =</equation>___
**解析: **解 由题设知，X，Y不相关. 又由于（X，Y）服从正态分布，故X，Y相互独立. 从而<equation>\begin{aligned} P \{X Y - Y < 0 \} &= P \{(X - 1) Y < 0 \} = P \{X < 1, Y > 0 \} + P \{X > 1, Y < 0 \} \\ &= P \{X < 1 \} \cdot P \{Y > 0 \} + P \{X > 1 \} \cdot P \{Y < 0 \}. \end{aligned}</equation>由<equation>( X, Y ) \sim N ( 1, 0 ; 1, 1 ; 0 )</equation>可知，<equation>X\sim N ( 1, 1 )</equation><equation>Y\sim N ( 0, 1 )</equation>从而X，Y的概率密度的图形分别关于<equation>x=1</equation>，<equation>x=0</equation>对称，于是<equation>P \{ X < 1 \} = P \{ X > 1 \} = \frac{1}{2}</equation><equation>P \{ Y < 0 \} = P \{ Y > 0 \} = \frac{1}{2}.</equation>因此，<equation>P \left\{X Y - Y < 0 \right\} = \frac {1}{2} \times \frac {1}{2} + \frac {1}{2} \times \frac {1}{2} = \frac {1}{2}.</equation>

---

**2013年第22题 | 解答题 | 11分**
2. (本题满分11分)

设随机变量 X的概率密度为<equation>f ( x )=\left\{\begin{array}{ll}\frac{1}{9} x^{2},&0<x<3,\\ 0,&\text{其他}.\end{array} \right.</equation>令随机变量<equation>Y=\left\{\begin{array}{ll}2,&X\leqslant 1,\\ X,&1<X<2,\\ 1,&X\geqslant 2. \end{array} \right.</equation>I. 求 Y的分布函数；

II. 求概率<equation>P \{ X \leqslant Y \}</equation>
**答案: **(22) (I)<equation>F_{Y}(y)=\left\{ \begin{array}{ll}0,& y<1,\\ \frac{y^{3}+18}{27},& 1\leqslant y<2,\\ 1,& y\geqslant 2; \end{array} \right.</equation>（Ⅱ）<equation>\frac{8}{27}.</equation>
**解析: **解（I）记<equation>Y</equation>的分布函数为<equation>F_{Y}(y).</equation>由Y的定义知，<equation>P\{1\leqslant Y\leqslant 2\} = 1.</equation>当<equation>y < 1</equation>时，<equation>F_{Y}(y) = P\{Y\leqslant y\} = 0.</equation>当 1≤y<2时，<equation>\begin{aligned} F _ {Y} (y) &= P \{Y \leqslant y \} = P \{Y < 1 \} + P \{Y = 1 \} + P \{1 < Y \leqslant y \} \\ &= 0 + P \{X \geqslant 2 \} + P \{1 < X \leqslant y \} \\ &= \int_ {2} ^ {3} \frac {1}{9} x ^ {2} \mathrm {d} x + \int_ {1} ^ {y} \frac {1}{9} x ^ {2} \mathrm {d} x \\ &= \frac {1 9}{2 7} + \frac {y ^ {3} - 1}{2 7} = \frac {y ^ {3} + 1 8}{2 7}. \end{aligned}</equation>当<equation>y \geqslant 2</equation>时，<equation>F_{Y}(y) = P\{Y \leqslant y\} = 1.</equation>因此，<equation>Y</equation>的分布函数为<equation>F_{Y}(y) = \left\{ \begin{array}{ll}0, & y < 1,\\ \frac{y^{3} + 18}{27}, & 1\leqslant y < 2,\\ 1, & y\geqslant 2. \end{array} \right.</equation>（Ⅱ）（法一）由 Y的定义知，<equation>\begin{aligned} P \{X \leqslant Y \} &= P \{X < Y \} + P \{X = Y \} = P \{X \leqslant 1 \} + P \{1 < X < 2 \} \\ &= P \{X < 2 \} = \int_ {0} ^ {2} \frac {1}{9} x ^ {2} \mathrm {d} x = \frac {8}{2 7}. \end{aligned}</equation>（法二）<equation>P \{ X \leqslant Y \} = 1 - P \{ X > Y \} = 1 - P \{ X \geqslant 2 \} = P \{ X < 2 \} = \int_ {0} ^ {2} \frac {1}{9} x^{2} \mathrm {d} x = \frac {8}{2 7}.</equation>

---

**2012年第7题 | 选择题 | 4分 | 答案: A**
7. 设随机变量 X与 Y相互独立，且分别服从参数为1与参数为4的指数分布，则<equation>P\{X < Y\} =</equation>（    ）

A.<equation>\frac{1}{5}</equation>B.<equation>\frac{1}{3}</equation>C.<equation>\frac{2}{3}</equation>D.<equation>\frac{4}{5}</equation>
答案: A
**解析: **解 由题设知，<equation>f_{X}(x)=\left\{ \begin{array}{ll}\mathrm{e}^{-x},&x>0\\ 0,&x\leqslant 0, \end{array} \right. f_{Y}(y)=\left\{ \begin{array}{ll}4\mathrm{e}^{-4y},&y>0\\ 0,&y\leqslant 0. \end{array} \right.</equation>由于 X与Y相互独立，故 (X,Y）的概率密度为<equation>f (x, y) = f _ {X} (x) f _ {Y} (y) = \left\{ \begin{array}{l l} 4 \mathrm {e} ^ {- x - 4 y}, & x > 0, y > 0, \\ 0, & \text {其 他}. \end{array} \right.</equation>记<equation>D=\{(x,y)\mid x<y\}</equation>，则<equation>\begin{aligned} P \{X < Y \} &= \iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {+ \infty} \mathrm {d} y \int_ {0} ^ {y} 4 \mathrm {e} ^ {- x - 4 y} \mathrm {d} x = \int_ {0} ^ {+ \infty} 4 \mathrm {e} ^ {- 4 y} \left(1 - \mathrm {e} ^ {- y}\right) \mathrm {d} y \\ &= \int_ {0} ^ {+ \infty} \left(4 \mathrm {e} ^ {- 4 y} - 4 \mathrm {e} ^ {- 5 y}\right) \mathrm {d} y = 1 - \frac {4}{5} = \frac {1}{5}. \end{aligned}</equation>应选A.

---

**2009年第8题 | 选择题 | 4分 | 答案: B**
8. 设随机变量 X与 Y相互独立，且 X服从标准正态分布 N(0,1), Y的概率分布为<equation>P\{Y=0\}=P\{Y=1\}=\frac{1}{2}</equation>. 记<equation>F_{Z}(z)</equation>为随机变量 Z=XY的分布函数，则函数<equation>F_{Z}(z)</equation>的间断点个数为（    )

A.0 B.1 C.2 D.3
答案: B
**解析: **解 先用两种方法求<equation>F_{Z}(z).</equation>（法一）由定义知<equation>\begin{aligned} F _ {Z} (z) &= P \{Z \leqslant z \} = P \{X Y \leqslant z \} \\ &= P \{X Y \leqslant z, Y = 0 \} + P \{X Y \leqslant z, Y = 1 \} \\ &= P \{z \geqslant 0, Y = 0 \} + P \{X \leqslant z, Y = 1 \} \\ &= P \{z \geqslant 0, Y = 0 \} + P \{X \leqslant z \} \cdot P \{Y = 1 \} \quad (X \text {与} Y \text {相 互 独立}) \\ &= P \{z \geqslant 0, Y = 0 \} + \frac {1}{2} \Phi (z), \end{aligned}</equation>其中<equation>\varPhi (z)</equation>为标准正态分布函数.

当<equation>z < 0</equation>时，<equation>P\{z\geqslant 0, Y = 0\} = P(\varnothing) = 0</equation>，从而<equation>F_{Z}(z) = \frac{1}{2}\Phi (z).</equation>当<equation>z \geqslant 0</equation>时，<equation>P\{z \geqslant 0, Y = 0\} = P\{Y = 0\} = \frac{1}{2}</equation>，从而<equation>F_{Z}(z) = \frac{1}{2} +\frac{1}{2}\Phi (z).</equation>（法二）由全概率公式知<equation>\begin{array}{l} F _ {Z} (z) = P \{Z \leqslant z \} = P \{X Y \leqslant z \} \\ = P \left\{X Y \leqslant z \mid Y = 0 \right\} \cdot P \left\{Y = 0 \right\} + P \left\{X Y \leqslant z \mid Y = 1 \right\} \cdot P \left\{Y = 1 \right\} \\ = \frac {1}{2} P \left\{z \geqslant 0 \mid Y = 0 \right\} + \frac {1}{2} P \left\{X \leqslant z \mid Y = 1 \right\} \\ = \frac {1}{2} P \left\{z \geqslant 0 \right\} + \frac {1}{2} P \left\{X \leqslant z \right\} \quad (X \text {与} Y \text {相 互 独立}) \\ = \left\{ \begin{array}{l l} \frac {1}{2} \Phi (z), & z < 0, \\ \frac {1}{2} + \frac {1}{2} \Phi (z), & z \geqslant 0. \end{array} \right. \\ \end{array}</equation>由于<equation>\varPhi(z)</equation>连续，故<equation>F_{z}(z)</equation>仅在<equation>z = 0</equation>处间断，从而选B.

---


**2024年第22题 | 解答题 | 12分**


设总体 X服从<equation>[0,\theta]</equation>上的均匀分布，其中<equation>\theta\in(0,+\infty)</equation>为未知参数，<equation>X_{1},X_{2},\cdots,X_{n}</equation>为来自总体 X的简单随机样本.记<equation>X_{(n)}=\max\{X_{1},X_{2},\cdots,X_{n}\}, T_{c}=cX_{(n)}</equation>.

I. 求 c，使得<equation>T_{c}</equation>是<equation>\theta</equation>的无偏估计；

II. 记<equation>h(c)=E\left[ (T_{c}-\theta)^{2} \right]</equation>，求 c使得 h(c)最小.

**答案:**(1) 当<equation>c=\frac{n+1}{n}</equation>时，<equation>T_{c}</equation>是<equation>\theta</equation>的无偏估计.

(2) 当<equation>c=\frac{n+2}{n+1}</equation>时，h（c）最小.

**解析:**（I）由于<equation>X</equation>服从<equation>[0,\theta]</equation>上的均匀分布，故<equation>X</equation>的分布函数为<equation>F _ {X} (x) = \left\{ \begin{array}{l l} 0, & x < 0, \\ \frac {x}{\theta}, & 0 \leqslant x < \theta , \\ 1, & x \geqslant \theta . \end{array} \right.</equation>记随机变量<equation>Y = X_{(n)} = \max \left\{X_{1}, X_{2}, \dots, X_{n}\right\}</equation>. 计算<equation>Y</equation>的分布函数<equation>F_{Y}(y)</equation>.

当<equation>y < 0</equation>时，<equation>F_{Y}(y) = 0.</equation>当<equation>0\leqslant y < \theta</equation>时，<equation>\begin{array}{l} F _ {Y} (y) = P \left\{Y \leqslant y \right\} = P \left\{\max _ {1 \leqslant i \leqslant n} X _ {i} \leqslant y \right\} = P \left\{X _ {1} \leqslant y, X _ {2} \leqslant y, \dots , X _ {n} \leqslant y \right\} \\ \underline {{\text {独立 性}}} P \left\{X _ {1} \leqslant y \right\} P \left\{X _ {2} \leqslant y \right\} \dots P \left\{X _ {n} \leqslant y \right\} = F _ {X} ^ {n} (y) = \left(\frac {y}{\theta}\right) ^ {n}. \\ \end{array}</equation>当<equation>y\geqslant \theta</equation>时，<equation>F_{Y}(y) = 1.</equation>于是，<equation>F_{Y}(y) = \left\{ \begin{array}{ll}0, & y < 0,\\ \left(\frac{y}{\theta}\right)^{n}, & 0\leqslant y < \theta ,\\ 1, & y\geqslant \theta . \end{array} \right.</equation>对<equation>F_{Y}(y)</equation>求导，可得<equation>f _ {Y} (y) = F _ {Y} ^ {\prime} (y) = \left\{ \begin{array}{l l} \frac {n y ^ {n - 1}}{\theta^ {n}}, & 0 < y < \theta , \\ 0, & \text {其 他}. \end{array} \right.</equation>因此，<equation>\begin{aligned} E \left(T _ {c}\right) &= E (c Y) = c \int_ {- \infty} ^ {+ \infty} y \cdot f _ {Y} (y) \mathrm {d} y = c \int_ {0} ^ {\theta} y \cdot \frac {n y ^ {n - 1}}{\theta^ {n}} \mathrm {d} y = c \cdot \frac {n}{\theta^ {n}} \cdot \frac {y ^ {n + 1}}{n + 1} \Bigg | _ {0} ^ {\theta} \\ &= \frac {c n}{n + 1} \theta . \end{aligned}</equation>若<equation>T_{c}</equation>为<equation>\theta</equation>的无偏估计，则<equation>E\left(T_{c}\right)=\theta</equation>，从而<equation>\frac{cn}{n+1}\theta =\theta</equation>，解得<equation>c=\frac{n+1}{n}.</equation>（Ⅱ）展开 h(c）可得<equation>h (c) = E \left[ \left(T _ {c} - \theta\right) ^ {2} \right] = E \left[ \left(c Y - \theta\right) ^ {2} \right] = c ^ {2} E \left(Y ^ {2}\right) - 2 c \theta E (Y) + \theta^ {2}.</equation>计算<equation>E ( Y^{2})</equation><equation>E \left(Y ^ {2}\right) = \int_ {- \infty} ^ {+ \infty} y ^ {2} \cdot f _ {Y} (y) \mathrm {d} y = \int_ {0} ^ {\theta} y ^ {2} \cdot \frac {n y ^ {n - 1}}{\theta^ {n}} \mathrm {d} y = \frac {n}{\theta^ {n}} \cdot \frac {y ^ {n + 2}}{n + 2} \Bigg | _ {0} ^ {\theta} = \frac {n}{n + 2} \theta^ {2}.</equation>于是，<equation>h (c) = c ^ {2} \cdot \frac {n}{n + 2} \theta^ {2} - 2 c \cdot \frac {n}{n + 1} \theta^ {2} + \theta^ {2} = \left(\frac {n}{n + 2} c ^ {2} - \frac {2 n}{n + 1} c + 1\right) \theta^ {2}.</equation>令<equation>\frac{\mathrm{d}[h(c)]}{\mathrm{d}c}=\left(\frac{2n}{n+2} c-\frac{2n}{n+1}\right)\theta^{2}=0</equation>，解得<equation>c=\frac{n+2}{n+1}</equation>该点是h(c)的唯一驻点.又因为<equation>h^{\prime \prime}(c)</equation><equation>= \frac{2n}{n+2}\theta^{2} > 0</equation>，所以该唯一驻点是h(c)的极小值点，也是最小值点.

因此，当<equation>c=\frac{n+2}{n+1}</equation>时，h(c）最小.

---

**2023年第10题 | 选择题 | 5分 | 答案: A**

10. 设<equation>X_{1}, X_{2}</equation>为来自总体<equation>N\left(\mu ,\sigma^{2}\right)</equation>的简单随机样本，其中<equation>\sigma(\sigma>0)</equation>是未知参数.若<equation>\hat{\sigma}=a\left| X_{1}-X_{2}\right|</equation>为<equation>\sigma</equation>的无偏估计，则 a=（    ）

A.<equation>\frac{\sqrt{\pi}}{2}</equation>B.<equation>\frac{\sqrt{2\pi}}{2}</equation>C.<equation>\sqrt{\pi}</equation>D.<equation>\sqrt{2\pi}</equation>

答案: A

**解析:**解 由于<equation>X_{1}, X_{2}</equation>为来自总体<equation>N(\mu ,\sigma^{2})</equation>的简单随机样本，故<equation>X_{1}, X_{2}</equation>相互独立.

令<equation>Z = X_{1} - X_{2}</equation>，则<equation>Z\sim N(0,2\sigma^{2})</equation>，从而Z的概率密度<equation>f(z) = \frac{1}{\sqrt{2\pi}\cdot \sqrt{2}\sigma}\mathrm{e}^{-\frac{z^{2}}{4\sigma^{2}}}</equation>.<equation>\begin{aligned} E (\mid Z \mid) &= \int_ {- \infty} ^ {+ \infty} | z | f (z) \mathrm {d} z = 2 \int_ {0} ^ {+ \infty} \frac {1}{\sqrt {2 \pi} \cdot \sqrt {2} \sigma} \cdot z \mathrm {e} ^ {- \frac {z ^ {2}}{4 \sigma^ {2}}} \mathrm {d} z = \frac {1}{2 \sqrt {\pi} \sigma} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {z ^ {2}}{4 \sigma^ {2}}} \mathrm {d} \left(z ^ {2}\right) \\ &= \frac {1}{2 \sqrt {\pi} \sigma} \cdot \left(- 4 \sigma^ {2} \mathrm {e} ^ {- \frac {z ^ {2}}{4 \sigma^ {2}}}\right) \Big | _ {0} ^ {+ \infty} = \frac {2}{\sqrt {\pi}} \sigma . \end{aligned}</equation>由此可得<equation>E (\hat {\sigma}) = E \left(a \mid X _ {1} - X _ {2} \mid\right) = E \left(a \mid Z \mid\right) = \frac {2 a}{\sqrt {\pi}} \sigma .</equation>又因为<equation>\hat{\sigma}</equation>为<equation>\sigma</equation>的无偏估计，所以<equation>E(\hat{\sigma})=\sigma</equation>，即<equation>\frac{2a}{\sqrt{\pi}}\sigma=\sigma</equation>，解得 a<equation>=\frac{\sqrt{\pi}}{2}.</equation>因此，应选A.

---

**2021年第9题 | 选择题 | 5分 | 答案: C**

9. 设<equation>( X_{1}, Y_{1}), ( X_{2}, Y_{2}), \cdots, ( X_{n}, Y_{n} )</equation>为来自总体<equation>N (\mu_{1}, \mu_{2}; \sigma_{1}^{2}, \sigma_{2}^{2}; \rho)</equation>的简单随机样本，令<equation>\theta=\mu_{1}-\mu_{2}, \bar{X}=\frac{1}{n}\sum_{i=1}^{n} X_{i}, \bar{Y}=\frac{1}{n}\sum_{i=1}^{n} Y_{i}, \hat{\theta}=\bar{X}-\bar{Y}</equation>则（    )

A.<equation>\hat{\theta}</equation>是<equation>\theta</equation>的无偏估计，<equation>D(\hat{\theta})=\frac{\sigma_{1}^{2}+\sigma_{2}^{2}}{n}</equation>B.<equation>\hat{\theta}</equation>不是<equation>\theta</equation>的无偏估计，<equation>D(\hat{\theta})=\frac{\sigma_{1}^{2}+\sigma_{2}^{2}}{n}</equation>C.<equation>\hat{\theta}</equation>是<equation>\theta</equation>的无偏估计，<equation>D(\hat{\theta})=\frac{\sigma_{1}^{2}+\sigma_{2}^{2}-2\rho\sigma_{1}\sigma_{2}}{n}</equation>D.<equation>\hat{\theta}</equation>不是<equation>\theta</equation>的无偏估计，<equation>D(\hat{\theta})=\frac{\sigma_{1}^{2}+\sigma_{2}^{2}-2\rho\sigma_{1}\sigma_{2}}{n}</equation>

答案: C

**解析:**解 由于总体（X，Y）服从<equation>N(\mu_{1},\mu_{2};\sigma_{1}^{2},\sigma_{2}^{2};\rho)</equation>，故<equation>X\sim N(\mu_{1},\sigma_{1}^{2}),Y\sim N(\mu_{2},\sigma_{2}^{2})</equation>，从而<equation>\bar{X}\sim</equation><equation>N\left(\mu_{1},\frac{\sigma_{1}^{2}}{n}\right),\bar{Y}\sim N\left(\mu_{2},\frac{\sigma_{2}^{2}}{n}\right).</equation>计算<equation>E(\hat{\theta})</equation><equation>E (\hat {\theta}) = E (\bar {X} - \bar {Y}) = E (\bar {X}) - E (\bar {Y}) = \mu_ {1} - \mu_ {2} = \theta .</equation>因此，<equation>\hat{\theta}</equation>是<equation>\theta</equation>的无偏估计.

计算<equation>D(\hat{\theta})</equation><equation>D (\hat {\theta}) = D (\bar {X} - \bar {Y}) = D (\bar {X}) + D (\bar {Y}) - 2 \operatorname {C o v} (\bar {X}, \bar {Y}) = \frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{n} - 2 \operatorname {C o v} (\bar {X}, \bar {Y}).</equation>由于<equation>\left(X_{1},Y_{1}\right), \left(X_{2},Y_{2}\right),\dots ,\left(X_{n},Y_{n}\right)</equation>为简单随机样本，故它们相互独立，从而当<equation>i\neq j</equation>时，<equation>X_{i}</equation>与<equation>Y_{j}</equation>独立.于是，<equation>\operatorname{Cov}(X_{i},Y_{i})=\operatorname{Cov}(X,Y),\operatorname{Cov}(X_{i},Y_{j})=0(i\neq j).</equation><equation>\begin{aligned} \operatorname {C o v} (\bar {X}, \bar {Y}) &= \operatorname {C o v} \left(\frac {\sum_ {i = 1} ^ {n} X _ {i}}{n}, \frac {\sum_ {j = 1} ^ {n} Y _ {j}}{n}\right) = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \operatorname {C o v} \left(X _ {i}, Y _ {j}\right) = \frac {1}{n ^ {2}} \cdot \sum_ {i = 1} ^ {n} \operatorname {C o v} \left(X _ {i}, Y _ {i}\right) \\ &= \frac {1}{n ^ {2}} \cdot n \operatorname {C o v} (X, Y) = \frac {\operatorname {C o v} (X , Y)}{n}. \end{aligned}</equation>因此，<equation>D (\hat {\theta}) = \frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{n} - 2 \operatorname {C o v} (\bar {X}, \bar {Y}) = \frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{n} - \frac {2}{n} \operatorname {C o v} (X, Y) = \frac {\sigma_ {1} ^ {2} + \sigma_ {2} ^ {2} - 2 \rho \sigma_ {1} \sigma_ {2}}{n}.</equation>应选C.

---

**2016年第23题 | 解答题 | 11分**

3. (本题满分11分)

设总体 X的概率密度为<equation>f ( x; \theta) = \left\{ \begin{array}{l l} \frac{3 x^{2}}{\theta^{3}}, & 0 < x < \theta , \\ 0, & \mathrm {其 他}, \end{array} \right.</equation>其中<equation>\theta \in(0,+\infty)</equation>为未知参数，<equation>X_{1}, X_{2}, X_{3}</equation>为来自总体 X的简单随机样本，令<equation>T=\max \left\{X_{1}, X_{2}, X_{3}\right\}</equation>.

I. 求 T的概率密度；

II. 确定 a，使得 aT为<equation>\theta</equation>的无偏估计.

**答案:**<equation>(\mathrm {I}) f _ {T} (t) = \left\{ \begin{array}{l l} \frac {9 t ^ {8}}{\theta^ {9}}, & 0 < t < \theta , \\ 0, & \mathrm {其 他}; \end{array} \right. (\mathrm {I I}) a = \frac {1 0}{9}.</equation>

**解析:**解（I）设<equation>T</equation>的分布函数为<equation>F_{T}(t), T</equation>的概率密度为<equation>f_{T}(t).</equation>由于<equation>X_{1}, X_{2}, X_{3}</equation>为来自总体X的简单随机样本，故它们相互独立且与X同分布.从而<equation>\begin{array}{l} F _ {T} (t) = P \left\{T \leqslant t \right\} = P \left\{X _ {1} \leqslant t, X _ {2} \leqslant t, X _ {3} \leqslant t \right\} = P \left\{X _ {1} \leqslant t \right\} \cdot P \left\{X _ {2} \leqslant t \right\} \cdot P \left\{X _ {3} \leqslant t \right\} \\ = \left[ P \left\{X \leqslant t \right\} \right] ^ {3} = \left[ F _ {X} (t) \right] ^ {3}, \\ \end{array}</equation>其中<equation>F_{X}(t)</equation>为X的分布函数.

下面用两种方法求<equation>f_{T}(t)</equation>（法一）先求<equation>F_{T}(t)</equation>，再求导得到<equation>f_{T}(t)</equation>当<equation>t < 0</equation>时，<equation>F_{X}(t) = \int_{-\infty}^{t} f(x;\theta)\mathrm{d}x = 0.</equation>于是<equation>F_{T}(t) = [F_{X}(t)]^{3} = 0.</equation>当 0≤t <<equation>\theta</equation>时，<equation>F_{X}(t)=\int_{-\infty}^{t} f(x;\theta)\mathrm{d}x=\int_{0}^{t}\frac{3x^{2}}{\theta^{3}}\mathrm{d}x=\frac{t^{3}}{\theta^{3}}.</equation>于是<equation>F_{T}(t)=[F_{X}(t)]^{3}=\frac{t^{9}}{\theta^{9}}.</equation>当 t≥<equation>\theta</equation>时，<equation>F_{X}(t)=1.</equation>于是<equation>F_{T}(t)=[F_{X}(t)]^{3}=1.</equation>因此，<equation>F _ {T} (t) = \left\{ \begin{array}{l l} 0, & t < 0, \\ \frac {t ^ {9}}{\theta^ {9}}, & 0 \leqslant t < \theta , \\ 1, & t \geqslant \theta . \end{array} \right.</equation>综上所述，<equation>T</equation>的概率密度为<equation>f_{T}(t) = F_{T}^{\prime}(t) = \left\{ \begin{array}{ll} \frac{9t^{8}}{\theta^{9}}, & 0 < t < \theta , \\ 0, & \text{其他}. \end{array} \right.</equation>（法二）直接求导得到<equation>f_{T}(t)</equation>后再求解.<equation>f _ {T} (t) = F _ {T} ^ {\prime} (t) = 3 F _ {X} ^ {\prime} (t) \left[ F _ {X} (t) \right] ^ {2} = 3 f (t; \theta) \left[ F _ {X} (t) \right] ^ {2}.</equation>当<equation>t < 0</equation>时，<equation>f(t; \theta) = 0.</equation>于是<equation>f_{T}(t) = 0.</equation>当<equation>0 \leqslant t < \theta</equation>时，<equation>F_{X}(t) = \int_{-\infty}^{t} f(x; \theta)\mathrm{d}x = \int_{0}^{t} \frac{3x^{2}}{\theta^{3}}\mathrm{d}x = \frac{t^{3}}{\theta^{3}}.</equation>于是<equation>f _ {T} (t) = 3 f (t; \theta) \left[ F _ {X} (t) \right] ^ {2} = 3 \cdot \frac {3 t ^ {2}}{\theta^ {3}} \cdot \left(\frac {t ^ {3}}{\theta^ {3}}\right) ^ {2} = \frac {9 t ^ {8}}{\theta^ {9}}.</equation>当<equation>t \geqslant \theta</equation>时，<equation>f(t; \theta) = 0.</equation>于是<equation>f_{T}(t) = 0.</equation>综上所述，<equation>T</equation>的概率密度为<equation>f_{T}(t) = \left\{ \begin{array}{ll} \frac{9t^8}{\theta^9}, & 0 < t < \theta , \\ 0, & \text{其他}. \end{array} \right.</equation>（Ⅱ）由第（I）问中所求结果知，<equation>E (a T) = a E (T) = a \int_ {- \infty} ^ {+ \infty} t f _ {T} (t) \mathrm {d} t = a \int_ {0} ^ {\theta} \frac {9 t ^ {9}}{\theta^ {9}} \mathrm {d} t = \frac {9 a}{1 0 \theta^ {9}} t ^ {1 0} \Bigg | _ {0} ^ {\theta} = \frac {9}{1 0} a \theta .</equation>要使<equation>E(aT) = \theta</equation>，则<equation>\frac{9}{10} a\theta = \theta</equation>，解得<equation>a = \frac{10}{9}</equation>.

因此，当<equation>a=\frac{10}{9}</equation>时，<equation>aT</equation>为<equation>\theta</equation>的无偏估计.

---

**2014年第14题 | 填空题 | 4分**

14. 设总体 X的概率密度为 f(x;<equation>\theta)=\left\{\begin{array}{ll}\frac{2x}{3\theta^{2}},&\theta<x<2\theta,\\ 0,&\text{其他},\end{array} \right.</equation>其中<equation>\theta</equation>是未知参数，<equation>X_{1},X_{2},\cdots,X_{n}</equation>为来自总体 X的简单随机样本，若<equation>c\sum_{i=1}^{n}X_{i}^{2}</equation>是<equation>\theta^{2}</equation>的无偏估计，则 c=___

**解析:**由题设知，<equation>\theta^ {2} = E \left(c \sum_ {i = 1} ^ {n} X _ {i} ^ {2}\right) = n c E \left(X ^ {2}\right) = n c \int_ {\theta} ^ {2 \theta} x ^ {2} \cdot \frac {2 x}{3 \theta^ {2}} \mathrm {d} x = \frac {5}{2} \theta^ {2} n c,</equation>从而<equation>c = \frac{2}{5n}</equation>

---

**2010年第23题 | 解答题 | 11分**


设总体 X的概率分布为：

<table border="1"><tr><td>X</td><td>1</td><td>2</td><td>3</td></tr><tr><td>P</td><td>1-θ</td><td>θ-θ2</td><td>θ2</td></tr></table>

其中参数<equation>\theta \in (0,1)</equation>未知.以<equation>N_{i}</equation>表示来自总体<equation>X</equation>的简单随机样本（样本容量为<equation>n</equation>）中等于<equation>i</equation>的个数<equation>(i = 1,2,3)</equation>试求常数<equation>a_{1},a_{2},a_{3}</equation>，使<equation>T = \sum_{i = 1}^{3}a_{i}N_{i}</equation>为<equation>\theta</equation>的无偏估计量，并求<equation>T</equation>的方差.

**答案:**<equation>(2 3) a _ {1} = 0, a _ {2} = a _ {3} = \frac {1}{n}, D (T) = \frac {\theta (1 - \theta)}{n}.</equation>

**解析:**解 令<equation>T = \sum_{i = 1}^{3} a_{i} N_{i}</equation>为<equation>\theta</equation>的无偏估计量，则有<equation>\theta = E (T) = \sum_ {i = 1} ^ {3} a _ {i} E \left(N _ {i}\right).</equation>由<equation>N_{i}</equation>的定义知，<equation>N_{i}</equation>服从二项分布，即<equation>N_{1}\sim B(n,1 - \theta),N_{2}\sim B(n,\theta -\theta^{2}),N_{3}\sim B(n,\theta^{2})</equation>，从而<equation>E(N_{1}) = n(1 - \theta),E(N_{2}) = n(\theta -\theta^{2}),E(N_{3}) = n\theta^{2}</equation>.代入（1）式得<equation>\theta = a _ {1} n (1 - \theta) + a _ {2} n \left(\theta - \theta^ {2}\right) + a _ {3} n \theta^ {2},</equation>整理得<equation>0 = a _ {1} n + \left(a _ {2} n - a _ {1} n - 1\right) \theta + \left(a _ {3} n - a _ {2} n\right) \theta^ {2},</equation>从而<equation>a _ {1} n = 0, \quad a _ {2} n - a _ {1} n - 1 = 0, \quad a _ {3} n - a _ {2} n = 0,</equation>解得<equation>a_{1}=0,a_{2}=\frac{1}{n},a_{3}=\frac{1}{n}.</equation>又由<equation>N_{i}</equation>的定义知，<equation>N_{1}+N_{2}+N_{3}=n</equation>，故<equation>T = \sum_ {i = 1} ^ {3} a _ {i} N _ {i} = \frac {1}{n} \left(N _ {2} + N _ {3}\right) = \frac {1}{n} \left(n - N _ {1}\right) = 1 - \frac {1}{n} N _ {1},</equation>从而<equation>D (T) = D \left(1 - \frac {1}{n} N _ {1}\right) = \frac {1}{n ^ {2}} D \left(N _ {1}\right) = \frac {1}{n ^ {2}} \cdot n (1 - \theta) \theta = \frac {\theta (1 - \theta)}{n}.</equation>综上所述，<equation>a_{1}=0, a_{2}=\frac{1}{n}, a_{3}=\frac{1}{n}, D(T)=\frac{\theta(1-\theta)}{n}.</equation>

---

**2009年第14题 | 填空题 | 4分**

14. 设<equation>X_{1}, X_{2}, \cdots, X_{m}</equation>为来自二项分布总体<equation>B(n,p)</equation>的简单随机样本，<equation>\bar{X}</equation>和<equation>S^{2}</equation>分别为样本均值和样本方差，若<equation>\bar{X}+k S^{2}</equation>为<equation>n p^{2}</equation>的无偏估计量，则 k=___

**答案:**<equation>- 1.</equation>

**解析:**解 由题设知，<equation>n p^{2}=E(\overline{X}+k S^{2})=E(\overline{X})+k E(S^{2}).</equation>又<equation>E(\overline{X})=E(X)=np,</equation><equation>E(S^{2})=D(X)=np(1-p),</equation>故有<equation>n p^{2}=np+np(1-p)k</equation>，解得 k=-1.

---


**2014年第23题 | 解答题 | 11分**


23. (本题满分11分)

设总体 X的分布函数为<equation>F ( x ; \theta) = \left\{ \begin{array}{l l} 1 - \mathrm{e}^{- \frac {x^{2}}{\theta}}, & x \geqslant 0, \\ 0, & x < 0, \end{array} \right.</equation>其中<equation>\theta</equation>是未知参数且大于零.<equation>X_{1}, X_{2}, \dots , X_{n}</equation>为来自总体 X的简单随机样本.

I. 求<equation>E ( X )</equation>与<equation>E \left( X^{2} \right)</equation>II. 求<equation>\theta</equation>的最大似然估计量<equation>\hat{\theta}_{n}</equation>III. 是否存在实数 a，使得对任何<equation>\varepsilon > 0</equation>，都有<equation>\lim_{n \to \infty} P \{ | \hat{\theta}_{n}-a | \geqslant \varepsilon \}=0</equation>？

**答案:**(23) (I)<equation>E ( X )=\frac{\sqrt{\pi\theta}}{2}, E ( X^{2} )=\theta;</equation>(Ⅱ)<equation>\widehat{\theta}_n = \frac{1}{n}\sum_{i=1}^{n} X_i^2</equation>;

（Ⅲ）存在实数<equation>a = \theta</equation>，使得对任何<equation>\varepsilon > 0</equation>，都有<equation>\lim_{n\to \infty}P\{|\widehat{\theta}_n - a| \geqslant \varepsilon \} = 0.</equation>

**解析:**解（I）由题设知，X的概率密度<equation>f ( x ; \theta) = \left\{ \begin{array}{ll} \frac{2 x}{\theta} \mathrm{e}^{- \frac{x^{2}}{\theta}}, & x \geqslant 0, \\ 0, & x < 0, \end{array} \right.</equation>于是<equation>\begin{aligned} E (X) &= \int_ {0} ^ {+ \infty} x \cdot \frac {2 x}{\theta} \mathrm {e} ^ {- \frac {x ^ {2}}{\theta}} \mathrm {d} x = \int_ {0} ^ {+ \infty} x \mathrm {d} \left(- \mathrm {e} ^ {- \frac {x ^ {2}}{\theta}}\right) = - x \cdot \mathrm {e} ^ {- \frac {x ^ {2}}{\theta}} \Bigg | _ {0} ^ {+ \infty} + \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {x ^ {2}}{\theta}} \mathrm {d} x \\ &= 0 + \sqrt {\theta} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \left(\frac {x}{\sqrt {\theta}}\right) ^ {2}} \mathrm {d} \left(\frac {x}{\sqrt {\theta}}\right) \stackrel {t = \frac {x}{\sqrt {\theta}}} {=} \sqrt {\theta} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t \\ &= \sqrt {\theta} \cdot \frac {\sqrt {\pi}}{2} = \frac {\sqrt {\pi \theta}}{2}, \quad \text {这 里 利用 了 等 式} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t = \frac {\sqrt {\pi}}{2}. \end{aligned}</equation><equation>\begin{aligned} E \left(X ^ {2}\right) &= \int_ {0} ^ {+ \infty} x ^ {2} \cdot \frac {2 x}{\theta} \mathrm {e} ^ {- \frac {x ^ {2}}{\theta}} \mathrm {d} x = \theta \int_ {0} ^ {+ \infty} \frac {x ^ {2}}{\theta} \mathrm {e} ^ {- \frac {x ^ {2}}{\theta}} \mathrm {d} \left(\frac {x ^ {2}}{\theta}\right) \stackrel {u = \frac {x ^ {2}}{\theta}} {=} \theta \int_ {0} ^ {+ \infty} u \mathrm {e} ^ {- u} \mathrm {d} u \\ &= \theta \left(- u \mathrm {e} ^ {- u} \Big | _ {0} ^ {+ \infty} + \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- u} \mathrm {d} u\right) = \theta . \end{aligned}</equation>（Ⅱ）设<equation>x_{1}, x_{2}, \dots, x_{n}</equation>是来自于样本<equation>X_{1}, X_{2}, \dots, X_{n}</equation>的一个样本值，则似然函数为<equation>L (\theta) = \prod_ {i = 1} ^ {n} f \left(x _ {i}; \theta\right) = \left\{ \begin{array}{l l} \frac {2 ^ {n} x _ {1} x _ {2} \cdots x _ {n}}{\theta^ {n}} \mathrm {e} ^ {- \frac {x _ {1} ^ {2} + x _ {2} ^ {2} + \cdots + x _ {n} ^ {2}}{\theta}}, & x _ {1} \geqslant 0, x _ {2} \geqslant 0, \dots , x _ {n} \geqslant 0, \\ 0, & \text {其 他}. \end{array} \right.</equation>当<equation>x_{1} > 0,x_{2} > 0,\dots ,x_{n} > 0</equation>时，<equation>\ln L (\theta) = \ln \left(2 ^ {n} x _ {1} x _ {2} \dots x _ {n}\right) - n \ln \theta - \frac {x _ {1} ^ {2} + x _ {2} ^ {2} + \dots + x _ {n} ^ {2}}{\theta}.</equation>令<equation>\frac{\mathrm{d}\left[\ln L(\theta)\right]}{\mathrm{d}\theta}=0</equation>即有<equation>-\frac{n}{\theta}+\frac{x_{1}^{2}+x_{2}^{2}+\cdots+x_{n}^{2}}{\theta^{2}}=0</equation>解得<equation>\theta=\frac{x_{1}^{2}+x_{2}^{2}+\cdots+x_{n}^{2}}{n}</equation>，于是<equation>\theta</equation>的最大似然估计量为<equation>\widehat {\theta} _ {n} = \frac {X _ {1} ^ {2} + X _ {2} ^ {2} + \cdots + X _ {n} ^ {2}}{n} = \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} ^ {2}.</equation>（Ⅲ）由<equation>X_{1},X_{2},\dots ,X_{n}</equation>独立同分布知，<equation>X_{1}^{2},X_{2}^{2},\dots ,X_{n}^{2}</equation>独立同分布.又由（I）知，<equation>E\left(X_{i}^{2}\right) = E\left(X^{2}\right) = \theta</equation>，故由辛钦大数定律知，对任意<equation>\varepsilon >0</equation>，有<equation>\lim_{n\to \infty}P\left\{\left|\frac{1}{n}\sum_{i = 1}^{n}X_{i}^{2} - \theta\right| < \varepsilon\right\} = 1</equation>，从而<equation>\lim _ {n \rightarrow \infty} P \left\{\left| \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} ^ {2} - \theta \right| \geqslant \varepsilon \right\} = 0,</equation>即存在实数<equation>a = \theta</equation>，使得对任何<equation>\varepsilon > 0</equation>，都有<equation>\lim P\{ |\widehat{\theta}_n - a | \geqslant \varepsilon \} = 0.</equation>

---

**2020年第23题 | 解答题 | 11分**


设某元件的使用寿命<equation>T</equation>的分布函数为<equation>F (t) = \left\{ \begin{array}{l l} 1 - \mathrm {e} ^ {- \left(\frac {t}{\theta}\right) ^ {m}}, & t \geqslant 0 \\ 0, & \text {其 他} \end{array} \right.</equation>其中<equation>\theta, m</equation>为参数且大于零.

I. 求概率<equation>P\{T > t\}</equation>与<equation>P\{T > s + t \mid T > s\}</equation>，其中<equation>s > 0, t > 0</equation>.

II. 任取 n个这种元件做寿命试验，测得它们的寿命分别为<equation>t_{1}, t_{2}, \dots , t_{n}</equation>，若 m已知，求<equation>\theta</equation>的最大似然估计值<equation>\hat{\theta}.</equation>

**答案:**（I）<equation>P \left\{ T > t \right\} = \mathrm{e}^{-\left(\frac{t}{\theta}\right)^{m}}, P \left\{ T > s + t \mid T > s \right\} = \mathrm{e}^{\frac{s^{m} - (s + t)^{m}}{\theta^{m}}};</equation>（Ⅱ）<equation>\theta</equation>的最大似然估计值为<equation>\hat{\theta}=\sqrt[m]{\frac{1}{n}\sum_{i=1}^{n}t_{i}^{m}}.</equation>

**解析:**（I）由分布函数的定义以及<equation>s > 0,t > 0</equation>可得，<equation>P \left\{T > t \right\} = 1 - P \left\{T \leqslant t \right\} = 1 - F (t) = \mathrm {e} ^ {- \left(\frac {t}{\theta}\right) ^ {n}}.</equation><equation>P \left\{T > s + t \mid T > s \right\} = \frac {P \left\{T > s + t \right\}}{P \left\{T > s \right\}} = \frac {\mathrm {e} ^ {- \left(\frac {s + t}{\theta}\right) ^ {m}}}{\mathrm {e} ^ {- \left(\frac {s}{\theta}\right) ^ {m}}} = \mathrm {e} ^ {\frac {s ^ {m} - \left(s + t\right) ^ {m}}{\theta^ {m}}}.</equation>（Ⅱ）计算概率密度<equation>f ( t ; \theta)</equation><equation>f (t; \theta) = F ^ {\prime} (t; \theta) = \left\{ \begin{array}{l l} - \mathrm {e} ^ {- \left(\frac {t}{\theta}\right) ^ {m}} \cdot (- m) \cdot \left(\frac {t}{\theta}\right) ^ {m - 1} \cdot \frac {1}{\theta}, & t > 0, \\ 0, & \text {其 他} \end{array} = \left\{ \begin{array}{l l} \frac {m t ^ {m - 1}}{\theta^ {m}} \mathrm {e} ^ {- \left(\frac {t}{\theta}\right) ^ {m}}, & t > 0, \\ 0, & \text {其 他}. \end{array} \right. \right.</equation>似然函数<equation>L (\theta) = \prod_ {i = 1} ^ {n} f \left(t _ {i}; \theta\right) = \left\{ \begin{array}{l l} \left(t _ {1} t _ {2} \dots t _ {n}\right) ^ {m - 1} \cdot \left(\frac {m}{\theta^ {m}}\right) ^ {n} \cdot \mathrm {e} ^ {- \frac {1}{\theta^ {m}} \sum_ {i = 1} ^ {n} t _ {i} ^ {m}}, & t _ {i} > 0, i = 1, 2, \dots , n, \\ 0, & \text {其 他}. \end{array} \right.</equation>取对数得<equation>\ln L (\theta) = (m - 1) \ln \left(t _ {1} t _ {2} \dots t _ {n}\right) + n \left(\ln m - m \ln \theta\right) - \frac {1}{\theta^ {m}} \sum_ {i = 1} ^ {n} t _ {i} ^ {m}.</equation>令<equation>\frac{\mathrm{d}[\ln L(\theta)]}{\mathrm{d}\theta} = -\frac{mn}{\theta} + \frac{m}{\theta^{m + 1}}\sum_{i = 1}^{n}t_{i}^{m} = 0</equation>，可得<equation>mn\theta^{m} = m\sum_{i = 1}^{n}t_{i}^{m}</equation>. 从而<equation>\theta^{m} = \frac{1}{n}\sum_{i = 1}^{n}t_{i}^{m},\hat{\theta} = \sqrt[m]{\frac{1}{n}\sum_{i = 1}^{n}t_{i}^{m}}</equation>因此，<equation>\theta</equation>的最大似然估计值为<equation>\hat{\theta} = \sqrt[m]{\frac{1}{n}\sum_{i = 1}^{n}t_{i}^{m}}</equation>

---

**2019年第23题 | 解答题 | 11分**


设总体<equation>X</equation>的概率密度为<equation>f \left(x; \sigma^ {2}\right) = \left\{ \begin{array}{l l} \frac {A}{\sigma} \mathrm {e} ^ {- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}}, & x \geqslant \mu \\ 0, & x < \mu \end{array} \right.</equation>其中<equation>\mu</equation>是已知参数，<equation>\sigma > 0</equation>是未知参数，<equation>A</equation>是常数.<equation>X_{1}, X_{2}, \dots , X_{n}</equation>是来自总体<equation>X</equation>的简单随机样本.

I. 求 A；

II. 求<equation>\sigma^{2}</equation>的最大似然估计量.

**答案:**（ I ）<equation>A=\sqrt{\frac{2}{\pi}};</equation>（ II ）<equation>\sigma^{2}</equation>的最大似然估计量为<equation>\widehat{\sigma^{2}}=\frac{\sum_{i=1}^{n}\left(X_{i}-\mu\right)^{2}}{n}.</equation>

**解析:**解（I）利用<equation>\int_{- \infty}^{+ \infty} f ( x ; \sigma^{2} ) \mathrm{d} x=1</equation>来计算A.<equation>\begin{aligned} \int_ {- \infty} ^ {+ \infty} f (x; \sigma^ {2}) \mathrm {d} x &= \int_ {\mu} ^ {+ \infty} \frac {A}{\sigma} \mathrm {e} ^ {- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}} \mathrm {d} x \underline {{= t = x - \mu}} A \int_ {0} ^ {+ \infty} \frac {1}{\sigma} \mathrm {e} ^ {- \frac {t ^ {2}}{2 \sigma^ {2}}} \mathrm {d} t = A \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {1}{2} \cdot \left(\frac {t}{\sigma}\right) ^ {2}} \mathrm {d} \left(\frac {t}{\sigma}\right) \\ \frac {\frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \mathrm {d} x = 1}{\underline {{}}} A \cdot \frac {\sqrt {2 \pi}}{2} &= 1. \end{aligned}</equation>因此，<equation>A = \frac{2}{\sqrt{2\pi}} = \sqrt{\frac{2}{\pi}}.</equation>（Ⅱ）设<equation>x_{1}, x_{2}, \dots , x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots , X_{n}</equation>的一组样本值，则关于<equation>\sigma^2</equation>的似然函数为<equation>\begin{array}{l} L \left(\sigma^ {2}\right) = \prod_ {i = 1} ^ {n} f \left(x _ {i}; \sigma^ {2}\right) = \left\{ \begin{array}{l l} \prod_ {i = 1} ^ {n} \sqrt {\frac {2}{\pi}} \cdot \frac {1}{\sigma} \cdot \mathrm {e} ^ {- \frac {\left(x _ {i} - \mu\right) ^ {2}}{2 \sigma^ {2}}}, & x _ {1} \geqslant \mu , x _ {2} \geqslant \mu , \dots , x _ {n} \geqslant \mu , \\ 0, & \text {其 他} \end{array} \right. \\ = \left\{ \begin{array}{l l} \left(\frac {2}{\pi}\right) ^ {\frac {n}{2}} \cdot \left(\frac {1}{\sigma^ {2}}\right) ^ {\frac {n}{2}} \cdot \mathrm {e} ^ {- \frac {\sum_ {i = 1} ^ {n} \left(x _ {i} - \mu\right) ^ {2}}{2 \sigma^ {2}}}, & x _ {1} \geqslant \mu , x _ {2} \geqslant \mu , \dots , x _ {n} \geqslant \mu , \\ 0, & \text {其 他}. \end{array} \right. \\ \end{array}</equation>当<equation>x_{1}\geqslant \mu ,x_{2}\geqslant \mu ,\dots ,x_{n}\geqslant \mu</equation>时，<equation>\ln L \left(\sigma^ {2}\right) = \frac {n}{2} \ln \frac {2}{\pi} - \frac {n}{2} \ln \sigma^ {2} - \frac {\sum_ {i = 1} ^ {n} \left(x _ {i} - \mu\right) ^ {2}}{2 \sigma^ {2}}.</equation>令<equation>\frac{\mathrm{d}\left[\ln L\left(\sigma^2\right)\right]}{\mathrm{d}\left(\sigma^2\right)} = 0</equation>，即<equation>-\frac{n}{2}\cdot \frac{1}{\sigma^2} +\frac{\sum_{i=1}^{n}\left(x_{i} - \mu\right)^{2}}{2}\cdot \frac{1}{\sigma^{4}} = 0</equation>，解得<equation>\sigma^2 = \frac{\sum_{i=1}^{n}\left(x_{i} - \mu\right)^{2}}{n}</equation>因此，<equation>\sigma^2</equation>的最大似然估计量为<equation>\widehat {\sigma^ {2}} = \frac {\sum_ {i = 1} ^ {n} \left(X _ {i} - \mu\right) ^ {2}}{n}.</equation>

---

**2018年第23题 | 解答题 | 11分**


设总体<equation>X</equation>的概率密度为<equation>f (x; \sigma) = \frac {1}{2 \sigma} \mathrm {e} ^ {- \frac {| x |}{\sigma}}, - \infty < x < + \infty</equation><equation>\sigma \in (0, + \infty)</equation>为未知参数，<equation>X_{1}, X_{2}, \dots , X_{n}</equation>为来自总体<equation>X</equation>的简单随机样本.记<equation>\sigma</equation>的最大似然估计量为<equation>\hat{\sigma}</equation>.

I. 求<equation>\hat{\sigma}</equation>；

II. 求<equation>E(\hat{\sigma})</equation>和<equation>D(\hat{\sigma})</equation>

**答案:**（I）<equation>\sigma</equation>的最大似然估计量为<equation>\hat{\sigma}=\frac{\sum_{i=1}^{n} \mid X_{i}\mid}{n}；</equation>（Ⅱ）<equation>E(\hat{\sigma})=\sigma,D(\hat{\sigma})=\frac{\sigma^{2}}{n}.</equation>

**解析:**解（I）设<equation>x_{1}, x_{2}, \dots, x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots, X_{n}</equation>的一组样本值. 似然函数为<equation>L (\sigma) = \prod_ {i = 1} ^ {n} f \left(x _ {i}; \sigma\right) = \frac {1}{2 ^ {n} \sigma^ {n}} \mathrm {e} ^ {- \frac {\left| x _ {1} \right| + \left| x _ {2} \right| + \cdots + \left| x _ {n} \right|}{\sigma}}, - \infty < x _ {i} < + \infty , i = 1, 2, \dots , n.</equation>对 L （<equation>\sigma</equation>）取对数，得<equation>\ln L (\sigma) = - \frac {\sum_ {i = 1} ^ {n} \left| x _ {i} \right|}{\sigma} - n \ln (2 \sigma).</equation>令<equation>\frac{\mathrm{d}[\ln L(\sigma)]}{\mathrm{d}\sigma} = \frac{\sum_{i=1}^{n}|x_i|}{\sigma^2} - \frac{n}{\sigma} = 0</equation>，即<equation>\sum_{i=1}^{n}|x_i| - n\sigma = 0.</equation>解得<equation>\sigma = \frac{\sum_{i=1}^{n}|x_i|}{n}.</equation>因此，<equation>\sigma</equation>的最大似然估计量为<equation>\hat {\sigma} = \frac {\sum_ {i = 1} ^ {n} \left| X _ {i} \right|}{n}.</equation>（Ⅱ）由于<equation>X_{1}, X_{2}, \dots , X_{n}</equation>为来自总体X的简单随机样本，故它们相互独立，且与总体X同分布<equation>E \left( X_{i}\right) = E \left( X\right), E \left( \mid X_{i} \mid\right) = E \left( \mid X \mid\right), i = 1, 2, \dots , n.</equation>根据期望的线性性质，<equation>E \left(\hat {\sigma}\right) = E \left(\frac {\sum_ {i = 1} ^ {n} \left| X _ {i} \right|}{n}\right) = \frac {\sum_ {i = 1} ^ {n} E \left(\left| X _ {i} \right|\right)}{n} = \frac {n E \left(\left| X \right|\right)}{n} = E \left(\left| X \right|\right).</equation>根据期望的定义，<equation>\begin{aligned} E (\mid X \mid) &= \int_ {- \infty} ^ {+ \infty} | x | \cdot f (x; \sigma) \mathrm {d} x = \int_ {- \infty} ^ {+ \infty} | x | \cdot \frac {1}{2 \sigma} \mathrm {e} ^ {- \frac {| x |}{\sigma}} \mathrm {d} x = 2 \int_ {0} ^ {+ \infty} \frac {x}{2 \sigma} \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x \\ &= \frac {1}{\sigma} \int_ {0} ^ {+ \infty} x \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x = - \int_ {0} ^ {+ \infty} x \mathrm {d} \left(\mathrm {e} ^ {- \frac {x}{\sigma}}\right) = - \left(x \mathrm {e} ^ {- \frac {x}{\sigma}} \Big | _ {0} ^ {+ \infty} - \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x\right) \\ &= \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x = - \sigma \mathrm {e} ^ {- \frac {x}{\sigma}} \Big | _ {0} ^ {+ \infty} = \sigma . \end{aligned}</equation>因此，<equation>E(\hat{\sigma}) = \sigma.</equation>下面计算<equation>D(\hat{\sigma})</equation>由于<equation>X_{1}, X_{2}, \dots, X_{n}</equation>相互独立，且与总体<equation>X</equation>同分布，故<equation>D(\mid X_{i}\mid) = D(\mid X\mid)</equation>，<equation>i = 1, 2, \dots, n.</equation><equation>D (\hat {\sigma}) = D \left(\frac {\sum_ {i = 1} ^ {n} \left| X _ {i} \right|}{n}\right) = \frac {1}{n ^ {2}} D \left(\sum_ {i = 1} ^ {n} \left| X _ {i} \right|\right) = \frac {1}{n ^ {2}} \cdot n D (\left| X \right|) = \frac {D (\left| X \right|)}{n}.</equation>根据方差的计算公式，<equation>D (| X |) = E \left(| X | ^ {2}\right) - \left[ E \left(| X |\right) \right] ^ {2} = E \left(X ^ {2}\right) - \left[ E \left(| X |\right) \right] ^ {2}.</equation><equation>\begin{aligned} E \left(X ^ {2}\right) &= \int_ {- \infty} ^ {+ \infty} x ^ {2} \cdot f (x; \sigma) \mathrm {d} x = \int_ {- \infty} ^ {+ \infty} x ^ {2} \cdot \frac {1}{2 \sigma} \mathrm {e} ^ {- \frac {| x |}{\sigma}} \mathrm {d} x = \frac {1}{\sigma} \int_ {0} ^ {+ \infty} x ^ {2} \cdot \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x \\ &= - \int_ {0} ^ {+ \infty} x ^ {2} \mathrm {d} \left(\mathrm {e} ^ {- \frac {x}{\sigma}}\right) = - \left(x ^ {2} \mathrm {e} ^ {- \frac {x}{\sigma}} \Big | _ {0} ^ {+ \infty} - 2 \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {x}{\sigma}} \cdot x \mathrm {d} x\right) \\ &= 2 \int_ {0} ^ {+ \infty} x \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x \stackrel {*} {=} 2 \sigma^ {2}. \end{aligned}</equation>于是，<equation>D ( \mid X \mid ) = 2 \sigma^{2} - \sigma^{2} = \sigma^{2}.</equation>因此，<equation>D(\hat{\sigma}) = \frac{D(|X|)}{n} = \frac{\sigma^2}{n}.</equation>

---

**2017年第23题 | 解答题 | 11分**


某工程师为了解一台天平的精度，用该天平对一物体的质量做 n次测量，该物体的质量<equation>\mu</equation>是已知的.设 n次测量结果<equation>X_{1},X_{2},\cdots,X_{n}</equation>相互独立且均服从正态分布<equation>N\left(\mu ,\sigma^{2}\right)</equation>，该工程师记录的是 n次测量的绝对误差<equation>Z_{i}=\left|X_{i}-\mu\right|(i=1,2,\cdots,n).</equation>利用<equation>Z_{1},Z_{2},\cdots,Z_{n}</equation>估计<equation>\sigma.</equation>I. 求<equation>Z_{1}</equation>的概率密度；

II. 利用一阶矩求<equation>\sigma</equation>的矩估计量；

III. 求<equation>\sigma</equation>的最大似然估计量.

**答案:**( I )<equation>f_{Z_{1}}(z)=\left\{\begin{array}{ll}\sqrt{\frac{2}{\pi}}\frac{1}{\sigma}\mathrm{e}^{-\frac{z^{2}}{2\sigma^{2}}},&z\geqslant0,\\ 0,&z<0;\end{array}\right.</equation>( II )<equation>\hat{\sigma}=\sqrt{\frac{\pi}{2}}\bar{Z};</equation>( III )<equation>\hat{\sigma}=\sqrt{\frac{1}{n}\sum_{i=1}^{n}Z_{i}^{2}}.</equation>

**解析:**解（I）由题设知，<equation>X_{1}\sim N(\mu ,\sigma^{2})</equation>，从而<equation>\frac{X_{1}-\mu}{\sigma}\sim N(0,1).</equation>当 z < 0时，<equation>F_{Z_{1}}(z)=0.</equation>当<equation>z\geqslant 0</equation>时，<equation>\begin{array}{l} F _ {Z _ {1}} (z) = P \left\{Z _ {1} \leqslant z \right\} = P \left\{\left| X _ {1} - \mu \right| \leqslant z \right\} \\ = P \left\{\left| \frac {X _ {1} - \mu}{\sigma} \right| \leqslant \frac {z}{\sigma} \right\} = P \left\{- \frac {z}{\sigma} \leqslant \frac {X _ {1} - \mu}{\sigma} \leqslant \frac {z}{\sigma} \right\} \\ = 2 \Phi \left(\frac {z}{\sigma}\right) - 1, \\ \end{array}</equation>其中<equation>\varPhi(x)</equation>为标准正态分布函数.

于是，<equation>Z_{1}</equation>的分布函数为<equation>F_{Z_{1}}(z) = \left\{ \begin{array}{ll} 2\Phi \left(\frac{z}{\sigma}\right) - 1, & z\geqslant 0, \\ 0, & z < 0. \end{array} \right.</equation>因此，<equation>Z_{1}</equation>的概率密度为<equation>f _ {Z _ {1}} (z) = F _ {Z _ {1}} ^ {\prime} (z) = \left\{ \begin{array}{l l} \frac {2}{\sigma} \varphi \left(\frac {z}{\sigma}\right), & z \geqslant 0, \\ 0, & z < 0 \end{array} = \left\{ \begin{array}{l l} \sqrt {\frac {2}{\pi}} \frac {1}{\sigma} \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}}, & z \geqslant 0, \\ 0, & z < 0, \end{array} \right. \right.</equation>其中<equation>\varphi (x)</equation>为标准正态分布的概率密度.

（Ⅱ）由于<equation>\begin{aligned} E \left(Z _ {1}\right) &= \int_ {- \infty} ^ {+ \infty} z f _ {Z _ {1}} (z) \mathrm {d} z = \int_ {0} ^ {+ \infty} z \cdot \sqrt {\frac {2}{\pi}} \frac {1}{\sigma} \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}} \mathrm {d} z = \sqrt {\frac {2}{\pi}} \sigma \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}} \mathrm {d} \left(\frac {z ^ {2}}{2 \sigma^ {2}}\right) \\ &= - \sqrt {\frac {2}{\pi}} \sigma \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}} \Bigg | _ {0} ^ {+ \infty} = \sqrt {\frac {2}{\pi}} \sigma , \end{aligned}</equation>故<equation>\sigma = \sqrt{\frac{\pi}{2}} E\left(Z_{1}\right)</equation>. 用<equation>\overline{Z} = \frac{1}{n}\sum_{i=1}^{n} Z_{i}</equation>代替<equation>E\left(Z_{1}\right)</equation>，得到<equation>\sigma</equation>的矩估计量<equation>\hat {\sigma} = \sqrt {\frac {\pi}{2}} \bar {Z}.</equation>（Ⅲ）设<equation>z_{1}, z_{2}, \dots, z_{n}</equation>是相应于<equation>Z_{1}, Z_{2}, \dots, Z_{n}</equation>的一组样本值，则似然函数为<equation>L (\sigma) = L \left(z _ {1}, z _ {2}, \dots , z _ {n}; \sigma\right) = \prod_ {i = 1} ^ {n} f _ {Z _ {i}} \left(z _ {i}\right) = \left\{ \begin{array}{l l} \left(\frac {2}{\pi}\right) ^ {\frac {n}{2}} \frac {1}{\sigma^ {n}} \mathrm {e} ^ {- \frac {1}{2 \sigma^ {2}} \left(z _ {1} ^ {2} + z _ {2} ^ {2} + \dots + z _ {n} ^ {2}\right)}, & z _ {1} > 0, z _ {2} > 0, \dots , z _ {n} > 0, \\ 0, & \text {其 他}. \end{array} \right.</equation>当<equation>z_{1} > 0, z_{2} > 0, \dots, z_{n} > 0</equation>时，<equation>\ln L (\sigma) = \frac {n}{2} \ln \frac {2}{\pi} - n \ln \sigma - \frac {1}{2 \sigma^ {2}} \left(z _ {1} ^ {2} + z _ {2} ^ {2} + \dots + z _ {n} ^ {2}\right).</equation>令<equation>\frac{\mathrm{d}[\ln L(\sigma)]}{\mathrm{d}\sigma} = 0</equation>，即<equation>-\frac{n}{\sigma} +\frac{1}{\sigma^3}\left(z_1^2 +z_2^2 +\dots +z_n^2\right) = 0</equation>，解得<equation>\sigma = \sqrt{\frac{1}{n}\sum_{i=1}^{n}z_i^2}</equation>.

因此，<equation>\sigma</equation>的最大似然估计量为<equation>\hat {\sigma} = \sqrt {\frac {1}{n} \sum_ {i = 1} ^ {n} Z _ {i} ^ {2}}.</equation>

---

**2015年第23题 | 解答题 | 11分**


设总体<equation>X</equation>的概率密度为<equation>f (x; \theta) = \left\{ \begin{array}{l l} \frac {1}{1 - \theta}, & \theta \leqslant x \leqslant 1 \\ 0, & \text {其 他} \end{array} \right.</equation>其中<equation>\theta</equation>为未知参数.<equation>X_{1},X_{2},\cdots ,X_{n}</equation>为来自该总体的简单随机样本.

I. 求<equation>\theta</equation>的矩估计量;

II. 求<equation>\theta</equation>的最大似然估计量.

**答案:**<equation>\begin{aligned} 2 3) (\mathrm {I}) \hat {\theta} &= 2 \bar {X} - 1; \\ (\mathrm {I I}) \hat {\theta} &= \min _ {1 \leqslant i \leqslant n} X _ {i}. \end{aligned}</equation>

**解析:**（ I ）由于<equation>E (X) = \int_ {- \infty} ^ {+ \infty} x f (x; \theta) \mathrm {d} x = \int_ {\theta} ^ {1} \frac {x}{1 - \theta} \mathrm {d} x = \frac {1 + \theta}{2},</equation>故<equation>\theta = 2 E ( X ) - 1.</equation>用样本均值<equation>\bar{X}=\frac{1}{n}\sum_{i=1}^{n}X_{i}</equation>代替<equation>E ( X )</equation>，可得<equation>\theta</equation>的矩估计量<equation>\hat {\theta} = 2 \bar {X} - 1.</equation>（Ⅱ）设<equation>x_{1}, x_{2}, \dots, x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots, X_{n}</equation>的一组样本值，则似然函数为<equation>L (\theta) = \prod_ {i = 1} ^ {n} f \left(x _ {i}; \theta\right) = \left\{ \begin{array}{l l} \frac {1}{(1 - \theta) ^ {n}}, & \theta \leqslant x _ {1}, x _ {2}, \dots , x _ {n} \leqslant 1, \\ 0, & \text {其 他} \end{array} = \left\{ \begin{array}{l l} \frac {1}{(1 - \theta) ^ {n}}, & \theta \leqslant \min _ {1 \leqslant i \leqslant n} x _ {i}, \\ 0, & \text {其 他}. \end{array} \right. \right.</equation>又由于<equation>\frac{1}{(1-\theta)^{n}}</equation>是关于<equation>\theta</equation>的单调增加函数，故当<equation>\theta=\min_{1\leqslant i\leqslant n}x_{i}</equation>时，<equation>L(\theta)</equation>取值最大因此，<equation>\theta</equation>的最大似然估计量为<equation>\hat {\theta} = \min _ {1 \leqslant i \leqslant n} X _ {i}.</equation>

---

**2013年第23题 | 解答题 | 11分**

23. (本题满分11分)

设总体 X的概率密度为 f(x;<equation>\theta)=\left\{\begin{array}{ll}\frac{\theta^{2}}{x^{3}} \mathrm{e}^{-\frac{\theta}{x}},&x>0,\\ 0,&\mathrm{其他},\end{array} \right.</equation>其中<equation>\theta</equation>为未知参数且大于零.<equation>X_{1},X_{2},\cdots,X_{n}</equation>为来自总体 X的简单随机样本.

I. 求<equation>\theta</equation>的矩估计量;

II. 求<equation>\theta</equation>的最大似然估计量.

**答案:**(23) （ I ）<equation>\hat{\theta}=\overline{X};</equation>(Ⅱ)<equation>\hat{\theta}=\frac{2 n}{\sum_{i=1}^{n}\frac{1}{X_{i}}}.</equation>

**解析:**解（I）由题设知，<equation>\begin{aligned} E (X) &= \int_ {0} ^ {+ \infty} x \cdot \frac {\theta^ {2}}{x ^ {3}} \mathrm {e} ^ {- \frac {\theta}{x}} \mathrm {d} x = \int_ {0} ^ {+ \infty} \frac {\theta^ {2}}{x ^ {2}} \mathrm {e} ^ {- \frac {\theta}{x}} \mathrm {d} x = \int_ {0} ^ {+ \infty} \theta \mathrm {e} ^ {- \frac {\theta}{x}} \mathrm {d} \left(- \frac {\theta}{x}\right) \\ \underline {{\underline {{t}} = - \frac {\theta}{x}}} \int_ {- \infty} ^ {0} \theta \mathrm {e} ^ {t} \mathrm {d} t &= \theta \mathrm {e} ^ {t} \Big | _ {- \infty} ^ {0} = \theta , \end{aligned}</equation>即<equation>\theta = E(X)</equation>. 以<equation>\overline{X} = \frac{1}{n}\sum_{i=1}^{n} X_{i}</equation>代替<equation>E(X)</equation>, 得到<equation>\theta</equation>的矩估计量<equation>\hat{\theta} = \overline{X}</equation>.

（Ⅱ）设<equation>x_{1}, x_{2}, \dots, x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots, X_{n}</equation>的一组样本值，则关于<equation>\theta</equation>的似然函数为<equation>L (\theta) = \prod_ {i = 1} ^ {n} f \left(x _ {i}; \theta\right) = \left\{ \begin{array}{l l} \frac {\theta^ {2 n}}{\left(x _ {1} x _ {2} \cdots x _ {n}\right) ^ {3}} \mathrm {e} ^ {- \theta \left(\frac {1}{x _ {1}} + \frac {1}{x _ {2}} + \cdots + \frac {1}{x _ {n}}\right)}, & x _ {1} > 0, x _ {2} > 0, \dots , x _ {n} > 0, \\ 0, & \text {其 他}. \end{array} \right.</equation>当<equation>x_{1} > 0,x_{2} > 0,\dots ,x_{n} > 0</equation>时，<equation>\ln L (\theta) = 2 n \ln \theta - 3 \ln \left(x _ {1} x _ {2} \dots x _ {n}\right) - \theta \left(\frac {1}{x _ {1}} + \frac {1}{x _ {2}} + \dots + \frac {1}{x _ {n}}\right).</equation>令<equation>\frac{\mathrm{d}[\ln L(\theta)]}{\mathrm{d}\theta} = 0</equation>，即<equation>\frac{2n}{\theta} - \left(\frac{1}{x_1} + \frac{1}{x_2} + \dots + \frac{1}{x_n}\right) = 0</equation>，解得<equation>\theta = \frac{2n}{\frac{1}{x_1} + \frac{1}{x_2} + \dots + \frac{1}{x_n}}.</equation>因此，<equation>\theta</equation>的最大似然估计量为<equation>\hat {\theta} = \frac {2 n}{\frac {1}{X _ {1}} + \frac {1}{X _ {2}} + \cdots + \frac {1}{X _ {n}}} = \frac {2 n}{\sum_ {i = 1} ^ {n} \frac {1}{X _ {i}}}.</equation>

---

**2012年第23题 | 解答题 | 11分**


设随机变量 X与 Y相互独立且分别服从正态分布<equation>N\left(\mu,\sigma^{2}\right)</equation>与<equation>N\left(\mu,2\sigma^{2}\right)</equation>，其中<equation>\sigma</equation>是未知参数且<equation>\sigma >0</equation>记<equation>Z=X-Y.</equation>I. 求 Z的概率密度<equation>f\left(z;\sigma^{2}\right)</equation>；

II. 设<equation>Z_{1},Z_{2},\cdots,Z_{n}</equation>为来自总体 Z的简单随机样本，求<equation>\sigma^{2}</equation>的最大似然估计量<equation>\hat{\sigma}^{2}</equation>；

III. 证明<equation>\hat{\sigma}^{2}</equation>为<equation>\sigma^{2}</equation>的无偏估计量.

**答案:**(23) ( I )<equation>f ( z ; \sigma^{2} )=\frac{1}{\sqrt{6 \pi} \sigma}\mathrm{e}^{-\frac{z^{2}}{6 \sigma^{2}}},-\infty<z<+\infty;</equation>（Ⅱ）<equation>\widehat{\sigma^{2}}=\frac{1}{3n}\sum_{i=1}^{n}Z_{i}^{2};</equation>（Ⅲ）证明略.

**解析:**（I）由于相互独立且服从正态分布的随机变量的线性组合仍服从正态分布，且<equation>E (Z) = E (X) - E (Y) = \mu - \mu = 0,</equation><equation>D (Z) = D (X - Y) = D (X) + D (Y) = \sigma^ {2} + 2 \sigma^ {2} = 3 \sigma^ {2},</equation>故<equation>Z\sim N(0,3\sigma^{2})</equation>，从而Z的概率密度<equation>f \left(z; \sigma^ {2}\right) = \frac {1}{\sqrt {2 \pi} \sqrt {3 \sigma^ {2}}} \mathrm {e} ^ {- \frac {z ^ {2}}{2 \cdot 3 \sigma^ {2}}} = \frac {1}{\sqrt {6 \pi} \sigma} \mathrm {e} ^ {- \frac {z ^ {2}}{6 \sigma^ {2}}}, - \infty < z < + \infty .</equation>（Ⅱ）设<equation>z_{1}, z_{2}, \dots, z_{n}</equation>是来自于样本<equation>Z_{1}, Z_{2}, \dots, Z_{n}</equation>的一个样本值，则似然函数为<equation>L \left(\sigma^ {2}\right) = \prod_ {i = 1} ^ {n} f \left(z _ {i}; \sigma^ {2}\right) = (6 \pi) ^ {- \frac {n}{2}} \cdot \left(\sigma^ {2}\right) ^ {- \frac {n}{2}} \mathrm {e} ^ {- \frac {z _ {1} ^ {2} + z _ {2} ^ {2} + \cdots + z _ {n} ^ {2}}{6 \sigma^ {2}}}.</equation>取对数得<equation>\ln L \left(\sigma^ {2}\right) = - \frac {n}{2} \ln (6 \pi) - \frac {n}{2} \ln \sigma^ {2} - \frac {z _ {1} ^ {2} + z _ {2} ^ {2} + \cdots + z _ {n} ^ {2}}{6 \sigma^ {2}}.</equation>令<equation>\frac{\mathrm{d}\left[\ln L(\sigma^{2})\right]}{\mathrm{d}(\sigma^{2})}=0</equation>即有<equation>-\frac{n}{2\sigma^{2}}+\frac{z_{1}^{2}+z_{2}^{2}+\cdots+z_{n}^{2}}{6(\sigma^{2})^{2}}=0</equation>解得<equation>\sigma^{2}=\frac{z_{1}^{2}+z_{2}^{2}+\cdots+z_{n}^{2}}{3n}.</equation>于是<equation>\sigma^{2}</equation>的最大似然估计量为<equation>\widehat {\sigma^ {2}} = \frac {Z _ {1} ^ {2} + Z _ {2} ^ {2} + \cdots + Z _ {n} ^ {2}}{3 n} = \frac {1}{3 n} \sum_ {i = 1} ^ {n} Z _ {i} ^ {2}.</equation>（Ⅲ）由于<equation>E \left(\widehat {\sigma^ {2}}\right) = E \left(\frac {1}{3 n} \sum_ {i = 1} ^ {n} Z _ {i} ^ {2}\right) = \frac {1}{3} E \left(Z ^ {2}\right) = \frac {1}{3} \left[ D (Z) + \left(E (Z)\right) ^ {2} \right] = \frac {3 \sigma^ {2}}{3} = \sigma^ {2},</equation>故<equation>\widehat{\sigma^2}</equation>为<equation>\sigma^2</equation>的无偏估计量，结论得证.

---

**2011年第23题 | 解答题 | 11分**


设<equation>X_{1}, X_{2}, \dots, X_{n}</equation>为来自正态总体<equation>N\left(\mu_{0},\sigma^{2}\right)</equation>的简单随机样本，其中<equation>\mu_{0}</equation>已知，<equation>\sigma^{2}>0</equation>未知，<equation>\bar{X}</equation>和<equation>S^{2}</equation>分别表示样本均值和样本方差.

I. 求参数<equation>\sigma^{2}</equation>的最大似然估计<equation>\hat{\sigma}^{2}</equation>；

II. 计算<equation>E(\hat{\sigma}^{2})</equation>和<equation>D(\hat{\sigma}^{2})</equation>

**答案:**(23) (I)<equation>\hat{\sigma}^{2} = \frac{1}{n}\sum_{i=1}^{n}\left(X_{i} - \mu_{0}\right)^{2}</equation>;<equation>(\mathrm {I I}) E \left(\widehat {\sigma^ {2}}\right) = \sigma^ {2}, D \left(\widehat {\sigma^ {2}}\right) = \frac {2 \sigma^ {4}}{n}.</equation>

**解析:**解（I）设 X为正态总体，<equation>x_{1}, x_{2}, \dots , x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots , X_{n}</equation>的一个样本值.由<equation>X\sim N(\mu_{0},\sigma^{2})</equation>知，X的概率密度为<equation>f \left(x; \mu_ {0}, \sigma^ {2}\right) = \frac {1}{\sqrt {2 \pi} \sigma} \mathrm {e} ^ {- \frac {\left(x - \mu_ {0}\right) ^ {2}}{2 \sigma^ {2}}},</equation>从而似然函数为<equation>L \left(\sigma^ {2}\right) = \prod_ {i = 1} ^ {n} \frac {1}{\sqrt {2 \pi} \sigma} \mathrm {e} ^ {- \frac {\left(x _ {i} - \mu_ {0}\right) ^ {2}}{2 \sigma^ {2}}} = \left(2 \pi\right) ^ {- \frac {n}{2}} \left(\sigma^ {2}\right) ^ {- \frac {n}{2}} \mathrm {e} ^ {- \frac {1}{2 \sigma^ {2}} \sum_ {i = 1} ^ {n} \left(x _ {i} - \mu_ {0}\right) ^ {2}},</equation>两边取对数得<equation>\ln L \left(\sigma^ {2}\right) = - \frac {n}{2} \ln 2 \pi - \frac {n}{2} \ln \sigma^ {2} - \frac {1}{2 \sigma^ {2}} \sum_ {i = 1} ^ {n} \left(x _ {i} - \mu_ {0}\right) ^ {2}.</equation>令<equation>\frac{\mathrm{d}\left[\ln L\left(\sigma^{2}\right)\right]}{\mathrm{d}\left(\sigma^{2}\right)} = 0</equation>，即有<equation>-\frac{n}{2\sigma^2} +\frac{1}{2\left(\sigma^2\right)^2}\sum_{i=1}^{n}\left(x_{i} - \mu_{0}\right)^{2} = 0</equation>（注意这里是关于<equation>\sigma^2</equation>求导），解得<equation>\sigma^2 = \frac{1}{n}\sum_{i=1}^{n}\left(x_{i} - \mu_{0}\right)^{2}</equation>.于是参数<equation>\sigma^2</equation>的最大似然估计为<equation>\widehat {\sigma^ {2}} = \frac {1}{n} \sum_ {i = 1} ^ {n} \left(X _ {i} - \mu_ {0}\right) ^ {2}.</equation>（Ⅱ）（法一）由于<equation>X_{i}\sim N(\mu_{0},\sigma^{2})</equation>，故<equation>\frac{X_{i} - \mu_{0}}{\sigma}\sim N(0,1),i = 1,2,\dots,n</equation>，从而由（I）知，<equation>\frac {n \widehat {\sigma^ {2}}}{\sigma^ {2}} = \sum_ {i = 1} ^ {n} \frac {\left(X _ {i} - \mu_ {0}\right) ^ {2}}{\sigma^ {2}} \sim \chi^ {2} (n).</equation>于是<equation>E\left(\frac{n\widehat{\sigma}^{2}}{\sigma^{2}}\right)=n,D\left(\frac{n\widehat{\sigma}^{2}}{\sigma^{2}}\right)=2n</equation>，即有<equation>E \left(\widehat {\sigma^ {2}}\right) = \sigma^ {2}, \quad D \left(\widehat {\sigma^ {2}}\right) = \frac {2 \sigma^ {4}}{n}.</equation>（法二）由（I）知，<equation>E \left(\widehat {\sigma^ {2}}\right) = \frac {1}{n} \sum_ {i = 1} ^ {n} E \left[ \left(X _ {i} - \mu_ {0}\right) ^ {2} \right] = E \left[ \left(X - \mu_ {0}\right) ^ {2} \right] \xlongequal {\text {方 差 的 定 义}} D (X) = \sigma^ {2}.</equation>由于<equation>X_{1}, X_{2}, \dots, X_{n}</equation>相互独立，故<equation>(X_{1} - \mu_{0})^{2}, (X_{2} - \mu_{0})^{2}, \dots, (X_{n} - \mu_{0})^{2}</equation>相互独立，从而<equation>D \left(\widehat {\sigma^ {2}}\right) = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} D \left[ \left(X _ {i} - \mu_ {0}\right) ^ {2} \right] = \frac {1}{n} D \left[ \left(X - \mu_ {0}\right) ^ {2} \right].</equation>又<equation>X\sim N(\mu_{0},\sigma^{2})</equation>，故<equation>\frac{X-\mu_{0}}{\sigma}\sim N(0,1)</equation>，从而<equation>\frac{(X-\mu_{0})^{2}}{\sigma^{2}}\sim \chi^{2}(1),D\left[ \frac{(X-\mu_{0})^{2}}{\sigma^{2}}\right] = 2.</equation>于是<equation>D \left(\widehat {\sigma^ {2}}\right) = \frac {1}{n} D \left[ \left(X - \mu_ {0}\right) ^ {2} \right] = \frac {1}{n} \cdot 2 \sigma^ {4} = \frac {2 \sigma^ {4}}{n}.</equation>综上所述，<equation>E(\widehat{\sigma^{2}}) = \sigma^{2}, D(\widehat{\sigma^{2}}) = \frac{2\sigma^{4}}{n}.</equation>

---

**2009年第23题 | 解答题 | 11分**

23. (本题满分11分)

设总体 X的概率密度为<equation>f ( x )=\left\{\begin{array}{ll}\lambda^{2} x \mathrm{e}^{- \lambda x},&x>0,\\0,&\mathrm {其 他},\end{array} \right.</equation>其中参数<equation>\lambda(\lambda>0)</equation>未知，<equation>X_{1},X_{2},\cdots,X_{n}</equation>是来自总体 X的简单随机样本.

I. 求参数<equation>\lambda</equation>的矩估计量;

II. 求参数<equation>\lambda</equation>的最大似然估计量.

**答案:**(23) (I)<equation>\lambda</equation>的矩估计量为<equation>\hat{\lambda} = \frac{2}{\bar{X}}</equation>; (II)<equation>\lambda</equation>的最大似然估计量为<equation>\hat{\lambda} = \frac{2}{\bar{X}}</equation>.

**解析:**（I）由题设知，<equation>\begin{aligned} E (X) &= \int_ {0} ^ {+ \infty} \lambda^ {2} x ^ {2} \mathrm {e} ^ {- \lambda x} \mathrm {d} x \xlongequal {t = \lambda x} \frac {1}{\lambda} \int_ {0} ^ {+ \infty} t ^ {2} \mathrm {e} ^ {- t} \mathrm {d} t \\ &= \frac {1}{\lambda} \left(- \mathrm {e} ^ {- t} \cdot t ^ {2} \Big | _ {0} ^ {+ \infty} + \int_ {0} ^ {+ \infty} 2 t \mathrm {e} ^ {- t} \mathrm {d} t\right) = \frac {2}{\lambda} \int_ {0} ^ {+ \infty} t \mathrm {e} ^ {- t} \mathrm {d} t \\ &= \frac {2}{\lambda} \left(- \mathrm {e} ^ {- t} \cdot t \Big | _ {0} ^ {+ \infty} + \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- t} \mathrm {d} t\right) = \frac {2}{\lambda}. \end{aligned}</equation>于是<equation>\lambda = \frac{2}{E(X)}</equation>，用<equation>\overline{X} = \frac{1}{n}\sum_{i=1}^{n} X_{i}</equation>代替<equation>E(X)</equation>，得到参数<equation>\lambda</equation>的矩估计量为<equation>\hat {\lambda} = \frac {2}{\bar {X}}.</equation>（Ⅱ）设<equation>x_{1}, x_{2}, \dots, x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots, X_{n}</equation>的一个样本值，则似然函数为<equation>L (\lambda)=L \left(x_{1}, x_{2}, \dots, x_{n}; \lambda\right)=\prod_{i=1}^{n} f \left(x_{i}; \lambda\right)=\left\{ \begin{array}{l l} \lambda^{2 n} x_{1} x_{2} \dots x_{n} \mathrm{e}^{- \lambda \left(x_{1}+x_{2}+\dots+x_{n}\right)}, & x_{1}>0, x_{2}>0, \dots, x_{n}>0, \\ 0, & \text{其他}. \end{array} \right.</equation>当<equation>x_{1}>0, x_{2}>0, \dots, x_{n}>0</equation>时，<equation>\ln L (\lambda)=\ln \left(x_{1} x_{2} \dots x_{n}\right)+2 n \ln \lambda-\lambda \left(x_{1}+x_{2}+\dots+x_{n}\right).</equation><equation>\frac{\mathrm{d}[\ln L(\lambda)]}{\mathrm{d}\lambda}=0</equation>即<equation>\frac{2 n}{\lambda}-\left(x_{1}+x_{2}+\dots+x_{n}\right)=0</equation>解得<equation>\lambda=\frac{2 n}{x_{1}+x_{2}+\dots+x_{n}}.</equation>于是参数<equation>\lambda</equation>的最大似然估计量为<equation>\hat {\lambda} = \frac {2 n}{X _ {1} + X _ {2} + \cdots + X _ {n}} = \frac {2 n}{n \bar {X}} = \frac {2}{\bar {X}}.</equation>

---