---

**2019年第21题 | 解答题 | 11分**
21. (本题满分11分)

已知函数 f(x)在[0,1]上具有2阶导数，且<equation>f(0)=0,f(1)=1,\int_{0}^{1} f(x)\mathrm{d} x=1</equation>，证明：

I. 存在<equation>\xi \in(0,1)</equation>，使得<equation>f^{\prime}(\xi)=0;</equation>II. 存在<equation>\eta \in(0,1)</equation>，使得<equation>f^{\prime\prime}(\eta)<-2</equation>
**答案: **（I）证明略；

（Ⅱ）证明略.
**解析: **证（I）（法一）构造辅助函数<equation>F ( x )=\int_{0}^{x} f ( t ) \mathrm{d} t</equation>，则<equation>F ( 0 )=0,F ( 1 )=\int_{0}^{1} f ( x ) \mathrm{d} x=1.</equation>由拉格朗日中值定理可得，存在<equation>c \in(0,1)</equation>，使得<equation>F^{\prime}(c)=1</equation>即<equation>f(c)=1.</equation>再对<equation>[c,1]</equation>上的<equation>f(x)</equation>使用罗尔定理可得，存在<equation>\xi\in(c,1)\subseteq(0,1)</equation>，使得<equation>f^{\prime}(\xi)=0.</equation>（法二）反证法.

由 f(x)在[0,1]上存在2阶导数可知<equation>f^{\prime}(x)</equation>在[0,1]上连续.若不存在<equation>\xi \in(0,1)</equation>，使得<equation>f^{\prime}(\xi)=0</equation>，则由<equation>f^{\prime}(x)</equation>的连续性以及零点定理可知，<equation>f^{\prime}(x)</equation>在(0,1)上恒大于零或恒小于零.

又因为<equation>f(0)=0</equation><equation>f(1)=1</equation>，所以<equation>f^{\prime}(x)</equation>恒大于零，<equation>f(x)</equation>在[0,1]上单调增加. f(1)是f(x)在 [0,1]上的最大值.于是，<equation>\int_ {0} ^ {1} f (x) \mathrm {d} x < \int_ {0} ^ {1} f (1) \mathrm {d} x = 1.</equation>这与<equation>\int_{0}^{1} f ( x ) \mathrm{d} x=1</equation>矛盾.

因此，存在<equation>\xi\in(0,1)</equation>，使得<equation>f^{\prime}(\xi)=0.</equation>（法三）证明 f(x)在[0,1]上的最大值大于1.

假设不然，则对于任意的<equation>x\in[0,1]</equation>，都有<equation>f(x)\leqslant 1</equation>，从而<equation>\int_{0}^{1}f(x)\mathrm{d}x\leqslant 1.</equation>又因为<equation>f(0)=0,f(1)=1</equation>所以由 f(x)的连续性可知，存在<equation>\delta >0</equation>，使得当<equation>x\in(0,\delta)</equation>时，<equation>f(x) < 1.</equation>于是，<equation>\int_{0}^{1}f(x)\mathrm{d}x < 1.</equation>这与<equation>\int_{0}^{1} f(x)\mathrm{d}x=1</equation>矛盾.假设不正确.

因此，<equation>f ( x )</equation>在[0,1]上的最大值大于1.如图（a）所示，记该点为<equation>\xi</equation>，由于<equation>f ( 0 )=0,f ( 1 )=1</equation>故<equation>\xi \in(0,1).</equation><equation>f ^ {\prime} (\xi) = 0.</equation>(a)

(b)

（Ⅱ）（法一）构造辅助函数<equation>G ( x )=f ( x )+x^{2}</equation>，于是 G(x)在[0,1]上2阶可导，且<equation>G^{\prime \prime} ( x )=f^{\prime \prime} ( x )+2.</equation>取 c为第（I）问中满足<equation>f ( c )=1</equation>的点，则<equation>G ( 0 )=0,G ( c )=1+c^{2},G ( 1 )=2.</equation>由拉格朗日中值定理可得，存在<equation>\eta_{1}\in (0,c)</equation>，使得<equation>G ^ {\prime} \left(\eta_ {1}\right) = \frac {G (c) - G (0)}{c - 0} = \frac {1 + c ^ {2}}{c}.</equation>存在<equation>\eta_{2}\in(c,1)</equation>，使得<equation>G ^ {\prime} \left(\eta_ {2}\right) = \frac {G (1) - G (c)}{1 - c} = \frac {1 - c ^ {2}}{1 - c} = 1 + c.</equation>再对<equation>[\eta_{1},\eta_{2} ]</equation>上的<equation>G^{\prime}(x)</equation>使用拉格朗日中值定理，可得存在<equation>\eta\in(\eta_{1},\eta_{2})\subseteq(0,1)</equation>，使得<equation>G ^ {\prime \prime} (\eta) = \frac {G ^ {\prime} \left(\eta_ {2}\right) - G ^ {\prime} \left(\eta_ {1}\right)}{\eta_ {2} - \eta_ {1}} = \frac {1 + c - \frac {1 + c ^ {2}}{c}}{\eta_ {2} - \eta_ {1}} = \frac {1 - \frac {1}{c}}{\eta_ {2} - \eta_ {1}}.</equation>由于<equation>c\in (0,1)</equation>，故<equation>1 - \frac{1}{c} < 0</equation>，从而<equation>G^{\prime \prime}(\eta) < 0</equation>，即<equation>f^{\prime \prime}(\eta) + 2 < 0</equation>，也即<equation>f^{\prime \prime}(\eta) < -2.</equation>（法二）构造二次函数<equation>g ( x )=a x^{2}+b x+c</equation>，使得<equation>g ( 0 )=f ( 0 )=0,g ( 1 )=f ( 1 )=1</equation>且<equation>\int_{0}^{1} g ( x ) \mathrm{d} x=\int_{0}^{1} f ( x ) \mathrm{d} x=1.</equation>由 g（0）=0可得 c=0.由 g（1）=1可得 a+b=1.又由<equation>\int_{0}^{1} g(x)\mathrm{d}x=1</equation>可得<equation>\frac{a}{3}+\frac{b}{2}=1</equation>即<equation>2a+3b=6.</equation>解得 a=-3,b=4.于是，令 g(x）=-3x²+4x. f(x)与 g(x)的图形如图（b）所示.

考虑<equation>G ( x ) = f ( x ) - g ( x )</equation>，则<equation>G ( 0 ) = 0, G ( 1 ) = 0, \int_{0}^{1} G ( x ) \mathrm{d} x = 0</equation>，且<equation>G^{\prime \prime}(x) = f^{\prime \prime}(x) + 6.</equation>下面我们证明，存在<equation>\eta\in(0,1)</equation>，使得<equation>G^{\prime\prime}(\eta)=0</equation>，即<equation>f^{\prime\prime}(\eta)=-6<-2.</equation>令<equation>H ( x )=\int_{0}^{x} G ( t ) \mathrm{d} t</equation>，则<equation>H ( 0 )=0,H ( 1 )=0.</equation>由拉格朗日中值定理可得，存在<equation>k \in(0,1)</equation>使得<equation>H^{\prime}(k)=0</equation>即<equation>G(k)=0.</equation>从而，<equation>G(0)=G(k)=G(1)=0.</equation>分别对<equation>[0,k],[k,1]</equation>上的<equation>G(x)</equation>使用罗尔定理，可得存在<equation>\eta_{1}\in(0,k),\eta_{2}\in(k,1)</equation>，使得<equation>G^{\prime}(\eta_{1})=0,G^{\prime}(\eta_{2})=0.</equation>再对<equation>[\eta_{1},\eta_{2}]</equation>上的<equation>G^{\prime}(x)</equation>使用罗尔定理，可得存在<equation>\eta \in (\eta_{1},\eta_{2})\subseteq (0,1)</equation>，使得<equation>G^{\prime \prime}(\eta) = 0</equation>，即<equation>f^{\prime \prime}(\eta) = -6 < -2.</equation>

---

**2015年第21题 | 解答题 | 11分**
21. (本题满分10分)

已知函数 f(x)在区间<equation>[ a,+\infty)</equation>上具有2阶导数，<equation>f ( a )=0, f^{\prime} ( x )>0, f^{\prime\prime} ( x )>0.</equation>设 b>a，曲线 y=f(x)在点 （b,f(b)）处的切线与x轴的交点是<equation>( x_{0},0)</equation>，证明 a<x0<b.
**答案: **## (21) 证明略.
**解析: **证 首先，由于过点（b，f(b)）的切线的斜率为<equation>f^{\prime}(b)</equation>，且该切线过点（<equation>x_{0},0)</equation>，故<equation>f^{\prime}(b)=\frac{f(b)-0}{b-x_{0}}</equation>，解得<equation>x_{0}=b-\frac{f(b)}{f^{\prime}(b)}。</equation>因为<equation>b > a, f^{\prime}(x) > 0, f(x)</equation>在<equation>[a, + \infty)</equation>上单调增加，所以<equation>f(b) > f(a)=0</equation>，从而<equation>\frac{f(b)}{f^{\prime}(b)} > 0.</equation>因此，<equation>x _ {0} = b - \frac {f (b)}{f ^ {\prime} (b)} < b.</equation>如图（a）所示，记点<equation>A</equation>为<equation>(a,f(a))</equation>，点<equation>B</equation>为<equation>(b,f(b))</equation>.

下面我们用两种方法证明<equation>a < x_{0}。</equation>(a)

(b)

（法一）由拉格朗日中值定理可得，存在<equation>\xi\in(a,b)</equation>，使得<equation>f^{\prime}(\xi)(b-a)=f(b)-f(a)</equation>，即弦AB的斜率等于曲线弧<equation>\widehat{AB}</equation>上某点<equation>(\xi,f(\xi))</equation>处的切线斜率<equation>f^{\prime}(\xi).</equation>由于<equation>f^{\prime\prime}(x)>0</equation>，故<equation>f^{\prime}(x)</equation>在<equation>[a,+\infty)</equation>上为单调增加函数，从而<equation>f^{\prime}(\xi)<f^{\prime}(b).</equation><equation>\frac {f (b) - f (a)}{b - a} = f ^ {\prime} (\xi) < f ^ {\prime} (b) = \frac {f (b) - 0}{b - x _ {0}}.</equation>代入<equation>f ( a ) = 0</equation>，得<equation>\frac{f ( b )}{b - a} < \frac{f ( b )}{b - x_0}.</equation>由于<equation>b - a > 0, b - x_0 > 0, f ( b ) > 0</equation>，故<equation>b - a > b - x_0</equation>，即<equation>a < x_0.</equation>（法二）要证<equation>x_{0} > a</equation>，即要证<equation>x_{0}=b-\frac{f(b)}{f^{\prime}(b)} > a.</equation>整理该不等式得<equation>b - \frac {f (b)}{f ^ {\prime} (b)} > a \xleftrightarrow {f ^ {\prime} (b) > 0} (b - a) f ^ {\prime} (b) - f (b) > 0.</equation>该不等式的几何意义为过点（a，0），斜率为<equation>f^{\prime}(b)</equation>的直线l在 x=b的纵坐标大于f(b).我们可证明在（a，b]上，直线l位于曲线 y=f(x）之上，如图（b）.

记<equation>g ( x )=f^{\prime} ( b ) ( x-a )</equation>，直线 l的方程为<equation>y=g ( x ).</equation>要证在（a,b]上，直线 l位于曲线<equation>y=f(x)</equation>之上，即要证当<equation>x\in(a,b]</equation>时，<equation>g ( x )-f ( x ) > 0.</equation>由拉格朗日中值定理，有<equation>f ( x ) = f ( a ) + f^{\prime} ( \xi_{x} ) ( x - a )</equation>，这里<equation>x \in(a,b]</equation><equation>\xi_{x} \in(a,x).</equation>从而<equation>g ( x ) - f ( x ) = f^{\prime} ( b ) ( x - a ) - f ( a ) - f^{\prime} ( \xi_{x} ) ( x - a)\frac{f ( a ) = 0}{=} \left[ f^{\prime} ( b ) - f^{\prime} ( \xi_{x} ) \right] ( x - a).</equation>由于对任意的<equation>x \in(a,b]</equation>，都有<equation>\xi_{x} < b</equation>，而<equation>f^{\prime\prime}(x)>0</equation><equation>f^{\prime}(x)</equation>在[a,b]上单调增加，故<equation>f ^ {\prime} (b) - f ^ {\prime} \left(\xi_ {x}\right) > 0.</equation>因此，<equation>g ( x ) - f ( x )</equation>在（a，b]上恒大于零.特别地，<equation>g ( b ) - f ( b ) > 0</equation>即<equation>f^{\prime} ( b ) ( b - a ) - f ( b ) > 0</equation><equation>x_{0}>a.</equation>综上所述，<equation>a < x_{0} < b.</equation>

---

**2013年第18题 | 解答题 | 10分**
8. (本题满分10分)

设奇函数 f(x)在<equation>[-1,1]</equation>上具有2阶导数，且 f(1)=1.证明：

I. 存在<equation>\xi \in(0,1)</equation>，使得<equation>f^{\prime}(\xi)=1;</equation>II. 存在<equation>\eta \in(-1,1)</equation>，使得<equation>f^{\prime\prime}(\eta)+f^{\prime}(\eta)=1.</equation>
**答案: **（18）（I）证明略；

（Ⅱ）证明略.
**解析: **证（I）由 f(x)为奇函数得 f(0)=0.由于 f(1)=1，且 f(x)在[-1,1]上可导，故由拉格朗日中值定理得，存在<equation>\xi \in(0,1)</equation>，使得<equation>f(1)-f(0)=f^{\prime}(\xi)</equation>，即<equation>f^{\prime}(\xi)=1.</equation>（Ⅱ）（法一）构造辅助函数<equation>g ( x )=f^{\prime} ( x )+f ( x )-x. g ( x )</equation>在[-1，1]上可导.

若能在[-1，1]上找到两个点<equation>x_{1}, x_{2}</equation>，使得<equation>g(x_{1})=g(x_{2})</equation>，则由罗尔定理可得，存在<equation>\eta \in</equation>（-1，1），<equation>g^{\prime}(\eta)=0</equation>，即<equation>f^{\prime\prime}(\eta)+f^{\prime}(\eta)=1.</equation>由于 f(x）是<equation>[-1,1]</equation>上的奇函数，故<equation>f(x)=-f(-x).</equation>该等式两端同时关于 x求导得<equation>f^{\prime}(x)=</equation><equation>f^{\prime}(-x).</equation>于是<equation>f^{\prime}(x)</equation>是<equation>[-1,1]</equation>上的偶函数.从而，<equation>g (1) = f ^ {\prime} (1) + f (1) - 1, \quad g (- 1) = f ^ {\prime} (- 1) + f (- 1) - (- 1) = f ^ {\prime} (1) - f (1) + 1.</equation>由于<equation>f(1) - 1 = 0</equation>，故<equation>g(1) = g(-1)</equation>由罗尔定理可知，存在<equation>\eta \in (-1,1)</equation>，<equation>g^{\prime}(\eta) = 0</equation>，即<equation>f^{\prime \prime}(\eta) + f^{\prime}(\eta) = 1.</equation>（法二）构造辅助函数<equation>G ( x ) = \mathrm{e}^{x} \left[ f^{\prime} ( x )-1 \right]. G ( x )</equation>在[-1，1]上可导.<equation>G ^ {\prime} (x) = \mathrm {e} ^ {x} \left[ f ^ {\prime} (x) - 1 \right] + \mathrm {e} ^ {x} f ^ {\prime \prime} (x) = \mathrm {e} ^ {x} \left[ f ^ {\prime \prime} (x) + f ^ {\prime} (x) - 1 \right].</equation>由于<equation>f ( x )</equation>是<equation>[-1,1]</equation>上的奇函数，同法一中的论证可知<equation>f^{\prime}(x)</equation>是<equation>[-1,1]</equation>上的偶函数.<equation>\xi</equation>为第（I）问中所得，满足<equation>f^{\prime}(\xi)=1</equation>，从而<equation>f^{\prime}(-\xi)=f^{\prime}(\xi)=1.</equation>因此<equation>G(\xi)=G(-\xi)=0.</equation>由罗尔定理，存在<equation>\eta\in(-1,1)</equation>，使得<equation>G^{\prime}(\eta)=0</equation>.又因为<equation>\mathrm{e}^{\eta}>0</equation>，所以<equation>f^{\prime\prime}(\eta)+f^{\prime}(\eta)-1=0</equation>，即<equation>f^{\prime\prime}(\eta)+f^{\prime}(\eta)=1.</equation>

---

**2010年第21题 | 解答题 | 11分**
21. (本题满分10分)

假设函数 f(x)在闭区间[0,1]上连续，在开区间（0，1）内可导，且 f(0)=0，f(1)=<equation>\frac{1}{3}</equation>.证明：存在<equation>\xi \in\left(0,\frac{1}{2}\right),\eta \in</equation><equation>\left(\frac{1}{2},1\right)</equation>，使得：<equation>f^{\prime}(\xi)+f^{\prime}(\eta)=\xi^{2}+\eta^{2}.</equation>
**解析: **证构造辅助函数<equation>g ( x )=f ( x )-\frac{1}{3} x^{3}</equation>，则 g(x)在[0，1]上连续，(0，1)内可导，<equation>g^{\prime} ( x )=</equation><equation>f^{\prime} ( x )-x^{2}.</equation>，于是，所要证的结论变为“存在<equation>\xi\in\left(0,\frac{1}{2}\right),\eta\in\left(\frac{1}{2},1\right)</equation>，使得<equation>g^{\prime} (\xi)+g^{\prime} (\eta)=0.</equation>”首先，由题设，有<equation>g ( 0 )=f ( 0 )=0</equation>，<equation>g ( 1 )=f ( 1 )-\frac{1}{3}=0.</equation>分别在<equation>\left[0,\frac{1}{2}\right]</equation>和<equation>\left[\frac{1}{2},1\right]</equation>上对 g(x)使用拉格朗日中值定理可得，存在<equation>\xi\in\left(0,\frac{1}{2}\right),\eta\in</equation><equation>\left(\frac{1}{2},1\right)</equation>，使得<equation>g \left(\frac {1}{2}\right) - g (0) = \frac {1}{2} g ^ {\prime} (\xi), \quad g (1) - g \left(\frac {1}{2}\right) = \frac {1}{2} g ^ {\prime} (\eta).</equation>由（1）式，得<equation>g ( 1 ) - g ( 0 ) = \frac { 1 } { 2 } \left[ g^{\prime} ( \xi ) + g^{\prime} ( \eta ) \right]</equation>.又因为<equation>g ( 0 ) = g ( 1 ) = 0</equation>，所以<equation>g^{\prime} (\xi) + g^{\prime} (\eta) = 0</equation>即<equation>f^{\prime} (\xi) + f^{\prime} (\eta) = \xi^{2} + \eta^{2}.</equation>

---

**2009年第21题 | 解答题 | 11分**

I. 证明拉格朗日中值定理：若函数 f(x)在<equation>[a,b]</equation>上连续，在（a,b）内可导，则存在点<equation>\xi\in(a,b)</equation>，使得<equation>f(b)-f(a)=f^{\prime}(\xi)(b-a).</equation>II. 证明：若函数 f(x)在 x=0处连续，在<equation>(0,\delta)(\delta>0)</equation>内可导，且<equation>\lim_{x\rightarrow 0^{+}}f^{\prime}(x)=A</equation>，则<equation>f_{+}^{\prime}(0)</equation>存在，且<equation>f_{+}^{\prime}(0)=A.</equation>
**答案: **（21）（Ⅰ）证明略.

（Ⅱ）证明略.
**解析: **证（ I ）令<equation>\varphi (x) = f (x) - f (a) - \frac {f (b) - f (a)}{b - a} (x - a).</equation><equation>\varphi (x)</equation>在<equation>[a,b]</equation>上连续，在<equation>(a,b)</equation>内可导.计算得<equation>\varphi (a) = 0,\varphi (b) = 0.</equation>对<equation>\varphi(x)</equation>使用罗尔定理得，存在<equation>\xi\in(a,b)</equation>，使得<equation>\varphi^{\prime}(\xi)=0</equation>，即<equation>f^{\prime}(\xi)-\frac{f(b)-f(a)}{b-a}=0.</equation>因此，存在<equation>\xi\in(a,b)</equation>，使得<equation>f(b)-f(a)=f^{\prime}(\xi)(b-a).</equation>（Ⅱ）（法一）根据右侧导数的定义，<equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x}.</equation>由拉格朗日中值定理，对任意的<equation>x\in (0,\delta)</equation>，都存在<equation>\xi_{x}\in (0,x)</equation>，使得<equation>f (x) - f (0) = f ^ {\prime} \left(\xi_ {x}\right) x.</equation>从而<equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x} = \lim _ {x \rightarrow 0 ^ {+}} \frac {f ^ {\prime} \left(\xi_ {x}\right) x}{x} = \lim _ {0 < \xi_ {x} < x, \atop x \rightarrow 0 ^ {+}} f ^ {\prime} \left(\xi_ {x}\right).</equation>由于<equation>x\to 0^{+}</equation>，故<equation>\xi_{x}\to 0^{+}</equation>.因此，<equation>f _ {+} ^ {\prime} (0) = \lim _ {0 < \xi_ {x} < x, x \rightarrow 0 ^ {+}} f ^ {\prime} \left(\xi_ {x}\right) = \lim _ {x \rightarrow 0 ^ {+}} f ^ {\prime} (x) = A.</equation>（法二）由洛必达法则，<equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {f ^ {\prime} (x)}{1} = A.</equation>因此，<equation>f_{+}^{\prime}(0)</equation>存在，且等于A.

