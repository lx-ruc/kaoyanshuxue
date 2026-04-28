#### 二重积分的计算

**2025年第19题 | 解答题 | 12分**

19. 已知平面有界区域<equation>D=\{(x,y)\mid y^{2}\leqslant x,x^{2}\leqslant y\}</equation>，计算二重积分<equation>\iint_{D}(x-y+1)^{2}\mathrm{d}x\mathrm{d}y.</equation>

**解析:**分析 本题主要考查二重积分的计算.

区域 D由两条抛物线围成，且关于直线 y=x对称，故可以考虑使用轮换对称性.

解如图所示，区域D由曲线<equation>y=x^{2}</equation>与<equation>x=y^{2}</equation>围成.由于区域D位于第一象限，故<equation>x=y^{2}</equation>可写成<equation>y=\sqrt{x}.</equation>注意到区域 D关于直线 y=x对称.记<equation>D_{1}</equation>为区域 D位于直线 y=x下方的部分，则由轮换对称性的结论可得<equation>\begin{aligned} \iint_ {D} (x - y + 1) ^ {2} \mathrm {d} x \mathrm {d} y &= \iint_ {D _ {1}} (x - y + 1) ^ {2} \mathrm {d} x \mathrm {d} y + \iint_ {D \backslash D _ {1}} (x - y + 1) ^ {2} \mathrm {d} x \mathrm {d} y \\ &= \iint_ {D _ {1}} \left[ (x - y + 1) ^ {2} + (y - x + 1) ^ {2} \right] \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} \left[ (x - y) ^ {2} + 1 \right] \mathrm {d} x \mathrm {d} y. \end{aligned}</equation>将<equation>D_{1}</equation>写成X型区域.<equation>D _ {1} = \left\{(x, y) \mid x ^ {2} \leqslant y \leqslant x, 0 \leqslant x \leqslant 1 \right\}.</equation>分别计算<equation>\iint_{D_1}\mathrm{d}x\mathrm{d}y,\iint_{D_1}(x - y)^2\mathrm{d}x\mathrm{d}y.</equation><equation>\iint_ {D _ {1}} \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {x ^ {2}} ^ {x} \mathrm {d} y = \int_ {0} ^ {1} \left(x - x ^ {2}\right) \mathrm {d} x = \left(\frac {x ^ {2}}{2} - \frac {x ^ {3}}{3}\right) \Bigg | _ {0} ^ {1} = \frac {1}{2} - \frac {1}{3} = \frac {1}{6}.</equation><equation>\begin{aligned} \iint_ {D _ {1}} (x - y) ^ {2} \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {1} \mathrm {d} x \int_ {x ^ {2}} ^ {x} (x - y) ^ {2} \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {x ^ {2}} ^ {x} \left(x ^ {2} - 2 x y + y ^ {2}\right) \mathrm {d} y \\ &= \int_ {0} ^ {1} \left(x ^ {2} y - x y ^ {2} + \frac {y ^ {3}}{3}\right) \Big | _ {x ^ {2}} ^ {x} \mathrm {d} x = \int_ {0} ^ {1} \left(\frac {x ^ {3}}{3} - x ^ {4} + x ^ {5} - \frac {x ^ {6}}{3}\right) \mathrm {d} x \\ &= \left. \left(- \frac {x ^ {7}}{2 1} + \frac {x ^ {6}}{6} - \frac {x ^ {5}}{5} + \frac {x ^ {4}}{1 2}\right) \right| _ {0} ^ {1} = - \frac {1}{2 1} + \frac {1}{6} - \frac {1}{5} + \frac {1}{1 2} = \frac {1}{4 2 0}. \end{aligned}</equation>因此，<equation>\iint_ {D} (x - y + 1) ^ {2} \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} \left[ (x - y) ^ {2} + 1 \right] \mathrm {d} x \mathrm {d} y = 2 \left(\frac {1}{4 2 0} + \frac {1}{6}\right) = \frac {7 1}{2 1 0}.</equation>

---

**2024年第17题 | 解答题 | 10分**

