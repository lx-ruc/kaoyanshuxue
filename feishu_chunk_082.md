#### 定积分的应用

**2019年第17题 | 解答题 | 10分**

17. (本题满分10分）

求曲线<equation>y=\mathrm{e}^{-x}\sin x(x\geqslant 0)</equation>与x轴之间图形的面积.

**答案:**<equation>\frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}.</equation>

**解析:**解（法一）注意到<equation>\mathrm{e}^{-x}</equation>恒大于零.根据定积分的几何意义，曲线位于<equation>(k\pi ,(k + 1)\pi)</equation>的部分与<equation>x</equation>轴之间的图形面积等于<equation>\int_{k\pi}^{(k + 1)\pi}\mathrm{e}^{-x}|\sin x|\mathrm{d}x.</equation>计算<equation>S_{n}。</equation><equation>\begin{aligned} S _ {n} &= \sum_ {k = 0} ^ {n - 1} \int_ {k \pi} ^ {(k + 1) \pi} \mathrm {e} ^ {- x} | \sin x | \mathrm {d} x \xlongequal {t = x - k \pi} \sum_ {k = 0} ^ {n - 1} \int_ {0} ^ {\pi} \mathrm {e} ^ {- (t + k \pi)} | \sin (t + k \pi) | \mathrm {d} t \\ &= \sum_ {k = 0} ^ {n - 1} \mathrm {e} ^ {- k \pi} \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t. \end{aligned}</equation>下面计算<equation>\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t &= - \int_ {0} ^ {\pi} \sin t \mathrm {d} \left(\mathrm {e} ^ {- t}\right) = - \left(\sin t \mathrm {e} ^ {- t} \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \cos t \mathrm {d} t\right) \\ &= \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \cos t \mathrm {d} t = - \int_ {0} ^ {\pi} \cos t \mathrm {d} \left(\mathrm {e} ^ {- t}\right) \\ &= - \cos t \mathrm {e} ^ {- t} \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t \\ &= \mathrm {e} ^ {- \pi} + 1 - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t. \end{aligned}</equation>由上式可得<equation>2\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t = \mathrm{e}^{-\pi} + 1</equation>，于是<equation>\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t = \frac{1}{2}\left(\mathrm{e}^{-\pi} + 1\right)</equation>.

因此，<equation>S = \lim _ {n \rightarrow \infty} S _ {n} = \frac {1}{2} \left(\mathrm {e} ^ {- \pi} + 1\right) \lim _ {n \rightarrow \infty} \frac {1 - \mathrm {e} ^ {- n \pi}}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} \cdot \frac {\mathrm {e} ^ {- \pi} + 1}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}.</equation>（法二）注意到<equation>\mathrm{e}^{-x}</equation>恒大于零.当<equation>x\in(2n\pi,(2n+1)\pi)</equation>时，<equation>\sin x > 0</equation>；当<equation>x\in((2n+1)\pi,</equation><equation>(2n+2)\pi)</equation>时，<equation>\sin x < 0</equation>因此，根据定积分的几何意义，曲线位于<equation>(2n\pi, (2n+1)\pi)</equation>的部分与x轴之间的图形面积等于<equation>\int_{2n\pi}^{(2n+1)\pi}\mathrm{e}^{-x}\sin x\mathrm{d}x</equation>；曲线位于<equation>((2n+1)\pi, (2n+2)\pi)</equation>的部分与x轴之间的图形面积等于<equation>-\int_{(2n+1)\pi}^{(2n+2)\pi}\mathrm{e}^{-x}\sin x\mathrm{d}x.</equation>记所求面积为 S，则<equation>S = \sum_ {n = 0} ^ {\infty} \int_ {2 n \pi} ^ {(2 n + 1) \pi} \mathrm {e} ^ {- x} \sin x \mathrm {d} x - \sum_ {n = 0} ^ {\infty} \int_ {(2 n + 1) \pi} ^ {(2 n + 2) \pi} \mathrm {e} ^ {- x} \sin x \mathrm {d} x.</equation>下面计算<equation>\int \mathrm{e}^{-x}\sin x\mathrm{d}x.</equation><equation>\begin{aligned} \int \mathrm {e} ^ {- x} \sin x \mathrm {d} x &= - \int \sin x \mathrm {d} \left(\mathrm {e} ^ {- x}\right) = - \left(\sin x \mathrm {e} ^ {- x} - \int \mathrm {e} ^ {- x} \cos x \mathrm {d} x\right) \\ &= - \sin x \mathrm {e} ^ {- x} + \int \mathrm {e} ^ {- x} \cos x \mathrm {d} x = - \sin x \mathrm {e} ^ {- x} - \int \cos x \mathrm {d} \left(\mathrm {e} ^ {- x}\right) \\ &= - \sin x \mathrm {e} ^ {- x} - \left(\cos x \mathrm {e} ^ {- x} + \int \mathrm {e} ^ {- x} \sin x \mathrm {d} x\right). \end{aligned}</equation>由上式可得<equation>2\int \mathrm{e}^{-x}\sin x\mathrm{d}x = -\mathrm{e}^{-x}(\sin x + \cos x) - C</equation>，于是<equation>\int \mathrm {e} ^ {- x} \sin x \mathrm {d} x = - \frac {1}{2} \left[ \mathrm {e} ^ {- x} \left(\sin x + \cos x\right) + C \right],</equation>其中 C为任意常数.

