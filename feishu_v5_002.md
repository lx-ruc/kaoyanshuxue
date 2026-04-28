---


#### 第二类曲面积分


**2025年第20题 | 解答题 | 12分**
20. 设<equation>\Sigma</equation>是由直线<equation>\left\{\begin{array}{l l}x=0\\ y=0\end{array}\right.</equation>，绕直线<equation>\left\{\begin{array}{l l}x=t\\ y=t\\ z=t\end{array}\right.</equation>（t为参数）旋转一周得到的曲面，<equation>\Sigma_{1}</equation>是<equation>\Sigma</equation>介于平面 x+y+z=0与平面 x+y+z=1之间部分的外侧，计算曲面积分<equation>I=\iint_{\Sigma_{1}}x\mathrm{d}y\mathrm{d}z+(y+1)\mathrm{d}z\mathrm{d}x+(z+2)\mathrm{d}x\mathrm{d}y.</equation>
**解析: **解直线<equation>\left\{\begin{array}{l l}x=0\\ y=0\end{array}\right.</equation>可视为z轴，直线<equation>\left\{\begin{array}{l l}x=t,\\ y=t,\\ z=t\end{array}\right.</equation>（t为参数）是以（1，1，1）为方向向量且过原点的直

线，故<equation>\varSigma</equation>是以原点为顶点，直线<equation>\frac{x}{1}=\frac{y}{1}=\frac{z}{1}</equation>为轴（圆锥底面上的高所在直线），且过点（1，0，0），（0，1，0），（0，0，1）的圆锥面.

如图所示，记<equation>\Sigma_{2}</equation>为平面<equation>x + y + z = 1</equation>被<equation>\Sigma</equation>所截得的有限部分，取上侧，则<equation>\Sigma_{1}</equation>与<equation>\Sigma_{2}</equation>共同围成一个圆锥体<equation>\Omega ,\Sigma_{1}\cup \Sigma_{2}</equation>构成<equation>\Omega</equation>的外侧.

圆锥体的底面圆心为平面<equation>x + y + z = 1</equation>与直线<equation>x = y = z</equation>的交点，解得<equation>x = y = z = \frac{1}{3}</equation>，即底面圆心为<equation>\left(\frac{1}{3}, \frac{1}{3}, \frac{1}{3}\right)</equation>. 底面圆的半径为点(0,0,1)

到点<equation>\left(\frac{1}{3},\frac{1}{3},\frac{1}{3}\right)</equation>的距离，即<equation>\sqrt{\frac{1}{9} + \frac{1}{9} + \frac{4}{9}} = \sqrt{\frac{2}{3}}.</equation>圆锥体的高为点（0,0,0）到点<equation>\left(\frac{1}{3},\frac{1}{3},\frac{1}{3}\right)</equation>的距离，即<equation>\sqrt{\frac{1}{9} + \frac{1}{9} + \frac{1}{9}} = \sqrt{\frac{1}{3}}.</equation>于是，<equation>\varOmega</equation>的体积<equation>V = \frac{1}{3}\cdot \frac{2\pi}{3}\cdot \sqrt{\frac{1}{3}} = \frac{2\sqrt{3}\pi}{27}.</equation>根据高斯公式，<equation>\iint_ {\Sigma_ {1} \cup \Sigma_ {2}} x \mathrm {d} y \mathrm {d} z + (y + 1) \mathrm {d} z \mathrm {d} x + (z + 2) \mathrm {d} x \mathrm {d} y = 3 \iiint_ {\Omega} \mathrm {d} v = \frac {2 \sqrt {3} \pi}{9}.</equation>于是，<equation>\iint_ {\Sigma_ {1}} x \mathrm {d} y \mathrm {d} z + (y + 1) \mathrm {d} z \mathrm {d} x + (z + 2) \mathrm {d} x \mathrm {d} y = \frac {2 \sqrt {3} \pi}{9} - \iint_ {\Sigma_ {2}} x \mathrm {d} y \mathrm {d} z + (y + 1) \mathrm {d} z \mathrm {d} x + (z + 2) \mathrm {d} x \mathrm {d} y.</equation>下面计算<equation>\iint\limits_{\Sigma_{2}}x\mathrm{d}y\mathrm{d}z+(y+1)\mathrm{d}z\mathrm{d}x+(z+2)\mathrm{d}x\mathrm{d}y.</equation>由于<equation>\varSigma_{2}</equation>的法向量（1，1，1）的方向余弦<equation>\cos \alpha=\cos \beta=\cos \gamma=\frac{1}{\sqrt{3}}</equation>，故<equation>\mathrm{d}y\mathrm{d}z=\mathrm{d}z\mathrm{d}x=\mathrm{d}x\mathrm{d}y</equation><equation>\begin{aligned} \iint_ {\Sigma_ {2}} x \mathrm {d} y \mathrm {d} z + (y + 1) \mathrm {d} z \mathrm {d} x + (z + 2) \mathrm {d} x \mathrm {d} y \xlongequal {z = 1 - x - y} \iint_ {\Sigma_ {2}} x \mathrm {d} y \mathrm {d} z + (y + 1) \mathrm {d} z \mathrm {d} x + (3 - x - y) \mathrm {d} x \mathrm {d} y \\ &= \iint_ {\Sigma_ {2}} 4 \mathrm {d} x \mathrm {d} y = \frac {4}{\sqrt {3}} \iint_ {\Sigma_ {2}} \mathrm {d} S = \frac {4}{\sqrt {3}} \Sigma_ {2} \text {的 面 积}. \end{aligned}</equation>又因为<equation>\varSigma_{2}</equation>的面积即圆锥体的底面圆面积，所以<equation>\iint_ {\Sigma_ {2}} x \mathrm {d} y \mathrm {d} z + (y + 1) \mathrm {d} z \mathrm {d} x + (z + 2) \mathrm {d} x \mathrm {d} y = \frac {4}{\sqrt {3}} \cdot \frac {2 \pi}{3} = \frac {8 \sqrt {3} \pi}{9}.</equation>因此，<equation>\iint_ {\Sigma_ {1}} x \mathrm {d} y \mathrm {d} z + (y + 1) \mathrm {d} z \mathrm {d} x + (z + 2) \mathrm {d} x \mathrm {d} y = \frac {2 \sqrt {3} \pi}{9} - \frac {8 \sqrt {3} \pi}{9} = - \frac {2 \sqrt {3} \pi}{3}.</equation>

---

**2024年第2题 | 选择题 | 5分 | 答案: A**
2. 设<equation>P=P(x,y,z), Q=Q(x,y,z)</equation>均为连续函数，<equation>\Sigma</equation>为曲面<equation>z=\sqrt{1-x^{2}-y^{2}}</equation><equation>( x \leqslant0, y \geqslant0)</equation>的上侧，则<equation>\iint\limits_{\Sigma} P\mathrm{d}y\mathrm{d}z+ Q\mathrm{d}z\mathrm{d}x=</equation>(    )

A.<equation>\iint\limits_{\Sigma} \left( \frac{x}{z} P+\frac{y}{z} Q \right) \mathrm{d}x\mathrm{d}y</equation>B.<equation>\iint\limits_{\Sigma} \left( -\frac{x}{z} P+\frac{y}{z} Q \right) \mathrm{d}x\mathrm{d}y</equation>C.<equation>\iint\limits_{\Sigma} \left( \frac{x}{z} P-\frac{y}{z} Q \right) \mathrm{d}x\mathrm{d}y</equation>D.<equation>\iint\limits_{\Sigma} \left( -\frac{x}{z} P-\frac{y}{z} Q \right) \mathrm{d}x\mathrm{d}y</equation>
答案: A
**解析: **解 由于曲面<equation>\varSigma</equation>取上侧，故<equation>\varSigma</equation>的法向量与z轴正向成锐角，从而<equation>\varSigma</equation>的法向量<equation>n=(-z_{x}^{\prime},-z_{y}^{\prime},1)</equation>的方向余弦为<equation>\cos \alpha = \frac {- z _ {x} ^ {\prime}}{\sqrt {1 + z _ {x} ^ {\prime 2} + z _ {y} ^ {\prime 2}}}, \quad \cos \beta = \frac {- z _ {y} ^ {\prime}}{\sqrt {1 + z _ {x} ^ {\prime 2} + z _ {y} ^ {\prime 2}}}, \quad \cos \gamma = \frac {1}{\sqrt {1 + z _ {x} ^ {\prime 2} + z _ {y} ^ {\prime 2}}}.</equation>由方向余弦的表达式可得，<equation>\cos \alpha=-z_{x}^{\prime}\cos \gamma, \cos \beta=-z_{y}^{\prime}\cos \gamma</equation>，从而<equation>\mathrm {d} y \mathrm {d} z = \cos \alpha \mathrm {d} S = - z _ {x} ^ {\prime} \cos \gamma \mathrm {d} S = - z _ {x} ^ {\prime} \mathrm {d} x \mathrm {d} y, \mathrm {d} z \mathrm {d} x = \cos \beta \mathrm {d} S = - z _ {y} ^ {\prime} \cos \gamma \mathrm {d} S = - z _ {y} ^ {\prime} \mathrm {d} x \mathrm {d} y.</equation>计算得<equation>z _ {x} ^ {\prime} = \frac {- x}{\sqrt {1 - x ^ {2} - y ^ {2}}} = - \frac {x}{z}, \quad z _ {y} ^ {\prime} = \frac {- y}{\sqrt {1 - x ^ {2} - y ^ {2}}} = - \frac {y}{z}.</equation>于是，<equation>\iint_ {\Sigma} P \mathrm {d} y \mathrm {d} z + Q \mathrm {d} z \mathrm {d} x = \iint_ {\Sigma} \left[ P \cdot \left(- z _ {x} ^ {\prime}\right) + Q \cdot \left(- z _ {y} ^ {\prime}\right) \right] \mathrm {d} x \mathrm {d} y = \iint_ {\Sigma} \left(\frac {x}{z} P + \frac {y}{z} Q\right) \mathrm {d} x \mathrm {d} y.</equation>因此，应选A.

---

**2023年第19题 | 解答题 | 12分**
19. (本题满分12分)

设空间有界区域<equation>\Omega</equation>由柱面<equation>x^{2}+y^{2}=1</equation>与平面 z=0和 x+z=1围成，<equation>\Sigma</equation>为<equation>\Omega</equation>边界曲面的外侧，计算曲面积分<equation>I=\iint_{\Sigma}2xz\mathrm{d}y\mathrm{d}z+xz\cos y\mathrm{d}z\mathrm{d}x+3yz\sin x\mathrm{d}x\mathrm{d}y.</equation>
**答案: **#<equation>I = \frac{5\pi}{4}.</equation>
**解析: **由于<equation>\varSigma</equation>为封闭曲面，且被积函数在<equation>\varOmega</equation>上具有一阶连续偏导数，故可以考虑直接利用高斯公式将第二类曲面积分转化为三重积分.

解 由高斯公式可知，<equation>I = \iiint_ {\Omega} \left(2 z - x z \sin y + 3 y \sin x\right) \mathrm {d} v.</equation>区域<equation>\varOmega</equation>如图所示.注意到<equation>\varOmega</equation>关于zOx面对称，而<equation>xz\sin y</equation>和3ysin x均为关于y的奇函数，故由对称性的结论可知，<equation>\iiint_ {\Omega} \left(2 z - x z \sin y + 3 y \sin x\right) \mathrm {d} v \xlongequal {\text {对称性}} \iiint_ {\Omega} 2 z \mathrm {d} v.</equation>采用先单后重的积分次序.由于<equation>\varOmega</equation>在 xOy面上的投影区域<equation>D=\{(x,y)\mid x^{2}+y^{2}\leqslant 1\}</equation>，D关于坐标轴均对称，且关于变量x,y具有轮换对称性，故<equation>\begin{aligned} \iiint_ {\Omega} 2 z \mathrm {d} v &= \iint_ {D} \mathrm {d} x \mathrm {d} y \int_ {0} ^ {1 - x} 2 z \mathrm {d} z = \iint_ {D} (1 - x) ^ {2} \mathrm {d} x \mathrm {d} y \xlongequal {\text {对称性}} \iint_ {D} \left(1 + x ^ {2}\right) \mathrm {d} x \mathrm {d} y \\ &= \pi + \iint_ {D} x ^ {2} \mathrm {d} x \mathrm {d} y \xlongequal {\text {轮换对称性}} \pi + \frac {1}{2} \iint_ {D} \left(x ^ {2} + y ^ {2}\right) \mathrm {d} x \mathrm {d} y \\ \xlongequal {\text {极 坐 标}} \pi + \frac {1}{2} \int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {0} ^ {1} r ^ {2} \cdot r \mathrm {d} r &= \pi + \frac {\pi}{4} = \frac {5 \pi}{4}. \end{aligned}</equation>

---

**2021年第14题 | 填空题 | 5分**
14. 设<equation>\Sigma</equation>为空间区域<equation>\left\{(x,y,z)\mid x^{2}+4 y^{2}\leqslant 4,0\leqslant z\leqslant 2\right\}</equation>表面的外侧，则曲面积分<equation>\iint\limits_{\Sigma} x^{2}\mathrm{d}y\mathrm{d}z+y^{2}\mathrm{d}z\mathrm{d}x+z\mathrm{d}x\mathrm{d}y=</equation>
**解析: **解空间区域<equation>\varOmega=\left\{(x,y,z)\mid x^{2}+4 y^{2}\leqslant 4,0\leqslant z\leqslant 2\right\}</equation>为椭圆柱面<equation>x^{2}+4 y^{2}=4</equation>，平面z=0以及z=2围成的区域，是一个椭圆柱体.该柱体的底面为椭圆区域<equation>\left\{(x,y)\left| \frac{x^{2}}{4}+y^{2}\leqslant 1\right.\right\}</equation>，面积为<equation>2\pi</equation>，柱体的高为2.<equation>\varSigma</equation>为<equation>\varOmega</equation>的外侧边界.

对曲面积分<equation>\iint_{\Sigma} x^{2}\mathrm{d}y\mathrm{d}z + y^{2}\mathrm{d}z\mathrm{d}x + z\mathrm{d}x\mathrm{d}y</equation>使用高斯公式可得，<equation>\iint_ {\Sigma} x ^ {2} \mathrm {d} y \mathrm {d} z + y ^ {2} \mathrm {d} z \mathrm {d} x + z \mathrm {d} x \mathrm {d} y = \iiint_ {\Omega} (2 x + 2 y + 1) \mathrm {d} v.</equation>由于<equation>\varOmega</equation>关于<equation>yOz</equation>面，<equation>zOx</equation>面均对称，故<equation>\iiint_{\varOmega} x\mathrm{d}v = 0,</equation><equation>\iiint_{\varOmega} y\mathrm{d}v = 0.</equation><equation>\iiint_ {\Omega} (2 x + 2 y + 1) \mathrm {d} v = \iiint_ {\Omega} \mathrm {d} v = \Omega \text {的 体 积} = 2 \pi \times 2 = 4 \pi .</equation>

---

**2020年第18题 | 解答题 | 10分**
18. (本题满分10分)

设<equation>\Sigma</equation>为曲面<equation>z=\sqrt{x^{2}+y^{2}}</equation><equation>(1\leqslant x^{2}+y^{2}\leqslant 4)</equation>的下侧，f(x)是连续函数，计算<equation>I=\iint\limits_{\Sigma}[xf(xy)+2x-y]\mathrm{d}y\mathrm{d}z+[yf(xy)+2y+x]\mathrm{d}z\mathrm{d}x+[zf(xy)+z]\mathrm{d}x\mathrm{d}y.</equation>
**答案: **<equation>I = \frac {1 4 \pi}{3}.</equation>
**解析: **解<equation>\varSigma</equation>如图（a）所示.由于曲面<equation>\varSigma</equation>取下侧，故<equation>\varSigma</equation>的法向量n与z轴正向成钝角.记<equation>F(x,y,z)=</equation><equation>\sqrt{x^{2}+y^{2}}-z</equation>，可得<equation>n=(F_{x}^{\prime},F_{y}^{\prime},F_{z}^{\prime})=\left(\frac{x}{\sqrt{x^{2}+y^{2}}},\frac{y}{\sqrt{x^{2}+y^{2}}},-1\right)=\left(\frac{x}{z},\frac{y}{z},-1\right).</equation>由此可知，<equation>\frac{\cos \alpha}{\cos \gamma}=-\frac{x}{z},\frac{\cos \beta}{\cos \gamma}=-\frac{y}{z}.</equation>(a)

(b)

记<equation>D</equation>为<equation>\Sigma</equation>在<equation>xOy</equation>面的投影区域. 利用两类曲面积分之间的联系，可得<equation>\begin{array}{l} I = \iint_ {\Sigma} \left\{\left[ x f (x y) + 2 x - y \right] \cdot \frac {\cos \alpha}{\cos \gamma} \cdot \cos \gamma + \left[ y f (x y) + 2 y + x \right] \cdot \frac {\cos \beta}{\cos \gamma} \cdot \cos \gamma + \left[ z f (x y) + z \right] \cos \gamma \right\} d S \\ \underline {{\cos \gamma \mathrm {d} S = \mathrm {d} x \mathrm {d} y}} \iint_ {\Sigma} \left\{\left[ x f (x y) + 2 x - y \right] \cdot \left(- \frac {x}{z}\right) + \left[ y f (x y) + 2 y + x \right] \cdot \left(- \frac {y}{z}\right) + \left[ z f (x y) + z \right] \right\} \mathrm {d} x \mathrm {d} y \\ = \iint_ {\Sigma} \left[ \left(- \frac {x ^ {2} + y ^ {2}}{z} + z\right) f (x y) - \frac {2 \left(x ^ {2} + y ^ {2}\right)}{z} + z \right] \mathrm {d} x \mathrm {d} y \underline {{= \frac {z = \sqrt {x ^ {2} + y ^ {2}}}{\Sigma}}} \iint_ {\Sigma} (z - 2 z) \mathrm {d} x \mathrm {d} y \\ = - \iint_ {\Sigma} z \mathrm {d} x \mathrm {d} y \underline {{\underline {{\Sigma}} \text {取 下 侧}}} \iint_ {D} \sqrt {x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y. \\ \end{array}</equation>如图（b）所示，<equation>D</equation>为一个圆环区域.<equation>D=\{(x,y)\mid 1\leqslant x^{2}+y^{2}\leqslant 4\}</equation>在极坐标系下计算<equation>\iint_{D}\sqrt{x^{2}+y^{2}}\mathrm{d}x\mathrm{d}y.</equation><equation>\iint_ {D} \sqrt {x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y \xlongequal {\text {极 坐 标}} \int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {1} ^ {2} r ^ {2} \mathrm {d} r = 2 \pi \cdot \frac {r ^ {3}}{3} \Big | _ {1} ^ {2} = \frac {1 4 \pi}{3}.</equation>因此，<equation>I=\frac{14\pi}{3}</equation>

---

**2019年第12题 | 填空题 | 4分**
12. 设<equation>\Sigma</equation>设为曲面<equation>x^{2}+y^{2}+4 z^{2}=4 ( z \geqslant0 )</equation>的上侧，则<equation>\iint\limits_{\Sigma} \sqrt{4-x^{2}-4 z^{2}} \mathrm{d} x \mathrm{d} y=</equation>___
**答案: **# 32 3.
**解析: **解 将曲面方程代入被积函数，可得<equation>\iint\limits_{\Sigma}\sqrt{4-x^{2}-4z^{2}}\mathrm{d}x\mathrm{d}y=\iint\limits_{\Sigma}\sqrt{y^{2}}\mathrm{d}x\mathrm{d}y=\iint\limits_{\Sigma}|y|\mathrm{d}x\mathrm{d}y.</equation>如图所示，令<equation>z = 0</equation>，可得曲面<equation>\Sigma</equation>在<equation>xOy</equation>面上的投影区域为<equation>D_{xy} = \{(x,y)|x^2 + y^2\leqslant 4\}</equation>.注意到<equation>D_{xy}</equation>关于<equation>x</equation>轴对称，记<equation>D</equation>为<equation>D_{xy}</equation>位于<equation>x</equation>轴上方的部分.<equation>D</equation>在极坐标系下的表示为<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2, 0 \leqslant \theta \leqslant \pi \right\}.</equation>又因为<equation>\sum</equation>取上侧，所以<equation>\begin{aligned} \iint_ {\Sigma} | y | \mathrm {d} x \mathrm {d} y &= \iint_ {D _ {x y}} | y | \mathrm {d} x \mathrm {d} y \xlongequal {\text {对称性}} 2 \iint_ {D} y \mathrm {d} x \mathrm {d} y \\ \xlongequal {\text {极 坐 标}} 2 \int_ {0} ^ {\pi} \mathrm {d} \theta \int_ {0} ^ {2} r \sin \theta \cdot r \mathrm {d} r \\ &= 2 \int_ {0} ^ {\pi} \sin \theta \mathrm {d} \theta \int_ {0} ^ {2} r ^ {2} \mathrm {d} r \\ &= 2 \cdot 2 \cdot \left. \frac {r ^ {3}}{3} \right| _ {0} ^ {2} = \frac {3 2}{3}. \end{aligned}</equation>

---

**2018年第17题 | 解答题 | 10分**
17. (本题满分10分）

设<equation>\Sigma</equation>是曲面<equation>x=\sqrt{1-3 y^{2}-3 z^{2}}</equation>的前侧，计算曲面积分<equation>I=\iint_{\Sigma} x \mathrm{d} y \mathrm{d} z+(y^{3}+2) \mathrm{d} z \mathrm{d} x+z^{3} \mathrm{d} x \mathrm{d} y.</equation>
**解析: **解如图所示，添加辅助平面<equation>\varSigma^{\prime}</equation>：<equation>x=0(3y^{2}+3z^{2}\leqslant 1)</equation>，取后侧，即法向量指向 x轴负向，则<equation>\varSigma</equation>与<equation>\varSigma^{\prime}</equation>围成一个半椭球体<equation>\varOmega</equation>，且法向量指向外侧.

根据高斯公式，

根据高斯公式，<equation>\iint_{\Sigma+\Sigma^{\prime}}x\mathrm{d}y\mathrm{d}z+(y^{3}+2)\mathrm{d}z\mathrm{d}x+z^{3}\mathrm{d}x\mathrm{d}y=\iiint_{\Omega}(1+3y^{2}+3z^{2})\mathrm{d}v.</equation>采用先重后单的积分次序计算<equation>\iiint_{\Omega}(1+3y^{2}+3z^{2})\mathrm{d}v.</equation>沿平行于 yOz面的方向作<equation>\varOmega</equation>的横截面，得<equation>D _ {x} = \left\{(y, z) \mid 3 y ^ {2} + 3 z ^ {2} \leqslant 1 - x ^ {2} \right\}.</equation><equation>D_{x}</equation>是半径为<equation>\sqrt{\frac{1-x^{2}}{3}}</equation>的圆盘.于是，<equation>\Omega = \left\{(x, y, z) \mid (y, z) \in D _ {x}, 0 \leqslant x \leqslant 1 \right\}.</equation><equation>\begin{aligned} \iiint_ {\Omega} \left(1 + 3 y ^ {2} + 3 z ^ {2}\right) \mathrm {d} v &= \int_ {0} ^ {1} \mathrm {d} x \iint_ {D _ {x}} \left(1 + 3 y ^ {2} + 3 z ^ {2}\right) \mathrm {d} y \mathrm {d} z \stackrel {\text {极 坐 标}} {=} \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {0} ^ {\sqrt {\frac {1 - x ^ {2}}{3}}} \left(1 + 3 r ^ {2}\right) \cdot r \mathrm {d} r \\ &= 2 \pi \int_ {0} ^ {1} \left(\frac {r ^ {2}}{2} + \frac {3 r ^ {4}}{4}\right) \Bigg | _ {0} ^ {\sqrt {\frac {1 - x ^ {2}}{3}}} \mathrm {d} x = 2 \pi \int_ {0} ^ {1} \left[ \frac {1 - x ^ {2}}{6} + \frac {3}{4} \cdot \frac {\left(1 - x ^ {2}\right) ^ {2}}{3 ^ {2}} \right] \mathrm {d} x \\ &= \frac {\pi}{6} \int_ {0} ^ {1} \left(x ^ {4} - 4 x ^ {2} + 3\right) \mathrm {d} x = \frac {\pi}{6} \times \left(\frac {1}{5} - \frac {4}{3} + 3\right) = \frac {1 4 \pi}{4 5}. \end{aligned}</equation>因为<equation>\Sigma^{\prime}</equation>垂直于<equation>zOx</equation>面与<equation>xOy</equation>面，且<equation>\Sigma^{\prime}</equation>的方程为<equation>x = 0(3y^{2} + 3z^{2}\leqslant 1)</equation>，所以<equation>\iint_ {\Sigma^ {\prime}} x \mathrm {d} y \mathrm {d} z + \left(y ^ {3} + 2\right) \mathrm {d} z \mathrm {d} x + z ^ {3} \mathrm {d} x \mathrm {d} y = \iint_ {\Sigma^ {\prime}} x \mathrm {d} y \mathrm {d} z \stackrel {x = 0} {=} \iint_ {\Sigma^ {\prime}} 0 \mathrm {d} y \mathrm {d} z = 0.</equation>因此，<equation>I=\frac{14\pi}{45}-0=\frac{14\pi}{45}.</equation>

---

**2016年第18题 | 解答题 | 10分**

设有界区域<equation>\Omega</equation>由平面<equation>2x+y+2z=2</equation>与三个坐标平面围成，<equation>\Sigma</equation>为<equation>\Omega</equation>整个表面的外侧，计算曲面积分 I =<equation>\iint\limits_{\Sigma} ( x^{2}+1 ) \mathrm{d} y \mathrm{d} z-2 y \mathrm{d} z \mathrm{d} x+3 z \mathrm{d} x \mathrm{d} y.</equation>
**答案: **# 1 2
**解析: **解 由题设知，<equation>\varOmega=\left\{(x,y,z)\mid0\leqslant z\leqslant\frac{2-2x-y}{2},0\leqslant y\leqslant 2-2x,0\leqslant x\leqslant 1\right\}</equation>，则<equation>\varOmega</equation>的体积为<equation>V_{\varOmega}=\frac{1}{3}\times \frac{1\times 2}{2}\times 1=\frac{1}{3}</equation>.再由高斯公式知，<equation>\begin{aligned} I &= \iint_ {\Sigma} \left(x ^ {2} + 1\right) \mathrm {d} y \mathrm {d} z - 2 y \mathrm {d} z \mathrm {d} x + 3 z \mathrm {d} x \mathrm {d} y = \iiint_ {\Omega} \left(2 x - 2 + 3\right) \mathrm {d} x \mathrm {d} y \mathrm {d} z \\ &= 2 \iiint_ {\Omega} x \mathrm {d} x \mathrm {d} y \mathrm {d} z + \iiint_ {\Omega} \mathrm {d} x \mathrm {d} y \mathrm {d} z = 2 \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {2 - 2 x} \mathrm {d} y \int_ {0} ^ {\frac {2 - 2 x - y}{2}} x \mathrm {d} z + V _ {\Omega} \\ &= \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {2 - 2 x} x (2 - 2 x - y) \mathrm {d} y + \frac {1}{3} = \int_ {0} ^ {1} x \left[ (2 - 2 x) ^ {2} - \frac {(2 - 2 x) ^ {2}}{2} \right] \mathrm {d} x + \frac {1}{3} \\ &= \int_ {0} ^ {1} 2 \left(x - 2 x ^ {2} + x ^ {3}\right) \mathrm {d} x + \frac {1}{3} = \left(x ^ {2} - \frac {4}{3} x ^ {3} + \frac {x ^ {4}}{2}\right) \Bigg | _ {0} ^ {1} + \frac {1}{3} = \frac {1}{2}. \end{aligned}</equation>

---

**2014年第18题 | 解答题 | 10分**
18. (本题满分10分）

设<equation>\Sigma</equation>为曲面<equation>z=x^{2}+y^{2}</equation>（<equation>z\leqslant1</equation>）的上侧，计算曲面积分<equation>I=\iint\limits_{\Sigma} ( x-1 )^{3} \mathrm{d} y \mathrm{d} z+( y-1 )^{3} \mathrm{d} z \mathrm{d} x+( z-1 ) \mathrm{d} x \mathrm{d} y.</equation>
**解析: **解记<equation>\varSigma_{1}</equation>为面<equation>\left\{ \begin{array}{l} z=1, \\ x^{2}+y^{2}\leqslant 1 \end{array} \right.</equation>的下侧，即其法向量与z轴负向同向，记<equation>\varOmega</equation>为<equation>\varSigma_{1}</equation>与<equation>\varSigma</equation>围成的区域，则<equation>\varOmega=\{(x,y,z)\mid(x,y)\in D_{z},0\leqslant z\leqslant 1\}</equation>，其中<equation>D_{z}=\{(x,y)\mid x^{2}+y^{2}\leqslant z\}</equation>.由高斯公式知，<equation>\iint_{\varSigma+\varSigma_{1}}(x-1)^{3}\mathrm{d}y\mathrm{d}z+(y-1)^{3}\mathrm{d}z\mathrm{d}x+(z-1)\mathrm{d}x\mathrm{d}y=-\iiint_{\varOmega}[3(x-1)^{2}+3(y-1)^{2}+1]\mathrm{d}x\mathrm{d}y\mathrm{d}z</equation><equation>= -\int_{0}^{1}\mathrm{d}z\iint_{D_{z}}[3(x-1)^{2}+3(y-1)^{2}+1]\mathrm{d}x\mathrm{d}y=-\int_{0}^{1}\mathrm{d}z\iint_{D_{z}}[3(x^{2}+y^{2})-6x-6y+7]\mathrm{d}x\mathrm{d}y</equation>对称性<equation>-\int_{0}^{1}\mathrm{d}z\iint_{D_{z}}[3(x^{2}+y^{2})+7]\mathrm{d}x\mathrm{d}y\frac{x=r\cos \theta}{y=r\sin \theta}-\int_{0}^{1}\mathrm{d}z\int_{0}^{2\pi}\mathrm{d}\theta \int_{0}^{\sqrt{z}}(3r^{2}+7)r\mathrm{d}r</equation><equation>= -\int_{0}^{1}\left(\frac{3}{2}\pi z^{2}+7\pi z\right)\mathrm{d}z=-4\pi.</equation>又在<equation>\Sigma_{1}</equation>上，<equation>z = 1</equation>，故<equation>\iint_{\Sigma_1} (x - 1)^3\mathrm{d}y\mathrm{d}z + (y - 1)^3\mathrm{d}z\mathrm{d}x + (z - 1)\mathrm{d}x\mathrm{d}y = 0 + 0 + 0 = 0</equation>，从而

---

**2009年第19题 | 解答题 | 10分**
19. (本题满分10分)<equation>I = \iint_ {\Sigma} \frac {x \mathrm {d} y \mathrm {d} z + y \mathrm {d} z \mathrm {d} x + z \mathrm {d} x \mathrm {d} y}{\left(x ^ {2} + y ^ {2} + z ^ {2}\right) ^ {\frac {3}{2}}}</equation>其中<equation>\Sigma</equation>是曲面<equation>2x^{2}+2y^{2}+z^{2}=4</equation>的外侧.
**解析: **<equation>P (x, y, z) = \frac {x}{\left(x ^ {2} + y ^ {2} + z ^ {2}\right) ^ {\frac {3}{2}}}, \quad Q (x, y, z) = \frac {y}{\left(x ^ {2} + y ^ {2} + z ^ {2}\right) ^ {\frac {3}{2}}}, \quad R (x, y, z) = \frac {z}{\left(x ^ {2} + y ^ {2} + z ^ {2}\right) ^ {\frac {3}{2}}}.</equation>当（x,y,z）<equation>\neq (0,0,0)</equation>时，有<equation>\frac {\partial P}{\partial x} = \frac {y ^ {2} + z ^ {2} - 2 x ^ {2}}{\left(x ^ {2} + y ^ {2} + z ^ {2}\right) ^ {\frac {5}{2}}}, \quad \frac {\partial Q}{\partial y} = \frac {x ^ {2} + z ^ {2} - 2 y ^ {2}}{\left(x ^ {2} + y ^ {2} + z ^ {2}\right) ^ {\frac {5}{2}}}, \quad \frac {\partial R}{\partial z} = \frac {x ^ {2} + y ^ {2} - 2 z ^ {2}}{\left(x ^ {2} + y ^ {2} + z ^ {2}\right) ^ {\frac {5}{2}}}.</equation>记<equation>\Sigma_{1}</equation>是曲面<equation>x^{2} + y^{2} + z^{2} = 1</equation>的内侧，则<equation>\Sigma_{1}</equation>包含在<equation>\Sigma</equation>内.记<equation>\Omega</equation>为<equation>\Sigma_{1}</equation>与<equation>\Sigma</equation>围成的闭区域，则<equation>\Sigma_{1} + \Sigma</equation>为<equation>\Omega</equation>的整个边界曲面的外侧，且<equation>P(x,y,z),Q(x,y,z),R(x,y,z)</equation>在<equation>\Omega</equation>上有一阶连续偏导数.由高斯公式知，<equation>\iint_ {\Sigma + \Sigma_ {1}} \frac {x \mathrm {d} y \mathrm {d} z + y \mathrm {d} z \mathrm {d} x + z \mathrm {d} x \mathrm {d} y}{\left(x ^ {2} + y ^ {2} + z ^ {2}\right) ^ {\frac {3}{2}}} = \iiint_ {\Omega} \left(\frac {\partial P}{\partial x} + \frac {\partial Q}{\partial y} + \frac {\partial R}{\partial z}\right) \mathrm {d} x \mathrm {d} y \mathrm {d} z = \iiint_ {\Omega} 0 \mathrm {d} x \mathrm {d} y \mathrm {d} z = 0.</equation>记<equation>\Omega_{1}</equation>为闭曲面<equation>\Sigma_{1}</equation>围成的闭区域，即<equation>\Omega_{1} = \{(x,y,z) | x^{2} + y^{2} + z^{2} \leqslant 1\}</equation>，则<equation>\begin{aligned} I &= \iint_ {\Sigma + \Sigma_ {1}} \frac {x \mathrm {d} y \mathrm {d} z + y \mathrm {d} z \mathrm {d} x + z \mathrm {d} x \mathrm {d} y}{\left(x ^ {2} + y ^ {2} + z ^ {2}\right) ^ {\frac {3}{2}}} - \iint_ {\Sigma_ {1}} \frac {x \mathrm {d} y \mathrm {d} z + y \mathrm {d} z \mathrm {d} x + z \mathrm {d} x \mathrm {d} y}{\left(x ^ {2} + y ^ {2} + z ^ {2}\right) ^ {\frac {3}{2}}} \\ &= 0 - \iint_ {\Sigma_ {1}} x \mathrm {d} y \mathrm {d} z + y \mathrm {d} z \mathrm {d} x + z \mathrm {d} x \mathrm {d} y \quad (\text {在} \Sigma_ {1} \text {上 有} x ^ {2} + y ^ {2} + z ^ {2} = 1) \\ \frac {\text {高斯公式}}{\Omega_ {1}} \iiint_ {\Omega_ {1}} (1 + 1 + 1) \mathrm {d} x \mathrm {d} y \mathrm {d} z &= 3 \iiint_ {\Omega_ {1}} \mathrm {d} x \mathrm {d} y \mathrm {d} z \\ &= 3 \cdot \frac {4}{3} \pi \cdot 1 ^ {3} = 4 \pi . \end{aligned}</equation>

---


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


#### 旋度的定义


**2018年第11题 | 填空题 | 4分**

11. 设<equation>F(x,y,z)= xy i-yz j+z x k</equation>, 则<equation>\mathbf{rot} F(1,1,0)=</equation>___

**答案:**i-k.

**解析:**根据旋度的定义，<equation>\operatorname {r o t} F (x, y, z) = \left| \begin{array}{c c c} i & j & k \\ \frac {\partial}{\partial x} & \frac {\partial}{\partial y} & \frac {\partial}{\partial z} \\ x y & - y z & z x \end{array} \right| = y i - z j - x k.</equation>代入<equation>(x,y,z) = (1,1,0)</equation>，可得<equation>\mathbf{rot} F(1,1,0) = i - k.</equation>

---

**2016年第10题 | 填空题 | 4分**

10. 向量场<equation>A(x,y,z) = (x+y+z)i+xyj+zk</equation>的旋度<equation>\mathbf{rot}A =</equation>___

**答案:**j + (y-1) k.

**解析:**令<equation>P= x+y+z, Q= x y, R=z</equation>，由旋度的定义知<equation>\mathbf{r o t} A=\left(\frac{\partial R}{\partial y}-\frac{\partial Q}{\partial z}\right) i+\left(\frac{\partial P}{\partial z}-\frac{\partial R}{\partial x}\right) j+\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right) k=j+(y-1) k.</equation>

---


#### 第一类曲线积分


**2018年第12题 | 填空题 | 4分**

12. 设 L为球面<equation>x^{2}+y^{2}+z^{2}=1</equation>与平面<equation>x+y+z=0</equation>的交线，则<equation>\oint_{L} xy\mathrm{d}s=</equation>___

**解析:**本题中，曲线<equation>L</equation>具有轮换对称性，故应利用轮换对称性来简化计算.

解 曲线 L如图所示.

由曲线<equation>L</equation>的方程可知，该曲线对变量<equation>x, y, z</equation>具有轮换对称性.于是，<equation>\oint_ {L} x y \mathrm {d} s = \oint_ {L} y z \mathrm {d} s = \oint_ {L} z x \mathrm {d} s = \frac {1}{3} \oint_ {L} (x y + y z + z x) \mathrm {d} s.</equation>又因为<equation>x y+y z+z x=\frac{1}{2} \left[ \left(x+y+z\right)^{2}-\left(x^{2}+y^{2}+z^{2}\right) \right]</equation>，所以<equation>\begin{aligned} \oint_ {L} x y \mathrm {d} s &= \frac {1}{3} \oint_ {L} \left(x y + y z + z x\right) \mathrm {d} s = \frac {1}{6} \oint_ {L} \left[ \left(x + y + z\right) ^ {2} - \left(x ^ {2} + y ^ {2} + z ^ {2}\right) \right] \mathrm {d} s \\ \frac {x + y + z = 0}{x ^ {2} + y ^ {2} + z ^ {2} = 1} \frac {1}{6} \oint_ {L} (0 - 1) \mathrm {d} s &= - \frac {1}{6} \oint_ {L} \mathrm {d} s. \end{aligned}</equation>由于 L为单位球面上的一个大圆，即以球心为圆心，且半径等于球半径的一个圆，故<equation>\oint_{L}\mathrm{d}s=L</equation>的周长<equation>= 2\pi.</equation>因此，原积分<equation>= -\frac{1}{6}\times 2\pi = -\frac{\pi}{3}.</equation>

---

**2009年第11题 | 填空题 | 4分**

11. 已知曲线<equation>L: y=x^{2}(0\leqslant x\leqslant\sqrt{2})</equation>，则<equation>\int_{L}x\mathrm{d}s=</equation>___

**答案:**# 13 6.

**解析:**由题设知，<equation>\begin{aligned} \int_ {L} x \mathrm {d} s &= \int_ {0} ^ {\sqrt {2}} x \sqrt {1 + \left[ y ^ {\prime} (x) \right] ^ {2}} \mathrm {d} x = \int_ {0} ^ {\sqrt {2}} x \sqrt {1 + 4 x ^ {2}} \mathrm {d} x \\ &= \frac {1}{8} \int_ {0} ^ {\sqrt {2}} \sqrt {1 + 4 x ^ {2}} \mathrm {d} \left(4 x ^ {2} + 1\right) = \frac {1}{8} \cdot \frac {2}{3} \left(1 + 4 x ^ {2}\right) ^ {\frac {3}{2}} \Bigg | _ {0} ^ {\sqrt {2}} = \frac {1 3}{6}. \end{aligned}</equation>

---


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


#### 重积分的概念与性质


**2010年第4题 | 选择题 | 4分 | 答案: D**

4.<equation>\lim_{n\rightarrow \infty}\sum_{i=1}^{n}\sum_{j=1}^{n}\frac{n}{(n+i)(n^{2}+j^{2})}=</equation>(    )

A.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{x}\frac{1}{(1+x)(1+y^{2})}\mathrm{d}y</equation>B.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{x}\frac{1}{(1+x)(1+y)}\mathrm{d}y</equation>C.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{1}\frac{1}{(1+x)(1+y)}\mathrm{d}y</equation>D.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{1}\frac{1}{(1+x)(1+y^{2})}\mathrm{d}y</equation>

答案: D

**解析:**解 （法一）考虑将原极限写成二重积分.

令<equation>\Delta \sigma_{ij} = \left[\frac{i - 1}{n},\frac{i}{n}\right]\times \left[\frac{j - 1}{n},\frac{j}{n}\right](i,j = 1,2,\dots ,n)</equation>，则<equation>\{\Delta \sigma_{ij}\}_{1\leqslant i,j\leqslant n}</equation>为<equation>D = [0,1]\times [0,1]</equation>上的一个划分，<equation>\Delta \sigma_{ij}</equation>的面积为<equation>\frac{1}{n^2}</equation>.取<equation>\Delta \sigma_{ij}</equation>上的一点<equation>\left(\frac{i}{n},\frac{j}{n}\right)</equation>.

由于<equation>\sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {n}{(n + i) \left(n ^ {2} + j ^ {2}\right)} = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {1}{\left(1 + \frac {i}{n}\right) \left(1 + \frac {j ^ {2}}{n ^ {2}}\right)} \cdot \frac {1}{n ^ {2}},</equation>故<equation>\begin{aligned} \text {原 极 限} &= \lim _ {n \rightarrow \infty} \left[ \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {1}{\left(1 + \frac {i}{n}\right)\left(1 + \frac {j ^ {2}}{n ^ {2}}\right)} \right] = \iint_ {D} \frac {1}{(1 + x) \left(1 + y ^ {2}\right)} \mathrm {d} \sigma \\ &= \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {1} \frac {1}{(1 + x) \left(1 + y ^ {2}\right)} \mathrm {d} y. \end{aligned}</equation>应选 D.

（法二）由于所求极限的表达式中 i，j无关，故可以考虑将原极限写成定积分的乘积.由于<equation>\begin{aligned} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {n}{(n + i) \left(n ^ {2} + j ^ {2}\right)} &= \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \left(\frac {1}{1 + \frac {i}{n}} \cdot \frac {1}{n}\right) \left(\frac {1}{1 + \frac {j ^ {2}}{n ^ {2}}} \cdot \frac {1}{n}\right) \\ \underline {{i , j \text {无关}}} \sum_ {i = 1} ^ {n} \left(\frac {1}{1 + \frac {i}{n}} \cdot \frac {1}{n}\right) \sum_ {j = 1} ^ {n} \left(\frac {1}{1 + \frac {j ^ {2}}{n ^ {2}}} \cdot \frac {1}{n}\right), \end{aligned}</equation>故<equation>\begin{aligned} &= \lim _ {n \rightarrow \infty} \sum_ {i = 1} ^ {n} \left(\frac {1}{1 + \frac {i}{n}} \cdot \frac {1}{n}\right) \cdot \lim _ {n \rightarrow \infty} \sum_ {j = 1} ^ {n} \left(\frac {1}{1 + \frac {j ^ {2}}{n ^ {2}}} \cdot \frac {1}{n}\right) = \left(\int_ {0} ^ {1} \frac {1}{1 + x} \mathrm {d} x\right)\left(\int_ {0} ^ {1} \frac {1}{1 + y ^ {2}} \mathrm {d} y\right) \\ &= \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {1} \frac {1}{(1 + x) \left(1 + y ^ {2}\right)} \mathrm {d} y. \end{aligned}</equation>应选 D.

---

**2009年第2题 | 选择题 | 4分 | 答案: A**

2. 如图，正方形<equation>\{(x,y)\mid|x|\leqslant1,|y|\leqslant1\}</equation>被其对角线划分为四个区域<equation>D_{k}(k=1,2,3,4),I_{k}=\iint_{D_{k}}y\cos x\mathrm{d}x\mathrm{d}y</equation>则<equation>\max_{1\leqslant k\leqslant4}\{I_{k}\}=</equation>（    ）

A.<equation>I_{1}</equation>B.<equation>I_{2}</equation>C.<equation>I_{3}</equation>D.<equation>I_{4}</equation>

答案: A

**解析:**解 令<equation>f ( x,y)=y \cos x</equation>，由于<equation>D_{4}</equation>关于x轴对称，且<equation>f ( x,y)=-f ( x,-y)</equation>，故<equation>I_{4}=0</equation>.同理得到<equation>I_{2}=0</equation>.又<equation>f ( x,y)</equation>在<equation>D_{1}</equation>内部恒大于0，在<equation>D_{3}</equation>内部恒小于0，故由重积分的保号性知，<equation>I_{1}>0, I_{3}<0.</equation>综上所述，<equation>\max_{1\leq k\leq 4}\left\{I_{k}\right\}=I_{1}</equation>应选A.

---


### 函数、极限、连续

#### 函数极限的计算


**2025年第11题 | 填空题 | 5分**

<equation>1 1. \lim _ {x \rightarrow 0 ^ {+}} \frac {x ^ {x} - 1}{\ln x \cdot \ln (1 - x)} = \underline {{}}</equation>

**解析:**解 由于<equation>x^{x}=\mathrm{e}^{x\ln x}</equation>，且当<equation>x\to0</equation>时，<equation>\mathrm{e}^{x}-1\sim x</equation>，故<equation>\lim_{x\to0^{+}}\frac{x^{x}-1}{\ln x\cdot\ln(1-x)}=\lim_{x\to0^{+}}\frac{\mathrm{e}^{x\ln x}-1}{\ln x\cdot\ln(1-x)} \frac{\mathrm{e}^{x\ln x}-1\sim x\ln x}{\ln(1-x)\sim-x} \lim_{x\to0^{+}}\frac{x\ln x}{\ln x\cdot(-x)}=-1.</equation>

---

**2021年第17题 | 解答题 | 10分**

17. (本题满分10分)

求极限 lim<equation>\left(\frac {1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t}{\mathrm {e} ^ {x} - 1} - \frac {1}{\sin x}\right)</equation>

**解析:**解 （法一）先整理原极限再计算.<equation>\begin{array}{l} \frac {\mathrm {e} ^ {x} - 1 \sim x}{\sin x \sim x} \lim _ {x \rightarrow 0} \frac {\int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t}{x} + \lim _ {x \rightarrow 0} \frac {\sin x - \mathrm {e} ^ {x} + 1}{x ^ {2}} \\ \frac {\text {洛必达}}{} \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x ^ {2}}}{1} + \lim _ {x \rightarrow 0} \frac {x - \frac {x ^ {3}}{6} - 1 - x - \frac {x ^ {2}}{2} + 1 + o \left(x ^ {2}\right)}{x ^ {2}} \\ = 1 + \lim _ {x \rightarrow 0} \frac {- \frac {x ^ {2}}{2} + o \left(x ^ {2}\right)}{x ^ {2}} = 1 - \frac {1}{2} = \frac {1}{2}. \\ \end{array}</equation>因此，原极限<equation>= \frac{1}{2}</equation>（法二）将原极限通分整理，化为<equation>\frac{0}{0}</equation>型未定式后再应用洛必达法则.<equation>\begin{aligned} \mathrm {原 极 限} &= \lim _ {x \rightarrow 0} \frac {\sin x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) - \mathrm {e} ^ {x} + 1}{\left(\mathrm {e} ^ {x} - 1\right) \sin x} \\ \frac {\mathrm {e} ^ {x} - 1 \sim x}{\sin x \sim x} \lim _ {x \rightarrow 0} \frac {\sin x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) - \mathrm {e} ^ {x} + 1}{x ^ {2}} \\ \underline {{\text {洛必达}}} \lim _ {x \rightarrow 0} \frac {\cos x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) + \sin x \cdot \mathrm {e} ^ {x ^ {2}} - \mathrm {e} ^ {x}}{2 x} \\ \underline {{\text {洛必达}}} \lim _ {x \rightarrow 0} \frac {- \sin x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) + \cos x \cdot \mathrm {e} ^ {x ^ {2}} + \cos x \cdot \mathrm {e} ^ {x ^ {2}} + 2 x \cdot \sin x \cdot \mathrm {e} ^ {x ^ {2}} - \mathrm {e} ^ {x}}{2} &= \frac {1}{2}. \\ \mathrm {因 此 , 原 极 限} &= \frac {1}{2}. \end{aligned}</equation>

---

**2020年第9题 | 填空题 | 4分**

9. lim

**答案:**```latex

-1.
```
**解析: **解 通分整理原极限.<equation>\lim _ {x \rightarrow 0} \left[ \frac {1}{\mathrm {e} ^ {x} - 1} - \frac {1}{\ln (1 + x)} \right] = \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - \mathrm {e} ^ {x} + 1}{\left(\mathrm {e} ^ {x} - 1\right) \ln (1 + x)} \frac {\mathrm {e} ^ {x} - 1 \sim x}{\ln (1 + x) \sim x} \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - \mathrm {e} ^ {x} + 1}{x ^ {2}}.</equation>下面用两种方法计算<equation>\lim_{x\to 0}\frac{\ln(1 + x) - \mathrm{e}^{x} + 1}{x^{2}}.</equation>（法一）利用泰勒公式.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - \mathrm {e} ^ {x} + 1}{x ^ {2}} &= \lim _ {x \rightarrow 0} \frac {x - \frac {x ^ {2}}{2} + o \left(x ^ {2}\right) - \left[ 1 + x + \frac {x ^ {2}}{2} + o \left(x ^ {2}\right)\right] + 1}{x ^ {2}} \\ &= \lim _ {x \rightarrow 0} \frac {- x ^ {2} + o \left(x ^ {2}\right)}{x ^ {2}} = - 1. \end{aligned}</equation>（法二）利用洛必达法则.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - \mathrm {e} ^ {x} + 1}{x ^ {2}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\frac {1}{1 + x} - \mathrm {e} ^ {x}}{2 x} &= \lim _ {x \rightarrow 0} \frac {1 - \mathrm {e} ^ {x} (1 + x)}{2 x (1 + x)} = \frac {1}{2} \lim _ {x \rightarrow 0} \frac {1 - \mathrm {e} ^ {x} - x \mathrm {e} ^ {x}}{x} \\ &= \frac {1}{2} \lim _ {x \rightarrow 0} \left(\frac {1 - \mathrm {e} ^ {x}}{x} - \mathrm {e} ^ {x}\right) \xlongequal {\text {洛必达}} \frac {1 - \mathrm {e} ^ {x} \sim - x}{2} \frac {1}{2} \times (- 1 - 1) = - 1. \end{aligned}</equation>

