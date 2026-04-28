#### 重积分的应用

**2019年第19题 | 解答题 | 10分**

19. (本题满分10分）

设<equation>\Omega</equation>是由锥面<equation>x^{2}+(y-z)^{2}=(1-z)^{2}(0\leqslant z\leqslant 1)</equation>与平面 z=0围成的锥体，求<equation>\Omega</equation>的形心坐标.

**答案:**<equation>\varOmega</equation>的形心坐标为<equation>\left( 0,\frac{1}{4},\frac{1}{4}\right).</equation>

**解析:**解 由锥面方程可知，<equation>\varOmega</equation>是一个介于 xOy面与平面 z=1之间的锥体，且<equation>\varOmega</equation>关于 yOz面对称，故由对称性可知，<equation>\overline{x}=0.</equation>下面计算<equation>\varOmega</equation>的体积V.

令<equation>z = 0</equation>，可得锥面与<equation>xOy</equation>面的交线为<equation>x^{2} + y^{2} = 1</equation>，故<equation>\varOmega</equation>的底面为一个圆心在原点、半径为1的圆，面积为<equation>\pi</equation>.又因为<equation>0\leqslant z\leqslant 1,\varOmega</equation>的高为1，所以由锥体的体积公式可知，<equation>\varOmega</equation>的体积<equation>V = \frac{1}{3}\pi</equation>下面分别计算<equation>\bar{z},\bar{y}。</equation>沿平行于<equation>x O y</equation>面的方向作<equation>\varOmega</equation>的截面，即以平面<equation>Z=z</equation>截<equation>\varOmega</equation>，所得截面记为<equation>D_{z}.</equation><equation>D_{z}</equation>为圆心在（0，z，z）、半径为1-z的圆盘区域.写出<equation>Z=z</equation>上的<equation>D_{z}</equation>的表示.<equation>D _ {z} = \left\{(x, y) \mid x ^ {2} + (y - z) ^ {2} \leqslant (1 - z) ^ {2} \right\}.</equation>于是，<equation>\Omega = \left\{(x, y, z) \mid (x, y) \in D _ {z}, 0 \leqslant z \leqslant 1 \right\}.</equation>利用“先重后单”的次序计算积分.<equation>\begin{aligned} \iiint_ {\Omega} z \mathrm {d} x \mathrm {d} y \mathrm {d} z &= \int_ {0} ^ {1} z \mathrm {d} z \iint_ {D _ {z}} \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} z \cdot \left(D _ {z} \text {的 面 积}\right) \mathrm {d} z = \pi \int_ {0} ^ {1} z (1 - z) ^ {2} \mathrm {d} z \\ &= \pi \cdot \int_ {0} ^ {1} \left(z ^ {3} - 2 z ^ {2} + z\right) \mathrm {d} z = \pi \cdot \left(\frac {1}{4} - \frac {2}{3} + \frac {1}{2}\right) = \frac {\pi}{1 2}. \end{aligned}</equation><equation>\begin{aligned} \iiint_ {\Omega} y \mathrm {d} x \mathrm {d} y \mathrm {d} z &= \int_ {0} ^ {1} \mathrm {d} z \iint_ {D _ {z}} y \mathrm {d} x \mathrm {d} y \frac {x = r \cos \theta}{y = z + r \sin \theta} \int_ {0} ^ {1} \mathrm {d} z \int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {0} ^ {1 - z} (z + r \sin \theta) \cdot r \mathrm {d} r \\ &= \int_ {0} ^ {1} \mathrm {d} z \int_ {0} ^ {2 \pi} \left(z \cdot \frac {r ^ {2}}{2} + \frac {r ^ {3}}{3} \cdot \sin \theta\right) \Bigg | _ {0} ^ {1 - z} \mathrm {d} \theta = \int_ {0} ^ {1} 2 \pi \cdot z \cdot \frac {(1 - z) ^ {2}}{2} \mathrm {d} z \\ &= \pi \int_ {0} ^ {1} z (1 - z) ^ {2} \mathrm {d} z = \frac {\pi}{1 2}. \end{aligned}</equation>因此，<equation>\bar{y} = \frac{\frac{\pi}{12}}{\frac{\pi}{3}} = \frac{1}{4},\bar{z} = \frac{\frac{\pi}{12}}{\frac{\pi}{3}} = \frac{1}{4}.</equation>综上所述，<equation>\varOmega</equation>的形心坐标为<equation>\left(0,\frac{1}{4},\frac{1}{4}\right)</equation>

---

**2013年第19题 | 解答题 | 10分**

19. (本题满分10分)

19. (本题满分10分)

设直线 L过 A(1,0,0),B(0,1,1)两点，将 L绕 z轴旋转一周得到曲面<equation>\Sigma</equation><equation>\Sigma</equation>与平面<equation>z=0,z=2</equation>所围成的立体为<equation>\Omega</equation>.

I. 求曲面<equation>\Sigma</equation>的方程;

II. 求<equation>\Omega</equation>的形心坐标.

**答案:**(19) ( I )<equation>x^{2}+y^{2}=2 z^{2}-2 z+1;</equation>

