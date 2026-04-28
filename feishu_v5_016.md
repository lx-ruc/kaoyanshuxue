---

**2023年第20题 | 解答题 | 12分**

20. (本题满分12分)

设函数 f(x)在<equation>[-a,a]</equation>上有二阶连续导数.证明：

I. 若 f(0)=0，则存在<equation>\xi\in(-a,a)</equation>，使得<equation>f^{\prime\prime}(\xi)=\frac{1}{a^{2}}[f(a)+f(-a)]；

II. 若 f(x)在</equation>(-a,a)<equation>内取得极值，则存在</equation>\eta\in(-a,a)<equation>，使得</equation>|f^{\prime\prime}(\eta)|\geqslant\frac{1}{2a^{2}}|f(a)-f(-a)|. $

**答案:**# （I）证明略；

（Ⅱ）证明略.

**解析:**证（ I ）由 f（ x ）的泰勒公式可得<equation>f (a) = f (0) + f ^ {\prime} (0) a + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {1}\right) a ^ {2} \stackrel {f (0) = 0} {=} f ^ {\prime} (0) a + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {1}\right) a ^ {2},</equation><equation>f (- a) = f (0) + f ^ {\prime} (0) \cdot (- a) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {2}\right) a ^ {2} \stackrel {f (0) = 0} {=} f ^ {\prime} (0) \cdot (- a) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {2}\right) a ^ {2},</equation>其中<equation>\xi_{1}\in(0,a),\xi_{2}\in(-a,0).</equation>两式相加可得<equation>f (a) + f (- a) = \frac {a ^ {2}}{2} \left[ f ^ {\prime \prime} \left(\xi_ {1}\right) + f ^ {\prime \prime} \left(\xi_ {2}\right) \right].</equation>记<equation>\max \left\{f^{\prime \prime}\left(\xi_{1}\right),f^{\prime \prime}\left(\xi_{2}\right)\right\}=M,</equation><equation>\min \left\{f^{\prime \prime}\left(\xi_{1}\right),f^{\prime \prime}\left(\xi_{2}\right)\right\}=m</equation>，则由（1）式可得<equation>m \leqslant \frac {f (a) + f (- a)}{a ^ {2}} = \frac {1}{2} \left[ f ^ {\prime \prime} \left(\xi_ {1}\right) + f ^ {\prime \prime} \left(\xi_ {2}\right) \right] \leqslant M.</equation>由于 f(x)在<equation>[-a,a]</equation>上有二阶连续导数，故由连续函数的介值定理可知，存在<equation>\xi \in[ \xi_{2},\xi_{1} ]\subset(-a,a)</equation>，使得<equation>f^{\prime \prime}(\xi)=\frac{1}{a^{2}}[f(a)+f(-a)]</equation>（Ⅱ）设<equation>f(x)</equation>在<equation>(-a,a)</equation>内的极值点为<equation>x_{0}</equation>，则<equation>f^{\prime}(x_{0})=0.</equation>由<equation>f(x)</equation>的泰勒公式可得<equation>\begin{array}{l} f (a) = f \left(x _ {0}\right) + f ^ {\prime} \left(x _ {0}\right) \left(a - x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {1}\right) \left(a - x _ {0}\right) ^ {2} \\ \frac {f ^ {\prime} \left(x _ {0}\right) = 0}{\overline {{=}}} f \left(x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {1}\right) \left(a - x _ {0}\right) ^ {2}, \\ \end{array}</equation><equation>\begin{aligned} f (- a) &= f \left(x _ {0}\right) + f ^ {\prime} \left(x _ {0}\right) \left(- a - x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {2}\right) \left(- a - x _ {0}\right) ^ {2} \\ \frac {f ^ {\prime} \left(x _ {0}\right) = 0}{\overline {{}}} f \left(x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {2}\right) \left(a + x _ {0}\right) ^ {2}, \end{aligned}</equation>其中<equation>\eta_{1}\in(x_{0},a),\eta_{2}\in(-a,x_{0}).</equation>两式相减可得<equation>f (a) - f (- a) = \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {1}\right) \left(a - x _ {0}\right) ^ {2} - \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {2}\right) \left(a + x _ {0}\right) ^ {2}.</equation>记<equation>\max \left\{ \left| f^{\prime \prime}\left(\eta_{1}\right)\right|, \left| f^{\prime \prime}\left(\eta_{2}\right)\right| \right\}=M</equation>，则由（2）式可得<equation>\left| f (a) - f (- a) \right| \leqslant \frac {M}{2} \left[ \left(a - x _ {0}\right) ^ {2} + \left(a + x _ {0}\right) ^ {2} \right] = \frac {M}{2} \left(2 a ^ {2} + 2 x _ {0} ^ {2}\right) \leqslant \frac {M}{2} \cdot 4 a ^ {2} = 2 a ^ {2} M.</equation>因此，<equation>M\geqslant \frac{1}{2a^{2}}|f(a) - f(-a)|.</equation>取<equation>\eta \in \{\eta_1, \eta_2\}</equation>使得<equation>|f^{\prime \prime}(\eta)| = M</equation>，则<equation>\eta \in (-a, a)</equation>满足<equation>|f^{\prime \prime}(\eta)| \geqslant \frac{1}{2a^2}|f(a) - f(-a)|</equation>.

---


#### 函数的单调性、极值与最值


**2023年第17题 | 解答题 | 10分**

17. (本题满分10分)

已知可导函数 y=y(x)满足<equation>a \mathrm{e}^{x}+y^{2}+y-\ln(1+x)\cos y+b=0</equation>，且 y(0)=0，<equation>y^{\prime}(0)=0</equation>I. 求 a,b的值；

II. 判断 x=0 是否为 y(x)的极值点.

