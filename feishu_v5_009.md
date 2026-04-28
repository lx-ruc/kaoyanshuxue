---

**2020年第15题 | 解答题 | 10分**
15. (本题满分10分)

求曲线<equation>y=\frac{x^{1+x}}{(1+x)^{x}}(x>0)</equation>的斜渐近线方程.
**答案: **<equation>斜渐近线方程为 y = \frac {x}{\mathrm {e}} + \frac {1}{2 \mathrm {e}}.</equation>
**解析: **解 根据斜渐近线的定义，先计算<equation>\lim_{x\rightarrow +\infty}\frac{y}{x}.</equation><equation>\begin{aligned} \lim _ {x \rightarrow + \infty} \frac {y}{x} &= \lim _ {x \rightarrow + \infty} \frac {x ^ {x}}{(1 + x) ^ {x}} = \lim _ {x \rightarrow + \infty} \left(\frac {x}{1 + x}\right) ^ {x} = \lim _ {x \rightarrow + \infty} \left(1 - \frac {1}{1 + x}\right) ^ {x} \\ &= \lim _ {x \rightarrow + \infty} \left(1 - \frac {1}{1 + x}\right) ^ {- (1 + x) \cdot \frac {x}{- (1 + x)}} = e ^ {- \lim _ {x \rightarrow + \infty} \frac {x}{1 + x}} = e ^ {- 1}. \end{aligned}</equation>下面计算<equation>\lim_{x\to +\infty}\left(y - \frac{x}{\mathrm{e}}\right)</equation><equation>\lim _ {x \rightarrow + \infty} \left(y - \frac {x}{\mathrm {e}}\right) = \lim _ {x \rightarrow + \infty} x \left[\left(\frac {x}{1 + x}\right) ^ {x} - \frac {1}{\mathrm {e}} \right] = \lim _ {x \rightarrow + \infty} \frac {x}{\mathrm {e}} \left(\mathrm {e} ^ {x \ln \frac {x}{1 + x} + 1} - 1\right).</equation>由（1）式继续计算可得，<equation>\begin{aligned} \lim _ {x \rightarrow + \infty} \left(y - \frac {x}{e}\right) &= \lim _ {x \rightarrow + \infty} \frac {x}{e} \left(e ^ {x \ln \frac {x}{1 + x} + 1} - 1\right) \frac {e ^ {x \ln \frac {x}{1 + x} + 1} - 1 \sim x \ln \frac {x}{1 + x} + 1}{=} \lim _ {x \rightarrow + \infty} \frac {x}{e} \left(x \ln \frac {x}{1 + x} + 1\right) \\ &= \frac {1}{e} \lim _ {x \rightarrow + \infty} \left(x ^ {2} \ln \frac {x}{1 + x} + x\right) \frac {t = \frac {1}{x}}{=} \frac {1}{e} \lim _ {t \rightarrow 0 ^ {+}} \left(\frac {1}{t ^ {2}} \ln \frac {\frac {1}{t}}{1 + \frac {1}{t}} + \frac {1}{t}\right) \\ &= \frac {1}{e} \lim _ {t \rightarrow 0 ^ {+}} \frac {\ln \frac {1}{1 + t} + t}{t ^ {2}} \xlongequal {\text {洛必达}} \frac {1}{e} \lim _ {t \rightarrow 0 ^ {+}} \frac {- \frac {1}{1 + t} + 1}{2 t} = \frac {1}{e} \lim _ {t \rightarrow 0 ^ {+}} \frac {\frac {t}{1 + t}}{2 t} = \frac {1}{2 e}. \end{aligned}</equation>因此，所求斜渐近线方程为<equation>y=\frac{x}{e}+\frac{1}{2e}.</equation>如果不采用倒代换，也可以如下计算<equation>\lim_{x\to +\infty}\left(x^{2}\ln \frac{x}{1+x}+x\right).</equation>由<equation>\ln(1+u)=u-\frac{u^{2}}{2}+o(u^{2})</equation>可得，<equation>\ln \frac{x}{1+x}=\ln \left(1-\frac{1}{1+x}\right)=-\frac{1}{1+x}-\frac{1}{2(1+x)^{2}}+</equation>o<equation>\left[ \frac{1}{(1+x)^{2}} \right].</equation>.于是，<equation>\begin{array}{l} \lim _ {x \rightarrow + \infty} \left(x ^ {2} \ln \frac {x}{1 + x} + x\right) = \lim _ {x \rightarrow + \infty} \left\{- \frac {x ^ {2}}{1 + x} - \frac {x ^ {2}}{2 (1 + x) ^ {2}} + \frac {x (1 + x)}{1 + x} + o \left[ \frac {x ^ {2}}{(1 + x) ^ {2}} \right]\right\} \\ = \lim _ {x \rightarrow + \infty} \left[ \frac {x}{1 + x} - \frac {x ^ {2}}{2 (1 + x) ^ {2}} \right] = 1 - \frac {1}{2} = \frac {1}{2}. \\ \end{array}</equation>

---

**2019年第2题 | 选择题 | 4分 | 答案: B**
2. 曲线<equation>y=x\sin x+2\cos x\left(-\frac{\pi}{2}<x<2\pi\right)</equation>的拐点坐标为（    )

A. (0,2) B.<equation>(\pi,-2)</equation>C.<equation>\left(\frac{\pi}{2},\frac{\pi}{2}\right)</equation>D.<equation>\left(\frac{3\pi}{2},-\frac{3\pi}{2}\right)</equation>
答案: B
**解析: **解分别计算<equation>y^{\prime}(x), y^{\prime \prime}(x).</equation><equation>y ^ {\prime} (x) = x \cos x + \sin x - 2 \sin x = x \cos x - \sin x,</equation><equation>y ^ {\prime \prime} (x) = - x \sin x + \cos x - \cos x = - x \sin x.</equation>在区间<equation>\left(-\frac{\pi}{2}, 2\pi\right)</equation>内，仅有 x=0和 x=<equation>\pi</equation>满足<equation>y^{\prime\prime}(x)=0</equation>.于是，可以排除选项C和选项D.

下面用两种方法来判定选项A和选项B的正确性.

（法一）当<equation>-\frac{\pi}{2} < x < 0</equation>时，<equation>\sin x < 0</equation><equation>y^{\prime\prime}(x) < 0</equation>；当<equation>0 < x < \pi</equation>时，<equation>\sin x > 0</equation><equation>y^{\prime\prime}(x) < 0</equation>由于<equation>y^{\prime\prime}(x)</equation>在 x=0处不变号，故曲线<equation>y=y(x)</equation>经过点（0，2）时，凹凸性没发生改变.点（0，2）不是<equation>y=y(x)</equation>的拐点.选项A不正确.

当 0 < x <<equation>\pi</equation>时，<equation>\sin x > 0</equation><equation>y^{\prime\prime}(x) < 0</equation><equation>\pi < x < 2\pi</equation>时，<equation>\sin x < 0</equation><equation>y^{\prime\prime}(x) > 0</equation>.由于<equation>y^{\prime\prime}(x)</equation>在<equation>x=\pi</equation>处变号，故曲线<equation>y=y(x)</equation>经过点（<equation>\pi,-2</equation>）时，凹凸性改变.点（<equation>\pi,-2</equation>）是<equation>y=y(x)</equation>的拐点.

（法二）计算<equation>y^{\prime \prime \prime}(x).</equation><equation>y ^ {\prime \prime \prime} (x) = - x \cos x - \sin x.</equation>当 x=0时，<equation>y^{\prime \prime \prime}(0)=0</equation>.此时不能确定点（0，2）是否为拐点.当 x=<equation>\pi</equation>时，<equation>y^{\prime \prime \prime}(\pi)=\pi</equation>.由拐点的充分条件可知，点（<equation>\pi,-2</equation>）是曲线 y=y（x）的拐点.

因此，应选B.

---

**2018年第4题 | 选择题 | 4分 | 答案: D**
4. 设函数 f(x)在[0,1]上二阶可导，且<equation>\int_{0}^{1} f(x)\mathrm{d}x=0</equation>，则（    )

A. 当<equation>f^{\prime}(x)<0</equation>时，<equation>f\left(\frac{1}{2}\right)<0</equation>B. 当<equation>f^{\prime\prime}(x)<0</equation>时，<equation>f\left(\frac{1}{2}\right)<0</equation>C. 当<equation>f^{\prime}(x)>0</equation>时，<equation>f\left(\frac{1}{2}\right)<0</equation>D. 当<equation>f^{\prime\prime}(x)>0</equation>时，<equation>f\left(\frac{1}{2}\right)<0</equation>
答案: D
**解析: **解（法一）考虑 f(x)在<equation>x=\frac{1}{2}</equation>处的带有拉格朗日余项的一阶泰勒公式.<equation>f (x) = f \left(\frac {1}{2}\right) + f ^ {\prime} \left(\frac {1}{2}\right) \left(x - \frac {1}{2}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {1}{2}\right) ^ {2},</equation>其中<equation>\xi_{x}</equation>介于x与<equation>\frac{1}{2}</equation>之间.<equation>\begin{aligned} \int_ {0} ^ {1} f (x) \mathrm {d} x &= \int_ {0} ^ {1} \left[ f \left(\frac {1}{2}\right) + f ^ {\prime} \left(\frac {1}{2}\right) \left(x - \frac {1}{2}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {1}{2}\right) ^ {2} \right] \mathrm {d} x \\ \frac {\int_ {0} ^ {1} \left(x - \frac {1}{2}\right) \mathrm {d} x = 0}{\underline {{}}} f \left(\frac {1}{2}\right) + \frac {1}{2} \int_ {0} ^ {1} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {1}{2}\right) ^ {2} \mathrm {d} x. \end{aligned}</equation>由于<equation>\int_{0}^{1} f(x)\mathrm{d}x=0</equation>，故<equation>f\left(\frac{1}{2}\right)=0-\frac{1}{2}\int_{0}^{1} f^{\prime \prime}(\xi_{x})\left(x-\frac{1}{2}\right)^{2}\mathrm{d}x</equation>.当<equation>f^{\prime \prime}(x) > 0</equation>时，<equation>\int_{0}^{1} f^{\prime \prime}(\xi_{x})\left(x-\frac{1}{2}\right)^{2}\mathrm{d}x></equation>0，于是，<equation>f\left(\frac{1}{2}\right)<0</equation>.同理可得，当<equation>f^{\prime \prime}(x)<0</equation>时，<equation>f\left(\frac{1}{2}\right)>0.</equation>因此，应选D.

下面说明选项A和选项C不正确.

选项A：考虑<equation>f(x)=-x+\frac{1}{2}</equation>，则<equation>f^{\prime}(x)=-1<0</equation>且<equation>\int_{0}^{1} f(x)\mathrm{d}x=0</equation>，但<equation>f\left(\frac{1}{2}\right)=0.</equation>选项C：考虑<equation>f ( x )=x-\frac{1}{2}</equation>，则<equation>f^{\prime}(x)=1>0</equation>且<equation>\int_{0}^{1} f(x)\mathrm{d}x=0</equation>，但<equation>f\left(\frac{1}{2}\right)=0.</equation>（法二）记<equation>g ( x )=f^{\prime}\left(\frac{1}{2}\right)\left(x-\frac{1}{2}\right)+f\left(\frac{1}{2}\right)</equation>，则 y = g ( x ) 为曲线 y = f ( x ) 在点<equation>\left(\frac{1}{2}, f\left(\frac{1}{2}\right)\right)</equation>处的切线.

如图所示，当<equation>f^{\prime \prime}(x) > 0</equation>时，由凹曲线的几何性质可知，曲线<equation>y=f(x)</equation>在点<equation>\left(\frac{1}{2}, f\left(\frac{1}{2}\right)\right)</equation>处的切线<equation>y=g(x)</equation>位于<equation>y=f(x)</equation>之下，即<equation>g(x)\leqslant f(x).</equation>由于<equation>f^{\prime \prime}(x) > 0</equation>，故 f(x)在[0,1]上不恒等于 g(x)，从而由定积分的性质可知，<equation>0=\int_{0}^{1} f(x)\mathrm{d} x>\int_{0}^{1} g(x)\mathrm{d} x=\int_{0}^{1} f\left(\frac{1}{2}\right)\mathrm{d} x+\int_{0}^{1} f^{\prime}\left(\frac{1}{2}\right)\left(x-\frac{1}{2}\right)\mathrm{d} x=f\left(\frac{1}{2}\right).</equation>因此，<equation>f\left(\frac{1}{2}\right)<0</equation>应选D.

---

**2018年第10题 | 填空题 | 4分**
10. 曲线<equation>y=x^{2}+2\ln x</equation>在其拐点处的切线方程是 ___
**答案: **<equation>y = 4 x - 3.</equation>
**解析: **解记<equation>f ( x )=x^{2}+2 \ln x</equation>，则<equation>f^{\prime}(x)=2 x+\frac{2}{x}, f^{\prime\prime}(x)=2-\frac{2}{x^{2}}.</equation>曲线<equation>y=f(x)</equation>的拐点<equation>\left(x_{0},f\left(x_{0}\right)\right)</equation>满足<equation>f^{\prime\prime}\left(x_{0}\right)=0</equation>解<equation>2-\frac{2}{x_{0}^{2}}=0</equation>得<equation>x_{0}=\pm 1.</equation>由于f(x)的自然定义域为<equation>(0,+\infty)</equation>，故<equation>x_{0}=1</equation>，拐点坐标为(1,1).

又因为<equation>f^{\prime}(1)=\left(2 x+\frac{2}{x}\right)\bigg|_{x=1}=4</equation>，所以拐点（1，1）处的切线方程为<equation>y-1=4(x-1)</equation>即<equation>y=4 x-3.</equation>

---

**2017年第2题 | 选择题 | 4分 | 答案: B**
2. 设二阶可导函数<equation>f ( x )</equation>满足<equation>f ( 1 )=f (-1)=1, f ( 0 )=-1</equation>且<equation>f^{\prime \prime} ( x ) > 0</equation>，则（    ）

A.<equation>\int_{-1}^{1} f ( x ) \mathrm{d} x>0</equation>B.<equation>\int_{-1}^{1} f ( x ) \mathrm{d} x<0</equation>C.<equation>\int_{-1}^{0} f ( x ) \mathrm{d} x> \int_{0}^{1} f ( x ) \mathrm{d} x</equation>D.<equation>\int_{-1}^{0} f ( x ) \mathrm{d} x<\int_{0}^{1} f ( x ) \mathrm{d} x</equation>
答案: B
**解析: **解（法一）如图所示，用直线连接点<equation>(-1,1),(0,-1),(1,1).</equation>记这三点所过折线为 y = g(x). 根据 g(-1) = g(1) = 1,g(0) = -1，求得<equation>g ( x )= 2 \mid x \mid-1.</equation>y = g(x)关于y轴对称.

