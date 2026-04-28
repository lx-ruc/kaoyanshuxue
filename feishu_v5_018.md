---

**2012年第12题 | 填空题 | 4分**

12. 由曲线<equation>y=\frac{4}{x}</equation>和直线<equation>y=x</equation>及<equation>y=4x</equation>在第一象限中围成的平面图形的面积为 ___

**答案:**## 4ln 2.

**解析:**解 D为由曲线<equation>y=\frac{4}{x}</equation>和直线 y=x及 y=4x在第一象限中围成的平面区域.由二重积分的几何意义知，所求面积为<equation>\iint\limits_{D}\mathrm{d}x\mathrm{d}y.</equation>先求出这三条曲线在第一象限中的交点，分别为（1，4），（2，2）.

(a)

(b)

（法一）如图（a）所示，将区域<equation>D</equation>划分为两个X型区域.<equation>D _ {1} = \left\{(x, y) \mid x \leqslant y \leqslant 4 x, 0 \leqslant x \leqslant 1 \right\}, \quad D _ {2} = \left\{(x, y) \mid x \leqslant y \leqslant \frac {4}{x}, 1 \leqslant x \leqslant 2 \right\}.</equation>因此，<equation>\begin{array}{l} D \text {的 面 积} = \iint_ {D} \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {x} ^ {4 x} \mathrm {d} y + \int_ {1} ^ {2} \mathrm {d} x \int_ {x} ^ {\frac {4}{x}} \mathrm {d} y = \int_ {0} ^ {1} 3 x \mathrm {d} x + \int_ {1} ^ {2} \left(\frac {4}{x} - x\right) \mathrm {d} x \\ = \frac {3}{2} + 4 \ln 2 - \frac {3}{2} = 4 \ln 2. \\ \end{array}</equation>（法二）如图（b）所示，将区域<equation>D</equation>划分为两个Y型区域.<equation>D _ {1} = \left\{(x, y) \mid \frac {y}{4} \leqslant x \leqslant y, 0 \leqslant y \leqslant 2 \right\}, \quad D _ {2} = \left\{(x, y) \mid \frac {y}{4} \leqslant x \leqslant \frac {4}{y}, 2 \leqslant y \leqslant 4 \right\}.</equation>因此，<equation>\begin{array}{l} D \text {的 面 积} = \iint_ {D} \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {2} \mathrm {d} y \int_ {\frac {y}{4}} ^ {y} \mathrm {d} x + \int_ {2} ^ {4} \mathrm {d} y \int_ {\frac {y}{4}} ^ {\frac {4}{y}} \mathrm {d} x = \int_ {0} ^ {2} \frac {3}{4} y \mathrm {d} y + \int_ {2} ^ {4} \left(\frac {4}{y} - \frac {y}{4}\right) \mathrm {d} y \\ = \frac {3}{2} + 4 \ln 2 - \frac {3}{2} = 4 \ln 2. \\ \end{array}</equation>

---

**2011年第19题 | 解答题 | 10分**

19. (本题满分10分)

设函数<equation>f(x)</equation>在区间[0,1]上具有连续导数，<equation>f(0) = 1</equation>，且满足<equation>\iint_ {D _ {t}} f ^ {\prime} (x + y) \mathrm {d} x \mathrm {d} y = \iint_ {D _ {t}} f (t) \mathrm {d} x \mathrm {d} y, \text {其 中} D _ {t} = \{(x, y) \mid 0 \leqslant y \leqslant t - x, 0 \leqslant x \leqslant t \} (0 < t \leqslant 1).</equation>求 f(x)的表达式.

**答案:**<equation>(1 9) f (x) = \frac {4}{(2 - x) ^ {2}}, 0 \leqslant x \leqslant 1.</equation>

