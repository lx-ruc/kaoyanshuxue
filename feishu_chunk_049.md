#### 泰勒公式

**2024年第19题 | 解答题 | 12分**

9. (本题满分12分)

设函数 f(x)具有2阶导数，且<equation>f^{\prime}(0)=f^{\prime}(1),\left| f^{\prime\prime}(x)\right| \leqslant 1</equation>.证明：

I. 当 x<equation>\in(0,1)</equation>时，<equation>|f(x)-f(0)(1-x)-f(1)x|\leqslant \frac{x(1-x)}{2}</equation>II.<equation>\left|\int_{0}^{1} f(x)\mathrm{d}x-\frac{f(0)+f(1)}{2}\right|\leqslant \frac{1}{12}.</equation>

**解析:**（I）（法一）分别写出 f(x)在 x=0与 x=1处的一阶泰勒公式.<equation>f (x) = f (0) + f ^ {\prime} (0) x + \frac {f ^ {\prime \prime} \left(\xi_ {1}\right) x ^ {2}}{2},</equation><equation>f (x) = f (1) + f ^ {\prime} (1) (x - 1) + \frac {f ^ {\prime \prime} \left(\xi_ {2}\right) \left(x - 1\right) ^ {2}}{2},</equation>其中<equation>\xi_{1}</equation>介于0与<equation>x</equation>之间，<equation>\xi_{2}</equation>介于1与<equation>x</equation>之间.

(2) 式<equation>\times x-（1）</equation>式<equation>\times (x-1)</equation>，并结合<equation>f^{\prime}(0)=f^{\prime}(1)</equation>可得<equation>f (x) = f (0) (1 - x) + f (1) x + \frac {x (x - 1)}{2} \left[ f ^ {\prime \prime} \left(\xi_ {2}\right) (x - 1) - f ^ {\prime \prime} \left(\xi_ {1}\right) x \right].</equation>由（3）式可得，当<equation>x\in(0,1)</equation>时，<equation>\left| f (x) - f (0) (1 - x) - f (1) x \right| = \frac {x (1 - x)}{2} \left| f ^ {\prime \prime} \left(\xi_ {2}\right) (x - 1) - f ^ {\prime \prime} \left(\xi_ {1}\right) x \right|.</equation>由于<equation>|f^{\prime \prime}(\xi_{2})(x - 1) - f^{\prime \prime}(\xi_{1})x| \leqslant |f^{\prime \prime}(\xi_{2})|(1 - x) + |f^{\prime \prime}(\xi_{1})|x,</equation>故结合<equation>|f^{\prime \prime}(x)| \leqslant 1</equation>以及（4）式可得<equation>| f (x) - f (0) (1 - x) - f (1) x | \leqslant \frac {x (1 - x)}{2} \cdot [ (1 - x) + x ] = \frac {x (1 - x)}{2}.</equation>（法二）所证命题等价于当<equation>x\in (0,1)</equation>时，<equation>- \frac {x (1 - x)}{2} \leqslant f (x) - f (0) (1 - x) - f (1) x \leqslant \frac {x (1 - x)}{2}.</equation>令<equation>F ( x )=f ( x )-f ( 0 ) ( 1-x )-f ( 1 ) x-\frac{x(1-x)}{2}</equation>，则<equation>F ( 0 )=F ( 1 )=0</equation>，且<equation>F^{\prime \prime}(x)=f^{\prime \prime}(x)</equation>+1. 由于<equation>|f^{\prime \prime}(x)| \leqslant 1</equation>，故<equation>F^{\prime \prime}(x) \geqslant 0.</equation>下面证明当<equation>x\in (0,1)</equation>时，<equation>F(x)\leqslant 0.</equation>若存在<equation>c\in (0,1)</equation>，使得<equation>F(c) > 0</equation>，则分别对<equation>[0,c],[c,1]</equation>上的<equation>F(x)</equation>使用拉格朗日中值定理可得，存在<equation>\xi_{1}\in (0,c),\xi_{2}\in (c,1)</equation>，使得<equation>F ^ {\prime} \left(\xi_ {1}\right) = \frac {F (c) - F (0)}{c - 0} > 0, \quad F ^ {\prime} \left(\xi_ {2}\right) = \frac {F (1) - F (c)}{1 - c} < 0.</equation>再对<equation>[\xi_{1},\xi_{2} ]</equation>上的<equation>F^{\prime}(x)</equation>使用拉格朗日中值定理可得，存在<equation>\xi\in(\xi_{1},\xi_{2})</equation>，使得<equation>F ^ {\prime \prime} (\xi) = \frac {F ^ {\prime} \left(\xi_ {2}\right) - F ^ {\prime} \left(\xi_ {1}\right)}{\xi_ {2} - \xi_ {1}} < 0.</equation>这与<equation>F^{\prime \prime}(x)\geqslant0</equation>矛盾.

