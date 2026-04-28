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