---

**2016年第9题 | 填空题 | 4分**
9. lim
**答案: **# 1 2.
**解析: **解 当<equation>x\to0</equation>时，<equation>1-\cos x^{2}\sim\frac{1}{2} x^{4},\ln(1+x\sin x)\sim x\sin x</equation>从而<equation>\lim _ {x \rightarrow 0} \frac {\int_ {0} ^ {x} t \ln (1 + t \sin t) \mathrm {d} t}{1 - \cos x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\int_ {0} ^ {x} t \ln (1 + t \sin t) \mathrm {d} t}{\frac {1}{2} x ^ {4}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {x \ln (1 + x \sin x)}{2 x ^ {3}} = \lim _ {x \rightarrow 0} \frac {x \cdot x \sin x}{2 x ^ {3}} = \frac {1}{2}.</equation>

---

**2015年第9题 | 填空题 | 4分**
（无内容）
**解析: **解 （法一）利用洛必达法则.<equation>\lim _ {x \rightarrow 0} \frac {\ln (\cos x)}{x ^ {2}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\frac {1}{\cos x} \cdot (- \sin x)}{2 x} = \lim _ {x \rightarrow 0} \left(- \frac {\sin x}{2 x}\right) = - \frac {1}{2}.</equation>（法二）利用等价无穷小替换.

当<equation>x\to 0</equation>时，<equation>\cos x - 1\to 0,\ln (1 + \cos x - 1)\sim \cos x - 1</equation>，于是<equation>\lim _ {x \rightarrow 0} \frac {\ln (\cos x)}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\ln (1 + \cos x - 1)}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\cos x - 1}{x ^ {2}} \frac {1 - \cos x - \frac {1}{2} x ^ {2}}{\overline {{=}}} \lim _ {x \rightarrow 0} \frac {- \frac {1}{2} x ^ {2}}{x ^ {2}} = - \frac {1}{2}.</equation>

