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


