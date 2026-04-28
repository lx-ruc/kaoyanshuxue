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


