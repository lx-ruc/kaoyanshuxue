#### 重积分的计算

**2024年第17题 | 解答题 | 10分**

17. (本题满分10分）

已知平面区域<equation>D=\{(x,y)\mid \sqrt{1-y^{2}}\leqslant x\leqslant 1,-1\leqslant y\leqslant 1\}</equation>，计算<equation>\iint_{D}\frac{x}{\sqrt{x^{2}+y^{2}}}\mathrm{d}x\mathrm{d}y.</equation>

**答案:**<equation>\ln(\sqrt{2}+1)+\sqrt{2}-2</equation>

**解析:**解（法一）如图（a）所示，区域 D关于 x轴对称，而<equation>\frac{x}{\sqrt{x^{2}+y^{2}}}</equation>为关于 y的偶函数，故<equation>\iint_{D}\frac{x}{\sqrt{x^{2}+y^{2}}}\mathrm{d}x\mathrm{d}y=</equation><equation>2\iint_{D_{1}}\frac{x}{\sqrt{x^{2}+y^{2}}}\mathrm{d}x\mathrm{d}y</equation>，其中<equation>D_{1}</equation>为D位于x轴上方的部分.

注意到<equation>D_{1}</equation>关于直线<equation>y=x</equation>对称，如图（b）所示，记<equation>D_{0}</equation>为<equation>D_{1}</equation>位于直线<equation>y=x</equation>下方的部分，则由轮换对称性的结论可知，

(a)

(b)<equation>\iint_ {D _ {1}} \frac {x}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y = \iint_ {D _ {0}} \frac {x}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y + \iint_ {D _ {1} \backslash D _ {0}} \frac {x}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y = \iint_ {D _ {0}} \frac {x + y}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y.</equation><equation>D_{0}</equation>在极坐标系下的表示为<equation>D_{0} = \left\{(r,\theta)\mid 1\leqslant r\leqslant \sec \theta ,0\leqslant \theta \leqslant \frac{\pi}{4}\right\}</equation>. 因此，<equation>\begin{aligned} \iint_ {D} \frac {x}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y &= 2 \iint_ {D _ {1}} \frac {x}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {0}} \frac {x + y}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y \\ \xlongequal {\text {极 坐 标}} 2 \iint_ {D _ {0}} (\cos \theta + \sin \theta) \cdot r \mathrm {d} r \mathrm {d} \theta &= 2 \int_ {0} ^ {\frac {\pi}{4}} (\cos \theta + \sin \theta) \mathrm {d} \theta \int_ {1} ^ {\sec \theta} r \mathrm {d} r \\ &= 2 \int_ {0} ^ {\frac {\pi}{4}} (\cos \theta + \sin \theta) \cdot \frac {1}{2} \left(\sec^ {2} \theta - 1\right) \mathrm {d} \theta = \int_ {0} ^ {\frac {\pi}{4}} (\cos \theta + \sin \theta) \left(\sec^ {2} \theta - 1\right) \mathrm {d} \theta \\ &= \int_ {0} ^ {\frac {\pi}{4}} \left(\sec \theta - \cos \theta + \frac {\sin \theta}{\cos^ {2} \theta} - \sin \theta\right) \mathrm {d} \theta = \left[ \ln \left(\sec \theta + \tan \theta\right) - \sin \theta + \frac {1}{\cos \theta} + \cos \theta \right] \Bigg | _ {0} ^ {\frac {\pi}{4}} \\ &= \ln (\sqrt {2} + 1) + \sqrt {2} - 2. \end{aligned}</equation>（法二）也可以在直角坐标系下计算<equation>\iint_{D} \frac{x}{\sqrt{x^{2}+y^{2}}} \mathrm{d}x \mathrm{d}y.</equation><equation>\begin{aligned} \iint_ {D} \frac {x}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y &= 2 \iint_ {D _ {1}} \frac {x}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y = 2 \int_ {0} ^ {1} \mathrm {d} y \int_ {\sqrt {1 - y ^ {2}}} ^ {1} \frac {x}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \\ &= 2 \int_ {0} ^ {1} \sqrt {x ^ {2} + y ^ {2}} \Big | _ {x = \sqrt {1 - y ^ {2}}} ^ {x = 1} \mathrm {d} y = 2 \int_ {0} ^ {1} \left(\sqrt {1 + y ^ {2}} - 1\right) \mathrm {d} y \\ \underline {{\underline {{y = \tan u}}}} 2 \int_ {0} ^ {\frac {\pi}{4}} \sec^ {3} u \mathrm {d} u - 2. \end{aligned}</equation>下面计算<equation>\int_{0}^{\frac{\pi}{4}}\sec^{3}u\mathrm{d}u.</equation><equation>\begin{aligned} \int_ {0} ^ {\frac {\pi}{4}} \sec^ {3} u \mathrm {d} u &= \int_ {0} ^ {\frac {\pi}{4}} \sec u \mathrm {d} (\tan u) = \sec u \tan u \left| _ {0} ^ {\frac {\pi}{4}} - \int_ {0} ^ {\frac {\pi}{4}} \tan u \cdot \sec u \tan u \mathrm {d} u \right. \\ &= \sqrt {2} - \int_ {0} ^ {\frac {\pi}{4}} \left(\sec^ {2} u - 1\right) \sec u \mathrm {d} u = \sqrt {2} - \int_ {0} ^ {\frac {\pi}{4}} \sec^ {3} u \mathrm {d} u + \int_ {0} ^ {\frac {\pi}{4}} \sec u \mathrm {d} u \\ &= \sqrt {2} - \int_ {0} ^ {\frac {\pi}{4}} \sec^ {3} u \mathrm {d} u + \ln (\sec u + \tan u) \Bigg | _ {0} ^ {\frac {\pi}{4}} \\ &= \sqrt {2} - \int_ {0} ^ {\frac {\pi}{4}} \sec^ {3} u \mathrm {d} u + \ln (\sqrt {2} + 1). \end{aligned}</equation>由此可得<equation>2\int_{0}^{\frac{\pi}{4}} \sec^{3} u \mathrm{d} u=\ln(\sqrt{2}+1)+\sqrt{2}.</equation>因此，<equation>\iint_{D}\frac{x}{\sqrt{x^{2}+y^{2}}}\mathrm{d}x\mathrm{d}y=\ln(\sqrt{2}+1)+\sqrt{2}-2.</equation>

