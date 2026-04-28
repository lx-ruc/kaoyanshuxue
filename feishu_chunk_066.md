#### 第一类曲面积分

**2017年第19题 | 解答题 | 10分**

19. (本题满分10分)

设薄片型物体 S是圆雉面<equation>z=\sqrt{x^{2}+y^{2}}</equation>被柱面<equation>z^{2}=2 x</equation>割下的有限部分，其上任一点的密度为<equation>\mu(x,y,z)=</equation><equation>9 \sqrt{x^{2}+y^{2}+z^{2}}.</equation>记圆雉面与柱面的交线为 C.

I. 求 C在 xOy平面上的投影曲线的方程；

II. 求 S的质量 M.

**答案:**<equation>\begin{array}{l} (\mathrm {I}) \left\{ \begin{array}{l} x ^ {2} + y ^ {2} = 2 x, \\ z = 0; \end{array} \right. \\ (\mathrm {I I}) 6 4. \\ \end{array}</equation>

**解析:**解（I）由题设知，圆锥面与柱面的交线 C的方程为<equation>\left\{\begin{array}{l l}z=\sqrt{x^{2}+y^{2}},\\ z^{2}=2 x, \end{array} \right.</equation>消去 z得到<equation>x^{2}+y^{2}= 2 x</equation>，于是 C在 xOy平面上的投影曲线的方程为<equation>\left\{ \begin{array}{l} x ^ {2} + y ^ {2} = 2 x, \\ z = 0. \end{array} \right.</equation>（Ⅱ）设<equation>D_{xy}=\{(x,y)|x^{2}+y^{2}\leqslant 2x\}</equation>，则曲面 S的方程为<equation>z=\sqrt{x^{2}+y^{2}},(x,y)\in D_{xy}</equation>，从而 S的质量为<equation>\begin{aligned} M &= \iint_ {S} \mu (x, y, z) \mathrm {d} S = \iint_ {S} 9 \sqrt {x ^ {2} + y ^ {2} + z ^ {2}} \mathrm {d} S \xlongequal {z = \sqrt {x ^ {2} + y ^ {2}}} \iint_ {S} 9 \sqrt {2 \left(x ^ {2} + y ^ {2}\right)} \mathrm {d} S \\ &= \iint_ {D _ {x y}} 9 \sqrt {2 \left(x ^ {2} + y ^ {2}\right)} \cdot \sqrt {1 + \left(\frac {\partial z}{\partial x}\right) ^ {2} + \left(\frac {\partial z}{\partial y}\right) ^ {2}} \mathrm {d} x \mathrm {d} y \\ &= \iint_ {D _ {x y}} 9 \sqrt {2 \left(x ^ {2} + y ^ {2}\right)} \cdot \sqrt {1 + \left(\frac {x}{\sqrt {x ^ {2} + y ^ {2}}}\right) ^ {2} + \left(\frac {y}{\sqrt {x ^ {2} + y ^ {2}}}\right) ^ {2}} \mathrm {d} x \mathrm {d} y \\ &= 1 8 \iint_ {D _ {x y}} \sqrt {x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y. \end{aligned}</equation>令<equation>x = r\cos \theta ,y = r\sin \theta</equation>，由<equation>x^{2} + y^{2}\leqslant 2x</equation>知，<equation>r^{2}\leqslant 2r\cos \theta</equation>，即<equation>r\leqslant 2\cos \theta</equation>.如下图，<equation>D_{xy}</equation>在极坐标

变换下对应区域<equation>D = \left\{(r,\theta)\mid 0\leqslant r\leqslant 2\cos \theta , - \frac{\pi}{2}\leqslant \theta \leqslant \frac{\pi}{2}\right\}</equation>，从而<equation>\begin{aligned} M &= 1 8 \iint_ {D _ {x y}} \sqrt {x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y = 1 8 \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {2 \cos \theta} r \cdot r \mathrm {d} r \\ &= 4 8 \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \cos^ {3} \theta \mathrm {d} \theta = 9 6 \int_ {0} ^ {\frac {\pi}{2}} \cos^ {3} \theta \mathrm {d} \theta \\ &= 9 6 \times \frac {2}{3} = 6 4. \end{aligned}</equation>

---

**2012年第12题 | 填空题 | 4分**

12. 设<equation>\Sigma=\{(x,y,z)\mid x+y+z=1,x\geqslant0,y\geqslant0,z\geqslant0\}</equation>，则<equation>\iint\limits_{\Sigma}y^{2}\mathrm{d}S=</equation>___

**答案:**#<equation>\frac{\sqrt{3}}{12}</equation>

**解析:**分析 本题主要考查第一类曲面积分的计算. 一般将其化为重积分后再计算.

若曲面<equation>\Sigma</equation>的方程为<equation>z = z(x,y),(x,y)\in D_{xy}</equation>，且<equation>z(x,y)</equation>在<equation>D_{xy}</equation>上有连续偏导数，<equation>f(x,y,z)</equation>在<equation>\Sigma</equation>上连续，则<equation>\iint_ {\Sigma} f (x, y, z) \mathrm {d} S = \iint_ {D _ {x y}} f (x, y, z (x, y)) \sqrt {1 + \left(\frac {\partial z}{\partial x}\right) ^ {2} + \left(\frac {\partial z}{\partial y}\right) ^ {2}} \mathrm {d} x \mathrm {d} y.</equation>解 曲面<equation>\varSigma=\{(x,y,z)\mid z=1-x-y,x\geqslant0,y\geqslant0,z\geqslant0\}</equation>在 xOy平面上的投影区域为<equation>D_{xy}=\{(x,y)\mid 0\leqslant y\leqslant1,0\leqslant x\leqslant1-y\}</equation>，于是<equation>\begin{aligned} \iint_ {\Sigma} y ^ {2} \mathrm {d} S &= \iint_ {D _ {x y}} y ^ {2} \sqrt {1 + \left(\frac {\partial z}{\partial x}\right) ^ {2} + \left(\frac {\partial z}{\partial y}\right) ^ {2}} \mathrm {d} x \mathrm {d} y \\ &= \iint_ {D _ {x y}} y ^ {2} \sqrt {1 + 1 + 1} \mathrm {d} x \mathrm {d} y = \sqrt {3} \iint_ {D _ {x y}} y ^ {2} \mathrm {d} x \mathrm {d} y \\ &= \sqrt {3} \int_ {0} ^ {1} y ^ {2} \mathrm {d} y \int_ {0} ^ {1 - y} \mathrm {d} x = \sqrt {3} \int_ {0} ^ {1} y ^ {2} (1 - y) \mathrm {d} y = \frac {\sqrt {3}}{1 2}. \end{aligned}</equation>

---

**2010年第19题 | 解答题 | 10分**

19. (本题满分10分)

设 P为椭球面 S：<equation>x^{2}+y^{2}+z^{2}-yz=1</equation>上的动点，若 S在点 P处的切平面与 xOy面垂直，求点 P的轨迹 C，并计算曲面积分 I =<equation>\iint\limits_{\Sigma}\frac{(x+\sqrt{3})|y-2z|}{\sqrt{4+y^{2}+z^{2}-4yz}} \mathrm{d} S</equation>，其中<equation>\varSigma</equation>是椭球面 S位于曲线 C上方的部分.

**答案:**(19) 点P的轨迹C为<equation>\left\{\begin{array}{l l}x^{2}+y^{2}+z^{2}-yz=1\\ y=2z,\end{array}\right.</equation>或者<equation>\left\{\begin{array}{l l}x^{2}+\frac{3}{4} y^{2}=1\\ y=2z,\end{array}\right.</equation>曲面积分为<equation>I=2\pi.</equation>

**解析:**解设点 P的坐标为（x,y,z），则椭球面 S在点 P处的法向量为（2x，2y-z，2z-y）.又 xOy面的法向量可取为（0,0,1），故由 S在点 P处的切平面与 xOy面垂直知，<equation>(2 x, 2 y - z, 2 z - y) \cdot (0, 0, 1) = 0,</equation>即有<equation>y = 2z</equation>. 由于点<equation>P</equation>在椭球面<equation>S</equation>上，故点<equation>P</equation>的轨迹<equation>C</equation>为<equation>\left\{ \begin{array}{l l} x ^ {2} + y ^ {2} + z ^ {2} - y z = 1, \\ y = 2 z, \end{array} \right. \text {或 者} \left\{ \begin{array}{l l} x ^ {2} + \frac {3}{4} y ^ {2} = 1, \\ y = 2 z. \end{array} \right.</equation>下面用两种方法求曲面积分 I.

（法一）<equation>\varSigma</equation>在xOy面上的投影区域为<equation>D_{xy}=\left\{(x,y)\mid x^{2}+\frac{3}{4} y^{2}\leqslant 1\right\}</equation>，其面积为<equation>\pi \cdot 1\cdot \frac{2}{\sqrt{3}}=\frac{2}{\sqrt{3}}\pi.</equation>对方程<equation>x^{2}+y^{2}+z^{2}-yz=1</equation>两边关于x,y分别求偏导数，得<equation>2 x + 2 z \frac {\partial z}{\partial x} - y \frac {\partial z}{\partial x} = 0, \quad 2 y + 2 z \frac {\partial z}{\partial y} - z - y \frac {\partial z}{\partial y} = 0,</equation>解得<equation>\frac{\partial z}{\partial x} = \frac{2x}{y - 2z},\frac{\partial z}{\partial y} = \frac{2y - z}{y - 2z}</equation>. 在<equation>\varSigma</equation>上，<equation>x^{2}+y^{2}+z^{2}-yz=1</equation>，故<equation>\begin{aligned} \sqrt {1 + \left(\frac {\partial z}{\partial x}\right) ^ {2} + \left(\frac {\partial z}{\partial y}\right) ^ {2}} &= \frac {\sqrt {4 x ^ {2} + 5 y ^ {2} + 5 z ^ {2} - 8 y z}}{| y - 2 z |} = \frac {\sqrt {4 \left(x ^ {2} + y ^ {2} + z ^ {2} - y z\right) + y ^ {2} + z ^ {2} - 4 y z}}{| y - 2 z |} \\ &= \frac {\sqrt {4 + y ^ {2} + z ^ {2} - 4 y z}}{| y - 2 z |}. \end{aligned}</equation>从而<equation>\begin{aligned} I &= \iint_ {\Sigma} \frac {\left(x + \sqrt {3}\right) \mid y - 2 z \mid}{\sqrt {4 + y ^ {2} + z ^ {2}} - 4 y z} \mathrm {d} S = \iint_ {D _ {x y}} \frac {\left(x + \sqrt {3}\right) \mid y - 2 z \mid}{\sqrt {4 + y ^ {2} + z ^ {2}} - 4 y z} \cdot \sqrt {1 + \left(\frac {\partial z}{\partial x}\right) ^ {2} + \left(\frac {\partial z}{\partial y}\right) ^ {2}} \mathrm {d} x \mathrm {d} y \\ &= \iint_ {D _ {x y}} \left(x + \sqrt {3}\right) \mathrm {d} x \mathrm {d} y \stackrel {\text {对 称 性}} {=} 0 + \iint_ {D _ {x y}} \sqrt {3} \mathrm {d} x \mathrm {d} y = \sqrt {3} \cdot \frac {2}{\sqrt {3}} \pi = 2 \pi . \end{aligned}</equation>（法二）<equation>\varSigma</equation>在 xOy面上的投影区域为<equation>D_{xy}=\left\{(x,y)\left|x^{2}+\frac{3}{4} y^{2}\leqslant 1\right.\right\}</equation>，其面积为<equation>\pi\cdot1\cdot\frac{2}{\sqrt{3}}=\frac{2}{\sqrt{3}}\pi.</equation><equation>\varSigma</equation>上任一点的法向量为（2x，2y-z，2z-y），其方向余弦<equation>\cos \gamma</equation>满足<equation>| \cos \gamma | = \frac {\left| 2 z - y \right|}{\sqrt {\left(2 x\right) ^ {2} + \left(2 y - z\right) ^ {2} + \left(2 z - y\right) ^ {2}}} = \frac {\left| 2 z - y \right|}{\sqrt {4 x ^ {2} + 5 y ^ {2} + 5 z ^ {2} - 8 y z}}.</equation>又<equation>\Sigma</equation>上的点满足<equation>x^{2}+y^{2}+z^{2}-yz=1</equation>，故有<equation>|\cos \gamma |=\frac{|2z-y|}{\sqrt{4+y^{2}+z^{2}-4yz}}</equation>，从而<equation>\begin{aligned} I &= \iint_ {\Sigma} \frac {(x + \sqrt {3}) | y - 2 z |}{\sqrt {4 + y ^ {2} + z ^ {2}} - 4 y z} \mathrm {d} S = \iint_ {\Sigma} (x + \sqrt {3}) | \cos \gamma | \mathrm {d} S \\ &= \iint_ {D _ {x y}} (x + \sqrt {3}) \mathrm {d} x \mathrm {d} y \xlongequal {\text {对称性}} 0 + \iint_ {D _ {x y}} \sqrt {3} \mathrm {d} x \mathrm {d} y \\ &= \sqrt {3} \cdot \frac {2}{\sqrt {3}} \pi = 2 \pi . \end{aligned}</equation>

---


