**解析:**解 记<equation>A=\iint_{D}f(x,y)\mathrm{d}x\mathrm{d}y.</equation>等式<equation>f ( x,y)=y \sqrt{1-x^{2}}+x \iint_{D} f ( x,y)\mathrm{d} x \mathrm{d} y</equation>两端在 D上积分，可得<equation>A=\iint_{D} y \sqrt{1-x^{2}}\mathrm{d} x \mathrm{d} y+A \iint_{D} x \mathrm{d} x \mathrm{d} y.</equation>区域 D如图所示，为位于 x轴上方的半圆盘，关于 y轴对称.又因为 x为关于 x的奇函数，所以<equation>\iint\limits_{D}x\mathrm{d}x\mathrm{d}y=0.</equation>将 D写成 X型区域.<equation>D=\{(x,y)\mid 0\leqslant y\leqslant \sqrt{1-x^{2}},-1\leqslant x\leqslant 1\}</equation>.于是，<equation>\begin{aligned} A &= \iint_ {D} y \sqrt {1 - x ^ {2}} \mathrm {d} x \mathrm {d} y = \int_ {- 1} ^ {1} \sqrt {1 - x ^ {2}} \mathrm {d} x \int_ {0} ^ {\sqrt {1 - x ^ {2}}} y \mathrm {d} y = \int_ {- 1} ^ {1} \sqrt {1 - x ^ {2}} \cdot \frac {1 - x ^ {2}}{2} \mathrm {d} x \\ \frac {\mathrm {对称 性}}{} \int_ {0} ^ {1} \left(1 - x ^ {2}\right) ^ {\frac {3}{2}} \mathrm {d} x \frac {x = \sin t}{\mathrm {对称 性}} \int_ {0} ^ {\frac {\pi}{2}} \cos^ {3} t \cdot \cos t \mathrm {d} t \\ &= \frac {3}{4} \times \frac {1}{2} \times \frac {\pi}{2} = \frac {3}{1 6} \pi . \end{aligned}</equation>因此，<equation>f ( x,y)=y\sqrt{1-x^{2}}+\frac{3\pi}{16} x.</equation><equation>\begin{aligned} \iint_ {D} x f (x, y) \mathrm {d} x \mathrm {d} y &= \iint_ {D} \left(x y \sqrt {1 - x ^ {2}} + \frac {3 \pi}{1 6} x ^ {2}\right) \mathrm {d} x \mathrm {d} y \xlongequal {\text {对称性}} \frac {3 \pi}{1 6} \iint_ {D} x ^ {2} \mathrm {d} x \mathrm {d} y \\ \underline {{\text {极 坐 标}}} \frac {3 \pi}{1 6} \int_ {0} ^ {\pi} \mathrm {d} \theta \int_ {0} ^ {1} r ^ {2} \cos^ {2} \theta \cdot r \mathrm {d} r &= \frac {3 \pi}{1 6} \int_ {0} ^ {\pi} \cos^ {2} \theta \mathrm {d} \theta \int_ {0} ^ {1} r ^ {3} \mathrm {d} r \\ &= \frac {3 \pi}{1 6} \cdot 2 \int_ {0} ^ {\frac {\pi}{2}} \cos^ {2} \theta \mathrm {d} \theta \cdot \frac {1}{4} = \frac {3 \pi}{1 6} \times 2 \times \frac {1}{2} \times \frac {\pi}{2} \times \frac {1}{4} \\ &= \frac {3 \pi^ {2}}{1 2 8}. \end{aligned}</equation>

---

**2018年第16题 | 解答题 | 10分**

16. (本题满分10分)

设平面区域 D由曲线<equation>y=\sqrt{3(1-x^{2})}</equation>与直线<equation>y=\sqrt{3}x</equation>及 y轴围成.计算二重积分<equation>\iint_{D}x^{2}\mathrm{d}x\mathrm{d}y.</equation>

**答案:**<equation>\frac {\sqrt {3}}{3 2} (\pi - 2).</equation>

**解析:**解 计算曲线<equation>y=\sqrt{3(1-x^{2})}</equation>与直线<equation>y=\sqrt{3} x</equation>的交点.

联立<equation>\left\{\begin{array}{l l}y=\sqrt{3(1-x^{2})},\\ y=\sqrt{3} x,\end{array}\right.</equation>解得<equation>x=\frac{\sqrt{2}}{2},y=\frac{\sqrt{6}}{2}.</equation>区域 D如图所示，其可以写成X型区域.<equation>D = \left\{(x, y) \mid \sqrt {3} x \leqslant y \leqslant \sqrt {3 \left(1 - x ^ {2}\right)}, 0 \leqslant x \leqslant \frac {\sqrt {2}}{2} \right\}.</equation>于是，<equation>\begin{aligned} \iint_ {D} x ^ {2} \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {\frac {\sqrt {2}}{2}} x ^ {2} \mathrm {d} x \int_ {\sqrt {3} x} ^ {\sqrt {3 (1 - x ^ {2})}} \mathrm {d} y = \sqrt {3} \int_ {0} ^ {\frac {\sqrt {2}}{2}} \left(\sqrt {1 - x ^ {2}} - x\right) x ^ {2} \mathrm {d} x \\ &= \sqrt {3} \left(\int_ {0} ^ {\frac {\sqrt {2}}{2}} x ^ {2} \sqrt {1 - x ^ {2}} \mathrm {d} x - \int_ {0} ^ {\frac {\sqrt {2}}{2}} x ^ {3} \mathrm {d} x\right). \end{aligned}</equation>分别计算<equation>\int_{0}^{\frac{\sqrt{2}}{2}}x^{2}\sqrt{1-x^{2}}\mathrm{d}x,</equation><equation>\int_{0}^{\frac{\sqrt{2}}{2}}x^{3}\mathrm{d}x.</equation><equation>\begin{aligned} \int_ {0} ^ {\frac {\sqrt {2}}{2}} x ^ {2} \sqrt {1 - x ^ {2}} \mathrm {d} x \xlongequal {x = \sin t} \int_ {0} ^ {\frac {\pi}{4}} \sin^ {2} t \cos t \cdot \cos t \mathrm {d} t &= \frac {1}{4} \int_ {0} ^ {\frac {\pi}{4}} \sin^ {2} 2 t \mathrm {d} t = \frac {1}{4} \int_ {0} ^ {\frac {\pi}{4}} \frac {1 - \cos 4 t}{2} \mathrm {d} t \\ &= \frac {1}{4} \times \frac {\pi}{8} - \frac {1}{4} \cdot \frac {\sin 4 t}{8} \Bigg | _ {0} ^ {\frac {\pi}{4}} = \frac {\pi}{3 2} - 0 = \frac {\pi}{3 2}. \end{aligned}</equation><equation>\int_ {0} ^ {\frac {\sqrt {2}}{2}} x ^ {3} \mathrm {d} x = \frac {x ^ {4}}{4} \Big | _ {0} ^ {\frac {\sqrt {2}}{2}} = \frac {1}{1 6}.</equation>因此，原积分<equation>= \sqrt{3}\times \left(\frac{\pi}{32} -\frac{1}{16}\right) = \frac{\sqrt{3}}{32}(\pi -2).</equation>也可以如下计算<equation>\int_{0}^{\frac{\sqrt{2}}{2}}x^{2}\sqrt{1-x^{2}}\mathrm{d}x.</equation><equation>\int_ {0} ^ {\frac {\sqrt {2}}{2}} x ^ {2} \sqrt {1 - x ^ {2}} \mathrm {d} x = \frac {1}{4} \int_ {0} ^ {\frac {\pi}{4}} \sin^ {2} 2 t \mathrm {d} t \xlongequal {u = 2 t} \frac {1}{8} \int_ {0} ^ {\frac {\pi}{2}} \sin^ {2} u \mathrm {d} u = \frac {1}{8} \times \frac {\pi}{2} \times \frac {1}{2} = \frac {\pi}{3 2}.</equation>

---

**2017年第16题 | 解答题 | 10分**

16. (本题满分10分)

计算积分<equation>\iint_ {D} \frac {y ^ {3}}{\left(1 + x ^ {2} + y ^ {4}\right) ^ {2}}</equation><equation>\mathrm{d}x\mathrm{d}y</equation>，其中<equation>D</equation>是第一象限中以曲线<equation>y = \sqrt{x}</equation>与<equation>x</equation>轴为边界的无界区域.

**答案:**<equation>\frac {(2 - \sqrt {2}) \pi}{1 6}.</equation>

**解析:**分析本题主要考查反常二重积分的计算.本题中的积分区域为无界区域，在计算时，写出无界区域的表示，将二重积分化为二次积分，最后得到一个反常积分.依照计算反常积分的方法求值即可.

解 积分区域 D为第一象限中，曲线<equation>y=\sqrt{x}</equation>以下，x轴以上的无界区域，写成X型区域的形式.<equation>D = \left\{(x, y) \mid 0 \leqslant y \leqslant \sqrt {x}, 0 \leqslant x < + \infty \right\}.</equation><equation>\begin{aligned} \iint_ {D} \frac {y ^ {3}}{\left(1 + x ^ {2} + y ^ {4}\right) ^ {2}} \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {+ \infty} \mathrm {d} x \int_ {0} ^ {\sqrt {x}} \frac {y ^ {3}}{\left(1 + x ^ {2} + y ^ {4}\right) ^ {2}} \mathrm {d} y = \frac {1}{4} \int_ {0} ^ {+ \infty} \mathrm {d} x \int_ {0} ^ {\sqrt {x}} \frac {\mathrm {d} \left(y ^ {4}\right)}{\left(1 + x ^ {2} + y ^ {4}\right) ^ {2}} \\ &= \frac {1}{4} \int_ {0} ^ {+ \infty} \left(- \frac {1}{1 + x ^ {2} + y ^ {4}} \Big | _ {0} ^ {\sqrt {x}}\right) \mathrm {d} x = \frac {1}{4} \int_ {0} ^ {+ \infty} \left(\frac {1}{1 + x ^ {2}} - \frac {1}{1 + 2 x ^ {2}}\right) \mathrm {d} x \\ &= \frac {1}{4} \left[ \arctan x - \frac {\sqrt {2}}{2} \arctan (\sqrt {2} x) \right] \Big | _ {0} ^ {+ \infty} = \frac {1}{4} \left(\frac {\pi}{2} - \frac {\sqrt {2}}{2} \times \frac {\pi}{2}\right) = \frac {(2 - \sqrt {2}) \pi}{1 6}. \end{aligned}</equation>

---

**2016年第12题 | 填空题 | 4分**

12. 设<equation>D=\{(x,y)\mid|x|\leqslant y\leqslant 1,-1\leqslant x\leqslant 1\}</equation>，则<equation>\iint_{D}x^{2}\mathrm{e}^{-y^{2}}\mathrm{d}x\mathrm{d}y=</equation>___

**答案:**# 2 3e.

**解析:**解如图所示，区域 D是由 y=x，y=-x以及 y=1围成的三角形区域. D关于 y轴对称.<equation>D_{1}</equation>为 D位于右半平面的部分.

由于<equation>x^{2}\mathrm{e}^{-y^{2}}</equation>是关于 x的偶函数，故<equation>\begin{aligned} \iint_ {D} x ^ {2} \mathrm {e} ^ {- y ^ {2}} \mathrm {d} x \mathrm {d} y &= 2 \iint_ {D _ {1}} x ^ {2} \mathrm {e} ^ {- y ^ {2}} \mathrm {d} x \mathrm {d} y = 2 \int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {y} x ^ {2} \mathrm {e} ^ {- y ^ {2}} \mathrm {d} x = \frac {2}{3} \int_ {0} ^ {1} y ^ {3} \mathrm {e} ^ {- y ^ {2}} \mathrm {d} y \\ \underline {{= t = y ^ {2}}} \frac {1}{3} \int_ {0} ^ {1} t \mathrm {e} ^ {- t} \mathrm {d} t &= \frac {1}{3} - \frac {2}{3 \mathrm {e}}. \end{aligned}</equation>

---

**2015年第16题 | 解答题 | 10分**

16. (本题满分10分)

计算二重积分<equation>D = \left\{(x, y) \mid x ^ {2} + y ^ {2} \leqslant 2, y \geqslant x ^ {2} \right\}.</equation>

**答案:**## (16)<equation>\frac{\pi}{4}-\frac{2}{5}.</equation>

**解析:**解 由图（a）可知，区域D关于y轴对称，而xy为关于x的奇函数，故<equation>\iint_{D} xy\mathrm{d}x\mathrm{d}y=0</equation>.又因为<equation>x^{2}</equation>为关于x的偶函数，所以

(a)

(b)

(c)<equation>\iint_ {D} x (x + y) \mathrm {d} x \mathrm {d} y = \iint_ {D} x ^ {2} \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} x ^ {2} \mathrm {d} x \mathrm {d} y,</equation>其中<equation>D_{1}</equation>是<equation>D</equation>位于右半平面的部分.我们可以用两种方法来计算<equation>\iint_{D} x^{2}\mathrm{d}x\mathrm{d}y.</equation>（法一）在直角坐标系下计算.

