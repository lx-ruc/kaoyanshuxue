<table border="1"><tr><td>Z1Z2</td><td>0</td><td>1</td></tr><tr><td>0</td><td><equation>\frac{1}{4}</equation></td><td>0</td></tr><tr><td>1</td><td><equation>\frac{1}{2}</equation></td><td><equation>\frac{1}{4}</equation></td></tr></table>

（Ⅱ）由<equation>Z_{1}, Z_{2}</equation>的联合分布律可知，<equation>P \left\{Z _ {1} = 0 \right\} = \frac {3}{4}, \quad P \left\{Z _ {1} = 1 \right\} = \frac {1}{4};</equation><equation>P \left\{Z _ {2} = 0 \right\} = \frac {1}{4}, \quad P \left\{Z _ {2} = 1 \right\} = \frac {3}{4};</equation><equation>P \left\{Z _ {1} Z _ {2} = 0 \right\} = \frac {3}{4}, \quad P \left\{Z _ {1} Z _ {2} = 1 \right\} = \frac {1}{4}.</equation>于是<equation>E ( Z_{1} )=\frac{1}{4}, E ( Z_{1}^{2} )=\frac{1}{4}, D ( Z_{1} )=\frac{3}{1 6}; E ( Z_{2} )=\frac{3}{4}, E ( Z_{2}^{2} )=\frac{3}{4}, D ( Z_{2} )=\frac{3}{1 6};</equation><equation>E ( Z_{1} Z_{2} )=\frac{1}{4}.</equation>从而<equation>\operatorname {C o v} \left(Z _ {1}, Z _ {2}\right) = E \left(Z _ {1} Z _ {2}\right) - E \left(Z _ {1}\right) E \left(Z _ {2}\right) = \frac {1}{4} - \frac {1}{4} \times \frac {3}{4} = \frac {1}{1 6}.</equation>因此，<equation>Z_{1}</equation>与<equation>Z_{2}</equation>的相关系数<equation>\rho_ {Z _ {1} Z _ {2}} = \frac {\operatorname {C o v} \left(Z _ {1} , Z _ {2}\right)}{\sqrt {D \left(Z _ {1}\right)} \sqrt {D \left(Z _ {2}\right)}} = \frac {\frac {1}{1 6}}{\sqrt {\frac {3}{1 6} \times \frac {3}{1 6}}} = \frac {1}{3}.</equation>

---

**2018年第22题 | 解答题 | 11分**

22. (本题满分11分)

设随机变量 X与 Y相互独立，X的概率分布为<equation>P\{X=1\}=P\{X=-1\}=\frac{1}{2},</equation>Y服从参数为<equation>\lambda</equation>的泊松分布. 令<equation>Z=XY</equation>.

I. 求<equation>\operatorname{Cov}(X,Z)</equation>;

II. 求 Z的概率分布.

**答案:**(I)<equation>\operatorname{C o v} ( X, Z )=\lambda</equation>;

