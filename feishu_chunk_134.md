#### 二重积分的综合与应用

**2014年第10题 | 填空题 | 4分**

10. 设 D 是由曲线<equation>xy+1=0</equation>与直线<equation>y+x=0</equation>及<equation>y=2</equation>围成的有界区域，则 D 的面积为 ___.

**答案:**<equation>\frac {3}{2} - \ln 2.</equation>

**解析:**（法一）区域D如图（a）所示.将D写为Y型区域，<equation>D = \left\{(x, y) \mid - y \leqslant x \leqslant - \frac {1}{y}, 1 \leqslant y \leqslant 2 \right\}.</equation>因此，<equation>D</equation>的面积<equation>= \iint_{D} \mathrm{d}x \mathrm{d}y = \int_{1}^{2} \mathrm{d}y \int_{-y}^{-\frac{1}{y}} \mathrm{d}x = \int_{1}^{2} \left(-\frac{1}{y} + y\right) \mathrm{d}y = -\ln y \left|_{1}^{2} + \frac{y^{2}}{2}\right|_{1}^{2} = \frac{3}{2} - \ln 2.</equation>（法二）如图（b）所示，将<equation>D</equation>分为两个X型区域<equation>D_{1}, D_{2}</equation>.<equation>D _ {1} = \left\{(x, y) \mid - x \leqslant y \leqslant 2, - 2 \leqslant x \leqslant - 1 \right\},</equation><equation>D _ {2} = \left\{(x, y) \mid - \frac {1}{x} \leqslant y \leqslant 2, - 1 \leqslant x \leqslant - \frac {1}{2} \right\}.</equation>因此，<equation>\begin{array}{l} D \text {的 面 积} = \iint_ {D} \mathrm {d} x \mathrm {d} y = \iint_ {D _ {1}} \mathrm {d} x \mathrm {d} y + \iint_ {D _ {2}} \mathrm {d} x \mathrm {d} y = \int_ {- 2} ^ {- 1} \mathrm {d} x \int_ {- x} ^ {2} \mathrm {d} y + \int_ {- 1} ^ {- \frac {1}{2}} \mathrm {d} x \int_ {- \frac {1}{x}} ^ {2} \mathrm {d} y \\ = \int_ {- 2} ^ {- 1} (2 + x) \mathrm {d} x + \int_ {- 1} ^ {- \frac {1}{2}} \left(2 + \frac {1}{x}\right) \mathrm {d} x = \frac {1}{2} + 1 + \ln \frac {1}{2} = \frac {3}{2} - \ln 2. \\ \end{array}</equation>

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


