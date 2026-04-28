#### 交换积分次序与坐标系之间的转化

**2025年第4题 | 选择题 | 5分 | 答案: D**

4. 设函数 f(x) 连续，<equation>\int_{0}^{1}\mathrm{d}y\int_{0}^{y}f(x)\mathrm{d}x=</equation>(    )

A.<equation>\int_{0}^{1}x f(x)\mathrm{d}x</equation>B.<equation>\int_{0}^{1}(x+1)f(x)\mathrm{d}x</equation>C.<equation>\int_{0}^{1}(x-1)f(x)\mathrm{d}x</equation>D.<equation>\int_{0}^{1}(1-x)f(x)\mathrm{d}x</equation>

答案: D

**解析:**解 二次积分<equation>\int_{0}^{1}\mathrm{d}y\int_{0}^{y}f(x)\mathrm{d}x</equation>对应的二重积分的积分区域<equation>D = \left\{(x, y) \mid 0 \leqslant x \leqslant y, 0 \leqslant y \leqslant 1 \right\}.</equation>区域 D如图所示.将 D写成 X型区域.<equation>D = \left\{(x, y) \mid x \leqslant y \leqslant 1, 0 \leqslant x \leqslant 1 \right\}.</equation>于是，<equation>\int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {y} f (x) \mathrm {d} x = \iint_ {D} f (x) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} f (x) \mathrm {d} x \int_ {x} ^ {1} \mathrm {d} y = \int_ {0} ^ {1} (1 - x) f (x) \mathrm {d} x.</equation>因此，应选D.

---

**2024年第3题 | 选择题 | 5分 | 答案: A**

3. 设 f(x,y)是连续函数，则<equation>\int_{\frac{\pi}{6}}^{\frac{\pi}{2}} \mathrm{d} x \int_{\sin x}^{1} f(x,y) \mathrm{d} y=</equation>(    )

A.<equation>\int_{\frac{1}{2}}^{1} \mathrm{d} y \int_{\frac{\pi}{6}}^{\arcsin y} f(x,y) \mathrm{d} x</equation>B.<equation>\int_{\frac{1}{2}}^{1} \mathrm{d} y \int_{\arcsin y}^{\frac{\pi}{2}} f(x,y) \mathrm{d} x</equation>C.<equation>\int_{0}^{\frac{1}{2}} \mathrm{d} y \int_{\frac{\pi}{6}}^{\arcsin y} f(x,y) \mathrm{d} x</equation>D.<equation>\int_{0}^{\frac{1}{2}} \mathrm{d} y \int_{\arcsin y}^{\frac{\pi}{2}} f(x,y) \mathrm{d} x</equation>

答案: A

**解析:**解二次积分<equation>\int_{\frac{\pi}{6}}^{\frac{\pi}{2}} \mathrm{d} x \int_{\sin x}^{1} f(x,y)\mathrm{d} y</equation>对应的二重积分的积分区域为<equation>D = \left\{(x, y) \mid \sin x \leqslant y \leqslant 1, \frac {\pi}{6} \leqslant x \leqslant \frac {\pi}{2} \right\}.</equation>由于<equation>\arcsin y</equation>的值域为<equation>\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>，而<equation>\left[\frac{\pi}{6},\frac{\pi}{2}\right]\subset\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>，故曲线<equation>y=\sin x \left(x\in\left[\frac{\pi}{6},\frac{\pi}{2}\right]\right)</equation>上的点（x,y）可写为（<equation>\arcsin y,y).</equation>由此可将 D改写成Y型区域，<equation>D = \left\{(x, y) \mid \frac {\pi}{6} \leqslant x \leqslant \arcsin y, \frac {1}{2} \leqslant y \leqslant 1 \right\}.</equation>因此，<equation>\int_ {\frac {\pi}{6}} ^ {\frac {\pi}{2}} \mathrm {d} x \int_ {\sin x} ^ {1} f (x, y) \mathrm {d} y = \int_ {\frac {1}{2}} ^ {1} \mathrm {d} y \int_ {\frac {\pi}{6}} ^ {\arcsin y} f (x, y) \mathrm {d} x.</equation>应选A.

---

**2015年第3题 | 选择题 | 4分 | 答案: B**