（Ⅱ）Z的分布律为<equation>P\{Z = i\} = \left\{ \begin{array}{ll}\frac{1}{2}\cdot \frac{\lambda^{i}\mathrm{e}^{- \lambda}}{i!}, & i > 0,\\ \mathrm{e}^{- \lambda}, & i = 0,\\ \frac{1}{2}\cdot \frac{\lambda^{-i}\mathrm{e}^{- \lambda}}{(-i)!}, & i < 0. \end{array} \right.</equation>

**解析:**解（I）（法一）注意到 X与 Y相互独立，故<equation>X^{2}</equation>与 Y也相互独立根据协方差的计算公式，<equation>\begin{array}{l} \operatorname {C o v} (X, Z) = E (X Z) - E (X) E (Z) \stackrel {Z = X Y} {=} E \left(X ^ {2} Y\right) - E (X) E (X Y) \\ \underline {{\underline {{\text {独立性}}}}} E \left(X ^ {2}\right) E (Y) - \left[ E (X) \right] ^ {2} E (Y). \\ \end{array}</equation>由于 X的概率分布为 P<equation>\{ X=1\}=P\{ X=-1\}=\frac{1}{2}</equation>，故<equation>E (X) = 1 \times \frac {1}{2} + (- 1) \times \frac {1}{2} = 0, \quad E \left(X ^ {2}\right) = 1 ^ {2} \times \frac {1}{2} + (- 1) ^ {2} \times \frac {1}{2} = 1.</equation>又因为<equation>Y</equation>服从参数为<equation>\lambda</equation>的泊松分布，所以<equation>E(Y) = \lambda</equation>因此，<equation>\operatorname {C o v} (X, Z) = E \left(X ^ {2}\right) E (Y) - \left[ E (X) \right] ^ {2} E (Y) = 1 \times \lambda - 0 = \lambda .</equation>（法二）由于<equation>X^{2}=1</equation>，故<equation>XZ=X(XY)=X^{2}Y=Y</equation>，而Y服从参数为<equation>\lambda</equation>的泊松分布，于是，<equation>E(XZ)=E(Y)=\lambda.</equation>由法一可知，<equation>E ( X ) = 0</equation>因此，<equation>\operatorname {C o v} (X, Z) = E (X Z) - E (X) E (Z) = \lambda - 0 = \lambda .</equation>（Ⅱ）由于<equation>Z=XY</equation>，故Z的所有可能的取值为i，其中i为整数.

当 i > 0时，<equation>\begin{aligned} P \{Z = i \} &= P \{X Y = i \} = P \{X = 1, Y = i \} \xlongequal {\text {独立性}} P \{X = 1 \} P \{Y = i \} \\ &= \frac {1}{2} \cdot \frac {\lambda^ {i} \mathrm {e} ^ {- \lambda}}{i !}. \end{aligned}</equation>当 i = 0时，<equation>P \{Z = 0 \} = P \{X Y = 0 \} \xlongequal {X \text {不 为} 0} P \{Y = 0 \} = \mathrm {e} ^ {- \lambda}.</equation>当 i < 0时，<equation>\begin{aligned} P \{Z = i \} &= P \{X Y = i \} = P \{X = - 1, Y = - i \} \xlongequal {\text {独立性}} P \{X = - 1 \} P \{Y = - i \} \\ &= \frac {1}{2} \cdot \frac {\lambda^ {- i} \mathrm {e} ^ {- \lambda}}{(- i) !}. \end{aligned}</equation>因此，<equation>Z</equation>的分布律为<equation>P\{Z = i\} = \left\{ \begin{array}{ll} \frac{1}{2} \cdot \frac{\lambda^{i}\mathrm{e}^{-\lambda}}{i!}, & i > 0, \\ \mathrm{e}^{-\lambda}, & i = 0, \\ \frac{1}{2} \cdot \frac{\lambda^{-i}\mathrm{e}^{-\lambda}}{(-i)!}, & i < 0. \end{array} \right.</equation>

---

**2014年第23题 | 解答题 | 11分**


设随机变量 X,Y的概率分布相同，X的概率分布为<equation>P\{X=0\}=\frac{1}{3},P\{X=1\}=\frac{2}{3}</equation>，且 X与 Y的相关系数<equation>\rho_{XY}=\frac{1}{2}.</equation>I. 求 (X,Y)的概率分布；

II. 求<equation>P\{X+Y\leqslant1\}.</equation>

**答案:**(23) （I）<equation>( X, Y )</equation>的概率分布为

（Ⅱ）<equation>\frac{4}{9}.</equation><table border="1"><tr><td>X

Y</td><td>0</td><td>1</td></tr><tr><td>0</td><td><equation>\frac{2}{9}</equation></td><td><equation>\frac{1}{9}</equation></td></tr><tr><td>1</td><td><equation>\frac{1}{9}</equation></td><td><equation>\frac{5}{9}</equation></td></tr></table>

**解析:**（ I ）设<equation>P \{ X=0, Y=0 \}=p</equation>，则<equation>P \{X = 0, Y = 1 \} = P \{X = 0 \} - P \{X = 0, Y = 0 \} = \frac {1}{3} - p,</equation><equation>P \{X = 1, Y = 0 \} = P \{Y = 0 \} - P \{X = 0, Y = 0 \} = \frac {1}{3} - p,</equation><equation>P \{X = 1, Y = 1 \} = P \{X = 1 \} - P \{X = 1, Y = 0 \} = \frac {2}{3} - \left(\frac {1}{3} - p\right) = \frac {1}{3} + p,</equation>即（X，Y）的概率分布为

<table border="1"><tr><td rowspan="2">X

Y</td><td>0</td><td>1</td></tr><tr><td>p</td><td><equation>\frac{1}{3}-p</equation></td></tr><tr><td>1</td><td><equation>\frac{1}{3}-p</equation></td><td><equation>\frac{1}{3}+p</equation></td></tr></table>

由于变量 XY可能的值为0，1，故<equation>E (X Y) = 0 \cdot P \{X Y = 0 \} + 1 \cdot P \{X Y = 1 \} = P \{X = 1, Y = 1 \} = \frac {1}{3} + p.</equation>又因为<equation>E (X) = E (Y) = 0 \times \frac {1}{3} + 1 \times \frac {2}{3} = \frac {2}{3},</equation><equation>E \left(X ^ {2}\right) = E \left(Y ^ {2}\right) = 0 ^ {2} \times \frac {1}{3} + 1 ^ {2} \times \frac {2}{3} = \frac {2}{3},</equation>所以<equation>D (X) = D (Y) = E \left(Y ^ {2}\right) - \left[ E (Y) \right] ^ {2} = \frac {2}{9}.</equation>于是，<equation>\rho_ {X Y} = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {p - \frac {1}{9}}{\frac {2}{9}} = \frac {1}{2}.</equation>解得<equation>p = \frac{2}{9}</equation>因此，<equation>(X, Y)</equation>的概率分布为

<table border="1"><tr><td>X

Y</td><td>0</td><td>1</td></tr><tr><td>0</td><td><equation>\frac{2}{9}</equation></td><td><equation>\frac{1}{9}</equation></td></tr><tr><td>1</td><td><equation>\frac{1}{9}</equation></td><td><equation>\frac{5}{9}</equation></td></tr></table>

（Ⅱ）（法一）<equation>P\{X + Y\leqslant 1\} = 1 - P\{X + Y > 1\} = 1 - P\{X = 1, Y = 1\} = 1 - \frac{5}{9} = \frac{4}{9}.</equation>(二)<equation>P \{ X + Y \leqslant 1 \} = P \{ X = 0, Y = 0 \} + P \{ X = 0, Y = 1 \} + P \{ X = 1, Y = 0 \}</equation><equation>= \frac{2}{9} +\frac{1}{9} +\frac{1}{9} = \frac{4}{9}.</equation>（法二）

---

**2012年第22题 | 解答题 | 11分**


设二维离散型随机变量<equation>(X, Y)</equation>的概率分布为

<table border="1"><tr><td>X\ Y</td><td>0</td><td>1</td><td>2</td></tr><tr><td>0</td><td>1/4</td><td>0</td><td>1/4</td></tr><tr><td>1</td><td>0</td><td>1/3</td><td>0</td></tr><tr><td>2</td><td>1/12</td><td>0</td><td>1/12</td></tr></table>

I. 求<equation>P\{X=2Y\}</equation>;

II. 求<equation>\operatorname{Cov}(X-Y,Y).</equation>

**答案:**(22) (I)<equation>\frac{1}{4}</equation>;<equation>(\mathrm {I I}) - \frac {2}{3}.</equation>

**解析:**（I）由题设知，<equation>P \{X = 2 Y \} = P \{X = 0, Y = 0 \} + P \{X = 2, Y = 1 \} = \frac {1}{4} + 0 = \frac {1}{4}.</equation>（Ⅱ）由<equation>(X,Y)</equation>的概率分布知，<equation>X,Y</equation>的概率分布分别为

<table border="1"><tr><td>X</td><td>0</td><td>1</td><td>2</td></tr><tr><td>P</td><td><equation>\frac{1}{2}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{6}</equation></td></tr></table>

<table border="1"><tr><td>Y</td><td>0</td><td>1</td><td>2</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td></tr></table>

又由于随机变量 XY可能的值为0，1，2，4，故XY的概率分布为<equation>\begin{aligned} P \{X Y = 0 \} &= P \{X = 0, Y = 0 \} + P \{X = 0, Y = 1 \} + P \{X = 0, Y = 2 \} \\ + P \{X = 1, Y = 0 \} + P \{X = 2, Y = 0 \} \\ &= \frac {1}{4} + 0 + \frac {1}{4} + 0 + \frac {1}{1 2} = \frac {7}{1 2}, \end{aligned}</equation><equation>P \{X Y = 1 \} = P \{X = 1, Y = 1 \} = \frac {1}{3},</equation><equation>P \{X Y = 2 \} = P \{X = 1, Y = 2 \} + P \{X = 2, Y = 1 \} = 0 + 0 = 0,</equation><equation>P \{X Y = 4 \} = P \{X = 2, Y = 2 \} = \frac {1}{1 2},</equation>即

<table border="1"><tr><td>XY</td><td>0</td><td>1</td><td>4</td></tr><tr><td>P</td><td><equation>\frac{7}{12}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{12}</equation></td></tr></table>

于是，<equation>E (X) = 0 \times \frac {1}{2} + 1 \times \frac {1}{3} + 2 \times \frac {1}{6} = \frac {2}{3},</equation><equation>E (Y) = 0 \times \frac {1}{3} + 1 \times \frac {1}{3} + 2 \times \frac {1}{3} = 1,</equation><equation>E \left(Y ^ {2}\right) = 0 ^ {2} \times \frac {1}{3} + 1 ^ {2} \times \frac {1}{3} + 2 ^ {2} \times \frac {1}{3} = \frac {5}{3},</equation><equation>E (X Y) = 0 \times \frac {7}{1 2} + 1 \times \frac {1}{3} + 4 \times \frac {1}{1 2} = \frac {2}{3}.</equation>因此，<equation>\begin{aligned} \operatorname {C o v} (X - Y, Y) &= \operatorname {C o v} (X, Y) - \operatorname {C o v} (Y, Y) = \left[ E (X Y) - E (X) E (Y) \right] - \left[ E \left(Y ^ {2}\right) - \left[ E (Y) \right] ^ {2} \right] \\ &= \left(\frac {2}{3} - \frac {2}{3} \times 1\right) - \left(\frac {5}{3} - 1 ^ {2}\right) = - \frac {2}{3}. \end{aligned}</equation>

---

**2011年第22题 | 解答题 | 11分**


设随机变量<equation>X</equation>与<equation>Y</equation>的概率分布分别为

<table border="1"><tr><td>X</td><td>0</td><td>1</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{2}{3}</equation></td></tr></table>

<table border="1"><tr><td>Y</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td></tr></table>

且<equation>P\{X^{2}=Y^{2}\}=1.</equation>I. 求二维随机变量<equation>(X, Y)</equation>的概率分布；

II. 求<equation>Z=XY</equation>的概率分布；

III. 求 X与Y的相关系数<equation>\rho_{XY}</equation>

**答案:**(22) （I）<equation>( X, Y )</equation>的概率分布为

<table border="1"><tr><td rowspan="2">X\ Y</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>0</td><td><equation>\frac{1}{3}</equation></td><td>0</td></tr><tr><td>1</td><td><equation>\frac{1}{3}</equation></td><td>0</td><td><equation>\frac{1}{3}</equation></td></tr></table>

（Ⅱ）<equation>Z=XY</equation>的概率分布为

<table border="1"><tr><td>Z</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td></tr></table>

（Ⅲ）0.

**解析:**解（I）由<equation>P\{X^{2}=Y^{2}\}=1</equation>知，<equation>P\{X^{2}\neq Y^{2}\}=0.</equation>于是，<equation>P \{X = 0, Y = - 1 \} = P \{X = 0, Y = 1 \} = P \{X = 1, Y = 0 \} = 0.</equation>从而<equation>P \{X = 0, Y = 0 \} = P \{Y = 0 \} - P \{X = 1, Y = 0 \} = \frac {1}{3} - 0 = \frac {1}{3},</equation><equation>P \{X = 1, Y = 1 \} = P \{Y = 1 \} - P \{X = 0, Y = 1 \} = \frac {1}{3} - 0 = \frac {1}{3},</equation><equation>P \{X = 1, Y = - 1 \} = P \{Y = - 1 \} - P \{X = 0, Y = - 1 \} = \frac {1}{3} - 0 = \frac {1}{3}.</equation>因此，<equation>(X, Y)</equation>的概率分布为

<table border="1"><tr><td>X\ Y</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>0</td><td><equation>\frac{1}{3}</equation></td><td>0</td></tr><tr><td>1</td><td><equation>\frac{1}{3}</equation></td><td>0</td><td><equation>\frac{1}{3}</equation></td></tr></table>

（Ⅱ）由于<equation>Z=XY</equation>可能的取值为-1，0，1，且<equation>P \{Z = - 1 \} = P \{X = 1, Y = - 1 \} = \frac {1}{3},</equation><equation>P \{Z = 1 \} = P \{X = 1, Y = 1 \} = \frac {1}{3},</equation><equation>P \{Z = 0 \} = 1 - P \{Z = - 1 \} - P \{Z = 1 \} = \frac {1}{3},</equation>（或者<equation>P\{Z = 0\} = P\{X = 0, Y = 0\} + P\{X = 0, Y = -1\} + P\{X = 0, Y = 1\} + P\{X = 1, Y = 0\} = \frac{1}{3},</equation>）故<equation>Z = X Y</equation>的概率分布为

<table border="1"><tr><td>Z</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td></tr></table><equation>E (X) = 0 \times \frac {1}{3} + 1 \times \frac {2}{3} = \frac {2}{3}, \quad E \left(X ^ {2}\right) = 0 ^ {2} \times \frac {1}{3} + 1 ^ {2} \times \frac {2}{3} = \frac {2}{3},</equation>（Ⅲ）由于<equation>D (X) = E \left(X ^ {2}\right) - \left[ E (X) \right] ^ {2} = \frac {2}{9},</equation><equation>E (Y) = (- 1) \times \frac {1}{3} + 0 \times \frac {1}{3} + 1 \times \frac {1}{3} = 0, \quad E \left(Y ^ {2}\right) = (- 1) ^ {2} \times \frac {1}{3} + 0 ^ {2} \times \frac {1}{3} + 1 ^ {2} \times \frac {1}{3} = \frac {2}{3},</equation><equation>D (Y) = E \left(Y ^ {2}\right) - \left[ E (Y) \right] ^ {2} = \frac {2}{3},</equation><equation>E (X Y) = E (Z) = (- 1) \times \frac {1}{3} + 0 \times \frac {1}{3} + 1 \times \frac {1}{3} = 0,</equation>故<equation>\rho_ {X Y} = \frac {\operatorname {C o v} (X , Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = 0.</equation>

---

**2017年第22题 | 解答题 | 11分**


设随机变量 X，Y相互独立，且 X的概率分布为<equation>P\{X=0\}=P\{X=2\}=\frac{1}{2},</equation>Y的概率密度为<equation>f (y) = \left\{ \begin{array}{l l} 2 y, & 0 < y < 1, \\ 0, & \text {其 他}. \end{array} \right.</equation>I. 求<equation>P\{Y\leqslant E(Y)\} ;</equation>II. 求<equation>Z=X+Y</equation>的概率密度

**答案:**<equation>\frac {4}{9};</equation>（Ⅱ）<equation>f_{Z}(z)=\left\{ \begin{array}{ll} z, & 0<z<1,\\ z-2, & 2<z<3,\\ 0, & \text{其他}. \end{array} \right.</equation>

**解析:**解（I）由题设知，<equation>E ( Y )=\int_{-\infty}^{+\infty} y f ( y ) \mathrm{d} y=\int_{0}^{1} 2 y^{2} \mathrm{d} y=\frac{2}{3}.</equation>因此，<equation>P \left\{Y \leqslant E (Y) \right\} = P \left\{Y \leqslant \frac {2}{3} \right\} = \int_ {0} ^ {\frac {2}{3}} 2 y \mathrm {d} y = \frac {4}{9}.</equation>（Ⅱ）Z的分布函数为<equation>\begin{aligned} F _ {Z} (z) &= P \{Z \leqslant z \} = P \{X + Y \leqslant z \} \\ &= P \{X + Y \leqslant z, X = 0 \} + P \{X + Y \leqslant z, X = 2 \} \\ &= P \{Y \leqslant z, X = 0 \} + P \{Y \leqslant z - 2, X = 2 \} \\ \underline {{\underline {{X , Y \text {相 互 独立}}}}} P \{Y \leqslant z \} \cdot P \{X = 0 \} + P \{Y \leqslant z - 2 \} \cdot P \{X = 2 \} \\ &= \frac {1}{2} P \{Y \leqslant z \} + \frac {1}{2} P \{Y \leqslant z - 2 \}. \end{aligned}</equation>下面用两种方法求 Z的概率密度.

（法一）如图所示，当<equation>z\leqslant 0</equation>时，<equation>F_{z}(z) = 0 + 0 = 0.</equation>当<equation>0 < z\leqslant 1</equation>时，<equation>F_{Z}(z) = \frac{1}{2}\int_{0}^{z}2y\mathrm{d}y + 0 = \frac{z^{2}}{2}.</equation>当<equation>1 < z\leqslant 2</equation>时，<equation>F_{z}(z) = \frac{1}{2}\int_{0}^{1}2y\mathrm{d}y + 0 = \frac{1}{2}</equation>.

当<equation>2 < z\leqslant 3</equation>时，<equation>F_{z}(z) = \frac{1}{2} +\frac{1}{2}\int_{0}^{z - 2}2y\mathrm{d}y = \frac{1}{2} +\frac{(z - 2)^{2}}{2}.</equation>当<equation>z > 3</equation>时，<equation>F_{Z}(z) = 1.</equation>综上所述，Z的概率密度为<equation>f _ {Z} (z) = F _ {Z} ^ {\prime} (z) = \left\{ \begin{array}{l l} z, & 0 < z < 1, \\ z - 2, & 2 < z < 3, \\ 0, & \text {其 他}. \end{array} \right.</equation>（法二）由 Z的分布函数<equation>F_{Z}(z)=\frac{1}{2} P\{Y\leqslant z\} +\frac{1}{2} P\{Y\leqslant z-2\}</equation>知，Z的概率密度为<equation>f _ {Z} (z) = F _ {Z} ^ {\prime} (z) = \frac {1}{2} f (z) + \frac {1}{2} f (z - 2).</equation>当<equation>z\leqslant 0</equation>时，<equation>z - 2\leqslant 0,f_{z}(z) = 0 + 0 = 0.</equation>当<equation>0 < z < 1</equation>时，<equation>z-2\leqslant 0,f_{Z}(z)=\frac{1}{2}\cdot 2z+0=z.</equation>当<equation>1\leqslant z\leqslant 2</equation>时，<equation>z - 2\leqslant 0,f_{z}(z) = 0 + 0 = 0.</equation>当<equation>2 < z < 3</equation>时，<equation>0 < z - 2 < 1,f_{Z}(z) = 0 + \frac{1}{2}\cdot 2(z - 2) = z - 2.</equation>当<equation>z\geqslant 3</equation>时，<equation>z - 2\geqslant 1,f_{Z}(z) = 0 + 0 = 0.</equation>综上所述，<equation>f_{Z}(z)=\left\{ \begin{array}{ll} z, & 0<z<1,\\ z-2, & 2<z<3,\\ 0, & \text{其他}. \end{array} \right.</equation>

---

**2016年第8题 | 选择题 | 4分 | 答案: C**

8. 设随机变量 X与 Y相互独立，且<equation>X\sim N(1,2),Y\sim N(1,4)</equation>，则<equation>D(XY)=</equation>(    )

A.6 B.8 C.14 D.15

答案: C

**解析:**解 由于<equation>X\sim N(1,2), Y\sim N(1,4)</equation>，故<equation>E(X)=E(Y)=1,D(X)=2,D(Y)=4.</equation>又由于随机变量 X与 Y相互独立，故<equation>X^{2}</equation>与<equation>Y^{2}</equation>也相互独立.于是，<equation>\begin{array}{l} E \left(X ^ {2} Y ^ {2}\right) = E \left(X ^ {2}\right) E \left(Y ^ {2}\right) = \left\{\left[ E (X) \right] ^ {2} + D (X) \right\} \left\{\left[ E (Y) \right] ^ {2} + D (Y) \right\} \\ = (1 + 2) (1 + 4) = 1 5, \\ \end{array}</equation><equation>E (X Y) = E (X) E (Y) = 1.</equation>因此，<equation>D (X Y) = E \left(X ^ {2} Y ^ {2}\right) - \left[ E (X Y) \right] ^ {2} = 1 5 - 1 = 1 4.</equation>应选C.

---


**2010年第23题 | 解答题 | 11分**


23. (本题满分11分)

箱中装有6个球，其中红、白、黑球的个数分别为1,2,3个. 现从箱中随机地取出2个球，记X为取出的红球个数，Y为取出的白球个数.

I. 求随机变量（X，Y）的概率分布；

II. 求<equation>\operatorname{C o v} ( X, Y ).</equation>

**答案:**(23) （I）随机变量<equation>(X, Y)</equation>的概率分布为

<table border="1"><tr><td rowspan="2">X\ Y</td><td>0</td><td>1</td><td>2</td></tr><tr><td><equation>\frac{1}{5}</equation></td><td><equation>\frac{2}{5}</equation></td><td><equation>\frac{1}{15}</equation></td></tr><tr><td>1</td><td><equation>\frac{1}{5}</equation></td><td><equation>\frac{2}{15}</equation></td><td>0</td></tr></table>

（Ⅱ）<equation>- \frac{4}{45}.</equation>

**解析:**解 （I）记Z为取出的黑球个数.由已知条件知X可能的取值为0，1；Y可能的取值为0，1，2.由于<equation>P \{X = 0, Y = 0 \} = P \{Z = 2 \} = \frac {\mathrm {C} _ {3} ^ {2}}{\mathrm {C} _ {6} ^ {2}} = \frac {1}{5},</equation><equation>P \{X = 0, Y = 1 \} = P \{Y = 1, Z = 1 \} = \frac {\mathrm {C} _ {2} ^ {1} \mathrm {C} _ {3} ^ {1}}{\mathrm {C} _ {6} ^ {2}} = \frac {2}{5},</equation><equation>P \{X = 0, Y = 2 \} = P \{Y = 2 \} = \frac {\mathrm {C} _ {2} ^ {2}}{\mathrm {C} _ {6} ^ {2}} = \frac {1}{1 5},</equation><equation>P \left\{X = 1, Y = 0 \right\} ^ {\prime} = P \left\{X = 1, Z = 1 \right\} = \frac {\mathrm {C} _ {1} ^ {1} \mathrm {C} _ {3} ^ {1}}{\mathrm {C} _ {6} ^ {2}} = \frac {1}{5},</equation><equation>P \left\{X = 1, Y = 1 \right\} = \frac {\mathrm {C} _ {1} ^ {1} \mathrm {C} _ {2} ^ {1}}{\mathrm {C} _ {6} ^ {2}} = \frac {2}{1 5},</equation><equation>P \{X = 1, Y = 2 \} = P (\varnothing) = 0,</equation>故随机变量（X，Y）的概率分布为

<table border="1"><tr><td>X\ Y</td><td>0</td><td>1</td><td>2</td></tr><tr><td>0</td><td><equation>\frac{1}{5}</equation></td><td><equation>\frac{2}{5}</equation></td><td><equation>\frac{1}{15}</equation></td></tr><tr><td>1</td><td><equation>\frac{1}{5}</equation></td><td><equation>\frac{2}{15}</equation></td><td>0</td></tr></table>

（Ⅱ）随机变量 XY可能的取值为0,1.

由于<equation>P \{ X Y=1 \} = P \{ X=1, Y=1 \} = \frac{2}{1 5}</equation>，故<equation>P \{ X Y=0 \} = 1 - P \{ X Y=1 \} = \frac{1 3}{1 5}</equation>（或者利用<equation>P \{ X Y=0 \} = P \{ X=0, Y=0 \} + P \{ X=0, Y=1 \} + P \{ X=0, Y=2 \} + P \{ X=1, Y=0 \} )</equation>.于是，<equation>E (X Y) = 0 \times \frac {1 3}{1 5} + 1 \times \frac {2}{1 5} = \frac {2}{1 5}.</equation>因为<equation>E (X) = 0 \cdot P \{X = 0 \} + 1 \cdot P \{X = 1 \} = P \{X = 1 \} = \frac {2}{1 5} + \frac {1}{5} = \frac {1}{3},</equation><equation>E (Y) = 0 \cdot P \{Y = 0 \} + 1 \cdot P \{Y = 1 \} + 2 \cdot P \{Y = 2 \} = 1 \times \left(\frac {2}{5} + \frac {2}{1 5}\right) + 2 \times \frac {1}{1 5} = \frac {2}{3},</equation>所以<equation>\operatorname {C o v} (X, Y) = E (X Y) - E (X) E (Y) = \frac {2}{1 5} - \frac {1}{3} \times \frac {2}{3} = - \frac {4}{4 5}.</equation>

---

**2011年第23题 | 解答题 | 11分**


设二维随机变量（X，Y）服从区域G上的均匀分布，其中G是由 x-y=0，x+y=2与 y=0所围成的三角形区域.

I. 求 X的概率密度<equation>f_{X}(x)</equation>;

II. 求条件概率密度<equation>f_{X|Y}(x \mid y).</equation>

**答案:**(23) （I）<equation>f_{X}(x)=\left\{\begin{array}{ll}x,&0<x\leqslant 1,\\ 2-x,&1<x\leqslant 2,\\ 0,&\text{其他};\end{array}\right.</equation>（Ⅱ）<equation>f_{X\mid Y}(x\mid y)=\left\{\begin{array}{ll}\frac{1}{2-2y},&y<x<2-y,\\ 0,&\text{其他}.\end{array}\right.</equation>

**解析:**(a)

(b)

(c)

解（I）如图（a）所示，G是一个底为2，高为1的三角形区域，故面积为1.于是二维随机变量 （X，Y）的概率密度为<equation>f (x, y) = \left\{ \begin{array}{l l} 1, & (x, y) \in G, \\ 0, & \text {其 他}, \end{array} \right.</equation>这里<equation>G = \{(x,y) \mid y \leqslant x \leqslant 2 - y, 0 \leqslant y \leqslant 1\}</equation>.

当<equation>x\leqslant 0</equation>时，<equation>f_{X}(x) = \int_{-\infty}^{+\infty}f(x,y)\mathrm{d}y = 0.</equation>当<equation>0 < x\leqslant 1</equation>时，<equation>f_{X}(x) = \int_{- \infty}^{+ \infty} f(x,y)\mathrm{d}y = \int_{0}^{x}1\mathrm{d}y = x.</equation>当<equation>1 < x\leqslant 2</equation>时，<equation>f_{X}(x) = \int_{-\infty}^{+\infty}f(x,y)\mathrm{d}y = \int_{0}^{2 - x}1\mathrm{d}y = 2 - x.</equation>当<equation>x > 2</equation>时，<equation>f_{X}(x) = \int_{- \infty}^{+ \infty} f(x,y)\mathrm{d}y = 0.</equation>综上所述，<equation>X</equation>的概率密度为<equation>f_{X}(x) = \left\{ \begin{array}{ll} x, & 0 < x \leqslant 1, \\ 2 - x, & 1 < x \leqslant 2, \\ 0, & \text{其他}. \end{array} \right.</equation>（Ⅱ）当<equation>0\leqslant y < 1</equation>时，<equation>f_{Y}(y) = \int_{- \infty}^{+ \infty} f(x,y)\mathrm{d}x = \int_{y}^{2 - y}1\mathrm{d}x = 2 - 2y.</equation>当<equation>y < 0</equation>或<equation>y\geqslant 1</equation>时，<equation>f_{Y}(y) = \int_{- \infty}^{+ \infty} f(x,y)\mathrm{d}x = 0.</equation>由于条件概率密度<equation>f_{X|Y}(x|y)</equation>是在Y的取值y满足<equation>f_{Y}(y) > 0</equation>的前提下定义的，故我们只考虑<equation>0\leqslant y < 1</equation>的情形.因此，在<equation>Y=y(0\leqslant y < 1)</equation>时，X的条件概率密度为<equation>f _ {X \mid Y} (x \mid y) = \frac {f (x , y)}{f _ {Y} (y)} = \left\{ \begin{array}{l l} \frac {1}{2 - 2 y}, & y < x < 2 - y, \\ 0, & \text {其 他}. \end{array} \right.</equation>

---

**2010年第22题 | 解答题 | 11分**

22. (本题满分11分)

设二维随机变量（X，Y）的概率密度为<equation>f ( x, y )=A \mathrm{e}^{-2 x^{2}+2 x y-y^{2}}</equation><equation>(-\infty < x < +\infty,-\infty < y < +\infty).</equation>求常数 A及条件概率密度<equation>f_{Y|X}(y\mid x).</equation>

**答案:**(22)<equation>A=\frac{1}{\pi}, f_{Y\mid X}(y\mid x)=\frac{1}{\sqrt{\pi}} \mathrm{e}^{-(x-y)^{2}}, y\in(-\infty ,+\infty).</equation>

**解析:**解 由概率密度的性质可知，<equation>\int_{- \infty}^{+ \infty}\int_{- \infty}^{+ \infty}f(x,y)\mathrm{d}x\mathrm{d}y=1.</equation>由于<equation>\begin{aligned} \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} x \mathrm {d} y &= \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} A \mathrm {e} ^ {- 2 x ^ {2} + 2 x y - y ^ {2}} \mathrm {d} x \mathrm {d} y = \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} A \mathrm {e} ^ {- x ^ {2} - (y - x) ^ {2}} \mathrm {d} x \mathrm {d} y \\ &= A \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- x ^ {2}} \mathrm {d} x \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- (y - x) ^ {2}} \mathrm {d} y = A \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- x ^ {2}} \mathrm {d} x \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- (y - x) ^ {2}} \mathrm {d} (y - x) \\ &= A \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- x ^ {2}} \mathrm {d} x \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t \frac {\int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t = \sqrt {\pi}}{A \pi}, \end{aligned}</equation>故<equation>A\pi = 1</equation>，从而<equation>A = \frac{1}{\pi}</equation>由条件概率密度的定义可知，<equation>f_{Y \mid X}(y \mid x) = \frac{f(x,y)}{f_X(x)}.</equation>又由于<equation>f _ {X} (x) = \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} y = \frac {1}{\pi} \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- 2 x ^ {2} + 2 x y - y ^ {2}} \mathrm {d} y = \frac {1}{\pi} \mathrm {e} ^ {- x ^ {2}} \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- (y - x) ^ {2}} \mathrm {d} y = \frac {1}{\pi} \mathrm {e} ^ {- x ^ {2}} \cdot \sqrt {\pi} = \frac {1}{\sqrt {\pi}} \mathrm {e} ^ {- x ^ {2}},</equation>故对任意给定的<equation>x\in(-\infty , + \infty)</equation>，在<equation>X = x</equation>的条件下，<equation>Y</equation>的条件概率密度为<equation>f _ {Y \mid X} (y \mid x) = \frac {f (x , y)}{f _ {X} (x)} = \frac {\frac {1}{\pi} \mathrm {e} ^ {- 2 x ^ {2} + 2 x y - y ^ {2}}}{\frac {1}{\sqrt {\pi}} \mathrm {e} ^ {- x ^ {2}}} = \frac {1}{\sqrt {\pi}} \mathrm {e} ^ {- x ^ {2} + 2 x y - y ^ {2}} = \frac {1}{\sqrt {\pi}} \mathrm {e} ^ {- (x - y) ^ {2}}, y \in (- \infty , + \infty).</equation>

---

**2009年第22题 | 解答题 | 11分**

22. (本题满分11分)

设二维随机变量（X，Y）的概率密度为 f(x,y) =<equation>\left\{\begin{array}{ll} \mathrm{e}^{-x}, & 0<y<x, \\ 0, & \mathrm{其他}. \end{array} \right.</equation>I. 求条件概率密度<equation>f_{Y|X}(y|x)</equation>II. 求条件概率<equation>P\{X\leqslant1\mid Y\leqslant1\}</equation>

**答案:**（22）（I）当<equation>f_{X}(x)\neq0</equation>，即 x > 0时，<equation>f_{Y\mid X}(y\mid x)=\frac{f(x,y)}{f_{X}(x)}=\left\{\begin{array}{ll}\frac{1}{x},&0<y<x,\\ 0,&\text{其他};\end{array}\right.</equation>（Ⅱ）<equation>\frac{\mathrm{e}-2}{\mathrm{e}-1}.</equation>

**解析:**解（I）由边缘概率密度的定义可知，当<equation>x > 0</equation>时，<equation>f _ {X} (x) = \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} y = \int_ {0} ^ {x} \mathrm {e} ^ {- x} \mathrm {d} y = x \mathrm {e} ^ {- x};</equation>当<equation>x\leqslant 0</equation>时，<equation>f _ {X} (x) = \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} y = 0.</equation>因此，当<equation>f_{X}(x) \neq 0</equation>，即<equation>x > 0</equation>时，<equation>Y</equation>在<equation>X = x</equation>的条件下的条件概率密度为<equation>f _ {Y \mid X} (y \mid x) = \frac {f (x , y)}{f _ {X} (x)} = \left\{ \begin{array}{l l} \frac {1}{x}, & 0 < y < x, \\ 0, & \text {其 他}. \end{array} \right.</equation>（Ⅱ）（法一）由条件概率的定义知<equation>\begin{aligned} P \{X \leqslant 1 \mid Y \leqslant 1 \} &= \frac {P \{X \leqslant 1 , Y \leqslant 1 \}}{P \{Y \leqslant 1 \}} = \frac {\int_ {- \infty} ^ {1} \mathrm {d} x \int_ {- \infty} ^ {1} f (x , y) \mathrm {d} y}{\int_ {- \infty} ^ {+ \infty} \mathrm {d} x \int_ {- \infty} ^ {1} f (x , y) \mathrm {d} y} \stackrel {*} {=} \frac {\int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {x} \mathrm {e} ^ {- x} \mathrm {d} y}{\int_ {0} ^ {1} \mathrm {d} y \int_ {y} ^ {+ \infty} \mathrm {e} ^ {- x} \mathrm {d} x} \\ &= \frac {\int_ {0} ^ {1} x \mathrm {e} ^ {- x} \mathrm {d} x}{\int_ {0} ^ {1} \mathrm {e} ^ {- y} \mathrm {d} y} = \frac {- x \mathrm {e} ^ {- x} \left| _ {0} ^ {1} + \int_ {0} ^ {1} \mathrm {e} ^ {- x} \mathrm {d} x \right.}{- \mathrm {e} ^ {- y} \left| _ {0} ^ {1} \right.} = \frac {1 - 2 \mathrm {e} ^ {- 1}}{1 - \mathrm {e} ^ {- 1}} = \frac {\mathrm {e} - 2}{\mathrm {e} - 1}. \end{aligned}</equation>（法二）由边缘概率密度的定义可知，当<equation>y > 0</equation>时，<equation>f _ {Y} (y) = \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} x = \int_ {y} ^ {+ \infty} \mathrm {e} ^ {- x} \mathrm {d} x = - \mathrm {e} ^ {- x} \Big | _ {y} ^ {+ \infty} = \mathrm {e} ^ {- y};</equation>当 y≤0时，<equation>f _ {Y} (y) = \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} x = 0.</equation>于是，<equation>P \left\{Y \leqslant 1 \right\} = \int_ {- \infty} ^ {1} f _ {Y} (y) \mathrm {d} y = \int_ {0} ^ {1} \mathrm {e} ^ {- y} \mathrm {d} y = 1 - \mathrm {e} ^ {- 1}.</equation>又因为<equation>P \left\{X \leqslant 1, Y \leqslant 1 \right\} = \int_ {- \infty} ^ {1} \mathrm {d} x \int_ {- \infty} ^ {1} f (x, y) \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {x} \mathrm {e} ^ {- x} \mathrm {d} y = \int_ {0} ^ {1} x \mathrm {e} ^ {- x} \mathrm {d} x = 1 - 2 \mathrm {e} ^ {- 1},</equation>所以由条件概率的定义知，<equation>P \{X \leqslant 1 \mid Y \leqslant 1 \} = \frac {P \{X \leqslant 1 , Y \leqslant 1 \}}{P \{Y \leqslant 1 \}} = \frac {1 - 2 \mathrm {e} ^ {- 1}}{1 - \mathrm {e} ^ {- 1}} = \frac {\mathrm {e} - 2}{\mathrm {e} - 1}.</equation>