**解析:**解<equation>\begin{array}{l} \iint_ {D _ {t}} f ^ {\prime} (x + y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {t} \mathrm {d} x \int_ {0} ^ {t - x} f ^ {\prime} (x + y) \mathrm {d} y \xlongequal {u = x + y} \int_ {0} ^ {t} \mathrm {d} x \int_ {x} ^ {t} f ^ {\prime} (u) \mathrm {d} u \\ = \int_ {0} ^ {t} \left[ f (t) - f (x) \right] \mathrm {d} x = t f (t) - \int_ {0} ^ {t} f (x) \mathrm {d} x. \\ \end{array}</equation>另一方面，由于 f（t）中不包含变量 x,y，从而<equation>\iint_ {D _ {t}} f (t) \mathrm {d} x \mathrm {d} y = f (t) \iint_ {D _ {t}} \mathrm {d} x \mathrm {d} y = \frac {t ^ {2}}{2} f (t),</equation>其中<equation>\frac{t^{2}}{2}</equation>是<equation>D_{t}</equation>的面积，故我们得到一个新的等式，<equation>t f (t) - \int_ {0} ^ {t} f (x) \mathrm {d} x = \frac {t ^ {2}}{2} f (t).</equation>对（1）式两端关于 t求导，得<equation>f ( t )+ t f^{\prime} ( t )-f ( t )= t f ( t )+\frac{t^{2}}{2} f^{\prime} ( t )</equation>，化简得<equation>( 2-t ) f^{\prime} ( t )=2 f ( t ).</equation>这是一个可分离变量的微分方程.解该方程得，<equation>f(t)=\frac{C}{(2-t)^{2}},</equation>0 < t≤1.由 f(x)在[0,1]上连续且<equation>f(0)=1</equation>得，<equation>f (0) = \lim _ {t \rightarrow 0 ^ {+}} \frac {C}{(2 - t) ^ {2}} = \frac {C}{4} = 1.</equation>从而 C=4.

因此，<equation>f ( x ) = \frac { 4 } { ( 2 - x ) ^ { 2 } }</equation><equation>0 \leqslant x \leqslant 1.</equation>

---


### 一元函数积分学

#### 反常积分的计算


**2025年第12题 | 填空题 | 5分**

12. 设<equation>\int_ {1} ^ {+ \infty} \frac {a}{x (2 x + a)} \mathrm {d} x = \ln 2, \mathrm {则} a = \underline {{}}</equation>

**解析:**解 由于<equation>\frac{a}{x(2x+a)}=\frac{1}{x}-\frac{2}{2x+a}</equation>，故<equation>\begin{aligned} \int_ {1} ^ {+ \infty} \frac {a}{x (2 x + a)} \mathrm {d} x &= \int_ {1} ^ {+ \infty} \left(\frac {1}{x} - \frac {2}{2 x + a}\right) \mathrm {d} x = \left(\ln x - \ln | 2 x + a |\right) \Bigg | _ {1} ^ {+ \infty} = \ln \frac {x}{| 2 x + a |} \Bigg | _ {1} ^ {+ \infty} \\ &= \lim _ {x \rightarrow + \infty} \ln \frac {x}{| 2 x + a |} - \ln \frac {1}{| 2 + a |} = \ln \frac {| 2 + a |}{2}. \end{aligned}</equation>由<equation>\int_{1}^{+\infty}\frac{a}{x(2x+a)} \mathrm{d}x=\ln 2</equation>可得<equation>\ln \frac{\mid 2+a\mid}{2}=\ln 2</equation>结合<equation>\ln x</equation>是单调函数可得<equation>\frac{\mid 2+a\mid}{2}=2</equation>解得 a=2或a=-6.

当 a=-6时，<equation>\int_{1}^{+\infty}\frac{a}{x(2x+a)}\mathrm{d}x=\int_{1}^{+\infty}\frac{-3}{x(x-3)}\mathrm{d}x</equation>，此时 x=3为被积函数的瑕点，且<equation>\lim_{x\to 3^{-}}\frac{x-3}{x(x-3)}=\frac{1}{3}</equation>，由无界函数的反常积分的极限审敛法可得<equation>\int_{1}^{3}\frac{1}{x(x-3)}\mathrm{d}x</equation>发散，从而<equation>\int_{1}^{+\infty}\frac{-3}{x(x-3)}\mathrm{d}x</equation>发散.于是，应舍去 a=-6.

当<equation>a = 2</equation>时，被积函数在<equation>(1, +\infty)</equation>上没有瑕点.

因此，a=2.

---

**2024年第12题 | 填空题 | 5分**

<equation>\int_ {2} ^ {+ \infty} \frac {5}{x ^ {4} + 3 x ^ {2} - 4} \mathrm {d} x = \underline {{}}</equation>

**答案:**<equation>\frac {1}{2} \ln 3 - \frac {\pi}{8}</equation>

**解析:**解（法一）注意到<equation>x^{4}+3 x^{2}-4=(x^{2}+4)(x^{2}-1)</equation>，而<equation>(x^{2}+4)-(x^{2}-1)=5</equation>，故<equation>\frac{5}{x^{4}+3 x^{2}-4}=\frac{5}{(x^{2}+4)(x^{2}-1)}=\frac{1}{x^{2}-1}-\frac{1}{x^{2}+4}=\frac{1}{2}\left(\frac{1}{x-1}-\frac{1}{x+1}\right)-\frac{1}{x^{2}+4}.</equation>因此，<equation>\begin{aligned} \int_ {2} ^ {+ \infty} \frac {5}{x ^ {4} + 3 x ^ {2} - 4} d x &= \int_ {2} ^ {+ \infty} \left[ \frac {1}{2} \left(\frac {1}{x - 1} - \frac {1}{x + 1}\right) - \frac {1}{x ^ {2} + 4} \right] d x \\ &= \frac {1}{2} \ln \left. \frac {x - 1}{x + 1} \right| _ {2} ^ {+ \infty} - \frac {1}{2} \int_ {2} ^ {+ \infty} \frac {1}{1 + \left(\frac {x}{2}\right) ^ {2}} d \left(\frac {x}{2}\right) \\ &= - \frac {1}{2} \ln \frac {1}{3} - \frac {1}{2} \arctan \frac {x}{2} \Big | _ {2} ^ {+ \infty} = \frac {1}{2} \ln 3 - \frac {1}{2} \left(\frac {\pi}{2} - \frac {\pi}{4}\right) \\ &= \frac {1}{2} \ln 3 - \frac {\pi}{8}. \end{aligned}</equation>（法二）注意到<equation>x^{4}+3 x^{2}-4=(x^{2}+4)(x+1)(x-1)</equation>，故对<equation>\frac{5}{x^{4}+3 x^{2}-4}</equation>进行部分分式分解设<equation>\frac {5}{x ^ {4} + 3 x ^ {2} - 4} = \frac {A}{x - 1} + \frac {B}{x + 1} + \frac {C x + D}{x ^ {2} + 4}.</equation>通分并整理可得，<equation>\begin{aligned} \frac {5}{x ^ {4} + 3 x ^ {2} - 4} &= \frac {A (x + 1) \left(x ^ {2} + 4\right) + B (x - 1) \left(x ^ {2} + 4\right) + (C x + D) \left(x ^ {2} - 1\right)}{x ^ {4} + 3 x ^ {2} - 4} \\ &= \frac {(A + B + C) x ^ {3} + (A - B + D) x ^ {2} + (4 A + 4 B - C) x + 4 A - 4 B - D}{x ^ {4} + 3 x ^ {2} - 4}. \end{aligned}</equation>比较<equation>x^{3},x^{2},x</equation>的系数以及常数项可得，<equation>[ A + B + C = 0,</equation><equation>A - B + D = 0,</equation><equation>4 A + 4 B - C = 0,</equation><equation>4 A - 4 B - D = 5.</equation>(1) 式与（3）式相加并整理可得<equation>A+B=0</equation>，进一步可得 C=0.将 B=-A代人（2）式与（4）式可得<equation>\left\{\begin{array}{l l}2 A+D=0,\\ 8 A-D=5,\end{array}\right.</equation>解得<equation>\left\{\begin{array}{l l}A=\frac{1}{2},\\ B=-\frac{1}{2},\\ C=0,\\ D=-1. \end{array}\right.</equation>因此，<equation>\frac {5}{x ^ {4} + 3 x ^ {2} - 4} = \frac {1}{2} \left(\frac {1}{x - 1} - \frac {1}{x + 1}\right) - \frac {1}{x ^ {2} + 4}.</equation>其余同法一.

---

**2013年第11题 | 填空题 | 4分**

<equation>\int_ {1} ^ {+ \infty} \frac {\ln x}{(1 + x) ^ {2}} \mathrm {d} x = \underline {{}}</equation>

**解析:**<equation>\begin{aligned} \int_ {1} ^ {+ \infty} \frac {\ln x}{(1 + x) ^ {2}} \mathrm {d} x &= - \int_ {1} ^ {+ \infty} \ln x \mathrm {d} \left(\frac {1}{1 + x}\right) = - \left[ \frac {\ln x}{1 + x} \Big | _ {1} ^ {+ \infty} - \int_ {1} ^ {+ \infty} \frac {1}{x (1 + x)} \mathrm {d} x \right] \\ &= - \lim _ {x \rightarrow + \infty} \frac {\ln x}{1 + x} + \int_ {1} ^ {+ \infty} \left(\frac {1}{x} - \frac {1}{x + 1}\right) \mathrm {d} x \\ \underline {{\text {洛必达}}} - \lim _ {x \rightarrow + \infty} \frac {1}{x} + \ln \frac {x}{x + 1} \Big | _ {1} ^ {+ \infty} \\ &= 0 + \ln 1 - \ln \frac {1}{2} = \ln 2. \end{aligned}</equation>

---


#### 定积分的计算


**2025年第17题 | 解答题 | 10分**

17. 计算<equation>\int_ {0} ^ {1} \frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} \mathrm {d} x.</equation>

**答案:**#<equation>\frac{3\ln 2+\pi}{10}.</equation>

**解析:**解设<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {A}{x + 1} + \frac {B x + C}{x ^ {2} - 2 x + 2}.</equation>通分并整理可得，<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {(A + B) x ^ {2} + (B + C - 2 A) x + 2 A + C}{(x + 1) \left(x ^ {2} - 2 x + 2\right)}.</equation>比较<equation>x^{2}, x</equation>的系数以及常数项可得，<equation>A + B = 0,</equation><equation>\left\{B + C - 2 A = 0, \right.</equation><equation>2 A + C = 1.</equation>由（1）式可得<equation>B=-A</equation>.将<equation>B=-A</equation>代入（2）式可得<equation>C=3A</equation>.将<equation>C=3A</equation>代入（3）式可得<equation>5A=1</equation>，即<equation>A=\frac{1}{5}</equation>.进一步可得<equation>B=-\frac{1}{5},C=\frac{3}{5}.</equation>由此可得，<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {1}{5} \left(\frac {1}{x + 1} - \frac {x - 3}{x ^ {2} - 2 x + 2}\right).</equation>下面分别计算<equation>\int_{0}^{1}\frac{1}{x+1}\mathrm{d}x</equation>与<equation>\int_{0}^{1}\frac{x-3}{x^{2}-2x+2}\mathrm{d}x.</equation><equation>\int_ {0} ^ {1} \frac {1}{x + 1} \mathrm {d} x = \ln (x + 1) \Big | _ {0} ^ {1} = \ln 2.</equation><equation>\begin{aligned} \int_ {0} ^ {1} \frac {x - 3}{x ^ {2} - 2 x + 2} \mathrm {d} x &= \int_ {0} ^ {1} \frac {x - 1}{x ^ {2} - 2 x + 2} \mathrm {d} x - \int_ {0} ^ {1} \frac {2}{x ^ {2} - 2 x + 2} \mathrm {d} x \\ &= \frac {1}{2} \int_ {0} ^ {1} \frac {\mathrm {d} \left(x ^ {2} - 2 x + 2\right)}{x ^ {2} - 2 x + 2} - 2 \int_ {0} ^ {1} \frac {1}{1 + (x - 1) ^ {2}} \mathrm {d} x \\ &= \frac {1}{2} \ln \left(x ^ {2} - 2 x + 2\right) \left| _ {0} ^ {1} - 2 \arctan (x - 1) \right| _ {0} ^ {1} \\ &= - \frac {1}{2} \ln 2 - 2 [ 0 - \arctan (- 1) ] = - \frac {1}{2} \ln 2 - \frac {\pi}{2}. \end{aligned}</equation>因此，<equation>\int_ {0} ^ {1} \frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} \mathrm {d} x = \frac {1}{5} \left[ \ln 2 - \left(- \frac {1}{2} \ln 2 - \frac {\pi}{2}\right) \right] = \frac {3 \ln 2 + \pi}{1 0}.</equation>

---

**2022年第12题 | 填空题 | 5分**

<equation>\int_ {0} ^ {2} \frac {2 x - 4}{x ^ {2} + 2 x + 4} \mathrm {d} x = \underline {{}}</equation>

**答案:**<equation>\ln 3 - \frac {\sqrt {3}}{3} \pi .</equation>

**解析:**解注意到<equation>( x^{2}+2 x+4)^{\prime}=2 x+2</equation>，<equation>\frac{2 x-4}{x^{2}+2 x+4}=\frac{2 x+2}{x^{2}+2 x+4}</equation><equation>-\frac{6}{x^{2}+2 x+4}.</equation>因此，<equation>\begin{aligned} \int_ {0} ^ {2} \frac {2 x - 4}{x ^ {2} + 2 x + 4} d x &= \int_ {0} ^ {2} \frac {2 x + 2}{x ^ {2} + 2 x + 4} d x - 6 \int_ {0} ^ {2} \frac {1}{x ^ {2} + 2 x + 4} d x \\ &= \int_ {0} ^ {2} \frac {\mathrm {d} \left(x ^ {2} + 2 x + 4\right)}{x ^ {2} + 2 x + 4} - 2 \int_ {0} ^ {2} \frac {1}{1 + \left[ \frac {1}{\sqrt {3}} (x + 1) \right] ^ {2}} d x \\ &= \ln \left(x ^ {2} + 2 x + 4\right) \Bigg | _ {0} ^ {2} - 2 \sqrt {3} \int_ {0} ^ {2} \frac {\mathrm {d} \left[ \frac {1}{\sqrt {3}} (x + 1) \right]}{1 + \left[ \frac {1}{\sqrt {3}} (x + 1) \right] ^ {2}} \\ &= \ln 3 - 2 \sqrt {3} \arctan \frac {1}{\sqrt {3}} (x + 1) \Bigg | _ {0} ^ {2} \\ &= \ln 3 - 2 \sqrt {3} \times \left(\frac {\pi}{3} - \frac {\pi}{6}\right) = \ln 3 - \frac {\sqrt {3}}{3} \pi . \end{aligned}</equation>

---

**2021年第12题 | 填空题 | 5分**

<equation>\int_ {\sqrt {5}} ^ {5} \frac {x}{\sqrt {\left| x ^ {2} - 9 \right|}} \mathrm {d} x = \underline {{}}</equation>

**解析:**当<equation>\sqrt{5} < x < 3</equation>时，<equation>x^{2}-9<0</equation>；当 3 < x < 5时，<equation>x^{2}-9>0.</equation><equation>\begin{aligned} \int_ {\sqrt {5}} ^ {5} \frac {x}{\sqrt {| x ^ {2} - 9 |}} \mathrm {d} x &= \int_ {\sqrt {5}} ^ {3} \frac {x}{\sqrt {9 - x ^ {2}}} \mathrm {d} x + \int_ {3} ^ {5} \frac {x}{\sqrt {x ^ {2} - 9}} \mathrm {d} x \\ &= - \frac {1}{2} \int_ {\sqrt {5}} ^ {3} \frac {\mathrm {d} \left(9 - x ^ {2}\right)}{\sqrt {9 - x ^ {2}}} + \frac {1}{2} \int_ {3} ^ {5} \frac {\mathrm {d} \left(x ^ {2} - 9\right)}{\sqrt {x ^ {2} - 9}} \\ &= \left(- \frac {1}{2}\right) \times 2 \times \sqrt {9 - x ^ {2}} \left| _ {\sqrt {5}} ^ {3} + \frac {1}{2} \times 2 \times \sqrt {x ^ {2} - 9} \right| _ {3} ^ {5} \\ &= - (0 - 2) + (4 - 0) = 6. \end{aligned}</equation>

---

**2019年第11题 | 填空题 | 4分**

11. 已知函数<equation>f ( x )=\int_{1}^{x}\sqrt{1+t^{4}}\mathrm{d} t</equation>，则<equation>\int_{0}^{1} x^{2} f ( x ) \mathrm{d} x=</equation>___.

**答案:**<equation>\frac{1-2\sqrt{2}}{18}.</equation>

**解析:**（法一）利用分部积分法.

注意到 f（1）=0.<equation>\begin{aligned} \int_ {0} ^ {1} x ^ {2} f (x) \mathrm {d} x &= \frac {1}{3} \int_ {0} ^ {1} f (x) \mathrm {d} \left(x ^ {3}\right) = \frac {1}{3} \left[ x ^ {3} f (x) \left| _ {0} ^ {1} - \int_ {0} ^ {1} x ^ {3} \cdot f ^ {\prime} (x) \mathrm {d} x \right] = - \frac {1}{3} \int_ {0} ^ {1} x ^ {3} \sqrt {1 + x ^ {4}} \mathrm {d} x \right. \\ &= - \frac {1}{1 2} \int_ {0} ^ {1} \sqrt {1 + x ^ {4}} \mathrm {d} \left(x ^ {4}\right) = - \frac {1}{1 2} \cdot \frac {2}{3} \cdot \left(1 + x ^ {4}\right) ^ {\frac {3}{2}} \Bigg | _ {0} ^ {1} = \frac {1 - 2 \sqrt {2}}{1 8}. \end{aligned}</equation>（法二）交换积分次序.

将 f(x) 代入所求积分.<equation>\int_ {0} ^ {1} x ^ {2} f (x) \mathrm {d} x = \int_ {0} ^ {1} x ^ {2} \left(\int_ {1} ^ {x} \sqrt {1 + t ^ {4}} \mathrm {d} t\right) \mathrm {d} x = \int_ {0} ^ {1} x ^ {2} \mathrm {d} x \int_ {1} ^ {x} \sqrt {1 + t ^ {4}} \mathrm {d} t.</equation>写出该积分对应的二重积分的积分区域 D. 由二次积分的表达式可知，边界曲线为 t=x，t=1以及 x=0，故<equation>D = \{(x, t) \mid x \leqslant t \leqslant 1, 0 \leqslant x \leqslant 1 \}.</equation>如图所示，交换积分次序可得<equation>D = \{(x, t) \mid 0 \leqslant x \leqslant t, 0 \leqslant t \leqslant 1 \}.</equation>因此，<equation>\begin{array}{l} = - \frac {1}{3} \cdot \frac {1}{4} \int_ {0} ^ {1} \sqrt {1 + t ^ {4}} \mathrm {d} \left(t ^ {4}\right) = - \frac {1}{1 2} \cdot \frac {2}{3} \cdot \left(1 + t ^ {4}\right) ^ {\frac {3}{2}} \Bigg | _ {0} ^ {1} = \frac {1 - 2 \sqrt {2}}{1 8}. \\ \end{array}</equation>

---

**2017年第9题 | 填空题 | 4分**

9.<equation>9. \int_ {- \pi} ^ {\pi} \left(\sin^ {3} x + \sqrt {\pi^ {2} - x ^ {2}}\right) \mathrm {d} x = \underline {{}}</equation>

**解析:**由于<equation>[-\pi ,\pi ]</equation>是对称区间，且<equation>\sin^{3}x</equation>是关于x的奇函数，<equation>\sqrt{\pi^{2}-x^{2}}</equation>是关于x的偶函数，故原积分<equation>\frac{\int_{-\pi}^{\pi}\sin^{3}x\mathrm{d}x=0}{\int_{-\pi}^{\pi}\sqrt{\pi^{2}-x^{2}}\mathrm{d}x} \int_{-\pi}^{\pi}\sqrt{\pi^{2}-x^{2}}\mathrm{d}x</equation><equation>\frac{x=\pi\sin t}{2} 2\int_{0}^{\frac{\pi}{2}}\pi\cos t\cdot \pi\cos t\mathrm{d}t=\pi^{2}\int_{0}^{\frac{\pi}{2}}2\cos^{2}t\mathrm{d}t</equation><equation>= \pi^{2}\int_{0}^{\frac{\pi}{2}}(1+\cos 2t)\mathrm{d}t=\pi^{2}\times \left(\frac{\pi}{2}+0\right)=\frac{\pi^{3}}{2}.</equation>

---

**2014年第11题 | 填空题 | 4分**

11. 设<equation>\int_{0}^{a} x \mathrm{e}^{2 x} \mathrm{d} x=\frac{1}{4}</equation>，则 a=___

**解析:**由于<equation>\frac{1}{4}=\int_{0}^{a}x\mathrm{e}^{2x}\mathrm{d}x=\frac{x\mathrm{e}^{2x}}{2}\bigg|_{0}^{a}-\int_{0}^{a}\frac{\mathrm{e}^{2x}}{2}\mathrm{d}x=\frac{a}{2}\mathrm{e}^{2a}-\frac{\mathrm{e}^{2x}}{4}\bigg|_{0}^{a}=\frac{a}{2}\mathrm{e}^{2a}-\frac{\mathrm{e}^{2a}}{4}+\frac{1}{4},</equation>故<equation>\frac{a}{2}\mathrm{e}^{2a}=\frac{\mathrm{e}^{2a}}{4}</equation>因此，<equation>a=\frac{1}{2}.</equation>

---


#### 变限积分


**2024年第2题 | 选择题 | 5分 | 答案: B**

2. 设<equation>I=\int_{a}^{a+k\pi}|\sin x|\mathrm{d}x,k</equation>为整数，则 I的值（    ）

A. 只与 a有关 B. 只与 k有关 C. 与 a,k均有关 D. 与 a,k均无关

答案: B

**解析:**解（法一）由于<equation>|\sin (x + \pi)| = | - \sin x| = |\sin x|</equation>，故<equation>|\sin x|</equation>是周期为<equation>\pi</equation>的周期函数由分析中的结论（2）可知，<equation>I = \int_ {a} ^ {a + k \pi} | \sin x | \mathrm {d} x = k \int_ {0} ^ {\pi} | \sin x | \mathrm {d} x = k \int_ {0} ^ {\pi} \sin x \mathrm {d} x = 2 k.</equation>因此，<equation>I</equation>的值只与k有关，应选B.

（法二）我们先证明：<equation>\int_{a}^{a+k\pi}|\sin x|\mathrm{d}x=\int_{0}^{k\pi}|\sin x|\mathrm{d}x.</equation>记<equation>F ( a )=\int_{a}^{a+k\pi}|\sin x| \mathrm{d} x.</equation>考虑<equation>F^{\prime}(a).</equation><equation>\begin{aligned} F ^ {\prime} (a) &= \left(\int_ {a} ^ {a + k \pi} | \sin x | \mathrm {d} x\right) ^ {\prime} = | \sin (a + k \pi) | - | \sin a | \\ \underline {{\sin (x + k \pi) = (- 1) ^ {k} \sin x}} | (- 1) ^ {k} \sin a | - | \sin a | &= 0. \end{aligned}</equation>于是，<equation>F(a)</equation>是常函数，<equation>F(a)</equation>恒等于<equation>F(0)</equation>，即<equation>\int_{0}^{k\pi}|\sin x|\mathrm{d}x.</equation>由定积分的性质可得，<equation>I = \int_ {0} ^ {k \pi} | \sin x | \mathrm {d} x = \sum_ {i = 0} ^ {k - 1} \int_ {i \pi} ^ {(i + 1) \pi} | \sin x | \mathrm {d} x.</equation>由于<equation>\int_ {i \pi} ^ {(i + 1) \pi} | \sin x | \mathrm {d} x \xlongequal {t = x - i \pi} \int_ {0} ^ {\pi} | \sin (t + i \pi) | \mathrm {d} t = \int_ {0} ^ {\pi} \sin t \mathrm {d} t = 2,</equation>故由（1）式可得<equation>I = \sum_ {i = 0} ^ {k - 1} \int_ {i \pi} ^ {(i + 1) \pi} | \sin x | \mathrm {d} x = 2 k.</equation>因此，<equation>I</equation>的值只与k有关，应选B.

---

**2020年第3题 | 选择题 | 4分 | 答案: A**

3. 设奇函数 f(x)在<equation>(-\infty,+\infty)</equation>上具有连续导数，则（    )

A.<equation>\int_{0}^{x}[\cos f(t)+f^{\prime}(t)]\mathrm{d}t</equation>是奇函数 B.<equation>\int_{0}^{x}[\cos f(t)+f^{\prime}(t)]\mathrm{d}t</equation>是偶函数

C.<equation>\int_{0}^{x}[\cos f^{\prime}(t)+f(t)]\mathrm{d}t</equation>是奇函数 D.<equation>\int_{0}^{x}[\cos f^{\prime}(t)+f(t)]\mathrm{d}t</equation>是偶函数

答案: A

**解析:**解 由于 f(x)是奇函数，故<equation>\cos f(x)</equation>是偶函数，<equation>f^{\prime}(x)</equation>是偶函数，从而<equation>\cos f(x)+f^{\prime}(x)</equation>也是偶函数.<equation>F(x)=\int_{0}^{x}[\cos f(t)+f^{\prime}(t)]\mathrm{d}t</equation>是<equation>\cos f(x)+f^{\prime}(x)</equation>的一个原函数，且 F(0)=0.因此， F(x)是奇函数.应选A.

下面说明其余选项均不正确.

取<equation>f ( x )=x</equation>，则<equation>\cos f ( x )=\cos x,f^{\prime}(x)=1,\cos f^{\prime}(x)=\cos 1.</equation><equation>\int_{0}^{x}[\cos t+1]\mathrm{d} t=\sin x+x</equation>是奇函数，故选项B不正确.<equation>\int_{0}^{x}[\cos 1+t]\mathrm{d} t=\cos 1\cdot x+\frac{x^{2}}{2}</equation>既不是奇函数，也不是偶函数，故选项C、D不正确.

---

**2016年第18题 | 解答题 | 10分**

18. (本题满分10分）

设函数 f(x)连续，且满足<equation>\int_{0}^{x} f(x-t)\mathrm{d} t=\int_{0}^{x}(x-t)f(t)\mathrm{d} t+\mathrm{e}^{-x}-1</equation>求 f(x).

**答案:**<equation>f (x) = - \frac {\mathrm {e} ^ {- x} + \mathrm {e} ^ {x}}{2}.</equation>

**解析:**令 u=x-t，则<equation>\int_ {0} ^ {x} f (x - t) \mathrm {d} t \xlongequal {u = x - t} - \int_ {x} ^ {0} f (u) \mathrm {d} u = \int_ {0} ^ {x} f (u) \mathrm {d} u.</equation>另一方面，<equation>\int_ {0} ^ {x} (x - t) f (t) \mathrm {d} t = x \int_ {0} ^ {x} f (t) \mathrm {d} t - \int_ {0} ^ {x} t f (t) \mathrm {d} t.</equation>于是已知等式化为<equation>\int_ {0} ^ {x} f (u) \mathrm {d} u = x \int_ {0} ^ {x} f (t) \mathrm {d} t - \int_ {0} ^ {x} t f (t) \mathrm {d} t + \mathrm {e} ^ {- x} - 1.</equation>由于 f(x) 连续，故<equation>\int_{0}^{x} f(t)\mathrm{d}t</equation>可导.对上式两端关于 x求导，可得<equation>f (x) = \int_ {0} ^ {x} f (t) \mathrm {d} t + x f (x) - x f (x) - \mathrm {e} ^ {- x},</equation>即<equation>f (x) = \int_ {0} ^ {x} f (t) \mathrm {d} t - \mathrm {e} ^ {- x}.</equation>对（1）式两端关于 x求导，可得<equation>f ^ {\prime} (x) = f (x) + \mathrm {e} ^ {- x},</equation>即<equation>f^{\prime}(x) - f(x) = \mathrm{e}^{-x}</equation>.<equation>\begin{aligned} f (x) &= \mathrm {e} ^ {- \int (- 1) \mathrm {d} x} \left[ \int \mathrm {e} ^ {- x} \cdot \mathrm {e} ^ {\int (- 1) \mathrm {d} x} \mathrm {d} x + C \right] = \mathrm {e} ^ {x} \left(\int \mathrm {e} ^ {- x} \cdot \mathrm {e} ^ {- x} \mathrm {d} x + C\right) \\ &= \mathrm {e} ^ {x} \left(\int \mathrm {e} ^ {- 2 x} \mathrm {d} x + C\right) = \mathrm {e} ^ {x} \left(- \frac {1}{2} \mathrm {e} ^ {- 2 x} + C\right), \end{aligned}</equation>此为一阶非齐次线性微分方程.由求解公式可得，

其中 C为待定常数.

将 x=0代入（1）式可得，<equation>f(0)=-1</equation>.再将 x=0，<equation>f(0)=-1</equation>代入（2）式，可得<equation>-1=-\frac{1}{2}+C</equation>解得 C=-<equation>\frac{1}{2}</equation>.因此，<equation>f (x) = \mathrm {e} ^ {x} \left(- \frac {1}{2} \mathrm {e} ^ {- 2 x} - \frac {1}{2}\right) = - \frac {\mathrm {e} ^ {- x} + \mathrm {e} ^ {x}}{2}.</equation>

---

**2015年第10题 | 填空题 | 4分**

10. 设函数 f(x) 连续，<equation>\varphi(x)=\int_{0}^{x^{2}} x f(t) \mathrm{d} t</equation>. 若<equation>\varphi(1)=1, \varphi^{\prime}(1)=5</equation>，则 f(1) = ___.

**解析:**解 首先，由于在<equation>\int_0^{x^2} xf(t)\mathrm{d}t</equation>中，<equation>x</equation>不是积分变量，故可将<equation>x</equation>作为因子提出放在积分号外，即<equation>\varphi (x) = \int_ {0} ^ {x ^ {2}} x f (t) \mathrm {d} t = x \int_ {0} ^ {x ^ {2}} f (t) \mathrm {d} t.</equation>由求导的乘法法则和变限积分的求导公式可得<equation>\varphi^ {\prime} (x) = \int_ {0} ^ {x ^ {2}} f (t) \mathrm {d} t + x f \left(x ^ {2}\right) \cdot 2 x.</equation>由<equation>\varphi(1)=1</equation>可得<equation>\varphi(1)=\int_{0}^{1} f(t)\mathrm{d} t=1</equation>；由<equation>\varphi^{\prime}(1)=5</equation>可得<equation>\varphi^{\prime}(1)=\int_{0}^{1} f(t)\mathrm{d} t+2f(1)=5.</equation>因此，<equation>f(1)=\frac{\varphi^{\prime}(1)-\varphi(1)}{2}=2.</equation>

---

**2010年第9题 | 填空题 | 4分**

9. 设可导函数<equation>y=y(x)</equation>由方程<equation>\int_{0}^{x+y}\mathrm{e}^{-t^{2}}\mathrm{d}t=\int_{0}^{x}x\sin t^{2}\mathrm{d}t</equation>确定，则<equation>\left.\frac{\mathrm{d}y}{\mathrm{d}x}\right|_{x=0}=</equation>___.

**解析:**解 对方程<equation>\int_{0}^{x+y}\mathrm{e}^{-t^{2}}\mathrm{d}t=\int_{0}^{x}x\sin t^{2}\mathrm{d}t=x\int_{0}^{x}\sin t^{2}\mathrm{d}t</equation>两端关于 x求导得，<equation>\mathrm{e}^{-(x+y)^{2}}\cdot[1+y^{\prime}(x)]=\int_{0}^{x}\sin t^{2}\mathrm{d}t+x\sin x^{2}.</equation>将 x=0代入原方程得<equation>\int_{0}^{y}\mathrm{e}^{-t^{2}}\mathrm{d}t=0</equation>.由于<equation>\mathrm{e}^{-t^{2}}</equation>恒大于零，故 y=0.再将 x=0，y=0代入（1）式可知，<equation>1+y^{\prime}(0)=0</equation>.因此，<equation>\left.\frac{\mathrm{d}y}{\mathrm{d}x}\right|_{x=0}=y^{\prime}(0)=-1.</equation>

---

**2009年第3题 | 选择题 | 4分 | 答案: A**

3. 使不等式<equation>\int_{1}^{x} \frac{\sin t}{t}\mathrm{d}t > \ln x</equation>成立的 x 的范围是（    ）

A. (0,1) B.<equation>\left(1, \frac{\pi}{2}\right)</equation>C.<equation>\left(\frac{\pi}{2}, \pi\right)</equation>D.<equation>(\pi, +\infty)</equation>

答案: A

**解析:**解 令<equation>f ( x )=\int_{1}^{x}\frac{\sin t}{t}\mathrm{d} t-\ln x</equation>，则<equation>f ( 1 )=0. f ( x )</equation>的自然定义域为<equation>x > 0.</equation>计算<equation>f^{\prime}(x)</equation>得，<equation>f ^ {\prime} (x) = \frac {\sin x}{x} - \frac {1}{x} = \frac {\sin x - 1}{x} \leqslant 0,</equation>并且等号仅在<equation>x=2 n \pi+\frac{\pi}{2}</equation>（<equation>n</equation>为正整数）时成立.于是，<equation>f(x)</equation>是（0，<equation>+\infty</equation>）上的单调减少函数.

当 0 < x < 1时，<equation>f ( x ) > f ( 1 ) = 0</equation>；当 x > 1时，<equation>f ( x ) < f ( 1 ) = 0</equation>因此，使得<equation>f ( x ) > 0</equation>即<equation>\int_{1}^{x}\frac{\sin t}{t}\mathrm{d}t-\ln x>0</equation>的 x的范围是(0,1).应选A.

---

**2009年第4题 | 选择题 | 4分 | 答案: D**

4. 设函数 y=f(x)在区间[-1,3]上的图形如图所示，则函数<equation>F ( x )=\int_{0}^{x} f ( t ) \mathrm{d} t</equation>的图形为（    ）

A.

B.

C.

D.

答案: D

**解析:**解（法一）我们可以从<equation>f(x)</equation>出发具体分析<equation>F(x)</equation>的性质.

因为<equation>f ( x )</equation>分段连续，所以由变上限积分函数的性质可知，在<equation>[-1,0)</equation>，（0,2），（2,3]上，均有<equation>F^{\prime}(x)=f(x).</equation><equation>\textcircled{1}</equation>由于 f(x)在[-1,3]上有界且只有两个间断点，故 f(x)可积.又因为<equation>F(x)=\int_{0}^{x} f(t)\mathrm{d}t</equation>所以 F(x)连续.<equation>\textcircled{2}</equation>在<equation>[-1,0)</equation>上，<equation>f ( x ) > 0</equation>，故 F(x) 单调增加；在(0,1)上，<equation>f ( x ) < 0</equation>，故 F(x) 单调减少；在

(1,2)上，<equation>f ( x ) > 0</equation>，故<equation>F ( x )</equation>单调增加；在（2,3]上，<equation>f ( x ) = 0</equation>，故<equation>F ( x )</equation>为常函数.<equation>\textcircled{3} F ( 0 )=\int_{0}^{0} f ( t ) \mathrm{d} t=0.</equation>在<equation>[-1,1]</equation>上，<equation>F ( x )</equation>均小于等于零.<equation>\textcircled{4}</equation><equation>f(1) = 0, x = 1</equation>为<equation>F(x)</equation>的驻点及极小值点.

同时满足以上要求的图形只有选项D.应选D.

（法二）通过图形考察<equation>f(x)</equation>在<equation>[-1,0)</equation>上的性质，可知当<equation>x\in[-1,0)</equation>时，<equation>f(x)\equiv 1</equation>，故<equation>F (- 1) = \int_ {0} ^ {- 1} 1 \mathrm {d} x = - 1, \quad F (0) = \int_ {0} ^ {0} 1 \mathrm {d} x = 0,</equation>从而可排除选项A和选项C.

又由于 f(x)在[-1,3]上有界且只有两个间断点，f(x)在[-1,3]上可积，而 F(x) =<equation>\int_{0}^{x} f(t)\mathrm{d} t</equation>，故 F(x)必连续，从而可以排除选项B.

综上所述，应选D.

---


#### 定积分的应用


**2024年第19题 | 解答题 | 12分**

19. (本题满分12分)

设 t>0，平面有界区域 D由曲线<equation>y=x\mathrm{e}^{-2x}</equation>与直线 x=t,x=2t及 x轴围成，D的面积为 S(t)，求 S(t)的最大值.

**答案:**<equation>\frac {1}{1 6} \ln 2 + \frac {3}{6 4}.</equation>

**解析:**解 由于<equation>x\mathrm{e}^{-2x} > 0</equation>，故区域D的面积<equation>S(t) = \int_{t}^{2t}x\mathrm{e}^{-2x}\mathrm{d}x.</equation>由变限积分的求导公式可得，<equation>S ^ {\prime} (t) = \left(\int_ {t} ^ {2 t} x \mathrm {e} ^ {- 2 x} \mathrm {d} x\right) ^ {\prime} = 2 \cdot 2 t \mathrm {e} ^ {- 4 t} - t \mathrm {e} ^ {- 2 t} = 4 t \mathrm {e} ^ {- 4 t} - t \mathrm {e} ^ {- 2 t} = t \mathrm {e} ^ {- 4 t} \left(4 - \mathrm {e} ^ {2 t}\right).</equation>解<equation>4-\mathrm{e}^{2 t}=0</equation>可得<equation>t=\ln 2</equation>.于是，当<equation>0 < t < \ln 2</equation>时，<equation>S^{\prime}(t)>0,S(t)</equation>单调增加，当<equation>t > \ln 2</equation>时，<equation>S^{\prime}(t)<0,S(t)</equation>单调减少.

因此，<equation>S ( t )</equation>的最大值在<equation>t=\ln 2</equation>时取得，最大值为<equation>S (\ln 2).</equation>下面用两种方法计算<equation>S(\ln 2).</equation>（法一）<equation>\begin{array}{l} S (\ln 2) = \int_ {\ln 2} ^ {2 \ln 2} x \mathrm {e} ^ {- 2 x} \mathrm {d} x = - \frac {1}{2} \int_ {\ln 2} ^ {2 \ln 2} x \mathrm {d} \left(\mathrm {e} ^ {- 2 x}\right) = - \frac {1}{2} \left(x \mathrm {e} ^ {- 2 x} \Big | _ {\ln 2} ^ {2 \ln 2} - \int_ {\ln 2} ^ {2 \ln 2} \mathrm {e} ^ {- 2 x} \mathrm {d} x\right) \\ = - \frac {1}{2} \left(2 \ln 2 \cdot \frac {1}{1 6} - \ln 2 \cdot \frac {1}{4} + \frac {1}{2} \mathrm {e} ^ {- 2 x} \Big | _ {\ln 2} ^ {2 \ln 2}\right) = \frac {\ln 2}{1 6} - \frac {1}{4} \left(\frac {1}{1 6} - \frac {1}{4}\right) \\ = \frac {\ln 2}{1 6} + \frac {3}{6 4}. \\ \end{array}</equation>（法二）也可以计算出<equation>S(t)</equation>的表达式再代入<equation>t = \ln 2</equation>.<equation>\begin{array}{l} S (t) = \int_ {t} ^ {2 t} x \mathrm {e} ^ {- 2 x} \mathrm {d} x = - \frac {1}{2} \int_ {t} ^ {2 t} x \mathrm {d} \left(\mathrm {e} ^ {- 2 x}\right) = - \frac {1}{2} \left(x \mathrm {e} ^ {- 2 x} \Big | _ {t} ^ {2 t} - \int_ {t} ^ {2 t} \mathrm {e} ^ {- 2 x} \mathrm {d} x\right) \\ = - \frac {1}{2} \left(2 t \mathrm {e} ^ {- 4 t} - t \mathrm {e} ^ {- 2 t} + \frac {1}{2} \mathrm {e} ^ {- 2 x} \Big | _ {t} ^ {2 t}\right) = - \frac {1}{2} \left(2 t \mathrm {e} ^ {- 4 t} - t \mathrm {e} ^ {- 2 t} + \frac {1}{2} \mathrm {e} ^ {- 4 t} - \frac {1}{2} \mathrm {e} ^ {- 2 t}\right) \\ = - \frac {1}{2} \left[ \left(2 t + \frac {1}{2}\right) \mathrm {e} ^ {- 4 t} - \left(t + \frac {1}{2}\right) \mathrm {e} ^ {- 2 t} \right]. \\ \end{array}</equation>因此，<equation>S (\ln 2) = - \frac {1}{2} \left[ \left(2 \ln 2 + \frac {1}{2}\right) \cdot \frac {1}{1 6} - \left(\ln 2 + \frac {1}{2}\right) \cdot \frac {1}{4} \right] = \frac {\ln 2}{1 6} + \frac {3}{6 4}.</equation>

---

**2023年第18题 | 解答题 | 12分**

8. (本题满分12分)

已知平面区域<equation>D=\left\{(x,y)\left|0\leqslant y\leqslant \frac{1}{x\sqrt{1+x^{2}}},x\geqslant 1\right.\right\}</equation>I. 求 D的面积;

II. 求 D绕 x轴旋转所成旋转体的体积.

**答案:**( I )<equation>\ln(\sqrt{2}+1)</equation>;

( II )<equation>\pi\left(1-\frac{\pi}{4}\right).</equation>

**解析:**（I）区域 D是由曲线<equation>y=\frac{1}{x\sqrt{1+x^{2}}}</equation>，直线 x=1以及 x轴围成的无界区域，其面积为<equation>\begin{aligned} S &= \int_ {1} ^ {+ \infty} \frac {1}{x \sqrt {1 + x ^ {2}}} \mathrm {d} x \xlongequal {x = \tan t} \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \frac {\mathrm {d} (\tan t)}{\tan t \sqrt {1 + \tan^ {2} t}} = \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \frac {\sec^ {2} t}{\tan t \sec t} \mathrm {d} t \\ &= \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \frac {\mathrm {d} t}{\sin t} = \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \frac {\mathrm {d} (- \cos t)}{1 - \cos^ {2} t} \xlongequal {u = \cos t} \int_ {\frac {\sqrt {2}}{2}} ^ {0} \frac {- \mathrm {d} u}{1 - u ^ {2}} = \frac {1}{2} \int_ {0} ^ {\frac {\sqrt {2}}{2}} \left(\frac {1}{1 - u} + \frac {1}{1 + u}\right) \mathrm {d} u \\ &= \frac {1}{2} \ln \frac {1 + u}{1 - u} \Bigg | _ {0} ^ {\frac {\sqrt {2}}{2}} = \ln (\sqrt {2} + 1). \end{aligned}</equation>（Ⅱ）由旋转体的体积公式可知，区域 D绕 x轴旋转所成旋转体的体积为<equation>\begin{aligned} V &= \int_ {1} ^ {+ \infty} \pi \left(\frac {1}{x \sqrt {1 + x ^ {2}}}\right) ^ {2} \mathrm {d} x = \pi \int_ {1} ^ {+ \infty} \frac {1}{x ^ {2} \left(1 + x ^ {2}\right)} \mathrm {d} x = \pi \int_ {1} ^ {+ \infty} \left(\frac {1}{x ^ {2}} - \frac {1}{1 + x ^ {2}}\right) \mathrm {d} x \\ &= \pi \left(- \frac {1}{x} - \arctan x\right) \Bigg | _ {1} ^ {+ \infty} = \pi \left(1 - \frac {\pi}{4}\right). \end{aligned}</equation>

---

**2021年第13题 | 填空题 | 5分**

13. 设平面区域 D 由曲线<equation>y=\sqrt{x}\sin\pi x(0\leqslant x\leqslant1)</equation>与 x轴围成，则 D绕 x轴旋转所成的旋转体的体积为 ___.

**答案:**##<equation>\frac{\pi}{4}</equation>

**解析:**（法一）根据旋转体的体积公式，<equation>\begin{array}{l} V = \pi \int_ {0} ^ {1} (\sqrt {x} \sin \pi x) ^ {2} \mathrm {d} x = \pi \int_ {0} ^ {1} x \sin^ {2} \pi x \mathrm {d} x \xlongequal {\pi x = t} \frac {1}{\pi} \int_ {0} ^ {\pi} t \sin^ {2} t \mathrm {d} t = \frac {1}{\pi} \cdot \frac {\pi}{2} \int_ {0} ^ {\pi} \sin^ {2} t \mathrm {d} t \\ = \frac {1}{2} \cdot 2 \int_ {0} ^ {\frac {\pi}{2}} \sin^ {2} t \mathrm {d} t = \frac {\pi}{4}. \\ \end{array}</equation>（法二）下面用另一种方法计算<equation>\int_{0}^{\pi} t\sin^{2}t\mathrm{d}t.</equation><equation>\begin{array}{l} \int_ {0} ^ {\pi} t \sin^ {2} t \mathrm {d} t = \int_ {0} ^ {\pi} t \cdot \frac {1 - \cos 2 t}{2} \mathrm {d} t = \frac {1}{2} \int_ {0} ^ {\pi} (t - t \cos 2 t) \mathrm {d} t = \frac {1}{2} \left(\frac {t ^ {2}}{2} \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} t \cos 2 t \mathrm {d} t\right) \\ = \frac {1}{2} \left[ \frac {\pi^ {2}}{2} - \frac {1}{2} \int_ {0} ^ {\pi} t \mathrm {d} (\sin 2 t) \right] = \frac {\pi^ {2}}{4} - \frac {1}{4} \left(t \sin 2 t \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} \sin 2 t \mathrm {d} t\right) \\ = \frac {\pi^ {2}}{4} - \frac {1}{4} \left(0 + \frac {\cos 2 t}{2} \Big | _ {0} ^ {\pi}\right) = \frac {\pi^ {2}}{4}. \\ \end{array}</equation>