---

**2022年第18题 | 解答题 | 12分**

18. (本题满分12分）

已知平面区域 D = {（x,y）| y-2≤x≤<equation>\sqrt{4-y^{2}}</equation>, 0≤y≤2} ，计算 I =<equation>\iint_{D} \frac{(x-y)^{2}}{x^{2}+y^{2}} \mathrm{d} x \mathrm{d} y.</equation>

**答案:**## I = 2<equation>\pi</equation>- 2.

**解析:**解 在极坐标系下计算.

由<equation>D</equation>的表达式可知，如图（a）所示，<equation>D</equation>是由直线<equation>y = x + 2</equation>，圆<equation>x^{2} + y^{2} = 4</equation>以及<equation>x</equation>轴围成的部分.直线<equation>y = x + 2</equation>在极坐标系下的表示为<equation>r = \frac{2}{\sin \theta - \cos \theta}</equation>，圆<equation>x^{2} + y^{2} = 4</equation>在极坐标系下的表示为<equation>r = 2</equation>.

(a)

(b)

如图（b）所示，将<equation>D</equation>分为两部分<equation>D_{1}</equation>和<equation>D_{2}</equation>.<equation>D _ {1} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2, 0 \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation><equation>D _ {2} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \frac {2}{\sin \theta - \cos \theta}, \frac {\pi}{2} \leqslant \theta \leqslant \pi \right\}.</equation>因此，<equation>\begin{aligned} \iint_ {D} \frac {(x - y) ^ {2}}{x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \iint_ {D} \frac {r ^ {2} (\cos \theta - \sin \theta) ^ {2}}{r ^ {2}} \cdot r \mathrm {d} r \mathrm {d} \theta &= \iint_ {D} (\cos \theta - \sin \theta) ^ {2} \cdot r \mathrm {d} r \mathrm {d} \theta \\ &= \int_ {0} ^ {\frac {\pi}{2}} (\cos \theta - \sin \theta) ^ {2} \mathrm {d} \theta \int_ {0} ^ {2} r \mathrm {d} r + \int_ {\frac {\pi}{2}} ^ {\pi} (\cos \theta - \sin \theta) ^ {2} \mathrm {d} \theta \int_ {0} ^ {\frac {2}{\sin \theta - \cos \theta}} r \mathrm {d} r \\ &= 2 \int_ {0} ^ {\frac {\pi}{2}} (1 - 2 \sin \theta \cos \theta) \mathrm {d} \theta + \int_ {\frac {\pi}{2}} ^ {\pi} (\cos \theta - \sin \theta) ^ {2} \cdot \frac {r ^ {2}}{2} \Bigg | _ {0} ^ {\frac {2}{\sin \theta - \cos \theta}} \mathrm {d} \theta \\ &= 2 \left(\frac {\pi}{2} - \sin^ {2} \theta \Big | _ {0} ^ {\frac {\pi}{2}}\right) + \int_ {\frac {\pi}{2}} ^ {\pi} (\cos \theta - \sin \theta) ^ {2} \cdot \frac {2}{(\sin \theta - \cos \theta) ^ {2}} \mathrm {d} \theta \\ &= \pi - 2 + 2 \times \left(\pi - \frac {\pi}{2}\right) = 2 \pi - 2. \end{aligned}</equation>

---

**2016年第15题 | 解答题 | 10分**

15. (本题满分10分）已知平面区域<equation>D=\left\{(r,\theta)\mid 2\leqslant r\leqslant 2(1+\cos \theta),-\frac{\pi}{2}\leqslant \theta \leqslant \frac{\pi}{2}\right\}</equation>，计算二重积分<equation>\iint_{D}x\mathrm{d}x\mathrm{d}y.</equation>

**答案:**#<equation>5 \pi +\frac{3 2}{3}</equation>

**解析:**<equation>x=r\cos \theta ,y=r\sin \theta</equation>则<equation>\begin{aligned} \iint_ {D} x \mathrm {d} x \mathrm {d} y &= \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {2} ^ {2 (1 + \cos \theta)} r ^ {2} \cos \theta \mathrm {d} r = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \cos \theta \cdot \frac {8 (1 + \cos \theta) ^ {3} - 8}{3} \mathrm {d} \theta \\ &= \frac {8}{3} \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \left(\cos^ {4} \theta + 3 \cos^ {3} \theta + 3 \cos^ {2} \theta\right) \mathrm {d} \theta \\ &= \frac {1 6}{3} \int_ {0} ^ {\frac {\pi}{2}} \cos^ {4} \theta \mathrm {d} \theta + 1 6 \int_ {0} ^ {\frac {\pi}{2}} \cos^ {3} \theta \mathrm {d} \theta + 1 6 \int_ {0} ^ {\frac {\pi}{2}} \cos^ {2} \theta \mathrm {d} \theta \\ \frac {\text {华 里 士公 式}}{} \frac {1 6}{3} \times \frac {3}{4} \times \frac {1}{2} \times \frac {\pi}{2} + 1 6 \times \frac {2}{3} + 1 6 \times \frac {1}{2} \times \frac {\pi}{2} \\ &= 5 \pi + \frac {3 2}{3}. \end{aligned}</equation>

---

**2015年第12题 | 填空题 | 4分**

12. 设<equation>\Omega</equation>是由平面<equation>x+y+z=1</equation>与三个坐标平面所围成的空间区域，则<equation>\iiint\limits_{\Omega} ( x+2 y+3 z ) \mathrm{d} x \mathrm{d} y \mathrm{d} z=</equation>___

**解析:**解 （法一）由轮换对称性知，<equation>\iiint_ {\Omega} x \mathrm {d} x \mathrm {d} y \mathrm {d} z = \iiint_ {\Omega} y \mathrm {d} x \mathrm {d} y \mathrm {d} z = \iiint_ {\Omega} z \mathrm {d} x \mathrm {d} y \mathrm {d} z.</equation>又<equation>\varOmega=\{(x,y,z)\mid(y,z)\in D_{x},0\leqslant x\leqslant 1\}</equation>，其中<equation>D_{x}=\{(y,z)\mid y+z\leqslant 1-x,y\geqslant 0,z\geqslant 0\}</equation>，其面积为<equation>\frac{(1-x)^{2}}{2}</equation>，故<equation>\begin{aligned} \iiint_ {\Omega} (x + 2 y + 3 z) \mathrm {d} x \mathrm {d} y \mathrm {d} z &= 6 \iiint_ {\Omega} x \mathrm {d} x \mathrm {d} y \mathrm {d} z = 6 \int_ {0} ^ {1} x \mathrm {d} x \iint_ {D _ {x}} \mathrm {d} y \mathrm {d} z \\ &= 6 \int_ {0} ^ {1} x \cdot \frac {(1 - x) ^ {2}}{2} \mathrm {d} x \\ &= 3 \int_ {0} ^ {1} \left(x ^ {3} - 2 x ^ {2} + x\right) \mathrm {d} x = \frac {1}{4}. \end{aligned}</equation>（法二）由题设知，<equation>\Omega = \left\{(x, y, z) \mid 0 \leqslant z \leqslant 1 - x - y, 0 \leqslant y \leqslant 1 - x, 0 \leqslant x \leqslant 1 \right\}.</equation>因此，<equation>\begin{aligned} \iiint_ {\Omega} (x + 2 y + 3 z) \mathrm {d} v \xlongequal {\text {轮 换 对称 性}} 6 \iiint_ {\Omega} z \mathrm {d} v &= 6 \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {1 - x} \mathrm {d} y \int_ {0} ^ {1 - x - y} z \mathrm {d} z \\ &= 6 \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {1 - x} \frac {\left(1 - x - y\right) ^ {2}}{2} \mathrm {d} y = 6 \int_ {0} ^ {1} \frac {\left(y + x - 1\right) ^ {3}}{6} \Big | _ {0} ^ {1 - x} \mathrm {d} x \\ &= 6 \int_ {0} ^ {1} \frac {\left(1 - x\right) ^ {3}}{6} \mathrm {d} x = \int_ {0} ^ {1} (1 - x) ^ {3} \mathrm {d} x \xlongequal {t = 1 - x} \int_ {0} ^ {1} t ^ {3} \mathrm {d} t = \frac {1}{4}. \end{aligned}</equation>

---

**2011年第19题 | 解答题 | 10分**

19. (本题满分11分)

已知函数 f(x,y)具有二阶连续偏导数，且<equation>f ( 1, y )=0, f ( x, 1 )=0, \iint_{D} f ( x, y ) \mathrm{d} x \mathrm{d} y=a</equation>，其中 D={（x,y）|0≤x≤ 1,0≤y≤1}，计算二重积分<equation>I=\iint_{D} x y f_{xy}^{\prime \prime}(x,y)\mathrm{d} x \mathrm{d} y.</equation>

**解析:**由于<equation>f_{xy}^{\prime \prime}(x,y)</equation>是<equation>f_x^{\prime}(x,y)</equation>对<equation>y</equation>的偏导数，故对每个固定的<equation>x,f_{xy}^{\prime \prime}(x,y)\mathrm{d}y = \mathrm{d}[f_x^{\prime}(x,y)]</equation><equation>\begin{aligned} I &= \iint_ {D} x y f _ {x y} ^ {\prime \prime} (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} x \mathrm {d} x \int_ {0} ^ {1} y f _ {x y} ^ {\prime \prime} (x, y) \mathrm {d} y = \int_ {0} ^ {1} x \mathrm {d} x \int_ {0} ^ {1} y \mathrm {d} \left[ f _ {x} ^ {\prime} (x, y) \right] \\ \underline {{\text {分 部 积 分}}} \int_ {0} ^ {1} x \left[ y f _ {x} ^ {\prime} (x, y) \right| _ {y = 0} ^ {y = 1} - \int_ {0} ^ {1} f _ {x} ^ {\prime} (x, y) \mathrm {d} y \Bigg ] \mathrm {d} x &= \int_ {0} ^ {1} x f _ {x} ^ {\prime} (x, 1) \mathrm {d} x - \int_ {0} ^ {1} x \mathrm {d} x \int_ {0} ^ {1} f _ {x} ^ {\prime} (x, y) \mathrm {d} y. \end{aligned}</equation>由于<equation>f ( x, 1 ) = 0</equation>，即一元函数<equation>f ( x, 1 )</equation>是关于 x的常函数，故<equation>f_{x}^{\prime}(x,1)=0.</equation>又由于 D为矩形区域，故交换二次积分的积分次序可得，<equation>\int_ {0} ^ {1} x \mathrm {d} x \int_ {0} ^ {1} f _ {x} ^ {\prime} (x, y) \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {1} x f _ {x} ^ {\prime} (x, y) \mathrm {d} x.</equation>从而，<equation>\begin{aligned} I &= 0 - \int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {1} x f _ {x} ^ {\prime} (x, y) \mathrm {d} x = - \int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {1} x \mathrm {d} [ f (x, y) ] \\ \frac {\mathrm {分 部 积 分}}{} - \int_ {0} ^ {1} \left[ x f (x, y) \mid_ {x = 0} ^ {x = 1} - \int_ {0} ^ {1} f (x, y) \mathrm {d} x \right] \mathrm {d} y &= - \int_ {0} ^ {1} f (1, y) \mathrm {d} y + \int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {1} f (x, y) \mathrm {d} x \\ \frac {f (1 , y) = 0}{\mathrm {一}} \int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {1} f (x, y) \mathrm {d} x &= \iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = a. \end{aligned}</equation>

---

**2009年第12题 | 填空题 | 4分**

12. 设<equation>\Omega=\{(x,y,z)\mid x^{2}+y^{2}+z^{2}\leqslant1\}</equation>，则<equation>\iiint\limits_{\Omega}z^{2}\mathrm{d}x\mathrm{d}y\mathrm{d}z=</equation>___

**答案:**##<equation>\frac{4}{1 5}\pi.</equation>

**解析:**解 （法一）由轮换对称性知，<equation>\iiint_ {\Omega} z ^ {2} \mathrm {d} x \mathrm {d} y \mathrm {d} z = \iiint_ {\Omega} y ^ {2} \mathrm {d} x \mathrm {d} y \mathrm {d} z = \iiint_ {\Omega} x ^ {2} \mathrm {d} x \mathrm {d} y \mathrm {d} z,</equation>于是<equation>\begin{aligned} \iiint_ {\Omega} z ^ {2} \mathrm {d} x \mathrm {d} y \mathrm {d} z &= \frac {1}{3} \iiint_ {\Omega} \left(x ^ {2} + y ^ {2} + z ^ {2}\right) \mathrm {d} x \mathrm {d} y \mathrm {d} z \\ &= \frac {1}{3} \int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {0} ^ {\pi} \mathrm {d} \varphi \int_ {0} ^ {1} r ^ {2} \cdot r ^ {2} \sin \varphi \mathrm {d} r \quad \mathrm {注 意 这里 利用 换 元 公 式 时}, \\ &= \frac {2 \pi}{3} \int_ {0} ^ {\pi} \sin \varphi \mathrm {d} \varphi \int_ {0} ^ {1} r ^ {4} \mathrm {d} r = \frac {2 \pi}{3} \cdot 2 \cdot \frac {1}{5} = \frac {4}{1 5} \pi . \end{aligned}</equation>（法二）令<equation>\left\{ \begin{array}{l}x = r\sin \varphi \cos \theta ,\\ y = r\sin \varphi \sin \theta ,0\leqslant \varphi \leqslant \pi ,0\leqslant \theta \leqslant 2\pi ,0\leqslant r\leqslant 1,\\ z = r\cos \varphi , \end{array} \right.</equation>则<equation>\begin{aligned} \iiint_ {\Omega} z ^ {2} \mathrm {d} x \mathrm {d} y \mathrm {d} z &= \int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {0} ^ {\pi} \mathrm {d} \varphi \int_ {0} ^ {1} \left(r ^ {2} \cos^ {2} \varphi \cdot r ^ {2} \sin \varphi\right) \mathrm {d} r \\ &= 2 \pi \cdot \left[ - \int_ {0} ^ {\pi} \cos^ {2} \varphi \mathrm {d} (\cos \varphi) \right] \cdot \int_ {0} ^ {1} r ^ {4} \mathrm {d} r \\ &= 2 \pi \cdot \left(\left. - \frac {\cos^ {3} \varphi}{3} \right| _ {0} ^ {\pi}\right) \cdot \frac {1}{5} = \frac {4}{1 5} \pi . \end{aligned}</equation>

---