---

**2014年第15题 | 解答题 | 10分**
15. (本题满分10分)

求极限<equation>\lim _ {x \rightarrow + \infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right)-t \right] \mathrm {d} t}{x ^ {2} \ln \left(1 + \frac {1}{x}\right)}.</equation>
**答案: **<equation>(1 5) \frac {1}{2}.</equation>
**解析: **解 由于<equation>\mathrm{e}^{x}</equation>在 x=0处的带拉格朗日余项的2阶泰勒公式为<equation>\mathrm{e}^{x}=1+x+\frac{x^{2}}{2}+\frac{\mathrm{e}^{\theta x}}{3!} x^{3}</equation>其中<equation>0 < \theta < 1</equation>，故当 x > 0时，<equation>\mathrm{e}^{x}>1+x+\frac{x^{2}}{2}.</equation>于是，<equation>\mathrm{e}^{\frac{1}{t}}-1 > \frac{1}{t}+\frac{1}{2t^{2}}(t > 0),</equation><equation>t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t > t ^ {2} \left(\frac {1}{t} + \frac {1}{2 t ^ {2}}\right) - t = \frac {1}{2}.</equation>从而<equation>\int_{1}^{+\infty}\left[ t^{2}\left(\mathrm{e}^{\frac{1}{t}} - 1\right) - t\right]\mathrm{d}t\to +\infty .</equation>另一方面，<equation>\lim _ {x \rightarrow + \infty} \left[ x ^ {2} \ln \left(1 + \frac {1}{x}\right)\right] \xlongequal {\ln \left(1 + \frac {1}{x}\right) \sim \frac {1}{x}} \lim _ {x \rightarrow + \infty} x = + \infty .</equation>因此，原极限为<equation>\frac{\infty}{\infty}</equation>型未定式.

