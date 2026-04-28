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

**2025年第5题 | 选择题 | 5分 | 答案: B**

5. 二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=x_{1}^{2}+2 x_{1} x_{2}+2 x_{1} x_{3}</equation>的正惯性指数为（    )

A.0 B.1 C.2 D.3

答案: B

**解析:**解 （法一）配方法.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= x _ {1} ^ {2} + 2 x _ {1} x _ {2} + 2 x _ {1} x _ {3} = \left(x _ {1} + x _ {2} + x _ {3}\right) ^ {2} - x _ {2} ^ {2} - x _ {3} ^ {2} - 2 x _ {2} x _ {3} \\ &= \left(x _ {1} + x _ {2} + x _ {3}\right) ^ {2} - \left(x _ {2} + x _ {3}\right) ^ {2}. \end{aligned}</equation>令<equation>\left\{ \begin{array}{l l} y_{1}=x_{1}+x_{2}+x_{3}, \\ y_{2}=x_{2}+x_{3}, \\ y_{3}=x_{3}, \end{array} \right.</equation>则该变换为可逆线性变换，在该变换下 f（<equation>x_{1}, x_{2}, x_{3}</equation>）化为标准形<equation>y_{1}^{2}-y_{2}^{2}.</equation>因此，<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>的正惯性指数为1，应选B.

（法二）特征值法.<equation>f\left(x_{1}, x_{2}, x_{3}\right)</equation>对应的实对称矩阵<equation>A = \left( \begin{array}{c c c} 1 & 1 & 1 \\ 1 & 0 & 0 \\ 1 & 0 & 0 \end{array} \right)</equation>.

计算 A的特征值.<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - 1 & - 1 & - 1 \\ - 1 & \lambda & 0 \\ - 1 & 0 & \lambda  \right| \xlongequal {c _ {3} + \lambda c _ {1}} \left| \begin{array}{c c c} \lambda - 1 & - 1 & \lambda^ {2} - \lambda - 1 \\ - 1 & \lambda & - \lambda \\ - 1 & 0 & 0  \right| &= (- 1) \cdot \left| \begin{array}{c c} - 1 & \lambda^ {2} - \lambda - 1 \\ \lambda & - \lambda  \right| \\ &= - \lambda \left| \begin{array}{c c} - 1 & \lambda^ {2} - \lambda - 1 \\ 1 & - 1  \right| &= \lambda \left(\lambda^ {2} - \lambda - 2\right) = \lambda (\lambda - 2) (\lambda + 1). \end{aligned}</equation>A的特征值为2，-1,0,A共有一个正特征值因此，<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>的正惯性指数为1，应选B.

---

**2024年第15题 | 填空题 | 5分**

15. 设实矩阵<equation>A=\left( \begin{array}{cc} a+1 & a \\ a & a \end{array} \right)</equation>，若对任意实向量<equation>\alpha=\binom{x_{1}}{x_{2}}</equation><equation>\beta=\binom{y_{1}}{y_{2}}</equation><equation>(\alpha^{\mathrm{T}}A\beta)^{2}\leqslant\alpha^{\mathrm{T}}A\alpha\cdot\beta^{\mathrm{T}}A\beta</equation>都成立，则 a的取值范围是___

**解析:**解（法一）先将 A通过合同变换化为对角矩阵.令<equation>P=\left( \begin{array}{c c}1&0\\ -1&1 \end{array} \right)</equation>，则<equation>\boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} = \left( \begin{array}{c c} 1 & - 1 \\ 0 & 1 \end{array} \right) \left( \begin{array}{c c} a + 1 & a \\ a & a \end{array} \right) \left( \begin{array}{c c} 1 & 0 \\ - 1 & 1 \end{array} \right) = \left( \begin{array}{c c} 1 & 0 \\ 0 & a \end{array} \right).</equation>令<equation>\gamma_{1}=\binom{w_{1}}{w_{2}}</equation>满足<equation>P\gamma_{1}=\alpha, \gamma_{2}=\binom{z_{1}}{z_{2}}</equation>满足<equation>P\gamma_{2}=\beta.</equation>由于<equation>\alpha, \beta</equation>为任意实向量，故<equation>\gamma_{1},\gamma_{2}</equation>也为任意实向量.于是，<equation>\boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {\beta} = \gamma_ {1} ^ {\mathrm {T}} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} \gamma_ {2} = \left(w _ {1}, w _ {2}\right) \binom {1} {0} \binom {z _ {1}} {z _ {2}} = w _ {1} z _ {1} + a w _ {2} z _ {2},</equation><equation>\boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {\alpha} = \gamma_ {1} ^ {\mathrm {T}} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} \boldsymbol {\gamma} _ {1} = \left(w _ {1}, w _ {2}\right) \binom {1} {0} \binom {0} {a} \binom {w _ {1}} {w _ {2}} = w _ {1} ^ {2} + a w _ {2} ^ {2},</equation><equation>\boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {\beta} = \gamma_ {2} ^ {\mathrm {T}} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} \gamma_ {2} = \left(z _ {1}, z _ {2}\right) \binom {1} {0} \binom {0} {a} \binom {z _ {1}} {z _ {2}} = z _ {1} ^ {2} + a z _ {2} ^ {2}.</equation><equation>\left(\boldsymbol{\alpha}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{\beta}\right)^{2} \leqslant \boldsymbol{\alpha}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{\alpha} \cdot \boldsymbol{\beta}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{\beta}</equation>对任意实向量<equation>\alpha, \beta</equation>恒成立等价于<equation>\left(w_{1}z_{1}+aw_{2}z_{2}\right)^{2} \leqslant \left(w_{1}^{2}+aw_{2}^{2}\right)\left(z_{1}^{2}+az_{2}^{2}\right)</equation>对任意<equation>w_{1}, w_{2}, z_{1}, z_{2}</equation>恒成立.

展开<equation>(w_{1}z_{1} + aw_{2}z_{2})^{2}\leqslant (w_{1}^{2} + aw_{2}^{2})(z_{1}^{2} + az_{2}^{2})</equation>可得，<equation>w _ {1} ^ {2} z _ {1} ^ {2} + a ^ {2} w _ {2} ^ {2} z _ {2} ^ {2} + 2 a w _ {1} z _ {1} w _ {2} z _ {2} \leqslant w _ {1} ^ {2} z _ {1} ^ {2} + a ^ {2} w _ {2} ^ {2} z _ {2} ^ {2} + a w _ {1} ^ {2} z _ {2} ^ {2} + a w _ {2} ^ {2} z _ {1} ^ {2}.</equation>整理（1）式可得<equation>a \left(w_{1} z_{2}-w_{2} z_{1}\right)^{2} \geqslant 0.</equation>对任意<equation>w_{1}, w_{2}, z_{1}, z_{2}</equation>，该式恒成立当且仅当<equation>a \geqslant 0.</equation>因此，<equation>a</equation>的取值范围是<equation>[0, +\infty)</equation>.

（法二）整理<equation>(\alpha^{\mathrm{T}}A\beta)^{2}\leqslant \alpha^{\mathrm{T}}A\alpha \cdot \beta^{\mathrm{T}}A\beta</equation>可得<equation>\alpha^ {\mathrm {T}} A \beta \alpha^ {\mathrm {T}} A \beta - \alpha^ {\mathrm {T}} A \alpha \beta^ {\mathrm {T}} A \beta \leqslant 0, \quad \text {即} \alpha^ {\mathrm {T}} A \left(\beta \alpha^ {\mathrm {T}} - \alpha \beta^ {\mathrm {T}}\right) A \beta \leqslant 0.</equation>计算可得<equation>\boldsymbol {\beta} \boldsymbol {\alpha} ^ {\mathrm {T}} - \alpha \boldsymbol {\beta} ^ {\mathrm {T}} = \left( \begin{array}{c c} x _ {1} y _ {1} & x _ {2} y _ {1} \\ x _ {1} y _ {2} & x _ {2} y _ {2} \end{array} \right) - \left( \begin{array}{c c} x _ {1} y _ {1} & x _ {1} y _ {2} \\ x _ {2} y _ {1} & x _ {2} y _ {2} \end{array} \right) = \left( \begin{array}{c c} 0 & x _ {2} y _ {1} - x _ {1} y _ {2} \\ x _ {1} y _ {2} - x _ {2} y _ {1} & 0 \end{array} \right).</equation>记<equation>z = x_{2}y_{1} - x_{1}y_{2}</equation>，则<equation>\beta \alpha^{\mathrm{T}} - \alpha \beta^{\mathrm{T}} = \left( \begin{array}{cc}0 & z\\ -z & 0 \end{array} \right)</equation>.

计算<equation>A(\beta\alpha^{\mathrm{T}}-\alpha\beta^{\mathrm{T}})A</equation>可得<equation>\begin{aligned} \boldsymbol {A} \left(\boldsymbol {\beta} \boldsymbol {\alpha} ^ {\mathrm {T}} - \boldsymbol {\alpha} \boldsymbol {\beta} ^ {\mathrm {T}}\right) \boldsymbol {A} &= \left( \begin{array}{c c} a + 1 & a \\ a & a  \right) \left( \begin{array}{c c} 0 & z \\ - z & 0  \right) \left( \begin{array}{c c} a + 1 & a \\ a & a  \right) \\ &= \left( \begin{array}{c c} - a z & (a + 1) z \\ - a z & a z  \right) \left( \begin{array}{c c} a + 1 & a \\ a & a  \right) &= \left( \begin{array}{c c} 0 & a z \\ - a z & 0  \right). \end{aligned}</equation>于是，<equation>\begin{aligned} \boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {A} \left(\boldsymbol {\beta} \boldsymbol {\alpha} ^ {\mathrm {T}} - \boldsymbol {\alpha} \boldsymbol {\beta} ^ {\mathrm {T}}\right) \boldsymbol {A} \boldsymbol {\beta} &= \left(x _ {1}, x _ {2}\right) \binom {0} {- a z} \binom {a z} {0} \binom {y _ {1}} {y _ {2}} = \left(- a x _ {2} z, a x _ {1} z\right) \binom {y _ {1}} {y _ {2}} \\ &= a x _ {1} y _ {2} z - a x _ {2} y _ {1} z = - a z ^ {2}. \end{aligned}</equation>对任意<equation>z = x_{2}y_{1} - x_{1}y_{2}, - a z^{2}\leqslant 0</equation>恒成立当且仅当<equation>a\geqslant 0.</equation>因此，<equation>a</equation>的取值范围是<equation>[0, +\infty)</equation>.

