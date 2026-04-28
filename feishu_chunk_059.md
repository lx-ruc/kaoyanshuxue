#### 交换积分次序与坐标系之间的转化

**2025年第4题 | 选择题 | 5分 | 答案: A**

4. 设函数 f(x,y) 连续，则<equation>\int_{-2}^{2}\mathrm{d}x\int_{4-x^{2}}^{4}f(x,y)\mathrm{d}y=</equation>(    )

A.<equation>\int_{0}^{4}\left[\int_{-2}^{-\sqrt{4-y}}f(x,y)\mathrm{d}x+\int_{\sqrt{4-y}}^{2}f(x,y)\mathrm{d}x\right]\mathrm{d}y</equation>B.<equation>\int_{0}^{4}\left[\int_{-2}^{\sqrt{4-y}}f(x,y)\mathrm{d}x+\int_{\sqrt{4-y}}^{2}f(x,y)\mathrm{d}x\right]\mathrm{d}y</equation>C.<equation>\int_{0}^{4}\left[\int_{-2}^{-\sqrt{4-y}}f(x,y)\mathrm{d}x+\int_{2}^{\sqrt{4-y}}f(x,y)\mathrm{d}x\right]\mathrm{d}y</equation>D.<equation>2\int_{0}^{4}\mathrm{d}y\int_{\sqrt{4-y}}^{2}f(x,y)\mathrm{d}x</equation>

答案: A

**解析:**解 如图所示，二次积分<equation>\int_{-2}^{2}\mathrm{d}x\int_{4-x^{2}}^{4}f(x,y)\mathrm{d}y</equation>对应的二重积分的积分区域 D为图中灰色区域.<equation>D = \left\{(x, y) \mid 4 - x ^ {2} \leqslant y \leqslant 4, - 2 \leqslant x \leqslant 2 \right\}.</equation>当 x < 0时，解 y = 4 - x²可得 x = -<equation>\sqrt{4-y}</equation>，当 x > 0时，解 y = 4 - x²可得 x =<equation>\sqrt{4-y}</equation>.于是，将 D写成 Y型区域需要将其分块，<equation>D=\{(x,y)\mid-2\leqslant x\leqslant-\sqrt{4-y},0\leqslant y\leqslant 4\} \cup \{(x,y)\mid\sqrt{4-y}\leqslant x\leqslant 2,0\leqslant y\leqslant 4\}</equation>从而，<equation>\int_ {- 2} ^ {2} \mathrm {d} x \int_ {4 - x ^ {2}} ^ {4} f (x, y) \mathrm {d} y = \iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {4} \left[ \int_ {- 2} ^ {- \sqrt {4 - y}} f (x, y) \mathrm {d} x + \int_ {\sqrt {4 - y}} ^ {2} f (x, y) \mathrm {d} x \right] \mathrm {d} y.</equation>选项A正确，选项B、C不正确.

对选项D，该选项正确意味着<equation>\iint_{D} f(x,y)\mathrm{d}x\mathrm{d}y = 2\iint_{D_1} f(x,y)\mathrm{d}x\mathrm{d}y</equation>，其中<equation>D_{1}</equation>为D位于y轴右边的部分，而该式成立需要<equation>f(x,y)</equation>是关于x的偶函数，但题干条件中并没有这一信息，故该选项不正确.例如，取<equation>f(x,y) = x</equation>，则<equation>\iint_{D} f(x,y)\mathrm{d}x\mathrm{d}y = 0</equation>，而<equation>\iint_{D_1} f(x,y)\mathrm{d}x\mathrm{d}y > 0.</equation>因此，应选A.

---

**2015年第4题 | 选择题 | 4分 | 答案: B**

4. 设 D是第一象限中的曲线<equation>2 x y=1, 4 x y=1</equation>与直线 y=x,y=<equation>\sqrt{3} x</equation>围成的平面区域，函数 f(x,y)在 D上连续，则<equation>\iint \limits_{D} f(x,y)\mathrm{d} x\mathrm{d} y=</equation>(    )

A.<equation>\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \mathrm{d} \theta \int_{\frac{1}{2 \sin 2 \theta}}^{\frac{1}{\sin 2 \theta}} f ( r \cos \theta,r \sin \theta ) r \mathrm{d} r</equation>B.<equation>\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \mathrm{d} \theta \int_{\frac{1}{\sqrt{2 \sin 2 \theta}}}^{\frac{1}{\sqrt{\sin 2 \theta}}} f ( r \cos \theta,r \sin \theta ) r \mathrm{d} r</equation>C.<equation>\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \mathrm{d} \theta \int_{\frac{1}{2 \sin 2 \theta}}^{\frac{1}{\sin 2 \theta}} f ( r \cos \theta,r \sin \theta ) \mathrm{d} r</equation>D.<equation>\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \mathrm{d} \theta \int_{\frac{1}{\sqrt{2 \sin 2 \theta}}}^{\frac{1}{\sqrt{\sin 2 \theta}}} f ( r \cos \theta,r \sin \theta ) \mathrm{d} r</equation>

答案: B