由于<equation>f^{\prime \prime}(x) > 0</equation>，故 y=f(x）是凹曲线.根据凹曲线的性质，曲线 y=f(x)位于曲线 y=g(x)以下，即 f(x)<equation>\leqslant</equation>g(x)，等号仅在 x=0，<equation>\pm 1</equation>处取得.

因此，<equation>\int_ {- 1} ^ {1} f (x) \mathrm {d} x < \int_ {- 1} ^ {1} g (x) \mathrm {d} x \xlongequal {\text {对称性}} 2 \int_ {0} ^ {1} (2 x - 1) \mathrm {d} x = 0.</equation>应选B.

（法二）记<equation>g ( x )=\frac{f ( x )-f ( 0 )}{x}</equation>，则 g(x)在（0,1]上可导.<equation>g ^ {\prime} (x) = \frac {x f ^ {\prime} (x) - [ f (x) - f (0) ]}{x ^ {2}}.</equation>对[0,1]上的<equation>f(x)</equation>使用拉格朗日中值定理，可得<equation>f(x)-f(0)=f^{\prime}(\xi)x</equation>其中<equation>\xi \in(0,x).</equation>由<equation>f^{\prime \prime}(x)>0</equation>可知，<equation>f^{\prime}(x)>f^{\prime}(\xi).</equation>代入（1）式，可得<equation>g ^ {\prime} (x) = \frac {x \left[ f ^ {\prime} (x) - f ^ {\prime} (\xi) \right]}{x ^ {2}} = \frac {f ^ {\prime} (x) - f ^ {\prime} (\xi)}{x} > 0.</equation>于是，<equation>g ( x )</equation>在（0，1]上单调增加，<equation>g ( x ) < g ( 1 )</equation>即<equation>f ( x ) < 2 x - 1.</equation>因此，<equation>\int_ {0} ^ {1} f (x) \mathrm {d} x < \int_ {0} ^ {1} (2 x - 1) \mathrm {d} x = 0.</equation>同理讨论[-1,0）上的 g(x）可得 g(x）在[-1,0）上单调增加，从而 g（-1）<g(x).于是对 [ -1,0 )上的 f(x)，有 f(x) < -2x-1.

因此，<equation>\int_ {- 1} ^ {0} f (x) \mathrm {d} x < \int_ {- 1} ^ {0} (- 2 x - 1) \mathrm {d} x = 0.</equation>综上所述，<equation>\int_{-1}^{1} f ( x ) \mathrm{d} x < 0</equation>应选B.

（法三）排除法.

取特殊的 f(x) ，使其满足<equation>f(-1)=f(1)=1,f(0)=-1</equation>，且<equation>f^{\prime \prime}(x) > 0.</equation>由于<equation>f^{\prime \prime}(x) > 0</equation>，故不妨取二次函数<equation>f(x)=ax^{2}+bx+c</equation>，且 a > 0.代入点（-1，1），（1，1）和（0，-1），可解得 a=2,b=0,c=-1.于是，设<equation>f(x)=2x^{2}-1.</equation>由于<equation>\int_ {- 1} ^ {1} \left(2 x ^ {2} - 1\right) \mathrm {d} x \xlongequal {\text {对称性}} 2 \int_ {0} ^ {1} \left(2 x ^ {2} - 1\right) \mathrm {d} x = 2 \left(\frac {2}{3} x ^ {3} - x\right) \Bigg | _ {0} ^ {1} = - \frac {2}{3} < 0,</equation>故可排除选项A.

进一步，可验证对<equation>f ( x )=2 x^{2}-1,</equation><equation>\int_ {- 1} ^ {0} f (x) \mathrm {d} x = \int_ {0} ^ {1} f (x) \mathrm {d} x = - \frac {1}{3}.</equation>可排除选项C和选项D.因此，应选B.

---

**2017年第9题 | 填空题 | 4分**
9. 曲线<equation>y=x\left(1+\arcsin \frac{2}{x}\right)</equation>的斜渐近线方程为 ___
**答案: **# y=x+2.
**解析: **计算<equation>\lim_{x\to \infty}\frac{y(x)}{x}.</equation><equation>\binom{x\to +\infty}{x\to -\infty}</equation><equation>\lim _ {x \rightarrow \infty} \frac {y (x)}{x} = \lim _ {x \rightarrow \infty} \frac {x \left(1 + \arcsin \frac {2}{x}\right)}{x} = \lim _ {x \rightarrow \infty} \left(1 + \arcsin \frac {2}{x}\right) = 1.</equation>计算<equation>\lim_{x\to \infty} \left[ y(x)-x\right].</equation><equation>\lim _ {x \rightarrow \infty} \left[ y (x) - x \right] = \lim _ {x \rightarrow \infty} x \arcsin \frac {2}{x} \frac {\arcsin \frac {2}{x} - \frac {2}{x}}{\overline {{\text {一}}}} \lim _ {x \rightarrow \infty} \left(x \cdot \frac {2}{x}\right) = 2.</equation>因此，斜渐近线方程为<equation>y=x+2.</equation>

---

**2016年第4题 | 选择题 | 4分 | 答案: B**
4. 设函数<equation>f ( x )</equation>在<equation>(-\infty, +\infty)</equation>内连续，其导函数的图形如图所示，则（    ）

A. 函数 f(x)有2个极值点，曲线 y=f(x)有2个拐点

B. 函数 f(x)有2个极值点，曲线 y=f(x)有3个拐点

C. 函数 f(x)有3个极值点，曲线 y=f(x)有1个拐点

D. 函数 f(x)有3个极值点，曲线 y=f(x)有2个拐点
答案: B
**解析: **解 观察图形，<equation>f ( x )</equation>共有4个可能的极值点，从左至右依次记为<equation>x_{1},</equation><equation>x_{2}, x_{3}, x_{4}</equation>其中<equation>x_{2}</equation>为虚线与x轴的交点，其余三点为<equation>f^{\prime}(x)</equation>与x轴的交点.在<equation>x=x_{1}, x_{3}, x_{4}</equation>处，<equation>f^{\prime}(x)=0</equation>在<equation>x=x_{2}</equation>处，<equation>f ( x )</equation>不可导.

分别考察<equation>x=x_{1}, x_{2}, x_{3}, x_{4}</equation>左、右小邻域内的<equation>f^{\prime}(x)</equation>的符号.

- 当<equation>x < x_{1}</equation>时，<equation>f^{\prime}(x) > 0</equation>；当<equation>x_{1} < x < x_{2}</equation>时，<equation>f^{\prime}(x) < 0</equation>故<equation>x=x_{1}</equation>是<equation>f(x)</equation>的极大值点.

- 当<equation>x_{1} < x < x_{2}</equation>时，<equation>f^{\prime}(x) < 0</equation>；当<equation>x_{2} < x < x_{3}</equation>时，<equation>f^{\prime}(x) < 0</equation>故<equation>x = x_{2}</equation>不是<equation>f(x)</equation>的极值点.

- 当<equation>x_{2} < x < x_{3}</equation>时，<equation>f^{\prime}(x) < 0</equation>；当<equation>x_{3} < x < x_{4}</equation>时，<equation>f^{\prime}(x) > 0</equation>故<equation>x = x_{3}</equation>是f(x)的极小值点.

- 当<equation>x_{3} < x < x_{4}</equation>时，<equation>f^{\prime}(x) > 0</equation>；当<equation>x > x_{4}</equation>时，<equation>f^{\prime}(x) > 0</equation>故<equation>x=x_{4}</equation>不是 f(x)的极值点.

因此，f（x）共有2个极值点.

曲线<equation>y=f(x)</equation>的可能拐点从左至右依次为<equation>\left(x_{2},f\left(x_{2}\right)\right),\left(x_{5},f\left(x_{5}\right)\right),\left(x_{4},f\left(x_{4}\right)\right)</equation>其中<equation>f^{\prime \prime}\left(x_{2}\right)</equation>不存在，<equation>f^{\prime \prime}\left(x_{5}\right)=f^{\prime \prime}\left(x_{4}\right)=0.</equation>- 当<equation>x < x_{2}</equation>时，<equation>f^{\prime}(x)</equation>单调减少；当<equation>x_{2} < x < x_{5}</equation>时，<equation>f^{\prime}(x)</equation>单调增加.故点（<equation>x_{2}, f(x_{2})</equation>）是曲线<equation>y=f(x)</equation>的拐点.

- 当<equation>x_{2} < x < x_{5}</equation>时，<equation>f^{\prime}(x)</equation>单调增加；当<equation>x_{5} < x < x_{4}</equation>时，<equation>f^{\prime}(x)</equation>单调减少.故点<equation>\left(x_{5}, f\left(x_{5}\right)\right)</equation>是曲线<equation>y=f(x)</equation>的拐点.

- 当<equation>x_{5} < x < x_{4}</equation>时，<equation>f^{\prime}(x)</equation>单调减少；当<equation>x > x_{4}</equation>时，<equation>f^{\prime}(x)</equation>单调增加. 故点<equation>\left(x_{4}, f\left(x_{4}\right)\right)</equation>是曲线<equation>y=f(x)</equation>的拐点.

因此，曲线 y=f(x）共有3个拐点.

综上所述，应选B.

---

**2016年第5题 | 选择题 | 4分 | 答案: A**
5. 设函数<equation>f_{i}(x)(i=1,2)</equation>具有二阶连续导数，且<equation>f_{i}^{\prime \prime}(x_{0})<0 (i=1,2).</equation>若两条曲线<equation>y=f_{i}(x)(i=1,2)</equation>在点<equation>(x_{0},y_{0})</equation>处具有公切线<equation>y=g(x)</equation>，且在该点处曲线<equation>y=f_{1}(x)</equation>的曲率大于曲线<equation>y=f_{2}(x)</equation>的曲率，则在<equation>x_{0}</equation>的某个邻域内，有（    ）

A.<equation>f_{1}(x)\leqslant f_{2}(x)\leqslant g(x)</equation>B.<equation>f_{2}(x)\leqslant f_{1}(x)\leqslant g(x)</equation>C.<equation>f_{1}(x)\leqslant g(x)\leqslant f_{2}(x)</equation>D.<equation>f_{2}(x)\leqslant g(x)\leqslant f_{1}(x)</equation>
答案: A
**解析: **解（法一）首先，由于函数<equation>f_{i}(x)(i=1,2)</equation>具有二阶连续导数，<equation>f_{i}^{\prime \prime}(x_{0})<0(i=1,2)</equation>，故<equation>y=f_{i}(x)(i=1,2)</equation>在<equation>x_{0}</equation>对应的点附近均为凸曲线.由凸曲线的性质可知，它们的公切线位于它们上方.因此，<equation>f_{i}(x)\leqslant g(x)(i=1,2).</equation>另一方面，由于<equation>y=f_{1}(x)</equation>和<equation>y=f_{2}(x)</equation>在点<equation>\left(x_{0},y_{0}\right)</equation>处具有公切线，故在点<equation>\left(x_{0},y_{0}\right)</equation>处，<equation>f_{1}^{\prime}\left(x_{0}\right)=f_{2}^{\prime}\left(x_{0}\right).</equation>根据曲率的定义，<equation>K _ {1} = \frac {\left| f _ {1} ^ {\prime \prime} \left(x _ {0}\right) \right|}{\left(1 + \left[ f _ {1} ^ {\prime} \left(x _ {0}\right) \right] ^ {2}\right) ^ {\frac {3}{2}}}, \quad K _ {2} = \frac {\left| f _ {2} ^ {\prime \prime} \left(x _ {0}\right) \right|}{\left(1 + \left[ f _ {2} ^ {\prime} \left(x _ {0}\right) \right] ^ {2}\right) ^ {\frac {3}{2}}}.</equation>由<equation>K_{1} > K_{2}</equation>可知，<equation>|f_{1}^{\prime \prime}(x_{0})| > |f_{2}^{\prime \prime}(x_{0})|.</equation>由于<equation>f_{i}^{\prime \prime}(x_{0}) < 0(i = 1,2)</equation>，故<equation>f_{1}^{\prime \prime}(x_{0}) < f_{2}^{\prime \prime}(x_{0})</equation>考虑函数<equation>F ( x )=f_{1} ( x )-f_{2} ( x ).</equation>由<equation>y=f_{1} ( x )</equation>和<equation>y=f_{2} ( x )</equation>在点<equation>\left(x_{0}, y_{0}\right)</equation>处相切知，<equation>F \left(x_{0}\right)=0</equation><equation>F^{\prime}\left(x_{0}\right)=0.</equation>而由前面的论述可知，<equation>F^{\prime \prime}\left(x_{0}\right)=f_{1}^{\prime \prime}\left(x_{0}\right)-f_{2}^{\prime \prime}\left(x_{0}\right)<0.</equation>由极值的第二充分条件可知，<equation>x=x_{0}</equation>是 F(x）的极大值点，从而在<equation>x_{0}</equation>的某个足够小的邻域内，<equation>F ( x )\leqslant F \left(x_{0}\right)=0</equation>即<equation>f_{1} ( x )\leqslant f_{2} ( x ).</equation>综上所述，应选A.

（法二）特殊值法.我们将题中的两条曲线分别取作两段圆弧.

以点<equation>\left(\frac{1}{4},\frac{1}{4}\right)</equation>为圆心，<equation>\frac{\sqrt{2}}{4}</equation>为半径作圆，取其位于直线<equation>y=\frac{1}{4}</equation>以上，<equation>x=\frac{1}{4}</equation>以右的部分作为曲线<equation>y=f_{1}(x)</equation>；以原点为圆心，<equation>\frac{\sqrt{2}}{2}</equation>为半径作圆，取其在第一象限内的部分作为曲线<equation>y=f_{2}(x).</equation>这两段圆弧均为凸曲线，且在点<equation>\left(\frac{1}{2},\frac{1}{2}\right)</equation>处相切.在该点处，

y = f1(x)的曲率大于 y = f2(x)的曲率.两条曲线的公切线为 x + y = 1，即 y = g(x).由图形易知，在切点附近，<equation>f_{1}(x)\leqslant f_{2}(x)\leqslant g(x).</equation>应选A.

---

**2016年第9题 | 填空题 | 4分**
9. 曲线<equation>y=\frac{x^{3}}{1+x^{2}}+\arctan(1+x^{2})</equation>的斜渐近线方程为 ___
**答案: **# y = x +<equation>\frac{\pi}{2}.</equation>
**解析: **解 记曲线为<equation>y=f(x).</equation>根据斜渐近线的定义，考虑<equation>\lim_{x\to \infty}\frac{f(x)}{x}.</equation><equation>\lim _ {x \rightarrow \infty} \frac {f (x)}{x} = \lim _ {x \rightarrow \infty} \left[ \frac {x ^ {2}}{1 + x ^ {2}} + \frac {\arctan \left(1 + x ^ {2}\right)}{x} \right] = 1 + \lim _ {x \rightarrow \infty} \frac {\arctan \left(1 + x ^ {2}\right)}{x} = 1.</equation>最后一个等号成立是因为反正切函数<equation>\arctan x</equation>的值域为<equation>\left(-\frac{\pi}{2},\frac{\pi}{2}\right)</equation>从而<equation>|\arctan(1+x^{2})|<\frac{\pi}{2},</equation>所以<equation>\lim_{x\to \infty}\frac{\arctan(1+x^{2})}{x}=0.</equation>再考虑<equation>\lim_{x\to \infty}[f(x)-x].</equation><equation>\begin{aligned} \lim _ {x \rightarrow \infty} [ f (x) - x ] &= \lim _ {x \rightarrow \infty} \left[ \frac {x ^ {3}}{1 + x ^ {2}} + \arctan \left(1 + x ^ {2}\right) - \frac {x \left(1 + x ^ {2}\right)}{1 + x ^ {2}} \right] = \lim _ {x \rightarrow \infty} \frac {- x}{1 + x ^ {2}} + \lim _ {x \rightarrow \infty} \arctan \left(1 + x ^ {2}\right) \\ &= 0 + \lim _ {x \rightarrow \infty} \arctan \left(1 + x ^ {2}\right) = \frac {\pi}{2}. \end{aligned}</equation>因此，所求斜渐近线的方程为<equation>y=x+\frac{\pi}{2}.</equation>

---

**2015年第4题 | 选择题 | 4分 | 答案: C**
4. 设函数在<equation>(-\infty, +\infty)</equation>内连续，其2阶导函数<equation>f^{\prime \prime}(x)</equation>的图形如图所示，则曲线<equation>y=f(x)</equation>的拐点个数为（    ）

A. 0 B. 1 C. 2 D. 3
答案: C
**解析: **解 由图可知，在<equation>(-\infty, +\infty)</equation>上，<equation>f^{\prime \prime}(x)=0</equation>有两个实根<equation>x_{1}, x_{2}</equation>，且<equation>f^{\prime \prime}(x)</equation>在<equation>x=0</equation>处无定义.

下面我们分别讨论点<equation>\left(x_{1},f\left(x_{1}\right)\right),\left(0,f(0)\right)</equation>和<equation>\left(x_{2},f\left(x_{2}\right)\right)</equation>是否为拐点.

在<equation>x = x_{1}</equation>的左、右邻域内，<equation>f^{\prime \prime}(x)</equation>均大于零.<equation>f^{\prime \prime}(x)</equation>在该点两侧不变号，故点<equation>(x_{1}, f(x_{1}))</equation>不是曲线<equation>y = f(x)</equation>的拐点.

在<equation>x=0</equation>的左侧邻域内，<equation>f^{\prime \prime}(x) > 0</equation>；在<equation>x=0</equation>的右侧邻域内，<equation>f^{\prime \prime}(x) < 0.</equation><equation>f^{\prime \prime}(x)</equation>在该点两侧变号，故点（0，<equation>f(0)</equation>）是曲线<equation>y=f(x)</equation>的拐点.

在<equation>x= x_{2}</equation>的左侧邻域内，<equation>f^{\prime \prime}(x)<0</equation>；在<equation>x= x_{2}</equation>的右侧邻域内，<equation>f^{\prime \prime}(x)>0.</equation><equation>f^{\prime \prime}(x)</equation>在该点两侧变号，故点（<equation>x_{2}, f\left(x_{2}\right)</equation>）是曲线<equation>y=f(x)</equation>的拐点.

综上所述，曲线<equation>y=f(x)</equation>共有2个拐点，应选C.

---

**2014年第2题 | 选择题 | 4分 | 答案: C**
2. 下列曲线中有渐近线的是（    ）

A. y=x+<equation>\sin x</equation>B. y=x²+<equation>\sin x</equation>C. y=x+<equation>\sin \frac{1}{x}</equation>D. y=x²+<equation>\sin \frac{1}{x}</equation>
答案: C
**解析: **解 先考察各曲线是否具有铅直渐近线.<equation>y=x+\sin x,y=x^{2}+\sin x</equation>在<equation>(-\infty ,+\infty)</equation>上均无间断点，故不存在铅直渐近线；<equation>y=x+\sin \frac{1}{x}</equation>和<equation>y=x^{2}+\sin \frac{1}{x}</equation>在<equation>x=0</equation>处无定义，但<equation>\lim_{x\to 0}\sin \frac{1}{x}</equation>不存在，从而也没有铅直渐近线.

再考察它们是否具有水平渐近线.

由于选项A、B、C、D中的曲线在<equation>x\to +\infty</equation>和<equation>x\to -\infty</equation>时均趋于<equation>\infty</equation>，故它们均没有水平渐近线最后考察它们是否具有斜渐近线.

对选项C，<equation>\lim\limits_{x\to \infty}\frac{x+\sin \frac{1}{x}}{x}=1</equation>，且<equation>\lim\limits_{x\to \infty}\left(x+\sin \frac{1}{x}-x\right)=\lim\limits_{x\to \infty}\sin \frac{1}{x}=0</equation>，故 y=x+sin<equation>\frac{1}{x}</equation>有斜渐近线 y=x.应选C.

下面我们说明选项A、B、D没有斜渐近线.

对选项A，<equation>\lim\limits_{x\to \infty}\frac{x+\sin x}{x}=1</equation>，但<equation>\lim\limits_{x\to \infty}\left(x+\sin x-x\right)=\lim\limits_{x\to \infty}\sin x</equation>，而<equation>\lim\limits_{x\to \infty}\sin x</equation>不存在，故选项A没有斜渐近线.

对选项B，<equation>\lim_{x\rightarrow \infty}\frac{x^{2}+\sin x}{x}=\infty</equation>；对选项D，<equation>\lim_{x\rightarrow \infty}\frac{x^{2}+\sin \frac{1}{x}}{x}=\infty</equation>，故选项B和选项D都没有斜渐近线.

---

**2014年第3题 | 选择题 | 4分 | 答案: D**
3. 设函数 f(x)具有2阶导数，<equation>g ( x )=f ( 0 ) ( 1-x )+f ( 1 ) x</equation>，则在区间[0,1]上，（    ）

A. 当<equation>f^{\prime}(x)\geqslant0</equation>时，<equation>f(x)\geqslant g(x)</equation>B. 当<equation>f^{\prime}(x)\geqslant0</equation>时，<equation>f(x)\leqslant g(x)</equation>C. 当<equation>f^{\prime\prime}(x)\geqslant0</equation>时，<equation>f(x)\geqslant g(x)</equation>D. 当<equation>f^{\prime\prime}(x)\geqslant0</equation>时，<equation>f(x)\leqslant g(x)</equation>
答案: D
**解析: **分析本题主要考查曲线的凹凸性. 对此类题，常用数形结合的方法.

(a)

(b)

设<equation>f(x)</equation>在区间<equation>I</equation>上连续，<equation>x_{1}, x_{2}</equation>为<equation>I</equation>中任意两点。不妨设<equation>x_{1} < x_{2}</equation>- 若恒有<equation>f\left(\frac{x_{1} + x_{2}}{2}\right) < \frac{f\left(x_{1}\right) + f\left(x_{2}\right)}{2}</equation>，则称曲线<equation>y = f(x)</equation>在区间I上凹，如图(a)；

- 若恒有<equation>f\left(\frac{x_{1} + x_{2}}{2}\right) > \frac{f\left(x_{1}\right) + f\left(x_{2}\right)}{2}</equation>，则称曲线<equation>y = f(x)</equation>在区间I上凸，如图(b).

从图形上看，过凹曲线<equation>y = f(x)</equation>上的任意两点的弦<equation>y = g(x)</equation>均位于该凹曲线之上，即<equation>f(x)\leqslant g(x)</equation>；过凸曲线<equation>y = f(x)</equation>上的任意两点的弦<equation>y = g(x)</equation>均位于该凸曲线之下，即<equation>f(x)\geqslant g(x)</equation>.

解 由于<equation>g ( x ) = \frac { f ( 1 ) - f ( 0 ) } { 1 - 0 } x + f ( 0 ) , g ( 0 ) = f ( 0 )</equation><equation>g ( 1 ) = f ( 1 )</equation>，故<equation>y = g ( x )</equation>表示的曲线是过点（0，f(0)），（1，f(1)）的弦.

由分析知，若<equation>y=f(x)</equation>在[0，1]上凹，则<equation>f(x)\leqslant g(x)</equation>；若<equation>y=f(x)</equation>在[0，1]上凸，则<equation>f(x)\geqslant g(x).</equation>由于f(x）具有2阶导数，故曲线的凹凸性可以由<equation>f^{\prime \prime}(x)</equation>确定.当<equation>f^{\prime \prime}(x)\geqslant 0</equation>时，<equation>y=f(x)</equation>在[0，1]上凹，从而<equation>f(x)\leqslant g(x).</equation>应选D.

一阶导数的符号与曲线的凹凸性没有直接关系。作为选项A的反例，可以考虑曲线<equation>y=x^{2}</equation>；作为选项B的反例，可以考虑曲线<equation>y=\sqrt{x}.</equation>

---

**2012年第1题 | 选择题 | 4分 | 答案: C**
1. 曲线<equation>y=\frac{x^{2}+x}{x^{2}-1}</equation>的渐近线的条数为（    ）

A.0 B.1 C.2 D.3
答案: C
**解析: **解 先判断曲线的铅直渐近线.

由于<equation>y = \frac{x^2 + x}{x^2 - 1}</equation>在<equation>x = \pm 1</equation>时间断，故可以分别考虑<equation>\lim_{x\to -1}\frac{x^2 + x}{x^2 - 1}</equation>和<equation>\lim_{x\to 1}\frac{x^2 + x}{x^2 - 1}</equation>.

由于<equation>\lim_{x\to -1}\frac{x^2 + x}{x^2 - 1} = \lim_{x\to -1}\frac{x}{x - 1} = \frac{1}{2}</equation>，故<equation>x = -1</equation>为<equation>y(x)</equation>的可去间断点.

由于<equation>\lim_{x\to 1}\frac{x^{2}+x}{x^{2}-1}=\lim_{x\to 1}\frac{x}{x-1}=\infty</equation>，故 x=1为 y(x)的无穷间断点.直线 x=1为曲线的铅直渐近线.

再判断曲线的水平渐近线

由于<equation>\lim_{x\to \infty}\frac{x^{2}+x}{x^{2}-1}=1</equation>，故直线 y=1为曲线的水平渐近线最后，由于<equation>\lim _ {\substack {x \rightarrow \infty \\ \left( \begin{array}{c} x \rightarrow + \infty \\ x \rightarrow - \infty \end{array} \right)}} \frac {y (x)}{x} = \lim _ {\substack {x \rightarrow \infty \\ \left( \begin{array}{c} x \rightarrow + \infty \\ x \rightarrow - \infty \end{array} \right)}} \frac {x + 1}{x ^ {2} - 1} = \lim _ {\substack {x \rightarrow \infty \\ \left( \begin{array}{c} x \rightarrow + \infty \\ x \rightarrow - \infty \end{array} \right)}} \frac {1}{x - 1} = 0,</equation>故曲线没有斜渐近线.

综上所述，曲线共有2条渐近线，如图所示.应选C.

---

**2011年第16题 | 解答题 | 10分**
16. (本题满分11分)

设函数 y=y(x）由参数方程<equation>\left\{ \begin{array}{l l} x=\frac{1}{3} t^{3}+t+\frac{1}{3} \\ y=\frac{1}{3} t^{3}-t+\frac{1}{3} \end{array} \right.</equation>点.<equation>y = y (x)</equation>
**答案: **(16) 极大值<equation>y(-1)=1</equation>，极小值<equation>y\left(\frac{5}{3}\right)=-\frac{1}{3}</equation>，凹区间<equation>\left(\frac{1}{3},+\infty\right)</equation>，凸区间<equation>\left(-\infty ,\frac{1}{3}\right)</equation>，拐点<equation>\left(\frac{1}{3},\frac{1}{3}\right).</equation>
**解析: **解求 y=y(x）的导数<equation>y^{\prime}(x)</equation>以及<equation>y^{\prime\prime}(x).</equation><equation>y ^ {\prime} (x) = \frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {t ^ {2} - 1}{t ^ {2} + 1}.</equation><equation>y ^ {\prime \prime} (x) = \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\mathrm {d} \left[ y ^ {\prime} (x) \right]}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {\frac {2 t \left(t ^ {2} + 1\right) - 2 t \left(t ^ {2} - 1\right)}{\left(t ^ {2} + 1\right) ^ {2}}}{t ^ {2} + 1} = \frac {4 t}{\left(t ^ {2} + 1\right) ^ {3}}.</equation>由(1)式可知，当<equation>|t| > 1</equation>时，<equation>y^{\prime}(x) > 0</equation>；当<equation>|t| < 1</equation>时，<equation>y^{\prime}(x) < 0</equation>；当<equation>t = \pm 1</equation>时，<equation>y^{\prime}(x) = 0</equation>因此，<equation>y(x)</equation>处处可导且参数<equation>t = \pm 1</equation>所对应的点满足<equation>y^{\prime}(x) = 0. t = 1</equation>对应的点为<equation>\left(\frac{5}{3}, -\frac{1}{3}\right)</equation><equation>t = -1</equation>对应的点为<equation>(-1,1)</equation>.

由于函数<equation>y(x)</equation>二阶可导，故可以通过<equation>y^{\prime \prime}(x)</equation>的符号来讨论<equation>y(x)</equation>的极值.

在点<equation>(-1,1)</equation>处，<equation>y^{\prime \prime}(x) = -\frac{1}{2} < 0</equation>，故<equation>x = -1</equation>为极大值点，对应的极大值为<equation>y(-1) = 1</equation>；在点<equation>\left(\frac{5}{3}, -\frac{1}{3}\right)</equation>处，<equation>y^{\prime \prime}(x) = \frac{1}{2} > 0</equation>，故<equation>x = \frac{5}{3}</equation>为极小值点，对应的极小值为<equation>y\left(\frac{5}{3}\right) = -\frac{1}{3}</equation>.

下面讨论曲线<equation>y=y(x)</equation>的凹凸区间以及拐点.

由（2）式可知，当<equation>t=0</equation>时，<equation>\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}\bigg|_{t=0}=0</equation>；当<equation>t > 0</equation>时，<equation>\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}} > 0</equation>；当<equation>t < 0</equation>时，<equation>\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}} < 0. t=0</equation>对应的点为<equation>\left(\frac{1}{3},\frac{1}{3}\right).</equation><equation>x^{\prime}(t)=t^{2}+1>0,x(t)</equation>是关于 t的单调增加函数.由反函数求导法则知，<equation>t^{\prime}(x)=\frac{1}{x^{\prime}(t)}>0</equation>故<equation>t(x)</equation>也是关于 x的单调增加函数.从而，

- 当<equation>x > \frac{1}{3}</equation>时，<equation>t > 0,y^{\prime \prime}(x) > 0</equation>，曲线<equation>y = y(x)</equation>为凹曲线；

- 当<equation>x < \frac{1}{3}</equation>时，<equation>t < 0,y^{\prime \prime}(x) < 0</equation>，曲线<equation>y=y(x)</equation>为凸曲线.

因此，<equation>y ( x )</equation>的极大值为<equation>y (-1)=1</equation>，极小值为<equation>y \left( {\frac{5}{3}}\right)=-{\frac{1}{3}}.</equation>曲线<equation>y=y ( x )</equation>的凹区间为<equation>\left({\frac{1}{3}},+\infty\right)</equation>，凸区间为<equation>\left(-\infty ,\frac{1}{3}\right)</equation>，拐点为<equation>\left({\frac{1}{3}},\frac{1}{3}\right).</equation>

---

**2010年第10题 | 填空题 | 4分**
10. 曲线<equation>y=\frac{2x^{3}}{x^{2}+1}</equation>的渐近线方程为 ___
**解析: **解 由于函数<equation>y=\frac{2x^{3}}{x^{2}+1}</equation>在<equation>(-\infty, +\infty)</equation>上均有定义且连续，故曲线没有铅直渐近线又由于<equation>\lim_{x\to +\infty}\frac{2x^{3}}{x^{2}+1}=+\infty, \lim_{x\to -\infty}\frac{2x^{3}}{x^{2}+1}=-\infty</equation>，故曲线没有水平渐近线考虑曲线的斜渐近线.<equation>\lim _ {\substack {x \rightarrow \infty \\ \binom {x \rightarrow + \infty} {x \rightarrow - \infty}}} \frac {\frac {2 x ^ {3}}{x ^ {2} + 1}}{x} = \lim _ {\substack {x \rightarrow \infty \\ \binom {x \rightarrow + \infty} {x \rightarrow - \infty}}} \frac {2 x ^ {2}}{x ^ {2} + 1} = 2,</equation><equation>\lim _ {\substack {x \rightarrow \infty \\ \left( \begin{array}{c} x \rightarrow + \infty \\ x \rightarrow - \infty \end{array} \right)}} \left(\frac {2 x ^ {3}}{x ^ {2} + 1} - 2 x\right) = \lim _ {\substack {x \rightarrow \infty \\ \left( \begin{array}{c} x \rightarrow + \infty \\ x \rightarrow - \infty \end{array} \right)}} \frac {2 x ^ {3} - 2 x ^ {3} - 2 x}{x ^ {2} + 1} = 0.</equation>因此，<equation>y=2x</equation>为曲线<equation>y=\frac{2x^{3}}{x^{2}+1}</equation>的斜渐近线

---


#### 导数与微分的概念


**2025年第7题 | 选择题 | 5分 | 答案: D**

7. 设函数 f(x) 连续，给出下列四个条件：<equation>\textcircled{1} \lim_{x \to 0} \frac{|f(x)|-f(0)}{x}</equation>存在；<equation>\textcircled{2} \lim_{x \to 0} \frac{f(x)-|f(0)|}{x}</equation>存在；<equation>\textcircled{3} \lim_{x \to 0} \frac{|f(x)|}{x}</equation>存在；<equation>\textcircled{4} \lim_{x \to 0} \frac{|f(x)|-|f(0)|}{x}</equation>存在；

其中能得到“ f(x)在 x=0处可导”的条件个数是（    ）

A.1 B.2 C.3 D.4

答案: D

**解析:**## 解 依次分析四个命题.

对命题<equation>\textcircled{1}</equation>，由<equation>\lim_{x\to 0}\frac{|f(x)| - f(0)}{x}</equation>存在可得<equation>\lim_{x\to 0}[|f(x)| - f(0)] = 0</equation>，即<equation>\lim_{x\to 0}|f(x)| = f(0)</equation>. 另一方面，由<equation>f(x)</equation>连续可得<equation>\lim_{x\to 0}|f(x)| = |f(0)|</equation>. 由此可得<equation>|f(0)| = f(0)</equation>，从而<equation>f(0)\geqslant 0</equation>.

若<equation>f(0) = 0</equation>，则由<equation>\lim_{x\to 0}\frac{|f(x)| - f(0)}{x}</equation>存在可得<equation>\lim_{x\to 0}\frac{|f(x)|}{x}</equation>存在，进一步可得<equation>\lim_{x\to 0}\left|\frac{f(x)}{x}\right|</equation>存在.于是，<equation>\lim _ {x \rightarrow 0 ^ {-}} \frac {\left| f (x) \right|}{x} = - \lim _ {x \rightarrow 0 ^ {-}} \left| \frac {f (x)}{x} \right| = - \lim _ {x \rightarrow 0} \left| \frac {f (x)}{x} \right|,</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {\left| f (x) \right|}{x} = \lim _ {x \rightarrow 0 ^ {+}} \left| \frac {f (x)}{x} \right| = \lim _ {x \rightarrow 0} \left| \frac {f (x)}{x} \right|.</equation>结合<equation>\lim_{x\to 0}\frac{|f(x)|}{x}</equation>存在，从而<equation>\lim_{x\to 0^{-}}\frac{|f(x)|}{x} = \lim_{x\to 0^{+}}\frac{|f(x)|}{x}</equation>可得<equation>-\lim_{x\to 0}\left|\frac{f(x)}{x}\right| = \lim_{x\to 0}\left|\frac{f(x)}{x}\right|</equation>，于是<equation>\lim_{x\to 0}\left|\frac{f(x)}{x}\right| = 0</equation>，进一步可得<equation>\lim_{x\to 0}\frac{f(x)}{x} = 0</equation>，即<equation>\lim_{x\to 0}\frac{f(x) - f(0)}{x - 0} = 0.</equation>由导数的定义可知<equation>f^{\prime}(0) = 0</equation>若<equation>f(0) > 0</equation>，则由<equation>f(x)</equation>连续可得<equation>\lim_{x\to 0}f(x) = f(0) > 0</equation>，再由极限的局部保号性可知，存在<equation>x = 0</equation>的某个去心邻域，<equation>f(x)</equation>在该邻域内恒大于0，<equation>|f(x)| = f(x)</equation>，故由<equation>\lim_{x\to 0}\frac{|f(x)| - f(0)}{x}</equation>存在可得<equation>\lim_{x\to 0}\frac{f(x) - f(0)}{x}</equation>存在.由导数的定义可知<equation>f^{\prime}(0)</equation>存在.

因此，命题<equation>\textcircled{1}</equation>正确.

对命题<equation>\textcircled{2}</equation>，由<equation>\lim_{x\to 0}\frac{f(x) - |f(0)|}{x}</equation>存在可得<equation>\lim_{x\to 0}[f(x) - |f(0)|] = 0</equation>，即<equation>\lim_{x\to 0}f(x) = |f(0)|</equation>.

另一方面，由<equation>f(x)</equation>连续可得<equation>\lim_{x\to 0}f(x) = f(0)</equation>.由此可得<equation>|f(0)| = f(0)</equation>，从而<equation>\lim_{x\to 0}\frac{f(x) - |f(0)|}{x}</equation>存在即<equation>\lim_{x\to 0}\frac{f(x) - f(0)}{x}</equation>存在.由导数的定义可知<equation>f^{\prime}(0)</equation>存在.

因此，命题<equation>\textcircled{2}</equation>正确.

对命题<equation>\textcircled{3}</equation>，由<equation>\lim_{x\to 0}\frac{|f(x)|}{x}</equation>存在可得<equation>\lim_{x\to 0}|f(x)| = 0</equation>，由此可得<equation>|f(0)| = 0</equation>，进一步可得<equation>f(0) = 0</equation>.

同命题<equation>\textcircled{1}</equation>的方法，由<equation>\lim_{x\to 0}\frac{|f(x)|}{x}</equation>存在可得<equation>\lim_{x\to 0}\left|\frac{f(x)}{x}\right|</equation>存在，进一步得到<equation>\lim_{x\to 0}\left|\frac{f(x)}{x}\right| = 0</equation>，从而<equation>\lim_{x\to 0}\frac{f(x)}{x} = 0</equation>。由导数的定义可知<equation>f^{\prime}(0) = 0</equation>.

因此，命题<equation>\textcircled{3}</equation>正确.

对命题<equation>\textcircled{4}</equation>，若<equation>f(0) = 0</equation>，则由<equation>\lim_{x\to 0}\frac{|f(x)| - |f(0)|}{x}</equation>存在可得<equation>\lim_{x\to 0}\frac{|f(x)|}{x}</equation>存在，由命题<equation>\textcircled{3}</equation>正确可得<equation>f^{\prime}(0) = 0</equation>.

若<equation>f(0) > 0</equation>，则由<equation>f(x)</equation>连续可得<equation>\lim_{x\to 0}f(x) = f(0) > 0</equation>，再由极限的局部保号性可知，存在<equation>x = 0</equation>的某个去心邻域，<equation>f(x)</equation>在该邻域内恒大于0，<equation>|f(x)| = f(x)</equation>，故由<equation>\lim_{x\to 0}\frac{|f(x)| - |f(0)|}{x}</equation>存在可得<equation>\lim_{x\to 0}\frac{f(x) - f(0)}{x}</equation>存在. 由导数的定义可知<equation>f^{\prime}(0)</equation>存在.

若<equation>f(0) < 0</equation>，则由<equation>f(x)</equation>连续可得<equation>\lim_{x\to 0}f(x) = f(0) < 0</equation>，再由极限的局部保号性可知，存在<equation>x = 0</equation>的某个去心邻域，<equation>f(x)</equation>在该邻域内恒小于0，<equation>|f(x)| = -f(x)</equation>，故由<equation>\lim_{x\to 0}\frac{|f(x)| - |f(0)|}{x}</equation>存在可得<equation>\lim_{x\to 0}\frac{-f(x) + f(0)}{x}</equation>存在，即<equation>-\lim_{x\to 0}\frac{f(x) - f(0)}{x}</equation>存在.由导数的定义可知<equation>f^{\prime}(0)</equation>存在.

因此，命题<equation>\textcircled{4}</equation>正确.

综上所述，应选D.

---

**2025年第18题 | 解答题 | 12分**

18. (本题满分12分)

设函数 f(x)在 x=0处连续，且<equation>\lim_{x\rightarrow 0}\frac{x f(x)-\mathrm{e}^{2 \sin x}+1}{\ln(1+x)+\ln(1-x)}=-3</equation>，证明 f(x)在 x=0处可导，并求<equation>f^{\prime}(0).</equation>

**答案:**<equation>f^{\prime}(0)=5</equation>

**解析:**对<equation>\mathrm{e}^{2 \sin x}</equation>的处理，可以考虑它的泰勒展开式.

解分别计算<equation>\mathrm{e}^{2\sin x}</equation>在 x=0处的一阶、二阶导数，并写出<equation>\mathrm{e}^{2\sin x}</equation>的带佩亚诺余项的二阶泰勒公式.<equation>\left(\mathrm {e} ^ {2 \sin x}\right) ^ {\prime} = \mathrm {e} ^ {2 \sin x} \cdot 2 \cos x,</equation><equation>\left(\mathrm {e} ^ {2 \sin x}\right) ^ {\prime \prime} = 2 \left(\mathrm {e} ^ {2 \sin x} \cdot \cos x\right) ^ {\prime} = 2 \left(2 \mathrm {e} ^ {2 \sin x} \cos^ {2} x - \mathrm {e} ^ {2 \sin x} \sin x\right).</equation>于是，<equation>(\mathrm{e}^{2\sin x})^{\prime}\bigg|_{x = 0} = 2,(\mathrm{e}^{2\sin x})^{\prime \prime}\bigg|_{x = 0} = 4.</equation>结合<equation>\mathrm{e}^{2\sin x}\bigg|_{x = 0} = 1</equation>可得，<equation>\mathrm {e} ^ {2 \sin x} = 1 + 2 x + \frac {4 x ^ {2}}{2} + o \left(x ^ {2}\right) = 1 + 2 x + 2 x ^ {2} + o \left(x ^ {2}\right).</equation>将（1）式代人已知极限可得，<equation>\begin{aligned} - 3 &= \lim _ {x \rightarrow 0} \frac {x f (x) - \mathrm {e} ^ {2 \sin x} + 1}{\ln (1 + x) + \ln (1 - x)} = \lim _ {x \rightarrow 0} \frac {x f (x) - 2 x - 2 x ^ {2} + o \left(x ^ {2}\right)}{\ln \left(1 - x ^ {2}\right)} \\ \frac {\ln \left(1 - x ^ {2}\right) - - x ^ {2}}{- x ^ {2}} \lim _ {x \rightarrow 0} \frac {x f (x) - 2 x - 2 x ^ {2} + o \left(x ^ {2}\right)}{- x ^ {2}} &= \lim _ {x \rightarrow 0} \frac {f (x) - 2}{- x} + 2. \end{aligned}</equation>由此可得，<equation>\lim_{x\to 0}\frac{f(x) - 2}{-x} = -5</equation>，即<equation>\lim_{x\to 0}\frac{f(x) - 2}{x} = 5.</equation>由于<equation>\lim_{x\to 0}x=0</equation>，故<equation>\lim_{x\to 0}[f(x)-2]=0</equation>，从而<equation>\lim_{x\to 0}f(x)=2</equation>.结合 f(x)在 x=0处连续可得 f(0)<equation>= \lim_{x\to 0}f(x)=2.</equation>进一步可得<equation>5 = \lim _ {x \rightarrow 0} \frac {f (x) - 2}{x} = \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0}.</equation>根据导数的定义，<equation>f ( x )</equation>在<equation>x=0</equation>处可导，且<equation>f^{\prime}(0)=5.</equation>

---

**2024年第2题 | 选择题 | 5分 | 答案: B**

2. 设函数 y=f(x)由参数方程<equation>\left\{\begin{array}{l l}x=1+t^{3}\\ y=\mathrm{e}^{t^{2}}\end{array}\right.</equation>确定，则<equation>\lim_{x\rightarrow+\infty}x\left[ f\left( 2+\frac{2}{x}\right)-f(2)\right] =</equation>(    )

A. 2e B.<equation>\frac{4\mathrm{e}}{3}</equation>C.<equation>\frac{2\mathrm{e}}{3}</equation>D.<equation>\frac{\mathrm{e}}{3}</equation>

答案: B

**解析:**<equation>\lim _ {x \rightarrow + \infty} x \left[ f \left(2 + \frac {2}{x}\right) - f (2) \right] = 2 \lim _ {x \rightarrow + \infty} \frac {f \left(2 + \frac {2}{x}\right) - f (2)}{2 + \frac {2}{x} - 2} = 2 f _ {+} ^ {\prime} (2) = 2 f ^ {\prime} (2).</equation>下面用两种方法计算<equation>f^{\prime}(2)</equation>.

（法一）根据由参数方程确定的函数的求导公式，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y / \mathrm {d} t}{\mathrm {d} x / \mathrm {d} t} = \frac {2 t \mathrm {e} ^ {t ^ {2}}}{3 t ^ {2}} = \frac {2 \mathrm {e} ^ {t ^ {2}}}{3 t}.</equation>解<equation>1 + t^{3} = 2</equation>可得，<equation>t = 1</equation>，故<equation>f^{\prime}(2) = \frac{2\mathrm{e}^{t^2}}{3t}\bigg|_{t = 1} = \frac{2\mathrm{e}}{3}</equation>.

（法二）由<equation>x = 1 + t^{3}</equation>解得<equation>t = \sqrt[3]{x - 1}</equation>，故<equation>y = \mathrm{e}^{t^2} = \mathrm{e}^{(x - 1)^{2/3}}</equation>。于是，<equation>f ^ {\prime} (2) = \left[ \mathrm {e} ^ {(x - 1) ^ {2 / 3}} \right] ^ {\prime} \Big | _ {x = 2} = \mathrm {e} ^ {(x - 1) ^ {2 / 3}} \cdot \frac {2}{3} (x - 1) ^ {- \frac {1}{3}} \Big | _ {x = 2} = \frac {2 \mathrm {e}}{3}.</equation>因此，<equation>\lim_{x\to +\infty}x\left[ f\left( 2 + \frac{2}{x}\right) - f(2)\right] = 2f^{\prime}(2) = \frac{4\mathrm{e}}{3}</equation>，应选B.

---

**2023年第5题 | 选择题 | 5分 | 答案: C**

5. 设函数 y=f(x)由<equation>\left\{\begin{array}{l l}x=2 t+|t|\\y=|t|\sin t\end{array}\right.</equation>确定，则（    )

A. f(x)连续，<equation>f^{\prime}(0)</equation>不存在 B.<equation>f^{\prime}(0)</equation>存在，<equation>f^{\prime}(x)</equation>在 x=0处不连续

C.<equation>f^{\prime}(x)</equation>连续，<equation>f^{\prime\prime}(0)</equation>不存在 D.<equation>f^{\prime\prime}(0)</equation>存在，<equation>f^{\prime\prime}(x)</equation>在 x=0处不连续

答案: C

**解析:**解 由于<equation>x=2 t+|t|=\left\{\begin{array}{ll}3 t,&t\geqslant 0,\\ t,&t<0\end{array}\right.</equation>在<equation>(-\infty ,+\infty)</equation>上单调增加，且值域为<equation>(-\infty ,+\infty)</equation>，

故其存在反函数<equation>t=\left\{\begin{array}{ll}\frac{x}{3},&x\geqslant 0,\\ x,&x<0.\end{array}\right.</equation>当<equation>x\geqslant 0</equation>时，<equation>t\geqslant 0</equation>；当<equation>x<0</equation>时，<equation>t<0</equation>．于是，<equation>f(x)=</equation>由其表达式可知，<equation>f(x)</equation>在<equation>x\neq0</equation>处连续．又由于<equation>\lim_{x\to 0}f(x)=0=f(0)</equation>，故<equation>f(x)</equation>在<equation>x=0</equation>处亦连续．因此<equation>f(x)</equation>连续.

计算可得<equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {f (x) - f (0)}{x - 0} \xlongequal {f (0) = 0} \lim _ {x \rightarrow 0 ^ {-}} \frac {- x \sin x}{x} = 0,</equation><equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x - 0} \xlongequal {f (0) = 0} \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {x}{3} \sin \frac {x}{3}}{x} = 0.</equation>f(x)在 x=0处的左、右导数均存在且相等，故<equation>f^{\prime}(0)</equation>存在，且<equation>f^{\prime}(0)=0.</equation>选项A不正确.

当 x < 0时，<equation>f ^ {\prime} (x) = \left(- x \sin x\right) ^ {\prime} = - \sin x - x \cos x.</equation>当 x > 0时，<equation>f ^ {\prime} (x) = \left(\frac {x}{3} \sin \frac {x}{3}\right) ^ {\prime} = \frac {1}{3} \left(\sin \frac {x}{3} + \frac {x}{3} \cos \frac {x}{3}\right).</equation>由此可知<equation>f^{\prime}(x)</equation>在<equation>x\neq0</equation>处连续.又由于<equation>\lim_{x\to0^{-}}f^{\prime}(x)=\lim_{x\to0^{+}}f^{\prime}(x)=0=f^{\prime}(0)</equation>，故<equation>f^{\prime}(x)</equation>在<equation>x=0</equation>处亦连续.因此<equation>f^{\prime}(x)</equation>连续.选项B不正确.

进一步计算可得，<equation>\begin{aligned} f _ {-} ^ {\prime \prime} (0) &= \lim _ {x \rightarrow 0 ^ {-}} \frac {f ^ {\prime} (x) - f ^ {\prime} (0)}{x - 0} \xlongequal {f ^ {\prime} (0) = 0} \lim _ {x \rightarrow 0 ^ {-}} \frac {- \sin x - x \cos x}{x} \\ &= - \lim _ {x \rightarrow 0 ^ {-}} \left(\frac {\sin x}{x} + \cos x\right) = - (1 + 1) = - 2, \end{aligned}</equation><equation>\begin{aligned} f _ {+} ^ {\prime \prime} (0) &= \lim _ {x \rightarrow 0 ^ {+}} \frac {f ^ {\prime} (x) - f ^ {\prime} (0)}{x - 0} \xlongequal {f ^ {\prime} (0) = 0} \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {1}{3} \left(\sin \frac {x}{3} + \frac {x}{3} \cos \frac {x}{3}\right)}{x} \\ &= \frac {1}{3} \lim _ {x \rightarrow 0 ^ {+}} \left(\frac {1}{3} \cdot \frac {\sin \frac {x}{3}}{\frac {x}{3}} + \frac {1}{3} \cos \frac {x}{3}\right) = \frac {1}{3} \times \left(\frac {1}{3} + \frac {1}{3}\right) = \frac {2}{9}. \end{aligned}</equation>由于<equation>f_{-}^{\prime \prime}(0)\neq f_{+}^{\prime \prime}(0)</equation>，故<equation>f^{\prime \prime}(0)</equation>不存在.选项C正确，选项D不正确.

综上所述，应选C.

---

**2022年第17题 | 解答题 | 10分**

17. (本题满分10分）

已知函数 f(x)在 x=1处可导，且<equation>\lim_{x\rightarrow 0}\frac{f(\mathrm{e}^{x^{2}})-3f(1+\sin^{2}x)}{x^{2}}=2</equation>，求<equation>f^{\prime}(1).</equation>

**答案:**```latex

-1.
```
**解析: **解 由 f(x)在 x=1处可导可得 f(x)在 x=1处连续，故由<equation>\lim_{x\rightarrow 0}\frac{f(\mathrm{e}^{x^{2}})-3f(1+\sin^{2}x)}{x^{2}}=2</equation>可得<equation>\lim _ {x \rightarrow 0} \left[ f \left(\mathrm {e} ^ {x ^ {2}}\right)-3 f \left(1+\sin^ {2} x\right)\right] \xlongequal {f \text {连 续}}-2 f (1)=0.</equation>于是，<equation>f(1)=0.</equation>另一方面，<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {f \left(\mathrm {e} ^ {x ^ {2}}\right)}{x ^ {2}} &= \lim _ {x \rightarrow 0} \left[ \frac {f \left(\mathrm {e} ^ {x ^ {2}}\right)-f (1)}{\mathrm {e} ^ {x ^ {2}}-1} \cdot \frac {\mathrm {e} ^ {x ^ {2}}-1}{x ^ {2}} \right] = \lim _ {x \rightarrow 0} \frac {f \left(\mathrm {e} ^ {x ^ {2}}\right)-f (1)}{\mathrm {e} ^ {x ^ {2}}-1} \cdot \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x ^ {2}}-1}{x ^ {2}} \\ &= f ^ {\prime} (1), \end{aligned}</equation><equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {f \left(1 + \sin^ {2} x\right)}{x ^ {2}} &= \lim _ {x \rightarrow 0} \left[ \frac {f \left(1 + \sin^ {2} x\right) - f (1)}{\left(\sin^ {2} x + 1\right) - 1} \cdot \frac {\sin^ {2} x}{x ^ {2}} \right] = \lim _ {x \rightarrow 0} \frac {f \left(1 + \sin^ {2} x\right) - f (1)}{\left(\sin^ {2} x + 1\right) - 1} \cdot \lim _ {x \rightarrow 0} \frac {\sin^ {2} x}{x ^ {2}} \\ &= f ^ {\prime} (1). \end{aligned}</equation>因此，<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {f \left(\mathrm {e} ^ {x ^ {2}}\right)-3 f \left(1+\sin^ {2} x\right)}{x ^ {2}} &= \lim _ {x \rightarrow 0} \frac {f \left(\mathrm {e} ^ {x ^ {2}}\right)}{x ^ {2}}-3 \lim _ {x \rightarrow 0} \frac {f \left(1+\sin^ {2} x\right)}{x ^ {2}}= f ^ {\prime} (1)-3 f ^ {\prime} (1) \\ &= - 2 f ^ {\prime} (1) = 2. \end{aligned}</equation>综上所述，<equation>f^{\prime}(1)=-1.</equation>

---

**2021年第2题 | 选择题 | 5分 | 答案: D**
2. 函数 f(x) =<equation>\left\{\begin{array}{l l}{\frac{\mathrm{e}^{x}-1}{x},}&{x\neq0}\\ {1,}&{x=0}\end{array} \right.</equation>在 x=0处（    ）

A. 连续且取得极大值 B. 连续且取得极小值 C. 可导且导数为零 D. 可导且导数不为零
答案: D
**解析: **解 首先考虑 f(x)在 x=0处的连续性.<equation>\lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x} - 1}{x} \xlongequal {\mathrm {e} ^ {x} - 1 \sim x} \lim _ {x \rightarrow 0} \frac {x}{x} = 1 = f (0).</equation>于是，f（x）在 x=0处连续.

