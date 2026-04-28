#### 二维随机变量及其分布

**2024年第10题 | 选择题 | 5分 | 答案: D**

10. 设随机变量 X，Y相互独立，且均服从参数为<equation>\lambda</equation>的指数分布. 令<equation>Z=|X-Y|</equation>，则下列随机变量中与 Z同分布的是（    ）

A.<equation>X+Y</equation>B.<equation>\frac{X+Y}{2}</equation>C. 2X D. X

答案: D

**解析:**解 由于 X, Y相互独立，且均服从参数为<equation>\lambda</equation>的指数分布，故（X，Y）的联合概率密度为<equation>f (x, y) = \left\{ \begin{array}{l l} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)}, & x > 0, y > 0, \\ 0, & \text {其 他}. \end{array} \right.</equation>记<equation>F_{Z}(z)</equation>为<equation>Z=|X-Y|</equation>的分布函数，<equation>D_{z}=\left\{(x,y)\right|-z\leq x-y\leq z\}</equation>，则<equation>F _ {Z} (z) = P \left\{Z \leqslant z \right\} = P \left\{\left| X - Y \right| \leqslant z \right\} = P \left\{- z \leqslant X - Y \leqslant z \right\} = \iint_ {D.} f (x, y) \mathrm {d} x \mathrm {d} y.</equation>当<equation>z < 0</equation>时，<equation>D_{z} = \varnothing , F_{Z}(z) = 0.</equation>当<equation>z \geqslant 0</equation>时，记<equation>D = \{(x,y) \mid x \geqslant 0, y \geqslant 0\}</equation>，则<equation>D \cap D_z \neq \emptyset</equation>，为图（a）中的灰色区域.

(a)

(b)

下面用两种方法计算<equation>z \geqslant 0</equation>时的<equation>F_{z}(z)</equation>.

(c)

