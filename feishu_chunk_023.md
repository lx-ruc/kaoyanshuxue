**解析:**解 （法一）利用导数的定义来求极限.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {x ^ {2} f (x) - 2 f \left(x ^ {3}\right)}{x ^ {3}} &= \lim _ {x \rightarrow 0} \left[ \frac {f (x)}{x} - \frac {2 f \left(x ^ {3}\right)}{x ^ {3}} \right] \xlongequal {f (0) = 0} \lim _ {x \rightarrow 0} \left[ \frac {f (x) - f (0)}{x - 0} - 2 \cdot \frac {f \left(x ^ {3}\right) - f (0)}{x ^ {3} - 0} \right] \\ &= \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0} - 2 \lim _ {x \rightarrow 0} \frac {f \left(x ^ {3}\right) - f (0)}{x ^ {3} - 0} = f ^ {\prime} (0) - 2 f ^ {\prime} (0) = - f ^ {\prime} (0). \end{aligned}</equation>应选B.

（法二）分别写出<equation>f(x)</equation>与<equation>f(x^{3})</equation>在<equation>x = 0</equation>处的一阶泰勒公式.<equation>f (x) = f (0) + f ^ {\prime} (0) x + o (x) \stackrel {f (0) = 0} {=} f ^ {\prime} (0) x + o (x),</equation><equation>f \left(x ^ {3}\right) = f (0) + f ^ {\prime} (0) x ^ {3} + o \left(x ^ {3}\right) \stackrel {f (0) = 0} {=} f ^ {\prime} (0) x ^ {3} + o \left(x ^ {3}\right).</equation>代入所求极限得<equation>\lim _ {x \rightarrow 0} \frac {x ^ {2} f (x) - 2 f \left(x ^ {3}\right)}{x ^ {3}} = \lim _ {x \rightarrow 0} \frac {f ^ {\prime} (0) x ^ {3} - 2 f ^ {\prime} (0) x ^ {3} + o \left(x ^ {3}\right)}{x ^ {3}} = - f ^ {\prime} (0).</equation>应选B.

---


#### 微分中值定理

**2025年第20题 | 解答题 | 12分**

20. 设函数 f(x)在区间（a,b）内可导，证明导函数<equation>f^{\prime}(x)</equation>在（a,b）内严格单调增加的充分必要条件是：对（a,b）内任意的<equation>x_{1},x_{2},x_{3}</equation>，当<equation>x_{1}<x_{2}<x_{3}</equation>时，<equation>\frac{f(x_{2})-f(x_{1})}{x_{2}-x_{1}}<\frac{f(x_{3})-f(x_{2})}{x_{3}-x_{2}}.</equation>

**解析:**证 先证明必要性.

对（a,b）内任意的<equation>x_{1}, x_{2}, x_{3}</equation>，当<equation>x_{1} < x_{2} < x_{3}</equation>时，由拉格朗日中值定理可得存在<equation>\xi_{1}\in(x_{1},x_{2})</equation><equation>\xi_{2}\in(x_{2},x_{3})</equation>，使得<equation>f^{\prime}(\xi_{1})=\frac{f(x_{2})-f(x_{1})}{x_{2}-x_{1}},f^{\prime}(\xi_{2})=\frac{f(x_{3})-f(x_{2})}{x_{3}-x_{2}}.</equation>由<equation>f^{\prime}(x)</equation>单调增加以及<equation>\xi_{1}<</equation><equation>\xi_{2}</equation>可得<equation>f^{\prime}(\xi_{1})<f^{\prime}(\xi_{2})</equation>即<equation>\frac{f(x_{2})-f(x_{1})}{x_{2}-x_{1}}<\frac{f(x_{3})-f(x_{2})}{x_{3}-x_{2}}.</equation>再证明充分性.

任取<equation>x_{0},x_{1},x_{2}\in(a,b)</equation>满足<equation>x_{1} < x_{0} < x_{2}</equation>，由已知条件可得<equation>\frac{f(x_0) - f(x_1)}{x_0 - x_1} < \frac{f(x_2) - f(x_0)}{x_2 - x_0}.</equation>取s,t满足<equation>x_{1} < s < x_{0} < t < x_{2}</equation>，由已知条件可得<equation>\frac {f (s) - f \left(x _ {1}\right)}{s - x _ {1}} < \frac {f \left(x _ {0}\right) - f (s)}{x _ {0} - s}, \quad \frac {f (t) - f \left(x _ {0}\right)}{t - x _ {0}} < \frac {f \left(x _ {2}\right) - f (t)}{x _ {2} - t}.</equation>在<equation>\frac{f(s) - f(x_1)}{s - x_1} < \frac{f(x_0) - f(s)}{x_0 - s}</equation>中令<equation>s\to x_1^+</equation>可得<equation>f ^ {\prime} \left(x _ {1}\right) = f _ {+} ^ {\prime} \left(x _ {1}\right) = \lim _ {s \rightarrow x _ {1} ^ {+}} \frac {f (s) - f \left(x _ {1}\right)}{s - x _ {1}} \leqslant \lim _ {s \rightarrow x _ {1} ^ {+}} \frac {f \left(x _ {0}\right) - f (s)}{x _ {0} - s} = \frac {f \left(x _ {0}\right) - f \left(x _ {1}\right)}{x _ {0} - x _ {1}}.</equation>在<equation>\frac{f(t) - f(x_0)}{t - x_0} < \frac{f(x_2) - f(t)}{x_2 - t}</equation>中令<equation>t\to x_2^{-}</equation>可行<equation>\frac {f \left(x _ {2}\right) - f \left(x _ {0}\right)}{x _ {2} - x _ {0}} = \lim _ {t \rightarrow x _ {2} ^ {-}} \frac {f (t) - f \left(x _ {0}\right)}{t - x _ {0}} \leqslant \lim _ {t \rightarrow x _ {2} ^ {-}} \frac {f \left(x _ {2}\right) - f (t)}{x _ {2} - t} = f _ {-} ^ {\prime} \left(x _ {2}\right) = f ^ {\prime} \left(x _ {2}\right).</equation>由(1)式，(2)式以及<equation>\frac{f(x_0) - f(x_1)}{x_0 - x_1} < \frac{f(x_2) - f(x_0)}{x_2 - x_0}</equation>可得<equation>f^{\prime}(x_{1}) < f^{\prime}(x_{2})</equation>由<equation>x_{1}, x_{2}</equation>的任意性可得<equation>f^{\prime}(x)</equation>在<equation>(a,b)</equation>内严格单调增加.

---

**2019年第19题 | 解答题 | 10分**

19. (本题满分10分)