当<equation>x\to +\infty</equation>时，<equation>\ln \left(1 + \frac{1}{x}\right)\sim \frac{1}{x}</equation>，故<equation>\begin{aligned} \lim _ {x \rightarrow + \infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t \right] \mathrm {d} t}{x ^ {2} \ln \left(1 + \frac {1}{x}\right)} \xlongequal {\ln \left(1 + \frac {1}{x}\right) \sim \frac {1}{x}} \lim _ {x \rightarrow + \infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t \right] \mathrm {d} t}{x} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow + \infty} \frac {x ^ {2} \left(\mathrm {e} ^ {\frac {1}{x}} - 1\right) - x}{1} &= \lim _ {x \rightarrow + \infty} \frac {\mathrm {e} ^ {\frac {1}{x}} - 1 - \frac {1}{x}}{\frac {1}{x ^ {2}}} \\ \xlongequal {u = \frac {1}{x}} \lim _ {u \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {u} - u - 1}{u ^ {2}} \xlongequal {\text {洛必达}} \lim _ {u \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {u} - 1}{2 u} \\ \xlongequal {\mathrm {e} ^ {u} - 1 \sim u} \lim _ {u \rightarrow 0 ^ {+}} \frac {u}{2 u} &= \frac {1}{2}. \end{aligned}</equation>因此，原极限<equation>= \frac{1}{2}.</equation>将原极限化简为<equation>\lim_{x\to +\infty}[x^{2}(\mathrm{e}^{\frac{1}{x}} -1) - x]</equation>后，也可以用泰勒公式来求该极限.

