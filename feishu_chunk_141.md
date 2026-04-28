#### 一阶非齐次线性微分方程

**2025年第13题 | 填空题 | 5分**

13. 微分方程<equation>x y^{\prime}-y+x^{2} \mathrm{e}^{x}=0</equation>满足条件<equation>y(1)=- \mathrm{e}</equation>的解为 y=___

**答案:**## xe<equation>^x</equation>.

**解析:**解 整理原方程可得<equation>y^{\prime}-\frac{y}{x}=-x\mathrm{e}^{x}.</equation>由一阶非齐次线性微分方程的通解公式可得<equation>y=\mathrm{e}^{\int \frac{1}{x}\mathrm{d}x}\left[\int(-x\mathrm{e}^{x})\cdot\mathrm{e}^{\int(-\frac{1}{x})\mathrm{d}x}\mathrm{d}x+C\right]=\mid x\mid\left[\int(-x\mathrm{e}^{x})\cdot\frac{1}{\mid x\mid}\mathrm{d}x+C\right]</equation><equation>=-x\int\mathrm{e}^{x}\mathrm{d}x+C\mid x\mid=-x\mathrm{e}^{x}+C\mid x\mid.</equation>将 y（1）=-e代入<equation>y=-x\mathrm{e}^{x}+C\left| x\right|</equation>可得<equation>-\mathrm{e}=-\mathrm{e}+C</equation>，解得 C=0.因此，<equation>y=-x\mathrm{e}^{x}.</equation>

---

**2022年第17题 | 解答题 | 10分**