因此，当<equation>x\in (0,1)</equation>时，<equation>F(x)\leqslant 0</equation>，即<equation>f(x) - f(0)(1 - x) - f(1)x\leqslant \frac{x(1 - x)}{2}.</equation>令<equation>G ( x ) = f ( x ) - f ( 0 ) ( 1 - x ) - f ( 1 ) x + \frac { x ( 1 - x ) } { 2 }</equation>，同理可得<equation>G^{\prime \prime}(x)\leqslant 0</equation>，且进一步可得当<equation>x\in</equation>（0,1）时，<equation>G ( x ) \geqslant 0</equation>，即<equation>f ( x ) - f ( 0 ) ( 1 - x ) - f ( 1 ) x \geqslant - \frac { x ( 1 - x ) } { 2 } .</equation>综上所述，所证命题成立.

（Ⅱ）由第（Ⅰ）问可得<equation>\left| f (x) - f (0) (1 - x) - f (1) x \right| \leqslant \frac {x (1 - x)}{2}.</equation>对（5）式两端从0到1积分可得，<equation>\begin{aligned} \int_ {0} ^ {1} | f (x) - f (0) (1 - x) - f (1) x | \mathrm {d} x \leqslant \int_ {0} ^ {1} \frac {x (1 - x)}{2} \mathrm {d} x &= \frac {1}{2} \int_ {0} ^ {1} \left(x - x ^ {2}\right) \mathrm {d} x \\ &= \frac {1}{2} \left(\frac {x ^ {2}}{2} - \frac {x ^ {3}}{3}\right) \Big | _ {0} ^ {1} = \frac {1}{1 2}. \end{aligned}</equation>进一步由定积分的性质可得<equation>\begin{array}{l} \left| \int_ {0} ^ {1} f (x) \mathrm {d} x - f (0) \int_ {0} ^ {1} (1 - x) \mathrm {d} x - f (1) \int_ {0} ^ {1} x \mathrm {d} x \right| = \left| \int_ {0} ^ {1} f (x) \mathrm {d} x - \frac {f (0) + f (1)}{2} \right| \\ \leqslant \int_ {0} ^ {1} | f (x) - f (0) (1 - x) - f (1) x | \mathrm {d} x \leqslant \frac {1}{1 2}. \\ \end{array}</equation>

---

**2023年第20题 | 解答题 | 12分**

20. (本题满分12分)

设函数 f(x)在<equation>[-a,a]</equation>上具有二阶连续导数，证明：

I. 若 f(0)=0，则存在<equation>\xi\in(-a,a)</equation>，使得<equation>f^{\prime\prime}(\xi)=\frac{1}{a^{2}}[f(a)+f(-a)]</equation>；

II. 若 f(x)在<equation>(-a,a)</equation>内取得极值，则存在<equation>\eta\in(-a,a)</equation>使得<equation>|f^{\prime\prime}(\eta)|\geqslant\frac{1}{2a^{2}}|f(a)-f(-a)|.</equation>

**答案:**# （I）证明略；

（Ⅱ）证明略.

**解析:**证 （ I ）由<equation>f ( x )</equation>的泰勒公式可得<equation>f (a) = f (0) + f ^ {\prime} (0) a + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {1}\right) a ^ {2} \xlongequal {f (0) = 0} f ^ {\prime} (0) a + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {1}\right) a ^ {2},</equation><equation>f (- a) = f (0) + f ^ {\prime} (0) \cdot (- a) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {2}\right) a ^ {2} \stackrel {f (0) = 0} {=} f ^ {\prime} (0) \cdot (- a) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {2}\right) a ^ {2},</equation>其中<equation>\xi_{1}\in (0,a),\xi_{2}\in (-a,0)</equation>.两式相加可得<equation>f (a) + f (- a) = \frac {a ^ {2}}{2} \left[ f ^ {\prime \prime} \left(\xi_ {1}\right) + f ^ {\prime \prime} \left(\xi_ {2}\right) \right].</equation>记<equation>\max \left\{f^{\prime \prime}\left(\xi_{1}\right), f^{\prime \prime}\left(\xi_{2}\right)\right\} = M,</equation><equation>\min \left\{f^{\prime \prime}\left(\xi_{1}\right), f^{\prime \prime}\left(\xi_{2}\right)\right\} = m,</equation>则由（1）式可得<equation>m \leqslant \frac {f (a) + f (- a)}{a ^ {2}} = \frac {1}{2} \left[ f ^ {\prime \prime} \left(\xi_ {1}\right) + f ^ {\prime \prime} \left(\xi_ {2}\right) \right] \leqslant M.</equation>由于<equation>f ( x )</equation>在<equation>[ - a,a]</equation>上有二阶连续导数，故由连续函数的介值定理可知，存在<equation>\xi \in[ \xi_{2},\xi_{1} ]\subset(-a,a)</equation>，使得<equation>f^{\prime \prime}(\xi)=\frac{1}{a^{2}}[f(a)+f(-a)]</equation>.

