#### 曲线的凹凸性、拐点及渐近线

**2025年第2题 | 选择题 | 5分 | 答案: B**

2. 已知函数<equation>f ( x )=\int_{0}^{x} \mathrm{e}^{t^{2}} \sin t \mathrm{d} t,g ( x )=\int_{0}^{x} \mathrm{e}^{t^{2}} \mathrm{d} t \cdot \sin^{2} x</equation>，则（    )

A. x=0是 f(x)的极值点，也是 g(x)的极值点

B. x=0是 f(x)的极值点，(0,0)是曲线 y=g(x)的拐点

C. x=0是 f(x)的极值点，(0,0)是曲线 y=f(x)的拐点

D. (0,0)是曲线 y=f(x)的拐点，(0,0)也是曲线 y=g(x)的拐点

答案: B

**解析:**解 先分析<equation>f(x)</equation>的性质，分别计算<equation>f^{\prime}(x)</equation>，<equation>f^{\prime \prime}(x)</equation>. 根据链式法则，<equation>f ^ {\prime} (x) = \sin x \mathrm {e} ^ {x ^ {2}},</equation><equation>f ^ {\prime \prime} (x) = 2 x \sin x \mathrm {e} ^ {x ^ {2}} + \cos x \mathrm {e} ^ {x ^ {2}} = \left(2 x \sin x + \cos x\right) \mathrm {e} ^ {x ^ {2}}.</equation>取<equation>\delta</equation>为充分小的正数，当<equation>x \in (-\delta, 0)</equation>时，<equation>f^{\prime}(x) < 0,f(x)</equation>单调减少，当<equation>x \in (0,\delta)</equation>时，<equation>f^{\prime}(x) > 0,f(x)</equation>单调增加.于是，<equation>x = 0</equation>是<equation>f(x)</equation>的极小值点.或者，也可以由<equation>f^{\prime}(0) = 0,f^{\prime \prime}(0) = 1 > 0</equation>以及极值的第二充分条件得到<equation>x = 0</equation>是<equation>f(x)</equation>的极小值点.

当<equation>x \in(-\delta ,\delta)</equation>时，<equation>x\sin x\geqslant0,\cos x > 0,f^{\prime \prime}(x)</equation>在<equation>(-\delta ,\delta)</equation>内恒大于0，<equation>y=f(x)</equation>是凹曲线.于是，点（0，0）不是曲线<equation>y=f(x)</equation>的拐点.

再分析<equation>g ( x )</equation>的性质，分别计算<equation>g^{\prime}(x), g^{\prime \prime}(x).</equation>根据链式法则，<equation>g ^ {\prime} (x) = \sin^ {2} x \mathrm {e} ^ {x ^ {2}} + 2 \sin x \cos x \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = \sin^ {2} x \mathrm {e} ^ {x ^ {2}} + \sin 2 x \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t,</equation><equation>\begin{aligned} g ^ {\prime \prime} (x) &= 2 \sin x \cos x \mathrm {e} ^ {x ^ {2}} + 2 x \sin^ {2} x \mathrm {e} ^ {x ^ {2}} + \sin 2 x \mathrm {e} ^ {x ^ {2}} + 2 \cos 2 x \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t \\ &= 2 \left(\sin 2 x + x \sin^ {2} x\right) \mathrm {e} ^ {x ^ {2}} + 2 \cos 2 x \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t. \end{aligned}</equation>取<equation>\delta</equation>为充分小的正数，由于<equation>\mathrm{e}^{t^2}</equation>恒大于0，故当<equation>x\in(-\delta,0)</equation>时，<equation>\int_0^x\mathrm{e}^{t^2}\mathrm{d}t < 0</equation>，结合<equation>\sin 2x < 0</equation>可得，<equation>g^{\prime}(x) > 0,g(x)</equation>单调增加，当<equation>x\in(0,\delta)</equation>时，<equation>\int_0^x\mathrm{e}^{t^2}\mathrm{d}t > 0</equation>，结合<equation>\sin 2x > 0</equation>可得，<equation>g^{\prime}(x) > 0,g(x)</equation>单调增加.于是，<equation>x = 0</equation>不是<equation>g(x)</equation>的极值点.

