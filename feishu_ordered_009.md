# 数学二

## 高等数学

### 常微分方程

#### 常系数齐次线性微分方程

**2025年第3题 | 选择题 | 5分 | 答案: C**
3. 如果对微分方程<equation>y^{\prime \prime}-2ay^{\prime}+(a+2)y=0</equation>的任一解 y(x)，反常积分<equation>\int_{0}^{+\infty}y(x)\mathrm{d}x</equation>均收敛，那么 a的取值范围是（    )

A.<equation>(-2,-1]</equation>B.<equation>(-\infty,-1]</equation>C.<equation>(-2,0)</equation>D.<equation>(-\infty,0)</equation>
答案: C
**解析: **解微分方程<equation>y^{\prime \prime}-2 a y^{\prime}+(a+2) y=0</equation>的特征方程为<equation>\lambda^{2}-2 a \lambda+a+2=0.</equation>- 若<equation>\Delta=4 a^{2}-4 ( a+2)=4 \left( a^{2}-a-2\right)>0</equation>，则特征方程有两个不同实根<equation>\lambda_{1},\lambda_{2}</equation>.此时，微分方程的解为<equation>y(x)=C_{1}\mathrm{e}^{\lambda_{1}x}+C_{2}\mathrm{e}^{\lambda_{2}x}.</equation>由于<equation>\mathrm{e}^{0 \cdot x} = 1</equation>，而<equation>\int_0^{+\infty}\mathrm{d}x</equation>发散，故当<equation>\lambda = 0</equation>时，<equation>\int_0^{+\infty}\mathrm{e}^{\lambda x}\mathrm{d}x</equation>发散.对<equation>\lambda \neq 0</equation>，<equation>\int_0^{+\infty}\mathrm{e}^{\lambda x}\mathrm{d}x = \frac{\mathrm{e}^{\lambda x}}{\lambda}\bigg|_0^{+\infty}</equation>当且仅当<equation>\lambda < 0</equation>时收敛，故对任一解<equation>y(x)</equation>，<equation>\int_0^{+\infty}y(x)\mathrm{d}x</equation>均收敛当且仅当<equation>\lambda_{1},\lambda_{2}</equation>均小于0.

由<equation>\Delta > 0</equation>以及根与系数的关系可得<equation>\left\{ \begin{array}{l l} a^{2} - a - 2 > 0, \\ 2a < 0, \\ a + 2 > 0, \end{array} \right.</equation>解得<equation>a \in (-2, -1)</equation>.

- 若<equation>\Delta = 4\left(a^{2} - a - 2\right) = 0</equation>，则特征方程有两个相同实根<equation>\lambda</equation>.当<equation>a = 2</equation>时，<equation>\lambda = 2</equation>，当<equation>a = -1</equation>时，<equation>\lambda = -1</equation>.此时，微分方程的解为<equation>y(x) = \left(C_{1} + C_{2}x\right)\mathrm{e}^{\lambda x}</equation>.

- 由于<equation>\int_0^{+\infty}\mathrm{e}^{\lambda x}\mathrm{d}x,\int_0^{+\infty}x\mathrm{e}^{\lambda x}\mathrm{d}x</equation>收敛当且仅当<equation>\lambda < 0</equation>，故此时对任一解<equation>y(x),\int_0^{+\infty}y(x)\mathrm{d}x</equation>均收敛当且仅当<equation>a = -1.</equation>- 若<equation>\Delta = 4\left(a^{2} - a - 2\right) < 0</equation>，则特征方程有一对共轭复根<equation>\lambda_{1,2} = a\pm \sqrt{-a^2 + a + 2}\mathrm{i} = \alpha \pm \beta \mathrm{i}</equation>此时，微分方程的解为<equation>y(x) = \mathrm{e}^{\alpha x}\left(C_1\cos \beta x + C_2\sin \beta x\right)</equation>，其中<equation>\alpha = a,\beta = \sqrt{-a^2 + a + 2}</equation>.

由于<equation>\int_{0}^{+\infty}\mathrm{e}^{\alpha x}\cos \beta x\mathrm{d}x,</equation><equation>\int_{0}^{+\infty}\mathrm{e}^{\alpha x}\sin \beta x\mathrm{d}x</equation>收敛当且仅当<equation>\alpha < 0</equation>（见注），故此时对任一解 y(x)<equation>\int_{0}^{+\infty}y(x)\mathrm{d}x</equation>均收敛当且仅当<equation>\left\{ \begin{array}{l l} a^{2}-a-2<0, \\ a<0, \end{array} \right.</equation>解得 a<equation>\in(-1,0).</equation>结合以上三种情况，若对任一解<equation>y ( x ) , \int_{0}^{+ \infty} y ( x ) \mathrm{d} x</equation>均收敛，则 a的取值范围是（-2,0）因此，应选C.

---

**2023年第4题 | 选择题 | 5分 | 答案: C**
4. 若微分方程<equation>y^{\prime \prime}+ay^{\prime}+by=0</equation>的解在<equation>(-\infty,+\infty)</equation>上有界，则 a,b的取值范围为（    )

A. a < 0,b > 0 B. a > 0,b > 0 C. a = 0,b > 0 D. a = 0,b < 0
答案: C
**解析: **解 由于二阶常系数齐次线性微分方程必有零解，而零解为有界解，故微分方程<equation>y^{\prime \prime}+ay^{\prime}+by=0</equation>必然存在（<equation>-\infty, +\infty</equation>）上的有界解.本题实际上是要求此方程的所有解都有界.

微分方程<equation>y^{\prime \prime}+a y^{\prime}+b y=0</equation>的特征方程为<equation>\lambda^{2}+a \lambda+b=0.</equation>- 若<equation>\Delta=a^{2}-4 b>0</equation>，则特征方程有两个不同实根<equation>\lambda_{1},\lambda_{2}</equation>，从而至少有一个实根非零.此时，微分方程的解为<equation>y=C_{1}\mathrm{e}^{\lambda_{1}x}+C_{2}\mathrm{e}^{\lambda_{2}x}.</equation>- 取<equation>C_{1}=C_{2}=1</equation>，则<equation>\lim_{x\to -\infty}\left(\mathrm{e}^{\lambda_{1}x}+\mathrm{e}^{\lambda_{2}x}\right)=+\infty</equation>或<equation>\lim_{x\to +\infty}\left(\mathrm{e}^{\lambda_{1}x}+\mathrm{e}^{\lambda_{2}x}\right)=+\infty.</equation>该解在<equation>(-\infty, +\infty)</equation>上无界.

- 若<equation>\Delta=a^{2}-4 b=0</equation>，则特征方程有两个相同实根<equation>\lambda</equation>.此时，微分方程的解为<equation>y=(C_{1}+ C_{2} x) \mathrm{e}^{\lambda x}.</equation>取<equation>C_{1} = 0,C_{2} = 1</equation>，则<equation>\lim_{x\to -\infty}x\mathrm{e}^{\lambda x} = \infty</equation>或<equation>\lim_{x\to +\infty}x\mathrm{e}^{\lambda x} = \infty</equation>.该解在<equation>(-\infty , + \infty)</equation>上无界.

- 若<equation>\Delta=a^{2}-4 b<0</equation>，则特征方程有一对共轭复根<equation>\lambda_{1,2}=\alpha\pm\beta\mathrm{i}</equation>.此时，微分方程的解为<equation>y=\mathrm{e}^{\alpha x}\left(C_{1}\cos \beta x+C_{2}\sin \beta x\right).</equation>当<equation>\alpha\neq0</equation>时，取<equation>C_{1}=1,C_{2}=0</equation>，所得解<equation>y=\mathrm{e}^{\alpha x}\cos \beta x</equation>是<equation>(-\infty, +\infty)</equation>上的无界函数.

当<equation>\alpha=0</equation>时，微分方程的解为<equation>y=C_{1}\cos \beta x+C_{2}\sin \beta x</equation>对任意常数<equation>C_{1},C_{2}</equation>，该解在<equation>(-\infty,+\infty)</equation>上均有界.根据求根公式，<equation>\lambda_{1,2}=-\frac{a}{2}\pm \frac{\sqrt{4b-a^{2}}}{2}\mathrm{i}</equation>即<equation>\alpha=-\frac{a}{2}</equation>于是，<equation>a=0</equation>结合<equation>a^{2}-4b<0</equation>可知，<equation>b>0.</equation>因此，<equation>a=0,b>0</equation>应选C.

---

**2022年第14题 | 填空题 | 5分**
14. 微分方程<equation>y^{\prime \prime \prime}-2 y^{\prime \prime}+5 y^{\prime}=0</equation>的通解为<equation>y ( x ) =</equation>
**答案: **<equation>C_{1}+ \mathrm{e}^{x}\left(C_{2}\cos 2 x+C_{3}\sin 2 x\right)</equation>，其中<equation>C_{1}, C_{2}, C_{3}</equation>为任意常数.
**解析: **解<equation>y^{\prime \prime \prime}-2 y^{\prime \prime}+5 y^{\prime}=0</equation>的特征方程为<equation>r^{3}-2 r^{2}+5 r=0</equation>，分解因式得<equation>r \left(r^{2}-2 r+5\right)=0.</equation>解得<equation>r_{1}=0, r_{2,3}=1\pm 2 \mathrm{i}.</equation>根据常系数齐次线性微分方程的通解与特征方程的根的关系，可得<equation>y^{\prime \prime \prime}-2 y^{\prime \prime}+5 y^{\prime}=0</equation>的通解为<equation>y=C_{1}+\mathrm{e}^{x}\left(C_{2}\cos 2 x+C_{3}\sin 2 x\right)</equation>，其中<equation>C_{1}, C_{2}, C_{3}</equation>为任意常数.

---

**2021年第15题 | 填空题 | 5分**
15. 微分方程<equation>y^{\prime\prime\prime}-y=0</equation>的通解<equation>y=</equation>___
**答案: **<equation>C_{1}\mathrm{e}^{x}+\mathrm{e}^{-\frac{x}{2}}\left(C_{2}\cos \frac{\sqrt{3}}{2} x+C_{3}\sin \frac{\sqrt{3}}{2} x\right),</equation>其中<equation>C_{1}, C_{2}, C_{3}</equation>为任意常数.
**解析: **解<equation>y^{\prime \prime \prime}-y=0</equation>的特征方程为<equation>r^{3}-1=0</equation>分解因式得<equation>( r-1 ) ( r^{2}+r+1 )=0</equation>解得<equation>r_{1}=1</equation><equation>r_{2,3}=-\frac{1}{2}\pm \frac{\sqrt{3}}{2}</equation>i.根据常系数齐次线性微分方程的通解与特征方程的根的关系，可得<equation>y^{\prime \prime \prime}-y=0</equation>的通解为<equation>y= C_{1}\mathrm{e}^{x}+\mathrm{e}^{-\frac{x}{2}}\left(C_{2}\cos \frac{\sqrt{3}}{2} x+C_{3}\sin \frac{\sqrt{3}}{2} x\right)</equation>，其中<equation>C_{1}, C_{2}, C_{3}</equation>为任意常数.

---

**2020年第13题 | 填空题 | 4分**
13. 设 y=y(x)满足<equation>y^{\prime\prime}+2 y^{\prime}+y=0</equation>，且 y(0)=0，<equation>y^{\prime}(0)=1</equation>，则<equation>\int_{0}^{+\infty} y(x)\mathrm{d}x=</equation>___
**答案: **```latex
1.
```

**解析:**解<equation>y^{\prime \prime}+2 y^{\prime}+y=0</equation>的特征方程为<equation>r^{2}+2 r+1=0</equation>，故特征根为<equation>r_{1,2}=-1.</equation>于是该方程的解为<equation>y(x)=(C_{1}+C_{2}x)\mathrm{e}^{-x}</equation>其中<equation>C_{1},C_{2}</equation>为待定常数.<equation>y^{\prime}(x)=(C_{2}-C_{1}-C_{2}x)\mathrm{e}^{-x}.</equation>（法一）由<equation>y(x)</equation>与<equation>y^{\prime}(x)</equation>的表达式可知，<equation>\lim_{x\to +\infty}y(x) = 0</equation>，<equation>\lim_{x\to +\infty}y^{\prime}(x) = 0.</equation>由<equation>y^{\prime \prime}+2 y^{\prime}+y=0</equation>可得，<equation>y(x)=-y^{\prime \prime}(x)-2 y^{\prime}(x).</equation>于是，<equation>\begin{aligned} \int_ {0} ^ {+ \infty} y (x) \mathrm {d} x &= \int_ {0} ^ {+ \infty} \left[ - y ^ {\prime \prime} (x) - 2 y ^ {\prime} (x) \right] \mathrm {d} x = \left[ - y ^ {\prime} (x) - 2 y (x) \right] \Bigg | _ {0} ^ {+ \infty} \\ &= \lim _ {x \rightarrow + \infty} \left[ - y ^ {\prime} (x) - 2 y (x) \right] - \left[ - y ^ {\prime} (0) - 2 y (0) \right] \\ &= y ^ {\prime} (0) + 2 y (0) = 1. \end{aligned}</equation>（法二）由<equation>y(0) = 0</equation>可得<equation>C_{1} = 0.</equation>由<equation>y^{\prime}(0) = 1</equation>可得<equation>C_{2} - C_{1} = 1</equation>，从而<equation>C_{2} = 1.</equation>于是，<equation>y(x) = x\mathrm{e}^{-x}.</equation><equation>\begin{aligned} \int_ {0} ^ {+ \infty} y (x) \mathrm {d} x &= \int_ {0} ^ {+ \infty} x \mathrm {e} ^ {- x} \mathrm {d} x = - \int_ {0} ^ {+ \infty} x \mathrm {d} \left(\mathrm {e} ^ {- x}\right) = - \left(x \mathrm {e} ^ {- x} \Big | _ {0} ^ {+ \infty} - \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- x} \mathrm {d} x\right) \\ &= \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- x} \mathrm {d} x = - \mathrm {e} ^ {- x} \Big | _ {0} ^ {+ \infty} = 1. \end{aligned}</equation>