（Ⅱ）设<equation>f(x)</equation>在<equation>(-a,a)</equation>内的极值点为<equation>x_{0}</equation>，则<equation>f^{\prime}(x_{0})=0.</equation>由<equation>f(x)</equation>的泰勒公式可得<equation>\begin{aligned} f (a) &= f \left(x _ {0}\right) + f ^ {\prime} \left(x _ {0}\right) \left(a - x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {1}\right) \left(a - x _ {0}\right) ^ {2} \\ \underline {{=}} f ^ {\prime \prime} \left(x _ {0}\right) &= 0 f \left(x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {1}\right) \left(a - x _ {0}\right) ^ {2}, \\ f (- a) &= f \left(x _ {0}\right) + f ^ {\prime} \left(x _ {0}\right) \left(- a - x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {2}\right) \left(- a - x _ {0}\right) ^ {2} \\ \underline {{=}} f ^ {\prime \prime} \left(x _ {0}\right) &= 0 f \left(x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {2}\right) \left(a + x _ {0}\right) ^ {2}, \end{aligned}</equation>其中<equation>\eta_{1}\in (x_{0},a),\eta_{2}\in (-a,x_{0})</equation>. 两式相减可得<equation>f (a) - f (- a) = \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {1}\right) \left(a - x _ {0}\right) ^ {2} - \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {2}\right) \left(a + x _ {0}\right) ^ {2}.</equation>记<equation>\max \{|f''(\eta_1)|, |f''(\eta_2)|\} = M</equation>，则由（2）式可得<equation>\left| f (a) - f (- a) \right| \leqslant \frac {M}{2} \left[ \left(a - x _ {0}\right) ^ {2} + \left(a + x _ {0}\right) ^ {2} \right] = \frac {M}{2} \left(2 a ^ {2} + 2 x _ {0} ^ {2}\right) \leqslant \frac {M}{2} \cdot 4 a ^ {2} = 2 a ^ {2} M.</equation>因此，<equation>M\geqslant \frac{1}{2a^{2}}|f(a) - f(-a)|.</equation>取<equation>\eta \in \{\eta_1, \eta_2\}</equation>使得<equation>|f''(\eta)| = M</equation>，则<equation>\eta \in (-a, a)</equation>满足<equation>|f''(\eta)| \geqslant \frac{1}{2a^2}|f(a) - f(-a)|</equation>.

---

**2021年第3题 | 选择题 | 5分 | 答案: A**

3. 设函数<equation>f(x)=\frac{\sin x}{1+x^{2}}</equation>在 x=0处的3次泰勒多项式为<equation>ax+bx^{2}+cx^{3}</equation>，则（    )

A. a=1,b=0,c=-<equation>\frac{7}{6}</equation>B. a=1,b=0,c=<equation>\frac{7}{6}</equation>C. a=-1,b=-1,c=-<equation>\frac{7}{6}</equation>D. a=-1,b=-1,c=<equation>\frac{7}{6}</equation>

答案: A

**解析:**解 由于<equation>\sin x=x-\frac{x^{3}}{6}+o\left(x^{3}\right),\frac{1}{1+x^{2}}=1-x^{2}+o\left(x^{2}\right)</equation>，故<equation>\frac{\sin x}{1+x^{2}}=\left[x-\frac{x^{3}}{6}+o\left(x^{3}\right)\right]\left[1-x^{2}+o\left(x^{2}\right)\right]=x-x^{3}-\frac{x^{3}}{6}+o\left(x^{3}\right)</equation><equation>= x-\frac{7x^{3}}{6}+o\left(x^{3}\right).</equation>因此，<equation>\frac{\sin x}{1+x^{2}}</equation>在 x=0处的3次泰勒多项式为<equation>x-\frac{7 x^{3}}{6}.</equation>a=1,b=0,c=-<equation>\frac{7}{6}.</equation>应选A.

---