**答案:**（ I ）<equation>a=1,b=-1;</equation>（ II ）<equation>x=0</equation>是 y(x）的极大值点.

**解析:**解（I）将 y（0）=0代入<equation>a \mathrm{e}^{x}+y^{2}+y-\ln(1+x)\cos y+b=0</equation>中可得，a+b=0.对方程<equation>a \mathrm{e}^{x}+y^{2}+y-\ln(1+x)\cos y+b=0</equation>两端关于 x求导，可得<equation>a \mathrm {e} ^ {x} + 2 y y ^ {\prime} + y ^ {\prime} - \frac {\cos y}{1 + x} + \ln (1 + x) y ^ {\prime} \sin y = 0.</equation>将<equation>y ( 0 )=0, y^{\prime} ( 0 )=0</equation>代入（1）式，可得<equation>a-1=0.</equation>联立可得<equation>\left\{ \begin{array}{l l} a + b = 0, \\ a - 1 = 0, \end{array} \right.</equation>解得<equation>\left\{ \begin{array}{l l} a = 1, \\ b = -1. \end{array} \right.</equation>（Ⅱ）由<equation>y^{\prime}(0)=0</equation>可知 x=0为 y(x）的驻点.如果能确定<equation>y^{\prime\prime}(0)</equation>的符号，那么就能利用一元函数极值的第二充分条件判断 x=0是否为极值点.

将 a=1 代入（1）式，可得<equation>\mathrm {e} ^ {x} + 2 y y ^ {\prime} + y ^ {\prime} - \frac {\cos y}{1 + x} + \ln (1 + x) y ^ {\prime} \sin y = 0.</equation>对（2）式两端关于 x求导，可得<equation>\mathrm {e} ^ {x} + 2 \left(y ^ {\prime}\right) ^ {2} + 2 y y ^ {\prime \prime} + y ^ {\prime \prime} + \frac {\cos y}{(1 + x) ^ {2}} + \frac {2 y ^ {\prime} \sin y}{1 + x} + \ln (1 + x) y ^ {\prime \prime} \sin y + \ln (1 + x) \left(y ^ {\prime}\right) ^ {2} \cos y = 0.</equation>将<equation>y ( 0 ) = 0, y^{\prime} ( 0 ) = 0</equation>代入（3）式可得<equation>y^{\prime \prime} ( 0 ) + 2 = 0.</equation>于是，<equation>y^{\prime \prime} ( 0 ) = - 2 < 0.</equation>由一元函数极值的第二充分条件可知，<equation>x=0</equation>是<equation>y(x)</equation>的极大值点.

---

**2019年第15题 | 解答题 | 10分**

15. (本题满分10分）

已知函数<equation>f ( x )=\left\{\begin{array}{ll}x^{2 x},&x>0,\\ x \mathrm{e}^{x}+1,&x\leqslant 0.\end{array} \right.</equation>求<equation>f^{\prime}(x)</equation>，并求 f(x)的极值.

**答案:**)<equation>f^{\prime}(x)=\left\{\begin{array}{ll}\mathrm{e}^{x}(x+1),&x<0,\\ 2\mathrm{e}^{2x\ln x}(\ln x+1),&x>0.\end{array} \right.</equation>x=-1和 x<equation>=\frac{1} {\mathrm{e}}</equation>是 f(x)的极小值点，极小值分别为 f(-1) =1<equation>-\mathrm{e}^{-1}</equation>和<equation>f\left(\frac{1}{\mathrm{e}}\right)=\mathrm{e}^{-\frac{2}{\mathrm{e}}}</equation>；x=

0是 f(x)的极大值点，极大值为 f(0) =1.

**解析:**解 f(x)是一个分段函数. x=0是分界点.分别计算 x > 0时与 x < 0时的<equation>f^{\prime}(x).</equation>当 x > 0时，<equation>f ^ {\prime} (x) = \left(x ^ {2 x}\right) ^ {\prime} = \left(\mathrm {e} ^ {2 x \ln x}\right) ^ {\prime} = \mathrm {e} ^ {2 x \ln x} \cdot \left(2 \ln x + 2 x \cdot \frac {1}{x}\right) = 2 \mathrm {e} ^ {2 x \ln x} (\ln x + 1).</equation>当 x < 0时，<equation>f ^ {\prime} (x) = \mathrm {e} ^ {x} + x \mathrm {e} ^ {x} = \mathrm {e} ^ {x} (x + 1).</equation>计算<equation>f^{\prime}(0).</equation>由<equation>f ( x )</equation>的定义知<equation>f ( 0 )=1.</equation><equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0 ^ {-}} \frac {x \mathrm {e} ^ {x} + 1 - 1}{x} = \lim _ {x \rightarrow 0 ^ {-}} \mathrm {e} ^ {x} = 1.</equation><equation>\begin{aligned} f _ {+} ^ {\prime} (0) &= \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {2 x \ln x} - 1}{x} \frac {\mathrm {e} ^ {2 x \ln x} - 1 \sim 2 x \ln x}{\lim _ {x \rightarrow 0 ^ {+}} \frac {2 x \ln x}{x}} \\ &= 2 \lim _ {x \rightarrow 0 ^ {+}} \ln x = - \infty . \end{aligned}</equation><equation>f ( x )</equation>的右导数不存在，故<equation>f ( x )</equation>在<equation>x=0</equation>处不可导.

因此，<equation>f^{\prime}(x)=\left\{ \begin{array}{ll}\mathrm{e}^{x}(x+1),&x<0,\\ 2\mathrm{e}^{2x\ln x}(\ln x+1),&x>0. \end{array} \right.</equation>考察 f（x）的极值，需分别考察 f（x）的驻点与不可导点.

令<equation>f^{\prime}(x)=0</equation>当 x > 0时，解得<equation>x=\frac{1} {\mathrm{e}}</equation>当 x < 0时，解得 x=-1.加上不可导点 x=0，这三个点将<equation>(-\infty, +\infty)</equation>分为4个区间.

当 x < -1时，<equation>f^{\prime}(x) < 0,f(x)</equation>单调减少.

当<equation>- 1 < x < 0</equation>时，<equation>f^{\prime}(x) > 0,f(x)</equation>单调增加.

当<equation>0 < x < \frac{1} {\mathrm{e}}</equation>时，<equation>f^{\prime}(x) < 0,f(x)</equation>单调减少.

当 x ><equation>\frac{1} {\mathrm{e}}</equation>时，<equation>f^{\prime}(x) > 0</equation>f(x)单调增加.

注意到 f(x)在 x=0处连续.于是，根据极值的第一充分条件，<equation>x=-1</equation>和<equation>x=\frac{1} {\mathrm{e}}</equation>是 f(x)的极小值点，极小值分别为<equation>f(-1)=1-\mathrm{e}^{-1}</equation>和<equation>f\left(\frac{1}{\mathrm{e}}\right)=\mathrm{e}^{-\frac{2}{\mathrm{e}}}</equation>；x=0是 f(x)的极大值点，极大值为<equation>f(0)=1.</equation>f（x）的单调性与极值可整理如下.

<table border="1"><tr><td>x</td><td><equation>(-\infty,-1)</equation></td><td>-1</td><td><equation>(-1,0)</equation></td><td>0</td><td><equation>(0,\frac{1}{e})</equation></td><td><equation>\frac{1}{e}</equation></td><td><equation>(\frac{1}{e},+\infty)</equation></td></tr><tr><td><equation>f^{\prime}(x)</equation></td><td>-</td><td>0</td><td>+</td><td>不存在</td><td>-</td><td>0</td><td>+</td></tr><tr><td><equation>f(x)</equation></td><td>单调减少</td><td>极小值</td><td>单调增加</td><td>极大值</td><td>单调减少</td><td>极小值</td><td>单调增加</td></tr></table>

---

**2017年第3题 | 选择题 | 4分 | 答案: C**

3. 设函数 f(x)可导，且 f(x)f'(x)>0，则（    ）

A. f(1)>f(-1) B. f(1)<f(-1) C.<equation>|f(1)|>|f(-1)|</equation>D.<equation>|f(1)|<|f(-1)|</equation>

答案: C

**解析:**解（法一）令<equation>F ( x )=f^{2} ( x ).</equation>由题设知，<equation>F^{\prime}(x)=2 f(x) f^{\prime}(x)>0</equation>，故<equation>f^{2}(x)</equation>单调增加，于是<equation>f^{2}(1)>f^{2}(-1)</equation>即<equation>|f(1)|>|f(-1)|</equation>应选C.

（法二）由于<equation>f ( x ) f^{\prime} ( x ) > 0</equation>即恒大于零，故<equation>f ( x )</equation>恒大于零或<equation>f ( x )</equation>恒小于零（否则由<equation>f ( x )</equation>的连续性可知<equation>f ( x )</equation>存在零点，从而<equation>f ( x ) f^{\prime} ( x )</equation>不恒大于零).

若 f(x) > 0，则<equation>f^{\prime}(x) > 0</equation>，故 f(x) 单调增加. 因此 f(1) > f(-1) > 0.

若 f(x) < 0 ，则<equation>f^{\prime}(x) < 0</equation>，故 f(x) 单调减少. 因此 f(1) < f(-1) < 0.

综上所述，<equation>|f(1)| > |f(-1)|</equation>.应选C.

（法三）排除法.

取<equation>f ( x )=\mathrm{e}^{x}</equation>，则<equation>f ( x )</equation>满足<equation>f ( x ) f^{\prime} ( x )=\mathrm{e}^{x}\cdot \mathrm{e}^{x}>0</equation>，且<equation>f (1) > f (- 1) > 0, \quad | f (1) | > | f (- 1) |,</equation>故可以排除选项B、D.

取<equation>f(x)=-\mathrm{e}^{x}</equation>，则 f(x)满足<equation>f(x)f^{\prime}(x)=(-\mathrm{e}^{x})\cdot(-\mathrm{e}^{x})>0</equation>，且<equation>f(1)<f(-1)<0</equation>，故可以排除选项A.

因此，应选C.

---

**2016年第17题 | 解答题 | 10分**

17. (本题满分10分）

设函数<equation>f ( x )=\int_{0}^{1} \left| t^{2}-x^{2} \right| \mathrm{d} t ( x > 0 )</equation>，求<equation>f^{\prime} ( x )</equation>，并求 f(x)的最小值.

**答案:**<equation>f^{\prime}(x) = \left\{ \begin{array}{ll} 4x^{2} - 2x, & 0 < x < 1, \\ 2x, & x \geqslant 1. \end{array} \right.</equation>最小值<equation>f\left(\frac{1}{2}\right) = \frac{1}{4}</equation>.

**解析:**解 对 x的取值范围进行讨论.由<equation>f ( x )=\int_{0}^{1} \mid t^{2}-x^{2} \mid \mathrm{d} t</equation>知，

- 当<equation>x \geqslant 1</equation>时，<equation>x \geqslant t</equation>，<equation>|t^{2} - x^{2}| = x^{2} - t^{2}</equation>.

- 当 0 < x < 1时，有两种情况.<equation>\left| t ^ {2} - x ^ {2} \right| = \left\{ \begin{array}{l l} x ^ {2} - t ^ {2}, & 0 \leqslant t \leqslant x, \\ t ^ {2} - x ^ {2}, & x < t \leqslant 1. \end{array} \right.</equation>于是，当<equation>x\geqslant 1</equation>时，<equation>f (x) = \int_ {0} ^ {1} \left| t ^ {2} - x ^ {2} \right| \mathrm {d} t = \int_ {0} ^ {1} \left(x ^ {2} - t ^ {2}\right) \mathrm {d} t = x ^ {2} - \frac {1}{3}.</equation>当 0 < x < 1时，<equation>\begin{array}{l} f (x) = \int_ {0} ^ {1} \left| t ^ {2} - x ^ {2} \right| \mathrm {d} t = \int_ {0} ^ {x} \left(x ^ {2} - t ^ {2}\right) \mathrm {d} t + \int_ {x} ^ {1} \left(t ^ {2} - x ^ {2}\right) \mathrm {d} t \\ = \left(x ^ {2} t - \frac {t ^ {3}}{3}\right) \Bigg | _ {0} ^ {x} + \left(\frac {t ^ {3}}{3} - x ^ {2} t\right) \Bigg | _ {x} ^ {1} = \frac {4}{3} x ^ {3} - x ^ {2} + \frac {1}{3}. \\ \end{array}</equation>因此，<equation>f ( x ) = \left\{ \begin{array}{l l} \frac{4}{3} x^{3} - x^{2} + \frac{1}{3}, & 0 < x < 1, \\ x^{2} - \frac{1}{3}, & x \geqslant 1. \end{array} \right.</equation>从<equation>f ( x )</equation>的表达式可以看出，<equation>f \left(1 ^ {-}\right) = f \left(1 ^ {+}\right) = f (1) = \frac {2}{3}.</equation>f(x）在 x=1处连续.

由<equation>f ( x )</equation>的表达式可知，当<equation>0 < x < 1</equation>时，<equation>f^{\prime}(x)=4 x^{2}-2 x</equation>；当<equation>x > 1</equation>时，<equation>f^{\prime}(x)=2 x.</equation>当<equation>x=1</equation>时，根据导数的定义分别计算<equation>f ( x )</equation>在<equation>x=1</equation>处的左侧导数和右侧导数.<equation>\begin{aligned} f _ {-} ^ {\prime} (1) &= \lim _ {x \rightarrow 1 ^ {-}} \frac {\frac {4}{3} x ^ {3} - x ^ {2} - \frac {1}{3}}{x - 1} = \lim _ {x \rightarrow 1 ^ {-}} \frac {\frac {4}{3} x ^ {3} - \frac {4}{3} x ^ {2} + \frac {1}{3} x ^ {2} - \frac {1}{3}}{x - 1} \\ &= \lim _ {x \rightarrow 1 ^ {-}} \frac {(x - 1) \left[ \frac {4}{3} x ^ {2} + \frac {1}{3} (x + 1) \right]}{x - 1} = \lim _ {x \rightarrow 1 ^ {-}} \left[ \frac {4}{3} x ^ {2} + \frac {1}{3} (x + 1) \right] = 2, \end{aligned}</equation><equation>f _ {+} ^ {\prime} (1) = \lim _ {x \rightarrow 1 ^ {+}} \frac {x ^ {2} - 1}{x - 1} = \lim _ {x \rightarrow 1 ^ {+}} (x + 1) = 2.</equation>由此可见，<equation>f^{\prime}(1)=f_{-}^{\prime}(1)=f_{+}^{\prime}(1)=2.</equation>因此，<equation>f ^ {\prime} (x) = \left\{ \begin{array}{l l} 4 x ^ {2} - 2 x, & 0 < x < 1, \\ 2 x, & x \geqslant 1. \end{array} \right.</equation>当 x > 1时，<equation>f^{\prime}(x)=2x>0</equation>，故 f(x)在（1，<equation>+\infty</equation>）内单调增加.

当<equation>0 < x < 1</equation>时，<equation>f^{\prime}(x)=4x^{2}-2x</equation>求<equation>f^{\prime}(x)</equation>的零点得，<equation>x=\frac{1}{2}</equation>或<equation>x=0</equation>（舍去）.因此，当<equation>0 < x < \frac{1}{2}</equation>时，<equation>f^{\prime}(x) < 0</equation>；当<equation>\frac{1}{2} < x < 1</equation>时，<equation>f^{\prime}(x) > 0.</equation>由于 f(x) 连续，故可知 f(x) 的最小值在<equation>x=\frac{1}{2}</equation>处取得，即最小值为<equation>f \left(\frac {1}{2}\right) = \frac {4}{3} \times \frac {1}{8} - \frac {1}{4} + \frac {1}{3} = \frac {1}{4}.</equation>

---

**2010年第3题 | 选择题 | 4分 | 答案: B**

3. 设函数 f(x)，g(x)具有二阶导数，且<equation>g^{\prime \prime}(x)<0</equation>. 若 g<equation>( x_{0} )=a</equation>是 g(x)的极值，则 f(g(x))在 x0处取极大值的一个充分条件是（    ）

A.<equation>f^{\prime}(a)<0</equation>B.<equation>f^{\prime}(a)>0</equation>C.<equation>f^{\prime\prime}(a)<0</equation>D.<equation>f^{\prime\prime}(a)>0</equation>

答案: B

**解析:**由于 g(x)在<equation>x_{0}</equation>处取得极值且 g(x)可导，故<equation>g^{\prime}(x_{0})=0.</equation>于是，<equation>[ f (g (x)) ] ^ {\prime} = f ^ {\prime} (g (x)) g ^ {\prime} (x),</equation><equation>[ f (g (x)) ] ^ {\prime \prime} = f ^ {\prime \prime} (g (x)) \left[ g ^ {\prime} (x) \right] ^ {2} + f ^ {\prime} (g (x)) g ^ {\prime \prime} (x).</equation>从而<equation>[f(g(x))]' \mid_{x = x_0} = f'(g(x_0))g'(x_0) = 0, [f(g(x))]'' \mid_{x = x_0} = f'(g(x_0))g''(x_0) = f'(a)g''(x_0).</equation>由于一个二阶可导的函数在某点取得极大值的一个充分条件是该函数在该点处的一阶导数为零，二阶导数小于零，又由于<equation>g^{\prime \prime}(x_{0}) < 0</equation>，故<equation>f(g(x))</equation>在<equation>x_{0}</equation>处取极大值的一个充分条件是<equation>f^{\prime}(a) > 0.</equation>应选B.

从上述过程可以看出，当<equation>f^{\prime}(a) < 0</equation>时，<equation>f(g(x))</equation>在<equation>x_{0}</equation>处取得极小值且<equation>f(g(x))</equation>在<equation>x_{0}</equation>处取得极值与<equation>f^{\prime \prime}(a)</equation>的取值无关，故选项A、C、D都不正确.

---


#### 导数与微分的计算


**2022年第13题 | 填空题 | 5分**

13. 已知函数<equation>f(x)=\mathrm{e}^{\sin x}+\mathrm{e}^{-\sin x}</equation>, 则<equation>f^{\prime\prime\prime}(2\pi)=</equation>___

**解析:**由于<equation>f (- x) = \mathrm {e} ^ {\sin (- x)} + \mathrm {e} ^ {- \sin (- x)} = \mathrm {e} ^ {- \sin x} + \mathrm {e} ^ {\sin x} = f (x),</equation>故 f(x)是偶函数.从而<equation>f^{\prime}(x)</equation>是奇函数，<equation>f^{\prime\prime}(x)</equation>是偶函数，<equation>f^{\prime\prime\prime}(x)</equation>是奇函数.由奇函数的性质可知，<equation>f^{\prime\prime\prime}(0)=0.</equation>又由于<equation>\sin x</equation>是周期为<equation>2\pi</equation>的周期函数，故 f(x)也是周期为<equation>2\pi</equation>的周期函数.从而 f(x)的各阶导函数均是周期为<equation>2\pi</equation>的周期函数.

因此，<equation>f^{\prime \prime \prime}(2\pi)=f^{\prime \prime \prime}(0)=0.</equation>

---

**2021年第11题 | 填空题 | 5分**

**答案:**<equation>\frac {\sin e ^ {- 1}}{2 e}.</equation>

**解析:**根据链式法则，<equation>\frac{\mathrm{d} y}{\mathrm{d} x}=-\sin\mathrm{e}^{-\sqrt{x}}\cdot\mathrm{e}^{-\sqrt{x}}\cdot\left(-\frac{1}{2\sqrt{x}}\right).</equation>代入 x = 1 可得，<equation>\left.\frac{\mathrm{d} y}{\mathrm{d} x}\right|_{x=1}=\frac{1}{2}\cdot\mathrm{e}^{-1}\cdot\sin\mathrm{e}^{-1}=\frac{\sin\mathrm{e}^{-1}}{2\mathrm{e}}.</equation>

---

**2012年第2题 | 选择题 | 4分 | 答案: A**

2. 设函数<equation>f(x)=\mathrm{e}^{x}-1)\mathrm{e}^{2x}-2)\cdots \mathrm{e}^{nx}-n)</equation>，其中 n为正整数，则<equation>f^{\prime}(0)=</equation>(    )

A.<equation>(-1)^{n-1}(n-1)!</equation>B.<equation>(-1)^{n}(n-1)!</equation>C.<equation>(-1)^{n-1}n!</equation>D.<equation>(-1)^{n}n!</equation>

答案: A

**解析:**解（法一）由题设知，<equation>f ( x ) = \left(\mathrm{e}^{x} - 1\right)\left[\left(\mathrm{e}^{2 x} - 2\right)\dots\left(\mathrm{e}^{n x} - n\right)\right]</equation>，再由函数乘积的求导法则知，<equation>f ^ {\prime} (x) = \mathrm {e} ^ {x} \left[ \left(\mathrm {e} ^ {2 x} - 2\right) \dots \left(\mathrm {e} ^ {n x} - n\right) \right] + \left(\mathrm {e} ^ {x} - 1\right) \left[ \left(\mathrm {e} ^ {2 x} - 2\right) \dots \left(\mathrm {e} ^ {n x} - n\right) \right] ^ {\prime},</equation><equation>f ^ {\prime} (0) = (- 1) (- 2) \dots (1 - n) + 0 = (- 1) ^ {n - 1} (n - 1)!</equation>应选A.

（法二）由题设知，<equation>f(0)=0.</equation>根据导数定义有<equation>\begin{array}{l} f ^ {\prime} (0) = \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0} \frac {\left(\mathrm {e} ^ {x} - 1\right)\left(\mathrm {e} ^ {2 x} - 2\right) \cdots \left(\mathrm {e} ^ {n x} - n\right)}{x} \\ \underline {{\mathrm {e} ^ {x} - 1 \sim x}} \lim _ {x \rightarrow 0} \left(\mathrm {e} ^ {2 x} - 2\right) \dots \left(\mathrm {e} ^ {n x} - n\right) = (1 - 2) \dots (1 - n) = (- 1) ^ {n - 1} (n - 1)!. \\ \end{array}</equation>应选A.

（法三）特殊值法.

观察各选项，可知当<equation>n\geqslant 2</equation>时，每个选项的值都不同.取<equation>n = 2</equation>，则<equation>f (x) = \left(\mathrm {e} ^ {x} - 1\right) \left(\mathrm {e} ^ {2 x} - 2\right), f ^ {\prime} (x) = \mathrm {e} ^ {x} \left(\mathrm {e} ^ {2 x} - 2\right) + \left(\mathrm {e} ^ {x} - 1\right) 2 \mathrm {e} ^ {2 x}.</equation>于是<equation>f^{\prime}(0) = -1.</equation>将<equation>n=2</equation>代入各选项，只有选项A的结果等于-1.

因此，应选A.

---

**2012年第10题 | 填空题 | 4分**

10. 设函数<equation>f ( x )=\left\{\begin{array}{ll}\ln \sqrt{x},&x\geqslant 1,\\ 2 x-1,&x<1,\end{array}\right. y=f(f(x))</equation>，则<equation>\left.\frac{\mathrm{d} y}{\mathrm{d} x}\right|_{x=\mathrm{e}}=</equation>___

**解析:**解 由已知条件知<equation>f(\mathrm{e})=\ln \sqrt{\mathrm{e}}=\frac{1}{2}.</equation>由链式法则知，<equation>\begin{array}{l} \left. \frac {\mathrm {d} y}{\mathrm {d} x} \right| _ {x = \mathrm {e}} = f ^ {\prime} (f (x)) \cdot f ^ {\prime} (x) \Big | _ {x = \mathrm {e}} = f ^ {\prime} (f (\mathrm {e})) \cdot f ^ {\prime} (\mathrm {e}) = f ^ {\prime} \left(\frac {1}{2}\right) \cdot f ^ {\prime} (\mathrm {e}) \\ = \frac {\mathrm {d} (2 x - 1)}{\mathrm {d} x} \Big | _ {x = \frac {1}{2}} \cdot \frac {\mathrm {d} (\ln \sqrt {x})}{\mathrm {d} x} \Big | _ {x = \mathrm {e}} = 2 \times \frac {1}{2 \mathrm {e}} = \frac {1}{\mathrm {e}}. \\ \end{array}</equation>

---


#### 方程根的存在性与个数


**2021年第3题 | 选择题 | 5分 | 答案: A**

3. 设函数<equation>f(x)=a x-b \ln x(a>0)</equation>有两个零点，则<equation>\frac{b}{a}</equation>的取值范围是（    ）

A. (e,+<equation>\infty</equation>)

B. (0,e)

C.<equation>\left( 0,\frac{1} {\mathrm{e}} \right)</equation>D.<equation>\left( \frac{1}{\mathrm{e}},+\infty \right)</equation>

答案: A

**解析:**解（法一）<equation>f ( x )</equation>的定义域为（0，<equation>+ \infty</equation>）.计算<equation>f^{\prime}(x)</equation>得<equation>f^{\prime}(x)=a-\frac{b}{x}.</equation>由于 a > 0，故若 b≤0，则<equation>f^{\prime}(x)>0</equation>，f(x)单调增加.此时 f(x)不可能有2个零点.于是，b > 0.

下面分析 f（x）的单调性.

当<equation>x=\frac{b}{a}</equation>时，<equation>f^{\prime}(x)=0</equation>；当<equation>0 < x < \frac{b}{a}</equation>时，<equation>f^{\prime}(x) < 0,f(x)</equation>单调减少；当<equation>x > \frac{b}{a}</equation>时，<equation>f^{\prime}(x) > 0</equation><equation>f(x)</equation>单调增加.于是，<equation>f(x)</equation>在（0，<equation>+\infty</equation>）上先单调减少，再单调增加.<equation>f\left(\frac{b}{a}\right)</equation>为f(x)的最小值.

f(x)有2个零点等价于<equation>f\left(\frac{b}{a}\right)</equation>小于零.否则f(x）恒大于等于零，不可能存在2个零点.<equation>f \left(\frac {b}{a}\right) = a \cdot \frac {b}{a} - b \ln \frac {b}{a} = b - b \ln \frac {b}{a} = b \left(1 - \ln \frac {b}{a}\right) < 0.</equation>又因为<equation>b > 0</equation>，所以<equation>b\left(1-\ln \frac{b}{a}\right)<0</equation>等价于<equation>1-\ln \frac{b}{a}<0</equation>即<equation>\ln \frac{b}{a}>1,\frac{b}{a}>\mathrm{e}.</equation>因此，应选A.

（法二）同法一可知<equation>b > 0.</equation>ax-b<equation>\ln x=0</equation>等价于<equation>\frac{x}{\ln x}=\frac{b}{a}</equation>，故函数 f(x）=ax-b<equation>\ln x</equation>有2个零点等价于曲线 y<equation>=\frac{x}{\ln x}</equation>与直线 y<equation>=\frac{b}{a}</equation>有2个交点.

计算<equation>g ( x )=\frac{x}{\ln x}</equation>的导数<equation>g^{\prime}(x).</equation><equation>g ^ {\prime} (x) = \frac {\ln x - 1}{(\ln x) ^ {2}}.</equation>由于<equation>x=1</equation>是<equation>g(x)</equation>的无穷间断点，故<equation>x=1</equation>是<equation>y=g(x)</equation>的铅直渐近线.当<equation>0 < x < 1</equation>时，<equation>g^{\prime}(x)<0,g(x)</equation>单调减少；当<equation>1 < x < \mathrm{e}</equation>时，<equation>g^{\prime}(x)<0,g(x)</equation>单调减少；当<equation>x > \mathrm{e}</equation>时，<equation>g^{\prime}(x)>0,g(x)</equation>单调增加，且<equation>\lim _ {x \rightarrow + \infty} g (x) = \lim _ {x \rightarrow + \infty} \frac {x}{\ln x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow + \infty} \frac {1}{\frac {1}{x}} = + \infty .</equation><equation>x=\mathrm{e}</equation>是<equation>g(x)</equation>的极小值点，极小值为<equation>g(\mathrm{e})=\mathrm{e}.</equation>y = g(x）的图形如右图所示.

由图可知，曲线<equation>y=\frac{x}{\ln x}</equation>与直线<equation>y=\frac{b}{a}</equation>有2个交点当且仅当<equation>\frac{b}{a}>\mathrm{e}.</equation>因此，应选A.

---

**2019年第2题 | 选择题 | 4分 | 答案: D**

2. 已知方程<equation>x^{5}-5 x+k=0</equation>有3个不同的实根，则 k的取值范围是（    )

A.<equation>(-\infty,-4)</equation>B.<equation>(4,+\infty)</equation>C.<equation>\{-4,4\}</equation>D.<equation>(-4,4)</equation>

答案: D

**解析:**解构造辅助函数<equation>f ( x )=x^{5}-5 x+k</equation>，则<equation>f^{\prime}(x)=5 x^{4}-5=5 \left(x^{4}-1\right).</equation>当 x >1或 x<-1时，<equation>f^{\prime}(x)>0</equation>f(x)单调增加；当<equation>-1<x<1</equation>时，<equation>f^{\prime}(x)<0</equation>f(x)单调减少；当 x=<equation>\pm 1</equation>时，<equation>f^{\prime}(\pm1)=0.</equation>因此， x=-1是 f(x)的极大值点，极大值为 f(-1)， x=1是 f(x)的极小值点，极小值为 f(1).

(a)

(b)

如图（a）所示，要使得 f(x)有3个不同的零点，必须有<equation>f(1)=k-4<0, f(-1)=k+4>0.</equation>解得<equation>-4<k<4.</equation>因此，应选D.

---

**2017年第18题 | 解答题 | 10分**

18. (本题满分10分）已知方程<equation>\frac{1}{\ln(1+x)}-\frac{1}{x}=k</equation>在区间（0，1）内有实根，确定常数 k的取值范围.

**答案:**<equation>\left(\frac {1}{\ln 2} - 1, \frac {1}{2}\right).</equation>

**解析:**解设<equation>f ( x )=\frac{1}{\ln(1+x)}-\frac{1}{x}, x\in(0,1].</equation>考察 f(x)在（0，1]内的单调性.<equation>f ^ {\prime} (x) = \left[ \frac {1}{\ln (1 + x)} - \frac {1}{x} \right] ^ {\prime} = - \frac {1}{(1 + x) \ln^ {2} (1 + x)} + \frac {1}{x ^ {2}} = \frac {(1 + x) \ln^ {2} (1 + x) - x ^ {2}}{(1 + x) x ^ {2} \ln^ {2} (1 + x)}.</equation>由于当 x<equation>\in(0,1)</equation>时，<equation>(1+x)x^{2}\ln^{2}(1+x)>0</equation>，故我们考察 g(x）=（1+x）<equation>\ln^{2}(1+x)-x^{2},</equation><equation>x\in[0,1].</equation><equation>g ^ {\prime} (x) = \ln^ {2} (1 + x) + 2 \ln (1 + x) - 2 x,</equation><equation>g ^ {\prime \prime} (x) = \frac {2 \ln (1 + x)}{1 + x} + \frac {2}{1 + x} - 2 = \frac {2}{1 + x} [ \ln (1 + x) - x ].</equation>当 x<equation>\in(0,1)</equation>时，<equation>\ln(1+x)-x=-\frac{x^{2}}{2}+o(x^{2})<0</equation>.于是当 x<equation>\in(0,1)</equation>时，<equation>g^{\prime\prime}(x)<0</equation>.又因为<equation>g^{\prime}(0)=0</equation>，所以当 x<equation>\in(0,1)</equation>时，<equation>g^{\prime}(x)<0</equation>，g(x)在(0,1)内单调减少.由于<equation>g(0)=0</equation>，故<equation>g(x)<0</equation>，<equation>x\in(0,1)</equation>.因此，当 x<equation>\in(0,1)</equation>时，<equation>f^{\prime}(x)=\frac{g(x)}{(1+x)x^{2}\ln^{2}(1+x)}<0</equation>，f(x)在(0,1)内单调减少.<equation>f ( x )</equation>在（0,1）内的值域为（f（1），<equation>\lim_{x\to 0^{+}}f(x) ).</equation><equation>f (1) = \frac {1}{\ln 2} - 1.</equation>$<equation>\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} \left[\frac{1}{\ln(1+x)} - \frac{1}{x}\right] = \lim_{x \to 0^+} \frac{x - \ln(1+x)}{x\ln(1+x)} = \frac{1}{2}</equation>\left(\frac{1}{\ln2}-1,\frac{1}{2}\right). $

---

**2011年第18题 | 解答题 | 10分**

18. (本题满分10分）

证明方程<equation>4\arctan x-x+\frac{4\pi}{3}-\sqrt{3}=0</equation>恰有两个实根.

**答案:**## （18）证明略.

**解析:**证设 f(x）=4arctan x-x+<equation>\frac{4\pi}{3}-\sqrt{3}</equation>；则<equation>f ^ {\prime} (x) = \frac {4}{1 + x ^ {2}} - 1 = \frac {3 - x ^ {2}}{1 + x ^ {2}}.</equation>当<equation>x\in(-\sqrt{3},\sqrt{3})</equation>时，<equation>f^{\prime}(x) > 0</equation>；当<equation>x\in(-\infty , - \sqrt{3})</equation>或<equation>x\in(\sqrt{3}, + \infty)</equation>时，<equation>f^{\prime}(x) < 0</equation>；当<equation>x = \pm \sqrt{3}</equation>时，<equation>f^{\prime}(x) = 0.</equation>因此，<equation>f ( x )</equation>在<equation>(-\infty,-\sqrt{3})</equation>和<equation>(\sqrt{3},+\infty)</equation>上单调减少，在<equation>(-\sqrt{3},\sqrt{3})</equation>上单调增加，<equation>f(-\sqrt{3})</equation>为<equation>f ( x )</equation>的极小值，<equation>f(\sqrt{3})</equation>为<equation>f ( x )</equation>的极大值.

分别计算<equation>f(-\sqrt{3})</equation>和<equation>f(\sqrt{3})</equation>得，<equation>f (- \sqrt {3}) = 0, f (\sqrt {3}) = \frac {8}{3} \pi - 2 \sqrt {3} > 0.</equation>另一方面，当<equation>x\to+\infty</equation>时，<equation>\lim _ {x \rightarrow + \infty} f (x) = - \infty .</equation>由零点定理和单调性可知，<equation>f ( x )</equation>在<equation>(\sqrt{3}, +\infty)</equation>上有唯一零点，加上<equation>x=-\sqrt{3}, f ( x )</equation>在<equation>(-\infty, +\infty)</equation>上共有两个零点.

f（x）的性质可列表如下.

<table border="1"><tr><td></td><td>(-∞,-√3)</td><td>-√3</td><td>(-√3,√3)</td><td>√3</td><td>(√3,+∞)</td></tr><tr><td>f(x)</td><td>单调减少,无零点，limx→-∞f(x)=+∞</td><td>f(-3)=0</td><td>单调增加，无零点</td><td>f(√3)>0</td><td>单调减少，有唯一零点，limx→+∞f(x)=-∞</td></tr></table>

因此，方程<equation>f ( x ) = 0</equation>恰有两个实根.

---


#### 导数的几何意义


**2020年第10题 | 填空题 | 4分**

10. 曲线<equation>x+y+\mathrm{e}^{2 x y}=0</equation>在点 (0,-1) 处的切线方程为 ___

**解析:**对已知方程两端关于 x求导，可得<equation>1+y^{\prime}+\mathrm{e}^{2 x y}(2 y+2 x y^{\prime})=0.</equation>整理可得<equation>(1+2 x \mathrm{e}^{2 x y}) y^{\prime}=-2 y \mathrm{e}^{2 x y}-1.</equation>代入<equation>x=0,y=-1</equation>，可得<equation>y^{\prime}(0)=2-1=1.</equation>又因为切线过点（0，-1），所以该切线的点斜式方程为<equation>y+1=x-0</equation>即<equation>y=x-1.</equation>

---

**2013年第9题 | 填空题 | 4分**

9. 设曲线<equation>y=f(x)</equation>与<equation>y=x^{2}-x</equation>在点(1,0)处有公共切线，则<equation>\lim_{n\rightarrow \infty} n f\left(\frac{n}{n+2}\right)=</equation>___

**解析:**由已知条件知<equation>f ( 1 )=0</equation>且<equation>f^{\prime}(1)=\frac{\mathrm{d}\left(x^{2}-x\right)}{\mathrm{d}x}\bigg|_{x=1}=1.</equation>因此，<equation>\begin{array}{l} \lim _ {n \rightarrow \infty} n f \left(\frac {n}{n + 2}\right) = \lim _ {n \rightarrow \infty} \frac {f \left(\frac {n}{n + 2}\right) - f (1)}{\frac {1}{n}} = \lim _ {n \rightarrow \infty} \frac {f \left(\frac {n}{n + 2}\right) - f (1)}{\frac {n}{n + 2} - 1} \cdot \frac {\frac {n}{n + 2} - 1}{\frac {1}{n}} \\ \underline {{\mathrm {导 数 定 义}}} f ^ {\prime} (1) \cdot \lim _ {n \rightarrow \infty} \frac {- 2 n}{n + 2} = - 2. \\ \end{array}</equation>

---

**2011年第11题 | 填空题 | 4分**

11. 曲线<equation>\tan \left(x+y+\frac{\pi}{4}\right)=\mathrm{e}^{y}</equation>在点 (0,0) 处的切线方程为 ___

**答案:**## y = - 2x.

**解析:**解（法一）将<equation>y</equation>看作<equation>x</equation>的函数，对<equation>\tan \left(x + y + \frac{\pi}{4}\right) = \mathrm{e}^{y}</equation>两端关于<equation>x</equation>求导得，<equation>\sec^ {2} \left(x + y + \frac {\pi}{4}\right) \cdot \left(1 + \frac {\mathrm {d} y}{\mathrm {d} x}\right) = \mathrm {e} ^ {y} \cdot \frac {\mathrm {d} y}{\mathrm {d} x}.</equation>将<equation>x = 0,y = 0</equation>代入上式得<equation>2\left(1 + \frac{\mathrm{d}y}{\mathrm{d}x}\bigg|_{x = 0}\right) = \frac{\mathrm{d}y}{\mathrm{d}x}\bigg|_{x = 0}.</equation>解得<equation>\frac{\mathrm{d}y}{\mathrm{d}x}\bigg|_{x = 0} = -2.</equation>因此，曲线在点（0,0）处的切线方程为<equation>y=-2x.</equation>（法二）对<equation>\tan \left(x + y + \frac{\pi}{4}\right) = \mathrm{e}^{y}</equation>两端微分得，<equation>\sec^ {2} \left(x + y + \frac {\pi}{4}\right) \cdot \left(\mathrm {d} x + \mathrm {d} y\right) = \mathrm {e} ^ {y} \mathrm {d} y.</equation>将<equation>x=0,y=0</equation>代入上式化简得<equation>2\mathrm{d}x=-\mathrm{d}y</equation>即<equation>\left.\frac{\mathrm{d}y}{\mathrm{d}x}\right|_{x=0}=-2.</equation>其余同法一.

---


#### 不等式


**2012年第18题 | 解答题 | 10分**

18. (本题满分10分)

证明<equation>x\ln \frac{1+x}{1-x}+\cos x\geqslant 1+\frac{x^{2}}{2}(-1<x<1).</equation>

**答案:**## （18）证明略.

**解析:**证（法一）考虑辅助函数<equation>f ( x )=x \ln \frac{1+x}{1-x}+\cos x-1-\frac{x^{2}}{2}.</equation>由于<equation>f (- x) = (- x) \ln \frac {1 - x}{1 + x} + \cos x - 1 - \frac {x ^ {2}}{2} = f (x),</equation>故 f(x)为偶函数.如果能证明当 x<equation>\in[0,1)</equation>时，<equation>f(x)\geqslant0</equation>，那么当 x<equation>\in(-1,1)</equation>时，也有 f(x)<equation>\geqslant0</equation>，从而题给不等式成立.

计算<equation>f^{\prime}(x)</equation><equation>f ^ {\prime} (x) = \left(x \ln \frac {1 + x}{1 - x} + \cos x - 1 - \frac {x ^ {2}}{2}\right) ^ {\prime} = \frac {2 x}{1 - x ^ {2}} + \ln \frac {1 + x}{1 - x} - \sin x - x.</equation>由于当<equation>x\in [0,1)</equation>时，<equation>\frac{x}{1 - x^2}\geqslant x\geqslant \sin x</equation>，故<equation>\frac {2 x}{1 - x ^ {2}} \geqslant 2 x \geqslant \sin x + x,</equation>等号在 x=0时取得.又因为<equation>\frac{1+x}{1-x}\geqslant 1</equation>，所以<equation>\ln \frac{1+x}{1-x}\geqslant 0</equation>，等号在 x=0时取得.

因此，当<equation>x\in(0,1)</equation>时，<equation>f ^ {\prime} (x) = \frac {2 x}{1 - x ^ {2}} + \ln \frac {1 + x}{1 - x} - \sin x - x > 0.</equation>综上所述，<equation>f ( x )</equation>在[0,1]上单调增加，<equation>f ( 0 )</equation>为<equation>f ( x )</equation>在[0,1]上的最小值.又由<equation>f ( x )</equation>为偶函数可知，在（-1，1）上，<equation>f ( x ) \geqslant f ( 0 ) = 0</equation>即<equation>x \ln \frac{1+x}{1-x}+\cos x\geqslant 1+\frac{x^{2}}{2}(-1<x<1).</equation>（法二）在法一中求得<equation>f^{\prime}(x)=\frac{2x}{1-x^{2}}+\ln \frac{1+x}{1-x}-\sin x-x</equation>后，继续求<equation>f^{\prime\prime}(x)</equation>以判断<equation>f^{\prime}(x)</equation>的性质.<equation>f ^ {\prime \prime} (x) = \frac {2 \left(1 + x ^ {2}\right)}{\left(1 - x ^ {2}\right) ^ {2}} + \frac {1}{1 + x} - \frac {- 1}{1 - x} - \cos x - 1 = \frac {4}{\left(1 - x ^ {2}\right) ^ {2}} - \cos x - 1.</equation>由于当<equation>x\in [0,1)</equation>时，<equation>\frac {4}{\left(1 - x ^ {2}\right) ^ {2}} \geqslant 4, \quad 1 + \cos x \leqslant 2,</equation>故<equation>f^{\prime \prime}(x) > 0. f^{\prime}(x)</equation>在[0,1）上单调增加，<equation>f^{\prime}(x)\geqslant f^{\prime}(0)=0,f(x)</equation>在[0,1）上单调增加.

（法三）首先，<equation>f(x)=x\ln \frac{1+x}{1-x}+\cos x</equation>为偶函数，<equation>g(x)=1+\frac{x^{2}}{2}</equation>也为偶函数，且<equation>f(0)=g(0)=1</equation>故我们只需证明，在（0，1）上，<equation>f(x)\geqslant g(x)</equation>，便能得到在（-1，1）上，<equation>f(x)\geqslant g(x).</equation>由泰勒中值定理，<equation>\cos x=1-\frac{x^{2}}{2!}+\frac{\cos \xi}{4!} x^{4},\xi</equation>为介于0和x之间的某个值.于是，当<equation>x\in(0,1)</equation>时，<equation>\cos x\geqslant 1-\frac{x^{2}}{2}.</equation>从而<equation>f (x) = x \ln \frac {1 + x}{1 - x} + \cos x \geqslant x \ln \frac {1 + x}{1 - x} + 1 - \frac {x ^ {2}}{2}.</equation>若能证明<equation>x\ln \frac{1+x}{1-x}+1-\frac{x^{2}}{2}\geqslant 1+\frac{x^{2}}{2}</equation>，则由不等号的传递性可知原不等式得证.

由于当<equation>x\in (0,1)</equation>时，<equation>x \ln \frac {1 + x}{1 - x} + 1 - \frac {x ^ {2}}{2} \geqslant 1 + \frac {x ^ {2}}{2} \Leftrightarrow x \ln \frac {1 + x}{1 - x} \geqslant x ^ {2} \Leftrightarrow \ln \frac {1 + x}{1 - x} \geqslant x,</equation>故我们只需要证明<equation>\ln \frac{1+x}{1-x}\geqslant x.</equation>考虑<equation>\varphi(x)=\ln \frac{1+x}{1-x}-x.</equation><equation>\varphi^ {\prime} (x) = \frac {1}{1 + x} - \frac {- 1}{1 - x} - 1 = \frac {2}{1 - x ^ {2}} - 1.</equation>当<equation>x \in(0,1)</equation>时，<equation>\frac{2}{1-x^{2}}\geqslant 2</equation>从而<equation>\varphi^{\prime}(x)=\frac{2}{1-x^{2}}-1>0, \varphi(x)</equation>在（0,1）上单调增加，<equation>\varphi(x)\geqslant \varphi(0)=0.</equation>综上所述，原不等式成立.

---

**2010年第4题 | 选择题 | 4分 | 答案: C**

4. 设<equation>f(x)=\ln^{1 0} x,g(x)=x,h(x)=\mathrm{e}^{\frac{x}{1 0}}</equation>，则当 x充分大时有（    )

A. g(x) < h(x) < f(x) B. h(x) < g(x) < f(x) C. f(x) < g(x) < h(x) D. g(x) < f(x) < h(x)

答案: C

**解析:**（法一）由于<equation>\lim _ {x \rightarrow + \infty} \frac {h (x)}{g (x)} = \lim _ {x \rightarrow + \infty} \frac {\mathrm {e} ^ {\frac {x}{1 0}}}{x} \xlongequal {\text {洛 必达}} \lim _ {x \rightarrow + \infty} \frac {\frac {1}{1 0} \mathrm {e} ^ {\frac {x}{1 0}}}{1} = + \infty ,</equation>故当 x充分大时，<equation>h ( x ) > g ( x ).</equation>又由于<equation>\lim _ {x \rightarrow + \infty} \frac {g (x)}{f (x)} = \lim _ {x \rightarrow + \infty} \frac {x}{\ln^ {1 0} x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow + \infty} \frac {x}{1 0 \ln^ {9} x} \xlongequal {\text {洛必达}} \dots \xlongequal {\text {洛必达}} \lim _ {x \rightarrow + \infty} \frac {x}{1 0 !} = + \infty ,</equation>故当<equation>x</equation>充分大时，<equation>g(x) > f(x)</equation>综上所述，当<equation>x</equation>充分大时，<equation>h(x) > g(x) > f(x)</equation>.应选C.

（法二）令<equation>H ( x )=h ( x )-g ( x )=\mathrm{e}^{\frac{x}{1 0}}-x</equation>，则<equation>H^{\prime}(x)=\frac{1}{1 0}\mathrm{e}^{\frac{x}{1 0}}-1.</equation>由于当<equation>x\geqslant 1 0 0</equation>时，<equation>\frac{1}{1 0}\mathrm{e}^{\frac{x}{1 0}}-1\geqslant</equation><equation>\frac{1}{1 0}\mathrm{e}^{1 0}-1>0</equation>，故H(x）在<equation>[ 1 0 0,+\infty)</equation>上为单调增加函数，从而当<equation>x\geqslant 1 0 0</equation>时，<equation>h (x) - g (x) \geqslant h (1 0 0) - g (1 0 0) = \mathrm {e} ^ {1 0} - 1 0 0 \geqslant 2 ^ {1 0} - 1 0 0 > 0.</equation>令<equation>F(x) = x^{\frac{1}{10}} - \ln x</equation>，则<equation>F^{\prime}(x) = \frac{1}{10} x^{-\frac{9}{10}} - \frac{1}{x} = \frac{1}{10x}\left(x^{\frac{1}{10}} - 10\right)</equation>.由于当<equation>x > 10^{10}</equation>时，<equation>F^{\prime}(x) > 0</equation>，故<equation>F(x)</equation>在<equation>[10^{10}, + \infty)</equation>上为单调增加函数，从而当<equation>x > 10^{100}</equation>时，<equation>F(x) \geqslant F(10^{100}) = 10^{10} - 100\ln 10 > 0</equation>即<equation>x^{\frac{1}{10}} > \ln x.</equation>因此，<equation>x > \ln^{10}x.</equation>综上所述，当 x充分大时，<equation>h ( x ) > g ( x ) > f ( x )</equation>.应选C.

---


### 无穷级数

#### 数项级数


**2025年第3题 | 选择题 | 5分 | 答案: B**

3. 已知 k为常数，则级数<equation>\sum_{n=1}^{\infty}(-1)^{n}\left[\frac{1}{n}-\ln \left(1+\frac{k}{n^{2}}\right)\right]</equation>(    )

A. 绝对收敛 B. 条件收敛

C. 发散 D. 敛散性与 k的取

答案: B

**解析:**解 由于数列<equation>\left\{\frac{1}{n}\right\}</equation>单调减少趋于0，故由交错级数的莱布尼茨定理可知<equation>\sum_{n=1}^{\infty}(-1)^{n}\frac{1}{n}</equation>收敛.但<equation>\sum_{n=1}^{\infty}\frac{1}{n}</equation>发散，于是级数<equation>\sum_{n=1}^{\infty}(-1)^{n}\frac{1}{n}</equation>条件收敛.

由于<equation>\left|\ln \left(1+\frac{k}{n^{2}}\right)\right|= \left|\frac{k}{n^{2}}+o\left(\frac{k}{n^{2}}\right)\right|</equation>，故当 n→<equation>\infty</equation>时，<equation>\left|\ln \left(1+\frac{k}{n^{2}}\right)\right| \sim \left|\frac{k}{n^{2}}\right|</equation>，而<equation>\lim_{n\to \infty}n^{2}\left|\frac{k}{n^{2}}\right|=|k|</equation>，从而由正项级数的极限审敛法可知<equation>\sum_{n=1}^{\infty}\left|\frac{k}{n^{2}}\right|</equation>收敛，进一步可得<equation>\sum_{n=1}^{\infty}\left|\ln \left(1+\frac{k}{n^{2}}\right)\right|</equation>收敛.于是级数<equation>\sum_{n=1}^{\infty}(-1)^{n}\ln \left(1+\frac{k}{n^{2}}\right)</equation>绝对收敛.

由级数<equation>\sum_{n=1}^{\infty}(-1)^{n}\frac{1}{n}</equation>条件收敛，级数<equation>\sum_{n=1}^{\infty}(-1)^{n}\ln \left(1+\frac{k}{n^{2}}\right)</equation>绝对收敛以及分析中的结论可得级数<equation>\sum_{n=1}^{\infty}(-1)^{n}\left[\frac{1}{n}-\ln \left(1+\frac{k}{n^{2}}\right)\right]</equation>条件收敛.

因此，应选B.

---

**2023年第4题 | 选择题 | 5分 | 答案: A**

4. 已知<equation>a_{n} < b_{n} ( n=1,2,\cdots)</equation>，若级数<equation>\sum_{n=1}^{\infty} a_{n}</equation>与<equation>\sum_{n=1}^{\infty} b_{n}</equation>均收敛，则“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的（    ）

A. 充分必要条件 B. 充分不必要条件

C. 必要不充分条件 D. 既不充分也不必要条件

答案: A

**解析:**解（法一）由<equation>a_{n} < b_{n}</equation>可知，<equation>\sum_{n=1}^{\infty} \left(b_{n}-a_{n}\right)</equation>为正项级数. 进一步，由<equation>\sum_{n=1}^{\infty} a_{n}</equation>与<equation>\sum_{n=1}^{\infty} b_{n}</equation>均收敛以及收敛级数的性质可知，<equation>\sum_ {n = 1} ^ {\infty} \left(b _ {n} - a _ {n}\right) = \sum_ {n = 1} ^ {\infty} b _ {n} - \sum_ {n = 1} ^ {\infty} a _ {n}.</equation>于是，<equation>\sum_{n=1}^{\infty} \left(b_{n}-a_{n}\right)</equation>为收敛的正项级数，从而<equation>\sum_{n=1}^{\infty} \left(b_{n}-a_{n}\right)</equation>绝对收敛.

由三角不等式可得<equation>\left| b _ {n} \right| = \left| b _ {n} - a _ {n} + a _ {n} \right| \leqslant \left| b _ {n} - a _ {n} \right| + \left| a _ {n} \right|,</equation><equation>\left| a _ {n} \right| = \left| a _ {n} - b _ {n} + b _ {n} \right| \leqslant \left| b _ {n} - a _ {n} \right| + \left| b _ {n} \right|.</equation>若<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛，即<equation>\sum_{n=1}^{\infty} \mid a_{n} \mid</equation>收敛，则由（1）式以及正项级数的比较审敛法可知<equation>\sum_{n=1}^{\infty} \mid b_{n} \mid</equation>收敛，从而<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛.“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的充分条件.

若<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛，即<equation>\sum_{n=1}^{\infty} \mid b_{n} \mid</equation>收敛，则由（2）式以及正项级数的比较审敛法可知<equation>\sum_{n=1}^{\infty} \mid a_{n} \mid</equation>收敛，从而<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛.“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的必要条件.

综上所述，“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的充分必要条件，应选A.

（法二）先考虑充分性.

设<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛，即<equation>\sum_{n=1}^{\infty} \mid a_{n}\mid</equation>收敛.

考虑正项级数<equation>\sum_{n=1}^{\infty} \frac{\mid b_{n}\mid -b_{n}}{2}.</equation>对<equation>\left\{b_{n}\right\}</equation>中小于0的项，<equation>a_{n} < b_{n} < 0</equation>，于是<equation>\left| a _ {n} \right| = - a _ {n} > - b _ {n} = \frac {\left| b _ {n} \right| - b _ {n}}{2} > 0.</equation>对<equation>\left\{b_{n}\right\}</equation>中大于等于0的项，<equation>\left| a _ {n} \right| \geqslant 0 = \frac {\left| b _ {n} \right| - b _ {n}}{2}.</equation>从而，对所有正整数 n，都有<equation>|a_{n}| \geqslant \frac{|b_{n}| - b_{n}}{2} \geqslant 0.</equation>由正项级数的比较审敛法可知，级数<equation>\sum_{n=1}^{\infty} \frac{\mid b_{n}\mid -b_{n}}{2}</equation>收敛. 进一步，<equation>\sum_ {n = 1} ^ {\infty} \left| b _ {n} \right| = \sum_ {n = 1} ^ {\infty} \left[ 2 \left(\frac {\left| b _ {n} \right| - b _ {n}}{2}\right) + b _ {n} \right] = 2 \sum_ {n = 1} ^ {\infty} \frac {\left| b _ {n} \right| - b _ {n}}{2} + \sum_ {n = 1} ^ {\infty} b _ {n}.</equation>由<equation>\sum_{n=1}^{\infty}b_{n}</equation>收敛以及收敛级数的性质可知，<equation>\sum_{n=1}^{\infty}|\boldsymbol{b}_{n}|</equation>收敛，从而<equation>\sum_{n=1}^{\infty}b_{n}</equation>绝对收敛.

因此，“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的充分条件.

再考虑必要性.

由<equation>a_{n} < b_{n}</equation>可得<equation>- b_{n} < - a_{n}.</equation>由<equation>\sum_{n=1}^{\infty} a_{n}</equation>与<equation>\sum_{n=1}^{\infty} b_{n}</equation>均收敛可知<equation>\sum_{n=1}^{\infty}(-a_{n})</equation>与<equation>\sum_{n=1}^{\infty}(-b_{n})</equation>均收敛.于是，同充分性的证明可知<equation>\sum_{n=1}^{\infty}(-b_{n})</equation>绝对收敛蕴含<equation>\sum_{n=1}^{\infty}(-a_{n})</equation>绝对收敛，即<equation>\sum_{n=1}^{\infty}b_{n}</equation>绝对收敛蕴含<equation>\sum_{n=1}^{\infty}a_{n}</equation>绝对收敛.

因此，“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的必要条件.

综上所述，“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的充分必要条件，应选A.

---

**2019年第4题 | 选择题 | 4分 | 答案: B**

4. 若<equation>\sum_{n=1}^{\infty} n u_{n}</equation>绝对收敛，<equation>\sum_{n=1}^{\infty} \frac{v_{n}}{n}</equation>条件收敛，则（    ）

A.<equation>\sum_{n=1}^{\infty} u_{n} v_{n}</equation>条件收敛 B.<equation>\sum_{n=1}^{\infty} u_{n} v_{n}</equation>绝对收敛 C.<equation>\sum_{n=1}^{\infty} \left(u_{n}+v_{n}\right)</equation>收敛 D.<equation>\sum_{n=1}^{\infty} \left(u_{n}+v_{n}\right)</equation>发散

答案: B

**解析:**解（法一）由<equation>\sum_{n=1}^{\infty}\frac{v_{n}}{n}</equation>条件收敛以及级数收敛的必要条件可得，<equation>\lim_{n\to \infty}\frac{v_{n}}{n}=0.</equation>由极限的有界性可知，存在 M > 0和正整数N，使得当 n > N时，<equation>\left|\frac{v_{n}}{n}\right|\leqslant M.</equation>于是，<equation>\left| u _ {n} v _ {n} \right| = \left| n u _ {n} \cdot \frac {v _ {n}}{n} \right| \leqslant M \left| n u _ {n} \right|.</equation>由于<equation>\sum_{n=1}^{\infty} n u_{n}</equation>绝对收敛，故其收敛，从而由比较审敛法可知，<equation>\sum_{n=1}^{\infty} \mid u_{n} v_{n} \mid</equation>收敛因此，<equation>\sum_{n=1}^{\infty} u_{n} v_{n}</equation>绝对收敛.应选B.

（法二）排除法.

选项A、C：取<equation>u_{n}=\frac{1}{n^{3}}, v_{n}=(-1)^{n}</equation>，则<equation>\sum_{n=1}^{\infty}u_{n}v_{n}=\sum_{n=1}^{\infty}\frac{(-1)^{n}}{n^{3}},\sum_{n=1}^{\infty}\left(u_{n}+v_{n}\right)=\sum_{n=1}^{\infty}\left[\frac{1}{n^{3}}+(-1)^{n}\right]</equation><equation>\sum_{n=1}^{\infty}\frac{(-1)^{n}}{n^{3}}</equation>绝对收敛，<equation>\sum_{n=1}^{\infty}\left[\frac{1}{n^{3}}+(-1)^{n}\right]</equation>发散. 选项A、C不正确.

选项D：取<equation>u_{n}=\frac{1}{n^{3}},</equation><equation>v_{n}=\frac{(-1)^{n+1}}{\ln(n+1)},</equation>则<equation>\sum_{n=1}^{\infty}\frac{1}{n^{3}}</equation>收敛，且由莱布尼茨定理可知<equation>\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{\ln(n+1)}</equation>收敛.由收敛级数的性质可知<equation>\sum_{n=1}^{\infty}\left[\frac{1}{n^{3}}+\frac{(-1)^{n+1}}{\ln(n+1)}\right]</equation>收敛.选项D不正确由排除法可知，应选B.

---

**2017年第4题 | 选择题 | 4分 | 答案: C**

4. 若级数<equation>\sum_{n=2}^{\infty}\left[\sin \frac{1}{n}-k\ln \left(1-\frac{1}{n}\right)\right]</equation>收敛，则 k=（    ）

A.1 B.2 C.-1 D.-2

答案: C

**解析:**解 考虑<equation>\sin \frac{1}{n}</equation>和<equation>\ln \left( 1-\frac{1}{n} \right)</equation>的泰勒公式.<equation>\sin \frac {1}{n} = \frac {1}{n} - \frac {1}{6 n ^ {3}} + o \left(\frac {1}{n ^ {3}}\right), \quad \ln \left(1 - \frac {1}{n}\right) = - \frac {1}{n} - \frac {1}{2 n ^ {2}} + o \left(\frac {1}{n ^ {2}}\right).</equation>于是，<equation>\sin \frac {1}{n} - k \ln \left(1 - \frac {1}{n}\right) = \frac {1}{n} + \frac {k}{n} + \frac {k}{2 n ^ {2}} + o \left(\frac {1}{n ^ {2}}\right).</equation>当 n充分大时，<equation>\sin \frac{1}{n}-k\ln \left(1-\frac{1}{n}\right)=\frac{1}{n}+\frac{k}{n}+\frac{k}{2n^{2}}+o\left(\frac{1}{n^{2}}\right)</equation>不变号.又因为舍去级数的有限项不影响级数的敛散性，所以可以对级数<equation>\sum_{n=2}^{\infty}\left[\sin \frac{1}{n}-k\ln \left(1-\frac{1}{n}\right)\right]</equation>使用极限形式的比较审敛法.当 k≠-1时，<equation>\lim _ {n \rightarrow \infty} \frac {\sin \frac {1}{n} - k \ln \left(1 - \frac {1}{n}\right)}{\frac {1}{n}} = \lim _ {n \rightarrow \infty} \frac {\frac {1}{n} + \frac {k}{n} + \frac {k}{2 n ^ {2}} + o \left(\frac {1}{n ^ {2}}\right)}{\frac {1}{n}} = 1 + k,</equation>而<equation>\sum_{n=1}^{\infty}\frac{1}{n}</equation>发散，故由极限形式的比较审敛法知，原级数发散.

当 k=-1时，<equation>\sum_{n=2}^{\infty}-\left[\sin \frac{1}{n}-k\ln \left(1-\frac{1}{n}\right)\right]</equation>为正项级数，且<equation>\lim _ {n \rightarrow \infty} \frac {- \left[ \sin \frac {1}{n} + \ln \left(1 - \frac {1}{n}\right)\right]}{\frac {1}{n ^ {2}}} = \lim _ {n \rightarrow \infty} \frac {\frac {1}{2 n ^ {2}} + o \left(\frac {1}{n ^ {2}}\right)}{\frac {1}{n ^ {2}}} = \frac {1}{2},</equation>而<equation>\sum_{n=1}^{\infty}\frac{1}{n^{2}}</equation>收敛，故由极限形式的比较审敛法知，原级数收敛.

级数<equation>\sum_{n=2}^{\infty}\left[\sin \frac{1}{n}-k\ln \left(1-\frac{1}{n}\right)\right]</equation>收敛等价于 k=-1.

因此，应选C.

---

**2016年第4题 | 选择题 | 4分 | 答案: A**

4. 级数<equation>\sum_{n=1}^{\infty}\left(\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}}\right)\sin(n+k)(k</equation>为常数)（    ）

A. 绝对收敛 B. 条件收敛 C. 发散 D. 收敛性与 k有关

答案: A

**解析:**解 （法一）首先，这并不是一个正项级数，但当 n<equation>\to\infty</equation>时，它的一般项<equation>\begin{array}{l} \left(\frac {1}{\sqrt {n}} - \frac {1}{\sqrt {n + 1}}\right) \sin (n + k) = \frac {\sqrt {n + 1} - \sqrt {n}}{\sqrt {n} \sqrt {n + 1}} \sin (n + k) \\ \xlongequal {\text {分子 有 理 化}} \frac {\sin (n + k)}{\sqrt {n} \sqrt {n + 1} (\sqrt {n + 1} + \sqrt {n})} \rightarrow 0, \\ \end{array}</equation>并且<equation>\left| \left(\frac {1}{\sqrt {n}} - \frac {1}{\sqrt {n + 1}}\right) \sin (n + k) \right| \leqslant \frac {1}{\sqrt {n} \sqrt {n + 1} \left(\sqrt {n + 1} + \sqrt {n}\right)} \leqslant \frac {1}{n \cdot 2 \sqrt {n}} < \frac {1}{n ^ {\frac {3}{2}}},</equation>而<equation>\sum_{n=1}^{\infty}\frac{1}{n^{\frac{3}{2}}}</equation>收敛，故由比较审敛法可知，<equation>\sum_{n=1}^{\infty}\left| \left( \frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}} \right)\sin(n+k) \right|</equation>收敛，从而原级数绝对收敛应选A.

（法二）注意到<equation>\left| \left(\frac {1}{\sqrt {n}} - \frac {1}{\sqrt {n + 1}}\right) \sin (n + k) \right| \leqslant \frac {1}{\sqrt {n}} - \frac {1}{\sqrt {n + 1}}.</equation>由于<equation>\sum_ {n = 1} ^ {m} \left(\frac {1}{\sqrt {n}} - \frac {1}{\sqrt {n + 1}}\right) = \left(1 - \frac {1}{\sqrt {2}}\right) + \left(\frac {1}{\sqrt {2}} - \frac {1}{\sqrt {3}}\right) + \dots + \left(\frac {1}{\sqrt {m}} - \frac {1}{\sqrt {m + 1}}\right) = 1 - \frac {1}{\sqrt {m + 1}},</equation>故<equation>\sum_{n=1}^{\infty}\left(\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}}\right)=\lim_{m\to \infty}\left(1-\frac{1}{\sqrt{m+1}}\right)=1</equation>，即级数<equation>\sum_{n=1}^{\infty}\left(\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}}\right)</equation>收敛.

由比较审敛法知，级数<equation>\sum_{n=1}^{\infty}\left| \left(\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}}\right)\sin(n+k)\right|</equation>收敛，即级数<equation>\sum_{n=1}^{\infty}\left(\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}}\right)\sin(n+k)</equation>绝对收敛.应选A.