---


#### 导数的应用


**2024年第11题 | 填空题 | 5分**
11. 曲线<equation>y^{2}=x</equation>在点(0,0)处的曲率圆方程为 ___
**答案: **<equation>\left(x - \frac {1}{2}\right) ^ {2} + y ^ {2} = \frac {1}{4}</equation>
**解析: **解曲线<equation>y^{2}=x</equation>的参数方程可写为<equation>\left\{\begin{array}{l l}x=y^{2},\\ y=y,\end{array}\right.</equation>故<equation>\frac{\mathrm{d}x}{\mathrm{d}y}=2y,\frac{\mathrm{d}^{2}x}{\mathrm{d}y^{2}}=2,\frac{\mathrm{d}y}{\mathrm{d}y}=1,\frac{\mathrm{d}^{2}y}{\mathrm{d}y^{2}}=0</equation>曲线上点 （x,y）处的曲率<equation>K=\frac{\left|2y\cdot0-2\cdot1\right|}{\left[(2y)^{2}+1^{2}\right]^{\frac{3}{2}}}=\frac{2}{\left(4y^{2}+1\right)^{\frac{3}{2}}}.</equation>(1)

由（1）式可得，点（0,0）处的曲率<equation>K=\frac{2}{(0+1)^{\frac{3}{2}}}=2</equation>，故该点处的曲率半径为<equation>\frac{1}{K}=\frac{1}{2}.</equation>由于曲线在点（0,0）处的切线为y轴，故法线为x轴，曲率中心在点<equation>\left(\frac{1}{2},0\right).</equation>因此，所求曲率圆方程为<equation>\left(x-\frac{1}{2}\right)^{2}+y^{2}=\frac{1}{4}.</equation>

---

**2024年第15题 | 填空题 | 5分**
15. 设某物体以速度<equation>v ( t )=t+k \sin \pi t</equation>做直线运动. 若它从 t=0到 t=3的时间段内平均速度是<equation>\frac{5}{2}</equation>，则 k=___
**答案: **##<equation>\frac{3}{2}\pi</equation>
**解析: **解 由函数的平均值的定义可知，物体从 t=0到 t=3的时间段内平均速度<equation>\bar{v} ( t )=\frac{\int_{0}^{3} v ( t ) \mathrm{d} t}{3}.</equation>于是，由平均速度为<equation>\frac{5}{2}</equation>可得<equation>\frac {\int_ {0} ^ {3} v (t) \mathrm {d} t}{3} = \frac {5}{2}, \quad \text {即} \int_ {0} ^ {3} (t + k \sin \pi t) \mathrm {d} t = \frac {1 5}{2}.</equation>由于<equation>\int_ {0} ^ {3} \left(t + k \sin \pi t\right) \mathrm {d} t = \left(\frac {t ^ {2}}{2} - \frac {k}{\pi} \cos \pi t\right) \Bigg | _ {0} ^ {3} = \frac {9}{2} - \frac {k}{\pi} (- 1 - 1) = \frac {9}{2} + \frac {2 k}{\pi},</equation>故由（1）式可得<equation>\frac{9}{2} +\frac{2k}{\pi} = \frac{15}{2}</equation>，解得<equation>k = \frac{3\pi}{2}</equation>

---

**2023年第14题 | 填空题 | 5分**
14. 曲线<equation>3 x^{3}=y^{5}+2 y^{3}</equation>在<equation>x=1</equation>对应点处的法线斜率为 ___
**答案: **# 11 9
**解析: **解记<equation>f ( y )=y^{5}+2 y^{3}-3</equation>，则<equation>f ( 1 )=0</equation>.又因为<equation>f^{\prime}(y)=5 y^{4}+6 y^{2}\geqslant 0</equation>，所以f(y）单调增加，<equation>y=1</equation>是f(y）的唯一零点.由于当且仅当 x=1时，<equation>3 x^{3}=3</equation>，故当且仅当 y=1时，x=1，从而曲线<equation>3 x^{3}=y^{5}+2 y^{3}</equation>在 x=1处的对应点为点（1,1）.

对方程<equation>3 x^{3}=y^{5}+2 y^{3}</equation>两端关于 x求导，可得<equation>9 x ^ {2} = \left(5 y ^ {4} + 6 y ^ {2}\right) y ^ {\prime}.</equation>将<equation>x = 1,y = 1</equation>代入（1）式，可得<equation>9 = 11y^{\prime}</equation>.因此，<equation>y^{\prime}(1) = \frac{9}{11}</equation>即<equation>x = 1</equation>对应点处的切线斜率为<equation>\frac{9}{11}</equation>.

由于同一点处的切线与法线相互垂直，此时切线斜率与法线斜率的乘积为-1，故 x=1对应点处的法线斜率为<equation>-\frac{11}{9}.</equation>

---

**2021年第3题 | 选择题 | 5分 | 答案: C**
3. 有一圆柱体，底面半径与高随时间的变化率分别为<equation>2 \mathrm{~cm} / \mathrm{s},-3 \mathrm{~cm} / \mathrm{s}</equation>，当底面半径为10cm，高为5cm时，圆体的体积与表面积随时间的变化速率为（    )

A.<equation>1 2 5 \pi \mathrm{c m}^{3} / \mathrm{s},4 0 \pi \mathrm{c m}^{2} / \mathrm{s}</equation>B.<equation>1 2 5 \pi \mathrm{c m}^{3} / \mathrm{s},-4 0 \pi \mathrm{c m}^{2} / \mathrm{s}</equation>C.<equation>- 1 0 0 \pi \mathrm{c m}^{3} / \mathrm{s},4 0 \pi \mathrm{c m}^{2} / \mathrm{s}</equation>D.<equation>- 1 0 0 \pi \mathrm{c m}^{3} / \mathrm{s},-4 0 \pi \mathrm{c m}^{2} / \mathrm{s}</equation>
答案: C
**解析: **解设圆柱体的底面半径为 r(t)，高为 h(t)，则圆柱体的体积<equation>V ( t )=\pi r^{2} ( t ) h ( t )</equation>，表面积<equation>S ( t )=2 \pi r ( t ) h ( t )+2 \pi r^{2} ( t ).</equation>由链式法则，<equation>\frac {\mathrm {d} V}{\mathrm {d} t} = \frac {\partial V}{\partial r} \frac {\mathrm {d} r}{\mathrm {d} t} + \frac {\partial V}{\partial h} \frac {\mathrm {d} h}{\mathrm {d} t} = 2 \pi r h \frac {\mathrm {d} r}{\mathrm {d} t} + \pi r ^ {2} \frac {\mathrm {d} h}{\mathrm {d} t}.</equation><equation>\frac {\mathrm {d} S}{\mathrm {d} t} = \frac {\partial S}{\partial r} \frac {\mathrm {d} r}{\mathrm {d} t} + \frac {\partial S}{\partial h} \frac {\mathrm {d} h}{\mathrm {d} t} = (2 \pi h + 4 \pi r) \frac {\mathrm {d} r}{\mathrm {d} t} + 2 \pi r \frac {\mathrm {d} h}{\mathrm {d} t}.</equation>代入 r=10 cm,h=5 cm<equation>\frac{\mathrm{d} r}{\mathrm{d} t}=2 \mathrm{~ c m / s}, \frac{\mathrm{d} h}{\mathrm{d} t}=-3 \mathrm{~ c m / s}</equation>可得<equation>\frac {\mathrm {d} V}{\mathrm {d} t} = 2 \pi \times 1 0 \times 5 \times 2 + \pi \times 1 0 0 \times (- 3) = 2 0 0 \pi - 3 0 0 \pi = - 1 0 0 \pi \left(\mathrm {c m} ^ {3} / \mathrm {s}\right).</equation><equation>\frac {\mathrm {d} S}{\mathrm {d} t} = \left(2 \pi \times 5 + 4 \pi \times 1 0\right) \times 2 + 2 \pi \times 1 0 \times (- 3) = 1 0 0 \pi - 6 0 \pi = 4 0 \pi \left(\mathrm {c m} ^ {2} / \mathrm {s}\right).</equation>因此，应选C.

---

**2019年第6题 | 选择题 | 4分 | 答案: A**
6. 已知 f(x), g(x)二阶可导，且2阶导函数在 x=a处连续，则<equation>\lim_{x\rightarrow a}\frac{f(x)-g(x)}{(x-a)^{2}}=0</equation>是曲线 y=f(x)和 y=g(x)在 x=a对应的点处相切且曲率相等的（    ）

A. 充分非必要条件 B. 充分必要条件

C. 必要非充分条件 D. 既非充分又非必要条件
答案: A
**解析: **解 由<equation>f ( x )</equation>，<equation>g ( x )</equation>在<equation>x=a</equation>处的二阶泰勒公式可得，<equation>f (x) = f (a) + f ^ {\prime} (a) (x - a) + \frac {f ^ {\prime \prime} (a)}{2} (x - a) ^ {2} + o \left(\left(x - a\right) ^ {2}\right),</equation><equation>g (x) = g (a) + g ^ {\prime} (a) (x - a) + \frac {g ^ {\prime \prime} (a)}{2} (x - a) ^ {2} + o \left(\left(x - a\right) ^ {2}\right).</equation>代入<equation>\lim_{x\to a}\frac{f(x) - g(x)}{(x - a)^2}</equation>可得，<equation>\lim_{x\to a}\frac{f(x) - g(x)}{(x - a)^2} = \lim_{x\to a}\frac{[f(a) - g(a)] + [f'(a) - g'(a)](x - a) + \frac{f''(a) - g''(a)}{2}(x - a)^2 + o((x - a)^2)}{(x - a)^2}.</equation>由上式可知<equation>\lim_{x\to a}\frac{f(x) - g(x)}{(x - a)^2} = 0</equation>当且仅当<equation>\left\{ \begin{array}{l} f(a) = g(a), \\ f'(a) = g'(a), \\ f''(a) = g''(a). \end{array} \right.</equation>曲线<equation>y=f(x)</equation>与<equation>y=g(x)</equation>在<equation>x=a</equation>对应的点处相切当且仅当<equation>\left\{ \begin{array}{l l} f(a)=g(a), \\ f^{\prime}(a)=g^{\prime}(a). \end{array} \right.</equation>又由曲率的计算公式<equation>K=\frac{\left|y^{\prime \prime}\right|}{\left[1+(y^{\prime})^{2}\right]^{\frac{3}{2}}}</equation>以及<equation>f^{\prime \prime}(a)=g^{\prime \prime}(a)</equation>可得两条曲线在<equation>x=a</equation>对应的点处曲率相等.

因此，<equation>\lim_{x\to a}\frac{f(x)-g(x)}{(x-a)^{2}}=0</equation>是曲线 y=f(x）和 y=g(x）在 x=a对应的点处相切且曲率相等的充分条件.

注意到两曲线在 x=a对应的点处曲率相等只能说明<equation>|f^{\prime \prime}(a)|=|g^{\prime \prime}(a)|</equation>，但并不能推出<equation>f^{\prime \prime}(a)=g^{\prime \prime}(a)</equation>，故<equation>\lim_{x\to a}\frac{f(x)-g(x)}{(x-a)^{2}}=0</equation>不是曲线 y=f(x)和 y=g(x)在 x=a对应的点处相切且曲率相等的必要条件.

例如：取<equation>f ( x )=1-\sqrt{1-x^{2}}</equation><equation>g ( x )=-1+\sqrt{1-x^{2}}</equation><equation>y=f(x), y=g(x)</equation>这两条曲线均为半径为1的半圆弧（圆弧上各点的曲率半径均为1）.于是，各点处曲率相等，均等于1.如图所示，这两条曲线在原点处相切，但<equation>y=f(x)</equation>在[-1，1]上是凹曲线，<equation>y=g(x)</equation>在[-1，1]上是凸曲线，<equation>f^{\prime \prime}(0)\neq g^{\prime \prime}(0).</equation>综上所述，应选A.

---

**2019年第10题 | 填空题 | 4分**
10. 曲线<equation>\left\{ \begin{array}{l} x = t - \sin t \\ y = 1 - \cos t \end{array} \right.</equation>在<equation>t=\frac{3\pi}{2}</equation>对应点处的切线在 y 轴上的截距为 ___
**答案: **#<equation>\frac{3\pi}{2}+2.</equation>
**解析: **分析 本题主要考查由参数方程确定的函数求导以及导数的几何意义.

如图所示，本题中的曲线为摆线，可利用由参数方程确定的函数求导计算<equation>t=\frac{3\pi}{2}</equation>对应点处的导数值，从而得到该点处的切线方程，再计算该切线在 y轴上的截距.

解 计算<equation>t=\frac{3\pi}{2}</equation>对应点处的导数值.<equation>\left. \frac {\mathrm {d} y}{\mathrm {d} x} \right| _ {t = \frac {3 \pi}{2}} = \left. \frac {\mathrm {d} y}{\mathrm {d} t} \right| / \left. \frac {\mathrm {d} x}{\mathrm {d} t} \right| _ {t = \frac {3 \pi}{2}} = \left. \frac {\sin t}{1 - \cos t} \right| _ {t = \frac {3 \pi}{2}} = \frac {- 1}{1} = - 1.</equation>当 t =<equation>\frac{3\pi}{2}</equation>时，x =<equation>\frac{3\pi}{2}+1</equation>，y=1.于是，该点处的切线方程为 y-1=-<equation>\left(x-\frac{3\pi}{2}-1\right).</equation>令 x=0，可得 y =<equation>\frac{3\pi}{2}+2.</equation>因此，所求截距为<equation>\frac{3\pi}{2}+2.</equation>

---

**2018年第12题 | 填空题 | 4分**
12. 曲线<equation>\left\{ \begin{array}{l} x = \cos^ {3} t \\ y = \sin^ {3} t \end{array} \right.</equation>
**答案: **# 2 3.
**解析: **解分别计算<equation>\frac{\mathrm{d} y}{\mathrm{d} x},\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}.</equation><equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {3 \sin^ {2} t \cos t}{- 3 \cos^ {2} t \sin t} = - \tan t,</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\mathrm {d} \left(\frac {\mathrm {d} y}{\mathrm {d} x}\right)}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {- \sec^ {2} t}{- 3 \cos^ {2} t \sin t} = \frac {\sec^ {4} t}{3 \sin t}.</equation>当 t =<equation>\frac{\pi}{4}</equation>时，<equation>\left. \frac{\mathrm{d} y}{\mathrm{d} x}\right|_{t=\frac{\pi}{4}}=-1</equation><equation>\left. \frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\right|_{t=\frac{\pi}{4}}=\frac{(\sqrt{2})^{4}}{3\times \frac{\sqrt{2}}{2}}=\frac{4\sqrt{2}}{3}</equation>根据曲率的计算公式，所求曲率<equation>= \frac{\frac{4\sqrt{2}}{3}}{\left[ 1+(-1)^{2}\right]^{\frac{3}{2}}}=\frac{4\sqrt{2}}{3}\bigg /2\sqrt{2}=\frac{2}{3}.</equation>

---

**2016年第13题 | 填空题 | 4分**
13. 已知动点 P在曲线<equation>y=x^{3}</equation>上运动，记坐标原点与点 P间的距离为 l. 若点 P的横坐标对时间的变化率为常数<equation>v_{0}</equation>，则当点 P运动到点（1,1）时，l对时间的变化率是 ___
**答案: **##<equation>2 \sqrt{2} v_{0}.</equation>
**解析: **解设点 P的坐标为<equation>( x,x^{3} )</equation>，则<equation>l=\sqrt{x^{2}+x^{6}}</equation>点 P的横坐标对时间的变化率为<equation>\frac{\mathrm{d} x}{\mathrm{d} t}=v_{0}.</equation>记 l对时间的变化率为<equation>\frac{\mathrm{d} l}{\mathrm{d} t}.</equation>由链式法则得<equation>\frac {\mathrm {d} l}{\mathrm {d} t} = \frac {\mathrm {d} l}{\mathrm {d} x} \cdot \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {1}{2} \cdot \frac {6 x ^ {5} + 2 x}{\sqrt {x ^ {2} + x ^ {6}}} \cdot v _ {0}.</equation>当 x=1时，代入（1）式得<equation>\frac{\mathrm{d} l}{\mathrm{d} t}\bigg|_{x=1}=\frac{4}{\sqrt{2}} v_{0}=2\sqrt{2} v_{0}.</equation>

---

**2014年第4题 | 选择题 | 4分 | 答案: C**
4. 曲线<equation>\left\{\begin{array}{l l}x=t^{2}+7,\\y=t^{2}+4 t+1\end{array}\right.</equation>上对应于 t=1的点处的曲率半径是（    )

A.<equation>\frac{\sqrt{1 0}}{5 0}</equation>B.<equation>\frac{\sqrt{1 0}}{1 0 0}</equation>C.<equation>1 0 \sqrt{1 0}</equation>D.<equation>5 \sqrt{1 0}</equation>
答案: C
**解析: **解 先求对应于<equation>t = 1</equation>的点处的曲率，需要得到该点处的<equation>y^{\prime}, y^{\prime \prime}</equation>.<equation>\left. \frac {\mathrm {d} y}{\mathrm {d} x} \right| _ {t = 1} = \left. \frac {\mathrm {d} y}{\mathrm {d} t} \right/ \left. \frac {\mathrm {d} x}{\mathrm {d} t} \right| _ {t = 1} = \left. \frac {2 t + 4}{2 t} \right| _ {t = 1} = \left. \frac {t + 2}{t} \right| _ {t = 1} = 3,</equation><equation>\left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {t = 1} = \frac {\mathrm {d} \left(\frac {\mathrm {d} y}{\mathrm {d} x}\right)}{\mathrm {d} t} / \left. \frac {\mathrm {d} x}{\mathrm {d} t} \right| _ {t = 1} = \frac {- \frac {2}{t ^ {2}}}{2 t} \left| _ {t = 1} = - \frac {1}{t ^ {3}} \right| _ {t = 1} = - 1.</equation>因此，该点处的曲率半径<equation>\rho = \frac{1}{K} = \frac{[1 + (y^{\prime})^{2}]^{\frac{3}{2}}}{|y^{\prime \prime}|} = \frac{(1 + 3^{2})^{\frac{3}{2}}}{|-1|} = 10\sqrt{10}</equation>. 应选C.

---

**2014年第12题 | 填空题 | 4分**
12. 曲线<equation>L</equation>的极坐标方程是<equation>r=\theta</equation>, 则<equation>L</equation>在点<equation>(r,\theta)=\left(\frac{\pi}{2},\frac{\pi}{2}\right)</equation>处的切线的直角坐标方程是 ___
**答案: **<equation>\frac {2}{\pi} x + y - \frac {\pi}{2} = 0.</equation>
**解析: **解（法一）由<equation>\left\{\begin{array}{l l}x=r\cos \theta \\ y=r\sin \theta\end{array}\right.</equation>以及r=得，<equation>\left\{\begin{array}{l l}x=\theta\cos \theta \\ y=\theta\sin \theta.\end{array}\right.</equation>于是，根据由参数方程确定的函数的求导公式，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} \theta} / \frac {\mathrm {d} x}{\mathrm {d} \theta} = \frac {\sin \theta + \theta \cos \theta}{\cos \theta - \theta \sin \theta}.</equation>于是，<equation>\frac{\mathrm{d}y}{\mathrm{d}x}\bigg|_{\theta = \frac{\pi}{2}} = \frac{1 + 0}{0 - \frac{\pi}{2}} = -\frac{2}{\pi}.</equation>由坐标变换公式得，极坐标系下的点<equation>\left(\frac{\pi}{2},\frac{\pi}{2}\right)</equation>对应直角坐标系下的点<equation>\left(0,\frac{\pi}{2}\right).</equation>因此，所求切线的点斜式方程为<equation>y-\frac{\pi}{2}=-\frac{2}{\pi} (x-0)</equation>即<equation>\frac{2}{\pi} x+y-\frac{\pi}{2}=0.</equation>（法二）曲线<equation>r = \theta</equation>是阿基米德螺线.这是一条光滑曲线.

由<equation>\left\{\begin{array}{l}x=r\cos \theta,\\ y=r\sin \theta\end{array}\right.</equation>可得，当<equation>\theta\in\left[0,\frac{\pi}{2}\right)</equation>时，<equation>r=\sqrt{x^{2}+y^{2}},</equation><equation>\theta=\arctan \frac{y}{x}.</equation>将该曲线方程写成直角坐标系下的形式，可得<equation>\sqrt{x^{2}+y^{2}}=\arctan \frac{y}{x}</equation>即当<equation>\theta\in\left[0,\frac{\pi}{2}\right)</equation>时，曲线<equation>r=\theta</equation>的直角坐标方程为<equation>\sqrt{x^{2}+y^{2}}=\arctan \frac{y}{x}.</equation>由（r，<equation>\theta)=\left(\frac{\pi}{2},\frac{\pi}{2}\right)</equation>得（x，y）<equation>=\left(0,\frac{\pi}{2}\right).</equation>虽然点<equation>\left(0,\frac{\pi}{2}\right)</equation>并不满足该方程，但由于曲线光滑，故该点处的斜率等于<equation>\lim_{x\to 0^{+}}y^{\prime}(x).</equation>对<equation>\sqrt{x^{2}+y^{2}}=\arctan \frac{y}{x}</equation>两端关于 x求导得<equation>\frac {2 x + 2 y y ^ {\prime}}{2 \sqrt {x ^ {2} + y ^ {2}}} = \frac {1}{1 + \left(\frac {y}{x}\right) ^ {2}} \cdot \frac {x y ^ {\prime} - y}{x ^ {2}}.</equation>化简得<equation>\frac {x y ^ {\prime} - y}{\sqrt {x ^ {2} + y ^ {2}}} = x ^ {-} + y y ^ {\prime}.</equation>由（1）式可得<equation>( x-y\sqrt{x^{2}+y^{2}}) y^{\prime}=x\sqrt{x^{2}+y^{2}}+y.</equation>令<equation>x\to0^{+}</equation>，并代入<equation>\lim_{x\to0^{+}}x=0,\lim_{x\to0^{+}}y(x)=\frac{\pi}{2}</equation>，可得<equation>\lim_{x\to0^{+}}y^{\prime}(x)=-\frac{2}{\pi}.</equation>因此，所求切线方程为<equation>y-\frac{\pi}{2}=- \frac{2}{\pi} x</equation>即<equation>\frac{2}{\pi} x+y-\frac{\pi}{2}=0.</equation>

---

**2013年第12题 | 填空题 | 4分**
12. 曲线<equation>\begin{aligned} x &= \arctan t, \\ y &= \ln \sqrt {1 + t ^ {2}} \end{aligned}</equation>上对应于<equation>t=1</equation>的点处的法线方程为 ___
**答案: **<equation>x+y=\frac{\pi}{4}+\frac{1}{2}\ln 2.</equation>
**解析: **曲线上对应于<equation>t = 1</equation>的点处的切线斜率为<equation>\left. \frac {\mathrm {d} y}{\mathrm {d} x} \right| _ {t = 1} = \frac {y ^ {\prime} (1)}{x ^ {\prime} (1)} = \frac {\frac {1}{2} \cdot \frac {2 t}{1 + t ^ {2}}}{\frac {1}{1 + t ^ {2}}} \Bigg | _ {t = 1} = 1,</equation>故曲线上对应于<equation>t=1</equation>的点处的法线斜率为-1.

又因为当 t=1时，<equation>x=\frac{\pi}{4}</equation><equation>y=\frac{1}{2}\ln 2</equation>，所以该法线过点<equation>\left(\frac{\pi}{4},\frac{1}{2}\ln 2\right)</equation>，从而可写出所求法线的点斜式方程<equation>y-\frac{1}{2}\ln 2=-\left(x-\frac{\pi}{4}\right)</equation>，即<equation>x+y=\frac{\pi}{4}+\frac{1}{2}\ln 2.</equation>

---

**2012年第13题 | 填空题 | 4分**
13. 曲线<equation>y=x^{2}+x \ ( x<0 )</equation>上曲率为<equation>\frac{\sqrt{2}}{2}</equation>的点的坐标是 ___
**答案: **## (-1,0).
**解析: **利用曲线方程可求得<equation>y^{\prime}=2 x+1</equation><equation>y^{\prime\prime}=2</equation>，故<equation>K = \frac {2}{\left[ 1 + \left(2 x + 1\right) ^ {2} \right] ^ {\frac {3}{2}}} = \frac {\sqrt {2}}{2}.</equation>由此可求得<equation>(2x + 1)^{2} = 1</equation>，故<equation>x = 0</equation>或<equation>x = -1</equation>.又因为<equation>x < 0</equation>，所以<equation>x = -1</equation>，此时<equation>y = 0</equation>因此，所求点的坐标为（-1，0）.

---

**2010年第3题 | 选择题 | 4分 | 答案: C**
3. 曲线<equation>y=x^{2}</equation>与曲线<equation>y=a\ln x \ (a\neq0)</equation>相切，则 a=（    ）

A. 4e B. 3e C. 2e D. e
答案: C
**解析: **解 若两曲线的公切点为<equation>\left(x_{0}, y_{0}\right)</equation>，则点<equation>\left(x_{0}, y_{0}\right)</equation>满足<equation>\left\{ \begin{array}{l} y _ {0} = x _ {0} ^ {2}, \\ y _ {0} = a \ln x _ {0} \\ 2 x _ {0} = \frac {a}{x _ {0}}. \end{array} \right.</equation>解上述方程组得，<equation>a=2\mathrm{e},\ x_{0}=\sqrt{\mathrm{e}},y_{0}=\mathrm{e}.</equation>应选C.

---

**2010年第13题 | 填空题 | 4分**
13. 已知一个长方形的长 l以 2 cm/s的速率增加，宽 w以 3 cm/s的速率增加，则当 l=12 cm，w=5 cm时，它的对角线增加的速率为___
**答案: **3 cm/s.
**解析: **解 设对角线长为 s（t），则<equation>s ^ {2} (t) = l ^ {2} (t) + w ^ {2} (t).</equation>等式两端同时关于 t 求导，得<equation>s \frac {\mathrm {d} s}{\mathrm {d} t} = l \frac {\mathrm {d} l}{\mathrm {d} t} + w \frac {\mathrm {d} w}{\mathrm {d} t}.</equation>当<equation>l = 12\mathrm{cm},w = 5\mathrm{cm}</equation>时，<equation>s = \sqrt{12^{2} + 5^{2}}\mathrm{cm} = 13\mathrm{cm}</equation>. 代入（1）式得<equation>1 3 \frac {\mathrm {d} s}{\mathrm {d} t} = 1 2 \times 2 + 5 \times 3.</equation>因此，<equation>\frac{\mathrm{d}s}{\mathrm{d}t}=3\mathrm{cm / s}.</equation>

---

**2009年第5题 | 选择题 | 4分 | 答案: B**
5. 若<equation>f^{\prime\prime}(x)</equation>不变号，且曲线<equation>y=f(x)</equation>在点（1，1）处的曲率圆为<equation>x^{2}+y^{2}=2</equation>，则函数 f(x)在区间（1，2）内（    ）

A. 有极值点，无零点 B. 无极值点，有零点 C. 有极值点，有零点 D. 无极值点，无零点
答案: B
**解析: **解（法一）由于曲线<equation>y=f(x)</equation>在点（1，1）附近的凹凸性与点 （1，1）处的曲率圆的凹凸性一致，而曲率圆为<equation>x^{2}+y^{2}=2</equation>，是凸曲线，故<equation>y^{\prime \prime}<0.</equation>考虑曲线在点（1，1）处的切线.

连接点（0，0）和点（1，1）的半径为点（1，1）处的法线，该法线斜率为<equation>\frac{1 - 0}{1 - 0} = 1</equation>，于是点（1，1）处的切线斜率为-1，即<equation>f^{\prime}(1) = -1.</equation>由于<equation>f^{\prime \prime}(x)</equation>不变号，故在区间（1，2）上，仍有<equation>f^{\prime \prime}(x)<0</equation>，从而<equation>f^{\prime}(x)</equation>在（1，2）上单调减少。又因为<equation>f^{\prime}(1)=-1<0</equation>，所以<equation>f^{\prime}(x)</equation>在（1，2）上恒小于零.于是 f(x)在（1，2）上单调减少.因此， f(x)在（1，2）上没有极值点.

再考虑<equation>f ( x )</equation>在（1，2）上的零点情况.

由拉格朗日中值定理知，存在<equation>\xi\in(1,2)</equation>，使得<equation>f(2)-f(1)=f^{\prime}(\xi)</equation>，即<equation>f(2)=1+f^{\prime}(\xi).</equation>由于<equation>f^{\prime}(x)</equation>在（1，2）上单调减少，且<equation>f^{\prime}(1)=-1</equation>，从而<equation>f^{\prime}(\xi)< - 1</equation>，故<equation>f(2)=1+f^{\prime}(\xi)< 0.</equation>因为<equation>f(1)=1>0,f(2)<0</equation>，所以由连续函数的介值定理知，<equation>f(x)</equation>在（1，2）上存在零点因此，<equation>f(x)</equation>在（1，2）上有零点，没有极值点.应选B.

（法二）由于曲线<equation>y=f(x)</equation>在点（1，1）附近的方程可由它在点（1，1）处的曲率圆方程来近似，即<equation>x^{2}+y^{2}=2</equation>，故我们可以用该方程算出<equation>f^{\prime}(1)</equation>和<equation>f^{\prime \prime}(1).</equation>对<equation>x^{2} + y^{2} = 2</equation>两端关于 x求导，得<equation>2 x + 2 y y ^ {\prime} = 0.</equation>代入<equation>x = 1</equation>，<equation>y(1) = 1</equation>得，<equation>y^{\prime}(1) = -1</equation>.继续对（1）式两端求导，得<equation>2 + 2 \left(y ^ {\prime}\right) ^ {2} + 2 y y ^ {\prime \prime} = 0.</equation>代入<equation>x = 1, y(1) = 1, y^{\prime}(1) = -1</equation>得，<equation>y^{\prime \prime}(1) = -2.</equation>由于<equation>y^{\prime \prime}</equation>不变号，故<equation>y^{\prime \prime}</equation>在（1，2）上恒小于零.

其余论证<equation>y = f(x)</equation>在（1，2）上有零点，没有极值点的过程同法一.

---

**2009年第9题 | 填空题 | 4分**
9. 曲线<equation>\left\{ \begin{array}{l} x = \int_ {0} ^ {1 - t} \mathrm {e} ^ {- u ^ {2}} \mathrm {d} u, \\ y = t ^ {2} \ln \left(2 - t ^ {2}\right) \end{array} \right.</equation>在点 (0,0) 处的切线方程为 ___
**答案: **## y=2x.
**解析: **解 先求点（0，0）所对应的参数 t的值.

由于<equation>\mathrm{e}^{-u^{2}}>0</equation>，故只有当<equation>1-t=0</equation>时，即<equation>t=1</equation>时，<equation>x=\int_{0}^{1-t}\mathrm{e}^{-u^{2}}\mathrm{d}u=0</equation>，且<equation>t=1</equation>时，<equation>y(1)=0.</equation>于是，<equation>t=1.</equation>由<equation>x = \int_0^{1 - t}\mathrm{e}^{-u^2}\mathrm{d}u</equation>得，<equation>\frac {\mathrm {d} x}{\mathrm {d} t} = \mathrm {e} ^ {- (1 - t) ^ {2}} \cdot \frac {\mathrm {d} (1 - t)}{\mathrm {d} t} = - \mathrm {e} ^ {- (1 - t) ^ {2}}.</equation>由<equation>y = t^{2}\ln (2 - t^{2})</equation>得，<equation>\frac {\mathrm {d} y}{\mathrm {d} t} = 2 t \ln \left(2 - t ^ {2}\right) - \frac {2 t ^ {3}}{2 - t ^ {2}}.</equation>因此，曲线在点（0，0）处的斜率为<equation>\left. \frac {\mathrm {d} y}{\mathrm {d} x} \right| _ {(0, 0)} = \frac {2 t \ln \left(2 - t ^ {2}\right) - \frac {2 t ^ {3}}{2 - t ^ {2}}}{- \mathrm {e} ^ {- (1 - t) ^ {2}}} \Bigg | _ {t = 1} = 2.</equation>曲线在点（0，0）处的切线方程为<equation>y - 0 = 2(x - 0)</equation>，即<equation>y = 2x</equation>

---


#### 方程根的存在性与个数


**2021年第4题 | 选择题 | 5分 | 答案: A**
4. 设函数<equation>f(x)=a x-b \ln x (a>0)</equation>有2个零点，则<equation>\frac{b}{a}</equation>的取值范围是（    )

A. (e,+∞) B. (0,e) C. (0,<equation>\frac{1}{e}</equation>D.<equation>(\frac{1}{e},+\infty)</equation>
答案: A
**解析: **解（法一）<equation>f ( x )</equation>的定义域为（0，<equation>+ \infty</equation>）.计算<equation>f^{\prime}(x)</equation>得<equation>f^{\prime}(x)=a-\frac{b}{x}.</equation>由于 a > 0，故若 b≤0，则<equation>f^{\prime}(x)>0</equation>，f(x)单调增加.此时 f(x)不可能有2个零点.于是，b > 0.

下面分析 f（x）的单调性.

当<equation>x=\frac{b}{a}</equation>时，<equation>f^{\prime}(x)=0</equation>；当<equation>0 < x < \frac{b}{a}</equation>时，<equation>f^{\prime}(x)<0,f(x)</equation>单调减少；当<equation>x > \frac{b}{a}</equation>时，<equation>f^{\prime}(x)>0,</equation>f(x)单调增加.于是，<equation>f(x)</equation>在（0，<equation>+\infty</equation>）上先单调减少，再单调增加.<equation>f\left(\frac{b}{a}\right)</equation>为f(x)的最小值.

f（x）有2个零点等价于<equation>f\left(\frac{b}{a}\right)</equation>小于零.否则f（x）恒大于等于零，不可能存在2个零点.<equation>f \left(\frac {b}{a}\right) = a \cdot \frac {b}{a} - b \ln \frac {b}{a} = b - b \ln \frac {b}{a} = b \left(1 - \ln \frac {b}{a}\right) < 0.</equation>又因为 b > 0，所以<equation>b \left( 1-\ln \frac{b}{a} \right) < 0</equation>等价于<equation>1-\ln \frac{b}{a} < 0</equation>即<equation>\ln \frac{b}{a} > 1,\frac{b}{a} > \mathrm{e}.</equation>因此，应选A.

（法二）同法一可知 b > 0.<equation>a x-b \ln x=0</equation>等价于<equation>\frac{x}{\ln x}=\frac{b}{a}</equation>，故函数<equation>f(x)=a x-b \ln x</equation>有2个零点等价于曲线<equation>y=\frac{x}{\ln x}</equation>与直线<equation>y=\frac{b}{a}</equation>有2个交点.

计算<equation>g ( x )=\frac{x}{\ln x}</equation>的导数<equation>g^{\prime}(x).</equation><equation>g ^ {\prime} (x) = \frac {\ln x - 1}{(\ln x) ^ {2}}.</equation>由于 x=1是 g(x)的无穷间断点，故 x=1是 y=g(x)的铅直渐近线.当 0 < x < 1时，<equation>g^{\prime}(x) < 0</equation>g(x)单调减少；当 1 < x < e时，<equation>g^{\prime}(x) < 0</equation>g(x)单调减少；当 x > e时，<equation>g^{\prime}(x) > 0</equation>g(x)单调增加，且<equation>\lim _ {x \rightarrow + \infty} g (x) = \lim _ {x \rightarrow + \infty} \frac {x}{\ln x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow + \infty} \frac {1}{\frac {1}{x}} = + \infty .</equation><equation>x=\mathrm{e}</equation>是<equation>g(x)</equation>的极小值点，极小值为<equation>g(\mathrm{e})=\mathrm{e}.</equation>y = g(x）的图形如右图所示.

由图可知，曲线<equation>y=\frac{x}{\ln x}</equation>与直线<equation>y=\frac{b}{a}</equation>有2个交点当且仅当<equation>\frac{b}{a}>\mathrm{e}.</equation>因此，应选A.

---

**2017年第19题 | 解答题 | 10分**
19. (本题满分10分)

设函数 f(x)在区间[0,1]上具有二阶导数，且<equation>f(1)>0,\lim_{x\rightarrow 0^{+}}\frac{f(x)}{x}<0.</equation>证明：

I. 方程 f(x)=0在区间（0,1）内至少存在一个实根；

II. 方程<equation>f(x)f^{\prime \prime}(x)+[f^{\prime}(x)]^{2}=0</equation>在区间（0,1）内至少存在两个不同实根.
**答案: **# （I）证明略；

（Ⅱ）证明略.
**解析: **证（I）由于<equation>\lim_{x\rightarrow 0^{+}}\frac{f(x)}{x}<0</equation>，故由函数极限的局部保号性可知，存在<equation>\theta >0</equation>，在（0，<equation>\theta</equation>）内，<equation>\frac{f(x)}{x}<0</equation>从而<equation>f(x) < 0</equation>.取0<equation>< \delta < \theta</equation>，则<equation>f(\delta) < 0.</equation>又因为<equation>f(1)>0</equation>，所以由连续函数的零点定理知，存在<equation>\xi\in(\delta,1)\subseteq(0,1)</equation>使得<equation>f(\xi)=0.</equation>因此，<equation>f(x)=0</equation>在区间（0，1）内至少存在一个实根.

（Ⅱ）考虑<equation>F ( x )=f ( x ) f^{\prime} ( x )</equation>，则<equation>F ^ {\prime} (x) = f (x) f ^ {\prime \prime} (x) + \left[ f ^ {\prime} (x) \right] ^ {2}.</equation>第（Ⅱ）问等价于证明<equation>F^{\prime}(x)=0</equation>在区间（0,1）内至少存在两个不同实根.

若能找到三个点 a < b < c ，使得 F(a) = F(b) = F(c) ，则由罗尔定理，存在<equation>\eta_{1}\in(a,b),</equation><equation>\eta_{2}\in(b,c)</equation>，满足<equation>F^{\prime}(\eta_{1})=0,F^{\prime}(\eta_{2})=0.</equation>由<equation>\lim_{x\rightarrow 0^{+}}\frac{f(x)}{x}<0</equation>知，分母趋于零，而极限仍存在，故<equation>f (0) \xlongequal {\text {连 续 性}} \lim _ {x \rightarrow 0 ^ {+}} f (x) = 0, \quad F (0) = f (0) f ^ {\prime} (0) = 0.</equation>由第（I）问的结论知，存在<equation>x_{1}\in(0,1)</equation>，满足<equation>f \left( x_{1} \right)=0</equation>，从而<equation>F \left( x_{1} \right)=f \left( x_{1} \right) f^{\prime} \left( x_{1} \right)=0.</equation>另一方面，由于<equation>f(0)=0</equation><equation>f(x_{1})=0</equation>，故由罗尔定理知，存在<equation>x_{2}\in(0,x_{1})</equation>，使得<equation>f^{\prime}(x_{2})=0</equation>，从而<equation>F(x_{2})=f(x_{2})f^{\prime}(x_{2})=0.</equation>如图所示，<equation>0 < x_{2} < x_{1}, F(0) = F(x_{2}) = F(x_{1}) = 0.</equation>由罗尔定理知，存在<equation>\eta_{1}\in(0,x_{2})</equation>，使得<equation>F^{\prime}(\eta_{1}) = 0</equation>；存在<equation>\eta_{2}\in(x_{2},x_{1})</equation>，使得<equation>F^{\prime}(\eta_{2}) = 0.</equation>命题得证

---

**2015年第19题 | 解答题 | 10分**
19. (本题满分11分)

已知函数<equation>f ( x )=\int_{x}^{1}\sqrt{1+t^{2}}\mathrm{d} t+\int_{1}^{x^{2}}\sqrt{1+t}\mathrm{d} t</equation>，求 f(x)零点的个数.
**答案: **(19)<equation>f(x)</equation>在<equation>(-\infty, +\infty)</equation>上共有两个零点.
**解析: **解（法一）由<equation>f ( x )=\int_{x}^{1}\sqrt{1+t^{2}}\mathrm{d} t+\int_{1}^{x^{2}}\sqrt{1+t}\mathrm{d} t</equation>，可知<equation>f ( x )</equation>在<equation>(-\infty , +\infty)</equation>上均有定义，且<equation>f^{\prime}(x)=\left(\int_{x}^{1}\sqrt{1+t^{2}}\mathrm{d} t\right)^{\prime}+\left(\int_{1}^{x^{2}}\sqrt{1+t}\mathrm{d} t\right)^{\prime}=-\sqrt{1+x^{2}}+2x\sqrt{1+x^{2}}=(2x-1)\sqrt{1+x^{2}}.</equation>由于<equation>\sqrt{1+x^{2}}>0</equation>，故<equation>x=\frac{1}{2}</equation>为f(x)的唯一驻点.

当<equation>x\in\left(\frac{1}{2},+\infty\right)</equation>时，<equation>f(x)</equation>单调增加；当<equation>x\in\left(-\infty ,\frac{1}{2}\right)</equation>时，<equation>f(x)</equation>单调减少. f(x)在<equation>x=\frac{1}{2}</equation>处取到最小值.

因为<equation>f ( 1 )=\int_{1}^{1}\sqrt{1+t^{2}}\mathrm{d} t+\int_{1}^{1^{2}}\sqrt{1+t}\mathrm{d} t=0</equation>，而<equation>f ( x )</equation>在<equation>\left(\frac{1}{2},+\infty\right)</equation>上单调增加，所以<equation>f ( x )</equation>在<equation>\left(\frac{1}{2},+\infty\right)</equation>上只有<equation>x=1</equation>一个零点.

由于<equation>f(1) = 0</equation>，故<equation>f\left(\frac{1}{2}\right) < f(1) = 0.</equation>又因为<equation>\lim_{x\to -\infty}f(x) = \lim_{x\to -\infty}\left(\int_x^1\sqrt{1 + t^2}\mathrm{d}t + \int_1^{x^2}\sqrt{1 + t}\mathrm{d}t\right)</equation>，两个被积函数<equation>\sqrt{1 + t^2},\sqrt{1 + t}</equation>均大于1，所以<equation>\lim_{x\to -\infty}f(x) = +\infty.</equation>由连续函数的零点定理可知，<equation>f(x)</equation>在<equation>\left(-\infty ,\frac{1}{2}\right)</equation>上必然也存在一个零点，且由<equation>f(x)</equation>的单调性可知，该零点也是该区间上的唯一零点.

综上所述，<equation>f ( x )</equation>在<equation>(-\infty, +\infty)</equation>上共有两个零点.

（法二）如法一，可得到<equation>f ( x )</equation>在<equation>\left(\frac{1}{2},+\infty\right)</equation>上只有<equation>x=1</equation>一个零点.

下面我们考虑 f（x）在<equation>\left(-\infty ,\frac{1}{2}\right)</equation>上是否存在零点.

计算 f（0），得<equation>f (0) = \int_ {0} ^ {1} \sqrt {1 + t ^ {2}} \mathrm {d} t + \int_ {1} ^ {0} \sqrt {1 + t} \mathrm {d} t = \int_ {0} ^ {1} \left(\sqrt {1 + t ^ {2}} - \sqrt {1 + t}\right) \mathrm {d} t.</equation>当<equation>t\in (0,1)</equation>时，<equation>t^{2} < t</equation>，故<equation>\sqrt{1 + t^2} -\sqrt{1 + t} < 0</equation>，从而<equation>f(0) < 0.</equation>又因为<equation>f(-1) = \int_{-1}^{1}\sqrt{1 + t^2}\mathrm{d}t + \int_{1}^{1}\sqrt{1 + t}\mathrm{d}t = \int_{-1}^{1}\sqrt{1 + t^2}\mathrm{d}t > 0</equation>，所以<equation>f(-1) > 0.</equation>由连续函数的零点定理可知，存在<equation>a\in(-1,0)</equation>，使得<equation>f(a)=0</equation>.由<equation>f(x)</equation>在<equation>\left(-\infty ,\frac{1}{2}\right)</equation>上的单调性可知该点也是<equation>\left(-\infty ,\frac{1}{2}\right)</equation>上的唯一零点.因此，<equation>f(x)</equation>在<equation>\left(-\infty ,\frac{1}{2}\right)</equation>上有且仅有一个零点.

综上所述，<equation>f ( x )</equation>在<equation>(-\infty, +\infty)</equation>上共有两个零点.

---

**2012年第21题 | 解答题 | 11分**
21. (本题满分10分)

I. 证明方程<equation>x^{n}+x^{n-1}+\cdots+x=1</equation>（ n为大于1的整数）在区间<equation>\left(\frac{1}{2},1\right)</equation>内有且仅有一个实根；

II. 记第一问中的实根为<equation>x_{n}</equation>，证明<equation>\lim_{n\rightarrow \infty}x_{n}</equation>存在，并求此极限.
**答案: **(21) （I）证明略；

（Ⅱ）证明略，<equation>\lim_{n\to \infty}x_n = \frac{1}{2}</equation>.
**解析: **证（I）设函数<equation>f_{n}(x)=x^{n}+x^{n-1}+\dots+x-1.</equation>考虑<equation>f_{n}\left(\frac{1}{2}\right)</equation>与<equation>f_{n}(1).</equation><equation>f _ {n} (1) = n - 1 > 0, \quad f _ {n} \left(\frac {1}{2}\right) = \frac {\frac {1}{2} \left(1 - \frac {1}{2 ^ {n}}\right)}{1 - \frac {1}{2}} - 1 = - \frac {1}{2 ^ {n}} < 0.</equation>由连续函数的零点定理知，存在<equation>x\in \left(\frac{1}{2},1\right)</equation>，使得<equation>f_{n}(x) = 0.</equation>又由于当<equation>x\in\left(\frac{1}{2},1\right)</equation>时，<equation>f _ {n} ^ {\prime} (x) = n x ^ {n - 1} + (n - 1) x ^ {n - 2} + \dots + 2 x + 1 > 0,</equation>故<equation>f_{n}(x)</equation>在<equation>\left(\frac{1}{2},1\right)</equation>上单调增加，在<equation>\left(\frac{1}{2},1\right)</equation>上有且仅有一个零点，即方程<equation>x^{n}+x^{n-1}+\cdots+x=</equation>1（n为大于1的整数）在区间<equation>\left(\frac{1}{2},1\right)</equation>内有且仅有一个实根.

（Ⅱ）我们利用单调有界准则证明<equation>\lim x_{n}</equation>存在.

考虑<equation>f_{n + 1}(x) = x^{n + 1} + x^n + \dots + x - 1.</equation>对于任意的<equation>x\in\left(\frac{1}{2},1\right)</equation>，都有<equation>f_{n}(x) < f_{n+1}(x)</equation>. 若<equation>x_{n}</equation>为<equation>f_{n}(x)=0</equation>的根，<equation>x_{n+1}</equation>为<equation>f_{n+1}(x)=0</equation>的根，则<equation>f _ {n} \left(x _ {n + 1}\right) < f _ {n + 1} \left(x _ {n + 1}\right) = 0 = f _ {n} \left(x _ {n}\right).</equation>由于<equation>f_{n}(x)</equation>在<equation>\left(\frac{1}{2},1\right)</equation>上为单调增加函数，故<equation>x_{n + 1} < x_n</equation>，从而<equation>\{x_n\}</equation>单调减少.

由第（I）问知，对每一个大于1的整数n，<equation>f_{n}(x)</equation>的零点<equation>x_{n}</equation>都满足<equation>x_{n}\in \left(\frac{1}{2},1\right)</equation>，故<equation>\{x_{n}\}</equation>单调且有界.由单调有界准则知，<equation>\lim_{n\to \infty}x_{n}</equation>存在.

下面求<equation>\lim_{n\to \infty}x_{n}.</equation>由于<equation>x_{n}</equation>满足方程<equation>x^{n} + x^{n - 1} + \dots + x = 1</equation>，故由等比数列的求和公式得<equation>\frac {x _ {n} \left(1 - x _ {n} ^ {n}\right)}{1 - x _ {n}} = 1.</equation>记<equation>\lim_{n\to\infty}x_{n}=a.</equation>关注公众号：小小考研 获取更多考研资料

由于对所有大于2的整数n，都有<equation>\frac{1}{2} < x_{n} < x_{2} < 1</equation>，故<equation>0 \leqslant \lim _ {n \rightarrow \infty} x _ {n} ^ {n} \leqslant \lim _ {n \rightarrow \infty} x _ {2} ^ {n} = 0.</equation>令（1）式中的<equation>n\to \infty</equation>得，<equation>\frac{a}{1 - a} = 1.</equation>因此，<equation>a = \frac{1}{2}.</equation>

---

**2011年第3题 | 选择题 | 4分 | 答案: C**
3. 函数<equation>f ( x )=\ln | ( x-1 ) ( x-2 ) ( x-3 ) |</equation>的驻点个数为（    ）

A.0 B.1 C.2 D.3
答案: C
**解析: **（法一）由于<equation>f (x) = \ln | x - 1 | + \ln | x - 2 | + \ln | x - 3 |,</equation>故<equation>f ^ {\prime} (x) = \frac {1}{x - 1} + \frac {1}{x - 2} + \frac {1}{x - 3} = \frac {3 x ^ {2} - 1 2 x + 1 1}{(x - 1) (x - 2) (x - 3)}.</equation><equation>f^{\prime}(x) = 0</equation>的零点为<equation>3 x^{2}-1 2 x+1 1=0</equation>的根.由于该方程的判别式<equation>\Delta = (- 1 2) ^ {2} - 4 \times 1 1 \times 3 > 0,</equation>故该方程有2个不同的实根.

因此，<equation>f^{\prime}(x)</equation>有2个零点，<equation>f(x)</equation>的驻点个数为2.应选C.

（法二）本题可用罗尔定理结合多项式的零点个数与其次数的关系来判断 f(x)的驻点个数当<equation>x\neq1,2,3</equation>时，<equation>f ^ {\prime} (x) = \frac {\left[ (x - 1) (x - 2) (x - 3) \right] ^ {\prime}}{(x - 1) (x - 2) (x - 3)}.</equation>令<equation>g(x) = (x - 1)(x - 2)(x - 3)</equation>，则<equation>f^{\prime}(x)</equation>的零点个数与<equation>g^{\prime}(x)</equation>的零点个数相同.

g(x)有3个根，<equation>x=1,x=2</equation>和<equation>x=3</equation>.由罗尔定理知，<equation>g^{\prime}(x)</equation>在（1，2），（2，3）上各有1个零点.又因为 g(x)为三次多项式，<equation>g^{\prime}(x)</equation>为二次多项式，<equation>g^{\prime}(x)</equation>至多有2个零点，所以<equation>g^{\prime}(x)</equation>有且仅有2个零点，即<equation>f^{\prime}(x)</equation>有且仅有2个零点. f(x)的驻点个数为2.应选C.

---


#### 泰勒公式


**2021年第5题 | 选择题 | 5分 | 答案: D**
5. 设函数 f(x) = secx在 x=0处的2次泰勒多项式为<equation>1+a x+b x^{2}</equation>，则（    )

A. a=1,b=-<equation>\frac{1}{2}</equation>B. a=1,b=<equation>\frac{1}{2}</equation>C. a=0,b=-<equation>\frac{1}{2}</equation>D. a=0,b=<equation>\frac{1}{2}</equation>
答案: D
**解析: **解 依次计算<equation>\left. \sec x\right)^{\prime}\left|_{x=0},\left. \left. \sec x\right)^{\prime \prime}\right|_{x=0}.</equation><equation>\left. \left. \sec x\right)^{\prime}\right|_{x=0}=\sec x\tan x,</equation><equation>\left. \left. \sec x\right)^{\prime \prime}\right|_{x=0}=\left. \left. \sec x\tan x\right)^{\prime}\right|=\tan^{2}x\sec x+\sec^{3}x.</equation>代入<equation>x=0</equation>，可得<equation>\left. \left. \sec x\right)^{\prime}\right|_{x=0}=0, \left. \left. \left. \sec x\right)^{\prime \prime}\right|_{x=0}=1.</equation>因此，<equation>f(x)=\sec x</equation>在 x=0处的2次泰勒多项式为<equation>1+0\cdot x+\frac{1}{2}\cdot x^{2}=1+\frac{1}{2}x^{2}, a=0, b=\frac{1}{2}.</equation>应选D.

---


#### 函数的单调性、极值与最值


**2020年第6题 | 选择题 | 4分 | 答案: B**
6. 设函数<equation>f ( x )</equation>在区间[-2,2]上可导，且<equation>f^{\prime} ( x ) > f ( x ) > 0</equation>，则（    ）

A.<equation>\frac{f(-2)}{f(-1)}>1</equation>B.<equation>\frac{f(0)}{f(-1)}>e</equation>C.<equation>\frac{f(1)}{f(-1)}<\mathrm{e}^{2}</equation>D.<equation>\frac{f(2)}{f(-1)}<\mathrm{e}^{3}</equation>
答案: B
**解析: **解（法一）令<equation>F ( x )=\frac{f ( x )} {\mathrm{e}^{x}}</equation>，则<equation>F ^ {\prime} (x) = \frac {\mathrm {e} ^ {x} \left[ f ^ {\prime} (x) - f (x) \right]}{\mathrm {e} ^ {2 x}} = \frac {f ^ {\prime} (x) - f (x)}{\mathrm {e} ^ {x}} > 0.</equation>由此可知，F（x）单调增加.

由<equation>F ( 0 ) > F (- 1 )</equation>可得，<equation>\frac{f(0)}{1}>\frac{f(-1)}{e^{-1}}.</equation>由<equation>f ( x ) > 0</equation>可得<equation>\frac{f(0)}{f(-1)} > \mathrm{e}.</equation>因此，应选B.

下面说明其余选项均不正确.

根据 F(x)的单调性，应有<equation>F(-2) < F(-1) < F(0) < F(1) < F(2)</equation>，结合 f(x) > 0 可得<equation>\frac {f (- 2)}{f (- 1)} < \mathrm {e} ^ {- 1}, \quad \frac {f (1)}{f (- 1)} > \mathrm {e} ^ {2}, \quad \frac {f (2)}{f (- 1)} > \mathrm {e} ^ {3}.</equation>（法二）取<equation>f ( x )=\mathrm{e}^{2 x}</equation>，则<equation>f ( x )</equation>在<equation>[-2,2]</equation>上可导，且<equation>f^{\prime}(x)=2\mathrm{e}^{2x}>\mathrm{e}^{2x}=f(x)>0.</equation>选项A：<equation>\frac{f(-2)}{f(-1)}=\frac{\mathrm{e}^{-4}}{\mathrm{e}^{-2}}=\mathrm{e}^{-2}<1.</equation>选项B：<equation>\frac{f(0)}{f(-1)}=\frac{1}{e^{-2}}=e^{2}>e.</equation>选项C：<equation>\frac{f(1)}{f(-1)}=\frac{\mathrm{e}^{2}}{\mathrm{e}^{-2}}=\mathrm{e}^{4}>\mathrm{e}^{2}.</equation>选项D：<equation>\frac{f(2)}{f(-1)}=\frac{\mathrm{e}^{4}}{\mathrm{e}^{-2}}=\mathrm{e}^{6}>\mathrm{e}^{3}.</equation>由排除法可知，应选B.

---

**2019年第15题 | 解答题 | 10分**
15. (本题满分10分）

已知函数<equation>f ( x )=\left\{\begin{array}{ll}x^{2 x},&x>0,\\ x \mathrm{e}^{x}+1,&x\leqslant 0.\end{array} \right.</equation>求<equation>f^{\prime}(x)</equation>，并求 f(x)的极值.
**答案: **<equation>f^{\prime}(x)=\left\{\begin{array}{ll}\mathrm{e}^{x}(x+1),&x<0,\\ 2\mathrm{e}^{2x\ln x}(\ln x+1),&x>0.\end{array} \right.</equation>x=-1和 x =<equation>\frac{1} {\mathrm{e}}</equation>是 f(x)的极小值点，极小值分别为 f(-1) = 1 -<equation>\mathrm{e}^{-1}</equation>和<equation>f\left(\frac{1}{\mathrm{e}}\right)=\mathrm{e}^{-\frac{2}{\mathrm{e}}}</equation>；x=0是 f(x)的极大值点，极大值为 f(0) = 1.
**解析: **解 f(x)是一个分段函数. x=0是分界点.分别计算 x > 0时与 x < 0时的<equation>f^{\prime}(x).</equation>当 x > 0时，<equation>f ^ {\prime} (x) = \left(x ^ {2 x}\right) ^ {\prime} = \left(\mathrm {e} ^ {2 x \ln x}\right) ^ {\prime} = \mathrm {e} ^ {2 x \ln x} \cdot \left(2 \ln x + 2 x \cdot \frac {1}{x}\right) = 2 \mathrm {e} ^ {2 x \ln x} (\ln x + 1).</equation>当 x < 0时，<equation>f ^ {\prime} (x) = \mathrm {e} ^ {x} + x \mathrm {e} ^ {x} = \mathrm {e} ^ {x} (x + 1).</equation>计算<equation>f^{\prime}(0).</equation>由<equation>f ( x )</equation>的定义知<equation>f ( 0 )=1.</equation><equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0 ^ {-}} \frac {x \mathrm {e} ^ {x} + 1 - 1}{x} = \lim _ {x \rightarrow 0 ^ {-}} \mathrm {e} ^ {x} = 1.</equation><equation>\begin{aligned} f _ {+} ^ {\prime} (0) &= \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {2 x \ln x} - 1}{x} \frac {\mathrm {e} ^ {2 x \ln x} - 1 \sim 2 x \ln x}{\lim _ {x \rightarrow 0 ^ {+}} \frac {2 x \ln x}{x}} \\ &= 2 \lim _ {x \rightarrow 0 ^ {+}} \ln x = - \infty . \end{aligned}</equation>f(x)的右导数不存在，故f(x）在<equation>x=0</equation>处不可导.

因此，<equation>f^{\prime}(x) = \left\{ \begin{array}{ll} \mathrm{e}^{x}(x + 1), & x < 0, \\ 2\mathrm{e}^{2x\ln x}(\ln x + 1), & x > 0. \end{array} \right.</equation>考察 f（x）的极值，需分别考察 f（x）的驻点与不可导点.

令<equation>f^{\prime}(x)=0</equation>当 x > 0时，解得<equation>x=\frac{1} {\mathrm{e}}</equation>当 x < 0时，解得 x=-1.加上不可导点 x=0，这三个点将<equation>(-\infty, +\infty)</equation>分为4个区间.

当 x < -1时，<equation>f^{\prime}(x) < 0,f(x)</equation>单调减少.

当<equation>- 1 < x < 0</equation>时，<equation>f^{\prime}(x) > 0,f(x)</equation>单调增加.

当<equation>0 < x < \frac{1} {\mathrm{e}}</equation>时，<equation>f^{\prime}(x) < 0,f(x)</equation>单调减少.

当<equation>x > \frac{1} {\mathrm{e}}</equation>时，<equation>f^{\prime}(x) > 0,f(x)</equation>单调增加.

注意到 f(x)在 x=0处连续.于是，根据极值的第一充分条件，<equation>x=-1</equation>和<equation>x=\frac{1} {\mathrm{e}}</equation>是 f(x)的极小值点，极小值分别为<equation>f(-1)=1-\mathrm{e}^{-1}</equation>和<equation>f\left(\frac{1}{\mathrm{e}}\right)=\mathrm{e}^{-\frac{2}{\mathrm{e}}}</equation>；x=0是 f(x)的极大值点，极大值为<equation>f(0)=1.</equation>f（x）的单调性与极值可整理如下.

<table border="1"><tr><td>x</td><td><equation>(-\infty,-1)</equation></td><td>-1</td><td><equation>(-1,0)</equation></td><td>0</td><td><equation>(0,\frac{1}{e})</equation></td><td><equation>\frac{1}{e}</equation></td><td><equation>(\frac{1}{e},+\infty)</equation></td></tr><tr><td><equation>f^{\prime}(x)</equation></td><td>-</td><td>0</td><td>+</td><td>不存在</td><td>-</td><td>0</td><td>+</td></tr><tr><td><equation>f(x)</equation></td><td>单调减少</td><td>极小值</td><td>单调增加</td><td>极大值</td><td>单调减少</td><td>极小值</td><td>单调增加</td></tr></table>

---

**2017年第18题 | 解答题 | 10分**
18. (本题满分10分）

已知函数 y(x)由方程<equation>x^{3}+y^{3}-3 x+3 y-2=0</equation>确定，求 y(x）的极值.
**答案: **极大值 y（1）=1，极小值 y（-1）=0.
**解析: **解 对方程两端关于 x求导，得<equation>3 x ^ {2} + 3 y ^ {2} y ^ {\prime} - 3 + 3 y ^ {\prime} = 0.</equation>整理得<equation>\left(y ^ {2} + 1\right) y ^ {\prime} = 1 - x ^ {2}.</equation>由于<equation>y^{2}+1>0</equation>，故 y(x）的全部驻点为 x=1和 x=-1.

将 x=1代入方程<equation>x^{3}+y^{3}-3 x+3 y-2=0</equation>，得<equation>y^{3}+3 y-4=0</equation>. 通过观察发现 y=1是该方程的一个根.由于<equation>\frac{\mathrm{d}\left(y^{3}+3 y-4\right)}{\mathrm{d} y}=3 y^{2}+3>0</equation>，故<equation>y^{3}+3 y-4</equation>关于 y单调增加. y=1是<equation>y^{3}+3 y-4=0</equation>的唯一实根，<equation>y(1)=1.</equation>将 x=-1代入方程<equation>x^{3}+y^{3}-3 x+3 y-2=0</equation>，得<equation>y^{3}+3 y=0</equation>，即<equation>y \left(y^{2}+3\right)=0. y=0</equation>是该方程的唯一实根，<equation>y(-1)=0.</equation>下面用两种方法来判断驻点的极值点类型.

（法一）对（1）式两端关于 x求导，得<equation>\left(y ^ {2} + 1\right) y ^ {\prime \prime} + 2 y \left(y ^ {\prime}\right) ^ {2} = - 2 x.</equation>利用（2）式计算驻点<equation>x=\pm1</equation>处的二阶导数.

由于在驻点处，<equation>y^{\prime}=0</equation>，故当<equation>x=\pm 1</equation>时，<equation>\left(y ^ {2} + 1\right) y ^ {\prime \prime} = - 2 x.</equation>当 x=1时，(3)式化为<equation>2y^{\prime \prime}(1)=-2,y^{\prime \prime}(1)=-1<0</equation>；当 x=-1时，(3)式化为<equation>y^{\prime \prime}(-1)=2>0.</equation>因此，<equation>y(1)=1</equation>为极大值，<equation>y(-1)=0</equation>为极小值.

（法二）由（1）式可得<equation>y^{\prime}=\frac{1-x^{2}}{y^{2}+1}.</equation>注意到<equation>y^{2}+1</equation>恒大于零，故<equation>y^{\prime}(x)</equation>与y(x）的性质如下表.

<table border="1"><tr><td>x</td><td>(-∞,-1)</td><td>-1</td><td>(-1,1)</td><td>1</td><td>(1,+∞)</td></tr><tr><td>y&#x27;(x)</td><td>-</td><td>0</td><td>+</td><td>0</td><td>-</td></tr><tr><td>y(x)</td><td>单调减少</td><td>极小值</td><td>单调增加</td><td>极大值</td><td>单调减少</td></tr></table>

因此，<equation>y ( 1 ) = 1</equation>为极大值，<equation>y (- 1 ) = 0</equation>为极小值.

---

**2010年第15题 | 解答题 | 10分**
15. (本题满分10分)

求函数<equation>f ( x )=\int_{1}^{x^{2}}(x^{2}-t)\mathrm{e}^{-t^{2}}\mathrm{d} t</equation>的单调区间与极值.
**答案: **5) 单调增加区间为（-1，0）和（1，<equation>+ \infty</equation>），单调减少区间为（<equation>-\infty,-1</equation>）和（0，1）；极大值<equation>f(0)=\frac{1}{2}\left(1-\frac{1}{\mathrm{e}}\right)</equation>，极小值<equation>f(\pm 1)=0.</equation>
**解析: **解 先求<equation>f^{\prime}(x).</equation>由于在变限积分<equation>\int_{1}^{x^2}(x^2 - t)\mathrm{e}^{-t^2}\mathrm{d}t</equation>中，<equation>x</equation>不是积分变量，故可以把它提到积分号外.<equation>f (x) = \int_ {1} ^ {x ^ {2}} \left(x ^ {2} - t\right) \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t = x ^ {2} \int_ {1} ^ {x ^ {2}} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t - \int_ {1} ^ {x ^ {2}} t \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t.</equation>根据变限积分函数的求导公式以及求导的乘法法则，<equation>f ^ {\prime} (x) = 2 x \int_ {1} ^ {x ^ {2}} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t + 2 x ^ {3} \mathrm {e} ^ {- x ^ {4}} - 2 x ^ {3} \mathrm {e} ^ {- x ^ {4}} = 2 x \int_ {1} ^ {x ^ {2}} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t.</equation><equation>f^{\prime}(x) = 0</equation>当且仅当<equation>x = 0</equation>或<equation>\int_{1}^{x^{2}}\mathrm{e}^{-t^{2}}\mathrm{d}t = 0.</equation>由于<equation>\mathrm{e}^{-t^{2}}</equation>恒大于零，故当且仅当<equation>x^{2} = 1</equation>，即<equation>x = \pm 1</equation>时，<equation>\int_{1}^{x^{2}}\mathrm{e}^{-t^{2}}\mathrm{d}t = 0.</equation>因此，<equation>x = 0,\pm 1</equation>为<equation>f(x)</equation>的驻点.

对<equation>\int_{1}^{x^{2}}\mathrm{e}^{-t^{2}}\mathrm{d}t</equation>来说，当<equation>x^{2} < 1</equation>时，<equation>\int_{1}^{x^{2}}\mathrm{e}^{-t^{2}}\mathrm{d}t < 0</equation>；当<equation>x^{2} > 1</equation>时，<equation>\int_{1}^{x^{2}}\mathrm{e}^{-t^{2}}\mathrm{d}t > 0.</equation>因此有下表.

<table border="1"><tr><td>x</td><td>(-∞,-1)</td><td>-1</td><td>(-1,0)</td><td>0</td><td>(0,1)</td><td>1</td><td>(1,+∞)</td></tr><tr><td>f&#x27;(x)</td><td>-</td><td>0</td><td>+</td><td>0</td><td>-</td><td>0</td><td>+</td></tr><tr><td>f(x)</td><td>单调减少</td><td>极小值</td><td>单调增加</td><td>极大值</td><td>单调减少</td><td>极小值</td><td>单调增加</td></tr></table>

由此可知，<equation>f ( x )</equation>的单调增加区间为<equation>(-1,0)</equation>和<equation>( 1,+\infty)</equation>；<equation>f ( x )</equation>的单调减少区间为<equation>(-\infty,-1)</equation>和(0，1)；<equation>f (-1)</equation>和f（1）为<equation>f ( x )</equation>的极小值，<equation>f (- 1) = f (1) = \int_ {1} ^ {1} (1 - t) \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t = 0;</equation>f（0）为f（x）的极大值，<equation>f (0) = \int_ {1} ^ {0} (- t) \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t = \frac {1}{2} \left(1 - \frac {1}{\mathrm {e}}\right).</equation>

---

**2009年第13题 | 填空题 | 4分**
13. 函数<equation>y=x^{2x}</equation>在区间 (0,1] 上的最小值为 ___
**答案: **# -<equation>\frac{2}{e}</equation>
**解析: **解 先求<equation>y^{\prime}</equation>. 由于<equation>y = x^{2x}</equation>是幂指函数，故可采用对数求导法.

在（0,1]上，<equation>y=x^{2x}>0.</equation>对<equation>y=x^{2x}</equation>两端取对数，得<equation>\ln y = 2x\ln x.</equation>对该式两端关于<equation>x</equation>求导得<equation>\frac {y ^ {\prime}}{y} = 2 x \cdot \frac {1}{x} + 2 \ln x = 2 (\ln x + 1),</equation>即<equation>y^{\prime} = 2(\ln x + 1)y = 2(\ln x + 1)x^{2x}</equation>.

由于在（0，1]上，<equation>x^{2 x}>0</equation>，故<equation>y^{\prime}</equation>的零点仅当<equation>\ln x+1=0</equation>时取得，此时<equation>x=\frac{1}{e}</equation>.于是，当<equation>0 < x < \frac{1}{e}</equation>时，<equation>\ln x+1<0, y^{\prime}<0, y</equation>单调减少；当<equation>\frac{1}{e} < x \leqslant 1</equation>时，<equation>\ln x+1>0, y^{\prime}>0, y</equation>单调增加.

因此，函数<equation>y=x^{2 x}</equation>在区间（0，1]上的最小值在<equation>x=\frac{1}{e}</equation>处取得，此时<equation>y=\left(\mathrm{e}^{-1}\right)^{\frac{2}{e}}=\mathrm{e}^{-\frac{2}{e}}.</equation>

---


#### 不等式的证明


**2018年第18题 | 解答题 | 10分**
18. (本题满分10分）

已知常数<equation>k\geqslant \ln 2-1</equation>. 证明：<equation>(x-1)(x-\ln^{2}x+2k\ln x-1)\geqslant 0.</equation>
**解析: **证记<equation>f ( x )=x-\ln^{2} x+2 k \ln x-1</equation>，则<equation>f ( 1 )=0</equation><equation>f ^ {\prime} (x) = 1 - \frac {2 \ln x}{x} + \frac {2 k}{x} = \frac {x - 2 \ln x + 2 k}{x}.</equation>由于在（0，<equation>+\infty</equation>）内，<equation>x > 0</equation>，故若能证明<equation>x - 2\ln x + 2k</equation>在（0，<equation>+\infty</equation>）内非负，则<equation>f^{\prime}(x)</equation>在（0，<equation>+\infty</equation>）内非负，从而<equation>f(x)</equation>在（0，<equation>+\infty</equation>）内单调增加.

考虑函数 g（x）=x-2lnx.<equation>g ^ {\prime} (x) = 1 - \frac {2}{x}.</equation>当<equation>x=2</equation>时，<equation>g^{\prime}(x)=0</equation>；当<equation>0 < x < 2</equation>时，<equation>g^{\prime}(x)<0</equation>，<equation>g(x)</equation>单调减少；当<equation>x > 2</equation>时，<equation>g^{\prime}(x)>0</equation>，<equation>g(x)</equation>单调增加.于是，<equation>g(x)</equation>在<equation>x=2</equation>处取得（0，<equation>+\infty</equation>）内的最小值，最小值为<equation>g(2)=2-2\ln 2.</equation>当 k<equation>\geqslant\ln2-1</equation>时，<equation>2-2\ln2+2k\geqslant0</equation>，从而 x-2<equation>\ln x+2k</equation>在（0，<equation>+\infty</equation>）内非负且仅当 x=2,k=<equation>\ln2-1</equation>时等于零.因此，在（0，<equation>+\infty</equation>）<equation>\backslash\{2\}</equation>内，<equation>f^{\prime}(x)>0</equation><equation>f(x)</equation>在（0，<equation>+\infty</equation>）内单调增加.又因为 f(1)=0，所以当 0 < x < 1时，<equation>f(x)<0</equation>当 x >1时，<equation>f(x)>0</equation>从而 f(x)与 x-1在（0，<equation>+\infty</equation>）内同号.

由于 f(x)与 x-1在（0，+∞）内同号，故（x-1）f(x）≥0，即（x-1）（x-<equation>\ln^{2}x+2k\ln x-1）\geqslant0.</equation>

---

**2012年第20题 | 解答题 | 11分**
20. (本题满分10分)

证明：<equation>x\ln \frac{1+x}{1-x}+\cos x\geqslant 1+\frac{x^{2}}{2}(-1<x<1)</equation>
**答案: **## （20）证明略.
**解析: **证（法一）考虑辅助函数<equation>f ( x )=x \ln \frac{1+x}{1-x}+\cos x-1-\frac{x^{2}}{2}.</equation><equation>f (- x) = (- x) \ln \frac {1 - x}{1 + x} + \cos x - 1 - \frac {x ^ {2}}{2} = f (x),</equation>故 f(x)为偶函数.如果能证明当 x<equation>\in[0,1)</equation>时，<equation>f(x)\geqslant0</equation>，那么当 x<equation>\in(-1,1)</equation>时，也有 f(x)<equation>\geqslant0</equation>从而题给不等式成立.

计算<equation>f^{\prime}(x).</equation><equation>f ^ {\prime} (x) = \left(x \ln \frac {1 + x}{1 - x} + \cos x - 1 - \frac {x ^ {2}}{2}\right) ^ {\prime} = \frac {2 x}{1 - x ^ {2}} + \ln \frac {1 + x}{1 - x} - \sin x - x.</equation>由于当<equation>x\in[0,1)</equation>时，<equation>\frac{x}{1-x^{2}}\geqslant x\geqslant\sin x</equation>，故<equation>\frac {2 x}{1 - x ^ {2}} \geqslant 2 x \geqslant \sin x + x,</equation>等号在<equation>x = 0</equation>时取得. 又因为<equation>\frac{1 + x}{1 - x}\geqslant 1</equation>，所以<equation>\ln \frac{1 + x}{1 - x}\geqslant 0</equation>，等号在<equation>x = 0</equation>时取得.

因此，当 x<equation>\in</equation>（0,1）时，<equation>f ^ {\prime} (x) = \frac {2 x}{1 - x ^ {2}} + \ln \frac {1 + x}{1 - x} - \sin x - x > 0.</equation>综上所述，<equation>f ( x )</equation>在[0，1）上单调增加，<equation>f ( 0 )</equation>为<equation>f ( x )</equation>在[0，1）上的最小值.又由<equation>f ( x )</equation>为偶函数可知，在（-1，1）上，<equation>f ( x ) \geqslant f ( 0 ) = 0</equation>即<equation>x \ln \frac{1+x}{1-x}+\cos x\geqslant 1+\frac{x^{2}}{2}(-1<x<1).</equation>（法二）在法一中求得<equation>f^{\prime}(x)=\frac{2x}{1-x^{2}}+\ln \frac{1+x}{1-x}-\sin x-x</equation>后，继续求<equation>f^{\prime\prime}(x)</equation>以判断<equation>f^{\prime}(x)</equation>的性质.<equation>f ^ {\prime \prime} (x) = \frac {2 \left(1 + x ^ {2}\right)}{\left(1 - x ^ {2}\right) ^ {2}} + \frac {1}{1 + x} - \frac {(- 1)}{1 - x} - \cos x - 1 = \frac {4}{\left(1 - x ^ {2}\right) ^ {2}} - \cos x - 1.</equation>由于当 x<equation>\in[0,1)</equation>时，<equation>\frac {4}{\left(1 - x ^ {2}\right) ^ {2}} \geqslant 4, \quad 1 + \cos x \leqslant 2,</equation>故<equation>f^{\prime \prime}(x) > 0. f^{\prime}(x)</equation>在[0，1）上单调增加，<equation>f^{\prime}(x)\geqslant f^{\prime}(0)=0,f(x)</equation>在[0，1）上单调增加.

（法三）首先，<equation>f ( x ) = x \ln \frac { 1 + x } { 1 - x } + \cos x</equation>为偶函数，<equation>g ( x ) = 1 + \frac { x^{2}}{2}</equation>也为偶函数，故我们只需证明，在（0，1）上，<equation>f ( x ) \geqslant g ( x )</equation>，并且<equation>f ( 0 ) = g ( 0 )</equation>，便能得到在（-1，1）上，<equation>f ( x ) \geqslant g ( x )</equation>由泰勒中值定理，<equation>\cos x=1-\frac{x^{2}}{2!}+\frac{\cos \xi}{4!} x^{4},\xi</equation>为介于0和x之间的某个值.于是，当<equation>x\in(0,1)</equation>时，<equation>\cos x\geqslant 1-\frac{x^{2}}{2}.</equation>从而<equation>f (x) = x \ln \frac {1 + x}{1 - x} + \cos x \geqslant x \ln \frac {1 + x}{1 - x} + 1 - \frac {x ^ {2}}{2}.</equation>若能证明<equation>x\ln \frac{1+x}{1-x}+1-\frac{x^{2}}{2}\geqslant 1+\frac{x^{2}}{2}</equation>，则由不等号的传递性可知原不等式得证.

由于当<equation>x\in(0,1)</equation>时，<equation>x \ln \frac {1 + x}{1 - x} + 1 - \frac {x ^ {2}}{2} \geqslant 1 + \frac {x ^ {2}}{2} \Leftrightarrow x \ln \frac {1 + x}{1 - x} \geqslant x ^ {2} \Leftrightarrow \ln \frac {1 + x}{1 - x} \geqslant x,</equation>故我们只需要证明<equation>\ln \frac{1+x}{1-x}\geqslant x.</equation>考虑<equation>\varphi(x)=\ln \frac{1+x}{1-x}-x.</equation><equation>\varphi^ {\prime} (x) = \frac {1}{1 + x} - \frac {(- 1)}{1 - x} - 1 = \frac {2}{1 - x ^ {2}} - 1.</equation>当<equation>x\in (0,1)</equation>时，<equation>\frac{2}{1 - x^2}\geqslant 2</equation>，从而<equation>\varphi^{\prime}(x) = \frac{2}{1 - x^2} -1 > 0,\varphi(x)</equation>在（0，1）上单调增加，<equation>\varphi(x)\geqslant \varphi(0) = 0.</equation>综上所述，原不等式成立.

---


### 函数、极限、连续

#### 无穷小量


**2025年第4题 | 选择题 | 5分 | 答案: C**

4. 设函数 f(x)，g(x)在 x=0的某去心邻域内有定义且恒不为零，若当<equation>x \rightarrow 0</equation>时，f(x)是 g(x)的高阶无穷小，则当<equation>x \rightarrow 0</equation>时（    )

A.<equation>f(x)+g(x)=o\left(g(x)\right)</equation>B.<equation>f(x)g(x)=o\left(f^{2}(x)\right)</equation>C.<equation>f(x)=o\left(\mathrm{e}^{g(x)}-1\right)</equation>D.<equation>f(x)=o\left(g^{2}(x)\right)</equation>

答案: C

**解析:**解 由于当<equation>x\to 0</equation>时，<equation>f(x)</equation>是<equation>g(x)</equation>的高阶无穷小，故<equation>\lim_{x\to 0}\frac{f(x)}{g(x)} = 0.</equation>于是，<equation>\lim _ {x \rightarrow 0} \frac {f (x) + g (x)}{g (x)} = 1 + \lim _ {x \rightarrow 0} \frac {f (x)}{g (x)} = 1,</equation><equation>\lim _ {x \rightarrow 0} \frac {f (x) g (x)}{f ^ {2} (x)} = \lim _ {x \rightarrow 0} \frac {g (x)}{f (x)} = \infty ,</equation><equation>\lim _ {x \rightarrow 0} \frac {f (x)}{\mathrm {e} ^ {g (x)} - 1} \xrightarrow {\mathrm {e} ^ {g (x)} - 1 - g (x)} \lim _ {x \rightarrow 0} \frac {f (x)}{g (x)} = 0.</equation>由此可得，选项A、B不正确，选项C正确.

对选项D，取<equation>f ( x )=x^{2}, g ( x )=x</equation>，则<equation>\lim_{x\to 0}\frac{f(x)}{g^{2}(x)}=1\neq0</equation>，选项D不正确因此，应选C.

---

**2023年第3题 | 选择题 | 5分 | 答案: B**

3. 已知数列<equation>\{x_{n}\}</equation><equation>\{y_{n}\}</equation>满足<equation>x_{1}=y_{1}=\frac{1}{2},x_{n+1}=\sin x_{n},y_{n+1}=y_{n}^{2}(n=1,2,\cdots)</equation>，则当 n<equation>\to\infty</equation>时，（    ）

A.<equation>x_{n}</equation>是<equation>y_{n}</equation>的高阶无穷小 B.<equation>y_{n}</equation>是<equation>x_{n}</equation>的高阶无穷小

C.<equation>x_{n}</equation>是<equation>y_{n}</equation>的等价无穷小 D.<equation>x_{n}</equation>是<equation>y_{n}</equation>的同阶但非等价无穷小

答案: B

**解析:**解（法一）首先证明对任意正整数<equation>n,x_{n}\in (0,1)</equation>.

当<equation>n=1</equation>时，<equation>x_{1}=\frac{1}{2}\in(0,1).</equation>假设<equation>x_{n}\in(0,1)</equation>，则<equation>x_{n+1}=\sin x_{n}\in(0,1).</equation>由数学归纳法可知对任意正整数 n，<equation>x_{n}\in(0,1).</equation>由<equation>\sin x</equation>的泰勒公式可知，存在<equation>\xi_{n}\in(0,x_{n})</equation>，使得<equation>x _ {n + 1} = \sin x _ {n} = x _ {n} - \frac {\cos \xi_ {n}}{6} x _ {n} ^ {3} > x _ {n} - \frac {x _ {n} ^ {3}}{6} > \frac {x _ {n}}{2}.</equation>于是，<equation>x _ {n} > \frac {1}{2} x _ {n - 1} > \left(\frac {1}{2}\right) ^ {2} x _ {n - 2} > \dots > \left(\frac {1}{2}\right) ^ {n - 1} x _ {1} = \left(\frac {1}{2}\right) ^ {n}.</equation>由<equation>y_{1} = \frac{1}{2}, y_{n + 1} = y_{n}^{2}</equation>可知<equation>y_{n} = y_{n - 1}^{2} = y_{n - 2}^{4} = \dots = y_{1}^{2^{n - 1}} = \left(\frac{1}{2}\right)^{2^{n - 1}}.</equation>因此，<equation>0 < \frac {y _ {n}}{x _ {n}} < \frac {\left(\frac {1}{2}\right) ^ {2 ^ {n - 1}}}{\left(\frac {1}{2}\right) ^ {n}} = \left(\frac {1}{2}\right) ^ {2 ^ {n - 1} - n}.</equation>由于<equation>\lim_{n\to \infty}\left(\frac{1}{2}\right)^{2^{n-1}-n}=0</equation>，故由夹逼准则可知，<equation>\lim_{n\to \infty}\frac{y_{n}}{x_{n}}=0.</equation>综上所述，当<equation>n\to\infty</equation>时，<equation>y_{n}</equation>是<equation>x_{n}</equation>的高阶无穷小，应选B.

（法二）首先我们证明，在<equation>\left( 0, \frac{\pi}{2} \right)</equation>内，<equation>\sin x > \frac{2}{\pi} x</equation>即<equation>\frac{\sin x}{x} > \frac{2}{\pi}.</equation>令<equation>f ( x )=\frac{\sin x}{x}, x \in\left(0,\frac{\pi}{2}\right)</equation>，则<equation>f^{\prime}(x)=\frac{x\cos x-\sin x}{x^{2}}.</equation>注意到<equation>f^{\prime}(x)</equation>的分母恒大于0，故考虑分子的符号.

令<equation>g ( x )=x \cos x-\sin x,x \in\left(0, \frac{\pi}{2}\right)</equation>，则<equation>g^{\prime}(x)=\cos x-x \sin x-\cos x=-x \sin x<0</equation>，于是，<equation>g ( x )</equation>在<equation>\left(0, \frac{\pi}{2}\right)</equation>内单调减少.结合<equation>g ( 0 )=0</equation>，可得<equation>g ( x )<0</equation>，从而<equation>f^{\prime}(x)</equation>在<equation>\left(0, \frac{\pi}{2}\right)</equation>内小于0，<equation>f ( x )</equation>在<equation>\left(0, \frac{\pi}{2}\right)</equation>内单调减少.因此，当<equation>x \in\left(0, \frac{\pi}{2}\right)</equation>时，<equation>f ( x )>f \left( \frac{\pi}{2} \right)=\frac{2}{\pi}</equation>即<equation>\frac{\sin x}{x}>\frac{2}{\pi}.</equation>由法一可知，对任意正整数 n，<equation>x_{n}\in(0,1)\subset\left(0,\frac{\pi}{2}\right)</equation>，从而由前面的分析可得<equation>x _ {n + 1} = \sin x _ {n} > \frac {2}{\pi} x _ {n}.</equation>下面我们证明，对任意正整数<equation>n, y_{n}\in \left[0,\frac{1}{2}\right]</equation>，从而<equation>y_{n + 1} = y_n^2 \leqslant \frac{1}{2} y_n.</equation>当 n=1时，<equation>y_{1}=\frac{1}{2}\in\left[0,\frac{1}{2}\right].</equation>假设<equation>y_{n}\in\left[0,\frac{1}{2}\right]</equation>，则<equation>y_{n+1}=y_{n}^{2}\in\left[0,\frac{1}{2}\right].</equation>由数学归纳法可知对任意正整数n，<equation>y_{n}\in\left[0,\frac{1}{2}\right],</equation>从而<equation>y_{n+1}=y_{n}^{2}\leqslant \frac{1}{2} y_{n}.</equation>因此，<equation>0 < \frac {y _ {n}}{x _ {n}} < \frac {\frac {1}{2} y _ {n - 1}}{\frac {2}{\pi} x _ {n - 1}} = \frac {\pi}{4} \cdot \frac {y _ {n - 1}}{x _ {n - 1}} < \frac {\pi}{4} \cdot \frac {\frac {1}{2} y _ {n - 2}}{\frac {2}{\pi} x _ {n - 2}} = \left(\frac {\pi}{4}\right) ^ {2} \frac {y _ {n - 2}}{x _ {n - 2}} < \dots = \left(\frac {\pi}{4}\right) ^ {n - 1} \frac {y _ {1}}{x _ {1}} = \left(\frac {\pi}{4}\right) ^ {n - 1}.</equation>由于<equation>\lim_{n\rightarrow\infty}\left(\frac{\pi}{4}\right)^{n-1}=0</equation>，故由夹逼准则可知，<equation>\lim_{n\rightarrow\infty}\frac{y_{n}}{x_{n}}=0.</equation>综上所述，当<equation>n\to\infty</equation>时，<equation>y_{n}</equation>是<equation>x_{n}</equation>的高阶无穷小，应选B.

---

**2022年第1题 | 选择题 | 5分 | 答案: C**

1. 当<equation>x\to0</equation>时，<equation>\alpha(x),\beta(x)</equation>是非零无穷小量，则以下的命题中：<equation>\textcircled{1}</equation>若<equation>\alpha(x)\sim\beta(x)</equation>，则<equation>\alpha^{2}(x)\sim\beta^{2}(x)</equation><equation>\textcircled{2}</equation>若<equation>\alpha^{2}(x)\sim\beta^{2}(x)</equation>，则<equation>\alpha(x)\sim\beta(x)</equation><equation>\textcircled{3}</equation>若<equation>\alpha(x)\sim\beta(x)</equation>，则<equation>\alpha(x)-\beta(x)=o(\alpha(x))</equation><equation>\textcircled{4}</equation>若<equation>\alpha(x)-\beta(x)=o(\alpha(x))</equation>，则<equation>\alpha(x)\sim\beta(x)</equation>真命题的序号为（    ）

A.<equation>\textcircled{1}\textcircled{3}</equation>B.<equation>\textcircled{1}\textcircled{4}</equation>C.<equation>\textcircled{1}\textcircled{3}\textcircled{4}</equation>D.<equation>\textcircled{2}\textcircled{3}\textcircled{4}</equation>

答案: C

**解析:**解 依次分析四个命题.

若<equation>\alpha(x)\sim\beta(x)</equation>，则<equation>\lim_{x\to0}\frac{\alpha(x)}{\beta(x)}=1</equation>，从而<equation>\lim_{x\to0}\frac{\alpha^{2}(x)}{\beta^{2}(x)}=1</equation>，即<equation>\alpha^{2}(x)\sim\beta^{2}(x).</equation>命题<equation>\textcircled{1}</equation>是真命题由<equation>\alpha^{2}(x)\sim\beta^{2}(x)</equation>并不能得到<equation>\alpha(x)\sim\beta(x).</equation>考虑<equation>\beta(x)=-\alpha(x)</equation>，则<equation>\lim_{x\to0}\frac{\alpha^{2}(x)}{\beta^{2}(x)}=\lim_{x\to0}\frac{\alpha^{2}(x)}{\alpha^{2}(x)}= 1</equation>，即<equation>\alpha^{2}(x)\sim\beta^{2}(x)</equation>，但<equation>\lim_{x\to0}\frac{\alpha(x)}{\beta(x)}=\lim_{x\to0}\frac{\alpha(x)}{- \alpha(x)}=-1, \alpha(x)</equation>与<equation>\beta(x)</equation>只是同阶但并不等价的无穷小量命题<equation>\textcircled{2}</equation>不是真命题.

要说明<equation>\alpha ( x )-\beta ( x )=o( \alpha ( x ) )</equation>，只需说明<equation>\lim_{x\to 0}\frac{\alpha ( x )-\beta ( x )}{\alpha ( x )}=0.</equation><equation>\lim _ {x \rightarrow 0} \frac {\alpha (x) - \beta (x)}{\alpha (x)} = 1 - \lim _ {x \rightarrow 0} \frac {\beta (x)}{\alpha (x)} \frac {\alpha (x) \sim \beta (x)}{1 - 1} 1 - 1 = 0.</equation>命题<equation>\textcircled{3}</equation>是真命题.

要说明<equation>\alpha ( x )\sim \beta ( x )</equation>，只需说明<equation>\lim_{x\to 0}\frac{\beta ( x )}{\alpha ( x )}=1.</equation><equation>\lim _ {x \rightarrow 0} \frac {\beta (x)}{\alpha (x)} = \lim _ {x \rightarrow 0} \frac {\alpha (x) - [ \alpha (x) - \beta (x) ]}{\alpha (x)} = 1 - \lim _ {x \rightarrow 0} \frac {\alpha (x) - \beta (x)}{\alpha (x)} = 1 - 0 = 1.</equation>命题<equation>\textcircled{4}</equation>是真命题.

综上所述，应选C.

---

**2021年第1题 | 选择题 | 5分 | 答案: C**

1. 当<equation>x \rightarrow 0</equation>时，<equation>\int_{0}^{x^{2}}(\mathrm{e}^{t^{3}}-1)\mathrm{d}t</equation>是<equation>x^{7}</equation>的（    ）

A. 低阶无穷小 B. 等价无穷小

C. 高阶无穷小 D. 同阶但非等价无穷小

答案: C

**解析:**解 计算<equation>\lim_{x\to 0}\frac{\int_{0}^{x^{2}}(\mathrm{e}^{t^{3}}-1)\mathrm{d}t}{x^{7}}</equation>来比较这两个无穷小量的阶.<equation>\lim _ {x \rightarrow 0} \frac {\int_ {0} ^ {x ^ {2}} \left(\mathrm {e} ^ {t ^ {3}} - 1\right) \mathrm {d} t}{x ^ {7}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\left(\mathrm {e} ^ {x ^ {6}} - 1\right) \cdot 2 x}{7 x ^ {6}} \xlongequal {\text {e} ^ {x ^ {6}} - 1 \sim x ^ {6}} \lim _ {x \rightarrow 0} \frac {x ^ {6} \cdot 2 x}{7 x ^ {6}} = 0.</equation>因此，<equation>\int_{0}^{x^{2}}(\mathrm{e}^{t^{3}}-1)\mathrm{d}t</equation>是<equation>x^{7}</equation>的高阶无穷小.应选C.

---

**2020年第1题 | 选择题 | 4分 | 答案: D**

1.<equation>x \rightarrow 0^{+}</equation>时，下列无穷小量中最高阶是（    ）

A.<equation>\int_{0}^{x} \left( \mathrm{e}^{t^{2}}-1 \right) \mathrm{d} t</equation>B.<equation>\int_{0}^{x} \ln(1+\sqrt{t^{3}}) \mathrm{d} t</equation>C.<equation>\int_{0}^{\sin x} \sin t^{2} \mathrm{d} t</equation>D.<equation>\int_{0}^{1-\cos x} \sqrt{\sin^{3} t} \mathrm{d} t</equation>

答案: D

**解析:**解 由于求一次导，无穷小量的阶数降低1，且选项A、B的积分上、下限相同，故比较这两项的无穷小量的阶的大小，可以转化为比较它们的被积函数的阶。又因为<equation>t\to 0^{+}</equation>时，<equation>\mathrm{e}^{t^{2}}-1\sim t^{2},</equation><equation>\ln(1+\sqrt{t^{3}})\sim t^{\frac{3}{2}}</equation>，所以<equation>\int_{0}^{x}\left(\mathrm{e}^{t^{2}}-1\right)\mathrm{d}t</equation>与<equation>x^{3}</equation>同阶，比<equation>\int_{0}^{x}\ln(1+\sqrt{t^{3}})\mathrm{d}t</equation>高阶.

比较<equation>\int_{0}^{\sin x}\sin t^{2}\mathrm{d}t</equation>与<equation>x^{3}</equation>的阶.<equation>\begin{aligned} \lim _ {x \rightarrow 0 ^ {+}} \frac {\int_ {0} ^ {\sin x} \sin t ^ {2} \mathrm {d} t}{x ^ {3}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sin (\sin x) ^ {2} \cdot \cos x}{3 x ^ {2}} &= \frac {1}{3} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sin (\sin x) ^ {2}}{x ^ {2}} \xlongequal {\frac {\sin u \sim u}{u \rightarrow 0}} \frac {1}{3} \lim _ {x \rightarrow 0 ^ {+}} \frac {(\sin x) ^ {2}}{x ^ {2}} \\ &= \frac {1}{3} \lim _ {x \rightarrow 0 ^ {+}} \left(\frac {\sin x}{x}\right) ^ {2} \xlongequal {\sin x \sim x} \frac {1}{3}. \end{aligned}</equation>于是，<equation>\int_{0}^{\sin x}\sin t^{2}\mathrm{d}t</equation>也与<equation>x^{3}</equation>同阶.

比较<equation>\int_{0}^{1-\cos x}\sqrt{\sin^{3}t}\mathrm{d}t</equation>与<equation>x^{3}</equation>的阶.<equation>\begin{aligned} \lim _ {x \rightarrow 0 ^ {+}} \frac {\int_ {0} ^ {1 - \cos x} \sqrt {\sin^ {3} t} \mathrm {d} t}{x ^ {3}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sqrt {\sin^ {3} (1 - \cos x)} \sin x}{3 x ^ {2}} \xlongequal {\sin x \sim x} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sin^ {\frac {3}{2}} (1 - \cos x)}{3 x} \\ &= \lim _ {x \rightarrow 0 ^ {+}} \frac {\sin^ {\frac {3}{2}} (1 - \cos x)}{(1 - \cos x) ^ {\frac {3}{2}}} \cdot \frac {(1 - \cos x) ^ {\frac {3}{2}}}{3 x} \\ \frac {1 - \cos x \sim \frac {x ^ {2}}{2}}{} {\lim _ {x \rightarrow 0 ^ {+}} \left[ \frac {\sin (1 - \cos x)}{1 - \cos x} \right] ^ {\frac {3}{2}} \cdot \frac {\left(\frac {x ^ {2}}{2}\right) ^ {\frac {3}{2}}}{3 x}} \\ &= 1 \times 0 = 0. \end{aligned}</equation>因此，<equation>\int_{0}^{1-\cos x}\sqrt{\sin^{3}t}\mathrm{d}t</equation>比<equation>x^{3}</equation>高阶，从而比选项A、B、C中的无穷小量均高阶.应选D.

---

**2016年第1题 | 选择题 | 4分 | 答案: B**

1. 设<equation>\alpha_{1}=x(\cos \sqrt{x}-1),\alpha_{2}=\sqrt{x}\ln(1+\sqrt[3]{x}),\alpha_{3}=\sqrt[3]{x+1}-1</equation>.当<equation>x\rightarrow 0^{+}</equation>时，以上3个无穷小量按照从低阶到高阶的排序是（    ）

A.<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>B.<equation>\alpha_{2},\alpha_{3},\alpha_{1}</equation>C.<equation>\alpha_{2},\alpha_{1},\alpha_{3}</equation>D.<equation>\alpha_{3},\alpha_{2},\alpha_{1}</equation>

答案: B

**解析:**解 由于当<equation>x\to 0^{+}</equation>时，<equation>\cos \sqrt {x} - 1 \sim - \frac {1}{2} (\sqrt {x}) ^ {2} = - \frac {x}{2}, \ln \left(1 + \sqrt [ 3 ]{x}\right) \sim \sqrt [ 3 ]{x}, \sqrt [ 3 ]{x + 1} - 1 = (x + 1) ^ {\frac {1}{3}} - 1 \sim \frac {x}{3},</equation>故<equation>\alpha_ {1} = x \left(\cos \sqrt {x} - 1\right) \sim x \cdot \left(- \frac {x}{2}\right) = - \frac {x ^ {2}}{2}, \quad \alpha_ {2} = \sqrt {x} \ln \left(1 + \sqrt [ 3 ]{x}\right) \sim x ^ {\frac {1}{2}} \cdot x ^ {\frac {1}{3}} = x ^ {\frac {5}{6}},</equation><equation>\alpha_ {3} = \sqrt [ 3 ]{x + 1} - 1 \sim \frac {x}{3}.</equation>比较<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>的阶，只需要比较与<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>等价的<equation>-\frac{x^{2}}{2},x^{\frac{5}{6}},\frac{x}{3}</equation>中 x的次数，次数越高，无穷小量的阶越高.

因此，正确的排序（阶从低到高）应当为<equation>\alpha_{2},\alpha_{3},\alpha_{1}</equation>应选B.

---

**2013年第1题 | 选择题 | 4分 | 答案: C**

1. 设<equation>\cos x-1=x\sin \alpha (x)</equation>，其中<equation>|\alpha (x)|<\frac{\pi}{2}</equation>，则当 x→0时，<equation>\alpha (x)</equation>是（    )

A. 比 x 高阶的无穷小量 B. 比 x 低阶的无穷小量

C. 与 x 同阶但不等价的无穷小量 D. 与 x 等价的无穷小量

答案: C

**解析:**解 首先说明<equation>\alpha(x)</equation>是<equation>x\rightarrow0</equation>时的无穷小量.<equation>\lim _ {x \rightarrow 0} \frac {\sin \alpha (x)}{x} = \lim _ {x \rightarrow 0} \frac {\cos x - 1}{x ^ {2}} \xlongequal {\cos x - 1 \sim - \frac {1}{2} x ^ {2}} \lim _ {x \rightarrow 0} \frac {- \frac {1}{2} x ^ {2}}{x ^ {2}} = - \frac {1}{2}.</equation>由于<equation>\lim_{x\to 0}\frac{\sin \alpha (x)}{x} = -\frac{1}{2}</equation>，而分母 x趋于零，故必有<equation>\lim_{x\to 0}\sin \alpha (x) = 0.</equation>又由于<equation>|\alpha (x)| < \frac{\pi}{2},\sin x</equation>在<equation>\left(-\frac{\pi}{2},\frac{\pi}{2}\right)</equation>上有连续的反函数<equation>arcsin x</equation>，从而<equation>\lim _ {x \rightarrow 0} \alpha (x) = \lim _ {x \rightarrow 0} \arcsin [ \sin \alpha (x) ] = 0.</equation><equation>\alpha (x)</equation>是<equation>x\to 0</equation>时的无穷小量，<equation>\sin \alpha (x)\sim \alpha (x)(x\to 0)</equation>.

因此，<equation>\lim_{x\to 0}\frac{\alpha (x)}{x}\frac{\sin \alpha (x)\sim \alpha (x)}{=}\lim_{x\to 0}\frac{\sin \alpha (x)}{x}=-\frac{1}{2},\alpha (x)</equation>是与<equation>x</equation>同阶但不等价的无穷小量.应选C.

---


#### 函数的连续性与间断点的类型


**2024年第1题 | 选择题 | 5分 | 答案: C**
1. 函数<equation>f ( x )=\left| x \right|^{\frac{1}{(1-x)(x-2)}}</equation>的第一类间断点的个数是（    )

A.3 B.2 C.1 D.0
答案: C
**解析: **解<equation>f(x)</equation>的间断点为<equation>x = 0, x = 1, x = 2</equation>，分别计算这三个点处的左、右极限.由于<equation>f(x) = \mathrm{e}^{\frac{\ln|x|}{(1 - x)(x - 2)}}</equation>，故<equation>\lim f(x) = \lim \mathrm{e}^{\frac{\ln|x|}{(1 - x)(x - 2)}} = \mathrm{e}^{\lim \frac{\ln|x|}{(1 - x)(x - 2)}}</equation>.并且，<equation>\lim _ {x \rightarrow 0 ^ {-}} \frac {\ln (- x)}{(1 - x) (x - 2)} = - \frac {1}{2} \lim _ {x \rightarrow 0 ^ {-}} \ln (- x) = + \infty ,</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {\ln x}{(1 - x) (x - 2)} = - \frac {1}{2} \lim _ {x \rightarrow 0 ^ {+}} \ln x = + \infty ,</equation><equation>\lim _ {x \rightarrow 1 ^ {-}} \frac {\ln x}{(1 - x) (x - 2)} = - \lim _ {x \rightarrow 1 ^ {-}} \frac {\ln x}{1 - x} \xlongequal {\text {洛必达}} - \lim _ {x \rightarrow 1 ^ {-}} \frac {1 / x}{- 1} = 1,</equation><equation>\lim _ {x \rightarrow 1 ^ {+}} \frac {\ln x}{(1 - x) (x - 2)} = - \lim _ {x \rightarrow 1 ^ {+}} \frac {\ln x}{1 - x} \xlongequal {\text {洛必达}} - \lim _ {x \rightarrow 1 ^ {+}} \frac {1 / x}{- 1} = 1,</equation><equation>\lim _ {x \rightarrow 2 ^ {-}} \frac {\ln x}{(1 - x) (x - 2)} = - \ln 2 \lim _ {x \rightarrow 2 ^ {-}} \frac {1}{x - 2} = + \infty ,</equation><equation>\lim _ {x \rightarrow 2 ^ {+}} \frac {\ln x}{(1 - x) (x - 2)} = - \ln 2 \lim _ {x \rightarrow 2 ^ {+}} \frac {1}{x - 2} = - \infty ,</equation>故<equation>\lim_{x\to 0}f(x)=+\infty, \lim_{x\to 1^{-}}f(x)=\lim_{x\to 1^{+}}f(x)=\mathrm{e}, \lim_{x\to 2^{-}}f(x)=+\infty, \lim_{x\to 2^{+}}f(x)=0. x=1</equation>为<equation>f(x)</equation>的可去间断点，<equation>x=0,x=2</equation>为<equation>f(x)</equation>的无穷间断点.

因此，仅有<equation>x = 1</equation>为<equation>f(x)</equation>的第一类间断点，应选C.

---

**2020年第2题 | 选择题 | 4分 | 答案: C**
2. 函数<equation>f(x)=\frac{\mathrm{e}^{\frac{1}{x-1}}\ln|1+x|}{(\mathrm{e}^{x}-1)(x-2)}</equation>的第二类间断点的个数为（    )

A.1 B.2 C.3 D.4
答案: C
**解析: **解 从 f(x)的表达式可以看出，<equation>x=-1,x=0,x=1,x=2</equation>为 f(x)的间断点.下面分别计算这些点处的左、右极限.<equation>\lim _ {x \rightarrow - 1} f (x) = \lim _ {x \rightarrow - 1} \frac {\mathrm {e} ^ {\frac {1}{x - 1}} \ln | 1 + x |}{\left(\mathrm {e} ^ {x} - 1\right) (x - 2)} = \frac {\mathrm {e} ^ {- \frac {1}{2}}}{\left(\mathrm {e} ^ {- 1} - 1\right) \cdot (- 3)} \lim _ {x \rightarrow - 1} \ln | 1 + x | = \infty .</equation><equation>\lim _ {x \rightarrow 0} f (x) = \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {\frac {1}{x - 1}} \ln | 1 + x |}{\left(\mathrm {e} ^ {x} - 1\right) (x - 2)} = \frac {\mathrm {e} ^ {- 1}}{- 2} \lim _ {x \rightarrow 0} \frac {\ln | 1 + x |}{\mathrm {e} ^ {x} - 1} \frac {\frac {\ln | 1 + x | \sim x}{\mathrm {e} ^ {x} - 1 \sim x}}{- \frac {1}{2 \mathrm {e}} \lim _ {x \rightarrow 0} \frac {x}{x}} = - \frac {1}{2 \mathrm {e}}.</equation><equation>\lim _ {x \rightarrow 1 ^ {+}} f (x) = \lim _ {x \rightarrow 1 ^ {+}} \frac {\mathrm {e} ^ {\frac {1}{x - 1}} \ln | 1 + x |}{\left(\mathrm {e} ^ {x} - 1\right) (x - 2)} = - \frac {\ln 2}{\mathrm {e} - 1} \lim _ {x \rightarrow 1 ^ {+}} \mathrm {e} ^ {\frac {1}{x - 1}} = \infty .</equation><equation>\lim _ {x \rightarrow 2} f (x) = \lim _ {x \rightarrow 2} \frac {\mathrm {e} ^ {\frac {1}{x - 1}} \ln | 1 + x |}{\left(\mathrm {e} ^ {x} - 1\right) (x - 2)} = \frac {\mathrm {e} \ln 3}{\mathrm {e} ^ {2} - 1} \lim _ {x \rightarrow 2} \frac {1}{x - 2} = \infty .</equation>因此，<equation>x=-1,x=1</equation>和 x=2均为 f(x)的无穷间断点，从而也是第二类间断点. f(x)共有3个第二类间断点.应选C.

---

**2018年第3题 | 选择题 | 4分 | 答案: D**
3. 设函数 f(x) =<equation>\left\{\begin{array}{l l} - 1, & x < 0, \\ 1, & x \geqslant 0, \end{array} \right.</equation>g(x) =<equation>\left\{\begin{array}{l l} 2 - a x, & x \leqslant - 1, \\ x, & - 1 < x < 0, \\ x - b, & x \geqslant 0. \end{array} \right.</equation>若 f(x) + g(x)在R上连续，则（    )

A. a=3,b=1 B. a=3,b=2 C. a=-3,b=1 D. a=-3,b=2
答案: D
**解析: **解 当<equation>x\leqslant -1</equation>时，<equation>f(x)+g(x)=-1+(2-ax)=1-ax.</equation>当<equation>- 1 < x < 0</equation>时，<equation>f ( x )+g ( x )=-1+x.</equation>当<equation>x\geqslant0</equation>时，<equation>f(x)+g(x)=1+(x-b)=1-b+x.</equation>于是，<equation>f ( x ) + g ( x ) = \left\{ \begin{array}{ll} 1 - a x, & x \leqslant - 1, \\ - 1 + x, & - 1 < x < 0, \\ 1 - b + x, & x \geqslant 0. \end{array} \right.</equation>由于<equation>f ( x )+g ( x )</equation>在R上连续，故<equation>f ( x )+g ( x )</equation>在<equation>x=-1</equation>和<equation>x=0</equation>处均连续.

因为<equation>\lim_{x\rightarrow -1^{+}}[f(x)+g(x)]=\lim_{x\rightarrow -1^{+}}(-1+x)=-2</equation>，而<equation>\left.[f(x)+g(x)]\right|_{x=-1}=1+a</equation>，所以 1+a=-2，即 a=-3.

又因为<equation>\lim_{x\rightarrow 0^{-}}[f(x)+g(x)]=\lim_{x\rightarrow 0^{-}}(-1+x)=-1</equation>，而<equation>[f(x)+g(x)]\bigg|_{x=0}=1-b</equation>，所以 1-b=-1，即 b=2.

因此，a=-3，b=2.应选D.

---

**2017年第1题 | 选择题 | 4分 | 答案: A**
1. 若函数 f(x)<equation>\left\{\begin{array}{l l}{\frac{1-\cos \sqrt{x}}{ax},}&{x>0,}\\ {b,}&{x\leqslant 0}\end{array}\right.</equation>在 x=0处连续，则（    )

A.<equation>a b=\frac{1}{2}</equation>B.<equation>a b=-\frac{1}{2}</equation>C.<equation>a b=0</equation>D.<equation>a b=2</equation>
答案: A
**解析: **解 f(x)是分段函数.代入 f(x)在<equation>(-\infty, 0]</equation>和<equation>(0, +\infty)</equation>上的表达式，分别计算<equation>\lim_{x\rightarrow 0^{+}}f(x),</equation><equation>\lim_{x\rightarrow 0^{+}}f(x).</equation><equation>\lim _ {x \rightarrow 0 ^ {-}} f (x) = f (0) = b,</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} f (x) = \lim _ {x \rightarrow 0 ^ {+}} \frac {1 - \cos \sqrt {x}}{a x} \frac {1 - \cos \sqrt {x} \sim \frac {1}{2} (\sqrt {x}) ^ {2}}{\overline {{=}}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {x}{2}}{a x} = \frac {1}{2 a}.</equation>因此，<equation>b=\frac{1}{2a}</equation>，即<equation>a b=\frac{1}{2}.</equation>应选A.

---

**2015年第2题 | 选择题 | 4分 | 答案: B**
2. 函数<equation>f ( x )=\lim_{t\rightarrow 0}\left( 1+\frac{\sin t}{x}\right)^{\frac{x^{2}}{t}}</equation>在<equation>(-\infty, +\infty)</equation>内（    ）

A. 连续 B. 有可去间断点 C. 有跳跃间断点 D. 有无穷间断点
答案: B
**解析: **解 由<equation>f ( x )</equation>的表达式可以看出，<equation>f ( x )</equation>在<equation>x=0</equation>处无定义.

当<equation>x\neq 0</equation>时，<equation>f(x) = \lim_{t\to 0}\left(1 + \frac{\sin t}{x}\right)^{\frac{x^2}{t}}.</equation>下面我们用两种方法计算<equation>\lim_{t\to 0}\left(1 + \frac{\sin t}{x}\right)^{\frac{x^2}{t}}.</equation>（法一）凑重要极限.<equation>\lim _ {t \rightarrow 0} \left(1 + \frac {\sin t}{x}\right) ^ {\frac {x ^ {2}}{t}} = \lim _ {t \rightarrow 0} \left[ \left(1 + \frac {\sin t}{x}\right) ^ {\frac {x}{\sin t}} \right] ^ {\frac {x \sin t}{t}} = \mathrm {e} ^ {\lim _ {t \rightarrow 0} \frac {x \sin t}{t}} \xlongequal {\sin t \sim t} \mathrm {e} ^ {x}.</equation>（法二）取对数.<equation>\lim_{t \to 0} \left(1 + \frac{\sin t}{x}\right)^{\frac{x^{2}}{t}} = \lim_{t \to 0} \left[\left(1 + \frac{\sin t}{x}\right)^{\frac{x}{\sin t}}\right]^{\frac{x \sin t}{t}} = \mathrm{e}^{\lim_{t \to 0} \frac{x \sin t}{t}} \xlongequal{\sin t \sim t} \mathrm{e}^{x}.</equation>于是，当<equation>x\neq 0</equation>时，<equation>f(x) = \mathrm{e}^{x},\lim_{x\to 0}f(x) = \mathrm{e}^{0} = 1.</equation>因此，<equation>x = 0</equation>为<equation>f(x)</equation>的可去间断点.应选B.

---

**2010年第1题 | 选择题 | 4分 | 答案: B**
1. 函数<equation>f ( x )=\frac{x^{2}-x}{x^{2}-1}\sqrt{1+\frac{1}{x^{2}}}</equation>的无穷间断点的个数为（    ）

A.0 B.1 C.2 D.3
答案: B
**解析: **解 简化 f(x).<equation>f (x) = \frac {x (x - 1)}{(x + 1) (x - 1)} \sqrt {1 + \frac {1}{x ^ {2}}} = \frac {x}{x + 1} \sqrt {1 + \frac {1}{x ^ {2}}}.</equation>考虑<equation>x\to 0</equation>时的情况.因为<equation>\lim _ {x \rightarrow 0} \left(\frac {x}{x + 1} \sqrt {1 + \frac {1}{x ^ {2}}}\right) = \lim _ {x \rightarrow 0} \left(x \sqrt {1 + \frac {1}{x ^ {2}}}\right) = \lim _ {x \rightarrow 0} \left(\frac {x}{| x |} \sqrt {x ^ {2} + 1}\right),</equation>所以，<equation>\lim _ {x \rightarrow 0 ^ {-}} f (x) = \lim _ {x \rightarrow 0 ^ {-}} \left[ \frac {x}{(- x)} \sqrt {x ^ {2} + 1} \right] = - 1, \quad \lim _ {x \rightarrow 0 ^ {+}} f (x) = \lim _ {x \rightarrow 0 ^ {+}} \left(\frac {x}{x} \sqrt {x ^ {2} + 1}\right) = 1.</equation>因此，<equation>x = 0</equation>为<equation>f(x)</equation>的跳跃间断点.

考虑 x→1时的情况.<equation>\lim _ {x \rightarrow 1} f (x) = \lim _ {x \rightarrow 1} \left(\frac {x}{x + 1} \sqrt {1 + \frac {1}{x ^ {2}}}\right) = \frac {\sqrt {2}}{2}.</equation>因此，<equation>x = 1</equation>为<equation>f(x)</equation>的可去间断点.

考虑 x -> -1时的情况.<equation>\lim _ {x \rightarrow - 1} f (x) = \lim _ {x \rightarrow - 1} \left(\frac {x}{x + 1} \sqrt {1 + \frac {1}{x ^ {2}}}\right) = \lim _ {x \rightarrow - 1} \frac {- \sqrt {2}}{x + 1} = \infty .</equation>因此，<equation>x = -1</equation>为<equation>f(x)</equation>的无穷间断点.

综上所述，<equation>f ( x )</equation>的无穷间断点的个数为1.应选B.

---

**2009年第1题 | 选择题 | 4分 | 答案: C**
1. 函数<equation>f(x)=\frac{x-x^{3}}{\sin \pi x}</equation>的可去间断点的个数为（    ）

A.1 B.2 C.3 D.无穷多个
答案: C
**解析: **解 因为当 k为整数时，<equation>\sin k\pi=0</equation>，所以 f(x)在 x=k（k为整数）时无定义，在其余点连续.当<equation>k-k^{3}\neq0</equation>时，即 k≠0，<equation>\pm1</equation>时，<equation>\lim _ {x \rightarrow k} \frac {x - x ^ {3}}{\sin \pi x} = \infty .</equation>x=k为f(x）的无穷间断点.

当<equation>k - k^{3} = 0</equation>时，即<equation>k = 0,\pm 1</equation>时，<equation>\lim_{x\to k}f(x)</equation>为<equation>\frac{0}{0}</equation>型未定式，可用洛必达法则求极限.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {x - x ^ {3}}{\sin \pi x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - 3 x ^ {2}}{\pi \cos \pi x} &= \frac {1}{\pi}, \\ \lim _ {x \rightarrow 1} \frac {x - x ^ {3}}{\sin \pi x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 1} \frac {1 - 3 x ^ {2}}{\pi \cos \pi x} &= \frac {- 2}{- \pi} = \frac {2}{\pi}, \\ \lim _ {x \rightarrow - 1} \frac {x - x ^ {3}}{\sin \pi x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow - 1} \frac {1 - 3 x ^ {2}}{\pi \cos \pi x} &= \frac {- 2}{- \pi} = \frac {2}{\pi}. \end{aligned}</equation>因此，<equation>f ( x )</equation>共有3个可去间断点，<equation>x=0</equation><equation>\pm 1.</equation>应选C.

---


#### 数列敛散性的判定


**2024年第4题 | 选择题 | 5分 | 答案: D**
4. 已知数列<equation>\left\{a_{n}\right\} \left(a_{n}\neq0\right)</equation>，若<equation>\left\{a_{n}\right\}</equation>发散，则（    )

A.<equation>\left\{a_{n}+\frac{1}{a_{n}}\right\}</equation>发散 B.<equation>\left\{a_{n}-\frac{1}{a_{n}}\right\}</equation>发散 C.<equation>\left\{\mathrm{e}^{a_{n}}+\frac{1}{\mathrm{e}^{a_{n}}}\right\}</equation>发散 D.<equation>\left\{\mathrm{e}^{a_{n}}-\frac{1}{\mathrm{e}^{a_{n}}}\right\}</equation>发散
答案: D
**解析: **解考虑函数<equation>f ( x )=\mathrm{e}^{x}-\frac{1}{\mathrm{e}^{x}}</equation>，则<equation>f^{\prime}(x)=\mathrm{e}^{x}+\mathrm{e}^{-x}>0</equation>，故<equation>f ( x )</equation>是在<equation>(-\infty , +\infty)</equation>上单调增加的连续函数，从而存在反函数<equation>f^{-1}(x), f^{-1}(x)</equation>也是在<equation>(-\infty , +\infty)</equation>上单调增加的连续函数.

记<equation>b_{n} = \mathrm{e}^{a_{n}} - \frac{1}{\mathrm{e}^{a_{n}}}</equation>，即<equation>b_{n} = f\left(a_{n}\right)</equation>，于是，<equation>a_{n} = f^{-1}\left(f\left(a_{n}\right)\right) = f^{-1}\left(b_{n}\right)</equation>. 若<equation>\{b_{n}\}</equation>收敛，即存在<equation>b</equation>，使得<equation>\lim_{n\to \infty}b_n = b</equation>，则<equation>\lim _ {n \rightarrow \infty} a _ {n} = \lim _ {n \rightarrow \infty} f ^ {- 1} \left(b _ {n}\right) = f ^ {- 1} \left(\lim _ {n \rightarrow \infty} b _ {n}\right) = f ^ {- 1} (b).</equation>由此可得，<equation>\lim_{n\to \infty}a_n</equation>存在.但这与<equation>\{a_n\}</equation>发散矛盾.

因此，<equation>\{b_{n}\}</equation>发散，即<equation>\left\{\mathrm{e}^{a_n} - \frac{1}{\mathrm{e}^{a_n}}\right\}</equation>发散，应选D.

下面说明选项 A、B、C 均不正确.

对选项A，取<equation>a_{n} = \left\{ \begin{array}{ll} 2, & n = 2k - 1, \\ \frac{1}{2}, & n = 2k, \end{array} \right.</equation><equation>k = 1,2,\dots</equation>，则<equation>\{a_{n}\}</equation>发散，但<equation>a_{n} + \frac{1}{a_{n}}\equiv 2 + \frac{1}{2} = \frac{5}{2},</equation><equation>\left\{a_{n} + \frac{1}{a_{n}}\right\}</equation>收敛.

对选项B、C，取<equation>a_{n} = (-1)^{n}</equation>，则<equation>\left\{a_{n}\right\}</equation>发散，但<equation>a_{n}-\frac{1}{a_{n}}\equiv 0,\mathrm{e}^{a_{n}}+\frac{1}{\mathrm{e}^{a_{n}}}\equiv \mathrm{e}+\frac{1}{\mathrm{e}},\left\{a_{n}-\frac{1}{a_{n}}\right\},</equation><equation>\left\{\mathrm{e}^{a_{n}}+\frac{1}{\mathrm{e}^{a_{n}}}\right\}</equation>均收敛.

---

**2022年第6题 | 选择题 | 5分 | 答案: D**
6. 设数列<equation>\{x_{n}\}</equation>满足<equation>-\frac{\pi}{2}\leqslant x_{n}\leqslant \frac{\pi}{2}</equation>，则（    )

A. 若<equation>\lim_{n\rightarrow \infty}\cos(\sin x_{n})</equation>存在，则<equation>\lim_{n\rightarrow \infty}x_{n}</equation>存在

B. 若<equation>\lim_{n\rightarrow \infty}\sin(\cos x_{n})</equation>存在，则<equation>\lim_{n\rightarrow \infty}x_{n}</equation>存在

C. 若<equation>\lim_{n\rightarrow \infty}\cos(\sin x_{n})</equation>存在，则<equation>\lim_{n\rightarrow \infty}\sin x_{n}</equation>存在，但<equation>\lim_{n\rightarrow \infty}x_{n}</equation>不一定存在

D. 若<equation>\lim_{n\rightarrow \infty}\sin(\cos x_{n})</equation>存在，则<equation>\lim_{n\rightarrow \infty}\cos x_{n}</equation>存在，但<equation>\lim_{n\rightarrow \infty}x_{n}</equation>不一定存在
答案: D
**解析: **解 若<equation>\lim_{n\rightarrow \infty}\sin(\cos x_{n})</equation>存在，则将其记为 a.由于<equation>\sin x</equation>在<equation>\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>上存在反函数<equation>\arcsin x</equation>，故<equation>\lim_{n\rightarrow \infty}\cos x_{n}=\lim_{n\rightarrow \infty}\arcsin(\sin(\cos x_{n}))=\arcsin(\lim_{n\rightarrow \infty}\sin(\cos x_{n}))=\arcsin a.</equation>但是<equation>\lim_{n\rightarrow \infty}\cos x_{n}</equation>存在并不能保证<equation>\lim_{n\rightarrow \infty}x_{n}</equation>存在.例如取<equation>x_{n}=(-1)^{n}\frac{\pi}{2}</equation>，则<equation>\lim_{n\rightarrow \infty}\cos x_{n}=0</equation>，但<equation>\lim_{n\rightarrow \infty}x_{n}</equation>不存在.选项B错误，选项D正确.应选D.

由于<equation>\cos x</equation>在<equation>\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>上并不单调，故由<equation>\lim_{n\to \infty}\cos(\sin x_{n})</equation>存在并不能保证<equation>\lim_{n\to \infty}\sin x_{n}</equation>存在.同样取<equation>x_{n}=(-1)^{n}\frac{\pi}{2}</equation>，则<equation>\lim_{n\to \infty}\cos(\sin x_{n})=\cos1</equation>，但<equation>\lim_{n\to \infty}\sin x_{n}</equation>和<equation>\lim_{n\to \infty}x_{n}</equation>均不存在.选项A、C不正确.