因此，<equation>\begin{aligned} S &= \sum_ {n = 0} ^ {\infty} \left[ - \frac {1}{2} \mathrm {e} ^ {- x} (\sin x + \cos x) \right] \Bigg | _ {2 n \pi} ^ {(2 n + 1) \pi} + \sum_ {n = 0} ^ {\infty} \left[ \frac {1}{2} \mathrm {e} ^ {- x} (\sin x + \cos x) \right] \Bigg | _ {(2 n + 1) \pi} ^ {(2 n + 2) \pi} \\ &= \frac {1}{2} \sum_ {n = 0} ^ {\infty} \left[ \mathrm {e} ^ {- (2 n + 1) \pi} + \mathrm {e} ^ {- 2 n \pi} \right] + \frac {1}{2} \sum_ {n = 0} ^ {\infty} \left[ \mathrm {e} ^ {- (2 n + 2) \pi} + \mathrm {e} ^ {- (2 n + 1) \pi} \right] \\ &= \frac {1}{2} \left[ \sum_ {n = 0} ^ {\infty} \mathrm {e} ^ {- 2 n \pi} + 2 \sum_ {n = 0} ^ {\infty} \mathrm {e} ^ {- (2 n + 1) \pi} + \sum_ {n = 1} ^ {\infty} \mathrm {e} ^ {- 2 n \pi} \right] \\ &= \frac {1}{2} \left(\frac {1}{1 - \mathrm {e} ^ {- 2 \pi}} + \frac {2 \mathrm {e} ^ {- \pi}}{1 - \mathrm {e} ^ {- 2 \pi}} + \frac {\mathrm {e} ^ {- 2 \pi}}{1 - \mathrm {e} ^ {- 2 \pi}}\right) = \frac {1}{2} \cdot \frac {\left(1 + \mathrm {e} ^ {- \pi}\right) ^ {2}}{\left(1 + \mathrm {e} ^ {- \pi}\right) \left(1 - \mathrm {e} ^ {- \pi}\right)} \\ &= \frac {1}{2} \cdot \frac {1 + \mathrm {e} ^ {- \pi}}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}. \end{aligned}</equation>

---

**2017年第4题 | 选择题 | 4分 | 答案: C**

4. 甲、乙两人赛跑，计时开始时，甲在乙前方10（单位：m）处，图中，实线表示甲的速度曲线<equation>v=v_{1}(t)</equation>（单位： m/s），虚线表示乙的速度曲线<equation>v=v_{2}(t)</equation>，三块阴影部分面积的数值依次是10，20，3. 计时开始后乙追上甲的时刻记为<equation>t_{0}</equation>（单位：s），则（    ）

A.<equation>t_{0}=1 0</equation>B.<equation>1 5<t_{0}<2 0</equation>C.<equation>t_{0}=2 5</equation>D.<equation>t_{0}>2 5</equation>

答案: C

**解析:**解 根据定积分的物理意义，从0s到10s这段时间内，实线位于虚线之上，于是甲跑过的路程比乙跑过的路程多10m；从10s到25s这段时间内，虚线位于实线之上，于是乙跑过的路程比甲跑过的路程多20m.

---

**2012年第18题 | 解答题 | 10分**

18. (本题满分10分)

