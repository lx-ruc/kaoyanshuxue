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