---

**2023年第21题 | 解答题 | 12分**

21. (本题满分12分)

已知二次型<equation>f \left(x_{1}, x_{2}, x_{3}\right)=x_{1}^{2}+2 x_{2}^{2}+2 x_{3}^{2}+2 x_{1} x_{2}-2 x_{1} x_{3},</equation><equation>g \left(y_{1}, y_{2}, y_{3}\right)=y_{1}^{2}+y_{2}^{2}+y_{3}^{2}+2 y_{2} y_{3}</equation>I. 求可逆变换<equation>\boldsymbol{x}=\boldsymbol{P}\boldsymbol{y}</equation>，将<equation>f \left(x_{1}, x_{2}, x_{3}\right)</equation>化为<equation>g \left(y_{1}, y_{2}, y_{3}\right)</equation>；

II. 是否存在正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>，将<equation>f \left(x_{1}, x_{2}, x_{3}\right)</equation>化为<equation>g \left(y_{1}, y_{2}, y_{3}\right).</equation>

**答案:**（I）<equation>P=\left( \begin{array}{c c c} 1 & -1 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，可逆变换<equation>\boldsymbol{x}=\boldsymbol{P}\boldsymbol{y}</equation>将<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>化为<equation>g \left( y_{1}, y_{2}, y_{3} \right)</equation>；

（Ⅱ）不存在正交变换<equation>\boldsymbol{x}=Q\boldsymbol{y}</equation>将<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>化为<equation>g \left( y_{1}, y_{2}, y_{3} \right).</equation>

**解析:**解（I）（法一）记<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>对应的对称矩阵为 A，<equation>g \left( y_{1}, y_{2}, y_{3} \right)</equation>对应的对称矩阵为 B，则<equation>f \left( x_{1}, x_{2}, x_{3} \right) = \mathbf{x}^{\mathrm{T}} \mathbf{A} \mathbf{x}, g \left( y_{1}, y_{2}, y_{3} \right) = \mathbf{y}^{\mathrm{T}} \mathbf{B} \mathbf{y}.</equation>由<equation>f(x_{1},x_{2},x_{3})</equation>与<equation>g(y_{1},y_{2},y_{3})</equation>的表达式可知，<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & 1 & - 1 \\ 1 & 2 & 0 \\ - 1 & 0 & 2 \end{array} \right), \quad \boldsymbol {B} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 1 & 1 \end{array} \right).</equation>对A作合同变换，将其化为B.<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & 1 & - 1 \\ 1 & 2 & 0 \\ - 1 & 0 & 2 \end{array} \right) \xrightarrow [ r _ {2} - r _ {1} ]{\text {行 变 换}} \left( \begin{array}{c c c} 1 & 1 & - 1 \\ 0 & 1 & 1 \\ - 1 & 0 & 2 \end{array} \right) \xrightarrow [ c _ {2} - c _ {1} ]{\text {列 变 换}} \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 1 \\ - 1 & 1 & 2 \end{array} \right)</equation><equation>\xrightarrow [ r _ {3} + r _ {1} ]{\text {行 变 换}} \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 1 \\ 0 & 1 & 1 \end{array} \right) \xrightarrow [ c _ {3} + c _ {1} ]{\text {列 变 换}} \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 1 & 1 \end{array} \right) = \boldsymbol {B}.</equation>记录每一次初等列变换所对应的初等矩阵，分别记为<equation>P_{1}, P_{2}</equation><equation>\boldsymbol {P} _ {1} = \left( \begin{array}{c c c} 1 & - 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right), \quad \boldsymbol {P} _ {2} = \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation><equation>\boldsymbol {P} = \boldsymbol {P} _ {1} \boldsymbol {P} _ {2} = \left( \begin{array}{c c c} 1 & - 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} 1 & - 1 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>因此，<equation>\mathbf{P}^{\mathrm{T}}\mathbf{A}\mathbf{P} = \mathbf{B}</equation>，即<equation>\mathbf{x} = \mathbf{P}\mathbf{y}</equation>将<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>化为<equation>g\left(y_{1},y_{2},y_{3}\right).</equation>（法二）由配方法可得<equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = \left(x _ {1} + x _ {2} - x _ {3}\right) ^ {2} + x _ {2} ^ {2} + x _ {3} ^ {2} + 2 x _ {2} x _ {3} = \left(x _ {1} + x _ {2} - x _ {3}\right) ^ {2} + \left(x _ {2} + x _ {3}\right) ^ {2},</equation><equation>g \left(y _ {1}, y _ {2}, y _ {3}\right) = y _ {1} ^ {2} + \left(y _ {2} + y _ {3}\right) ^ {2}.</equation><equation>\text {令} \left\{ \begin{array}{l l} z _ {1} = x _ {1} + x _ {2} - x _ {3}, \\ z _ {2} = x _ {2} + x _ {3}, \\ z _ {3} = x _ {3}, \end{array} \right. \quad \text {则} \left( \begin{array}{l} z _ {1} \\ z _ {2} \\ z _ {3} \end{array} \right) = \left( \begin{array}{c c c} 1 & 1 & - 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right) \left( \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right). \text {由 于} \left| \begin{array}{c c c} 1 & 1 & - 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right| = 1, \text {故} \left( \begin{array}{c c c} 1 & 1 & - 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right) \text {可}</equation>逆.记<equation>P_{1}^{-1}=\left( \begin{array}{c c c}1&1&-1\\ 0&1&1\\ 0&0&1 \end{array} \right),</equation>则可逆变换<equation>\boldsymbol{x}=\boldsymbol{P}_{1}\boldsymbol{z}</equation>将<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>化为规范形<equation>h\left(z_{1},z_{2},z_{3}\right)=z_{1}^{2}+z_{2}^{2},</equation>即<equation>\boldsymbol {P} _ {1} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} _ {1} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>令<equation>\left\{ \begin{array}{l} z_{1}=y_{1},\\ z_{2}=y_{2}+y_{3},\\ z_{3}=y_{3}, \end{array} \right.</equation>则<equation>\left( \begin{array}{l} z_{1} \\ z_{2} \\ z_{3} \end{array} \right)=\left( \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)\left( \begin{array}{l} y_{1} \\ y_{2} \\ y_{3} \end{array} \right).</equation>由于<equation>\left| \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right|=1</equation>故<equation>\left( \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>可逆.记<equation>P_{2}^{-1}=</equation><equation>\left( \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>则可逆变换<equation>\mathbf{y}=\mathbf{P}_{2}\mathbf{z}</equation>将<equation>g(y_{1},y_{2},y_{3})</equation>化为规范形<equation>h(z_{1},z_{2},z_{3})=z_{1}^{2}+z_{2}^{2}</equation>即<equation>\boldsymbol {P} _ {2} ^ {\mathrm {T}} \boldsymbol {B} \boldsymbol {P} _ {2} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>记<equation>\Lambda = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>. 由于<equation>P_{1}^{\mathrm{T}}A P_{1} = \Lambda , P_{2}^{\mathrm{T}}B P_{2} = \Lambda</equation>，故<equation>\boldsymbol {B} = \left(\boldsymbol {P} _ {2} ^ {\mathrm {T}}\right) ^ {- 1} \boldsymbol {\Lambda} \boldsymbol {P} _ {2} ^ {- 1} \xlongequal {\left(\boldsymbol {P} _ {2} ^ {\mathrm {T}}\right) ^ {- 1} = \left(\boldsymbol {P} _ {2} ^ {- 1}\right) ^ {\mathrm {T}}} \left(\boldsymbol {P} _ {2} ^ {- 1}\right) ^ {\mathrm {T}} \boldsymbol {P} _ {1} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} _ {1} \boldsymbol {P} _ {2} ^ {- 1},</equation>即<equation>x = P_{1}P_{2}^{-1}y</equation>将<equation>f(x_{1},x_{2},x_{3})</equation>化为<equation>g(y_{1},y_{2},y_{3})</equation>下面计算<equation>P_{1}</equation><equation>\begin{array}{l} \left(\boldsymbol {P} _ {1} ^ {- 1}, \boldsymbol {E}\right) = \left( \begin{array}{c c c c c c} 1 & 1 & - 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {2} - r _ {3} ]{r _ {1} + r _ {3}} \left( \begin{array}{c c c c c c} 1 & 1 & 0 & 1 & 0 & 1 \\ 0 & 1 & 0 & 0 & 1 & - 1 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} ^ {*} - r _ {2} ^ {*}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 1 & - 1 & 2 \\ 0 & 1 & 0 & 0 & 1 & - 1 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right). \\ \end{array}</equation>于是，<equation>P_{1} = \left( \begin{array}{c c c} 1 & -1 & 2 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{array} \right).</equation>记<equation>P=P_{1} P_{2}^{-1}</equation>，则<equation>\boldsymbol {P} = \left( \begin{array}{c c c} 1 & - 1 & 2 \\ 0 & 1 & - 1 \\ 0 & 0 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} 1 & - 1 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>矩阵<equation>P</equation>即为所求可逆矩阵，使得可逆变换<equation>x = P y</equation>将<equation>f\left(x_{1}, x_{2}, x_{3}\right)</equation>化为<equation>g\left(y_{1}, y_{2}, y_{3}\right)</equation>（Ⅱ）若正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>将<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>化为<equation>g \left( y_{1}, y_{2}, y_{3} \right)</equation>，则<equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = \boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {x} \xlongequal {\boldsymbol {x} = \boldsymbol {Q} \boldsymbol {y}} \boldsymbol {y} ^ {\mathrm {T}} \boldsymbol {Q} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {Q} \boldsymbol {y} = \boldsymbol {y} ^ {\mathrm {T}} \boldsymbol {B} \boldsymbol {y} = g \left(y _ {1}, y _ {2}, y _ {3}\right).</equation>由此可得<equation>B = Q^{1}AQ</equation>. 又因为<equation>Q</equation>为正交矩阵，<equation>Q^{1} = Q^{-1}</equation>，所以<equation>B = Q^{-1}AQ</equation>. 于是，<equation>A</equation>与<equation>B</equation>相似.

由于<equation>\operatorname{tr}(A) = 5, \operatorname{tr}(B) = 3, A</equation>与<equation>B</equation>的迹不相等，故<equation>A</equation>与<equation>B</equation>不相似，从而不存在正交变换<equation>x = Qy</equation>将<equation>f(x_{1}, x_{2}, x_{3})</equation>化为<equation>g(y_{1}, y_{2}, y_{3})</equation>.

---

**2022年第21题 | 解答题 | 12分**

21. （本题满分12分）

设二次型<equation>f(x_{1},x_{2},x_{3}) = \sum_{i=1}^{3}\sum_{j=1}^{3}ijx_{i}x_{j}</equation>.

I. 写出<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>对应的矩阵；

II. 求正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>将<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>化为标准形；

III. 求<equation>f \left( x_{1}, x_{2}, x_{3} \right)=0</equation>的解.

**答案:**（I）<equation>A=\left( \begin{array}{c c c} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 3 & 6 & 9 \end{array} \right) ;</equation>（Ⅱ）<equation>Q=\left( \begin{array}{c c c} \frac{1}{\sqrt{14}} & -\frac{2}{\sqrt{5}} & -\frac{3}{\sqrt{70}} \\ \frac{2}{\sqrt{14}} & \frac{1}{\sqrt{5}} & -\frac{6}{\sqrt{70}} \\ \frac{3}{\sqrt{14}} & 0 & \frac{5}{\sqrt{70}} \end{array} \right)</equation>正交变换<equation>x=Qy</equation>将二次型 f化为标准形<equation>1 4 y_{1}^{2}</equation>；

（Ⅲ）<equation>f\left(x_{1},x_{2},x_{3}\right)=0</equation>的通解可以取为<equation>k_{1}\left( \begin{array}{c}-2\\ 1\\ 0 \end{array} \right)+k_{2}\left( \begin{array}{c}-3\\ 0\\ 1 \end{array} \right)</equation>或<equation>k_{1}\left( \begin{array}{c}-2\\ 1\\ 0 \end{array} \right)+k_{2}\left( \begin{array}{c}-3\\ -6\\ 5 \end{array} \right)</equation>其中<equation>k_{1},k_{2}</equation>为任意常数.

**解析:**解（I）根据二次型<equation>f</equation>的表达式，其对应的对称矩阵<equation>A</equation>的<equation>(i, j)</equation>元<equation>a_{ij} = ij(i, j = 1, 2, 3)</equation>.

因此，<equation>A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 3 & 6 & 9 \end{pmatrix}</equation>.

（II）由第（I）问可知，<equation>A</equation>是一个秩为1，且迹为14的实对称矩阵。由于实对称矩阵必能相似对角化，且相似的矩阵具有相同的秩与迹，故<equation>A</equation>相似于对角矩阵<equation>\begin{pmatrix} 14 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}</equation>.<equation>A</equation>的特征值为<equation>14, 0, 0</equation>.

