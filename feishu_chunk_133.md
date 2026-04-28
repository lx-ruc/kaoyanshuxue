#### 二重积分的概念与性质

**2016年第3题 | 选择题 | 4分 | 答案: B**

3. 设<equation>J_{i}=\iint_{D_{i}} \sqrt[3]{x-y}\mathrm{d}x\mathrm{d}y(i=1,2,3)</equation>，其中<equation>D_{1}=\{(x,y)\mid 0\leqslant x\leqslant 1,0\leqslant y\leqslant 1\}</equation><equation>D_{2}=\{(x,y)\mid 0\leqslant x\leqslant 1,0\leqslant y\leqslant \sqrt{x}\}</equation><equation>D_{3}=\{(x,y)\mid 0\leqslant x\leqslant 1,x^{2}\leqslant y\leqslant 1</equation>则（    ）

A.<equation>J_{1}<J_{2}<J_{3}</equation>B.<equation>J_{3}<J_{1}<J_{2}</equation>C.<equation>J_{2}<J_{3}<J_{1}</equation>D.<equation>J_{2}<J_{1}<J_{3}</equation>

答案: B

**解析:**解如图所示，<equation>D_{1}=D_{2}\cup D_{2}^{\prime}=D_{3}\cup D_{3}^{\prime}.</equation>在<equation>D_{2}^{\prime}</equation>上，由于<equation>x-y<0,\sqrt[3]{x-y}<0</equation>，故<equation>\iint_{D_{2}^{\prime}} \sqrt[3]{x-y}\mathrm{d}x\mathrm{d}y<0.</equation>在<equation>D_{3}^{\prime}</equation>上，由于<equation>x-y>0,\sqrt[3]{x-y}>0</equation>，故<equation>\iint_{D_{3}^{\prime}} \sqrt[3]{x-y}\mathrm{d}x\mathrm{d}y>0.</equation>因此，<equation>J _ {1} - J _ {2} = \iint_ {D _ {1} \backslash D _ {2}} \sqrt [ 3 ]{x - y} \mathrm {d} x \mathrm {d} y = \iint_ {D _ {2} ^ {\prime}} \sqrt [ 3 ]{x - y} \mathrm {d} x \mathrm {d} y < 0,</equation><equation>J _ {1} - J _ {3} = \iint_ {D _ {1} \backslash D _ {3}} \sqrt [ 3 ]{x - y} \mathrm {d} x \mathrm {d} y = \iint_ {D _ {3} ^ {\prime}} \sqrt [ 3 ]{x - y} \mathrm {d} x \mathrm {d} y > 0.</equation>综上所述，<equation>J_{1} < J_{2}, J_{1} > J_{3}</equation>，即<equation>J_{3} < J_{1} < J_{2}.</equation>应选B.

---

**2013年第3题 | 选择题 | 4分 | 答案: B**

3. 设<equation>D_{k}</equation>是圆域<equation>D=\{(x,y)\mid x^{2}+y^{2}\leqslant 1\}</equation>位于第 k象限的部分.记<equation>I_{k}=\iint_{D_{k}}(y-x)\mathrm{d}x\mathrm{d}y(k=1,2,3,4)</equation>，则（    )

A.<equation>I_{1}>0</equation>B.<equation>I_{2}>0</equation>C.<equation>I_{3}>0</equation>D.<equation>I_{4}>0</equation>

答案: B

**解析:**解（法一）由于在第一象限内 x > 0，y > 0，第二象限内 x < 0，y > 0，第三象限内 x < 0， y < 0，第四象限内 x > 0，y < 0，故被积函数 y - x在第二象限内恒大于零，从而<equation>\iint_{D_{2}}(y-x)\mathrm{d}x\mathrm{d}y>0.</equation>应选B.

（法二）在极坐标系下计算<equation>I_{k}(k = 1,2,3,4).</equation><equation>\begin{array}{l} I _ {k} \stackrel {\text {极 坐 标}} {=} \int_ {\frac {(k - 1) \pi}{2}} ^ {\frac {k \pi}{2}} (\sin \theta - \cos \theta) \mathrm {d} \theta \int_ {0} ^ {1} r ^ {2} \mathrm {d} r = \frac {1}{3} \int_ {\frac {(k - 1) \pi}{2}} ^ {\frac {k \pi}{2}} (\sin \theta - \cos \theta) \mathrm {d} \theta \\ = - \frac {\left(\sin \theta + \cos \theta\right)}{3} \Bigg | _ {\frac {(k - 1) \pi}{2}} ^ {\frac {k \pi}{2}}. \\ \end{array}</equation>分别求得<equation>I _ {1} = 0, \quad I _ {2} = \frac {2}{3}, \quad I _ {3} = 0, \quad I _ {4} = - \frac {2}{3}.</equation><equation>I_{2} > 0</equation>应选B.

---