---

**2020年第12题 | 填空题 | 4分**

12. 设平面区域<equation>D=\left\{(x,y)\left| \frac{x}{2}\leqslant y\leqslant \frac{1}{1+x^{2}},0\leqslant x\leqslant 1\right. \right\}</equation>，则 D绕 y轴旋转所成的旋转体的体积为 ___.

**答案:**<equation>\pi \ln 2 - \frac {\pi}{3}.</equation>

**解析:**解 由已知条件可知，区域 D由曲线<equation>y=\frac{1}{1+x^{2}},y=\frac{x}{2},x=0,x=1</equation>围成，其绕 y轴旋转一周所得旋转体的体积可看作两个旋转体的体积之差.

由旋转体的体积公式可得，所求旋转体的体积<equation>\begin{array}{l} V = 2 \pi \int_ {0} ^ {1} x \left(\frac {1}{1 + x ^ {2}} - \frac {x}{2}\right) \mathrm {d} x = 2 \pi \int_ {0} ^ {1} \left(\frac {x}{1 + x ^ {2}} - \frac {x ^ {2}}{2}\right) \mathrm {d} x \\ = 2 \pi \left[ \frac {1}{2} \ln \left(1 + x ^ {2}\right) - \frac {x ^ {3}}{6} \right] \Bigg | _ {0} ^ {1} = \pi \ln 2 - \frac {\pi}{3}. \\ \end{array}</equation>

---

**2019年第18题 | 解答题 | 10分**

18. (本题满分10分)

求曲线<equation>y=\mathrm{e}^{-x}\sin x(x\geqslant 0)</equation>与x轴之间图形的面积.

**答案:**<equation>\frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}.</equation>

**解析:**如图所示，曲线<equation>y=\mathrm{e}^{-x}\sin x(x\geqslant 0)</equation>与 x轴有无穷多个交点，<equation>x=n\pi</equation>（n为非负整数）均为曲线与 x轴的交点. 因此，该曲线与 x轴围成的平面图形在 x轴上方与 x轴下方均有无穷多部分. 计算面积时，应分别计算该平面图形位于 x轴上方部分的面积与位于 x轴下方部分的面积，再求级数和.

解（法一）注意到<equation>\mathrm{e}^{-x}</equation>恒大于零.根据定积分的几何意义，曲线位于（<equation>k\pi</equation>，<equation>( k+1)\pi</equation>）的部分与 x轴之间的图形面积等于<equation>\int_{k\pi}^{(k+1)\pi} \mathrm{e}^{-x}|\sin x|\mathrm{d}x.</equation>计算<equation>S_{n}。</equation><equation>\begin{array}{l} S _ {n} = \sum_ {k = 0} ^ {n - 1} \int_ {k \pi} ^ {(k + 1) \pi} \mathrm {e} ^ {- x} | \sin x | \mathrm {d} x \underline {{= x - k \pi}} \sum_ {k = 0} ^ {n - 1} \int_ {0} ^ {\pi} \mathrm {e} ^ {- (t + k \pi)} | \sin (t + k \pi) | \mathrm {d} t \\ = \sum_ {k = 0} ^ {n - 1} \mathrm {e} ^ {- k \pi} \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t. \\ \end{array}</equation>下面计算<equation>\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t &= - \int_ {0} ^ {\pi} \sin t \mathrm {d} \left(\mathrm {e} ^ {- t}\right) = - \left(\sin t \mathrm {e} ^ {- t} \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \cos t \mathrm {d} t\right) \\ &= \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \cos t \mathrm {d} t = - \int_ {0} ^ {\pi} \cos t \mathrm {d} \left(\mathrm {e} ^ {- t}\right) \\ &= - \cos t \mathrm {e} ^ {- t} \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t \\ &= \mathrm {e} ^ {- \pi} + 1 - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t. \end{aligned}</equation>由上式可得<equation>2\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t=\mathrm{e}^{-\pi}+1</equation>，于是<equation>\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t=\frac{1}{2}\left(\mathrm{e}^{-\pi}+1\right).</equation><equation>S = \lim _ {n \rightarrow \infty} S _ {n} = \frac {1}{2} \left(\mathrm {e} ^ {- \pi} + 1\right) \lim _ {n \rightarrow \infty} \frac {1 - \mathrm {e} ^ {- n \pi}}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} \cdot \frac {\mathrm {e} ^ {- \pi} + 1}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}.</equation>（法二）注意到<equation>\mathrm{e}^{-x}</equation>恒大于零.当<equation>x\in(2n\pi,(2n+1)\pi)</equation>时，<equation>\sin x > 0</equation>；当<equation>x\in((2n+1)\pi,</equation><equation>(2n+2)\pi)</equation>时，<equation>\sin x < 0</equation>因此，根据定积分的几何意义，曲线位于<equation>(2n\pi, (2n+1)\pi)</equation>的部分与x轴之间的图形面积等于<equation>\int_{2n\pi}^{(2n+1)\pi} \mathrm{e}^{-x}\sin x\mathrm{d}x</equation>；曲线位于<equation>((2n+1)\pi, (2n+2)\pi)</equation>的部分与x轴之间的图形面积等于<equation>-\int_{(2n+1)\pi}^{(2n+2)\pi} \mathrm{e}^{-x}\sin x\mathrm{d}x.</equation>记所求面积为 S，则<equation>S = \sum_ {n = 0} ^ {\infty} \int_ {2 n \pi} ^ {(2 n + 1) \pi} \mathrm {e} ^ {- x} \sin x \mathrm {d} x - \sum_ {n = 0} ^ {\infty} \int_ {(2 n + 1) \pi} ^ {(2 n + 2) \pi} \mathrm {e} ^ {- x} \sin x \mathrm {d} x.</equation>下面计算<equation>\int\mathrm{e}^{-x}\sin x\mathrm{d}x.</equation><equation>\begin{aligned} \int \mathrm {e} ^ {- x} \sin x \mathrm {d} x &= - \int \sin x \mathrm {d} \left(\mathrm {e} ^ {- x}\right) = - \left(\sin x \mathrm {e} ^ {- x} - \int \mathrm {e} ^ {- x} \cos x \mathrm {d} x\right) \\ &= - \sin x \mathrm {e} ^ {- x} + \int \mathrm {e} ^ {- x} \cos x \mathrm {d} x = - \sin x \mathrm {e} ^ {- x} - \int \cos x \mathrm {d} \left(\mathrm {e} ^ {- x}\right) \\ &= - \sin x \mathrm {e} ^ {- x} - \left(\cos x \mathrm {e} ^ {- x} + \int \mathrm {e} ^ {- x} \sin x \mathrm {d} x\right). \end{aligned}</equation>由上式可得<equation>2\int \mathrm{e}^{-x}\sin x\mathrm{d}x = -\mathrm{e}^{-x}(\sin x + \cos x) - C</equation>，于是<equation>\int \mathrm {e} ^ {- x} \sin x \mathrm {d} x = - \frac {1}{2} \left[ \mathrm {e} ^ {- x} (\sin x + \cos x) + C \right],</equation>其中 C为任意常数.