下面分别计算<equation>A</equation>的属于特征值0和14的特征向量.

考虑<equation>(0E - A)x = 0</equation>.<equation>-A = \begin{pmatrix} -1 & -2 & -3 \\ -2 & -4 & -6 \\ -3 & -6 & -9 \end{pmatrix} \rightarrow \begin{pmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}</equation>.

于是，<equation>-Ax = 0</equation>等价于方程组<equation>x_1 + 2x_2 + 3x_3 = 0</equation>. 分别令<equation>\begin{pmatrix} x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix}</equation>, 可得<equation>\xi_2 = \begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix}, \xi_3 = \begin{pmatrix} -3 \\ 0 \\ 1 \end{pmatrix}</equation>.

由<equation>\xi_2, \xi_3</equation>满足的方程也可知，<equation>\xi_2, \xi_3</equation>均与向量<equation>\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}</equation>正交. 并且，在三维向量空间中，<equation>k \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}</equation>(<equation>k</equation>为任意非零常数) 代表与<equation>\xi_2, \xi_3</equation>均正交的唯一方向. 由于实对称矩阵属于不同特征值的特征向量相互正交，故向量<equation>\xi_1 = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}</equation>即矩阵<equation>A</equation>的属于特征值14的一个特征向量.

将<equation>\xi_1, \xi_2, \xi_3</equation>单位正交. 实际上，由于<equation>\xi_1</equation>与<equation>\xi_2, \xi_3</equation>均正交，故正交的过程只需将<equation>\xi_2, \xi_3</equation>正交.<equation>\beta_1 = \xi_1</equation>,<equation>\beta_2 = \xi_2</equation>,<equation>\beta_3 = \xi_3 - \frac{(\beta_2, \xi_3)}{\|\beta_2\|^2}\beta_2 = \begin{pmatrix} -3 \\ 0 \\ 1 \end{pmatrix} - \frac{6}{5}\begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} -\frac{3}{5} \\ -\frac{6}{5} \\ 1 \end{pmatrix}</equation>.

或者，也可以通过计算<equation>\beta_1 \times \beta_2</equation>得到与<equation>\beta_1, \beta_2</equation>均正交的向量<equation>\beta_3</equation>.<equation>\beta_3 = \beta_1 \times \beta_2 = \begin{pmatrix} i & j & k \\ 1 & 2 & 3 \\ -2 & 1 & 0 \end{pmatrix} = -3i - 6j + 5k</equation>.

将<equation>\beta_1, \beta_2, \beta_3</equation>单位化，可得<equation>\varepsilon_1 = \frac{\beta_1}{\|\beta_1\|} = \frac{1}{\sqrt{14}}\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}, \varepsilon_2 = \frac{\beta_2}{\|\beta_2\|} = \frac{1}{\sqrt{5}}\begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix}, \varepsilon_3 = \frac{\beta_3}{\|\beta_3\|} = \frac{1}{\sqrt{70}}\begin{pmatrix} -3 \\ -6 \\ 5 \end{pmatrix}</equation>.

令<equation>Q = (\varepsilon_1, \varepsilon_2, \varepsilon_3)</equation>，可得<equation>Q^{-1}AQ = Q^T AQ = \begin{pmatrix} 14 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}</equation>，即正交变换<equation>x = Qy</equation>将二次型<equation>f</equation>化为标准形<equation>14y_1^2</equation>.

（III）（法一）由二次型<equation>f(x_1, x_2, x_3)</equation>的表达式可知,<equation>f(x_1, x_2, x_3) = x_1^2 + 4x_2^2 + 9x_3^2 + 4x_1x_2 + 6x_1x_3 + 12x_2x_3 = (x_1 + 2x_2 + 3x_3)^2</equation>.

因此，<equation>f(x_1, x_2, x_3) = 0</equation>当且仅当<equation>x_1 + 2x_2 + 3x_3 = 0</equation>. 由第（II）问的结果可知，该方程组的通解可取为<equation>k_1 \begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix} + k_2 \begin{pmatrix} -3 \\ 0 \\ 1 \end{pmatrix} + k_1 \begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix} + k_2 \begin{pmatrix} -3 \\ -6 \\ 5 \end{pmatrix}</equation>，其中<equation>k_1, k_2</equation>为任意常数.

（法二）根据第（II）问的结果，<equation>f</equation>在正交变换<equation>x = Qy</equation>下的标准形为<equation>14y_1^2</equation>，故当<equation>y_1 = 0</equation>时，<equation>14y_1^2 = 0</equation>. 从而，当<equation>\begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = Q \begin{pmatrix} 0 \\ y_2 \\ y_3 \end{pmatrix}</equation>时，<equation>f(x_1, x_2, x_3) = 0</equation>.

将<equation>\begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} \frac{1}{\sqrt{14}} & -\frac{2}{\sqrt{5}} & -\frac{3}{\sqrt{70}} \\ \frac{2}{\sqrt{14}} & \frac{1}{\sqrt{5}} & -\frac{6}{\sqrt{70}} \\ \frac{3}{\sqrt{14}} & 0 & \frac{5}{\sqrt{70}} \end{pmatrix} \begin{pmatrix} 0 \\ y_2 \\ y_3 \end{pmatrix}</equation>展开可得，<equation>\begin{pmatrix} x_1 = -\frac{2}{\sqrt{5}}y_2 - \frac{3}{\sqrt{70}}y_3, \\ x_2 = \frac{1}{\sqrt{5}}y_2 - \frac{6}{\sqrt{70}}y_3, \\ x_3 = \frac{5}{\sqrt{70}}y_3 \end{pmatrix}</equation>，其中<equation>k_1, k_2</equation>为任意常数.