---

**2015年第4题 | 选择题 | 4分 | 答案: C**

4. 下列级数中发散的是（    ）<equation>\sum_ {n = 1} ^ {\infty} \frac {n}{3 ^ {n}}</equation><equation>\sum_ {n = 1} ^ {\infty} \frac {1}{\sqrt {n}} \ln \left(1 + \frac {1}{n}\right)</equation>C.<equation>\sum_{n=2}^{\infty} \frac{(-1)^{n}+1}{\ln n}</equation>D.<equation>\sum_{n=1}^{\infty} \frac{n!}{n^{n}}</equation>

答案: C

**解析:**解 由于当 n为奇数时，<equation>(-1)^{n}+1=0;</equation>n为偶数时，<equation>(-1)^{n}+1=2</equation>，故<equation>\sum_ {n = 2} ^ {2 N} \frac {(- 1) ^ {n} + 1}{\ln n} = \sum_ {k = 1} ^ {N} \frac {2}{\ln 2 k} = \sum_ {k = 1} ^ {N} \frac {2}{\ln 2 + \ln k} \geqslant \frac {2}{\ln 2} + \sum_ {k = 2} ^ {N} \frac {2}{2 \ln k} > \sum_ {k = 2} ^ {N} \frac {1}{\ln k} > \sum_ {k = 2} ^ {N} \frac {1}{k}.</equation>而<equation>\sum_{k=2}^{\infty} \frac{1}{k}</equation>发散.由比较审敛法可知，<equation>\sum_{n=2}^{\infty} \frac{(-1)^{n}+1}{\ln n}</equation>发散.应选C.