当<equation>x\to +\infty</equation>时，<equation>\frac{1}{x}\rightarrow 0^{+}</equation>.由<equation>\mathrm{e}^{u}</equation>在<equation>u = 0</equation>处的泰勒公式得，<equation>\mathrm {e} ^ {\frac {1}{x}} = 1 + \frac {1}{x} + \frac {1}{2 !} \cdot \frac {1}{x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right).</equation>从而，<equation>\begin{array}{l} \lim _ {x \rightarrow + \infty} \left[ x ^ {2} \left(\mathrm {e} ^ {\frac {1}{x}} - 1\right) - x \right] = \lim _ {x \rightarrow + \infty} \left\{x ^ {2} \left[ \frac {1}{x} + \frac {1}{2 !} \cdot \frac {1}{x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right)\right] - x \right\} \\ = \lim _ {x \rightarrow + \infty} \left[ \frac {1}{2} + x ^ {2} \cdot o \left(\frac {1}{x ^ {2}}\right)\right] = \frac {1}{2}. \\ \end{array}</equation>

---

**2011年第15题 | 解答题 | 10分**
15. (本题满分10分)
**解析: **解（法一）由于当<equation>x\to 0</equation>时，<equation>\frac{\ln(1+x)}{x}>0</equation>，故可以对函数<equation>\left[\frac{\ln(1+x)}{x}\right]^{\frac{1}{e^{x}-1}}</equation>取对数.又<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {1}{\mathrm {e} ^ {x} - 1} \ln \frac {\ln (1 + x)}{x} \xlongequal {\mathrm {e} ^ {x} - 1 \sim x} \lim _ {x \rightarrow 0} \frac {\ln \left[ 1 + \frac {\ln (1 + x) - x}{x} \right]}{x} \\ \xlongequal {\ln (1 + t) - t} \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - x}{x ^ {2}} \\ = \lim _ {x \rightarrow 0} \frac {x - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right) - x}{x ^ {2}} = - \frac {1}{2}, \\ \end{array}</equation>故<equation>\lim_{x\to 0}\left[\frac{\ln(1 + x)}{x}\right]^{\frac{1}{e^x - 1}} = \mathrm{e}^{-\frac{1}{2}}.</equation>(法二)<equation>\lim_{x\to 0}\left[\frac{\ln(1 + x)}{x}\right]^{\frac{1}{e^x - 1}} = \lim_{x\to 0}\left[1 + \frac{\ln(1 + x) - x}{x}\right]^{\frac{x}{\ln(1 + x) - x} \cdot \frac{\ln(1 + x) - x}{x} \cdot \frac{1}{e^x - 1}}.</equation>由于<equation>\lim _ {x \rightarrow 0} \left[ \frac {\ln (1 + x) - x}{x} \cdot \frac {1}{\mathrm {e} ^ {x} - 1} \right] = \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - x}{x ^ {2}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\frac {1}{1 + x} - 1}{2 x} = \lim _ {x \rightarrow 0} \frac {- 1}{2 (1 + x)} = - \frac {1}{2},</equation><equation>= \mathrm {e} ^ {- \frac {1}{2}}</equation>（法三）由于

注意该技巧！添加绝对值后不用分情况讨论.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {1}{\mathrm {e} ^ {x} - 1} \ln \frac {\ln (1 + x)}{x} &= \lim _ {x \rightarrow 0} \frac {\ln \left| \frac {\ln (1 + x)}{x} \right|}{\mathrm {e} ^ {x} - 1} = \lim _ {x \rightarrow 0} \frac {\ln | \ln (1 + x) | - \ln | x |}{x} \\ \underline {{\text {洛必达}}} \lim _ {x \rightarrow 0} \left[ \frac {\frac {1}{1 + x}}{\ln (1 + x)} - \frac {1}{x} \right] &= \lim _ {x \rightarrow 0} \frac {x - (1 + x) \ln (1 + x)}{x (1 + x) \ln (1 + x)} \\ \underline {{\frac {\ln (1 + x) - x}{\lim _ {x \rightarrow 0} (1 + x) = 1}}} \lim _ {x \rightarrow 0} \frac {x - (1 + x) \ln (1 + x)}{x ^ {2}} \\ \underline {{\text {洛必达}}} \lim _ {x \rightarrow 0} \frac {- \ln (1 + x)}{2 x} &= - \frac {1}{2}, \end{aligned}</equation>故<equation>\lim_{x\to 0}\left[\frac{\ln(1 + x)}{x}\right]^{\frac{1}{e^x - 1}} = \mathrm{e}^{-\frac{1}{2}}.</equation>