不妨令<equation>k_1 = \frac{y_2}{\sqrt{5}}, k_2 = \frac{y_3}{\sqrt{70}}</equation>，则<equation>f(x_1, x_2, x_3) = 0</equation>的解可以取为<equation>\begin{pmatrix} x_1 = -2k_1 - 3k_2, \\ x_2 = k_1 - 6k_2, \\ x_3 = 5k_2 \end{pmatrix}</equation>.

---

**2021年第5题 | 选择题 | 5分 | 答案: B**

5. 设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=\left( x_{1}+x_{2} \right)^{2}+\left( x_{2}+x_{3} \right)^{2}-\left( x_{3}-x_{1} \right)^{2}</equation>的正惯性指数与负惯性指数依次为（    ）

A. 2,0 B. 1,1 C. 2,1 D. 1,2

答案: B

**解析:**解（法一）令<equation>\left\{ \begin{array}{l l} y_{1}=x_{1}+x_{2}, \\ y_{2}=x_{2}+x_{3}, \\ y_{3}=x_{3}, \end{array} \right.</equation>则<equation>x_{3}-x_{1}=y_{2}-y_{1}</equation>，且该变换为可逆线性变换.在该变换下，二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>化为<equation>g \left(y _ {1}, y _ {2}, y _ {3}\right) = y _ {1} ^ {2} + y _ {2} ^ {2} - \left(y _ {2} - y _ {1}\right) ^ {2} = 2 y _ {1} y _ {2}.</equation>再令<equation>\left\{ \begin{array}{l l} y_{1} = z_{1} + z_{2}, \\ y_{2} = z_{1} - z_{2}, \\ y_{3} = z_{3}, \end{array} \right.</equation>则<equation>g\left(y_{1}, y_{2}, y_{3}\right)</equation>化为<equation>h \left(z _ {1}, z _ {2}, z _ {3}\right) = 2 \left(z _ {1} + z _ {2}\right) \left(z _ {1} - z _ {2}\right) = 2 z _ {1} ^ {2} - 2 z _ {2} ^ {2}.</equation>因此，<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>的一个标准形为<equation>2z_{1}^{2}-2z_{2}^{2}</equation>，其正、负惯性指数分别为1，1.应选B.

（法二）将<equation>f(x_{1},x_{2},x_{3})</equation>展开可得<equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = 2 x _ {2} ^ {2} + 2 x _ {1} x _ {2} + 2 x _ {2} x _ {3} + 2 x _ {1} x _ {3}.</equation>该二次型对应的矩阵为<equation>A = \left( \begin{array}{c c c} 0 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 0 \end{array} \right)</equation>. 不难发现，<equation>A</equation>的第二行为第一行与第三行的和，故<equation>r(A)\leqslant 2.</equation>又因为<equation>A</equation>有一个2阶非零子式<equation>\left| \begin{array}{c c} 0 & 1 \\ 1 & 2 \end{array} \right|</equation>，所以<equation>r(A)\geqslant 2.</equation>于是，<equation>r(A) = 2.</equation>由于二次型的正、负惯性指数之和等于其对应矩阵的秩，而选项C、D的两数之和均为3，故可排除选项C、D.

另一方面，若 f的负惯性指数为0，则 f非负，即对任意<equation>\left(x_{1},x_{2},x_{3}\right)</equation>，均有<equation>f\left(x_{1},x_{2},x_{3}\right)\geqslant0</equation>但是，<equation>f(1,0,-1)=1+1-4<0</equation>，矛盾.因此，选项A不正确.

根据排除法，应选B.

---

**2021年第21题 | 解答题 | 12分**

21. （本题满分12分）

已知<equation>A = \left( \begin{array}{c c c} a & 1 & -1 \\ 1 & a & -1 \\ -1 & -1 & a \end{array} \right).</equation>I. 求正交矩阵<equation>P</equation>，使得<equation>P^{\mathrm{T}}AP</equation>为对角矩阵；

II. 求正定矩阵<equation>C</equation>，使得<equation>C^{2} = (a + 3)E - A</equation>，其中<equation>E</equation>为3阶单位矩阵.

**答案:**( I )<equation>P=\left( \begin{array}{c c c} -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{3}} \\ 0 & \frac{2}{\sqrt{6}} & \frac{1}{\sqrt{3}} \end{array} \right), P^{\mathrm{T}} A P=\left( \begin{array}{c c c} a-1 & 0 & 0 \\ 0 & a-1 & 0 \\ 0 & 0 & a+2 \end{array} \right);</equation>( II )<equation>C=\left( \begin{array}{c c c} \frac{5}{3} & -\frac{1}{3} & \frac{1}{3} \\ -\frac{1}{3} & \frac{5}{3} & \frac{1}{3} \\ \frac{1}{3} & \frac{1}{3} & \frac{5}{3} \end{array} \right).</equation>

**解析:**解（ I ）计算 A的特征多项式.<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - a & - 1 & 1 \\ - 1 & \lambda - a & 1 \\ 1 & 1 & \lambda - a  \right| \xlongequal {r _ {1} - r _ {2}} \left| \begin{array}{c c c} \lambda - a + 1 & - \lambda + a - 1 & 0 \\ - 1 & \lambda - a & 1 \\ 1 & 1 & \lambda - a  \right| \\ &= (\lambda - a + 1) \left| \begin{array}{c c c} 1 & - 1 & 0 \\ - 1 & \lambda - a & 1 \\ 1 & 1 & \lambda - a  \right| &= (\lambda - a + 1) \left| \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & \lambda - a - 1 & 1 \\ 1 & 2 & \lambda - a  \right| \\ &= (\lambda - a + 1) \left[ (\lambda - a - 1) (\lambda - a) - 2 \right] = (\lambda - a + 1) \left[ (\lambda - a) ^ {2} - (\lambda - a) - 2 \right] \\ &= (\lambda - a + 1) (\lambda - a - 2) (\lambda - a + 1) = (\lambda - a + 1) ^ {2} (\lambda - a - 2). \end{aligned}</equation>A的特征值为<equation>a - 1,a - 1,a + 2</equation>.

分别计算<equation>A</equation>的属于特征值<equation>a - 1, a + 2</equation>的特征向量.

考虑<equation>[(a - 1)E - A]x = 0.</equation><equation>(a - 1) \boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} - 1 & - 1 & 1 \\ - 1 & - 1 & 1 \\ 1 & 1 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & - 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>分别令<equation>\left\{\begin{array}{l l}x_{2}=1,\\ x_{3}=0,\end{array}\right.</equation><equation>\left\{\begin{array}{l l}x_{2}=0,\\ x_{3}=1,\end{array}\right.</equation>可得<equation>\boldsymbol{\xi}_{1}=\left( \begin{array}{c}-1\\ 1\\ 0 \end{array} \right)</equation>与<equation>\boldsymbol{\xi}_{2}=\left( \begin{array}{c}1\\ 0\\ 1 \end{array} \right)</equation>为<equation>[(a-1)\boldsymbol{E}-\boldsymbol{A}]\boldsymbol{x}=\boldsymbol{0}</equation>的两个线性

无关的解，从而<equation>\xi_{1},\xi_{2}</equation>为<equation>A</equation>的属于特征值<equation>a - 1</equation>的两个线性无关的特征向量.

考虑<equation>[(a + 2)E - A]x = 0.</equation><equation>(a + 2) \boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} 2 & - 1 & 1 \\ - 1 & 2 & 1 \\ 1 & 1 & 2 \end{array} \right) \xrightarrow [ r _ {2} + r _ {1} ^ {*} ]{r _ {1} \leftrightarrow r _ {3}} \left( \begin{array}{c c c} 1 & 1 & 2 \\ 0 & 3 & 3 \\ 0 & - 3 & - 3 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 2 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

令<equation>x_{3} = 1</equation>，可得<equation>\xi_{3} = \left( \begin{array}{c} - 1 \\ - 1 \\ 1 \end{array} \right)</equation>为<equation>[(a + 2)E - A]x = 0</equation>的一个解，从而<equation>\xi_{3}</equation>为A的属于特征值<equation>a + 2</equation>的一个特征向量.

将<equation>\boldsymbol{\xi}_{1},\boldsymbol{\xi}_{2},\boldsymbol{\xi}_{3}</equation>施密特正交.由于<equation>\boldsymbol{\xi}_{3}</equation>与<equation>\boldsymbol{\xi}_{1},\boldsymbol{\xi}_{2}</equation>为属于不同特征值的特征向量，<equation>\boldsymbol{\xi}_{3}</equation>与<equation>\boldsymbol{\xi}_{i} ( i=1,2)</equation>相互正交，故只需将<equation>\boldsymbol{\xi}_{1},\boldsymbol{\xi}_{2}</equation>正交.<equation>\boldsymbol {\beta} _ {1} = \boldsymbol {\xi} _ {1} = \left( \begin{array}{c} - 1 \\ 1 \\ 0 \end{array} \right),</equation><equation>\boldsymbol {\beta} _ {2} = \boldsymbol {\xi} _ {2} - \frac {\left(\boldsymbol {\beta} _ {1} , \boldsymbol {\xi} _ {2}\right)}{\| \boldsymbol {\beta} _ {1} \| ^ {2}} \boldsymbol {\beta} _ {1} = \left( \begin{array}{c} 1 \\ 0 \\ 1 \end{array} \right) - \frac {(- 1)}{2} \left( \begin{array}{c} - 1 \\ 1 \\ 0 \end{array} \right) = \frac {1}{2} \left( \begin{array}{c} 1 \\ 1 \\ 2 \end{array} \right),</equation><equation>\boldsymbol {\beta} _ {3} = \boldsymbol {\xi} _ {3} = \left( \begin{array}{c} - 1 \\ - 1 \\ 1 \end{array} \right).</equation>将<equation>\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3}</equation>单位化.<equation>\boldsymbol {\varepsilon} _ {1} = \frac {\boldsymbol {\beta} _ {1}}{\| \boldsymbol {\beta} _ {1} \|} = \frac {1}{\sqrt {2}} \left( \begin{array}{c} - 1 \\ 1 \\ 0 \end{array} \right), \quad \boldsymbol {\varepsilon} _ {2} = \frac {\boldsymbol {\beta} _ {2}}{\| \boldsymbol {\beta} _ {2} \|} = \frac {1}{\sqrt {6}} \left( \begin{array}{c} 1 \\ 1 \\ 2 \end{array} \right), \quad \boldsymbol {\varepsilon} _ {3} = \frac {\boldsymbol {\beta} _ {3}}{\| \boldsymbol {\beta} _ {3} \|} = \frac {1}{\sqrt {3}} \left( \begin{array}{c} - 1 \\ - 1 \\ 1 \end{array} \right).</equation><equation>\text {令} \boldsymbol {P} = \left(\varepsilon_ {1}, \varepsilon_ {2}, \varepsilon_ {3}\right) = \left( \begin{array}{c c c} - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {6}} & - \frac {1}{\sqrt {3}} \\ \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {6}} & - \frac {1}{\sqrt {3}} \\ 0 & \frac {2}{\sqrt {6}} & \frac {1}{\sqrt {2}} \end{array} \right), \text {则} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} = \left( \begin{array}{c c c} a - 1 & 0 & 0 \\ 0 & a - 1 & 0 \\ 0 & 0 & a + 2 \end{array} \right).</equation>（Ⅱ）由第（I）问可得，<equation>P^{\mathrm{T}} A P=\left( \begin{array}{c c c} a-1 & 0 & 0 \\ 0 & a-1 & 0 \\ 0 & 0 & a+2 \end{array} \right)</equation>，则<equation>A=P\left( \begin{array}{c c c} a-1 & 0 & 0 \\ 0 & a-1 & 0 \\ 0 & 0 & a+2 \end{array} \right) P^{\mathrm{T}}.</equation><equation>\begin{aligned} (a + 3) \boldsymbol {E} - \boldsymbol {A} &= \boldsymbol {P} (a + 3) \boldsymbol {E P} ^ {\mathrm {T}} - \boldsymbol {P} \left( \begin{array}{c c c} a - 1 & 0 & 0 \\ 0 & a - 1 & 0 \\ 0 & 0 & a + 2  \right) \boldsymbol {P} ^ {\mathrm {T}} \\ &= \boldsymbol {P} \left[ \left( \begin{array}{c c c} a + 3 & 0 & 0 \\ 0 & a + 3 & 0 \\ 0 & 0 & a + 3  \right) - \left( \begin{array}{c c c} a - 1 & 0 & 0 \\ 0 & a - 1 & 0 \\ 0 & 0 & a + 2  \right) \right] \boldsymbol {P} ^ {\mathrm {T}} \\ &= \boldsymbol {P} \left( \begin{array}{c c c} 4 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 1  \right) \boldsymbol {P} ^ {\mathrm {T}} &= \boldsymbol {P} \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1  \right) \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {P} \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1  \right) \boldsymbol {P} ^ {\mathrm {T}}. \end{aligned}</equation>取<equation>C = P\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right) P^{\mathrm{T}}</equation>，则<equation>C</equation>的特征值均为正，从而正定，且<equation>C^{2} = (a + 3)E - A.</equation><equation>\begin{aligned} \boldsymbol {C} &= \left( \begin{array}{c c c} - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {6}} & - \frac {1}{\sqrt {3}} \\ \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {6}} & - \frac {1}{\sqrt {3}} \\ 0 & \frac {2}{\sqrt {6}} & \frac {1}{\sqrt {3}}  \right) \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1  \right) \left( \begin{array}{c c c} - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {2}} & 0 \\ \frac {1}{\sqrt {6}} & \frac {1}{\sqrt {6}} & \frac {2}{\sqrt {6}} \\ - \frac {1}{\sqrt {3}} & - \frac {1}{\sqrt {3}} & \frac {1}{\sqrt {3}}  \right) \\ &= \left( \begin{array}{c c c} - \sqrt {2} & \frac {2}{\sqrt {6}} & - \frac {1}{\sqrt {3}} \\ \sqrt {2} & \frac {2}{\sqrt {6}} & - \frac {1}{\sqrt {3}} \\ 0 & \frac {4}{\sqrt {6}} & \frac {1}{\sqrt {3}}  \right) \left( \begin{array}{c c c} - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {2}} & 0 \\ \frac {1}{\sqrt {6}} & \frac {1}{\sqrt {6}} & \frac {2}{\sqrt {6}} \\ - \frac {1}{\sqrt {3}} & - \frac {1}{\sqrt {3}} & \frac {1}{\sqrt {3}}  \right) &= \left( \begin{array}{c c c} \frac {5}{3} & - \frac {1}{3} & \frac {1}{3} \\ - \frac {1}{3} & \frac {5}{3} & \frac {1}{3} \\ \frac {1}{3} & \frac {1}{3} & \frac {5}{3}  \right). \end{aligned}</equation>

