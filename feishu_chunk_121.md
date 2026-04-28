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