当<equation>x\in(-\delta ,0)</equation>时，<equation>\sin 2x + x\sin^2 x < 0,\int_0^x\mathrm{e}^{t^2}\mathrm{d}t < 0,\cos 2x > 0,g''(x) < 0,y = g(x)</equation>是凸曲线，当<equation>x\in(0,\delta)</equation>时，<equation>\sin 2x + x\sin^2 x > 0,\int_0^x\mathrm{e}^{t^2}\mathrm{d}t > 0,\cos 2x > 0,g''(x) > 0,y = g(x)</equation>是凹曲线.于是，点(0,0)是曲线<equation>y = g(x)</equation>的拐点.

综上所述，应选B.

---

**2025年第11题 | 填空题 | 5分**

11. 设<equation>g(x)</equation>是函数<equation>f(x)=\frac{1}{2}\ln \frac{3+x}{3-x}</equation>的反函数,则曲线<equation>y=g(x)</equation>的渐近线方程为___

**答案:**y=-3,y=3.

**解析:**解由<equation>y=f(x)=\frac{1}{2}\ln \frac{3+x}{3-x}</equation>可得<equation>\mathrm{e}^{2 y}=\frac{3+x}{3-x}.</equation>整理可得<equation>3(\mathrm{e}^{2 y}-1)=x(\mathrm{e}^{2 y}+1)</equation>解得 x=<equation>\frac{3(\mathrm{e}^{2 y}-1)}{\mathrm{e}^{2 y}+1}</equation>即<equation>f^{-1}(y)=\frac{3(\mathrm{e}^{2 y}-1)}{\mathrm{e}^{2 y}+1}</equation>令 g = f<equation>^{-1}</equation>，并将 y换成 x，可得 g(x)<equation>= \frac{3(\mathrm{e}^{2 x}-1)}{\mathrm{e}^{2 x}+1}.</equation>由于 g(x)是连续函数，故 y = g(x)没有铅直渐近线.

计算<equation>\lim_{x\to -\infty}g(x)</equation>，<equation>\lim_{x\to +\infty}g(x)</equation>可得<equation>\lim _ {x \rightarrow - \infty} g (x) = \lim _ {x \rightarrow - \infty} \frac {3 \left(\mathrm {e} ^ {2 x} - 1\right)}{\mathrm {e} ^ {2 x} + 1} = \frac {3 \cdot (0 - 1)}{0 + 1} = - 3,</equation><equation>\lim _ {x \rightarrow + \infty} g (x) = \lim _ {x \rightarrow + \infty} \frac {3 \left(\mathrm {e} ^ {2 x} - 1\right)}{\mathrm {e} ^ {2 x} + 1} = \lim _ {x \rightarrow + \infty} \frac {3 \left(1 - \mathrm {e} ^ {- 2 x}\right)}{1 + \mathrm {e} ^ {- 2 x}} = \frac {3 \cdot (1 - 0)}{1 + 0} = 3.</equation>因此，曲线 y=g(x)共有两条水平渐近线，y=3和y=-3.又因为曲线 y=g(x)已有两条不同的水平渐近线，所以曲线 y=g(x)没有斜渐近线.

---

**2019年第10题 | 填空题 | 4分**

10. 曲线<equation>y=x\sin x+2\cos x\left(-\frac{\pi}{2}<x<\frac{3\pi}{2}\right)</equation>的拐点坐标为 ___

**答案:**## (<equation>\pi</equation>, -2).

**解析:**解分别计算<equation>y^{\prime}(x), y^{\prime\prime}(x).</equation><equation>y ^ {\prime} (x) = x \cos x + \sin x - 2 \sin x = x \cos x - \sin x,</equation><equation>y ^ {\prime \prime} (x) = - x \sin x + \cos x - \cos x = - x \sin x.</equation>在区间<equation>\left(-\frac{\pi}{2},\frac{3\pi}{2}\right)</equation>内，仅有 x=0和 x=<equation>\pi</equation>满足<equation>y^{\prime\prime}(x)=0.</equation>下面用两种方法来判定拐点.