下面考虑 f(x)在 x=0处的可导性.<equation>f ^ {\prime} (0) = \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0} \frac {\frac {\mathrm {e} ^ {x} - 1}{x} - 1}{x} = \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x} - 1 - x}{x ^ {2}} \frac {\mathrm {e} ^ {x} = 1 + x + \frac {x ^ {2}}{2} + o \left(x ^ {2}\right)}{\frac {1}{2} \neq 0}.</equation>于是，<equation>f ( x )</equation>在<equation>x=0</equation>处可导且导数不为0.

因此，应选D.

下面说明选项A、B不正确.

由于<equation>f^{\prime}(0)\neq 0</equation>，故 x=0不满足成为极值点的必要条件，从而选项A、B均不正确.

---

**2018年第2题 | 选择题 | 4分 | 答案: D**
2. 下列函数中，在 x=0处不可导的是（    ）

A. f(x) = |x|<equation>\sin|x|</equation>B. f(x) = |x|<equation>\sin\sqrt{|x|}</equation>C. f(x) =<equation>\cos|x|</equation>D. f(x) =<equation>\cos\sqrt{|x|}</equation>
答案: D
**解析: **解 考虑选项 D.<equation>f (x) = \left\{ \begin{array}{l l} \cos \sqrt {x}, & x \geqslant 0, \\ \cos \sqrt {- x}, & x < 0. \end{array} \right.</equation><equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {\cos \sqrt {- x} - 1}{x - 0} \frac {\cos \sqrt {- x} - 1 \sim - \frac {\left(\sqrt {- x}\right) ^ {2}}{2}}{\lim _ {x \rightarrow 0 ^ {-}} \frac {x}{x}} = \frac {1}{2},</equation><equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {\cos \sqrt {x} - 1}{x - 0} \frac {\cos \sqrt {x} - 1 \sim - \frac {(\sqrt {x}) ^ {2}}{2}}{\lim _ {x \rightarrow 0 ^ {+}} \frac {- \frac {x}{2}}{x}} = - \frac {1}{2}.</equation>由于<equation>f_{-}^{\prime}(0)\neq f_{+}^{\prime}(0)</equation>，故<equation>f(x)=\cos \sqrt{|x|}</equation>在 x=0处不可导.应选D.

下面分别说明选项A、B、C不正确.

选项A：<equation>f ( x )=\left\{\begin{array}{l l}x \sin x,\\-x \sin(-x),\end{array}\right.</equation><equation>x \geqslant0</equation>又因为<equation>-x \sin(-x)=-x\cdot(-\sin x)=x \sin x</equation>，所以<equation>x<0.</equation><equation>f ( x )=x \sin x,f ( x )</equation>在 x=0处可导.

选项B：<equation>f ( x )=\left\{\begin{array}{ll}x\sin \sqrt{x},&x\geqslant 0,\\ -x\sin \sqrt{-x},&x<0.\end{array} \right.</equation><equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {- x \sin \sqrt {- x} - 0}{x - 0} = \lim _ {x \rightarrow 0 ^ {-}} (- \sin \sqrt {- x}) = 0,</equation><equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {x \sin \sqrt {x} - 0}{x - 0} = \lim _ {x \rightarrow 0 ^ {+}} \sin \sqrt {x} = 0.</equation>由于<equation>f_{-}^{\prime}(0)=f_{+}^{\prime}(0)</equation>，故<equation>f(x)=|x|\sin \sqrt{|x|}</equation>在 x=0处可导.

选项C：<equation>f ( x )=\left\{\begin{array}{ll}\cos x,&x\geqslant0,\\ \cos(-x),&x<0.\end{array} \right.</equation>又因为<equation>\cos(-x)=\cos x</equation>，所以<equation>f ( x )=\cos x,f ( x )</equation>在 x=0处可导.

---

**2015年第3题 | 选择题 | 4分 | 答案: A**
3. 设函数 f(x) =<equation>\left\{\begin{array}{l l}{x^{\alpha}\cos \frac{1}{x^{\beta}},}&{x>0,\\0,&x\leqslant 0}\end{array} \right.</equation>（<equation>\alpha>0,\beta>0</equation>）. 若 f'(x)在 x=0处连续，则（    )

A.<equation>\alpha-\beta>1</equation>B. 0 <<equation>\alpha-\beta\leqslant1</equation>C.<equation>\alpha-\beta>2</equation>D. 0 <<equation>\alpha-\beta\leqslant2</equation>
答案: A
**解析: **解 首先求<equation>f^{\prime}(0).</equation>根据导数的定义，<equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {f (x) - f (0)}{x - 0} = 0, \quad f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0 ^ {+}} \left(x ^ {\alpha - 1} \cos \frac {1}{x ^ {\beta}}\right).</equation>由于<equation>f^{\prime}(x)</equation>在<equation>x=0</equation>处连续，故<equation>f^{\prime}(0)</equation>存在，从而<equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \left(x ^ {\alpha - 1} \cos \frac {1}{x ^ {\beta}}\right) = 0 = f _ {-} ^ {\prime} (0).</equation>由于当<equation>\beta > 0</equation>时，<equation>\cos \frac{1}{x^{\beta}}</equation>有界但<equation>\lim_{x\to 0^{+}}\cos \frac{1}{x^{\beta}}</equation>不存在，故<equation>\lim_{x\to 0^{+}}\left(x^{\alpha -1}\cos \frac{1}{x^{\beta}}\right)=0</equation>当且仅当<equation>\alpha >1.</equation>由上可知，当<equation>\alpha >1</equation>时，<equation>f^{\prime}(0)=0.</equation>还需要再检查<equation>\lim_{x\to 0}f^{\prime}(x)=f^{\prime}(0)=0</equation>成立的条件.

当<equation>x \leqslant 0</equation>时，<equation>f(x)\equiv 0</equation>，故当<equation>x < 0</equation>时，<equation>f^{\prime}(x)\equiv 0</equation>，从而<equation>\lim_{x\to 0^{-}}f^{\prime}(x) = 0.</equation>当 x > 0时，<equation>f ^ {\prime} (x) = \alpha x ^ {\alpha - 1} \cos \frac {1}{x ^ {\beta}} + x ^ {\alpha} \left(- \sin \frac {1}{x ^ {\beta}}\right) (- \beta) \frac {1}{x ^ {\beta + 1}} = \alpha x ^ {\alpha - 1} \cos \frac {1}{x ^ {\beta}} + \beta x ^ {\alpha - \beta - 1} \sin \frac {1}{x ^ {\beta}}.</equation>由于<equation>\alpha >1</equation>，故<equation>\lim _ {x \rightarrow 0 ^ {+}} \left(\alpha x ^ {\alpha - 1} \cos \frac {1}{x ^ {\beta}} + \beta x ^ {\alpha - \beta - 1} \sin \frac {1}{x ^ {\beta}}\right) = \lim _ {x \rightarrow 0 ^ {+}} \left(\beta x ^ {\alpha - \beta - 1} \sin \frac {1}{x ^ {\beta}}\right).</equation>由于当<equation>\beta > 0</equation>时，<equation>\sin \frac{1}{x^{\beta}}</equation>有界但<equation>\lim_{x\to 0^{+}}\sin \frac{1}{x^{\beta}}</equation>不存在，故<equation>\lim_{x\to 0^{+}}\left(\beta x^{\alpha -\beta -1}\sin \frac{1}{x^{\beta}}\right)=0</equation>当且仅当<equation>\alpha -\beta -1 > 0</equation>即<equation>\alpha -\beta >1.</equation>联立<equation>\left\{ \begin{array}{l l} \alpha >1, \\ \alpha -\beta -1 > 0, \\ \alpha >0,\beta >0, \end{array} \right.</equation>可得<equation>\alpha -\beta -1 > 0.</equation>应选A.

---

**2013年第2题 | 选择题 | 4分 | 答案: A**
2. 设函数 y=f(x)由方程<equation>\cos(xy)+\ln y-x=1</equation>确定，则<equation>\lim_{n\rightarrow \infty}n\left[ f\left( \frac{2}{n}\right)-1\right] =</equation>(    )

A.2 B.1 C.-1 D.-2
答案: A
**解析: **解 将<equation>x = 0</equation>代入方程<equation>\cos (xy) + \ln y - x = 1</equation>可得，<equation>f(0) = 1.</equation>对方程<equation>\cos ( x y )+\ln y-x=1</equation>两端关于 x求导可得<equation>- \sin (x y) \cdot \left(y + x y ^ {\prime}\right) + \frac {y ^ {\prime}}{y} - 1 = 0.</equation>代入<equation>x = 0,f(0) = 1</equation>，可得<equation>f^{\prime}(0) = 1.</equation>由导数的定义可得，<equation>\lim _ {n \rightarrow \infty} n \left[ f \left(\frac {2}{n}\right)-1 \right] = 2 \lim _ {n \rightarrow \infty} \frac {f \left(\frac {2}{n}\right)-1}{\frac {2}{n}} = 2 \lim _ {n \rightarrow \infty} \frac {f \left(\frac {2}{n}\right)-f (0)}{\frac {2}{n}-0} = 2 f ^ {\prime} (0) = 2.</equation>应选A.

---

**2011年第2题 | 选择题 | 4分 | 答案: B**
2. 设函数 f(x)在 x=0处可导，且 f(0)=0，则<equation>\lim_{x\rightarrow 0}\frac{x^{2}f(x)-2f\left(x^{3}\right)}{x^{3}}=</equation>(    )

A.<equation>-2f^{\prime}(0)</equation>B.<equation>-f^{\prime}(0)</equation>C.<equation>f^{\prime}(0)</equation>D. 0
答案: B
**解析: **解 （法一）利用导数的定义来求极限.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {x ^ {2} f (x) - 2 f \left(x ^ {3}\right)}{x ^ {3}} &= \lim _ {x \rightarrow 0} \left[ \frac {f (x)}{x} - \frac {2 f \left(x ^ {3}\right)}{x ^ {3}} \right] \xlongequal {f (0) = 0} \lim _ {x \rightarrow 0} \left[ \frac {f (x) - f (0)}{x - 0} - 2 \cdot \frac {f \left(x ^ {3}\right) - f (0)}{x ^ {3} - 0} \right] \\ &= \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0} - 2 \lim _ {x \rightarrow 0} \frac {f \left(x ^ {3}\right) - f (0)}{x ^ {3} - 0} = f ^ {\prime} (0) - 2 f ^ {\prime} (0) = - f ^ {\prime} (0). \end{aligned}</equation>应选B.

（法二）分别写出<equation>f(x)</equation>与<equation>f(x^{3})</equation>在<equation>x=0</equation>处的一阶泰勒公式.<equation>f (x) = f (0) + f ^ {\prime} (0) x + o (x) \stackrel {f (0) = 0} {=} f ^ {\prime} (0) x + o (x),</equation><equation>f \left(x ^ {3}\right) = f (0) + f ^ {\prime} (0) x ^ {3} + o \left(x ^ {3}\right) \stackrel {f (0) = 0} {=} f ^ {\prime} (0) x ^ {3} + o \left(x ^ {3}\right).</equation>代入所求极限得<equation>\lim _ {x \rightarrow 0} \frac {x ^ {2} f (x) - 2 f \left(x ^ {3}\right)}{x ^ {3}} = \lim _ {x \rightarrow 0} \frac {f ^ {\prime} (0) x ^ {3} - 2 f ^ {\prime} (0) x ^ {3} + o \left(x ^ {3}\right)}{x ^ {3}} = - f ^ {\prime} (0).</equation>应选B.

---


#### 导数与微分的计算


**2025年第14题 | 填空题 | 5分**
14. 已知函数 y=y(x)由<equation>\left\{\begin{array}{l l}x=\ln(1+2t)\\ 2t-\int_{1}^{y+t^{2}}\mathrm{e}^{-u^{2}}\mathrm{d}u=0\end{array}\right.</equation>确定，则<equation>\left.\frac{\mathrm{d} y}{\mathrm{d} x}\right|_{t=0}=</equation>___
**解析: **解 对<equation>x = \ln (1 + 2t)</equation>关于<equation>t</equation>求导可得<equation>\frac{\mathrm{d}x}{\mathrm{d}t} = \frac{2}{1 + 2t}</equation>，于是<equation>\frac{\mathrm{d}x}{\mathrm{d}t}\bigg|_{t = 0} = \frac{2}{1 + 2t}\bigg|_{t = 0} = 2</equation>.

在<equation>2t - \int_{1}^{y + t^2}\mathrm{e}^{-u^2}\mathrm{d}u = 0</equation>中令<equation>t = 0</equation>，可得<equation>\int_{1}^{y}\mathrm{e}^{-u^2}\mathrm{d}u = 0</equation>. 由于<equation>\mathrm{e}^{-u^2} > 0</equation>，故<equation>\int_{1}^{y}\mathrm{e}^{-u^2}\mathrm{d}u = 0</equation>当且仅当<equation>y = 1</equation>，从而<equation>y(t)\big|_{t = 0} = 1</equation>.

对<equation>2t - \int_{1}^{y + t^2}\mathrm{e}^{-u^2}\mathrm{d}u = 0</equation>两端关于<equation>t</equation>求导可得<equation>2 - \mathrm{e}^{-(y + t^2)^2}\left(\frac{\mathrm{d}y}{\mathrm{d}t} + 2t\right) = 0. \tag{1}</equation>在(1)式中令<equation>t = 0</equation>可得<equation>2 - \mathrm{e}^{-1}\frac{\mathrm{d}y}{\mathrm{d}t}\bigg|_{t = 0} = 0</equation>，解得<equation>\frac{\mathrm{d}y}{\mathrm{d}t}\bigg|_{t = 0} = 2\mathrm{e}</equation>.

因此，<equation>\frac{\mathrm{d}y}{\mathrm{d}x}\bigg|_{t = 0} = \frac{2\mathrm{e}}{2} = \mathrm{e}</equation>.

---

**2024年第14题 | 填空题 | 5分**
14. 已知函数<equation>f(x)=x^{2}\left(\mathrm{e}^{x}+1\right)</equation>, 则<equation>f^{(5)}(1)=</equation>___.
**答案: **## 31e
**解析: **解记<equation>u ( x )=\mathrm{e}^{x}+1, v ( x )=x^{2}</equation>，则当 k≥1时，<equation>u^{(k)}(x)=\mathrm{e}^{x}, v^{\prime}(x)=2 x, v^{\prime \prime}(x)=2</equation>，当 k≥ 3时，<equation>v^{(k)}(x)=0</equation>.由莱布尼茨公式可得，<equation>f^{(5)}(x)=\mathrm{C}_{5}^{0} u^{(5)}(x) v(x)+\mathrm{C}_{5}^{1} u^{(4)}(x) v^{\prime}(x)+\mathrm{C}_{5}^{2} u^{(3)}(x) v^{\prime \prime}(x)</equation><equation>=\mathrm{e}^{x}\cdot x^{2}+5\cdot\mathrm{e}^{x}\cdot 2 x+1 0\cdot\mathrm{e}^{x}\cdot 2=(x^{2}+1 0 x+2 0)\mathrm{e}^{x}.</equation>当 x=1时，<equation>f^{(5)}(1)=\left[ \left(x^{2}+1 0 x+2 0\right) \mathrm{e}^{x}\right] \bigg|_{x=1}=3 1 \mathrm{e}.</equation>

---

**2022年第12题 | 填空题 | 5分**
12. 已知函数<equation>y=y(x)</equation>由方程<equation>x^{2}+xy+y^{3}=3</equation>确定，则<equation>y^{\prime\prime}(1)=</equation>___
**答案: **# -<equation>\frac{31}{32}.</equation>
**解析: **解 将 x=1代入原方程可得，<equation>1+y+y^{3}=3</equation>，即<equation>y^{3}+y-2=0</equation>. 通过观察可得 y=1是该方程的一个解. 令<equation>f(y)=y^{3}+y-2</equation>，则<equation>f^{\prime}(y)=3y^{2}+1>0</equation>，f(y)为单调增加函数，从而 y=1为<equation>y^{3}+y-2=0</equation>的唯一解.

对<equation>x^{2}+ x y+ y^{3}=3</equation>两端关于 x求导可得，<equation>2 x + y + x y ^ {\prime} + 3 y ^ {2} y ^ {\prime} = 0, \quad \mathrm {即} 2 x + y + \left(x + 3 y ^ {2}\right) y ^ {\prime} = 0.</equation>代入 x=1,y（1）=1可得<equation>3+4 y^{\prime}(1)=0</equation>.解得<equation>y^{\prime}(1)=-\frac{3}{4}.</equation>对（1）式两端再次关于 x求导可得，<equation>2 + y ^ {\prime} + \left(1 + 6 y y ^ {\prime}\right) y ^ {\prime} + \left(x + 3 y ^ {2}\right) y ^ {\prime \prime} = 0.</equation>代入<equation>x=1,y(1)=1,y^{\prime}(1)=-\frac{3}{4}</equation>可得<equation>\frac{31}{8}+4y^{\prime \prime}(1)=0.</equation>解得<equation>y^{\prime \prime}(1)=-\frac{31}{32}.</equation>

---

**2021年第12题 | 填空题 | 5分**
12. 设函数<equation>y=y(x)</equation>由参数方程<equation>\left\{ \begin{array}{l} x = 2 \mathrm {e} ^ {t} + t + 1 \\ y = 4 (t - 1) \mathrm {e} ^ {t} + t ^ {2} \end{array} \right.</equation>确定，则<equation>\left.\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}\right|_{t=0}=</equation>___
**解析: **解 根据由参数方程确定的函数的导数计算公式，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {4 \mathrm {e} ^ {t} + 4 (t - 1) \mathrm {e} ^ {t} + 2 t}{2 \mathrm {e} ^ {t} + 1} = \frac {4 t \mathrm {e} ^ {t} + 2 t}{2 \mathrm {e} ^ {t} + 1} = 2 t.</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\mathrm {d} \left(\frac {\mathrm {d} y}{\mathrm {d} x}\right)}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {2}{2 \mathrm {e} ^ {t} + 1}.</equation>代入<equation>t = 0</equation>，可得<equation>\frac{\mathrm{d}^2y}{\mathrm{d}x^2}\bigg|_{t = 0} = \frac{2}{3}</equation>.

---

**2020年第4题 | 选择题 | 4分 | 答案: A**
4. 已知函数<equation>f ( x )=x^{2} \ln(1-x)</equation>，当<equation>n\geqslant 3</equation>时，<equation>f^{(n)}(0)=</equation>（    ）

A.<equation>-\frac{n!}{n-2}</equation>B.<equation>\frac{n!}{n-2}</equation>C.<equation>-\frac{(n-2)!}{n}</equation>D.<equation>\frac{(n-2)!}{n}</equation>
答案: A
**解析: **解（法一）记<equation>u ( x )=\ln( 1-x)</equation><equation>v ( x )=x^{2}</equation>，则<equation>f ( x )=u ( x ) v ( x )</equation>，从而可以用莱布尼茨公式来计算 f(x)的高阶导数.

由于<equation>f ^ {(n)} (0) = (u v) ^ {(n)} (0) = \sum_ {k = 0} ^ {n} C _ {n} ^ {k} u ^ {(n - k)} (0) v ^ {(k)} (0),</equation>而<equation>v^{\prime \prime}(0)=2,v^{(k)}(0)=0(k\neq 2)</equation>，故<equation>f ^ {(n)} (0) = 2 \mathrm {C} _ {n} ^ {2} \left[ \ln (1 - x) \right] ^ {(n - 2)} (0) = n (n - 1) \left[ \ln (1 - x) \right] ^ {(n - 2)} (0).</equation>下面利用逐次求导的方法计算<equation>\ln(1-x)</equation>在 x=0处的的 n-2阶导数.<equation>[ \ln (1 - x) ] ^ {\prime} = - \frac {1}{1 - x} = (- 1) \cdot (1 - x) ^ {- 1},</equation><equation>[ \ln (1 - x) ] ^ {\prime \prime} = (- 1) ^ {2} \cdot (- 1) \cdot (1 - x) ^ {- 2},</equation><equation>[ \ln (1 - x) ] ^ {(3)} = (- 1) ^ {3} \cdot (- 1) \cdot (- 2) \cdot (1 - x) ^ {- 3},</equation>由数学归纳法可知，<equation>[\ln(1 - x)]^{(n)} = (-1)^{n}\cdot(-1)^{n - 1}(n - 1)!(1 - x)^{-n} = -(n - 1)!(1 - x)^{-n}.</equation>于是，<equation>[\ln(1 - x)]^{(n - 2)} = -(n - 3)!(1 - x)^{-(n - 2)}.</equation>令<equation>x=0</equation>，可得<equation>[\ln(1-x)]^{(n-2)}(0)=-(n-3)!</equation>代入（1）式可得，<equation>f ^ {(n)} (0) = n (n - 1) \cdot [ - (n - 3)! ] = - \frac {n !}{n - 2}.</equation>因此，应选A.

（法二）由于<equation>\ln(1-x)</equation>的麦克劳林级数为<equation>-\sum_{n=1}^{\infty}\frac{x^{n}}{n}</equation>，故<equation>x^{2}\ln(1-x)</equation>的麦克劳林级数为<equation>-\sum_{n=1}^{\infty}\frac{x^{n+2}}{n}.x^{n}</equation>的系数为<equation>-\frac{1}{n-2}.</equation>又因为 f(x)的麦克劳林级数中，<equation>x^{n}</equation>的系数为<equation>\frac{f^{(n)}(0)}{n!}</equation>所以<equation>\frac{f^{(n)}(0)}{n!}=-\frac{1}{n-2}, f^{(n)}(0)=-\frac{n!}{n-2}.</equation>因此，应选A.

---

**2020年第9题 | 填空题 | 4分**
9.<equation>\left\{ \begin{array}{l l} x = \sqrt {t ^ {2} + 1} \\ y = \ln (t + \sqrt {t ^ {2} + 1}) \end{array} \right. \quad \mathrm {则} \left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {t = 1} = \underline {{\quad}}</equation>
**解析: **解 根据由参数方程确定的函数的求导公式，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {1 + \frac {t}{\sqrt {t ^ {2} + 1}}}{t + \sqrt {t ^ {2} + 1}} / \frac {t}{\sqrt {t ^ {2} + 1}} = \frac {1}{\sqrt {t ^ {2} + 1}} / \frac {t}{\sqrt {t ^ {2} + 1}} = \frac {1}{t}.</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\mathrm {d} \left(\frac {\mathrm {d} y}{\mathrm {d} x}\right)}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = - \frac {1}{t ^ {2}} / \frac {t}{\sqrt {t ^ {2} + 1}} = - \frac {\sqrt {t ^ {2} + 1}}{t ^ {3}}.</equation>代入 t=1，可得<equation>\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}} \Bigg|_{t=1}=-\sqrt{2}.</equation>

---

**2017年第10题 | 填空题 | 4分**
10. 设函数 y=y(x)由参数方程<equation>\left\{ \begin{array}{l} x = t + \mathrm {e} ^ {t} \\ y = \sin t \end{array} \right.</equation><equation>\left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {t = 0} = \underline {{}}</equation>
**答案: **# -<equation>\frac{1}{8}.</equation>
**解析: **解 根据由参数方程确定的函数的求导公式，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {\cos t}{1 + \mathrm {e} ^ {t}},</equation><equation>\begin{aligned} \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} &= \frac {\mathrm {d} \left[ y ^ {\prime} (x) \right]}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {\frac {\mathrm {d} \left(\frac {\cos t}{1 + \mathrm {e} ^ {t}}\right)}{\mathrm {d} t}}{1 + \mathrm {e} ^ {t}} = \frac {\frac {- \sin t \left(1 + \mathrm {e} ^ {t}\right) - \cos t \mathrm {e} ^ {t}}{\left(1 + \mathrm {e} ^ {t}\right) ^ {2}}}{1 + \mathrm {e} ^ {t}} \\ &= \frac {- \sin t \left(1 + \mathrm {e} ^ {t}\right) - \cos t \mathrm {e} ^ {t}}{\left(1 + \mathrm {e} ^ {t}\right) ^ {3}}. \end{aligned}</equation>当<equation>t = 0</equation>时，<equation>\frac{\mathrm{d}^2y}{\mathrm{d}x^2}\bigg|_{t = 0} = -\frac{1}{8}.</equation>或者也可以这样计算<equation>\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}</equation>由于<equation>x^{\prime}(t) = 1 + \mathrm{e}^{t}, x^{\prime \prime}(t) = \mathrm{e}^{t}, y^{\prime}(t) = \cos t, y^{\prime \prime}(t) = -\sin t</equation>，故<equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {y ^ {\prime \prime} (t) x ^ {\prime} (t) - y ^ {\prime} (t) x ^ {\prime \prime} (t)}{\left[ x ^ {\prime} (t) \right] ^ {3}} = \frac {- \sin t \left(1 + \mathrm {e} ^ {t}\right) - \cos t \mathrm {e} ^ {t}}{\left(1 + \mathrm {e} ^ {t}\right) ^ {3}}.</equation>

---

**2016年第12题 | 填空题 | 4分**
12. 已知函数 f(x)在<equation>(-\infty,+\infty)</equation>上连续，且<equation>f(x)=(x+1)^{2}+2\int_{0}^{x} f(t)\mathrm{d}t</equation>，则当 n≥2时，<equation>f^{(n)}(0)=</equation>___
**答案: **5·2<equation>^{n-1}</equation>
**解析: **解 （法一）逐次求导.

虽然条件中仅给出了 f(x)的连续性，但由<equation>f ( x )=( x+1 )^{2}+2 \int_{0}^{x} f ( t ) \mathrm{d} t</equation>知，f(x）可导.由于<equation>f^{\prime}(x)=2(x+1)+2 f(x)</equation>，故<equation>f^{\prime}(x)</equation>也可导，从而可推出 f(x)为 n阶可导函数（n为任意正整数）.<equation>\begin{aligned} f ^ {\prime} (x) &= 2 (x + 1) + 2 f (x), \\ f ^ {\prime \prime} (x) &= 2 + 2 f ^ {\prime} (x), \\ f ^ {(3)} (x) &= 2 f ^ {\prime \prime} (x), \\ f ^ {(4)} (x) &= \left[ f ^ {(3)} (x) \right] ^ {\prime} = \left[ 2 f ^ {\prime \prime} (x) \right] ^ {\prime} = 2 f ^ {(3)} (x) = 2 ^ {2} f ^ {\prime \prime} (x), \\ \dots \\ \mathrm {即} f ^ {(n)} (x) &= 2 ^ {n - 2} f ^ {\prime \prime} (x), n \geqslant 2. \end{aligned}</equation>由数学归纳法可知<equation>f^{(n)}(x)=2^{n-2} f^{\prime \prime}(x), n\geqslant 2.</equation>当 x=0时，<equation>f(0)=1,f^{\prime}(0)=2+2f(0)=4,f^{\prime\prime}(0)=2+2\times 4=10.</equation>因此，<equation>f^{(n)}(0) = 2^{n - 2}\cdot 10 = 5\cdot 2^{n - 1}, n\geqslant 2.</equation>（法二）先求出<equation>f(x)</equation>的表达式，再计算其导数.

当 x=0时，由已知等式易求得<equation>f(0)=1.</equation>对已知等式两端关于 x求导，得<equation>f^{\prime}(x)=2(x+1)+2 f(x)</equation>，即<equation>f^{\prime}(x)-2 f(x)=2(x+1).</equation>这是一个一阶非齐次线性微分方程.

由求解公式，得<equation>\begin{aligned} f (x) &= C \mathrm {e} ^ {\int 2 \mathrm {d} x} + \mathrm {e} ^ {\int 2 \mathrm {d} x} \int \mathrm {e} ^ {\int (- 2) \mathrm {d} x} \cdot 2 (x + 1) \mathrm {d} x = C \mathrm {e} ^ {2 x} + \mathrm {e} ^ {2 x} \int \mathrm {e} ^ {- 2 x} \cdot 2 (x + 1) \mathrm {d} x \\ &= C \mathrm {e} ^ {2 x} - x - \frac {3}{2}. \end{aligned}</equation>代入<equation>f ( 0 )=1</equation>得，<equation>C=\frac{5}{2}.</equation>因此，<equation>f ( x )=\frac{5}{2}\mathrm{e}^{2 x}-x-\frac{3}{2}.</equation>对<equation>f ( x )</equation>逐次求导，可得<equation>f^{(n)}(x)=\frac{5}{2}\cdot 2^{n}\cdot \mathrm{e}^{2x},</equation><equation>n\geqslant 2.</equation>代入<equation>x = 0</equation>，得<equation>f^{(n)}(0) = 5\cdot 2^{n - 1}, n\geqslant 2.</equation>

---

**2015年第9题 | 填空题 | 4分**
9. 设<equation>\begin{aligned} x &= \arctan t \\ y &= 3 t + t ^ {3} \end{aligned}</equation><equation>\text {则} \left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {t = 1} = \underline {{}}</equation>
**答案: **## 48.
**解析: **解 根据由参数方程确定的函数的求导公式，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {3 t ^ {2} + 3}{\frac {1}{t ^ {2} + 1}} = 3 \left(t ^ {2} + 1\right) ^ {2},</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\mathrm {d} \left[ y ^ {\prime} (x) \right]}{\mathrm {d} t} \Bigg / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {6 \left(t ^ {2} + 1\right) \cdot 2 t}{\frac {1}{t ^ {2} + 1}} = 1 2 t \left(t ^ {2} + 1\right) ^ {2}.</equation>代入<equation>t = 1</equation>，得<equation>\frac{\mathrm{d}^2y}{\mathrm{d}x^2}\bigg|_{t = 1} = 12\times 4 = 48.</equation>

---

**2015年第10题 | 填空题 | 4分**
10. 函数<equation>f(x) = x^2 2^x</equation>在<equation>x = 0</equation>处的<equation>n</equation>阶导数<equation>f^{(n)}(0) =</equation>___
**答案: **n(n-1)<equation>(\ln 2)^{n-2}.</equation>
**解析: **解记<equation>u ( x )=2^{x},</equation><equation>v ( x )=x^{2}</equation>，则<equation>f ( x )=u ( x ) v ( x )</equation>，从而可以用莱布尼茨公式来计算<equation>f ( x )</equation>的高阶导数.

由于<equation>f ^ {(n)} (0) = (u v) ^ {(n)} (0) = \sum_ {k = 0} ^ {n} \mathrm {C} _ {n} ^ {k} u ^ {(n - k)} (0) v ^ {(k)} (0)</equation>而<equation>v^{\prime \prime}(0) = 2,v^{(k)}(0) = 0(k\neq 2)</equation>，故<equation>f ^ {(n)} (0) = 2 \mathrm {C} _ {n} ^ {2} \left(2 ^ {x}\right) ^ {(n - 2)} (0) = n (n - 1) (\ln 2) ^ {n - 2}.</equation>

---

**2013年第10题 | 填空题 | 4分**
10. 设函数<equation>f ( x )=\int_{-1}^{x}\sqrt{1-\mathrm{e}^{t}}\mathrm{d} t</equation>，则 y=f(x)的反函数<equation>x=f^{-1} ( y )</equation>在 y=0处的导数<equation>\left.\frac{\mathrm{d} x}{\mathrm{d} y}\right|_{y=0}=</equation>___
**解析: **解 因为<equation>f ( x )=\int_{-1}^{x}\sqrt{1-\mathrm{e}^{t}}\mathrm{d} t</equation>，而被积函数<equation>\sqrt{1-\mathrm{e}^{t}}\geqslant 0</equation>，所以当且仅当<equation>x=-1</equation>时，<equation>y = f (x) = \int_ {- 1} ^ {x} \sqrt {1 - \mathrm {e} ^ {t}} \mathrm {d} t = 0,</equation>即<equation>f^{-1}(0)=-1.</equation>由于<equation>f^{\prime}(-1)=\sqrt{1-\mathrm{e}^{x}} \Bigg|_{x=-1}=\sqrt{1-\frac{1}{\mathrm{e}}}</equation>，故<equation>\left[ f ^ {- 1} (y) \right] ^ {\prime} \Big | _ {y = 0} = \frac {1}{f ^ {\prime} (- 1)} = \frac {1}{\sqrt {1 - \frac {1}{e}}} = \sqrt {\frac {e}{e - 1}}.</equation>

---

**2012年第2题 | 选择题 | 4分 | 答案: A**
2. 设函数<equation>f(x)=\mathrm{e}^{x}-1)(\mathrm{e}^{2x}-2)\cdots(\mathrm{e}^{nx}-n)</equation>，其中 n为正整数，则<equation>f^{\prime}(0)=</equation>(    )

