# 数学三

## 概率论与数理统计

### 多维随机变量及其分布

#### 边缘分布与条件分布

**2025年第22题 | 解答题 | 12分**

22. 投保人的损失事件发生时，保险公司的赔付额 Y与投保人的损失额 X的关系为<equation>Y=\left\{\begin{array}{ll}0,&X\leqslant 100\\ X-100,&X>100\end{array} \right.</equation>. 设定损事件发生时，投保人的损失额 X的概率密度为<equation>f(x)=\left\{\begin{array}{ll}\frac{2\times 100^{2}}{(100+x)^{3}},&x>0\\ 0,&x\leqslant 0\end{array} \right.</equation>I. 求<equation>P\{Y>0\}</equation>及 EY.

Ⅱ. 这种损失事件在一年内发生的次数记为 N，保险公司在一年内就这种损失事件产生的理赔次数记为 M，假设 N服从参数为8的泊松分布，在<equation>N=n</equation>（<equation>n\geqslant1</equation>）的条件下，M服从二项分布<equation>B(n,p)</equation>，其中<equation>p=P\{Y>0\}</equation>，求 M的概率分布.

**答案:**（I）<equation>P \left\{Y > 0\right\}=\frac{1}{4}, E (Y)=50;</equation>（Ⅱ）M服从参数为2的泊松分布.

**解析:**解（I）根据 Y的定义，<equation>\begin{aligned} P \{Y > 0 \} &= P \{X > 1 0 0 \} = \int_ {1 0 0} ^ {+ \infty} f (x) \mathrm {d} x = \int_ {1 0 0} ^ {+ \infty} \frac {2 \times 1 0 0 ^ {2}}{(1 0 0 + x) ^ {3}} \mathrm {d} x = - \frac {2 \times 1 0 0 ^ {2}}{2} (1 0 0 + x) ^ {- 2} \Bigg | _ {1 0 0} ^ {+ \infty} \\ &= - \frac {1 0 0 ^ {2}}{(1 0 0 + x) ^ {2}} \Bigg | _ {1 0 0} ^ {+ \infty} = \frac {1}{4}. \end{aligned}</equation>由于随机变量<equation>Y</equation>是随机变量<equation>X</equation>的函数，故根据数学期望的定义，<equation>\begin{aligned} E (Y) &= 0 \cdot P \{Y = 0 \} + \int_ {1 0 0} ^ {+ \infty} (x - 1 0 0) f (x) \mathrm {d} x = \int_ {1 0 0} ^ {+ \infty} \frac {2 \times 1 0 0 ^ {2} (x - 1 0 0)}{\left(1 0 0 + x\right) ^ {3}} \mathrm {d} x \\ &= - 1 0 0 ^ {2} \int_ {1 0 0} ^ {+ \infty} (x - 1 0 0) \mathrm {d} \left[ (1 0 0 + x) ^ {- 2} \right] = - 1 0 0 ^ {2} \left[ \frac {x - 1 0 0}{(1 0 0 + x) ^ {2}} \right| _ {1 0 0} ^ {+ \infty} - \int_ {1 0 0} ^ {+ \infty} \frac {\mathrm {d} x}{(1 0 0 + x) ^ {2}} ] \\ &= \frac {- 1 0 0 ^ {2}}{1 0 0 + x} \Bigg | _ {1 0 0} ^ {+ \infty} = 0 - \left(- \frac {1 0 0 ^ {2}}{2 0 0}\right) = 5 0. \end{aligned}</equation>（Ⅱ）由于<equation>N</equation>服从参数为8的泊松分布，故<equation>P\{N = n\} = \frac{8^n\mathrm{e}^{-8}}{n!}</equation>，进一步可得<equation>P\{N = 0\} = \mathrm{e}^{-8}</equation>由于当<equation>N = 0</equation>时，<equation>M</equation>必然等于0，故<equation>P\{M = 0\mid N = 0\} = 1</equation>，从而<equation>P \{M = 0, N = 0 \} = P \{M = 0 \mid N = 0 \} P \{N = 0 \} = 1 \cdot P \{N = 0 \} = \mathrm {e} ^ {- 8}.</equation>由 M的定义可知，当<equation>M=k</equation>时，<equation>N=n\geqslant k</equation>由在<equation>N=n(n\geqslant 1)</equation>的条件下，M服从二项分布 B(n,p）可得，<equation>P \left\{M = k \mid N = n \right\} = \mathrm {C} _ {n} ^ {k} p ^ {k} (1 - p) ^ {n - k}, \quad k = 0, 1, \dots , n, n = 1, 2, \dots .</equation>由条件概率公式以及<equation>p=\frac{1}{4}</equation>可得<equation>\begin{aligned} P \{M = k, N = n \} &= P \{M = k \mid N = n \} P \{N = n \} = C _ {n} ^ {k} p ^ {k} (1 - p) ^ {n - k} \frac {8 ^ {n} \mathrm {e} ^ {- 8}}{n !} \\ &= \frac {n !}{k ! (n - k) !} \cdot \left(\frac {1}{4}\right) ^ {k} \cdot \left(\frac {3}{4}\right) ^ {n - k} \cdot \frac {8 ^ {n} \mathrm {e} ^ {- 8}}{n !} = \frac {3 ^ {n - k} 2 ^ {n} \mathrm {e} ^ {- 8}}{k ! (n - k) !} \\ &= \frac {6 ^ {n - k} 2 ^ {k} \mathrm {e} ^ {- 8}}{k ! (n - k) !}. \end{aligned}</equation>由此可得，当<equation>k\neq 0</equation>时，<equation>\begin{aligned} P \{M = k \} &= \sum_ {n = k} ^ {\infty} P \{M = k, N = n \} = \sum_ {n = k} ^ {\infty} \frac {6 ^ {n - k} 2 ^ {k} \mathrm {e} ^ {- 8}}{k ! (n - k) !} = \frac {2 ^ {k} \mathrm {e} ^ {- 2}}{k !} \sum_ {n = k} ^ {\infty} \frac {6 ^ {n - k} \mathrm {e} ^ {- 6}}{(n - k) !} \\ &= \frac {2 ^ {k} \mathrm {e} ^ {- 2}}{k !} \sum_ {n = 0} ^ {\infty} \frac {6 ^ {n} \mathrm {e} ^ {- 6}}{n !}. \end{aligned}</equation><equation>\begin{aligned} P \{M = 0 \} &= \sum_ {n = 0} ^ {\infty} P \{M = 0, N = n \} = \mathrm {e} ^ {- 8} + \sum_ {n = 1} ^ {\infty} P \{M = 0, N = n \} = \mathrm {e} ^ {- 8} + \sum_ {n = 1} ^ {\infty} \frac {6 ^ {n} \mathrm {e} ^ {- 6}}{n !} \cdot \mathrm {e} ^ {- 2} \\ &= \mathrm {e} ^ {- 2} \sum_ {n = 0} ^ {\infty} \frac {6 ^ {n} \mathrm {e} ^ {- 6}}{n !}. \end{aligned}</equation>由泊松分布的定义可知，服从参数为6的泊松分布的随机变量Z的分布律为<equation>P\{Z = n\} = \frac{6^{n}\mathrm{e}^{-6}}{n!}</equation>.由分布律的性质可得，<equation>\sum_{n = 0}^{\infty}\frac{6^{n}\mathrm{e}^{-6}}{n!} = 1.</equation>于是，<equation>P\{M = k\} = \frac{2^{k}\mathrm{e}^{-2}}{k!},k = 0,1,2,\dots .</equation>因此，M服从参数为2的泊松分布

---

**2013年第22题 | 解答题 | 11分**


设 (X,Y)是二维随机变量，X的边缘概率密度为<equation>f_{X}(x)=\left\{ \begin{array}{ll} 3x^{2}, & 0<x<1, \\ 0, & \text{其他.} \end{array} \right.</equation>在给定 X=x(0<x<1)的条件下 Y的条件概率密度为<equation>f_{Y|X}(y\mid x)=\left\{ \begin{array}{ll} \frac{3y^{2}}{x^{3}}, & 0<y<x, \\ 0, & \text{其他.} \end{array} \right.</equation>I. 求 (X,Y)的概率密度 f(x,y);

II. 求 Y的边缘概率密度<equation>f_{Y}(y)</equation>III. 求<equation>P\{X>2Y\}</equation>

**答案:**(22) (I)<equation>f ( x,y)=\left\{\begin{array}{ll}\frac{9 y^{2}}{x},&0<y<x,0<x<1,\\ 0,&\text{其他};\end{array} \right.</equation>(Ⅱ)<equation>f_{Y}(y)=\left\{\begin{array}{ll}-9 y^{2}\ln y,&0<y<1,\\ 0,&\text{其他};\end{array} \right.</equation>(Ⅲ)<equation>\frac{1}{8}.</equation>

**解析:**解（I）当<equation>0 < x < 1</equation>时，<equation>f_{X}(x)=3x^{2},f_{Y\mid X}(y\mid x)=\frac{f(x,y)}{f_{X}(x)}=\left\{ \begin{array}{ll}\frac{3y^{2}}{x^{3}},&0<y<x,\\ 0,&\text{其他}, \end{array} \right.</equation>故当<equation>0 < x < 1</equation>时，<equation>f (x, y) = \left\{ \begin{array}{l l} \frac {9 y ^ {2}}{x}, & 0 < y < x, \\ 0, & y \leqslant 0 \text {或} y \geqslant x. \end{array} \right.</equation>下面求当<equation>x \leqslant 0</equation>或<equation>x \geqslant 1</equation>时<equation>f(x,y)</equation>的取值.

由于<equation>\int_ {0} ^ {1} \mathrm {d} x \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {x} \frac {9 y ^ {2}}{x} \mathrm {d} y = \int_ {0} ^ {1} 3 x ^ {2} \mathrm {d} x = 1,</equation>故可以认为在<equation>\left\{(x,y)\mid 0 < x < 1,-\infty < y < +\infty\right\}</equation>以外的平面上，即<equation>x\leqslant 0</equation>或<equation>x\geqslant 1</equation>时，<equation>f(x,y)=0.</equation>综上所述，<equation>(X,Y)</equation>的概率密度<equation>f(x,y) = \left\{ \begin{array}{ll}\frac{9y^2}{x}, & 0 < y < x,0 < x < 1,\\ 0, & \text{其他}. \end{array} \right.</equation>（Ⅱ）由第（I）问知<equation>Y</equation>的边缘概率密度为<equation>f _ {Y} (y) = \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} x = \left\{ \begin{array}{l l} \int_ {y} ^ {1} \frac {9 y ^ {2}}{x} \mathrm {d} x, & 0 < y < 1, \\ 0, & \text {其 他} \end{array} = \left\{ \begin{array}{l l} - 9 y ^ {2} \ln y, & 0 < y < 1, \\ 0, & \text {其 他}. \end{array} \right. \right.</equation>或者，将上述积分次序改为先对<equation>x</equation>积分，再对<equation>y</equation>积分，可得<equation>\begin{array}{l} P \left\{X > 2 Y \right\} = \iint_ {| (x, y) | x > 2 y |} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {\frac {1}{2}} \mathrm {d} y \int_ {2 y} ^ {1} \frac {9 y ^ {2}}{x} \mathrm {d} x = \int_ {0} ^ {\frac {1}{2}} \left(- 9 y ^ {2} \ln 2 y\right) \mathrm {d} y \\ = - 3 y ^ {3} \ln 2 y \left| _ {0} ^ {\frac {1}{2}} + \int_ {0} ^ {\frac {1}{2}} \frac {6 y ^ {3}}{2 y} \mathrm {d} y = \int_ {0} ^ {\frac {1}{2}} 3 y ^ {2} \mathrm {d} y = \frac {1}{8}. \right. \\ \end{array}</equation>

---


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
### 大数定律和中心极限定理
### 参数估计
# 张宇数学公式手册
## 第一部分 高等数学
### 第三章 一元函数积分学
### 第七章 级 数
## 第二部分 线性代数
### 第二章 矩 阵 91
## 第三部分 概率论与数理统计
### 第一章 随机事件和概率
### 第四章 随机变量的数字特征
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

<equation>\textcircled{2}</equation>若<equation>\lim \frac{\alpha(x)}{\beta(x)} = 1</equation>，则称<equation>\alpha(x)</equation>与<equation>\beta(x)</equation>为等价无穷小量，记作<equation>\alpha(x)\sim \beta(x)</equation>；

---


#### 7. 无穷大量的定义

<equation>\textcircled{3}</equation>若<equation>\lim\frac{\alpha (x)}{\beta (x)}=0</equation>，则称<equation>\alpha (x)</equation>是比<equation>\beta (x)</equation>高阶的无穷小量，记作<equation>\alpha (x)=o(\beta (x))</equation>；

<equation>\textcircled{4}</equation>若<equation>\lim\frac{\alpha (x)}{\beta (x)}=\infty</equation>，则称<equation>\alpha (x)</equation>是比<equation>\beta (x)</equation>低阶的无穷小量.


设<equation>\alpha (x),\beta (x),\tilde{\alpha}(x),\tilde{\beta}(x)</equation>都是同一自变量变化过程中的无穷小量，且<equation>\alpha (x)\sim \tilde{\alpha}(x),\beta (x)\sim \tilde{\beta}(x)</equation>，则

<equation>\begin{array}{l} \lim \frac {\alpha (x) f (x)}{\beta (x) g (x)} = \lim \frac {\tilde {\alpha} (x) f (x)}{\beta (x) g (x)} = \lim \frac {\alpha (x) f (x)}{\tilde {\beta} (x) g (x)} \\ = \lim \frac {\tilde {\alpha} (x) f (x)}{\tilde {\beta} (x) g (x)}. \\ \end{array}</equation>


设<equation>\alpha ,\beta</equation>都是同一自变量变化过程中的无穷小量，若存在<equation>k > 0</equation>，使得<equation>\lim \frac{\alpha}{\beta^k} = C(C</equation>为非零的常数），则称在同一自变量变化过程中<equation>\alpha</equation>是<equation>\beta</equation>的<equation>k</equation>阶无穷小量.


任给<equation>M > 0</equation>，存在正数<equation>\delta</equation>，当<equation>0 < |x - x_0| < \delta</equation>时，恒有<equation>|f(x)| > M</equation>，则称<equation>x\to x_0</equation>时<equation>f(x)</equation>是无穷大量，记为<equation>\lim_{x\to x_0} f(x) = \infty</equation>.

---


#### (2)左、右连续的定义

在自变量的同一变化过程中，如果<equation>f(x)</equation>为无穷大量，则<equation>\frac{1}{f(x)}</equation>为无穷小量；反之，如果<equation>f(x)</equation>为无穷小量，且<equation>f(x)\neq 0</equation>，则<equation>\frac{1}{f(x)}</equation>为无穷大量.


(1) 连续的定义

<equation>\textcircled{1}</equation>设函数<equation>f(x)</equation>在点<equation>x_{0}</equation>的某个邻域内有定义，若

<equation>\lim _ {\Delta x \rightarrow 0} \Delta y = \lim _ {\Delta x \rightarrow 0} \left[ f \left(x _ {0} + \Delta x\right) - f \left(x _ {0}\right)\right] = 0,</equation>

则称<equation>f(x)</equation>在点<equation>x_{0}</equation>处连续.

<equation>\textcircled{2}</equation>设函数<equation>f(x)</equation>在点<equation>x_{0}</equation>的某个邻域内有定义，若

<equation>\lim _ {x \rightarrow x _ {0}} f (x) = f \left(x _ {0}\right),</equation>

则称<equation>f ( x )</equation>在点<equation>x_{0}</equation>处连续.


设<equation>f ( x )</equation>在点<equation>x_{0}</equation>的左侧（或右侧）某邻域（包括点<equation>x_{0}</equation>）有定义，并且

<equation>\lim _ {x \rightarrow x _ {0}} f (x) = f \left(x _ {0}\right),</equation>

则称<equation>f ( x )</equation>在点<equation>x_{0}</equation>处左连续（或右连续）.

函数<equation>f(x)</equation>在点<equation>x_{0}</equation>处连续的充要条件是<equation>f(x)</equation>在点

---


#### (2) 间断点的分类

<equation>x_{0}</equation>处既左连续又右连续


若函数<equation>f(x), g(x)</equation>在点<equation>x_0</equation>处连续，则<equation>f(x)\pm g(x), f(x)\cdot g(x), \frac{f(x)}{g(x)} (g(x_0)\neq 0)</equation>在点<equation>x_0</equation>处也连续.


若函数<equation>u = \varphi (x)</equation>在点<equation>x_0</equation>处连续，函数<equation>y = f(u)</equation>在点<equation>u_0 = \varphi (x_0)</equation>处连续，则函数<equation>y = f[\varphi (x)]</equation>在点<equation>x_0</equation>处连续.


设函数<equation>y = f(x)</equation>在区间<equation>(a,b)</equation>内为单调的连续函数，其值域为<equation>(m,n)</equation>，则其反函数<equation>x = f^{-1}(y)</equation>在区间<equation>(m,n)</equation>内也是连续的.

一切初等函数在其定义区间内都是连续的.


若函数<equation>f(x)</equation>在点<equation>x_{0}</equation>的任何邻域内总有异于<equation>x_{0}</equation>而属于函数<equation>f(x)</equation>定义域内的点，且函数<equation>f(x)</equation>在点<equation>x_{0}</equation>处不连续，则称<equation>x_{0}</equation>是<equation>f(x)</equation>的一个间断点.


左、右极限都存在的间断点称为第一类间断点.其

---


#### (3)零点定理

中，左、右极限都存在且相等的间断点称为可去间断点；左、右极限都存在且不相等的间断点称为跳跃间断点.

左、右极限至少有一个不存在的间断点称为第二类间断点. 若<equation>x\to x_0^{-}</equation>或<equation>x\to x_0^{+}</equation>时，<equation>f(x)\rightarrow \infty</equation>，则称<equation>x_0</equation>为<equation>f(x)</equation>的无穷间断点.


如果函数<equation>f(x)</equation>在闭区间<equation>[a,b]</equation>上连续，则在该区间上至少存在两点<equation>x_{1}, x_{2}</equation>，使得对于任意的<equation>x \in [a,b]</equation>，恒有<equation>f(x_{1}) \leqslant f(x) \leqslant f(x_{2})</equation>。


如果函数<equation>f(x)</equation>在闭区间<equation>[a,b]</equation>上连续，<equation>m,M</equation>是<equation>f(x)</equation>在该区间上的最小值与最大值，则对任意的<equation>\mu \in [m,M]</equation>在<equation>[a,b]</equation>上至少存在一点<equation>\xi</equation>，满足<equation>f(\xi) = \mu</equation>


如果<equation>f(x)</equation>在闭区间<equation>[a,b]</equation>上连续，且满足<equation>f(a)\cdot f(b) < 0</equation>，则在开区间（a,b）内至少存在一点<equation>\xi</equation>，使得<equation>f(\xi) = 0.</equation>

---


### 第二章 一元函数微分学
#### 一、导数与微分

1. 导数的定义式

<equation>\begin{array}{l} f ^ {\prime} \left(x _ {0}\right) = \frac {\mathrm {d} y}{\mathrm {d} x} \Bigg | _ {x = x _ {0}} = \lim _ {\Delta x \rightarrow 0} \frac {f \left(x _ {0} + \Delta x\right) - f \left(x _ {0}\right)}{\Delta x} \\ = \lim _ {x \rightarrow x _ {0}} \frac {f (x) - f \left(x _ {0}\right)}{x - x _ {0}}. \\ \end{array}</equation>

2. 微分的定义式

若<equation>\Delta y = A\Delta x + o(\Delta x)</equation>，则<equation>\mathrm{d}y = A\Delta x.</equation>

3. 可微的充要条件

可导<equation>\Leftrightarrow</equation>可微，<equation>\mathrm{d}y = f^{\prime}(x)\mathrm{d}x.</equation>

4. 可导与连续的关系

<equation>f(x)</equation>在<equation>x_{0}</equation>点可导<equation>\Rightarrow f(x)</equation>在<equation>x_{0}</equation>点处连续.

5. 可导、可微、连续等的关系

可微<equation>\Leftrightarrow</equation>可导<equation>\Rightarrow</equation>函数连续<equation>\Rightarrow \lim_{x\to x_0} f(x)</equation>存在<equation>\Rightarrow f(x)</equation>在<equation>x_0</equation>点的某邻域内有界.

---


#### 1. 基本初等函数的导数公式

<equation>\textcircled{1}</equation><equation>( C )^{\prime}=0</equation>（C为常数）；

<equation>\textcircled{2}</equation><equation>( x^{a} )^{\prime}=\alpha x^{a-1}</equation>（<equation>\alpha</equation>为实数）；

<equation>\textcircled{3}</equation><equation>( a^{x} )^{\prime}=a^{x} \ln a</equation><equation>( a>0,a\neq1)</equation>

<equation>\textcircled{4} \left( \mathrm{e}^{x} \right)^{\prime}=\mathrm{e}^{x};</equation>

<equation>\textcircled{5}</equation><equation>(\log_{a} x)^{\prime} = \frac{1}{x \ln a}</equation>（<equation>a > 0,a\neq 1</equation>）；

<equation>\textcircled{6}</equation><equation>(\ln x)^{\prime}=\frac{1}{x};</equation>

<equation>\textcircled{7}</equation><equation>(\sin x)^{\prime}=\cos x;</equation>

<equation>\textcircled{8}</equation><equation>(\cos x)^{\prime}=-\sin x;</equation>

<equation>\textcircled{9}</equation><equation>(\tan x)^{\prime}=\frac{1}{\cos^{2} x}</equation>;

<equation>\textcircled{1 0} \left( \cot x \right)^{\prime}=-\frac{1}{\sin^{2} x};</equation>

<equation>\textcircled{11}</equation><equation>(\sec x)^{\prime}=\sec x\tan x;</equation>

<equation>\textcircled{12} (\csc x)^{\prime} = -\csc x\cot x;</equation>

<equation>\textcircled{1 3}</equation><equation>\operatorname{a r c s i n} x )^{\prime}=\frac{1}{\sqrt{1-x^{2}}}</equation>

<equation>\textcircled{14} (\arccos x)^{\prime} = -\frac{1}{\sqrt{1-x^{2}}}</equation>;

---


#### 5. 隐函数的导数

<equation>\textcircled{15}</equation><equation>(\arctan x)^{\prime}=\frac{1}{1+x^{2}}</equation>

<equation>\textcircled{16} (\operatorname{arccot} x)^{\prime}=-\frac{1}{1+x^{2}}.</equation>


设 u(x), v(x)都可导，则

<equation>\textcircled{1}</equation><equation>( u \pm v )^{\prime}=u^{\prime} \pm v^{\prime}</equation>

<equation>\textcircled{2}</equation><equation>(uv)^{\prime} = u^{\prime}v + uv^{\prime}</equation>，特别地，有<equation>(cu)^{\prime} = cu^{\prime}</equation>（<equation>c</equation>为常数）；

<equation>\textcircled{3} \left( \frac{u}{v} \right)^{\prime}=\frac{u^{\prime} v-u v^{\prime}}{v^{2}} \quad(v \neq 0).</equation>


设<equation>u = \varphi (x)</equation>在<equation>x</equation>处可导，<equation>y = f(u)</equation>在对应的<equation>u = \varphi (x)</equation>处可导，则复合函数<equation>y = f[\varphi (x)]</equation>在<equation>x</equation>处可导，且

<equation>\{f[\varphi(x)]\}' = f'(u)\varphi'(x)</equation>，即<equation>\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\mathrm{d}y}{\mathrm{d}u} \cdot \frac{\mathrm{d}u}{\mathrm{d}x}</equation>.


若<equation>x = \varphi (y)</equation>在某区间内单调、可导，且<equation>\varphi^{\prime}(y)\neq 0</equation>，则其反函数<equation>y = f(x)</equation>在对应的区间内也可导，且<equation>f^{\prime}(x) = \frac{1}{\varphi^{\prime}(y)}</equation>


设<equation>y = y(x)</equation>是由方程<equation>F(x,y) = 0</equation>确定的可导函数，方程两端同时对<equation>x</equation>求导，遇到<equation>y</equation>的函数则视为复合

---


#### （2）高阶导数的运算法则

函数，y为中间变量，可得到一个含<equation>y^{\prime}</equation>的方程，从中解出<equation>y^{\prime}</equation>即可.


如果<equation>y^{\prime} = f^{\prime}(x)</equation>作为<equation>x</equation>的函数在点<equation>x</equation>可导，则<equation>y^{\prime}</equation>的导数称为<equation>y = f(x)</equation>的二阶导数，记为<equation>y^{\prime \prime}</equation>，或<equation>f^{\prime \prime}(x)</equation>，或<equation>\frac{\mathrm{d}^2y}{\mathrm{d}x^2}</equation>.

一般地，函数<equation>y = f(x)</equation>的<equation>n</equation>阶导数为<equation>y^{(n)} = [y^{(n - 1)}]'</equation>，也可写作<equation>f^{(n)}(x)</equation>或<equation>\frac{\mathrm{d}^n y}{\mathrm{d}x^n}</equation>.


设<equation>u=u ( x )</equation><equation>v=v ( x ) n</equation>阶可导，则

<equation>\textcircled{1}</equation><equation>(u \pm v)^{(n)} = u^{(n)} \pm v^{(n)}</equation>;

<equation>\textcircled{2}</equation><equation>( C u ) ^{ ( n )}=C u ^{ ( n )}</equation>（C为常数）；

<equation>\textcircled{3} ( u v )^{ ( n )}=\mathrm{C}_{n}^{0} u^{ ( n )} v+\mathrm{C}_{n}^{1} u^{ ( n-1 )} v^{\prime}+\dots+\mathrm{C}_{n}^{n-1} u^{\prime} v^{ ( n-1 )}+\mathrm{C}_{n}^{n} u v^{ ( n )}</equation>（莱布尼茨公式）.

(3) 几个常见初等函数的<equation>n</equation>阶导数公式

<equation>\textcircled{1}</equation><equation>(a^{x})^{(n)} = a^{x} \cdot \ln^{n} a</equation>;

---


#### 2. 拉格朗日中值定理

<equation>\textcircled{4} \left( \frac{1}{a x+b} \right)^{(n)}=\frac{(-1)^{n} a^{n} n!}{(a x+b)^{n+1}};</equation>


设<equation>y = y(x)</equation>是由参数方程<equation>\left\{ \begin{array}{l} x = \varphi (t), \\ y = \psi (t) \end{array} \right.</equation>（<equation>\alpha < t < \beta</equation>）确定的函数. 则

<equation>\textcircled{1}</equation>若<equation>\varphi (t),\psi (t)</equation>都可导，且<equation>\varphi^{\prime}(t)\neq 0</equation>，则

<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\psi^ {\prime} (t)}{\varphi^ {\prime} (t)}.</equation>

<equation>\textcircled{2}</equation>若<equation>\varphi(t),\psi(t)</equation>二阶可导，且<equation>\varphi^{\prime}(t)\neq 0</equation>，则

<equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\psi^ {\prime \prime} (t) \varphi^ {\prime} (t) - \psi^ {\prime} (t) \varphi^ {\prime \prime} (t)}{\left[ \varphi^ {\prime} (t) \right] ^ {3}}.</equation>


设 f(x)在闭区间<equation>[a,b]</equation>上连续，在开区间（a,b）内可导，若<equation>f(a) = f(b)</equation>，则至少存在一点<equation>\xi\in( a,b)</equation>，使得

<equation>f ^ {\prime} (\xi) = 0.</equation>


设 f(x)在闭区间<equation>[a,b]</equation>上连续，在开区间（a,b）内可导，则至少存在一点<equation>\xi\in(a,b)</equation>，使得

---


#### (2) 带皮亚诺余项的泰勒定理

<equation>f (b) - f (a) = f ^ {\prime} (\xi) (b - a).</equation>


设<equation>f(x),g(x)</equation>在闭区间<equation>[a,b]</equation>上连续，在开区间<equation>(a,b)</equation>内可导，且<equation>g^{\prime}(x)\neq 0,x\in(a,b)</equation>，则至少存在一点<equation>\xi \in (a,b)</equation>，使得

<equation>\frac {f (b) - f (a)}{g (b) - g (a)} = \frac {f ^ {\prime} (\xi)}{g ^ {\prime} (\xi)}.</equation>


设<equation>f(x)</equation>在点<equation>x_{0}</equation>的某一邻域内有直到<equation>n + 1</equation>阶的导数，则对该邻域内的任意点<equation>x</equation>，都有

<equation>\begin{array}{l} f (x) = f \left(x _ {0}\right) + \frac {f ^ {\prime} \left(x _ {0}\right)}{1 !} \left(x - x _ {0}\right) + \frac {f ^ {\prime \prime} \left(x _ {0}\right)}{2 !} \left(x - x _ {0}\right) ^ {2} + \dots + \\ \frac {f ^ {(n)} \left(x _ {0}\right)}{n !} \left(x - x _ {0}\right) ^ {n} + \frac {f ^ {(n + 1)} (\xi)}{(n + 1) !} \left(x - x _ {0}\right) ^ {n + 1}, \\ \end{array}</equation>

其中<equation>\xi</equation>介于 x，<equation>x_{0}</equation>之间.


设<equation>f(x)</equation>在点<equation>x_{0}</equation>的某一邻域内有直到<equation>n</equation>阶的导数，则对该邻域内的任意点<equation>x</equation>，都有

<equation>\begin{array}{l} f (x) = f \left(x _ {0}\right) + \frac {f ^ {\prime} \left(x _ {0}\right)}{1 !} \left(x - x _ {0}\right) + \frac {f ^ {\prime \prime} \left(x _ {0}\right)}{2 !} \left(x - x _ {0}\right) ^ {2} + \dots + \\ \frac {f ^ {(n)} \left(x _ {0}\right)}{n !} \left(x - x _ {0}\right) ^ {n} + o \left(x - x _ {0}\right) ^ {n}. \\ \end{array}</equation>

---


#### 四、洛必达法则

(3) 几个常用函数的带皮亚诺余项的麦克劳林展开式

<equation>\mathrm {e} ^ {x} = 1 + x + \frac {x ^ {2}}{2 !} + \dots + \frac {x ^ {n}}{n !} + o \left(x ^ {n}\right).</equation>

<equation>\sin x = x - \frac {1}{3 !} x ^ {3} + \dots + \frac {(- 1) ^ {n}}{(2 n + 1) !} x ^ {2 n + 1} + o \left(x ^ {2 n + 1}\right),</equation>

<equation>\cos x = 1 - \frac {x ^ {2}}{2 !} + \dots + (- 1) ^ {n} \frac {x ^ {2 n}}{(2 n) !} + o \left(x ^ {2 n}\right),</equation>

<equation>\ln (1 + x) = x - \frac {x ^ {2}}{2} + \frac {x ^ {3}}{3} - \dots + (- 1) ^ {n - 1} \frac {x ^ {n}}{n} + o \left(x ^ {n}\right),</equation>

<equation>\begin{array}{l} (1 + x) ^ {m} = 1 + m x + \frac {m (m - 1)}{2 !} x ^ {2} + \dots + \\ \frac {m (m - 1) \cdots (m - n + 1)}{n !} x ^ {n} + o \left(x ^ {n}\right). \\ \end{array}</equation>


1. 求“<equation>\frac{0}{0}</equation>”型未定式极限的洛必达法则设<equation>\textcircled{1}\lim_{x\to x_0}f(x) = 0,\lim_{x\to x_0}g(x) = 0</equation>；

<equation>\textcircled{2} f ( x ) , g ( x )</equation>在<equation>x_{0}</equation>的某去心邻域内可导，且<equation>g^{\prime}(x)\neq0;</equation>

<equation>\textcircled{3}</equation><equation>\lim_{x\to x_1}\frac{f'(x)}{g'(x)} = A</equation>或为<equation>\infty</equation>

---


#### (1)定义

则<equation>\lim_{x\to x_0}\frac{f(x)}{g(x)} = \lim_{x\to x_0}\frac{f'(x)}{g'(x)}</equation>.


设<equation>\textcircled{1}\lim_{x\to x_1}f(x) = \infty ,\lim_{x\to x_1}g(x) = \infty ;</equation>

<equation>\textcircled{2} f ( x )</equation>, g ( x ) 在<equation>x_{0}</equation>的某去心邻域内可导，且<equation>g^{\prime}(x)\neq0;</equation>

<equation>\textcircled{3} \lim_{x \to x_0} \frac{f^{\prime}(x)}{g^{\prime}(x)} = A</equation>或为<equation>\infty,</equation>

则<equation>\lim_{x\to x_1}\frac{f(x)}{g(x)} = \lim_{x\to x_1}\frac{f'(x)}{g'(x)}</equation>.


设<equation>f(x)</equation>在区间 I 上满足<equation>f^{\prime}(x)\geqslant 0</equation>（或<equation>f^{\prime}(x)\leqslant 0</equation>），且不在任意子区间上恒取等号，则<equation>f(x)</equation>在区间 I 上单调增加（或单调减少）.


设函数<equation>y = f(x)</equation>在点<equation>x_0</equation>的某个邻域内有定义.如果对于该邻域内任何异于<equation>x_0</equation>的点<equation>x</equation>，恒有<equation>f(x) < f(x_0)</equation>（或<equation>f(x) > f(x_0)</equation>），则称<equation>x_0</equation>为<equation>f(x)</equation>的一个极大值点（或极小值点），称<equation>f(x_0)</equation>为<equation>f(x)</equation>的极大值（或极小值).

---

设<equation>f(x)</equation>在<equation>x_0</equation>点取极值，且<equation>f^{\prime}(x_0)</equation>存在，则<equation>f^{\prime}(x_0) = 0.</equation>


设<equation>f(x)</equation>在<equation>x_{0}</equation>处连续，在<equation>x = x_{0}</equation>的去心邻域内可导，则

(a) 若在<equation>x_0</equation>的左侧邻域内<equation>f^{\prime}(x) > 0</equation>，右侧邻域内<equation>f^{\prime}(x) < 0</equation>，则<equation>f(x_0)</equation>为极大值.

(b)若在<equation>x_{0}</equation>的左侧邻域内<equation>f^{\prime}(x) < 0</equation>，右侧邻域内<equation>f^{\prime}(x) > 0</equation>，则<equation>f(x_{0})</equation>为极小值.

(c) 若在<equation>x = x_{0}</equation>的左、右邻域内<equation>f^{\prime}(x)</equation>同号，则<equation>f(x_{0})</equation>不是极值.


设<equation>f(x)</equation>在<equation>x_{0}</equation>处有二阶导数，<equation>f^{\prime}(x_{0}) = 0,f^{\prime \prime}(x_{0})\neq 0</equation>则

(a)当<equation>f^{\prime \prime} \left(x_{0}\right) > 0</equation>时，函数<equation>f(x)</equation>在点<equation>x_{0}</equation>处取得极小值.

(b)当<equation>f^{\prime \prime} \left(x_{0}\right) < 0</equation>时，函数<equation>f(x)</equation>在点<equation>x_{0}</equation>处取得极大值.


设函数<equation>y = f(x)</equation>在区间<equation>(a,b)</equation>内可导，<equation>x_{0}</equation>是<equation>(a,b)</equation>内任一点. 若曲线弧上点<equation>(x_{0},f(x_{0}))</equation>处的切线总位于

---


#### 5. 渐近线

曲线弧的下方，则称此曲线弧在<equation>(a,b)</equation>内是凹的；若曲线弧上点<equation>(x_0,f(x_0))</equation>处的切线总位于曲线弧的上方，则称此曲线弧在<equation>(a,b)</equation>内是凸的.


设<equation>f(x)</equation>在区间<equation>I</equation>上满足<equation>f^{\prime \prime}(x) \geqslant 0</equation>（或<equation>f^{\prime \prime}(x) \leqslant 0</equation>），且不在任一子区间上恒取等号，则曲线<equation>y = f(x)</equation>在区间<equation>I</equation>上是凹（或凸）的.


连续曲线弧上凹、凸部分的分界点称为曲线弧的拐点.


设点<equation>(x_{0}, f(x_{0}))</equation>为曲线<equation>y = f(x)</equation>的拐点，且<equation>f^{\prime \prime}(x_{0})</equation>存在，则<equation>f^{\prime \prime}(x_0) = 0.</equation>


设<equation>f(x)</equation>在<equation>x_{0}</equation>点的某邻域内二阶可导，并且在<equation>x_{0}</equation>的左、右邻域内<equation>f^{\prime \prime}(x)</equation>反号，则点<equation>(x_0,f(x_0))</equation>是曲线<equation>y = f(x)</equation>的拐点.


<equation>\textcircled{1}</equation>若<equation>\lim_{x\to +\infty}f(x)=C</equation>（或<equation>\lim_{x\to -\infty}f(x)=C)</equation>，则直线 y=C叫做曲线 y=f(x)的一条水平渐近线.

<equation>\textcircled{2}</equation>若<equation>\lim_{x\to x_0^+}f(x) = \infty</equation>（或<equation>\lim_{x\to x_0^+}f(x) = \infty</equation>），则直线<equation>x =</equation>

---


#### 3. 曲率半径

<equation>x_0</equation>叫做曲线<equation>y = f(x)</equation>的一条垂直渐近线.

<equation>\textcircled{3}</equation>若<equation>\lim_{x\to +\infty}[f(x) - ax - b] = 0</equation>（或<equation>\lim_{x\to -\infty}[f(x) - ax - b] = 0</equation>）<equation>(a\neq 0)</equation>，则直线<equation>y = ax + b</equation>叫做曲线<equation>y = f(x)</equation>的一条斜渐近线.


设<equation>y = f(x)</equation>是平面内的光滑曲线，则弧微分

<equation>\mathrm {d} s = \sqrt {1 + \left[ f ^ {\prime} (x) \right] ^ {2}} \mathrm {d} x;</equation>

若曲线方程为<equation>\left\{ \begin{array}{l}x = x(t),\\ y = y(t), \end{array} \right.</equation>则弧微分

<equation>\mathrm {d} s = \sqrt {\left[ x ^ {\prime} (t) \right] ^ {2} + \left[ y ^ {\prime} (t) \right] ^ {2}} \mathrm {d} t.</equation>


曲线<equation>y = f(x)</equation>上任一点<equation>(x,f(x))</equation>处的曲率为

<equation>K = \frac {\left| y ^ {\prime \prime} \right|}{\left[ 1 + \left(y ^ {\prime}\right) ^ {2} \right] ^ {\frac {3}{2}}};</equation>

曲线<equation>\left\{ \begin{array}{l}x = x(t),\\ y = y(t) \end{array} \right.</equation>上任一点处的曲率为

<equation>K = \frac {\left| x ^ {\prime} (t) y ^ {\prime \prime} (t) - y ^ {\prime} (t) x ^ {\prime \prime} (t) \right|}{\left\{\left[ x ^ {\prime} (t) \right] ^ {2} + \left[ y ^ {\prime} (t) \right] ^ {2} \right\} ^ {\frac {3}{2}}}.</equation>


<equation>R = \frac {1}{K} (K \neq 0).</equation>

---


### 第三章 一元函数积分学
#### 2. 不定积分的基本性质

设函数<equation>f(x)</equation>在区间<equation>I</equation>上有定义，若存在函数<equation>F(x)</equation>，使得在区间<equation>I</equation>上处处有<equation>F^{\prime}(x) = f(x)</equation>，若<equation>\mathrm{d}F(x) = f(x)\mathrm{d}x</equation>，则称<equation>F(x)</equation>是<equation>f(x)</equation>在区间<equation>I</equation>上的一个原函数.


函数<equation>f(x)</equation>在区间 I上的原函数的全体，称为<equation>f(x)</equation>在区间 I上的不定积分，记为<equation>\int f(x)\mathrm{d}x.</equation>


<equation>\textcircled{1}</equation><equation>\left[\int f(x)\mathrm{d}x\right]^{\prime} = f(x)</equation>，或<equation>\mathrm{d}\int f(x)\mathrm{d}x = f(x)\mathrm{d}x</equation>；

<equation>\textcircled{2}\int f^{\prime}(x)\mathrm{d}x = f(x) + C</equation>，或<equation>\int \mathrm{d}f(x) = f(x) + C</equation>

<equation>\textcircled{3}\int kf(x)\mathrm{d}x = k\int f(x)\mathrm{d}x</equation>（<equation>k</equation>为常数，且<equation>k\neq 0</equation>）；

---


#### 3. 不定积分的基本积分公式

<equation>\textcircled{1}</equation><equation>\int x^{a}\mathrm{d}x=\frac{1}{1+\alpha} x^{1+\alpha}+C \quad(\alpha \neq-1);</equation>

<equation>\textcircled{2} \int \frac{1}{x} \mathrm{d} x=\ln | x |+C;</equation>

<equation>\textcircled{3}</equation><equation>\int a^{x}\mathrm{d}x = \frac{a^{x}}{\ln a} +C,\int \mathrm{e}^{x}\mathrm{d}x = \mathrm{e}^{x} +C;</equation>

<equation>\textcircled{4} \int \cos x \mathrm{d} x=\sin x+C;</equation>

<equation>\textcircled{5} \int \sin x \mathrm{d} x=-\cos x+C;</equation>

<equation>\textcircled{6} \int \sec^{2} x \mathrm{d} x=\int \frac{1}{\cos^{2} x} \mathrm{d} x=\tan x+C;</equation>

<equation>\textcircled{8} \int \sec x\tan x\mathrm{d} x=\sec x+C;</equation>

<equation>\textcircled{9} \int \csc x\cot x\mathrm{d} x=-\csc x+C;</equation>

<equation>\textcircled{11} \int \csc x \mathrm{d} x = \ln | \csc x - \cot x | + C;</equation>

<equation>\textcircled{1 2} \int \frac{1}{a^{2}+x^{2}} \mathrm{d} x=\frac{1}{a} \arctan \frac{x}{a}+C,</equation>

<equation>\int \frac {1}{1 + x ^ {2}} \mathrm {d} x = \arctan x + C;</equation>

---


#### 4. 不定积分的计算方法

<equation>\textcircled{1 3} \int \frac {1}{\sqrt {a ^ {2} - x ^ {2}}} \mathrm {d} x = \arcsin \frac {x}{a} + C (a > 0),</equation>

<equation>\int \frac {1}{\sqrt {1 - x ^ {2}}} \mathrm {d} x = \arcsin x + C;</equation>

<equation>\textcircled{1 4} \int \frac {\mathrm {d} x}{a ^ {2} - x ^ {2}} = \frac {1}{2 a} \ln \left| \frac {a + x}{a - x} \right| + C;</equation>

<equation>\textcircled{1 5} \int \frac {1}{\sqrt {x ^ {2} \pm a ^ {2}}} d x = \ln | x + \sqrt {x ^ {2} \pm a ^ {2}} | + C.</equation>


(1) 第一换元积分法（凑微分法）

设<equation>f(u)</equation>有原函数<equation>F(u), u = \varphi(x)</equation>可导，则有

<equation>\begin{array}{l} \int f [ \varphi (x) ] \varphi^ {\prime} (x) \mathrm {d} x = \int f [ \varphi (x) ] \mathrm {d} \varphi (x) \\ = \int f (u) \mathrm {d} u = F (u) + C \\ = F [ \varphi (x) ] + C. \\ \end{array}</equation>

(2) 第二换元积分法

设函数<equation>x = \varphi (t)</equation>具有连续导数，且<equation>\varphi^{\prime}(t)\neq 0</equation>，又设<equation>f[\varphi (t)]\varphi^{\prime}(t)</equation>具有原函数<equation>\Phi (t)</equation>，则有

<equation>\begin{array}{l} \int f (x) \mathrm {d} x = \int f [ \varphi (t) ] \varphi^ {\prime} (t) \mathrm {d} t = \Phi (t) + C \\ = \Phi \left[ \varphi^ {- 1} (x) \right] + C. \\ \end{array}</equation>

(3) 分部积分法

设函数<equation>u = u(x), v = v(x)</equation>具有连续导数，则有

---


#### 3. 定积分的性质

<equation>\int u \mathrm {d} v = u v - \int v \mathrm {d} u.</equation>


<equation>\int_ {a} ^ {b} f (x) \mathrm {d} x = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} f \left(\xi_ {i}\right) \Delta x _ {i},</equation>

其中<equation>\xi_{i}\in [x_{i - 1},x_{i}]</equation>

<equation>\Delta x _ {i} = x _ {i} - x _ {i - 1},</equation>

<equation>\lambda = \max _ {1 \leqslant i \leqslant n} \left\{\Delta x _ {1}, \Delta x _ {2}, \dots , \Delta x _ {n} \right\}.</equation>


<equation>\textcircled{1}</equation><equation>f(x)</equation>在<equation>[a,b]</equation>上连续<equation>\Rightarrow f(x)</equation>在<equation>[a,b]</equation>上可积；

<equation>\textcircled{2}</equation><equation>f(x)</equation>在<equation>[a,b]</equation>上有界且只有有限个间断点<equation>\Rightarrow f(x)</equation>在<equation>[a,b]</equation>上可积；

<equation>\textcircled{3} f ( x )</equation>在<equation>[ a,b]</equation>上单调有界<equation>\Rightarrow f ( x )</equation>在<equation>[ a,b]</equation>上可积.


设<equation>f ( x )</equation>，<equation>g ( x )</equation>在区间<equation>[ a,b]</equation>上可积，则

<equation>\textcircled{3}</equation><equation>\int_{a}^{b}1\cdot \mathrm{d}x=\int_{a}^{b}\mathrm{d}x=b-a.</equation>

---


#### 4. 重要的定理、公式、关系

<equation>\textcircled{4}</equation>若<equation>f(x)</equation>在由<equation>a,b,c</equation>构成的最大的区间上可积，则

<equation>\int_ {a} ^ {b} f (x) \mathrm {d} x = \int_ {a} ^ {c} f (x) \mathrm {d} x + \int_ {c} ^ {b} f (x) \mathrm {d} x.</equation>

<equation>\textcircled{5}</equation>若在区间<equation>[a,b]</equation>上<equation>f(x)\leqslant g(x)</equation>，则

<equation>\int_ {a} ^ {b} f (x) \mathrm {d} x \leqslant \int_ {a} ^ {b} g (x) \mathrm {d} x.</equation>

<equation>\textcircled{6}</equation>如果 f(x)在区间<equation>[a,b]</equation>上的最大值与最小值分别为 M,m，则

<equation>m (b - a) \leqslant \int_ {a} ^ {b} f (x) \mathrm {d} x \leqslant M (b - a).</equation>

此性质称为定积分的估值定理.

<equation>\textcircled{7}</equation>（积分中值定理）如果<equation>f(x)</equation>在区间<equation>[a,b]</equation>上连续，则在<equation>[a,b]</equation>上至少存在一点<equation>\xi</equation>，使

<equation>\int_ {a} ^ {b} f (x) \mathrm {d} x = f (\xi) (b - a).</equation>

称<equation>\frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x</equation>为函数<equation>y=f(x)</equation>在区间<equation>[a,b]</equation>上的平均值.


(1) 变上限函数的求导定理

设<equation>f(x)</equation>在区间<equation>[a,b]</equation>上连续，则变上限函数<equation>F(x) = \int_{a}^{x} f(t)\mathrm{d}t</equation>在区间<equation>[a,b]</equation>上可导，且<equation>F^{\prime}(x) = f(x)</equation>.

---


#### (3)换元积分法

设<equation>f ( x )</equation>在区间<equation>[ a,b]</equation>上连续，<equation>F ( x )</equation>是它的任一个原函数，则

<equation>\int_ {a} ^ {b} f (x) \mathrm {d} x = F (x) \Bigg | _ {a} ^ {b} = F (b) - F (a).</equation>

(3) 定积分和不定积分之间的关系

<equation>\int f (x) \mathrm {d} x = \int_ {a} ^ {x} f (t) \mathrm {d} t + C.</equation>


如果<equation>f(x)</equation>在<equation>[a,b]</equation>上连续，并且容易求出它的一个原函数<equation>F(x)</equation>，则

<equation>\left. \int_ {a} ^ {b} f (x) \mathrm {d} x = F (x) \right| _ {a} ^ {b} = F (b) - F (a).</equation>


定积分的分部积分法，其公式与方法和不定积分类似，只是多了个上、下限而已.

<equation>\left. \int_ {a} ^ {b} u (x) \mathrm {d} v (x) = \left[ u (x) v (x) \right] \right| _ {a} ^ {b} - \int_ {a} ^ {b} v (x) \mathrm {d} u (x).</equation>


设<equation>f(x)</equation>在<equation>[a,b]</equation>上连续，函数<equation>x = \varphi(t)</equation>满足条件；

<equation>\textcircled{1} \varphi (\alpha) = a, \varphi (\beta) = b.</equation>

<equation>\textcircled{2}\varphi (t)</equation>在<equation>[\alpha ,\beta ]</equation>或<equation>[\beta ,\alpha ]</equation>上为单值、有连续导数的函

---


#### 6. 有关定积分的重要结论

数，则有

<equation>\int_ {a} ^ {b} f (x) \mathrm {d} x = \int_ {\alpha} ^ {\beta} f [ \varphi (t) ] \varphi^ {\prime} (t) \mathrm {d} t.</equation>


<equation>\textcircled{1}</equation>设<equation>f(x)</equation>是在区间<equation>[-a,a](a > 0)</equation>上连续的偶函数，则

<equation>\int_ {- a} ^ {a} f (x) \mathrm {d} x = 2 \int_ {0} ^ {a} f (x) \mathrm {d} x.</equation>

<equation>\textcircled{2}</equation>设<equation>f(x)</equation>是在区间<equation>[-a,a](a > 0)</equation>上连续的奇函数，则

<equation>\int_ {- a} ^ {a} f (x) \mathrm {d} x = 0.</equation>

<equation>\textcircled{3}</equation>设<equation>f(x)</equation>在<equation>(-\infty , + \infty)</equation>内是以<equation>T</equation>为周期的连续的周期函数，则对任意常数<equation>a</equation>和任意正整数<equation>n</equation>，都有

<equation>\int_ {a} ^ {a + T} f (x) \mathrm {d} x = \int_ {0} ^ {T} f (x) \mathrm {d} x,</equation>

<equation>\int_ {a} ^ {a + n T} f (x) \mathrm {d} x = n \int_ {0} ^ {T} f (x) \mathrm {d} x.</equation>

<equation>\textcircled{4}</equation>设<equation>f(x)</equation>在<equation>[-1,1]</equation>上连续，则

<equation>\int_ {0} ^ {\frac {\pi}{2}} f (\sin x) \mathrm {d} x = \int_ {0} ^ {\frac {\pi}{2}} f (\cos x) \mathrm {d} x,</equation>

<equation>\int_ {0} ^ {\pi} x f (\sin x) \mathrm {d} x = \frac {\pi}{2} \int_ {0} ^ {\pi} f (\sin x) \mathrm {d} x,</equation>

---


#### 7. 定积分的应用

<equation>\int_ {0} ^ {\pi} f (\sin x) \mathrm {d} x = 2 \int_ {0} ^ {\frac {\pi}{2}} f (\sin x) \mathrm {d} x.</equation>

<equation>\textcircled{5}</equation>华里士公式

<equation>\begin{array}{l} \int_ {0} ^ {\frac {\pi}{2}} \sin^ {2 n} x \mathrm {d} x = \int_ {0} ^ {\frac {\pi}{2}} \cos^ {2 n} x \mathrm {d} x \\ = \frac {1}{2} \cdot \frac {3}{4} \cdot \dots \cdot \frac {2 n - 1}{2 n} \cdot \frac {\pi}{2}, \\ \end{array}</equation>

<equation>\begin{array}{l} \int_ {0} ^ {\frac {\pi}{2}} \sin^ {2 n + 1} x \mathrm {d} x = \int_ {0} ^ {\frac {\pi}{2}} \cos^ {2 n + 1} x \mathrm {d} x \\ = 1 \cdot \frac {2}{3} \cdot \frac {4}{5} \cdot \dots \cdot \frac {2 n}{2 n + 1}. \\ \end{array}</equation>


(1) 求平面图形的面积

<equation>\textcircled{1}</equation>由曲线<equation>y = f(x), x = a, x = b(a < b)</equation>及<equation>x</equation>轴所围成封闭平面图形的面积为

<equation>S = \int_ {a} ^ {b} | f (x) | \mathrm {d} x.</equation>

<equation>\textcircled{2}</equation>由曲线<equation>y=f(x),y=g(x)</equation>及直线<equation>x=a,x= b(a<b)</equation>所围成封闭平面图形的面积为

<equation>S = \int_ {a} ^ {b} | f (x) - g (x) | \mathrm {d} x.</equation>

<equation>\textcircled{3}</equation>要求由曲线<equation>y = f(x)</equation>与<equation>y = g(x)</equation>所围成的封闭平面图形的面积，需先求出两条曲线的交点，即求解方

---

程组<equation>\left\{ \begin{array}{l l} y=f(x), \\ y=g(x) \end{array} \right.</equation>得出解中 x的最小值记为 a，解中 x的最大值记为 b，则

<equation>S = \int_ {a} ^ {b} | f (x) - g (x) | \mathrm {d} x.</equation>

<equation>\textcircled{4}</equation>在极坐标系下，如果曲线<equation>r = r(\theta),\theta = \alpha ,\theta = \beta (\alpha < \beta)</equation>围成的平面封闭图形面积为 S，则

<equation>S = \int_ {\alpha} ^ {\beta} \frac {1}{2} r ^ {2} (\theta) \mathrm {d} \theta .</equation>

如果曲线<equation>r = r_{1}(\theta),r = r_{2}(\theta),\theta = \alpha ,\theta = \beta (\alpha < \beta)</equation>围成的平面封闭图形面积为S，则

<equation>S = \int_ {a} ^ {\beta} \frac {1}{2} \mid r _ {1} ^ {2} (\theta) - r _ {2} ^ {2} (\theta) \mid \mathrm {d} \theta .</equation>

<equation>\textcircled{5}</equation>曲边由参数方程<equation>\left\{ \begin{array}{l l} x = \varphi (t), \\ y = \psi (t) \end{array} \right.</equation>给出的曲边梯形的面积为

<equation>S = \int_ {a} ^ {b} y \mathrm {d} x \xlongequal {x = \varphi (t)} \int_ {a} ^ {\beta} \psi (t) \cdot \varphi^ {\prime} (t) \mathrm {d} t.</equation>

(2) 求平行截面面积已知的立体体积

若垂直于<equation>x</equation>轴的平面截立体<equation>\Omega</equation>所得截面积是<equation>x</equation>的连续函数<equation>A(x)(a \leqslant x \leqslant b)</equation>，则<equation>\Omega</equation>的体积为

<equation>V = \int_ {a} ^ {b} A (x) \mathrm {d} x, \text {其 中} a < b.</equation>

---


#### （3）求旋转体的体积

<equation>\textcircled{1}</equation>如下图所示的平面图形绕 x轴旋转所得立体的体积为

<equation>V = \int_{a}^{b}\pi f^{2}(x)\mathrm{d}x</equation>，其中<equation>a < b.</equation>

<equation>\textcircled{2}</equation>如下图所示的平面图形绕<equation>x</equation>轴旋转所得立体的体积为

---

<equation>V = \pi \int_ {a} ^ {b} \left[ f ^ {2} (x) - g ^ {2} (x) \right] \mathrm {d} x,</equation>

其中<equation>a < b,f(x)\geqslant g(x)\geqslant 0.</equation>

<equation>\textcircled{3}</equation>如下图所示的平面图形绕 y轴旋转所得立体的体积为

<equation>V = 2 \pi \int_ {a} ^ {b} x \mid f (x) \mid \mathrm {d} x, \text {其 中} 0 \leqslant a \leqslant b.</equation>

<equation>\textcircled{4}</equation>如下图所示的平面图形绕 y轴旋转所得立体的体积为

---


#### （5）求平面曲线段的弧长

<equation>V = 2 \pi \int_ {a} ^ {b} x [ f (x) - g (x) ] \mathrm {d} x,</equation>

其中<equation>0 \leqslant a < b, f(x) \geqslant g(x)</equation>.


<equation>\textcircled{1}</equation>如下图所示的曲线弧绕<equation>x</equation>轴旋转所得旋转曲面的表面积为

<equation>S = 2 \pi \int_ {x} ^ {b} | f (x) | \sqrt {1 + \left[ f ^ {\prime} (x) \right] ^ {2}} \mathrm {d} x,</equation>

其中 a < b.

<equation>\textcircled{2}</equation>如上图所示的曲线弧绕<equation>y</equation>轴旋转所得旋转曲面的表面积为

<equation>S = 2 \pi \int_ {a} ^ {b} x \sqrt {1 + \left[ f ^ {\prime} (x) \right] ^ {2}} \mathrm {d} x,</equation>

其中<equation>0\leqslant a < b</equation>


<equation>\textcircled{1}</equation>曲线段<equation>y = f(x)</equation>,<equation>a \leqslant x \leqslant b</equation>, 设<equation>f(x)</equation>有连续导

---


#### 三、反常积分

数，则所给平面曲线段的弧长为

<equation>S = \int_ {a} ^ {b} \sqrt {1 + f ^ {\prime 2} (x)} \mathrm {d} x.</equation>

<equation>\textcircled{2}</equation>如果曲线弧段AB的方程可表示为<equation>x=x(t)</equation><equation>y=y(t)(\alpha \leqslant t\leqslant \beta)</equation>，且<equation>x=x(t),y=y(t)</equation>在区间<equation>(\alpha ,\beta)</equation>内有连续导数，则曲线弧<equation>\widehat{AB}</equation>的长度为

<equation>S = \int_ {\alpha} ^ {\beta} \sqrt {x ^ {\prime 2} (t) + y ^ {\prime 2} (t)} \mathrm {d} t.</equation>

<equation>\textcircled{3}</equation>如果曲线弧AB可以用极坐标表示为<equation>r=r(\theta)</equation><equation>(\alpha\leqslant\theta\leqslant\beta)</equation>，则曲线弧长为

<equation>S = \int_ {\alpha} ^ {\beta} \sqrt {r ^ {2} (\theta) + r ^ {\prime 2} (\theta)} \mathrm {d} \theta .</equation>


1. 无穷区间上的反常积分

<equation>\textcircled{1}</equation>设<equation>f(x)</equation>在<equation>[a, +\infty)</equation>上连续，称

<equation>\int_ {a} ^ {+ \infty} f (x) \mathrm {d} x = \lim _ {b \rightarrow + \infty} \int_ {a} ^ {b} f (x) \mathrm {d} x</equation>

为<equation>f(x)</equation>在<equation>[a, +\infty)</equation>上的反常积分. 若上式右边的极限存在，称此反常积分收敛；若极限不存在，称此反常积分发散.

<equation>\textcircled{2}</equation>设 f(x)在<equation>(-\infty,b]</equation>上连续，称

<equation>\int_ {- \infty} ^ {b} f (x) \mathrm {d} x = \lim _ {a \rightarrow - \infty} \int_ {a} ^ {b} f (x) \mathrm {d} x</equation>

---


#### 2. 无界函数的反常积分

为<equation>f(x)</equation>在<equation>(-\infty ,b)</equation>上的反常积分. 若上式右边的极限存在，称此反常积分收敛；若极限不存在，称此反常积分发散.

<equation>\textcircled{3}</equation>设<equation>f(x)</equation>在<equation>(-\infty , + \infty)</equation>内连续，称

<equation>\int_ {- \infty} ^ {+ \infty} f (x) \mathrm {d} x = \int_ {- \infty} ^ {c} f (x) \mathrm {d} x + \int_ {c} ^ {+ \infty} f (x) \mathrm {d} x</equation>

为<equation>f(x)</equation>在<equation>(-\infty , + \infty)</equation>内的反常积分.如果反常积分<equation>\int_{-\infty}^{c} f(x)\mathrm{d}x</equation>和<equation>\int_{c}^{+\infty} f(x)\mathrm{d}x</equation>都收敛，则称反常积分<equation>\int_{-\infty}^{+\infty} f(x)\mathrm{d}x</equation>收敛；否则就称反常积分<equation>\int_{-\infty}^{+\infty} f(x)\mathrm{d}x</equation>发散.


<equation>\textcircled{1}</equation>设<equation>f(x)</equation>在<equation>[a,b)</equation>上连续，且<equation>\lim f(x) = \infty</equation>，则称

<equation>\int_ {a} ^ {b} f (x) \mathrm {d} x = \lim _ {\varepsilon \rightarrow 0 ^ {+}} \int_ {a} ^ {b - \varepsilon} f (x) \mathrm {d} x</equation>

为<equation>f(x)</equation>在<equation>[a,b)</equation>上的反常积分. 若上式右边的极限存在，称此反常积分收敛；若极限不存在，称此反常积分发散. 使<equation>f(x)\rightarrow \infty</equation>的点<equation>b</equation>称为<equation>f(x)</equation>的奇点（也称瑕点).

<equation>\textcircled{2}</equation>设<equation>f(x)</equation>在<equation>(a,b]</equation>上连续，且<equation>\lim_{x\to \infty}f(x) = \infty</equation>，则称

<equation>\int_ {a} ^ {b} f (x) \mathrm {d} x = \lim _ {\varepsilon \rightarrow 0 ^ {+}} \int_ {a + \varepsilon} ^ {b} f (x) \mathrm {d} x</equation>

为<equation>f(x)</equation>在<equation>[a,b]</equation>上的反常积分. 若上式右边的极限存

---

在，称此反常积分收敛；若极限不存在，称此反常积分发散.

<equation>\textcircled{3}</equation>设<equation>f(x)</equation>在<equation>[a,b]</equation>上除点<equation>c(a < c < b)</equation>外连续，<equation>\lim_{x\to c}f(x) = \infty</equation>，则反常积分<equation>\int_{a}^{b}f(x)\mathrm{d}y</equation>定义为

<equation>\int_ {a} ^ {b} f (x) \mathrm {d} x = \int_ {a} ^ {c} f (x) \mathrm {d} x + \int_ {c} ^ {b} f (x) \mathrm {d} x.</equation>

如果反常积分<equation>\int_{a}^{c} f(x)\mathrm{d}x</equation>和<equation>\int_{c}^{b} f(x)\mathrm{d}x</equation>都收敛，则称反常积分<equation>\int_{a}^{b} f(x)\mathrm{d}x</equation>收敛，否则就称反常积分<equation>\int_{a}^{b} f(x)\mathrm{d}x</equation>发散.

---


### 第四章 向量代数和空间解析几何
#### 2. 两向量的夹角

1. 向量的数量积、向量积与混合积

设<equation>\boldsymbol{a}=\{a_{x},a_{y},a_{z}\}</equation><equation>\boldsymbol{b}=\{b_{x},b_{y},b_{z}\}</equation><equation>\boldsymbol{c}=\{c_{x},c_{y},c_{z}\}</equation>，则

(1) 数量积

<equation>\boldsymbol {a} \cdot \boldsymbol {b} = a _ {x} b _ {x} + a _ {y} b _ {y} + a _ {z} b _ {z}.</equation>

(2) 向量积

<equation>\boldsymbol {a} \times \boldsymbol {b} = \left| \begin{array}{c c c} \boldsymbol {i} & \boldsymbol {j} & \boldsymbol {k} \\ a _ {x} & a _ {y} & a _ {z} \\ b _ {x} & b _ {y} & b _ {z} \end{array} \right|.</equation>

(3) 混合积

<equation>(a \times b) \cdot c = \left| \begin{array}{c c c} a _ {x} & a _ {y} & a _ {z} \\ b _ {x} & b _ {y} & b _ {z} \\ c _ {x} & c _ {y} & c _ {z} \end{array} \right|.</equation>


(1) 两向量夹角的余弦

---


#### 1. 平面的方程

<equation>\cos \theta = \frac {a _ {x} b _ {x} + a _ {y} b _ {y} + a _ {z} b _ {z}}{\sqrt {a _ {x} ^ {2} + a _ {y} ^ {2} + a _ {z} ^ {2}} \sqrt {b _ {x} ^ {2} + b _ {y} ^ {2} + b _ {z} ^ {2}}}.</equation>

(2) 两非零向量平行与垂直的条件

<equation>\textcircled{1}</equation>垂直

<equation>a \bot b \Leftrightarrow a \cdot b = 0 \Leftrightarrow a _ {x} b _ {x} + a _ {y} b _ {y} + a _ {x} b _ {z} = 0.</equation>

<equation>\textcircled{2}</equation>平行

<equation>a / / b \Leftrightarrow a \times b = 0 \Leftrightarrow \frac {a _ {x}}{b _ {x}} = \frac {a _ {y}}{b _ {y}} = \frac {a _ {x}}{b _ {x}}.</equation>

(3) 方向余弦

<equation>\textcircled{1}</equation>计算公式

<equation>\cos a = \frac {a _ {x}}{\sqrt {a _ {x} ^ {2} + a _ {y} ^ {2} + a _ {z} ^ {2}}},</equation>

<equation>\cos \beta = \frac {a _ {y}}{\sqrt {a _ {x} ^ {2} + a _ {y} ^ {2} + a _ {z} ^ {2}}},</equation>

<equation>\cos \gamma = \frac {a _ {x}}{\sqrt {a _ {x} ^ {2} + a _ {y} ^ {2} + a _ {z} ^ {2}}}.</equation>

<equation>\textcircled{2}</equation>关系

<equation>\cos^ {2} \alpha + \cos^ {2} \beta + \cos^ {2} \gamma = 1.</equation>


(1) 点法式方程

<equation>A \left(x - x _ {0}\right) + B \left(y - y _ {0}\right) + C \left(z - z _ {0}\right) = 0.</equation>

---


#### （4）直线的两点式方程

(2) 平面的一般式方程

<equation>A x + B y + C z + D = 0.</equation>

(3) 平面的截距式方程

<equation>\frac {x}{a} + \frac {y}{b} + \frac {z}{c} = 1.</equation>


点<equation>M_{0}\left(x_{0},y_{0},z_{0}\right)</equation>到平面<equation>A x+B y+C z+D=0</equation>的距离为

<equation>d = \frac {\left| A x _ {0} + B y _ {0} + C z _ {0} + D \right|}{\sqrt {A ^ {2} + B ^ {2} + C ^ {2}}}.</equation>


(1) 直线的标准式（对称式）方程

<equation>\frac {x - x _ {0}}{m} = \frac {y - y _ {0}}{n} = \frac {z - z _ {0}}{p}.</equation>

(2) 直线的一般式方程

<equation>\left\{ \begin{array}{l} A _ {1} x + B _ {1} y + C _ {1} z + D _ {1} = 0, \\ A _ {2} x + B _ {2} y + C _ {2} z + D _ {2} = 0. \end{array} \right.</equation>

(3) 直线的参数式方程

<equation>\left\{ \begin{array}{l} x = x _ {0} + m t, \\ y = y _ {0} + n t, \\ z = z _ {0} + p t. \end{array} \right.</equation>


过点<equation>M_{1}\left(x_{1},y_{1},z_{1}\right)</equation>与<equation>M_{2}\left(x_{2},y_{2},z_{2}\right)</equation>的直线方程为

---


#### 2. 空间曲线的方程

<equation>\frac {x - x _ {1}}{x _ {2} - x _ {1}} = \frac {y - y _ {1}}{y _ {2} - y _ {1}} = \frac {z - z _ {1}}{z _ {2} - z _ {1}}.</equation>


点<equation>M_{0}\left(x_{0},y_{0},z_{0}\right)</equation>到直线<equation>\frac{x-x_{1}}{m}=\frac{y-y_{1}}{n}=\frac{z-z_{1}}{p}</equation>的垂直距离为

<equation>d = \frac {\left| \left| \begin{array}{c c c} i & j & k \\ x _ {1} - x _ {0} & y _ {1} - y _ {0} & z _ {1} - z _ {0} \\ m & n & p \end{array} \right| \right|}{\sqrt {m ^ {2} + n ^ {2} + p ^ {2}}}.</equation>


(1) 一般式方程

<equation>F (x, y, z) = 0.</equation>

(2) 参数式方程

<equation>\left\{ \begin{array}{l} x = x (u, v), \\ y = y (u, v), \\ z = z (u, v). \end{array} \right.</equation>


(1) 空间曲线的一般式方程

---


#### 3. 常见曲面与曲线

<equation>\left\{ \begin{array}{l} F (x, y, z) = 0, \\ G (x, y, z) = 0. \end{array} \right.</equation>

(2) 空间曲线的参数式方程

<equation>\left\{ \begin{array}{l} x = x (t), \\ y = y (t), \\ z = z (t). \end{array} \right.</equation>

(3) 空间曲线在坐标面上投影曲线的方程

空间曲线<equation>\varGamma</equation>：<equation>\left\{ \begin{array}{l} F (x,y,z) = 0, \\ G (x,y,z) = 0 \end{array} \right.</equation>在 xOy坐标面上的投影曲线，可以采取以下方法来求：

从方程组<equation>\left\{ \begin{array}{l} F(x,y,z) = 0, \\ G(x,y,z) = 0 \end{array} \right.</equation>中消去 z，得方程

<equation>H (x, y) = 0,</equation>

于是<equation>\varGamma</equation>在<equation>xOy</equation>坐标面上的投影曲线方程为

<equation>\left\{ \begin{array}{l} H (x, y) = 0, \\ z = 0. \end{array} \right.</equation>


(1) 球面

<equation>(x - a) ^ {2} + (y - b) ^ {2} + (z - c) ^ {2} = R ^ {2}.</equation>

(2) 椭球面

<equation>\frac {x ^ {2}}{a ^ {2}} + \frac {y ^ {2}}{b ^ {2}} + \frac {z ^ {2}}{c ^ {2}} = 1.</equation>

---

(3) 单叶双曲面

<equation>\frac {x ^ {2}}{a ^ {2}} + \frac {y ^ {2}}{b ^ {2}} - \frac {z ^ {2}}{c ^ {2}} = 1.</equation>

(4) 双叶双曲面

<equation>\frac {x ^ {2}}{a ^ {2}} - \frac {y ^ {2}}{b ^ {2}} - \frac {z ^ {2}}{c ^ {2}} = 1.</equation>

(5) 椭圆抛物面

<equation>\frac {x ^ {2}}{2 p} + \frac {y ^ {2}}{2 q} = z \quad (p, q \text {同 号}).</equation>

(6) 双曲抛物面

<equation>\frac {x ^ {2}}{2 p} - \frac {y ^ {2}}{2 q} = z (p, q \text {同 号}).</equation>

(7) 锥面

<equation>\frac {x ^ {2}}{a ^ {2}} + \frac {y ^ {2}}{b ^ {2}} - \frac {z ^ {2}}{c ^ {2}} = 0.</equation>

---


### 第五章 多元函数微分学
#### 3. 复合函数微分法

函数<equation>z = f(x,y)</equation>的偏导数

<equation>\left. \frac {\partial z}{\partial x} \right| _ {x = 0} = \lim _ {\Delta x \rightarrow 0} \frac {f \left(x _ {0} + \Delta x , y _ {0}\right) - f \left(x _ {0} , y _ {0}\right)}{\Delta x},</equation>

<equation>\left. \frac {\partial z}{\partial y} \right| _ {y = \frac {x}{y}} = \lim _ {\Delta y \rightarrow 0} \frac {f \left(x _ {0} , y _ {0} + \Delta y\right) - f \left(x _ {0} , y _ {0}\right)}{\Delta y}.</equation>

存在，则称这两个极限值为<equation>z = f(x,y)</equation>在点<equation>(x_0,y_0)</equation>处对<equation>x,y</equation>的偏导数.


若<equation>\Delta z = A\Delta x + B\Delta y + o(\sqrt{(\Delta x)^2 + (\Delta y)^2})</equation>，则称<equation>z = f(x,y)</equation>在点<equation>(x,y)</equation>处可微，且<equation>\mathrm{d}z = \frac{\partial z}{\partial x}\mathrm{d}x + \frac{\partial z}{\partial y}\mathrm{d}y.</equation>


设函数<equation>z = f(u,v)</equation>可微，<equation>u = u(x,y)</equation>，<equation>v = v(x,y)</equation>具有一阶偏导数，并且它们可以构成<equation>z</equation>关于<equation>(x,y)</equation>在某区域<equation>D</equation>内的复合函数，则在<equation>D</equation>内复合函数的求导法则为

---