也可以这样说明<equation>\sum_{n=2}^{\infty} \frac{(-1)^{n}+1}{\ln n}</equation>发散.

由莱布尼茨定理可知<equation>\sum_{n = 2}^{\infty}\frac{(-1)^n}{\ln n}</equation>收敛，由比较审敛法可知<equation>\sum_{n = 2}^{\infty}\frac{1}{\ln n}</equation>发散.因此，<equation>\sum_{n = 2}^{\infty}\frac{(-1)^n + 1}{\ln n}</equation>发散.

下面我们说明选项 A、B、D不正确.

由于<equation>\lim _ {n \rightarrow \infty} \frac {n + 1}{3 ^ {n + 1}} \cdot \frac {3 ^ {n}}{n} = \lim _ {n \rightarrow \infty} \frac {n + 1}{n} \cdot \frac {1}{3} = \frac {1}{3} < 1,</equation><equation>\lim _ {n \rightarrow \infty} \frac {(n + 1) !}{(n + 1) ^ {n + 1}} \cdot \frac {n ^ {n}}{n !} = \lim _ {n \rightarrow \infty} \left(\frac {n}{n + 1}\right) ^ {n} = \lim _ {n \rightarrow \infty} \frac {1}{\left(1 + \frac {1}{n}\right) ^ {n}} = \frac {1}{\mathrm {e}} < 1,</equation>故由比值审敛法可知，选项A与选项D中的级数均收敛.