A.<equation>(-1)^{n-1}(n-1)!</equation>B.<equation>(-1)^{n}(n-1)!</equation>C.<equation>(-1)^{n-1}n!</equation>D.<equation>(-1)^{n}n!</equation>
答案: A
**解析: **解（法一）利用求导的乘法法则来计算<equation>f^{\prime}(0)</equation>.

令<equation>g ( x ) = \left( \mathrm{e}^{2 x}-2 \right) \dots \left( \mathrm{e}^{n x}-n \right)</equation>，则<equation>f ( x ) = \left( \mathrm{e}^{x}-1 \right) g ( x )</equation>.由求导的乘法法则可得，<equation>f ^ {\prime} (x) = \mathrm {e} ^ {x} g (x) + \left(\mathrm {e} ^ {x} - 1\right) g ^ {\prime} (x).</equation>由于<equation>\mathrm{e}^{0}-1=0</equation>，故<equation>f ^ {\prime} (0) = \mathrm {e} ^ {0} g (0) = (- 1) (- 2) \dots [ - (n - 1) ] = (- 1) ^ {n - 1} (n - 1)!</equation>因此，应选A.

（法二）从导数的定义出发来计算<equation>f^{\prime}(0)</equation>.

由于 f（0）=0，故<equation>\begin{aligned} f ^ {\prime} (0) &= \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0} \frac {f (x)}{x} = \lim _ {x \rightarrow 0} \frac {\left(\mathrm {e} ^ {x} - 1\right)\left(\mathrm {e} ^ {2 x} - 2\right) \dots \left(\mathrm {e} ^ {n x} - n\right)}{x} \\ \underline {{\mathrm {e} ^ {x} - 1 \sim x}} \lim _ {x \rightarrow 0} \left[ \left(\mathrm {e} ^ {2 x} - 2\right) \dots \left(\mathrm {e} ^ {n x} - n\right)\right] \cdot 1 &= (- 1) (- 2) \dots [ - (n - 1) ] \cdot 1 \\ &= (- 1) ^ {n - 1} (n - 1)!. \end{aligned}</equation>因此，应选A.