---

**2010年第1题 | 选择题 | 4分 | 答案: C**
1. 极限<equation>\lim_{x\to \infty}\left[\frac{x^{2}}{(x-a)(x+b)}\right]^{x}=(\quad)</equation>A. 1 B. e C.<equation>e^{a-b}</equation>D.<equation>e^{b-a}</equation>
答案: C
**解析: **解（法一）若 a,b 不同时为0，则<equation>( a-b) x+a b\neq0</equation>由<equation>\lim_{x\to\infty}\frac{(a-b)x+ab}{(x-a)(x+b)}=0</equation>以及重要极限<equation>\lim_{x\to\infty}\left(1+\frac{1}{x}\right)^{x}=e</equation>的复合形式可知，<equation>\begin{aligned} \lim _ {x \rightarrow \infty} \left[ \frac {x ^ {2}}{(x - a) (x + b)} \right] ^ {x} &= \lim _ {x \rightarrow \infty} \left[ 1 + \frac {(a - b) x + a b}{(x - a) (x + b)} \right] ^ {x} \\ &= \lim _ {x \rightarrow \infty} \left[ \left[ 1 + \frac {(a - b) x + a b}{(x - a) (x + b)} \right] ^ {\frac {(x - a) (x + b)}{(a - b) x + a b}} \right] ^ {\left[ \frac {(a - b) x + a b}{(x - a) (x + b)} \cdot x \right]} \\ &= \mathrm {e} ^ {\lim _ {x \rightarrow \infty} \frac {(a - b) x ^ {2} + a b x}{x ^ {2} - (a - b) x - a b}} = \mathrm {e} ^ {\lim _ {x \rightarrow \infty} \frac {(a - b) + \frac {a b}{x}}{- \frac {a - b}{x} - \frac {a b}{x ^ {2}}}} = \mathrm {e} ^ {a - b}. \end{aligned}</equation>若<equation>a = b = 0</equation>，则原式<equation>= \lim_{x\to \infty}1^{x} = 1 = \mathrm{e}^{a - b}</equation>.

综上所述，应选C.

（法二）当<equation>x\to \infty</equation>时（无论是<equation>+\infty</equation>还是<equation>-\infty</equation>），<equation>\frac{x^{2}}{(x-a)(x+b)}>0</equation>，故可以对<equation>\left[ \frac{x^{2}}{(x-a)(x+b)} \right]^{x}</equation>取对数.又<equation>\begin{aligned} \lim _ {x \rightarrow \infty} \ln \left[ \frac {x ^ {2}}{(x - a) (x + b)} \right] ^ {x} &= \lim _ {x \rightarrow \infty} x \ln \frac {x ^ {2}}{(x - a) (x + b)} = \lim _ {x \rightarrow \infty} x \ln \left[ 1 + \frac {(a - b) x + a b}{(x - a) (x + b)} \right] \\ &= \lim _ {x \rightarrow \infty} \left[ x \cdot \frac {(a - b) x + a b}{(x - a) (x + b)} \right] = \lim _ {x \rightarrow \infty} \frac {(a - b) x ^ {2} + a b x}{(x - a) (x + b)} = a - b, \end{aligned}</equation>故原式<equation>= \mathrm{e}^{a - b}.</equation>应选C.

---


#### 确定极限中的参数


**2024年第11题 | 填空题 | 5分**
<equation>. \mathrm {若} \lim _ {x \rightarrow 0} \frac {\left(1 + a x ^ {2}\right) ^ {\sin x} - 1}{x ^ {3}} = 6, \mathrm {则} a = \underline {{}}</equation>
**答案: **## a=6.
**解析: **<equation>\begin{aligned} 6 &= \lim _ {x \rightarrow 0} \frac {\left(1 + a x ^ {2}\right) ^ {\sin x} - 1}{x ^ {3}} = \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {\sin x \ln \left(1 + a x ^ {2}\right)} - 1}{x ^ {3}} = \lim _ {x \rightarrow 0} \frac {\sin x \ln \left(1 + a x ^ {2}\right)}{x ^ {3}} \\ &= \lim _ {x \rightarrow 0} \frac {x \cdot a x ^ {2}}{x ^ {3}} = a. \end{aligned}</equation>因此，<equation>a=6.</equation>

---

**2023年第11题 | 填空题 | 5分**
11. 当<equation>x \to0</equation>时，函数<equation>f(x)=ax+bx^{2}+\ln(1+x)</equation>与<equation>g(x)=\mathrm{e}^{x^{2}}-\cos x</equation>是等价无穷小，则 ab=___
**答案: **<equation>- 2.</equation>
**解析: **解分别写出<equation>f ( x )</equation>与<equation>g ( x )</equation>在<equation>x=0</equation>处的二阶泰勒公式.当<equation>x\to0</equation>时，<equation>f (x) = a x + b x ^ {2} + x - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right) = (a + 1) x + \left(b - \frac {1}{2}\right) x ^ {2} + o \left(x ^ {2}\right),</equation><equation>g (x) = 1 + x ^ {2} + o \left(x ^ {2}\right) - \left[ 1 - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right) \right] = \frac {3}{2} x ^ {2} + o \left(x ^ {2}\right).</equation>由于<equation>f(x)</equation>与<equation>g(x)</equation>是<equation>x\to 0</equation>时的等价无穷小，故<equation>1 = \lim _ {x \rightarrow 0} \frac {f (x)}{g (x)} = \lim _ {x \rightarrow 0} \frac {(a + 1) x + \left(b - \frac {1}{2}\right) x ^ {2} + o \left(x ^ {2}\right)}{\frac {3}{2} x ^ {2} + o \left(x ^ {2}\right)}.</equation>由（1）式成立可得<equation>a+1=0,b-\frac{1}{2}=\frac{3}{2}.</equation>解得<equation>a=-1,b=2.</equation>因此，<equation>ab=-2.</equation>

---

**2019年第1题 | 选择题 | 4分 | 答案: C**
1. 当 x→0时，若 x-tanx与<equation>x^{k}</equation>是同阶无穷小，则 k=（    ）

A.1 B.2 C.3 D.4
答案: C
**解析: **解 首先，由于当<equation>x\to0</equation>时，<equation>x-\tan x\to0</equation>，而<equation>\lim_{x\to0}\frac{x-\tan x}{x^{k}}</equation>为非零常数，故 k > 0.下面用两种方法讨论<equation>\lim_{x\to0}\frac{x-\tan x}{x^{k}}.</equation>（法一）由于<equation>\tan x=x+\frac{x^{3}}{3}+o\left(x^{3}\right)</equation>，故<equation>\lim _ {x \rightarrow 0} \frac {x - \tan x}{x ^ {k}} = \lim _ {x \rightarrow 0} \frac {- \frac {x ^ {3}}{3} + o \left(x ^ {3}\right)}{x ^ {k}}.</equation>当 k > 3时，该极限为<equation>\infty</equation>；当0 < k < 3时，该极限为0；当 k=3时，该极限为<equation>-\frac{1}{3}.</equation>于是，<equation>x-\tan x</equation>与<equation>x^{3}</equation>是同阶无穷小，k=3.

因此，应选C.

（法二）利用洛必达法则讨论<equation>\lim_{x\to 0}\frac{x - \tan x}{x^k}</equation>.<equation>\lim _ {x \rightarrow 0} \frac {x - \tan x}{x ^ {k}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - \sec^ {2} x}{k x ^ {k - 1}} = \lim _ {x \rightarrow 0} \frac {- \tan^ {2} x}{k x ^ {k - 1}} \xlongequal {\tan x \sim x} \lim _ {x \rightarrow 0} \frac {- x ^ {2}}{k x ^ {k - 1}}.</equation>当 k > 3时，该极限为<equation>\infty</equation>；当0 < k < 3时，该极限为0；当 k=3时，该极限为<equation>-\frac{1}{3}.</equation>于是，<equation>x-\tan x</equation>与<equation>x^{3}</equation>是同阶无穷小， k=3.

因此，应选C.

---

**2018年第9题 | 填空题 | 4分**
9. 若<equation>\lim_{x\rightarrow 0}\left(\frac{1-\tan x}{1+\tan x}\right)^{\frac{1}{\sin k x}}=\mathrm{e}</equation>，则 k= ___
**解析: **解（法一）对原极限进行恒等变形，再凑重要极限.<equation>\lim _ {x \rightarrow 0} \left(\frac {1 - \tan x}{1 + \tan x}\right) ^ {\frac {1}{\sin k x}} = \lim _ {x \rightarrow 0} \left(1 - \frac {2 \tan x}{1 + \tan x}\right) ^ {\frac {1}{\sin k x}} = \lim _ {x \rightarrow 0} \left(1 - \frac {2 \tan x}{1 + \tan x}\right) ^ {\frac {1 + \tan x}{- 2 \tan x} \cdot \frac {- 2 \tan x}{1 + \tan x} \cdot \frac {1}{\sin k x}}.</equation>因为<equation>\lim _ {x \rightarrow 0} \left(\frac {- 2 \tan x}{1 + \tan x} \cdot \frac {1}{\sin k x}\right) = \lim _ {x \rightarrow 0} \frac {- 2 \tan x}{\sin k x} \frac {\tan x \sim x}{\sin k x \sim k x} \lim _ {x \rightarrow 0} \frac {- 2 x}{k x} = - \frac {2}{k},</equation>所以原极限<equation>= \mathrm{e}^{-\frac{2}{k}} = \mathrm{e}.</equation>因此，<equation>-\frac{2}{k} = 1,k = -2.</equation>（法二）取对数，再求极限.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \left(\frac {1 - \tan x}{1 + \tan x}\right) ^ {\frac {1}{\sin k x}} &= \lim _ {x \rightarrow 0} \mathrm {e} ^ {\frac {1}{\sin k x} \cdot \ln \left(\frac {1 - \tan x}{1 + \tan x}\right)} = \mathrm {e} ^ {\lim _ {x \rightarrow 0} \frac {1}{\sin k x} \cdot \ln \left(1 - \frac {2 \tan x}{1 + \tan x}\right)} \\ \frac {\ln \left(1 - \frac {2 \tan x}{1 + \tan x}\right) \sim \frac {- 2 \tan x}{1 + \tan x}}{\frac {\tan x \sim x}{\sin k x \sim k x}} \mathrm {e} ^ {\lim _ {x \rightarrow 0} \frac {- 2 x}{k x}} &= \mathrm {e} ^ {- \frac {2}{k}}. \end{aligned}</equation>由于原极限<equation>= \mathrm{e}</equation>，故<equation>-\frac{2}{k} = 1</equation>，即<equation>k = -2.</equation>

---

**2015年第15题 | 解答题 | 10分**
15. (本题满分10分)