**解析:**解（I）直线 L的方程为<equation>\frac{x-1}{-1}=\frac{y}{1}=\frac{z}{1}</equation>即<equation>\left\{ \begin{array}{l} x = 1 - z, \\ y = z, \end{array} \right.</equation>从而曲面<equation>\Sigma</equation>的方程为<equation>x^{2} + y^{2} = (1 - z)^{2} + z^{2}</equation>，即<equation>x^{2} + y^{2} = 2z^{2} - 2z + 1.</equation>（Ⅱ）设<equation>\varOmega</equation>的形心坐标为<equation>(\bar{x},\bar{y},\bar{z})</equation>.由曲面<equation>\Sigma</equation>的方程知，<equation>\varOmega</equation>关于<equation>xOz,yOz</equation>面对称，从而<equation>\bar {x} = \frac {\iiint_ {\Omega} x \mathrm {d} x \mathrm {d} y \mathrm {d} z}{\iiint_ {\Omega} \mathrm {d} x \mathrm {d} y \mathrm {d} z} = 0, \quad \bar {y} = \frac {\iiint_ {\Omega} y \mathrm {d} x \mathrm {d} y \mathrm {d} z}{\iiint_ {\Omega} \mathrm {d} x \mathrm {d} y \mathrm {d} z} = 0.</equation>记<equation>D_{z} = \{(x,y)\mid x^{2} + y^{2}\leqslant 2z^{2} - 2z + 1\}</equation>，则<equation>\iiint_ {\Omega} z \mathrm {d} x \mathrm {d} y \mathrm {d} z = \int_ {0} ^ {2} z \mathrm {d} z \iint_ {D _ {z}} \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {2} z \cdot \pi \left(2 z ^ {2} - 2 z + 1\right) \mathrm {d} z = \frac {1 4}{3} \pi ,</equation><equation>\iiint_ {\Omega} \mathrm {d} x \mathrm {d} y \mathrm {d} z = \int_ {0} ^ {2} \mathrm {d} z \iint_ {D _ {z}} \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {2} \pi \left(2 z ^ {2} - 2 z + 1\right) \mathrm {d} z = \frac {1 0}{3} \pi .</equation>于是<equation>\bar{z} = \frac{\iiint \Omega z\mathrm{d}x\mathrm{d}y\mathrm{d}z}{\iiint \Omega \mathrm{d}x\mathrm{d}y\mathrm{d}z} = \frac{7}{5}</equation>. 因此<equation>\varOmega</equation>的形心坐标为<equation>\left(0,0,\frac{7}{5}\right)</equation>.

---

**2010年第12题 | 填空题 | 4分**

12. 设<equation>\varOmega = \{(x,y,z) \mid x^2 + y^2 \leqslant z \leqslant 1\}</equation>, 则<equation>\varOmega</equation>的形心的坚坐标<equation>\bar{z} =</equation>___

**解析:**解（法一）由题设知，<equation>\varOmega=\{(x,y,z)\mid(x,y)\in D_{z},0\leqslant z\leqslant 1\}</equation>，其中<equation>D_{z}=\{(x,y)\mid x^{2}+y^{2}\leqslant z\}</equation>且<equation>D_{z}</equation>的面积为<equation>\pi z</equation>，从而<equation>\bar {z} = \frac {\iiint_ {\Omega} z \mathrm {d} x \mathrm {d} y \mathrm {d} z}{\iiint_ {\Omega} \mathrm {d} x \mathrm {d} y \mathrm {d} z} = \frac {\int_ {0} ^ {1} z \mathrm {d} z \iint_ {D _ {z}} \mathrm {d} x \mathrm {d} y}{\int_ {0} ^ {1} \mathrm {d} z \iint_ {D _ {z}} \mathrm {d} x \mathrm {d} y} = \frac {\int_ {0} ^ {1} \left(z \cdot \pi z\right) \mathrm {d} z}{\int_ {0} ^ {1} \pi z \mathrm {d} z} = \frac {\frac {\pi}{3}}{\frac {\pi}{2}} = \frac {2}{3}.</equation>（法二）由题设知，<equation>\varOmega=\{(x,y,z)\mid(x,y)\in D_{xy},x^{2}+y^{2}\leqslant z\leqslant 1\}</equation>，其中<equation>D_{xy}=\{(x,y)\mid x^{2}+y^{2}\leqslant 1\}</equation>，从而<equation>\begin{aligned} \bar {z} &= \frac {\iiint_ {\Omega} z \mathrm {d} x \mathrm {d} y \mathrm {d} z}{\iiint_ {\Omega} \mathrm {d} x \mathrm {d} y \mathrm {d} z} = \frac {\iint_ {D _ {x y}} \mathrm {d} x \mathrm {d} y \int_ {x ^ {2} + y ^ {2}} ^ {1} z \mathrm {d} z}{\iint_ {D _ {x y}} \mathrm {d} x \mathrm {d} y \int_ {x ^ {2} + y ^ {2}} ^ {1} \mathrm {d} z} = \frac {\frac {1}{2} \iint_ {D _ {x y}} \left[ 1 - \left(x ^ {2} + y ^ {2}\right) ^ {2} \right] \mathrm {d} x \mathrm {d} y}{\iint_ {D _ {x y}} \left(1 - x ^ {2} - y ^ {2}\right) \mathrm {d} x \mathrm {d} y} \\ \frac {x = r \cos \theta}{y = r \sin \theta} \frac {\frac {1}{2} \int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {0} ^ {1} \left(1 - r ^ {4}\right) r \mathrm {d} r}{\int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {0} ^ {1} \left(1 - r ^ {2}\right) r \mathrm {d} r} &= \frac {\frac {\pi}{3}}{\frac {\pi}{2}} = \frac {2}{3}. \end{aligned}</equation>

---