已知曲线 L：<equation>\left\{\begin{array}{l l}x=f(t),\\ y=\cos t\end{array}\right.</equation><equation>(0\leqslant t<\frac{\pi}{2})</equation>，其中函数 f(t)具有连续导数，且 f(0)=0，<equation>f^{\prime}(t)>0</equation><equation>(0<t<\frac{\pi}{2})</equation>. 若曲线 L的切线与 x轴的交点到切点的距离恒为1，求函数 f(t)的表达式，并求以曲线 L及 x轴和 y轴为边界的区域的面积.

**答案:**(18)<equation>f ( t )=\ln | \sec t+\tan t |-\sin t, 0\leqslant t < \frac{\pi}{2}</equation>; 面积为<equation>\frac{\pi}{4}</equation>

**解析:**解曲线 L在点（ f(t），cos t）处的切线的斜率为<equation>\frac{\mathrm{d} y}{\mathrm{d} x}=\frac{\frac{\mathrm{d} y}{\mathrm{d} t}}{\frac{\mathrm{d} x}{\mathrm{d} t}}=-\frac{\sin t}{f^{\prime}(t)},</equation>从而切线方程为<equation>y - \cos t = \frac {- \sin t}{f ^ {\prime} (t)} [ x - f (t) ],</equation>于是切线与<equation>x</equation>轴的交点为<equation>\left(f(t) + \frac{\cos t}{\sin t} f^{\prime}(t),0\right)</equation>.由已知条件可得<equation>\left[ f (t) + \frac {\cos t}{\sin t} f ^ {\prime} (t) - f (t) \right] ^ {2} + \left(0 - \cos t\right) ^ {2} = 1,</equation>化简得<equation>[f^{\prime}(t)]^{2} = \left(\frac{\sin^{2}t}{\cos t}\right)^{2}</equation>.

由于当<equation>0 < t < \frac{\pi}{2}</equation>时，<equation>f^{\prime}(t) > 0</equation>，故<equation>f^{\prime}(t) = \frac{\sin^{2}t}{\cos t}</equation>. 又<equation>f(0) = 0</equation>，故<equation>\forall 0\leqslant t < \frac{\pi}{2}</equation>，有<equation>f (t) = \int_ {0} ^ {t} \frac {\sin^ {2} x}{\cos x} \mathrm {d} x = \int_ {0} ^ {t} \frac {1 - \cos^ {2} x}{\cos x} \mathrm {d} x = \int_ {0} ^ {t} \sec x \mathrm {d} x - \int_ {0} ^ {t} \cos x \mathrm {d} x = \ln | \sec t + \tan t | - \sin t,</equation>设以曲线<equation>L</equation>及<equation>x</equation>轴和<equation>y</equation>轴为边界的区域的面积为<equation>S</equation>，则<equation>\begin{aligned} S &= \int_ {0} ^ {\frac {\pi}{2}} y (t) \mathrm {d} \left(x (t)\right) = \int_ {0} ^ {\frac {\pi}{2}} \cos t \cdot x ^ {\prime} (t) \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \cos t \cdot f ^ {\prime} (t) \mathrm {d} t \\ &= \int_ {0} ^ {\frac {\pi}{2}} \cos t \cdot \frac {\sin^ {2} t}{\cos t} \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {2} t \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \frac {1 - \cos 2 t}{2} \mathrm {d} t = \frac {\pi}{4}. \end{aligned}</equation>

---

**2011年第9题 | 填空题 | 4分**

9. 曲线<equation>y=\int_{0}^{x}\tan t\mathrm{d}t \left( 0\leqslant x\leqslant\frac{\pi}{4} \right)</equation>的弧长 s = ___

**答案:**##<equation>\ln(\sqrt{2}+1).</equation>

**解析:**<equation>\begin{aligned} s &= \int_ {0} ^ {\frac {\pi}{4}} \sqrt {1 + \left[ y ^ {\prime} (x) \right] ^ {2}} \mathrm {d} x = \int_ {0} ^ {\frac {\pi}{4}} \sqrt {1 + \tan^ {2} x} \mathrm {d} x \\ &= \int_ {0} ^ {\frac {\pi}{4}} \sec x \mathrm {d} x = \ln | \sec x + \tan x | \Bigg | _ {0} ^ {\frac {\pi}{4}} = \ln (\sqrt {2} + 1). \end{aligned}</equation>

---

**2009年第17题 | 解答题 | 10分**

17. (本题满分11分)

椭球面<equation>S_{1}</equation>是椭圆<equation>\frac{x^{2}}{4}+\frac{y^{2}}{3}=1</equation>绕 x轴旋转而成，圆雉面<equation>S_{2}</equation>是由过点(4,0)且与椭圆<equation>\frac{x^{2}}{4}+\frac{y^{2}}{3}=1</equation>相切的直线绕 x轴旋转而成.

I. 求<equation>S_{1}</equation>及<equation>S_{2}</equation>的方程；

II. 求<equation>S_{1}</equation>与<equation>S_{2}</equation>之间的立体的体积.

**答案:**(17) （I）椭球面<equation>S_{1}</equation>的方程为<equation>\frac{x^{2}}{4}+\frac{y^{2}+z^{2}}{3}=1</equation>，圆锥面<equation>S_{2}</equation>的方程为<equation>y^{2}+z^{2}=\frac{1}{4}(x-4)^{2}</equation>； （Ⅱ）<equation>V=\pi.</equation>

**解析:**解（I）由椭圆<equation>\frac{x^{2}}{4}+\frac{y^{2}}{3}=1</equation>绕 x轴旋转得到的椭球面<equation>S_{1}</equation>的方程为<equation>\frac {x ^ {2}}{4} + \frac {\left(\pm \sqrt {y ^ {2} + z ^ {2}}\right) ^ {2}}{3} = 1,</equation>即为<equation>\frac{x^2}{4} +\frac{y^2 + z^2}{3} = 1.</equation>设椭圆<equation>\frac{x^{2}}{4}+\frac{y^{2}}{3}=1</equation>上任一点为（<equation>2\cos \theta ,\sqrt{3}\sin \theta )</equation>，则过该点且与椭圆相切的直线的斜率为<equation>\frac{\mathrm{d}y}{\mathrm{d}x}=</equation><equation>\frac{\frac{\mathrm{d}y}{\mathrm{d}\theta}}{\frac{\mathrm{d}x}{\mathrm{d}\theta}}=\frac{(\sqrt{3}\sin \theta)^{\prime}}{(2\cos \theta)^{\prime}}=\frac{\sqrt{3}\cos \theta}{-2\sin \theta}</equation>，从而切线方程为<equation>y = - \frac {\sqrt {3} \cos \theta}{2 \sin \theta} (x - 2 \cos \theta) + \sqrt {3} \sin \theta .</equation>将<equation>( x,y)=(4,0)</equation>代入上式得<equation>\cos \theta=\frac{1}{2},\sin \theta=\pm \frac{\sqrt{3}}{2}</equation>，于是切线方程为<equation>y=\pm \frac{1}{2} ( x-4 )</equation>，切点为<equation>\left( 1,\pm \frac{3}{2} \right).</equation>又圆锥面<equation>S_{2}</equation>是由直线<equation>y=\frac{1}{2} ( x-4 )</equation>绕x轴旋转得到，故<equation>S_{2}</equation>的方程为<equation>\pm \sqrt{y^{2}+z^{2}}=\frac{1}{2} ( x-4 )</equation>即为<equation>y^{2}+z^{2}=\frac{1}{4} ( x-4 )^{2}.</equation>（Ⅱ）记<equation>V_{1}</equation>为椭球面<equation>S_{1}</equation>所围成的椭球体在平面<equation>x=1</equation>与<equation>x=2</equation>之间的部分的体积，则由旋转体体积公式知，<equation>V_{1}=\pi \int_{1}^{2} y^{2}\mathrm{d}x=\pi \int_{1}^{2} 3 \left( 1-\frac{x^{2}}{4} \right) \mathrm{d}x=\frac{5}{4} \pi</equation>；记<equation>V_{2}</equation>为圆锥面<equation>S_{2}</equation>与平面<equation>x=1</equation>所围成的区域的体积，即底面半径为<equation>\frac{3}{2}</equation>，高为3的圆锥体体积，则<equation>V_{2}=\frac{1}{3}\pi r^{2} h=\frac{1}{3}\pi \cdot \left( \frac{3}{2} \right)^{2} \cdot 3=\frac{9}{4}\pi.</equation>因此，<equation>S_{1}</equation>与<equation>S_{2}</equation>之间的立体的体积为<equation>V=V_{2}-V_{1}=\frac{9}{4}\pi -\frac{5}{4}\pi =\pi.</equation>

---