设<equation>a_{n}=\int_{0}^{1} x^{n}\sqrt{1-x^{2}}\mathrm{d}x(n=0,1,2,\dots).</equation>I. 证明数列<equation>\{a_{n}\}</equation>单调递减，且<equation>a_{n}=\frac{n-1}{n+2} a_{n-2}(n=2,3,\cdots);</equation>II. 求<equation>\lim_{n\to\infty}\frac{a_{n}}{a_{n-1}}.</equation>

**答案:**（I）证明略；（Ⅱ）<equation>\lim_{n\to \infty}\frac{a_{n}}{a_{n-1}}=1.</equation>

**解析:**解（I）考虑<equation>a_{n+1}-a_{n}</equation>. 由于在（0，1）内，<equation>x^{n+1}-x^{n}<0,\sqrt{1-x^{2}}>0</equation>，故由定积分的保号性可知，<equation>a _ {n + 1} - a _ {n} = \int_ {0} ^ {1} \left(x ^ {n + 1} - x ^ {n}\right) \sqrt {1 - x ^ {2}} \mathrm {d} x < 0.</equation>因此，<equation>\{a_{n}\}</equation>单调递减.

下面用两种方法证明<equation>a_{n} = \frac{n - 1}{n + 2} a_{n - 2} (n = 2,3,\dots).</equation>（法一）先三角换元，再分部积分.

令<equation>x=\sin t</equation>，则<equation>\mathrm{d}x=\cos t\mathrm{d}t.</equation><equation>\begin{aligned} a _ {n} &= \int_ {0} ^ {1} x ^ {n} \sqrt {1 - x ^ {2}} \mathrm {d} x \xlongequal {x = \sin t} \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \cos t \cdot \cos t \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \cos^ {2} t \mathrm {d} t \\ &= \int_ {0} ^ {\frac {\pi}{2}} \left(\sin^ {n} t - \sin^ {n + 2} t\right) \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t + \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n + 1} t \mathrm {d} (\cos t) \\ &= \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t + \sin^ {n + 1} t \cos t \left| _ {0} ^ {\frac {\pi}{2}} - \int_ {0} ^ {\frac {\pi}{2}} \cos t \cdot (n + 1) \sin^ {n} t \cdot \cos t \mathrm {d} t \right. \\ &= \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t - (n + 1) \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \cos^ {2} t \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t - (n + 1) a _ {n}. \end{aligned}</equation>由上可得，<equation>(n + 2)a_{n} = \int_{0}^{\frac{\pi}{2}}\sin^{n}t\mathrm{d}t.</equation>另一方面，<equation>\begin{aligned} \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t &= - \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n - 1} t \mathrm {d} (\cos t) = - \left[ \sin^ {n - 1} t \cos t \Big | _ {0} ^ {\frac {\pi}{2}} - \int_ {0} ^ {\frac {\pi}{2}} \cos t \cdot (n - 1) \sin^ {n - 2} t \cdot \cos t \mathrm {d} t \right] \\ &= (n - 1) \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n - 2} t \cos^ {2} t \mathrm {d} t = (n - 1) a _ {n - 2}. \end{aligned}</equation>因此，<equation>( n+2) a_{n}=( n-1) a_{n-2}</equation>，即<equation>a_{n}=\frac{n-1}{n+2} a_{n-2}( n=2,3,\dots).</equation>（法二）直接分部积分.注意到<equation>[（1-x^{2})^{\frac{3}{2}}]^{\prime}=-3x\sqrt{1-x^{2}}</equation>，故<equation>\begin{array}{l} a _ {n} = \int_ {0} ^ {1} x ^ {n} \sqrt {1 - x ^ {2}} \mathrm {d} x = - \frac {1}{3} \int_ {0} ^ {1} x ^ {n - 1} \mathrm {d} \left(1 - x ^ {2}\right) ^ {\frac {3}{2}} \\ = - \frac {1}{3} \left\{\left[ x ^ {n - 1} \left(1 - x ^ {2}\right) ^ {\frac {3}{2}} \right] \Bigg | _ {0} ^ {1} - \int_ {0} ^ {1} \left(1 - x ^ {2}\right) ^ {\frac {3}{2}} \cdot (n - 1) x ^ {n - 2} \mathrm {d} x \right\} \\ = \frac {n - 1}{3} \int_ {0} ^ {1} \left(1 - x ^ {2}\right) \sqrt {1 - x ^ {2}} x ^ {n - 2} \mathrm {d} x = \frac {n - 1}{3} \int_ {0} ^ {1} \left(x ^ {n - 2} - x ^ {n}\right) \sqrt {1 - x ^ {2}} \mathrm {d} x \\ = \frac {n - 1}{3} \left(\int_ {0} ^ {1} x ^ {n - 2} \sqrt {1 - x ^ {2}} \mathrm {d} x - \int_ {0} ^ {1} x ^ {n} \sqrt {1 - x ^ {2}} \mathrm {d} x\right) \\ = \frac {n - 1}{3} \left(a _ {n - 2} - a _ {n}\right). \\ \end{array}</equation>因此，<equation>a_{n} = \frac{n - 1}{n + 2} a_{n - 2} (n = 2,3,\dots).</equation>（Ⅱ）由第（Ⅰ）问可知<equation>\left\{a_{n}\right\}</equation>单调递减，故<equation>a_{n} < a_{n-1} < a_{n-2}</equation>. 又由<equation>a_{n}</equation>的表达式可知<equation>a_{n} > 0 (n= 0,1,\cdots)</equation>，故<equation>\frac {n - 1}{n + 2} = \frac {a _ {n}}{a _ {n - 2}} < \frac {a _ {n}}{a _ {n - 1}} < \frac {a _ {n}}{a _ {n}} = 1.</equation>对（1）式中各项同时取极限，令<equation>n\to\infty</equation>，可得<equation>1 = \lim _ {n \rightarrow \infty} \frac {n - 1}{n + 2} \leqslant \lim _ {n \rightarrow \infty} \frac {a _ {n}}{a _ {n - 1}} \leqslant 1.</equation>由夹逼准则可知，<equation>\lim_{n\to \infty}\frac{a_n}{a_{n - 1}} = 1.</equation>

---

**2013年第19题 | 解答题 | 10分**

19. (本题满分10分)

设函数 f(x)在<equation>[0,+\infty)</equation>上可导，<equation>f(0)=0</equation>且<equation>\lim_{x\rightarrow+\infty}f(x)=2.</equation>证明：

I. 存在 a > 0，使得 f(a)=1;

II. 对第一问中的 a，存在<equation>\xi\in(0,a)</equation>，使得<equation>f^{\prime}(\xi)=\frac{1}{a}.</equation>

**答案:**（19）（I）证明略；