由于<equation>\lim _ {n \rightarrow \infty} \frac {\frac {1}{\sqrt {n}} \ln \left(1 + \frac {1}{n}\right)}{n ^ {- \frac {3}{2}}} \xlongequal {\ln \left(1 + \frac {1}{n}\right) \sim \frac {1}{n}} \lim _ {n \rightarrow \infty} \frac {\frac {1}{\sqrt {n}} \cdot \frac {1}{n}}{n ^ {- \frac {3}{2}}} = 1,</equation>而<equation>\sum_{n=1}^{\infty}\frac{1}{n^{\frac{3}{2}}}</equation>收敛，故由比较审敛法的极限形式可知，选项B中的级数收敛.

---

**2013年第4题 | 选择题 | 4分 | 答案: D**

4. 设<equation>\{a_{n}\}</equation>为正项数列，下列选项正确的是（    )

A. 若<equation>a_{n}>a_{n+1}</equation>，则<equation>\sum_{n=1}^{\infty}(-1)^{n-1}a_{n}</equation>收敛

B. 若<equation>\sum_{n=1}^{\infty}(-1)^{n-1}a_{n}</equation>收敛，则<equation>a_{n}>a_{n+1}</equation>C. 若<equation>\sum_{n=1}^{\infty}a_{n}</equation>收敛，则存在常数 p>1，使<equation>\lim_{n\rightarrow \infty}n^{p}a_{n}</equation>存在

D. 若存在常数 p>1，使<equation>\lim_{n\rightarrow \infty}n^{p}a_{n}</equation>存在，则<equation>\sum_{n=1}^{\infty}a_{n}</equation>收敛

答案: D

**解析:**解 观察四个选项，发现选项D即极限审敛法的内容，故选项D正确.应选D.

下面我们分别说明选项 A、B、C 不正确.

选项A：虽然<equation>\sum_{n=1}^{\infty}(-1)^{n-1}a_{n}</equation>是交错级数，但是与莱布尼茨定理的条件相比较，该级数不满足<equation>\lim_{n\to \infty}a_{n}=0</equation>的条件.因此不能使用莱布尼茨定理说明它收敛.事实上，取<equation>a_{n}=\frac{1}{n}+1</equation><equation>a_{n}>a_{n+1}</equation>，但由于<equation>\lim_{n\to \infty}(-1)^{n-1}\left(\frac{1}{n}+1\right)</equation>不存在，<equation>\sum_{n=1}^{\infty}(-1)^{n-1}a_{n}</equation>不收敛.

选项B：由于级数舍去有限项不影响其敛散性，故我们可以令<equation>a_{n}=\left\{ \begin{array}{ll}1, & n=1,2,3,\\ \frac{1}{n}, & n=4,5,\dots. \end{array} \right.</equation>级数<equation>\sum_{n=1}^{\infty}(-1)^{n-1}a_{n}</equation>收敛，但<equation>a_{1}=a_{2}=a_{3}</equation>，不满足<equation>a_{n}>a_{n+1}</equation>.

选项C：令<equation>a_{n}=\frac{1}{(n+1)\ln^{2}(n+1)}</equation>，对任意的 p > 1，都有<equation>\lim_{n\to \infty}n^{p}\frac{1}{(n+1)\ln^{2}(n+1)}=\infty.</equation>令<equation>f(x)=\frac{1}{(x+1)\ln^{2}(x+1)}.</equation><equation>\int_{1}^{+\infty}f(x)\mathrm{d}x=\int_{1}^{+\infty}\frac{1}{\ln^{2}(x+1)}\mathrm{d}\left[\ln(x+1)\right]=-\frac{1}{\ln(x+1)}\bigg|_{1}^{+\infty}=\frac{1}{\ln 2}.</equation>由积分判别法可知级数<equation>\sum_{n=1}^{\infty}a_{n}</equation>收敛.

---

**2012年第4题 | 选择题 | 4分 | 答案: D**

4. 已知级数<equation>\sum_{n=1}^{\infty}(-1)^{n}\sqrt{n}\sin \frac{1}{n^{\alpha}}</equation>绝对收敛，级数<equation>\sum_{n=1}^{\infty}\frac{(-1)^{n}}{n^{2-\alpha}}</equation>条件收敛，则（    )

A.<equation>0<\alpha \leqslant \frac{1}{2}</equation>B.<equation>\frac{1}{2}<\alpha \leqslant 1</equation>C.<equation>1<\alpha \leqslant \frac{3}{2}</equation>D.<equation>\frac{3}{2}<\alpha <2</equation>

答案: D

**解析:**解 首先，<equation>\alpha >0</equation>，否则<equation>\lim_{n\rightarrow \infty}\sin \frac{1}{n^{\alpha}}\neq 0</equation><equation>\sum_{n=1}^{\infty}(-1)^{n}\sqrt{n}\sin \frac{1}{n^{\alpha}}</equation>不绝对收敛.于是，<equation>0 < \frac{1}{n^{\alpha}}\leqslant 1</equation><equation>\sin \frac{1}{n^{\alpha}}\geqslant 0.</equation>由于<equation>\sum_{n=1}^{\infty}(-1)^{n}\sqrt{n}\sin \frac{1}{n^{\alpha}}</equation>绝对收敛，故<equation>\sum_{n=1}^{\infty}\sqrt{n}\sin \frac{1}{n^{\alpha}}</equation>收敛.

由于<equation>\lim _ {n \rightarrow \infty} \frac {\sqrt {n} \sin \frac {1}{n ^ {\alpha}}}{n ^ {\frac {1}{2} - \alpha}} \xlongequal {\sin \frac {1}{n ^ {\alpha}} \sim \frac {1}{n ^ {\alpha}}} \lim _ {n \rightarrow \infty} \frac {n ^ {\frac {1}{2} - \alpha}}{n ^ {\frac {1}{2} - \alpha}} = 1,</equation>故<equation>\sum_{n=1}^{\infty}\sqrt{n}\sin \frac{1}{n^{\alpha}}</equation>与<equation>\sum_{n=1}^{\infty}n^{\frac{1}{2}-\alpha}</equation>同敛散.

由于<equation>n^{\frac{1}{2} -\alpha} = \frac{1}{n^{\alpha -\frac{1}{2}}}</equation>，故当<equation>\alpha -\frac{1}{2} >1</equation>，即<equation>\alpha >\frac{3}{2}</equation>时，<equation>\sum_{n = 1}^{\infty}n^{\frac{1}{2} -\alpha}</equation>收敛.

由于级数<equation>\sum_{n=1}^{\infty} \frac{(-1)^{n}}{n^{2-\alpha}}</equation>条件收敛，故<equation>\sum_{n=1}^{\infty} \frac{1}{n^{2-\alpha}}</equation>发散，于是<equation>2-\alpha\leqslant1</equation>又因为级数<equation>\sum_{n=1}^{\infty} \frac{(-1)^{n}}{n^{2-\alpha}}</equation>收敛，所以<equation>\lim_{n\to\infty}\frac{(-1)^{n}}{n^{2-\alpha}}=0</equation>，从而<equation>2-\alpha>0</equation>因此，<equation>1\leqslant\alpha<2.</equation>取<equation>\left(\frac{3}{2},+\infty\right)</equation>与[1,2）的交集，得<equation>\frac{3}{2} < \alpha < 2</equation>应选D.

---

**2011年第3题 | 选择题 | 4分 | 答案: A**

3. 设<equation>\{u_{n}\}</equation>是数列，则下列命题正确的是（    ）

A. 若<equation>\sum_{n=1}^{\infty} u_{n}</equation>收敛，则<equation>\sum_{n=1}^{\infty} \left(u_{2n-1}+u_{2n}\right)</equation>收敛

C. 若<equation>\sum_{n=1}^{\infty} u_{n}</equation>收敛，则<equation>\sum_{n=1}^{\infty} \left(u_{2n-1}-u_{2n}\right)</equation>收敛

B. 若<equation>\sum_{n=1}^{\infty} \left(u_{2n-1}+u_{2n}\right)</equation>收敛，则<equation>\sum_{n=1}^{\infty} u_{n}</equation>收敛

D. 若<equation>\sum_{n=1}^{\infty} \left(u_{2n-1}-u_{2n}\right)</equation>收敛，则<equation>\sum_{n=1}^{\infty} u_{n}</equation>收敛

答案: A

**解析:**解 依次讨论各选项.

对选项A，级数<equation>\sum_{n=1}^{\infty}\left(u_{2n-1}+u_{2n}\right)</equation>可由<equation>\sum_{n=1}^{\infty}u_{n}</equation>添加括号得到.由收敛级数的性质，可知当<equation>\sum_{n=1}^{\infty}u_{n}</equation>收敛时，<equation>\sum_{n=1}^{\infty}\left(u_{2n-1}+u_{2n}\right)</equation>收敛.应选A.

取<equation>u_{2n - 1} = 1, u_{2n} = -1</equation>，则<equation>\sum_{n = 1}^{\infty}\left(u_{2n - 1} + u_{2n}\right) = 0</equation>，而<equation>\sum_{n = 1}^{\infty}u_{n}</equation>发散.选项B不正确.

取<equation>u_{n} = (-1)^{n - 1}\frac{1}{n},\sum_{n = 1}^{\infty}u_{n}</equation>为交错级数，由莱布尼茨定理可知<equation>\sum_{n = 1}^{\infty}u_{n}</equation>收敛，但<equation>\begin{aligned} \sum_ {n = 1} ^ {\infty} \left(u _ {2 n - 1} - u _ {2 n}\right) &= \sum_ {n = 1} ^ {\infty} \left[ (- 1) ^ {2 n - 2} \frac {1}{2 n - 1} - (- 1) ^ {2 n - 1} \frac {1}{2 n} \right] \\ &= \sum_ {n = 1} ^ {\infty} \left(\frac {1}{2 n - 1} + \frac {1}{2 n}\right) = \sum_ {n = 1} ^ {\infty} \frac {4 n - 1}{2 n (2 n - 1)}. \end{aligned}</equation>由于<equation>\frac{4 n-1}{2 n(2 n-1)} \geqslant \frac{2 n-1}{2 n(2 n-1)}=\frac{1}{2 n}</equation>，而级数<equation>\sum_{n=1}^{\infty}\frac{1}{2 n}</equation>发散，故<equation>\sum_{n=1}^{\infty}\left(u_{2 n-1}-u_{2 n}\right)</equation>发散.选项C不正确取<equation>u_{n}=1</equation>，则<equation>\sum_{n=1}^{\infty}\left(u_{2 n-1}-u_{2 n}\right)=0</equation>，收敛，但<equation>\sum_{n=1}^{\infty}u_{n}</equation>发散.选项D不正确.

---


#### 幂级数


**2024年第4题 | 选择题 | 5分 | 答案: A**

4. 已知幂级数<equation>\sum_{n=0}^{\infty} a_{n} x^{n}</equation>的和函数为<equation>\ln(2+x)</equation>，则<equation>\sum_{n=0}^{\infty} n a_{2n}=(\quad)</equation>A.<equation>-\frac{1}{6}</equation>B.<equation>-\frac{1}{3}</equation>C.<equation>\frac{1}{6}</equation>D.<equation>\frac{1}{3}</equation>

答案: A

**解析:**解（法一）由<equation>\ln (1 + x) = \sum_{n = 1}^{\infty}(-1)^{n - 1}\frac{x^n}{n}(-1 < x\leqslant 1)</equation>可得<equation>\ln (2 + x) = \ln \left[ 2 \cdot \left(1 + \frac {x}{2}\right) \right] = \ln 2 + \ln \left(1 + \frac {x}{2}\right) = \ln 2 + \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1}}{n} \left(\frac {x}{2}\right) ^ {n}.</equation>由此可得，当<equation>n > 0</equation>时，<equation>x^{2n}</equation>的系数为<equation>a_{2n}=\frac{(-1)^{2n-1}}{2n2^{2n}}=\frac{-1}{2n2^{2n}}.</equation>因此，<equation>\sum_ {n = 0} ^ {\infty} n a _ {2 n} = \sum_ {n = 1} ^ {\infty} n a _ {2 n} = \sum_ {n = 1} ^ {\infty} \frac {- n}{2 n 2 ^ {2 n}} = \sum_ {n = 1} ^ {\infty} \frac {- 1}{2 ^ {2 n + 1}} = \frac {- \frac {1}{8}}{1 - \frac {1}{4}} = - \frac {1}{6}.</equation>应选A.

（法二）由<equation>\sum_{n = 0}^{\infty}a_nx^n = \ln (2 + x)</equation>可得<equation>\sum_{n = 0}^{\infty}a_n(-x)^n = \sum_{n = 0}^{\infty}(-1)^n a_nx^n = \ln (2 - x)</equation>.由此可得<equation>\sum_{n = 0}^{\infty}[1 + (-1)^n]a_nx^n = \ln (2 + x) + \ln (2 - x)</equation>，即<equation>2 \sum_ {n = 0} ^ {\infty} a _ {2 n} x ^ {2 n} = \ln (2 + x) + \ln (2 - x).</equation>对（1）式两端关于<equation>x</equation>求导可得，<equation>4 \sum_ {n = 1} ^ {\infty} n a _ {2 n} x ^ {2 n - 1} = \frac {1}{2 + x} - \frac {1}{2 - x}.</equation>在(2)式中令<equation>x = 1</equation>，可得<equation>4\sum_{n = 1}^{\infty}na_{2n} = \frac{1}{3} -1 = -\frac{2}{3}</equation>，进一步可得<equation>\sum_{n = 0}^{\infty}na_{2n} = -\frac{1}{6}</equation>因此，应选A.

（法三）注意到<equation>\left[ \ln (2 + x) \right] ^ {\prime} = \frac {1}{2 + x} = \frac {1}{2 \left(1 + \frac {x}{2}\right)} = \frac {1}{2} \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} \left(\frac {x}{2}\right) ^ {n},</equation>该幂级数的收敛半径为2，故在（-2，2）上，由牛顿一莱布尼茨公式可得<equation>\begin{aligned} \ln (2 + x) - \ln 2 &= \int_ {0} ^ {x} \left[ \ln (2 + t) \right] ^ {\prime} \mathrm {d} t = \int_ {0} ^ {x} \frac {1}{2} \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} \left(\frac {t}{2}\right) ^ {n} \mathrm {d} t \\ \frac {\text {逐 项 积 分}}{} \frac {1}{2} \sum_ {n = 0} ^ {\infty} \int_ {0} ^ {x} (- 1) ^ {n} \left(\frac {t}{2}\right) ^ {n} \mathrm {d} t &= \frac {1}{2} \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{n + 1} \cdot \frac {x ^ {n + 1}}{2 ^ {n}} \\ &= \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1} x ^ {n}}{n 2 ^ {n}}. \end{aligned}</equation>因此，<equation>\ln (2 + x) = \ln 2 + \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1} x ^ {n}}{n 2 ^ {n}}.</equation>其余同法一.

---

**2023年第13题 | 填空题 | 5分**

13.<equation>3. \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n}}{(2 n) !} = \underline {{}}</equation>

**答案:**<equation>\frac {\mathrm {e} ^ {x} + \mathrm {e} ^ {- x}}{2}.</equation>

