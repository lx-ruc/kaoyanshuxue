#### 微分方程的应用

**2023年第14题 | 填空题 | 5分**

14. 设某公司在 t 时刻的资产为 f(t)，从 0 时刻到 t 时刻的平均资产等于<equation>\frac{f(t)}{t}-t</equation>. 假设 f(t) 连续且 f(0)=0，则<equation>f(t)=</equation>___.

**答案:**<equation>2 \mathrm {e} ^ {t} - 2 t - 2.</equation>

**解析:**解对 t > 0，从0时刻到 t时刻的平均资产为<equation>\frac{1}{t}\int_{0}^{t} f(u)\mathrm{d}u</equation>，故由已知条件可知<equation>\frac {1}{t} \int_ {0} ^ {t} f (u) \mathrm {d} u = \frac {f (t)}{t} - t.</equation>整理可得<equation>\int_ {0} ^ {t} f (u) \mathrm {d} u = f (t) - t ^ {2}.</equation>对（1）式两端关于 t求导，可得<equation>f (t) = f ^ {\prime} (t) - 2 t, \quad \mathrm {即} f ^ {\prime} (t) - f (t) = 2 t.</equation>由一阶非齐次线性微分方程的通解公式可得<equation>\begin{array}{l} f (t) = \mathrm {e} ^ {\int \mathrm {d} t} \left(\int 2 t \cdot \mathrm {e} ^ {- \int \mathrm {d} t} \mathrm {d} t + C\right) = \mathrm {e} ^ {t} \left(\int 2 t \cdot \mathrm {e} ^ {- t} \mathrm {d} t + C\right) \\ = \mathrm {e} ^ {t} \left[ - 2 \int t \mathrm {d} \left(\mathrm {e} ^ {- t}\right) + C \right] = \mathrm {e} ^ {t} \left[ - 2 \left(t \mathrm {e} ^ {- t} - \int \mathrm {e} ^ {- t} \mathrm {d} t\right) + C \right] \\ = \mathrm {e} ^ {t} \left(- 2 t \mathrm {e} ^ {- t} - 2 \mathrm {e} ^ {- t} + C\right) = C \mathrm {e} ^ {t} - 2 t - 2. \\ \end{array}</equation>代入初始条件<equation>f ( 0 ) = 0</equation>，可得<equation>0 = C - 2</equation>，即<equation>C = 2.</equation>因此，<equation>f ( t ) = 2 \mathrm{e}^{t} - 2 t - 2.</equation>

---

**2015年第18题 | 解答题 | 10分**

18. (本题满分10分)

设函数 f(x)在定义域 I上的导数大于零.若对任意的<equation>x_{0}\in I</equation>，曲线 y=f(x)在点 （<equation>x_{0},f(x_{0})</equation>）处的切线与直线<equation>x=x_{0}</equation>及 x轴所围成区域的面积恒为4，且 f(0)=2，求 f(x)的表达式.

**答案:**<equation>(1 8) f (x) = \frac {8}{4 - x}, x \in I.</equation>

**解析:**解如图所示，曲线<equation>y=f(x)</equation>在点<equation>\left(x_{0},f\left(x_{0}\right)\right)</equation>处的切线为<equation>y - f \left(x _ {0}\right) = f ^ {\prime} \left(x _ {0}\right) \left(x - x _ {0}\right).</equation>令<equation>y = 0</equation>，注意到<equation>f^{\prime}(x) > 0</equation>，解得<equation>x = x_{0} - \frac{f(x_{0})}{f^{\prime}(x_{0})}</equation>，即该切线与<equation>x</equation>轴的交点为<equation>\left(x_0 - \frac{f(x_0)}{f^{\prime}(x_0)},0\right)</equation>.

曲线<equation>y=f(x)</equation>在点<equation>\left(x_{0}, f\left(x_{0}\right)\right)</equation>处的切线与直线<equation>x=x_{0}</equation>及x轴所围成区域为三角形，底边长<equation>\left|x_{0}-\left[x_{0}-\frac{f\left(x_{0}\right)}{f^{\prime}\left(x_{0}\right)}\right]\right|</equation>，高<equation>|f(x_{0})-0|</equation>.于是，<equation>\frac {\left| f \left(x _ {0}\right) - 0 \right| \cdot \left| x _ {0} - \left[ x _ {0} - \frac {f \left(x _ {0}\right)}{f ^ {\prime} \left(x _ {0}\right)} \right] \right|}{2} = 4, \quad \text {即} \frac {\left| f \left(x _ {0}\right) \right| \cdot \left| \frac {f \left(x _ {0}\right)}{f ^ {\prime} \left(x _ {0}\right)} \right|}{2} = 4.</equation>由于<equation>f^{\prime}(x) > 0</equation>，故<equation>\frac {\left[ f \left(x _ {0}\right) \right] ^ {2}}{f ^ {\prime} \left(x _ {0}\right)} = 8, \quad x _ {0} \in I,</equation>即<equation>f(x)</equation>满足微分方程<equation>8y^{\prime} = y^{2}</equation>.

分离变量，得<equation>\frac{8}{y^{2}}\mathrm{d}y=\mathrm{d}x.</equation>方程两端积分，得<equation>-\frac{8}{y}=x+C</equation>其中C为待定常数.由于<equation>f(0)=2</equation>故 C=-4，从而<equation>y=\frac{8}{4-x}.</equation>因此，<equation>f (x) = \frac {8}{4 - x}, \quad x \in I.</equation>

---