---

**2020年第20题 | 解答题 | 11分**

20. (本题满分11分)

设二次型<equation>f \left( x_{1}, x_{2} \right)=x_{1}^{2}-4 x_{1} x_{2}+4 x_{2}^{2}</equation>经正交变换<equation>\binom{x_{1}}{x_{2}}=Q \binom{y_{1}}{y_{2}}</equation>化为二次型<equation>g \left( y_{1}, y_{2} \right)=a y_{1}^{2}+4 y_{1} y_{2}+b y_{2}^{2}</equation>其中<equation>a \geqslant b</equation>.

I. 求 a,b的值;

II. 求正交矩阵 Q.

**答案:**（ I ）<equation>a=4,b=1;</equation>（Ⅱ）<equation>Q = \left( \begin{array}{c c} - \frac{4}{5} & \frac{3}{5} \\ \frac{3}{5} & \frac{4}{5} \end{array} \right), f \left( x_{1}, x_{2} \right)</equation>经过正交变换<equation>\binom{x_1}{x_2} = Q\binom{y_1}{y_2}</equation>化为二次型<equation>g \left( y_{1}, y_{2} \right).</equation>

**解析:**解（I）写出二次型<equation>f ( x_{1}, x_{2} )=x_{1}^{2}-4 x_{1} x_{2}+4 x_{2}^{2}</equation>对应的矩阵A，二次型<equation>g ( y_{1}, y_{2} )=a y_{1}^{2}+</equation><equation>4 y_{1} y_{2}+b y_{2}^{2}</equation>对应的矩阵B.<equation>\boldsymbol {A} = \left( \begin{array}{c c} 1 & - 2 \\ - 2 & 4 \end{array} \right), \quad \boldsymbol {B} = \left( \begin{array}{c c} a & 2 \\ 2 & b \end{array} \right).</equation>由于正交变换也是相似变换，故<equation>A</equation>与<equation>B</equation>相似。又因为相似的矩阵具有相同的迹与行列式，所以<equation>\left\{ \begin{array}{l} a + b = 5, \\ a b = 4. \end{array} \right.</equation>由<equation>a\geqslant b</equation>可确定<equation>\left\{ \begin{array}{l l} a = 4, \\ b = 1. \end{array} \right.</equation>（Ⅱ）由第（I）问可知，<equation>A=\left( \begin{array}{c c}1&-2\\ -2&4 \end{array} \right), B=\left( \begin{array}{c c}4&2\\ 2&1 \end{array} \right).</equation>计算 A和B的特征多项式可得<equation>|\lambda E - A| = \left| \begin{array}{cc}\lambda -1 & 2\\ 2 & \lambda -4 \end{array} \right| = \lambda (\lambda -5)</equation>.于是A和B的特征值为5和0.分别计算A，B的特征向量.

计算<equation>A</equation>的属于特征值5的特征向量.

考虑（5E-A）x=0.<equation>5 E - A = \left( \begin{array}{c c} 4 & 2 \\ 2 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c} 2 & 1 \\ 0 & 0 \end{array} \right).</equation>于是，<equation>r ( 5 E - A ) = 1</equation>，求得<equation>\boldsymbol{\xi}_{1}=(-1,2)^{\mathrm{T}}</equation>为<equation>( 5 E-A ) x=0</equation>的一个基础解系.<equation>(-1,2)^{\mathrm{T}}</equation>为A的属于特征值5的一个特征向量.

计算<equation>A</equation>的属于特征值0的特征向量.

考虑（0E-A）x=0.<equation>- \boldsymbol {A} = \left( \begin{array}{c c} - 1 & 2 \\ 2 & - 4 \end{array} \right) \rightarrow \left( \begin{array}{c c} - 1 & 2 \\ 0 & 0 \end{array} \right).</equation>于是，<equation>r ( 0 E - A ) = 1</equation>，求得<equation>\boldsymbol{\xi}_{2}=(2,1)^{\mathrm{T}}</equation>为<equation>( 0 E-A ) x=0</equation>的一个基础解系.<equation>( 2,1)^{\mathrm{T}}</equation>为A的属于特征值0的一个特征向量.

取<equation>P_{1} = \left( \begin{array}{cc} -1 & 2 \\ 2 & 1 \end{array} \right)</equation>，则<equation>P_{1}^{-1} A P_{1} = \left( \begin{array}{cc} 5 & 0 \\ 0 & 0 \end{array} \right)</equation>.

计算<equation>B</equation>的属于特征值5的特征向量.

考虑（5E-B）x=0.<equation>5 E - B = \left( \begin{array}{c c} 1 & - 2 \\ - 2 & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c} 1 & - 2 \\ 0 & 0 \end{array} \right).</equation>于是，<equation>r ( 5 E-B )=1</equation>，求得<equation>\boldsymbol{\eta}_{1}=(2,1)^{\mathrm{T}}</equation>为（5E-B）<equation>\boldsymbol{x}=\mathbf{0}</equation>的一个基础解系. （2，1）<equation>^{\mathrm{T}}</equation>为B的属于特征值5的一个特征向量.