---

**2016年第23题 | 解答题 | 11分**


设总体<equation>X</equation>的概率密度为<equation>f (x; \theta) = \left\{ \begin{array}{l l} \frac {3 x ^ {2}}{\theta^ {3}}, & 0 < x < \theta , \\ 0, & \text {其 他}, \end{array} \right.</equation>其中<equation>\theta\in(0,+\infty)</equation>为未知参数，<equation>X_{1},X_{2},X_{3}</equation>为来自总体 X的简单随机样本，令<equation>T=\max\{X_{1},X_{2},X_{3}\}</equation>I. 求 T的概率密度； II. 确定 a，使得<equation>E(aT)=\theta.</equation>

**答案:**（I）<equation>f_{T}(t)=\left\{\begin{array}{ll}\frac{9 t^{8}}{\theta^{9}},&0<t<\theta,\\ 0,&\text{其他};\end{array}\right.</equation>（Ⅱ）当 a<equation>=\frac{10}{9}</equation>时，<equation>E(aT)=\theta.</equation>

**解析:**解（I）设 T的分布函数为<equation>F_{T}(t), T</equation>的概率密度为<equation>f_{T}(t).</equation>由于<equation>X_{1}, X_{2}, X_{3}</equation>为来自总体 X的简单随机样本，故它们相互独立且与 X同分布.从而<equation>\begin{array}{l} F _ {T} (t) = P \{T \leqslant t \} = P \left\{X _ {1} \leqslant t, X _ {2} \leqslant t, X _ {3} \leqslant t \right\} = P \left\{X _ {1} \leqslant t \right\} \cdot P \left\{X _ {2} \leqslant t \right\} \cdot P \left\{X _ {3} \leqslant t \right\} \\ = \left[ P \left\{X \leqslant t \right\} \right] ^ {3} = \left[ F _ {X} ^ {\prime} (t) \right] ^ {3}, \\ \end{array}</equation>其中<equation>F_{X}(t)</equation>为X的分布函数.

下面用两种方法求<equation>f_{T}(t)</equation>（法一）先求<equation>F_{T}(t)</equation>，再求导得到<equation>f_{T}(t)</equation>当<equation>t < 0</equation>时，<equation>F_{X}(t) = \int_{-\infty}^{t} f(x;\theta)\mathrm{d}x = 0.</equation>于是<equation>F_{T}(t) = \left[ F_{X}(t)\right]^{3} = 0.</equation>当<equation>0 \leqslant t < \theta</equation>时，<equation>F_{X}(t) = \int_{-\infty}^{t} f(x; \theta)\mathrm{d}x = \int_{0}^{t}\frac{3x^{2}}{\theta^{3}}\mathrm{d}x = \frac{t^{3}}{\theta^{3}}.</equation>于是<equation>F_{T}(t) = [F_{X}(t)]^{3} = \frac{t^{9}}{\theta^{9}}.</equation>当<equation>t \geqslant \theta</equation>时，<equation>F_{X}(t) = 1.</equation>于是<equation>F_{T}(t) = \left[ F_{X}(t) \right]^{3} = 1.</equation>因此，<equation>F _ {T} (t) = \left\{ \begin{array}{l l} 0, & t < 0, \\ \frac {t ^ {9}}{\theta^ {9}}, & 0 \leqslant t < \theta , \\ 1, & t \geqslant \theta . \end{array} \right.</equation>综上所述，<equation>T</equation>的概率密度为<equation>f_{T}(t) = F_{T}^{\prime}(t) = \left\{ \begin{array}{ll}\frac{9t^{8}}{\theta^{9}}, & 0 < t < \theta ,\\ 0, & \text{其他}. \end{array} \right.</equation>（法二）直接求导得到<equation>f_{T}(t)</equation>后再求解.<equation>f _ {T} (t) = F _ {T} ^ {\prime} (t) = 3 F _ {X} ^ {\prime} (t) \left[ F _ {X} (t) \right] ^ {2} = 3 f (t; \theta) \left[ F _ {X} (t) \right] ^ {2}.</equation>当<equation>t < 0</equation>时，<equation>f(t; \theta) = 0.</equation>于是<equation>f_{T}(t) = 0.</equation>当<equation>0\leqslant t < \theta</equation>时，<equation>F_{X}(t) = \int_{-\infty}^{t} f(x;\theta)\mathrm{d}x = \int_{0}^{t}\frac{3x^{2}}{\theta^{3}}\mathrm{d}x = \frac{t^{3}}{\theta^{3}}.</equation>于是<equation>f _ {T} (t) = 3 f (t; \theta) \left[ F _ {X} (t) \right] ^ {2} = 3 \cdot \frac {3 t ^ {2}}{\theta^ {3}} \cdot \left(\frac {t ^ {3}}{\theta^ {3}}\right) ^ {2} = \frac {9 t ^ {8}}{\theta^ {9}}.</equation>当<equation>t \geqslant \theta</equation>时，<equation>f(t; \theta) = 0.</equation>于是<equation>f_{T}(t) = 0.</equation>综上所述，<equation>T</equation>的概率密度为<equation>f_{T}(t)=\left\{ \begin{array}{ll}\frac{9 t^{8}}{\theta^{9}},&0<t<\theta ,\\ 0,&\text{其他}. \end{array} \right.</equation>（Ⅱ）由第（Ⅰ）问中所求结果知，<equation>E (a T) = a E (T) = a \int_ {- \infty} ^ {+ \infty} t f _ {T} (t) \mathrm {d} t = a \int_ {0} ^ {\theta} \frac {9 t ^ {9}}{\theta^ {9}} \mathrm {d} t = \frac {9 a}{1 0 \theta^ {9}} t ^ {1 0} \Bigg | _ {0} ^ {\theta} = \frac {9}{1 0} a \theta .</equation>要使<equation>E ( a T)=\theta</equation>，则<equation>\frac{9}{10} a\theta =\theta</equation>，解得<equation>a=\frac{10}{9}.</equation>因此，当<equation>a = \frac{10}{9}</equation>时，<equation>E(aT) = \theta .</equation>

---

**2015年第22题 | 解答题 | 11分**

22. (本题满分11分)

设随机变量 X的概率密度为<equation>f ( x )=\left\{\begin{array}{ll}2^{-x}\ln 2,&x>0,\\ 0,&x\leqslant 0.\end{array} \right.</equation>对 X 进行独立重复的观测，直到第2个大于3的观测值出现时停止，记 Y为观测次数.

I. 求 Y的既率分布；

II. 求 E(Y).

**答案:**(22) （I）Y的概率分布为<equation>P \{Y = k \} = \frac {1}{6 4} (k - 1) \left(\frac {7}{8}\right) ^ {k - 2}, \quad k = 2, 3, 4, \dots ;</equation>

**解析:**解（ I ）由题设知，<equation>P \left\{X \leqslant 3 \right\} = \int_ {- \infty} ^ {3} f (x) \mathrm {d} x = \int_ {0} ^ {3} 2 ^ {- x} \ln 2 \mathrm {d} x = - 2 ^ {- x} \Bigg | _ {0} ^ {3} = - \frac {1}{8} - (- 1) = \frac {7}{8},</equation><equation>P \{X > 3 \} = 1 - P \{X \leqslant 3 \} = 1 - \frac {7}{8} = \frac {1}{8}.</equation>Y可能的取值为2，3，4，….又由于<equation>Y=k(k\geqslant 2)</equation>意味着前k-1次只有1次出现大于3的观测值，且第k次出现大于3的观测值，故Y的概率分布为<equation>P \{Y = k \} = C _ {k - 1} ^ {1} \times \frac {1}{8} \times \left(\frac {7}{8}\right) ^ {k - 2} \times \frac {1}{8} = \frac {1}{6 4} (k - 1) \left(\frac {7}{8}\right) ^ {k - 2}, \quad k = 2, 3, 4, \dots .</equation>（Ⅱ）（法一）由期望的定义知，<equation>E (Y) = \sum_ {k = 2} ^ {\infty} k \cdot P \{Y = k \} = \frac {1}{6 4} \sum_ {k = 2} ^ {\infty} k (k - 1) \left(\frac {7}{8}\right) ^ {k - 2}.</equation>考虑幂级数<equation>\sum_{k = 2}^{\infty}k(k - 1)x^{k - 2}</equation>，其收敛域为（-1，1），故该级数在<equation>x = \frac{7}{8}</equation>处收敛.当<equation>x\in(-1,1)</equation>时，<equation>\begin{aligned} \sum_ {k = 2} ^ {\infty} k (k - 1) x ^ {k - 2} &= \sum_ {k = 2} ^ {\infty} \left(x ^ {k}\right) ^ {\prime \prime} = \left(\sum_ {k = 2} ^ {\infty} x ^ {k}\right) ^ {\prime \prime} = \left(\frac {x ^ {2}}{1 - x}\right) ^ {\prime \prime} = \left(\frac {x ^ {2} - 1 + 1}{1 - x}\right) ^ {\prime \prime} \\ &= \left(- x - 1 + \frac {1}{1 - x}\right) ^ {\prime \prime} = \left(\frac {1}{1 - x}\right) ^ {\prime \prime} = \frac {2}{(1 - x) ^ {3}}. \end{aligned}</equation>因此，<equation>E (Y) = \frac {1}{6 4} \sum_ {k = 2} ^ {\infty} k (k - 1) \left(\frac {7}{8}\right) ^ {k - 2} = \frac {1}{6 4} \times \frac {2}{\left(1 - \frac {7}{8}\right) ^ {3}} = 1 6.</equation>（法二）利用几何分布的性质.

设<equation>Y_{1}</equation>表示出现第1个大于3的观测值时所需的观测次数，<equation>Y_{2}</equation>表示出现第1个大于3的观测值之后到出现第2个大于3的观测值时所需的观测次数，则<equation>Y=Y_{1}+Y_{2}</equation>，且<equation>Y_{1},Y_{2}</equation>均服从参数为<equation>p=\frac{1}{8}</equation>的几何分布.于是<equation>E\left(Y_{1}\right)=E\left(Y_{2}\right)=\frac{1}{p}=8.</equation>因此，<equation>E (Y) = E \left(Y _ {1}\right) + E \left(Y _ {2}\right) = 1 6.</equation>

---

**2014年第22题 | 解答题 | 11分**


22. (本题满分11分)

设随机变量 X的概率分布为<equation>P\{X=1\}=P\{X=2\}=\frac{1}{2}.</equation>在给定 X=i 的条件下，随机变量 Y服从均匀分布<equation>U(0,i)(i=1,2).</equation>I. 求 Y的分布函数<equation>F_{Y}(y);</equation>II. 求 E(Y).

**答案:**(22) (I)<equation>F_{Y}(y)=\left\{ \begin{array}{ll} 0, & y<0, \\ \frac{3}{4} y, & 0\leqslant y<1, \\ \frac{1}{2}+\frac{1}{4} y, & 1\leqslant y<2, \\ 1, & y\geqslant 2; \end{array} \right.</equation><equation>\frac {3}{4}.</equation>

**解析:**解（I）由题设知，当<equation>X=1</equation>时，<equation>Y\sim U(0,1)</equation>；当<equation>X=2</equation>时，<equation>Y\sim U(0,2).</equation>于是，<equation>\begin{array}{l} F _ {Y} (y) = P \left\{Y \leqslant y \right\} = P \left\{Y \leqslant y, X = 1 \right\} + P \left\{Y \leqslant y, X = 2 \right\} \\ = P \left\{Y \leqslant y \mid X = 1 \right\} P \left\{X = 1 \right\} + P \left\{Y \leqslant y \mid X = 2 \right\} P \left\{X = 2 \right\}. \\ \end{array}</equation>当<equation>y < 0</equation>时，<equation>F_{Y}(y)=0\times \frac{1}{2}+0\times \frac{1}{2}=0.</equation>当<equation>0 \leqslant y < 1</equation>时，<equation>F_{Y}(y) = \left(\int_{0}^{y}1\mathrm{d}y\right)\cdot \frac{1}{2} + \left(\int_{0}^{y}\frac{1}{2}\mathrm{d}y\right)\cdot \frac{1}{2} = \frac{3}{4} y.</equation>当<equation>1\leqslant y < 2</equation>时，<equation>F_{Y}(y) = \left(\int_{0}^{1}1\mathrm{d}y\right)\cdot \frac{1}{2} + \left(\int_{0}^{y}\frac{1}{2}\mathrm{d}y\right)\cdot \frac{1}{2} = \frac{1}{2} + \frac{1}{4} y.</equation>当<equation>y\geqslant 2</equation>时，<equation>F_{Y}(y) = 1\times \frac{1}{2} +1\times \frac{1}{2} = 1.</equation>因此，<equation>Y</equation>的分布函数为<equation>F_{Y}(y) = \left\{ \begin{array}{ll}0, & y < 0,\\ \frac{3}{4} y, & 0 \leqslant y < 1,\\ \frac{1}{2} +\frac{1}{4} y, & 1 \leqslant y < 2,\\ 1, & y \geqslant 2. \end{array} \right.</equation>（Ⅱ）由第（I）问中<equation>Y</equation>的分布函数的表达式知，<equation>Y</equation>的概率密度函数为<equation>f _ {Y} (y) = F _ {Y} ^ {\prime} (y) = \left\{ \begin{array}{l l} \frac {3}{4}, & 0 \leqslant y < 1, \\ \frac {1}{4}, & 1 \leqslant y < 2, \\ 0, & \text {其 他}. \end{array} \right.</equation>因此，<equation>E (Y) = \int_ {- \infty} ^ {+ \infty} y f _ {Y} (y) \mathrm {d} y = \int_ {0} ^ {1} \frac {3}{4} y \mathrm {d} y + \int_ {1} ^ {2} \frac {1}{4} y \mathrm {d} y = \frac {3}{8} + \frac {3}{8} = \frac {3}{4}.</equation>

---

**2013年第14题 | 填空题 | 4分**

14. 设随机变量<equation>X</equation>服从标准正态分布<equation>N(0,1)</equation>, 则<equation>E(X \mathrm{e}^{2 X}) =</equation>___

**解析:**解 由题设知<equation>E \left(X \mathrm {e} ^ {2 X}\right) = \int_ {- \infty} ^ {+ \infty} x \mathrm {e} ^ {2 x} \cdot \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \mathrm {d} x = \frac {\mathrm {e} ^ {2}}{\sqrt {2 \pi}} \int_ {- \infty} ^ {+ \infty} x \mathrm {e} ^ {- \frac {(x - 2) ^ {2}}{2}} \mathrm {d} x.</equation>记<equation>E=\frac{\mathrm{e}^{2}}{\sqrt{2\pi}}\int_{-\infty}^{+\infty}x\mathrm{e}^{-\frac{(x-2)^{2}}{2}}\mathrm{d}x.</equation>下面我们用两种方法计算E.

（法一）积分<equation>\frac{1}{\sqrt{2\pi}}\int_{- \infty}^{+ \infty}x\mathrm{e}^{-\frac{(x-2)^{2}}{2}}\mathrm{d}x</equation>可看作服从正态分布N（2,1）的随机变量的数学期望，故<equation>\frac{1}{\sqrt{2\pi}}\int_{- \infty}^{+ \infty}x\mathrm{e}^{-\frac{(x-2)^{2}}{2}}\mathrm{d}x=2.</equation>因此，<equation>E=2\mathrm{e}^{2}.</equation>（法二）<equation>\begin{array}{l} E = \frac {\mathrm {e} ^ {2}}{\sqrt {2 \pi}} \int_ {- \infty} ^ {+ \infty} x \mathrm {e} ^ {- \frac {(x - 2) ^ {2}}{2}} \mathrm {d} x = \frac {\mathrm {e} ^ {2}}{\sqrt {2 \pi}} \left[ \int_ {- \infty} ^ {+ \infty} (x - 2) \mathrm {e} ^ {- \frac {(x - 2) ^ {2}}{2}} \mathrm {d} x + 2 \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- \frac {(x - 2) ^ {2}}{2}} \mathrm {d} x \right] \\ \underline {{= t = x - 2}} \mathrm {e} ^ {2} \left(\frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {+ \infty} t \mathrm {e} ^ {- \frac {t ^ {2}}{2}} \mathrm {d} t + \frac {2}{\sqrt {2 \pi}} \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- \frac {t ^ {2}}{2}} \mathrm {d} t\right). \\ \end{array}</equation>由标准正态分布的性质知<equation>\frac{1}{\sqrt{2\pi}}\int_{- \infty}^{+ \infty}\mathrm{e}^{-\frac{x^{2}}{2}}\mathrm{d}x=1, E(X)=\frac{1}{\sqrt{2\pi}}\int_{- \infty}^{+ \infty}x\mathrm{e}^{-\frac{x^{2}}{2}}\mathrm{d}x=0.</equation>代入上式可得<equation>E=\mathrm{e}^{2}(0+2)=2\mathrm{e}^{2}.</equation>综上所述，<equation>E\left(X\mathrm{e}^{2X}\right)=E=2\mathrm{e}^{2}.</equation>

---

**2012年第23题 | 解答题 | 11分**

23. (本题满分11分)

设随机变量 X与 Y相互独立，且都服从参数为1的指数分布. 记<equation>U=\max \{X,Y\}, V=\min \{X,Y\}</equation>I. 求 V的概率密度<equation>f_{V}(v)</equation>II. 求<equation>E(U+V).</equation>

**答案:**(23) （ I ）<equation>f_{V}(v)=\left\{\begin{array}{ll}2\mathrm{e}^{-2v},&v>0,\\ 0,&v\leqslant 0; \end{array}\right.</equation>（Ⅱ）2.

**解析:**解（I）由题设，随机变量 X, Y的概率密度均为<equation>f ( x )=\left\{\begin{array}{ll}\mathrm{e}^{-x},&x>0,\\ 0,&\text{其他}.\end{array} \right.</equation>于是 X, Y的分布函数均为<equation>F ( x )=\left\{\begin{array}{ll}1-\mathrm{e}^{-x},&x>0,\\ 0,&\text{其他},\end{array} \right.</equation>从而 V的分布函数为<equation>\begin{array}{l} F _ {V} (v) = P \{V \leqslant v \} = 1 - P \{V > v \} = 1 - P \{X > v, Y > v \} \\ = 1 - P \{X > v \} \cdot P \{Y > v \} \\ = 1 - \left[ 1 - F (v) \right] ^ {2} = \left\{ \begin{array}{l l} 1 - \mathrm {e} ^ {- 2 v}, & v > 0, \\ 0, & v \leqslant 0. \end{array} \right. \\ \end{array}</equation>因此，V的概率密度为<equation>f _ {V} (v) = F _ {V} ^ {\prime} (v) = \left\{ \begin{array}{l l} 2 \mathrm {e} ^ {- 2 v}, & v > 0, \\ 0, & v \leqslant 0. \end{array} \right.</equation>（Ⅱ）（法一）由于<equation>U + V = \max \{X, Y\} + \min \{X, Y\} = X + Y</equation>，故<equation>E (U + V) = E (X + Y) = E (X) + E (Y) = 2 E (X) = 2 \int_ {0} ^ {+ \infty} x \mathrm {e} ^ {- x} \mathrm {d} x = 2.</equation>（法二）U的分布函数为<equation>F _ {U} (u) = P \left\{U \leqslant u \right\} = P \left\{X \leqslant u, Y \leqslant u \right\} = P \left\{X \leqslant u \right\} \cdot P \left\{Y \leqslant u \right\} = \left[ F (u) \right] ^ {2}.</equation>于是，U的概率密度为<equation>f _ {U} (u) = F _ {U} ^ {\prime} (u) = 2 F (u) f (u) = \left\{ \begin{array}{l l} 2 \mathrm {e} ^ {- u} \left(1 - \mathrm {e} ^ {- u}\right), & u > 0, \\ 0, & u \leqslant 0. \end{array} \right.</equation>分别计算<equation>E ( u ) , E ( V )</equation><equation>E (U) = \int_ {- \infty} ^ {+ \infty} u f _ {U} (u) \mathrm {d} u = \int_ {0} ^ {+ \infty} 2 u \left(\mathrm {e} ^ {- u} - \mathrm {e} ^ {- 2 u}\right) \mathrm {d} u,</equation><equation>E (V) = \int_ {- \infty} ^ {+ \infty} v f _ {V} (v) \mathrm {d} v = \int_ {0} ^ {+ \infty} 2 v \mathrm {e} ^ {- 2 v} \mathrm {d} v.</equation>因此，<equation>E (U + V) = E (U) + E (V) = \int_ {0} ^ {+ \infty} 2 u \left(\mathrm {e} ^ {- u} - \mathrm {e} ^ {- 2 u}\right) \mathrm {d} u + \int_ {0} ^ {+ \infty} 2 v \mathrm {e} ^ {- 2 v} \mathrm {d} v = \int_ {0} ^ {+ \infty} 2 u \mathrm {e} ^ {- u} \mathrm {d} u = 2.</equation>

---

**2011年第4题 | 选择题 | 4分 | 答案: B**

4. 设<equation>I=\int_{0}^{\frac{\pi}{4}}\ln(\sin x)\mathrm{d}x, J=\int_{0}^{\frac{\pi}{4}}\ln(\cot x)\mathrm{d}x, K=\int_{0}^{\frac{\pi}{4}}\ln(\cos x)\mathrm{d}x</equation>，则 I, J, K的大小关系为（    )

A. I < J < K

B. I < K < J

C. J < I < K

D. K < J < I

答案: B

**解析:**解当 0 < x <<equation>\frac{\pi}{4}</equation>时，0 < sin x < cos x < 1 < cot x.又由于 f(u) = ln u在（0，+∞）上单调增加，故当 0 < x <<equation>\frac{\pi}{4}</equation>时，<equation>\ln(\sin x) < \ln(\cos x) < 0 < \ln(\cot x).</equation>因此，由定积分的保号性可知， I < K < J.应选B.

---

**2020年第23题 | 解答题 | 11分**


设某元件的使用寿命<equation>T</equation>的分布函数为<equation>F (t) = \left\{ \begin{array}{l l} 1 - \mathrm {e} ^ {- \left(\frac {t}{\theta}\right) ^ {m}}, & t \geqslant 0, \\ 0, & \text {其 他}, \end{array} \right.</equation>其中<equation>\theta, m</equation>为参数且均大于零.

I. 求概率<equation>P\{T > t\}</equation>与<equation>P\{T > s + t \mid T > s\}</equation>，其中<equation>s > 0, t > 0</equation>；

II. 任取 n个这种元件做寿命试验，测得它们的寿命分别为<equation>t_{1}, t_{2}, \dots , t_{n}</equation>，若 m已知，求<equation>\theta</equation>的最大似然估计值<equation>\hat{\theta}.</equation>

**答案:**（I）<equation>P \left\{ T > t \right\} = \mathrm{e}^{-\left(\frac{t}{\theta}\right)^{m}}, P \left\{ T > s + t \mid T > s \right\} = \mathrm{e}^{\frac{s^{m}-(s+t)^{m}}{\theta^{m}}};</equation>（Ⅱ）<equation>\theta</equation>的最大似然估计值为<equation>\hat{\theta}=\sqrt[m]{\frac{1}{n}\sum_{i=1}^{n}t_{i}^{m}}.</equation>

**解析:**（I）由分布函数的定义以及 s > 0，t > 0可得，<equation>P \left\{T > t \right\} = 1 - P \left\{T \leqslant t \right\} = 1 - F (t) = \mathrm {e} ^ {- \left(\frac {t}{\theta}\right) ^ {m}}.</equation><equation>P \left\{T > s + t \mid T > s \right\} = \frac {P \left\{T > s + t \right\}}{P \left\{T > s \right\}} = \frac {\mathrm {e} ^ {- \left(\frac {s + t}{\theta}\right) ^ {m}}}{\mathrm {e} ^ {- \left(\frac {s}{\theta}\right) ^ {m}}} = \mathrm {e} ^ {\frac {s ^ {m} - (s + t) ^ {m}}{\theta^ {m}}}.</equation>（Ⅱ）计算概率密度<equation>f(t; \theta).</equation><equation>f (t; \theta) = F ^ {\prime} (t; \theta) = \left\{ \begin{array}{l l} - \mathrm {e} ^ {- \left(\frac {t}{\theta}\right) ^ {m}} \cdot (- m) \cdot \left(\frac {t}{\theta}\right) ^ {m - 1} \cdot \frac {1}{\theta}, & t > 0, \\ 0, & \text {其 他} = \left\{ \begin{array}{l l} \frac {m t ^ {m - 1}}{\theta^ {m}} \mathrm {e} ^ {- \left(\frac {t}{\theta}\right) ^ {m}}, & t > 0, \\ 0, & \text {其 他}. \end{array} \right. \end{array} \right.</equation>似然函数<equation>L (\theta) = \prod_ {i = 1} ^ {n} f \left(t _ {i}; \theta\right) = \left\{ \begin{array}{l l} \left(t _ {1} t _ {2} \dots t _ {n}\right) ^ {m - 1} \cdot \left(\frac {m}{\theta^ {m}}\right) ^ {n} \cdot \mathrm {e} ^ {- \frac {1}{\theta^ {m}} \sum_ {i = 1} ^ {n} t _ {i} ^ {m}}, & t _ {i} > 0, i = 1, 2, \dots , n, \\ 0, & \text {其 他}. \end{array} \right.</equation>取对数得<equation>\ln L (\theta) = (m - 1) \ln \left(t _ {1} t _ {2} \dots t _ {n}\right) + n \left(\ln m - m \ln \theta\right) - \frac {1}{\theta^ {m}} \sum_ {i = 1} ^ {n} t _ {i} ^ {m}.</equation>令<equation>\frac{\mathrm{d}\left[\ln L(\theta)\right]}{\mathrm{d}\theta}=-\frac{mn}{\theta}+\frac{m}{\theta^{m+1}}\sum_{i=1}^{n}t_{i}^{m}=0</equation>，可得<equation>mn\theta^{m}=m\sum_{i=1}^{n}t_{i}^{m}</equation>. 从而<equation>\theta^{m}=\frac{1}{n}\sum_{i=1}^{n}t_{i}^{m},</equation><equation>\hat{\theta}=\sqrt[m]{\frac{1}{n}\sum_{i=1}^{n}t_{i}^{m}}.</equation>因此，<equation>\theta</equation>的最大似然估计值为<equation>\hat{\theta}=\sqrt[m]{\frac{1}{n}\sum_{i=1}^{n}t_{i}^{m}}.</equation>

---

**2019年第23题 | 解答题 | 11分**


设总体<equation>X</equation>的概率密度为<equation>f \left(x; \sigma^ {2}\right) = \left\{ \begin{array}{l l} \frac {A}{\sigma} \mathrm {e} ^ {- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}}, & x \geqslant \mu , \\ 0, & x < \mu . \end{array} \right.</equation>其中<equation>\mu</equation>是已知参数，<equation>\sigma >0</equation>是未知参数，A是常数.<equation>X_{1},X_{2},\cdots,X_{n}</equation>是来自总体 X的简单随机样本.

I. 求 A;

II. 求<equation>\sigma^{2}</equation>的最大似然估计量.

**答案:**( I )<equation>A=\sqrt{\frac{2}{\pi}};</equation>( II )<equation>\sigma^{2}</equation>的最大似然估计量为<equation>\widehat{\sigma^{2}}=\frac{\sum_{i=1}^{n}\left(X_{i}-\mu\right)^{2}}{n}.</equation>

**解析:**解（ I ）利用<equation>\int_{- \infty}^{+ \infty} f ( x ; \sigma^{2} ) \mathrm{d} x=1</equation>来计算 A.<equation>\begin{aligned} \int_ {- \infty} ^ {+ \infty} f (x; \sigma^ {2}) \mathrm {d} x &= \int_ {\mu} ^ {+ \infty} \frac {A}{\sigma} \mathrm {e} ^ {- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}} \mathrm {d} x \underline {{= t = x - \mu}} A \int_ {0} ^ {+ \infty} \frac {1}{\sigma} \mathrm {e} ^ {- \frac {t ^ {2}}{2 \sigma^ {2}}} \mathrm {d} t = A \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {1}{2} \cdot \left(\frac {t}{\sigma}\right) ^ {2}} \mathrm {d} \left(\frac {t}{\sigma}\right) \\ \frac {\frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \mathrm {d} x = 1}{\underline {{}}} A \cdot \frac {\sqrt {2 \pi}}{2} &= 1. \end{aligned}</equation>因此，<equation>A=\frac{2}{\sqrt{2\pi}}=\sqrt{\frac{2}{\pi}}.</equation>（Ⅱ）设<equation>x_{1}, x_{2}, \dots, x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots, X_{n}</equation>的一组样本值，则关于<equation>\sigma^2</equation>的似然函数为<equation>\begin{array}{l} L \left(\sigma^ {2}\right) = \prod_ {i = 1} ^ {n} f \left(x _ {i}; \sigma^ {2}\right) = \left\{ \begin{array}{l l} \prod_ {i = 1} ^ {n} \sqrt {\frac {2}{\pi}} \cdot \frac {1}{\sigma} \cdot \mathrm {e} ^ {- \frac {\left(x _ {i} - \mu\right) ^ {2}}{2 \sigma^ {2}}}, & x _ {1} \geqslant \mu , x _ {2} \geqslant \mu , \dots , x _ {n} \geqslant \mu , \\ 0, & \text {其 他} \end{array} \right. \\ = \left\{ \begin{array}{l l} \left(\frac {2}{\pi}\right) ^ {\frac {n}{2}} \cdot \left(\frac {1}{\sigma^ {2}}\right) ^ {\frac {n}{2}} \cdot \mathrm {e} ^ {- \frac {\sum_ {i = 1} ^ {n} \left(x _ {i} - \mu\right) ^ {2}}{2 \sigma^ {2}}}, & x _ {1} \geqslant \mu , x _ {2} \geqslant \mu , \dots , x _ {n} \geqslant \mu , \\ 0, & \text {其 他}. \end{array} \right. \\ \end{array}</equation>当<equation>x_{1}\geqslant \mu ,x_{2}\geqslant \mu ,\dots ,x_{n}\geqslant \mu</equation>时，<equation>\ln L \left(\sigma^ {2}\right) = \frac {n}{2} \ln \frac {2}{\pi} - \frac {n}{2} \ln \sigma^ {2} - \frac {\sum_ {i = 1} ^ {n} \left(x _ {i} - \mu\right) ^ {2}}{2 \sigma^ {2}}.</equation>令<equation>\frac{\mathrm{d}\left[\ln L(\sigma^{2})\right]}{\mathrm{d}(\sigma^{2})}=0</equation>即<equation>-\frac{n}{2}\cdot \frac{1}{\sigma^{2}}+\frac{\sum_{i=1}^{n}\left(x_{i}-\mu\right)^{2}}{2}\cdot \frac{1}{\sigma^{4}}=0</equation>，解得<equation>\sigma^{2}=\frac{\sum_{i=1}^{n}\left(x_{i}-\mu\right)^{2}}{n}.</equation>因此，<equation>\sigma^{2}</equation>的最大似然估计量为<equation>\hat {\sigma^ {2}} = \frac {\sum_ {i = 1} ^ {n} \left(X _ {i} - \mu\right) ^ {2}}{n}.</equation>

---

**2018年第23题 | 解答题 | 11分**


设总体<equation>X</equation>的概率密度为<equation>f (x; \sigma) = \frac {1}{2 \sigma} \mathrm {e} ^ {- \frac {| x |}{\sigma}}, (- \infty < x < + \infty).</equation>其中<equation>\sigma \in(0,+\infty)</equation>为未知参数，<equation>X_{1},X_{2},\cdots,X_{n}</equation>为来自总体 X的简单随机样本.记<equation>\sigma</equation>的最大似然估计量为<equation>\hat{\sigma}.</equation>I. 求<equation>\hat{\sigma}</equation>;

II. 求<equation>E(\hat{\sigma}),D(\hat{\sigma}).</equation>

**答案:**（I）<equation>\sigma</equation>的最大似然估计量为<equation>\hat{\sigma}=\frac{\sum_{i=1}^{n} \mid X_{i}\mid}{n}；</equation>（Ⅱ）<equation>E(\hat{\sigma})=\sigma</equation>，<equation>D(\hat{\sigma})=\frac{\sigma^{2}}{n}.</equation>

**解析:**解（ I ）设<equation>x_{1}, x_{2}, \dots , x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots , X_{n}</equation>的一组样本值.似然函数为<equation>L (\sigma) = \prod_ {i = 1} ^ {n} f \left(x _ {i}; \sigma\right) = \frac {1}{2 ^ {n} \sigma^ {n}} \mathrm {e} ^ {- \frac {\left| x _ {1} \right| + \left| x _ {2} \right| + \cdots + \left| x _ {n} \right|}{\sigma}}, - \infty < x _ {i} < + \infty , i = 1, 2, \dots , n.</equation>对 L（<equation>\sigma</equation>）取对数，得<equation>\ln L (\sigma) = - \frac {\sum_ {i = 1} ^ {n} \left| x _ {i} \right|}{\sigma} - n \ln (2 \sigma).</equation>令<equation>\frac{\mathrm{d}[\ln L(\sigma)]}{\mathrm{d}\sigma}=\frac{\sum_{i=1}^{n} \mid x_{i}\mid}{\sigma^{2}}-\frac{n}{\sigma}=0</equation>即<equation>\sum_{i=1}^{n} \mid x_{i}\mid-n\sigma=0</equation>解得<equation>\sigma=\frac{\sum_{i=1}^{n} \mid x_{i}\mid}{n}.</equation>因此，<equation>\sigma</equation>的最大似然估计量为<equation>\hat {\sigma} = \frac {\sum_ {i = 1} ^ {n} \left| X _ {i} \right|}{n}.</equation>（Ⅱ）由于<equation>X_{1}, X_{2}, \dots , X_{n}</equation>为来自总体X的简单随机样本，故它们相互独立，且与总体X同分布<equation>E(X_{i})=E(X), E(|X_{i}|)=E(|X|), i=1,2,\dots ,n.</equation>根据期望的线性性质，<equation>E (\hat {\sigma}) = E \left(\frac {\sum_ {i = 1} ^ {n} \left| X _ {i} \right|}{n}\right) = \frac {\sum_ {i = 1} ^ {n} E \left(\left| X _ {i} \right|\right)}{n} = \frac {n E \left(\left| X \right|\right)}{n} = E (\left| X \right|).</equation>根据期望的定义，<equation>\begin{aligned} E (\mid X \mid) &= \int_ {- \infty} ^ {+ \infty} | x | \cdot f (x; \sigma) \mathrm {d} x = \int_ {- \infty} ^ {+ \infty} | x | \cdot \frac {1}{2 \sigma} \mathrm {e} ^ {- \frac {| x |}{\sigma}} \mathrm {d} x = 2 \int_ {0} ^ {+ \infty} \frac {x}{2 \sigma} \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x \\ &= \frac {1}{\sigma} \int_ {0} ^ {+ \infty} x \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x = - \int_ {0} ^ {+ \infty} x \mathrm {d} \left(\mathrm {e} ^ {- \frac {x}{\sigma}}\right) = - \left(x \mathrm {e} ^ {- \frac {x}{\sigma}} \Big | _ {0} ^ {+ \infty} - \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x\right) \\ &= \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x = - \sigma \mathrm {e} ^ {- \frac {x}{\sigma}} \Big | _ {0} ^ {+ \infty} = \sigma . \end{aligned}</equation>因此，<equation>E(\hat{\sigma}) = \sigma .</equation>下面计算<equation>D(\hat{\sigma})。</equation>由于<equation>X_{1}, X_{2}, \dots, X_{n}</equation>相互独立，且与总体<equation>X</equation>同分布，故<equation>D(\mid X_{i}\mid) = D(\mid X\mid)</equation>，<equation>i = 1, 2, \dots, n.</equation><equation>D (\hat {\sigma}) = D \left(\frac {\sum_ {i = 1} ^ {n} \left| X _ {i} \right|}{n}\right) = \frac {1}{n ^ {2}} D \left(\sum_ {i = 1} ^ {n} \left| X _ {i} \right|\right) = \frac {1}{n ^ {2}} \cdot n D (\mid X \mid) = \frac {D (\mid X \mid)}{n}.</equation>根据方差的计算公式，<equation>D (\mid X \mid) = E \left(\mid X \mid^ {2}\right) - \left[ E (\mid X \mid) \right] ^ {2} = E \left(X ^ {2}\right) - \left[ E (\mid X \mid) \right] ^ {2}.</equation><equation>\begin{aligned} E \left(X ^ {2}\right) &= \int_ {- \infty} ^ {+ \infty} x ^ {2} \cdot f (x; \sigma) \mathrm {d} x = \int_ {- \infty} ^ {+ \infty} x ^ {2} \cdot \frac {1}{2 \sigma} \mathrm {e} ^ {- \frac {| x |}{\sigma}} \mathrm {d} x = \frac {1}{\sigma} \int_ {0} ^ {+ \infty} x ^ {2} \cdot \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x \\ &= - \int_ {0} ^ {+ \infty} x ^ {2} \mathrm {d} \left(\mathrm {e} ^ {- \frac {x}{\sigma}}\right) = - \left(x ^ {2} \mathrm {e} ^ {- \frac {x}{\sigma}} \Big | _ {0} ^ {+ \infty} - 2 \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {x}{\sigma}} \cdot x \mathrm {d} x\right) \\ &= 2 \int_ {0} ^ {+ \infty} x \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x \stackrel {*} {=} 2 \sigma^ {2}. \end{aligned}</equation>于是，<equation>D ( \mid X \mid ) = 2 \sigma^{2} - \sigma^{2} = \sigma^{2}.</equation>因此，<equation>D(\hat{\sigma}) = \frac{D(|X|)}{n} = \frac{\sigma^{2}}{n}.</equation>

---

**2017年第23题 | 解答题 | 11分**


某工程师为了解一台天平的精度，用该天平对一物体的质量做 n次测量，该物体的质量<equation>\mu</equation>是已知的，设 n次测量结果<equation>X_{1},X_{2},\cdots ,X_{n}</equation>相互独立且均服从正态分布<equation>N\left(\mu ,\sigma^{2}\right).</equation>该工程师记录的是 n次测量的绝对误差<equation>Z_{i}=\left|X_{i}-\mu\right|(i=1,2,\cdots,n),</equation>利用<equation>Z_{1},Z_{2},\cdots,Z_{n}</equation>估计<equation>\sigma.</equation>I. 求<equation>Z_{1}</equation>的概率密度；

II. 利用一阶矩求<equation>\sigma</equation>的矩估计量；

III. 求<equation>\sigma</equation>的最大似然估计量.

**答案:**( I )<equation>f_{Z_{1}}(z) = \left\{ \begin{array}{ll} \sqrt{\frac{2}{\pi}} \frac{1}{\sigma} \mathrm{e}^{-\frac{z^{2}}{2\sigma^{2}}}, & z \geqslant 0, \\ 0, & z < 0; \end{array} \right.</equation>( II )<equation>\hat{\sigma} = \sqrt{\frac{\pi}{2}} \bar{Z}</equation>;

( III )<equation>\hat{\sigma} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} Z_{i}^{2}}</equation>.

**解析:**解（I）由题设知，<equation>X_{1}\sim N(\mu ,\sigma^{2})</equation>，从而<equation>\frac{X_{1}-\mu}{\sigma}\sim N(0,1).</equation>当 z < 0时，<equation>F_{Z_{1}}(z)=0.</equation>当<equation>z\geqslant0</equation>时，<equation>\begin{array}{l} F _ {Z _ {1}} (z) = P \left\{Z _ {1} \leqslant z \right\} = P \left\{\mid X _ {1} - \mu \mid \leqslant z \right\} \\ = P \left\{\left| \frac {X _ {1} - \mu}{\sigma} \right| \leqslant \frac {z}{\sigma} \right\} = P \left\{- \frac {z}{\sigma} \leqslant \frac {X _ {1} - \mu}{\sigma} \leqslant \frac {z}{\sigma} \right\} \\ = 2 \Phi \left(\frac {z}{\sigma}\right) - 1, \\ \end{array}</equation>其中<equation>\varPhi(x)</equation>为标准正态分布函数.

于是，<equation>Z_{1}</equation>的分布函数为<equation>F_{Z_{1}}(z)=\left\{ \begin{array}{ll} 2\Phi \left(\frac{z}{\sigma}\right)-1, & z\geqslant 0, \\ 0, & z<0. \end{array} \right.</equation>因此，<equation>Z_{1}</equation>的概率密度为<equation>f _ {Z _ {1}} (z) = F _ {Z _ {1}} ^ {\prime} (z) = \left\{ \begin{array}{l l} \frac {2}{\sigma} \varphi \left(\frac {z}{\sigma}\right), & z \geqslant 0, \\ 0, & z < 0 \end{array} = \left\{ \begin{array}{l l} \sqrt {\frac {2}{\pi}} \frac {1}{\sigma} \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}}, & z \geqslant 0, \\ 0, & z < 0, \end{array} \right. \right.</equation>其中<equation>\varphi(x)</equation>为标准正态分布的概率密度.

（Ⅱ）由于<equation>\begin{array}{l} E \left(Z _ {1}\right) = \int_ {- \infty} ^ {+ \infty} z f _ {Z _ {1}} (z) \mathrm {d} z = \int_ {0} ^ {+ \infty} z \cdot \sqrt {\frac {2}{\pi}} \frac {1}{\sigma} \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}} \mathrm {d} z = \sqrt {\frac {2}{\pi}} \sigma \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}} \mathrm {d} \left(\frac {z ^ {2}}{2 \sigma^ {2}}\right) \\ = - \sqrt {\frac {2}{\pi}} \sigma \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}} \Big | _ {0} ^ {+ \infty} = \sqrt {\frac {2}{\pi}} \sigma , \\ \end{array}</equation>故<equation>\sigma=\sqrt{\frac{\pi}{2}} E(Z_{1})</equation>用<equation>\overline{Z}=\frac{1}{n}\sum_{i=1}^{n} Z_{i}</equation>代替<equation>E(Z_{1})</equation>，得到<equation>\sigma</equation>的矩估计量<equation>\hat {\sigma} = \sqrt {\frac {\pi}{2}} \bar {Z}.</equation>（Ⅲ）设<equation>z_{1}, z_{2}, \dots , z_{n}</equation>是相应于<equation>Z_{1}, Z_{2}, \dots , Z_{n}</equation>的一组样本值，则似然函数为<equation>L (\sigma) = L \left(z _ {1}, z _ {2}, \dots , z _ {n}; \sigma\right) = \prod_ {i = 1} ^ {n} f _ {Z _ {i}} \left(z _ {i}\right) = \left\{ \begin{array}{l l} \left(\frac {2}{\pi}\right) ^ {\frac {n}{2}} \frac {1}{\sigma^ {n}} \mathrm {e} ^ {- \frac {1}{2 \sigma^ {2}} \left(z _ {1} ^ {2} + z _ {2} ^ {2} + \dots + z _ {n} ^ {2}\right)}, & z _ {1} > 0, z _ {2} > 0, \dots , z _ {n} > 0, \\ 0, & \text {其 他}. \end{array} \right.</equation>当<equation>z_{1} > 0, z_{2} > 0, \dots, z_{n} > 0</equation>时，<equation>\ln L (\sigma) = \frac {n}{2} \ln \frac {2}{\pi} - n \ln \sigma - \frac {1}{2 \sigma^ {2}} \left(z _ {1} ^ {2} + z _ {2} ^ {2} + \dots + z _ {n} ^ {2}\right).</equation>令<equation>\frac{\mathrm{d}[\ln L(\sigma)]}{\mathrm{d}\sigma} = 0</equation>，即<equation>-\frac{n}{\sigma} +\frac{1}{\sigma^3}\left(z_1^2 +z_2^2 +\dots +z_n^2\right) = 0</equation>，解得<equation>\sigma = \sqrt{\frac{1}{n}\sum_{i=1}^{n}z_i^2}</equation><equation>\sigma</equation><equation>\hat {\sigma} = \sqrt {\frac {1}{n} \sum_ {i = 1} ^ {n} Z _ {i} ^ {2}}.</equation>

---

**2015年第23题 | 解答题 | 11分**


设总体<equation>X</equation>的概率密度为<equation>f (x; \theta) = \left\{ \begin{array}{l l} \frac {1}{1 - \theta}, & \theta \leqslant x \leqslant 1, \\ 0, & \text {其 他}, \end{array} \right.</equation>其中<equation>\theta</equation>为未知参数.<equation>X_{1},X_{2},\cdots ,X_{n}</equation>为来自该总体的简单随机样本.

I. 求<equation>\theta</equation>的矩估计量;

II. 求<equation>\theta</equation>的最大似然估计量.

**答案:**<equation>\begin{array}{l} (2 3) (\mathrm {I}) \hat {\theta} = 2 \bar {X} - 1; \\ (\mathrm {I I}) \hat {\theta} = \min _ {1 \leqslant i \leqslant n} X _ {i}. \\ \end{array}</equation>

**解析:**（ I ）由于<equation>E (X) = \int_ {- \infty} ^ {+ \infty} x f (x; \theta) \mathrm {d} x = \int_ {\theta} ^ {1} \frac {x}{1 - \theta} \mathrm {d} x = \frac {1 + \theta}{2},</equation>故<equation>\theta = 2 E ( X ) - 1.</equation>用样本均值<equation>\overline{X}=\frac{1}{n}\sum_{i=1}^{n}X_{i}</equation>代替<equation>E ( X )</equation>，可得<equation>\theta</equation>的矩估计量<equation>\hat {\theta} = 2 \bar {X} - 1.</equation>（Ⅱ）设<equation>x_{1}, x_{2}, \dots, x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots, X_{n}</equation>的一组样本值，则似然函数为<equation>L (\theta) = \prod_ {i = 1} ^ {n} f \left(x _ {i}; \theta\right) = \left\{ \begin{array}{l l} \frac {1}{(1 - \theta) ^ {n}}, & \theta \leqslant x _ {1}, x _ {2}, \dots , x _ {n} \leqslant 1, \\ 0, & \text {其 他} \end{array} = \left\{ \begin{array}{l l} \frac {1}{(1 - \theta) ^ {n}}, & \theta \leqslant \min _ {1 \leqslant i \leqslant n} x _ {i}, \\ 0, & \text {其 他}. \end{array} \right. \right.</equation>又由于<equation>\frac{1}{(1-\theta)^{n}}</equation>是关于<equation>\theta</equation>的单调增加函数，故当<equation>\theta=\min_{1\leqslant i\leqslant n}x_{i}</equation>时，<equation>L(\theta)</equation>取值最大因此，<equation>\theta</equation>的最大似然估计量为<equation>\hat {\theta} = \min _ {1 \leqslant i \leqslant n} X _ {i}.</equation>

---


**2024年第22题 | 解答题 | 12分**


设总体 X服从<equation>[0,\theta]</equation>上的均匀分布，<equation>\theta\in(0,+\infty)</equation>为未知参数，<equation>X_{1},X_{2},\cdots,X_{n}</equation>为来自总体 X的简单随机样本，记为<equation>X_{(n)}=\max\{X_{1},X_{2},\cdots,X_{n}\}, T_{c}=cX_{(n)}.</equation>I. 求 c，使得<equation>E\left(T_{c}\right)=\theta;</equation>II. 记 h(c)=E<equation>[\left(T_{c}-\theta\right)^{2}]</equation>，求 c使得 h(c)最小.

**答案:**(1)<equation>c=\frac{n+1}{n}.</equation>(2)<equation>c=\frac{n+2}{n+1}</equation>时，<equation>h(c)</equation>取最小值.

**解析:**（I）由于 X服从<equation>[0,\theta]</equation>上的均匀分布，故 X的分布函数为<equation>F _ {X} (x) = \left\{ \begin{array}{l l} 0, & x < 0, \\ \frac {x}{\theta}, & 0 \leqslant x < \theta , \\ 1, & x \geqslant \theta . \end{array} \right.</equation>记随机变量<equation>Y = X_{(n)} = \max \left|X_{1},X_{2},\dots ,X_{n}\right|</equation>. 计算<equation>Y</equation>的分布函数<equation>F_{Y}(y)</equation>当<equation>y < 0</equation>时，<equation>F_{Y}(y) = 0.</equation>当<equation>0\leqslant y < \theta</equation>时，<equation>\begin{array}{l} F _ {Y} (y) = P \left\{Y \leqslant y \right\} = P \left\{\max _ {1 \leqslant i \leqslant n} X _ {i} \leqslant y \right\} = P \left\{X _ {1} \leqslant y, X _ {2} \leqslant y, \dots , X _ {n} \leqslant y \right\} \\ \underline {{\text {独立 性}}} P \left\{X _ {1} \leqslant y \right\} P \left\{X _ {2} \leqslant y \right\} \dots P \left\{X _ {n} \leqslant y \right\} = F _ {X} ^ {n} (y) = \left(\frac {y}{\theta}\right) ^ {n}. \\ \end{array}</equation>当<equation>y\geqslant \theta</equation>时，<equation>F_{Y}(y) = 1.</equation>于是，<equation>F_{Y}(y) = \left\{ \begin{array}{ll} 0, & y < 0, \\ \left(\frac{y}{\theta}\right)^{n}, & 0 \leqslant y < \theta , \\ 1, & y \geqslant \theta . \end{array} \right.</equation>对<equation>F_{\gamma}(y)</equation>求导，可得<equation>f _ {Y} (y) = F _ {Y} ^ {\prime} (y) = \left\{ \begin{array}{l l} \frac {n y ^ {n - 1}}{\theta^ {n}}, & 0 < y < \theta , \\ 0, & \text {其 他}. \end{array} \right.</equation>因此，<equation>\begin{aligned} E \left(T _ {c}\right) &= E (c Y) = c \int_ {- \infty} ^ {+ \infty} y \cdot f _ {Y} (y) \mathrm {d} y = c \int_ {0} ^ {\theta} y \cdot \frac {n y ^ {n - 1}}{\theta^ {n}} \mathrm {d} y = c \cdot \frac {n}{\theta^ {n}} \cdot \frac {y ^ {n + 1}}{n + 1} \Bigg | _ {0} ^ {\theta} \\ &= \frac {c n}{n + 1} \theta . \end{aligned}</equation>若<equation>E\left(T_{c}\right) = \theta</equation>，则<equation>\frac{cn}{n + 1}\theta = \theta</equation>，解得<equation>c = \frac{n + 1}{n}</equation>.

（Ⅱ）展开 h（c）可得<equation>h (c) = E \left[ \left(T _ {c} - \theta\right) ^ {2} \right] = E \left[ \left(c Y - \theta\right) ^ {2} \right] = c ^ {2} E \left(Y ^ {2}\right) - 2 c \theta E (Y) + \theta^ {2}.</equation>计算<equation>E ( Y^{2})</equation><equation>E \left(Y ^ {2}\right) = \int_ {- \infty} ^ {+ \infty} y ^ {2} \cdot f _ {Y} (y) \mathrm {d} y = \int_ {0} ^ {\theta} y ^ {2} \cdot \frac {n y ^ {n - 1}}{\theta^ {n}} \mathrm {d} y = \frac {n}{\theta^ {n}} \cdot \frac {y ^ {n + 2}}{n + 2} \Bigg | _ {0} ^ {\theta} = \frac {n}{n + 2} \theta^ {2}.</equation>于是，<equation>h (c) = c ^ {2} \cdot \frac {n}{n + 2} \theta^ {2} - 2 c \cdot \frac {n}{n + 1} \theta^ {2} + \theta^ {2} = \left(\frac {n}{n + 2} c ^ {2} - \frac {2 n}{n + 1} c + 1\right) \theta^ {2}.</equation>令<equation>\frac{\mathrm{d}[h(c)]}{\mathrm{d}c}=\left(\frac{2 n}{n+2} c-\frac{2 n}{n+1}\right)\theta^{2}=0</equation>，解得 c =<equation>\frac{n+2}{n+1}.</equation>该点是 h(c）的唯一驻点. 又因为<equation>h^{\prime \prime}(c)=\frac{2 n}{n+2}\theta^{2}>0</equation>，所以该唯一驻点是 h(c）的极小值点，也是最小值点.

因此，当<equation>c=\frac{n+2}{n+1}</equation>时，<equation>h(c)</equation>最小.

---

**2023年第8题 | 选择题 | 5分 | 答案: C**

8. 设随机变量<equation>X</equation>服从参数为1的泊松分布，则<equation>E[|X - E(X)|] = (\quad)</equation>A.<equation>\frac{1} {\mathrm{e}}</equation>B.<equation>\frac{1}{2}</equation>C.<equation>\frac{2} {\mathrm{e}}</equation>D. 1

答案: C

**解析:**由于 X服从参数为1的泊松分布，故<equation>E ( X )=1.</equation>从而<equation>| X - E (X) | = | X - 1 | = \left\{ \begin{array}{l l} 1, & X = 0, \\ X - 1, & X = 1, 2, \dots . \end{array} \right.</equation>由参数为1的泊松分布的分布律可知，<equation>P\{X = 0\} = \frac{1^{0}\cdot\mathrm{e}^{-1}}{0!} = \frac{1}{\mathrm{e}}.</equation>根据数学期望的定义，<equation>\begin{aligned} E [ \mid X - E (X) \mid ] &= 1 \cdot P \{X = 0 \} + \sum_ {k = 1} ^ {\infty} (k - 1) P \{X = k \} \\ &= \frac {1}{\mathrm {e}} + \sum_ {k = 0} ^ {\infty} (k - 1) P \{X = k \} - (0 - 1) P \{X = 0 \} \\ &= \frac {1}{\mathrm {e}} + E (X - 1) + \frac {1}{\mathrm {e}} = \frac {1}{\mathrm {e}} + E (X) - 1 + \frac {1}{\mathrm {e}} \\ \underline {{\underline {{E (X) = 1}}}} \frac {2}{\mathrm {e}}. \end{aligned}</equation>因此，应选C.

---

**2023年第22题 | 解答题 | 12分**

22. (本题满分12分)

设随机变量 X的概率密度为<equation>f ( x )=\frac{\mathrm{e}^{x}}{\left( 1+\mathrm{e}^{x}\right)^{2}},-\infty<x<+\infty</equation>，令<equation>Y=\mathrm{e}^{X}.</equation>I. 求 X的分布函数;

II. 求 Y的概率密度;

III. Y的数学期望是否存在?

**答案:**（I）<equation>X</equation>的分布函数<equation>F_{X}(x)=\frac{\mathrm{e}^{x}}{1+\mathrm{e}^{x}};</equation>（Ⅱ）<equation>Y</equation>的概率密度为<equation>f_{Y}(y)=\left\{\begin{array}{ll}\frac{1}{(1+y)^{2}},&y>0,\\ 0,&y\leqslant 0.\end{array}\right.</equation>（Ⅲ）Y的数学期望不存在.

**解析:**解（ I ）记 X的分布函数为<equation>F_{X}(x).</equation>由概率密度的定义可知，<equation>F _ {X} (x) = \int_ {- \infty} ^ {x} f (t) \mathrm {d} t = \int_ {- \infty} ^ {x} \frac {\mathrm {e} ^ {t}}{\left(1 + \mathrm {e} ^ {t}\right) ^ {2}} \mathrm {d} t \xlongequal {=} \int_ {0} ^ {\mathrm {e} ^ {x}} \frac {\mathrm {d} u}{\left(1 + u\right) ^ {2}} = \frac {- 1}{1 + u} \Big | _ {0} ^ {\mathrm {e} ^ {x}} = \frac {\mathrm {e} ^ {x}}{1 + \mathrm {e} ^ {x}}.</equation>（Ⅱ）（法一）定义法.

计算<equation>Y</equation>的分布函数<equation>F_{Y}(y)</equation>由于<equation>Y=\mathrm{e}^{X}>0</equation>，故当<equation>y\leqslant0</equation>时，<equation>F_{Y}(y)=P\{Y\leqslant y\}=0.</equation>当 y > 0时，<equation>F _ {Y} (y) = P \left\{Y \leqslant y \right\} = P \left\{\mathrm {e} ^ {X} \leqslant y \right\} = P \left\{X \leqslant \ln y \right\} = F _ {X} (\ln y) = \frac {y}{1 + y}.</equation>因此，<equation>F_{Y}(y)=\left\{ \begin{array}{ll}\frac{y}{1+y},&y>0,\\ 0,&y\leqslant 0. \end{array} \right.</equation>当 y > 0时，<equation>f_{Y}(y)=F_{Y}^{\prime}(y)=\frac{1}{(1+y)^{2}}.</equation>当 y≤0时，<equation>f_{Y}(y)</equation><equation>= F_{Y}^{\prime}(y)=0.</equation>综上所述，Y的概率密度为<equation>f _ {Y} (y) = \left\{ \begin{array}{l l} \frac {1}{(1 + y) ^ {2}}, & y > 0, \\ 0, & y \leqslant 0. \end{array} \right.</equation>（法二）公式法.

函数<equation>g ( x )=\mathrm{e}^{x}</equation>在<equation>(-\infty, +\infty)</equation>上处处可导且<equation>g^{\prime}(x)=\mathrm{e}^{x}>0.</equation><equation>\alpha = \min \left\{g (- \infty), g (+ \infty) \right\} = 0, \beta = \max \left\{g (- \infty), g (+ \infty) \right\} = + \infty .</equation><equation>g(x)</equation>的反函数为<equation>x = \ln y, (\ln y)^{\prime} = \frac{1}{y}</equation>.

由公式法可得，当 y > 0时，<equation>f _ {Y} (y) = f _ {X} (\ln y) \left| \frac {1}{y} \right| = \frac {1}{y} \cdot \frac {\mathrm {e} ^ {\ln y}}{\left(1 + \mathrm {e} ^ {\ln y}\right) ^ {2}} = \frac {1}{y} \cdot \frac {y}{(1 + y) ^ {2}} = \frac {1}{(1 + y) ^ {2}}.</equation>当<equation>y\leqslant0</equation>时，<equation>f_{Y}(y)=0.</equation>因此，Y的概率密度为<equation>f_{Y}(y)=\left\{ \begin{array}{ll}\frac{1}{(1+y)^{2}},&y>0,\\ 0,&y\leqslant 0. \end{array} \right.</equation>（Ⅲ）若 Y的数学期望存在，则由数学期望的定义可知<equation>\begin{array}{l} E (Y) = \int_ {- \infty} ^ {+ \infty} y f _ {Y} (y) \mathrm {d} y = \int_ {0} ^ {+ \infty} \frac {y \mathrm {d} y}{(1 + y) ^ {2}} = \int_ {0} ^ {+ \infty} \frac {1 + y - 1}{(1 + y) ^ {2}} \mathrm {d} y \\ = \int_ {0} ^ {+ \infty} \left[ \frac {1}{1 + y} - \frac {1}{(1 + y) ^ {2}} \right] \mathrm {d} y = \left[ \ln (1 + y) + \frac {1}{1 + y} \right] \Bigg | _ {0} ^ {+ \infty} = + \infty . \\ \end{array}</equation>因此，E（Y）不存在.

---

**2020年第14题 | 填空题 | 4分**

14. 设随机变量<equation>X</equation>的概率分布为<equation>P\{X=k\}=\frac{1}{2^{k}}(k=1,2,3,\cdots),Y</equation>表示<equation>X</equation>被3除的余数，则<equation>E(Y)=</equation>___.

**答案:**# 8 7

**解析:**解 X的取值为全体正整数，而 Y表示 X被3除的余数，故 Y的可能取值为0，1，2，分别对应 X = 3i+3, X=3i+1, X=3i+2（i=0，1，2，…）的情况.

下面计算 Y的分布律.<equation>P \{Y = 0 \} = \sum_ {i = 0} ^ {\infty} P \{X = 3 i + 3 \} = \sum_ {i = 0} ^ {\infty} \frac {1}{2 ^ {3 i + 3}} = \frac {1}{8} \sum_ {i = 0} ^ {\infty} \frac {1}{8 ^ {i}},</equation><equation>P \{Y = 1 \} = \sum_ {i = 0} ^ {\infty} P \{X = 3 i + 1 \} = \sum_ {i = 0} ^ {\infty} \frac {1}{2 ^ {3 i + 1}} = \frac {1}{2} \sum_ {i = 0} ^ {\infty} \frac {1}{8 ^ {i}},</equation><equation>P \{Y = 2 \} = \sum_ {i = 0} ^ {\infty} P \{X = 3 i + 2 \} = \sum_ {i = 0} ^ {\infty} \frac {1}{2 ^ {3 i + 2}} = \frac {1}{4} \sum_ {i = 0} ^ {\infty} \frac {1}{8 ^ {i}}.</equation>根据期望的定义，<equation>\begin{array}{l} E (Y) = 0 \times P \{Y = 0 \} + 1 \times P \{Y = 1 \} + 2 \times P \{Y = 2 \} \\ = 1 \times \frac {1}{2} \sum_ {i = 0} ^ {\infty} \frac {1}{8 ^ {i}} + 2 \times \frac {1}{4} \sum_ {i = 0} ^ {\infty} \frac {1}{8 ^ {i}} = \sum_ {i = 0} ^ {\infty} \frac {1}{8 ^ {i}} \\ = \frac {1}{1 - \frac {1}{8}} = \frac {8}{7}. \\ \end{array}</equation>

---

**2019年第14题 | 填空题 | 4分**

14. 设随机变量 X的概率密度为 f(x)<equation>\left\{\begin{array}{l l} {\frac{x}{2},}&{0<x<2,}\\ {0,}&{\mathrm {其 他},}\end{array}\right.</equation>F(x)为 X的分布函数，E(X)为 X的数学期望，则<equation>P\{F(X)>E(X)-1\}=</equation>___

**答案:**# 2 3.

**解析:**（法一）分别计算<equation>E ( X )</equation>，<equation>F ( x )</equation><equation>E (X) = \int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \int_ {0} ^ {2} \frac {x ^ {2}}{2} \mathrm {d} x = \frac {x ^ {3}}{6} \Big | _ {0} ^ {2} = \frac {4}{3}.</equation>当<equation>x < 0</equation>时，<equation>F ( x )=0.</equation>当<equation>0 \leqslant x < 2</equation>时，<equation>F(x) = \int_{-\infty}^{x} f(t)\mathrm{d}t = \int_{0}^{x}\frac{t}{2}\mathrm{d}t = \frac{x^2}{4}.</equation>当<equation>x\geqslant 2</equation>时，<equation>F(x) = 1.</equation>于是，<equation>F ( x ) = \left\{ \begin{array}{ll} 0, & x < 0, \\ \frac{x^{2}}{4}, & 0 \leqslant x < 2, \\ 1, & x \geqslant 2. \end{array} \right.</equation>因此，<equation>\begin{array}{l} P \left\{F (X) > E (X) - 1 \right\} = P \left\{F (X) > \frac {1}{3} \right\} = P \left\{\frac {X ^ {2}}{4} > \frac {1}{3}, 0 \leqslant X < 2 \right\} + P \left\{X \geqslant 2 \right\} \\ = P \left\{\frac {2}{\sqrt {3}} < X < 2 \right\} + \int_ {2} ^ {+ \infty} f (x) \mathrm {d} x = 1 - \int_ {0} ^ {\frac {2}{\sqrt {3}}} \frac {x}{2} \mathrm {d} x + 0 \\ = 1 - \frac {x ^ {2}}{4} \Bigg | _ {0} ^ {\frac {2}{\sqrt {3}}} = \frac {2}{3}. \\ \end{array}</equation>（法二）我们先证明<equation>Y=F(X)</equation>服从（0，1）上的均匀分布.

注意到 F(x)在（0，2）上严格单调增加，其值域为（0，1），故可定义<equation>F^{-1}(y), y\in(0,1).</equation>考虑 Y的分布函数<equation>F_{Y}(y).</equation>当<equation>y < 0</equation>时，由于<equation>F ( X )</equation>仅在[0，1]上取值，故<equation>F_{Y} ( y )=0.</equation>当<equation>0\leqslant y < 1</equation>时，<equation>F _ {Y} (y) = P \left\{Y \leqslant y \right\} = P \left\{F (X) \leqslant y \right\} = P \left\{X \leqslant F ^ {- 1} (y) \right\} = F \left(F ^ {- 1} (y)\right) = y.</equation>当<equation>y \geqslant 1</equation>时，<equation>P\{Y \leqslant y\} = 1</equation>，即<equation>F_{Y}(y) = 1.</equation>因此，<equation>F_{Y}(y)=\left\{ \begin{array}{ll}0,& y<0,\\ y,& 0\leqslant y<1,\\ 1,& y\geqslant 1. \end{array} \right.</equation>这说明<equation>Y=F(X)</equation>服从（0，1）上的均匀分布.

由法一可知<equation>E ( X )=\frac{4}{3}</equation>，故<equation>P \left\{F (X) > E (X) - 1 \right\} = P \left\{F (X) > \frac {1}{3} \right\} = 1 - P \left\{F (X) \leqslant \frac {1}{3} \right\} = 1 - \frac {1}{3} = \frac {2}{3}.</equation>

---

**2017年第14题 | 填空题 | 4分**

14. 设随机变量 X的概率分布为<equation>P\{X=-2\}=\frac{1}{2}, P\{X=1\}=a, P\{X=3\}=b</equation>，若<equation>E(X)=0</equation>，则 D(X) =___

**答案:**# 9 2.

**解析:**解 由于<equation>P\{X=-2\}=\frac{1}{2}, P\{X=1\}=a, P\{X=3\}=b</equation>为随机变量X的分布律，故<equation>\frac{1}{2}+a+b=1</equation>即 a+b<equation>= 1</equation>，即 a+b<equation>= \frac{1}{2}.</equation>又因为<equation>E ( X )=0</equation>，所以<equation>(-2)\times \frac{1}{2}+1\times a+3\times b=0</equation>，即<equation>a+3b=1.</equation>联立<equation>\left\{ \begin{array}{l l} a+b=\frac{1}{2}, \\ a+3b=1, \end{array} \right.</equation>解得 a=b=<equation>\frac{1}{4}.</equation>代入<equation>D ( X )=\sum_{k=1}^{\infty} \left[ x_{k}-E ( X ) \right]^{2} p_{k}</equation>得，<equation>D (X) = (- 2 - 0) ^ {2} \times \frac {1}{2} + (1 - 0) ^ {2} \times \frac {1}{4} + (3 - 0) ^ {2} \times \frac {1}{4} = 2 + \frac {1}{4} + \frac {9}{4} = \frac {9}{2}.</equation>也可以利用公式<equation>D ( X )=E \left( X^{2} \right)-\left[ E ( X ) \right]^{2}</equation>来计算.<equation>E \left(X ^ {2}\right) = 4 \times \frac {1}{2} + 1 \times \frac {1}{4} + 9 \times \frac {1}{4} = \frac {9}{2}, \quad D (X) = \frac {9}{2} - 0 = \frac {9}{2}.</equation>

---


# 张宇数学公式手册


## 第一部分 高等数学


### 第三章 一元函数积分学

一、函数

二、极限

三、无穷小量与无穷大量

四、连续


一、导数与微分

二、导数的计算

三、微分中值定理

四、洛必达法则

五、函数及其性态的研究

六、曲率、曲率半径、曲率圆


一、不定积分

---


### 第七章 级 数

二、定积分

三、反常积分


一、向量代数

二、空间平面与直线

三、空间曲面与曲线


一、偏导数与全微分

二、隐函数求导法

三、方向导数

四、偏导数在几何中的应用

五、多元函数的极值


一、重积分的计算

二、重积分的应用(数学二不作要求)

三、曲线、曲面积分


一、数项级数

二、幂级数

三、傅里叶级数

---


## 第二部分 线性代数


### 第二章 矩 阵 91

一、一阶微分方程的类型及其解法 74

二、可降阶的高阶微分方程 76

三、线性微分方程解的结构定理 77

四、常系数齐次线性微分方程 78

五、二阶常系数非齐次线性微分方程 79

六、欧拉方程 81

七、差分方程 81


一、行列式的定义与性质 84

二、行列式的展开定理 86

三、几种特殊的行列式 87

四、有关行列式的若干个重要公式 90


一、矩阵的定义与运算 91

二、矩阵的秩 97

三、分块矩阵 98

四、矩阵的初等变换与初等矩阵 102

---


## 第三部分 概率论与数理统计


### 第一章 随机事件和概率

一、<equation>n</equation>维向量的定义及其运算

二、向量组的线性相(无)关性

三、极大无关组与向量组的秩

四、内积与施密特正交化

五、<equation>n</equation>维向量空间(数学二不作要求)


一、线性方程组的 4 种表示形式

二、线性方程组有解的判别条件

三、齐次线性方程组的解的结构

四、非齐次线性方程组<equation>AX=b</equation>的解的结构


一、特征值和特征向量

二、矩阵的对角化问题


一、二次型及其表示法

二、正定二次型及其判定


一、随机事件的关系及其运算

---


### 第四章 随机变量的数字特征

二、概率及其基本性质

三、概型、条件概率公式


一、分布函数

二、离散型随机变量

三、连续型随机变量

四、常见随机变量的概率分布

五、随机变量的函数的分布


一、二维随机变量的联合分布函数

二、二维离散型随机变量

三、二维连续型随机变量

四、条件分布

五、随机变量的独立性

六、二维常见分布

七、函数的分布


一、数学期望与函数期望

二、方差、协方差和矩

三、相关系数

---


#### 附录 和等数学

第五章 大数定律和中心极限定理

一、切比雪夫不等式

二、大数定律

三、中心极限定理

第六章 数理统计的基本概念

一、统计量的样本数字特征及极限

二、统计分布与抽样分布定理

第七章 参数估计

一、矩估计法

二、最大似然估计法

三、置信区间

四、常用单个正态总体参数的置信区间表


初等代数

初等几何

三角函数

平面解析几何

---


## 第一部分高等数学


### 第一章 函数、极限、连续


#### (2)有界性

设在某个过程中有两个变量 x和 y，对变量 x在允许范围内的每一个确定的值，变量 y按照某一确定的法则总有相应的值与之对应，则称 y为 x的函数，记为<equation>y = f(x)</equation>.


设函数<equation>y = f(x)</equation>的定义区间<equation>I</equation>关于原点对称，如果对于<equation>I</equation>内任意一点<equation>x</equation>，恒有<equation>f(-x) = f(x)</equation>，则称<equation>f(x)</equation>为区间<equation>I</equation>内的偶函数；如果恒有<equation>f(-x) = -f(x)</equation>，则称<equation>f(x)</equation>为区间<equation>I</equation>内的奇函数.


设函数<equation>f(x)</equation>在<equation>I</equation>上有定义，如果存在常数<equation>M</equation>，当<equation>x \in I</equation>时，恒有<equation>f(x) \leqslant M</equation>，则称<equation>f(x)</equation>在<equation>I</equation>上有上界；设函数<equation>f(x)</equation>在<equation>I</equation>上有定义，如果存在常数<equation>m</equation>，当<equation>x \in I</equation>时，恒有<equation>f(x) \geqslant m</equation>，则称<equation>f(x)</equation>在<equation>I</equation>上有下界；设函数

---


#### （3）初等函数

<equation>f(x)</equation>在<equation>I</equation>上有定义，如果存在常数<equation>M > 0</equation>，当<equation>x\in I</equation>时，恒有<equation>|f(x)|\leqslant M</equation>，则称<equation>f(x)</equation>在<equation>I</equation>上有界.


设函数<equation>f(x)</equation>在区间<equation>I</equation>上有定义，若存在<equation>T > 0</equation>，对任意的<equation>x\in I</equation>，必有<equation>x\pm T\in I</equation>，并且<equation>f(x + T) = f(x)</equation>，则称<equation>f(x)</equation>为周期函数.使得上述关系式成立的最小正数<equation>T</equation>称为<equation>f(x)</equation>的最小正周期，简称为函数<equation>f(x)</equation>的周期.


设函数<equation>f(x)</equation>在区间<equation>I</equation>内有定义，如果对于该区间内的任意两点<equation>x_{1} < x_{2}</equation>，恒有<equation>f(x_{1}) < f(x_{2})</equation>（或<equation>f(x_{1}) > f(x_{2})</equation>），则称<equation>f(x)</equation>在区间<equation>I</equation>内单调增加（或单调减少）。


设函数<equation>y = f(x)</equation>的定义域为<equation>D</equation>，值域为<equation>R</equation>.若对任意<equation>y\in R</equation>，有唯一确定的<equation>x\in D</equation>，使得<equation>y = f(x)</equation>，则记为<equation>x = f^{-1}(y)</equation>，称其为<equation>y = f(x)</equation>的反函数.


若函数<equation>u = \varphi (x)</equation>在<equation>x_{0}</equation>处有定义，函数<equation>y = f(u)</equation>在<equation>u_{0} = \varphi (x_{0})</equation>处有定义，则函数<equation>y = f[\varphi (x)]</equation>在<equation>x_{0}</equation>处有定义，称<equation>y = f[\varphi (x)]</equation>是由函数<equation>y = f(u)</equation>和<equation>u = \varphi (x)</equation>复合而成的复合函数，<equation>u</equation>为中间变量.


由六类基本初等函数经过有限次四则运算及有限

---


#### （5）隐函数

次复合运算得到的，并能用一个数学表达式表示的函数，称为初等函数.

注 六类基本初等函数为：

<equation>y=C</equation>（常数）；

<equation>y=x^{n}</equation>；

<equation>y=a^{x}</equation>（<equation>a>0</equation>且<equation>a\neq1)</equation>；

<equation>y=\log_{a} x</equation>（<equation>a>0</equation>且<equation>a\neq1)</equation>；

<equation>y=\sin x,\cos x,\tan x,\cot x,\sec x,\csc x;</equation>

<equation>y=\arcsin x,\arccos x,\arctan x,\arccot x.</equation>


在定义域内的不同范围用不同表达式表示的函数称为分段函数.

注 常见的分段函数有：

<equation>\textcircled{1}</equation>绝对值函数<equation>|x|=\left\{ \begin{array}{ll} x, & x\geqslant 0, \\ -x, & x<0. \end{array} \right.</equation>

<equation>\textcircled{2}</equation>符号函数<equation>\operatorname{sgn} x=\left\{ \begin{array}{ll} 1, & x>0, \\ 0, & x=0, \\ -1, & x<0. \end{array} \right.</equation>

<equation>\textcircled{3}</equation>取整函数<equation>[x]</equation>表示不超过 x的最大整；


如果在方程<equation>F(x,y) = 0</equation>中，当<equation>x</equation>取某区间内的任一值时，相应地总有满足这一方程的唯一的<equation>y</equation>值存在，

---


#### (1)唯一性

那么就说方程 F(x,y)=0在该区间内确定了一个隐函数 y=y(x).


若对于任意给定的正数<equation>\varepsilon</equation>，总存在正整数<equation>N</equation>，当<equation>n > N</equation>时，恒有<equation>|x_{n} - A| < \varepsilon</equation>，则称常数<equation>A</equation>为当<equation>n\to \infty</equation>时数列<equation>x_{n}</equation>的极限，记为<equation>\lim x_n = A</equation>


设函数<equation>f(x)</equation>在<equation>|x|</equation>充分大时都有定义，若对于任意给定的正数<equation>\varepsilon</equation>，总存在正数<equation>X</equation>，当<equation>|x| > X</equation>时，恒有<equation>|f(x) - A| < \varepsilon</equation>，则称常数<equation>A</equation>为当<equation>x\to \infty</equation>时函数<equation>f(x)</equation>的极限，记为<equation>\lim f(x) = A</equation>。


设函数<equation>f(x)</equation>在<equation>x_0</equation>的某个去心邻域内有定义，若对于任意给定的正数<equation>\varepsilon</equation>，总存在正数<equation>\delta</equation>，当<equation>0 < |x - x_0| < \delta</equation>时，恒有<equation>|f(x) - A| < \varepsilon</equation>，则称常数<equation>A</equation>为当<equation>x \rightarrow x_0</equation>时函数<equation>f(x)</equation>的极限，记为<equation>\lim f(x) = A</equation>。


设<equation>\lim_{x\to x_0}f(x) = A,</equation><equation>\lim_{x\to x_0}f(x) = B,</equation>则<equation>A = B.</equation>

---


#### （1）极限的四则运算法则

若<equation>\lim_{x\to x_0}f(x)</equation>存在，则存在<equation>\delta > 0</equation>，使<equation>f(x)</equation>在<equation>U = \{x|0\leqslant |x - x_0| < \delta \}</equation>内有界.


<equation>\textcircled{1}</equation>若<equation>\lim_{x\to x_0}f(x) = A > 0</equation>，则存在<equation>x_0</equation>的一个去心邻域，在该邻域内恒有<equation>f(x) > 0.</equation>

<equation>\textcircled{2}</equation>若存在<equation>x_0</equation>的一个去心邻域，在该邻域内<equation>f(x) > 0</equation>且<equation>\lim_{x\to x_0}f(x)</equation>存在，则<equation>\lim_{x\to x_0}f(x)\geqslant 0.</equation>


设在<equation>x_0</equation>的某个去心邻域内恒有<equation>g(x)\leqslant f(x)\leqslant h(x)</equation>，且<equation>\lim_{x\to x_0}g(x) = \lim_{x\to x_0}h(x) = A</equation>，则<equation>\lim_{x\to x_0}f(x) = A.</equation>

同理，若存在<equation>M > 0</equation>，使得<equation>|x| > M</equation>时，恒有<equation>g(x)\leqslant f(x)\leqslant h(x)</equation>，且<equation>\lim_{x\to \infty}g(x) = \lim_{x\to \infty}h(x) = A</equation>，则<equation>\lim_{x\to \infty}f(x) = A.</equation>


单调有界数列（函数）必有极限


(1)<equation>\lim_{x\to 0}\frac{\sin x}{x}=1.</equation>

(2)<equation>\lim_{x\to 0}(1+x)^{\frac{1}{x}}=\mathrm{e}.</equation>

---

设<equation>\lim_{x\to x_1}f(x)\stackrel{\text{存在}}{=}A,\lim_{x\to x_1}g(x)\stackrel{\text{存在}}{=}B</equation>，则

<equation>\textcircled{2}</equation><equation>\lim_{x\to x_0}[f(x)g(x)]=A\cdot B.</equation>

<equation>\textcircled{3} \lim_{x \to x_-} \frac{f(x)}{g(x)} = \frac{A}{B}</equation><equation>(B \neq 0).</equation>

(2) 一些特殊情形下的运算结论

<equation>\textcircled{1}</equation>若<equation>\lim_{x\to x}f(x) = +\infty ,\lim_{x\to x}g(x) = +\infty</equation>，则

<equation>\lim _ {x \rightarrow x _ {0}} [ f (x) + g (x) ] = + \infty .</equation>

<equation>\textcircled{2}</equation>若<equation>\lim_{x\to x_0}f(x) = -\infty ,\lim_{x\to x_0}g(x) = -\infty</equation>，则

<equation>\lim _ {x \rightarrow x _ {1}} [ f (x) + g (x) ] = - \infty .</equation>

<equation>\textcircled{3}</equation>若<equation>\lim_{x\to x_{0}}f(x)=0,g(x)</equation>在<equation>x_{0}</equation>的某个去心邻域内有界，则

<equation>\lim _ {x \rightarrow x _ {1}} [ f (x) g (x) ] = 0.</equation>

<equation>\textcircled{4}</equation>若<equation>\lim_{x\to x_{0}}f(x)=\infty</equation>，g(x)在<equation>x_{0}</equation>的某个去心邻域内有界，则

<equation>\lim _ {x \rightarrow x _ {0}} [ f (x) \pm g (x) ] = \infty .</equation>

<equation>\textcircled{5}</equation>若<equation>\lim_{x\to x_0}f(x)\stackrel{\text{存在}}{=}A\neq 0,\lim_{x\to x_0}g(x)=0</equation>，则

<equation>\lim _ {x \rightarrow x _ {0}} \frac {f (x)}{g (x)} = \infty .</equation>

---


#### 4. 无穷小量的比较

如果<equation>\lim_{x\to x_{0}}f(x)=0</equation>，则称函数 f(x)是<equation>x\to x_{0}</equation>时的无穷小量.


<equation>\textcircled{1}</equation>有限多个无穷小量的和、差、积仍然是无穷小量.

<equation>\textcircled{2}</equation>有界函数与无穷小量的乘积还是无穷小量.


<equation>\lim_{x\to x_0}f(x) = A</equation>的充分必要条件为<equation>f(x) = A + \alpha (x)</equation>其中<equation>\lim_{x\to x_0}\alpha (x) = 0.</equation>


设<equation>\alpha (x),\beta (x)</equation>是同一自变量变化过程中的无穷小量，<equation>\beta (x)\neq 0</equation>，且<equation>\lim \frac{\alpha (x)}{\beta (x)}</equation>也是此变化过程中的极限，则

<equation>\textcircled{1}</equation>若<equation>\lim \frac{\alpha (x)}{\beta (x)} = C (C</equation>为常数，且<equation>C\neq 0)</equation>，则称<equation>\alpha (x)</equation>与<equation>\beta (x)</equation>为同阶无穷小量；