因此，<equation>\begin{array}{l} S = \sum_ {n = 0} ^ {\infty} \left[ - \frac {1}{2} \mathrm {e} ^ {- x} (\sin x + \cos x) \right] \left| _ {2 n \pi} ^ {(2 n + 1) \pi} + \sum_ {n = 0} ^ {\infty} \left[ \frac {1}{2} \mathrm {e} ^ {- x} (\sin x + \cos x) \right] \right| _ {(2 n + 1) \pi} ^ {(2 n + 2) \pi} \\ = \frac {1}{2} \sum_ {n = 0} ^ {\infty} \left[ \mathrm {e} ^ {- (2 n + 1) \pi} + \mathrm {e} ^ {- 2 n \pi} \right] + \frac {1}{2} \sum_ {n = 0} ^ {\infty} \left[ \mathrm {e} ^ {- (2 n + 2) \pi} + \mathrm {e} ^ {- (2 n + 1) \pi} \right] \\ = \frac {1}{2} \left[ \sum_ {n = 0} ^ {\infty} \mathrm {e} ^ {- 2 n \pi} + 2 \sum_ {n = 0} ^ {\infty} \mathrm {e} ^ {- (2 n + 1) \pi} + \sum_ {n = 1} ^ {\infty} \mathrm {e} ^ {- 2 n \pi} \right] \\ = \frac {1}{2} \left(\frac {1}{1 - \mathrm {e} ^ {- 2 \pi}} + \frac {2 \mathrm {e} ^ {- \pi}}{1 - \mathrm {e} ^ {- 2 \pi}} + \frac {\mathrm {e} ^ {- 2 \pi}}{1 - \mathrm {e} ^ {- 2 \pi}}\right) = \frac {1}{2} \cdot \frac {\left(1 + \mathrm {e} ^ {- \pi}\right) ^ {2}}{\left(1 + \mathrm {e} ^ {- \pi}\right) \left(1 - \mathrm {e} ^ {- \pi}\right)} \\ = \frac {1}{2} \cdot \frac {1 + \mathrm {e} ^ {- \pi}}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}. \\ \end{array}</equation>

---

**2013年第16题 | 解答题 | 10分**

16. (本题满分10分)

设 D是由曲线<equation>y=x^{\frac{1}{3}}</equation>，直线 x=a（a>0）及 x轴所围成的平面图形，<equation>V_{x}</equation>和<equation>V_{y}</equation>分别是 D绕 x轴，y轴旋转一周所得旋转体的体积.若<equation>V_{y}=1 0 V_{x}</equation>，求 a的值.

**答案:**(16)<equation>a=7\sqrt{7}.</equation>

**解析:**解（法一）<equation>D</equation>绕<equation>x</equation>轴旋转所得的旋转体的体积<equation>V_{x}</equation>为<equation>V _ {x} = \pi \int_ {0} ^ {a} \left(x ^ {\frac {1}{3}}\right) ^ {2} \mathrm {d} x = \frac {3 \pi}{5} x ^ {\frac {5}{3}} \Bigg | _ {0} ^ {a} = \frac {3 \pi}{5} a ^ {\frac {5}{3}}.</equation><equation>D</equation>绕<equation>y</equation>轴旋转所得旋转体的体积<equation>V_{y}</equation>为<equation>V _ {y} = 2 \pi \int_ {0} ^ {a} x \cdot x ^ {\frac {1}{3}} \mathrm {d} x = 2 \pi \cdot \frac {3}{7} a ^ {\frac {7}{3}} = \frac {6 \pi}{7} a ^ {\frac {7}{3}}.</equation>由于<equation>V_{y}=1 0 V_{x}</equation>，故<equation>\frac{6\pi}{7} a^{\frac{7}{3}}=1 0\cdot \frac{3\pi}{5} a^{\frac{5}{3}}.</equation>整理得<equation>a ^ {\frac {5}{3}} \left(6 \pi - \frac {6 \pi}{7} a ^ {\frac {2}{3}}\right) = 0.</equation>因此，<equation>a = 0</equation>或<equation>a^{\frac{2}{3}} = 7.</equation>由题设知，<equation>a > 0</equation>，故<equation>a^{\frac{2}{3}} = 7</equation>，即<equation>a = 7\sqrt{7}.</equation>（法二）<equation>D</equation>绕<equation>y</equation>轴旋转所得旋转体的体积<equation>V_{y}</equation>为底面半径为<equation>a</equation>，高为<equation>a^{\frac{1}{3}}</equation>的圆柱体体积减去<equation>D^{\prime}</equation>（如图，由曲线<equation>y = x^{\frac{1}{3}}</equation>，直线<equation>y = a^{\frac{1}{3}}</equation>与<equation>y</equation>轴围成）绕<equation>y</equation>轴旋转所得旋转体的体积<equation>V_{y}^{\prime}</equation>圆柱体的体积<equation>V = \pi a^{2}\cdot a^{\frac{1}{3}} = \pi a^{\frac{7}{3}}.</equation><equation>V _ {y} ^ {\prime} = \pi \int_ {0} ^ {a ^ {\frac {1}{3}}} \left(y ^ {3}\right) ^ {2} \mathrm {d} y = \frac {\pi}{7} y ^ {7} \left| _ {0} ^ {a ^ {\frac {1}{3}}} = \frac {\pi}{7} a ^ {\frac {7}{3}}. \right.</equation>因此，<equation>V_{y} = \pi a^{\frac{7}{3}} - \frac{\pi}{7} a^{\frac{7}{3}} = \frac{6\pi}{7} a^{\frac{7}{3}}.</equation>其余同法一.

---

**2011年第12题 | 填空题 | 4分**

12. 曲线<equation>y=\sqrt{x^{2}-1}</equation>, 直线<equation>x=2</equation>及<equation>x</equation>轴所围的平面图形绕<equation>x</equation>轴旋转所成的旋转体的体积为 ___.

**解析:**解如图所示，联立方程<equation>\left\{\begin{array}{l l}y=\sqrt{x^{2}-1}\\ x=2,\end{array}\right.</equation>可解得曲线<equation>y=\sqrt{x^{2}-1}</equation>与直线<equation>x=2</equation>的交点为（2，<equation>\sqrt{3}</equation>）由旋转体的体积公式知所求体积为<equation>V = \pi \int_ {1} ^ {2} y ^ {2} (x) \mathrm {d} x = \pi \int_ {1} ^ {2} \left(x ^ {2} - 1\right) \mathrm {d} x = \pi \left(\frac {x ^ {3}}{3} - x\right) \Big | _ {1} ^ {2} = \frac {4}{3} \pi .</equation>

---

**2010年第10题 | 填空题 | 4分**

10. 设位于曲线<equation>y=\frac{1}{\sqrt{x(1+\ln^{2}x)}}</equation>（<equation>\mathrm{e}\leqslant x<+\infty</equation>）下方，x轴上方的无界区域为 G，则 G绕 x轴旋转一周所得空间区域的体积为 ___

**答案:**#<equation>\frac{\pi^{2}}{4}.</equation>

**解析:**解 由曲线表达式可知，<equation>y</equation>是关于<equation>x</equation>的单调减少函数且<equation>\lim_{x\to +\infty}y(x) = 0.</equation>由旋转体的体积公式知G绕<equation>x</equation>轴旋转一周所得空间区域的体积<equation>\begin{array}{l} V = \pi \int_ {\mathrm {e}} ^ {+ \infty} \left[ \frac {1}{\sqrt {x \left(1 + \ln^ {2} x\right)}} \right] ^ {2} \mathrm {d} x = \pi \int_ {\mathrm {e}} ^ {+ \infty} \frac {1}{x \left(1 + \ln^ {2} x\right)} \mathrm {d} x \\ = \pi \int_ {\mathrm {e}} ^ {+ \infty} \frac {\mathrm {d} (\ln x)}{1 + \ln^ {2} x} = \pi \arctan (\ln x) \Big | _ {\mathrm {e}} ^ {+ \infty} = \pi \left(\frac {\pi}{2} - \frac {\pi}{4}\right) = \frac {\pi^ {2}}{4}. \\ \end{array}</equation>

---

**2009年第19题 | 解答题 | 10分**

19. (本题满分10分)

设曲线 y=f(x)，其中 f(x)是可导函数，且 f(x)>0.已知曲线 y=f(x)与直线 y=0,x=1及 x=t(t>1)所围成的曲边梯形绕 x轴旋转一周所得的立体体积值是该曲边梯形面积值的<equation>\pi t</equation>倍，求该曲线的方程.

**答案:**(19)<equation>x=\frac{1}{3\sqrt{y}}+\frac{2}{3} y,x\geqslant 1.</equation>

**解析:**解 由旋转体的体积公式知曲边梯形绕 x轴旋转一周所得的立体体积<equation>V=\pi \int_{1}^{t}[f(x)]^{2}\mathrm{d}x.</equation>由定积分的几何意义知曲边梯形的面积<equation>S=\int_{1}^{t}f(x)\mathrm{d}x.</equation>由已知条件知<equation>V=\pi t S</equation>，故对任意的 t > 1，都有<equation>\pi \int_{1}^{t}[f(x)]^{2}\mathrm{d}x=\pi t\int_{1}^{t}f(x)\mathrm{d}x.</equation><equation>\pi \int_ {1} ^ {t} [ f (x) ] ^ {2} \mathrm {d} x = \pi t \int_ {1} ^ {t} f (x) \mathrm {d} x.</equation>上式两端消去<equation>\pi</equation>后并关于<equation>t</equation>求导得，<equation>[ f (t) ] ^ {2} = \int_ {1} ^ {t} f (x) \mathrm {d} x + t f (t).</equation>继续对上式两端关于 t求导得，<equation>2 f (t) f ^ {\prime} (t) = 2 f (t) + t f ^ {\prime} (t).</equation>令<equation>y=f(t)</equation>，得<equation>\frac {\mathrm {d} y}{\mathrm {d} t} = \frac {2 y}{2 y - t}.</equation>下面用两种方法解方程<equation>\frac{\mathrm{d}y}{\mathrm{d}t}=\frac{2y}{2y-t}.</equation>（法一）由<equation>\frac{\mathrm{d}y}{\mathrm{d}t} = \frac{2y}{2y - t}</equation>可得<equation>\frac{\mathrm{d}t}{\mathrm{d}y} + \frac{1}{2y} t = 1.</equation>此为一阶非齐次线性微分方程，其通解为<equation>t = \mathrm {e} ^ {- \int \frac {1}{2 y} \mathrm {d} y} \left(\int \mathrm {e} ^ {\int \frac {1}{2 y} \mathrm {d} y} \mathrm {d} y + C\right) = y ^ {- \frac {1}{2}} \left(\frac {2}{3} y ^ {\frac {3}{2}} + C\right) = C y ^ {- \frac {1}{2}} + \frac {2}{3} y.</equation>由（1）式可得<equation>[ f(1)]^{2}=f(1)</equation>，于是<equation>f(1)=1</equation>（舍去<equation>f(1)=0 )</equation>.代入上式解得<equation>C=\frac{1}{3}</equation>，即<equation>t=\frac{1}{3\sqrt{y}}+\frac{2}{3} y</equation>因此，所求曲线方程为<equation>x = \frac {1}{3 \sqrt {y}} + \frac {2}{3} y, \quad x \geqslant 1.</equation>（法二）此为齐次微分方程.令<equation>u=\frac{y}{t}</equation>，则<equation>y=ut,\frac{\mathrm{d}y}{\mathrm{d}t}=u+t\frac{\mathrm{d}u}{\mathrm{d}t}</equation>，从而<equation>u+t\frac{\mathrm{d}u}{\mathrm{d}t}=\frac{\mathrm{d}y}{\mathrm{d}t}=\frac{2y}{2y-t}=\frac{2u}{2u-1}.</equation>整理得<equation>\frac {2 u - 1}{3 u - 2 u ^ {2}} \mathrm {d} u = \frac {\mathrm {d} t}{t}.</equation>对上式两端积分得，<equation>\int \frac {2 u - 1}{3 u - 2 u ^ {2}} \mathrm {d} u = \int \left(- \frac {1}{3 u} + \frac {4}{3} \cdot \frac {1}{3 - 2 u}\right) \mathrm {d} u = \int \frac {\mathrm {d} t}{t}.</equation>由于 y > 0，t > 1，故 u > 0，从而<equation>-\frac{1}{3}\ln u-\frac{2}{3}\ln |3-2u|=\ln t+C_{1}</equation>，其中<equation>C_{1}</equation>为常数，即<equation>[ u (3 - 2 u) ^ {2} ] ^ {- \frac {1}{3}} = C t, \quad C = \mathrm {e} ^ {C _ {1}}.</equation>同法一可得<equation>f ( 1 )=1.</equation>于是<equation>u ( 1 )=\frac{f ( 1 )}{1}=1.</equation>代入（2）式解得<equation>C=1.</equation>将<equation>u=\frac{y}{t}</equation>代入（2）式化简得到<equation>y(3t-2y)^{2}=1</equation>，从而<equation>t=\frac{1}{3}\left(\pm \frac{1}{\sqrt{y}}+2y\right).</equation>由于<equation>y(1)=1</equation>，故<equation>t=\frac{1}{3}\left(\frac{1}{\sqrt{y}}+2y\right)</equation>即所求曲线方程为<equation>x=\frac{1}{3\sqrt{y}}+\frac{2}{3}y,x\geqslant 1.</equation>

---


#### 不定积分的计算


**2023年第2题 | 选择题 | 5分 | 答案: D**

2. 函数 f(x) =<equation>\left\{\begin{array}{l l}{\frac{1}{\sqrt{1+x^{2}}},}&{x\leqslant0,}\\ {(x+1)\cos x,}&{x>0}\end{array} \right.</equation>的一个原函数为（    )