（法三）排除法.

我们可以尝试代入 n值，排除不符合题意的选项.由于当 n=2时，四个选项的取值均不同，故可选择 n=2.

当<equation>n = 2</equation>时，<equation>f(x) = \left(\mathrm{e}^{x} - 1\right)\left(\mathrm{e}^{2x} - 2\right), f^{\prime}(0) = -1</equation>，故可排除选项B、C、D.

因此，应选A.

---

**2012年第9题 | 填空题 | 4分**
9. 设 y=y(x) 是由方程<equation>x^{2}-y+1=\mathrm{e}^{y}</equation>所确定的隐函数，则<equation>\left.\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\right|_{x=0}=</equation>___
**解析: **<equation>x^{2}-y+1=\mathrm{e}^{y}</equation>可得，<equation>y(0)=0.</equation>对原方程两端关于 x 求导，可得<equation>2 x-y^{\prime}=\mathrm{e}^{y} y^{\prime}</equation>代入<equation>x=0,y(0)=0</equation>，可得<equation>-y^{\prime}(0)=y^{\prime}(0)</equation>即<equation>y^{\prime}(0)=0.</equation>对<equation>2 x-y^{\prime}=\mathrm{e}^{y} y^{\prime}</equation>两端关于 x求导，可得<equation>2-y^{\prime \prime}=\mathrm{e}^{y}\left(y^{\prime}\right)^{2}+\mathrm{e}^{y} y^{\prime \prime}.</equation>代入<equation>x=0,y(0)=0</equation><equation>y^{\prime}(0)=0</equation>，得<equation>2-y^{\prime \prime}(0)=y^{\prime \prime}(0).</equation>因此，<equation>y^{\prime \prime}(0) = 1.</equation>