如图（b）所示，先求出圆弧<equation>x^{2}+y^{2}=2</equation>与抛物线<equation>y=x^{2}</equation>的交点.由<equation>\left\{ \begin{array}{l l} x^{2}+y^{2}=2, \\ y=x^{2}, \end{array} \right.</equation>可求得<equation>(x,y) = (1,1)</equation>或<equation>(x,y) = (-1,1)</equation>.在第一象限中的交点为<equation>(x,y) = (1,1).</equation>由圆方程<equation>x^{2}+y^{2}=2</equation>可得，<equation>y=\sqrt{2-x^{2}}</equation>.由于圆弧在第一象限，故根号前取+号.将区域<equation>D_{1}</equation>写成 X型区域，

从而<equation>D _ {1} = \left\{(x, y) \mid x ^ {2} \leqslant y \leqslant \sqrt {2 - x ^ {2}}, 0 \leqslant x \leqslant 1 \right\}.</equation><equation>\begin{aligned} \iint_ {D _ {1}} x ^ {2} \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {1} \mathrm {d} x \int_ {x ^ {2}} ^ {\sqrt {2 - x ^ {2}}} x ^ {2} \mathrm {d} y = \int_ {0} ^ {1} x ^ {2} \left(\sqrt {2 - x ^ {2}} - x ^ {2}\right) \mathrm {d} x \\ &= \int_ {0} ^ {1} x ^ {2} \sqrt {2 - x ^ {2}} \mathrm {d} x - \int_ {0} ^ {1} x ^ {4} \mathrm {d} x = \int_ {0} ^ {1} x ^ {2} \sqrt {2 - x ^ {2}} \mathrm {d} x - \frac {1}{5} \\ \xlongequal {x = \sqrt {2} \sin t} \int_ {0} ^ {\frac {\pi}{4}} 4 \sin^ {2} t \cos^ {2} t \mathrm {d} t - \frac {1}{5} &= \int_ {0} ^ {\frac {\pi}{4}} (\sin 2 t) ^ {2} \mathrm {d} t - \frac {1}{5} \\ &= \int_ {0} ^ {\frac {\pi}{4}} \frac {1 - \cos 4 t}{2} \mathrm {d} t - \frac {1}{5} = \frac {\pi}{8} - \frac {1}{5}. \end{aligned}</equation>因此，<equation>\iint_ {D} x (x + y) \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} x ^ {2} \mathrm {d} x \mathrm {d} y = \frac {\pi}{4} - \frac {2}{5}.</equation>（法二）在极坐标系下计算.

写出<equation>x^{2}+y^{2}=2</equation>的极坐标形式：<equation>r=\sqrt{2}</equation>写出<equation>y=x^{2}</equation>的极坐标形式：<equation>r\sin \theta=r^{2}\cos^{2}\theta</equation>化简为<equation>r=\tan \theta \sec \theta.</equation>可求得圆弧与抛物线的交点坐标为<equation>\left(\sqrt{2},\frac{\pi}{4}\right).</equation>如图（c）所示，连接极点与该交点，将区域<equation>D_{1}</equation>分成两部分，<equation>D_{1}=D_{1}^{\prime}\cup D_{1}^{\prime\prime}.</equation><equation>D_{1}^{\prime}</equation>由<equation>\theta=\frac{\pi}{4},</equation><equation>\theta=\frac{\pi}{2}</equation>以及圆弧<equation>r=\sqrt{2}</equation>围成；<equation>D_{1}^{\prime\prime}</equation>由<equation>\theta=\frac{\pi}{4},</equation><equation>r=\tan \theta\sec \theta</equation>围成从而<equation>D _ {1} ^ {\prime} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \sqrt {2}, \frac {\pi}{4} \leqslant \theta \leqslant \frac {\pi}{2} \right\}, \quad D _ {1} ^ {\prime \prime} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \tan \theta \sec \theta , 0 \leqslant \theta \leqslant \frac {\pi}{4} \right\}.</equation><equation>\begin{aligned} \iint_ {D _ {1}} x ^ {2} \mathrm {d} x \mathrm {d} y &= \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {\sqrt {2}} r ^ {3} \cos^ {2} \theta \mathrm {d} r + \int_ {0} ^ {\frac {\pi}{4}} \mathrm {d} \theta \int_ {0} ^ {\tan \theta \sec \theta} r ^ {3} \cos^ {2} \theta \mathrm {d} r \\ &= \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \frac {1 + \cos 2 \theta}{2} \mathrm {d} \theta + \int_ {0} ^ {\frac {\pi}{4}} \cos^ {2} \theta \cdot \frac {\tan^ {4} \theta \sec^ {4} \theta}{4} \mathrm {d} \theta \\ &= \frac {\pi}{8} - \frac {1}{4} + \frac {1}{4} \int_ {0} ^ {\frac {\pi}{4}} \tan^ {4} \theta \sec^ {2} \theta \mathrm {d} \theta \frac {u = \tan \theta}{\pi} - \frac {1}{4} + \frac {1}{4} \int_ {0} ^ {1} u ^ {4} \mathrm {d} u \\ &= \frac {\pi}{8} - \frac {1}{5}. \end{aligned}</equation>因此，<equation>\iint_ {D} x (x + y) \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} x ^ {2} \mathrm {d} x \mathrm {d} y = \frac {\pi}{4} - \frac {2}{5}.</equation>

---

**2014年第16题 | 解答题 | 10分**

16. (本题满分10分)

设平面区域<equation>D=\{(x,y)\mid 1\leqslant x^{2}+y^{2}\leqslant 4,x\geqslant 0,y\geqslant 0\}</equation>，计算<equation>\iint_{D}\frac{x\sin(\pi\sqrt{x^{2}+y^{2}})}{x+y}\mathrm{d}x\mathrm{d}y.</equation>

**答案:**<equation>(1 6) - \frac {3}{4}.</equation>

**解析:**解记<equation>\iint_{D} \frac{x\sin(\pi \sqrt{x^{2}+y^{2}})}{x+y}\mathrm{d}x\mathrm{d}y=I.</equation>积分区域如图所示.

（法一）在极坐标系下，<equation>D=\left\{(r,\theta)\mid 1\leqslant r\leqslant 2,0\leqslant \theta \leqslant \frac{\pi}{2}\right\} .</equation><equation>I=\int_{0}^{\frac{\pi}{2}}\mathrm{d}\theta \int_{1}^{2}\frac{r\cos \theta \sin (\pi r)}{r(\cos \theta +\sin \theta)} \cdot r\mathrm{d}r=\int_{0}^{\frac{\pi}{2}}\frac{\cos \theta}{\cos \theta +\sin \theta}\mathrm{d}\theta \int_{1}^{2}r\sin (\pi r)\mathrm{d}r.</equation>由于<equation>\int_ {0} ^ {\frac {\pi}{2}} \frac {\cos \theta}{\cos \theta + \sin \theta} \mathrm {d} \theta \stackrel {t = \frac {\pi}{2} - \theta} {=} - \int_ {\frac {\pi}{2}} ^ {0} \frac {\sin t}{\cos t + \sin t} \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \frac {\sin \theta}{\cos \theta + \sin \theta} \mathrm {d} \theta ,</equation>故<equation>\int_ {0} ^ {\frac {\pi}{2}} \frac {\cos \theta}{\cos \theta + \sin \theta} \mathrm {d} \theta = \frac {1}{2} \int_ {0} ^ {\frac {\pi}{2}} \left(\frac {\cos \theta}{\cos \theta + \sin \theta} + \frac {\sin \theta}{\cos \theta + \sin \theta}\right) \mathrm {d} \theta = \frac {1}{2} \int_ {0} ^ {\frac {\pi}{2}} 1 \mathrm {d} \theta = \frac {\pi}{4}.</equation>此外，<equation>\int_ {1} ^ {2} r \sin (\pi r) \mathrm {d} r = - \frac {1}{\pi} \int_ {1} ^ {2} r \mathrm {d} [ \cos (\pi r) ] = - \frac {1}{\pi} \left[ r \cos (\pi r) \left| _ {1} ^ {2} - \int_ {1} ^ {2} \cos (\pi r) \mathrm {d} r \right] = - \frac {3}{\pi} \right].</equation>因此，<equation>I = \frac{\pi}{4}\times \left(-\frac{3}{\pi}\right) = -\frac{3}{4}.</equation>（法二）首先，由于积分区域<equation>D</equation>关于<equation>y = x</equation>对称，故对<equation>x, y</equation>具有轮换对称性，从而<equation>I = \iint_ {D} \frac {x \sin \left(\pi \sqrt {x ^ {2} + y ^ {2}}\right)}{x + y} \mathrm {d} x \mathrm {d} y = \iint_ {D} \frac {y \sin \left(\pi \sqrt {x ^ {2} + y ^ {2}}\right)}{x + y} \mathrm {d} x \mathrm {d} y.</equation>因此，<equation>I = \frac {1}{2} \iint_ {D} \left[ \frac {x \sin \left(\pi \sqrt {x ^ {2} + y ^ {2}}\right)}{x + y} + \frac {y \sin \left(\pi \sqrt {x ^ {2} + y ^ {2}}\right)}{x + y} \right] \mathrm {d} x \mathrm {d} y = \frac {1}{2} \iint_ {D} \sin \left(\pi \sqrt {x ^ {2} + y ^ {2}}\right) \mathrm {d} x \mathrm {d} y.</equation>在极坐标系下，<equation>D = \left\{(r,\theta)\mid 1\leqslant r\leqslant 2,0\leqslant \theta \leqslant \frac{\pi}{2}\right\}.</equation><equation>I = \frac {1}{2} \int_ {0} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {1} ^ {2} \sin (\pi r) \cdot r \mathrm {d} r = \frac {\pi}{4} \int_ {1} ^ {2} r \sin (\pi r) \mathrm {d} r,</equation>由法一知<equation>\int_1^2 r\sin (\pi r)\mathrm{d}r = -\frac{3}{\pi}</equation>，故<equation>I = \frac{\pi}{4}\times \left(-\frac{3}{\pi}\right) = -\frac{3}{4}</equation>.