A. F(x) =<equation>\left\{\begin{array}{l l}{\ln(\sqrt{1+x^{2}}-x),}&{x\leqslant0,}\\ {(x+1)\cos x-\sin x,}&{x>0.}\end{array} \right.</equation>B. F(x) =<equation>\left\{\begin{array}{l l}{\ln(\sqrt{1+x^{2}}-x)+1,}&{x\leqslant0,}\\ {(x+1)\cos x-\sin x,}&{x>0.}\end{array} \right.</equation>C. F(x) =<equation>\left\{\begin{array}{l l}{\ln(\sqrt{1+x^{2}}+x),}&{x\leqslant0,}\\ {(x+1)\sin x+\cos x,}&{x>0.}\end{array} \right.</equation>D. F(x) =<equation>\left\{\begin{array}{l l}{\ln(\sqrt{1+x^{2}}+x)+1,}&{x\leqslant0,}\\ {(x+1)\sin x+\cos x,}&{x>0.}\end{array} \right.</equation>

答案: D

**解析:**解（法一）首先，由于 F(x）是 f(x)的原函数，故必连续，而四个选项中的 F(x)均为分段函数，于是我们可以分别考察 F(x)在分界点处的连续性.

对选项 A,<equation>\lim_{x\rightarrow 0^{-}}F(x)=0, \lim_{x\rightarrow 0^{+}}F(x)=1. F(x)</equation>不连续.

对选项B，<equation>\lim_{x\to 0^{-}}F(x)=\lim_{x\to 0^{+}}F(x)=1=F(0).F(x)</equation>连续.

对选项 C<equation>\lim_{x\rightarrow 0^{-}}F(x)=0,\lim_{x\rightarrow 0^{+}}F(x)=1. F(x)</equation>不连续.

对选项 D<equation>\lim_{x\to 0^{-}}F(x)=\lim_{x\to 0^{+}}F(x)=1=F(0).F(x)</equation>连续.

由上可排除选项A与选项C.

选项B与选项D的差别在于函数表达式.<equation>[ (x + 1) \cos x - \sin x ] ^ {\prime} = \cos x - (x + 1) \sin x - \cos x = - (x + 1) \sin x,</equation><equation>[ (x + 1) \sin x + \cos x ] ^ {\prime} = \sin x + (x + 1) \cos x - \sin x = (x + 1) \cos x.</equation>由上可排除选项B.

因此，应选D.

（法二）当<equation>x\leqslant0</equation>时，<equation>\begin{array}{l} F (x) = \int \frac {\mathrm {d} x}{\sqrt {1 + x ^ {2}}} \xlongequal {x = \tan \theta} \int \frac {\sec^ {2} \theta}{\sec \theta} \mathrm {d} \theta = \int \sec \theta \mathrm {d} \theta = \ln | \sec \theta + \tan \theta | + C _ {1} \\ \underline {{\frac {x = \tan \theta}{2}}} \ln \left(\sqrt {1 + x ^ {2}} + x\right) + C _ {1}. \\ \end{array}</equation>当 x > 0时，<equation>\begin{aligned} F (x) &= \int (x + 1) \cos x \mathrm {d} x = \int (x + 1) \mathrm {d} (\sin x) = (x + 1) \sin x - \int \sin x \mathrm {d} x \\ &= (x + 1) \sin x + \cos x + C _ {2}. \end{aligned}</equation>四个选项中，仅有选项C、D符合要求.

由于 F(x）是 f(x)在<equation>(-\infty, +\infty)</equation>上的一个原函数，故 F(x)在 x=0处连续.<equation>\lim _ {x \rightarrow 0 ^ {-}} F (x) = \lim _ {x \rightarrow 0 ^ {-}} \left[ \ln \left(\sqrt {1 + x ^ {2}} + x\right) + C _ {1} \right] = C _ {1},</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} F (x) = \lim _ {x \rightarrow 0 ^ {+}} \left[ (x + 1) \sin x + \cos x + C _ {2} \right] = C _ {2} + 1.</equation>由<equation>\lim_{x\to 0^{-}}F(x) = \lim_{x\to 0^{+}}F(x)</equation>可得<equation>C_1 = C_2 + 1.</equation>选项C中，<equation>C_{1}=C_{2}=0,F(x)</equation>不连续，选项D中，<equation>C_{1}=1,C_{2}=0,F(x)</equation>连续，应选D.

---

**2018年第10题 | 填空题 | 4分**

**答案:**<equation>\mathrm{e}^{x}\arcsin \sqrt{1 - \mathrm{e}^{2x}} -\sqrt{1 - \mathrm{e}^{2x}} +C</equation>，其中C为任意常数.

**解析:**解 （法一）利用分部积分法.<equation>\begin{array}{l} \int \mathrm {e} ^ {x} \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} \mathrm {d} x \xlongequal {\text {分 部 积 分}} \int \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} \mathrm {d} \left(\mathrm {e} ^ {x}\right) \\ = \mathrm {e} ^ {x} \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} - \int \mathrm {e} ^ {x} \cdot \frac {1}{\sqrt {1 - 1 + \mathrm {e} ^ {2 x}}} \cdot \frac {- 2 \mathrm {e} ^ {2 x}}{2 \sqrt {1 - \mathrm {e} ^ {2 x}}} \mathrm {d} x \\ = \mathrm {e} ^ {x} \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} + \int \frac {\mathrm {e} ^ {2 x}}{\sqrt {1 - \mathrm {e} ^ {2 x}}} \mathrm {d} x \\ = \mathrm {e} ^ {x} \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} - \frac {1}{2} \int \frac {\mathrm {d} \left(1 - \mathrm {e} ^ {2 x}\right)}{\sqrt {1 - \mathrm {e} ^ {2 x}}} \\ = \mathrm {e} ^ {x} \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} - \sqrt {1 - \mathrm {e} ^ {2 x}} + C, \\ \end{array}</equation>其中 C为任意常数.

（法二）利用第二类换元法.

令<equation>\mathrm{e}^{x}=\cos t, t\in\left[0,\frac{\pi}{2}\right)</equation>，则<equation>\sqrt{1-\mathrm{e}^{2x}}=\sin t, t=\arcsin \sqrt{1-\mathrm{e}^{2x}},\mathrm{e}^{x}\mathrm{d}x=-\sin t\mathrm{d}t.</equation>因此，<equation>\begin{array}{l} \int \mathrm {e} ^ {x} \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} \mathrm {d} x = \int t \cdot (- \sin t) \mathrm {d} t = \int t \mathrm {d} (\cos t) = t \cos t - \int \cos t \mathrm {d} t \\ = t \cos t - \sin t + C = \mathrm {e} ^ {x} \arccos \mathrm {e} ^ {x} - \sqrt {1 - \mathrm {e} ^ {2 x}} + C \\ = \mathrm {e} ^ {x} \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} - \sqrt {1 - \mathrm {e} ^ {2 x}} + C, \\ \end{array}</equation>其中 C为任意常数.

---

**2011年第17题 | 解答题 | 10分**

17. (本题满分10分)

求不定积分

**答案:**(17)<equation>2 \sqrt{x} \arcsin \sqrt{x}+2 \sqrt{x} \ln x+2 \sqrt{1-x}-4 \sqrt{x}+C</equation>，其中C为任意常数.

**解析:**解 （法一）利用换元法和分部积分法.

令<equation>\sqrt{x} = t</equation>，则<equation>x = t^{2}</equation>，<equation>t > 0</equation>，<equation>\mathrm{d}x = 2t\mathrm{d}t.</equation>于是，<equation>\begin{array}{l} \int \frac {\arcsin \sqrt {x} + \ln x}{\sqrt {x}} \mathrm {d} x = \int \frac {\arcsin t + \ln t ^ {2}}{t} \cdot 2 t \mathrm {d} t = 2 \int \left(\arcsin t + \ln t ^ {2}\right) \mathrm {d} t \\ \underline {{\mathrm {分 部 积 分}}} = 2 \left[ \left(\arcsin t + \ln t ^ {2}\right) t - \int \left(\frac {1}{\sqrt {1 - t ^ {2}}} + \frac {2 t}{t ^ {2}}\right) t \mathrm {d} t \right] \\ = 2 \left(\arcsin t + \ln t ^ {2}\right) t + \int \frac {\mathrm {d} \left(1 - t ^ {2}\right)}{\sqrt {1 - t ^ {2}}} - \int 4 \mathrm {d} t \\ = 2 \left(\arcsin t + \ln t ^ {2}\right) t + 2 \sqrt {1 - t ^ {2}} - 4 t + C, \\ \end{array}</equation>其中 C为任意常数.

将<equation>t=\sqrt{x}</equation>代回，可得<equation>\text {原 积 分} = 2 \sqrt {x} \arcsin \sqrt {x} + 2 \sqrt {x} \ln x + 2 \sqrt {1 - x} - 4 \sqrt {x} + C,</equation>其中 C为任意常数.

（法二）分部积分法.<equation>\begin{array}{l} \int \frac {\arcsin \sqrt {x} + \ln x}{\sqrt {x}} \mathrm {d} x = 2 \int (\arcsin \sqrt {x} + \ln x) \mathrm {d} (\sqrt {x}) \\ \underline {{\mathrm {分 部 积 分}}} = 2 \left[ \left(\arcsin \sqrt {x} + \ln x\right) \sqrt {x} - \int \sqrt {x} \left(\frac {\frac {1}{2} x ^ {- \frac {1}{2}}}{\sqrt {1 - x}} + \frac {1}{x}\right) \mathrm {d} x \right] \\ = 2 \sqrt {x} \arcsin \sqrt {x} + 2 \sqrt {x} \ln x - \int \left(\frac {1}{\sqrt {1 - x}} + \frac {2}{\sqrt {x}}\right) \mathrm {d} x \\ = 2 \sqrt {x} \arcsin \sqrt {x} + 2 \sqrt {x} \ln x + 2 \sqrt {1 - x} - 4 \sqrt {x} + C, \\ \end{array}</equation>其中 C为任意常数.

---

**2009年第16题 | 解答题 | 10分**

16. (本题满分10分)

计算不定积分<equation>\int\ln\left(1+\sqrt{\frac{1+x}{x}}\right)\mathrm{d}x(x>0).</equation>

**答案:**(16)<equation>x \ln \left( 1+\sqrt{\frac{1+x}{x}} \right)+\frac{1}{2} \ln \left( \sqrt{1+x}+\sqrt{x} \right)-\frac{\sqrt{x}}{2\left( \sqrt{1+x}+\sqrt{x} \right)}-C</equation>，其中C为任意常数.

**解析:**解（法一）令<equation>u=\sqrt{\frac{1+x}{x}}</equation>，则<equation>x=\frac{1}{u^{2}-1}.</equation>于是，<equation>\int \ln \left(1 + \sqrt {\frac {1 + x}{x}}\right) \mathrm {d} x = \int \ln (1 + u) \mathrm {d} \left(\frac {1}{u ^ {2} - 1}\right) = \frac {\ln (1 + u)}{u ^ {2} - 1} - \int \frac {1}{\left(u ^ {2} - 1\right) \left(u + 1\right)} \mathrm {d} u.</equation>计算<equation>\int \frac{1}{(u^{2}-1)(u+1)} \mathrm{d} u.</equation><equation>\begin{aligned} \int \frac {1}{\left(u ^ {2} - 1\right) (u + 1)} \mathrm {d} u &= \frac {1}{2} \int \frac {(u + 1) - (u - 1)}{\left(u ^ {2} - 1\right) (u + 1)} \mathrm {d} u = \frac {1}{2} \left[ \int \frac {1}{u ^ {2} - 1} \mathrm {d} u - \int \frac {1}{(u + 1) ^ {2}} \mathrm {d} u \right] \\ &= \frac {1}{4} \int \left(\frac {1}{u - 1} - \frac {1}{u + 1}\right) \mathrm {d} u - \frac {1}{2} \int \frac {1}{(u + 1) ^ {2}} \mathrm {d} u = \frac {1}{4} \ln \frac {u - 1}{u + 1} + \frac {1}{2 (u + 1)} + C, \end{aligned}</equation>其中 C为任意常数.这里的<equation>\ln \frac{u-1}{u+1}</equation>没有绝对值符号，是因为<equation>u=\sqrt{\frac{1+x}{x}}>1.</equation>将 u =<equation>\sqrt{\frac{1+x}{x}}</equation>代回原积分，得<equation>\begin{aligned} \mathrm {原 积 分} &= \frac {\ln (1 + u)}{u ^ {2} - 1} + \frac {1}{4} \ln \frac {u + 1}{u - 1} - \frac {1}{2 (u + 1)} - C \\ \frac {u = \sqrt {\frac {1 + x}{x}}}{x \ln \left(1 + \sqrt {\frac {1 + x}{x}}\right)} + \frac {1}{2} \ln \left(\sqrt {1 + x} + \sqrt {x}\right) - \frac {\sqrt {x}}{2 \left(\sqrt {1 + x} + \sqrt {x}\right)} - C, \end{aligned}</equation>其中 C为任意常数.

（法二）使用待定系数法来求<equation>\int \frac{1}{(u^{2}-1)(u+1)} \mathrm{d} u.</equation><equation>\begin{aligned} \frac {1}{\left(u ^ {2} - 1\right) (u + 1)} &= \frac {a}{u - 1} + \frac {b}{u + 1} + \frac {c}{(u + 1) ^ {2}} = \frac {a (u + 1) ^ {2} + b (u - 1) (u + 1) + c (u - 1)}{(u - 1) (u + 1) ^ {2}} \\ &= \frac {(a + b) u ^ {2} + (2 a + c) u + a - b - c}{(u - 1) (u + 1) ^ {2}}. \end{aligned}</equation>比较<equation>u^{2}</equation>，<equation>u</equation>的系数以及常数项，可得<equation>\left\{ \begin{array}{l l} a + b = 0, \\ 2a + c = 0, \\ a - b - c = 1, \end{array} \right.</equation>解得<equation>a = \frac{1}{4}, b = -\frac{1}{4}, c = -\frac{1}{2}</equation>.

因此，<equation>\int \frac{1}{(u^{2}-1)(u+1)} \mathrm{d} u=\frac{1}{4} \int \left[ \frac{1}{u-1}-\frac{1}{u+1}-\frac{2}{(u+1)^{2}} \right] \mathrm{d} u=\frac{1}{4} \left( \ln \frac{u-1}{u+1}+\frac{2}{u+1} \right)+C</equation>其中C为任意常数.

其余同法一.

---


#### 定积分的概念与性质


**2022年第4题 | 选择题 | 5分 | 答案: A**

4. 若<equation>I_{1}=\int_{0}^{1}\frac{x}{2(1+\cos x)}\mathrm{d}x,I_{2}=\int_{0}^{1}\frac{\ln(1+x)}{1+\cos x}\mathrm{d}x,I_{3}=\int_{0}^{1}\frac{2x}{1+\sin x}\mathrm{d}x</equation>，则（    )

A.<equation>I_{1}<I_{2}<I_{3}</equation>B.<equation>I_{2}<I_{1}<I_{3}</equation>C.<equation>I_{1}<I_{3}<I_{2}</equation>D.<equation>I_{3}<I_{2}<I_{1}</equation>

答案: A

**解析:**解 通过观察可发现，要比较<equation>I_{1}</equation>与<equation>I_{2}</equation>的大小，只需比较<equation>\frac{x}{2}</equation>与<equation>\ln(1+x)</equation>的大小.

令<equation>f(x)=\ln(1+x)-\frac{x}{2}</equation>，则<equation>f(0)=0</equation><equation>f^{\prime}(x)=\frac{1}{1+x}-\frac{1}{2}</equation>当<equation>x\in(0,1)</equation>时，<equation>f^{\prime}(x)>0</equation><equation>f(x)</equation>单调增加，从而<equation>f(x)>f(0)=0</equation>即<equation>\ln(1+x)>\frac{x}{2},\frac{\ln(1+x)}{1+\cos x}>\frac{x}{2(1+\cos x)}</equation>因此，<equation>I_{2}>I_{1}</equation>.

此外，同样的方法不难证明在(0,1)内，<equation>\ln(1+x)<x.</equation>另一方面，由于在(0,1)内，<equation>0<\sin x,\cos x<1,1<1+\sin x<2</equation>故<equation>I_{3}</equation>的被积函数<equation>\frac{2x}{1+\sin x} >x.</equation>结合<equation>\ln(1+x)<x</equation>可得，<equation>\frac{\ln(1+x)}{1+\cos x}<\frac{x}{1+\cos x}<x.</equation>于是，<equation>\frac{2x}{1+\sin x}>x>\frac{\ln(1+x)}{1+\cos x}.</equation>因此，<equation>I_{3}>I_{2}.</equation>综上所述，应选A.

---

**2018年第3题 | 选择题 | 4分 | 答案: C**

3. 设<equation>M=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{(1+x)^{2}}{1+x^{2}}\mathrm{d}x,N=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{1+x}{\mathrm{e}^{x}}\mathrm{d}x,K=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}(1+\sqrt{\cos x})\mathrm{d}x</equation>，则（    )

A. M > N > K B. M > K > N C. K > M > N D. K > N > M

答案: C

**解析:**分别计算 M,N,K.

由于<equation>\frac{2x}{1+x^{2}}</equation>是奇函数，故<equation>\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{2x}{1+x^{2}}\mathrm{d}x=0.</equation>于是，<equation>M = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {(1 + x) ^ {2}}{1 + x ^ {2}} \mathrm {d} x = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {1 + x ^ {2} + 2 x}{1 + x ^ {2}} \mathrm {d} x \frac {\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {2 x}{1 + x ^ {2}} \mathrm {d} x = 0}{\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \mathrm {d} x = \pi}.</equation>注意到当<equation>x\neq 0</equation>时，<equation>\mathrm{e}^{x}>1+x</equation>.于是，在<equation>\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>上，<equation>\frac{1+x}{e^{x}}\leqslant 1</equation>且等号仅在<equation>x=0</equation>处成立.<equation>N = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {1 + x}{\mathrm {e} ^ {x}} \mathrm {d} x < \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \mathrm {d} x = \pi .</equation>由于<equation>\sqrt{\cos x}</equation>是偶函数，且当 x<equation>\in\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>时，<equation>\cos x\geqslant0</equation>且等号仅在端点处成立，故<equation>\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\sqrt{\cos x}\mathrm{d}x=2\int_{0}^{\frac{\pi}{2}}\sqrt{\cos x}\mathrm{d}x>0.</equation>于是，<equation>K = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \left(1 + \sqrt {\cos x}\right) \mathrm {d} x = \pi + \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \sqrt {\cos x} \mathrm {d} x > \pi .</equation>综上所述，<equation>K > M > N</equation>应选C.

---

**2017年第17题 | 解答题 | 10分**

17. (本题满分10分)<equation>\text {求} \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n ^ {2}} \ln \left(1 + \frac {k}{n}\right)</equation>

**解析:**解 根据定积分的定义，提出因子<equation>\frac{1}{n}</equation>，可得<equation>\begin{array}{l} \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n ^ {2}} \ln \left(1 + \frac {k}{n}\right) = \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n} \ln \left(1 + \frac {k}{n}\right) \cdot \frac {1}{n} = \int_ {0} ^ {1} x \ln (1 + x) d x \\ = \frac {1}{2} \int_ {0} ^ {1} \ln (1 + x) d \left(x ^ {2}\right) \xlongequal {\text {分 部 积 分}} \frac {x ^ {2}}{2} \ln (1 + x) \Bigg | _ {0} ^ {1} - \frac {1}{2} \int_ {0} ^ {1} \frac {x ^ {2}}{1 + x} d x \\ = \frac {\ln 2}{2} - \frac {1}{2} \int_ {0} ^ {1} \frac {x ^ {2} - 1 + 1}{1 + x} d x = \frac {\ln 2}{2} - \frac {1}{2} \int_ {0} ^ {1} \left(x - 1 + \frac {1}{1 + x}\right) d x \\ = \frac {\ln 2}{2} - \frac {1}{2} \left[ \frac {x ^ {2}}{2} - x + \ln (1 + x) \right] \Bigg | _ {0} ^ {1} = \frac {1}{4}. \\ \end{array}</equation>因此，原极限<equation>= \frac{1}{4}.</equation>

---

**2016年第10题 | 填空题 | 4分**

<equation>0. \mathrm {极 限} \lim _ {n \rightarrow \infty} \frac {1}{n ^ {2}} \left(\sin \frac {1}{n} + 2 \sin \frac {2}{n} + \dots + n \sin \frac {n}{n}\right) = \underline {{}}</equation>