---

**2010年第11题 | 填空题 | 4分**
11. 函数<equation>y = \ln(1 - 2x)</equation>在<equation>x = 0</equation>处的<equation>n</equation>阶导数<equation>y^{(n)}(0) =</equation>___
**答案: **- 2<equation>^{n}</equation>(n-1) !.
**解析: **解 利用链式法则对 y逐次求各阶导数，可得<equation>y ^ {\prime} = \frac {- 2}{1 - 2 x} = - 2 \left(1 - 2 x\right) ^ {- 1},</equation><equation>y ^ {\prime \prime} = (- 2) ^ {2} (- 1) (1 - 2 x) ^ {- 2}.</equation>由数学归纳法，可证明<equation>\begin{aligned} y ^ {(n)} &= (- 2) ^ {n} (- 1) (- 2) \dots [ - (n - 1) ] (1 - 2 x) ^ {- n} \\ &= - 2 ^ {n} (n - 1)! (1 - 2 x) ^ {- n}. \end{aligned}</equation>当<equation>x = 0</equation>时，<equation>y^{(n)}(0) = -2^{n}(n - 1)!.</equation>

---

**2009年第12题 | 填空题 | 4分**
12. 设 y=y(x) 是由方程<equation>x y+\mathrm{e}^{y}=x+1</equation>确定的隐函数，则<equation>\left.\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\right|_{x=0}=</equation>___
**解析: **由<equation>xy + \mathrm{e}^{y} = x + 1</equation>知，当<equation>x = 0</equation>时，<equation>y = 0</equation>，即<equation>y(0) = 0.</equation>对原方程两端关于 x求导，得<equation>y + x y ^ {\prime} + \mathrm {e} ^ {y} y ^ {\prime} = 1.</equation>代入<equation>x = 0, y(0) = 0</equation>得，<equation>y^{\prime}(0) = 1.</equation>继续对（1）式两端关于 x求导，得<equation>y ^ {\prime} + x y ^ {\prime \prime} + y ^ {\prime} + \mathrm {e} ^ {y} \left(y ^ {\prime}\right) ^ {2} + \mathrm {e} ^ {y} y ^ {\prime \prime} = 0.</equation>代入<equation>x = 0, y(0) = 0, y^{\prime}(0) = 1</equation>得，<equation>y^{\prime \prime}(0) = -3.</equation>

