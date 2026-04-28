---


**2020年第22题 | 解答题 | 11分**


设二维随机变量<equation>(X,Y)</equation>在区域<equation>D = \{(x,y) \mid 0 < y < \sqrt{1 - x^2}\}</equation>上服从均匀分布，令<equation>Z _ {1} = \left\{ \begin{array}{l l} 1, & X - Y > 0, \\ 0, & X - Y \leqslant 0, \end{array} \right. \quad Z _ {2} = \left\{ \begin{array}{l l} 1, & X + Y > 0, \\ 0, & X + Y \leqslant 0. \end{array} \right.</equation>I. 求二维随机变量<equation>(Z_{1}, Z_{2})</equation>的概率分布；

II. 求<equation>Z_{1}</equation>与<equation>Z_{2}</equation>的相关系数.

**答案:**（I）<equation>Z_{1}</equation>和<equation>Z_{2}</equation>的联合分布律为

（Ⅱ）<equation>\frac{1}{3}.</equation><table border="1"><tr><td>Z1Z2</td><td>0</td><td>1</td></tr><tr><td>0</td><td><equation>\frac{1}{4}</equation></td><td>0</td></tr><tr><td>1</td><td><equation>\frac{1}{2}</equation></td><td><equation>\frac{1}{4}</equation></td></tr></table>

**解析:**解（I）区域 D如图（a）所示，为半径1的半圆盘，其面积为<equation>\frac{\pi}{2}</equation>由于（X，Y）服从区域 D上的均匀分布，故（X，Y）的联合概率密度为<equation>f (x, y) = \left\{ \begin{array}{l l} \frac {2}{\pi}, & (x, y) \in D, \\ 0, & \text {其 他}. \end{array} \right.</equation>（<equation>Z_{1}, Z_{2}</equation>）为二维离散型随机变量，其有4个可能取值（0，0），（0，1），（1，0），（1，1）.

由<equation>Z_{1}, Z_{2}</equation>的定义可知，<equation>Z_{1}=0</equation>当且仅当<equation>X\leqslant Y</equation>即（X，Y）落在直线<equation>y=x</equation>上或左侧，<equation>Z_{1}=1</equation>当且仅当<equation>X>Y</equation>即（X，Y）落在直线<equation>y=x</equation>右侧；<equation>Z_{2}=0</equation>当且仅当<equation>X\leqslant -Y</equation>即（X，Y）落在直线<equation>y=-x</equation>上或左侧，<equation>Z_{2}=1</equation>当且仅当<equation>X>-Y</equation>即（X，Y）落在直线<equation>y=-x</equation>右侧.区域<equation>D_{1}, D_{2}, D_{3}</equation>如图（b）所示.

(a)

(b)

下面计算<equation>\left(Z_{1},Z_{2}\right)</equation>的分布律.注意到 Y的取值均大于0.<equation>P \left\{Z _ {1} = 0, Z _ {2} = 0 \right\} = P \left\{X \leqslant Y, X \leqslant - Y \right\} = P \left\{X \leqslant - Y \right\} = \frac {D _ {1} \text {的 面 积}}{D \text {的 面 积}} = \frac {1}{4},</equation><equation>P \left\{Z _ {1} = 0, Z _ {2} = 1 \right\} = P \left\{X \leqslant Y, X > - Y \right\} = P \left\{- Y < X \leqslant Y \right\} = \frac {D _ {2} \text {的 面 积}}{D \text {的 面 积}} = \frac {1}{2},</equation><equation>P \left\{Z _ {1} = 1, Z _ {2} = 0 \right\} = P \left\{X > Y, X \leqslant - Y \right\} = 0,</equation><equation>P \left\{Z _ {1} = 1, Z _ {2} = 1 \right\} = P \left\{X > Y, X > - Y \right\} = P \left\{X > Y \right\} = \frac {D _ {3} \text {的 面 积}}{D \text {的 面 积}} = \frac {1}{4}.</equation>因此，<equation>Z_{1}</equation>和<equation>Z_{2}</equation>的联合分布律为

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