**答案:**## sin 1-cos 1.

**解析:**解 将原表达式作恒等变形，得<equation>\frac {1}{n ^ {2}} \left(\sin \frac {1}{n} + 2 \sin \frac {2}{n} + \dots + n \sin \frac {n}{n}\right) = \frac {1}{n} \left(\frac {1}{n} \sin \frac {1}{n} + \frac {2}{n} \sin \frac {2}{n} + \dots + \frac {n}{n} \sin \frac {n}{n}\right).</equation>因此，<equation>\begin{array}{l} \lim _ {n \rightarrow \infty} \left(\frac {1}{n} \sum_ {i = 1} ^ {n} \frac {i}{n} \sin \frac {i}{n}\right) = \int_ {0} ^ {1} x \sin x d x = \int_ {0} ^ {1} x d (- \cos x) \\ = - x \cos x \left| _ {0} ^ {1} + \int_ {0} ^ {1} \cos x d x = \sin 1 - \cos 1. \right. \\ \end{array}</equation>

---

**2014年第19题 | 解答题 | 10分**

19. (本题满分10分)

设函数 f(x), g(x)在区间 [a,b]上连续，且 f(x)单调增加，<equation>0 \leqslant g ( x ) \leqslant1</equation>证明：

I.<equation>0 \leqslant\int_{a}^{x} g ( t ) \mathrm{d} t \leqslant x-a,x \in[a,b]</equation>II.<equation>\int_{a}^{a+\int_{a}^{b} g ( t ) \mathrm{d} t} f ( x ) \mathrm{d} x \leqslant\int_{a}^{b} f ( x ) g ( x ) \mathrm{d} x.</equation>

**答案:**（19）（I）证明略；

（Ⅱ）证明略.

**解析:**证（I）由于在<equation>[a,b]</equation>上，<equation>0\leqslant g(x)\leqslant 1</equation>，故<equation>0 = \int_ {a} ^ {x} 0 \mathrm {d} t \leqslant \int_ {a} ^ {x} g (t) \mathrm {d} t \leqslant \int_ {a} ^ {x} 1 \mathrm {d} t = x - a.</equation>（Ⅱ）（法一）构造辅助函数<equation>F ( u )=\int_{a}^{u} f ( x ) g ( x ) \mathrm{d} x-\int_{a}^{a+\int_{a}^{u} g ( t ) \mathrm{d} t} f ( x ) \mathrm{d} x, u \in[ a, b ],</equation>则第（Ⅱ）问中的不等式等价于<equation>F ( b ) \geqslant0.</equation>由于<equation>F ( a )=0</equation>故若能证明<equation>F^{\prime} ( u ) \geqslant0</equation>则由 F(u)在[a,b]上单调增加可推出<equation>F ( b ) \geqslant0.</equation>计算<equation>F^{\prime}(u).</equation><equation>F ^ {\prime} (u) = f (u) g (u) - f \left(a + \int_ {a} ^ {u} g (t) \mathrm {d} t\right) g (u) = g (u) \left[ f (u) - f \left(a + \int_ {a} ^ {u} g (t) \mathrm {d} t\right) \right].</equation>由第（I）问知，<equation>0 \leqslant \int_{a}^{u} g ( t ) \mathrm{d} t \leqslant u - a</equation>，故<equation>a \leqslant a + \int_{a}^{u} g ( t ) \mathrm{d} t \leqslant u.</equation>于是，由<equation>f ( x )</equation>在<equation>[ a,b]</equation>上单调增加可知，<equation>f (u) - f \left(a + \int_ {a} ^ {u} g (t) \mathrm {d} t\right) \geqslant 0.</equation>从而<equation>F^{\prime}(u)\geqslant 0</equation>，故<equation>F(u)</equation>在<equation>[a,b]</equation>上单调增加.

因此，<equation>F ( b ) \geqslant F ( a ) = 0</equation>，原不等式成立.

（法二）在下面的证明中，我们将用到积分中值定理的一个一般形式.

若<equation>f ( x )</equation>,<equation>g ( x )</equation>在<equation>[ a,b]</equation>上连续，且<equation>g ( x )</equation>在<equation>[ a,b]</equation>上不变号，则<equation>\int_ {a} ^ {b} f (x) g (x) \mathrm {d} x = f (\xi) \int_ {a} ^ {b} g (x) \mathrm {d} x,</equation>其中<equation>\xi\in[a,b].</equation>记<equation>D=\int_{a}^{b} f ( x ) g ( x ) \mathrm{d} x-\int_{a}^{a+\int_{a}^{b} g ( t ) \mathrm{d} t} f ( x ) \mathrm{d} x.</equation>我们证明<equation>D \geqslant 0</equation>注意到<equation>a+\int_{a}^{b} g ( t ) \mathrm{d} t \in[ a,b]</equation>，故<equation>\begin{aligned} D &= \int_ {a} ^ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} [ f (x) g (x) - f (x) ] \mathrm {d} x + \int_ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} ^ {b} f (x) g (x) \mathrm {d} x \\ &= \int_ {a} ^ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} f (x) [ g (x) - 1 ] \mathrm {d} x + \int_ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} ^ {b} f (x) g (x) \mathrm {d} x. \end{aligned}</equation>由于<equation>0 \leqslant g(x) \leqslant 1</equation>，故<equation>g(x) - 1</equation>在<equation>[a,b]</equation>上不变号.由积分中值定理可得<equation>D = f \left(\xi_ {1}\right) \int_ {a} ^ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} [ g (x) - 1 ] \mathrm {d} x + f \left(\xi_ {2}\right) \int_ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} ^ {b} g (x) \mathrm {d} x,</equation>其中，<equation>\xi_{1}\in \left[ a,a + \int_{a}^{b}g(t)\mathrm{d}t\right],\xi_{2}\in \left[ a + \int_{a}^{b}g(t)\mathrm{d}t,b\right].</equation>由于<equation>f(x)</equation>在<equation>[a,b]</equation>上单调增加，故<equation>f(\xi_{1})\leqslant f(\xi_{2})</equation>，从而<equation>\begin{array}{l} D \geqslant f \left(\xi_ {1}\right) \left\{\int_ {a} ^ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} [ g (x) - 1 ] \mathrm {d} x + \int_ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} ^ {b} g (x) \mathrm {d} x \right\} = f \left(\xi_ {1}\right) \left[ \int_ {a} ^ {b} g (x) \mathrm {d} x - \int_ {a} ^ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} 1 \mathrm {d} x \right] \\ = f \left(\xi_ {1}\right) \left[ \int_ {a} ^ {b} g (x) \mathrm {d} x - \int_ {a} ^ {b} g (t) \mathrm {d} t \right] = 0. \\ \end{array}</equation>因此，<equation>D\geqslant 0</equation>，故原不等式得证.

---

**2010年第18题 | 解答题 | 10分**

18. (本题满分10分)

18. (本题满分10分)

I. 比较<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>与<equation>\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t</equation>（ n=1,2，<equation>\cdots</equation>）的大小，说明理由；

II. 记<equation>u_{n}=\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>（ n=1,2，<equation>\cdots</equation>），求极限<equation>\lim_{n\to\infty}u_{n}.</equation>

**答案:**(18) （I）<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t<\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t(n=1,2,\dots),</equation>，理由略；

（Ⅱ）<equation>\lim_{n\to \infty}u_{n}=0.</equation>

**解析:**解（I）在（0,1]上，<equation>\mid \ln t\mid</equation><equation>\ln(1+t)</equation>与 t均非负，故比较<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>与<equation>\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t(n=1,2,\cdots)</equation>的大小，只需比较<equation>\ln(1+t)</equation>与 t的大小.

考虑<equation>f(t)=\ln(1+t)-t</equation>考虑<equation>f ( t )=\ln( 1+t)-t.</equation><equation>f ^ {\prime} (t) = \frac {1}{1 + t} - 1.</equation>当<equation>t\in (0,1]</equation>时，<equation>f^{\prime}(t) < 0,f(t)\leqslant f(0) = 0.</equation>因此，当<equation>t\in [0,1]</equation>时，<equation>\ln (1 + t)\leqslant t.</equation>由于两被积函数仅在<equation>t = 1</equation>处相等，故<equation>\int_ {0} ^ {1} | \ln t | [ \ln (1 + t) ] ^ {n} \mathrm {d} t < \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t (n = 1, 2, \dots).</equation>（Ⅱ）（法一）由第（I）问知，<equation>0 < u_{n} < \int_{0}^{1} t^{n}|\ln t|\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {0} ^ {1} t ^ {n} \mid \ln t \mid \mathrm {d} t &= \frac {- 1}{n + 1} \int_ {0} ^ {1} \ln t \mathrm {d} \left(t ^ {n + 1}\right) = \frac {- 1}{n + 1} \left(t ^ {n + 1} \ln t \mid_ {0} ^ {1} - \int_ {0} ^ {1} t ^ {n + 1} \cdot \frac {1}{t} \mathrm {d} t\right) \\ \frac {\lim _ {t \rightarrow 0 ^ {+}} t ^ {n + 1} \ln t = 0}{\overline {{\quad}}} \frac {1}{n + 1} \int_ {0} ^ {1} t ^ {n} \mathrm {d} t &= \frac {1}{(n + 1) ^ {2}}. \end{aligned}</equation>因此，<equation>\lim _ {n \rightarrow \infty} \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t = \lim _ {n \rightarrow \infty} \frac {1}{(n + 1) ^ {2}} = 0.</equation>由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>（法二）由第（I）问知，<equation>0 < u_{n} < \int_{0}^{1} t^{n}|\ln t|\mathrm{d}t.</equation>又因为<equation>\lim_{t\to 0^{+}}t\ln t = 0</equation>，所以存在<equation>M > 0</equation>，使得对任意的<equation>t\in (0,1]</equation>，有<equation>t|\ln t|\leqslant M</equation>，从而<equation>0 < u _ {n} < \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t \leqslant M \int_ {0} ^ {1} t ^ {n - 1} \mathrm {d} t = \frac {M}{n}.</equation>由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>（法三）由于<equation>t\in[0,1]</equation>时，<equation>\ln(1 + t)\leqslant \ln 2 < 1</equation>，故<equation>u_{n}\leqslant (\ln 2)^{n}\int_{0}^{1}|\ln t|\mathrm{d}t.</equation>计算<equation>\int_{0}^{1}|\ln t| \mathrm{d} t</equation>得，<equation>\int_ {0} ^ {1} | \ln t | \mathrm {d} t = - \int_ {0} ^ {1} \ln t \mathrm {d} t = - \left(t \ln t \left| _ {0} ^ {1} - \int_ {0} ^ {1} 1 \mathrm {d} t\right)\right) \xlongequal {\lim _ {t \rightarrow 0 ^ {+}} t \ln t = 0} 1.</equation>从而<equation>0 < u_{n}\leqslant (\ln 2)^{n}</equation>因为<equation>\lim_{n\to \infty}(\ln 2)^n = 0</equation>，所以由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>

---


### 常微分方程与差分方程

#### 一阶非齐次线性微分方程


**2025年第13题 | 填空题 | 5分**

13. 微分方程<equation>x y^{\prime}-y+x^{2} \mathrm{e}^{x}=0</equation>满足条件<equation>y(1)=- \mathrm{e}</equation>的解为 y=___

**答案:**## xe<equation>^x</equation>.

**解析:**解 整理原方程可得<equation>y^{\prime}-\frac{y}{x}=-x\mathrm{e}^{x}.</equation>由一阶非齐次线性微分方程的通解公式可得<equation>y=\mathrm{e}^{\int \frac{1}{x}\mathrm{d}x}\left[\int(-x\mathrm{e}^{x})\cdot\mathrm{e}^{\int(-\frac{1}{x})\mathrm{d}x}\mathrm{d}x+C\right]=\mid x\mid\left[\int(-x\mathrm{e}^{x})\cdot\frac{1}{\mid x\mid}\mathrm{d}x+C\right]</equation><equation>=-x\int\mathrm{e}^{x}\mathrm{d}x+C\mid x\mid=-x\mathrm{e}^{x}+C\mid x\mid.</equation>将 y（1）=-e代入<equation>y=-x\mathrm{e}^{x}+C\left| x\right|</equation>可得<equation>-\mathrm{e}=-\mathrm{e}+C</equation>，解得 C=0.因此，<equation>y=-x\mathrm{e}^{x}.</equation>

---

**2022年第17题 | 解答题 | 10分**

17. (本题满分10分）

设函数 y(x）是微分方程<equation>y^{\prime}+\frac{1}{2\sqrt{x}} y=2+\sqrt{x}</equation>满足条件 y(1）=3的解，求曲线 y=y(x）的渐近线.

**答案:**y=2x为曲线 y=2x+<equation>\mathrm{e}^{1-\sqrt{x}}</equation>的斜渐近线，也是唯一的渐近线.

**解析:**根据求解公式，<equation>y = \mathrm {e} ^ {- \int \frac {1}{2 \sqrt {x}} \mathrm {d} x} \left[ \int (2 + \sqrt {x}) \mathrm {e} ^ {\int \frac {1}{2 \sqrt {x}} \mathrm {d} x} \mathrm {d} x + C _ {0} \right] = \mathrm {e} ^ {- \sqrt {x}} \left[ \int (2 + \sqrt {x}) \mathrm {e} ^ {\sqrt {x}} \mathrm {d} x + C _ {0} \right].</equation>下面计算<equation>\int(2+\sqrt{x})\mathrm{e}^{\sqrt{x}}\mathrm{d}x.</equation>令<equation>u=\sqrt{x}</equation>，则<equation>x=u^{2}</equation>，<equation>\mathrm{d} x=2 u \mathrm{d} u.</equation><equation>\begin{aligned} \int (2 + \sqrt {x}) \mathrm {e} ^ {\sqrt {x}} \mathrm {d} x \xlongequal {u = \sqrt {x}} 2 \int (2 + u) u \mathrm {e} ^ {u} \mathrm {d} u &= 2 \left(\int u ^ {2} \mathrm {e} ^ {u} \mathrm {d} u + \int 2 u \mathrm {e} ^ {u} \mathrm {d} u\right) \\ &= 2 \left[ \int u ^ {2} \mathrm {d} \left(\mathrm {e} ^ {u}\right) + \int 2 u \mathrm {e} ^ {u} \mathrm {d} u \right] = 2 \left(u ^ {2} \mathrm {e} ^ {u} - \int 2 u \mathrm {e} ^ {u} \mathrm {d} u + \int 2 u \mathrm {e} ^ {u} \mathrm {d} u\right) \\ &= 2 u ^ {2} \mathrm {e} ^ {u} + C _ {1} = 2 x \mathrm {e} ^ {\sqrt {x}} + C _ {1}. \end{aligned}</equation>将该结果代入（1）式，可得<equation>y = \mathrm {e} ^ {- \sqrt {x}} \left(2 x \mathrm {e} ^ {\sqrt {x}} + C\right) = 2 x + C \mathrm {e} ^ {- \sqrt {x}},</equation>其中 C为待定常数.代入<equation>y ( 1 )=3</equation>，可得<equation>3=2+C\cdot\mathrm{e}^{-1}</equation>，解得<equation>C=\mathrm{e}.</equation>因此，<equation>y ( x ) = 2 x + \mathrm {e} ^ {1 - \sqrt {x}} , x \in ( 0, + \infty) .</equation>由于函数<equation>y(x)=2 x+\mathrm{e}^{1-\sqrt{x}}</equation>在（0，<equation>+\infty</equation>）内连续，且<equation>\lim_{x\to 0^{+}}y(x)=\mathrm{e}</equation>，故曲线<equation>y=2 x+\mathrm{e}^{1-\sqrt{x}}</equation>没有铅直渐近线.

又因为<equation>\lim_{x\to +\infty}y(x) = \lim_{x\to +\infty}\left(2x + \mathrm{e}^{1 - \sqrt{x}}\right) = +\infty</equation>，所以曲线<equation>y = 2x + \mathrm{e}^{1 - \sqrt{x}}</equation>没有水平渐近线.

下面计算斜渐近线.<equation>\lim _ {x \rightarrow + \infty} \frac {y (x)}{x} = \lim _ {x \rightarrow + \infty} \frac {2 x + \mathrm {e} ^ {1 - \sqrt {x}}}{x} = 2,</equation><equation>\lim _ {x \rightarrow + \infty} [ y (x) - 2 x ] = \lim _ {x \rightarrow + \infty} \mathrm {e} ^ {1 - \sqrt {x}} = 0.</equation>因此，<equation>y=2x</equation>为曲线<equation>y=2x+\mathrm{e}^{1-\sqrt{x}}</equation>的斜渐近线，也是唯一的渐近线.

---

**2019年第17题 | 解答题 | 10分**

17. (本题满分10分)

设函数 y(x)是微分方程<equation>y^{\prime}-xy=\frac{1}{2\sqrt{x}} \mathrm{e}^{\frac{x^{2}}{2}}</equation>满足条件 y(1)<equation>=\sqrt{\mathrm{e}}</equation>的特解.

I. 求 y(x);

II. 设平面区域 D = {(x,y) | 1≤x≤2,0≤y≤y(x)}，求 D绕 x轴旋转所得旋转体的体积.

**答案:**(I)<equation>y(x)=\sqrt{x}\mathrm{e}^{\frac{x^{2}}{2}}</equation>; (II)<equation>\frac{1}{2}\pi(\mathrm{e}^{4}-\mathrm{e}).</equation>

**解析:**（I）由一阶非齐次线性微分方程的求解公式可得，<equation>\begin{aligned} y &= \mathrm {e} ^ {\int x \mathrm {d} x} \left[ \int \frac {1}{2 \sqrt {x}} \cdot \mathrm {e} ^ {\frac {x ^ {2}}{2}} \cdot \mathrm {e} ^ {\int (- x) \mathrm {d} x} \mathrm {d} x + C \right] = \mathrm {e} ^ {\frac {x ^ {2}}{2}} \left(\int \frac {1}{2 \sqrt {x}} \cdot \mathrm {e} ^ {\frac {x ^ {2}}{2}} \cdot \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \mathrm {d} x + C\right) \\ &= \mathrm {e} ^ {\frac {x ^ {2}}{2}} \left(\int \frac {1}{2 \sqrt {x}} \mathrm {d} x + C\right) = \sqrt {x} \mathrm {e} ^ {\frac {x ^ {2}}{2}} + C \mathrm {e} ^ {\frac {x ^ {2}}{2}}, \end{aligned}</equation>其中 C为待定常数.

代入<equation>x = 1,y(1) = \sqrt{\mathrm{e}}</equation>，可得<equation>\sqrt{\mathrm{e}} = \sqrt{\mathrm{e}} + C\sqrt{\mathrm{e}}.</equation>解得<equation>C = 0.</equation>因此，<equation>y ( x ) = \sqrt{x}\mathrm{e}^{\frac{x^{2}}{2}}.</equation>（Ⅱ）区域 D 如图所示.

根据旋转体的体积计算公式，<equation>\begin{aligned} V &= \pi \int_ {1} ^ {2} \left(\sqrt {x} \mathrm {e} ^ {\frac {x ^ {2}}{2}}\right) ^ {2} \mathrm {d} x = \pi \int_ {1} ^ {2} x \mathrm {e} ^ {x ^ {2}} \mathrm {d} x = \frac {1}{2} \pi \int_ {1} ^ {2} \mathrm {e} ^ {x ^ {2}} \mathrm {d} \left(x ^ {2}\right) \\ &= \frac {1}{2} \pi \mathrm {e} ^ {x ^ {2}} \Bigg | _ {1} ^ {2} = \frac {1}{2} \pi \left(\mathrm {e} ^ {4} - \mathrm {e}\right). \end{aligned}</equation>

---

**2014年第17题 | 解答题 | 10分**

17. (本题满分10分)

设函数 f(u)具有连续导数，且<equation>z=f(\mathrm{e}^{x}\cos y)</equation>满足<equation>\cos y\frac{\partial z}{\partial x}-\sin y\frac{\partial z}{\partial y}=(4z+\mathrm{e}^{x}\cos y)\mathrm{e}^{x}.</equation>若 f(0)=0，求 f(u)的表达式.

**答案:**<equation>(1 7) f (u) = \frac {1}{1 6} \mathrm {e} ^ {4 u} - \frac {1}{4} u - \frac {1}{1 6}.</equation>

**解析:**由链式法则知，<equation>\frac {\partial z}{\partial x} = f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right) \cdot \left(\mathrm {e} ^ {x} \cos y\right), \quad \frac {\partial z}{\partial y} = f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right) \cdot \left(- \mathrm {e} ^ {x} \sin y\right).</equation>代入题设等式中可得，<equation>\mathrm {e} ^ {x} \cos^ {2} y f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right) + \mathrm {e} ^ {x} \sin^ {2} y f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right) = \left(4 z + \mathrm {e} ^ {x} \cos y\right) \mathrm {e} ^ {x}.</equation>化简得<equation>f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right) = 4 f \left(\mathrm {e} ^ {x} \cos y\right) + \mathrm {e} ^ {x} \cos y.</equation>令<equation>u=\mathrm{e}^{x}\cos y</equation>，得<equation>f ^ {\prime} (u) - 4 f (u) = u.</equation>此为一阶非齐次线性微分方程，由求解公式知，<equation>f (u) = \mathrm {e} ^ {- \int (- 4) \mathrm {d} u} \left[ \int u \mathrm {e} ^ {\int (- 4) \mathrm {d} u} \mathrm {d} u + C \right] = \mathrm {e} ^ {4 u} \left(\frac {\mathrm {e} ^ {- 4 u}}{- 4} u - \int \frac {\mathrm {e} ^ {- 4 u}}{- 4} \mathrm {d} u + C\right) = - \frac {1}{4} u - \frac {1}{1 6} + C \mathrm {e} ^ {4 u},</equation>其中 C为待定常数.