**解析:**解 将曲线<equation>2 x y=1</equation>，<equation>4 x y=1</equation>，直线<equation>y=x</equation>，<equation>y=\sqrt{3} x</equation>改写为极坐标形式.积分区域如图所示.<equation>2 x y = 1 \Rightarrow r ^ {2} \sin 2 \theta = 1 \Rightarrow r = \frac {1}{\sqrt {\sin 2 \theta}},</equation><equation>4 x y = 1 \Rightarrow 2 r ^ {2} \sin 2 \theta = 1 \Rightarrow r = \frac {1}{\sqrt {2 \sin 2 \theta}},</equation><equation>y = x \Rightarrow \theta = \frac {\pi}{4},</equation><equation>y = \sqrt {3} x \Rightarrow \theta = \frac {\pi}{3},</equation><equation>\mathrm {d} x \mathrm {d} y = r \mathrm {d} r \mathrm {d} \theta .</equation>于是，积分区域<equation>D</equation>在极坐标系下表示为<equation>D = \left\{(r, \theta) \mid \frac {1}{\sqrt {2 \sin 2 \theta}} \leqslant r \leqslant \frac {1}{\sqrt {\sin 2 \theta}}, \frac {\pi}{4} \leqslant \theta \leqslant \frac {\pi}{3} \right\}.</equation>因此，<equation>\iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{3}} \mathrm {d} \theta \int_ {\frac {1}{\sqrt {2 \sin 2 \theta}}} ^ {\frac {1}{\sqrt {\sin 2 \theta}}} f (r \cos \theta , r \sin \theta) r \mathrm {d} r.</equation>应选B.

---

**2014年第3题 | 选择题 | 4分 | 答案: D**

3. 设 f(x,y)是连续函数，则<equation>\int_{0}^{1}\mathrm{d}y\int_{-\sqrt{1-y^{2}}}^{1-y}f(x,y)\mathrm{d}x=</equation>(    )

A.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{x-1}f(x,y)\mathrm{d}y+\int_{-1}^{0}\mathrm{d}x\int_{0}^{\sqrt{1-x^{2}}}f(x,y)\mathrm{d}y</equation>B.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{1-x}f(x,y)\mathrm{d}y+\int_{-1}^{0}\mathrm{d}x\int_{-\sqrt{1-x^{2}}}^{0}f(x,y)\mathrm{d}y</equation>C.<equation>\int_{0}^{\frac{\pi}{2}}\mathrm{d}\theta \int_{0}^{\frac{1}{\cos \theta+\sin \theta}}f(r\cos \theta,r\sin \theta)\mathrm{d}r+\int_{\frac{\pi}{2}}^{\pi}\mathrm{d}\theta \int_{0}^{1}f(r\cos \theta,r\sin \theta)\mathrm{d}r</equation>D.<equation>\int_{0}^{\frac{\pi}{2}}\mathrm{d}\theta \int_{0}^{\frac{1}{\cos \theta+\sin \theta}}f(r\cos \theta,r\sin \theta)r\mathrm{d}r+\int_{\frac{\pi}{2}}^{\pi}\mathrm{d}\theta \int_{0}^{1}f(r\cos \theta,r\sin \theta)r\mathrm{d}r</equation>

答案: D

**解析:**分析本题主要考查二次积分的积分次序交换和换元法.观察选项A、B，是将先x后y的二次积分化为先y后x的二次积分，结合积分区域的图形来转化会比较方便；观察选项C、D，是将原二次积分化为极坐标系下的二次积分，需要用到换元公式<equation>\iint_{D} f(x,y)\mathrm{d}x\mathrm{d}y=\iint_{D} f(r\cos \theta ,r\sin \theta )r\mathrm{d}r\mathrm{d}\theta.</equation>解题设中二次积分的积分区域为<equation>D=\{(x,y)\mid 0\leqslant y\leqslant 1,-\sqrt{1-y^{2}}\leqslant x\leqslant 1-y\}</equation>，将区域D分成两部分<equation>D_{1}</equation>和<equation>D_{2}</equation>（如上图所示），其中<equation>\begin{array}{l} D _ {1} = \left\{(x, y) \mid 0 \leqslant y \leqslant \sqrt {1 - x ^ {2}}, - 1 \leqslant x \leqslant 0 \right\}, \\ D _ {2} = \left\{(x, y) \mid 0 \leqslant y \leqslant 1 - x, 0 \leqslant x \leqslant 1 \right\}. \\ \end{array}</equation>于是<equation>\int_0^1\mathrm{d}y\int_{- \sqrt{1 - y^2}}^{1 - y}f(x,y)\mathrm{d}x = \int_{-1}^0\mathrm{d}x\int_0^{\sqrt{1 - x^2}}f(x,y)\mathrm{d}y + \int_0^1\mathrm{d}x\int_0^{1 - x}f(x,y)\mathrm{d}y</equation>，从而选项A、B均不正确.

在极坐标变换下，区域<equation>D_{1}</equation>的边界方程为<equation>\theta = \frac{\pi}{2},\theta = \pi,r = 1</equation>；区域<equation>D_{2}</equation>的边界方程为<equation>\theta = 0,\theta = \frac{\pi}{2},r = \frac{1}{\cos \theta + \sin \theta}</equation>设区域<equation>D_{1},D_{2}</equation>在极坐标变换下对应于直角坐标平面<equation>rO\theta</equation>上的区域为<equation>D_{1}^{\prime},D_{2}^{\prime}</equation>，则<equation>D _ {1} ^ {\prime} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 1, \frac {\pi}{2} \leqslant \theta \leqslant \pi \right\},</equation><equation>D _ {2} ^ {\prime} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \frac {1}{\cos \theta + \sin \theta}, 0 \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation>从而<equation>\int_ {0} ^ {1} \mathrm {d} y \int_ {- \sqrt {1 - y ^ {2}}} ^ {1 - y} f (x, y) \mathrm {d} x = \int_ {0} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {\frac {1}{\cos \theta + \sin \theta}} f (r \cos \theta , r \sin \theta) r \mathrm {d} r + \int_ {\frac {\pi}{2}} ^ {\pi} \mathrm {d} \theta \int_ {0} ^ {1} f (r \cos \theta , r \sin \theta) r \mathrm {d} r.</equation>应选 D.

选项C错误的原因是少了雅可比式<equation>r</equation>

---