（法一）当<equation>-\frac{\pi}{2} < x < 0</equation>时，<equation>\sin x < 0</equation><equation>y^{\prime\prime}(x) < 0</equation>；当<equation>0 < x < \pi</equation>时，<equation>\sin x > 0</equation><equation>y^{\prime\prime}(x) < 0</equation>由于<equation>y^{\prime\prime}(x)</equation>在<equation>x=0</equation>处不变号，故曲线<equation>y=y(x)</equation>经过点（0，2）时，凹凸性没发生改变.点（0，2）不是<equation>y=y(x)</equation>的拐点.

当<equation>0 < x < \pi</equation>时，<equation>\sin x > 0</equation><equation>y^{\prime \prime}(x) < 0</equation>；当<equation>\pi < x < \frac{3\pi}{2}</equation>时，<equation>\sin x < 0</equation><equation>y^{\prime \prime}(x) > 0</equation>.由于<equation>y^{\prime \prime}(x)</equation>在<equation>x=\pi</equation>处变号，故曲线<equation>y=y(x)</equation>经过点（<equation>\pi,-2</equation>）时，凹凸性改变.点（<equation>\pi,-2</equation>）是<equation>y=y(x)</equation>的拐点.

（法二）计算<equation>y^{\prime \prime \prime}(x).</equation><equation>y ^ {\prime \prime \prime} (x) = - x \cos x - \sin x.</equation>当 x=0时，<equation>y^{\prime \prime \prime}(0)=0</equation>.此时不能确定点（0，2）是否为拐点.当 x=<equation>\pi</equation>时，<equation>y^{\prime \prime \prime}(\pi)=\pi</equation>.由拐点的充分条件可知，点（<equation>\pi,-2</equation>）是曲线 y=y(x)的拐点.

---

**2018年第2题 | 选择题 | 4分 | 答案: D**

2. 设函数 f(x)在[0,1]上二阶可导，且<equation>\int_{0}^{1} f(x)\mathrm{d}x=0</equation>，则（    )

A. 当<equation>f^{\prime}(x)<0</equation>时，<equation>f\left(\frac{1}{2}\right)<0</equation>B. 当<equation>f^{\prime\prime}(x)<0</equation>时，<equation>f\left(\frac{1}{2}\right)<0</equation>C. 当<equation>f^{\prime}(x)>0</equation>时，<equation>f\left(\frac{1}{2}\right)<0</equation>D. 当<equation>f^{\prime\prime}(x)>0</equation>时，<equation>f\left(\frac{1}{2}\right)<0</equation>

答案: D

**解析:**解（法一）考虑 f(x)在<equation>x=\frac{1}{2}</equation>处的带有拉格朗日余项的一阶泰勒公式.<equation>f (x) = f \left(\frac {1}{2}\right) + f ^ {\prime} \left(\frac {1}{2}\right) \left(x - \frac {1}{2}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {1}{2}\right) ^ {2},</equation>其中<equation>\xi_{x}</equation>介于x与<equation>\frac{1}{2}</equation>之间.<equation>\begin{aligned} \int_ {0} ^ {1} f (x) \mathrm {d} x &= \int_ {0} ^ {1} \left[ f \left(\frac {1}{2}\right) + f ^ {\prime} \left(\frac {1}{2}\right) \left(x - \frac {1}{2}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {1}{2}\right) ^ {2} \right] \mathrm {d} x \\ \underline {{\frac {\int_ {0} ^ {1} \left(x - \frac {1}{2}\right) \mathrm {d} x = 0}{\mathrm {一}}}} f \left(\frac {1}{2}\right) + \frac {1}{2} \int_ {0} ^ {1} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {1}{2}\right) ^ {2} \mathrm {d} x. \end{aligned}</equation>由于<equation>\int_{0}^{1} f(x)\mathrm{d}x=0</equation>，故<equation>f\left(\frac{1}{2}\right)=-\frac{1}{2}\int_{0}^{1} f^{\prime \prime}(\xi_{x})\left(x-\frac{1}{2}\right)^{2}\mathrm{d}x</equation>.当<equation>f^{\prime \prime}(x)>0</equation>时，<equation>\int_{0}^{1} f^{\prime \prime}(\xi_{x})\left(x-\frac{1}{2}\right)^{2}\mathrm{d}x > 0</equation>，于是，<equation>f\left(\frac{1}{2}\right)<0</equation>.同理可得，当<equation>f^{\prime \prime}(x)<0</equation>时，<equation>f\left(\frac{1}{2}\right)>0.</equation>因此，应选D.