将<equation>f ( 0 )=0</equation>代入上式得<equation>C=\frac{1}{1 6}.</equation>因此，<equation>f (u) = \frac {1}{1 6} \mathrm {e} ^ {4 u} - \frac {1}{4} u - \frac {1}{1 6}.</equation>

---


#### 常系数齐次线性微分方程


**2023年第3题 | 选择题 | 5分 | 答案: C**

3. 若微分方程<equation>y^{\prime \prime}+ay^{\prime}+by=0</equation>的解在<equation>(-\infty,+\infty)</equation>上有界，则（    )

A. a < 0,b > 0 B. a > 0,b > 0 C. a = 0,b > 0 D. a = 0,b < 0

答案: C

**解析:**解 由于二阶常系数齐次线性微分方程必有零解，而零解为有界解，故微分方程<equation>y^{\prime \prime}+a y^{\prime}+b y</equation>=0必然存在（<equation>-\infty, +\infty</equation>）上的有界解.本题实际上是要求此方程的所有解都有界.

微分方程<equation>y^{\prime \prime}+a y^{\prime}+b y=0</equation>的特征方程为<equation>\lambda^{2}+a \lambda+b=0.</equation>- 若<equation>\Delta=a^{2}-4 b>0</equation>，则特征方程有两个不同实根<equation>\lambda_{1},\lambda_{2}</equation>，从而至少有一个实根非零.此时，微分方程的解为<equation>y=C_{1}\mathrm{e}^{\lambda_{1}x}+C_{2}\mathrm{e}^{\lambda_{2}x}.</equation>- 取<equation>C_{1}=C_{2}=1</equation>，则<equation>\lim_{x\to -\infty}\left(\mathrm{e}^{\lambda_{1}x}+\mathrm{e}^{\lambda_{2}x}\right)=+\infty</equation>或<equation>\lim_{x\to +\infty}\left(\mathrm{e}^{\lambda_{1}x}+\mathrm{e}^{\lambda_{2}x}\right)=+\infty.</equation>该解在<equation>(-\infty, +\infty)</equation>上无界.

- 若<equation>\Delta=a^{2}-4 b=0</equation>，则特征方程有两个相同实根<equation>\lambda</equation>.此时，微分方程的解为<equation>y=(C_{1}+ C_{2} x) \mathrm{e}^{\lambda x}.</equation>取<equation>C_{1}=0, C_{2}=1</equation>，则<equation>\lim_{x\to -\infty}x\mathrm{e}^{\lambda x}=\infty</equation>或<equation>\lim_{x\to +\infty}x\mathrm{e}^{\lambda x}=\infty</equation>.该解在<equation>(-\infty , +\infty)</equation>上无界.

- 若<equation>\Delta=a^{2}-4 b<0</equation>，则特征方程有一对共轭复根<equation>\lambda_{1,2}=\alpha\pm\beta\mathrm{i}</equation>.此时，微分方程的解为<equation>y=\mathrm{e}^{\alpha x}\left(C_{1}\cos \beta x+C_{2}\sin \beta x\right).</equation>当<equation>\alpha\neq0</equation>时，取<equation>C_{1}=1,C_{2}=0</equation>，所得解<equation>y=\mathrm{e}^{\alpha x}\cos \beta x</equation>是<equation>(-\infty, +\infty)</equation>上的无界函数.

当<equation>\alpha=0</equation>时，微分方程的解为<equation>y=C_{1}\cos \beta x+C_{2}\sin \beta x</equation>对任意常数<equation>C_{1},C_{2}</equation>，该解在<equation>(-\infty,+\infty)</equation>上均有界.根据求根公式，<equation>\lambda_{1,2}=-\frac{a}{2}\pm \frac{\sqrt{4b-a^{2}}}{2}\mathrm{i}</equation>即<equation>\alpha=-\frac{a}{2}</equation>于是，<equation>a=0</equation>结合<equation>a^{2}-4b<0</equation>可知，<equation>b>0.</equation>因此，<equation>a=0,b>0</equation>应选C.

---

**2020年第17题 | 解答题 | 10分**

17. (本题满分10分)

设函数 y=f(x)满足<equation>y^{\prime \prime}+2 y^{\prime}+5 y=0</equation>，且 f(0)=1，<equation>f^{\prime}(0)=-1.</equation>I. 求 f(x)的表达式；

II. 设<equation>a_{n}=\int_{n \pi}^{+\infty} f(x)\mathrm{d} x</equation>，求<equation>\sum_{n=1}^{\infty} a_{n}.</equation>

**答案:**<equation>\begin{array}{l} (\mathrm {I}) f (x) = \mathrm {e} ^ {- x} \cos 2 x; \\ (\mathrm {I I}) \sum_ {n = 1} ^ {\infty} a _ {n} = \frac {1}{5 \left(\mathrm {e} ^ {\pi} - 1\right)}. \\ \end{array}</equation>

**解析:**解（I）<equation>y^{\prime \prime}+2 y^{\prime}+5 y=0</equation>的特征方程为<equation>r^{2}+2 r+5=0</equation>.解得特征根<equation>r_{1,2}=-1\pm 2 \mathrm{i}.</equation>由特征根与解的关系可得<equation>f (x) = \mathrm {e} ^ {- x} \left(C _ {1} \cos 2 x + C _ {2} \sin 2 x\right),</equation>其中<equation>C_{1}, C_{2}</equation>为待定常数.

由<equation>f(0) = 1</equation>可得，<equation>C_{1} = 1.</equation>计算<equation>f^{\prime}(x).</equation><equation>f ^ {\prime} (x) = - \mathrm {e} ^ {- x} \left(C _ {1} \cos 2 x + C _ {2} \sin 2 x\right) + \mathrm {e} ^ {- x} \left(- 2 C _ {1} \sin 2 x + 2 C _ {2} \cos 2 x\right).</equation>由<equation>f^{\prime}(0)=-1</equation>可得，<equation>-C_{1}+2 C_{2}=-1</equation>，解得<equation>C_{2}=0.</equation>因此，<equation>f ( x ) = \mathrm{e}^{-x}\cos 2x.</equation>（Ⅱ）（法一）由<equation>y^{\prime \prime}+2 y^{\prime}+5 y=0</equation>可得，<equation>f(x)=-\frac{1}{5}[f^{\prime \prime}(x)+2 f^{\prime}(x)]</equation>.于是，<equation>\begin{array}{l} a _ {n} = \int_ {n \pi} ^ {+ \infty} f (x) \mathrm {d} x = - \frac {1}{5} \int_ {n \pi} ^ {+ \infty} \left[ f ^ {\prime \prime} (x) + 2 f ^ {\prime} (x) \right] \mathrm {d} x = - \frac {1}{5} \left[ f ^ {\prime} (x) + 2 f (x) \right] \Bigg | _ {n \pi} ^ {+ \infty} \\ = - \frac {1}{5} \left\{\lim _ {x \rightarrow + \infty} \left[ f ^ {\prime} (x) + 2 f (x) \right] - \left[ f ^ {\prime} (n \pi) + 2 f (n \pi) \right]\right\}. \\ \end{array}</equation>由第（I）问可知，<equation>f(x) = \mathrm{e}^{-x}\cos 2x,f^{\prime}(x) = -\mathrm{e}^{-x}\cos 2x-2\mathrm{e}^{-x}\sin 2x.</equation>从而，<equation>\lim_{x\to +\infty}f(x) = 0,</equation><equation>\lim_{x\to +\infty}f^{\prime}(x) = 0,f(n\pi) = \mathrm{e}^{-n\pi},f^{\prime}(n\pi) = -\mathrm{e}^{-n\pi}.</equation>因此，<equation>a _ {n} = \frac {1}{5} \left[ f ^ {\prime} (n \pi) + 2 f (n \pi) \right] = \frac {1}{5} \mathrm {e} ^ {- n \pi}.</equation><equation>\sum_ {n = 1} ^ {\infty} a _ {n} = \frac {1}{5} \sum_ {n = 1} ^ {\infty} \mathrm {e} ^ {- n \pi} = \frac {1}{5} \cdot \frac {\mathrm {e} ^ {- \pi}}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{5 \left(\mathrm {e} ^ {\pi} - 1\right)}.</equation>（法二）计算<equation>a_{n}</equation><equation>\begin{array}{l} a _ {n} = \int_ {n \pi} ^ {+ \infty} \mathrm {e} ^ {- x} \cos 2 x \mathrm {d} x \xlongequal {t = x - n \pi} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- (t + n \pi)} \cos 2 (t + n \pi) \mathrm {d} t \\ = \mathrm {e} ^ {- n \pi} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- t} \cos 2 t \mathrm {d} t. \\ \end{array}</equation>下面计算<equation>\int_{0}^{+\infty}\mathrm{e}^{-t}\cos 2t\mathrm{d}t.</equation><equation>\begin{array}{l} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- t} \cos 2 t \mathrm {d} t = - \int_ {0} ^ {+ \infty} \cos 2 t \mathrm {d} \left(\mathrm {e} ^ {- t}\right) = - \left[ \mathrm {e} ^ {- t} \cos 2 t \Big | _ {0} ^ {+ \infty} - \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- t} \cdot (- 2 \sin 2 t) \mathrm {d} t \right] \\ = - \left(- 1 + 2 \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- t} \sin 2 t \mathrm {d} t\right) = 1 - 2 \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- t} \sin 2 t \mathrm {d} t \\ = 1 + 2 \int_ {0} ^ {+ \infty} \sin 2 t \mathrm {d} \left(\mathrm {e} ^ {- t}\right) = 1 + 2 \left(\mathrm {e} ^ {- t} \sin 2 t \Big | _ {0} ^ {+ \infty} - \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- t} \cdot 2 \cos 2 t \mathrm {d} t\right) \\ = 1 - 4 \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- t} \cos 2 t \mathrm {d} t. \\ \end{array}</equation>由上式可得，<equation>5\int_{0}^{+\infty}\mathrm{e}^{-t}\cos 2t\mathrm{d}t=1</equation>即<equation>\int_{0}^{+\infty}\mathrm{e}^{-t}\cos 2t\mathrm{d}t=\frac{1}{5}.</equation>因此，<equation>a_{n}=\frac{1}{5}\mathrm{e}^{-n\pi}.</equation><equation>\sum_ {n = 1} ^ {\infty} a _ {n} = \frac {1}{5} \sum_ {n = 1} ^ {\infty} \mathrm {e} ^ {- n \pi} = \frac {1}{5} \cdot \frac {\mathrm {e} ^ {- \pi}}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{5 \left(\mathrm {e} ^ {\pi} - 1\right)}.</equation>

---

**2015年第12题 | 填空题 | 4分**

12. 设函数<equation>y=y(x)</equation>是微分方程<equation>y^{\prime\prime}+y^{\prime}-2y=0</equation>的解，且在<equation>x=0</equation>处<equation>y(x)</equation>取得极值3，则<equation>y(x)=</equation>___.

**答案:**<equation>2 \mathrm{e}^{x}+\mathrm{e}^{-2 x}.</equation>

**解析:**解<equation>y^{\prime \prime}+y^{\prime}-2 y=0</equation>的特征方程为<equation>\lambda^{2}+\lambda-2=0</equation>，解得<equation>\lambda_{1}=1,\lambda_{2}=-2.</equation>于是<equation>y(x)= C_{1}\mathrm{e}^{x}+C_{2}\mathrm{e}^{-2x}</equation>，其中<equation>C_{1},C_{2}</equation>为待定常数.

由题设及一元函数取极值的必要条件知，<equation>y ( 0 )=3, y^{\prime} ( 0 )=0.</equation>将其代入 y(x）的表达式中可得<equation>C_{1}+C_{2}=3, C_{1}-2 C_{2}=0.</equation>解得<equation>C_{1}=2, C_{2}=1.</equation>因此，<equation>y (x) = 2 \mathrm {e} ^ {x} + \mathrm {e} ^ {- 2 x}.</equation>

---

**2013年第12题 | 填空题 | 4分**

12. 微分方程<equation>y^{\prime\prime}-y^{\prime}+\frac{1}{4} y=0</equation>的通解为 y=___

**答案:**（<equation>C_{1}+C_{2}x) \mathrm{e}^{\frac{1}{2} x}</equation>，其中<equation>C_{1},C_{2}</equation>为任意常数.

**解析:**解 微分方程<equation>y^{\prime \prime}-y^{\prime}+\frac{1}{4} y=0</equation>的特征方程为<equation>\lambda^{2}-\lambda+\frac{1}{4}=0</equation>，解得<equation>\lambda_{1}=\lambda_{2}=\frac{1}{2}</equation>因此，原方程的通解为<equation>y=(C_{1}+C_{2}x)\mathrm{e}^{\frac{1}{2}x}</equation>其中<equation>C_{1}, C_{2}</equation>为任意常数.

---

**2012年第19题 | 解答题 | 10分**

19. (本题满分10分)

已知函数 f(x)满足方程<equation>f^{\prime \prime}(x)+f^{\prime}(x)-2 f(x)=0</equation>及<equation>f^{\prime \prime}(x)+f(x)=2 \mathrm{e}^{x}</equation>.

I. 求 f(x)的表达式;

II. 求曲线<equation>y=f\left(x^{2}\right)\int_{0}^{x} f\left(-t^{2}\right)\mathrm{d} t</equation>的拐点.

**答案:**(19) ( I )<equation>f(x)=\mathrm{e}^{x};</equation>( II ) ( 0,0 ).

**解析:**解（I）（法一）本题中有两个微分方程，可先写出其中的二阶常系数齐次线性微分方程的通解，再将该通解代入另一个方程以确定通解中的常数.<equation>f^{\prime \prime}(x) + f^{\prime}(x) - 2 f(x) = 0</equation>为二阶常系数齐次线性微分方程它的特征方程为<equation>r^{2}+r-2=0</equation>，该方程有两个不同的实根<equation>r_{1}=1,r_{2}=-2</equation>，从而其解为<equation>f(x)=C_{1}\mathrm{e}^{x}+C_{2}\mathrm{e}^{-2x}</equation>其中<equation>C_{1},C_{2}</equation>为待定常数.

