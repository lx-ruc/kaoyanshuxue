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