3. 设<equation>D=\{(x,y)\mid x^{2}+y^{2}\leqslant 2x,x^{2}+y^{2}\leqslant 2y\}</equation>，函数 f(x,y)在 D上连续，则<equation>\iint_{D}f(x,y)\mathrm{d}x\mathrm{d}y=</equation>(    )

A.<equation>\int_{0}^{\frac{\pi}{4}}\mathrm{d}\theta \int_{0}^{2\cos \theta}f(r\cos \theta,r\sin \theta)r\mathrm{d}r+\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}\mathrm{d}\theta \int_{0}^{2\sin \theta}f(r\cos \theta,r\sin \theta)r\mathrm{d}r</equation>B.<equation>\int_{0}^{\frac{\pi}{4}}\mathrm{d}\theta \int_{0}^{2\sin \theta}f(r\cos \theta,r\sin \theta)r\mathrm{d}r+\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}\mathrm{d}\theta \int_{0}^{2\cos \theta}f(r\cos \theta,r\sin \theta)r\mathrm{d}r</equation>C.<equation>2\int_{0}^{1}\mathrm{d}x\int_{1-\sqrt{1-x^{2}}}^{x}f(x,y)\mathrm{d}y</equation>D.<equation>2\int_{0}^{1}\mathrm{d}x\int_{x}^{\sqrt{2x-x^{2}}}f(x,y)\mathrm{d}y</equation>

答案: B

**解析:**解 圆<equation>x^{2}+y^{2}=2x</equation>的极坐标方程为<equation>r=2\cos \theta</equation>，圆<equation>x^{2}+y^{2}=2y</equation>的极坐标方程为<equation>r=2\sin \theta.</equation>由图可知，当<equation>0\leqslant \theta \leqslant \frac{\pi}{4}</equation>时，D的边界为<equation>r=2\sin \theta</equation>；当<equation>\frac{\pi}{4}\leqslant \theta \leqslant \frac{\pi}{2}</equation>时，D的边界为<equation>r=2\cos \theta</equation>于是，<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2 \sin \theta , 0 \leqslant \theta \leqslant \frac {\pi}{4} \right\} \cup \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2 \cos \theta , \frac {\pi}{4} \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation>因此，<equation>\iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {\frac {\pi}{4}} \mathrm {d} \theta \int_ {0} ^ {2 \sin \theta} f (r \cos \theta , r \sin \theta) r \mathrm {d} r + \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {2 \cos \theta} f (r \cos \theta , r \sin \theta) r \mathrm {d} r.</equation>应选B.

由上述论证可知选项A不正确.

若在直角坐标系下计算，则区域 D 可表示为<equation>D = \left\{(x, y) \mid 1 - \sqrt {1 - x ^ {2}} \leqslant y \leqslant \sqrt {2 x - x ^ {2}}, 0 \leqslant x \leqslant 1 \right\}.</equation>于是，<equation>\iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {1 - \sqrt {1 - x ^ {2}}} ^ {\sqrt {2 x - x ^ {2}}} f (x, y) \mathrm {d} y.</equation>因此，选项C、D均不正确.

---

**2014年第12题 | 填空题 | 4分**

12. 二次积分<equation>\int_{0}^{1}\mathrm{d}y\int_{y}^{1}\left(\frac{\mathrm{e}^{x^{2}}}{x}-\mathrm{e}^{y^{2}}\right)\mathrm{d}x=</equation>___

**解析:**<equation>\begin{aligned} \int_ {0} ^ {1} \mathrm {d} y \int_ {y} ^ {1} \left(\frac {\mathrm {e} ^ {x ^ {2}}}{x} - \mathrm {e} ^ {y ^ {2}}\right) \mathrm {d} x &= \int_ {0} ^ {1} \mathrm {d} y \int_ {y} ^ {1} \frac {\mathrm {e} ^ {x ^ {2}}}{x} \mathrm {d} x - \int_ {0} ^ {1} \mathrm {d} y \int_ {y} ^ {1} \mathrm {e} ^ {y ^ {2}} \mathrm {d} x \\ &= \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {x} \frac {\mathrm {e} ^ {x ^ {2}}}{x} \mathrm {d} y - \int_ {0} ^ {1} (1 - y) \mathrm {e} ^ {y ^ {2}} \mathrm {d} y \\ &= \int_ {0} ^ {1} \mathrm {e} ^ {x ^ {2}} \mathrm {d} x - \int_ {0} ^ {1} \mathrm {e} ^ {y ^ {2}} \mathrm {d} y + \int_ {0} ^ {1} y \mathrm {e} ^ {y ^ {2}} \mathrm {d} y \\ &= \frac {1}{2} \int_ {0} ^ {1} \mathrm {e} ^ {y ^ {2}} \mathrm {d} \left(y ^ {2}\right) = \frac {1}{2} \mathrm {e} ^ {y ^ {2}} \Big | _ {0} ^ {1} = \frac {\mathrm {e} - 1}{2}. \end{aligned}</equation>

