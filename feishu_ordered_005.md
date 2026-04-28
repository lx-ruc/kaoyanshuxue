# 数学一

## 高等数学

### 一元函数积分学

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


#### 不定积分的计算

**2018年第15题 | 解答题 | 10分**

15. (本题满分10分)

求不定积分

**答案:**<equation>\frac{\mathrm{e}^{2x}\arctan \sqrt{\mathrm{e}^{x} - 1}}{2} -\frac{1}{6}\left(\mathrm{e}^{x} - 1\right)^{\frac{3}{2}} - \frac{1}{2}\sqrt{\mathrm{e}^{x} - 1} + C</equation>，其中C为任意常数.

**解析:**解 利用分部积分法.<equation>\begin{aligned} \int \mathrm {e} ^ {2 x} \arctan \sqrt {\mathrm {e} ^ {x} - 1} \mathrm {d} x \stackrel {\text {分 部 积 分}} {=} \frac {1}{2} \int \arctan \sqrt {\mathrm {e} ^ {x} - 1} \mathrm {d} \left(\mathrm {e} ^ {2 x}\right) \\ &= \frac {\mathrm {e} ^ {2 x}}{2} \cdot \arctan \sqrt {\mathrm {e} ^ {x} - 1} - \frac {1}{2} \int \mathrm {e} ^ {2 x} \cdot \frac {1}{1 + \mathrm {e} ^ {x} - 1} \cdot \frac {\mathrm {e} ^ {x}}{2 \sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x \\ &= \frac {\mathrm {e} ^ {2 x} \arctan \sqrt {\mathrm {e} ^ {x} - 1}}{2} - \frac {1}{4} \int \frac {\mathrm {e} ^ {2 x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x. \end{aligned}</equation>下面用两种方法计算<equation>\int \frac{\mathrm{e}^{2x}}{\sqrt{\mathrm{e}^{x} - 1}}\mathrm{d}x.</equation>（法一）令<equation>u = \sqrt{\mathrm{e}^{x} - 1}</equation>，则<equation>x = \ln (u^{2} + 1)</equation>，<equation>\mathrm{d}x = \frac{2u}{u^{2} + 1}\mathrm{d}u.</equation><equation>\begin{aligned} \int \frac {\mathrm {e} ^ {2 x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x &= \int \frac {\left(u ^ {2} + 1\right) ^ {2}}{u} \cdot \frac {2 u}{u ^ {2} + 1} \mathrm {d} u = 2 \int \left(u ^ {2} + 1\right) \mathrm {d} u = \frac {2}{3} u ^ {3} + 2 u + C _ {1} \\ &= \frac {2}{3} \left(\mathrm {e} ^ {x} - 1\right) ^ {\frac {3}{2}} + 2 \sqrt {\mathrm {e} ^ {x} - 1} + C _ {1}, \end{aligned}</equation>其中<equation>C_{1}</equation>为任意常数.

（法二）令<equation>t = \mathrm{e}^{x}</equation>，则<equation>\mathrm{d}t = \mathrm{e}^{x}\mathrm{d}x.</equation><equation>\begin{aligned} \int \frac {\mathrm {e} ^ {2 x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x &= \int \frac {\mathrm {e} ^ {x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} \left(\mathrm {e} ^ {x}\right) = \int \frac {t}{\sqrt {t - 1}} \mathrm {d} t = \int \frac {t - 1 + 1}{\sqrt {t - 1}} \mathrm {d} t = \int \left(\sqrt {t - 1} + \frac {1}{\sqrt {t - 1}}\right) \mathrm {d} t \\ &= \frac {2}{3} (t - 1) ^ {\frac {3}{2}} + 2 \sqrt {t - 1} + C _ {1} = \frac {2}{3} \left(\mathrm {e} ^ {x} - 1\right) ^ {\frac {3}{2}} + 2 \sqrt {\mathrm {e} ^ {x} - 1} + C _ {1}, \end{aligned}</equation>其中<equation>C_{1}</equation>为任意常数.

因此，<equation>\text {原 积 分} = \frac {\mathrm {e} ^ {2 x} \arctan \sqrt {\mathrm {e} ^ {x} - 1}}{2} - \frac {1}{6} \left(\mathrm {e} ^ {x} - 1\right) ^ {\frac {3}{2}} - \frac {1}{2} \sqrt {\mathrm {e} ^ {x} - 1} + C,</equation>其中 C为任意常数.

---

**2016年第2题 | 选择题 | 4分 | 答案: D**

2. 已知函数<equation>f(x)=\left\{\begin{array}{l l}2(x-1),&x<1,\\ \ln x,&x\geqslant 1,\end{array} \right.</equation>则 f(x)的一个原函数是（    ）

A.<equation>F(x)=\left\{\begin{array}{l l}{(x-1)^{2},}&{x<1,}\\ {x(\ln x-1),}&{x\geqslant 1.}\\ \end{array} \right.</equation>B.<equation>F(x)=\left\{\begin{array}{l l}{(x-1)^{2},}&{x<1,}\\ {x(\ln x+1)-1,}&{x\geqslant 1.}\\ \end{array} \right.</equation>C.<equation>F(x)=\left\{\begin{array}{l l}{(x-1)^{2},}&{x<1,}\\ {x(\ln x+1)+1,}&{x\geqslant 1.}\\ \end{array} \right.</equation>D.<equation>F(x)=\left\{\begin{array}{l l}{(x-1)^{2},}&{x<1,}\\ {x(\ln x-1)+1,}&{x\geqslant 1.}\\ \end{array} \right.</equation>

答案: D

**解析:**解（法一）当 x < 1时，<equation>F (x) = \int 2 (x - 1) \mathrm {d} x = (x - 1) ^ {2} + C _ {1};</equation>当 x≥1时，<equation>F (x) = \int \ln x \mathrm {d} x = x (\ln x - 1) + C _ {2},</equation>其中<equation>C_{1}, C_{2}</equation>均为任意常数.

进一步，由于<equation>F(x)</equation>是<equation>f(x)</equation>在<equation>(-\infty , + \infty)</equation>上的一个原函数，故<equation>F(x)</equation>在<equation>x = 1</equation>处应连续.<equation>\lim _ {x \rightarrow 1 ^ {-}} F (x) = \lim _ {x \rightarrow 1 ^ {-}} \left(x - 1\right) ^ {2} + C _ {1} = C _ {1}, \quad \lim _ {x \rightarrow 1 ^ {+}} F (x) = \lim _ {x \rightarrow 1 ^ {+}} x \left(\ln x - 1\right) + C _ {2} = C _ {2} - 1.</equation>若<equation>F ( x )</equation>连续，则<equation>C_{1}=C_{2}-1.</equation>选项D中，<equation>C_{1}=0, C_{2}=1, F(x)</equation>连续，应选D.

（法二）首先，由于<equation>F ( x )</equation>是<equation>f ( x )</equation>的原函数，故必连续，而四个选项中的<equation>F ( x )</equation>均是分段函数，于是我们可以分别考察<equation>F ( x )</equation>在分界点处的连续性.

选项A：<equation>\lim_{x\to 1^{-}}F(x)=0,\lim_{x\to 1^{+}}F(x)=-1.F(x)</equation>不连续.

选项B：<equation>\lim_{x\to 1^{-}}F(x)=\lim_{x\to 1^{+}}F(x)=0=F(1). F(x)</equation>连续.

选项C：<equation>\lim_{x\to 1^{-}}F(x) = 0</equation>，<equation>\lim_{x\to 1^{+}}F(x) = 2.F(x)</equation>不连续.

选项D：<equation>\lim_{x\to 1^{-}}F(x) = \lim_{x\to 1^{+}}F(x) = 0 = F(1).F(x)</equation>连续.

由上可排除选项A与选项C.

选项B与选项D的差别在于函数表达式.

计算<equation>f(x)</equation>在<equation>[1, +\infty)</equation>上的原函数，得<equation>\int f (x) \mathrm {d} x = \int \ln x \mathrm {d} x = x (\ln x - 1) + C,</equation>其中 C为任意常数.比较（1）式与选项B、选项D，可排除选项B.应选D.

---


### 常微分方程
#### 一阶非齐次线性微分方程

**2025年第18题 | 解答题 | 12分**
18. 已知函数 f(u)在区间 （0，<equation>+ \infty</equation>）内具有2阶导数，记<equation>g ( x,y)=f\left(\frac{x}{y}\right)</equation>，若 g(x,y)满足<equation>x ^ {2} \frac {\partial^ {2} g}{\partial x ^ {2}} + x y \frac {\partial^ {2} g}{\partial x \partial y} + y ^ {2} \frac {\partial^ {2} g}{\partial y ^ {2}} = 1,</equation>且<equation>g ( x,x)=1,\frac{\partial g}{\partial x}\bigg|_{(x,x)}=\frac{2}{x}</equation>，求 f(u).
**答案: **<equation>f ( u ) = \frac { 1 } { 2 } \left( \ln u \right)^{2}+2 \ln u+1.</equation>
**解析: **解 根据链式法则，<equation>\frac {\partial g}{\partial x} = f ^ {\prime} \left(\frac {x}{y}\right) \cdot \frac {1}{y}, \quad \frac {\partial g}{\partial y} = f ^ {\prime} \left(\frac {x}{y}\right) \cdot \left(- \frac {x}{y ^ {2}}\right),</equation><equation>\frac {\partial^ {2} g}{\partial x ^ {2}} = f ^ {\prime \prime} \left(\frac {x}{y}\right) \cdot \frac {1}{y ^ {2}},</equation><equation>\frac {\partial^ {2} g}{\partial x \partial y} = f ^ {\prime \prime} \left(\frac {x}{y}\right) \cdot \left(- \frac {x}{y ^ {2}}\right) \cdot \frac {1}{y} - \frac {1}{y ^ {2}} f ^ {\prime} \left(\frac {x}{y}\right) = - \frac {x}{y ^ {3}} f ^ {\prime \prime} \left(\frac {x}{y}\right) - \frac {1}{y ^ {2}} f ^ {\prime} \left(\frac {x}{y}\right),</equation><equation>\frac {\partial^ {2} g}{\partial y ^ {2}} = f ^ {\prime \prime} \left(\frac {x}{y}\right) \cdot \left(- \frac {x}{y ^ {2}}\right) \cdot \left(- \frac {x}{y ^ {2}}\right) + \frac {2 x}{y ^ {3}} f ^ {\prime} \left(\frac {x}{y}\right) = \frac {x ^ {2}}{y ^ {4}} f ^ {\prime \prime} \left(\frac {x}{y}\right) + \frac {2 x}{y ^ {3}} f ^ {\prime} \left(\frac {x}{y}\right).</equation>代入<equation>x^{2}\frac{\partial^{2}g}{\partial x^{2}}+xy\frac{\partial^{2}g}{\partial x\partial y}+y^{2}\frac{\partial^{2}g}{\partial y^{2}}=1</equation>可得<equation>\frac {x ^ {2}}{y ^ {2}} f ^ {\prime \prime} \left(\frac {x}{y}\right) - \frac {x ^ {2}}{y ^ {2}} f ^ {\prime \prime} \left(\frac {x}{y}\right) - \frac {x}{y} f ^ {\prime} \left(\frac {x}{y}\right) + \frac {x ^ {2}}{y ^ {2}} f ^ {\prime \prime} \left(\frac {x}{y}\right) + \frac {2 x}{y} f ^ {\prime} \left(\frac {x}{y}\right) = 1.</equation>整理可得<equation>\frac{x^2}{y^2} f^{\prime \prime}\left(\frac{x}{y}\right) + \frac{x}{y} f^{\prime}\left(\frac{x}{y}\right) = 1.</equation>令<equation>u=\frac{x}{y}</equation>，可得<equation>u^{2}f^{\prime \prime}(u)+u f^{\prime}(u)=1.</equation>下面用两种方法解该方程

（法一）整理<equation>u^{2}f^{\prime \prime}(u)+u f^{\prime}(u)=1</equation>可得<equation>f^{\prime \prime}(u)+\frac{1}{u} f^{\prime}(u)=\frac{1}{u^{2}}.</equation>这是一个可降阶微分方程.令<equation>p=f^{\prime}(u)</equation>，则该方程化为<equation>p^{\prime}+\frac{p}{u}=\frac{1}{u^{2}}.</equation>由一阶非齐次线性微分方程的通解公式可得<equation>p = \mathrm {e} ^ {\int \left(- \frac {1}{u}\right) \mathrm {d} u} \left(\int \frac {1}{u ^ {2}} \cdot \mathrm {e} ^ {\int \frac {1}{u} \mathrm {d} u} \mathrm {d} u + C _ {1}\right) = \frac {1}{u} \left(\int \frac {1}{u} \mathrm {d} u + C _ {1}\right) = \frac {1}{u} \left(\ln u + C _ {1}\right),</equation>其中<equation>C_{1}</equation>为待定常数.

由<equation>\frac{\partial g}{\partial x}=f^{\prime}\left(\frac{x}{y}\right)\cdot \frac{1}{y}</equation>可得<equation>\frac{\partial g}{\partial x}\bigg|_{(x,x)}=\frac{1}{x} f^{\prime}(1),</equation>结合<equation>\frac{\partial g}{\partial x}\bigg|_{(x,x)}=\frac{2}{x}</equation>可得<equation>f^{\prime}(1)=2.</equation>代入<equation>f^{\prime}(u)</equation><equation>= \frac{1}{u} (\ln u + C_1)</equation>可得<equation>C_{1}=2.</equation>于是，<equation>f^{\prime}(u)=\frac{1}{u}(\ln u+2).</equation>进一步积分可得<equation>f (u) = \int \frac {1}{u} (\ln u + 2) \mathrm {d} u = \int \ln u \mathrm {d} (\ln u) + \int \frac {2}{u} \mathrm {d} u = \frac {1}{2} (\ln u) ^ {2} + 2 \ln u + C _ {2},</equation>其中<equation>C_{2}</equation>为待定常数.

由<equation>g(x,x) = 1</equation>可得<equation>f(1) = 1</equation>，代入<equation>f(u) = \frac{1}{2} (\ln u)^{2} + 2\ln u + C_{2}</equation>可得<equation>C_{2} = 1.</equation>因此，<equation>f(u)=\frac{1}{2} (\ln u)^{2}+2\ln u+1.</equation>（法二）注意到<equation>u^{2} f^{\prime \prime}(u) + uf^{\prime}(u) = 1</equation>是欧拉方程

令<equation>u=\mathrm{e}^{\prime}.</equation>于是，<equation>\frac {\mathrm {d} f}{\mathrm {d} t} = \frac {\mathrm {d} f}{\mathrm {d} u} \cdot \frac {\mathrm {d} u}{\mathrm {d} t} = \frac {\mathrm {d} f}{\mathrm {d} u} \cdot \mathrm {e} ^ {t}.</equation><equation>\frac {\mathrm {d} ^ {2} f}{\mathrm {d} t ^ {2}} = \frac {\mathrm {d} \left(\frac {\mathrm {d} f}{\mathrm {d} u} \cdot \mathrm {e} ^ {t}\right)}{\mathrm {d} t} = \frac {\mathrm {d} ^ {2} f}{\mathrm {d} u ^ {2}} \cdot \frac {\mathrm {d} u}{\mathrm {d} t} \cdot \mathrm {e} ^ {t} + \frac {\mathrm {d} f}{\mathrm {d} u} \cdot \mathrm {e} ^ {t} = \frac {\mathrm {d} ^ {2} f}{\mathrm {d} u ^ {2}} \cdot \mathrm {e} ^ {2 t} + \frac {\mathrm {d} f}{\mathrm {d} u} \cdot \mathrm {e} ^ {t} = \frac {\mathrm {d} ^ {2} f}{\mathrm {d} u ^ {2}} \cdot \mathrm {e} ^ {2 t} + \frac {\mathrm {d} f}{\mathrm {d} t}.</equation>由此可得<equation>\frac{\mathrm{d}f}{\mathrm{d}u} = \mathrm{e}^{-t}\frac{\mathrm{d}f}{\mathrm{d}t},\frac{\mathrm{d}^2f}{\mathrm{d}u^2} = \mathrm{e}^{-2t}\left(\frac{\mathrm{d}^2f}{\mathrm{d}t^2} -\frac{\mathrm{d}f}{\mathrm{d}t}\right)</equation>，于是<equation>u^{2}f^{\prime \prime}(u) = \frac{\mathrm{d}^2f}{\mathrm{d}t^2} -\frac{\mathrm{d}f}{\mathrm{d}t},uf^{\prime}(u) = \frac{\mathrm{d}f}{\mathrm{d}t}</equation>代入<equation>u^{2}f^{\prime \prime}(u)</equation><equation>+uf^{\prime}(u) = 1</equation>可得<equation>\frac{\mathrm{d}^2f}{\mathrm{d}t^2} = 1.</equation>这是一个二阶常系数非齐次线性微分方程，其对应的齐次方程的特征方程为<equation>\lambda^2 = 0</equation>，特征根为<equation>\lambda_{1,2} = 0</equation>.于是，该齐次方程的解为<equation>y = C_{1} + C_{2} t</equation>，其中<equation>C_{1}, C_{2}</equation>为待定常数.

由于0是特征方程的二重根，故可设<equation>\frac{\mathrm{d}^2f}{\mathrm{d}t^2} = 1</equation>的特解<equation>y^{*} = At^{2}</equation>. 将<equation>y^{*} = At^{2}</equation>代入<equation>\frac{\mathrm{d}^2f}{\mathrm{d}t^2} = 1</equation>可得2A<equation>= 1</equation>，即<equation>A = \frac{1}{2}</equation>.由此可得<equation>y^{*} = \frac{1}{2} t^{2}</equation>，进一步可得<equation>\frac{\mathrm{d}^2f}{\mathrm{d}t^2} = 1</equation>的解为<equation>y = C_{1} + C_{2}t + \frac{1}{2} t^{2}</equation>.由<equation>u = \mathrm{e}^{t}</equation>可得<equation>t = \ln u</equation>，从而<equation>f(u) = C_{1} + C_{2}\ln u + \frac{1}{2}(\ln u)^{2}</equation>.计算可得<equation>f^{\prime}(u) = \frac{1}{u}(\ln u + C_{2})</equation>同法一可得<equation>f(1) = 1,f^{\prime}(1) = 2</equation>，代入<equation>f(u),f^{\prime}(u)</equation>的表达式解得<equation>\left\{ \begin{array}{l} C_{1} = 1, \\ C_{2} = 2 \end{array} \right.</equation>因此，<equation>f ( u ) = \frac { 1 } { 2 } \left( \ln u \right)^{2}+2 \ln u+1.</equation>

---

**2022年第17题 | 解答题 | 10分**
17. (本题满分10分）

设函数 y(x)是微分方程<equation>y^{\prime}+\frac{1}{2\sqrt{x}} y=2+\sqrt{x}</equation>的满足条件 y(1)=3的解，求曲线 y=y(x)的渐近线.
**答案: **<equation>y=2 x</equation>为曲线<equation>y=2 x+\mathrm{e}^{1-\sqrt{x}}</equation>的斜渐近线，也是唯一的渐近线.
**解析: **解 根据求解公式，<equation>y = \mathrm {e} ^ {- \int \frac {1}{2 \sqrt {x}} \mathrm {d} x} \left[ \int (2 + \sqrt {x}) \mathrm {e} ^ {\int \frac {1}{2 \sqrt {x}} \mathrm {d} x} \mathrm {d} x + C _ {0} \right] = \mathrm {e} ^ {- \sqrt {x}} \left[ \int (2 + \sqrt {x}) \mathrm {e} ^ {\sqrt {x}} \mathrm {d} x + C _ {0} \right].</equation>下面计算<equation>\int (2 + \sqrt{x})\mathrm{e}^{\sqrt{x}}\mathrm{d}x.</equation>令<equation>u=\sqrt{x}</equation>，则<equation>x=u^{2}</equation>，<equation>\mathrm{d}x=2u\mathrm{d}u.</equation><equation>\begin{aligned} \int (2 + \sqrt {x}) \mathrm {e} ^ {\sqrt {x}} \mathrm {d} x \xlongequal {u = \sqrt {x}} 2 \int (2 + u) u \mathrm {e} ^ {u} \mathrm {d} u &= 2 \left(\int u ^ {2} \mathrm {e} ^ {u} \mathrm {d} u + \int 2 u \mathrm {e} ^ {u} \mathrm {d} u\right) \\ &= 2 \left[ \int u ^ {2} \mathrm {d} \left(\mathrm {e} ^ {u}\right) + \int 2 u \mathrm {e} ^ {u} \mathrm {d} u \right] = 2 \left(u ^ {2} \mathrm {e} ^ {u} - \int 2 u \mathrm {e} ^ {u} \mathrm {d} u + \int 2 u \mathrm {e} ^ {u} \mathrm {d} u\right) \\ &= 2 u ^ {2} \mathrm {e} ^ {u} + C _ {1} = 2 x \mathrm {e} ^ {\sqrt {x}} + C _ {1}. \end{aligned}</equation>将该结果代入（1）式，可得<equation>y = \mathrm {e} ^ {- \sqrt {x}} \left(2 x \mathrm {e} ^ {\sqrt {x}} + C\right) = 2 x + C \mathrm {e} ^ {- \sqrt {x}},</equation>其中<equation>C</equation>为待定常数. 代入<equation>y(1) = 3</equation>，可得<equation>3 = 2 + C \cdot \mathrm{e}^{-1}</equation>，解得<equation>C = \mathrm{e}</equation>.

因此，<equation>y ( x ) = 2 x + \mathrm {e} ^ {1 - \sqrt {x}} , x \in ( 0, + \infty).</equation>由于函数<equation>y(x) = 2x + \mathrm{e}^{1 - \sqrt{x}}</equation>在<equation>(0, +\infty)</equation>内连续，且<equation>\lim_{x\to 0^{+}}y(x) = \mathrm{e}</equation>，故曲线<equation>y = 2x + \mathrm{e}^{1 - \sqrt{x}}</equation>没有铅直渐近线.

又因为<equation>\lim_{x\to +\infty}y(x) = \lim_{x\to +\infty}\left(2x + \mathrm{e}^{1 - \sqrt{x}}\right) = +\infty</equation>，所以曲线<equation>y = 2x + \mathrm{e}^{1 - \sqrt{x}}</equation>没有水平渐近线.

下面计算斜渐近线.<equation>\lim _ {x \rightarrow + \infty} \frac {y (x)}{x} = \lim _ {x \rightarrow + \infty} \frac {2 x + \mathrm {e} ^ {1 - \sqrt {x}}}{x} = 2,</equation><equation>\lim _ {x \rightarrow + \infty} [ y (x) - 2 x ] = \lim _ {x \rightarrow + \infty} \mathrm {e} ^ {1 - \sqrt {x}} = 0.</equation>因此，<equation>y=2x</equation>为曲线<equation>y=2x+\mathrm{e}^{1-\sqrt{x}}</equation>的斜渐近线，也是唯一的渐近线.

---

**2019年第15题 | 解答题 | 10分**
15. (本题满分10分)

设函数 y(x)是微分方程<equation>y^{\prime}+xy=\mathrm{e}^{-\frac{x^{2}}{2}}</equation>满足条件 y(0)=0的特解.

I. 求 y(x) ;

II. 求曲线 y=y(x)的凹凸区间及拐点.
**答案: **（I）<equation>y ( x )=x \mathrm{e}^{- \frac{x^{2}}{2}};</equation>（Ⅱ）凹区间为<equation>(-\sqrt{3},0)</equation>和<equation>(\sqrt{3},+\infty)</equation>，凸区间为<equation>(-\infty,-\sqrt{3})</equation>和<equation>(0,\sqrt{3})</equation>，拐点为<equation>(-\sqrt{3},-\sqrt{3} \mathrm{e}^{- \frac{3}{2}}),(0,0)</equation>和<equation>(\sqrt{3},\sqrt{3} \mathrm{e}^{- \frac{3}{2}}).</equation>
**解析: **（I）由一阶非齐次线性微分方程的求解公式可得，<equation>y = \mathrm {e} ^ {\int (- x) \mathrm {d} x} \left(\int \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \cdot \mathrm {e} ^ {\int x \mathrm {d} x} \mathrm {d} x + C\right) = \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \left(\int 1 \mathrm {d} x + C\right) = x \mathrm {e} ^ {- \frac {x ^ {2}}{2}} + C \mathrm {e} ^ {- \frac {x ^ {2}}{2}},</equation>其中 C为待定常数.

代入<equation>x = 0</equation>，<equation>y(0) = 0</equation>可得，<equation>C = 0.</equation>因此，<equation>y = x\mathrm{e}^{-\frac{x^2}{2}}.</equation>（Ⅱ）分别计算<equation>y^{\prime}, y^{\prime\prime}.</equation><equation>y ^ {\prime} = \mathrm {e} ^ {- \frac {x ^ {2}}{2}} + x \cdot \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \cdot (- x) = \left(1 - x ^ {2}\right) \mathrm {e} ^ {- \frac {x ^ {2}}{2}},</equation><equation>y ^ {\prime \prime} = (- 2 x) \mathrm {e} ^ {- \frac {x ^ {2}}{2}} + \left(1 - x ^ {2}\right) \cdot \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \cdot (- x) = \left(x ^ {3} - 3 x\right) \mathrm {e} ^ {- \frac {x ^ {2}}{2}}.</equation>令<equation>y^{\prime \prime}=0</equation>，可得<equation>x=0</equation><equation>x=\pm \sqrt{3}</equation>.当<equation>x < -\sqrt{3}</equation>时，<equation>y^{\prime \prime} < 0</equation>；当<equation>-\sqrt{3} < x < 0</equation>时，<equation>y^{\prime \prime} > 0</equation>；当<equation>0 < x < \sqrt{3}</equation>时，<equation>y^{\prime \prime} < 0</equation>；当<equation>x > \sqrt{3}</equation>时，<equation>y^{\prime \prime} > 0.</equation>因此，<equation>y=y(x)</equation>的凹区间为<equation>(-\sqrt{3},0)</equation>和<equation>(\sqrt{3},+\infty)</equation>，凸区间为<equation>(-\infty,-\sqrt{3})</equation>和<equation>(0,\sqrt{3})</equation>。拐点共有3个：<equation>(-\sqrt{3},-\sqrt{3}\mathrm{e}^{-\frac{3}{2}}),(0,0),(\sqrt{3},\sqrt{3}\mathrm{e}^{-\frac{3}{2}}).</equation>

---

**2018年第18题 | 解答题 | 10分**
18. (本题满分10分)

已知微分方程<equation>y^{\prime}+y=f(x)</equation>，其中 f(x)是 R上的连续函数.

I. 若 f(x)=x，求方程的通解;

II. 若 f(x)是周期为 T的函数，证明：方程存在唯一的以 T为周期的解.
**答案: **（I）<equation>y=x-1+C\mathrm{e}^{-x}</equation>，其中C为任意常数； （Ⅱ）证明略.
**解析: **解（I）若<equation>f ( x )=x</equation>，则<equation>y^{\prime}+y=f ( x )</equation>是一阶非齐次线性微分方程根据求解公式，可得已知方程的通解为<equation>\begin{aligned} y &= \mathrm {e} ^ {- \int \mathrm {d} x} \left(\int x \cdot \mathrm {e} ^ {\int \mathrm {d} x} \mathrm {d} x + C\right) = \mathrm {e} ^ {- x} \left(\int x \cdot \mathrm {e} ^ {x} \mathrm {d} x + C\right) \\ &= \mathrm {e} ^ {- x} \left[ (x - 1) \mathrm {e} ^ {x} + C \right] = x - 1 + C \mathrm {e} ^ {- x}, \end{aligned}</equation>其中 C为任意常数.

（Ⅱ）下面证明方程<equation>y^{\prime} + y = f(x)</equation>的以<equation>T</equation>为周期的解存在.

根据求解公式，可得已知方程的通解为<equation>y (x) = \mathrm {e} ^ {- x} \left[ \int f (x) \mathrm {e} ^ {x} \mathrm {d} x + C ^ {\prime} \right] = \mathrm {e} ^ {- x} \left[ \int_ {0} ^ {x} f (t) \mathrm {e} ^ {t} \mathrm {d} t + C \right],</equation>其中 C为任意常数.

于是，<equation>\begin{aligned} y (x + T) &= \mathrm {e} ^ {- x - T} \left[ \int_ {0} ^ {x + T} f (t) \mathrm {e} ^ {t} \mathrm {d} t + C \right] = \mathrm {e} ^ {- x - T} \left[ \int_ {0} ^ {T} f (t) \mathrm {e} ^ {t} \mathrm {d} t + \int_ {T} ^ {x + T} f (t) \mathrm {e} ^ {t} \mathrm {d} t + C \right] \\ \underline {{= u = t - T}} \mathrm {e} ^ {- x - T} \left[ \int_ {0} ^ {T} f (t) \mathrm {e} ^ {t} \mathrm {d} t + \int_ {0} ^ {x} f (u + T) \mathrm {e} ^ {u + T} \mathrm {d} u + C \right] \\ \underline {{= \frac {f (u + T) = f (u)}{2}}} \mathrm {e} ^ {- x - T} \left[ \int_ {0} ^ {T} f (t) \mathrm {e} ^ {t} \mathrm {d} t + \mathrm {e} ^ {T} \int_ {0} ^ {x} f (u) \mathrm {e} ^ {u} \mathrm {d} u + C \right] \\ &= \mathrm {e} ^ {- x} \left[ \mathrm {e} ^ {- T} \int_ {0} ^ {T} f (t) \mathrm {e} ^ {t} \mathrm {d} t + \int_ {0} ^ {x} f (u) \mathrm {e} ^ {u} \mathrm {d} u + C \mathrm {e} ^ {- T} \right]. \end{aligned}</equation>比较 y(x)与 y(x+T).若<equation>\mathrm{e}^{-x}\left[ \mathrm{e}^{-T}\int_{0}^{T}f(t)\mathrm{e}^{t}\mathrm{d}t+\int_{0}^{x}f(u)\mathrm{e}^{u}\mathrm{d}u+C\mathrm{e}^{-T}\right]=\mathrm{e}^{-x}\left[ \int_{0}^{x}f(t)\mathrm{e}^{t}\mathrm{d}t+C\right]</equation>即<equation>\mathrm {e} ^ {- T} \int_ {0} ^ {T} f (t) \mathrm {e} ^ {t} \mathrm {d} t + G \mathrm {e} ^ {- T} = C,</equation>则<equation>y ( x+T)=y ( x ), y ( x )</equation>是以T为周期的解.解（1）式得<equation>C=\frac{\int_{0}^{T} f ( t ) \mathrm{e}^{t} \mathrm{d} t}{\mathrm{e}^{T}-1}.</equation>由于T为一常数，故C为一确定常数.

因此，若<equation>f(x)</equation>是周期为<equation>T</equation>的函数，则方程<equation>y^{\prime} + y = f(x)</equation>存在以<equation>T</equation>为周期的解.

下面证明方程<equation>y^{\prime} + y = f(x)</equation>的以<equation>T</equation>为周期的解唯一.

假设<equation>y_{1}, y_{2}</equation>是方程<equation>y^{\prime} + y = f(x)</equation>的两个不同的以<equation>T</equation>为周期的解，则<equation>y_{1} - y_{2}</equation>为齐次线性微分方程<equation>y^{\prime} + y = 0</equation>的解，且<equation>y_{1} - y_{2}</equation>也是以<equation>T</equation>为周期的函数. 解<equation>y^{\prime} + y = 0</equation>可得<equation>y = C_{0}\mathrm{e}^{-x}</equation>，其中<equation>C_{0}</equation>为任意常数. 于是，<equation>y_{1} - y_{2} = C_{0}\mathrm{e}^{-x}</equation>，但是该函数不是以<equation>T</equation>为周期的函数. 矛盾.

综上所述，若<equation>f ( x )</equation>是周期为<equation>T</equation>的函数，则方程<equation>y^{\prime}+y=f ( x )</equation>存在唯一的以<equation>T</equation>为周期的解.

---

**2016年第3题 | 选择题 | 4分 | 答案: A**
3. 若<equation>y=(1+x^{2})^{2}-\sqrt{1+x^{2}},</equation><equation>y=(1+x^{2})^{2}+\sqrt{1+x^{2}}</equation>是微分方程<equation>y^{\prime}+p(x)y=q(x)</equation>的两个解，则 q(x) =（    )

A.<equation>3 x(1+x^{2})</equation>B.<equation>- 3 x(1+x^{2})</equation>C.<equation>\frac{x}{1+x^{2}}</equation>D.<equation>- \frac{x}{1+x^{2}}</equation>
答案: A
**解析: **解 令<equation>y_{1}=(1+x^{2})^{2}-\sqrt{1+x^{2}}, y_{2}=(1+x^{2})^{2}+\sqrt{1+x^{2}}.</equation>由于<equation>y_{1}, y_{2}</equation>均是微分方程<equation>y^{\prime}+p(x)y=q(x)</equation>的解，故<equation>y_{2}-y_{1}=2\sqrt{1+x^{2}}</equation>是对应的齐次线性方程<equation>y^{\prime}+p(x)y=0</equation>的解.将解代入方程中得到<equation>\frac {2 x}{\sqrt {1 + x ^ {2}}} + 2 p (x) \sqrt {1 + x ^ {2}} = 0,</equation>从而<equation>p ( x ) = - \frac { x } { 1 + x ^ { 2 } } .</equation>由于<equation>y_{1}, y_{2}</equation>是微分方程<equation>y^{\prime}+p(x)y=q(x)</equation>的解，故<equation>\frac{y_{1}+y_{2}}{2}=(1+x^{2})^{2}</equation>也是该微分方程的解.将解代入方程中得到<equation>4 x \left(1 + x ^ {2}\right) - \frac {x}{1 + x ^ {2}} \cdot \left(1 + x ^ {2}\right) ^ {2} = q (x),</equation>即<equation>q ( x ) = 3 x \left( 1+x^{2} \right).</equation>应选A.

---

**2011年第10题 | 填空题 | 4分**
10. 微分方程<equation>y' + y = \mathrm{e}^{-x}\cos x</equation>满足条件<equation>y(0) = 0</equation>的解为<equation>y = \underline{\quad}</equation>
**解析: **利用求解公式可得，<equation>y=\mathrm{e}^{-\int\mathrm{d} x}\left(\int\mathrm{e}^{-x}\cos x\mathrm{e}^{\int\mathrm{d} x}\mathrm{d} x+C\right)=\mathrm{e}^{-x}\left(\int\cos x\mathrm{d} x+C\right)=\mathrm{e}^{-x}(\sin x+C).</equation>将 y(0) = 0 代入上式得到 C = 0，于是所求解为 y =<equation>\mathrm{e}^{-x}\sin x.</equation>

---


#### 其他方程

**2024年第14题 | 填空题 | 5分**

14. 微分方程<equation>y^{\prime}=\frac{1}{(x+y)^{2}}</equation>满足条件 y(1)=0的解为 ___

**答案:**<equation>\arctan (x + y) = y + \frac {\pi}{4}</equation>

**解析:**解 令<equation>u=x+y</equation>，则<equation>\frac{\mathrm{d}u}{\mathrm{d}x}=1+\frac{\mathrm{d}y}{\mathrm{d}x}</equation>，原方程化为<equation>\frac{\mathrm{d}u}{\mathrm{d}x}-1=\frac{1}{u^{2}}</equation>，即<equation>\frac{\mathrm{d}u}{\mathrm{d}x}=\frac{1+u^{2}}{u^{2}}.</equation>这是一个可分离变量的微分方程，分离变量可得<equation>\left(1-\frac{1}{1+u^{2}}\right)\mathrm{d}u=\mathrm{d}x.</equation>方程两端同时积分可得<equation>u-\arctan u=x+C.</equation>由<equation>y(1)=0</equation>可得，<equation>u(1)=1.</equation>代入<equation>u-\arctan u=x+C</equation>可得<equation>1-\frac{\pi}{4}=1+C,</equation>解得<equation>C=-\frac{\pi}{4}.</equation>于是，<equation>u-\arctan u=x-\frac{\pi}{4}.</equation>将<equation>u=x+y</equation>代回<equation>u-\arctan u=x-\frac{\pi}{4}</equation>并整理可得<equation>y-\arctan(x+y)+\frac{\pi}{4}=0.</equation>

---

**2021年第13题 | 填空题 | 5分**

13. 欧拉方程<equation>x^{2} y^{\prime \prime}+x y^{\prime}-4 y=0</equation>满足条件<equation>y(1)=1, y^{\prime}(1)=2</equation>的解为<equation>y=</equation>___.

**答案:**<equation>x^{2}.</equation>

**解析:**解 由初始条件<equation>y ( 1 ) = 1, y^{\prime} ( 1 ) = 2</equation>可知应在<equation>x > 0</equation>的范围内求解.

令<equation>x = \mathrm{e}^{t}</equation>. 于是，<equation>\frac {\mathrm {d} y}{\mathrm {d} t} = \frac {\mathrm {d} y}{\mathrm {d} x} \cdot \mathrm {e} ^ {t}.</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} t ^ {2}} = \frac {\mathrm {d} \left(\frac {\mathrm {d} y}{\mathrm {d} x} \cdot \mathrm {e} ^ {t}\right)}{\mathrm {d} t} = \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \cdot \frac {\mathrm {d} x}{\mathrm {d} t} \cdot \mathrm {e} ^ {t} + \frac {\mathrm {d} y}{\mathrm {d} x} \cdot \mathrm {e} ^ {t} = \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \cdot \mathrm {e} ^ {2 t} + \frac {\mathrm {d} y}{\mathrm {d} x} \cdot \mathrm {e} ^ {t} = \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \cdot \mathrm {e} ^ {2 t} + \frac {\mathrm {d} y}{\mathrm {d} t}.</equation>从而，<equation>y^{\prime} = \mathrm{e}^{-t}\frac{\mathrm{d}y}{\mathrm{d}t}, y^{\prime \prime} = \mathrm{e}^{-2t}\left(\frac{\mathrm{d}^{2}y}{\mathrm{d}t^{2}} - \frac{\mathrm{d}y}{\mathrm{d}t}\right).</equation>因此，<equation>xy^{\prime} = \frac{\mathrm{d}y}{\mathrm{d}t}, x^{2}y^{\prime \prime} = \frac{\mathrm{d}^{2}y}{\mathrm{d}t^{2}} - \frac{\mathrm{d}y}{\mathrm{d}t}.</equation>代入<equation>x^{2} y^{\prime \prime}+x y^{\prime}-4 y=0</equation>可得<equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} t ^ {2}} - \frac {\mathrm {d} y}{\mathrm {d} t} + \frac {\mathrm {d} y}{\mathrm {d} t} - 4 y = \frac {\mathrm {d} ^ {2} y}{\mathrm {d} t ^ {2}} - 4 y = 0.</equation><equation>\frac{\mathrm{d}^2y}{\mathrm{d}t^2} - 4y = 0</equation>是一个二阶常系数齐次线性微分方程，其特征方程为<equation>r^2 - 4 = 0</equation>，特征根为<equation>r_{1,2} = \pm 2.</equation>于是，该方程的解为<equation>y = C_{1}\mathrm{e}^{2t} + C_{2}\mathrm{e}^{-2t} = C_{1}x^{2} + C_{2}x^{-2}</equation>，其中<equation>C_{1},C_{2}</equation>为待定常数. 从而，<equation>y^{\prime} = 2C_{1}x - 2C_{2}x^{-3}.</equation>代入 y（1）=1可得<equation>1=C_{1}+C_{2}</equation>代入<equation>y^{\prime}(1)=2</equation>可得<equation>2=2 C_{1}-2 C_{2}</equation>解得<equation>C_{1}=1,C_{2}=0.</equation>综上所述，原方程的解为<equation>y=x^{2}.</equation>

---


#### 常系数齐次线性微分方程

**2023年第2题 | 选择题 | 5分 | 答案: C**

2. 若微分方程<equation>y^{\prime \prime}+ay^{\prime}+by=0</equation>的解在<equation>(-\infty,+\infty)</equation>上有界，则（    )

A. a < 0,b > 0 B. a > 0,b > 0 C. a = 0,b > 0 D. a = 0,b < 0

答案: C

**解析:**解 由于二阶常系数齐次线性微分方程必有零解，而零解为有界解，故微分方程<equation>y^{\prime \prime}+ay^{\prime}+by=0</equation>必然存在<equation>(-\infty , +\infty)</equation>上的有界解.本题实际上是要求此方程的所有解都有界.

微分方程<equation>y^{\prime \prime} + a y^{\prime} + b y = 0</equation>的特征方程为<equation>\lambda^{2} + a \lambda + b = 0.</equation>- 若<equation>\Delta=a^{2}-4 b>0</equation>，则特征方程有两个不同实根<equation>\lambda_{1},\lambda_{2}</equation>，从而至少有一个实根非零.此时，微分方程的解为<equation>y=C_{1}\mathrm{e}^{\lambda_{1}x}+C_{2}\mathrm{e}^{\lambda_{2}x}.</equation>取<equation>C_{1} = C_{2} = 1</equation>，则<equation>\lim_{x\to -\infty}\left(\mathrm{e}^{\lambda_{1}x} + \mathrm{e}^{\lambda_{2}x}\right) = +\infty</equation>或<equation>\lim_{x\to +\infty}\left(\mathrm{e}^{\lambda_{1}x} + \mathrm{e}^{\lambda_{2}x}\right) = +\infty</equation>. 该解在<equation>(-\infty , +\infty)</equation>上无界.

- 若<equation>\Delta=a^{2}-4 b=0</equation>，则特征方程有两个相同实根<equation>\lambda</equation>.此时，微分方程的解为<equation>y=(C_{1}+ C_{2} x) \mathrm{e}^{\lambda x}.</equation>取<equation>C_{1} = 0, C_{2} = 1</equation>，则<equation>\lim_{x\to -\infty}x\mathrm{e}^{\lambda x} = \infty</equation>或<equation>\lim_{x\to +\infty}x\mathrm{e}^{\lambda x} = \infty</equation>. 该解在<equation>(-\infty , +\infty)</equation>上无界.

- 若<equation>\Delta=a^{2}-4 b<0</equation>，则特征方程有一对共轭复根<equation>\lambda_{1,2}=\alpha\pm\beta\mathrm{i}</equation>.此时，微分方程的解为<equation>y=\mathrm{e}^{\alpha x}\left(C_{1}\cos \beta x+C_{2}\sin \beta x\right).</equation>当<equation>\alpha \neq 0</equation>时，取<equation>C_{1} = 1, C_{2} = 0</equation>，所得解<equation>y = \mathrm{e}^{\alpha x}\cos \beta x</equation>是<equation>(-\infty , + \infty)</equation>上的无界函数.

当<equation>\alpha=0</equation>时，微分方程的解为<equation>y=C_{1}\cos \beta x+C_{2}\sin \beta x</equation>.对任意常数<equation>C_{1},C_{2}</equation>，该解在<equation>(-\infty, +\infty)</equation>上均有界.根据求根公式，<equation>\lambda_{1,2}=-\frac{a}{2}\pm \frac{\sqrt{4b-a^{2}}}{2}\mathrm{i}</equation>，即<equation>\alpha=-\frac{a}{2}.</equation>于是，<equation>a=0.</equation>结合<equation>a^{2}-4b<0</equation>可知，<equation>b>0.</equation>因此，<equation>a=0,b>0.</equation>应选C.

---

**2020年第11题 | 填空题 | 4分**

11. 设函数 f(x)满足<equation>f^{\prime\prime}(x)+af^{\prime}(x)+f(x)=0(a>0)</equation>，且 f(0)=m，<equation>f^{\prime}(0)=n</equation>，则<equation>\int_{0}^{+\infty}f(x)\mathrm{d}x=</equation>___

**答案:**## n+am.

**解析:**解 原方程的特征方程为<equation>r^{2}+ar+1=0</equation>. 该方程的判别式<equation>\Delta=a^{2}-4</equation>. 下面根据 a 的取值讨论解的情况.<equation>\textcircled{1}</equation>a > 2.<equation>r^{2}+ar+1=0</equation>有两个不同实根<equation>r_{1,2}=\frac{-a\pm \sqrt{a^{2}-4}}{2}, r_{1}, r_{2}</equation>均小于零. 原方程的解为<equation>f(x)=</equation><equation>C_{1}\mathrm{e}^{r_{1}x}+C_{2}\mathrm{e}^{r_{2}x}</equation>，其中<equation>C_{1},C_{2}</equation>为待定常数.<equation>f^{\prime}(x)=C_{1}r_{1}\mathrm{e}^{r_{1}x}+C_{2}r_{2}\mathrm{e}^{r_{2}x}.</equation><equation>\textcircled{2}</equation>a=2.<equation>r^{2}+2 r+1=0</equation>有两个相同实根<equation>r_{1,2}=-1</equation>. 原方程的解为<equation>f(x)=\left(C_{1}+C_{2}x\right)\mathrm{e}^{-x}</equation>，其中<equation>C_{1},C_{2}</equation>为待定常数.<equation>f^{\prime}(x)=\left(C_{2}-C_{1}-C_{2}x\right)\mathrm{e}^{-x}.</equation><equation>\textcircled{3}</equation>0 < a < 2.<equation>r^{2}+ar+1=0</equation>有一对共轭复根<equation>r_{1,2}=-\frac{a}{2}\pm b\mathrm{i}</equation>，其中<equation>b=\frac{\sqrt{4-a^{2}}}{2}</equation>原方程的解为<equation>f(x)=</equation><equation>\mathrm{e}^{-\frac{a}{2}x}\left(C_{1}\cos bx+C_{2}\sin bx\right)</equation>，其中<equation>C_{1},C_{2}</equation>为待定常数.<equation>f^{\prime}(x)</equation>的形式与f(x)的形式相同.

不论是哪种情况，由<equation>a > 0</equation>均可得<equation>\lim_{x\to +\infty}f(x) = 0,\lim_{x\to +\infty}f^{\prime}(x) = 0.</equation>由<equation>f^{\prime \prime}(x) + af^{\prime}(x) + f(x) = 0</equation>可得，<equation>f(x) = -f^{\prime \prime}(x) - af^{\prime}(x)</equation>. 因此，<equation>\begin{aligned} \int_ {0} ^ {+ \infty} f (x) \mathrm {d} x &= \int_ {0} ^ {+ \infty} \left[ - f ^ {\prime \prime} (x) - a f ^ {\prime} (x) \right] \mathrm {d} x = \left[ - f ^ {\prime} (x) - a f (x) \right] \Bigg | _ {0} ^ {+ \infty} \\ &= \lim _ {x \rightarrow + \infty} \left[ - f ^ {\prime} (x) - a f (x) \right] - \left[ - f ^ {\prime} (0) - a f (0) \right] \\ &= f ^ {\prime} (0) + a f (0) = n + a m. \end{aligned}</equation>

---

**2017年第10题 | 填空题 | 4分**

10. 微分方程<equation>y'' + 2y' + 3y = 0</equation>的通解为<equation>y = \_\_\_</equation>

**答案:**<equation>\mathrm{e}^{-x}\left(C_1\cos \sqrt{2} x + C_2\sin \sqrt{2} x\right)</equation>，其中<equation>C_{1}, C_{2}</equation>为任意常数.

**解析:**解 原方程的特征方程为<equation>\lambda^{2}+2\lambda+3=0</equation>，解得<equation>\lambda_{1,2}=-1\pm \sqrt{2}\mathrm{i}</equation>，于是所求通解为<equation>y=\mathrm{e}^{-x}\left(C_{1}\cos \sqrt{2} x+C_{2}\sin \sqrt{2} x\right)</equation>其中<equation>C_{1}, C_{2}</equation>为任意常数.

---

**2016年第16题 | 解答题 | 10分**

16. (本题满分10分)

设函数 y(x)满足方程<equation>y^{\prime\prime}+2 y^{\prime}+k y=0</equation>，其中 0 < k < 1.

I. 证明：反常积分<equation>\int_{0}^{+\infty} y(x)\mathrm{d}x</equation>收敛；

II. 若 y(0)=1，<equation>y^{\prime}(0)=1</equation>，求<equation>\int_{0}^{+\infty} y(x)\mathrm{d}x</equation>的值.

**答案:**（ I ）证明略. （ II ）<equation>\frac{3}{k}</equation>

**解析:**解（I）原方程的特征方程为<equation>\lambda^{2}+2\lambda+k=0</equation>.由于<equation>0 < k < 1</equation>，故<equation>\Delta = 4 - 4 k > 0</equation>，从而解得<equation>\lambda_{1,2}=-1\pm \sqrt{1-k}<0</equation>.于是<equation>y (x) = C _ {1} \mathrm {e} ^ {\lambda_ {1} x} + C _ {2} \mathrm {e} ^ {\lambda_ {2} x},</equation><equation>\begin{aligned} \int_ {0} ^ {+ \infty} y (x) \mathrm {d} x &= \int_ {0} ^ {+ \infty} \left(C _ {1} \mathrm {e} ^ {\lambda_ {1} x} + C _ {2} \mathrm {e} ^ {\lambda_ {2} x}\right) \mathrm {d} x = \left. \left(\frac {C _ {1}}{\lambda_ {1}} \mathrm {e} ^ {\lambda_ {1} x} + \frac {C _ {2}}{\lambda_ {2}} \mathrm {e} ^ {\lambda_ {2} x}\right) \right| _ {0} ^ {+ \infty} \\ &= 0 - \frac {C _ {1}}{\lambda_ {1}} + 0 - \frac {C _ {2}}{\lambda_ {2}} = - \left(\frac {C _ {1}}{\lambda_ {1}} + \frac {C _ {2}}{\lambda_ {2}}\right). \end{aligned}</equation>因此，<equation>\int_{0}^{+\infty} y ( x ) \mathrm{d} x</equation>收敛，结论得证.

（Ⅱ）（法一）由<equation>y^{\prime \prime}+2y^{\prime}+ky=0</equation>可得，<equation>\begin{array}{l} \int_ {0} ^ {+ \infty} y (x) \mathrm {d} x = \int_ {0} ^ {+ \infty} \frac {- \left[ y ^ {\prime \prime} (x) + 2 y ^ {\prime} (x) \right]}{k} \mathrm {d} x = - \frac {1}{k} \left[ y ^ {\prime} (x) + 2 y (x) \right] \Bigg | _ {0} ^ {+ \infty} \\ = - \frac {1}{k} \left\{\lim _ {x \rightarrow + \infty} \left[ y ^ {\prime} (x) + 2 y (x) \right] - \left[ y ^ {\prime} (0) + 2 y (0) \right]\right\}. \\ \end{array}</equation>由第（Ⅰ）问知，<equation>\lim _ {x \rightarrow + \infty} y (x) = \lim _ {x \rightarrow + \infty} \left(C _ {1} \mathrm {e} ^ {\lambda_ {1} x} + C _ {2} \mathrm {e} ^ {\lambda_ {2} x}\right) = 0,</equation><equation>\lim _ {x \rightarrow + \infty} y ^ {\prime} (x) = \lim _ {x \rightarrow + \infty} \left(C _ {1} \lambda_ {1} \mathrm {e} ^ {\lambda_ {1} x} + C _ {2} \lambda_ {2} \mathrm {e} ^ {\lambda_ {2} x}\right) = 0.</equation>代入<equation>y (0) = 1, y^{\prime} (0) = 1</equation>，可得<equation>\int_0^{+\infty} y (x)\mathrm{d}x = -\frac{1}{k} (0 - 1 - 2) = \frac{3}{k}.</equation>（法二）由<equation>y(x) = C_{1}\mathrm{e}^{\lambda_{1}x} + C_{2}\mathrm{e}^{\lambda_{2}x}</equation>知，<equation>y ^ {\prime} (x) = C _ {1} \lambda_ {1} \mathrm {e} ^ {\lambda_ {1} x} + C _ {2} \lambda_ {2} \mathrm {e} ^ {\lambda_ {2} x}.</equation>将<equation>y(0) = 1, y^{\prime}(0) = 1</equation>代入<equation>y(x)</equation>与<equation>y^{\prime}(x)</equation>的表达式中，得到<equation>\left\{ \begin{array}{l} C _ {1} + C _ {2} = 1, \\ C _ {1} \lambda_ {1} + C _ {2} \lambda_ {2} = 1. \end{array} \right.</equation>将<equation>C_{2} = 1 - C_{1}</equation>代入<equation>C_{1}\lambda_{1} + C_{2}\lambda_{2} = 1</equation>，解得<equation>C_{1} = \frac{1 - \lambda_{2}}{\lambda_{1} - \lambda_{2}}</equation>，从而<equation>C_{2} = 1 - C_{1} = \frac{\lambda_{1} - \lambda_{2} - 1 + \lambda_{2}}{\lambda_{1} - \lambda_{2}} = \frac{\lambda_{1} - 1}{\lambda_{1} - \lambda_{2}}</equation>.于是，<equation>\begin{aligned} \int_ {0} ^ {+ \infty} y (x) \mathrm {d} x &= - \frac {C _ {1}}{\lambda_ {1}} - \frac {C _ {2}}{\lambda_ {2}} = \frac {\lambda_ {2} - 1}{\lambda_ {1} - \lambda_ {2}} \cdot \frac {1}{\lambda_ {1}} + \frac {1 - \lambda_ {1}}{\lambda_ {1} - \lambda_ {2}} \cdot \frac {1}{\lambda_ {2}} = \frac {\left(\lambda_ {2} - 1\right) \lambda_ {2} + \left(1 - \lambda_ {1}\right) \lambda_ {1}}{\lambda_ {1} \lambda_ {2} \left(\lambda_ {1} - \lambda_ {2}\right)} \\ &= \frac {\lambda_ {2} ^ {2} - \lambda_ {1} ^ {2} + \lambda_ {1} - \lambda_ {2}}{\lambda_ {1} \lambda_ {2} \left(\lambda_ {1} - \lambda_ {2}\right)} = \frac {1 - \left(\lambda_ {1} + \lambda_ {2}\right)}{\lambda_ {1} \lambda_ {2}}. \end{aligned}</equation>由于<equation>\lambda_{1},\lambda_{2}</equation>为特征方程<equation>\lambda^{2} + 2\lambda +k = 0</equation>的两个根，故<equation>\lambda_{1} + \lambda_{2} = -2,\lambda_{1}\lambda_{2} = k.</equation>因此，<equation>\int_0^{+\infty}y(x)\mathrm{d}x = \frac{1 - (-2)}{k} = \frac{3}{k}</equation>.

---

**2012年第9题 | 填空题 | 4分**

9. 若函数<equation>f(x)</equation>满足方程<equation>f^{\prime\prime}(x)+f^{\prime}(x)-2f(x)=0</equation>及<equation>f^{\prime\prime}(x)+f(x)=2\mathrm{e}^{x}</equation>，则<equation>f(x)=</equation>___.

**解析:**解（法一）由题设知，<equation>f(x)</equation>满足二阶常系数齐次线性微分方程<equation>y^{\prime \prime}+y^{\prime}-2y=0.</equation>其特征方程为<equation>\lambda^{2}+\lambda-2=0</equation>，解得<equation>\lambda_{1}=1,\lambda_{2}=-2</equation>，于是<equation>f(x)=C_{1}\mathrm{e}^{x}+C_{2}\mathrm{e}^{-2x}</equation>其中<equation>C_{1},C_{2}</equation>为待定常数.将<equation>f(x)</equation>的表达式代入<equation>f^{\prime \prime}(x)+f(x)=2\mathrm{e}^{x}</equation>中，得到<equation>C _ {1} \mathrm {e} ^ {x} + 4 C _ {2} \mathrm {e} ^ {- 2 x} + C _ {1} \mathrm {e} ^ {x} + C _ {2} \mathrm {e} ^ {- 2 x} = 2 \mathrm {e} ^ {x}.</equation>化简得<equation>2 C _ {1} \mathrm {e} ^ {x} + 5 C _ {2} \mathrm {e} ^ {- 2 x} = 2 \mathrm {e} ^ {x}.</equation>于是<equation>2C_{1} = 2,5C_{2} = 0</equation>，从而<equation>C_{1} = 1,C_{2} = 0.</equation>故<equation>f(x) = \mathrm{e}^{x}.</equation>（法二）由<equation>\left\{ \begin{array}{l} f^{\prime \prime}(x) + f^{\prime}(x) - 2f(x) = 0, \\ f^{\prime \prime}(x) + f(x) = 2\mathrm{e}^{x} \end{array} \right.</equation>得到<equation>f^{\prime}(x) - 3f(x) = -2\mathrm{e}^{x}</equation>. 由一阶非齐次线性微分方程的求解公式知，<equation>f (x) = \mathrm {e} ^ {\int 3 \mathrm {d} x} \left[ \int (- 2 \mathrm {e} ^ {x}) \mathrm {e} ^ {- \int 3 \mathrm {d} x} \mathrm {d} x + C \right] = \mathrm {e} ^ {3 x} \left(\mathrm {e} ^ {- 2 x} + C\right) = \mathrm {e} ^ {x} + C \mathrm {e} ^ {3 x}, C \text {为待 定 常 数}.</equation>将<equation>f ( x )</equation>的表达式代入<equation>f^{\prime \prime} ( x )+f^{\prime} ( x )-2 f ( x )=0</equation>中，得到<equation>1 0 C \mathrm{e}^{3 x}=0</equation>即有<equation>C=0</equation>（或者将<equation>f ( x )</equation>的表达式代入<equation>f^{\prime \prime} ( x )+f ( x )=2 \mathrm{e}^{x}</equation>中，同样可得<equation>C=0 )</equation>.于是<equation>f (x) = \mathrm {e} ^ {x}.</equation>

---


#### 微分方程的应用

**2023年第17题 | 解答题 | 10分**

17. (本题满分10分)

设曲线<equation>y=y(x)(x>0)</equation>经过点(1,2)，该曲线上任一点 P(x,y)到 y轴的距离等于该点处的切线在 y轴上的截距.

I. 求 y(x);

II. 求函数<equation>f(x)=\int_{1}^{x} y(t)\mathrm{d} t</equation>在（0，+∞）上的最大值.

**答案:**<equation>\begin{array}{l} (\mathrm {I}) y (x) = x (2 - \ln x); \\ (\mathrm {I I}) \frac {1}{4} \mathrm {e} ^ {4} - \frac {5}{4}. \\ \end{array}</equation>

**解析:**解（I）由导数的几何意义可知，点<equation>P(x,y)</equation>处的切线方程为<equation>Y-y=y^{\prime}(X-x).</equation>该点到y轴的距离为<equation>|x|\overset{x>0}{=}x.</equation>令<equation>X=0</equation>，可得<equation>Y=y-xy^{\prime}</equation>.由点<equation>P(x,y)</equation>到y轴的距离等于该点处的切线在y轴上的截距可得<equation>x=y-xy^{\prime}</equation>.整理可得<equation>y^{\prime}-\frac{y}{x}=-1</equation>.由一阶非齐次线性微分方程的通解公式可得<equation>\begin{aligned} y &= \mathrm {e} ^ {\int \frac {1}{x} \mathrm {d} x} \left[ \int (- 1) \mathrm {e} ^ {- \int \frac {1}{x} \mathrm {d} x} \mathrm {d} x + C \right] = \mathrm {e} ^ {\ln x} \left(- \int \mathrm {e} ^ {- \ln x} \mathrm {d} x + C\right) \\ &= x \left(- \int \frac {1}{x} \mathrm {d} x + C\right) = x (C - \ln x). \end{aligned}</equation>代入<equation>x = 1, y = 2</equation>可得<equation>C = 2</equation>. 因此，<equation>y(x) = x(2 - \ln x)</equation>.

（Ⅱ）由第（I）问的结果可知，<equation>f ( x ) = \int_{1}^{x} t ( 2 - \ln t ) \mathrm{d} t.</equation>由变限积分的求导公式可得<equation>f^{\prime}(x) = x(2 - \ln x)</equation>. 解<equation>2 - \ln x = 0</equation>可得<equation>x = \mathrm{e}^{2}</equation>. 于是，<equation>x = \mathrm{e}^{2}</equation>为<equation>f(x)</equation>在<equation>(0, + \infty)</equation>上的唯一驻点.当<equation>0 < x < \mathrm{e}^{2}</equation>时，<equation>f^{\prime}(x) > 0</equation>，<equation>f(x)</equation>单调增加；当<equation>x > \mathrm{e}^{2}</equation>时，<equation>f^{\prime}(x) < 0</equation>，<equation>f(x)</equation>单调减少.<equation>x = \mathrm{e}^{2}</equation>为<equation>f(x)</equation>在<equation>(0, + \infty)</equation>上的最大值点，最大值为<equation>\begin{aligned} f \left(\mathrm {e} ^ {2}\right) &= \int_ {1} ^ {\mathrm {e} ^ {2}} t (2 - \ln t) \mathrm {d} t = \frac {1}{2} \int_ {1} ^ {\mathrm {e} ^ {2}} (2 - \ln t) \mathrm {d} \left(t ^ {2}\right) = \frac {1}{2} t ^ {2} (2 - \ln t) \left| _ {1} ^ {\mathrm {e} ^ {2}} - \frac {1}{2} \int_ {1} ^ {\mathrm {e} ^ {2}} t ^ {2} \cdot \left(- \frac {1}{t}\right) \mathrm {d} t \right. \\ &= 0 - 1 + \frac {1}{2} \int_ {1} ^ {\mathrm {e} ^ {2}} t \mathrm {d} t = - 1 + \frac {1}{4} t ^ {2} \Bigg | _ {1} ^ {\mathrm {e} ^ {2}} = \frac {1}{4} \mathrm {e} ^ {4} - \frac {5}{4}. \end{aligned}</equation>

---

**2015年第16题 | 解答题 | 10分**

16. (本题满分10分)

设函数 f(x)在定义域 I上的导数大于零.若对任意的<equation>x_{0}\in I</equation>，曲线 y=f(x)在点<equation>\left(x_{0},f\left(x_{0}\right)\right)</equation>处的切线与直线<equation>x=x_{0}</equation>及 x轴所围成区域的面积恒为4，且 f(0)=2，求 f(x)的表达式.

**答案:**<equation>1 6) f (x) = \frac {8}{4 - x}, x \in I.</equation>

**解析:**解如图所示，曲线<equation>y=f(x)</equation>在点<equation>\left(x_{0},f\left(x_{0}\right)\right)</equation>处的切线为<equation>y - f \left(x _ {0}\right) = f ^ {\prime} \left(x _ {0}\right) \left(x - x _ {0}\right).</equation>令<equation>y = 0</equation>，注意到<equation>f^{\prime}(x) > 0</equation>，解得<equation>x = x_{0} - \frac{f(x_{0})}{f^{\prime}(x_{0})}</equation>，即该切线与<equation>x</equation>轴的交点为<equation>\left(x_0 - \frac{f(x_0)}{f^{\prime}(x_0)},0\right)</equation>.

曲线<equation>y=f(x)</equation>在点<equation>\left(x_{0},f\left(x_{0}\right)\right)</equation>处的切线与直线<equation>x=x_{0}</equation>及x轴所围成区域为三角形，底边长<equation>\left|x_{0}-\left[x_{0}-\frac{f\left(x_{0}\right)}{f^{\prime}\left(x_{0}\right)}\right]\right|</equation>，高<equation>|f(x_{0})-0|</equation>.于是，<equation>\frac {\left| f \left(x _ {0}\right) - 0 \right| \cdot \left| x _ {0} - \left[ x _ {0} - \frac {f \left(x _ {0}\right)}{f ^ {\prime} \left(x _ {0}\right)} \right] \right|}{2} = 4, \quad \text {即} \frac {\left| f \left(x _ {0}\right) \right| \cdot \left| \frac {f \left(x _ {0}\right)}{f ^ {\prime} \left(x _ {0}\right)} \right|}{2} = 4.</equation>由于<equation>f^{\prime}(x) > 0</equation>，故<equation>\frac {\left[ f \left(x _ {0}\right) \right] ^ {2}}{f ^ {\prime} \left(x _ {0}\right)} = 8, \quad x _ {0} \in I,</equation>即<equation>f(x)</equation>满足微分方程<equation>8y^{\prime} = y^{2}</equation>.

分离变量，得<equation>\frac{8}{y^{2}}\mathrm{d}y=\mathrm{d}x.</equation>方程两端积分，得<equation>-\frac{8}{y}=x+C</equation>其中C为待定常数.由于<equation>f(0)=2</equation>故C=-4，从而<equation>y=\frac{8}{4-x}.</equation>因此，<equation>f (x) = \frac {8}{4 - x}, \quad x \in I.</equation>

---


#### 可分离变量的微分方程与齐次方程

**2019年第10题 | 填空题 | 4分**

10. 微分方程<equation>2 y y^{\prime}-y^{2}-2=0</equation>满足条件<equation>y(0)=1</equation>的特解<equation>y=</equation>___

**解析:**解 整理原方程可得<equation>2 y \frac{\mathrm{d} y}{\mathrm{d} x}=y^{2}+2.</equation>分离变量可得<equation>\frac{2 y}{y^{2}+2}\mathrm{d} y=\mathrm{d} x.</equation>方程两端积分，<equation>\int \frac{2 y}{y^{2}+2}\mathrm{d} y=\int \frac{\mathrm{d}\left(y^{2}+2\right)}{y^{2}+2}=\ln \left(y^{2}+2\right)=x+C,</equation>其中 C为待定常数.

代入 x=0，<equation>y(0)=1</equation>可得，<equation>C=\ln 3</equation>.于是，<equation>y^{2}+2=3\mathrm{e}^{x}.</equation>又因为<equation>y(0)=1>0</equation>，所以<equation>y=\sqrt{3\mathrm{e}^{x}-2}.</equation>

---

**2014年第11题 | 填空题 | 4分**

11. 微分方程<equation>x y^{\prime}+y(\ln x-\ln y)=0</equation>满足条件<equation>y(1)=\mathrm{e}^{3}</equation>的解为<equation>y=</equation>___.

**答案:**##<equation>x \mathrm{e}^{2 x+1}.</equation>

**解析:**解 由题设中微分方程的表达式知 x > 0，y > 0，且原方程可化为<equation>y ^ {\prime} = \frac {y}{x} \ln \frac {y}{x},</equation>此为齐次方程. 令<equation>u=\frac{y}{x}</equation>，则<equation>y=ux,\frac{\mathrm{d}y}{\mathrm{d}x}=u+x\frac{\mathrm{d}u}{\mathrm{d}x}</equation>，于是方程（1）化为<equation>u + x \frac {\mathrm {d} u}{\mathrm {d} x} = u \ln u.</equation>分离变量，得到<equation>\frac {\mathrm {d} u}{u (\ln u - 1)} = \frac {\mathrm {d} x}{x},</equation>即<equation>\frac {\mathrm {d} (\ln u - 1)}{\ln u - 1} = \frac {\mathrm {d} x}{x}.</equation>对上式两端积分，得到于是<equation>\begin{aligned} \ln | \ln u - 1 | &= \ln x + C _ {1}, \\ \ln u - 1 &= C x, \end{aligned}</equation>其中<equation>C = \pm \mathrm{e}^{C_1}</equation>. 代回原变量<equation>u = \frac{y}{x}</equation>，得到原方程的通解为

注意这里由于 x > 0，y > 0，故 u > 0从而<equation>\int \frac{1}{u}=\ln u+C</equation>，但由于<equation>\ln u-1</equation>的正负无法判断，故<equation>\int \frac {\mathrm {d} (\ln u - 1)}{\ln u - 1} = \ln | \ln u - 1 | + C.</equation><equation>\ln \frac {y}{x} - 1 = C x.</equation>将<equation>y ( 1 ) = \mathrm{e}^{3}</equation>代入上式，得到<equation>C=2</equation>，于是<equation>\ln \frac{y}{x}=2x+1</equation>，从而所求初值问题的解为<equation>y = x \mathrm {e} ^ {2 x + 1}.</equation>

---


#### 常系数非齐次线性微分方程

**2015年第2题 | 选择题 | 4分 | 答案: A**

2. 设<equation>y=\frac{1}{2}\mathrm{e}^{2 x}+\left(x-\frac{1}{3}\right)\mathrm{e}^{x}</equation>是二阶常系数非齐次线性微分方程<equation>y^{\prime \prime}+ay^{\prime}+by=c\mathrm{e}^{x}</equation>的一个特解，则（    )

A. a=-3,b=2,c=-1 B. a=3,b=2,c=-1 C. a=-3,b=2,c=1 D. a=3,b=2,c=1

答案: A

**解析:**解（法一）将<equation>y=\frac{1}{2}\mathrm{e}^{2x}+\left(x-\frac{1}{3}\right)\mathrm{e}^{x}</equation>代入<equation>y^{\prime \prime}+ay^{\prime}+by=c\mathrm{e}^{x}</equation>中，整理得到<equation>\left(2+a+\frac{1}{2}b\right)\mathrm{e}^{2x}+\left(1+a+b\right)x\mathrm{e}^{x}+\left(\frac{5}{3}+\frac{2}{3}a-\frac{1}{3}b\right)\mathrm{e}^{x}=c\mathrm{e}^{x}.</equation>比较上式两端系数，得到<equation>\left\{ \begin{array}{l l} 2+a+\frac{1}{2}b=0, \\ 1+a+b=0, \\ \frac{5}{3}+\frac{2}{3}a-\frac{1}{3}b=c, \end{array} \right.</equation>解得<equation>\left\{ \begin{array}{l l} a=-3, \\ b=2, \\ c=-1, \end{array} \right.</equation>故选A.

（法二）方程<equation>y^{\prime \prime}+a y^{\prime}+b y=c \mathrm{e}^{x}</equation>的特解可设为<equation>y^{*} = a_{0} x^{l} \mathrm{e}^{x}</equation>，其中当1不是特征方程的根时，l取0；当1是特征方程的单根时，l取1；当1是特征方程的重根时，l取2，因此得到如下表格.

<table border="1"><tr><td colspan="2"></td><td>1不是特征方程的根</td><td>1是特征方程的单根</td><td>1是特征方程的重根</td></tr><tr><td rowspan="3">非齐次线性方程的通解</td><td><equation>\lambda_{1}\neq\lambda_{2}</equation></td><td><equation>C_{1}\mathrm{e}^{\lambda_{1}x}+C_{2}\mathrm{e}^{\lambda_{2}x}+a_{0}\mathrm{e}^{x}</equation><equation>\lambda_{1}\neq1,\lambda_{2}\neq1</equation></td><td><equation>C_{1}\mathrm{e}^{x}+C_{2}\mathrm{e}^{\lambda_{2}x}+a_{0}x\mathrm{e}^{x}</equation><equation>\lambda_{1}=1,\lambda_{2}\neq1</equation></td><td>-</td></tr><tr><td><equation>\lambda_{1}=\lambda_{2}</equation></td><td><equation>C_{1}\mathrm{e}^{\lambda_{1}x}+C_{2}x\mathrm{e}^{\lambda_{1}x}+a_{0}\mathrm{e}^{x}</equation><equation>\lambda_{1}\neq1</equation></td><td>-</td><td><equation>C_{1}\mathrm{e}^{x}+C_{2}x\mathrm{e}^{x}+a_{0}x^{2}\mathrm{e}^{x}</equation></td></tr><tr><td><equation>\lambda_{1,2}=\alpha\pm\beta\mathrm{i}</equation></td><td><equation>\mathrm{e}^{\alpha x}(C_{1}\cos\beta x+C_{2}\sin\beta x)+a_{0}\mathrm{e}^{x}</equation></td><td>-</td><td>-</td></tr></table>

又<equation>y=\frac{1}{2}\mathrm{e}^{2x}+\left(x-\frac{1}{3}\right)\mathrm{e}^{x}</equation>是非齐次线性方程的一个特解，对比上述表格可知，非齐次线性方程的通解应为<equation>y=C_{1}\mathrm{e}^{x}+C_{2}\mathrm{e}^{\lambda_{2}x}+a_{0}x\mathrm{e}^{x}</equation>的形式.再由特解的表达式可知，<equation>\lambda_{1}=1,\lambda_{2}=2,a_{0}=1</equation>从而<equation>a=-\left(\lambda_{1}+\lambda_{2}\right)=-3,b=\lambda_{1}\lambda_{2}=2.</equation>将<equation>y^{*} = x\mathrm{e}^{x}</equation>代入方程<equation>y^{\prime \prime}-3y^{\prime}+2y=c\mathrm{e}^{x}</equation>中，可得c=-1，故选A.

---

**2014年第17题 | 解答题 | 10分**

17. (本题满分10分）

设函数 f(u)具有二阶连续导数，<equation>z=f(\mathrm{e}^{x}\cos y)</equation>满足<equation>\frac{\partial^{2} z}{\partial x^{2}}+\frac{\partial^{2} z}{\partial y^{2}}=(4 z+\mathrm{e}^{x}\cos y)\mathrm{e}^{2 x}.</equation>若 f(0)=0，<equation>f^{\prime}(0)=0</equation>求 f(u)的表达式.

**答案:**17)<equation>f(u)</equation><equation>= \frac {1}{1 6} \mathrm {e} ^ {2 u} - \frac {1}{1 6} \mathrm {e} ^ {- 2 u} - \frac {1}{4} u.</equation>

**解析:**解分别计算<equation>\frac{\partial^{2} z}{\partial x^{2}}</equation>和<equation>\frac{\partial^{2} z}{\partial y^{2}}.</equation><equation>\frac {\partial z}{\partial x} = \cos y \mathrm {e} ^ {x} f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right), \quad \frac {\partial^ {2} z}{\partial x ^ {2}} = \cos y \mathrm {e} ^ {x} f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right) + \cos^ {2} y \mathrm {e} ^ {2 x} f ^ {\prime \prime} \left(\mathrm {e} ^ {x} \cos y\right),</equation><equation>\frac {\partial z}{\partial y} = - \sin y \mathrm {e} ^ {x} f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right), \quad \frac {\partial^ {2} z}{\partial y ^ {2}} = - \cos y \mathrm {e} ^ {x} f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right) + \sin^ {2} y \mathrm {e} ^ {2 x} f ^ {\prime \prime} \left(\mathrm {e} ^ {x} \cos y\right).</equation>由<equation>\frac{\partial^{2} z}{\partial x^{2}}+\frac{\partial^{2} z}{\partial y^{2}}=(4 z+ \mathrm{e}^{x} \cos y) \mathrm{e}^{2 x}</equation>可得<equation>\mathrm {e} ^ {2 x} f ^ {\prime \prime} \left(\mathrm {e} ^ {x} \cos y\right) = \left[ 4 f \left(\mathrm {e} ^ {x} \cos y\right) + \mathrm {e} ^ {x} \cos y \right] \mathrm {e} ^ {2 x},</equation>即<equation>f ^ {\prime \prime} \left(\mathrm {e} ^ {x} \cos y\right) = 4 f \left(\mathrm {e} ^ {x} \cos y\right) + \mathrm {e} ^ {x} \cos y.</equation>我们得到一个二阶常系数非齐次线性微分方程<equation>f^{\prime \prime}(u) - 4f(u) = u.</equation>该方程对应的齐次方程的特征方程为<equation>r^{2}-4=0</equation>，因而解为<equation>f(u)=C_{1}\mathrm{e}^{2u}+C_{2}\mathrm{e}^{-2u}</equation>，其中<equation>C_{1},C_{2}</equation>为待定常数.

由于0不是特征方程的根，故<equation>f^{\prime \prime}(u) - 4 f(u) = u</equation>有形如<equation>z^{*} = C_{3} u + C_{4}</equation>的特解.代入原方程得<equation>- 4 C_{3} u - 4 C_{4} = u.</equation>于是<equation>C_{3} = -\frac{1}{4}, C_{4} = 0.</equation>因此，原方程的解为<equation>f (u) = C _ {1} \mathrm {e} ^ {2 u} + C _ {2} \mathrm {e} ^ {- 2 u} - \frac {1}{4} u.</equation>代入初值以确定<equation>C_{1}, C_{2}</equation>的值.由<equation>f(0)=0</equation>得，<equation>C_{1}+C_{2}=0.</equation>由<equation>f^{\prime}(0)=0</equation>得，<equation>2 C_{1}-2 C_{2}-\frac{1}{4}=0.</equation>从而解得<equation>C_{1}=\frac{1}{1 6}, C_{2}=-\frac{1}{1 6}.</equation>因此，<equation>f ( u ) = \frac { 1 } { 1 6 } \mathrm { e } ^ { 2 u } - \frac { 1 } { 1 6 } \mathrm { e } ^ { - 2 u } - \frac { 1 } { 4 } u .</equation>

---

**2010年第15题 | 解答题 | 10分**

15. (本题满分10分）

求微分方程<equation>y^{\prime \prime}-3 y^{\prime}+2 y=2 x \mathrm{e}^{x}</equation>的通解.

**答案:**(15)<equation>y = C_{1}\mathrm{e}^{x} + C_{2}\mathrm{e}^{2x} - (x^{2} + 2x)\mathrm{e}^{x}</equation>，其中<equation>C_{1}, C_{2}</equation>为任意常数.

**解析:**应的齐次线性方程<equation>y^{\prime \prime}-3 y^{\prime}+2 y=0</equation>的特征方程为<equation>\lambda^{2}-3 \lambda+2=0</equation>，解得<equation>\lambda_{1}=1,\lambda_{2}=</equation>2，于是齐次线性方程的通解为<equation>Y = C_{1}\mathrm{e}^{x} + C_{2}\mathrm{e}^{2x}</equation>，其中<equation>C_{1}, C_{2}</equation>为任意常数.

设原方程的一个特解为<equation>y^{*} = (ax + b)x\mathrm{e}^{x}</equation>，代入原方程得到<equation>\left(a x ^ {2} + 4 a x + b x + 2 a + 2 b\right) \mathrm {e} ^ {x} - 3 \left(a x ^ {2} + 2 a x + b x + b\right) \mathrm {e} ^ {x} + 2 \left(a x ^ {2} + b x\right) \mathrm {e} ^ {x} = 2 x \mathrm {e} ^ {x}.</equation>化简得<equation>- 2 a x+2 a-b=2 x</equation>，于是<equation>- 2 a = 2, \quad 2 a - b = 0,</equation>

---

**2009年第10题 | 填空题 | 4分**

10. 若二阶常系数线性齐次微分方程<equation>y^{\prime \prime}+a y^{\prime}+b y=0</equation>的通解为<equation>y=( C_{1}+C_{2} x ) \mathrm{e}^{x}</equation>，则非齐次方程<equation>y^{\prime \prime}+a y^{\prime}+b y=x</equation>满足条件<equation>y ( 0 )=2, y^{\prime} ( 0 )=0</equation>的解为 y=___

**答案:**- xe<equation>^{x}</equation>+ x + 2.

**解析:**解 由题设及二阶常系数线性齐次微分方程通解的形式知，特征方程<equation>\lambda^{2}+a\lambda+b=0</equation>的根为<equation>\lambda_{1}=\lambda_{2}=1</equation>，从而 a=-2,b=1.设非齐次线性方程<equation>y^{\prime \prime}-2y^{\prime}+y=x</equation>的一个特解为<equation>y^{*} = cx+d</equation>代入该方程，整理得到<equation>c x + d - 2 c = x.</equation>于是<equation>c = 1,d = 2c = 2</equation>，从而非齐次线性方程的通解为<equation>y = \left(C _ {1} + C _ {2} x\right) \mathrm {e} ^ {x} + x + 2.</equation>进而<equation>y^{\prime} = \left(C_{1} + C_{2} + C_{2}x\right)\mathrm{e}^{x} + 1.</equation>将<equation>y(0) = 2,y^{\prime}(0) = 0</equation>代入，得到<equation>C _ {1} + 2 = 2, \quad C _ {1} + C _ {2} + 1 = 0.</equation>解得<equation>C_{1} = 0, C_{2} = -1.</equation>因此，所求解为<equation>y = -x\mathrm{e}^{x} + x + 2.</equation>

---


#### 线性微分方程的解的结构

**2013年第10题 | 填空题 | 4分**

10. 已知<equation>y_{1}=\mathrm{e}^{3 x}-x \mathrm{e}^{2 x}, y_{2}=\mathrm{e}^{x}-x \mathrm{e}^{2 x}, y_{3}=-x \mathrm{e}^{2 x}</equation>是某二阶常系数非齐次线性微分方程的3个解，则该方程的通解为 y=___

**答案:**<equation>C_{1}\mathrm{e}^{3x} + C_{2}\mathrm{e}^{x} - x\mathrm{e}^{2x}</equation>，其中<equation>C_{1}, C_{2}</equation>为任意常数.

**解析:**解 由题设知，<equation>y_{1}-y_{3}=\mathrm{e}^{3 x}, y_{2}-y_{3}=\mathrm{e}^{x}</equation>是对应的齐次线性微分方程的两个线性无关的解。又<equation>y_{3}=-x\mathrm{e}^{2 x}</equation>是非齐次线性微分方程的解，故所求通解为<equation>y = C _ {1} \mathrm {e} ^ {3 x} + C _ {2} \mathrm {e} ^ {x} - x \mathrm {e} ^ {2 x},</equation>其中<equation>C_{1}, C_{2}</equation>为任意常数.

---


## 线性代数
### 二次型
### 线性方程组
### 矩阵