17. (本题满分10分）设平面有界区域 D位于第一象限，由曲线<equation>x y=\frac{1}{3},</equation><equation>x y=3</equation>与直线<equation>y=\frac{1}{3} x</equation><equation>y=3 x</equation>所围成，请计算<equation>\iint_{D}(1+x-y) \mathrm{d} x \mathrm{d} y.</equation>

**答案:**##<equation>\frac{8}{3}\ln 3.</equation>

**解析:**解区域 D如图（a）所示，注意到区域 D的四条边界曲线中，交换曲线<equation>xy=\frac{1}{3}</equation>与<equation>xy=3</equation>中x， y的位置，可得<equation>yx=\frac{1}{3}</equation>与<equation>yx=3</equation>，即曲线方程不变，故这两条曲线均关于直线 y=x对称，而直线<equation>y=\frac{1}{3} x</equation>与直线 y=3x关于直线 y=x对称，故这四条曲线所围成的区域 D也关于直线 y=x对称，从而对变量 x，y具有轮换对称性.

(a)

(b)

由轮换对称性的结论（2）可得<equation>\iint_{D}x\mathrm{d}x\mathrm{d}y=\iint_{D}y\mathrm{d}x\mathrm{d}y</equation>，故<equation>\iint_ {D} (1 + x - y) \mathrm {d} x \mathrm {d} y = \iint_ {D} \mathrm {d} x \mathrm {d} y + \iint_ {D} x \mathrm {d} x \mathrm {d} y - \iint_ {D} y \mathrm {d} x \mathrm {d} y = \iint_ {D} \mathrm {d} x \mathrm {d} y.</equation>下面用两种方法计算<equation>\iint_{D}\mathrm{d}x\mathrm{d}y.</equation>（法一）在极坐标系下计算.

曲线<equation>xy = \frac{1}{3}</equation>的极坐标方程为<equation>r^2\cos \theta \sin \theta = \frac{1}{3}</equation>，整理可得<equation>r = \sqrt{\frac{2}{3\sin 2\theta}}</equation>，曲线<equation>xy = 3</equation>的极坐标方程为<equation>r^2\cos \theta \sin \theta = 3</equation>，整理可得<equation>r = \sqrt{\frac{6}{\sin 2\theta}}</equation>直线<equation>y = \frac{1}{3} x</equation>的极坐标方程为<equation>\theta = \arctan \frac{1}{3},y = 3x</equation>的极坐标方程为<equation>\theta = \arctan 3.</equation>区域 D的极坐标表示为<equation>D = \left\{(r, \theta) \mid \sqrt {\frac {2}{3 \sin 2 \theta}} \leqslant r \leqslant \sqrt {\frac {6}{\sin 2 \theta}}, \arctan \frac {1}{3} \leqslant \theta \leqslant \arctan 3 \right\}.</equation>于是，<equation>\begin{aligned} \iint_ {D} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} \mathrm {d} \theta \int_ {\sqrt {\frac {2}{3 \sin 2 \theta}}} ^ {\sqrt {\frac {6}{\sin 2 \theta}}} r \mathrm {d} r &= \frac {1}{2} \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} r ^ {2} \left|  \sqrt {\frac {6}{\sin 2 \theta}} \\ \sqrt {\frac {2}{3 \sin 2 \theta}}  \right) \mathrm {d} \theta \\ &= \frac {8}{3} \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} \csc 2 \theta \mathrm {d} \theta = \frac {4}{3} \ln | \csc 2 \theta - \cot 2 \theta | \left| _ {\arctan \frac {1}{3}} ^ {\arctan 3}. \right. \end{aligned}</equation>由于<equation>\csc 2\theta -\cot 2\theta = \frac{1 - \cos 2\theta}{\sin 2\theta} = \frac{2\sin^2\theta}{2\sin \theta \cos \theta} = \tan \theta</equation>，故<equation>\iint_{D}\mathrm{d}x\mathrm{d}y = \frac{4}{3}\ln |\tan \theta |\Bigg|_{\arctan \frac{1}{3}}^{ \arctan 3}</equation>当<equation>\theta = \arctan \frac{1}{3}</equation>时，<equation>\tan \theta = \frac{1}{3}</equation>，当<equation>\theta = \arctan 3</equation>时，<equation>\tan \theta = 3.</equation>因此，<equation>\iint_ {D} \mathrm {d} x \mathrm {d} y = \frac {4}{3} \left(\ln 3 - \ln \frac {1}{3}\right) = \frac {8}{3} \ln 3.</equation>（法二）在直角坐标系下计算.