计算<equation>B</equation>的属于特征值0的特征向量.

考虑（0E-B）x=0.<equation>- \boldsymbol {B} = \left( \begin{array}{c c} - 4 & - 2 \\ - 2 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c} 2 & 1 \\ 0 & 0 \end{array} \right).</equation>于是，<equation>r ( 0 E-B )=1</equation>，求得<equation>\boldsymbol{\eta}_{2}=(-1,2)^{\mathrm{T}}</equation>为<equation>( 0 E-B ) \boldsymbol{x}=\mathbf{0}</equation>的一个基础解系.<equation>(-1,2)^{\mathrm{T}}</equation>为B的属于特征值0的一个特征向量.

取<equation>P_{2} = \left( \begin{array}{cc}2 & -1\\ 1 & 2 \end{array} \right)</equation>，则<equation>P_{2}^{-1}B P_{2} = \left( \begin{array}{cc}5 & 0\\ 0 & 0 \end{array} \right).</equation>由于<equation>B = P_{2}P_{1}^{-1}AP_{1}P_{2}^{-1}</equation>，故取<equation>Q = P_{1}P_{2}^{-1}</equation>，则<equation>Q^{-1}AQ = B.</equation>计算得<equation>P_{2}^{-1}=\frac{1}{5}\left( \begin{array}{cc}2&1\\ -1&2 \end{array} \right)</equation>，则<equation>Q=\frac{1}{5}\left( \begin{array}{cc}-1&2\\ 2&1 \end{array} \right)\left( \begin{array}{cc}2&1\\ -1&2 \end{array} \right)=\left( \begin{array}{cc}-\frac{4}{5}&\frac{3}{5}\\ \frac{3}{5}&\frac{4}{5} \end{array} \right).</equation>并且，Q已经是正交矩阵，无需再单位正交化.

因此，<equation>Q = \left( \begin{array}{c c} - \frac{4}{5} & \frac{3}{5} \\ \frac{3}{5} & \frac{4}{5} \end{array} \right), f(x_{1}, x_{2})</equation>经过正交变换<equation>\binom{x_1}{x_2} = Q\binom{y_1}{y_2}</equation>化为二次型<equation>g(y_1, y_2)</equation>.

---

**2019年第5题 | 选择题 | 4分 | 答案: C**

5. 设 A是3阶实对称矩阵，E是3阶单位矩阵.若<equation>A^{2}+A=2 E</equation>，且<equation>|A|=4</equation>，则二次型<equation>x^{\mathrm{T}} A x</equation>的规范形为（    )

A.<equation>y_{1}^{2}+y_{2}^{2}+y_{3}^{2}</equation>B.<equation>y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>C.<equation>y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>D.<equation>-y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>

答案: C

**解析:**解 设<equation>\lambda</equation>为 A的一个特征值，<equation>\alpha</equation>为属于特征值<equation>\lambda</equation>的特征向量.

由<equation>A^{2}+A=2 E</equation>可得<equation>\left(\lambda^{2}+\lambda-2\right)\alpha=0</equation>. 由于<equation>\alpha</equation>为非零向量，故<equation>\lambda^{2}+\lambda-2=0</equation>. 解得<equation>\lambda=1</equation>或<equation>\lambda=-2</equation>. A的特征值只能取1和-2.

又因为<equation>| A |=4</equation>，所以 A的特征值应为-2，-2，1.因此，二次型<equation>x^{\mathrm{T}} A x</equation>的正惯性指数为1，负惯性指数为2.四个选项中，只有<equation>y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>满足该性质.应选C.

---

**2018年第20题 | 解答题 | 11分**

20. (本题满分11分)

设实二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=\left( x_{1}-x_{2}+x_{3} \right)^{2}+\left( x_{2}+x_{3} \right)^{2}+\left( x_{1}+a x_{3} \right)^{2}</equation>其中 a是参数.

I. 求<equation>f \left( x_{1}, x_{2}, x_{3} \right)=0</equation>的解；

II. 求<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>的规范形.

**答案:**（I）当 a≠2时，<equation>f ( x_{1}, x_{2}, x_{3} )=0</equation>的解为<equation>\left( x_{1}, x_{2}, x_{3}\right)^{\mathrm{T}}=\left( 0,0,0\right)^{\mathrm{T}}</equation>；当 a=2时，<equation>f \left( x_{1}, x_{2}, x_{3}\right)=0</equation>的解为<equation>\left( x_{1}, x_{2}, x_{3}\right)^{\mathrm{T}}=k \left( -2,-1,1\right)^{\mathrm{T}}</equation>其中 k为任意常数.

（Ⅱ）当 a≠2时，f的规范形为<equation>f=y_{1}^{2}+y_{2}^{2}+y_{3}^{2}</equation>；当 a=2时，f的规范形为<equation>f=z_{1}^{2}+z_{2}^{2}.</equation>

**解析:**解（I）<equation>f \left(x_{1}, x_{2}, x_{3}\right)=0</equation>当且仅当<equation>\left\{ \begin{array}{l l} x_{1}-x_{2}+x_{3}=0, \\ x_{2}+x_{3}=0, \\ x_{1}+a x_{3}=0. \end{array} \right.</equation>记<equation>A</equation>为该方程组的系数矩阵. 对<equation>A</equation>作初等行变换.<equation>A = \left( \begin{array}{c c c} 1 & - 1 & 1 \\ 0 & 1 & 1 \\ 1 & 0 & a \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c} 1 & - 1 & 1 \\ 0 & 1 & 1 \\ 0 & 1 & a - 1 \end{array} \right) \xrightarrow {r _ {1} + r _ {2}} \left( \begin{array}{c c c} 1 & 0 & 2 \\ 0 & 1 & 1 \\ 0 & 0 & a - 2 \end{array} \right).</equation><equation>\left(r _ {i} ^ {*}\right)</equation>当<equation>a\neq 2</equation>时，<equation>r(\mathbf{A}) = 3</equation>，方程组只有零解.

当<equation>a = 2</equation>时，<equation>r(A) = 2.</equation>方程组的基础解系仅包含一个向量.取<equation>x_{3}</equation>为自由变元，令<equation>x_{3} = 1</equation>，解得<equation>(x_{1},x_{2},x_{3})^{\mathrm{T}} = (-2,-1,1)^{\mathrm{T}}</equation>为该方程组的一个基础解系.

因此，当<equation>a\neq 2</equation>时，<equation>f ( x_{1}, x_{2}, x_{3} )=0</equation>的解为<equation>( x_{1}, x_{2}, x_{3} )^{\mathrm{T}}=(0,0,0)^{\mathrm{T}}</equation>；当<equation>a=2</equation>时，<equation>f ( x_{1}, x_{2}, x_{3} )=0</equation>的解为<equation>( x_{1}, x_{2}, x_{3} )^{\mathrm{T}}=k (-2,-1,1)^{\mathrm{T}}</equation>，其中k为任意常数.

（Ⅱ）由<equation>f(x_{1},x_{2},x_{3})</equation>的表达式知，<equation>f(x_{1},x_{2},x_{3})\geqslant 0.</equation>当 a≠2时，由第（I）问可知，<equation>f ( x_{1}, x_{2}, x_{3} )=0</equation>只有零解，f为正定二次型.因此，当 a≠2时， f的规范形为<equation>f=y_{1}^{2}+y_{2}^{2}+y_{3}^{2}.</equation>当 a = 2时，f不满秩.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= \left(x _ {1} - x _ {2} + x _ {3}\right) ^ {2} + \left(x _ {2} + x _ {3}\right) ^ {2} + \left(x _ {1} + 2 x _ {3}\right) ^ {2} \\ &= 2 x _ {1} ^ {2} + 2 x _ {2} ^ {2} + 6 x _ {3} ^ {2} - 2 x _ {1} x _ {2} + 6 x _ {1} x _ {3}. \end{aligned}</equation>记<equation>f</equation>对应的对称矩阵为<equation>B = \left( \begin{array}{c c c} 2 & -1 & 3 \\ -1 & 2 & 0 \\ 3 & 0 & 6 \end{array} \right)</equation>.

下面用三种方法求 f的规范形.

（法一）由<equation>f(x_{1},x_{2},x_{3})\geqslant 0</equation>可知<equation>f</equation>的负惯性指数为0（否则，若规范形有负系数，不妨设规范形为<equation>f = y_{1}^{2} + y_{2}^{2} - y_{3}^{2}</equation>，取<equation>(y_{1},y_{2},y_{3}) = (0,0,1)</equation>，则<equation>f(y_{1},y_{2},y_{3}) = -1 < 0</equation>，矛盾).由于B的秩等于f的正、负惯性指数之和，故<equation>f</equation>的正惯性指数等于<equation>r(B)</equation>.