---

**2012年第3题 | 选择题 | 4分 | 答案: B**

3. 设函数 f(t) 连续，则二次积分<equation>\int_{0}^{\frac{\pi}{2}} \mathrm{d}\theta \int_{2\cos \theta}^{2} f\left(r^{2}\right) r \mathrm{d} r=</equation>(    )

A.<equation>\int_{0}^{2} \mathrm{d} x \int_{\sqrt{2 x-x^{2}}}^{\sqrt{4-x^{2}}} \sqrt{x^{2}+y^{2}} f\left(x^{2}+y^{2}\right) \mathrm{d} y</equation>B.<equation>\int_{0}^{2} \mathrm{d} x \int_{\sqrt{2 x-x^{2}}}^{\sqrt{4-x^{2}}} f\left(x^{2}+y^{2}\right) \mathrm{d} y</equation>C.<equation>\int_{0}^{2} \mathrm{d} y \int_{1+\sqrt{1-y^{2}}}^{\sqrt{4-y^{2}}} \sqrt{x^{2}+y^{2}} f\left(x^{2}+y^{2}\right) \mathrm{d} x</equation>D.<equation>\int_{0}^{2} \mathrm{d} y \int_{1+\sqrt{1-y^{2}}}^{\sqrt{4-y^{2}}} f\left(x^{2}+y^{2}\right) \mathrm{d} x</equation>

答案: B

**解析:**解 原二次积分对应的二重积分的积分区域为<equation>D=\left\{(r,\theta)\mid 2\cos \theta \leqslant r\leqslant 2,0\leqslant \theta \leqslant \frac{\pi}{2}\right\}</equation>曲线 r=2，r=2cos<equation>\theta</equation>的直角坐标方程分别为<equation>x^{2}+y^{2}=4</equation><equation>x^{2}+y^{2}=2x.</equation>(a)

(b)

由于<equation>0 \leqslant \theta \leqslant \frac{\pi}{2}</equation>，故区域D如图（a）所示. D在直角坐标系下可表示为<equation>D = \left\{(x, y) \mid \sqrt {2 x - x ^ {2}} \leqslant y \leqslant \sqrt {4 - x ^ {2}}, 0 \leqslant x \leqslant 2 \right\}.</equation>将<equation>f(r^{2})</equation>换成<equation>f(x^{2}+y^{2})</equation>，将<equation>r\mathrm{d}r\mathrm{d}\theta</equation>换成<equation>\mathrm{d}x\mathrm{d}y</equation>，得<equation>\int_{0}^{2}\mathrm{d}x\int_{\sqrt{2x-x^{2}}}^{\sqrt{4-x^{2}}}f(x^{2}+y^{2})\mathrm{d}y.</equation>应选B.

下面我们说明选项 A、C、D不正确.

选项A中的积分区域表示与选项B一样，但是被积函数多了一个因子<equation>\sqrt{x^{2}+y^{2}}</equation>注意到，极坐标与直角坐标的相互转化中，<equation>\mathrm{r} \mathrm{d} r \mathrm{d} \theta=\mathrm{d} x \mathrm{d} y</equation>原积分中的<equation>\mathrm{r} \mathrm{d} r \mathrm{d} \theta</equation>转化为<equation>\mathrm{d} x \mathrm{d} y</equation>被积函数变为<equation>f \left(x^{2}+y^{2}\right)</equation>在新积分中，没有因子r.选项A不正确.

被积函数与选项A一样.选项C不正确.

选项D中的积分区域为<equation>D^{\prime}=\{(x,y)\mid 1+\sqrt{1-y^{2}}\leqslant x\leqslant \sqrt{4-y^{2}},0\leqslant y\leqslant 2\}</equation><equation>D^{\prime}</equation>如图（b）所示.选项D不正确.

---