计算<equation>f^{\prime}(x), f^{\prime\prime}(x)</equation>得<equation>f ^ {\prime} (x) = C _ {1} \mathrm {e} ^ {x} - 2 C _ {2} \mathrm {e} ^ {- 2 x}, f ^ {\prime \prime} (x) = C _ {1} \mathrm {e} ^ {x} + 4 C _ {2} \mathrm {e} ^ {- 2 x}.</equation>代入<equation>f^{\prime \prime}(x) + f(x) = 2\mathrm{e}^{x}</equation>，得<equation>2C_{1}\mathrm{e}^{x} + 5C_{2}\mathrm{e}^{-2x} = 2\mathrm{e}^{x}</equation>，从而得<equation>C_{1} = 1, C_{2} = 0.</equation>因此，<equation>f ( x ) = \mathrm{e}^{x}.</equation><equation>f ^ {\prime \prime} (x) + f ^ {\prime} (x) - 2 f (x) = 0,</equation><equation>f ^ {\prime \prime} (x) + f (x) = 2 \mathrm {e} ^ {x}.</equation>(1) 式-（2）式得<equation>f^{\prime}(x) - 3f(x) = -2\mathrm{e}^{x}</equation>，为一阶非齐次线性微分方程.由求解公式得<equation>f (x) = C \mathrm {e} ^ {- \int (- 3) \mathrm {d} x} + \mathrm {e} ^ {- \int (- 3) \mathrm {d} x} \int \left(- 2 \mathrm {e} ^ {x}\right) \mathrm {e} ^ {\int (- 3) \mathrm {d} x} \mathrm {d} x = \mathrm {e} ^ {x} + C \mathrm {e} ^ {3 x},</equation>其中 C为待定常数.

代回（2）式，得<equation>\mathrm {e} ^ {x} + 9 C \mathrm {e} ^ {3 x} + \mathrm {e} ^ {x} + C \mathrm {e} ^ {3 x} = 2 \mathrm {e} ^ {x}.</equation>从而 C=0.

因此，<equation>f ( x ) = \mathrm{e}^{x}.</equation>（Ⅱ）将<equation>f(x) = \mathrm{e}^{x}</equation>代入曲线方程，对<equation>y</equation>逐次求导，得<equation>y = f \left(x ^ {2}\right) \int_ {0} ^ {x} f \left(- t ^ {2}\right) \mathrm {d} t = \mathrm {e} ^ {x ^ {2}} \int_ {0} ^ {x} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t,</equation><equation>y ^ {\prime} = \mathrm {e} ^ {x ^ {2}} \cdot \mathrm {e} ^ {- x ^ {2}} + 2 x \mathrm {e} ^ {x ^ {2}} \int_ {0} ^ {x} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t = 1 + 2 x y,</equation><equation>y ^ {\prime \prime} = \frac {\mathrm {d} (1 + 2 x y)}{\mathrm {d} x} = 2 y + 2 x y ^ {\prime} = 2 y + 2 x (1 + 2 x y) = 2 \left(2 x ^ {2} + 1\right) y + 2 x.</equation>由于<equation>\mathrm{e}^{x^{2}} > 0</equation><equation>\mathrm{e}^{-t^{2}} > 0</equation>，故当 x > 0时，y > 0.从而<equation>y ^ {\prime \prime} (x) = 2 \left(2 x ^ {2} + 1\right) y + 2 x > 0.</equation>当<equation>x < 0</equation>时，<equation>y < 0</equation><equation>y ^ {\prime \prime} (x) = 2 \left(2 x ^ {2} + 1\right) y + 2 x < 0.</equation>当<equation>x = 0</equation>时，<equation>y(0) = 0</equation>，<equation>y^{\prime \prime}(0) = 0.</equation>因此，点（0,0）为曲线<equation>y = f\left(x^{2}\right)\int_{0}^{x}f\left(-t^{2}\right)\mathrm{d}t</equation>的拐点.

---


#### 微分方程的应用


**2023年第14题 | 填空题 | 5分**

14. 设某公司在 t 时刻的资产为 f(t)，从 0 时刻到 t 时刻的平均资产等于<equation>\frac{f(t)}{t}-t</equation>. 假设 f(t) 连续且 f(0)=0，则<equation>f(t)=</equation>___.

**答案:**<equation>2 \mathrm {e} ^ {t} - 2 t - 2.</equation>

**解析:**解对 t > 0，从0时刻到 t时刻的平均资产为<equation>\frac{1}{t}\int_{0}^{t} f(u)\mathrm{d}u</equation>，故由已知条件可知<equation>\frac {1}{t} \int_ {0} ^ {t} f (u) \mathrm {d} u = \frac {f (t)}{t} - t.</equation>整理可得<equation>\int_ {0} ^ {t} f (u) \mathrm {d} u = f (t) - t ^ {2}.</equation>对（1）式两端关于 t求导，可得<equation>f (t) = f ^ {\prime} (t) - 2 t, \quad \mathrm {即} f ^ {\prime} (t) - f (t) = 2 t.</equation>由一阶非齐次线性微分方程的通解公式可得<equation>\begin{array}{l} f (t) = \mathrm {e} ^ {\int \mathrm {d} t} \left(\int 2 t \cdot \mathrm {e} ^ {- \int \mathrm {d} t} \mathrm {d} t + C\right) = \mathrm {e} ^ {t} \left(\int 2 t \cdot \mathrm {e} ^ {- t} \mathrm {d} t + C\right) \\ = \mathrm {e} ^ {t} \left[ - 2 \int t \mathrm {d} \left(\mathrm {e} ^ {- t}\right) + C \right] = \mathrm {e} ^ {t} \left[ - 2 \left(t \mathrm {e} ^ {- t} - \int \mathrm {e} ^ {- t} \mathrm {d} t\right) + C \right] \\ = \mathrm {e} ^ {t} \left(- 2 t \mathrm {e} ^ {- t} - 2 \mathrm {e} ^ {- t} + C\right) = C \mathrm {e} ^ {t} - 2 t - 2. \\ \end{array}</equation>代入初始条件<equation>f ( 0 ) = 0</equation>，可得<equation>0 = C - 2</equation>，即<equation>C = 2.</equation>因此，<equation>f ( t ) = 2 \mathrm{e}^{t} - 2 t - 2.</equation>

---

**2015年第18题 | 解答题 | 10分**

18. (本题满分10分)

设函数 f(x)在定义域 I上的导数大于零.若对任意的<equation>x_{0}\in I</equation>，曲线 y=f(x)在点 （<equation>x_{0},f(x_{0})</equation>）处的切线与直线<equation>x=x_{0}</equation>及 x轴所围成区域的面积恒为4，且 f(0)=2，求 f(x)的表达式.

**答案:**<equation>(1 8) f (x) = \frac {8}{4 - x}, x \in I.</equation>

**解析:**解如图所示，曲线<equation>y=f(x)</equation>在点<equation>\left(x_{0},f\left(x_{0}\right)\right)</equation>处的切线为<equation>y - f \left(x _ {0}\right) = f ^ {\prime} \left(x _ {0}\right) \left(x - x _ {0}\right).</equation>令<equation>y = 0</equation>，注意到<equation>f^{\prime}(x) > 0</equation>，解得<equation>x = x_{0} - \frac{f(x_{0})}{f^{\prime}(x_{0})}</equation>，即该切线与<equation>x</equation>轴的交点为<equation>\left(x_0 - \frac{f(x_0)}{f^{\prime}(x_0)},0\right)</equation>.

曲线<equation>y=f(x)</equation>在点<equation>\left(x_{0}, f\left(x_{0}\right)\right)</equation>处的切线与直线<equation>x=x_{0}</equation>及x轴所围成区域为三角形，底边长<equation>\left|x_{0}-\left[x_{0}-\frac{f\left(x_{0}\right)}{f^{\prime}\left(x_{0}\right)}\right]\right|</equation>，高<equation>|f(x_{0})-0|</equation>.于是，<equation>\frac {\left| f \left(x _ {0}\right) - 0 \right| \cdot \left| x _ {0} - \left[ x _ {0} - \frac {f \left(x _ {0}\right)}{f ^ {\prime} \left(x _ {0}\right)} \right] \right|}{2} = 4, \quad \text {即} \frac {\left| f \left(x _ {0}\right) \right| \cdot \left| \frac {f \left(x _ {0}\right)}{f ^ {\prime} \left(x _ {0}\right)} \right|}{2} = 4.</equation>由于<equation>f^{\prime}(x) > 0</equation>，故<equation>\frac {\left[ f \left(x _ {0}\right) \right] ^ {2}}{f ^ {\prime} \left(x _ {0}\right)} = 8, \quad x _ {0} \in I,</equation>即<equation>f(x)</equation>满足微分方程<equation>8y^{\prime} = y^{2}</equation>.

分离变量，得<equation>\frac{8}{y^{2}}\mathrm{d}y=\mathrm{d}x.</equation>方程两端积分，得<equation>-\frac{8}{y}=x+C</equation>其中C为待定常数.由于<equation>f(0)=2</equation>故 C=-4，从而<equation>y=\frac{8}{4-x}.</equation>因此，<equation>f (x) = \frac {8}{4 - x}, \quad x \in I.</equation>

---


#### 差分方程


**2021年第14题 | 填空题 | 5分**

14. 差分方程<equation>\Delta y_{t} = t</equation>的通解为<equation>y_{t} =</equation>___

**答案:**<equation>\frac{1}{2} t^{2}-\frac{1}{2} t+C</equation>，其中C为任意常数.

**解析:**解（法一）由于<equation>\Delta y_{t}=y_{t+1}-y_{t}</equation>，故<equation>\Delta y_{t}=t</equation>等价于<equation>y_{t+1}-y_{t}=t</equation>，为一阶常系数非齐次线性差分方程.

因为<equation>a = 1</equation>，所以<equation>\tilde{y}_t = C</equation>为<equation>y_{t + 1} - y_t = 0</equation>的通解.

又因为自由项为 t，所以可设<equation>y_{t}^{*} = t \left(B_{0} + B_{1} t\right).</equation>代回<equation>y_{t+1}-y_{t}=t</equation>可得<equation>B _ {0} (t + 1) + B _ {1} (t + 1) ^ {2} - B _ {0} t - B _ {1} t ^ {2} = 2 B _ {1} t + B _ {1} + B _ {0} = t.</equation>于是，<equation>B_{1}=\frac{1}{2}, B_{0}=-\frac{1}{2}.</equation>从而，<equation>y_{t}^{*}=\frac{1}{2} t^{2}-\frac{1}{2} t.</equation>因此，原方程的通解为<equation>y_{t}=\frac{1}{2} t^{2}-\frac{1}{2} t+C</equation>，其中C为任意常数.

（法二）由已知条件可知，<equation>y_{t + 1} - y_{t} = t.</equation>于是，<equation>y _ {t} - y _ {t - 1} = t - 1, \quad y _ {t - 1} - y _ {t - 2} = t - 2, \quad \dots , \quad y _ {2} - y _ {1} = 1.</equation>从而，<equation>y _ {t} = \left(y _ {t} - y _ {t - 1}\right) + \left(y _ {t - 1} - y _ {t - 2}\right) + \dots + \left(y _ {2} - y _ {1}\right) + y _ {1} = \frac {t (t - 1)}{2} + y _ {1}.</equation>由于<equation>y_{1}</equation>可以取任意常数，故<equation>y_{t}=\frac{t(t-1)}{2}+C=\frac{1}{2} t^{2}-\frac{1}{2} t+C</equation>，其中C为任意常数.

---

**2018年第11题 | 填空题 | 4分**

11. 差分方程<equation>\Delta^{2} y_{x}-y_{x}=5</equation>的通解为 ___

**答案:**<equation>y_{x}=C2^{x}-5</equation>，其中C为任意常数.

**解析:**解 由于<equation>\Delta^{2} y_{x}=\Delta y_{x+1}-\Delta y_{x}</equation>，故<equation>\Delta^{2} y_{x}=\Delta y_{x+1}-\Delta y_{x}=\left(y_{x+2}-y_{x+1}\right)-\left(y_{x+1}-y_{x}\right)=y_{x+2}-2y_{x+1}+y_{x}.</equation>由<equation>\Delta^{2} y_{x}-y_{x}=5</equation>可得，<equation>y_{x+2}-2y_{x+1}=5</equation>即<equation>y_{x+1}-2y_{x}=5.</equation>下面用两种方法解<equation>y_{x + 1} - 2y_{x} = 5.</equation>（法一）这是一个一阶非齐次线性差分方程.该方程对应的齐次差分方程的通解为<equation>\tilde{y}_{x}=C2^{x}</equation>其中C为任意常数.

设原方程的一个特解为<equation>y_{x}^{*} = k</equation>，代入原方程得 k-2k=5.解得 k=-5.于是，特解为<equation>y_{x}^{*} = -5.</equation>因此，原方程的通解为<equation>y_{x} = C2^{x} - 5</equation>其中 C为任意常数.

（法二）由<equation>y_{x+1}-2 y_{x}=5</equation>可得，<equation>y_{x+1}+5=2 \left( y_{x}+5 \right).</equation>于是，<equation>\left\{y_{x}+5\right\}_{x \in \mathbf{N}}</equation>是一个首项为<equation>y_{0}+5</equation>公比为2的等比数列.记<equation>C=y_{0}+5</equation>，可得<equation>y_{x}+5=C2^{x}</equation>即<equation>y_{x}=C2^{x}-5.</equation>由于<equation>y_{0}</equation>可取任意常数，故C为任意常数.

---

**2017年第10题 | 填空题 | 4分**

10. 差分方程<equation>y_{t+1}-2y_{t}=2^{t}</equation>的通解为<equation>y_{t}=</equation>___.

**答案:**<equation>\left(C + \frac{1}{2} t\right)2^{t}</equation>，其中C为任意常数.

**解析:**解<equation>y_{t+1}-2 y_{t}=2^{t}</equation>对应的齐次方程为<equation>y_{t+1}-2 y_{t}=0</equation>，其通解为<equation>\widetilde{y}_{t}=C2^{t}</equation>其中C为任意常数设原方程的一个特解为<equation>y_{t}^{*} = k t 2^{t}</equation>，代入原方程得<equation>k ( t+1 ) 2^{t+1}-2 k t 2^{t}=2^{t}</equation>解得<equation>k=\frac{1}{2}</equation>于是，特解为<equation>y_{t}^{*} = \frac{1}{2} t 2^{t}</equation>因此，原方程的通解为<equation>y_{t} = \left(C + \frac{1}{2} t\right) 2^{t}</equation>其中C为任意常数.

---


#### 二阶常系数非齐次线性微分方程


**2019年第3题 | 选择题 | 4分 | 答案: D**

3. 已知微分方程<equation>y^{\prime \prime}+ay^{\prime}+by=c\mathrm{e}^{x}</equation>的通解为<equation>y=(C_{1}+C_{2}x)\mathrm{e}^{-x}+\mathrm{e}^{x}</equation>，则 a,b,c依次为（    )

A. 1,0,1 B. 1,0,2 C. 2,1,3 D. 2,1,4

答案: D

**解析:**解 由原方程的通解形式可知，<equation>y = ( C_{1} + C_{2} x ) \mathrm{e}^{-x}</equation>是原方程对应的齐次线性微分方程的通解，故<equation>r=-1</equation>为该齐次方程的特征方程的二重根.于是，特征方程为<equation>( r+1 )^{2}=0</equation>即<equation>r^{2}+2 r+1=0.</equation>从而，<equation>a=2,b=1.</equation>由原方程的通解形式可知，<equation>y=\mathrm{e}^{x}</equation>是原方程的一个特解.将<equation>y=\mathrm{e}^{x}</equation>代入<equation>y^{\prime \prime}+2y^{\prime}+y=c\mathrm{e}^{x}</equation>可得，<equation>4\mathrm{e}^{x}=c\mathrm{e}^{x}.</equation>于是，<equation>c=4.</equation>因此，<equation>a=2,b=1,c=4.</equation>应选D.

---


#### 线性微分方程的解的结构


**2010年第2题 | 选择题 | 4分 | 答案: A**

2. 设<equation>y_{1}, y_{2}</equation>是一阶线性非齐次微分方程<equation>y^{\prime}+p(x)y=q(x)</equation>的两个特解，若常数<equation>\lambda,\mu</equation>使<equation>\lambda y_{1}+\mu y_{2}</equation>是该方程的解，<equation>\lambda y_{1}-\mu y_{2}</equation>是该方程对应的齐次方程的解，则（    )

A.<equation>\lambda=\frac{1}{2},\mu=\frac{1}{2}</equation>B.<equation>\lambda=-\frac{1}{2},\mu=-\frac{1}{2}</equation>C.<equation>\lambda=\frac{2}{3},\mu=\frac{1}{3}</equation>D.<equation>\lambda=\frac{2}{3},\mu=\frac{2}{3}</equation>

答案: A

**解析:**由题设知，<equation>y _ {1} ^ {\prime} + p (x) y _ {1} = q (x), \quad y _ {2} ^ {\prime} + p (x) y _ {2} = q (x).</equation>又由题设知，<equation>\lambda y_{1} + \mu y_{2}</equation>也是<equation>y^{\prime} + p(x)y = q(x)</equation>的解，故<equation>\left(\lambda y _ {1} + \mu y _ {2}\right) ^ {\prime} + p (x) \left(\lambda y _ {1} + \mu y _ {2}\right) = q (x).</equation>整理（1）式，得<equation>\lambda \left[ y _ {1} ^ {\prime} + p (x) y _ {1} \right] + \mu \left[ y _ {2} ^ {\prime} + p (x) y _ {2} \right] = q (x),</equation>即<equation>(\lambda +\mu)q(x) = q(x)</equation>. 由于<equation>q(x)\neq 0</equation>，故<equation>\lambda +\mu = 1.</equation>又由<equation>\lambda y_{1} - \mu y_{2}</equation>是<equation>y^{\prime} + p(x)y = 0</equation>的解知<equation>\left(\lambda y _ {1} - \mu y _ {2}\right) ^ {\prime} + p (x) \left(\lambda y _ {1} - \mu y _ {2}\right) = 0.</equation>整理（2）式，得<equation>\lambda \left[ y _ {1} ^ {\prime} + p (x) y _ {1} \right] - \mu \left[ y _ {2} ^ {\prime} + p (x) y _ {2} \right] = 0,</equation>即<equation>(\lambda -\mu)q(x) = 0.</equation>由于<equation>q(x)\neq 0</equation>，故<equation>\lambda -\mu = 0.</equation>联立<equation>\left\{ \begin{array}{l l} \lambda +\mu =1, \\ \lambda -\mu =0, \end{array} \right.</equation>解得<equation>\lambda =\frac{1}{2},\mu =\frac{1}{2}</equation>.应选A.