计算<equation>| B |</equation>得<equation>| B |=0</equation>，故<equation>r ( B ) \leqslant2</equation>.又因为B有一个2阶子式<equation>\left| \begin{array}{c c} {2} & {-1} \\ {-1} & {2} \end{array} \right|=3\neq0</equation>，所以<equation>r ( B ) \geqslant2.</equation>因此，<equation>r ( B )=2.</equation>综上所述，<equation>f</equation>的正惯性指数为2，负惯性指数为0.<equation>f</equation>的规范形为<equation>f = z_{1}^{2} + z_{2}^{2}</equation>.

（法二）计算<equation>B</equation>的特征值，从而得到<equation>f</equation>的正、负惯性指数.

计算 B的特征多项式.<equation>| \lambda E - B | = \left| \begin{array}{c c c} \lambda - 2 & 1 & - 3 \\ 1 & \lambda - 2 & 0 \\ - 3 & 0 & \lambda - 6 \end{array} \right| = \lambda \left(\lambda^ {2} - 1 0 \lambda + 1 8\right).</equation>解<equation>\lambda^{2}-1 0 \lambda+1 8=0</equation>可得<equation>\lambda_{1,2}=\frac{1 0 \pm \sqrt{1 0 0}-7 2}{2}=5 \pm \sqrt{7}.</equation>由于<equation>5+\sqrt{7}>0, 5-\sqrt{7}>0</equation>故f有两个正特征值，一个零特征值，从而f的正惯性指数为2，负惯性指数为0.

因此，<equation>f</equation>的规范形为<equation>f = z_{1}^{2} + z_{2}^{2}</equation>.

（法三）配方法.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= 2 x _ {1} ^ {2} + 2 x _ {2} ^ {2} + 6 x _ {3} ^ {2} - 2 x _ {1} x _ {2} + 6 x _ {1} x _ {3} = 2 \left(x _ {1} ^ {2} - x _ {1} x _ {2} + 3 x _ {1} x _ {3}\right) + 2 x _ {2} ^ {2} + 6 x _ {3} ^ {2} \\ &= 2 \left(x _ {1} - \frac {x _ {2}}{2} + \frac {3}{2} x _ {3}\right) ^ {2} + \frac {3}{2} x _ {2} ^ {2} - \frac {9}{2} x _ {3} ^ {2} + 3 x _ {2} x _ {3} + 6 x _ {3} ^ {2} \\ &= 2 \left(x _ {1} - \frac {x _ {2}}{2} + \frac {3}{2} x _ {3}\right) ^ {2} + \frac {3}{2} \left(x _ {2} + x _ {3}\right) ^ {2}. \end{aligned}</equation>令<equation>\left\{ \begin{array}{l l} z_{1}=\sqrt{2}\left(x_{1}-\frac{x_{2}}{2}+\frac{3}{2} x_{3}\right), \\ z_{2}=\sqrt{\frac{3}{2}}\left(x_{2}+x_{3}\right), \\ z_{3}=x_{3}, \end{array} \right.</equation>则<equation>f\left(z_{1},z_{2},z_{3}\right)=z_{1}^{2}+z_{2}^{2}.</equation>因此 f的规范形为<equation>f=z_{1}^{2}+z_{2}^{2}.</equation>因此，<equation>f</equation>的规范形为<equation>f = z_{1}^{2} + z_{2}^{2}</equation>.

---

**2017年第21题 | 解答题 | 11分**

21. (本题满分11分)

设二次型<equation>f \left(x_{1}, x_{2}, x_{3}\right)=2 x_{1}^{2}-x_{2}^{2}+a x_{3}^{2}+2 x_{1} x_{2}-8 x_{1} x_{3}+2 x_{2} x_{3}</equation>在正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>下的标准形为<equation>\lambda_{1} y_{1}^{2}+\lambda_{2} y_{2}^{2}</equation>求 a的值及一个正交矩阵 Q.

**答案:**a=2，<equation>Q=\left( \begin{array}{c c c} -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \\ 0 & -\frac{1}{\sqrt{3}} & \frac{2}{\sqrt{6}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \end{array} \right)</equation>，且<equation>Q^{\mathrm{T}}AQ=\left( \begin{array}{c c c} 6 & 0 & 0 \\ 0 & -3 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>，即f在正交变换 x = Qy下的标准

形为<equation>f = 6y_{1}^{2} - 3y_{2}^{2}</equation>.

**解析:**记二次型<equation>f</equation>对应的实对称矩阵为<equation>A</equation>，则<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 2 & 1 & - 4 \\ 1 & - 1 & 1 \\ - 4 & 1 & a \end{array} \right).</equation>由于f在正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>下的标准形为<equation>\lambda_{1}y_{1}^{2}+\lambda_{2}y_{2}^{2}</equation>，故A的特征值为<equation>\lambda_{1},\lambda_{2},0.</equation>从而<equation>|\boldsymbol{A}|=0.</equation>计算A的行列式得<equation>| A | = - 3 a + 6.</equation>因此，<equation>a = 2</equation>，<equation>A = \left( \begin{array}{c c c} 2 & 1 & -4 \\ 1 & -1 & 1 \\ -4 & 1 & 2 \end{array} \right)</equation>计算 A的特征多项式得<equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda - 2 & - 1 & 4 \\ - 1 & \lambda + 1 & - 1 \\ 4 & - 1 & \lambda - 2 \end{array} \right| = \lambda^ {3} - 3 \lambda^ {2} - 1 8 \lambda = \lambda (\lambda - 6) (\lambda + 3).</equation>于是，<equation>\boldsymbol{A}</equation>的3个特征值分别为6，-3，0.

当<equation>\lambda=6</equation>时，<equation>\begin{array}{l} 6 E - A = \left( \begin{array}{c c c} 4 & - 1 & 4 \\ - 1 & 7 & - 1 \\ 4 & - 1 & 4 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c} 4 & - 1 & 4 \\ - 1 & 7 & - 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} + 4 r _ {2}} \left( \begin{array}{c c c} 0 & 1 & 0 \\ - 1 & 7 & - 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} - 7 r _ {1} ^ {* *}} \frac {1}{r _ {2} ^ {*} \times (- 1)} \left( \begin{array}{c c c} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）<equation>(6E - A)x = 0</equation>的一个基础解系为<equation>\eta_1 = (-1,0,1)^{\mathrm{T}}.</equation>当<equation>\lambda=-3</equation>时，<equation>\begin{array}{l} - 3 E - A = \left( \begin{array}{c c c} - 5 & - 1 & 4 \\ - 1 & - 2 & - 1 \\ 4 & - 1 & - 5 \end{array} \right) \xrightarrow [ r _ {3} ^ {*} - r _ {2} ]{r _ {3} + r _ {1}} \left( \begin{array}{c c c} - 5 & - 1 & 4 \\ - 1 & - 2 & - 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {2} \times (- 1) ]{r _ {1} - 5 r _ {2}} \left( \begin{array}{c c c} 0 & 9 & 9 \\ 1 & 2 & 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow [ r _ {2} ^ {*} - r _ {1} ^ {* *} ]{r _ {1} ^ {*} \times \frac {1}{9}} \left( \begin{array}{c c c} 0 & 1 & 1 \\ 1 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation><equation>(-3E - A)x = 0</equation>的一个基础解系为<equation>\eta_2 = (1, -1, 1)^{\mathrm{T}}.</equation>当<equation>\lambda=0</equation>时，<equation>\begin{array}{l} 0 E - A = \left( \begin{array}{c c c} - 2 & - 1 & 4 \\ - 1 & 1 & - 1 \\ 4 & - 1 & - 2 \end{array} \right) \xrightarrow {r _ {3} + r _ {1}} \frac {r _ {3} ^ {*} + 2 r _ {2}}{r _ {3} ^ {*} + 2 r _ {2}} \left( \begin{array}{c c c} - 2 & - 1 & 4 \\ - 1 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} - 2 r _ {2}} \left( \begin{array}{c c c} 0 & 1 & - 2 \\ - 1 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} \times (- 1) + r _ {1} ^ {* *}} \left( \begin{array}{c c c} 0 & 1 & - 2 \\ 1 & 0 & - 1 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation><equation>(0E - A)x = 0</equation>的一个基础解系为<equation>\eta_3 = (1,2,1)^{\mathrm{T}}.</equation>由于实对称矩阵对应于不同特征值的特征向量相互正交，故只需要将所得特征向量单位化.<equation>\boldsymbol{\eta}_{1},\boldsymbol{\eta}_{2},\boldsymbol{\eta}_{3}</equation>分别单位化，作为Q的列向量，得正交矩阵<equation>Q=\left( \begin{array}{c c c} -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \\ 0 & -\frac{1}{\sqrt{3}} & \frac{2}{\sqrt{6}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \end{array} \right)</equation>，且<equation>Q^{\mathrm{T}}AQ=</equation><equation>\left( \begin{array}{c c c} 6 & 0 & 0 \\ 0 & -3 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>，即<equation>f</equation>在正交变换<equation>\boldsymbol{x} = Q\boldsymbol{y}</equation>下的标准形为<equation>f = 6y_{1}^{2} - 3y_{2}^{2}</equation>.

---

**2016年第6题 | 选择题 | 4分 | 答案: B**

6. 设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=x_{1}^{2}+x_{2}^{2}+x_{3}^{2}+4 x_{1} x_{2}+4 x_{1} x_{3}+4 x_{2} x_{3}</equation>，则<equation>f \left( x_{1}, x_{2}, x_{3} \right)=2</equation>在空间直角坐标下表示的二次曲面为（    ）

A. 单叶双曲面 B. 双叶双曲面 C. 椭球面 D. 柱面

答案: B

**解析:**解 二次型<equation>f</equation>对应的矩阵为<equation>A = \left( \begin{array}{lll}1 & 2 & 2\\ 2 & 1 & 2\\ 2 & 2 & 1 \end{array} \right)</equation>，则矩阵<equation>A</equation>的特征多项式为<equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda - 1 & - 2 & - 2 \\ - 2 & \lambda - 1 & - 2 \\ - 2 & - 2 & \lambda - 1 \end{array} \right| = (\lambda + 1) ^ {2} (\lambda - 5),</equation>从而矩阵 A的特征值为<equation>\lambda_{1}=\lambda_{2}=-1,\lambda_{3}=5</equation>.于是<equation>f(x_{1},x_{2},x_{3})=2</equation>在空间直角坐标下表示的二次曲面在坐标系的正交变换下可化为二次曲面<equation>-y_{1}^{2}-y_{2}^{2}+5y_{3}^{2}=2</equation>即<equation>\frac{5y_{3}^{2}}{2}-\frac{y_{1}^{2}}{2}-\frac{y_{2}^{2}}{2}=1.</equation>对照上述表格可知，所求二次曲面为双叶双曲面，应选B.

---

**2015年第6题 | 选择题 | 4分 | 答案: A**

6. 设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>在正交变换<equation>x=P y</equation>下的标准形为<equation>2 y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>其中<equation>P=(e_{1}, e_{2}, e_{3})</equation>.若<equation>Q=(e_{1},-e_{3},e_{2})</equation>则<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>在正交变换<equation>x=Q y</equation>下的标准形为（    )

A.<equation>2 y_{1}^{2}-y_{2}^{2}+y_{3}^{2}</equation>B.<equation>2 y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>C.<equation>2 y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>D.<equation>2 y_{1}^{2}+y_{2}^{2}+y_{3}^{2}</equation>

答案: A

**解析:**解（法一）由题设知，二次型<equation>f ( x_{1}, x_{2}, x_{3} )</equation>对应的对称矩阵 A满足<equation>P^{\mathrm{T}} A P=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -1 \end{array} \right).</equation>又由题设，<equation>Q=P\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{array} \right)</equation>，故<equation>Q^{\mathrm{T}} A Q=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{array} \right)\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -1 \end{array} \right)\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{array} \right)=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>因此，<equation>f \left(x_{1}, x_{2}, x_{3}\right)</equation>在<equation>\mathbf{x}=Q\mathbf{y}</equation>下的标准形为<equation>f=2y_{1}^{2}-y_{2}^{2}+y_{3}^{2}</equation>应选A.