设函数<equation>f(x)=x+a\ln(1+x)+bx\sin x,g(x)=kx^{3}.</equation>若 f(x)与 g(x)在<equation>x\rightarrow0</equation>时是等价无穷小，求 a,b,k的值.
**解析: **由于 g(x）中 x的次数为3，故可考虑写出 f(x)在 x=0处的3阶泰勒公式.

由<equation>\ln (1 + x) = x - \frac {x ^ {2}}{2} + \frac {x ^ {3}}{3} + o \left(x ^ {3}\right), \quad \sin x = x - \frac {x ^ {3}}{3 !} + o \left(x ^ {3}\right),</equation>可得<equation>f (x) = x + a x - \frac {a x ^ {2}}{2} + \frac {a x ^ {3}}{3} + b x ^ {2} + o \left(x ^ {3}\right) = (a + 1) x + \left(b - \frac {a}{2}\right) x ^ {2} + \frac {a}{3} x ^ {3} + o \left(x ^ {3}\right).</equation>记<equation>I=\lim_{x\to 0}\frac{f(x)}{g(x)}=\lim_{x\to 0}\frac{(a+1)x+\left(b-\frac{a}{2}\right)x^{2}+\frac{a}{3}x^{3}+o\left(x^{3}\right)}{kx^{3}}.</equation>由等价无穷小量的定义知<equation>I=1.</equation>首先，<equation>k\neq 0</equation>当 k≠0时，若 I存在，则必有<equation>\left\{\begin{array}{l l}a+1=0,\\ b-\frac{a}{2}=0,\end{array}\right.</equation>否则<equation>I=\infty.</equation>解得 a=-1，b=-<equation>\frac{1}{2}.</equation>又因为 I=1，所以<equation>\frac{a}{3}=k,k=-\frac{1}{3}.</equation>综上所述，<equation>a = -1</equation>，<equation>b = -\frac{1}{2}</equation>，<equation>k = -\frac{1}{3}</equation>

---

**2013年第1题 | 选择题 | 4分 | 答案: D**
1. 已知极限<equation>\lim_{x\rightarrow 0}\frac{x-\arctan x}{x^{k}}=c</equation>，其中 k,c为常数，且<equation>c\neq 0</equation>，则（    )

A. k=2, c=-<equation>\frac{1}{2}</equation>B. k=2, c=<equation>\frac{1}{2}</equation>C. k=3, c=-<equation>\frac{1}{3}</equation>D. k=3, c=<equation>\frac{1}{3}</equation>
答案: D
**解析: **解（法一）当<equation>x\to0</equation>时，<equation>\arctan x=x-\frac{x^{3}}{3}+o\left(x^{3}\right)</equation>，于是<equation>0 \neq c = \lim _ {x \rightarrow 0} \frac {x - \arctan x}{x ^ {k}} = \lim _ {x \rightarrow 0} \frac {\frac {x ^ {3}}{3} + o \left(x ^ {3}\right)}{x ^ {k}}.</equation>当<equation>k > 3</equation>时，<equation>\lim_{x\to 0}\frac{\frac{x^3}{3} + o(x^3)}{x^k} = \lim_{x\to 0}\frac{\frac{1}{3} + \frac{o(x^3)}{x^3}}{x^{k - 3}} = \lim_{x\to 0}\frac{\frac{1}{3}}{x^{k - 3}} = \infty .</equation>当 k < 3时，<equation>\lim_{x\to 0}\frac{\frac{x^{3}}{3}+o\left(x^{3}\right)}{x^{k}}=\lim_{x\to 0}\left[\frac{x^{3-k}}{3}+\frac{o\left(x^{3}\right)}{x^{3}}\cdot x^{3-k}\right]=\lim_{x\to 0}\frac{x^{3-k}}{3}=0.</equation>因此，k=3，此时<equation>c=\frac{1}{3}</equation>应选D.

（法二）由于<equation>c\neq 0</equation>且<equation>\lim_{x\to 0} \left(x-\arctan x\right)=0</equation>，故<equation>\lim_{x\to 0} x^{k}=0</equation>，从而 k>0，于是题设中极限为<equation>\frac{0}{0}</equation>型.根据洛必达法则，<equation>\lim _ {x \rightarrow 0} \frac {x - \arctan x}{x ^ {k}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - \frac {1}{1 + x ^ {2}}}{k x ^ {k - 1}} = \lim _ {x \rightarrow 0} \left(\frac {1}{1 + x ^ {2}} \cdot \frac {x ^ {2}}{k x ^ {k - 1}}\right) = \lim _ {x \rightarrow 0} \frac {1}{k x ^ {k - 3}} = c.</equation>又<equation>c\neq 0</equation>，故<equation>k=3</equation>，从而<equation>c=\frac{1}{3}</equation>应选D.

---

**2009年第1题 | 选择题 | 4分 | 答案: A**
1. 当<equation>x\to0</equation>时，<equation>f(x)=x-\sin ax</equation>与<equation>g(x)=x^{2}\ln(1-bx)</equation>是等价无穷小量，则（    )

A. a=1,b=-<equation>\frac{1}{6}</equation>B. a=1,b=<equation>\frac{1}{6}</equation>C. a=-1,b=-<equation>\frac{1}{6}</equation>D. a=-1,b=<equation>\frac{1}{6}</equation>
答案: A
**解析: **由于<equation>x\to0</equation>时，<equation>f(x)</equation>与<equation>g(x)</equation>是等价无穷小量，故<equation>\begin{aligned} 1 &= \lim _ {x \rightarrow 0} \frac {f (x)}{g (x)} = \lim _ {x \rightarrow 0} \frac {x - \sin a x}{x ^ {2} \ln (1 - b x)} \xlongequal {\ln (1 - b x) \sim (- b x)} \lim _ {x \rightarrow 0} \frac {x - \sin a x}{- b x ^ {3}} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - a \cos a x}{- 3 b x ^ {2}} &= I _ {1}. \end{aligned}</equation>由于<equation>\lim_{x\to 0}(-3bx^2) = 0</equation>，故若<equation>I_{1}</equation>存在，则<equation>\lim_{x\to 0}(1 - a\cos ax) = 0</equation>，从而<equation>a = 1.</equation>代人 a=1，得<equation>I _ {1} = \lim _ {x \rightarrow 0} \frac {1 - \cos x}{- 3 b x ^ {2}} \xlongequal {1 - \cos x \sim \frac {x ^ {2}}{2}} \lim _ {x \rightarrow 0} \frac {\frac {x ^ {2}}{2}}{- 3 b x ^ {2}} = - \frac {1}{6 b}.</equation>当<equation>b = -\frac{1}{6}</equation>时，<equation>I_{1}</equation>存在且等于1.

因此，当<equation>a = 1,b = -\frac{1}{6}</equation>时，<equation>\lim_{x\to 0}\frac{f(x)}{g(x)} = 1,f(x)</equation>与<equation>g(x)</equation>是<equation>x\to 0</equation>时的等价无穷小量.应选A.

---


#### 数列敛散性的判定


**2022年第3题 | 选择题 | 5分 | 答案: D**

3. 已知数列<equation>\{x_{n}\}</equation>满足<equation>-\frac{\pi}{2}\leqslant x_{n}\leqslant \frac{\pi}{2}</equation>，则（    )

A. 若<equation>\lim_{n\to\infty}\cos(\sin x_{n})</equation>存在，则<equation>\lim_{n\to\infty}x_{n}</equation>存在

B. 若<equation>\lim_{n\to\infty}\sin(\cos x_{n})</equation>存在，则<equation>\lim_{n\to\infty}x_{n}</equation>存在

C. 若<equation>\lim_{n\to\infty}\cos(\sin x_{n})</equation>存在，则<equation>\lim_{n\to\infty}\sin x_{n}</equation>存在，但<equation>\lim_{n\to\infty}x_{n}</equation>不一定存在

D. 若<equation>\lim_{n\to\infty}\sin(\cos x_{n})</equation>存在，则<equation>\lim_{n\to\infty}\cos x_{n}</equation>存在，但<equation>\lim_{n\to\infty}x_{n}</equation>不一定存在

答案: D

**解析:**解 若<equation>\lim_{n\rightarrow \infty}\sin(\cos x_{n})</equation>存在，则将其记为 a.由于<equation>\sin x</equation>在<equation>\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>上存在反函数<equation>\arcsin x</equation>，故<equation>\lim_{n\rightarrow \infty}\cos x_{n}=\lim_{n\rightarrow \infty}\arcsin(\sin(\cos x_{n}))=\arcsin(\lim_{n\rightarrow \infty}\sin(\cos x_{n}))=\arcsin a.</equation>但是<equation>\lim_{n\rightarrow \infty}\cos x_{n}</equation>存在并不能保证<equation>\lim_{n\rightarrow \infty}x_{n}</equation>存在.例如取<equation>x_{n}=(-1)^{n}\frac{\pi}{2}</equation>，则<equation>\lim_{n\rightarrow \infty}\cos x_{n}=0</equation>，但<equation>\lim_{n\rightarrow \infty}x_{n}</equation>不存在.选项B错误，选项D正确.应选D.

由于<equation>\cos x</equation>在<equation>\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]</equation>上并不单调，故由<equation>\lim_{n\to \infty}\cos (\sin x_n)</equation>存在并不能保证<equation>\lim_{n\to \infty}\sin x_n</equation>存在。同样取<equation>x_{n} = (-1)^{n}\frac{\pi}{2}</equation>，则<equation>\lim_{n\to \infty}\cos (\sin x_n) = \cos 1</equation>，但<equation>\lim_{n\to \infty}\sin x_n</equation>和<equation>\lim_{n\to \infty}x_n</equation>均不存在。选项A、C不正确。

---

**2019年第18题 | 解答题 | 10分**

18. (本题满分10分)

设<equation>a_{n}=\int_{0}^{1} x^{n}\sqrt{1-x^{2}}\mathrm{d}x(n=0,1,2,\dots).</equation>I. 证明数列<equation>\{a_{n}\}</equation>单调递减，且<equation>a_{n}=\frac{n-1}{n+2} a_{n-2}(n=2,3,\cdots)</equation>；

II. 求<equation>\lim_{n\to\infty}\frac{a_{n}}{a_{n-1}}.</equation>

**答案:**（I）证明略；（Ⅱ）<equation>\lim_{n\to \infty}\frac{a_{n}}{a}=1.</equation>

**解析:**解（I）考虑<equation>a_{n+1}-a_{n}</equation>由于在（0，1）内，<equation>x^{n+1}-x^{n}<0,\sqrt{1-x^{2}}>0</equation>故由定积分的保号性可知，<equation>a _ {n + 1} - a _ {n} = \int_ {0} ^ {1} \left(x ^ {n + 1} - x ^ {n}\right) \sqrt {1 - x ^ {2}} \mathrm {d} x < 0.</equation>因此，<equation>\{a_{n}\}</equation>单调递减.

下面用两种方法证明<equation>a_{n} = \frac{n - 1}{n + 2} a_{n - 2}(n = 2,3,\dots)</equation>.

（法一）先三角换元，再分部分分.

令<equation>x=\sin t</equation>，则<equation>\mathrm{d}x=\cos t\mathrm{d}t.</equation><equation>\begin{aligned} a _ {n} &= \int_ {0} ^ {1} x ^ {n} \sqrt {1 - x ^ {2}} \mathrm {d} x \xlongequal {x = \sin t} \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \cos t \cdot \cos t \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \cos^ {2} t \mathrm {d} t \\ &= \int_ {0} ^ {\frac {\pi}{2}} \left(\sin^ {n} t - \sin^ {n + 2} t\right) \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t + \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n + 1} t \mathrm {d} (\cos t) \\ &= \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t + \sin^ {n + 1} t \cos t \left| _ {0} ^ {\frac {\pi}{2}} - \int_ {0} ^ {\frac {\pi}{2}} \cos t \cdot (n + 1) \sin^ {n} t \cdot \cos t \mathrm {d} t \right. \\ &= \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t - (n + 1) \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \cos^ {2} t \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t - (n + 1) a _ {n}. \end{aligned}</equation>由上可得，<equation>(n + 2)a_{n} = \int_{0}^{\frac{\pi}{2}}\sin^{n}t\mathrm{d}t.</equation>另一方面，<equation>\begin{aligned} \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t &= - \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n - 1} t \mathrm {d} (\cos t) = - \left[ \sin^ {n - 1} t \cos t \left| _ {0} ^ {\frac {\pi}{2}} - \int_ {0} ^ {\frac {\pi}{2}} \cos t \cdot (n - 1) \sin^ {n - 2} t \cdot \cos t \mathrm {d} t \right] \right. \\ &= (n - 1) \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n - 2} t \cos^ {2} t \mathrm {d} t = (n - 1) a _ {n - 2}. \end{aligned}</equation>因此，<equation>(n + 2)a_{n} = (n - 1)a_{n - 2}</equation>，即<equation>a_{n} = \frac{n - 1}{n + 2} a_{n - 2}(n = 2,3,\dots)</equation>.