---

**2013年第17题 | 解答题 | 10分**

17. (本题满分10分)

设平面区域 D由直线 x=3y，y=3x及 x+y=8围成，计算<equation>\iint\limits_{D}x^{2}\mathrm{d}x\mathrm{d}y.</equation>

**答案:**## (17)<equation>\frac{4 1 6}{3}.</equation>

**解析:**解（法一）在直角坐标系下计算.

如图所示，可以分别求出<equation>y=3 x</equation>与<equation>x+y=8</equation>的交点，以及<equation>x=3 y</equation>与<equation>x+y=8</equation>的交点.<equation>\left\{ \begin{array}{l l} y = 3 x, \\ x + y = 8, \end{array} \right. \Rightarrow \left\{ \begin{array}{l l} x = 2, \\ y = 6, \end{array} \right. \quad \left\{ \begin{array}{l l} x = 3 y, \\ x + y = 8, \end{array} \right. \Rightarrow \left\{ \begin{array}{l l} x = 6, \\ y = 2. \end{array} \right.</equation>于是直线<equation>x = 2</equation>将区域<equation>D</equation>分为两部分<equation>D_{1}, D_{2}</equation>.<equation>D _ {1} = \left\{(x, y) \mid \frac {x}{3} \leqslant y \leqslant 3 x, 0 \leqslant x \leqslant 2 \right\}, \quad D _ {2} = \left\{(x, y) \mid \frac {x}{3} \leqslant y \leqslant 8 - x, 2 \leqslant x \leqslant 6 \right\}.</equation><equation>\begin{aligned} \iint_ {D} x ^ {2} \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {2} x ^ {2} \mathrm {d} x \int_ {\frac {x}{3}} ^ {3 x} \mathrm {d} y + \int_ {2} ^ {6} x ^ {2} \mathrm {d} x \int_ {\frac {x}{3}} ^ {8 - x} \mathrm {d} y = \int_ {0} ^ {2} x ^ {2} \cdot \frac {8}{3} x \mathrm {d} x + \int_ {2} ^ {6} \left(8 - \frac {4}{3} x\right) x ^ {2} \mathrm {d} x \\ &= \frac {2}{3} x ^ {4} \left| _ {0} ^ {2} + \frac {8}{3} x ^ {3} \right| _ {2} ^ {6} - \frac {1}{3} x ^ {4} \left| _ {2} ^ {6} = \frac {4 1 6}{3}. \right. \end{aligned}</equation>（法二）在极坐标系下计算.

三条直线的方程分别为<equation>\theta=\arctan \frac{1}{3},</equation><equation>\theta=\arctan 3</equation>，以及<equation>r(\cos \theta+\sin \theta)=8.</equation>此时，区域D在极坐标系下的表示为<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \frac {8}{\cos \theta + \sin \theta}, \arctan \frac {1}{3} \leqslant \theta \leqslant \arctan 3 \right\}.</equation><equation>\begin{aligned} \iint_ {D} x ^ {2} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \iint_ {D} r ^ {2} \cos^ {2} \theta \cdot r \mathrm {d} r \mathrm {d} \theta &= \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} \cos^ {2} \theta \mathrm {d} \theta \int_ {0} ^ {\frac {8}{\cos \theta + \sin \theta}} r ^ {3} \mathrm {d} r \\ &= \frac {8 ^ {4}}{4} \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} \frac {\cos^ {2} \theta}{\left(\cos \theta + \sin \theta\right) ^ {4}} \mathrm {d} \theta = \frac {8 ^ {4}}{4} \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} \frac {1}{\left(1 + \tan \theta\right) ^ {4}} \cdot \sec^ {2} \theta \mathrm {d} \theta \\ \underline {{= u = \tan \theta}} \frac {8 ^ {4}}{4} \int_ {\frac {1}{3}} ^ {3} \frac {1}{(1 + u) ^ {4}} \mathrm {d} u &= \frac {8 ^ {4}}{4} \cdot \left(- \frac {1}{3}\right) \frac {1}{(1 + u) ^ {3}} \Big | _ {\frac {1}{3}} ^ {3} = \frac {4 1 6}{3}. \end{aligned}</equation>

---

**2012年第16题 | 解答题 | 10分**

16. (本题满分10分)

计算二重积分<equation>\iint_{D} \mathrm{e}^{x} x y \mathrm{d} x \mathrm{d} y</equation>，其中 D是以曲线<equation>y=\sqrt{x}, y=\frac{1}{\sqrt{x}}</equation>及 y轴为边界的无界区域.

**答案:**## (16)<equation>\frac{1}{2}.</equation>

**解析:**分析本题主要考查反常二重积分的计算。本题中的积分区域为无界区域，在计算时，写出无界区域的表示，将二重积分化为二次积分，最后得到一个反常积分。依照反常积分的计算方法求值即可。

解 将<equation>D</equation>看作X型区域，<equation>D = \left\{(x,y)\mid \sqrt{x}\leq y\leq \frac{1}{\sqrt{x}},0 < x\leq 1\right\}</equation>，则<equation>\begin{aligned} \iint_ {D} \mathrm {e} ^ {x} x y \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {1} \mathrm {d} x \int_ {\sqrt {x}} ^ {\frac {1}{\sqrt {x}}} \mathrm {e} ^ {x} x y \mathrm {d} y = \int_ {0} ^ {1} \frac {1}{2} \left(1 - x ^ {2}\right) \mathrm {e} ^ {x} \mathrm {d} x = \frac {1}{2} \int_ {0} ^ {1} \left(1 - x ^ {2}\right) \mathrm {d} \left(\mathrm {e} ^ {x}\right) \\ &= \frac {1}{2} \left[ \left(1 - x ^ {2}\right) \mathrm {e} ^ {x} \left| _ {0} ^ {1} + \int_ {0} ^ {1} 2 x \mathrm {e} ^ {x} \mathrm {d} x \right] \right. \\ &= \frac {1}{2} \left(- 1 + 2 x \mathrm {e} ^ {x} \left| _ {0} ^ {1} - 2 \int_ {0} ^ {1} \mathrm {e} ^ {x} \mathrm {d} x\right)\right) \\ &= \frac {1}{2} \left[ - 1 + 2 \mathrm {e} - 2 (\mathrm {e} - 1) \right] = \frac {1}{2}. \end{aligned}</equation>

---

**2010年第16题 | 解答题 | 10分**

16. (本题满分10分)

计算二重积分<equation>\iint_{D} ( x+y )^{3} \mathrm{d} x \mathrm{d} y</equation>，其中 D由曲线<equation>x=\sqrt{1+y^{2}}</equation>与直线<equation>x+\sqrt{2} y=0</equation>及<equation>x-\sqrt{2} y=0</equation>围成.

**答案:**## (16)<equation>\frac{1 4}{1 5}.</equation>

**解析:**分析本题主要考查二重积分的计算.通过观察发现，积分区域 D关于 x轴对称，因此我们可以利用积分区域的对称性以及被积函数的奇偶性来简化计算.

解如图所示，积分区域 D关于 x轴对称，故<equation>\iint_ {D} (x + y) ^ {3} \mathrm {d} x \mathrm {d} y = \iint_ {D} \left(x ^ {3} + 3 x ^ {2} y + 3 x y ^ {2} + y ^ {3}\right) \mathrm {d} x \mathrm {d} y = \iint_ {D} \left(x ^ {3} + 3 x y ^ {2}\right) \mathrm {d} x \mathrm {d} y.</equation>分别计算<equation>x = \sqrt{1 + y^2}</equation>与<equation>x = \sqrt{2} y, x = -\sqrt{2} y</equation>的交点得<equation>(\sqrt{2}, 1), (\sqrt{2}, -1)</equation>. 记<equation>D_{1}</equation>为区域<equation>D</equation>位于<equation>x</equation>轴以上的部分. 将<equation>D_{1}</equation>写为 Y 型区域.<equation>D_{1} = \{(x, y) \mid \sqrt{2} y \leqslant x \leqslant \sqrt{1 + y^2}, 0 \leqslant y \leqslant 1\}</equation>. 于是，<equation>\begin{aligned} \iint_ {D} (x + y) ^ {3} \mathrm {d} x \mathrm {d} y &= 2 \iint_ {D _ {1}} \left(x ^ {3} + 3 x y ^ {2}\right) \mathrm {d} x \mathrm {d} y = 2 \int_ {0} ^ {1} \mathrm {d} y \int_ {\sqrt {2} y} ^ {\sqrt {1 + y ^ {2}}} \left(x ^ {3} + 3 x y ^ {2}\right) \mathrm {d} x \\ &= 2 \left[ \int_ {0} ^ {1} \frac {\left(1 + y ^ {2}\right) ^ {2} - \left(2 y ^ {2}\right) ^ {2}}{4} \mathrm {d} y + \int_ {0} ^ {1} \frac {3 y ^ {2} \left(1 + y ^ {2} - 2 y ^ {2}\right)}{2} \mathrm {d} y \right] \\ &= \frac {1}{2} \int_ {0} ^ {1} \left(1 + 2 y ^ {2} - 3 y ^ {4}\right) \mathrm {d} y + 3 \int_ {0} ^ {1} \left(y ^ {2} - y ^ {4}\right) \mathrm {d} y = \int_ {0} ^ {1} \left(\frac {1}{2} + 4 y ^ {2} - \frac {9}{2} y ^ {4}\right) \mathrm {d} y \\ &= \frac {1}{2} + \frac {4}{3} - \frac {9}{1 0} = \frac {1 4}{1 5}. \end{aligned}</equation>