（法二）由题设知，二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>在正交变换<equation>\boldsymbol{x}=\boldsymbol{P}\boldsymbol{y}</equation>下的标准形为<equation>f=2 y_{1}^{2}+y_{2}^{2}-y_{3}^{2}.</equation>因此，该二次型所对应的对称矩阵A的特征值为2，1，-1，而<equation>e_{1}, e_{2}, e_{3}</equation>分别为属于特征值2，1，-1的特征向量.

若<equation>Q=\left(e_{1},-e_{3},e_{2}\right)</equation>，则由<equation>A\left(-e_{3}\right)=-Ae_{3}=-\left(-e_{3}\right)</equation>可知<equation>-e_{3}</equation>也为属于特征值-1的特征向量，故<equation>Q^{\mathrm{T}}AQ=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{array} \right). f \left( x_{1}, x_{2}, x_{3} \right)</equation>在<equation>\boldsymbol{x}=Q\boldsymbol{y}</equation>下的标准形为<equation>f=2 y_{1}^{2}-y_{2}^{2}+y_{3}^{2}.</equation>应选A.

---

**2014年第13题 | 填空题 | 4分**

13. 设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=x_{1}^{2}-x_{2}^{2}+2 a x_{1} x_{3}+4 x_{2} x_{3}</equation>的负惯性指数为1，则 a的取值范围是 ___.

**解析:**解 （法一）用配方法将原二次型化为标准形.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= \left(x _ {1} + a x _ {3}\right) ^ {2} - a ^ {2} x _ {3} ^ {2} - \left(x _ {2} - 2 x _ {3}\right) ^ {2} + 4 x _ {3} ^ {2} \\ &= \left(x _ {1} + a x _ {3}\right) ^ {2} - \left(x _ {2} - 2 x _ {3}\right) ^ {2} + \left(4 - a ^ {2}\right) x _ {3} ^ {2}. \end{aligned}</equation>因此，若二次型<equation>f(x_{1},x_{2},x_{3})</equation>的负惯性指数为1，则<equation>4 - a^{2}\geqslant 0</equation>，即<equation>a\in [-2,2]</equation>（法二）写出二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>对应的对称矩阵<equation>A.</equation><equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & 0 & a \\ 0 & - 1 & 2 \\ a & 2 & 0 \end{array} \right).</equation>计算<equation>A</equation>的行列式得，<equation>|A| = a^{2} - 4.</equation>A的迹等于零，说明A的特征值之和为零.

下面我们证明，当3阶非零实对称矩阵<equation>A</equation>的迹为零时，<equation>A</equation>的负惯性指数为1等价于<equation>|A| \leqslant 0.</equation>当3阶非零实对称矩阵<equation>A</equation>的迹为零时，由<equation>A</equation>的负惯性指数为1可知，<equation>A</equation>的特征值可能为两正、一负，或者一正、一零、一负.在这两种情形下，<equation>|A| \leqslant 0.</equation>若<equation>A</equation>为3阶非零实对称矩阵，且<equation>|A| \leqslant 0</equation>，则<equation>A</equation>的特征值的符号有五种可能：（1）两正、一负；（2）一正、一零、一负；（3）两零、一负；（4）三负；（5）全为零.两个零特征值、一个负特征值与三个负特征值的情形与<equation>A</equation>的迹为零矛盾.特征值全为零的情形与<equation>A</equation>是非零实对称矩阵矛盾，因为若<equation>A</equation>的特征值全为零，则<equation>A</equation>相似于零矩阵，从而<equation>A</equation>为零矩阵.因此，<equation>A</equation>的特征值仅可能为两正、一负，或一正、一零、一负.在这两种情形下，<equation>A</equation>的负惯性指数都为1.

综上所述，<equation>A</equation>的负惯性指数为1等价于<equation>|A| \leqslant 0</equation>，即<equation>a \in [-2, 2]</equation>

---

**2013年第21题 | 解答题 | 11分**


设二次型<equation>f\left(x_{1},x_{2},x_{3}\right)=2\left(a_{1}x_{1}+a_{2}x_{2}+a_{3}x_{3}\right)^{2}+\left(b_{1}x_{1}+b_{2}x_{2}+b_{3}x_{3}\right)^{2}</equation>，记<equation>\begin{aligned} \alpha &= \left(  a _ {1} \\ a _ {2} \\ a _ {3}  \right), \quad \beta &= \left(  b _ {1} \\ b _ {2} \\ b _ {3}  \right) \end{aligned}</equation>I. 证明二次型 f对应的矩阵为<equation>2\alpha\alpha^{\mathrm{T}}+\beta\beta^{\mathrm{T}}</equation>；

II. 若<equation>\alpha, \beta</equation>正交且均为单位向量，证明 f在正交变换下的标准形为<equation>2y_{1}^{2}+y_{2}^{2}.</equation>

**答案:**(21) （ I ）证明略；（ II ）证明略

**解析:**证 （I）记<equation>\boldsymbol{x}=\left(x_{1},x_{2},x_{3}\right)^{\mathrm{T}}</equation><equation>f</equation>对应的矩阵为A,A为对称矩阵，则<equation>a _ {1} x _ {1} + a _ {2} x _ {2} + a _ {3} x _ {3} = \boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\alpha} = \boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {x}, \quad b _ {1} x _ {1} + b _ {2} x _ {2} + b _ {3} x _ {3} = \boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\beta} = \boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {x}.</equation><equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = 2 \left(\boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\alpha}\right) \left(\boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {x}\right) + \left(\boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\beta}\right) \left(\boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {x}\right) = \boldsymbol {x} ^ {\mathrm {T}} \left(2 \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}\right) \boldsymbol {x}.</equation>又由于<equation>(2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}})^{\mathrm{T}} = 2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>，故<equation>2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>是对称矩阵.于是<equation>2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>为所求A.

（Ⅱ）（法一）由<equation>A = 2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>且<equation>\alpha</equation>与<equation>\beta</equation>相互正交<equation>(\alpha^{\mathrm{T}}\beta = 0, \beta^{\mathrm{T}}\alpha = 0)</equation>得，<equation>A \alpha = \left(2 \alpha \alpha^ {\mathrm {T}} + \beta \beta^ {\mathrm {T}}\right) \alpha = 2 \alpha , \quad A \beta = \left(2 \alpha \alpha^ {\mathrm {T}} + \beta \beta^ {\mathrm {T}}\right) \beta = \beta .</equation>因此，2,1均为<equation>A</equation>的特征值，而<equation>\alpha ,\beta</equation>分别为属于特征值2,1的特征向量.

下面还需确定 A的另一个特征值.

考虑 A的秩.

由于对任何非零<equation>n</equation>维列向量<equation>\alpha ,\beta ,</equation>矩阵<equation>\beta \alpha^{\mathrm{T}}</equation>的秩均为1，故<equation>r (\boldsymbol {A}) = r \left(2 \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}\right) \leqslant r \left(2 \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}}\right) + r \left(\boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}\right) = 2.</equation>于是，<equation>\mathbf{A}</equation>不满秩，0也是<equation>\mathbf{A}</equation>的特征值.