（法一）如图（a）所示，由于<equation>D \cap D_{z}</equation>关于直线<equation>y=x</equation>对称，故记其位于直线<equation>y=x</equation>下方的部分为<equation>D_{0}.</equation>将<equation>D_{0}</equation>写成Y型区域，<equation>D_{0}=\left|(x,y)\right| \mid y \leqslant x \leqslant y+z,0 \leqslant y < +\infty \mid.</equation><equation>\begin{array}{l} F _ {z} (z) = \iint_ {D _ {z}} f (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {D \cap D _ {z}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y \xlongequal {\text {轮 换 对称 性}} 2 \iint_ {D _ {0}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y \\ = 2 \lambda^ {2} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \mathrm {d} y \int_ {y} ^ {y + z} \mathrm {e} ^ {- \lambda x} \mathrm {d} x = - 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \cdot \mathrm {e} ^ {- \lambda x} \Bigg | _ {x = y} ^ {x = y + z} \mathrm {d} y \\ = - 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \left(\mathrm {e} ^ {- \lambda y - \lambda z} - \mathrm {e} ^ {- \lambda y}\right) \mathrm {d} y = - 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- 2 \lambda y} \left(\mathrm {e} ^ {- \lambda z} - 1\right) \mathrm {d} y \\ = \left(\mathrm {e} ^ {- \lambda z} - 1\right) \int_ {0} ^ {+ \infty} \left(- 2 \lambda \mathrm {e} ^ {- 2 \lambda y}\right) \mathrm {d} y = \left(\mathrm {e} ^ {- \lambda z} - 1\right) \mathrm {e} ^ {- 2 \lambda y} \Bigg | _ {0} ^ {+ \infty} \\ = \left(\mathrm {e} ^ {- \lambda z} - 1\right) \cdot (- 1) = 1 - \mathrm {e} ^ {- \lambda z}. \\ \end{array}</equation>（法二）如图（b）所示，<equation>D_{1}=D\backslash D_{z}</equation>关于直线<equation>y=x</equation>对称，记其位于直线<equation>y=x</equation>下方的部分为<equation>D_{2}.</equation>将<equation>D_{2}</equation>写成Y型区域，<equation>D_{2}=\{(x,y)\mid y+z\leqslant x<+\infty ,0\leqslant y<+\infty \}.</equation><equation>\begin{array}{l} F _ {Z} (z) = \iint_ {D _ {z}} f (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {D \cap D _ {z}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y = 1 - \iint_ {D _ {1}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y \\ \underline {{\text {轮换 对称性}}} 1 - 2 \iint_ {D _ {2}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y = 1 - 2 \lambda^ {2} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \mathrm {d} y \int_ {y + z} ^ {+ \infty} \mathrm {e} ^ {- \lambda x} \mathrm {d} x \\ = 1 + 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \cdot \mathrm {e} ^ {- \lambda x} \Bigg | _ {x = y + z} ^ {+ \infty} \mathrm {d} y = 1 - 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \cdot \mathrm {e} ^ {- \lambda (y + z)} \mathrm {d} y \\ = 1 - 2 \lambda \mathrm {e} ^ {- \lambda z} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- 2 \lambda y} \mathrm {d} y = 1 + \mathrm {e} ^ {- \lambda z} \cdot \mathrm {e} ^ {- 2 \lambda y} \Bigg | _ {0} ^ {+ \infty} = 1 - \mathrm {e} ^ {- \lambda z}. \\ \end{array}</equation>因此，<equation>F_{z}(z)=\left\{ \begin{array}{ll}1-\mathrm{e}^{-\lambda z},& z\geqslant 0,\\ 0,& \text{其他}, \end{array} \right. f_{z}(z)=\left\{ \begin{array}{ll}\lambda \mathrm{e}^{-\lambda z},& z\geqslant 0,\\ 0,& \text{其他}, \end{array} \right. Z</equation>服从参数为<equation>\lambda</equation>的指数分布.进一步可得，Z与X同分布.选项D正确，选项C错误.

下面说明选项A、B不正确.

对选项A，当<equation>z\geqslant 0</equation>时，由于<equation>D_{3} = \{(x,y)|x + y\leqslant z,x\geqslant 0,y\geqslant 0\}</equation>真包含于<equation>D\cap D_{z}</equation>，故<equation>X + Y</equation>的分布函数<equation>F_{1}(z)</equation>满足，对任意<equation>z > 0,F_{1}(z) < F_{Z}(z)</equation>.从而<equation>X + Y</equation>与Z不同分布.

对选项B，当<equation>z\geqslant 0</equation>时，记<equation>D_{4} = \left| (x,y)\right| x + y\leqslant 2z,x\geqslant 0,y\geqslant 0\}</equation>，则<equation>\frac{X+Y}{2}</equation>的分布函数<equation>\begin{array}{l} F _ {2} (z) = \iint_ {D _ {4}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y = \lambda^ {2} \int_ {0} ^ {2 x} \mathrm {e} ^ {- \lambda x} \mathrm {d} x \int_ {0} ^ {2 x - x} \mathrm {e} ^ {- \lambda y} \mathrm {d} y = 1 - (2 \lambda z + 1) \mathrm {e} ^ {- 2 \lambda z} \\ \neq F _ {Z} (z). \\ \end{array}</equation>从而<equation>\frac{X+Y}{2}</equation>与Z不同分布.

综上所述，应选D.

---

**2020年第8题 | 选择题 | 4分 | 答案: C**

8. 设随机变量（X，Y）服从二维正态分布<equation>N \left( 0,0;1,4;-\frac{1}{2} \right)</equation>，则下列随机变量中服从标准正态分布且与 X相互独立的是（    )

A.<equation>\frac{\sqrt{5}}{5} ( X+Y )</equation>B.<equation>\frac{\sqrt{5}}{5} ( X-Y )</equation>C.<equation>\frac{\sqrt{3}}{3} ( X+Y )</equation>D.<equation>\frac{\sqrt{3}}{3} ( X-Y )</equation>

答案: C

**解析:**解 由（X，Y）服从二维正态分布<equation>N \left( 0,0;1,4;-\frac{1}{2} \right)</equation>可知，<equation>X\sim N (0,1), Y\sim N (0,4)</equation>，且<equation>\rho_{X Y}=-\frac{1}{2}.</equation><equation>E ( X )=0,D ( X )=1,E ( Y )=0,D ( Y )=4.</equation>由此可计算<equation>\operatorname{C o v} ( X, Y ).</equation>由协方差的计算公式，可得<equation>\operatorname {C o v} (X, Y) = \rho_ {X Y} \sqrt {D (X)} \sqrt {D (Y)} = - \frac {1}{2} \times 1 \times 2 = - 1.</equation>由选项设置，分别考虑<equation>\operatorname{Cov}(X,X+Y),\operatorname{Cov}(X,X-Y)</equation>（由注可知，<equation>(X,X+Y),(X,X-Y)</equation>均服从二维正态分布）.<equation>\operatorname {C o v} (X, X + Y) = \operatorname {C o v} (X, X) + \operatorname {C o v} (X, Y) = 1 - 1 = 0.</equation><equation>\operatorname {C o v} (X, X - Y) = \operatorname {C o v} (X, X) - \operatorname {C o v} (X, Y) = 1 - (- 1) = 2.</equation>X与X-Y相关，从而不独立，故可以排除选项B、D.

又因为所求随机变量应服从标准正态分布，所以考虑将 X+Y标准化.<equation>E (X + Y) = 0, \quad D (X + Y) = D (X) + D (Y) + 2 \operatorname {C o v} (X, Y) = 1 + 4 - 2 = 3.</equation>由于<equation>D \left[ \frac{\sqrt{5}}{5} (X+Y) \right]=\frac{1}{5} D (X+Y)=\frac{3}{5} \neq 1,D \left[ \frac{\sqrt{3}}{3} (X+Y) \right]=\frac{1}{3} D (X+Y)=1</equation>，故可排除选项A，应选C.

---

**2019年第22题 | 解答题 | 11分**

2. (本题满分11分)

设随机变量 X与 Y相互独立，X服从参数为1的指数分布，Y的概率分布为<equation>P\{Y=-1\}=p,P\{Y=1\}=</equation><equation>1-p \left( 0<p<1 \right).</equation>令<equation>Z=XY</equation>.

I. 求 Z的概率密度；

II. p为何值时，X与 Z不相关；

III. X与 Z是否相互独立？

**答案:**（I）<equation>Z</equation>的概率密度为<equation>f_{Z}(z)=\left\{\begin{array}{ll}p\mathrm{e}^{z},&z\leqslant 0,\\ (1-p)\mathrm{e}^{-z},&z>0; \end{array} \right.</equation>（Ⅱ）当<equation>p=\frac{1}{2}</equation>时，X与Z不相关；

（Ⅲ）X与Z不相互独立.

**解析:**（I）先计算 Z的分布函数<equation>F_{Z}(z).</equation><equation>\begin{array}{l} F _ {Z} (z) = P \left\{X Y \leqslant z \right\} = P \left\{X \geqslant - z, Y = - 1 \right\} + P \left\{X \leqslant z, Y = 1 \right\} \\ \underline {{\text {独立性}}} P \left\{X \geqslant - z \right\} P \left\{Y = - 1 \right\} + P \left\{X \leqslant z \right\} P \left\{Y = 1 \right\} \\ = p \left[ 1 - F _ {X} (- z) \right] + (1 - p) F _ {X} (z), \\ \end{array}</equation>其中<equation>F_{X}(x)</equation>是X的分布函数.

于是，Z的概率密度为<equation>f _ {Z} (z) = F _ {Z} ^ {\prime} (z) = \left\{p \left[ 1 - F _ {X} (- z) \right] + (1 - p) F _ {X} (z) \right\} ^ {\prime} = p f _ {X} (- z) + (1 - p) f _ {X} (z).</equation>由于<equation>X</equation>服从参数为1的指数分布，故<equation>X</equation>的概率密度为<equation>f_{X}(x) = \left\{ \begin{array}{ll} \mathrm{e}^{-x}, & x > 0, \\ 0, & x \leqslant 0. \end{array} \right.</equation>当<equation>z\leqslant0</equation>时，<equation>-z\geqslant0,f_{X}(-z)=\mathrm{e}^{z},f_{X}(z)=0</equation>；当<equation>z > 0</equation>时，<equation>-z < 0,f_{X}(z)=\mathrm{e}^{-z},f_{X}(-z)=0.</equation><equation>f _ {Z} (z) = \left\{ \begin{array}{l l} p \mathrm {e} ^ {z}, & z \leqslant 0, \\ (1 - p) \mathrm {e} ^ {- z}, & z > 0. \end{array} \right.</equation>（Ⅱ）计算<equation>\operatorname{Cov}(X,Z).</equation><equation>\begin{array}{l} \operatorname {C o v} (X, Z) = E (X Z) - E (X) E (Z) = E \left(X ^ {2} Y\right) - E (X) E (X Y) \\ \underline {{\mathrm {独立性}}} E \left(X ^ {2}\right) E (Y) - \left[ E (X) \right] ^ {2} E (Y) \\ = D (X) E (Y). \\ \end{array}</equation>下面分别计算 D（X），E（Y）.

由于 X服从参数为1的指数分布，故<equation>D ( X )=1.</equation><equation>E (Y) = 1 \times (1 - p) + (- 1) \times p = 1 - 2 p.</equation>因此，<equation>\operatorname{Cov}(X,Z) = E(Y) = 1 - 2p.</equation>当<equation>p=\frac{1}{2}</equation>时，<equation>\operatorname{Cov}(X,Z)=0</equation>，X与Z不相关.

（Ⅲ）由第（Ⅱ）问可知，当<equation>p\neq \frac{1}{2}</equation>时，X与Z相关，从而不相互独立.

下面只需考虑 p =<equation>\frac{1}{2}</equation>的情况.

（法一）当<equation>p=\frac{1}{2}</equation>时，检验<equation>P\{X < 1,Z < 1\} = P\{X < 1\} P\{Z < 1\}</equation>是否成立.<equation>P \{X < 1 \} = \int_ {0} ^ {1} \mathrm {e} ^ {- x} \mathrm {d} x = 1 - \mathrm {e} ^ {- 1}.</equation><equation>\begin{aligned} P \{Z < 1 \} &= P \{X Y < 1 \} = F _ {Z} (1) = \frac {1}{2} \left[ 1 - F _ {X} (- 1) \right] + \frac {1}{2} F _ {X} (1) \\ &= \frac {1}{2} \times (1 - 0) + \frac {1}{2} \int_ {0} ^ {1} \mathrm {e} ^ {- x} \mathrm {d} x = \frac {1}{2} + \frac {1}{2} \left(1 - \mathrm {e} ^ {- 1}\right). \end{aligned}</equation><equation>\begin{aligned} P \{X < 1, Z < 1 \} &= P \{X < 1, X Y < 1 \} = P \{X \leqslant 0, X Y < 1 \} + P \{0 < X < 1, X Y < 1 \} \\ &= P \{0 < X < 1, X Y < 1 \} = P \{0 < X < 1, Y = 1 \} + P \{0 < X < 1, Y = - 1 \} \\ &= P \{0 < X < 1 \} = P \{X < 1 \} = 1 - \mathrm {e} ^ {- 1}. \end{aligned}</equation>由于<equation>1-\mathrm{e}^{-1}\neq(1-\mathrm{e}^{-1})\cdot\left[\frac{1}{2}+\frac{1}{2}(1-\mathrm{e}^{-1})\right]</equation>，故X，Z不相互独立.

（法二）当<equation>p=\frac{1}{2}</equation>时，检验<equation>P\{X > 1,Z < 1\} = P\{X > 1\} P\{Z < 1\}</equation>是否成立.

当 X > 1时，XY < 1等价于<equation>Y < \frac{1}{X}.</equation>又因为此时<equation>\frac{1}{X} < 1</equation>，而Y只可能取1和-1两个值，所以<equation>Y < \frac{1}{X}</equation>能推出 Y=-1.于是，<equation>P \{X > 1 \} = \int_ {1} ^ {+ \infty} \mathrm {e} ^ {- x} \mathrm {d} x = \mathrm {e} ^ {- 1}.</equation><equation>P \{Z < 1 \} \xlongequal {\text {同 法 一}} \frac {1}{2} + \frac {1}{2} \left(1 - \mathrm {e} ^ {- 1}\right).</equation><equation>\begin{array}{l} P \{X > 1, Z < 1 \} = P \{X > 1, X Y < 1 \} = P \left\{X > 1, Y < \frac {1}{X} \right\} = P \{X > 1, Y = - 1 \} \\ \underline {{\mathrm {独立 性}}} P \{X > 1 \} P \{Y = - 1 \} = \frac {1}{2} \mathrm {e} ^ {- 1}. \\ \end{array}</equation>由于<equation>\frac{1}{2}\mathrm{e}^{-1}\neq \mathrm{e}^{-1}\cdot \left[\frac{1}{2}+\frac{1}{2}\left(1-\mathrm{e}^{-1}\right)\right]</equation>，故X，Z不相互独立.

综上所述，X，Z不相互独立.

---

**2016年第22题 | 解答题 | 11分**

（本题满分11分）

设二维随机变量 (X,Y)在区域 D = {(x,y) | 0 < x < 1, x² < y <<equation>\sqrt{x}</equation>}上服从均匀分布，令<equation>U=\left\{\begin{array}{l l}1,&X\leqslant Y,\\ 0,&X>Y. \end{array} \right.</equation>I. 写出 (X,Y)的概率密度；

II. 问 U与 X是否相互独立？并说明理由；

III. 求 Z=U+X的分布函数 F(z).

**答案:**（I）<equation>f ( x,y)=\left\{ \begin{array}{ll} 3, & 0 < x < 1, x^{2} < y < \sqrt{x}, \\ 0, & \text{其他}; \end{array} \right.</equation>（Ⅱ）<equation>U</equation>与X不相互独立，理由略；

(Ⅲ)<equation>F (z) = \left\{ \begin{array}{ll} 0, & z < 0, \\ \frac{3}{2} z^{2} - z^{3}, & 0 \leqslant z < 1, \\ 2 (z - 1)^{\frac{3}{2}} - \frac{3}{2} z^{2} + 3 z - 1, & 1 \leqslant z < 2, \\ 1, & z \geqslant 2. \end{array} \right.</equation>

**解析:**（I）区域 D如图（a）所示，其面积为<equation>S = \int_ {0} ^ {1} \sqrt {x} \mathrm {d} x - \int_ {0} ^ {1} x ^ {2} \mathrm {d} x = \frac {2}{3} x ^ {\frac {3}{2}} \left| _ {0} ^ {1} - \frac {x ^ {3}}{3} \right| _ {0} ^ {1} = \frac {2}{3} - \frac {1}{3} = \frac {1}{3}.</equation>又由于（X，Y）在区域 D上服从均匀分布，故（X，Y）的概率密度为<equation>f (x, y) = \left\{ \begin{array}{l l} 3, & 0 < x < 1, x ^ {2} < y < \sqrt {x}, \\ 0, & \text {其 他}. \end{array} \right.</equation>(a)

(b)

（Ⅱ）考虑<equation>P\{U = 0, X\leqslant t\}</equation><equation>P \{U = 0 \} = P \{X > Y \} = \iint_ {\{(x, y) | x > x \}} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {x ^ {2}} ^ {x} 3 \mathrm {d} y = \int_ {0} ^ {1} 3 \left(x - x ^ {2}\right) \mathrm {d} x = \frac {1}{2}.</equation>对<equation>t \leqslant 0</equation>，<equation>P\{X \leqslant t\} = 0</equation>，<equation>P\{U = 0, X \leqslant t\} = 0.</equation>于是，<equation>P \left\{U = 0, X \leqslant t \right\} = P \left\{U = 0 \right\} \cdot P \left\{X \leqslant t \right\}.</equation>对<equation>t \geqslant 1</equation><equation>P\{X \leqslant t\} = 1,P\{U = 0,X \leqslant t\} = P\{U = 0\}</equation>.于是，<equation>P \{U = 0, X \leqslant t \} = P \{U = 0 \} \cdot P \{X \leqslant t \}.</equation>对 0 < t < 1，有效积分区域为图（b）中的蓝色区域.<equation>P \left\{U = 0, X \leqslant t \right\} = P \left\{X > Y, X \leqslant t \right\} = \int_ {0} ^ {t} \mathrm {d} x \int_ {x ^ {2}} ^ {x} 3 \mathrm {d} y = \int_ {0} ^ {t} 3 \left(x - x ^ {2}\right) \mathrm {d} x = \frac {3}{2} t ^ {2} - t ^ {3},</equation><equation>P \left\{X \leqslant t \right\} = \int_ {0} ^ {t} \mathrm {d} x \int_ {x ^ {2}} ^ {\sqrt {x}} 3 \mathrm {d} y = \int_ {0} ^ {t} 3 \left(\sqrt {x} - x ^ {2}\right) \mathrm {d} x = 2 t ^ {\frac {3}{2}} - t ^ {3}.</equation>于是，<equation>\begin{aligned} P \{U = 0, X \leqslant t \} - P \{U = 0 \} \cdot P \{X \leqslant t \} &= \frac {3}{2} t ^ {2} - t ^ {3} - \frac {1}{2} \left(2 t ^ {\frac {3}{2}} - t ^ {3}\right) \\ &= \frac {3}{2} t ^ {2} - \frac {1}{2} t ^ {3} - t ^ {\frac {3}{2}} \neq 0. (\mathrm {见 注} \textcircled{1}) \end{aligned}</equation>因此，当 0 < t < 1时，U与X不相互独立.

（Ⅲ）由题设知，<equation>\begin{array}{l} F (z) = P \left\{Z \leqslant z \right\} = P \left\{U + X \leqslant z \right\} \\ = P \left\{U + X \leqslant z, U = 0 \right\} + P \left\{U + X \leqslant z, U = 1 \right\} \\ = P \left\{X \leqslant z, U = 0 \right\} + P \left\{X \leqslant z - 1, U = 1 \right\} \\ = P \left\{X \leqslant z, X > Y \right\} + P \left\{X \leqslant z - 1, X \leqslant Y \right\}. \\ \end{array}</equation>当 z < 0时，z-1<0，于是<equation>P\{X\leqslant z,X > Y\}=0,P\{X\leqslant z-1,X\leqslant Y\}=0</equation>从而 F（z）=0.当 0≤z<1时，z-1<0，于是 P<equation>\{X\leqslant z-1,X\leqslant Y\}=0</equation>从而<equation>F (z) = P \left\{X \leqslant z, X > Y \right\} = \int_ {0} ^ {z} \mathrm {d} x \int_ {x ^ {2}} ^ {x} 3 \mathrm {d} y = \int_ {0} ^ {z} 3 \left(x - x ^ {2}\right) \mathrm {d} x = \frac {3}{2} z ^ {2} - z ^ {3}.</equation>当<equation>1\leqslant z < 2</equation>时，<equation>0\leqslant z - 1 < 1</equation><equation>\begin{array}{l} F (z) = P \left\{X \leqslant z, X > Y \right\} + P \left\{X \leqslant z - 1, X \leqslant Y \right\} \\ = P \left\{X \leqslant 1, X > Y \right\} + P \left\{X \leqslant z - 1, X \leqslant Y \right\} \\ = \frac {1}{2} + \int_ {0} ^ {z - 1} \mathrm {d} x \int_ {x} ^ {\sqrt {x}} 3 \mathrm {d} y = \frac {1}{2} + \int_ {0} ^ {z - 1} 3 (\sqrt {x} - x) \mathrm {d} x \\ = \frac {1}{2} + 2 (z - 1) ^ {\frac {3}{2}} - \frac {3}{2} (z - 1) ^ {2} = 2 (z - 1) ^ {\frac {3}{2}} - \frac {3}{2} z ^ {2} + 3 z - 1. \\ \end{array}</equation>当<equation>z\geqslant 2</equation>时，<equation>z - 1\geqslant 1,F(z) = 1.</equation>综上所述，<equation>F ( z ) = \left\{ \begin{array}{ll} 0, & z < 0, \\ \frac{3}{2} z^{2} - z^{3}, & 0 \leqslant z < 1, \\ 2 ( z - 1 )^{\frac{3}{2}} - \frac{3}{2} z^{2} + 3 z - 1, & 1 \leqslant z < 2, \\ 1, & z \geqslant 2. \end{array} \right.</equation>

---

**2015年第14题 | 填空题 | 4分**

14. 设二维随机变量<equation>(X, Y)</equation>服从正态分布<equation>N(1, 0; 1, 1; 0)</equation>, 则<equation>P\{XY - Y < 0\} =</equation>___

**解析:**由题设知，X，Y不相关。又由于（X，Y）服从正态分布，故X，Y相互独立.从而<equation>\begin{aligned} P \{X Y - Y < 0 \} &= P \{(X - 1) Y < 0 \} = P \{X < 1, Y > 0 \} + P \{X > 1, Y < 0 \} \\ &= P \{X < 1 \} \cdot P \{Y > 0 \} + P \{X > 1 \} \cdot P \{Y < 0 \}. \end{aligned}</equation>由<equation>( X, Y ) \sim N ( 1, 0 ; 1, 1 ; 0 )</equation>可知，<equation>X\sim N ( 1, 1 )</equation><equation>Y\sim N ( 0, 1 )</equation>从而X，Y的概率密度的图像分别关于<equation>x=1</equation>，<equation>x=0</equation>对称，于是<equation>P \{ X < 1 \} = P \{ X > 1 \} = \frac{1}{2}</equation><equation>P \{ Y < 0 \} = P \{ Y > 0 \} = \frac{1}{2}.</equation>因此，<equation>P \left\{X Y - Y < 0 \right\} = \frac {1}{2} \times \frac {1}{2} + \frac {1}{2} \times \frac {1}{2} = \frac {1}{2}.</equation>

---

**2013年第8题 | 选择题 | 4分 | 答案: C**

8. 设随机变量 X和 Y相互独立，且 X和 Y的概率分布分别为（    ）

<table border="1"><tr><td>X</td><td>0</td><td>1</td><td>2</td><td>3</td></tr><tr><td>P</td><td><equation>\frac{1}{2}</equation></td><td><equation>\frac{1}{4}</equation></td><td><equation>\frac{1}{8}</equation></td><td><equation>\frac{1}{8}</equation></td></tr></table>

<table border="1"><tr><td>Y</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td></tr></table>

则<equation>P\{X+Y=2\}=(\quad)</equation>A.<equation>\frac{1}{1 2}</equation>B.<equation>\frac{1}{8}</equation>C.<equation>\frac{1}{6}</equation>D.<equation>\frac{1}{2}</equation>

答案: C

**解析:**由题设知<equation>\begin{array}{l} P \{X + Y = 2 \} = P \{X = 1, Y = 1 \} + P \{X = 2, Y = 0 \} + P \{X = 3, Y = - 1 \} \\ \underline {{\underline {{X , Y}} \mathrm {相 互 独立}}} P \{X = 1 \} \cdot P \{Y = 1 \} + P \{X = 2 \} \cdot P \{Y = 0 \} + P \{X = 3 \} \cdot P \{Y = - 1 \} \\ = \frac {1}{4} \times \frac {1}{3} + \frac {1}{8} \times \frac {1}{3} + \frac {1}{8} \times \frac {1}{3} = \frac {1}{6}. \\ \end{array}</equation>应选C.

---

**2012年第7题 | 选择题 | 4分 | 答案: D**

7. 设随机变量 X与 Y相互独立，且都服从区间（0,1）上的均匀分布，则<equation>P\{ X^{2}+Y^{2}\leqslant1\}=</equation>A.<equation>\frac{1}{4}</equation>B.<equation>\frac{1}{2}</equation>C.<equation>\frac{\pi}{8}</equation>D.<equation>\frac{\pi}{4}</equation>

答案: D

**解析:**解 由题设知<equation>f_{X}(x) = \left\{ \begin{array}{ll}1, & 0 < x < 1,\\ 0, & \text{其他}, \end{array} \right.</equation><equation>f_{Y}(y) = \left\{ \begin{array}{ll}1, & 0 < y < 1,\\ 0, & \text{其他}. \end{array} \right.</equation>由于X与Y相互独立，故

（X，Y）的概率密度为<equation>f (x, y) = f _ {X} (x) f _ {Y} (y) = \left\{ \begin{array}{l l} 1, & 0 < x < 1, 0 < y < 1, \\ 0, & \text {其 他}. \end{array} \right.</equation>记<equation>D = \{(x,y)\mid 0\leqslant x\leqslant 1,0\leqslant y\leqslant 1\}</equation>，<equation>P \left\{X ^ {2} + Y ^ {2} \leqslant 1 \right\} = \iint_ {\left\{(x, y) \mid x ^ {2} + y ^ {2} \leqslant 1 \right\} \cap D} f (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {\left\{(x, y) \mid x ^ {2} + y ^ {2} \leqslant 1, x \geqslant 0, y \geqslant 0 \right\}} 1 \mathrm {d} x \mathrm {d} y = \frac {\pi}{4}.</equation>应选 D.

---

**2009年第8题 | 选择题 | 4分 | 答案: B**

8. 设随机变量 X与 Y相互独立，且 X服从标准正态分布 N(0,1), Y的概率分布为<equation>P\{Y=0\}=P\{Y=1\}=\frac{1}{2}</equation>. 记<equation>F_{Z}(z)</equation>为随机变量 Z=XY的分布函数，则函数<equation>F_{Z}(z)</equation>的间断点个数为（    )

A.0 B.1 C.2 D.3

答案: B

**解析:**解 先用两种方法求<equation>F_{Z}(z).</equation>（法一）由定义知<equation>\begin{array}{l} F _ {Z} (z) = P \left\{Z \leqslant z \right\} = P \left\{X Y \leqslant z \right\} = P \left\{X Y \leqslant z, Y = 0 \right\} + P \left\{X Y \leqslant z, Y = 1 \right\} \\ = P \left\{z \geqslant 0, Y = 0 \right\} + P \left\{X \leqslant z, Y = 1 \right\} \\ \xlongequal {X, Y \text {相 互 独立}} P \left\{z \geqslant 0, Y = 0 \right\} + P \left\{X \leqslant z \right\} \cdot P \left\{Y = 1 \right\} \\ = P \left\{z \geqslant 0, Y = 0 \right\} + \frac {1}{2} \Phi (z), \\ \end{array}</equation>其中<equation>\varPhi(z)</equation>为标准正态分布函数.

当<equation>z < 0</equation>时，<equation>P\{z\geqslant 0, Y = 0\} = P(\varnothing) = 0</equation>，故<equation>F_{Z}(z) = \frac{1}{2}\Phi (z).</equation>当<equation>z \geqslant 0</equation>时，<equation>P\{z \geqslant 0, Y = 0\} = P\{Y = 0\} = \frac{1}{2}</equation>，故<equation>F_{Z}(z) = \frac{1}{2} +\frac{1}{2}\Phi (z).</equation>（法二）由全概率公式知<equation>\begin{array}{l} F _ {Z} (z) = P \left\{Z \leqslant z \right\} = P \left\{X Y \leqslant z \right\} \\ = P \left\{X Y \leqslant z \mid Y = 0 \right\} \cdot P \left\{Y = 0 \right\} + P \left\{X Y \leqslant z \mid Y = 1 \right\} \cdot P \left\{Y = 1 \right\} \\ = \frac {1}{2} P \left\{z \geqslant 0 \mid Y = 0 \right\} + \frac {1}{2} P \left\{X \leqslant z \mid Y = 1 \right\} \\ \underline {{\underline {{X , Y}} \text {相 互 独 立}}} \frac {1}{2} P \left\{z \geqslant 0 \right\} + \frac {1}{2} P \left\{X \leqslant z \right\} \\ = \left\{ \begin{array}{l l} \frac {1}{2} \Phi (z), & z < 0, \\ \frac {1}{2} + \frac {1}{2} \Phi (z), & z \geqslant 0. \end{array} \right. \\ \end{array}</equation>由于<equation>\varPhi(z)</equation>连续，故<equation>F_{z}(z)</equation>仅在<equation>z = 0</equation>处间断.应选B.

---

**2009年第23题 | 解答题 | 11分**


袋中有1个红球、2个黑球与3个白球.现有放回地从袋中取两次，每次取一个球.以 X，Y，Z分别表示两次取球所取得的红球、黑球与白球的个数.

I. 求<equation>P\{X=1\mid Z=0\}</equation>；

II. 求二维随机变量（X，Y）的概率分布.

**答案:**(23) (I)<equation>\frac{4}{9}</equation>;

（Ⅱ）X和Y的联合分布律为

<table border="1"><tr><td rowspan="2">X

Y</td><td>0</td><td>1</td><td>2</td></tr><tr><td><equation>\frac{1}{4}</equation></td><td><equation>\frac{1}{6}</equation></td><td><equation>\frac{1}{36}</equation></td></tr><tr><td>1</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{9}</equation></td><td>0</td></tr><tr><td>2</td><td><equation>\frac{1}{9}</equation></td><td>0</td><td>0</td></tr></table>

**解析:**解（I）（法一）由条件概率的定义知，<equation>P \{X = 1 \mid Z = 0 \} = \frac {P \{X = 1 , Z = 0 \}}{P \{Z = 0 \}} = \frac {P \{X = 1 , Y = 1 \}}{P \{Z = 0 \}} = \frac {\mathrm {C} _ {2} ^ {1} \times \frac {1}{6} \times \frac {2}{6}}{\frac {3}{6} \times \frac {3}{6}} = \frac {4}{9}.</equation>（法二）<equation>P \{ X=1 \mid Z=0 \}</equation>是指在 Z=0，即两次所取的球中没有白球的条件下，两次取球为一黑一红的概率，即在1个红球、2个黑球中有放回地取得一黑一红的概率.因此，<equation>P \left\{X = 1 \mid Z = 0 \right\} = C _ {2} ^ {1} \times \frac {1}{3} \times \frac {2}{3} = \frac {4}{9}.</equation>（Ⅱ）由于是有放回地取球，故 X，Y所有可能的取值均为0，1，2.于是二维随机变量（X，Y）的概率分布为，<equation>P \{X = 0, Y = 0 \} = P \{Z = 2 \} = \frac {3}{6} \times \frac {3}{6} = \frac {1}{4},</equation><equation>P \{X = 0, Y = 1 \} = P \{Y = 1, Z = 1 \} = C _ {2} ^ {1} \times \frac {2}{6} \times \frac {3}{6} = \frac {1}{3},</equation><equation>P \{X = 0, Y = 2 \} = \frac {2}{6} \times \frac {2}{6} = \frac {1}{9},</equation><equation>P \{X = 1, Y = 0 \} = P \{X = 1, Z = 1 \} = C _ {2} ^ {1} \times \frac {1}{6} \times \frac {3}{6} = \frac {1}{6},</equation><equation>P \{X = 1, Y = 1 \} = \mathrm {C} _ {2} ^ {1} \times \frac {1}{6} \times \frac {2}{6} = \frac {1}{9}, \quad P \{X = 1, Y = 2 \} = 0,</equation><equation>P \{X = 2, Y = 0 \} = \frac {1}{6} \times \frac {1}{6} = \frac {1}{3 6}, \quad P \{X = 2, Y = 1 \} = 0, \quad P \{X = 2, Y = 2 \} = 0.</equation>因此，X和Y的联合分布律为

<table border="1"><tr><td rowspan="2">Y

X</td><td>0</td><td>1</td><td>2</td></tr><tr><td><equation>\frac{1}{4}</equation></td><td><equation>\frac{1}{6}</equation></td><td><equation>\frac{1}{36}</equation></td></tr><tr><td>1</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{9}</equation></td><td>0</td></tr><tr><td>2</td><td><equation>\frac{1}{9}</equation></td><td>0</td><td>0</td></tr></table>

---


### 数理统计的基本概念

**2023年第9题 | 选择题 | 5分 | 答案: D**

9. 设<equation>X_{1}, X_{2}, \dots, X_{n}</equation>为来自总体<equation>N(\mu_{1},\sigma^{2})</equation>的简单随机样本，<equation>Y_{1}, Y_{2}, \dots, Y_{m}</equation>为来自总体<equation>N(\mu_{2}, 2\sigma^{2})</equation>的简单随机样本，且两样本相互独立，记<equation>\bar{X}=\frac{1}{n}\sum_{i=1}^{n}X_{i},\bar{Y}=\frac{1}{m}\sum_{i=1}^{m}Y_{i},S_{1}^{2}=\frac{1}{n-1}\sum_{i=1}^{n}(X_{i}-\bar{X})^{2},S_{2}^{2}=\frac{1}{m-1}\sum_{i=1}^{m}(Y_{i}-\bar{Y})^{2}</equation>，则（    )

A.<equation>\frac{S_{1}^{2}}{S_{2}^{2}}\sim F(n,m)</equation>B.<equation>\frac{S_{1}^{2}}{S_{2}^{2}}\sim F(n-1,m-1)</equation>C.<equation>\frac{2S_{1}^{2}}{S_{2}^{2}}\sim F(n,m)</equation>D.<equation>\frac{2S_{1}^{2}}{S_{2}^{2}}\sim F(n-1,m-1)</equation>

答案: D

**解析:**解<equation>S_{1}^{2}=\frac{1}{n-1}\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}</equation>为<equation>X_{1},X_{2},\dots,X_{n}</equation>的样本方差，<equation>S_{2}^{2}=\frac{1}{m-1}\sum_{i=1}^{m}\left(Y_{i}-\bar{Y}\right)^{2}</equation>为<equation>Y_{1},</equation><equation>Y_{2},\dots,Y_{m}</equation>的样本方差.由正态总体的抽样分布定理可知，<equation>\frac {(n - 1) S _ {1} ^ {2}}{\sigma^ {2}} \sim \chi^ {2} (n - 1), \quad \frac {(m - 1) S _ {2} ^ {2}}{2 \sigma^ {2}} \sim \chi^ {2} (m - 1).</equation>又因为两个样本相互独立，所以由 F分布的定义可知<equation>\frac {\frac {(n - 1) S _ {1} ^ {2}}{\sigma^ {2}} / (n - 1)}{\frac {(m - 1) S _ {2} ^ {2}}{2 \sigma^ {2}} / (m - 1)} = \frac {S _ {1} ^ {2} / \sigma^ {2}}{S _ {2} ^ {2} / 2 \sigma^ {2}} = \frac {2 S _ {1} ^ {2}}{S _ {2} ^ {2}} \sim F (n - 1, m - 1).</equation>因此，应选D.

---

**2023年第10题 | 选择题 | 5分 | 答案: A**

10. 设<equation>X_{1}, X_{2}</equation>为来自总体<equation>N(\mu ,\sigma^{2})</equation>的简单随机样本，其中<equation>\sigma(\sigma >0)</equation>为未知参数.记<equation>\hat{\sigma}=a\left| X_{1}-X_{2}\right|</equation>若<equation>E(\hat{\sigma})=\sigma</equation>则 a=（    )

A.<equation>\frac{\sqrt{\pi}}{2}</equation>B.<equation>\frac{\sqrt{2\pi}}{2}</equation>C.<equation>\sqrt{\pi}</equation>D.<equation>\sqrt{2\pi}</equation>

答案: A

**解析:**由于<equation>X_{1}, X_{2}</equation>为来自总体<equation>N(\mu ,\sigma^{2})</equation>的简单随机样本，故<equation>X_{1}, X_{2}</equation>相互独立.

令<equation>Z = X_{1} - X_{2}</equation>，则<equation>Z\sim N(0,2\sigma^{2})</equation>，从而Z的概率密度<equation>f(z) = \frac{1}{\sqrt{2\pi}\cdot \sqrt{2}\sigma}\mathrm{e}^{-\frac{z^{2}}{4\sigma^{2}}}</equation><equation>\begin{array}{l} E (\mid Z \mid) = \int_ {- \infty} ^ {+ \infty} | z | f (z) \mathrm {d} z = 2 \int_ {0} ^ {+ \infty} \frac {1}{\sqrt {2 \pi} \cdot \sqrt {2} \sigma} \cdot z \mathrm {e} ^ {- \frac {z ^ {2}}{4 \sigma^ {2}}} \mathrm {d} z = \frac {1}{2 \sqrt {\pi} \sigma} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {z ^ {2}}{4 \sigma^ {2}}} \mathrm {d} \left(z ^ {2}\right) \\ = \frac {1}{2 \sqrt {\pi} \sigma} \cdot \left(- 4 \sigma^ {2} \mathrm {e} ^ {- \frac {z ^ {2}}{4 \sigma^ {2}}}\right) \Bigg | _ {0} ^ {+ \infty} = \frac {2}{\sqrt {\pi}} \sigma . \\ \end{array}</equation>由此可得<equation>E (\hat {\sigma}) = E \left(a \mid X _ {1} - X _ {2} \mid\right) = E \left(a \mid Z \mid\right) = \frac {2 a}{\sqrt {\pi}} \sigma .</equation>又因为<equation>E(\hat{\sigma}) = \sigma</equation>，即<equation>\frac{2a}{\sqrt{\pi}}\sigma = \sigma</equation>，所以<equation>a=\frac{\sqrt{\pi}}{2}.</equation>因此，应选A.

---

**2021年第9题 | 选择题 | 5分 | 答案: B**

9. 设<equation>( X_{1}, Y_{1}), ( X_{2}, Y_{2}), \cdots, ( X_{n}, Y_{n} )</equation>为来自总体<equation>N (\mu_{1}, \mu_{2}; \sigma_{1}^{2}, \sigma_{2}^{2}; \rho)</equation>的简单随机样本，令<equation>\theta=\mu_{1}-\mu_{2}, \bar{X}=\frac{1}{n}\sum_{i=1}^{n} X_{i}, \bar{Y}=</equation><equation>\frac{1}{n}\sum_{i=1}^{n} Y_{i}, \hat{\theta}=\bar{X}-\bar{Y}</equation>，则（    )

A.<equation>E(\hat{\theta})=\theta,D(\hat{\theta})=\frac{\sigma_{1}^{2}+\sigma_{2}^{2}}{n}</equation>B.<equation>E(\hat{\theta})=\theta,D(\hat{\theta})=\frac{\sigma_{1}^{2}+\sigma_{2}^{2}-2\rho\sigma_{1}\sigma_{2}}{n}</equation>C.<equation>E(\hat{\theta})\neq\theta,D(\hat{\theta})=\frac{\sigma_{1}^{2}+\sigma_{2}^{2}}{n}</equation>D.<equation>E(\hat{\theta})\neq\theta,D(\hat{\theta})=\frac{\sigma_{1}^{2}+\sigma_{2}^{2}-2\rho\sigma_{1}\sigma_{2}}{n}</equation>

答案: B

**解析:**解 由于总体（X，Y）服从<equation>N(\mu_{1},\mu_{2};\sigma_{1}^{2},\sigma_{2}^{2};\rho)</equation>，故<equation>X\sim N(\mu_{1},\sigma_{1}^{2}),Y\sim N(\mu_{2},\sigma_{2}^{2})</equation>，从而<equation>\overline{X}\sim</equation><equation>N \left( \mu_{1},\frac{\sigma_{1}^{2}}{n} \right),\overline{Y}\sim N \left( \mu_{2},\frac{\sigma_{2}^{2}}{n} \right).</equation>计算<equation>E(\hat{\theta})</equation><equation>E (\hat {\theta}) = E (\bar {X} - \bar {Y}) = E (\bar {X}) - E (\bar {Y}) = \mu_ {1} - \mu_ {2} = \theta .</equation>计算<equation>D(\hat{\theta})。</equation><equation>D (\hat {\theta}) = D (\bar {X} - \bar {Y}) = D (\bar {X}) + D (\bar {Y}) - 2 \operatorname {C o v} (\bar {X}, \bar {Y}) = \frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{n} - 2 \operatorname {C o v} (\bar {X}, \bar {Y}).</equation>由于<equation>\left(X_{1},Y_{1}\right),\left(X_{2},Y_{2}\right),\dots,\left(X_{n},Y_{n}\right)</equation>为简单随机样本，故它们相互独立，从而当<equation>i\neq j</equation>时，<equation>X_{i}</equation>与<equation>Y_{j}</equation>独立.于是，<equation>\operatorname{Cov}(X_{i},Y_{i})=\operatorname{Cov}(X,Y),\operatorname{Cov}(X_{i},Y_{j})=0(i\neq j).</equation><equation>\begin{aligned} \operatorname {C o v} (\bar {X}, \bar {Y}) &= \operatorname {C o v} \left(\frac {\sum_ {i = 1} ^ {n} X _ {i}}{n}, \frac {\sum_ {j = 1} ^ {n} Y _ {j}}{n}\right) = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \operatorname {C o v} \left(X _ {i}, Y _ {j}\right) = \frac {1}{n ^ {2}} \cdot \sum_ {i = 1} ^ {n} \operatorname {C o v} \left(X _ {i}, Y _ {i}\right) \\ &= \frac {1}{n ^ {2}} \cdot n \operatorname {C o v} (X, Y) = \frac {\operatorname {C o v} (X , Y)}{n}. \end{aligned}</equation>因此，<equation>D (\hat {\theta}) = \frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{n} - 2 \operatorname {C o v} (\bar {X}, \bar {Y}) = \frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{n} - \frac {2}{n} \operatorname {C o v} (X, Y) = \frac {\sigma_ {1} ^ {2} + \sigma_ {2} ^ {2} - 2 \rho \sigma_ {1} \sigma_ {2}}{n}.</equation>应选B.

---

**2018年第8题 | 选择题 | 4分 | 答案: B**

8. 设<equation>X_{1}, X_{2}, \cdots , X_{n}</equation>（其中 n≥2）为来自总体<equation>N(\mu ,\sigma^{2})(\sigma >0)</equation>的简单随机样本. 令<equation>\bar{X}=\frac{1}{n}\sum_{i=1}^{n}X_{i},</equation>S=<equation>\sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(X_{i}-\bar{X})^{2}},</equation><equation>S^{*} =\sqrt{\frac{1}{n}\sum_{i=1}^{n}(X_{i}-\mu)^{2}}</equation>，则（    )

A.<equation>\frac{\sqrt{n}(\bar{X}-\mu)}{S}\sim t(n)</equation>B.<equation>\frac{\sqrt{n}(\bar{X}-\mu)}{S}\sim t(n-1)</equation>C.<equation>\frac{\sqrt{n}(\bar{X}-\mu)}{S^{*}}\sim t(n)</equation>D.<equation>\frac{\sqrt{n}(\bar{X}-\mu)}{S^{*}}-t(n-1)</equation>

答案: B

**解析:**解 由于<equation>\bar{X}</equation>为样本均值，故<equation>\bar{X}\sim N\left(\mu ,\frac{\sigma^{2}}{n}\right).</equation>于是，<equation>\frac{\overline{{X}} - \mu}{\sqrt{\frac{\sigma^{2}}{n}}} = \frac{\sqrt{n}\left(\overline{{X}} - \mu\right)}{\sigma}\sim N(0,1)</equation>根据抽样分布定理（2），有<equation>\frac{(n - 1)S^{2}}{\sigma^{2}}\sim X^{2}(n - 1).</equation>又因为<equation>\frac{\sqrt{n}\left(\bar{X} - \mu\right)}{\sigma}</equation>与<equation>\frac{(n - 1)S^{2}}{\sigma^{2}}</equation>相互独立，所以<equation>\frac{\frac{\sqrt{n}\left(\bar{X} - \mu\right)}{\sigma}}{\sqrt{\frac{(n - 1)S^{2}}{\sigma^{2}}}\bigg /(n - 1)} = \frac{\sqrt{n}\left(\bar{X} - \mu\right)}{S}\sim t(n - 1).</equation>应选B.

---

**2017年第8题 | 选择题 | 4分 | 答案: B**

8. 设<equation>X_{1}, X_{2}, \dots , X_{n} ( n \geqslant 2 )</equation>为来自总体<equation>N (\mu , 1)</equation>的简单随机样本，记<equation>\bar{X}=\frac{1}{n}\sum_{i=1}^{n} X_{i}</equation>，则下列结论中不正确的是（    ）

A.<equation>\sum_{i=1}^{n} ( X_{i}-\mu )^{2}</equation>服从<equation>\chi^{2}</equation>分布

B.<equation>2 ( X_{n}-X_{1} )^{2}</equation>服从<equation>\chi^{2}</equation>分布

C.<equation>\sum_{i=1}^{n} ( X_{i}-\bar{X} )^{2}</equation>服从<equation>\chi^{2}</equation>分布

D.<equation>n ( \bar{X}-\mu )^{2}</equation>服从<equation>\chi^{2}</equation>分布

答案: B

**解析:**解 由题设知，<equation>X_{1}, X_{2}, \dots , X_{n}</equation>相互独立且与总体同分布.

依次分析各选项.

选项A：由<equation>X_{i}\sim N(\mu,1)</equation>知，<equation>X_{i}-\mu\sim N(0,1)</equation>，<equation>i=1,2,\cdots,n</equation>，故<equation>\sum_{i=1}^{n} \left(X_{i}-\mu\right)^{2}\sim X^{2}(n).</equation>因此选项A正确.

选项B：由<equation>X_{1}\sim N(\mu ,1), X_{n}\sim N(\mu ,1)</equation>知，<equation>X_{n}-X_{1}\sim N(0,2)</equation>，故<equation>\frac{X_{n}-X_{1}}{\sqrt{2}}\sim N(0,1)</equation>，于是<equation>\frac{(X_{n}-X_{1})^{2}}{2}\sim X^{2}(1).</equation>但2（<equation>X_{n}-X_{1} )^{2}</equation>不服从<equation>\chi^{2}</equation>分布.因此选项B不正确.

事实上，若<equation>2 \left(X_{n}-X_{1}\right)^{2}\sim \mathcal{X}^{2}(m)</equation>，则<equation>E \left[ 2 \left(X _ {n} - X _ {1}\right) ^ {2} \right] = m, \quad D \left[ 2 \left(X _ {n} - X _ {1}\right) ^ {2} \right] = 2 m.</equation>但由<equation>\frac{\left(X_{n}-X_{1}\right)^{2}}{2}\sim X^{2}(1)</equation>知，<equation>E \left[ \frac {\left(X _ {n} - X _ {1}\right) ^ {2}}{2} \right] = 1, \quad D \left[ \frac {\left(X _ {n} - X _ {1}\right) ^ {2}}{2} \right] = 2,</equation>从而<equation>E[2(X_{n}-X_{1})^{2}]=4,D[2(X_{n}-X_{1})^{2}]=32.</equation>这与<equation>D[2(X_{n}-X_{1})^{2}]=2E[2(X_{n}-X_{1})^{2}]</equation>矛盾，故<equation>2(X_{n}-X_{1})^{2}</equation>不服从<equation>\chi^{2}</equation>分布.

选项C：由性质（2）知，<equation>( n-1 ) S^{2} \sim X^{2} ( n-1 ).</equation>又因为<equation>S^{2}=\frac{1}{n-1}\sum_{i=1}^{n} \left( X_{i}-\overline{X}\right)^{2}</equation>，所以<equation>\sum_{i=1}^{n} \left( X_{i}-\overline{X}\right)^{2} \sim X^{2} ( n-1 ).</equation>因此选项C正确.

选项D：由性质（2）知，<equation>\overline{X}=\frac{1}{n}\sum_{i=1}^{n}X_{i}\sim N\left(\mu ,\frac{1}{n}\right)</equation>，于是<equation>\sqrt{n} \left( \overline{{X}}-\mu \right) \sim N (0,1)</equation>，从而<equation>n \left( \overline{{X}}-\mu \right)^{2} \sim X^{2} (1).</equation>因此选项D正确.

综上所述，应选B.

---

**2015年第8题 | 选择题 | 4分 | 答案: B**

8. 设总体<equation>X\sim B(m,\theta),X_{1},X_{2},\cdots,X_{n}</equation>为来自该总体的简单随机样本，<equation>\bar{X}</equation>为样本均值，则<equation>E\left[ \sum_{i=1}^{n}(X_{i}-\bar{X})^{2}\right] =</equation>(    )

A.<equation>( m-1 ) n \theta( 1-\theta)</equation>B.<equation>m(n-1)\theta( 1-\theta)</equation>C.<equation>( m-1 ) ( n-1 ) \theta( 1-\theta)</equation>D.<equation>mn \theta( 1-\theta)</equation>

答案: B

**解析:**解（法一）由于样本方差<equation>S^{2}=\frac{1}{n-1}\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}</equation>且<equation>E(S^{2})=D(X)=m\theta(1-\theta)</equation>，故<equation>E\left[ \sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}\right] = E\left[ (n-1)S^{2}\right] = (n-1)E(S^{2})=m(n-1)\theta(1-\theta).</equation>应选B.

（法二）直接计算.<equation>\begin{array}{l} E \left[ \sum_ {i = 1} ^ {n} \left(X _ {i} - \bar {X}\right) ^ {2} \right] = E \left(\sum_ {i = 1} ^ {n} X _ {i} ^ {2} - 2 \sum_ {i = 1} ^ {n} X _ {i} \bar {X} + n \bar {X} ^ {2}\right) = E \left(\sum_ {i = 1} ^ {n} X _ {i} ^ {2} - 2 n \bar {X} ^ {2} + n \bar {X} ^ {2}\right) \\ = E \left(\sum_ {i = 1} ^ {n} X _ {i} ^ {2} - n \bar {X} ^ {2}\right) = n E \left(X ^ {2}\right) - n E \left(\bar {X} ^ {2}\right) \\ = n \left\{\left[ E (X) \right] ^ {2} + D (X) \right\} - n \left\{\left[ E (\bar {X}) \right] ^ {2} + D (\bar {X}) \right\} \\ \frac {E (\bar {X}) = E (X)}{D (\bar {X}) = \frac {1}{n} D (X)} n \left[ D (X) - \frac {1}{n} D (X) \right] = m (n - 1) \theta (1 - \theta). \\ \end{array}</equation>应选B.

---

**2014年第8题 | 选择题 | 4分 | 答案: C**

8. 设<equation>X_{1}, X_{2}, X_{3}</equation>为来自正态总体<equation>N(0,\sigma^{2})</equation>的简单随机样本，则统计量<equation>S=\frac{X_{1}-X_{2}}{\sqrt{2}|X_{3}|}</equation>服从的分布为（    )

A. F(1,1) B. F(2,1) C. t(1) D. t(2)

答案: C

**解析:**解 由题设知，<equation>X_{1}, X_{2}, X_{3}</equation>相互独立且服从正态分布<equation>N(0,\sigma^{2})</equation>，故<equation>\frac{X_{1}-X_{2}}{\sqrt{2}\sigma}\sim N(0,1),\frac{X_{3}}{\sigma}\sim</equation><equation>N(0,1),\left(\frac{X_{3}}{\sigma}\right)^{2}\sim X^{2}(1).</equation>又因为<equation>\frac{X_{1}-X_{2}}{\sqrt{2}\sigma}</equation>与<equation>\left(\frac{X_{3}}{\sigma}\right)^{2}</equation>相互独立，所以<equation>S = \frac {X _ {1} - X _ {2}}{\sqrt {2} \left| X _ {3} \right|} = \frac {\frac {X _ {1} - X _ {2}}{\sqrt {2} \sigma}}{\left| \frac {X _ {3}}{\sigma} \right|} \sim t (1).</equation>应选C.

---

**2012年第8题 | 选择题 | 4分 | 答案: B**

8. 设<equation>X_{1}, X_{2}, X_{3}, X_{4}</equation>为来自总体<equation>N(1,\sigma^{2})(\sigma >0)</equation>的简单随机样本，则统计量<equation>\frac{X_{1}-X_{2}} {|X_{3}+X_{4}-2|}</equation>的分布为（    )

A. N(0,1) B. t(1) C.<equation>X^{2}(1)</equation>D. F(1,1)

答案: B

**解析:**解<equation>X_{1}, X_{2}, X_{3}, X_{4}</equation>相互独立且都服从正态分布<equation>N(1, \sigma^{2})</equation>.由正态分布的性质可得<equation>E \left(X _ {1} - X _ {2}\right) = 0, \quad D \left(X _ {1} - X _ {2}\right) = D \left(X _ {1}\right) + D \left(X _ {2}\right) = 2 \sigma^ {2},</equation><equation>E \left(X _ {3} + X _ {4} - 2\right) = 0, \quad D \left(X _ {3} + X _ {4} - 2\right) = D \left(X _ {3}\right) + D \left(X _ {4}\right) = 2 \sigma^ {2}.</equation>于是<equation>X_{1} - X_{2}\sim N(0,2\sigma^{2})</equation>，<equation>X_{3} + X_{4} - 2\sim N(0,2\sigma^{2})</equation>，从而<equation>\frac {X _ {1} - X _ {2}}{\sqrt {2} \sigma} \sim N (0, 1), \quad \frac {X _ {3} + X _ {4} - 2}{\sqrt {2} \sigma} \sim N (0, 1), \quad \left(\frac {X _ {3} + X _ {4} - 2}{\sqrt {2} \sigma}\right) ^ {2} \sim X ^ {2} (1).</equation>又因为<equation>\frac{X_{1}-X_{2}}{\sqrt{2}\sigma}</equation>与<equation>\left(\frac{X_{3}+X_{4}-2}{\sqrt{2}\sigma}\right)^{2}</equation>相互独立，所以<equation>\frac {X _ {1} - X _ {2}}{\left| X _ {3} + X _ {4} - 2 \right|} = \frac {\frac {X _ {1} - X _ {2}}{\sqrt {2} \sigma}}{\left| \frac {X _ {3} + X _ {4} - 2}{\sqrt {2} \sigma} \right|} \sim t (1).</equation>应选B.

---

**2011年第8题 | 选择题 | 4分 | 答案: D**

8. 设总体<equation>X</equation>服从参数为<equation>\lambda(\lambda>0)</equation>的泊松分布，<equation>X_{1},X_{2},\cdots,X_{n}(n\geqslant2)</equation>为来自该总体的简单随机样本，则对于统计量<equation>T_{1}=\frac{1}{n}\sum_{i=1}^{n}X_{i}</equation>和<equation>T_{2}=\frac{1}{n-1}\sum_{i=1}^{n-1}X_{i}+\frac{1}{n}X_{n}</equation>，有（    ）

A.<equation>E(T_{1})>E(T_{2}),D(T_{1})>D(T_{2})</equation>B.<equation>E(T_{1})>E(T_{2}),D(T_{1})<D(T_{2})</equation>C.<equation>E(T_{1})<E(T_{2}),D(T_{1})>D(T_{2})</equation>D.<equation>E(T_{1})<E(T_{2}),D(T_{1})<D(T_{2})</equation>

答案: D

**解析:**由于<equation>X_{1}, X_{2}, \dots, X_{n}</equation>为简单随机样本，故它们相互独立且与总体同分布，从而<equation>E \left(T _ {1}\right) = E \left(\frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i}\right) = \frac {1}{n} \sum_ {i = 1} ^ {n} E \left(X _ {i}\right) = \frac {1}{n} \cdot n E (X) = E (X),</equation><equation>\begin{array}{l} E \left(T _ {2}\right) = E \left(\frac {1}{n - 1} \sum_ {i = 1} ^ {n - 1} X _ {i} + \frac {1}{n} X _ {n}\right) = \frac {1}{n - 1} \sum_ {i = 1} ^ {n - 1} E \left(X _ {i}\right) + \frac {1}{n} E \left(X _ {n}\right) \\ = \frac {1}{n - 1} \cdot (n - 1) E (X) + \frac {1}{n} E (X) = E (X) + \frac {1}{n} E (X), \\ \end{array}</equation><equation>D \left(T _ {1}\right) = D \left(\frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i}\right) = \frac {1}{n ^ {2}} \cdot D \left(\sum_ {i = 1} ^ {n} X _ {i}\right) = \frac {1}{n ^ {2}} \cdot n D (X) = \frac {1}{n} D (X),</equation><equation>\begin{array}{l} D \left(T _ {2}\right) = D \left(\frac {1}{n - 1} \sum_ {i = 1} ^ {n - 1} X _ {i} + \frac {1}{n} X _ {n}\right) = \frac {1}{(n - 1) ^ {2}} \sum_ {i = 1} ^ {n - 1} D \left(X _ {i}\right) + \frac {1}{n ^ {2}} D \left(X _ {n}\right) \\ = \frac {1}{(n - 1) ^ {2}} \cdot (n - 1) D (X) + \frac {1}{n ^ {2}} D (X) = \frac {1}{n - 1} D (X) + \frac {1}{n ^ {2}} D (X). \\ \end{array}</equation>又由于<equation>E ( X ) = D ( X ) = \lambda > 0</equation>，故<equation>E \left(T _ {2}\right) > E \left(T _ {1}\right), \quad D \left(T _ {2}\right) > \frac {1}{n - 1} D (X) > \frac {1}{n} D (X) = D \left(T _ {1}\right).</equation>应选 D.

---

**2010年第14题 | 填空题 | 4分**

14. 设<equation>X_{1}, X_{2}, \cdots, X_{n}</equation>是来自总体<equation>N(\mu, \sigma^{2})(\sigma>0)</equation>的简单随机样本. 记统计量<equation>T=\frac{1}{n}\sum_{i=1}^{n} X_{i}^{2}</equation>，则 E(T) = ___.

**答案:**#<equation>\sigma^{2}+\mu^{2}.</equation>

**解析:**由期望的性质可知，<equation>\begin{array}{l} E (T) = \frac {1}{n} E \left(\sum_ {i = 1} ^ {n} X _ {i} ^ {2}\right) = \frac {1}{n} \sum_ {i = 1} ^ {n} E \left(X _ {i} ^ {2}\right) = \frac {1}{n} \cdot n E \left(X ^ {2}\right) = E \left(X ^ {2}\right) \\ = D (X) + \left[ E (X) \right] ^ {2} = \sigma^ {2} + \mu^ {2}. \\ \end{array}</equation>

---

**2009年第14题 | 填空题 | 4分**

14. 设<equation>X_{1}, X_{2}, \cdots, X_{n}</equation>为来自二项分布总体 B(n,p)的简单随机样本，<equation>\bar{X}</equation>和<equation>S^{2}</equation>分别为样本均值和样本方差. 记统计量<equation>T=\bar{X}-S^{2}</equation>，则 E(T) = ___.

**解析:**解 由于 X ~ B(n,p)，故 E(X) = np，D(X) = np(1-p).于是 E<equation>\overline{{{X}}}</equation>= E(X) = np，<equation>E(S^{2})= D(X)=np(1-p).</equation>因此，<equation>E (T) = E \left(\bar {X} - S ^ {2}\right) = E \left(\bar {X}\right) - E \left(S ^ {2}\right) = n p - n p (1 - p) = n p ^ {2}.</equation>

---


### 大数定律和中心极限定理

**2022年第9题 | 选择题 | 5分 | 答案: B**

9. 设随机变量序列<equation>X_{1}, X_{2}, \dots , X_{n}, \dots</equation>独立同分布，且<equation>X_{1}</equation>的概率密度为<equation>f(x)=\left\{\begin{array}{ll}1-|x|,&|x|<1,\\0,&\text{其他},\end{array}\right.</equation>则当 n<equation>\to\infty</equation>时，<equation>\frac{1}{n}\sum_{i=1}^{n}X_{i}^{2}</equation>依概率收敛于（    )

A.<equation>\frac{1}{8}</equation>B.<equation>\frac{1}{6}</equation>C.<equation>\frac{1}{3}</equation>D.<equation>\frac{1}{2}</equation>

答案: B

**解析:**解 由于随机变量序列<equation>X_{1}, X_{2}, \dots, X_{n}, \dots</equation>独立同分布，故<equation>X_{1}^{2}, X_{2}^{2}, \dots, X_{n}^{2}, \dots</equation>独立同分布.根据辛钦大数定律，<equation>\frac{1}{n}\sum_{i=1}^{n}X_{i}^{2}</equation>依概率收敛于<equation>E \left( X_{i}^{2} \right).</equation><equation>\begin{array}{l} E \left(X _ {i} ^ {2}\right) = E \left(X _ {1} ^ {2}\right) = \int_ {- \infty} ^ {+ \infty} x ^ {2} f (x) \mathrm {d} x = \int_ {- 1} ^ {1} x ^ {2} (1 - | x |) \mathrm {d} x \xlongequal {\text {对称性}} 2 \int_ {0} ^ {1} x ^ {2} (1 - x) \mathrm {d} x \\ = 2 \left(\frac {x ^ {3}}{3} - \frac {x ^ {4}}{4}\right) \Bigg | _ {0} ^ {1} = \frac {1}{6}. \\ \end{array}</equation>因此，应选B.

---


### 参数估计

**2022年第22题 | 解答题 | 12分**


设<equation>X_{1}, X_{2}, \dots, X_{n}</equation>为来自均值为<equation>\theta</equation>的指数分布总体的简单随机样本，<equation>Y_{1}, Y_{2}, \dots, Y_{m}</equation>为来自均值为2<equation>\theta</equation>的指数分布总体的简单随机样本，且两样本相互独立，其中<equation>\theta(\theta>0)</equation>是未知参数。利用样本<equation>X_{1}, X_{2}, \dots, X_{n}, Y_{1}, Y_{2}, \dots, Y_{m}</equation>求<equation>\theta</equation>的最大似然估计量<equation>\hat{\theta}</equation>，并求<equation>D(\hat{\theta})</equation>

**答案:**<equation>\hat {\theta} = \frac {2 \sum_ {i = 1} ^ {n} X _ {i} + \sum_ {j = 1} ^ {m} Y _ {j}}{2 (m + n)}, D (\hat {\theta}) = \frac {\theta^ {2}}{m + n}.</equation>

**解析:**解<equation>X_{1}, X_{2}, \dots , X_{n}</equation>是来自总体 X的简单随机样本.由于<equation>E ( X )=\theta</equation>，故 X服从参数为<equation>\frac{1}{\theta}</equation>的指数分布.于是，X的概率密度函数为<equation>f _ {X} (x) = \left\{ \begin{array}{l l} \frac {1}{\theta} \mathrm {e} ^ {- \frac {x}{\theta}}, & x > 0, \\ 0, & x \leqslant 0. \end{array} \right.</equation><equation>Y_{1}, Y_{2}, \dots , Y_{m}</equation>是来自总体Y的简单随机样本.由于<equation>E(Y)=2\theta</equation>，故Y服从参数为<equation>\frac{1}{2\theta}</equation>的指数分布.于是，Y的概率密度函数为<equation>f _ {Y} (y) = \left\{ \begin{array}{l l} \frac {1}{2 \theta} \mathrm {e} ^ {- \frac {y}{2 \theta}}, & y > 0, \\ 0, & y \leqslant 0. \end{array} \right.</equation>设<equation>x_{1}, x_{2}, \dots , x_{n}, y_{1}, y_{2}, \dots , y_{m}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots , X_{n}, Y_{1}, Y_{2}, \dots , Y_{m}</equation>的一组样本值，则似然函数<equation>L (\theta) = \left\{ \begin{array}{l l} \frac {1}{2 ^ {m} \theta^ {m + n}} \mathrm {e} ^ {- \frac {\sum_ {i = 1} ^ {n} x _ {i}}{\theta}} - \frac {\sum_ {i = 1} ^ {m} y _ {j}}{2 \theta}, & x _ {i} > 0, y _ {j} > 0, i = 1, 2, \dots , n, j = 1, 2, \dots , m, \\ 0, & \text {其 他}. \end{array} \right.</equation>当<equation>x_{i} > 0, y_{j} > 0, i = 1, 2, \dots , n, j = 1, 2, \dots , m</equation>时，取对数得<equation>\ln L (\theta) = - m \ln 2 - (m + n) \ln \theta - \frac {\sum_ {i = 1} ^ {n} x _ {i}}{\theta} - \frac {\sum_ {j = 1} ^ {m} y _ {j}}{2 \theta}.</equation>令<equation>\frac{\mathrm{d}\left[\ln L(\theta)\right]}{\mathrm{d}\theta}=0</equation>即<equation>-\frac{m+n}{\theta}+\frac{\sum_{i=1}^{n}x_{i}}{\theta^{2}}+\frac{\sum_{j=1}^{m}y_{j}}{2\theta^{2}}=0</equation>解得<equation>\theta=\frac{2\sum_{i=1}^{n}x_{i}+\sum_{j=1}^{m}y_{j}}{2(m+n)}</equation>因此，<equation>\theta</equation>的最大似然估计量<equation>\hat{\theta}=\frac{2\sum_{i=1}^{n}X_{i}+\sum_{j=1}^{m}Y_{j}}{2(m+n)}</equation>下面计算<equation>D(\hat{\theta})</equation><equation>\begin{aligned} D (\hat {\theta}) &= D \left[ \frac {2 \sum_ {i = 1} ^ {n} X _ {i} + \sum_ {j = 1} ^ {m} Y _ {j}}{2 (m + n)} \right] = \frac {1}{(m + n) ^ {2}} D \left(\sum_ {i = 1} ^ {n} X _ {i}\right) + \frac {1}{4 (m + n) ^ {2}} D \left(\sum_ {j = 1} ^ {m} Y _ {j}\right) \\ &= \frac {1}{(m + n) ^ {2}} \sum_ {i = 1} ^ {n} D \left(X _ {i}\right) + \frac {1}{4 (m + n) ^ {2}} \sum_ {j = 1} ^ {m} D \left(Y _ {j}\right) = \frac {n D (X)}{(m + n) ^ {2}} + \frac {m D (Y)}{4 (m + n) ^ {2}} \\ &= \frac {n \theta^ {2}}{(m + n) ^ {2}} + \frac {m \cdot 4 \theta^ {2}}{4 (m + n) ^ {2}} = \frac {\theta^ {2}}{m + n}. \end{aligned}</equation>或者，注意到<equation>\hat{\theta}=\frac{2\sum_{i=1}^{n}X_{i}+\sum_{j=1}^{m}Y_{j}}{2(m+n)}=\frac{2n\overline{X}+m\overline{Y}}{2(m+n)},</equation>利用<equation>D(\overline{X})=\frac{D(X)}{n}, D(\overline{Y})=\frac{D(Y)}{m}</equation>可得，<equation>\begin{array}{l} D (\hat {\theta}) = D \left[ \frac {2 n \bar {X} + m \bar {Y}}{2 (m + n)} \right] = \frac {n ^ {2} D (\bar {X})}{(m + n) ^ {2}} + \frac {m ^ {2} D (\bar {Y})}{4 (m + n) ^ {2}} \\ = \frac {n ^ {2}}{(m + n) ^ {2}} \cdot \frac {D (X)}{n} + \frac {m ^ {2}}{4 (m + n) ^ {2}} \cdot \frac {D (Y)}{m} \\ = \frac {n \theta^ {2}}{(m + n) ^ {2}} + \frac {m \cdot 4 \theta^ {2}}{4 (m + n) ^ {2}} = \frac {\theta^ {2}}{m + n}. \\ \end{array}</equation>

---

**2021年第10题 | 选择题 | 5分 | 答案: A**

10. 设总体 X的概率分布为<equation>P\{X=1\}=\frac{1-\theta}{2}, P\{X=2\}=P\{X=3\}=\frac{1+\theta}{4}</equation>，利用来自总体的样本值1,3,2,2,1,3,1,2可得<equation>\theta</equation>的最大似然估计值为（    ）

A.<equation>\frac{1}{4}</equation>B.<equation>\frac{3}{8}</equation>C.<equation>\frac{1}{2}</equation>D.<equation>\frac{5}{8}</equation>

答案: A

**解析:**解记<equation>P \{ X=i \}=p_{i}, i=1,2,3.</equation>由于样本值中1出现3次，2出现3次，3出现2次，故似然函数<equation>L (\theta) = p _ {1} ^ {3} p _ {2} ^ {3} p _ {3} ^ {2} = \left(\frac {1 - \theta}{2}\right) ^ {3} \left(\frac {1 + \theta}{4}\right) ^ {5} = \frac {1}{2 ^ {1 3}} (1 - \theta) ^ {3} (1 + \theta) ^ {5}.</equation>计算<equation>\ln L(\theta)</equation>得，<equation>\ln L (\theta) = - 1 3 \ln 2 + 3 \ln (1 - \theta) + 5 \ln (1 + \theta).</equation>计算<equation>\frac{\mathrm{d}\left[\ln L(\theta)\right]}{\mathrm{d}\theta}</equation>得，<equation>\frac {\mathrm {d} [ \ln L (\theta) ]}{\mathrm {d} \theta} = \frac {- 3}{1 - \theta} + \frac {5}{1 + \theta}.</equation>令<equation>\frac{\mathrm{d}[\ln L(\theta)]}{\mathrm{d}\theta}=0</equation>，可得<equation>\frac{5}{1+\theta}=\frac{3}{1-\theta}</equation>，即<equation>5(1-\theta)=3(1+\theta).</equation>，解得<equation>\theta=\frac{1}{4}.</equation>因此，应选A.

