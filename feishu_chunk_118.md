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