下面说明选项A和选项C不正确.

选项A：考虑<equation>f ( x )=-x+\frac{1}{2}</equation>，则<equation>f^{\prime}(x)=-1<0</equation>且<equation>\int_{0}^{1} f(x)\mathrm{d}x=0</equation>，但<equation>f\left(\frac{1}{2}\right)=0.</equation>选项C：考虑<equation>f ( x )=x-\frac{1}{2}</equation>，则<equation>f^{\prime}(x)=1>0</equation>且<equation>\int_{0}^{1} f(x)\mathrm{d}x=0</equation>，但<equation>f\left(\frac{1}{2}\right)=0.</equation>（法二）记<equation>g ( x )=f^{\prime}\left(\frac{1}{2}\right)\left(x-\frac{1}{2}\right)+f\left(\frac{1}{2}\right)</equation>，则 y=g(x)为曲线 y=f(x)在点<equation>\left(\frac{1}{2},f\left(\frac{1}{2}\right)\right)</equation>处的切线.

如图所示，当<equation>f^{\prime \prime}(x) > 0</equation>时，由凹曲线的几何性质可知，曲线<equation>y=f(x)</equation>在点<equation>\left(\frac{1}{2}, f\left(\frac{1}{2}\right)\right)</equation>处的

切线<equation>y = g(x)</equation>位于<equation>y = f(x)</equation>之下，即<equation>g(x)\leqslant f(x)</equation>.

由于<equation>f^{\prime \prime}(x) > 0</equation>，故<equation>f(x)</equation>在[0,1]上不恒等于g(x)，从而由定积分的性质可知，<equation>0=\int_{0}^{1} f(x)\mathrm{d} x > \int_{0}^{1} g(x)\mathrm{d} x=\int_{0}^{1} f\left(\frac{1}{2}\right)\mathrm{d} x+\int_{0}^{1} f^{\prime}\left(\frac{1}{2}\right)\left(x-\frac{1}{2}\right)\mathrm{d} x=f\left(\frac{1}{2}\right).</equation>因此，<equation>f\left(\frac{1}{2}\right) < 0.</equation>应选D.

---

**2018年第9题 | 填空题 | 4分**

9. 曲线<equation>y=x^{2}+2 \ln x</equation>在其拐点处的切线方程是 ___

**答案:**# y=4x-3.

**解析:**解记<equation>f ( x )=x^{2}+2 \ln x</equation>，则<equation>f^{\prime}(x)=2 x+\frac{2}{x}, f^{\prime\prime}(x)=2-\frac{2}{x^{2}}.</equation>曲线<equation>y=f(x)</equation>的拐点<equation>\left(x_{0},f\left(x_{0}\right)\right)</equation>满足<equation>f^{\prime \prime}\left(x_{0}\right)=0</equation>解<equation>2-\frac{2}{x_{0}^{2}}=0</equation>得<equation>x_{0}=\pm 1.</equation>由于f(x)的自然定义域为<equation>\left(0,+\infty\right)</equation>，故<equation>x_{0}=1</equation>，拐点坐标为（1，1）.

又因为<equation>f^{\prime}(1)=\left. \left( 2 x+\frac{2}{x} \right) \right|_{x=1}=4</equation>，所以拐点（1，1）处的切线方程为 y-1=4(x-1)，即 y=4x-3.

---

**2016年第1题 | 选择题 | 4分 | 答案: B**

1. 设函数<equation>f ( x )</equation>在<equation>(-\infty, +\infty)</equation>内连续，其导函数的图形如图所示，则（    ）

