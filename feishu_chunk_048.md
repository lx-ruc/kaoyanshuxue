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