**解析:**解（法一）考虑<equation>\mathrm{e}^{x}</equation>与<equation>\mathrm{e}^{-x}</equation>的幂级数展开式，<equation>\mathrm {e} ^ {x} = \sum_ {n = 0} ^ {\infty} \frac {x ^ {n}}{n !}, \quad \mathrm {e} ^ {- x} = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n} x ^ {n}}{n !}, \quad - \infty < x < + \infty .</equation>由此可得<equation>\mathrm {e} ^ {x} + \mathrm {e} ^ {- x} = \sum_ {n = 0} ^ {\infty} \frac {x ^ {n}}{n !} + \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n} x ^ {n}}{n !} = \sum_ {n = 0} ^ {\infty} \frac {\left[ 1 + (- 1) ^ {n} \right] x ^ {n}}{n !} = 2 \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n}}{(2 n) !}.</equation>因此，<equation>\sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n}}{(2 n) !} = \frac {\mathrm {e} ^ {x} + \mathrm {e} ^ {- x}}{2}.</equation>（法二）当 x=0时，<equation>\sum_{n=0}^{\infty}\frac{x^{2n}}{(2n)!}</equation>显然收敛. 又当 x≠0时，<equation>\lim _ {n \rightarrow \infty} \frac {x ^ {2 n + 2}}{(2 n + 2) !} \cdot \frac {(2 n) !}{x ^ {2 n}} = \lim _ {n \rightarrow \infty} \frac {x ^ {2}}{(2 n + 1) (2 n + 2)} = 0.</equation>由正项级数的比值审敛法可知，对任意<equation>x\neq 0</equation>，都有<equation>\sum_{n=0}^{\infty}\frac{x^{2n}}{(2n)!}</equation>收敛.因此，幂级数<equation>\sum_{n=0}^{\infty}\frac{x^{2n}}{(2n)!}</equation>的收敛域为<equation>(-\infty, +\infty).</equation>记<equation>\sum_{n=0}^{\infty}\frac{x^{2n}}{(2n)!}</equation>的和函数为 S(x)，则在<equation>(-\infty, +\infty)</equation>上，<equation>S ^ {\prime} (x) = \left[ \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n}}{(2 n) !} \right] ^ {\prime} \xlongequal {\text {逐 项 求 导}} \sum_ {n = 0} ^ {\infty} \frac {\left(x ^ {2 n}\right) ^ {\prime}}{(2 n) !} = \sum_ {n = 1} ^ {\infty} \frac {x ^ {2 n - 1}}{(2 n - 1) !},</equation><equation>S ^ {\prime \prime} (x) = \left[ \sum_ {n = 1} ^ {\infty} \frac {x ^ {2 n - 1}}{(2 n - 1) !} \right] ^ {\prime} \xlongequal {\text {逐 项 求 导}} \sum_ {n = 1} ^ {\infty} \frac {\left(x ^ {2 n - 1}\right) ^ {\prime}}{(2 n - 1) !} = \sum_ {n = 1} ^ {\infty} \frac {x ^ {2 n - 2}}{(2 n - 2) !} = \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n}}{(2 n) !}.</equation>由此可得，<equation>S^{\prime \prime}(x)=S(x), S(x)</equation>满足微分方程<equation>y^{\prime \prime}-y=0.</equation>这是一个二阶常系数齐次线性微分方程，其特征方程为<equation>r^{2}-1=0</equation>，特征根为<equation>r_{1,2}=\pm 1.</equation>从而通解为<equation>y=C_{1}\mathrm{e}^{x}+C_{2}\mathrm{e}^{-x}</equation>即<equation>S(x)=C_{1}\mathrm{e}^{x}+C_{2}\mathrm{e}^{-x}.</equation>将 x = 0 代入<equation>S ( x )=\sum_{n=0}^{\infty}\frac{x^{2 n}} {(2 n)!}, S^{\prime} ( x )=\sum_{n=1}^{\infty}\frac{x^{2 n-1}} {(2 n-1)!}</equation>可得，<equation>S ( 0 )=1, S^{\prime} ( 0 )=0.</equation>另一方面，由<equation>S ( x )=C_{1}\mathrm{e}^{x}+C_{2}\mathrm{e}^{-x}</equation>可得，<equation>S ( 0 )=C_{1}+C_{2}, S^{\prime} ( 0 )=\left(C_{1}\mathrm{e}^{x}-C_{2}\mathrm{e}^{-x}\right)\mid_{x=0}=C_{1}-C_{2}.</equation>于是，解得<equation>\left\{\begin{array}{l l} C_{1}+C_{2}=1, \\ C_{1}-C_{2}=0. \end{array} \right.</equation>因此，<equation>S ( x ) = \frac {\mathrm {e}^{x} + \mathrm {e}^{-x}}{2}.</equation>

---

**2022年第20题 | 解答题 | 12分**

20. （本题满分12分）

求幂级数<equation>\sum_ {n = 0} ^ {\infty} \frac {(- 4) ^ {n} + 1}{4 ^ {n} (2 n + 1)} x</equation>的收敛域及和函数 S(x).

**答案:**收敛域为<equation>[-1,1]</equation>，和函数<equation>S ( x )=\left\{\begin{array}{ll}\frac{\arctan x}{x}+\frac{1}{x}\ln \frac{2+x}{2-x},&x\in[-1,0)\cup(0,1],\\ 2,&x=0.\end{array}\right.</equation>

**解析:**先求收敛域.

原级数是一个缺项型幂级数，我们用比值法来求它的收敛半径.<equation>\lim _ {n \rightarrow \infty} \left| \frac {\frac {(- 4) ^ {n + 1} + 1}{4 ^ {n + 1} (2 n + 3)} x ^ {2 n + 2}}{\frac {(- 4) ^ {n} + 1}{4 ^ {n} (2 n + 1)} x ^ {2 n}} \right| = \lim _ {n \rightarrow \infty} \left| \frac {(- 4) ^ {n + 1} + 1}{(- 4) ^ {n} + 1} \cdot \frac {2 n + 1}{4 (2 n + 3)} \right| x ^ {2} = x ^ {2}.</equation>由比值审敛法可知，当<equation>| x | < 1</equation>时，原幂级数收敛；当<equation>| x | > 1</equation>时，原幂级数发散，从而收敛半径为1，收敛区间为（-1，1）.

又由于当<equation>x=\pm 1</equation>时，<equation>\text {原 幂 级 数} = \sum_ {n = 0} ^ {\infty} \frac {(- 4) ^ {n} + 1}{4 ^ {n} (2 n + 1)} = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{2 n + 1} + \sum_ {n = 0} ^ {\infty} \frac {1}{4 ^ {n} (2 n + 1)},</equation>而级数<equation>\sum_{n=0}^{\infty} \frac{(-1)^{n}}{2n+1}</equation>和<equation>\sum_{n=0}^{\infty} \frac{1}{4^{n}(2n+1)}</equation>均收敛，故原幂级数收敛。因此，原幂级数的收敛域为<equation>[-1,1]</equation>下面求和函数.

记<equation>S ( x )=\sum_{n=0}^{\infty}\frac{(-4)^{n}+1}{4^{n}(2n+1)} x^{2n}, x\in[-1,1],</equation>，则<equation>S (x) = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{2 n + 1} x ^ {2 n} + \sum_ {n = 0} ^ {\infty} \frac {1}{4 ^ {n} (2 n + 1)} x ^ {2 n}.</equation>记<equation>S_{1}(x)=\sum_{n=0}^{\infty}\frac{(-1)^{n}}{2n+1} x^{2n}, S_{2}(x)=\sum_{n=0}^{\infty}\frac{1}{4^{n}(2n+1)} x^{2n}</equation>，则当 x<equation>\in[ -1,1]</equation>时，<equation>S (x) = S _ {1} (x) + S _ {2} (x).</equation>注意到<equation>x S_{1}(x)=\sum_{n=0}^{\infty}\frac{(-1)^{n}}{2n+1} x^{2n+1}</equation>，故<equation>\begin{aligned} \left[ x S _ {1} (x) \right] ^ {\prime} &= \left[ \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{2 n + 1} x ^ {2 n + 1} \right] ^ {\prime} \xlongequal {\text {逐 项 求 导}} \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{2 n + 1} \left(x ^ {2 n + 1}\right) ^ {\prime} = \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} x ^ {2 n} \\ &= \frac {1}{1 + x ^ {2}}, \end{aligned}</equation><equation>x S _ {1} (x) = x S _ {1} (x) - 0 \times S _ {1} (0) = \int_ {0} ^ {x} \left[ t S _ {1} (t) \right] ^ {\prime} \mathrm {d} t = \int_ {0} ^ {x} \frac {1}{1 + t ^ {2}} \mathrm {d} t = \arctan x.</equation>当<equation>x \in[ - 1,0)\cup(0,1]</equation>时，<equation>S_{1}(x)=\frac{\arctan x}{x}</equation>当 x=0时，<equation>S_{1}(0)=\frac{(-1)^{0}}{2\times 0+1}=1.</equation>注意到<equation>x S_{2}(x)=\sum_{n=0}^{\infty}\frac{1}{4^{n}(2n+1)} x^{2n+1}</equation>，故<equation>\begin{aligned} \left[ x S _ {2} (x) \right] ^ {\prime} &= \left[ \sum_ {n = 0} ^ {\infty} \frac {1}{4 ^ {n} (2 n + 1)} x ^ {2 n + 1} \right] ^ {\prime} \stackrel {\mathrm {逐 项 求 导}} {=} \sum_ {n = 0} ^ {\infty} \frac {1}{4 ^ {n} (2 n + 1)} \left(x ^ {2 n + 1}\right) ^ {\prime} \\ &= \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n}}{4 ^ {n}} = \sum_ {n = 0} ^ {\infty} \left(\frac {x}{2}\right) ^ {2 n} = \frac {1}{1 - \left(\frac {x}{2}\right) ^ {2}} = \frac {4}{4 - x ^ {2}} \\ &= \frac {1}{2 - x} + \frac {1}{2 + x}, \end{aligned}</equation><equation>\begin{aligned} x S _ {2} (x) &= x S _ {2} (x) - 0 \times S _ {2} (0) = \int_ {0} ^ {x} \left[ t S _ {2} (t) \right] ^ {\prime} \mathrm {d} t = \int_ {0} ^ {x} \left(\frac {1}{2 - t} + \frac {1}{2 + t}\right) \mathrm {d} t \\ &= \ln \frac {2 + x}{2 - x}. \end{aligned}</equation>当<equation>x \in[ - 1,0)\cup(0,1]</equation>时，<equation>S_{2}(x) = \frac{1}{x}\ln \frac{2+x}{2-x}.</equation>当<equation>x=0</equation>时，<equation>S_{2}(0) = \frac{1}{1\times(2\times 0 + 1)} = 1.</equation>综上所述，幂级数的和函数为<equation>S (x) = \left\{ \begin{array}{l l} \frac {\arctan x}{x} + \frac {1}{x} \ln \frac {2 + x}{2 - x}, & x \in [ - 1, 0) \cup (0, 1 ], \\ 2, & x = 0. \end{array} \right.</equation>

---

**2021年第20题 | 解答题 | 12分**

20. (本题满分12分)

设 n为正整数，<equation>y=y_{n}(x)</equation>是微分方程<equation>x y^{\prime}-(n+1) y=0</equation>的满足条件<equation>y_{n}(1)=\frac{1}{n(n+1)}</equation>的解.

I. 求<equation>y_{n}(x)</equation>II. 求级数<equation>\sum_{n=1}^{\infty} y_{n}(x)</equation>的收敛域及和函数.

**答案:**（I）<equation>y_{n}(x)=\frac{x^{n+1}}{n(n+1)};</equation>（Ⅱ）收敛域为<equation>[-1,1]</equation>，和函数 s(x)<equation>= \left\{\begin{array}{ll}(1-x)\ln(1-x)+x,&x\in[-1,1),\\ 1,&x=1.\end{array}\right.</equation>

**解析:**解（I）整理<equation>x y^{\prime}-(n+1) y=0</equation>可得，<equation>y^{\prime}=\frac{n+1}{x} y.</equation>分离变量得<equation>\frac{\mathrm{d} y}{y}=\frac{n+1}{x}\mathrm{d} x.</equation>两端同时积分可得<equation>\ln |y|=(n+1)\ln |x|+C_{0}.</equation>于是，<equation>y_{n}(x)=Cx^{n+1}</equation>其中C为待定常数.

代入<equation>y_{n}(1)=\frac{1}{n(n+1)},</equation>可得<equation>C=\frac{1}{n(n+1)}.</equation>因此，<equation>y_{n}(x) = \frac{x^{n + 1}}{n(n + 1)}.</equation>（Ⅱ）记<equation>s(x) = \sum_{n = 1}^{\infty}\frac{x^{n + 1}}{n(n + 1)},</equation>其系数<equation>a_{n} = \frac{1}{n(n + 1)}.</equation><equation>\lim _ {n \rightarrow \infty} \left| \frac {a _ {n + 1}}{a _ {n}} \right| = \lim _ {n \rightarrow \infty} \frac {n (n + 1)}{(n + 1) (n + 2)} = 1.</equation>于是，<equation>s ( x )</equation>的收敛半径为1，收敛区间为<equation>(-1,1).</equation>s ( x ) 在 x=-1处为<equation>\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n(n+1)},</equation>由莱布尼茨定理可知该级数收敛. s ( x ) 在 x=1处为<equation>\sum_{n=1}^{\infty}\frac{1}{n(n+1)},</equation>由极限审敛法可知该级数收敛.因此，s ( x ) 的收敛域为<equation>[-1,1].</equation>下面用两种方法计算 s(x).

（法一）整理<equation>s(x).</equation>当 x<equation>\in(-1,1)</equation>时，<equation>\begin{aligned} s (x) &= \sum_ {n = 1} ^ {\infty} \left(\frac {x ^ {n + 1}}{n} - \frac {x ^ {n + 1}}{n + 1}\right) = x \sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n} - \sum_ {n = 1} ^ {\infty} \frac {x ^ {n + 1}}{n + 1} = x \sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n} - \sum_ {n = 2} ^ {\infty} \frac {x ^ {n}}{n} \\ &= (x - 1) \sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n} + x. \end{aligned}</equation>记<equation>t ( x )=\sum_{n=1}^{\infty}\frac{x^{n}}{n}</equation>，则<equation>s ( x )=(x-1)t ( x )+x.</equation><equation>t ^ {\prime} (x) = \left(\sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n}\right) ^ {\prime} \xlongequal {\text {逐 项 求 导}} \sum_ {n = 1} ^ {\infty} \left(\frac {x ^ {n}}{n}\right) ^ {\prime} = \sum_ {n = 1} ^ {\infty} x ^ {n - 1} = \frac {1}{1 - x}.</equation>注意到 t（0）=0，故<equation>t (x) = t (x) - t (0) = \int_ {0} ^ {x} \frac {1}{1 - t} \mathrm {d} t = - \ln (1 - x).</equation>于是，当 x<equation>\in(-1,1)</equation>时，s（x）=（1-x）<equation>\ln(1-x)+x.</equation>因为幂级数的和函数在收敛域上连续，且<equation>( 1-x)\ln(1-x)+x</equation>在 x=-1处连续，所以当 x<equation>\in[ -1,1)</equation>时，<equation>s (x) = (1 - x) \ln (1 - x) + x.</equation>当<equation>x=1</equation>时，<equation>s(1)=\sum_{n=1}^{\infty}\frac{1}{n(n+1)}.</equation>计算<equation>\sum_{n=1}^{\infty} \frac{1}{n(n+1)}</equation>的部分和<equation>\sum_{n=1}^{k} \frac{1}{n(n+1)}</equation>得<equation>\sum_ {n = 1} ^ {k} \frac {1}{n (n + 1)} = \sum_ {n = 1} ^ {k} \left(\frac {1}{n} - \frac {1}{n + 1}\right) = 1 - \frac {1}{2} + \frac {1}{2} - \frac {1}{3} + \dots + \frac {1}{k} - \frac {1}{k + 1} = 1 - \frac {1}{k + 1}.</equation>于是，<equation>\sum_{n = 1}^{\infty}\frac{1}{n(n + 1)} = \lim_{k\to \infty}\sum_{n = 1}^{k}\frac{1}{n(n + 1)} = \lim_{k\to \infty}\left(1 - \frac{1}{k + 1}\right) = 1.</equation>因此，s（x）为分段函数.<equation>s (x) = \left\{ \begin{array}{l l} (1 - x) \ln (1 - x) + x, & x \in [ - 1, 1), \\ 1, & x = 1. \end{array} \right.</equation>（法二）当<equation>x\in(-1,1)</equation>时，<equation>s ^ {\prime} (x) = \left[ \sum_ {n = 1} ^ {\infty} \frac {x ^ {n + 1}}{n (n + 1)} \right] ^ {\prime} \xlongequal {\text {逐 项 求 导}} \sum_ {n = 1} ^ {\infty} \left[ \frac {x ^ {n + 1}}{n (n + 1)} \right] ^ {\prime} = \sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n}.</equation><equation>s ^ {\prime \prime} (x) = \left(\sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n}\right) ^ {\prime} \xlongequal {\text {逐 项 求 导}} \sum_ {n = 1} ^ {\infty} \left(\frac {x ^ {n}}{n}\right) ^ {\prime} = \sum_ {n = 1} ^ {\infty} x ^ {n - 1} = \frac {1}{1 - x}.</equation>注意到<equation>s^{\prime}(0)=0</equation>，故<equation>s ^ {\prime} (x) = s ^ {\prime} (x) - s ^ {\prime} (0) = \int_ {0} ^ {x} \frac {1}{1 - t} \mathrm {d} t = - \ln (1 - t) \Big | _ {0} ^ {x} = - \ln (1 - x).</equation>又因为 s（0）=0，所以<equation>\begin{aligned} s (x) &= s (x) - s (0) = \int_ {0} ^ {x} [ - \ln (1 - t) ] \mathrm {d} t = - \left[ t \ln (1 - t) \left| _ {0} ^ {x} - \int_ {0} ^ {x} \frac {- t}{1 - t} \mathrm {d} t \right. \right] \\ &= - x \ln (1 - x) - \int_ {0} ^ {x} \frac {t}{1 - t} \mathrm {d} t = - x \ln (1 - x) - \int_ {0} ^ {x} \left(- 1 + \frac {1}{1 - t}\right) \mathrm {d} t \\ &= - x \ln (1 - x) - \left[ - t - \ln (1 - t) \right] \left| _ {0} ^ {x} = - x \ln (1 - x) + \left[ t + \ln (1 - t) \right] \right| _ {0} ^ {x} \\ &= - x \ln (1 - x) + x + \ln (1 - x) = (1 - x) \ln (1 - x) + x. \end{aligned}</equation>其余同法一.