联立<equation>\left\{\begin{array}{l l} x y=\frac{1}{3}, \\ y=\frac{1}{3} x, \end{array} \right.</equation>解得<equation>\left\{\begin{array}{l l} x=1, \\ y=\frac{1}{3}. \end{array} \right.</equation>联立<equation>\left\{\begin{array}{l l} x y=\frac{1}{3}, \\ y=3 x, \end{array} \right.</equation>解得<equation>\left\{\begin{array}{l l} x=\frac{1}{3}, \\ y=1. \end{array} \right.</equation>联立<equation>\left\{\begin{array}{l l} x y=3, \\ y=\frac{1}{3} x, \end{array} \right.</equation>解得<equation>\left\{\begin{array}{l l} x=3, \\ y=1. \end{array} \right.</equation>联立<equation>\left\{\begin{array}{l l} x y=3, \\ y=3 x, \end{array} \right.</equation>解得<equation>\left\{\begin{array}{l l} x=1, \\ y=3. \end{array} \right.</equation>如图（b）所示，直线<equation>x=1</equation>将区域D分为两部分<equation>D_{1}, D_{2}.</equation><equation>D_{1}</equation>由曲线<equation>xy=\frac{1}{3}</equation>，直线<equation>y=3x</equation>与<equation>x= 1</equation>围成，<equation>D_{2}</equation>由曲线<equation>xy=3</equation>，直线<equation>y=\frac{1}{3} x</equation>与<equation>x=1</equation>围成，<equation>\iint_{D}\mathrm{d}x\mathrm{d}y</equation>等于D的面积，即<equation>D_{1}</equation>的面积与<equation>D_{2}</equation>的面积之和.

因此，<equation>\begin{aligned} \iint_ {D} \mathrm {d} x \mathrm {d} y &= \int_ {\frac {1}{3}} ^ {1} \left(3 x - \frac {1}{3 x}\right) \mathrm {d} x + \int_ {1} ^ {3} \left(\frac {3}{x} - \frac {x}{3}\right) \mathrm {d} x = \left(\frac {3 x ^ {2}}{2} - \frac {1}{3} \ln x\right) \Bigg | _ {\frac {1}{3}} ^ {1} + \left(3 \ln x - \frac {x ^ {2}}{6}\right) \Bigg | _ {1} ^ {3} \\ &= \frac {3}{2} - \frac {1}{6} + \frac {1}{3} \ln \frac {1}{3} + 3 \ln 3 - \frac {3}{2} + \frac {1}{6} = - \frac {1}{3} \ln 3 + 3 \ln 3 = \frac {8}{3} \ln 3. \end{aligned}</equation>

---

**2023年第19题 | 解答题 | 12分**

19. (本题满分12分)

已知平面区域<equation>D=\{(x,y)\mid(x-1)^{2}+y^{2}\leqslant1\}</equation>，计算二重积分<equation>\iint_{D}|\sqrt{x^{2}+y^{2}}-1|\mathrm{d}x\mathrm{d}y.</equation>

**答案:**<equation>- \frac {3 2}{9} - \frac {\pi}{9} + 3 \sqrt {3}.</equation>

**解析:**解注意到<equation>\mid \sqrt{x^{2}+y^{2}}-1\mid</equation>为关于 y的偶函数，而积分区域 D关于 x轴对称，记 D位于上半平面的部分为<equation>D_{1}</equation>即图（b）中的蓝色部分与灰色部分，则<equation>\iint_ {D} \left| \sqrt {x ^ {2} + y ^ {2}} - 1 \right| \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} \left| \sqrt {x ^ {2} + y ^ {2}} - 1 \right| \mathrm {d} x \mathrm {d} y.</equation>在区域<equation>x^{2}+y^{2}\leqslant 1</equation>内，<equation>|\sqrt{x^{2}+y^{2}}-1|=1-\sqrt{x^{2}+y^{2}}</equation>在区域<equation>x^{2}+y^{2}\leqslant 1</equation>外，<equation>|\sqrt{x^{2}+y^{2}}-1|=</equation><equation>\sqrt{x^{2}+y^{2}}-1.</equation>记<equation>x^{2}+y^{2}\leqslant 1</equation>与<equation>D_{1}</equation>的公共部分为<equation>D_{2}</equation>即图（b）中的蓝色部分，则<equation>\begin{aligned} \iint_ {D _ {1}} \left| \sqrt {x ^ {2} + y ^ {2}} - 1 \right| \mathrm {d} x \mathrm {d} y &= \iint_ {D _ {1} \backslash D _ {2}} \left(\sqrt {x ^ {2} + y ^ {2}} - 1\right) \mathrm {d} x \mathrm {d} y + \iint_ {D _ {2}} \left(1 - \sqrt {x ^ {2} + y ^ {2}}\right) \mathrm {d} x \mathrm {d} y \\ &= \iint_ {D _ {1}} \left(\sqrt {x ^ {2} + y ^ {2}} - 1\right) \mathrm {d} x \mathrm {d} y - 2 \iint_ {D _ {2}} \left(\sqrt {x ^ {2} + y ^ {2}} - 1\right) \mathrm {d} x \mathrm {d} y. \end{aligned}</equation>下面分别计算<equation>\iint_{D_{1}}(\sqrt{x^{2}+y^{2}}-1)\mathrm{d}x\mathrm{d}y, \iint_{D_{2}}(\sqrt{x^{2}+y^{2}}-1)\mathrm{d}x\mathrm{d}y.</equation>圆周<equation>( x-1 )^{2}+y^{2}=1</equation>的极坐标方程为<equation>r=2\cos \theta</equation>，故<equation>D_{1}</equation>在极坐标系下的表示为<equation>D _ {1} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2 \cos \theta , 0 \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation>于是，<equation>\begin{aligned} \iint_ {D _ {1}} \left(\sqrt {x ^ {2} + y ^ {2}} - 1\right) \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \int_ {0} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {2 \cos \theta} (r - 1) \cdot r \mathrm {d} r &= \int_ {0} ^ {\frac {\pi}{2}} \left(\frac {r ^ {3}}{3} - \frac {r ^ {2}}{2}\right) \Bigg | _ {0} ^ {2 \cos \theta} \mathrm {d} \theta \\ &= \int_ {0} ^ {\frac {\pi}{2}} \left(\frac {8}{3} \cos^ {3} \theta - 2 \cos^ {2} \theta\right) \mathrm {d} \theta = \frac {8}{3} \int_ {0} ^ {\frac {\pi}{2}} \cos^ {3} \theta \mathrm {d} \theta - 2 \int_ {0} ^ {\frac {\pi}{2}} \cos^ {2} \theta \mathrm {d} \theta \\ &= \frac {8}{3} \cdot \frac {2}{3} - 2 \cdot \frac {\pi}{4} = \frac {1 6}{9} - \frac {\pi}{2}. \end{aligned}</equation>联立<equation>\left\{\begin{array}{l l}x^{2}+y^{2}=1,\\ (x-1)^{2}+y^{2}=1,\end{array}\right.</equation>解得<equation>\left\{\begin{array}{l l}x=\frac{1}{2},\\ y=\pm \frac{\sqrt{3}}{2},\end{array}\right.</equation>从而圆周<equation>x^{2}+y^{2}=1</equation>与圆周<equation>(x-1)^{2}+y^{2}=1</equation>在上半平面的交点为<equation>\left(\frac{1}{2},\frac{\sqrt{3}}{2}\right).</equation>连接原点O与点<equation>\left(\frac{1}{2},\frac{\sqrt{3}}{2}\right)</equation>的直线方程为<equation>y=\sqrt{3} x</equation>其极坐标方程为<equation>\theta=\frac{\pi}{3}.</equation>如图（c）所示，<equation>D_{2}</equation>可以由直线<equation>\theta=\frac{\pi}{3}</equation>分为两部分，在极坐标系下的表示为<equation>D _ {2} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 1, 0 \leqslant \theta \leqslant \frac {\pi}{3} \right\} \cup \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2 \cos \theta , \frac {\pi}{3} \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation>于是，<equation>\iint_ {D _ {2}} \left(\sqrt {x ^ {2} + y ^ {2}} - 1\right) \mathrm {d} x \mathrm {d} y \xlongequal {\text {极 坐 标}} \int_ {0} ^ {\frac {\pi}{3}} \mathrm {d} \theta \int_ {0} ^ {1} (r - 1) \cdot r \mathrm {d} r + \int_ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {2 \cos \theta} (r - 1) \cdot r \mathrm {d} r.</equation>其中，<equation>\int_ {0} ^ {\frac {\pi}{3}} \mathrm {d} \theta \int_ {0} ^ {1} (r - 1) \cdot r \mathrm {d} r = \int_ {0} ^ {\frac {\pi}{3}} \left(\frac {r ^ {3}}{3} - \frac {r ^ {2}}{2}\right) \Big | _ {0} ^ {1} \mathrm {d} \theta = \int_ {0} ^ {\frac {\pi}{3}} \left(\frac {1}{3} - \frac {1}{2}\right) \mathrm {d} \theta = - \frac {1}{6} \cdot \frac {\pi}{3} = - \frac {\pi}{1 8}.</equation><equation>\begin{aligned} \int_ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {2 \cos \theta} (r - 1) \cdot r \mathrm {d} r &= \int_ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \left(\frac {8}{3} \cos^ {3} \theta - 2 \cos^ {2} \theta\right) \mathrm {d} \theta = \frac {8}{3} \int_ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \cos^ {3} \theta \mathrm {d} \theta - 2 \int_ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \cos^ {2} \theta \mathrm {d} \theta \\ &= \frac {8}{3} \int_ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \left(1 - \sin^ {2} \theta\right) \mathrm {d} (\sin \theta) - \int_ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \left(1 + \cos 2 \theta\right) \mathrm {d} \theta \\ &= \frac {8}{3} \left(\sin \theta - \frac {\sin^ {3} \theta}{3}\right) \left| _ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} - \frac {\pi}{6} - \frac {\sin 2 \theta}{2} \right| _ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \\ &= - \frac {\pi}{6} + \frac {8}{3} \left(\frac {2}{3} - \frac {3 \sqrt {3}}{8}\right) + \frac {\sqrt {3}}{4} = - \frac {\pi}{6} + \frac {1 6}{9} - \frac {3 \sqrt {3}}{4}. \end{aligned}</equation>因此，<equation>\iint_ {D _ {2}} \left(\sqrt {x ^ {2} + y ^ {2}} - 1\right) \mathrm {d} x \mathrm {d} y = - \frac {\pi}{1 8} - \frac {\pi}{6} + \frac {1 6}{9} - \frac {3 \sqrt {3}}{4} = - \frac {2 \pi}{9} + \frac {1 6}{9} - \frac {3 \sqrt {3}}{4}.</equation>综上所述，<equation>\iint_ {D} \left| \sqrt {x ^ {2} + y ^ {2}} - 1 \right| \mathrm {d} x \mathrm {d} y = 2 \left(\frac {1 6}{9} - \frac {\pi}{2} + \frac {4 \pi}{9} - \frac {3 2}{9} + \frac {3 \sqrt {3}}{2}\right) = - \frac {3 2}{9} - \frac {\pi}{9} + 3 \sqrt {3}.</equation>

---

**2022年第14题 | 填空题 | 5分**

14. 已知函数 f(x)<equation>\left\{\begin{array}{l l} {\mathrm{e}^{x},}&{0 \leqslant x \leqslant 1,}\\ {0,}&{\mathrm{其他},}\end{array} \right.</equation>则<equation>\int_{-\infty}^{+\infty}\mathrm{d}x\int_{-\infty}^{+\infty}f(x)f(y-x)\mathrm{d}y=</equation>___.

**解析:**解 根据 f(x)的定义，f(x)仅在 0≤x≤1时非零，f(y-x)仅在 0≤y-x≤1时非零.于是，f(x)f(y-x)仅在区域 D = {（x,y）|0≤y-x≤1,0≤x≤1}，即 D = {（x,y）|x≤y≤x+1,0≤x≤1}上非零.<equation>\begin{aligned} \int_ {- \infty} ^ {+ \infty} \mathrm {d} x \int_ {- \infty} ^ {+ \infty} f (x) f (y - x) \mathrm {d} y &= \int_ {0} ^ {1} \mathrm {d} x \int_ {x} ^ {x + 1} \mathrm {e} ^ {x} \mathrm {e} ^ {y - x} \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {x} ^ {x + 1} \mathrm {e} ^ {y} \mathrm {d} y \\ &= \int_ {0} ^ {1} \left(\mathrm {e} ^ {x + 1} - \mathrm {e} ^ {x}\right) \mathrm {d} x = \left(\mathrm {e} ^ {x + 1} - \mathrm {e} ^ {x}\right) \Bigg | _ {0} ^ {1} \\ &= \left(\mathrm {e} ^ {2} - \mathrm {e}\right) - (\mathrm {e} - 1) = \mathrm {e} ^ {2} - 2 \mathrm {e} + 1. \end{aligned}</equation>

---

**2022年第19题 | 解答题 | 12分**

19. (本题满分12分）

已知平面区域 D = {（x,y）| y-2≤x≤<equation>\sqrt{4-y^{2}}</equation>, 0≤y≤2} ，计算 I =<equation>\iint_{D} \frac{(x-y)^{2}}{x^{2}+y^{2}} \mathrm{d} x \mathrm{d} y.</equation>

**解析:**解 在极坐标系下计算.

由 D的表达式可知，如图（a）所示，D是由直线<equation>y=x+2</equation>，圆<equation>x^{2}+y^{2}=4</equation>以及 x轴围成的部分.直线<equation>y=x+2</equation>在极坐标系下的表示为<equation>r=\frac{2}{\sin \theta -\cos \theta}</equation>，圆<equation>x^{2}+y^{2}=4</equation>在极坐标系下的表示为<equation>r=2.</equation>(a)

(b)

如图（b）所示，将 D分为两部分<equation>D_{1}</equation>和<equation>D_{2}.</equation><equation>D _ {1} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2, 0 \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation><equation>D _ {2} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \frac {2}{\sin \theta - \cos \theta}, \frac {\pi}{2} \leqslant \theta \leqslant \pi \right\}.</equation>因此，<equation>\begin{aligned} \iint_ {D} \frac {\left(x - y\right) ^ {2}}{x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \iint_ {D} \frac {r ^ {2} \left(\cos \theta - \sin \theta\right) ^ {2}}{r ^ {2}} \cdot r \mathrm {d} r \mathrm {d} \theta &= \iint_ {D} \left(\cos \theta - \sin \theta\right) ^ {2} \cdot r \mathrm {d} r \mathrm {d} \theta \\ &= \int_ {0} ^ {\frac {\pi}{2}} \left(\cos \theta - \sin \theta\right) ^ {2} \mathrm {d} \theta \int_ {0} ^ {2} r \mathrm {d} r + \int_ {\frac {\pi}{2}} ^ {\pi} \left(\cos \theta - \sin \theta\right) ^ {2} \mathrm {d} \theta \int_ {0} ^ {\frac {2}{\sin \theta - \cos \theta}} r \mathrm {d} r \\ &= 2 \int_ {0} ^ {\frac {\pi}{2}} \left(1 - 2 \sin \theta \cos \theta\right) \mathrm {d} \theta + \int_ {\frac {\pi}{2}} ^ {\pi} \left(\cos \theta - \sin \theta\right) ^ {2} \cdot \frac {r ^ {2}}{2} \Bigg | _ {0} ^ {\frac {2}{\sin \theta - \cos \theta}} \mathrm {d} \theta \\ &= 2 \left(\frac {\pi}{2} - \sin^ {2} \theta \Bigg | _ {0} ^ {\frac {\pi}{2}}\right) + \int_ {\frac {\pi}{2}} ^ {\pi} \left(\cos \theta - \sin \theta\right) ^ {2} \cdot \frac {2}{\left(\sin \theta - \cos \theta\right) ^ {2}} \mathrm {d} \theta \\ &= \pi - 2 + 2 \times \left(\pi - \frac {\pi}{2}\right) = 2 \pi - 2. \end{aligned}</equation>

---

**2021年第19题 | 解答题 | 12分**

19. (本题满分12分)

设有界区域 D是圆<equation>x^{2}+y^{2}=1</equation>与直线 y=x以及 x轴在第一象限围成的部分，请计算二重积分<equation>\iint_{D} \mathrm{e}^{(x+y)^{2}}(x^{2}-y^{2})\mathrm{d}x\mathrm{d}y.</equation>

**答案:**<equation>\frac {1}{8} (\mathrm {e} - 1) ^ {2}.</equation>

**解析:**区域 D在极坐标系下的表示为<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 1, 0 \leqslant \theta \leqslant \frac {\pi}{4} \right\}.</equation>在极坐标系下计算积分.<equation>\begin{aligned} \iint_ {D} \mathrm {e} ^ {(x + y) ^ {2}} \left(x ^ {2} - y ^ {2}\right) \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \iint_ {D} \mathrm {e} ^ {r ^ {2} (\cos \theta + \sin \theta) ^ {2}} \cdot r ^ {2} \left(\cos^ {2} \theta - \sin^ {2} \theta\right) \cdot r \mathrm {d} r \mathrm {d} \theta \\ &= \iint_ {D} \mathrm {e} ^ {r ^ {2} (1 + \sin 2 \theta)} r ^ {3} \cos 2 \theta \mathrm {d} r \mathrm {d} \theta = \int_ {0} ^ {1} r ^ {3} \mathrm {d} r \int_ {0} ^ {\frac {\pi}{4}} \mathrm {e} ^ {r ^ {2} (1 + \sin 2 \theta)} \cos 2 \theta \mathrm {d} \theta \\ &= \int_ {0} ^ {1} r ^ {3} \mathrm {d} r \int_ {0} ^ {\frac {\pi}{4}} \mathrm {e} ^ {r ^ {2} (1 + \sin 2 \theta)} \mathrm {d} \left(\frac {1 + \sin 2 \theta}{2}\right) = \frac {1}{2} \int_ {0} ^ {1} r ^ {3} \cdot \frac {\mathrm {e} ^ {r ^ {2} (1 + \sin 2 \theta)}}{r ^ {2}} \Bigg | _ {0} ^ {\frac {\pi}{4}} \mathrm {d} r \\ &= \frac {1}{2} \int_ {0} ^ {1} r \left(\mathrm {e} ^ {2 r ^ {2}} - \mathrm {e} ^ {r ^ {2}}\right) \mathrm {d} r = \frac {1}{4} \int_ {0} ^ {1} \left(\mathrm {e} ^ {2 r ^ {2}} - \mathrm {e} ^ {r ^ {2}}\right) \mathrm {d} \left(r ^ {2}\right) \\ &= \frac {1}{4} \left(\frac {\mathrm {e} ^ {2 r ^ {2}}}{2} - \mathrm {e} ^ {r ^ {2}}\right) \Bigg | _ {0} ^ {1} = \frac {1}{8} \left(\mathrm {e} ^ {2} - 2 \mathrm {e} + 1\right) = \frac {1}{8} (\mathrm {e} - 1) ^ {2}. \end{aligned}</equation>

---

**2020年第18题 | 解答题 | 10分**

18. (本题满分10分)

设 D = {(x,y) | x²+y²≤1,y≥0}, 连续函数 f(x,y)满足 f(x,y) = y<equation>\sqrt{1-x^{2}}</equation>+ x<equation>\iint_{D} f(x,y)\mathrm{d}x\mathrm{d}y</equation>，求<equation>\iint_{D} xf(x,y)\mathrm{d}x\mathrm{d}y.</equation>

**答案:**# 128

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