（法二）直接分部积分.注意到<equation>[ ( 1 - x^{2} )^{\frac{3}{2}} ]^{\prime} = - 3 x \sqrt{1 - x^{2}}</equation>，故<equation>\begin{array}{l} a _ {n} = \int_ {0} ^ {1} x ^ {n} \sqrt {1 - x ^ {2}} \mathrm {d} x = - \frac {1}{3} \int_ {0} ^ {1} x ^ {n - 1} \mathrm {d} \left(1 - x ^ {2}\right) ^ {\frac {3}{2}} \\ = - \frac {1}{3} \left\{\left[ x ^ {n - 1} \left(1 - x ^ {2}\right) ^ {\frac {3}{2}} \right] \Bigg | _ {0} ^ {1} - \int_ {0} ^ {1} \left(1 - x ^ {2}\right) ^ {\frac {3}{2}} \cdot (n - 1) x ^ {n - 2} \mathrm {d} x \right\} \\ = \frac {n - 1}{3} \int_ {0} ^ {1} \left(1 - x ^ {2}\right) \sqrt {1 - x ^ {2}} x ^ {n - 2} \mathrm {d} x = \frac {n - 1}{3} \int_ {0} ^ {1} \left(x ^ {n - 2} - x ^ {n}\right) \sqrt {1 - x ^ {2}} \mathrm {d} x \\ = \frac {n - 1}{3} \left(\int_ {0} ^ {1} x ^ {n - 2} \sqrt {1 - x ^ {2}} \mathrm {d} x - \int_ {0} ^ {1} x ^ {n} \sqrt {1 - x ^ {2}} \mathrm {d} x\right) \\ = \frac {n - 1}{3} \left(a _ {n - 2} - a _ {n}\right). \\ \end{array}</equation>因此，<equation>a_{n} = \frac{n - 1}{n + 2} a_{n - 2}(n = 2,3,\dots)</equation>（Ⅱ）由第（I）问可知<equation>\{a_{n}\}</equation>单调递减，故<equation>a_{n} < a_{n-1} < a_{n-2}</equation>又由<equation>a_{n}</equation>的表达式可知<equation>a_{n} > 0 (n= 0,1,\dots)</equation>，故<equation>\frac {n - 1}{n + 2} = \frac {a _ {n}}{a _ {n - 2}} < \frac {a _ {n}}{a _ {n - 1}} < \frac {a _ {n}}{a _ {n}} = 1.</equation>对（1）式中各项同时取极限，令<equation>n\to \infty</equation>，可得<equation>1 = \lim _ {n \rightarrow \infty} \frac {n - 1}{n + 2} \leqslant \lim _ {n \rightarrow \infty} \frac {a _ {n}}{a _ {n - 1}} \leqslant 1.</equation>由夹逼准则可知，<equation>\lim_{n\to \infty}\frac{a_n}{a_{n-1}} = 1.</equation>

---

**2018年第19题 | 解答题 | 10分**

19. (本题满分10分）

设数列<equation>\{x_{n}\}</equation>满足：<equation>x_{1}>0,x_{n}\mathrm{e}^{x_{n+1}}=\mathrm{e}^{x_{n}}-1(n=1,2,\cdots).</equation>证明数列<equation>\{x_{n}\}</equation>收敛，并求<equation>\lim_{n\rightarrow \infty}x_{n}.</equation>

**答案:**证明略，<equation>\lim x_{n}=0.</equation>n->infty

**解析:**解 由<equation>x_{n}\mathrm{e}^{x_{n + 1}} = \mathrm{e}^{x_{n}} - 1(n = 1,2,\dots)</equation>可得，<equation>x _ {n + 1} = \ln \left(\frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n}}\right).</equation>先用数学归纳法证明对所有的正整数<equation>n</equation>，都有<equation>x_{n} > 0</equation>首先，<equation>x_{1} > 0.</equation>假设当<equation>n = k</equation>时，<equation>x_{k} > 0.</equation>注意到当<equation>x > 0</equation>时，<equation>\mathrm{e}^{x} - 1 > x</equation>，从而<equation>\frac{\mathrm{e}^{x} - 1}{x} > 1.</equation>于是，<equation>x _ {k + 1} = \ln \left(\frac {\mathrm {e} ^ {x _ {k}} - 1}{x _ {k}}\right) > \ln 1 = 0.</equation>由数学归纳法可知，对所有的正整数<equation>n</equation>，都有<equation>x_{n} > 0</equation>因此，数列<equation>\{x_{n}\}</equation>有下界.

下面用两种方法证明数列<equation>\{x_{n}\}</equation>单调减少，即<equation>x_{n + 1} < x_n(n = 1,2,\dots)</equation>.

（法一）由<equation>x_{n}\mathrm{e}^{x_{n + 1}} = \mathrm{e}^{x_{n}} - 1</equation>可知，<equation>\mathrm {e} ^ {x _ {n + 1}} = \frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n}} = \frac {\mathrm {e} ^ {x _ {n}} - \mathrm {e} ^ {0}}{x _ {n} - 0} \frac {\text {拉 格 朗 日}}{\text {中 值 定 理}} \mathrm {e} ^ {\xi_ {n}},</equation>其中<equation>\xi_{n}\in (0,x_{n})</equation>由于<equation>\mathrm{e}^x</equation>单调增加，故由<equation>\mathrm{e}^{x_{n+1}} = \mathrm{e}^{\xi_n} < \mathrm{e}^{x_n}</equation>可得<equation>x_{n+1} < x_n</equation>，即数列<equation>\{x_n\}</equation>单调减少.

（法二）<equation>x _ {n + 1} - x _ {n} = \ln \left(\frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n}}\right) - x _ {n} = \ln \left(\frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n} \mathrm {e} ^ {x _ {n}}}\right).</equation>记<equation>f(x) = \mathrm{e}^{x} - 1 - x\mathrm{e}^{x}</equation>，则<equation>f^{\prime}(x) = \mathrm{e}^{x} - \mathrm{e}^{x} - x\mathrm{e}^{x} = -x\mathrm{e}^{x}</equation>.

当<equation>x > 0</equation>时，<equation>f^{\prime}(x) < 0,f(x)</equation>在<equation>[0, + \infty)</equation>上单调减少，于是，<equation>f(x) < f(0) = 0.</equation>从而，当<equation>x > 0</equation>时，<equation>\frac {\mathrm {e} ^ {x} - 1}{x \mathrm {e} ^ {x}} - 1 = \frac {\mathrm {e} ^ {x} - 1 - x \mathrm {e} ^ {x}}{x \mathrm {e} ^ {x}} < 0,</equation>即<equation>\frac{\mathrm{e}^x - 1}{x\mathrm{e}^x} < 1.</equation>又因为对所有的正整数<equation>n</equation>，都有<equation>x_{n} > 0</equation>，所以<equation>\ln \left(\frac{\mathrm{e}^{x_n} - 1}{x_n\mathrm{e}^{x_n}}\right) < \ln 1 = 0</equation>，即<equation>x_{n + 1} - x_n < 0.</equation>因此，数列<equation>\{x_{n}\}</equation>单调减少.

由单调有界准则可知，数列<equation>\{x_{n}\}</equation>收敛.由于对所有的正整数<equation>n</equation>，都有<equation>x_{n} > 0</equation>，故<equation>\lim_{n\to \infty}x_n = a\geqslant 0.</equation>对<equation>x_{n}\mathrm{e}^{x_{n + 1}} = \mathrm{e}^{x_{n}} - 1</equation>两端同时令<equation>n\to \infty</equation>，可得<equation>a\mathrm{e}^{a} = \mathrm{e}^{a} - 1.</equation>由前面的结果可知，<equation>x=0</equation>是<equation>f(x)=\mathrm{e}^{x}-1-x\mathrm{e}^{x}</equation>在<equation>[0,+\infty)</equation>上的唯一零点.因此，<equation>a=0</equation>即<equation>\lim_{n\to \infty}x_{n}=0.</equation>

---

**2011年第18题 | 解答题 | 10分**

18. (本题满分10分)

I. 证明：对任意的正整数 n, 都有<equation>\frac{1}{n+1}<\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}</equation>成立；

II. 设<equation>a_{n}=1+\frac{1}{2}+\cdots+\frac{1}{n}-\ln n</equation>（<equation>n=1,2,\cdots</equation>），证明数列<equation>\left\{a_{n}\right\}</equation>收敛.

**解析:**证（I）（法一）考虑函数<equation>f ( x )=\ln x</equation>，则<equation>f^{\prime}(x)=\frac{1}{x}</equation>由拉格朗日中值定理，对任意的正整数n，都存在<equation>\xi_{n}\in(n,n+1)</equation>，使得<equation>\ln \left(1 + \frac {1}{n}\right) = f (n + 1) - f (n) = f ^ {\prime} \left(\xi_ {n}\right) = \frac {1}{\xi_ {n}}.</equation>又因为<equation>\xi_{n}\in (n,n + 1)</equation>，所以<equation>\frac{1}{n + 1} < \frac{1}{\xi_n} < \frac{1}{n}</equation>因此，对任意的正整数 n，都有<equation>\frac{1}{n+1}<\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}</equation>成立.

（法二）分别证明<equation>\frac{1}{n+1}<\ln \left(1+\frac{1}{n}\right)</equation>和<equation>\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}.</equation>为证明<equation>\ln \left(1 + \frac{1}{n}\right) < \frac{1}{n}</equation>，可考虑函数<equation>f(x) = \ln (1 + x) - x.</equation><equation>f^{\prime}(x)=\frac{1}{1+x}-1</equation>当 x > 0时，<equation>f^{\prime}(x)<0</equation>，故 f(x)在<equation>[0,+\infty)</equation>上单调减少.又由于 f(0) = 0，故对任意的正整数 n，<equation>f\left(\frac{1}{n}\right)<f(0)=0</equation>即<equation>\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}.</equation>为证明<equation>\frac{1}{n+1} < \ln \left( 1+\frac{1}{n} \right)</equation>，可考虑函数<equation>g(x)=\ln(1+x)-\frac{x}{1+x}.</equation><equation>g ^ {\prime} (x) = \frac {1}{1 + x} - \frac {(1 + x) - x}{(1 + x) ^ {2}} = \frac {x}{(1 + x) ^ {2}}.</equation>当 x > 0时，<equation>g^{\prime}(x) > 0</equation>，故 g(x)在<equation>[0,+\infty)</equation>上单调增加.又由于<equation>g(0)=0</equation>，故对任意的正整数n，<equation>g\left(\frac{1}{n}\right) > g(0) = 0</equation>，即<equation>\frac{1}{n+1} < \ln \left(1+\frac{1}{n}\right).</equation>综上所述，对任意的正整数 n，都有<equation>\frac{1}{n+1}<\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}</equation>成立.

（法三）注意到<equation>\ln \left( 1+\frac{1}{n} \right)=\int_{n}^{n+1} \frac{1}{x} \mathrm{d} x.</equation>由于<equation>\int_ {n} ^ {n + 1} \frac {1}{n + 1} \mathrm {d} x < \int_ {n} ^ {n + 1} \frac {1}{x} \mathrm {d} x < \int_ {n} ^ {n + 1} \frac {1}{n} \mathrm {d} x,</equation>故<equation>\frac {1}{n + 1} < \ln \left(1 + \frac {1}{n}\right) < \frac {1}{n}.</equation>（Ⅱ）若能证明数列<equation>\{a_{n}\}</equation>单调且有界，则由单调有界准则知其收敛.

先证<equation>\left\{a_{n}\right\}</equation>单调.

对任意的正整数<equation>n = 1,2,3,\dots</equation><equation>a _ {n + 1} - a _ {n} = \frac {1}{n + 1} + \ln \frac {n}{n + 1} = \frac {1}{n + 1} - \ln \left(1 + \frac {1}{n}\right).</equation>由第（I）问知，<equation>a_{n+1}-a_{n}<0</equation>，故<equation>\left\{a_{n}\right\}</equation>单调减少.

下面证明<equation>\left\{a_{n}\right\}</equation>有下界.

由第（Ⅰ）问知，<equation>\ln 2 - \ln 1 < 1,</equation><equation>\ln 3 - \ln 2 < \frac {1}{2},</equation><equation>\ln (n + 1) - \ln n < \frac {1}{n}.</equation>将上述不等式左端和右端分别相加，得<equation>\ln (n + 1) - \ln 1 < 1 + \frac {1}{2} + \dots + \frac {1}{n}.</equation>同时减去<equation>\ln n</equation>，得<equation>a _ {n} > \ln (n + 1) - \ln n > 0.</equation>因此，<equation>\{a_{n}\}</equation>有下界.

综上所述，数列<equation>\left\{a_{n}\right\}</equation>收敛.