---

**2020年第4题 | 选择题 | 4分 | 答案: B**

4. 设幂级数<equation>\sum_{n=1}^{\infty} n a_{n}(x-2)^{n}</equation>的收敛区间为（-2，6），则<equation>\sum_{n=1}^{\infty} a_{n}(x+1)^{2n}</equation>的收敛区间为（    )

A. (-2,6) B. (-3,1) C. (-5,3) D. (-17,15)

答案: B

**解析:**解 由已知条件可得，幂级数<equation>\sum_{n=1}^{\infty} n a_{n}(x-2)^{n}=(x-2)\sum_{n=1}^{\infty} n a_{n}(x-2)^{n-1}</equation>的收敛中心为2，收敛区间为（-2，6），故收敛半径为6-2=4.由收敛半径的平移不变性可知，<equation>\sum_{n=1}^{\infty} n a_{n} x^{n-1}</equation>的收敛半径为4.记<equation>s(x)=\int_{0}^{x}\sum_{n=1}^{\infty} n a_{n} t^{n-1}\mathrm{d}t</equation>则<equation>s(x)\overset{\mathrm{逐项积分}}{=}\sum_{n=1}^{\infty}\int_{0}^{x} n a_{n} t^{n-1}\mathrm{d}t=\sum_{n=1}^{\infty} a_{n} x^{n}.</equation>由收敛半径的逐项积分不变性可知，<equation>\sum_{n=1}^{\infty} a_{n} x^{n}</equation>的收敛半径也为4.<equation>\sum_{n=1}^{\infty} a_{n}(x+1)^{2n}</equation>为缺项幂级数，其收敛半径等于<equation>\sum_{n=1}^{\infty} a_{n} x^{2n}</equation>的收敛半径.由<equation>\sum_{n=1}^{\infty} a_{n} x^{n}</equation>的收敛半径为4可得，<equation>\sum_{n=1}^{\infty} a_{n} x^{2n}</equation>的收敛半径为2.又因为<equation>\sum_{n=1}^{\infty} a_{n}(x+1)^{2n}</equation>的收敛中心为-1，所以其收敛区间为（-3，1）因此，应选B.

---

**2018年第18题 | 解答题 | 10分**

18. (本题满分10分)

已知<equation>\cos 2x-\frac{1}{(1+x)^{2}}=\sum_{n=0}^{\infty}a_{n}x^{n}(-1<x<1)</equation>，求<equation>a_{n}.</equation>

**答案:**<equation>a _ {n} = \left\{ \begin{array}{l l} \frac {(- 1) ^ {k} 4 ^ {k}}{(2 k) !} - 2 k - 1, & n = 2 k, \\ 2 k + 2, & n = 2 k + 1, \end{array} \right. \mathrm {其 中} k \mathrm {为 非 负 整 数}.</equation>

**解析:**由<equation>\cos x</equation>的幂级数展开式可得，<equation>\cos 2 x = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n} (2 x) ^ {2 n}}{(2 n) !} = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n} 4 ^ {n} x ^ {2 n}}{(2 n) !}, - \infty < x < + \infty .</equation>注意到<equation>\left(\frac{1}{1+x}\right)^{\prime}=-\frac{1}{(1+x)^{2}}</equation>故<equation>\begin{aligned} - \frac {1}{(1 + x) ^ {2}} &= \left(\frac {1}{1 + x}\right) ^ {\prime} = \left[ \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} x ^ {n} \right] ^ {\prime} = \sum_ {n = 1} ^ {\infty} (- 1) ^ {n} n x ^ {n - 1} \\ &= \sum_ {n = 0} ^ {\infty} (- 1) ^ {n + 1} (n + 1) x ^ {n}, - 1 < x < 1. \end{aligned}</equation>于是，<equation>\cos 2 x - \frac {1}{(1 + x) ^ {2}} = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n} 4 ^ {n} x ^ {2 n}}{(2 n) !} + \sum_ {n = 0} ^ {\infty} (- 1) ^ {n + 1} (n + 1) x ^ {n} = \sum_ {n = 0} ^ {\infty} a _ {n} x ^ {n}, - 1 < x < 1.</equation>由于<equation>a_{n}</equation>为<equation>x^{n}</equation>的系数，故<equation>\sum_{n=0}^{\infty}\frac{(-1)^{n}4^{n}x^{2n}}{(2n)!}+\sum_{n=0}^{\infty}(-1)^{n+1}(n+1)x^{n}</equation>中<equation>x^{n}</equation>的系数等于<equation>a_{n}.</equation>当<equation>n=2k</equation>，<equation>k=0,1,2,\dots</equation>时，<equation>a _ {2 k} = \frac {(- 1) ^ {k} 4 ^ {k}}{(2 k) !} + (- 1) ^ {2 k + 1} (2 k + 1) = \frac {(- 1) ^ {k} 4 ^ {k}}{(2 k) !} - 2 k - 1.</equation>当<equation>n = 2k + 1</equation>，<equation>k = 0,1,2,\dots</equation>时，<equation>a _ {2 k + 1} = (- 1) ^ {2 k + 1 + 1} (2 k + 1 + 1) = 2 k + 2.</equation>因此，<equation>a _ {n} = \left\{ \begin{array}{l l} \frac {(- 1) ^ {k} 4 ^ {k}}{(2 k) !} - 2 k - 1, & n = 2 k, \\ 2 k + 2, & n = 2 k + 1, \end{array} \right.</equation>其中 k为非负整数.

---

**2017年第19题 | 解答题 | 10分**

19. (本题满分10分)

若<equation>a_{0}=1, a_{1}=0, a_{n+1}=\frac{1}{n+1}\left(n a_{n}+a_{n-1}\right)\left(n=1, 2, 3, \cdots\right), S(x)</equation>为幂级数<equation>\sum_{n=0}^{\infty}a_{n}x^{n}</equation>的和函数.

I. 证明<equation>\sum_{n=0}^{\infty}a_{n}x^{n}</equation>的收敛半径不小于1；

II. 证明<equation>(1 - x)S^{\prime}(x) - xS(x) = 0,(x\in (-1,1))</equation>，并求<equation>S(x)</equation>的表达式.

**答案:**（I）证明略；

（Ⅱ）证明略，<equation>S ( x )=\frac{\mathrm{e}^{-x}}{1-x}, x \in(-1,1).</equation>

**解析:**解（I）（法一）利用阿贝尔定理.我们证明在（-1，1）内，幂级数<equation>\sum_{n=0}^{\infty} a_{n} x^{n}</equation>绝对收敛，从而由阿贝尔定理可知幂级数的收敛半径不小于1.

首先，证明对任意的<equation>n=0,1,2,\dots</equation>，若 m≤n，则<equation>|a_{m}| \leqslant 1.</equation>由已知条件，<equation>a_{0}=1, a_{1}=0</equation>，故<equation>a_{2}=\frac{1}{2}(0+1)=\frac{1}{2}\leqslant1.</equation>假设对<equation>n = k</equation>时，命题成立，则当<equation>n = k + 1</equation>时，只需证明<equation>|a_{k + 1}| \leqslant 1</equation>.

由递推式<equation>a_{n + 1} = \frac{1}{n + 1}\left(n a_{n} + a_{n - 1}\right)</equation>以及归纳假设可得，<equation>\left| a _ {k + 1} \right| \leqslant \frac {k}{k + 1} \left| a _ {k} \right| + \frac {1}{k + 1} \left| a _ {k - 1} \right| \leqslant \frac {k}{k + 1} + \frac {1}{k + 1} = 1.</equation>由数学归纳法可知，对任意的 n=0，1，2，…，若 m≤n，则<equation>|a_{m}| \leqslant 1.</equation>由此易知，对任意的 n=0， 1，2，…，<equation>|a_{n}| \leqslant 1.</equation><equation>x _ {0} \in (- 1, 1)</equation><equation>\sum_ {n = 0} ^ {\infty} x _ {0} ^ {n}</equation><equation>\left| a _ {n} \right| \leqslant 1</equation><equation>\left| a _ {n} x _ {0} ^ {n} \right| \leqslant \left| x _ {0} ^ {n} \right|</equation><equation>\sum_ {n = 0} ^ {\infty} \left| a _ {n} x _ {0} ^ {n} \right| \leqslant \sum_ {n = 0} ^ {\infty} \left| x _ {0} ^ {n} \right|</equation><equation>\sum_ {n = 0} ^ {\infty} a _ {n} x _ {0} ^ {n}</equation>由于对任意的<equation>x_{0}\in(-1,1)</equation>，级数<equation>\sum_{n=0}^{\infty} a_{n} x_{0}^{n}</equation>均绝对收敛，故由阿贝尔定理可知，幂级数<equation>\sum_{n=0}^{\infty} a_{n} x^{n}</equation>的收敛半径不小于1.

下面的法二、法三均需要计算<equation>a_{n}</equation>的表达式，并且可计算得幂级数的收敛半径实际上等于1.

由<equation>a_{n+1}=\frac{1}{n+1} \left(n a_{n}+a_{n-1}\right) \left(n=1,2,3,\cdots\right)</equation>可得<equation>a _ {n + 1} - a _ {n} = - \frac {1}{n + 1} \left(a _ {n} - a _ {n - 1}\right) (n = 1, 2, 3, \dots).</equation>于是，<equation>a _ {n} - a _ {n - 1} = \frac {- 1}{n} \left(a _ {n - 1} - a _ {n - 2}\right) = \frac {- 1}{n} \cdot \frac {- 1}{n - 1} \left(a _ {n - 2} - a _ {n - 3}\right) = \dots = \frac {(- 1) ^ {n - 1}}{n !} \left(a _ {1} - a _ {0}\right) = \frac {(- 1) ^ {n}}{n !}.</equation>因此，<equation>a _ {n} = \sum_ {k = 1} ^ {n} \left(a _ {k} - a _ {k - 1}\right) + a _ {0} = \sum_ {k = 1} ^ {n} \frac {(- 1) ^ {k}}{k !} + 1 = \sum_ {k = 0} ^ {n} \frac {(- 1) ^ {k}}{k !}.</equation>注意到<equation>\mathrm{e}^{-x}=\sum_{n=0}^{\infty}\frac{(-1)^{n}x^{n}}{n!}</equation>，故<equation>\lim_{n\to \infty}a_{n}=\mathrm{e}^{-1}.</equation>下面我们用两种方法证明<equation>\sum a_{n}x^{n}</equation>的收敛半径等于1.

（法二）考虑<equation>\left| \frac{a_{n+1}}{a_{n}} \right|.</equation>由<equation>\lim_{n\rightarrow\infty}a_{n}=\mathrm{e}^{-1}</equation>，可得<equation>\lim_{n\rightarrow\infty}a_{n+1}=\mathrm{e}^{-1}</equation>，从而<equation>\lim _ {n \rightarrow \infty} \left| \frac {a _ {n + 1}}{a _ {n}} \right| = 1.</equation>因此，幂级数<equation>\sum_{n=0}^{\infty} a_{n} x^{n}</equation>的收敛半径等于1.

（法三）考虑<equation>\sqrt[n]{|a_n|}.</equation><equation>\lim _ {n \rightarrow \infty} \sqrt [ n ]{| a _ {n} |} = \lim _ {n \rightarrow \infty} \mathrm {e} ^ {\frac {1}{n} \ln | a _ {n} |} = \mathrm {e} ^ {\lim _ {n \rightarrow \infty} \frac {\ln | a _ {n} |}{n}} \underline {{\frac {\lim _ {n \rightarrow \infty} a _ {n} = \mathrm {e} ^ {- 1}}{n}}} \mathrm {e} ^ {\lim _ {n \rightarrow \infty} \frac {- 1}{n}} = 1.</equation><equation>\sum_ {n = 0} ^ {\infty} a _ {n} x ^ {n}</equation>（Ⅱ）由第（Ⅰ）问可知，在区间（-1，1）内，<equation>S ( x )</equation>可逐项求导.<equation>x S (x) = \sum_ {n = 0} ^ {\infty} a _ {n} x ^ {n + 1} = \sum_ {n = 1} ^ {\infty} a _ {n - 1} x ^ {n},</equation><equation>S ^ {\prime} (x) = \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n - 1},</equation><equation>(1 - x) S ^ {\prime} (x) = \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n - 1} - \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n} = \sum_ {n = 0} ^ {\infty} (n + 1) a _ {n + 1} x ^ {n} - \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n}.</equation>将<equation>a_{n+1}=\frac{1}{n+1}\left(n a_{n}+a_{n-1}\right)\left(n=1,2,3,\dots\right)</equation>代入<equation>(1-x)S^{\prime}(x)</equation>，得<equation>\begin{aligned} (1 - x) S ^ {\prime} (x) - x S (x) &= \sum_ {n = 0} ^ {\infty} (n + 1) a _ {n + 1} x ^ {n} - \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n} - \sum_ {n = 1} ^ {\infty} a _ {n - 1} x ^ {n} \\ &= a _ {1} + \sum_ {n = 1} ^ {\infty} \left(n a _ {n} + a _ {n - 1}\right) x ^ {n} - \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n} - \sum_ {n = 1} ^ {\infty} a _ {n - 1} x ^ {n} = a _ {1} = 0. \end{aligned}</equation>解微分方程（1-x）y'-xy=0.分离变量得<equation>\frac {\mathrm {d} y}{y} = \left(\frac {x}{1 - x}\right) \mathrm {d} x.</equation>上式两端积分得<equation>\ln | y | = \int \left(- 1 + \frac {1}{1 - x}\right) \mathrm {d} x = - x - \ln (1 - x) + C.</equation>当 x=0时，y=1，代入上式得 C=0.由于初值为<equation>y(0)=1>0</equation>，故取<equation>\ln y=-x-\ln(1-x)</equation>即<equation>y=\frac{\mathrm{e}^{-x}}{1-x}.</equation>因此，<equation>S ( x ) = \frac {\mathrm {e}^{- x}}{1 - x}, x \in(-1,1).</equation>

---

**2016年第19题 | 解答题 | 10分**

19. (本题满分10分)

求幂级数<equation>\sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n + 2}}{(n + 1) (2 n + 1)}</equation>的收敛域及和函数.

**答案:**收敛域为<equation>[-1,1]</equation>，和函数 s(x)<equation>\left\{\begin{array}{l l}x\ln \frac{1+x}{1-x}+\ln(1-x^{2}),&x\in(-1,1),\\ 2\ln 2,&x=\pm 1.\end{array}\right.</equation>

**解析:**解 先求收敛域.

原级数是一个缺项型幂级数，我们用比值法来求它的收敛半径.<equation>\lim _ {n \rightarrow \infty} \left| \frac {\frac {x ^ {2 n + 4}}{(n + 2) (2 n + 3)}}{\frac {x ^ {2 n + 2}}{(n + 1) (2 n + 1)}} \right| = \lim _ {n \rightarrow \infty} \left| \frac {(n + 1) (2 n + 1)}{(n + 2) (2 n + 3)} x ^ {2} \right| = x ^ {2}.</equation>由比值审敛法可知，当<equation>|x| < 1</equation>时，原幂级数收敛；当<equation>|x| > 1</equation>时，原幂级数发散，从而收敛半径为1，收敛区间为（-1，1）.

又由于当 x=<equation>\pm 1</equation><equation>\text {原 幂 级 数} = \sum_ {n = 0} ^ {\infty} \frac {1}{(n + 1) (2 n + 1)} \leqslant \sum_ {n = 0} ^ {\infty} \frac {1}{(n + 1) ^ {2}} = \sum_ {n = 1} ^ {\infty} \frac {1}{n ^ {2}},</equation>而<equation>\sum_{n=1}^{\infty}\frac{1}{n^{2}}</equation>收敛，故原幂级数收敛.因此，原幂级数的收敛域为[-1,1].

下面求和函数.

（法一）记<equation>s(x)=\sum_{n=0}^{\infty}\frac{x^{2n+2}}{(n+1)(2n+1)}, x\in[-1,1].</equation>在收敛区间内，可对幂级数进行逐项求导，且不改变幂级数的收敛半径，从而<equation>s ^ {\prime} (x) = \left[ \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n + 2}}{(n + 1) (2 n + 1)} \right] ^ {\prime} = \sum_ {n = 0} ^ {\infty} \left[ \frac {x ^ {2 n + 2}}{(n + 1) (2 n + 1)} \right] ^ {\prime} = 2 \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n + 1}}{2 n + 1}, x \in (- 1, 1),</equation><equation>s ^ {\prime \prime} (x) = 2 \left(\sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n + 1}}{2 n + 1}\right) ^ {\prime} = 2 \sum_ {n = 0} ^ {\infty} \left(\frac {x ^ {2 n + 1}}{2 n + 1}\right) ^ {\prime} = 2 \sum_ {n = 0} ^ {\infty} x ^ {2 n} = \frac {2}{1 - x ^ {2}}, x \in (- 1, 1).</equation>先求<equation>s^{\prime}(x).</equation>.由于<equation>s^{\prime}(0)=0</equation>，故<equation>s ^ {\prime} (x) = \int_ {0} ^ {x} s ^ {\prime \prime} (t) \mathrm {d} t = \int_ {0} ^ {x} \frac {2}{1 - t ^ {2}} \mathrm {d} t = \int_ {0} ^ {x} \left(\frac {1}{1 - t} + \frac {1}{1 + t}\right) \mathrm {d} t = \ln \frac {1 + x}{1 - x}, x \in (- 1, 1).</equation>又因为 s（0）=0，所以<equation>\begin{aligned} s (x) &= \int_ {0} ^ {x} s ^ {\prime} (t) \mathrm {d} t = \int_ {0} ^ {x} \left[ \ln (1 + t) - \ln (1 - t) \right] \mathrm {d} t \\ \underline {{\mathrm {分 部 积 分}}} t \left[ \ln (1 + t) - \ln (1 - t) \right] \left| _ {0} ^ {x} - \int_ {0} ^ {x} t \left(\frac {1}{1 + t} + \frac {1}{1 - t}\right) \mathrm {d} t \right. \\ &= x \ln \frac {1 + x}{1 - x} - \int_ {0} ^ {x} \frac {2 t}{1 - t ^ {2}} \mathrm {d} t = x \ln \frac {1 + x}{1 - x} + \int_ {0} ^ {x} \frac {\mathrm {d} \left(1 - t ^ {2}\right)}{1 - t ^ {2}} \\ &= x \ln \frac {1 + x}{1 - x} + \ln \left(1 - x ^ {2}\right), x \in (- 1, 1). \end{aligned}</equation>最后，由于幂级数的和函数在收敛域上连续，故<equation>\begin{aligned} s (1) &= \lim _ {x \rightarrow 1 ^ {-}} s (x) = \lim _ {x \rightarrow 1 ^ {-}} \left[ x \ln \frac {1 + x}{1 - x} + \ln \left(1 - x ^ {2}\right)\right] \\ &= \lim _ {x \rightarrow 1 ^ {-}} \left[ x \ln (1 + x) - x \ln (1 - x) + \ln (1 + x) + \ln (1 - x) \right] \\ &= \lim _ {x \rightarrow 1 ^ {-}} \left[ (1 + x) \ln (1 + x) + (1 - x) \ln (1 - x) \right] \\ \underline {{\underline {{\lim _ {x \rightarrow 1 ^ {-}}} (1 - x) \ln (1 - x) \stackrel {\mathrm {洛 必 达}} {=} 0}}} 2 \ln 2 + 0 &= 2 \ln 2. \end{aligned}</equation>同理可得 s（-1）=2ln2.