（Ⅱ）证明略.

**解析:**证（I）由<equation>\lim_{x\to +\infty}f(x)=2 > \frac{3}{2}</equation>以及极限的局部保号性知，存在 M > 0，使得当 x≥M时，<equation>f(x) > \frac{3}{2}</equation>，从而<equation>f(M) > \frac{3}{2} > 1 > 0 = f(0).</equation>又由于<equation>f ( x )</equation>在<equation>[ 0,M]</equation>上可导，从而连续，故由连续函数的介值定理知，存在<equation>0 < a < M</equation>，使得<equation>f ( a )=1.</equation>（Ⅱ）（法一）由于 f(x)在[0,a]上可导，故由拉格朗日中值定理知存在<equation>\xi\in(0,a)</equation>，使得 f(a）<equation>- f(0)=1-0=f^{\prime}(\xi)a</equation>，即<equation>f^{\prime}(\xi)=\frac{1}{a}.</equation>（法二）令<equation>F ( x )=f ( x )-\frac{1}{a} x</equation>，则<equation>F ( a )=f ( a )-1=0</equation>.又由于<equation>F ( 0 )=f ( 0 )-0=0</equation>，且<equation>F ( x )</equation>在<equation>[ 0,a ]</equation>上可导，故由罗尔定理可知，存在<equation>\xi\in(0,a)</equation>，使得<equation>F^{\prime}(\xi)=0</equation>，即<equation>f^{\prime}(\xi)=\frac{1}{a}.</equation>

---

**2010年第19题 | 解答题 | 10分**

19. (本题满分10分)

设函数 f(x)在[0,3]上连续，在(0,3)内存在二阶导数，且<equation>2 f ( 0 )=\int_{0}^{2} f ( x ) \mathrm{d} x=f ( 2 )+f ( 3 )</equation>.

I. 证明存在<equation>\eta \in(0,2)</equation>，使<equation>f(\eta)=f(0);</equation>II. 证明存在<equation>\xi \in(0,3)</equation>，使<equation>f^{\prime \prime}(\xi)=0.</equation>

**答案:**## （19）（I）证明略；（Ⅱ）证明略.

**解析:**证（I）（法一）设<equation>F ( x )=\int_{0}^{x} f ( t ) \mathrm{d} t, 0 \leqslant x \leqslant 2</equation>，则<equation>2 f ( 0 )=\int_{0}^{2} f ( x ) \mathrm{d} x=F ( 2 )-F ( 0 ) \frac{\mathrm{拉格朗日}}{\mathrm{中值定理}} 2 F^{\prime} (\eta)=2 f (\eta), \eta \in(0,2),</equation>即存在<equation>\eta \in(0,2)</equation>，使得<equation>f ( 0 )=f (\eta).</equation>（法二）假设不存在<equation>\eta\in(0,2)</equation>，使得<equation>f(\eta)=f(0)</equation>，则由连续函数的介值定理可知，<equation>f(x)-f(0)</equation>在 （0,2）上恒大于零或者恒小于零，从而积分值<equation>\int_{0}^{2}[f(x)-f(0)]\mathrm{d}x</equation>大于零或者小于零.

另一方面，由题设知，<equation>0 = \int_ {0} ^ {2} f (x) \mathrm {d} x - 2 f (0) = \int_ {0} ^ {2} \left[ f (x) - f (0) \right] \mathrm {d} x.</equation>这与<equation>\int_{0}^{2}[f(x)-f(0)]\mathrm{d}x>0</equation>或<equation>\int_{0}^{2}[f(x)-f(0)]\mathrm{d}x<0</equation>矛盾，故假设不成立，即存在<equation>\eta \in(0,2)</equation>使得<equation>f(\eta)=f(0).</equation>（Ⅱ）（法一）若<equation>f(2) = f(0)</equation>，则由<equation>2 f(0) = f(2) + f(3)</equation>知<equation>f(3) = f(0)</equation>，从而<equation>f(0) = f(2) = f(3).</equation>在区间[0,2],[2,3]上分别使用罗尔定理可知，存在<equation>\eta_{1}\in(0,2),\eta_{2}\in(2,3)</equation>，使得<equation>f^{\prime}(\eta_{1})= f^{\prime}(\eta_{2})=0.</equation>由于<equation>0 < \eta_{1} < 2 < \eta_{2} < 3</equation>，且<equation>f(x)</equation>在<equation>[\eta_{1},\eta_{2}]</equation>上二阶可导，故<equation>f^{\prime}(x)</equation>在<equation>[\eta_{1},\eta_{2}]</equation>上可导，从而由罗尔定理可知存在<equation>\xi \in(\eta_{1},\eta_{2})\subseteq(0,3)</equation>，使得<equation>f^{\prime\prime}(\xi)=0.</equation>若<equation>f ( 2 ) \neq f ( 0 )</equation>，不妨设<equation>f ( 2 ) > f ( 0 )</equation>，则<equation>f ( 3 ) < f ( 0 )</equation>.由连续函数的介值定理知存在<equation>\theta \in</equation>(2,3)，使得<equation>f (\theta)=f(0)</equation>.于是由第（I）问的结论有<equation>f ( 0 )=f (\eta)=f (\theta)</equation><equation>0 < \eta < 2 < \theta < 3.</equation>对区间<equation>[0,\eta ],[\eta ,\theta]</equation>上的<equation>f(x)</equation>分别使用罗尔定理可知，存在<equation>\xi_{1}\in (0,\eta),\xi_{2}\in (\eta ,\theta)</equation>，使得<equation>f^{\prime}(\xi_{1}) = f^{\prime}(\xi_{2}) = 0.</equation>由于<equation>0 < \xi_{1} < \eta < \xi_{2} < \theta</equation>，且<equation>f(x)</equation>在<equation>[\xi_{1},\xi_{2}]</equation>上二阶可导，故<equation>f^{\prime}(x)</equation>在<equation>[\xi_{1},\xi_{2}]</equation>上可导，从而由罗尔定理可知存在<equation>\xi \in (\xi_{1},\xi_{2})\subseteq (0,3)</equation>，使得<equation>f^{\prime \prime}(\xi) = 0.</equation><equation>f ( 2 ) < f ( 0 )</equation><equation>f ( 3 ) > f ( 0 )</equation>时同理可证.

综上所述，存在<equation>\xi \in (0,3)</equation>，使得<equation>f^{\prime \prime}(\xi) = 0.</equation>（法二）由于<equation>\min \{ f(2), f(3)\} \leqslant \frac{f(2)+f(3)}{2}\leqslant \max \{ f(2), f(3)\}</equation>，故由介值定理知存在 a<equation>\in</equation>[2,3]，使得<equation>f(a)=\frac{f(2)+f(3)}{2}=f(0).</equation>于是由第（I）问的结论知<equation>f (0) = f (\eta) = f (a), 0 < \eta < 2 \leqslant a \leqslant 3.</equation>对区间<equation>[0,\eta ],[\eta ,a]</equation>上的<equation>f(x)</equation>分别使用罗尔定理可知，存在<equation>\xi_{1}\in (0,\eta),\xi_{2}\in (\eta ,a)</equation>，使得<equation>f^{\prime}(\xi_{1}) = f^{\prime}(\xi_{2}) = 0.</equation>由于<equation>0 < \xi_{1} < \eta < \xi_{2} < a\leqslant 3,f(x)</equation>在<equation>[\xi_{1},\xi_{2}]</equation>上二阶可导，从而<equation>f^{\prime}(x)</equation>在<equation>[\xi_{1},\xi_{2}]</equation>上可导，故由罗尔定理可知存在<equation>\xi \in (\xi_{1},\xi_{2})\subseteq (0,3)</equation>，使得<equation>f^{\prime \prime}(\xi) = 0.</equation>

---

**2009年第18题 | 解答题 | 10分**

18. (本题满分11分)

I. 证明拉格朗日中值定理：若函数 f(x)在<equation>[a,b]</equation>上连续，在（a,b）内可导，则存在<equation>\xi\in(a,b)</equation>，使得<equation>f(b)-f(a)=f^{\prime}(\xi)(b-a).</equation>II. 证明：若函数 f(x)在 x=0处连续，在<equation>(0,\delta)(\delta>0)</equation>内可导，且<equation>\lim_{x\to 0^{+}}f^{\prime}(x)=A</equation>，则<equation>f_{+}^{\prime}(0)</equation>存在，且<equation>f_{+}^{\prime}(0)=A.</equation>

**答案:**## （18）（I）证明略；（Ⅱ）证明略.

**解析:**证（ I ）令<equation>\varphi (x) = f (x) - f (a) - \frac {f (b) - f (a)}{b - a} (x - a).</equation><equation>\varphi (x)</equation>在<equation>[a,b]</equation>上连续，在<equation>(a,b)</equation>内可导.计算得<equation>\varphi (a) = 0,\varphi (b) = 0.</equation>对<equation>\varphi(x)</equation>使用罗尔定理得，存在<equation>\xi\in(a,b)</equation>，使得<equation>\varphi^{\prime}(\xi)=0</equation>，即<equation>f^{\prime}(\xi)-\frac{f(b)-f(a)}{b-a}=0.</equation>因此，存在<equation>\xi\in(a,b)</equation>，使得<equation>f(b)-f(a)=f^{\prime}(\xi)(b-a).</equation>（Ⅱ）（法一）根据右侧导数的定义，<equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x}.</equation>任取<equation>x\in (0,\delta)</equation>，由题设知，<equation>f(x)</equation>在<equation>[0,x]</equation>上连续，在（0,x）内可导.由拉格朗日中值定理知，存在<equation>\xi_{x}\in (0,x)</equation>，使得<equation>f (x) - f (0) = f ^ {\prime} \left(\xi_ {x}\right) x.</equation>从而<equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x} = \lim _ {x \rightarrow 0 ^ {+}} \frac {f ^ {\prime} \left(\xi_ {x}\right) x}{x} = \lim _ {0 < \xi_ {x} < x, \atop x \rightarrow 0 ^ {+}} f ^ {\prime} \left(\xi_ {x}\right).</equation>由于<equation>x\to 0^{+}</equation>，故<equation>\xi_{x}\rightarrow 0^{+}</equation>.因此，<equation>f _ {+} ^ {\prime} (0) = \lim _ {0 < \xi_ {x} < x, \atop x \rightarrow 0 ^ {+}} f ^ {\prime} \left(\xi_ {x}\right) = \lim _ {x \rightarrow 0 ^ {+}} f ^ {\prime} (x) = A.</equation>（法二）由洛必达法则，<equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x} \xlongequal {\text {洛 必达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {f ^ {\prime} (x)}{1} = A.</equation>因此，<equation>f_{+}^{\prime}(0)</equation>存在，且等于A.

---


#### 微分学在经济学中的应用

**2024年第14题 | 填空题 | 5分**

14. 某产品的价格函数为<equation>p=\left\{\begin{array}{l l}2 5-0. 2 5 Q,&Q \leqslant 2 0,\\ 3 5-0. 7 5 Q,&Q>2 0\end{array}\right.</equation>（p为单价，单位：万元；Q为产量，单位：件），总成本函数为<equation>C=1 5 0+5 Q+0. 2 5 Q^{2}</equation>（万元），则经营该产品可获得的最大利润为___(万元).

**答案:**## 50

**解析:**解 由于利润 = 收益-成本，故当<equation>Q\leqslant 2 0</equation>时，利润函数<equation>L ( Q ) = p Q - C ( Q ) = ( 2 5 - 0. 2 5 Q ) Q - 1 5 0 - 5 Q - 0. 2 5 Q^{2} = - 0. 5 Q^{2} + 2 0 Q - 1 5 0</equation>当<equation>Q > 2 0</equation>时，<equation>L (Q) = p Q - C (Q) = (3 5 - 0. 7 5 Q) Q - 1 5 0 - 5 Q - 0. 2 5 Q ^ {2} = - Q ^ {2} + 3 0 Q - 1 5 0.</equation>于是，<equation>L ( Q ) = \left\{ \begin{array}{ll} - 0. 5 Q^{2} + 2 0 Q - 1 5 0, & Q \leqslant 2 0, \\ - Q^{2} + 3 0 Q - 1 5 0, & Q > 2 0. \end{array} \right.</equation>由于<equation>\lim_{Q\to 20^{-}} L ( Q ) = \lim_{Q\to 20^{+}} L ( Q ) = L ( 2 0 ) = 5 0</equation>，故

L（Q）在分界点<equation>Q=2 0</equation>处连续，从而是连续函数.

又因为当 Q < 20时，<equation>L^{\prime}(Q)=-Q+20>0,L(Q)</equation>单调增加，当 Q > 20时，<equation>L^{\prime}(Q)=-2Q+ 30<0,L(Q)</equation>单调减少，所以 Q = 20是 L（Q）的极大值点，也是最大值点.因此，最大利润为 L（20）= 50（万元）.

---

**2022年第18题 | 解答题 | 12分**

18. (本题满分12分）

设某产品的产量 Q由资本投入量 x和劳动投入量 y决定，生产函数<equation>Q=1 2 x^{\frac{1}{2}} y^{\frac{1}{6}}</equation>，该产品的销售单价 p与产量 Q的关系为<equation>p=1 1 6 0-1. 5 Q</equation>.若单位资本投入和单位劳动投入的价格分别为6和8，求利润最大时的产量.

**答案:**## 利润最大时的产量 Q=384.

**解析:**根据已知条件，该产品的成本函数为 C（x,y）=6x+8y，收益函数为<equation>R ( x,y)=p Q=(1160-1.5 Q) Q=(1160-18 x^{\frac{1}{2}} y^{\frac{1}{6}})\cdot 1 2 x^{\frac{1}{2}} y^{\frac{1}{6}}=1 3 9 2 0 x^{\frac{1}{2}} y^{\frac{1}{6}}-2 1 6 x y^{\frac{1}{3}},</equation>故利润函数为<equation>L (x, y) = R (x, y) - C (x, y) = 1 3 9 2 0 x ^ {\frac {1}{2}} y ^ {\frac {1}{6}} - 2 1 6 x y ^ {\frac {1}{3}} - 6 x - 8 y.</equation>分别计算 L（x,y）关于 x和 y的偏导数.<equation>\left\{ \begin{array}{l} L _ {x} ^ {\prime} (x, y) = 6 9 6 0 x ^ {- \frac {1}{2}} y ^ {\frac {1}{6}} - 2 1 6 y ^ {\frac {1}{3}} - 6 = \frac {3 \left(2 3 2 0 x ^ {\frac {1}{2}} y ^ {\frac {1}{6}} - 7 2 x y ^ {\frac {1}{3}}\right)}{x} - 6, \\ L _ {y} ^ {\prime} (x, y) = 2 3 2 0 x ^ {\frac {1}{2}} y ^ {- \frac {5}{6}} - 7 2 x y ^ {- \frac {2}{3}} - 8 = \frac {2 3 2 0 x ^ {\frac {1}{2}} y ^ {\frac {1}{6}} - 7 2 x y ^ {\frac {1}{3}}}{y} - 8. \end{array} \right.</equation>令<equation>\left\{\begin{array}{l l}L_{x}^{\prime}(x,y)=0,\\ L_{y}^{\prime}(x,y)=0,\end{array} \right.</equation>可得<equation>\left\{\begin{array}{l l}2320x^{\frac{1}{2}}y^{\frac{1}{6}}-72xy^{\frac{1}{3}}=2x,\\ 2320x^{\frac{1}{2}}y^{\frac{1}{6}}-72xy^{\frac{1}{3}}=8y.\end{array} \right.</equation>于是，<equation>x=4y</equation>进一步，将 x=4y 代入 2<equation>3 2 0 x^{\frac{1}{2}} y^{\frac{1}{6}}-7 2 x y^{\frac{1}{3}}=8 y</equation>即<equation>2 9 0 x^{\frac{1}{2}} y^{\frac{1}{6}}-9 x y^{\frac{1}{3}}=y</equation>可得，<equation>5 8 0 y^{\frac{2}{3}}-3 6 y^{\frac{4}{3}}=y.</equation>等式两端同时除 y 可得<equation>5 8 0 y^{-\frac{1}{3}}-3 6 y^{\frac{1}{3}}=1.</equation>(1)

令<equation>z=y^{\frac{1}{3}}</equation>，则（1）式可整理为<equation>3 6 z^{2}+z-5 8 0=0</equation>.由求根公式可得<equation>z=\frac{-1\pm \sqrt{1+4\times 3 6\times 5 8 0}}{7 2}</equation>解得<equation>z=4</equation>或<equation>z=-\frac{1 4 5}{3 6}</equation>（舍去）.于是，<equation>y=z^{3}=6 4,x=4 y=2 5 6,L(x,y)</equation>的唯一驻点为（256，64）.

由问题的实际意义可知，最大利润必定存在，故最大利润在驻点（256，64）处取得。此时，<equation>Q= 1 2 \times\sqrt{2 5 6} \times\sqrt[6]{6 4}=1 2 \times1 6 \times2=3 8 4.</equation>因此，当利润最大时，产量<equation>Q=3 8 4.</equation>

---

**2020年第11题 | 填空题 | 4分**

11. 设某厂家生产某产品的产量为 Q，成本<equation>C(Q)=1 0 0+1 3 Q</equation>，该产品的单价为 p，需求量<equation>q ( p )=\frac{8 0 0}{p+3}-2</equation>，则该厂家获得最大利润时的产量为 ___.

**解析:**解 根据经济学的含义，获得最大利润时，应满足产销平衡，即需求量等于产量。由需求量与价格的关系，将价格 p写成需求量 q的函数，进而将利润写成需求量 q的函数.

由<equation>q ( p )=\frac{8 0 0}{p+3}-2</equation>可得<equation>p ( q )=\frac{8 0 0}{q+2}-3.</equation>由利润 = 价格<equation>\times</equation>需求-成本可得，<equation>L (q) = p (q) q - C (q) = \left(\frac {8 0 0}{q + 2} - 3\right) q - 1 3 q - 1 0 0.</equation><equation>L ^ {\prime} (q) = \frac {8 0 0}{q + 2} - 3 + q \cdot \left[ - \frac {8 0 0}{(q + 2) ^ {2}} \right] - 1 3 = \frac {1 6 0 0 - 1 6 (q + 2) ^ {2}}{(q + 2) ^ {2}}.</equation>令<equation>L^{\prime}(q)=0</equation>，可得<equation>(q+2)^{2}=100</equation>.由 q>0可得 q=8.当 0 < q < 8时，<equation>L^{\prime}(q)>0,L(q)</equation>单调增加；当 q>8时，<equation>L^{\prime}(q)<0,L(q)</equation>单调减少.因此， q=8为 L(q) 的最大值点，当 q=8时， L(q) 最大.因此，获得最大利润时的产量 Q=8.

---

**2019年第12题 | 填空题 | 4分**

12. 以<equation>P_{\mathrm{A}}, P_{\mathrm{B}}</equation>分别表示 A，B两个商品的价格，设商品 A的需求函数<equation>Q_{\mathrm{A}}=5 0 0-P_{\mathrm{A}}^{2}-P_{\mathrm{A}} P_{\mathrm{B}}+2 P_{\mathrm{B}}^{2}</equation>，则当<equation>P_{\mathrm{A}}= 1 0, P_{\mathrm{B}}=2 0</equation>时，商品 A的需求量对自身价格的弹性<equation>\eta_{\mathrm{A A}}(\eta_{\mathrm{A A}}>0)=</equation>___

**解析:**解<equation>Q_{\mathrm{A}}</equation>可看作关于<equation>P_{\mathrm{A}}</equation>、<equation>P_{\mathrm{B}}</equation>的二元函数，则商品A对自身价格的需求弹性<equation>\eta_ {\mathrm {A A}} = - \frac {P _ {\mathrm {A}}}{Q _ {\mathrm {A}}} \cdot \frac {\partial Q _ {\mathrm {A}}}{\partial P _ {\mathrm {A}}} = - \frac {P _ {\mathrm {A}}}{Q _ {\mathrm {A}}} \cdot \left(- 2 P _ {\mathrm {A}} - P _ {\mathrm {B}}\right).</equation>代入<equation>P_{\mathrm{A}}=10</equation><equation>P_{\mathrm{B}}=20</equation>，可得<equation>\eta_ {\mathrm {A A}} = - \frac {1 0}{5 0 0 - 1 0 0 - 2 0 0 + 8 0 0} \times (- 2 0 - 2 0) = 0. 4.</equation>

---

**2018年第4题 | 选择题 | 4分 | 答案: D**

4. 设某产品的成本函数 C(Q)可导，其中Q为产量.若产量为<equation>Q_{0}</equation>时平均成本最小，则（    )

A.<equation>C^{\prime}(Q_{0})=0</equation>B.<equation>C^{\prime}(Q_{0})=C(Q_{0})</equation>C.<equation>C^{\prime}(Q_{0})=Q_{0}C(Q_{0})</equation>D.<equation>Q_{0}C^{\prime}(Q_{0})=C(Q_{0})</equation>

答案: D

**解析:**由于<equation>\overline{C} ( Q )=\frac{C ( Q )}{Q}</equation>，故<equation>\bar {C} ^ {\prime} (Q) = \frac {Q C ^ {\prime} (Q) - C (Q)}{Q ^ {2}}.</equation>又因为当<equation>Q=Q_{0}</equation>时，平均成本最小，所以<equation>\overline{{C}}^{\prime}(Q_{0})=0</equation>即<equation>Q_{0}C^{\prime}(Q_{0})-C(Q_{0})=0</equation>也即<equation>Q_{0}C^{\prime}(Q_{0})=C(Q_{0}).</equation>因此，应选D.

---

**2017年第11题 | 填空题 | 4分**

11. 设生产某产品的平均成本为<equation>\bar{C} (Q)=1+\mathrm{e}^{-Q}</equation>, 其中产量为<equation>Q</equation>, 则边际成本为 ___

**答案:**<equation>1 + \mathrm {e} ^ {- Q} - Q \mathrm {e} ^ {- Q}.</equation>

**解析:**解 根据题意，总成本<equation>C ( Q ) = ( 1 + \mathrm{e}^{- Q} ) Q</equation>因此，边际成本<equation>C^{\prime} ( Q ) = 1 + \mathrm{e}^{- Q} - Q \mathrm{e}^{- Q}.</equation>

---

**2016年第16题 | 解答题 | 10分**

16. (本题满分10分)

设某商品的最大需求量为1200件，该商品的需求函数<equation>Q=Q(p)</equation>，需求弹性<equation>\eta=\frac{p}{120-p}</equation><equation>(\eta>0)</equation>，p为单价（万元）.

I. 求需求函数的表达式；

II. 求 p=100万元时的边际收益，并说明其经济意义.

**答案:**（I）<equation>Q ( p )=1 2 0 0-1 0 p.</equation>（Ⅱ）当 p=100万元时，边际收益为80万元.其经济意义为，当 p=100万元，Q=200件时，销售第201件商品所得的收益为80万元.

**解析:**解（I）由需求弹性的定义知，<equation>\eta=-Q^{\prime}(p)\frac{p}{Q(p)}.</equation>由题设知，<equation>\eta=\frac{p}{120-p}>0</equation>即 0 < p < 120.于是，<equation>- Q ^ {\prime} (p) \frac {p}{Q (p)} = \frac {p}{1 2 0 - p}, \quad 0 < p < 1 2 0.</equation>整理得<equation>\frac {Q ^ {\prime} (p)}{Q (p)} = \frac {- 1}{1 2 0 - p}, \quad 0 < p < 1 2 0.</equation>对上式两端求不定积分可得<equation>\ln[Q(p)]=\ln(120-p)+C</equation>，其中C为待定常数.从而，<equation>Q (p) = C _ {1} (1 2 0 - p), \quad C _ {1} = \mathrm {e} ^ {c}, \quad 0 < p < 1 2 0.</equation>又由题设知，<equation>1\ 200=Q(0)=\lim_{p\to 0}Q(p)=120C_{1}</equation>，解得<equation>C_{1}=10</equation>因此，需求函数的表达式为<equation>Q(p)=1\ 200-10p.</equation>（Ⅱ）由第（Ⅰ）问可知，<equation>p=\frac{1200-Q}{10}</equation>，故收益函数<equation>R(Q)=pQ=\frac{(1200-Q)Q}{10}=\frac{1200Q-Q^{2}}{10}.</equation>于是，该商品的边际收益为<equation>\frac {\mathrm {d} R}{\mathrm {d} Q} = \frac {1 2 0 0 - 2 Q}{1 0} = \frac {6 0 0 - Q}{5}.</equation>当 p=100时，<equation>Q=200</equation>因此，此时的边际收益为<equation>\left.\frac{\mathrm{d}R}{\mathrm{d}Q}\right|_{Q=200}=\frac{600-200}{5}=80.</equation>综上所述，当 p=100万元时，边际收益为80万元.其经济意义为，当 p=100万元，Q=200件时，销售第201件商品所得的收益为80万元.

---

**2015年第17题 | 解答题 | 10分**


为了实现利润最大化，厂商需要对某商品确定其定价模型.设Q为该商品的需求量，p为价格，MC为边际成本，<equation>\eta</equation>为需求弹性（<equation>\eta >0</equation>）.

I. 证明定价模型为<equation>p=\frac{MC}{1-\frac{1}{\eta}};</equation>II. 若该商品的成本函数为<equation>C ( Q )=1 6 0 0+Q^{2}</equation>，需求函数为<equation>Q=4 0-p</equation>，试由第一问中的定价模型确定此商品的价格.

**解析:**解（I）利润函数<equation>L ( Q )=R ( Q )-C ( Q )=Q p-C ( Q )</equation>，其中R（Q）为总收益函数，C（Q）为总成本函数，于是<equation>L ^ {\prime} (Q) = p + Q \frac {\mathrm {d} p}{\mathrm {d} Q} - \frac {\mathrm {d} [ C (Q) ]}{\mathrm {d} Q} = p + Q \frac {\mathrm {d} p}{\mathrm {d} Q} - M C.</equation>又由需求弹性的定义知<equation>\eta=-\frac{\mathrm{d} Q}{\mathrm{d} p}\cdot \frac{p}{Q}</equation>，故<equation>\frac{\mathrm{d} p}{\mathrm{d} Q}=-\frac{p}{Q\eta}.</equation>从而，<equation>L ^ {\prime} (Q) = p - \frac {p}{\eta} - M C = p \left(1 - \frac {1}{\eta}\right) - M C.</equation>当 L(Q) 取得最大值时，<equation>L^{\prime}(Q)=0</equation>，即<equation>p=\frac{MC}{1-\frac{1}{\eta}}.</equation>因此，为了实现利润最大化，定价模型应设为<equation>p=\frac{MC}{1-\frac{1}{\eta}}.</equation>（Ⅱ）由题设知，边际成本<equation>MC=C^{\prime}(Q)=2 Q=8 0-2 p</equation><equation>\eta=-\frac{\mathrm{d} Q}{\mathrm{d} p}\cdot \frac{p}{Q}=\frac{p}{4 0-p}.</equation>代入第（I）问所得定价模型可得<equation>p = \frac {8 0 - 2 p}{1 - \frac {4 0 - p}{p}}.</equation>解得<equation>p = 30.</equation>因此，所求商品的价格为30.

---

**2014年第9题 | 填空题 | 4分**

9. 设某商品的需求函数为<equation>Q=40-2P</equation>(P为商品的价格),则该商品的边际收益为 ___

**解析:**解 由题设知，价格函数<equation>P=\frac{4 0-Q}{2}</equation>，故该商品的总收益函数<equation>R(Q)=P Q=\frac{4 0-Q}{2} \cdot Q= 2 0 Q-\frac{Q^{2}}{2}.</equation>因此，该商品的边际收益为<equation>R^{\prime}(Q)=2 0-Q.</equation>

---

**2013年第18题 | 解答题 | 10分**


8. (本题满分10分)

设生产某商品的固定成本为60000元，可变成本为20元/件，价格函数为<equation>p=60-\frac{Q}{1000}</equation>（ p是单价，单位：元；

Q是销量，单位：件）. 已知产销平衡，求：

I. 该商品的边际利润；

II. 当 p=50时的边际利润，并解释其经济意义；

III. 使得利润最大的定价 p.

**答案:**(18) （I）<equation>L^{\prime}(Q)=40-\frac{Q}{500}.</equation>（Ⅱ）当 p=50时，边际利润为20.其经济意义为，当 p=50时，销售第10001件商品时所得的利润为20元.

（Ⅲ）当定价为40元时，利润最大.

**解析:**解（I）由于该商品的成本函数为<equation>C ( Q )=6 0\ 0 0 0+2 0 Q</equation>，收益函数为<equation>R ( Q )=p Q=6 0 Q-\frac{Q^{2}}{1\ 0 0 0}</equation>，故利润函数为<equation>L (Q) = R (Q) - C (Q) = 4 0 Q - \frac {Q ^ {2}}{1 0 0 0} - 6 0 0 0 0.</equation>因此，该商品的边际利润为<equation>L^{\prime}(Q)=40-\frac{Q}{500}.</equation>（Ⅱ）当 p=50时，<equation>Q=1 0 0 0 0</equation>，此时边际利润为<equation>L^{\prime}(Q)\bigg|_{1 0 0 0 0}=4 0-\frac{Q}{5 0 0}\bigg|_{1 0 0 0 0}=2 0.</equation>其经济意义为，当 p=50时，销售第10001件商品时所得的利润为20元.

（Ⅲ）令<equation>L^{\prime}(Q)=0</equation>，解得<equation>Q=20000</equation>.又由于<equation>L^{\prime\prime}(20000)=-\frac{1}{500}<0</equation>，故当<equation>Q=20000</equation>时，L（Q）取得最大值，此时<equation>p=60-\frac{Q}{1000}=40.</equation>因此，当定价为40元时，利润最大.

---

**2010年第11题 | 填空题 | 4分**

11. 设某商品的收益函数为<equation>R(p)</equation>,收益弹性为<equation>1+p^{3}</equation>,其中<equation>p</equation>为价格,且<equation>R(1)=1</equation>,则<equation>R(p)=</equation>___.

**答案:**<equation>p e ^ {\frac {p ^ {3} - 1}{3}}.</equation>

**解析:**由收益弹性的定义及题设可知<equation>\frac {p}{R (p)} R ^ {\prime} (p) = 1 + p ^ {3}.</equation>此为可分离变量的微分方程. 分离变量得，<equation>\frac {\mathrm {d} R}{R} = \left(\frac {1}{p} + p ^ {2}\right) \mathrm {d} p.</equation>方程两端积分可得<equation>\ln R=\ln p+\frac{p^{3}}{3}+C</equation>，其中C为待定常数.于是<equation>R(p)=p\mathrm{e}^{\frac{p^{3}}{3}+C}.</equation>将<equation>R(1)=1</equation>代入上式解得<equation>C=-\frac{1}{3}.</equation>因此，<equation>R(p)=p\mathrm{e}^{\frac{p^{3}-1}{3}}.</equation>

---

**2009年第12题 | 填空题 | 4分**

12. 设某产品的需求函数为<equation>Q=Q(p)</equation>，其对价格 p的弹性<equation>\varepsilon_{p}=0.2</equation>，则当需求量为10000件时，价格增加1元会使产品收益增加 ___元.

**答案:**## 8000.

**解析:**解 由需求弹性的定义知<equation>\varepsilon_{p}=-Q^{\prime}(p)\cdot \frac{p}{Q}=0.2</equation>因为收益函数为<equation>R ( p )=Q ( p )\cdot p</equation>所以，<equation>\frac{\mathrm{d} R}{\mathrm{d} p}=Q^{\prime}(p) p+Q ( p )=Q ( p ) \left[ \frac{Q^{\prime}(p)}{Q ( p )} p+1 \right]=Q ( p ) \left( 1-\varepsilon_{p} \right).</equation>由微分的经济学意义知，当需求量为10000件，价格增加1元时，即<equation>Q=1 0 0 00</equation><equation>\mathrm{d} p=1</equation>时，产品的收益会增加<equation>\mathrm{d} R=Q(p)(1-\varepsilon_{p})\mathrm{d} p=1 0 0 0 0 \times(1-0. 2) \times1=8 0 0 0</equation>（元）.

---


#### 泰勒公式

**2024年第20题 | 解答题 | 12分**

20. (本题满分12分)

设函数 f(x)具有2阶导数，且<equation>f^{\prime}(0)=f^{\prime}(1),\left| f^{\prime\prime}(x)\right| \leqslant 1</equation>证明：

I. 当 x<equation>\in(0,1)</equation>时，<equation>|f(x)-f(0)(1-x)-f(1)x|\leqslant \frac{x(1-x)}{2}</equation>II.<equation>\left| \int_{0}^{1} f(x)\mathrm{d}x-\frac{f(0)+f(1)}{2}\right| \leqslant \frac{1}{12}.</equation>

**解析:**证（I）（法一）分别写出<equation>f(x)</equation>在<equation>x=0</equation>与<equation>x=1</equation>处的一阶泰勒公式.<equation>f (x) = f (0) + f ^ {\prime} (0) x + \frac {f ^ {\prime \prime} \left(\xi_ {1}\right) x ^ {2}}{2},</equation><equation>f (x) = f (1) + f ^ {\prime} (1) (x - 1) + \frac {f ^ {\prime \prime} \left(\xi_ {2}\right) \left(x - 1\right) ^ {2}}{2},</equation>其中<equation>\xi_{1}</equation>介于0与x之间，<equation>\xi_{2}</equation>介于1与x之间.

(2) 式<equation>\times x-</equation>(1)式<equation>\times(x-1)</equation>，并结合<equation>f^{\prime}(0)=f^{\prime}(1)</equation>可得<equation>f (x) = f (0) (1 - x) + f (1) x + \frac {x (x - 1)}{2} \left[ f ^ {\prime \prime} \left(\xi_ {2}\right) (x - 1) - f ^ {\prime \prime} \left(\xi_ {1}\right) x \right].</equation>由（3）式可得，当<equation>x\in(0,1)</equation>时，<equation>\left| f (x) - f (0) (1 - x) - f (1) x \right| = \frac {x (1 - x)}{2} \left| f ^ {\prime \prime} \left(\xi_ {2}\right) (x - 1) - f ^ {\prime \prime} \left(\xi_ {1}\right) x \right|.</equation>由于<equation>| f^{\prime \prime}(\xi_{2})(x - 1) - f^{\prime \prime}(\xi_{1})x | \leqslant | f^{\prime \prime}(\xi_{2}) | (1 - x) + | f^{\prime \prime}(\xi_{1}) | x</equation>，故结合<equation>| f^{\prime \prime}(x) | \leqslant 1</equation>以及（4）式可得<equation>| f (x) - f (0) (1 - x) - f (1) x | \leqslant \frac {x (1 - x)}{2} \cdot [ (1 - x) + x ] = \frac {x (1 - x)}{2}.</equation>（法二）所证命题等价于当<equation>x\in (0,1)</equation>时，<equation>- \frac {x (1 - x)}{2} \leqslant f (x) - f (0) (1 - x) - f (1) x \leqslant \frac {x (1 - x)}{2}.</equation>令<equation>F ( x ) = f ( x ) - f ( 0 ) ( 1 - x ) - f ( 1 ) x - \frac { x ( 1 - x ) } { 2 }</equation>，则<equation>F ( 0 ) = F ( 1 ) = 0</equation>，且<equation>F^{\prime \prime}(x)=f^{\prime \prime}(x)</equation>+1.由于<equation>| f^{\prime \prime}(x) | \leqslant 1</equation>，故<equation>F^{\prime \prime}(x)\geqslant 0.</equation>下面证明当<equation>x\in (0,1)</equation>时，<equation>F(x)\leqslant 0.</equation>若存在<equation>c\in(0,1)</equation>，使得<equation>F(c)>0</equation>，则分别对<equation>[0,c],[c,1]</equation>上的<equation>F(x)</equation>使用拉格朗日中值定理可得，存在<equation>\xi_{1}\in(0,c),\xi_{2}\in(c,1)</equation>，使得<equation>F ^ {\prime} \left(\xi_ {1}\right) = \frac {F (c) - F (0)}{c - 0} > 0, \quad F ^ {\prime} \left(\xi_ {2}\right) = \frac {F (1) - F (c)}{1 - c} < 0.</equation>再对<equation>[\xi_{1},\xi_{2} ]</equation>上的<equation>F^{\prime}(x)</equation>使用拉格朗日中值定理可得，存在<equation>\xi\in(\xi_{1},\xi_{2})</equation>，使得<equation>F ^ {\prime \prime} (\xi) = \frac {F ^ {\prime} \left(\xi_ {2}\right) - F ^ {\prime} \left(\xi_ {1}\right)}{\xi_ {2} - \xi_ {1}} < 0.</equation>这与<equation>F^{\prime \prime}(x)\geqslant 0</equation>矛盾.

因此，当<equation>x\in (0,1)</equation>时，<equation>F(x)\leqslant 0</equation>，即<equation>f(x) - f(0)(1 - x) - f(1)x\leqslant \frac{x(1 - x)}{2}.</equation>令<equation>G(x) = f(x) - f(0)(1 - x) - f(1)x + \frac{x(1 - x)}{2}</equation>，同理可得<equation>G^{\prime \prime}(x)\leqslant 0</equation>，且进一步可得当<equation>x\in</equation>(0,1)时，<equation>G(x)\geqslant 0</equation>，即<equation>f(x) - f(0)(1 - x) - f(1)x\geqslant -\frac{x(1 - x)}{2}</equation>.

综上所述，所证命题成立.

（Ⅱ）由第（Ⅰ）问可得<equation>\left| f (x) - f (0) (1 - x) - f (1) x \right| \leqslant \frac {x (1 - x)}{2}.</equation>对（5）式两端从0到1积分可得，<equation>\begin{aligned} \int_ {0} ^ {1} | f (x) - f (0) (1 - x) - f (1) x | \mathrm {d} x \leqslant \int_ {0} ^ {1} \frac {x (1 - x)}{2} \mathrm {d} x &= \frac {1}{2} \int_ {0} ^ {1} \left(x - x ^ {2}\right) \mathrm {d} x \\ &= \frac {1}{2} \left(\frac {x ^ {2}}{2} - \frac {x ^ {3}}{3}\right) \Big | _ {0} ^ {1} = \frac {1}{1 2}. \end{aligned}</equation>进一步由定积分的性质可得<equation>\begin{array}{l} \left| \int_ {0} ^ {1} f (x) \mathrm {d} x - f (0) \int_ {0} ^ {1} (1 - x) \mathrm {d} x - f (1) \int_ {0} ^ {1} x \mathrm {d} x \right| = \left| \int_ {0} ^ {1} f (x) \mathrm {d} x - \frac {f (0) + f (1)}{2} \right| \\ \leqslant \int_ {0} ^ {1} | f (x) - f (0) (1 - x) - f (1) x | \mathrm {d} x \leqslant \frac {1}{1 2}. \\ \end{array}</equation>

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
