#### 数学期望与方差

**2025年第8题 | 选择题 | 5分 | 答案: C**
8. 设二维随机变量 (X,Y) 服从正态分布 N(0,0;1,1;<equation>\rho</equation>), 其中<equation>\rho \in(-1,1)</equation>, 若 a,b为满足<equation>a^{2}+b^{2}=1</equation>的任意实数，则 D(aX+bY) 的最大值为（    )

A.1 B.2 C.<equation>1+|\rho|</equation>D.<equation>1+\rho^{2}</equation>
答案: C
**解析: **解 由于<equation>(X, Y)</equation>服从正态分布<equation>N(0, 0; 1, 1; \rho)</equation>，故<equation>D (X) = D (Y) = 1, \quad \operatorname {C o v} (X, Y) = \rho \sqrt {D (X)} \sqrt {D (Y)} = \rho .</equation>根据方差的性质，<equation>\begin{aligned} D (a X + b Y) &= D (a X) + D (b Y) + 2 \operatorname {C o v} (a X, b Y) = a ^ {2} D (X) + b ^ {2} D (Y) + 2 a b \operatorname {C o v} (X, Y) \\ &= a ^ {2} + b ^ {2} + 2 a b \rho \xlongequal {a ^ {2} + b ^ {2} = 1} 1 + 2 a b \rho . \end{aligned}</equation>又因为<equation>a^2 + b^2 = 1 \geqslant 2 |ab|</equation>，所以<equation>1 + 2ab\rho \leqslant 1 + 2|ab\rho| \leqslant 1 + |\rho|</equation>，从而<equation>D(aX + bY) \leqslant</equation>1+<equation>| \rho |</equation>. 若<equation>\rho > 0</equation>，则 D（aX+bY）的最大值为1+<equation>\rho</equation>，最大值在<equation>\left\{ \begin{array}{l l} a=\pm \frac{\sqrt{2}}{2}, \\ b=\pm \frac{\sqrt{2}}{2} \end{array} \right.</equation>时取得；若<equation>\rho < 0</equation>，则 D（aX+

bY）的最大值为<equation>1 - \rho</equation>，最大值在时取得；若<equation>\rho = 0</equation>，则<equation>D(aX + bY)\equiv 1.</equation>因此，<equation>D ( a X+b Y )</equation>的最大值为<equation>1+|\rho|</equation>，应选C.

---

**2023年第8题 | 选择题 | 5分 | 答案: C**
8. 设随机变量 X服从参数为1的泊松分布，则<equation>E[|X - E(X)|] =</equation>（    ）

A.<equation>\frac{1} {\mathrm{e}}</equation>B.<equation>\frac{1}{2}</equation>C.<equation>\frac{2} {\mathrm{e}}</equation>D. 1
答案: C
**解析: **归于 X服从参数为1的泊松分布，故<equation>E ( X )=1.</equation>从而<equation>| X - E (X) | = | X - 1 | = \left\{ \begin{array}{l l} 1, & X = 0, \\ X - 1, & X = 1, 2, \dots . \end{array} \right.</equation>由参数为1的泊松分布的分布律可知，<equation>P\{X = 0\} = \frac{1^{0}\cdot\mathrm{e}^{-1}}{0!} = \frac{1}{\mathrm{e}}.</equation>根据数学期望的定义，<equation>\begin{aligned} E [ \mid X - E (X) \mid ] &= 1 \cdot P \{X = 0 \} + \sum_ {k = 1} ^ {\infty} (k - 1) P \{X = k \} \\ &= \frac {1}{\mathrm {e}} + \sum_ {k = 0} ^ {\infty} (k - 1) P \{X = k \} - (0 - 1) P \{X = 0 \} \\ &= \frac {1}{\mathrm {e}} + E (X - 1) + \frac {1}{\mathrm {e}} = \frac {1}{\mathrm {e}} + E (X) - 1 + \frac {1}{\mathrm {e}} \\ \underline {{\underline {{E (X) = 1}}}} \frac {2}{\mathrm {e}}. \end{aligned}</equation>因此，应选C.

---

**2021年第22题 | 解答题 | 12分**
2. (本题满分12分)

在区间（0,2）上随机取一点，将该区间分成两段，较短一段的长度为 X，较长一段的长度为 Y，令<equation>Z=\frac{Y}{X}</equation>.

I. 求 X的概率密度；

II. 求 Z的概率密度；

III. 求<equation>E\left(\frac{X}{Y}\right).</equation>
**答案: **（I）<equation>X</equation>的概率密度为<equation>f_{X}(x)=\left\{\begin{array}{ll}1,&0<x<1,\\ 0,&\text{其他};\end{array} \right.</equation>（Ⅱ）<equation>Z</equation>的概率密度为<equation>f_{Z}(z)=\left\{\begin{array}{ll}0,&z<1,\\ \frac{2}{(z+1)^{2}},&z\geqslant 1; \end{array} \right.</equation>（Ⅲ）<equation>2\ln 2-1.</equation>
**解析: **解（I）根据分析，在区间（0，2）上随机取一点，将该点位置记为 W，则 W服从（0，2）上的均匀分布.<equation>X=\min \{ W,2-W\}</equation>由于<equation>X</equation>为较短一段的长度，故<equation>X</equation>的取值范围为（0,1].

记<equation>X</equation>的分布函数为<equation>F_{X}(x)</equation>当<equation>x < 0</equation>时，<equation>F_{X}(x) = P\{X\leqslant x\} = 0.</equation>当<equation>0\leqslant x < 1</equation>时，<equation>\begin{array}{l} F _ {X} (x) = P \{X \leqslant x \} = 1 - P \{X > x \} = 1 - P \{W > x, 2 - W > x \} \\ = 1 - P \left\{x < W < 2 - x \right\} = 1 - P \left\{W < 2 - x \right\} + P \left\{W \leqslant x \right\} \\ = 1 - \frac {2 - x}{2} + \frac {x}{2} = x. \\ \end{array}</equation>当<equation>x\geqslant 1</equation>时，<equation>F_{X}(x) = P\{X\leqslant x\} = 1.</equation>因此，<equation>F_{X}(x) = \left\{ \begin{array}{ll}0, & x < 0,\\ x, & 0\leqslant x < 1, f_{X}(x) = \left\{ \begin{array}{ll}1, & 0 < x < 1,\\ 0, & \text{其他}. \end{array} \right. X</equation>服从区间（0,1）上的均匀分布.<equation>1, x \geqslant 1,</equation>（Ⅱ）<equation>Z=\frac{Y}{X}=\frac{2-X}{X}=\frac{2}{X}-1.</equation>记Z的分布函数为<equation>F_{Z}(z).</equation>由于<equation>X</equation>的取值范围为<equation>(0,1]</equation>，故<equation>Z</equation>的取值范围为<equation>[1, + \infty)</equation>.

当<equation>z < 1</equation>时，<equation>F_{Z}(z) = P\{Z\leqslant z\} = 0.</equation>当<equation>z\geqslant 1</equation>时，<equation>\begin{array}{l} F _ {Z} (z) = P \left\{\frac {2}{X} - 1 \leqslant z \right\} = P \left\{\frac {2}{X} \leqslant z + 1 \right\} = P \left\{X \geqslant \frac {2}{z + 1} \right\} \\ = 1 - P \left\{X < \frac {2}{z + 1} \right\}. \\ \end{array}</equation>由于<equation>P\left\{X < \frac{2}{z + 1}\right\} = \frac{2}{z + 1}</equation>，故<equation>F_{Z}(z) = 1 - \frac{2}{z + 1}</equation>因此，<equation>F_{Z}(z) = \left\{ \begin{array}{ll} 0, & z < 1, \\ 1 - \frac{2}{z + 1}, & z \geqslant 1. \end{array} \right. f_{Z}(z) = \left\{ \begin{array}{ll} 0, & z < 1, \\ \frac{2}{(z + 1)^{2}}, & z \geqslant 1. \end{array} \right.</equation>（Ⅲ）（法一）注意到<equation>\frac{X}{Y}=\frac{X}{2-X}.</equation><equation>\begin{aligned} E \left(\frac {X}{Y}\right) &= E \left(\frac {X}{2 - X}\right) = \int_ {- \infty} ^ {+ \infty} \frac {x}{2 - x} \cdot f _ {X} (x) \mathrm {d} x = \int_ {0} ^ {1} \frac {x}{2 - x} \mathrm {d} x = \int_ {0} ^ {1} \left(- 1 + \frac {2}{2 - x}\right) \mathrm {d} x \\ &= \left[ - x - 2 \ln (2 - x) \right] \Bigg | _ {0} ^ {1} = 2 \ln 2 - 1. \end{aligned}</equation>（法二）由于<equation>Z = \frac{Y}{X}</equation>，故<equation>\frac{X}{Y} = \frac{1}{Z}</equation>.于是，<equation>E \left(\frac {X}{Y}\right) = E \left(\frac {1}{Z}\right) = \int_ {- \infty} ^ {+ \infty} \frac {1}{z} \cdot f _ {Z} (z) \mathrm {d} z = 2 \int_ {1} ^ {+ \infty} \frac {1}{z} \cdot \frac {1}{(z + 1) ^ {2}} \mathrm {d} z.</equation>设<equation>\frac{1}{z(z + 1)^2} = \frac{A}{z} +\frac{B}{z + 1} +\frac{C}{(z + 1)^2}</equation>，则<equation>\frac {1}{z (z + 1) ^ {2}} = \frac {A (z + 1) ^ {2} + B z (z + 1) + C z}{z (z + 1) ^ {2}} = \frac {(A + B) z ^ {2} + (2 A + B + C) z + A}{z (z + 1) ^ {2}}.</equation>比较系数可得<equation>\left\{ \begin{array}{l l} A+B=0, \\ 2 A+B+C=0, \\ A=1. \end{array} \right.</equation>解得<equation>\left\{ \begin{array}{l l} A=1, \\ B=-1, \\ C=-1. \end{array} \right.</equation>从而<equation>\frac{1}{z(z+1)^2}=\frac{1}{z}-\frac{1}{z+1}-\frac{1}{(z+1)^2}.</equation><equation>\begin{aligned} E \left(\frac {X}{Y}\right) &= 2 \int_ {1} ^ {+ \infty} \left[ \frac {1}{z} - \frac {1}{z + 1} - \frac {1}{(z + 1) ^ {2}} \right] \mathrm {d} z = 2 \left(\ln \frac {z}{z + 1} + \frac {1}{z + 1}\right) \Bigg | _ {1} ^ {+ \infty} \\ &= 2 \left(0 - \ln \frac {1}{2} - \frac {1}{2}\right) = 2 \ln 2 - 1. \end{aligned}</equation>

---

**2019年第14题 | 填空题 | 4分**
14. 设随机变量 X的概率密度为 f(x)<equation>\left\{\begin{array}{ll}\frac{x}{2},&0<x<2,\\0,&\text{其他},\end{array}\right.</equation>F(x)为 X的分布函数，E(X)为 X的数学期望，则<equation>P\{F(X)>E(X)-1\}=</equation>___
**解析: **解（法一）分别计算<equation>E ( X )</equation>，<equation>F ( x )</equation><equation>E (X) = \int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \int_ {0} ^ {2} \frac {x ^ {2}}{2} \mathrm {d} x = \left. \frac {x ^ {3}}{6} \right| _ {0} ^ {2} = \frac {4}{3}.</equation>当<equation>x < 0</equation>时，<equation>F ( x )=0.</equation>当<equation>0 \leqslant x < 2</equation>时，<equation>F(x) = \int_{-\infty}^{x} f(t)\mathrm{d}t = \int_{0}^{x}\frac{t}{2}\mathrm{d}t = \frac{x^2}{4}</equation>.

当<equation>x\geqslant 2</equation>时，<equation>F(x) = 1.</equation>于是，<equation>F ( x ) = \left\{ \begin{array}{ll} 0, & x < 0, \\ \frac{x^{2}}{4}, & 0 \leqslant x < 2, \\ 1, & x \geqslant 2. \end{array} \right.</equation>因此，<equation>\begin{array}{l} P \left\{F (X) > E (X) - 1 \right\} = P \left\{F (X) > \frac {1}{3} \right\} = P \left\{\frac {X ^ {2}}{4} > \frac {1}{3}, 0 \leqslant X < 2 \right\} + P \left\{X \geqslant 2 \right\} \\ = P \left\{\frac {2}{\sqrt {3}} < X < 2 \right\} + \int_ {2} ^ {+ \infty} f (x) \mathrm {d} x = 1 - \int_ {0} ^ {\frac {2}{\sqrt {3}}} \frac {x}{2} \mathrm {d} x + 0 \\ = 1 - \frac {x ^ {2}}{4} \Bigg | _ {0} ^ {\frac {2}{\sqrt {3}}} = \frac {2}{3}. \\ \end{array}</equation>（法二）我们先证明<equation>Y = F(X)</equation>服从（0，1）上的均匀分布.

注意到<equation>F ( x )</equation>在（0，2）上严格单调增加，其值域为（0，1），故可定义<equation>F^{-1}(y)</equation>，<equation>y\in(0,1).</equation>考虑Y的分布函数<equation>F_{Y}(y).</equation>当<equation>y < 0</equation>时，由于<equation>F(X)</equation>仅在<equation>[0,1]</equation>上取值，故<equation>F_{Y}(y) = 0.</equation>当<equation>0\leqslant y < 1</equation>时，<equation>F _ {Y} (y) = P \left\{Y \leqslant y \right\} = P \left\{F (X) \leqslant y \right\} = P \left\{X \leqslant F ^ {- 1} (y) \right\} = F \left(F ^ {- 1} (y)\right) = y.</equation>当<equation>y \geqslant 1</equation>时，<equation>P\{Y \leqslant y\} = 1</equation>，即<equation>F_{Y}(y) = 1.</equation>因此，<equation>F_{Y}(y) = \left\{ \begin{array}{ll}0, & y < 0,\\ y, & 0\leqslant y < 1,\\ 1, & y\geqslant 1. \end{array} \right.</equation>这说明<equation>Y = F(X)</equation>服从（0，1）上的均匀分布.

由法一可知<equation>E ( X )=\frac{4}{3}</equation>故<equation>P \left\{F (X) > E (X) - 1 \right\} = P \left\{F (X) > \frac {1}{3} \right\} = 1 - P \left\{F (X) \leqslant \frac {1}{3} \right\} = 1 - \frac {1}{3} = \frac {2}{3}.</equation>

---