---

**2009年第17题 | 解答题 | 10分**

17. (本题满分10分)

计算二重积分<equation>\iint\limits_{D} ( x-y ) \mathrm{d} x \mathrm{d} y</equation>，其中<equation>D=\{(x,y)\mid(x-1)^{2}+(y-1)^{2}\leqslant 2,y\geqslant x\}</equation>

**答案:**<equation>(1 7) - \frac {8}{3}.</equation>

**解析:**<equation>D</equation>分析 本题主要考查二重积分的计算.由于积分区域为圆域的一部分，故可以考虑在极坐标系下进行计算.

点M的直角坐标(x,y)与极坐标（r，θ）满足<equation>\left\{ \begin{array}{l l} x = r\cos \theta , \\ y = r\sin \theta . \end{array} \right.</equation>若在极坐标系下计算，则有公式<equation>\iint_ {D} f (x, y) \mathrm {d} \sigma = \iint_ {D} f (r \cos \theta , r \sin \theta) r \mathrm {d} r \mathrm {d} \theta ,</equation>其中<equation>r\mathrm{d}r\mathrm{d}\theta</equation>为极坐标系中的面积元素.

解如图所示，作极坐标变换<equation>\left\{ \begin{array}{l l} x = r\cos \theta , \\ y = r\sin \theta , \end{array} \right.</equation>则圆方程<equation>(x - 1)^{2}</equation><equation>+ (y - 1)^{2} = 2</equation>变成<equation>r = 2(\cos \theta +\sin \theta)</equation>，从而D在极坐标系下表示为<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2 (\cos \theta + \sin \theta), \frac {\pi}{4} \leqslant \theta \leqslant \frac {3 \pi}{4} \right\}.</equation>因此，<equation>\begin{aligned} \iint_ {D} (x - y) \mathrm {d} x \mathrm {d} y &= \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} (\cos \theta - \sin \theta) \mathrm {d} \theta \int_ {0} ^ {2 (\cos \theta + \sin \theta)} r ^ {2} \mathrm {d} r = \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} (\cos \theta - \sin \theta) \left[ \frac {r ^ {3}}{3} \right| _ {0} ^ {2 (\cos \theta + \sin \theta)} \mathrm {d} \theta \\ &= \frac {8}{3} \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} (\cos \theta + \sin \theta) ^ {2} \left(\cos^ {2} \theta - \sin^ {2} \theta\right) \mathrm {d} \theta = \frac {8}{3} \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} (1 + \sin 2 \theta) \cos 2 \theta \mathrm {d} \theta \\ \underline {{= u = \sin 2 \theta}} \frac {4}{3} \int_ {1} ^ {- 1} (1 + u) \mathrm {d} u &= - \frac {8}{3}. \end{aligned}</equation>或者也可以这样计算.<equation>\begin{aligned} \iint_ {D} (x - y) \mathrm {d} x \mathrm {d} y &= \frac {8}{3} \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} \left(\cos \theta + \sin \theta\right) ^ {3} \left(\cos \theta - \sin \theta\right) \mathrm {d} \theta = \frac {8}{3} \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} \left(\cos \theta + \sin \theta\right) ^ {3} \mathrm {d} \left(\cos \theta + \sin \theta\right) \\ &= \frac {2}{3} \left(\cos \theta + \sin \theta\right) ^ {4} \Bigg | _ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} = - \frac {8}{3}. \end{aligned}</equation>

---


#### 多元函数微分学的几何应用

**2024年第13题 | 填空题 | 5分**

13. 函数<equation>f(x,y)=2x^{3}-9x^{2}-6y^{4}+12x+24y</equation>的极值点是 ___

**答案:**## (1,1)

**解析:**解 计算 f(x,y) 的驻点.