A. 函数 f(x)有2个极值点，曲线 y=f(x)有2个拐点

B. 函数 f(x)有2个极值点，曲线 y=f(x)有3个拐点

C. 函数 f(x)有3个极值点，曲线 y=f(x)有1个拐点

D. 函数 f(x)有3个极值点，曲线 y=f(x)有2个拐点

答案: B

**解析:**解 观察图形，<equation>f(x)</equation>共有4个可能的极值点，从左至右依次记为<equation>x_{1},</equation><equation>x_{2}, x_{3}, x_{4}</equation>其中<equation>x_{2}</equation>为虚线与x轴的交点，其余三点为<equation>f^{\prime}(x)</equation>与x轴的交点.在<equation>x=x_{1}, x_{3}, x_{4}</equation>处，<equation>f^{\prime}(x)=0</equation>在<equation>x=x_{2}</equation>处，<equation>f(x)</equation>不可导.

分别考察<equation>x=x_{1}, x_{2}, x_{3}, x_{4}</equation>左、右两侧<equation>f^{\prime}(x)</equation>的符号.

- 当<equation>x < x_{1}</equation>时，<equation>f^{\prime}(x) > 0</equation>；当<equation>x_{1} < x < x_{2}</equation>时，<equation>f^{\prime}(x) < 0</equation>，故<equation>x=x_{1}</equation>是<equation>f(x)</equation>的极大值点.

- 当<equation>x_{1} < x < x_{2}</equation>时，<equation>f^{\prime}(x) < 0</equation>；当<equation>x_{2} < x < x_{3}</equation>时，<equation>f^{\prime}(x) < 0</equation>，故<equation>x = x_{2}</equation>不是<equation>f(x)</equation>的极值点.

- 当<equation>x_{2} < x < x_{3}</equation>时，<equation>f^{\prime}(x) < 0</equation>；当<equation>x_{3} < x < x_{4}</equation>时，<equation>f^{\prime}(x) > 0</equation>，故<equation>x = x_{3}</equation>是<equation>f(x)</equation>的极小值点.

- 当<equation>x_{3} < x < x_{4}</equation>时，<equation>f^{\prime}(x) > 0</equation>；当<equation>x > x_{4}</equation>时，<equation>f^{\prime}(x) > 0</equation>，故<equation>x = x_{4}</equation>不是<equation>f(x)</equation>的极值点.

因此，f（x）共有2个极值点.

曲线<equation>y=f(x)</equation>可能的拐点从左至右依次为<equation>\left(x_{2},f\left(x_{2}\right)\right),\left(x_{5},f\left(x_{5}\right)\right),\left(x_{4},f\left(x_{4}\right)\right)</equation>其中<equation>f^{\prime \prime}\left(x_{2}\right)</equation>不存在，<equation>f^{\prime \prime}\left(x_{5}\right)=f^{\prime \prime}\left(x_{4}\right)=0.</equation>- 当<equation>x<x_{2}</equation>时，<equation>f^{\prime}(x)</equation>单调减少；当<equation>x_{2}<x<x_{5}</equation>时，<equation>f^{\prime}(x)</equation>单调增加，故点（<equation>x_{2}, f(x_{2})</equation>）是曲线<equation>y=f(x)</equation>的拐点.

- 当<equation>x_{2} < x < x_{5}</equation>时，<equation>f^{\prime}(x)</equation>单调增加；当<equation>x_{5} < x < x_{4}</equation>时，<equation>f^{\prime}(x)</equation>单调减少，故点（<equation>x_{5}, f(x_{5})</equation>）是曲线<equation>y=f(x)</equation>的拐点.

- 当<equation>x_{5} < x < x_{4}</equation>时，<equation>f^{\prime}(x)</equation>单调减少；当<equation>x > x_{4}</equation>时，<equation>f^{\prime}(x)</equation>单调增加，故点（<equation>x_{4}, f(x_{4})</equation>）是曲线<equation>y=f(x)</equation>的拐点.