17. (本题满分10分）

设函数 y(x）是微分方程<equation>y^{\prime}+\frac{1}{2\sqrt{x}} y=2+\sqrt{x}</equation>满足条件 y(1）=3的解，求曲线 y=y(x）的渐近线.

**答案:**y=2x为曲线 y=2x+<equation>\mathrm{e}^{1-\sqrt{x}}</equation>的斜渐近线，也是唯一的渐近线.

**解析:**根据求解公式，<equation>y = \mathrm {e} ^ {- \int \frac {1}{2 \sqrt {x}} \mathrm {d} x} \left[ \int (2 + \sqrt {x}) \mathrm {e} ^ {\int \frac {1}{2 \sqrt {x}} \mathrm {d} x} \mathrm {d} x + C _ {0} \right] = \mathrm {e} ^ {- \sqrt {x}} \left[ \int (2 + \sqrt {x}) \mathrm {e} ^ {\sqrt {x}} \mathrm {d} x + C _ {0} \right].</equation>下面计算<equation>\int(2+\sqrt{x})\mathrm{e}^{\sqrt{x}}\mathrm{d}x.</equation>令<equation>u=\sqrt{x}</equation>，则<equation>x=u^{2}</equation>，<equation>\mathrm{d} x=2 u \mathrm{d} u.</equation><equation>\begin{aligned} \int (2 + \sqrt {x}) \mathrm {e} ^ {\sqrt {x}} \mathrm {d} x \xlongequal {u = \sqrt {x}} 2 \int (2 + u) u \mathrm {e} ^ {u} \mathrm {d} u &= 2 \left(\int u ^ {2} \mathrm {e} ^ {u} \mathrm {d} u + \int 2 u \mathrm {e} ^ {u} \mathrm {d} u\right) \\ &= 2 \left[ \int u ^ {2} \mathrm {d} \left(\mathrm {e} ^ {u}\right) + \int 2 u \mathrm {e} ^ {u} \mathrm {d} u \right] = 2 \left(u ^ {2} \mathrm {e} ^ {u} - \int 2 u \mathrm {e} ^ {u} \mathrm {d} u + \int 2 u \mathrm {e} ^ {u} \mathrm {d} u\right) \\ &= 2 u ^ {2} \mathrm {e} ^ {u} + C _ {1} = 2 x \mathrm {e} ^ {\sqrt {x}} + C _ {1}. \end{aligned}</equation>将该结果代入（1）式，可得<equation>y = \mathrm {e} ^ {- \sqrt {x}} \left(2 x \mathrm {e} ^ {\sqrt {x}} + C\right) = 2 x + C \mathrm {e} ^ {- \sqrt {x}},</equation>其中 C为待定常数.代入<equation>y ( 1 )=3</equation>，可得<equation>3=2+C\cdot\mathrm{e}^{-1}</equation>，解得<equation>C=\mathrm{e}.</equation>因此，<equation>y ( x ) = 2 x + \mathrm {e} ^ {1 - \sqrt {x}} , x \in ( 0, + \infty) .</equation>由于函数<equation>y(x)=2 x+\mathrm{e}^{1-\sqrt{x}}</equation>在（0，<equation>+\infty</equation>）内连续，且<equation>\lim_{x\to 0^{+}}y(x)=\mathrm{e}</equation>，故曲线<equation>y=2 x+\mathrm{e}^{1-\sqrt{x}}</equation>没有铅直渐近线.

又因为<equation>\lim_{x\to +\infty}y(x) = \lim_{x\to +\infty}\left(2x + \mathrm{e}^{1 - \sqrt{x}}\right) = +\infty</equation>，所以曲线<equation>y = 2x + \mathrm{e}^{1 - \sqrt{x}}</equation>没有水平渐近线.

下面计算斜渐近线.<equation>\lim _ {x \rightarrow + \infty} \frac {y (x)}{x} = \lim _ {x \rightarrow + \infty} \frac {2 x + \mathrm {e} ^ {1 - \sqrt {x}}}{x} = 2,</equation><equation>\lim _ {x \rightarrow + \infty} [ y (x) - 2 x ] = \lim _ {x \rightarrow + \infty} \mathrm {e} ^ {1 - \sqrt {x}} = 0.</equation>因此，<equation>y=2x</equation>为曲线<equation>y=2x+\mathrm{e}^{1-\sqrt{x}}</equation>的斜渐近线，也是唯一的渐近线.

---

**2019年第17题 | 解答题 | 10分**

17. (本题满分10分)

设函数 y(x)是微分方程<equation>y^{\prime}-xy=\frac{1}{2\sqrt{x}} \mathrm{e}^{\frac{x^{2}}{2}}</equation>满足条件 y(1)<equation>=\sqrt{\mathrm{e}}</equation>的特解.

I. 求 y(x);

II. 设平面区域 D = {(x,y) | 1≤x≤2,0≤y≤y(x)}，求 D绕 x轴旋转所得旋转体的体积.

**答案:**(I)<equation>y(x)=\sqrt{x}\mathrm{e}^{\frac{x^{2}}{2}}</equation>; (II)<equation>\frac{1}{2}\pi(\mathrm{e}^{4}-\mathrm{e}).</equation>

**解析:**（I）由一阶非齐次线性微分方程的求解公式可得，<equation>\begin{aligned} y &= \mathrm {e} ^ {\int x \mathrm {d} x} \left[ \int \frac {1}{2 \sqrt {x}} \cdot \mathrm {e} ^ {\frac {x ^ {2}}{2}} \cdot \mathrm {e} ^ {\int (- x) \mathrm {d} x} \mathrm {d} x + C \right] = \mathrm {e} ^ {\frac {x ^ {2}}{2}} \left(\int \frac {1}{2 \sqrt {x}} \cdot \mathrm {e} ^ {\frac {x ^ {2}}{2}} \cdot \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \mathrm {d} x + C\right) \\ &= \mathrm {e} ^ {\frac {x ^ {2}}{2}} \left(\int \frac {1}{2 \sqrt {x}} \mathrm {d} x + C\right) = \sqrt {x} \mathrm {e} ^ {\frac {x ^ {2}}{2}} + C \mathrm {e} ^ {\frac {x ^ {2}}{2}}, \end{aligned}</equation>其中 C为待定常数.

代入<equation>x = 1,y(1) = \sqrt{\mathrm{e}}</equation>，可得<equation>\sqrt{\mathrm{e}} = \sqrt{\mathrm{e}} + C\sqrt{\mathrm{e}}.</equation>解得<equation>C = 0.</equation>因此，<equation>y ( x ) = \sqrt{x}\mathrm{e}^{\frac{x^{2}}{2}}.</equation>（Ⅱ）区域 D 如图所示.

根据旋转体的体积计算公式，<equation>\begin{aligned} V &= \pi \int_ {1} ^ {2} \left(\sqrt {x} \mathrm {e} ^ {\frac {x ^ {2}}{2}}\right) ^ {2} \mathrm {d} x = \pi \int_ {1} ^ {2} x \mathrm {e} ^ {x ^ {2}} \mathrm {d} x = \frac {1}{2} \pi \int_ {1} ^ {2} \mathrm {e} ^ {x ^ {2}} \mathrm {d} \left(x ^ {2}\right) \\ &= \frac {1}{2} \pi \mathrm {e} ^ {x ^ {2}} \Bigg | _ {1} ^ {2} = \frac {1}{2} \pi \left(\mathrm {e} ^ {4} - \mathrm {e}\right). \end{aligned}</equation>

---

**2014年第17题 | 解答题 | 10分**

17. (本题满分10分)

设函数 f(u)具有连续导数，且<equation>z=f(\mathrm{e}^{x}\cos y)</equation>满足<equation>\cos y\frac{\partial z}{\partial x}-\sin y\frac{\partial z}{\partial y}=(4z+\mathrm{e}^{x}\cos y)\mathrm{e}^{x}.</equation>若 f(0)=0，求 f(u)的表达式.

**答案:**<equation>(1 7) f (u) = \frac {1}{1 6} \mathrm {e} ^ {4 u} - \frac {1}{4} u - \frac {1}{1 6}.</equation>

**解析:**由链式法则知，<equation>\frac {\partial z}{\partial x} = f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right) \cdot \left(\mathrm {e} ^ {x} \cos y\right), \quad \frac {\partial z}{\partial y} = f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right) \cdot \left(- \mathrm {e} ^ {x} \sin y\right).</equation>代入题设等式中可得，<equation>\mathrm {e} ^ {x} \cos^ {2} y f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right) + \mathrm {e} ^ {x} \sin^ {2} y f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right) = \left(4 z + \mathrm {e} ^ {x} \cos y\right) \mathrm {e} ^ {x}.</equation>化简得<equation>f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right) = 4 f \left(\mathrm {e} ^ {x} \cos y\right) + \mathrm {e} ^ {x} \cos y.</equation>令<equation>u=\mathrm{e}^{x}\cos y</equation>，得<equation>f ^ {\prime} (u) - 4 f (u) = u.</equation>此为一阶非齐次线性微分方程，由求解公式知，<equation>f (u) = \mathrm {e} ^ {- \int (- 4) \mathrm {d} u} \left[ \int u \mathrm {e} ^ {\int (- 4) \mathrm {d} u} \mathrm {d} u + C \right] = \mathrm {e} ^ {4 u} \left(\frac {\mathrm {e} ^ {- 4 u}}{- 4} u - \int \frac {\mathrm {e} ^ {- 4 u}}{- 4} \mathrm {d} u + C\right) = - \frac {1}{4} u - \frac {1}{1 6} + C \mathrm {e} ^ {4 u},</equation>其中 C为待定常数.

将<equation>f ( 0 )=0</equation>代入上式得<equation>C=\frac{1}{1 6}.</equation>因此，<equation>f (u) = \frac {1}{1 6} \mathrm {e} ^ {4 u} - \frac {1}{4} u - \frac {1}{1 6}.</equation>

---