整理<equation>\left\{\begin{array}{l l}f_{x}^{\prime}(x,y)=6x^{2}-18x+12=0\\ f_{y}^{\prime}(x,y)=-24y^{3}+24=0\end{array}\right.</equation>可得<equation>\left\{\begin{array}{l l}x^{2}-3x+2=0\\ y^{3}-1=0,\end{array}\right.</equation>解得<equation>\left\{\begin{array}{l l}x=1,\\ y=1,\end{array}\right.</equation>或<equation>\left\{\begin{array}{l l}x=2,\\ y=1,\end{array}\right.</equation>即<equation>f(x,y)</equation>的全部驻点为点（1，1），（2，1）.

计算 f（x,y）的二阶偏导数.<equation>f _ {x x} ^ {\prime \prime} (x, y) = 1 2 x - 1 8, f _ {x y} ^ {\prime \prime} (x, y) = 0, f _ {y y} ^ {\prime \prime} (x, y) = - 7 2 y ^ {2}.</equation>对点（1,1），<equation>A=f_{x x}^{\prime \prime}(1,1)=-6,B=f_{x y}^{\prime \prime}(1,1)=0,C=f_{y y}^{\prime \prime}(1,1)=-72,AC-B^{2}=(-6)\times</equation>（-72）-0>0，且<equation>A<0</equation>，故由二元函数极值存在的充分条件可知，点（1,1）是<equation>f(x,y)</equation>的极大值点.

对点（2,1），<equation>A=f_{xx}^{\prime \prime}(2,1)=6,B=f_{xy}^{\prime \prime}(2,1)=0,C=f_{yy}^{\prime \prime}(2,1)=-72,AC-B^{2}=6\times(-72)</equation><equation>- 0 < 0</equation>，故由二元函数极值存在的充分条件可知，点（2,1）不是<equation>f(x,y)</equation>的极值点.

因此，<equation>f(x,y)</equation>的唯一极值点为（1，1）.

---

**2021年第18题 | 解答题 | 12分**

18. (本题满分12分)

求函数<equation>f ( x,y)=2 \ln | x |+\frac{(x-1)^{2}+y^{2}}{2 x^{2}}</equation>的极值

的极值.

**答案:**（-1,0）为 f(x,y)的极小值点，极小值为 f(-1,0) = 2.<equation>\left(\frac{1}{2},0\right)</equation>为 f(x,y)的极小值点，极小值为<equation>f\left(\frac{1}{2},0\right)=-2\ln 2+\frac{1}{2}.</equation>

**解析:**解 先求驻点坐标. 计算<equation>f_{x}^{\prime}(x,y)</equation>与<equation>f_{y}^{\prime}(x,y).</equation><equation>\begin{array}{l} f _ {x} ^ {\prime} (x, y) = \frac {2}{x} + \frac {2 (x - 1) \cdot 2 x ^ {2} - [ (x - 1) ^ {2} + y ^ {2} ] \cdot 4 x}{4 x ^ {4}} \\ = \frac {2}{x} + \frac {(x - 1) \cdot x - (x - 1) ^ {2} - y ^ {2}}{x ^ {3}} \\ = \frac {2 x ^ {2} + x - 1 - y ^ {2}}{x ^ {3}}. \\ \end{array}</equation><equation>f _ {y} ^ {\prime} (x, y) = \frac {2 y}{2 x ^ {2}} = \frac {y}{x ^ {2}}.</equation>令<equation>\left\{\begin{array}{l l} {\frac{2x^{2}+x-1-y^{2}}{x^{3}}=0,} \\ {\frac{y}{x^{2}}=0,} \\ \end{array} \right.</equation>解得 y=0,x=<equation>\frac{1}{2}</equation>或 x=-1.于是，f(x,y)有两个驻点 (-1,0),<equation>\left(\frac{1}{2},0\right).</equation>分别计算 f（x,y）的二阶偏导数.<equation>\begin{array}{l} f _ {x x} ^ {\prime \prime} (x, y) = \frac {(4 x + 1) \cdot x ^ {3} - \left(2 x ^ {2} + x - 1 - y ^ {2}\right) \cdot 3 x ^ {2}}{x ^ {6}} \\ = \frac {(4 x + 1) \cdot x - 3 \left(2 x ^ {2} + x - 1 - y ^ {2}\right)}{x ^ {4}} \\ = \frac {- 2 x ^ {2} - 2 x + 3 + 3 y ^ {2}}{x ^ {4}}. \\ \end{array}</equation><equation>f _ {x y} ^ {\prime \prime} (x, y) = - \frac {2 y}{x ^ {3}}.</equation><equation>f _ {y y} ^ {\prime \prime} (x, y) = \frac {1}{x ^ {2}}.</equation>(1) 对驻点（-1，0），计算得 A=3,B=0,C=1. 从而<equation>A C-B^{2}>0</equation>，且 A > 0 ，故（-1，0）为<equation>f(x,y)</equation>的极小值点，极小值为<equation>f(-1,0)=2.</equation>(2) 对驻点<equation>\left(\frac{1}{2},0\right)</equation>，计算得 A=24,B=0,C=4.从而<equation>AC-B^{2}>0</equation>，且 A>0，故<equation>\left(\frac{1}{2},0\right)</equation>为<equation>f(x,y)</equation>的极小值点，极小值为<equation>f\left(\frac{1}{2},0\right)=-2\ln 2+\frac{1}{2}.</equation>

---

**2020年第16题 | 解答题 | 10分**

16. (本题满分10分)

求函数<equation>f ( x,y)=x^{3}+8 y^{3}-x y</equation>的极值.

**答案:**极小值为<equation>f\left(\frac{1}{6},\frac{1}{12}\right)=- \frac{1}{216}.</equation>

**解析:**解<equation>\left\{ \begin{array}{l l} f_{x}^{\prime}(x,y)=3x^{2}-y=0, \\ f_{y}^{\prime}(x,y)=24y^{2}-x=0. \end{array} \right.</equation>将 y=3x²代入24y²-x=0可得216x4=x，解得x=0或x<equation>=\frac{1}{6}.</equation>于是，<equation>\left\{ \begin{array}{l l} x=0, \\ y=0 \end{array} \right.</equation>或<equation>\left\{ \begin{array}{l l} x=\frac{1}{6}, \\ y=\frac{1}{12}. \end{array} \right.</equation><equation>f(x,y)</equation>有两个驻点(0,0)，<equation>\left(\frac{1}{6},\frac{1}{12}\right).</equation><equation>\textcircled{2}</equation>计算 f(x,y)的二阶偏导数.<equation>f_{xx}^{\prime\prime}(x,y)=6x,</equation><equation>f_{xy}^{\prime\prime}(x,y)=-1,</equation><equation>f_{yy}^{\prime\prime}(x,y)=48y.</equation><equation>\textcircled{3}</equation>判断驻点是否为极值点以及确定极值点类型.

• 考虑驻点(0,0).<equation>A=f_{xx}^{\prime\prime}(0,0)=0,</equation><equation>B=f_{xy}^{\prime\prime}(0,0)=-1,</equation><equation>C=f_{yy}^{\prime\prime}(0,0)=0.</equation><equation>AC-B^{2}=0-1=-1<0</equation>，故点(0,0)不是极值点.

• 考虑驻点<equation>\left(\frac{1}{6},\frac{1}{12}\right).</equation><equation>A=f_{xx}^{\prime\prime}\left(\frac{1}{6},\frac{1}{12}\right)=1,</equation><equation>B=f_{xy}^{\prime\prime}\left(\frac{1}{6},\frac{1}{12}\right)=-1,</equation><equation>C=f_{yy}^{\prime\prime}\left(\frac{1}{6},\frac{1}{12}\right)=4.</equation><equation>AC-B^{2}=4-1=3>0</equation>，且 A>0，故点<equation>\left(\frac{1}{6},\frac{1}{12}\right)</equation>为极小值点，极小值为<equation>f\left(\frac{1}{6},\frac{1}{12}\right)=\frac{1}{6^{3}}+\frac{8}{12^{3}}-\frac{1}{6\times 12}=-\frac{1}{216}.</equation>

---

**2018年第17题 | 解答题 | 10分**

17. (本题满分10分)

将长为2m的铁丝分成三段，依次围成圆、正方形与正三角形. 三个图形的面积之和是否存在最小值？若存在，求出最小值.

**答案:**三个图形的面积之和存在最小值，最小值为<equation>\frac{1}{\pi+4+3\sqrt{3}}.</equation>

**解析:**解设圆、正方形、正三角形的周长分别为 x,y,z，则圆的半径<equation>r=\frac{x}{2\pi}</equation>正方形的边长 a<equation>=\frac{y}{4}</equation>正三角形的边长 b<equation>=\frac{z}{3}</equation>.于是，三个图形的面积之和为<equation>S (x, y, z) = \pi \cdot \left(\frac {x}{2 \pi}\right) ^ {2} + \left(\frac {y}{4}\right) ^ {2} + \frac {1}{2} \cdot \left(\frac {z}{3}\right) ^ {2} \cdot \sin \frac {\pi}{3} = \frac {x ^ {2}}{4 \pi} + \frac {y ^ {2}}{1 6} + \frac {\sqrt {3}}{3 6} z ^ {2}.</equation>由于三段铁丝的周长之和为2，故<equation>x+y+z=2.</equation>建立拉格朗日函数<equation>L ( x,y,z,\lambda) = \frac{x^{2}}{4\pi} +\frac{y^{2}}{16} +\frac{\sqrt{3}}{36} z^{2} +\lambda ( x+y+z-2).</equation>令<equation>\left\{ \begin{array}{l} L _ {x} ^ {\prime} = \frac {1}{2 \pi} x + \lambda = 0, \\ L _ {y} ^ {\prime} = \frac {1}{8} y + \lambda = 0, \\ L _ {z} ^ {\prime} = \frac {\sqrt {3}}{1 8} z + \lambda = 0, \\ L _ {\lambda} ^ {\prime} = x + y + z - 2 = \end{array} \right.</equation>由前三个方程可得<equation>x = -2\pi \lambda ,y = -8\lambda ,z = -6\sqrt{3}\lambda .</equation>代入 x+y+z-2=0可得<equation>\lambda = - \frac {2}{2 \pi + 8 + 6 \sqrt {3}} = - \frac {1}{\pi + 4 + 3 \sqrt {3}}.</equation>于是，<equation>x=\frac{2\pi}{\pi+4+3\sqrt{3}}, y=\frac{8}{\pi+4+3\sqrt{3}}, z=\frac{6\sqrt{3}}{\pi+4+3\sqrt{3}}.</equation>将所得 x,y,z的值代入 S（x，y，z）可得<equation>S (x, y, z) = \frac {\pi + 4 + 3 \sqrt {3}}{(\pi + 4 + 3 \sqrt {3}) ^ {2}} = \frac {1}{\pi + 4 + 3 \sqrt {3}}.</equation>为了判定所求得可能的极值点是否为最小值点，我们把问题转化为目标函数 S（x，y，z）在有界闭区域 D = {（x，y，z）| x+y+z=2，x≥0，y≥0，z≥0}上的最值问题.

由于连续函数在有界闭区域上一定能取到最值，故若我们能分别计算出<equation>S ( x, y, z )</equation>在边界<equation>y + z = 2, z + x = 2, x + y = 2</equation>上的最值，再与<equation>\frac{1} {\pi+4+3 \sqrt{3}}</equation>比较，则所得最小值即为区域D上的最小值当 x=0时，<equation>S ( 0, y, z )</equation>在 y+z=2下的最小值为<equation>S \left( 0, \frac{8}{4+3 \sqrt{3}}, \frac{6 \sqrt{3}}{4+3 \sqrt{3}} \right)=\frac{1}{4+3 \sqrt{3}}.</equation>当 y=0时，<equation>S ( x, 0, z )</equation>在 x+z=2下的最小值为<equation>S \left( \frac{2 \pi}{\pi+3 \sqrt{3}}, 0, \frac{6 \sqrt{3}}{\pi+3 \sqrt{3}} \right)=\frac{1}{\pi+3 \sqrt{3}}.</equation>当 z=0时，<equation>S ( x, y, 0 )</equation>在 x+y=2下的最小值为<equation>S \left( \frac{2 \pi}{\pi+4}, \frac{8}{\pi+4}, 0 \right)=\frac{1}{\pi+4}.</equation>4个值比较可得，<equation>\frac{1} {\pi+4+3 \sqrt{3}}</equation>为整个区域D上的最小值，也为 x+y+z=2,x>0,y>0，z>0时的 S(x,y,z)的最小值.三个图形的面积之和存在最小值，最小值为<equation>\frac{1} {\pi+4+3 \sqrt{3}}.</equation>

---

**2017年第2题 | 选择题 | 4分 | 答案: D**

2. 二元函数 z=xy（3-x-y）的极值点是（    ）

A. (0,0) B. (0,3) C. (3,0) D. (1,1)

答案: D

**解析:**解 先求驻点坐标.计算<equation>\frac{\partial z}{\partial x}</equation>与<equation>\frac{\partial z}{\partial y}.</equation><equation>\frac {\partial z}{\partial x} = - y ^ {2} - 2 x y + 3 y = y (3 - 2 x - y),</equation><equation>\frac {\partial z}{\partial y} = - x ^ {2} - 2 x y + 3 x = x (3 - x - 2 y).</equation>解<equation>\left\{\begin{array}{l l}y(3-2x-y)=0,\\ x(3-x-2y)=0,\end{array} \right.</equation>得4组解：<equation>\left\{ \begin{array}{l l} x = 0, \\ y = 0, \end{array} \right. \quad \left\{ \begin{array}{l l} x = 0, \\ y = 3, \end{array} \right. \quad \left\{ \begin{array}{l l} x = 3, \\ y = 0, \end{array} \right. \quad \left\{ \begin{array}{l l} x = 1, \\ y = 1. \end{array} \right.</equation>计算 z的二阶偏导数得<equation>\frac {\partial^ {2} z}{\partial x ^ {2}} = - 2 y, \quad \frac {\partial^ {2} z}{\partial y ^ {2}} = - 2 x, \quad \frac {\partial^ {2} z}{\partial x \partial y} = 3 - 2 x - 2 y.</equation>当（x,y）=（0,0）或（3,0）或（0,3）时，<equation>\frac{\partial^{2}z}{\partial x^{2}}\frac{\partial^{2}z}{\partial y^{2}}-\left(\frac{\partial^{2}z}{\partial x\partial y}\right)^{2}<0</equation>，故这三个点都不是极值点当（x,y）=（1,1）时，<equation>\frac {\partial^ {2} z}{\partial x ^ {2}} \frac {\partial^ {2} z}{\partial y ^ {2}} - \left(\frac {\partial^ {2} z}{\partial x \partial y}\right) ^ {2} = 4 - 1 = 3 > 0, \quad \frac {\partial^ {2} z}{\partial x ^ {2}} = - 2 < 0.</equation>因此，点（1，1）是极大值点.应选D.

---

**2012年第17题 | 解答题 | 10分**


某企业为生产甲、乙两种型号的产品投入的固定成本为10000(万元).设该企业生产甲、乙两种产品的产量分别为 x (件)和 y (件)，且这两种产品的边际成本分别为<equation>2 0+\frac { x } { 2 }</equation>(万元/件)与<equation>6+y</equation>(万元/件).

I. 求生产甲、乙两种产品的总成本函数 C(x,y) (万元).

II. 当总产量为50件时，甲、乙两种产品的产量各为多少时可使总成本最小？求最小总成本.

III. 求总产量为50件且总成本最小时甲产品的边际成本，并解释其经济意义.

**答案:**(17) ( I )<equation>C ( x,y)=2 0 x+\frac{x^{2}}{4}+6 y+\frac{y^{2}}{2}+1 0 0 0 0.</equation>（Ⅱ）若总产量为50件，则当甲种产品的产量为24件，乙种产品的产量为26件时，总成本最小，最小成本为<equation>C ( 2 4, 2 6 ) = 1 1 1 1 8</equation>万元.

（Ⅲ）当总产量为50件且总成本最小时，甲种产品的边际成本为32万元。其经济意义为，当甲、乙两种产品的产量分别为24件，26件时，若甲种产品的产量再增加1件，则总成本增加32万元，即当乙种产品的产量为26件时，生产第25件甲种产品需要32万元.

**解析:**（I）由边际成本的定义及题设知<equation>\frac {\partial C (x , y)}{\partial x} = 2 0 + \frac {x}{2},</equation><equation>\frac {\partial C (x , y)}{\partial y} = 6 + y.</equation>由（1）式知<equation>C ( x,y)=2 0 x+\frac{x^{2}}{4}+f ( y )</equation>，其中<equation>f ( y )</equation>为关于y的待定函数.将<equation>C ( x,y)</equation>的表达式代入（2）式得<equation>f^{\prime}(y)=6+y.</equation>于是<equation>f ( y ) = 6 y + \frac{y^{2}}{2} + a</equation>其中a为待定常数.因此，<equation>C (x, y) = 2 0 x + \frac {x ^ {2}}{4} + 6 y + \frac {y ^ {2}}{2} + a.</equation>又由题设知<equation>C(0,0) = 10000</equation>，代入上式得到<equation>a = 10000</equation>，故<equation>C (x, y) = 2 0 x + \frac {x ^ {2}}{4} + 6 y + \frac {y ^ {2}}{2} + 1 0 0 0 0.</equation>（Ⅱ）（法一）由题设知<equation>x+y=50</equation>，于是<equation>\begin{array}{l} C (x, y) = C (x, 5 0 - x) = 2 0 x + \frac {x ^ {2}}{4} + 6 (5 0 - x) + \frac {(5 0 - x) ^ {2}}{2} + 1 0 0 0 0 \\ = \frac {3}{4} x ^ {2} - 3 6 x + 1 1 5 5 0 = \frac {3}{4} (x - 2 4) ^ {2} + 1 1 1 1 8. \\ \end{array}</equation>从而当<equation>x = 24</equation>时，<equation>C(x,y)</equation>取值最小且最小值为11118，此时<equation>y = 26.</equation>因此，若总产量为50件，则当甲种产品的产量为24件，乙种产品的产量为26件时，总成本最小，最小成本为11118万元.

（法二）由题设知，要求<equation>C(x,y)</equation>在<equation>x + y = 50</equation>的条件下的最值，我们可以采用拉格朗日乘数法.

作拉格朗日函数<equation>L(x,y,\lambda) = C(x,y) + \lambda (x + y - 50)</equation>，令<equation>\left\{ \begin{array}{l} L _ {x} ^ {\prime} = \frac {\partial C (x , y)}{\partial x} + \lambda = 2 0 + \frac {x}{2} + \lambda = 0, \\ L _ {y} ^ {\prime} = \frac {\partial C (x , y)}{\partial y} + \lambda = 6 + y + \lambda = 0, \\ L _ {\lambda} ^ {\prime} = x + y - 5 0 = 0. \end{array} \right.</equation>解得 x=24，y=26，这是唯一可能的极值点.因为由问题本身可知最小值一定存在，所以最小值在这个可能的极值点处取得.

因此，若总产量为50件，则当甲种产品的产量为24件，乙种产品的产量为26件时，总成本最小，最小成本为<equation>C (2 4, 2 6) = 1 1 1 1 8 (\text {万 元}).</equation>（Ⅲ）由边际成本的定义知，当总产量为50件且总成本最小时，甲种产品的边际成本为<equation>\left. \frac {\partial C}{\partial x} \right| _ {(2 4, 2 6)} = \left(2 0 + \frac {x}{2}\right) \Big | _ {(2 4, 2 6)} = 2 0 + \frac {2 4}{2} = 3 2 (\text {万 元}).</equation>其经济意义为，当甲、乙两种产品的产量分别为24件，26件时，若甲种产品的产量再增加1件，则总成本增加32万元，即当乙种产品的产量为26件时，生产第25件甲种产品需要32万元.

---

**2010年第17题 | 解答题 | 10分**

17. (本题满分10分)

求函数<equation>u=xy+2yz</equation>在约束条件<equation>x^{2}+y^{2}+z^{2}=1 0</equation>下的最大值和最小值.

**答案:**## （17）最大值为<equation>5\sqrt{5}</equation>最小值为<equation>- 5\sqrt{5}.</equation>

**解析:**作拉格朗日函数<equation>L ( x,y,z,\lambda) = x y+2 y z+\lambda \left( x^{2}+y^{2}+z^{2}-1 0 \right)</equation>，其中<equation>\lambda</equation>为参数.令<equation>\left[ L _ {x} ^ {\prime} = y + 2 \lambda x = 0, \right.</equation><equation>\left| L _ {y} ^ {\prime} = x + 2 z + 2 \lambda y = 0, \right.</equation><equation>L _ {z} ^ {\prime} = 2 y + 2 \lambda z = 0,</equation><equation>\left[ L _ {\lambda} ^ {\prime} = x ^ {2} + y ^ {2} + z ^ {2} - 1 0 = 0. \right.</equation>解得所有可能的最值点为<equation>(1, -\sqrt{5}, 2), (1, \sqrt{5}, 2), (-1, \sqrt{5}, -2), (-1, -\sqrt{5}, -2), (-2\sqrt{2}, 0, \sqrt{2}), (2\sqrt{2}, 0, -\sqrt{2})</equation>.代入<equation>u</equation>的表达式中得，<equation>u (1, - \sqrt {5}, 2) = u (- 1, \sqrt {5}, - 2) = - 5 \sqrt {5},</equation><equation>u (1, \sqrt {5}, 2) = u (- 1, - \sqrt {5}, - 2) = 5 \sqrt {5},</equation><equation>u \left(- 2 \sqrt {2}, 0, \sqrt {2}\right) = u \left(2 \sqrt {2}, 0, - \sqrt {2}\right) = 0.</equation>因此，所求最大值为<equation>5\sqrt{5}</equation>，最小值为<equation>-5\sqrt{5}</equation>.

---

**2009年第15题 | 解答题 | 10分**

15. (本题满分9分）

求二元函数<equation>f ( x,y)=x^{2}(2+y^{2})+y\ln y</equation>的极值.

**答案:**(15)<equation>f ( x,y )</equation>在点<equation>\left( 0,\frac{1} {\mathrm{e}} \right)</equation>处取得极小值<equation>f \left( 0,\frac{1} {\mathrm{e}} \right)=-\frac{1} {\mathrm{e}}.</equation>

**解析:**解 令<equation>\left\{ \begin{array}{l l} f_{x}^{\prime}(x,y)=2 x(2+y^{2})=0, \\ f_{y}^{\prime}(x,y)=2 x^{2} y+\ln y+1=0, \end{array} \right.</equation>解得驻点为<equation>\left( 0, \frac{1} {\mathrm{e}} \right). f(x,y)</equation>的二阶偏导数为<equation>f_{xx}^{\prime \prime}(x,y)=2(2+y^{2}),</equation><equation>f_{xy}^{\prime \prime}(x,y)=4 x y,</equation><equation>f_{yy}^{\prime \prime}(x,y)=2 x^{2}+\frac{1}{y}.</equation>于是<equation>A=f_{xx}^{\prime \prime}\left( 0, \frac{1} {\mathrm{e}} \right)=2\left( 2+\frac{1} {\mathrm{e}^{2}} \right),</equation><equation>B=f_{xy}^{\prime \prime}\left( 0, \frac{1} {\mathrm{e}} \right)=0,</equation><equation>C=f_{yy}^{\prime \prime}\left( 0, \frac{1} {\mathrm{e}} \right)=\mathrm{e}.</equation>由于<equation>AC-B^{2}>0, A>0,</equation>故<equation>f(x,y)</equation>在点<equation>\left( 0, \frac{1} {\mathrm{e}} \right)</equation>处取得极小值<equation>f\left( 0, \frac{1} {\mathrm{e}} \right)=-\frac{1} {\mathrm{e}}.</equation>

---


#### 全微分的概念与计算

**2023年第12题 | 填空题 | 5分**

12. 已知函数 f(x,y)满足<equation>\mathrm{d} f(x,y)=\frac{x\mathrm{d} y-y\mathrm{d} x}{x^{2}+y^{2}}, f(1,1)=\frac{\pi}{4}</equation>，则 f<equation>(\sqrt{3},3)=</equation>___.

**答案:**##<equation>\frac{\pi}{3}</equation>

**解析:**解 由<equation>\mathrm{d}f(x,y)=\frac{x\mathrm{d}y-y\mathrm{d}x}{x^{2}+y^{2}}</equation>可知，<equation>f_{x}^{\prime}(x,y)=\frac{-y}{x^{2}+y^{2}},f_{y}^{\prime}(x,y)=\frac{x}{x^{2}+y^{2}}.</equation>于是，当<equation>y > 0</equation>时，<equation>f (x, y) = \int f _ {x} ^ {\prime} (x, y) \mathrm {d} x = \int \frac {- y}{x ^ {2} + y ^ {2}} \mathrm {d} x = - \int \frac {\mathrm {d} \left(\frac {x}{y}\right)}{1 + \left(\frac {x}{y}\right) ^ {2}} = - \arctan \frac {x}{y} + \varphi (y),</equation>其中<equation>\varphi(y)</equation>为关于 y的一元函数.实际上，<equation>\varphi(y)=f(0,y).</equation>对 f(x,y）=-arctan<equation>\frac{x}{y}+\varphi(y)</equation>关于 y求偏导数可得<equation>f _ {y} ^ {\prime} (x, y) = - \frac {- \frac {x}{y ^ {2}}}{1 + \left(\frac {x}{y}\right) ^ {2}} + \varphi^ {\prime} (y) = \frac {x}{x ^ {2} + y ^ {2}} + \varphi^ {\prime} (y).</equation>比较可得<equation>\varphi^{\prime}(y)=0</equation>，从而当 y > 0时，<equation>\varphi(y)=C,f(x,y)=-\arctan \frac{x}{y}+C</equation>，其中 C为待定常数.

由<equation>f(1,1)=\frac{\pi}{4}</equation>可得，<equation>\frac{\pi}{4}=-\frac{\pi}{4}+C</equation>，解得 C<equation>=\frac{\pi}{2}.</equation>因此，<equation>f(x,y)=-\arctan \frac{x}{y}+\frac{\pi}{2}.</equation>进一步可得<equation>f (\sqrt {3}, 3) = - \arctan \frac {1}{\sqrt {3}} + \frac {\pi}{2} = \frac {\pi}{2} - \frac {\pi}{6} = \frac {\pi}{3}.</equation>

---

**2021年第4题 | 选择题 | 5分 | 答案: C**

4. 设函数 f(x,y)可微，且<equation>f ( x+1, \mathrm{e}^{x} )=x ( x+1 )^{2}, f ( x, x^{2} )=2 x^{2} \ln x</equation>，则<equation>\mathrm{d} f ( 1, 1 )=</equation>(    )

A.<equation>\mathrm{d} x+\mathrm{d} y</equation>B.<equation>\mathrm{d} x-\mathrm{d} y</equation>C.<equation>\mathrm{d} y</equation>D.<equation>-\mathrm{d} y</equation>

答案: C

**解析:**根据全微分的定义，<equation>\mathrm {d} f (1, 1) = f _ {1} ^ {\prime} (1, 1) \mathrm {d} x + f _ {2} ^ {\prime} (1, 1) \mathrm {d} y.</equation>对<equation>f ( x+1,\mathrm{e}^{x} )=x ( x+1 )^{2}, f ( x,x^{2} )=2 x^{2} \ln x</equation>两端均关于 x求导，可得<equation>f _ {1} ^ {\prime} \left(x + 1, \mathrm {e} ^ {x}\right) + f _ {2} ^ {\prime} \left(x + 1, \mathrm {e} ^ {x}\right) \cdot \mathrm {e} ^ {x} = (x + 1) ^ {2} + x \cdot 2 (x + 1) = (x + 1) (3 x + 1).</equation><equation>f _ {1} ^ {\prime} \left(x, x ^ {2}\right) + f _ {2} ^ {\prime} \left(x, x ^ {2}\right) \cdot 2 x = 4 x \ln x + 2 x ^ {2} \cdot \frac {1}{x} = 2 x \left(2 \ln x + 1\right).</equation>在（1）式中令<equation>x=0</equation>，可得<equation>f_{1}^{\prime}(1,1)+f_{2}^{\prime}(1,1)=1.</equation>在（2）式中令<equation>x=1</equation>，可得<equation>f_{1}^{\prime}(1,1)+ 2 f_{2}^{\prime}(1,1)=2.</equation>联立两式解得<equation>f_{1}^{\prime}(1,1)=0,f_{2}^{\prime}(1,1)=1.</equation>因此，<equation>\mathrm{d}f(1,1)=\mathrm{d}y.</equation>应选C.

---

**2020年第9题 | 填空题 | 4分**

9. 设<equation>z=\arctan[xy+\sin(x+y)]</equation>，则<equation>\mathrm{d}z|_{(0,\pi)}=</equation>___.

**答案:**<equation>(\pi - 1) \mathrm {d} x - \mathrm {d} y.</equation>

**解析:**根据链式法则，<equation>\frac{\partial z}{\partial x}=\frac{y+\cos(x+y)}{1+\left[ x y+\sin(x+y)\right]^{2}},</equation><equation>\frac{\partial z}{\partial y}=\frac{x+\cos(x+y)}{1+\left[ x y+\sin(x+y)\right]^{2}}.</equation>代入<equation>x=0,y=\pi</equation>，可得<equation>\frac{\partial z}{\partial x}\bigg|_{(0,\pi)}=\pi-1, \frac{\partial z}{\partial y}\bigg|_{(0,\pi)}=-1.</equation>因此，<equation>\mathrm{d}z\bigg|_{(0,\pi)}=(\pi-1)\mathrm{d}x-\mathrm{d}y.</equation>

---

**2017年第12题 | 填空题 | 4分**

12. 设函数<equation>f(x,y)</equation>具有一阶连续偏导数，且<equation>\mathrm{d} f(x,y)=y \mathrm{e}^{y} \mathrm{d} x+x(1+y) \mathrm{e}^{y} \mathrm{d} y,f(0,0)=0</equation>，则<equation>f(x,y)=</equation>___

**答案:**##<equation>x y \mathrm{e}^{y}.</equation>

**解析:**由于<equation>\mathrm {d} f (x, y) = y \mathrm {e} ^ {y} \mathrm {d} x + x (1 + y) \mathrm {e} ^ {y} \mathrm {d} y,</equation>故<equation>f_x^{\prime}(x,y) = y\mathrm{e}^{y}, f_y^{\prime}(x,y) = x(1 + y)\mathrm{e}^{y}.</equation>对<equation>f_{x}^{\prime}(x,y)</equation>关于 x积分，得<equation>f (x, y) = \int f _ {x} ^ {\prime} (x, y) \mathrm {d} x = \int y \mathrm {e} ^ {y} \mathrm {d} x = x y \mathrm {e} ^ {y} + \varphi (y),</equation>其中<equation>\varphi(y)</equation>为关于 y的一元函数.

对<equation>x y \mathrm{e}^{y}+\varphi(y)</equation>关于y求偏导数，得<equation>\frac {\partial \left[ x y \mathrm {e} ^ {y} + \varphi (y) \right]}{\partial y} = x \mathrm {e} ^ {y} + x y \mathrm {e} ^ {y} + \varphi^ {\prime} (y) = x (1 + y) \mathrm {e} ^ {y} + \varphi^ {\prime} (y).</equation>与<equation>f_{y}^{\prime}(x,y)</equation>比较，得<equation>\varphi^{\prime}(y) = 0</equation>，故<equation>\varphi(y)\equiv C</equation>，其中C为常数.

代入<equation>x = 0</equation>，<equation>y = 0</equation>，得<equation>f(0,0) = 0 + C.</equation>于是，<equation>C = 0.</equation>因此，<equation>f ( x,y)= x y \mathrm{e}^{y}.</equation>

---

**2016年第11题 | 填空题 | 4分**

11. 设函数 f(u,v) 可微，z=z(x,y) 由方程<equation>( x+1 ) z-y^{2}=x^{2} f ( x-z,y )</equation>确定，则<equation>\mathrm{d} z |_{(0,1)}=</equation>___

**答案:**## dx + 2dy.

**解析:**（法一）对已知方程两端分别关于 x，y求偏导数，可得<equation>z + (x + 1) \frac {\partial z}{\partial x} = 2 x f (x - z, y) + x ^ {2} \left[ f _ {1} ^ {\prime} (x - z, y) \cdot \left(1 - \frac {\partial z}{\partial x}\right) \right].</equation><equation>(x + 1) \frac {\partial z}{\partial y} - 2 y = x ^ {2} \left[ f _ {1} ^ {\prime} (x - z, y) \cdot \left(- \frac {\partial z}{\partial y}\right) + f _ {2} ^ {\prime} (x - z, y) \right].</equation>将（x,y）=（0,1）代入已知方程，可得 z-1=0，从而 z(0,1)=1.再将（x,y,z）=（0,1,1）代入（1）、（2）两式，可得<equation>\frac{\partial z}{\partial x}\bigg|_{(0,1)}=-1, \frac{\partial z}{\partial y}\bigg|_{(0,1)}=2.</equation>因此，<equation>\mathrm{d} z \bigg|_{(0,1)}=-\mathrm{d} x+2 \mathrm{d} y</equation><equation>\mathrm {d} z \mid_ {(0, 1)} = - \mathrm {d} x + 2 \mathrm {d} y.</equation>（法二）对已知方程两端微分，可得<equation>\mathrm{d}[(x+1)z]-\mathrm{d}(y^{2})=\mathrm{d}[x^{2}f(x-z,y)]</equation>.进一步可得，<equation>\begin{aligned} (x + 1) \mathrm {d} z + z \mathrm {d} x - 2 y \mathrm {d} y &= f (x - z, y) \mathrm {d} \left(x ^ {2}\right) + x ^ {2} \mathrm {d} \left[ f (x - z, y) \right] \\ &= 2 x f (x - z, y) \mathrm {d} x + x ^ {2} \mathrm {d} \left[ f (x - z, y) \right]. \end{aligned}</equation>将（x,y）=（0,1）代入已知方程，可得 z-1=0，从而 z（0,1）=1.代入上式可得<equation>\mathrm {d} z + \mathrm {d} x - 2 \mathrm {d} y = 0,</equation>即<equation>\mathrm{d}z\mid_{(0,1)} = -\mathrm{d}x + 2\mathrm{d}y.</equation>

---

**2015年第11题 | 填空题 | 4分**

11. 若函数<equation>z = z(x,y)</equation>由方程<equation>\mathrm{e}^{x+2y+3z} + xyz = 1</equation>确定，则<equation>\mathrm{d}z|_{(0,0)} =</equation>___

**答案:**<equation>- \frac {1}{3} \mathrm {d} x - \frac {2}{3} \mathrm {d} y.</equation>

**解析:**解下面我们分别用上述三种方法解本题.

（法一）对原方程两端分别关于 x,y求偏导数，可得<equation>\mathrm {e} ^ {x + 2 y + 3 z} \left(1 + 3 \frac {\partial z}{\partial x}\right) + y z + x y \frac {\partial z}{\partial x} = 0.</equation><equation>\mathrm {e} ^ {x + 2 y + 3 z} \left(2 + 3 \frac {\partial z}{\partial y}\right) + x z + x y \frac {\partial z}{\partial y} = 0.</equation>当<equation>x=0,y=0</equation>时，由原方程知<equation>\mathrm{e}^{3 z}=1</equation>，故<equation>z(0,0)=0</equation>代入（1）式得<equation>\frac{\partial z}{\partial x}=-\frac{1}{3}</equation>代入（2）式得<equation>\frac{\partial z}{\partial y}=-\frac{2}{3}.</equation>因此，<equation>\mathrm{d}z\mid_{(0,0)} = -\frac{1}{3}\mathrm{d}x - \frac{2}{3}\mathrm{d}y.</equation>（法二）对原方程两端微分，可得<equation>\mathrm{d}\left(\mathrm{e}^{x + 2y + 3z} + xyz\right) = 0</equation>，展开得<equation>\mathrm {e} ^ {x + 2 y + 3 z} \left(\mathrm {d} x + 2 \mathrm {d} y + 3 \mathrm {d} z\right) + y z \mathrm {d} x + x z \mathrm {d} y + x y \mathrm {d} z = 0.</equation>当<equation>x = 0, y = 0</equation>时，由原方程知<equation>\mathrm{e}^{3z} = 1</equation>，故<equation>z(0,0) = 0.</equation>代入（3）式得<equation>\mathrm {d} x + 2 \mathrm {d} y + 3 \mathrm {d} z = 0,</equation>即<equation>\mathrm{d}z\mid_{(0,0)} = -\frac{1}{3}\mathrm{d}x - \frac{2}{3}\mathrm{d}y.</equation>（法三）当<equation>x = 0, y = 0</equation>时，由原方程知<equation>\mathrm{e}^{3z} = 1</equation>，故<equation>z(0,0) = 0.</equation>令<equation>F ( x, y, z) = \mathrm{e}^{x+2 y+3 z} + x y z - 1</equation>，则由隐函数存在定理知，<equation>\left. \frac {\partial z}{\partial x} \right| _ {(0, 0)} = - \left. \frac {F _ {x} ^ {\prime}}{F _ {z} ^ {\prime}} \right| _ {(0, 0, 0)} = - \left. \frac {\mathrm {e} ^ {x + 2 y + 3 z} + y z}{3 \mathrm {e} ^ {x + 2 y + 3 z} + x y} \right| _ {(0, 0, 0)} = - \frac {1}{3},</equation><equation>\left. \frac {\partial z}{\partial y} \right| _ {(0, 0)} = - \left. \frac {F _ {y} ^ {\prime}}{F _ {z} ^ {\prime}} \right| _ {(0, 0, 0)} = - \left. \frac {2 \mathrm {e} ^ {x + 2 y + 3 z} + x z}{3 \mathrm {e} ^ {x + 2 y + 3 z} + x y} \right| _ {(0, 0, 0)} = - \frac {2}{3}.</equation>因此，<equation>\mathrm{d}z\mid_{(0,0)} = -\frac{1}{3}\mathrm{d}x - \frac{2}{3}\mathrm{d}y.</equation>

---

**2012年第11题 | 填空题 | 4分**

11. 设连续函数<equation>z=f(x,y)</equation>满足<equation>\lim_{ \begin{array}{l} x\to 0 \\ y\to 1 \end{array} } \frac{f(x,y)-2x+y-2} {\sqrt{x^{2}+(y-1)^{2}}}=0</equation>，则<equation>\mathrm{d} z|_{(0,1)}=</equation>___

**答案:**## 2dx-dy.

**解析:**解 由于<equation>\lim_{x\to 0}\frac{f(x,y)-2x+y-2}{\sqrt{x^2+(y-1)^2}} = 0</equation>，故<equation>\lim_{y\to 0}\left[f(x,y)-2x+y-2\right] = 0.</equation>又由<equation>f ( x,y )</equation>在点（0,1）处连续可知，<equation>f ( 0,1 )=\lim_{x\to 0}\lim_{y\to 1} f ( x,y)=\lim_{x\to 0}\lim_{y\to 1} ( 2 x-y+2 )=1</equation>，故<equation>f ( 0,1 )=1.</equation>代入题给条件，可得<equation>\lim _ {\substack {x \rightarrow 0 \\ y \rightarrow 1}} \frac {f (x , y) - f (0 , 1) - 2 x + (y - 1)}{\sqrt {x ^ {2} + (y - 1) ^ {2}}} = 0.</equation>因此，由函数<equation>f ( x,y )</equation>可微的定义可知，<equation>f ( x,y )</equation>在点(0,1)处可微且<equation>\frac{\partial f}{\partial x}\bigg|_{(0,1)} = 2,\frac{\partial f}{\partial y}\bigg|_{(0,1)} = -1,</equation><equation>\mathrm{d}z\mid_{(0,1)} = 2\mathrm{d}x - \mathrm{d}y.</equation>本题也可以直接计算<equation>\frac{\partial f}{\partial x}\bigg|_{(0,1)}, \frac{\partial f}{\partial y}\bigg|_{(0,1)}</equation>.

在等式<equation>\lim_{x\to 0}\frac{f(x,y)-2x+y-2}{\sqrt{x^2+(y-1)^2}} = 0</equation>中分别令<equation>y = 1</equation>，<equation>x = 0</equation>可得，<equation>\lim _ {x \rightarrow 0} \frac {f (x , 1) - 2 x - 1}{| x |} = 0, \quad \lim _ {y \rightarrow 1} \frac {f (0 , y) + y - 2}{| y - 1 |} = 0.</equation>于是，<equation>\lim _ {x \rightarrow 0} \frac {f (x , 1) - 2 x - 1}{x} = \lim _ {x \rightarrow 0} \frac {f (x , 1) - 2 x - 1}{| x |} \cdot \frac {| x |}{x} = 0.</equation>同理可得<equation>\lim_{y\rightarrow 1}\frac{f(0,y)+y-2}{y-1}=0.</equation>从而<equation>\lim_{x\rightarrow 0}\frac{f(x,1)-1}{x}=2, \lim_{y\rightarrow 1}\frac{f(0,y)-1}{y-1}=-1.</equation>又因为 f(0,1)=1，所以<equation>\left. \frac {\partial f}{\partial x} \right| _ {(0, 1)} = \lim _ {x \rightarrow 0} \frac {f (x , 1) - 1}{x} = 2, \quad \left. \frac {\partial f}{\partial y} \right| _ {(0, 1)} = \lim _ {y \rightarrow 1} \frac {f (0 , y) - 1}{y - 1} = - 1.</equation>

---

**2011年第10题 | 填空题 | 4分**

10. 设函数<equation>z=\left(1+\frac{x}{y}\right)^{\frac{x}{y}}</equation>，则<equation>\mathrm{d}z|_{(1,1)}=</equation>___

**答案:**(1 + 2ln2) (dx - dy).

**解析:**解<equation>z = \mathrm{e}^{\frac{x}{y}\ln(1 + \frac{x}{y})}</equation>.根据链式法则，<equation>\begin{array}{l} \frac {\partial z}{\partial x} = \left(1 + \frac {x}{y}\right) ^ {\frac {x}{y}} \left[ \frac {1}{y} \ln \left(1 + \frac {x}{y}\right) + \frac {x}{y (x + y)} \right], \\ \frac {\partial z}{\partial y} = - \left(1 + \frac {x}{y}\right) ^ {\frac {x}{y}} \left[ \frac {x}{y ^ {2}} \ln \left(1 + \frac {x}{y}\right) + \frac {x ^ {2}}{y ^ {2} (x + y)} \right]. \\ \mathrm {n} 2, \frac {\partial z}{\partial y} \Big | _ {(1, 1)} = - (1 + 2 \ln 2), \mathrm {d} z \Big | _ {(1, 1)} = (1 + 2 \ln 2) \\ \end{array}</equation>因此，<equation>\frac{\partial z}{\partial x}\bigg|_{(1,1)} = 1 + 2\ln 2,\frac{\partial z}{\partial y}\bigg|_{(1,1)} = -(1 + 2\ln 2),\mathrm{d}z\bigg|_{(1,1)} = (1 + 2\ln 2)(\mathrm{d}x - \mathrm{d}y).</equation>

---


#### 二重积分的概念与性质

**2016年第3题 | 选择题 | 4分 | 答案: B**

3. 设<equation>J_{i}=\iint_{D_{i}} \sqrt[3]{x-y}\mathrm{d}x\mathrm{d}y(i=1,2,3)</equation>，其中<equation>D_{1}=\{(x,y)\mid 0\leqslant x\leqslant 1,0\leqslant y\leqslant 1\}</equation><equation>D_{2}=\{(x,y)\mid 0\leqslant x\leqslant 1,0\leqslant y\leqslant \sqrt{x}\}</equation><equation>D_{3}=\{(x,y)\mid 0\leqslant x\leqslant 1,x^{2}\leqslant y\leqslant 1</equation>则（    ）

A.<equation>J_{1}<J_{2}<J_{3}</equation>B.<equation>J_{3}<J_{1}<J_{2}</equation>C.<equation>J_{2}<J_{3}<J_{1}</equation>D.<equation>J_{2}<J_{1}<J_{3}</equation>

答案: B

**解析:**解如图所示，<equation>D_{1}=D_{2}\cup D_{2}^{\prime}=D_{3}\cup D_{3}^{\prime}.</equation>在<equation>D_{2}^{\prime}</equation>上，由于<equation>x-y<0,\sqrt[3]{x-y}<0</equation>，故<equation>\iint_{D_{2}^{\prime}} \sqrt[3]{x-y}\mathrm{d}x\mathrm{d}y<0.</equation>在<equation>D_{3}^{\prime}</equation>上，由于<equation>x-y>0,\sqrt[3]{x-y}>0</equation>，故<equation>\iint_{D_{3}^{\prime}} \sqrt[3]{x-y}\mathrm{d}x\mathrm{d}y>0.</equation>因此，<equation>J _ {1} - J _ {2} = \iint_ {D _ {1} \backslash D _ {2}} \sqrt [ 3 ]{x - y} \mathrm {d} x \mathrm {d} y = \iint_ {D _ {2} ^ {\prime}} \sqrt [ 3 ]{x - y} \mathrm {d} x \mathrm {d} y < 0,</equation><equation>J _ {1} - J _ {3} = \iint_ {D _ {1} \backslash D _ {3}} \sqrt [ 3 ]{x - y} \mathrm {d} x \mathrm {d} y = \iint_ {D _ {3} ^ {\prime}} \sqrt [ 3 ]{x - y} \mathrm {d} x \mathrm {d} y > 0.</equation>综上所述，<equation>J_{1} < J_{2}, J_{1} > J_{3}</equation>，即<equation>J_{3} < J_{1} < J_{2}.</equation>应选B.

---

**2013年第3题 | 选择题 | 4分 | 答案: B**

3. 设<equation>D_{k}</equation>是圆域<equation>D=\{(x,y)\mid x^{2}+y^{2}\leqslant 1\}</equation>位于第 k象限的部分.记<equation>I_{k}=\iint_{D_{k}}(y-x)\mathrm{d}x\mathrm{d}y(k=1,2,3,4)</equation>，则（    )

A.<equation>I_{1}>0</equation>B.<equation>I_{2}>0</equation>C.<equation>I_{3}>0</equation>D.<equation>I_{4}>0</equation>

答案: B

**解析:**解（法一）由于在第一象限内 x > 0，y > 0，第二象限内 x < 0，y > 0，第三象限内 x < 0， y < 0，第四象限内 x > 0，y < 0，故被积函数 y - x在第二象限内恒大于零，从而<equation>\iint_{D_{2}}(y-x)\mathrm{d}x\mathrm{d}y>0.</equation>应选B.

（法二）在极坐标系下计算<equation>I_{k}(k = 1,2,3,4).</equation><equation>\begin{array}{l} I _ {k} \stackrel {\text {极 坐 标}} {=} \int_ {\frac {(k - 1) \pi}{2}} ^ {\frac {k \pi}{2}} (\sin \theta - \cos \theta) \mathrm {d} \theta \int_ {0} ^ {1} r ^ {2} \mathrm {d} r = \frac {1}{3} \int_ {\frac {(k - 1) \pi}{2}} ^ {\frac {k \pi}{2}} (\sin \theta - \cos \theta) \mathrm {d} \theta \\ = - \frac {\left(\sin \theta + \cos \theta\right)}{3} \Bigg | _ {\frac {(k - 1) \pi}{2}} ^ {\frac {k \pi}{2}}. \\ \end{array}</equation>分别求得<equation>I _ {1} = 0, \quad I _ {2} = \frac {2}{3}, \quad I _ {3} = 0, \quad I _ {4} = - \frac {2}{3}.</equation><equation>I_{2} > 0</equation>应选B.

---


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