因此，曲线 y=f(x）共有3个拐点.

综上所述，应选B.

---

**2015年第2题 | 选择题 | 4分 | 答案: C**

2. 设函数 f(x)在<equation>(-\infty,+\infty)</equation>内连续，其2阶导函数<equation>f^{\prime\prime}(x)</equation>的图形如图所示，则曲线 y=f(x)的拐点个数为（    ）

A. 0 B. 1 C. 2 D. 3

答案: C

**解析:**由图可知，在<equation>(-\infty, +\infty)</equation>上，<equation>f^{\prime \prime}(x)=0</equation>有两个实根<equation>x_{1}, x_{2}</equation>，且<equation>f^{\prime \prime}(x)</equation>在 x=0处无定义.

下面我们分别讨论点<equation>\left(x_{1},f\left(x_{1}\right)\right),\left(0,f(0)\right)</equation>和<equation>\left(x_{2},f\left(x_{2}\right)\right)</equation>是否为拐点.

在<equation>x = x_{1}</equation>的左、右邻域内，<equation>f^{\prime \prime}(x)</equation>均大于零.<equation>f^{\prime \prime}(x)</equation>在该点两侧不变号，故点<equation>(x_{1}, f(x_{1}))</equation>不是曲线<equation>y = f(x)</equation>的拐点.

在<equation>x = 0</equation>的左侧邻域内，<equation>f^{\prime \prime}(x) > 0</equation>；在<equation>x = 0</equation>的右侧邻域内，<equation>f^{\prime \prime}(x) < 0</equation><equation>f^{\prime \prime}(x)</equation>在该点两侧变号，故点（0，<equation>f(0)</equation>）是曲线<equation>y = f(x)</equation>的拐点.

在<equation>x= x_{2}</equation>的左侧邻域内，<equation>f^{\prime \prime}(x)<0</equation>；在<equation>x= x_{2}</equation>的右侧邻域内，<equation>f^{\prime \prime}(x)>0. f^{\prime \prime}(x)</equation>在该点两侧变号，故点（<equation>x_{2}, f(x_{2})</equation>）是曲线<equation>y=f(x)</equation>的拐点.

综上所述，曲线<equation>y=f(x)</equation>共有2个拐点，应选C.

---

**2014年第2题 | 选择题 | 4分 | 答案: C**

2. 下列曲线中有渐近线的是（    ）

A. y=x+<equation>\sin x</equation>B. y=x²+<equation>\sin x</equation>C. y=x+<equation>\sin \frac{1}{x}</equation>D. y=x²+<equation>\sin \frac{1}{x}</equation>

答案: C

**解析:**解 先考察各曲线是否具有铅直渐近线.<equation>y = x + \sin x, y = x^{2} + \sin x</equation>在<equation>(-\infty , +\infty)</equation>上均无间断点，故不存在铅直渐近线；<equation>y = x + \sin \frac{1}{x}</equation>和<equation>y = x^{2} + \sin \frac{1}{x}</equation>在<equation>x = 0</equation>处无定义，但<equation>\lim_{x\to 0}\sin \frac{1}{x}</equation>不存在，从而也没有铅直渐近线.

再考察它们是否具有水平渐近线

由于选项A、B、C、D中的曲线在<equation>x\to +\infty</equation>和<equation>x\to -\infty</equation>时均趋于<equation>\infty</equation>，故它们均没有水平渐近线最后考察它们是否具有斜渐近线.

对选项C，<equation>\lim_{x\to \infty}\frac{x+\sin \frac{1}{x}}{x}=1</equation>，且<equation>\lim_{x\to \infty}\left(x+\sin \frac{1}{x}-x\right)=\lim_{x\to \infty}\sin \frac{1}{x}=0</equation>，故<equation>y=x+\sin \frac{1}{x}</equation>有斜渐近线<equation>y=x</equation>.应选C.

下面我们说明选项A、B、D没有斜渐近线.

对选项 A<equation>\lim_{x\to \infty}\frac{x+\sin x}{x}=1</equation>，但<equation>\lim_{x\to \infty}(x+\sin x-x)=\lim_{x\to \infty}\sin x</equation>不存在，故选项A没有斜渐近线

对选项 B，<equation>\lim_{x\to \infty}\frac{x^{2}+\sin x}{x}=\infty</equation>，对选项D，<equation>\lim_{x\to \infty}\frac{x^{2}+\sin \frac{1}{x}}{x}=\infty</equation>，故选项B和选项D都没有斜渐近线

---

**2014年第4题 | 选择题 | 4分 | 答案: D**

4. 设函数 f(x)具有2阶导数，<equation>g ( x )=f ( 0 ) ( 1-x )+f ( 1 ) x</equation>，则在区间[0,1]上（    )