---


#### 微分中值定理


**2025年第21题 | 解答题 | 12分**
21. (本题满分12分）

设函数 f(x)在区间（a,b）内可导，证明导函数<equation>f^{\prime}(x)</equation>在（a,b）内严格单调增加的充分必要条件是：对（a,b）内任意的<equation>x_{1},x_{2},x_{3}</equation>，当<equation>x_{1}<x_{2}<x_{3}</equation>时，有<equation>\frac{f(x_{2})-f(x_{1})}{x_{2}-x_{1}}<\frac{f(x_{3})-f(x_{2})}{x_{3}-x_{2}}.</equation>
**解析: **证 先证明必要性.

对<equation>(a,b)</equation>内任意的<equation>x_{1}, x_{2}, x_{3}</equation>，当<equation>x_{1} < x_{2} < x_{3}</equation>时，由拉格朗日中值定理可得存在<equation>\xi_{1}\in (x_{1}, x_{2})</equation><equation>\xi_{2}\in (x_{2}, x_{3})</equation>，使得<equation>f^{\prime}(\xi_{1}) = \frac{f(x_{2}) - f(x_{1})}{x_{2} - x_{1}}</equation><equation>f^{\prime}(\xi_{2}) = \frac{f(x_{3}) - f(x_{2})}{x_{3} - x_{2}}</equation>.由<equation>f^{\prime}(x)</equation>单调增加以及<equation>\xi_{1} <</equation><equation>\xi_{2}</equation>可得<equation>f^{\prime}(\xi_{1}) < f^{\prime}(\xi_{2})</equation>，即<equation>\frac{f(x_{2}) - f(x_{1})}{x_{2} - x_{1}} < \frac{f(x_{3}) - f(x_{2})}{x_{3} - x_{2}}.</equation>再证明充分性.

任取<equation>x_{0}, x_{1}, x_{2}\in(a,b)</equation>满足<equation>x_{1} < x_{0} < x_{2}</equation>，由已知条件可得<equation>\frac{f(x_0) - f(x_1)}{x_0 - x_1} < \frac{f(x_2) - f(x_0)}{x_2 - x_0}.</equation>取s,t满足<equation>x_{1} < s < x_{0} < t < x_{2}</equation>，由已知条件可得<equation>\frac {f (s) - f \left(x _ {1}\right)}{s - x _ {1}} < \frac {f \left(x _ {0}\right) - f (s)}{x _ {0} - s}, \quad \frac {f (t) - f \left(x _ {0}\right)}{t - x _ {0}} < \frac {f \left(x _ {2}\right) - f (t)}{x _ {2} - t}.</equation>在<equation>\frac{f(s)-f(x_{1})}{s-x_{1}}<\frac{f(x_{0})-f(s)}{x_{0}-s}</equation>中令 s<equation>\rightarrow x_{1}^{+}</equation>可得<equation>f ^ {\prime} \left(x _ {1}\right) = f _ {*} ^ {\prime} \left(x _ {1}\right) = \lim _ {s \rightarrow x _ {1}} \frac {f (s) - f \left(x _ {1}\right)}{s - x _ {1}} \leqslant \lim _ {s \rightarrow x _ {1}} \frac {f \left(x _ {0}\right) - f (s)}{x _ {0} - s} = \frac {f \left(x _ {0}\right) - f \left(x _ {1}\right)}{x _ {0} - x _ {1}}.</equation>在<equation>\frac{f(t)-f(x_{0})}{t-x_{0}}<\frac{f(x_{2})-f(t)}{x_{2}-t}</equation>中令<equation>t\to x_{2}^{-}</equation>可得<equation>\frac {f \left(x _ {2}\right) - f \left(x _ {0}\right)}{x _ {2} - x _ {0}} = \lim _ {t \rightarrow x _ {2}} \frac {f (t) - f \left(x _ {0}\right)}{t - x _ {0}} \leqslant \lim _ {t \rightarrow x _ {2}} \frac {f \left(x _ {2}\right) - f (t)}{x _ {2} - t} = f _ {-} ^ {\prime} \left(x _ {2}\right) = f ^ {\prime} \left(x _ {2}\right).</equation>由(1)式，(2)式以及<equation>\frac{f(x_{0})-f(x_{1})}{x_{0}-x_{1}}<\frac{f(x_{2})-f(x_{0})}{x_{2}-x_{0}}</equation>可得<equation>f^{\prime}(x_{1})<f^{\prime}(x_{2}).</equation>由<equation>x_{1},x_{2}</equation>的任意性可得<equation>f^{\prime}(x)</equation>在（a,b）内严格单调增加.

---

**2024年第21题 | 解答题 | 12分**
21. (本题满分12分)

设函数 f(x)具有二阶导数，且<equation>f^{\prime}(0)=f^{\prime}(1),\left| f^{\prime\prime}(x)\right| \leqslant 1</equation>，证明：

I. 当 x<equation>\in(0,1)</equation>时，<equation>|f(x)-f(0)(1-x)-f(1)x|\leqslant \frac{x(1-x)}{2}</equation>；

II.<equation>\left|\int_{0}^{1} f(x)\mathrm{d}x-\frac{f(0)+f(1)}{2}\right|\leqslant \frac{1}{12}.</equation>
**解析: **证（I）（法一）分别写出<equation>f ( x )</equation>在<equation>x=0</equation>与<equation>x=1</equation>处的一阶泰勒公式.<equation>f (x) = f (0) + f ^ {\prime} (0) x + \frac {f ^ {\prime \prime} \left(\xi_ {1}\right) x ^ {2}}{2},</equation><equation>f (x) = f (1) + f ^ {\prime} (1) (x - 1) + \frac {f ^ {\prime \prime} \left(\xi_ {2}\right) \left(x - 1\right) ^ {2}}{2},</equation>其中<equation>\xi_{1}</equation>介于0与<equation>x</equation>之间，<equation>\xi_{2}</equation>介于1与<equation>x</equation>之间.

(2) 式<equation>\times x-（1）</equation>式<equation>\times (x-1)</equation>，并结合<equation>f^{\prime}(0)=f^{\prime}(1)</equation>可得<equation>f (x) = f (0) (1 - x) + f (1) x + \frac {x (x - 1)}{2} \left[ f ^ {\prime \prime} \left(\xi_ {2}\right) (x - 1) - f ^ {\prime \prime} \left(\xi_ {1}\right) x \right].</equation>由（3）式可得，当<equation>x\in (0,1)</equation>时，<equation>\left| f (x) - f (0) (1 - x) - f (1) x \right| = \frac {x (1 - x)}{2} \left| f ^ {\prime \prime} \left(\xi_ {2}\right) (x - 1) - f ^ {\prime \prime} \left(\xi_ {1}\right) x \right|.</equation>由于<equation>|f^{\prime \prime}(\xi_{2})(x - 1) - f^{\prime \prime}(\xi_{1})x| \leqslant |f^{\prime \prime}(\xi_{2})|(1 - x) + |f^{\prime \prime}(\xi_{1})|x,</equation>故结合<equation>|f^{\prime \prime}(x)| \leqslant 1</equation>以及（4）式可得<equation>\left| f (x) - f (0) (1 - x) - f (1) x \right| \leqslant \frac {x (1 - x)}{2} \cdot [ (1 - x) + x ] = \frac {x (1 - x)}{2}.</equation>（法二）所证命题等价于当<equation>x\in (0,1)</equation>时，<equation>- \frac {x (1 - x)}{2} \leqslant f (x) - f (0) (1 - x) - f (1) x \leqslant \frac {x (1 - x)}{2}.</equation>令<equation>F ( x ) = f ( x ) - f ( 0 ) ( 1 - x ) - f ( 1 ) x - \frac { x ( 1 - x ) } { 2 }</equation>，则<equation>F ( 0 ) = F ( 1 ) = 0</equation>，且<equation>F^{\prime \prime}(x)=f^{\prime \prime}(x)</equation>+1.由于<equation>| f^{\prime \prime}(x) | \leqslant 1</equation>，故<equation>F^{\prime \prime}(x) \geqslant 0.</equation>下面证明当<equation>x\in (0,1)</equation>时，<equation>F(x)\leqslant 0.</equation>若存在<equation>c\in (0,1)</equation>，使得<equation>F(c) > 0</equation>，则分别对<equation>[0,c],[c,1]</equation>上的<equation>F(x)</equation>使用拉格朗日中值定理可得，存在<equation>\xi_{1}\in (0,c),\xi_{2}\in (c,1)</equation>，使得<equation>F ^ {\prime} \left(\xi_ {1}\right) = \frac {F (c) - F (0)}{c - 0} > 0, \quad F ^ {\prime} \left(\xi_ {2}\right) = \frac {F (1) - F (c)}{1 - c} < 0.</equation>再对<equation>[\xi_{1},\xi_{2} ]</equation>上的<equation>F^{\prime}(x)</equation>使用拉格朗日中值定理可得，存在<equation>\xi\in(\xi_{1},\xi_{2})</equation>，使得<equation>F ^ {\prime \prime} (\xi) = \frac {F ^ {\prime} \left(\xi_ {2}\right) - F ^ {\prime} \left(\xi_ {1}\right)}{\xi_ {2} - \xi_ {1}} < 0.</equation>这与<equation>F^{\prime \prime}(x)\geqslant0</equation>矛盾.

因此，当<equation>x\in (0,1)</equation>时，<equation>F(x)\leqslant 0</equation>，即<equation>f(x) - f(0)(1 - x) - f(1)x\leqslant \frac{x(1 - x)}{2}.</equation>令<equation>G ( x )=f ( x )-f ( 0 ) ( 1-x )-f ( 1 ) x+\frac{x(1-x)}{2}</equation>，同理可得<equation>G^{\prime \prime}(x)\leqslant0</equation>，且进一步可得当<equation>x\in</equation>（0,1）时，<equation>G ( x )\geqslant0</equation>，即<equation>f ( x )-f ( 0 ) ( 1-x )-f ( 1 ) x\geqslant-\frac{x(1-x)}{2}.</equation>综上所述，所证命题成立.

（Ⅱ）由第（Ⅰ）问可得<equation>\left| f (x) - f (0) (1 - x) - f (1) x \right| \leqslant \frac {x (1 - x)}{2}.</equation>对（5）式两端从0到1积分可得，<equation>\begin{aligned} \int_ {0} ^ {1} | f (x) - f (0) (1 - x) - f (1) x | \mathrm {d} x \leqslant \int_ {0} ^ {1} \frac {x (1 - x)}{2} \mathrm {d} x &= \frac {1}{2} \int_ {0} ^ {1} \left(x - x ^ {2}\right) \mathrm {d} x \\ &= \frac {1}{2} \left(\frac {x ^ {2}}{2} - \frac {x ^ {3}}{3}\right) \Big | _ {0} ^ {1} = \frac {1}{1 2}. \end{aligned}</equation><equation>\begin{array}{l} \left| \int_ {0} ^ {1} f (x) \mathrm {d} x - f (0) \int_ {0} ^ {1} (1 - x) \mathrm {d} x - f (1) \int_ {0} ^ {1} x \mathrm {d} x \right| = \left| \int_ {0} ^ {1} f (x) \mathrm {d} x - \frac {f (0) + f (1)}{2} \right| \\ \leqslant \int_ {0} ^ {1} | f (x) - f (0) (1 - x) - f (1) x | \mathrm {d} x \leqslant \frac {1}{1 2}. \\ \end{array}</equation>

---

**2023年第21题 | 解答题 | 12分**
21. (本题满分12分)

设函数 f(x)在<equation>[-a,a]</equation>上具有二阶连续导数，证明：

I. 若 f(0)=0，则存在<equation>\xi\in(-a,a)</equation>，使得<equation>f^{\prime\prime}(\xi)=\frac{1}{a^{2}}[f(a)+f(-a)].

II. 若 f(x)在</equation>(-a,a)<equation>内取得极值，则存在</equation>\eta\in(-a,a)<equation>使得</equation>|f^{\prime\prime}(\eta)|\geqslant\frac{1}{2a^{2}}|f(a)-f(-a)|.
**答案: **# （I）证明略；

（Ⅱ）证明略.
**解析: **证（I）由 f(x）的泰勒公式可得<equation>f (a) = f (0) + f ^ {\prime} (0) a + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {1}\right) a ^ {2} \xlongequal {f (0) = 0} f ^ {\prime} (0) a + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {1}\right) a ^ {2},</equation><equation>f (- a) = f (0) + f ^ {\prime} (0) \cdot (- a) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {2}\right) a ^ {2} \stackrel {f (0) = 0} {=} f ^ {\prime} (0) \cdot (- a) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {2}\right) a ^ {2},</equation>其中<equation>\xi_{1}\in(0,a),\xi_{2}\in(-a,0).</equation>两式相加可得<equation>f (a) + f (- a) = \frac {a ^ {2}}{2} \left[ f ^ {\prime \prime} \left(\xi_ {1}\right) + f ^ {\prime \prime} \left(\xi_ {2}\right) \right].</equation>记<equation>\max \left\{f^{\prime \prime}\left(\xi_{1}\right),f^{\prime \prime}\left(\xi_{2}\right)\right\}=M</equation>，<equation>\min \left\{f^{\prime \prime}\left(\xi_{1}\right),f^{\prime \prime}\left(\xi_{2}\right)\right\}=m</equation>，则由（1）式可得<equation>m \leqslant \frac {f (a) + f (- a)}{a ^ {2}} = \frac {1}{2} \left[ f ^ {\prime \prime} \left(\xi_ {1}\right) + f ^ {\prime \prime} \left(\xi_ {2}\right) \right] \leqslant M.</equation>由于 f(x)在<equation>[-a,a]</equation>上有二阶连续导数，故由连续函数的介值定理可知，存在<equation>\xi \in[ \xi_{2},\xi_{1} ]\subset(-a,a)</equation>，使得<equation>f^{\prime \prime}(\xi)=\frac{1}{a^{2}}[f(a)+f(-a)]</equation>（Ⅱ）设 f(x)在<equation>(-a,a)</equation>内的极值点为<equation>x_{0}</equation>，则<equation>f^{\prime}(x_{0})=0.</equation>由 f(x)的泰勒公式可得<equation>\begin{aligned} f (a) &= f \left(x _ {0}\right) + f ^ {\prime} \left(x _ {0}\right) \left(a - x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {1}\right) \left(a - x _ {0}\right) ^ {2} \\ \frac {f ^ {\prime} \left(x _ {0}\right) = 0}{\overline {{}}} f \left(x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {1}\right) \left(a - x _ {0}\right) ^ {2}, \end{aligned}</equation><equation>\begin{aligned} f (- a) &= f \left(x _ {0}\right) + f ^ {\prime} \left(x _ {0}\right) \left(- a - x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {2}\right) \left(- a - x _ {0}\right) ^ {2} \\ \frac {f ^ {\prime} \left(x _ {0}\right) = 0}{\overline {{}}} f \left(x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {2}\right) \left(a + x _ {0}\right) ^ {2}, \end{aligned}</equation>其中<equation>\eta_{1}\in(x_{0},a),\eta_{2}\in(-a,x_{0}).</equation>两式相减可得<equation>f (a) - f (- a) = \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {1}\right) \left(a - x _ {0}\right) ^ {2} - \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {2}\right) \left(a + x _ {0}\right) ^ {2}.</equation>记<equation>\max \left\{ \left| f^{\prime \prime}\left(\eta_{1}\right)\right|, \left| f^{\prime \prime}\left(\eta_{2}\right)\right| \right\}=M</equation>，则由（2）式可得<equation>\left| f (a) - f (- a) \right| \leqslant \frac {M}{2} \left[ \left(a - x _ {0}\right) ^ {2} + \left(a + x _ {0}\right) ^ {2} \right] = \frac {M}{2} \left(2 a ^ {2} + 2 x _ {0} ^ {2}\right) \leqslant \frac {M}{2} \cdot 4 a ^ {2} = 2 a ^ {2} M.</equation>因此，<equation>M\geqslant \frac{1}{2a^{2}}|f(a)-f(-a)|.</equation>取<equation>\eta\in\{\eta_{1},\eta_{2}\}</equation>使得<equation>|f^{\prime \prime}(\eta)|=M</equation>，则<equation>\eta\in(-a,a)</equation>满足<equation>|f^{\prime \prime}(\eta)|\geqslant\frac{1}{2a^{2}}|f(a)-f(-a)|.</equation>

