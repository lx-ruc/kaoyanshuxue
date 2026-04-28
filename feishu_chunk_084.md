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