A. 当<equation>f^{\prime}(x)\geqslant0</equation>时，<equation>f(x)\geqslant g(x)</equation>B. 当<equation>f^{\prime}(x)\geqslant0</equation>时，<equation>f(x)\leqslant g(x)</equation>C. 当<equation>f^{\prime\prime}(x)\geqslant0</equation>时，<equation>f(x)\geqslant g(x)</equation>D. 当<equation>f^{\prime\prime}(x)\geqslant0</equation>时，<equation>f(x)\leqslant g(x)</equation>

答案: D

**解析:**解 由于<equation>g ( x )=\frac{f ( 1 )-f ( 0 )}{1-0} x+f ( 0 )</equation><equation>g ( 0 )=f ( 0 )</equation><equation>g ( 1 )= f ( 1 )</equation>，故<equation>y=g ( x )</equation>表示的曲线是过点（0，f(0)），（1，f(1)）的弦由分析知，若<equation>y=f ( x )</equation>在[0,1]上凹，则<equation>f ( x ) \leqslant g ( x )</equation>；若<equation>y=f ( x )</equation>在[0,1]上凸，则<equation>f ( x ) \geqslant g ( x )</equation>.由于f(x)具有2阶导数，故曲线的凹凸性可以由<equation>f^{\prime \prime} ( x )</equation>确定.当<equation>f^{\prime \prime} ( x ) \geqslant 0</equation>时，<equation>y=f ( x )</equation>在[0,1]上凹，从而<equation>f ( x ) \leqslant g ( x )</equation>.应选D.

一阶导数的符号与曲线的凹凸性没有直接关系.作为选项A的反例，可以考虑曲线<equation>y=x^{2}</equation>；作为选项B的反例，可以考虑曲线<equation>y=\sqrt{x}.</equation>

---

**2012年第1题 | 选择题 | 4分 | 答案: C**

1. 曲线<equation>y=\frac{x^{2}+x}{x^{2}-1}</equation>的渐近线的条数为（    ）

A.0 B.1 C.2 D.3

答案: C

**解析:**解 先考虑间断点处的情况.<equation>y=\frac{x^{2}+x}{x^{2}-1}</equation>有间断点<equation>x=\pm 1.</equation>由于<equation>\lim_{x\rightarrow 1}\frac{x^{2}+x}{x^{2}-1}=\lim_{x\rightarrow 1}\frac{x}{x-1}=\infty</equation>，故曲线有铅直渐近线<equation>x=1.</equation>又由于<equation>\lim_{x\rightarrow -1}\frac{x^{2}+x}{x^{2}-1}=\lim_{x\rightarrow -1}\frac{x}{x-1}=\frac{1}{2}</equation>，故曲线在<equation>x=-1</equation>处没有渐近线.

再考虑无穷远处的情况.由于<equation>\lim_{x\rightarrow \infty}\frac{x^{2}+x}{x^{2}-1}=1</equation>，故曲线有水平渐近线<equation>y=1.</equation>综上所述，曲线共有两条渐近线.应选C.

---

**2010年第12题 | 填空题 | 4分**

12. 若曲线<equation>y=x^{3}+ax^{2}+bx+1</equation>有拐点<equation>(-1,0)</equation>, 则<equation>b=</equation>___

**解析:**解 由于点（-1，0）在曲线上，故<equation>0=-1+a-b+1=a-b</equation>即 a=b.又由拐点的必要条件知 (x)在 x=-1处的二阶导数必为零.于是<equation>y^{\prime \prime}(-1)=-6+2a=0</equation>即 a=3.因此，b=a=3.

---