---

**2015年第12题 | 填空题 | 4分**

12. 设函数<equation>y=y(x)</equation>是微分方程<equation>y^{\prime\prime}+y^{\prime}-2y=0</equation>的解，且在<equation>x=0</equation>处<equation>y(x)</equation>取得极值3，则<equation>y(x)=</equation>___.

**答案:**<equation>2 \mathrm{e}^{x}+\mathrm{e}^{-2 x}.</equation>

**解析:**解 由于<equation>y^{\prime \prime}+y^{\prime}-2 y=0</equation>的特征方程为<equation>r^{2}+r-2=0</equation>，故 r=-2和r=1为其特征方程的两个根.于是<equation>y=C_{1}\mathrm{e}^{x}+C_{2}\mathrm{e}^{-2 x}</equation>为原方程的解，其中<equation>C_{1}, C_{2}</equation>为待定常数.

由于<equation>y(0)=3</equation>，故<equation>C_{1}+C_{2}=3</equation>.又由于<equation>y(0)=3</equation>是y(x)的极值，故<equation>y^{\prime}(0)=0</equation>，从而<equation>C_{1}-2 C_{2}=0.</equation>由<equation>\left\{\begin{array}{l l} C_{1}+C_{2}=3, \\ C_{1}-2 C_{2}=0 \end{array} \right.</equation>解得，<equation>C_{1}=2, C_{2}=1.</equation>因此，<equation>y=2\mathrm{e}^{x}+\mathrm{e}^{-2 x}.</equation>

---

**2012年第19题 | 解答题 | 10分**

19. (本题满分10分)

已知函数 f(x)满足方程<equation>f^{\prime \prime}(x)+f^{\prime}(x)-2 f(x)=0</equation>及<equation>f^{\prime \prime}(x)+f(x)=2 \mathrm{e}^{x}</equation>.

I. 求 f(x)的表达式;

II. 求曲线<equation>y=f\left(x^{2}\right)\int_{0}^{x} f\left(-t^{2}\right)\mathrm{d} t</equation>的拐点.

**答案:**(19) ( I )<equation>f ( x )=\mathrm{e}^{x}</equation>;

( II ) ( 0, 0 ).

**解析:**解（I）（法一）本题中有两个微分方程，可先写出其中的二阶常系数齐次线性微分方程的通解，再将该通解代入另一个方程以确定通解中的常数.<equation>f^{\prime \prime}(x) + f^{\prime}(x) - 2 f(x) = 0</equation>为二阶常系数齐次线性微分方程。它的特征方程为<equation>r^{2}+r-2=0</equation>有两个不同的实根<equation>r_{1}=1,r_{2}=-2</equation>，从而其解为<equation>f(x)=C_{1}\mathrm{e}^{x}+C_{2}\mathrm{e}^{-2x}</equation>，其中<equation>C_{1},C_{2}</equation>为待定常数.

计算<equation>f^{\prime}(x), f^{\prime\prime}(x)</equation>得<equation>f ^ {\prime} (x) = C _ {1} \mathrm {e} ^ {x} - 2 C _ {2} \mathrm {e} ^ {- 2 x}, f ^ {\prime \prime} (x) = C _ {1} \mathrm {e} ^ {x} + 4 C _ {2} \mathrm {e} ^ {- 2 x}.</equation>代入<equation>f^{\prime \prime}(x) + f(x) = 2\mathrm{e}^{x}</equation>，得<equation>2C_{1}\mathrm{e}^{x} + 5C_{2}\mathrm{e}^{-2x} = 2\mathrm{e}^{x}</equation>，从而得<equation>C_{1} = 1,C_{2} = 0.</equation>因此，<equation>f ( x ) = \mathrm{e}^{x}.</equation>（法二）将两个微分方程联立，得<equation>\int f ^ {\prime \prime} (x) + f ^ {\prime} (x) - 2 f (x) = 0,</equation><equation>f ^ {\prime \prime} (x) + f (x) = 2 \mathrm {e} ^ {x}.</equation>(1) 式-（2）式得<equation>f^{\prime}(x)-3 f(x)=-2 \mathrm{e}^{x}</equation>，为一阶非齐次线性微分方程.由求解公式得<equation>f (x) = C \mathrm {e} ^ {- \int (- 3) \mathrm {d} x} + \mathrm {e} ^ {- \int (- 3) \mathrm {d} x} \int (- 2 \mathrm {e} ^ {x}) \mathrm {e} ^ {\int (- 3) \mathrm {d} x} \mathrm {d} x = \mathrm {e} ^ {x} + C \mathrm {e} ^ {3 x},</equation>其中 C为待定常数.

代回（2）式，得<equation>\mathrm {e} ^ {x} + 9 C \mathrm {e} ^ {3 x} + \mathrm {e} ^ {x} + C \mathrm {e} ^ {3 x} = 2 \mathrm {e} ^ {x}.</equation>从而 C=0.

因此，<equation>f ( x ) = \mathrm{e}^{x}.</equation>（Ⅱ）代入<equation>f ( x )=\mathrm{e}^{x}</equation>，对y逐次求导，得<equation>y = f \left(x ^ {2}\right) \int_ {0} ^ {x} f \left(- t ^ {2}\right) \mathrm {d} t = \mathrm {e} ^ {x ^ {2}} \int_ {0} ^ {x} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t,</equation><equation>y ^ {\prime} = \mathrm {e} ^ {x ^ {2}} \cdot \mathrm {e} ^ {- x ^ {2}} + 2 x \mathrm {e} ^ {x ^ {2}} \int_ {0} ^ {x} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t = 1 + 2 x y,</equation><equation>y ^ {\prime \prime} = \frac {\mathrm {d} (1 + 2 x y)}{\mathrm {d} x} = 2 y + 2 x y ^ {\prime} = 2 y + 2 x (1 + 2 x y) = 2 \left(2 x ^ {2} + 1\right) y + 2 x.</equation>由于<equation>\mathrm{e}^{x^2} > 0</equation>，<equation>\mathrm{e}^{-t^2} > 0</equation>，故当<equation>x > 0</equation>时，<equation>y > 0</equation>，从而<equation>y ^ {\prime \prime} (x) = 2 \left(2 x ^ {2} + 1\right) y + 2 x > 0.</equation>同理，当<equation>x < 0</equation>时，<equation>y < 0</equation><equation>y ^ {\prime \prime} (x) = 2 \left(2 x ^ {2} + 1\right) y + 2 x < 0.</equation>当<equation>x = 0</equation>时，<equation>y(0) = 0,y^{\prime \prime}(0) = 0.</equation>因此，点（0，0）为曲线<equation>y = f\left(x^{2}\right)\int_{0}^{x}f\left(-t^{2}\right)\mathrm{d}t</equation>的拐点.

---

**2010年第9题 | 填空题 | 4分**

9. 三阶常系数线性齐次微分方程<equation>y''' - 2y'' + y' - 2y = 0</equation>的通解为<equation>y =</equation>___

**答案:**<equation>C_{1}\mathrm{e}^{2 x}+C_{2}\cos x+C_{3}\sin x</equation>，其中<equation>C_{1},C_{2},C_{3}</equation>为任意常数.

**解析:**解<equation>y^{\prime \prime \prime}-2 y^{\prime \prime}+y^{\prime}-2 y=0</equation>对应的特征方程为<equation>r^{3}-2 r^{2}+r-2=0.</equation>分解因式得<equation>( r^{2}+1 ) ( r-2 )=0.</equation>因此，特征方程有3个根，<equation>r=2,r=\pm i.</equation>原方程的通解为<equation>y= C_{1} \mathrm{e}^{2 x}+C_{2} \cos x+C_{3} \sin x</equation>其中<equation>C_{1}, C_{2}, C_{3}</equation>为任意常数.

---


#### 微分方程的解与线性微分方程的解的结构

**2025年第15题 | 填空题 | 5分**
15. 微分方程<equation>(2y-3x)\mathrm{d}x+(2x-5y)\mathrm{d}y=0</equation>满足条件<equation>y(1)=1</equation>的解为 ___
**解析: **解（法一）整理<equation>( 2 y-3 x ) \mathrm{d} x+( 2 x-5 y ) \mathrm{d} y=0</equation>得到<equation>\frac{\mathrm{d} y}{\mathrm{d} x}=\frac{2 y-3 x}{5 y-2 x}=\frac{2 \frac{y}{x}-3}{5 \frac{y}{x}-2}.</equation>令<equation>u=\frac{y}{x}</equation>则<equation>y=u x,\frac{\mathrm{d} y}{\mathrm{d} x}=u+x\frac{\mathrm{d} u}{\mathrm{d} x}</equation>原方程可化为<equation>u+x\frac{\mathrm{d} u}{\mathrm{d} x}=\frac{2 u-3}{5 u-2}.</equation>这是一个可分离变量的微分方程.整理该方程可得<equation>x\frac{\mathrm{d} u}{\mathrm{d} x}=\frac{-5 u^{2}+4 u-3}{5 u-2},</equation>进一步分离变量可得<equation>\frac{(5 u-2)\mathrm{d} u}{5 u^{2}-4 u+3}=-\frac{\mathrm{d} x}{x}.</equation>方程两端同时积分可得<equation>\frac{1}{2}\ln |5 u^{2}-4 u+3|=-\ln |x|+C</equation>进一步可得<equation>5 u^{2}</equation><equation>-4 u+3=\frac{C_{1}}{x^{2}}</equation>其中<equation>C_{1}</equation>为待定常数.

当<equation>x = 1</equation>时，<equation>y = 1, u = 1</equation>，代入<equation>5 u^{2} - 4 u + 3 = \frac{C_{1}}{x^{2}}</equation>可得<equation>4 = \frac{C_{1}}{1}</equation>，即<equation>C_{1} = 4.</equation>由此可得<equation>5 u^{2} - 4 u+3 = \frac{4}{x^{2}}.</equation>代入<equation>u = \frac{y}{x}</equation>可得<equation>\frac{5 y^{2}}{x^{2}} - \frac{4 y}{x} + 3 = \frac{4}{x^{2}}</equation>，即<equation>5 y^{2} - 4 x y + 3 x^{2} - 4 = 0.</equation>（法二）考虑隐函数<equation>F ( x,y)=0</equation>，若<equation>F ( x,y)</equation>满足<equation>\frac{\partial F}{\partial x}=2 y-3 x, \frac{\partial F}{\partial y}=2 x-5 y</equation>，则<equation>(2 y-3 x)\mathrm{d} x+ ( 2 x-5 y ) \mathrm{d} y=0</equation>即<equation>\frac{\partial F}{\partial x}\mathrm{d} x+\frac{\partial F}{\partial y}\mathrm{d} y=0.</equation>对<equation>\frac{\partial F}{\partial x}</equation>关于 x积分可得<equation>F (x, y) = \int \frac {\partial F}{\partial x} \mathrm {d} x = \int (2 y - 3 x) \mathrm {d} x = 2 x y - \frac {3}{2} x ^ {2} + \varphi (y),</equation>其中<equation>\varphi(y)</equation>为关于y的一元函数.

对<equation>F(x,y) = 2xy - \frac{3}{2} x^2 + \varphi(y)</equation>关于<equation>y</equation>求偏导数可得<equation>\frac{\partial F}{\partial y} = 2x + \varphi^{\prime}(y)</equation>，与<equation>\frac{\partial F}{\partial y} = 2x - 5y</equation>比较可得<equation>\varphi^{\prime}(y) = -5y</equation>. 于是，<equation>\varphi (y) = \int \varphi^ {\prime} (y) \mathrm {d} y = \int (- 5 y) \mathrm {d} y = - \frac {5}{2} y ^ {2} + C,</equation>其中 C为待定常数.进一步可得<equation>F ( x,y) = 2 x y - \frac{3}{2} x^{2} - \frac{5}{2} y^{2} + C.</equation>将<equation>x=1,y=1</equation>代入<equation>F ( x,y) = 0</equation>可得<equation>2 - \frac{3}{2} -\frac{5}{2} + C = 0</equation>，解得<equation>C=2.</equation>因此，微分方程的解为<equation>2 x y-\frac{3}{2} x^{2}-\frac{5}{2} y^{2}+2=0</equation>即<equation>5 y^{2}-4 x y+3 x^{2}-4=0.</equation>

---

**2019年第4题 | 选择题 | 4分 | 答案: D**
4. 已知微分方程<equation>y^{\prime \prime}+ay^{\prime}+by=c\mathrm{e}^{x}</equation>的通解为<equation>y=(C_{1}+C_{2}x)\mathrm{e}^{-x}+\mathrm{e}^{x}</equation>，则 a,b,c依次为（    )

A. 1,0,1 B. 1,0,2 C. 2,1,3 D. 2,1,4
答案: D
**解析: **解 由原方程的通解形式可知，<equation>y=\left(C_{1}+C_{2}x\right)\mathrm{e}^{-x}</equation>是原方程对应的齐次线性微分方程的通解，故<equation>r=-1</equation>为该齐次方程的特征方程的二重根.于是，特征方程为<equation>(r+1)^{2}=0</equation>即<equation>r^{2}+2r+1=0.</equation>从而，<equation>a=2,b=1.</equation>由原方程的通解形式可知，<equation>y=\mathrm{e}^{x}</equation>是原方程的一个特解.将<equation>y=\mathrm{e}^{x}</equation>代入<equation>y^{\prime \prime}+2y^{\prime}+y=c\mathrm{e}^{x}</equation>可得，<equation>4\mathrm{e}^{x}=c\mathrm{e}^{x}.</equation>于是，<equation>c=4.</equation>因此，<equation>a=2,b=1,c=4.</equation>应选D.

---

**2014年第18题 | 解答题 | 10分**
18. (本题满分10分）

设函数 f(u)具有2阶连续导数，<equation>z=f(\mathrm{e}^{x}\cos y)</equation>满足<equation>\frac{\partial^{2} z}{\partial x^{2}}+\frac{\partial^{2} z}{\partial y^{2}}=(4 z+\mathrm{e}^{x}\cos y)\mathrm{e}^{2 x}.</equation>若 f(0)=0，<equation>f^{\prime}(0)=0</equation>求 f(u)的表达式.
**答案: **<equation>(1 8) f (u) = \frac {1}{1 6} \mathrm {e} ^ {2 u} - \frac {1}{1 6} \mathrm {e} ^ {- 2 u} - \frac {1}{4} u.</equation>
**解析: **解分别计算<equation>\frac{\partial^{2} z}{\partial x^{2}}</equation>和<equation>\frac{\partial^{2} z}{\partial y^{2}}.</equation><equation>\frac {\partial z}{\partial x} = \cos y \mathrm {e} ^ {x} f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right), \quad \frac {\partial^ {2} z}{\partial x ^ {2}} = \cos y \mathrm {e} ^ {x} f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right) + \cos^ {2} y \mathrm {e} ^ {2 x} f ^ {\prime \prime} \left(\mathrm {e} ^ {x} \cos y\right),</equation><equation>\frac {\partial z}{\partial y} = - \sin y \mathrm {e} ^ {x} f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right), \quad \frac {\partial^ {2} z}{\partial y ^ {2}} = - \cos y \mathrm {e} ^ {x} f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right) + \sin^ {2} y \mathrm {e} ^ {2 x} f ^ {\prime \prime} \left(\mathrm {e} ^ {x} \cos y\right).</equation>由<equation>\frac{\partial^{2}z}{\partial x^{2}}+\frac{\partial^{2}z}{\partial y^{2}}=(4z+\mathrm{e}^{x}\cos y)\mathrm{e}^{2x}</equation>可得<equation>\mathrm {e} ^ {2 x} f ^ {\prime \prime} \left(\mathrm {e} ^ {x} \cos y\right) = \left[ 4 f \left(\mathrm {e} ^ {x} \cos y\right) + \mathrm {e} ^ {x} \cos y \right] \mathrm {e} ^ {2 x},</equation>即<equation>f ^ {\prime \prime} \left(\mathrm {e} ^ {x} \cos y\right) = 4 f \left(\mathrm {e} ^ {x} \cos y\right) + \mathrm {e} ^ {x} \cos y.</equation>我们得到一个二阶常系数非齐次线性微分方程<equation>f^{\prime \prime}(u) - 4 f(u) = u.</equation>该方程对应的齐次方程的特征方程为<equation>r^{2}-4=0</equation>，因而解为<equation>f(u)=C_{1}\mathrm{e}^{2u}+C_{2}\mathrm{e}^{-2u}</equation>，其中<equation>C_{1},C_{2}</equation>为待定常数.

由于0不是特征方程的根，故<equation>f^{\prime \prime}(u)-4 f(u)=u</equation>有形如<equation>z^{*} = C_{3} u+C_{4}</equation>的特解.代入原方程得<equation>-4 C_{3} u-4 C_{4}=u.</equation>于是<equation>C_{3}=-\frac{1}{4}, C_{4}=0.</equation>因此，原方程的解为<equation>f (u) = C _ {1} \mathrm {e} ^ {2 u} + C _ {2} \mathrm {e} ^ {- 2 u} - \frac {1}{4} u.</equation>代入初值以确定<equation>C_{1}, C_{2}</equation>的值.由<equation>f(0)=0</equation>得，<equation>C_{1}+C_{2}=0.</equation>由<equation>f^{\prime}(0)=0</equation>得，<equation>2 C_{1}-2 C_{2}-\frac{1}{4}=0.</equation>从而解得<equation>C_{1}=\frac{1}{1 6}, C_{2}=-\frac{1}{1 6}.</equation>因此，<equation>f ( u ) = \frac { 1 } { 1 6 } \mathrm { e } ^ { 2 u } - \frac { 1 } { 1 6 } \mathrm { e } ^ { - 2 u } - \frac { 1 } { 4 } u .</equation>

---


#### 其他方程

**2024年第13题 | 填空题 | 5分**
13. 微分方程<equation>y^{\prime}=\frac{1}{(x+y)^{2}}</equation>满足条件 y(1)=0的解为 ___
**答案: **<equation>\arctan \left(x+y\right)=y+\frac{\pi}{4}</equation>
**解析: **解 令<equation>u=x+y</equation>，则<equation>\frac{\mathrm{d} u}{\mathrm{d} x}=1+\frac{\mathrm{d} y}{\mathrm{d} x}</equation>，原方程化为<equation>\frac{\mathrm{d} u}{\mathrm{d} x}-1=\frac{1}{u^{2}}</equation>，即<equation>\frac{\mathrm{d} u}{\mathrm{d} x}=\frac{1+u^{2}}{u^{2}}.</equation>这是一个可分离变量的微分方程，分离变量可得<equation>\left(1-\frac{1}{1+u^{2}}\right)\mathrm{d} u=\mathrm{d} x.</equation>方程两端同时积分可得<equation>u-\arctan u=x+C.</equation>由<equation>y(1)=0</equation>可得，<equation>u(1)=1.</equation>代入<equation>u-\arctan u=x+C</equation>可得<equation>1-\frac{\pi}{4}=1+C,</equation>解得<equation>C=-\frac{\pi}{4}.</equation>于是，<equation>u-\arctan u=x-\frac{\pi}{4}.</equation>将<equation>u=x+y</equation>代回<equation>u-\arctan u=x-\frac{\pi}{4}</equation>并整理可得<equation>y-\arctan (x+y)+\frac{\pi}{4}=0.</equation>

---

**2024年第18题 | 解答题 | 12分**
18. (本题满分12分)

设函数 y(x)为微分方程<equation>x^{2} y^{\prime \prime}+ x y^{\prime}-9 y=0</equation>满足条件<equation>y \mid_{x=1}=2, y^{\prime} \mid_{x=1}=6</equation>的解.

I. 利用变换<equation>x=\mathrm{e}^{t}</equation>将上述方程化为常系数线性方程，并求 y(x)；

II. 计算<equation>\int_{1}^{2} y(x)\sqrt{4-x^{2}} \mathrm{d} x.</equation>
**答案: **<equation>\begin{array}{l} (1) y (x) = 2 x ^ {3}. \\ (2) \frac {2 2 \sqrt {3}}{5}. \\ \end{array}</equation>
**解析: **解（I）令<equation>x=\mathrm{e}^{t}</equation>，则<equation>t=\ln x,</equation><equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} t} \cdot \frac {\mathrm {d} t}{\mathrm {d} x} = \frac {1}{x} \cdot \frac {\mathrm {d} y}{\mathrm {d} t},</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\mathrm {d} \left(\frac {\mathrm {d} y}{\mathrm {d} x}\right)}{\mathrm {d} x} = \frac {\mathrm {d} \left(\frac {1}{x} \cdot \frac {\mathrm {d} y}{\mathrm {d} t}\right)}{\mathrm {d} x} = \frac {1}{x} \cdot \frac {\mathrm {d} ^ {2} y}{\mathrm {d} t ^ {2}} \cdot \frac {\mathrm {d} t}{\mathrm {d} x} - \frac {1}{x ^ {2}} \cdot \frac {\mathrm {d} y}{\mathrm {d} t} = \frac {1}{x ^ {2}} \left(\frac {\mathrm {d} ^ {2} y}{\mathrm {d} t ^ {2}} - \frac {\mathrm {d} y}{\mathrm {d} t}\right).</equation>代入原方程可得<equation>\frac{\mathrm{d}^2 y}{\mathrm{d}t^2} -\frac{\mathrm{d}y}{\mathrm{d}t} +\frac{\mathrm{d}y}{\mathrm{d}t} -9y = 0</equation>，即<equation>\frac{\mathrm{d}^2 y}{\mathrm{d}t^2} -9y = 0.</equation>这是一个二阶常系数齐次线性微分方程. 该方程的特征方程为<equation>r^{2} - 9 = 0</equation>，特征根为<equation>r_{1,2} = \pm 3.</equation>于是，该方程的通解为<equation>y = C_{1}\mathrm{e}^{3t} + C_{2}\mathrm{e}^{-3t}.</equation>代入<equation>x = \mathrm{e}^{t}</equation>可得<equation>y = C_{1}x^{3} + C_{2}x^{-3}.</equation>进一步可得<equation>y^{\prime}(x) = 3C_{1}x^{2} - 3C_{2}x^{-4}.</equation>由<equation>y\mid_{x = 1} = 2,y^{\prime}\mid_{x = 1} = 6</equation>可得<equation>\left\{ \begin{array}{l}C_1 + C_2 = 2,\\ 3C_1 - 3C_2 = 6, \end{array} \right.</equation>解得<equation>\left\{ \begin{array}{l}C_1 = 2,\\ C_2 = 0. \end{array} \right.</equation>因此，<equation>y(x) = 2x^{3}</equation>.

（Ⅱ）由第（I）问的结果可得<equation>\int_1^2 y(x)\sqrt{4 - x^2}\mathrm{d}x = 2\int_1^2 x^3\sqrt{4 - x^2}\mathrm{d}x.</equation>下面用两种方法计算<equation>\int_{1}^{2} x^{3}\sqrt{4 - x^{2}}\mathrm{d}x.</equation>（法一）令<equation>t = 4 - x^{2}</equation>，则<equation>\mathrm{d}(x^{2}) = -\mathrm{d}t.</equation>于是，<equation>\begin{aligned} \int_ {1} ^ {2} x ^ {3} \sqrt {4 - x ^ {2}} \mathrm {d} x &= \frac {1}{2} \int_ {1} ^ {2} x ^ {2} \sqrt {4 - x ^ {2}} \mathrm {d} \left(x ^ {2}\right) \xlongequal {t = 4 - x ^ {2}} \frac {1}{2} \int_ {3} ^ {0} (4 - t) \sqrt {t} (- \mathrm {d} t) \\ &= \frac {1}{2} \int_ {0} ^ {3} \left(4 t ^ {\frac {1}{2}} - t ^ {\frac {3}{2}}\right) \mathrm {d} t = \frac {1}{2} \left(\frac {8}{3} t ^ {\frac {3}{2}} - \frac {2}{5} t ^ {\frac {5}{2}}\right) \Bigg | _ {0} ^ {3} \\ &= \frac {4}{3} \cdot 3 \sqrt {3} - \frac {1}{5} \cdot 9 \sqrt {3} = \frac {1 1 \sqrt {3}}{5}. \end{aligned}</equation>（法二）令<equation>x=2\sin t</equation>，则<equation>\begin{aligned} \int_ {1} ^ {2} x ^ {3} \sqrt {4 - x ^ {2}} \mathrm {d} x \xlongequal {x = 2 \sin t} \int_ {\frac {\pi}{6}} ^ {\frac {\pi}{2}} 8 \sin^ {3} t \cdot 2 \cos t \cdot 2 \cos t \mathrm {d} t &= 3 2 \int_ {\frac {\pi}{6}} ^ {\frac {\pi}{2}} \sin^ {3} t \cos^ {2} t \mathrm {d} t \\ &= 3 2 \int_ {\frac {\pi}{6}} ^ {\frac {\pi}{2}} \left(1 - \cos^ {2} t\right) \cos^ {2} t \sin t \mathrm {d} t \xlongequal {u = \cos t} - 3 2 \int_ {\frac {\sqrt {3}}{2}} ^ {0} \left(u ^ {2} - u ^ {4}\right) \mathrm {d} u \\ &= 3 2 \int_ {0} ^ {\frac {\sqrt {3}}{2}} \left(u ^ {2} - u ^ {4}\right) \mathrm {d} u = 3 2 \left(\frac {u ^ {3}}{3} - \frac {u ^ {5}}{5}\right) \Bigg | _ {0} ^ {\frac {\sqrt {3}}{2}} \\ &= 3 2 \cdot \left(\frac {3 \sqrt {3}}{8} \cdot \frac {1}{3} - \frac {9 \sqrt {3}}{3 2} \cdot \frac {1}{5}\right) = \frac {1 1 \sqrt {3}}{5}. \end{aligned}</equation>因此，<equation>\int_1^2 y(x)\sqrt{4 - x^2}\mathrm{d}x = 2\cdot \frac{11\sqrt{3}}{5} = \frac{22\sqrt{3}}{5}.</equation>

---


#### 微分方程的应用

**2023年第17题 | 解答题 | 10分**

设曲线 L: y=y(x)(x>e)经过点<equation>\mathrm{e}^{2},0),L</equation>上任一点 P(x,y)到 y轴的距离等于该点处的切线在 y轴上的截距.

I. 求 y(x);

II. 在 L上求一点，使该点的切线与两坐标轴所围三角形面积最小，并求此最小面积.

**答案:**（I）<equation>y ( x ) = x ( 2 - \ln x )</equation>；

（Ⅱ）点<equation>\left( \mathrm{e}^{\frac{3}{2}},\frac{\mathrm{e}^{\frac{3}{2}}}{2} \right)</equation>处的切线与坐标轴所围成的三角形面积最小，最小值为<equation>S \left( \mathrm{e}^{\frac{3}{2}} \right)=\mathrm{e}^{3}.</equation>

**解析:**解（I）由导数的几何意义可知，点 P(x,y)处的切线方程为<equation>Y-y=y^{\prime}(X-x).</equation>该点到y轴的距离为<equation>|x|\frac{x>e>0}{x}.</equation>令 X=0，可得 Y=y-xy'.由点 P(x,y)到 y轴的距离等于该点处的切线在 y轴上的截距可得 x=y-xy'.整理可得<equation>y^{\prime}-\frac{y}{x}=-1.</equation>由一阶非齐次线性微分方程的通解公式可得<equation>\begin{aligned} y &= \mathrm {e} ^ {\int \frac {1}{x} \mathrm {d} x} \left[ \int (- 1) \mathrm {e} ^ {- \int \frac {1}{x} \mathrm {d} x} \mathrm {d} x + C \right] = \mathrm {e} ^ {\ln x} \left(- \int \mathrm {e} ^ {- \ln x} \mathrm {d} x + C\right) \\ &= x \left(- \int \frac {1}{x} \mathrm {d} x + C\right) = x (C - \ln x). \end{aligned}</equation>代入<equation>x=\mathrm{e}^{2}, y=0</equation>可得 C=2. 因此，<equation>y(x)=x(2-\ln x).</equation>（Ⅱ）点（x,y）处的切线与两坐标轴所围成的三角形是一个直角三角形，记切线在 x轴，y轴上的截距为<equation>x_{0}, y_{0}</equation>，则三角形的面积<equation>S=\frac{1}{2}|x_{0}||y_{0}|.</equation>由第（I）问可知，点<equation>P(x,y)</equation>处的切线方程为<equation>Y-y=y^{\prime}(X-x),y_{0}=y-xy^{\prime}.</equation>令<equation>Y=0</equation>，可得<equation>X=x-\frac{y}{y^{\prime}}</equation>从而切线与x轴的交点为<equation>\left(x-\frac{y}{y^{\prime}},0\right),x_{0}=x-\frac{y}{y^{\prime}}.</equation>又由第（I）问可知，<equation>y=x(2-\ln x)</equation><equation>y ^ {\prime} = \left[ x (2 - \ln x) \right] ^ {\prime} = 2 - \ln x - x \cdot \frac {1}{x} = 1 - \ln x.</equation>于是，<equation>\left| x _ {0} \right| = \left| x - \frac {x (2 - \ln x)}{1 - \ln x} \right| = \frac {x}{\ln x - 1},</equation><equation>\left| y _ {0} \right| = \left| x \left(2 - \ln x\right) - x \left(1 - \ln x\right) \right| = x.</equation>由此可得<equation>S ( x ) = \frac { x^{2} } { 2 ( \ln x - 1 ) } .</equation>下面求 S（x）的最小值.

计算<equation>S^{\prime}(x).</equation><equation>S ^ {\prime} (x) = \frac {1}{2} \cdot \frac {2 x (\ln x - 1) - x ^ {2} \cdot \frac {1}{x}}{(\ln x - 1) ^ {2}} = \frac {2 x \ln x - 3 x}{2 (\ln x - 1) ^ {2}} = \frac {x \left(\ln x - \frac {3}{2}\right)}{(\ln x - 1) ^ {2}}.</equation>当且仅当<equation>x=\mathrm{e}^{\frac{3}{2}}</equation>时，<equation>S^{\prime}(x)=0</equation>.又因为当<equation>\mathrm{e}<x<\mathrm{e}^{\frac{3}{2}}</equation>时，<equation>S^{\prime}(x)<0,S(x)</equation>单调减少，当<equation>x > \mathrm{e}^{\frac{3}{2}}</equation>时，<equation>S^{\prime}(x)>0,S(x)</equation>单调增加，所以<equation>x=\mathrm{e}^{\frac{3}{2}}</equation>是 S(x)的最小值点.

因此，点<equation>\left(\mathrm{e}^{\frac{3}{2}},\frac{\mathrm{e}^{\frac{3}{2}}}{2}\right)</equation>处的切线与坐标轴所围成的三角形面积最小，最小值为<equation>S(\mathrm{e}^{\frac{3}{2}})=\mathrm{e}^{3}.</equation>

---

**2020年第21题 | 解答题 | 11分**


设函数 f(x)可导，且<equation>f^{\prime}(x) > 0</equation>，曲线<equation>y=f(x)(x\geqslant0)</equation>经过坐标原点O，其上任意一点M处的切线与x轴交于 T，又MP垂直x轴于点P.已知由曲线<equation>y=f(x)</equation>，直线MP以及x轴所围图形的面积与<equation>\triangle M T P</equation>的面积之比恒为3：2，求满足上述条件的曲线的方程.

**答案:**##<equation>y=Cx^{3}</equation>，其中C为任意正常数.

**解析:**解 点 M，T，P如图所示.

计算<equation>\triangle M T P</equation>的面积.

曲线<equation>y=f(x)</equation>上任意一点<equation>M(x,f(x))</equation>处的切线方程为<equation>Y - f (x) = f ^ {\prime} (x) (X - x).</equation>令 Y=0，可得点 T的横坐标为<equation>X=x-\frac{f(x)}{f^{\prime}(x)}.</equation>由于<equation>y = f(x) (x\geqslant 0)</equation>过原点，且<equation>f^{\prime}(x) > 0</equation>，故点M的纵坐标<equation>f(x) > 0.</equation><equation>|MP|=f(x),</equation><equation>|TP|=\left|x-\left[x-\frac{f(x)}{f^{\prime}(x)}\right]\right|=\left|\frac{f(x)}{f^{\prime}(x)}\right|=\frac{f(x)}{f^{\prime}(x)}.</equation>于是，<equation>S_{\triangle MTP}=\frac{1}{2}|MP||TP|=\frac{1}{2}\cdot f(x).</equation><equation>\frac{f(x)}{f^{\prime}(x)}=\frac{[f(x)]^{2}}{2f^{\prime}(x)}.</equation>由定积分的几何意义可得，曲边三角形 OMP的面积<equation>S=\int_{0}^{x} f(t)\mathrm{d} t.</equation>由曲边三角形 OMP的面积与<equation>\triangle M T P</equation>的面积之比恒为3：2可知<equation>\frac{\int_{0}^{x} f(t)\mathrm{d} t}{\frac{[f(x)]^{2}}{2f^{\prime}(x)}}=\frac{3}{2}</equation>即<equation>4 \int_ {0} ^ {x} f (t) \mathrm {d} t = \frac {3 [ f (x) ] ^ {2}}{f ^ {\prime} (x)}.</equation>对（1）式两端同时求导可得，<equation>4 f (x) = \frac {3 \left\{2 f (x) \left[ f ^ {\prime} (x) \right] ^ {2} - \left[ f (x) \right] ^ {2} f ^ {\prime \prime} (x) \right\}}{\left[ f ^ {\prime} (x) \right] ^ {2}}.</equation>整理可得<equation>2[f^{\prime}(x)]^{2}=3 f(x)f^{\prime \prime}(x)</equation>，即<equation>2(y^{\prime})^{2}=3 y y^{\prime \prime}.</equation>这是一个可降阶微分方程. 令<equation>p = y^{\prime}</equation>, 则<equation>y^{\prime \prime} = p \frac{\mathrm{d}p}{\mathrm{d}y}</equation>. 原方程化为<equation>2 p^{2} = 3 y \cdot p \frac{\mathrm{d}p}{\mathrm{d}y}</equation>, 即<equation>3 y \frac{\mathrm{d}p}{\mathrm{d}y} = 2 p</equation>. 分离变量可得<equation>\frac{\mathrm{d}p}{p} = \frac{2}{3 y} \mathrm{d}y</equation>. 方程两端积分可得<equation>\ln p = \frac{2}{3} \ln y + C_{0}</equation>（<equation>C_{0}</equation>为常数，这里不用加绝对值符号是因为由已知条件可得<equation>p > 0, y > 0</equation>）。由此可得<equation>y^{\prime} = p = C_{1} y^{\frac{2}{3}}</equation>, 其中<equation>C_{1}</equation>为常数，即<equation>\frac{\mathrm{d}y}{\mathrm{d}x} = C_{1} y^{\frac{2}{3}}</equation>.

由<equation>y = f(x)</equation>过原点可知，<equation>f(0) = 0</equation>. 代入<equation>2[f^{\prime}(x)]^{2} = 3 f(x) f^{\prime \prime}(x)</equation>可知<equation>f^{\prime}(0) = 0</equation>. 由<equation>f(0) = 0</equation>和<equation>f^{\prime}(0) = 0</equation>无法确定<equation>C_{1}</equation>.

分离变量可得<equation>\frac{\mathrm{d} y}{y^{\frac{2}{3}}}=C_{1}\mathrm{d} x.</equation>方程两端积分可得<equation>3y^{\frac{1}{3}}=C_{1}x+C_{2}.</equation>由<equation>f(0)=0</equation>可得<equation>C_{2}=0.</equation>从而<equation>3y^{\frac{1}{3}}=C_{1}x</equation>即<equation>y^{\frac{1}{3}}=\frac{C_{1}}{3}x.</equation>因此，<equation>y=\frac{C_{1}^{3}}{27}x^{3}=Cx^{3}, C=\frac{C_{1}^{3}}{27}.</equation>由于 y > 0，故 C > 0.

综上所述，<equation>y=Cx^{3}</equation>，其中C为任意正常数.

---

**2017年第21题 | 解答题 | 11分**

21. (本题满分11分)

设 y(x)是区间<equation>\left(0, \frac{3}{2}\right)</equation>内的可导函数，且 y(1)=0.点 P是曲线 l：y=y(x)上的任意一点，l在点 P处的切线与 y轴相交于点（0，<equation>Y_{P}</equation>），法线与 x轴相交于点（<equation>X_{P},0</equation>），若<equation>X_{P}=Y_{P}</equation>，求 l上点的坐标（x,y）满足的方程.

**答案:**<equation>\ln ( x^{2}+y^{2} )+2\arctan \frac{y}{x}=0</equation><equation>x\in\left( 0,\frac{3}{2}\right).</equation>

**解析:**解曲线 l在点 P（x,y(x)）处的切线方程为<equation>Y-y(x)=y^{\prime}(x)(X-x).</equation>由于 l在点 P处的切线过点（0，<equation>Y_{P}</equation>），故可得<equation>y - Y _ {P} = y ^ {\prime} x.</equation>由于同一点处的法线与切线相互垂直，故曲线 l在点 P(x,y(x))处的法线方程为 Y-y(x) =<equation>- \frac{1}{y^{\prime}(x)}(X-x).</equation>又因为法线过点（<equation>X_{P},0</equation>），所以得<equation>y = \frac {1}{y ^ {\prime}} \left(X _ {P} - x\right).</equation>由（1）式可得<equation>y - y^{\prime}x = Y_{P}.</equation>由（2）式可得<equation>y^{\prime}y+x=X_{P}.</equation>由<equation>X_{P}=Y_{P}</equation>可得<equation>y-y^{\prime}x=y^{\prime}y+x.</equation>于是，<equation>y ^ {\prime} = \frac {y - x}{y + x} = \frac {\frac {y}{x} - 1}{\frac {y}{x} + 1}.</equation>这是一个齐次微分方程.令<equation>u=\frac{y}{x}</equation>，则<equation>\frac{\mathrm{d} y}{\mathrm{d} x}=u+x\frac{\mathrm{d} u}{\mathrm{d} x}.</equation>（3）式可化为<equation>u + x \frac {\mathrm {d} u}{\mathrm {d} x} = \frac {u - 1}{u + 1}.</equation>这是一个可分离变量的微分方程. 整理得<equation>\frac {(u + 1) \mathrm {d} u}{u ^ {2} + 1} = - \frac {\mathrm {d} x}{x}.</equation>(4) 式两端同时积分可得<equation>\int \frac {u + 1}{u ^ {2} + 1} \mathrm {d} u = \int \frac {u \mathrm {d} u}{u ^ {2} + 1} + \int \frac {\mathrm {d} u}{u ^ {2} + 1} = \frac {1}{2} \ln \left(u ^ {2} + 1\right) + \arctan u = - \ln x + C.</equation>当 x=1时，y=0，<equation>u=\frac{y}{x}=0</equation>. 代入上式得 C=0.

将 u =<equation>\frac{y}{x}</equation>代回，整理得曲线方程为<equation>\ln \left(x ^ {2} + y ^ {2}\right) + 2 \arctan \frac {y}{x} = 0, x \in \left(0, \frac {3}{2}\right).</equation>

---

**2015年第20题 | 解答题 | 11分**


已知高温物体置于低温介质中，任一时刻该物体温度对时间的变化率与该时刻物体和介质的温差成正比。现将一初始温度为<equation>1 2 0^{\circ} \mathrm{C}</equation>的物体在<equation>2 0^{\circ} \mathrm{C}</equation>的恒温介质中冷却，<equation>3 0 \mathrm{~m i n}</equation>后该物体温度降至<equation>3 0^{\circ} \mathrm{C}</equation>，若要将该物体的温度继续降至<equation>2 1^{\circ} \mathrm{C}</equation>，还需冷却多长时间？

**答案:**## (20) 30 min.

**解析:**解设物体温度<equation>T</equation>为关于时间<equation>t</equation>的函数<equation>T(t)</equation>，则物体温度对时间的变化率为<equation>\frac{\mathrm{d}T}{\mathrm{d}t}</equation>.

由于任一时刻物体温度对时间的变化率与该时刻物体和介质的温差成正比，且介质温度恒为<equation>20^{\circ} \mathrm{C}</equation>，故可以建立关于<equation>T, t</equation>的微分方程：<equation>\frac{\mathrm{d} T}{\mathrm{d} t}=k ( T-2 0 ).</equation>注意：k的符号表示温度随时间推移增加或减少.由于温度随着时间推移而降低，这里的比例系数k是一个小于零的数.

分离变量得<equation>\frac{\mathrm{d} T}{T-2 0}=k \mathrm{d} t.</equation>对该方程两端积分得<equation>\ln ( T-2 0 )= k t+C</equation>其中C为待定常数.

当 t=0时，<equation>T(0)=1 2 0</equation>，由此可得 C=2ln10；当 t=30时，<equation>T(30)=30</equation>，由此可得 k=<equation>\frac{\ln 1 0-2 \ln 1 0}{3 0}=-\frac{\ln 1 0}{3 0}.</equation>因此，<equation>\ln (T - 2 0) = - \frac {\ln 1 0}{3 0} t + 2 \ln 1 0.</equation>当 T=21时，代入（1）式，可得<equation>0=-\frac{\ln 1 0}{3 0} t+2 \ln 1 0</equation>，解得 t=60，即冷却 30 min后，还需要继续冷却 30 min，才能把该物体温度降至 21<equation>^{\circ} \mathrm{C}.</equation>

---

**2011年第18题 | 解答题 | 10分**

18. (本题满分10分)

设函数 y(x)具有二阶导数，且曲线 l：y=y(x)与直线 y=x相切于原点.记<equation>\alpha</equation>为曲线 l在点（x,y）处切线的倾角，若<equation>\frac{\mathrm{d}\alpha}{\mathrm{d}x}=\frac{\mathrm{d}y}{\mathrm{d}x}</equation>求 y(x)的表达式.

**答案:**<equation>(1 8) y (x) = \arcsin \frac {\mathrm {e} ^ {x}}{\sqrt {2}} - \frac {\pi}{4}.</equation>

**解析:**解（法一）构造关于<equation>\alpha</equation>，<equation>x</equation>和关于<equation>\alpha</equation>，<equation>y</equation>的微分方程

由<equation>\frac{\mathrm{d}\alpha}{\mathrm{d}x}=\frac{\mathrm{d}y}{\mathrm{d}x}</equation>可得，<equation>\alpha=y+C_{1}</equation>，其中<equation>C_{1}</equation>为待定常数.于是，可以将求<equation>y(x)</equation>的表达式转化为求<equation>\alpha</equation>的表达式.

由导数的几何意义知，<equation>\frac{\mathrm{d}\alpha}{\mathrm{d}x}=\frac{\mathrm{d}y}{\mathrm{d}x}=\tan \alpha</equation>，故<equation>\frac{\mathrm{d}\alpha}{\mathrm{d}x}=\frac{\sin \alpha}{\cos \alpha}.</equation>分离变量得，<equation>\frac{\cos \alpha}{\sin \alpha}\mathrm{d}\alpha=\mathrm{d}x</equation>，解得<equation>\sin \alpha =C_{2}\mathrm{e}^{x}</equation>，其中<equation>C_{2}</equation>为待定常数.

由于曲线<equation>y=y(x)</equation>与直线<equation>y=x</equation>在原点相切，故当<equation>x=0</equation>时，<equation>\alpha(0)=\frac{\pi}{4}</equation>从而可求得<equation>C_{2}=\frac{\sqrt{2}}{2},</equation><equation>\alpha(x)=\arcsin \frac{\mathrm{e}^{x}}{\sqrt{2}}.</equation><equation>y (x) = \alpha (x) - C _ {1} = \arcsin \frac {\mathrm {e} ^ {x}}{\sqrt {2}} - C _ {1}.</equation>下面求<equation>C_{1}.</equation>由于<equation>\alpha (0)=\frac{\pi}{4}, y(0)=0</equation>，故<equation>0=\frac{\pi}{4}-C_{1}, C_{1}=\frac{\pi}{4}.</equation>因此，<equation>y (x) = \arcsin \frac {\mathrm {e} ^ {x}}{\sqrt {2}} - \frac {\pi}{4}.</equation>（法二）由于曲线 l：<equation>y=y(x)</equation>在点（x，y）处的切线斜率为<equation>y^{\prime}</equation>，故<equation>\tan \alpha =y^{\prime},\alpha =\arctan y^{\prime}.</equation>由链式法则可得，<equation>\frac{\mathrm{d}\alpha}{\mathrm{d}x}=\frac{y^{\prime \prime}}{1+(y^{\prime})^{2}}.</equation>又因为<equation>\frac{\mathrm{d}\alpha}{\mathrm{d}x}=\frac{\mathrm{d}y}{\mathrm{d}x}</equation>所以<equation>\frac {y ^ {\prime \prime}}{1 + \left(y ^ {\prime}\right) ^ {2}} = y ^ {\prime}.</equation>(1) 式为可降阶二阶微分方程.令<equation>p=y^{\prime}</equation>，则（1）式变成<equation>p^{\prime}=p(1+p^{2})</equation>，分离变量得，<equation>\frac{\mathrm{d} p}{p(1+p^{2})}=\mathrm{d} x.</equation>方程两端同时积分得<equation>\frac {1}{2} \ln \frac {p ^ {2}}{1 + p ^ {2}} = x + C,</equation>其中 C为待定常数.

由于曲线<equation>y = y(x)</equation>与直线<equation>y = x</equation>相切于原点，故<equation>y^{\prime}(0) = 1</equation>，即<equation>p(0) = 1.</equation>代入<equation>\frac{1}{2}\ln \frac{p^{2}}{1+p^{2}}=x+C</equation>得，<equation>\frac{1}{2}\ln \frac{1}{2}=0+C</equation>从而<equation>C=\frac{1}{2}\ln \frac{1}{2},x=\frac{1}{2}\ln \frac{2p^{2}}{1+p^{2}}</equation>即<equation>\frac{2(y^{\prime})^{2}}{1+(y^{\prime})^{2}}=</equation><equation>\mathrm{e}^{2x}.</equation>解得<equation>\left(y ^ {\prime}\right) ^ {2} = \frac {\mathrm {e} ^ {2 x}}{2 - \mathrm {e} ^ {2 x}}, \quad y ^ {\prime} = \pm \frac {\mathrm {e} ^ {x}}{\sqrt {2 - \mathrm {e} ^ {2 x}}}.</equation>由于<equation>y^{\prime}(0) = 1</equation>，故取<equation>y^{\prime} = \frac{\mathrm{e}^{x}}{\sqrt{2 - \mathrm{e}^{2x}}}</equation>对<equation>y^{\prime}</equation>积分求<equation>y ( x )</equation>的表达式.由于曲线过原点，故<equation>y ( 0 ) = 0</equation>从而<equation>y (x) = \int_ {0} ^ {x} \frac {\mathrm {e} ^ {t}}{\sqrt {2 - \mathrm {e} ^ {2 t}}} \mathrm {d} t = \int_ {0} ^ {x} \frac {\frac {\mathrm {e} ^ {t}}{\sqrt {2}}}{\sqrt {1 - \left(\frac {\mathrm {e} ^ {t}}{\sqrt {2}}\right) ^ {2}}} \mathrm {d} t = \arcsin \frac {\mathrm {e} ^ {t}}{\sqrt {2}} \Big | _ {0} ^ {x} = \arcsin \frac {\mathrm {e} ^ {x}}{\sqrt {2}} - \frac {\pi}{4}.</equation>因此，<equation>y ( x )</equation>的表达式为<equation>y ( x ) = \arcsin \frac{\mathrm{e}^{x}}{\sqrt{2}} -\frac{\pi}{4}.</equation>

---

**2009年第20题 | 解答题 | 11分**

20. (本题满分12分）设 y=y(x)是区间<equation>(-\pi,\pi)</equation>内过点<equation>\left(-\frac{\pi}{\sqrt{2}},\frac{\pi}{\sqrt{2}}\right)</equation>的光滑曲线.当<equation>-\pi < x < 0</equation>时，曲线上任一点处的法线都过原点；当<equation>0\leqslant x < \pi</equation>时，函数 y(x)满足<equation>y^{\prime \prime}+y+x=0.</equation>求 y(x)的表达式.

**答案:**(20)<equation>y ( x )=\left\{\begin{array}{ll}\sqrt{\pi^{2}-x^{2}},&x\in(-\pi,0),\\ \pi\cos x+\sin x-x,&x\in[0,\pi).\end{array}\right.</equation>

**解析:**解 在（-<equation>\pi</equation>，0）以及[0，<equation>\pi</equation>）上分别计算 y(x).

当<equation>x\in(-\pi ,0)</equation>时，曲线上任一点<equation>(x,y)</equation>处的法线都过原点，故点<equation>(x,y)</equation>处的法线斜率为<equation>\frac{y}{x}</equation>由同一点处的切线斜率与法线斜率的乘积为-1可得，点<equation>(x,y)</equation>处的切线斜率为<equation>y^{\prime} = -\frac{x}{x}</equation>.

分离变量得<equation>y \mathrm {d} y = - x \mathrm {d} x.</equation>于是<equation>x^{2}+y^{2}=C</equation>，其中C是待定常数.由<equation>y\left(-\frac{\pi}{\sqrt{2}}\right)=\frac{\pi}{\sqrt{2}}>0</equation>可知<equation>y=\sqrt{C-x^{2}}</equation>，再代入<equation>x=-\frac{\pi}{\sqrt{2}},</equation><equation>y=\frac{\pi}{\sqrt{2}}</equation>可求得<equation>C=\pi^{2}.</equation>因此，在<equation>(-\pi, 0)</equation>上，<equation>y ( x ) = \sqrt {\pi^{2}-x^{2}}.</equation>当<equation>x\in [0,\pi)</equation>时，通过解<equation>y^{\prime \prime} + y + x = 0</equation>得到<equation>y(x)</equation>的表达式.<equation>y^{\prime \prime}+y+x=0</equation>为二阶常系数非齐次线性微分方程，其对应的齐次线性微分方程为<equation>y^{\prime \prime}+y=0.</equation>由于<equation>y^{\prime \prime}+y=0</equation>的特征方程为<equation>r^{2}+1=0, r=\pm \mathrm{i}</equation>为特征方程的一对共轭复根，故<equation>y^{\prime \prime}+y=0</equation>的解为<equation>y=C_{1}\cos x+C_{2}\sin x</equation>，其中<equation>C_{1}, C_{2}</equation>为待定常数.

由待定系数法求<equation>y^{\prime \prime}+y+x=0</equation>的特解.由该方程的形式可知，该方程有形如<equation>y^{*} = ax+b</equation>的特解.<equation>(y^{*})^{\prime}=a, (y^{*})^{\prime \prime}=0.</equation>代回<equation>y^{\prime \prime}+y+x=0</equation>得<equation>ax+b+x=0</equation>，故<equation>a=-1,b=0</equation>，所求特解为<equation>y^{*}=-x.</equation>因此，<equation>y^{\prime \prime} + y + x = 0</equation>的解为<equation>y = C_{1}\cos x + C_{2}\sin x - x</equation>，其中<equation>C_{1}, C_{2}</equation>为待定常数.

由于所求曲线<equation>y=y(x)</equation>为光滑曲线，故<equation>y(x)</equation>连续且一阶导数连续，特别地，<equation>y(x)</equation>在分界点<equation>x=0</equation>处连续且一阶导数连续，可由该条件确定<equation>C_{1}, C_{2}</equation>的值.<equation>y \left(0 ^ {-}\right) = \lim _ {x \rightarrow 0 ^ {-}} \sqrt {\pi^ {2} - x ^ {2}} = \pi , \quad y \left(0 ^ {+}\right) = \lim _ {x \rightarrow 0 ^ {+}} \left(C _ {1} \cos x + C _ {2} \sin x - x\right) = C _ {1}.</equation>由<equation>y(0^{-}) = y(0^{+})</equation>得，<equation>C_{1} = \pi .</equation><equation>y ^ {\prime} (x) = \left\{ \begin{array}{l l} - \frac {x}{\sqrt {\pi^ {2} - x ^ {2}}}, & x \in (- \pi , 0), \\ - C _ {1} \sin x + C _ {2} \cos x - 1, & x \in (0, \pi). \end{array} \right.</equation>由于<equation>y^{\prime}(x)</equation>连续，故<equation>0 = \lim _ {x \rightarrow 0 ^ {-}} \left(- \frac {x}{\sqrt {\pi^ {2} - x ^ {2}}}\right) = \lim _ {x \rightarrow 0 ^ {+}} \left(- C _ {1} \sin x + C _ {2} \cos x - 1\right) = C _ {2} - 1.</equation>于是<equation>C_{2}=1.</equation>综上所述，可知<equation>y (x) = \left\{ \begin{array}{l l} \sqrt {\pi^ {2} - x ^ {2}}, & x \in (- \pi , 0), \\ \pi \cos x + \sin x - x, & x \in [ 0, \pi). \end{array} \right.</equation>

---


#### 一阶线性微分方程

**2022年第18题 | 解答题 | 12分**
18. (本题满分12分)

设函数 y(x)是微分方程<equation>2 x y^{\prime}-4 y=2 \ln x-1</equation>满足条件<equation>y ( 1 )=\frac{1} {4}</equation>的解，求曲线 y=y(x)（1≤x≤e）的弧长.
**解析: **解 整理原方程可得<equation>y^{\prime}-\frac{2 y}{x}=\frac{2 \ln x-1}{2 x}.</equation>这是一个一阶非齐次线性微分方程，由求解公式可得，<equation>\begin{aligned} y &= \mathrm {e} ^ {\int \frac {2}{x} \mathrm {d} x} \left(\int \frac {2 \ln x - 1}{2 x} \cdot \mathrm {e} ^ {- \int \frac {2}{x} \mathrm {d} x} \mathrm {d} x + C _ {0}\right) = x ^ {2} \left[ \int (2 \ln x - 1) \cdot \frac {1}{2} x ^ {- 3} \mathrm {d} x + C _ {0} \right] \\ &= x ^ {2} \left(\int \ln x \cdot x ^ {- 3} \mathrm {d} x - \int \frac {1}{2} x ^ {- 3} \mathrm {d} x + C _ {0}\right) = x ^ {2} \left[ \int \ln x \mathrm {d} \left(- \frac {1}{2} x ^ {- 2}\right) - \int \frac {1}{2} x ^ {- 3} \mathrm {d} x + C _ {0} \right] \\ &= x ^ {2} \left(- \frac {1}{2} x ^ {- 2} \ln x + \int \frac {1}{2} x ^ {- 2} \cdot \frac {1}{x} \mathrm {d} x - \int \frac {1}{2} x ^ {- 3} \mathrm {d} x + C _ {0}\right) \\ &= C x ^ {2} - \frac {\ln x}{2}. \end{aligned}</equation>代入<equation>y ( 1 )=\frac{1}{4}</equation>可得，<equation>C=\frac{1}{4}.</equation>因此，<equation>y ( x )=\frac{x^{2}}{4}-\frac{\ln x}{2}.</equation>计算得<equation>y^{\prime}=\frac{x}{2}-\frac{1}{2x}=\frac{1}{2}\left(x-\frac{1}{x}\right).</equation>代入曲线弧长的计算公式可得<equation>\begin{aligned} s &= \int_ {1} ^ {\mathrm {e}} \sqrt {1 + \left[ y ^ {\prime} (x) \right] ^ {2}} \mathrm {d} x = \int_ {1} ^ {\mathrm {e}} \sqrt {1 + \frac {1}{4} \left(x - \frac {1}{x}\right) ^ {2}} \mathrm {d} x = \int_ {1} ^ {\mathrm {e}} \sqrt {\frac {1}{4} \left(x + \frac {1}{x}\right) ^ {2}} \mathrm {d} x \\ &= \frac {1}{2} \int_ {1} ^ {\mathrm {e}} \left(x + \frac {1}{x}\right) \mathrm {d} x = \frac {1}{2} \left(\frac {x ^ {2}}{2} + \ln x\right) \Bigg | _ {1} ^ {\mathrm {e}} = \frac {\mathrm {e} ^ {2} + 1}{4}. \end{aligned}</equation>

---

**2021年第20题 | 解答题 | 12分**
0. (本题满分12分)

设函数 y=y(x)(x>0)满足微分方程<equation>x y^{\prime}-6 y=-6</equation>，且满足<equation>y(\sqrt{3})=10</equation>I. 求 y(x);

II. P为曲线 y=y(x)上的一点，曲线 y=y(x)在点 P的法线在 y轴上的截距为<equation>I_{P}</equation>，当<equation>I_{P}</equation>最小时，求 P的坐标.
**答案: **（ I ）<equation>y ( x )=\frac{x^{6}}{3}+1;</equation>（ II ）点 P的坐标为<equation>\left( 1,\frac{4}{3} \right)</equation>时，<equation>I_{P}</equation>有最小值<equation>\frac{11}{6}.</equation>
**解析: **解（I）整理<equation>x y^{\prime}-6 y=-6</equation>得，<equation>y^{\prime}-\frac{6 y}{x}=-\frac{6}{x}.</equation>由求解公式，可得<equation>\begin{aligned} y &= \mathrm {e} ^ {\int \frac {6}{x} \mathrm {d} x} \left[ \int \left(- \frac {6}{x}\right) \cdot \mathrm {e} ^ {- \int \frac {6}{x} \mathrm {d} x} \mathrm {d} x + C \right] = \mathrm {e} ^ {6 \ln x} \left[ \int \left(- \frac {6}{x}\right) \cdot \mathrm {e} ^ {- 6 \ln x} \mathrm {d} x + C \right] \\ &= x ^ {6} \left[ \int \left(- \frac {6}{x}\right) \cdot \frac {1}{x ^ {6}} \mathrm {d} x + C \right] = x ^ {6} \left[ \int (- 6) x ^ {- 7} \mathrm {d} x + C \right] = x ^ {6} \left(x ^ {- 6} + C\right) = C x ^ {6} + 1. \end{aligned}</equation>代入<equation>y(\sqrt{3})=10</equation>，可得<equation>1 0=1+C(\sqrt{3})^{6}</equation>，即<equation>1 0=1+2 7 C</equation>.解得<equation>C=\frac{1}{3}.</equation>因此，<equation>y ( x )=\frac{x^{6}}{3}+1,x>0.</equation>（Ⅱ）根据导数的几何意义，曲线<equation>y=\frac{x^{6}}{3}+1</equation>上的点P（x，y）处的切线斜率为<equation>2x^{5}.</equation>由同一点处的切线与法线相互垂直，斜率乘积为-1可得点P处的法线斜率为<equation>-\frac{1}{2x^{5}}.</equation>于是，点P处的法线方程为<equation>Y - y = - \frac {1}{2 x ^ {5}} (X - x).</equation>令<equation>X=0</equation>，可得<equation>Y=y+\frac{1}{2x^{4}}=\frac{x^{6}}{3}+1+\frac{1}{2x^{4}}</equation>，即<equation>I_{P}(x)=\frac{x^{6}}{3}+\frac{1}{2x^{4}}+1.</equation>计算<equation>I_{P}^{\prime}(x)</equation><equation>I _ {P} ^ {\prime} (x) = \left(\frac {x ^ {6}}{3} + \frac {1}{2 x ^ {4}} + 1\right) ^ {\prime} = 2 x ^ {5} - 2 x ^ {- 5} = \frac {2 \left(x ^ {1 0} - 1\right)}{x ^ {5}}, x > 0.</equation>令<equation>I_{P}^{\prime}(x) = 0</equation>，可得<equation>x=1.</equation>当<equation>0 < x < 1</equation>时，<equation>I_{P}^{\prime}(x) < 0, I_{P}(x)</equation>单调减少；当<equation>x > 1</equation>时，<equation>I_{P}^{\prime}(x) > 0, I_{P}(x)</equation>单调增加.故<equation>I_{P}(1)</equation>为<equation>I_{P}(x)</equation>在（0，<equation>+ \infty</equation>）上的最小值.<equation>I_{P}(1) = \frac{1}{3} +\frac{1}{2} +1 = \frac{11}{6}.</equation>因此，当<equation>x=1,y=\frac{4}{3}</equation>时，<equation>I_{P}(x)</equation>有最小值<equation>\frac{11}{6}.</equation>

---

**2019年第17题 | 解答题 | 10分**
17. (本题满分10分)

设函数 y(x)是微分方程<equation>y^{\prime}-xy=\frac{1}{2\sqrt{x}} \mathrm{e}^{\frac{x^{2}}{2}}</equation>满足条件 y(1)<equation>=\sqrt{\mathrm{e}}</equation>的特解.

I. 求 y(x);

II. 设平面区域 D = {(x,y) | 1≤x≤2,0≤y≤y(x)}，求 D绕 x轴旋转所得旋转体的体积.
**答案: **<equation>\begin{array}{l} (\mathrm {I}) y (x) = \sqrt {x} \mathrm {e} ^ {\frac {x ^ {2}}{2}}; \\ (\mathrm {I I}) \frac {1}{2} \pi \left(\mathrm {e} ^ {4} - \mathrm {e}\right). \\ \end{array}</equation>
**解析: **（I）由一阶非齐次线性微分方程的求解公式可得，<equation>\begin{aligned} y &= \mathrm {e} ^ {\int x \mathrm {d} x} \left[ \int \frac {1}{2 \sqrt {x}} \cdot \mathrm {e} ^ {\frac {x ^ {2}}{2}} \cdot \mathrm {e} ^ {\int (- x) \mathrm {d} x} \mathrm {d} x + C \right] = \mathrm {e} ^ {\frac {x ^ {2}}{2}} \left(\int \frac {1}{2 \sqrt {x}} \cdot \mathrm {e} ^ {\frac {x ^ {2}}{2}} \cdot \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \mathrm {d} x + C\right) \\ &= \mathrm {e} ^ {\frac {x ^ {2}}{2}} \left(\int \frac {1}{2 \sqrt {x}} \mathrm {d} x + C\right) = \sqrt {x} \mathrm {e} ^ {\frac {x ^ {2}}{2}} + C \mathrm {e} ^ {\frac {x ^ {2}}{2}}, \end{aligned}</equation>其中 C为待定常数.

代入<equation>x = 1,y(1) = \sqrt{\mathrm{e}}</equation>，可得<equation>\sqrt{\mathrm{e}} = \sqrt{\mathrm{e}} + C\sqrt{\mathrm{e}}.</equation>解得<equation>C = 0.</equation>因此，<equation>y ( x ) = \sqrt{x}\mathrm{e}^{\frac{x^{2}}{2}}.</equation>（Ⅱ）区域 D 如图所示.

根据旋转体的体积计算公式，<equation>\begin{aligned} V &= \pi \int_ {1} ^ {2} \left(\sqrt {x} \mathrm {e} ^ {\frac {x ^ {2}}{2}}\right) ^ {2} \mathrm {d} x = \pi \int_ {1} ^ {2} x \mathrm {e} ^ {x ^ {2}} \mathrm {d} x = \frac {1}{2} \pi \int_ {1} ^ {2} \mathrm {e} ^ {x ^ {2}} \mathrm {d} \left(x ^ {2}\right) \\ &= \frac {1}{2} \pi \mathrm {e} ^ {x ^ {2}} \Bigg | _ {1} ^ {2} = \frac {1}{2} \pi \left(\mathrm {e} ^ {4} - \mathrm {e}\right). \end{aligned}</equation>

---

**2016年第11题 | 填空题 | 4分**
11. 以<equation>y=x^{2}-\mathrm{e}^{x}</equation>和<equation>y=x^{2}</equation>为特解的一阶非齐次线性微分方程为 ___
**答案: **<equation>y ^ {\prime} - y = 2 x - x ^ {2}.</equation>
**解析: **解（法一）设原方程为<equation>y^{\prime}+p(x)y=q(x)</equation>，则其对应的一阶齐次线性微分方程为<equation>y^{\prime}+p(x)y=0.</equation>记<equation>y_{1}=x^{2}-\mathrm{e}^{x},</equation><equation>y_{2}=x^{2}</equation>，则<equation>y_{2}-y_{1}=\mathrm{e}^{x}</equation>是原方程对应的一阶齐次线性微分方程的解.将<equation>y=\mathrm{e}^{x}</equation>代入，可得<equation>p(x)=-1.</equation>再将<equation>y=x^{2}</equation>代入<equation>y^{\prime}-y=q(x)</equation>，得<equation>q(x)=2x-x^{2}.</equation>因此，原方程为<equation>y^{\prime} - y = 2x - x^{2}</equation>.

（法二）由于已知原方程的两个特解，而一阶非齐次线性微分方程形如<equation>y^{\prime}+p(x)y=q(x)</equation>，故可以用待定系数法来确定 p(x），q(x).

由已知条件，得<equation>2 x - \mathrm {e} ^ {x} + x ^ {2} p (x) - \mathrm {e} ^ {x} p (x) = q (x),</equation><equation>2 x + x ^ {2} p (x) = q (x).</equation>(2) 式减去（1）式得，<equation>\mathrm{e}^{x}+\mathrm{e}^{x}p(x)=0</equation>.于是<equation>p(x)=-1</equation>.再代回（2）式得，<equation>q(x)=2x-x^{2}.</equation>因此，原方程为<equation>y^{\prime}-y=2x-x^{2}.</equation>

---

**2012年第12题 | 填空题 | 4分**
12. 微分方程<equation>y \mathrm{d} x+(x-3 y^{2}) \mathrm{d} y=0</equation>满足条件<equation>y|_{x=1}=1</equation>的解为 y= ___.
**解析: **解 整理原微分方程，得<equation>\frac{\mathrm{d} x}{\mathrm{d} y}+\frac{x}{y}=3 y</equation>这是一个以 y为自变量，x为因变量的一阶非齐次线性微分方程.

根据求解公式，<equation>x = C \mathrm {e} ^ {- \int \frac {1}{y} \mathrm {d} y} + \mathrm {e} ^ {- \int \frac {1}{y} \mathrm {d} y} \int 3 y \mathrm {e} ^ {\int \frac {1}{y} \mathrm {d} y} \mathrm {d} y = \frac {C}{| y |} + \frac {1}{| y |} \int 3 y \cdot | y | \mathrm {d} y = \frac {C}{| y |} + y ^ {2},</equation>其中 C为待定常数.

代入初始值 x=1，y=1，得 C=0，故 x=y².又因为当 x=1时，y=1，所以 y=<equation>\sqrt{x}.</equation>

---

**2011年第10题 | 填空题 | 4分**
10. 微分方程<equation>y' + y = \mathrm{e}^{-x}\cos x</equation>满足条件<equation>y(0) = 0</equation>的解为<equation>y = \underline{\quad}</equation>
**答案: **#<equation>\mathrm{e}^{-x}\sin x.</equation>
**解析: **解（法一）原方程是一阶非齐次线性微分方程，故<equation>y = C \mathrm {e} ^ {- \int 1 \mathrm {d} x} + \mathrm {e} ^ {- \int 1 \mathrm {d} x} \int \mathrm {e} ^ {- x} \cos x \mathrm {e} ^ {\int 1 \mathrm {d} x} \mathrm {d} x = C \mathrm {e} ^ {- x} + \mathrm {e} ^ {- x} \sin x.</equation>当<equation>y(0) = 0</equation>时，解得<equation>C = 0</equation>，故原方程的解为<equation>y = \mathrm{e}^{-x}\sin x.</equation>（法二）方程两端同乘以<equation>\mathrm{e}^{x}</equation>得<equation>\mathrm{e}^{x} y^{\prime}+\mathrm{e}^{x} y=\cos x.</equation>方程左端等于<equation>\frac{\mathrm{d}\left(y\mathrm{e}^{x}\right)}{\mathrm{d}x}</equation>，方程可化为<equation>\mathrm{d}\left(y\mathrm{e}^{x}\right)=\cos x\mathrm{d}x</equation>，两端同时积分，<equation>\int \mathrm {d} \left(y \mathrm {e} ^ {x}\right) = \int \cos x \mathrm {d} x,</equation>得<equation>y\mathrm{e}^{x} = \sin x + C</equation>，其中C为待定常数.

代入<equation>y(0) = 0</equation>，得<equation>C = 0.</equation>因此，原方程的解为<equation>y = \mathrm{e}^{-x}\sin x.</equation>

---

**2010年第17题 | 解答题 | 10分**
17. (本题满分11分)

设函数 y=f(x)由参数方程<equation>\left\{\begin{array}{l l}x=2 t+t^{2}\\ y=\psi(t)\end{array}\right.</equation>（t>-1）所确定，其中<equation>\psi(t)</equation>具有2阶导数，且<equation>\psi(1)=\frac{5}{2},\psi^{\prime}(1)=6</equation>已知<equation>\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}=\frac{3}{4(1+t)}</equation>，求函数<equation>\psi(t).</equation>
**答案: **(17)<equation>\psi ( t )=t^{3}+\frac{3}{2} t^{2} ( t > -1 )</equation>
**解析: **解 由参数方程，可得<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {\psi^ {\prime} (t)}{2 t + 2},</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\mathrm {d} \left[ y ^ {\prime} (x) \right]}{\mathrm {d} x} = \frac {\mathrm {d} \left[ \frac {\psi^ {\prime} (t)}{2 t + 2} \right]}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {(t + 1) \psi^ {\prime \prime} (t) - \psi^ {\prime} (t)}{4 (t + 1) ^ {3}}.</equation>由<equation>\frac{\mathrm{d}^2y}{\mathrm{d}x^2} = \frac{3}{4(t + 1)}</equation>得，<equation>(t + 1) \psi^ {\prime \prime} (t) - \psi^ {\prime} (t) = 3 (t + 1) ^ {2}.</equation>这是一个可降阶二阶微分方程.令<equation>p = \psi^{\prime}(t)</equation>，对该方程降阶并整理，得<equation>p ^ {\prime} - \frac {p}{t + 1} = 3 (t + 1).</equation>由一阶非齐次线性微分方程的求解公式得，<equation>p = \mathrm {e} ^ {- \int \frac {- 1}{t + 1} \mathrm {d} t} \left[ \int 3 (t + 1) \mathrm {e} ^ {\int \frac {- 1}{t + 1} \mathrm {d} t} \mathrm {d} t + C \right] = (t + 1) (3 t + C),</equation>其中 C为待定常数.

由<equation>\psi^{\prime}(1) = 6</equation>得，<equation>p(1) = 2(3 + C) = 6</equation>，得<equation>C = 0.</equation>从而<equation>\psi^{\prime}(t) = 3t^{2} + 3t.</equation>对<equation>\psi^{\prime}(t)</equation>积分，得<equation>\psi (t) = \int \left(3 t ^ {2} + 3 t\right) \mathrm {d} t = t ^ {3} + \frac {3}{2} t ^ {2} + C ^ {\prime}.</equation>代入<equation>\psi (1) = \frac{5}{2}</equation>，得<equation>C^{\prime} = 0.</equation>因此，<equation>\psi (t) = t ^ {3} + \frac {3}{2} t ^ {2} (t > - 1).</equation>

---


#### 二阶常系数非齐次线性微分方程

**2017年第4题 | 选择题 | 4分 | 答案: C**
4. 微分方程<equation>y^{\prime \prime}-4 y^{\prime}+8 y=\mathrm{e}^{2 x}(1+\cos 2 x)</equation>的特解可设为<equation>y^{*}</equation>=（    )

A.<equation>A \mathrm{e}^{2 x}+\mathrm{e}^{2 x}(B \cos 2 x+C \sin 2 x)</equation>B.<equation>A x \mathrm{e}^{2 x}+\mathrm{e}^{2 x}(B \cos 2 x+C \sin 2 x)</equation>C.<equation>A \mathrm{e}^{2 x}+x \mathrm{e}^{2 x}(B \cos 2 x+C \sin 2 x)</equation>D.<equation>A x \mathrm{e}^{2 x}+x \mathrm{e}^{2 x}(B \cos 2 x+C \sin 2 x)</equation>
答案: C
**解析: **解 原微分方程对应的齐次方程的特征方程为<equation>r^{2}-4 r+8=0</equation>，有一对共轭复根<equation>r_{1,2}=2\pm 2 \mathrm{i}.</equation>原微分方程的非齐次项<equation>f(x)=\mathrm{e}^{2 x}+\mathrm{e}^{2 x}\cos 2 x.</equation>对<equation>f_{1}(x)=\mathrm{e}^{2 x}</equation>，由于2不是特征方程的根，故<equation>y^{\prime \prime}-4 y^{\prime}+8 y=\mathrm{e}^{2 x}</equation>的特解形式应为<equation>y^{*} = A\mathrm{e}^{2 x}.</equation>对<equation>f_{2}(x)=\mathrm{e}^{2 x}\cos 2 x</equation>，由于<equation>2\pm 2\mathrm{i}</equation>是特征方程的根，故<equation>y^{\prime \prime}-4 y^{\prime}+8 y=\mathrm{e}^{2 x}\cos 2 x</equation>的特解形式应为<equation>y^{*} = x\mathrm{e}^{2 x} ( B\cos 2 x+C\sin 2 x).</equation>根据线性微分方程的解的叠加原理，原微分方程的特解可设为<equation>y = A \mathrm {e} ^ {2 x} + x \mathrm {e} ^ {2 x} \left(B \cos 2 x + C \sin 2 x\right).</equation>应选C.

---

**2016年第19题 | 解答题 | 10分**
19. (本题满分10分)

已知<equation>y_{1}(x)=\mathrm{e}^{x}, y_{2}(x)=u(x)\mathrm{e}^{x}</equation>是二阶微分方程<equation>(2x-1)y^{\prime \prime}-(2x+1)y^{\prime}+2y=0</equation>的两个解.若<equation>u(-1)=\mathrm{e}, u(0)=-1</equation>求 u(x),并写出该微分方程的通解.
**答案: **<equation>u ( x )=-( 2 x+1 ) \mathrm{e}^{-x}</equation>，原方程的通解为<equation>y=k_{1}\mathrm{e}^{x}-k_{2}(2 x+1)</equation>，其中<equation>k_{1}, k_{2}</equation>为任意常数.
**解析: **计算<equation>y_{2}^{\prime}(x), y_{2}^{\prime\prime}(x).</equation><equation>\left(u \mathrm {e} ^ {x}\right) ^ {\prime} = \left(u + u ^ {\prime}\right) \mathrm {e} ^ {x}, \quad \left(u \mathrm {e} ^ {x}\right) ^ {\prime \prime} = \left(u ^ {\prime \prime} + 2 u ^ {\prime} + u\right) \mathrm {e} ^ {x}.</equation>将<equation>y_{2}^{\prime}(x), y_{2}^{\prime\prime}(x)</equation>代入（2x-1）<equation>y^{\prime\prime}-(2x+1)y^{\prime}+2y=0</equation>并整理，得<equation>(2 x - 1) u ^ {\prime \prime} \mathrm {e} ^ {x} + (2 x - 3) u ^ {\prime} \mathrm {e} ^ {x} = 0.</equation>由于<equation>\mathrm{e}^{x} > 0</equation>，故<equation>(2 x - 1) u ^ {\prime \prime} + (2 x - 3) u ^ {\prime} = 0.</equation>(1) 式为可降阶微分方程.令<equation>u^{\prime}=p</equation>，则得<equation>(2x-1)p^{\prime}=(3-2x)p.</equation>由分离变量法，得<equation>\frac {\mathrm {d} p}{p} = \left(- 1 + \frac {2}{2 x - 1}\right) \mathrm {d} x.</equation>上式两端同时积分，得<equation>\ln | p |=-x+\ln | 2 x-1 |+C_{0},| p |=C_{1}| 2 x-1 | \mathrm{e}^{-x},</equation>其中<equation>C_{0}, C_{1}</equation>为待定常数，<equation>C_{1}=\mathrm{e}^{C_{0}}.</equation>我们不妨去掉绝对值符号，记<equation>p=C(2 x-1)\mathrm{e}^{-x}</equation>，从而<equation>u ^ {\prime} = p = C (2 x - 1) \mathrm {e} ^ {- x},</equation>其中 C为待定常数，可能为正值，也可能为负值.

(2) 式两端同时关于 x积分得，<equation>\begin{aligned} u (x) &= C \int (2 x - 1) \mathrm {e} ^ {- x} \mathrm {d} x = C \int - (2 x - 1) \mathrm {d} \left(\mathrm {e} ^ {- x}\right) = C \left[ \mathrm {e} ^ {- x} (1 - 2 x) - \int \mathrm {e} ^ {- x} \mathrm {d} (1 - 2 x) \right] \\ &= C \left[ \mathrm {e} ^ {- x} (1 - 2 x) - 2 \mathrm {e} ^ {- x} \right] + C ^ {\prime} = - C \mathrm {e} ^ {- x} (2 x + 1) + C ^ {\prime}, \end{aligned}</equation>其中 C，C'为待定常数.

由题目条件，<equation>u(0)=-1</equation><equation>u(-1)=\mathrm{e}</equation>，代入<equation>u(x)</equation>的表达式得<equation>\left\{ \begin{array}{l l} C^{\prime}-C=-1, \\ C\mathrm{e}+C^{\prime}=\mathrm{e}. \end{array} \right.</equation>解得 C=1，<equation>C^{\prime}=0.</equation>于是，<equation>u(x)=-(2x+1)\mathrm{e}^{-x}, y_{2}(x)=u(x)\mathrm{e}^{x}=-(2x+1).</equation><equation>y_{1}(x), y_{2}(x)</equation>为二阶齐次线性微分方程<equation>( 2 x-1 ) y^{\prime \prime}-( 2 x+1 ) y^{\prime}+2 y=0</equation>的两个线性无关的解因此，由齐次线性微分方程的解的结构知，原方程的通解为<equation>y=k_{1}\mathrm{e}^{x}-k_{2}(2 x+1)</equation>其中<equation>k_{1}, k_{2}</equation>为任意常数.

---

**2013年第13题 | 填空题 | 4分**
13. 已知<equation>y_{1}=\mathrm{e}^{3 x}-x \mathrm{e}^{2 x}, y_{2}=\mathrm{e}^{x}-x \mathrm{e}^{2 x}, y_{3}=-x \mathrm{e}^{2 x}</equation>是某二阶常系数非齐次线性微分方程的3个解，则该方程满足条件<equation>y |_{x=0}=0, y^{\prime} |_{x=0}=1</equation>的解为 y=___
**答案: **<equation>\mathrm {e} ^ {3 x} - \mathrm {e} ^ {x} - x \mathrm {e} ^ {2 x}.</equation>
**解析: **解 对题设方程的3个解<equation>y_{i}\left(i=1,2,3\right), y_{i}-y_{j}\left(i,j=1,2,3,i\neq j\right)</equation>均为原方程对应的齐次线性微分方程的解.由于<equation>y_{1}-y_{3}=\mathrm{e}^{3x}, y_{2}-y_{3}=\mathrm{e}^{x}</equation>故<equation>y_{1}-y_{3}</equation>与<equation>y_{2}-y_{3}</equation>线性无关，从而<equation>C_{1}\left(y_{1}-y_{3}\right)</equation><equation>+ C_{2}\left(y_{2}-y_{3}\right)</equation>为原方程对应的齐次线性微分方程的解，其中<equation>C_{1}, C_{2}</equation>为常数.

原方程的通解可表示为<equation>y=C_{1}\mathrm{e}^{3x}+C_{2}\mathrm{e}^{x}-x\mathrm{e}^{2x}</equation>由<equation>y(0)=0, y^{\prime}(0)=1</equation>可得，<equation>\left\{ \begin{array}{l l} C_{1}+C_{2}=0, \\ 3 C_{1}+C_{2}=2. \end{array} \right.</equation>解得<equation>C_{1}=1, C_{2}=-1</equation>，故所求解为<equation>y=\mathrm{e}^{3x}-\mathrm{e}^{x}-x\mathrm{e}^{2x}.</equation>

---

**2011年第4题 | 选择题 | 4分 | 答案: C**
4. 微分方程<equation>y^{\prime \prime}-\lambda^{2} y=\mathrm{e}^{\lambda x}+\mathrm{e}^{-\lambda x} (\lambda>0)</equation>的特解形式为（    )

A.<equation>a\left(\mathrm{e}^{\lambda x}+\mathrm{e}^{-\lambda x}\right)</equation>B.<equation>a x\left(\mathrm{e}^{\lambda x}+\mathrm{e}^{-\lambda x}\right)</equation>C.<equation>x\left(a\mathrm{e}^{\lambda x}+b\mathrm{e}^{-\lambda x}\right)</equation>D.<equation>x^{2}\left(a\mathrm{e}^{\lambda x}+b\mathrm{e}^{-\lambda x}\right)</equation>
答案: C
**解析: **解 先写出<equation>y^{\prime \prime}-\lambda^{2} y=\mathrm{e}^{\lambda x}</equation>与<equation>y^{\prime \prime}-\lambda^{2} y=\mathrm{e}^{-\lambda x}</equation>的特解形式.

由于<equation>y^{\prime \prime}-\lambda^{2} y=0</equation>的特征方程为<equation>r^{2}-\lambda^{2}=0</equation>，故<equation>\pm \lambda</equation>为特征方程的单根.对于方程<equation>y^{\prime \prime}-\lambda^{2} y=\mathrm{e}^{\lambda x}</equation>由于<equation>\lambda</equation>是其特征方程的单根，故它的特解形如<equation>y_{1}^{*} = a x \mathrm{e}^{\lambda x}</equation>；同理，方程<equation>y^{\prime \prime}-\lambda^{2} y=\mathrm{e}^{- \lambda x}</equation>的特解形如<equation>y_{2}^{*} = b x \mathrm{e}^{- \lambda x}.</equation>因此，根据线性微分方程的解的叠加原理，<equation>y^{\prime \prime} - \lambda^{2} y = \mathrm{e}^{\lambda x} + \mathrm{e}^{- \lambda x} (\lambda > 0)</equation>的特解形式为<equation>y _ {1} ^ {*} + y _ {2} ^ {*} = x \left(a \mathrm {e} ^ {\lambda x} + b \mathrm {e} ^ {- \lambda x}\right).</equation>应选C.

---

**2010年第2题 | 选择题 | 4分 | 答案: A**
2. 设<equation>y_{1}, y_{2}</equation>是一阶线性非齐次微分方程<equation>y^{\prime}+p(x)y=q(x)</equation>的两个特解，若常数<equation>\lambda,\mu</equation>使<equation>\lambda y_{1}+\mu y_{2}</equation>是该方程的解，<equation>\lambda y_{1}-\mu y_{2}</equation>是该方程对应的齐次方程的解，则（    ）

A.<equation>\lambda=\frac{1}{2},\mu=\frac{1}{2}</equation>B.<equation>\lambda=-\frac{1}{2},\mu=-\frac{1}{2}</equation>C.<equation>\lambda=\frac{2}{3},\mu=\frac{1}{3}</equation>D.<equation>\lambda=\frac{2}{3},\mu=\frac{2}{3}</equation>
答案: A
**解析: **由题设知，<equation>y _ {1} ^ {\prime} + p (x) y _ {1} = q (x), \quad y _ {2} ^ {\prime} + p (x) y _ {2} = q (x).</equation>又由题设知，<equation>\lambda y_{1} + \mu y_{2}</equation>也是<equation>y^{\prime} + p(x)y = q(x)</equation>的解，故<equation>\left(\lambda y _ {1} + \mu y _ {2}\right) ^ {\prime} + p (x) \left(\lambda y _ {1} + \mu y _ {2}\right) = q (x).</equation>整理（1）式，得<equation>\lambda \left[ y _ {1} ^ {\prime} + p (x) y _ {1} \right] + \mu \left[ y _ {2} ^ {\prime} + p (x) y _ {2} \right] = q (x),</equation>即<equation>(\lambda +\mu)q(x) = q(x)</equation>. 由于<equation>q(x)\neq 0</equation>，故<equation>\lambda +\mu = 1.</equation>又由<equation>\lambda y_{1} - \mu y_{2}</equation>是<equation>y^{\prime} + p(x)y = 0</equation>的解知<equation>\left(\lambda y _ {1} - \mu y _ {2}\right) ^ {\prime} + p (x) \left(\lambda y _ {1} - \mu y _ {2}\right) = 0.</equation>整理（2）式，得<equation>\lambda \left[ y _ {1} ^ {\prime} + p (x) y _ {1} \right] - \mu \left[ y _ {2} ^ {\prime} + p (x) y _ {2} \right] = 0,</equation>即<equation>(\lambda -\mu)q(x) = 0.</equation>由于<equation>q(x)\neq 0</equation>，故<equation>\lambda -\mu = 0.</equation>联立<equation>\left\{ \begin{array}{l l} \lambda + \mu = 1, \\ \lambda - \mu = 0, \end{array} \right.</equation>解得<equation>\lambda = \frac{1}{2}, \mu = \frac{1}{2}</equation>. 应选A.

---


### 多元函数微积分学
#### 二重积分的应用

**2013年第21题 | 解答题 | 11分**

21. (本题满分11分)

设曲线 L的方程为<equation>y=\frac{1}{4} x^{2}-\frac{1}{2} \ln x</equation>(1≤x≤e).

I. 求 L的弧长;

II. 设 D是由曲线 L，直线 x=1,x=e及 x轴所围平面图形，求 D的形心的横坐标.

**答案:**(21) ( I )<equation>\frac{1}{4} \left( \mathrm{e}^{2}+1 \right);</equation>(Ⅱ）<equation>\frac{3\left(\mathrm{e}^{4}-2\mathrm{e}^{2}-3\right)}{4\left(\mathrm{e}^{3}-7\right)}.</equation>

**解析:**解（I）由求弧长的公式得<equation>\begin{aligned} s &= \int_ {1} ^ {e} \sqrt {1 + \left(y ^ {\prime}\right) ^ {2}} \mathrm {d} x \xlongequal {y ^ {\prime} = \frac {1}{2} \left(x - \frac {1}{x}\right)} \int_ {1} ^ {e} \sqrt {1 + \frac {1}{4} \left(x - \frac {1}{x}\right) ^ {2}} \mathrm {d} x \\ &= \frac {1}{2} \int_ {1} ^ {e} \left(x + \frac {1}{x}\right) \mathrm {d} x = \frac {1}{4} \left(\mathrm {e} ^ {2} + 1\right). \end{aligned}</equation>（Ⅱ）由于<equation>y ^ {\prime} = \frac {1}{2} \left(x - \frac {1}{x}\right), \quad y ^ {\prime} (1) = 0, \quad y ^ {\prime \prime} = \frac {1}{2} \left(1 + \frac {1}{x ^ {2}}\right) > 0,</equation>故在<equation>[1,\mathrm{e}]</equation>上，<equation>y^{\prime}\geqslant 0,y(x)\geqslant y(1) = \frac{1}{4}</equation>. 因此，当<equation>x\in [1,\mathrm{e}]</equation>时，曲线 L位于 x轴上方，如图所示.

区域<equation>D = \left\{(x, y) \mid 0 \leqslant y \leqslant \frac {1}{4} \left(x ^ {2} - 2 \ln x\right), 1 \leqslant x \leqslant \mathrm {e} \right\}.</equation><equation>\bar {x} = \frac {\int_ {1} ^ {\mathrm {e}} x \mathrm {d} x \int_ {0} ^ {\frac {1}{4} \left(x ^ {2} - 2 \ln x\right)} \mathrm {d} y}{\int_ {1} ^ {\mathrm {e}} \mathrm {d} x \int_ {0} ^ {\frac {1}{4} \left(x ^ {2} - 2 \ln x\right)} \mathrm {d} y} = \frac {\frac {1}{4} \int_ {1} ^ {\mathrm {e}} \left(x ^ {3} - 2 x \ln x\right) \mathrm {d} x}{\frac {1}{4} \int_ {1} ^ {\mathrm {e}} \left(x ^ {2} - 2 \ln x\right) \mathrm {d} x}.</equation>其中，<equation>\begin{aligned} \int_ {1} ^ {e} \left(x ^ {3} - 2 x \ln x\right) d x &= \frac {x ^ {4}}{4} \Bigg | _ {1} ^ {e} - \int_ {1} ^ {e} 2 x \ln x d x = \frac {\mathrm {e} ^ {4} - 1}{4} - \int_ {1} ^ {e} \ln x d \left(x ^ {2}\right) \\ &= \frac {\mathrm {e} ^ {4} - 1}{4} - \left(x ^ {2} \ln x \Big | _ {1} ^ {e} - \int_ {1} ^ {e} x \mathrm {d} x\right) = \frac {\mathrm {e} ^ {4}}{4} - \frac {\mathrm {e} ^ {2}}{2} - \frac {3}{4}. \end{aligned}</equation><equation>\int_ {1} ^ {e} \left(x ^ {2} - 2 \ln x\right) \mathrm {d} x = \frac {x ^ {3}}{3} \Big | _ {1} ^ {e} - 2 \int_ {1} ^ {e} \ln x \mathrm {d} x = \frac {\mathrm {e} ^ {3} - 1}{3} - 2 \left(x \ln x \Big | _ {1} ^ {e} - \int_ {1} ^ {e} 1 \mathrm {d} x\right) = \frac {\mathrm {e} ^ {3} - 7}{3}.</equation>因此，<equation>\bar {x} = \frac {\frac {\mathrm {e} ^ {4}}{4} - \frac {\mathrm {e} ^ {2}}{2} - \frac {3}{4}}{\frac {\mathrm {e} ^ {3} - 7}{3}} = \frac {3 \left(\mathrm {e} ^ {4} - 2 \mathrm {e} ^ {2} - 3\right)}{4 \left(\mathrm {e} ^ {3} - 7\right)}.</equation>

---

**2013年第21题 | 解答题 | 11分**
21. (本题满分11分)

设曲线 L的方程为<equation>y=\frac{1}{4} x^{2}-\frac{1}{2} \ln x</equation>(1≤x≤e).

I. 求 L的弧长;

II. 设 D是由曲线 L，直线 x=1,x=e及 x轴所围平面图形，求 D的形心的横坐标.
**答案: **(21) ( I )<equation>\frac{1}{4} \left( \mathrm{e}^{2}+1 \right);</equation>(Ⅱ）<equation>\frac{3\left(\mathrm{e}^{4}-2\mathrm{e}^{2}-3\right)}{4\left(\mathrm{e}^{3}-7\right)}.</equation>
**解析: **解（I）由求弧长的公式得<equation>\begin{aligned} s &= \int_ {1} ^ {e} \sqrt {1 + \left(y ^ {\prime}\right) ^ {2}} \mathrm {d} x \xlongequal {y ^ {\prime} = \frac {1}{2} \left(x - \frac {1}{x}\right)} \int_ {1} ^ {e} \sqrt {1 + \frac {1}{4} \left(x - \frac {1}{x}\right) ^ {2}} \mathrm {d} x \\ &= \frac {1}{2} \int_ {1} ^ {e} \left(x + \frac {1}{x}\right) \mathrm {d} x = \frac {1}{4} \left(\mathrm {e} ^ {2} + 1\right). \end{aligned}</equation>（Ⅱ）由于<equation>y ^ {\prime} = \frac {1}{2} \left(x - \frac {1}{x}\right), \quad y ^ {\prime} (1) = 0, \quad y ^ {\prime \prime} = \frac {1}{2} \left(1 + \frac {1}{x ^ {2}}\right) > 0,</equation>故在<equation>[1,\mathrm{e}]</equation>上，<equation>y^{\prime}\geqslant 0,y(x)\geqslant y(1) = \frac{1}{4}</equation>. 因此，当<equation>x\in [1,\mathrm{e}]</equation>时，曲线 L位于 x轴上方，如图所示.

区域<equation>D = \left\{(x, y) \mid 0 \leqslant y \leqslant \frac {1}{4} \left(x ^ {2} - 2 \ln x\right), 1 \leqslant x \leqslant \mathrm {e} \right\}.</equation><equation>\bar {x} = \frac {\int_ {1} ^ {\mathrm {e}} x \mathrm {d} x \int_ {0} ^ {\frac {1}{4} \left(x ^ {2} - 2 \ln x\right)} \mathrm {d} y}{\int_ {1} ^ {\mathrm {e}} \mathrm {d} x \int_ {0} ^ {\frac {1}{4} \left(x ^ {2} - 2 \ln x\right)} \mathrm {d} y} = \frac {\frac {1}{4} \int_ {1} ^ {\mathrm {e}} \left(x ^ {3} - 2 x \ln x\right) \mathrm {d} x}{\frac {1}{4} \int_ {1} ^ {\mathrm {e}} \left(x ^ {2} - 2 \ln x\right) \mathrm {d} x}.</equation>其中，<equation>\begin{aligned} \int_ {1} ^ {e} \left(x ^ {3} - 2 x \ln x\right) d x &= \frac {x ^ {4}}{4} \Bigg | _ {1} ^ {e} - \int_ {1} ^ {e} 2 x \ln x d x = \frac {\mathrm {e} ^ {4} - 1}{4} - \int_ {1} ^ {e} \ln x d \left(x ^ {2}\right) \\ &= \frac {\mathrm {e} ^ {4} - 1}{4} - \left(x ^ {2} \ln x \Big | _ {1} ^ {e} - \int_ {1} ^ {e} x \mathrm {d} x\right) = \frac {\mathrm {e} ^ {4}}{4} - \frac {\mathrm {e} ^ {2}}{2} - \frac {3}{4}. \end{aligned}</equation><equation>\int_ {1} ^ {e} \left(x ^ {2} - 2 \ln x\right) \mathrm {d} x = \frac {x ^ {3}}{3} \Big | _ {1} ^ {e} - 2 \int_ {1} ^ {e} \ln x \mathrm {d} x = \frac {\mathrm {e} ^ {3} - 1}{3} - 2 \left(x \ln x \Big | _ {1} ^ {e} - \int_ {1} ^ {e} 1 \mathrm {d} x\right) = \frac {\mathrm {e} ^ {3} - 7}{3}.</equation>因此，<equation>\bar {x} = \frac {\frac {\mathrm {e} ^ {4}}{4} - \frac {\mathrm {e} ^ {2}}{2} - \frac {3}{4}}{\frac {\mathrm {e} ^ {3} - 7}{3}} = \frac {3 \left(\mathrm {e} ^ {4} - 2 \mathrm {e} ^ {2} - 3\right)}{4 \left(\mathrm {e} ^ {3} - 7\right)}.</equation>

---

