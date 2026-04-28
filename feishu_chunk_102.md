#### 协方差与相关系数

**2024年第9题 | 选择题 | 5分 | 答案: D**
9. 设随机变量 X的概率密度为<equation>f ( x )=\left\{\begin{array}{ll}2(1-x),&0<x<1,\\ 0,&\text{其他}.\end{array}\right.</equation>在 X=x(0<x<1)的条件下，随机变量 Y服从区间 (x,1)上的均匀分布，则<equation>\operatorname{C o v} ( X, Y )=</equation>(    )

A.<equation>-\frac{1}{36}</equation>B.<equation>-\frac{1}{72}</equation>C.<equation>\frac{1}{72}</equation>D.<equation>\frac{1}{36}</equation>
答案: D
**解析: **解 由于在<equation>X=x(0<x<1)</equation>的条件下，随机变量Y服从区间（x，1）上的均匀分布，故<equation>f_{Y \mid X}(y \mid x)=\frac{1}{1-x}.</equation>记区域<equation>D=\{(x,y)\mid x<y<1,0<x<1\}</equation>，则在区域D上，<equation>(X,Y)</equation>的联合概率密度<equation>\varphi (x, y) = f _ {Y \mid X} (y \mid x) f (x) = \frac {1}{1 - x} \cdot 2 (1 - x) = 2.</equation>注意到区域 D是一个直角边长为1的等腰直角三角形区域，面积为<equation>\frac{1}{2}</equation>，故<equation>\iint_ {D} \varphi (x, y) \mathrm {d} x \mathrm {d} y = 2 \iint_ {D} \mathrm {d} x \mathrm {d} y = 1,</equation>从而可认为在<equation>D</equation>以外的区域上，<equation>\varphi (x,y) = 0.</equation>进一步可得，当<equation>0 < y < 1</equation>时，<equation>Y</equation>的边缘概率密度<equation>f _ {Y} (y) = \int_ {- \infty} ^ {+ \infty} \varphi (x, y) \mathrm {d} x = \int_ {0} ^ {y} 2 \mathrm {d} x = 2 y.</equation>当<equation>y \leqslant 0</equation>或<equation>y \geqslant 1</equation>时，<equation>f_{Y}(y) = \int_{-\infty}^{+\infty}\varphi(x,y)\mathrm{d}x = 0.</equation>由数学期望的定义可得，<equation>E (X) = \int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \int_ {0} ^ {1} x \cdot 2 (1 - x) \mathrm {d} x = \int_ {0} ^ {1} \left(2 x - 2 x ^ {2}\right) \mathrm {d} x = \left(x ^ {2} - \frac {2 x ^ {3}}{3}\right) \Bigg | _ {0} ^ {1} = \frac {1}{3},</equation><equation>E (Y) = \int_ {- \infty} ^ {+ \infty} y f _ {Y} (y) \mathrm {d} y = \int_ {0} ^ {1} y \cdot 2 y \mathrm {d} y = \left. \frac {2 y ^ {3}}{3} \right| _ {0} ^ {1} = \frac {2}{3},</equation><equation>\begin{aligned} E (X Y) &= \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} x y \varphi (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {D} 2 x y \mathrm {d} x \mathrm {d} y = 2 \int_ {0} ^ {1} y \mathrm {d} y \int_ {0} ^ {y} x \mathrm {d} x = 2 \int_ {0} ^ {1} y \cdot \frac {y ^ {2}}{2} \mathrm {d} y \\ &= \left. \frac {y ^ {4}}{4} \right| _ {0} ^ {1} = \frac {1}{4}. \end{aligned}</equation>因此，<equation>\operatorname {C o v} (X, Y) = E (X Y) - E (X) E (Y) = \frac {1}{4} - \frac {1}{3} \times \frac {2}{3} = \frac {1}{3 6}.</equation>应选 D.

---

**2023年第22题 | 解答题 | 12分**
. (本题满分12分)

设二维随机变量（X，Y）的概率密度为<equation>f ( x, y )=\left\{\begin{array}{ll}\frac{2}{\pi} \left(x^{2}+y^{2}\right),&x^{2}+y^{2}\leqslant 1\\ 0,&\text{其它}\end{array} \right.</equation>I. 求 X与 Y的斜方差；

II. 求 X与 Y是否相互独立；

III. 求<equation>Z=X^{2}+Y^{2}</equation>的概率密度.
**答案: **(I) Cov(X,Y) = 0;

（Ⅱ）X与Y不相互独立；

（Ⅲ）Z的概率密度<equation>f_{Z}(z)=\left\{ \begin{array}{ll} 2z, & 0<z<1, \\ 0, & \text{其他}. \end{array} \right.</equation>
**解析: **解（I）由<equation>f ( x,y )</equation>的定义可知，当<equation>| x | > 1</equation>时，<equation>f ( x,y ) = 0</equation>，当<equation>| x | \leqslant 1</equation>时，<equation>f ( x,y )</equation>仅在<equation>- \sqrt{1-x^{2}}\leqslant y\leqslant \sqrt{1-x^{2}}</equation>时非零.<equation>\begin{aligned} f _ {X} (x) &= \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} y = \frac {2}{\pi} \int_ {- \sqrt {1 - x ^ {2}}} ^ {\sqrt {1 - x ^ {2}}} \left(x ^ {2} + y ^ {2}\right) \mathrm {d} y = \frac {4}{\pi} \int_ {0} ^ {\sqrt {1 - x ^ {2}}} \left(x ^ {2} + y ^ {2}\right) \mathrm {d} y \\ &= \frac {4}{\pi} \left[ x ^ {2} \sqrt {1 - x ^ {2}} + \frac {\left(1 - x ^ {2}\right) ^ {\frac {3}{2}}}{3} \right] = \frac {4}{3 \pi} \sqrt {1 - x ^ {2}} \left(1 + 2 x ^ {2}\right), \end{aligned}</equation>即<equation>f_{X}(x) = \left\{ \begin{array}{ll}\frac{4}{3\pi}\sqrt{1 - x^{2}}(1 + 2x^{2}), & |x|\leqslant 1,\\ 0, & |x| > 1. \end{array} \right.</equation>同理可得<equation>f _ {Y} (y) = \left\{ \begin{array}{l l} \frac {4}{3 \pi} \sqrt {1 - y ^ {2}} \left(1 + 2 y ^ {2}\right), & | y | \leqslant 1, \\ 0, & | y | > 1. \end{array} \right.</equation>(a)

(b)

记<equation>D = \{(x,y)\mid x^{2} + y^{2}\leqslant 1\} .</equation>如图（a）所示，区域D关于x轴，y轴均对称.进一步计算可得<equation>E (X) = \int_ {- \infty} ^ {+ \infty} x f _ {X} (x) \mathrm {d} x = \int_ {- 1} ^ {1} \frac {4 x}{3 \pi} \sqrt {1 - x ^ {2}} \left(1 + 2 x ^ {2}\right) \mathrm {d} x \stackrel {\text {对称性}} {=} 0,</equation><equation>E (Y) \stackrel {\text {同 理}} {=} 0,</equation><equation>E (X Y) = \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} x y f (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {D} x y \cdot \frac {2}{\pi} \left(x ^ {2} + y ^ {2}\right) \mathrm {d} x \mathrm {d} y \stackrel {\text {对称 性}} {=} 0,</equation>从而<equation>\operatorname{Cov}(X, Y) = E(XY) - E(X)E(Y) = 0.</equation>（Ⅱ）由第（I）问可知，<equation>f_{X}(x)f_{Y}(y)\neq f(x,y)</equation>，故X与Y不相互独立.

（Ⅲ）记<equation>Z = X^{2} + Y^{2}</equation>的分布函数为<equation>F_{Z}(z), D_{z} = \{(x,y)|x^{2} + y^{2}\leqslant z\} .</equation>当<equation>z < 0</equation>时，<equation>F_{Z}(z) = P\{Z\leqslant z\} = 0.</equation>当<equation>0 \leqslant z < 1</equation>时，<equation>D \cap D_{z} = D_{z}</equation>，如图（b）所示.<equation>\begin{array}{l} F _ {Z} (z) = P \left\{Z \leqslant z \right\} = \iint_ {D _ {z}} \frac {2}{\pi} \left(x ^ {2} + y ^ {2}\right) \mathrm {d} x \mathrm {d} y = \frac {2}{\pi} \int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {0} ^ {\sqrt {z}} r ^ {2} \cdot r \mathrm {d} r \\ = \frac {2}{\pi} \cdot 2 \pi \cdot \frac {r ^ {4}}{4} \Bigg | _ {0} ^ {\sqrt {z}} = z ^ {2}. \\ \end{array}</equation>当<equation>z \geqslant 1</equation>时，<equation>F_{Z}(z) = P\{Z \leqslant z\} = 1.</equation>因此，<equation>Z</equation>的分布函数<equation>F_{Z}(z) = \left\{ \begin{array}{ll}0, & z < 0,\\ z^{2}, & 0\leqslant z < 1,\\ 1, & z\geqslant 1, \end{array} \right.</equation>概率密度<equation>f_{Z}(z) = F_{Z}^{\prime}(z) = \left\{ \begin{array}{ll}2z, & 0 < z < 1,\\ 0, & \text{其他}. \end{array} \right.</equation>

---

**2022年第8题 | 选择题 | 5分 | 答案: C**
8. 设随机变量 X服从区间（0,3）上的均匀分布，随机变量 Y服从参数为2的泊松分布，且 X与 Y的协方差为 -1，则<equation>D(2X-Y+1)=</equation>(    )

A.1 B.5 C.9 D.12
答案: C
**解析: **解 由于 X服从区间（0,3）上的均匀分布，故 X的方差<equation>D ( X )=\frac{(3-0)^{2}}{1 2}=\frac{3}{4}.</equation>又由于 Y服从参数为2的泊松分布，故 Y的方差<equation>D ( Y )=2.</equation>由方差的性质，<equation>\begin{aligned} D (2 X - Y + 1) &= D (2 X - Y) = D (2 X) + D (Y) - 2 \operatorname {C o v} (2 X, Y) \\ &= 4 D (X) + D (Y) - 4 \operatorname {C o v} (X, Y) = 4 \times \frac {3}{4} + 2 - 4 \times (- 1) = 9. \end{aligned}</equation>因此，应选C.

---

**2022年第10题 | 选择题 | 5分 | 答案: D**
10. 设随机变量<equation>X\sim N(0,1)</equation>，若在<equation>X=x</equation>的条件下，随机变量<equation>Y\sim N(x,1)</equation>，则 X与Y的相关系数为（    ）

A.<equation>\frac{1}{4}</equation>B.<equation>\frac{1}{2}</equation>C.<equation>\frac{\sqrt{3}}{3}</equation>D.<equation>\frac{\sqrt{2}}{2}</equation>
答案: D
**解析: **解（法一）由于<equation>X\sim N(0,1)</equation>，故<equation>X</equation>的概率密度函数为<equation>f _ {X} (x) = \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {x ^ {2}}{2}}.</equation>由于在<equation>X = x</equation>的条件下，<equation>Y\sim N(x,1)</equation>，故在<equation>X = x</equation>的条件下，<equation>Y</equation>的条件概率密度为<equation>f _ {Y \mid X} (y \mid x) = \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {(y - x) ^ {2}}{2}}.</equation>于是，二维随机变量<equation>(X, Y)</equation>的联合概率密度为<equation>f (x, y) = f _ {X} (x) f _ {Y \mid X} (y \mid x) = \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \cdot \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {(y - x) ^ {2}}{2}} = \frac {1}{2 \pi} \mathrm {e} ^ {- x ^ {2} + x y - \frac {y ^ {2}}{2}}.</equation>计算<equation>Y</equation>的边缘概率密度<equation>f_{Y}(y)</equation>. 对<equation>y \in (-\infty, +\infty)</equation>，<equation>\begin{aligned} f _ {Y} (y) &= \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} x = \int_ {- \infty} ^ {+ \infty} \frac {1}{2 \pi} \mathrm {e} ^ {- x ^ {2} + x y - \frac {y ^ {2}}{2}} \mathrm {d} x = \frac {1}{2 \sqrt {\pi}} \mathrm {e} ^ {- \frac {y ^ {2}}{4}} \int_ {- \infty} ^ {+ \infty} \frac {1}{\sqrt {2 \pi} \cdot \frac {\sqrt {2}}{2}} \mathrm {e} ^ {- (x - \frac {y}{2}) ^ {2}} \mathrm {d} x \\ &= \frac {1}{2 \sqrt {\pi}} \mathrm {e} ^ {- \frac {y ^ {2}}{4}} = \frac {1}{\sqrt {2 \pi} \cdot \sqrt {2}} \mathrm {e} ^ {- \frac {y ^ {2}}{2 (\sqrt {2}) ^ {2}}}. \end{aligned}</equation>于是，<equation>(X,Y)</equation>关于<equation>Y</equation>的边缘分布是正态分布<equation>N(0,2)</equation>.

结合<equation>f(x,y)</equation>与二维正态分布的概率密度的形式，取<equation>\mu_{1} = 0,\mu_{2} = 0,\sigma_{1} = 1,\sigma_{2} = \sqrt{2}</equation><equation>\frac {1}{2 \pi} \mathrm {e} ^ {- x ^ {2} + x y - \frac {y ^ {2}}{2}} = \frac {1}{2 \pi \cdot 1 \cdot \sqrt {2} \cdot \frac {\sqrt {2}}{2}} \cdot \mathrm {e} ^ {- \frac {1}{2} \cdot \frac {1}{2}} \left[ \frac {(x - 0) ^ {2}}{1 ^ {2}} - 2 \cdot \frac {\sqrt {2}}{2} \frac {(x - 0) (y - 0)}{1 \cdot \sqrt {2}} + \frac {(y - 0) ^ {2}}{(\sqrt {2}) ^ {2}} \right].</equation>因此，取<equation>\rho = \frac{\sqrt{2}}{2}</equation>，则<equation>(X,Y)</equation>服从二维正态分布<equation>N\left(0,0;1,2;\frac{\sqrt{2}}{2}\right)</equation>.

由二维正态分布的概率密度的参数的含义可知，<equation>\rho_{X Y}=\frac{\sqrt{2}}{2}</equation>，应选D.

（法二）计算<equation>\rho_{X Y}.</equation>先计算 E(XY).

由法一可得<equation>f(x,y) = \frac{1}{2\pi}\mathrm{e}^{-x^2 + xy - \frac{y^2}{2}}.</equation>于是，<equation>\begin{aligned} E (X Y) &= \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} x y f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {- \infty} ^ {+ \infty} x \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \mathrm {d} x \int_ {- \infty} ^ {+ \infty} y \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {(y - x) ^ {2}}{2}} \mathrm {d} y \\ &= \int_ {- \infty} ^ {+ \infty} x \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \mathrm {d} x \left[ \int_ {- \infty} ^ {+ \infty} \frac {1}{\sqrt {2 \pi}} (y - x) \mathrm {e} ^ {- \frac {(y - x) ^ {2}}{2}} \mathrm {d} y + x \int_ {- \infty} ^ {+ \infty} \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {(y - x) ^ {2}}{2}} \mathrm {d} (y - x) \right] \\ &= \int_ {- \infty} ^ {+ \infty} x \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {x ^ {2}}{2}} (0 + x) \mathrm {d} x = \int_ {- \infty} ^ {+ \infty} x ^ {2} \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \mathrm {d} x. \end{aligned}</equation>又因为<equation>\int_{-\infty}^{+\infty}x^{2}\frac{1}{\sqrt{2\pi}}\mathrm{e}^{-\frac{x^{2}}{2}}\mathrm{d}x = E(X^{2})</equation>，而<equation>X\sim N(0,1)</equation>，所以<equation>E(X^{2}) = D(X) + [E(X)]^{2} = 1.</equation>从而，<equation>E(XY) = 1.</equation>又由法一可得<equation>Y\sim N(0,2)</equation>，故<equation>E(Y)=0,D(Y)=2.</equation>因此，<equation>\rho_ {X Y} = \frac {\operatorname {C o v} (X , Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {1 - 0}{\sqrt {2}} = \frac {\sqrt {2}}{2}.</equation>

---

**2021年第16题 | 填空题 | 5分**
16. 甲、乙两个盒子中各装有2个红球和2个白球，先从甲盒中任取一球，观察颜色后放入乙盒中，再从乙盒中任取一球，令 X, Y分别表示从甲盒和乙盒中取到的红球个数，则 X与 Y的相关系数为 ___.
**答案: **# 1 5.
**解析: **根据相关系数的计算公式，X与Y的相关系数为<equation>\rho = \frac {\operatorname {C o v} (X , Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}}.</equation>下面分别计算<equation>X, Y</equation>的分布律与数字特征.

取球模型为等可能模型.<equation>X</equation>的可能取值为0，1. 取到白球，则<equation>X = 0</equation>；取到红球，则<equation>X = 1</equation><equation>P \{X = 0 \} = \frac {1}{2}, \quad P \{X = 1 \} = \frac {1}{2}.</equation>于是，<equation>E ( X ) = \frac {1}{2}, E \left( X^{2}\right) = \frac {1}{2}, D ( X ) = \frac {1}{2} - \left(\frac {1}{2}\right)^{2} = \frac {1}{4}.</equation>Y的可能取值为0，1.若从甲盒中取出的是白球，则后来乙盒中共有2个红球和3个白球，取到红球的概率为<equation>\frac{2}{5}</equation>即在X=0发生的条件下Y=1发生的概率为<equation>\frac{2}{5}</equation>；若从甲盒中取出的是红球，则后来乙盒中共有3个红球和2个白球，取到红球的概率为<equation>\frac{3}{5}</equation>即在X=1发生的条件下Y=1发生的概率为<equation>\frac{3}{5}.</equation><equation>\begin{aligned} P \{Y = 1 \} &= P \{Y = 1 \mid X = 0 \} P \{X = 0 \} + P \{Y = 1 \mid X = 1 \} P \{X = 1 \} \\ &= \frac {2}{5} \times \frac {1}{2} + \frac {3}{5} \times \frac {1}{2} = \frac {1}{2}. \end{aligned}</equation><equation>P \{Y = 0 \} = 1 - P \{Y = 1 \} = 1 - \frac {1}{2} = \frac {1}{2}.</equation>于是，<equation>E ( Y ) = \frac {1}{2}, E ( Y^{2} ) = \frac {1}{2}, D ( Y ) = \frac {1}{2} - \left(\frac {1}{2}\right)^{2} = \frac {1}{4}.</equation>XY的可能取值为0,1.<equation>P \{X Y = 1 \} = P \{X = 1, Y = 1 \} = P \{Y = 1 \mid X = 1 \} P \{X = 1 \} = \frac {3}{5} \times \frac {1}{2} = \frac {3}{1 0}.</equation><equation>P \left\{X Y = 0 \right\} = 1 - \frac {3}{1 0} = \frac {7}{1 0}.</equation>于是，<equation>E ( X Y ) = P \{ X Y = 1 \} \times 1 + P \{ X Y = 0 \} \times 0 = \frac {3}{1 0}.</equation>因此，<equation>\rho = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {\frac {3}{1 0} - \frac {1}{2} \times \frac {1}{2}}{\frac {1}{2} \times \frac {1}{2}} = \frac {\frac {1}{2 0}}{\frac {1}{4}} = \frac {1}{5}.</equation>

---

**2020年第14题 | 填空题 | 4分**
14. 设 X 服从区间<equation>\left(-\frac{\pi}{2},\frac{\pi}{2}\right)</equation>上的均匀分布，<equation>Y=\sin X</equation>，则<equation>\operatorname{Cov}(X,Y)=</equation>___
**答案: **# 2 π.
**解析: **解 由 X服从<equation>\left(-\frac{\pi}{2},\frac{\pi}{2}\right)</equation>上的均匀分布可知，<equation>f(x)=\left\{\begin{array}{ll}\frac{1}{\pi},&x\in\left(-\frac{\pi}{2},\frac{\pi}{2}\right),\\ 0,&\text{其他}.\end{array}\right.</equation><equation>E (X) = \int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \frac {1}{\pi} \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} x \mathrm {d} x = 0.</equation>根据协方差的计算公式，<equation>\begin{aligned} \operatorname {C o v} (X, Y) &= \operatorname {C o v} (X, \sin X) = E (X \sin X) - E (X) E (\sin X) \xlongequal {E (X) = 0} \int_ {- \infty} ^ {+ \infty} x \sin x f (x) \mathrm {d} x - 0 \\ &= \frac {1}{\pi} \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} x \sin x \mathrm {d} x \xlongequal {\text {对称性}} \frac {2}{\pi} \int_ {0} ^ {\frac {\pi}{2}} x \sin x \mathrm {d} x = - \frac {2}{\pi} \int_ {0} ^ {\frac {\pi}{2}} x \mathrm {d} (\cos x) \\ &= - \frac {2}{\pi} \left(x \cos x \Big | _ {0} ^ {\frac {\pi}{2}} - \int_ {0} ^ {\frac {\pi}{2}} \cos x \mathrm {d} x\right) = - \frac {2}{\pi} \times (0 - 1) = \frac {2}{\pi}. \end{aligned}</equation>

---

**2018年第22题 | 解答题 | 11分**
22. (本题满分11分)

设随机变量 X与 Y相互独立，X的概率分布为<equation>P\{X=1\}=P\{X=-1\}=\frac{1}{2},</equation>Y服从参数为<equation>\lambda</equation>的泊松分布.令<equation>Z=XY.</equation>I. 求<equation>\operatorname{Cov}(X,Z)</equation>;

II. 求 Z的概率分布.
**答案: **（ I ）<equation>\operatorname{C o v} ( X, Z ) = \lambda</equation>（Ⅱ）Z的分布律为<equation>P\{Z = i\} = \left\{ \begin{array}{ll}\frac{1}{2}\cdot \frac{\lambda^{i}\mathrm{e}^{-\lambda}}{i!}, & i > 0,\\ \mathrm{e}^{-\lambda}, & i = 0,\\ \frac{1}{2}\cdot \frac{\lambda^{-i}\mathrm{e}^{-\lambda}}{(-i)!}, & i < 0. \end{array} \right.</equation>
**解析: **解（I）（法一）注意到<equation>X</equation>与Y相互独立，故<equation>X^{2}</equation>与Y也相互独立.

根据协方差的计算公式，<equation>\begin{aligned} \operatorname {C o v} (X, Z) &= E (X Z) - E (X) E (Z) \stackrel {Z = X Y} {=} E \left(X ^ {2} Y\right) - E (X) E (X Y) \\ \stackrel {\text {独立 性}} {=} E \left(X ^ {2}\right) E (Y) - \left[ E (X) \right] ^ {2} E (Y). \end{aligned}</equation>由于 X的概率分布为<equation>P \{ X=1 \} = P \{ X=-1 \} = \frac{1}{2}</equation>，故<equation>E (X) = 1 \times \frac {1}{2} + (- 1) \times \frac {1}{2} = 0, \quad E \left(X ^ {2}\right) = 1 ^ {2} \times \frac {1}{2} + (- 1) ^ {2} \times \frac {1}{2} = 1.</equation>又因为<equation>Y</equation>服从参数为<equation>\lambda</equation>的泊松分布，所以<equation>E(Y) = \lambda</equation>因此，<equation>\operatorname {C o v} (X, Z) = E \left(X ^ {2}\right) E (Y) - \left[ E (X) \right] ^ {2} E (Y) = 1 \times \lambda - 0 = \lambda .</equation>（法二）由于<equation>X^{2}=1</equation>，故<equation>XZ=X(XY)=X^{2}Y=Y</equation>，而Y服从参数为<equation>\lambda</equation>的泊松分布，于是，<equation>E(XZ)=E(Y)=\lambda.</equation>由法一可知，<equation>E ( X ) = 0</equation>因此，<equation>\operatorname {C o v} (X, Z) = E (X Z) - E (X) E (Z) = \lambda - 0 = \lambda .</equation>（Ⅱ）由于<equation>Z = XY</equation>，故<equation>Z</equation>的所有可能的取值为<equation>i</equation>，其中<equation>i</equation>为整数.

当 i > 0时，<equation>\begin{aligned} P \{Z = i \} &= P \{X Y = i \} = P \{X = 1, Y = i \} \xlongequal {\text {独立 性}} P \{X = 1 \} P \{Y = i \} \\ &= \frac {1}{2} \cdot \frac {\lambda^ {i} \mathrm {e} ^ {- \lambda}}{i !}. \end{aligned}</equation>当 i = 0时，<equation>P \{Z = 0 \} = P \{X Y = 0 \} \xlongequal {X \text {不 为} 0} P \{Y = 0 \} = \mathrm {e} ^ {- \lambda}.</equation>当 i < 0时，<equation>\begin{aligned} P \{Z = i \} &= P \{X Y = i \} = P \{X = - 1, Y = - i \} \xlongequal {\text {独立性}} P \{X = - 1 \} P \{Y = - i \} \\ &= \frac {1}{2} \cdot \frac {\lambda^ {- i} \mathrm {e} ^ {- \lambda}}{(- i) !}. \end{aligned}</equation>因此，Z的分布律为<equation>P\{Z = i\} = \left\{ \begin{array}{ll}\frac{1}{2}\cdot \frac{\lambda^{i}\mathrm{e}^{-\lambda}}{i!}, & i > 0,\\ \mathrm{e}^{-\lambda}, & i = 0,\\ \frac{1}{2}\cdot \frac{\lambda^{-i}\mathrm{e}^{-\lambda}}{(-i)!}, & i < 0. \end{array} \right.</equation>

---

**2016年第8题 | 选择题 | 4分 | 答案: A**
8. 随机试验 E有三种两两不相容的结果<equation>A_{1}, A_{2}, A_{3}</equation>，且三种结果发生的概率均为<equation>\frac{1}{3}</equation>，将试验 E独立重复做2次， X表示2次试验中结果<equation>A_{1}</equation>发生的次数，Y表示2次试验中结果<equation>A_{2}</equation>发生的次数，则 X与 Y的相关系数为（    )

A.<equation>-\frac{1}{2}</equation>B.<equation>-\frac{1}{3}</equation>C.<equation>\frac{1}{3}</equation>D.<equation>\frac{1}{2}</equation>
答案: A
**解析: **解（法一）由题设知，<equation>X\sim B\left(2,\frac{1}{3}\right),Y\sim B\left(2,\frac{1}{3}\right)</equation>，从而<equation>E (X) = E (Y) = 2 \times \frac {1}{3} = \frac {2}{3}, \quad D (X) = D (Y) = 2 \times \frac {1}{3} \times \left(1 - \frac {1}{3}\right) = \frac {4}{9}.</equation>又 XY所有可能的取值为0，1，故<equation>E ( X Y ) = 0 \cdot P \{ X Y = 0 \} + 1 \cdot P \{ X Y = 1 \} = P \{ X = 1, Y = 1 \} = \mathrm {C} _ {2} ^ {1} \times \frac {1}{3} \times \frac {1}{3} = \frac {2}{9},</equation>从而<equation>\rho_{X Y}=\frac{E(X Y)-E(X)E(Y)}{\sqrt{D(X)}\sqrt{D(Y)}}=\frac{\frac{2}{9}-\frac{2}{3}\times \frac{2}{3}}{\frac{4}{9}}=-\frac{1}{2}.</equation>应选A.

（法二）记Z表示2次试验中结果<equation>A_{3}</equation>发生的次数，则<equation>X+Y+Z=2</equation>从而<equation>D (Z) = D (2 - X - Y) = D (X + Y) = D (X) + D (Y) + 2 \operatorname {C o v} (X, Y).</equation>又由题设知，<equation>D ( X )=D ( Y )=D ( Z )</equation>，故<equation>D ( X )=-2\operatorname{C o v} ( X , Y )</equation>，从而<equation>\rho_ {X Y} = \frac {\operatorname {C o v} (X , Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {\operatorname {C o v} (X , Y)}{D (X)} = - \frac {1}{2}.</equation>应选A.

---

**2015年第8题 | 选择题 | 4分 | 答案: D**
8. 设随机变量 X,Y不相关，且<equation>E ( X )=2, E ( Y )=1, D ( X )=3</equation>，则<equation>E [ X ( X+Y-2) ]=</equation>(    )

A. -3 B. 3 C. -5 D. 5
答案: D
**解析: **解 由题设知，<equation>\rho_{XY}=\frac{\operatorname{Cov}(X,Y)}{\sqrt{D(X)}\sqrt{D(Y)}}=\frac{E(XY)-E(X)E(Y)}{\sqrt{D(X)}\sqrt{D(Y)}}=0</equation>，从而<equation>E(XY)=E(X)E(Y)</equation>于是<equation>\begin{aligned} E [ X (X + Y - 2) ] &= E \left(X ^ {2}\right) + E (X Y) - 2 E (X) \\ &= D (X) + \left[ E (X) \right] ^ {2} + E (X) E (Y) - 2 E (X) \\ &= 3 + 4 + 2 - 4 = 5. \end{aligned}</equation>应选 D.

---

**2012年第8题 | 选择题 | 4分 | 答案: D**
8. 将长度为1m的木棒随机地截成两段，则两段长度的相关系数为（    ）

A. 1 B.<equation>\frac{1}{2}</equation>C.<equation>-\frac{1}{2}</equation>D. -1
答案: D
**解析: **解（法一）设木棒被截成两段的长度分别为 X，Y，则有 X+Y=1，即 Y=1-X.于是<equation>D(Y)=D(1-X)=D(X),</equation><equation>\operatorname{Cov}(X,Y)=\operatorname{Cov}(X,1-X)=-\operatorname{Cov}(X,X)=-D(X),</equation>从而<equation>\rho_ {X Y} = \frac {\operatorname {C o v} (X , Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {- D (X)}{\sqrt {D (X)} \sqrt {D (X)}} = - 1.</equation>应选 D.

（法二）由于<equation>|\rho_{XY}|=1</equation>的充要条件是存在常数 a,b，使得<equation>P\{Y=a+bX\}=1</equation>，且此时<equation>\rho_{XY}=\frac{b}{|b|}</equation>由于 Y=1-X，故<equation>\rho_{XY}=-1</equation>从而选D.

---

**2012年第22题 | 解答题 | 11分**

设二维离散型随机变量<equation>(X, Y)</equation>的概率分布为

<table border="1"><tr><td>X\ Y</td><td>0</td><td>1</td><td>2</td></tr><tr><td>0</td><td>1/4</td><td>0</td><td>1/4</td></tr><tr><td>1</td><td>0</td><td>1/3</td><td>0</td></tr><tr><td>2</td><td>1/12</td><td>0</td><td>1/12</td></tr></table>

I. 求<equation>P\{X = 2Y\}</equation>;

II. 求<equation>\operatorname{Cov}(X - Y, Y)</equation>.
**答案: **(22) （ I )<equation>P \{ X=2 Y \}=\frac{1}{4}</equation>；

（Ⅱ）<equation>\operatorname{C o v} ( X-Y, Y)=-\frac{2}{3}.</equation>
**解析: **（ I ）由题设知，<equation>P \{X = 2 Y \} = P \{X = 0, Y = 0 \} + P \{X = 2, Y = 1 \} = \frac {1}{4} + 0 = \frac {1}{4}.</equation>（Ⅱ）由<equation>(X,Y)</equation>的概率分布知，<equation>X,Y</equation>的概率分布分别为

<table border="1"><tr><td>X</td><td>0</td><td>1</td><td>2</td></tr><tr><td>P</td><td><equation>\frac{1}{2}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{6}</equation></td></tr></table>

<table border="1"><tr><td>Y</td><td>0</td><td>1</td><td>2</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td></tr></table>

又由于随机变量 XY可能的值为0，1，2，4，故XY的概率分布为<equation>\begin{aligned} P \{X Y = 0 \} &= P \{X = 0, Y = 0 \} + P \{X = 0, Y = 1 \} + P \{X = 0, Y = 2 \} \\ + P \{X = 1, Y = 0 \} + P \{X = 2, Y = 0 \} \\ &= \frac {1}{4} + 0 + \frac {1}{4} + 0 + \frac {1}{1 2} = \frac {7}{1 2}, \end{aligned}</equation><equation>P \left\{X Y = 1 \right\} = P \left\{X = 1, Y = 1 \right\} = \frac {1}{3},</equation><equation>P \left\{X Y = 2 \right\} = P \left\{X = 1, Y = 2 \right\} + P \left\{X = 2, Y = 1 \right\} = 0 + 0 = 0,</equation><equation>P \{X Y = 4 \} = P \{X = 2, Y = 2 \} = \frac {1}{1 2},</equation>即

<table border="1"><tr><td>XY</td><td>0</td><td>1</td><td>4</td></tr><tr><td>P</td><td><equation>\frac{7}{12}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{12}</equation></td></tr></table>

于是，<equation>E (X) = 0 \times \frac {1}{2} + 1 \times \frac {1}{3} + 2 \times \frac {1}{6} = \frac {2}{3},</equation><equation>E (Y) = 0 \times \frac {1}{3} + 1 \times \frac {1}{3} + 2 \times \frac {1}{3} = 1,</equation><equation>E \left(Y ^ {2}\right) = 0 ^ {2} \times \frac {1}{3} + 1 ^ {2} \times \frac {1}{3} + 2 ^ {2} \times \frac {1}{3} = \frac {5}{3},</equation><equation>E (X Y) = 0 \times \frac {7}{1 2} + 1 \times \frac {1}{3} + 4 \times \frac {1}{1 2} = \frac {2}{3}.</equation>因此，<equation>\begin{aligned} \operatorname {C o v} (X - Y, Y) &= \operatorname {C o v} (X, Y) - \operatorname {C o v} (Y, Y) = \left[ E (X Y) - E (X) E (Y) \right] - \left[ E \left(Y ^ {2}\right) - \left[ E (Y) \right] ^ {2} \right] \\ &= \left(\frac {2}{3} - \frac {2}{3} \times 1\right) - \left(\frac {5}{3} - 1 ^ {2}\right) = - \frac {2}{3}. \end{aligned}</equation>

---

**2011年第14题 | 填空题 | 4分**
14. 设二维随机变量<equation>(X, Y)</equation>服从正态分布<equation>N\left(\mu, \mu; \sigma^2, \sigma^2; 0\right)</equation>, 则<equation>E(XY^2) =</equation>___
**答案: **##<equation>\mu\sigma^{2}+\mu^{3}.</equation>
**解析: **解由（X，Y）服从正态分布<equation>N(\mu ,\mu ;\sigma^{2},\sigma^{2};0)</equation>知，<equation>X\sim N(\mu ,\sigma^{2}),Y\sim N(\mu ,\sigma^{2})</equation>且<equation>\rho_{XY}=0.</equation>由于对二维正态随机变量，不相关与相互独立等价，故X与Y相互独立，从而X与<equation>Y^{2}</equation>相互独立.于是<equation>E(XY^{2})=E(X)E(Y^{2})=E(X)[D(Y)+[E(Y)]^{2}]</equation><equation>=\mu(\sigma^{2}+\mu^{2})=\mu\sigma^{2}+\mu^{3}.</equation>

---

**2011年第22题 | 解答题 | 11分**

设随机变量<equation>X</equation>与<equation>Y</equation>的概率分布分别为

<table border="1"><tr><td>X</td><td>0</td><td>1</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{2}{3}</equation></td></tr></table>

<table border="1"><tr><td>Y</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td></tr></table>

且<equation>P \left\{X^{2}=Y^{2}\right\}=1.</equation>I. 求二维随机变量（X,Y）的概率分布；

II. 求<equation>Z=XY</equation>的概率分布；

III. 求 X与Y的相关系数<equation>\rho_{XY}</equation>.
**答案: **(22) （I）

<table border="1"><tr><td rowspan="2">X\ Y</td><td colspan="3">-1</td></tr><tr><td>0</td><td>1/3</td><td>0</td></tr><tr><td>1</td><td>1/3</td><td>0</td><td>1/3</td></tr><tr><td>Z</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>P</td><td>1/3</td><td>1/3</td><td>1/3</td></tr></table>

(Ⅱ)

( III ) 0.
**解析: **（I）由<equation>P\{X^{2} = Y^{2}\} = 1</equation>知，<equation>P\{X^{2}\neq Y^{2}\} = 0.</equation>于是，<equation>P \{X = 0, Y = - 1 \} = P \{X = 0, Y = 1 \} = P \{X = 1, Y = 0 \} = 0.</equation>从而<equation>P \{X = 0, Y = 0 \} = P \{Y = 0 \} - P \{X = 1, Y = 0 \} = \frac {1}{3} - 0 = \frac {1}{3},</equation><equation>P \{X = 1, Y = 1 \} = P \{Y = 1 \} - P \{X = 0, Y = 1 \} = \frac {1}{3} - 0 = \frac {1}{3},</equation><equation>P \{X = 1, Y = - 1 \} = P \{Y = - 1 \} - P \{X = 0, Y = - 1 \} = \frac {1}{3} - 0 = \frac {1}{3}.</equation>因此，<equation>( X, Y )</equation>的概率分布为

<table border="1"><tr><td>X\ Y</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>0</td><td><equation>\frac{1}{3}</equation></td><td>0</td></tr><tr><td>1</td><td><equation>\frac{1}{3}</equation></td><td>0</td><td><equation>\frac{1}{3}</equation></td></tr></table>

（Ⅱ）由于<equation>Z=XY</equation>可能的取值为-1，0，1，且<equation>P \{Z = - 1 \} = P \{X = 1, Y = - 1 \} = \frac {1}{3},</equation><equation>P \{Z = 1 \} = P \{X = 1, Y = 1 \} = \frac {1}{3},</equation><equation>P \{Z = 0 \} = 1 - P \{Z = - 1 \} - P \{Z = 1 \} = \frac {1}{3},</equation>故 Z = XY的概率分布为

<table border="1"><tr><td>Z</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td></tr></table>

（Ⅲ）由于<equation>E (X) = 0 \times \frac {1}{3} + 1 \times \frac {2}{3} = \frac {2}{3}, \quad E \left(X ^ {2}\right) = 0 ^ {2} \times \frac {1}{3} + 1 ^ {2} \times \frac {2}{3} = \frac {2}{3},</equation><equation>D (X) = E \left(X ^ {2}\right) - \left[ E (X) \right] ^ {2} = \frac {2}{9},</equation><equation>E (Y) = (- 1) \times \frac {1}{3} + 0 \times \frac {1}{3} + 1 \times \frac {1}{3} = 0, \quad E \left(Y ^ {2}\right) = (- 1) ^ {2} \times \frac {1}{3} + 0 ^ {2} \times \frac {1}{3} + 1 ^ {2} \times \frac {1}{3} = \frac {2}{3},</equation><equation>D (Y) = E \left(Y ^ {2}\right) - \left[ E (Y) \right] ^ {2} = \frac {2}{3},</equation><equation>E (X Y) = E (Z) = (- 1) \times \frac {1}{3} + 0 \times \frac {1}{3} + 1 \times \frac {1}{3} = 0,</equation>故<equation>\rho_ {X Y} = \frac {\operatorname {C o v} (X , Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = 0.</equation>

---


### 随机变量及其分布

**2025年第9题 | 选择题 | 5分 | 答案: C**
9. 设<equation>X_{1}, X_{2}, \dots , X_{2 0}</equation>是来自总体B(1,0.1)的简单随机样本，令<equation>T=\sum_{i=1}^{2 0} X_{i}</equation>利用泊松分布近似表示二项分布的方法可得<equation>P\{ T\leqslant 1\}\approx</equation>(    )

A.<equation>\frac{1} {\mathrm{e}^{2}}</equation>B.<equation>\frac{2} {\mathrm{e}^{2}}</equation>C.<equation>\frac{3} {\mathrm{e}^{2}}</equation>D.<equation>\frac{4} {\mathrm{e}^{2}}</equation>
答案: C
**解析: **解 由<equation>X_{i}(i = 1,2,\dots ,20)\sim B(1,0.1)</equation>可知，<equation>X_{i}</equation>可看作一次随机试验的结果，试验成功的概率为0.1，<equation>T = \sum_{i = 1}^{20}X_{i}</equation>可看作20次独立重复试验中试验成功的次数，服从<equation>B(20,0.1)</equation>.根据泊松定理，<equation>n = 20,p_{n} = 0.1,\lambda = 2,T</equation>近似服从参数为2的泊松分布.

因此，<equation>P \{T \leqslant 1 \} = P \{T = 0 \} + P \{T = 1 \} \approx \frac {2 ^ {0} \cdot \mathrm {e} ^ {- 2}}{1} + \frac {2 ^ {1} \cdot \mathrm {e} ^ {- 2}}{1} = \frac {3}{\mathrm {e} ^ {2}}.</equation>应选C.

---

**2024年第8题 | 选择题 | 5分 | 答案: B**
8. 设随机变量 X,Y相互独立，且 X服从正态分布 N(0,2),Y服从正态分布 N(-2,2).若<equation>P\{2 X+Y< a \}=P\{X>Y\}</equation>，则 a=（    )

A.<equation>- 2-\sqrt{1 0}</equation>B.<equation>- 2+\sqrt{1 0}</equation>C.<equation>- 2-\sqrt{6}</equation>D.<equation>- 2+\sqrt{6}</equation>
答案: B
**解析: **由于<equation>X\sim N(0,2),Y\sim N(-2,2)</equation>，故<equation>E(X) = 0,D(X) = 2,E(Y) = -2,D(Y) = 2</equation>，从而<equation>E (2 X + Y) = E (2 X) + E (Y) = 2 E (X) + E (Y) = - 2,</equation><equation>D (2 X + Y) = D (2 X) + D (Y) = 4 D (X) + D (Y) = 4 \times 2 + 2 = 1 0,</equation><equation>E (Y - X) = E (Y) - E (X) = - 2,</equation><equation>D (Y - X) = D (Y) + D (X) = 4.</equation>于是，<equation>2 X+Y\sim N(-2,1 0), Y-X\sim N(-2,4).</equation>将它们标准化可得<equation>\frac{2 X+Y+2}{\sqrt{1 0}}\sim N(0,1), \frac{Y-X+2}{2}</equation><equation>\sim N(0,1).</equation>由此可得，<equation>P \left\{2 X + Y < a \right\} = P \left\{2 X + Y \leqslant a \right\} = P \left\{\frac {2 X + Y + 2}{\sqrt {1 0}} \leqslant \frac {a + 2}{\sqrt {1 0}} \right\} = \Phi \left(\frac {a + 2}{\sqrt {1 0}}\right),</equation><equation>P \{X > Y \} = P \{Y - X < 0 \} = P \{Y - X \leqslant 0 \} = P \left\{\frac {Y - X + 2}{2} \leqslant 1 \right\} = \Phi (1),</equation>其中<equation>\varPhi(x)</equation>是标准正态分布<equation>N(0,1)</equation>的分布函数.

由<equation>P\{2X + Y < a\} = P\{X > Y\}</equation>可得<equation>\varPhi\left(\frac{a + 2}{\sqrt{10}}\right) = \varPhi(1).</equation>又因为<equation>\varPhi(x)</equation>单调增加，所以<equation>\frac{a + 2}{\sqrt{10}} = 1</equation>，即<equation>a = -2 + \sqrt{10}.</equation>因此，应选B.

---

**2024年第16题 | 填空题 | 5分**
16. 设随机试验每次成功的概率为 p，现进行3次独立重复试验，在至少成功1次的条件下，3次试验全部成功的概率为<equation>\frac{4}{1 3}</equation>，则 p=___
**答案: **#<equation>p = \frac{2}{3}</equation>
**解析: **解设 X为3次独立重复试验中试验成功的次数，则<equation>X\sim B(3,p).</equation>在至少成功1次的条件下， 3次试验全部成功的概率为<equation>P\{X=3\mid X\geqslant 1\}=\frac{P\{X=3,X\geqslant 1\}}{P\{X\geqslant 1\}}=\frac{P\{X=3\}}{P\{X\geqslant 1\}}=\frac{C_{3}^{3} p^{3}}{1-C_{3}^{0}(1-p)^{3}}=\frac{4}{13}.</equation>于是，<equation>\frac{p^{3}}{1-(1-p)^{3}}=\frac{4}{13}.</equation>整理可得<equation>3 p^{3}+4 p^{2}-4 p=0</equation>即 p（p+2）(3p-2）=0.由于 p>0，故 p<equation>=\frac{2}{3}.</equation>

---

**2023年第16题 | 填空题 | 5分**
16. 设随机变量与 Y相互独立， X且<equation>X\sim B\left(1,\frac{1}{3}\right),Y\sim B\left(2,\frac{1}{2}\right)</equation>则<equation>P\{X=Y\}=</equation>___
**解析: **解 由于<equation>X\sim B\left(1,\frac{1}{3}\right)</equation>，故<equation>P \left\{X = 0 \right\} = \mathrm {C} _ {1} ^ {0} \left(\frac {1}{3}\right) ^ {0} \left(\frac {2}{3}\right) ^ {1} = \frac {2}{3},</equation><equation>P \{X = 1 \} = C _ {1} ^ {1} \left(\frac {1}{3}\right) ^ {1} \left(\frac {2}{3}\right) ^ {0} = \frac {1}{3}.</equation>由于<equation>Y\sim B\left(2,\frac{1}{2}\right)</equation>，故<equation>P \left\{Y = 0 \right\} = \mathrm {C} _ {2} ^ {0} \left(\frac {1}{2}\right) ^ {0} \left(\frac {1}{2}\right) ^ {2} = \frac {1}{4},</equation><equation>P \left\{Y = 1 \right\} = \mathrm {C} _ {2} ^ {1} \left(\frac {1}{2}\right) ^ {1} \left(\frac {1}{2}\right) ^ {1} = \frac {1}{2}.</equation>因此，<equation>\begin{aligned} P \{X = Y \} &= P \{X = 0, Y = 0 \} + P \{X = 1, Y = 1 \} \\ \underline {{\text {独立性}}} P \{X = 0 \} P \{Y = 0 \} + P \{X = 1 \} P \{Y = 1 \} \\ &= \frac {2}{3} \times \frac {1}{4} + \frac {1}{3} \times \frac {1}{2} = \frac {1}{3}. \end{aligned}</equation>

---

**2019年第8题 | 选择题 | 4分 | 答案: A**
8. 设随机变量 X与 Y相互独立，且都服从正态分布<equation>N\left(\mu ,\sigma^{2}\right)</equation>，则<equation>P\{|X-Y|<1\}</equation>(    )

A. 与<equation>\mu</equation>无关，而与<equation>\sigma^{2}</equation>有关 B. 与<equation>\mu</equation>有关，而与<equation>\sigma^{2}</equation>无关

C. 与<equation>\mu,\sigma^{2}</equation>都有关 D. 与<equation>\mu,\sigma^{2}</equation>都无关
答案: A
**解析: **解 由于 X，Y相互独立且都服从正态分布<equation>N(\mu, \sigma^{2})</equation>，故<equation>E(X-Y)=0,D(X-Y)=2\sigma^{2},</equation><equation>X-Y\sim N(0,2\sigma^{2}).</equation>将 X-Y标准化，可得<equation>\frac{X-Y}{\sqrt{2}\sigma}\sim N(0,1).</equation>，于是，<equation>\begin{array}{l} P \left\{\mid X - Y \mid < 1 \right\} = P \left\{- 1 < X - Y < 1 \right\} = P \left\{\frac {- 1}{\sqrt {2} \sigma} < \frac {X - Y}{\sqrt {2} \sigma} < \frac {1}{\sqrt {2} \sigma} \right\} \\ = \Phi \left(\frac {1}{\sqrt {2} \sigma}\right) - \Phi \left(\frac {- 1}{\sqrt {2} \sigma}\right) = 2 \Phi \left(\frac {1}{\sqrt {2} \sigma}\right) - 1. \\ \end{array}</equation>因此，<equation>P\{|X - Y| < 1\}</equation>仅与<equation>\sigma^2</equation>有关.应选A.

---

**2018年第7题 | 选择题 | 4分 | 答案: A**
7. 设随机变量 X的概率密度 f(x)满足<equation>f(1+x)=f(1-x)</equation>，且<equation>\int_{0}^{2} f(x)\mathrm{d}x=0.6</equation>，则<equation>P\{ X<0\}=</equation>(    )

A. 0.2 B. 0.3 C. 0.4 D. 0.5
答案: A
**解析: **解（法一）由于<equation>f(1+x)=f(1-x)</equation>，故 f(x)的图像关于 x=1对称.于是，<equation>P\{X<0\}= P\{X>2\}.</equation>又因为<equation>P \{0 \leqslant X \leqslant 2 \} = \int_{0}^{2} f ( x ) \mathrm{d} x = 0. 6</equation>，且<equation>P \{X < 0 \} + P \{0 \leqslant X \leqslant 2 \} + P \{X > 2 \} = 1,</equation>所以<equation>P \{ X < 0 \} = \frac {1 - P \{0 \leqslant X \leqslant 2 \}}{2} = \frac {1 - 0 . 6}{2} = 0. 2.</equation>因此，应选A.

（法二）利用换元法.

由于<equation>\begin{aligned} \int_ {- \infty} ^ {0} f (x) \mathrm {d} x \xlongequal {u = 1 - x} \int_ {+ \infty} ^ {1} f (1 - u) \mathrm {d} (1 - u) &= \int_ {1} ^ {+ \infty} f (1 - u) \mathrm {d} u \\ \frac {f (1 + u) = f (1 - u)}{\mathrm {二}} \int_ {1} ^ {+ \infty} f (1 + u) \mathrm {d} u &= \int_ {2} ^ {+ \infty} f (t) \mathrm {d} t, \end{aligned}</equation>故<equation>P\{X < 0\} = P\{X > 2\}</equation>.

其余同法一.

---

**2017年第14题 | 填空题 | 4分**
14. 设随机变量 X的分布函数为<equation>F ( x )=0. 5 \Phi ( x )+0. 5 \Phi \left( \frac{x-4}{2} \right)</equation>，其中<equation>\Phi ( x )</equation>为标准正态分布函数，则<equation>E ( X )=</equation>
**答案: **```latex
2
```

**解析:**解记<equation>\varphi(x)</equation>为标准正态分布的概率密度函数，则<equation>\int_{-\infty}^{+\infty}\varphi(x)\mathrm{d}x=1,\int_{-\infty}^{+\infty}x\varphi(x)\mathrm{d}x=0.</equation>由题设知，X的概率密度为<equation>f(x)=F^{\prime}(x)=0. 5 \varphi(x)+0. 2 5 \varphi \left( \frac{x-4}{2} \right)</equation>，于是<equation>\begin{aligned} E (X) &= \int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \int_ {- \infty} ^ {+ \infty} \left[ 0. 5 x \varphi (x) + 0. 2 5 x \varphi \left(\frac {x - 4}{2}\right) \right] \mathrm {d} x \\ &= 0 + 0. 2 5 \int_ {- \infty} ^ {+ \infty} x \varphi \left(\frac {x - 4}{2}\right) \mathrm {d} x \xlongequal {t = \frac {x - 4}{2}} 0. 5 \int_ {- \infty} ^ {+ \infty} (2 t + 4) \varphi (t) \mathrm {d} t \\ &= \int_ {- \infty} ^ {+ \infty} t \varphi (t) \mathrm {d} t + 2 \int_ {- \infty} ^ {+ \infty} \varphi (t) \mathrm {d} t = 0 + 2 = 2. \end{aligned}</equation>

---

**2016年第7题 | 选择题 | 4分 | 答案: B**

7. 设随机变量<equation>X\sim N(\mu,\sigma^{2})(\sigma>0)</equation>，记<equation>p=P\{X\leqslant\mu+\sigma^{2}\}</equation>，则（    )

A. p随着<equation>\mu</equation>的增加而增加 B. p随着<equation>\sigma</equation>的增加而增加

C. p随着<equation>\mu</equation>的增加而减少 D. p随着<equation>\sigma</equation>的增加而减少

答案: B

**解析:**解（法一）令<equation>Y=\frac{X-\mu}{\sigma}</equation>，则由<equation>X\sim N(\mu ,\sigma^{2})</equation>知，<equation>Y\sim N(0,1).</equation>又<equation>p = P \left\{X \leqslant \mu + \sigma^ {2} \right\} = P \left\{\frac {X - \mu}{\sigma} \leqslant \sigma \right\} = P \left\{Y \leqslant \sigma \right\}</equation>故 p与<equation>\mu</equation>的取值无关，且p随着<equation>\sigma</equation>的增加而增加.应选B.

（法二）由于<equation>X\sim N(\mu ,\sigma^2)</equation>，故<equation>\begin{array}{l} p = P \left\{X \leqslant \mu + \sigma^ {2} \right\} = \int_ {- \infty} ^ {\mu + \sigma^ {2}} \frac {1}{\sqrt {2 \pi} \sigma} \mathrm {e} ^ {- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}} \mathrm {d} x \\ = \int_ {- \infty} ^ {\mu} \frac {1}{\sqrt {2 \pi} \sigma} \mathrm {e} ^ {- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}} \mathrm {d} x + \int_ {\mu} ^ {\mu + \sigma^ {2}} \frac {1}{\sqrt {2 \pi} \sigma} \mathrm {e} ^ {- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}} \mathrm {d} x \\ = \frac {1}{2} + \int_ {\mu} ^ {\mu + \sigma^ {2}} \frac {1}{\sqrt {2 \pi} \sigma} \mathrm {e} ^ {- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}} \mathrm {d} x \xlongequal {t = \frac {x - \mu}{\sigma}} \frac {1}{2} + \int_ {0} ^ {\sigma} \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {t ^ {2}}{2}} \mathrm {d} t, \\ \end{array}</equation>从而<equation>p</equation>与<equation>\mu</equation>的取值无关，且<equation>p</equation>随着<equation>\sigma</equation>的增加而增加.应选B.

---

**2013年第7题 | 选择题 | 4分 | 答案: A**

7. 设<equation>X_{1}, X_{2}, X_{3}</equation>是随机变量，且<equation>X_{1}\sim N(0,1), X_{2}\sim N\left(0,2^{2}\right), X_{3}\sim N\left(5,3^{2}\right), p_{i}=P\left\{-2\leqslant X_{i}\leqslant 2\right\} (i=1,2,3)</equation>则（    ）

A.<equation>p_{1}>p_{2}>p_{3}</equation>B.<equation>p_{2}>p_{1}>p_{3}</equation>C.<equation>p_{3}>p_{1}>p_{2}</equation>D.<equation>p_{1}>p_{3}>p_{2}</equation>

答案: A

**解析:**解 由<equation>X_{2} \sim N(0,2^{2}), X_{3} \sim N(5,3^{2})</equation>知，<equation>\frac{X_2}{2} \sim N(0,1), \frac{X_3 - 5}{3} \sim N(0,1)</equation>.于是，<equation>p_{1} = P\{-2 \leqslant X_{1} \leqslant 2\} = \Phi (2) - \Phi (-2) = 1 - \Phi (-2) - \Phi (-2) = 1 - 2\Phi (-2),</equation><equation>p_{2} = P\{-2 \leqslant X_{2} \leqslant 2\} = P\{-1 \leqslant \frac{X_{2}}{2} \leqslant 1\} = \Phi (1) - \Phi (-1) = 1 - 2\Phi (-1),</equation><equation>p_{3} = P\{-2 \leqslant X_{3} \leqslant 2\} = P\{- \frac{7}{3} \leqslant \frac{X_3 - 5}{3} \leqslant -1\} = \Phi (-1) - \Phi \left(-\frac{7}{3}\right).</equation>于<equation>\Phi (-1) > \Phi (-2)</equation>，故<equation>p_{1} > p_{2}</equation>.

由于<equation>\varPhi(-1) > \varPhi(-2)</equation>，故<equation>p_1 > p_2</equation>。

设标准正态分布的概率密度为<equation>\varphi(x)</equation>，则<equation>\varphi(x)</equation>为偶函数，且在<equation>(-\infty ,0]</equation>上单调增加（如图所示）.又由于<equation>p_{2}=\int_{-1}^{1}\varphi(x)\mathrm{d}x, p_{3}=</equation><equation>\int_{-\frac{7}{3}}^{-1}\varphi(x)\mathrm{d}x</equation>，而<equation>\varphi(x)</equation>在（-1,1）上的取值都大于<equation>\varphi(x)</equation>在<equation>\left(-\frac{7}{3},-1\right)</equation>上的取值，且积分区间的长度满足<equation>|1-(-1)|> \left| -1-\left(-\frac{7}{3}\right) \right|</equation>，故<equation>p_{2}>p_{3}.</equation>综上所述，<equation>p_{1}>p_{2}>p_{3}.</equation>应选A.

---

**2013年第14题 | 填空题 | 4分**

14. 设随机变量<equation>Y</equation>服从参数为 1 的指数分布,<equation>a</equation>为常数且大于零, 则<equation>P\{Y \leqslant a+1 \mid Y > a\} =</equation>___

**解析:**解 由题设知，Y的概率密度为<equation>f_{Y}(y)=\left\{\begin{array}{ll}\mathrm{e}^{-y},&y>0,\\ 0,&y\leqslant 0.\end{array}\right.</equation>又 a > 0，故<equation>P \left\{Y \leqslant a + 1 \mid Y > a \right\} = \frac {P \left\{a < Y \leqslant a + 1 \right\}}{P \left\{Y > a \right\}} = \frac {\int_ {a} ^ {a + 1} \mathrm {e} ^ {- y} \mathrm {d} y}{\int_ {a} ^ {+ \infty} \mathrm {e} ^ {- y} \mathrm {d} y} = \frac {\mathrm {e} ^ {- a} - \mathrm {e} ^ {- a - 1}}{\mathrm {e} ^ {- a}} = 1 - \frac {1}{\mathrm {e}}.</equation>

---

**2011年第7题 | 选择题 | 4分 | 答案: D**

7. 设<equation>F_{1}(x)</equation>与<equation>F_{2}(x)</equation>为两个分布函数，其相应的概率密度<equation>f_{1}(x)</equation>与<equation>f_{2}(x)</equation>是连续函数，则必为概率密度的是（    )

A.<equation>f_{1}(x)f_{2}(x)</equation>B.<equation>2f_{2}(x)F_{1}(x)</equation>C.<equation>f_{1}(x)F_{2}(x)</equation>D.<equation>f_{1}(x)F_{2}(x)+f_{2}(x)F_{1}(x)</equation>

答案: D

**解析:**解 由分布函数和概率密度的性质知，<equation>f_{1}(x)F_{2}(x) + f_{2}(x)F_{1}(x)\geqslant 0</equation>，且<equation>\begin{aligned} \int_ {- \infty} ^ {+ \infty} \left[ f _ {1} (x) F _ {2} (x) + f _ {2} (x) F _ {1} (x) \right] \mathrm {d} x &= \int_ {- \infty} ^ {+ \infty} \left[ F _ {1} (x) F _ {2} (x) \right] ^ {\prime} \mathrm {d} x \\ &= F _ {1} (+ \infty) F _ {2} (+ \infty) - F _ {1} (- \infty) F _ {2} (- \infty) \\ &= 1 - 0 = 1. \end{aligned}</equation>因此，<equation>f_{1}(x)F_{2}(x) + f_{2}(x)F_{1}(x)</equation>为概率密度.应选D.

---

**2010年第7题 | 选择题 | 4分 | 答案: C**

7. 设随机变量 X的分布函数 F(x) =<equation>\left\{\begin{array}{l l}0,&x<0,\\ \frac{1}{2},&0\leqslant x<1,\\ 1-\mathrm{e}^{-x},&x\geqslant 1,\end{array} \right.</equation>则 P{X=1} =（    )

A. 0 B.<equation>\frac{1}{2}</equation>C.<equation>\frac{1}{2}-\mathrm{e}^{-1}</equation><equation>1 - \mathrm {e} ^ {- 1}</equation>

答案: C

**解析:**解<equation>P \{ X = 1 \} = P \{ X \leqslant 1 \} - P \{ X < 1 \} = F ( 1 ) - F ( 1^{-} ) = 1 - \frac{1} {\mathrm{e}} - \frac{1}{2} = \frac{1}{2} - \frac{1} {\mathrm{e}}</equation>，故选C.

---

**2010年第8题 | 选择题 | 4分 | 答案: A**

8. 设<equation>f_{1}(x)</equation>为标准正态分布的概率密度，<equation>f_{2}(x)</equation>为<equation>[-1,3]</equation>上均匀分布的概率密度，若<equation>f (x) = \left\{ \begin{array}{l l} a f _ {1} (x), & x \leqslant 0, \\ b f _ {2} (x), & x > 0 \end{array} \right. \quad (a > 0, b > 0)</equation>为概率密度，则 a,b应满足（    ）

A. 2a+3b=4 B. 3a+2b=4 C. a+b=1 D. a+b=2

答案: A

**解析:**解 由于标准正态分布的概率密度的图形关于 x=0对称，故<equation>\int_{0}^{+\infty} f_{1}(x)\mathrm{d}x=\int_{-\infty}^{0} f_{1}(x)\mathrm{d}x=\frac{1}{2}.</equation>又由题设知，<equation>f_{2}(x)=\left\{\begin{array}{ll}\frac{1}{4},&-1\leqslant x\leqslant 3,\\ 0,&\text{其他}.\end{array} \right.</equation>由于 f(x)为概率密度，故<equation>1=\int_{-\infty}^{+\infty} f(x)\mathrm{d}x=\int_{-\infty}^{0} a f_{1}(x)\mathrm{d}x+\int_{0}^{+\infty} b f_{2}(x)\mathrm{d}x=\frac{1}{2} a+\int_{0}^{3} \frac{b}{4}\mathrm{d}x=\frac{1}{2} a+\frac{3}{4} b,</equation>即<equation>\frac{1}{2} a+\frac{3}{4} b=1</equation>从而2a+3b=4.应选A.

---


### 参数估计与假设检验