---

**2022年第21题 | 解答题 | 12分**
21. (本题满分12分)

设函数 f(x)在<equation>(-\infty, +\infty)</equation>上有二阶连续导数，证明：<equation>f^{\prime \prime}(x)\geqslant0</equation>的充分必要条件是对任意不同的实数 a,b，都有<equation>f\left(\frac{a+b}{2}\right)\leqslant\frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x</equation>成立.
**解析: **证 先证明必要性，即证明，若<equation>f^{\prime \prime}(x)\geqslant 0</equation>，则对不同的实数a,b，<equation>f\left(\frac{a+b}{2}\right)\leqslant \frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x.</equation>（法一）不妨设 b > a. 在区间<equation>[a,b]</equation>上，使用 f(x)在点<equation>\frac{a+b}{2}</equation>处的二阶泰勒公式.<equation>f (x) = f \left(\frac {a + b}{2}\right) + f ^ {\prime} \left(\frac {a + b}{2}\right) \left(x - \frac {a + b}{2}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a + b}{2}\right) ^ {2},</equation>其中<equation>\xi_{x}</equation>介于x与<equation>\frac{a+b}{2}</equation>之间.

将（1）式代入<equation>\int_{a}^{b} f(x)\mathrm{d}x</equation>，可得<equation>\begin{aligned} \int_ {a} ^ {b} f (x) \mathrm {d} x &= \int_ {a} ^ {b} \left[ f \left(\frac {a + b}{2}\right) + f ^ {\prime} \left(\frac {a + b}{2}\right) \left(x - \frac {a + b}{2}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a + b}{2}\right) ^ {2} \right] \mathrm {d} x \\ &= f \left(\frac {a + b}{2}\right) (b - a) + f ^ {\prime} \left(\frac {a + b}{2}\right) \int_ {a} ^ {b} \left(x - \frac {a + b}{2}\right) \mathrm {d} x \\ + \frac {1}{2} \int_ {a} ^ {b} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a + b}{2}\right) ^ {2} \mathrm {d} x. \end{aligned}</equation>注意到<equation>\int_ {a} ^ {b} \left(x - \frac {a + b}{2}\right) \mathrm {d} x = \frac {x ^ {2}}{2} \Bigg | _ {a} ^ {b} - \frac {(a + b) (b - a)}{2} = \frac {b ^ {2} - a ^ {2}}{2} - \frac {b ^ {2} - a ^ {2}}{2} = 0,</equation>故<equation>\int_ {a} ^ {b} f (x) \mathrm {d} x = f \left(\frac {a + b}{2}\right) (b - a) + \frac {1}{2} \int_ {a} ^ {b} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a + b}{2}\right) ^ {2} \mathrm {d} x.</equation>结合<equation>f^{\prime \prime}(x)\geqslant 0</equation>可得<equation>\int_{a}^{b}f(x)\mathrm{d}x\geqslant f\left(\frac{a+b}{2}\right)(b-a)</equation>，即<equation>f\left(\frac{a+b}{2}\right)\leqslant \frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x.</equation>（法二）不妨设 b > a.<equation>f\left(\frac{a+b}{2}\right)\leqslant \frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x</equation>等价于<equation>f\left(\frac{a+b}{2}\right)(b-a)-\int_{a}^{b}f(x)\mathrm{d}x\leqslant 0.</equation>令<equation>F ( x )=\int_{a}^{x} f ( t ) \mathrm{d} t-f \left( \frac{a+x}{2} \right) ( x-a), x \in[ a, b ],</equation>则<equation>F ( a )=0</equation>，且<equation>\begin{aligned} F ^ {\prime} (x) &= f (x) - f \left(\frac {a + x}{2}\right) - f ^ {\prime} \left(\frac {a + x}{2}\right) \frac {x - a}{2} \frac {\text {拉 格 朗 日}}{\text {中 值 定 理}} f ^ {\prime} \left(\eta_ {x}\right) \frac {x - a}{2} - f ^ {\prime} \left(\frac {a + x}{2}\right) \frac {x - a}{2} \\ &= \left[ f ^ {\prime} \left(\eta_ {x}\right) - f ^ {\prime} \left(\frac {a + x}{2}\right) \right] \frac {x - a}{2}, \end{aligned}</equation>其中<equation>\eta_{x}\in \left(\frac{a + x}{2},x\right)</equation>由于<equation>f^{\prime \prime}(x)\geqslant 0</equation>，故<equation>f^{\prime}(x)</equation>单调不减，从而<equation>f^{\prime}(\eta_{x})\geqslant f^{\prime}\left(\frac{a+x}{2}\right)</equation>即<equation>f^{\prime}(\eta_{x})-f^{\prime}\left(\frac{a+x}{2}\right)\geqslant 0.</equation>于是，对<equation>x\in(a,b),F^{\prime}(x)\geqslant 0,F(x)</equation>在[a,b]上单调不减.

又因为<equation>F ( a )=0</equation>，所以<equation>F ( b )\geqslant F ( a )=0</equation>，即<equation>\int_{a}^{b} f ( x )\mathrm{d} x\geqslant f \left( \frac{a+b}{2} \right) ( b-a).</equation>下面证明充分性，即证明，若对不同的实数 a,b，<equation>f\left(\frac{a+b}{2}\right)\leqslant \frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x</equation>，则<equation>f^{\prime \prime}(x)\geqslant 0.</equation>假设存在<equation>x_{0}</equation>，使得<equation>f^{\prime \prime}(x_{0})<0</equation>，由二阶导数连续可得<equation>\lim_{x\to x_{0}}f^{\prime \prime}(x)=f^{\prime \prime}(x_{0})<0</equation>，结合极限的局部保号性可知，存在<equation>\delta >0</equation>，在区间<equation>(x_{0}-\delta,x_{0}+\delta)</equation>内，均有<equation>f^{\prime \prime}(x)<0</equation>.从而取<equation>[a_{0},b_{0}]\subset(x_{0}-\delta,x_{0}+\delta)</equation>，可得在<equation>[a_{0},b_{0}]</equation>上，均有<equation>f^{\prime \prime}(x)<0.</equation>在区间<equation>[ a_{0}, b_{0} ]</equation>上重复必要性中的做法.<equation>\begin{aligned} \int_ {a _ {0}} ^ {b _ {0}} f (x) \mathrm {d} x &= \int_ {a _ {0}} ^ {b _ {0}} \left[ f \left(\frac {a _ {0} + b _ {0}}{2}\right) + f ^ {\prime} \left(\frac {a _ {0} + b _ {0}}{2}\right) \left(x - \frac {a _ {0} + b _ {0}}{2}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a _ {0} + b _ {0}}{2}\right) ^ {2} \right] \mathrm {d} x \\ &= f \left(\frac {a _ {0} + b _ {0}}{2}\right) \left(b _ {0} - a _ {0}\right) + f ^ {\prime} \left(\frac {a _ {0} + b _ {0}}{2}\right) \int_ {a _ {0}} ^ {b _ {0}} \left(x - \frac {a _ {0} + b _ {0}}{2}\right) \mathrm {d} x \\ + \frac {1}{2} \int_ {a _ {0}} ^ {b _ {0}} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a _ {0} + b _ {0}}{2}\right) ^ {2} \mathrm {d} x, \end{aligned}</equation>其中<equation>\xi_{x}</equation>介于x与<equation>\frac{a_{0}+b_{0}}{2}</equation>之间.

于是，<equation>\int_ {a _ {0}} ^ {b _ {0}} f (x) \mathrm {d} x = f \left(\frac {a _ {0} + b _ {0}}{2}\right) \left(b _ {0} - a _ {0}\right) + \frac {1}{2} \int_ {a _ {0}} ^ {b _ {0}} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a _ {0} + b _ {0}}{2}\right) ^ {2} \mathrm {d} x.</equation>结合<equation>f^{\prime \prime}(x) < 0</equation>可得<equation>\int_{a_{0}}^{b_{0}}f(x)\mathrm{d}x < f\left(\frac{a_{0}+b_{0}}{2}\right)\left(b_{0}-a_{0}\right)</equation>，即<equation>f\left(\frac{a_{0}+b_{0}}{2}\right) > \frac{1}{b_{0}-a_{0}}\int_{a_{0}}^{b_{0}}f(x)\mathrm{d}x.</equation>这与前提矛盾.

因此，假设不正确.<equation>f^{\prime \prime}(x)</equation>在<equation>(-\infty, +\infty)</equation>上恒非负.

（法二）若对不同的实数 a,b，<equation>f\left(\frac{a+b}{2}\right)\leqslant \frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x</equation>，则对任意实数<equation>x_{0}</equation>以及任意<equation>\delta >0,</equation>均有<equation>\int_{x_0 - \delta}^{x_0 + \delta}f(x)\mathrm{d}x - 2\delta f(x_0)\geqslant 0</equation>，从而<equation>\frac{\int_{x_0 - \delta}^{x_0 + \delta}f(x)\mathrm{d}x - 2\delta f(x_0)}{\delta^{3}}\geqslant 0.</equation>而<equation>\begin{array}{l} \lim _ {\delta \rightarrow 0 ^ {+}} \frac {\int_ {x _ {0} - \delta} ^ {x _ {0} + \delta} f (x) \mathrm {d} x - 2 \delta f \left(x _ {0}\right)}{\delta^ {3}} \xlongequal {\text {洛必达}} \lim _ {\delta \rightarrow 0 ^ {+}} \frac {f \left(x _ {0} + \delta\right) + f \left(x _ {0} - \delta\right) - 2 f \left(x _ {0}\right)}{3 \delta^ {2}} \\ \xlongequal {\text {洛必达}} \lim _ {\delta \rightarrow 0 ^ {+}} \frac {f ^ {\prime} \left(x _ {0} + \delta\right) - f ^ {\prime} \left(x _ {0} - \delta\right)}{6 \delta} \\ \xlongequal {\text {洛必达}} \lim _ {\delta \rightarrow 0 ^ {+}} \frac {f ^ {\prime \prime} \left(x _ {0} + \delta\right) + f ^ {\prime \prime} \left(x _ {0} - \delta\right)}{6} \\ \xlongequal {f ^ {\prime \prime} \text {连续}} \frac {1}{3} f ^ {\prime \prime} \left(x _ {0}\right), \\ \end{array}</equation>故由极限的保号性可知，<equation>f^{\prime \prime} \left( x_{0} \right) \geqslant 0.</equation>由<equation>x_0</equation>的任意性可知，对不同的实数<equation>a,b,f\left(\frac{a + b}{2}\right)\leqslant \frac{1}{b - a}\int_{a}^{b}f(x)\mathrm{d}x</equation>是<equation>f^{\prime \prime}(x)\geqslant 0</equation>的充分条件.综上所述，<equation>f^{\prime \prime}(x)\geqslant 0</equation>的充分必要条件是对不同的实数<equation>a,b,f\left(\frac{a + b}{2}\right)\leqslant \frac{1}{b - a}\int_{a}^{b}f(x)\mathrm{d}x.</equation>

---

**2020年第20题 | 解答题 | 11分**
20. (本题满分11分）

设函数<equation>f ( x )=\int_{1}^{x} \mathrm{e}^{t^{2}} \mathrm{d} t.</equation>I. 证明：存在<equation>\xi\in(1,2)</equation>，使得<equation>f(\xi)=(2-\xi)\mathrm{e}^{\xi^{2}}</equation>II. 证明：存在<equation>\eta\in(1,2)</equation>，使得<equation>f(2)=\ln 2\cdot\eta\mathrm{e}^{\eta^{2}}</equation>
**答案: **# （I）证明略；

（Ⅱ）证明略.
**解析: **证 （ I ）注意到<equation>f(1)=0.</equation>（法一）待证等式等价于<equation>f (\xi) + (\xi -2)\mathrm{e}^{\xi^{2}} = 0.</equation>令<equation>F ( x ) = f ( x ) + ( x - 2 ) \mathrm{e}^{x^{2}}</equation>，则<equation>F ( 1 ) = f ( 1 ) - \mathrm{e} = - \mathrm{e} < 0,F(2) = f(2) = \int_{1}^{2}\mathrm{e}^{t^{2}}\mathrm{d}t > 0.</equation>对[1,2]上的<equation>F(x)</equation>使用零点定理可得，存在<equation>\xi\in(1,2)</equation>，使得<equation>F(\xi)=0</equation>即<equation>f(\xi)+(\xi-2)\mathrm{e}^{\xi^{2}}=0</equation>也即<equation>f(\xi)=(2-\xi)\mathrm{e}^{\xi^{2}}.</equation>（法二）由变限积分求导公式可得，<equation>f^{\prime}(x)=\mathrm{e}^{x^{2}}</equation>，故待证等式<equation>f(\xi)=(2-\xi)\mathrm{e}^{\xi^{2}}</equation>等价于<equation>f(\xi)=(2-\xi)f^{\prime}(\xi)</equation>，也等价于<equation>f(\xi)+(\xi-2)f^{\prime}(\xi)=0.</equation>令<equation>F ( x ) = ( x - 2 ) f ( x )</equation>，则<equation>F^{\prime}(x)=f(x)+(x-2)f^{\prime}(x).</equation>由于<equation>F ( 1 )=-f ( 1 )=0,F ( 2 )=0</equation>，故由罗尔定理可知，存在<equation>\xi\in(1,2)</equation>，使得<equation>F^{\prime}(\xi)=0</equation>，即<equation>f(\xi)=(2-\xi)f^{\prime}(\xi)</equation>，也即<equation>f(\xi)=(2-\xi)\mathrm{e}^{\xi^{2}}.</equation>（法三）令<equation>F ( x )=\int_{1}^{x}\left(\int_{1}^{u}\mathrm{e}^{t^{2}}\mathrm{d} t\right)\mathrm{d} u</equation>，则利用变限积分求导公式可得<equation>F^{\prime}(x)=\int_{1}^{x}\mathrm{e}^{t^{2}}\mathrm{d} t=f(x).</equation>F（1）=0.此外，利用交换积分次序，可得<equation>F (x) = \int_ {1} ^ {x} \mathrm {d} u \int_ {1} ^ {u} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = \int_ {1} ^ {x} \mathrm {d} t \int_ {t} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} u = \int_ {1} ^ {x} (x - t) \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = x \int_ {1} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t - \int_ {1} ^ {x} t \mathrm {e} ^ {t ^ {2}} \mathrm {d} t.</equation>于是，<equation>F ( 2 )=\int_{1}^{2} ( 2-t ) \mathrm{e}^{t^{2}} \mathrm{d} t.</equation>令<equation>G ( x ) = F ( x ) - \int_{1}^{x} ( 2 - t ) \mathrm{e}^{t^{2}} \mathrm{d} t</equation>，则<equation>G ( 1 ) = 0.</equation><equation>G (2) = F (2) - \int_ {1} ^ {2} (2 - t) \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = \int_ {1} ^ {2} (2 - t) \mathrm {e} ^ {t ^ {2}} \mathrm {d} t - \int_ {1} ^ {2} (2 - t) \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = 0.</equation>由罗尔定理，存在<equation>\xi\in(1,2)</equation>，使得<equation>G^{\prime}(\xi)=0</equation>，即<equation>G ^ {\prime} (\xi) = F ^ {\prime} (\xi) - (2 - \xi) \mathrm {e} ^ {\xi^ {2}} = f (\xi) - (2 - \xi) \mathrm {e} ^ {\xi^ {2}} = 0.</equation>因此，存在<equation>\xi \in (1,2)</equation>，使得<equation>f(\xi) = (2 - \xi)\mathrm{e}^{\xi^2}</equation>（Ⅱ）令<equation>g ( x )=\ln x</equation>，则<equation>g^{\prime}(x)=\frac{1}{x}.</equation>由柯西中值定理，存在<equation>\eta\in(1,2)</equation>，使得<equation>\frac {f (2) - f (1)}{g (2) - g (1)} = \frac {f ^ {\prime} (\eta)}{g ^ {\prime} (\eta)}.</equation>由于<equation>f(1) = 0,g(1) = 0,g(2) = \ln 2</equation>，故（1）式可化为<equation>\frac{f(2)}{\ln 2} = \frac{\mathrm{e}^{\eta^2}}{\frac{1}{\eta}}</equation>即<equation>f(2) = \ln 2\cdot \eta \mathrm{e}^{\eta^2}</equation>.
