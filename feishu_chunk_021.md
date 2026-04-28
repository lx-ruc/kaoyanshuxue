综上所述，X，Z不相互独立.

---

**2016年第22题 | 解答题 | 11分**
. (本题满分11分)

设二维随机变量 (X,Y)在区域 D = {(x,y) | 0 < x < 1,<equation>x^{2} < y < \sqrt{x}</equation>}上服从均匀分布，令<equation>U=\left\{\begin{array}{l l}1,&X\leqslant Y,\\ 0,&X>Y. \end{array} \right.</equation>I. 写出 (X,Y)的概率密度；

II. 问 U与 X是否相互独立？并说明理由；

III. 求 Z=U+X的分布函数 F(z).
**答案: **（I）<equation>f ( x,y)=\left\{\begin{array}{ll}3,&0<x<1,x^{2}<y<\sqrt{x},\\ 0,&\text{其他};\end{array}\right.</equation>（Ⅱ）U与X不相互独立；

（Ⅲ）<equation>F ( z )=\left\{\begin{array}{ll}0,&z<0,\\ \frac{3}{2} z^{2}-z^{3},&0\leqslant z<1,\\ 2 ( z-1 )^{\frac{3}{2}}-\frac{3}{2} z^{2}+3 z-1,&1\leqslant z<2,\\ 1,&z\geqslant 2.\end{array}\right.</equation>
**解析: **（I）区域D如图（a）所示，其面积为<equation>S = \int_ {0} ^ {1} \sqrt {x} \mathrm {d} x - \int_ {0} ^ {1} x ^ {2} \mathrm {d} x = \frac {2}{3} x ^ {\frac {3}{2}} \left| _ {0} ^ {1} - \frac {x ^ {3}}{3} \right| _ {0} ^ {1} = \frac {2}{3} - \frac {1}{3} = \frac {1}{3}.</equation>又由于<equation>(X, Y)</equation>在区域<equation>D</equation>上服从均匀分布，故<equation>(X, Y)</equation>的概率密度为<equation>f (x, y) = \left\{ \begin{array}{l l} 3, & 0 < x < 1, x ^ {2} < y < \sqrt {x}, \\ 0, & \text {其 他}. \end{array} \right.</equation>(a)

(b)

（Ⅱ）考虑<equation>P\{U = 0, X\leqslant t\}</equation><equation>P \{U = 0 \} = P \{X > Y \} = \iint f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {x ^ {2}} ^ {x} 3 \mathrm {d} y = \int_ {0} ^ {1} 3 \left(x - x ^ {2}\right) \mathrm {d} x = \frac {1}{2}.</equation>对<equation>t \leqslant 0</equation>，<equation>P\{X \leqslant t\} = 0</equation>，<equation>P\{U = 0, X \leqslant t\} = 0.</equation>于是，<equation>P \left\{U = 0, X \leqslant t \right\} = P \left\{U = 0 \right\} \cdot P \left\{X \leqslant t \right\}.</equation>对<equation>t \geqslant 1</equation>，<equation>P\{X \leqslant t\} = 1, P\{U = 0, X \leqslant t\} = P\{U = 0\}</equation>.于是，<equation>P \left\{U = 0, X \leqslant t \right\} = P \left\{U = 0 \right\} \cdot P \left\{X \leqslant t \right\}.</equation>对<equation>0 < t < 1</equation>，有效积分区域为图（b）中的蓝色区域.<equation>P \left\{U = 0, X \leqslant t \right\} = P \left\{X > Y, X \leqslant t \right\} = \int_ {0} ^ {t} \mathrm {d} x \int_ {x ^ {2}} ^ {x} 3 \mathrm {d} y = \int_ {0} ^ {t} 3 \left(x - x ^ {2}\right) \mathrm {d} x = \frac {3}{2} t ^ {2} - t ^ {3},</equation><equation>P \left\{X \leqslant t \right\} = \int_ {0} ^ {t} \mathrm {d} x \int_ {x ^ {2}} ^ {\sqrt {x}} 3 \mathrm {d} y = \int_ {0} ^ {t} 3 \left(\sqrt {x} - x ^ {2}\right) \mathrm {d} x = 2 t ^ {\frac {3}{2}} - t ^ {3}.</equation>于是，<equation>\begin{aligned} P \{U = 0, X \leqslant t \} - P \{U = 0 \} \cdot P \{X \leqslant t \} &= \frac {3}{2} t ^ {2} - t ^ {3} - \frac {1}{2} \left(2 t ^ {\frac {3}{2}} - t ^ {3}\right) \\ &= \frac {3}{2} t ^ {2} - \frac {1}{2} t ^ {3} - t ^ {\frac {3}{2}} \neq 0. (\mathrm {见 注} \textcircled{1}) \end{aligned}</equation>因此，当<equation>0 < t < 1</equation>时，U与X不相互独立.

（Ⅲ）由题设知，<equation>\begin{array}{l} F (z) = P \left\{Z \leqslant z \right\} = P \left\{U + X \leqslant z \right\} \\ = P \left\{U + X \leqslant z, U = 0 \right\} + P \left\{U + X \leqslant z, U = 1 \right\} \\ = P \left\{X \leqslant z, U = 0 \right\} + P \left\{X \leqslant z - 1, U = 1 \right\} \\ = P \left\{X \leqslant z, X > Y \right\} + P \left\{X \leqslant z - 1, X \leqslant Y \right\}. \\ \end{array}</equation>当<equation>z < 0</equation>时，<equation>z - 1 < 0</equation>，于是<equation>P\{X\leqslant z,X > Y\} = 0,P\{X\leqslant z - 1,X\leqslant Y\} = 0.</equation>从而<equation>F(z) = 0.</equation><equation>0 \leqslant z < 1</equation><equation>z - 1 < 0</equation><equation>P \left\{X \leqslant z - 1, X \leqslant Y \right\} = 0</equation><equation>F (z) = P \left\{X \leqslant z, X > Y \right\} = \int_ {0} ^ {z} \mathrm {d} x \int_ {x ^ {2}} ^ {x} 3 \mathrm {d} y = \int_ {0} ^ {z} 3 \left(x - x ^ {2}\right) \mathrm {d} x = \frac {3}{2} z ^ {2} - z ^ {3}.</equation>当<equation>1\leqslant z < 2</equation>时，<equation>0\leqslant z - 1 < 1</equation><equation>\begin{array}{l} F (z) = P \left\{X \leqslant z, X > Y \right\} + P \left\{X \leqslant z - 1, X \leqslant Y \right\} \\ = P \left\{X \leqslant 1, X > Y \right\} + P \left\{X \leqslant z - 1, X \leqslant Y \right\} \\ = \frac {1}{2} + \int_ {0} ^ {z - 1} \mathrm {d} x \int_ {x} ^ {\sqrt {x}} 3 \mathrm {d} y = \frac {1}{2} + \int_ {0} ^ {z - 1} 3 (\sqrt {x} - x) \mathrm {d} x \\ = \frac {1}{2} + 2 (z - 1) ^ {\frac {3}{2}} - \frac {3}{2} (z - 1) ^ {2} = 2 (z - 1) ^ {\frac {3}{2}} - \frac {3}{2} z ^ {2} + 3 z - 1. \\ \end{array}</equation>当<equation>z\geqslant 2</equation>时，<equation>z - 1\geqslant 1,F(z) = 1.</equation>综上所述，<equation>F (z) = \left\{ \begin{array}{ll} 0, & z < 0, \\ \frac{3}{2} z^{2} - z^{3}, & 0 \leqslant z < 1, \\ 2 (z - 1)^{\frac{3}{2}} - \frac{3}{2} z^{2} + 3 z - 1, & 1 \leqslant z < 2, \\ 1, & z \geqslant 2. \end{array} \right.</equation>

---

**2015年第14题 | 填空题 | 4分**
14. 设二维随机变量<equation>(X, Y)</equation>服从正态分布<equation>N(1, 0; 1, 1; 0)</equation>, 则<equation>P\{XY - Y < 0\} =</equation>___
**解析: **解 由题设知，X，Y不相关. 又由于（X，Y）服从正态分布，故X，Y相互独立. 从而<equation>\begin{aligned} P \{X Y - Y < 0 \} &= P \{(X - 1) Y < 0 \} = P \{X < 1, Y > 0 \} + P \{X > 1, Y < 0 \} \\ &= P \{X < 1 \} \cdot P \{Y > 0 \} + P \{X > 1 \} \cdot P \{Y < 0 \}. \end{aligned}</equation>由<equation>( X, Y ) \sim N ( 1, 0 ; 1, 1 ; 0 )</equation>可知，<equation>X\sim N ( 1, 1 )</equation><equation>Y\sim N ( 0, 1 )</equation>从而X，Y的概率密度的图形分别关于<equation>x=1</equation>，<equation>x=0</equation>对称，于是<equation>P \{ X < 1 \} = P \{ X > 1 \} = \frac{1}{2}</equation><equation>P \{ Y < 0 \} = P \{ Y > 0 \} = \frac{1}{2}.</equation>因此，<equation>P \left\{X Y - Y < 0 \right\} = \frac {1}{2} \times \frac {1}{2} + \frac {1}{2} \times \frac {1}{2} = \frac {1}{2}.</equation>

---

**2013年第22题 | 解答题 | 11分**
2. (本题满分11分)

设随机变量 X的概率密度为<equation>f ( x )=\left\{\begin{array}{ll}\frac{1}{9} x^{2},&0<x<3,\\ 0,&\text{其他}.\end{array} \right.</equation>令随机变量<equation>Y=\left\{\begin{array}{ll}2,&X\leqslant 1,\\ X,&1<X<2,\\ 1,&X\geqslant 2. \end{array} \right.</equation>I. 求 Y的分布函数；

II. 求概率<equation>P \{ X \leqslant Y \}</equation>
**答案: **(22) (I)<equation>F_{Y}(y)=\left\{ \begin{array}{ll}0,& y<1,\\ \frac{y^{3}+18}{27},& 1\leqslant y<2,\\ 1,& y\geqslant 2; \end{array} \right.</equation>（Ⅱ）<equation>\frac{8}{27}.</equation>
**解析: **解（I）记<equation>Y</equation>的分布函数为<equation>F_{Y}(y).</equation>由Y的定义知，<equation>P\{1\leqslant Y\leqslant 2\} = 1.</equation>当<equation>y < 1</equation>时，<equation>F_{Y}(y) = P\{Y\leqslant y\} = 0.</equation>当 1≤y<2时，<equation>\begin{aligned} F _ {Y} (y) &= P \{Y \leqslant y \} = P \{Y < 1 \} + P \{Y = 1 \} + P \{1 < Y \leqslant y \} \\ &= 0 + P \{X \geqslant 2 \} + P \{1 < X \leqslant y \} \\ &= \int_ {2} ^ {3} \frac {1}{9} x ^ {2} \mathrm {d} x + \int_ {1} ^ {y} \frac {1}{9} x ^ {2} \mathrm {d} x \\ &= \frac {1 9}{2 7} + \frac {y ^ {3} - 1}{2 7} = \frac {y ^ {3} + 1 8}{2 7}. \end{aligned}</equation>当<equation>y \geqslant 2</equation>时，<equation>F_{Y}(y) = P\{Y \leqslant y\} = 1.</equation>因此，<equation>Y</equation>的分布函数为<equation>F_{Y}(y) = \left\{ \begin{array}{ll}0, & y < 1,\\ \frac{y^{3} + 18}{27}, & 1\leqslant y < 2,\\ 1, & y\geqslant 2. \end{array} \right.</equation>（Ⅱ）（法一）由 Y的定义知，<equation>\begin{aligned} P \{X \leqslant Y \} &= P \{X < Y \} + P \{X = Y \} = P \{X \leqslant 1 \} + P \{1 < X < 2 \} \\ &= P \{X < 2 \} = \int_ {0} ^ {2} \frac {1}{9} x ^ {2} \mathrm {d} x = \frac {8}{2 7}. \end{aligned}</equation>（法二）<equation>P \{ X \leqslant Y \} = 1 - P \{ X > Y \} = 1 - P \{ X \geqslant 2 \} = P \{ X < 2 \} = \int_ {0} ^ {2} \frac {1}{9} x^{2} \mathrm {d} x = \frac {8}{2 7}.</equation>

---

**2012年第7题 | 选择题 | 4分 | 答案: A**
7. 设随机变量 X与 Y相互独立，且分别服从参数为1与参数为4的指数分布，则<equation>P\{X < Y\} =</equation>（    ）

A.<equation>\frac{1}{5}</equation>B.<equation>\frac{1}{3}</equation>C.<equation>\frac{2}{3}</equation>D.<equation>\frac{4}{5}</equation>
答案: A
**解析: **解 由题设知，<equation>f_{X}(x)=\left\{ \begin{array}{ll}\mathrm{e}^{-x},&x>0\\ 0,&x\leqslant 0, \end{array} \right. f_{Y}(y)=\left\{ \begin{array}{ll}4\mathrm{e}^{-4y},&y>0\\ 0,&y\leqslant 0. \end{array} \right.</equation>由于 X与Y相互独立，故 (X,Y）的概率密度为<equation>f (x, y) = f _ {X} (x) f _ {Y} (y) = \left\{ \begin{array}{l l} 4 \mathrm {e} ^ {- x - 4 y}, & x > 0, y > 0, \\ 0, & \text {其 他}. \end{array} \right.</equation>记<equation>D=\{(x,y)\mid x<y\}</equation>，则<equation>\begin{aligned} P \{X < Y \} &= \iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {+ \infty} \mathrm {d} y \int_ {0} ^ {y} 4 \mathrm {e} ^ {- x - 4 y} \mathrm {d} x = \int_ {0} ^ {+ \infty} 4 \mathrm {e} ^ {- 4 y} \left(1 - \mathrm {e} ^ {- y}\right) \mathrm {d} y \\ &= \int_ {0} ^ {+ \infty} \left(4 \mathrm {e} ^ {- 4 y} - 4 \mathrm {e} ^ {- 5 y}\right) \mathrm {d} y = 1 - \frac {4}{5} = \frac {1}{5}. \end{aligned}</equation>应选A.

---

**2009年第8题 | 选择题 | 4分 | 答案: B**
8. 设随机变量 X与 Y相互独立，且 X服从标准正态分布 N(0,1), Y的概率分布为<equation>P\{Y=0\}=P\{Y=1\}=\frac{1}{2}</equation>. 记<equation>F_{Z}(z)</equation>为随机变量 Z=XY的分布函数，则函数<equation>F_{Z}(z)</equation>的间断点个数为（    )

A.0 B.1 C.2 D.3
答案: B
**解析: **解 先用两种方法求<equation>F_{Z}(z).</equation>（法一）由定义知<equation>\begin{aligned} F _ {Z} (z) &= P \{Z \leqslant z \} = P \{X Y \leqslant z \} \\ &= P \{X Y \leqslant z, Y = 0 \} + P \{X Y \leqslant z, Y = 1 \} \\ &= P \{z \geqslant 0, Y = 0 \} + P \{X \leqslant z, Y = 1 \} \\ &= P \{z \geqslant 0, Y = 0 \} + P \{X \leqslant z \} \cdot P \{Y = 1 \} \quad (X \text {与} Y \text {相 互 独立}) \\ &= P \{z \geqslant 0, Y = 0 \} + \frac {1}{2} \Phi (z), \end{aligned}</equation>其中<equation>\varPhi (z)</equation>为标准正态分布函数.

当<equation>z < 0</equation>时，<equation>P\{z\geqslant 0, Y = 0\} = P(\varnothing) = 0</equation>，从而<equation>F_{Z}(z) = \frac{1}{2}\Phi (z).</equation>当<equation>z \geqslant 0</equation>时，<equation>P\{z \geqslant 0, Y = 0\} = P\{Y = 0\} = \frac{1}{2}</equation>，从而<equation>F_{Z}(z) = \frac{1}{2} +\frac{1}{2}\Phi (z).</equation>（法二）由全概率公式知<equation>\begin{array}{l} F _ {Z} (z) = P \{Z \leqslant z \} = P \{X Y \leqslant z \} \\ = P \left\{X Y \leqslant z \mid Y = 0 \right\} \cdot P \left\{Y = 0 \right\} + P \left\{X Y \leqslant z \mid Y = 1 \right\} \cdot P \left\{Y = 1 \right\} \\ = \frac {1}{2} P \left\{z \geqslant 0 \mid Y = 0 \right\} + \frac {1}{2} P \left\{X \leqslant z \mid Y = 1 \right\} \\ = \frac {1}{2} P \left\{z \geqslant 0 \right\} + \frac {1}{2} P \left\{X \leqslant z \right\} \quad (X \text {与} Y \text {相 互 独立}) \\ = \left\{ \begin{array}{l l} \frac {1}{2} \Phi (z), & z < 0, \\ \frac {1}{2} + \frac {1}{2} \Phi (z), & z \geqslant 0. \end{array} \right. \\ \end{array}</equation>由于<equation>\varPhi(z)</equation>连续，故<equation>F_{z}(z)</equation>仅在<equation>z = 0</equation>处间断，从而选B.

---


**2024年第22题 | 解答题 | 12分**


设总体 X服从<equation>[0,\theta]</equation>上的均匀分布，其中<equation>\theta\in(0,+\infty)</equation>为未知参数，<equation>X_{1},X_{2},\cdots,X_{n}</equation>为来自总体 X的简单随机样本.记<equation>X_{(n)}=\max\{X_{1},X_{2},\cdots,X_{n}\}, T_{c}=cX_{(n)}</equation>.

I. 求 c，使得<equation>T_{c}</equation>是<equation>\theta</equation>的无偏估计；

II. 记<equation>h(c)=E\left[ (T_{c}-\theta)^{2} \right]</equation>，求 c使得 h(c)最小.

**答案:**(1) 当<equation>c=\frac{n+1}{n}</equation>时，<equation>T_{c}</equation>是<equation>\theta</equation>的无偏估计.

(2) 当<equation>c=\frac{n+2}{n+1}</equation>时，h（c）最小.

**解析:**（I）由于<equation>X</equation>服从<equation>[0,\theta]</equation>上的均匀分布，故<equation>X</equation>的分布函数为<equation>F _ {X} (x) = \left\{ \begin{array}{l l} 0, & x < 0, \\ \frac {x}{\theta}, & 0 \leqslant x < \theta , \\ 1, & x \geqslant \theta . \end{array} \right.</equation>记随机变量<equation>Y = X_{(n)} = \max \left\{X_{1}, X_{2}, \dots, X_{n}\right\}</equation>. 计算<equation>Y</equation>的分布函数<equation>F_{Y}(y)</equation>.

当<equation>y < 0</equation>时，<equation>F_{Y}(y) = 0.</equation>当<equation>0\leqslant y < \theta</equation>时，<equation>\begin{array}{l} F _ {Y} (y) = P \left\{Y \leqslant y \right\} = P \left\{\max _ {1 \leqslant i \leqslant n} X _ {i} \leqslant y \right\} = P \left\{X _ {1} \leqslant y, X _ {2} \leqslant y, \dots , X _ {n} \leqslant y \right\} \\ \underline {{\text {独立 性}}} P \left\{X _ {1} \leqslant y \right\} P \left\{X _ {2} \leqslant y \right\} \dots P \left\{X _ {n} \leqslant y \right\} = F _ {X} ^ {n} (y) = \left(\frac {y}{\theta}\right) ^ {n}. \\ \end{array}</equation>当<equation>y\geqslant \theta</equation>时，<equation>F_{Y}(y) = 1.</equation>于是，<equation>F_{Y}(y) = \left\{ \begin{array}{ll}0, & y < 0,\\ \left(\frac{y}{\theta}\right)^{n}, & 0\leqslant y < \theta ,\\ 1, & y\geqslant \theta . \end{array} \right.</equation>对<equation>F_{Y}(y)</equation>求导，可得<equation>f _ {Y} (y) = F _ {Y} ^ {\prime} (y) = \left\{ \begin{array}{l l} \frac {n y ^ {n - 1}}{\theta^ {n}}, & 0 < y < \theta , \\ 0, & \text {其 他}. \end{array} \right.</equation>因此，<equation>\begin{aligned} E \left(T _ {c}\right) &= E (c Y) = c \int_ {- \infty} ^ {+ \infty} y \cdot f _ {Y} (y) \mathrm {d} y = c \int_ {0} ^ {\theta} y \cdot \frac {n y ^ {n - 1}}{\theta^ {n}} \mathrm {d} y = c \cdot \frac {n}{\theta^ {n}} \cdot \frac {y ^ {n + 1}}{n + 1} \Bigg | _ {0} ^ {\theta} \\ &= \frac {c n}{n + 1} \theta . \end{aligned}</equation>若<equation>T_{c}</equation>为<equation>\theta</equation>的无偏估计，则<equation>E\left(T_{c}\right)=\theta</equation>，从而<equation>\frac{cn}{n+1}\theta =\theta</equation>，解得<equation>c=\frac{n+1}{n}.</equation>（Ⅱ）展开 h(c）可得<equation>h (c) = E \left[ \left(T _ {c} - \theta\right) ^ {2} \right] = E \left[ \left(c Y - \theta\right) ^ {2} \right] = c ^ {2} E \left(Y ^ {2}\right) - 2 c \theta E (Y) + \theta^ {2}.</equation>计算<equation>E ( Y^{2})</equation><equation>E \left(Y ^ {2}\right) = \int_ {- \infty} ^ {+ \infty} y ^ {2} \cdot f _ {Y} (y) \mathrm {d} y = \int_ {0} ^ {\theta} y ^ {2} \cdot \frac {n y ^ {n - 1}}{\theta^ {n}} \mathrm {d} y = \frac {n}{\theta^ {n}} \cdot \frac {y ^ {n + 2}}{n + 2} \Bigg | _ {0} ^ {\theta} = \frac {n}{n + 2} \theta^ {2}.</equation>于是，<equation>h (c) = c ^ {2} \cdot \frac {n}{n + 2} \theta^ {2} - 2 c \cdot \frac {n}{n + 1} \theta^ {2} + \theta^ {2} = \left(\frac {n}{n + 2} c ^ {2} - \frac {2 n}{n + 1} c + 1\right) \theta^ {2}.</equation>令<equation>\frac{\mathrm{d}[h(c)]}{\mathrm{d}c}=\left(\frac{2n}{n+2} c-\frac{2n}{n+1}\right)\theta^{2}=0</equation>，解得<equation>c=\frac{n+2}{n+1}</equation>该点是h(c)的唯一驻点.又因为<equation>h^{\prime \prime}(c)</equation><equation>= \frac{2n}{n+2}\theta^{2} > 0</equation>，所以该唯一驻点是h(c)的极小值点，也是最小值点.

因此，当<equation>c=\frac{n+2}{n+1}</equation>时，h(c）最小.

---

**2023年第10题 | 选择题 | 5分 | 答案: A**

10. 设<equation>X_{1}, X_{2}</equation>为来自总体<equation>N\left(\mu ,\sigma^{2}\right)</equation>的简单随机样本，其中<equation>\sigma(\sigma>0)</equation>是未知参数.若<equation>\hat{\sigma}=a\left| X_{1}-X_{2}\right|</equation>为<equation>\sigma</equation>的无偏估计，则 a=（    ）

A.<equation>\frac{\sqrt{\pi}}{2}</equation>B.<equation>\frac{\sqrt{2\pi}}{2}</equation>C.<equation>\sqrt{\pi}</equation>D.<equation>\sqrt{2\pi}</equation>

答案: A

**解析:**解 由于<equation>X_{1}, X_{2}</equation>为来自总体<equation>N(\mu ,\sigma^{2})</equation>的简单随机样本，故<equation>X_{1}, X_{2}</equation>相互独立.

令<equation>Z = X_{1} - X_{2}</equation>，则<equation>Z\sim N(0,2\sigma^{2})</equation>，从而Z的概率密度<equation>f(z) = \frac{1}{\sqrt{2\pi}\cdot \sqrt{2}\sigma}\mathrm{e}^{-\frac{z^{2}}{4\sigma^{2}}}</equation>.<equation>\begin{aligned} E (\mid Z \mid) &= \int_ {- \infty} ^ {+ \infty} | z | f (z) \mathrm {d} z = 2 \int_ {0} ^ {+ \infty} \frac {1}{\sqrt {2 \pi} \cdot \sqrt {2} \sigma} \cdot z \mathrm {e} ^ {- \frac {z ^ {2}}{4 \sigma^ {2}}} \mathrm {d} z = \frac {1}{2 \sqrt {\pi} \sigma} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {z ^ {2}}{4 \sigma^ {2}}} \mathrm {d} \left(z ^ {2}\right) \\ &= \frac {1}{2 \sqrt {\pi} \sigma} \cdot \left(- 4 \sigma^ {2} \mathrm {e} ^ {- \frac {z ^ {2}}{4 \sigma^ {2}}}\right) \Big | _ {0} ^ {+ \infty} = \frac {2}{\sqrt {\pi}} \sigma . \end{aligned}</equation>由此可得<equation>E (\hat {\sigma}) = E \left(a \mid X _ {1} - X _ {2} \mid\right) = E \left(a \mid Z \mid\right) = \frac {2 a}{\sqrt {\pi}} \sigma .</equation>又因为<equation>\hat{\sigma}</equation>为<equation>\sigma</equation>的无偏估计，所以<equation>E(\hat{\sigma})=\sigma</equation>，即<equation>\frac{2a}{\sqrt{\pi}}\sigma=\sigma</equation>，解得 a<equation>=\frac{\sqrt{\pi}}{2}.</equation>因此，应选A.

---

**2021年第9题 | 选择题 | 5分 | 答案: C**

9. 设<equation>( X_{1}, Y_{1}), ( X_{2}, Y_{2}), \cdots, ( X_{n}, Y_{n} )</equation>为来自总体<equation>N (\mu_{1}, \mu_{2}; \sigma_{1}^{2}, \sigma_{2}^{2}; \rho)</equation>的简单随机样本，令<equation>\theta=\mu_{1}-\mu_{2}, \bar{X}=\frac{1}{n}\sum_{i=1}^{n} X_{i}, \bar{Y}=\frac{1}{n}\sum_{i=1}^{n} Y_{i}, \hat{\theta}=\bar{X}-\bar{Y}</equation>则（    )

A.<equation>\hat{\theta}</equation>是<equation>\theta</equation>的无偏估计，<equation>D(\hat{\theta})=\frac{\sigma_{1}^{2}+\sigma_{2}^{2}}{n}</equation>B.<equation>\hat{\theta}</equation>不是<equation>\theta</equation>的无偏估计，<equation>D(\hat{\theta})=\frac{\sigma_{1}^{2}+\sigma_{2}^{2}}{n}</equation>C.<equation>\hat{\theta}</equation>是<equation>\theta</equation>的无偏估计，<equation>D(\hat{\theta})=\frac{\sigma_{1}^{2}+\sigma_{2}^{2}-2\rho\sigma_{1}\sigma_{2}}{n}</equation>D.<equation>\hat{\theta}</equation>不是<equation>\theta</equation>的无偏估计，<equation>D(\hat{\theta})=\frac{\sigma_{1}^{2}+\sigma_{2}^{2}-2\rho\sigma_{1}\sigma_{2}}{n}</equation>

答案: C

**解析:**解 由于总体（X，Y）服从<equation>N(\mu_{1},\mu_{2};\sigma_{1}^{2},\sigma_{2}^{2};\rho)</equation>，故<equation>X\sim N(\mu_{1},\sigma_{1}^{2}),Y\sim N(\mu_{2},\sigma_{2}^{2})</equation>，从而<equation>\bar{X}\sim</equation><equation>N\left(\mu_{1},\frac{\sigma_{1}^{2}}{n}\right),\bar{Y}\sim N\left(\mu_{2},\frac{\sigma_{2}^{2}}{n}\right).</equation>计算<equation>E(\hat{\theta})</equation><equation>E (\hat {\theta}) = E (\bar {X} - \bar {Y}) = E (\bar {X}) - E (\bar {Y}) = \mu_ {1} - \mu_ {2} = \theta .</equation>因此，<equation>\hat{\theta}</equation>是<equation>\theta</equation>的无偏估计.

计算<equation>D(\hat{\theta})</equation><equation>D (\hat {\theta}) = D (\bar {X} - \bar {Y}) = D (\bar {X}) + D (\bar {Y}) - 2 \operatorname {C o v} (\bar {X}, \bar {Y}) = \frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{n} - 2 \operatorname {C o v} (\bar {X}, \bar {Y}).</equation>由于<equation>\left(X_{1},Y_{1}\right), \left(X_{2},Y_{2}\right),\dots ,\left(X_{n},Y_{n}\right)</equation>为简单随机样本，故它们相互独立，从而当<equation>i\neq j</equation>时，<equation>X_{i}</equation>与<equation>Y_{j}</equation>独立.于是，<equation>\operatorname{Cov}(X_{i},Y_{i})=\operatorname{Cov}(X,Y),\operatorname{Cov}(X_{i},Y_{j})=0(i\neq j).</equation><equation>\begin{aligned} \operatorname {C o v} (\bar {X}, \bar {Y}) &= \operatorname {C o v} \left(\frac {\sum_ {i = 1} ^ {n} X _ {i}}{n}, \frac {\sum_ {j = 1} ^ {n} Y _ {j}}{n}\right) = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \operatorname {C o v} \left(X _ {i}, Y _ {j}\right) = \frac {1}{n ^ {2}} \cdot \sum_ {i = 1} ^ {n} \operatorname {C o v} \left(X _ {i}, Y _ {i}\right) \\ &= \frac {1}{n ^ {2}} \cdot n \operatorname {C o v} (X, Y) = \frac {\operatorname {C o v} (X , Y)}{n}. \end{aligned}</equation>因此，<equation>D (\hat {\theta}) = \frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{n} - 2 \operatorname {C o v} (\bar {X}, \bar {Y}) = \frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{n} - \frac {2}{n} \operatorname {C o v} (X, Y) = \frac {\sigma_ {1} ^ {2} + \sigma_ {2} ^ {2} - 2 \rho \sigma_ {1} \sigma_ {2}}{n}.</equation>应选C.

---

**2016年第23题 | 解答题 | 11分**

3. (本题满分11分)

设总体 X的概率密度为<equation>f ( x; \theta) = \left\{ \begin{array}{l l} \frac{3 x^{2}}{\theta^{3}}, & 0 < x < \theta , \\ 0, & \mathrm {其 他}, \end{array} \right.</equation>其中<equation>\theta \in(0,+\infty)</equation>为未知参数，<equation>X_{1}, X_{2}, X_{3}</equation>为来自总体 X的简单随机样本，令<equation>T=\max \left\{X_{1}, X_{2}, X_{3}\right\}</equation>.

I. 求 T的概率密度；

II. 确定 a，使得 aT为<equation>\theta</equation>的无偏估计.

**答案:**<equation>(\mathrm {I}) f _ {T} (t) = \left\{ \begin{array}{l l} \frac {9 t ^ {8}}{\theta^ {9}}, & 0 < t < \theta , \\ 0, & \mathrm {其 他}; \end{array} \right. (\mathrm {I I}) a = \frac {1 0}{9}.</equation>

**解析:**解（I）设<equation>T</equation>的分布函数为<equation>F_{T}(t), T</equation>的概率密度为<equation>f_{T}(t).</equation>由于<equation>X_{1}, X_{2}, X_{3}</equation>为来自总体X的简单随机样本，故它们相互独立且与X同分布.从而<equation>\begin{array}{l} F _ {T} (t) = P \left\{T \leqslant t \right\} = P \left\{X _ {1} \leqslant t, X _ {2} \leqslant t, X _ {3} \leqslant t \right\} = P \left\{X _ {1} \leqslant t \right\} \cdot P \left\{X _ {2} \leqslant t \right\} \cdot P \left\{X _ {3} \leqslant t \right\} \\ = \left[ P \left\{X \leqslant t \right\} \right] ^ {3} = \left[ F _ {X} (t) \right] ^ {3}, \\ \end{array}</equation>其中<equation>F_{X}(t)</equation>为X的分布函数.

下面用两种方法求<equation>f_{T}(t)</equation>（法一）先求<equation>F_{T}(t)</equation>，再求导得到<equation>f_{T}(t)</equation>当<equation>t < 0</equation>时，<equation>F_{X}(t) = \int_{-\infty}^{t} f(x;\theta)\mathrm{d}x = 0.</equation>于是<equation>F_{T}(t) = [F_{X}(t)]^{3} = 0.</equation>当 0≤t <<equation>\theta</equation>时，<equation>F_{X}(t)=\int_{-\infty}^{t} f(x;\theta)\mathrm{d}x=\int_{0}^{t}\frac{3x^{2}}{\theta^{3}}\mathrm{d}x=\frac{t^{3}}{\theta^{3}}.</equation>于是<equation>F_{T}(t)=[F_{X}(t)]^{3}=\frac{t^{9}}{\theta^{9}}.</equation>当 t≥<equation>\theta</equation>时，<equation>F_{X}(t)=1.</equation>于是<equation>F_{T}(t)=[F_{X}(t)]^{3}=1.</equation>因此，<equation>F _ {T} (t) = \left\{ \begin{array}{l l} 0, & t < 0, \\ \frac {t ^ {9}}{\theta^ {9}}, & 0 \leqslant t < \theta , \\ 1, & t \geqslant \theta . \end{array} \right.</equation>综上所述，<equation>T</equation>的概率密度为<equation>f_{T}(t) = F_{T}^{\prime}(t) = \left\{ \begin{array}{ll} \frac{9t^{8}}{\theta^{9}}, & 0 < t < \theta , \\ 0, & \text{其他}. \end{array} \right.</equation>（法二）直接求导得到<equation>f_{T}(t)</equation>后再求解.<equation>f _ {T} (t) = F _ {T} ^ {\prime} (t) = 3 F _ {X} ^ {\prime} (t) \left[ F _ {X} (t) \right] ^ {2} = 3 f (t; \theta) \left[ F _ {X} (t) \right] ^ {2}.</equation>当<equation>t < 0</equation>时，<equation>f(t; \theta) = 0.</equation>于是<equation>f_{T}(t) = 0.</equation>当<equation>0 \leqslant t < \theta</equation>时，<equation>F_{X}(t) = \int_{-\infty}^{t} f(x; \theta)\mathrm{d}x = \int_{0}^{t} \frac{3x^{2}}{\theta^{3}}\mathrm{d}x = \frac{t^{3}}{\theta^{3}}.</equation>于是<equation>f _ {T} (t) = 3 f (t; \theta) \left[ F _ {X} (t) \right] ^ {2} = 3 \cdot \frac {3 t ^ {2}}{\theta^ {3}} \cdot \left(\frac {t ^ {3}}{\theta^ {3}}\right) ^ {2} = \frac {9 t ^ {8}}{\theta^ {9}}.</equation>当<equation>t \geqslant \theta</equation>时，<equation>f(t; \theta) = 0.</equation>于是<equation>f_{T}(t) = 0.</equation>综上所述，<equation>T</equation>的概率密度为<equation>f_{T}(t) = \left\{ \begin{array}{ll} \frac{9t^8}{\theta^9}, & 0 < t < \theta , \\ 0, & \text{其他}. \end{array} \right.</equation>（Ⅱ）由第（I）问中所求结果知，<equation>E (a T) = a E (T) = a \int_ {- \infty} ^ {+ \infty} t f _ {T} (t) \mathrm {d} t = a \int_ {0} ^ {\theta} \frac {9 t ^ {9}}{\theta^ {9}} \mathrm {d} t = \frac {9 a}{1 0 \theta^ {9}} t ^ {1 0} \Bigg | _ {0} ^ {\theta} = \frac {9}{1 0} a \theta .</equation>要使<equation>E(aT) = \theta</equation>，则<equation>\frac{9}{10} a\theta = \theta</equation>，解得<equation>a = \frac{10}{9}</equation>.

因此，当<equation>a=\frac{10}{9}</equation>时，<equation>aT</equation>为<equation>\theta</equation>的无偏估计.

---

**2014年第14题 | 填空题 | 4分**

14. 设总体 X的概率密度为 f(x;<equation>\theta)=\left\{\begin{array}{ll}\frac{2x}{3\theta^{2}},&\theta<x<2\theta,\\ 0,&\text{其他},\end{array} \right.</equation>其中<equation>\theta</equation>是未知参数，<equation>X_{1},X_{2},\cdots,X_{n}</equation>为来自总体 X的简单随机样本，若<equation>c\sum_{i=1}^{n}X_{i}^{2}</equation>是<equation>\theta^{2}</equation>的无偏估计，则 c=___

**解析:**由题设知，<equation>\theta^ {2} = E \left(c \sum_ {i = 1} ^ {n} X _ {i} ^ {2}\right) = n c E \left(X ^ {2}\right) = n c \int_ {\theta} ^ {2 \theta} x ^ {2} \cdot \frac {2 x}{3 \theta^ {2}} \mathrm {d} x = \frac {5}{2} \theta^ {2} n c,</equation>从而<equation>c = \frac{2}{5n}</equation>

---

**2010年第23题 | 解答题 | 11分**


设总体 X的概率分布为：

<table border="1"><tr><td>X</td><td>1</td><td>2</td><td>3</td></tr><tr><td>P</td><td>1-θ</td><td>θ-θ2</td><td>θ2</td></tr></table>

其中参数<equation>\theta \in (0,1)</equation>未知.以<equation>N_{i}</equation>表示来自总体<equation>X</equation>的简单随机样本（样本容量为<equation>n</equation>）中等于<equation>i</equation>的个数<equation>(i = 1,2,3)</equation>试求常数<equation>a_{1},a_{2},a_{3}</equation>，使<equation>T = \sum_{i = 1}^{3}a_{i}N_{i}</equation>为<equation>\theta</equation>的无偏估计量，并求<equation>T</equation>的方差.

**答案:**<equation>(2 3) a _ {1} = 0, a _ {2} = a _ {3} = \frac {1}{n}, D (T) = \frac {\theta (1 - \theta)}{n}.</equation>

**解析:**解 令<equation>T = \sum_{i = 1}^{3} a_{i} N_{i}</equation>为<equation>\theta</equation>的无偏估计量，则有<equation>\theta = E (T) = \sum_ {i = 1} ^ {3} a _ {i} E \left(N _ {i}\right).</equation>由<equation>N_{i}</equation>的定义知，<equation>N_{i}</equation>服从二项分布，即<equation>N_{1}\sim B(n,1 - \theta),N_{2}\sim B(n,\theta -\theta^{2}),N_{3}\sim B(n,\theta^{2})</equation>，从而<equation>E(N_{1}) = n(1 - \theta),E(N_{2}) = n(\theta -\theta^{2}),E(N_{3}) = n\theta^{2}</equation>.代入（1）式得<equation>\theta = a _ {1} n (1 - \theta) + a _ {2} n \left(\theta - \theta^ {2}\right) + a _ {3} n \theta^ {2},</equation>整理得<equation>0 = a _ {1} n + \left(a _ {2} n - a _ {1} n - 1\right) \theta + \left(a _ {3} n - a _ {2} n\right) \theta^ {2},</equation>从而<equation>a _ {1} n = 0, \quad a _ {2} n - a _ {1} n - 1 = 0, \quad a _ {3} n - a _ {2} n = 0,</equation>解得<equation>a_{1}=0,a_{2}=\frac{1}{n},a_{3}=\frac{1}{n}.</equation>又由<equation>N_{i}</equation>的定义知，<equation>N_{1}+N_{2}+N_{3}=n</equation>，故<equation>T = \sum_ {i = 1} ^ {3} a _ {i} N _ {i} = \frac {1}{n} \left(N _ {2} + N _ {3}\right) = \frac {1}{n} \left(n - N _ {1}\right) = 1 - \frac {1}{n} N _ {1},</equation>从而<equation>D (T) = D \left(1 - \frac {1}{n} N _ {1}\right) = \frac {1}{n ^ {2}} D \left(N _ {1}\right) = \frac {1}{n ^ {2}} \cdot n (1 - \theta) \theta = \frac {\theta (1 - \theta)}{n}.</equation>综上所述，<equation>a_{1}=0, a_{2}=\frac{1}{n}, a_{3}=\frac{1}{n}, D(T)=\frac{\theta(1-\theta)}{n}.</equation>

---

**2009年第14题 | 填空题 | 4分**

14. 设<equation>X_{1}, X_{2}, \cdots, X_{m}</equation>为来自二项分布总体<equation>B(n,p)</equation>的简单随机样本，<equation>\bar{X}</equation>和<equation>S^{2}</equation>分别为样本均值和样本方差，若<equation>\bar{X}+k S^{2}</equation>为<equation>n p^{2}</equation>的无偏估计量，则 k=___

**答案:**<equation>- 1.</equation>

**解析:**解 由题设知，<equation>n p^{2}=E(\overline{X}+k S^{2})=E(\overline{X})+k E(S^{2}).</equation>又<equation>E(\overline{X})=E(X)=np,</equation><equation>E(S^{2})=D(X)=np(1-p),</equation>故有<equation>n p^{2}=np+np(1-p)k</equation>，解得 k=-1.

---


**2014年第23题 | 解答题 | 11分**


23. (本题满分11分)

设总体 X的分布函数为<equation>F ( x ; \theta) = \left\{ \begin{array}{l l} 1 - \mathrm{e}^{- \frac {x^{2}}{\theta}}, & x \geqslant 0, \\ 0, & x < 0, \end{array} \right.</equation>其中<equation>\theta</equation>是未知参数且大于零.<equation>X_{1}, X_{2}, \dots , X_{n}</equation>为来自总体 X的简单随机样本.

I. 求<equation>E ( X )</equation>与<equation>E \left( X^{2} \right)</equation>II. 求<equation>\theta</equation>的最大似然估计量<equation>\hat{\theta}_{n}</equation>III. 是否存在实数 a，使得对任何<equation>\varepsilon > 0</equation>，都有<equation>\lim_{n \to \infty} P \{ | \hat{\theta}_{n}-a | \geqslant \varepsilon \}=0</equation>？

**答案:**(23) (I)<equation>E ( X )=\frac{\sqrt{\pi\theta}}{2}, E ( X^{2} )=\theta;</equation>(Ⅱ)<equation>\widehat{\theta}_n = \frac{1}{n}\sum_{i=1}^{n} X_i^2</equation>;

（Ⅲ）存在实数<equation>a = \theta</equation>，使得对任何<equation>\varepsilon > 0</equation>，都有<equation>\lim_{n\to \infty}P\{|\widehat{\theta}_n - a| \geqslant \varepsilon \} = 0.</equation>

**解析:**解（I）由题设知，X的概率密度<equation>f ( x ; \theta) = \left\{ \begin{array}{ll} \frac{2 x}{\theta} \mathrm{e}^{- \frac{x^{2}}{\theta}}, & x \geqslant 0, \\ 0, & x < 0, \end{array} \right.</equation>于是<equation>\begin{aligned} E (X) &= \int_ {0} ^ {+ \infty} x \cdot \frac {2 x}{\theta} \mathrm {e} ^ {- \frac {x ^ {2}}{\theta}} \mathrm {d} x = \int_ {0} ^ {+ \infty} x \mathrm {d} \left(- \mathrm {e} ^ {- \frac {x ^ {2}}{\theta}}\right) = - x \cdot \mathrm {e} ^ {- \frac {x ^ {2}}{\theta}} \Bigg | _ {0} ^ {+ \infty} + \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {x ^ {2}}{\theta}} \mathrm {d} x \\ &= 0 + \sqrt {\theta} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \left(\frac {x}{\sqrt {\theta}}\right) ^ {2}} \mathrm {d} \left(\frac {x}{\sqrt {\theta}}\right) \stackrel {t = \frac {x}{\sqrt {\theta}}} {=} \sqrt {\theta} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t \\ &= \sqrt {\theta} \cdot \frac {\sqrt {\pi}}{2} = \frac {\sqrt {\pi \theta}}{2}, \quad \text {这 里 利用 了 等 式} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t = \frac {\sqrt {\pi}}{2}. \end{aligned}</equation><equation>\begin{aligned} E \left(X ^ {2}\right) &= \int_ {0} ^ {+ \infty} x ^ {2} \cdot \frac {2 x}{\theta} \mathrm {e} ^ {- \frac {x ^ {2}}{\theta}} \mathrm {d} x = \theta \int_ {0} ^ {+ \infty} \frac {x ^ {2}}{\theta} \mathrm {e} ^ {- \frac {x ^ {2}}{\theta}} \mathrm {d} \left(\frac {x ^ {2}}{\theta}\right) \stackrel {u = \frac {x ^ {2}}{\theta}} {=} \theta \int_ {0} ^ {+ \infty} u \mathrm {e} ^ {- u} \mathrm {d} u \\ &= \theta \left(- u \mathrm {e} ^ {- u} \Big | _ {0} ^ {+ \infty} + \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- u} \mathrm {d} u\right) = \theta . \end{aligned}</equation>（Ⅱ）设<equation>x_{1}, x_{2}, \dots, x_{n}</equation>是来自于样本<equation>X_{1}, X_{2}, \dots, X_{n}</equation>的一个样本值，则似然函数为<equation>L (\theta) = \prod_ {i = 1} ^ {n} f \left(x _ {i}; \theta\right) = \left\{ \begin{array}{l l} \frac {2 ^ {n} x _ {1} x _ {2} \cdots x _ {n}}{\theta^ {n}} \mathrm {e} ^ {- \frac {x _ {1} ^ {2} + x _ {2} ^ {2} + \cdots + x _ {n} ^ {2}}{\theta}}, & x _ {1} \geqslant 0, x _ {2} \geqslant 0, \dots , x _ {n} \geqslant 0, \\ 0, & \text {其 他}. \end{array} \right.</equation>当<equation>x_{1} > 0,x_{2} > 0,\dots ,x_{n} > 0</equation>时，<equation>\ln L (\theta) = \ln \left(2 ^ {n} x _ {1} x _ {2} \dots x _ {n}\right) - n \ln \theta - \frac {x _ {1} ^ {2} + x _ {2} ^ {2} + \dots + x _ {n} ^ {2}}{\theta}.</equation>令<equation>\frac{\mathrm{d}\left[\ln L(\theta)\right]}{\mathrm{d}\theta}=0</equation>即有<equation>-\frac{n}{\theta}+\frac{x_{1}^{2}+x_{2}^{2}+\cdots+x_{n}^{2}}{\theta^{2}}=0</equation>解得<equation>\theta=\frac{x_{1}^{2}+x_{2}^{2}+\cdots+x_{n}^{2}}{n}</equation>，于是<equation>\theta</equation>的最大似然估计量为<equation>\widehat {\theta} _ {n} = \frac {X _ {1} ^ {2} + X _ {2} ^ {2} + \cdots + X _ {n} ^ {2}}{n} = \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} ^ {2}.</equation>（Ⅲ）由<equation>X_{1},X_{2},\dots ,X_{n}</equation>独立同分布知，<equation>X_{1}^{2},X_{2}^{2},\dots ,X_{n}^{2}</equation>独立同分布.又由（I）知，<equation>E\left(X_{i}^{2}\right) = E\left(X^{2}\right) = \theta</equation>，故由辛钦大数定律知，对任意<equation>\varepsilon >0</equation>，有<equation>\lim_{n\to \infty}P\left\{\left|\frac{1}{n}\sum_{i = 1}^{n}X_{i}^{2} - \theta\right| < \varepsilon\right\} = 1</equation>，从而<equation>\lim _ {n \rightarrow \infty} P \left\{\left| \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} ^ {2} - \theta \right| \geqslant \varepsilon \right\} = 0,</equation>即存在实数<equation>a = \theta</equation>，使得对任何<equation>\varepsilon > 0</equation>，都有<equation>\lim P\{ |\widehat{\theta}_n - a | \geqslant \varepsilon \} = 0.</equation>

---

**2020年第23题 | 解答题 | 11分**


设某元件的使用寿命<equation>T</equation>的分布函数为<equation>F (t) = \left\{ \begin{array}{l l} 1 - \mathrm {e} ^ {- \left(\frac {t}{\theta}\right) ^ {m}}, & t \geqslant 0 \\ 0, & \text {其 他} \end{array} \right.</equation>其中<equation>\theta, m</equation>为参数且大于零.

I. 求概率<equation>P\{T > t\}</equation>与<equation>P\{T > s + t \mid T > s\}</equation>，其中<equation>s > 0, t > 0</equation>.

II. 任取 n个这种元件做寿命试验，测得它们的寿命分别为<equation>t_{1}, t_{2}, \dots , t_{n}</equation>，若 m已知，求<equation>\theta</equation>的最大似然估计值<equation>\hat{\theta}.</equation>

**答案:**（I）<equation>P \left\{ T > t \right\} = \mathrm{e}^{-\left(\frac{t}{\theta}\right)^{m}}, P \left\{ T > s + t \mid T > s \right\} = \mathrm{e}^{\frac{s^{m} - (s + t)^{m}}{\theta^{m}}};</equation>（Ⅱ）<equation>\theta</equation>的最大似然估计值为<equation>\hat{\theta}=\sqrt[m]{\frac{1}{n}\sum_{i=1}^{n}t_{i}^{m}}.</equation>

**解析:**（I）由分布函数的定义以及<equation>s > 0,t > 0</equation>可得，<equation>P \left\{T > t \right\} = 1 - P \left\{T \leqslant t \right\} = 1 - F (t) = \mathrm {e} ^ {- \left(\frac {t}{\theta}\right) ^ {n}}.</equation><equation>P \left\{T > s + t \mid T > s \right\} = \frac {P \left\{T > s + t \right\}}{P \left\{T > s \right\}} = \frac {\mathrm {e} ^ {- \left(\frac {s + t}{\theta}\right) ^ {m}}}{\mathrm {e} ^ {- \left(\frac {s}{\theta}\right) ^ {m}}} = \mathrm {e} ^ {\frac {s ^ {m} - \left(s + t\right) ^ {m}}{\theta^ {m}}}.</equation>（Ⅱ）计算概率密度<equation>f ( t ; \theta)</equation><equation>f (t; \theta) = F ^ {\prime} (t; \theta) = \left\{ \begin{array}{l l} - \mathrm {e} ^ {- \left(\frac {t}{\theta}\right) ^ {m}} \cdot (- m) \cdot \left(\frac {t}{\theta}\right) ^ {m - 1} \cdot \frac {1}{\theta}, & t > 0, \\ 0, & \text {其 他} \end{array} = \left\{ \begin{array}{l l} \frac {m t ^ {m - 1}}{\theta^ {m}} \mathrm {e} ^ {- \left(\frac {t}{\theta}\right) ^ {m}}, & t > 0, \\ 0, & \text {其 他}. \end{array} \right. \right.</equation>似然函数<equation>L (\theta) = \prod_ {i = 1} ^ {n} f \left(t _ {i}; \theta\right) = \left\{ \begin{array}{l l} \left(t _ {1} t _ {2} \dots t _ {n}\right) ^ {m - 1} \cdot \left(\frac {m}{\theta^ {m}}\right) ^ {n} \cdot \mathrm {e} ^ {- \frac {1}{\theta^ {m}} \sum_ {i = 1} ^ {n} t _ {i} ^ {m}}, & t _ {i} > 0, i = 1, 2, \dots , n, \\ 0, & \text {其 他}. \end{array} \right.</equation>取对数得<equation>\ln L (\theta) = (m - 1) \ln \left(t _ {1} t _ {2} \dots t _ {n}\right) + n \left(\ln m - m \ln \theta\right) - \frac {1}{\theta^ {m}} \sum_ {i = 1} ^ {n} t _ {i} ^ {m}.</equation>令<equation>\frac{\mathrm{d}[\ln L(\theta)]}{\mathrm{d}\theta} = -\frac{mn}{\theta} + \frac{m}{\theta^{m + 1}}\sum_{i = 1}^{n}t_{i}^{m} = 0</equation>，可得<equation>mn\theta^{m} = m\sum_{i = 1}^{n}t_{i}^{m}</equation>. 从而<equation>\theta^{m} = \frac{1}{n}\sum_{i = 1}^{n}t_{i}^{m},\hat{\theta} = \sqrt[m]{\frac{1}{n}\sum_{i = 1}^{n}t_{i}^{m}}</equation>因此，<equation>\theta</equation>的最大似然估计值为<equation>\hat{\theta} = \sqrt[m]{\frac{1}{n}\sum_{i = 1}^{n}t_{i}^{m}}</equation>

---

**2019年第23题 | 解答题 | 11分**


设总体<equation>X</equation>的概率密度为<equation>f \left(x; \sigma^ {2}\right) = \left\{ \begin{array}{l l} \frac {A}{\sigma} \mathrm {e} ^ {- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}}, & x \geqslant \mu \\ 0, & x < \mu \end{array} \right.</equation>其中<equation>\mu</equation>是已知参数，<equation>\sigma > 0</equation>是未知参数，<equation>A</equation>是常数.<equation>X_{1}, X_{2}, \dots , X_{n}</equation>是来自总体<equation>X</equation>的简单随机样本.

I. 求 A；

II. 求<equation>\sigma^{2}</equation>的最大似然估计量.

**答案:**（ I ）<equation>A=\sqrt{\frac{2}{\pi}};</equation>（ II ）<equation>\sigma^{2}</equation>的最大似然估计量为<equation>\widehat{\sigma^{2}}=\frac{\sum_{i=1}^{n}\left(X_{i}-\mu\right)^{2}}{n}.</equation>

**解析:**解（I）利用<equation>\int_{- \infty}^{+ \infty} f ( x ; \sigma^{2} ) \mathrm{d} x=1</equation>来计算A.<equation>\begin{aligned} \int_ {- \infty} ^ {+ \infty} f (x; \sigma^ {2}) \mathrm {d} x &= \int_ {\mu} ^ {+ \infty} \frac {A}{\sigma} \mathrm {e} ^ {- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}} \mathrm {d} x \underline {{= t = x - \mu}} A \int_ {0} ^ {+ \infty} \frac {1}{\sigma} \mathrm {e} ^ {- \frac {t ^ {2}}{2 \sigma^ {2}}} \mathrm {d} t = A \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {1}{2} \cdot \left(\frac {t}{\sigma}\right) ^ {2}} \mathrm {d} \left(\frac {t}{\sigma}\right) \\ \frac {\frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \mathrm {d} x = 1}{\underline {{}}} A \cdot \frac {\sqrt {2 \pi}}{2} &= 1. \end{aligned}</equation>因此，<equation>A = \frac{2}{\sqrt{2\pi}} = \sqrt{\frac{2}{\pi}}.</equation>（Ⅱ）设<equation>x_{1}, x_{2}, \dots , x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots , X_{n}</equation>的一组样本值，则关于<equation>\sigma^2</equation>的似然函数为<equation>\begin{array}{l} L \left(\sigma^ {2}\right) = \prod_ {i = 1} ^ {n} f \left(x _ {i}; \sigma^ {2}\right) = \left\{ \begin{array}{l l} \prod_ {i = 1} ^ {n} \sqrt {\frac {2}{\pi}} \cdot \frac {1}{\sigma} \cdot \mathrm {e} ^ {- \frac {\left(x _ {i} - \mu\right) ^ {2}}{2 \sigma^ {2}}}, & x _ {1} \geqslant \mu , x _ {2} \geqslant \mu , \dots , x _ {n} \geqslant \mu , \\ 0, & \text {其 他} \end{array} \right. \\ = \left\{ \begin{array}{l l} \left(\frac {2}{\pi}\right) ^ {\frac {n}{2}} \cdot \left(\frac {1}{\sigma^ {2}}\right) ^ {\frac {n}{2}} \cdot \mathrm {e} ^ {- \frac {\sum_ {i = 1} ^ {n} \left(x _ {i} - \mu\right) ^ {2}}{2 \sigma^ {2}}}, & x _ {1} \geqslant \mu , x _ {2} \geqslant \mu , \dots , x _ {n} \geqslant \mu , \\ 0, & \text {其 他}. \end{array} \right. \\ \end{array}</equation>当<equation>x_{1}\geqslant \mu ,x_{2}\geqslant \mu ,\dots ,x_{n}\geqslant \mu</equation>时，<equation>\ln L \left(\sigma^ {2}\right) = \frac {n}{2} \ln \frac {2}{\pi} - \frac {n}{2} \ln \sigma^ {2} - \frac {\sum_ {i = 1} ^ {n} \left(x _ {i} - \mu\right) ^ {2}}{2 \sigma^ {2}}.</equation>令<equation>\frac{\mathrm{d}\left[\ln L\left(\sigma^2\right)\right]}{\mathrm{d}\left(\sigma^2\right)} = 0</equation>，即<equation>-\frac{n}{2}\cdot \frac{1}{\sigma^2} +\frac{\sum_{i=1}^{n}\left(x_{i} - \mu\right)^{2}}{2}\cdot \frac{1}{\sigma^{4}} = 0</equation>，解得<equation>\sigma^2 = \frac{\sum_{i=1}^{n}\left(x_{i} - \mu\right)^{2}}{n}</equation>因此，<equation>\sigma^2</equation>的最大似然估计量为<equation>\widehat {\sigma^ {2}} = \frac {\sum_ {i = 1} ^ {n} \left(X _ {i} - \mu\right) ^ {2}}{n}.</equation>

---

**2018年第23题 | 解答题 | 11分**


设总体<equation>X</equation>的概率密度为<equation>f (x; \sigma) = \frac {1}{2 \sigma} \mathrm {e} ^ {- \frac {| x |}{\sigma}}, - \infty < x < + \infty</equation><equation>\sigma \in (0, + \infty)</equation>为未知参数，<equation>X_{1}, X_{2}, \dots , X_{n}</equation>为来自总体<equation>X</equation>的简单随机样本.记<equation>\sigma</equation>的最大似然估计量为<equation>\hat{\sigma}</equation>.

I. 求<equation>\hat{\sigma}</equation>；

II. 求<equation>E(\hat{\sigma})</equation>和<equation>D(\hat{\sigma})</equation>

**答案:**（I）<equation>\sigma</equation>的最大似然估计量为<equation>\hat{\sigma}=\frac{\sum_{i=1}^{n} \mid X_{i}\mid}{n}；</equation>（Ⅱ）<equation>E(\hat{\sigma})=\sigma,D(\hat{\sigma})=\frac{\sigma^{2}}{n}.</equation>

**解析:**解（I）设<equation>x_{1}, x_{2}, \dots, x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots, X_{n}</equation>的一组样本值. 似然函数为<equation>L (\sigma) = \prod_ {i = 1} ^ {n} f \left(x _ {i}; \sigma\right) = \frac {1}{2 ^ {n} \sigma^ {n}} \mathrm {e} ^ {- \frac {\left| x _ {1} \right| + \left| x _ {2} \right| + \cdots + \left| x _ {n} \right|}{\sigma}}, - \infty < x _ {i} < + \infty , i = 1, 2, \dots , n.</equation>对 L （<equation>\sigma</equation>）取对数，得<equation>\ln L (\sigma) = - \frac {\sum_ {i = 1} ^ {n} \left| x _ {i} \right|}{\sigma} - n \ln (2 \sigma).</equation>令<equation>\frac{\mathrm{d}[\ln L(\sigma)]}{\mathrm{d}\sigma} = \frac{\sum_{i=1}^{n}|x_i|}{\sigma^2} - \frac{n}{\sigma} = 0</equation>，即<equation>\sum_{i=1}^{n}|x_i| - n\sigma = 0.</equation>解得<equation>\sigma = \frac{\sum_{i=1}^{n}|x_i|}{n}.</equation>因此，<equation>\sigma</equation>的最大似然估计量为<equation>\hat {\sigma} = \frac {\sum_ {i = 1} ^ {n} \left| X _ {i} \right|}{n}.</equation>（Ⅱ）由于<equation>X_{1}, X_{2}, \dots , X_{n}</equation>为来自总体X的简单随机样本，故它们相互独立，且与总体X同分布<equation>E \left( X_{i}\right) = E \left( X\right), E \left( \mid X_{i} \mid\right) = E \left( \mid X \mid\right), i = 1, 2, \dots , n.</equation>根据期望的线性性质，<equation>E \left(\hat {\sigma}\right) = E \left(\frac {\sum_ {i = 1} ^ {n} \left| X _ {i} \right|}{n}\right) = \frac {\sum_ {i = 1} ^ {n} E \left(\left| X _ {i} \right|\right)}{n} = \frac {n E \left(\left| X \right|\right)}{n} = E \left(\left| X \right|\right).</equation>根据期望的定义，<equation>\begin{aligned} E (\mid X \mid) &= \int_ {- \infty} ^ {+ \infty} | x | \cdot f (x; \sigma) \mathrm {d} x = \int_ {- \infty} ^ {+ \infty} | x | \cdot \frac {1}{2 \sigma} \mathrm {e} ^ {- \frac {| x |}{\sigma}} \mathrm {d} x = 2 \int_ {0} ^ {+ \infty} \frac {x}{2 \sigma} \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x \\ &= \frac {1}{\sigma} \int_ {0} ^ {+ \infty} x \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x = - \int_ {0} ^ {+ \infty} x \mathrm {d} \left(\mathrm {e} ^ {- \frac {x}{\sigma}}\right) = - \left(x \mathrm {e} ^ {- \frac {x}{\sigma}} \Big | _ {0} ^ {+ \infty} - \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x\right) \\ &= \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x = - \sigma \mathrm {e} ^ {- \frac {x}{\sigma}} \Big | _ {0} ^ {+ \infty} = \sigma . \end{aligned}</equation>因此，<equation>E(\hat{\sigma}) = \sigma.</equation>下面计算<equation>D(\hat{\sigma})</equation>由于<equation>X_{1}, X_{2}, \dots, X_{n}</equation>相互独立，且与总体<equation>X</equation>同分布，故<equation>D(\mid X_{i}\mid) = D(\mid X\mid)</equation>，<equation>i = 1, 2, \dots, n.</equation><equation>D (\hat {\sigma}) = D \left(\frac {\sum_ {i = 1} ^ {n} \left| X _ {i} \right|}{n}\right) = \frac {1}{n ^ {2}} D \left(\sum_ {i = 1} ^ {n} \left| X _ {i} \right|\right) = \frac {1}{n ^ {2}} \cdot n D (\left| X \right|) = \frac {D (\left| X \right|)}{n}.</equation>根据方差的计算公式，<equation>D (| X |) = E \left(| X | ^ {2}\right) - \left[ E \left(| X |\right) \right] ^ {2} = E \left(X ^ {2}\right) - \left[ E \left(| X |\right) \right] ^ {2}.</equation><equation>\begin{aligned} E \left(X ^ {2}\right) &= \int_ {- \infty} ^ {+ \infty} x ^ {2} \cdot f (x; \sigma) \mathrm {d} x = \int_ {- \infty} ^ {+ \infty} x ^ {2} \cdot \frac {1}{2 \sigma} \mathrm {e} ^ {- \frac {| x |}{\sigma}} \mathrm {d} x = \frac {1}{\sigma} \int_ {0} ^ {+ \infty} x ^ {2} \cdot \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x \\ &= - \int_ {0} ^ {+ \infty} x ^ {2} \mathrm {d} \left(\mathrm {e} ^ {- \frac {x}{\sigma}}\right) = - \left(x ^ {2} \mathrm {e} ^ {- \frac {x}{\sigma}} \Big | _ {0} ^ {+ \infty} - 2 \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {x}{\sigma}} \cdot x \mathrm {d} x\right) \\ &= 2 \int_ {0} ^ {+ \infty} x \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x \stackrel {*} {=} 2 \sigma^ {2}. \end{aligned}</equation>于是，<equation>D ( \mid X \mid ) = 2 \sigma^{2} - \sigma^{2} = \sigma^{2}.</equation>因此，<equation>D(\hat{\sigma}) = \frac{D(|X|)}{n} = \frac{\sigma^2}{n}.</equation>

---

**2017年第23题 | 解答题 | 11分**


某工程师为了解一台天平的精度，用该天平对一物体的质量做 n次测量，该物体的质量<equation>\mu</equation>是已知的.设 n次测量结果<equation>X_{1},X_{2},\cdots,X_{n}</equation>相互独立且均服从正态分布<equation>N\left(\mu ,\sigma^{2}\right)</equation>，该工程师记录的是 n次测量的绝对误差<equation>Z_{i}=\left|X_{i}-\mu\right|(i=1,2,\cdots,n).</equation>利用<equation>Z_{1},Z_{2},\cdots,Z_{n}</equation>估计<equation>\sigma.</equation>I. 求<equation>Z_{1}</equation>的概率密度；

II. 利用一阶矩求<equation>\sigma</equation>的矩估计量；

III. 求<equation>\sigma</equation>的最大似然估计量.

**答案:**( I )<equation>f_{Z_{1}}(z)=\left\{\begin{array}{ll}\sqrt{\frac{2}{\pi}}\frac{1}{\sigma}\mathrm{e}^{-\frac{z^{2}}{2\sigma^{2}}},&z\geqslant0,\\ 0,&z<0;\end{array}\right.</equation>( II )<equation>\hat{\sigma}=\sqrt{\frac{\pi}{2}}\bar{Z};</equation>( III )<equation>\hat{\sigma}=\sqrt{\frac{1}{n}\sum_{i=1}^{n}Z_{i}^{2}}.</equation>

**解析:**解（I）由题设知，<equation>X_{1}\sim N(\mu ,\sigma^{2})</equation>，从而<equation>\frac{X_{1}-\mu}{\sigma}\sim N(0,1).</equation>当 z < 0时，<equation>F_{Z_{1}}(z)=0.</equation>当<equation>z\geqslant 0</equation>时，<equation>\begin{array}{l} F _ {Z _ {1}} (z) = P \left\{Z _ {1} \leqslant z \right\} = P \left\{\left| X _ {1} - \mu \right| \leqslant z \right\} \\ = P \left\{\left| \frac {X _ {1} - \mu}{\sigma} \right| \leqslant \frac {z}{\sigma} \right\} = P \left\{- \frac {z}{\sigma} \leqslant \frac {X _ {1} - \mu}{\sigma} \leqslant \frac {z}{\sigma} \right\} \\ = 2 \Phi \left(\frac {z}{\sigma}\right) - 1, \\ \end{array}</equation>其中<equation>\varPhi(x)</equation>为标准正态分布函数.

于是，<equation>Z_{1}</equation>的分布函数为<equation>F_{Z_{1}}(z) = \left\{ \begin{array}{ll} 2\Phi \left(\frac{z}{\sigma}\right) - 1, & z\geqslant 0, \\ 0, & z < 0. \end{array} \right.</equation>因此，<equation>Z_{1}</equation>的概率密度为<equation>f _ {Z _ {1}} (z) = F _ {Z _ {1}} ^ {\prime} (z) = \left\{ \begin{array}{l l} \frac {2}{\sigma} \varphi \left(\frac {z}{\sigma}\right), & z \geqslant 0, \\ 0, & z < 0 \end{array} = \left\{ \begin{array}{l l} \sqrt {\frac {2}{\pi}} \frac {1}{\sigma} \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}}, & z \geqslant 0, \\ 0, & z < 0, \end{array} \right. \right.</equation>其中<equation>\varphi (x)</equation>为标准正态分布的概率密度.

（Ⅱ）由于<equation>\begin{aligned} E \left(Z _ {1}\right) &= \int_ {- \infty} ^ {+ \infty} z f _ {Z _ {1}} (z) \mathrm {d} z = \int_ {0} ^ {+ \infty} z \cdot \sqrt {\frac {2}{\pi}} \frac {1}{\sigma} \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}} \mathrm {d} z = \sqrt {\frac {2}{\pi}} \sigma \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}} \mathrm {d} \left(\frac {z ^ {2}}{2 \sigma^ {2}}\right) \\ &= - \sqrt {\frac {2}{\pi}} \sigma \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}} \Bigg | _ {0} ^ {+ \infty} = \sqrt {\frac {2}{\pi}} \sigma , \end{aligned}</equation>故<equation>\sigma = \sqrt{\frac{\pi}{2}} E\left(Z_{1}\right)</equation>. 用<equation>\overline{Z} = \frac{1}{n}\sum_{i=1}^{n} Z_{i}</equation>代替<equation>E\left(Z_{1}\right)</equation>，得到<equation>\sigma</equation>的矩估计量<equation>\hat {\sigma} = \sqrt {\frac {\pi}{2}} \bar {Z}.</equation>（Ⅲ）设<equation>z_{1}, z_{2}, \dots, z_{n}</equation>是相应于<equation>Z_{1}, Z_{2}, \dots, Z_{n}</equation>的一组样本值，则似然函数为<equation>L (\sigma) = L \left(z _ {1}, z _ {2}, \dots , z _ {n}; \sigma\right) = \prod_ {i = 1} ^ {n} f _ {Z _ {i}} \left(z _ {i}\right) = \left\{ \begin{array}{l l} \left(\frac {2}{\pi}\right) ^ {\frac {n}{2}} \frac {1}{\sigma^ {n}} \mathrm {e} ^ {- \frac {1}{2 \sigma^ {2}} \left(z _ {1} ^ {2} + z _ {2} ^ {2} + \dots + z _ {n} ^ {2}\right)}, & z _ {1} > 0, z _ {2} > 0, \dots , z _ {n} > 0, \\ 0, & \text {其 他}. \end{array} \right.</equation>当<equation>z_{1} > 0, z_{2} > 0, \dots, z_{n} > 0</equation>时，<equation>\ln L (\sigma) = \frac {n}{2} \ln \frac {2}{\pi} - n \ln \sigma - \frac {1}{2 \sigma^ {2}} \left(z _ {1} ^ {2} + z _ {2} ^ {2} + \dots + z _ {n} ^ {2}\right).</equation>令<equation>\frac{\mathrm{d}[\ln L(\sigma)]}{\mathrm{d}\sigma} = 0</equation>，即<equation>-\frac{n}{\sigma} +\frac{1}{\sigma^3}\left(z_1^2 +z_2^2 +\dots +z_n^2\right) = 0</equation>，解得<equation>\sigma = \sqrt{\frac{1}{n}\sum_{i=1}^{n}z_i^2}</equation>.

因此，<equation>\sigma</equation>的最大似然估计量为<equation>\hat {\sigma} = \sqrt {\frac {1}{n} \sum_ {i = 1} ^ {n} Z _ {i} ^ {2}}.</equation>

---

**2015年第23题 | 解答题 | 11分**


设总体<equation>X</equation>的概率密度为<equation>f (x; \theta) = \left\{ \begin{array}{l l} \frac {1}{1 - \theta}, & \theta \leqslant x \leqslant 1 \\ 0, & \text {其 他} \end{array} \right.</equation>其中<equation>\theta</equation>为未知参数.<equation>X_{1},X_{2},\cdots ,X_{n}</equation>为来自该总体的简单随机样本.

I. 求<equation>\theta</equation>的矩估计量;

II. 求<equation>\theta</equation>的最大似然估计量.

**答案:**<equation>\begin{aligned} 2 3) (\mathrm {I}) \hat {\theta} &= 2 \bar {X} - 1; \\ (\mathrm {I I}) \hat {\theta} &= \min _ {1 \leqslant i \leqslant n} X _ {i}. \end{aligned}</equation>

**解析:**（ I ）由于<equation>E (X) = \int_ {- \infty} ^ {+ \infty} x f (x; \theta) \mathrm {d} x = \int_ {\theta} ^ {1} \frac {x}{1 - \theta} \mathrm {d} x = \frac {1 + \theta}{2},</equation>故<equation>\theta = 2 E ( X ) - 1.</equation>用样本均值<equation>\bar{X}=\frac{1}{n}\sum_{i=1}^{n}X_{i}</equation>代替<equation>E ( X )</equation>，可得<equation>\theta</equation>的矩估计量<equation>\hat {\theta} = 2 \bar {X} - 1.</equation>（Ⅱ）设<equation>x_{1}, x_{2}, \dots, x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots, X_{n}</equation>的一组样本值，则似然函数为<equation>L (\theta) = \prod_ {i = 1} ^ {n} f \left(x _ {i}; \theta\right) = \left\{ \begin{array}{l l} \frac {1}{(1 - \theta) ^ {n}}, & \theta \leqslant x _ {1}, x _ {2}, \dots , x _ {n} \leqslant 1, \\ 0, & \text {其 他} \end{array} = \left\{ \begin{array}{l l} \frac {1}{(1 - \theta) ^ {n}}, & \theta \leqslant \min _ {1 \leqslant i \leqslant n} x _ {i}, \\ 0, & \text {其 他}. \end{array} \right. \right.</equation>又由于<equation>\frac{1}{(1-\theta)^{n}}</equation>是关于<equation>\theta</equation>的单调增加函数，故当<equation>\theta=\min_{1\leqslant i\leqslant n}x_{i}</equation>时，<equation>L(\theta)</equation>取值最大因此，<equation>\theta</equation>的最大似然估计量为<equation>\hat {\theta} = \min _ {1 \leqslant i \leqslant n} X _ {i}.</equation>

---

**2013年第23题 | 解答题 | 11分**

23. (本题满分11分)

设总体 X的概率密度为 f(x;<equation>\theta)=\left\{\begin{array}{ll}\frac{\theta^{2}}{x^{3}} \mathrm{e}^{-\frac{\theta}{x}},&x>0,\\ 0,&\mathrm{其他},\end{array} \right.</equation>其中<equation>\theta</equation>为未知参数且大于零.<equation>X_{1},X_{2},\cdots,X_{n}</equation>为来自总体 X的简单随机样本.

I. 求<equation>\theta</equation>的矩估计量;

II. 求<equation>\theta</equation>的最大似然估计量.

**答案:**(23) （ I ）<equation>\hat{\theta}=\overline{X};</equation>(Ⅱ)<equation>\hat{\theta}=\frac{2 n}{\sum_{i=1}^{n}\frac{1}{X_{i}}}.</equation>

**解析:**解（I）由题设知，<equation>\begin{aligned} E (X) &= \int_ {0} ^ {+ \infty} x \cdot \frac {\theta^ {2}}{x ^ {3}} \mathrm {e} ^ {- \frac {\theta}{x}} \mathrm {d} x = \int_ {0} ^ {+ \infty} \frac {\theta^ {2}}{x ^ {2}} \mathrm {e} ^ {- \frac {\theta}{x}} \mathrm {d} x = \int_ {0} ^ {+ \infty} \theta \mathrm {e} ^ {- \frac {\theta}{x}} \mathrm {d} \left(- \frac {\theta}{x}\right) \\ \underline {{\underline {{t}} = - \frac {\theta}{x}}} \int_ {- \infty} ^ {0} \theta \mathrm {e} ^ {t} \mathrm {d} t &= \theta \mathrm {e} ^ {t} \Big | _ {- \infty} ^ {0} = \theta , \end{aligned}</equation>即<equation>\theta = E(X)</equation>. 以<equation>\overline{X} = \frac{1}{n}\sum_{i=1}^{n} X_{i}</equation>代替<equation>E(X)</equation>, 得到<equation>\theta</equation>的矩估计量<equation>\hat{\theta} = \overline{X}</equation>.

（Ⅱ）设<equation>x_{1}, x_{2}, \dots, x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots, X_{n}</equation>的一组样本值，则关于<equation>\theta</equation>的似然函数为<equation>L (\theta) = \prod_ {i = 1} ^ {n} f \left(x _ {i}; \theta\right) = \left\{ \begin{array}{l l} \frac {\theta^ {2 n}}{\left(x _ {1} x _ {2} \cdots x _ {n}\right) ^ {3}} \mathrm {e} ^ {- \theta \left(\frac {1}{x _ {1}} + \frac {1}{x _ {2}} + \cdots + \frac {1}{x _ {n}}\right)}, & x _ {1} > 0, x _ {2} > 0, \dots , x _ {n} > 0, \\ 0, & \text {其 他}. \end{array} \right.</equation>当<equation>x_{1} > 0,x_{2} > 0,\dots ,x_{n} > 0</equation>时，<equation>\ln L (\theta) = 2 n \ln \theta - 3 \ln \left(x _ {1} x _ {2} \dots x _ {n}\right) - \theta \left(\frac {1}{x _ {1}} + \frac {1}{x _ {2}} + \dots + \frac {1}{x _ {n}}\right).</equation>令<equation>\frac{\mathrm{d}[\ln L(\theta)]}{\mathrm{d}\theta} = 0</equation>，即<equation>\frac{2n}{\theta} - \left(\frac{1}{x_1} + \frac{1}{x_2} + \dots + \frac{1}{x_n}\right) = 0</equation>，解得<equation>\theta = \frac{2n}{\frac{1}{x_1} + \frac{1}{x_2} + \dots + \frac{1}{x_n}}.</equation>因此，<equation>\theta</equation>的最大似然估计量为<equation>\hat {\theta} = \frac {2 n}{\frac {1}{X _ {1}} + \frac {1}{X _ {2}} + \cdots + \frac {1}{X _ {n}}} = \frac {2 n}{\sum_ {i = 1} ^ {n} \frac {1}{X _ {i}}}.</equation>

---

**2012年第23题 | 解答题 | 11分**


设随机变量 X与 Y相互独立且分别服从正态分布<equation>N\left(\mu,\sigma^{2}\right)</equation>与<equation>N\left(\mu,2\sigma^{2}\right)</equation>，其中<equation>\sigma</equation>是未知参数且<equation>\sigma >0</equation>记<equation>Z=X-Y.</equation>I. 求 Z的概率密度<equation>f\left(z;\sigma^{2}\right)</equation>；

II. 设<equation>Z_{1},Z_{2},\cdots,Z_{n}</equation>为来自总体 Z的简单随机样本，求<equation>\sigma^{2}</equation>的最大似然估计量<equation>\hat{\sigma}^{2}</equation>；

III. 证明<equation>\hat{\sigma}^{2}</equation>为<equation>\sigma^{2}</equation>的无偏估计量.

**答案:**(23) ( I )<equation>f ( z ; \sigma^{2} )=\frac{1}{\sqrt{6 \pi} \sigma}\mathrm{e}^{-\frac{z^{2}}{6 \sigma^{2}}},-\infty<z<+\infty;</equation>（Ⅱ）<equation>\widehat{\sigma^{2}}=\frac{1}{3n}\sum_{i=1}^{n}Z_{i}^{2};</equation>（Ⅲ）证明略.

**解析:**（I）由于相互独立且服从正态分布的随机变量的线性组合仍服从正态分布，且<equation>E (Z) = E (X) - E (Y) = \mu - \mu = 0,</equation><equation>D (Z) = D (X - Y) = D (X) + D (Y) = \sigma^ {2} + 2 \sigma^ {2} = 3 \sigma^ {2},</equation>故<equation>Z\sim N(0,3\sigma^{2})</equation>，从而Z的概率密度<equation>f \left(z; \sigma^ {2}\right) = \frac {1}{\sqrt {2 \pi} \sqrt {3 \sigma^ {2}}} \mathrm {e} ^ {- \frac {z ^ {2}}{2 \cdot 3 \sigma^ {2}}} = \frac {1}{\sqrt {6 \pi} \sigma} \mathrm {e} ^ {- \frac {z ^ {2}}{6 \sigma^ {2}}}, - \infty < z < + \infty .</equation>（Ⅱ）设<equation>z_{1}, z_{2}, \dots, z_{n}</equation>是来自于样本<equation>Z_{1}, Z_{2}, \dots, Z_{n}</equation>的一个样本值，则似然函数为<equation>L \left(\sigma^ {2}\right) = \prod_ {i = 1} ^ {n} f \left(z _ {i}; \sigma^ {2}\right) = (6 \pi) ^ {- \frac {n}{2}} \cdot \left(\sigma^ {2}\right) ^ {- \frac {n}{2}} \mathrm {e} ^ {- \frac {z _ {1} ^ {2} + z _ {2} ^ {2} + \cdots + z _ {n} ^ {2}}{6 \sigma^ {2}}}.</equation>取对数得<equation>\ln L \left(\sigma^ {2}\right) = - \frac {n}{2} \ln (6 \pi) - \frac {n}{2} \ln \sigma^ {2} - \frac {z _ {1} ^ {2} + z _ {2} ^ {2} + \cdots + z _ {n} ^ {2}}{6 \sigma^ {2}}.</equation>令<equation>\frac{\mathrm{d}\left[\ln L(\sigma^{2})\right]}{\mathrm{d}(\sigma^{2})}=0</equation>即有<equation>-\frac{n}{2\sigma^{2}}+\frac{z_{1}^{2}+z_{2}^{2}+\cdots+z_{n}^{2}}{6(\sigma^{2})^{2}}=0</equation>解得<equation>\sigma^{2}=\frac{z_{1}^{2}+z_{2}^{2}+\cdots+z_{n}^{2}}{3n}.</equation>于是<equation>\sigma^{2}</equation>的最大似然估计量为<equation>\widehat {\sigma^ {2}} = \frac {Z _ {1} ^ {2} + Z _ {2} ^ {2} + \cdots + Z _ {n} ^ {2}}{3 n} = \frac {1}{3 n} \sum_ {i = 1} ^ {n} Z _ {i} ^ {2}.</equation>（Ⅲ）由于<equation>E \left(\widehat {\sigma^ {2}}\right) = E \left(\frac {1}{3 n} \sum_ {i = 1} ^ {n} Z _ {i} ^ {2}\right) = \frac {1}{3} E \left(Z ^ {2}\right) = \frac {1}{3} \left[ D (Z) + \left(E (Z)\right) ^ {2} \right] = \frac {3 \sigma^ {2}}{3} = \sigma^ {2},</equation>故<equation>\widehat{\sigma^2}</equation>为<equation>\sigma^2</equation>的无偏估计量，结论得证.

---

**2011年第23题 | 解答题 | 11分**


设<equation>X_{1}, X_{2}, \dots, X_{n}</equation>为来自正态总体<equation>N\left(\mu_{0},\sigma^{2}\right)</equation>的简单随机样本，其中<equation>\mu_{0}</equation>已知，<equation>\sigma^{2}>0</equation>未知，<equation>\bar{X}</equation>和<equation>S^{2}</equation>分别表示样本均值和样本方差.

I. 求参数<equation>\sigma^{2}</equation>的最大似然估计<equation>\hat{\sigma}^{2}</equation>；

II. 计算<equation>E(\hat{\sigma}^{2})</equation>和<equation>D(\hat{\sigma}^{2})</equation>

**答案:**(23) (I)<equation>\hat{\sigma}^{2} = \frac{1}{n}\sum_{i=1}^{n}\left(X_{i} - \mu_{0}\right)^{2}</equation>;<equation>(\mathrm {I I}) E \left(\widehat {\sigma^ {2}}\right) = \sigma^ {2}, D \left(\widehat {\sigma^ {2}}\right) = \frac {2 \sigma^ {4}}{n}.</equation>

**解析:**解（I）设 X为正态总体，<equation>x_{1}, x_{2}, \dots , x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots , X_{n}</equation>的一个样本值.由<equation>X\sim N(\mu_{0},\sigma^{2})</equation>知，X的概率密度为<equation>f \left(x; \mu_ {0}, \sigma^ {2}\right) = \frac {1}{\sqrt {2 \pi} \sigma} \mathrm {e} ^ {- \frac {\left(x - \mu_ {0}\right) ^ {2}}{2 \sigma^ {2}}},</equation>从而似然函数为<equation>L \left(\sigma^ {2}\right) = \prod_ {i = 1} ^ {n} \frac {1}{\sqrt {2 \pi} \sigma} \mathrm {e} ^ {- \frac {\left(x _ {i} - \mu_ {0}\right) ^ {2}}{2 \sigma^ {2}}} = \left(2 \pi\right) ^ {- \frac {n}{2}} \left(\sigma^ {2}\right) ^ {- \frac {n}{2}} \mathrm {e} ^ {- \frac {1}{2 \sigma^ {2}} \sum_ {i = 1} ^ {n} \left(x _ {i} - \mu_ {0}\right) ^ {2}},</equation>两边取对数得<equation>\ln L \left(\sigma^ {2}\right) = - \frac {n}{2} \ln 2 \pi - \frac {n}{2} \ln \sigma^ {2} - \frac {1}{2 \sigma^ {2}} \sum_ {i = 1} ^ {n} \left(x _ {i} - \mu_ {0}\right) ^ {2}.</equation>令<equation>\frac{\mathrm{d}\left[\ln L\left(\sigma^{2}\right)\right]}{\mathrm{d}\left(\sigma^{2}\right)} = 0</equation>，即有<equation>-\frac{n}{2\sigma^2} +\frac{1}{2\left(\sigma^2\right)^2}\sum_{i=1}^{n}\left(x_{i} - \mu_{0}\right)^{2} = 0</equation>（注意这里是关于<equation>\sigma^2</equation>求导），解得<equation>\sigma^2 = \frac{1}{n}\sum_{i=1}^{n}\left(x_{i} - \mu_{0}\right)^{2}</equation>.于是参数<equation>\sigma^2</equation>的最大似然估计为<equation>\widehat {\sigma^ {2}} = \frac {1}{n} \sum_ {i = 1} ^ {n} \left(X _ {i} - \mu_ {0}\right) ^ {2}.</equation>（Ⅱ）（法一）由于<equation>X_{i}\sim N(\mu_{0},\sigma^{2})</equation>，故<equation>\frac{X_{i} - \mu_{0}}{\sigma}\sim N(0,1),i = 1,2,\dots,n</equation>，从而由（I）知，<equation>\frac {n \widehat {\sigma^ {2}}}{\sigma^ {2}} = \sum_ {i = 1} ^ {n} \frac {\left(X _ {i} - \mu_ {0}\right) ^ {2}}{\sigma^ {2}} \sim \chi^ {2} (n).</equation>于是<equation>E\left(\frac{n\widehat{\sigma}^{2}}{\sigma^{2}}\right)=n,D\left(\frac{n\widehat{\sigma}^{2}}{\sigma^{2}}\right)=2n</equation>，即有<equation>E \left(\widehat {\sigma^ {2}}\right) = \sigma^ {2}, \quad D \left(\widehat {\sigma^ {2}}\right) = \frac {2 \sigma^ {4}}{n}.</equation>（法二）由（I）知，<equation>E \left(\widehat {\sigma^ {2}}\right) = \frac {1}{n} \sum_ {i = 1} ^ {n} E \left[ \left(X _ {i} - \mu_ {0}\right) ^ {2} \right] = E \left[ \left(X - \mu_ {0}\right) ^ {2} \right] \xlongequal {\text {方 差 的 定 义}} D (X) = \sigma^ {2}.</equation>由于<equation>X_{1}, X_{2}, \dots, X_{n}</equation>相互独立，故<equation>(X_{1} - \mu_{0})^{2}, (X_{2} - \mu_{0})^{2}, \dots, (X_{n} - \mu_{0})^{2}</equation>相互独立，从而<equation>D \left(\widehat {\sigma^ {2}}\right) = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} D \left[ \left(X _ {i} - \mu_ {0}\right) ^ {2} \right] = \frac {1}{n} D \left[ \left(X - \mu_ {0}\right) ^ {2} \right].</equation>又<equation>X\sim N(\mu_{0},\sigma^{2})</equation>，故<equation>\frac{X-\mu_{0}}{\sigma}\sim N(0,1)</equation>，从而<equation>\frac{(X-\mu_{0})^{2}}{\sigma^{2}}\sim \chi^{2}(1),D\left[ \frac{(X-\mu_{0})^{2}}{\sigma^{2}}\right] = 2.</equation>于是<equation>D \left(\widehat {\sigma^ {2}}\right) = \frac {1}{n} D \left[ \left(X - \mu_ {0}\right) ^ {2} \right] = \frac {1}{n} \cdot 2 \sigma^ {4} = \frac {2 \sigma^ {4}}{n}.</equation>综上所述，<equation>E(\widehat{\sigma^{2}}) = \sigma^{2}, D(\widehat{\sigma^{2}}) = \frac{2\sigma^{4}}{n}.</equation>

---

**2009年第23题 | 解答题 | 11分**

23. (本题满分11分)

设总体 X的概率密度为<equation>f ( x )=\left\{\begin{array}{ll}\lambda^{2} x \mathrm{e}^{- \lambda x},&x>0,\\0,&\mathrm {其 他},\end{array} \right.</equation>其中参数<equation>\lambda(\lambda>0)</equation>未知，<equation>X_{1},X_{2},\cdots,X_{n}</equation>是来自总体 X的简单随机样本.

I. 求参数<equation>\lambda</equation>的矩估计量;

II. 求参数<equation>\lambda</equation>的最大似然估计量.

**答案:**(23) (I)<equation>\lambda</equation>的矩估计量为<equation>\hat{\lambda} = \frac{2}{\bar{X}}</equation>; (II)<equation>\lambda</equation>的最大似然估计量为<equation>\hat{\lambda} = \frac{2}{\bar{X}}</equation>.

**解析:**（I）由题设知，<equation>\begin{aligned} E (X) &= \int_ {0} ^ {+ \infty} \lambda^ {2} x ^ {2} \mathrm {e} ^ {- \lambda x} \mathrm {d} x \xlongequal {t = \lambda x} \frac {1}{\lambda} \int_ {0} ^ {+ \infty} t ^ {2} \mathrm {e} ^ {- t} \mathrm {d} t \\ &= \frac {1}{\lambda} \left(- \mathrm {e} ^ {- t} \cdot t ^ {2} \Big | _ {0} ^ {+ \infty} + \int_ {0} ^ {+ \infty} 2 t \mathrm {e} ^ {- t} \mathrm {d} t\right) = \frac {2}{\lambda} \int_ {0} ^ {+ \infty} t \mathrm {e} ^ {- t} \mathrm {d} t \\ &= \frac {2}{\lambda} \left(- \mathrm {e} ^ {- t} \cdot t \Big | _ {0} ^ {+ \infty} + \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- t} \mathrm {d} t\right) = \frac {2}{\lambda}. \end{aligned}</equation>于是<equation>\lambda = \frac{2}{E(X)}</equation>，用<equation>\overline{X} = \frac{1}{n}\sum_{i=1}^{n} X_{i}</equation>代替<equation>E(X)</equation>，得到参数<equation>\lambda</equation>的矩估计量为<equation>\hat {\lambda} = \frac {2}{\bar {X}}.</equation>（Ⅱ）设<equation>x_{1}, x_{2}, \dots, x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots, X_{n}</equation>的一个样本值，则似然函数为<equation>L (\lambda)=L \left(x_{1}, x_{2}, \dots, x_{n}; \lambda\right)=\prod_{i=1}^{n} f \left(x_{i}; \lambda\right)=\left\{ \begin{array}{l l} \lambda^{2 n} x_{1} x_{2} \dots x_{n} \mathrm{e}^{- \lambda \left(x_{1}+x_{2}+\dots+x_{n}\right)}, & x_{1}>0, x_{2}>0, \dots, x_{n}>0, \\ 0, & \text{其他}. \end{array} \right.</equation>当<equation>x_{1}>0, x_{2}>0, \dots, x_{n}>0</equation>时，<equation>\ln L (\lambda)=\ln \left(x_{1} x_{2} \dots x_{n}\right)+2 n \ln \lambda-\lambda \left(x_{1}+x_{2}+\dots+x_{n}\right).</equation><equation>\frac{\mathrm{d}[\ln L(\lambda)]}{\mathrm{d}\lambda}=0</equation>即<equation>\frac{2 n}{\lambda}-\left(x_{1}+x_{2}+\dots+x_{n}\right)=0</equation>解得<equation>\lambda=\frac{2 n}{x_{1}+x_{2}+\dots+x_{n}}.</equation>于是参数<equation>\lambda</equation>的最大似然估计量为<equation>\hat {\lambda} = \frac {2 n}{X _ {1} + X _ {2} + \cdots + X _ {n}} = \frac {2 n}{n \bar {X}} = \frac {2}{\bar {X}}.</equation>

---


# 数学三


## 高等数学


### 函数、极限、连续


#### 无穷小量

**2025年第1题 | 选择题 | 5分 | 答案: C**
1. 在<equation>x \rightarrow 0^{+}</equation>时，下列无穷小量中与 x等价的是（    )

A.<equation>\mathrm{e}^{-\sin x}-1</equation>B.<equation>\sqrt{x+1}-\cos x</equation>C.<equation>1-\cos \sqrt{2 x}</equation>D.<equation>1-\frac{\ln(1+x)}{x}</equation>
答案: C
**解析: **解分别记四个选项中的函数为<equation>f_{i}(x)(i = 1,2,3,4)</equation>，计算<equation>\lim_{x\to 0^{+}}\frac{f_{i}(x)}{x}</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {f _ {1} (x)}{x} = \lim _ {x \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {- \sin x} - 1}{x} \xlongequal {\mathrm {e} ^ {- \sin x} - 1 \sim - \sin x} \lim _ {x \rightarrow 0 ^ {+}} \frac {- \sin x}{x} = - 1.</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {f _ {2} (x)}{x} = \lim _ {x \rightarrow 0 ^ {+}} \frac {\sqrt {x + 1} - \cos x}{x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0 ^ {+}} \left(\frac {1}{2 \sqrt {x + 1}} + \sin x\right) = \frac {1}{2}.</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {f _ {3} (x)}{x} = \lim _ {x \rightarrow 0 ^ {+}} \frac {1 - \cos \sqrt {2 x}}{x} \xlongequal {\frac {1 - \cos \sqrt {2 x} \sim \frac {1}{2} (\sqrt {2 x}) ^ {2}}{x}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {1}{2} (\sqrt {2 x}) ^ {2}}{x} = 1.</equation><equation>\begin{aligned} \lim _ {x \rightarrow 0 ^ {+}} \frac {f _ {4} (x)}{x} &= \lim _ {x \rightarrow 0 ^ {+}} \frac {1 - \frac {\ln (1 + x)}{x}}{x} = \lim _ {x \rightarrow 0 ^ {+}} \frac {x - \ln (1 + x)}{x ^ {2}} \\ \frac {\ln (1 + x) = x - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right)}{\hline} \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {1}{2} x ^ {2} + o \left(x ^ {2}\right)}{x ^ {2}} &= \frac {1}{2}. \end{aligned}</equation>由此可得，仅有选项C的函数<equation>f_{3}(x)</equation>满足<equation>\lim_{x\rightarrow 0^{+}}\frac{f_{3}(x)}{x}=1</equation>，其余选项的函数均不符合要求因此，应选C.

---

**2024年第11题 | 填空题 | 5分**
11. 当<equation>x\to 0</equation>时，<equation>\frac {\left(1 + t ^ {2}\right) \sin t ^ {2}}{1 + \cos^ {2} t}</equation><equation>\mathrm{d}t</equation>与<equation>x^{k}</equation>是同阶无穷小，则<equation>k =</equation>___
**答案: **```latex
3
```

**解析:**解记<equation>f ( x )=\int_{0}^{x}\frac{(1+t^{2})\sin t^{2}}{1+\cos^{2}t}\mathrm{d} t</equation>，则<equation>f ( 0 )=0</equation>，且由变限积分的求导公式可得<equation>f^{\prime}(x)=</equation><equation>\frac{(1+x^{2})\sin x^{2}}{1+\cos^{2}x}.</equation>由于<equation>\lim _ {x \rightarrow 0} \frac {f ^ {\prime} (x)}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\left(1 + x ^ {2}\right) \sin x ^ {2}}{\left(1 + \cos^ {2} x\right) x ^ {2}} = \frac {1}{2} \lim _ {x \rightarrow 0} \frac {\sin x ^ {2}}{x ^ {2}} = \frac {1}{2},</equation>故当<equation>x\to0</equation>时，<equation>f^{\prime}(x)</equation>与<equation>x^{2}</equation>是同阶无穷小，且<equation>f^{\prime}(x)\sim \frac{1}{2} x^{2}.</equation>于是，<equation>f (x) = f (x) - f (0) = \int_ {0} ^ {x} f ^ {\prime} (t) \mathrm {d} t \sim \int_ {0} ^ {x} \frac {t ^ {2}}{2} \mathrm {d} t = \frac {t ^ {3}}{6} \Big | _ {0} ^ {x} = \frac {x ^ {3}}{6}. \quad (x \rightarrow 0)</equation>因此，当<equation>x\to 0</equation>时，<equation>f(x)</equation>与<equation>x^{3}</equation>同阶，<equation>k = 3.</equation>

---

**2022年第1题 | 选择题 | 5分 | 答案: C**

1. 若当<equation>x \rightarrow 0</equation>时，<equation>\alpha (x),\beta (x)</equation>是非零无穷小量，则以下四个命题：<equation>\textcircled{1}</equation>若<equation>\alpha (x)\sim \beta (x)</equation>，则<equation>\alpha^{2}(x)\sim \beta^{2}(x);</equation><equation>\textcircled{2}</equation>若<equation>\alpha^{2}(x)\sim \beta^{2}(x)</equation>，则<equation>\alpha (x)\sim \beta (x);</equation><equation>\textcircled{3}</equation>若<equation>\alpha (x)\sim \beta (x)</equation>，则<equation>\alpha (x)-\beta (x)=o(\alpha (x));</equation><equation>\textcircled{4}</equation>若<equation>\alpha (x)-\beta (x)=o(\alpha (x))</equation>，则<equation>\alpha (x)\sim \beta (x).</equation>其中所有真命题的序号是（    ）

A.<equation>\textcircled{1}\textcircled{3}</equation>B.<equation>\textcircled{1}\textcircled{4}</equation>C.<equation>\textcircled{1}\textcircled{3}\textcircled{4}</equation>D.<equation>\textcircled{2}\textcircled{3}\textcircled{4}</equation>

答案: C

**解析:**## 依次分析四个命题.

若<equation>\alpha(x)\sim\beta(x)</equation>，则<equation>\lim_{x\to0}\frac{\alpha(x)}{\beta(x)}=1</equation>，从而<equation>\lim_{x\to0}\frac{\alpha^{2}(x)}{\beta^{2}(x)}=1</equation>，即<equation>\alpha^{2}(x)\sim\beta^{2}(x).</equation>命题<equation>\textcircled{1}</equation>是真命题.

由<equation>\alpha^{2}(x)\sim\beta^{2}(x)</equation>并不能得到<equation>\alpha(x)\sim\beta(x).</equation>考虑<equation>\beta(x)=-\alpha(x)</equation>，则<equation>\lim_{x\to0}\frac{\alpha^{2}(x)}{\beta^{2}(x)}=\lim_{x\to0}\frac{\alpha^{2}(x)}{\alpha^{2}(x)}= 1</equation>，即<equation>\alpha^{2}(x)\sim\beta^{2}(x)</equation>，但<equation>\lim_{x\to0}\frac{\alpha(x)}{\beta(x)}=\lim_{x\to0}\frac{\alpha(x)}{- \alpha(x)}=-1, \alpha(x)</equation>与<equation>\beta(x)</equation>只是同阶但并不等价的无穷小量.

命题<equation>\textcircled{2}</equation>不是真命题.

要说明<equation>\alpha ( x )-\beta ( x )=o( \dot{\alpha} ( x ) )</equation>，只需说明<equation>\lim_{x\to 0}\frac{\alpha ( x )-\beta ( x )}{\alpha ( x )}=0.</equation><equation>\lim _ {x \rightarrow 0} \frac {\alpha (x) - \beta (x)}{\alpha (x)} = 1 - \lim _ {x \rightarrow 0} \frac {\beta (x)}{\alpha (x)} \frac {\alpha (x) \sim \beta (x)}{1 - 1} = 0.</equation>命题<equation>\textcircled{3}</equation>是真命题.

要说明<equation>\alpha (x)\sim \beta (x)</equation>，只需说明<equation>\lim_{x\to 0}\frac{\beta (x)}{\alpha (x)} = 1.</equation><equation>\lim _ {x \rightarrow 0} \frac {\beta (x)}{\alpha (x)} = \lim _ {x \rightarrow 0} \frac {\alpha (x) - [ \alpha (x) - \beta (x) ]}{\alpha (x)} = 1 - \lim _ {x \rightarrow 0} \frac {\alpha (x) - \beta (x)}{\alpha (x)} = 1 - 0 = 1.</equation>命题<equation>\textcircled{4}</equation>是真命题.

综上所述，应选C.

---

**2021年第1题 | 选择题 | 5分 | 答案: C**

1. 当<equation>x \rightarrow 0</equation>时，<equation>\int_{0}^{x^{2}}(\mathrm{e}^{t^{3}}-1)\mathrm{d}t</equation>是<equation>x^{7}</equation>的（    ）

A. 低阶无穷小 B. 等价无穷小

C. 高阶无穷小 D. 同阶但非等价无穷小

答案: C

**解析:**解 计算<equation>\lim_{x\rightarrow 0}\frac{\int_{0}^{x^{2}}(\mathrm{e}^{t^{3}}-1)\mathrm{d}t}{x^{7}}</equation>来比较这两个无穷小量的阶.<equation>\lim _ {x \rightarrow 0} \frac {\int_ {0} ^ {x ^ {2}} \left(\mathrm {e} ^ {t ^ {3}} - 1\right) \mathrm {d} t}{x ^ {7}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\left(\mathrm {e} ^ {x ^ {6}} - 1\right) \cdot 2 x}{7 x ^ {6}} \xlongequal {\text {e} ^ {x ^ {6}} - 1 \sim x ^ {6}} \lim _ {x \rightarrow 0} \frac {x ^ {6} \cdot 2 x}{7 x ^ {6}} = 0.</equation>因此，<equation>\int_{0}^{x^{2}}(\mathrm{e}^{t^{3}}-1)\mathrm{d}t</equation>是<equation>x^{7}</equation>的高阶无穷小.应选C.

---

**2013年第1题 | 选择题 | 4分 | 答案: D**

1. 当<equation>x \to0</equation>时，用“<equation>o(x)</equation>”表示比 x高阶的无穷小量，则下列式子中错误的是（    )

A.<equation>x \cdot o \left( x^{2} \right)=o \left( x^{3} \right)</equation>B.<equation>o(x)\cdot o \left( x^{2} \right)=o \left( x^{3} \right)</equation>C.<equation>o \left( x^{2} \right)+o \left( x^{2} \right)=o \left( x^{2} \right)</equation>D.<equation>o(x)+o \left( x^{2} \right)=o \left( x^{2} \right)</equation>

答案: D

**解析:**由于<equation>\lim _ {x \rightarrow 0} \frac {x \cdot o \left(x ^ {2}\right)}{x ^ {3}} = \lim _ {x \rightarrow 0} \frac {o \left(x ^ {2}\right)}{x ^ {2}} = 0,</equation><equation>\lim _ {x \rightarrow 0} \frac {o (x) \cdot o \left(x ^ {2}\right)}{x ^ {3}} = \lim _ {x \rightarrow 0} \frac {o (x)}{x} \cdot \lim _ {x \rightarrow 0} \frac {o \left(x ^ {2}\right)}{x ^ {2}} = 0,</equation><equation>\lim _ {x \rightarrow 0} \frac {o \left(x ^ {2}\right) + o \left(x ^ {2}\right)}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {o \left(x ^ {2}\right)}{x ^ {2}} + \lim _ {x \rightarrow 0} \frac {o \left(x ^ {2}\right)}{x ^ {2}} = 0 + 0 = 0,</equation>故选项A、B、C均正确.应选D.

对选项D，若令<equation>f ( x )=x^{2}, g ( x )=x^{3}</equation>，则当<equation>x\to 0</equation>时，<equation>x^{2}+x^{3}</equation>形如<equation>o ( x )+o \left( x^{2}\right)</equation>，但<equation>\lim_{x\to 0}\frac{x^{2}+x^{3}}{x^{2}}=1.</equation>因此，当<equation>x\to 0</equation>时，<equation>x^{2}+x^{3}</equation>不是<equation>x^{2}</equation>的高阶无穷小量.

---


#### 函数的连续性与间断点的类型

**2024年第1题 | 选择题 | 5分 | 答案: D**

1. 设函数<equation>f ( x )=\lim_{n \to \infty} \frac{1+x}{1+n x^{2 n}},</equation>则 f(x)，（    ）

A. 在 x=1,x=-1处都连续 B. 在 x=1处连续，在 x=-1处不连续

C. 在 x=1,x=-1处都不连续 D. 在 x=1处不连续，在 x=-1处连续

答案: D

**解析:**解 由于<equation>\lim_{n\to \infty}x^{2n}=\left\{\begin{array}{ll}0,&|x|<1,\\ 1,&|x|=1,\text{故当}|x|<1\text{时},\lim_{n\to \infty}\frac{1+x}{1+nx^{2n}}=\lim_{n\to \infty}\frac{1+x}{1}=1+x,\text{当} \\ +\infty,&|x|>1,\end{array} \right.</equation><equation>|x| = 1</equation>时，<equation>\lim_{n\to \infty}\frac{1 + x}{1 + nx^{2n}} = \lim_{n\to \infty}\frac{1 + x}{1 + n} = 0</equation>，当<equation>|x| > 1</equation>时，<equation>\lim_{n\to \infty}\frac{1 + x}{1 + nx^{2n}} = 0.</equation>于是，<equation>f (x) = \left\{ \begin{array}{l l} 1 + x, & | x | < 1, \\ 0, & | x | \geqslant 1. \end{array} \right.</equation>由于<equation>\lim_{x\to -1^{+}}f(x) = \lim_{x\to -1^{+}}(1 + x) = 0,\lim_{x\to -1^{-}}f(x) = 0 = f(-1),\lim_{x\to -1^{-}}f(x) = \lim_{x\to -1^{+}}(1 + x) = 2,</equation><equation>\lim_{x\to 1^{+}}f(x) = 0</equation>，故<equation>f(x)</equation>在<equation>x = -1</equation>处连续，<equation>x = 1</equation>处不连续.因此，应选D.

---

**2020年第2题 | 选择题 | 4分 | 答案: C**

2. 函数<equation>f(x)=\frac{\mathrm{e}^{\frac{1}{x-1}}\ln|1+x|}{(\mathrm{e}^{x}-1)(x-2)}</equation>的第二类间断点的个数为（    )

A.1 B.2 C.3 D.4

答案: C

**解析:**解从 f(x)的表达式可以看出，<equation>x=-1,x=0,x=1,x=2</equation>为 f(x)的间断点.下面分别计算这些点处的左、右极限.<equation>\lim _ {x \rightarrow - 1} f (x) = \lim _ {x \rightarrow - 1} \frac {\mathrm {e} ^ {\frac {1}{x - 1}} \ln | 1 + x |}{\left(\mathrm {e} ^ {x} - 1\right) (x - 2)} = \frac {\mathrm {e} ^ {- \frac {1}{2}}}{\left(\mathrm {e} ^ {- 1} - 1\right) \cdot (- 3)} \lim _ {x \rightarrow - 1} \ln | 1 + x | = \infty .</equation><equation>\lim _ {x \rightarrow 0} f (x) = \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {\frac {1}{x - 1}} \ln | 1 + x |}{\left(\mathrm {e} ^ {x} - 1\right) (x - 2)} = \frac {\mathrm {e} ^ {- 1}}{- 2} \lim _ {x \rightarrow 0} \frac {\ln | 1 + x |}{\mathrm {e} ^ {x} - 1} \frac {\ln | 1 + x | \sim x}{\mathrm {e} ^ {x} - 1 \sim x} - \frac {1}{2 \mathrm {e}} \lim _ {x \rightarrow 0} \frac {x}{x} = - \frac {1}{2 \mathrm {e}}.</equation><equation>\lim _ {x \rightarrow 1 ^ {+}} f (x) = \lim _ {x \rightarrow 1 ^ {+}} \frac {\mathrm {e} ^ {\frac {1}{x - 1}} \ln | 1 + x |}{\left(\mathrm {e} ^ {x} - 1\right) (x - 2)} = - \frac {\ln 2}{\mathrm {e} - 1} \lim _ {x \rightarrow 1 ^ {+}} \mathrm {e} ^ {\frac {1}{x - 1}} = \infty .</equation><equation>\lim _ {x \rightarrow 2} f (x) = \lim _ {x \rightarrow 2} \frac {\mathrm {e} ^ {\frac {1}{x - 1}} \ln | 1 + x |}{\left(\mathrm {e} ^ {x} - 1\right) (x - 2)} = \frac {\mathrm {e} \ln 3}{\mathrm {e} ^ {2} - 1} \lim _ {x \rightarrow 2} \frac {1}{x - 2} = \infty .</equation>因此，<equation>x=-1,x=1</equation>和 x=2均为 f(x)的无穷间断点，从而也是第二类间断点. f(x)共有3个第二类间断点.应选C.

---

**2017年第1题 | 选择题 | 4分 | 答案: A**

1. 若函数 f(x)<equation>\left\{\begin{array}{l l}{\frac{1-\cos \sqrt{x}}{ax},}&{x>0,}\\ {b,}&{x\leqslant 0}\end{array}\right.</equation>在 x=0处连续，则（   ）

A.<equation>a b=\frac{1}{2}</equation>B.<equation>a b=-\frac{1}{2}</equation>C.<equation>a b=0</equation>D.<equation>a b=2</equation>

答案: A

**解析:**解 f(x)是分段函数.代入 f(x)在<equation>(-\infty, 0]</equation>和（0，<equation>+\infty</equation>）上的表达式，分别计算<equation>\lim_{x\to 0^{-}}f(x),</equation><equation>\lim_{x\to 0^{+}}f(x).</equation><equation>\lim _ {x \rightarrow 0 ^ {-}} f (x) = f (0) = b,</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} f (x) = \lim _ {x \rightarrow 0 ^ {+}} \frac {1 - \cos \sqrt {x}}{a x} \frac {1 - \cos \sqrt {x} \sim \frac {1}{2} (\sqrt {x}) ^ {2}}{\overline {{=}}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {x}{2}}{a x} = \frac {1}{2 a}.</equation>因此，<equation>b=\frac{1}{2a}</equation>即<equation>a b=\frac{1}{2}</equation>应选A.

---

**2013年第2题 | 选择题 | 4分 | 答案: C**

2. 函数<equation>f ( x )=\frac{| x |^{x}-1}{x ( x+1 ) \ln| x |}</equation>的可去间断点的个数为（    ）

A.0 B.1 C.2 D.3

答案: C

**解析:**解 由于 f(x)在 x=-1,0,1处没有定义且在其他点处连续，故 f(x)的间断点为 x=-1,0,1. 由于<equation>\lim _ {x \rightarrow 0} | x | ^ {x} = \lim _ {x \rightarrow 0} \mathrm {e} ^ {x \ln | x |} = \mathrm {e} ^ {\lim _ {x \rightarrow 0} x \ln | x |} = \mathrm {e} ^ {\lim _ {x \rightarrow 0} \frac {\ln | x |}{x ^ {- 1}} \xlongequal {\text {洛 必达}}} \mathrm {e} ^ {\lim _ {x \rightarrow 0} (- x)} = 1,</equation><equation>\lim _ {x \rightarrow 1} | x | ^ {x} = 1, \quad \lim _ {x \rightarrow - 1} | x | ^ {x} = 1,</equation>故<equation>\lim _ {x \rightarrow 0} \frac {\left| x \right| ^ {x} - 1}{x (x + 1) \ln | x |} = \lim _ {x \rightarrow 0} \frac {\left| x \right| ^ {x} - 1}{(x + 1) \ln (1 + \left| x \right| ^ {x} - 1)} = \lim _ {x \rightarrow 0} \frac {\left| x \right| ^ {x} - 1}{(x + 1) \left(\left| x \right| ^ {x} - 1\right)} = \lim _ {x \rightarrow 0} \frac {1}{x + 1} = 1,</equation><equation>\lim _ {x \rightarrow 1} \frac {\left| x \right| ^ {x} - 1}{x (x + 1) \ln | x |} \stackrel {\text {同 上}} {=} \lim _ {x \rightarrow 1} \frac {1}{x + 1} = \frac {1}{2},</equation><equation>\lim _ {x \rightarrow - 1} \frac {\left| x \right| ^ {x} - 1}{x (x + 1) \ln | x |} \stackrel {\text {同 上}} {=} \lim _ {x \rightarrow - 1} \frac {1}{x + 1} = \infty .</equation>因此，<equation>f ( x )</equation>的可去间断点为<equation>x=0,1. f ( x )</equation>共有2个可去间断点.应选C.

---

**2009年第1题 | 选择题 | 4分 | 答案: C**

1. 函数<equation>f(x)=\frac{x-x^{3}}{\sin \pi x}</equation>的可去间断点的个数为（    ）

A.1 B.2 C.3 D.无穷多个

答案: C

**解析:**解 因为当 k为整数时，<equation>\sin k\pi=0</equation>，所以 f(x）在 x=k（k为整数）时无定义，在其余点连续.当<equation>k-k^{3}\neq0</equation>时，即 k≠0，<equation>\pm1</equation>时，<equation>\lim _ {x \rightarrow k} \frac {x - x ^ {3}}{\sin \pi x} = \infty .</equation>x=k为f（x）的无穷间断点.

当<equation>k - k^{3} = 0</equation>时，即<equation>k = 0, \pm 1</equation>时，<equation>\lim_{x\to k}f(x)</equation>为<equation>\frac{0}{0}</equation>型未定式极限，可用洛必达法则求极限.<equation>\lim _ {x \rightarrow 0} \frac {x - x ^ {3}}{\sin \pi x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - 3 x ^ {2}}{\pi \cos \pi x} = \frac {1}{\pi},</equation><equation>\lim _ {x \rightarrow 1} \frac {x - x ^ {3}}{\sin \pi x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 1} \frac {1 - 3 x ^ {2}}{\pi \cos \pi x} = \frac {- 2}{- \pi} = \frac {2}{\pi},</equation><equation>\lim _ {x \rightarrow - 1} \frac {x - x ^ {3}}{\sin \pi x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow - 1} \frac {1 - 3 x ^ {2}}{\pi \cos \pi x} = \frac {- 2}{- \pi} = \frac {2}{\pi}.</equation>因此，<equation>f ( x )</equation>共有3个可去间断点，<equation>x=0</equation>，<equation>\pm 1.</equation>应选C.

---


#### 函数极限的计算

**2023年第11题 | 填空题 | 5分**

<equation>\lim _ {x \rightarrow \infty} x ^ {2} \left(2 - x \sin \frac {1}{x} - \cos \frac {1}{x}\right) = \underline {{}}</equation>

**答案:**# 2 3.

**解析:**考虑<equation>\sin x, \cos x</equation>在 x=0处的泰勒公式.当 x<equation>\to\infty</equation>时，<equation>\frac{1}{x}\to0,</equation><equation>\sin \frac {1}{x} = \frac {1}{x} - \frac {1}{6 x ^ {3}} + o \left(\frac {1}{x ^ {3}}\right),</equation><equation>\cos \frac {1}{x} = 1 - \frac {1}{2 x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right).</equation>于是，<equation>\begin{array}{l} x ^ {2} \left(2 - x \sin \frac {1}{x} - \cos \frac {1}{x}\right) = x ^ {2} \left[ 2 - 1 + \frac {1}{6 x ^ {2}} - 1 + \frac {1}{2 x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right) \right] \\ = x ^ {2} \left[ \frac {2}{3 x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right) \right] = \frac {2}{3} + o (1). \\ \end{array}</equation>因此，<equation>\lim _ {x \rightarrow \infty} x ^ {2} \left(2 - x \sin \frac {1}{x} - \cos \frac {1}{x}\right) = \frac {2}{3}.</equation>

---

**2022年第11题 | 填空题 | 5分**

<equation>1. \lim _ {x \rightarrow 0} \left(\frac {1 + \mathrm {e} ^ {x}}{2}\right) ^ {\cot x} = \underline {{}}</equation>

**解析:**取对数再求极限.<equation>\lim _ {x \rightarrow 0} \left(\frac {1 + \mathrm {e} ^ {x}}{2}\right) ^ {\cot x} = \lim _ {x \rightarrow 0} \mathrm {e} ^ {\cot x \ln \frac {1 + \mathrm {e} ^ {x}}{2}} = \mathrm {e} _ {x \rightarrow 0} ^ {\lim _ {x \rightarrow 0} \cot x \ln \frac {1 + \mathrm {e} ^ {x}}{2}}.</equation>下面计算<equation>\lim_{x\to 0}\cot x\ln \frac{1 + \mathrm{e}^{x}}{2}</equation>.<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \cot x \ln \frac {1 + e ^ {x}}{2} = \lim _ {x \rightarrow 0} \frac {\ln \frac {1 + e ^ {x}}{2}}{\tan x} \xlongequal {\tan x \sim x} \lim _ {x \rightarrow 0} \frac {\ln \left(1 + \frac {e ^ {x} - 1}{2}\right)}{x} \\ \frac {\ln \left(1 + \frac {e ^ {x} - 1}{2}\right) \sim \frac {e ^ {x} - 1}{2}}{\lim _ {x \rightarrow 0} \frac {e ^ {x} - 1}{2 x}} \lim _ {x \rightarrow 0} \frac {x}{2 x} \\ = \frac {1}{2}. \\ \end{array}</equation>因此，原极限<equation>= \mathrm{e}^{\frac{1}{2}} = \sqrt{\mathrm{e}}.</equation>

---

**2020年第1题 | 选择题 | 4分 | 答案: B**

1. 设<equation>\lim_{x\rightarrow a}\frac{f(x)-a}{x-a}=b</equation>，则<equation>\lim_{x\rightarrow a}\frac{\sin f(x)-\sin a}{x-a}=</equation>(    )

A.<equation>b\sin a</equation>B.<equation>b\cos a</equation>C.<equation>b\sin f(a)</equation>D.<equation>b\cos f(a)</equation>

答案: B

**解析:**解 由<equation>\lim_{x\to a}\frac{f(x)-a}{x-a}=b</equation>可得，<equation>\lim_{x\to a}[f(x)-a]=0</equation>，即<equation>\lim_{x\to a}f(x)=a.</equation>对<equation>[ f ( x ) , a ]</equation>或<equation>[ a,f ( x ) ]</equation>上的<equation>\sin z</equation>应用拉格朗日中值定理可得，<equation>\sin f (x) - \sin a = \cos \xi_ {x} [ f (x) - a ],</equation>其中<equation>\xi_{x}</equation>介于<equation>f(x)</equation>与<equation>a</equation>之间. 由于<equation>\lim_{x\to a}f(x) = a</equation>，故<equation>\lim_{x\to a}\xi_x = a.</equation><equation>\lim _ {x \rightarrow a} \frac {\sin f (x) - \sin a}{x - a} = \lim _ {x \rightarrow a} \frac {\cos \xi_ {x} [ f (x) - a ]}{x - a} = \lim _ {x \rightarrow a} \cos \xi_ {x} \cdot \lim _ {x \rightarrow a} \frac {f (x) - a}{x - a} = b \cos a.</equation>因此，应选B.

---

**2017年第15题 | 解答题 | 10分**

15. (本题满分10分)

**答案:**# 2 3.

**解析:**解（法一）令<equation>u=x-t</equation>，则<equation>t=x-u,\mathrm{d}u=-\mathrm{d}t,</equation><equation>\int_ {0} ^ {x} \sqrt {x - t} \mathrm {e} ^ {t} \mathrm {d} t = - \int_ {x} ^ {0} \sqrt {u} \mathrm {e} ^ {x - u} \mathrm {d} u = \mathrm {e} ^ {x} \int_ {0} ^ {x} \sqrt {u} \mathrm {e} ^ {- u} \mathrm {d} u.</equation>于是，<equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {x} \int_ {0} ^ {x} \sqrt {u} \mathrm {e} ^ {- u} \mathrm {d} u}{\sqrt {x ^ {3}}} \xlongequal {\lim _ {x \rightarrow 0 ^ {+}} \mathrm {e} ^ {x} = 1} \lim _ {x \rightarrow 0 ^ {+}} \frac {\int_ {0} ^ {x} \sqrt {u} \mathrm {e} ^ {- u} \mathrm {d} u}{\sqrt {x ^ {3}}} \xlongequal {\text {洛 必 达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sqrt {x} \mathrm {e} ^ {- x}}{\frac {3}{2} \sqrt {x}} = \frac {2}{3}.</equation>因此，原极限<equation>= \frac{2}{3}.</equation>（法二）由于<equation>\mathrm{e}^{t}</equation>和<equation>\sqrt{x-t}</equation>均为关于 t的连续函数，且<equation>\sqrt{x-t}</equation>在[0,x]上不变号，故由积分中值定理可得，存在<equation>\xi_{x}\in[0,x]</equation>，使得<equation>\int_ {0} ^ {x} \sqrt {x - t} \mathrm {e} ^ {t} \mathrm {d} t = \mathrm {e} ^ {\xi_ {x}} \int_ {0} ^ {x} \sqrt {x - t} \mathrm {d} t.</equation>因此，<equation>\begin{aligned} \lim _ {x \rightarrow 0 ^ {+}} \frac {\int_ {0} ^ {x} \sqrt {x - t} \mathrm {e} ^ {t} \mathrm {d} t}{\sqrt {x ^ {3}}} &= \lim _ {x \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {\xi_ {x}} \int_ {0} ^ {x} \sqrt {x - t} \mathrm {d} t}{\sqrt {x ^ {3}}} = \lim _ {\substack {x \rightarrow 0 ^ {+} \\ 0 \leqslant \xi_ {x} \leqslant x}} \mathrm {e} ^ {\xi_ {x}} \cdot \lim _ {x \rightarrow 0 ^ {+}} \frac {- \frac {2}{3} (x - t) ^ {\frac {3}{2}} \Big| _ {0} ^ {x}}{\sqrt {x ^ {3}}} \\ &= 1 \cdot \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {2}{3} x ^ {\frac {3}{2}}}{\sqrt {x ^ {3}}} = \frac {2}{3}. \end{aligned}</equation>

---

**2016年第9题 | 填空题 | 4分**

9. 已知函数 f(x)满足<equation>\lim_{x\rightarrow 0}\frac{\sqrt{1+f(x)\sin 2x}-1}{\mathrm{e}^{3x}-1}=2</equation>，则<equation>\lim_{x\rightarrow 0}f(x)=</equation>___.