因此，<equation>s ( x ) = \left\{ \begin{array}{l l} x \ln \frac {1 + x}{1 - x} + \ln \left( 1 - x^{2} \right), & x \in(-1,1), \\ 2 \ln 2, & x = \pm 1. \end{array} \right.</equation>（法二）记<equation>\begin{aligned} s (x) &= \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n + 2}}{(n + 1) (2 n + 1)} = 2 \cdot \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n + 2}}{(2 n + 1) (2 n + 2)} \\ &= 2 \cdot \sum_ {n = 0} ^ {\infty} \left(\frac {x ^ {2 n + 2}}{2 n + 1} - \frac {x ^ {2 n + 2}}{2 n + 2}\right), x \in [ - 1, 1 ]. \end{aligned}</equation>记<equation>s_{1}(x)=\sum_{n=0}^{\infty}\frac{x^{2n+1}}{2n+1}, s_{2}(x)=\sum_{n=0}^{\infty}\frac{x^{2n+2}}{2n+2}, x\in(-1,1),</equation>则当<equation>x\in(-1,1)</equation>时，<equation>s (x) = 2 \left[ x s _ {1} (x) - s _ {2} (x) \right].</equation>下面我们分别计算<equation>s_{1}(x)</equation>与<equation>s_{2}(x).</equation>由于<equation>s_1^{\prime}(x) = \left(\sum_{n = 0}^{\infty}\frac{x^{2n + 1}}{2n + 1}\right)^{\prime} = \sum_{n = 0}^{\infty}\left(\frac{x^{2n + 1}}{2n + 1}\right)^{\prime} = \sum_{n = 0}^{\infty}x^{2n} = \frac{1}{1 - x^2}, x\in(-1,1), s_1(0) = 0</equation>，故<equation>s _ {1} (x) = \int_ {0} ^ {x} \frac {1}{1 - t ^ {2}} \mathrm {d} t = \frac {1}{2} \ln \frac {1 + x}{1 - x}, x \in (- 1, 1).</equation>由于<equation>s_2^{\prime}(x) = \left(\sum_{n = 0}^{\infty}\frac{x^{2n + 2}}{2n + 2}\right)^{\prime} = \sum_{n = 0}^{\infty}\left(\frac{x^{2n + 2}}{2n + 2}\right)^{\prime} = \sum_{n = 0}^{\infty}x^{2n + 1} = \frac{x}{1 - x^2},x\in(-1,1),s_2(0) = 0</equation>，故<equation>s _ {2} (x) = \int_ {0} ^ {x} \frac {t}{1 - t ^ {2}} \mathrm {d} t = - \frac {1}{2} \ln \left(1 - x ^ {2}\right), x \in (- 1, 1).</equation>因此，当<equation>x\in(-1,1)</equation>时，<equation>s (x) = 2 \left[ x s _ {1} (x) - s _ {2} (x) \right] = x \ln \frac {1 + x}{1 - x} + \ln \left(1 - x ^ {2}\right).</equation>其余同法一.

---

**2014年第18题 | 解答题 | 10分**

18. (本题满分10分)

求幂级数<equation>\sum_{n=0}^{\infty} ( n+1 ) ( n+3 ) x^{n}</equation>的收敛域及和函数.

**答案:**(18) 收敛域为<equation>(-1,1)</equation>，和函数<equation>s(x) = \frac{3 - x}{(1 - x)^{3}}.</equation>

**解析:**解 先求收敛域.

令<equation>a_{n} = (n + 1)(n + 3)</equation>，则<equation>\lim _ {n \rightarrow \infty} \left| \frac {a _ {n + 1}}{a _ {n}} \right| = \lim _ {n \rightarrow \infty} \frac {(n + 2) (n + 4)}{(n + 1) (n + 3)} = 1,</equation>从而幂级数的收敛半径为1，收敛区间为（-1，1）.又因为幂级数在 x=<equation>\pm 1</equation>时发散，所以幂级数的收敛域为（-1，1）.

下面求和函数.

（法一）记<equation>s ( x )=\sum_{n=0}^{\infty} ( n+1 ) ( n+3 ) x^{n}, x\in(-1,1).</equation>由于幂级数在其收敛区间内可逐项求导和逐项积分，故<equation>\begin{aligned} s (x) &= \sum_ {n = 0} ^ {\infty} (n + 1) (n + 3) x ^ {n} = \sum_ {n = 0} ^ {\infty} (n + 3) \left(x ^ {n + 1}\right) ^ {\prime} = \sum_ {n = 0} ^ {\infty} \left(x ^ {n + 1}\right) ^ {\prime} + \sum_ {n = 0} ^ {\infty} (n + 2) \left(x ^ {n + 1}\right) ^ {\prime} \\ &= \left(\sum_ {n = 0} ^ {\infty} x ^ {n + 1}\right) ^ {\prime} + \sum_ {n = 0} ^ {\infty} \left(x ^ {n + 2}\right) ^ {\prime \prime} = \left(\sum_ {n = 0} ^ {\infty} x ^ {n + 1}\right) ^ {\prime} + \left(\sum_ {n = 0} ^ {\infty} x ^ {n + 2}\right) ^ {\prime \prime} = \left(\frac {x}{1 - x}\right) ^ {\prime} + \left(\frac {x ^ {2}}{1 - x}\right) ^ {\prime \prime} \\ &= \frac {1}{(1 - x) ^ {2}} + \frac {2}{(1 - x) ^ {3}} = \frac {3 - x}{(1 - x) ^ {3}}, x \in (- 1, 1). \end{aligned}</equation>因此，幂级数的和函数为<equation>s ( x )=\frac{3-x}{(1-x)^{3}}, x\in(-1,1).</equation>（法二）也可以如下计算<equation>s(x).</equation><equation>\begin{aligned} s (x) &= \sum_ {n = 0} ^ {\infty} (n + 1) (n + 3) x ^ {n} = \sum_ {n = 0} ^ {\infty} (n + 3) \left(x ^ {n + 1}\right) ^ {\prime} = 3 \sum_ {n = 0} ^ {\infty} \left(x ^ {n + 1}\right) ^ {\prime} + \sum_ {n = 0} ^ {\infty} n \left(x ^ {n + 1}\right) ^ {\prime} \\ &= 3 \left(\sum_ {n = 0} ^ {\infty} x ^ {n + 1}\right) ^ {\prime} + \sum_ {n = 0} ^ {\infty} (n + 1) n x ^ {n} = 3 \cdot \left(\frac {x}{1 - x}\right) ^ {\prime} + x \cdot \sum_ {n = 0} ^ {\infty} (n + 1) n x ^ {n - 1} \\ &= \frac {3}{(1 - x) ^ {2}} + x \cdot \sum_ {n = 0} ^ {\infty} \left(x ^ {n + 1}\right) ^ {\prime \prime} = \frac {3}{(1 - x) ^ {2}} + x \cdot \left(\frac {x}{1 - x}\right) ^ {\prime \prime} = \frac {3}{(1 - x) ^ {2}} + \frac {2 x}{(1 - x) ^ {3}} \\ &= \frac {3 - x}{(1 - x) ^ {3}}, x \in (- 1, 1). \end{aligned}</equation>

---

**2009年第11题 | 填空题 | 4分**

11. 幂级数<equation>\sum_{n=1}^{\infty} \frac{\mathrm{e}^{n}-(-1)^{n}}{n^{2}} x^{n}</equation>的收敛半径为 ___

**解析:**<equation>a _ {n} = \frac {\mathrm {e} ^ {n} - (- 1) ^ {n}}{n ^ {2}}</equation><equation>\lim _ {n \rightarrow \infty} \left| \frac {a _ {n + 1}}{a _ {n}} \right| = \lim _ {n \rightarrow \infty} \frac {\frac {\mathrm {e} ^ {n + 1} - (- 1) ^ {n + 1}}{(n + 1) ^ {2}}}{\frac {\mathrm {e} ^ {n} - (- 1) ^ {n}}{n ^ {2}}} = \lim _ {n \rightarrow \infty} \frac {\mathrm {e} ^ {n + 1} - (- 1) ^ {n + 1}}{\mathrm {e} ^ {n} - (- 1) ^ {n}} \cdot \frac {n ^ {2}}{(n + 1) ^ {2}} = \lim _ {n \rightarrow \infty} \frac {\mathrm {e} - \frac {(- 1) ^ {n + 1}}{\mathrm {e} ^ {n}}}{1 - \frac {(- 1) ^ {n}}{\mathrm {e} ^ {n}}} \cdot 1 = \mathrm {e}.</equation>因此，幂级数的收敛半径为<equation>\frac{1}{e}。</equation>

---


### 多元函数微积分学

#### 交换积分次序与坐标系之间的转化


**2025年第4题 | 选择题 | 5分 | 答案: D**

4. 设函数 f(x) 连续，<equation>\int_{0}^{1}\mathrm{d}y\int_{0}^{y}f(x)\mathrm{d}x=</equation>(    )

A.<equation>\int_{0}^{1}x f(x)\mathrm{d}x</equation>B.<equation>\int_{0}^{1}(x+1)f(x)\mathrm{d}x</equation>C.<equation>\int_{0}^{1}(x-1)f(x)\mathrm{d}x</equation>D.<equation>\int_{0}^{1}(1-x)f(x)\mathrm{d}x</equation>

答案: D

**解析:**解 二次积分<equation>\int_{0}^{1}\mathrm{d}y\int_{0}^{y}f(x)\mathrm{d}x</equation>对应的二重积分的积分区域<equation>D = \left\{(x, y) \mid 0 \leqslant x \leqslant y, 0 \leqslant y \leqslant 1 \right\}.</equation>区域 D如图所示.将 D写成 X型区域.<equation>D = \left\{(x, y) \mid x \leqslant y \leqslant 1, 0 \leqslant x \leqslant 1 \right\}.</equation>于是，<equation>\int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {y} f (x) \mathrm {d} x = \iint_ {D} f (x) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} f (x) \mathrm {d} x \int_ {x} ^ {1} \mathrm {d} y = \int_ {0} ^ {1} (1 - x) f (x) \mathrm {d} x.</equation>因此，应选D.

---

**2024年第3题 | 选择题 | 5分 | 答案: A**

3. 设 f(x,y)是连续函数，则<equation>\int_{\frac{\pi}{6}}^{\frac{\pi}{2}} \mathrm{d} x \int_{\sin x}^{1} f(x,y) \mathrm{d} y=</equation>(    )

A.<equation>\int_{\frac{1}{2}}^{1} \mathrm{d} y \int_{\frac{\pi}{6}}^{\arcsin y} f(x,y) \mathrm{d} x</equation>B.<equation>\int_{\frac{1}{2}}^{1} \mathrm{d} y \int_{\arcsin y}^{\frac{\pi}{2}} f(x,y) \mathrm{d} x</equation>C.<equation>\int_{0}^{\frac{1}{2}} \mathrm{d} y \int_{\frac{\pi}{6}}^{\arcsin y} f(x,y) \mathrm{d} x</equation>D.<equation>\int_{0}^{\frac{1}{2}} \mathrm{d} y \int_{\arcsin y}^{\frac{\pi}{2}} f(x,y) \mathrm{d} x</equation>

答案: A

**解析:**解二次积分<equation>\int_{\frac{\pi}{6}}^{\frac{\pi}{2}} \mathrm{d} x \int_{\sin x}^{1} f(x,y)\mathrm{d} y</equation>对应的二重积分的积分区域为<equation>D = \left\{(x, y) \mid \sin x \leqslant y \leqslant 1, \frac {\pi}{6} \leqslant x \leqslant \frac {\pi}{2} \right\}.</equation>由于<equation>\arcsin y</equation>的值域为<equation>\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>，而<equation>\left[\frac{\pi}{6},\frac{\pi}{2}\right]\subset\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>，故曲线<equation>y=\sin x \left(x\in\left[\frac{\pi}{6},\frac{\pi}{2}\right]\right)</equation>上的点（x,y）可写为（<equation>\arcsin y,y).</equation>由此可将 D改写成Y型区域，<equation>D = \left\{(x, y) \mid \frac {\pi}{6} \leqslant x \leqslant \arcsin y, \frac {1}{2} \leqslant y \leqslant 1 \right\}.</equation>因此，<equation>\int_ {\frac {\pi}{6}} ^ {\frac {\pi}{2}} \mathrm {d} x \int_ {\sin x} ^ {1} f (x, y) \mathrm {d} y = \int_ {\frac {1}{2}} ^ {1} \mathrm {d} y \int_ {\frac {\pi}{6}} ^ {\arcsin y} f (x, y) \mathrm {d} x.</equation>应选A.

---

**2015年第3题 | 选择题 | 4分 | 答案: B**

3. 设<equation>D=\{(x,y)\mid x^{2}+y^{2}\leqslant 2x,x^{2}+y^{2}\leqslant 2y\}</equation>，函数 f(x,y)在 D上连续，则<equation>\iint_{D}f(x,y)\mathrm{d}x\mathrm{d}y=</equation>(    )

A.<equation>\int_{0}^{\frac{\pi}{4}}\mathrm{d}\theta \int_{0}^{2\cos \theta}f(r\cos \theta,r\sin \theta)r\mathrm{d}r+\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}\mathrm{d}\theta \int_{0}^{2\sin \theta}f(r\cos \theta,r\sin \theta)r\mathrm{d}r</equation>B.<equation>\int_{0}^{\frac{\pi}{4}}\mathrm{d}\theta \int_{0}^{2\sin \theta}f(r\cos \theta,r\sin \theta)r\mathrm{d}r+\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}\mathrm{d}\theta \int_{0}^{2\cos \theta}f(r\cos \theta,r\sin \theta)r\mathrm{d}r</equation>C.<equation>2\int_{0}^{1}\mathrm{d}x\int_{1-\sqrt{1-x^{2}}}^{x}f(x,y)\mathrm{d}y</equation>D.<equation>2\int_{0}^{1}\mathrm{d}x\int_{x}^{\sqrt{2x-x^{2}}}f(x,y)\mathrm{d}y</equation>

答案: B

**解析:**解 圆<equation>x^{2}+y^{2}=2x</equation>的极坐标方程为<equation>r=2\cos \theta</equation>，圆<equation>x^{2}+y^{2}=2y</equation>的极坐标方程为<equation>r=2\sin \theta.</equation>由图可知，当<equation>0\leqslant \theta \leqslant \frac{\pi}{4}</equation>时，D的边界为<equation>r=2\sin \theta</equation>；当<equation>\frac{\pi}{4}\leqslant \theta \leqslant \frac{\pi}{2}</equation>时，D的边界为<equation>r=2\cos \theta</equation>于是，<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2 \sin \theta , 0 \leqslant \theta \leqslant \frac {\pi}{4} \right\} \cup \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2 \cos \theta , \frac {\pi}{4} \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation>因此，<equation>\iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {\frac {\pi}{4}} \mathrm {d} \theta \int_ {0} ^ {2 \sin \theta} f (r \cos \theta , r \sin \theta) r \mathrm {d} r + \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {2 \cos \theta} f (r \cos \theta , r \sin \theta) r \mathrm {d} r.</equation>应选B.

由上述论证可知选项A不正确.

若在直角坐标系下计算，则区域 D 可表示为<equation>D = \left\{(x, y) \mid 1 - \sqrt {1 - x ^ {2}} \leqslant y \leqslant \sqrt {2 x - x ^ {2}}, 0 \leqslant x \leqslant 1 \right\}.</equation>于是，<equation>\iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {1 - \sqrt {1 - x ^ {2}}} ^ {\sqrt {2 x - x ^ {2}}} f (x, y) \mathrm {d} y.</equation>因此，选项C、D均不正确.
