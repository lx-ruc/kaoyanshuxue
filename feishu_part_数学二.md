# 数学二


## 高等数学


### 常微分方程


#### 可分离变量的微分方程

**2014年第16题 | 解答题 | 10分**

16. (本题满分10分）

已知函数 y=y(x)满足微分方程<equation>x^{2}+y^{2} y^{\prime}=1-y^{\prime}</equation>，且 y(2)=0，求 y(x)的极大值与极小值.

**答案:**(16) 极大值<equation>y ( 1 ) = 1</equation>，极小值<equation>y (- 1 ) = 0.</equation>

**解析:**整理原微分方程得，<equation>(1 + y ^ {2}) \mathrm {d} y = (1 - x ^ {2}) \mathrm {d} x.</equation>这是可分离变量的微分方程. 方程两端积分得<equation>y + \frac {y ^ {3}}{3} = x - \frac {x ^ {3}}{3} + C.</equation>代入<equation>x = 2</equation>，<equation>y(2) = 0</equation>，得<equation>C = \frac{2}{3}</equation>，从而得到关于<equation>x,y</equation>的一个隐函数方程：<equation>x^{3} + y^{3} - 3x + 3y = 2.</equation>要求<equation>y(x)</equation>的极大值与极小值，可先求<equation>y^{\prime}(x)</equation>. 由（1）式可得<equation>y ^ {\prime} = \frac {1 - x ^ {2}}{1 + y ^ {2}}.</equation>由此可知，当<equation>x=\pm1</equation>时，<equation>y^{\prime}=0</equation>；当<equation>x>1</equation>或<equation>x<-1</equation>时，<equation>y^{\prime}<0</equation>，<equation>y(x)</equation>单调减少；当<equation>-1<x<1</equation>时，<equation>y^{\prime}>0</equation>，<equation>y(x)</equation>单调增加.

于是，<equation>y ( x )</equation>在<equation>x=1</equation>处取到极大值，在<equation>x=-1</equation>处取到极小值.由<equation>x^{3}+y^{3}-3 x+3 y=2</equation>可计算得，当<equation>x=-1</equation>时，<equation>y=0</equation>；当<equation>x=1</equation>时，<equation>y=1</equation>因此，<equation>y ( x )</equation>的极大值为<equation>y ( 1 )=1</equation>，极小值为<equation>y (-1)=0.</equation>

---

**2014年第16题 | 解答题 | 10分**
16. (本题满分10分）

已知函数 y=y(x)满足微分方程<equation>x^{2}+y^{2} y^{\prime}=1-y^{\prime}</equation>，且 y(2)=0，求 y(x)的极大值与极小值.
**答案: **(16) 极大值<equation>y ( 1 ) = 1</equation>，极小值<equation>y (- 1 ) = 0.</equation>
**解析: **整理原微分方程得，<equation>(1 + y ^ {2}) \mathrm {d} y = (1 - x ^ {2}) \mathrm {d} x.</equation>这是可分离变量的微分方程. 方程两端积分得<equation>y + \frac {y ^ {3}}{3} = x - \frac {x ^ {3}}{3} + C.</equation>代入<equation>x = 2</equation>，<equation>y(2) = 0</equation>，得<equation>C = \frac{2}{3}</equation>，从而得到关于<equation>x,y</equation>的一个隐函数方程：<equation>x^{3} + y^{3} - 3x + 3y = 2.</equation>要求<equation>y(x)</equation>的极大值与极小值，可先求<equation>y^{\prime}(x)</equation>. 由（1）式可得<equation>y ^ {\prime} = \frac {1 - x ^ {2}}{1 + y ^ {2}}.</equation>由此可知，当<equation>x=\pm1</equation>时，<equation>y^{\prime}=0</equation>；当<equation>x>1</equation>或<equation>x<-1</equation>时，<equation>y^{\prime}<0</equation>，<equation>y(x)</equation>单调减少；当<equation>-1<x<1</equation>时，<equation>y^{\prime}>0</equation>，<equation>y(x)</equation>单调增加.

于是，<equation>y ( x )</equation>在<equation>x=1</equation>处取到极大值，在<equation>x=-1</equation>处取到极小值.由<equation>x^{3}+y^{3}-3 x+3 y=2</equation>可计算得，当<equation>x=-1</equation>时，<equation>y=0</equation>；当<equation>x=1</equation>时，<equation>y=1</equation>因此，<equation>y ( x )</equation>的极大值为<equation>y ( 1 )=1</equation>，极小值为<equation>y (-1)=0.</equation>

---


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


#### 偏导数的概念与计算

**2025年第1题 | 选择题 | 5分 | 答案: A**

1. 设函数<equation>z=z(x,y)</equation>由<equation>z+\ln z-\int_{y}^{x}\mathrm{e}^{-t^{2}}\mathrm{d}t=0</equation>确定，则<equation>\frac{\partial z}{\partial x}+\frac{\partial z}{\partial y}=</equation>(    )

A.<equation>\frac{z}{z+1} \left( \mathrm{e}^{-x^{2}}-\mathrm{e}^{-y^{2}} \right)</equation>B.<equation>\frac{z}{z+1} \left( \mathrm{e}^{-x^{2}}+\mathrm{e}^{-y^{2}} \right)</equation>C.<equation>-\frac{z}{z+1} \left( \mathrm{e}^{-x^{2}}-\mathrm{e}^{-y^{2}} \right)</equation>D.<equation>-\frac{z}{z+1} \left( \mathrm{e}^{-x^{2}}+\mathrm{e}^{-y^{2}} \right)</equation>

答案: A

**解析:**解 对已知方程两端关于 x求偏导数可得<equation>\frac {\partial z}{\partial x} + \frac {1}{z} \cdot \frac {\partial z}{\partial x} - \mathrm {e} ^ {- x ^ {2}} = 0.</equation>整理可得<equation>\frac{z + 1}{z}\frac{\partial z}{\partial x} = \mathrm{e}^{-x^2}</equation>，解得<equation>\frac{\partial z}{\partial x} = \frac{z}{z + 1}\mathrm{e}^{-x^2}</equation>.

同理，对已知方程两端关于 y 求偏导数可得<equation>\frac {\partial z}{\partial y} + \frac {1}{z} \cdot \frac {\partial z}{\partial y} + \mathrm {e} ^ {- \gamma^ {2}} = 0.</equation>整理可得<equation>\frac{z + 1}{z}\frac{\partial z}{\partial y} = -\mathrm{e}^{-y^2}</equation>，解得<equation>\frac{\partial z}{\partial y} = -\frac{z}{z + 1}\mathrm{e}^{-y^2}</equation>.

因此，<equation>\frac {\partial z}{\partial x} + \frac {\partial z}{\partial y} = \frac {z}{z + 1} \left(\mathrm {e} ^ {- x ^ {2}} - \mathrm {e} ^ {- y ^ {2}}\right).</equation>应选A.

---

**2024年第5题 | 选择题 | 5分 | 答案: C**

5. 已知函数<equation>f ( x,y)=\left\{\begin{array}{ll} \left(x^{2}+y^{2}\right)\sin \frac{1}{xy},& xy\neq 0\\ 0,& xy=0 \end{array} \right.</equation>则在点（0，0）处（    ）

A.<equation>\frac{\partial f(x,y)}{\partial x}</equation>连续，f(x,y)可微 B.<equation>\frac{\partial f(x,y)}{\partial x}</equation>连续，f(x,y)不可微

C.<equation>\frac{\partial f(x,y)}{\partial x}</equation>不连续，f(x,y)可微 D.<equation>\frac{\partial f(x,y)}{\partial x}</equation>不连续，f(x,y)不可微

答案: C

**解析:**解 当<equation>y = 0</equation>时，根据偏导数的定义，<equation>\frac{\partial f(x,y)}{\partial x}\bigg|_{(x,0)} = \lim_{\Delta x\to 0}\frac{f(x + \Delta x,0) - f(x,0)}{\Delta x} = \lim_{\Delta x\to 0}\frac{0 - 0}{\Delta x} = 0,</equation>即<equation>f_x^{\prime}(x,0) = 0.</equation>同理可得<equation>\frac{\partial f(x,y)}{\partial y}\bigg|_{(0,y)} = 0,</equation>即<equation>f_y^{\prime}(0,y) = 0.</equation>特别地，<equation>f_x^{\prime}(0,0) = f_y^{\prime}(0,0) = 0.</equation><equation>- 0 -</equation>当 xy≠0时，由链式法则可得<equation>\frac {\partial f (x , y)}{\partial x} = 2 x \sin \frac {1}{x y} + \left(x ^ {2} + y ^ {2}\right) \cdot \cos \frac {1}{x y} \cdot \left(- \frac {1}{x ^ {2} y}\right) = 2 x \sin \frac {1}{x y} - \frac {x ^ {2} + y ^ {2}}{x ^ {2} y} \cos \frac {1}{x y}.</equation>取<equation>x_{n} = y_{n} = \frac{1}{\sqrt{2n\pi}}</equation>，则<equation>\lim_{n\to \infty}x_n = \lim_{n\to \infty}y_n = 0,\sin \frac{1}{x_n y_n}\equiv 0,\cos \frac{1}{x_n y_n}\equiv 1</equation>，而<equation>\frac {x _ {n} ^ {2} + y _ {n} ^ {2}}{x _ {n} ^ {2} y _ {n}} = \frac {\frac {1}{2 n \pi} + \frac {1}{2 n \pi}}{\frac {1}{2 n \pi \sqrt {2 n \pi}}} = 2 \sqrt {2 n \pi},</equation>从而<equation>\lim _ {n \rightarrow \infty} \left(2 x _ {n} \sin \frac {1}{x _ {n} y _ {n}} - \frac {x _ {n} ^ {2} + y _ {n} ^ {2}}{x _ {n} ^ {2} y _ {n}} \cos \frac {1}{x _ {n} y _ {n}}\right) = - \infty .</equation>由此可得，<equation>\lim_{(x,y)\to(0,0)} \left( 2x\sin \frac{1}{xy}-\frac{x^{2}+y^{2}}{x^{2}y}\cos \frac{1}{xy}\right)</equation>不存在.进一步可得<equation>\frac{\partial f(x,y)}{\partial x}</equation>在点（0,0）处不连续另一方面，<equation>\begin{aligned} \lim _ {(x, y) \rightarrow (0, 0)} \frac {f (x , y) - f (0 , 0) - f _ {x} ^ {\prime} (0 , 0) x - f _ {y} ^ {\prime} (0 , 0) y}{\sqrt {x ^ {2} + y ^ {2}}} &= \lim _ {(x, y) \rightarrow (0, 0)} \frac {f (x , y) - 0 - 0 \cdot x - 0 \cdot y}{\sqrt {x ^ {2} + y ^ {2}}} \\ &= \lim _ {(x, y) \rightarrow (0, 0)} \frac {f (x , y)}{\sqrt {x ^ {2} + y ^ {2}}}. \end{aligned}</equation>当 xy≠0时，<equation>\left|\sin \frac{1}{xy}\right|\leqslant 1</equation>，故<equation>0 \leqslant \frac {\left| f (x , y) \right|}{\sqrt {x ^ {2} + y ^ {2}}} = \left| \sqrt {x ^ {2} + y ^ {2}} \sin \frac {1}{x y} \right| \leqslant \sqrt {x ^ {2} + y ^ {2}},</equation>当<equation>xy = 0</equation>时，<equation>\frac{|f(x,y)|}{\sqrt{x^2 + y^2}} = 0\leqslant \sqrt{x^2 + y^2}.</equation>进一步由<equation>\lim_{(x,y)\to(0,0)}\sqrt{x^2 + y^2} = 0</equation>以及夹逼准则可得<equation>\lim_{(x,y)\to(0,0)}\frac{|f(x,y)|}{\sqrt{x^2 + y^2}} = 0</equation>，从而<equation>\lim_{(x,y)\to(0,0)}\frac{f(x,y)}{\sqrt{x^2 + y^2}} = 0.</equation>于是，由可微的定义可知，<equation>f(x,y)</equation>在点(0,0)处可微.

综上所述，应选C.

---

**2024年第20题 | 解答题 | 12分**

20. (本题满分12分)

已知函数 f(u,v)具有二阶连续偏导数，且函数 g(x,y)=f(2x+y,3x-y)满足<equation>\frac{\partial^{2} g}{\partial x^{2}}+\frac{\partial^{2} g}{\partial x \partial y}-6 \frac{\partial^{2} g}{\partial y^{2}}=1.</equation>I. 求<equation>\frac{\partial^{2} f}{\partial u \partial v}</equation>；

II. 若<equation>\frac{\partial f(u,0)}{\partial u}=u e^{-u}</equation>，且 f(0,v)<equation>= \frac{1}{50} v^{2}-1</equation>，求 f(u,v)的表达式.

**答案:**(1)<equation>\frac {\partial^ {2} f}{\partial v \partial v} = \frac {1}{2 5}</equation>(2)<equation>f (u, v) = - (u + 1) e ^ {- u} + \frac {1}{2 5} u v + \frac {1}{5 0} v ^ {2}</equation>

**解析:**解（I）根据链式法则，并结合<equation>f(u,v)</equation>具有2阶连续偏导数，从而<equation>\frac{\partial^{2} f}{\partial u \partial v}=\frac{\partial^{2} f}{\partial v \partial u}</equation>可得<equation>\frac {\partial g}{\partial x} = 2 \frac {\partial f}{\partial u} + 3 \frac {\partial f}{\partial v},</equation><equation>\frac {\partial g}{\partial y} = \frac {\partial f}{\partial u} - \frac {\partial f}{\partial v},</equation><equation>\frac {\partial^ {2} g}{\partial x ^ {2}} = 2 \left(2 \frac {\partial^ {2} f}{\partial u ^ {2}} + 3 \frac {\partial^ {2} f}{\partial u \partial v}\right) + 3 \left(2 \frac {\partial^ {2} f}{\partial v \partial u} + 3 \frac {\partial^ {2} f}{\partial v ^ {2}}\right) = 4 \frac {\partial^ {2} f}{\partial u ^ {2}} + 1 2 \frac {\partial^ {2} f}{\partial u \partial v} + 9 \frac {\partial^ {2} f}{\partial v ^ {2}},</equation><equation>\frac {\partial^ {2} g}{\partial x \partial y} = 2 \left(\frac {\partial^ {2} f}{\partial u ^ {2}} - \frac {\partial^ {2} f}{\partial u \partial v}\right) + 3 \left(\frac {\partial^ {2} f}{\partial v \partial u} - \frac {\partial^ {2} f}{\partial v ^ {2}}\right) = 2 \frac {\partial^ {2} f}{\partial u ^ {2}} + \frac {\partial^ {2} f}{\partial u \partial v} - 3 \frac {\partial^ {2} f}{\partial v ^ {2}},</equation><equation>\frac {\partial^ {2} g}{\partial y ^ {2}} = \frac {\partial^ {2} f}{\partial u ^ {2}} - \frac {\partial^ {2} f}{\partial u \partial v} - \left(\frac {\partial^ {2} f}{\partial v \partial u} - \frac {\partial^ {2} f}{\partial v ^ {2}}\right) = \frac {\partial^ {2} f}{\partial u ^ {2}} - 2 \frac {\partial^ {2} f}{\partial u \partial v} + \frac {\partial^ {2} f}{\partial v ^ {2}}.</equation>将上述结果代入<equation>\frac{\partial^{2}g}{\partial x^{2}}+\frac{\partial^{2}g}{\partial x\partial y}-6\frac{\partial^{2}g}{\partial y^{2}}=1</equation>可得<equation>4 \frac {\partial^ {2} f}{\partial u ^ {2}} + 1 2 \frac {\partial^ {2} f}{\partial u \partial v} + 9 \frac {\partial^ {2} f}{\partial v ^ {2}} + 2 \frac {\partial^ {2} f}{\partial u ^ {2}} + \frac {\partial^ {2} f}{\partial u \partial v} - 3 \frac {\partial^ {2} f}{\partial v ^ {2}} - 6 \frac {\partial^ {2} f}{\partial u ^ {2}} + 1 2 \frac {\partial^ {2} f}{\partial u \partial v} - 6 \frac {\partial^ {2} f}{\partial v ^ {2}} = 1.</equation>整理可得<equation>25\frac{\partial^{2}f}{\partial u\partial v} = 1</equation>，即<equation>\frac{\partial^{2}f}{\partial u\partial v} = \frac{1}{25}</equation>（Ⅱ）对<equation>\frac{\partial^{2} f}{\partial u \partial v}</equation>关于<equation>v</equation>积分可得，<equation>\frac {\partial f}{\partial u} = \int \frac {\partial^ {2} f}{\partial u \partial v} \mathrm {d} v = \int \frac {1}{2 5} \mathrm {d} v = \frac {v}{2 5} + C _ {1} (u),</equation>其中<equation>C_{1}(u)</equation>是关于<equation>u</equation>的一元函数.

由于<equation>\frac{\partial f(u,0)}{\partial u}=u\mathrm{e}^{-u}</equation>，故在<equation>\frac{\partial f}{\partial u}=\frac{v}{25}+C_{1}(u)</equation>中令<equation>v=0</equation>可得<equation>C_{1}(u)=u\mathrm{e}^{-u}.</equation>于是，<equation>\frac{\partial f}{\partial u}=\frac{v}{25}+</equation><equation>u\mathrm{e}^{-u}.</equation>对<equation>\frac{\partial f}{\partial u}</equation>关于 u积分可得，<equation>\begin{aligned} f (u, v) &= \int \frac {\partial f}{\partial u} \mathrm {d} u = \int \left(\frac {v}{2 5} + u \mathrm {e} ^ {- u}\right) \mathrm {d} u = \frac {u v}{2 5} - \int u \mathrm {d} \left(\mathrm {e} ^ {- u}\right) \\ &= \frac {u v}{2 5} - \left(u \mathrm {e} ^ {- u} - \int \mathrm {e} ^ {- u} \mathrm {d} u\right) = \frac {u v}{2 5} - u \mathrm {e} ^ {- u} - \mathrm {e} ^ {- u} + C _ {2} (v), \end{aligned}</equation>其中<equation>C_{2}(v)</equation>是关于<equation>v</equation>的一元函数.

由于<equation>f(0,v) = \frac{1}{50} v^{2} - 1</equation>，故在<equation>f(u,v) = \frac{uv}{25} - u\mathrm{e}^{-u} - \mathrm{e}^{-u} + C_{2}(v)</equation>中令<equation>u = 0</equation>可得，<equation>\frac{v^2}{50} - 1 = -1</equation><equation>+C_{2}(v)</equation>，即<equation>C_{2}(v) = \frac{v^{2}}{50}</equation>.

因此，<equation>f ( u,v) = \frac{u v}{2 5} +\frac{v^{2}}{5 0} -(u + 1) \mathrm{e}^{-u}.</equation>

---

**2023年第13题 | 填空题 | 5分**

13. 设函数<equation>z=z(x,y)</equation>由<equation>\mathrm{e}^{z}+xz=2x-y</equation>确定，则<equation>\left.\frac{\partial^{2} z}{\partial x^{2}}\right|_{(1,1)}=</equation>___

**答案:**# 3 2

**解析:**解 将 x=1，y=1 代入已知方程，可得<equation>\mathrm{e}^{z}+z=1.</equation>考虑<equation>f ( z )=\mathrm{e}^{z}+z-1.</equation>由于<equation>f^{\prime}(z)=\mathrm{e}^{z}+1>0,f(0)=0</equation>，故 f(z)单调增加，z=0是f(z)的唯一零点.于是，<equation>z ( 1,1 )=0.</equation>对方程<equation>\mathrm{e}^{z}+xz=2x-y</equation>两端关于 x求偏导数，可得<equation>\mathrm {e} ^ {z} \frac {\partial z}{\partial x} + z + x \frac {\partial z}{\partial x} = 2.</equation>将<equation>x=1,y=1,z=0</equation>代入（1）式可得<equation>2\frac{\partial z}{\partial x}=2.</equation>因此，<equation>\left.\frac{\partial z}{\partial x}\right|_{(1,1)}=1.</equation>对（1）式两端继续关于 x求偏导数，可得<equation>\mathrm {e} ^ {z} \left(\frac {\partial z}{\partial x}\right) ^ {2} + \mathrm {e} ^ {z} \frac {\partial^ {2} z}{\partial x ^ {2}} + \frac {\partial z}{\partial x} + \frac {\partial z}{\partial x} + x \frac {\partial^ {2} z}{\partial x ^ {2}} = 0.</equation>整理可得<equation>\mathrm {e} ^ {z} \left(\frac {\partial z}{\partial x}\right) ^ {2} + 2 \frac {\partial z}{\partial x} + \left(\mathrm {e} ^ {z} + x\right) \frac {\partial^ {2} z}{\partial x ^ {2}} = 0.</equation>将<equation>x = 1,y = 1,z = 0,\frac{\partial z}{\partial x}\bigg|_{(1,1)} = 1</equation>代入（2）式可得<equation>3 + 2\frac{\partial^{2}z}{\partial x^{2}} = 0.</equation>因此，<equation>\frac{\partial^{2}z}{\partial x^{2}}\bigg|_{(1,1)} = -\frac{3}{2}.</equation>

---

**2022年第4题 | 选择题 | 5分 | 答案: C**

4. 已知 f(t) 连续，令<equation>F ( x,y)=\int_{0}^{x-y} ( x-y-t ) f ( t ) \mathrm{d} t</equation>，则（    ）<equation>\begin{aligned} \mathrm {A.} \frac {\partial F}{\partial x} &= \frac {\partial F}{\partial y}, \frac {\partial^ {2} F}{\partial x ^ {2}} = \frac {\partial^ {2} F}{\partial y ^ {2}} \\ \mathrm {C.} \frac {\partial F}{\partial x} &= - \frac {\partial F}{\partial y}, \frac {\partial^ {2} F}{\partial x ^ {2}} = \frac {\partial^ {2} F}{\partial y ^ {2}} \end{aligned}</equation><equation>\begin{aligned} B. \frac {\partial F}{\partial x} &= \frac {\partial F}{\partial y}, \frac {\partial^ {2} F}{\partial x ^ {2}} = - \frac {\partial^ {2} F}{\partial y ^ {2}} \\ D. \frac {\partial F}{\partial x} &= - \frac {\partial F}{\partial y}, \frac {\partial^ {2} F}{\partial x ^ {2}} = - \frac {\partial^ {2} F}{\partial y ^ {2}} \end{aligned}</equation>

答案: C

**解析:**解 整理 F(x,y）的表达式.<equation>F (x, y) = \int_ {0} ^ {x - y} (x - y - t) f (t) \mathrm {d} t = (x - y) \int_ {0} ^ {x - y} f (t) \mathrm {d} t - \int_ {0} ^ {x - y} t f (t) \mathrm {d} t.</equation>分别计算<equation>\frac{\partial F}{\partial x},\frac{\partial^{2}F}{\partial x^{2}},\frac{\partial F}{\partial y},\frac{\partial^{2}F}{\partial y^{2}}.</equation><equation>\frac {\partial F}{\partial x} = (x - y) f (x - y) + \int_ {0} ^ {x - y} f (t) \mathrm {d} t - (x - y) f (x - y) = \int_ {0} ^ {x - y} f (t) \mathrm {d} t,</equation><equation>\frac {\partial^ {2} F}{\partial x ^ {2}} = \frac {\partial \left[ \int_ {0} ^ {x - y} f (t) \mathrm {d} t \right]}{\partial x} = f (x - y),</equation><equation>\frac {\partial F}{\partial y} = - (x - y) f (x - y) - \int_ {0} ^ {x - y} f (t) \mathrm {d} t + (x - y) f (x - y) = - \int_ {0} ^ {x - y} f (t) \mathrm {d} t,</equation><equation>\frac {\partial^ {2} F}{\partial y ^ {2}} = \frac {\partial \left[ - \int_ {0} ^ {x - y} f (t) \mathrm {d} t \right]}{\partial y} = f (x - y).</equation>因此，<equation>\frac{\partial F}{\partial x}=-\frac{\partial F}{\partial y},\frac{\partial^{2}F}{\partial x^{2}}=\frac{\partial^{2}F}{\partial y^{2}}.</equation>应选C.

---

**2021年第13题 | 填空题 | 5分**

13. 设函数<equation>z=z(x,y)</equation>由方程<equation>( x+1 ) z+y \ln z-\arctan ( 2 x y )=1</equation>确定，则<equation>\left. \frac{\partial z}{\partial x}\right|_{(0,2)}=</equation>___

**答案:**```latex

1.
```
**解析: **解 对方程两端关于 x求偏导，可得<equation>z + (x + 1) \frac {\partial z}{\partial x} + y \cdot \frac {1}{z} \cdot \frac {\partial z}{\partial x} - \frac {2 y}{1 + 4 x ^ {2} y ^ {2}} = 0.</equation>解得<equation>\left(x + 1 + \frac {y}{z}\right) \frac {\partial z}{\partial x} = \frac {2 y}{1 + 4 x ^ {2} y ^ {2}} - z.</equation>将 x=0,y=2代入方程（x+1）z+y<equation>\ln z-\arctan(2 x y)=1</equation>可得 z+2<equation>\ln z=1</equation>.观察可得 z=1 是该方程的一个实根.计算函数 f（z）=z+2<equation>\ln z-1</equation>的导数可得<equation>f^{\prime}(z)=1+\frac{2}{z}>0.</equation>于是，函数<equation>f(z)=z+2\ln z-1</equation>单调增加，z=1是该方程的唯一实根.

将 x=0,y=2,z=1代入（1）式可得<equation>3\frac{\partial z}{\partial x}\bigg|_{(0,2)}=3.</equation>解得<equation>\frac{\partial z}{\partial x}\bigg|_{(0,2)}=1.</equation>

---

**2020年第5题 | 选择题 | 4分 | 答案: B**
5. 关于函数<equation>f ( x, y )=\left\{\begin{array}{l l}x y,&x y\neq 0\\ x,&y=0\\ y,&x=0\end{array} \right.</equation>给出以下结论：<equation>\textcircled{1} \left. \frac{\partial f}{\partial x} \right|_{(0,0)}=1;</equation><equation>\textcircled{2} \left. \frac{\partial^{2} f}{\partial x \partial y} \right|_{(0,0)}=1;</equation><equation>\textcircled{3} \lim_{(x,y)\to(0,0)}f(x,y)=0;</equation><equation>\textcircled{4} \lim_{y\to0}\lim_{x\to0}f(x,y)=0</equation>其中正确的个数是（    ）

A.4 B.3 C.2 D.1
答案: B
**解析: **解 根据偏导数的定义，<equation>\left. \frac {\partial f}{\partial x} \right| _ {(0, 0)} = \lim _ {x \rightarrow 0} \frac {f (x , 0) - f (0 , 0)}{x - 0} = \lim _ {x \rightarrow 0} \frac {x - 0}{x} = 1.</equation><equation>\textcircled{1}</equation>正确.

根据偏导数的定义，<equation>\left. \frac {\partial^ {2} f}{\partial x \partial y} \right| _ {(0, 0)} = \lim _ {y \rightarrow 0} \frac {\left. \frac {\partial f (x , y)}{\partial x} \right| _ {x = 0} - \left. \frac {\partial f (x , y)}{\partial x} \right| _ {x = 0}}{y - 0}.</equation>但是根据定义，当 y≠0时，<equation>\left. \frac {\partial f (x , y)}{\partial x} \right| _ {x = 0 \atop y \neq 0} = \lim _ {x \rightarrow 0} \frac {f (x , y) - f (0 , y)}{x - 0} = \lim _ {x \rightarrow 0} \frac {x y - y}{x} = \infty .</equation><equation>\frac{\partial f(x,y)}{\partial x}\bigg|_{x=0}</equation>不存在，<equation>\frac{\partial^{2}f}{\partial x\partial y}\bigg|_{(0,0)}</equation>当然也不存在.<equation>\textcircled{2}</equation>不正确.

根据 f(x,y）的定义，

- 当 xy≠0时，<equation>0\leqslant|f(x,y)-0|=|xy|\leqslant\frac{x^{2}+y^{2}}{2}<x^{2}+y^{2}</equation>，当 0 < x²+y² < 1时，<equation>x^{2}+y^{2}<\sqrt{x^{2}+y^{2}};</equation>- 当<equation>x = 0</equation>时，<equation>0\leqslant |f(x,y) - 0| = |y| \leqslant \sqrt{x^2 + y^2};</equation>- 当<equation>y = 0</equation>时，<equation>0\leqslant |f(x,y) - 0| = |x|\leqslant \sqrt{x^2 + y^2}.</equation>而<equation>\lim_{(x,y)\to (0,0)}\sqrt{x^2 + y^2} = 0</equation>，故<equation>\lim_{(x,y)\to (0,0)}f(x,y) = 0.</equation><equation>\textcircled{3}</equation>正确.

按照累次极限的顺序，先计算<equation>\lim_{x\to 0}f(x,y)</equation>，再计算<equation>\lim_{y\to 0}\lim_{x\to 0}f(x,y).</equation>根据累次极限的定义，只需考虑 x≠0，y≠0的情况.<equation>\lim _ {x \rightarrow 0} f (x, y) = \lim _ {x \rightarrow 0} x y = 0, \quad \lim _ {y \rightarrow 0} \lim _ {x \rightarrow 0} f (x, y) = \lim _ {y \rightarrow 0} 0 = 0.</equation><equation>\textcircled{4}</equation>正确.

因此，共有3个结论正确，应选B.

---

**2019年第11题 | 填空题 | 4分**
11. 设函数 f(u)可导，<equation>z=y f\left(\frac{y^{2}}{x}\right)</equation>，则<equation>2 x \frac{\partial z}{\partial x}+y \frac{\partial z}{\partial y}=</equation>___
**解析: **分别计算<equation>\frac{\partial z}{\partial x},\frac{\partial z}{\partial y}.</equation><equation>\frac {\partial z}{\partial x} = y f ^ {\prime} \left(\frac {y ^ {2}}{x}\right) \cdot \left(- \frac {y ^ {2}}{x ^ {2}}\right) = - \frac {y ^ {3}}{x ^ {2}} f ^ {\prime} \left(\frac {y ^ {2}}{x}\right).</equation><equation>\frac {\partial z}{\partial y} = f \left(\frac {y ^ {2}}{x}\right) + y \cdot f ^ {\prime} \left(\frac {y ^ {2}}{x}\right) \cdot \frac {2 y}{x} = f \left(\frac {y ^ {2}}{x}\right) + \frac {2 y ^ {2}}{x} f ^ {\prime} \left(\frac {y ^ {2}}{x}\right).</equation>代入<equation>2 x \frac{\partial z}{\partial x}+y\frac{\partial z}{\partial y}</equation>可得，<equation>2 x \frac {\partial z}{\partial x} + y \frac {\partial z}{\partial y} = - \frac {2 y ^ {3}}{x} f ^ {\prime} \left(\frac {y ^ {2}}{x}\right) + \frac {2 y ^ {3}}{x} f ^ {\prime} \left(\frac {y ^ {2}}{x}\right) + y f \left(\frac {y ^ {2}}{x}\right) = y f \left(\frac {y ^ {2}}{x}\right).</equation>

---

**2019年第20题 | 解答题 | 11分**
20. （本题满分11分）

已知函数 u(x,y)满足<equation>2\frac{\partial^{2} u}{\partial x^{2}}-2\frac{\partial^{2} u}{\partial y^{2}}+3\frac{\partial u}{\partial x}+3\frac{\partial u}{\partial y}=0</equation>，求 a,b的值，使得在变换<equation>u(x,y)=v(x,y)\mathrm{e}^{ax+by}</equation>下，上述等式可化为 v(x,y)不含一阶偏导数的等式.
**答案: **<equation>a = - \frac {3}{4}, b = \frac {3}{4}.</equation>
**解析: **由<equation>u ( x,y)=v ( x,y)\mathrm{e}^{a x+b y}</equation>可得，<equation>\frac {\partial u}{\partial x} = \frac {\partial v}{\partial x} \cdot \mathrm {e} ^ {a x + b y} + \mathrm {e} ^ {a x + b y} \cdot a v = \mathrm {e} ^ {a x + b y} \left(\frac {\partial v}{\partial x} + a v\right).</equation><equation>\frac {\partial u}{\partial y} = \frac {\partial v}{\partial y} \cdot \mathrm {e} ^ {a x + b y} + \mathrm {e} ^ {a x + b y} \cdot b v = \mathrm {e} ^ {a x + b y} \left(\frac {\partial v}{\partial y} + b v\right).</equation><equation>\frac {\partial^ {2} u}{\partial x ^ {2}} = a \cdot \mathrm {e} ^ {a x + b y} \left(\frac {\partial v}{\partial x} + a v\right) + \mathrm {e} ^ {a x + b y} \left(\frac {\partial^ {2} v}{\partial x ^ {2}} + a \frac {\partial v}{\partial x}\right) = \mathrm {e} ^ {a x + b y} \left(2 a \frac {\partial v}{\partial x} + a ^ {2} v + \frac {\partial^ {2} v}{\partial x ^ {2}}\right).</equation><equation>\frac {\partial^ {2} u}{\partial y ^ {2}} = b \cdot \mathrm {e} ^ {a x + b y} \left(\frac {\partial v}{\partial y} + b v\right) + \mathrm {e} ^ {a x + b y} \left(\frac {\partial^ {2} v}{\partial y ^ {2}} + b \frac {\partial v}{\partial y}\right) = \mathrm {e} ^ {a x + b y} \left(2 b \frac {\partial v}{\partial y} + b ^ {2} v + \frac {\partial^ {2} v}{\partial y ^ {2}}\right).</equation>代入已知等式可得，<equation>\mathrm {e} ^ {a x + b y} \left[ 2 \left(2 a \frac {\partial v}{\partial x} + a ^ {2} v + \frac {\partial^ {2} v}{\partial x ^ {2}}\right) - 2 \left(2 b \frac {\partial v}{\partial y} + b ^ {2} v + \frac {\partial^ {2} v}{\partial y ^ {2}}\right) + 3 \left(\frac {\partial v}{\partial x} + a v\right) + 3 \left(\frac {\partial v}{\partial y} + b v\right) \right] = 0.</equation>整理上式，可得<equation>2 \frac {\partial^ {2} v}{\partial x ^ {2}} - 2 \frac {\partial^ {2} v}{\partial y ^ {2}} + (4 a + 3) \frac {\partial v}{\partial x} + (- 4 b + 3) \frac {\partial v}{\partial y} + \left(2 a ^ {2} v - 2 b ^ {2} v + 3 a v + 3 b v\right) = 0.</equation>要使得（1）式中不含有 v(x,y) 的一阶偏导数，需使<equation>4 a+3=0,-4 b+3=0</equation>.解得 a=-<equation>\frac{3}{4},</equation><equation>b=\frac{3}{4}.</equation>因此，<equation>a=-\frac{3}{4}, b=\frac{3}{4}.</equation>

---

**2018年第13题 | 填空题 | 4分**
13. 设函数<equation>z=z(x,y)</equation>由方程<equation>\ln z+\mathrm{e}^{z-1}=xy</equation>确定，则<equation>\left.\frac{\partial z}{\partial x}\right|_{(2,\frac{1}{2})}=</equation>___
**答案: **## 1 4.
**解析: **解（法一）对已知方程两端关于 x求导，可得<equation>\frac {1}{z} \cdot \frac {\partial z}{\partial x} + \mathrm {e} ^ {z - 1} \cdot \frac {\partial z}{\partial x} = y.</equation>将 x=2，<equation>y=\frac{1}{2}</equation>代入已知方程可得，<equation>\ln z+\mathrm{e}^{z-1}=1.</equation>解得 z=1.

将<equation>x = 2, y = \frac{1}{2}, z = 1</equation>代入（1）式可得，<equation>2\frac{\partial z}{\partial x}\bigg|_{(2,\frac{1}{2})} = \frac{1}{2}</equation>，即<equation>\frac{\partial z}{\partial x}\bigg|_{(2,\frac{1}{2})} = \frac{1}{4}</equation>.

（法二）记<equation>F ( x,y,z)=\ln z+\mathrm{e}^{z-1}-x y</equation>，则<equation>F_{x}^{\prime}(x,y,z)=-y,F_{z}^{\prime}(x,y,z)=\frac{1}{z}+\mathrm{e}^{z-1}.</equation>将 x=2，y<equation>=\frac{1}{2}</equation>代入已知方程可得，<equation>\ln z+\mathrm{e}^{z-1}=1.</equation>解得 z=1.

根据隐函数存在定理，<equation>\left. \frac {\partial z}{\partial x} \right| _ {\left(2, \frac {1}{2}\right)} = - \frac {F _ {x} ^ {\prime} \left(2 , \frac {1}{2} , 1\right)}{F _ {z} ^ {\prime} \left(2 , \frac {1}{2} , 1\right)} = - \frac {- \frac {1}{2}}{2} = \frac {1}{4}.</equation>

---

**2017年第5题 | 选择题 | 4分 | 答案: D**
5. 设 f(x,y)具有一阶偏导数，且对任意的(x,y)，都有<equation>\frac{\partial f(x,y)}{\partial x}>0,\frac{\partial f(x,y)}{\partial y}<0</equation>，则（    ）

A. f(0,0)>f(1,1) B. f(0,0)<f(1,1) C. f(0,1)>f(1,0) D. f(0,1)<f(1,0)
答案: D
**解析: **解固定变量 y=0，则 f(x,0)是关于 x的一元函数.由于<equation>\frac{\partial f(x,y)}{\partial x}>0</equation>，故 f(x,0)是关于 x的单调增加函数.于是，<equation>f (1, 0) - f (0, 0) > 0.</equation>固定变量 x=0，则 f（0,y）是关于 y的一元函数.由于<equation>\frac{\partial f(x,y)}{\partial y}<0</equation>，故 f（0,y）是关于 y的单调减少函数.于是，<equation>f (0, 1) - f (0, 0) < 0.</equation>因此，<equation>f ( 1, 0 ) > f ( 0, 0 ) > f ( 0, 1 )</equation>.应选D.

---

**2017年第16题 | 解答题 | 10分**
16. (本题满分10分）设函数<equation>f(u,v)</equation>具有2阶连续偏导数，<equation>y=f(\mathrm{e}^{x},\cos x)</equation>，求<equation>\left.\frac{\mathrm{d} y}{\mathrm{d} x}\right|_{x=0},\left.\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\right|_{x=0}.</equation>
**答案: **<equation>\frac{\mathrm{d} y}{\mathrm{d} x}\bigg|_{x=0}=f_{1}^{\prime}(1,1),\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\bigg|_{x=0}=f_{1}^{\prime}(1,1)+f_{11}^{\prime\prime}(1,1)-f_{2}^{\prime}(1,1).</equation>
**解析: **解分别记 f（u,v）关于第一个变量、第二个变量的偏导数为<equation>f_{1}^{\prime}, f_{2}^{\prime}. f_{1}^{\prime}, f_{2}^{\prime}</equation>具有与 f相同的复合结构.根据链式法则，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = f _ {1} ^ {\prime} \frac {\mathrm {d} \left(\mathrm {e} ^ {x}\right)}{\mathrm {d} x} + f _ {2} ^ {\prime} \frac {\mathrm {d} (\cos x)}{\mathrm {d} x} = f _ {1} ^ {\prime} \mathrm {e} ^ {x} - f _ {2} ^ {\prime} \sin x.</equation>代入 x=0，得<equation>\left. \frac {\mathrm {d} y}{\mathrm {d} x} \right| _ {x = 0} = f _ {1} ^ {\prime} (1, 1) - 0 = f _ {1} ^ {\prime} (1, 1).</equation>对（1）式两端关于 x求导，得<equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = f _ {1} ^ {\prime} \mathrm {e} ^ {x} + \mathrm {e} ^ {x} \left(f _ {1 1} ^ {\prime \prime} \mathrm {e} ^ {x} - f _ {1 2} ^ {\prime \prime} \sin x\right) - f _ {2} ^ {\prime} \cos x - \sin x \left(f _ {2 1} ^ {\prime \prime} \mathrm {e} ^ {x} - f _ {2 2} ^ {\prime \prime} \sin x\right).</equation>代入 x=0，得<equation>\left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {x = 0} = f _ {1} ^ {\prime} (1, 1) + f _ {1 1} ^ {\prime \prime} (1, 1) - f _ {2} ^ {\prime} (1, 1).</equation>

---

**2016年第6题 | 选择题 | 4分 | 答案: D**
6. 已知函数<equation>f(x,y)=\frac{\mathrm{e}^{x}}{x-y}</equation>，则（    ）

A.<equation>f_{x}^{\prime}-f_{y}^{\prime}=0</equation>B.<equation>f_{x}^{\prime}+f_{y}^{\prime}=0</equation>C.<equation>f_{x}^{\prime}-f_{y}^{\prime}=f</equation>D.<equation>f_{x}^{\prime}+f_{y}^{\prime}=f</equation>
答案: D
**解析: **分别计算<equation>f_{x}^{\prime}, f_{y}^{\prime}</equation>得<equation>f _ {x} ^ {\prime} = \frac {\mathrm {e} ^ {x} (x - y) - \mathrm {e} ^ {x}}{(x - y) ^ {2}}, \quad f _ {y} ^ {\prime} = \frac {\mathrm {e} ^ {x}}{(x - y) ^ {2}}.</equation>因此，<equation>f _ {x} ^ {\prime} + f _ {y} ^ {\prime} = \frac {\mathrm {e} ^ {x} (x - y)}{(x - y) ^ {2}} = \frac {\mathrm {e} ^ {x}}{x - y} = f.</equation>应选 D.

---

**2015年第5题 | 选择题 | 4分 | 答案: D**
5. 设函数 f（u,v）满足<equation>f \left( x+y, \frac{y}{x} \right)=x^{2}-y^{2}</equation>，则<equation>\left. \frac{\partial f}{\partial u} \right|_{u=1},\left. \frac{\partial f}{\partial v} \right|_{u=1}</equation>依次是（    )

A.<equation>\frac{1}{2},0</equation>B. 0,<equation>\frac{1}{2}</equation>C.<equation>-\frac{1}{2},0</equation>D. 0,<equation>-\frac{1}{2}</equation>
答案: D
**解析: **解（法一）由<equation>u=x+y,v=\frac{y}{x}</equation>解出x，y关于u，v的表达式，从而将<equation>f\left(x+y,\frac{y}{x}\right)</equation>写成关于 u,v的表达式，进而求得<equation>\frac{\partial f}{\partial u}\bigg|_{u=1}\,,\frac{\partial f}{\partial v}\bigg|_{u=1}.</equation>由<equation>\left\{\begin{array}{l l}u=x+y,\\ v=\frac{y}{x},\end{array}\right.</equation>解得<equation>\left\{\begin{array}{l l}x=\frac{u}{1+v},\\ y=\frac{uv}{1+v},\end{array}\right.</equation>故<equation>f (u, v) = \left(\frac {u}{1 + v}\right) ^ {2} - \left(\frac {u v}{1 + v}\right) ^ {2} = \frac {u ^ {2} \left(1 - v ^ {2}\right)}{\left(1 + v\right) ^ {2}} = u ^ {2} \left(\frac {1 - v}{1 + v}\right) = u ^ {2} \left(\frac {2}{1 + v} - 1\right).</equation>因此，<equation>\left. \frac {\partial f}{\partial u} \right| _ {u = 1 \atop v = 1} = 2 u \left(\frac {2}{1 + v} - 1\right) \Bigg | _ {u = 1 \atop v = 1} = 0, \quad \left. \frac {\partial f}{\partial v} \right| _ {u = 1 \atop v = 1} = u ^ {2} \cdot \frac {- 2}{(1 + v) ^ {2}} \Bigg | _ {u = 1 \atop v = 1} = - \frac {1}{2}.</equation>应选 D.

（法二）一方面，<equation>\mathrm {d} f \left(x + y, \frac {y}{x}\right) = \frac {\partial \left(x ^ {2} - y ^ {2}\right)}{\partial x} \mathrm {d} x + \frac {\partial \left(x ^ {2} - y ^ {2}\right)}{\partial y} \mathrm {d} y = 2 x \mathrm {d} x - 2 y \mathrm {d} y;</equation>另一方面，<equation>\begin{aligned} \mathrm {d} f \left(x + y, \frac {y}{x}\right) \frac {u = x + y}{v = \frac {y}{x}} \frac {\partial f}{\partial u} \mathrm {d} u + \frac {\partial f}{\partial v} \mathrm {d} v &= \frac {\partial f}{\partial u} (\mathrm {d} x + \mathrm {d} y) + \frac {\partial f}{\partial v} \left(- \frac {y}{x ^ {2}} \mathrm {d} x + \frac {1}{x} \mathrm {d} y\right) \\ &= \left(\frac {\partial f}{\partial u} - \frac {y}{x ^ {2}} \frac {\partial f}{\partial v}\right) \mathrm {d} x + \left(\frac {\partial f}{\partial u} + \frac {1}{x} \frac {\partial f}{\partial v}\right) \mathrm {d} y. \end{aligned}</equation>比较 dx，dy的系数可得<equation>\left\{ \begin{array}{l} \frac {\partial f}{\partial u} - \frac {y}{x ^ {2}} \frac {\partial f}{\partial v} = 2 x, \\ \frac {\partial f}{\partial u} + \frac {1}{x} \frac {\partial f}{\partial v} = - 2 y. \end{array} \right.</equation>当 u=1，v=1时，由<equation>\left\{\begin{array}{l l}x+y=u,\\ \frac{y}{x}=v\end{array}\right.</equation>解得 x =<equation>\frac{1}{2}</equation>, y =<equation>\frac{1}{2}</equation>. 代入上面的方程组，可得<equation>\frac{\partial f}{\partial u}\bigg|_{u=1} = 0,</equation><equation>\frac{\partial f}{\partial v}\bigg|_{u=1} = -\frac{1}{2}</equation>. 应选D.

---

**2013年第5题 | 选择题 | 4分 | 答案: A**
5. 设<equation>z=\frac{y}{x} f(xy)</equation>，其中函数 f可微，则<equation>\frac{x}{y}\frac{\partial z}{\partial x}+\frac{\partial z}{\partial y}=(\quad)</equation>A.<equation>2 y f^{\prime}( x y )</equation>B.<equation>- 2 y f^{\prime}( x y )</equation>C.<equation>\frac{2}{x} f(x y)</equation>D.<equation>- \frac{2}{x} f(x y)</equation>
答案: A
**解析: **解（法一）用链式法则分别求<equation>\frac{\partial z}{\partial x},\frac{\partial z}{\partial y}</equation><equation>\frac {\partial z}{\partial x} = - \frac {y}{x ^ {2}} f (x y) + \frac {y}{x} f ^ {\prime} (x y) \cdot y = - \frac {y}{x ^ {2}} f (x y) + \frac {y ^ {2}}{x} f ^ {\prime} (x y),</equation><equation>\frac {\partial z}{\partial y} = \frac {1}{x} f (x y) + \frac {y}{x} f ^ {\prime} (x y) \cdot x = \frac {1}{x} f (x y) + y f ^ {\prime} (x y).</equation>因此，<equation>\frac {x}{y} \frac {\partial z}{\partial x} + \frac {\partial z}{\partial y} = - \frac {1}{x} f (x y) + y f ^ {\prime} (x y) + \frac {1}{x} f (x y) + y f ^ {\prime} (x y) = 2 y f ^ {\prime} (x y).</equation>应选A.

（法二）利用全微分形式的不变性.<equation>\begin{aligned} \mathrm {d} z &= f (x y) \mathrm {d} \left(\frac {y}{x}\right) + \frac {y}{x} \mathrm {d} [ f (x y) ] \\ &= - \frac {y}{x ^ {2}} f (x y) \mathrm {d} x + \frac {1}{x} f (x y) \mathrm {d} y + \frac {y}{x} f ^ {\prime} (x y) \cdot y \mathrm {d} x + \frac {y}{x} f ^ {\prime} (x y) \cdot x \mathrm {d} y \\ &= \left[ \frac {y ^ {2}}{x} f ^ {\prime} (x y) - \frac {y}{x ^ {2}} f (x y) \right] \mathrm {d} x + \left[ y f ^ {\prime} (x y) + \frac {1}{x} f (x y) \right] \mathrm {d} y. \end{aligned}</equation>因此，<equation>\frac {\partial z}{\partial x} = - \frac {y}{x ^ {2}} f (x y) + \frac {y ^ {2}}{x} f ^ {\prime} (x y), \quad \frac {\partial z}{\partial y} = \frac {1}{x} f (x y) + y f ^ {\prime} (x y).</equation>其余同法一.

---

**2012年第5题 | 选择题 | 4分 | 答案: D**
5. 设函数 f(x,y)可微，且对任意的 x,y都有<equation>\frac{\partial f(x,y)}{\partial x}>0,\frac{\partial f(x,y)}{\partial y}<0</equation>，则使不等式<equation>f(x_{1},y_{1})<f(x_{2},y_{2})</equation>成立的一个充分条件是（    ）

A.<equation>x_{1}>x_{2},y_{1}<y_{2}</equation>B.<equation>x_{1}>x_{2},y_{1}>y_{2}</equation>C.<equation>x_{1}<x_{2},y_{1}<y_{2}</equation>D.<equation>x_{1}<x_{2},y_{1}>y_{2}</equation>
答案: D
**解析: **解 将<equation>f \left(x_{2}, y_{2}\right)-f \left(x_{1}, y_{1}\right)</equation>看作两部分的和，即<equation>f \left(x _ {2}, y _ {2}\right) - f \left(x _ {1}, y _ {1}\right) = f \left(x _ {2}, y _ {2}\right) - f \left(x _ {1}, y _ {2}\right) + f \left(x _ {1}, y _ {2}\right) - f \left(x _ {1}, y _ {1}\right).</equation><equation>f ( x, y_{2} )</equation>为关于<equation>x</equation>的一元函数.由于<equation>\frac{\partial f(x,y)}{\partial x} > 0</equation>，故当<equation>x_{2} > x_{1}</equation>时，<equation>f \left(x _ {2}, y _ {2}\right) - f \left(x _ {1}, y _ {2}\right) > 0.</equation><equation>f ( x_{1}, y )</equation>为关于y的一元函数.由于<equation>\frac{\partial f ( x,y)}{\partial y} < 0</equation>，故当<equation>y_{2} < y_{1}</equation>时，<equation>f \left(x _ {1}, y _ {2}\right) - f \left(x _ {1}, y _ {1}\right) > 0.</equation>因此，当<equation>x_{1} < x_{2}, y_{1} > y_{2}</equation>时，<equation>f \left(x _ {2}, y _ {2}\right) - f \left(x _ {1}, y _ {1}\right) = f \left(x _ {2}, y _ {2}\right) - f \left(x _ {1}, y _ {2}\right) + f \left(x _ {1}, y _ {2}\right) - f \left(x _ {1}, y _ {1}\right) > 0.</equation>应选 D.

---

**2012年第11题 | 填空题 | 4分**
11. 设<equation>z=f\left(\ln x+\frac{1}{y}\right)</equation>，其中函数 f(u)可微，则<equation>x\frac{\partial z}{\partial x}+y^{2}\frac{\partial z}{\partial y}=</equation>___
**解析: **利用链式法则，<equation>\frac {\partial z}{\partial x} = f ^ {\prime} \left(\ln x + \frac {1}{y}\right) \cdot \frac {1}{x}, \quad \frac {\partial z}{\partial y} = f ^ {\prime} \left(\ln x + \frac {1}{y}\right) \cdot \left(- \frac {1}{y ^ {2}}\right).</equation>因此，<equation>x \frac {\partial z}{\partial x} + y ^ {2} \frac {\partial z}{\partial y} = f ^ {\prime} \left(\ln x + \frac {1}{y}\right) - f ^ {\prime} \left(\ln x + \frac {1}{y}\right) = 0.</equation>

---

**2011年第17题 | 解答题 | 10分**
17. (本题满分9分)

设函数 z = f(xy, yg(x))，其中函数 f具有二阶连续偏导数，函数 g(x)可导且在 x=1处取得极值 g(1)=1，求<equation>\left.\frac{\partial^{2} z}{\partial x \partial y}\right|_{x=1}</equation>y=1.
**答案: **(17)<equation>f_{1}^{\prime}(1,1)+f_{11}^{\prime\prime}(1,1)+f_{12}^{\prime\prime}(1,1).</equation>
**解析: **由链式法则，<equation>\begin{array}{l} \frac {\partial z}{\partial x} = f _ {1} ^ {\prime} \frac {\partial (x y)}{\partial x} + f _ {2} ^ {\prime} \frac {\partial [ y g (x) ]}{\partial x} = y f _ {1} ^ {\prime} + y g ^ {\prime} (x) f _ {2} ^ {\prime}, \\ \frac {\partial^ {2} z}{\partial x \partial y} = \frac {\partial \left[ y \left(f _ {1} ^ {\prime} + g ^ {\prime} (x) f _ {2} ^ {\prime}\right) \right]}{\partial y} \\ = f _ {1} ^ {\prime} + g ^ {\prime} (x) f _ {2} ^ {\prime} + y \left\{f _ {1 1} ^ {\prime \prime} \frac {\partial (x y)}{\partial y} + f _ {1 2} ^ {\prime \prime} \frac {\partial [ y g (x) ]}{\partial y} + g ^ {\prime} (x) f _ {2 1} ^ {\prime \prime} \frac {\partial (x y)}{\partial y} + g ^ {\prime} (x) f _ {2 2} ^ {\prime \prime} \frac {\partial [ y g (x) ]}{\partial y} \right\} \\ = f _ {1} ^ {\prime} + g ^ {\prime} (x) f _ {2} ^ {\prime} + y \left[ x f _ {1 1} ^ {\prime \prime} + g (x) f _ {1 2} ^ {\prime \prime} + x g ^ {\prime} (x) f _ {2 1} ^ {\prime \prime} + g (x) g ^ {\prime} (x) f _ {2 2} ^ {\prime \prime} \right]. \\ \end{array}</equation>由<equation>g ( x )</equation>可导且在<equation>x=1</equation>处取得极值<equation>g ( 1 )=1</equation>知，<equation>g^{\prime}(1)=0.</equation>将<equation>x=1, y=1, g ( 1 )=1,</equation><equation>g^{\prime}(1)=0</equation>代入<equation>\frac{\partial^{2} z}{\partial x \partial y}</equation>，得<equation>\left. \frac {\partial^ {2} z}{\partial x \partial y} \right| _ {x = 1 \atop y = 1} = f _ {1} ^ {\prime} (1, 1) + f _ {1 1} ^ {\prime \prime} (1, 1) + f _ {1 2} ^ {\prime \prime} (1, 1).</equation>

---

**2010年第5题 | 选择题 | 4分 | 答案: B**
5. 设函数 z=z(x,y)由方程<equation>F\left( \frac{y}{x},\frac{z}{x} \right)=0</equation>确定，其中 F为可微函数，且<equation>F_{2}^{\prime}\neq0</equation>，则<equation>x\frac{\partial z}{\partial x}+y\frac{\partial z}{\partial y}=</equation>(    )

A. x B. z C. -x D. -z
答案: B
**解析: **解对方程<equation>F\left(\frac{y}{x},\frac{z}{x}\right)=0</equation>两端同时关于 x，y求偏导数，可得<equation>- \frac {y}{x ^ {2}} F _ {1} ^ {\prime} + \left(- \frac {z}{x ^ {2}} + \frac {1}{x} \cdot \frac {\partial z}{\partial x}\right) F _ {2} ^ {\prime} = 0, \quad \frac {F _ {1} ^ {\prime}}{x} + \frac {F _ {2} ^ {\prime}}{x} \cdot \frac {\partial z}{\partial y} = 0.</equation>由上面两个方程解得，<equation>\frac {\partial z}{\partial x} = \frac {\frac {y}{x} F _ {1} ^ {\prime} + \frac {z}{x} F _ {2} ^ {\prime}}{F _ {2} ^ {\prime}}, \quad \frac {\partial z}{\partial y} = - \frac {F _ {1} ^ {\prime}}{F _ {2} ^ {\prime}}.</equation>因此，<equation>x \frac {\partial z}{\partial x} + y \frac {\partial z}{\partial y} = \frac {y F _ {1} ^ {\prime} + z F _ {2} ^ {\prime} - y F _ {1} ^ {\prime}}{F _ {2} ^ {\prime}} = z.</equation>应选B.

---

**2010年第19题 | 解答题 | 10分**
19. (本题满分11分)

设函数 u=f(x,y)具有二阶连续偏导数，且满足等式<equation>4\frac{\partial^{2} u}{\partial x^{2}}+1 2 \frac{\partial^{2} u}{\partial x \partial y}+5 \frac{\partial^{2} u}{\partial y^{2}}=0</equation>. 确定 a,b的值，使等式在变换<equation>\xi=x+a y,\eta=x+b y</equation>下简化为<equation>\frac{\partial^{2} u}{\partial\xi\partial\eta}=0.</equation>
**答案: **(19)<equation>\left\{ \begin{array}{l l} a = - 2, \\ b = - \frac {2}{5}, \end{array} \right. \text {或} \left\{ \begin{array}{l l} a = - \frac {2}{5}, \\ b = - 2. \end{array} \right.</equation>
**解析: **解 由<equation>\left\{\begin{array}{l l} {\xi=x+ay,} \\ {\eta=x+by,} \end{array} \right.</equation>得<equation>\left\{\begin{array}{l l} {x=\frac{a\eta-b\xi}{a-b},} \\ {y=\frac{\xi-\eta}{a-b}.} \end{array} \right.</equation>注意到<equation>u=f(x,y)</equation>具有二阶连续偏导数.由链式法则，当 a≠b时，<equation>u=f(x(\xi,\eta),y(\xi,\eta))</equation>仍具有关于<equation>\xi,\eta</equation>的二阶连续偏导数，从而<equation>\frac{\partial^{2} u}{\partial\xi\partial\eta}=\frac{\partial^{2} u}{\partial\eta\partial\xi}.</equation>由链式法则可得，<equation>\frac {\partial u}{\partial x} = \frac {\partial u}{\partial \xi} \frac {\partial \xi}{\partial x} + \frac {\partial u}{\partial \eta} \frac {\partial \eta}{\partial x} = \frac {\partial u}{\partial \xi} + \frac {\partial u}{\partial \eta},</equation><equation>\frac {\partial u}{\partial y} = \frac {\partial u}{\partial \xi} \frac {\partial \xi}{\partial y} + \frac {\partial u}{\partial \eta} \frac {\partial \eta}{\partial y} = a \frac {\partial u}{\partial \xi} + b \frac {\partial u}{\partial \eta},</equation><equation>\begin{aligned} \frac {\partial^ {2} u}{\partial x ^ {2}} &= \frac {\partial \left(\frac {\partial u}{\partial \xi} + \frac {\partial u}{\partial \eta}\right)}{\partial x} = \frac {\partial^ {2} u}{\partial \xi^ {2}} \frac {\partial \xi}{\partial x} + \frac {\partial^ {2} u}{\partial \xi \partial \eta} \frac {\partial \eta}{\partial x} + \frac {\partial^ {2} u}{\partial \eta \partial \xi} \frac {\partial \xi}{\partial x} + \frac {\partial^ {2} u}{\partial \eta^ {2}} \frac {\partial \eta}{\partial x} \\ &= \frac {\partial^ {2} u}{\partial \xi^ {2}} + 2 \frac {\partial^ {2} u}{\partial \xi \partial \eta} + \frac {\partial^ {2} u}{\partial \eta^ {2}}, \end{aligned}</equation><equation>\begin{aligned} \frac {\partial^ {2} u}{\partial x \partial y} &= \frac {\partial \left(\frac {\partial u}{\partial \xi} + \frac {\partial u}{\partial \eta}\right)}{\partial y} = \frac {\partial^ {2} u}{\partial \xi^ {2}} \frac {\partial \xi}{\partial y} + \frac {\partial^ {2} u}{\partial \xi \partial \eta} \frac {\partial \eta}{\partial y} + \frac {\partial^ {2} u}{\partial \eta \partial \xi} \frac {\partial \xi}{\partial y} + \frac {\partial^ {2} u}{\partial \eta^ {2}} \frac {\partial \eta}{\partial y} \\ &= a \frac {\partial^ {2} u}{\partial \xi^ {2}} + (a + b) \frac {\partial^ {2} u}{\partial \xi \partial \eta} + b \frac {\partial^ {2} u}{\partial \eta^ {2}}, \end{aligned}</equation><equation>\begin{aligned} \frac {\partial^ {2} u}{\partial y ^ {2}} &= \frac {\partial \left(a \frac {\partial u}{\partial \xi} + b \frac {\partial u}{\partial \eta}\right)}{\partial y} = a \left(\frac {\partial^ {2} u}{\partial \xi^ {2}} \frac {\partial \xi}{\partial y} + \frac {\partial^ {2} u}{\partial \xi \partial \eta} \frac {\partial \eta}{\partial y}\right) + b \left(\frac {\partial^ {2} u}{\partial \eta \partial \xi} \frac {\partial \xi}{\partial y} + \frac {\partial^ {2} u}{\partial \eta^ {2}} \frac {\partial \eta}{\partial y}\right) \\ &= a ^ {2} \frac {\partial^ {2} u}{\partial \xi^ {2}} + 2 a b \frac {\partial^ {2} u}{\partial \xi \partial \eta} + b ^ {2} \frac {\partial^ {2} u}{\partial \eta^ {2}}. \end{aligned}</equation>代入<equation>4\frac{\partial^{2} u}{\partial x^{2}}+1 2\frac{\partial^{2} u}{\partial x \partial y}+5\frac{\partial^{2} u}{\partial y^{2}}=0</equation>，整理得<equation>\left(5 a ^ {2} + 1 2 a + 4\right) \frac {\partial^ {2} u}{\partial \xi^ {2}} + \left(5 b ^ {2} + 1 2 b + 4\right) \frac {\partial^ {2} u}{\partial \eta^ {2}} + \left[ 8 + 1 2 (a + b) + 1 0 a b \right] \frac {\partial^ {2} u}{\partial \xi \partial \eta} = 0.</equation>由上可得，<equation>\left\{ \begin{array}{l} 5 a ^ {2} + 1 2 a + 4 = 0, \\ 5 b ^ {2} + 1 2 b + 4 = 0, \\ 8 + 1 2 (a + b) + 1 0 a b \neq 0. \end{array} \right.</equation>解得<equation>\left\{ \begin{array}{l l} a = - 2, \\ b = - \frac {2}{5}, \end{array} \right. \quad \text {或} \quad \left\{ \begin{array}{l l} a = - \frac {2}{5}, \\ b = - 2. \end{array} \right.</equation>

---

**2009年第17题 | 解答题 | 10分**
17. (本题满分10分)

设<equation>z= f ( x+y, x-y, x y )</equation>，其中f具有二阶连续偏导数，求<equation>\mathrm{d} z</equation>与<equation>\frac{\partial^{2} z}{\partial x \partial y}.</equation>
**答案: **7)<equation>\mathrm{d} z=\left(f_{1}^{\prime}+f_{2}^{\prime}+y f_{3}^{\prime}\right) \mathrm{d} x+\left(f_{1}^{\prime}-f_{2}^{\prime}+x f_{3}^{\prime}\right) \mathrm{d} y,</equation><equation>\frac{\partial^{2} z}{\partial x \partial y}=f_{3}^{\prime}+f_{11}^{\prime \prime}+(x+y) f_{13}^{\prime \prime}-f_{22}^{\prime \prime}+(x-y) f_{23}^{\prime \prime}+xy f_{33}^{\prime \prime}.</equation>
**解析: **解 下面的<equation>f_{i}^{\prime}, f_{ij}^{\prime \prime}(i,j = 1,2,3)</equation>分别表示<equation>f_{i}^{\prime}(x + y,x - y,xy),f_{ij}^{\prime \prime}(x + y,x - y,</equation>（法一）将中间变量<equation>x + y,x - y,xy</equation>依次记为1，2，3号.利用链式法则，计算<equation>\frac{\partial z}{\partial x},\frac{\partial z}{\partial y},\frac{\partial^{2}z}{\partial x\partial y}</equation><equation>\frac {\partial z}{\partial x} = f _ {1} ^ {\prime} \frac {\partial (x + y)}{\partial x} + f _ {2} ^ {\prime} \frac {\partial (x - y)}{\partial x} + f _ {3} ^ {\prime} \frac {\partial (x y)}{\partial x} = f _ {1} ^ {\prime} + f _ {2} ^ {\prime} + y f _ {3} ^ {\prime},</equation><equation>\frac {\partial z}{\partial y} = f _ {1} ^ {\prime} \frac {\partial (x + y)}{\partial y} + f _ {2} ^ {\prime} \frac {\partial (x - y)}{\partial y} + f _ {3} ^ {\prime} \frac {\partial (x y)}{\partial y} = f _ {1} ^ {\prime} - f _ {2} ^ {\prime} + x f _ {3} ^ {\prime}.</equation>因为<equation>\mathrm{d}z = \frac{\partial z}{\partial x}\mathrm{d}x + \frac{\partial z}{\partial y}\mathrm{d}y</equation>，所以<equation>\mathrm {d} z = \left(f _ {1} ^ {\prime} + f _ {2} ^ {\prime} + y f _ {3} ^ {\prime}\right) \mathrm {d} x + \left(f _ {1} ^ {\prime} - f _ {2} ^ {\prime} + x f _ {3} ^ {\prime}\right) \mathrm {d} y.</equation><equation>\begin{aligned} \frac {\partial^ {2} z}{\partial x \partial y} &= \frac {\partial \left(\frac {\partial z}{\partial x}\right)}{\partial y} = \frac {\partial f _ {1} ^ {\prime}}{\partial y} + \frac {\partial f _ {2} ^ {\prime}}{\partial y} + \frac {\partial \left(y f _ {3} ^ {\prime}\right)}{\partial y} \\ &= f _ {1 1} ^ {\prime \prime} \frac {\partial (x + y)}{\partial y} + f _ {1 2} ^ {\prime \prime} \frac {\partial (x - y)}{\partial y} + f _ {1 3} ^ {\prime \prime} \frac {\partial (x y)}{\partial y} \\ + f _ {2 1} ^ {\prime \prime} \frac {\partial (x + y)}{\partial y} + f _ {2 2} ^ {\prime \prime} \frac {\partial (x - y)}{\partial y} + f _ {2 3} ^ {\prime \prime} \frac {\partial (x y)}{\partial y} \\ + y f _ {3 1} ^ {\prime \prime} \frac {\partial (x + y)}{\partial y} + y f _ {3 2} ^ {\prime \prime} \frac {\partial (x - y)}{\partial y} + y f _ {3 3} ^ {\prime \prime} \frac {\partial (x y)}{\partial y} + f _ {3} ^ {\prime} \\ &= f _ {1 1} ^ {\prime \prime} - f _ {1 2} ^ {\prime \prime} + x f _ {1 3} ^ {\prime \prime} + f _ {2 1} ^ {\prime \prime} - f _ {2 2} ^ {\prime \prime} + x f _ {2 3} ^ {\prime \prime} + y f _ {3 1} ^ {\prime \prime} - y f _ {3 2} ^ {\prime \prime} + x y f _ {3 3} ^ {\prime \prime} + f _ {3} ^ {\prime} \end{aligned}</equation>由于<equation>f</equation>的二阶偏导数连续，故<equation>f_{12}^{\prime \prime} = f_{21}^{\prime \prime}, f_{13}^{\prime \prime} = f_{31}^{\prime \prime}, f_{23}^{\prime \prime} = f_{32}^{\prime \prime}</equation>. 因此，<equation>\frac {\partial^ {2} z}{\partial x \partial y} = f _ {3} ^ {\prime} + f _ {1 1} ^ {\prime \prime} + (x + y) f _ {1 3} ^ {\prime \prime} - f _ {2 2} ^ {\prime \prime} + (x - y) f _ {2 3} ^ {\prime \prime} + x y f _ {3 3} ^ {\prime \prime}.</equation>（法二）利用全微分形式的不变性.

由于<equation>f</equation>具有二阶连续偏导数，故<equation>z,\frac{\partial z}{\partial x}</equation>均可微.<equation>\begin{aligned} \mathrm {d} z &= f _ {1} ^ {\prime} \mathrm {d} (x + y) + f _ {2} ^ {\prime} \mathrm {d} (x - y) + f _ {3} ^ {\prime} \mathrm {d} (x y) = f _ {1} ^ {\prime} \mathrm {d} x + f _ {1} ^ {\prime} \mathrm {d} y + f _ {2} ^ {\prime} \mathrm {d} x - f _ {2} ^ {\prime} \mathrm {d} y + y f _ {3} ^ {\prime} \mathrm {d} x + x f _ {3} ^ {\prime} \mathrm {d} y \\ &= \left(f _ {1} ^ {\prime} + f _ {2} ^ {\prime} + y f _ {3} ^ {\prime}\right) \mathrm {d} x + \left(f _ {1} ^ {\prime} - f _ {2} ^ {\prime} + x f _ {3} ^ {\prime}\right) \mathrm {d} y. \end{aligned}</equation>因此，<equation>\frac{\partial z}{\partial x} = f_1^{\prime} + f_2^{\prime} + yf_3^{\prime}</equation>.

继续对<equation>\frac{\partial z}{\partial x}</equation>微分，得<equation>\begin{aligned} \mathrm {d} \left(\frac {\partial z}{\partial x}\right) &= \mathrm {d} f _ {1} ^ {\prime} + \mathrm {d} f _ {2} ^ {\prime} + y \mathrm {d} f _ {3} ^ {\prime} + f _ {3} ^ {\prime} \mathrm {d} y \\ &= f _ {1 1} ^ {\prime \prime} \mathrm {d} (x + y) + f _ {1 2} ^ {\prime \prime} \mathrm {d} (x - y) + f _ {1 3} ^ {\prime \prime} \mathrm {d} (x y) \\ + f _ {2 1} ^ {\prime \prime} \mathrm {d} (x + y) + f _ {2 2} ^ {\prime \prime} \mathrm {d} (x - y) + f _ {2 3} ^ {\prime \prime} \mathrm {d} (x y) \\ + y f _ {3 1} ^ {\prime \prime} \mathrm {d} (x + y) + y f _ {3 2} ^ {\prime \prime} \mathrm {d} (x - y) + y f _ {3 3} ^ {\prime \prime} \mathrm {d} (x y) + f _ {3} ^ {\prime} \mathrm {d} y. \end{aligned}</equation>其中，<equation>\mathrm {d} y \text {的系 数} ^ {\prime} = f _ {1 1} ^ {\prime \prime} - f _ {1 2} ^ {\prime \prime} + x f _ {1 3} ^ {\prime \prime} + f _ {2 1} ^ {\prime \prime} - f _ {2 2} ^ {\prime \prime} + x f _ {2 3} ^ {\prime \prime} + y f _ {3 1} ^ {\prime \prime} - y f _ {3 2} ^ {\prime \prime} + x y f _ {3 3} ^ {\prime \prime} + f _ {3} ^ {\prime}.</equation>其余同法一.

---


#### 二次积分与变换积分次序

**2025年第5题 | 选择题 | 5分 | 答案: A**

5. 设函数 f(x,y) 连续，则<equation>\int_{-2}^{2}\mathrm{d}x\int_{4-x^{2}}^{4}f(x,y)\mathrm{d}y=</equation>(    )

A.<equation>\int_{0}^{4}\left[\int_{-2}^{-\sqrt{4-y}}f(x,y)\mathrm{d}x+\int_{\sqrt{4-y}}^{2}f(x,y)\mathrm{d}x\right]\mathrm{d}y</equation>B.<equation>\int_{0}^{4}\left[\int_{-2}^{\sqrt{4-y}}f(x,y)\mathrm{d}x+\int_{\sqrt{4-y}}^{2}f(x,y)\mathrm{d}x\right]\mathrm{d}y</equation>C.<equation>\int_{0}^{4}\left[\int_{-2}^{-\sqrt{4-y}}f(x,y)\mathrm{d}x+\int_{2}^{\sqrt{4-y}}f(x,y)\mathrm{d}x\right]\mathrm{d}y</equation>D.<equation>2\int_{0}^{4}\mathrm{d}y\int_{\sqrt{4-y}}^{2}f(x,y)\mathrm{d}x</equation>

答案: A

**解析:**解如图所示，二次积分<equation>\int_{-2}^{2}\mathrm{d}x\int_{4-x^{2}}^{4}f(x,y)\mathrm{d}y</equation>对应的二重积分的积分区域 D为图中灰色区域.<equation>D = \left\{(x, y) \mid 4 - x ^ {2} \leqslant y \leqslant 4, - 2 \leqslant x \leqslant 2 \right\}.</equation>当 x < 0时，解<equation>y=4-x^{2}</equation>可得<equation>x=-\sqrt{4-y}</equation>当 x > 0时，解<equation>y=4-x^{2}</equation>可得<equation>x=\sqrt{4-y}</equation>于是，将D写成Y型区域需要将其分块，<equation>D = \left\{(x, y) \mid - 2 \leqslant x \leqslant - \sqrt {4 - y}, 0 \leqslant y \leqslant 4 \right\} \cup \left\{(x, y) \mid \sqrt {4 - y} \leqslant x \leqslant 2, 0 \leqslant y \leqslant 4 \right\}.</equation>从而，<equation>\int_ {- 2} ^ {2} \mathrm {d} x \int_ {4 - x ^ {2}} ^ {4} f (x, y) \mathrm {d} y = \iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {4} \left[ \int_ {- 2} ^ {- \sqrt {4 - y}} f (x, y) \mathrm {d} x + \int_ {\sqrt {4 - y}} ^ {2} f (x, y) \mathrm {d} x \right] \mathrm {d} y.</equation>选项A正确，选项B、C不正确.

对选项D，该选项正确意味着<equation>\iint \limits_{D} f(x,y)\mathrm{d}x\mathrm{d}y=2\iint \limits_{D_{1}} f(x,y)\mathrm{d}x\mathrm{d}y</equation>，其中<equation>D_{1}</equation>为D位于y轴右边的部分，而该式成立需要<equation>f(x,y)</equation>是关于x的偶函数，但题干条件中并没有这一信息，故该选项不正确。例如，取<equation>f(x,y)=x</equation>，则<equation>\iint \limits_{D} f(x,y)\mathrm{d}x\mathrm{d}y=0</equation>，而<equation>\iint \limits_{D_{1}} f(x,y)\mathrm{d}x\mathrm{d}y>0.</equation>因此，应选A.

---

**2024年第6题 | 选择题 | 5分 | 答案: A**

6. 设 f(x,y)是连续函数，则<equation>\int_{\frac{\pi}{6}}^{\frac{\pi}{2}} \mathrm{d} x \int_{\sin x}^{1} f(x,y) \mathrm{d} y=</equation>(    )

A.<equation>\int_{\frac{1}{2}}^{1} \mathrm{d} y \int_{\frac{\pi}{6}}^{\arcsin y} f(x,y) \mathrm{d} x</equation>B.<equation>\int_{\frac{1}{2}}^{1} \mathrm{d} y \int_{\arcsin y}^{\frac{\pi}{2}} f(x,y) \mathrm{d} x</equation>C.<equation>\int_{0}^{\frac{1}{2}} \mathrm{d} y \int_{\frac{\pi}{6}}^{\arcsin y} f(x,y) \mathrm{d} x</equation>D.<equation>\int_{0}^{\frac{1}{2}} \mathrm{d} y \int_{\arcsin y}^{\frac{\pi}{2}} f(x,y) \mathrm{d} x</equation>

答案: A

**解析:**解二次积分<equation>\int_{\frac{\pi}{6}}^{\frac{\pi}{2}} \mathrm{d} x \int_{\sin x}^{1} f(x,y) \mathrm{d} y</equation>对应的二重积分的积分区域为<equation>D=\left\{(x,y)\mid \sin x\leqslant y\leqslant 1,\frac{\pi}{6}\leqslant x\leqslant \frac{\pi}{2}\right\}</equation>由于<equation>\arcsin y</equation>的值域为<equation>\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>，而<equation>\left[\frac{\pi}{6},\frac{\pi}{2}\right]\subset\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>，故曲线<equation>y=\sin x\left(x\in\left[\frac{\pi}{6},\frac{\pi}{2}\right]\right)</equation>上的点（x,y）可写为（<equation>\arcsin y,y).</equation>由此可将 D改写成Y型区域，<equation>D = \left\{(x, y) \mid \frac {\pi}{6} \leqslant x \leqslant \arcsin y, \frac {1}{2} \leqslant y \leqslant 1 \right\}.</equation>因此，<equation>\int_ {\frac {\pi}{6}} ^ {\frac {\pi}{2}} \mathrm {d} x \int_ {\sin x} ^ {1} f (x, y) \mathrm {d} y = \int_ {\frac {1}{2}} ^ {1} \mathrm {d} y \int_ {\frac {\pi}{6}} ^ {\arcsin y} f (x, y) \mathrm {d} x.</equation>应选A.

---

**2022年第2题 | 选择题 | 5分 | 答案: D**

2.<equation>\int_{0}^{2}\mathrm{d}y\int_{y}^{2}\frac{y}{\sqrt{1+x^{3}}}\mathrm{d}x=</equation>(    )

A.<equation>\frac{\sqrt{2}}{6}</equation>B.<equation>\frac{1}{3}</equation>C.<equation>\frac{\sqrt{2}}{3}</equation>D.<equation>\frac{2}{3}</equation>

答案: D

**解析:**解如图（a）所示，二次积分对应的积分区域 D是由直线 y=x,x=2以及 x轴所围成的三角形区域. 原二次积分采用的是先 x，后 y的积分次序，改写成先 y，后 x的积分次序，即将 D写成 X型区域，如图（b）所示.<equation>D = \{(x, y) \mid 0 \leqslant y \leqslant x, 0 \leqslant x \leqslant 2 \}.</equation>(a)

(b)

因此，<equation>\begin{aligned} \text {原 积 分} &= \iint_ {D} \frac {y}{\sqrt {1 + x ^ {3}}} \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {2} \frac {1}{\sqrt {1 + x ^ {3}}} \mathrm {d} x \int_ {0} ^ {x} y \mathrm {d} y = \frac {1}{2} \int_ {0} ^ {2} \frac {x ^ {2}}{\sqrt {1 + x ^ {3}}} \mathrm {d} x \\ &= \frac {1}{6} \int_ {0} ^ {2} \frac {\mathrm {d} \left(1 + x ^ {3}\right)}{\sqrt {1 + x ^ {3}}} = \frac {1}{6} \cdot 2 \sqrt {1 + x ^ {3}} \Bigg | _ {0} ^ {2} = \frac {1}{3} \times (3 - 1) = \frac {2}{3}. \end{aligned}</equation>应选 D.

---

**2021年第14题 | 填空题 | 5分**

14. 已知函数<equation>f ( t )=\int_{1}^{t^{2}} \mathrm{d} x \int_{\sqrt{x}}^{t} \sin \frac{x}{y} \mathrm{d} y</equation>，则<equation>f^{\prime}\left(\frac{\pi}{2}\right)=</equation>___

**答案:**##<equation>\frac{\pi}{2} \cos \frac{2}{\pi}.</equation>

**解析:**解 根据二次积分的积分限，可得积分<equation>\int_{1}^{t^{2}}\mathrm{d}x\int_{\sqrt{x}}^{t}\sin \frac{x}{y}\mathrm{d}y</equation>对应的积分区域的边界为<equation>y=\sqrt{x},</equation><equation>y = t, x = 1, x = t ^ {2}.</equation>二次积分对应的积分区域 D为图中阴影部分，写成X型区域为<equation>D = \left\{(x, y) \mid \sqrt {x} \leqslant y \leqslant t, 1 \leqslant x \leqslant t ^ {2} \right\}.</equation>交换积分次序，将 D写成 Y型区域，可得<equation>D = \left\{(x, y) \mid 1 \leqslant x \leqslant y ^ {2}, 1 \leqslant y \leqslant t \right\}.</equation>因此，<equation>\begin{aligned} f (t) &= \int_ {1} ^ {t ^ {2}} \mathrm {d} x \int_ {\sqrt {x}} ^ {t} \sin \frac {x}{y} \mathrm {d} y = \int_ {1} ^ {t} \mathrm {d} y \int_ {1} ^ {y ^ {2}} \sin \frac {x}{y} \mathrm {d} x = \int_ {1} ^ {t} y \cdot \left(- \cos \frac {x}{y}\right) \Bigg | _ {1} ^ {y ^ {2}} \mathrm {d} y \\ &= \int_ {1} ^ {t} \left(- y \cos y + y \cos \frac {1}{y}\right) \mathrm {d} y. \end{aligned}</equation>根据变限积分的求导公式，<equation>f ^ {\prime} (t) = \left[ \int_ {1} ^ {t} \left(- y \cos y + y \cos \frac {1}{y}\right) \mathrm {d} y \right] ^ {\prime} = - t \cos t + t \cos \frac {1}{t}.</equation>代入<equation>t = \frac{\pi}{2}</equation>，可得<equation>f^{\prime}\left(\frac{\pi}{2}\right) = \frac{\pi}{2}\cos \frac{2}{\pi}</equation>

---

**2020年第10题 | 填空题 | 4分**

<equation>1 0. \int_ {0} ^ {1} \mathrm {d} y \int_ {\sqrt {y}} ^ {1} \sqrt {x ^ {3} + 1} \mathrm {d} x = \underline {{}}</equation>

**答案:**<equation>\frac {2}{9} (2 \sqrt {2} - 1).</equation>

**解析:**解 由二次积分的积分限，可写出其对应的二重积分的积分区域的边界曲线：<equation>x=\sqrt{y}, x=1,</equation><equation>y=0, y=1.</equation>由这四条边界围成的区域 D如图（a）所示.<equation>D = \left\{(x, y) \mid \sqrt {y} \leqslant x \leqslant 1, 0 \leqslant y \leqslant 1 \right\}.</equation>如图（b）所示，将 D写成 X型区域的形式，可得<equation>D = \left\{(x, y) \mid 0 \leqslant y \leqslant x ^ {2}, 0 \leqslant x \leqslant 1 \right\}.</equation>(a)

(b)

由此可得，<equation>\begin{aligned} \int_ {0} ^ {1} \mathrm {d} y \int_ {\sqrt {y}} ^ {1} \sqrt {x ^ {3} + 1} \mathrm {d} x &= \int_ {0} ^ {1} \sqrt {x ^ {3} + 1} \mathrm {d} x \int_ {0} ^ {x ^ {2}} \mathrm {d} y = \frac {1}{3} \int_ {0} ^ {1} \sqrt {x ^ {3} + 1} \mathrm {d} \left(x ^ {3} + 1\right) \\ &= \frac {1}{3} \cdot \frac {2}{3} \left(x ^ {3} + 1\right) ^ {\frac {3}{2}} \Bigg | _ {0} ^ {1} = \frac {2}{9} \left(2 \sqrt {2} - 1\right). \end{aligned}</equation>

---

**2018年第6题 | 选择题 | 4分 | 答案: C**

6.<equation>\int_{-1}^{0}\mathrm{d}x\int_{-x}^{2-x^{2}}(1-xy)\mathrm{d}y+\int_{0}^{1}\mathrm{d}x\int_{x}^{2-x^{2}}(1-xy)\mathrm{d}y=</equation>(    )

A.<equation>\frac{5}{3}</equation>B.<equation>\frac{5}{6}</equation>C.<equation>\frac{7}{3}</equation>D.<equation>\frac{7}{6}</equation>

答案: C

**解析:**解 记<equation>D _ {1} = \left\{(x, y) \mid - x \leqslant y \leqslant 2 - x ^ {2}, - 1 \leqslant x \leqslant 0 \right\},</equation><equation>D _ {2} = \left\{(x, y) \mid x \leqslant y \leqslant 2 - x ^ {2}, 0 \leqslant x \leqslant 1 \right\},</equation>则<equation>\int_ {- 1} ^ {0} \mathrm {d} x \int_ {- x} ^ {2 - x ^ {2}} (1 - x y) \mathrm {d} y = \iint_ {D _ {1}} (1 - x y) \mathrm {d} x \mathrm {d} y, \quad \int_ {0} ^ {1} \mathrm {d} x \int_ {x} ^ {2 - x ^ {2}} (1 - x y) \mathrm {d} y = \iint_ {D _ {2}} (1 - x y) \mathrm {d} x \mathrm {d} y.</equation>记<equation>D=D_{1}\cup D_{2}</equation>.如图所示，D为由抛物线<equation>y=2-x^{2}</equation>，直线 y=x以及直线 y=-x所围成的阴影区域.所求积分<equation>=\iint_{D}(1-xy)\mathrm{d}x\mathrm{d}y.</equation>由于区域 D关于 y轴对称，而 xy为关于 x的奇函数，1为关于 x的偶函数，故<equation>\begin{aligned} \iint_ {D} (1 - x y) \mathrm {d} x \mathrm {d} y \xlongequal {\iint_ {D} x y \mathrm {d} x \mathrm {d} y = 0} 2 \iint_ {D _ {2}} \mathrm {d} x \mathrm {d} y &= 2 \int_ {0} ^ {1} \mathrm {d} x \int_ {x} ^ {2 - x ^ {2}} \mathrm {d} y = 2 \int_ {0} ^ {1} \left(2 - x ^ {2} - x\right) \mathrm {d} x \\ &= 2 \cdot \left(2 x - \frac {x ^ {3}}{3} - \frac {x ^ {2}}{2}\right) \Big | _ {0} ^ {1} = 2 \times \frac {7}{6} = \frac {7}{3}. \end{aligned}</equation>因此，应选C.

---

**2017年第13题 | 填空题 | 4分**

<equation>\int_ {0} ^ {1} \mathrm {d} y \int_ {y} ^ {1} \frac {\tan x}{x} \mathrm {d} x = \underline {{}}</equation>

**解析:**原二次积分对应的二重积分的积分区域 D为 Y型区域，<equation>D = \left\{(x, y) \mid y \leqslant x \leqslant 1, 0 \leqslant y \leqslant 1 \right\}.</equation>如图所示，将区域 D写成 X型区域，可得<equation>D = \left\{(x, y) \mid 0 \leqslant y \leqslant x, 0 \leqslant x \leqslant 1 \right\}.</equation>因此，<equation>\begin{aligned} \int_ {0} ^ {1} \mathrm {d} y \int_ {y} ^ {1} \frac {\tan x}{x} \mathrm {d} x &= \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {x} \frac {\tan x}{x} \mathrm {d} y = \int_ {0} ^ {1} \tan x \mathrm {d} x = \int_ {0} ^ {1} \frac {\sin x}{\cos x} \mathrm {d} x = \int_ {0} ^ {1} \frac {- \mathrm {d} (\cos x)}{\cos x} \\ &= - \ln (\cos x) \Bigg | _ {0} ^ {1} = - \ln (\cos 1). \end{aligned}</equation>

---

**2015年第6题 | 选择题 | 4分 | 答案: B**

6. 设 D是第一象限中由曲线<equation>2 x y=1, 4 x y=1</equation>与直线<equation>y=x,y=\sqrt{3} x</equation>围成的平面区域，函数 f(x,y)在 D上连续，则<equation>\iint\limits_{D} f(x,y)\mathrm{d}x\mathrm{d}y=</equation>(    )

A.<equation>\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \mathrm{d}\theta \int_{\frac{1}{2\sin 2\theta}}^{\frac{1}{\sin 2\theta}} f(r\cos \theta,r\sin \theta) r\mathrm{d}r</equation>B.<equation>\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \mathrm{d}\theta \int_{\frac{1}{\sqrt{2}\sin 2\theta}}^{\frac{1}{\sqrt{\sin 2\theta}}} f(r\cos \theta,r\sin \theta) r\mathrm{d}r</equation>C.<equation>\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \mathrm{d}\theta \int_{\frac{1}{2\sin 2\theta}}^{\frac{1}{\sin 2\theta}} f(r\cos \theta,r\sin \theta) \mathrm{d}r</equation>D.<equation>\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \mathrm{d}\theta \int_{\frac{1}{\sqrt{2}\sin 2\theta}}^{\frac{1}{\sqrt{\sin 2\theta}}} f(r\cos \theta,r\sin \theta) \mathrm{d}r</equation>

答案: B

**解析:**将曲线 2xy=1，4xy=1，直线 y=x，<equation>y=\sqrt{3}x</equation>改写为极坐标形式. 积分区域如图所示.<equation>2 x y = 1 \Rightarrow r ^ {2} \sin 2 \theta = 1 \Rightarrow r = \frac {1}{\sqrt {\sin 2 \theta}},</equation><equation>4 x y = 1 \Rightarrow 2 r ^ {2} \sin 2 \theta = 1 \Rightarrow r = \frac {1}{\sqrt {2 \sin 2 \theta}},</equation><equation>y = x \Rightarrow \theta = \frac {\pi}{4},</equation><equation>y = \sqrt {3} x \Rightarrow \theta = \frac {\pi}{3},</equation><equation>\mathrm {d} x \mathrm {d} y = r \mathrm {d} r \mathrm {d} \theta .</equation>于是，积分区域<equation>D</equation>在极坐标系下表示为<equation>D = \left\{(r, \theta) \mid \frac {1}{\sqrt {2 \sin 2 \theta}} \leqslant r \leqslant \frac {1}{\sqrt {\sin 2 \theta}}, \frac {\pi}{4} \leqslant \theta \leqslant \frac {\pi}{3} \right\}.</equation>因此，<equation>\iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{3}} \mathrm {d} \theta \int_ {\frac {1}{\sqrt {2 \sin 2 \theta}}} ^ {\frac {1}{\sqrt {\sin 2 \theta}}} f (r \cos \theta , r \sin \theta) r \mathrm {d} r.</equation>应选B.

---

**2009年第4题 | 选择题 | 4分 | 答案: C**

4. 设函数 f(x,y) 连续，则<equation>\int_{1}^{2}\mathrm{d}x\int_{x}^{2}f(x,y)\mathrm{d}y+\int_{1}^{2}\mathrm{d}y\int_{y}^{4-y}f(x,y)\mathrm{d}x=</equation>(    )

A.<equation>\int_{1}^{2}\mathrm{d}x\int_{1}^{4-x}f(x,y)\mathrm{d}y</equation>B.<equation>\int_{1}^{2}\mathrm{d}x\int_{x}^{4-x}f(x,y)\mathrm{d}y</equation>C.<equation>\int_{1}^{2}\mathrm{d}y\int_{1}^{4-y}f(x,y)\mathrm{d}x</equation>D.<equation>\int_{1}^{2}\mathrm{d}y\int_{y}^{2}f(x,y)\mathrm{d}x</equation>

答案: C

**解析:**解<equation>\int_{1}^{2}\mathrm{d}x\int_{x}^{2}f(x,y)\mathrm{d}y</equation>对应的积分区域为<equation>D _ {1} = \left\{(x, y) \mid x \leqslant y \leqslant 2, 1 \leqslant x \leqslant 2 \right\}</equation>如图所示，<equation>D_{1}</equation>为由直线<equation>x = 1, y = 2</equation>以及<equation>x = y</equation>围成的三角形.<equation>\int_{1}^{2}\mathrm{d}y\int_{y}^{4-y}f(x,y)\mathrm{d}x</equation>对应的积分区域为<equation>D _ {2} = \left\{(x, y) \mid y \leqslant x \leqslant 4 - y, 1 \leqslant y \leqslant 2 \right\}</equation>如图所示，<equation>D_{2}</equation>为由直线<equation>y=x,x+y=4</equation>以及<equation>y=1</equation>围成的三角形

由图可知，<equation>D _ {1} \cup D _ {2} = D = \left\{(x, y) \mid 1 \leqslant x \leqslant 4 - y, 1 \leqslant y \leqslant 2 \right\}</equation>因此，原积分可写为<equation>\int_{1}^{2}\mathrm{d}y\int_{1}^{4-y}f(x,y)\mathrm{d}x.</equation>应选C.

---


#### 多元函数的极值问题

**2025年第19题 | 解答题 | 12分**
19. (本题满分12分)

设函数 f(x,y)可微且满足：<equation>\mathrm {d} f (x, y) = - 2 x \mathrm {e} ^ {- y} \mathrm {d} x + \mathrm {e} ^ {- y} \left(x ^ {2} - y - 1\right) \mathrm {d} y, f (0, 0) = 2</equation>求 f(x,y)，并求 f(x,y)的极值.
**答案: **f（x,y）=-x²e^{-y}+（y+2）e^{-y}； f（0,-1）为极大值
**解析: **解 由<equation>\mathrm{d}f(x,y) = -2x\mathrm{e}^{-y}\mathrm{d}x + \mathrm{e}^{-y}(x^2 - y - 1)\mathrm{d}y</equation>可得<equation>\frac{\partial f}{\partial x} = -2x\mathrm{e}^{-y},\frac{\partial f}{\partial y} = \mathrm{e}^{-y}(x^2 - y - 1)</equation>.于是，<equation>f (x, y) = \int \frac {\partial f}{\partial x} \mathrm {d} x = \int (- 2 x) \mathrm {e} ^ {- y} \mathrm {d} x = - x ^ {2} \mathrm {e} ^ {- y} + \varphi (y),</equation>其中<equation>\varphi(y)</equation>为关于y的一元函数.

对<equation>f(x,y)</equation>关于<equation>y</equation>求偏导数可得<equation>\frac{\partial f}{\partial y} = x^{2}\mathrm{e}^{-y} + \varphi^{\prime}(y)</equation>. 与<equation>\frac{\partial f}{\partial y} = \mathrm{e}^{-y}(x^{2} - y - 1)</equation>比较可得<equation>\varphi^{\prime}(y) = -\mathrm{e}^{-y}(y + 1)</equation>. 进一步可得<equation>\begin{aligned} \varphi (y) &= \int \varphi^ {\prime} (y) \mathrm {d} y = \int \left[ - \mathrm {e} ^ {- y} (y + 1) \right] \mathrm {d} y = \int (y + 1) \mathrm {d} \left(\mathrm {e} ^ {- y}\right) = (y + 1) \mathrm {e} ^ {- y} - \int \mathrm {e} ^ {- y} \mathrm {d} y \\ &= (y + 1) \mathrm {e} ^ {- y} + \mathrm {e} ^ {- y} + C = (y + 2) \mathrm {e} ^ {- y} + C, \end{aligned}</equation>其中 C为待定常数.

将<equation>\varphi(y)</equation>的表达式代入<equation>f(x,y)</equation>可得<equation>f (x, y) = - x ^ {2} \mathrm {e} ^ {- y} + (y + 2) \mathrm {e} ^ {- y} + C = \left(- x ^ {2} + y + 2\right) \mathrm {e} ^ {- y} + C.</equation>代入<equation>f ( 0, 0 )=2</equation>可得<equation>2=2+C</equation>，解得<equation>C=0</equation>因此，<equation>f ( x,y )=\left(-x^{2}+y+2\right) \mathrm{e}^{-y}.</equation>下面计算 f（x,y）的极值.

计算 f（x,y）的驻点.

解<equation>\left\{ \begin{array}{l l} \frac{\partial f}{\partial x} = 0, \\ \frac{\partial f}{\partial y} = 0, \end{array} \right.</equation>即<equation>\left\{ \begin{array}{l l} - 2x\mathrm{e}^{-y} = 0, \\ \mathrm{e}^{-y}(x^2 - y - 1) = 0. \end{array} \right.</equation>由<equation>-2x\mathrm{e}^{-y} = 0</equation>可得<equation>x = 0</equation>. 将<equation>x = 0</equation>代入<equation>\mathrm{e}^{-y}(x^2 - y - 1)</equation>= 0 可得<equation>y = -1</equation>. 于是，点<equation>(0, -1)</equation>为<equation>f(x,y)</equation>的唯一驻点.

计算 f(x,y)的二阶偏导数.<equation>\frac {\partial^ {2} f}{\partial x ^ {2}} = - 2 \mathrm {e} ^ {- y}, \quad \frac {\partial^ {2} f}{\partial x \partial y} = 2 x \mathrm {e} ^ {- y}, \quad \frac {\partial^ {2} f}{\partial y ^ {2}} = - \left(x ^ {2} - y\right) \mathrm {e} ^ {- y}.</equation>对点（0，-1），<equation>A = \left. \frac {\partial^ {2} f}{\partial x ^ {2}} \right| _ {(0, - 1)} = - 2 \mathrm {e}, \quad B = \left. \frac {\partial^ {2} f}{\partial x \partial y} \right| _ {(0, - 1)} = 0, \quad C = \left. \frac {\partial^ {2} f}{\partial y ^ {2}} \right| _ {(0, - 1)} = - \mathrm {e}.</equation>由于<equation>AC - B^{2} > 0</equation>，且<equation>A < 0</equation>，故点（0，-1）为<equation>f(x,y)</equation>的极大值点，极大值为<equation>f(0, - 1) = \mathrm{e}</equation>.

---

**2024年第12题 | 填空题 | 5分**
12. 函数<equation>f(x,y)=2x^{3}-9x^{2}-6y^{4}+12x+24y</equation>的极值点是 ___
**答案: **## (1,1)
**解析: **解 计算 f(x,y) 的驻点.

整理<equation>\left\{\begin{array}{l l}f_{x}^{\prime}(x,y)=6x^{2}-18x+12=0,\\ f_{y}^{\prime}(x,y)=-24y^{3}+24=0\end{array}\right.</equation>可得<equation>\left\{\begin{array}{l l}x^{2}-3x+2=0,\\ y^{3}-1=0,\end{array}\right.</equation>解得<equation>\left\{\begin{array}{l l}x=1,\\ y=1,\end{array}\right.</equation>或<equation>\left\{\begin{array}{l l}x=2,\\ y=1,\end{array}\right.</equation>即<equation>f(x,y)</equation>的全部驻点为点（1，1），（2，1）.

计算 f(x,y)的二阶偏导数.<equation>f _ {x x} ^ {\prime \prime} (x, y) = 1 2 x - 1 8, f _ {x y} ^ {\prime \prime} (x, y) = 0, f _ {y y} ^ {\prime \prime} (x, y) = - 7 2 y ^ {2}.</equation>对点（1,1），<equation>A=f_{xx}^{\prime \prime}(1,1)=-6,B=f_{xy}^{\prime \prime}(1,1)=0,C=f_{yy}^{\prime \prime}(1,1)=-72,AC-B^{2}=(-6)\times</equation>（-72）-0>0，且<equation>A<0</equation>，故由二元函数极值存在的充分条件可知，点（1,1）是<equation>f(x,y)</equation>的极大值点.

对点（2,1），<equation>A=f_{xx}^{\prime \prime}(2,1)=6,B=f_{xy}^{\prime \prime}(2,1)=0,C=f_{yy}^{\prime \prime}(2,1)=-72,AC-B^{2}=6\times(-72)</equation><equation>- 0 < 0</equation>，故由二元函数极值存在的充分条件可知，点（2,1）不是<equation>f(x,y)</equation>的极值点.

因此，<equation>f(x,y)</equation>的唯一极值点为（1,1）.

---

**2023年第18题 | 解答题 | 12分**
18. (本题满分12分)

求函数<equation>f ( x,y)=x \mathrm{e}^{\cos y}+\frac{x^{2}}{2}</equation>的极值.
**答案: **f(x,y)有极小值，极小值为<equation>f(-\mathrm{e},2 k \pi)=-\frac{\mathrm{e}^{2}}{2}</equation>，其中 k<equation>\in\mathbf{Z}.</equation>
**解析: **解<equation>\textcircled{1}</equation>计算 f(x,y）的驻点.<equation>f _ {x} ^ {\prime} (x, y) = \mathrm {e} ^ {\cos y} + x, \quad f _ {y} ^ {\prime} (x, y) = - x \sin y \mathrm {e} ^ {\cos y}.</equation>令<equation>\left\{\begin{array}{l l} {\mathrm{e}^{\cos y}+x=0,} \\ {-x\sin y\mathrm{e}^{\cos y}=0.} \end{array} \right.</equation>由<equation>\mathrm{e}^{\cos y}>0</equation>以及<equation>- x\sin y\mathrm{e}^{\cos y}=0</equation>可得 x=0或<equation>\sin y=0.</equation>但当 x=0时，<equation>\mathrm{e}^{\cos y}+x=0</equation>，且 A > 0. 不成立，于是<equation>\sin y=0</equation>，从而 y = k<equation>\pi</equation>，其中 k<equation>\in\mathbf{Z}.</equation>当 y = 2k<equation>\pi</equation>时，<equation>\mathrm{e}^{\cos y}=\mathrm{e},x=-\mathrm{e}</equation>；当 y = （2k+1）<equation>\pi</equation>时，<equation>\mathrm{e}^{\cos y}=\mathrm{e}^{-1},x=-\mathrm{e}^{-1}</equation>由此可得 f(x,y)的全部驻点为（-e，2k<equation>\pi</equation>），（<equation>-\mathrm{e}^{-1},(2k+1)\pi</equation>），其中 k<equation>\in</equation>Z.<equation>\textcircled{2}</equation>计算 f(x,y)的二阶偏导数.<equation>f _ {x x} ^ {\prime \prime} (x, y) = 1,</equation><equation>f _ {x y} ^ {\prime \prime} (x, y) = - \sin y \mathrm {e} ^ {\cos y},</equation><equation>f _ {y y} ^ {\prime \prime} (x, y) = - x \cos y \mathrm {e} ^ {\cos y} - x \sin y \cdot (- \sin y) \mathrm {e} ^ {\cos y} = x \left(\sin^ {2} y - \cos y\right) \mathrm {e} ^ {\cos y}.</equation><equation>\textcircled{3}</equation>计算<equation>AC-B^{2}.</equation>（i）对点<equation>(-\mathrm{e},2k\pi),A=f_{xx}^{\prime \prime}(-\mathrm{e},2k\pi)=1,B=f_{xy}^{\prime \prime}(-\mathrm{e},2k\pi)=0,C=f_{yy}^{\prime \prime}(-\mathrm{e},2k\pi)=\mathrm{e}^{2},</equation><equation>AC-B^{2}=\mathrm{e}^{2}>0</equation>，且 A > 0.由二元函数极值存在的充分条件可知，点<equation>(-\mathrm{e},2k\pi),k\in \mathbf{Z}</equation>是 f(x,y)的极小值点.极小值为<equation>f(-\mathrm{e},2k\pi)=-\frac{\mathrm{e}^{2}}{2}.</equation>（ii）对点<equation>(-\mathrm{e}^{-1},(2 k+1)\pi), A=f_{x x}^{\prime \prime}(-\mathrm{e}^{-1},(2 k+1)\pi)=1, B=f_{x y}^{\prime \prime}(-\mathrm{e}^{-1},(2 k+1)\pi)= 0, C=f_{y y}^{\prime \prime}(-\mathrm{e}^{-1},(2 k+1)\pi)=-\mathrm{e}^{-2}, A C-B^{2}=-\mathrm{e}^{-2}<0.</equation>由二元函数极值存在的充分条件可知，点<equation>(-\mathrm{e}^{-1},(2 k+1)\pi), k\in \mathbf{Z}</equation>不是 f(x,y）的极值点.

综上所述，<equation>f ( x,y )</equation>有极小值，极小值为<equation>f(-\mathrm{e},2 k \pi)=-\frac{\mathrm{e}^{2}}{2}.</equation>

---

**2022年第20题 | 解答题 | 12分**
20. (本题满分12分)

已知可微函数 f(u,v)满足<equation>\frac{\partial f(u,v)}{\partial u}-\frac{\partial f(u,v)}{\partial v}=2(u-v)\mathrm{e}^{-(u+v)},</equation>且<equation>f(u,0)=u^{2}\mathrm{e}^{-u}.</equation>I. 记<equation>g(x,y)=f(x,y-x),</equation>求<equation>\frac{\partial g(x,y)}{\partial x};</equation>II. 求 f(u,v)的表达式与极值.
**答案: **（ I ）<equation>( 4 x-2 y ) \mathrm{e}^{-y}；</equation>（Ⅱ）<equation>f ( u,v )</equation>的表达式为<equation>\left(u^{2}+v^{2}\right)\mathrm{e}^{-(u+v)}</equation>，该函数有极小值，极小值为<equation>f ( 0,0 )=0.</equation>
**解析: **（ I ）根据链式法则，<equation>\frac {\partial g (x , y)}{\partial x} = \frac {\partial f (x , y - x)}{\partial x} = f _ {1} ^ {\prime} (x, y - x) - f _ {2} ^ {\prime} (x, y - x).</equation>令<equation>u=x,v=y-x</equation>，并代入<equation>\frac{\partial f(u,v)}{\partial u}-\frac{\partial f(u,v)}{\partial v}=2(u-v)\mathrm{e}^{-(u+v)}</equation>可得<equation>f _ {1} ^ {\prime} (x, y - x) - f _ {2} ^ {\prime} (x, y - x) = 2 (2 x - y) \mathrm {e} ^ {- y}.</equation>因此，<equation>\frac{\partial g(x,y)}{\partial x} = (4x - 2y)\mathrm{e}^{-y}.</equation>（Ⅱ）通过积分先计算<equation>g ( x,y )</equation>即<equation>f ( x,y-x )</equation>的表达式.<equation>\begin{aligned} f (x, y - x) &= g (x, y) = \int \frac {\partial g (x , y)}{\partial x} \mathrm {d} x = \int (4 x - 2 y) \mathrm {e} ^ {- y} \mathrm {d} x = \left(2 x ^ {2} - 2 x y\right) \mathrm {e} ^ {- y} + \varphi (y) \\ &= 2 x (x - y) \mathrm {e} ^ {- y} + \varphi (y), \end{aligned}</equation>其中<equation>\varphi(y)</equation>为关于 y的一元函数.

令 u=x,v=y-x可得<equation>f (u, v) = - 2 u v \mathrm {e} ^ {- (u + v)} + \varphi (u + v).</equation>代入<equation>f ( u, 0 ) = u^{2} \mathrm{e}^{-u}</equation>可得<equation>\varphi ( u )=u^{2}\mathrm{e}^{-u}.</equation>于是，<equation>f (u, v) = - 2 u v \mathrm {e} ^ {- (u + v)} + \varphi (u + v) = - 2 u v \mathrm {e} ^ {- (u + v)} + (u + v) ^ {2} \mathrm {e} ^ {- (u + v)} = \left(u ^ {2} + v ^ {2}\right) \mathrm {e} ^ {- (u + v)}.</equation>计算 f（u,v）的驻点.<equation>f _ {1} ^ {\prime} (u, v) = 2 u \mathrm {e} ^ {- (u + v)} - \left(u ^ {2} + v ^ {2}\right) \mathrm {e} ^ {- (u + v)} = \left(2 u - u ^ {2} - v ^ {2}\right) \mathrm {e} ^ {- (u + v)},</equation><equation>f _ {2} ^ {\prime} (u, v) = 2 v \mathrm {e} ^ {- (u + v)} - \left(u ^ {2} + v ^ {2}\right) \mathrm {e} ^ {- (u + v)} = \left(2 v - u ^ {2} - v ^ {2}\right) \mathrm {e} ^ {- (u + v)}.</equation>解<equation>\left\{\begin{array}{l l}2 u-u^{2}-v^{2}=0,\\ 2 v-u^{2}-v^{2}=0.\end{array} \right.</equation>两式相减得 u=v，将 u=v 代入 2u-u²-v²=0 可得 2u-2u²=0，从而 u=0或 u=1.<equation>\left\{\begin{array}{l l}u=0,\\ v=0\end{array} \right.</equation>和<equation>\left\{\begin{array}{l l}u=1,\\ v=1\end{array} \right.</equation>为该方程组的两组解.

因此，点（0，0）和点（1，1）为 f（u,v）的全部驻点.

计算 f（u,v）的二阶偏导数.<equation>f _ {1 1} ^ {\prime \prime} (u, v) = (2 - 2 u) \mathrm {e} ^ {- (u + v)} - \left(2 u - u ^ {2} - v ^ {2}\right) \mathrm {e} ^ {- (u + v)} = \left(u ^ {2} + v ^ {2} - 4 u + 2\right) \mathrm {e} ^ {- (u + v)},</equation><equation>f _ {1 2} ^ {\prime \prime} (u, v) = - 2 v \mathrm {e} ^ {- (u + v)} - \left(2 u - u ^ {2} - v ^ {2}\right) \mathrm {e} ^ {- (u + v)} = \left(u ^ {2} + v ^ {2} - 2 u - 2 v\right) \mathrm {e} ^ {- (u + v)},</equation><equation>f _ {2 2} ^ {\prime \prime} (u, v) = (2 - 2 v) \mathrm {e} ^ {- (u + v)} - \left(2 v - u ^ {2} - v ^ {2}\right) \mathrm {e} ^ {- (u + v)} = \left(u ^ {2} + v ^ {2} - 4 v + 2\right) \mathrm {e} ^ {- (u + v)}.</equation>对点（0，0），<equation>A = f _ {1 1} ^ {\prime \prime} (0, 0) = 2, \quad B = f _ {1 2} ^ {\prime \prime} (0, 0) = 0, \quad C = f _ {2 2} ^ {\prime \prime} (0, 0) = 2.</equation>由于<equation>AC-B^{2}>0</equation>，且<equation>A>0</equation>，故点（0,0）为<equation>f(u,v)</equation>的极小值点，极小值为<equation>f(0,0)=0.</equation>对点（1，1），<equation>A = f _ {1 1} ^ {\prime \prime} (1, 1) = 0, \quad B = f _ {1 2} ^ {\prime \prime} (1, 1) = - 2 \mathrm {e} ^ {- 2}, \quad C = f _ {2 2} ^ {\prime \prime} (1, 1) = 0.</equation>由于<equation>AC-B^{2}<0</equation>，故点（1，1）不是极值点.

综上所述，<equation>f ( u,v )</equation>有极小值，极小值为<equation>f ( 0,0 )=0.</equation>

---

**2020年第17题 | 解答题 | 10分**
17. (本题满分10分)

求函数<equation>f ( x,y)=x^{3}+8 y^{3}- x y</equation>的极值.
**答案: **<equation>\text {极 小 值} f \left(\frac {1}{6}, \frac {1}{1 2}\right) = - \frac {1}{2 1 6}.</equation>
**解析: **解<equation>\textcircled{1}</equation>计算 f(x,y）的驻点.

解<equation>\left\{ \begin{array}{l l} f_{x}^{\prime}(x,y)=3x^{2}-y=0, \\ f_{y}^{\prime}(x,y)=24y^{2}-x=0. \end{array} \right.</equation>将 y=3x²代入24y²-x=0可得216x4=x，解得x=0或x<equation>= \frac{1}{6}.</equation>于是，<equation>\left\{ \begin{array}{l}x = 0,\\ y = 0 \end{array} \right.</equation>或<equation>\left\{ \begin{array}{l}x = \frac{1}{6},\\ y = \frac{1}{12}. \end{array} \right.</equation>f(x,y)有两个驻点（0，0），<equation>\left(\frac{1}{6},\frac{1}{12}\right).</equation><equation>\textcircled{2}</equation>计算 f(x,y)的二阶偏导数.<equation>f _ {x x} ^ {\prime \prime} (x, y) = 6 x, \quad f _ {x y} ^ {\prime \prime} (x, y) = - 1, \quad f _ {y y} ^ {\prime \prime} (x, y) = 4 8 y.</equation><equation>\textcircled{3}</equation>判断驻点是否为极值点以及确定极值点类型.

- 考虑驻点（0,0）.<equation>A = f _ {x x} ^ {\prime \prime} (0, 0) = 0, \quad B = f _ {x y} ^ {\prime \prime} (0, 0) = - 1, \quad C = f _ {y y} ^ {\prime \prime} (0, 0) = 0.</equation>AC-B²=0-1=-1<0，故点（0,0）不是极值点.

- 考虑驻点<equation>\left(\frac{1}{6},\frac{1}{12}\right).</equation><equation>A = f _ {x x} ^ {\prime \prime} \left(\frac {1}{6}, \frac {1}{1 2}\right) = 1, \quad B = f _ {x y} ^ {\prime \prime} \left(\frac {1}{6}, \frac {1}{1 2}\right) = - 1, \quad C = f _ {y y} ^ {\prime \prime} \left(\frac {1}{6}, \frac {1}{1 2}\right) = 4.</equation><equation>AC-B^{2}=4-1=3>0</equation>，且 A > 0，故点<equation>\left(\frac{1}{6},\frac{1}{12}\right)</equation>为极小值点，极小值为<equation>f \left(\frac {1}{6}, \frac {1}{1 2}\right) = \frac {1}{6 ^ {3}} + \frac {8}{1 2 ^ {3}} - \frac {1}{6 \times 1 2} = - \frac {1}{2 1 6}.</equation>

---

**2018年第19题 | 解答题 | 10分**
19. (本题满分10分)

将长为2m的铁丝分成三段，依次围成圆、正方形与正三角形. 三个图形的面积之和是否存在最小值？若存在，求出最小值.
**答案: **三个图形的面积之和存在最小值，最小值为<equation>\frac{1}{\pi+4+3\sqrt{3}}.</equation>
**解析: **解设圆、正方形、正三角形的周长分别为 x,y,z，则圆的半径<equation>r=\frac{x}{2\pi}</equation>正方形的边长<equation>a=\frac{y}{4}</equation>正三角形的边长<equation>b=\frac{z}{3}</equation>.于是，三个图形的面积之和为<equation>S (x, y, z) = \pi \cdot \left(\frac {x}{2 \pi}\right) ^ {2} + \left(\frac {y}{4}\right) ^ {2} + \frac {1}{2} \cdot \left(\frac {z}{3}\right) ^ {2} \cdot \sin \frac {\pi}{3} = \frac {x ^ {2}}{4 \pi} + \frac {y ^ {2}}{1 6} + \frac {\sqrt {3}}{3 6} z ^ {2}.</equation>由于三段铁丝的周长之和为2，故<equation>x+y+z=2.</equation>建立拉格朗日函数<equation>L ( x,y,z,\lambda) = \frac{x^{2}}{4\pi} +\frac{y^{2}}{16} +\frac{\sqrt{3}}{36} z^{2} +\lambda(x+y+z-2).</equation>令<equation>\left\{ \begin{array}{l} L _ {x} ^ {\prime} = \frac {1}{2 \pi} x + \lambda = 0, \\ L _ {y} ^ {\prime} = \frac {1}{8} y + \lambda = 0, \\ L _ {z} ^ {\prime} = \frac {\sqrt {3}}{1 8} z + \lambda = 0, \\ L _ {\lambda} ^ {\prime} = x + y + z - 2 = \end{array} \right.</equation>由前三个方程可得<equation>x = -2\pi \lambda ,y = -8\lambda ,z = -6\sqrt{3}\lambda .</equation>代入 x+y+z-2=0可得<equation>\lambda = - \frac {2}{2 \pi + 8 + 6 \sqrt {3}} = - \frac {1}{\pi + 4 + 3 \sqrt {3}}.</equation>于是，<equation>x=\frac{2\pi}{\pi+4+3\sqrt{3}}, y=\frac{8}{\pi+4+3\sqrt{3}}, z=\frac{6\sqrt{3}}{\pi+4+3\sqrt{3}}.</equation>将所得 x,y,z的值代入 S（x，y，z）可得<equation>S (x, y, z) = \frac {\pi + 4 + 3 \sqrt {3}}{(\pi + 4 + 3 \sqrt {3}) ^ {2}} = \frac {1}{\pi + 4 + 3 \sqrt {3}}.</equation>为了判定所求得可能的极值点是否为最小值点，我们把问题转化为目标函数 S（x，y，z）在有界闭区域 D = {（x，y，z）| x+y+z=2，x≥0，y≥0，z≥0}上的最值问题.

由于连续函数在有界闭区域上一定能取到最值，故若我们能分别计算出<equation>S ( x, y, z )</equation>在边界<equation>y + z = 2, z + x = 2, x + y = 2</equation>上的最值，再与<equation>\frac{1} {\pi+4+3\sqrt{3}}</equation>比较，则所得最小值即为区域D上的最小值当 x=0时，<equation>S ( 0, y, z )</equation>在 y+z=2下的最小值为<equation>S \left( 0, \frac{8}{4+3\sqrt{3}}, \frac{6\sqrt{3}}{4+3\sqrt{3}} \right) = \frac{1}{4+3\sqrt{3}}.</equation>当 y=0时，<equation>S ( x, 0, z )</equation>在 x+z=2下的最小值为<equation>S \left( \frac{2\pi}{\pi+3\sqrt{3}}, 0, \frac{6\sqrt{3}}{\pi+3\sqrt{3}} \right) = \frac{1}{\pi+3\sqrt{3}}.</equation>当 z=0时，<equation>S ( x, y, 0 )</equation>在 x+y=2下的最小值为<equation>S \left( \frac{2\pi}{\pi+4}, \frac{8}{\pi+4}, 0 \right) = \frac{1}{\pi+4}.</equation>4个值比较可得，<equation>\frac{1} {\pi+4+3\sqrt{3}}</equation>为整个区域D上的最小值，也为<equation>x+y+z=2, x > 0, y > 0, z > 0</equation>时的<equation>S ( x, y, z )</equation>的最小值. 三个图形的面积之和存在最小值，最小值为<equation>\frac{1} {\pi+4+3\sqrt{3}}.</equation>

---

**2016年第17题 | 解答题 | 10分**
17. (本题满分10分）

已知函数<equation>z=z(x,y)</equation>由方程<equation>( x^{2}+y^{2}) z+\ln z+2(x+y+1)=0</equation>确定，求<equation>z=z(x,y)</equation>的极值.
**答案: **极大值<equation>f(-1,-1)=1.</equation>
**解析: **对方程两端分别关于 x和关于 y求偏导数，得<equation>2 x z + \left(x ^ {2} + y ^ {2}\right) \frac {\partial z}{\partial x} + \frac {1}{z} \frac {\partial z}{\partial x} + 2 = 0,</equation><equation>2 y z + \left(x ^ {2} + y ^ {2}\right) \frac {\partial z}{\partial y} + \frac {1}{z} \frac {\partial z}{\partial y} + 2 = 0.</equation>当<equation>\frac{\partial z}{\partial x}=0</equation>时，<equation>2 x z+2=0,x=-\frac{1}{z}.</equation>同理，当<equation>\frac{\partial z}{\partial y}=0</equation>时，<equation>2 y z+2=0,y=-\frac{1}{z}.</equation>将（x，y）<equation>= \left(-\frac{1}{z}, -\frac{1}{z}\right)</equation>代入原方程求 x，y.<equation>\frac {2}{z ^ {2}} \cdot z + \ln z + 2 \left(- \frac {2}{z} + 1\right) = 0.</equation>化简（3）式得<equation>\ln z=\frac{2}{z}-2</equation>. 通过观察 y=<equation>\ln z</equation>以及 y=<equation>\frac{2}{z}-2</equation>的图像，可知这两条曲线交于点 (1,0). 考虑函数<equation>f(z)=\ln z-\frac{2}{z}+2.</equation><equation>f^{\prime}(z)=\frac{1}{z}+\frac{2}{z^{2}}>0</equation>，从而 f(z)在（0，<equation>+\infty</equation>）上单调增加，于是 z=1是 f(z)=0的唯一解. 因此，驻点坐标为（-1，-1）.

下面计算驻点（-1，-1）处的二阶偏导数.

对（1）式两端关于 x求导，得<equation>2 z + 2 x \frac {\partial z}{\partial x} + 2 x \frac {\partial z}{\partial x} + \left(x ^ {2} + y ^ {2}\right) \frac {\partial^ {2} z}{\partial x ^ {2}} - \frac {1}{z ^ {2}} \left(\frac {\partial z}{\partial x}\right) ^ {2} + \frac {1}{z} \frac {\partial^ {2} z}{\partial x ^ {2}} = 0.</equation>对（2）式两端关于 y求导，得<equation>2 z + 2 y \frac {\partial z}{\partial y} + 2 y \frac {\partial z}{\partial y} + \left(x ^ {2} + y ^ {2}\right) \frac {\partial^ {2} z}{\partial y ^ {2}} - \frac {1}{z ^ {2}} \left(\frac {\partial z}{\partial y}\right) ^ {2} + \frac {1}{z} \frac {\partial^ {2} z}{\partial y ^ {2}} = 0.</equation>对（1）式两端关于 y求导，得<equation>2 x \frac {\partial z}{\partial y} + 2 y \frac {\partial z}{\partial x} + \left(x ^ {2} + y ^ {2}\right) \frac {\partial^ {2} z}{\partial x \partial y} - \frac {1}{z ^ {2}} \frac {\partial z}{\partial x} \frac {\partial z}{\partial y} + \frac {1}{z} \frac {\partial^ {2} z}{\partial x \partial y} = 0.</equation>将<equation>x=-1, y=-1, z=1</equation>代入（4）式，（5）式，（6）式，并注意到<equation>\frac{\partial z}{\partial x}\bigg|_{(-1,-1)}=\frac{\partial z}{\partial y}\bigg|_{(-1,-1)}=0</equation>可得，<equation>\begin{aligned} 2 + 2 \left. \frac {\partial^ {2} z}{\partial x ^ {2}} \right| _ {(- 1, - 1)} + \left. \frac {\partial^ {2} z}{\partial x ^ {2}} \right| _ {(- 1, - 1)} &= 0, \quad 2 + 2 \left. \frac {\partial^ {2} z}{\partial y ^ {2}} \right| _ {(- 1, - 1)} + \left. \frac {\partial^ {2} z}{\partial y ^ {2}} \right| _ {(- 1, - 1)} = 0. \\ 2 \left. \frac {\partial^ {2} z}{\partial x \partial y} \right| _ {(- 1, - 1)} + \left. \frac {\partial^ {2} z}{\partial x \partial y} \right| _ {(- 1, - 1)} &= 0. \end{aligned}</equation>从而，<equation>\frac{\partial^{2}z}{\partial x^{2}}\bigg|_{(-1,-1)}=\frac{\partial^{2}z}{\partial y^{2}}\bigg|_{(-1,-1)}=-\frac{2}{3},\frac{\partial^{2}z}{\partial x\partial y}\bigg|_{(-1,-1)}=0.</equation>因此，<equation>\left[ \frac{\partial^{2} z}{\partial x^{2}}\frac{\partial^{2} z}{\partial y^{2}}-\left(\frac{\partial^{2} z}{\partial x \partial y}\right)^{2} \right] \Bigg|_{(-1,-1)}>0, \frac{\partial^{2} z}{\partial x^{2}} \Bigg|_{(-1,-1)}<0.</equation>由二元函数极值存在的充分条件可知，点（-1，-1）是函数<equation>z=z(x,y)</equation>的极大值点，极大值为1.

---

**2015年第17题 | 解答题 | 10分**
17. (本题满分11分)

已知函数 f(x,y)满足<equation>f_{xy}^{\prime\prime}(x,y)=2(y+1)\mathrm{e}^{x},f_{x}^{\prime}(x,0)=(x+1)\mathrm{e}^{x},f(0,y)=y^{2}+2y</equation>，求 f(x,y)的极值.
**答案: **(17) 极小值<equation>f ( 0,-1 )=-1.</equation>
**解析: **解 利用题给条件，我们来逐步求 f（x，y）.

由于<equation>f_{xy}^{\prime \prime}(x,y)=2(y+1)\mathrm{e}^{x}</equation>，故<equation>f _ {x} ^ {\prime} (x, y) = \int f _ {x y} ^ {\prime \prime} (x, y) \mathrm {d} y = \int 2 (y + 1) \mathrm {e} ^ {x} \mathrm {d} y = \mathrm {e} ^ {x} \left(y ^ {2} + 2 y\right) + g (x),</equation>其中<equation>g(x)</equation>是以<equation>x</equation>为变量的一元函数.当<equation>y = 0</equation>时，<equation>f_x^{\prime}(x,0) = g(x) = (x + 1)\mathrm{e}^x</equation>，故<equation>f _ {x} ^ {\prime} (x, y) = \left(y ^ {2} + 2 y\right) \mathrm {e} ^ {x} + (x + 1) \mathrm {e} ^ {x} = \left(y + 1\right) ^ {2} \mathrm {e} ^ {x} + x \mathrm {e} ^ {x}.</equation>从而，<equation>f (x, y) = \int f _ {x} ^ {\prime} (x, y) \mathrm {d} x = \int \left[ (y + 1) ^ {2} \mathrm {e} ^ {x} + x \mathrm {e} ^ {x} \right] \mathrm {d} x = (y + 1) ^ {2} \mathrm {e} ^ {x} + (x - 1) \mathrm {e} ^ {x} + h (y),</equation>其中 h(y)是以y为变量的一元函数.代入 x=0，得 f（0，y）=（y+1）²-1+h(y）=y²+2y，故 h(y)=0.

因此，<equation>f ( x, y ) = ( y + 1 )^{2} \mathrm{e}^{x} + ( x - 1 ) \mathrm{e}^{x}.</equation>计算 f（x，y）的偏导数得，<equation>f _ {x} ^ {\prime} (x, y) = (y + 1) ^ {2} \mathrm {e} ^ {x} + x \mathrm {e} ^ {x}, \quad f _ {y} ^ {\prime} (x, y) = 2 (y + 1) \mathrm {e} ^ {x}.</equation>由于 f(x,y)的驻点满足<equation>f_{x}^{\prime}(x,y)=f_{y}^{\prime}(x,y)=0</equation>，故解<equation>\left\{ \begin{array}{l l} (y+1)^{2}\mathrm{e}^{x}+x\mathrm{e}^{x}=0, \\ 2(y+1)\mathrm{e}^{x}=0 \end{array} \right.</equation>得 x=0，y=-1. 因此，点（0，-1）为 f(x,y)的驻点.

根据二元函数极值存在的充分条件，分别计算<equation>f_{xx}^{\prime \prime}(0, - 1), f_{yy}^{\prime \prime}(0, - 1), f_{xy}^{\prime \prime}(0, - 1)</equation>.<equation>f _ {x x} ^ {\prime \prime} (x, y) = (y + 1) ^ {2} \mathrm {e} ^ {x} + (x + 1) \mathrm {e} ^ {x}, f _ {x x} ^ {\prime \prime} (0, - 1) = 1,</equation><equation>f _ {y y} ^ {\prime \prime} (x, y) = 2 \mathrm {e} ^ {x}, \quad f _ {y y} ^ {\prime \prime} (0, - 1) = 2,</equation><equation>f _ {x y} ^ {\prime \prime} (x, y) = 2 (y + 1) \mathrm {e} ^ {x}, f _ {x y} ^ {\prime \prime} (0, - 1) = 0.</equation>由于<equation>f_{xx}^{\prime \prime}(0,-1)f_{yy}^{\prime \prime}(0,-1)-[f_{xy}^{\prime \prime}(0,-1)]^{2}=2>0</equation>，且<equation>f_{xx}^{\prime \prime}(0,-1)=1>0</equation>，故点（0，-1）为<equation>f(x,y)</equation>的极小值点，<equation>f(0,-1)=-1</equation>为<equation>f(x,y)</equation>的极小值.

---

**2014年第6题 | 选择题 | 4分 | 答案: A**
6. 设函数 u(x,y)在有界闭区域 D上连续，在 D的内部具有2阶连续偏导数，且满足<equation>\frac{\partial^{2} u}{\partial x \partial y}\neq0</equation>及<equation>\frac{\partial^{2} u}{\partial x^{2}}+\frac{\partial^{2} u}{\partial y^{2}}=0</equation>则（    )

A. u(x,y)的最大值和最小值都在 D的边界上取得

B. u(x,y)的最大值和最小值都在 D的内部取得

C. u(x,y)的最大值在 D的内部取得，最小值在 D的边界上取得

D. u(x,y)的最小值在 D的内部取得，最大值在 D的边界上取得
答案: A
**解析: **解 由于<equation>u ( x, y )</equation>是有界闭区域D上的连续函数，故<equation>u ( x, y )</equation>在D上必有最大值和最小值.若<equation>u ( x, y )</equation>在区域D的内部取得最大值或最小值，则该最值点是<equation>u ( x, y )</equation>的驻点.

由题设，对区域 D内的任何一点，都有<equation>\frac{\partial^2 u}{\partial x^2} +\frac{\partial^2 u}{\partial y^2} = 0</equation>，故<equation>\frac{\partial^2 u}{\partial x^2}\cdot \frac{\partial^2 u}{\partial y^2}\leqslant 0</equation>，而<equation>\frac{\partial^2 u}{\partial x\partial y}\neq 0</equation>，从而<equation>\left(\frac{\partial^2 u}{\partial x\partial y}\right)^2 > 0</equation>，因此<equation>\frac{\partial^2 u}{\partial x^2}\frac{\partial^2 u}{\partial y^2} -\left(\frac{\partial^2 u}{\partial x\partial y}\right)^2 < 0.</equation>特别地，该不等式对区域 D内的驻点也成立.

由二元函数极值存在的充分条件知，区域 D内的驻点都不是 u（x，y）的极值点.因此 u（x,y）的最大值和最小值都在 D的边界上取得.应选A.

---

**2013年第19题 | 解答题 | 10分**
19. (本题满分10分)

求曲线<equation>x^{3}- x y+y^{3}=1 ( x \geqslant0, y \geqslant0)</equation>上的点到坐标原点的最长距离和最短距离.
**答案: **(19) 最长距离<equation>\sqrt{2}</equation>，最短距离1.
**解析: **解作拉格朗日函数<equation>L ( x,y,\lambda) = x^{2}+y^{2}+\lambda \left( x^{3}-xy+y^{3}-1 \right).</equation>令<equation>L _ {x} ^ {\prime} = 2 x + 3 \lambda x ^ {2} - \lambda y = 0,</equation><equation>L _ {y} ^ {\prime} = 2 y + 3 \lambda y ^ {2} - \lambda x = 0,</equation><equation>L _ {\lambda} ^ {\prime} = \varphi (x, y) = x ^ {3} - x y + y ^ {3} - 1 = 0.</equation>整理（1）式，（2）式得<equation>2 x = \lambda \left(y - 3 x ^ {2}\right),</equation><equation>2 y = \lambda \left(x - 3 y ^ {2}\right).</equation>当<equation>\lambda=0</equation>时，由（4）式，（5）式可得<equation>x=y=0</equation>；当<equation>\lambda\neq0</equation>，<equation>x=0</equation>时，由（4）式可得<equation>y=0</equation>；当<equation>\lambda\neq0</equation><equation>y=0</equation>时，由（5）式可得<equation>x=0</equation>.由于点（0，0）不在曲线<equation>x^{3}-xy+y^{3}-1=0</equation>上，故以上情况均不符合题意.

下面只考虑<equation>\lambda\neq0</equation>，<equation>x\neq0</equation>，<equation>y\neq0</equation>的情况.

当<equation>\lambda \neq 0</equation>，<equation>x\neq 0</equation>，<equation>y\neq 0</equation>时，<equation>\frac{(4)}</equation>式（5）式得，<equation>\frac{x}{y} = \frac{y - 3x^2}{x - 3y^2}</equation>，整理得<equation>x^{2} - 3y^{2}x - y^{2} + 3x^{2}y = 0</equation>，即<equation>(x - y) (x + y + 3 x y) = 0.</equation>当<equation>x > 0</equation>，<equation>y > 0</equation>时，<equation>x + y + 3xy > 0</equation>，故只有<equation>x = y</equation>成立.代入（3）式，可得<equation>2x^{3} - x^{2} - 1 = 0.</equation>分解因式，得<equation>(x - 1)(2x^{2} + x + 1) = 0.</equation>由于<equation>2x^{2} + x + 1 > 0</equation>，故<equation>x = 1</equation>，从而<equation>y = 1.</equation>点（1，1）为曲线<equation>x^{3} - xy + y^{3} = 1(x\geqslant 0,y\geqslant 0)</equation>上唯一可能的极值点.此时，<equation>d = \sqrt{1 + 1} = \sqrt{2}.</equation>考虑曲线端点到原点的距离，当<equation>x=0</equation>时，代入曲线方程得<equation>y=1,d=\sqrt{1+0}=1</equation>；当<equation>y=0</equation>时，代入曲线方程得<equation>x=1,d=\sqrt{1+0}=1.</equation>综上所述，最长距离为<equation>\sqrt{2}</equation>，最短距离为1.

---

**2012年第16题 | 解答题 | 10分**
16. (本题满分10分）

求函数<equation>f ( x,y)=x \mathrm{e}^{- \frac{x^{2}+y^{2}}{2}}</equation>的极值.
**答案: **(16) 极大值<equation>f(1,0) = \mathrm{e}^{-\frac{1}{2}}</equation>，极小值<equation>f(-1,0) = -\mathrm{e}^{-\frac{1}{2}}.</equation>
**解析: **解<equation>\textcircled{1}</equation>先找到<equation>f(x,y)</equation>的全部驻点.

记<equation>g ( x,y)=\mathrm{e}^{- \frac{x^{2}+y^{2}}{2}}.</equation>由于<equation>f _ {x} ^ {\prime} (x, y) = \mathrm {e} ^ {- \frac {x ^ {2} + y ^ {2}}{2}} + x \cdot \mathrm {e} ^ {- \frac {x ^ {2} + y ^ {2}}{2}} \cdot (- x) = \left(1 - x ^ {2}\right) \mathrm {e} ^ {- \frac {x ^ {2} + y ^ {2}}{2}} = \left(1 - x ^ {2}\right) g (x, y),</equation><equation>f _ {y} ^ {\prime} (x, y) = - x y \mathrm {e} ^ {- \frac {x ^ {2} + y ^ {2}}{2}} = (- x y) g (x, y).</equation>由于 g(x,y) > 0，故满足<equation>\left\{\begin{array}{l l}1-x^{2}=0\\-xy=0\end{array}\right.</equation>的点（x，y）为 f(x，y）的驻点.解该方程组得（x，y）= （<equation>\pm1,0).</equation>因此，点（1，0）和点（-1，0）为<equation>f(x,y)</equation>的全部驻点.<equation>\textcircled{2}</equation>计算二阶偏导数.<equation>f _ {x x} ^ {\prime \prime} (x, y) = (- 2 x) g (x, y) + \left(1 - x ^ {2}\right) g _ {x} ^ {\prime} (x, y),</equation><equation>f _ {x y} ^ {\prime \prime} (x, y) = \left(1 - x ^ {2}\right) g _ {y} ^ {\prime} (x, y),</equation><equation>f _ {y y} ^ {\prime \prime} (x, y) = (- x) g (x, y) + (- x y) g _ {y} ^ {\prime} (x, y).</equation><equation>\textcircled{3}</equation>计算<equation>A C-B^{2}.</equation>由于<equation>f ( x, y )</equation>的驻点<equation>\left(x_{0}, y_{0}\right)</equation>均满足<equation>1-x_{0}^{2}=0,-x_{0}y_{0}=0</equation>，而<equation>g ( x, y )</equation>恒大于零，故在驻点 (1,0)处，<equation>f_{xx}^{\prime \prime}(1,0)=-2g(1,0)<0,f_{xy}^{\prime \prime}(1,0)=0,f_{yy}^{\prime \prime}(1,0)=-g(1,0).</equation>因此，<equation>f _ {x x} ^ {\prime \prime} (1, 0) f _ {y y} ^ {\prime \prime} (1, 0) - \left[ f _ {x y} ^ {\prime \prime} (1, 0) \right] ^ {2} = 2 g ^ {2} (1, 0) > 0.</equation>由于<equation>f_{xx}^{\prime \prime}(1,0)=-2 g(1,0)<0</equation>，故点（1，0）为<equation>f(x,y)</equation>的极大值点，<equation>f(1,0)=\mathrm{e}^{-\frac{1}{2}}</equation>为<equation>f(x,y)</equation>的极大值.同理可得，点（-1，0）为<equation>f(x,y)</equation>的极小值点，<equation>f(-1,0)=-\mathrm{e}^{-\frac{1}{2}}</equation>为<equation>f(x,y)</equation>的极小值.

因此，函数<equation>f ( x, y ) = x \mathrm{e}^{- \frac{x^{2}+y^{2}}{2}}</equation>的极大值为<equation>\mathrm{e}^{- \frac{1}{2}}</equation>，极小值为<equation>- \mathrm{e}^{- \frac{1}{2}}.</equation>

---

**2011年第5题 | 选择题 | 4分 | 答案: A**
5. 设函数 f(x)，g(x)均有二阶连续导数，满足 f(0)>0,g(0)<0，且<equation>f^{\prime}(0)=g^{\prime}(0)=0</equation>，则函数 z=f(x)g(y)在点 (0,0)处取得极小值的一个充分条件是（    ）

A.<equation>f^{\prime\prime}(0)<0,g^{\prime\prime}(0)>0</equation>B.<equation>f^{\prime\prime}(0)<0,g^{\prime\prime}(0)<0</equation>C.<equation>f^{\prime\prime}(0)>0,g^{\prime\prime}(0)>0</equation>D.<equation>f^{\prime\prime}(0)>0,g^{\prime\prime}(0)<0</equation>
答案: A
**解析: **解分别求出<equation>\frac{\partial z}{\partial x},\frac{\partial z}{\partial y},\frac{\partial^{2}z}{\partial x^{2}},\frac{\partial^{2}z}{\partial y^{2}}</equation>以及<equation>\frac{\partial^{2}z}{\partial x\partial y}.</equation>由<equation>z = f(x)g(y)</equation>得<equation>\frac {\partial z}{\partial x} = f ^ {\prime} (x) g (y), \quad \frac {\partial z}{\partial y} = f (x) g ^ {\prime} (y),</equation><equation>\frac {\partial^ {2} z}{\partial x ^ {2}} = f ^ {\prime \prime} (x) g (y), \quad \frac {\partial^ {2} z}{\partial y ^ {2}} = f (x) g ^ {\prime \prime} (y), \quad \frac {\partial^ {2} z}{\partial x \partial y} = f ^ {\prime} (x) g ^ {\prime} (y).</equation>根据二元函数取极小值的充分条件，若在点（0，0）处，<equation>\left. \left(\frac {\partial^ {2} z}{\partial x ^ {2}} \frac {\partial^ {2} z}{\partial y ^ {2}}\right) \right| _ {(0, 0)} - \left. \left(\frac {\partial^ {2} z}{\partial x \partial y}\right) ^ {2} \right| _ {(0, 0)} > 0,</equation>且<equation>\left.\frac{\partial^2 z}{\partial x^2}\right|_{(0,0)} > 0</equation>，则二元函数<equation>z = f(x)g(y)</equation>在点（0，0）处有极小值.

首先，<equation>\left. \frac {\partial^ {2} z}{\partial x ^ {2}} \right| _ {(0, 0)} > 0 \Leftrightarrow f ^ {\prime \prime} (0) g (0) > 0 \xleftrightarrow {g (0) < 0} f ^ {\prime \prime} (0) < 0.</equation>又由于<equation>f^{\prime}(0)=g^{\prime}(0)=0</equation>，故<equation>\left. \frac{\partial^{2} z}{\partial x \partial y}\right|_{(0,0)}=0.</equation>（1）式成立当且仅当<equation>\left. \left(\frac{\partial^{2} z}{\partial x^{2}}\frac{\partial^{2} z}{\partial y^{2}}\right)\right|_{(0,0)}>0.</equation>因为<equation>\left. \frac{\partial^{2} z}{\partial x^{2}}\right|_{(0,0)}>0</equation>，所以必有<equation>\left. \frac{\partial^{2} z}{\partial y^{2}}\right|_{(0,0)}>0</equation>，而<equation>\left. \frac {\partial^ {2} z}{\partial y ^ {2}} \right| _ {(0, 0)} > 0 \Leftrightarrow f (0) g ^ {\prime \prime} (0) > 0 \Longleftrightarrow \frac {f (0) > 0}{g ^ {\prime \prime} (0)} g ^ {\prime \prime} (0) > 0.</equation>因此，<equation>z=f(x)g(y)</equation>在点（0，0）处取得极小值的一个充分条件是<equation>f^{\prime \prime}(0)<0,g^{\prime \prime}(0)>0.</equation>应选A.

---

**2009年第3题 | 选择题 | 4分 | 答案: D**
3. 设函数 z=f(x,y)的全微分为<equation>\mathrm{d} z=x\mathrm{d} x+y\mathrm{d} y</equation>，则点（0,0）（    )

A. 不是 f(x,y)的连续点 B. 不是 f(x,y)的极值点

C. 是 f(x,y)的极大值点 D. 是 f(x,y)的极小值点
答案: D
**解析: **解 由全微分的表达式知，<equation>f_{x}^{\prime}(x,y)=x,f_{y}^{\prime}(x,y)=y</equation>，从而点（0，0）为 f(x,y)的驻点.根据二元函数极值存在的充分条件，计算<equation>f_{xx}^{\prime\prime},f_{xy}^{\prime\prime},f_{yy}^{\prime\prime}</equation>，得<equation>f_{xx}^{\prime\prime}\equiv 1,f_{xy}^{\prime\prime}\equiv 0,f_{yy}^{\prime\prime}\equiv 1.</equation>从而<equation>f_{xx}^{\prime\prime}(0,0)f_{yy}^{\prime\prime}(0,0)-[f_{xy}^{\prime\prime}(0,0)]^{2}=1>0, f_{xx}^{\prime\prime}(0,0)>0.</equation>因此，<equation>f(x,y)</equation>在点（0，0）处取极小值.应选D.

---


#### 二重积分的计算

**2025年第20题 | 解答题 | 12分**
20. (本题满分12分)

已知平面有界区域 D = {（x,y）<equation>\mid x^{2}+y^{2}\leqslant 4 x, x^{2}+y^{2}\leqslant 4 y</equation>，计算<equation>\iint_{D} ( x-y )^{2} \mathrm{d} x \mathrm{d} y.</equation>
**答案: **<equation>1 2 \pi - \frac {1 1 2}{3}</equation>
**解析: **解如图所示，区域D由两个圆围成，计算两圆的交点。联立两圆方程可得<equation>\left\{ \begin{array}{l l} x^{2} + y^{2} = 4x, \\ x^{2} + y^{2} = 4y, \end{array} \right.</equation>两式相减可得<equation>x = y</equation>，代入第一个方程可得<equation>2x^{2}</equation><equation>-4x = 0</equation>，解得<equation>x = 0</equation>或<equation>x = 2</equation>.于是，两圆的交点为（0,0），（2,2）.连接两交点的直线方程为<equation>y = x</equation>.进一步可得区域D关于直线<equation>y = x</equation>对称.

记区域<equation>D</equation>位于直线<equation>y = x</equation>下方的部分为<equation>D_{1}</equation>，则由轮换对称性的结论可得<equation>\begin{aligned} \iint_ {D} (x - y) ^ {2} \mathrm {d} x \mathrm {d} y &= \iint_ {D _ {1}} (x - y) ^ {2} \mathrm {d} x \mathrm {d} y + \iint_ {D \backslash D _ {1}} (x - y) ^ {2} \mathrm {d} x \mathrm {d} y \\ &= \iint_ {D _ {1}} (x - y) ^ {2} \mathrm {d} x \mathrm {d} y + \iint_ {D _ {1}} (y - x) ^ {2} \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} (x - y) ^ {2} \mathrm {d} x \mathrm {d} y. \end{aligned}</equation><equation>D_{1}</equation>的极坐标表示为<equation>D_{1} = \left\{(r,\theta)\mid 0 \leqslant r \leqslant 4 \sin \theta ,0 \leqslant \theta \leqslant \frac{\pi}{4}\right\}</equation>.<equation>\begin{aligned} \iint_ {D _ {1}} (x - y) ^ {2} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \iint_ {D _ {1}} \left(r ^ {2} - 2 r ^ {2} \cos \theta \sin \theta\right) \cdot r \mathrm {d} r \mathrm {d} \theta &= \int_ {0} ^ {\frac {\pi}{4}} \left(1 - 2 \sin \theta \cos \theta\right) \mathrm {d} \theta \int_ {0} ^ {4 \sin \theta} r ^ {3} \mathrm {d} r \\ &= \int_ {0} ^ {\frac {\pi}{4}} \left(1 - 2 \sin \theta \cos \theta\right) \cdot \frac {r ^ {4}}{4} \Bigg | _ {0} ^ {4 \sin \theta} \mathrm {d} \theta = 6 4 \int_ {0} ^ {\frac {\pi}{4}} \left(1 - 2 \sin \theta \cos \theta\right) \sin^ {4} \theta \mathrm {d} \theta \\ &= 6 4 \int_ {0} ^ {\frac {\pi}{4}} \sin^ {4} \theta \mathrm {d} \theta - 1 2 8 \int_ {0} ^ {\frac {\pi}{4}} \sin^ {5} \theta \cos \theta \mathrm {d} \theta . \end{aligned}</equation>分别计算<equation>64\int_{0}^{\frac{\pi}{4}}\sin^{4}\theta \mathrm{d}\theta</equation>与<equation>128\int_{0}^{\frac{\pi}{4}}\sin^{5}\theta \cos \theta \mathrm{d}\theta .</equation><equation>\begin{aligned} 6 4 \int_ {0} ^ {\frac {\pi}{4}} \sin^ {4} \theta \mathrm {d} \theta &= 6 4 \int_ {0} ^ {\frac {\pi}{4}} \left(\frac {1 - \cos 2 \theta}{2}\right) ^ {2} \mathrm {d} \theta = 1 6 \int_ {0} ^ {\frac {\pi}{4}} \left(1 - 2 \cos 2 \theta + \cos^ {2} 2 \theta\right) \mathrm {d} \theta \\ &= 1 6 \int_ {0} ^ {\frac {\pi}{4}} \left(1 - 2 \cos 2 \theta + \frac {1 + \cos 4 \theta}{2}\right) \mathrm {d} \theta \\ &= 6 \pi - 3 2 \int_ {0} ^ {\frac {\pi}{4}} \cos 2 \theta \mathrm {d} \theta + 8 \int_ {0} ^ {\frac {\pi}{4}} \cos 4 \theta \mathrm {d} \theta \\ &= 6 \pi - 3 2 \cdot \frac {\sin 2 \theta}{2} \Bigg | _ {0} ^ {\frac {\pi}{4}} + 8 \cdot \frac {\sin 4 \theta}{4} \Bigg | _ {0} ^ {\frac {\pi}{4}} = 6 \pi - 1 6. \end{aligned}</equation><equation>128\int_{0}^{\frac{\pi}{4}}\sin^{5}\theta \cos \theta \mathrm{d}\theta = 128\int_{0}^{\frac{\pi}{4}}\sin^{5}\theta \mathrm{d}(\sin \theta) = 128\cdot \frac{\sin^{6}\theta}{6}\bigg|_{0}^{\frac{\pi}{4}} = 128\cdot \frac{1}{6}\cdot \frac{1}{8} = \frac{8}{3}.</equation>因此，<equation>\iint_{D}(x - y)^{2}\mathrm{d}x\mathrm{d}y = 2\cdot \left(6\pi - 16 - \frac{8}{3}\right) = 12\pi - \frac{112}{3}.</equation>

---

**2024年第17题 | 解答题 | 10分**
17. (本题满分10分)

假设平面某有界区域 D位于第一象限，并且由曲线<equation>x y=\frac{1}{3}, x y=3</equation>与直线<equation>y=\frac{1}{3} x, y=3 x</equation>围成，试计算<equation>\iint_{D} ( 1+x-y ) \mathrm{d} x \mathrm{d} y.</equation>
**答案: **##<equation>\frac{8}{3}\ln 3.</equation>
**解析: **解区域 D如图（a）所示，注意到区域 D的四条边界曲线中，交换曲线<equation>xy=\frac{1}{3}</equation>与<equation>xy=3</equation>中x， y的位置，可得<equation>yx=\frac{1}{3}</equation>与<equation>yx=3</equation>，即曲线方程不变，故这两条曲线均关于直线<equation>y=x</equation>对称，而直线<equation>y=\frac{1}{3} x</equation>与直线<equation>y=3x</equation>关于直线<equation>y=x</equation>对称，故这四条曲线所围成的区域 D也关于直线<equation>y=x</equation>对称，从而对变量 x，y具有轮换对称性.

(a)

(b)

由轮换对称性的结论（2）可得<equation>\iint_{D}x\mathrm{d}x\mathrm{d}y=\iint_{D}y\mathrm{d}x\mathrm{d}y</equation>，故<equation>\iint_ {D} (1 + x - y) \mathrm {d} x \mathrm {d} y = \iint_ {D} \mathrm {d} x \mathrm {d} y + \iint_ {D} x \mathrm {d} x \mathrm {d} y - \iint_ {D} y \mathrm {d} x \mathrm {d} y = \iint_ {D} \mathrm {d} x \mathrm {d} y.</equation>下面用两种方法计算<equation>\iint_{D}\mathrm{d}x\mathrm{d}y.</equation>（法一）在极坐标系下计算.

曲线<equation>xy = \frac{1}{3}</equation>的极坐标方程为<equation>r^2\cos \theta \sin \theta = \frac{1}{3}</equation>，整理可得<equation>r = \sqrt{\frac{2}{3\sin 2\theta}}</equation>，曲线<equation>xy = 3</equation>的极坐标方程为<equation>r^2\cos \theta \sin \theta = 3</equation>，整理可得<equation>r = \sqrt{\frac{6}{\sin 2\theta}}</equation>直线<equation>y = \frac{1}{3} x</equation>的极坐标方程为<equation>\theta = \arctan \frac{1}{3},y = 3x</equation>的极坐标方程为<equation>\theta = \arctan 3.</equation>区域 D的极坐标表示为<equation>D = \left\{(r, \theta) \mid \sqrt {\frac {2}{3 \sin 2 \theta}} \leqslant r \leqslant \sqrt {\frac {6}{\sin 2 \theta}}, \arctan \frac {1}{3} \leqslant \theta \leqslant \arctan 3 \right\}.</equation>于是，<equation>\begin{aligned} \iint_ {D} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} \mathrm {d} \theta \int_ {\sqrt {\frac {2}{3 \sin 2 \theta}}} ^ {\sqrt {\frac {6}{\sin 2 \theta}}} r \mathrm {d} r &= \frac {1}{2} \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} r ^ {2} \left| \begin{array}{c} \sqrt {\frac {6}{\sin 2 \theta}} \\ \sqrt {\frac {2}{3 \sin 2 \theta}}  \right| \mathrm {d} \theta \\ &= \frac {8}{3} \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} \csc 2 \theta \mathrm {d} \theta = \frac {4}{3} \ln | \csc 2 \theta - \cot 2 \theta | \Bigg | _ {\arctan \frac {1}{3}} ^ {\arctan 3}. \end{aligned}</equation>由于<equation>\csc 2\theta-\cot 2\theta=\frac{1-\cos 2\theta}{\sin 2\theta}=\frac{2\sin^{2}\theta}{2\sin \theta\cos \theta}=\tan \theta</equation>，故<equation>\iint_{D}\mathrm{d}x\mathrm{d}y=\frac{4}{3}\ln |\tan \theta |\Bigg|_{\arctan \frac{1}{3}}^{\arctan 3}</equation>当<equation>\theta =\arctan \frac{1}{3}</equation>时，<equation>\tan \theta =\frac{1}{3}</equation>，当<equation>\theta =\arctan 3</equation>时，<equation>\tan \theta =3.</equation>因此，<equation>\iint_ {D} \mathrm {d} x \mathrm {d} y = \frac {4}{3} \left(\ln 3 - \ln \frac {1}{3}\right) = \frac {8}{3} \ln 3.</equation>（法二）在直角坐标系下计算.

联立<equation>\left\{ \begin{array}{l l} x y = \frac{1}{3}, \\ y = \frac{1}{3} x, \end{array} \right.</equation>解得<equation>\left\{ \begin{array}{l l} x = 1, \\ y = \frac{1}{3}. \end{array} \right.</equation>联立<equation>\left\{ \begin{array}{l l} x y = \frac{1}{3}, \\ y = 3 x, \end{array} \right.</equation>解得<equation>\left\{ \begin{array}{l l} x = \frac{1}{3}, \\ y = 1. \end{array} \right.</equation>联立<equation>\left\{ \begin{array}{l l} x y = 3, \\ y = \frac{1}{3} x, \end{array} \right.</equation>解得<equation>\left\{ \begin{array}{l l} x = 3, \\ y = 1. \end{array} \right.</equation>联立<equation>\left\{ \begin{array}{l l} x y = 3, \\ y = 3 x, \end{array} \right.</equation>解得<equation>\left\{ \begin{array}{l l} x = 1, \\ y = 3. \end{array} \right.</equation>如图（b）所示，直线<equation>x = 1</equation>将区域D分为两部分<equation>D_{1}, D_{2}</equation>.<equation>D_{1}</equation>由曲线<equation>xy = \frac{1}{3}</equation>，直线<equation>y = 3x</equation>与<equation>x = 1</equation>围成，<equation>D_{2}</equation>由曲线<equation>xy = 3</equation>，直线<equation>y = \frac{1}{3} x</equation>与<equation>x = 1</equation>围成，<equation>\iint_{D}\mathrm{d}x\mathrm{d}y</equation>等于D的面积，即<equation>D_{1}</equation>的面积与<equation>D_{2}</equation>的面积之和.

因此，<equation>\begin{aligned} \iint_ {D} \mathrm {d} x \mathrm {d} y &= \int_ {\frac {1}{3}} ^ {1} \left(3 x - \frac {1}{3 x}\right) \mathrm {d} x + \int_ {1} ^ {3} \left(\frac {3}{x} - \frac {x}{3}\right) \mathrm {d} x = \left(\frac {3 x ^ {2}}{2} - \frac {1}{3} \ln x\right) \left| _ {\frac {1}{3}} ^ {1} + \left(3 \ln x - \frac {x ^ {2}}{6}\right) \right| _ {1} ^ {3} \\ &= \frac {3}{2} - \frac {1}{6} + \frac {1}{3} \ln \frac {1}{3} + 3 \ln 3 - \frac {3}{2} + \frac {1}{6} = - \frac {1}{3} \ln 3 + 3 \ln 3 = \frac {8}{3} \ln 3. \end{aligned}</equation>

---


#### 全微分的概念与计算

**2021年第6题 | 选择题 | 5分 | 答案: C**
6. 设函数 f(u,v)可微，且<equation>f \left( x+1, \mathrm{e}^{x} \right)=x \left( x+1 \right)^{2}, f \left( x, x^{2} \right)=2 x^{2} \ln x</equation>，则<equation>\mathrm{d} f \left( 1, 1 \right)=</equation>(    )

A.<equation>\mathrm{d} x+\mathrm{d} y</equation>B.<equation>\mathrm{d} x-\mathrm{d} y</equation>C.<equation>\mathrm{d} y</equation>D.<equation>-\mathrm{d} y</equation>
答案: C
**解析: **根据全微分的定义，<equation>\mathrm {d} f (1, 1) = f _ {1} ^ {\prime} (1, 1) \mathrm {d} x + f _ {2} ^ {\prime} (1, 1) \mathrm {d} y.</equation>对<equation>f ( x+1,\mathrm{e}^{x} )=x ( x+1 )^{2}, f ( x,x^{2} )=2 x^{2} \ln x</equation>两端均关于 x求导，可得<equation>f _ {1} ^ {\prime} \left(x + 1, \mathrm {e} ^ {x}\right) + f _ {2} ^ {\prime} \left(x + 1, \mathrm {e} ^ {x}\right) \cdot \mathrm {e} ^ {x} = (x + 1) ^ {2} + x \cdot 2 (x + 1) = (x + 1) (3 x + 1).</equation><equation>f _ {1} ^ {\prime} \left(x, x ^ {2}\right) + f _ {2} ^ {\prime} \left(x, x ^ {2}\right) \cdot 2 x = 4 x \ln x + 2 x ^ {2} \cdot \frac {1}{x} = 2 x \left(2 \ln x + 1\right).</equation>在（1）式中令 x=0，可得<equation>f_{1}^{\prime}(1,1)+f_{2}^{\prime}(1,1)=1.</equation>在（2）式中令 x=1，可得<equation>f_{1}^{\prime}(1,1)+ 2 f_{2}^{\prime}(1,1)=2.</equation>联立两式解得<equation>f_{1}^{\prime}(1,1)=0,f_{2}^{\prime}(1,1)=1.</equation>因此，<equation>\mathrm{d}f(1,1)=\mathrm{d}y.</equation>应选C.

---

**2020年第11题 | 填空题 | 4分**
11. 设<equation>z=\arctan[ x y+\sin(x+y) ]</equation>, 则<equation>\mathrm{d} z|_{(0,\pi)}=</equation>___
**答案: **<equation>(\pi - 1) \mathrm {d} x - \mathrm {d} y.</equation>
**解析: **根据链式法则，<equation>\frac{\partial z}{\partial x}=\frac{y+\cos(x+y)}{1+\left[ x y+\sin(x+y)\right]^{2}},</equation><equation>\frac{\partial z}{\partial y}=\frac{x+\cos(x+y)}{1+\left[ x y+\sin(x+y)\right]^{2}}.</equation>代入 x=0，y=<equation>\pi</equation>，可得<equation>\frac{\partial z}{\partial x}\bigg|_{(0,\pi)}=\pi-1, \frac{\partial z}{\partial y}\bigg|_{(0,\pi)}=-1.</equation>因此，<equation>\mathrm{d}z\bigg|_{(0,\pi)}=(\pi-1)\mathrm{d}x-\mathrm{d}y.</equation>

---

**2017年第12题 | 填空题 | 4分**
12. 设函数<equation>f(x,y)</equation>具有一阶连续偏导数，且<equation>\mathrm{d} f(x,y)=y \mathrm{e}^{y} \mathrm{d} x+x(1+y) \mathrm{e}^{y} \mathrm{d} y</equation><equation>f(0,0)=0</equation>，则<equation>f(x,y)=</equation>___.
**答案: **##<equation>x y \mathrm{e}^{y}.</equation>
**解析: **由于<equation>\mathrm {d} f (x, y) = y \mathrm {e} ^ {y} \mathrm {d} x + x (1 + y) \mathrm {e} ^ {y} \mathrm {d} y,</equation>故<equation>f_x^{\prime}(x,y) = y\mathrm{e}^{y}, f_y^{\prime}(x,y) = x(1 + y)\mathrm{e}^{y}.</equation>对<equation>f_{x}^{\prime}(x,y)</equation>关于 x积分，得<equation>f (x, y) = \int f _ {x} ^ {\prime} (x, y) \mathrm {d} x = \int y \mathrm {e} ^ {y} \mathrm {d} x = x y \mathrm {e} ^ {y} + \varphi (y),</equation>其中<equation>\varphi(y)</equation>为关于 y的一元函数.

对<equation>x y \mathrm{e}^{y}+\varphi(y)</equation>关于y求偏导数，得<equation>\frac {\partial \left[ x y \mathrm {e} ^ {y} + \varphi (y) \right]}{\partial y} = x \mathrm {e} ^ {y} + x y \mathrm {e} ^ {y} + \varphi^ {\prime} (y) = x (1 + y) \mathrm {e} ^ {y} + \varphi^ {\prime} (y).</equation>与<equation>f_{y}^{\prime}(x,y)</equation>比较，得<equation>\varphi^{\prime}(y)=0</equation>，故<equation>\varphi(y)\equiv C</equation>，其中C为常数.

代入<equation>x=0,y=0</equation>，得<equation>f(0,0)=0+C.</equation>，于是，<equation>C=0.</equation>因此，<equation>f ( x,y) = x y \mathrm{e}^{y}.</equation>

---

**2015年第13题 | 填空题 | 4分**
13. 若函数<equation>z = z(x,y)</equation>由方程<equation>\mathrm{e}^{x+2y+3z} + xyz = 1</equation>确定，则<equation>\mathrm{d}z|_{(0,0)} =</equation>___
**答案: **<equation>- \frac {1}{3} \mathrm {d} x - \frac {2}{3} \mathrm {d} y.</equation>
**解析: **解下面我们分别用上述三种方法解本题.

（法一）对原方程两端分别关于<equation>x,y</equation>求偏导数，可得<equation>\mathrm {e} ^ {x + 2 y + 3 z} \left(1 + 3 \frac {\partial z}{\partial x}\right) + y z + x y \frac {\partial z}{\partial x} = 0.</equation><equation>\mathrm {e} ^ {x + 2 y + 3 z} \left(2 + 3 \frac {\partial z}{\partial y}\right) + x z + x y \frac {\partial z}{\partial y} = 0.</equation>当 x=0,y=0时，由原方程知<equation>\mathrm{e}^{3 z}=1</equation>，故 z(0,0）=0.代入（1）式得<equation>3\frac{\partial z}{\partial x}=-1.</equation>代入（2）式得<equation>3\frac{\partial z}{\partial y}=-2.</equation>因此，<equation>\mathrm{d}z|_{(0,0)} = -\frac{1}{3}\mathrm{d}x - \frac{2}{3}\mathrm{d}y.</equation>（法二）对原方程两端微分，可得<equation>\mathrm{d}\left(\mathrm{e}^{x + 2y + 3z} + xyz\right) = 0</equation>，展开得<equation>\mathrm {e} ^ {x + 2 y + 3 z} \left(\mathrm {d} x + 2 \mathrm {d} y + 3 \mathrm {d} z\right) + y z \mathrm {d} x + x z \mathrm {d} y + x y \mathrm {d} z = 0.</equation>当<equation>x = 0, y = 0</equation>时，由原方程知<equation>\mathrm{e}^{3z} = 1</equation>，故<equation>z(0,0) = 0.</equation>代入（3）式得<equation>\mathrm {d} x + 2 \mathrm {d} y + 3 \mathrm {d} z = 0,</equation>即<equation>\mathrm{d}z\mid_{(0,0)} = -\frac{1}{3}\mathrm{d}x - \frac{2}{3}\mathrm{d}y.</equation>（法三）当<equation>x = 0, y = 0</equation>时，由原方程知<equation>\mathrm{e}^{3z} = 1</equation>，故<equation>z(0,0) = 0.</equation>令<equation>F(x,y,z) = \mathrm{e}^{x + 2y + 3z} + xyz - 1</equation>，则由隐函数存在定理知，<equation>\left. \frac {\partial z}{\partial x} \right| _ {(0, 0)} = - \left. \frac {F _ {x} ^ {\prime}}{F _ {z} ^ {\prime}} \right| _ {(0, 0, 0)} = - \left. \frac {\mathrm {e} ^ {x + 2 y + 3 z} + y z}{3 \mathrm {e} ^ {x + 2 y + 3 z} + x y} \right| _ {(0, 0, 0)} = - \frac {1}{3},</equation><equation>\left. \frac {\partial z}{\partial y} \right| _ {(0, 0)} = - \left. \frac {F _ {y} ^ {\prime}}{F _ {z} ^ {\prime}} \right| _ {(0, 0, 0)} = - \left. \frac {2 \mathrm {e} ^ {x + 2 y + 3 z} + x z}{3 \mathrm {e} ^ {x + 2 y + 3 z} + x y} \right| _ {(0, 0, 0)} = - \frac {2}{3}.</equation>因此，<equation>\mathrm{d}z|_{(0,0)} = -\frac{1}{3}\mathrm{d}x - \frac{2}{3}\mathrm{d}y.</equation>

---

**2014年第11题 | 填空题 | 4分**
11. 设<equation>z=z(x,y)</equation>是由方程<equation>\mathrm{e}^{2 y z}+x+y^{2}+z=\frac{7}{4}</equation>确定的函数，则<equation>\mathrm{d} z|_{\left(\frac{1}{2},\frac{1}{2}\right)}=</equation>___
**答案: **<equation>- \frac {1}{2} \left(\mathrm {d} x + \mathrm {d} y\right).</equation>
**解析: **解（法一）将<equation>x=\frac{1}{2}, y=\frac{1}{2}</equation>代入原方程得<equation>z=0.</equation>对方程两端微分，可得<equation>\mathrm{d}\left(\mathrm{e}^{2yz}\right) + \mathrm{d}x + \mathrm{d}\left(y^{2}\right) + \mathrm{d}z = 0.</equation>进一步得<equation>\mathrm {e} ^ {2 y z} \mathrm {d} (2 y z) + \mathrm {d} x + 2 y \mathrm {d} y + \mathrm {d} z = 0,</equation>即<equation>2 z \mathrm {e} ^ {2 y z} \mathrm {d} y + 2 y \mathrm {e} ^ {2 y z} \mathrm {d} z + \mathrm {d} x + 2 y \mathrm {d} y + \mathrm {d} z = 0.</equation>代入<equation>x=y=\frac{1}{2}, z=0</equation>，可得<equation>\mathrm {d} z + \mathrm {d} x + \mathrm {d} y + \mathrm {d} z = 0,</equation>即<equation>\mathrm{d}z\bigg|_{\left(\frac{1}{2},\frac{1}{2}\right)} = -\frac{1}{2} (\mathrm{d}x + \mathrm{d}y).</equation>（法二）由<equation>\mathrm{d}z = \frac{\partial z}{\partial x}\mathrm{d}x + \frac{\partial z}{\partial y}\mathrm{d}y</equation>知，需求<equation>\left.\frac{\partial z}{\partial x}\right|_{\left(\frac{1}{2},\frac{1}{2}\right)}</equation>和<equation>\left.\frac{\partial z}{\partial y}\right|_{\left(\frac{1}{2},\frac{1}{2}\right)}</equation>.

对方程两端分别关于<equation>x</equation>，y求导，得<equation>\mathrm {e} ^ {2 y z} \cdot 2 y \cdot \frac {\partial z}{\partial x} + 1 + \frac {\partial z}{\partial x} = 0, \quad \mathrm {e} ^ {2 y z} \cdot 2 z + \mathrm {e} ^ {2 y z} \cdot 2 y \cdot \frac {\partial z}{\partial y} + 2 y + \frac {\partial z}{\partial y} = 0.</equation>当<equation>x=y=\frac{1}{2}</equation>时，代入原方程解得<equation>z=0</equation>将<equation>x=y=\frac{1}{2}</equation><equation>z=0</equation>代入（1）式，可分别求得<equation>\frac{\partial z}{\partial x}=-\frac{1}{2},\frac{\partial z}{\partial y}=-\frac{1}{2}.</equation>因此，<equation>\mathrm{d}z\Big|_{\left(\frac{1}{2},\frac{1}{2}\right)} = -\frac{1}{2} (\mathrm{d}x + \mathrm{d}y).</equation>

---


#### 二重积分的概念与性质

**2019年第5题 | 选择题 | 4分 | 答案: A**
5. 已知平面区域<equation>D=\left\{(x,y)\mid|x|+|y|\leqslant \frac{\pi}{2}\right\}, I_{1}=\iint_{D}\sqrt{x^{2}+y^{2}}\mathrm{d}x\mathrm{d}y, I_{2}=\iint_{D}\sin \sqrt{x^{2}+y^{2}}\mathrm{d}x\mathrm{d}y, I_{3}=</equation><equation>\iint_{D}(1-\cos \sqrt{x^{2}+y^{2}})\mathrm{d}x\mathrm{d}y</equation>，则（    ）

A.<equation>I_{3}<I_{2}<I_{1}</equation>B.<equation>I_{2}<I_{1}<I_{3}</equation>C.<equation>I_{1}<I_{2}<I_{3}</equation>D.<equation>I_{2}<I_{3}<I_{1}</equation>
答案: A
**解析: **解如图所示，区域 D由四条直线<equation>x\pm y=\frac{\pi}{2}, x\pm y=-\frac{\pi}{2}</equation>围成.该

区域包含于圆心在原点，半径为<equation>\frac{\pi}{2}</equation>的圆盘区域<equation>\left\{(x,y)\left|x^{2}+y^{2}\leqslant\left(\frac{\pi}{2}\right)^{2}\right.\right\}</equation>.于是，在区域D内，点(x,y）满足<equation>0\leqslant\sqrt{x^{2}+y^{2}}\leqslant\frac{\pi}{2}.</equation>令<equation>u=\sqrt{x^{2}+y^{2}}.</equation>由于在<equation>\left(0,\frac{\pi}{2}\right)</equation>内，<equation>\sin u < u</equation>，故对区域D内的点，均有<equation>\sin \sqrt{x^{2}+y^{2}}<</equation><equation>\sqrt{x^{2}+y^{2}}.</equation>由定积分的保号性可知，<equation>I_{2} < I_{1}.</equation>考虑<equation>1-\cos u</equation>与<equation>\sin u</equation>的大小关系.令<equation>f(u)=\sin u+\cos u-1</equation>，则<equation>f^{\prime}(u)=\cos u-\sin u.</equation>当<equation>0 < u < \frac{\pi}{4}</equation>时，<equation>f^{\prime}(u)>0,f(u)</equation>单调增加；当<equation>\frac{\pi}{4} < u < \frac{\pi}{2}</equation>时，<equation>f^{\prime}(u)<0,f(u)</equation>单调减少.于是，<equation>f(u)</equation>在<equation>\left[0,\frac{\pi}{2}\right]</equation>上的最大值为<equation>f\left(\frac{\pi}{4}\right)=\sqrt{2}-1</equation>，最小值为<equation>f(0)=f\left(\frac{\pi}{2}\right)=0.</equation>在<equation>\left[0,\frac{\pi}{2}\right]</equation>上，<equation>f(u)\geqslant0</equation>即<equation>\sin u\geqslant1-\cos u</equation>，且等号仅当<equation>u=0</equation>和<equation>u=\frac{\pi}{2}</equation>时取得.

因此，对区域 D内的点，均有<equation>\sin \sqrt{x^{2}+y^{2}}\geqslant 1-\cos \sqrt{x^{2}+y^{2}}.</equation>由定积分的保号性可知，<equation>I_{3} < I_{2}.</equation>综上所述，<equation>I_{3} < I_{2} < I_{1}.</equation>应选A.

---

**2013年第6题 | 选择题 | 4分 | 答案: B**
6. 设<equation>D_{k}</equation>是圆域<equation>D=\{(x,y)\mid x^{2}+y^{2}\leqslant 1\}</equation>在第 k象限的部分.记<equation>I_{k}=\iint_{D_{k}}(y-x)\mathrm{d}x\mathrm{d}y(k=1,2,3,4)</equation>，则（    )

A.<equation>I_{1}>0</equation>B.<equation>I_{2}>0</equation>C.<equation>I_{3}>0</equation>D.<equation>I_{4}>0</equation>
答案: B
**解析: **解（法一）由于在第一象限内 x>0，y>0，第二象限内 x<0，y>0，第三象限内 x<0， y<0，第四象限内 x>0，y<0，故被积函数 y-x在第二象限内恒大于零，从而<equation>\iint_{D_{2}}(y-x)\mathrm{d}x\mathrm{d}y>0.</equation>应选B.

（法二）在极坐标系下计算<equation>I_{k}(k = 1,2,3,4).</equation><equation>\begin{aligned} I _ {k} \stackrel {\text {极 坐 标}} {=} \int_ {\frac {(k - 1) \pi}{2}} ^ {\frac {k \pi}{2}} (\sin \theta - \cos \theta) \mathrm {d} \theta \int_ {0} ^ {1} r ^ {2} \mathrm {d} r &= \frac {1}{3} \int_ {\frac {(k - 1) \pi}{2}} ^ {\frac {k \pi}{2}} (\sin \theta - \cos \theta) \mathrm {d} \theta \\ &= - \frac {\left(\sin \theta + \cos \theta\right)}{3} \left| \frac {k \pi}{2} \right. _ {\frac {(k - 1) \pi}{2}}. \end{aligned}</equation>分别求得<equation>I _ {1} = 0, \quad I _ {2} = \frac {2}{3}, \quad I _ {3} = 0, \quad I _ {4} = - \frac {2}{3}.</equation><equation>I_{2} > 0</equation>应选B.

---

**2010年第6题 | 选择题 | 4分 | 答案: D**
6.<equation>\lim_{n\rightarrow \infty}\sum_{i=1}^{n}\sum_{j=1}^{n}\frac{n}{(n+i)(n^{2}+j^{2})}=</equation>(    )

A.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{x}\frac{1}{(1+x)(1+y^{2})}\mathrm{d}y</equation>B.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{x}\frac{1}{(1+x)(1+y)}\mathrm{d}y</equation>C.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{1}\frac{1}{(1+x)(1+y)}\mathrm{d}y</equation>D.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{1}\frac{1}{(1+x)(1+y^{2})}\mathrm{d}y</equation>
答案: D
**解析: **## 解 （法一）考虑将原极限写成二重积分.

令<equation>\Delta\sigma_{ij}=\left[\frac{i-1}{n},\frac{i}{n}\right]\times\left[\frac{j-1}{n},\frac{j}{n}\right]\left(i,j=1,2,\dots,n\right)</equation>，则<equation>\left\{\Delta\sigma_{ij}\right\}_{1\leqslant i,j\leqslant n}</equation>为<equation>D=[0,1]\times[0,1]</equation>上的一个划分，<equation>\Delta\sigma_{ij}</equation>的面积为<equation>\frac{1}{n^{2}}</equation>取<equation>\Delta\sigma_{ij}</equation>上的一点<equation>\left(\frac{i}{n},\frac{j}{n}\right).</equation>由于<equation>\sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {n}{(n + i) \left(n ^ {2} + j ^ {2}\right)} = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {1}{\left(1 + \frac {i}{n}\right) \left(1 + \frac {j ^ {2}}{n ^ {2}}\right)} \cdot \frac {1}{n ^ {2}},</equation>故<equation>\begin{aligned} \text {原 极 限} &= \lim _ {n \rightarrow \infty} \left[ \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {1}{\left(1 + \frac {i}{n}\right)\left(1 + \frac {j ^ {2}}{n ^ {2}}\right)} \right] = \iint_ {D} \frac {1}{(1 + x) \left(1 + y ^ {2}\right)} \mathrm {d} \sigma \\ &= \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {1} \frac {1}{(1 + x) \left(1 + y ^ {2}\right)} \mathrm {d} y. \end{aligned}</equation>应选 D.

（法二）由于所求极限的表达式中 i，j无关，故可以考虑将原极限写成定积分的乘积.由于<equation>\begin{aligned} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {n}{(n + i) \left(n ^ {2} + j ^ {2}\right)} &= \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \left(\frac {1}{1 + \frac {i}{n}} \cdot \frac {1}{n}\right) \left(\frac {1}{1 + \frac {j ^ {2}}{n ^ {2}}} \cdot \frac {1}{n}\right) \\ \underline {{i , j \text {无关}}} \sum_ {i = 1} ^ {n} \left(\frac {1}{1 + \frac {i}{n}} \cdot \frac {1}{n}\right) \sum_ {j = 1} ^ {n} \left(\frac {1}{1 + \frac {j ^ {2}}{n ^ {2}}} \cdot \frac {1}{n}\right), \end{aligned}</equation>故<equation>\begin{aligned} &= \lim _ {n \rightarrow \infty} \sum_ {i = 1} ^ {n} \left(\frac {1}{1 + \frac {i}{n}} \cdot \frac {1}{n}\right) \cdot \lim _ {n \rightarrow \infty} \sum_ {j = 1} ^ {n} \left(\frac {1}{1 + \frac {j ^ {2}}{n ^ {2}}} \cdot \frac {1}{n}\right) = \left(\int_ {0} ^ {1} \frac {1}{1 + x} d x\right)\left(\int_ {0} ^ {1} \frac {1}{1 + y ^ {2}} d y\right) \\ &= \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {1} \frac {1}{(1 + x) \left(1 + y ^ {2}\right)} \mathrm {d} y. \end{aligned}</equation>应选 D.

---


### 一元函数微分学


#### 曲线的凹凸性、拐点及渐近线

**2025年第2题 | 选择题 | 5分 | 答案: B**
2. 已知函数<equation>f ( x )=\int_{0}^{x} \mathrm{e}^{t^{2}} \sin t \mathrm{d} t,g ( x )=\int_{0}^{x} \mathrm{e}^{t^{2}} \mathrm{d} t \cdot \sin^{2} x</equation>，则（    )

A. x=0是 f(x)的极值点，也是 g(x)的极值点

B. x=0是 f(x)的极值点，(0,0)是曲线 y=g(x)的拐点

C. x=0是 f(x)的极值点，(0,0)是曲线 y=f(x)的拐点

D. (0,0)是曲线 y=f(x)的拐点，也是曲线 y=g(x)的拐点
答案: B
**解析: **解 先分析<equation>f ( x )</equation>的性质，分别计算<equation>f^{\prime} ( x )</equation>，<equation>f^{\prime \prime} ( x )</equation>根据链式法则，<equation>f ^ {\prime} (x) = \sin x \mathrm {e} ^ {x ^ {2}},</equation><equation>f ^ {\prime \prime} (x) = 2 x \sin x \mathrm {e} ^ {x ^ {2}} + \cos x \mathrm {e} ^ {x ^ {2}} = \left(2 x \sin x + \cos x\right) \mathrm {e} ^ {x ^ {2}}.</equation>取<equation>\delta</equation>为充分小的正数，当<equation>x\in(-\delta,0)</equation>时，<equation>f^{\prime}(x) < 0,f(x)</equation>单调减少，当<equation>x\in(0,\delta)</equation>时，<equation>f^{\prime}(x) > 0,f(x)</equation>单调增加.于是，<equation>x = 0</equation>是<equation>f(x)</equation>的极小值点.或者，也可以由<equation>f^{\prime}(0) = 0,f^{\prime \prime}(0) = 1 > 0</equation>以及极值的第二充分条件得到<equation>x = 0</equation>是<equation>f(x)</equation>的极小值点.

当<equation>x \in(-\delta ,\delta)</equation>时，<equation>x\sin x \geqslant0,\cos x > 0,f^{\prime \prime}(x)</equation>在<equation>(-\delta ,\delta)</equation>内恒大于0，<equation>y=f(x)</equation>是凹曲线.于是，点（0,0）不是曲线<equation>y=f(x)</equation>的拐点.

再分析<equation>g ( x )</equation>的性质，分别计算<equation>g^{\prime} ( x )</equation>，<equation>g^{\prime \prime} ( x )</equation>根据链式法则，<equation>g ^ {\prime} (x) = \sin^ {2} x \mathrm {e} ^ {x ^ {2}} + 2 \sin x \cos x \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = \sin^ {2} x \mathrm {e} ^ {x ^ {2}} + \sin 2 x \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t,</equation><equation>\begin{aligned} g ^ {\prime \prime} (x) &= 2 \sin x \cos x \mathrm {e} ^ {x ^ {2}} + 2 x \sin^ {2} x \mathrm {e} ^ {x ^ {2}} + \sin 2 x \mathrm {e} ^ {x ^ {2}} + 2 \cos 2 x \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t \\ &= 2 \left(\sin 2 x + x \sin^ {2} x\right) \mathrm {e} ^ {x ^ {2}} + 2 \cos 2 x \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t. \end{aligned}</equation>取<equation>\delta</equation>为充分小的正数，由于<equation>\mathrm{e}^{t^2}</equation>恒大于0，故当<equation>x\in(-\delta,0)</equation>时，<equation>\int_0^x\mathrm{e}^{t^2}\mathrm{d}t < 0</equation>，结合<equation>\sin 2x < 0</equation>可得，<equation>g^{\prime}(x) > 0,g(x)</equation>单调增加，当<equation>x\in(0,\delta)</equation>时，<equation>\int_0^x\mathrm{e}^{t^2}\mathrm{d}t > 0</equation>，结合<equation>\sin 2x > 0</equation>可得，<equation>g^{\prime}(x) > 0,g(x)</equation>单调增加.于是，<equation>x = 0</equation>不是<equation>g(x)</equation>的极值点.

当<equation>x \in (-\delta, 0)</equation>时，<equation>\sin 2x + x\sin^2 x < 0, \int_0^x\mathrm{e}^{t^2}\mathrm{d}t < 0,\cos 2x > 0,g''(x) < 0,y = g(x)</equation>是凸曲线，当<equation>x \in (0,\delta)</equation>时，<equation>\sin 2x + x\sin^2 x > 0, \int_0^x\mathrm{e}^{t^2}\mathrm{d}t > 0,\cos 2x > 0,g''(x) > 0,y = g(x)</equation>是凹曲线.于是，点(0,0)是曲线<equation>y = g(x)</equation>的拐点.

综上所述，应选B.

---

**2025年第12题 | 填空题 | 5分**
12. 曲线<equation>y=\sqrt[3]{x^{3}-3x^{2}+1}</equation>的渐近线方程为 ___
**答案: **<equation>y = x - 1</equation>
**解析: **解 由于函数<equation>\sqrt[3]{x^{3}-3x^{2}+1}</equation>没有间断点，故曲线<equation>y=\sqrt[3]{x^{3}-3x^{2}+1}</equation>没有铅直渐近线又由于<equation>\lim _ {x \rightarrow \infty} \frac {\sqrt [ 3 ]{x ^ {3} - 3 x ^ {2} + 1}}{x} = \lim _ {x \rightarrow \infty} \sqrt [ 3 ]{\frac {x ^ {3} - 3 x ^ {2} + 1}{x ^ {3}}} = \lim _ {x \rightarrow \infty} \sqrt [ 3 ]{1 - \frac {3}{x} + \frac {1}{x ^ {3}}} = 1,</equation>故<equation>\lim_{x\to \infty}\sqrt[3]{x^3 - 3x^2 + 1} = \infty</equation>，从而曲线<equation>y = \sqrt[3]{x^3 - 3x^2 + 1}</equation>没有水平渐近线.

下面计算曲线<equation>y=\sqrt[3]{x^{3}-3x^{2}+1}</equation>的斜渐近线<equation>\begin{aligned} \lim _ {x \rightarrow \infty} \left(\sqrt [ 3 ]{x ^ {3} - 3 x ^ {2} + 1} - x\right) \xlongequal {=} \frac {t = \frac {1}{x}}{\lim _ {t \rightarrow 0}} \lim _ {t \rightarrow 0} \left(\sqrt [ 3 ]{\frac {1}{t ^ {3}} - \frac {3}{t ^ {2}} + 1} - \frac {1}{t}\right) &= \lim _ {t \rightarrow 0} \frac {\sqrt [ 3 ]{t ^ {3} - 3 t + 1} - 1}{t} \\ \frac {\sqrt [ 3 ]{t ^ {3} - 3 t + 1} - 1 - \frac {1}{3} \left(t ^ {3} - 3 t\right)}{\frac {1}{3} \left(t ^ {3} - 3 t\right)} \lim _ {t \rightarrow 0} \frac {\frac {1}{3} \left(t ^ {3} - 3 t\right)}{t} &= - 1. \end{aligned}</equation>因此，曲线<equation>y=\sqrt[3]{x^{3}-3x^{2}+1}</equation>的斜渐近线为<equation>y=x-1.</equation>

---

**2023年第1题 | 选择题 | 5分 | 答案: B**
1. 曲线<equation>y=x\ln \left(\mathrm{e}+\frac{1}{x-1}\right)</equation>的斜渐近线方程为（    )

A.<equation>y=x+\mathrm{e}</equation>B.<equation>y=x+\frac{1}{\mathrm{e}}</equation>C.<equation>y=x</equation>D.<equation>y=x-\frac{1}{\mathrm{e}}</equation>
答案: B
**解析: **先计算<equation>\lim_{x\to \infty}\frac{y}{x}</equation><equation>\lim _ {x \rightarrow \infty} \frac {y}{x} = \lim _ {x \rightarrow \infty} \frac {x \ln \left(\mathrm {e} + \frac {1}{x - 1}\right)}{x} = \lim _ {x \rightarrow \infty} \ln \left(\mathrm {e} + \frac {1}{x - 1}\right) = 1.</equation>由此可得斜渐近线的斜率为1.

下面计算<equation>\lim_{x\to \infty} ( y - x).</equation><equation>\begin{aligned} \lim _ {x \rightarrow \infty} (y - x) &= \lim _ {x \rightarrow \infty} \left[ x \ln \left(e + \frac {1}{x - 1}\right) - x \right] = \lim _ {x \rightarrow \infty} x \left[ \ln \left(e + \frac {1}{x - 1}\right) - 1 \right] \\ &= \lim _ {x \rightarrow \infty} x \left[ \ln \left(e + \frac {1}{x - 1}\right) - \ln e \right] = \lim _ {x \rightarrow \infty} x \ln \left[ 1 + \frac {1}{e (x - 1)} \right] \\ \frac {\ln \left[ 1 + \frac {1}{e (x - 1)} \right] \sim \frac {1}{e (x - 1)}}{\lim _ {x \rightarrow \infty} x \cdot \frac {1}{e (x - 1)}} &= \frac {1}{e}. \end{aligned}</equation>因此，曲线<equation>y=x\ln \left(\mathrm{e}+\frac{1}{x-1}\right)</equation>的斜渐近线方程为<equation>y=x+\frac{1}{e}.</equation>应选B.

---

**2023年第7题 | 选择题 | 5分 | 答案: C**
7. 设函数<equation>f(x)=(x^{2}+a) \mathrm{e}^{x}</equation>，若 f(x)没有极值点，但曲线 y=f(x)有拐点，则 a的取值范围是（

A. [0,1) B.<equation>[1,+\infty)</equation>C.<equation>[1,2)</equation>D.<equation>[2,+\infty)</equation>
答案: C
**解析: **解分别计算<equation>f^{\prime}(x)</equation>与<equation>f^{\prime\prime}(x).</equation><equation>f ^ {\prime} (x) = \left(x ^ {2} + a\right) \mathrm {e} ^ {x} + 2 x \mathrm {e} ^ {x} = \left(x ^ {2} + 2 x + a\right) \mathrm {e} ^ {x},</equation><equation>f ^ {\prime \prime} (x) = \left(x ^ {2} + 2 x + a\right) \mathrm {e} ^ {x} + (2 x + 2) \mathrm {e} ^ {x} = \left(x ^ {2} + 4 x + a + 2\right) \mathrm {e} ^ {x}.</equation>由于<equation>\mathrm{e}^{x} > 0</equation>，故<equation>f^{\prime}(x)</equation>和<equation>f^{\prime\prime}(x)</equation>的符号分别由<equation>x^{2}+2x+a</equation>和<equation>x^{2}+4x+a+2</equation>的符号决定.

由于 f(x)二阶可导，故由极值的第一充分条件可知，f(x）没有极值点说明<equation>f^{\prime}(x)</equation>不变号.这意味着<equation>x^{2}+2 x+a=0</equation>的判别式<equation>\Delta=4-4 a\leqslant0</equation>，解得 a<equation>\geqslant1.</equation>另一方面，由于 f(x)二阶可导，故由拐点的第一充分条件可知，曲线 y=f(x)有拐点说明<equation>f^{\prime\prime}(x)</equation>变号.这意味着<equation>f^{\prime\prime}(x)=0</equation>有两个不同实根。由此可知<equation>x^{2}+4 x+a+2=0</equation>的判别式<equation>\Delta=1 6-4 a-8>0</equation>，解得 a < 2.

取<equation>[ 1, + \infty)</equation>与<equation>(-\infty, 2)</equation>的交集可得，<equation>a \in[ 1, 2)</equation>，应选C.

---

**2022年第3题 | 选择题 | 5分 | 答案: B**
3. 设函数 f(x)在<equation>x=x_{0}</equation>处有二阶导数，则（    )

A. 当 f(x)在<equation>x_{0}</equation>的某邻域内单调增加时，<equation>f^{\prime}(x_{0})>0</equation>B. 当<equation>f^{\prime}(x_{0})>0</equation>时，f(x)在<equation>x_{0}</equation>的某邻域内单调增加

C. 当 f(x)在<equation>x_{0}</equation>的某邻域内是凹函数时，<equation>f^{\prime\prime}(x_{0})>0</equation>D. 当<equation>f^{\prime\prime}(x_{0})>0</equation>时，f(x)在<equation>x_{0}</equation>的某邻域内是凹函数
答案: B
**解析: **解注意到题目条件给出 f(x)在<equation>x= x_{0}</equation>处有二阶导数，故<equation>f^{\prime}(x)</equation>在<equation>x= x_{0}</equation>处连续.从而，<equation>\lim_{x\rightarrow x_{0}}f^{\prime}(x)=f^{\prime}(x_{0})>0.</equation>结合极限的定义可得，存在<equation>\delta >0</equation>，当<equation>x\in(x_{0}-\delta,x_{0}+\delta)</equation>时，<equation>f^{\prime}(x) > 0.</equation>于是，f(x)在<equation>(x_{0}-\delta,x_{0}+\delta)</equation>内单调增加.应选B.

下面说明选项A、C、D不正确.

当 f(x)在<equation>x_{0}</equation>的某邻域内单调增加时，我们能得到在该邻域内<equation>f^{\prime}(x)\geqslant 0</equation>，但却不能保证<equation>f^{\prime}(x) > 0</equation>，因为可能存在有限个点，在这些点处，<equation>f^{\prime}(x)=0</equation>例如<equation>f(x)=x^{3}</equation>，该函数在<equation>(-\infty, +\infty)</equation>上单调增加，但是<equation>f^{\prime}(0)=0</equation>选项A不正确.

对选项C，考虑<equation>f ( x )=x^{4}</equation>，则<equation>f ( x )</equation>为<equation>(-\infty , +\infty)</equation>上的凹函数，但是<equation>f^{\prime \prime}(0)=0.</equation>选项C不正确.

对选项D，我们可以考虑二阶导函数存在间断点的例子.若<equation>x_{0}</equation>为<equation>f^{\prime \prime}(x)</equation>的间断点，则<equation>\lim_{x\to x_{0}}f^{\prime \prime}(x)= f^{\prime \prime}(x_{0})>0</equation>不成立，从而无法通过极限的定义得到<equation>x_{0}</equation>的一个小邻域，在该小邻域内<equation>f^{\prime \prime}(x) > 0.</equation>考虑函数<equation>f ( x )=\left\{\begin{array}{ll}x^{4}\sin \frac{1}{x}+\frac{x^{2}}{4},&x\neq 0,\\ 0,&x=0,\end{array} \right.</equation>该函数在 x=0处存在二阶导数，但是<equation>f^{\prime \prime} ( x )</equation>在 x=0处不连续.

当 x≠0时，<equation>f^{\prime}(x)=4x^{3}\sin \frac{1}{x}-x^{2}\cos \frac{1}{x}+\frac{1}{2}x.</equation>当 x=0时，由导数定义，<equation>f ^ {\prime} (0) = \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0} \frac {x ^ {4} \sin \frac {1}{x} + \frac {x ^ {2}}{4}}{x} = 0.</equation>因此，<equation>f ^ {\prime} (x) = \left\{ \begin{array}{l l} 4 x ^ {3} \sin \frac {1}{x} - x ^ {2} \cos \frac {1}{x} + \frac {1}{2} x, x \neq 0, \\ 0, x = 0. \end{array} \right.</equation>f'(x)在 x=0处连续.

当 x=0时，由导数定义，<equation>f ^ {\prime \prime} (0) = \lim _ {x \rightarrow 0} \frac {f ^ {\prime} (x) - f ^ {\prime} (0)}{x - 0} = \lim _ {x \rightarrow 0} \frac {4 x ^ {3} \sin \frac {1}{x} - x ^ {2} \cos \frac {1}{x} + \frac {1}{2} x}{x} = \frac {1}{2} > 0.</equation>当 x≠0时，<equation>f^{\prime \prime}(x)=1 2 x^{2} \sin \frac{1}{x}-6 x \cos \frac{1}{x}-\sin \frac{1}{x}+\frac{1}{2}.</equation>如图所示，<equation>f^{\prime \prime}(x)</equation>在 x=0附近振荡，振幅为1，在 x=0附近不存在小邻域使得<equation>f^{\prime \prime}(x)</equation>在该邻域上保持不变号，即不存在 x=0的小邻域，使得 f(x)在该邻域上是凹函数或凸函数.选项D不正确.

---

**2021年第18题 | 解答题 | 12分**
18. (本题满分12分）已知<equation>f ( x )=\frac{x \mid x \mid}{1+x}</equation>，求函数 y=f(x）的凹凸区间及渐近线.
**答案: **（<equation>-\infty</equation>，-1）和（0，<equation>+\infty</equation>）为 y=f(x)的凹区间，<equation>(-1,0)</equation>为 y=f(x)的凸区间. y=f(x)共有3条渐近线：x=-1，y=-x+1与 y=x-1.
**解析: **解 f(x)为分段函数，其分段表达式为 f(x）<equation>= \left\{ \begin{array}{l l} \frac{x^{2}}{x+1}, x\geqslant 0, \\ \frac{-x^{2}}{x+1}, x<0. \end{array} \right.</equation>进一步将 f(x)整理可得

当<equation>x\geqslant0</equation>时，<equation>f ^ {\prime} (x) = \left(x - 1 + \frac {1}{x + 1}\right) ^ {\prime} = 1 - \frac {1}{(x + 1) ^ {2}}.</equation><equation>f ^ {\prime \prime} (x) = \left[ 1 - \frac {1}{(x + 1) ^ {2}} \right] ^ {\prime} = 2 (x + 1) ^ {- 3}.</equation>当<equation>x\geqslant0</equation>时，<equation>f^{\prime\prime}(x) > 0,(0,+\infty)</equation>为凹区间.

当 x < 0时，<equation>f ^ {\prime} (x) = \left(1 - x - \frac {1}{x + 1}\right) ^ {\prime} = - 1 + \frac {1}{(x + 1) ^ {2}}.</equation><equation>f ^ {\prime \prime} (x) = \left[ - 1 + \frac {1}{(x + 1) ^ {2}} \right] ^ {\prime} = - 2 (x + 1) ^ {- 3}.</equation>当 x < -1时，<equation>f^{\prime \prime}(x) > 0,(-\infty ,-1)</equation>为凹区间；当<equation>-1 < x < 0</equation>时，<equation>f^{\prime \prime}(x) < 0,(-1,0)</equation>为凸区间. 因此，<equation>(-\infty ,-1)</equation>和（0，<equation>+\infty</equation>）为 y=f(x)的凹区间，<equation>(-1,0)</equation>为 y=f(x)的凸区间.

下面计算 y=f（x）的渐近线.

(1) 由于<equation>\lim_{x\rightarrow -1}\frac{x\left|x\right|}{1+x}=\infty</equation>，故 x=-1为 y=f(x）的铅直渐近线.

(2) 由于当<equation>x\to\pm\infty</equation>时，<equation>\lim_{x\to+\infty}f(x)=+\infty</equation>，故 y=f(x）没有水平渐近线.

(3) 分别考虑<equation>y=f(x)</equation>在<equation>x\rightarrow -\infty</equation>与<equation>x\rightarrow +\infty</equation>时的斜渐近线.<equation>\lim _ {x \rightarrow - \infty} \frac {f (x)}{x} = \lim _ {x \rightarrow - \infty} \frac {- x}{x + 1} = - 1.</equation><equation>\lim _ {x \rightarrow - \infty} [ f (x) - (- x) ] = \lim _ {x \rightarrow - \infty} \left(\frac {- x ^ {2}}{x + 1} + x\right) = \lim _ {x \rightarrow - \infty} \frac {- x ^ {2} + x ^ {2} + x}{x + 1} = \lim _ {x \rightarrow - \infty} \frac {x}{x + 1} = 1.</equation>于是，<equation>y=-x+1</equation>为<equation>y=f(x)</equation>在<equation>x\rightarrow -\infty</equation>时的斜渐近线.<equation>\lim _ {x \rightarrow + \infty} \frac {f (x)}{x} = \lim _ {x \rightarrow + \infty} \frac {x}{x + 1} = 1.</equation><equation>\lim _ {x \rightarrow + \infty} [ f (x) - x ] = \lim _ {x \rightarrow + \infty} \left(\frac {x ^ {2}}{x + 1} - x\right) = \lim _ {x \rightarrow + \infty} \frac {x ^ {2} - x ^ {2} - x}{x + 1} = \lim _ {x \rightarrow + \infty} \frac {- x}{x + 1} = - 1.</equation>于是，<equation>y=x-1</equation>为<equation>y=f(x)</equation>在<equation>x\to +\infty</equation>时的斜渐近线.

因此，<equation>y=f(x)</equation>共有3条渐近线：<equation>x=-1,y=-x+1</equation>与<equation>y=x-1.</equation>

---

**2020年第15题 | 解答题 | 10分**
15. (本题满分10分)

求曲线<equation>y=\frac{x^{1+x}}{(1+x)^{x}}(x>0)</equation>的斜渐近线方程.
**答案: **<equation>斜渐近线方程为 y = \frac {x}{\mathrm {e}} + \frac {1}{2 \mathrm {e}}.</equation>
**解析: **解 根据斜渐近线的定义，先计算<equation>\lim_{x\rightarrow +\infty}\frac{y}{x}.</equation><equation>\begin{aligned} \lim _ {x \rightarrow + \infty} \frac {y}{x} &= \lim _ {x \rightarrow + \infty} \frac {x ^ {x}}{(1 + x) ^ {x}} = \lim _ {x \rightarrow + \infty} \left(\frac {x}{1 + x}\right) ^ {x} = \lim _ {x \rightarrow + \infty} \left(1 - \frac {1}{1 + x}\right) ^ {x} \\ &= \lim _ {x \rightarrow + \infty} \left(1 - \frac {1}{1 + x}\right) ^ {- (1 + x) \cdot \frac {x}{- (1 + x)}} = e ^ {- \lim _ {x \rightarrow + \infty} \frac {x}{1 + x}} = e ^ {- 1}. \end{aligned}</equation>下面计算<equation>\lim_{x\to +\infty}\left(y - \frac{x}{\mathrm{e}}\right)</equation><equation>\lim _ {x \rightarrow + \infty} \left(y - \frac {x}{\mathrm {e}}\right) = \lim _ {x \rightarrow + \infty} x \left[\left(\frac {x}{1 + x}\right) ^ {x} - \frac {1}{\mathrm {e}} \right] = \lim _ {x \rightarrow + \infty} \frac {x}{\mathrm {e}} \left(\mathrm {e} ^ {x \ln \frac {x}{1 + x} + 1} - 1\right).</equation>由（1）式继续计算可得，<equation>\begin{aligned} \lim _ {x \rightarrow + \infty} \left(y - \frac {x}{e}\right) &= \lim _ {x \rightarrow + \infty} \frac {x}{e} \left(e ^ {x \ln \frac {x}{1 + x} + 1} - 1\right) \frac {e ^ {x \ln \frac {x}{1 + x} + 1} - 1 \sim x \ln \frac {x}{1 + x} + 1}{=} \lim _ {x \rightarrow + \infty} \frac {x}{e} \left(x \ln \frac {x}{1 + x} + 1\right) \\ &= \frac {1}{e} \lim _ {x \rightarrow + \infty} \left(x ^ {2} \ln \frac {x}{1 + x} + x\right) \frac {t = \frac {1}{x}}{=} \frac {1}{e} \lim _ {t \rightarrow 0 ^ {+}} \left(\frac {1}{t ^ {2}} \ln \frac {\frac {1}{t}}{1 + \frac {1}{t}} + \frac {1}{t}\right) \\ &= \frac {1}{e} \lim _ {t \rightarrow 0 ^ {+}} \frac {\ln \frac {1}{1 + t} + t}{t ^ {2}} \xlongequal {\text {洛必达}} \frac {1}{e} \lim _ {t \rightarrow 0 ^ {+}} \frac {- \frac {1}{1 + t} + 1}{2 t} = \frac {1}{e} \lim _ {t \rightarrow 0 ^ {+}} \frac {\frac {t}{1 + t}}{2 t} = \frac {1}{2 e}. \end{aligned}</equation>因此，所求斜渐近线方程为<equation>y=\frac{x}{e}+\frac{1}{2e}.</equation>如果不采用倒代换，也可以如下计算<equation>\lim_{x\to +\infty}\left(x^{2}\ln \frac{x}{1+x}+x\right).</equation>由<equation>\ln(1+u)=u-\frac{u^{2}}{2}+o(u^{2})</equation>可得，<equation>\ln \frac{x}{1+x}=\ln \left(1-\frac{1}{1+x}\right)=-\frac{1}{1+x}-\frac{1}{2(1+x)^{2}}+</equation>o<equation>\left[ \frac{1}{(1+x)^{2}} \right].</equation>.于是，<equation>\begin{array}{l} \lim _ {x \rightarrow + \infty} \left(x ^ {2} \ln \frac {x}{1 + x} + x\right) = \lim _ {x \rightarrow + \infty} \left\{- \frac {x ^ {2}}{1 + x} - \frac {x ^ {2}}{2 (1 + x) ^ {2}} + \frac {x (1 + x)}{1 + x} + o \left[ \frac {x ^ {2}}{(1 + x) ^ {2}} \right]\right\} \\ = \lim _ {x \rightarrow + \infty} \left[ \frac {x}{1 + x} - \frac {x ^ {2}}{2 (1 + x) ^ {2}} \right] = 1 - \frac {1}{2} = \frac {1}{2}. \\ \end{array}</equation>

---

**2019年第2题 | 选择题 | 4分 | 答案: B**
2. 曲线<equation>y=x\sin x+2\cos x\left(-\frac{\pi}{2}<x<2\pi\right)</equation>的拐点坐标为（    )

A. (0,2) B.<equation>(\pi,-2)</equation>C.<equation>\left(\frac{\pi}{2},\frac{\pi}{2}\right)</equation>D.<equation>\left(\frac{3\pi}{2},-\frac{3\pi}{2}\right)</equation>
答案: B
**解析: **解分别计算<equation>y^{\prime}(x), y^{\prime \prime}(x).</equation><equation>y ^ {\prime} (x) = x \cos x + \sin x - 2 \sin x = x \cos x - \sin x,</equation><equation>y ^ {\prime \prime} (x) = - x \sin x + \cos x - \cos x = - x \sin x.</equation>在区间<equation>\left(-\frac{\pi}{2}, 2\pi\right)</equation>内，仅有 x=0和 x=<equation>\pi</equation>满足<equation>y^{\prime\prime}(x)=0</equation>.于是，可以排除选项C和选项D.

下面用两种方法来判定选项A和选项B的正确性.

（法一）当<equation>-\frac{\pi}{2} < x < 0</equation>时，<equation>\sin x < 0</equation><equation>y^{\prime\prime}(x) < 0</equation>；当<equation>0 < x < \pi</equation>时，<equation>\sin x > 0</equation><equation>y^{\prime\prime}(x) < 0</equation>由于<equation>y^{\prime\prime}(x)</equation>在 x=0处不变号，故曲线<equation>y=y(x)</equation>经过点（0，2）时，凹凸性没发生改变.点（0，2）不是<equation>y=y(x)</equation>的拐点.选项A不正确.

当 0 < x <<equation>\pi</equation>时，<equation>\sin x > 0</equation><equation>y^{\prime\prime}(x) < 0</equation><equation>\pi < x < 2\pi</equation>时，<equation>\sin x < 0</equation><equation>y^{\prime\prime}(x) > 0</equation>.由于<equation>y^{\prime\prime}(x)</equation>在<equation>x=\pi</equation>处变号，故曲线<equation>y=y(x)</equation>经过点（<equation>\pi,-2</equation>）时，凹凸性改变.点（<equation>\pi,-2</equation>）是<equation>y=y(x)</equation>的拐点.

（法二）计算<equation>y^{\prime \prime \prime}(x).</equation><equation>y ^ {\prime \prime \prime} (x) = - x \cos x - \sin x.</equation>当 x=0时，<equation>y^{\prime \prime \prime}(0)=0</equation>.此时不能确定点（0，2）是否为拐点.当 x=<equation>\pi</equation>时，<equation>y^{\prime \prime \prime}(\pi)=\pi</equation>.由拐点的充分条件可知，点（<equation>\pi,-2</equation>）是曲线 y=y（x）的拐点.

因此，应选B.

---

**2018年第4题 | 选择题 | 4分 | 答案: D**
4. 设函数 f(x)在[0,1]上二阶可导，且<equation>\int_{0}^{1} f(x)\mathrm{d}x=0</equation>，则（    )

A. 当<equation>f^{\prime}(x)<0</equation>时，<equation>f\left(\frac{1}{2}\right)<0</equation>B. 当<equation>f^{\prime\prime}(x)<0</equation>时，<equation>f\left(\frac{1}{2}\right)<0</equation>C. 当<equation>f^{\prime}(x)>0</equation>时，<equation>f\left(\frac{1}{2}\right)<0</equation>D. 当<equation>f^{\prime\prime}(x)>0</equation>时，<equation>f\left(\frac{1}{2}\right)<0</equation>
答案: D
**解析: **解（法一）考虑 f(x)在<equation>x=\frac{1}{2}</equation>处的带有拉格朗日余项的一阶泰勒公式.<equation>f (x) = f \left(\frac {1}{2}\right) + f ^ {\prime} \left(\frac {1}{2}\right) \left(x - \frac {1}{2}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {1}{2}\right) ^ {2},</equation>其中<equation>\xi_{x}</equation>介于x与<equation>\frac{1}{2}</equation>之间.<equation>\begin{aligned} \int_ {0} ^ {1} f (x) \mathrm {d} x &= \int_ {0} ^ {1} \left[ f \left(\frac {1}{2}\right) + f ^ {\prime} \left(\frac {1}{2}\right) \left(x - \frac {1}{2}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {1}{2}\right) ^ {2} \right] \mathrm {d} x \\ \frac {\int_ {0} ^ {1} \left(x - \frac {1}{2}\right) \mathrm {d} x = 0}{\underline {{}}} f \left(\frac {1}{2}\right) + \frac {1}{2} \int_ {0} ^ {1} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {1}{2}\right) ^ {2} \mathrm {d} x. \end{aligned}</equation>由于<equation>\int_{0}^{1} f(x)\mathrm{d}x=0</equation>，故<equation>f\left(\frac{1}{2}\right)=0-\frac{1}{2}\int_{0}^{1} f^{\prime \prime}(\xi_{x})\left(x-\frac{1}{2}\right)^{2}\mathrm{d}x</equation>.当<equation>f^{\prime \prime}(x) > 0</equation>时，<equation>\int_{0}^{1} f^{\prime \prime}(\xi_{x})\left(x-\frac{1}{2}\right)^{2}\mathrm{d}x></equation>0，于是，<equation>f\left(\frac{1}{2}\right)<0</equation>.同理可得，当<equation>f^{\prime \prime}(x)<0</equation>时，<equation>f\left(\frac{1}{2}\right)>0.</equation>因此，应选D.

下面说明选项A和选项C不正确.

选项A：考虑<equation>f(x)=-x+\frac{1}{2}</equation>，则<equation>f^{\prime}(x)=-1<0</equation>且<equation>\int_{0}^{1} f(x)\mathrm{d}x=0</equation>，但<equation>f\left(\frac{1}{2}\right)=0.</equation>选项C：考虑<equation>f ( x )=x-\frac{1}{2}</equation>，则<equation>f^{\prime}(x)=1>0</equation>且<equation>\int_{0}^{1} f(x)\mathrm{d}x=0</equation>，但<equation>f\left(\frac{1}{2}\right)=0.</equation>（法二）记<equation>g ( x )=f^{\prime}\left(\frac{1}{2}\right)\left(x-\frac{1}{2}\right)+f\left(\frac{1}{2}\right)</equation>，则 y = g ( x ) 为曲线 y = f ( x ) 在点<equation>\left(\frac{1}{2}, f\left(\frac{1}{2}\right)\right)</equation>处的切线.

如图所示，当<equation>f^{\prime \prime}(x) > 0</equation>时，由凹曲线的几何性质可知，曲线<equation>y=f(x)</equation>在点<equation>\left(\frac{1}{2}, f\left(\frac{1}{2}\right)\right)</equation>处的切线<equation>y=g(x)</equation>位于<equation>y=f(x)</equation>之下，即<equation>g(x)\leqslant f(x).</equation>由于<equation>f^{\prime \prime}(x) > 0</equation>，故 f(x)在[0,1]上不恒等于 g(x)，从而由定积分的性质可知，<equation>0=\int_{0}^{1} f(x)\mathrm{d} x>\int_{0}^{1} g(x)\mathrm{d} x=\int_{0}^{1} f\left(\frac{1}{2}\right)\mathrm{d} x+\int_{0}^{1} f^{\prime}\left(\frac{1}{2}\right)\left(x-\frac{1}{2}\right)\mathrm{d} x=f\left(\frac{1}{2}\right).</equation>因此，<equation>f\left(\frac{1}{2}\right)<0</equation>应选D.

---

**2018年第10题 | 填空题 | 4分**
10. 曲线<equation>y=x^{2}+2\ln x</equation>在其拐点处的切线方程是 ___
**答案: **<equation>y = 4 x - 3.</equation>
**解析: **解记<equation>f ( x )=x^{2}+2 \ln x</equation>，则<equation>f^{\prime}(x)=2 x+\frac{2}{x}, f^{\prime\prime}(x)=2-\frac{2}{x^{2}}.</equation>曲线<equation>y=f(x)</equation>的拐点<equation>\left(x_{0},f\left(x_{0}\right)\right)</equation>满足<equation>f^{\prime\prime}\left(x_{0}\right)=0</equation>解<equation>2-\frac{2}{x_{0}^{2}}=0</equation>得<equation>x_{0}=\pm 1.</equation>由于f(x)的自然定义域为<equation>(0,+\infty)</equation>，故<equation>x_{0}=1</equation>，拐点坐标为(1,1).

又因为<equation>f^{\prime}(1)=\left(2 x+\frac{2}{x}\right)\bigg|_{x=1}=4</equation>，所以拐点（1，1）处的切线方程为<equation>y-1=4(x-1)</equation>即<equation>y=4 x-3.</equation>

---

**2017年第2题 | 选择题 | 4分 | 答案: B**
2. 设二阶可导函数<equation>f ( x )</equation>满足<equation>f ( 1 )=f (-1)=1, f ( 0 )=-1</equation>且<equation>f^{\prime \prime} ( x ) > 0</equation>，则（    ）

A.<equation>\int_{-1}^{1} f ( x ) \mathrm{d} x>0</equation>B.<equation>\int_{-1}^{1} f ( x ) \mathrm{d} x<0</equation>C.<equation>\int_{-1}^{0} f ( x ) \mathrm{d} x> \int_{0}^{1} f ( x ) \mathrm{d} x</equation>D.<equation>\int_{-1}^{0} f ( x ) \mathrm{d} x<\int_{0}^{1} f ( x ) \mathrm{d} x</equation>
答案: B
**解析: **解（法一）如图所示，用直线连接点<equation>(-1,1),(0,-1),(1,1).</equation>记这三点所过折线为 y = g(x). 根据 g(-1) = g(1) = 1,g(0) = -1，求得<equation>g ( x )= 2 \mid x \mid-1.</equation>y = g(x)关于y轴对称.

由于<equation>f^{\prime \prime}(x) > 0</equation>，故 y=f(x）是凹曲线.根据凹曲线的性质，曲线 y=f(x)位于曲线 y=g(x)以下，即 f(x)<equation>\leqslant</equation>g(x)，等号仅在 x=0，<equation>\pm 1</equation>处取得.

因此，<equation>\int_ {- 1} ^ {1} f (x) \mathrm {d} x < \int_ {- 1} ^ {1} g (x) \mathrm {d} x \xlongequal {\text {对称性}} 2 \int_ {0} ^ {1} (2 x - 1) \mathrm {d} x = 0.</equation>应选B.

（法二）记<equation>g ( x )=\frac{f ( x )-f ( 0 )}{x}</equation>，则 g(x)在（0,1]上可导.<equation>g ^ {\prime} (x) = \frac {x f ^ {\prime} (x) - [ f (x) - f (0) ]}{x ^ {2}}.</equation>对[0,1]上的<equation>f(x)</equation>使用拉格朗日中值定理，可得<equation>f(x)-f(0)=f^{\prime}(\xi)x</equation>其中<equation>\xi \in(0,x).</equation>由<equation>f^{\prime \prime}(x)>0</equation>可知，<equation>f^{\prime}(x)>f^{\prime}(\xi).</equation>代入（1）式，可得<equation>g ^ {\prime} (x) = \frac {x \left[ f ^ {\prime} (x) - f ^ {\prime} (\xi) \right]}{x ^ {2}} = \frac {f ^ {\prime} (x) - f ^ {\prime} (\xi)}{x} > 0.</equation>于是，<equation>g ( x )</equation>在（0，1]上单调增加，<equation>g ( x ) < g ( 1 )</equation>即<equation>f ( x ) < 2 x - 1.</equation>因此，<equation>\int_ {0} ^ {1} f (x) \mathrm {d} x < \int_ {0} ^ {1} (2 x - 1) \mathrm {d} x = 0.</equation>同理讨论[-1,0）上的 g(x）可得 g(x）在[-1,0）上单调增加，从而 g（-1）<g(x).于是对 [ -1,0 )上的 f(x)，有 f(x) < -2x-1.

因此，<equation>\int_ {- 1} ^ {0} f (x) \mathrm {d} x < \int_ {- 1} ^ {0} (- 2 x - 1) \mathrm {d} x = 0.</equation>综上所述，<equation>\int_{-1}^{1} f ( x ) \mathrm{d} x < 0</equation>应选B.

（法三）排除法.

取特殊的 f(x) ，使其满足<equation>f(-1)=f(1)=1,f(0)=-1</equation>，且<equation>f^{\prime \prime}(x) > 0.</equation>由于<equation>f^{\prime \prime}(x) > 0</equation>，故不妨取二次函数<equation>f(x)=ax^{2}+bx+c</equation>，且 a > 0.代入点（-1，1），（1，1）和（0，-1），可解得 a=2,b=0,c=-1.于是，设<equation>f(x)=2x^{2}-1.</equation>由于<equation>\int_ {- 1} ^ {1} \left(2 x ^ {2} - 1\right) \mathrm {d} x \xlongequal {\text {对称性}} 2 \int_ {0} ^ {1} \left(2 x ^ {2} - 1\right) \mathrm {d} x = 2 \left(\frac {2}{3} x ^ {3} - x\right) \Bigg | _ {0} ^ {1} = - \frac {2}{3} < 0,</equation>故可排除选项A.

进一步，可验证对<equation>f ( x )=2 x^{2}-1,</equation><equation>\int_ {- 1} ^ {0} f (x) \mathrm {d} x = \int_ {0} ^ {1} f (x) \mathrm {d} x = - \frac {1}{3}.</equation>可排除选项C和选项D.因此，应选B.

---

**2017年第9题 | 填空题 | 4分**
9. 曲线<equation>y=x\left(1+\arcsin \frac{2}{x}\right)</equation>的斜渐近线方程为 ___
**答案: **# y=x+2.
**解析: **计算<equation>\lim_{x\to \infty}\frac{y(x)}{x}.</equation><equation>\binom{x\to +\infty}{x\to -\infty}</equation><equation>\lim _ {x \rightarrow \infty} \frac {y (x)}{x} = \lim _ {x \rightarrow \infty} \frac {x \left(1 + \arcsin \frac {2}{x}\right)}{x} = \lim _ {x \rightarrow \infty} \left(1 + \arcsin \frac {2}{x}\right) = 1.</equation>计算<equation>\lim_{x\to \infty} \left[ y(x)-x\right].</equation><equation>\lim _ {x \rightarrow \infty} \left[ y (x) - x \right] = \lim _ {x \rightarrow \infty} x \arcsin \frac {2}{x} \frac {\arcsin \frac {2}{x} - \frac {2}{x}}{\overline {{\text {一}}}} \lim _ {x \rightarrow \infty} \left(x \cdot \frac {2}{x}\right) = 2.</equation>因此，斜渐近线方程为<equation>y=x+2.</equation>

---

**2016年第4题 | 选择题 | 4分 | 答案: B**
4. 设函数<equation>f ( x )</equation>在<equation>(-\infty, +\infty)</equation>内连续，其导函数的图形如图所示，则（    ）

A. 函数 f(x)有2个极值点，曲线 y=f(x)有2个拐点

B. 函数 f(x)有2个极值点，曲线 y=f(x)有3个拐点

C. 函数 f(x)有3个极值点，曲线 y=f(x)有1个拐点

D. 函数 f(x)有3个极值点，曲线 y=f(x)有2个拐点
答案: B
**解析: **解 观察图形，<equation>f ( x )</equation>共有4个可能的极值点，从左至右依次记为<equation>x_{1},</equation><equation>x_{2}, x_{3}, x_{4}</equation>其中<equation>x_{2}</equation>为虚线与x轴的交点，其余三点为<equation>f^{\prime}(x)</equation>与x轴的交点.在<equation>x=x_{1}, x_{3}, x_{4}</equation>处，<equation>f^{\prime}(x)=0</equation>在<equation>x=x_{2}</equation>处，<equation>f ( x )</equation>不可导.

分别考察<equation>x=x_{1}, x_{2}, x_{3}, x_{4}</equation>左、右小邻域内的<equation>f^{\prime}(x)</equation>的符号.

- 当<equation>x < x_{1}</equation>时，<equation>f^{\prime}(x) > 0</equation>；当<equation>x_{1} < x < x_{2}</equation>时，<equation>f^{\prime}(x) < 0</equation>故<equation>x=x_{1}</equation>是<equation>f(x)</equation>的极大值点.

- 当<equation>x_{1} < x < x_{2}</equation>时，<equation>f^{\prime}(x) < 0</equation>；当<equation>x_{2} < x < x_{3}</equation>时，<equation>f^{\prime}(x) < 0</equation>故<equation>x = x_{2}</equation>不是<equation>f(x)</equation>的极值点.

- 当<equation>x_{2} < x < x_{3}</equation>时，<equation>f^{\prime}(x) < 0</equation>；当<equation>x_{3} < x < x_{4}</equation>时，<equation>f^{\prime}(x) > 0</equation>故<equation>x = x_{3}</equation>是f(x)的极小值点.

- 当<equation>x_{3} < x < x_{4}</equation>时，<equation>f^{\prime}(x) > 0</equation>；当<equation>x > x_{4}</equation>时，<equation>f^{\prime}(x) > 0</equation>故<equation>x=x_{4}</equation>不是 f(x)的极值点.

因此，f（x）共有2个极值点.

曲线<equation>y=f(x)</equation>的可能拐点从左至右依次为<equation>\left(x_{2},f\left(x_{2}\right)\right),\left(x_{5},f\left(x_{5}\right)\right),\left(x_{4},f\left(x_{4}\right)\right)</equation>其中<equation>f^{\prime \prime}\left(x_{2}\right)</equation>不存在，<equation>f^{\prime \prime}\left(x_{5}\right)=f^{\prime \prime}\left(x_{4}\right)=0.</equation>- 当<equation>x < x_{2}</equation>时，<equation>f^{\prime}(x)</equation>单调减少；当<equation>x_{2} < x < x_{5}</equation>时，<equation>f^{\prime}(x)</equation>单调增加.故点（<equation>x_{2}, f(x_{2})</equation>）是曲线<equation>y=f(x)</equation>的拐点.

- 当<equation>x_{2} < x < x_{5}</equation>时，<equation>f^{\prime}(x)</equation>单调增加；当<equation>x_{5} < x < x_{4}</equation>时，<equation>f^{\prime}(x)</equation>单调减少.故点<equation>\left(x_{5}, f\left(x_{5}\right)\right)</equation>是曲线<equation>y=f(x)</equation>的拐点.

- 当<equation>x_{5} < x < x_{4}</equation>时，<equation>f^{\prime}(x)</equation>单调减少；当<equation>x > x_{4}</equation>时，<equation>f^{\prime}(x)</equation>单调增加. 故点<equation>\left(x_{4}, f\left(x_{4}\right)\right)</equation>是曲线<equation>y=f(x)</equation>的拐点.

因此，曲线 y=f(x）共有3个拐点.

综上所述，应选B.

---

**2016年第5题 | 选择题 | 4分 | 答案: A**
5. 设函数<equation>f_{i}(x)(i=1,2)</equation>具有二阶连续导数，且<equation>f_{i}^{\prime \prime}(x_{0})<0 (i=1,2).</equation>若两条曲线<equation>y=f_{i}(x)(i=1,2)</equation>在点<equation>(x_{0},y_{0})</equation>处具有公切线<equation>y=g(x)</equation>，且在该点处曲线<equation>y=f_{1}(x)</equation>的曲率大于曲线<equation>y=f_{2}(x)</equation>的曲率，则在<equation>x_{0}</equation>的某个邻域内，有（    ）

A.<equation>f_{1}(x)\leqslant f_{2}(x)\leqslant g(x)</equation>B.<equation>f_{2}(x)\leqslant f_{1}(x)\leqslant g(x)</equation>C.<equation>f_{1}(x)\leqslant g(x)\leqslant f_{2}(x)</equation>D.<equation>f_{2}(x)\leqslant g(x)\leqslant f_{1}(x)</equation>
答案: A
**解析: **解（法一）首先，由于函数<equation>f_{i}(x)(i=1,2)</equation>具有二阶连续导数，<equation>f_{i}^{\prime \prime}(x_{0})<0(i=1,2)</equation>，故<equation>y=f_{i}(x)(i=1,2)</equation>在<equation>x_{0}</equation>对应的点附近均为凸曲线.由凸曲线的性质可知，它们的公切线位于它们上方.因此，<equation>f_{i}(x)\leqslant g(x)(i=1,2).</equation>另一方面，由于<equation>y=f_{1}(x)</equation>和<equation>y=f_{2}(x)</equation>在点<equation>\left(x_{0},y_{0}\right)</equation>处具有公切线，故在点<equation>\left(x_{0},y_{0}\right)</equation>处，<equation>f_{1}^{\prime}\left(x_{0}\right)=f_{2}^{\prime}\left(x_{0}\right).</equation>根据曲率的定义，<equation>K _ {1} = \frac {\left| f _ {1} ^ {\prime \prime} \left(x _ {0}\right) \right|}{\left(1 + \left[ f _ {1} ^ {\prime} \left(x _ {0}\right) \right] ^ {2}\right) ^ {\frac {3}{2}}}, \quad K _ {2} = \frac {\left| f _ {2} ^ {\prime \prime} \left(x _ {0}\right) \right|}{\left(1 + \left[ f _ {2} ^ {\prime} \left(x _ {0}\right) \right] ^ {2}\right) ^ {\frac {3}{2}}}.</equation>由<equation>K_{1} > K_{2}</equation>可知，<equation>|f_{1}^{\prime \prime}(x_{0})| > |f_{2}^{\prime \prime}(x_{0})|.</equation>由于<equation>f_{i}^{\prime \prime}(x_{0}) < 0(i = 1,2)</equation>，故<equation>f_{1}^{\prime \prime}(x_{0}) < f_{2}^{\prime \prime}(x_{0})</equation>考虑函数<equation>F ( x )=f_{1} ( x )-f_{2} ( x ).</equation>由<equation>y=f_{1} ( x )</equation>和<equation>y=f_{2} ( x )</equation>在点<equation>\left(x_{0}, y_{0}\right)</equation>处相切知，<equation>F \left(x_{0}\right)=0</equation><equation>F^{\prime}\left(x_{0}\right)=0.</equation>而由前面的论述可知，<equation>F^{\prime \prime}\left(x_{0}\right)=f_{1}^{\prime \prime}\left(x_{0}\right)-f_{2}^{\prime \prime}\left(x_{0}\right)<0.</equation>由极值的第二充分条件可知，<equation>x=x_{0}</equation>是 F(x）的极大值点，从而在<equation>x_{0}</equation>的某个足够小的邻域内，<equation>F ( x )\leqslant F \left(x_{0}\right)=0</equation>即<equation>f_{1} ( x )\leqslant f_{2} ( x ).</equation>综上所述，应选A.

（法二）特殊值法.我们将题中的两条曲线分别取作两段圆弧.

以点<equation>\left(\frac{1}{4},\frac{1}{4}\right)</equation>为圆心，<equation>\frac{\sqrt{2}}{4}</equation>为半径作圆，取其位于直线<equation>y=\frac{1}{4}</equation>以上，<equation>x=\frac{1}{4}</equation>以右的部分作为曲线<equation>y=f_{1}(x)</equation>；以原点为圆心，<equation>\frac{\sqrt{2}}{2}</equation>为半径作圆，取其在第一象限内的部分作为曲线<equation>y=f_{2}(x).</equation>这两段圆弧均为凸曲线，且在点<equation>\left(\frac{1}{2},\frac{1}{2}\right)</equation>处相切.在该点处，

y = f1(x)的曲率大于 y = f2(x)的曲率.两条曲线的公切线为 x + y = 1，即 y = g(x).由图形易知，在切点附近，<equation>f_{1}(x)\leqslant f_{2}(x)\leqslant g(x).</equation>应选A.

---

**2016年第9题 | 填空题 | 4分**
9. 曲线<equation>y=\frac{x^{3}}{1+x^{2}}+\arctan(1+x^{2})</equation>的斜渐近线方程为 ___
**答案: **# y = x +<equation>\frac{\pi}{2}.</equation>
**解析: **解 记曲线为<equation>y=f(x).</equation>根据斜渐近线的定义，考虑<equation>\lim_{x\to \infty}\frac{f(x)}{x}.</equation><equation>\lim _ {x \rightarrow \infty} \frac {f (x)}{x} = \lim _ {x \rightarrow \infty} \left[ \frac {x ^ {2}}{1 + x ^ {2}} + \frac {\arctan \left(1 + x ^ {2}\right)}{x} \right] = 1 + \lim _ {x \rightarrow \infty} \frac {\arctan \left(1 + x ^ {2}\right)}{x} = 1.</equation>最后一个等号成立是因为反正切函数<equation>\arctan x</equation>的值域为<equation>\left(-\frac{\pi}{2},\frac{\pi}{2}\right)</equation>从而<equation>|\arctan(1+x^{2})|<\frac{\pi}{2},</equation>所以<equation>\lim_{x\to \infty}\frac{\arctan(1+x^{2})}{x}=0.</equation>再考虑<equation>\lim_{x\to \infty}[f(x)-x].</equation><equation>\begin{aligned} \lim _ {x \rightarrow \infty} [ f (x) - x ] &= \lim _ {x \rightarrow \infty} \left[ \frac {x ^ {3}}{1 + x ^ {2}} + \arctan \left(1 + x ^ {2}\right) - \frac {x \left(1 + x ^ {2}\right)}{1 + x ^ {2}} \right] = \lim _ {x \rightarrow \infty} \frac {- x}{1 + x ^ {2}} + \lim _ {x \rightarrow \infty} \arctan \left(1 + x ^ {2}\right) \\ &= 0 + \lim _ {x \rightarrow \infty} \arctan \left(1 + x ^ {2}\right) = \frac {\pi}{2}. \end{aligned}</equation>因此，所求斜渐近线的方程为<equation>y=x+\frac{\pi}{2}.</equation>

---

**2015年第4题 | 选择题 | 4分 | 答案: C**
4. 设函数在<equation>(-\infty, +\infty)</equation>内连续，其2阶导函数<equation>f^{\prime \prime}(x)</equation>的图形如图所示，则曲线<equation>y=f(x)</equation>的拐点个数为（    ）

A. 0 B. 1 C. 2 D. 3
答案: C
**解析: **解 由图可知，在<equation>(-\infty, +\infty)</equation>上，<equation>f^{\prime \prime}(x)=0</equation>有两个实根<equation>x_{1}, x_{2}</equation>，且<equation>f^{\prime \prime}(x)</equation>在<equation>x=0</equation>处无定义.

下面我们分别讨论点<equation>\left(x_{1},f\left(x_{1}\right)\right),\left(0,f(0)\right)</equation>和<equation>\left(x_{2},f\left(x_{2}\right)\right)</equation>是否为拐点.

在<equation>x = x_{1}</equation>的左、右邻域内，<equation>f^{\prime \prime}(x)</equation>均大于零.<equation>f^{\prime \prime}(x)</equation>在该点两侧不变号，故点<equation>(x_{1}, f(x_{1}))</equation>不是曲线<equation>y = f(x)</equation>的拐点.

在<equation>x=0</equation>的左侧邻域内，<equation>f^{\prime \prime}(x) > 0</equation>；在<equation>x=0</equation>的右侧邻域内，<equation>f^{\prime \prime}(x) < 0.</equation><equation>f^{\prime \prime}(x)</equation>在该点两侧变号，故点（0，<equation>f(0)</equation>）是曲线<equation>y=f(x)</equation>的拐点.

在<equation>x= x_{2}</equation>的左侧邻域内，<equation>f^{\prime \prime}(x)<0</equation>；在<equation>x= x_{2}</equation>的右侧邻域内，<equation>f^{\prime \prime}(x)>0.</equation><equation>f^{\prime \prime}(x)</equation>在该点两侧变号，故点（<equation>x_{2}, f\left(x_{2}\right)</equation>）是曲线<equation>y=f(x)</equation>的拐点.

综上所述，曲线<equation>y=f(x)</equation>共有2个拐点，应选C.

---

**2014年第2题 | 选择题 | 4分 | 答案: C**
2. 下列曲线中有渐近线的是（    ）

A. y=x+<equation>\sin x</equation>B. y=x²+<equation>\sin x</equation>C. y=x+<equation>\sin \frac{1}{x}</equation>D. y=x²+<equation>\sin \frac{1}{x}</equation>
答案: C
**解析: **解 先考察各曲线是否具有铅直渐近线.<equation>y=x+\sin x,y=x^{2}+\sin x</equation>在<equation>(-\infty ,+\infty)</equation>上均无间断点，故不存在铅直渐近线；<equation>y=x+\sin \frac{1}{x}</equation>和<equation>y=x^{2}+\sin \frac{1}{x}</equation>在<equation>x=0</equation>处无定义，但<equation>\lim_{x\to 0}\sin \frac{1}{x}</equation>不存在，从而也没有铅直渐近线.

再考察它们是否具有水平渐近线.

由于选项A、B、C、D中的曲线在<equation>x\to +\infty</equation>和<equation>x\to -\infty</equation>时均趋于<equation>\infty</equation>，故它们均没有水平渐近线最后考察它们是否具有斜渐近线.

对选项C，<equation>\lim\limits_{x\to \infty}\frac{x+\sin \frac{1}{x}}{x}=1</equation>，且<equation>\lim\limits_{x\to \infty}\left(x+\sin \frac{1}{x}-x\right)=\lim\limits_{x\to \infty}\sin \frac{1}{x}=0</equation>，故 y=x+sin<equation>\frac{1}{x}</equation>有斜渐近线 y=x.应选C.

下面我们说明选项A、B、D没有斜渐近线.

对选项A，<equation>\lim\limits_{x\to \infty}\frac{x+\sin x}{x}=1</equation>，但<equation>\lim\limits_{x\to \infty}\left(x+\sin x-x\right)=\lim\limits_{x\to \infty}\sin x</equation>，而<equation>\lim\limits_{x\to \infty}\sin x</equation>不存在，故选项A没有斜渐近线.

对选项B，<equation>\lim_{x\rightarrow \infty}\frac{x^{2}+\sin x}{x}=\infty</equation>；对选项D，<equation>\lim_{x\rightarrow \infty}\frac{x^{2}+\sin \frac{1}{x}}{x}=\infty</equation>，故选项B和选项D都没有斜渐近线.

---

**2014年第3题 | 选择题 | 4分 | 答案: D**
3. 设函数 f(x)具有2阶导数，<equation>g ( x )=f ( 0 ) ( 1-x )+f ( 1 ) x</equation>，则在区间[0,1]上，（    ）

A. 当<equation>f^{\prime}(x)\geqslant0</equation>时，<equation>f(x)\geqslant g(x)</equation>B. 当<equation>f^{\prime}(x)\geqslant0</equation>时，<equation>f(x)\leqslant g(x)</equation>C. 当<equation>f^{\prime\prime}(x)\geqslant0</equation>时，<equation>f(x)\geqslant g(x)</equation>D. 当<equation>f^{\prime\prime}(x)\geqslant0</equation>时，<equation>f(x)\leqslant g(x)</equation>
答案: D
**解析: **分析本题主要考查曲线的凹凸性. 对此类题，常用数形结合的方法.

(a)

(b)

设<equation>f(x)</equation>在区间<equation>I</equation>上连续，<equation>x_{1}, x_{2}</equation>为<equation>I</equation>中任意两点。不妨设<equation>x_{1} < x_{2}</equation>- 若恒有<equation>f\left(\frac{x_{1} + x_{2}}{2}\right) < \frac{f\left(x_{1}\right) + f\left(x_{2}\right)}{2}</equation>，则称曲线<equation>y = f(x)</equation>在区间I上凹，如图(a)；

- 若恒有<equation>f\left(\frac{x_{1} + x_{2}}{2}\right) > \frac{f\left(x_{1}\right) + f\left(x_{2}\right)}{2}</equation>，则称曲线<equation>y = f(x)</equation>在区间I上凸，如图(b).

从图形上看，过凹曲线<equation>y = f(x)</equation>上的任意两点的弦<equation>y = g(x)</equation>均位于该凹曲线之上，即<equation>f(x)\leqslant g(x)</equation>；过凸曲线<equation>y = f(x)</equation>上的任意两点的弦<equation>y = g(x)</equation>均位于该凸曲线之下，即<equation>f(x)\geqslant g(x)</equation>.

解 由于<equation>g ( x ) = \frac { f ( 1 ) - f ( 0 ) } { 1 - 0 } x + f ( 0 ) , g ( 0 ) = f ( 0 )</equation><equation>g ( 1 ) = f ( 1 )</equation>，故<equation>y = g ( x )</equation>表示的曲线是过点（0，f(0)），（1，f(1)）的弦.

由分析知，若<equation>y=f(x)</equation>在[0，1]上凹，则<equation>f(x)\leqslant g(x)</equation>；若<equation>y=f(x)</equation>在[0，1]上凸，则<equation>f(x)\geqslant g(x).</equation>由于f(x）具有2阶导数，故曲线的凹凸性可以由<equation>f^{\prime \prime}(x)</equation>确定.当<equation>f^{\prime \prime}(x)\geqslant 0</equation>时，<equation>y=f(x)</equation>在[0，1]上凹，从而<equation>f(x)\leqslant g(x).</equation>应选D.

一阶导数的符号与曲线的凹凸性没有直接关系。作为选项A的反例，可以考虑曲线<equation>y=x^{2}</equation>；作为选项B的反例，可以考虑曲线<equation>y=\sqrt{x}.</equation>

---

**2012年第1题 | 选择题 | 4分 | 答案: C**
1. 曲线<equation>y=\frac{x^{2}+x}{x^{2}-1}</equation>的渐近线的条数为（    ）

A.0 B.1 C.2 D.3
答案: C
**解析: **解 先判断曲线的铅直渐近线.

由于<equation>y = \frac{x^2 + x}{x^2 - 1}</equation>在<equation>x = \pm 1</equation>时间断，故可以分别考虑<equation>\lim_{x\to -1}\frac{x^2 + x}{x^2 - 1}</equation>和<equation>\lim_{x\to 1}\frac{x^2 + x}{x^2 - 1}</equation>.

由于<equation>\lim_{x\to -1}\frac{x^2 + x}{x^2 - 1} = \lim_{x\to -1}\frac{x}{x - 1} = \frac{1}{2}</equation>，故<equation>x = -1</equation>为<equation>y(x)</equation>的可去间断点.

由于<equation>\lim_{x\to 1}\frac{x^{2}+x}{x^{2}-1}=\lim_{x\to 1}\frac{x}{x-1}=\infty</equation>，故 x=1为 y(x)的无穷间断点.直线 x=1为曲线的铅直渐近线.

再判断曲线的水平渐近线

由于<equation>\lim_{x\to \infty}\frac{x^{2}+x}{x^{2}-1}=1</equation>，故直线 y=1为曲线的水平渐近线最后，由于<equation>\lim _ {\substack {x \rightarrow \infty \\ \left( \begin{array}{c} x \rightarrow + \infty \\ x \rightarrow - \infty \end{array} \right)}} \frac {y (x)}{x} = \lim _ {\substack {x \rightarrow \infty \\ \left( \begin{array}{c} x \rightarrow + \infty \\ x \rightarrow - \infty \end{array} \right)}} \frac {x + 1}{x ^ {2} - 1} = \lim _ {\substack {x \rightarrow \infty \\ \left( \begin{array}{c} x \rightarrow + \infty \\ x \rightarrow - \infty \end{array} \right)}} \frac {1}{x - 1} = 0,</equation>故曲线没有斜渐近线.

综上所述，曲线共有2条渐近线，如图所示.应选C.

---

**2011年第16题 | 解答题 | 10分**
16. (本题满分11分)

设函数 y=y(x）由参数方程<equation>\left\{ \begin{array}{l l} x=\frac{1}{3} t^{3}+t+\frac{1}{3} \\ y=\frac{1}{3} t^{3}-t+\frac{1}{3} \end{array} \right.</equation>点.<equation>y = y (x)</equation>
**答案: **(16) 极大值<equation>y(-1)=1</equation>，极小值<equation>y\left(\frac{5}{3}\right)=-\frac{1}{3}</equation>，凹区间<equation>\left(\frac{1}{3},+\infty\right)</equation>，凸区间<equation>\left(-\infty ,\frac{1}{3}\right)</equation>，拐点<equation>\left(\frac{1}{3},\frac{1}{3}\right).</equation>
**解析: **解求 y=y(x）的导数<equation>y^{\prime}(x)</equation>以及<equation>y^{\prime\prime}(x).</equation><equation>y ^ {\prime} (x) = \frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {t ^ {2} - 1}{t ^ {2} + 1}.</equation><equation>y ^ {\prime \prime} (x) = \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\mathrm {d} \left[ y ^ {\prime} (x) \right]}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {\frac {2 t \left(t ^ {2} + 1\right) - 2 t \left(t ^ {2} - 1\right)}{\left(t ^ {2} + 1\right) ^ {2}}}{t ^ {2} + 1} = \frac {4 t}{\left(t ^ {2} + 1\right) ^ {3}}.</equation>由(1)式可知，当<equation>|t| > 1</equation>时，<equation>y^{\prime}(x) > 0</equation>；当<equation>|t| < 1</equation>时，<equation>y^{\prime}(x) < 0</equation>；当<equation>t = \pm 1</equation>时，<equation>y^{\prime}(x) = 0</equation>因此，<equation>y(x)</equation>处处可导且参数<equation>t = \pm 1</equation>所对应的点满足<equation>y^{\prime}(x) = 0. t = 1</equation>对应的点为<equation>\left(\frac{5}{3}, -\frac{1}{3}\right)</equation><equation>t = -1</equation>对应的点为<equation>(-1,1)</equation>.

由于函数<equation>y(x)</equation>二阶可导，故可以通过<equation>y^{\prime \prime}(x)</equation>的符号来讨论<equation>y(x)</equation>的极值.

在点<equation>(-1,1)</equation>处，<equation>y^{\prime \prime}(x) = -\frac{1}{2} < 0</equation>，故<equation>x = -1</equation>为极大值点，对应的极大值为<equation>y(-1) = 1</equation>；在点<equation>\left(\frac{5}{3}, -\frac{1}{3}\right)</equation>处，<equation>y^{\prime \prime}(x) = \frac{1}{2} > 0</equation>，故<equation>x = \frac{5}{3}</equation>为极小值点，对应的极小值为<equation>y\left(\frac{5}{3}\right) = -\frac{1}{3}</equation>.

下面讨论曲线<equation>y=y(x)</equation>的凹凸区间以及拐点.

由（2）式可知，当<equation>t=0</equation>时，<equation>\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}\bigg|_{t=0}=0</equation>；当<equation>t > 0</equation>时，<equation>\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}} > 0</equation>；当<equation>t < 0</equation>时，<equation>\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}} < 0. t=0</equation>对应的点为<equation>\left(\frac{1}{3},\frac{1}{3}\right).</equation><equation>x^{\prime}(t)=t^{2}+1>0,x(t)</equation>是关于 t的单调增加函数.由反函数求导法则知，<equation>t^{\prime}(x)=\frac{1}{x^{\prime}(t)}>0</equation>故<equation>t(x)</equation>也是关于 x的单调增加函数.从而，

- 当<equation>x > \frac{1}{3}</equation>时，<equation>t > 0,y^{\prime \prime}(x) > 0</equation>，曲线<equation>y = y(x)</equation>为凹曲线；

- 当<equation>x < \frac{1}{3}</equation>时，<equation>t < 0,y^{\prime \prime}(x) < 0</equation>，曲线<equation>y=y(x)</equation>为凸曲线.

因此，<equation>y ( x )</equation>的极大值为<equation>y (-1)=1</equation>，极小值为<equation>y \left( {\frac{5}{3}}\right)=-{\frac{1}{3}}.</equation>曲线<equation>y=y ( x )</equation>的凹区间为<equation>\left({\frac{1}{3}},+\infty\right)</equation>，凸区间为<equation>\left(-\infty ,\frac{1}{3}\right)</equation>，拐点为<equation>\left({\frac{1}{3}},\frac{1}{3}\right).</equation>

---

**2010年第10题 | 填空题 | 4分**
10. 曲线<equation>y=\frac{2x^{3}}{x^{2}+1}</equation>的渐近线方程为 ___
**解析: **解 由于函数<equation>y=\frac{2x^{3}}{x^{2}+1}</equation>在<equation>(-\infty, +\infty)</equation>上均有定义且连续，故曲线没有铅直渐近线又由于<equation>\lim_{x\to +\infty}\frac{2x^{3}}{x^{2}+1}=+\infty, \lim_{x\to -\infty}\frac{2x^{3}}{x^{2}+1}=-\infty</equation>，故曲线没有水平渐近线考虑曲线的斜渐近线.<equation>\lim _ {\substack {x \rightarrow \infty \\ \binom {x \rightarrow + \infty} {x \rightarrow - \infty}}} \frac {\frac {2 x ^ {3}}{x ^ {2} + 1}}{x} = \lim _ {\substack {x \rightarrow \infty \\ \binom {x \rightarrow + \infty} {x \rightarrow - \infty}}} \frac {2 x ^ {2}}{x ^ {2} + 1} = 2,</equation><equation>\lim _ {\substack {x \rightarrow \infty \\ \left( \begin{array}{c} x \rightarrow + \infty \\ x \rightarrow - \infty \end{array} \right)}} \left(\frac {2 x ^ {3}}{x ^ {2} + 1} - 2 x\right) = \lim _ {\substack {x \rightarrow \infty \\ \left( \begin{array}{c} x \rightarrow + \infty \\ x \rightarrow - \infty \end{array} \right)}} \frac {2 x ^ {3} - 2 x ^ {3} - 2 x}{x ^ {2} + 1} = 0.</equation>因此，<equation>y=2x</equation>为曲线<equation>y=\frac{2x^{3}}{x^{2}+1}</equation>的斜渐近线

---


#### 导数与微分的概念

**2025年第7题 | 选择题 | 5分 | 答案: D**

7. 设函数 f(x) 连续，给出下列四个条件：<equation>\textcircled{1} \lim_{x \to 0} \frac{|f(x)|-f(0)}{x}</equation>存在；<equation>\textcircled{2} \lim_{x \to 0} \frac{f(x)-|f(0)|}{x}</equation>存在；<equation>\textcircled{3} \lim_{x \to 0} \frac{|f(x)|}{x}</equation>存在；<equation>\textcircled{4} \lim_{x \to 0} \frac{|f(x)|-|f(0)|}{x}</equation>存在；

其中能得到“ f(x)在 x=0处可导”的条件个数是（    ）

A.1 B.2 C.3 D.4

答案: D

**解析:**## 解 依次分析四个命题.

对命题<equation>\textcircled{1}</equation>，由<equation>\lim_{x\to 0}\frac{|f(x)| - f(0)}{x}</equation>存在可得<equation>\lim_{x\to 0}[|f(x)| - f(0)] = 0</equation>，即<equation>\lim_{x\to 0}|f(x)| = f(0)</equation>. 另一方面，由<equation>f(x)</equation>连续可得<equation>\lim_{x\to 0}|f(x)| = |f(0)|</equation>. 由此可得<equation>|f(0)| = f(0)</equation>，从而<equation>f(0)\geqslant 0</equation>.

若<equation>f(0) = 0</equation>，则由<equation>\lim_{x\to 0}\frac{|f(x)| - f(0)}{x}</equation>存在可得<equation>\lim_{x\to 0}\frac{|f(x)|}{x}</equation>存在，进一步可得<equation>\lim_{x\to 0}\left|\frac{f(x)}{x}\right|</equation>存在.于是，<equation>\lim _ {x \rightarrow 0 ^ {-}} \frac {\left| f (x) \right|}{x} = - \lim _ {x \rightarrow 0 ^ {-}} \left| \frac {f (x)}{x} \right| = - \lim _ {x \rightarrow 0} \left| \frac {f (x)}{x} \right|,</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {\left| f (x) \right|}{x} = \lim _ {x \rightarrow 0 ^ {+}} \left| \frac {f (x)}{x} \right| = \lim _ {x \rightarrow 0} \left| \frac {f (x)}{x} \right|.</equation>结合<equation>\lim_{x\to 0}\frac{|f(x)|}{x}</equation>存在，从而<equation>\lim_{x\to 0^{-}}\frac{|f(x)|}{x} = \lim_{x\to 0^{+}}\frac{|f(x)|}{x}</equation>可得<equation>-\lim_{x\to 0}\left|\frac{f(x)}{x}\right| = \lim_{x\to 0}\left|\frac{f(x)}{x}\right|</equation>，于是<equation>\lim_{x\to 0}\left|\frac{f(x)}{x}\right| = 0</equation>，进一步可得<equation>\lim_{x\to 0}\frac{f(x)}{x} = 0</equation>，即<equation>\lim_{x\to 0}\frac{f(x) - f(0)}{x - 0} = 0.</equation>由导数的定义可知<equation>f^{\prime}(0) = 0</equation>若<equation>f(0) > 0</equation>，则由<equation>f(x)</equation>连续可得<equation>\lim_{x\to 0}f(x) = f(0) > 0</equation>，再由极限的局部保号性可知，存在<equation>x = 0</equation>的某个去心邻域，<equation>f(x)</equation>在该邻域内恒大于0，<equation>|f(x)| = f(x)</equation>，故由<equation>\lim_{x\to 0}\frac{|f(x)| - f(0)}{x}</equation>存在可得<equation>\lim_{x\to 0}\frac{f(x) - f(0)}{x}</equation>存在.由导数的定义可知<equation>f^{\prime}(0)</equation>存在.

因此，命题<equation>\textcircled{1}</equation>正确.

对命题<equation>\textcircled{2}</equation>，由<equation>\lim_{x\to 0}\frac{f(x) - |f(0)|}{x}</equation>存在可得<equation>\lim_{x\to 0}[f(x) - |f(0)|] = 0</equation>，即<equation>\lim_{x\to 0}f(x) = |f(0)|</equation>.

另一方面，由<equation>f(x)</equation>连续可得<equation>\lim_{x\to 0}f(x) = f(0)</equation>.由此可得<equation>|f(0)| = f(0)</equation>，从而<equation>\lim_{x\to 0}\frac{f(x) - |f(0)|}{x}</equation>存在即<equation>\lim_{x\to 0}\frac{f(x) - f(0)}{x}</equation>存在.由导数的定义可知<equation>f^{\prime}(0)</equation>存在.

因此，命题<equation>\textcircled{2}</equation>正确.

对命题<equation>\textcircled{3}</equation>，由<equation>\lim_{x\to 0}\frac{|f(x)|}{x}</equation>存在可得<equation>\lim_{x\to 0}|f(x)| = 0</equation>，由此可得<equation>|f(0)| = 0</equation>，进一步可得<equation>f(0) = 0</equation>.

同命题<equation>\textcircled{1}</equation>的方法，由<equation>\lim_{x\to 0}\frac{|f(x)|}{x}</equation>存在可得<equation>\lim_{x\to 0}\left|\frac{f(x)}{x}\right|</equation>存在，进一步得到<equation>\lim_{x\to 0}\left|\frac{f(x)}{x}\right| = 0</equation>，从而<equation>\lim_{x\to 0}\frac{f(x)}{x} = 0</equation>。由导数的定义可知<equation>f^{\prime}(0) = 0</equation>.

因此，命题<equation>\textcircled{3}</equation>正确.

对命题<equation>\textcircled{4}</equation>，若<equation>f(0) = 0</equation>，则由<equation>\lim_{x\to 0}\frac{|f(x)| - |f(0)|}{x}</equation>存在可得<equation>\lim_{x\to 0}\frac{|f(x)|}{x}</equation>存在，由命题<equation>\textcircled{3}</equation>正确可得<equation>f^{\prime}(0) = 0</equation>.

若<equation>f(0) > 0</equation>，则由<equation>f(x)</equation>连续可得<equation>\lim_{x\to 0}f(x) = f(0) > 0</equation>，再由极限的局部保号性可知，存在<equation>x = 0</equation>的某个去心邻域，<equation>f(x)</equation>在该邻域内恒大于0，<equation>|f(x)| = f(x)</equation>，故由<equation>\lim_{x\to 0}\frac{|f(x)| - |f(0)|}{x}</equation>存在可得<equation>\lim_{x\to 0}\frac{f(x) - f(0)}{x}</equation>存在. 由导数的定义可知<equation>f^{\prime}(0)</equation>存在.

若<equation>f(0) < 0</equation>，则由<equation>f(x)</equation>连续可得<equation>\lim_{x\to 0}f(x) = f(0) < 0</equation>，再由极限的局部保号性可知，存在<equation>x = 0</equation>的某个去心邻域，<equation>f(x)</equation>在该邻域内恒小于0，<equation>|f(x)| = -f(x)</equation>，故由<equation>\lim_{x\to 0}\frac{|f(x)| - |f(0)|}{x}</equation>存在可得<equation>\lim_{x\to 0}\frac{-f(x) + f(0)}{x}</equation>存在，即<equation>-\lim_{x\to 0}\frac{f(x) - f(0)}{x}</equation>存在.由导数的定义可知<equation>f^{\prime}(0)</equation>存在.

因此，命题<equation>\textcircled{4}</equation>正确.

综上所述，应选D.

---

**2025年第18题 | 解答题 | 12分**

18. (本题满分12分)

设函数 f(x)在 x=0处连续，且<equation>\lim_{x\rightarrow 0}\frac{x f(x)-\mathrm{e}^{2 \sin x}+1}{\ln(1+x)+\ln(1-x)}=-3</equation>，证明 f(x)在 x=0处可导，并求<equation>f^{\prime}(0).</equation>

**答案:**<equation>f^{\prime}(0)=5</equation>

**解析:**对<equation>\mathrm{e}^{2 \sin x}</equation>的处理，可以考虑它的泰勒展开式.

解分别计算<equation>\mathrm{e}^{2\sin x}</equation>在 x=0处的一阶、二阶导数，并写出<equation>\mathrm{e}^{2\sin x}</equation>的带佩亚诺余项的二阶泰勒公式.<equation>\left(\mathrm {e} ^ {2 \sin x}\right) ^ {\prime} = \mathrm {e} ^ {2 \sin x} \cdot 2 \cos x,</equation><equation>\left(\mathrm {e} ^ {2 \sin x}\right) ^ {\prime \prime} = 2 \left(\mathrm {e} ^ {2 \sin x} \cdot \cos x\right) ^ {\prime} = 2 \left(2 \mathrm {e} ^ {2 \sin x} \cos^ {2} x - \mathrm {e} ^ {2 \sin x} \sin x\right).</equation>于是，<equation>(\mathrm{e}^{2\sin x})^{\prime}\bigg|_{x = 0} = 2,(\mathrm{e}^{2\sin x})^{\prime \prime}\bigg|_{x = 0} = 4.</equation>结合<equation>\mathrm{e}^{2\sin x}\bigg|_{x = 0} = 1</equation>可得，<equation>\mathrm {e} ^ {2 \sin x} = 1 + 2 x + \frac {4 x ^ {2}}{2} + o \left(x ^ {2}\right) = 1 + 2 x + 2 x ^ {2} + o \left(x ^ {2}\right).</equation>将（1）式代人已知极限可得，<equation>\begin{aligned} - 3 &= \lim _ {x \rightarrow 0} \frac {x f (x) - \mathrm {e} ^ {2 \sin x} + 1}{\ln (1 + x) + \ln (1 - x)} = \lim _ {x \rightarrow 0} \frac {x f (x) - 2 x - 2 x ^ {2} + o \left(x ^ {2}\right)}{\ln \left(1 - x ^ {2}\right)} \\ \frac {\ln \left(1 - x ^ {2}\right) - - x ^ {2}}{- x ^ {2}} \lim _ {x \rightarrow 0} \frac {x f (x) - 2 x - 2 x ^ {2} + o \left(x ^ {2}\right)}{- x ^ {2}} &= \lim _ {x \rightarrow 0} \frac {f (x) - 2}{- x} + 2. \end{aligned}</equation>由此可得，<equation>\lim_{x\to 0}\frac{f(x) - 2}{-x} = -5</equation>，即<equation>\lim_{x\to 0}\frac{f(x) - 2}{x} = 5.</equation>由于<equation>\lim_{x\to 0}x=0</equation>，故<equation>\lim_{x\to 0}[f(x)-2]=0</equation>，从而<equation>\lim_{x\to 0}f(x)=2</equation>.结合 f(x)在 x=0处连续可得 f(0)<equation>= \lim_{x\to 0}f(x)=2.</equation>进一步可得<equation>5 = \lim _ {x \rightarrow 0} \frac {f (x) - 2}{x} = \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0}.</equation>根据导数的定义，<equation>f ( x )</equation>在<equation>x=0</equation>处可导，且<equation>f^{\prime}(0)=5.</equation>

---

**2024年第2题 | 选择题 | 5分 | 答案: B**

2. 设函数 y=f(x)由参数方程<equation>\left\{\begin{array}{l l}x=1+t^{3}\\ y=\mathrm{e}^{t^{2}}\end{array}\right.</equation>确定，则<equation>\lim_{x\rightarrow+\infty}x\left[ f\left( 2+\frac{2}{x}\right)-f(2)\right] =</equation>(    )

A. 2e B.<equation>\frac{4\mathrm{e}}{3}</equation>C.<equation>\frac{2\mathrm{e}}{3}</equation>D.<equation>\frac{\mathrm{e}}{3}</equation>

答案: B

**解析:**<equation>\lim _ {x \rightarrow + \infty} x \left[ f \left(2 + \frac {2}{x}\right) - f (2) \right] = 2 \lim _ {x \rightarrow + \infty} \frac {f \left(2 + \frac {2}{x}\right) - f (2)}{2 + \frac {2}{x} - 2} = 2 f _ {+} ^ {\prime} (2) = 2 f ^ {\prime} (2).</equation>下面用两种方法计算<equation>f^{\prime}(2)</equation>.

（法一）根据由参数方程确定的函数的求导公式，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y / \mathrm {d} t}{\mathrm {d} x / \mathrm {d} t} = \frac {2 t \mathrm {e} ^ {t ^ {2}}}{3 t ^ {2}} = \frac {2 \mathrm {e} ^ {t ^ {2}}}{3 t}.</equation>解<equation>1 + t^{3} = 2</equation>可得，<equation>t = 1</equation>，故<equation>f^{\prime}(2) = \frac{2\mathrm{e}^{t^2}}{3t}\bigg|_{t = 1} = \frac{2\mathrm{e}}{3}</equation>.

（法二）由<equation>x = 1 + t^{3}</equation>解得<equation>t = \sqrt[3]{x - 1}</equation>，故<equation>y = \mathrm{e}^{t^2} = \mathrm{e}^{(x - 1)^{2/3}}</equation>。于是，<equation>f ^ {\prime} (2) = \left[ \mathrm {e} ^ {(x - 1) ^ {2 / 3}} \right] ^ {\prime} \Big | _ {x = 2} = \mathrm {e} ^ {(x - 1) ^ {2 / 3}} \cdot \frac {2}{3} (x - 1) ^ {- \frac {1}{3}} \Big | _ {x = 2} = \frac {2 \mathrm {e}}{3}.</equation>因此，<equation>\lim_{x\to +\infty}x\left[ f\left( 2 + \frac{2}{x}\right) - f(2)\right] = 2f^{\prime}(2) = \frac{4\mathrm{e}}{3}</equation>，应选B.

---

**2023年第5题 | 选择题 | 5分 | 答案: C**

5. 设函数 y=f(x)由<equation>\left\{\begin{array}{l l}x=2 t+|t|\\y=|t|\sin t\end{array}\right.</equation>确定，则（    )

A. f(x)连续，<equation>f^{\prime}(0)</equation>不存在 B.<equation>f^{\prime}(0)</equation>存在，<equation>f^{\prime}(x)</equation>在 x=0处不连续

C.<equation>f^{\prime}(x)</equation>连续，<equation>f^{\prime\prime}(0)</equation>不存在 D.<equation>f^{\prime\prime}(0)</equation>存在，<equation>f^{\prime\prime}(x)</equation>在 x=0处不连续

答案: C

**解析:**解 由于<equation>x=2 t+|t|=\left\{\begin{array}{ll}3 t,&t\geqslant 0,\\ t,&t<0\end{array}\right.</equation>在<equation>(-\infty ,+\infty)</equation>上单调增加，且值域为<equation>(-\infty ,+\infty)</equation>，

故其存在反函数<equation>t=\left\{\begin{array}{ll}\frac{x}{3},&x\geqslant 0,\\ x,&x<0.\end{array}\right.</equation>当<equation>x\geqslant 0</equation>时，<equation>t\geqslant 0</equation>；当<equation>x<0</equation>时，<equation>t<0</equation>．于是，<equation>f(x)=</equation>由其表达式可知，<equation>f(x)</equation>在<equation>x\neq0</equation>处连续．又由于<equation>\lim_{x\to 0}f(x)=0=f(0)</equation>，故<equation>f(x)</equation>在<equation>x=0</equation>处亦连续．因此<equation>f(x)</equation>连续.

计算可得<equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {f (x) - f (0)}{x - 0} \xlongequal {f (0) = 0} \lim _ {x \rightarrow 0 ^ {-}} \frac {- x \sin x}{x} = 0,</equation><equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x - 0} \xlongequal {f (0) = 0} \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {x}{3} \sin \frac {x}{3}}{x} = 0.</equation>f(x)在 x=0处的左、右导数均存在且相等，故<equation>f^{\prime}(0)</equation>存在，且<equation>f^{\prime}(0)=0.</equation>选项A不正确.

当 x < 0时，<equation>f ^ {\prime} (x) = \left(- x \sin x\right) ^ {\prime} = - \sin x - x \cos x.</equation>当 x > 0时，<equation>f ^ {\prime} (x) = \left(\frac {x}{3} \sin \frac {x}{3}\right) ^ {\prime} = \frac {1}{3} \left(\sin \frac {x}{3} + \frac {x}{3} \cos \frac {x}{3}\right).</equation>由此可知<equation>f^{\prime}(x)</equation>在<equation>x\neq0</equation>处连续.又由于<equation>\lim_{x\to0^{-}}f^{\prime}(x)=\lim_{x\to0^{+}}f^{\prime}(x)=0=f^{\prime}(0)</equation>，故<equation>f^{\prime}(x)</equation>在<equation>x=0</equation>处亦连续.因此<equation>f^{\prime}(x)</equation>连续.选项B不正确.

进一步计算可得，<equation>\begin{aligned} f _ {-} ^ {\prime \prime} (0) &= \lim _ {x \rightarrow 0 ^ {-}} \frac {f ^ {\prime} (x) - f ^ {\prime} (0)}{x - 0} \xlongequal {f ^ {\prime} (0) = 0} \lim _ {x \rightarrow 0 ^ {-}} \frac {- \sin x - x \cos x}{x} \\ &= - \lim _ {x \rightarrow 0 ^ {-}} \left(\frac {\sin x}{x} + \cos x\right) = - (1 + 1) = - 2, \end{aligned}</equation><equation>\begin{aligned} f _ {+} ^ {\prime \prime} (0) &= \lim _ {x \rightarrow 0 ^ {+}} \frac {f ^ {\prime} (x) - f ^ {\prime} (0)}{x - 0} \xlongequal {f ^ {\prime} (0) = 0} \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {1}{3} \left(\sin \frac {x}{3} + \frac {x}{3} \cos \frac {x}{3}\right)}{x} \\ &= \frac {1}{3} \lim _ {x \rightarrow 0 ^ {+}} \left(\frac {1}{3} \cdot \frac {\sin \frac {x}{3}}{\frac {x}{3}} + \frac {1}{3} \cos \frac {x}{3}\right) = \frac {1}{3} \times \left(\frac {1}{3} + \frac {1}{3}\right) = \frac {2}{9}. \end{aligned}</equation>由于<equation>f_{-}^{\prime \prime}(0)\neq f_{+}^{\prime \prime}(0)</equation>，故<equation>f^{\prime \prime}(0)</equation>不存在.选项C正确，选项D不正确.

综上所述，应选C.

---

**2022年第17题 | 解答题 | 10分**

17. (本题满分10分）

已知函数 f(x)在 x=1处可导，且<equation>\lim_{x\rightarrow 0}\frac{f(\mathrm{e}^{x^{2}})-3f(1+\sin^{2}x)}{x^{2}}=2</equation>，求<equation>f^{\prime}(1).</equation>

**答案:**```latex

-1.
```
**解析: **解 由 f(x)在 x=1处可导可得 f(x)在 x=1处连续，故由<equation>\lim_{x\rightarrow 0}\frac{f(\mathrm{e}^{x^{2}})-3f(1+\sin^{2}x)}{x^{2}}=2</equation>可得<equation>\lim _ {x \rightarrow 0} \left[ f \left(\mathrm {e} ^ {x ^ {2}}\right)-3 f \left(1+\sin^ {2} x\right)\right] \xlongequal {f \text {连 续}}-2 f (1)=0.</equation>于是，<equation>f(1)=0.</equation>另一方面，<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {f \left(\mathrm {e} ^ {x ^ {2}}\right)}{x ^ {2}} &= \lim _ {x \rightarrow 0} \left[ \frac {f \left(\mathrm {e} ^ {x ^ {2}}\right)-f (1)}{\mathrm {e} ^ {x ^ {2}}-1} \cdot \frac {\mathrm {e} ^ {x ^ {2}}-1}{x ^ {2}} \right] = \lim _ {x \rightarrow 0} \frac {f \left(\mathrm {e} ^ {x ^ {2}}\right)-f (1)}{\mathrm {e} ^ {x ^ {2}}-1} \cdot \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x ^ {2}}-1}{x ^ {2}} \\ &= f ^ {\prime} (1), \end{aligned}</equation><equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {f \left(1 + \sin^ {2} x\right)}{x ^ {2}} &= \lim _ {x \rightarrow 0} \left[ \frac {f \left(1 + \sin^ {2} x\right) - f (1)}{\left(\sin^ {2} x + 1\right) - 1} \cdot \frac {\sin^ {2} x}{x ^ {2}} \right] = \lim _ {x \rightarrow 0} \frac {f \left(1 + \sin^ {2} x\right) - f (1)}{\left(\sin^ {2} x + 1\right) - 1} \cdot \lim _ {x \rightarrow 0} \frac {\sin^ {2} x}{x ^ {2}} \\ &= f ^ {\prime} (1). \end{aligned}</equation>因此，<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {f \left(\mathrm {e} ^ {x ^ {2}}\right)-3 f \left(1+\sin^ {2} x\right)}{x ^ {2}} &= \lim _ {x \rightarrow 0} \frac {f \left(\mathrm {e} ^ {x ^ {2}}\right)}{x ^ {2}}-3 \lim _ {x \rightarrow 0} \frac {f \left(1+\sin^ {2} x\right)}{x ^ {2}}= f ^ {\prime} (1)-3 f ^ {\prime} (1) \\ &= - 2 f ^ {\prime} (1) = 2. \end{aligned}</equation>综上所述，<equation>f^{\prime}(1)=-1.</equation>

---

**2021年第2题 | 选择题 | 5分 | 答案: D**
2. 函数 f(x) =<equation>\left\{\begin{array}{l l}{\frac{\mathrm{e}^{x}-1}{x},}&{x\neq0}\\ {1,}&{x=0}\end{array} \right.</equation>在 x=0处（    ）

A. 连续且取得极大值 B. 连续且取得极小值 C. 可导且导数为零 D. 可导且导数不为零
答案: D
**解析: **解 首先考虑 f(x)在 x=0处的连续性.<equation>\lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x} - 1}{x} \xlongequal {\mathrm {e} ^ {x} - 1 \sim x} \lim _ {x \rightarrow 0} \frac {x}{x} = 1 = f (0).</equation>于是，f（x）在 x=0处连续.

下面考虑 f(x)在 x=0处的可导性.<equation>f ^ {\prime} (0) = \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0} \frac {\frac {\mathrm {e} ^ {x} - 1}{x} - 1}{x} = \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x} - 1 - x}{x ^ {2}} \frac {\mathrm {e} ^ {x} = 1 + x + \frac {x ^ {2}}{2} + o \left(x ^ {2}\right)}{\frac {1}{2} \neq 0}.</equation>于是，<equation>f ( x )</equation>在<equation>x=0</equation>处可导且导数不为0.

因此，应选D.

下面说明选项A、B不正确.

由于<equation>f^{\prime}(0)\neq 0</equation>，故 x=0不满足成为极值点的必要条件，从而选项A、B均不正确.

---

**2018年第2题 | 选择题 | 4分 | 答案: D**
2. 下列函数中，在 x=0处不可导的是（    ）

A. f(x) = |x|<equation>\sin|x|</equation>B. f(x) = |x|<equation>\sin\sqrt{|x|}</equation>C. f(x) =<equation>\cos|x|</equation>D. f(x) =<equation>\cos\sqrt{|x|}</equation>
答案: D
**解析: **解 考虑选项 D.<equation>f (x) = \left\{ \begin{array}{l l} \cos \sqrt {x}, & x \geqslant 0, \\ \cos \sqrt {- x}, & x < 0. \end{array} \right.</equation><equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {\cos \sqrt {- x} - 1}{x - 0} \frac {\cos \sqrt {- x} - 1 \sim - \frac {\left(\sqrt {- x}\right) ^ {2}}{2}}{\lim _ {x \rightarrow 0 ^ {-}} \frac {x}{x}} = \frac {1}{2},</equation><equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {\cos \sqrt {x} - 1}{x - 0} \frac {\cos \sqrt {x} - 1 \sim - \frac {(\sqrt {x}) ^ {2}}{2}}{\lim _ {x \rightarrow 0 ^ {+}} \frac {- \frac {x}{2}}{x}} = - \frac {1}{2}.</equation>由于<equation>f_{-}^{\prime}(0)\neq f_{+}^{\prime}(0)</equation>，故<equation>f(x)=\cos \sqrt{|x|}</equation>在 x=0处不可导.应选D.

下面分别说明选项A、B、C不正确.

选项A：<equation>f ( x )=\left\{\begin{array}{l l}x \sin x,\\-x \sin(-x),\end{array}\right.</equation><equation>x \geqslant0</equation>又因为<equation>-x \sin(-x)=-x\cdot(-\sin x)=x \sin x</equation>，所以<equation>x<0.</equation><equation>f ( x )=x \sin x,f ( x )</equation>在 x=0处可导.

选项B：<equation>f ( x )=\left\{\begin{array}{ll}x\sin \sqrt{x},&x\geqslant 0,\\ -x\sin \sqrt{-x},&x<0.\end{array} \right.</equation><equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {- x \sin \sqrt {- x} - 0}{x - 0} = \lim _ {x \rightarrow 0 ^ {-}} (- \sin \sqrt {- x}) = 0,</equation><equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {x \sin \sqrt {x} - 0}{x - 0} = \lim _ {x \rightarrow 0 ^ {+}} \sin \sqrt {x} = 0.</equation>由于<equation>f_{-}^{\prime}(0)=f_{+}^{\prime}(0)</equation>，故<equation>f(x)=|x|\sin \sqrt{|x|}</equation>在 x=0处可导.

选项C：<equation>f ( x )=\left\{\begin{array}{ll}\cos x,&x\geqslant0,\\ \cos(-x),&x<0.\end{array} \right.</equation>又因为<equation>\cos(-x)=\cos x</equation>，所以<equation>f ( x )=\cos x,f ( x )</equation>在 x=0处可导.

---

**2015年第3题 | 选择题 | 4分 | 答案: A**
3. 设函数 f(x) =<equation>\left\{\begin{array}{l l}{x^{\alpha}\cos \frac{1}{x^{\beta}},}&{x>0,\\0,&x\leqslant 0}\end{array} \right.</equation>（<equation>\alpha>0,\beta>0</equation>）. 若 f'(x)在 x=0处连续，则（    )

A.<equation>\alpha-\beta>1</equation>B. 0 <<equation>\alpha-\beta\leqslant1</equation>C.<equation>\alpha-\beta>2</equation>D. 0 <<equation>\alpha-\beta\leqslant2</equation>
答案: A
**解析: **解 首先求<equation>f^{\prime}(0).</equation>根据导数的定义，<equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {f (x) - f (0)}{x - 0} = 0, \quad f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0 ^ {+}} \left(x ^ {\alpha - 1} \cos \frac {1}{x ^ {\beta}}\right).</equation>由于<equation>f^{\prime}(x)</equation>在<equation>x=0</equation>处连续，故<equation>f^{\prime}(0)</equation>存在，从而<equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \left(x ^ {\alpha - 1} \cos \frac {1}{x ^ {\beta}}\right) = 0 = f _ {-} ^ {\prime} (0).</equation>由于当<equation>\beta > 0</equation>时，<equation>\cos \frac{1}{x^{\beta}}</equation>有界但<equation>\lim_{x\to 0^{+}}\cos \frac{1}{x^{\beta}}</equation>不存在，故<equation>\lim_{x\to 0^{+}}\left(x^{\alpha -1}\cos \frac{1}{x^{\beta}}\right)=0</equation>当且仅当<equation>\alpha >1.</equation>由上可知，当<equation>\alpha >1</equation>时，<equation>f^{\prime}(0)=0.</equation>还需要再检查<equation>\lim_{x\to 0}f^{\prime}(x)=f^{\prime}(0)=0</equation>成立的条件.

当<equation>x \leqslant 0</equation>时，<equation>f(x)\equiv 0</equation>，故当<equation>x < 0</equation>时，<equation>f^{\prime}(x)\equiv 0</equation>，从而<equation>\lim_{x\to 0^{-}}f^{\prime}(x) = 0.</equation>当 x > 0时，<equation>f ^ {\prime} (x) = \alpha x ^ {\alpha - 1} \cos \frac {1}{x ^ {\beta}} + x ^ {\alpha} \left(- \sin \frac {1}{x ^ {\beta}}\right) (- \beta) \frac {1}{x ^ {\beta + 1}} = \alpha x ^ {\alpha - 1} \cos \frac {1}{x ^ {\beta}} + \beta x ^ {\alpha - \beta - 1} \sin \frac {1}{x ^ {\beta}}.</equation>由于<equation>\alpha >1</equation>，故<equation>\lim _ {x \rightarrow 0 ^ {+}} \left(\alpha x ^ {\alpha - 1} \cos \frac {1}{x ^ {\beta}} + \beta x ^ {\alpha - \beta - 1} \sin \frac {1}{x ^ {\beta}}\right) = \lim _ {x \rightarrow 0 ^ {+}} \left(\beta x ^ {\alpha - \beta - 1} \sin \frac {1}{x ^ {\beta}}\right).</equation>由于当<equation>\beta > 0</equation>时，<equation>\sin \frac{1}{x^{\beta}}</equation>有界但<equation>\lim_{x\to 0^{+}}\sin \frac{1}{x^{\beta}}</equation>不存在，故<equation>\lim_{x\to 0^{+}}\left(\beta x^{\alpha -\beta -1}\sin \frac{1}{x^{\beta}}\right)=0</equation>当且仅当<equation>\alpha -\beta -1 > 0</equation>即<equation>\alpha -\beta >1.</equation>联立<equation>\left\{ \begin{array}{l l} \alpha >1, \\ \alpha -\beta -1 > 0, \\ \alpha >0,\beta >0, \end{array} \right.</equation>可得<equation>\alpha -\beta -1 > 0.</equation>应选A.

---

**2013年第2题 | 选择题 | 4分 | 答案: A**
2. 设函数 y=f(x)由方程<equation>\cos(xy)+\ln y-x=1</equation>确定，则<equation>\lim_{n\rightarrow \infty}n\left[ f\left( \frac{2}{n}\right)-1\right] =</equation>(    )

A.2 B.1 C.-1 D.-2
答案: A
**解析: **解 将<equation>x = 0</equation>代入方程<equation>\cos (xy) + \ln y - x = 1</equation>可得，<equation>f(0) = 1.</equation>对方程<equation>\cos ( x y )+\ln y-x=1</equation>两端关于 x求导可得<equation>- \sin (x y) \cdot \left(y + x y ^ {\prime}\right) + \frac {y ^ {\prime}}{y} - 1 = 0.</equation>代入<equation>x = 0,f(0) = 1</equation>，可得<equation>f^{\prime}(0) = 1.</equation>由导数的定义可得，<equation>\lim _ {n \rightarrow \infty} n \left[ f \left(\frac {2}{n}\right)-1 \right] = 2 \lim _ {n \rightarrow \infty} \frac {f \left(\frac {2}{n}\right)-1}{\frac {2}{n}} = 2 \lim _ {n \rightarrow \infty} \frac {f \left(\frac {2}{n}\right)-f (0)}{\frac {2}{n}-0} = 2 f ^ {\prime} (0) = 2.</equation>应选A.

---

**2011年第2题 | 选择题 | 4分 | 答案: B**
2. 设函数 f(x)在 x=0处可导，且 f(0)=0，则<equation>\lim_{x\rightarrow 0}\frac{x^{2}f(x)-2f\left(x^{3}\right)}{x^{3}}=</equation>(    )

A.<equation>-2f^{\prime}(0)</equation>B.<equation>-f^{\prime}(0)</equation>C.<equation>f^{\prime}(0)</equation>D. 0
答案: B
**解析: **解 （法一）利用导数的定义来求极限.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {x ^ {2} f (x) - 2 f \left(x ^ {3}\right)}{x ^ {3}} &= \lim _ {x \rightarrow 0} \left[ \frac {f (x)}{x} - \frac {2 f \left(x ^ {3}\right)}{x ^ {3}} \right] \xlongequal {f (0) = 0} \lim _ {x \rightarrow 0} \left[ \frac {f (x) - f (0)}{x - 0} - 2 \cdot \frac {f \left(x ^ {3}\right) - f (0)}{x ^ {3} - 0} \right] \\ &= \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0} - 2 \lim _ {x \rightarrow 0} \frac {f \left(x ^ {3}\right) - f (0)}{x ^ {3} - 0} = f ^ {\prime} (0) - 2 f ^ {\prime} (0) = - f ^ {\prime} (0). \end{aligned}</equation>应选B.

（法二）分别写出<equation>f(x)</equation>与<equation>f(x^{3})</equation>在<equation>x=0</equation>处的一阶泰勒公式.<equation>f (x) = f (0) + f ^ {\prime} (0) x + o (x) \stackrel {f (0) = 0} {=} f ^ {\prime} (0) x + o (x),</equation><equation>f \left(x ^ {3}\right) = f (0) + f ^ {\prime} (0) x ^ {3} + o \left(x ^ {3}\right) \stackrel {f (0) = 0} {=} f ^ {\prime} (0) x ^ {3} + o \left(x ^ {3}\right).</equation>代入所求极限得<equation>\lim _ {x \rightarrow 0} \frac {x ^ {2} f (x) - 2 f \left(x ^ {3}\right)}{x ^ {3}} = \lim _ {x \rightarrow 0} \frac {f ^ {\prime} (0) x ^ {3} - 2 f ^ {\prime} (0) x ^ {3} + o \left(x ^ {3}\right)}{x ^ {3}} = - f ^ {\prime} (0).</equation>应选B.

---


#### 导数与微分的计算

**2025年第14题 | 填空题 | 5分**
14. 已知函数 y=y(x)由<equation>\left\{\begin{array}{l l}x=\ln(1+2t)\\ 2t-\int_{1}^{y+t^{2}}\mathrm{e}^{-u^{2}}\mathrm{d}u=0\end{array}\right.</equation>确定，则<equation>\left.\frac{\mathrm{d} y}{\mathrm{d} x}\right|_{t=0}=</equation>___
**解析: **解 对<equation>x = \ln (1 + 2t)</equation>关于<equation>t</equation>求导可得<equation>\frac{\mathrm{d}x}{\mathrm{d}t} = \frac{2}{1 + 2t}</equation>，于是<equation>\frac{\mathrm{d}x}{\mathrm{d}t}\bigg|_{t = 0} = \frac{2}{1 + 2t}\bigg|_{t = 0} = 2</equation>.

在<equation>2t - \int_{1}^{y + t^2}\mathrm{e}^{-u^2}\mathrm{d}u = 0</equation>中令<equation>t = 0</equation>，可得<equation>\int_{1}^{y}\mathrm{e}^{-u^2}\mathrm{d}u = 0</equation>. 由于<equation>\mathrm{e}^{-u^2} > 0</equation>，故<equation>\int_{1}^{y}\mathrm{e}^{-u^2}\mathrm{d}u = 0</equation>当且仅当<equation>y = 1</equation>，从而<equation>y(t)\big|_{t = 0} = 1</equation>.

对<equation>2t - \int_{1}^{y + t^2}\mathrm{e}^{-u^2}\mathrm{d}u = 0</equation>两端关于<equation>t</equation>求导可得<equation>2 - \mathrm{e}^{-(y + t^2)^2}\left(\frac{\mathrm{d}y}{\mathrm{d}t} + 2t\right) = 0. \tag{1}</equation>在(1)式中令<equation>t = 0</equation>可得<equation>2 - \mathrm{e}^{-1}\frac{\mathrm{d}y}{\mathrm{d}t}\bigg|_{t = 0} = 0</equation>，解得<equation>\frac{\mathrm{d}y}{\mathrm{d}t}\bigg|_{t = 0} = 2\mathrm{e}</equation>.

因此，<equation>\frac{\mathrm{d}y}{\mathrm{d}x}\bigg|_{t = 0} = \frac{2\mathrm{e}}{2} = \mathrm{e}</equation>.

---

**2024年第14题 | 填空题 | 5分**
14. 已知函数<equation>f(x)=x^{2}\left(\mathrm{e}^{x}+1\right)</equation>, 则<equation>f^{(5)}(1)=</equation>___.
**答案: **## 31e
**解析: **解记<equation>u ( x )=\mathrm{e}^{x}+1, v ( x )=x^{2}</equation>，则当 k≥1时，<equation>u^{(k)}(x)=\mathrm{e}^{x}, v^{\prime}(x)=2 x, v^{\prime \prime}(x)=2</equation>，当 k≥ 3时，<equation>v^{(k)}(x)=0</equation>.由莱布尼茨公式可得，<equation>f^{(5)}(x)=\mathrm{C}_{5}^{0} u^{(5)}(x) v(x)+\mathrm{C}_{5}^{1} u^{(4)}(x) v^{\prime}(x)+\mathrm{C}_{5}^{2} u^{(3)}(x) v^{\prime \prime}(x)</equation><equation>=\mathrm{e}^{x}\cdot x^{2}+5\cdot\mathrm{e}^{x}\cdot 2 x+1 0\cdot\mathrm{e}^{x}\cdot 2=(x^{2}+1 0 x+2 0)\mathrm{e}^{x}.</equation>当 x=1时，<equation>f^{(5)}(1)=\left[ \left(x^{2}+1 0 x+2 0\right) \mathrm{e}^{x}\right] \bigg|_{x=1}=3 1 \mathrm{e}.</equation>

---

**2022年第12题 | 填空题 | 5分**
12. 已知函数<equation>y=y(x)</equation>由方程<equation>x^{2}+xy+y^{3}=3</equation>确定，则<equation>y^{\prime\prime}(1)=</equation>___
**答案: **# -<equation>\frac{31}{32}.</equation>
**解析: **解 将 x=1代入原方程可得，<equation>1+y+y^{3}=3</equation>，即<equation>y^{3}+y-2=0</equation>. 通过观察可得 y=1是该方程的一个解. 令<equation>f(y)=y^{3}+y-2</equation>，则<equation>f^{\prime}(y)=3y^{2}+1>0</equation>，f(y)为单调增加函数，从而 y=1为<equation>y^{3}+y-2=0</equation>的唯一解.

对<equation>x^{2}+ x y+ y^{3}=3</equation>两端关于 x求导可得，<equation>2 x + y + x y ^ {\prime} + 3 y ^ {2} y ^ {\prime} = 0, \quad \mathrm {即} 2 x + y + \left(x + 3 y ^ {2}\right) y ^ {\prime} = 0.</equation>代入 x=1,y（1）=1可得<equation>3+4 y^{\prime}(1)=0</equation>.解得<equation>y^{\prime}(1)=-\frac{3}{4}.</equation>对（1）式两端再次关于 x求导可得，<equation>2 + y ^ {\prime} + \left(1 + 6 y y ^ {\prime}\right) y ^ {\prime} + \left(x + 3 y ^ {2}\right) y ^ {\prime \prime} = 0.</equation>代入<equation>x=1,y(1)=1,y^{\prime}(1)=-\frac{3}{4}</equation>可得<equation>\frac{31}{8}+4y^{\prime \prime}(1)=0.</equation>解得<equation>y^{\prime \prime}(1)=-\frac{31}{32}.</equation>

---

**2021年第12题 | 填空题 | 5分**
12. 设函数<equation>y=y(x)</equation>由参数方程<equation>\left\{ \begin{array}{l} x = 2 \mathrm {e} ^ {t} + t + 1 \\ y = 4 (t - 1) \mathrm {e} ^ {t} + t ^ {2} \end{array} \right.</equation>确定，则<equation>\left.\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}\right|_{t=0}=</equation>___
**解析: **解 根据由参数方程确定的函数的导数计算公式，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {4 \mathrm {e} ^ {t} + 4 (t - 1) \mathrm {e} ^ {t} + 2 t}{2 \mathrm {e} ^ {t} + 1} = \frac {4 t \mathrm {e} ^ {t} + 2 t}{2 \mathrm {e} ^ {t} + 1} = 2 t.</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\mathrm {d} \left(\frac {\mathrm {d} y}{\mathrm {d} x}\right)}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {2}{2 \mathrm {e} ^ {t} + 1}.</equation>代入<equation>t = 0</equation>，可得<equation>\frac{\mathrm{d}^2y}{\mathrm{d}x^2}\bigg|_{t = 0} = \frac{2}{3}</equation>.

---

**2020年第4题 | 选择题 | 4分 | 答案: A**
4. 已知函数<equation>f ( x )=x^{2} \ln(1-x)</equation>，当<equation>n\geqslant 3</equation>时，<equation>f^{(n)}(0)=</equation>（    ）

A.<equation>-\frac{n!}{n-2}</equation>B.<equation>\frac{n!}{n-2}</equation>C.<equation>-\frac{(n-2)!}{n}</equation>D.<equation>\frac{(n-2)!}{n}</equation>
答案: A
**解析: **解（法一）记<equation>u ( x )=\ln( 1-x)</equation><equation>v ( x )=x^{2}</equation>，则<equation>f ( x )=u ( x ) v ( x )</equation>，从而可以用莱布尼茨公式来计算 f(x)的高阶导数.

由于<equation>f ^ {(n)} (0) = (u v) ^ {(n)} (0) = \sum_ {k = 0} ^ {n} C _ {n} ^ {k} u ^ {(n - k)} (0) v ^ {(k)} (0),</equation>而<equation>v^{\prime \prime}(0)=2,v^{(k)}(0)=0(k\neq 2)</equation>，故<equation>f ^ {(n)} (0) = 2 \mathrm {C} _ {n} ^ {2} \left[ \ln (1 - x) \right] ^ {(n - 2)} (0) = n (n - 1) \left[ \ln (1 - x) \right] ^ {(n - 2)} (0).</equation>下面利用逐次求导的方法计算<equation>\ln(1-x)</equation>在 x=0处的的 n-2阶导数.<equation>[ \ln (1 - x) ] ^ {\prime} = - \frac {1}{1 - x} = (- 1) \cdot (1 - x) ^ {- 1},</equation><equation>[ \ln (1 - x) ] ^ {\prime \prime} = (- 1) ^ {2} \cdot (- 1) \cdot (1 - x) ^ {- 2},</equation><equation>[ \ln (1 - x) ] ^ {(3)} = (- 1) ^ {3} \cdot (- 1) \cdot (- 2) \cdot (1 - x) ^ {- 3},</equation>由数学归纳法可知，<equation>[\ln(1 - x)]^{(n)} = (-1)^{n}\cdot(-1)^{n - 1}(n - 1)!(1 - x)^{-n} = -(n - 1)!(1 - x)^{-n}.</equation>于是，<equation>[\ln(1 - x)]^{(n - 2)} = -(n - 3)!(1 - x)^{-(n - 2)}.</equation>令<equation>x=0</equation>，可得<equation>[\ln(1-x)]^{(n-2)}(0)=-(n-3)!</equation>代入（1）式可得，<equation>f ^ {(n)} (0) = n (n - 1) \cdot [ - (n - 3)! ] = - \frac {n !}{n - 2}.</equation>因此，应选A.

（法二）由于<equation>\ln(1-x)</equation>的麦克劳林级数为<equation>-\sum_{n=1}^{\infty}\frac{x^{n}}{n}</equation>，故<equation>x^{2}\ln(1-x)</equation>的麦克劳林级数为<equation>-\sum_{n=1}^{\infty}\frac{x^{n+2}}{n}.x^{n}</equation>的系数为<equation>-\frac{1}{n-2}.</equation>又因为 f(x)的麦克劳林级数中，<equation>x^{n}</equation>的系数为<equation>\frac{f^{(n)}(0)}{n!}</equation>所以<equation>\frac{f^{(n)}(0)}{n!}=-\frac{1}{n-2}, f^{(n)}(0)=-\frac{n!}{n-2}.</equation>因此，应选A.

---

**2020年第9题 | 填空题 | 4分**
9.<equation>\left\{ \begin{array}{l l} x = \sqrt {t ^ {2} + 1} \\ y = \ln (t + \sqrt {t ^ {2} + 1}) \end{array} \right. \quad \mathrm {则} \left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {t = 1} = \underline {{\quad}}</equation>
**解析: **解 根据由参数方程确定的函数的求导公式，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {1 + \frac {t}{\sqrt {t ^ {2} + 1}}}{t + \sqrt {t ^ {2} + 1}} / \frac {t}{\sqrt {t ^ {2} + 1}} = \frac {1}{\sqrt {t ^ {2} + 1}} / \frac {t}{\sqrt {t ^ {2} + 1}} = \frac {1}{t}.</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\mathrm {d} \left(\frac {\mathrm {d} y}{\mathrm {d} x}\right)}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = - \frac {1}{t ^ {2}} / \frac {t}{\sqrt {t ^ {2} + 1}} = - \frac {\sqrt {t ^ {2} + 1}}{t ^ {3}}.</equation>代入 t=1，可得<equation>\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}} \Bigg|_{t=1}=-\sqrt{2}.</equation>

---

**2017年第10题 | 填空题 | 4分**
10. 设函数 y=y(x)由参数方程<equation>\left\{ \begin{array}{l} x = t + \mathrm {e} ^ {t} \\ y = \sin t \end{array} \right.</equation><equation>\left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {t = 0} = \underline {{}}</equation>
**答案: **# -<equation>\frac{1}{8}.</equation>
**解析: **解 根据由参数方程确定的函数的求导公式，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {\cos t}{1 + \mathrm {e} ^ {t}},</equation><equation>\begin{aligned} \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} &= \frac {\mathrm {d} \left[ y ^ {\prime} (x) \right]}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {\frac {\mathrm {d} \left(\frac {\cos t}{1 + \mathrm {e} ^ {t}}\right)}{\mathrm {d} t}}{1 + \mathrm {e} ^ {t}} = \frac {\frac {- \sin t \left(1 + \mathrm {e} ^ {t}\right) - \cos t \mathrm {e} ^ {t}}{\left(1 + \mathrm {e} ^ {t}\right) ^ {2}}}{1 + \mathrm {e} ^ {t}} \\ &= \frac {- \sin t \left(1 + \mathrm {e} ^ {t}\right) - \cos t \mathrm {e} ^ {t}}{\left(1 + \mathrm {e} ^ {t}\right) ^ {3}}. \end{aligned}</equation>当<equation>t = 0</equation>时，<equation>\frac{\mathrm{d}^2y}{\mathrm{d}x^2}\bigg|_{t = 0} = -\frac{1}{8}.</equation>或者也可以这样计算<equation>\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}</equation>由于<equation>x^{\prime}(t) = 1 + \mathrm{e}^{t}, x^{\prime \prime}(t) = \mathrm{e}^{t}, y^{\prime}(t) = \cos t, y^{\prime \prime}(t) = -\sin t</equation>，故<equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {y ^ {\prime \prime} (t) x ^ {\prime} (t) - y ^ {\prime} (t) x ^ {\prime \prime} (t)}{\left[ x ^ {\prime} (t) \right] ^ {3}} = \frac {- \sin t \left(1 + \mathrm {e} ^ {t}\right) - \cos t \mathrm {e} ^ {t}}{\left(1 + \mathrm {e} ^ {t}\right) ^ {3}}.</equation>

---

**2016年第12题 | 填空题 | 4分**
12. 已知函数 f(x)在<equation>(-\infty,+\infty)</equation>上连续，且<equation>f(x)=(x+1)^{2}+2\int_{0}^{x} f(t)\mathrm{d}t</equation>，则当 n≥2时，<equation>f^{(n)}(0)=</equation>___
**答案: **5·2<equation>^{n-1}</equation>
**解析: **解 （法一）逐次求导.

虽然条件中仅给出了 f(x)的连续性，但由<equation>f ( x )=( x+1 )^{2}+2 \int_{0}^{x} f ( t ) \mathrm{d} t</equation>知，f(x）可导.由于<equation>f^{\prime}(x)=2(x+1)+2 f(x)</equation>，故<equation>f^{\prime}(x)</equation>也可导，从而可推出 f(x)为 n阶可导函数（n为任意正整数）.<equation>\begin{aligned} f ^ {\prime} (x) &= 2 (x + 1) + 2 f (x), \\ f ^ {\prime \prime} (x) &= 2 + 2 f ^ {\prime} (x), \\ f ^ {(3)} (x) &= 2 f ^ {\prime \prime} (x), \\ f ^ {(4)} (x) &= \left[ f ^ {(3)} (x) \right] ^ {\prime} = \left[ 2 f ^ {\prime \prime} (x) \right] ^ {\prime} = 2 f ^ {(3)} (x) = 2 ^ {2} f ^ {\prime \prime} (x), \\ \dots \\ \mathrm {即} f ^ {(n)} (x) &= 2 ^ {n - 2} f ^ {\prime \prime} (x), n \geqslant 2. \end{aligned}</equation>由数学归纳法可知<equation>f^{(n)}(x)=2^{n-2} f^{\prime \prime}(x), n\geqslant 2.</equation>当 x=0时，<equation>f(0)=1,f^{\prime}(0)=2+2f(0)=4,f^{\prime\prime}(0)=2+2\times 4=10.</equation>因此，<equation>f^{(n)}(0) = 2^{n - 2}\cdot 10 = 5\cdot 2^{n - 1}, n\geqslant 2.</equation>（法二）先求出<equation>f(x)</equation>的表达式，再计算其导数.

当 x=0时，由已知等式易求得<equation>f(0)=1.</equation>对已知等式两端关于 x求导，得<equation>f^{\prime}(x)=2(x+1)+2 f(x)</equation>，即<equation>f^{\prime}(x)-2 f(x)=2(x+1).</equation>这是一个一阶非齐次线性微分方程.

由求解公式，得<equation>\begin{aligned} f (x) &= C \mathrm {e} ^ {\int 2 \mathrm {d} x} + \mathrm {e} ^ {\int 2 \mathrm {d} x} \int \mathrm {e} ^ {\int (- 2) \mathrm {d} x} \cdot 2 (x + 1) \mathrm {d} x = C \mathrm {e} ^ {2 x} + \mathrm {e} ^ {2 x} \int \mathrm {e} ^ {- 2 x} \cdot 2 (x + 1) \mathrm {d} x \\ &= C \mathrm {e} ^ {2 x} - x - \frac {3}{2}. \end{aligned}</equation>代入<equation>f ( 0 )=1</equation>得，<equation>C=\frac{5}{2}.</equation>因此，<equation>f ( x )=\frac{5}{2}\mathrm{e}^{2 x}-x-\frac{3}{2}.</equation>对<equation>f ( x )</equation>逐次求导，可得<equation>f^{(n)}(x)=\frac{5}{2}\cdot 2^{n}\cdot \mathrm{e}^{2x},</equation><equation>n\geqslant 2.</equation>代入<equation>x = 0</equation>，得<equation>f^{(n)}(0) = 5\cdot 2^{n - 1}, n\geqslant 2.</equation>

---

**2015年第9题 | 填空题 | 4分**
9. 设<equation>\begin{aligned} x &= \arctan t \\ y &= 3 t + t ^ {3} \end{aligned}</equation><equation>\text {则} \left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {t = 1} = \underline {{}}</equation>
**答案: **## 48.
**解析: **解 根据由参数方程确定的函数的求导公式，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {3 t ^ {2} + 3}{\frac {1}{t ^ {2} + 1}} = 3 \left(t ^ {2} + 1\right) ^ {2},</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\mathrm {d} \left[ y ^ {\prime} (x) \right]}{\mathrm {d} t} \Bigg / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {6 \left(t ^ {2} + 1\right) \cdot 2 t}{\frac {1}{t ^ {2} + 1}} = 1 2 t \left(t ^ {2} + 1\right) ^ {2}.</equation>代入<equation>t = 1</equation>，得<equation>\frac{\mathrm{d}^2y}{\mathrm{d}x^2}\bigg|_{t = 1} = 12\times 4 = 48.</equation>

---

**2015年第10题 | 填空题 | 4分**
10. 函数<equation>f(x) = x^2 2^x</equation>在<equation>x = 0</equation>处的<equation>n</equation>阶导数<equation>f^{(n)}(0) =</equation>___
**答案: **n(n-1)<equation>(\ln 2)^{n-2}.</equation>
**解析: **解记<equation>u ( x )=2^{x},</equation><equation>v ( x )=x^{2}</equation>，则<equation>f ( x )=u ( x ) v ( x )</equation>，从而可以用莱布尼茨公式来计算<equation>f ( x )</equation>的高阶导数.

由于<equation>f ^ {(n)} (0) = (u v) ^ {(n)} (0) = \sum_ {k = 0} ^ {n} \mathrm {C} _ {n} ^ {k} u ^ {(n - k)} (0) v ^ {(k)} (0)</equation>而<equation>v^{\prime \prime}(0) = 2,v^{(k)}(0) = 0(k\neq 2)</equation>，故<equation>f ^ {(n)} (0) = 2 \mathrm {C} _ {n} ^ {2} \left(2 ^ {x}\right) ^ {(n - 2)} (0) = n (n - 1) (\ln 2) ^ {n - 2}.</equation>

---

**2013年第10题 | 填空题 | 4分**
10. 设函数<equation>f ( x )=\int_{-1}^{x}\sqrt{1-\mathrm{e}^{t}}\mathrm{d} t</equation>，则 y=f(x)的反函数<equation>x=f^{-1} ( y )</equation>在 y=0处的导数<equation>\left.\frac{\mathrm{d} x}{\mathrm{d} y}\right|_{y=0}=</equation>___
**解析: **解 因为<equation>f ( x )=\int_{-1}^{x}\sqrt{1-\mathrm{e}^{t}}\mathrm{d} t</equation>，而被积函数<equation>\sqrt{1-\mathrm{e}^{t}}\geqslant 0</equation>，所以当且仅当<equation>x=-1</equation>时，<equation>y = f (x) = \int_ {- 1} ^ {x} \sqrt {1 - \mathrm {e} ^ {t}} \mathrm {d} t = 0,</equation>即<equation>f^{-1}(0)=-1.</equation>由于<equation>f^{\prime}(-1)=\sqrt{1-\mathrm{e}^{x}} \Bigg|_{x=-1}=\sqrt{1-\frac{1}{\mathrm{e}}}</equation>，故<equation>\left[ f ^ {- 1} (y) \right] ^ {\prime} \Big | _ {y = 0} = \frac {1}{f ^ {\prime} (- 1)} = \frac {1}{\sqrt {1 - \frac {1}{e}}} = \sqrt {\frac {e}{e - 1}}.</equation>

---

**2012年第2题 | 选择题 | 4分 | 答案: A**
2. 设函数<equation>f(x)=\mathrm{e}^{x}-1)(\mathrm{e}^{2x}-2)\cdots(\mathrm{e}^{nx}-n)</equation>，其中 n为正整数，则<equation>f^{\prime}(0)=</equation>(    )

A.<equation>(-1)^{n-1}(n-1)!</equation>B.<equation>(-1)^{n}(n-1)!</equation>C.<equation>(-1)^{n-1}n!</equation>D.<equation>(-1)^{n}n!</equation>
答案: A
**解析: **解（法一）利用求导的乘法法则来计算<equation>f^{\prime}(0)</equation>.

令<equation>g ( x ) = \left( \mathrm{e}^{2 x}-2 \right) \dots \left( \mathrm{e}^{n x}-n \right)</equation>，则<equation>f ( x ) = \left( \mathrm{e}^{x}-1 \right) g ( x )</equation>.由求导的乘法法则可得，<equation>f ^ {\prime} (x) = \mathrm {e} ^ {x} g (x) + \left(\mathrm {e} ^ {x} - 1\right) g ^ {\prime} (x).</equation>由于<equation>\mathrm{e}^{0}-1=0</equation>，故<equation>f ^ {\prime} (0) = \mathrm {e} ^ {0} g (0) = (- 1) (- 2) \dots [ - (n - 1) ] = (- 1) ^ {n - 1} (n - 1)!</equation>因此，应选A.

（法二）从导数的定义出发来计算<equation>f^{\prime}(0)</equation>.

由于 f（0）=0，故<equation>\begin{aligned} f ^ {\prime} (0) &= \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0} \frac {f (x)}{x} = \lim _ {x \rightarrow 0} \frac {\left(\mathrm {e} ^ {x} - 1\right)\left(\mathrm {e} ^ {2 x} - 2\right) \dots \left(\mathrm {e} ^ {n x} - n\right)}{x} \\ \underline {{\mathrm {e} ^ {x} - 1 \sim x}} \lim _ {x \rightarrow 0} \left[ \left(\mathrm {e} ^ {2 x} - 2\right) \dots \left(\mathrm {e} ^ {n x} - n\right)\right] \cdot 1 &= (- 1) (- 2) \dots [ - (n - 1) ] \cdot 1 \\ &= (- 1) ^ {n - 1} (n - 1)!. \end{aligned}</equation>因此，应选A.

（法三）排除法.

我们可以尝试代入 n值，排除不符合题意的选项.由于当 n=2时，四个选项的取值均不同，故可选择 n=2.

当<equation>n = 2</equation>时，<equation>f(x) = \left(\mathrm{e}^{x} - 1\right)\left(\mathrm{e}^{2x} - 2\right), f^{\prime}(0) = -1</equation>，故可排除选项B、C、D.

因此，应选A.

---

**2012年第9题 | 填空题 | 4分**
9. 设 y=y(x) 是由方程<equation>x^{2}-y+1=\mathrm{e}^{y}</equation>所确定的隐函数，则<equation>\left.\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\right|_{x=0}=</equation>___
**解析: **<equation>x^{2}-y+1=\mathrm{e}^{y}</equation>可得，<equation>y(0)=0.</equation>对原方程两端关于 x 求导，可得<equation>2 x-y^{\prime}=\mathrm{e}^{y} y^{\prime}</equation>代入<equation>x=0,y(0)=0</equation>，可得<equation>-y^{\prime}(0)=y^{\prime}(0)</equation>即<equation>y^{\prime}(0)=0.</equation>对<equation>2 x-y^{\prime}=\mathrm{e}^{y} y^{\prime}</equation>两端关于 x求导，可得<equation>2-y^{\prime \prime}=\mathrm{e}^{y}\left(y^{\prime}\right)^{2}+\mathrm{e}^{y} y^{\prime \prime}.</equation>代入<equation>x=0,y(0)=0</equation><equation>y^{\prime}(0)=0</equation>，得<equation>2-y^{\prime \prime}(0)=y^{\prime \prime}(0).</equation>因此，<equation>y^{\prime \prime}(0) = 1.</equation>

---

**2010年第11题 | 填空题 | 4分**
11. 函数<equation>y = \ln(1 - 2x)</equation>在<equation>x = 0</equation>处的<equation>n</equation>阶导数<equation>y^{(n)}(0) =</equation>___
**答案: **- 2<equation>^{n}</equation>(n-1) !.
**解析: **解 利用链式法则对 y逐次求各阶导数，可得<equation>y ^ {\prime} = \frac {- 2}{1 - 2 x} = - 2 \left(1 - 2 x\right) ^ {- 1},</equation><equation>y ^ {\prime \prime} = (- 2) ^ {2} (- 1) (1 - 2 x) ^ {- 2}.</equation>由数学归纳法，可证明<equation>\begin{aligned} y ^ {(n)} &= (- 2) ^ {n} (- 1) (- 2) \dots [ - (n - 1) ] (1 - 2 x) ^ {- n} \\ &= - 2 ^ {n} (n - 1)! (1 - 2 x) ^ {- n}. \end{aligned}</equation>当<equation>x = 0</equation>时，<equation>y^{(n)}(0) = -2^{n}(n - 1)!.</equation>

---

**2009年第12题 | 填空题 | 4分**
12. 设 y=y(x) 是由方程<equation>x y+\mathrm{e}^{y}=x+1</equation>确定的隐函数，则<equation>\left.\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\right|_{x=0}=</equation>___
**解析: **由<equation>xy + \mathrm{e}^{y} = x + 1</equation>知，当<equation>x = 0</equation>时，<equation>y = 0</equation>，即<equation>y(0) = 0.</equation>对原方程两端关于 x求导，得<equation>y + x y ^ {\prime} + \mathrm {e} ^ {y} y ^ {\prime} = 1.</equation>代入<equation>x = 0, y(0) = 0</equation>得，<equation>y^{\prime}(0) = 1.</equation>继续对（1）式两端关于 x求导，得<equation>y ^ {\prime} + x y ^ {\prime \prime} + y ^ {\prime} + \mathrm {e} ^ {y} \left(y ^ {\prime}\right) ^ {2} + \mathrm {e} ^ {y} y ^ {\prime \prime} = 0.</equation>代入<equation>x = 0, y(0) = 0, y^{\prime}(0) = 1</equation>得，<equation>y^{\prime \prime}(0) = -3.</equation>

---


#### 微分中值定理

**2025年第21题 | 解答题 | 12分**
21. (本题满分12分）

设函数 f(x)在区间（a,b）内可导，证明导函数<equation>f^{\prime}(x)</equation>在（a,b）内严格单调增加的充分必要条件是：对（a,b）内任意的<equation>x_{1},x_{2},x_{3}</equation>，当<equation>x_{1}<x_{2}<x_{3}</equation>时，有<equation>\frac{f(x_{2})-f(x_{1})}{x_{2}-x_{1}}<\frac{f(x_{3})-f(x_{2})}{x_{3}-x_{2}}.</equation>
**解析: **证 先证明必要性.

对<equation>(a,b)</equation>内任意的<equation>x_{1}, x_{2}, x_{3}</equation>，当<equation>x_{1} < x_{2} < x_{3}</equation>时，由拉格朗日中值定理可得存在<equation>\xi_{1}\in (x_{1}, x_{2})</equation><equation>\xi_{2}\in (x_{2}, x_{3})</equation>，使得<equation>f^{\prime}(\xi_{1}) = \frac{f(x_{2}) - f(x_{1})}{x_{2} - x_{1}}</equation><equation>f^{\prime}(\xi_{2}) = \frac{f(x_{3}) - f(x_{2})}{x_{3} - x_{2}}</equation>.由<equation>f^{\prime}(x)</equation>单调增加以及<equation>\xi_{1} <</equation><equation>\xi_{2}</equation>可得<equation>f^{\prime}(\xi_{1}) < f^{\prime}(\xi_{2})</equation>，即<equation>\frac{f(x_{2}) - f(x_{1})}{x_{2} - x_{1}} < \frac{f(x_{3}) - f(x_{2})}{x_{3} - x_{2}}.</equation>再证明充分性.

任取<equation>x_{0}, x_{1}, x_{2}\in(a,b)</equation>满足<equation>x_{1} < x_{0} < x_{2}</equation>，由已知条件可得<equation>\frac{f(x_0) - f(x_1)}{x_0 - x_1} < \frac{f(x_2) - f(x_0)}{x_2 - x_0}.</equation>取s,t满足<equation>x_{1} < s < x_{0} < t < x_{2}</equation>，由已知条件可得<equation>\frac {f (s) - f \left(x _ {1}\right)}{s - x _ {1}} < \frac {f \left(x _ {0}\right) - f (s)}{x _ {0} - s}, \quad \frac {f (t) - f \left(x _ {0}\right)}{t - x _ {0}} < \frac {f \left(x _ {2}\right) - f (t)}{x _ {2} - t}.</equation>在<equation>\frac{f(s)-f(x_{1})}{s-x_{1}}<\frac{f(x_{0})-f(s)}{x_{0}-s}</equation>中令 s<equation>\rightarrow x_{1}^{+}</equation>可得<equation>f ^ {\prime} \left(x _ {1}\right) = f _ {*} ^ {\prime} \left(x _ {1}\right) = \lim _ {s \rightarrow x _ {1}} \frac {f (s) - f \left(x _ {1}\right)}{s - x _ {1}} \leqslant \lim _ {s \rightarrow x _ {1}} \frac {f \left(x _ {0}\right) - f (s)}{x _ {0} - s} = \frac {f \left(x _ {0}\right) - f \left(x _ {1}\right)}{x _ {0} - x _ {1}}.</equation>在<equation>\frac{f(t)-f(x_{0})}{t-x_{0}}<\frac{f(x_{2})-f(t)}{x_{2}-t}</equation>中令<equation>t\to x_{2}^{-}</equation>可得<equation>\frac {f \left(x _ {2}\right) - f \left(x _ {0}\right)}{x _ {2} - x _ {0}} = \lim _ {t \rightarrow x _ {2}} \frac {f (t) - f \left(x _ {0}\right)}{t - x _ {0}} \leqslant \lim _ {t \rightarrow x _ {2}} \frac {f \left(x _ {2}\right) - f (t)}{x _ {2} - t} = f _ {-} ^ {\prime} \left(x _ {2}\right) = f ^ {\prime} \left(x _ {2}\right).</equation>由(1)式，(2)式以及<equation>\frac{f(x_{0})-f(x_{1})}{x_{0}-x_{1}}<\frac{f(x_{2})-f(x_{0})}{x_{2}-x_{0}}</equation>可得<equation>f^{\prime}(x_{1})<f^{\prime}(x_{2}).</equation>由<equation>x_{1},x_{2}</equation>的任意性可得<equation>f^{\prime}(x)</equation>在（a,b）内严格单调增加.

---

**2024年第21题 | 解答题 | 12分**
21. (本题满分12分)

设函数 f(x)具有二阶导数，且<equation>f^{\prime}(0)=f^{\prime}(1),\left| f^{\prime\prime}(x)\right| \leqslant 1</equation>，证明：

I. 当 x<equation>\in(0,1)</equation>时，<equation>|f(x)-f(0)(1-x)-f(1)x|\leqslant \frac{x(1-x)}{2}</equation>；

II.<equation>\left|\int_{0}^{1} f(x)\mathrm{d}x-\frac{f(0)+f(1)}{2}\right|\leqslant \frac{1}{12}.</equation>
**解析: **证（I）（法一）分别写出<equation>f ( x )</equation>在<equation>x=0</equation>与<equation>x=1</equation>处的一阶泰勒公式.<equation>f (x) = f (0) + f ^ {\prime} (0) x + \frac {f ^ {\prime \prime} \left(\xi_ {1}\right) x ^ {2}}{2},</equation><equation>f (x) = f (1) + f ^ {\prime} (1) (x - 1) + \frac {f ^ {\prime \prime} \left(\xi_ {2}\right) \left(x - 1\right) ^ {2}}{2},</equation>其中<equation>\xi_{1}</equation>介于0与<equation>x</equation>之间，<equation>\xi_{2}</equation>介于1与<equation>x</equation>之间.

(2) 式<equation>\times x-（1）</equation>式<equation>\times (x-1)</equation>，并结合<equation>f^{\prime}(0)=f^{\prime}(1)</equation>可得<equation>f (x) = f (0) (1 - x) + f (1) x + \frac {x (x - 1)}{2} \left[ f ^ {\prime \prime} \left(\xi_ {2}\right) (x - 1) - f ^ {\prime \prime} \left(\xi_ {1}\right) x \right].</equation>由（3）式可得，当<equation>x\in (0,1)</equation>时，<equation>\left| f (x) - f (0) (1 - x) - f (1) x \right| = \frac {x (1 - x)}{2} \left| f ^ {\prime \prime} \left(\xi_ {2}\right) (x - 1) - f ^ {\prime \prime} \left(\xi_ {1}\right) x \right|.</equation>由于<equation>|f^{\prime \prime}(\xi_{2})(x - 1) - f^{\prime \prime}(\xi_{1})x| \leqslant |f^{\prime \prime}(\xi_{2})|(1 - x) + |f^{\prime \prime}(\xi_{1})|x,</equation>故结合<equation>|f^{\prime \prime}(x)| \leqslant 1</equation>以及（4）式可得<equation>\left| f (x) - f (0) (1 - x) - f (1) x \right| \leqslant \frac {x (1 - x)}{2} \cdot [ (1 - x) + x ] = \frac {x (1 - x)}{2}.</equation>（法二）所证命题等价于当<equation>x\in (0,1)</equation>时，<equation>- \frac {x (1 - x)}{2} \leqslant f (x) - f (0) (1 - x) - f (1) x \leqslant \frac {x (1 - x)}{2}.</equation>令<equation>F ( x ) = f ( x ) - f ( 0 ) ( 1 - x ) - f ( 1 ) x - \frac { x ( 1 - x ) } { 2 }</equation>，则<equation>F ( 0 ) = F ( 1 ) = 0</equation>，且<equation>F^{\prime \prime}(x)=f^{\prime \prime}(x)</equation>+1.由于<equation>| f^{\prime \prime}(x) | \leqslant 1</equation>，故<equation>F^{\prime \prime}(x) \geqslant 0.</equation>下面证明当<equation>x\in (0,1)</equation>时，<equation>F(x)\leqslant 0.</equation>若存在<equation>c\in (0,1)</equation>，使得<equation>F(c) > 0</equation>，则分别对<equation>[0,c],[c,1]</equation>上的<equation>F(x)</equation>使用拉格朗日中值定理可得，存在<equation>\xi_{1}\in (0,c),\xi_{2}\in (c,1)</equation>，使得<equation>F ^ {\prime} \left(\xi_ {1}\right) = \frac {F (c) - F (0)}{c - 0} > 0, \quad F ^ {\prime} \left(\xi_ {2}\right) = \frac {F (1) - F (c)}{1 - c} < 0.</equation>再对<equation>[\xi_{1},\xi_{2} ]</equation>上的<equation>F^{\prime}(x)</equation>使用拉格朗日中值定理可得，存在<equation>\xi\in(\xi_{1},\xi_{2})</equation>，使得<equation>F ^ {\prime \prime} (\xi) = \frac {F ^ {\prime} \left(\xi_ {2}\right) - F ^ {\prime} \left(\xi_ {1}\right)}{\xi_ {2} - \xi_ {1}} < 0.</equation>这与<equation>F^{\prime \prime}(x)\geqslant0</equation>矛盾.

因此，当<equation>x\in (0,1)</equation>时，<equation>F(x)\leqslant 0</equation>，即<equation>f(x) - f(0)(1 - x) - f(1)x\leqslant \frac{x(1 - x)}{2}.</equation>令<equation>G ( x )=f ( x )-f ( 0 ) ( 1-x )-f ( 1 ) x+\frac{x(1-x)}{2}</equation>，同理可得<equation>G^{\prime \prime}(x)\leqslant0</equation>，且进一步可得当<equation>x\in</equation>（0,1）时，<equation>G ( x )\geqslant0</equation>，即<equation>f ( x )-f ( 0 ) ( 1-x )-f ( 1 ) x\geqslant-\frac{x(1-x)}{2}.</equation>综上所述，所证命题成立.

（Ⅱ）由第（Ⅰ）问可得<equation>\left| f (x) - f (0) (1 - x) - f (1) x \right| \leqslant \frac {x (1 - x)}{2}.</equation>对（5）式两端从0到1积分可得，<equation>\begin{aligned} \int_ {0} ^ {1} | f (x) - f (0) (1 - x) - f (1) x | \mathrm {d} x \leqslant \int_ {0} ^ {1} \frac {x (1 - x)}{2} \mathrm {d} x &= \frac {1}{2} \int_ {0} ^ {1} \left(x - x ^ {2}\right) \mathrm {d} x \\ &= \frac {1}{2} \left(\frac {x ^ {2}}{2} - \frac {x ^ {3}}{3}\right) \Big | _ {0} ^ {1} = \frac {1}{1 2}. \end{aligned}</equation><equation>\begin{array}{l} \left| \int_ {0} ^ {1} f (x) \mathrm {d} x - f (0) \int_ {0} ^ {1} (1 - x) \mathrm {d} x - f (1) \int_ {0} ^ {1} x \mathrm {d} x \right| = \left| \int_ {0} ^ {1} f (x) \mathrm {d} x - \frac {f (0) + f (1)}{2} \right| \\ \leqslant \int_ {0} ^ {1} | f (x) - f (0) (1 - x) - f (1) x | \mathrm {d} x \leqslant \frac {1}{1 2}. \\ \end{array}</equation>

---

**2023年第21题 | 解答题 | 12分**
21. (本题满分12分)

设函数 f(x)在<equation>[-a,a]</equation>上具有二阶连续导数，证明：

I. 若 f(0)=0，则存在<equation>\xi\in(-a,a)</equation>，使得<equation>f^{\prime\prime}(\xi)=\frac{1}{a^{2}}[f(a)+f(-a)].

II. 若 f(x)在</equation>(-a,a)<equation>内取得极值，则存在</equation>\eta\in(-a,a)<equation>使得</equation>|f^{\prime\prime}(\eta)|\geqslant\frac{1}{2a^{2}}|f(a)-f(-a)|.
**答案: **# （I）证明略；

（Ⅱ）证明略.
**解析: **证（I）由 f(x）的泰勒公式可得<equation>f (a) = f (0) + f ^ {\prime} (0) a + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {1}\right) a ^ {2} \xlongequal {f (0) = 0} f ^ {\prime} (0) a + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {1}\right) a ^ {2},</equation><equation>f (- a) = f (0) + f ^ {\prime} (0) \cdot (- a) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {2}\right) a ^ {2} \stackrel {f (0) = 0} {=} f ^ {\prime} (0) \cdot (- a) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {2}\right) a ^ {2},</equation>其中<equation>\xi_{1}\in(0,a),\xi_{2}\in(-a,0).</equation>两式相加可得<equation>f (a) + f (- a) = \frac {a ^ {2}}{2} \left[ f ^ {\prime \prime} \left(\xi_ {1}\right) + f ^ {\prime \prime} \left(\xi_ {2}\right) \right].</equation>记<equation>\max \left\{f^{\prime \prime}\left(\xi_{1}\right),f^{\prime \prime}\left(\xi_{2}\right)\right\}=M</equation>，<equation>\min \left\{f^{\prime \prime}\left(\xi_{1}\right),f^{\prime \prime}\left(\xi_{2}\right)\right\}=m</equation>，则由（1）式可得<equation>m \leqslant \frac {f (a) + f (- a)}{a ^ {2}} = \frac {1}{2} \left[ f ^ {\prime \prime} \left(\xi_ {1}\right) + f ^ {\prime \prime} \left(\xi_ {2}\right) \right] \leqslant M.</equation>由于 f(x)在<equation>[-a,a]</equation>上有二阶连续导数，故由连续函数的介值定理可知，存在<equation>\xi \in[ \xi_{2},\xi_{1} ]\subset(-a,a)</equation>，使得<equation>f^{\prime \prime}(\xi)=\frac{1}{a^{2}}[f(a)+f(-a)]</equation>（Ⅱ）设 f(x)在<equation>(-a,a)</equation>内的极值点为<equation>x_{0}</equation>，则<equation>f^{\prime}(x_{0})=0.</equation>由 f(x)的泰勒公式可得<equation>\begin{aligned} f (a) &= f \left(x _ {0}\right) + f ^ {\prime} \left(x _ {0}\right) \left(a - x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {1}\right) \left(a - x _ {0}\right) ^ {2} \\ \frac {f ^ {\prime} \left(x _ {0}\right) = 0}{\overline {{}}} f \left(x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {1}\right) \left(a - x _ {0}\right) ^ {2}, \end{aligned}</equation><equation>\begin{aligned} f (- a) &= f \left(x _ {0}\right) + f ^ {\prime} \left(x _ {0}\right) \left(- a - x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {2}\right) \left(- a - x _ {0}\right) ^ {2} \\ \frac {f ^ {\prime} \left(x _ {0}\right) = 0}{\overline {{}}} f \left(x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {2}\right) \left(a + x _ {0}\right) ^ {2}, \end{aligned}</equation>其中<equation>\eta_{1}\in(x_{0},a),\eta_{2}\in(-a,x_{0}).</equation>两式相减可得<equation>f (a) - f (- a) = \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {1}\right) \left(a - x _ {0}\right) ^ {2} - \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {2}\right) \left(a + x _ {0}\right) ^ {2}.</equation>记<equation>\max \left\{ \left| f^{\prime \prime}\left(\eta_{1}\right)\right|, \left| f^{\prime \prime}\left(\eta_{2}\right)\right| \right\}=M</equation>，则由（2）式可得<equation>\left| f (a) - f (- a) \right| \leqslant \frac {M}{2} \left[ \left(a - x _ {0}\right) ^ {2} + \left(a + x _ {0}\right) ^ {2} \right] = \frac {M}{2} \left(2 a ^ {2} + 2 x _ {0} ^ {2}\right) \leqslant \frac {M}{2} \cdot 4 a ^ {2} = 2 a ^ {2} M.</equation>因此，<equation>M\geqslant \frac{1}{2a^{2}}|f(a)-f(-a)|.</equation>取<equation>\eta\in\{\eta_{1},\eta_{2}\}</equation>使得<equation>|f^{\prime \prime}(\eta)|=M</equation>，则<equation>\eta\in(-a,a)</equation>满足<equation>|f^{\prime \prime}(\eta)|\geqslant\frac{1}{2a^{2}}|f(a)-f(-a)|.</equation>

---

**2022年第21题 | 解答题 | 12分**
21. (本题满分12分)

设函数 f(x)在<equation>(-\infty, +\infty)</equation>上有二阶连续导数，证明：<equation>f^{\prime \prime}(x)\geqslant0</equation>的充分必要条件是对任意不同的实数 a,b，都有<equation>f\left(\frac{a+b}{2}\right)\leqslant\frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x</equation>成立.
**解析: **证 先证明必要性，即证明，若<equation>f^{\prime \prime}(x)\geqslant 0</equation>，则对不同的实数a,b，<equation>f\left(\frac{a+b}{2}\right)\leqslant \frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x.</equation>（法一）不妨设 b > a. 在区间<equation>[a,b]</equation>上，使用 f(x)在点<equation>\frac{a+b}{2}</equation>处的二阶泰勒公式.<equation>f (x) = f \left(\frac {a + b}{2}\right) + f ^ {\prime} \left(\frac {a + b}{2}\right) \left(x - \frac {a + b}{2}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a + b}{2}\right) ^ {2},</equation>其中<equation>\xi_{x}</equation>介于x与<equation>\frac{a+b}{2}</equation>之间.

将（1）式代入<equation>\int_{a}^{b} f(x)\mathrm{d}x</equation>，可得<equation>\begin{aligned} \int_ {a} ^ {b} f (x) \mathrm {d} x &= \int_ {a} ^ {b} \left[ f \left(\frac {a + b}{2}\right) + f ^ {\prime} \left(\frac {a + b}{2}\right) \left(x - \frac {a + b}{2}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a + b}{2}\right) ^ {2} \right] \mathrm {d} x \\ &= f \left(\frac {a + b}{2}\right) (b - a) + f ^ {\prime} \left(\frac {a + b}{2}\right) \int_ {a} ^ {b} \left(x - \frac {a + b}{2}\right) \mathrm {d} x \\ + \frac {1}{2} \int_ {a} ^ {b} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a + b}{2}\right) ^ {2} \mathrm {d} x. \end{aligned}</equation>注意到<equation>\int_ {a} ^ {b} \left(x - \frac {a + b}{2}\right) \mathrm {d} x = \frac {x ^ {2}}{2} \Bigg | _ {a} ^ {b} - \frac {(a + b) (b - a)}{2} = \frac {b ^ {2} - a ^ {2}}{2} - \frac {b ^ {2} - a ^ {2}}{2} = 0,</equation>故<equation>\int_ {a} ^ {b} f (x) \mathrm {d} x = f \left(\frac {a + b}{2}\right) (b - a) + \frac {1}{2} \int_ {a} ^ {b} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a + b}{2}\right) ^ {2} \mathrm {d} x.</equation>结合<equation>f^{\prime \prime}(x)\geqslant 0</equation>可得<equation>\int_{a}^{b}f(x)\mathrm{d}x\geqslant f\left(\frac{a+b}{2}\right)(b-a)</equation>，即<equation>f\left(\frac{a+b}{2}\right)\leqslant \frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x.</equation>（法二）不妨设 b > a.<equation>f\left(\frac{a+b}{2}\right)\leqslant \frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x</equation>等价于<equation>f\left(\frac{a+b}{2}\right)(b-a)-\int_{a}^{b}f(x)\mathrm{d}x\leqslant 0.</equation>令<equation>F ( x )=\int_{a}^{x} f ( t ) \mathrm{d} t-f \left( \frac{a+x}{2} \right) ( x-a), x \in[ a, b ],</equation>则<equation>F ( a )=0</equation>，且<equation>\begin{aligned} F ^ {\prime} (x) &= f (x) - f \left(\frac {a + x}{2}\right) - f ^ {\prime} \left(\frac {a + x}{2}\right) \frac {x - a}{2} \frac {\text {拉 格 朗 日}}{\text {中 值 定 理}} f ^ {\prime} \left(\eta_ {x}\right) \frac {x - a}{2} - f ^ {\prime} \left(\frac {a + x}{2}\right) \frac {x - a}{2} \\ &= \left[ f ^ {\prime} \left(\eta_ {x}\right) - f ^ {\prime} \left(\frac {a + x}{2}\right) \right] \frac {x - a}{2}, \end{aligned}</equation>其中<equation>\eta_{x}\in \left(\frac{a + x}{2},x\right)</equation>由于<equation>f^{\prime \prime}(x)\geqslant 0</equation>，故<equation>f^{\prime}(x)</equation>单调不减，从而<equation>f^{\prime}(\eta_{x})\geqslant f^{\prime}\left(\frac{a+x}{2}\right)</equation>即<equation>f^{\prime}(\eta_{x})-f^{\prime}\left(\frac{a+x}{2}\right)\geqslant 0.</equation>于是，对<equation>x\in(a,b),F^{\prime}(x)\geqslant 0,F(x)</equation>在[a,b]上单调不减.

又因为<equation>F ( a )=0</equation>，所以<equation>F ( b )\geqslant F ( a )=0</equation>，即<equation>\int_{a}^{b} f ( x )\mathrm{d} x\geqslant f \left( \frac{a+b}{2} \right) ( b-a).</equation>下面证明充分性，即证明，若对不同的实数 a,b，<equation>f\left(\frac{a+b}{2}\right)\leqslant \frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x</equation>，则<equation>f^{\prime \prime}(x)\geqslant 0.</equation>假设存在<equation>x_{0}</equation>，使得<equation>f^{\prime \prime}(x_{0})<0</equation>，由二阶导数连续可得<equation>\lim_{x\to x_{0}}f^{\prime \prime}(x)=f^{\prime \prime}(x_{0})<0</equation>，结合极限的局部保号性可知，存在<equation>\delta >0</equation>，在区间<equation>(x_{0}-\delta,x_{0}+\delta)</equation>内，均有<equation>f^{\prime \prime}(x)<0</equation>.从而取<equation>[a_{0},b_{0}]\subset(x_{0}-\delta,x_{0}+\delta)</equation>，可得在<equation>[a_{0},b_{0}]</equation>上，均有<equation>f^{\prime \prime}(x)<0.</equation>在区间<equation>[ a_{0}, b_{0} ]</equation>上重复必要性中的做法.<equation>\begin{aligned} \int_ {a _ {0}} ^ {b _ {0}} f (x) \mathrm {d} x &= \int_ {a _ {0}} ^ {b _ {0}} \left[ f \left(\frac {a _ {0} + b _ {0}}{2}\right) + f ^ {\prime} \left(\frac {a _ {0} + b _ {0}}{2}\right) \left(x - \frac {a _ {0} + b _ {0}}{2}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a _ {0} + b _ {0}}{2}\right) ^ {2} \right] \mathrm {d} x \\ &= f \left(\frac {a _ {0} + b _ {0}}{2}\right) \left(b _ {0} - a _ {0}\right) + f ^ {\prime} \left(\frac {a _ {0} + b _ {0}}{2}\right) \int_ {a _ {0}} ^ {b _ {0}} \left(x - \frac {a _ {0} + b _ {0}}{2}\right) \mathrm {d} x \\ + \frac {1}{2} \int_ {a _ {0}} ^ {b _ {0}} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a _ {0} + b _ {0}}{2}\right) ^ {2} \mathrm {d} x, \end{aligned}</equation>其中<equation>\xi_{x}</equation>介于x与<equation>\frac{a_{0}+b_{0}}{2}</equation>之间.

于是，<equation>\int_ {a _ {0}} ^ {b _ {0}} f (x) \mathrm {d} x = f \left(\frac {a _ {0} + b _ {0}}{2}\right) \left(b _ {0} - a _ {0}\right) + \frac {1}{2} \int_ {a _ {0}} ^ {b _ {0}} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a _ {0} + b _ {0}}{2}\right) ^ {2} \mathrm {d} x.</equation>结合<equation>f^{\prime \prime}(x) < 0</equation>可得<equation>\int_{a_{0}}^{b_{0}}f(x)\mathrm{d}x < f\left(\frac{a_{0}+b_{0}}{2}\right)\left(b_{0}-a_{0}\right)</equation>，即<equation>f\left(\frac{a_{0}+b_{0}}{2}\right) > \frac{1}{b_{0}-a_{0}}\int_{a_{0}}^{b_{0}}f(x)\mathrm{d}x.</equation>这与前提矛盾.

因此，假设不正确.<equation>f^{\prime \prime}(x)</equation>在<equation>(-\infty, +\infty)</equation>上恒非负.

（法二）若对不同的实数 a,b，<equation>f\left(\frac{a+b}{2}\right)\leqslant \frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x</equation>，则对任意实数<equation>x_{0}</equation>以及任意<equation>\delta >0,</equation>均有<equation>\int_{x_0 - \delta}^{x_0 + \delta}f(x)\mathrm{d}x - 2\delta f(x_0)\geqslant 0</equation>，从而<equation>\frac{\int_{x_0 - \delta}^{x_0 + \delta}f(x)\mathrm{d}x - 2\delta f(x_0)}{\delta^{3}}\geqslant 0.</equation>而<equation>\begin{array}{l} \lim _ {\delta \rightarrow 0 ^ {+}} \frac {\int_ {x _ {0} - \delta} ^ {x _ {0} + \delta} f (x) \mathrm {d} x - 2 \delta f \left(x _ {0}\right)}{\delta^ {3}} \xlongequal {\text {洛必达}} \lim _ {\delta \rightarrow 0 ^ {+}} \frac {f \left(x _ {0} + \delta\right) + f \left(x _ {0} - \delta\right) - 2 f \left(x _ {0}\right)}{3 \delta^ {2}} \\ \xlongequal {\text {洛必达}} \lim _ {\delta \rightarrow 0 ^ {+}} \frac {f ^ {\prime} \left(x _ {0} + \delta\right) - f ^ {\prime} \left(x _ {0} - \delta\right)}{6 \delta} \\ \xlongequal {\text {洛必达}} \lim _ {\delta \rightarrow 0 ^ {+}} \frac {f ^ {\prime \prime} \left(x _ {0} + \delta\right) + f ^ {\prime \prime} \left(x _ {0} - \delta\right)}{6} \\ \xlongequal {f ^ {\prime \prime} \text {连续}} \frac {1}{3} f ^ {\prime \prime} \left(x _ {0}\right), \\ \end{array}</equation>故由极限的保号性可知，<equation>f^{\prime \prime} \left( x_{0} \right) \geqslant 0.</equation>由<equation>x_0</equation>的任意性可知，对不同的实数<equation>a,b,f\left(\frac{a + b}{2}\right)\leqslant \frac{1}{b - a}\int_{a}^{b}f(x)\mathrm{d}x</equation>是<equation>f^{\prime \prime}(x)\geqslant 0</equation>的充分条件.综上所述，<equation>f^{\prime \prime}(x)\geqslant 0</equation>的充分必要条件是对不同的实数<equation>a,b,f\left(\frac{a + b}{2}\right)\leqslant \frac{1}{b - a}\int_{a}^{b}f(x)\mathrm{d}x.</equation>

---

**2020年第20题 | 解答题 | 11分**
20. (本题满分11分）

设函数<equation>f ( x )=\int_{1}^{x} \mathrm{e}^{t^{2}} \mathrm{d} t.</equation>I. 证明：存在<equation>\xi\in(1,2)</equation>，使得<equation>f(\xi)=(2-\xi)\mathrm{e}^{\xi^{2}}</equation>II. 证明：存在<equation>\eta\in(1,2)</equation>，使得<equation>f(2)=\ln 2\cdot\eta\mathrm{e}^{\eta^{2}}</equation>
**答案: **# （I）证明略；

（Ⅱ）证明略.
**解析: **证 （ I ）注意到<equation>f(1)=0.</equation>（法一）待证等式等价于<equation>f (\xi) + (\xi -2)\mathrm{e}^{\xi^{2}} = 0.</equation>令<equation>F ( x ) = f ( x ) + ( x - 2 ) \mathrm{e}^{x^{2}}</equation>，则<equation>F ( 1 ) = f ( 1 ) - \mathrm{e} = - \mathrm{e} < 0,F(2) = f(2) = \int_{1}^{2}\mathrm{e}^{t^{2}}\mathrm{d}t > 0.</equation>对[1,2]上的<equation>F(x)</equation>使用零点定理可得，存在<equation>\xi\in(1,2)</equation>，使得<equation>F(\xi)=0</equation>即<equation>f(\xi)+(\xi-2)\mathrm{e}^{\xi^{2}}=0</equation>也即<equation>f(\xi)=(2-\xi)\mathrm{e}^{\xi^{2}}.</equation>（法二）由变限积分求导公式可得，<equation>f^{\prime}(x)=\mathrm{e}^{x^{2}}</equation>，故待证等式<equation>f(\xi)=(2-\xi)\mathrm{e}^{\xi^{2}}</equation>等价于<equation>f(\xi)=(2-\xi)f^{\prime}(\xi)</equation>，也等价于<equation>f(\xi)+(\xi-2)f^{\prime}(\xi)=0.</equation>令<equation>F ( x ) = ( x - 2 ) f ( x )</equation>，则<equation>F^{\prime}(x)=f(x)+(x-2)f^{\prime}(x).</equation>由于<equation>F ( 1 )=-f ( 1 )=0,F ( 2 )=0</equation>，故由罗尔定理可知，存在<equation>\xi\in(1,2)</equation>，使得<equation>F^{\prime}(\xi)=0</equation>，即<equation>f(\xi)=(2-\xi)f^{\prime}(\xi)</equation>，也即<equation>f(\xi)=(2-\xi)\mathrm{e}^{\xi^{2}}.</equation>（法三）令<equation>F ( x )=\int_{1}^{x}\left(\int_{1}^{u}\mathrm{e}^{t^{2}}\mathrm{d} t\right)\mathrm{d} u</equation>，则利用变限积分求导公式可得<equation>F^{\prime}(x)=\int_{1}^{x}\mathrm{e}^{t^{2}}\mathrm{d} t=f(x).</equation>F（1）=0.此外，利用交换积分次序，可得<equation>F (x) = \int_ {1} ^ {x} \mathrm {d} u \int_ {1} ^ {u} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = \int_ {1} ^ {x} \mathrm {d} t \int_ {t} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} u = \int_ {1} ^ {x} (x - t) \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = x \int_ {1} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t - \int_ {1} ^ {x} t \mathrm {e} ^ {t ^ {2}} \mathrm {d} t.</equation>于是，<equation>F ( 2 )=\int_{1}^{2} ( 2-t ) \mathrm{e}^{t^{2}} \mathrm{d} t.</equation>令<equation>G ( x ) = F ( x ) - \int_{1}^{x} ( 2 - t ) \mathrm{e}^{t^{2}} \mathrm{d} t</equation>，则<equation>G ( 1 ) = 0.</equation><equation>G (2) = F (2) - \int_ {1} ^ {2} (2 - t) \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = \int_ {1} ^ {2} (2 - t) \mathrm {e} ^ {t ^ {2}} \mathrm {d} t - \int_ {1} ^ {2} (2 - t) \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = 0.</equation>由罗尔定理，存在<equation>\xi\in(1,2)</equation>，使得<equation>G^{\prime}(\xi)=0</equation>，即<equation>G ^ {\prime} (\xi) = F ^ {\prime} (\xi) - (2 - \xi) \mathrm {e} ^ {\xi^ {2}} = f (\xi) - (2 - \xi) \mathrm {e} ^ {\xi^ {2}} = 0.</equation>因此，存在<equation>\xi \in (1,2)</equation>，使得<equation>f(\xi) = (2 - \xi)\mathrm{e}^{\xi^2}</equation>（Ⅱ）令<equation>g ( x )=\ln x</equation>，则<equation>g^{\prime}(x)=\frac{1}{x}.</equation>由柯西中值定理，存在<equation>\eta\in(1,2)</equation>，使得<equation>\frac {f (2) - f (1)}{g (2) - g (1)} = \frac {f ^ {\prime} (\eta)}{g ^ {\prime} (\eta)}.</equation>由于<equation>f(1) = 0,g(1) = 0,g(2) = \ln 2</equation>，故（1）式可化为<equation>\frac{f(2)}{\ln 2} = \frac{\mathrm{e}^{\eta^2}}{\frac{1}{\eta}}</equation>即<equation>f(2) = \ln 2\cdot \eta \mathrm{e}^{\eta^2}</equation>.

---

**2019年第21题 | 解答题 | 11分**
21. (本题满分11分)

已知函数 f(x)在[0,1]上具有2阶导数，且<equation>f(0)=0,f(1)=1,\int_{0}^{1} f(x)\mathrm{d} x=1</equation>，证明：

I. 存在<equation>\xi \in(0,1)</equation>，使得<equation>f^{\prime}(\xi)=0;</equation>II. 存在<equation>\eta \in(0,1)</equation>，使得<equation>f^{\prime\prime}(\eta)<-2</equation>
**答案: **（I）证明略；

（Ⅱ）证明略.
**解析: **证（I）（法一）构造辅助函数<equation>F ( x )=\int_{0}^{x} f ( t ) \mathrm{d} t</equation>，则<equation>F ( 0 )=0,F ( 1 )=\int_{0}^{1} f ( x ) \mathrm{d} x=1.</equation>由拉格朗日中值定理可得，存在<equation>c \in(0,1)</equation>，使得<equation>F^{\prime}(c)=1</equation>即<equation>f(c)=1.</equation>再对<equation>[c,1]</equation>上的<equation>f(x)</equation>使用罗尔定理可得，存在<equation>\xi\in(c,1)\subseteq(0,1)</equation>，使得<equation>f^{\prime}(\xi)=0.</equation>（法二）反证法.

由 f(x)在[0,1]上存在2阶导数可知<equation>f^{\prime}(x)</equation>在[0,1]上连续.若不存在<equation>\xi \in(0,1)</equation>，使得<equation>f^{\prime}(\xi)=0</equation>，则由<equation>f^{\prime}(x)</equation>的连续性以及零点定理可知，<equation>f^{\prime}(x)</equation>在(0,1)上恒大于零或恒小于零.

又因为<equation>f(0)=0</equation><equation>f(1)=1</equation>，所以<equation>f^{\prime}(x)</equation>恒大于零，<equation>f(x)</equation>在[0,1]上单调增加. f(1)是f(x)在 [0,1]上的最大值.于是，<equation>\int_ {0} ^ {1} f (x) \mathrm {d} x < \int_ {0} ^ {1} f (1) \mathrm {d} x = 1.</equation>这与<equation>\int_{0}^{1} f ( x ) \mathrm{d} x=1</equation>矛盾.

因此，存在<equation>\xi\in(0,1)</equation>，使得<equation>f^{\prime}(\xi)=0.</equation>（法三）证明 f(x)在[0,1]上的最大值大于1.

假设不然，则对于任意的<equation>x\in[0,1]</equation>，都有<equation>f(x)\leqslant 1</equation>，从而<equation>\int_{0}^{1}f(x)\mathrm{d}x\leqslant 1.</equation>又因为<equation>f(0)=0,f(1)=1</equation>所以由 f(x)的连续性可知，存在<equation>\delta >0</equation>，使得当<equation>x\in(0,\delta)</equation>时，<equation>f(x) < 1.</equation>于是，<equation>\int_{0}^{1}f(x)\mathrm{d}x < 1.</equation>这与<equation>\int_{0}^{1} f(x)\mathrm{d}x=1</equation>矛盾.假设不正确.

因此，<equation>f ( x )</equation>在[0,1]上的最大值大于1.如图（a）所示，记该点为<equation>\xi</equation>，由于<equation>f ( 0 )=0,f ( 1 )=1</equation>故<equation>\xi \in(0,1).</equation><equation>f ^ {\prime} (\xi) = 0.</equation>(a)

(b)

（Ⅱ）（法一）构造辅助函数<equation>G ( x )=f ( x )+x^{2}</equation>，于是 G(x)在[0,1]上2阶可导，且<equation>G^{\prime \prime} ( x )=f^{\prime \prime} ( x )+2.</equation>取 c为第（I）问中满足<equation>f ( c )=1</equation>的点，则<equation>G ( 0 )=0,G ( c )=1+c^{2},G ( 1 )=2.</equation>由拉格朗日中值定理可得，存在<equation>\eta_{1}\in (0,c)</equation>，使得<equation>G ^ {\prime} \left(\eta_ {1}\right) = \frac {G (c) - G (0)}{c - 0} = \frac {1 + c ^ {2}}{c}.</equation>存在<equation>\eta_{2}\in(c,1)</equation>，使得<equation>G ^ {\prime} \left(\eta_ {2}\right) = \frac {G (1) - G (c)}{1 - c} = \frac {1 - c ^ {2}}{1 - c} = 1 + c.</equation>再对<equation>[\eta_{1},\eta_{2} ]</equation>上的<equation>G^{\prime}(x)</equation>使用拉格朗日中值定理，可得存在<equation>\eta\in(\eta_{1},\eta_{2})\subseteq(0,1)</equation>，使得<equation>G ^ {\prime \prime} (\eta) = \frac {G ^ {\prime} \left(\eta_ {2}\right) - G ^ {\prime} \left(\eta_ {1}\right)}{\eta_ {2} - \eta_ {1}} = \frac {1 + c - \frac {1 + c ^ {2}}{c}}{\eta_ {2} - \eta_ {1}} = \frac {1 - \frac {1}{c}}{\eta_ {2} - \eta_ {1}}.</equation>由于<equation>c\in (0,1)</equation>，故<equation>1 - \frac{1}{c} < 0</equation>，从而<equation>G^{\prime \prime}(\eta) < 0</equation>，即<equation>f^{\prime \prime}(\eta) + 2 < 0</equation>，也即<equation>f^{\prime \prime}(\eta) < -2.</equation>（法二）构造二次函数<equation>g ( x )=a x^{2}+b x+c</equation>，使得<equation>g ( 0 )=f ( 0 )=0,g ( 1 )=f ( 1 )=1</equation>且<equation>\int_{0}^{1} g ( x ) \mathrm{d} x=\int_{0}^{1} f ( x ) \mathrm{d} x=1.</equation>由 g（0）=0可得 c=0.由 g（1）=1可得 a+b=1.又由<equation>\int_{0}^{1} g(x)\mathrm{d}x=1</equation>可得<equation>\frac{a}{3}+\frac{b}{2}=1</equation>即<equation>2a+3b=6.</equation>解得 a=-3,b=4.于是，令 g(x）=-3x²+4x. f(x)与 g(x)的图形如图（b）所示.

考虑<equation>G ( x ) = f ( x ) - g ( x )</equation>，则<equation>G ( 0 ) = 0, G ( 1 ) = 0, \int_{0}^{1} G ( x ) \mathrm{d} x = 0</equation>，且<equation>G^{\prime \prime}(x) = f^{\prime \prime}(x) + 6.</equation>下面我们证明，存在<equation>\eta\in(0,1)</equation>，使得<equation>G^{\prime\prime}(\eta)=0</equation>，即<equation>f^{\prime\prime}(\eta)=-6<-2.</equation>令<equation>H ( x )=\int_{0}^{x} G ( t ) \mathrm{d} t</equation>，则<equation>H ( 0 )=0,H ( 1 )=0.</equation>由拉格朗日中值定理可得，存在<equation>k \in(0,1)</equation>使得<equation>H^{\prime}(k)=0</equation>即<equation>G(k)=0.</equation>从而，<equation>G(0)=G(k)=G(1)=0.</equation>分别对<equation>[0,k],[k,1]</equation>上的<equation>G(x)</equation>使用罗尔定理，可得存在<equation>\eta_{1}\in(0,k),\eta_{2}\in(k,1)</equation>，使得<equation>G^{\prime}(\eta_{1})=0,G^{\prime}(\eta_{2})=0.</equation>再对<equation>[\eta_{1},\eta_{2}]</equation>上的<equation>G^{\prime}(x)</equation>使用罗尔定理，可得存在<equation>\eta \in (\eta_{1},\eta_{2})\subseteq (0,1)</equation>，使得<equation>G^{\prime \prime}(\eta) = 0</equation>，即<equation>f^{\prime \prime}(\eta) = -6 < -2.</equation>

---

**2015年第21题 | 解答题 | 11分**
21. (本题满分10分)

已知函数 f(x)在区间<equation>[ a,+\infty)</equation>上具有2阶导数，<equation>f ( a )=0, f^{\prime} ( x )>0, f^{\prime\prime} ( x )>0.</equation>设 b>a，曲线 y=f(x)在点 （b,f(b)）处的切线与x轴的交点是<equation>( x_{0},0)</equation>，证明 a<x0<b.
**答案: **## (21) 证明略.
**解析: **证 首先，由于过点（b，f(b)）的切线的斜率为<equation>f^{\prime}(b)</equation>，且该切线过点（<equation>x_{0},0)</equation>，故<equation>f^{\prime}(b)=\frac{f(b)-0}{b-x_{0}}</equation>，解得<equation>x_{0}=b-\frac{f(b)}{f^{\prime}(b)}。</equation>因为<equation>b > a, f^{\prime}(x) > 0, f(x)</equation>在<equation>[a, + \infty)</equation>上单调增加，所以<equation>f(b) > f(a)=0</equation>，从而<equation>\frac{f(b)}{f^{\prime}(b)} > 0.</equation>因此，<equation>x _ {0} = b - \frac {f (b)}{f ^ {\prime} (b)} < b.</equation>如图（a）所示，记点<equation>A</equation>为<equation>(a,f(a))</equation>，点<equation>B</equation>为<equation>(b,f(b))</equation>.

下面我们用两种方法证明<equation>a < x_{0}。</equation>(a)

(b)

（法一）由拉格朗日中值定理可得，存在<equation>\xi\in(a,b)</equation>，使得<equation>f^{\prime}(\xi)(b-a)=f(b)-f(a)</equation>，即弦AB的斜率等于曲线弧<equation>\widehat{AB}</equation>上某点<equation>(\xi,f(\xi))</equation>处的切线斜率<equation>f^{\prime}(\xi).</equation>由于<equation>f^{\prime\prime}(x)>0</equation>，故<equation>f^{\prime}(x)</equation>在<equation>[a,+\infty)</equation>上为单调增加函数，从而<equation>f^{\prime}(\xi)<f^{\prime}(b).</equation><equation>\frac {f (b) - f (a)}{b - a} = f ^ {\prime} (\xi) < f ^ {\prime} (b) = \frac {f (b) - 0}{b - x _ {0}}.</equation>代入<equation>f ( a ) = 0</equation>，得<equation>\frac{f ( b )}{b - a} < \frac{f ( b )}{b - x_0}.</equation>由于<equation>b - a > 0, b - x_0 > 0, f ( b ) > 0</equation>，故<equation>b - a > b - x_0</equation>，即<equation>a < x_0.</equation>（法二）要证<equation>x_{0} > a</equation>，即要证<equation>x_{0}=b-\frac{f(b)}{f^{\prime}(b)} > a.</equation>整理该不等式得<equation>b - \frac {f (b)}{f ^ {\prime} (b)} > a \xleftrightarrow {f ^ {\prime} (b) > 0} (b - a) f ^ {\prime} (b) - f (b) > 0.</equation>该不等式的几何意义为过点（a，0），斜率为<equation>f^{\prime}(b)</equation>的直线l在 x=b的纵坐标大于f(b).我们可证明在（a，b]上，直线l位于曲线 y=f(x）之上，如图（b）.

记<equation>g ( x )=f^{\prime} ( b ) ( x-a )</equation>，直线 l的方程为<equation>y=g ( x ).</equation>要证在（a,b]上，直线 l位于曲线<equation>y=f(x)</equation>之上，即要证当<equation>x\in(a,b]</equation>时，<equation>g ( x )-f ( x ) > 0.</equation>由拉格朗日中值定理，有<equation>f ( x ) = f ( a ) + f^{\prime} ( \xi_{x} ) ( x - a )</equation>，这里<equation>x \in(a,b]</equation><equation>\xi_{x} \in(a,x).</equation>从而<equation>g ( x ) - f ( x ) = f^{\prime} ( b ) ( x - a ) - f ( a ) - f^{\prime} ( \xi_{x} ) ( x - a)\frac{f ( a ) = 0}{=} \left[ f^{\prime} ( b ) - f^{\prime} ( \xi_{x} ) \right] ( x - a).</equation>由于对任意的<equation>x \in(a,b]</equation>，都有<equation>\xi_{x} < b</equation>，而<equation>f^{\prime\prime}(x)>0</equation><equation>f^{\prime}(x)</equation>在[a,b]上单调增加，故<equation>f ^ {\prime} (b) - f ^ {\prime} \left(\xi_ {x}\right) > 0.</equation>因此，<equation>g ( x ) - f ( x )</equation>在（a，b]上恒大于零.特别地，<equation>g ( b ) - f ( b ) > 0</equation>即<equation>f^{\prime} ( b ) ( b - a ) - f ( b ) > 0</equation><equation>x_{0}>a.</equation>综上所述，<equation>a < x_{0} < b.</equation>

---

**2013年第18题 | 解答题 | 10分**
8. (本题满分10分)

设奇函数 f(x)在<equation>[-1,1]</equation>上具有2阶导数，且 f(1)=1.证明：

I. 存在<equation>\xi \in(0,1)</equation>，使得<equation>f^{\prime}(\xi)=1;</equation>II. 存在<equation>\eta \in(-1,1)</equation>，使得<equation>f^{\prime\prime}(\eta)+f^{\prime}(\eta)=1.</equation>
**答案: **（18）（I）证明略；

（Ⅱ）证明略.
**解析: **证（I）由 f(x)为奇函数得 f(0)=0.由于 f(1)=1，且 f(x)在[-1,1]上可导，故由拉格朗日中值定理得，存在<equation>\xi \in(0,1)</equation>，使得<equation>f(1)-f(0)=f^{\prime}(\xi)</equation>，即<equation>f^{\prime}(\xi)=1.</equation>（Ⅱ）（法一）构造辅助函数<equation>g ( x )=f^{\prime} ( x )+f ( x )-x. g ( x )</equation>在[-1，1]上可导.

若能在[-1，1]上找到两个点<equation>x_{1}, x_{2}</equation>，使得<equation>g(x_{1})=g(x_{2})</equation>，则由罗尔定理可得，存在<equation>\eta \in</equation>（-1，1），<equation>g^{\prime}(\eta)=0</equation>，即<equation>f^{\prime\prime}(\eta)+f^{\prime}(\eta)=1.</equation>由于 f(x）是<equation>[-1,1]</equation>上的奇函数，故<equation>f(x)=-f(-x).</equation>该等式两端同时关于 x求导得<equation>f^{\prime}(x)=</equation><equation>f^{\prime}(-x).</equation>于是<equation>f^{\prime}(x)</equation>是<equation>[-1,1]</equation>上的偶函数.从而，<equation>g (1) = f ^ {\prime} (1) + f (1) - 1, \quad g (- 1) = f ^ {\prime} (- 1) + f (- 1) - (- 1) = f ^ {\prime} (1) - f (1) + 1.</equation>由于<equation>f(1) - 1 = 0</equation>，故<equation>g(1) = g(-1)</equation>由罗尔定理可知，存在<equation>\eta \in (-1,1)</equation>，<equation>g^{\prime}(\eta) = 0</equation>，即<equation>f^{\prime \prime}(\eta) + f^{\prime}(\eta) = 1.</equation>（法二）构造辅助函数<equation>G ( x ) = \mathrm{e}^{x} \left[ f^{\prime} ( x )-1 \right]. G ( x )</equation>在[-1，1]上可导.<equation>G ^ {\prime} (x) = \mathrm {e} ^ {x} \left[ f ^ {\prime} (x) - 1 \right] + \mathrm {e} ^ {x} f ^ {\prime \prime} (x) = \mathrm {e} ^ {x} \left[ f ^ {\prime \prime} (x) + f ^ {\prime} (x) - 1 \right].</equation>由于<equation>f ( x )</equation>是<equation>[-1,1]</equation>上的奇函数，同法一中的论证可知<equation>f^{\prime}(x)</equation>是<equation>[-1,1]</equation>上的偶函数.<equation>\xi</equation>为第（I）问中所得，满足<equation>f^{\prime}(\xi)=1</equation>，从而<equation>f^{\prime}(-\xi)=f^{\prime}(\xi)=1.</equation>因此<equation>G(\xi)=G(-\xi)=0.</equation>由罗尔定理，存在<equation>\eta\in(-1,1)</equation>，使得<equation>G^{\prime}(\eta)=0</equation>.又因为<equation>\mathrm{e}^{\eta}>0</equation>，所以<equation>f^{\prime\prime}(\eta)+f^{\prime}(\eta)-1=0</equation>，即<equation>f^{\prime\prime}(\eta)+f^{\prime}(\eta)=1.</equation>

---

**2010年第21题 | 解答题 | 11分**
21. (本题满分10分)

假设函数 f(x)在闭区间[0,1]上连续，在开区间（0，1）内可导，且 f(0)=0，f(1)=<equation>\frac{1}{3}</equation>.证明：存在<equation>\xi \in\left(0,\frac{1}{2}\right),\eta \in</equation><equation>\left(\frac{1}{2},1\right)</equation>，使得：<equation>f^{\prime}(\xi)+f^{\prime}(\eta)=\xi^{2}+\eta^{2}.</equation>
**解析: **证构造辅助函数<equation>g ( x )=f ( x )-\frac{1}{3} x^{3}</equation>，则 g(x)在[0，1]上连续，(0，1)内可导，<equation>g^{\prime} ( x )=</equation><equation>f^{\prime} ( x )-x^{2}.</equation>，于是，所要证的结论变为“存在<equation>\xi\in\left(0,\frac{1}{2}\right),\eta\in\left(\frac{1}{2},1\right)</equation>，使得<equation>g^{\prime} (\xi)+g^{\prime} (\eta)=0.</equation>”首先，由题设，有<equation>g ( 0 )=f ( 0 )=0</equation>，<equation>g ( 1 )=f ( 1 )-\frac{1}{3}=0.</equation>分别在<equation>\left[0,\frac{1}{2}\right]</equation>和<equation>\left[\frac{1}{2},1\right]</equation>上对 g(x)使用拉格朗日中值定理可得，存在<equation>\xi\in\left(0,\frac{1}{2}\right),\eta\in</equation><equation>\left(\frac{1}{2},1\right)</equation>，使得<equation>g \left(\frac {1}{2}\right) - g (0) = \frac {1}{2} g ^ {\prime} (\xi), \quad g (1) - g \left(\frac {1}{2}\right) = \frac {1}{2} g ^ {\prime} (\eta).</equation>由（1）式，得<equation>g ( 1 ) - g ( 0 ) = \frac { 1 } { 2 } \left[ g^{\prime} ( \xi ) + g^{\prime} ( \eta ) \right]</equation>.又因为<equation>g ( 0 ) = g ( 1 ) = 0</equation>，所以<equation>g^{\prime} (\xi) + g^{\prime} (\eta) = 0</equation>即<equation>f^{\prime} (\xi) + f^{\prime} (\eta) = \xi^{2} + \eta^{2}.</equation>

---

**2009年第21题 | 解答题 | 11分**

I. 证明拉格朗日中值定理：若函数 f(x)在<equation>[a,b]</equation>上连续，在（a,b）内可导，则存在点<equation>\xi\in(a,b)</equation>，使得<equation>f(b)-f(a)=f^{\prime}(\xi)(b-a).</equation>II. 证明：若函数 f(x)在 x=0处连续，在<equation>(0,\delta)(\delta>0)</equation>内可导，且<equation>\lim_{x\rightarrow 0^{+}}f^{\prime}(x)=A</equation>，则<equation>f_{+}^{\prime}(0)</equation>存在，且<equation>f_{+}^{\prime}(0)=A.</equation>
**答案: **（21）（Ⅰ）证明略.

（Ⅱ）证明略.
**解析: **证（ I ）令<equation>\varphi (x) = f (x) - f (a) - \frac {f (b) - f (a)}{b - a} (x - a).</equation><equation>\varphi (x)</equation>在<equation>[a,b]</equation>上连续，在<equation>(a,b)</equation>内可导.计算得<equation>\varphi (a) = 0,\varphi (b) = 0.</equation>对<equation>\varphi(x)</equation>使用罗尔定理得，存在<equation>\xi\in(a,b)</equation>，使得<equation>\varphi^{\prime}(\xi)=0</equation>，即<equation>f^{\prime}(\xi)-\frac{f(b)-f(a)}{b-a}=0.</equation>因此，存在<equation>\xi\in(a,b)</equation>，使得<equation>f(b)-f(a)=f^{\prime}(\xi)(b-a).</equation>（Ⅱ）（法一）根据右侧导数的定义，<equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x}.</equation>由拉格朗日中值定理，对任意的<equation>x\in (0,\delta)</equation>，都存在<equation>\xi_{x}\in (0,x)</equation>，使得<equation>f (x) - f (0) = f ^ {\prime} \left(\xi_ {x}\right) x.</equation>从而<equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x} = \lim _ {x \rightarrow 0 ^ {+}} \frac {f ^ {\prime} \left(\xi_ {x}\right) x}{x} = \lim _ {0 < \xi_ {x} < x, \atop x \rightarrow 0 ^ {+}} f ^ {\prime} \left(\xi_ {x}\right).</equation>由于<equation>x\to 0^{+}</equation>，故<equation>\xi_{x}\to 0^{+}</equation>.因此，<equation>f _ {+} ^ {\prime} (0) = \lim _ {0 < \xi_ {x} < x, x \rightarrow 0 ^ {+}} f ^ {\prime} \left(\xi_ {x}\right) = \lim _ {x \rightarrow 0 ^ {+}} f ^ {\prime} (x) = A.</equation>（法二）由洛必达法则，<equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {f ^ {\prime} (x)}{1} = A.</equation>因此，<equation>f_{+}^{\prime}(0)</equation>存在，且等于A.

---


#### 导数的应用

**2024年第11题 | 填空题 | 5分**
11. 曲线<equation>y^{2}=x</equation>在点(0,0)处的曲率圆方程为 ___
**答案: **<equation>\left(x - \frac {1}{2}\right) ^ {2} + y ^ {2} = \frac {1}{4}</equation>
**解析: **解曲线<equation>y^{2}=x</equation>的参数方程可写为<equation>\left\{\begin{array}{l l}x=y^{2},\\ y=y,\end{array}\right.</equation>故<equation>\frac{\mathrm{d}x}{\mathrm{d}y}=2y,\frac{\mathrm{d}^{2}x}{\mathrm{d}y^{2}}=2,\frac{\mathrm{d}y}{\mathrm{d}y}=1,\frac{\mathrm{d}^{2}y}{\mathrm{d}y^{2}}=0</equation>曲线上点 （x,y）处的曲率<equation>K=\frac{\left|2y\cdot0-2\cdot1\right|}{\left[(2y)^{2}+1^{2}\right]^{\frac{3}{2}}}=\frac{2}{\left(4y^{2}+1\right)^{\frac{3}{2}}}.</equation>(1)

由（1）式可得，点（0,0）处的曲率<equation>K=\frac{2}{(0+1)^{\frac{3}{2}}}=2</equation>，故该点处的曲率半径为<equation>\frac{1}{K}=\frac{1}{2}.</equation>由于曲线在点（0,0）处的切线为y轴，故法线为x轴，曲率中心在点<equation>\left(\frac{1}{2},0\right).</equation>因此，所求曲率圆方程为<equation>\left(x-\frac{1}{2}\right)^{2}+y^{2}=\frac{1}{4}.</equation>

---

**2024年第15题 | 填空题 | 5分**
15. 设某物体以速度<equation>v ( t )=t+k \sin \pi t</equation>做直线运动. 若它从 t=0到 t=3的时间段内平均速度是<equation>\frac{5}{2}</equation>，则 k=___
**答案: **##<equation>\frac{3}{2}\pi</equation>
**解析: **解 由函数的平均值的定义可知，物体从 t=0到 t=3的时间段内平均速度<equation>\bar{v} ( t )=\frac{\int_{0}^{3} v ( t ) \mathrm{d} t}{3}.</equation>于是，由平均速度为<equation>\frac{5}{2}</equation>可得<equation>\frac {\int_ {0} ^ {3} v (t) \mathrm {d} t}{3} = \frac {5}{2}, \quad \text {即} \int_ {0} ^ {3} (t + k \sin \pi t) \mathrm {d} t = \frac {1 5}{2}.</equation>由于<equation>\int_ {0} ^ {3} \left(t + k \sin \pi t\right) \mathrm {d} t = \left(\frac {t ^ {2}}{2} - \frac {k}{\pi} \cos \pi t\right) \Bigg | _ {0} ^ {3} = \frac {9}{2} - \frac {k}{\pi} (- 1 - 1) = \frac {9}{2} + \frac {2 k}{\pi},</equation>故由（1）式可得<equation>\frac{9}{2} +\frac{2k}{\pi} = \frac{15}{2}</equation>，解得<equation>k = \frac{3\pi}{2}</equation>

---

**2023年第14题 | 填空题 | 5分**
14. 曲线<equation>3 x^{3}=y^{5}+2 y^{3}</equation>在<equation>x=1</equation>对应点处的法线斜率为 ___
**答案: **# 11 9
**解析: **解记<equation>f ( y )=y^{5}+2 y^{3}-3</equation>，则<equation>f ( 1 )=0</equation>.又因为<equation>f^{\prime}(y)=5 y^{4}+6 y^{2}\geqslant 0</equation>，所以f(y）单调增加，<equation>y=1</equation>是f(y）的唯一零点.由于当且仅当 x=1时，<equation>3 x^{3}=3</equation>，故当且仅当 y=1时，x=1，从而曲线<equation>3 x^{3}=y^{5}+2 y^{3}</equation>在 x=1处的对应点为点（1,1）.

对方程<equation>3 x^{3}=y^{5}+2 y^{3}</equation>两端关于 x求导，可得<equation>9 x ^ {2} = \left(5 y ^ {4} + 6 y ^ {2}\right) y ^ {\prime}.</equation>将<equation>x = 1,y = 1</equation>代入（1）式，可得<equation>9 = 11y^{\prime}</equation>.因此，<equation>y^{\prime}(1) = \frac{9}{11}</equation>即<equation>x = 1</equation>对应点处的切线斜率为<equation>\frac{9}{11}</equation>.

由于同一点处的切线与法线相互垂直，此时切线斜率与法线斜率的乘积为-1，故 x=1对应点处的法线斜率为<equation>-\frac{11}{9}.</equation>

---

**2021年第3题 | 选择题 | 5分 | 答案: C**
3. 有一圆柱体，底面半径与高随时间的变化率分别为<equation>2 \mathrm{~cm} / \mathrm{s},-3 \mathrm{~cm} / \mathrm{s}</equation>，当底面半径为10cm，高为5cm时，圆体的体积与表面积随时间的变化速率为（    )

A.<equation>1 2 5 \pi \mathrm{c m}^{3} / \mathrm{s},4 0 \pi \mathrm{c m}^{2} / \mathrm{s}</equation>B.<equation>1 2 5 \pi \mathrm{c m}^{3} / \mathrm{s},-4 0 \pi \mathrm{c m}^{2} / \mathrm{s}</equation>C.<equation>- 1 0 0 \pi \mathrm{c m}^{3} / \mathrm{s},4 0 \pi \mathrm{c m}^{2} / \mathrm{s}</equation>D.<equation>- 1 0 0 \pi \mathrm{c m}^{3} / \mathrm{s},-4 0 \pi \mathrm{c m}^{2} / \mathrm{s}</equation>
答案: C
**解析: **解设圆柱体的底面半径为 r(t)，高为 h(t)，则圆柱体的体积<equation>V ( t )=\pi r^{2} ( t ) h ( t )</equation>，表面积<equation>S ( t )=2 \pi r ( t ) h ( t )+2 \pi r^{2} ( t ).</equation>由链式法则，<equation>\frac {\mathrm {d} V}{\mathrm {d} t} = \frac {\partial V}{\partial r} \frac {\mathrm {d} r}{\mathrm {d} t} + \frac {\partial V}{\partial h} \frac {\mathrm {d} h}{\mathrm {d} t} = 2 \pi r h \frac {\mathrm {d} r}{\mathrm {d} t} + \pi r ^ {2} \frac {\mathrm {d} h}{\mathrm {d} t}.</equation><equation>\frac {\mathrm {d} S}{\mathrm {d} t} = \frac {\partial S}{\partial r} \frac {\mathrm {d} r}{\mathrm {d} t} + \frac {\partial S}{\partial h} \frac {\mathrm {d} h}{\mathrm {d} t} = (2 \pi h + 4 \pi r) \frac {\mathrm {d} r}{\mathrm {d} t} + 2 \pi r \frac {\mathrm {d} h}{\mathrm {d} t}.</equation>代入 r=10 cm,h=5 cm<equation>\frac{\mathrm{d} r}{\mathrm{d} t}=2 \mathrm{~ c m / s}, \frac{\mathrm{d} h}{\mathrm{d} t}=-3 \mathrm{~ c m / s}</equation>可得<equation>\frac {\mathrm {d} V}{\mathrm {d} t} = 2 \pi \times 1 0 \times 5 \times 2 + \pi \times 1 0 0 \times (- 3) = 2 0 0 \pi - 3 0 0 \pi = - 1 0 0 \pi \left(\mathrm {c m} ^ {3} / \mathrm {s}\right).</equation><equation>\frac {\mathrm {d} S}{\mathrm {d} t} = \left(2 \pi \times 5 + 4 \pi \times 1 0\right) \times 2 + 2 \pi \times 1 0 \times (- 3) = 1 0 0 \pi - 6 0 \pi = 4 0 \pi \left(\mathrm {c m} ^ {2} / \mathrm {s}\right).</equation>因此，应选C.

---

**2019年第6题 | 选择题 | 4分 | 答案: A**
6. 已知 f(x), g(x)二阶可导，且2阶导函数在 x=a处连续，则<equation>\lim_{x\rightarrow a}\frac{f(x)-g(x)}{(x-a)^{2}}=0</equation>是曲线 y=f(x)和 y=g(x)在 x=a对应的点处相切且曲率相等的（    ）

A. 充分非必要条件 B. 充分必要条件

C. 必要非充分条件 D. 既非充分又非必要条件
答案: A
**解析: **解 由<equation>f ( x )</equation>，<equation>g ( x )</equation>在<equation>x=a</equation>处的二阶泰勒公式可得，<equation>f (x) = f (a) + f ^ {\prime} (a) (x - a) + \frac {f ^ {\prime \prime} (a)}{2} (x - a) ^ {2} + o \left(\left(x - a\right) ^ {2}\right),</equation><equation>g (x) = g (a) + g ^ {\prime} (a) (x - a) + \frac {g ^ {\prime \prime} (a)}{2} (x - a) ^ {2} + o \left(\left(x - a\right) ^ {2}\right).</equation>代入<equation>\lim_{x\to a}\frac{f(x) - g(x)}{(x - a)^2}</equation>可得，<equation>\lim_{x\to a}\frac{f(x) - g(x)}{(x - a)^2} = \lim_{x\to a}\frac{[f(a) - g(a)] + [f'(a) - g'(a)](x - a) + \frac{f''(a) - g''(a)}{2}(x - a)^2 + o((x - a)^2)}{(x - a)^2}.</equation>由上式可知<equation>\lim_{x\to a}\frac{f(x) - g(x)}{(x - a)^2} = 0</equation>当且仅当<equation>\left\{ \begin{array}{l} f(a) = g(a), \\ f'(a) = g'(a), \\ f''(a) = g''(a). \end{array} \right.</equation>曲线<equation>y=f(x)</equation>与<equation>y=g(x)</equation>在<equation>x=a</equation>对应的点处相切当且仅当<equation>\left\{ \begin{array}{l l} f(a)=g(a), \\ f^{\prime}(a)=g^{\prime}(a). \end{array} \right.</equation>又由曲率的计算公式<equation>K=\frac{\left|y^{\prime \prime}\right|}{\left[1+(y^{\prime})^{2}\right]^{\frac{3}{2}}}</equation>以及<equation>f^{\prime \prime}(a)=g^{\prime \prime}(a)</equation>可得两条曲线在<equation>x=a</equation>对应的点处曲率相等.

因此，<equation>\lim_{x\to a}\frac{f(x)-g(x)}{(x-a)^{2}}=0</equation>是曲线 y=f(x）和 y=g(x）在 x=a对应的点处相切且曲率相等的充分条件.

注意到两曲线在 x=a对应的点处曲率相等只能说明<equation>|f^{\prime \prime}(a)|=|g^{\prime \prime}(a)|</equation>，但并不能推出<equation>f^{\prime \prime}(a)=g^{\prime \prime}(a)</equation>，故<equation>\lim_{x\to a}\frac{f(x)-g(x)}{(x-a)^{2}}=0</equation>不是曲线 y=f(x)和 y=g(x)在 x=a对应的点处相切且曲率相等的必要条件.

例如：取<equation>f ( x )=1-\sqrt{1-x^{2}}</equation><equation>g ( x )=-1+\sqrt{1-x^{2}}</equation><equation>y=f(x), y=g(x)</equation>这两条曲线均为半径为1的半圆弧（圆弧上各点的曲率半径均为1）.于是，各点处曲率相等，均等于1.如图所示，这两条曲线在原点处相切，但<equation>y=f(x)</equation>在[-1，1]上是凹曲线，<equation>y=g(x)</equation>在[-1，1]上是凸曲线，<equation>f^{\prime \prime}(0)\neq g^{\prime \prime}(0).</equation>综上所述，应选A.

---

**2019年第10题 | 填空题 | 4分**
10. 曲线<equation>\left\{ \begin{array}{l} x = t - \sin t \\ y = 1 - \cos t \end{array} \right.</equation>在<equation>t=\frac{3\pi}{2}</equation>对应点处的切线在 y 轴上的截距为 ___
**答案: **#<equation>\frac{3\pi}{2}+2.</equation>
**解析: **分析 本题主要考查由参数方程确定的函数求导以及导数的几何意义.

如图所示，本题中的曲线为摆线，可利用由参数方程确定的函数求导计算<equation>t=\frac{3\pi}{2}</equation>对应点处的导数值，从而得到该点处的切线方程，再计算该切线在 y轴上的截距.

解 计算<equation>t=\frac{3\pi}{2}</equation>对应点处的导数值.<equation>\left. \frac {\mathrm {d} y}{\mathrm {d} x} \right| _ {t = \frac {3 \pi}{2}} = \left. \frac {\mathrm {d} y}{\mathrm {d} t} \right| / \left. \frac {\mathrm {d} x}{\mathrm {d} t} \right| _ {t = \frac {3 \pi}{2}} = \left. \frac {\sin t}{1 - \cos t} \right| _ {t = \frac {3 \pi}{2}} = \frac {- 1}{1} = - 1.</equation>当 t =<equation>\frac{3\pi}{2}</equation>时，x =<equation>\frac{3\pi}{2}+1</equation>，y=1.于是，该点处的切线方程为 y-1=-<equation>\left(x-\frac{3\pi}{2}-1\right).</equation>令 x=0，可得 y =<equation>\frac{3\pi}{2}+2.</equation>因此，所求截距为<equation>\frac{3\pi}{2}+2.</equation>

---

**2018年第12题 | 填空题 | 4分**
12. 曲线<equation>\left\{ \begin{array}{l} x = \cos^ {3} t \\ y = \sin^ {3} t \end{array} \right.</equation>
**答案: **# 2 3.
**解析: **解分别计算<equation>\frac{\mathrm{d} y}{\mathrm{d} x},\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}.</equation><equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {3 \sin^ {2} t \cos t}{- 3 \cos^ {2} t \sin t} = - \tan t,</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\mathrm {d} \left(\frac {\mathrm {d} y}{\mathrm {d} x}\right)}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {- \sec^ {2} t}{- 3 \cos^ {2} t \sin t} = \frac {\sec^ {4} t}{3 \sin t}.</equation>当 t =<equation>\frac{\pi}{4}</equation>时，<equation>\left. \frac{\mathrm{d} y}{\mathrm{d} x}\right|_{t=\frac{\pi}{4}}=-1</equation><equation>\left. \frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\right|_{t=\frac{\pi}{4}}=\frac{(\sqrt{2})^{4}}{3\times \frac{\sqrt{2}}{2}}=\frac{4\sqrt{2}}{3}</equation>根据曲率的计算公式，所求曲率<equation>= \frac{\frac{4\sqrt{2}}{3}}{\left[ 1+(-1)^{2}\right]^{\frac{3}{2}}}=\frac{4\sqrt{2}}{3}\bigg /2\sqrt{2}=\frac{2}{3}.</equation>

---

**2016年第13题 | 填空题 | 4分**
13. 已知动点 P在曲线<equation>y=x^{3}</equation>上运动，记坐标原点与点 P间的距离为 l. 若点 P的横坐标对时间的变化率为常数<equation>v_{0}</equation>，则当点 P运动到点（1,1）时，l对时间的变化率是 ___
**答案: **##<equation>2 \sqrt{2} v_{0}.</equation>
**解析: **解设点 P的坐标为<equation>( x,x^{3} )</equation>，则<equation>l=\sqrt{x^{2}+x^{6}}</equation>点 P的横坐标对时间的变化率为<equation>\frac{\mathrm{d} x}{\mathrm{d} t}=v_{0}.</equation>记 l对时间的变化率为<equation>\frac{\mathrm{d} l}{\mathrm{d} t}.</equation>由链式法则得<equation>\frac {\mathrm {d} l}{\mathrm {d} t} = \frac {\mathrm {d} l}{\mathrm {d} x} \cdot \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {1}{2} \cdot \frac {6 x ^ {5} + 2 x}{\sqrt {x ^ {2} + x ^ {6}}} \cdot v _ {0}.</equation>当 x=1时，代入（1）式得<equation>\frac{\mathrm{d} l}{\mathrm{d} t}\bigg|_{x=1}=\frac{4}{\sqrt{2}} v_{0}=2\sqrt{2} v_{0}.</equation>

---

**2014年第4题 | 选择题 | 4分 | 答案: C**
4. 曲线<equation>\left\{\begin{array}{l l}x=t^{2}+7,\\y=t^{2}+4 t+1\end{array}\right.</equation>上对应于 t=1的点处的曲率半径是（    )

A.<equation>\frac{\sqrt{1 0}}{5 0}</equation>B.<equation>\frac{\sqrt{1 0}}{1 0 0}</equation>C.<equation>1 0 \sqrt{1 0}</equation>D.<equation>5 \sqrt{1 0}</equation>
答案: C
**解析: **解 先求对应于<equation>t = 1</equation>的点处的曲率，需要得到该点处的<equation>y^{\prime}, y^{\prime \prime}</equation>.<equation>\left. \frac {\mathrm {d} y}{\mathrm {d} x} \right| _ {t = 1} = \left. \frac {\mathrm {d} y}{\mathrm {d} t} \right/ \left. \frac {\mathrm {d} x}{\mathrm {d} t} \right| _ {t = 1} = \left. \frac {2 t + 4}{2 t} \right| _ {t = 1} = \left. \frac {t + 2}{t} \right| _ {t = 1} = 3,</equation><equation>\left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {t = 1} = \frac {\mathrm {d} \left(\frac {\mathrm {d} y}{\mathrm {d} x}\right)}{\mathrm {d} t} / \left. \frac {\mathrm {d} x}{\mathrm {d} t} \right| _ {t = 1} = \frac {- \frac {2}{t ^ {2}}}{2 t} \left| _ {t = 1} = - \frac {1}{t ^ {3}} \right| _ {t = 1} = - 1.</equation>因此，该点处的曲率半径<equation>\rho = \frac{1}{K} = \frac{[1 + (y^{\prime})^{2}]^{\frac{3}{2}}}{|y^{\prime \prime}|} = \frac{(1 + 3^{2})^{\frac{3}{2}}}{|-1|} = 10\sqrt{10}</equation>. 应选C.

---

**2014年第12题 | 填空题 | 4分**
12. 曲线<equation>L</equation>的极坐标方程是<equation>r=\theta</equation>, 则<equation>L</equation>在点<equation>(r,\theta)=\left(\frac{\pi}{2},\frac{\pi}{2}\right)</equation>处的切线的直角坐标方程是 ___
**答案: **<equation>\frac {2}{\pi} x + y - \frac {\pi}{2} = 0.</equation>
**解析: **解（法一）由<equation>\left\{\begin{array}{l l}x=r\cos \theta \\ y=r\sin \theta\end{array}\right.</equation>以及r=得，<equation>\left\{\begin{array}{l l}x=\theta\cos \theta \\ y=\theta\sin \theta.\end{array}\right.</equation>于是，根据由参数方程确定的函数的求导公式，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} \theta} / \frac {\mathrm {d} x}{\mathrm {d} \theta} = \frac {\sin \theta + \theta \cos \theta}{\cos \theta - \theta \sin \theta}.</equation>于是，<equation>\frac{\mathrm{d}y}{\mathrm{d}x}\bigg|_{\theta = \frac{\pi}{2}} = \frac{1 + 0}{0 - \frac{\pi}{2}} = -\frac{2}{\pi}.</equation>由坐标变换公式得，极坐标系下的点<equation>\left(\frac{\pi}{2},\frac{\pi}{2}\right)</equation>对应直角坐标系下的点<equation>\left(0,\frac{\pi}{2}\right).</equation>因此，所求切线的点斜式方程为<equation>y-\frac{\pi}{2}=-\frac{2}{\pi} (x-0)</equation>即<equation>\frac{2}{\pi} x+y-\frac{\pi}{2}=0.</equation>（法二）曲线<equation>r = \theta</equation>是阿基米德螺线.这是一条光滑曲线.

由<equation>\left\{\begin{array}{l}x=r\cos \theta,\\ y=r\sin \theta\end{array}\right.</equation>可得，当<equation>\theta\in\left[0,\frac{\pi}{2}\right)</equation>时，<equation>r=\sqrt{x^{2}+y^{2}},</equation><equation>\theta=\arctan \frac{y}{x}.</equation>将该曲线方程写成直角坐标系下的形式，可得<equation>\sqrt{x^{2}+y^{2}}=\arctan \frac{y}{x}</equation>即当<equation>\theta\in\left[0,\frac{\pi}{2}\right)</equation>时，曲线<equation>r=\theta</equation>的直角坐标方程为<equation>\sqrt{x^{2}+y^{2}}=\arctan \frac{y}{x}.</equation>由（r，<equation>\theta)=\left(\frac{\pi}{2},\frac{\pi}{2}\right)</equation>得（x，y）<equation>=\left(0,\frac{\pi}{2}\right).</equation>虽然点<equation>\left(0,\frac{\pi}{2}\right)</equation>并不满足该方程，但由于曲线光滑，故该点处的斜率等于<equation>\lim_{x\to 0^{+}}y^{\prime}(x).</equation>对<equation>\sqrt{x^{2}+y^{2}}=\arctan \frac{y}{x}</equation>两端关于 x求导得<equation>\frac {2 x + 2 y y ^ {\prime}}{2 \sqrt {x ^ {2} + y ^ {2}}} = \frac {1}{1 + \left(\frac {y}{x}\right) ^ {2}} \cdot \frac {x y ^ {\prime} - y}{x ^ {2}}.</equation>化简得<equation>\frac {x y ^ {\prime} - y}{\sqrt {x ^ {2} + y ^ {2}}} = x ^ {-} + y y ^ {\prime}.</equation>由（1）式可得<equation>( x-y\sqrt{x^{2}+y^{2}}) y^{\prime}=x\sqrt{x^{2}+y^{2}}+y.</equation>令<equation>x\to0^{+}</equation>，并代入<equation>\lim_{x\to0^{+}}x=0,\lim_{x\to0^{+}}y(x)=\frac{\pi}{2}</equation>，可得<equation>\lim_{x\to0^{+}}y^{\prime}(x)=-\frac{2}{\pi}.</equation>因此，所求切线方程为<equation>y-\frac{\pi}{2}=- \frac{2}{\pi} x</equation>即<equation>\frac{2}{\pi} x+y-\frac{\pi}{2}=0.</equation>

---

**2013年第12题 | 填空题 | 4分**
12. 曲线<equation>\begin{aligned} x &= \arctan t, \\ y &= \ln \sqrt {1 + t ^ {2}} \end{aligned}</equation>上对应于<equation>t=1</equation>的点处的法线方程为 ___
**答案: **<equation>x+y=\frac{\pi}{4}+\frac{1}{2}\ln 2.</equation>
**解析: **曲线上对应于<equation>t = 1</equation>的点处的切线斜率为<equation>\left. \frac {\mathrm {d} y}{\mathrm {d} x} \right| _ {t = 1} = \frac {y ^ {\prime} (1)}{x ^ {\prime} (1)} = \frac {\frac {1}{2} \cdot \frac {2 t}{1 + t ^ {2}}}{\frac {1}{1 + t ^ {2}}} \Bigg | _ {t = 1} = 1,</equation>故曲线上对应于<equation>t=1</equation>的点处的法线斜率为-1.

又因为当 t=1时，<equation>x=\frac{\pi}{4}</equation><equation>y=\frac{1}{2}\ln 2</equation>，所以该法线过点<equation>\left(\frac{\pi}{4},\frac{1}{2}\ln 2\right)</equation>，从而可写出所求法线的点斜式方程<equation>y-\frac{1}{2}\ln 2=-\left(x-\frac{\pi}{4}\right)</equation>，即<equation>x+y=\frac{\pi}{4}+\frac{1}{2}\ln 2.</equation>

---

**2012年第13题 | 填空题 | 4分**
13. 曲线<equation>y=x^{2}+x \ ( x<0 )</equation>上曲率为<equation>\frac{\sqrt{2}}{2}</equation>的点的坐标是 ___
**答案: **## (-1,0).
**解析: **利用曲线方程可求得<equation>y^{\prime}=2 x+1</equation><equation>y^{\prime\prime}=2</equation>，故<equation>K = \frac {2}{\left[ 1 + \left(2 x + 1\right) ^ {2} \right] ^ {\frac {3}{2}}} = \frac {\sqrt {2}}{2}.</equation>由此可求得<equation>(2x + 1)^{2} = 1</equation>，故<equation>x = 0</equation>或<equation>x = -1</equation>.又因为<equation>x < 0</equation>，所以<equation>x = -1</equation>，此时<equation>y = 0</equation>因此，所求点的坐标为（-1，0）.

---

**2010年第3题 | 选择题 | 4分 | 答案: C**
3. 曲线<equation>y=x^{2}</equation>与曲线<equation>y=a\ln x \ (a\neq0)</equation>相切，则 a=（    ）

A. 4e B. 3e C. 2e D. e
答案: C
**解析: **解 若两曲线的公切点为<equation>\left(x_{0}, y_{0}\right)</equation>，则点<equation>\left(x_{0}, y_{0}\right)</equation>满足<equation>\left\{ \begin{array}{l} y _ {0} = x _ {0} ^ {2}, \\ y _ {0} = a \ln x _ {0} \\ 2 x _ {0} = \frac {a}{x _ {0}}. \end{array} \right.</equation>解上述方程组得，<equation>a=2\mathrm{e},\ x_{0}=\sqrt{\mathrm{e}},y_{0}=\mathrm{e}.</equation>应选C.

---

**2010年第13题 | 填空题 | 4分**
13. 已知一个长方形的长 l以 2 cm/s的速率增加，宽 w以 3 cm/s的速率增加，则当 l=12 cm，w=5 cm时，它的对角线增加的速率为___
**答案: **3 cm/s.
**解析: **解 设对角线长为 s（t），则<equation>s ^ {2} (t) = l ^ {2} (t) + w ^ {2} (t).</equation>等式两端同时关于 t 求导，得<equation>s \frac {\mathrm {d} s}{\mathrm {d} t} = l \frac {\mathrm {d} l}{\mathrm {d} t} + w \frac {\mathrm {d} w}{\mathrm {d} t}.</equation>当<equation>l = 12\mathrm{cm},w = 5\mathrm{cm}</equation>时，<equation>s = \sqrt{12^{2} + 5^{2}}\mathrm{cm} = 13\mathrm{cm}</equation>. 代入（1）式得<equation>1 3 \frac {\mathrm {d} s}{\mathrm {d} t} = 1 2 \times 2 + 5 \times 3.</equation>因此，<equation>\frac{\mathrm{d}s}{\mathrm{d}t}=3\mathrm{cm / s}.</equation>

---

**2009年第5题 | 选择题 | 4分 | 答案: B**
5. 若<equation>f^{\prime\prime}(x)</equation>不变号，且曲线<equation>y=f(x)</equation>在点（1，1）处的曲率圆为<equation>x^{2}+y^{2}=2</equation>，则函数 f(x)在区间（1，2）内（    ）

A. 有极值点，无零点 B. 无极值点，有零点 C. 有极值点，有零点 D. 无极值点，无零点
答案: B
**解析: **解（法一）由于曲线<equation>y=f(x)</equation>在点（1，1）附近的凹凸性与点 （1，1）处的曲率圆的凹凸性一致，而曲率圆为<equation>x^{2}+y^{2}=2</equation>，是凸曲线，故<equation>y^{\prime \prime}<0.</equation>考虑曲线在点（1，1）处的切线.

连接点（0，0）和点（1，1）的半径为点（1，1）处的法线，该法线斜率为<equation>\frac{1 - 0}{1 - 0} = 1</equation>，于是点（1，1）处的切线斜率为-1，即<equation>f^{\prime}(1) = -1.</equation>由于<equation>f^{\prime \prime}(x)</equation>不变号，故在区间（1，2）上，仍有<equation>f^{\prime \prime}(x)<0</equation>，从而<equation>f^{\prime}(x)</equation>在（1，2）上单调减少。又因为<equation>f^{\prime}(1)=-1<0</equation>，所以<equation>f^{\prime}(x)</equation>在（1，2）上恒小于零.于是 f(x)在（1，2）上单调减少.因此， f(x)在（1，2）上没有极值点.

再考虑<equation>f ( x )</equation>在（1，2）上的零点情况.

由拉格朗日中值定理知，存在<equation>\xi\in(1,2)</equation>，使得<equation>f(2)-f(1)=f^{\prime}(\xi)</equation>，即<equation>f(2)=1+f^{\prime}(\xi).</equation>由于<equation>f^{\prime}(x)</equation>在（1，2）上单调减少，且<equation>f^{\prime}(1)=-1</equation>，从而<equation>f^{\prime}(\xi)< - 1</equation>，故<equation>f(2)=1+f^{\prime}(\xi)< 0.</equation>因为<equation>f(1)=1>0,f(2)<0</equation>，所以由连续函数的介值定理知，<equation>f(x)</equation>在（1，2）上存在零点因此，<equation>f(x)</equation>在（1，2）上有零点，没有极值点.应选B.

（法二）由于曲线<equation>y=f(x)</equation>在点（1，1）附近的方程可由它在点（1，1）处的曲率圆方程来近似，即<equation>x^{2}+y^{2}=2</equation>，故我们可以用该方程算出<equation>f^{\prime}(1)</equation>和<equation>f^{\prime \prime}(1).</equation>对<equation>x^{2} + y^{2} = 2</equation>两端关于 x求导，得<equation>2 x + 2 y y ^ {\prime} = 0.</equation>代入<equation>x = 1</equation>，<equation>y(1) = 1</equation>得，<equation>y^{\prime}(1) = -1</equation>.继续对（1）式两端求导，得<equation>2 + 2 \left(y ^ {\prime}\right) ^ {2} + 2 y y ^ {\prime \prime} = 0.</equation>代入<equation>x = 1, y(1) = 1, y^{\prime}(1) = -1</equation>得，<equation>y^{\prime \prime}(1) = -2.</equation>由于<equation>y^{\prime \prime}</equation>不变号，故<equation>y^{\prime \prime}</equation>在（1，2）上恒小于零.

其余论证<equation>y = f(x)</equation>在（1，2）上有零点，没有极值点的过程同法一.

---

**2009年第9题 | 填空题 | 4分**
9. 曲线<equation>\left\{ \begin{array}{l} x = \int_ {0} ^ {1 - t} \mathrm {e} ^ {- u ^ {2}} \mathrm {d} u, \\ y = t ^ {2} \ln \left(2 - t ^ {2}\right) \end{array} \right.</equation>在点 (0,0) 处的切线方程为 ___
**答案: **## y=2x.
**解析: **解 先求点（0，0）所对应的参数 t的值.

由于<equation>\mathrm{e}^{-u^{2}}>0</equation>，故只有当<equation>1-t=0</equation>时，即<equation>t=1</equation>时，<equation>x=\int_{0}^{1-t}\mathrm{e}^{-u^{2}}\mathrm{d}u=0</equation>，且<equation>t=1</equation>时，<equation>y(1)=0.</equation>于是，<equation>t=1.</equation>由<equation>x = \int_0^{1 - t}\mathrm{e}^{-u^2}\mathrm{d}u</equation>得，<equation>\frac {\mathrm {d} x}{\mathrm {d} t} = \mathrm {e} ^ {- (1 - t) ^ {2}} \cdot \frac {\mathrm {d} (1 - t)}{\mathrm {d} t} = - \mathrm {e} ^ {- (1 - t) ^ {2}}.</equation>由<equation>y = t^{2}\ln (2 - t^{2})</equation>得，<equation>\frac {\mathrm {d} y}{\mathrm {d} t} = 2 t \ln \left(2 - t ^ {2}\right) - \frac {2 t ^ {3}}{2 - t ^ {2}}.</equation>因此，曲线在点（0，0）处的斜率为<equation>\left. \frac {\mathrm {d} y}{\mathrm {d} x} \right| _ {(0, 0)} = \frac {2 t \ln \left(2 - t ^ {2}\right) - \frac {2 t ^ {3}}{2 - t ^ {2}}}{- \mathrm {e} ^ {- (1 - t) ^ {2}}} \Bigg | _ {t = 1} = 2.</equation>曲线在点（0，0）处的切线方程为<equation>y - 0 = 2(x - 0)</equation>，即<equation>y = 2x</equation>

---


#### 方程根的存在性与个数

**2021年第4题 | 选择题 | 5分 | 答案: A**
4. 设函数<equation>f(x)=a x-b \ln x (a>0)</equation>有2个零点，则<equation>\frac{b}{a}</equation>的取值范围是（    )

A. (e,+∞) B. (0,e) C. (0,<equation>\frac{1}{e}</equation>D.<equation>(\frac{1}{e},+\infty)</equation>
答案: A
**解析: **解（法一）<equation>f ( x )</equation>的定义域为（0，<equation>+ \infty</equation>）.计算<equation>f^{\prime}(x)</equation>得<equation>f^{\prime}(x)=a-\frac{b}{x}.</equation>由于 a > 0，故若 b≤0，则<equation>f^{\prime}(x)>0</equation>，f(x)单调增加.此时 f(x)不可能有2个零点.于是，b > 0.

下面分析 f（x）的单调性.

当<equation>x=\frac{b}{a}</equation>时，<equation>f^{\prime}(x)=0</equation>；当<equation>0 < x < \frac{b}{a}</equation>时，<equation>f^{\prime}(x)<0,f(x)</equation>单调减少；当<equation>x > \frac{b}{a}</equation>时，<equation>f^{\prime}(x)>0,</equation>f(x)单调增加.于是，<equation>f(x)</equation>在（0，<equation>+\infty</equation>）上先单调减少，再单调增加.<equation>f\left(\frac{b}{a}\right)</equation>为f(x)的最小值.

f（x）有2个零点等价于<equation>f\left(\frac{b}{a}\right)</equation>小于零.否则f（x）恒大于等于零，不可能存在2个零点.<equation>f \left(\frac {b}{a}\right) = a \cdot \frac {b}{a} - b \ln \frac {b}{a} = b - b \ln \frac {b}{a} = b \left(1 - \ln \frac {b}{a}\right) < 0.</equation>又因为 b > 0，所以<equation>b \left( 1-\ln \frac{b}{a} \right) < 0</equation>等价于<equation>1-\ln \frac{b}{a} < 0</equation>即<equation>\ln \frac{b}{a} > 1,\frac{b}{a} > \mathrm{e}.</equation>因此，应选A.

（法二）同法一可知 b > 0.<equation>a x-b \ln x=0</equation>等价于<equation>\frac{x}{\ln x}=\frac{b}{a}</equation>，故函数<equation>f(x)=a x-b \ln x</equation>有2个零点等价于曲线<equation>y=\frac{x}{\ln x}</equation>与直线<equation>y=\frac{b}{a}</equation>有2个交点.

计算<equation>g ( x )=\frac{x}{\ln x}</equation>的导数<equation>g^{\prime}(x).</equation><equation>g ^ {\prime} (x) = \frac {\ln x - 1}{(\ln x) ^ {2}}.</equation>由于 x=1是 g(x)的无穷间断点，故 x=1是 y=g(x)的铅直渐近线.当 0 < x < 1时，<equation>g^{\prime}(x) < 0</equation>g(x)单调减少；当 1 < x < e时，<equation>g^{\prime}(x) < 0</equation>g(x)单调减少；当 x > e时，<equation>g^{\prime}(x) > 0</equation>g(x)单调增加，且<equation>\lim _ {x \rightarrow + \infty} g (x) = \lim _ {x \rightarrow + \infty} \frac {x}{\ln x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow + \infty} \frac {1}{\frac {1}{x}} = + \infty .</equation><equation>x=\mathrm{e}</equation>是<equation>g(x)</equation>的极小值点，极小值为<equation>g(\mathrm{e})=\mathrm{e}.</equation>y = g(x）的图形如右图所示.

由图可知，曲线<equation>y=\frac{x}{\ln x}</equation>与直线<equation>y=\frac{b}{a}</equation>有2个交点当且仅当<equation>\frac{b}{a}>\mathrm{e}.</equation>因此，应选A.

---

**2017年第19题 | 解答题 | 10分**
19. (本题满分10分)

设函数 f(x)在区间[0,1]上具有二阶导数，且<equation>f(1)>0,\lim_{x\rightarrow 0^{+}}\frac{f(x)}{x}<0.</equation>证明：

I. 方程 f(x)=0在区间（0,1）内至少存在一个实根；

II. 方程<equation>f(x)f^{\prime \prime}(x)+[f^{\prime}(x)]^{2}=0</equation>在区间（0,1）内至少存在两个不同实根.
**答案: **# （I）证明略；

（Ⅱ）证明略.
**解析: **证（I）由于<equation>\lim_{x\rightarrow 0^{+}}\frac{f(x)}{x}<0</equation>，故由函数极限的局部保号性可知，存在<equation>\theta >0</equation>，在（0，<equation>\theta</equation>）内，<equation>\frac{f(x)}{x}<0</equation>从而<equation>f(x) < 0</equation>.取0<equation>< \delta < \theta</equation>，则<equation>f(\delta) < 0.</equation>又因为<equation>f(1)>0</equation>，所以由连续函数的零点定理知，存在<equation>\xi\in(\delta,1)\subseteq(0,1)</equation>使得<equation>f(\xi)=0.</equation>因此，<equation>f(x)=0</equation>在区间（0，1）内至少存在一个实根.

（Ⅱ）考虑<equation>F ( x )=f ( x ) f^{\prime} ( x )</equation>，则<equation>F ^ {\prime} (x) = f (x) f ^ {\prime \prime} (x) + \left[ f ^ {\prime} (x) \right] ^ {2}.</equation>第（Ⅱ）问等价于证明<equation>F^{\prime}(x)=0</equation>在区间（0,1）内至少存在两个不同实根.

若能找到三个点 a < b < c ，使得 F(a) = F(b) = F(c) ，则由罗尔定理，存在<equation>\eta_{1}\in(a,b),</equation><equation>\eta_{2}\in(b,c)</equation>，满足<equation>F^{\prime}(\eta_{1})=0,F^{\prime}(\eta_{2})=0.</equation>由<equation>\lim_{x\rightarrow 0^{+}}\frac{f(x)}{x}<0</equation>知，分母趋于零，而极限仍存在，故<equation>f (0) \xlongequal {\text {连 续 性}} \lim _ {x \rightarrow 0 ^ {+}} f (x) = 0, \quad F (0) = f (0) f ^ {\prime} (0) = 0.</equation>由第（I）问的结论知，存在<equation>x_{1}\in(0,1)</equation>，满足<equation>f \left( x_{1} \right)=0</equation>，从而<equation>F \left( x_{1} \right)=f \left( x_{1} \right) f^{\prime} \left( x_{1} \right)=0.</equation>另一方面，由于<equation>f(0)=0</equation><equation>f(x_{1})=0</equation>，故由罗尔定理知，存在<equation>x_{2}\in(0,x_{1})</equation>，使得<equation>f^{\prime}(x_{2})=0</equation>，从而<equation>F(x_{2})=f(x_{2})f^{\prime}(x_{2})=0.</equation>如图所示，<equation>0 < x_{2} < x_{1}, F(0) = F(x_{2}) = F(x_{1}) = 0.</equation>由罗尔定理知，存在<equation>\eta_{1}\in(0,x_{2})</equation>，使得<equation>F^{\prime}(\eta_{1}) = 0</equation>；存在<equation>\eta_{2}\in(x_{2},x_{1})</equation>，使得<equation>F^{\prime}(\eta_{2}) = 0.</equation>命题得证

---

**2015年第19题 | 解答题 | 10分**
19. (本题满分11分)

已知函数<equation>f ( x )=\int_{x}^{1}\sqrt{1+t^{2}}\mathrm{d} t+\int_{1}^{x^{2}}\sqrt{1+t}\mathrm{d} t</equation>，求 f(x)零点的个数.
**答案: **(19)<equation>f(x)</equation>在<equation>(-\infty, +\infty)</equation>上共有两个零点.
**解析: **解（法一）由<equation>f ( x )=\int_{x}^{1}\sqrt{1+t^{2}}\mathrm{d} t+\int_{1}^{x^{2}}\sqrt{1+t}\mathrm{d} t</equation>，可知<equation>f ( x )</equation>在<equation>(-\infty , +\infty)</equation>上均有定义，且<equation>f^{\prime}(x)=\left(\int_{x}^{1}\sqrt{1+t^{2}}\mathrm{d} t\right)^{\prime}+\left(\int_{1}^{x^{2}}\sqrt{1+t}\mathrm{d} t\right)^{\prime}=-\sqrt{1+x^{2}}+2x\sqrt{1+x^{2}}=(2x-1)\sqrt{1+x^{2}}.</equation>由于<equation>\sqrt{1+x^{2}}>0</equation>，故<equation>x=\frac{1}{2}</equation>为f(x)的唯一驻点.

当<equation>x\in\left(\frac{1}{2},+\infty\right)</equation>时，<equation>f(x)</equation>单调增加；当<equation>x\in\left(-\infty ,\frac{1}{2}\right)</equation>时，<equation>f(x)</equation>单调减少. f(x)在<equation>x=\frac{1}{2}</equation>处取到最小值.

因为<equation>f ( 1 )=\int_{1}^{1}\sqrt{1+t^{2}}\mathrm{d} t+\int_{1}^{1^{2}}\sqrt{1+t}\mathrm{d} t=0</equation>，而<equation>f ( x )</equation>在<equation>\left(\frac{1}{2},+\infty\right)</equation>上单调增加，所以<equation>f ( x )</equation>在<equation>\left(\frac{1}{2},+\infty\right)</equation>上只有<equation>x=1</equation>一个零点.

由于<equation>f(1) = 0</equation>，故<equation>f\left(\frac{1}{2}\right) < f(1) = 0.</equation>又因为<equation>\lim_{x\to -\infty}f(x) = \lim_{x\to -\infty}\left(\int_x^1\sqrt{1 + t^2}\mathrm{d}t + \int_1^{x^2}\sqrt{1 + t}\mathrm{d}t\right)</equation>，两个被积函数<equation>\sqrt{1 + t^2},\sqrt{1 + t}</equation>均大于1，所以<equation>\lim_{x\to -\infty}f(x) = +\infty.</equation>由连续函数的零点定理可知，<equation>f(x)</equation>在<equation>\left(-\infty ,\frac{1}{2}\right)</equation>上必然也存在一个零点，且由<equation>f(x)</equation>的单调性可知，该零点也是该区间上的唯一零点.

综上所述，<equation>f ( x )</equation>在<equation>(-\infty, +\infty)</equation>上共有两个零点.

（法二）如法一，可得到<equation>f ( x )</equation>在<equation>\left(\frac{1}{2},+\infty\right)</equation>上只有<equation>x=1</equation>一个零点.

下面我们考虑 f（x）在<equation>\left(-\infty ,\frac{1}{2}\right)</equation>上是否存在零点.

计算 f（0），得<equation>f (0) = \int_ {0} ^ {1} \sqrt {1 + t ^ {2}} \mathrm {d} t + \int_ {1} ^ {0} \sqrt {1 + t} \mathrm {d} t = \int_ {0} ^ {1} \left(\sqrt {1 + t ^ {2}} - \sqrt {1 + t}\right) \mathrm {d} t.</equation>当<equation>t\in (0,1)</equation>时，<equation>t^{2} < t</equation>，故<equation>\sqrt{1 + t^2} -\sqrt{1 + t} < 0</equation>，从而<equation>f(0) < 0.</equation>又因为<equation>f(-1) = \int_{-1}^{1}\sqrt{1 + t^2}\mathrm{d}t + \int_{1}^{1}\sqrt{1 + t}\mathrm{d}t = \int_{-1}^{1}\sqrt{1 + t^2}\mathrm{d}t > 0</equation>，所以<equation>f(-1) > 0.</equation>由连续函数的零点定理可知，存在<equation>a\in(-1,0)</equation>，使得<equation>f(a)=0</equation>.由<equation>f(x)</equation>在<equation>\left(-\infty ,\frac{1}{2}\right)</equation>上的单调性可知该点也是<equation>\left(-\infty ,\frac{1}{2}\right)</equation>上的唯一零点.因此，<equation>f(x)</equation>在<equation>\left(-\infty ,\frac{1}{2}\right)</equation>上有且仅有一个零点.

综上所述，<equation>f ( x )</equation>在<equation>(-\infty, +\infty)</equation>上共有两个零点.

---

**2012年第21题 | 解答题 | 11分**
21. (本题满分10分)

I. 证明方程<equation>x^{n}+x^{n-1}+\cdots+x=1</equation>（ n为大于1的整数）在区间<equation>\left(\frac{1}{2},1\right)</equation>内有且仅有一个实根；

II. 记第一问中的实根为<equation>x_{n}</equation>，证明<equation>\lim_{n\rightarrow \infty}x_{n}</equation>存在，并求此极限.
**答案: **(21) （I）证明略；

（Ⅱ）证明略，<equation>\lim_{n\to \infty}x_n = \frac{1}{2}</equation>.
**解析: **证（I）设函数<equation>f_{n}(x)=x^{n}+x^{n-1}+\dots+x-1.</equation>考虑<equation>f_{n}\left(\frac{1}{2}\right)</equation>与<equation>f_{n}(1).</equation><equation>f _ {n} (1) = n - 1 > 0, \quad f _ {n} \left(\frac {1}{2}\right) = \frac {\frac {1}{2} \left(1 - \frac {1}{2 ^ {n}}\right)}{1 - \frac {1}{2}} - 1 = - \frac {1}{2 ^ {n}} < 0.</equation>由连续函数的零点定理知，存在<equation>x\in \left(\frac{1}{2},1\right)</equation>，使得<equation>f_{n}(x) = 0.</equation>又由于当<equation>x\in\left(\frac{1}{2},1\right)</equation>时，<equation>f _ {n} ^ {\prime} (x) = n x ^ {n - 1} + (n - 1) x ^ {n - 2} + \dots + 2 x + 1 > 0,</equation>故<equation>f_{n}(x)</equation>在<equation>\left(\frac{1}{2},1\right)</equation>上单调增加，在<equation>\left(\frac{1}{2},1\right)</equation>上有且仅有一个零点，即方程<equation>x^{n}+x^{n-1}+\cdots+x=</equation>1（n为大于1的整数）在区间<equation>\left(\frac{1}{2},1\right)</equation>内有且仅有一个实根.

（Ⅱ）我们利用单调有界准则证明<equation>\lim x_{n}</equation>存在.

考虑<equation>f_{n + 1}(x) = x^{n + 1} + x^n + \dots + x - 1.</equation>对于任意的<equation>x\in\left(\frac{1}{2},1\right)</equation>，都有<equation>f_{n}(x) < f_{n+1}(x)</equation>. 若<equation>x_{n}</equation>为<equation>f_{n}(x)=0</equation>的根，<equation>x_{n+1}</equation>为<equation>f_{n+1}(x)=0</equation>的根，则<equation>f _ {n} \left(x _ {n + 1}\right) < f _ {n + 1} \left(x _ {n + 1}\right) = 0 = f _ {n} \left(x _ {n}\right).</equation>由于<equation>f_{n}(x)</equation>在<equation>\left(\frac{1}{2},1\right)</equation>上为单调增加函数，故<equation>x_{n + 1} < x_n</equation>，从而<equation>\{x_n\}</equation>单调减少.

由第（I）问知，对每一个大于1的整数n，<equation>f_{n}(x)</equation>的零点<equation>x_{n}</equation>都满足<equation>x_{n}\in \left(\frac{1}{2},1\right)</equation>，故<equation>\{x_{n}\}</equation>单调且有界.由单调有界准则知，<equation>\lim_{n\to \infty}x_{n}</equation>存在.

下面求<equation>\lim_{n\to \infty}x_{n}.</equation>由于<equation>x_{n}</equation>满足方程<equation>x^{n} + x^{n - 1} + \dots + x = 1</equation>，故由等比数列的求和公式得<equation>\frac {x _ {n} \left(1 - x _ {n} ^ {n}\right)}{1 - x _ {n}} = 1.</equation>记<equation>\lim_{n\to\infty}x_{n}=a.</equation>关注公众号：小小考研 获取更多考研资料

由于对所有大于2的整数n，都有<equation>\frac{1}{2} < x_{n} < x_{2} < 1</equation>，故<equation>0 \leqslant \lim _ {n \rightarrow \infty} x _ {n} ^ {n} \leqslant \lim _ {n \rightarrow \infty} x _ {2} ^ {n} = 0.</equation>令（1）式中的<equation>n\to \infty</equation>得，<equation>\frac{a}{1 - a} = 1.</equation>因此，<equation>a = \frac{1}{2}.</equation>

---

**2011年第3题 | 选择题 | 4分 | 答案: C**
3. 函数<equation>f ( x )=\ln | ( x-1 ) ( x-2 ) ( x-3 ) |</equation>的驻点个数为（    ）

A.0 B.1 C.2 D.3
答案: C
**解析: **（法一）由于<equation>f (x) = \ln | x - 1 | + \ln | x - 2 | + \ln | x - 3 |,</equation>故<equation>f ^ {\prime} (x) = \frac {1}{x - 1} + \frac {1}{x - 2} + \frac {1}{x - 3} = \frac {3 x ^ {2} - 1 2 x + 1 1}{(x - 1) (x - 2) (x - 3)}.</equation><equation>f^{\prime}(x) = 0</equation>的零点为<equation>3 x^{2}-1 2 x+1 1=0</equation>的根.由于该方程的判别式<equation>\Delta = (- 1 2) ^ {2} - 4 \times 1 1 \times 3 > 0,</equation>故该方程有2个不同的实根.

因此，<equation>f^{\prime}(x)</equation>有2个零点，<equation>f(x)</equation>的驻点个数为2.应选C.

（法二）本题可用罗尔定理结合多项式的零点个数与其次数的关系来判断 f(x)的驻点个数当<equation>x\neq1,2,3</equation>时，<equation>f ^ {\prime} (x) = \frac {\left[ (x - 1) (x - 2) (x - 3) \right] ^ {\prime}}{(x - 1) (x - 2) (x - 3)}.</equation>令<equation>g(x) = (x - 1)(x - 2)(x - 3)</equation>，则<equation>f^{\prime}(x)</equation>的零点个数与<equation>g^{\prime}(x)</equation>的零点个数相同.

g(x)有3个根，<equation>x=1,x=2</equation>和<equation>x=3</equation>.由罗尔定理知，<equation>g^{\prime}(x)</equation>在（1，2），（2，3）上各有1个零点.又因为 g(x)为三次多项式，<equation>g^{\prime}(x)</equation>为二次多项式，<equation>g^{\prime}(x)</equation>至多有2个零点，所以<equation>g^{\prime}(x)</equation>有且仅有2个零点，即<equation>f^{\prime}(x)</equation>有且仅有2个零点. f(x)的驻点个数为2.应选C.

---


#### 泰勒公式

**2021年第5题 | 选择题 | 5分 | 答案: D**
5. 设函数 f(x) = secx在 x=0处的2次泰勒多项式为<equation>1+a x+b x^{2}</equation>，则（    )

A. a=1,b=-<equation>\frac{1}{2}</equation>B. a=1,b=<equation>\frac{1}{2}</equation>C. a=0,b=-<equation>\frac{1}{2}</equation>D. a=0,b=<equation>\frac{1}{2}</equation>
答案: D
**解析: **解 依次计算<equation>\left. \sec x\right)^{\prime}\left|_{x=0},\left. \left. \sec x\right)^{\prime \prime}\right|_{x=0}.</equation><equation>\left. \left. \sec x\right)^{\prime}\right|_{x=0}=\sec x\tan x,</equation><equation>\left. \left. \sec x\right)^{\prime \prime}\right|_{x=0}=\left. \left. \sec x\tan x\right)^{\prime}\right|=\tan^{2}x\sec x+\sec^{3}x.</equation>代入<equation>x=0</equation>，可得<equation>\left. \left. \sec x\right)^{\prime}\right|_{x=0}=0, \left. \left. \left. \sec x\right)^{\prime \prime}\right|_{x=0}=1.</equation>因此，<equation>f(x)=\sec x</equation>在 x=0处的2次泰勒多项式为<equation>1+0\cdot x+\frac{1}{2}\cdot x^{2}=1+\frac{1}{2}x^{2}, a=0, b=\frac{1}{2}.</equation>应选D.

---


#### 函数的单调性、极值与最值

**2020年第6题 | 选择题 | 4分 | 答案: B**
6. 设函数<equation>f ( x )</equation>在区间[-2,2]上可导，且<equation>f^{\prime} ( x ) > f ( x ) > 0</equation>，则（    ）

A.<equation>\frac{f(-2)}{f(-1)}>1</equation>B.<equation>\frac{f(0)}{f(-1)}>e</equation>C.<equation>\frac{f(1)}{f(-1)}<\mathrm{e}^{2}</equation>D.<equation>\frac{f(2)}{f(-1)}<\mathrm{e}^{3}</equation>
答案: B
**解析: **解（法一）令<equation>F ( x )=\frac{f ( x )} {\mathrm{e}^{x}}</equation>，则<equation>F ^ {\prime} (x) = \frac {\mathrm {e} ^ {x} \left[ f ^ {\prime} (x) - f (x) \right]}{\mathrm {e} ^ {2 x}} = \frac {f ^ {\prime} (x) - f (x)}{\mathrm {e} ^ {x}} > 0.</equation>由此可知，F（x）单调增加.

由<equation>F ( 0 ) > F (- 1 )</equation>可得，<equation>\frac{f(0)}{1}>\frac{f(-1)}{e^{-1}}.</equation>由<equation>f ( x ) > 0</equation>可得<equation>\frac{f(0)}{f(-1)} > \mathrm{e}.</equation>因此，应选B.

下面说明其余选项均不正确.

根据 F(x)的单调性，应有<equation>F(-2) < F(-1) < F(0) < F(1) < F(2)</equation>，结合 f(x) > 0 可得<equation>\frac {f (- 2)}{f (- 1)} < \mathrm {e} ^ {- 1}, \quad \frac {f (1)}{f (- 1)} > \mathrm {e} ^ {2}, \quad \frac {f (2)}{f (- 1)} > \mathrm {e} ^ {3}.</equation>（法二）取<equation>f ( x )=\mathrm{e}^{2 x}</equation>，则<equation>f ( x )</equation>在<equation>[-2,2]</equation>上可导，且<equation>f^{\prime}(x)=2\mathrm{e}^{2x}>\mathrm{e}^{2x}=f(x)>0.</equation>选项A：<equation>\frac{f(-2)}{f(-1)}=\frac{\mathrm{e}^{-4}}{\mathrm{e}^{-2}}=\mathrm{e}^{-2}<1.</equation>选项B：<equation>\frac{f(0)}{f(-1)}=\frac{1}{e^{-2}}=e^{2}>e.</equation>选项C：<equation>\frac{f(1)}{f(-1)}=\frac{\mathrm{e}^{2}}{\mathrm{e}^{-2}}=\mathrm{e}^{4}>\mathrm{e}^{2}.</equation>选项D：<equation>\frac{f(2)}{f(-1)}=\frac{\mathrm{e}^{4}}{\mathrm{e}^{-2}}=\mathrm{e}^{6}>\mathrm{e}^{3}.</equation>由排除法可知，应选B.

---

**2019年第15题 | 解答题 | 10分**
15. (本题满分10分）

已知函数<equation>f ( x )=\left\{\begin{array}{ll}x^{2 x},&x>0,\\ x \mathrm{e}^{x}+1,&x\leqslant 0.\end{array} \right.</equation>求<equation>f^{\prime}(x)</equation>，并求 f(x)的极值.
**答案: **<equation>f^{\prime}(x)=\left\{\begin{array}{ll}\mathrm{e}^{x}(x+1),&x<0,\\ 2\mathrm{e}^{2x\ln x}(\ln x+1),&x>0.\end{array} \right.</equation>x=-1和 x =<equation>\frac{1} {\mathrm{e}}</equation>是 f(x)的极小值点，极小值分别为 f(-1) = 1 -<equation>\mathrm{e}^{-1}</equation>和<equation>f\left(\frac{1}{\mathrm{e}}\right)=\mathrm{e}^{-\frac{2}{\mathrm{e}}}</equation>；x=0是 f(x)的极大值点，极大值为 f(0) = 1.
**解析: **解 f(x)是一个分段函数. x=0是分界点.分别计算 x > 0时与 x < 0时的<equation>f^{\prime}(x).</equation>当 x > 0时，<equation>f ^ {\prime} (x) = \left(x ^ {2 x}\right) ^ {\prime} = \left(\mathrm {e} ^ {2 x \ln x}\right) ^ {\prime} = \mathrm {e} ^ {2 x \ln x} \cdot \left(2 \ln x + 2 x \cdot \frac {1}{x}\right) = 2 \mathrm {e} ^ {2 x \ln x} (\ln x + 1).</equation>当 x < 0时，<equation>f ^ {\prime} (x) = \mathrm {e} ^ {x} + x \mathrm {e} ^ {x} = \mathrm {e} ^ {x} (x + 1).</equation>计算<equation>f^{\prime}(0).</equation>由<equation>f ( x )</equation>的定义知<equation>f ( 0 )=1.</equation><equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0 ^ {-}} \frac {x \mathrm {e} ^ {x} + 1 - 1}{x} = \lim _ {x \rightarrow 0 ^ {-}} \mathrm {e} ^ {x} = 1.</equation><equation>\begin{aligned} f _ {+} ^ {\prime} (0) &= \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {2 x \ln x} - 1}{x} \frac {\mathrm {e} ^ {2 x \ln x} - 1 \sim 2 x \ln x}{\lim _ {x \rightarrow 0 ^ {+}} \frac {2 x \ln x}{x}} \\ &= 2 \lim _ {x \rightarrow 0 ^ {+}} \ln x = - \infty . \end{aligned}</equation>f(x)的右导数不存在，故f(x）在<equation>x=0</equation>处不可导.

因此，<equation>f^{\prime}(x) = \left\{ \begin{array}{ll} \mathrm{e}^{x}(x + 1), & x < 0, \\ 2\mathrm{e}^{2x\ln x}(\ln x + 1), & x > 0. \end{array} \right.</equation>考察 f（x）的极值，需分别考察 f（x）的驻点与不可导点.

令<equation>f^{\prime}(x)=0</equation>当 x > 0时，解得<equation>x=\frac{1} {\mathrm{e}}</equation>当 x < 0时，解得 x=-1.加上不可导点 x=0，这三个点将<equation>(-\infty, +\infty)</equation>分为4个区间.

当 x < -1时，<equation>f^{\prime}(x) < 0,f(x)</equation>单调减少.

当<equation>- 1 < x < 0</equation>时，<equation>f^{\prime}(x) > 0,f(x)</equation>单调增加.

当<equation>0 < x < \frac{1} {\mathrm{e}}</equation>时，<equation>f^{\prime}(x) < 0,f(x)</equation>单调减少.

当<equation>x > \frac{1} {\mathrm{e}}</equation>时，<equation>f^{\prime}(x) > 0,f(x)</equation>单调增加.

注意到 f(x)在 x=0处连续.于是，根据极值的第一充分条件，<equation>x=-1</equation>和<equation>x=\frac{1} {\mathrm{e}}</equation>是 f(x)的极小值点，极小值分别为<equation>f(-1)=1-\mathrm{e}^{-1}</equation>和<equation>f\left(\frac{1}{\mathrm{e}}\right)=\mathrm{e}^{-\frac{2}{\mathrm{e}}}</equation>；x=0是 f(x)的极大值点，极大值为<equation>f(0)=1.</equation>f（x）的单调性与极值可整理如下.

<table border="1"><tr><td>x</td><td><equation>(-\infty,-1)</equation></td><td>-1</td><td><equation>(-1,0)</equation></td><td>0</td><td><equation>(0,\frac{1}{e})</equation></td><td><equation>\frac{1}{e}</equation></td><td><equation>(\frac{1}{e},+\infty)</equation></td></tr><tr><td><equation>f^{\prime}(x)</equation></td><td>-</td><td>0</td><td>+</td><td>不存在</td><td>-</td><td>0</td><td>+</td></tr><tr><td><equation>f(x)</equation></td><td>单调减少</td><td>极小值</td><td>单调增加</td><td>极大值</td><td>单调减少</td><td>极小值</td><td>单调增加</td></tr></table>

---

**2017年第18题 | 解答题 | 10分**
18. (本题满分10分）

已知函数 y(x)由方程<equation>x^{3}+y^{3}-3 x+3 y-2=0</equation>确定，求 y(x）的极值.
**答案: **极大值 y（1）=1，极小值 y（-1）=0.
**解析: **解 对方程两端关于 x求导，得<equation>3 x ^ {2} + 3 y ^ {2} y ^ {\prime} - 3 + 3 y ^ {\prime} = 0.</equation>整理得<equation>\left(y ^ {2} + 1\right) y ^ {\prime} = 1 - x ^ {2}.</equation>由于<equation>y^{2}+1>0</equation>，故 y(x）的全部驻点为 x=1和 x=-1.

将 x=1代入方程<equation>x^{3}+y^{3}-3 x+3 y-2=0</equation>，得<equation>y^{3}+3 y-4=0</equation>. 通过观察发现 y=1是该方程的一个根.由于<equation>\frac{\mathrm{d}\left(y^{3}+3 y-4\right)}{\mathrm{d} y}=3 y^{2}+3>0</equation>，故<equation>y^{3}+3 y-4</equation>关于 y单调增加. y=1是<equation>y^{3}+3 y-4=0</equation>的唯一实根，<equation>y(1)=1.</equation>将 x=-1代入方程<equation>x^{3}+y^{3}-3 x+3 y-2=0</equation>，得<equation>y^{3}+3 y=0</equation>，即<equation>y \left(y^{2}+3\right)=0. y=0</equation>是该方程的唯一实根，<equation>y(-1)=0.</equation>下面用两种方法来判断驻点的极值点类型.

（法一）对（1）式两端关于 x求导，得<equation>\left(y ^ {2} + 1\right) y ^ {\prime \prime} + 2 y \left(y ^ {\prime}\right) ^ {2} = - 2 x.</equation>利用（2）式计算驻点<equation>x=\pm1</equation>处的二阶导数.

由于在驻点处，<equation>y^{\prime}=0</equation>，故当<equation>x=\pm 1</equation>时，<equation>\left(y ^ {2} + 1\right) y ^ {\prime \prime} = - 2 x.</equation>当 x=1时，(3)式化为<equation>2y^{\prime \prime}(1)=-2,y^{\prime \prime}(1)=-1<0</equation>；当 x=-1时，(3)式化为<equation>y^{\prime \prime}(-1)=2>0.</equation>因此，<equation>y(1)=1</equation>为极大值，<equation>y(-1)=0</equation>为极小值.

（法二）由（1）式可得<equation>y^{\prime}=\frac{1-x^{2}}{y^{2}+1}.</equation>注意到<equation>y^{2}+1</equation>恒大于零，故<equation>y^{\prime}(x)</equation>与y(x）的性质如下表.

<table border="1"><tr><td>x</td><td>(-∞,-1)</td><td>-1</td><td>(-1,1)</td><td>1</td><td>(1,+∞)</td></tr><tr><td>y&#x27;(x)</td><td>-</td><td>0</td><td>+</td><td>0</td><td>-</td></tr><tr><td>y(x)</td><td>单调减少</td><td>极小值</td><td>单调增加</td><td>极大值</td><td>单调减少</td></tr></table>

因此，<equation>y ( 1 ) = 1</equation>为极大值，<equation>y (- 1 ) = 0</equation>为极小值.

---

**2010年第15题 | 解答题 | 10分**
15. (本题满分10分)

求函数<equation>f ( x )=\int_{1}^{x^{2}}(x^{2}-t)\mathrm{e}^{-t^{2}}\mathrm{d} t</equation>的单调区间与极值.
**答案: **5) 单调增加区间为（-1，0）和（1，<equation>+ \infty</equation>），单调减少区间为（<equation>-\infty,-1</equation>）和（0，1）；极大值<equation>f(0)=\frac{1}{2}\left(1-\frac{1}{\mathrm{e}}\right)</equation>，极小值<equation>f(\pm 1)=0.</equation>
**解析: **解 先求<equation>f^{\prime}(x).</equation>由于在变限积分<equation>\int_{1}^{x^2}(x^2 - t)\mathrm{e}^{-t^2}\mathrm{d}t</equation>中，<equation>x</equation>不是积分变量，故可以把它提到积分号外.<equation>f (x) = \int_ {1} ^ {x ^ {2}} \left(x ^ {2} - t\right) \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t = x ^ {2} \int_ {1} ^ {x ^ {2}} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t - \int_ {1} ^ {x ^ {2}} t \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t.</equation>根据变限积分函数的求导公式以及求导的乘法法则，<equation>f ^ {\prime} (x) = 2 x \int_ {1} ^ {x ^ {2}} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t + 2 x ^ {3} \mathrm {e} ^ {- x ^ {4}} - 2 x ^ {3} \mathrm {e} ^ {- x ^ {4}} = 2 x \int_ {1} ^ {x ^ {2}} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t.</equation><equation>f^{\prime}(x) = 0</equation>当且仅当<equation>x = 0</equation>或<equation>\int_{1}^{x^{2}}\mathrm{e}^{-t^{2}}\mathrm{d}t = 0.</equation>由于<equation>\mathrm{e}^{-t^{2}}</equation>恒大于零，故当且仅当<equation>x^{2} = 1</equation>，即<equation>x = \pm 1</equation>时，<equation>\int_{1}^{x^{2}}\mathrm{e}^{-t^{2}}\mathrm{d}t = 0.</equation>因此，<equation>x = 0,\pm 1</equation>为<equation>f(x)</equation>的驻点.

对<equation>\int_{1}^{x^{2}}\mathrm{e}^{-t^{2}}\mathrm{d}t</equation>来说，当<equation>x^{2} < 1</equation>时，<equation>\int_{1}^{x^{2}}\mathrm{e}^{-t^{2}}\mathrm{d}t < 0</equation>；当<equation>x^{2} > 1</equation>时，<equation>\int_{1}^{x^{2}}\mathrm{e}^{-t^{2}}\mathrm{d}t > 0.</equation>因此有下表.

<table border="1"><tr><td>x</td><td>(-∞,-1)</td><td>-1</td><td>(-1,0)</td><td>0</td><td>(0,1)</td><td>1</td><td>(1,+∞)</td></tr><tr><td>f&#x27;(x)</td><td>-</td><td>0</td><td>+</td><td>0</td><td>-</td><td>0</td><td>+</td></tr><tr><td>f(x)</td><td>单调减少</td><td>极小值</td><td>单调增加</td><td>极大值</td><td>单调减少</td><td>极小值</td><td>单调增加</td></tr></table>

由此可知，<equation>f ( x )</equation>的单调增加区间为<equation>(-1,0)</equation>和<equation>( 1,+\infty)</equation>；<equation>f ( x )</equation>的单调减少区间为<equation>(-\infty,-1)</equation>和(0，1)；<equation>f (-1)</equation>和f（1）为<equation>f ( x )</equation>的极小值，<equation>f (- 1) = f (1) = \int_ {1} ^ {1} (1 - t) \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t = 0;</equation>f（0）为f（x）的极大值，<equation>f (0) = \int_ {1} ^ {0} (- t) \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t = \frac {1}{2} \left(1 - \frac {1}{\mathrm {e}}\right).</equation>

---

**2009年第13题 | 填空题 | 4分**
13. 函数<equation>y=x^{2x}</equation>在区间 (0,1] 上的最小值为 ___
**答案: **# -<equation>\frac{2}{e}</equation>
**解析: **解 先求<equation>y^{\prime}</equation>. 由于<equation>y = x^{2x}</equation>是幂指函数，故可采用对数求导法.

在（0,1]上，<equation>y=x^{2x}>0.</equation>对<equation>y=x^{2x}</equation>两端取对数，得<equation>\ln y = 2x\ln x.</equation>对该式两端关于<equation>x</equation>求导得<equation>\frac {y ^ {\prime}}{y} = 2 x \cdot \frac {1}{x} + 2 \ln x = 2 (\ln x + 1),</equation>即<equation>y^{\prime} = 2(\ln x + 1)y = 2(\ln x + 1)x^{2x}</equation>.

由于在（0，1]上，<equation>x^{2 x}>0</equation>，故<equation>y^{\prime}</equation>的零点仅当<equation>\ln x+1=0</equation>时取得，此时<equation>x=\frac{1}{e}</equation>.于是，当<equation>0 < x < \frac{1}{e}</equation>时，<equation>\ln x+1<0, y^{\prime}<0, y</equation>单调减少；当<equation>\frac{1}{e} < x \leqslant 1</equation>时，<equation>\ln x+1>0, y^{\prime}>0, y</equation>单调增加.

因此，函数<equation>y=x^{2 x}</equation>在区间（0，1]上的最小值在<equation>x=\frac{1}{e}</equation>处取得，此时<equation>y=\left(\mathrm{e}^{-1}\right)^{\frac{2}{e}}=\mathrm{e}^{-\frac{2}{e}}.</equation>

---


#### 不等式的证明

**2018年第18题 | 解答题 | 10分**
18. (本题满分10分）

已知常数<equation>k\geqslant \ln 2-1</equation>. 证明：<equation>(x-1)(x-\ln^{2}x+2k\ln x-1)\geqslant 0.</equation>
**解析: **证记<equation>f ( x )=x-\ln^{2} x+2 k \ln x-1</equation>，则<equation>f ( 1 )=0</equation><equation>f ^ {\prime} (x) = 1 - \frac {2 \ln x}{x} + \frac {2 k}{x} = \frac {x - 2 \ln x + 2 k}{x}.</equation>由于在（0，<equation>+\infty</equation>）内，<equation>x > 0</equation>，故若能证明<equation>x - 2\ln x + 2k</equation>在（0，<equation>+\infty</equation>）内非负，则<equation>f^{\prime}(x)</equation>在（0，<equation>+\infty</equation>）内非负，从而<equation>f(x)</equation>在（0，<equation>+\infty</equation>）内单调增加.

考虑函数 g（x）=x-2lnx.<equation>g ^ {\prime} (x) = 1 - \frac {2}{x}.</equation>当<equation>x=2</equation>时，<equation>g^{\prime}(x)=0</equation>；当<equation>0 < x < 2</equation>时，<equation>g^{\prime}(x)<0</equation>，<equation>g(x)</equation>单调减少；当<equation>x > 2</equation>时，<equation>g^{\prime}(x)>0</equation>，<equation>g(x)</equation>单调增加.于是，<equation>g(x)</equation>在<equation>x=2</equation>处取得（0，<equation>+\infty</equation>）内的最小值，最小值为<equation>g(2)=2-2\ln 2.</equation>当 k<equation>\geqslant\ln2-1</equation>时，<equation>2-2\ln2+2k\geqslant0</equation>，从而 x-2<equation>\ln x+2k</equation>在（0，<equation>+\infty</equation>）内非负且仅当 x=2,k=<equation>\ln2-1</equation>时等于零.因此，在（0，<equation>+\infty</equation>）<equation>\backslash\{2\}</equation>内，<equation>f^{\prime}(x)>0</equation><equation>f(x)</equation>在（0，<equation>+\infty</equation>）内单调增加.又因为 f(1)=0，所以当 0 < x < 1时，<equation>f(x)<0</equation>当 x >1时，<equation>f(x)>0</equation>从而 f(x)与 x-1在（0，<equation>+\infty</equation>）内同号.

由于 f(x)与 x-1在（0，+∞）内同号，故（x-1）f(x）≥0，即（x-1）（x-<equation>\ln^{2}x+2k\ln x-1）\geqslant0.</equation>

---

**2012年第20题 | 解答题 | 11分**
20. (本题满分10分)

证明：<equation>x\ln \frac{1+x}{1-x}+\cos x\geqslant 1+\frac{x^{2}}{2}(-1<x<1)</equation>
**答案: **## （20）证明略.
**解析: **证（法一）考虑辅助函数<equation>f ( x )=x \ln \frac{1+x}{1-x}+\cos x-1-\frac{x^{2}}{2}.</equation><equation>f (- x) = (- x) \ln \frac {1 - x}{1 + x} + \cos x - 1 - \frac {x ^ {2}}{2} = f (x),</equation>故 f(x)为偶函数.如果能证明当 x<equation>\in[0,1)</equation>时，<equation>f(x)\geqslant0</equation>，那么当 x<equation>\in(-1,1)</equation>时，也有 f(x)<equation>\geqslant0</equation>从而题给不等式成立.

计算<equation>f^{\prime}(x).</equation><equation>f ^ {\prime} (x) = \left(x \ln \frac {1 + x}{1 - x} + \cos x - 1 - \frac {x ^ {2}}{2}\right) ^ {\prime} = \frac {2 x}{1 - x ^ {2}} + \ln \frac {1 + x}{1 - x} - \sin x - x.</equation>由于当<equation>x\in[0,1)</equation>时，<equation>\frac{x}{1-x^{2}}\geqslant x\geqslant\sin x</equation>，故<equation>\frac {2 x}{1 - x ^ {2}} \geqslant 2 x \geqslant \sin x + x,</equation>等号在<equation>x = 0</equation>时取得. 又因为<equation>\frac{1 + x}{1 - x}\geqslant 1</equation>，所以<equation>\ln \frac{1 + x}{1 - x}\geqslant 0</equation>，等号在<equation>x = 0</equation>时取得.

因此，当 x<equation>\in</equation>（0,1）时，<equation>f ^ {\prime} (x) = \frac {2 x}{1 - x ^ {2}} + \ln \frac {1 + x}{1 - x} - \sin x - x > 0.</equation>综上所述，<equation>f ( x )</equation>在[0，1）上单调增加，<equation>f ( 0 )</equation>为<equation>f ( x )</equation>在[0，1）上的最小值.又由<equation>f ( x )</equation>为偶函数可知，在（-1，1）上，<equation>f ( x ) \geqslant f ( 0 ) = 0</equation>即<equation>x \ln \frac{1+x}{1-x}+\cos x\geqslant 1+\frac{x^{2}}{2}(-1<x<1).</equation>（法二）在法一中求得<equation>f^{\prime}(x)=\frac{2x}{1-x^{2}}+\ln \frac{1+x}{1-x}-\sin x-x</equation>后，继续求<equation>f^{\prime\prime}(x)</equation>以判断<equation>f^{\prime}(x)</equation>的性质.<equation>f ^ {\prime \prime} (x) = \frac {2 \left(1 + x ^ {2}\right)}{\left(1 - x ^ {2}\right) ^ {2}} + \frac {1}{1 + x} - \frac {(- 1)}{1 - x} - \cos x - 1 = \frac {4}{\left(1 - x ^ {2}\right) ^ {2}} - \cos x - 1.</equation>由于当 x<equation>\in[0,1)</equation>时，<equation>\frac {4}{\left(1 - x ^ {2}\right) ^ {2}} \geqslant 4, \quad 1 + \cos x \leqslant 2,</equation>故<equation>f^{\prime \prime}(x) > 0. f^{\prime}(x)</equation>在[0，1）上单调增加，<equation>f^{\prime}(x)\geqslant f^{\prime}(0)=0,f(x)</equation>在[0，1）上单调增加.

（法三）首先，<equation>f ( x ) = x \ln \frac { 1 + x } { 1 - x } + \cos x</equation>为偶函数，<equation>g ( x ) = 1 + \frac { x^{2}}{2}</equation>也为偶函数，故我们只需证明，在（0，1）上，<equation>f ( x ) \geqslant g ( x )</equation>，并且<equation>f ( 0 ) = g ( 0 )</equation>，便能得到在（-1，1）上，<equation>f ( x ) \geqslant g ( x )</equation>由泰勒中值定理，<equation>\cos x=1-\frac{x^{2}}{2!}+\frac{\cos \xi}{4!} x^{4},\xi</equation>为介于0和x之间的某个值.于是，当<equation>x\in(0,1)</equation>时，<equation>\cos x\geqslant 1-\frac{x^{2}}{2}.</equation>从而<equation>f (x) = x \ln \frac {1 + x}{1 - x} + \cos x \geqslant x \ln \frac {1 + x}{1 - x} + 1 - \frac {x ^ {2}}{2}.</equation>若能证明<equation>x\ln \frac{1+x}{1-x}+1-\frac{x^{2}}{2}\geqslant 1+\frac{x^{2}}{2}</equation>，则由不等号的传递性可知原不等式得证.

由于当<equation>x\in(0,1)</equation>时，<equation>x \ln \frac {1 + x}{1 - x} + 1 - \frac {x ^ {2}}{2} \geqslant 1 + \frac {x ^ {2}}{2} \Leftrightarrow x \ln \frac {1 + x}{1 - x} \geqslant x ^ {2} \Leftrightarrow \ln \frac {1 + x}{1 - x} \geqslant x,</equation>故我们只需要证明<equation>\ln \frac{1+x}{1-x}\geqslant x.</equation>考虑<equation>\varphi(x)=\ln \frac{1+x}{1-x}-x.</equation><equation>\varphi^ {\prime} (x) = \frac {1}{1 + x} - \frac {(- 1)}{1 - x} - 1 = \frac {2}{1 - x ^ {2}} - 1.</equation>当<equation>x\in (0,1)</equation>时，<equation>\frac{2}{1 - x^2}\geqslant 2</equation>，从而<equation>\varphi^{\prime}(x) = \frac{2}{1 - x^2} -1 > 0,\varphi(x)</equation>在（0，1）上单调增加，<equation>\varphi(x)\geqslant \varphi(0) = 0.</equation>综上所述，原不等式成立.

---


### 函数、极限、连续


#### 无穷小量

**2025年第4题 | 选择题 | 5分 | 答案: C**

4. 设函数 f(x)，g(x)在 x=0的某去心邻域内有定义且恒不为零，若当<equation>x \rightarrow 0</equation>时，f(x)是 g(x)的高阶无穷小，则当<equation>x \rightarrow 0</equation>时（    )

A.<equation>f(x)+g(x)=o\left(g(x)\right)</equation>B.<equation>f(x)g(x)=o\left(f^{2}(x)\right)</equation>C.<equation>f(x)=o\left(\mathrm{e}^{g(x)}-1\right)</equation>D.<equation>f(x)=o\left(g^{2}(x)\right)</equation>

答案: C

**解析:**解 由于当<equation>x\to 0</equation>时，<equation>f(x)</equation>是<equation>g(x)</equation>的高阶无穷小，故<equation>\lim_{x\to 0}\frac{f(x)}{g(x)} = 0.</equation>于是，<equation>\lim _ {x \rightarrow 0} \frac {f (x) + g (x)}{g (x)} = 1 + \lim _ {x \rightarrow 0} \frac {f (x)}{g (x)} = 1,</equation><equation>\lim _ {x \rightarrow 0} \frac {f (x) g (x)}{f ^ {2} (x)} = \lim _ {x \rightarrow 0} \frac {g (x)}{f (x)} = \infty ,</equation><equation>\lim _ {x \rightarrow 0} \frac {f (x)}{\mathrm {e} ^ {g (x)} - 1} \xrightarrow {\mathrm {e} ^ {g (x)} - 1 - g (x)} \lim _ {x \rightarrow 0} \frac {f (x)}{g (x)} = 0.</equation>由此可得，选项A、B不正确，选项C正确.

对选项D，取<equation>f ( x )=x^{2}, g ( x )=x</equation>，则<equation>\lim_{x\to 0}\frac{f(x)}{g^{2}(x)}=1\neq0</equation>，选项D不正确因此，应选C.

---

**2023年第3题 | 选择题 | 5分 | 答案: B**

3. 已知数列<equation>\{x_{n}\}</equation><equation>\{y_{n}\}</equation>满足<equation>x_{1}=y_{1}=\frac{1}{2},x_{n+1}=\sin x_{n},y_{n+1}=y_{n}^{2}(n=1,2,\cdots)</equation>，则当 n<equation>\to\infty</equation>时，（    ）

A.<equation>x_{n}</equation>是<equation>y_{n}</equation>的高阶无穷小 B.<equation>y_{n}</equation>是<equation>x_{n}</equation>的高阶无穷小

C.<equation>x_{n}</equation>是<equation>y_{n}</equation>的等价无穷小 D.<equation>x_{n}</equation>是<equation>y_{n}</equation>的同阶但非等价无穷小

答案: B

**解析:**解（法一）首先证明对任意正整数<equation>n,x_{n}\in (0,1)</equation>.

当<equation>n=1</equation>时，<equation>x_{1}=\frac{1}{2}\in(0,1).</equation>假设<equation>x_{n}\in(0,1)</equation>，则<equation>x_{n+1}=\sin x_{n}\in(0,1).</equation>由数学归纳法可知对任意正整数 n，<equation>x_{n}\in(0,1).</equation>由<equation>\sin x</equation>的泰勒公式可知，存在<equation>\xi_{n}\in(0,x_{n})</equation>，使得<equation>x _ {n + 1} = \sin x _ {n} = x _ {n} - \frac {\cos \xi_ {n}}{6} x _ {n} ^ {3} > x _ {n} - \frac {x _ {n} ^ {3}}{6} > \frac {x _ {n}}{2}.</equation>于是，<equation>x _ {n} > \frac {1}{2} x _ {n - 1} > \left(\frac {1}{2}\right) ^ {2} x _ {n - 2} > \dots > \left(\frac {1}{2}\right) ^ {n - 1} x _ {1} = \left(\frac {1}{2}\right) ^ {n}.</equation>由<equation>y_{1} = \frac{1}{2}, y_{n + 1} = y_{n}^{2}</equation>可知<equation>y_{n} = y_{n - 1}^{2} = y_{n - 2}^{4} = \dots = y_{1}^{2^{n - 1}} = \left(\frac{1}{2}\right)^{2^{n - 1}}.</equation>因此，<equation>0 < \frac {y _ {n}}{x _ {n}} < \frac {\left(\frac {1}{2}\right) ^ {2 ^ {n - 1}}}{\left(\frac {1}{2}\right) ^ {n}} = \left(\frac {1}{2}\right) ^ {2 ^ {n - 1} - n}.</equation>由于<equation>\lim_{n\to \infty}\left(\frac{1}{2}\right)^{2^{n-1}-n}=0</equation>，故由夹逼准则可知，<equation>\lim_{n\to \infty}\frac{y_{n}}{x_{n}}=0.</equation>综上所述，当<equation>n\to\infty</equation>时，<equation>y_{n}</equation>是<equation>x_{n}</equation>的高阶无穷小，应选B.

（法二）首先我们证明，在<equation>\left( 0, \frac{\pi}{2} \right)</equation>内，<equation>\sin x > \frac{2}{\pi} x</equation>即<equation>\frac{\sin x}{x} > \frac{2}{\pi}.</equation>令<equation>f ( x )=\frac{\sin x}{x}, x \in\left(0,\frac{\pi}{2}\right)</equation>，则<equation>f^{\prime}(x)=\frac{x\cos x-\sin x}{x^{2}}.</equation>注意到<equation>f^{\prime}(x)</equation>的分母恒大于0，故考虑分子的符号.

令<equation>g ( x )=x \cos x-\sin x,x \in\left(0, \frac{\pi}{2}\right)</equation>，则<equation>g^{\prime}(x)=\cos x-x \sin x-\cos x=-x \sin x<0</equation>，于是，<equation>g ( x )</equation>在<equation>\left(0, \frac{\pi}{2}\right)</equation>内单调减少.结合<equation>g ( 0 )=0</equation>，可得<equation>g ( x )<0</equation>，从而<equation>f^{\prime}(x)</equation>在<equation>\left(0, \frac{\pi}{2}\right)</equation>内小于0，<equation>f ( x )</equation>在<equation>\left(0, \frac{\pi}{2}\right)</equation>内单调减少.因此，当<equation>x \in\left(0, \frac{\pi}{2}\right)</equation>时，<equation>f ( x )>f \left( \frac{\pi}{2} \right)=\frac{2}{\pi}</equation>即<equation>\frac{\sin x}{x}>\frac{2}{\pi}.</equation>由法一可知，对任意正整数 n，<equation>x_{n}\in(0,1)\subset\left(0,\frac{\pi}{2}\right)</equation>，从而由前面的分析可得<equation>x _ {n + 1} = \sin x _ {n} > \frac {2}{\pi} x _ {n}.</equation>下面我们证明，对任意正整数<equation>n, y_{n}\in \left[0,\frac{1}{2}\right]</equation>，从而<equation>y_{n + 1} = y_n^2 \leqslant \frac{1}{2} y_n.</equation>当 n=1时，<equation>y_{1}=\frac{1}{2}\in\left[0,\frac{1}{2}\right].</equation>假设<equation>y_{n}\in\left[0,\frac{1}{2}\right]</equation>，则<equation>y_{n+1}=y_{n}^{2}\in\left[0,\frac{1}{2}\right].</equation>由数学归纳法可知对任意正整数n，<equation>y_{n}\in\left[0,\frac{1}{2}\right],</equation>从而<equation>y_{n+1}=y_{n}^{2}\leqslant \frac{1}{2} y_{n}.</equation>因此，<equation>0 < \frac {y _ {n}}{x _ {n}} < \frac {\frac {1}{2} y _ {n - 1}}{\frac {2}{\pi} x _ {n - 1}} = \frac {\pi}{4} \cdot \frac {y _ {n - 1}}{x _ {n - 1}} < \frac {\pi}{4} \cdot \frac {\frac {1}{2} y _ {n - 2}}{\frac {2}{\pi} x _ {n - 2}} = \left(\frac {\pi}{4}\right) ^ {2} \frac {y _ {n - 2}}{x _ {n - 2}} < \dots = \left(\frac {\pi}{4}\right) ^ {n - 1} \frac {y _ {1}}{x _ {1}} = \left(\frac {\pi}{4}\right) ^ {n - 1}.</equation>由于<equation>\lim_{n\rightarrow\infty}\left(\frac{\pi}{4}\right)^{n-1}=0</equation>，故由夹逼准则可知，<equation>\lim_{n\rightarrow\infty}\frac{y_{n}}{x_{n}}=0.</equation>综上所述，当<equation>n\to\infty</equation>时，<equation>y_{n}</equation>是<equation>x_{n}</equation>的高阶无穷小，应选B.

---

**2022年第1题 | 选择题 | 5分 | 答案: C**

1. 当<equation>x\to0</equation>时，<equation>\alpha(x),\beta(x)</equation>是非零无穷小量，则以下的命题中：<equation>\textcircled{1}</equation>若<equation>\alpha(x)\sim\beta(x)</equation>，则<equation>\alpha^{2}(x)\sim\beta^{2}(x)</equation><equation>\textcircled{2}</equation>若<equation>\alpha^{2}(x)\sim\beta^{2}(x)</equation>，则<equation>\alpha(x)\sim\beta(x)</equation><equation>\textcircled{3}</equation>若<equation>\alpha(x)\sim\beta(x)</equation>，则<equation>\alpha(x)-\beta(x)=o(\alpha(x))</equation><equation>\textcircled{4}</equation>若<equation>\alpha(x)-\beta(x)=o(\alpha(x))</equation>，则<equation>\alpha(x)\sim\beta(x)</equation>真命题的序号为（    ）

A.<equation>\textcircled{1}\textcircled{3}</equation>B.<equation>\textcircled{1}\textcircled{4}</equation>C.<equation>\textcircled{1}\textcircled{3}\textcircled{4}</equation>D.<equation>\textcircled{2}\textcircled{3}\textcircled{4}</equation>

答案: C

**解析:**解 依次分析四个命题.

若<equation>\alpha(x)\sim\beta(x)</equation>，则<equation>\lim_{x\to0}\frac{\alpha(x)}{\beta(x)}=1</equation>，从而<equation>\lim_{x\to0}\frac{\alpha^{2}(x)}{\beta^{2}(x)}=1</equation>，即<equation>\alpha^{2}(x)\sim\beta^{2}(x).</equation>命题<equation>\textcircled{1}</equation>是真命题由<equation>\alpha^{2}(x)\sim\beta^{2}(x)</equation>并不能得到<equation>\alpha(x)\sim\beta(x).</equation>考虑<equation>\beta(x)=-\alpha(x)</equation>，则<equation>\lim_{x\to0}\frac{\alpha^{2}(x)}{\beta^{2}(x)}=\lim_{x\to0}\frac{\alpha^{2}(x)}{\alpha^{2}(x)}= 1</equation>，即<equation>\alpha^{2}(x)\sim\beta^{2}(x)</equation>，但<equation>\lim_{x\to0}\frac{\alpha(x)}{\beta(x)}=\lim_{x\to0}\frac{\alpha(x)}{- \alpha(x)}=-1, \alpha(x)</equation>与<equation>\beta(x)</equation>只是同阶但并不等价的无穷小量命题<equation>\textcircled{2}</equation>不是真命题.

要说明<equation>\alpha ( x )-\beta ( x )=o( \alpha ( x ) )</equation>，只需说明<equation>\lim_{x\to 0}\frac{\alpha ( x )-\beta ( x )}{\alpha ( x )}=0.</equation><equation>\lim _ {x \rightarrow 0} \frac {\alpha (x) - \beta (x)}{\alpha (x)} = 1 - \lim _ {x \rightarrow 0} \frac {\beta (x)}{\alpha (x)} \frac {\alpha (x) \sim \beta (x)}{1 - 1} 1 - 1 = 0.</equation>命题<equation>\textcircled{3}</equation>是真命题.

要说明<equation>\alpha ( x )\sim \beta ( x )</equation>，只需说明<equation>\lim_{x\to 0}\frac{\beta ( x )}{\alpha ( x )}=1.</equation><equation>\lim _ {x \rightarrow 0} \frac {\beta (x)}{\alpha (x)} = \lim _ {x \rightarrow 0} \frac {\alpha (x) - [ \alpha (x) - \beta (x) ]}{\alpha (x)} = 1 - \lim _ {x \rightarrow 0} \frac {\alpha (x) - \beta (x)}{\alpha (x)} = 1 - 0 = 1.</equation>命题<equation>\textcircled{4}</equation>是真命题.

综上所述，应选C.

---

**2021年第1题 | 选择题 | 5分 | 答案: C**

1. 当<equation>x \rightarrow 0</equation>时，<equation>\int_{0}^{x^{2}}(\mathrm{e}^{t^{3}}-1)\mathrm{d}t</equation>是<equation>x^{7}</equation>的（    ）

A. 低阶无穷小 B. 等价无穷小

C. 高阶无穷小 D. 同阶但非等价无穷小

答案: C

**解析:**解 计算<equation>\lim_{x\to 0}\frac{\int_{0}^{x^{2}}(\mathrm{e}^{t^{3}}-1)\mathrm{d}t}{x^{7}}</equation>来比较这两个无穷小量的阶.<equation>\lim _ {x \rightarrow 0} \frac {\int_ {0} ^ {x ^ {2}} \left(\mathrm {e} ^ {t ^ {3}} - 1\right) \mathrm {d} t}{x ^ {7}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\left(\mathrm {e} ^ {x ^ {6}} - 1\right) \cdot 2 x}{7 x ^ {6}} \xlongequal {\text {e} ^ {x ^ {6}} - 1 \sim x ^ {6}} \lim _ {x \rightarrow 0} \frac {x ^ {6} \cdot 2 x}{7 x ^ {6}} = 0.</equation>因此，<equation>\int_{0}^{x^{2}}(\mathrm{e}^{t^{3}}-1)\mathrm{d}t</equation>是<equation>x^{7}</equation>的高阶无穷小.应选C.

---

**2020年第1题 | 选择题 | 4分 | 答案: D**

1.<equation>x \rightarrow 0^{+}</equation>时，下列无穷小量中最高阶是（    ）

A.<equation>\int_{0}^{x} \left( \mathrm{e}^{t^{2}}-1 \right) \mathrm{d} t</equation>B.<equation>\int_{0}^{x} \ln(1+\sqrt{t^{3}}) \mathrm{d} t</equation>C.<equation>\int_{0}^{\sin x} \sin t^{2} \mathrm{d} t</equation>D.<equation>\int_{0}^{1-\cos x} \sqrt{\sin^{3} t} \mathrm{d} t</equation>

答案: D

**解析:**解 由于求一次导，无穷小量的阶数降低1，且选项A、B的积分上、下限相同，故比较这两项的无穷小量的阶的大小，可以转化为比较它们的被积函数的阶。又因为<equation>t\to 0^{+}</equation>时，<equation>\mathrm{e}^{t^{2}}-1\sim t^{2},</equation><equation>\ln(1+\sqrt{t^{3}})\sim t^{\frac{3}{2}}</equation>，所以<equation>\int_{0}^{x}\left(\mathrm{e}^{t^{2}}-1\right)\mathrm{d}t</equation>与<equation>x^{3}</equation>同阶，比<equation>\int_{0}^{x}\ln(1+\sqrt{t^{3}})\mathrm{d}t</equation>高阶.

比较<equation>\int_{0}^{\sin x}\sin t^{2}\mathrm{d}t</equation>与<equation>x^{3}</equation>的阶.<equation>\begin{aligned} \lim _ {x \rightarrow 0 ^ {+}} \frac {\int_ {0} ^ {\sin x} \sin t ^ {2} \mathrm {d} t}{x ^ {3}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sin (\sin x) ^ {2} \cdot \cos x}{3 x ^ {2}} &= \frac {1}{3} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sin (\sin x) ^ {2}}{x ^ {2}} \xlongequal {\frac {\sin u \sim u}{u \rightarrow 0}} \frac {1}{3} \lim _ {x \rightarrow 0 ^ {+}} \frac {(\sin x) ^ {2}}{x ^ {2}} \\ &= \frac {1}{3} \lim _ {x \rightarrow 0 ^ {+}} \left(\frac {\sin x}{x}\right) ^ {2} \xlongequal {\sin x \sim x} \frac {1}{3}. \end{aligned}</equation>于是，<equation>\int_{0}^{\sin x}\sin t^{2}\mathrm{d}t</equation>也与<equation>x^{3}</equation>同阶.

比较<equation>\int_{0}^{1-\cos x}\sqrt{\sin^{3}t}\mathrm{d}t</equation>与<equation>x^{3}</equation>的阶.<equation>\begin{aligned} \lim _ {x \rightarrow 0 ^ {+}} \frac {\int_ {0} ^ {1 - \cos x} \sqrt {\sin^ {3} t} \mathrm {d} t}{x ^ {3}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sqrt {\sin^ {3} (1 - \cos x)} \sin x}{3 x ^ {2}} \xlongequal {\sin x \sim x} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sin^ {\frac {3}{2}} (1 - \cos x)}{3 x} \\ &= \lim _ {x \rightarrow 0 ^ {+}} \frac {\sin^ {\frac {3}{2}} (1 - \cos x)}{(1 - \cos x) ^ {\frac {3}{2}}} \cdot \frac {(1 - \cos x) ^ {\frac {3}{2}}}{3 x} \\ \frac {1 - \cos x \sim \frac {x ^ {2}}{2}}{} {\lim _ {x \rightarrow 0 ^ {+}} \left[ \frac {\sin (1 - \cos x)}{1 - \cos x} \right] ^ {\frac {3}{2}} \cdot \frac {\left(\frac {x ^ {2}}{2}\right) ^ {\frac {3}{2}}}{3 x}} \\ &= 1 \times 0 = 0. \end{aligned}</equation>因此，<equation>\int_{0}^{1-\cos x}\sqrt{\sin^{3}t}\mathrm{d}t</equation>比<equation>x^{3}</equation>高阶，从而比选项A、B、C中的无穷小量均高阶.应选D.

---

**2016年第1题 | 选择题 | 4分 | 答案: B**

1. 设<equation>\alpha_{1}=x(\cos \sqrt{x}-1),\alpha_{2}=\sqrt{x}\ln(1+\sqrt[3]{x}),\alpha_{3}=\sqrt[3]{x+1}-1</equation>.当<equation>x\rightarrow 0^{+}</equation>时，以上3个无穷小量按照从低阶到高阶的排序是（    ）

A.<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>B.<equation>\alpha_{2},\alpha_{3},\alpha_{1}</equation>C.<equation>\alpha_{2},\alpha_{1},\alpha_{3}</equation>D.<equation>\alpha_{3},\alpha_{2},\alpha_{1}</equation>

答案: B

**解析:**解 由于当<equation>x\to 0^{+}</equation>时，<equation>\cos \sqrt {x} - 1 \sim - \frac {1}{2} (\sqrt {x}) ^ {2} = - \frac {x}{2}, \ln \left(1 + \sqrt [ 3 ]{x}\right) \sim \sqrt [ 3 ]{x}, \sqrt [ 3 ]{x + 1} - 1 = (x + 1) ^ {\frac {1}{3}} - 1 \sim \frac {x}{3},</equation>故<equation>\alpha_ {1} = x \left(\cos \sqrt {x} - 1\right) \sim x \cdot \left(- \frac {x}{2}\right) = - \frac {x ^ {2}}{2}, \quad \alpha_ {2} = \sqrt {x} \ln \left(1 + \sqrt [ 3 ]{x}\right) \sim x ^ {\frac {1}{2}} \cdot x ^ {\frac {1}{3}} = x ^ {\frac {5}{6}},</equation><equation>\alpha_ {3} = \sqrt [ 3 ]{x + 1} - 1 \sim \frac {x}{3}.</equation>比较<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>的阶，只需要比较与<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>等价的<equation>-\frac{x^{2}}{2},x^{\frac{5}{6}},\frac{x}{3}</equation>中 x的次数，次数越高，无穷小量的阶越高.

因此，正确的排序（阶从低到高）应当为<equation>\alpha_{2},\alpha_{3},\alpha_{1}</equation>应选B.

---

**2013年第1题 | 选择题 | 4分 | 答案: C**

1. 设<equation>\cos x-1=x\sin \alpha (x)</equation>，其中<equation>|\alpha (x)|<\frac{\pi}{2}</equation>，则当 x→0时，<equation>\alpha (x)</equation>是（    )

A. 比 x 高阶的无穷小量 B. 比 x 低阶的无穷小量

C. 与 x 同阶但不等价的无穷小量 D. 与 x 等价的无穷小量

答案: C

**解析:**解 首先说明<equation>\alpha(x)</equation>是<equation>x\rightarrow0</equation>时的无穷小量.<equation>\lim _ {x \rightarrow 0} \frac {\sin \alpha (x)}{x} = \lim _ {x \rightarrow 0} \frac {\cos x - 1}{x ^ {2}} \xlongequal {\cos x - 1 \sim - \frac {1}{2} x ^ {2}} \lim _ {x \rightarrow 0} \frac {- \frac {1}{2} x ^ {2}}{x ^ {2}} = - \frac {1}{2}.</equation>由于<equation>\lim_{x\to 0}\frac{\sin \alpha (x)}{x} = -\frac{1}{2}</equation>，而分母 x趋于零，故必有<equation>\lim_{x\to 0}\sin \alpha (x) = 0.</equation>又由于<equation>|\alpha (x)| < \frac{\pi}{2},\sin x</equation>在<equation>\left(-\frac{\pi}{2},\frac{\pi}{2}\right)</equation>上有连续的反函数<equation>arcsin x</equation>，从而<equation>\lim _ {x \rightarrow 0} \alpha (x) = \lim _ {x \rightarrow 0} \arcsin [ \sin \alpha (x) ] = 0.</equation><equation>\alpha (x)</equation>是<equation>x\to 0</equation>时的无穷小量，<equation>\sin \alpha (x)\sim \alpha (x)(x\to 0)</equation>.

因此，<equation>\lim_{x\to 0}\frac{\alpha (x)}{x}\frac{\sin \alpha (x)\sim \alpha (x)}{=}\lim_{x\to 0}\frac{\sin \alpha (x)}{x}=-\frac{1}{2},\alpha (x)</equation>是与<equation>x</equation>同阶但不等价的无穷小量.应选C.

---


#### 函数的连续性与间断点的类型

**2024年第1题 | 选择题 | 5分 | 答案: C**
1. 函数<equation>f ( x )=\left| x \right|^{\frac{1}{(1-x)(x-2)}}</equation>的第一类间断点的个数是（    )

A.3 B.2 C.1 D.0
答案: C
**解析: **解<equation>f(x)</equation>的间断点为<equation>x = 0, x = 1, x = 2</equation>，分别计算这三个点处的左、右极限.由于<equation>f(x) = \mathrm{e}^{\frac{\ln|x|}{(1 - x)(x - 2)}}</equation>，故<equation>\lim f(x) = \lim \mathrm{e}^{\frac{\ln|x|}{(1 - x)(x - 2)}} = \mathrm{e}^{\lim \frac{\ln|x|}{(1 - x)(x - 2)}}</equation>.并且，<equation>\lim _ {x \rightarrow 0 ^ {-}} \frac {\ln (- x)}{(1 - x) (x - 2)} = - \frac {1}{2} \lim _ {x \rightarrow 0 ^ {-}} \ln (- x) = + \infty ,</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {\ln x}{(1 - x) (x - 2)} = - \frac {1}{2} \lim _ {x \rightarrow 0 ^ {+}} \ln x = + \infty ,</equation><equation>\lim _ {x \rightarrow 1 ^ {-}} \frac {\ln x}{(1 - x) (x - 2)} = - \lim _ {x \rightarrow 1 ^ {-}} \frac {\ln x}{1 - x} \xlongequal {\text {洛必达}} - \lim _ {x \rightarrow 1 ^ {-}} \frac {1 / x}{- 1} = 1,</equation><equation>\lim _ {x \rightarrow 1 ^ {+}} \frac {\ln x}{(1 - x) (x - 2)} = - \lim _ {x \rightarrow 1 ^ {+}} \frac {\ln x}{1 - x} \xlongequal {\text {洛必达}} - \lim _ {x \rightarrow 1 ^ {+}} \frac {1 / x}{- 1} = 1,</equation><equation>\lim _ {x \rightarrow 2 ^ {-}} \frac {\ln x}{(1 - x) (x - 2)} = - \ln 2 \lim _ {x \rightarrow 2 ^ {-}} \frac {1}{x - 2} = + \infty ,</equation><equation>\lim _ {x \rightarrow 2 ^ {+}} \frac {\ln x}{(1 - x) (x - 2)} = - \ln 2 \lim _ {x \rightarrow 2 ^ {+}} \frac {1}{x - 2} = - \infty ,</equation>故<equation>\lim_{x\to 0}f(x)=+\infty, \lim_{x\to 1^{-}}f(x)=\lim_{x\to 1^{+}}f(x)=\mathrm{e}, \lim_{x\to 2^{-}}f(x)=+\infty, \lim_{x\to 2^{+}}f(x)=0. x=1</equation>为<equation>f(x)</equation>的可去间断点，<equation>x=0,x=2</equation>为<equation>f(x)</equation>的无穷间断点.

因此，仅有<equation>x = 1</equation>为<equation>f(x)</equation>的第一类间断点，应选C.

---

**2020年第2题 | 选择题 | 4分 | 答案: C**
2. 函数<equation>f(x)=\frac{\mathrm{e}^{\frac{1}{x-1}}\ln|1+x|}{(\mathrm{e}^{x}-1)(x-2)}</equation>的第二类间断点的个数为（    )

A.1 B.2 C.3 D.4
答案: C
**解析: **解 从 f(x)的表达式可以看出，<equation>x=-1,x=0,x=1,x=2</equation>为 f(x)的间断点.下面分别计算这些点处的左、右极限.<equation>\lim _ {x \rightarrow - 1} f (x) = \lim _ {x \rightarrow - 1} \frac {\mathrm {e} ^ {\frac {1}{x - 1}} \ln | 1 + x |}{\left(\mathrm {e} ^ {x} - 1\right) (x - 2)} = \frac {\mathrm {e} ^ {- \frac {1}{2}}}{\left(\mathrm {e} ^ {- 1} - 1\right) \cdot (- 3)} \lim _ {x \rightarrow - 1} \ln | 1 + x | = \infty .</equation><equation>\lim _ {x \rightarrow 0} f (x) = \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {\frac {1}{x - 1}} \ln | 1 + x |}{\left(\mathrm {e} ^ {x} - 1\right) (x - 2)} = \frac {\mathrm {e} ^ {- 1}}{- 2} \lim _ {x \rightarrow 0} \frac {\ln | 1 + x |}{\mathrm {e} ^ {x} - 1} \frac {\frac {\ln | 1 + x | \sim x}{\mathrm {e} ^ {x} - 1 \sim x}}{- \frac {1}{2 \mathrm {e}} \lim _ {x \rightarrow 0} \frac {x}{x}} = - \frac {1}{2 \mathrm {e}}.</equation><equation>\lim _ {x \rightarrow 1 ^ {+}} f (x) = \lim _ {x \rightarrow 1 ^ {+}} \frac {\mathrm {e} ^ {\frac {1}{x - 1}} \ln | 1 + x |}{\left(\mathrm {e} ^ {x} - 1\right) (x - 2)} = - \frac {\ln 2}{\mathrm {e} - 1} \lim _ {x \rightarrow 1 ^ {+}} \mathrm {e} ^ {\frac {1}{x - 1}} = \infty .</equation><equation>\lim _ {x \rightarrow 2} f (x) = \lim _ {x \rightarrow 2} \frac {\mathrm {e} ^ {\frac {1}{x - 1}} \ln | 1 + x |}{\left(\mathrm {e} ^ {x} - 1\right) (x - 2)} = \frac {\mathrm {e} \ln 3}{\mathrm {e} ^ {2} - 1} \lim _ {x \rightarrow 2} \frac {1}{x - 2} = \infty .</equation>因此，<equation>x=-1,x=1</equation>和 x=2均为 f(x)的无穷间断点，从而也是第二类间断点. f(x)共有3个第二类间断点.应选C.

---

**2018年第3题 | 选择题 | 4分 | 答案: D**
3. 设函数 f(x) =<equation>\left\{\begin{array}{l l} - 1, & x < 0, \\ 1, & x \geqslant 0, \end{array} \right.</equation>g(x) =<equation>\left\{\begin{array}{l l} 2 - a x, & x \leqslant - 1, \\ x, & - 1 < x < 0, \\ x - b, & x \geqslant 0. \end{array} \right.</equation>若 f(x) + g(x)在R上连续，则（    )

A. a=3,b=1 B. a=3,b=2 C. a=-3,b=1 D. a=-3,b=2
答案: D
**解析: **解 当<equation>x\leqslant -1</equation>时，<equation>f(x)+g(x)=-1+(2-ax)=1-ax.</equation>当<equation>- 1 < x < 0</equation>时，<equation>f ( x )+g ( x )=-1+x.</equation>当<equation>x\geqslant0</equation>时，<equation>f(x)+g(x)=1+(x-b)=1-b+x.</equation>于是，<equation>f ( x ) + g ( x ) = \left\{ \begin{array}{ll} 1 - a x, & x \leqslant - 1, \\ - 1 + x, & - 1 < x < 0, \\ 1 - b + x, & x \geqslant 0. \end{array} \right.</equation>由于<equation>f ( x )+g ( x )</equation>在R上连续，故<equation>f ( x )+g ( x )</equation>在<equation>x=-1</equation>和<equation>x=0</equation>处均连续.

因为<equation>\lim_{x\rightarrow -1^{+}}[f(x)+g(x)]=\lim_{x\rightarrow -1^{+}}(-1+x)=-2</equation>，而<equation>\left.[f(x)+g(x)]\right|_{x=-1}=1+a</equation>，所以 1+a=-2，即 a=-3.

又因为<equation>\lim_{x\rightarrow 0^{-}}[f(x)+g(x)]=\lim_{x\rightarrow 0^{-}}(-1+x)=-1</equation>，而<equation>[f(x)+g(x)]\bigg|_{x=0}=1-b</equation>，所以 1-b=-1，即 b=2.

因此，a=-3，b=2.应选D.

---

**2017年第1题 | 选择题 | 4分 | 答案: A**
1. 若函数 f(x)<equation>\left\{\begin{array}{l l}{\frac{1-\cos \sqrt{x}}{ax},}&{x>0,}\\ {b,}&{x\leqslant 0}\end{array}\right.</equation>在 x=0处连续，则（    )

A.<equation>a b=\frac{1}{2}</equation>B.<equation>a b=-\frac{1}{2}</equation>C.<equation>a b=0</equation>D.<equation>a b=2</equation>
答案: A
**解析: **解 f(x)是分段函数.代入 f(x)在<equation>(-\infty, 0]</equation>和<equation>(0, +\infty)</equation>上的表达式，分别计算<equation>\lim_{x\rightarrow 0^{+}}f(x),</equation><equation>\lim_{x\rightarrow 0^{+}}f(x).</equation><equation>\lim _ {x \rightarrow 0 ^ {-}} f (x) = f (0) = b,</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} f (x) = \lim _ {x \rightarrow 0 ^ {+}} \frac {1 - \cos \sqrt {x}}{a x} \frac {1 - \cos \sqrt {x} \sim \frac {1}{2} (\sqrt {x}) ^ {2}}{\overline {{=}}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {x}{2}}{a x} = \frac {1}{2 a}.</equation>因此，<equation>b=\frac{1}{2a}</equation>，即<equation>a b=\frac{1}{2}.</equation>应选A.

---

**2015年第2题 | 选择题 | 4分 | 答案: B**
2. 函数<equation>f ( x )=\lim_{t\rightarrow 0}\left( 1+\frac{\sin t}{x}\right)^{\frac{x^{2}}{t}}</equation>在<equation>(-\infty, +\infty)</equation>内（    ）

A. 连续 B. 有可去间断点 C. 有跳跃间断点 D. 有无穷间断点
答案: B
**解析: **解 由<equation>f ( x )</equation>的表达式可以看出，<equation>f ( x )</equation>在<equation>x=0</equation>处无定义.

当<equation>x\neq 0</equation>时，<equation>f(x) = \lim_{t\to 0}\left(1 + \frac{\sin t}{x}\right)^{\frac{x^2}{t}}.</equation>下面我们用两种方法计算<equation>\lim_{t\to 0}\left(1 + \frac{\sin t}{x}\right)^{\frac{x^2}{t}}.</equation>（法一）凑重要极限.<equation>\lim _ {t \rightarrow 0} \left(1 + \frac {\sin t}{x}\right) ^ {\frac {x ^ {2}}{t}} = \lim _ {t \rightarrow 0} \left[ \left(1 + \frac {\sin t}{x}\right) ^ {\frac {x}{\sin t}} \right] ^ {\frac {x \sin t}{t}} = \mathrm {e} ^ {\lim _ {t \rightarrow 0} \frac {x \sin t}{t}} \xlongequal {\sin t \sim t} \mathrm {e} ^ {x}.</equation>（法二）取对数.<equation>\lim_{t \to 0} \left(1 + \frac{\sin t}{x}\right)^{\frac{x^{2}}{t}} = \lim_{t \to 0} \left[\left(1 + \frac{\sin t}{x}\right)^{\frac{x}{\sin t}}\right]^{\frac{x \sin t}{t}} = \mathrm{e}^{\lim_{t \to 0} \frac{x \sin t}{t}} \xlongequal{\sin t \sim t} \mathrm{e}^{x}.</equation>于是，当<equation>x\neq 0</equation>时，<equation>f(x) = \mathrm{e}^{x},\lim_{x\to 0}f(x) = \mathrm{e}^{0} = 1.</equation>因此，<equation>x = 0</equation>为<equation>f(x)</equation>的可去间断点.应选B.

---

**2010年第1题 | 选择题 | 4分 | 答案: B**
1. 函数<equation>f ( x )=\frac{x^{2}-x}{x^{2}-1}\sqrt{1+\frac{1}{x^{2}}}</equation>的无穷间断点的个数为（    ）

A.0 B.1 C.2 D.3
答案: B
**解析: **解 简化 f(x).<equation>f (x) = \frac {x (x - 1)}{(x + 1) (x - 1)} \sqrt {1 + \frac {1}{x ^ {2}}} = \frac {x}{x + 1} \sqrt {1 + \frac {1}{x ^ {2}}}.</equation>考虑<equation>x\to 0</equation>时的情况.因为<equation>\lim _ {x \rightarrow 0} \left(\frac {x}{x + 1} \sqrt {1 + \frac {1}{x ^ {2}}}\right) = \lim _ {x \rightarrow 0} \left(x \sqrt {1 + \frac {1}{x ^ {2}}}\right) = \lim _ {x \rightarrow 0} \left(\frac {x}{| x |} \sqrt {x ^ {2} + 1}\right),</equation>所以，<equation>\lim _ {x \rightarrow 0 ^ {-}} f (x) = \lim _ {x \rightarrow 0 ^ {-}} \left[ \frac {x}{(- x)} \sqrt {x ^ {2} + 1} \right] = - 1, \quad \lim _ {x \rightarrow 0 ^ {+}} f (x) = \lim _ {x \rightarrow 0 ^ {+}} \left(\frac {x}{x} \sqrt {x ^ {2} + 1}\right) = 1.</equation>因此，<equation>x = 0</equation>为<equation>f(x)</equation>的跳跃间断点.

考虑 x→1时的情况.<equation>\lim _ {x \rightarrow 1} f (x) = \lim _ {x \rightarrow 1} \left(\frac {x}{x + 1} \sqrt {1 + \frac {1}{x ^ {2}}}\right) = \frac {\sqrt {2}}{2}.</equation>因此，<equation>x = 1</equation>为<equation>f(x)</equation>的可去间断点.

考虑 x -> -1时的情况.<equation>\lim _ {x \rightarrow - 1} f (x) = \lim _ {x \rightarrow - 1} \left(\frac {x}{x + 1} \sqrt {1 + \frac {1}{x ^ {2}}}\right) = \lim _ {x \rightarrow - 1} \frac {- \sqrt {2}}{x + 1} = \infty .</equation>因此，<equation>x = -1</equation>为<equation>f(x)</equation>的无穷间断点.

综上所述，<equation>f ( x )</equation>的无穷间断点的个数为1.应选B.

---

**2009年第1题 | 选择题 | 4分 | 答案: C**
1. 函数<equation>f(x)=\frac{x-x^{3}}{\sin \pi x}</equation>的可去间断点的个数为（    ）

A.1 B.2 C.3 D.无穷多个
答案: C
**解析: **解 因为当 k为整数时，<equation>\sin k\pi=0</equation>，所以 f(x)在 x=k（k为整数）时无定义，在其余点连续.当<equation>k-k^{3}\neq0</equation>时，即 k≠0，<equation>\pm1</equation>时，<equation>\lim _ {x \rightarrow k} \frac {x - x ^ {3}}{\sin \pi x} = \infty .</equation>x=k为f(x）的无穷间断点.

当<equation>k - k^{3} = 0</equation>时，即<equation>k = 0,\pm 1</equation>时，<equation>\lim_{x\to k}f(x)</equation>为<equation>\frac{0}{0}</equation>型未定式，可用洛必达法则求极限.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {x - x ^ {3}}{\sin \pi x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - 3 x ^ {2}}{\pi \cos \pi x} &= \frac {1}{\pi}, \\ \lim _ {x \rightarrow 1} \frac {x - x ^ {3}}{\sin \pi x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 1} \frac {1 - 3 x ^ {2}}{\pi \cos \pi x} &= \frac {- 2}{- \pi} = \frac {2}{\pi}, \\ \lim _ {x \rightarrow - 1} \frac {x - x ^ {3}}{\sin \pi x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow - 1} \frac {1 - 3 x ^ {2}}{\pi \cos \pi x} &= \frac {- 2}{- \pi} = \frac {2}{\pi}. \end{aligned}</equation>因此，<equation>f ( x )</equation>共有3个可去间断点，<equation>x=0</equation><equation>\pm 1.</equation>应选C.

---


#### 数列敛散性的判定

**2024年第4题 | 选择题 | 5分 | 答案: D**
4. 已知数列<equation>\left\{a_{n}\right\} \left(a_{n}\neq0\right)</equation>，若<equation>\left\{a_{n}\right\}</equation>发散，则（    )

A.<equation>\left\{a_{n}+\frac{1}{a_{n}}\right\}</equation>发散 B.<equation>\left\{a_{n}-\frac{1}{a_{n}}\right\}</equation>发散 C.<equation>\left\{\mathrm{e}^{a_{n}}+\frac{1}{\mathrm{e}^{a_{n}}}\right\}</equation>发散 D.<equation>\left\{\mathrm{e}^{a_{n}}-\frac{1}{\mathrm{e}^{a_{n}}}\right\}</equation>发散
答案: D
**解析: **解考虑函数<equation>f ( x )=\mathrm{e}^{x}-\frac{1}{\mathrm{e}^{x}}</equation>，则<equation>f^{\prime}(x)=\mathrm{e}^{x}+\mathrm{e}^{-x}>0</equation>，故<equation>f ( x )</equation>是在<equation>(-\infty , +\infty)</equation>上单调增加的连续函数，从而存在反函数<equation>f^{-1}(x), f^{-1}(x)</equation>也是在<equation>(-\infty , +\infty)</equation>上单调增加的连续函数.

记<equation>b_{n} = \mathrm{e}^{a_{n}} - \frac{1}{\mathrm{e}^{a_{n}}}</equation>，即<equation>b_{n} = f\left(a_{n}\right)</equation>，于是，<equation>a_{n} = f^{-1}\left(f\left(a_{n}\right)\right) = f^{-1}\left(b_{n}\right)</equation>. 若<equation>\{b_{n}\}</equation>收敛，即存在<equation>b</equation>，使得<equation>\lim_{n\to \infty}b_n = b</equation>，则<equation>\lim _ {n \rightarrow \infty} a _ {n} = \lim _ {n \rightarrow \infty} f ^ {- 1} \left(b _ {n}\right) = f ^ {- 1} \left(\lim _ {n \rightarrow \infty} b _ {n}\right) = f ^ {- 1} (b).</equation>由此可得，<equation>\lim_{n\to \infty}a_n</equation>存在.但这与<equation>\{a_n\}</equation>发散矛盾.

因此，<equation>\{b_{n}\}</equation>发散，即<equation>\left\{\mathrm{e}^{a_n} - \frac{1}{\mathrm{e}^{a_n}}\right\}</equation>发散，应选D.

下面说明选项 A、B、C 均不正确.

对选项A，取<equation>a_{n} = \left\{ \begin{array}{ll} 2, & n = 2k - 1, \\ \frac{1}{2}, & n = 2k, \end{array} \right.</equation><equation>k = 1,2,\dots</equation>，则<equation>\{a_{n}\}</equation>发散，但<equation>a_{n} + \frac{1}{a_{n}}\equiv 2 + \frac{1}{2} = \frac{5}{2},</equation><equation>\left\{a_{n} + \frac{1}{a_{n}}\right\}</equation>收敛.

对选项B、C，取<equation>a_{n} = (-1)^{n}</equation>，则<equation>\left\{a_{n}\right\}</equation>发散，但<equation>a_{n}-\frac{1}{a_{n}}\equiv 0,\mathrm{e}^{a_{n}}+\frac{1}{\mathrm{e}^{a_{n}}}\equiv \mathrm{e}+\frac{1}{\mathrm{e}},\left\{a_{n}-\frac{1}{a_{n}}\right\},</equation><equation>\left\{\mathrm{e}^{a_{n}}+\frac{1}{\mathrm{e}^{a_{n}}}\right\}</equation>均收敛.

---

**2022年第6题 | 选择题 | 5分 | 答案: D**
6. 设数列<equation>\{x_{n}\}</equation>满足<equation>-\frac{\pi}{2}\leqslant x_{n}\leqslant \frac{\pi}{2}</equation>，则（    )

A. 若<equation>\lim_{n\rightarrow \infty}\cos(\sin x_{n})</equation>存在，则<equation>\lim_{n\rightarrow \infty}x_{n}</equation>存在

B. 若<equation>\lim_{n\rightarrow \infty}\sin(\cos x_{n})</equation>存在，则<equation>\lim_{n\rightarrow \infty}x_{n}</equation>存在

C. 若<equation>\lim_{n\rightarrow \infty}\cos(\sin x_{n})</equation>存在，则<equation>\lim_{n\rightarrow \infty}\sin x_{n}</equation>存在，但<equation>\lim_{n\rightarrow \infty}x_{n}</equation>不一定存在

D. 若<equation>\lim_{n\rightarrow \infty}\sin(\cos x_{n})</equation>存在，则<equation>\lim_{n\rightarrow \infty}\cos x_{n}</equation>存在，但<equation>\lim_{n\rightarrow \infty}x_{n}</equation>不一定存在
答案: D
**解析: **解 若<equation>\lim_{n\rightarrow \infty}\sin(\cos x_{n})</equation>存在，则将其记为 a.由于<equation>\sin x</equation>在<equation>\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>上存在反函数<equation>\arcsin x</equation>，故<equation>\lim_{n\rightarrow \infty}\cos x_{n}=\lim_{n\rightarrow \infty}\arcsin(\sin(\cos x_{n}))=\arcsin(\lim_{n\rightarrow \infty}\sin(\cos x_{n}))=\arcsin a.</equation>但是<equation>\lim_{n\rightarrow \infty}\cos x_{n}</equation>存在并不能保证<equation>\lim_{n\rightarrow \infty}x_{n}</equation>存在.例如取<equation>x_{n}=(-1)^{n}\frac{\pi}{2}</equation>，则<equation>\lim_{n\rightarrow \infty}\cos x_{n}=0</equation>，但<equation>\lim_{n\rightarrow \infty}x_{n}</equation>不存在.选项B错误，选项D正确.应选D.

由于<equation>\cos x</equation>在<equation>\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>上并不单调，故由<equation>\lim_{n\to \infty}\cos(\sin x_{n})</equation>存在并不能保证<equation>\lim_{n\to \infty}\sin x_{n}</equation>存在.同样取<equation>x_{n}=(-1)^{n}\frac{\pi}{2}</equation>，则<equation>\lim_{n\to \infty}\cos(\sin x_{n})=\cos1</equation>，但<equation>\lim_{n\to \infty}\sin x_{n}</equation>和<equation>\lim_{n\to \infty}x_{n}</equation>均不存在.选项A、C不正确.

---

**2018年第21题 | 解答题 | 11分**
21. (本题满分11分）

设数列<equation>\{x_{n}\}</equation>满足：<equation>x_{1}>0,x_{n}\mathrm{e}^{x_{n+1}}=\mathrm{e}^{x_{n}}-1(n=1,2,\cdots).</equation>证明<equation>\{x_{n}\}</equation>收敛，并求<equation>\lim_{n\rightarrow \infty}x_{n}.</equation>
**答案: **证明略，<equation>\lim_{n\to\infty}x_{n}=0.</equation>
**解析: **解 由<equation>x_{n}\mathrm{e}^{x_{n + 1}} = \mathrm{e}^{x_{n}} - 1(n = 1,2,\dots)</equation>可得，<equation>x _ {n + 1} = \ln \left(\frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n}}\right).</equation>先用数学归纳法证明对所有的正整数 n，都有<equation>x_{n} > 0.</equation>首先，<equation>x_{1} > 0.</equation>假设当<equation>n = k</equation>时，<equation>x_{k} > 0.</equation>注意到当<equation>x > 0</equation>时，<equation>\mathrm{e}^{x} - 1 > x</equation>，从而<equation>\frac{\mathrm{e}^{x} - 1}{x} > 1.</equation>于是，<equation>x _ {k + 1} = \ln \left(\frac {\mathrm {e} ^ {x _ {k}} - 1}{x _ {k}}\right) > \ln 1 = 0.</equation>由数学归纳法可知，对所有的正整数 n，都有<equation>x_{n} > 0.</equation>因此，数列<equation>\{x_{n}\}</equation>有下界.

下面用两种方法证明数列<equation>\{x_{n}\}</equation>单调减少，即<equation>x_{n+1} < x_{n}</equation>（<equation>n=1,2,\dots).</equation>（法一）由<equation>x_{n}\mathrm{e}^{x_{n+1}}=\mathrm{e}^{x_{n}}-1</equation>可知，<equation>\mathrm {e} ^ {x _ {n + 1}} = \frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n}} = \frac {\mathrm {e} ^ {x _ {n}} - \mathrm {e} ^ {0}}{x _ {n} - 0} \frac {\text {拉 格 朗 日}}{\text {中 值 定 理}} \mathrm {e} ^ {\xi_ {n}},</equation>其中<equation>\xi_{n}\in (0,x_{n})</equation>由于<equation>\mathrm{e}^{x}</equation>单调增加，故由<equation>\mathrm{e}^{x_{n+1}}=\mathrm{e}^{\xi_{n}}<\mathrm{e}^{x_{n}}</equation>可得<equation>x_{n+1}<x_{n}</equation>，即数列<equation>\left\{x_{n}\right\}</equation>单调减少.

（法二）<equation>x _ {n + 1} - x _ {n} = \ln \left(\frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n}}\right) - x _ {n} = \ln \left(\frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n} \mathrm {e} ^ {x _ {n}}}\right).</equation>记<equation>f ( x )=\mathrm{e}^{x}-1-x\mathrm{e}^{x}</equation>，则<equation>f^{\prime}(x)=\mathrm{e}^{x}-\mathrm{e}^{x}-x\mathrm{e}^{x}=-x\mathrm{e}^{x}.</equation>当 x > 0时，<equation>f^{\prime}(x) < 0,f(x)</equation>在<equation>[0,+\infty)</equation>上单调减少，于是，<equation>f(x) < f(0)=0.</equation>从而，当 x > 0时，<equation>\frac {\mathrm {e} ^ {x} - 1}{x \mathrm {e} ^ {x}} - 1 = \frac {\mathrm {e} ^ {x} - 1 - x \mathrm {e} ^ {x}}{x \mathrm {e} ^ {x}} < 0,</equation>即<equation>\frac{\mathrm{e}^{x}-1}{x\mathrm{e}^{x}}<1.</equation>又因为对所有的正整数<equation>n</equation>，都有<equation>x_{n} > 0</equation>，所以<equation>\ln \left(\frac{\mathrm{e}^{x_n} - 1}{x_n\mathrm{e}^{x_n}}\right) < \ln 1 = 0</equation>，即<equation>x_{n + 1} - x_n < 0.</equation>因此，数列<equation>\left\{x_{n}\right\}</equation>单调减少.

由单调有界准则可知，数列<equation>\{x_{n}\}</equation>收敛.由于对所有的正整数n，都有<equation>x_{n} > 0</equation>，故<equation>\lim_{n\to \infty}x_{n}=a\geqslant 0.</equation>对<equation>x_{n}\mathrm{e}^{x_{n+1}}=\mathrm{e}^{x_{n}}-1</equation>两端同时令<equation>n\to \infty</equation>，可得<equation>a\mathrm{e}^{a}=\mathrm{e}^{a}-1.</equation>由前面的结果可知，<equation>x=0</equation>是<equation>f(x)=\mathrm{e}^{x}-1-x\mathrm{e}^{x}</equation>在<equation>[0,+\infty)</equation>上的唯一零点.因此，<equation>a=0</equation>即<equation>\lim_{n\to \infty}x_{n}=0.</equation>

---

**2013年第20题 | 解答题 | 11分**
20. (本题满分11分)

设函数<equation>f ( x )=\ln x+\frac{1}{x}.</equation>I. 求 f(x)的最小值;

II. 设数列<equation>\{x_{n}\}</equation>满足<equation>\ln x_{n}+\frac{1}{x_{n+1}}<1</equation>，证明<equation>\lim_{n\to\infty}x_{n}</equation>存在，并求此极限.
**答案: **(20) ( I ) 1;

（Ⅱ）证明略，<equation>\lim_{n\to \infty}x_n = 1.</equation>
**解析: **解（I）首先，<equation>f ( x )</equation>的定义域为（0，<equation>+ \infty</equation>）.计算<equation>f^{\prime}(x)</equation>得<equation>f^{\prime}(x)=\frac{1}{x}-\frac{1}{x^{2}}=\frac{x-1}{x^{2}}.</equation>当 x=1时，<equation>f^{\prime}(x)=0</equation>，故 x=1为 f(x)的驻点；当 x>1时，<equation>f^{\prime}(x)>0</equation>，f(x)单调增加；当 0 < x < 1时，<equation>f^{\prime}(x)<0</equation>，f(x)单调减少.

因此，<equation>f ( x )</equation>的最小值为<equation>f ( 1 )=1.</equation>（Ⅱ）若能证明<equation>\{x_{n}\}</equation>单调且有界，则能证明<equation>\lim_{n\to \infty}x_{n}</equation>存在.

由第（Ⅰ）问的结论及第（Ⅱ）问的条件，<equation>f \left(x _ {n}\right) = \ln x _ {n} + \frac {1}{x _ {n}} \geqslant 1 > \ln x _ {n} + \frac {1}{x _ {n + 1}},</equation>故<equation>\frac{1}{x_{n}} >\frac{1}{x_{n+1}}.</equation>由题设，<equation>\{x_{n}\}</equation>应为正项数列，故由<equation>\frac{1}{x_{n}} >\frac{1}{x_{n+1}}</equation>可得<equation>x_{n} < x_{n+1}</equation>即<equation>\{x_{n}\}</equation>单调增加.

由<equation>\ln x_{n} + \frac{1}{x_{n + 1}} < 1</equation>得，<equation>\ln x_{n} < 1 - \frac{1}{x_{n + 1}}</equation>，即<equation>x _ {n} < \mathrm {e} ^ {\left(1 - \frac {1}{x _ {n + 1}}\right)} < \mathrm {e},</equation>故<equation>\left\{x_{n}\right\}</equation>单调增加且有上界.

因此，由单调有界准则知，<equation>\lim_{n\to\infty}x_{n}</equation>存在.

记<equation>\lim_{n\to \infty}x_n = a</equation>，则<equation>a\geqslant x_{1} > 0.</equation>对不等式<equation>\ln x_{n} + \frac{1}{x_{n + 1}} < 1</equation>两端取极限得<equation>\ln a + \frac {1}{a} \leqslant 1.</equation>又由第（I）问得，<equation>\ln a + \frac{1}{a}\geqslant 1</equation>，故<equation>\ln a + \frac{1}{a} = 1</equation>，此时<equation>a = 1</equation>，即<equation>\lim_{n\to \infty}x_n = 1.</equation>

---

**2012年第3题 | 选择题 | 4分 | 答案: B**
3. 设<equation>a_{n} > 0</equation>（<equation>n=1,2,\cdots</equation>），<equation>S_{n}=a_{1}+a_{2}+\cdots+a_{n}</equation>，则数列<equation>\{S_{n}\}</equation>有界是数列<equation>\{a_{n}\}</equation>收敛的（    ）

A. 充分必要条件 B. 充分非必要条件

C. 必要非充分条件 D. 既非充分也非必要条件
答案: B
**解析: **由于<equation>S _ {n} - S _ {n - 1} = a _ {n} > 0 (n = 2, 3, \dots),</equation>故数列<equation>\left\{S_{n}\right\}</equation>单调增加.

若数列<equation>\{S_{n}\}</equation>有界，则由单调有界准则可知<equation>\{S_{n}\}</equation>收敛.记<equation>\lim_{n\to \infty}S_{n}=S.</equation>于是<equation>\lim _ {n \rightarrow \infty} a _ {n} = \lim _ {n \rightarrow \infty} \left(S _ {n} - S _ {n - 1}\right) = S - S = 0.</equation>因此，数列<equation>\left\{S_{n}\right\}</equation>有界是数列<equation>\left\{a_{n}\right\}</equation>收敛的充分条件.

但数列<equation>\left\{S_{n}\right\}</equation>有界并不是数列<equation>\left\{a_{n}\right\}</equation>收敛的必要条件.考虑数列<equation>a_{n}=1 ( n=1, 2, \cdots), \lim_{n\to \infty} a_{n}=1</equation>但<equation>S_{n}=n.</equation>数列<equation>\left\{S_{n}\right\}</equation>无上界.

因此，应选B.

---

**2011年第19题 | 解答题 | 10分**
19. (本题满分10分)

I. 证明：对任意的正整数 n, 都有<equation>\frac{1}{n+1}<\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}</equation>成立；

II. 设<equation>a_{n}=1+\frac{1}{2}+\cdots+\frac{1}{n}-\ln n</equation>（<equation>n=1,2,\cdots</equation>），证明数列<equation>\left\{a_{n}\right\}</equation>收敛.
**答案: **（19）（Ⅰ）证明略；

（Ⅱ）证明略.
**解析: **证（I）（法一）考虑函数<equation>f ( x )=\ln x</equation>，则<equation>f^{\prime}(x)=\frac{1}{x}.</equation>由拉格朗日中值定理，对任意的正整数n，都存在<equation>\xi_{n}\in(n,n+1)</equation>，使得<equation>\ln \left(1 + \frac {1}{n}\right) = f (n + 1) - f (n) = f ^ {\prime} \left(\xi_ {n}\right) = \frac {1}{\xi_ {n}}.</equation>又因为<equation>\xi_{n}\in (n,n + 1)</equation>，所以<equation>\frac{1}{n + 1} < \frac{1}{\xi_n} < \frac{1}{n}</equation>因此，对任意的正整数 n，都有<equation>\frac{1}{n+1}<\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}</equation>成立.

（法二）分别证明<equation>\frac{1}{n + 1} < \ln \left(1 + \frac{1}{n}\right)</equation>和<equation>\ln \left(1 + \frac{1}{n}\right) < \frac{1}{n}</equation>.

为证明<equation>\ln \left(1 + \frac{1}{n}\right) < \frac{1}{n}</equation>，可考虑函数<equation>f(x) = \ln (1 + x) - x.</equation><equation>f^{\prime}(x)=\frac{1}{1+x}-1.</equation>当<equation>x > 0</equation>时，<equation>f^{\prime}(x)<0</equation>，故<equation>f(x)</equation>在<equation>[0,+\infty)</equation>上单调减少. 又由于<equation>f(0)=0</equation>故对任意的正整数n，<equation>f\left(\frac{1}{n}\right)<f(0)=0</equation>即<equation>\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}.</equation>为证明<equation>\frac{1}{n+1} < \ln \left( 1+\frac{1}{n} \right)</equation>，可考虑函数<equation>g(x)=\ln(1+x)-\frac{x}{1+x}.</equation><equation>g ^ {\prime} (x) = \frac {1}{1 + x} - \frac {(1 + x) - x}{(1 + x) ^ {2}} = \frac {x}{(1 + x) ^ {2}}.</equation>当 x > 0时，<equation>g^{\prime}(x) > 0</equation>，故 g(x)在<equation>[0,+\infty)</equation>上单调增加.又由于<equation>g(0)=0</equation>，故对任意的正整数n，<equation>g\left(\frac{1}{n}\right)>g(0)=0</equation>，即<equation>\frac{1}{n+1}<\ln \left(1+\frac{1}{n}\right).</equation>综上所述，对任意的正整数 n，都有<equation>\frac{1}{n+1}<\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}</equation>成立.

（法三）注意到<equation>\ln \left( 1+\frac{1}{n} \right)=\int_{n}^{n+1} \frac{1}{x}\mathrm{d}x.</equation>由于<equation>\int_ {n} ^ {n + 1} \frac {1}{n + 1} \mathrm {d} x < \int_ {n} ^ {n + 1} \frac {1}{x} \mathrm {d} x < \int_ {n} ^ {n + 1} \frac {1}{n} \mathrm {d} x,</equation>故<equation>\frac {1}{n + 1} < \ln \left(1 + \frac {1}{n}\right) < \frac {1}{n}.</equation>（Ⅱ）若能证明数列<equation>\left\{a_{n}\right\}</equation>单调且有界，则由单调有界准则知其收敛先证<equation>\left\{a_{n}\right\}</equation>单调.

对任意的正整数<equation>n = 1,2,3,\dots</equation><equation>a _ {n + 1} - a _ {n} = \frac {1}{n + 1} + \ln \frac {n}{n + 1} = \frac {1}{n + 1} - \ln \left(1 + \frac {1}{n}\right).</equation>由第（I）问知，<equation>a_{n+1} - a_n < 0</equation>，故<equation>\left\{a_{n}\right\}</equation>单调减少.

下面证明<equation>\left\{a_{n}\right\}</equation>有下界.

由第（I）问知，<equation>\ln 2 - \ln 1 < 1,</equation><equation>\ln 3 - \ln 2 < \frac {1}{2},</equation><equation>\ln (n + 1) - \ln n < \frac {1}{n}.</equation>将上述不等式左端和右端分别相加，得<equation>\ln (n + 1) - \ln 1 < 1 + \frac {1}{2} + \dots + \frac {1}{n}.</equation>同时减去<equation>\ln n</equation>，得<equation>a _ {n} > \ln (n + 1) - \ln n > 0.</equation>因此，<equation>\{a_{n}\}</equation>有下界.

综上所述，数列<equation>\left\{a_{n}\right\}</equation>收敛.

---


#### 确定极限中的参数

**2023年第11题 | 填空题 | 5分**

11. 当<equation>x \to0</equation>时，函数<equation>f(x)=ax+bx^{2}+\ln(1+x)</equation>与<equation>g(x)=\mathrm{e}^{x^{2}}-\cos x</equation>是等价无穷小，则 ab=___

**答案:**-2.

**解析:**分别写出 f（x）与 g（x）在 x=0处的二阶泰勒公式.当 x→0时，<equation>f (x) = a x + b x ^ {2} + x - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right) = (a + 1) x + \left(b - \frac {1}{2}\right) x ^ {2} + o \left(x ^ {2}\right),</equation><equation>g (x) = 1 + x ^ {2} + o \left(x ^ {2}\right) - \left[ 1 - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right) \right] = \frac {3}{2} x ^ {2} + o \left(x ^ {2}\right).</equation>由于 f(x)与 g(x）是<equation>x\to0</equation>时的等价无穷小，故<equation>1 = \lim _ {x \rightarrow 0} \frac {f (x)}{g (x)} = \lim _ {x \rightarrow 0} \frac {(a + 1) x + \left(b - \frac {1}{2}\right) x ^ {2} + o \left(x ^ {2}\right)}{\frac {3}{2} x ^ {2} + o \left(x ^ {2}\right)}.</equation>由（1）式成立可得 a+1=0,b<equation>- \frac{1}{2}=\frac{3}{2}</equation>.解得 a=-1,b=2.因此，ab=-2.

---

**2019年第1题 | 选择题 | 4分 | 答案: C**

1. 当 x→0时，若 x-tanx与<equation>x^{k}</equation>是同阶无穷小，则 k=（    ）

A.1 B.2 C.3 D.4

答案: C

**解析:**解 首先，由于当 x→0时，<equation>x-\tan x\to 0</equation>，而<equation>\lim_{x\to 0}\frac{x-\tan x}{x^{k}}</equation>为非零常数，故 k > 0.下面用两种方法讨论<equation>\lim_{x\to 0}\frac{x-\tan x}{x^{k}}.</equation>（法一）由于<equation>\tan x=x+\frac{x^{3}}{3}+o\left(x^{3}\right)</equation>，故<equation>\lim _ {x \rightarrow 0} \frac {x - \tan x}{x ^ {k}} = \lim _ {x \rightarrow 0} \frac {- \frac {x ^ {3}}{3} + o \left(x ^ {3}\right)}{x ^ {k}}.</equation>当 k > 3时，该极限为<equation>\infty</equation>；当 0 < k < 3时，该极限为0；当 k=3时，该极限为<equation>-\frac{1}{3}.</equation>于是，<equation>x-\tan x</equation>与<equation>x^{3}</equation>是同阶无穷小，k=3.

因此，应选C.

（法二）利用洛必达法则讨论<equation>\lim_{x\to 0}\frac{x-\tan x}{x^{k}}.</equation><equation>\lim _ {x \rightarrow 0} \frac {x - \tan x}{x ^ {k}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - \sec^ {2} x}{k x ^ {k - 1}} = \lim _ {x \rightarrow 0} \frac {- \tan^ {2} x}{k x ^ {k - 1}} \xlongequal {\tan x \sim x} \lim _ {x \rightarrow 0} \frac {- x ^ {2}}{k x ^ {k - 1}}.</equation>当 k > 3时，该极限为<equation>\infty</equation>；当 0 < k < 3时，该极限为0；当 k=3时，该极限为<equation>-\frac{1}{3}.</equation>于是，<equation>x-\tan x</equation>与<equation>x^{3}</equation>是同阶无穷小， k=3.

因此，应选C.

---

**2018年第1题 | 选择题 | 4分 | 答案: B**

1. 若<equation>\lim_{x\rightarrow 0} \left( \mathrm{e}^{x}+a x^{2}+b x\right)^{\frac{1}{x^{2}}}=1</equation>，则（    ）

A. a<equation>=\frac{1}{2},</equation>b<equation>=-1</equation>B. a<equation>=-\frac{1}{2},</equation>b<equation>=-1</equation>C. a<equation>=\frac{1}{2},</equation>b<equation>=1</equation>D. a<equation>=-\frac{1}{2},</equation>b<equation>=1</equation>

答案: B

**解析:**解 记<equation>I = \lim_{x\to 0}\left(\mathrm{e}^{x} + ax^{2} + bx\right)^{\frac{1}{x^{2}}}</equation>.

对原极限进行恒等变形，再凑重要极限.<equation>\begin{aligned} I &= \lim _ {x \rightarrow 0} \left(1 + \mathrm {e} ^ {x} - 1 + a x ^ {2} + b x\right) ^ {\frac {1}{x ^ {2}}} = \lim _ {x \rightarrow 0} \left(1 + \mathrm {e} ^ {x} - 1 + a x ^ {2} + b x\right) ^ {\frac {1}{\mathrm {e} ^ {x} - 1 + a x ^ {2} + b x}} \cdot \frac {\mathrm {e} ^ {x} - 1 + a x ^ {2} + b x}{x ^ {2}} \\ &= \mathrm {e} ^ {\lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x} - 1 + a x ^ {2} + b x}{x ^ {2}}}. \end{aligned}</equation>由于<equation>I = 1</equation>，故<equation>\lim_{x\to 0}\frac{\mathrm{e}^{x}-1+ax^{2}+bx}{x^{2}}=0.</equation>又因为<equation>\mathrm{e}^{x}</equation>在 x=0处的二阶泰勒公式为<equation>\mathrm{e}^{x}=1+x+\frac{x^{2}}{2}+o\left(x^{2}\right)</equation>，所以<equation>\lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x} - 1 + a x ^ {2} + b x}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {(1 + b) x + \left(\frac {1}{2} + a\right) x ^ {2} + o \left(x ^ {2}\right)}{x ^ {2}}.</equation>当且仅当<equation>1 + b = 0, \frac{1}{2} + a = 0</equation>，即<equation>b = -1</equation>，<equation>a = -\frac{1}{2}</equation>时，<equation>\lim_{x\to 0}\frac{\mathrm{e}^{x} - 1 + ax^{2} + bx}{x^{2}} = 0.</equation>因此，<equation>a=-\frac{1}{2}</equation><equation>b=-1</equation>应选B.

---

**2015年第15题 | 解答题 | 10分**

15. (本题满分10分）

设函数<equation>f(x)=x+a\ln(1+x)+bx\sin x,g(x)=kx^{3}.</equation>若 f(x)与 g(x)在<equation>x\rightarrow0</equation>时是等价无穷小，求 a,b,k的值.

**答案:**<equation>(1 5) a = - 1, b = - \frac {1}{2}, k = - \frac {1}{3}.</equation>

**解析:**解 由于 g(x）中 x的次数为3，故可考虑写出 f(x)在 x=0处的3阶泰勒公式.<equation>\ln (1 + x) = x - \frac {x ^ {2}}{2} + \frac {x ^ {3}}{3} + o \left(x ^ {3}\right), \sin x = x - \frac {x ^ {3}}{3 !} + o \left(x ^ {3}\right),</equation><equation>f (x) = x + a x - \frac {a x ^ {2}}{2} + \frac {a x ^ {3}}{3} + b x ^ {2} + o \left(x ^ {3}\right) = (a + 1) x + \left(b - \frac {a}{2}\right) x ^ {2} + \frac {a}{3} x ^ {3} + o \left(x ^ {3}\right).</equation>记<equation>I=\lim_{x\to 0}\frac{f(x)}{g(x)}=\lim_{x\to 0}\frac{(a+1)x+\left(b-\frac{a}{2}\right)x^{2}+\frac{a}{3}x^{3}+o\left(x^{3}\right)}{kx^{3}}.</equation>由等价无穷小量的定义知<equation>I=1.</equation>首先，<equation>k\neq 0.</equation>当<equation>k\neq 0</equation>时，若I存在，则必有<equation>\left\{ \begin{array}{l l} a+1=0, \\ b-\frac{a}{2}=0, \end{array} \right.</equation>否则<equation>I=\infty.</equation>解得<equation>a=-1, b=-\frac{1}{2}.</equation>又因为<equation>I=1</equation>所以<equation>\frac{a}{3}=k,k=-\frac{1}{3}.</equation>综上所述，<equation>a=-1</equation><equation>b=-\frac{1}{2}</equation><equation>k=-\frac{1}{3}.</equation>

---

**2014年第1题 | 选择题 | 4分 | 答案: B**

1. 当<equation>x \to 0^{+}</equation>时，若<equation>\ln^{\alpha}(1+2x),(1-\cos x)^{\frac{1}{\alpha}}</equation>均是比 x高阶的无穷小量，则<equation>\alpha</equation>的取值范围是（    ）

A. (2,+<equation>\infty</equation>) B. (1,2) C.<equation>\left(\frac{1}{2},1\right)</equation>D.<equation>\left(0,\frac{1}{2}\right)</equation>

答案: B

**解析:**解 当<equation>x\to0^{+}</equation>时，<equation>\ln(1+2x)\sim2x,1-\cos x\sim\frac{1}{2}x^{2}.</equation>若<equation>\ln^{\alpha}(1+2x)</equation>和<equation>(1-\cos x)^{\frac{1}{\alpha}}</equation>均为比x高阶的无穷小量，则<equation>(2x)^{\alpha}</equation>与<equation>\left(\frac{1}{2} x^{2}\right)^{\frac{1}{\alpha}}</equation>也均为比x高阶的无穷小量，即<equation>\left\{\begin{array}{l l} {\alpha>1,} \\ {\frac{2}{\alpha}>1,} \end{array} \right.</equation>解得<equation>1<\alpha<2.</equation>应选B.

---

**2013年第15题 | 解答题 | 10分**

15. (本题满分10分)

当<equation>x\to0</equation>时，<equation>1-\cos x\cdot\cos 2x\cdot\cos 3x</equation>与<equation>ax^{n}</equation>为等价无穷小量，求 n与 a的值.

**答案:**(15) n=2, a=7.

**解析:**解记<equation>I=\lim_{x\to 0}\frac{1-\cos x\cos 2x\cos 3x}{a x^{n}}.</equation>由题设，<equation>I=1.</equation>（法一）分别考虑<equation>\cos x,\cos 2x,\cos 3x</equation>的二阶泰勒公式，<equation>\cos x = 1 - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right),</equation><equation>\cos 2 x = 1 - \frac {1}{2} (2 x) ^ {2} + o \left(\left(2 x\right) ^ {2}\right) = 1 - 2 x ^ {2} + o \left(x ^ {2}\right),</equation><equation>\cos 3 x = 1 - \frac {1}{2} (3 x) ^ {2} + o \left((3 x) ^ {2}\right) = 1 - \frac {9}{2} x ^ {2} + o \left(x ^ {2}\right).</equation>代人I，得<equation>\begin{aligned} I &= \lim _ {x \rightarrow 0} \frac {1 - \left[ 1 - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right)\right]\left[ 1 - 2 x ^ {2} + o \left(x ^ {2}\right)\right]\left[ 1 - \frac {9}{2} x ^ {2} + o \left(x ^ {2}\right)\right]}{a x ^ {n}} \\ &= \lim _ {x \rightarrow 0} \frac {\frac {1}{2} x ^ {2} + 2 x ^ {2} + \frac {9}{2} x ^ {2} + o \left(x ^ {2}\right)}{a x ^ {n}} = \lim _ {x \rightarrow 0} \frac {7 x ^ {2} + o \left(x ^ {2}\right)}{a x ^ {n}}. \end{aligned}</equation>由于<equation>\lim _ {x \rightarrow 0} \frac {7 x ^ {2} + o \left(x ^ {2}\right)}{a x ^ {n}} = \frac {7}{a} \lim _ {x \rightarrow 0} \frac {x ^ {2}}{x ^ {n}} \left[ 1 + \frac {o \left(x ^ {2}\right)}{7 x ^ {2}} \right] = \frac {7}{a} \lim _ {x \rightarrow 0} \frac {x ^ {2}}{x ^ {n}},</equation>故当 n > 2时，<equation>\lim_{x\rightarrow 0}\frac{7x^{2}+o\left(x^{2}\right)}{ax^{n}}=\infty</equation>；当 n < 2时，<equation>\lim_{x\rightarrow 0}\frac{7x^{2}+o\left(x^{2}\right)}{ax^{n}}=0</equation>；而当 n = 2时，<equation>\lim_{x\rightarrow 0}\frac{7x^{2}+o\left(x^{2}\right)}{ax^{2}}=</equation><equation>\frac{7}{a}</equation>.因此，由 I = 1得，<equation>\frac{7}{a}=1,a=7.</equation>综上所述，<equation>n=2</equation><equation>a=7.</equation>（法二）我们先利用三角函数的积化和差公式将<equation>\cos x\cos 2x\cos 3x</equation>作恒等变形，然后再利用洛必达法则来计算 I.<equation>\begin{aligned} \cos x \cos 2 x \cos 3 x &= \frac {1}{2} (\cos 4 x + \cos 2 x) \cos 2 x = \frac {1}{4} (\cos 6 x + \cos 2 x) + \frac {1}{4} \cos 4 x + \frac {1}{4} \\ &= \frac {1}{4} (1 + \cos 2 x + \cos 4 x + \cos 6 x). \end{aligned}</equation>从而，<equation>\begin{aligned} I &= \lim _ {x \rightarrow 0} \frac {\frac {3}{4} - \frac {1}{4} (\cos 2 x + \cos 4 x + \cos 6 x)}{a x ^ {n}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\frac {1}{4} (2 \sin 2 x + 4 \sin 4 x + 6 \sin 6 x)}{n a x ^ {n - 1}} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\cos 2 x + 4 \cos 4 x + 9 \cos 6 x}{n (n - 1) a x ^ {n - 2}} &= \lim _ {x \rightarrow 0} \frac {1 4}{n (n - 1) a x ^ {n - 2}}. \end{aligned}</equation>由上可以看出，若 I存在且等于1，则 n-2=0.否则当 n-2<0时， I=0.当 n-2>0时，<equation>I=\infty</equation>当 n=2时，<equation>I=\frac{14}{2a}=1</equation>a=7.

综上所述，<equation>n=2</equation><equation>a=7.</equation>（法三）使用添项、减项的技巧对<equation>I</equation>进行恒等变形<equation>\begin{aligned} I &= \lim _ {x \rightarrow 0} \frac {1 - \cos x + \cos x - \cos x \cos 2 x + \cos x \cos 2 x - \cos x \cos 2 x \cos 3 x}{a x ^ {n}} \\ &= \lim _ {x \rightarrow 0} \left[ \frac {1 - \cos x}{a x ^ {n}} + \frac {\cos x (1 - \cos 2 x)}{a x ^ {n}} + \frac {\cos x \cos 2 x (1 - \cos 3 x)}{a x ^ {n}} \right]. \end{aligned}</equation>分别考虑<equation>\lim_{x\to 0}\frac{1 - \cos x}{ax^n},\lim_{x\to 0}\frac{\cos x(1 - \cos 2x)}{ax^n},\lim_{x\to 0}\frac{\cos x\cos 2x(1 - \cos 3x)}{ax^n}.</equation>由于当<equation>x\to0</equation>时，<equation>\cos x\to1,1-\cos x\sim\frac{x^{2}}{2}</equation>，故这三个极限均仅当 n=2时存在且不为零.当 n>2时，极限为<equation>\infty</equation>；当 n<2时，极限为零.<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {1 - \cos x}{a x ^ {2}} \xlongequal {\frac {1 - \cos x \sim \frac {x ^ {2}}{2}}{2}} \frac {1}{2 a}, \quad \lim _ {x \rightarrow 0} \frac {\cos x (1 - \cos 2 x)}{a x ^ {2}} \xlongequal {\frac {1 - \cos 2 x \sim \frac {(2 x) ^ {2}}{2}}{2}} \frac {2}{a}, \\ \lim _ {x \rightarrow 0} \frac {\cos x \cos 2 x (1 - \cos 3 x)}{a x ^ {2}} \xlongequal {\frac {1 - \cos 3 x \sim \frac {(3 x) ^ {2}}{2}}{2}} \frac {9}{2 a}. \\ \end{array}</equation><equation>I = \frac {1}{2 a} + \frac {2}{a} + \frac {9}{2 a} = \frac {7}{a} = 1.</equation>因此，<equation>n = 2</equation>，<equation>a = 7</equation>

---

**2012年第15题 | 解答题 | 10分**

15. (本题满分10分）

已知函数<equation>f ( x )=\frac{1+x}{\sin x}-\frac{1}{x}</equation>，记 a =<equation>\lim_{x\to 0}f(x).</equation>I. 求 a的值；

II. 若当<equation>x\to0</equation>时，<equation>f(x)-a</equation>与<equation>x^{k}</equation>是同阶无穷小量，求常数 k的值.

**答案:**(15) ( I ) a = 1 ;

( II ) k = 1.

**解析:**解（I）<equation>\lim_{x\to 0}f(x)</equation>为<equation>\infty -\infty</equation>型未定式，可通分写成<equation>\frac{0}{0}</equation>型未定式.<equation>a = \lim _ {x \rightarrow 0} \left(\frac {1 + x}{\sin x} - \frac {1}{x}\right) = \lim _ {x \rightarrow 0} \frac {x ^ {2} + x - \sin x}{x \sin x} \xlongequal {\sin x \sim x} \lim _ {x \rightarrow 0} \frac {x ^ {2} + x - \sin x}{x ^ {2}}.</equation>考虑<equation>\lim_{x\to 0}\frac{x-\sin x}{x^{2}}.</equation><equation>\lim _ {x \rightarrow 0} \frac {x - \sin x}{x ^ {2}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - \cos x}{2 x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\sin x}{2} = 0.</equation>或者，利用<equation>\sin x=x-\frac{x^{3}}{6}+o\left(x^{3}\right)</equation>可得<equation>\lim _ {x \rightarrow 0} \frac {x - \sin x}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\frac {x ^ {3}}{6} + o \left(x ^ {3}\right)}{x ^ {2}} = 0.</equation>因此，<equation>a = \lim _ {x \rightarrow 0} \frac {x ^ {2} + x - \sin x}{x ^ {2}} = 1 + \lim _ {x \rightarrow 0} \frac {x - \sin x}{x ^ {2}} = 1 + 0 = 1.</equation>（Ⅱ）由第（I）问得，<equation>a=\lim_{x\to 0}f(x)=1</equation>，故<equation>\lim_{x\to 0}[f(x)-1] = 0.</equation>若<equation>f ( x ) - 1</equation>与<equation>x^{k}</equation>是<equation>x\to 0</equation>时的同阶无穷小量，则<equation>\lim_{x\to 0}\frac{f(x)-1}{x^k}</equation>为一非零常数.<equation>\lim _ {x \rightarrow 0} \frac {f (x) - 1}{x ^ {k}} = \lim _ {x \rightarrow 0} \frac {x ^ {2} + x - \sin x - x \sin x}{x ^ {k + 1} \sin x} \xlongequal {\sin x \sim x} \lim _ {x \rightarrow 0} \frac {x ^ {2} + x - \sin x - x \sin x}{x ^ {k + 2}}.</equation>下面用两种方法来求上面的极限.

（法一）利用洛必达法则.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {x ^ {2} + x - \sin x - x \sin x}{x ^ {k + 2}} &= \lim _ {x \rightarrow 0} \frac {(1 + x) (x - \sin x)}{x ^ {k + 2}} = \lim _ {x \rightarrow 0} \frac {x - \sin x}{x ^ {k + 2}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - \cos x}{(k + 2) x ^ {k + 1}} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\sin x}{(k + 2) (k + 1) x ^ {k}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\cos x}{(k + 2) (k + 1) k x ^ {k - 1}} \\ &= \lim _ {x \rightarrow 0} \frac {1}{(k + 2) (k + 1) k x ^ {k - 1}} = c. \end{aligned}</equation>要使上面的极限等于非零常数<equation>c, x^{k - 1}</equation>必须等于1，即<equation>k = 1</equation>. 此时<equation>c = \frac{1}{6}</equation>.

（法二）利用等价无穷小替换.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {x ^ {2} + x - \sin x - x \sin x}{x ^ {k + 2}} &= \lim _ {x \rightarrow 0} \frac {(1 + x) (x - \sin x)}{x ^ {k + 2}} = \lim _ {x \rightarrow 0} \frac {x - \sin x}{x ^ {k + 2}} \\ \frac {x - \sin x - \frac {x ^ {3}}{6}}{\frac {1}{6}} \frac {1}{6} \lim _ {x \rightarrow 0} \frac {x ^ {3}}{x ^ {k + 2}} &= c. \end{aligned}</equation>若<equation>k+2<3</equation>，则<equation>\lim_{x\to 0}\frac{x^{3}}{x^{k+2}}=0</equation>；若<equation>k+2>3</equation>，则<equation>\lim_{x\to 0}\frac{x^{3}}{x^{k+2}}=\infty</equation>；若<equation>k+2=3</equation>，则<equation>\lim_{x\to 0}\frac{x^{3}}{x^{3}}=1.</equation>因此，<equation>k+2=3</equation>，<equation>c=\frac{1}{6}</equation>，即<equation>k=1</equation>，<equation>c=\frac{1}{6}.</equation>

---

**2011年第1题 | 选择题 | 4分 | 答案: C**

1. 已知当<equation>x\to0</equation>时，函数<equation>f(x)=3\sin x-\sin 3x</equation>与<equation>cx^{k}</equation>是等价无穷小量，则（    )

A. k=1,c=4 B. k=1,c=-4 C. k=3,c=4 D. k=3,c=-4

答案: C

**解析:**解 由题设知，<equation>c\neq 0,k > 0.</equation>记<equation>I=\lim_{x\to 0}\frac{f(x)}{cx^{k}}</equation>，则由等价无穷小量的定义知，<equation>I=1.</equation>下面我们用两种方法讨论 k,c的值.

（法一）考虑 f(x)在 x=0处的泰勒公式.由于<equation>\sin x=x-\frac{1}{3!} x^{3}+o\left(x^{3}\right)</equation>，故<equation>\sin 3x=3x-\frac{1}{3!}\left(3x\right)^{3}+o\left(x^{3}\right).</equation>因此，<equation>1 = \lim _ {x \rightarrow 0} \frac {3 \sin x - \sin 3 x}{c x ^ {k}} = \lim _ {x \rightarrow 0} \frac {3 x - \frac {1}{2} x ^ {3} - 3 x + \frac {2 7}{6} x ^ {3} + o \left(x ^ {3}\right)}{c x ^ {k}} = \lim _ {x \rightarrow 0} \frac {4 x ^ {3} + o \left(x ^ {3}\right)}{c x ^ {k}}.</equation>下面讨论使<equation>\lim_{x\to 0}\frac{4x^{3}+o\left(x^{3}\right)}{cx^{k}}=1</equation>成立的 k，c的值.

由于<equation>I = \frac {4}{c} \lim _ {x \rightarrow 0} \frac {x ^ {3}}{x ^ {k}} \left[ 1 + \frac {o \left(x ^ {3}\right)}{4 x ^ {3}} \right] = \frac {4}{c} \lim _ {x \rightarrow 0} \frac {x ^ {3}}{x ^ {k}},</equation>故当<equation>c\neq 0,k < 3</equation>时，<equation>I = 0</equation>；当<equation>c\neq 0,k > 3</equation>时，<equation>I = \infty</equation>；只有当<equation>c\neq 0,k = 3</equation>时，<equation>I = \frac{4}{c} = 1.</equation>因此，<equation>k = 3,c = 4.</equation>应选C.

（法二）对<equation>I</equation>使用洛必达法则可得，<equation>I = \lim _ {x \rightarrow 0} \frac {3 \sin x - \sin 3 x}{c x ^ {k}} \xlongequal {\text {洛 必达}} \lim _ {x \rightarrow 0} \frac {3 \cos x - 3 \cos 3 x}{k c x ^ {k - 1}}.</equation>由于<equation>I = 1</equation>，而<equation>\lim_{x\to 0}(3\cos x - 3\cos 3x) = 0</equation>，故<equation>k > 1</equation>，否则<equation>I = 0.</equation>当<equation>k > 1</equation>时，继续对（1）式使用洛必达法则可得，<equation>\lim _ {x \rightarrow 0} \frac {3 \cos x - 3 \cos 3 x}{k c x ^ {k - 1}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {- 3 \sin x + 9 \sin 3 x}{k (k - 1) c x ^ {k - 2}}.</equation>由于<equation>I = 1</equation>，而<equation>\lim_{x\to 0}(-3\sin x + 9\sin 3x) = 0</equation>，故<equation>k > 2</equation>，否则<equation>I = 0.</equation>当<equation>k > 2</equation>时，继续对（2）式使用洛必达法则可得，<equation>\lim _ {x \rightarrow 0} \frac {- 3 \sin x + 9 \sin 3 x}{k (k - 1) c x ^ {k - 2}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {- 3 \cos x + 2 7 \cos 3 x}{k (k - 1) (k - 2) c x ^ {k - 3}} = \lim _ {x \rightarrow 0} \frac {2 4}{k (k - 1) (k - 2) c x ^ {k - 3}}.</equation>若 I=1，则 k=3，否则当 k<3时，I=0；当 k>3时，<equation>I=\infty</equation>.进一步可得<equation>3\times 2\times c=2 4</equation>从而 c=4.应选C.

---

**2009年第2题 | 选择题 | 4分 | 答案: A**

2. 当<equation>x\to0</equation>时，<equation>f(x)=x-\sin ax</equation>与<equation>g(x)=x^{2}\ln(1-bx)</equation>是等价无穷小量，则（    )

A. a=1,b=-<equation>\frac{1}{6}</equation>B. a=1,b=<equation>\frac{1}{6}</equation>C. a=-1,b=-<equation>\frac{1}{6}</equation>D. a=-1,b=<equation>\frac{1}{6}</equation>

答案: A

**解析:**解（法一）由于<equation>x\to 0</equation>时，<equation>f(x)</equation>与<equation>g(x)</equation>是等价无穷小量，故<equation>\begin{aligned} 1 &= \lim _ {x \rightarrow 0} \frac {f (x)}{g (x)} = \lim _ {x \rightarrow 0} \frac {x - \sin a x}{x ^ {2} \ln (1 - b x)} \xlongequal {\ln (1 - b x) \sim (- b x)} \lim _ {x \rightarrow 0} \frac {x - \sin a x}{- b x ^ {3}} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - a \cos a x}{- 3 b x ^ {2}} &= I _ {1}. \end{aligned}</equation>由于<equation>\lim_{x\to 0}(-3bx^2) = 0</equation>，故若<equation>I_{1}</equation>存在，则<equation>\lim_{x\to 0}(1 - a\cos ax) = 0</equation>，从而<equation>a = 1.</equation>代人 a=1，得<equation>I _ {1} = \lim _ {x \rightarrow 0} \frac {1 - \cos x}{- 3 b x ^ {2}} \xlongequal {\text {一}} \frac {1 - \cos x \sim \frac {x ^ {2}}{2}}{\lim _ {x \rightarrow 0} \frac {\frac {x ^ {2}}{2}}{- 3 b x ^ {2}}} = - \frac {1}{6 b}.</equation>当<equation>b = -\frac{1}{6}</equation>时，<equation>I_{1}</equation>存在且等于1.

因此，当<equation>a=1,b=-\frac{1}{6}</equation>时，<equation>\lim_{x\to 0}\frac{f(x)}{g(x)}=1,f(x)</equation>与g(x）是<equation>x\to 0</equation>时的等价无穷小量.应选A.

（法二）因为<equation>\sin a x = a x - \frac {1}{6} a ^ {3} x ^ {3} + o \left(x ^ {3}\right), \quad \ln (1 - b x) = - b x + o (x),</equation>所以<equation>1 = \lim _ {x \rightarrow 0} \frac {x - \sin a x}{x ^ {2} \ln (1 - b x)} = \lim _ {x \rightarrow 0} \frac {(x - a x) + \frac {1}{6} a ^ {3} x ^ {3} - o \left(x ^ {3}\right)}{x ^ {2} \left[ - b x + o (x) \right]} = \lim _ {x \rightarrow 0} \frac {(1 - a) x + \frac {1}{6} a ^ {3} x ^ {3} - o \left(x ^ {3}\right)}{- b x ^ {3} + o \left(x ^ {3}\right)} = I.</equation>首先，<equation>b\neq 0</equation>，否则<equation>I = \infty</equation>.当<equation>b\neq 0</equation>时，若<equation>a - 1\neq 0</equation>，则<equation>I = \infty</equation>，从而可得<equation>a = 1</equation>代入 a=1，得<equation>1 = \lim _ {x \rightarrow 0} \frac {\frac {1}{6} x ^ {3} - o \left(x ^ {3}\right)}{- b x ^ {3} + o \left(x ^ {3}\right)} = - \frac {1}{6 b}.</equation>从而<equation>b = -\frac{1}{6}</equation>因此，<equation>a=1,b=-\frac{1}{6}</equation>应选A.

---


#### 函数极限的计算

**2022年第11题 | 填空题 | 5分**

<equation>1. \lim _ {x \rightarrow 0} \left(\frac {1 + \mathrm {e} ^ {x}}{2}\right) ^ {\cot x} = \underline {{}}</equation>

**解析:**取对数再求极限.<equation>\lim _ {x \rightarrow 0} \left(\frac {1 + \mathrm {e} ^ {x}}{2}\right) ^ {\cot x} = \lim _ {x \rightarrow 0} \mathrm {e} ^ {\cot x \ln \frac {1 + \mathrm {e} ^ {x}}{2}} = \mathrm {e} _ {x \rightarrow 0} ^ {\lim _ {x \rightarrow 0} \cot x \ln \frac {1 + \mathrm {e} ^ {x}}{2}}.</equation>下面计算<equation>\lim_{x\to 0}\cot x\ln \frac{1 + \mathrm{e}^{x}}{2}</equation>.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \cot x \ln \frac {1 + e ^ {x}}{2} &= \lim _ {x \rightarrow 0} \frac {\ln \frac {1 + e ^ {x}}{2}}{\tan x} \xlongequal {\tan x \sim x} \lim _ {x \rightarrow 0} \frac {\ln \left(1 + \frac {e ^ {x} - 1}{2}\right)}{x} \\ \frac {\ln \left(1 + \frac {\mathrm {e} ^ {x} - 1}{2}\right) - \frac {\mathrm {e} ^ {x} - 1}{2}}{\lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x} - 1}{2 x}} \xlongequal {\mathrm {e} ^ {x} - 1 \sim x} \lim _ {x \rightarrow 0} \frac {x}{2 x} \\ &= \frac {1}{2}. \end{aligned}</equation>因此，原极限<equation>= \mathrm{e}^{\frac{1}{2}} = \sqrt{\mathrm{e}}.</equation>

---

**2021年第17题 | 解答题 | 10分**

17. (本题满分10分)

求极限 lim<equation>\left(\frac {1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t}{\mathrm {e} ^ {x} - 1} - \frac {1}{\sin x}\right)</equation>

**解析:**解 （法一）先整理原极限再计算.<equation>\begin{array}{l} \frac {\mathrm {e} ^ {x} - 1 \sim x}{\sin x \sim x} \lim _ {x \rightarrow 0} \frac {\int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t}{x} + \lim _ {x \rightarrow 0} \frac {\sin x - \mathrm {e} ^ {x} + 1}{x ^ {2}} \\ \frac {\mathrm {洛 必 达}}{} \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x ^ {2}}}{1} + \lim _ {x \rightarrow 0} \frac {x - \frac {x ^ {3}}{6} - 1 - x - \frac {x ^ {2}}{2} + 1 + o \left(x ^ {2}\right)}{x ^ {2}} \\ = 1 + \lim _ {x \rightarrow 0} \frac {- \frac {x ^ {2}}{2} + o \left(x ^ {2}\right)}{x ^ {2}} = 1 - \frac {1}{2} = \frac {1}{2}. \\ \end{array}</equation>因此，原极限<equation>= \frac{1}{2}。</equation>（法二）将原极限通分整理，化为<equation>\frac{0}{0}</equation>型未定式后再应用洛必达法则.<equation>\begin{aligned} \mathrm {原 极 限} &= \lim _ {x \rightarrow 0} \frac {\sin x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) - \mathrm {e} ^ {x} + 1}{\left(\mathrm {e} ^ {x} - 1\right) \sin x} \\ \frac {\mathrm {e} ^ {x} - 1 \sim x}{\sin x \sim x} \lim _ {x \rightarrow 0} \frac {\sin x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) - \mathrm {e} ^ {x} + 1}{x ^ {2}} \\ \underline {{\text {洛必达}}} \lim _ {x \rightarrow 0} \frac {\cos x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) + \sin x \cdot \mathrm {e} ^ {x ^ {2}} - \mathrm {e} ^ {x}}{2 x} \\ \underline {{\text {洛必达}}} \lim _ {x \rightarrow 0} \frac {- \sin x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) + \cos x \cdot \mathrm {e} ^ {x ^ {2}} + 2 x \cdot \sin x \cdot \mathrm {e} ^ {x ^ {2}} - \mathrm {e} ^ {x}}{2} &= \frac {1}{2}. \end{aligned}</equation>因此，原极限<equation>= \frac{1}{2}.</equation>

---

**2019年第9题 | 填空题 | 4分**

（无内容）

**答案:**##<equation>4 \mathrm{e}^{2}.</equation>

**解析:**（法一）凑重要极限.<equation>\lim _ {x \rightarrow 0} \left(x + 2 ^ {x}\right) ^ {\frac {2}{x}} = \lim _ {x \rightarrow 0} \left(1 + x + 2 ^ {x} - 1\right) ^ {\frac {1}{x + 2 ^ {x} - 1}} \cdot \frac {2 \left(x + 2 ^ {x} - 1\right)}{x}.</equation>计算<equation>\lim_{x\to 0}\frac{2(x+2^{x}-1)}{x}.</equation><equation>\lim _ {x \rightarrow 0} \frac {2 \left(x + 2 ^ {x} - 1\right)}{x} = 2 + 2 \lim _ {x \rightarrow 0} \frac {2 ^ {x} - 1}{x} \frac {2 ^ {x} - 1 \sim x \ln 2}{2} + 2 \lim _ {x \rightarrow 0} \frac {x \ln 2}{x} = 2 + 2 \ln 2.</equation>因此，原极限<equation>= \mathrm{e}^{2 + 2\ln 2} = 4\mathrm{e}^{2}.</equation>（法二）取对数，再求极限.<equation>\lim _ {x \rightarrow 0} \left(x + 2 ^ {x}\right) ^ {\frac {2}{x}} = \lim _ {x \rightarrow 0} \mathrm {e} ^ {\frac {2 \ln \left(x + 2 ^ {x}\right)}{x}} = \mathrm {e} ^ {\lim _ {x \rightarrow 0} \frac {2 \ln \left(x + 2 ^ {x}\right)}{x}} \xlongequal {\text {洛必达}} \mathrm {e} ^ {2 \lim _ {x \rightarrow 0} \frac {1 + 2 ^ {x} \ln 2}{x + 2 ^ {x}}} = \mathrm {e} ^ {2 + 2 \ln 2} = 4 \mathrm {e} ^ {2}.</equation>

---

**2018年第9题 | 填空题 | 4分**

9.<equation>\lim x^{2}[\arctan(x+1)-\arctan x]=</equation>

**答案:**```latex

1.
```
**解析: **解（法一）由拉格朗日中值定理可得，存在<equation>\xi_{x}\in(x,x+1)</equation>，使得<equation>\arctan (x + 1) - \arctan x = \frac {1}{1 + \xi_ {x} ^ {2}}.</equation>于是，原极限<equation>= \lim_{x\to +\infty}\frac{x^{2}}{1 + \xi_{x}^{2}}.</equation>由于当 x > 0时，<equation>\frac{x^{2}}{1+(x+1)^{2}}\leqslant \frac{x^{2}}{1+\xi_{x}^{2}}\leqslant \frac{x^{2}}{1+x^{2}}</equation>，而<equation>\lim_{x\rightarrow +\infty}\frac{x^{2}}{1+(x+1)^{2}}=\lim_{x\rightarrow +\infty}\frac{x^{2}}{1+x^{2}}=1</equation>，故由夹逼准则可知<equation>\lim_{x\rightarrow +\infty}\frac{x^{2}}{1+\xi_{x}^{2}}=1.</equation>因此，原极限 = 1.

（法二）利用洛必达法则.<equation>\begin{aligned} \lim _ {x \rightarrow + \infty} x ^ {2} [ \arctan (x + 1) - \arctan x ] &= \lim _ {x \rightarrow + \infty} \frac {\arctan (x + 1) - \arctan x}{\frac {1}{x ^ {2}}} \\ \underline {{\mathrm {洛 必 达}}} \lim _ {x \rightarrow + \infty} \frac {\frac {1}{1 + (x + 1) ^ {2}} - \frac {1}{1 + x ^ {2}}}{- 2 \cdot \frac {1}{x ^ {3}}} \\ &= - \frac {1}{2} \lim _ {x \rightarrow + \infty} \frac {\left[ x ^ {2} - (x + 1) ^ {2} \right] \cdot x ^ {3}}{\left[ 1 + (x + 1) ^ {2} \right]\left(1 + x ^ {2}\right)} \\ &= - \frac {1}{2} \lim _ {x \rightarrow + \infty} \frac {- 2 x ^ {4} - x ^ {3}}{x ^ {4} + 2 x ^ {3} + 3 x ^ {2} + 2 x + 2} = 1. \end{aligned}</equation>

---

**2017年第3题 | 选择题 | 4分 | 答案: D**
3. 设数列<equation>\{x_{n}\}</equation>收敛，则（    )

A. 当<equation>\lim_{n\rightarrow \infty}\sin x_{n}=0</equation>时，<equation>\lim_{n\rightarrow \infty}x_{n}=0</equation>B. 当<equation>\lim_{n\rightarrow \infty}(x_{n}+\sqrt{|x_{n}|})=0</equation>时，<equation>\lim_{n\rightarrow \infty}x_{n}=0</equation>C. 当<equation>\lim_{n\rightarrow \infty}(x_{n}+x_{n}^{2})=0</equation>时，<equation>\lim_{n\rightarrow \infty}x_{n}=0</equation>D. 当<equation>\lim_{n\rightarrow \infty}(x_{n}+\sin x_{n})=0</equation>时，<equation>\lim_{n\rightarrow \infty}x_{n}=0</equation>
答案: D
**解析: **解（法一）记<equation>\lim_{n\to \infty}x_n = a</equation>，则由<equation>\sin x</equation>是连续函数以及<equation>\lim_{n\to \infty}(x_n + \sin x_n) = 0</equation>可知，<equation>\lim _ {n \rightarrow \infty} \left(x _ {n} + \sin x _ {n}\right) = a + \sin a = 0.</equation>x=a是函数<equation>f ( x )=x+\sin x</equation>的零点.

注意到<equation>f(0)=0</equation>，又因为<equation>f^{\prime}(x)=1+\cos x\geqslant 0</equation>，所以 f(x)单调增加.于是 x=0是 f(x)的唯一零点，a=0.因此，<equation>\lim_{n\to \infty}x_{n}=0.</equation>应选D.

（法二）记<equation>f ( x )=x+\sin x</equation>，则<equation>f ( 0 )=0</equation><equation>f^{\prime}(x)=1+\cos x\geqslant0.</equation>于是 f(x)是单调增加的可导函数，<equation>f^{-1}</equation>存在且连续.

由于<equation>\lim_{n\to \infty} \left(x_{n}+\sin x_{n}\right)=0</equation>，故<equation>\lim _ {n \rightarrow \infty} x _ {n} = \lim _ {n \rightarrow \infty} f ^ {- 1} \left(f \left(x _ {n}\right)\right) = \lim _ {n \rightarrow \infty} f ^ {- 1} \left(x _ {n} + \sin x _ {n}\right) = f ^ {- 1} \left(\lim _ {n \rightarrow \infty} \left(x _ {n} + \sin x _ {n}\right)\right) = f ^ {- 1} (0) = 0.</equation>（法三）排除法.

对选项A：考虑<equation>x_{n}=\pi +\frac{1}{n}</equation>，则<equation>\lim_{n\to \infty}\sin x_{n}=0</equation>，但<equation>\lim_{n\to \infty}x_{n}=\pi.</equation>对选项B和选项C：考虑<equation>x_{n}\equiv-1</equation>，则<equation>\lim _ {n \rightarrow \infty} \left(x _ {n} + \sqrt {\left| x _ {n} \right|}\right) = 0, \quad \lim _ {n \rightarrow \infty} \left(x _ {n} + x _ {n} ^ {2}\right) = 0,</equation>但<equation>\lim_{n\to \infty}x_{n}=-1.</equation>由排除法知，应选D.

---

**2016年第15题 | 解答题 | 10分**
15. (本题满分10分）

求极限<equation>\lim_{x\to 0}(\cos 2x+2x\sin x)^{\frac{1}{x^{4}}}.</equation>
**解析: **## 记原极限为 I.

（法一）凑重要极限<equation>\lim_{x\to 0}(1+x)^{\frac{1}{x}}=e.</equation>由于<equation>x\to0</equation>时，<equation>\cos 2x+2x\sin x-1\to0</equation>，故<equation>\lim_{x\to0}\left(1+\cos 2x+2x\sin x-1\right)^{\frac{1}{\cos 2x+2x\sin x-1}}=e.</equation><equation>I = \lim _ {x \rightarrow 0} \left(1 + \cos 2 x + 2 x \sin x - 1\right) ^ {\frac {1}{\cos 2 x + 2 x \sin x - 1}} \cdot \frac {\cos 2 x + 2 x \sin x - 1}{x ^ {4}}.</equation>下面求<equation>\lim_{x\rightarrow0}\frac{\cos 2x+2x\sin x-1}{x^{4}}.</equation><equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {\cos 2 x + 2 x \sin x - 1}{x ^ {4}} \xlongequal {\cos 2 x - 1 = - 2 \sin^ {2} x} \lim _ {x \rightarrow 0} \frac {2 x \sin x - 2 \sin^ {2} x}{x ^ {4}} &= \lim _ {x \rightarrow 0} \frac {2 \sin x (x - \sin x)}{x ^ {4}} \\ \frac {\sin x - x}{x} 2 \lim _ {x \rightarrow 0} \frac {x - \sin x}{x ^ {3}} &= 2 \lim _ {x \rightarrow 0} \frac {x - x + \frac {x ^ {3}}{3 !} - o \left(x ^ {3}\right)}{x ^ {3}} = \frac {1}{3}. \end{aligned}</equation>因此，<equation>I=\mathrm{e}^{\frac{1}{3}}.</equation>下面我们用另外两种方法计算<equation>\lim_{x\to 0}\frac{\cos 2x+2x\sin x-1}{x^{4}}.</equation>(1) 利用泰勒公式.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {\cos 2 x + 2 x \sin x - 1}{x ^ {4}} &= \lim _ {x \rightarrow 0} \frac {1 - \frac {(2 x) ^ {2}}{2 !} + \frac {(2 x) ^ {4}}{4 !} + o \left(x ^ {4}\right) + 2 x \left[x - \frac {x ^ {3}}{3 !} + o \left(x ^ {3}\right)\right]}{x ^ {4}} - 1 \\ &= \lim _ {x \rightarrow 0} \frac {\frac {1}{3} x ^ {4} + o \left(x ^ {4}\right)}{x ^ {4}} = \frac {1}{3}. \end{aligned}</equation>(2) 利用洛必达法则.<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\cos 2 x + 2 x \sin x - 1}{x ^ {4}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {- \sin 2 x + \sin x + x \cos x}{2 x ^ {3}} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {- 2 \cos 2 x + 2 \cos x - x \sin x}{6 x ^ {2}} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {4 \sin 2 x - 3 \sin x - x \cos x}{1 2 x} \\ \end{array}</equation><equation>\frac {\mathrm {洛 必 达}}{\mathrm {}} \lim _ {x \rightarrow 0} \frac {8 \cos 2 x - 4 \cos x + x \sin x}{1 2} = \frac {1}{3}.</equation>（法二）因为<equation>\lim_{x\to 0} \left(\cos 2x+2x\sin x\right)=1</equation>，从而我们可以对<equation>\cos 2x+2x\sin x</equation>取对数，所以<equation>I=\mathrm{e}^{\lim_{x\to 0}\frac{\ln(\cos 2x+2x\sin x)}{x^{4}}}.</equation>下面求<equation>\lim_{x\rightarrow0}\frac{\ln(\cos 2x+2x\sin x)}{x^{4}}.</equation><equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {\ln (\cos 2 x + 2 x \sin x)}{x ^ {4}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\frac {1}{\cos 2 x + 2 x \sin x} \cdot (- 2 \sin 2 x + 2 \sin x + 2 x \cos x)}{4 x ^ {3}} \\ &= - \frac {1}{2} \lim _ {x \rightarrow 0} \frac {\sin 2 x - \sin x - x \cos x}{x ^ {3}} \\ &= - \frac {1}{2} \lim _ {x \rightarrow 0} \frac {2 x - \frac {(2 x) ^ {3}}{3 !} + o \left(x ^ {3}\right) - x + \frac {x ^ {3}}{3 !} - o \left(x ^ {3}\right) - x \left[ 1 - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right)\right]}{x ^ {3}} \\ &= - \frac {1}{2} \lim _ {x \rightarrow 0} \frac {\left(- \frac {8}{6} + \frac {1}{6} + \frac {1}{2}\right) x ^ {3} + o \left(x ^ {3}\right)}{x ^ {3}} = \frac {1}{3}. \end{aligned}</equation>因此，<equation>I=\mathrm{e}^{\frac{1}{3}}.</equation>

---

**2014年第5题 | 选择题 | 4分 | 答案: D**
5. 设函数 f(x) = arctanx. 若 f(x) = xf'(<equation>\xi</equation>)，则<equation>\lim_{x\to 0}\frac{\xi^{2}}{x^{2}}</equation>= (    )

A. 1 B.<equation>\frac{2}{3}</equation>C.<equation>\frac{1}{2}</equation>D.<equation>\frac{1}{3}</equation>
答案: D
**解析: **解 由于<equation>f^{\prime}(x)=(\arctan x)^{\prime}=\frac{1}{1+x^{2}}</equation>，故<equation>f^{\prime}(\xi)=\frac{1}{1+\xi^{2}}</equation>. 由于<equation>f(x)=xf^{\prime}(\xi)=\frac{x}{1+\xi^{2}}</equation>，解得<equation>\xi^{2}=\frac{x}{f(x)}-1.</equation><equation>\lim _ {x \rightarrow 0} \frac {\xi^ {2}}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\frac {x}{\arctan x} - 1}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {x - \arctan x}{x ^ {2} \arctan x}.</equation>下面我们用两种方法计算上面的极限.

（法一）由于<equation>\arctan x</equation>的3阶泰勒公式为<equation>\arctan x = x - \frac{x^3}{3} + o(x^3)</equation>，故当<equation>x\to 0</equation>时，<equation>\arctan x \sim x, \quad x - \arctan x \sim \frac {x ^ {3}}{3}.</equation><equation>\lim _ {x \rightarrow 0} \frac {x - \arctan x}{x ^ {2} \arctan x} \xlongequal {\arctan x \sim x} \lim _ {x \rightarrow 0} \frac {x - \arctan x}{x ^ {3}} \xlongequal {x - \arctan x \sim \frac {x ^ {3}}{3}} \lim _ {x \rightarrow 0} \frac {\frac {1}{3} x ^ {3}}{x ^ {3}} = \frac {1}{3}.</equation>应选 D.

（法二）利用洛必达法则计算该极限.<equation>\lim _ {x \rightarrow 0} \frac {x - \arctan x}{x ^ {2} \arctan x} \xlongequal {\arctan x \sim x} \lim _ {x \rightarrow 0} \frac {x - \arctan x}{x ^ {3}} \xlongequal {\text {洛 必 达}} \lim _ {x \rightarrow 0} \frac {1 - \frac {1}{1 + x ^ {2}}}{3 x ^ {2}} = \lim _ {x \rightarrow 0} \frac {x ^ {2}}{3 x ^ {2}} = \frac {1}{3}.</equation>

---

**2014年第15题 | 解答题 | 10分**
15. (本题满分10分)<equation>\lim _ {r \rightarrow + \infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t \right] \mathrm {d} t}{x ^ {2} \ln \left(1 + \frac {1}{x}\right)}.</equation>
**答案: **## (15)<equation>\frac{1}{2}.</equation>
**解析: **解 由于<equation>\mathrm{e}^{x}</equation>在 x=0处的带拉格朗日余项的2阶泰勒公式为<equation>\mathrm{e}^{x}=1+x+\frac{x^{2}}{2}+\frac{\mathrm{e}^{\theta x}}{3!} x^{3}</equation>其中<equation>0 < \theta < 1</equation>，故当 x > 0时，<equation>\mathrm{e}^{x}>1+x+\frac{x^{2}}{2}.</equation>于是，<equation>\mathrm{e}^{\frac{1}{t}}-1 > \frac{1}{t} +\frac{1}{2t^{2}}(t > 0),</equation><equation>t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t > t ^ {2} \left(\frac {1}{t} + \frac {1}{2 t ^ {2}}\right) - t = \frac {1}{2}.</equation>从而<equation>\int_1^{+\infty}\left[ t^2\left(\mathrm{e}^{\frac{1}{t}} -1\right) - t\right]\mathrm{d}t\to +\infty .</equation>另一方面，<equation>\lim _ {x \rightarrow + \infty} \left[ x ^ {2} \ln \left(1 + \frac {1}{x}\right)\right] \xlongequal {\ln \left(1 + \frac {1}{x}\right) \sim \frac {1}{x}} \lim _ {x \rightarrow + \infty} x = + \infty .</equation>因此，原极限为<equation>\frac{\infty}{\infty}</equation>型未定式.

当<equation>x\to +\infty</equation>时，<equation>\ln \left(1 + \frac{1}{x}\right)\sim \frac{1}{x}</equation>，故<equation>\lim _ {x \rightarrow + \infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t \right] \mathrm {d} t}{x ^ {2} \ln \left(1 + \frac {1}{x}\right)} \xlongequal {\ln \left(1 + \frac {1}{x}\right) \sim \frac {1}{x}} \lim _ {x \rightarrow + \infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t \right] \mathrm {d} t}{x}</equation><equation>\begin{aligned} \underline {{\text {洛必达}}} \lim _ {x \rightarrow + \infty} \frac {x ^ {2} \left(\mathrm {e} ^ {\frac {1}{x}} - 1\right) - x}{1} &= \lim _ {x \rightarrow + \infty} \frac {\mathrm {e} ^ {\frac {1}{x}} - 1 - \frac {1}{x}}{\frac {1}{x ^ {2}}} \\ \underline {{\frac {u = \frac {1}{x}}}} \lim _ {u \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {u} - u - 1}{u ^ {2}} \underline {{\underline {{\text {洛必达}}}}} \lim _ {u \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {u} - 1}{2 u} \\ \underline {{\frac {\mathrm {e} ^ {u} - 1 \sim u}{u \rightarrow 0 ^ {+}}}} \lim _ {u \rightarrow 0 ^ {+}} \frac {u}{2 u} &= \frac {1}{2}. \end{aligned}</equation>因此，原极限<equation>= \frac{1}{2}.</equation>将原极限化简为<equation>\lim_{x\to +\infty}[x^{2}(\mathrm{e}^{\frac{1}{x}} - 1) - x]</equation>后，也可以用泰勒公式来求该极限.

当<equation>x\to +\infty</equation>时，<equation>\frac{1}{x}\rightarrow 0^{+}</equation>.由<equation>\mathrm{e}^{u}</equation>在<equation>u = 0</equation>处的泰勒公式得，<equation>\mathrm {e} ^ {\frac {1}{x}} = 1 + \frac {1}{x} + \frac {1}{2 !} \cdot \frac {1}{x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right).</equation>从而，<equation>\begin{array}{l} \lim _ {x \rightarrow + \infty} \left[ x ^ {2} \left(\mathrm {e} ^ {\frac {1}{x}} - 1\right) - x \right] = \lim _ {x \rightarrow + \infty} \left\{x ^ {2} \left[ \frac {1}{x} + \frac {1}{2 !} \cdot \frac {1}{x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right)\right] - x \right\} \\ = \lim _ {x \rightarrow + \infty} \left[ \frac {1}{2} + x ^ {2} \cdot o \left(\frac {1}{x ^ {2}}\right)\right] = \frac {1}{2}. \\ \end{array}</equation>

---

**2013年第9题 | 填空题 | 4分**
9. lim
**解析: **解（法一）将原极限改写，得<equation>\lim _ {x \rightarrow 0} \left[ 2 - \frac {\ln (1 + x)}{x} \right] ^ {\frac {1}{x}} = \lim _ {x \rightarrow 0} \left\{\left[ 1 + \frac {x - \ln (1 + x)}{x} \right] ^ {\frac {x}{x - \ln (1 + x)}} \right\} ^ {\frac {x - \ln (1 + x)}{x}}. \frac {1}{x}.</equation>由于<equation>\lim _ {x \rightarrow 0} \frac {x - \ln (1 + x)}{x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - \frac {1}{1 + x}}{1} = 0,</equation><equation>\lim _ {x \rightarrow 0} \frac {x - \ln (1 + x)}{x ^ {2}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - \frac {1}{1 + x}}{2 x} = \lim _ {x \rightarrow 0} \frac {1}{2 (1 + x)} = \frac {1}{2},</equation>故利用重要极限<equation>\lim_{x\to 0}(1 + x)^{\frac{1}{x}} = \mathrm{e}</equation>可得原极限<equation>= \sqrt{\mathrm{e}}.</equation>（法二）由于<equation>\ln \left[ 2 - \frac{\ln(1 + x)}{x} \right]^{\frac{1}{x}} = \frac{1}{x}\ln \left[ 2 - \frac{\ln(1 + x)}{x} \right],</equation>故<equation>\lim_{x\to 0}\left[ 2 - \frac{\ln(1 + x)}{x} \right]^{\frac{1}{x}} = \mathrm{e}^{\lim_{x\to 0}\frac{\ln[2 - \frac{\ln(1 + x)}{x}]}{x}}.</equation>下面求<equation>\lim_{x\to 0}\frac{\ln\left[2 - \frac{\ln(1 + x)}{x}\right]}{x}</equation>.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {\ln \left[ 2 - \frac {\ln (1 + x)}{x} \right]}{x} &= \lim _ {x \rightarrow 0} \frac {\ln \left[ 1 + 1 - \frac {\ln (1 + x)}{x} \right]}{x} \\ \underline {{\underline {{\ln \left[ 1 + 1 - \frac {\ln (1 + x)}{x} \right] \sim 1 - \frac {\ln (1 + x)}{x}}}}} \lim _ {x \rightarrow 0} \frac {1 - \frac {\ln (1 + x)}{x}}{x} \\ &= \lim _ {x \rightarrow 0} \frac {x - \ln (1 + x)}{x ^ {2}} \xlongequal {\text {洛 必达}} \lim _ {x \rightarrow 0} \frac {1 - \frac {1}{1 + x}}{2 x} = \lim _ {x \rightarrow 0} \frac {1}{2 (1 + x)} = \frac {1}{2}. \end{aligned}</equation>因此，原极限<equation>= \sqrt{\mathrm{e}}.</equation>也可以利用<equation>\ln (1 + x) = x - \frac{x^2}{2} + o\left(x^2\right)</equation>来求<equation>\lim_{x\to 0}\frac{x - \ln(1 + x)}{x^2}</equation>.<equation>\lim _ {x \rightarrow 0} \frac {x - \ln (1 + x)}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {x - x + \frac {x ^ {2}}{2} - o \left(x ^ {2}\right)}{x ^ {2}} = \frac {1}{2}.</equation>

---

**2011年第9题 | 填空题 | 4分**
（无内容）
**解析: **解 （法一）由于<equation>\lim _ {x \rightarrow 0} \left(\frac {1 + 2 ^ {x}}{2}\right) ^ {\frac {1}{x}} = \lim _ {x \rightarrow 0} \mathrm {e} ^ {\frac {1}{x} \ln \frac {1 + 2 ^ {x}}{2}} = \mathrm {e} ^ {\lim _ {x \rightarrow 0} \frac {1}{x} \ln \frac {1 + 2 ^ {x}}{2}},</equation>故只需要求<equation>\lim_{x\to 0}\frac{1}{x}\ln \frac{1 + 2^x}{2}</equation>.<equation>\lim _ {x \rightarrow 0} \frac {\ln \frac {1 + 2 ^ {x}}{2}}{x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \left(\frac {2}{1 + 2 ^ {x}} \cdot \frac {2 ^ {x}}{2} \cdot \ln 2\right)=\frac {\ln 2}{2}.</equation>因此，<equation>\lim _ {x \rightarrow 0} \left(\frac {1 + 2 ^ {x}}{2}\right) ^ {\frac {1}{x}} = \mathrm {e} ^ {\frac {\ln 2}{2}} = \sqrt {2}.</equation>（法二）由于<equation>\left(\frac {1 + 2 ^ {x}}{2}\right) ^ {\frac {1}{x}} = \left(1 + \frac {2 ^ {x} - 1}{2}\right) ^ {\frac {1}{x}} = \left[ \left(1 + \frac {2 ^ {x} - 1}{2}\right) ^ {\frac {2}{2 ^ {x} - 1}} \right] ^ {\frac {2 ^ {x} - 1}{2 x}},</equation>而利用重要极限可得<equation>\lim_{x\to 0}\left(1 + \frac{2^x - 1}{2}\right)^{\frac{2}{2^x - 1}} = \mathrm{e},\lim_{x\to 0}\frac{2^x - 1}{2x}\xlongequal{\text{洛必达}}\lim_{x\to 0}\frac{2^x\ln 2}{2} = \frac{\ln 2}{2}</equation>，故<equation>\lim _ {x \rightarrow 0} \left(\frac {1 + 2 ^ {x}}{2}\right) ^ {\frac {1}{x}} = \mathrm {e} ^ {\frac {\ln 2}{2}} = \sqrt {2}.</equation>

---

**2011年第15题 | 解答题 | 10分**
15. (本题满分10分）

已知函数 F(x)<equation>= \frac{\int_{0}^{x}\ln(1+t^{2})\mathrm{d}t}{x^{\alpha}}</equation>. 设<equation>\lim_{x\rightarrow+\infty}F(x)=\lim_{x\rightarrow 0^{+}}F(x)=0</equation>，试求<equation>\alpha</equation>的取值范围.
**答案: **(15) 1 <<equation>\alpha < 3</equation>
**解析: **解记<equation>f ( x )=\int_{0}^{x}\ln(1+t^{2})\mathrm{d} t</equation>，则<equation>F ( x )=\frac{f ( x )}{x^{\alpha}}.</equation>可以看出，<equation>\lim_{x\to 0^{+}}f(x) = 0,</equation><equation>\lim_{x\to +\infty}f(x) = +\infty.</equation><equation>\textcircled{1}</equation><equation>x \to+\infty</equation>时的情形.

当<equation>\alpha \leqslant 0</equation>时，<equation>\lim_{x\to +\infty}\frac{f(x)}{x^{\alpha}} = +\infty</equation>当<equation>\alpha > 0</equation>时，<equation>\lim_{x\to +\infty}\frac{f(x)}{x^{\alpha}}</equation>为<equation>\frac{\infty}{\infty}</equation>型未定式.<equation>\lim _ {x \rightarrow + \infty} \frac {f (x)}{x ^ {\alpha}} \xlongequal {\text {洛 必达}} \lim _ {x \rightarrow + \infty} \frac {\ln \left(1 + x ^ {2}\right)}{\alpha x ^ {\alpha - 1}}.</equation>- 当<equation>0 < \alpha \leqslant 1</equation>时，<equation>\lim_{x\to +\infty}\frac{\ln(1 + x^2)}{\alpha x^{\alpha -1}} = +\infty .</equation>- 当<equation>\alpha >1</equation>时，<equation>\lim_{x\rightarrow +\infty}\frac{\ln(1+x^{2})}{\alpha x^{\alpha-1}}</equation>为<equation>\frac{\infty}{\infty}</equation>型未定式，继续使用洛必达法则得<equation>\begin{aligned} \lim _ {x \rightarrow + \infty} \frac {\ln \left(1 + x ^ {2}\right)}{\alpha x ^ {\alpha - 1}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow + \infty} \frac {\frac {2 x}{x ^ {2} + 1}}{\alpha (\alpha - 1) x ^ {\alpha - 2}} &= \lim _ {x \rightarrow + \infty} \frac {2}{\alpha (\alpha - 1) \left(x ^ {2} + 1\right) x ^ {\alpha - 3}} \\ &= \lim _ {x \rightarrow + \infty} \frac {2}{\alpha (\alpha - 1) x ^ {\alpha - 1} \left(1 + \frac {1}{x ^ {2}}\right)} = \lim _ {x \rightarrow + \infty} \frac {2}{\alpha (\alpha - 1) x ^ {\alpha - 1}} = 0. \end{aligned}</equation>因此，当<equation>\alpha > 1</equation>时，<equation>\lim_{x\to +\infty}\frac{f(x)}{x^{\alpha}} = 0.</equation><equation>\textcircled{2}</equation><equation>x\to 0^{+}</equation>时的情形.

当<equation>\alpha \leqslant 0</equation>时，<equation>\lim_{x\to 0^{+}}\frac{f(x)}{x^{\alpha}} = 0.</equation>当<equation>\alpha > 0</equation>时，<equation>\lim_{x\to 0^{+}}\frac{f(x)}{x^{\alpha}}</equation>为<equation>\frac{0}{0}</equation>型未定式.<equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {f (x)}{x ^ {\alpha}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\ln \left(1 + x ^ {2}\right)}{\alpha x ^ {\alpha - 1}} \xlongequal {\text {~} \ln \left(1 + x ^ {2}\right) \sim x ^ {2}} \lim _ {x \rightarrow 0 ^ {+}} \frac {x ^ {2}}{\alpha x ^ {\alpha - 1}} = \frac {1}{\alpha} \lim _ {x \rightarrow 0 ^ {+}} x ^ {3 - \alpha}.</equation>因此，当<equation>\alpha > 3</equation>时，<equation>\lim_{x\to 0^{+}}\frac{f(x)}{x^{\alpha}}=+\infty</equation>；当<equation>\alpha =3</equation>时，<equation>\lim_{x\to 0^{+}}\frac{f(x)}{x^{3}}=\frac{1}{3}</equation>；当<equation>\alpha < 3</equation>时，<equation>\lim_{x\to 0^{+}}\frac{f(x)}{x^{\alpha}}=0.</equation>综上所述，<equation>1 < \alpha < 3.</equation>

---

**2009年第15题 | 解答题 | 10分**
15. (本题满分9分)

求极限<equation>\lim _ {x \rightarrow 0} \frac {(1 - \cos x) [ x - \ln (1 + \tan x) ]}{\sin^ {4} x}.</equation>
**答案: **<equation>(1 5) \frac {1}{4}.</equation>
**解析: **解 （法一）使用等价无穷小替换结合洛必达法则求极限.

当<equation>x\to0</equation>时，<equation>1-\cos x\sim \frac{1}{2} x^{2},\sin^{4}x\sim x^{4},\tan x\sim x.</equation>因此，<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {(1 - \cos x) [ x - \ln (1 + \tan x) ]}{\sin^ {4} x} &= \lim _ {x \rightarrow 0} \frac {\frac {1}{2} x ^ {2} [ x - \ln (1 + \tan x) ]}{x ^ {4}} = \lim _ {x \rightarrow 0} \frac {x - \ln (1 + \tan x)}{2 x ^ {2}} \\ \underline {{\text {洛必达}}} \lim _ {x \rightarrow 0} \frac {1 - \frac {\sec^ {2} x}{1 + \tan x}}{4 x} &= \lim _ {x \rightarrow 0} \frac {1 + \tan x - \sec^ {2} x}{4 x} \\ &= \lim _ {x \rightarrow 0} \frac {(1 - \tan x) \tan x}{4 x} = \lim _ {x \rightarrow 0} \frac {\tan x}{4 x} \underline {{\frac {\tan x \sim x}{4}}} \frac {1}{4}. \end{aligned}</equation>（法二）同法一的步骤化简原极限式，之后利用泰勒公式来求<equation>\lim_{x\to 0}\frac{x-\ln(1+\tan x)}{2x^{2}}.</equation>利用<equation>\ln(1+x)=x-\frac{1}{2}x^{2}+o\left(x^{2}\right)</equation>得<equation>\ln (1 + \tan x) = \tan x - \frac {\left(\tan x\right) ^ {2}}{2} + o \left(\tan^ {2} x\right) = \tan x - \frac {\left(\tan x\right) ^ {2}}{2} + o \left(x ^ {2}\right).</equation>因此，<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {x - \ln (1 + \tan x)}{2 x ^ {2}} &= \lim _ {x \rightarrow 0} \frac {x - \tan x + \frac {\left(\tan x\right) ^ {2}}{2} - o \left(x ^ {2}\right)}{2 x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\frac {\left(\tan x\right) ^ {2}}{2}}{2 x ^ {2}} + \lim _ {x \rightarrow 0} \frac {x - \tan x}{2 x ^ {2}} \\ \underline {{\text {洛必达}}} \frac {1}{4} + \lim _ {x \rightarrow 0} \frac {1 - \sec^ {2} x}{4 x} &= \frac {1}{4} - \lim _ {x \rightarrow 0} \frac {\tan^ {2} x}{4 x} \\ \underline {{\frac {\tan x - x}{4}}} \frac {1}{4} - \lim _ {x \rightarrow 0} \frac {x}{4} &= \frac {1}{4}. \end{aligned}</equation>因此，原极限<equation>= \frac{1}{4}.</equation>

---


### 一元函数积分学


#### 定积分的应用

**2025年第6题 | 选择题 | 5分 | 答案: B**

6. 设单位质点 P,Q分别位于点（0,0）和（0,1）处，P从点（0,0）出发沿 x正向移动，记 G为引力常量，则当质点 P移动到点（l,0）时，克服质点 Q的引力所做的功为（    ）<equation>\int_ {0} ^ {l} \frac {G}{x ^ {2} + 1} \mathrm {d} x</equation><equation>\int_ {0} ^ {l} \frac {G x}{\left(x ^ {2} + 1\right) ^ {\frac {3}{2}}} \mathrm {d} x</equation><equation>\int_ {0} ^ {l} \frac {G}{\left(x ^ {2} + 1\right) ^ {\frac {3}{2}}} \mathrm {d} x</equation><equation>\int_ {0} ^ {l} \frac {G (x + 1)}{\left(x ^ {2} + 1\right) ^ {\frac {3}{2}}} \mathrm {d} x</equation>

答案: B

**解析:**解 当质点 P从点（0，0）移动到点（l，0）时，引力 F的方向是变化的，始终沿点 P，Q的连线方向，克服质点 Q的引力所做的功等于克服 F沿 x轴方向的分力所做的功.

如图所示，当质点P运动到点<equation>(x,0)</equation>时，单位质点P，Q之间的距离<equation>r = \sqrt{1 + x^2}</equation>，从而引力F的大小为<equation>\frac{G}{1 + x^2}</equation>记PQ与x轴的夹角为<equation>\theta</equation>，则<equation>\cos \theta = \frac{x}{\sqrt{1 + x^2}}</equation>，F沿x轴方向的分力大小为<equation>\frac{G}{1 + x^2}\cdot \cos \theta = \frac{Gx}{(1 + x^2)^{\frac{3}{2}}}</equation>，克服引力的做功元素为<equation>\mathrm{d}W = \frac{Gx}{(1 + x^2)^{\frac{3}{2}}}\mathrm{d}x.</equation>因此，当质点 P从点（0,0）移动到点（l,0）时，克服质点 Q的引力所做的功<equation>W=\int_{0}^{l}\frac{Gx}{\left(1+x^{2}\right)^{\frac{3}{2}}}\mathrm{d}x</equation>，应选B.

---

**2024年第19题 | 解答题 | 12分**

19. (本题满分12分)

设 t>0，平面有界区域 D由曲线<equation>y=\sqrt{x}\mathrm{e}^{-x}</equation>与直线 x=t,x=2t及 x轴围成，D绕 x轴旋转一周所得旋转体的体积为 V(t)，求 V(t) 的最大值.

**答案:**##<equation>\frac{\pi}{1 6} \ln2+\frac{3 \pi}{6 4}</equation>

**解析:**解 根据旋转体的体积公式，<equation>V (t) = \pi \int_ {t} ^ {2 t} \left(\sqrt {x} \mathrm {e} ^ {- x}\right) ^ {2} \mathrm {d} x = \pi \int_ {t} ^ {2 t} x \mathrm {e} ^ {- 2 x} \mathrm {d} x.</equation>由变限积分的求导公式可得，<equation>V ^ {\prime} (t) = \left(\pi \int_ {t} ^ {2 t} x \mathrm {e} ^ {- 2 x} \mathrm {d} x\right) ^ {\prime} = \pi \left(2 \cdot 2 t \mathrm {e} ^ {- 4 t} - t \mathrm {e} ^ {- 2 t}\right) = \pi t \mathrm {e} ^ {- 4 t} \left(4 - \mathrm {e} ^ {2 t}\right).</equation>解<equation>4-\mathrm{e}^{2 t}=0</equation>可得<equation>t=\ln 2</equation>.于是，当<equation>0 < t < \ln 2</equation>时，<equation>V^{\prime}(t)>0,V(t)</equation>单调增加，当<equation>t > \ln 2</equation>时，<equation>V^{\prime}(t)<0,V(t)</equation>单调减少.

因此，<equation>V(t)</equation>的最大值在<equation>t = \ln 2</equation>时取得，最大值为<equation>V(\ln 2)</equation>.

下面用两种方法计算<equation>V(\ln 2).</equation><equation>\begin{aligned} (\text {法 一}) V (\ln 2) &= \pi \int_ {\ln 2} ^ {2 \ln 2} x e ^ {- 2 x} d x = - \frac {\pi}{2} \int_ {\ln 2} ^ {2 \ln 2} x d \left(e ^ {- 2 x}\right) = - \frac {\pi}{2} \left(x e ^ {- 2 x} \left| _ {\ln 2} ^ {2 \ln 2} - \int_ {\ln 2} ^ {2 \ln 2} e ^ {- 2 x} d x \right.\right) \\ &= - \frac {\pi}{2} \left(2 \ln 2 \cdot \frac {1}{1 6} - \ln 2 \cdot \frac {1}{4} + \frac {1}{2} e ^ {- 2 x} \Big | _ {\ln 2} ^ {2 \ln 2}\right) = \frac {\pi}{1 6} \ln 2 - \frac {\pi}{4} \left(\frac {1}{1 6} - \frac {1}{4}\right) \\ &= \frac {\pi}{6 4} (4 \ln 2 + 3). \end{aligned}</equation>（法二）也可以计算出<equation>V(t)</equation>的表达式再代入<equation>t = \ln 2</equation><equation>\begin{aligned} V (t) &= \pi \int_ {t} ^ {2 t} x \mathrm {e} ^ {- 2 x} \mathrm {d} x = - \frac {\pi}{2} \int_ {t} ^ {2 t} x \mathrm {d} \left(\mathrm {e} ^ {- 2 x}\right) = - \frac {\pi}{2} \left(x \mathrm {e} ^ {- 2 x} \Big | _ {t} ^ {2 t} - \int_ {t} ^ {2 t} \mathrm {e} ^ {- 2 x} \mathrm {d} x\right) \\ &= - \frac {\pi}{2} \left(2 t \mathrm {e} ^ {- 4 t} - t \mathrm {e} ^ {- 2 t} + \frac {1}{2} \mathrm {e} ^ {- 2 x} \Big | _ {t} ^ {2 t}\right) = - \frac {\pi}{2} \left(2 t \mathrm {e} ^ {- 4 t} - t \mathrm {e} ^ {- 2 t} + \frac {1}{2} \mathrm {e} ^ {- 4 t} - \frac {1}{2} \mathrm {e} ^ {- 2 t}\right) \\ &= - \frac {\pi}{4} \left[ (4 t + 1) \mathrm {e} ^ {- 4 t} - (2 t + 1) \mathrm {e} ^ {- 2 t} \right]. \end{aligned}</equation>因此，<equation>V (\ln 2) = - \frac {\pi}{4} \left[ \left(4 \ln 2 + 1\right) \cdot \frac {1}{1 6} - \left(2 \ln 2 + 1\right) \cdot \frac {1}{4} \right] = \frac {\pi}{6 4} \left(4 \ln 2 + 3\right).</equation>

---

**2023年第12题 | 填空题 | 5分**

12. 曲线<equation>y=\int_{-\sqrt{3}}^{x}\sqrt{3-t^{2}}\mathrm{d}t</equation>的弧长为 ___

**答案:**#<equation>\frac{4\pi}{3}+\sqrt{3}.</equation>

**解析:**解注意到当<equation>| x | > \sqrt{3}</equation>时，<equation>\sqrt{3-x^{2}}</equation>无定义，故变限积分函数<equation>y=\int_{-\sqrt{3}}^{x}\sqrt{3-t^{2}}\mathrm{d}t</equation>的定义域为<equation>[-\sqrt{3},\sqrt{3}].</equation>由变限积分的求导公式可知，<equation>y ^ {\prime} = \left(\int_ {- \sqrt {3}} ^ {x} \sqrt {3 - t ^ {2}} \mathrm {d} t\right) ^ {\prime} = \sqrt {3 - x ^ {2}}.</equation>由弧长公式可知，曲线的弧长为<equation>\begin{aligned} \int_ {- \sqrt {3}} ^ {\sqrt {3}} \sqrt {1 + \left(y ^ {\prime}\right) ^ {2}} \mathrm {d} x &= \int_ {- \sqrt {3}} ^ {\sqrt {3}} \sqrt {4 - x ^ {2}} \mathrm {d} x \xlongequal {\text {对称性}} 2 \int_ {0} ^ {\sqrt {3}} \sqrt {4 - x ^ {2}} \mathrm {d} x \\ \xlongequal {x = 2 \sin t} 2 \int_ {0} ^ {\frac {\pi}{3}} 2 \cos t \cdot 2 \cos t \mathrm {d} t &= 8 \int_ {0} ^ {\frac {\pi}{3}} \cos^ {2} t \mathrm {d} t \\ &= 8 \int_ {0} ^ {\frac {\pi}{3}} \frac {1 + \cos 2 t}{2} \mathrm {d} t = \frac {4 \pi}{3} + 4 \int_ {0} ^ {\frac {\pi}{3}} \cos 2 t \mathrm {d} t \\ &= \frac {4 \pi}{3} + 2 \sin 2 t \Bigg | _ {0} ^ {\frac {\pi}{3}} = \frac {4 \pi}{3} + \sqrt {3}. \end{aligned}</equation>

---

**2023年第19题 | 解答题 | 12分**

9. (本题满分12分)

已知平面区域<equation>D=\left\{(x,y)\left|0\leqslant y\leqslant \frac{1}{x\sqrt{1+x^{2}}},x\geqslant 1\right.\right\}</equation>I. 求 D的面积；

II. 求 D绕 x轴旋转所成旋转体的体积.

**答案:**( I )<equation>\ln(\sqrt{2}+1)</equation>;

( II )<equation>\pi\left(1-\frac{\pi}{4}\right).</equation>

**解析:**分析 本题主要考查定积分的几何应用.

如图所示，区域 D是由曲线<equation>y=\frac{1}{x\sqrt{1+x^{2}}}</equation>，直线 x=1以及 x轴围成的无界区域，求面积与旋转体的体积时，需要计算反常积分.

解（I）区域 D是由曲线<equation>y=\frac{1}{x\sqrt{1+x^{2}}}</equation>，直线 x=1以及 x轴围成的无界区域，其面积为<equation>\begin{aligned} S &= \int_ {1} ^ {+ \infty} \frac {1}{x \sqrt {1 + x ^ {2}}} \mathrm {d} x \xlongequal {x = \tan t} \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \frac {\mathrm {d} (\tan t)}{\tan t \sqrt {1 + \tan^ {2} t}} = \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \frac {\sec^ {2} t}{\tan t \sec t} \mathrm {d} t \\ &= \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \frac {\mathrm {d} t}{\sin t} = \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \frac {\mathrm {d} (- \cos t)}{1 - \cos^ {2} t} \xlongequal {u = \cos t} \int_ {\frac {\sqrt {2}}{2}} ^ {0} \frac {- \mathrm {d} u}{1 - u ^ {2}} = \frac {1}{2} \int_ {0} ^ {\frac {\sqrt {2}}{2}} \left(\frac {1}{1 - u} + \frac {1}{1 + u}\right) \mathrm {d} u \\ &= \frac {1}{2} \ln \frac {1 + u}{1 - u} \Bigg | _ {0} ^ {\frac {\sqrt {2}}{2}} = \ln (\sqrt {2} + 1). \end{aligned}</equation>（Ⅱ）由旋转体的体积公式可知，区域 D绕 x轴旋转所成旋转体的体积为<equation>\begin{aligned} V &= \int_ {1} ^ {+ \infty} \pi \left(\frac {1}{x \sqrt {1 + x ^ {2}}}\right) ^ {2} \mathrm {d} x = \pi \int_ {1} ^ {+ \infty} \frac {1}{x ^ {2} \left(1 + x ^ {2}\right)} \mathrm {d} x = \pi \int_ {1} ^ {+ \infty} \left(\frac {1}{x ^ {2}} - \frac {1}{1 + x ^ {2}}\right) \mathrm {d} x \\ &= \pi \left(- \frac {1}{x} - \arctan x\right) \Bigg | _ {1} ^ {+ \infty} = \pi \left(1 - \frac {\pi}{4}\right). \end{aligned}</equation>

---

**2022年第15题 | 填空题 | 5分**

15. 已知曲线 L的极坐标方程为<equation>r=\sin 3 \theta\left(0 \leqslant \theta \leqslant \frac{\pi}{3}\right)</equation>，则 L围成的有界区域的面积为 ___

**解析:**<equation>A = \frac {1}{2} \int_ {0} ^ {\frac {\pi}{3}} (\sin 3 \theta) ^ {2} \mathrm {d} \theta = \frac {1}{4} \int_ {0} ^ {\frac {\pi}{3}} (1 - \cos 6 \theta) \mathrm {d} \theta = \frac {\pi}{1 2} - \frac {1}{2 4} \sin 6 \theta \Big | _ {0} ^ {\frac {\pi}{3}} = \frac {\pi}{1 2}.</equation>

---

**2021年第19题 | 解答题 | 12分**

19. (本题满分12分）设函数 f(x)满足<equation>\int\frac{f(x)}{\sqrt{x}} \mathrm{d} x=\frac{1}{6} x^{2}-x+C,L</equation>为曲线 y=f(x)(4≤x≤9). L的弧长为s，L绕x轴旋转一周所形成的曲面面积为A，求s和A.

**答案:**<equation>s = \frac {2 2}{3}, A = \frac {4 2 5 \pi}{9}.</equation>

**解析:**解 对<equation>\int \frac{f(x)}{\sqrt{x}} \mathrm{d} x=\frac{1}{6} x^{2}-x+C</equation>两端关于 x求导，可得<equation>\frac{f(x)}{\sqrt{x}}=\frac{x}{3}-1.</equation>于是，<equation>f(x)=\frac{x^{\frac{3}{2}}}{3}-\sqrt{x}.</equation><equation>f ^ {\prime} (x) = \frac {1}{3} \cdot \frac {3}{2} \cdot \sqrt {x} - \frac {1}{2 \sqrt {x}} = \frac {1}{2} \left(\sqrt {x} - \frac {1}{\sqrt {x}}\right).</equation>L的弧长为<equation>\begin{aligned} s &= \int_ {4} ^ {9} \sqrt {1 + \left[ f ^ {\prime} (x) \right] ^ {2}} \mathrm {d} x = \int_ {4} ^ {9} \sqrt {1 + \frac {1}{4} \left(x + \frac {1}{x} - 2\right)} \mathrm {d} x = \int_ {4} ^ {9} \sqrt {\frac {1}{4} \left(\sqrt {x} + \frac {1}{\sqrt {x}}\right) ^ {2}} \mathrm {d} x \\ &= \frac {1}{2} \int_ {4} ^ {9} \left(\sqrt {x} + \frac {1}{\sqrt {x}}\right) \mathrm {d} x = \frac {1}{2} \left(\frac {2}{3} x ^ {\frac {3}{2}} + 2 \sqrt {x}\right) \Bigg | _ {4} ^ {9} = \left(\frac {1}{3} x ^ {\frac {3}{2}} + \sqrt {x}\right) \Bigg | _ {4} ^ {9} = \frac {2 2}{3}. \end{aligned}</equation>L绕 x轴旋转一周所形成的曲面面积为<equation>\begin{aligned} A &= 2 \pi \int_ {4} ^ {9} f (x) \sqrt {1 + \left[ f ^ {\prime} (x) \right] ^ {2}} d x = 2 \pi \int_ {4} ^ {9} \left(\frac {x ^ {\frac {3}{2}}}{3} - \sqrt {x}\right) \cdot \frac {1}{2} \left(\sqrt {x} + \frac {1}{\sqrt {x}}\right) d x \\ &= \pi \int_ {4} ^ {9} \sqrt {x} \left(\frac {x}{3} - 1\right) \left(\sqrt {x} + \frac {1}{\sqrt {x}}\right) d x = \frac {\pi}{3} \int_ {4} ^ {9} (x - 3) (x + 1) d x = \frac {\pi}{3} \int_ {4} ^ {9} \left(x ^ {2} - 2 x - 3\right) d x \\ &= \frac {\pi}{3} \left. \left(\frac {x ^ {3}}{3} - x ^ {2} - 3 x\right) \right| _ {4} ^ {9} = \frac {4 2 5 \pi}{9}. \end{aligned}</equation>

---

**2020年第12题 | 填空题 | 4分**

12. 斜边长为 2a 等腰直角三角形平板铅直地沉没在水中，且斜边与水面相齐，设重力加速度为 g，水密度为<equation>\rho</equation>，则该平板一侧所受的水压力为___

**答案:**##<equation>\frac{1}{3}\rho g a^{3}.</equation>

**解析:**如图（a）所示建立坐标系.

如图（b）所示，将平板所受水压力按照水深分割为如图中带状阴影区域所受力之和。带状阴影区域近似为矩形区域.该矩形长为 2（a-h），宽为 dh.

(a)

(b)

根据液体压力公式，平板一侧所受的水压力元素<equation>\mathrm{d} F=\rho g h\cdot2(a-h)\mathrm{d} h</equation>其中 h为水的深度，<equation>2(a-h)\mathrm{d} h</equation>为受力面积，h的变化范围为<equation>[0,a]</equation><equation>F = \int_ {0} ^ {a} 2 \rho g h (a - h) \mathrm {d} h = 2 \rho g \int_ {0} ^ {a} \left(a h - h ^ {2}\right) \mathrm {d} h = 2 \rho g \left(\frac {a h ^ {2}}{2} - \frac {h ^ {3}}{3}\right) \Bigg | _ {0} ^ {a} = \frac {1}{3} \rho g a ^ {3}.</equation>

---

**2020年第18题 | 解答题 | 10分**

18. (本题满分10分)

设函数 f(x)的定义域为（0，+∞）且满足<equation>2 f ( x )+x^{2} f \left( \frac{1}{x} \right)=\frac{x^{2}+2 x}{\sqrt{1+x^{2}}}</equation>求 f(x)，并求曲线 y=f(x)，y<equation>=\frac{1}{2},</equation><equation>y=\frac{\sqrt{3}}{2}</equation>及 y轴所围图形绕 x轴旋转一周而成的旋转体的体积.

**答案:**f(x) =<equation>\frac{x}{\sqrt{1+x^{2}}}</equation>，旋转体体积为<equation>\frac{\pi^{2}}{6}.</equation>

**解析:**解 令<equation>\frac{1}{x}=t,t\in(0,+\infty)</equation>，代入<equation>2 f ( x )+x^{2} f \left( \frac{1}{x} \right)=\frac{x^{2}+2 x}{\sqrt{1+x^{2}}}</equation>可得<equation>2 f \left(\frac {1}{t}\right) + \frac {1}{t ^ {2}} f (t) = \frac {\frac {1}{t ^ {2}} + \frac {2}{t}}{\sqrt {1 + \frac {1}{t ^ {2}}}} = \frac {1 + 2 t}{t \sqrt {1 + t ^ {2}}}.</equation>(1) 式中的 t换为 x 可得<equation>2 f \left(\frac {1}{x}\right) + \frac {1}{x ^ {2}} f (x) = \frac {1 + 2 x}{x \sqrt {1 + x ^ {2}}}.</equation>原方程乘以<equation>\frac{2}{x^{2}}</equation>可得<equation>2 f \left(\frac {1}{x}\right) + \frac {4}{x ^ {2}} f (x) = \frac {x ^ {2} + 2 x}{\sqrt {1 + x ^ {2}}} \cdot \frac {2}{x ^ {2}} = \frac {2 (x + 2)}{x \sqrt {1 + x ^ {2}}}.</equation>(3) 式-（2）式消去<equation>f\left(\frac{1}{x}\right)</equation>可得<equation>\frac{3}{x^{2}} f(x)=\frac{3}{x\sqrt{1+x^{2}}}</equation>.解得<equation>f(x)=\frac{x}{\sqrt{1+x^{2}}}</equation>即<equation>y=\frac{x}{\sqrt{1+x^{2}}}</equation>将<equation>y=\frac{x}{\sqrt{1+x^{2}}}</equation>写成<equation>x=g(y)</equation>的形式.

由<equation>y=\frac{x}{\sqrt{1+x^{2}}}</equation>可得<equation>y^{2}=\frac{x^{2}}{1+x^{2}}</equation>，从而<equation>y^{2}+x^{2}y^{2}=x^{2}</equation>即<equation>(1-y^{2})x^{2}=y^{2}</equation>，解得<equation>x^{2}=\frac{y^{2}}{1-y^{2}}</equation>由于<equation>x>0</equation>，故由<equation>y=\frac{x}{\sqrt{1+x^{2}}}</equation>可知<equation>0<y<1.</equation>于是，<equation>x=\frac{y}{\sqrt{1-y^{2}}}.</equation>平面区域如图所示.

由旋转体的体积公式可得，所求旋转体体积<equation>\begin{aligned} V &= 2 \pi \int_ {\frac {1}{2}} ^ {\frac {\sqrt {3}}{2}} y g (y) \mathrm {d} y = 2 \pi \int_ {\frac {1}{2}} ^ {\frac {\sqrt {3}}{2}} \frac {y ^ {2}}{\sqrt {1 - y ^ {2}}} \mathrm {d} y \underline {{y = \sin t}} 2 \pi \int_ {\frac {\pi}{6}} ^ {\frac {\pi}{3}} \frac {\sin^ {2} t}{\cos t} \cdot \cos t \mathrm {d} t \\ &= 2 \pi \int_ {\frac {\pi}{6}} ^ {\frac {\pi}{3}} \sin^ {2} t \mathrm {d} t = 2 \pi \int_ {\frac {\pi}{6}} ^ {\frac {\pi}{3}} \frac {1 - \cos 2 t}{2} \mathrm {d} t = \pi \left(t - \frac {\sin 2 t}{2}\right) \Bigg | _ {\frac {\pi}{6}} ^ {\frac {\pi}{3}} \\ \frac {\sin \frac {\pi}{3} = \sin \frac {2 \pi}{3}}{\pi} \frac {\pi^ {2}}{6} - 0 &= \frac {\pi^ {2}}{6}. \end{aligned}</equation>

---

**2019年第12题 | 填空题 | 4分**

12. 曲线<equation>y=\ln\cos x\left(0\leqslant x\leqslant\frac{\pi}{6}\right)</equation>的弧长为 ___

**答案:**##<equation>\frac{1}{2} \ln 3.</equation>

**解析:**计算<equation>y^{\prime}。</equation><equation>y ^ {\prime} = (\ln \cos x) ^ {\prime} = \frac {- \sin x}{\cos x} = - \tan x.</equation>由曲线弧长公式，可得所求弧长为<equation>\begin{aligned} s &= \int_ {0} ^ {\frac {\pi}{6}} \sqrt {1 + \left(y ^ {\prime}\right) ^ {2}} \mathrm {d} x = \int_ {0} ^ {\frac {\pi}{6}} \sqrt {1 + \tan^ {2} x} \mathrm {d} x = \int_ {0} ^ {\frac {\pi}{6}} \sec x \mathrm {d} x = \ln | \sec x + \tan x | \Bigg | _ {0} ^ {\frac {\pi}{6}} \\ &= \ln \left(\frac {2}{\sqrt {3}} + \frac {1}{\sqrt {3}}\right) = \frac {1}{2} \ln 3. \end{aligned}</equation>

---

**2018年第20题 | 解答题 | 11分**

20. (本题满分11分)

已知曲线 L：<equation>y=\frac{4}{9} x^{2} ( x\geqslant0)</equation>，点 O(0,0)，点 A(0,1).设 P是 L上的动点，S是直线 OA与直线 AP及曲线 L所围图形的面积.若 P运动到点（3,4）时沿 x轴正向的速度是4，求此时 S关于时间 t的变化率.

**解析:**本题中，既可以利用定积分计算 S，也可以利用二重积分计算 S.

解曲线 L如图所示，直线 OA与直线 AP及曲线 L所围区域为 D.设点 P的坐标为（x,y），过点 P作 x轴的垂线，垂足为 Q，则点 Q的坐标为（x,0）.由于点 P位于曲线 L上，故点 P的坐标可写为<equation>\left(x,\frac{4}{9} x^{2}\right).</equation>下面用三种方法计算 S.

（法一）区域 D的面积 S等于梯形 OAPQ的面积<equation>S_{1}</equation>减去曲边三角形 OPQ的面积<equation>S_{2}.</equation>由图可知，梯形OAPQ的两条底边长分别为1和<equation>\frac{4}{9} x^{2}</equation>，高为x.根据梯形的面积公式，<equation>S_{1}= \frac{1+\frac{4}{9} x^{2}}{2} \cdot x=\frac{2}{9} x^{3}+\frac{x}{2}.</equation>根据定积分的几何意义，曲边三角形 OPQ的面积<equation>S_{2}=\int_{0}^{x}\frac{4}{9} t^{2}\mathrm{d}t=\frac{4}{27} x^{3}.</equation>因此，<equation>S = S _ {1} - S _ {2} = \frac {2}{9} x ^ {3} + \frac {x}{2} - \frac {4}{2 7} x ^ {3} = \frac {2}{2 7} x ^ {3} + \frac {x}{2}.</equation>（法二）直线 AP的方程为<equation>Y - 1 = \frac {\frac {4}{9} x ^ {2} - 1}{x - 0} (X - 0), \quad \mathrm {即} Y = \left(\frac {4}{9} x - \frac {1}{x}\right) X + 1.</equation>根据定积分的几何意义，<equation>S = \int_ {0} ^ {x} \left[ \left(\frac {4}{9} x - \frac {1}{x}\right) t + 1 - \frac {4}{9} t ^ {2} \right] \mathrm {d} t = \left(\frac {4}{9} x - \frac {1}{x}\right) \cdot \frac {x ^ {2}}{2} + x - \frac {4}{2 7} x ^ {3} = \frac {2}{2 7} x ^ {3} + \frac {x}{2}.</equation>（法三）由法二可得直线 AP的方程为<equation>Y=\left(\frac{4}{9} x-\frac{1}{x}\right) X+1.</equation>将区域 D看作X型区域，区域 D可表示为<equation>D = \left\{(X, Y) \mid \frac {4}{9} X ^ {2} \leqslant Y \leqslant \left(\frac {4}{9} x - \frac {1}{x}\right) X + 1, 0 \leqslant X \leqslant x \right\}.</equation>根据二重积分的几何意义，<equation>\begin{aligned} S &= \iint_ {D} \mathrm {d} X \mathrm {d} Y = \int_ {0} ^ {x} \mathrm {d} X \int_ {\frac {4}{9} X ^ {2}} ^ {\left(\frac {4}{9} x - \frac {1}{x}\right) X + 1} \mathrm {d} Y = \int_ {0} ^ {x} \left[ \left(\frac {4}{9} x - \frac {1}{x}\right) X + 1 - \frac {4}{9} X ^ {2} \right] \mathrm {d} X \\ &= \left(\frac {4}{9} x - \frac {1}{x}\right) \cdot \frac {x ^ {2}}{2} + x - \frac {4}{2 7} x ^ {3} = \frac {2}{2 7} x ^ {3} + \frac {x}{2}. \end{aligned}</equation>根据链式法则，<equation>\frac {\mathrm {d} S}{\mathrm {d} t} = \frac {\mathrm {d} S}{\mathrm {d} x} \cdot \frac {\mathrm {d} x}{\mathrm {d} t} = \left(\frac {2}{9} x ^ {2} + \frac {1}{2}\right) \cdot \frac {\mathrm {d} x}{\mathrm {d} t}.</equation>当 x=3时，<equation>\left.\frac{\mathrm{d}x}{\mathrm{d}t}\right|_{x=3}=4.</equation>因此，<equation>\left. \frac {\mathrm {d} S}{\mathrm {d} t} \right| _ {x = 3} = \left(\frac {2}{9} x ^ {2} + \frac {1}{2}\right) \cdot \left. \frac {\mathrm {d} x}{\mathrm {d} t} \right| _ {x = 3} = \left(\frac {2}{9} \times 9 + \frac {1}{2}\right) \times 4 = 1 0.</equation>因此，所求 S关于时间 t的变化率为10.

---

**2017年第6题 | 选择题 | 4分 | 答案: C**

6. 甲，乙两人赛跑，计时开始时，甲在乙前方10（单位：m）处，图中，实线表示甲的速度曲线<equation>v=v_{1}(t)</equation>（单位：m/s），虚线表示乙的速度曲线<equation>v=v_{2}(t)</equation>，三块阴影部分面积的数值依次为10，20，3. 计时开始后乙追上甲的时刻记为<equation>t_{0}</equation>（单位：s），则（    ）

A.<equation>t_{0}=1 0</equation>B.<equation>1 5<t_{0}<2 0</equation>C.<equation>t_{0}=2 5</equation>D.<equation>t_{0}>2 5</equation>

答案: C

**解析:**解 根据定积分的物理意义，从0s到10s这段时间内，实线位于虚线之上，于是甲跑过的路程比乙跑过的路程多<equation>1 0 \mathrm{~m}</equation>；从10s到25s这段时间内，虚线位于实线之上，于是乙跑过的路程比甲跑过的路程多<equation>2 0 \mathrm{~m}.</equation>由于在计时开始时，甲领先乙10m，故到25s时，甲与乙之间的距离为<equation>1 0+1 0-2 0=0</equation>（m），即乙追上甲.

因此，应选C.

---

**2016年第20题 | 解答题 | 11分**

20. (本题满分11分)

设 D是由曲线<equation>y=\sqrt{1-x^{2}}</equation>（0≤x≤1）与<equation>\left\{\begin{array}{l l}x=\cos^{3} t,\\ y=\sin^{3} t\end{array}\right.</equation><equation>\left(0\leq t\leq \frac{\pi}{2}\right)</equation>围成的平面区域，求 D绕 x轴旋转一周所得旋转体的体积和表面积.

**答案:**体积<equation>\frac{18}{35}\pi</equation>，表面积<equation>\frac{16}{5}\pi.</equation>

**解析:**区域 D 如图所示.

记曲线<equation>l_{1}:y_{1}=\sqrt{1-x^{2}}(0\leqslant x\leqslant 1)</equation>与x轴，y轴围成的区域为<equation>D_{1}</equation>曲线<equation>l_{2}:\left\{\begin{array}{l l}x=\cos^{3}t,\\ y=\sin^{3}t\end{array}\right. \left(0\leqslant t\leqslant \frac{\pi}{2}\right)</equation>与x轴，y轴围成的区域为<equation>D_{2}.</equation>D绕 x轴旋转一周所得旋转体的体积可以看作由<equation>D_{1}</equation>绕 x轴旋转一周所得旋转体的体积<equation>V_{1}</equation>减去由<equation>D_{2}</equation>绕 x轴旋转一周所得旋转体的体积<equation>V_{2}.</equation>D绕 x轴旋转一周所得旋转体的表面积可以看作由曲线<equation>l_{1}</equation>绕 x轴旋转一周所得曲面的表面积<equation>S_{1}</equation>加上由曲线<equation>l_{2}</equation>绕 x轴旋转一周所得曲面的表面积<equation>S_{2}.</equation><equation>D_{1}</equation>绕x轴旋转一周所得旋转体为球心在原点，半径为1的半球体，其体积<equation>V_{1}=\frac{1}{2}\times \frac{4}{3}\pi =\frac{2\pi}{3}</equation>表面积<equation>S_{1}=\frac{1}{2}\times 4\pi =2\pi.</equation>此外，可求得两条曲线的交点为（1，0）和（0，1）.

下面我们用两种方法来计算所得旋转体的体积与表面积.

（法一）利用<equation>l_{2}</equation>的参数方程，找出曲线交点所对应的 t.交点（1，0）对应 t=0，交点（0，1）对应<equation>t=\frac{\pi}{2}.</equation><equation>V _ {2} = \pi \int_ {0} ^ {1} y ^ {2} \mathrm {d} x \xlongequal {x = \cos^ {3} t} \pi \int_ {\frac {\pi}{2}} ^ {0} \sin^ {6} t \cdot 3 \cos^ {2} t (- \sin t) \mathrm {d} t = 3 \pi \int_ {0} ^ {\frac {\pi}{2}} \sin^ {7} t \cos^ {2} t \mathrm {d} t,</equation><equation>\begin{aligned} V _ {1} - V _ {2} &= \frac {2 \pi}{3} - 3 \pi \int_ {0} ^ {\frac {\pi}{2}} \sin^ {7} t \cos^ {2} t \mathrm {d} t = \frac {2 \pi}{3} - 3 \pi \int_ {0} ^ {\frac {\pi}{2}} \left[ \sin^ {7} t \left(1 - \sin^ {2} t\right) \right] \mathrm {d} t \\ &= \frac {2 \pi}{3} - 3 \pi \int_ {0} ^ {\frac {\pi}{2}} \left(\sin^ {7} t - \sin^ {9} t\right) \mathrm {d} t = \frac {2 \pi}{3} - 3 \pi \times \left(\frac {6}{7} \times \frac {4}{5} \times \frac {2}{3} - \frac {8}{9} \times \frac {6}{7} \times \frac {4}{5} \times \frac {2}{3}\right) = \frac {1 8}{3 5} \pi . \end{aligned}</equation><equation>\begin{aligned} S _ {2} &= 2 \pi \int_ {0} ^ {1} y \mathrm {d} s = 2 \pi \int_ {0} ^ {\frac {\pi}{2}} \sin^ {3} t \sqrt {\left[ 3 \cos^ {2} t (- \sin t) \right] ^ {2} + \left(3 \sin^ {2} t \cos t\right) ^ {2}} \mathrm {d} t \\ &= 2 \pi \int_ {0} ^ {\frac {\pi}{2}} \sin^ {3} t \cdot 3 \cos t \sin t \mathrm {d} t = 6 \pi \int_ {0} ^ {\frac {\pi}{2}} \sin^ {4} t \mathrm {d} (\sin t) = \frac {6}{5} \pi . \end{aligned}</equation>因此，<equation>V=\frac{1 8}{3 5}\pi</equation><equation>S=2\pi+\frac{6}{5}\pi=\frac{1 6}{5}\pi.</equation>（法二）写出曲线<equation>l_{2}:\left\{ \begin{array}{l l} x=\cos^{3} t, \\ y=\sin^{3} t \end{array} \right. \left( 0\leqslant t\leqslant \frac{\pi}{2} \right)</equation>的显式表达式.

由<equation>\cos^{2} t+\sin^{2} t=1</equation>可得，<equation>x^{\frac{2}{3}}+y^{\frac{2}{3}}=1.</equation>由于<equation>0\leqslant x\leqslant 1, 0\leqslant y\leqslant 1</equation>，故<equation>y=(1-x^{\frac{2}{3}})^{\frac{3}{2}}</equation>（<equation>0\leqslant x\leqslant 1</equation>）.于是，<equation>\begin{aligned} V &= V _ {1} - V _ {2} = \pi \int_ {0} ^ {1} \left(1 - x ^ {2}\right) \mathrm {d} x - \pi \int_ {0} ^ {1} \left(1 - x ^ {\frac {2}{3}}\right) ^ {3} \mathrm {d} x \\ &= \pi \int_ {0} ^ {1} \left(1 - x ^ {2}\right) \mathrm {d} x - \pi \int_ {0} ^ {1} \left(1 - 3 x ^ {\frac {2}{3}} + 3 x ^ {\frac {4}{3}} - x ^ {2}\right) \mathrm {d} x \\ &= 3 \pi \int_ {0} ^ {1} \left(x ^ {\frac {2}{3}} - x ^ {\frac {4}{3}}\right) \mathrm {d} x = 3 \pi \left(\frac {3}{5} - \frac {3}{7}\right) = \frac {1 8}{3 5} \pi . \end{aligned}</equation>下面计算<equation>S_{2}.</equation><equation>y ^ {\prime} (x) = \frac {3}{2} \left(1 - x ^ {\frac {2}{3}}\right) ^ {\frac {1}{2}} \cdot \left(- \frac {2}{3}\right) \cdot x ^ {- \frac {1}{3}} = - \left(1 - x ^ {\frac {2}{3}}\right) ^ {\frac {1}{2}} \cdot x ^ {- \frac {1}{3}}.</equation><equation>\begin{aligned} S _ {2} &= 2 \pi \int_ {0} ^ {1} y \mathrm {d} s = 2 \pi \int_ {0} ^ {1} \left(1 - x ^ {\frac {2}{3}}\right) ^ {\frac {3}{2}} \sqrt {1 + \left(y ^ {\prime}\right) ^ {2}} \mathrm {d} x = 2 \pi \int_ {0} ^ {1} \left(1 - x ^ {\frac {2}{3}}\right) ^ {\frac {3}{2}} \sqrt {1 + \left(1 - x ^ {\frac {2}{3}}\right) \cdot x ^ {- \frac {2}{3}}} \mathrm {d} x \\ &= 2 \pi \int_ {0} ^ {1} \left(1 - x ^ {\frac {2}{3}}\right) ^ {\frac {3}{2}} \cdot x ^ {- \frac {1}{3}} \mathrm {d} x = 2 \pi \int_ {0} ^ {1} \left(1 - x ^ {\frac {2}{3}}\right) ^ {\frac {3}{2}} \mathrm {d} \left(\frac {3}{2} x ^ {\frac {2}{3}}\right) \xlongequal {u = x ^ {\frac {2}{3}}} 3 \pi \int_ {0} ^ {1} (1 - u) ^ {\frac {3}{2}} \mathrm {d} u \\ &= 3 \pi \cdot - \frac {2}{5} (1 - u) ^ {\frac {5}{2}} \Bigg | _ {0} ^ {1} = \frac {6}{5} \pi . \end{aligned}</equation>因此，<equation>V=\frac{1 8}{3 5}\pi , S=2\pi +\frac{6}{5}\pi =\frac{1 6}{5}\pi.</equation>

---

**2015年第16题 | 解答题 | 10分**

16. (本题满分10分)

设 A > 0,D是由曲线段 y = A sin x<equation>\left( 0\leqslant x\leqslant\frac{\pi}{2} \right)</equation>及直线 y=0,x<equation>= \frac{\pi}{2}</equation>所围成的平面区域，<equation>V_{1},V_{2}</equation>分别表示 D绕 x轴与绕 y轴旋转所成旋转体的体积.若<equation>V_{1}=V_{2}</equation>，求 A的值.

**答案:**<equation>(1 6) \frac {8}{\pi}.</equation>

**解析:**解 （法一）由旋转体的体积计算公式，可得<equation>V _ {1} = \pi \int_ {0} ^ {\frac {\pi}{2}} \left(A \sin x\right) ^ {2} \mathrm {d} x = \frac {A ^ {2} \pi}{2} \int_ {0} ^ {\frac {\pi}{2}} \left(1 - \cos 2 x\right) \mathrm {d} x = \frac {A ^ {2} \pi^ {2}}{4},</equation><equation>\begin{aligned} V _ {2} &= 2 \pi \int_ {0} ^ {\frac {\pi}{2}} x A \sin x \mathrm {d} x = 2 A \pi \int_ {0} ^ {\frac {\pi}{2}} x \sin x \mathrm {d} x = - 2 A \pi \int_ {0} ^ {\frac {\pi}{2}} x \mathrm {d} (\cos x) \\ &= - 2 A \pi \left(x \cos x \Big | _ {0} ^ {\frac {\pi}{2}} - \int_ {0} ^ {\frac {\pi}{2}} \cos x \mathrm {d} x\right) = 2 A \pi . \end{aligned}</equation>由<equation>V_{1} = V_{2}</equation>得，<equation>\frac{A^2\pi^2}{4} = 2A\pi</equation>，从而可得<equation>A = 0</equation>或<equation>A = \frac{8}{\pi}</equation>.由于<equation>A > 0</equation>，故<equation>A = \frac{8}{\pi}</equation>（法二）如图所示，<equation>V_{2}</equation>可看作由底面半径为<equation>\frac{\pi}{2}</equation>高为A的圆柱体体积减去<equation>D^{\prime}</equation>绕y轴旋转所得旋转体的体积<equation>V_{2}^{\prime}</equation>所得.

底面半径为<equation>\frac{\pi}{2}</equation>，高为 A的圆柱体体积<equation>= \frac{A\pi^{3}}{4}</equation><equation>D^{\prime}</equation>为由<equation>y=A</equation>，<equation>x=0</equation>以及<equation>y=A\sin x</equation>即<equation>x=\arcsin \frac{y}{A}</equation>围成

的区域. 由旋转体的体积公式可得<equation>V _ {2} ^ {\prime} = \pi \int_ {0} ^ {A} \left(\arcsin \frac {y}{A}\right) ^ {2} \mathrm {d} y \xlongequal {y = A \sin u} A \pi \int_ {0} ^ {\frac {\pi}{2}} u ^ {2} \cos u \mathrm {d} u = A \pi \int_ {0} ^ {\frac {\pi}{2}} u ^ {2} \mathrm {d} (\sin u) = A \pi \left(\frac {\pi^ {2}}{4} - 2\right).</equation>因此，<equation>V_{2}=\frac{A\pi^{3}}{4}-A\pi\left(\frac{\pi^{2}}{4}-2\right)=2A\pi.</equation>其余同法一.

---

**2014年第13题 | 填空题 | 4分**

13. 一根长度为1的细棒位于 x轴的区间 [0,1] 上，若其线密度<equation>\rho(x)=-x^{2}+2 x+1</equation>，则该细棒的质心坐标<equation>\bar{x}=</equation>

**答案:**# 11 20.

**解析:**由于<equation>\int_ {0} ^ {1} \rho (x) \mathrm {d} x = \int_ {0} ^ {1} \left(- x ^ {2} + 2 x + 1\right) \mathrm {d} x = \left. \left(- \frac {x ^ {3}}{3} + x ^ {2} + x\right) \right| _ {0} ^ {1} = \frac {5}{3},</equation><equation>\int_ {0} ^ {1} x \rho (x) \mathrm {d} x = \int_ {0} ^ {1} \left(- x ^ {3} + 2 x ^ {2} + x\right) \mathrm {d} x = \left. \left(- \frac {x ^ {4}}{4} + \frac {2}{3} x ^ {3} + \frac {1}{2} x ^ {2}\right) \right| _ {0} ^ {1} = \frac {1 1}{1 2},</equation>故<equation>\bar{x}=\frac{11}{12}\times \frac{3}{5}=\frac{11}{20}.</equation>

---

**2014年第21题 | 解答题 | 11分**

21. (本题满分11分)

已知函数 f(x,y)满足<equation>\frac{\partial f}{\partial y}=2(y+1)</equation>，且 f(y,y)<equation>= ( y+1 )^{2}-( 2-y ) \ln y</equation>，求曲线 f(x,y)=0所围图形绕直线 y=-1旋转所成旋转体的体积.

**答案:**<equation>(2 1) \left(2 \ln 2 - \frac {5}{4}\right) \pi .</equation>

**解析:**解 由<equation>\frac{\partial f}{\partial y}=2(y+1)</equation>得<equation>f (x, y) = \int 2 (y + 1) \mathrm {d} y = (y + 1) ^ {2} + g (x).</equation>又由于<equation>f ( y, y ) = ( y + 1 )^{2} - ( 2 - y ) \ln y</equation>，故<equation>g ( x ) =</equation><equation>- ( 2 - x ) \ln x.</equation>因此，<equation>f ( x, y ) = ( y + 1 )^{2} - ( 2 - x ) \ln x.</equation>曲线<equation>f ( x, y )=0</equation>的方程为<equation>( y+1 )^{2}=( 2-x ) \ln x.</equation>由<equation>( y+1 )^{2} \geqslant 0</equation>可得该曲线上的点的横坐标满足<equation>( 2-x)\ln x \geqslant 0</equation>，解得<equation>1\leqslant x\leqslant 2</equation>，而曲线上的点（x，y）到旋转轴<equation>y=-1</equation>的距离为y+1，故曲线所围图形绕<equation>y=-1</equation>旋转所得旋转体的体积为<equation>\begin{aligned} V &= \pi \int_ {1} ^ {2} (y + 1) ^ {2} \mathrm {d} x = \pi \int_ {1} ^ {2} (2 - x) \ln x \mathrm {d} x = - \pi \int_ {1} ^ {2} \ln x \mathrm {d} \left[ \frac {(2 - x) ^ {2}}{2} \right] \\ &= - \pi \left[ \ln x \cdot \frac {(2 - x) ^ {2}}{2} \right| _ {1} ^ {2} - \int_ {1} ^ {2} \frac {(2 - x) ^ {2}}{2} \cdot \frac {1}{x} \mathrm {d} x ] = \pi \int_ {1} ^ {2} \left(\frac {x}{2} - 2 + \frac {2}{x}\right) \mathrm {d} x \\ &= \pi \left(\frac {x ^ {2}}{4} - 2 x + 2 \ln x\right) \Bigg | _ {1} ^ {2} = \left(2 \ln 2 - \frac {5}{4}\right) \pi . \end{aligned}</equation>

---

**2013年第11题 | 填空题 | 4分**

11. 设封闭曲线<equation>L</equation>的极坐标方程为<equation>r=\cos 3\theta \left(-\frac{\pi}{6}\leqslant \theta \leqslant \frac{\pi}{6}\right)</equation>，则<equation>L</equation>所围平面图形的面积是 ___

**解析:**## 分析 本题主要考查定积分在几何上的应用.

本题中的曲线是由极坐标形式给出的.对于由极坐标形式<equation>r = r(\theta)</equation>（<equation>\alpha\leqslant\theta\leqslant\beta)</equation>）给出的封闭曲线 L，其围成的平面图形的面积为<equation>A=\int_{\alpha}^{\beta}\frac{1}{2}[r(\theta)]^{2}\mathrm{d}\theta.</equation>如图所示，本题中的曲线 L是“三叶玫瑰线”的一个花瓣，图中蓝色曲线为 L. 由图可知，曲线 L关于极轴对称.

由面积公式得<equation>A = \frac {1}{2} \int_ {- \frac {\pi}{6}} ^ {\frac {\pi}{6}} (\cos 3 \theta) ^ {2} \mathrm {d} \theta \xlongequal {\text {对称 性}} \int_ {0} ^ {\frac {\pi}{6}} (\cos 3 \theta) ^ {2} \mathrm {d} \theta = \frac {1}{2} \int_ {0} ^ {\frac {\pi}{6}} (1 + \cos 6 \theta) \mathrm {d} \theta = \frac {1}{2} \left(\frac {\pi}{6} + 0\right) = \frac {\pi}{1 2}.</equation>

---

**2013年第16题 | 解答题 | 10分**

16. (本题满分10分)

设 D是由曲线<equation>y=x^{\frac{1}{3}}</equation>，直线 x=a（a>0）及 x轴所围成的平面图形，<equation>V_{x},V_{y}</equation>分别是 D绕 x轴，y轴旋转一周所得旋转体的体积.若<equation>V_{y}=1 0 V_{x}</equation>，求 a的值.

**解析:**解（法一）<equation>D</equation>绕<equation>x</equation>轴旋转所得的旋转体的体积<equation>V_{x}</equation>为<equation>V _ {x} = \pi \int_ {0} ^ {a} \left(x ^ {\frac {1}{3}}\right) ^ {2} \mathrm {d} x = \frac {3 \pi}{5} x ^ {\frac {5}{3}} \Bigg | _ {0} ^ {a} = \frac {3 \pi}{5} a ^ {\frac {5}{3}}.</equation><equation>D</equation>绕<equation>y</equation>轴旋转所得旋转体的体积<equation>V_{y}</equation>为<equation>V _ {y} = 2 \pi \int_ {0} ^ {a} x \cdot x ^ {\frac {1}{3}} \mathrm {d} x = 2 \pi \cdot \frac {3}{7} a ^ {\frac {7}{3}} = \frac {6 \pi}{7} a ^ {\frac {7}{3}}.</equation>由于<equation>V_{y}=1 0 V_{x}</equation>，故<equation>\frac{6\pi}{7} a^{\frac{7}{3}}=1 0\cdot \frac{3\pi}{5} a^{\frac{5}{3}}.</equation>整理得<equation>a ^ {\frac {5}{3}} \left(6 \pi - \frac {6 \pi}{7} a ^ {\frac {2}{3}}\right) = 0.</equation>因此，<equation>a = 0</equation>或<equation>a^{\frac{2}{3}} = 7.</equation>由题设知，<equation>a > 0</equation>，故<equation>a^{\frac{2}{3}} = 7</equation>，即<equation>a = 7\sqrt{7}.</equation>（法二）D绕y轴旋转所得旋转体的体积<equation>V_{y}</equation>为底面半径为a，高为<equation>a^{\frac{1}{3}}</equation>的圆柱体体积减去<equation>D^{\prime}</equation>（如图，由曲线<equation>y=x^{\frac{1}{3}}</equation>，直线<equation>y=a^{\frac{1}{3}}</equation>与y轴围成）绕 y轴旋转所得旋转体的体积<equation>V_{y}^{\prime}.</equation>圆柱体的体积<equation>V=\pi a^{2}\cdot a^{\frac{1}{3}}=\pi a^{\frac{7}{3}}.</equation><equation>V _ {y} ^ {\prime} = \pi \int_ {0} ^ {a ^ {\frac {1}{3}}} \left(y ^ {3}\right) ^ {2} \mathrm {d} y = \frac {\pi}{7} y ^ {7} \Bigg | _ {0} ^ {a ^ {\frac {1}{3}}} = \frac {\pi}{7} a ^ {\frac {7}{3}}.</equation>因此，<equation>V_{y}=\pi a^{\frac{7}{3}}-\frac{\pi}{7} a^{\frac{7}{3}}=\frac{6\pi}{7} a^{\frac{7}{3}}.</equation>其余同法一.

---

**2012年第17题 | 解答题 | 10分**

17. (本题满分12分)

过点（0,1）作曲线 L：<equation>y=\ln x</equation>的切线，切点为 A，又 L与 x轴交于 B点，区域 D由 L与直线 AB围成.求区域 D的面积及 D绕 x轴旋转一周所得旋转体的体积.

**答案:**(17) D的面积为2，旋转体的体积为<equation>\frac{2\pi}{3} \left( \mathrm{e}^{2}-1 \right).</equation>

**解析:**分析 本题主要考查利用定积分求平面图形面积及求旋转体的体积. 解题时，最好是能画出大致图形.

解<equation>\textcircled{1}</equation>求区域 D的面积.

（法一）过点A作<equation>x</equation>轴的垂线AC，因此D的面积为曲线L与直线AC，<equation>x</equation>轴围成的曲边三角形ABC的面积减去<equation>\triangle ABC</equation>的面积.

下面求点 A和点 B的坐标.

由于曲线<equation>L</equation>的方程为<equation>y = \ln x</equation>，故<equation>y^{\prime} = \frac{1}{x}</equation>.于是过点<equation>A(x_{0},y_{0})</equation>的曲线<equation>L</equation>的切线斜率为<equation>\frac{1}{x_0}</equation>，且该切线过点（0，1），故由斜率公式知<equation>\frac{y_0 - 1}{x_0} = \frac{1}{x_0}</equation>.解该方程得<equation>y_{0} = 2</equation>.代入曲线<equation>L</equation>的方程得<equation>x_0 = \mathrm{e}^2</equation>因此，点<equation>A</equation>的坐标为<equation>(\mathrm{e}^2,2)</equation>.

另一方面，由于曲线 L与 x轴交于点 B，故点 B的坐标<equation>\left(x_{1},y_{1}\right)</equation>满足<equation>\ln x_{1}=0</equation>因此<equation>x_{1}=1</equation>点 B的坐标为（1，0）.

根据三角形的面积公式以及定积分的几何意义，<equation>S _ {\triangle A B C} = \frac {1}{2} \times 2 \times \left(\mathrm {e} ^ {2} - 1\right) = \mathrm {e} ^ {2} - 1,</equation><equation>S _ {\text {曲 边 三 角形} A B C} = \int_ {1} ^ {e ^ {2}} \ln x \mathrm {d} x = x \ln x \left| _ {1} ^ {e ^ {2}} - \int_ {1} ^ {e ^ {2}} \mathrm {d} x = 2 \mathrm {e} ^ {2} - \left(\mathrm {e} ^ {2} - 1\right) = \mathrm {e} ^ {2} + 1. \right.</equation>因此，区域 D的面积<equation>= \mathrm{e}^{2}+1-(\mathrm{e}^{2}-1) = 2.</equation>（法二）由点 A和点 B的坐标求出直线 AB的方程，进而可利用二重积分来求区域 D的面积由法一中得到的点 A和点 B的坐标可求出直线 AB的方程，<equation>y=\frac{2} {\mathrm{e}^{2}-1} (x-1).</equation>因此，区域 D可表示为<equation>D = \left\{(x, y) \mid \frac {2}{\mathrm {e} ^ {2} - 1} (x - 1) \leqslant y \leqslant \ln x, 1 \leqslant x \leqslant \mathrm {e} ^ {2} \right\}.</equation>D的面积S为<equation>\begin{aligned} S &= \iint_ {D} \mathrm {d} \sigma = \int_ {1} ^ {\mathrm {e} ^ {2}} \mathrm {d} x \int_ {\frac {2}{\mathrm {e} ^ {2} - 1} (x - 1)} ^ {\ln x} \mathrm {d} y = \int_ {1} ^ {\mathrm {e} ^ {2}} \left[ \ln x - \frac {2}{\mathrm {e} ^ {2} - 1} (x - 1) \right] \mathrm {d} x \\ &= \int_ {1} ^ {\mathrm {e} ^ {2}} \ln x \mathrm {d} x - \frac {2}{\mathrm {e} ^ {2} - 1} \int_ {1} ^ {\mathrm {e} ^ {2}} (x - 1) \mathrm {d} x = \mathrm {e} ^ {2} + 1 - \left(\mathrm {e} ^ {2} - 1\right) = 2. \end{aligned}</equation><equation>\textcircled{2}</equation>求旋转体的体积.

D绕x轴旋转一周的体积V可以看作曲边三角形ABC绕x轴旋转一周得到的旋转体体积<equation>V_{1}</equation>减去<equation>\triangle ABC</equation>绕x轴旋转一周得到的圆锥体体积<equation>V_{2}.</equation>由于该圆锥体的底面半径为2，高为<equation>\mathrm{e}^{2}-1</equation>，故由圆锥体的体积公式可得，<equation>V_{2}=\frac{4\pi}{3} \left( \mathrm{e}^{2}-1 \right).</equation>由旋转体的体积公式可得<equation>V _ {1} = \pi \int_ {1} ^ {\mathrm {e} ^ {2}} (\ln x) ^ {2} \mathrm {d} x = \pi \left[ x (\ln x) ^ {2} \Big | _ {1} ^ {\mathrm {e} ^ {2}} - 2 \int_ {1} ^ {\mathrm {e} ^ {2}} \ln x \mathrm {d} x \right] = \pi \left[ 4 \mathrm {e} ^ {2} - 2 \left(\mathrm {e} ^ {2} + 1\right) \right] = 2 \pi \left(\mathrm {e} ^ {2} - 1\right).</equation>因此，<equation>V = V _ {1} - V _ {2} = 2 \pi \left(\mathrm {e} ^ {2} - 1\right) - \frac {4 \pi}{3} \left(\mathrm {e} ^ {2} - 1\right) = \frac {2 \pi}{3} \left(\mathrm {e} ^ {2} - 1\right).</equation>

---

**2011年第11题 | 填空题 | 4分**

11. 曲线<equation>y=\int_{0}^{x}\tan t\mathrm{d}t\left(0\leqslant x\leqslant \frac{\pi}{4}\right)</equation>的弧长 s = ___

**答案:**##<equation>\ln(\sqrt{2}+1).</equation>

**解析:**解 由弧长公式，得<equation>s=\int_{0}^{\frac{\pi}{4}}\sqrt{1+(y^{\prime})^{2}}\mathrm{d}x.</equation>对 y =<equation>\int_{0}^{x}\tan t\mathrm{d}t</equation>关于 x求导，得<equation>y^{\prime}(x)=\tan x.</equation>因此，<equation>s=\int_{0}^{\frac{\pi}{4}}\sqrt{1+\tan^{2}x}\mathrm{d}x=\int_{0}^{\frac{\pi}{4}}\sec x\mathrm{d}x=\ln \mid \sec x+\tan x\mid \Bigg|_{0}^{\frac{\pi}{4}}=\ln(\sqrt{2}+1).</equation>

---

**2011年第20题 | 解答题 | 11分**


某一容器的内侧是由下图中曲线绕 y轴旋转一周而形成的曲面，该曲线由<equation>x^{2}+y^{2}=2 y \left( y \geqslant \frac{1}{2} \right)</equation>与<equation>x^{2}+y^{2}= 1 \left( y \leqslant \frac{1}{2} \right)</equation>连接而成.

I. 求容器的容积;

II. 若将容器内盛满的水从容器顶部全部抽出，至少需要做多少功？（长度单位：m，重力加速度为<equation>g \mathrm{~m} / \mathrm{s}^{2}</equation>水的密度为<equation>1 0^{3} \mathrm{~k g} / \mathrm{m}^{3}</equation>）

**答案:**<equation>\frac {2 7 \times 1 0 ^ {3}}{8}</equation>

**解析:**(a)

(b)

解（I）如图（a）所示，旋转体可看作由图中阴影区域绕 y轴旋转一周所得，由两部分组成，<equation>V=V_{1}+V_{2}.</equation><equation>V_{1}</equation>是由区域<equation>D_{1}</equation>绕y轴旋转而成的旋转体的体积，<equation>V_{2}</equation>是由区域<equation>D_{2}</equation>绕y轴旋转而成的旋转体的体积.

由于曲线<equation>x^{2}+y^{2}=2 y</equation>与曲线<equation>x^{2}+y^{2}=1</equation>关于<equation>y=\frac{1}{2}</equation>对称，故<equation>V=V_{1}+V_{2}=2 V_{1}.</equation>旋转体<equation>V_{1}</equation>的母线可取为<equation>x=\sqrt{2 y-y^{2}}, y\in\left[\frac{1}{2},2\right].</equation><equation>V = 2 V _ {1} = 2 \pi \int_ {\frac {1}{2}} ^ {2} \left(2 y - y ^ {2}\right) \mathrm {d} y = 2 \pi \left(y ^ {2} - \frac {1}{3} y ^ {3}\right) \Big | _ {\frac {1}{2}} ^ {2} = \frac {9 \pi}{4}.</equation>因此，该容器的容积为<equation>\frac{9\pi}{4} \left( \mathrm{m}^{3} \right).</equation>（Ⅱ）用元素法，取图（b）中阴影部分的小薄片为做功的元素.该小薄片近似于高为<equation>\mathrm{d} y</equation>的圆柱体.当<equation>y\in\left[-1,\frac{1}{2}\right]</equation>时，小薄片的底面半径<equation>r(y)=\sqrt{1-y^{2}}</equation>；当<equation>y\in\left[\frac{1}{2},2\right]</equation>时，小薄片的底面半径为<equation>r(y)=\sqrt{2y-y^{2}}.</equation>小薄片提升的高度近似为2-y，克服该小薄片形状的水的重力所做功为<equation>\mathrm{d} W=\rho g \pi[ r(y)]^{2}(2-y)\mathrm{d} y.</equation>因此，<equation>W = \int_ {- 1} ^ {2} \rho g \pi [ r (y) ] ^ {2} (2 - y) \mathrm {d} y = \rho g \pi \left[ \int_ {- 1} ^ {\frac {1}{2}} \left(1 - y ^ {2}\right) (2 - y) \mathrm {d} y + \int_ {\frac {1}{2}} ^ {2} \left(2 y - y ^ {2}\right) (2 - y) \mathrm {d} y \right].</equation>由于<equation>\int_ {\frac {1}{2}} ^ {2} \left(2 y - y ^ {2}\right) (2 - y) \mathrm {d} y \xlongequal {u = y - \frac {3}{2}} \int_ {- 1} ^ {\frac {1}{2}} \left(u + \frac {3}{2}\right) \left(u - \frac {1}{2}\right) ^ {2} \mathrm {d} u,</equation>故<equation>\begin{aligned} W &= \rho g \pi \left[ \int_ {- 1} ^ {\frac {1}{2}} \left(1 - y ^ {2}\right) (2 - y) \mathrm {d} y + \int_ {- 1} ^ {\frac {1}{2}} \left(y + \frac {3}{2}\right) \left(y - \frac {1}{2}\right) ^ {2} \mathrm {d} y \right] = \rho g \pi \int_ {- 1} ^ {\frac {1}{2}} \left(2 y ^ {3} - \frac {3}{2} y ^ {2} - \frac {9}{4} y + \frac {1 9}{8}\right) \mathrm {d} y \\ &= \frac {\rho g \pi}{8} \left(4 y ^ {4} - 4 y ^ {3} - 9 y ^ {2} + 1 9 y\right) \Bigg | _ {- 1} ^ {\frac {1}{2}} = \frac {2 7}{8} \rho g \pi . \end{aligned}</equation>因此，所求的功为<equation>\frac{27}{8}\rho g\pi = \frac{27\times 10^{3}}{8}\pi g(\mathrm{J})</equation>

---

**2010年第12题 | 填空题 | 4分**

12. 当<equation>0 \leqslant \theta \leqslant \pi</equation>时，对数螺线<equation>r = \mathrm{e}^{\theta}</equation>的弧长为 ___

**答案:**<equation>\sqrt{2} \left( \mathrm{e}^{\pi}-1 \right).</equation>

**解析:**根据极坐标系下的曲线弧长公式，<equation>s = \int_ {0} ^ {\pi} \sqrt {\left(\mathrm {e} ^ {\theta}\right) ^ {2} + \left[ \left(\mathrm {e} ^ {\theta}\right) ^ {\prime} \right] ^ {2}} \mathrm {d} \theta = \sqrt {2} \int_ {0} ^ {\pi} \mathrm {e} ^ {\theta} \mathrm {d} \theta = \sqrt {2} \mathrm {e} ^ {\theta} \Bigg | _ {0} ^ {\pi} = \sqrt {2} \left(\mathrm {e} ^ {\pi} - 1\right).</equation>

---

**2010年第18题 | 解答题 | 10分**


一个高为 l的柱体形贮油罐，底面是长轴为 2a，短轴为 2b的椭圆.现将贮油罐平放，当油罐中油面高度为<equation>\frac{3}{2}b</equation>时（如图），计算油的质量.（长度单位为 m，质量单位为 kg，油的密度为常量<equation>\rho</equation>，单位为<equation>\mathrm{k g / m^{3}}</equation>）

**答案:**(18)<equation>a b \rho l \left(\frac{2 \pi}{3}+\frac{\sqrt{3}}{4}\right)</equation>

**解析:**解 以贮油罐的底面中心为原点，x轴方向平行于地面方向建立直角坐标系 xOy，则平放时贮油罐底面所对应的椭圆方程为<equation>\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1.</equation>由于油的密度为常量，贮油罐为柱体，故油的质量<equation>m=\rho V=\rho l S</equation>，其中 l为柱体的高，S为底面油面的面积.因此，要求油的质量，只需求出平放时油面的面积 S.

设油面所占区域为 D. 下面用两种方法来求 D的面积

（法一）利用定积分计算区域 D的面积

记<equation>D^{\prime}</equation>为D在<equation>x\geqslant 0</equation>的半平面上的部分.由于区域D关于y轴对称，故D的面积是<equation>D^{\prime}</equation>的面积的2倍.如图所示，<equation>D^{\prime} = D_{1}^{\prime}\cup D_{2}^{\prime}</equation>其中<equation>D_{1}^{\prime}</equation>为<equation>D^{\prime}</equation>位于x轴上方的部分，<equation>D_{2}^{\prime}</equation>为<equation>D^{\prime}</equation>位于x轴下方的部分.

根据椭圆面积公式，<equation>D_{2}^{\prime}</equation>的面积为<equation>S_{D_{2}} = \frac{\pi ab}{4}.</equation>将<equation>D_{1}^{\prime}</equation>看作由曲线<equation>x=a\sqrt{1-\frac{y^{2}}{b^{2}}}</equation>与直线<equation>y=\frac{b}{2},x</equation>轴，y轴所围区域.由定积分的几何意义，<equation>S _ {D _ {1} ^ {\prime}} = \int_ {0} ^ {\frac {b}{2}} a \sqrt {1 - \frac {y ^ {2}}{b ^ {2}}} \mathrm {d} y \xlongequal {y = b \sin t} a \int_ {0} ^ {\frac {\pi}{6}} b \cos^ {2} t \mathrm {d} t = \frac {a b}{2} \int_ {0} ^ {\frac {\pi}{6}} (1 + \cos 2 t) \mathrm {d} t = a b \left(\frac {\pi}{1 2} + \frac {\sqrt {3}}{8}\right).</equation>因此，<equation>S _ {D ^ {\prime}} = \frac {\pi a b}{4} + \frac {\pi a b}{1 2} + \frac {\sqrt {3} a b}{8} = a b \left(\frac {\pi}{3} + \frac {\sqrt {3}}{8}\right).</equation><equation>S = 2 S_{D^{\prime}} = ab\left(\frac{2\pi}{3} +\frac{\sqrt{3}}{4}\right)</equation>，油的质量为<equation>m = ab\rho l\left(\frac{2\pi}{3} +\frac{\sqrt{3}}{4}\right).</equation>（法二）利用二重积分来计算<equation>D_{1}^{\prime}</equation>的面积

将区域<equation>D_{1}^{\prime}</equation>看作 x≥0的半平面上的Y型区域，由椭圆方程<equation>\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1</equation>解得 x=a<equation>\sqrt{1-\frac{y^{2}}{b^{2}}}.</equation>于是，<equation>D _ {1} ^ {\prime} = \left\{(x, y) \mid 0 \leqslant x \leqslant a \sqrt {1 - \frac {y ^ {2}}{b ^ {2}}}, 0 \leqslant y \leqslant \frac {b}{2} \right\}.</equation>从而<equation>S _ {D _ {1} ^ {\prime}} = \int_ {0} ^ {\frac {b}{2}} \mathrm {d} y \int_ {0} ^ {a \sqrt {1 - \frac {y ^ {2}}{b ^ {2}}}} \mathrm {d} x = a \int_ {0} ^ {\frac {b}{2}} \sqrt {1 - \frac {y ^ {2}}{b ^ {2}}} \mathrm {d} y.</equation>其余同法一.

---

**2009年第18题 | 解答题 | 10分**

18. (本题满分10分)

设非负函数 y=y(x） （<equation>x\geqslant0</equation>）满足微分方程<equation>xy^{\prime\prime}-y^{\prime}+2=0</equation>. 当曲线 y=y(x）过原点时，其与直线 x=1及 y=0围成平面区域 D的面积为2，求 D绕 y轴旋转所得旋转体体积.

**解析:**解 当 x > 0时，<equation>x y^{\prime \prime}-y^{\prime}+2=0</equation>可写为<equation>y^{\prime \prime}=\frac{y^{\prime}-2}{x}.</equation>令 p=y'，得<equation>p^{\prime}=\frac{p-2}{x}.</equation>整理得，<equation>\frac {\mathrm {d} p}{\mathrm {d} x} - \frac {p}{x} = - \frac {2}{x}.</equation>这是一个关于<equation>p</equation>，<equation>x</equation>的一阶非齐次线性微分方程.由求解公式可得，<equation>p = C \mathrm {e} ^ {- \int p (x) \mathrm {d} x} + \mathrm {e} ^ {- \int p (x) \mathrm {d} x} \int q (x) \mathrm {e} ^ {\int p (x) \mathrm {d} x} \mathrm {d} x,</equation>其中<equation>C</equation>为待定常数. 因此，<equation>y^{\prime} = p = Cx + 2</equation>. 该等式两端同时对<equation>x</equation>积分得<equation>y = C _ {1} x ^ {2} + 2 x + C _ {2},</equation>其中<equation>C_{1}, C_{2}</equation>均为待定常数，<equation>C_{1} = \frac{C}{2}</equation>.

由于<equation>y = y(x)</equation>过原点，将<equation>x = 0, y = 0</equation>代入（1）式得<equation>C_2 = 0</equation>.

又因为曲线<equation>y=y(x)</equation>与直线<equation>x=1</equation>及<equation>y=0</equation>围成的平面区域D的面积为2，且<equation>y(x)</equation>非负，所以由定积分的几何意义可知<equation>\int_{0}^{1} y(x)\mathrm{d}x=2</equation>即<equation>\int_{0}^{1}\left(C_{1}x^{2}+2x\right)\mathrm{d}x=2.</equation>从而求得<equation>C_{1}=3.</equation>因此，<equation>y ( x ) = 3 x^{2} + 2 x ( x \geqslant 0 ).</equation>下面用两种方法求<equation>D</equation>绕<equation>y</equation>轴旋转所得旋转体的体积.

(a)

(b)

（法一）取体积元素为以底面半径为<equation>x</equation>，高为<equation>y(x)</equation>，厚度为<equation>\mathrm{d}x</equation>的圆柱壳的体积，则<equation>\mathrm {d} V = 2 \pi x y (x) \mathrm {d} x, \quad V = 2 \pi \int_ {0} ^ {1} x \left(2 x + 3 x ^ {2}\right) \mathrm {d} x = 2 \pi \left(\frac {2 x ^ {3}}{3} + \frac {3 x ^ {4}}{4}\right) \Bigg | _ {0} ^ {1} = \frac {1 7 \pi}{6}.</equation>（法二）如图（b）所示，<equation>D^{\prime}</equation>是由曲线<equation>y=y(x),y=5</equation>以及y轴围成的区域.由于<equation>y(1)=5</equation>，故所求旋转体的体积可看作由底面半径为1，高为5的圆柱体的体积<equation>V_{\mathrm{柱}}</equation>减去由区域<equation>D^{\prime}</equation>绕y轴旋转所得旋转体的体积<equation>V_{D^{\prime}}.</equation>由于<equation>y ( x ) = 2 x + 3 x^{2}</equation>，故<equation>x=\frac{-1\pm \sqrt{1+3y}}{3}</equation>.又由于<equation>x > 0</equation>，故<equation>x=\frac{-1+\sqrt{1+3y}}{3}.</equation><equation>V _ {D ^ {\prime}} = \pi \int_ {0} ^ {5} [ x (y) ] ^ {2} \mathrm {d} y = \pi \int_ {0} ^ {5} \frac {2 + 3 y - 2 \sqrt {1 + 3 y}}{9} \mathrm {d} y = \pi \left[ \frac {2 y}{9} + \frac {y ^ {2}}{6} - \frac {4}{8 1} (1 + 3 y) ^ {\frac {3}{2}} \right] \Bigg | _ {0} ^ {5} = \frac {1 3 \pi}{6}.</equation>又因为圆柱体的体积<equation>V = 5\pi</equation>，所以<equation>V = V _ {\text {柱}} - V _ {D ^ {\prime}} = 5 \pi - \frac {1 3 \pi}{6} = \frac {1 7 \pi}{6}.</equation>

---


#### 反常积分的计算与敛散性

**2025年第11题 | 填空题 | 5分**
11. 设<equation>\int_{1}^{+\infty} \frac{a}{x(2x+a)} \mathrm{d} x=\ln 2</equation>，则 a= ___
**答案: **# a=2
**解析: **解 由于<equation>\frac{a}{x(2x+a)}=\frac{1}{x}-\frac{2}{2x+a}</equation>故<equation>\begin{aligned} \int_ {1} ^ {+ \infty} \frac {a}{x (2 x + a)} \mathrm {d} x &= \int_ {1} ^ {+ \infty} \left(\frac {1}{x} - \frac {2}{2 x + a}\right) \mathrm {d} x = \left(\ln x - \ln | 2 x + a |\right) \Big | _ {1} ^ {+ \infty} = \ln \frac {x}{| 2 x + a |} \Big | _ {1} ^ {+ \infty} \\ &= \lim _ {x \rightarrow + \infty} \ln \frac {x}{| 2 x + a |} - \ln \frac {1}{| 2 + a |} = \ln \frac {| 2 + a |}{2}. \end{aligned}</equation>由<equation>\int_1^{+\infty}\frac{a}{x(2x + a)}\mathrm{d}x = \ln 2</equation>可得<equation>\ln \frac{|2 + a|}{2} = \ln 2</equation>，结合<equation>\ln x</equation>是单调函数可得<equation>\frac{|2 + a|}{2} = 2</equation>，解得<equation>a = 2</equation>或<equation>a = -6.</equation>当<equation>a = -6</equation>时，<equation>\int_{1}^{+\infty}\frac{a}{x(2x + a)}\mathrm{d}x = \int_{1}^{+\infty}\frac{-3}{x(x - 3)}\mathrm{d}x</equation>，此时<equation>x = 3</equation>为被积函数的瑕点，且<equation>\lim_{x\to 3^{-}}\frac{x - 3}{x(x - 3)} = \frac{1}{3}</equation>，由无界函数的反常积分的极限审敛法可得<equation>\int_{1}^{3}\frac{1}{x(x - 3)}\mathrm{d}x</equation>发散，从而<equation>\int_{1}^{+\infty}\frac{-3}{x(x - 3)}\mathrm{d}x</equation>发散.于是，应舍去<equation>a = -6.</equation>当<equation>a = 2</equation>时，被积函数在<equation>(1, +\infty)</equation>上没有瑕点.

因此，<equation>a=2.</equation>

---

**2024年第7题 | 选择题 | 5分 | 答案: B**
7. 设非负函数 f(x)在<equation>[0,+\infty)</equation>上连续，给出以下三个命题：<equation>\textcircled{1}</equation>若<equation>\int_{0}^{+\infty} f^{2}(x)\mathrm{d}x</equation>收敛、则<equation>\int_{0}^{+\infty} f(x)\mathrm{d}x</equation>收敛.<equation>\textcircled{2}</equation>若存在 p>1，使得<equation>\lim_{x\rightarrow+\infty} x^{p} f(x)</equation>存在，则<equation>\int_{0}^{+\infty} f(x)\mathrm{d}x</equation>收敛.<equation>\textcircled{3}</equation>若<equation>\int_{0}^{+\infty} f(x)\mathrm{d}x</equation>收敛、则存在 p>1，使得<equation>\lim_{x\rightarrow+\infty} x^{p} f(x)</equation>存在.

其中真命题的个数为（    ）

A. 0 B. 1 C. 2
答案: B
**解析: **解 依次分析各命题.

对命题<equation>\textcircled{1}</equation>，考虑<equation>f(x) = \frac{1}{x + 1}</equation>，则该函数在<equation>[0, +\infty)</equation>上连续非负，<equation>f^{2}(x) = \frac{1}{(x + 1)^{2}}</equation><equation>\int_ {0} ^ {+ \infty} f ^ {2} (x) \mathrm {d} x = \int_ {0} ^ {+ \infty} \frac {1}{(1 + x) ^ {2}} \mathrm {d} x = - \frac {1}{1 + x} \Big | _ {0} ^ {+ \infty} = 1.</equation>但是，<equation>\int_ {0} ^ {+ \infty} f (x) \mathrm {d} x = \int_ {0} ^ {+ \infty} \frac {1}{1 + x} \mathrm {d} x = \ln (1 + x) \Big | _ {0} ^ {+ \infty} = + \infty .</equation>因此，命题<equation>\textcircled{1}</equation>不正确.

对命题<equation>\textcircled{2}</equation>，若存在 p > 1，使得<equation>\lim_{x\to +\infty}x^{p}f(x)</equation>存在，则由无穷限反常积分的极限审敛法可得<equation>\int_{0}^{+\infty}f(x)\mathrm{d}x</equation>收敛.因此，命题<equation>\textcircled{2}</equation>正确.

对命题<equation>\textcircled{3}</equation>，考虑<equation>f(x) = \frac{1}{(x + 2)\ln^2(x + 2)}</equation>，则该函数在<equation>[0, + \infty)</equation>上连续非负，<equation>\begin{aligned} \int_ {0} ^ {+ \infty} f (x) \mathrm {d} x &= \int_ {0} ^ {+ \infty} \frac {1}{(x + 2) \ln^ {2} (x + 2)} \mathrm {d} x = \int_ {0} ^ {+ \infty} \frac {1}{\ln^ {2} (x + 2)} \mathrm {d} [ \ln (x + 2) ] \\ &= - \frac {1}{\ln (x + 2)} \Big | _ {0} ^ {+ \infty} = \frac {1}{\ln 2}. \end{aligned}</equation>但对任意 p > 1，都有<equation>\begin{aligned} \lim _ {x \rightarrow + \infty} x ^ {p} f (x) &= \lim _ {x \rightarrow + \infty} \frac {x ^ {p}}{(x + 2) \ln^ {2} (x + 2)} = \lim _ {x \rightarrow + \infty} \frac {(x + 2) ^ {p}}{(x + 2) \ln^ {2} (x + 2)} \cdot \frac {x ^ {p}}{(x + 2) ^ {p}} \\ &= \lim _ {x \rightarrow + \infty} \frac {(x + 2) ^ {p - 1}}{\ln^ {2} (x + 2)} \stackrel {*} {=} + \infty . \end{aligned}</equation>因此，命题<equation>\textcircled{3}</equation>不正确.

综上所述，正确命题的个数为1，应选B.

---

**2023年第6题 | 选择题 | 5分 | 答案: A**
6. 若函数<equation>f(\alpha)=\int_{2}^{+\infty}\frac{1}{x(\ln x)^{\alpha+1}}\mathrm{d}x</equation>在<equation>\alpha=\alpha_{0}</equation>处取得最小值，则<equation>\alpha_{0}=</equation>（    )

A.<equation>-\frac{1}{\ln(\ln 2)}</equation>B.<equation>-\ln(\ln 2)</equation>C.<equation>\frac{1}{\ln 2}</equation>D.<equation>\ln 2</equation>
答案: A
**解析: **解 当<equation>\alpha=0</equation>时，<equation>f (\alpha) = \int_ {2} ^ {+ \infty} \frac {1}{x \ln x} \mathrm {d} x = \int_ {2} ^ {+ \infty} \frac {1}{\ln x} \mathrm {d} (\ln x) = \ln (\ln x) \Big | _ {2} ^ {+ \infty} = + \infty .</equation>当<equation>\alpha=0</equation>时，<equation>f(\alpha)</equation>无定义.

当<equation>\alpha\neq0</equation>时，<equation>f (\alpha) = \int_ {2} ^ {+ \infty} \frac {1}{x (\ln x) ^ {\alpha + 1}} \mathrm {d} x = \int_ {2} ^ {+ \infty} (\ln x) ^ {- \alpha - 1} \mathrm {d} (\ln x) = - \frac {1}{\alpha} (\ln x) ^ {- \alpha} \Big | _ {2} ^ {+ \infty}.</equation>当<equation>\alpha < 0</equation>时，<equation>\lim_{x\to +\infty} (\ln x)^{-\alpha}=+\infty</equation><equation>f(\alpha)</equation>无定义；当<equation>\alpha >0</equation>时，<equation>f (\alpha) = - \frac {1}{\alpha} \left(\ln x\right) ^ {- \alpha} \Bigg | _ {2} ^ {+ \infty} = - \frac {1}{\alpha} \left[ 0 - \left(\ln 2\right) ^ {- \alpha} \right] = \frac {\left(\ln 2\right) ^ {- \alpha}}{\alpha}.</equation>因此，<equation>f(\alpha)</equation>的定义域为（0，<equation>+\infty</equation>），<equation>f(\alpha) = \frac{(\ln 2)^{-\alpha}}{\alpha}.</equation>计算<equation>f^{\prime}(\alpha).</equation><equation>f ^ {\prime} (\alpha) = \frac {- \alpha (\ln 2) ^ {- \alpha} \ln (\ln 2) - (\ln 2) ^ {- \alpha}}{\alpha^ {2}} = \frac {- (\ln 2) ^ {- \alpha} [ \alpha \ln (\ln 2) + 1 ]}{\alpha^ {2}}.</equation><equation>f^{\prime}(\alpha)=0</equation>当且仅当<equation>\alpha=-\frac{1}{\ln(\ln 2)}。</equation>当<equation>0 < \alpha < - \frac{1}{\ln(\ln 2)}</equation>时，<equation>f^{\prime}(\alpha)<0,f(\alpha)</equation>单调减少；当<equation>\alpha > - \frac{1}{\ln(\ln 2)}</equation>时，<equation>f^{\prime}(\alpha)>0,f(\alpha)</equation>单调增加.因此，<equation>\alpha_{0}=- \frac{1}{\ln(\ln 2)}</equation>为 f（<equation>\alpha</equation>）的最小值点，应选A.

---

**2022年第5题 | 选择题 | 5分 | 答案: A**
5. 设 p为常数，若反常积分<equation>\int_{0}^{1}\frac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x</equation>收敛，则 p的取值范围是（    )

A. (-1,1) B. (-1,2) C.<equation>(-\infty,1)</equation>D.<equation>(-\infty,2)</equation>
答案: A
**解析: **由于 x=0和 x=1均为可能的瑕点，故将积分拆成两部分.<equation>\int_ {0} ^ {1} \frac {\ln x}{x ^ {p} (1 - x) ^ {1 - p}} \mathrm {d} x = \int_ {0} ^ {\frac {1}{2}} \frac {\ln x}{x ^ {p} (1 - x) ^ {1 - p}} \mathrm {d} x + \int_ {\frac {1}{2}} ^ {1} \frac {\ln x}{x ^ {p} (1 - x) ^ {1 - p}} \mathrm {d} x.</equation>先考虑<equation>\int_{0}^{\frac{1}{2}}\frac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x.</equation>当 p < 0时，<equation>\lim_{x\rightarrow 0^{+}}\frac{\ln x}{x^{p}(1-x)^{1-p}}=0,x=0</equation>不是瑕点，<equation>\int_{0}^{\frac{1}{2}}\frac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x</equation>为常义积分当 0≤p < 1时，取<equation>\delta >0</equation>使得0 < p+<equation>\delta < 1</equation>从而<equation>\lim _ {x \rightarrow 0 ^ {+}} x ^ {p + \delta} \cdot \frac {\ln x}{x ^ {p} (1 - x) ^ {1 - p}} = \lim _ {x \rightarrow 0 ^ {+}} x ^ {\delta} \ln x = \lim _ {x \rightarrow 0 ^ {+}} \frac {\ln x}{x ^ {- \delta}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {1}{- \delta x ^ {- \delta}} = 0.</equation>由无界函数的极限审敛法可知，<equation>\int_{0}^{\frac{1}{2}}\frac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x</equation>收敛.

当 p=1时，<equation>\int_ {0} ^ {\frac {1}{2}} \frac {\ln x}{x} \mathrm {d} x = \int_ {0} ^ {\frac {1}{2}} \ln x \mathrm {d} (\ln x) = \frac {\left(\ln x\right) ^ {2}}{2} \Bigg | _ {0} ^ {\frac {1}{2}} = - \infty .</equation>于是，当<equation>p \geqslant 1</equation>时，<equation>\int_{0}^{\frac{1}{2}}\frac{\ln x}{x^{p}\left(1-x\right)^{1-p}}\mathrm{d}x</equation>发散.

因此，当<equation>p < 1</equation>时，<equation>\int_{0}^{\frac{1}{2}}\frac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x</equation>收敛，当<equation>p\geqslant 1</equation>时，<equation>\int_{0}^{\frac{1}{2}}\frac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x</equation>发散.

再考虑<equation>\int_{\frac{1}{2}}^{1} \frac{\ln x}{x^{p}(1-x)^{1-p}} \mathrm{d} x.</equation><equation>\lim _ {x \rightarrow 1 ^ {-}} \frac {\ln x}{x ^ {p} (1 - x) ^ {1 - p}} = \lim _ {x \rightarrow 1 ^ {-}} \frac {\ln (1 + x - 1)}{x ^ {p} (1 - x) ^ {1 - p}} = \lim _ {x \rightarrow 1 ^ {-}} \frac {- (1 - x)}{(1 - x) ^ {1 - p}} = - \lim _ {x \rightarrow 1 ^ {-}} (1 - x) ^ {p}.</equation>于是，当 p≥0时，x=1不是瑕点，<equation>\int_{\frac{1}{2}}^{1} \frac{\ln x}{x^{p}(1-x)^{1-p}} \mathrm{d} x</equation>为常义积分.

当 0 < - p < 1，即<equation>- 1 < p < 0</equation>时，<equation>\lim _ {x \rightarrow 1 ^ {-}} (1 - x) ^ {- p} \cdot \frac {- \ln x}{x ^ {p} (1 - x) ^ {1 - p}} = \lim _ {x \rightarrow 1 ^ {-}} (1 - x) ^ {- p} \cdot (1 - x) ^ {p} = 1.</equation>由无界函数的极限审敛法可知，<equation>\int_{\frac{1}{2}}^{1} \frac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x</equation>收敛.

当<equation>- p \geqslant 1</equation>，即<equation>p \leqslant - 1</equation>时，同理可得<equation>\lim_{x\to 1^{-}}(1-x)^{-p}\cdot \frac{-\ln x}{x^{p}(1-x)^{1-p}}=1</equation>从而由无界函数的极限审敛法可知，<equation>\int_{\frac{1}{2}}^{1}\frac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x</equation>发散.

因此，当 p > -1时，<equation>\int_{\frac{1}{2}}^{1} \frac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x</equation>收敛，当 p≤-1时，<equation>\int_{\frac{1}{2}}^{1} \frac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x</equation>发散.

综上所述，<equation>\int_{0}^{1}\frac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x</equation>收敛当且仅当 p<equation>\in(-\infty,1)\cap(-1,+\infty)=(-1,1).</equation>应选A.

---

**2021年第11题 | 填空题 | 5分**
<equation>1 1. \int_ {- \infty} ^ {+ \infty} | x | 3 ^ {- x ^ {2}} \mathrm {d} x = \underline {{}}</equation>
**解析: **由于<equation>| x | = \left\{ \begin{array}{ll} x, & x\geqslant 0, \\ - x, & x < 0, \end{array} \right.</equation>故<equation>\begin{aligned} \int_ {- \infty} ^ {+ \infty} | x | 3 ^ {- x ^ {2}} \mathrm {d} x &= \int_ {- \infty} ^ {0} (- x) \cdot 3 ^ {- x ^ {2}} \mathrm {d} x + \int_ {0} ^ {+ \infty} x \cdot 3 ^ {- x ^ {2}} \mathrm {d} x \xlongequal {t = - x} \int_ {+ \infty} ^ {0} t \cdot 3 ^ {- t ^ {2}} \mathrm {d} (- t) + \int_ {0} ^ {+ \infty} x \cdot 3 ^ {- x ^ {2}} \mathrm {d} x \\ &= 2 \int_ {0} ^ {+ \infty} x \cdot 3 ^ {- x ^ {2}} \mathrm {d} x = \int_ {0} ^ {+ \infty} 3 ^ {- x ^ {2}} \mathrm {d} \left(x ^ {2}\right) = \frac {- 3 ^ {- x ^ {2}}}{\ln 3} \Big | _ {0} ^ {+ \infty} = 0 - \left(- \frac {1}{\ln 3}\right) = \frac {1}{\ln 3}. \end{aligned}</equation>

---

**2019年第3题 | 选择题 | 4分 | 答案: D**
3. 下列反常积分发散的是（    ）

A.<equation>\int_{0}^{+\infty} x \mathrm{e}^{-x} \mathrm{d} x</equation>B.<equation>\int_{0}^{+\infty} x \mathrm{e}^{-x^{2}} \mathrm{d} x</equation>C.<equation>\int_{0}^{+\infty} \frac{\arctan x}{1+x^{2}} \mathrm{d} x</equation>D.<equation>\int_{0}^{+\infty} \frac{x}{1+x^{2}} \mathrm{d} x</equation>
答案: D
**解析: **由于各选项中的积分都不太复杂，故可先积分，再讨论极限.<equation>\begin{aligned} \int_ {0} ^ {+ \infty} x \mathrm {e} ^ {- x} \mathrm {d} x &= - \int_ {0} ^ {+ \infty} x \mathrm {d} \left(\mathrm {e} ^ {- x}\right) = - \left(x \mathrm {e} ^ {- x} \Big | _ {0} ^ {+ \infty} - \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- x} \mathrm {d} x\right) \\ &= \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- x} \mathrm {d} x = - \mathrm {e} ^ {- x} \Big | _ {0} ^ {+ \infty} = - (0 - 1) = 1. \end{aligned}</equation><equation>\begin{aligned} \int_ {0} ^ {+ \infty} x \mathrm {e} ^ {- x ^ {2}} \mathrm {d} x &= \frac {1}{2} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- x ^ {2}} \mathrm {d} \left(x ^ {2}\right) = - \frac {1}{2} \mathrm {e} ^ {- x ^ {2}} \Bigg | _ {0} ^ {+ \infty} = - \frac {1}{2} \times (0 - 1) = \frac {1}{2}. \\ \int_ {0} ^ {+ \infty} \frac {\arctan x}{1 + x ^ {2}} \mathrm {d} x &= \int_ {0} ^ {+ \infty} \arctan x \mathrm {d} (\arctan x) = \frac {\left(\arctan x\right) ^ {2}}{2} \Bigg | _ {0} ^ {+ \infty} \\ \frac {\lim _ {x \rightarrow + \infty} \arctan x = \frac {\pi}{2}}{\frac {1}{2}} \frac {1}{2} \left[\left(\frac {\pi}{2}\right) ^ {2} - 0 \right] &= \frac {\pi^ {2}}{8}. \end{aligned}</equation><equation>\int_ {0} ^ {+ \infty} \frac {x}{1 + x ^ {2}} \mathrm {d} x = \frac {1}{2} \int_ {0} ^ {+ \infty} \frac {\mathrm {d} \left(1 + x ^ {2}\right)}{1 + x ^ {2}} = \frac {1}{2} \ln \left(1 + x ^ {2}\right) \Big | _ {0} ^ {+ \infty} = + \infty .</equation>综上所述，应选D.

---

**2018年第11题 | 填空题 | 4分**
11.
**答案: **##<equation>\frac{1}{2} \ln 2.</equation>
**解析: **<equation>\begin{array}{l} = \frac {1}{2} \ln \left| \frac {x - 3}{x - 1} \right| \Big | _ {5} ^ {+ \infty} \stackrel {*} {=} \frac {1}{2} \left(0 - \ln \frac {5 - 3}{5 - 1}\right) = \frac {1}{2} \ln 2. \\ \end{array}</equation>

---

**2017年第11题 | 填空题 | 4分**
11.<equation>\int_ {0} ^ {+ \infty} \frac {\ln (1 + x)}{(1 + x) ^ {2}} \mathrm {d} x = \underline {{}}</equation>
**解析: **采用分部积分法.<equation>\begin{aligned} \int_ {0} ^ {+ \infty} \frac {\ln (1 + x)}{(1 + x) ^ {2}} \mathrm {d} x &= - \int_ {0} ^ {+ \infty} \ln (1 + x) \mathrm {d} \left(\frac {1}{1 + x}\right) = - \left[ \frac {\ln (1 + x)}{1 + x} \Big | _ {0} ^ {+ \infty} - \int_ {0} ^ {+ \infty} \frac {1}{(1 + x) ^ {2}} \mathrm {d} x \right] \\ &= \int_ {0} ^ {+ \infty} \frac {1}{(1 + x) ^ {2}} \mathrm {d} x = - \frac {1}{1 + x} \Big | _ {0} ^ {+ \infty} = 0 - (- 1) = 1. \end{aligned}</equation>

---

**2016年第3题 | 选择题 | 4分 | 答案: B**
3. 反常积分<equation>\int_{-\infty}^{0}\frac{1}{x^{2}}\mathrm{e}^{\frac{1}{x}}\mathrm{d}x</equation>和<equation>\int_{0}^{+\infty}\frac{1}{x^{2}}\mathrm{e}^{\frac{1}{x}}\mathrm{d}x</equation>的敛散性分别为（    )

A. 收敛，收敛 B. 收敛，发散 C. 发散，收敛 D. 发散，发散
答案: B
**解析: **解分别计算<equation>\int_{- \infty}^{0} \frac{1}{x^{2}} \mathrm{e}^{\frac{1}{x}} \mathrm{d} x</equation>和<equation>\int_{0}^{+\infty} \frac{1}{x^{2}} \mathrm{e}^{\frac{1}{x}} \mathrm{d} x.</equation>设 R < c < 0.<equation>\begin{aligned} \int_ {- \infty} ^ {0} \frac {1}{x ^ {2}} \mathrm {e} ^ {\frac {1}{x}} \mathrm {d} x &= \lim _ {\substack {c \rightarrow 0 ^ {-} \\ R \rightarrow - \infty}} \int_ {R} ^ {c} \frac {1}{x ^ {2}} \mathrm {e} ^ {\frac {1}{x}} \mathrm {d} x = \lim _ {\substack {c \rightarrow 0 ^ {-} \\ R \rightarrow - \infty}} \int_ {R} ^ {c} - \mathrm {e} ^ {\frac {1}{x}} \mathrm {d} \left(\frac {1}{x}\right) = \lim _ {\substack {c \rightarrow 0 ^ {-} \\ R \rightarrow - \infty}} \left(- \mathrm {e} ^ {\frac {1}{x}} \Bigg | _ {R} ^ {c}\right) \\ &= \lim _ {x \rightarrow 0 ^ {-}} \left(- \mathrm {e} ^ {\frac {1}{x}}\right) - \lim _ {x \rightarrow - \infty} \left(- \mathrm {e} ^ {\frac {1}{x}}\right) = 0 - (- 1) = 1. \end{aligned}</equation>设 0 < c < R.<equation>\begin{aligned} \int_ {0} ^ {+ \infty} \frac {1}{x ^ {2}} \mathrm {e} ^ {\frac {1}{x}} \mathrm {d} x &= \lim _ {\substack {c \rightarrow 0 ^ {+} \\ R \rightarrow + \infty}} \int_ {c} ^ {R} \frac {1}{x ^ {2}} \mathrm {e} ^ {\frac {1}{x}} \mathrm {d} x = \lim _ {\substack {c \rightarrow 0 ^ {+} \\ R \rightarrow + \infty}} \int_ {c} ^ {R} - \mathrm {e} ^ {\frac {1}{x}} \mathrm {d} \left(\frac {1}{x}\right) = \lim _ {\substack {c \rightarrow 0 ^ {+} \\ R \rightarrow + \infty}} \left(- \mathrm {e} ^ {\frac {1}{x}} \Bigg | _ {c} ^ {R}\right) \\ &= \lim _ {x \rightarrow + \infty} \left(- \mathrm {e} ^ {\frac {1}{x}}\right) - \lim _ {x \rightarrow 0 ^ {+}} \left(- \mathrm {e} ^ {\frac {1}{x}}\right). \end{aligned}</equation>由于<equation>\lim_{x\rightarrow +\infty}(-\mathrm{e}^{\frac{1}{x}})=-1</equation>，而<equation>\lim_{x\rightarrow 0^{+}}(-\mathrm{e}^{\frac{1}{x}})=-\infty</equation>，故<equation>\int_{0}^{+\infty}\frac{1}{x^{2}}\mathrm{e}^{\frac{1}{x}}\mathrm{d}x</equation>发散.

因此，应选B.

---

**2015年第1题 | 选择题 | 4分 | 答案: D**
1. 下列反常积分中收敛的是（    ）

A.<equation>\int_{2}^{+\infty}\frac{1}{\sqrt{x}} \mathrm{d} x</equation>B.<equation>\int_{2}^{+\infty}\frac{\ln x}{x} \mathrm{d} x</equation>C.<equation>\int_{2}^{+\infty}\frac{1}{x \ln x} \mathrm{d} x</equation>D.<equation>\int_{2}^{+\infty}\frac{x}{\mathrm{e}^{x}} \mathrm{d} x</equation>
答案: D
**解析: **由于各选项中的积分都不太复杂，故可先积分，再讨论极限.<equation>\int_ {2} ^ {+ \infty} \frac {1}{\sqrt {x}} \mathrm {d} x = 2 \sqrt {x} \Big | _ {2} ^ {+ \infty} = + \infty ,</equation><equation>\left. \int_ {2} ^ {+ \infty} \frac {\ln x}{x} \mathrm {d} x = \frac {\left(\ln x\right) ^ {2}}{2} \right| _ {2} ^ {+ \infty} = + \infty ,</equation><equation>\left. \int_ {2} ^ {+ \infty} \frac {1}{x \ln x} \mathrm {d} x = \ln (\ln x) \right| _ {2} ^ {+ \infty} = + \infty ,</equation><equation>\left. \int_ {2} ^ {+ \infty} \frac {x}{\mathrm {e} ^ {x}} \mathrm {d} x = - \int_ {2} ^ {+ \infty} x \mathrm {d} \left(\mathrm {e} ^ {- x}\right) = - (x + 1) \mathrm {e} ^ {- x} \right| _ {2} ^ {+ \infty} = \frac {3}{\mathrm {e} ^ {2}}.</equation>综上可知，应选D.

---

**2014年第9题 | 填空题 | 4分**
（无内容）
**解析: **对被积函数的分母配方.<equation>\begin{aligned} \int_ {- \infty} ^ {1} \frac {1}{x ^ {2} + 2 x + 5} \mathrm {d} x &= \int_ {- \infty} ^ {1} \frac {1}{(x + 1) ^ {2} + 4} \mathrm {d} x = \frac {1}{2} \int_ {- \infty} ^ {1} \frac {1}{\left(\frac {x + 1}{2}\right) ^ {2} + 1} \mathrm {d} \left(\frac {x + 1}{2}\right) \\ &= \frac {1}{2} \arctan \frac {x + 1}{2} \Big | _ {- \infty} ^ {1} = \frac {1}{2} \left[ \frac {\pi}{4} - \left(- \frac {\pi}{2}\right) \right] = \frac {3 \pi}{8}. \end{aligned}</equation>

---

**2013年第4题 | 选择题 | 4分 | 答案: D**
4. 设函数 f(x) =<equation>\left\{\begin{array}{l l} \frac{1}{(x-1)^{\alpha-1}},&1<x<\mathrm{e},\\ \frac{1}{x\ln^{\alpha+1}x},&x\geqslant\mathrm{e}. \end{array} \right.</equation>若反常积分<equation>\int_{1}^{+\infty} f(x)\mathrm{d}x</equation>收敛，则（    )

A.<equation>\alpha<-2</equation>B.<equation>\alpha>2</equation>C.<equation>-2<\alpha<0</equation>D.<equation>0<\alpha<2</equation>
答案: D
**解析: **解 由 f(x) 的定义，知<equation>\int_ {1} ^ {+ \infty} f (x) \mathrm {d} x = \int_ {1} ^ {\mathrm {e}} \frac {1}{(x - 1) ^ {\alpha - 1}} \mathrm {d} x + \int_ {\mathrm {e}} ^ {+ \infty} \frac {1}{x \ln^ {\alpha + 1} x} \mathrm {d} x.</equation>由于<equation>\int_{1}^{+\infty} f(x)\mathrm{d}x</equation>收敛，故上式中的两个积分值均应存在且有限.

考虑积分<equation>\int_{1}^{e}\frac{1}{(x-1)^{\alpha-1}}\mathrm{d}x.</equation>当<equation>\alpha-1\leqslant0</equation>即<equation>\alpha\leqslant1</equation>时，该积分为普通定积分.当<equation>\alpha-1>0</equation>时，该积分为无界函数的反常积分（瑕积分），瑕点为<equation>x=1.</equation><equation>\int_ {1} ^ {\mathrm {e}} \frac {1}{(x - 1) ^ {\alpha - 1}} \mathrm {d} x = \frac {(x - 1) ^ {2 - \alpha}}{2 - \alpha} \Bigg | _ {1} ^ {\mathrm {e}}.</equation>若该积分收敛，则<equation>\lim_{x\to 1}\frac{(x - 1)^{2 - \alpha}}{2 - \alpha}</equation>存在，从而<equation>2 - \alpha > 0</equation>，即<equation>\alpha < 2</equation>考虑无穷区间上的反常积分<equation>\int_{\mathrm{e}}^{+\infty}\frac{1}{x\ln^{\alpha+1}x}\mathrm{d}x.</equation><equation>\int_ {\mathrm {e}} ^ {+ \infty} \frac {1}{x \ln^ {\alpha + 1} x} \mathrm {d} x \xlongequal {u = \ln x} \int_ {1} ^ {+ \infty} \frac {1}{u ^ {\alpha + 1}} \mathrm {d} u = - \left. \frac {u ^ {- \alpha}}{\alpha} \right| _ {1} ^ {+ \infty}.</equation>若<equation>\int_{\mathrm{e}}^{+\infty}\frac{1}{x\ln^{\alpha +1}x}\mathrm{d}x</equation>收敛，则<equation>\lim_{u\to +\infty}u^{-\alpha}</equation>存在，从而<equation>-\alpha < 0</equation>，即<equation>\alpha > 0</equation>综上所述，若<equation>\int_{1}^{+\infty} f ( x ) \mathrm{d} x</equation>收敛，则<equation>0 < \alpha < 2</equation>应选D.

---

**2011年第12题 | 填空题 | 4分**
12. 设函数<equation>f ( x )=\left\{\begin{array}{ll}\lambda \mathrm{e}^{-\lambda x}&x>0,\\ 0,&x\leqslant 0,\end{array} \right. \lambda>0</equation>，则<equation>\int_{-\infty}^{+\infty} x f ( x ) \mathrm{d} x=</equation>___
**解析: **解 由于 f(x) 具有分段表达式，故<equation>\int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \int_ {- \infty} ^ {0} x f (x) \mathrm {d} x + \int_ {0} ^ {+ \infty} x f (x) \mathrm {d} x = 0 + \int_ {0} ^ {+ \infty} x f (x) \mathrm {d} x.</equation>下面求<equation>\int_0^{+\infty} xf(x)\mathrm{d}x.</equation><equation>\begin{aligned} \int_ {0} ^ {+ \infty} x f (x) \mathrm {d} x &= \int_ {0} ^ {+ \infty} \lambda x \mathrm {e} ^ {- \lambda x} \mathrm {d} x = - \int_ {0} ^ {+ \infty} x \mathrm {d} \left(\mathrm {e} ^ {- \lambda x}\right) = - \left(x \mathrm {e} ^ {- \lambda x} \Big | _ {0} ^ {+ \infty} - \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda x} \mathrm {d} x\right) \\ &= - \left(\lim _ {x \rightarrow + \infty} x \mathrm {e} ^ {- \lambda x} - 0\right) + \left[ \lim _ {x \rightarrow + \infty} \frac {\mathrm {e} ^ {- \lambda x}}{- \lambda} - \left(\frac {1}{- \lambda}\right)\right]. \end{aligned}</equation>由于<equation>\lambda >0</equation>，故<equation>\lim _ {x \rightarrow + \infty} \frac {x}{\mathrm {e} ^ {\lambda x}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow + \infty} \frac {1}{\lambda \mathrm {e} ^ {\lambda x}} = 0, \quad \lim _ {x \rightarrow + \infty} \frac {\mathrm {e} ^ {- \lambda x}}{- \lambda} = 0.</equation>因此，<equation>\int_ {0} ^ {+ \infty} x f (x) \mathrm {d} x = \frac {1}{\lambda}, \quad \int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \frac {1}{\lambda}.</equation>

---

**2010年第4题 | 选择题 | 4分 | 答案: D**
4. 设 m,n均是正整数，则反常积分<equation>\int_{0}^{1}\frac{\sqrt[m]{\ln^{2}(1-x)}}{\sqrt[n]{x}} \mathrm{d}x</equation>的收敛性（    ）

A. 仅与 m的取值有关 B. 仅与 n的取值有关

C. 与 m,n的取值都有关 D. 与 m,n的取值都无关
答案: D
**解析: **由于被积函数有两个可能的瑕点，<equation>x=0</equation>和<equation>x=1</equation>，故将原积分拆成两部分进行考虑.<equation>\int_ {0} ^ {1} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} \mathrm {d} x = \int_ {0} ^ {\frac {1}{2}} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} \mathrm {d} x + \int_ {\frac {1}{2}} ^ {1} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} \mathrm {d} x.</equation>先讨论<equation>\int_0^{\frac{1}{2}}\frac{\left[\ln(1 - x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>的收敛性.考虑<equation>\lim_{x\to 0^{+}}\frac{\left[\ln(1 - x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}</equation>.<equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} \xlongequal {\ln (1 - x) \sim (- x)} \lim _ {x \rightarrow 0 ^ {+}} x ^ {\frac {2}{m} - \frac {1}{n}} = \left\{\begin{array}{l l}0,&\frac {2}{m} - \frac {1}{n} > 0,\\1,&\frac {2}{m} - \frac {1}{n} = 0,\\\infty ,&\frac {2}{m} - \frac {1}{n} < 0.\end{array}\right.</equation>当 m，n为正整数时，<equation>\frac{2}{m} -\frac{1}{n}\geqslant \frac{2}{m} -1 > -1.</equation>- 当<equation>\frac{2}{m}-\frac{1}{n}\geqslant0</equation>时，<equation>x=0</equation>是被积函数的可去间断点，<equation>\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}</equation>在<equation>\left[0,\frac{1}{2}\right]</equation>上可积，<equation>\int_{0}^{\frac{1}{2}}\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>存在且有限.

- 当<equation>- 1 < \frac{2}{m} - \frac{1}{n} < 0</equation>时，<equation>x=0</equation>是被积函数的瑕点.取<equation>p=\frac{1}{n}-\frac{2}{m}</equation>则<equation>0 < p < 1</equation><equation>\lim_{x\to 0^{+}}\frac{x^{p}\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}=1.</equation>由极限审敛法可知反常积分<equation>\int_{0}^{\frac{1}{2}}\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>收敛.

因此，不论 m，n 取何正整数，积分<equation>\int_{0}^{\frac{1}{2}}\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>均收敛.

下面讨论<equation>\int_{\frac{1}{2}}^{1}\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>的收敛性. x=1为被积函数的瑕点.

考虑极限<equation>\lim _ {x \rightarrow 1 ^ {-}} \sqrt {1 - x} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} = \lim _ {x \rightarrow 1 ^ {-}} \sqrt {1 - x} \left[ \ln (1 - x) \right] ^ {\frac {2}{m}}.</equation>记<equation>I _ {0} = \lim _ {x \rightarrow 1 ^ {-}} \sqrt {1 - x} \left[ \ln (1 - x) \right] ^ {\frac {2}{m}} \xlongequal {u = 1 - x} \lim _ {u \rightarrow 0 ^ {+}} u ^ {\frac {1}{2}} (\ln u) ^ {\frac {2}{m}}.</equation>若 m=1，则<equation>I _ {0} = \lim _ {u \rightarrow 0 ^ {+}} \frac {\left(\ln u\right) ^ {2}}{u ^ {- \frac {1}{2}}} \xlongequal {\text {洛必达}} \lim _ {u \rightarrow 0 ^ {+}} \frac {- 4 \ln u}{u ^ {- \frac {1}{2}}} \xlongequal {\text {洛必达}} \lim _ {u \rightarrow 0 ^ {+}} 8 u ^ {\frac {1}{2}} = 0.</equation>若 m=2，则<equation>I _ {0} = \lim _ {u \rightarrow 0 ^ {+}} \frac {\ln u}{u ^ {- \frac {1}{2}}} \xlongequal {\text {洛 必达}} \lim _ {u \rightarrow 0 ^ {+}} (- 2) u ^ {\frac {1}{2}} = 0.</equation>若<equation>m > 2</equation>，则<equation>0 < \frac{2}{m} < 1</equation>，同理使用洛必达法则可计算得<equation>I_0 = 0.</equation>因此，由极限审敛法知，不论 m，n 取何正整数，积分<equation>\int_{\frac{1}{2}}^{1} \frac{\left[ \ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>均收敛.综上所述，不论 m，n 取何正整数，积分<equation>\int_{0}^{1} \frac{\left[ \ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>均收敛.应选D.

---

**2009年第10题 | 填空题 | 4分**
10. 已知
**答案: **-2.
**解析: **解 由已知等式知，<equation>k\neq 0</equation>，否则<equation>\int_{-\infty}^{+\infty}\mathrm{e}^{k|x|}\mathrm{d}x</equation>不收敛.

去掉被积函数中的绝对值符号.<equation>1 = \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {k | x |} \mathrm {d} x = \int_ {- \infty} ^ {0} \mathrm {e} ^ {- k x} \mathrm {d} x + \int_ {0} ^ {+ \infty} \mathrm {e} ^ {k x} \mathrm {d} x = 2 \int_ {0} ^ {+ \infty} \mathrm {e} ^ {k x} \mathrm {d} x.</equation>由（1）式知，<equation>\int_{0}^{+\infty}\mathrm{e}^{kx}\mathrm{d}x=\frac{1}{2}</equation>从而，<equation>\frac {1}{2} = \int_ {0} ^ {+ \infty} \mathrm {e} ^ {k x} \mathrm {d} x = \lim _ {t \rightarrow + \infty} \left(\int_ {0} ^ {t} \mathrm {e} ^ {k x} \mathrm {d} x\right) = \lim _ {t \rightarrow + \infty} \left. \frac {\mathrm {e} ^ {k x}}{k} \right| _ {0} ^ {t} = \lim _ {t \rightarrow + \infty} \left(\frac {\mathrm {e} ^ {k t}}{k} - \frac {1}{k}\right).</equation>由函数<equation>y=\mathrm{e}^{k x}</equation>的性质知，当<equation>t\to +\infty</equation>时，若<equation>\lim_{t\to +\infty}\mathrm{e}^{k t}</equation>存在，则<equation>k<0.</equation>此时<equation>\lim_{t\to +\infty}\mathrm{e}^{k t}=0.</equation>因此由（2）式可得<equation>-\frac{1}{k}=\frac{1}{2}</equation>即<equation>k=-2.</equation>

---


#### 定积分的概念与性质

**2025年第13题 | 填空题 | 5分**
<equation>\lim _ {n \rightarrow \infty} \frac {1}{n ^ {2}} \left[ \ln \frac {1}{n} + 2 \ln \frac {2}{n} + \dots + (n - 1) \ln \frac {n - 1}{n} \right] = \underline {{}}</equation>
**答案: **# -<equation>\frac{1}{4}</equation>
**解析: **解 从定积分的定义出发，对原极限进行恒等变形，注意到<equation>\ln 1 = 0</equation>，故<equation>\ln \frac {1}{n} + 2 \ln \frac {2}{n} + \dots + (n - 1) \ln \frac {n - 1}{n} = \ln \frac {1}{n} + 2 \ln \frac {2}{n} + \dots + (n - 1) \ln \frac {n - 1}{n} + n \ln \frac {n}{n}.</equation>进一步可得<equation>\begin{aligned} \lim _ {n \rightarrow \infty} \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {i}{n} \ln \frac {i}{n} &= \int_ {0} ^ {1} x \ln x d x = \frac {1}{2} \int_ {0} ^ {1} \ln x d \left(x ^ {2}\right) \\ &= \frac {1}{2} \left(x ^ {2} \ln x \Big | _ {0} ^ {1} - \int_ {0} ^ {1} x ^ {2} \cdot \frac {1}{x} d x\right) = \frac {1}{2} \left(0 - \lim _ {x \rightarrow 0 ^ {+}} x ^ {2} \ln x - \frac {x ^ {2}}{2} \Big | _ {0} ^ {1}\right) \\ \frac {\lim _ {x \rightarrow 0 ^ {+}} x ^ {2} \ln x = 0}{\frac {1}{2}} - \frac {1}{2} \cdot \frac {x ^ {2}}{2} \Big | _ {0} ^ {1} &= - \frac {1}{4}. \end{aligned}</equation>

---

**2022年第7题 | 选择题 | 5分 | 答案: A**
7. 若<equation>I_{1}=\int_{0}^{1}\frac{x}{2(1+\cos x)} \mathrm{d} x, I_{2}=\int_{0}^{1}\frac{\ln(1+x)}{1+\cos x} \mathrm{d} x, I_{3}=\int_{0}^{1}\frac{2x}{1+\sin x} \mathrm{d} x</equation>，则（    )

A.<equation>I_{1}<I_{2}<I_{3}</equation>B.<equation>I_{2}<I_{1}<I_{3}</equation>C.<equation>I_{1}<I_{3}<I_{2}</equation>D.<equation>I_{3}<I_{2}<I_{1}</equation>
答案: A
**解析: **解 通过观察可发现，要比较<equation>I_{1}</equation>与<equation>I_{2}</equation>的大小，只需比较<equation>\frac{x}{2}</equation>与<equation>\ln(1+x)</equation>的大小.

令<equation>f(x)=\ln(1+x)-\frac{x}{2}</equation>，则<equation>f(0)=0</equation><equation>f^{\prime}(x)=\frac{1}{1+x}-\frac{1}{2}</equation>当<equation>x\in(0,1)</equation>时，<equation>f^{\prime}(x)>0</equation><equation>f(x)</equation>单调增加，从而<equation>f(x)>f(0)=0</equation>即<equation>\ln(1+x) > \frac{x}{2},\frac{\ln(1+x)}{1+\cos x} > \frac{x}{2(1+\cos x)}</equation>因此，<equation>I_{2}>I_{1}</equation>此外，同样的方法不难证明在(0,1)内，<equation>\ln(1+x)<x.</equation>另一方面，由于在(0,1)内，<equation>0<\sin x,\cos x<1,1<1+\sin x<2</equation>故<equation>I_{3}</equation>的被积函数<equation>\frac{2x}{1+\sin x} > x.</equation>结合<equation>\ln(1+x)<x</equation>可得，<equation>\frac{\ln(1+x)}{1+\cos x} < \frac{x}{1+\cos x} < x.</equation>于是，<equation>\frac{2x}{1+\sin x}>x > \frac{\ln(1+x)}{1+\cos x}.</equation>因此，<equation>I_{3}>I_{2}.</equation>综上所述，应选A.

---

**2021年第7题 | 选择题 | 5分 | 答案: B**
7. 设函数 f(x)在区间[0,1]上连续，则<equation>\int_{0}^{1} f(x)\mathrm{d}x=</equation>(    )

A.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{n}f\left(\frac{2k-1}{2n}\right)\frac{1}{2n}</equation>B.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{n}f\left(\frac{2k-1}{2n}\right)\frac{1}{n}</equation>C.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{2n}f\left(\frac{k-1}{2n}\right)\frac{1}{n}</equation>D.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{2n}f\left(\frac{k}{2n}\right)\frac{2}{n}</equation>
答案: B
**解析: **解 由于 f(x) 连续，故<equation>\int_{0}^{1} f(x)\mathrm{d}x</equation>存在，从而可对区间[0，1]进行划分，将该积分写为 n项和式的极限.

将[0,1]分为n等份，每个小区间为<equation>\left[ \frac{k-1}{n},\frac{k}{n}\right]</equation><equation>k=1,2,\dots,n</equation>从<equation>\left[ \frac{k-1}{n},\frac{k}{n}\right]</equation>中取点<equation>\frac{2k-1}{2n}</equation>，故由<equation>\int_{0}^{1} f(x)\mathrm{d}x</equation>存在以及定积分的定义可得<equation>\int_ {0} ^ {1} f (x) \mathrm {d} x = \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} f \left(\frac {2 k - 1}{2 n}\right) \cdot \frac {1}{n}.</equation>因此，应选B.

下面说明选项A、C、D均不正确.

选项A：<equation>\lim_{n\to \infty}\sum_{k=1}^{n}f\left(\frac{2k-1}{2n}\right)\frac{1}{2n}=\frac{1}{2}\lim_{n\to \infty}\sum_{k=1}^{n}f\left(\frac{2k-1}{2n}\right)\frac{1}{n}=\frac{1}{2}\int_{0}^{1}f(x)\mathrm{d}x.</equation>选项C：<equation>\lim_{n\to \infty}\sum_{k=1}^{2n}f\left(\frac{k-1}{2n}\right)\frac{1}{n}=2\lim_{n\to \infty}\sum_{k=1}^{2n}f\left(\frac{k-1}{2n}\right)\frac{1}{2n}=2\int_{0}^{1}f(x)\mathrm{d}x.</equation>选项D：<equation>\lim_{n\to \infty}\sum_{k=1}^{2n}f\left(\frac{k}{2n}\right)\frac{2}{n}=4\lim_{n\to \infty}\sum_{k=1}^{2n}f\left(\frac{k}{2n}\right)\frac{1}{2n}=4\int_{0}^{1}f(x)\mathrm{d}x.</equation>

---

**2018年第5题 | 选择题 | 4分 | 答案: C**
5. 设<equation>M=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{(1+x)^{2}}{1+x^{2}}\mathrm{d}x,N=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{1+x}{\mathrm{e}^{x}}\mathrm{d}x,K=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}(1+\sqrt{\cos x})\mathrm{d}x</equation>，则（    )

A. M > N > K B. M > K > N C. K > M > N D. K > N > M
答案: C
**解析: **分别计算 M,N,K.

由于<equation>\frac{2x}{1+x^{2}}</equation>是奇函数，故<equation>\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{2x}{1+x^{2}}\mathrm{d}x=0.</equation>于是，<equation>M = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {(1 + x) ^ {2}}{1 + x ^ {2}} \mathrm {d} x = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {1 + x ^ {2} + 2 x}{1 + x ^ {2}} \mathrm {d} x \frac {\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {2 x}{1 + x ^ {2}} \mathrm {d} x = 0}{\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \mathrm {d} x = \pi}.</equation>注意到当<equation>x\neq 0</equation>时，<equation>\mathrm{e}^{x}>1+x</equation>.于是，在<equation>\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>上，<equation>\frac{1+x}{e^{x}}\leqslant 1</equation>且等号仅在<equation>x=0</equation>处成立.<equation>N = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {1 + x}{\mathrm {e} ^ {x}} \mathrm {d} x < \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \mathrm {d} x = \pi .</equation>由于<equation>\sqrt{\cos x}</equation>是偶函数，且当 x<equation>\in\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>时，<equation>\cos x\geqslant0</equation>且等号仅在端点处成立，故<equation>\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\sqrt{\cos x}\mathrm{d}x=2\int_{0}^{\frac{\pi}{2}}\sqrt{\cos x}\mathrm{d}x>0.</equation>于是，<equation>K = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \left(1 + \sqrt {\cos x}\right) \mathrm {d} x = \pi + \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \sqrt {\cos x} \mathrm {d} x > \pi .</equation>综上所述，<equation>K > M > N</equation>应选C.

---

**2017年第17题 | 解答题 | 10分**
17. (本题满分10分)<equation>\text {求} \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n ^ {2}} \ln \left(1 + \frac {k}{n}\right)</equation>
**解析: **解 根据定积分的定义，提出因子<equation>\frac{1}{n}</equation>，可得<equation>\begin{aligned} \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n ^ {2}} \ln \left(1 + \frac {k}{n}\right) &= \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n} \ln \left(1 + \frac {k}{n}\right) \cdot \frac {1}{n} = \int_ {0} ^ {1} x \ln (1 + x) d x \\ &= \frac {1}{2} \int_ {0} ^ {1} \ln (1 + x) d \left(x ^ {2}\right) \xlongequal {\mathrm {分 部 积 分}} \frac {x ^ {2}}{2} \ln (1 + x) \Bigg | _ {0} ^ {1} - \int_ {0} ^ {1} \frac {x ^ {2}}{2 (1 + x)} d x \\ &= \frac {\ln 2}{2} - \frac {1}{2} \int_ {0} ^ {1} \frac {x ^ {2} - 1 + 1}{1 + x} d x = \frac {\ln 2}{2} - \frac {1}{2} \int_ {0} ^ {1} \left(x - 1 + \frac {1}{1 + x}\right) d x \\ &= \frac {\ln 2}{2} - \frac {1}{2} \left[ \frac {x ^ {2}}{2} - x + \ln (1 + x) \right] \Bigg | _ {0} ^ {1} = \frac {1}{4}. \end{aligned}</equation>因此，原极限<equation>= \frac{1}{4}.</equation>

---

**2016年第10题 | 填空题 | 4分**
<equation>0. \mathrm {极 限} \lim _ {n \rightarrow \infty} \frac {1}{n ^ {2}} \left(\sin \frac {1}{n} + 2 \sin \frac {2}{n} + \dots + n \sin \frac {n}{n}\right) = \underline {{}}</equation>
**答案: **sin 1-cos 1.
**解析: **解 将原表达式作恒等变形，提出因子<equation>\frac{1}{n}</equation><equation>\frac {1}{n ^ {2}} \left(\sin \frac {1}{n} + 2 \sin \frac {2}{n} + \dots + n \sin \frac {n}{n}\right) = \frac {1}{n} \left(\frac {1}{n} \sin \frac {1}{n} + \frac {2}{n} \sin \frac {2}{n} + \dots + \frac {n}{n} \sin \frac {n}{n}\right).</equation><equation>\begin{aligned} \mathrm {原 极 限} &= \lim _ {n \rightarrow \infty} \left(\frac {1}{n} \sum_ {i = 1} ^ {n} \frac {i}{n} \sin \frac {i}{n}\right) = \int_ {0} ^ {1} x \sin x \mathrm {d} x = \int_ {0} ^ {1} x \mathrm {d} (- \cos x) \\ &= - x \cos x \Bigg | _ {0} ^ {1} + \int_ {0} ^ {1} \cos x \mathrm {d} x = \sin 1 - \cos 1. \end{aligned}</equation>

---

**2012年第4题 | 选择题 | 4分 | 答案: D**
4. 设<equation>I_{k}=\int_{0}^{k\pi}\mathrm{e}^{x^{2}}\sin x\mathrm{d}x(k=1,2,3)</equation>，则有（    ）

A.<equation>I_{1}<I_{2}<I_{3}</equation>B.<equation>I_{3}<I_{2}<I_{1}</equation>C.<equation>I_{2}<I_{3}<I_{1}</equation>D.<equation>I_{2}<I_{1}<I_{3}</equation>
答案: D
**解析: **解（法一）记<equation>J_{k}=\int_{(k-1)\pi}^{k\pi}\mathrm{e}^{x^{2}}\sin x\mathrm{d}x(k=1,2,3)</equation>，则<equation>I _ {1} = J _ {1}, \quad I _ {2} = J _ {1} + J _ {2}, \quad I _ {3} = J _ {1} + J _ {2} + J _ {3}.</equation>由于<equation>\mathrm{e}^{x^{2}}>0</equation>，且在（0，<equation>\pi</equation>）上，<equation>\sin x>0</equation>；在（<equation>\pi,2\pi</equation>）上，<equation>\sin x<0</equation>；在（<equation>2\pi,3\pi</equation>）上，<equation>\sin x>0</equation>，故<equation>J_{1}>0</equation>，<equation>J_{2}<0</equation>，<equation>J_{3}>0</equation>.由此可得，<equation>I_{1}>I_{2},I_{3}>I_{2}.</equation>下面比较<equation>I_{1}</equation>和<equation>I_{3}.</equation><equation>I _ {3} - I _ {1} = J _ {2} + J _ {3}.</equation><equation>J _ {3} = \int_ {2 \pi} ^ {3 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x > \mathrm {e} ^ {(2 \pi) ^ {2}} \int_ {2 \pi} ^ {3 \pi} \sin x \mathrm {d} x,</equation><equation>\left| J _ {2} \right| = \left| \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x \right| < \mathrm {e} ^ {(2 \pi) ^ {2}} \left| \int_ {\pi} ^ {2 \pi} \sin x \mathrm {d} x \right|, \quad J _ {2} > - \mathrm {e} ^ {(2 \pi) ^ {2}} \left| \int_ {\pi} ^ {2 \pi} \sin x \mathrm {d} x \right|.</equation>由定积分的几何意义可知，<equation>\int_{2\pi}^{3\pi}\sin x\mathrm{d}x</equation>和<equation>|\int_{\pi}^{2\pi}\sin x\mathrm{d}x|</equation>分别为<equation>\sin x</equation>在<equation>(2\pi ,3\pi)</equation>上以及在<equation>(\pi ,2\pi)</equation>上的部分与<equation>x</equation>轴围成的图形面积.根据<equation>\sin x</equation>的图形，这两部分面积相等，即<equation>\int_{2\pi}^{3\pi}\sin x\mathrm{d}x = \left|\int_{\pi}^{2\pi}\sin x\mathrm{d}x\right|.</equation>于是，<equation>J _ {2} + J _ {3} > \mathrm {e} ^ {(2 \pi) ^ {2}} \left(\int_ {2 \pi} ^ {3 \pi} \sin x \mathrm {d} x - \left| \int_ {\pi} ^ {2 \pi} \sin x \mathrm {d} x \right|\right) = 0,</equation>即<equation>I_{3} > I_{1}.</equation>因此，<equation>I_{2} < I_{1} < I_{3}</equation>应选D.

（法二）在法一中，证明<equation>J_{2} + J_{3} > 0</equation>，也可以使用如下方法.<equation>J _ {3} = \int_ {2 \pi} ^ {3 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x \xlongequal {u = x - \pi} \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {(u + \pi) ^ {2}} \sin (u + \pi) \mathrm {d} u = - \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {(u + \pi) ^ {2}} \sin u \mathrm {d} u,</equation><equation>J _ {2} + J _ {3} = \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x - \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {(x + \pi) ^ {2}} \sin x \mathrm {d} x = \int_ {\pi} ^ {2 \pi} \sin x \left[ \mathrm {e} ^ {x ^ {2}} - \mathrm {e} ^ {(x + \pi) ^ {2}} \right] \mathrm {d} x.</equation>当<equation>x \in(\pi, 2\pi)</equation>时，<equation>\sin x < 0,\mathrm{e}^{x^{2}}-\mathrm{e}^{(x+\pi)^{2}} < 0,\sin x[\mathrm{e}^{x^{2}}-\mathrm{e}^{(x+\pi)^{2}}] > 0</equation>从而<equation>J_{2}+J_{3}>0.</equation>其余同法一.

---

**2012年第10题 | 填空题 | 4分**
10.<equation>\lim_{n\to\infty}n</equation>
**解析: **从定积分的定义出发，对原极限进行恒等变形<equation>\begin{aligned} \lim _ {n \rightarrow \infty} n \left(\frac {1}{1 + n ^ {2}} + \frac {1}{2 ^ {2} + n ^ {2}} + \dots + \frac {1}{n ^ {2} + n ^ {2}}\right) &= \lim _ {n \rightarrow \infty} \frac {1}{n} \left(\frac {n ^ {2}}{1 + n ^ {2}} + \frac {n ^ {2}}{2 ^ {2} + n ^ {2}} + \dots + \frac {n ^ {2}}{n ^ {2} + n ^ {2}}\right) \\ &= \lim _ {n \rightarrow \infty} \frac {1}{n} \left[ \frac {1}{\left(\frac {1}{n}\right) ^ {2} + 1} + \frac {1}{\left(\frac {2}{n}\right) ^ {2} + 1} + \dots + \frac {1}{\left(\frac {n}{n}\right) ^ {2} + 1} \right] \\ &= \lim _ {n \rightarrow \infty} \frac {1}{n} \left[ \sum_ {i = 1} ^ {n} \frac {1}{1 + \left(\frac {i}{n}\right) ^ {2}} \right] = \int_ {0} ^ {1} \frac {1}{1 + x ^ {2}} d x \\ &= \arctan x \Bigg | _ {0} ^ {1} = \frac {\pi}{4}. \end{aligned}</equation>

---

**2011年第6题 | 选择题 | 4分 | 答案: B**
6. 设<equation>I=\int_{0}^{\frac{\pi}{4}}\ln(\sin x)\mathrm{d}x, J=\int_{0}^{\frac{\pi}{4}}\ln(\cot x)\mathrm{d}x, K=\int_{0}^{\frac{\pi}{4}}\ln(\cos x)\mathrm{d}x</equation>，则 I, J, K的大小关系为（    )

A. I < J < K

B. I < K < J

C. J < I < K

D. K < J < I
答案: B
**解析: **解 由于在<equation>\left( 0, \frac{\pi}{4} \right)</equation>上，<equation>0 < \sin x < \cos x < 1 < \cot x</equation>，而<equation>\ln u</equation>为（0，<equation>+\infty</equation>）上的单调增加函数，故<equation>\ln(\sin x) < \ln(\cos x) < 0 < \ln(\cot x).</equation>又因为 I，J，K的积分区间一致，所以 I < K < J.应选B.

---

**2010年第16题 | 解答题 | 10分**
16. (本题满分10分)

16. (本题满分10分)

I. 比较<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>与<equation>\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t</equation>（ n=1,2,<equation>\cdots</equation>）的大小，说明理由；

II. 记<equation>u_{n}=\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>（ n=1,2,<equation>\cdots</equation>），求极限<equation>\lim_{n\to\infty}u_{n}.</equation>
**答案: **（16）（I）<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t<\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t(n=1,2,\cdots)</equation>，理由略；

（Ⅱ）<equation>\lim_{n\to \infty}u_{n}=0.</equation>
**解析: **解（I）在（0，1]上，<equation>|\ln t|</equation><equation>\ln(1+t)</equation>与 t均非负，故比较<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>与<equation>\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t(n=1,2,\cdots)</equation>的大小，只需比较<equation>\ln(1+t)</equation>与 t的大小.

考虑 f（t）=<equation>\ln(1+t)-t.</equation><equation>f ^ {\prime} (t) = \frac {1}{1 + t} - 1.</equation>当<equation>t\in (0,1]</equation>时，<equation>f^{\prime}(t) < 0,f(t)\leqslant f(0) = 0.</equation>因此，当<equation>t\in[0,1]</equation>时，<equation>\ln(1 + t)\leqslant t.</equation>由于两被积函数仅在<equation>t = 1</equation>处相等，故<equation>\int_ {0} ^ {1} | \ln t | [ \ln (1 + t) ] ^ {n} \mathrm {d} t < \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t (n = 1, 2, \dots).</equation>（Ⅱ）（法一）由第（I）问知，<equation>0 < u_{n} < \int_{0}^{1} t^{n}|\ln t|\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {0} ^ {1} t ^ {n} \mid \ln t \mid \mathrm {d} t &= \frac {- 1}{n + 1} \int_ {0} ^ {1} \ln t \mathrm {d} \left(t ^ {n + 1}\right) = \frac {- 1}{n + 1} \left(t ^ {n + 1} \ln t \mid_ {0} ^ {1} - \int_ {0} ^ {1} t ^ {n + 1} \cdot \frac {1}{t} \mathrm {d} t\right) \\ \frac {\lim _ {t \rightarrow 0 ^ {+}} t ^ {n + 1} \ln t = 0}{\overline {{\quad}}} \frac {1}{n + 1} \int_ {0} ^ {1} t ^ {n} \mathrm {d} t &= \frac {1}{(n + 1) ^ {2}}. \end{aligned}</equation>因此，<equation>\lim _ {n \rightarrow \infty} \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t = \lim _ {n \rightarrow \infty} \frac {1}{(n + 1) ^ {2}} = 0.</equation>由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>（法二）由第（I）问知，<equation>0 < u_{n} < \int_{0}^{1} t^{n}|\ln t|\mathrm{d}t.</equation>又因为<equation>\lim_{t\to 0^{+}}t\ln t = 0</equation>，所以存在<equation>M > 0</equation>，使得对任意的<equation>t\in (0,1]</equation>，有<equation>t|\ln t|\leqslant M</equation>，从而<equation>0 < u _ {n} < \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t \leqslant M \int_ {0} ^ {1} t ^ {n - 1} \mathrm {d} t = \frac {M}{n}.</equation>由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>（法三）由于<equation>t\in[0,1]</equation>时，<equation>\ln(1 + t)\leqslant \ln 2 < 1</equation>，故<equation>u_{n}\leqslant (\ln 2)^{n}\int_{0}^{1}|\ln t|\mathrm{d}t.</equation>计算<equation>\int_{0}^{1}|\ln t| \mathrm{d} t</equation>得，<equation>\int_ {0} ^ {1} | \ln t | \mathrm {d} t = - \int_ {0} ^ {1} \ln t \mathrm {d} t = - \left(t \ln t \Big | _ {0} ^ {1} - \int_ {0} ^ {1} 1 \mathrm {d} t\right) \xlongequal {\lim _ {t \rightarrow 0 ^ {+}} t \ln t = 0} 1.</equation>从而<equation>0 < u_{n}\leqslant (\ln 2)^{n}</equation>因为<equation>\lim_{n\to \infty}(\ln 2)^n = 0</equation>，所以由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>

---


#### 定积分的计算

**2025年第17题 | 解答题 | 10分**
17. (本题满分10分)

计算<equation>\int_ {0} ^ {1} \frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} \mathrm {d} x</equation>
**答案: **<equation>\frac {3}{1 0} \ln 2 + \frac {\pi}{1 0}</equation>
**解析: **解设<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {A}{x + 1} + \frac {B x + C}{x ^ {2} - 2 x + 2}.</equation>通分并整理可得，<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {(A + B) x ^ {2} + (B + C - 2 A) x + 2 A + C}{(x + 1) \left(x ^ {2} - 2 x + 2\right)}.</equation>比较<equation>x^{2}, x</equation>的系数以及常数项可得，<equation>A + B = 0,</equation><equation>B + C - 2 A = 0,</equation><equation>2 A + C = 1.</equation>由（1）式可得<equation>B=-A</equation>.将<equation>B=-A</equation>代入（2）式可得<equation>C=3A</equation>.将<equation>C=3A</equation>代入（3）式可得<equation>5A=1</equation>，即<equation>A=\frac{1}{5}</equation>.进一步可得<equation>B=-\frac{1}{5},C=\frac{3}{5}.</equation>由此可得，<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {1}{5} \left(\frac {1}{x + 1} - \frac {x - 3}{x ^ {2} - 2 x + 2}\right).</equation>下面分别计算<equation>\int_0^1\frac{1}{x + 1}\mathrm{d}x</equation>与<equation>\int_0^1\frac{x - 3}{x^2 - 2x + 2}\mathrm{d}x.</equation><equation>\int_ {0} ^ {1} \frac {1}{x + 1} \mathrm {d} x = \ln (x + 1) \Big | _ {0} ^ {1} = \ln 2.</equation><equation>\begin{aligned} \int_ {0} ^ {1} \frac {x - 3}{x ^ {2} - 2 x + 2} \mathrm {d} x &= \int_ {0} ^ {1} \frac {x - 1}{x ^ {2} - 2 x + 2} \mathrm {d} x - \int_ {0} ^ {1} \frac {2}{x ^ {2} - 2 x + 2} \mathrm {d} x \\ &= \frac {1}{2} \int_ {0} ^ {1} \frac {\mathrm {d} \left(x ^ {2} - 2 x + 2\right)}{x ^ {2} - 2 x + 2} - 2 \int_ {0} ^ {1} \frac {1}{1 + (x - 1) ^ {2}} \mathrm {d} x \\ &= \frac {1}{2} \ln \left(x ^ {2} - 2 x + 2\right) \left| _ {0} ^ {1} - 2 \arctan (x - 1) \right| _ {0} ^ {1} \\ &= - \frac {1}{2} \ln 2 - 2 [ 0 - \arctan (- 1) ] = - \frac {1}{2} \ln 2 - \frac {\pi}{2}. \end{aligned}</equation>因此，<equation>\int_ {0} ^ {1} \frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} \mathrm {d} x = \frac {1}{5} \left[ \ln 2 - \left(- \frac {1}{2} \ln 2 - \frac {\pi}{2}\right) \right] = \frac {3 \ln 2 + \pi}{1 0}.</equation>

---

**2023年第15题 | 填空题 | 5分**
15. 设连续函数 f(x)满足<equation>f(x+2)-f(x)=x,\int_{0}^{2} f(x)\mathrm{d} x=0</equation>，则<equation>\int_{1}^{3} f(x)\mathrm{d} x=</equation>___
**答案: **# 1/2
**解析: **解注意到<equation>\int_{2}^{3} f ( x ) \mathrm{d} x=\int_{0}^{1} f ( x+2 ) \mathrm{d} x</equation>，故由<equation>f ( x+2 )-f ( x )=x</equation>可得，<equation>\int_{2}^{3} f ( x ) \mathrm{d} x-\int_{0}^{1} f ( x ) \mathrm{d} x=\int_{0}^{1} f ( x+2 ) \mathrm{d} x-\int_{0}^{1} f ( x ) \mathrm{d} x=\int_{0}^{1} x \mathrm{d} x=\frac{1}{2}.</equation>(1)

又因为<equation>\int_{0}^{1} f ( x ) \mathrm{d} x+\int_{1}^{2} f ( x ) \mathrm{d} x=\int_{0}^{2} f ( x ) \mathrm{d} x=0</equation>，所以<equation>-\int_{0}^{1} f ( x ) \mathrm{d} x=\int_{1}^{2} f ( x ) \mathrm{d} x.</equation>从而由（1）式可得<equation>\int_{2}^{3} f ( x ) \mathrm{d} x+\int_{1}^{2} f ( x ) \mathrm{d} x=\frac{1}{2},</equation>即<equation>\int_{1}^{3} f ( x ) \mathrm{d} x=\frac{1}{2}.</equation>

---

**2022年第13题 | 填空题 | 5分**
13.<equation>\int_ {0} ^ {1} \frac {2 x + 3}{x ^ {2} - x + 1} \mathrm {d} x = \underline {{}}</equation>
**答案: **<equation>\frac{8\sqrt{3}\pi}{9}.</equation>
**解析: **解注意到<equation>( x^{2}-x+1)^{\prime}=2 x-1</equation>，<equation>\frac{2 x+3}{x^{2}-x+1}=\frac{2 x-1}{x^{2}-x+1}+\frac{4}{x^{2}-x+1}.</equation>因此，<equation>\begin{aligned} \int_ {0} ^ {1} \frac {2 x + 3}{x ^ {2} - x + 1} \mathrm {d} x &= \int_ {0} ^ {1} \frac {2 x - 1}{x ^ {2} - x + 1} \mathrm {d} x + 4 \int_ {0} ^ {1} \frac {1}{\left(x - \frac {1}{2}\right) ^ {2} + \frac {3}{4}} \mathrm {d} x \\ &= \int_ {0} ^ {1} \frac {\mathrm {d} \left(x ^ {2} - x + 1\right)}{x ^ {2} - x + 1} + \frac {1 6}{3} \int_ {0} ^ {1} \frac {1}{1 + \left[ \frac {2}{\sqrt {3}} \left(x - \frac {1}{2}\right) \right] ^ {2}} \mathrm {d} x \\ &= \ln \left(x ^ {2} - x + 1\right) \Bigg | _ {0} ^ {1} + \frac {8 \sqrt {3}}{3} \int_ {0} ^ {1} \frac {\mathrm {d} \left[ \frac {2}{\sqrt {3}} \left(x - \frac {1}{2}\right) \right]}{1 + \left[ \frac {2}{\sqrt {3}} \left(x - \frac {1}{2}\right) \right] ^ {2}} \\ &= \frac {8 \sqrt {3}}{3} \arctan \frac {2}{\sqrt {3}} \left(x - \frac {1}{2}\right) \Bigg | _ {0} ^ {1} = \frac {8 \sqrt {3}}{3} \times \frac {\pi}{3} = \frac {8 \sqrt {3} \pi}{9}. \end{aligned}</equation>

---

**2020年第3题 | 选择题 | 4分 | 答案: A**
3. 

.<equation>\int_{0}^{1} \frac{\arcsin \sqrt{x}}{\sqrt{x(1-x)}} \mathrm{d} x=</equation>(    )

A.<equation>\frac{\pi^{2}}{4}</equation>B.<equation>\frac{\pi^{2}}{8}</equation>C.<equation>\frac{\pi}{4}</equation>D.<equation>\frac{\pi}{8}</equation>
答案: A
**解析: **解 令<equation>\sqrt{x}=\sin t,t\in\left(0,\frac{\pi}{2}\right)</equation>，则 x=<equation>\sin^{2}t</equation>,<equation>\mathrm{d}x=2\sin t\cos t\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {0} ^ {1} \frac {\arcsin \sqrt {x}}{\sqrt {x (1 - x)}} \mathrm {d} x \xlongequal {\sqrt {x} = \sin t} \int_ {0} ^ {\frac {\pi}{2}} \frac {t}{\sqrt {\sin^ {2} t \cos^ {2} t}} \cdot 2 \sin t \cos t \mathrm {d} t &= \int_ {0} ^ {\frac {\pi}{2}} 2 t \mathrm {d} t \\ &= t ^ {2} \Big | _ {0} ^ {\frac {\pi}{2}} = \frac {\pi^ {2}}{4}. \end{aligned}</equation>因此，应选A.

---

**2019年第13题 | 填空题 | 4分**
13. 已知函数<equation>f ( x )=x \int_{1}^{x} \frac{\sin t^{2}}{t} \mathrm{d} t</equation>，则<equation>\int_{0}^{1} f ( x ) \mathrm{d} x=</equation>___.
**答案: **<equation>\frac {1}{4} (\cos 1 - 1).</equation>
**解析: **解 （法一）利用分部积分法.

记<equation>F ( x )=\int_{1}^{x}\frac{\sin t^{2}}{t}\mathrm{d} t</equation>，则<equation>F ( 1 )=0,F^{\prime}(x)=\frac{\sin x^{2}}{x}.</equation><equation>\begin{aligned} \int_ {0} ^ {1} f (x) \mathrm {d} x &= \int_ {0} ^ {1} x F (x) \mathrm {d} x = \frac {1}{2} \int_ {0} ^ {1} F (x) \mathrm {d} \left(x ^ {2}\right) = \frac {1}{2} \left[ x ^ {2} F (x) \left| _ {0} ^ {1} - \int_ {0} ^ {1} x ^ {2} \cdot F ^ {\prime} (x) \mathrm {d} x \right. \right] \\ &= - \frac {1}{2} \int_ {0} ^ {1} x ^ {2} \cdot \frac {\sin x ^ {2}}{x} \mathrm {d} x = - \frac {1}{2} \int_ {0} ^ {1} x \sin x ^ {2} \mathrm {d} x = - \frac {1}{4} \int_ {0} ^ {1} \sin x ^ {2} \mathrm {d} \left(x ^ {2}\right) \\ &= \frac {1}{4} \cos x ^ {2} \Bigg | _ {0} ^ {1} = \frac {1}{4} (\cos 1 - 1). \end{aligned}</equation>（法二）交换积分次序.

将 f(x) 代入所求积分.<equation>\int_ {0} ^ {1} f (x) \mathrm {d} x = \int_ {0} ^ {1} x \left(\int_ {1} ^ {x} \frac {\sin t ^ {2}}{t} \mathrm {d} t\right) \mathrm {d} x = \int_ {0} ^ {1} x \mathrm {d} x \int_ {1} ^ {x} \frac {\sin t ^ {2}}{t} \mathrm {d} t.</equation>写出该积分对应的二重积分的积分区域 D. 由二次积分的表达式可知，边界曲线为 t=x， t=1以及 x=0，故<equation>D = \left\{(x, t) \mid x \leqslant t \leqslant 1, 0 \leqslant x \leqslant 1 \right\}.</equation>如图所示，交换积分次序可得<equation>D = \left\{(x, t) \mid 0 \leqslant x \leqslant t, 0 \leqslant t \leqslant 1 \right\}.</equation>因此，<equation>\begin{aligned} \mathrm {原 积 分} &= - \iint_ {D} \frac {x \sin t ^ {2}}{t} \mathrm {d} x \mathrm {d} t = - \int_ {0} ^ {1} \frac {\sin t ^ {2}}{t} \mathrm {d} t \int_ {0} ^ {t} x \mathrm {d} x = - \int_ {0} ^ {1} \frac {\sin t ^ {2}}{t} \cdot \frac {t ^ {2}}{2} \mathrm {d} t \\ &= - \frac {1}{2} \int_ {0} ^ {1} t \sin t ^ {2} \mathrm {d} t = - \frac {1}{4} \int_ {0} ^ {1} \sin t ^ {2} \mathrm {d} \left(t ^ {2}\right) = \frac {1}{4} \cos t ^ {2} \Big | _ {0} ^ {1} = \frac {1}{4} (\cos 1 - 1). \end{aligned}</equation>

---

**2016年第16题 | 解答题 | 10分**
16. (本题满分10分）

设函数<equation>f ( x )=\int_{0}^{1} \left| t^{2}-x^{2} \right| \mathrm{d} t ( x > 0 )</equation>，求<equation>f^{\prime} ( x )</equation>，并求 f(x)的最小值.
**答案: **<equation>f^{\prime}(x)=\left\{ \begin{array}{ll} 4x^{2}-2x, & 0<x<1,\\ 2x, & x\geqslant1. \end{array} \right.</equation>最小值<equation>f\left(\frac{1}{2}\right)=\frac{1}{4}.</equation>
**解析: **解 对 x的取值范围进行讨论.由<equation>f ( x )=\int_{0}^{1} \mid t^{2}-x^{2} \mid \mathrm{d} t</equation>知， •当 x≥1时，<equation>x\geqslant t</equation><equation>\mid t^{2}-x^{2}\mid=x^{2}-t^{2}.</equation>- 当 0 < x < 1时，有两种情况.<equation>\left| t ^ {2} - x ^ {2} \right| = \left\{ \begin{array}{l l} x ^ {2} - t ^ {2}, & 0 \leqslant t \leqslant x, \\ t ^ {2} - x ^ {2}, & x < t \leqslant 1. \end{array} \right.</equation>于是，当 x > 1时，<equation>f (x) = \int_ {0} ^ {1} \left| t ^ {2} - x ^ {2} \right| \mathrm {d} t = \int_ {0} ^ {1} \left(x ^ {2} - t ^ {2}\right) \mathrm {d} t = x ^ {2} - \frac {1}{3}.</equation>当 x=1时，<equation>f (x) = \int_ {0} ^ {1} \left| t ^ {2} - 1 \right| \mathrm {d} t = \int_ {0} ^ {1} \left(1 - t ^ {2}\right) \mathrm {d} t = 1 - \frac {1}{3} = \frac {2}{3}.</equation>当 0 < x < 1时，<equation>\begin{aligned} f (x) &= \int_ {0} ^ {1} \left| t ^ {2} - x ^ {2} \right| \mathrm {d} t = \int_ {0} ^ {x} \left(x ^ {2} - t ^ {2}\right) \mathrm {d} t + \int_ {x} ^ {1} \left(t ^ {2} - x ^ {2}\right) \mathrm {d} t \\ &= x ^ {3} - \frac {t ^ {3}}{3} \left| _ {0} ^ {x} + \frac {t ^ {3}}{3} \right| _ {x} ^ {1} - x ^ {2} (1 - x) = \frac {4}{3} x ^ {3} - x ^ {2} + \frac {1}{3}. \end{aligned}</equation>因此，<equation>f ( x )=\left\{\begin{array}{ll}\frac{4}{3} x^{3}-x^{2}+\frac{1}{3},&0<x<1,\\ x^{2}-\frac{1}{3},&x\geqslant 1.\end{array}\right.</equation>从<equation>f ( x )</equation>的表达式可以看出，<equation>f \left(1 ^ {-}\right) = f \left(1 ^ {+}\right) = f (1) = \frac {2}{3}.</equation>f（x）在 x=1处连续.

由 f(x)的表达式可知，当<equation>0 < x < 1</equation>时，<equation>f^{\prime}(x)=4x^{2}-2x</equation>；当 x > 1时，<equation>f^{\prime}(x)=2x.</equation>当 x=1时，根据导数的定义分别计算 f（x）在 x=1处的左侧导数和右侧导数.<equation>\begin{aligned} f _ {-} ^ {\prime} (1) &= \lim _ {x \rightarrow 1 ^ {-}} \frac {\frac {4}{3} x ^ {3} - x ^ {2} - \frac {1}{3}}{x - 1} = \lim _ {x \rightarrow 1 ^ {-}} \frac {\frac {4}{3} x ^ {3} - \frac {4}{3} x ^ {2} + \frac {1}{3} x ^ {2} - \frac {1}{3}}{x - 1} \\ &= \lim _ {x \rightarrow 1 ^ {-}} \frac {(x - 1) \left[ \frac {4}{3} x ^ {2} + \frac {1}{3} (x + 1) \right]}{x - 1} = \lim _ {x \rightarrow 1 ^ {-}} \left[ \frac {4}{3} x ^ {2} + \frac {1}{3} (x + 1) \right] = 2, \end{aligned}</equation><equation>f _ {+} ^ {\prime} (1) = \lim _ {x \rightarrow 1 ^ {+}} \frac {x ^ {2} - 1}{x - 1} = \lim _ {x \rightarrow 1 ^ {+}} (x + 1) = 2.</equation>由此可见，<equation>f^{\prime}(1)=f_{-}^{\prime}(1)=f_{+}^{\prime}(1)=2.</equation>因此，<equation>f ^ {\prime} (x) = \left\{ \begin{array}{l l} 4 x ^ {2} - 2 x, & 0 < x < 1, \\ 2 x, & x \geqslant 1. \end{array} \right.</equation>从<equation>f^{\prime}(x)</equation>的表达式可以看出，<equation>f^{\prime}(x)</equation>连续，从而<equation>y=f(x)</equation>是一条光滑曲线.

当 x > 1时，<equation>f^{\prime}(x)=2x>0</equation>，故 f(x)在（1，<equation>+\infty</equation>）内单调增加.

当 0 < x < 1时，<equation>f^{\prime}(x)=4x^{2}-2x.</equation>求<equation>f^{\prime}(x)</equation>的零点得，<equation>x=\frac{1}{2}</equation>或 x=0（舍去）.因此，当 0 < x <<equation>\frac{1}{2}</equation>时，<equation>f^{\prime}(x)<0</equation>；当<equation>\frac{1}{2} < x < 1</equation>时，<equation>f^{\prime}(x)>0.</equation>由于 f(x) 连续，故可知 f(x) 的最小值在 x =<equation>\frac{1}{2}</equation>处取得.<equation>f\left(\frac{1}{2}\right)=\frac{4}{3}\times \frac{1}{8}-\frac{1}{4}+\frac{1}{3}=\frac{1}{4}.</equation>

---

**2014年第10题 | 填空题 | 4分**
10. 设<equation>f(x)</equation>是周期为4的可导奇函数,且<equation>f^{\prime}(x)=2(x-1),x\in[0,2]</equation>,则<equation>f(7)=</equation>___.
**解析: **由于<equation>f ( x )</equation>是周期为4的函数，且<equation>7=2 \times4-1</equation>，故<equation>f ( 7 )=f (-1).</equation>(a)

(b)

（法一）由 f(x)为奇函数可得 f（0）=0.由当 x<equation>\in[0,2]</equation>时，<equation>f^{\prime}(x)=2(x-1)</equation>可得， f(x)在 [0,2]上的表达式为<equation>f (x) = \int_ {0} ^ {x} 2 (t - 1) \mathrm {d} t + f (0) = x ^ {2} - 2 x = (x - 1) ^ {2} - 1.</equation>于是<equation>f(1) = -1.</equation>由<equation>f(x)</equation>为奇函数得，<equation>f(-1) = -f(1) = 1</equation>，即<equation>f(7) = 1.</equation>（法二）由 f(x)为奇函数可知，<equation>f(x)=-f(-x).</equation>在等式两端求导得<equation>f^{\prime}(x)=f^{\prime}(-x),</equation>从而<equation>f^{\prime}(x)</equation>为偶函数，<equation>f^{\prime}(x)</equation>的图像关于 y轴对称.在[0，2]上，<equation>f^{\prime}(x)=2(x-1)</equation>，为一条过点（0，-2）和点（1，0）的直线.由此可知，在[-2，0]上，<equation>y=f^{\prime}(x)</equation>为过点（0，-2）和点（-1，0）的直线，可求得<equation>f^{\prime}(x)=-2(x+1).</equation>从而，<equation>f(x)</equation>在[-2，0]上为<equation>f (x) = \int_ {0} ^ {x} - 2 (t + 1) \mathrm {d} t + f (0) = - x ^ {2} - 2 x = - (x + 1) ^ {2} + 1.</equation>因此，<equation>f(-1)=1</equation>，即<equation>f(7)=1.</equation>

---

**2009年第11题 | 填空题 | 4分**
11.<equation>\lim_{n \to \infty} \int_{0}^{1} \mathrm{e}^{-x} \sin nx \mathrm{d}x=</equation>___
**解析: **解 （法一）由分部积分法，可得<equation>\int_ {0} ^ {1} \mathrm {e} ^ {- x} \sin n x \mathrm {d} x = \int_ {0} ^ {1} \mathrm {e} ^ {- x} \mathrm {d} \left(- \frac {\cos n x}{n}\right) = - \frac {1}{n} \int_ {0} ^ {1} \mathrm {e} ^ {- x} \mathrm {d} (\cos n x) = - \frac {1}{n} \left(\mathrm {e} ^ {- x} \cos n x \mid_ {0} ^ {1} + \int_ {0} ^ {1} \mathrm {e} ^ {- x} \cos n x \mathrm {d} x\right).</equation>当<equation>x\in[0,1]</equation>时，<equation>\mathrm{e}^{-x}\in\left[\frac{1}{\mathrm{e}},1\right],|\cos nx|\leqslant1</equation>从而<equation>\left| \int_ {0} ^ {1} \mathrm {e} ^ {- x} \cos n x \mathrm {d} x \right| \leqslant \int_ {0} ^ {1} | \mathrm {e} ^ {- x} \cos n x | \mathrm {d} x \leqslant \int_ {0} ^ {1} 1 \mathrm {d} x \leqslant 1.</equation>因此，<equation>0 \leqslant \left| \mathrm {e} ^ {- x} \cos n x \right| _ {0} ^ {1} + \int_ {0} ^ {1} \mathrm {e} ^ {- x} \cos n x \mathrm {d} x \leqslant \left| \frac {\cos n}{\mathrm {e}} - 1 \right| + 1 \leqslant 3.</equation>从而<equation>\lim _ {n \rightarrow \infty} \int_ {0} ^ {1} \mathrm {e} ^ {- x} \sin n x \mathrm {d} x = \lim _ {n \rightarrow \infty} \left(- \frac {\mathrm {e} ^ {- x} \cos n x \Big| _ {0} ^ {1} + \int_ {0} ^ {1} \mathrm {e} ^ {- x} \cos n x \mathrm {d} x}{n}\right) \stackrel {\text {分 子 有 界}} {=} 0.</equation>（法二）记<equation>I_{n} = \int_{0}^{1}\mathrm{e}^{-x}\sin nx\mathrm{d}x.</equation>我们可以计算出<equation>I_{n}</equation>的值，再求<equation>\lim_{n\to \infty}I_{n}.</equation><equation>\begin{aligned} I _ {n} &= \int_ {0} ^ {1} \mathrm {e} ^ {- x} \sin n x \mathrm {d} x = - \int_ {0} ^ {1} \sin n x \mathrm {d} \left(\mathrm {e} ^ {- x}\right) = - \mathrm {e} ^ {- x} \sin n x \left| _ {0} ^ {1} + n \int_ {0} ^ {1} \mathrm {e} ^ {- x} \cos n x \mathrm {d} x \right. \\ &= - \mathrm {e} ^ {- x} \sin n x \left| _ {0} ^ {1} - n \mathrm {e} ^ {- x} \cos n x \right| _ {0} ^ {1} - n ^ {2} I _ {n}. \end{aligned}</equation>整理得，<equation>I _ {n} = - \frac {n \cos n + \sin n}{\mathrm {e} \left(n ^ {2} + 1\right)} + \frac {n}{n ^ {2} + 1}.</equation>因此，<equation>\lim _ {n \rightarrow \infty} I _ {n} = \lim _ {n \rightarrow \infty} \left[ - \frac {n \cos n + \sin n}{\mathrm {e} \left(n ^ {2} + 1\right)} + \frac {n}{n ^ {2} + 1} \right] = 0.</equation>

---


#### 变限积分

**2024年第3题 | 选择题 | 5分 | 答案: D**
3. 已知函数<equation>f ( x )=\int_{0}^{\sin x}\sin t^{3}\mathrm{d} t,g ( x )=\int_{0}^{x} f ( t )\mathrm{d} t</equation>，则（    ）

A. f(x)是奇函数，g(x)是奇函数 B. f(x)是奇函数，g(x)是偶函数

C. f(x)是偶函数，g(x)是偶函数 D. f(x)是偶函数，g(x)是奇函数
答案: D
**解析: **解（法一）由于<equation>\sin t^{3}</equation>是奇函数，故由分析中的结论可得<equation>h(x)=\int_{0}^{x}\sin t^{3}\mathrm{d}t</equation>是偶函数，而<equation>f(x)=h(\sin x),</equation><equation>f (- x) = h (\sin (- x)) = h (- \sin x) = h (\sin x) = f (x).</equation>于是，<equation>f(x)</equation>是偶函数.

另一方面，<equation>g ( x )</equation>是<equation>f ( x )</equation>的一个原函数，且<equation>g ( 0 ) = \int_{0}^{0} f ( t ) \mathrm{d} t = 0</equation>，故由分析中的结论可得<equation>g ( x )</equation>是奇函数.

因此，<equation>f ( x )</equation>是偶函数，<equation>g ( x )</equation>是奇函数，应选D.

（法二）首先考察<equation>f(-x).</equation><equation>\begin{aligned} f (- x) &= \int_ {0} ^ {\sin (- x)} \sin t ^ {3} \mathrm {d} t = \int_ {0} ^ {- \sin x} \sin t ^ {3} \mathrm {d} t \xlongequal {u = - t} - \int_ {0} ^ {\sin x} \sin (- u) ^ {3} \mathrm {d} u \\ &= - \int_ {0} ^ {\sin x} \left(- \sin u ^ {3}\right) \mathrm {d} u = \int_ {0} ^ {\sin x} \sin u ^ {3} \mathrm {d} u = f (x). \end{aligned}</equation>于是，<equation>f(x)</equation>是偶函数.

下面考察<equation>g(-x).</equation><equation>g (- x) = \int_ {0} ^ {- x} f (t) \mathrm {d} t \underline {{= u = - t}} - \int_ {0} ^ {x} f (- u) \mathrm {d} u = - \int_ {0} ^ {x} f (u) \mathrm {d} u = - g (x).</equation>于是，<equation>g ( x )</equation>是奇函数.

因此，<equation>f(x)</equation>是偶函数，<equation>g(x)</equation>是奇函数，应选D.

---

**2020年第16题 | 解答题 | 10分**
16. (本题满分10分）

已知函数 f(x)连续且<equation>\lim_{x\rightarrow 0}\frac{f(x)}{x}=1,g(x)=\int_{0}^{1}f(xt)\mathrm{d}t</equation>，求 g'(x)并证明 g'(x)在 x=0处连续.
**答案: **<equation>g ^ {\prime} (x) = \left\{ \begin{array}{l l} \frac {x f (x) - \int_ {0} ^ {x} f (u) \mathrm {d} u}{x ^ {2}}, & x \neq 0, \\ \frac {1}{2}, & x = 0. \end{array} \right. \mathrm {证 明 略}.</equation>
**解析: **解 对 g（x）进行恒等变形.<equation>g (x) = \int_ {0} ^ {1} f (x t) \mathrm {d} t \stackrel {u = x t} {=} \int_ {0} ^ {x} f (u) \cdot \frac {1}{x} \mathrm {d} u = \frac {\int_ {0} ^ {x} f (u) \mathrm {d} u}{x} (x \neq 0).</equation>由<equation>\lim_{x\rightarrow 0}\frac{f(x)}{x}=1</equation>可知，分母趋于零，而极限存在，故<equation>\lim_{x\rightarrow 0}f(x)=0.</equation>又因为 f(x) 连续，所以 f(0) = 0.于是，<equation>g(0)=\int_{0}^{1} f(0)\mathrm{d} t=f(0)=0.</equation>当 x≠0时，<equation>g ^ {\prime} (x) = \frac {\left[ \int_ {0} ^ {x} f (u) \mathrm {d} u \right] ^ {\prime} \cdot x - \int_ {0} ^ {x} f (u) \mathrm {d} u}{x ^ {2}} = \frac {x f (x) - \int_ {0} ^ {x} f (u) \mathrm {d} u}{x ^ {2}}.</equation>当<equation>x=0</equation>时，根据导数的定义计算<equation>g^{\prime}(0).</equation><equation>\begin{aligned} g ^ {\prime} (0) &= \lim _ {x \rightarrow 0} \frac {g (x) - g (0)}{x - 0} = \lim _ {x \rightarrow 0} \frac {\frac {\int_ {0} ^ {x} f (u) \mathrm {d} u}{x} - 0}{x} = \lim _ {x \rightarrow 0} \frac {\int_ {0} ^ {x} f (u) \mathrm {d} u}{x ^ {2}} \\ \underline {{\mathrm {洛 必达}}} \lim _ {x \rightarrow 0} \frac {f (x)}{2 x} &= \frac {1}{2}. \end{aligned}</equation>因此，<equation>g^{\prime}(x)=\left\{ \begin{array}{ll}\frac{x f(x)-\int_{0}^{x} f(u)\mathrm{d} u}{x^{2}},&x\neq 0,\\ \frac{1}{2},&x=0. \end{array} \right.</equation>计算<equation>\lim_{x\to 0}g^{\prime}(x).</equation><equation>\lim _ {x \rightarrow 0} g ^ {\prime} (x) = \lim _ {x \rightarrow 0} \frac {x f (x) - \int_ {0} ^ {x} f (u) \mathrm {d} u}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {f (x)}{x} - \lim _ {x \rightarrow 0} \frac {\int_ {0} ^ {x} f (u) \mathrm {d} u}{x ^ {2}} = 1 - \frac {1}{2} = \frac {1}{2}.</equation>由于<equation>\lim_{x\to 0}g^{\prime}(x)=g^{\prime}(0)</equation>，故<equation>g^{\prime}(x)</equation>在 x=0处连续.

---

**2017年第15题 | 解答题 | 10分**
15. (本题满分10分)
**解析: **解（法一）令<equation>u=x-t</equation>，则<equation>t=x-u,\mathrm{d}u=-\mathrm{d}t,</equation><equation>\int_ {0} ^ {x} \sqrt {x - t} \mathrm {e} ^ {t} \mathrm {d} t = - \int_ {x} ^ {0} \sqrt {u} \mathrm {e} ^ {x - u} \mathrm {d} u = \mathrm {e} ^ {x} \int_ {0} ^ {x} \sqrt {u} \mathrm {e} ^ {- u} \mathrm {d} u.</equation>于是，<equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {x} \int_ {0} ^ {x} \sqrt {u} \mathrm {e} ^ {- u} \mathrm {d} u}{\sqrt {x ^ {3}}} \xlongequal {\lim _ {x \rightarrow 0 ^ {+}} \mathrm {e} ^ {x} = 1} \lim _ {x \rightarrow 0 ^ {+}} \frac {\int_ {0} ^ {x} \sqrt {u} \mathrm {e} ^ {- u} \mathrm {d} u}{\sqrt {x ^ {3}}} \xlongequal {\text {洛 必 达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sqrt {x} \mathrm {e} ^ {- x}}{\frac {3}{2} \sqrt {x}} = \frac {2}{3}.</equation>因此，原极限<equation>= \frac{2}{3}.</equation>（法二）由于<equation>\mathrm{e}^{t}</equation>和<equation>\sqrt{x-t}</equation>均为关于 t的连续函数，且<equation>\sqrt{x-t}</equation>在[0,x]上不变号，故由积分中值定理可得，存在<equation>\xi_{x}\in[0,x]</equation>，使得<equation>\int_ {0} ^ {x} \sqrt {x - t} \mathrm {e} ^ {t} \mathrm {d} t = \mathrm {e} ^ {\xi_ {x}} \int_ {0} ^ {x} \sqrt {x - t} \mathrm {d} t.</equation>因此，<equation>\begin{aligned} \lim _ {x \rightarrow 0 ^ {+}} \frac {\int_ {0} ^ {x} \sqrt {x - t} \mathrm {e} ^ {t} \mathrm {d} t}{\sqrt {x ^ {3}}} &= \lim _ {x \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {\xi_ {x}} \int_ {0} ^ {x} \sqrt {x - t} \mathrm {d} t}{\sqrt {x ^ {3}}} = \lim _ {\substack {x \rightarrow 0 ^ {+} \\ 0 \leqslant \xi_ {x} \leqslant x}} \mathrm {e} ^ {\xi_ {x}} \cdot \lim _ {x \rightarrow 0 ^ {+}} \frac {- \frac {2}{3} (x - t) ^ {\frac {3}{2}} \Big| _ {0} ^ {x}}{\sqrt {x ^ {3}}} \\ &= 1 \cdot \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {2}{3} x ^ {\frac {3}{2}}}{\sqrt {x ^ {3}}} = \frac {2}{3}. \end{aligned}</equation>

---

**2015年第11题 | 填空题 | 4分**
11. 设函数 f(x) 连续，<equation>\varphi(x)=\int_{0}^{x^{2}} x f(t)\mathrm{d} t</equation>. 若<equation>\varphi(1)=1, \varphi^{\prime}(1)=5</equation>，则 f(1) =___
**解析: **解 首先，由于在<equation>\int_{0}^{x^{2}}xf(t)\mathrm{d}t</equation>中，x不再是积分变量，故可将 x作为因子提出放在积分号外，即<equation>\varphi (x) = \int_ {0} ^ {x ^ {2}} x f (t) \mathrm {d} t = x \int_ {0} ^ {x ^ {2}} f (t) \mathrm {d} t.</equation>由求导的乘法法则和变限积分的求导公式可得<equation>\varphi^ {\prime} (x) = \int_ {0} ^ {x ^ {2}} f (t) \mathrm {d} t + x f \left(x ^ {2}\right) \cdot 2 x.</equation>由<equation>\varphi(1)=1</equation>可得<equation>\varphi(1)=\int_{0}^{1} f(t)\mathrm{d} t=1</equation>；由<equation>\varphi^{\prime}(1)=5</equation>可得<equation>\varphi^{\prime}(1)=\int_{0}^{1} f(t)\mathrm{d} t+2f(1)=5.</equation>因此，<equation>f(1)=\frac{\varphi^{\prime}(1)-\varphi(1)}{2}=2.</equation>

---

**2013年第3题 | 选择题 | 4分 | 答案: C**
3. 设函数 f(x) =<equation>\left\{\begin{array}{l l} \sin x, & 0 \leqslant x < \pi, \\ 2, & \pi \leqslant x \leqslant 2 \pi, \end{array} \right.</equation>F(x) =<equation>\int_{0}^{x} f(t)\mathrm{d}t</equation>，则（    ）

A. x=<equation>\pi</equation>是函数 F(x)的跳跃间断点 B. x=<equation>\pi</equation>是函数 F(x)的可去间断点

C. F(x)在 x=<equation>\pi</equation>处连续但不可导 D. F(x)在 x=<equation>\pi</equation>处可导
答案: C
**解析: **解（法一）由于<equation>f ( x )</equation>有界且只有一个跳跃间断点，故<equation>f ( x )</equation>可积，而<equation>F ( x ) = \int_{0}^{x} f ( t ) \mathrm{d} t</equation>，于是 F(x)连续.另一方面，由于<equation>x=\pi</equation>是f(x)的跳跃间断点，故F(x)在<equation>x=\pi</equation>处不可导.应选C.

（法二）在<equation>[0,\pi)</equation>上，<equation>F (x) = \int_ {0} ^ {x} \sin t \mathrm {d} t = \left(- \cos t\right) \Bigg | _ {0} ^ {x} = - \cos x + 1.</equation>在<equation>[\pi ,2\pi ]</equation>上，<equation>F (x) = \int_ {0} ^ {\pi} \sin t \mathrm {d} t + \int_ {\pi} ^ {x} 2 \mathrm {d} t = 2 + 2 (x - \pi).</equation>因此，<equation>F (x) = \left\{ \begin{array}{l l} - \cos x + 1, & 0 \leqslant x < \pi , \\ 2 (x + 1 - \pi), & \pi \leqslant x \leqslant 2 \pi . \end{array} \right.</equation>由于<equation>\lim _ {x \rightarrow \pi^ {-}} F (x) = \lim _ {x \rightarrow \pi^ {-}} (- \cos x + 1) = 2, \quad \lim _ {x \rightarrow \pi^ {+}} F (x) = \lim _ {x \rightarrow \pi^ {+}} 2 (x + 1 - \pi) = 2,</equation>且由<equation>F(x)</equation>的定义可得<equation>F(\pi) = 2</equation>，故<equation>F(x)</equation>在<equation>x = \pi</equation>处连续.

由于<equation>F _ {-} ^ {\prime} (\pi) = \lim _ {x \rightarrow \pi^ {-}} \frac {F (\pi) - F (x)}{\pi - x} = \lim _ {x \rightarrow \pi^ {-}} \frac {2 - 1 + \cos x}{\pi - x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow \pi^ {-}} \frac {- \sin x}{- 1} = 0,</equation><equation>F _ {+} ^ {\prime} (\pi) = \lim _ {x \rightarrow \pi^ {+}} \frac {F (x) - F (\pi)}{x - \pi} = \lim _ {x \rightarrow \pi^ {+}} \frac {2 (x + 1 - \pi) - 2}{x - \pi} = 2,</equation>故<equation>F_{-}^{\prime}(\pi)\neq F_{+}^{\prime}(\pi), F(x)</equation>在<equation>x=\pi</equation>处不可导.应选C.

---

**2009年第6题 | 选择题 | 4分 | 答案: D**
6. 设函数 y=f(x)在区间[-1,3]上的图形如图所示，则函数<equation>F ( x )=\int_{0}^{x} f ( t ) \mathrm{d} t</equation>的图形为（    ）

A.

B.

C.

D.
答案: D
**解析: **解（法一）我们可以从<equation>f(x)</equation>出发具体分析<equation>F(x)</equation>的性质.

因为 f(x) 分段连续，所以由变上限积分函数的性质可知，在[-1，0），（0，2），（2，3]上，均有<equation>F^{\prime}(x)=f(x).</equation><equation>\textcircled{1}</equation>由于 f(x)在[-1,3]上有界且只有两个间断点，故 f(x)可积.又因为<equation>F(x)=\int_{0}^{x} f(t)\mathrm{d}t</equation>所以 F(x)连续.<equation>\textcircled{2}</equation>在[-1,0）上，<equation>f ( x ) > 0</equation>，故 F(x)单调增加；在（0，1）上，<equation>f ( x ) < 0</equation>，故 F(x)单调减少；在（1，2）上，<equation>f ( x ) > 0</equation>，故 F(x)单调增加；在（2，3]上，<equation>f ( x ) = 0</equation>，故 F(x)为常函数.<equation>\textcircled{3} F ( 0 )=\int_{0}^{0} f ( t ) \mathrm{d} t=0.</equation>在<equation>[-1,1]</equation>上，<equation>F ( x )</equation>均小于等于零.<equation>\textcircled{4}</equation><equation>f(1) = 0, x = 1</equation>为<equation>F(x)</equation>的驻点及极小值点.

同时满足以上要求的图形只有选项D. 应选D.

（法二）通过图形考察<equation>f(x)</equation>在<equation>[-1,0)</equation>上的性质，可知当<equation>x\in[-1,0)</equation>时，<equation>f(x)\equiv 1</equation>，故<equation>F (- 1) = \int_ {0} ^ {- 1} 1 \mathrm {d} x = - 1, \quad F (0) = \int_ {0} ^ {0} 1 \mathrm {d} x = 0,</equation>从而可排除选项A和选项C.

又由于 f(x)在[-1，3]上有界且只有两个间断点，f(x)在[-1，3]上可积，而 F(x) =<equation>\int_{0}^{x} f(t)\mathrm{d} t</equation>，故 F(x)必连续，从而可以排除选项B.

综上所述，应选D.

---


#### 不定积分的计算

**2023年第2题 | 选择题 | 5分 | 答案: D**

2. 函数 f(x) =<equation>\left\{\begin{array}{l l}{\frac{1}{\sqrt{1+x^{2}}},}&{x\leqslant0}\\ {(x+1)\cos x,}&{x>0}\end{array} \right.</equation>的一个原函数为（    )

A. F(x) =<equation>\left\{\begin{array}{l l}{\ln(\sqrt{1+x^{2}}-x),}&{x\leqslant0}\\ {(x+1)\cos x-\sin x,}&{x>0}\end{array} \right.</equation>B. F(x) =<equation>\left\{\begin{array}{l l}{\ln(\sqrt{1+x^{2}}-x)+1,}&{x\leqslant0}\\ {(x+1)\cos x-\sin x,}&{x>0}\end{array} \right.</equation>C. F(x) =<equation>\left\{\begin{array}{l l}{\ln(\sqrt{1+x^{2}}+x),}&{x\leqslant0}\\ {(x+1)\sin x+\cos x,}&{x>0}\end{array} \right.</equation>D. F(x) =<equation>\left\{\begin{array}{l l}{\ln(\sqrt{1+x^{2}}+x)+1,}&{x\leqslant0}\\ {(x+1)\sin x+\cos x,}&{x>0}\end{array} \right.</equation>

答案: D

**解析:**解（法一）首先，由于 F(x）是 f(x)的原函数，故必连续，而四个选项中的 F(x)均为分段函数，于是我们可以分别考察 F(x)在分界点处的连续性.

对选项 A,<equation>\lim_{x\rightarrow 0^{-}}F(x)=0, \lim_{x\rightarrow 0^{+}}F(x)=1. F(x)</equation>不连续.

对选项B，<equation>\lim_{x\to 0^{-}}F(x)=\lim_{x\to 0^{+}}F(x)=1=F(0).F(x)</equation>连续.

对选项 C<equation>\lim_{x\to 0^{-}}F(x)=0,\lim_{x\to 0^{+}}F(x)=1. F(x)</equation>不连续.

对选项 D<equation>\lim_{x\to 0^{-}}F(x)=\lim_{x\to 0^{+}}F(x)=1=F(0). F(x)</equation>连续.

由上可排除选项A与选项C.

选项B与选项D的差别在于函数表达式.<equation>[ (x + 1) \cos x - \sin x ] ^ {\prime} = \cos x - (x + 1) \sin x - \cos x = - (x + 1) \sin x,</equation><equation>[ (x + 1) \sin x + \cos x ] ^ {\prime} = \sin x + (x + 1) \cos x - \sin x = (x + 1) \cos x.</equation>由上可排除选项B.

因此，应选D.

（法二）当<equation>x\leqslant0</equation>时，<equation>\begin{aligned} F (x) &= \int \frac {\mathrm {d} x}{\sqrt {1 + x ^ {2}}} \xlongequal {x = \tan \theta} \int \frac {\sec^ {2} \theta}{\sec \theta} \mathrm {d} \theta = \int \sec \theta \mathrm {d} \theta = \ln | \sec \theta + \tan \theta | + C _ {1} \\ \frac {x = \tan \theta}{2} \ln \left(\sqrt {1 + x ^ {2}} + x\right) + C _ {1}. \end{aligned}</equation>当 x > 0时，<equation>\begin{aligned} F (x) &= \int (x + 1) \cos x \mathrm {d} x = \int (x + 1) \mathrm {d} (\sin x) = (x + 1) \sin x - \int \sin x \mathrm {d} x \\ &= (x + 1) \sin x + \cos x + C _ {2}. \end{aligned}</equation>四个选项中，仅有选项C、D符合要求.

由于 F(x）是 f(x)在<equation>(-\infty, +\infty)</equation>上的一个原函数，故 F(x)在 x=0处连续.<equation>\lim _ {x \rightarrow 0 ^ {-}} F (x) = \lim _ {x \rightarrow 0 ^ {-}} \left[ \ln \left(\sqrt {1 + x ^ {2}} + x\right) + C _ {1} \right] = C _ {1},</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} F (x) = \lim _ {x \rightarrow 0 ^ {+}} \left[ (x + 1) \sin x + \cos x + C _ {2} \right] = C _ {2} + 1.</equation>由<equation>\lim_{x\to 0^{-}}F(x) = \lim_{x\to 0^{+}}F(x)</equation>可得<equation>C_1 = C_2 + 1.</equation>选项C中，<equation>C_{1}=C_{2}=0,F(x)</equation>不连续，选项D中，<equation>C_{1}=1,C_{2}=0,F(x)</equation>连续，应选D.

---

**2019年第16题 | 解答题 | 10分**

16. (本题满分10分)

求不定积分<equation>\frac {3 x + 6}{(x - 1) ^ {2} \left(x ^ {2} + x + 1\right)} \mathrm {d} x.</equation>

**答案:**-2ln<equation>| x-1 |-\frac{3}{x-1}+\ln( x^{2}+x+1 )+C</equation>，其中C为任意常数.

**解析:**解设<equation>\frac {3 x + 6}{(x - 1) ^ {2} \left(x ^ {2} + x + 1\right)} = \frac {A _ {1}}{x - 1} + \frac {A _ {2}}{(x - 1) ^ {2}} + \frac {B _ {1} x + B _ {2}}{x ^ {2} + x + 1}.</equation>通分并整理可得，<equation>\frac {3 x + 6}{(x - 1) ^ {2} \left(x ^ {2} + x + 1\right)} = \frac {\left(A _ {1} + B _ {1}\right) x ^ {3} + \left(A _ {2} - 2 B _ {1} + B _ {2}\right) x ^ {2} + \left(A _ {2} + B _ {1} - 2 B _ {2}\right) x + \left(- A _ {1} + A _ {2} + B _ {2}\right)}{(x - 1) ^ {2} \left(x ^ {2} + x + 1\right)}.</equation>比较<equation>x^{3}, x^{2}, x</equation>的系数以及常数项可得，<equation>\left[ A _ {1} + B _ {1} = 0, \right.</equation><equation>\left| A _ {2} - 2 B _ {1} + B _ {2} = 0, \right.</equation><equation>A _ {2} + B _ {1} - 2 B _ {2} = 3,</equation><equation>- A _ {1} + A _ {2} + B _ {2} = 6.</equation>由（1）式可得<equation>- A_{1}=B_{1}.</equation>代入（4）式可得<equation>A _ {2} + B _ {1} + B _ {2} = 6.</equation>(5) 式与（3）式相减，可得<equation>3 B_{2}=3</equation>即<equation>B_{2}=1.</equation>分别代入（2）式与（3）式，可解得<equation>A_{2}=3,B_{1}=2.</equation>从而<equation>A_{1}=-2.</equation>因此，<equation>\frac {3 x + 6}{(x - 1) ^ {2} \left(x ^ {2} + x + 1\right)} = \frac {- 2}{x - 1} + \frac {3}{(x - 1) ^ {2}} + \frac {2 x + 1}{x ^ {2} + x + 1}.</equation><equation>\begin{aligned} \int \frac {3 x + 6}{(x - 1) ^ {2} \left(x ^ {2} + x + 1\right)} \mathrm {d} x &= \int \left[ \frac {- 2}{x - 1} + \frac {3}{(x - 1) ^ {2}} + \frac {2 x + 1}{x ^ {2} + x + 1} \right] \mathrm {d} x \\ &= \int \frac {- 2}{x - 1} \mathrm {d} x + \int \frac {3}{(x - 1) ^ {2}} \mathrm {d} x + \int \frac {2 x + 1}{x ^ {2} + x + 1} \mathrm {d} x \\ &= - 2 \ln | x - 1 | - \frac {3}{x - 1} + \int \frac {\mathrm {d} \left(x ^ {2} + x + 1\right)}{x ^ {2} + x + 1} \\ \stackrel {*} {=} - 2 \ln | x - 1 | - \frac {3}{x - 1} + \ln \left(x ^ {2} + x + 1\right) + C, \end{aligned}</equation>其中 C为任意常数.

---

**2018年第15题 | 解答题 | 10分**

15. (本题满分10分)

求不定积分

**答案:**<equation>\frac{\mathrm{e}^{2x}\arctan \sqrt{\mathrm{e}^{x} - 1}}{2} -\frac{1}{6}\left(\mathrm{e}^{x} - 1\right)^{\frac{3}{2}} - \frac{1}{2}\sqrt{\mathrm{e}^{x} - 1} + C</equation>，其中C为任意常数.

**解析:**解 利用分部积分法.<equation>\begin{aligned} \int \mathrm {e} ^ {2 x} \arctan \sqrt {\mathrm {e} ^ {x} - 1} \mathrm {d} x \xlongequal {\text {分 部 积 分}} \frac {1}{2} \int \arctan \sqrt {\mathrm {e} ^ {x} - 1} \mathrm {d} \left(\mathrm {e} ^ {2 x}\right) \\ &= \frac {\mathrm {e} ^ {2 x}}{2} \cdot \arctan \sqrt {\mathrm {e} ^ {x} - 1} - \frac {1}{2} \int \mathrm {e} ^ {2 x} \cdot \frac {1}{1 + \mathrm {e} ^ {x} - 1} \cdot \frac {\mathrm {e} ^ {x}}{2 \sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x \\ &= \frac {\mathrm {e} ^ {2 x} \arctan \sqrt {\mathrm {e} ^ {x} - 1}}{2} - \frac {1}{4} \int \frac {\mathrm {e} ^ {2 x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x. \end{aligned}</equation>下面用两种方法计算<equation>\int \frac{\mathrm{e}^{2 x}}{\sqrt{\mathrm{e}^{x}-1}}\mathrm{d}x.</equation>（法一）令<equation>u=\sqrt{\mathrm{e}^{x}-1}</equation>，则<equation>x=\ln \left(u^{2}+1\right)</equation>，<equation>\mathrm{d}x=\frac{2u}{u^{2}+1}\mathrm{d}u.</equation><equation>\begin{aligned} \int \frac {\mathrm {e} ^ {2 x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x &= \int \frac {\left(u ^ {2} + 1\right) ^ {2}}{u} \cdot \frac {2 u}{u ^ {2} + 1} \mathrm {d} u = 2 \int \left(u ^ {2} + 1\right) \mathrm {d} u = \frac {2}{3} u ^ {3} + 2 u + C _ {1} \\ &= \frac {2}{3} \left(\mathrm {e} ^ {x} - 1\right) ^ {\frac {3}{2}} + 2 \sqrt {\mathrm {e} ^ {x} - 1} + C _ {1}, \end{aligned}</equation>其中<equation>C_{1}</equation>为任意常数.

（法二）令<equation>t=\mathrm{e}^{x}</equation>，则<equation>\mathrm{d}t=\mathrm{e}^{x}\mathrm{d}x.</equation><equation>\begin{aligned} \int \frac {\mathrm {e} ^ {2 x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x &= \int \frac {\mathrm {e} ^ {x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} \left(\mathrm {e} ^ {x}\right) = \int \frac {t}{\sqrt {t - 1}} \mathrm {d} t = \int \frac {t - 1 + 1}{\sqrt {t - 1}} \mathrm {d} t \\ &= \int \left(\sqrt {t - 1} + \frac {1}{\sqrt {t - 1}}\right) \mathrm {d} t = \frac {2}{3} (t - 1) ^ {\frac {3}{2}} + 2 \sqrt {t - 1} + C _ {1} \\ &= \frac {2}{3} \left(\mathrm {e} ^ {x} - 1\right) ^ {\frac {3}{2}} + 2 \sqrt {\mathrm {e} ^ {x} - 1} + C _ {1}, \end{aligned}</equation>其中<equation>C_{1}</equation>为任意常数.

因此，<equation>\text {原 积 分} = \frac {\mathrm {e} ^ {2 x} \arctan \sqrt {\mathrm {e} ^ {x} - 1}}{2} - \frac {1}{6} \left(\mathrm {e} ^ {x} - 1\right) ^ {\frac {3}{2}} - \frac {1}{2} \sqrt {\mathrm {e} ^ {x} - 1} + C,</equation>其中 C为任意常数.

---

**2016年第2题 | 选择题 | 4分 | 答案: D**

2. 已知函数<equation>f ( x )=\left\{\begin{array}{l l}2 ( x-1 ),&x<1,\\\ln x,&x\geqslant 1,\end{array} \right.</equation>则 f(x)的一个原函数是（    )

A.<equation>F ( x )=\left\{\begin{array}{l l} ( x-1 )^{2},&x<1,\\x(\ln x-1),&x\geqslant 1.\end{array} \right.</equation>B.<equation>F ( x )=\left\{\begin{array}{l l} ( x-1 )^{2},&x<1,\\x(\ln x+1)-1,&x\geqslant 1.\end{array} \right.</equation>C.<equation>F ( x )=\left\{\begin{array}{l l} ( x-1 )^{2},&x<1,\\x(\ln x+1)+1,&x\geqslant 1.\end{array} \right.</equation>D.<equation>F ( x )=\left\{\begin{array}{l l} ( x-1 )^{2},&x<1,\\x(\ln x-1)+1,&x\geqslant 1.\end{array} \right.</equation>

答案: D

**解析:**解 （法一）当 x < 1时，<equation>F (x) = \int 2 (x - 1) \mathrm {d} x = (x - 1) ^ {2} + C _ {1};</equation>当 x≥1时，<equation>F (x) = \int \ln x \mathrm {d} x = x (\ln x - 1) + C _ {2},</equation>其中<equation>C_{1}, C_{2}</equation>均为任意常数.

进一步，由于 F(x）是 f(x)在<equation>(-\infty, +\infty)</equation>上的一个原函数，故 F(x)在 x=1处应连续.<equation>\lim _ {x \rightarrow 1 ^ {-}} F (x) = \lim _ {x \rightarrow 1 ^ {-}} \left(x - 1\right) ^ {2} + C _ {1} = C _ {1}, \quad \lim _ {x \rightarrow 1 ^ {+}} F (x) = \lim _ {x \rightarrow 1 ^ {+}} x (\ln x - 1) + C _ {2} = C _ {2} - 1.</equation>若 F(x) 连续，则<equation>C_{1}=C_{2}-1.</equation>选项D中，<equation>C_{1}=0,C_{2}=1,F(x)</equation>连续，应选D.

（法二）首先，由于 F(x）是 f(x)的原函数，必连续，而四个选项中的 F(x)均是分段函数，故我们可以分别考察 F(x)在分界点处的连续性.

选项A：<equation>\lim_{x\to 1^{-}}F(x)=0</equation><equation>\lim_{x\to 1^{+}}F(x)=-1.</equation>不连续.

选项B：<equation>\lim_{x\to 1^{-}}F(x)=0</equation><equation>\lim_{x\to 1^{+}}F(x)=0.</equation>连续.

选项C：<equation>\lim_{x\to 1^{-}}F(x)=0</equation><equation>\lim_{x\to 1^{+}}F(x)=2.</equation>不连续.

选项D：<equation>\lim_{x\to 1^{-}}F(x)=0</equation><equation>\lim_{x\to 1^{+}}F(x)=0.</equation>连续.

由上可排除选项A与选项C.

选项B与选项D的差别在于函数表达式.

计算 f（x）在<equation>[ 1,+\infty)</equation>上的原函数，得<equation>\int f (x) \mathrm {d} x = \int \ln x \mathrm {d} x = x (\ln x - 1) + C,</equation>其中 C为任意常数.比较（1）式与选项B、选项D，可排除选项B.应选D.

---

**2009年第16题 | 解答题 | 10分**

16. (本题满分10分)

计算不定积分<equation>\int\ln\left(1+\sqrt{\frac{1+x}{x}}\right)\mathrm{d}x(x>0).</equation>

**答案:**(16)<equation>x \ln \left( 1+\sqrt{\frac{1+x}{x}} \right)+\frac{1}{2} \ln \left( \sqrt{1+x}+\sqrt{x} \right)-\frac{\sqrt{x}}{2(\sqrt{1+x}+\sqrt{x})}-C</equation>，其中C为任意常数.

**解析:**解（法一）令<equation>u=\sqrt{\frac{1+x}{x}}</equation>，则<equation>x=\frac{1}{u^{2}-1}.</equation>于是，<equation>\int \ln \left(1 + \sqrt {\frac {1 + x}{x}}\right) \mathrm {d} x = \int \ln (1 + u) \mathrm {d} \left(\frac {1}{u ^ {2} - 1}\right) = \frac {\ln (1 + u)}{u ^ {2} - 1} - \int \frac {1}{\left(u ^ {2} - 1\right) \left(u + 1\right)} \mathrm {d} u.</equation>计算<equation>\int \frac{1}{(u^{2}-1)(u+1)} \mathrm{d} u.</equation><equation>\begin{aligned} \int \frac {1}{\left(u ^ {2} - 1\right) (u + 1)} \mathrm {d} u &= \frac {1}{2} \int \frac {(u + 1) - (u - 1)}{\left(u ^ {2} - 1\right) (u + 1)} \mathrm {d} u = \frac {1}{2} \left[ \int \frac {1}{u ^ {2} - 1} \mathrm {d} u - \int \frac {1}{(u + 1) ^ {2}} \mathrm {d} u \right] \\ &= \frac {1}{4} \int \left(\frac {1}{u - 1} - \frac {1}{u + 1}\right) \mathrm {d} u - \frac {1}{2} \int \frac {1}{(u + 1) ^ {2}} \mathrm {d} u = \frac {1}{4} \ln \frac {u - 1}{u + 1} + \frac {1}{2 (u + 1)} + C, \end{aligned}</equation>其中 C为任意常数.这里的<equation>\ln \frac{u - 1}{u + 1}</equation>没有绝对值符号，是因为<equation>u = \sqrt{\frac{1 + x}{x}} > 1.</equation>将 u =<equation>\sqrt{\frac{1+x}{x}}</equation>代回原积分，得<equation>\begin{aligned} \mathrm {原 积 分} &= \frac {\ln (1 + u)}{u ^ {2} - 1} + \frac {1}{4} \ln \frac {u + 1}{u - 1} - \frac {1}{2 (u + 1)} - C \\ \frac {u = \sqrt {\frac {1 + x}{x}}}{x \ln \left(1 + \sqrt {\frac {1 + x}{x}}\right)} + \frac {1}{2} \ln \left(\sqrt {1 + x} + \sqrt {x}\right) - \frac {\sqrt {x}}{2 \left(\sqrt {1 + x} + \sqrt {x}\right)} - C, \end{aligned}</equation>其中 C为任意常数.

（法二）使用待定系数法来求<equation>\int \frac{1}{(u^2 - 1)(u + 1)}\mathrm{d}u.</equation><equation>\begin{aligned} \frac {1}{\left(u ^ {2} - 1\right) (u + 1)} &= \frac {a}{u - 1} + \frac {b}{u + 1} + \frac {c}{(u + 1) ^ {2}} = \frac {a (u + 1) ^ {2} + b (u - 1) (u + 1) + c (u - 1)}{(u - 1) (u + 1) ^ {2}} \\ &= \frac {(a + b) u ^ {2} + (2 a + c) u + a - b - c}{(u - 1) (u + 1) ^ {2}}. \end{aligned}</equation>比较<equation>u^{2}</equation>，<equation>u</equation>的系数以及常数项，可得<equation>\left\{ \begin{array}{l l} a + b = 0, \\ 2a + c = 0, \\ a - b - c = 1, \end{array} \right.</equation>解得<equation>a = \frac{1}{4}, b = -\frac{1}{4}, c = -\frac{1}{2}</equation>.

因此，<equation>\int \frac{1}{(u^{2}-1)(u+1)} \mathrm{d} u=\frac{1}{4} \int \left[ \frac{1}{u-1}-\frac{1}{u+1}-\frac{2}{(u+1)^{2}} \right] \mathrm{d} u=\frac{1}{4} \left( \ln \frac{u-1}{u+1}+\frac{2}{u+1} \right)+C</equation>其中C为任意常数.

其余同法一.

---


#### 一元函数积分学综合题

**2018年第16题 | 解答题 | 10分**
16. (本题满分10分)

已知连续函数 f(x)满足<equation>\int_{0}^{x} f(t)\mathrm{d} t+\int_{0}^{x} t f(x-t)\mathrm{d} t=a x^{2}.</equation>I. 求 f(x);

II. 若 f(x)在区间[0,1]上的平均值为1，求 a的值.
**答案: **( I )<equation>f ( x ) = 2 a \left( 1 - \mathrm{e}^{-x} \right)</equation>;

( II )<equation>a = \frac{\mathrm{e}}{2}.</equation>
**解析: **解（I）令<equation>u=x-t</equation>，则

于是，<equation>\int_{0}^{x}tf(x - t)\mathrm{d}t = \int_{x}^{0}(x - u)f(u)\mathrm{d}(x - u) = \int_{0}^{x}(x - u)f(u)\mathrm{d}u = x\int_{0}^{x}f(u)\mathrm{d}u - \int_{0}^{x}uf(u)\mathrm{d}u.</equation><equation>\int_ {0} ^ {x} f (t) \mathrm {d} t + \int_ {0} ^ {x} t f (x - t) \mathrm {d} t = \int_ {0} ^ {x} f (t) \mathrm {d} t + x \int_ {0} ^ {x} f (t) \mathrm {d} t - \int_ {0} ^ {x} t f (t) \mathrm {d} t = a x ^ {2}.</equation>对<equation>\int_{0}^{x} f(t)\mathrm{d} t+x\int_{0}^{x} f(t)\mathrm{d} t-\int_{0}^{x} t f(t)\mathrm{d} t=a x^{2}</equation>两端关于 x求导，可得<equation>f (x) + \int_ {0} ^ {x} f (t) \mathrm {d} t + x f (x) - x f (x) = 2 a x,</equation>即<equation>f (x) + \int_ {0} ^ {x} f (t) \mathrm {d} t = 2 a x.</equation>由（1）式可知，<equation>f ( x )=2 a x-\int_{0}^{x} f ( t ) \mathrm{d} t</equation>，而 f(x) 连续，故<equation>\int_{0}^{x} f ( t ) \mathrm{d} t</equation>可导，从而 f(x) 可导.

对（1）式两端关于 x求导，可得<equation>f ^ {\prime} (x) + f (x) = 2 a.</equation>这是一个一阶非齐次线性微分方程. 由求解公式可得，<equation>f (x) = \mathrm {e} ^ {- \int \mathrm {d} x} \left(\int 2 a \cdot \mathrm {e} ^ {\int \mathrm {d} x} \mathrm {d} x + C\right) = \mathrm {e} ^ {- x} \left(2 a \mathrm {e} ^ {x} + C\right) = 2 a + C \mathrm {e} ^ {- x},</equation>其中 C为待定常数.

在（1）式中，令 x=0，可得 f(0)=0.将 x=0，f(0)=0代入 f(x）=2a+C<equation>\mathrm{e}^{-x}</equation>可得，0=2a+C，即 C=-2a.

因此，<equation>f ( x ) = 2 a \left( 1 - \mathrm{e}^{-x} \right).</equation>（Ⅱ）根据平均值的定义，<equation>\frac{\int_{0}^{1} f(x)\mathrm{d} x}{1-0}=1</equation>即<equation>\int_{0}^{1} f(x)\mathrm{d} x=1.</equation>由于<equation>\int_ {0} ^ {1} f (x) \mathrm {d} x = \int_ {0} ^ {1} 2 a \left(1 - \mathrm {e} ^ {- x}\right) \mathrm {d} x = 2 a + 2 a \mathrm {e} ^ {- x} \Bigg | _ {0} ^ {1} = 2 a \mathrm {e} ^ {- 1},</equation>故<equation>2a\mathrm{e}^{-1} = 1.</equation>解得<equation>a = \frac{\mathrm{e}}{2}.</equation>因此，<equation>a=\frac{\mathrm{e}}{2}.</equation>

---

**2016年第21题 | 解答题 | 11分**
21. (本题满分11分)

已知函数 f(x)在<equation>\left[ 0, \frac{3\pi}{2} \right]</equation>上连续，在<equation>\left( 0, \frac{3\pi}{2} \right)</equation>内是函数<equation>\frac{\cos x}{2x-3\pi}</equation>的一个原函数，且 f(0)=0.

I. 求 f(x)在区间<equation>\left[ 0, \frac{3\pi}{2} \right]</equation>上的平均值；

II. 证明 f(x)在区间<equation>\left( 0, \frac{3\pi}{2} \right)</equation>内存在唯一零点
**答案: **（I）平均值为<equation>\frac{1}{3\pi}</equation>；

（Ⅱ）证明略.
**解析: **解（I）由于 f(x）是<equation>\frac{\cos x}{2x-3\pi}</equation>的一个原函数，故不妨设 f(x)<equation>= \int_{0}^{x}\frac{\cos t}{2t-3\pi}\mathrm{d}t+C.</equation>由 f(0) = 0可知，C=0.于是，<equation>f(x)=\int_{0}^{x}\frac{\cos t}{2t-3\pi}\mathrm{d}t.</equation>根据 f(x)在区间<equation>\left[0,\frac{3\pi}{2}\right]</equation>上的平均值的定义，可知<equation>A = \frac {\int_ {0} ^ {\frac {3 \pi}{2}} f (x) \mathrm {d} x}{\frac {3 \pi}{2}} = \frac {\int_ {0} ^ {\frac {3 \pi}{2}} \left(\int_ {0} ^ {x} \frac {\cos t}{2 t - 3 \pi} \mathrm {d} t\right) \mathrm {d} x}{\frac {3 \pi}{2}}.</equation>（法一）我们可以使用分部积分法来处理（1）式中的<equation>\int_{0}^{\frac{3\pi}{2}} f(x)\mathrm{d}x.</equation>由上可知，<equation>f^{\prime}(x) = \frac{\cos x}{2x - 3\pi}.</equation>记<equation>I = \int_{0}^{\frac{3\pi}{2}} f(x)\mathrm{d}x</equation>，则<equation>\begin{aligned} I &= \frac {1}{2} \int_ {0} ^ {\frac {3 \pi}{2}} f (x) \mathrm {d} (2 x - 3 \pi) = \frac {1}{2} f (x) (2 x - 3 \pi) \left| _ {0} ^ {\frac {3 \pi}{2}} - \frac {1}{2} \int_ {0} ^ {\frac {3 \pi}{2}} (2 x - 3 \pi) \mathrm {d} [ f (x) ] \right. \\ &= - \frac {1}{2} \int_ {0} ^ {\frac {3 \pi}{2}} (2 x - 3 \pi) \cdot f ^ {\prime} (x) \mathrm {d} x = - \frac {1}{2} \int_ {0} ^ {\frac {3 \pi}{2}} \cos x \mathrm {d} x = \frac {1}{2}. \end{aligned}</equation>因此，<equation>A=\frac{\frac{1}{2}}{\frac{3\pi}{2}}=\frac{1}{3\pi}.</equation>（法二）（1）式右端分式中的分子为一个二次积分.由于被积函数是仅关于 t的函数，故我们不妨交换积分次序，先关于 x积分，再关于 t积分.

该二次积分对应的二重积分的积分区域为<equation>D = \left\{(x, t) \mid 0 \leqslant t \leqslant x, 0 \leqslant x \leqslant \frac {3 \pi}{2} \right\}.</equation>将区域 D写成 Y型区域，得<equation>D = \left\{(x, t) \mid t \leqslant x \leqslant \frac {3 \pi}{2}, 0 \leqslant t \leqslant \frac {3 \pi}{2} \right\}.</equation>因此，<equation>\begin{aligned} A &= \frac {\int_ {0} ^ {\frac {3 \pi}{2}} \left(\int_ {0} ^ {x} \frac {\cos t}{2 t - 3 \pi} \mathrm {d} t\right) \mathrm {d} x}{\frac {3 \pi}{2}} = \frac {\int_ {0} ^ {\frac {3 \pi}{2}} \frac {\cos t}{2 t - 3 \pi} \mathrm {d} t \int_ {t} ^ {\frac {3 \pi}{2}} \mathrm {d} x}{\frac {3 \pi}{2}} = \frac {\int_ {0} ^ {\frac {3 \pi}{2}} \frac {\cos t}{2 t - 3 \pi} \left(\frac {3 \pi}{2} - t\right) \mathrm {d} t}{\frac {3 \pi}{2}} \\ &= - \frac {1}{3 \pi} \int_ {0} ^ {\frac {3 \pi}{2}} \cos t \mathrm {d} t = \frac {1}{3 \pi}. \end{aligned}</equation>（Ⅱ）<equation>f^{\prime}(x)=\frac{\cos x}{2x-3\pi}.</equation>由于在<equation>\left(0,\frac{3\pi}{2}\right)</equation>内，<equation>2x-3\pi < 0</equation>，而在<equation>\left(0,\frac{\pi}{2}\right)</equation>内，<equation>\cos x > 0</equation>；在<equation>\left(\frac{\pi}{2},\frac{3\pi}{2}\right)</equation>内，<equation>\cos x < 0</equation>，故在<equation>\left(0,\frac{\pi}{2}\right)</equation>内，<equation>f^{\prime}(x) < 0</equation>，f(x)单调减少，在<equation>\left(\frac{\pi}{2},\frac{3\pi}{2}\right)</equation>内，<equation>f^{\prime}(x) > 0</equation>，f(x)单调增加.

由于<equation>f ( 0 )=0</equation>，而 f(x)在<equation>\left( 0,\frac{\pi}{2} \right)</equation>内单调减少，故<equation>f\left(\frac{\pi}{2}\right)<0</equation>，f(x)在<equation>\left( 0,\frac{\pi}{2} \right)</equation>内无零点.

若<equation>f\left(\frac{3\pi}{2}\right)>0</equation>，则由连续函数的零点定理以及单调性可知，f(x)在<equation>\left(\frac{\pi}{2},\frac{3\pi}{2}\right)</equation>内存在唯一零点.

下面我们用两种方法来证明<equation>f\left(\frac{3\pi}{2}\right)>0.</equation>（法一）由第（I）问知，<equation>\int_ {0} ^ {\frac {3 \pi}{2}} f (x) \mathrm {d} x = \frac {1}{3 \pi} \times \frac {3 \pi}{2} = \frac {1}{2} > 0.</equation>另一方面，<equation>f(0)=0</equation><equation>f(x)</equation>在<equation>\left(0,\frac{\pi}{2}\right)</equation>内单调减少，在<equation>\left(\frac{\pi}{2},\frac{3\pi}{2}\right)</equation>内单调增加.若<equation>f\left(\frac{3\pi}{2}\right)\leqslant0</equation>，则<equation>f(x)</equation>在<equation>\left(0,\frac{3\pi}{2}\right)</equation>内恒小于零，<equation>\int_{0}^{\frac{3\pi}{2}}f(x)\mathrm{d}x<0</equation>.矛盾.

因此，<equation>f\left(\frac{3\pi}{2}\right) > 0.</equation>（法二）通过换元对<equation>f\left(\frac{3\pi}{2}\right)</equation>进行估计.<equation>\begin{aligned} f \left(\frac {3 \pi}{2}\right) &= \int_ {0} ^ {\frac {3 \pi}{2}} \frac {\cos x}{2 x - 3 \pi} \mathrm {d} x \xlongequal {t = \frac {3 \pi}{2} - x} \int_ {\frac {3 \pi}{2}} ^ {0} \frac {- \sin t}{- 2 t} \mathrm {d} \left(\frac {3 \pi}{2} - t\right) = \frac {1}{2} \int_ {0} ^ {\frac {3 \pi}{2}} \frac {\sin t}{t} \mathrm {d} t \\ &= \frac {1}{2} \int_ {0} ^ {\frac {\pi}{2}} \frac {\sin t}{t} \mathrm {d} t + \frac {1}{2} \int_ {\frac {\pi}{2}} ^ {\pi} \frac {\sin t}{t} \mathrm {d} t + \frac {1}{2} \int_ {\pi} ^ {\frac {3 \pi}{2}} \frac {\sin t}{t} \mathrm {d} t. \end{aligned}</equation>对第三个积分换元，令<equation>u=t-\pi</equation>，得<equation>\int_{\pi}^{\frac{3\pi}{2}}\frac{\sin t}{t}\mathrm{d}t\frac{u=t-\pi}{=}\int_{0}^{\frac{\pi}{2}}\frac{-\sin u}{u+\pi}\mathrm{d}u.</equation>因此，<equation>f \left(\frac {3 \pi}{2}\right) = \frac {1}{2} \int_ {0} ^ {\frac {\pi}{2}} \left(\frac {1}{t} - \frac {1}{t + \pi}\right) \sin t \mathrm {d} t + \frac {1}{2} \int_ {\frac {\pi}{2}} ^ {\pi} \frac {\sin t}{t} \mathrm {d} t > 0.</equation>

---

**2014年第19题 | 解答题 | 10分**
19. (本题满分10分)

设函数 f(x), g(x)在区间 [a,b]上连续，且 f(x)单调增加，<equation>0 \leqslant g ( x ) \leqslant1</equation>证明：

I.<equation>0 \leqslant\int_{a}^{x} g ( t ) \mathrm{d} t \leqslant x-a,x \in[a,b]</equation>II.<equation>\int_{a}^{a+\int_{a}^{b} g ( t ) \mathrm{d} t} f ( x ) \mathrm{d} x \leqslant\int_{a}^{b} f ( x ) g ( x ) \mathrm{d} x.</equation>
**答案: **（19）（I）证明略；

（Ⅱ）证明略.
**解析: **证（I）由于在<equation>[a,b]</equation>上，<equation>0\leqslant g(x)\leqslant 1</equation>，故<equation>0 = \int_ {a} ^ {x} 0 \mathrm {d} t \leqslant \int_ {a} ^ {x} g (t) \mathrm {d} t \leqslant \int_ {a} ^ {x} 1 \mathrm {d} t = x - a.</equation>不等式得证.

（Ⅱ）（法一）构造辅助函数<equation>F ( u )=\int_{a}^{u} f ( x ) g ( x ) \mathrm{d} x-\int_{a}^{a+\int_{a}^{u} g ( t ) \mathrm{d} t} f ( x ) \mathrm{d} x, u \in[ a, b ],</equation>则第（Ⅱ）问中的不等式等价于<equation>F ( b ) \geqslant0.</equation>由于<equation>F ( a )=0</equation>故若能证明<equation>F^{\prime} ( u ) \geqslant0</equation>则由F(u)在<equation>[ a,b]</equation>上单调增加可推出<equation>F ( b ) \geqslant0.</equation>计算<equation>F^{\prime}(u).</equation><equation>F ^ {\prime} (u) = f (u) g (u) - f \left(a + \int_ {a} ^ {u} g (t) \mathrm {d} t\right) g (u) = g (u) \left[ f (u) - f \left(a + \int_ {a} ^ {u} g (t) \mathrm {d} t\right) \right].</equation>由第（I）问知，<equation>0 \leqslant \int_{a}^{u} g ( t ) \mathrm{d} t \leqslant u - a</equation>，故<equation>a \leqslant a+\int_{a}^{u} g ( t ) \mathrm{d} t \leqslant u.</equation>于是，由<equation>f ( x )</equation>在<equation>[ a,b]</equation>上单调增加可知，<equation>f (u) - f \left(a + \int_ {a} ^ {u} g (t) \mathrm {d} t\right) \geqslant 0.</equation>从而<equation>F^{\prime}(u)\geqslant 0,F(u)</equation>在<equation>[a,b]</equation>上单调增加.

因此，<equation>F ( b ) \geqslant F ( a ) = 0</equation>，原不等式成立.

（法二）在下面的证明中，我们将用到积分中值定理的一个一般形式.

若<equation>f ( x )</equation>,<equation>g ( x )</equation>在<equation>[ a,b]</equation>上连续，且<equation>g ( x )</equation>在<equation>[ a,b]</equation>上不变号，则<equation>\int_ {a} ^ {b} f (x) g (x) \mathrm {d} x = f (\xi) \int_ {a} ^ {b} g (x) \mathrm {d} x,</equation>其中<equation>\xi\in[a,b].</equation>记<equation>D=\int_{a}^{b} f ( x ) g ( x ) \mathrm{d} x-\int_{a}^{a+\int_{a}^{b} g ( t ) \mathrm{d} t} f ( x ) \mathrm{d} x.</equation>我们证明<equation>D \geqslant 0</equation>，从而证明原不等式成立.改写D，得<equation>\begin{aligned} D &= \int_ {a} ^ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} [ f (x) g (x) - f (x) ] \mathrm {d} x + \int_ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} ^ {b} f (x) g (x) \mathrm {d} x \\ &= \int_ {a} ^ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} f (x) [ g (x) - 1 ] \mathrm {d} x + \int_ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} ^ {b} f (x) g (x) \mathrm {d} x. \end{aligned}</equation>由于<equation>0 \leqslant g(x) \leqslant 1</equation>，故<equation>g(x) - 1</equation>在<equation>[a,b]</equation>上不变号.由积分中值定理可得<equation>D = f \left(\xi_ {1}\right) \int_ {a} ^ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} [ g (x) - 1 ] \mathrm {d} x + f \left(\xi_ {2}\right) \int_ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} ^ {b} g (x) \mathrm {d} x,</equation>其中，<equation>\xi_{1}\in \left[a,a + \int_{a}^{b}g(t)\mathrm{d}t\right],\xi_{2}\in \left[a + \int_{a}^{b}g(t)\mathrm{d}t,b\right].</equation>由于<equation>f ( x )</equation>在<equation>[ a,b]</equation>上单调增加，故<equation>f (\xi_{1})\leqslant f (\xi_{2})</equation>从而<equation>\begin{array}{l} D \geqslant f \left(\xi_ {1}\right) \left\{\int_ {a} ^ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} [ g (x) - 1 ] \mathrm {d} x + \int_ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} ^ {b} g (x) \mathrm {d} x \right\} = f \left(\xi_ {1}\right) \left[ \int_ {a} ^ {b} g (x) \mathrm {d} x - \int_ {a} ^ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} 1 \mathrm {d} x \right] \\ = f \left(\xi_ {1}\right) \left[ \int_ {a} ^ {b} g (x) \mathrm {d} x - \int_ {a} ^ {b} g (t) \mathrm {d} t \right] = 0. \\ \end{array}</equation>因此，<equation>D\geqslant 0</equation>，原不等式得证.

---

**2014年第20题 | 解答题 | 11分**
20. (本题满分11分)

设函数<equation>f ( x )=\frac{x}{1+x}, x \in[0,1].</equation>定义函数列：<equation>f_{1}(x)=f(x),</equation><equation>f_{2}(x)=f\left(f_{1}(x)\right),</equation><equation>\cdots,</equation><equation>f_{n}(x)=f\left(f_{n-1}(x)\right),</equation><equation>\cdots</equation>记<equation>S_{n}</equation>是由曲线<equation>y=f_{n}(x)</equation>，直线 x=1及 x轴所围平面图形的面积.求极限<equation>\lim_{n \to \infty} n S_{n}.</equation>
**答案: **(20) 1.
**解析: **解 求<equation>f_{n}(x)</equation>的一般项表达式.首先，<equation>f _ {1} (x) = \frac {x}{1 + x}, \quad f _ {2} (x) = \frac {\frac {x}{1 + x}}{1 + \frac {x}{1 + x}} = \frac {x}{1 + 2 x}.</equation>下面用数学归纳法证明对所有正整数 n，都有<equation>f_{n}(x)=\frac{x}{1+nx}.</equation>我们已经验证了<equation>f_{1}(x)</equation>与<equation>f_{2}(x)</equation>的情形. 假设 n = k时，<equation>f_{k}(x)=\frac{x}{1+kx}</equation>则<equation>f _ {k + 1} (x) = f \left(f _ {k} (x)\right) = f \left(\frac {x}{1 + k x}\right) = \frac {\frac {x}{1 + k x}}{1 + \frac {x}{1 + k x}} = \frac {x}{1 + (k + 1) x}.</equation>因此，对所有正整数 n，<equation>f_{n}(x) = \frac{x}{1 + nx}</equation>都成立.

由定积分的几何意义，<equation>\begin{aligned} S _ {n} &= \int_ {0} ^ {1} f _ {n} (x) \mathrm {d} x = \int_ {0} ^ {1} \frac {x}{1 + n x} \mathrm {d} x = \frac {1}{n} \int_ {0} ^ {1} \frac {1 + n x - 1}{1 + n x} \mathrm {d} x = \frac {1}{n} \int_ {0} ^ {1} \left(1 - \frac {1}{1 + n x}\right) \mathrm {d} x \\ &= \frac {1}{n} - \frac {\ln (1 + n x)}{n ^ {2}} \Bigg | _ {0} ^ {1} = \frac {1}{n} - \frac {\ln (1 + n)}{n ^ {2}}. \end{aligned}</equation>因此，<equation>\lim _ {n \rightarrow \infty} n S _ {n} = \lim _ {n \rightarrow \infty} n \left[ \frac {1}{n} - \frac {\ln (1 + n)}{n ^ {2}} \right] = \lim _ {n \rightarrow \infty} \left[ 1 - \frac {\ln (1 + n)}{n} \right].</equation>由<equation>\lim_{x\to +\infty}\frac{\ln(1 + x)}{x}\xlongequal{\text{洛必达}}\lim_{x\to +\infty}\frac{1}{1 + x} = 0</equation>得，<equation>\lim_{n\to \infty}\frac{\ln(1 + n)}{n} = 0.</equation>综上所述，<equation>\lim_{n\to \infty}nS_n = \lim_{n\to \infty}\left[1 - \frac{\ln(1 + n)}{n}\right] = 1.</equation>

---


## 线性代数


### 矩阵的特征值和特征向量


#### 特征值与特征向量

**2025年第8题 | 选择题 | 5分 | 答案: D**
8. 设矩阵<equation>\left( \begin{array}{c c c} {1} & {2} & {0} \\ {2} & {a} & {0} \\ {0} & {0} & {b} \end{array} \right)</equation>有一个正特征值和两个负特征值，则（    ）

A. a > 4,b > 0 B. a < 4,b > 0 C. a > 4,b < 0 D. a < 4,b < 0
答案: D
**解析: **解（法一）记<equation>A = \left( \begin{array}{c c c} 1 & 2 & 0 \\ 2 & a & 0 \\ 0 & 0 & b \end{array} \right)</equation>，由<equation>A</equation>有一个正特征值和两个负特征值可得<equation>A</equation>所对应的二次型<equation>f\left(x_{1}, x_{2}, x_{3}\right)</equation>的正、负惯性指数分别为1,2.

对<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>配方可得<equation>f\left(x_{1}, x_{2}, x_{3}\right) = x_{1}^{2} + a x_{2}^{2} + b x_{3}^{2} + 4 x_{1} x_{2} = \left(x_{1} + 2 x_{2}\right)^{2} + (a - 4) x_{2}^{2} + b x_{3}^{2}.</equation>由于<equation>\left(x_{1} + 2 x_{2}\right)^{2}</equation>的系数为正数1，故<equation>a - 4, b</equation>均为负数，即<equation>\left\{ \begin{array}{l} a - 4 < 0, \\ b < 0. \end{array} \right.</equation>因此，<equation>a < 4,b < 0</equation>，应选D.

（法二）记<equation>A = \left( \begin{array}{c c c} 1 & 2 & 0 \\ 2 & a & 0 \\ 0 & 0 & b \end{array} \right)</equation>，由<equation>A</equation>有一个正特征值和两个负特征值可得<equation>|A| > 0.</equation>计算<equation>|A|</equation>可得<equation>|A| = b(a - 4)</equation>. 由<equation>|A| > 0</equation>可得b与a-4同号，即<equation>a > 4,b > 0</equation>或<equation>a < 4,b < 0.</equation>计算 A的特征多项式.<equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda - 1 & - 2 & 0 \\ - 2 & \lambda - a & 0 \\ 0 & 0 & \lambda - b \end{array} \right| = (\lambda - b) \left[ \lambda^ {2} - (a + 1) \lambda + a - 4 \right].</equation>若<equation>a > 4, b > 0</equation>，则<equation>a + 1 > 0, a - 4 > 0</equation>，由根与系数的关系可知<equation>\lambda^2 - (a + 1)\lambda + a - 4 = 0</equation>的两根均大于0，加上<equation>b > 0, A</equation>的三个特征值均为正数，不符合题意.

若<equation>a < 4, b < 0</equation>，则<equation>a - 4 < 0</equation>，由根与系数的关系可知<equation>\lambda^2 - (a + 1)\lambda + a - 4 = 0</equation>的两根一正、一负，加上<equation>b < 0, A</equation>的三个特征值为一正、两负，符合题意.

因此，应选D.

---

**2020年第8题 | 选择题 | 4分 | 答案: D**
8. 设 A为3阶矩阵，<equation>\alpha_{1},\alpha_{2}</equation>为 A的属于特征值1的线性无关的特征向量，<equation>\alpha_{3}</equation>为 A的属于特征值-1的特征向量，则满足<equation>P^{-1}AP=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>的可逆矩阵 P可为（    ）

A.<equation>\left( \alpha_{1}+\alpha_{3},\alpha_{2},-\alpha_{3} \right)</equation>B.<equation>\left( \alpha_{1}+\alpha_{2},\alpha_{2},-\alpha_{3} \right)</equation>C.<equation>\left( \alpha_{1}+\alpha_{3},-\alpha_{3},\alpha_{2} \right)</equation>D.<equation>\left( \alpha_{1}+\alpha_{2},-\alpha_{3},\alpha_{2} \right)</equation>
答案: D
**解析: **解 由于<equation>P^{-1} A P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，故 P的列向量应分别为属于特征值1，-1，1的特征向量，且

第1列与第3列为属于特征值1的线性无关的特征向量.

由已知条件，<equation>\alpha_{3}</equation>为 A的属于特征值-1的特征向量，故 P的第2列可取为<equation>k\alpha_{3}</equation>其中 k为任意非零常数.

由于<equation>\alpha_{1},\alpha_{2}</equation>为 A的属于特征值1的线性无关的特征向量，且<equation>\left(\alpha_{1}+\alpha_{2},\alpha_{2}\right)=\left(\alpha_{1},\alpha_{2}\right)\left( \begin{array}{cc}1&0\\ 1&1 \end{array} \right)</equation>故<equation>\alpha_{1}+\alpha_{2}</equation>也为 A的属于特征值1的特征向量，且与<equation>\alpha_{2}</equation>线性无关.

因此，<equation>P</equation>可取为<equation>\left(\alpha_{1}+\alpha_{2},-\alpha_{3},\alpha_{2}\right).</equation>应选D.

---

**2018年第14题 | 填空题 | 4分**
14. 设 A为3阶矩阵，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>为线性无关的向量组. 若<equation>A\alpha_{1}=2\alpha_{1}+\alpha_{2}+\alpha_{3},A\alpha_{2}=\alpha_{2}+2\alpha_{3},A\alpha_{3}=-\alpha_{2}+\alpha_{3}</equation>，则 A的实特征值为___
**解析: **解记 P=（<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>）. 由于<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关，故 P可逆由题设可知，<equation>A P = A \left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) = \left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) \left( \begin{array}{c c c} 2 & 0 & 0 \\ 1 & 1 & - 1 \\ 1 & 2 & 1 \end{array} \right) = P \left( \begin{array}{c c c} 2 & 0 & 0 \\ 1 & 1 & - 1 \\ 1 & 2 & 1 \end{array} \right).</equation>于是，<equation>P^{-1} A P=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 1 & 1 & -1 \\ 1 & 2 & 1 \end{array} \right)=B.</equation>由矩阵相似的定义可知，A与B相似.

下面计算矩阵 B的特征多项式.<equation>| \lambda E - B | = \left| \begin{array}{c c c} \lambda - 2 & 0 & 0 \\ - 1 & \lambda - 1 & 1 \\ - 1 & - 2 & \lambda - 1 \end{array} \right| = (\lambda - 2) \left(\lambda^ {2} - 2 \lambda + 3\right).</equation>由于<equation>\lambda^{2}-2\lambda+3=(\lambda-1)^{2}+2>0</equation>，故<equation>|\lambda E-B|=0</equation>仅有一个实根，即<equation>\lambda=2</equation>.于是，B仅有一个实特征值2.

又因为 A与B相似，而相似的矩阵具有相同的特征值，所以 A的实特征值为2.

---

**2017年第7题 | 选择题 | 4分 | 答案: B**
7. 设 A为3阶矩阵，<equation>P=(\alpha_{1},\alpha_{2},\alpha_{3})</equation>为可逆矩阵，使得<equation>P^{-1}AP=\left( \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>，则<equation>A(\alpha_{1}+\alpha_{2}+\alpha_{3})=</equation>(    )

A.<equation>\alpha_{1}+\alpha_{2}</equation>B.<equation>\alpha_{2}+2\alpha_{3}</equation>C.<equation>\alpha_{2}+\alpha_{3}</equation>D.<equation>\alpha_{1}+2\alpha_{2}</equation>
答案: B
**解析: **解（法一）由于<equation>P^{-1} A P=\left( \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>，故<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>分别为 A的属于特征值0,1,2的特征向量.于是，<equation>A\alpha_{1}=0</equation><equation>A\alpha_{2}=\alpha_{2}</equation><equation>A\alpha_{3}=2\alpha_{3}</equation>因此，<equation>A(\alpha_{1}+\alpha_{2}+\alpha_{3})=\alpha_{2}+2\alpha_{3}</equation>应选B.

（法二）由于<equation>P^{-1} A P=\left( \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>，故<equation>A \left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) = A P = P \left( \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right) = \left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) \left( \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right) = \left(0, \alpha_ {2}, 2 \alpha_ {3}\right).</equation>因此，应选B.<equation>\boldsymbol {A} \left(\boldsymbol {\alpha} _ {1} + \boldsymbol {\alpha} _ {2} + \boldsymbol {\alpha} _ {3}\right) = \boldsymbol {\alpha} _ {2} + 2 \boldsymbol {\alpha} _ {3}.</equation>

---

**2017年第14题 | 填空题 | 4分**
14. 设矩阵<equation>A=\left( \begin{array}{c c c} 4 & 1 & -2 \\ 1 & 2 & a \\ 3 & 1 & -1 \end{array} \right)</equation>的一个特征向量为<equation>\left( \begin{array}{c} 1 \\ 1 \\ 2 \end{array} \right)</equation>，则 a=___
**答案: **<equation>- 1.</equation>
**解析: **设（1，1，2）<equation>^{\mathrm{T}}</equation>对应的特征值为<equation>\lambda</equation>，则<equation>\left( \begin{array}{c c c} 4 & 1 & - 2 \\ 1 & 2 & a \\ 3 & 1 & - 1 \end{array} \right) \left( \begin{array}{c} 1 \\ 1 \\ 2 \end{array} \right) = \left( \begin{array}{c} 1 \\ 3 + 2 a \\ 2 \end{array} \right) = \lambda \left( \begin{array}{c} 1 \\ 1 \\ 2 \end{array} \right)</equation>因此，<equation>\lambda=1</equation>，<equation>3+2a=1</equation>，<equation>a=-1.</equation>

---

**2015年第14题 | 填空题 | 4分**
14. 设 3 阶矩阵<equation>\mathbf{A}</equation>的特征值为 2,-2,1,<equation>\mathbf{B}=\mathbf{A}^{2}-\mathbf{A}+\mathbf{E}</equation>,其中<equation>\mathbf{E}</equation>为 3 阶单位矩阵,则行列式<equation>|\mathbf{B}|=</equation>___.
**解析: **解（法一）由于 A有3个不同的特征值，故 A有3个线性无关的特征向量，从而存在可逆矩阵 P使得<equation>P^{-1} A P=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>.于是<equation>\boldsymbol {A} = \boldsymbol {P} \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & - 2 & 0 \\ 0 & 0 & 1 \end{array} \right) \boldsymbol {P} ^ {- 1}, \quad \boldsymbol {A} ^ {2} = \boldsymbol {P} \left( \begin{array}{c c c} 2 ^ {2} & 0 & 0 \\ 0 & (- 2) ^ {2} & 0 \\ 0 & 0 & 1 ^ {2} \end{array} \right) \boldsymbol {P} ^ {- 1},</equation><equation>\boldsymbol {B} = \boldsymbol {P} \left( \begin{array}{c c c} 2 ^ {2} - 2 + 1 & 0 & 0 \\ 0 & (- 2) ^ {2} - (- 2) + 1 & 0 \\ 0 & 0 & 1 ^ {2} - 1 + 1 \end{array} \right) \boldsymbol {P} ^ {- 1} = \boldsymbol {P} \left( \begin{array}{c c c} 3 & 0 & 0 \\ 0 & 7 & 0 \\ 0 & 0 & 1 \end{array} \right) \boldsymbol {P} ^ {- 1}.</equation>因此，<equation>|B| = 21\cdot |P| \cdot |P^{-1}| = 21.</equation>（法二）设<equation>\alpha</equation>为矩阵<equation>A</equation>的属于特征值<equation>\lambda</equation>的特征向量，即<equation>A\alpha = \lambda \alpha</equation>，则<equation>\boldsymbol {B} \boldsymbol {\alpha} = \left(\boldsymbol {A} ^ {2} - \boldsymbol {A} + \boldsymbol {E}\right) \boldsymbol {\alpha} = \left(\lambda^ {2} - \lambda + 1\right) \boldsymbol {\alpha}.</equation>由上可见，若<equation>\alpha</equation>为A的属于特征值<equation>\lambda</equation>的特征向量，则<equation>\alpha</equation>为B的属于特征值<equation>\lambda^{2}-\lambda+1</equation>的特征向量.A的3个线性无关的特征向量也是B的3个线性无关的特征向量，对应的特征值为<equation>\lambda^{2}-\lambda+1</equation><equation>(\lambda=2,-2,1)</equation>.由此可求得B的特征值为3,7,1.

因此，<equation>|B| = 3\times 7\times 1 = 21.</equation>

---

**2011年第23题 | 解答题 | 11分**

设<equation>A</equation>为3阶实对称矩阵，<equation>A</equation>的秩为2，且<equation>\left( \begin{array}{c c} 1 & 1 \\ 0 & 0 \\ - 1 & 1 \end{array} \right) = \left( \begin{array}{c c} - 1 & 1 \\ 0 & 0 \\ 1 & 1 \end{array} \right)</equation>I. 求 A的所有特征值与特征向量；

II. 求矩阵 A.
**答案: **23) （I）特征值-1，1，0，分别对应特征向量<equation>k_{1}\left(1,0,-1\right)^{\mathrm{T}}, k_{2}\left(1,0,1\right)^{\mathrm{T}}, k_{3}\left(0,1,0\right)^{\mathrm{T}}</equation>，其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意非零常数；

（Ⅱ）<equation>\left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{array} \right).</equation>
**解析: **解（I）由于<equation>A\left( \begin{array}{c c} 1 & 1 \\ 0 & 0 \\ -1 & 1 \end{array} \right)=\left( \begin{array}{c c} -1 & 1 \\ 0 & 0 \\ 1 & 1 \end{array} \right)</equation>，故<equation>\alpha_{1}=(1,0,-1)^{\mathrm{T}},\alpha_{2}=(1,0,1)^{\mathrm{T}}</equation>满足<equation>A\alpha_{1}=</equation><equation>-\alpha_{1},A\alpha_{2}=\alpha_{2}</equation>，从而<equation>\alpha_{1}</equation>为A的属于特征值-1的特征向量，<equation>\alpha_{2}</equation>为A的属于特征值1的特征向量又因为<equation>r(A)=2,|A|=0</equation>，所以A还有一个特征值为零.

因为实对称矩阵属于不同特征值的特征向量相互正交，所以 A的属于特征值0的特征向量<equation>\boldsymbol{\alpha}_{3}=(x_{1},x_{2},x_{3})^{\mathrm{T}}</equation>满足<equation>\boldsymbol{\alpha}_{1}^{\mathrm{T}}\boldsymbol{\alpha}_{3}=0,\boldsymbol{\alpha}_{2}^{\mathrm{T}}\boldsymbol{\alpha}_{3}=0</equation>从而得<equation>\left\{ \begin{array}{l l} x_{1}-x_{3}=0, \\ x_{1}+x_{3}=0. \end{array} \right.</equation>由此可得<equation>\boldsymbol{\alpha}_{3}=k_{3}(0,1,0)^{\mathrm{T}},k_{3}</equation>为任意非零常数.

因此，<equation>\mathbf{A}</equation>的特征值为-1，1，0.对应的特征向量分别为<equation>k_{1}(1,0,-1)^{\mathrm{T}}</equation><equation>k_{2}(1,0,1)^{\mathrm{T}}</equation><equation>k_{3}(0,1,0)^{\mathrm{T}}</equation>其中<equation>k_{1},k_{2},k_{3}</equation>为任意非零常数.

（Ⅱ）（法一）由第（I）问可知，取<equation>P=\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)=\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \\ -1 & 1 & 0 \end{array} \right)</equation>，可得<equation>P^{-1}AP=</equation><equation>\left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>，于是<equation>A=P\left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right) P^{-1}.</equation>利用初等变换法计算<equation>P^{-1}.</equation><equation>\begin{array}{l} (P, E) = \left( \begin{array}{c c c c c c} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 1 & 0 \\ - 1 & 1 & 0 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} + r _ {1}} \left( \begin{array}{c c c c c c} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 1 & 0 \\ 0 & 2 & 0 & 1 & 0 & 1 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {*} \times \frac {1}{2}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & \frac {1}{2} & 0 & - \frac {1}{2} \\ 0 & 0 & 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & \frac {1}{2} & 0 & \frac {1}{2} \end{array} \right) \xrightarrow {r _ {2} \leftrightarrow r _ {3} ^ {* *}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & \frac {1}{2} & 0 & - \frac {1}{2} \\ 0 & 1 & 0 & \frac {1}{2} & 0 & \frac {1}{2} \\ 0 & 0 & 1 & 0 & 1 & 0 \end{array} \right). \\ \end{array}</equation>于是，<equation>P^{-1}=\left( \begin{array}{c c c} \frac{1}{2} & 0 & -\frac{1}{2} \\ \frac{1}{2} & 0 & \frac{1}{2} \\ 0 & 1 & 0 \end{array} \right).</equation>因此，<equation>\begin{aligned} \boldsymbol {A} &= \boldsymbol {P} \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \boldsymbol {P} ^ {- 1} &= \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \\ - 1 & 1 & 0  \right) \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \left( \begin{array}{c c c} \frac {1}{2} & 0 & - \frac {1}{2} \\ \frac {1}{2} & 0 & \frac {1}{2} \\ 0 & 1 & 0  \right) \\ &= \left( \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & 0 & 0 \\ 1 & 1 & 0  \right) \left( \begin{array}{c c c} \frac {1}{2} & 0 & - \frac {1}{2} \\ \frac {1}{2} & 0 & \frac {1}{2} \\ 0 & 1 & 0  \right) &= \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0  \right). \end{aligned}</equation>或者，由<equation>A P = \left(A \alpha_ {1}, A \alpha_ {2}, A \alpha_ {3}\right) = \left(- \alpha_ {1}, \alpha_ {2}, 0\right)</equation>可得，<equation>\boldsymbol {A} = \left(- \alpha_ {1}, \alpha_ {2}, 0\right) \boldsymbol {P} ^ {- 1} = - \frac {1}{2} \left( \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & 0 & 0 \\ 1 & 1 & 0 \end{array} \right) \left( \begin{array}{c c c} - 1 & 0 & 1 \\ - 1 & 0 & - 1 \\ 0 & - 2 & 0 \end{array} \right) = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{array} \right).</equation>（法二）将<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>单位化，组成一正交矩阵<equation>Q=\left( \begin{array}{c c c} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0 \\ 0 & 0 & 1 \\ -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0 \end{array} \right)</equation>，则<equation>Q^{\mathrm{T}}AQ=\left( \begin{array}{c c c} -1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>因此，<equation>\begin{aligned} \boldsymbol {A} &= \boldsymbol {Q} \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \boldsymbol {Q} ^ {\mathrm {T}} &= \left( \begin{array}{c c c} \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {2}} & 0 \\ 0 & 0 & 1 \\ - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {2}} & 0  \right) \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \left( \begin{array}{c c c} \frac {1}{\sqrt {2}} & 0 & - \frac {1}{\sqrt {2}} \\ \frac {1}{\sqrt {2}} & 0 & \frac {1}{\sqrt {2}} \\ 0 & 1 & 0  \right) \\ &= \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0  \right). \end{aligned}</equation>

---

**2010年第23题 | 解答题 | 11分**
23. (本题满分11分)

设<equation>A=\left( \begin{array}{c c c} 0 & -1 & 4 \\ -1 & 3 & a \\ 4 & a & 0 \end{array} \right)</equation>，正交矩阵Q使<equation>Q^{\mathrm{T}}AQ</equation>为对角矩阵，若Q的第1列为<equation>\frac{1}{\sqrt{6}}(1,2,1)^{\mathrm{T}}</equation>求a,Q.
**答案: **<equation>a = - 1, Q = \left( \begin{array}{c c c} \frac {1}{\sqrt {6}} & - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {3}} \\ \frac {2}{\sqrt {6}} & 0 & - \frac {1}{\sqrt {3}} \\ \frac {1}{\sqrt {6}} & \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {3}} \end{array} \right), Q ^ {\mathrm {T}} A Q = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & - 4 & 0 \\ 0 & 0 & 5 \end{array} \right).</equation>
**解析: **解 由题设知，<equation>\alpha_{1}=\frac{1}{\sqrt{6}}(1,2,1)^{\mathrm{T}}</equation>为 A的特征向量.不妨设<equation>\alpha_{1}</equation>对应的特征值为 k，则<equation>\begin{aligned} \boldsymbol {A} \boldsymbol {\alpha} _ {1} &= \frac {1}{\sqrt {6}} \left( \begin{array}{c c c} 0 & - 1 & 4 \\ - 1 & 3 & a \\ 4 & a & 0  \right) \left(  1 \\ 2 \\ 1  \right) &= \frac {1}{\sqrt {6}} \left( \begin{array}{c} 2 \\ 5 + a \\ 4 + 2 a  \right) &= \frac {k}{\sqrt {6}} \left(  1 \\ 2 \\ 1  \right). \end{aligned}</equation>从而有<equation>\left\{ \begin{array}{l}2 = k,\\ 5 + a = 2k,\\ 4 + 2a = k, \end{array} \right.</equation>解得<equation>a = -1, k = 2.</equation>于是，<equation>A = \left( \begin{array}{c c c}0 & -1 & 4\\ -1 & 3 & -1\\ 4 & -1 & 0 \end{array} \right).</equation>计算 A的特征多项式得<equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda & 1 & - 4 \\ 1 & \lambda - 3 & 1 \\ - 4 & 1 & \lambda \end{array} \right| = (\lambda - 2) (\lambda - 5) (\lambda + 4).</equation>因此，<equation>A</equation>的特征值为2，5，-4.<equation>\alpha_{1}</equation>是<equation>A</equation>的属于特征值2的特征向量.

先求属于特征值-4的特征向量<equation>\alpha_{2}</equation>.由特征向量的定义可知，<equation>(-4E - A)x = 0.</equation><equation>\begin{array}{l} - 4 E - A = \left( \begin{array}{c c c} - 4 & 1 & - 4 \\ 1 & - 7 & 1 \\ - 4 & 1 & - 4 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c} - 4 & 1 & - 4 \\ 1 & - 7 & 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} + 4 r _ {2}} \left( \begin{array}{c c c} 0 & 1 & 0 \\ 1 & - 7 & 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} + 7 r _ {1} ^ {* *}} \frac {1}{r _ {1} ^ {* *} \leftrightarrow r _ {2} ^ {*}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>由此可得<equation>\left\{\begin{array}{l l}x_{1}+x_{3}=0,\\ x_{2}=0,\end{array}\right.</equation>故<equation>\boldsymbol{\xi}_{2}=(-1,0,1)^{\mathrm{T}}</equation>为它的一个基础解系.将<equation>\boldsymbol{\xi}_{2}</equation>单位化得<equation>\boldsymbol{\alpha}_{2}=\frac{1}{\sqrt{2}}(-1,0,1)^{\mathrm{T}}.</equation>同理，解（5E-A）<equation>x=0.</equation><equation>5 E - A = \left( \begin{array}{c c c} 5 & 1 & - 4 \\ 1 & 2 & 1 \\ - 4 & 1 & 5 \end{array} \right) \xrightarrow [ r _ {1} ^ {*} \times \left(- \frac {1}{9}\right) ]{r _ {1} - 5 r _ {2}} \left( \begin{array}{c c c} 0 & 1 & 1 \\ 1 & 2 & 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {1} ^ {* *} \leftrightarrow r _ {2} ^ {*} ]{r _ {2} - r _ {1} ^ {* *}} \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>由此可得<equation>\left\{ \begin{array}{l}x_{1} + x_{2} = 0,\\ x_{2} + x_{3} = 0, \end{array} \right.</equation>故<equation>\xi_3 = (1, -1, 1)^{\mathrm{T}}</equation>为它的一个基础解系.将<equation>\xi_3</equation>单位化得<equation>\alpha_{3} = \frac{1}{\sqrt{3}} (1, -1, 1)^{\mathrm{T}}.</equation>或者也可以如下求<equation>\alpha_{3}</equation>由于<equation>\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2}</equation>为属于不同特征值的特征向量，故它们相互正交。于是<equation>\boldsymbol {\alpha} _ {3} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {1} = 0, \quad \boldsymbol {\alpha} _ {3} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {2} = 0.</equation><equation>\pmb{\alpha}_{3}</equation>的坐标<equation>(x_{1}, x_{2}, x_{3})^{\mathrm{T}}</equation>满足<equation>\left\{ \begin{array}{l} x_{1} + 2x_{2} + x_{3} = 0, \\ x_{1} - x_{3} = 0. \end{array} \right.</equation>因此可得<equation>\pmb{\xi}_{3} = (1, -1, 1)^{\mathrm{T}}</equation>为此方程组的一个基础解系.将<equation>\pmb{\xi}_{3}</equation>单位化得<equation>\pmb{\alpha}_{3} = \frac{1}{\sqrt{3}} (1, -1, 1)^{\mathrm{T}}.</equation>因此，

---


#### 矩阵的相似与相似对角化

**2025年第22题 | 解答题 | 12分**
22. （本题满分12分）

已知矩阵<equation>A = \left( \begin{array}{c c c} 4 & 1 & -2 \\ 1 & 1 & 1 \\ -2 & 1 & a \end{array} \right)</equation>与<equation>B = \left( \begin{array}{c c c} k & 0 & 0 \\ 0 & 6 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>合同.

I. 求 a的值及 k的范围.

II. 若存在正交矩阵<equation>Q</equation>，使得<equation>Q^{\mathrm{T}}AQ = B</equation>，求<equation>k</equation>及<equation>Q</equation>
**答案: **<equation>(1) a = 4, k > 0; (2) k = 3, Q = \left[ \begin{array}{c c c} \frac {1}{\sqrt {3}} & - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {6}} \\ \frac {1}{\sqrt {3}} & 0 & - \frac {2}{\sqrt {6}} \\ \frac {1}{\sqrt {3}} & \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {6}} \end{array} \right]</equation>
**解析: **解（I）由于矩阵A，B合同，故A，B的正、负特征值个数均相等。又因为B是对角矩阵，对角元为k，6，0，所以A也有零特征值，<equation>|A|=0.</equation>计算<equation>|A|</equation>可得<equation>| A | = \left| \begin{array}{c c c} 4 & 1 & - 2 \\ 1 & 1 & 1 \\ - 2 & 1 & a \end{array} \right| \frac {c _ {1} - c _ {2}}{c _ {3} - c _ {2}} \left| \begin{array}{c c c} 3 & 1 & - 3 \\ 0 & 1 & 0 \\ - 3 & 1 & a - 1 \end{array} \right| = (- 1) ^ {2 + 2} \cdot 1 \cdot \left| \begin{array}{c c} 3 & - 3 \\ - 3 & a - 1 \end{array} \right| = 3 (a - 4).</equation>由<equation>|A| = 0</equation>可得<equation>a = 4.</equation>于是，<equation>A = \left( \begin{array}{c c c} 4 & 1 & -2 \\ 1 & 1 & 1 \\ -2 & 1 & 4 \end{array} \right).</equation>计算 A的特征值.<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - 4 & - 1 & 2 \\ - 1 & \lambda - 1 & - 1 \\ 2 & - 1 & \lambda - 4  \right| \xlongequal {r _ {1} - r _ {3}} \left| \begin{array}{c c c} \lambda - 6 & 0 & 6 - \lambda \\ - 1 & \lambda - 1 & - 1 \\ 2 & - 1 & \lambda - 4  \right| \\ &= (\lambda - 6) \left| \begin{array}{c c c} 1 & 0 & - 1 \\ - 1 & \lambda - 1 & - 1 \\ 2 & - 1 & \lambda - 4  \right| \xlongequal {c _ {3} + c _ {1}} (\lambda - 6) \left| \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & \lambda - 1 & - 2 \\ 2 & - 1 & \lambda - 2  \right| \\ &= (\lambda - 6) \left(\lambda^ {2} - 3 \lambda\right) = \lambda (\lambda - 3) (\lambda - 6). \end{aligned}</equation>于是，<equation>A</equation>的特征值为3，6，0. A有两个正特征值，一个零特征值.

由 A,B的正、负特征值个数均相等可得，B也有两个正特征值.结合B的特征值为k,6,0可得， k的取值范围是（0，<equation>+\infty).</equation>（Ⅱ）若存在正交矩阵Q，使得<equation>Q^{\mathrm{T}}AQ=B</equation>，则A，B相似，从而A，B的特征值相同，由此可得 k=3. 由于B为对角矩阵，故满足<equation>Q^{\mathrm{T}}AQ=B</equation>的正交矩阵Q的列向量即A的单位正交化后的属于特征值3,6,0的特征向量.

分别计算<equation>A</equation>的属于特征值3,6,0的特征向量

考虑（3E-A）x=0.<equation>3 E - A = \left( \begin{array}{c c c} - 1 & - 1 & 2 \\ - 1 & 2 & - 1 \\ 2 & - 1 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} - 1 & - 1 & 2 \\ 0 & 3 & - 3 \\ 0 & - 3 & 3 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & - 2 \\ 0 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right).</equation><equation>\xi_{1} = \left( \begin{array}{c}1\\ 1\\ 1 \end{array} \right)</equation>为 A 的属于特征值3的一个线性无关的特征向量.

考虑（6E-A）x=0.<equation>6 E - A = \left( \begin{array}{c c c} 2 & - 1 & 2 \\ - 1 & 5 & - 1 \\ 2 & - 1 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 2 & - 1 & 2 \\ - 1 & 5 & - 1 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 0 & 9 & 0 \\ - 1 & 5 & - 1 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation><equation>\xi_{2} = \left( \begin{array}{c} - 1 \\ 0 \\ 1 \end{array} \right)</equation>为<equation>A</equation>的属于特征值6的一个线性无关的特征向量.

考虑（0E-A）x=0.<equation>- A = \left( \begin{array}{c c c} - 4 & - 1 & 2 \\ - 1 & - 1 & - 1 \\ 2 & - 1 & - 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 0 & 3 & 6 \\ 1 & 1 & 1 \\ 0 & - 3 & - 6 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{array} \right).</equation><equation>\xi_3 = \left( \begin{array}{c}1\\ -2\\ 1 \end{array} \right)</equation>为 A 的属于特征值0的一个线性无关的特征向量.

或者，由实对称矩阵属于不同特征值的特征向量相互正交可得，<equation>A</equation>的属于特征值0的特征向量<equation>\xi_{3}</equation>与<equation>\xi_{1},\xi_{2}</equation>均正交，即<equation>\xi_3^{\mathrm{T}}\xi_1 = 0,\xi_3^{\mathrm{T}}\xi_2 = 0.</equation>于是，<equation>\xi_{3} = (x_{1},x_{2},x_{3})^{\mathrm{T}}</equation>满足<equation>\left\{ \begin{array}{l}x_{1} + x_{2} + x_{3} = 0,\\ -x_{1} + x_{3} = 0, \end{array} \right.</equation>解得<equation>\left( \begin{array}{c}x_{1}\\ x_{2}\\ x_{3} \end{array} \right) = k\left( \begin{array}{c}1\\ -2\\ 1 \end{array} \right)</equation>，其中<equation>k</equation>为任意非零常数.

由于<equation>\xi_{1},\xi_{2},\xi_{3}</equation>已经相互正交，故只需将它们单位化即可得到 A的一组相互正交的单位特征向量.令<equation>Q = \left(\frac {\xi_ {1}}{\| \xi_ {1} \|}, \frac {\xi_ {2}}{\| \xi_ {2} \|}, \frac {\xi_ {3}}{\| \xi_ {3} \|}\right) = \left( \begin{array}{c c c} \frac {1}{\sqrt {3}} & - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {6}} \\ \frac {1}{\sqrt {3}} & 0 & - \frac {2}{\sqrt {6}} \\ \frac {1}{\sqrt {3}} & \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {6}} \end{array} \right),</equation>则<equation>Q^{\mathrm{T}} A Q=B, Q</equation>为所求矩阵

---

**2024年第10题 | 选择题 | 5分 | 答案: B**
10. 设 A,B为2阶矩阵，且<equation>A B=B A</equation>，则“ A有两个不相等的特征值”是“ B可对角化”的（    ）

A. 充分必要条件 B. 充分不必要条件

C. 必要不充分条件 D. 既不充分也不必要条件
答案: B
**解析: **解设<equation>\lambda_{1},\lambda_{2}</equation>是A的两个不同的特征值，非零向量<equation>\alpha_{1},\alpha_{2}</equation>满足<equation>A\alpha_{1} = \lambda_{1}\alpha_{1},A\alpha_{2} = \lambda_{2}\alpha_{2}</equation>.由于<equation>\lambda_{1}</equation><equation>\neq \lambda_{2}</equation>，故<equation>\alpha_{1},\alpha_{2}</equation>线性无关.进一步可得，<equation>AB\alpha_{1} = BA\alpha_{1} = \lambda_{1}B\alpha_{1},AB\alpha_{2} = BA\alpha_{2} = \lambda_{2}B\alpha_{2}</equation>.

（i）若<equation>B\alpha_{i}\neq 0(i = 1,2)</equation>，则<equation>B\alpha_{i}</equation>是A的属于<equation>\lambda_{i}</equation>的一个特征向量。又因为A有两个不同的特征值且为2阶矩阵，所以这两个特征值均只有一个线性无关的特征向量，从而<equation>B\alpha_{i} = k_{i}\alpha_{i}(k_{i}\neq 0)</equation>，<equation>\alpha_{i}</equation>是B的属于特征值<equation>k_{i}</equation>的一个特征向量.

（ii）若<equation>B\alpha_{i} = 0</equation>，则<equation>\alpha_{i}</equation>是B的属于特征值0的一个特征向量.

不论是哪种情况，<equation>\alpha_{i} ( i=1,2 )</equation>均为B的两个线性无关的特征向量，故B能相似对角化.因此，“A有两个不相等的特征值”是“B可对角化”的充分条件.

但是，“A有两个不相等的特征值”不是“B可对角化”的必要条件.取 A=B=E，则 AB= BA，且B是对角矩阵，但是A没有两个不同的特征值.

综上所述，“<equation>\mathbf{A}</equation>有两个不相等的特征值”是“<equation>\mathbf{B}</equation>可对角化”的充分不必要条件，应选B.

---

**2023年第22题 | 解答题 | 12分**
22. (本题满分12分)

设矩阵 A满足：对任意<equation>x_{1}, x_{2}, x_{3}</equation>均有<equation>A\left( \begin{array}{c} x_{1} \\ x_{2} \\ x_{3} \end{array} \right)=\left( \begin{array}{c} x_{1}+x_{2}+x_{3} \\ 2 x_{1}-x_{2}+x_{3} \\ x_{2}-x_{3} \end{array} \right)</equation>I. 求 A；

II. 求可逆矩阵<equation>P</equation>与对角矩阵<equation>\Lambda</equation>，使得<equation>P^{-1}AP = \Lambda</equation>
**答案: **<equation>\begin{aligned} (\mathrm {I}) \boldsymbol {A} &= \left( \begin{array}{c c c} 1 & 1 & 1 \\ 2 & - 1 & 1 \\ 0 & 1 & - 1  \right); \\ (\mathrm {I I}) \boldsymbol {P} &= \left( \begin{array}{c c c} 0 & - 1 & 4 \\ - 1 & 0 & 3 \\ 1 & 2 & 1  \right), \boldsymbol {A} &= \left( \begin{array}{c c c} - 2 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 2  \right). \end{aligned}</equation>
**解析: **（ I ）因为<equation>\begin{aligned} \mathbf {A} \left(  x _ {1} \\ x _ {2} \\ x _ {3}  \right) &= \left( \begin{array}{c} x _ {1} + x _ {2} + x _ {3} \\ 2 x _ {1} - x _ {2} + x _ {3} \\ x _ {2} - x _ {3}  \right) &= \left( \begin{array}{c c c} 1 & 1 & 1 \\ 2 & - 1 & 1 \\ 0 & 1 & - 1  \right) \left(  x _ {1} \\ x _ {2} \\ x _ {3}  \right) \end{aligned}</equation>对任意<equation>x_{1}, x_{2}, x_{3}</equation>均成立，所以方程组<equation>\left[ A-\left( \begin{array}{c c c} 1 & 1 & 1 \\ 2 & -1 & 1 \\ 0 & 1 & -1 \end{array} \right) \right] \left( \begin{array}{l} x_{1} \\ x_{2} \\ x_{3} \end{array} \right)=\mathbf{0}</equation>的解为全体3维列向量.于是该方程组的系数矩阵的秩为0，从而<equation>A-\left( \begin{array}{c c c} 1 & 1 & 1 \\ 2 & -1 & 1 \\ 0 & 1 & -1 \end{array} \right)=\mathbf{0}</equation>，即<equation>A=\left( \begin{array}{c c c} 1 & 1 & 1 \\ 2 & -1 & 1 \\ \end{array} \right).</equation>（Ⅱ）计算 A的特征值. A的特征多项式为<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - 1 & - 1 & - 1 \\ - 2 & \lambda + 1 & - 1 \\ 0 & - 1 & \lambda + 1  \right| \xlongequal {\text {按 第三 行 展开}} \left| \begin{array}{c c} \lambda - 1 & - 1 \\ - 2 & - 1  \right| + (\lambda + 1) \left| \begin{array}{c c} \lambda - 1 & - 1 \\ - 2 & \lambda + 1  \right| \\ &= - (\lambda + 1) + (\lambda + 1) \left(\lambda^ {2} - 3\right) = (\lambda + 1) \left(\lambda^ {2} - 4\right) \\ &= (\lambda + 1) (\lambda + 2) (\lambda - 2). \end{aligned}</equation>于是，A的特征值为-2，-1，2.

计算 A的属于特征值-2的特征向量.考虑方程组<equation>(-2 E-A) x=0.</equation><equation>- 2 E - A = \left( \begin{array}{c c c} - 3 & - 1 & - 1 \\ - 2 & - 1 & - 1 \\ 0 & - 1 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} - 3 & 0 & 0 \\ - 2 & 0 & 0 \\ 0 & 1 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>解方程组<equation>(-2 E-A) x=0</equation>可得<equation>\left( \begin{array}{c}0\\ -1\\ 1 \end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c}0\\ -1\\ 1 \end{array} \right)</equation>为A的属于特征值 -2的一个特征向量.

计算 A的属于特征值-1的特征向量.考虑方程组<equation>(- E-A) x=0.</equation><equation>- E - A = \left( \begin{array}{c c c} - 2 & - 1 & - 1 \\ - 2 & 0 & - 1 \\ 0 & - 1 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 2 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>解方程组<equation>(- E-A) x=0</equation>可得<equation>\left( \begin{array}{c}-1\\ 0\\ 2 \end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c}-1\\ 0\\ 2 \end{array} \right)</equation>为 A的属于特征值 1的一个特征向量.

计算 A的属于特征值2的特征向量.考虑方程组（2E-A）x=0.<equation>2 E - A = \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ - 2 & 3 & - 1 \\ 0 & - 1 & 3 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ 0 & 1 & - 3 \\ 0 & - 1 & 3 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & - 4 \\ 0 & 1 & - 3 \\ 0 & 0 & 0 \end{array} \right).</equation>解方程组<equation>( 2 E-A ) x=0</equation>可得<equation>\left( \begin{array}{c c c} 4 \\ 3 \\ 1 \end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c} 4 \\ 3 \\ 1 \end{array} \right)</equation>为A的属于特征值2的一个特征向量.

令<equation>P=\left( \begin{array}{c c c} 0 & -1 & 4 \\ -1 & 0 & 3 \\ 1 & 2 & 1 \end{array} \right).</equation>由于属于不同特征值的特征向量线性无关，故P的列向量组线性无关，从而P可逆.由特征向量的性质可得<equation>P^{-1} A P=A</equation>其中<equation>\Lambda=\left( \begin{array}{c c c} -2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>

---

**2022年第8题 | 选择题 | 5分 | 答案: B**
8. 设 A为3阶矩阵，<equation>\Lambda=\left( \begin{array}{c c c} {1} & {0} & {0} \\ {0} & {-1} & {0} \\ {0} & {0} & {0} \end{array} \right)</equation>，则 A的特征值为1，-1，0的充分必要条件是（    )

A. 存在可逆矩阵 P,Q，使得<equation>A=P\Lambda Q</equation>B. 存在可逆矩阵 P，使得<equation>A=P\Lambda P^{-1}</equation>C. 存在正交矩阵 Q，使得<equation>A=Q\Lambda Q^{-1}</equation>D. 存在可逆矩阵 P，使得<equation>A=P\Lambda P^{\mathrm{T}}</equation>
答案: B
**解析: **解3阶矩阵 A的特征值为1，-1，0意味着 A有3个不同的特征值，从而 A相似于与它具有相同特征值的对角矩阵，即<equation>\Lambda</equation>.于是，A的特征值为1，-1，0的充分必要条件即 A与<equation>\Lambda</equation>相似的充分必要条件.

选项B实际上为 A与<equation>\Lambda</equation>相似的定义，即存在可逆矩阵 P，使得<equation>\Lambda = P^{-1}AP</equation>，也即<equation>A=P\Lambda P^{-1}</equation>因此，应选B.

下面说明选项A、C、D不正确.

选项A是A与A等价的定义.若两矩阵相似，则它们必等价，但两个等价的矩阵不一定相似，如<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>和<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>，故选项A是A与A相似的必要不充分条件.

因为正交矩阵也是可逆矩阵，所以选项C是A与A相似的充分条件.但选项C并不是A与A相似的必要条件，因为A不一定能找到一组相互正交的特征向量，这一要求对实对称矩阵成立，对一般矩阵不成立.

取<equation>\boldsymbol{\xi}_{1}=\left( \begin{array}{c}1\\ 0\\ 0 \end{array} \right),\boldsymbol{\xi}_{2}=\left( \begin{array}{c}1\\ 1\\ 0 \end{array} \right),\boldsymbol{\xi}_{3}=\left( \begin{array}{c}1\\ 0\\ 1 \end{array} \right)</equation>，则<equation>\boldsymbol{\xi}_{1},\boldsymbol{\xi}_{2},\boldsymbol{\xi}_{3}</equation>相互均不正交.令<equation>P=(\boldsymbol{\xi}_{1},\boldsymbol{\xi}_{2},\boldsymbol{\xi}_{3})</equation>，<equation>\boldsymbol{A}=</equation><equation>\left( \begin{array}{c c c}1&0&0\\ 0&-1&0\\ 0&0&0 \end{array} \right)</equation>，则<equation>\boldsymbol {A} = \boldsymbol {P} \boldsymbol {\Lambda} \boldsymbol {P} ^ {- 1} = \left( \begin{array}{c c c} 1 & 1 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right) \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} 1 & - 2 & - 1 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>A与对角矩阵 A相似，但是 A的线性无关的特征向量均不正交.

选项D是A与A合同的定义.对一般矩阵而言，相似与合同之间并无相互蕴含的关系.

考虑选项A的反例<equation>\left( \begin{array}{c c c} {1} & {0} & {0} \\ {0} & {0} & {0} \\ {0} & {0} & {0} \end{array} \right)</equation>和<equation>\left( \begin{array}{c c c} {2} & {0} & {0} \\ {0} & {0} & {0} \\ {0} & {0} & {0} \end{array} \right)</equation>，这两个矩阵具有相同的正、负惯性指数，从而合同，但它们并不相似.

考虑选项C的反例<equation>A=\left( \begin{array}{c c c}1&0&0\\ 0&-1&0\\ 0&0&0 \end{array} \right), A=\left( \begin{array}{c c c}1&-2&-1\\ 0&-1&0\\ 0&0&0 \end{array} \right).</equation>由前面的分析可知，A与A相似又因为A是实对称矩阵，而与实对称矩阵合同的矩阵一定是实对称矩阵，但A不是实对称矩阵，所以A与A不合同.

因此，选项D既不是A与A相似的充分条件，也不是A与A相似的必要条件.

---

**2021年第22题 | 解答题 | 12分**
22. (本题满分12分)

设矩阵<equation>A = \left( \begin{array}{c c c} 2 & 1 & 0 \\ 1 & 2 & 0 \\ 1 & a & b \end{array} \right)</equation>仅有两个不同的特征值，若 A相似于对角矩阵，求 a,b的值，并求可逆矩阵 P，使得<equation>P^{-1} A P</equation>为对角矩阵.
**答案: **当<equation>a = 1,b = 1</equation>时，<equation>P = \left( \begin{array}{c c c} - 1 & 0 & 1 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right),P^{-1} A P = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 3 \end{array} \right)</equation>为对角矩阵；

当<equation>a = -1,b = 3</equation>时，<equation>P = \left( \begin{array}{c c c} 1 & 0 & -1 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right),P^{-1} A P = \left( \begin{array}{c c c} 3 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>为对角矩阵
**解析: **计算 A的特征多项式.<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - 2 & - 1 & 0 \\ - 1 & \lambda - 2 & 0 \\ - 1 & - a & \lambda - b  \right| \xlongequal {\text {按 第三 列 展 开}} (\lambda - b) \left| \begin{array}{c c} \lambda - 2 & - 1 \\ - 1 & \lambda - 2  \right| \\ &= (\lambda - b) \left[ (\lambda - 2) ^ {2} - 1 \right] = (\lambda - 1) (\lambda - 3) (\lambda - b). \end{aligned}</equation>A的所有特征值为1,3,b.

若 A仅有两个不同的特征值，则 b只可能为1或者3.

下面分情况讨论.

(1) 若 b=1，则 A的特征值为1，1，3.

计算 A的属于特征值1的特征向量.考虑 （E-A）x=0.<equation>\boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} - 1 & - 1 & 0 \\ - 1 & - 1 & 0 \\ - 1 & - a & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 - a & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>若 A可相似对角化，则方程组 （E-A）x=0有两个线性无关的解. r（E-A）=1.于是，a=1.

解方程组（<equation>E-A ) x=0</equation>可得<equation>\left( \begin{array}{c}-1\\1\\0\end{array} \right)</equation>与<equation>\left( \begin{array}{c}0\\0\\1\end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c}-1\\1\\0\end{array} \right)</equation>与<equation>\left( \begin{array}{c}0\\0\\1\end{array} \right)</equation>为 A的属于特征值1的两个线性无关的特征向量.

计算 A的属于特征值3的特征向量.考虑<equation>( 3 E-A ) x=0.</equation><equation>3 E - A = \left( \begin{array}{c c c} 1 & - 1 & 0 \\ - 1 & 1 & 0 \\ - 1 & - 1 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & - 1 & 0 \\ 0 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right).</equation>解方程组<equation>( 3 E-A ) x=0</equation>可得<equation>\left( \begin{array}{c} 1 \\ 1 \\ 1 \end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c} 1 \\ 1 \\ 1 \end{array} \right)</equation>为A的属于特征值3的一个特征向量.

令<equation>P=\left( \begin{array}{c c c} -1 & 0 & 1 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right)</equation>，则<equation>P^{-1} A P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 3 \end{array} \right)</equation>为对角矩阵.

(2) 若 b=3，则 A的特征值为1，3，3.

计算 A的属于特征值3的特征向量.考虑（<equation>3 E-A ) x=0.</equation><equation>3 E - A = \left( \begin{array}{c c c} 1 & - 1 & 0 \\ - 1 & 1 & 0 \\ - 1 & - a & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & - 1 & 0 \\ 0 & - 1 - a & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>若 A可相似对角化，则方程组<equation>( 3 E-A ) x=0</equation>有两个线性无关的解. r（3E-A）=1.于是，a=-1.解方程组<equation>( 3 E-A ) x=0</equation>可得<equation>\left( \begin{array}{l} 1 \\ 1 \\ 0 \end{array} \right)</equation>与<equation>\left( \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{l} 1 \\ 1 \\ 0 \end{array} \right)</equation>与<equation>\left( \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right)</equation>为 A的属于特征值3的两个线性无关的特征向量.

计算 A的属于特征值1的特征向量.考虑 （E-A）x=0.<equation>E - A = \left( \begin{array}{c c c} - 1 & - 1 & 0 \\ - 1 & - 1 & 0 \\ - 1 & 1 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right)</equation>解方程组<equation>( E-A ) x=0</equation>可得<equation>\left( \begin{array}{c}-1\\1\\1\end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c}-1\\1\\1\end{array} \right)</equation>为 A的属于特征值1的一个特征向量.

令<equation>P=\left( \begin{array}{c c c}1&0&-1\\1&0&1\\0&1&1\end{array} \right)</equation>，则<equation>P^{-1} A P=\left( \begin{array}{c c c}3&0&0\\0&3&0\\0&0&1\end{array} \right)</equation>为对角矩阵.

---

**2020年第23题 | 解答题 | 11分**
23. (本题满分11分)

设 A为2阶矩阵，<equation>P=(\alpha ,A\alpha)</equation>，其中<equation>\alpha</equation>是非零向量且不是 A的特征向量.

I. 证明 P为可逆矩阵

II. 若<equation>A^{2}\alpha+A\alpha-6\alpha=0</equation>.求<equation>P^{-1}AP</equation>，并判断 A是否相似于对角矩阵.
**答案: **（I）证明略；

（Ⅱ）<equation>P^{-1} A P=\left( \begin{array}{cc} 0 & 6 \\ 1 & -1 \end{array} \right), A</equation>相似于对角矩阵<equation>\left( \begin{array}{c c} 2 & 0 \\ 0 & -3 \end{array} \right).</equation>
**解析: **解（I）要证明 P为可逆矩阵，可证明<equation>\alpha, A\alpha</equation>线性无关.

假设<equation>\alpha, A\alpha</equation>线性相关，则存在不全为零的常数<equation>k_{1}, k_{2}</equation>，使得<equation>k_{1}\alpha+k_{2}A\alpha=0.</equation>若<equation>k_{2}=0</equation>，则<equation>k_{1}\alpha=0</equation>.但<equation>\alpha</equation>为非零向量，故<equation>k_{1}=0</equation>.这与假设矛盾.

若<equation>k_{2}\neq0</equation>，则<equation>A\alpha=-\frac{k_{1}}{k_{2}}\alpha.</equation>由特征向量的定义可知<equation>\alpha</equation>为A的特征向量.这与<equation>\alpha</equation>不是A的特征向量矛盾.

因此，<equation>\alpha, A\alpha</equation>线性无关.P为可逆矩阵.

（Ⅱ）考虑AP.<equation>\begin{aligned} A P &= \left(A \alpha , A ^ {2} \alpha\right) \xlongequal {A ^ {2} \alpha + A \alpha - 6 \alpha = 0} \left(A \alpha , 6 \alpha - A \alpha\right) = (\alpha , A \alpha) \left( \begin{array}{c c} 0 & 6 \\ 1 & - 1  \right) \\ &= P \left( \begin{array}{c c} 0 & 6 \\ 1 & - 1  \right). \end{aligned}</equation>由第（I）问可知，P可逆.上式两端同时左乘<equation>P^{-1}</equation>可得<equation>P^{-1} A P=\left( \begin{array}{cc}0&6\\ 1&-1 \end{array} \right).</equation>记<equation>B=\left( \begin{array}{cc}0&6\\ 1&-1 \end{array} \right)</equation>，则A与B相似.A与对角矩阵相似等价于B与对角矩阵相似.

计算 B的特征多项式.<equation>| \lambda E - B | = \left| \begin{array}{c c} \lambda & - 6 \\ - 1 & \lambda + 1 \end{array} \right| = \lambda^ {2} + \lambda - 6 = (\lambda + 3) (\lambda - 2).</equation>2与-3是B的两个不同特征值.于是，B相似于对角矩阵<equation>\left( \begin{array}{cc}2&0\\ 0&-3 \end{array} \right).</equation>由相似关系的传递性可知，A相似于对角矩阵<equation>\left( \begin{array}{cc}2&0\\ 0&-3 \end{array} \right).</equation>

---

**2019年第23题 | 解答题 | 11分**
23. （本题满分11分）

已知矩阵<equation>A = \left( \begin{array}{c c c} - 2 & - 2 & 1 \\ 2 & x & - 2 \\ 0 & 0 & - 2 \end{array} \right)</equation>与<equation>B = \left( \begin{array}{c c c} 2 & 1 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & y \end{array} \right)</equation>相似.

I. 求 x,y;

II. 求可逆矩阵<equation>P</equation>，使得<equation>P^{-1}AP = B</equation>.
**答案: **（ I ）<equation>x=3,y=-2;</equation>（Ⅱ）满足<equation>P^{-1} A P=B</equation>的可逆矩阵为<equation>\boldsymbol {P} = \left( \begin{array}{c c c} - 1 & - 1 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right)</equation>
**解析: **解（I）由于 A,B相似，故它们的迹与行列式均相同.

由 A,B有相同的迹可得<equation>- 4+x=1+y</equation>，即 x-y=5.

计算<equation>| A |,| B |. B</equation>为上三角矩阵，故易得<equation>| B |=-2 y.</equation><equation>| A | \xlongequal {\mathrm {按 第三 行 展 开}} (- 2) \cdot \left| \begin{array}{c c} - 2 & - 2 \\ 2 & x \end{array} \right| = 4 x - 8.</equation>由<equation>| A | = | B |</equation>可得<equation>4 x-8=-2 y</equation>即<equation>2 x+y=4.</equation>联立<equation>\left\{ \begin{array}{l l} x-y=5, \\ 2 x+y-4 \end{array} \right.</equation>解得 x=3,y=-2.

（Ⅱ）由于 A,B相似，故它们有相同的特征值.

计算 B的特征多项式.<equation>| \lambda E - B | = \left| \begin{array}{c c c} \lambda - 2 & - 1 & 0 \\ 0 & \lambda + 1 & 0 \\ 0 & 0 & \lambda + 2 \end{array} \right| = (\lambda - 2) (\lambda + 1) (\lambda + 2).</equation>于是，B的特征值为2，-1，-2.从而A的特征值也为2，-1，-2.

由于 A,B具有3个不同的特征值2，-1，-2，故存在可逆矩阵<equation>P_{1}, P_{2}</equation>，使得<equation>P_{1}^{-1} A P_{1}=</equation><equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -2 \end{array} \right), P_{2}^{-1} B P_{2}=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -2 \end{array} \right).</equation>令<equation>P=P_{1} P_{2}^{-1}</equation>，则<equation>P^{-1} A P=P_{2} P_{1}^{-1} A P_{1} P_{2}^{-1}=P_{2}\left(P_{1}^{-1} A P_{1}\right) P_{2}^{-1}=B.</equation><equation>P_{1}</equation>的列向量为A的属于特征值2，-1，-2的特征向量，<equation>P_{2}</equation>的列向量为B的属于特征值2，-1，-2的特征向量.下面分别计算A，B的特征向量.

计算 A的属于特征值2的特征向量.考虑（2E-A）x=0.<equation>2 E - A = \left( \begin{array}{c c c} 4 & 2 & - 1 \\ - 2 & - 1 & 2 \\ 0 & 0 & 4 \end{array} \right) \xrightarrow [ r _ {1} + r _ {3} ^ {*} ]{r _ {3} \times \frac {1}{4}} \left( \begin{array}{c c c} 4 & 2 & 0 \\ - 2 & - 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {2} ^ {*} \times (- 1) ]{r _ {1} ^ {*} + 2 r _ {2} ^ {*}} \left( \begin{array}{c c c} 0 & 0 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>于是，<equation>r ( 2 E-A)=2</equation>，求得<equation>\xi_{1}=(-1,2,0)^{\mathrm{T}}</equation>为（2E-A）x=0的一个基础解系.<equation>(-1,2,0)^{\mathrm{T}}</equation>为 A的属于特征值2的特征向量.

计算 A的属于特征值-1的特征向量.考虑<equation>(- E-A) x=0.</equation><equation>- E - A = \left( \begin{array}{c c c} 1 & 2 & - 1 \\ - 2 & - 4 & 2 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {1} + r _ {3} ]{r _ {2} + 2 r _ {1}} \left( \begin{array}{c c c} 1 & 2 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>于是，<equation>r(-E-A)=2</equation>，求得<equation>\xi_{2}=(-2,1,0)^{\mathrm{T}}</equation>为<equation>(-E-A)x=0</equation>的一个基础解系.<equation>(-2,1,0)^{\mathrm{T}}</equation>为 A的属于特征值-1的特征向量.

计算 A的属于特征值-2的特征向量.考虑<equation>(-2 E-A) x=0.</equation><equation>- 2 E - A = \left( \begin{array}{c c c} 0 & 2 & - 1 \\ - 2 & - 5 & 2 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {2} + 2 r _ {1}} \left( \begin{array}{c c c} 0 & 2 & - 1 \\ - 2 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {2} ^ {*} \times (- 2) - r _ {1}} \left( \begin{array}{c c c} 0 & 2 & - 1 \\ 4 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r(-2 E-A)=2</equation>，求得<equation>\xi_{3}=(-1,2,4)^{\mathrm{T}}</equation>为<equation>(-2 E-A) x=0</equation>的一个基础解系.<equation>(-1,2,4)^{\mathrm{T}}</equation>为 A的属于特征值-2的特征向量.

因此，<equation>P_{1}</equation>可取为<equation>\left( \begin{array}{c c c} - 1 & - 2 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right).</equation>计算 B的属于特征值2的特征向量.考虑（2E-B）x=0.<equation>2 E - B = \left( \begin{array}{c c c} 0 & - 1 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r ( 2 E-B)=2</equation>，求得<equation>\boldsymbol{\eta}_{1}=(1,0,0)^{\mathrm{T}}</equation>为（2E-B）<equation>\boldsymbol{x}=\mathbf{0}</equation>的一个基础解系. （1，0，0）<equation>^{\mathrm{T}}</equation>为B的属于特征值2的特征向量.

计算 B的属于特征值-1的特征向量.考虑<equation>(- E-B) x=0.</equation><equation>- \boldsymbol {E} - \boldsymbol {B} = \left( \begin{array}{c c c} - 3 & - 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {2} \leftrightarrow r _ {3} ]{r _ {1} \times (- 1)} \left( \begin{array}{c c c} 3 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r(-E-B)=2</equation>，求得<equation>\eta_{2}=(-1,3,0)^{\mathrm{T}}</equation>为<equation>(-E-B)x=0</equation>的一个基础解系.<equation>(-1,3,0)^{\mathrm{T}}</equation>为 B的属于特征值-1的特征向量.

计算 B的属于特征值-2的特征向量.考虑<equation>(-2 E-B) x=0.</equation><equation>- 2 E - B = \left( \begin{array}{c c c} - 4 & - 1 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {2} \times (- 1) ]{r _ {1} \times (- 1)} \left( \begin{array}{c c c} 4 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r(-2 E-B)=2</equation>，求得<equation>\boldsymbol{\eta}_{3}=(0,0,1)^{\mathrm{T}}</equation>为<equation>(-2 E-B) x=0</equation>的一个基础解系.<equation>(0,0,1)^{\mathrm{T}}</equation>为 B的属于特征值-2的特征向量.

因此，<equation>P_{2}</equation>可取为<equation>\left( \begin{array}{c c c} 1 & -1 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>利用初等变换法计算<equation>P_{2}^{-1}</equation><equation>\left(\boldsymbol {P} _ {2}, \boldsymbol {E}\right) = \left( \begin{array}{c c c c c c} 1 & - 1 & 0 & 1 & 0 & 0 \\ 0 & 3 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {1} + r _ {2} ^ {*} ]{r _ {2} \times \frac {1}{3}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 1 & \frac {1}{3} & 0 \\ 0 & 1 & 0 & 0 & \frac {1}{3} & 0 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right).</equation>于是，<equation>P_{2}^{-1}=\left( \begin{array}{c c c} 1 & \frac{1}{3} & 0 \\ 0 & \frac{1}{3} & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>综上所述，<equation>\boldsymbol {P} = \boldsymbol {P} _ {1} \boldsymbol {P} _ {2} ^ {- 1} = \left( \begin{array}{c c c} - 1 & - 2 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right) \left( \begin{array}{c c c} 1 & \frac {1}{3} & 0 \\ 0 & \frac {1}{3} & 0 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} - 1 & - 1 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right).</equation>

---

**2018年第7题 | 选择题 | 4分 | 答案: A**
7. 下列矩阵中，与矩阵<equation>\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>A.

相似的是（    ）<equation>\left( \begin{array}{c c c} 1 & 1 & - 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c} 1 & 1 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>
答案: A
**解析: **解已知矩阵与四个选项中的矩阵的特征多项式均为<equation>( x-1 )^{3}</equation>，故1为这五个矩阵的三重特征值记<equation>A=\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E-A=\left( \begin{array}{c c c} 0 & -1 & 0 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r ( E-A )=2.</equation>记<equation>B_{1}=\left( \begin{array}{c c c} 1 & 1 & -1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E-B_{1}=\left( \begin{array}{c c c} 0 & -1 & 1 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r \left( E-B_{1}\right)=2.</equation>记<equation>B_{2}=\left( \begin{array}{c c c} 1 & 0 & -1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E-B_{2}=\left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r \left( E-B_{2}\right) =1.</equation>记<equation>B_{3}=\left( \begin{array}{c c c} 1 & 1 & -1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E-B_{3}=\left( \begin{array}{c c c} 0 & -1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r \left( E-B_{3}\right)=1.</equation>记<equation>B_{4}=\left( \begin{array}{c c c} 1 & 0 & -1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E-B_{4}=\left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r \left( E-B_{4}\right)=1.</equation>由上可见，只有<equation>E-B_{1}</equation>与<equation>E-A</equation>的秩相等，而<equation>E-B_{i}(i=2,3,4)</equation>与<equation>E-A</equation>的秩均不相等，故<equation>E-B_{i}(i=2,3,4)</equation>与<equation>E-A</equation>不相似，从而A与<equation>B_{i}(i=2,3,4)</equation>不相似.

由排除法可知，应选A.

---

**2017年第8题 | 选择题 | 4分 | 答案: B**
8. 已知矩阵<equation>A = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 1 \end{array} \right), B = \left( \begin{array}{c c c} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right), C = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{array} \right),</equation>则（    ）

A. A与 C相似，B与 C相似 B. A与 C相似，B与 C不相似

C. A与 C不相似，B与 C相似 D. A与 C不相似，B与 C不相似
答案: B
**解析: **解分别计算 A,B,C的特征多项式，均为<equation>(\lambda-2)^{2}</equation><equation>(\lambda-1)</equation>，故 A,B,C具有相同的特征值，其中2是二重特征值.

矩阵 C是对角矩阵，故其相似于其自身.

考虑属于特征值2的特征向量.<equation>2 E - A = \left( \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 0 & - 1 \\ 0 & 0 & 1 \end{array} \right), \quad 2 E - B = \left( \begin{array}{c c c} 0 & - 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>由上可知，<equation>r ( 2 E-A )=1</equation><equation>r ( 2 E-B )=2</equation>.于是，<equation>( 2 E-A ) x=0</equation>的基础解系包含两个向量，A有2个线性无关的属于特征值2的特征向量；而<equation>( 2 E-B ) x=0</equation>的基础解系只包含一个向量，B只有1个线性无关的属于特征值2的特征向量.

因此，加上属于特征值1的特征向量，A共有3个线性无关的特征向量，A与C相似；B只有2个线性无关的特征向量，B与C不相似.应选B.

---

**2016年第7题 | 选择题 | 4分 | 答案: C**
7. 设 A,B是可逆矩阵，且 A与 B相似，则下列结论错误的是（    )

A.<equation>A^{\mathrm{T}}</equation>与<equation>B^{\mathrm{T}}</equation>相似 B.<equation>A^{-1}</equation>与<equation>B^{-1}</equation>相似

C.<equation>A+A^{\mathrm{T}}</equation>与<equation>B+B^{\mathrm{T}}</equation>相似 D.<equation>A+A^{-1}</equation>与<equation>B+B^{-1}</equation>相似
答案: C
**解析: **解 由于 A与B相似，故存在可逆矩阵 P，使得<equation>B=P^{-1} A P.</equation>-<equation>B^{\mathrm{T}}=P^{\mathrm{T}}A^{\mathrm{T}}(P^{-1})^{\mathrm{T}}=P^{\mathrm{T}}A^{\mathrm{T}}(P^{\mathrm{T}})^{-1}</equation>，选项A中的结论正确.

-<equation>B^{-1}=P^{-1} A^{-1} \left(P^{-1}\right)^{-1}=P^{-1} A^{-1} P</equation>，选项B中的结论正确.

- 由<equation>B=P^{-1} A P</equation>和<equation>B^{-1}=P^{-1} A^{-1} P</equation>可知，<equation>B+B^{-1}=P^{-1} \left(A+A^{-1}\right) P</equation>，选项D中的结论正确由排除法可知，应选C.

下面我们举例说明选项C不正确.

设<equation>A=\left( \begin{array}{c c}1&0\\ 0&-1 \end{array} \right), P=\left( \begin{array}{c c}1&1\\ 2&1 \end{array} \right),</equation>则<equation>P^{-1}=\left( \begin{array}{c c}-1&1\\ 2&-1 \end{array} \right).</equation>令<equation>\boldsymbol {B} = \boldsymbol {P} ^ {- 1} \boldsymbol {A P} = \left( \begin{array}{c c} - 1 & 1 \\ 2 & - 1 \end{array} \right) \left( \begin{array}{c c} 1 & 0 \\ 0 & - 1 \end{array} \right) \left( \begin{array}{c c} 1 & 1 \\ 2 & 1 \end{array} \right) = \left( \begin{array}{c c} - 3 & - 2 \\ 4 & 3 \end{array} \right),</equation>则<equation>\boldsymbol {A} + \boldsymbol {A} ^ {\mathrm {T}} = \left( \begin{array}{c c} 2 & 0 \\ 0 & - 2 \end{array} \right), \quad \boldsymbol {B} + \boldsymbol {B} ^ {\mathrm {T}} = \left( \begin{array}{c c} - 6 & 2 \\ 2 & 6 \end{array} \right).</equation>计算<equation>A+A^{\mathrm{T}}</equation>的特征多项式得<equation>\lambda^{2}-4</equation>，计算<equation>B+B^{\mathrm{T}}</equation>的特征多项式得<equation>\lambda^{2}-40.</equation>因此<equation>A+A^{\mathrm{T}}</equation>和<equation>B+B^{\mathrm{T}}</equation>不相似.

---

**2016年第23题 | 解答题 | 11分**
23. （本题满分11分）

已知矩阵<equation>A = \left( \begin{array}{c c c} 0 & -1 & 1 \\ 2 & -3 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>I. 求<equation>A^{99};</equation>II. 设3阶矩阵<equation>B=\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)</equation>满足<equation>B^{2}=B A</equation>记<equation>B^{100}=\left(\beta_{1},\beta_{2},\beta_{3}\right)</equation>将<equation>\beta_{1},\beta_{2},\beta_{3}</equation>分别表示为<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>的线性组合.
**答案: **（Ⅱ）<equation>\boldsymbol{\beta}_{1}=(2^{99}-2)\boldsymbol{\alpha}_{1}+(2^{100}-2)\boldsymbol{\alpha}_{2},\boldsymbol{\beta}_{2}=(1-2^{99})\boldsymbol{\alpha}_{1}+(1-2^{100})\boldsymbol{\alpha}_{2},\boldsymbol{\beta}_{3}=(2-2^{98})\boldsymbol{\alpha}_{1}+</equation>（2-2<equation>^{99}</equation>）<equation>\boldsymbol{\alpha}_{2}.</equation>
**解析: **解（I）计算 A的特征多项式<equation>|\lambda E - A|.</equation><equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda & 1 & - 1 \\ - 2 & \lambda + 3 & 0 \\ 0 & 0 & \lambda \end{array} \right| \xlongequal {\text {按 第三 行 展开}} \lambda \left(\lambda^ {2} + 3 \lambda + 2\right) = \lambda (\lambda + 1) (\lambda + 2).</equation>因此，A有3个不同的特征值：-2，-1，0.

由于属于不同特征值的特征向量线性无关，故A有3个线性无关的特征向量，A相似于对角矩阵<equation>\left( \begin{array}{c c c} - 2 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>分别计算 A的属于特征值-2，-1，0的特征向量.

当<equation>\lambda=-2</equation>时，解<equation>(-2E-A)x=0</equation>.由于<equation>- 2 E - A = \left( \begin{array}{c c c} - 2 & 1 & - 1 \\ - 2 & 1 & 0 \\ 0 & 0 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} - 2 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right),</equation>故<equation>( 1, 2, 0 )^{\mathrm{T}}</equation>为 A的属于特征值-2的一个特征向量.

当<equation>\lambda=-1</equation>时，解<equation>(-E-A)x=0</equation>.由于<equation>- E - A = \left( \begin{array}{c c c} - 1 & 1 & - 1 \\ - 2 & 2 & 0 \\ 0 & 0 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right),</equation>故<equation>( 1,1,0 )^{\mathrm{T}}</equation>为 A的属于特征值-1的一个特征向量.

当<equation>\lambda=0</equation>时，解（0E-A）x=0.由于<equation>0 E - A = \left( \begin{array}{c c c} 0 & 1 & - 1 \\ - 2 & 3 & 0 \\ 0 & 0 & 0 \end{array} \right),</equation>故（3，2，2）<equation>^{\mathrm{T}}</equation>为 A的属于特征值0的一个特征向量.

令<equation>P=\left( \begin{array}{c c c} 1 & 1 & 3 \\ 2 & 1 & 2 \\ 0 & 0 & 2 \end{array} \right)</equation>，则<equation>P^{-1} A P=\left( \begin{array}{c c c} - 2 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>计算<equation>P^{-1}</equation>得，<equation>P^{-1}=\left( \begin{array}{c c c} - 1 & 1 & \frac{1}{2} \\ 2 & - 1 & - 2 \\ 0 & 0 & \frac{1}{2} \end{array} \right).</equation><equation>\begin{aligned} \boldsymbol {A} ^ {9 9} &= \boldsymbol {P} \left( \begin{array}{c c c} (- 2) ^ {9 9} & 0 & 0 \\ 0 & (- 1) ^ {9 9} & 0 \\ 0 & 0 & 0  \right) \boldsymbol {P} ^ {- 1} &= \left( \begin{array}{c c c} 1 & 1 & 3 \\ 2 & 1 & 2 \\ 0 & 0 & 2  \right) \left( \begin{array}{c c c} - 2 ^ {9 9} & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0  \right) \left( \begin{array}{c c c} - 1 & 1 & \frac {1}{2} \\ 2 & - 1 & - 2 \\ 0 & 0 & \frac {1}{2}  \right) \\ &= \left( \begin{array}{c c c} 2 ^ {9 9} - 2 & 1 - 2 ^ {9 9} & 2 - 2 ^ {9 8} \\ 2 ^ {1 0 0} - 2 & 1 - 2 ^ {1 0 0} & 2 - 2 ^ {9 9} \\ 0 & 0 & 0  \right). \end{aligned}</equation>（Ⅱ）先求<equation>B^{100}.</equation>由于<equation>B^{2}=BA</equation>，故<equation>\boldsymbol {B} ^ {3} = \boldsymbol {B} \left(\boldsymbol {B} ^ {2}\right) = \boldsymbol {B} (\boldsymbol {B} \boldsymbol {A}) = \boldsymbol {B} ^ {2} \boldsymbol {A} = (\boldsymbol {B} \boldsymbol {A}) \boldsymbol {A} = \boldsymbol {B} \boldsymbol {A} ^ {2}.</equation>下面我们用数学归纳法证明<equation>B^{n}=B A^{n-1}, n=2, 3, \dots</equation>当 n = 2时，<equation>B^{2}=BA.</equation>假设该命题对 n = k 成立，下面证明该命题对 n = k +1 也成立.<equation>\boldsymbol {B} ^ {n} = \boldsymbol {B} ^ {k + 1} = \boldsymbol {B} \boldsymbol {B} ^ {k} \xlongequal {\text {归 纳 假 设}} \boldsymbol {B} \left(\boldsymbol {B} \boldsymbol {A} ^ {k - 1}\right) = \boldsymbol {B} ^ {2} \boldsymbol {A} ^ {k - 1} = (\boldsymbol {B} \boldsymbol {A}) \boldsymbol {A} ^ {k - 1} = \boldsymbol {B} \boldsymbol {A} ^ {k} = \boldsymbol {B} \boldsymbol {A} ^ {n - 1}.</equation>于是，该命题对 n=k+1也成立，从而由数学归纳法可知，该命题对所有<equation>\geqslant2</equation>的正整数均成立因此，<equation>\left(\boldsymbol {\beta} _ {1}, \boldsymbol {\beta} _ {2}, \boldsymbol {\beta} _ {3}\right) = \boldsymbol {B} ^ {1 0 0} = \boldsymbol {B A} ^ {9 9} = \left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\alpha} _ {2}, \boldsymbol {\alpha} _ {3}\right) \left( \begin{array}{c c c} 2 ^ {9 9} - 2 & 1 - 2 ^ {9 9} & 2 - 2 ^ {9 8} \\ 2 ^ {1 0 0} - 2 & 1 - 2 ^ {1 0 0} & 2 - 2 ^ {9 9} \\ 0 & 0 & 0 \end{array} \right).</equation>综上所述，<equation>\begin{aligned} \boldsymbol {\beta} _ {1} &= \left(2 ^ {9 9} - 2\right) \boldsymbol {\alpha} _ {1} + \left(2 ^ {1 0 0} - 2\right) \boldsymbol {\alpha} _ {2}, \\ \boldsymbol {\beta} _ {2} &= \left(1 - 2 ^ {9 9}\right) \boldsymbol {\alpha} _ {1} + \left(1 - 2 ^ {1 0 0}\right) \boldsymbol {\alpha} _ {2}, \\ \boldsymbol {\beta} _ {3} &= \left(2 - 2 ^ {9 8}\right) \boldsymbol {\alpha} _ {1} + \left(2 - 2 ^ {9 9}\right) \boldsymbol {\alpha} _ {2}. \end{aligned}</equation>

---

**2015年第23题 | 解答题 | 11分**
23. (本题满分11分)

设矩阵<equation>A = \left( \begin{array}{c c c} 0 & 2 & -3 \\ -1 & 3 & -3 \\ 1 & -2 & a \end{array} \right)</equation>相似于矩阵<equation>B = \left( \begin{array}{c c c} 1 & -2 & 0 \\ 0 & b & 0 \\ 0 & 3 & 1 \end{array} \right).</equation>I. 求 a,b的值；

II. 求可逆矩阵<equation>P</equation>，使<equation>P^{-1}AP</equation>为对角矩阵.
**答案: **(23) ( I ) a = 4, b = 5;<equation>(\mathrm {I I}) \boldsymbol {P} = \left( \begin{array}{c c c} - 1 & 2 & - 3 \\ - 1 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right), \boldsymbol {P} ^ {- 1} \boldsymbol {A} \boldsymbol {P} = \left( \begin{array}{c c c} 5 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>
**解析: **解（I）由于A,B相似，故存在可逆矩阵Q使得<equation>Q^{-1}AQ=B</equation>，从而<equation>|B|=|Q^{-1}|\cdot|A|\cdot|Q|=|A|.</equation>计算得<equation>|A|=2a-3, |B|=b.</equation>另一方面，A和B具有相同的迹，故<equation>3+a=2+b.</equation>联立得<equation>\left\{ \begin{array}{l l} a+3=b+2, \\ 2a-3=b, \end{array} \right.</equation>解得<equation>\left\{ \begin{array}{l l} a=4, \\ b=5. \end{array} \right.</equation>（Ⅱ）由题设和第（Ⅰ）问得，<equation>| \lambda E - B | = \left| \begin{array}{c c c} \lambda - 1 & 2 & 0 \\ 0 & \lambda - 5 & 0 \\ 0 & - 3 & \lambda - 1 \end{array} \right| = (\lambda - 1) ^ {2} (\lambda - 5).</equation>从而<equation>B</equation>的特征值为1，1，5.由于<equation>A</equation>和<equation>B</equation>相似，故<equation>A</equation>的特征值也为1，1，5.

由第（I）问可得，<equation>A = \left( \begin{array}{c c c} 0 & 2 & -3 \\ -1 & 3 & -3 \\ 1 & -2 & 4 \end{array} \right).</equation>考虑<equation>A</equation>的属于特征值5的特征向量.<equation>\begin{array}{l} 5 E - A = \left( \begin{array}{c c c} 5 & - 2 & 3 \\ 1 & 2 & 3 \\ - 1 & 2 & 1 \end{array} \right) \xrightarrow [ r _ {2} ^ {*} \times \frac {1}{2} ]{r _ {2} - r _ {3}} \left( \begin{array}{c c c} 5 & - 2 & 3 \\ 1 & 0 & 1 \\ - 1 & 2 & 1 \end{array} \right) \xrightarrow [ r _ {3} ^ {*} \times \frac {1}{2} ]{r _ {3} + r _ {2} ^ {* *}} \left( \begin{array}{c c c} 5 & - 2 & 3 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} - 5 r _ {2} ^ {* *} + 2 r _ {3} ^ {* *}} \left( \begin{array}{c c c} 0 & 0 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right). \\ \end{array}</equation>于是，<equation>r(5E - A) = 2</equation>，求得<equation>\xi_{1} = (-1, -1, 1)^{\mathrm{T}}</equation>为<equation>(5E - A)x = 0</equation>的一个基础解系.<equation>(-1, -1, 1)^{\mathrm{T}}</equation>为<equation>A</equation>的属于特征值5的特征向量.

考虑<equation>A</equation>的属于特征值1的特征向量.<equation>\boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} 1 & - 2 & 3 \\ 1 & - 2 & 3 \\ - 1 & 2 & - 3 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & - 2 & 3 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r ( E - A ) = 1</equation>，求得<equation>\boldsymbol{\xi}_{2} = ( 2,1,0 )^{\mathrm{T}}</equation>和<equation>\boldsymbol{\xi}_{3} = (-3,0,1)^{\mathrm{T}}</equation>为<equation>( E - A ) x = 0</equation>的一个基础解系<equation>( 2,1,0 )^{\mathrm{T}}</equation>和<equation>(-3,0,1)^{\mathrm{T}}</equation>为 A的属于特征值1的两个线性无关的特征向量.

取<equation>P = \left( \begin{array}{c c c} - 1 & 2 & - 3 \\ - 1 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right)</equation>，则<equation>P^{-1}AP = \left( \begin{array}{c c c} 5 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>.

---

**2014年第23题 | 解答题 | 11分**
23. (本题满分11分)

证明 n阶矩阵

相似.
**答案: **## （23）证明略.
**解析: **证（法一）记<equation>A=\left( \begin{array}{c c c c} 1 & 1 & \dots & 1 \\ 1 & 1 & \dots & 1 \\ \vdots & \vdots & & \vdots \\ 1 & 1 & \dots & 1 \end{array} \right), B=\left( \begin{array}{c c c c} 0 & \dots & 0 & 1 \\ 0 & \dots & 0 & 2 \\ \vdots & & \vdots & \vdots \\ 0 & \dots & 0 & n \end{array} \right).</equation>由观察可知，<equation>r ( \mathbf{A} )=1</equation>，<equation>\operatorname{t r} ( \mathbf{A} )=n</equation>. 又由于A为实对称矩阵，故必相似于对角矩阵.由相似的矩阵具有相同的秩和迹可知，A相似于秩为1，迹为 n的对角矩阵，不妨记为<equation>\left( \begin{array}{c c c c} n & & & \\ & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right).</equation>另一方面，计算<equation>B</equation>的特征多项式得，<equation>| \lambda E - B | = \left| \begin{array}{c c c c} \lambda & 0 & \dots & - 1 \\ 0 & \lambda & \dots & - 2 \\ \vdots & \vdots & & \vdots \\ 0 & 0 & \dots & \lambda - n \end{array} \right| = \lambda^ {n - 1} (\lambda - n).</equation>B的特征值为<equation>n,0,\dots ,0</equation>，其中0为<equation>n - 1</equation>重特征值.

由于<equation>0E - B = \left( \begin{array}{c c c} 0 & & -1 \\ & 0 & -2 \\ & \ddots & \vdots \\ & & -n \end{array} \right)</equation>，故<equation>r(0E - B) = 1</equation>，从而<equation>(0E - B)x = 0</equation>的解集的秩为<equation>n - 1</equation><equation>0E - B)x = 0</equation>有<equation>n - 1</equation>个线性无关的解.

B有 n-1个属于特征值0的线性无关的特征向量，再加上B的属于n的特征向量，B共有n个线性无关的特征向量. 从而B也相似于<equation>\left( \begin{array}{c c c c} n & & & \\ & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right).</equation>因此，存在可逆矩阵 P，Q，使得<equation>P^{-1} A P=Q^{-1} B Q=\left( \begin{array}{c c c c} n & & & \\ & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right)</equation>，于是<equation>Q P^{-1} A P Q^{-1}=B.</equation>令 U = PQ<equation>^{-1}</equation>，则 B = U<equation>^{-1}</equation>AU，A和B相似.

（法二）计算 A的特征多项式.<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c c} \lambda - 1 & - 1 & \dots & - 1 \\ - 1 & \lambda - 1 & \dots & - 1 \\ \vdots & \vdots & & \vdots \\ - 1 & - 1 & \dots & \lambda - 1  \right| \frac {c _ {1} + \left(c _ {2} + c _ {3} + \dots + c _ {n}\right)}{\hline} \left| \begin{array}{c c c c} \lambda - n & - 1 & \dots & - 1 \\ \lambda - n & \lambda - 1 & \dots & - 1 \\ \vdots & \vdots & & \vdots \\ \lambda - n & - 1 & \dots & \lambda - 1  \right| \\ &= (\lambda - n) \left| \begin{array}{c c c c} 1 & - 1 & \dots & - 1 \\ 1 & \lambda - 1 & \dots & - 1 \\ \vdots & \vdots & & \vdots \\ 1 & - 1 & \dots & \lambda - 1  \right| \frac {c _ {i} + c _ {1}}{i = 2 , \dots , n} (\lambda - n) \left| \begin{array}{c c c c} 1 & 0 & \dots & 0 \\ 1 & \lambda & \dots & 0 \\ \vdots & \vdots & & \vdots \\ 1 & 0 & \dots & \lambda  \right| \\ &= \lambda^ {n - 1} (\lambda - n). \end{aligned}</equation>由于 A为实对称矩阵，故由 A的特征多项式为<equation>\lambda^{n-1} (\lambda-n)</equation>可知 A相似于对角矩阵<equation>= \left( \begin{array}{c c c c} n & & & \\ & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right).</equation>其全同法一

---

**2013年第8题 | 选择题 | 4分 | 答案: B**
8. 矩阵

相似的充分必要条件为（    ）

A. a=0,b=2 B. a=0,b为任意常数 C. a=2,b=0 D. a=2,b为任意常数
答案: B
**解析: **解 矩阵<equation>\left( \begin{array}{lll}1&a&1\\ a&b&a\\ 1&a&1 \end{array} \right)</equation>与<equation>\left( \begin{array}{lll}2&0&0\\ 0&b&0\\ 0&0&0 \end{array} \right)</equation>均为实对称矩阵，故它们相似等价于它们有相同的特征多项式.

项式.

矩阵<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>的特征多项式为<equation>f (\lambda) = \lambda (\lambda - 2) (\lambda - b).</equation>考虑<equation>A = \left( \begin{array}{c c c} 1 & a & 1 \\ a & b & a \\ 1 & a & 1 \end{array} \right)</equation>的特征多项式<equation>g(\lambda)</equation>.<equation>g (\lambda) = | \lambda E - A | = \left| \begin{array}{c c c} \lambda - 1 & - a & - 1 \\ - a & \lambda - b & - a \\ - 1 & - a & \lambda - 1 \end{array} \right| = \lambda \left[ (\lambda - 2) (\lambda - b) - 2 a ^ {2} \right].</equation>由于<equation>f(\lambda)-g(\lambda)=2 a^{2}\lambda</equation>，故<equation>f(\lambda)=g(\lambda)</equation>当且仅当 a=0.由于上述论证不涉及到b，故b取任意常数均不影响结果.应选B.

---

**2010年第8题 | 选择题 | 4分 | 答案: D**
8. 设 A为4阶实对称矩阵，则<equation>A^{2}+A=O</equation>. 若 A的秩为3，则 A相似于（    ）

A.<equation>\left( \begin{array}{c c c c} 1 & & \\ & 1 & \\ & & 1 \\ & & 0 \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c c} 1 & & \\ & 1 & \\ & & - 1 \\ & & 0 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c c} 1 & & \\ & - 1 & \\ & & - 1 \\ & & 0 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c c} - 1 & & \\ & - 1 & \\ & & - 1 \\ & & 0 \end{array} \right)</equation>
答案: D
**解析: **解（法一）不妨设<equation>\lambda</equation>为 A的特征值，<equation>\alpha</equation>为其相应的特征向量.由<equation>A^{2}+A=O</equation>得<equation>(A^{2}+A)\alpha=0.</equation>代入<equation>A\alpha=\lambda\alpha</equation>得，<equation>(\lambda^{2}+\lambda)\alpha=0.</equation>又由于<equation>\alpha</equation>非零，故<equation>\lambda^{2}+\lambda=0,\lambda=0</equation>或<equation>\lambda=-1.</equation>由于 A为实对称矩阵，故 A相似于对角矩阵.又因为<equation>r ( A )=3</equation>，所以对角矩阵的秩也为3，<equation>\lambda=-1</equation>是 A的三重特征值， A相似于<equation>\left( \begin{array}{c c c c} - 1 & & & \\ & - 1 & & \\ & & - 1 & \\ & & & 0 \end{array} \right)</equation>.应选 D.

（法二）由于 A为实对称矩阵，故存在可逆矩阵 P使得<equation>P^{-1} A P=\left( \begin{array}{c c c c} \lambda_{1} & & & \\ & \lambda_{2} & & \\ & & \lambda_{3} & \\ & & & \lambda_{4} \end{array} \right).</equation>从而<equation>\begin{aligned} \boldsymbol {O} &= \boldsymbol {A} ^ {2} + \boldsymbol {A} = \boldsymbol {P} \left( \begin{array}{c c c c} \lambda_ {1} ^ {2} & & & \\ & \lambda_ {2} ^ {2} & & \\ & & \lambda_ {3} ^ {2} & \\ & & & \lambda_ {4} ^ {2}  \right) \boldsymbol {P} ^ {- 1} + \boldsymbol {P} \left( \begin{array}{c c c c} \lambda_ {1} & & & \\ & \lambda_ {2} & & \\ & & \lambda_ {3} & \\ & & & \lambda_ {4}  \right) \boldsymbol {P} ^ {- 1} \\ &= \boldsymbol {P} \left( \begin{array}{c c c c} \lambda_ {1} ^ {2} + \lambda_ {1} & & & \\ & \lambda_ {2} ^ {2} + \lambda_ {2} & & \\ & & \lambda_ {3} ^ {2} + \lambda_ {3} & \\ & & & \lambda_ {4} ^ {2} + \lambda_ {4}  \right) \boldsymbol {P} ^ {- 1}. \end{aligned}</equation>因此<equation>\lambda_{i}^{2}+\lambda_{i}=0 ( i=1,2,3,4).</equation>解得<equation>\lambda_{i}=0</equation>或<equation>\lambda_{i}=-1 ( i=1,2,3,4).</equation>又由于<equation>r ( A )=3</equation>，故 A相似于<equation>\left( \begin{array}{c c c c} - 1 & & & \\ & - 1 & & \\ & & - 1 & \\ & & & 0 \end{array} \right).</equation>应选D.

---

**2009年第14题 | 填空题 | 4分**
14. 设<equation>\alpha, \beta</equation>为3维列向量，<equation>\beta^{\mathrm{T}}</equation>为<equation>\beta</equation>的转置. 若矩阵<equation>\alpha\beta^{\mathrm{T}}</equation>相似于<equation>\left( \begin{array}{c c c} {2} & {0} & {0} \\ {0} & {0} & {0} \\ {0} & {0} & {0} \end{array} \right)</equation>，则<equation>\beta^{\mathrm{T}}\alpha=</equation>___
**解析: **解设<equation>\pmb{\alpha} = (a_{1}, a_{2}, a_{3})^{\mathrm{T}},\pmb {\beta} = (b_{1}, b_{2}, b_{3})^{\mathrm{T}}</equation>，则<equation>\begin{aligned} \boldsymbol {\alpha} \boldsymbol {\beta} ^ {\mathrm {T}} &= \left(  a _ {1} \\ a _ {2} \\ a _ {3}  \right) \left(b _ {1}, b _ {2}, b _ {3}\right) &= \left( \begin{array}{l l l} a _ {1} b _ {1} & a _ {1} b _ {2} & a _ {1} b _ {3} \\ a _ {2} b _ {1} & a _ {2} b _ {2} & a _ {2} b _ {3} \\ a _ {3} b _ {1} & a _ {3} b _ {2} & a _ {3} b _ {3}  \right), \end{aligned}</equation><equation>\begin{aligned} \boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {\alpha} &= \left(b _ {1}, b _ {2}, b _ {3}\right) \left(  a _ {1} \\ a _ {2} \\ a _ {3}  \right) &= a _ {1} b _ {1} + a _ {2} b _ {2} + a _ {3} b _ {3} = \operatorname {t r} \left(\boldsymbol {\alpha} \boldsymbol {\beta} ^ {\mathrm {T}}\right). \end{aligned}</equation>由于<equation>\alpha \beta^{\mathrm{T}}</equation>相似于<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>，故<equation>\operatorname{tr}(\alpha \beta^{\mathrm{T}}) = \operatorname{tr}(\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)) = 2.</equation>因此，<equation>\beta^{\mathrm{T}}\alpha = 2.</equation>

---


### 矩阵


#### 矩阵的运算与变换

**2025年第9题 | 选择题 | 5分 | 答案: B**
9. 下列矩阵中，可以经过若干初等行变换得到矩阵<equation>\left( \begin{array}{c c c c} 1 & 1 & 0 & 1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{array} \right)</equation>的是（    ）

A.

B.<equation>\left( \begin{array}{c c c c} 1 & 1 & 0 & 1 \\ 1 & 2 & 1 & 3 \\ 2 & 3 & 1 & 4 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c c} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 3 \\ 0 & 0 & 0 & 0 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c c} 1 & 1 & 2 & 3 \\ 1 & 2 & 2 & 3 \\ 2 & 3 & 4 & 6 \end{array} \right)</equation>
答案: B
**解析: **解（法一）由于对矩阵做初等行变换不改变矩阵的列向量组的线性相关性，且注意到矩阵<equation>\left( \begin{array}{c c c c} 1 & 1 & 0 & 1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{array} \right)</equation>的第一列与第二列线性相关，而除了选项B中<equation>\left( \begin{array}{c c c c} 1 & 1 & 0 & 1 \\ 1 & 1 & 2 & 5 \\ 1 & 1 & 1 & 3 \end{array} \right)</equation>的第一列与第二列线性相关外，其余选项的第一列与第二列均线性无关，故可以排除选项A、C、D.

由排除法可知，应选B.

（法二）依次分析各选项.<equation>\left( \begin{array}{c c c c} 1 & 1 & 0 & 1 \\ 1 & 2 & 1 & 3 \\ 2 & 3 & 1 & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & 0 & 1 \\ 0 & 1 & 1 & 2 \\ 0 & 1 & 1 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & 0 & 1 \\ 0 & 1 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{array} \right).</equation>对选项A，

由此可得，选项A不正确.

对选项B，<equation>\left( \begin{array}{c c c c} 1 & 1 & 0 & 1 \\ 1 & 1 & 2 & 5 \\ 1 & 1 & 1 & 3 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & 0 & 1 \\ 0 & 0 & 2 & 4 \\ 0 & 0 & 1 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & 0 & 1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{array} \right).</equation>由此可得，选项B正确.

注意到选项C的矩阵<equation>\left( \begin{array}{c c c c} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 3 \\ 0 & 1 & 0 & 0 \end{array} \right)</equation>有3阶非零子式<equation>\left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 1 & 0 \end{array} \right)</equation>，故该矩阵的秩为3，不可能与矩阵<equation>\left( \begin{array}{c c c c} 1 & 1 & 0 & 1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{array} \right)</equation>行等价.由此可得，选项C不正确.

对选项D，<equation>\left( \begin{array}{c c c c} 1 & 1 & 2 & 3 \\ 1 & 2 & 2 & 3 \\ 2 & 3 & 4 & 6 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & 2 & 3 \\ 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 0 & 2 & 3 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{array} \right).</equation>由此可得，选项D不正确.

因此，应选B.

---

**2024年第8题 | 选择题 | 5分 | 答案: C**
8. 设 A为3阶矩阵，<equation>P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right)</equation>，若<equation>P^{\mathrm{T}} A P^{2}=\left( \begin{array}{c c c} a+2 c & 0 & c \\ 0 & b & 0 \\ 2 c & 0 & c \end{array} \right)</equation>，则 A=（    )

A.<equation>\left( \begin{array}{c c c} c & 0 & 0 \\ 0 & a & 0 \\ 0 & 0 & b \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c} b & 0 & 0 \\ 0 & c & 0 \\ 0 & 0 & a \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c} a & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & c \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} c & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & a \end{array} \right)</equation>
答案: C
**解析: **解 由于<equation>P = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right)</equation>，故<equation>\boldsymbol {P} ^ {- 1} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ - 1 & 0 & 1 \end{array} \right), \quad \boldsymbol {P} ^ {\mathrm {T}} = \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right), \quad \left(\boldsymbol {P} ^ {\mathrm {T}}\right) ^ {- 1} = \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>进一步可得，<equation>\begin{aligned} \boldsymbol {A} &= \left(\boldsymbol {P} ^ {\mathrm {T}}\right) ^ {- 1} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} ^ {2} \left(\boldsymbol {P} ^ {2}\right) ^ {- 1} = \left(\boldsymbol {P} ^ {\mathrm {T}}\right) ^ {- 1} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} ^ {2} \left(\boldsymbol {P} ^ {- 1}\right) ^ {2} \\ &= \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1  \right) \left( \begin{array}{c c c} a + 2 c & 0 & c \\ 0 & b & 0 \\ 2 c & 0 & c  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ - 1 & 0 & 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ - 1 & 0 & 1  \right) \\ &= \left( \begin{array}{c c c} a & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & c  \right). \end{aligned}</equation>因此，应选C.

---

**2022年第16题 | 填空题 | 5分**
16. 设 A为3阶矩阵，交换 A的第2行和第3行，再将第2列的-1倍加到第1列，得到矩阵<equation>A^{-1}</equation>的迹<equation>\operatorname{tr}\left(A^{-1}\right)=</equation>___
**答案: **-1.
**解析: **解 交换第2行和第3行对应左乘初等矩阵<equation>P_{1}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{array} \right)</equation>，将第2列的-1倍加到第1列对应右乘初等矩阵<equation>P_{2}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>.记<equation>B=\left( \begin{array}{c c c} -2 & 1 & -1 \\ 1 & -1 & 0 \\ -1 & 0 & 0 \end{array} \right)</equation>.于是，<equation>P_{1}AP_{2}=B</equation>，从而<equation>A= P_{1}^{-1}BP_{2}^{-1}</equation>.由此可得，<equation>A^{-1}=P_{2}B^{-1}P_{1}.</equation>下面利用初等行变换计算<equation>B^{-1}.</equation><equation>\begin{array}{l} (\boldsymbol {B}, \boldsymbol {E}) = \left( \begin{array}{c c c c c c} - 2 & 1 & - 1 & 1 & 0 & 0 \\ 1 & - 1 & 0 & 0 & 1 & 0 \\ - 1 & 0 & 0 & 0 & 0 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 0 & 0 & - 1 \\ 1 & - 1 & 0 & 0 & 1 & 0 \\ - 2 & 1 & - 1 & 1 & 0 & 0 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 0 & 0 & - 1 \\ 0 & - 1 & 0 & 0 & 1 & 1 \\ 0 & 1 & - 1 & 1 & 0 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 0 & 0 & - 1 \\ 0 & - 1 & 0 & 0 & 1 & 1 \\ 0 & 0 & - 1 & 1 & 1 & - 1 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 0 & 0 & - 1 \\ 0 & 1 & 0 & 0 & - 1 & - 1 \\ 0 & 0 & 1 & - 1 & - 1 & 1 \end{array} \right). \\ \end{array}</equation>于是，<equation>B^{-1}=\left( \begin{array}{c c c} 0 & 0 & -1 \\ 0 & -1 & -1 \\ -1 & -1 & 1 \end{array} \right).</equation>因此，<equation>\boldsymbol {A} ^ {- 1} = \boldsymbol {P} _ {2} \boldsymbol {B} ^ {- 1} \boldsymbol {P} _ {1} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \left( \begin{array}{c c c} 0 & 0 & - 1 \\ 0 & - 1 & - 1 \\ - 1 & - 1 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{array} \right) = \left( \begin{array}{c c c} 0 & - 1 & 0 \\ 0 & 0 & - 1 \\ - 1 & 1 & - 1 \end{array} \right).</equation>进一步可得<equation>\operatorname{tr}(A^{-1}) = -1.</equation>

---

**2021年第10题 | 选择题 | 5分 | 答案: C**
10. 已知矩阵<equation>A=\left( \begin{array}{c c c}1&0&-1\\ 2&-1&1\\ -1&2&-5 \end{array} \right)</equation>，若存在下三角可逆矩阵 P与上三角可逆矩阵 Q，使得 PAQ为对角矩阵，则

P和Q分别为（    ）

A.<equation>\begin{array}{l} \left. \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right), \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right) \right. \\ \left(\left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right), \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right) \right. \\ \end{array}</equation>B.

C.<equation>\begin{array}{l} \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right), \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \\ \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 3 & 1 \end{array} \right), \left( \begin{array}{c c c} 1 & 2 & - 3 \\ 0 & - 1 & 2 \\ 0 & 0 & 1 \end{array} \right) \\ \end{array}</equation>D.
答案: C
**解析: **解（法一）对（A，E）作初等行变换.<equation>\begin{array}{l} (A, E) = \left( \begin{array}{c c c c c c} 1 & 0 & - 1 & 1 & 0 & 0 \\ 2 & - 1 & 1 & 0 & 1 & 0 \\ - 1 & 2 & - 5 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {2} - 2 r _ {1}} \left( \begin{array}{c c c c c c} 1 & 0 & - 1 & 1 & 0 & 0 \\ 0 & - 1 & 3 & - 2 & 1 & 0 \\ 0 & 2 & - 6 & 1 & 0 & 1 \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} \times (- 1)} \left( \begin{array}{c c c c c c} 1 & 0 & - 1 & 1 & 0 & 0 \\ 0 & 1 & - 3 & 2 & - 1 & 0 \\ 0 & 2 & - 6 & 1 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} ^ {*} - 2 r _ {2} ^ {* *}} \left( \begin{array}{c c c c c c} 1 & 0 & - 1 & 1 & 0 & 0 \\ 0 & 1 & - 3 & 2 & - 1 & 0 \\ 0 & 0 & 0 & - 3 & 2 & 1 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个 *.）

取<equation>P = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & -1 & 0 \\ -3 & 2 & 1 \end{array} \right).</equation>记<equation>U=\left( \begin{array}{c c c}1&0&-1\\ 0&1&-3\\ 0&0&0 \end{array} \right)</equation>，对<equation>\binom{U}{E}</equation>作初等列变换.<equation>\binom {U} {E} = \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & - 3 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow {c _ {3} + c _ {1} + 3 c _ {2}} \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right).</equation>取<equation>Q = \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right).</equation>此时，PAQ =<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>为对角矩阵.因此，应选C.

（法二）代人法.

观察选项A、B发现，其中各有一个单位矩阵。

由于左乘矩阵相当于对原矩阵作行变换，右乘矩阵相当于对原矩阵作列变换，故<equation>\boldsymbol {A} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 2 & - 1 & 1 \\ - 1 & 2 & - 5 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right)</equation>的第一列为 A的第一列，即<equation>\left( \begin{array}{c c c} 1 \\ 2 \\ - 1 \end{array} \right),</equation><equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right) A = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 2 & - 1 & 1 \\ - 1 & 2 & - 5 \end{array} \right)</equation>的第一行为 A的第一行，即（1，0，-1），而任何矩阵与单位矩阵相乘所得结果均为原矩阵，于是选项A、B所给 P，Q均不能使得 PAQ为对角矩阵。由此可排除选项A、B.

将选项C中的两个矩阵代入计算，可得<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 2 & - 1 & 1 \\ - 1 & 2 & - 5 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 1 & 2 & 0 \end{array} \right) = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>由此可见选项C正确. 应选C.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 3 & 1 \end{array} \right) A</equation>的第一行、第二行与A的第一行、第二行相同，即<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 3 & 1 \end{array} \right) A=\left( \begin{array}{c c c} 1 & 0 & -1 \\ 2 & -1 & 1 \\ * & * & * \end{array} \right),</equation>记为B.B再右乘<equation>\left( \begin{array}{c c c} 1 & 2 & -3 \\ 0 & -1 & 2 \\ 0 & 0 & 1 \end{array} \right),</equation>则新矩阵的第一列为<equation>\left( \begin{array}{c} 1 \\ 2 \\ * \end{array} \right).</equation>于是，所得结果不是对角矩阵.

---

**2015年第22题 | 解答题 | 11分**
22. (本题满分11分)

设矩阵<equation>A=\left( \begin{array}{c c c} a & 1 & 0 \\ 1 & a & -1 \\ 0 & 1 & a \end{array} \right)</equation>，且<equation>A^{3}=O.</equation>I. 求 a的值；

II. 若矩阵<equation>X</equation>满足<equation>X - XA^{2} - AX + AXA^{2} = E</equation>，其中<equation>E</equation>为3阶单位矩阵，求<equation>X</equation>
**答案: **(22) （I）<equation>a=0;</equation><equation>(\mathrm {I I}) X = \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1 \end{array} \right)</equation>
**解析: **解（I）（法一）由<equation>A^{3}=O</equation>知<equation>|A^{3}|=0.</equation>又因为<equation>|A^{3}|=|A|^{3},</equation>所以<equation>|A|=0.</equation>由题设可计算得<equation>|A|=a^{3},</equation>从而<equation>a^{3}=0, a=0.</equation>（法二）设<equation>\lambda</equation>为<equation>A</equation>的一个特征值，则由<equation>A^{3}=O</equation>可知<equation>\lambda^{3}=0</equation>.于是，<equation>A</equation>的特征值均为零。由矩阵的迹等于其特征值之和，可知<equation>\operatorname{tr}(A)=3 a=0</equation>即<equation>a=0.</equation>（Ⅱ）由第（I）问知，<equation>A=\left( \begin{array}{c c c} 0 & 1 & 0 \\ 1 & 0 & -1 \\ 0 & 1 & 0 \end{array} \right).</equation>由<equation>X - X A^{2} - A X + A X A^{2} = E</equation>可得，<equation>X \left(E - A ^ {2}\right) - A X \left(E - A ^ {2}\right) = E.</equation>化简得（E-A）X（E-A²）=E.

由此可知，<equation>E - A, E - A^{2}</equation>均为可逆矩阵，且<equation>\boldsymbol {X} = \left(\boldsymbol {E} - \boldsymbol {A}\right) ^ {- 1} \left(\boldsymbol {E} - \boldsymbol {A} ^ {2}\right) ^ {- 1}.</equation>下面用三种方法计算 X.

（法一）由<equation>(AB)^{-1} = B^{-1}A^{-1}</equation>得，<equation>X = \left(E - A\right) ^ {- 1} \left(E - A ^ {2}\right) ^ {- 1} = \left[ \left(E - A ^ {2}\right) \left(E - A\right) \right] ^ {- 1} \xlongequal {A ^ {3} = O} \left(E - A - A ^ {2}\right) ^ {- 1}.</equation>计算得<equation>A^{2} = \left( \begin{array}{c c c} 1 & 0 & -1 \\ 0 & 0 & 0 \\ 1 & 0 & -1 \end{array} \right)</equation>，故<equation>E - A - A^{2} = \left( \begin{array}{c c c} 0 & -1 & 1 \\ -1 & 1 & 1 \\ -1 & -1 & 2 \end{array} \right)</equation>，再计算得<equation>|E - A - A^{2}| = 1.</equation>因此，<equation>\boldsymbol {X} = \left(\boldsymbol {E} - \boldsymbol {A} - \boldsymbol {A} ^ {2}\right) ^ {- 1} = \left(\boldsymbol {E} - \boldsymbol {A} - \boldsymbol {A} ^ {2}\right) ^ {*} = \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1 \end{array} \right).</equation>或利用初等变换法计算 X.<equation>\begin{array}{l} \left(\boldsymbol {E} - \boldsymbol {A} - \boldsymbol {A} ^ {2}, \boldsymbol {E}\right) = \left( \begin{array}{c c c c c c} 0 & - 1 & 1 & 1 & 0 & 0 \\ - 1 & 1 & 1 & 0 & 1 & 0 \\ - 1 & - 1 & 2 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {2} + r _ {1}} \left( \begin{array}{c c c c c c} 0 & - 1 & 1 & 1 & 0 & 0 \\ - 1 & 0 & 2 & 1 & 1 & 0 \\ 0 & - 1 & 0 & - 1 & - 1 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} - r _ {3} ^ {*}} \binom {0} {r _ {2} ^ {*} - 2 r _ {1} ^ {*}} \rightarrow \binom {1} {0} \binom {0} {1} \binom {3} {0} \binom {1} {- 2} \\ \end{array}</equation>因此，<equation>\boldsymbol {X} = \left(\boldsymbol {E} - \boldsymbol {A} - \boldsymbol {A} ^ {2}\right) ^ {- 1} = \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1 \end{array} \right).</equation>（法二）由于<equation>A^{3} = O</equation>，故<equation>A^{4} = O</equation>，从而<equation>\left(E - A\right) \left(E + A + A ^ {2}\right) = E - A ^ {3} = E, \quad \left(E - A ^ {2}\right) \left(E + A ^ {2}\right) = E - A ^ {4} = E.</equation>于是，<equation>(E - A)^{-1} = E + A + A^{2},(E - A^{2})^{-1} = E + A^{2}</equation>因此，<equation>\begin{aligned} \boldsymbol {X} &= \left(\boldsymbol {E} - \boldsymbol {A}\right) ^ {- 1} \left(\boldsymbol {E} - \boldsymbol {A} ^ {2}\right) ^ {- 1} = \left(\boldsymbol {E} + \boldsymbol {A} + \boldsymbol {A} ^ {2}\right) \left(\boldsymbol {E} + \boldsymbol {A} ^ {2}\right) \stackrel {A ^ {3} = O} {=} \boldsymbol {E} + \boldsymbol {A} + 2 \boldsymbol {A} ^ {2} \\ &= \boldsymbol {E} + \left( \begin{array}{c c c} 0 & 1 & 0 \\ 1 & 0 & - 1 \\ 0 & 1 & 0  \right) + 2 \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 0 & 0 \\ 1 & 0 & - 1  \right) &= \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1  \right). \end{aligned}</equation>（法三）分别计算<equation>(E - A)^{-1}, (E - A^{2})^{-1}</equation>.<equation>\boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} 1 & - 1 & 0 \\ - 1 & 1 & 1 \\ 0 & - 1 & 1 \end{array} \right), \quad \boldsymbol {E} - \boldsymbol {A} ^ {2} = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 1 & 0 \\ - 1 & 0 & 2 \end{array} \right).</equation>利用初等变换法计算<equation>(E - A)^{-1}, (E - A^{2})^{-1}</equation>.<equation>\begin{array}{l} (E - A, E) = \left( \begin{array}{c c c c c c} 1 & - 1 & 0 & 1 & 0 & 0 \\ - 1 & 1 & 1 & 0 & 1 & 0 \\ 0 & - 1 & 1 & 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {3} - r _ {2} ^ {*} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c c c} 1 & - 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 & 1 & 0 \\ 0 & - 1 & 0 & - 1 & - 1 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} - r _ {3} ^ {*}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 2 & 1 & - 1 \\ 0 & 0 & 1 & 1 & 1 & 0 \\ 0 & - 1 & 0 & - 1 & - 1 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 2 & 1 & - 1 \\ 0 & 1 & 0 & 1 & 1 & - 1 \\ 0 & 0 & 1 & 1 & 1 & 0 \end{array} \right), \\ \end{array}</equation><equation>\begin{array}{l} \left(\boldsymbol {E} - \boldsymbol {A} ^ {2}, \boldsymbol {E}\right) = \left( \begin{array}{c c c c c c} 0 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ - 1 & 0 & 2 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} - 2 r _ {1}} \left( \begin{array}{c c c c c c} 0 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ - 1 & 0 & 0 & - 2 & 0 & 1 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 2 & 0 & - 1 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 1 & 0 & 0 \end{array} \right). \\ \end{array}</equation>因此，<equation>\left(\boldsymbol {E} - \boldsymbol {A}\right) ^ {- 1} = \left( \begin{array}{c c c} 2 & 1 & - 1 \\ 1 & 1 & - 1 \\ 1 & 1 & 0 \end{array} \right), \quad \left(\boldsymbol {E} ^ {-} - \boldsymbol {A} ^ {2}\right) ^ {- 1} = \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{array} \right).</equation>综上所述，<equation>\boldsymbol {X} = \left(\boldsymbol {E} - \boldsymbol {A}\right) ^ {- 1} \left(\boldsymbol {E} - \boldsymbol {A} ^ {2}\right) ^ {- 1} = \left( \begin{array}{c c c} 2 & 1 & - 1 \\ 1 & 1 & - 1 \\ 1 & 1 & 0 \end{array} \right) \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{array} \right) = \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1 \end{array} \right).</equation>

---

**2012年第8题 | 选择题 | 4分 | 答案: B**
8. 设 A为3阶矩阵，P为3阶可逆矩阵，且<equation>P^{-1} A P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>若<equation>P=(\alpha_{1},\alpha_{2},\alpha_{3}), Q=(\alpha_{1}+\alpha_{2},\alpha_{2},\alpha_{3}),</equation>则<equation>Q^{-1} A Q=</equation>(    )

A.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>
答案: B
**解析: **解（法一）由题设知，<equation>Q=P\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，故<equation>Q^{-1}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) P^{-1}</equation>. 从而<equation>\begin{aligned} Q ^ {- 1} A Q &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 0 & 0 & 1  \right) P ^ {- 1} A P \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1  \right) \\ &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 0 & 0 & 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1  \right) &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2  \right). \end{aligned}</equation>应选B.

（法二）由题设知，1，1，2是A的特征值，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>分别是属于特征值1，1，2的特征向量，即<equation>A\alpha_{1}=\alpha_{1},</equation><equation>A\alpha_{2}=\alpha_{2},</equation><equation>A\alpha_{3}=2\alpha_{3}.</equation>从而<equation>A\left(\alpha_{1} + \alpha_{2}\right) = \alpha_{1} + \alpha_{2},\alpha_{1} + \alpha_{2}</equation>也是<equation>A</equation>的属于特征值1的特征向量.<equation>A Q = A \left(\alpha_ {1} + \alpha_ {2}, \alpha_ {2}, \alpha_ {3}\right) = \left(\alpha_ {1} + \alpha_ {2}, \alpha_ {2}, 2 \alpha_ {3}\right) = Q \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>又由于<equation>Q</equation>由<equation>P</equation>作初等变换得到，<equation>P</equation>可逆，故<equation>Q</equation>可逆.于是<equation>Q^{-1}AQ = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>.应选B.

---

**2011年第7题 | 选择题 | 4分 | 答案: D**
7. 设 A为3阶矩阵，将 A的第2列加到第1列得矩阵 B，再交换 B的第2行与第3行得单位矩阵.记<equation>P_{1}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right), P_{2}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{array} \right),</equation>则 A=（    )

A.<equation>P_{1} P_{2}</equation>B.<equation>P_{1}^{-1} P_{2}</equation>C.<equation>P_{2} P_{1}</equation>D.<equation>P_{2} P_{1}^{-1}</equation>
答案: D
**解析: **解 将 A的第2列加到第1列对应 A右乘矩阵<equation>P_{1}</equation>，得<equation>B=A P_{1}</equation>.交换 B的第2行与第3行对应 B左乘矩阵<equation>P_{2}</equation>，得<equation>E=P_{2} A P_{1}</equation>.于是<equation>A=P_{2}^{-1} P_{1}^{-1}.</equation>又因为<equation>P_{2}^{-1}=P_{2}</equation>，所以 A=P<equation>P_{2}^{-1}.</equation>应选 D.

---

**2010年第14题 | 填空题 | 4分**
14. 设<equation>A, B</equation>为3阶矩阵，且<equation>|A| = 3, |B| = 2, |A^{-1} + B| = 2</equation>，则<equation>|A + B^{-1}</equation>
**解析: **由于<equation>A, B</equation>的行列式均不为零，故它们均可逆.因为<equation>\boldsymbol {A} \left(\boldsymbol {A} ^ {- 1} + \boldsymbol {B}\right) \boldsymbol {B} ^ {- 1} = \boldsymbol {B} ^ {- 1} + \boldsymbol {A} = \boldsymbol {A} + \boldsymbol {B} ^ {- 1},</equation>所以<equation>| A + B ^ {- 1} | = | A | \cdot | A ^ {- 1} + B | \cdot | B ^ {- 1} | \frac {| B ^ {- 1} | = \frac {1}{| B |}}{\underline {{}}} 3 \times 2 \times \frac {1}{2} = 3.</equation>

---

**2009年第8题 | 选择题 | 4分**
8. 设<equation>A, P</equation>均为3阶矩阵，<equation>P^{\mathrm{T}}</equation>为<equation>P</equation>的转置矩阵，且<equation>P^{\mathrm{T}}AP = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>. 若<equation>P = \left(\alpha_{1}, \alpha_{2}, \alpha_{3}\right)</equation>，<equation>Q = \left(\alpha_{1} + \alpha_{2}, \alpha_{2}, \alpha_{3}\right)</equation>，

则<equation>Q^{\mathrm{T}} A Q</equation>为（    ）

A.<equation>\left( \begin{array}{c c c} 2 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>3.<equation>\left( \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>B.

C.<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>
**解析: **解 由题设知，<equation>Q</equation>为把<equation>P</equation>的第2列加到第1列的结果，故<equation>Q=P\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>.从<equation>\begin{aligned} Q ^ {\mathrm {T}} A Q &= \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1  \right) P ^ {\mathrm {T}} A P \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1  \right) &= \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1  \right) \\ &= \left( \begin{array}{c c c} 2 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 2  \right). \end{aligned}</equation>应选A.

---


#### 矩阵的秩

**2024年第9题 | 选择题 | 5分 | 答案: D**
9. 设 A为4阶矩阵，<equation>A^{*}</equation>为 A的伴随矩阵. 若<equation>A(A-A^{*})=O</equation>，且<equation>A\neq A^{*}</equation>，则 r(A)的取值为（

A.0或1 B.1或3 C.2或3 D.1或2
答案: D
**解析: **解由<equation>A(A - A^{*}) = O</equation>可得，<equation>r(A) + r(A - A^{*})\leqslant 4.</equation>结合<equation>A - A^{*}\neq O</equation>，从而<equation>r(A - A^{*})\geqslant</equation>1可得，<equation>r(A)\leqslant 3.</equation>于是，<equation>|A| = 0,AA^{*} = O.</equation>进一步由<equation>A(A - A^{*}) = O</equation>可得，<equation>A^{2} = O.</equation>由<equation>A^{2} = O</equation>可得，<equation>2r(A)\leqslant 4</equation>，即<equation>r(A)\leqslant 2</equation>.当<equation>r(A)\leqslant 2</equation>时，<equation>r(A^{*}) = 0</equation>，即<equation>A^{*} = O.</equation>由于<equation>A\neq A^{*}</equation>，故<equation>A\neq O</equation>，从而<equation>r(A)\geqslant 1.</equation>因此，<equation>r(\mathbf{A})</equation>的取值为1或2，应选D.

下面举例说明<equation>r(A) = 1</equation>与<equation>r(A) = 2</equation>均可能实现.

取<equation>A = \left( \begin{array}{cccc} 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{array} \right)</equation>，则<equation>r(A) = 1, A^{*} = O, A \neq A^{*}</equation>，且<equation>A^{2} = O.</equation>取<equation>A = \left( \begin{array}{cccc} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{array} \right)</equation>，则<equation>r(A) = 2, A^{*} = O, A \neq A^{*}</equation>，且<equation>A^{2} = O.</equation>

---

**2018年第8题 | 选择题 | 4分 | 答案: A**
8. 设 A,B为 n阶矩阵，记 r(X)为矩阵 X的秩，(X,Y)表示分块矩阵，则（    ）

A.<equation>r ( A, A B )=r ( A )</equation>B.<equation>r ( A, B A )=r ( A )</equation>C.<equation>r ( A, B )=\max \{ r ( A ) , r ( B ) \}</equation>D.<equation>r ( A, B )=r \left( A^{\mathrm{T}}, B^{\mathrm{T}} \right)</equation>
答案: A
**解析: **解记 C=AB.由于右乘矩阵表示对矩阵作列变换，故 C的列向量可由 A的列向量线性表示.于是，<equation>r ( A, C )=r ( A, A B )=r ( A ).</equation>因此，应选A.

下面分别说明选项B、C、D不正确.

选项B：<equation>r ( A, B A ) \geqslant r ( A )</equation>.但是，<equation>r ( A, B A ) = r ( A )</equation>并不成立.

取<equation>A=\left( \begin{array}{ll}1&0\\ 0&0 \end{array} \right), B=\left( \begin{array}{ll}1&0\\ 1&1 \end{array} \right)</equation>，则<equation>B A=\left( \begin{array}{ll}1&0\\ 1&0 \end{array} \right), (A, B A)=\left( \begin{array}{lll}1&0&1&0\\ 0&0&1&0 \end{array} \right). r(A, B A)=2</equation>，但<equation>r(A)=1.</equation>选项 C：<equation>r ( A, B ) \geqslant\max \left\{r ( A ) , r ( B ) \right\}</equation>.但是，<equation>r ( A, B )=\max \left\{r ( A ) , r ( B ) \right\}</equation>并不成立.

取<equation>A = \left( \begin{array}{ll}1 & 0\\ 0 & 0 \end{array} \right),B = \left( \begin{array}{ll}0 & 0\\ 1 & 0 \end{array} \right)</equation>，则<equation>(A,B) = \left( \begin{array}{lll}1 & 0 & 0 & 0\\ 0 & 0 & 1 & 0 \end{array} \right),r(A,B) = 2</equation>，但<equation>r(A) = r(B) = 1.</equation>选项D：由于<equation>r(\mathbf{P})=r(\mathbf{P}^{\mathrm{T}})</equation>，而<equation>(\mathbf{A},\mathbf{B})^{\mathrm{T}}=\binom{\mathbf{A}^{\mathrm{T}}}{\mathbf{B}^{\mathrm{T}}}</equation>，故<equation>r(\mathbf{A},\mathbf{B})=r\binom{\mathbf{A}^{\mathrm{T}}}{\mathbf{B}^{\mathrm{T}}}</equation>.但是，<equation>r(\mathbf{A},\mathbf{B})= r(\mathbf{A}^{\mathrm{T}},\mathbf{B}^{\mathrm{T}})</equation>并不成立.

取<equation>A=\left( \begin{array}{cc}1&0\\ 0&0 \end{array} \right), B=\left( \begin{array}{cc}0&0\\ 1&0 \end{array} \right)</equation>，则<equation>(\mathbf{A},\mathbf{B})=\left( \begin{array}{cccc}1&0&0&0\\ 0&0&1&0 \end{array} \right),(\mathbf{A}^{\mathrm{T}},\mathbf{B}^{\mathrm{T}})=\left( \begin{array}{cccc}1&0&0&1\\ 0&0&0&0 \end{array} \right). r(\mathbf{A},\mathbf{B})=2</equation>但<equation>r(\mathbf{A}^{\mathrm{T}},\mathbf{B}^{\mathrm{T}})=1.</equation>

---

**2016年第14题 | 填空题 | 4分**
14. 设矩阵<equation>\left( \begin{array}{c c c} a & - 1 & - 1 \\ - 1 & a & - 1 \\ - 1 & - 1 & a \end{array} \right)</equation>与矩阵<equation>\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & - 1 & 1 \\ 1 & 0 & 1 \end{array} \right)</equation>等价，则 a = ___
**解析: **解（法一）记<equation>A=\left( \begin{array}{c c c} a & -1 & -1 \\ -1 & a & -1 \\ -1 & -1 & a \end{array} \right), B=\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & -1 & 1 \\ 1 & 0 & 1 \end{array} \right).</equation><equation>\boldsymbol {B} = \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & - 1 & 1 \\ 1 & 0 & 1 \end{array} \right) \xrightarrow {r _ {1} + r _ {2}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & - 1 & 1 \\ 1 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} - r _ {1} ^ {*}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & - 1 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个 *.）于是<equation>r(B)=2.</equation>由于<equation>A, B</equation>等价，故<equation>r(A) = r(B) = 2</equation>，从而<equation>|A| = 0.</equation>另一方面，计算<equation>|A|</equation>得，<equation>| A | = \left| \begin{array}{c c c} a & - 1 & - 1 \\ - 1 & a & - 1 \\ - 1 & - 1 & a \end{array} \right| = (a + 1) ^ {2} (a - 2).</equation>| A | = 0当且仅当 a=-1或 a=2.当 a=-1时，<equation>r ( A )=1</equation>，不符合题意.因此， a=2. （法二）由法一知，<equation>r ( B )=2.</equation>对A作初等行变换，<equation>\boldsymbol {A} = \left( \begin{array}{c c c} a & - 1 & - 1 \\ - 1 & a & - 1 \\ - 1 & - 1 & a \end{array} \right) \xrightarrow [ r _ {1} \leftrightarrow r _ {3} ^ {*} ]{r _ {3} \times (- 1)} \left( \begin{array}{c c c} 1 & 1 & - a \\ - 1 & a & - 1 \\ a & - 1 & - 1 \end{array} \right) \xrightarrow [ r _ {3} ^ {* *} - a r _ {1} ^ {*} ]{r _ {2} + r _ {1} ^ {*}} \left( \begin{array}{c c c} 1 & 1 & - a \\ 0 & a + 1 & - a - 1 \\ 0 & - a - 1 & a ^ {2} - 1 \end{array} \right)</equation><equation>\xrightarrow {r _ {3} ^ {* * *} + r _ {2} ^ {*}} \left( \begin{array}{c c c} 1 & 1 & - a \\ 0 & a + 1 & - a - 1 \\ 0 & 0 & a ^ {2} - a - 2 \end{array} \right).</equation>当<equation>a^{2}-a-2=0</equation>，即 a=-1或 a=2时，<equation>r(A)<3.</equation>又由于当 a=-1时，<equation>r(A)=1\neq r(B)</equation>，故舍去.

因此，<equation>a = 2</equation>

---


#### 伴随矩阵与可逆矩阵

**2023年第8题 | 选择题 | 5分 | 答案: D**

3. 设 A,B为 n阶可逆矩阵，E为 n阶单位矩阵，<equation>M^{*}</equation>为矩阵 M的伴随矩阵，则<equation>\left( \begin{array}{cc} A & E \\ O & B \end{array} \right)^{*}=(\quad)</equation>A.<equation>\left( \begin{array}{c c} | A | B^{*} & - B^{*} A^{*} \\ O & | B | A^{*} \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c} | A | B^{*} & - A^{*} B^{*} \\ O & | B | A^{*} \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c} | B | A^{*} & - B^{*} A^{*} \\ O & | A | B^{*} \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c} | B | A^{*} & - A^{*} B^{*} \\ O & | A | B^{*} \end{array} \right)</equation>

答案: D

**解析:**解（法一）由于 A,B都可逆，故可以作初等行变换来求<equation>\left( \begin{array}{cc} A & E \\ O & B \end{array} \right)^{-1}.</equation><equation>\left( \begin{array}{c c c c} A & E & E & O \\ O & B & O & E \end{array} \right) \xrightarrow {\textcircled{1}} \left( \begin{array}{c c c c} E & A ^ {- 1} & A ^ {- 1} & O \\ O & E & O & B ^ {- 1} \end{array} \right) \xrightarrow {\textcircled{2}} \left( \begin{array}{c c c c} E & O & A ^ {- 1} & - A ^ {- 1} B ^ {- 1} \\ O & E & O & B ^ {- 1} \end{array} \right),</equation>其中操作<equation>\textcircled{1}</equation>对应左乘可逆矩阵<equation>\left( \begin{array}{cc} A^{-1} & O \\ O & B^{-1} \end{array} \right)</equation>，操作<equation>\textcircled{2}</equation>对应左乘可逆矩阵<equation>\left( \begin{array}{cc} E & -A^{-1} \\ O & E \end{array} \right)</equation>.于是，<equation>\left( \begin{array}{c c} A & E \\ O & B \end{array} \right) ^ {- 1} = \left( \begin{array}{c c} A ^ {- 1} & - A ^ {- 1} B ^ {- 1} \\ O & B ^ {- 1} \end{array} \right).</equation>对于任意 n阶方阵 M，都有<equation>M M^{*} = | M | E</equation>，从而当 M可逆时，<equation>M^{*} = | M | M^{-1}.</equation>又因为<equation>\left| \begin{array}{l l} A & E \\ O & B \end{array} \right| = | A | | B |</equation>，所以<equation>\left( \begin{array}{c c} A & E \\ O & B \end{array} \right) ^ {*} = \left| \begin{array}{c c} A & E \\ O & B \end{array} \right| \left( \begin{array}{c c} A & E \\ O & B \end{array} \right) ^ {- 1} = | A | | B | \left( \begin{array}{c c} A ^ {- 1} & - A ^ {- 1} B ^ {- 1} \\ O & B ^ {- 1} \end{array} \right) = \left( \begin{array}{c c} | B | A ^ {*} & - A ^ {*} B ^ {*} \\ O & | A | B ^ {*} \end{array} \right).</equation>因此，应选D.

也可以如下计算<equation>\left( \begin{array}{cc}A&E\\ O&B \end{array} \right)^{-1}</equation>.

设<equation>\left( \begin{array}{cc} A & E \\ O & B \end{array} \right)^{-1}=\left( \begin{array}{cc} X_{1} & X_{2} \\ X_{3} & X_{4} \end{array} \right),</equation>则<equation>\left( \begin{array}{c c} A & E \\ O & B \end{array} \right) \left( \begin{array}{c c} X _ {1} & X _ {2} \\ X _ {3} & X _ {4} \end{array} \right) = \left( \begin{array}{c c} A X _ {1} + X _ {3} & A X _ {2} + X _ {4} \\ B X _ {3} & B X _ {4} \end{array} \right) = \left( \begin{array}{c c} E & O \\ O & E \end{array} \right).</equation>于是，<equation>\left\{ \begin{array}{l l} A X_{1}+X_{3}=E, \\ A X_{2}+X_{4}=O, \\ B X_{3}=O, \\ B X_{4}=E. \end{array} \right.</equation>由A，B均为可逆矩阵可得<equation>\left\{ \begin{array}{l l} X_{1}=A^{-1}, \\ X_{2}=-A^{-1}B^{-1}, \\ X_{3}=O, \\ X_{4}=B^{-1}. \end{array} \right.</equation>从而<equation>\left( \begin{array}{c c} A & E \\ O & B \end{array} \right) ^ {- 1} = \left( \begin{array}{c c} A ^ {- 1} & - A ^ {- 1} B ^ {- 1} \\ O & B ^ {- 1} \end{array} \right).</equation>（法二）分别记选项A、B、C、D中的矩阵为<equation>M_{1}, M_{2}, M_{3}, M_{4}</equation>，记<equation>\left( \begin{array}{cc} A & E \\ O & B \end{array} \right)=M.</equation>考虑<equation>M_{i}M (i=1,</equation>2,3,4). 若<equation>M_{i}=M^{*}</equation>，则<equation>M_{i}M=|A||B|E_{2n}.</equation>观察可得<equation>M_{1}M</equation>与<equation>M_{2}M</equation>的“第一列”均为<equation>\left( \begin{array}{c c} {| A | B^{*} A} \\ {O} \end{array} \right)</equation>，故<equation>M _ {1} M \neq | A | | B | E _ {2 n}, \quad M _ {2} M \neq | A | | B | E _ {2 n}.</equation>选项A、B均不正确.

又因为<equation>\begin{aligned} \left( \begin{array}{c c c} | B | A ^ {*} & - B ^ {*} A ^ {*} \\ O & | A | B ^ {*}  \right) \left( \begin{array}{c c} A & E \\ O & B  \right) &= \left( \begin{array}{c c c} | A | | B | E & | B | A ^ {*} - B ^ {*} A ^ {*} B \\ O & | A | | B | E  \right) \neq | A | | B | E _ {2 n}, \\ \left( \begin{array}{c c c} | B | A ^ {*} & - A ^ {*} B ^ {*} \\ O & | A | B ^ {*}  \right) \left( \begin{array}{c c} A & E \\ O & B  \right) &= \left( \begin{array}{c c c} | A | | B | E & | B | A ^ {*} - A ^ {*} B ^ {*} B \\ O & | A | | B | E  \right) &= | A | | B | E _ {2 n}, \end{aligned}</equation>所以选项C不正确，选项D正确. 应选D.

---

**2020年第7题 | 选择题 | 4分 | 答案: C**

7. 设4阶矩阵<equation>A=(a_{ij})</equation>不可逆，<equation>a_{12}</equation>代数余子式<equation>A_{12}\neq0,\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4}</equation>为矩阵 A的列向量组，<equation>A^{*}</equation>为 A伴随矩阵，则方程组<equation>A^{*}x=0</equation>通解为（    )

A.<equation>x=k_{1}\alpha_{1}+k_{2}\alpha_{2}+k_{3}\alpha_{3}</equation>，其中<equation>k_{1},k_{2},k_{3}</equation>为任意常数

B.<equation>x=k_{1}\alpha_{1}+k_{2}\alpha_{2}+k_{3}\alpha_{4}</equation>，其中<equation>k_{1},k_{2},k_{3}</equation>为任意常数

C.<equation>x=k_{1}\alpha_{1}+k_{2}\alpha_{3}+k_{3}\alpha_{4}</equation>，其中<equation>k_{1},k_{2},k_{3}</equation>为任意常数

D.<equation>x=k_{1}\alpha_{2}+k_{2}\alpha_{3}+k_{3}\alpha_{4}</equation>，其中<equation>k_{1},k_{2},k_{3}</equation>为任意常数

答案: C

**解析:**解 由 A不可逆可知，<equation>|A|=0</equation>.于是，<equation>A^{*}A=|A|E=0</equation>.从而， A的列向量均为<equation>A^{*}x=0</equation>的解.另一方面，<equation>A_{12}\neq0</equation>，说明<equation>A^{*}</equation>中有非零元素，<equation>r(A^{*})\geqslant1</equation>.又因为 A不可逆，所以<equation>r(A)\leqslant3</equation>.但是当<equation>r(A)<3</equation>时，<equation>r(A^{*})=0</equation>.因此，<equation>r(A)=3</equation><equation>r(A^{*})=1</equation><equation>A^{*}x=0</equation>的基础解系中包含3个解向量.

由<equation>A_{12}\neq0</equation>可知，<equation>\left| \begin{array}{c c c} a_{21} & a_{23} & a_{24} \\ a_{31} & a_{33} & a_{34} \\ a_{41} & a_{43} & a_{44} \end{array} \right| \neq0</equation>.于是，<equation>\left( \begin{array}{l} a_{21} \\ a_{31} \\ a_{41} \end{array} \right), \left( \begin{array}{l} a_{23} \\ a_{33} \\ a_{43} \end{array} \right), \left( \begin{array}{l} a_{24} \\ a_{34} \\ a_{44} \end{array} \right)</equation>线性无关.由分析中的结论可知，<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>线性无关，从而构成<equation>A^{*}x = 0</equation>的一个基础解系.

因此，<equation>A^{*}x=0</equation>的通解可写为<equation>x=k_{1}\alpha_{1}+k_{2}\alpha_{3}+k_{3}\alpha_{4}</equation>其中<equation>k_{1},k_{2},k_{3}</equation>为任意常数.应选C.

---

**2019年第7题 | 选择题 | 4分 | 答案: A**

7. 假设 A是4阶矩阵，<equation>A^{*}</equation>是 A的伴随矩阵，若线性方程组<equation>A x=0</equation>的基础解系中只有2个向量，则<equation>r \left( A^{*} \right)=</equation>(    )

A.0 B.1 C.2 D.3

答案: A

**解析:**解 由于<equation>A x=0</equation>的基础解系中只含有2个向量，故<equation>r(A)=4-2=2</equation>又因为<equation>r(A)=2< 4-1</equation>所以<equation>r(A^{*})=0.</equation>因此，应选A.

---

**2013年第14题 | 填空题 | 4分**

14. 设<equation>A=(a_{ij})</equation>是3阶非零矩阵，<equation>|A|</equation>为 A的行列式，<equation>A_{ij}</equation>为<equation>a_{ij}</equation>的代数余子式. 若<equation>a_{ij}+A_{ij}=0</equation>（i,j=1,2,3），则<equation>|A|=</equation>___

**解析:**首先，由题设可知<equation>\boldsymbol {A} ^ {*} = \left( \begin{array}{c c c} A _ {1 1} & A _ {2 1} & A _ {3 1} \\ A _ {1 2} & A _ {2 2} & A _ {3 2} \\ A _ {1 3} & A _ {2 3} & A _ {3 3} \end{array} \right) \xlongequal {\text {一}} \frac {a _ {i j} + A _ {i j} = 0}{\text {一}} \left( \begin{array}{c c c} - a _ {1 1} & - a _ {2 1} & - a _ {3 1} \\ - a _ {1 2} & - a _ {2 2} & - a _ {3 2} \\ - a _ {1 3} & - a _ {2 3} & - a _ {3 3} \end{array} \right) = - \boldsymbol {A} ^ {\mathrm {T}},</equation>故<equation>|\mathbf{A}|^3 = |\mathbf{A}\mathbf{A}^*| = |-\mathbf{A}\mathbf{A}^{\mathrm{T}}| = -|\mathbf{A}|^2.</equation>因此可以得到<equation>|\mathbf{A}| = 0,</equation>或<equation>|\mathbf{A}| = -1.</equation>另一方面，由于<equation>A</equation>为非零矩阵，故不妨假设<equation>a_{11} \neq 0</equation>，则<equation>| \boldsymbol {A} | = a _ {1 1} A _ {1 1} + a _ {1 2} A _ {1 2} + a _ {1 3} A _ {1 3} = - \left(a _ {1 1} ^ {2} + a _ {1 2} ^ {2} + a _ {1 3} ^ {2}\right) < 0.</equation>因此，<equation>|A| = -1.</equation>

---

**2012年第14题 | 填空题 | 4分**

14. 设<equation>A</equation>为3阶矩阵，<equation>|A|=3</equation><equation>A^{*}</equation>为<equation>A</equation>的伴随矩阵，若交换<equation>A</equation>的第1行与第2行得矩阵<equation>B</equation>，则<equation>|BA^{*}|=</equation>___.

**解析:**解（法一）由于<equation>B</equation>为交换<equation>A</equation>的第1行与第2行所得，故<equation>B = E(1,2)A.</equation>从而<equation>\boldsymbol {B} \boldsymbol {A} ^ {*} = \boldsymbol {E} (1, 2) \boldsymbol {A} \boldsymbol {A} ^ {*} = \boldsymbol {E} (1, 2) | \boldsymbol {A} | \boldsymbol {E} = 3 \boldsymbol {E} (1, 2).</equation>因此，<equation>\left| B A ^ {*} \right| = \left| 3 E (1, 2) \right| = 3 ^ {3} \left| \begin{array}{c c c} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right| = - 2 7.</equation>（法二）由于<equation>A A^{*} = |A|E</equation>，故当A为3阶矩阵时，<equation>| \boldsymbol {A} | \cdot | \boldsymbol {A} ^ {*} | = | \boldsymbol {A A} ^ {*} | = \left| \begin{array}{c c c} | \boldsymbol {A} | & 0 & 0 \\ 0 & | \boldsymbol {A} | & 0 \\ 0 & 0 & | \boldsymbol {A} | \end{array} \right| = | \boldsymbol {A} | ^ {3}.</equation>从而<equation>|A^{*}| = |A|^{2}.</equation>另一方面，由于<equation>B</equation>为交换<equation>A</equation>的第1行与第2行所得矩阵，故<equation>|B| = -|A|</equation>.因此，<equation>| B A ^ {*} | = | B | \cdot | A ^ {*} | = - | A | \cdot | A | ^ {2} = - 2 7.</equation>

---

**2011年第8题 | 选择题 | 4分 | 答案: D**

8. 设<equation>A=\left( \alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4} \right)</equation>是4阶矩阵，<equation>A^{*}</equation>为A的伴随矩阵.若<equation>(1,0,1,0)^{\mathrm{T}}</equation>是方程组<equation>A x=0</equation>的一个基础解系，则<equation>A^{*} x=0</equation>的基础解系可为（    ）

A.<equation>\alpha_{1},\alpha_{3}</equation>B.<equation>\alpha_{1},\alpha_{2}</equation>C.<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>D.<equation>\alpha_{2},\alpha_{3},\alpha_{4}</equation>

答案: D

**解析:**解 由于<equation>( 1,0,1,0 )^{\mathrm{T}}</equation>为<equation>A x=0</equation>的一个基础解系，故该方程组的解集的秩为1，从而<equation>r ( A )=3.</equation>由<equation>r ( A )</equation>与<equation>r ( A^{*} )</equation>的关系可得<equation>r ( A^{*} )=1.</equation>于是<equation>A^{*} x=0</equation>的解集的秩为3，基础解系应包含3个线性无关的向量.因此，可以排除选项A、B.

由于<equation>r(A) = 3, |A| = 0, A^{*}A = |A|E = O</equation>，故<equation>A</equation>的列向量均为<equation>A^{*}x = 0</equation>的解。又因为<equation>r(A) = 3</equation>，所以可以从<equation>A</equation>的列向量组中找出3个线性无关的列向量作为<equation>A^{*}x = 0</equation>的一个基础解系.

另一方面，由于<equation>(1,0,1,0)^{\mathrm{T}}</equation>是方程组<equation>Ax = 0</equation>的一个基础解系，故<equation>\left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\alpha} _ {2}, \boldsymbol {\alpha} _ {3}, \boldsymbol {\alpha} _ {4}\right) (1, 0, 1, 0) ^ {\mathrm {T}} = \boldsymbol {\alpha} _ {1} + \boldsymbol {\alpha} _ {3} = \mathbf {0}.</equation>于是<equation>\alpha_{1}</equation>与<equation>\alpha_{3}</equation>线性相关，因此可以排除选项C.由排除法知，应选D.

---

**2009年第7题 | 选择题 | 4分 | 答案: B**

7. 设 A,B均为2阶方阵，<equation>A^{*}，B^{*}</equation>分别为 A,B的伴随矩阵.若<equation>|A|=2,|B|=3</equation>，则分块矩阵<equation>\left( \begin{array}{cc} O&A \\ B/O \end{array} \right)</equation>的伴随矩阵为（    )

A.<equation>\left( \begin{array}{cc} O&3 B^{*} \\ 2 A^{*}&O \end{array} \right)</equation>B.<equation>\left( \begin{array}{cc} O&2 B^{*} \\ 3 A^{*}&O \end{array} \right)</equation>C.<equation>\left( \begin{array}{cc} O&3 A^{*} \\ 2 B^{*}&O \end{array} \right)</equation>D.<equation>\left( \begin{array}{cc} O&2 A^{*} \\ 3 B^{*}&O \end{array} \right)</equation>

答案: B

**解析:**解 （法一）先求<equation>\left| \begin{array}{ll}O&A\\ BO\end{array} \right|.</equation>记<equation>C=\left( \begin{array}{cc}O&A\\ B/O \end{array} \right), C</equation>为4阶矩阵，A位于它的第1，2行和第3，4列，可按照以下步骤把C变为<equation>\left( \begin{array}{cc}A&O\\ O&B \end{array} \right).</equation>把C的第3列与第1列对换，第4列与第2列对换.

因此，<equation>\left| \begin{array}{c c} O & A \\ B & O \end{array} \right| = (- 1) ^ {2} \left| \begin{array}{c c} A & O \\ O & B \end{array} \right| = | A | \cdot | B | = 6.</equation><equation>\left( \begin{array}{cc}O&A\\ BO\end{array} \right)</equation>可逆.

由可逆矩阵与其伴随矩阵的关系可知，<equation>\left( \begin{array}{c c} O & A \\ B & O \end{array} \right) ^ {*} = \left| \begin{array}{c c} O & A \\ B & O \end{array} \right| \left( \begin{array}{c c} O & A \\ B & O \end{array} \right) ^ {- 1} = 6 \left( \begin{array}{c c} O & A \\ B & O \end{array} \right) ^ {- 1}.</equation>不妨设<equation>\left( \begin{array}{cc}O&A\\ B/O \end{array} \right)^{-1} = \left( \begin{array}{cc}X_1 & X_2\\ X_3 & X_4 \end{array} \right)</equation>，则<equation>\left( \begin{array}{c c} O & A \\ B & O \end{array} \right) \left( \begin{array}{c c} X _ {1} & X _ {2} \\ X _ {3} & X _ {4} \end{array} \right) = \left( \begin{array}{c c} A X _ {3} & A X _ {4} \\ B X _ {1} & B X _ {2} \end{array} \right) = \left( \begin{array}{c c} E & O \\ O & E \end{array} \right).</equation>由于 A,B均为可逆矩阵，故由<equation>A X_{4}=O</equation><equation>B X_{1}=O</equation>可知，<equation>X_{1}=X_{4}=O</equation>；由<equation>A X_{3}=E</equation><equation>B X_{2}=E</equation>得，<equation>X_{3}=A^{-1}</equation><equation>X_{2}=B^{-1}</equation>因此，<equation>\left( \begin{array}{c c} \boldsymbol {O} & \boldsymbol {A} \\ \boldsymbol {B} & \boldsymbol {O} \end{array} \right) ^ {- 1} = \left( \begin{array}{c c} \boldsymbol {O} & \boldsymbol {B} ^ {- 1} \\ \boldsymbol {A} ^ {- 1} & \boldsymbol {O} \end{array} \right).</equation><equation>\left( \begin{array}{c c} O & A \\ B & O \end{array} \right) ^ {*} = 6 \left( \begin{array}{c c} O & B ^ {- 1} \\ A ^ {- 1} & O \end{array} \right) = 6 \left( \begin{array}{c c} O & \frac {B ^ {*}}{| B |} \\ \frac {A ^ {*}}{| A |} & O \end{array} \right) = \left( \begin{array}{c c} O & 2 B ^ {*} \\ 3 A ^ {*} & O \end{array} \right).</equation>应选B.

（法二）不妨设<equation>\left( \begin{array}{cc}O&A\\ B/O \end{array} \right)^{*} = \left( \begin{array}{cc}X_{1} & X_{2}\\ X_{3} & X_{4} \end{array} \right)</equation>由法一知，<equation>\left| \begin{array}{cc}O&A\\ BO\end{array}\right|=6</equation>故<equation>\left( \begin{array}{c c} O & A \\ B & O \end{array} \right) \left( \begin{array}{c c} X _ {1} & X _ {2} \\ X _ {3} & X _ {4} \end{array} \right) = \left( \begin{array}{c c} A X _ {3} & A X _ {4} \\ B X _ {1} & B X _ {2} \end{array} \right) = \left( \begin{array}{c c} 6 E & O \\ O & 6 E \end{array} \right).</equation>从而，<equation>A X _ {3} = 6 E, \quad B X _ {2} = 6 E, \quad A X _ {4} = B X _ {1} = O.</equation>由此可推出，<equation>X_{3}=6 A^{-1}=6 \cdot \frac{A^{*}}{\mid A\mid}=3 A^{*}, X_{2}=6 B^{-1}=6 \cdot \frac{B^{*}}{\mid B\mid}=2 B^{*}, X_{1}=X_{4}=O.</equation>因此，<equation>\left( \begin{array}{cc} O & A \\ B & O \end{array} \right)^{*} = \left( \begin{array}{cc} O & 2 B^{*} \\ 3 A^{*} & O \end{array} \right).</equation>应选B.

（法三）特殊值法.

取<equation>A=\sqrt{2} E, B=\sqrt{3} E</equation>满足<equation>| A |=2, | B |=3</equation>，则<equation>A^{*} = | A | A^{-1} = \sqrt{2} E, B^{*} = | B | B^{-1} = \sqrt{3} E.</equation>因此，<equation>\begin{aligned} \left( \begin{array}{c c} O & A \\ B & O  \right) ^ {*} &= \left( \begin{array}{c c} O & \sqrt {2} E \\ \sqrt {3} E & O  \right) ^ {*} &= \left| \begin{array}{c c} O & \sqrt {2} E \\ \sqrt {3} E & O  \right| \left( \begin{array}{c c} O & \sqrt {2} E \\ \sqrt {3} E & O  \right) ^ {- 1} &= 6 \left( \begin{array}{c c} O & \frac {1}{\sqrt {3}} E \\ \frac {1}{\sqrt {2}} E & O  \right) \\ &= \left( \begin{array}{c c} O & 2 \sqrt {3} E \\ 3 \sqrt {2} E & O  \right) &= \left( \begin{array}{c c} O & 2 B ^ {*} \\ 3 A ^ {*} & O  \right). \end{aligned}</equation>应选B.

---


### 线性方程组

**2025年第10题 | 选择题 | 5分 | 答案: D**
10. 设3阶矩阵 A,B满足<equation>r( A B)=r( B A)+1</equation>，则（    )

A. 方程组<equation>( A+B) x=0</equation>只有零解

B. 方程组<equation>A x=0</equation>与方程组<equation>B x=0</equation>均只有零解

C. 方程组<equation>A x=0</equation>与方程组<equation>B x=0</equation>没有公共非零解

D. 方程组<equation>A B A x=0</equation>与方程组<equation>B A B x=0</equation>有公共非零
答案: D
**解析: **解 若矩阵 A,B 中有一个为可逆矩阵，则<equation>r(AB)=r(BA)=\min \{r(A),r(B)\}</equation>，这与<equation>r(AB)</equation><equation>= r(BA) + 1</equation>矛盾.同理，若矩阵 A,B 中有一个为零矩阵，则<equation>r(AB)=r(BA)=0</equation>，这也与<equation>r(AB)</equation><equation>= r(BA) + 1</equation>矛盾.由此可得，<equation>1\leqslant r(A),r(B)\leqslant 2.</equation>进一步可得方程组<equation>Ax=0</equation>与方程组<equation>Bx=0</equation>均有非零解.选项B不正确.

由<equation>1 \leqslant r(A), r(B) \leqslant 2</equation>可得<equation>r(AB) \leqslant 2, r(BA) \leqslant 2.</equation>由<equation>r(\mathbf{AB}) = r(\mathbf{BA}) + 1</equation>可得，<equation>\left\{ \begin{array}{l l} r(\mathbf{AB}) = 2, \\ r(\mathbf{BA}) = 1 \end{array} \right.</equation>或<equation>\left\{ \begin{array}{l l} r(\mathbf{AB}) = 1, \\ r(\mathbf{BA}) = 0. \end{array} \right.</equation>若<equation>\left\{ \begin{array}{l l} r ( A B ) = 1, \\ r ( B A ) = 0, \end{array} \right.</equation>则<equation>A B A=B A B=O</equation>方程组ABAx=0与方程组BABx=0的解均为全体3维列向量，从而存在公共非零解.

若<equation>\left\{ \begin{array}{l} r(AB) = 2, \\ r(BA) = 1, \end{array} \right.</equation>则<equation>r(ABA) \leqslant \min \{r(A), r(BA)\} = 1, r(BAB) \leqslant \min \{r(B), r(BA)\} = 1,</equation>从而<equation>r(ABA) + r(BAB) \leqslant 2 < 3.</equation>考虑方程组<equation>\left\{ \begin{array}{l l} A B A x = 0, \\ B A B x = 0. \end{array} \right.</equation>下面我们证明<equation>r \binom {A B A}{B A B} < 3.</equation><equation>\begin{aligned} r \binom {A B A} {B A B} &= r \left(\left(\mathrm {A B A}\right) ^ {\mathrm {T}}, \left(\mathrm {B A B}\right) ^ {\mathrm {T}}\right) \leqslant r \left(\left(\mathrm {A B A}\right) ^ {\mathrm {T}}\right) + r \left(\left(\mathrm {B A B}\right) ^ {\mathrm {T}}\right) \\ &= r \left(\mathrm {A B A}\right) + r \left(\mathrm {B A B}\right) < 3. \end{aligned}</equation>由于方程组<equation>\left\{\begin{array}{l l} A B A x=0, \\ B A B x=0 \end{array} \right.</equation>的系数矩阵的秩小于3，故该方程组有非零解，从而方程组<equation>A B A x=0</equation>与方程组<equation>B A B x=0</equation>有公共非零解.选项D正确.

因此，应选D.

下面我们说明选项A、C不正确.

注意到若方程组<equation>A x=0</equation>与方程组<equation>B x=0</equation>有公共非零解，则该非零解也是方程组（<equation>A+B ) x= 0</equation>的解.

取<equation>A=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right), B=\left( \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>，则<equation>A B=\left( \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right), B A=\left( \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>，满足<equation>r( A B)=</equation><equation>r( B A )+1</equation>，但（0，0，1）<equation>^{\mathrm{T}}</equation>是方程组<equation>A x=0</equation>与<equation>B x=0</equation>的公共非零解，也是方程组（A+B）x=0的非零解.

---

**2025年第16题 | 填空题 | 5分**
16. 设矩阵<equation>A=\left( \alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4}\right)</equation>，若<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关，且<equation>\alpha_{1}+\alpha_{2}=\alpha_{3}+\alpha_{4}</equation>，则方程组<equation>A x=\alpha_{1}+4 \alpha_{4}</equation>的通解为 x=
**答案: **<equation>k \left( \begin{array}{c} 1 \\ 1 \\ - 1 \\ - 1 \end{array} \right) + \left( \begin{array}{c} 1 \\ 0 \\ 0 \\ 4 \end{array} \right)</equation>
**解析: **解 由于<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关，故<equation>r(A)\geqslant 3.</equation>又因为<equation>\alpha_{1} + \alpha_{2} = \alpha_{3} + \alpha_{4}</equation>，所以<equation>\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4}</equation>线性相关，从而<equation>r(A)\leqslant 3.</equation>由此可得<equation>r(A) = 3</equation>，进一步可得方程组<equation>Ax = 0</equation>的基础解系中仅包含4-3=1个向量.

由<equation>\alpha_{1}+\alpha_{2}=\alpha_{3}+\alpha_{4}</equation>可得<equation>\alpha_{1}+\alpha_{2}-\alpha_{3}-\alpha_{4}=0</equation>即<equation>\left( \alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4}\right)\left( \begin{array}{c}1\\ 1\\ -1\\ -1 \end{array}\right)=0</equation>于是<equation>\left( \begin{array}{c}1\\ 1\\ -1\\ -1 \end{array}\right)</equation>是方

程组<equation>Ax = 0</equation>的一个解，且构成<equation>Ax = 0</equation>的一个基础解系.

由于<equation>A\left( \begin{array}{c}1\\ 0\\ 0\\ 4 \end{array} \right)=(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4})\left( \begin{array}{c}1\\ 0\\ 0\\ 4 \end{array} \right)=\alpha_{1}+4\alpha_{4}</equation>，故<equation>\left( \begin{array}{c}1\\ 0\\ 0\\ 4 \end{array} \right)</equation>是方程组<equation>Ax = \alpha_{1} + 4\alpha_{4}</equation>的一个特解.

因此，方程组<equation>A x=\alpha_{1}+4 \alpha_{4}</equation>的通解为<equation>k ( 1,1,-1,-1 )^{\mathrm{T}}+(1,0,0,4)^{\mathrm{T}}</equation>，其中 k为任意常数.

---

**2023年第16题 | 填空题 | 5分**
16. 已知线性方程组<equation>\left\{ \begin{array}{l l} a x _ {1} + x _ {3} = 1 \\ x _ {1} + a x _ {2} + x _ {3} = 0 \\ x _ {1} + 2 x _ {2} + a x _ {3} = 0 \\ a x _ {1} + b x _ {2} = 2 \end{array} \right. \mathrm {有 解}, \mathrm {其 中} a, b \mathrm {为 常 数}, \mathrm {若} \left| \begin{array}{c c c} a & 0 & 1 \\ 1 & a & 1 \\ 1 & 2 & a \end{array} \right| = 4, \mathrm {则} \left| \begin{array}{c c c} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right| = \underline {{\quad}}.</equation>
**解析: **解（法一）记方程组<equation>\left\{ \begin{array}{l l} a x_{1}+x_{3}=1, \\ x_{1}+a x_{2}+x_{3}=0, \\ x_{1}+2 x_{2}+a x_{3}=0, \\ a x_{1}+b x_{2}=2 \end{array} \right.</equation>的系数矩阵为A，增广矩阵为（A,b），则<equation>(\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} a & 0 & 1 & 1 \\ 1 & a & 1 & 0 \\ 1 & 2 & a & 0 \\ a & b & 0 & 2 \end{array} \right).</equation>由方程组有解可知<equation>r ( A )=r ( A , b ).</equation>因为A为<equation>4\times 3</equation>矩阵，所以<equation>r ( A )\leqslant 3</equation>从而<equation>r ( A )=r ( A , b )\leqslant 3</equation>进一步可得<equation>| A,b|=0.</equation>于是，<equation>0 = \left| \begin{array}{c c c c} a & 0 & 1 & 1 \\ 1 & a & 1 & 0 \\ 1 & 2 & a & 0 \\ a & b & 0 & 2 \end{array} \right| \xlongequal {\text {按 第四 列 展开}} - \left| \begin{array}{c c c} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right| + 2 \left| \begin{array}{c c c} a & 0 & 1 \\ 1 & a & 1 \\ 1 & 2 & a \end{array} \right| = - \left| \begin{array}{c c c} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right| + 8.</equation>因此，<equation>\left| \begin{array}{c c c} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right|=8.</equation>（法二）记方程组<equation>\left\{ \begin{array}{l l} a x_{1}+x_{3}=1, \\ x_{1}+a x_{2}+x_{3}=0, \\ x_{1}+2 x_{2}+a x_{3}=0, \\ a x_{1}+b x_{2}=2 \end{array} \right.</equation>的系数矩阵为 A，增广矩阵为（A,b）.由方程组有解可知<equation>r ( \mathbf{A})=r ( \mathbf{A},\mathbf{b})</equation>注意到<equation>\left| \begin{array}{c c c} a & 0 & 1 \\ 1 & a & 1 \\ 1 & 2 & a \end{array} \right|=4</equation>为 A的一个3阶非零子式，故<equation>r ( \mathbf{A})\geqslant 3.</equation>又因为 A为<equation>4 \times 3</equation>矩阵，所以<equation>r ( \mathbf{A})\leqslant 3</equation>从而<equation>r ( \mathbf{A})=3.</equation>由<equation>r ( A )=r ( A , b )</equation>可得，<equation>r ( A , b )=3</equation>.于是<equation>r ( A )=r ( A , b )=3</equation>，该方程组有唯一解.

考虑方程组 I：<equation>\left\{\begin{array}{l l} a x_{1}+x_{3}=1, \\ x_{1}+a x_{2}+x_{3}=0, \\ x_{1}+2 x_{2}+a x_{3}=0 \end{array} \right.</equation>，和方程组Ⅱ：<equation>\left\{\begin{array}{l l} x_{1}+a x_{2}+x_{3}=0, \\ x_{1}+2 x_{2}+a x_{3}=0, \\ a x_{1}+b x_{2}=2. \end{array} \right.</equation>，由原方程组有唯一解

可知方程组 I和方程组Ⅱ有唯一公共解.

由于方程组Ⅰ的系数矩阵行列式等于4，故由克拉默法则知其仅有唯一解，进一步可得其增广矩阵的秩为3，行向量组线性无关。由此可知方程组Ⅱ的增广矩阵<equation>\left( \begin{array}{c c c c} {1} & {a} & {1} & {0} \\ {1} & {2} & {a} & {0} \\ {a} & {b} & {0} & {2} \end{array} \right)</equation>的前两行线性无关。又因为该增广矩阵的第三行为（a,b，0，2），最后一个元素非零，所以第三行与前两行线性无关。于是，方程组Ⅱ的增广矩阵的秩为3。由方程组Ⅱ有解可知，其系数矩阵的秩也为3，从而行列式非零.

记该公共解为<equation>\left( x_{1}, x_{2}, x_{3}\right)^{\mathrm{T}}</equation><equation>\left| \begin{array}{lll} a & 0 & 1 \\ 1 & a & 1 \\ 1 & 2 & a \end{array} \right|=A_{1}=4</equation><equation>\left| \begin{array}{lll} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right|=A_{2}\neq0.</equation>对方程组 I 使用克拉默法则可得<equation>x_{1}=\frac{\left| \begin{array}{lll} 1 & 0 & 1 \\ 0 & a & 1 \\ 0 & 2 & a \end{array} \right|}{A_{1}}=\frac{\left| \begin{array}{lll} 1 & 0 & 1 \\ 0 & a & 1 \\ 0 & 2 & a \end{array} \right|}{4}</equation>，对方程组Ⅱ使用克拉默法则可得<equation>x_{1}=\frac{\left| \begin{array}{lll} 0 & a & 1 \\ 0 & 2 & a \\ 2 & b & 0 \end{array} \right|}{A_{2}}.</equation>由此可得<equation>x _ {1} = \frac {\left| \begin{array}{c c} a & 1 \\ 2 & a \end{array} \right|}{4} = \frac {2 \left| \begin{array}{c c} a & 1 \\ 2 & a \end{array} \right|}{A _ {2}}.</equation>若<equation>\left| \begin{array}{ll} a & 1 \\ 2 & a \end{array} \right|=0</equation>，则 a =<equation>\pm \sqrt{2}</equation>.但将 a =<equation>\pm \sqrt{2}</equation>代入<equation>\left| \begin{array}{lll} a & 0 & 1 \\ 1 & a & 1 \\ 1 & 2 & a \end{array} \right|</equation>所得行列式并不等于4，故<equation>\left| \begin{array}{ll} a & 1 \\ 2 & a \end{array} \right| \neq</equation>0. 因此，由（1）式可得<equation>A_{2}=8</equation>，即<equation>\left| \begin{array}{lll} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right|=8.</equation>

---

**2022年第9题 | 选择题 | 5分 | 答案: D**
9. 设矩阵<equation>A=\left( \begin{array}{c c c} {1} & {1} & {1} \\ {1} & {a} & a^{2} \\ {1} & {b} & b^{2} \end{array} \right), b=\left( \begin{array}{c} {1} \\ {2} \\ {4} \end{array} \right),</equation>则线性方程组<equation>A x=b</equation>的解的情况为（    )

A. 无解 B. 有解 C. 有无穷多解或无解 D. 有唯一解或无解
答案: D
**解析: **解 （法一）注意到<equation>| A | = \left| \begin{array}{c c c} 1 & 1 & 1 \\ 1 & a & a ^ {2} \\ 1 & b & b ^ {2} \end{array} \right| = \left| \begin{array}{c c c} 1 & 1 & 1 \\ 1 & a & b \\ 1 & a ^ {2} & b ^ {2} \end{array} \right| = (b - a) (b - 1) (a - 1).</equation>当 a≠1,b≠1，且 a≠b时，<equation>|A| \neq 0.</equation>由克拉默法则可知，此时方程组<equation>A x=b</equation>有唯一解.

当 a=1时，<equation>(\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 2 \\ 1 & b & b ^ {2} & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 0 & 0 & 0 & 1 \\ 1 & b & b ^ {2} & 4 \end{array} \right).</equation><equation>r ( \mathbf{A}, \mathbf{b} ) \neq r ( \mathbf{A} )</equation>，方程组无解.同理可得，当<equation>b=1</equation>时，<equation>r ( \mathbf{A}, \mathbf{b} ) \neq r ( \mathbf{A} )</equation>，方程组无解.

当 a = b时，<equation>(\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 1 & a & a ^ {2} & 2 \\ 1 & b & b ^ {2} & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 1 & a & a ^ {2} & 2 \\ 0 & 0 & 0 & 2 \end{array} \right).</equation><equation>r ( \mathbf{A}, \mathbf{b}) \neq r (\mathbf{A})</equation>，方程组无解.

综上所述，方程组<equation>A x=b</equation>的解的情况只有两种可能，有唯一解或无解.应选D.

（法二）直接对增广矩阵（A,b）作初等行变换.<equation>(\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 1 & a & a ^ {2} & 2 \\ 1 & b & b ^ {2} & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 0 & a - 1 & a ^ {2} - 1 & 1 \\ 0 & b - 1 & b ^ {2} - 1 & 3 \end{array} \right).</equation>当 a = b = 1时，<equation>r ( \mathbf{A} )=1, r ( \mathbf{A}, \mathbf{b} )=2</equation>，方程组无解.

当<equation>a = 1,b\neq 1</equation>或<equation>a\neq 1,b = 1</equation>时，<equation>r(A) = 2,r(A,b) = 3</equation>，方程组无解.

当 a = b，但均不等于1时，<equation>r(\mathbf{A})=2,r(\mathbf{A},\mathbf{b})=3</equation>，方程组无解.

当<equation>a\neq 1,b\neq 1</equation>，且<equation>a\neq b</equation>时，<equation>r(A) = r(A,b) = 3.</equation>方程组有唯一解.

综上所述，方程组<equation>A x=b</equation>的解的情况只有两种可能，有唯一解或无解.应选D.

---

**2021年第9题 | 选择题 | 5分 | 答案: D**
9. 设3阶矩阵<equation>A=(\alpha_{1},\alpha_{2},\alpha_{3}),B=(\beta_{1},\beta_{2},\beta_{3})</equation>，若向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>可以由向量组<equation>\beta_{1},\beta_{2},\beta_{3}</equation>线性表示，则（    )

A.<equation>A x=0</equation>的解均为<equation>B x=0</equation>解 B.<equation>A^{\mathrm{T}} x=0</equation>的解均为<equation>B^{\mathrm{T}} x=0</equation>解

C.<equation>B x=0</equation>的解均为<equation>A x=0</equation>解 D.<equation>B^{\mathrm{T}} x=0</equation>的解均为<equation>A^{\mathrm{T}} x=0</equation>解
答案: D
**解析: **解（法一）由已知条件可知 A的列向量组可由 B的列向量组线性表示，故<equation>A^{\mathrm{T}}</equation>的行向量组可由<equation>B^{\mathrm{T}}</equation>的行向量组线性表示.若<equation>x_{0}</equation>为<equation>B^{\mathrm{T}} x=0</equation>的解，则<equation>x_{0}</equation>与<equation>B^{\mathrm{T}}</equation>的行向量均正交，从而与<equation>A^{\mathrm{T}}</equation>的行向量均正交.根据分析中的结论，可得<equation>A^{\mathrm{T}} x_{0}=0.</equation>因此，<equation>\mathbf{B}^{\mathrm{T}}\mathbf{x}=\mathbf{0}</equation>的解均为<equation>\mathbf{A}^{\mathrm{T}}\mathbf{x}=\mathbf{0}</equation>的解.应选D.

（法二）由于向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>可由向量组<equation>\beta_{1},\beta_{2},\beta_{3}</equation>线性表示，故存在矩阵<equation>P</equation>，使得<equation>A = BP</equation>由<equation>A=B P</equation>可得<equation>A^{\mathrm{T}}=P^{\mathrm{T}}B^{\mathrm{T}}</equation>.于是，若<equation>B^{\mathrm{T}}x=0</equation>，则<equation>A^{\mathrm{T}}x=P^{\mathrm{T}}B^{\mathrm{T}}x=P^{\mathrm{T}}(B^{\mathrm{T}}x)=0</equation>，即<equation>B^{\mathrm{T}}x=0</equation>的解均为<equation>A^{\mathrm{T}}x=0</equation>的解.

因此，应选D.

---

**2018年第23题 | 解答题 | 11分**
23. （本题满分11分）

已知 a是常数，且矩阵<equation>A=\left( \begin{array}{c c c}1&2&a\\ 1&3&0\\ 2&7&-a \end{array} \right)</equation>可经初等列变换化为矩阵<equation>B=\left( \begin{array}{c c c}1&a&2\\ 0&1&1\\ -1&1&1 \end{array} \right).</equation>I. 求 a;

II. 求满足<equation>A P=B</equation>的可逆矩阵<equation>P.</equation>
**答案: **(I)<equation>a=2;</equation>（Ⅱ）满足<equation>A P=B</equation>的可逆矩阵为<equation>\boldsymbol {P} = \left( \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right),</equation>其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数，且<equation>k_{2} \neq k_{3}</equation>.
**解析: **解（I）由于 A可经初等列变换化为 B，故矩阵方程 AX=B有解.于是，<equation>r(A)=r(A,B).</equation>对（A,B）作初等行变换.<equation>\begin{array}{l} (A, B) = \left( \begin{array}{c c c c c c} 1 & 2 & a & 1 & a & 2 \\ 1 & 3 & 0 & 0 & 1 & 1 \\ 2 & 7 & - a & - 1 & 1 & 1 \end{array} \right) \xrightarrow [ r _ {3} - 2 r _ {1} ]{r _ {2} - r _ {1}} \left( \begin{array}{c c c c c c} 1 & 2 & a & 1 & a & 2 \\ 0 & 1 & - a & - 1 & 1 - a & - 1 \\ 0 & 3 & - 3 a & - 3 & 1 - 2 a & - 3 \end{array} \right) \\ \xrightarrow [ r _ {3} ^ {*} - 3 r _ {2} ^ {*} ]{r _ {1} - 2 r _ {2} ^ {*}} \left( \begin{array}{c c c c c c} 1 & 0 & 3 a & 3 & 3 a - 2 & 4 \\ 0 & 1 & - a & - 1 & 1 - a & - 1 \\ 0 & 0 & 0 & 0 & a - 2 & 0 \end{array} \right). \\ \end{array}</equation>当且仅当 a = 2时，<equation>r(\mathbf{A})=r(\mathbf{A},\mathbf{B})=2.</equation>或者，由矩阵<equation>A</equation>可经初等列变换化为矩阵<equation>B</equation>可知，<equation>A</equation>的列秩等于<equation>B</equation>的列秩，从而<equation>r(A) = r(B)</equation>.同上面的计算可知<equation>r(A) = 2</equation>，当且仅当<equation>a = 2</equation>时，<equation>r(A) = r(B)</equation>.

因此，<equation>a=2.</equation>（Ⅱ）当 a=2时，<equation>(\boldsymbol {A}, \boldsymbol {B}) \rightarrow \left(\begin{array}{c c c c c c}1&0&6&3&4&4\\0&1&- 2&- 1&- 1&- 1\\0&0&0&0&0&0\end{array}\right).</equation><equation>A X=B</equation>等价于<equation>\left( \begin{array}{c c c} 1 & 0 & 6 \\ 0 & 1 & -2 \\ 0 & 0 & 0 \end{array} \right) X=\left( \begin{array}{c c c} 3 & 4 & 4 \\ -1 & -1 & -1 \\ 0 & 0 & 0 \end{array} \right).</equation>记<equation>\left( \begin{array}{c c c} 1 & 0 & 6 \\ 0 & 1 & -2 \\ 0 & 0 & 0 \end{array} \right)=A^{\prime}.</equation>方程组<equation>A^{\prime} x=0</equation>的一个基础解系为<equation>(-6,2,1)^{\mathrm{T}}.</equation>于是，方程组<equation>A^{\prime} x=(3,-1,0)^{\mathrm{T}}</equation>的通解为<equation>x_{1}=k_{1}(-6,2,1)^{\mathrm{T}}+</equation><equation>(3,-1,0)^{\mathrm{T}}</equation>其中<equation>k_{1}</equation>为任意常数；方程组<equation>A^{\prime} x=(4,-1,0)^{\mathrm{T}}</equation>的通解为<equation>x_{2}=k_{2}(-6,2,1)^{\mathrm{T}}+</equation><equation>(4,-1,0)^{\mathrm{T}}</equation>其中<equation>k_{2}</equation>为任意常数；方程组<equation>A^{\prime} x=(4,-1,0)^{\mathrm{T}}</equation>的通解为<equation>x_{3}=k_{3}(-6,2,1)^{\mathrm{T}}+</equation><equation>(4,-1,0)^{\mathrm{T}}</equation>其中<equation>k_{3}</equation>为任意常数.

因此，矩阵方程 AX=B的通解为<equation>\boldsymbol {X} = \left( \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right),</equation>其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数.

若可逆矩阵 P满足 AP=B，则<equation>\boldsymbol {P} = \left( \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right),</equation>且<equation>| P | \neq 0.</equation>由于<equation>| P | = \left| \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right| = \left| \begin{array}{c c c} 0 & 1 & 1 \\ - 1 & - 1 & - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right| = \left| \begin{array}{c c c} 0 & 1 & 1 \\ - 1 & 0 & 0 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right| = k _ {3} - k _ {2},</equation>故当<equation>k_{2}\neq k_{3}</equation>时，P可逆.

因此，满足 AP=B的可逆矩阵为<equation>\boldsymbol {P} = \left( \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right),</equation>其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数，且<equation>k_{2} \neq k_{3}</equation>.

---

**2017年第22题 | 解答题 | 11分**
22. (本题满分11分)

设3阶矩阵<equation>A=(\alpha_{1},\alpha_{2},\alpha_{3})</equation>有3个不同的特征值，且<equation>\alpha_{3}=\alpha_{1}+2\alpha_{2}</equation>I. 证明<equation>r(A)=2;</equation>II. 若<equation>\beta=\alpha_{1}+\alpha_{2}+\alpha_{3}</equation>，求方程组<equation>A x=\beta</equation>的通解.
**答案: **（I）证明略；

（Ⅱ）<equation>k ( 1, 2, - 1 )^{\mathrm{T}}+( 1, 1, 1 )^{\mathrm{T}}</equation>为线性方程组<equation>A x=\beta</equation>的通解，其中 k为任意常数.
**解析: **解（I）（法一）由于 A有3个不同的特征值<equation>\lambda_{1},\lambda_{2},\lambda_{3}</equation>，故 A相似于对角矩阵，且至多仅有一个零特征值.该对角矩阵的秩<equation>\geqslant 2</equation>，于是<equation>r(A)\geqslant 2.</equation>又因为<equation>\boldsymbol{\alpha}_{3}=\boldsymbol{\alpha}_{1}+2\boldsymbol{\alpha}_{2}</equation>，所以<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性相关，<equation>|A|=0.</equation>由于<equation>| A| = \lambda_{1}\lambda_{2}\lambda_{3}</equation>，故A有一个特征值为零.

因此，<equation>r ( A ) = 2.</equation>（法二）也可以如下证明0是A的一个特征值.

由<equation>\boldsymbol{\alpha}_{3}=\boldsymbol{\alpha}_{1}+2\boldsymbol{\alpha}_{2}</equation>知<equation>\left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) \left( \begin{array}{c} 1 \\ 2 \\ - 1 \end{array} \right) = \mathbf {0} = 0 \left( \begin{array}{c} 1 \\ 2 \\ - 1 \end{array} \right).</equation>于是，0是 A的一个特征值，<equation>( 1, 2, - 1 )^{\mathrm{T}}</equation>是 A的属于特征值0的一个特征向量.

其余同法一.

（Ⅱ）考虑<equation>A x=0</equation>. 由于<equation>r(A)=2</equation>，故<equation>A x=0</equation>的基础解系中只包含一个向量. 又因为<equation>\alpha_{3}=\alpha_{1}+2\alpha_{2}</equation>，所以<equation>\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)\left(1,2,-1\right)^{\mathrm{T}}=0</equation>，即<equation>\left(1,2,-1\right)^{\mathrm{T}}</equation>是该齐次线性方程组的一个基础解系.

由于<equation>\beta = \alpha_{1} + \alpha_{2} + \alpha_{3}</equation>，即<equation>(\alpha_{1},\alpha_{2},\alpha_{3}) (1,1,1)^{\mathrm{T}} = \beta</equation>，故<equation>(1,1,1)^{\mathrm{T}}</equation>是<equation>A x = \beta</equation>的一个特解.

因此，<equation>k ( 1, 2, - 1 )^{\mathrm{T}}+( 1, 1, 1 )^{\mathrm{T}}</equation>为线性方程组<equation>A x=\beta</equation>的通解，其中k为任意常数.

---

**2016年第22题 | 解答题 | 11分**
22. （本题满分11分）

设矩阵<equation>A = \left( \begin{array}{c c c} 1 & 1 & 1 - a \\ 1 & 0 & a \\ a + 1 & 1 & a + 1 \end{array} \right),\beta = \left( \begin{array}{c} 0 \\ 1 \\ 2a - 2 \end{array} \right),</equation>且方程组<equation>A x=\beta</equation>无解.

I. 求 a的值；

II. 求方程组<equation>A^{\mathrm{T}} A x=A^{\mathrm{T}} \beta</equation>的通解.
**答案: **（ I ）<equation>a=0;</equation>（ II ）<equation>k(0,-1,1)^{\mathrm{T}}+(1,-2,0)^{\mathrm{T}}</equation>，其中 k为任意常数.
**解析: **解（I）由于<equation>A x=\beta</equation>无解，故由非齐次线性方程组有解的充分必要条件可知，<equation>r(A,\beta)\neq r(A).</equation><equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c} 1 & 1 & 1 - a & 0 \\ 1 & 0 & a & 1 \\ a + 1 & 1 & a + 1 & 2 a - 2 \end{array} \right) \xrightarrow {r _ {2} - r _ {1}} \frac {r _ {2} - r _ {1}}{r _ {3} - (a + 1) r _ {1}} \left( \begin{array}{c c c c} 1 & 1 & 1 - a & 0 \\ 0 & - 1 & 2 a - 1 & 1 \\ 0 & - a & a ^ {2} + a & 2 a - 2 \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} \times (- 1)} \left( \begin{array}{c c c c} 1 & 1 & 1 - a & 0 \\ 0 & 1 & 1 - 2 a & - 1 \\ 0 & - a & a ^ {2} + a & 2 a - 2 \end{array} \right) \xrightarrow {r _ {1} - r _ {2} ^ {* *}} \left( \begin{array}{c c c c} 1 & 0 & a & 1 \\ 0 & 1 & 1 - 2 a & - 1 \\ 0 & 0 & - a ^ {2} + 2 a & a - 2 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个 *.）

由上面的式子可知，<equation>r ( A ) \geqslant 2</equation>. 从而，<equation>A x=\beta</equation>无解当且仅当<equation>r ( A )=2</equation>且<equation>r ( A,\beta)=3.</equation>此时，<equation>- a^{2}+2 a=0</equation>，且 a-2<equation>\neq0</equation>，解得 a=0.

（Ⅱ）当<equation>a = 0</equation>时，<equation>A^{\mathrm{T}} = \left( \begin{array}{lll}1&1&1\\ 1&0&1\\ 1&0&1 \end{array} \right), A^{\mathrm{T}}A = \left( \begin{array}{lll}3&2&2\\ 2&2&2\\ 2&2&2 \end{array} \right), A^{\mathrm{T}}\boldsymbol {\beta} = \left( \begin{array}{c}-1\\ -2\\ -2 \end{array} \right).</equation><equation>\begin{array}{l} \left(\boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {A}, \boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {\beta}\right) = \left( \begin{array}{c c c c} 3 & 2 & 2 & - 1 \\ 2 & 2 & 2 & - 2 \\ 2 & 2 & 2 & - 2 \end{array} \right) \xrightarrow [ r _ {2} \times \frac {1}{2} ]{r _ {3} - r _ {2}} \left( \begin{array}{c c c c} 3 & 2 & 2 & - 1 \\ 1 & 1 & 1 & - 1 \\ 0 & 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {1} - 2 r _ {2} ^ {*} ]{r _ {1} - 2 r _ {2} ^ {*}} \left( \begin{array}{c c c c} 1 & 0 & 0 & 1 \\ 1 & 1 & 1 & - 1 \\ 0 & 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} - r _ {1} ^ {*}} \left( \begin{array}{c c c c} 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & - 2 \\ 0 & 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation><equation>A^{\mathrm{T}} A x=A^{\mathrm{T}} \beta</equation>对应的齐次线性方程组等价于<equation>\left\{ \begin{array}{l l} x_{1}=0, \\ x_{2}+x_{3}=0. \end{array} \right.</equation>（0，-1，1）<equation>^{\mathrm{T}}</equation>为该方程组的一个基础解系.又因为<equation>(1,-2,0)^{\mathrm{T}}</equation>是<equation>A^{\mathrm{T}} A x=A^{\mathrm{T}} \beta</equation>的一个特解，所以<equation>A^{\mathrm{T}} A x=A^{\mathrm{T}} \beta</equation>的通解为<equation>k(0,-1,1)^{\mathrm{T}}+</equation>（1，-2，0）<equation>^{\mathrm{T}}</equation>，其中k为任意常数.

---

**2015年第7题 | 选择题 | 4分 | 答案: D**
7. 设矩阵<equation>A=\left( \begin{array}{c c c} {1} & {1} & {1} \\ {1} & {2} & {a} \\ {1} & {4} & {a^{2}} \\ \end{array} \right), b=\left( \begin{array}{c} {1} \\ {d} \\ {d^{2}} \\ \end{array} \right).</equation>若集合<equation>\Omega=\{1,2\}</equation>，则线性方程组<equation>A x=b</equation>有无穷多解的充分必要条件为（    ）

A. a<equation>\notin\Omega, d\notin\Omega</equation>B. a<equation>\notin\Omega, d\in\Omega</equation>C. a<equation>\in\Omega, d\notin\Omega</equation>D. a<equation>\in\Omega, d\in\Omega</equation>
答案: D
**解析: **解（法一）当 a<equation>\in\Omega</equation>，d<equation>\in\Omega</equation>时，r（A）=r（A，b）=2<3，故 a<equation>\in\Omega</equation>，d<equation>\in\Omega</equation>是 Ax=b有无穷多解的充分条件.

当<equation>A x=b</equation>有无穷多解时，<equation>r(A)=r(A,b)<3</equation>，从而<equation>r(A)<3</equation><equation>|A|=0</equation>.由于<equation>|A|</equation>为范德蒙德行列式，故<equation>|A|=0</equation>当且仅当 a=1或 a=2，即 a<equation>\in\Omega</equation>.此时，若<equation>r(A,b)=r(A)<3</equation>，则<equation>(1,d,d^{2})^{\mathrm{T}}</equation>与<equation>(1,1,1)^{\mathrm{T}}</equation>和<equation>(1,2,4)^{\mathrm{T}}</equation>线性相关，从而<equation>\left| \begin{array}{c c c} {1} & {1} & {1} \\ {1} & {2} & {d} \\ {1} & {4} & {d^{2}} \end{array} \right|=0</equation>.再次由范德蒙德行列式的性质可推出 d=1或 d=2，即 d<equation>\in\Omega.</equation>因此，<equation>a\in \Omega</equation>，<equation>d\in \Omega</equation>是<equation>Ax = b</equation>有无穷多解的充分必要条件.应选D.

（法二）对（A，b）作初等行变换.<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 1 & 2 & a & d \\ 1 & 4 & a ^ {2} & d ^ {2} \end{array} \right) \xrightarrow [ r _ {3} - r _ {1} ]{r _ {2} - r _ {1}} \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 0 & 1 & a - 1 & d - 1 \\ 0 & 3 & a ^ {2} - 1 & d ^ {2} - 1 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {*} - 3 r _ {2} ^ {*}} \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 0 & 1 & a - 1 & d - 1 \\ 0 & 0 & a ^ {2} - 3 a + 2 & d ^ {2} - 3 d + 2 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每作一次初等行变换，加一个<equation>*.</equation>）

由此可见，<equation>r(\mathbf{A}) = r(\mathbf{A},\mathbf{b}) < 3</equation>当且仅当<equation>a^{2} - 3a + 2 = 0</equation>且<equation>d^{2} - 3d + 2 = 0</equation>，即<equation>a = 1</equation>或<equation>a = 2</equation>且<equation>d = 1</equation>或<equation>d = 2</equation>，也即<equation>a\in \Omega</equation>，<equation>d\in \Omega</equation>因此，<equation>a\in \Omega</equation>，<equation>d\in \Omega</equation>是<equation>Ax = b</equation>有无穷多解的充分必要条件.应选D.

（法三）排除法.我们可以把简单的值代入各选项，然后根据<equation>A x=b</equation>是否有无穷多解来排除错误选项.

选项A：代入<equation>a=0</equation>，<equation>d=0</equation>，<equation>r(\mathbf{A})=r(\mathbf{A},\mathbf{b})=3</equation>，不符合题意.

选项B：代入<equation>a=0</equation><equation>d\in\{1,2\}</equation><equation>r(A)=r(A,b)=3</equation>，不符合题意.

选项C：代入<equation>a\in\{1,2\}</equation>，<equation>d=0</equation>，<equation>r(\mathbf{A},\mathbf{b})=3</equation>，<equation>r(\mathbf{A})=2</equation>，不符合题意.

由上可见，选项A、B、C均不是正确选项.由排除法知，应选D.

---

**2014年第22题 | 解答题 | 11分**
22. （本题满分11分）

设矩阵<equation>A = \left( \begin{array}{c c c c} 1 & -2 & 3 & -4 \\ 0 & 1 & -1 & 1 \\ 1 & 2 & 0 & -3 \end{array} \right), E</equation>为3阶单位矩阵.

I. 求方程组<equation>A x=0</equation>的一个基础解系；

II. 求满足<equation>A B=E</equation>的所有矩阵 B.
**答案: **(22) ( I )<equation>(-1, 2, 3, 1)^{\mathrm{T}};</equation><equation>(\mathrm {I I}) \boldsymbol {B} = \left( \begin{array}{c c c} 2 - k _ {1} & 6 - k _ {2} & - 1 - k _ {3} \\ - 1 + 2 k _ {1} & - 3 + 2 k _ {2} & 1 + 2 k _ {3} \\ - 1 + 3 k _ {1} & - 4 + 3 k _ {2} & 1 + 3 k _ {3} \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right), \text {其 中} k _ {1}, k _ {2}, k _ {3} \text {为 任 意 常 数}</equation>
**解析: **解（I）考察系数矩阵 A.<equation>\begin{array}{l} \boldsymbol {A} = \left( \begin{array}{c c c c} 1 & - 2 & 3 & - 4 \\ 0 & 1 & - 1 & 1 \\ 1 & 2 & 0 & - 3 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c c} 1 & - 2 & 3 & - 4 \\ 0 & 1 & - 1 & 1 \\ 0 & 4 & - 3 & 1 \end{array} \right) \xrightarrow {r _ {1} + 2 r _ {2}} \left( \begin{array}{c c c c} 1 & 0 & 1 & - 2 \\ 0 & 1 & - 1 & 1 \\ 0 & 0 & 1 & - 3 \end{array} \right) \\ \xrightarrow {r _ {1} ^ {*} - r _ {3} ^ {* *}} \frac {1}{r _ {2} + r _ {3} ^ {* *}} \left( \begin{array}{c c c c} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & - 2 \\ 0 & 0 & 1 & - 3 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每作一次初等行变换，加一个 *.）<equation>Ax = 0</equation>可化为方程组<equation>\left\{ \begin{array}{l} x_{1} + x_{4} = 0, \\ x_{2} - 2x_{4} = 0, \\ x_{3} - 3x_{4} = 0. \end{array} \right.</equation>由此可得<equation>\xi = (-1,2,3,1)^{\mathrm{T}}</equation>为<equation>Ax = 0</equation>的一个基础解系.

（Ⅱ）实际上我们要求的是三个非齐次线性方程组<equation>A x=(1,0,0)^{\mathrm{T}}</equation>，<equation>A x=(0,1,0)^{\mathrm{T}}</equation>，<equation>A x=(0,0,1)^{\mathrm{T}}</equation>的解.由于它们的系数矩阵都是A，故可考虑对（A，E）作初等行变换，同第（I）问中的步骤可得<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {E}) = \left( \begin{array}{c c c c c c c} 1 & - 2 & 3 & - 4 & 1 & 0 & 0 \\ 0 & 1 & - 1 & 1 & 0 & 1 & 0 \\ 1 & 2 & 0 & - 3 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c c c c c} 1 & - 2 & 3 & - 4 & 1 & 0 & 0 \\ 0 & 1 & - 1 & 1 & 0 & 1 & 0 \\ 0 & 4 & - 3 & 1 & - 1 & 0 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} + 2 r _ {2}} \frac {r _ {1} ^ {*} - 4 r _ {2}}{r _ {3} ^ {*} - 4 r _ {2}} \left( \begin{array}{c c c c c c c} 1 & 0 & 1 & - 2 & 1 & 2 & 0 \\ 0 & 1 & - 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & 1 & - 3 & - 1 & - 4 & 1 \end{array} \right) \xrightarrow {r _ {1} ^ {*} - r _ {3} ^ {* *}} \left( \begin{array}{c c c c c c c} 1 & 0 & 0 & 1 & 2 & 6 & - 1 \\ 0 & 1 & 0 & - 2 & - 1 & - 3 & 1 \\ 0 & 0 & 1 & - 3 & - 1 & - 4 & 1 \end{array} \right). \\ \end{array}</equation>由于<equation>\mathbf{A}</equation>为<equation>3\times4</equation>矩阵，<equation>\mathbf{E}</equation>为3阶单位矩阵，<equation>\mathbf{B}</equation>应为<equation>4\times3</equation>矩阵，从而知，<equation>(2,-1,-1,0)^{\mathrm{T}}</equation><equation>(6,-3,-4,0)^{\mathrm{T}}</equation><equation>(-1,1,1,0)^{\mathrm{T}}</equation>分别为<equation>A x=(1,0,0)^{\mathrm{T}}</equation><equation>A x=(0,1,0)^{\mathrm{T}}</equation><equation>A x=(0,0,1)^{\mathrm{T}}</equation>的一个特解.

与第（I）问中<equation>A x=0</equation>的通解相结合，得到<equation>A x=(1,0,0)^{\mathrm{T}}</equation><equation>A x=(0,1,0)^{\mathrm{T}}</equation><equation>A x=(0,0,1)^{\mathrm{T}}</equation>的通解分别为<equation>\boldsymbol {\alpha} _ {1} = k _ {1} \left(- 1, 2, 3, 1\right) ^ {\mathrm {T}} + \left(2, - 1, - 1, 0\right) ^ {\mathrm {T}},</equation><equation>\boldsymbol {\alpha} _ {2} = k _ {2} \left(- 1, 2, 3, 1\right) ^ {\mathrm {T}} + \left(6, - 3, - 4, 0\right) ^ {\mathrm {T}},</equation><equation>\boldsymbol {\alpha} _ {3} = k _ {3} (- 1, 2, 3, 1) ^ {\mathrm {T}} + (- 1, 1, 1, 0) ^ {\mathrm {T}},</equation>其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数.

因此，<equation>B = \left( \begin{array}{c c c} 2 - k_1 & 6 - k_2 & -1 - k_3 \\ -1 + 2k_1 & -3 + 2k_2 & 1 + 2k_3 \\ -1 + 3k_1 & -4 + 3k_2 & 1 + 3k_3 \\ k_1 & k_2 & k_3 \end{array} \right)</equation>，其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数.

---

**2013年第22题 | 解答题 | 11分**
22. (本题满分11分)

设<equation>A = \left( \begin{array}{c c} 1 & a \\ 1 & 0 \end{array} \right), B = \left( \begin{array}{c c} 0 & 1 \\ 1 & b \end{array} \right).</equation>当<equation>a,b</equation>为何值时，存在矩阵<equation>C</equation>使得<equation>AC - CA = B</equation>，并求所有矩阵<equation>C</equation>
**答案: **(22)<equation>a=-1,b=0</equation>时，<equation>C=\left( \begin{array}{c c} k_{1}+k_{2}+1 & -k_{2} \\ k_{2} & k_{1} \end{array} \right)</equation>其中<equation>k_{1},k_{2}</equation>为任意常数.
**解析: **解（法一）设<equation>C=\left( \begin{array}{cc}x_{1}&x_{2}\\ x_{3}&x_{4}\end{array} \right)</equation>，则由AC-CA=B可得<equation>\binom {1} {1} \begin{array}{l l} a \\ 0 \end{array} \binom {x _ {1}} {x _ {3}} \begin{array}{l l} x _ {2} \\ x _ {4} \end{array} - \binom {x _ {1}} {x _ {3}} \begin{array}{l l} x _ {2} \\ x _ {4} \end{array} \binom {1} {1} \begin{array}{l l} a \\ 0 \end{array} = \binom {0} {1} \binom {1} {b}.</equation>写成线性方程组的形式：<equation>\left\{ \begin{array}{l} - x _ {2} + a x _ {3} = 0, \\ - a x _ {1} + x _ {2} + a x _ {4} = 1, \\ x _ {1} - x _ {3} - x _ {4} = 1, \\ x _ {2} - a x _ {3} = b. \end{array} \right.</equation>记该线性方程组为<equation>Px = \beta ,\beta = (0,1,1,b)^{\mathrm{T}}</equation>，则<equation>Px = \beta</equation>有解当且仅当<equation>r(P,\beta) = r(P)</equation>.<equation>\begin{array}{l} (P, \beta) = \left( \begin{array}{c c c c c} 0 & - 1 & a & 0 & 0 \\ - a & 1 & 0 & a & 1 \\ 1 & 0 & - 1 & - 1 & 1 \\ 0 & 1 & - a & 0 & b \end{array} \right) \xrightarrow {r _ {2} + a r _ {3}} \left( \begin{array}{c c c c c} 0 & - 1 & a & 0 & 0 \\ 0 & 1 & - a & 0 & a + 1 \\ 1 & 0 & - 1 & - 1 & 1 \\ 0 & 1 & - a & 0 & b \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} + r _ {1}} \left( \begin{array}{c c c c c} 0 & - 1 & a & 0 & 0 \\ 0 & 0 & 0 & 0 & a + 1 \\ 1 & 0 & - 1 & - 1 & 1 \\ 0 & 0 & 0 & 0 & b \end{array} \right) \rightarrow \left( \begin{array}{c c c c c} 1 & 0 & - 1 & - 1 & 1 \\ 0 & 1 & - a & 0 & 0 \\ 0 & 0 & 0 & 0 & a + 1 \\ 0 & 0 & 0 & 0 & b \end{array} \right). \\ \end{array}</equation><equation>r_{2}^{*}</equation>表示对<equation>r_{2}</equation>作初等行变换后所得新的第二行.由上可见，若<equation>r ( \boldsymbol{P}, \boldsymbol{\beta})=r ( \boldsymbol{P})</equation>，则必有<equation>a+1=b=0</equation>从而<equation>a=-1,b=0.</equation>当 a = -1，b = 0时，<equation>(\boldsymbol {P}, \boldsymbol {\beta}) \rightarrow \left(\begin{array}{c c c c c}1&0&- 1&- 1&1\\0&1&1&0&0\\0&0&0&0&0\\0&0&0&0&0\end{array}\right),</equation>即<equation>\left\{ \begin{array}{l l} x_{2}+x_{3}=0, \\ x_{1}-x_{3}-x_{4}=1. \end{array} \right.</equation>（1，0，0，1）<equation>^{\mathrm{T}}</equation>和（1，-1，1，0）<equation>^{\mathrm{T}}</equation>为该方程组对应的齐次线性方程组的一个基础解系.又（1，0，0，0）<equation>^{\mathrm{T}}</equation>为<equation>P x=\beta</equation>的一个特解，故<equation>P x=\beta</equation>的通解为<equation>k _ {1} \left(1, 0, 0, 1\right) ^ {\mathrm {T}} + k _ {2} \left(1, - 1, 1, 0\right) ^ {\mathrm {T}} + \left(1, 0, 0, 0\right) ^ {\mathrm {T}},</equation>其中<equation>k_{1}, k_{2}</equation>为任意常数.

因此，当<equation>a = -1</equation>，<equation>b = 0</equation>时，存在C使得AC-CA=B.此时的C形如<equation>\left( \begin{array}{c c} k_{1}+k_{2}+1 & -k_{2} \\ k_{2} & k_{1} \end{array} \right)</equation>其中<equation>k_{1}, k_{2}</equation>为任意常数.

（法二）由于AC的迹等于CA的迹，故AC-CA的迹等于零.因此 b=0. B =<equation>\left( \begin{array}{c c} 0 & 1 \\ 1 & 0 \end{array} \right).</equation>设 C =<equation>\left( \begin{array}{c c} x_{1} & x_{2} \\ x_{3} & x_{4} \end{array} \right)</equation>，则由 AC-CA=B可得<equation>\left\{ \begin{array}{l} - x _ {2} + a x _ {3} = 0, \\ - a x _ {1} + x _ {2} + a x _ {4} = 1, \\ x _ {1} - x _ {3} - x _ {4} = 1, \\ x _ {2} - a x _ {3} = 0. \end{array} \right.</equation>将<equation>x_{2}=a x_{3}</equation>代入<equation>- a x_{1}+x_{2}+a x_{4}=1</equation>可得<equation>- a \left(x_{1}-x_{3}-x_{4}\right)=1.</equation>与<equation>x_{1}-x_{3}-x_{4}=1</equation>比较得，<equation>a=-1.</equation>从而<equation>a=-1</equation>，<equation>b=0.</equation>其余同法一.

---

**2012年第22题 | 解答题 | 11分**
22. （本题满分11分）

设<equation>\text {设} A = \left( \begin{array}{c c c c} 1 & a & 0 & 0 \\ 0 & 1 & a & 0 \\ 0 & 0 & 1 & a \\ a & 0 & 0 & 1 \end{array} \right), \beta = \left( \begin{array}{c} 1 \\ - 1 \\ 0 \\ 0 \end{array} \right).</equation>I. 计算行列式<equation>|A|</equation>;

II. 当实数<equation>a</equation>为何值时，方程组<equation>Ax = \beta</equation>有无穷多解，并求其通解.
**答案: **（22）（I）<equation>| A |=1-a^{4}</equation>；

（Ⅱ）当 a=-1时，方程组<equation>A x=\beta</equation>有无穷多解，其通解为<equation>k(1,1,1,1)^{\mathrm{T}}+(0,-1,0,0)^{\mathrm{T}}</equation>其中 k为任意常数.
**解析: **（I）按第一行展开<equation>|A|</equation>，得<equation>| \boldsymbol {A} | = \left| \begin{array}{c c c} 1 & a & 0 \\ 0 & 1 & a \\ 0 & 0 & 1 \end{array} \right| - a \left| \begin{array}{c c c} 0 & a & 0 \\ 0 & 1 & a \\ a & 0 & 1 \end{array} \right| = 1 - a ^ {4}.</equation>（Ⅱ）（法一）<equation>A x=\beta</equation>有无穷多解的充要条件为<equation>r(A)=r(A,\beta)<4.</equation>由<equation>r(A)<4</equation>可得，<equation>|A|=0</equation>从而<equation>a=\pm 1.</equation>当 a = 1时，<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 1 & 0 & 0 & 1 & 0 \end{array} \right) \xrightarrow {r _ {4} - r _ {1}} \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & - 1 & 0 & 1 & - 1 \end{array} \right) \xrightarrow {r _ {4} ^ {*} + r _ {2}} \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1 & - 2 \end{array} \right) \\ \xrightarrow {r _ {4} ^ {* *} - r _ {3}} \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 & - 2 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每作一次初等行变换，加一个 *.）由上可知，<equation>r(\mathbf{A},\boldsymbol{\beta})=4</equation>，而<equation>r(\mathbf{A})=3</equation>，<equation>\mathbf{Ax}=\boldsymbol{\beta}</equation>无解. a=1不符合题意.

当 a = -1时，<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 1 & - 1 & 0 & 0 & 1 \\ 0 & 1 & - 1 & 0 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ - 1 & 0 & 0 & 1 & 0 \end{array} \right) \xrightarrow {r _ {4} + r _ {1}} \left( \begin{array}{c c c c c} 1 & - 1 & 0 & 0 & 1 \\ 0 & 1 & - 1 & 0 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ 0 & - 1 & 0 & 1 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} + r _ {2}} \frac {r _ {4} ^ {*} + r _ {2}} {r _ {4} ^ {*} + r _ {2}} \left( \begin{array}{c c c c c} 1 & 0 & - 1 & 0 & 0 \\ 0 & 1 & - 1 & 0 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ 0 & 0 & - 1 & 1 & 0 \end{array} \right) \xrightarrow {r _ {1} ^ {*} + r _ {3}} \frac {r _ {2} + r _ {3}}{r _ {4} ^ {* *} + r _ {3}} \left( \begin{array}{c c c c c} 1 & 0 & 0 & - 1 & 0 \\ 0 & 1 & 0 & - 1 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>由上可知，<equation>r(\mathbf{A},\boldsymbol{\beta})=r(\mathbf{A})=3<4, A\boldsymbol{x}=\boldsymbol{\beta}</equation>有无穷多解.

齐次方程<equation>A x=0</equation>的通解为<equation>k ( 1,1,1,1 )^{\mathrm{T}}</equation>，其中<equation>k</equation>为任意常数。又因为<equation>( 0,-1,0,0 )^{\mathrm{T}}</equation>为<equation>A x=\beta</equation>的一个特解，所以<equation>A x=\beta</equation>的通解为<equation>k ( 1,1,1,1 )^{\mathrm{T}}+( 0,-1,0,0 )^{\mathrm{T}}</equation>，其中<equation>k</equation>为任意常数综上所述，当<equation>a=-1</equation>时，方程组<equation>A x=\beta</equation>有无穷多解，其通解为<equation>k ( 1,1,1,1 )^{\mathrm{T}}+( 0,-1,0,0 )^{\mathrm{T}}</equation>其中<equation>k</equation>为任意常数.

（法二）对含有参数<equation>a</equation>的增广矩阵<equation>(A, \beta)</equation>作初等行变换.<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ a & 0 & 0 & 1 & 0 \end{array} \right) \xrightarrow {r _ {4} - a r _ {1}} \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ 0 & - a ^ {2} & 0 & 1 & - a \end{array} \right) \\ \xrightarrow {r _ {4} ^ {*} + a ^ {2} r _ {2}} \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ 0 & 0 & a ^ {3} & 1 & - a - a ^ {2} \end{array} \right) \xrightarrow {r _ {4} ^ {* *} - a ^ {3} r _ {3}} \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ 0 & 0 & 0 & 1 - a ^ {4} & - a - a ^ {2} \end{array} \right). \\ \end{array}</equation>由于<equation>A x=\beta</equation>有无穷多解，故<equation>r(A)=r(A,\beta)<4.</equation>因此，<equation>1-a^{4}=0,-a-a^{2}=0</equation>解得 a=-1其余同法一.

---

**2010年第22题 | 解答题 | 11分**
22. (本题满分11分)

设<equation>A=\left( \begin{array}{c c c} \lambda & 1 & 1 \\ 0 & \lambda-1 & 0 \\ 1 & 1 & \lambda \end{array} \right), b=\left( \begin{array}{c} a \\ 1 \\ 1 \end{array} \right).</equation>已知线性方程组<equation>A x=b</equation>存在两个不同的解.

I. 求<equation>\lambda, a;</equation>II. 求方程组<equation>A x=b</equation>的通解.
**答案: **(22) （I）<equation>\lambda=-1</equation><equation>a=-2;</equation>（Ⅱ）<equation>k(1,0,1)^{\mathrm{T}}+\left(\frac{3}{2},-\frac{1}{2},0\right)^{\mathrm{T}}</equation>为<equation>A x=b</equation>的通解，其中k为任意常数.
**解析: **解（I）<equation>A x=b</equation>有两个不同的解意味着<equation>A x=b</equation>有解但不唯一，故<equation>r(A)=r(A,b)<3.</equation><equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} \lambda & 1 & 1 & a \\ 0 & \lambda - 1 & 0 & 1 \\ 1 & 1 & \lambda & 1 \end{array} \right) \xrightarrow {r _ {1} \leftrightarrow r _ {3}} \left( \begin{array}{c c c c} 1 & 1 & \lambda & 1 \\ 0 & \lambda - 1 & 0 & 1 \\ \lambda & 1 & 1 & a \end{array} \right) \xrightarrow {r _ {3} ^ {*} - \lambda r _ {1} ^ {*}} \left( \begin{array}{c c c c} 1 & 1 & \lambda & 1 \\ 0 & \lambda - 1 & 0 & 1 \\ 0 & 1 - \lambda & 1 - \lambda^ {2} & a - \lambda \end{array} \right) \\ \xrightarrow {r _ {3} ^ {* *} + r _ {2}} \left( \begin{array}{c c c c} 1 & 1 & \lambda & 1 \\ 0 & \lambda - 1 & 0 & 1 \\ 0 & 0 & 1 - \lambda^ {2} & a - \lambda + 1 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每做一次初等行变换，加一个 *.）

由于<equation>r(A) < 3</equation>，故<equation>1 - \lambda^2 = 0, \lambda = \pm 1.</equation>当<equation>\lambda = 1</equation>时，<equation>r(A,b) = 2,r(A) = 1</equation>，方程组无解，舍去.

当<equation>\lambda=-1</equation>时，<equation>(\mathbf{A},\mathbf{b})\rightarrow\left( \begin{array}{c c c c}1&1&-1&1\\0&-2&0&1\\0&0&0&a+2 \end{array} \right).</equation>此时<equation>r(\mathbf{A})=2.</equation>若<equation>r(\mathbf{A})=r(\mathbf{A},\mathbf{b})</equation>，则<equation>r(\mathbf{A},\mathbf{b})=2, a+2=0</equation>即<equation>a=-2.</equation>（Ⅱ）由第（I）问知，当<equation>\lambda=-1</equation>a=-2时，<equation>(\boldsymbol {A}, \boldsymbol {b}) \rightarrow \left(\begin{array}{c c c c}1&1&- 1&1\\0&- 2&0&1\\0&0&0&0\end{array}\right) \xrightarrow [ r _ {1} - r _ {2} ^ {*} ]{r _ {2} \times \left(- \frac {1}{2}\right)} \left(\begin{array}{c c c c}1&0&- 1&\frac {3}{2}\\\0&1&0&- \frac {1}{2}\\\0&0&0&0\end{array}\right).</equation>其对应的齐次方程组等价于<equation>\left\{\begin{array}{l l}x_{1}-x_{3}=0,\\ x_{2}=0,\end{array}\right.</equation>故可取<equation>(1,0,1)^{\mathrm{T}}</equation>为该方程组的一个基础解系.又<equation>\left(\frac{3}{2},-\frac{1}{2},0\right)^{\mathrm{T}}</equation>为原方程组的一个特解，故<equation>A x=b</equation>的通解为<equation>k(1,0,1)^{\mathrm{T}}+\left(\frac{3}{2},-\frac{1}{2},0\right)^{\mathrm{T}}</equation>其中k为任意常数.

---


### 向量


#### 向量组的线性相关性

**2024年第16题 | 填空题 | 5分**
16. 设向量<equation>\alpha_{1}=\left( \begin{array}{c} a \\ 1 \\ -1 \\ 1 \end{array} \right),\alpha_{2}=\left( \begin{array}{c} 1 \\ 1 \\ b \\ a \end{array} \right),\alpha_{3}=\left( \begin{array}{c} 1 \\ a \\ -1 \\ 1 \end{array} \right)</equation>若<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性相关，且其中任意两个向量均线性无关，则

ab = ___
**答案: **```latex
-4
```

**解析:**解（法一）由于<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性相关，故该向量组的秩小于3，从而<equation>r(\alpha_{1},\alpha_{2},\alpha_{3})\leqslant 2.</equation>又因为该向量组中任意两个向量均线性无关，所以该向量组的秩不小于2，从而<equation>r(\alpha_{1},\alpha_{2},\alpha_{3})\geqslant 2.</equation>于是，<equation>r(\alpha_{1},\alpha_{2},\alpha_{3})=2.</equation>由<equation>r(\alpha_{1},\alpha_{2},\alpha_{3}) = 2</equation>可得，矩阵<equation>(\alpha_{1},\alpha_{2},\alpha_{3})</equation>的任意一个3阶子式均为0.于是，<equation>\begin{aligned} \left| \begin{array}{l l l} a & 1 & 1 \\ 1 & 1 & a \\ 1 & a & 1  \right| \xlongequal {c _ {1} + c _ {2} + c _ {3}} \left| \begin{array}{l l l} a + 2 & 1 & 1 \\ a + 2 & 1 & a \\ a + 2 & a & 1  \right| &= (a + 2) \left| \begin{array}{l l l} 1 & 1 & 1 \\ 1 & 1 & a \\ 1 & a & 1  \right| &= (a + 2) \left| \begin{array}{l l l} 1 & 0 & 0 \\ 1 & 0 & a - 1 \\ 1 & a - 1 & 0  \right| \\ &= - (a + 2) (a - 1) ^ {2} = 0. \end{aligned}</equation>由此可得 a=-2或a=1. 但是当 a=1时，<equation>\alpha_{1}=\alpha_{3}</equation>，从而<equation>\alpha_{1},\alpha_{3}</equation>线性相关，不符合题意.于是，a=-2.

代入<equation>a = -2</equation>，再由矩阵<equation>(\alpha_{1},\alpha_{2},\alpha_{3})</equation>的任意一个3阶子式均为0可得<equation>\left| \begin{array}{c c c} 1 & 1 & - 2 \\ - 1 & b & - 1 \\ 1 & - 2 & 1 \end{array} \right| \frac {c _ {2} - c _ {1}}{c _ {3} + 2 c _ {1}} \left| \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & b + 1 & - 3 \\ 1 & - 3 & 3 \end{array} \right| = 3 (b + 1) - 9 = 0.</equation>解得 b=2.

因此，<equation>a=-2,b=2,ab=-4.</equation>（法二）同法一可得<equation>r(\alpha_{1},\alpha_{2},\alpha_{3}) = 2.</equation>对矩阵<equation>(\alpha_{1},\alpha_{2},\alpha_{3})</equation>作初等行变换.<equation>\begin{array}{l} \left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) = \left( \begin{array}{c c c} a & 1 & 1 \\ 1 & 1 & a \\ - 1 & b & - 1 \\ 1 & a & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & a \\ 1 & a & 1 \\ - 1 & b & - 1 \\ a & 1 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & a \\ 0 & a - 1 & 1 - a \\ 0 & b + 1 & a - 1 \\ 0 & 1 - a & 1 - a ^ {2} \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c} 1 & 1 & a \\ 0 & a - 1 & 1 - a \\ 0 & b + 1 & a - 1 \\ 0 & 0 & 2 - a - a ^ {2} \end{array} \right). \\ \end{array}</equation>当<equation>a = -2</equation>或<equation>a = 1</equation>时，<equation>2 - a - a^{2} = -(a + 2)(a - 1) = 0.</equation>当 a =1时，<equation>\left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) \rightarrow \left(\begin{array}{c c c}1&1&1\\0&0&0\\0&b + 1&0\\0&0&0\end{array}\right)\rightarrow \left(\begin{array}{c c c}1&1&1\\0&b + 1&0\\0&0&0\\0&0&0\end{array}\right).</equation>由此可得<equation>\alpha_{1},\alpha_{3}</equation>线性相关，不符合题意.

当 a = -2时，<equation>\left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right)\rightarrow \left(\begin{array}{c c c}1&1&- 2\\0&- 3&3\\0&b + 1&- 3\\0&0&0\end{array}\right)\rightarrow \left(\begin{array}{c c c}1&1&- 2\\0&1&- 1\\0&b - 2&0\\0&0&0\end{array}\right).</equation>由<equation>r(\alpha_{1},\alpha_{2},\alpha_{3}) = 2</equation>可得<equation>b - 2 = 0</equation>，即<equation>b = 2</equation>因此，<equation>a=-2,b=2,ab=-4.</equation>

---

**2014年第8题 | 选择题 | 4分 | 答案: A**

8. 设<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>均为3维向量，则对任意常数 k,l，向量组<equation>\alpha_{1}+k\alpha_{3},\alpha_{2}+l\alpha_{3}</equation>线性无关是向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关的（    )

A. 必要非充分条件 B. 充分非必要条件

C. 充分必要条件 D. 既非充分也非必要条件

答案: A

**解析:**假设<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性无关.考虑向量组<equation>\boldsymbol{\alpha}_{1}+k\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{2}+l\boldsymbol{\alpha}_{3}.</equation>由于<equation>a\left(\boldsymbol{\alpha}_{1} + k\boldsymbol{\alpha}_{3}\right) + b\left(\boldsymbol{\alpha}_{2} + l\boldsymbol{\alpha}_{3}\right) = a\boldsymbol{\alpha}_{1} + b\boldsymbol{\alpha}_{2} + (ak + bl)\boldsymbol{\alpha}_{3} = 0</equation>，故由<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性无关可知，<equation>a=b=ak+bl=0.</equation>因此，<equation>\boldsymbol{\alpha}_{1} + k\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{2} + l\boldsymbol{\alpha}_{3}</equation>线性无关.向量组<equation>\boldsymbol{\alpha}_{1} + k\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{2} + l\boldsymbol{\alpha}_{3}</equation>线性无关是向量组<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性无关的必要条件.

但是向量组<equation>\boldsymbol{\alpha}_{1}+k\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{2}+l\boldsymbol{\alpha}_{3}</equation>线性无关不是向量组<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性无关的充分条件.

下面我们给出反例.令<equation>\alpha_{1},\alpha_{2}</equation>线性无关，而<equation>\alpha_{3}=0</equation>，则此时<equation>\alpha_{1}+k\alpha_{3}=\alpha_{1},\alpha_{2}+l\alpha_{3}=\alpha_{2}</equation>线性无关.对任意非零常数k，有<equation>0\alpha_{1}+0\alpha_{2}+k\alpha_{3}=0</equation>，从而<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性相关.

因此，<equation>\alpha_{1} + k\alpha_{3},\alpha_{2} + l\alpha_{3}</equation>线性无关是向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关的必要非充分条件.应选A.

---

**2012年第7题 | 选择题 | 4分 | 答案: C**

7. 设<equation>\alpha_{1}=\left( \begin{array}{c}0\\ 0\\ c_{1}\end{array} \right),\alpha_{2}=\left( \begin{array}{c}0\\ 1\\ c_{2}\end{array} \right),\alpha_{3}=\left( \begin{array}{c}1\\ -1\\ c_{3}\end{array} \right),\alpha_{4}=\left( \begin{array}{c}-1\\ 1\\ c_{4}\end{array} \right),</equation>其中<equation>c_{1},c_{2},c_{3},c_{4}</equation>为任意常数，则下列向量组线性相关

为（    ）

A.<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>B.<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>C.<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>D.<equation>\alpha_{2},\alpha_{3},\alpha_{4}</equation>

答案: C

**解析:**解（法一）由题设可得，<equation>\alpha_{3} + \alpha_{4} = \left( \begin{array}{c} 0 \\ 0 \\ c_{3} + c_{4} \end{array} \right),\alpha_{1} = \left( \begin{array}{c} 0 \\ 0 \\ c_{1} \end{array} \right).</equation>当<equation>c_{3} + c_{4}\neq 0</equation>时，<equation>\boldsymbol{\alpha}_{1} = \frac{c_{1}}{c_{3} + c_{4}} \left( \boldsymbol{\alpha}_{3} + \boldsymbol{\alpha}_{4} \right), \boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{3}, \boldsymbol{\alpha}_{4}</equation>线性相关；当<equation>c_{3} + c_{4} = 0</equation>时，<equation>\boldsymbol{\alpha}_{3} + \boldsymbol{\alpha}_{4} = 0</equation><equation>\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}</equation>线性相关.从而<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}</equation>线性相关.

综上所述，<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>线性相关，应选C.

（法二）由于<equation>n</equation>个<equation>n</equation>维列向量<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{n}</equation>线性相关等价于<equation>|\alpha_{1},\alpha_{2},\dots ,\alpha_{n}| = 0</equation>，而<equation>\left| \alpha_ {1}, \alpha_ {3}, \alpha_ {4} \right| = \left| \begin{array}{c c c} 0 & 1 & - 1 \\ 0 & - 1 & 1 \\ c _ {1} & c _ {3} & c _ {4} \end{array} \right| = c _ {1} \left| \begin{array}{c c} 1 & - 1 \\ - 1 & 1 \end{array} \right| = 0,</equation>故<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>线性相关.应选C.

同理可计算其他选项中的3个向量组成的矩阵的行列式，可知它们均不恒为零

---


#### 向量组之间的线性表示

**2023年第10题 | 选择题 | 5分 | 答案: D**

10. 已知向量<equation>\alpha_{1}=\left( \begin{array}{c}1\\ 2\\ 3 \end{array} \right),\alpha_{2}=\left( \begin{array}{c}2\\ 1\\ 1 \end{array} \right),\beta_{1}=\left( \begin{array}{c}2\\ 5\\ 9 \end{array} \right),\beta_{2}=\left( \begin{array}{c}1\\ 0\\ 1 \end{array} \right)</equation>若<equation>\gamma</equation>既可由<equation>\alpha_{1},\alpha_{2}</equation>线性表示，也可由<equation>\beta_{1},\beta_{2}</equation>线性表示，则<equation>\gamma=(\quad)</equation>A. k<equation>\left( \begin{array}{c}3\\ 3\\ 4 \end{array} \right),k \in \mathbf{R}</equation>B. k<equation>\left( \begin{array}{c}3\\ 5\\ 10 \end{array} \right),k \in \mathbf{R}</equation>C. k<equation>\left( \begin{array}{c}-1\\ 1\\ 2 \end{array} \right),k \in \mathbf{R}</equation>D. k<equation>\left( \begin{array}{c}1\\ 5\\ 8 \end{array} \right),k \in \mathbf{R}</equation>

答案: D

**解析:**解 由于<equation>\boldsymbol{\gamma}</equation>既可由<equation>\alpha_{1},\alpha_{2}</equation>线性表示，也可由<equation>\beta_{1},\beta_{2}</equation>线性表示，故存在<equation>k_{1},k_{2},l_{1},l_{2}</equation>，使得<equation>\boldsymbol{\gamma}=k_{1}\boldsymbol{\alpha}_{1}</equation><equation>+ k_{2}\boldsymbol{\alpha}_{2}=l_{1}\boldsymbol{\beta}_{1}+l_{2}\boldsymbol{\beta}_{2}</equation>.于是，<equation>\left(k_{1},-l_{1},k_{2},-l_{2}\right)^{\mathrm{T}}</equation>是齐次线性方程组<equation>\left(\alpha_{1},\beta_{1},\alpha_{2},\beta_{2}\right)\boldsymbol{x}=\mathbf{0}</equation>的解.

记<equation>A=(\alpha_{1},\beta_{1},\alpha_{2},\beta_{2})</equation>，对A作初等行变换.

---<equation>\begin{array}{l} \boldsymbol {A} = \left( \begin{array}{c c c c} 1 & 2 & 2 & 1 \\ 2 & 5 & 1 & 0 \\ 3 & 9 & 1 & 1 \end{array} \right) \xrightarrow [ r _ {3} - 3 r _ {1} ]{r _ {2} - 2 r _ {1}} \left( \begin{array}{c c c c} 1 & 2 & 2 & 1 \\ 0 & 1 & - 3 & - 2 \\ 0 & 3 & - 5 & - 2 \end{array} \right) \xrightarrow [ r _ {3} ^ {*} - 3 r _ {2} ^ {*} ]{r _ {1} - 2 r _ {2} ^ {*}} \left( \begin{array}{c c c c} 1 & 0 & 8 & 5 \\ 0 & 1 & - 3 & - 2 \\ 0 & 0 & 4 & 4 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {* *} \times \frac {1}{4}} \left( \begin{array}{c c c c} 1 & 0 & 8 & 5 \\ 0 & 1 & - 3 & - 2 \\ 0 & 0 & 1 & 1 \end{array} \right) \xrightarrow {r _ {1} ^ {*} - 8 r _ {3} ^ {* * *}} \left( \begin{array}{c c c c} 1 & 0 & 0 & - 3 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 \end{array} \right). \\ \end{array}</equation>（<equation>r_{t}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

取<equation>x_{4}=1</equation>，可得<equation>\boldsymbol{\xi}=(3,-1,-1,1)^{\mathrm{T}}</equation>为该方程组的一个基础解系，从而<equation>\left(k_{1},-l_{1},k_{2},-l_{2}\right)^{\mathrm{T}}= k \left(3,-1,-1,1\right)^{\mathrm{T}}</equation>，其中<equation>k \in \mathbf{R}.</equation>因此，<equation>\gamma = k _ {1} \alpha_ {1} + k _ {2} \alpha_ {2} = 3 k \binom {1} {2} - k \binom {2} {1} = k \binom {1} {5}, \quad k \in \mathbf {R}.</equation>应选 D.

---

**2022年第10题 | 选择题 | 5分 | 答案: C**

10. 设<equation>\alpha_{1}=(\lambda,1,1)^{\mathrm{T}},\alpha_{2}=(1,\lambda,1)^{\mathrm{T}},\alpha_{3}=(1,1,\lambda)^{\mathrm{T}},\alpha_{4}=(1,\lambda, \lambda^{2})^{\mathrm{T}}</equation>，若<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>等价，则<equation>\lambda</equation>的取值范围是（    ）

A.<equation>\{0,1\}</equation>B.<equation>\{\lambda \mid \lambda \in \mathbf{R},\lambda \neq -2\}</equation>C.<equation>\{\lambda \mid \lambda \in \mathbf{R},\lambda \neq -1,\lambda \neq -2\}</equation>D.<equation>\{\lambda \mid \lambda \in \mathbf{R},\lambda \neq -1\}</equation>

答案: C

**解析:**解（法一）当<equation>\lambda=1</equation>时，<equation>\alpha_{1}=\alpha_{2}=\alpha_{3}=\alpha_{4}=\left( \begin{array}{c}1\\ 1\\ 1 \end{array} \right).</equation>此时<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>显然等价当<equation>\lambda\neq1</equation>时，考虑矩阵<equation>A=(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4}).</equation><equation>\begin{array}{l} A = \left( \begin{array}{c c c c} \lambda & 1 & 1 & 1 \\ 1 & \lambda & 1 & \lambda \\ 1 & 1 & \lambda & \lambda^ {2} \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 1 & 1 & \lambda & \lambda^ {2} \\ \lambda & 1 & 1 & 1 \end{array} \right) \xrightarrow {r _ {2} - r _ {1}} \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 0 & 1 - \lambda & \lambda - 1 & \lambda^ {2} - \lambda \\ 0 & 1 - \lambda^ {2} & 1 - \lambda & 1 - \lambda^ {2} \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} \times \frac {1}{1 - \lambda}} \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 0 & 1 & - 1 & - \lambda \\ 0 & 1 + \lambda & 1 & 1 + \lambda \end{array} \right) \xrightarrow {r _ {3} ^ {* *} - (1 + \lambda) r _ {2} ^ {* *}} \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 0 & 1 & - 1 & - \lambda \\ 0 & 0 & \lambda + 2 & (\lambda + 1) ^ {2} \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

由于 A有2阶非零子式<equation>\left| \begin{array}{ll} \lambda & 1 \\ 1 & \lambda \end{array} \right|</equation>，故<equation>r(A)\geqslant 2</equation>另一方面，因为不存在<equation>\lambda</equation>满足<equation>\lambda +2=(\lambda+1)^{2}=</equation>0，所以<equation>r(A)=3.</equation><equation>r(\alpha_{1},\alpha_{2},\alpha_{3})=3</equation>当且仅当<equation>\lambda\neq-2.</equation><equation>r(\alpha_{1},\alpha_{2},\alpha_{4})=3</equation>当且仅当<equation>\lambda\neq-1.</equation>因此，当<equation>\lambda\neq1</equation>时，<equation>r(A)=r(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4})=r(\alpha_{1},\alpha_{2},\alpha_{3})=r(\alpha_{1},\alpha_{2},\alpha_{4})</equation>当且仅当<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1.</equation>注意到<equation>\lambda=1</equation>也包含在条件<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1</equation>中，故<equation>r(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4})=r(\alpha_{1},\alpha_{2},\alpha_{3})= r(\alpha_{1},\alpha_{2},\alpha_{4})</equation>当且仅当<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1.</equation>综上所述，应选C.

（法二）分别计算<equation>|\alpha_{1},\alpha_{2},\alpha_{3}|</equation>，<equation>|\alpha_{1},\alpha_{2},\alpha_{4}|</equation><equation>\left| \alpha_ {1}, \alpha_ {2}, \alpha_ {3} \right| = \left| \begin{array}{c c c} \lambda & 1 & 1 \\ 1 & \lambda & 1 \\ 1 & 1 & \lambda \end{array} \right| = \left| \begin{array}{c c c} \lambda & 1 - \lambda & 1 - \lambda^ {2} \\ 1 & \lambda - 1 & 1 - \lambda \\ 1 & 0 & 0 \end{array} \right| = (1 - \lambda) ^ {2} (\lambda + 2).</equation><equation>\left| \alpha_ {1}, \alpha_ {2}, \alpha_ {4} \right| = \left| \begin{array}{c c c} \lambda & 1 & 1 \\ 1 & \lambda & \lambda \\ 1 & 1 & \lambda^ {2} \end{array} \right| = \left| \begin{array}{c c c} \lambda & 1 - \lambda & 1 - \lambda^ {3} \\ 1 & \lambda - 1 & \lambda - \lambda^ {2} \\ 1 & 0 & 0 \end{array} \right| = (1 - \lambda) ^ {2} (1 + \lambda) ^ {2}.</equation>当<equation>\lambda\neq1,-2,-1</equation>时，<equation>|\alpha_{1},\alpha_{2},\alpha_{3}|</equation>与<equation>|\alpha_{1},\alpha_{2},\alpha_{4}|</equation>均不为0.此时，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>和<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>均为3维列向量组的极大无关组，从而等价.

当<equation>\lambda=1</equation>时，<equation>\alpha_{1}=\alpha_{2}=\alpha_{3}=\alpha_{4}=\left( \begin{array}{c}1\\ 1\\ 1 \end{array} \right).</equation>此时<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>显然等价.

当<equation>\lambda=-2</equation>或<equation>\lambda=-1</equation>时，<equation>|\alpha_{1},\alpha_{2},\alpha_{3}| \neq |\alpha_{1},\alpha_{2},\alpha_{4}|</equation>，且其中一个为0，另一个不为0，说明两向量组的秩不相等，从而不等价.

综上所述，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>等价当且仅当<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1.</equation>应选C.

---

**2019年第22题 | 解答题 | 11分**

22. （本题满分11分）

2. (本题满分11分)

已知向量组 I：<equation>\alpha_{1}=\left( \begin{array}{c}1\\ 1\\ 4 \end{array} \right),\alpha_{2}=\left( \begin{array}{c}1\\ 0\\ 4 \end{array} \right),\alpha_{3}=\left( \begin{array}{c}1\\ 2\\ a^{2}+3 \end{array} \right)</equation>与向量组 II：<equation>\beta_{1}=\left( \begin{array}{c}1\\ 1\\ a+3 \end{array} \right),\beta_{2}=\left( \begin{array}{c}0\\ 2\\ 1-a \end{array} \right),</equation><equation>\beta_{3}=\left( \begin{array}{c}1\\ 3\\ a^{2}+3 \end{array} \right).</equation>若向量组 I与Ⅱ等价，求 a的取值，并将<equation>\beta_{3}</equation>用<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性表示.

**答案:**当 a≠-1时，向量组Ⅰ与向量组Ⅱ等价。当 a=1时，<equation>\boldsymbol{\beta}_{3}=(3-2k)\boldsymbol{\alpha}_{1}+(-2+k)\boldsymbol{\alpha}_{2}+k\boldsymbol{\alpha}_{3}</equation>其中 k为任意常数；当 a≠±1时，<equation>\boldsymbol{\beta}_{3}=\boldsymbol{\alpha}_{1}-\boldsymbol{\alpha}_{2}+\boldsymbol{\alpha}_{3}.</equation>

**解析:**解记<equation>A=(\alpha_{1},\alpha_{2},\alpha_{3}),B=(\beta_{1},\beta_{2},\beta_{3})</equation>，则由向量组Ⅰ与向量组Ⅱ等价可知<equation>r(A)= r(B)=r(A,B).</equation>对（A,B）作初等行变换.<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {B}) = \left( \begin{array}{c c c c c c} 1 & 1 & 1 & 1 & 0 & 1 \\ 1 & 0 & 2 & 1 & 2 & 3 \\ 4 & 4 & a ^ {2} + 3 & a + 3 & 1 - a & a ^ {2} + 3 \end{array} \right) \\ \xrightarrow {r _ {2} - r _ {1}} \frac {1}{r _ {3} - 4 r _ {1}} \left( \begin{array}{c c c c c c} 1 & 1 & 1 & 1 & 0 & 1 \\ 0 & - 1 & 1 & 0 & 2 & 2 \\ 0 & 0 & a ^ {2} - 1 & a - 1 & 1 - a & a ^ {2} - 1 \end{array} \right). \\ \end{array}</equation>由上式可知<equation>r(A)\geqslant 2</equation>，故<equation>r(A) = 2</equation>或<equation>r(A) = 3.</equation>当<equation>a^{2}-1=0</equation>时，<equation>a=1</equation>或<equation>a=-1</equation><equation>r(A)=2</equation>.又由于当<equation>a=-1</equation>时，<equation>r(A,B)=3</equation>，故<equation>a=-1</equation>不符合题意，而当<equation>a=1</equation>时，<equation>r(A)=r(B)=r(A,B)=2</equation>，此时向量组 I与向量组Ⅱ等价.

当 a = 1时，<equation>\left(\boldsymbol {A}, \boldsymbol {\beta} _ {3}\right)\rightarrow \left(\begin{array}{c c c c}1&1&1&1\\0&- 1&1&2\\0&0&0&0\end{array}\right) \xrightarrow {r _ {2} \times (- 1)} \left(\begin{array}{c c c c}1&1&1&1\\0&1&- 1&- 2\\0&0&0&0\end{array}\right) \xrightarrow {r _ {1} - r _ {2} ^ {*}} \left(\begin{array}{c c c c}1&0&2&3\\0&1&- 1&- 2\\0&0&0&0\end{array}\right).</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

取<equation>x_{3}</equation>为自由变元，令<equation>x_{3} = 1</equation>，可得<equation>(-2,1,1)^{\mathrm{T}}</equation>为<equation>Ax = 0</equation>的一个基础解系。又因为<equation>(3,-2,0)^{\mathrm{T}}</equation>为<equation>Ax = \beta_{3}</equation>的一个特解，所以<equation>Ax = \beta_{3}</equation>的通解为<equation>k(-2,1,1)^{\mathrm{T}} + (3,-2,0)^{\mathrm{T}}</equation>，其中<equation>k</equation>为任意常数.

因此，<equation>\boldsymbol {\beta} _ {3} = (3 - 2 k) \boldsymbol {\alpha} _ {1} + (- 2 + k) \boldsymbol {\alpha} _ {2} + k \boldsymbol {\alpha} _ {3},</equation>其中 k为任意常数.

当 a<equation>\neq\pm1</equation>时，<equation>a^{2}-1\neq0,r(A)=r(B)=r(A,B)=3</equation>，向量组Ⅰ与向量组Ⅱ等价，且它们相互之间的线性表示唯一.<equation>\left(\boldsymbol {A}, \boldsymbol {\beta} _ {3}\right)\rightarrow \left(\begin{array}{c c c c}1&1&1&1\\0&- 1&1&2\\0&0&1&1\end{array}\right) \xrightarrow [ r _ {1} - r _ {2} ^ {*} ]{r _ {2} \times (- 1)} \left(\begin{array}{c c c c}1&0&2&3\\0&1&- 1&- 2\\0&0&1&1\end{array}\right) \xrightarrow [ r _ {2} ^ {*} + r _ {3} ]{r _ {1} ^ {*} - 2 r _ {3}} \left(\begin{array}{c c c c}1&0&0&1\\0&1&0&- 1\\0&0&1&1\end{array}\right).</equation>因此，<equation>A x=\beta_{3}</equation>的唯一解为<equation>(1,-1,1)^{\mathrm{T}}.</equation><equation>\boldsymbol {\beta} _ {3} = \boldsymbol {\alpha} _ {1} - \boldsymbol {\alpha} _ {2} + \boldsymbol {\alpha} _ {3}.</equation>综上所述，当<equation>a\neq -1</equation>时，向量组I与向量组Ⅱ等价。当<equation>a = 1</equation>时，<equation>\beta_{3} = (3 - 2k)\alpha_{1} + (-2 + k)\alpha_{2} + k\alpha_{3}</equation>，其中k为任意常数；当<equation>a\neq \pm 1</equation>时，<equation>\beta_{3} = \alpha_{1} - \alpha_{2} + \alpha_{3}</equation>.

---

**2013年第7题 | 选择题 | 4分 | 答案: B**

7. 设 A,B,C均为 n阶矩阵. 若 AB=C，且 B可逆，则（    ）

A. 矩阵 C的行向量组与矩阵 A的行向量组等价

B. 矩阵 C的列向量组与矩阵 A的列向量组等价

C. 矩阵 C的行向量组与矩阵 B的行向量组等价

D. 矩阵 C的列向量组与矩阵 B的列向量组等价

答案: B

**解析:**我们证明 C的列向量组与 A的列向量组能相互线性表示.

不妨设<equation>A = \left(\alpha_{1},\alpha_{2},\dots ,\alpha_{n}\right),C = \left(\gamma_{1},\gamma_{2},\dots ,\gamma_{n}\right),B = \left(b_{ij}\right)_{n\times n}</equation>，则<equation>\boldsymbol {A B} = \left(\alpha_ {1}, \alpha_ {2}, \dots , \alpha_ {n}\right) \left(b _ {i j}\right) _ {n \times n} = C = \left(\gamma_ {1}, \gamma_ {2}, \dots , \gamma_ {n}\right),</equation><equation>\left\{ \begin{array}{l} \boldsymbol {\gamma} _ {1} = b _ {1 1} \boldsymbol {\alpha} _ {1} + b _ {2 1} \boldsymbol {\alpha} _ {2} + \dots + b _ {n 1} \boldsymbol {\alpha} _ {n}, \\ \boldsymbol {\gamma} _ {2} = b _ {1 2} \boldsymbol {\alpha} _ {1} + b _ {2 2} \boldsymbol {\alpha} _ {2} + \dots + b _ {n 2} \boldsymbol {\alpha} _ {n}, \\ \dots , \\ \boldsymbol {\gamma} _ {n} = b _ {1 n} \boldsymbol {\alpha} _ {1} + b _ {2 n} \boldsymbol {\alpha} _ {2} + \dots + b _ {n n} \boldsymbol {\alpha} _ {n}. \end{array} \right.</equation>因此，C的列向量组<equation>\left( \gamma_{1},\gamma_{2},\dots ,\gamma_{n}\right)</equation>能由A的列向量组<equation>\left( \alpha_{1},\alpha_{2},\dots ,\alpha_{n}\right)</equation>线性表示。同理，由于B可逆，故A的列向量组也能由C的列向量组线性表示.应选B.

下面我们说明选项A、C、D不正确.

选项A：令<equation>A=\left( \begin{array}{cc}1&1\\ 0&0 \end{array} \right), B=\left( \begin{array}{cc}1&1\\ 0&1 \end{array} \right)</equation>，则<equation>C=A B=\left( \begin{array}{cc}1&2\\ 0&0 \end{array} \right).</equation>但A的行向量组<equation>\{(1,1),(0,0)\}</equation>与C的行向量组<equation>\{(1,2),(0,0)\}</equation>不等价.

选项C、D：取B为单位矩阵E，C为一个非满秩矩阵. B的行（列）向量组线性无关，C的行（列）向量组线性相关.

---

**2011年第22题 | 解答题 | 11分**


设向量组<equation>\alpha_{1}=(1,0,1)^{\mathrm{T}},\alpha_{2}=(0,1,1)^{\mathrm{T}},\alpha_{3}=(1,3,5)^{\mathrm{T}}</equation>不能由向量组<equation>\beta_{1}=(1,1,1)^{\mathrm{T}},\beta_{2}=(1,2,3)^{\mathrm{T}},\beta_{3}=(3,4,a)^{\mathrm{T}}</equation>线性表示.

I. 求 a的值；

II. 将<equation>\beta_{1},\beta_{2},\beta_{3}</equation>用<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性表示.

**答案:**22) ( I )<equation>a=5;</equation>( II )<equation>\boldsymbol{\beta}_{1}=2\boldsymbol{\alpha}_{1}+4\boldsymbol{\alpha}_{2}-\boldsymbol{\alpha}_{3},\boldsymbol{\beta}_{2}=\boldsymbol{\alpha}_{1}+2\boldsymbol{\alpha}_{2},\boldsymbol{\beta}_{3}=5\boldsymbol{\alpha}_{1}+10\boldsymbol{\alpha}_{2}-2\boldsymbol{\alpha}_{3}.</equation>

**解析:**解（I）记<equation>A=\left(\alpha_{1},\alpha_{2},\alpha_{3}\right),B=\left(\beta_{1},\beta_{2},\beta_{3}\right),A,B</equation>的列向量组分别记为 A,B.

首先，<equation>|A|=\left| \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 1 & 1 & 5 \end{array} \right|=1</equation>，故<equation>r(A)=3</equation>，A满秩.

由于向量组 B不能线性表示 A，故<equation>r(\mathbf{B})<3</equation>；否则 B也满秩，从而 B能线性表示 A，矛盾.由于<equation>r(\mathbf{B})<3</equation>，故<equation>| \boldsymbol {B} | = \left| \begin{array}{c c c} 1 & 1 & 3 \\ 1 & 2 & 4 \\ 1 & 3 & a \end{array} \right| \frac {c _ {2} - c _ {1}}{c _ {3} - 3 c _ {1}} \left| \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 1 \\ 1 & 2 & a - 3 \end{array} \right| = a - 5 = 0.</equation>因此，<equation>a=5.</equation>（Ⅱ）（法一）求B用A的线性表示，相当于求<equation>A X=B</equation>的解. X的列向量的坐标为线性表示的系数，即<equation>\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)\left(x_{1i},x_{2i},x_{3i}\right)^{\mathrm{T}}=\boldsymbol{\beta}_{i}(i=1,2,3).</equation><equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {B}) = \left( \begin{array}{c c c c c c} 1 & 0 & 1 & 1 & 1 & 3 \\ 0 & 1 & 3 & 1 & 2 & 4 \\ 1 & 1 & 5 & 1 & 3 & 5 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c c c c} 1 & 0 & 1 & 1 & 1 & 3 \\ 0 & 1 & 3 & 1 & 2 & 4 \\ 0 & 1 & 4 & 0 & 2 & 2 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {*} - r _ {2}} \left( \begin{array}{c c c c c c} 1 & 0 & 1 & 1 & 1 & 3 \\ 0 & 1 & 3 & 1 & 2 & 4 \\ 0 & 0 & 1 & - 1 & 0 & - 2 \end{array} \right) \xrightarrow {r _ {1} - r _ {3} ^ {* *}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 2 & 1 & 5 \\ 0 & 1 & 0 & 4 & 2 & 1 0 \\ 0 & 0 & 1 & - 1 & 0 & - 2 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每做一次初等行变换，加一个*.）

因此，<equation>A x=\beta_{1}</equation>的解为<equation>(2,4,-1)^{\mathrm{T}},\beta_{1}=2\alpha_{1}+4\alpha_{2}-\alpha_{3};A x=\beta_{2}</equation>的解为<equation>(1,2,0)^{\mathrm{T}},\beta_{2}=\alpha_{1}+2\alpha_{2};A x=\beta_{3}</equation>的解为<equation>(5,10,-2)^{\mathrm{T}},\beta_{3}=5\alpha_{1}+10\alpha_{2}-2\alpha_{3}.</equation>（法二）用克拉默法则分别求<equation>A x=\beta_{1}, A x=\beta_{2}, A x=\beta_{3}</equation>的解. x的分量为线性表示的系数，即<equation>\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)\left(x_{1},x_{2},x_{3}\right)^{\mathrm{T}}=\beta_{i}(i=1,2,3).</equation>首先，可计算得<equation>|A| = 1</equation>. 由克拉默法则知，<equation>Ax = \beta_{1}</equation>的解为<equation>x _ {1} = \left| \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 3 \\ 1 & 1 & 5 \end{array} \right| = 2, \quad x _ {2} = \left| \begin{array}{c c c} 1 & 1 & 1 \\ 0 & 1 & 3 \\ 1 & 1 & 5 \end{array} \right| = 4, \quad x _ {3} = \left| \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 1 \end{array} \right| = - 1.</equation>因此，<equation>\pmb{\beta}_{1} = 2\pmb{\alpha}_{1} + 4\pmb{\alpha}_{2} - \pmb{\alpha}_{3}</equation>。同理可得<equation>\pmb{\beta}_{2} = \pmb{\alpha}_{1} + 2\pmb{\alpha}_{2},\pmb{\beta}_{3} = 5\pmb{\alpha}_{1} + 10\pmb{\alpha}_{2} - 2\pmb{\alpha}_{3}</equation>。

---

**2010年第7题 | 选择题 | 4分 | 答案: A**

7. 设向量组 I:<equation>\alpha_{1},\alpha_{2},\cdots,\alpha_{r}</equation>可由向量组 II:<equation>\beta_{1},\beta_{2},\cdots,\beta_{s}</equation>线性表示.下列命题正确的是（    ）

A. 若向量组 I 线性无关，则<equation>r\leqslant s</equation>B. 若向量组 I 线性相关，则<equation>r>s</equation>C. 若向量组 II 线性无关，则<equation>r\leqslant s</equation>D. 若向量组 II 线性相关，则<equation>r>s</equation>

答案: A

**解析:**解 由于向量组 I 能被向量组Ⅱ线性表示，故<equation>r_{\mathrm{I}}\leqslant r_{\mathrm{II}}</equation>. 又由题设，有<equation>r_{\mathrm{I}}\leqslant r, r_{\mathrm{II}}\leqslant s.</equation>若向量组 I 线性无关，则<equation>r_{\mathrm{I}}=r</equation>，从而有<equation>r = r _ {\mathrm {I}} \leqslant r _ {\mathrm {I I}} \leqslant s,</equation>即<equation>r\leqslant s</equation>应选A.

下面我们说明选项B、C、D不正确.

考虑 I = {<equation>\left( \begin{array}{c} 1 \\ 0 \end{array} \right),\left( \begin{array}{c} 2 \\ 0 \end{array} \right)</equation>，<equation>\mathrm {I I}=\left\{ \left( \begin{array}{c} 1 \\ 0 \end{array} \right),\left( \begin{array}{c} 0 \\ 1 \end{array} \right),\left( \begin{array}{c} 2 \\ 0 \end{array} \right) \right\}</equation>.<equation>\mathrm {I I}</equation>能表示 I，且向量组 I，<equation>\mathrm {I I}</equation>均线性相关，但<equation>2=r<s=3</equation>.选项B、D不正确.

考虑 I = {<equation>\left\{\begin{array}{l l}1\\0\end{array}\right\},\left(\begin{array}{l l}2\\0\end{array}\right),\left(\begin{array}{l l}3\\0\end{array}\right)</equation>，<equation>\mathrm {II}=\left\{\left(\begin{array}{l l}1\\0\end{array}\right),\left(\begin{array}{l l}0\\1\end{array}\right)\right\}</equation>. II能表示 I，且向量组Ⅱ线性无关，但 3 = r > s=2.选项C不正确.

---


### 二次型

**2024年第22题 | 解答题 | 12分**

22. （本题满分12分）

设矩阵<equation>A=\left( \begin{array}{c c c} 0 & 1 & a \\ 1 & 0 & 1 \end{array} \right), B=\left( \begin{array}{c c} 1 & 1 \\ 1 & 1 \\ b & 2 \end{array} \right),</equation>二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=\boldsymbol{x}^{\mathrm{T}} \boldsymbol{B} \boldsymbol{A} \boldsymbol{x},</equation>已知方程组<equation>A\boldsymbol{x}=\boldsymbol{0}</equation>的解均是<equation>B^{\mathrm{T}} \boldsymbol{x}=\boldsymbol{0}</equation>的解，但两个方程组不同解.

I. 求 a,b的值；

II. 求正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>，将<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>化为标准形.

**答案:**(1)<equation>a=1,b=2</equation>(2)<equation>f=\boldsymbol{x}^{\mathrm{T}}\boldsymbol{C}\boldsymbol{x}^{x=Qy}=6\boldsymbol{y}_{3}^{2}</equation>

**解析:**解（I）（法一）由于A有2阶非零子式，且A为<equation>2 \times3</equation>矩阵，故<equation>r ( A )=2, A x=0</equation>的基础解系中有3-2=1个解向量.又因为<equation>A x=0</equation>的解均是<equation>B^{\mathrm{T}} x=0</equation>的解，但这两个方程组不同解，所以<equation>B^{\mathrm{T}} x=0</equation>的基础解系中至少有两个解向量，从而<equation>r ( B^{\mathrm{T}} )\leqslant 3-2=1.</equation>结合B为非零矩阵可知<equation>r ( B^{\mathrm{T}} )=r ( B )\geqslant 1</equation>，于是<equation>r ( B^{\mathrm{T}} )=1.</equation>由于<equation>\boldsymbol {B} ^ {\mathrm {T}} = \left( \begin{array}{c c c} 1 & 1 & b \\ 1 & 1 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 2 \\ 0 & 0 & b - 2 \end{array} \right),</equation>故由<equation>r(\mathbf{B}^{\mathrm{T}}) = 1</equation>可得<equation>b = 2</equation>设<equation>( x_{1}, x_{2}, x_{3} )^{\mathrm{T}}</equation>为<equation>A x=0</equation>的解，令<equation>x_{3}=1</equation>可得<equation>(-1,-a,1)^{\mathrm{T}}</equation>为<equation>A x=0</equation>的一个基础解系.将其代入<equation>B^{\mathrm{T}} x=0</equation>即<equation>x_{1}+x_{2}+2 x_{3}=0</equation>可得，<equation>-1-a+2=0</equation>，解得 a=1.

因此，<equation>a=1,b=2.</equation>（法二）由于方程组<equation>Ax = 0</equation>的解均是<equation>B^{\mathrm{T}}x = 0</equation>的解，故方程组<equation>\binom{A}{B^{\mathrm{T}}}x = 0</equation>与<equation>Ax = 0</equation>同解（见注）.由此可得<equation>r\left( \begin{array}{c} A \\ B^{\mathrm{T}} \end{array} \right) = r(A)</equation>.又因为A有2阶非零子式，且A为<equation>2\times 3</equation>矩阵，所以<equation>r(A) = 2</equation>，从而<equation>r\left( \begin{array}{c} A \\ B^{\mathrm{T}} \end{array} \right) = 2.</equation>对<equation>\left( \begin{array}{c}A\\ B^{\mathrm{T}} \end{array} \right)</equation>作初等行变换.<equation>\binom {A} {B ^ {\mathrm {T}}} = \left( \begin{array}{c c c} 0 & 1 & a \\ 1 & 0 & 1 \\ 1 & 1 & b \\ 1 & 1 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 2 \\ 1 & 1 & b \\ 0 & 1 & a \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 1 & b - 1 \\ 0 & 1 & a \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & b - 2 \\ 0 & 0 & a - 1 \end{array} \right).</equation>由于<equation>r \binom{A}{B^{\mathrm{T}}} = 2</equation>，故<equation>a - 1 = 0, b - 2 = 0</equation>，即<equation>a = 1, b = 2</equation>（Ⅱ）由第（I）问可得<equation>A = \left( \begin{array}{lll}0 & 1 & 1\\ 1 & 0 & 1 \end{array} \right),B = \left( \begin{array}{ll}1 & 1\\ 1 & 1\\ 2 & 2 \end{array} \right)</equation>，则<equation>BA = \left( \begin{array}{lll}1 & 1 & 2\\ 1 & 1 & 2\\ 2 & 2 & 4 \end{array} \right).</equation>由于BA是一个实对称矩阵，且秩为1，迹为6，故BA相似于秩为1，迹为6的对角矩阵，特征值为6，0，0.

分别计算 BA的属于特征值6和0的特征向量.

考虑（6E-BA）x=0.<equation>\begin{array}{l} 6 E - B A = \left( \begin{array}{c c c} 5 & - 1 & - 2 \\ - 1 & 5 & - 2 \\ - 2 & - 2 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & - 5 & 2 \\ - 2 & - 2 & 2 \\ 5 & - 1 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & - 5 & 2 \\ 0 & - 1 2 & 6 \\ 0 & 2 4 & - 1 2 \end{array} \right) \\ \rightarrow \left(\begin{array}{c c c}1&- 5&2\\0&1&- \frac {1}{2}\\0&0&0\end{array}\right)\rightarrow \left(\begin{array}{c c c}1&0&- \frac {1}{2}\\0&1&- \frac {1}{2}\\0&0&0\end{array}\right). \\ \end{array}</equation><equation>\xi_{1} = \left( \begin{array}{l}1\\ 1\\ 2 \end{array} \right)</equation>为BA的属于特征值6的一个线性无关的特征向量.

考虑（0E-BA）x=0.<equation>- B A = \left( \begin{array}{c c c} - 1 & - 1 & - 2 \\ - 1 & - 1 & - 2 \\ - 2 & - 2 & - 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 2 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation><equation>\xi_{2} = \left( \begin{array}{c} - 1 \\ 1 \\ 0 \end{array} \right)</equation>和<equation>\xi_{3} = \left( \begin{array}{c} - 2 \\ 0 \\ 1 \end{array} \right)</equation>为BA的属于特征值0的两个线性无关的特征向量.

将<equation>\xi_{1},\xi_{2},\xi_{3}</equation>单位正交.由于<equation>\xi_{2},\xi_{3}</equation>已经与<equation>\xi_{1}</equation>正交，故只需将<equation>\xi_{2},\xi_{3}</equation>正交.<equation>\eta_ {2} = \xi_ {2}</equation><equation>\eta_ {3} = \xi_ {3} - \frac {\left(\eta_ {2} , \xi_ {3}\right)}{\left(\eta_ {2} , \eta_ {2}\right)} \eta_ {2} = \left( \begin{array}{c} - 2 \\ 0 \\ 1 \end{array} \right) - \left( \begin{array}{c} - 1 \\ 1 \\ 0 \end{array} \right) = \left( \begin{array}{c} - 1 \\ - 1 \\ 1 \end{array} \right).</equation>令<equation>\varepsilon_ {1} = \frac {\xi_ {1}}{\| \xi_ {1} \|} = \frac {1}{\sqrt {6}} \binom {1} {2}, \quad \varepsilon_ {2} = \frac {\eta_ {2}}{\| \eta_ {2} \|} = \frac {1}{\sqrt {2}} \binom {- 1} {1}, \quad \varepsilon_ {3} = \frac {\eta_ {3}}{\| \eta_ {3} \|} = \frac {1}{\sqrt {3}} \binom {- 1} {- 1},</equation>则<equation>Q=(\varepsilon_{1},\varepsilon_{2},\varepsilon_{3})=\left( \begin{array}{c c c} \frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{6}} & \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{3}} \\ \frac{2}{\sqrt{6}} & 0 & \frac{1}{\sqrt{3}} \end{array} \right)</equation>为正交矩阵，正交变换<equation>x=Qy</equation>将<equation>f(x_{1},x_{2},x_{3})</equation>化为标准形<equation>6 y _ {1} ^ {2}.</equation>

---

**2023年第9题 | 选择题 | 5分 | 答案: B**

9. 二次型<equation>f \left(x_{1}, x_{2}, x_{3}\right)=\left(x_{1}+x_{2}\right)^{2}+\left(x_{1}+x_{3}\right)^{2}-4\left(x_{2}-x_{3}\right)^{2}</equation>的规范形为（    )

A.<equation>y_{1}^{2}+y_{2}^{2}</equation>B.<equation>y_{1}^{2}-y_{2}^{2}</equation>C.<equation>y_{1}^{2}+y_{2}^{2}-4y_{3}^{2}</equation>D.<equation>y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>

答案: B

**解析:**解 （法一）将<equation>f ( x_{1}, x_{2}, x_{3} )</equation>展开可得<equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = 2 x _ {1} ^ {2} - 3 x _ {2} ^ {2} - 3 x _ {3} ^ {2} + 2 x _ {1} x _ {2} + 2 x _ {1} x _ {3} + 8 x _ {2} x _ {3}.</equation>该二次型对应的矩阵为<equation>A=\left( \begin{array}{c c c} 2 & 1 & 1 \\ 1 & -3 & 4 \\ 1 & 4 & -3 \end{array} \right).</equation>计算可得<equation>| A | = \left| \begin{array}{c c c} 2 & 1 & 1 \\ 1 & - 3 & 4 \\ 1 & 4 & - 3 \end{array} \right| \xlongequal {r _ {2} + r _ {3}} \left| \begin{array}{c c c} 2 & 1 & 1 \\ 2 & 1 & 1 \\ 1 & 4 & - 3 \end{array} \right| = 0.</equation>由于<equation>| A|=0</equation>，故 A有零特征值，从而<equation>r(A)\leqslant 2</equation>，f的正、负惯性指数之和不超过2.

若 f的负惯性指数为0，则f非负，即对任意<equation>\left(x_{1},x_{2},x_{3}\right)</equation>，均有<equation>f\left(x_{1},x_{2},x_{3}\right)\geqslant 0</equation>.但是，<equation>f(0,0,1)=0+1-4=-3<0</equation>，矛盾.同理，若 f的正惯性指数为0，则f非正，即对任意<equation>\left(x_{1},x_{2},x_{3}\right)</equation>，均有<equation>f\left(x_{1},x_{2},x_{3}\right)\leqslant 0</equation>.但是，<equation>f(1,0,0)=1+1-0=2>0</equation>，矛盾.

由于 f的正、负惯性指数之和不超过2，而正、负惯性指数又均大于0，故其正、负惯性指数均为 1. 应选B.<equation>(\mathrm {法 二}) \mathrm {记} \left\{ \begin{array}{l l l} y _ {1} = x _ {1} + x _ {2}, \\ y _ {2} = x _ {1} + x _ {3}, \\ y _ {3} = x _ {2} - x _ {3}, \end{array} \right. P = \left( \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & - 1 \end{array} \right), \mathrm {则} \left( \begin{array}{l} y _ {1} \\ y _ {2} \\ y _ {3} \end{array} \right) = P \left( \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right).</equation>记<equation>\boldsymbol{\Lambda}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & - 4 \end{array} \right)</equation>，则由<equation>f \left( x_{1}, x_{2}, x_{3}\right) = \left(x_{1} + x_{2}\right)^{2}+\left(x_{1} + x_{3}\right)^{2}-4\left(x_{2}-x_{3}\right)^{2}</equation>可知，<equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = y ^ {\mathrm {T}} \Lambda y \xlongequal {y = P x} x ^ {\mathrm {T}} P ^ {\mathrm {T}} \Lambda P x.</equation>于是，<equation>A=P^{\mathrm{T}}\Lambda P</equation>为二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>对应的对称矩阵.

又因为<equation>| P | = \left| \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & - 1 \end{array} \right| = 0</equation>，所以<equation>| A | = 0</equation>，从而A有零特征值.

（法三）令<equation>\left\{\begin{array}{l l}y_{1}=x_{1}+x_{2},\\ y_{2}=x_{1}+x_{3},\\ y_{3}=x_{3},\end{array} \right.</equation>则<equation>x_{2}-x_{3}=y_{1}-y_{2}</equation>，且该变换为可逆线性变换.在该变换下，二次型<equation>f \left(x_{1}, x_{2}, x_{3}\right)</equation>化为

其余同法一.<equation>\begin{aligned} g \left(y _ {1}, y _ {2}, y _ {3}\right) &= y _ {1} ^ {2} + y _ {2} ^ {2} - 4 \left(y _ {1} - y _ {2}\right) ^ {2} = - 3 y _ {1} ^ {2} - 3 y _ {2} ^ {2} + 8 y _ {1} y _ {2} \\ &= - 3 y _ {1} ^ {2} + 3 \cdot \frac {8}{3} y _ {1} y _ {2} - 3 y _ {2} ^ {2} = - 3 \left(y _ {1} - \frac {4}{3} y _ {2}\right) ^ {2} - 3 y _ {2} ^ {2} + \frac {1 6}{3} y _ {2} ^ {2} \\ &= - 3 \left(y _ {1} - \frac {4}{3} y _ {2}\right) ^ {2} + \frac {7}{3} y _ {2} ^ {2}. \end{aligned}</equation>再令<equation>\left\{ \begin{array}{l l} z_{1}=y_{1}-\frac{4}{3} y_{2}, \\ z_{2}=y_{2}, \\ z_{3}=y_{3}, \end{array} \right.</equation>该变换为可逆线性变换.在该变换下，二次型<equation>g \left( y_{1}, y_{2}, y_{3} \right)</equation>化为<equation>h \left(z _ {1}, z _ {2}, z _ {3}\right) = - 3 z _ {1} ^ {2} + \frac {7}{3} z _ {2} ^ {2}.</equation>因此，<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>的一个标准形为<equation>- 3 z_{1}^{2}+\frac{7}{3} z_{2}^{2}</equation>其正、负惯性指数均为1.应选B.

---

**2022年第22题 | 解答题 | 12分**

22. (本题满分12分)

已知二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=3 x_{1}^{2}+4 x_{2}^{2}+3 x_{3}^{2}+2 x_{1} x_{3}</equation>.

I. 求正交矩阵 Q，使正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>将二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>化为标准形；

II. 证明<equation>\min_{x\neq 0} \frac{f(x)}{x^{\mathrm{T}}x}=2.</equation>

**答案:**（I）<equation>Q=\left( \begin{array}{c c c} {\frac{1}{\sqrt{2}}} & {0} & {-\frac{1}{\sqrt{2}}} \\ {0} & {1} & {0} \\ {\frac{1}{\sqrt{2}}} & {0} & {\frac{1}{\sqrt{2}}} \end{array} \right)</equation>正交变换<equation>x=Qy</equation>将二次型f化为标准形<equation>4y_{1}^{2}+4y_{2}^{2}+2y_{3}^{2}</equation>；

（Ⅱ）证明略.

**解析:**解（I）由 f的表达式可得 f对应的矩阵 A =<equation>\left( \begin{array}{c c c} 3 & 0 & 1 \\ 0 & 4 & 0 \\ 1 & 0 & 3 \end{array} \right).</equation>计算 A的特征多项式.<equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda - 3 & 0 & - 1 \\ 0 & \lambda - 4 & 0 \\ - 1 & 0 & \lambda - 3 \end{array} \right| = (\lambda - 4) \left[ (\lambda - 3) ^ {2} - 1 \right] = (\lambda - 4) ^ {2} (\lambda - 2).</equation>A的特征值为4,4,2.

分别计算 A的属于特征值4和2的特征向量.

考虑（4E-A）x=0.<equation>4 E - A = \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 0 & 0 \\ - 1 & 0 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation><equation>\boldsymbol{\xi}_{1}=\left( \begin{array}{c}1\\ 0\\ 1 \end{array} \right)</equation>和<equation>\boldsymbol{\xi}_{2}=\left( \begin{array}{c}0\\ 1\\ 0 \end{array} \right)</equation>为 A的属于特征值4的两个线性无关的特征向量考虑<equation>( 2 E-A ) x=0.</equation><equation>2 E - A = \left( \begin{array}{c c c} - 1 & 0 & - 1 \\ 0 & - 2 & 0 \\ - 1 & 0 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation><equation>\xi_{3}=\left( \begin{array}{c}-1\\ 0\\ 1 \end{array} \right)</equation>为 A的属于特征值2的一个特征向量.

由于<equation>\xi_{1},\xi_{2},\xi_{3}</equation>相互正交，故只需将它们各自单位化即可得一组相互正交的单位特征向量.<equation>\boldsymbol {\varepsilon} _ {1} = \frac {\boldsymbol {\xi} _ {1}}{\| \boldsymbol {\xi} _ {1} \|} = \frac {1}{\sqrt {2}} \left( \begin{array}{c} 1 \\ 0 \\ 1 \end{array} \right), \quad \boldsymbol {\varepsilon} _ {2} = \frac {\boldsymbol {\xi} _ {2}}{\| \boldsymbol {\xi} _ {2} \|} = \left( \begin{array}{c} 0 \\ 1 \\ 0 \end{array} \right), \quad \boldsymbol {\varepsilon} _ {3} = \frac {\boldsymbol {\xi} _ {3}}{\| \boldsymbol {\xi} _ {3} \|} = \frac {1}{\sqrt {2}} \left( \begin{array}{c} - 1 \\ 0 \\ 1 \end{array} \right).</equation>令<equation>Q=(\varepsilon_{1},\varepsilon_{2},\varepsilon_{3})</equation>，可得<equation>Q^{-1}AQ=Q^{\mathrm{T}}AQ=\left( \begin{array}{c c c} 4 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>，即正交变换<equation>x=Qy</equation>将二次型f化为标准形<equation>4y_{1}^{2}+4y_{2}^{2}+2y_{3}^{2}.</equation>（Ⅱ）由第（I）问可知，在正交变换<equation>x=Q y</equation>下，<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>的标准形为<equation>4 y_{1}^{2}+4 y_{2}^{2}+2 y_{3}^{2}.</equation>又因为<equation>\boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {x} = \left(Q \boldsymbol {y}\right) ^ {\mathrm {T}} Q \boldsymbol {y} = \boldsymbol {y} ^ {\mathrm {T}} Q ^ {\mathrm {T}} Q \boldsymbol {y} \xlongequal {Q ^ {\mathrm {T}} Q = E} \boldsymbol {y} ^ {\mathrm {T}} \boldsymbol {y} = y _ {1} ^ {2} + y _ {2} ^ {2} + y _ {3} ^ {2},</equation>所以对<equation>x\neq 0</equation><equation>\frac {f (\boldsymbol {x})}{\boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {x}} \xlongequal {\boldsymbol {x} = Q \boldsymbol {y}} \frac {4 y _ {1} ^ {2} + 4 y _ {2} ^ {2} + 2 y _ {3} ^ {2}}{y _ {1} ^ {2} + y _ {2} ^ {2} + y _ {3} ^ {2}} \geqslant \frac {2 y _ {1} ^ {2} + 2 y _ {2} ^ {2} + 2 y _ {3} ^ {2}}{y _ {1} ^ {2} + y _ {2} ^ {2} + y _ {3} ^ {2}} = 2.</equation>取<equation>y_{0}</equation>满足<equation>y_{1}=y_{2}=0,y_{3}\neq 0,x_{0}=Qy_{0}</equation>即<equation>x_{0}=y_{3}\varepsilon_{3}</equation>时，可得<equation>\frac{f(\boldsymbol{x}_{0})}{\boldsymbol{x}_{0}^{\mathrm{T}}\boldsymbol{x}_{0}}=2.</equation>因此，<equation>\min_{x\neq0}\frac{f(x)}{x^{\mathrm{T}}x}=2.</equation>

---

**2021年第8题 | 选择题 | 5分 | 答案: B**

8. 二次型<equation>f \left(x_{1}, x_{2}, x_{3}\right)=\left(x_{1}+x_{2}\right)^{2}+\left(x_{2}+x_{3}\right)^{2}-\left(x_{3}-x_{1}\right)^{2}</equation>的正惯性指数和负惯性指数分别为（    ）

A. 2,0 B. 1,1 C. 2,1 D. 1,2

答案: B

**解析:**解（法一）令<equation>\left\{ \begin{array}{l l} y_{1}=x_{1}+x_{2}, \\ y_{2}=x_{2}+x_{3}, \\ y_{3}=x_{3}, \end{array} \right.</equation>则<equation>x_{3}-x_{1}=y_{2}-y_{1}</equation>，且该变换为可逆线性变换.在该变换下，二次型<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>化为<equation>g \left(y _ {1}, y _ {2}, y _ {3}\right) = y _ {1} ^ {2} + y _ {2} ^ {2} - \left(y _ {2} - y _ {1}\right) ^ {2} = 2 y _ {1} y _ {2}.</equation>再令<equation>\left\{ \begin{array}{l l} y_{1}=z_{1}+z_{2}, \\ y_{2}=z_{1}-z_{2}, \\ y_{3}=z_{3}, \end{array} \right.</equation>则<equation>g \left( y_{1}, y_{2}, y_{3} \right)</equation>化为<equation>h \left(z _ {1}, z _ {2}, z _ {3}\right) = 2 \left(z _ {1} + z _ {2}\right) \left(z _ {1} - z _ {2}\right) = 2 z _ {1} ^ {2} - 2 z _ {2} ^ {2}.</equation>因此，<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>的一个标准形为<equation>2z_{1}^{2}-2z_{2}^{2}</equation>其正、负惯性指数分别为1，1.应选B.

（法二）将<equation>f(x_{1},x_{2},x_{3})</equation>展开可得<equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = 2 x _ {2} ^ {2} + 2 x _ {1} x _ {2} + 2 x _ {2} x _ {3} + 2 x _ {1} x _ {3}.</equation>该二次型对应的矩阵为<equation>A=\left( \begin{array}{c c c} 0 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 0 \end{array} \right)</equation>. 不难发现，A的第二行为第一行与第三行的和，故<equation>r(A)\leqslant 2</equation>. 又因为A有一个2阶非零子式<equation>\left| \begin{array}{c c} 0 & 1 \\ 1 & 2 \end{array} \right|</equation>，所以<equation>r(A)\geqslant 2</equation>. 于是，<equation>r(A)=2.</equation>由于二次型的正、负惯性指数之和等于其对应矩阵的秩，而选项C、D的两数之和均为3，故可排除选项C、D.

另一方面，若 f的负惯性指数为0，则f非负，即对任意<equation>\left(x_{1},x_{2},x_{3}\right)</equation>，均有<equation>f\left(x_{1},x_{2},x_{3}\right)\geqslant 0.</equation>但是，<equation>f(1,0,-1)=1+1-4<0</equation>矛盾.因此，选项A不正确.

根据排除法，应选B.

---

**2020年第22题 | 解答题 | 11分**

22. （本题满分11分）

2. (本题满分11分)

设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=x_{1}^{2}+x_{2}^{2}+x_{3}^{2}+2 a x_{1} x_{2}+2 a x_{1} x_{3}+2 a x_{2} x_{3}</equation>经可逆线性变换<equation>\left( \begin{array}{c} x_{1} \\ x_{2} \\ x_{3} \end{array} \right)=P \left( \begin{array}{c} y_{1} \\ y_{2} \\ y_{3} \end{array} \right)</equation>化为二次型<equation>g \left( y_{1}, y_{2}, y_{3} \right)=y_{1}^{2}+y_{2}^{2}+4 y_{3}^{2}+2 y_{1} y_{2}</equation>I. 求 a的值；

II. 求可逆矩阵 P.

**答案:**( I )<equation>a=-\frac{1}{2}</equation>;

( II )<equation>P=\left( \begin{array}{c c c} 1 & 2 & \frac{2}{\sqrt{3}} \\ 0 & 1 & \frac{4}{\sqrt{3}} \\ 0 & 1 & 0 \end{array} \right)</equation>，可逆线性变换<equation>\left( \begin{array}{c} x_{1} \\ x_{2} \\ x_{3} \end{array} \right)=P\left( \begin{array}{c} y_{1} \\ y_{2} \\ y_{3} \end{array} \right)</equation>可将二次型<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>化为二次型

**解析:**解（I）<equation>f ( x_{1}, x_{2}, x_{3} )=x_{1}^{2}+x_{2}^{2}+x_{3}^{2}+2 a x_{1} x_{2}+2 a x_{1} x_{3}+2 a x_{2} x_{3}</equation>对应的矩阵<equation>A=\left( \begin{array}{c c c} 1 & a & a \\ a & 1 & a \\ a & a & 1 \end{array} \right),</equation><equation>g ( y_{1}, y_{2}, y_{3} )=y_{1}^{2}+y_{2}^{2}+4 y_{3}^{2}+2 y_{1} y_{2}</equation>对应的矩阵<equation>B=\left( \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 4 \end{array} \right).</equation>易知<equation>r ( B )=2</equation>从而由合同变换不改变矩阵的秩可知<equation>r ( A )=2, | A |=0.</equation><equation>| A | = \left| \begin{array}{l l l} 1 & a & a \\ a & 1 & a \\ a & a & 1 \end{array} \right| = (2 a + 1) \left| \begin{array}{l l l} 1 & a & a \\ 1 & 1 & a \\ 1 & a & 1 \end{array} \right| = (2 a + 1) \left| \begin{array}{l l l} 1 & 0 & 0 \\ 1 & 1 - a & 0 \\ 1 & 0 & 1 - a \end{array} \right| = (2 a + 1) (1 - a) ^ {2}.</equation>由<equation>|A| = 0</equation>可得<equation>a = 1</equation>或<equation>a = -\frac{1}{2}</equation>. 但是当<equation>a = 1</equation>时，<equation>r(A) = 1</equation>，不符合题意，故<equation>a = -\frac{1}{2}</equation>.

将<equation>a=-\frac{1}{2}</equation>代入<equation>f \left(x_{1}, x_{2}, x_{3}\right)</equation>，并将其化为规范形.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= x _ {1} ^ {2} + x _ {2} ^ {2} + x _ {3} ^ {2} - x _ {1} x _ {2} - x _ {1} x _ {3} - x _ {2} x _ {3} \\ &= \left(x _ {1} - \frac {1}{2} x _ {2} - \frac {1}{2} x _ {3}\right) ^ {2} + \frac {3}{4} x _ {2} ^ {2} + \frac {3}{4} x _ {3} ^ {2} - \frac {3}{2} x _ {2} x _ {3} \\ &= \left(x _ {1} - \frac {1}{2} x _ {2} - \frac {1}{2} x _ {3}\right) ^ {2} + \frac {3}{4} \left(x _ {2} - x _ {3}\right) ^ {2}. \end{aligned}</equation>令<equation>\left\{ \begin{array}{l l} z_{1}=x_{1}-\frac{1}{2} x_{2}-\frac{1}{2} x_{3}, \\ z_{2}=\frac{\sqrt{3}}{2}(x_{2}-x_{3}), \\ z_{3}=x_{3}, \end{array} \right.</equation>则可得<equation>z_{1}^{2}+z_{2}^{2}</equation>即<equation>f(x_{1},x_{2},x_{3})</equation>的规范形.<equation>\begin{array}{l} \left(P _ {1} ^ {- 1}, E\right) = \left( \begin{array}{c c c c c c} 1 & - \frac {1}{2} & - \frac {1}{2} & 1 & 0 & 0 \\ 0 & \frac {\sqrt {3}}{2} & - \frac {\sqrt {3}}{2} & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {2} + \frac {\sqrt {3}}{2} r _ {3} ]{r _ {1} + \frac {1}{2} r _ {3}} \left( \begin{array}{c c c c c c} 1 & - \frac {1}{2} & 0 & 1 & 0 & \frac {1}{2} \\ 0 & \frac {\sqrt {3}}{2} & 0 & 0 & 1 & \frac {\sqrt {3}}{2} \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} \times \frac {2}{\sqrt {3}}} \left( \begin{array}{c c c c c c} 1 & - \frac {1}{2} & 0 & 1 & 0 & \frac {1}{2} \\ 0 & 1 & 0 & 0 & \frac {2}{\sqrt {3}} & 1 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {1} ^ {*} + \frac {1}{2} r _ {2} ^ {* *}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 1 & \frac {1}{\sqrt {3}} & 1 \\ 0 & 1 & 0 & 0 & \frac {2}{\sqrt {3}} & 1 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

于是，<equation>P_{1}=\left( \begin{array}{c c c} 1 & \frac{1}{\sqrt{3}} & 1 \\ 0 & \frac{2}{\sqrt{3}} & 1 \\ 0 & 0 & 1 \end{array} \right), P_{1}^{\mathrm{T}} A P_{1}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>再将<equation>g(y_{1},y_{2},y_{3})</equation>化为规范形.<equation>g(y_{1},y_{2},y_{3})=y_{1}^{2}+y_{2}^{2}+4y_{3}^{2}+2y_{1}y_{2}=(y_{1}+y_{2})^{2}+4y_{3}^{2}.</equation>令<equation>\left\{ \begin{array}{l l l} z_{1}=y_{1}+y_{2}, \\ z_{2}=2y_{3}, \\ z_{3}=y_{2}, \end{array} \right.</equation>则<equation>\left( \begin{array}{l} z_{1} \\ z_{2} \\ z_{3} \end{array} \right)=\left( \begin{array}{l l l} 1 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 1 & 0 \end{array} \right)\left( \begin{array}{l} y_{1} \\ y_{2} \\ y_{3} \end{array} \right).</equation>记<equation>P_{2}^{-1}=\left( \begin{array}{l l l} 1 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 1 & 0 \end{array} \right),</equation>则<equation>\left( \begin{array}{l} z_{1} \\ z_{2} \\ z_{3} \end{array} \right)=P_{2}^{-1}\left( \begin{array}{l} y_{1} \\ y_{2} \\ y_{3} \end{array} \right),</equation>且<equation>P_{2}^{\mathrm{T}} B P_{2}=\left( \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>记<equation>\Lambda=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>由于<equation>P_{1}^{\mathrm{T}} A P_{1}=\Lambda, P_{2}^{\mathrm{T}} B P_{2}=\Lambda,</equation>故<equation>\boldsymbol{B}=(P_{2}^{\mathrm{T}})^{-1}\boldsymbol{\Lambda}P_{2}^{-1}\frac{(P_{2}^{\mathrm{T}})^{-1}=(P_{2}^{-1})^{\mathrm{T}}}{(P_{2}^{-1})^{\mathrm{T}}P_{1}^{\mathrm{T}} A P_{1} P_{2}^{-1}}.</equation>因此，<equation>P=P_{1} P_{2}^{-1}=\left( \begin{array}{c c c} 1 & \frac{1}{\sqrt{3}} & 1 \\ 0 & \frac{2}{\sqrt{3}} & 1 \\ 0 & 0 & 1 \end{array} \right)\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 1 & 0 \end{array} \right)=\left( \begin{array}{c c c} 1 & 2 & \frac{2}{\sqrt{3}} \\ 0 & 1 & \frac{4}{\sqrt{3}} \\ 0 & 1 & 0 \end{array} \right).</equation><equation>\left( \begin{array}{l} x_{1} \\ x_{2} \end{array} \right)=P\left( \begin{array}{l} y_{1} \\ y_{2} \end{array} \right)</equation>可将二次型<equation>f(x_{1},x_{2},x_{3})</equation>化为二次型<equation>g(y_{1},y_{2},y_{3}).</equation><equation>\binom{x_1}{x_2} = P\binom{y_1}{y_2}</equation>可将二次型<equation>f ( x_{1}, x_{2}, x_{3} )</equation>化为二次型<equation>g ( y_{1}, y_{2}, y_{3} ).</equation>（法二）对A做合同变换，将其化为B.<equation>\begin{aligned} A &= \left( \begin{array}{c c c} 1 & - \frac {1}{2} & - \frac {1}{2} \\ - \frac {1}{2} & 1 & - \frac {1}{2} \\ - \frac {1}{2} & - \frac {1}{2} & 1  \right) \xrightarrow {\mathrm {行 变换}} \frac {1}{r _ {3} - r _ {2}} \left( \begin{array}{c c c} 1 & - \frac {1}{2} & - \frac {1}{2} \\ - \frac {1}{2} & 1 & - \frac {1}{2} \\ 0 & - \frac {3}{2} & \frac {3}{2}  \right) \xrightarrow {\mathrm {列 变换}} \frac {1}{c _ {3} - c _ {2}} \left( \begin{array}{c c c} 1 & - \frac {1}{2} & 0 \\ - \frac {1}{2} & 1 & - \frac {3}{2} \\ 0 & - \frac {3}{2} & 3  \right) \\ \xrightarrow {\mathrm {行 变换}} \frac {1}{r _ {2} + \frac {1}{2} r _ {3}} \left( \begin{array}{c c c} 1 & - \frac {1}{2} & 0 \\ - \frac {1}{2} & \frac {1}{4} & 0 \\ 0 & - \frac {3}{2} & 3  \right) \xrightarrow {\mathrm {列 变换}} \frac {1}{c _ {2} + \frac {1}{2} c _ {3}} \left( \begin{array}{c c c} 1 & - \frac {1}{2} & 0 \\ - \frac {1}{2} & \frac {1}{4} & 0 \\ 0 & 0 & 3  \right) \\ \xrightarrow {\mathrm {行 变换}} \frac {1}{r _ {2} + \frac {3}{2} r _ {1}} \left( \begin{array}{c c c} 1 & - \frac {1}{2} & 0 \\ 1 & - \frac {1}{2} & 0 \\ 0 & 0 & 3  \right) \xrightarrow {\mathrm {列 变换}} \frac {1}{c _ {2} + \frac {3}{2} c _ {1}} \left( \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 3  \right) \\ \xrightarrow {\mathrm {行 变换}} \frac {1}{r _ {3} \times \frac {2}{\sqrt {3}}} \left( \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 2 \sqrt {3}  \right) \xrightarrow {\mathrm {列 变换}} \frac {1}{c _ {3} \times \frac {2}{\sqrt {3}}} \left( \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 4  \right) &= B. \end{aligned}</equation>记录每一次初等列变换所对应的初等矩阵，分别记为<equation>P_{1}, P_{2}, P_{3}, P_{4}</equation><equation>\begin{aligned} P _ {1} &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & - 1 \\ 0 & 0 & 1  \right), \quad P _ {2} &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & \frac {1}{2} & 1  \right), \quad P _ {3} &= \left( \begin{array}{c c c} 1 & \frac {3}{2} & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1  \right), \quad P _ {4} &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & \frac {2}{\sqrt {3}}  \right). \\ P &= P _ {1} P _ {2} P _ {3} P _ {4} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & - 1 \\ 0 & 0 & 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & \frac {1}{2} & 1  \right) \left( \begin{array}{c c c} 1 & \frac {3}{2} & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & \frac {2}{\sqrt {3}}  \right) \\ &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & \frac {1}{2} & - 1 \\ 0 & \frac {1}{2} & 1  \right) \left( \begin{array}{c c c} 1 & \frac {3}{2} & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & \frac {2}{\sqrt {3}}  \right) \\ &= \left( \begin{array}{c c c} 1 & \frac {3}{2} & 0 \\ 0 & \frac {1}{2} & - 1 \\ 0 & \frac {1}{2} & 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & \frac {2}{\sqrt {3}}  \right) &= \left( \begin{array}{c c c} 1 & \frac {3}{2} & 0 \\ 0 & \frac {1}{2} & - \frac {2}{\sqrt {3}} \\ 0 & \frac {1}{2} & \frac {2}{\sqrt {3}}  \right). \end{aligned}</equation>因此，<equation>P^{\mathrm{T}} A P=B</equation>，即<equation>\left( \begin{array}{c}x_{1}\\ x_{2}\\ x_{3}\end{array} \right)=P\left( \begin{array}{c}y_{1}\\ y_{2}\\ y_{3} \end{array} \right)</equation>可将二次型<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>化为二次型<equation>g\left(y_{1},y_{2},y_{3}\right).</equation>

---

**2019年第8题 | 选择题 | 4分 | 答案: C**

8. 设 A是3阶实对称矩阵，E是3阶单位矩阵.若<equation>A^{2}+A=2 E</equation>，且<equation>|A|=4</equation>，则二次型<equation>x^{\mathrm{T}} A x</equation>的规范形为（    )

A.<equation>y_{1}^{2}+y_{2}^{2}+y_{3}^{2}</equation>B.<equation>y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>C.<equation>y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>D.<equation>-y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>

答案: C

**解析:**设<equation>\lambda</equation>为 A的一个特征值，<equation>\alpha</equation>为属于特征值<equation>\lambda</equation>的特征向量.

由<equation>A^{2}+A=2 E</equation>可得<equation>(\lambda^{2}+\lambda-2)\alpha=0</equation>. 由于<equation>\alpha</equation>为非零向量，故<equation>\lambda^{2}+\lambda-2=0</equation>. 解得<equation>\lambda=1</equation>或<equation>\lambda=-2</equation>. A的特征值只能取1和-2.

又因为<equation>| A |=4</equation>，所以 A的特征值应为-2，-2，1. 因此，二次型<equation>x^{\mathrm{T}} A x</equation>的正惯性指数为1，负惯性指数为2. 四个选项中，只有<equation>y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>满足该性质. 应选C.

---

**2018年第22题 | 解答题 | 11分**

22. (本题满分11分)

设实二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=\left( x_{1}-x_{2}+x_{3} \right)^{2}+\left( x_{2}+x_{3} \right)^{2}+\left( x_{1}+a x_{3} \right)^{2}</equation>其中 a是参数.

I. 求<equation>f \left( x_{1}, x_{2}, x_{3} \right)=0</equation>的解;

II. 求<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>的规范形.

**答案:**（I）当 a≠2时，<equation>f ( x_{1}, x_{2}, x_{3} )=0</equation>的解为<equation>\left( x_{1}, x_{2}, x_{3}\right)^{\mathrm{T}}=\left( 0,0,0\right)^{\mathrm{T}}</equation>；当 a=2时，<equation>f \left( x_{1}, x_{2}, x_{3}\right)=0</equation>的解为<equation>\left( x_{1}, x_{2}, x_{3}\right)^{\mathrm{T}}=k \left( -2,-1,1\right)^{\mathrm{T}}</equation>其中 k为任意常数.

（Ⅱ）当 a≠2时， f的规范形为<equation>f=y_{1}^{2}+y_{2}^{2}+y_{3}^{2}</equation>；当 a=2时， f的规范形为<equation>f=z_{1}^{2}+z_{2}^{2}.</equation>

**解析:**解（I）<equation>f \left( x_{1}, x_{2}, x_{3} \right)=0</equation>当且仅当<equation>\left\{ \begin{array}{l l} x_{1}-x_{2}+x_{3}=0, \\ x_{2}+x_{3}=0, \\ x_{1}+a x_{3}=0. \end{array} \right.</equation>记 A为该方程组的系数矩阵.对 A作初等行变换.<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & - 1 & 1 \\ 0 & 1 & 1 \\ 1 & 0 & a \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c} 1 & - 1 & 1 \\ 0 & 1 & 1 \\ 0 & 1 & a - 1 \end{array} \right) \xrightarrow {r _ {1} + r _ {2}} \left( \begin{array}{c c c} 1 & 0 & 2 \\ 0 & 1 & 1 \\ 0 & 0 & a - 2 \end{array} \right).</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

当 a≠2时，<equation>r ( \mathbf{A} )=3</equation>，方程组只有零解.

当 a=2时，<equation>r ( \mathbf{A} )=2.</equation>方程组的基础解系仅包含一个向量.取<equation>x_{3}</equation>为自由变元，令<equation>x_{3}=1</equation>解得<equation>\left(x_{1},x_{2},x_{3}\right)^{\mathrm{T}}=\left(-2,-1,1\right)^{\mathrm{T}}</equation>为该方程组的一个基础解系.

因此，当 a≠2时，<equation>f \left( x_{1}, x_{2}, x_{3} \right)=0</equation>的解为<equation>\left(x_{1}, x_{2}, x_{3}\right)^{\mathrm{T}}=\left(0, 0, 0\right)^{\mathrm{T}}</equation>；当 a=2时，<equation>f \left( x_{1}, x_{2}, x_{3} \right)=0</equation>的解为<equation>\left(x_{1}, x_{2}, x_{3}\right)^{\mathrm{T}}=k \left(-2,-1,1\right)^{\mathrm{T}}</equation>其中 k为任意常数.

（Ⅱ）由<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>的表达式知，<equation>f\left(x_{1},x_{2},x_{3}\right)\geqslant 0.</equation>当 a≠2时，由第（I）问可知，<equation>f ( x_{1}, x_{2}, x_{3} )=0</equation>只有零解，f为正定二次型.因此，当 a≠2时， f的规范形为<equation>f=y_{1}^{2}+y_{2}^{2}+y_{3}^{2}.</equation>当 a=2时，f不满秩.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= \left(x _ {1} - x _ {2} + x _ {3}\right) ^ {2} + \left(x _ {2} + x _ {3}\right) ^ {2} + \left(x _ {1} + 2 x _ {3}\right) ^ {2} \\ &= 2 x _ {1} ^ {2} + 2 x _ {2} ^ {2} + 6 x _ {3} ^ {2} - 2 x _ {1} x _ {2} + 6 x _ {1} x _ {3}. \end{aligned}</equation>记f对应的对称矩阵为<equation>B=\left( \begin{array}{c c c} 2 & -1 & 3 \\ -1 & 2 & 0 \\ 3 & 0 & 6 \end{array} \right).</equation>下面用三种方法求 f的规范形.

（法一）由<equation>f ( x_{1}, x_{2}, x_{3} ) \geqslant0</equation>可知 f的负惯性指数为0（否则，若规范形有负系数，不妨设规范形为<equation>f=y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>，取<equation>( y_{1}, y_{2}, y_{3} )=(0,0,1)</equation>，则<equation>f ( y_{1}, y_{2}, y_{3} )=-1<0</equation>，矛盾）.由于B的秩等于f的正、负惯性指数之和，故 f的正惯性指数等于r（B）.

计算<equation>| B |</equation>得<equation>| B |=0</equation>，故<equation>r ( B ) \leqslant2</equation>. 又因为B有一个2阶子式<equation>\left| \begin{array}{c c} {2} & {-1} \\ {-1} & {2} \end{array} \right|=3\neq0</equation>，所以<equation>r ( B ) \geqslant2.</equation>因此，<equation>r ( B )=2.</equation>综上所述，f的正惯性指数为2，负惯性指数为0.f的规范形为<equation>f=z_{1}^{2}+z_{2}^{2}.</equation>（法二）计算 B的特征值，从而得到 f的正、负惯性指数.

计算 B的特征多项式.<equation>| \lambda E - B | = \left| \begin{array}{c c c} \lambda - 2 & 1 & - 3 \\ 1 & \lambda - 2 & 0 \\ - 3 & 0 & \lambda - 6 \end{array} \right| = \lambda \left(\lambda^ {2} - 1 0 \lambda + 1 8\right).</equation>解<equation>\lambda^{2}-1 0 \lambda+1 8=0</equation>可得<equation>\lambda_{1,2}=\frac{1 0 \pm \sqrt{1 0 0}-7 2}{2}=5 \pm \sqrt{7}.</equation>由于<equation>5+\sqrt{7}>0, 5-\sqrt{7}>0</equation>，故f有两个正特征值，一个零特征值，从而f的正惯性指数为2，负惯性指数为0.

因此，<equation>f</equation>的规范形为<equation>f = z_{1}^{2} + z_{2}^{2}</equation>.

（法三）配方法.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= 2 x _ {1} ^ {2} + 2 x _ {2} ^ {2} + 6 x _ {3} ^ {2} - 2 x _ {1} x _ {2} + 6 x _ {1} x _ {3} = 2 \left(x _ {1} ^ {2} - x _ {1} x _ {2} + 3 x _ {1} x _ {3}\right) + 2 x _ {2} ^ {2} + 6 x _ {3} ^ {2} \\ &= 2 \left(x _ {1} - \frac {x _ {2}}{2} + \frac {3}{2} x _ {3}\right) ^ {2} + \frac {3}{2} x _ {2} ^ {2} - \frac {9}{2} x _ {3} ^ {2} + 3 x _ {2} x _ {3} + 6 x _ {3} ^ {2} \\ &= 2 \left(x _ {1} - \frac {x _ {2}}{2} + \frac {3}{2} x _ {3}\right) ^ {2} + \frac {3}{2} \left(x _ {2} + x _ {3}\right) ^ {2}. \end{aligned}</equation>令<equation>\left\{ \begin{array}{l l} z_{1}=\sqrt{2}\left(x_{1}-\frac{x_{2}}{2}+\frac{3}{2} x_{3}\right), \\ z_{2}=\sqrt{\frac{3}{2}}\left(x_{2}+x_{3}\right), \\ z_{3}=x_{3}, \end{array} \right.</equation>则<equation>f \left(z_{1}, z_{2}, z_{3}\right)=z_{1}^{2}+z_{2}^{2}.</equation>因此，<equation>f</equation>的规范形为<equation>f=z_{1}^{2}+z_{2}^{2}.</equation>

---

**2017年第23题 | 解答题 | 11分**

23. (本题满分11分)

设二次型<equation>f \left(x_{1}, x_{2}, x_{3}\right)=2 x_{1}^{2}-x_{2}^{2}+a x_{3}^{2}+2 x_{1} x_{2}-8 x_{1} x_{3}+2 x_{2} x_{3}</equation>在正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>下的标准形为<equation>\lambda_{1} y_{1}^{2}+\lambda_{2} y_{2}^{2}</equation>求 a的值及一个正交矩阵 Q.

**答案:**a=2，<equation>Q=\left( \begin{array}{c c c} -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \\ 0 & -\frac{1}{\sqrt{3}} & \frac{2}{\sqrt{6}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \end{array} \right)</equation>，且<equation>Q^{\mathrm{T}}AQ=\left( \begin{array}{c c c} 6 & 0 & 0 \\ 0 & -3 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>，即f在正交变换 x = Qy下的标准

形为<equation>f=6 y_{1}^{2}-3 y_{2}^{2}.</equation>

**解析:**解 记二次型 f对应的实对称矩阵为 A，则<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 2 & 1 & - 4 \\ 1 & - 1 & 1 \\ - 4 & 1 & a \end{array} \right).</equation>由于 f在正交变换<equation>x=Q y</equation>下的标准形为<equation>\lambda_{1} y_{1}^{2}+\lambda_{2} y_{2}^{2}</equation>，故 A的特征值为<equation>\lambda_{1},\lambda_{2},0.</equation>从而<equation>|A|=0.</equation>计算 A的行列式得<equation>| A | = - 3 a + 6.</equation>因此，<equation>a = 2</equation>，<equation>A = \left( \begin{array}{c c c} 2 & 1 & -4 \\ 1 & -1 & 1 \\ -4 & 1 & 2 \end{array} \right).</equation>计算 A的特征多项式得<equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda - 2 & - 1 & 4 \\ - 1 & \lambda + 1 & - 1 \\ 4 & - 1 & \lambda - 2 \end{array} \right| = \lambda^ {3} - 3 \lambda^ {2} - 1 8 \lambda = \lambda (\lambda - 6) (\lambda + 3).</equation>于是，A的3个特征值分别为6，-3，0.

当<equation>\lambda=6</equation>时，<equation>\begin{array}{l} 6 E - A = \left( \begin{array}{c c c} 4 & - 1 & 4 \\ - 1 & 7 & - 1 \\ 4 & - 1 & 4 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c} 4 & - 1 & 4 \\ - 1 & 7 & - 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} + 4 r _ {2}} \left( \begin{array}{c c c} 0 & 1 & 0 \\ - 1 & 7 & - 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} - 7 r _ {1} ^ {* *}} r _ {2} ^ {*} \times (- 1) \left( \begin{array}{c c c} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）<equation>(6E - A)x = 0</equation>的一个基础解系为<equation>\eta_1 = (-1,0,1)^{\mathrm{T}}.</equation>当<equation>\lambda=-3</equation>时，<equation>\begin{array}{l} - 3 E - A = \left( \begin{array}{c c c} - 5 & - 1 & 4 \\ - 1 & - 2 & - 1 \\ 4 & - 1 & - 5 \end{array} \right) \xrightarrow {r _ {3} + r _ {1}} \frac {r _ {3} ^ {*} - r _ {2}}{r _ {3} ^ {*}} \left( \begin{array}{c c c} - 5 & - 1 & 4 \\ - 1 & - 2 & - 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} - 5 r _ {2}} \frac {r _ {1} - 5 r _ {2}}{r _ {2} \times (- 1)} \left( \begin{array}{c c c} 0 & 9 & 9 \\ 1 & 2 & 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {1} ^ {*} \times \frac {1}{9}} \frac {r _ {2} ^ {*} - r _ {1} ^ {* *}}{r _ {2} ^ {*} - r _ {1} ^ {* *}} \left( \begin{array}{c c c} 0 & 1 & 1 \\ 1 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation><equation>(-3E - A)x = 0</equation>的一个基础解系为<equation>\eta_2 = (1, -1, 1)^{\mathrm{T}}.</equation>当<equation>\lambda=0</equation>时，<equation>\begin{array}{l} 0 E - A = \left( \begin{array}{c c c} - 2 & - 1 & 4 \\ - 1 & 1 & - 1 \\ 4 & - 1 & - 2 \end{array} \right) \xrightarrow {r _ {3} + r _ {1}} \frac {r _ {3} ^ {*} + 2 r _ {2}}{r _ {3} ^ {*} + 2 r _ {2}} \left( \begin{array}{c c c} - 2 & - 1 & 4 \\ - 1 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} - 2 r _ {2}} \frac {r _ {1} ^ {*} \times \left(- \frac {1}{3}\right)}{r _ {1} ^ {*} \times \left(- \frac {1}{3}\right)} \left( \begin{array}{c c c} 0 & 1 & - 2 \\ - 1 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} \times (- 1) + r _ {1} ^ {* *}} \left( \begin{array}{c c c} 0 & 1 & - 2 \\ 1 & 0 & - 1 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation><equation>(0E - A)x = 0</equation>的一个基础解系为<equation>\eta_3 = (1,2,1)^{\mathrm{T}}.</equation>由于实对称矩阵对应于不同特征值的特征向量相互正交，故只需要将所得特征向量单位化.

将<equation>\boldsymbol{\eta}_{1},\boldsymbol{\eta}_{2},\boldsymbol{\eta}_{3}</equation>分别单位化，作为Q的列向量，得正交矩阵<equation>Q=\left( \begin{array}{c c c} -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \\ 0 & -\frac{1}{\sqrt{3}} & \frac{2}{\sqrt{6}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \end{array} \right)</equation>，且<equation>Q^{\mathrm{T}}AQ=</equation><equation>\left( \begin{array}{c c c} 6 & 0 & 0 \\ 0 & - 3 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>即f在正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>下的标准形为<equation>f=6 y_{1}^{2}-3 y_{2}^{2}.</equation>

---

**2016年第8题 | 选择题 | 4分 | 答案: C**

8. 设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=a \left( x_{1}^{2}+x_{2}^{2}+x_{3}^{2} \right)+2 x_{1} x_{2}+2 x_{2} x_{3}+2 x_{1} x_{3}</equation>的正、负惯性指数分别为1，2，则（    )

A. a > 1 B. a < -2 C.<equation>- 2 < a < 1</equation>D. a=1或a=-2

答案: C

**解析:**解（法一）f对应的对称矩阵为<equation>A=\left( \begin{array}{c c c} a & 1 & 1 \\ 1 & a & 1 \\ 1 & 1 & a \end{array} \right).</equation>A正交相似于一个对角矩阵，该矩阵的主对角元为 A的特征值.

计算 A的特征多项式，得<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - a & - 1 & - 1 \\ - 1 & \lambda - a & - 1 \\ - 1 & - 1 & \lambda - a  \right| \xlongequal {c _ {2} - c _ {3}} \left| \begin{array}{c c c} \lambda - a & 0 & - 1 \\ - 1 & \lambda - a + 1 & - 1 \\ - 1 & - (\lambda - a + 1) & \lambda - a  \right| \\ \underline {{\text {按 第一 行 展 开}}} (\lambda - a) (\lambda - a + 1) (\lambda - a - 1) - 2 (\lambda - a + 1) \\ &= (\lambda - a + 1) ^ {2} (\lambda - a - 2). \end{aligned}</equation>因此，A的特征值为 a-1，a-1，a+2.

由于 a+2>a-1，故若 f的正、负惯性指数分别为1，2，则<equation>\left\{\begin{array}{l l}a-1<0,\\ a+2>0.\end{array}\right.</equation>解得-2<a<1.应选C.

（法二）如法一，写出 A.

由于二次型 f的正、负惯性指数分别为1，2，故 A的特征值有一个为正值，两个为负值，从而<equation>| A | > 0.</equation>计算 A的行列式.<equation>| A | = \left| \begin{array}{c c c} a & 1 & 1 \\ 1 & a & 1 \\ 1 & 1 & a \end{array} \right| = (a - 1) ^ {2} (a + 2).</equation>由于<equation>| A | > 0</equation>，故<equation>a+2>0</equation>，即<equation>a>-2.</equation>由此可以排除选项B和选项D.

另一方面，若 a > 1，则 a > 0，<equation>a^{2}-1>0</equation><equation>| A | > 0</equation>，A的各阶顺序主子式皆为正.由正定矩阵的判别法可知，A为正定矩阵，从而 f的正惯性指数为3.与f的正、负惯性指数分别为1，2矛盾，故可排除选项A.

因此，应选C.

---

**2015年第8题 | 选择题 | 4分 | 答案: A**

8. 设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>在正交变换<equation>x=P y</equation>下的标准形为<equation>2 y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>其中<equation>P=\left( e_{1}, e_{2}, e_{3} \right)</equation>若<equation>Q=\left( e_{1},-e_{3}, e_{2} \right)</equation>则<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>在正交变换<equation>x=Q y</equation>下的标准形为（    )

A.<equation>2 y_{1}^{2}-y_{2}^{2}+y_{3}^{2}</equation>B.<equation>2 y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>C.<equation>2 y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>D.<equation>2 y_{1}^{2}+y_{2}^{2}+y_{3}^{2}</equation>

答案: A

**解析:**解（法一）由题设知，二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>对应的对称矩阵 A满足<equation>P^{\mathrm{T}} A P=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -1 \end{array} \right).</equation>又由题设，<equation>Q=P\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{array} \right)</equation>，故<equation>Q^{\mathrm{T}} A Q=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{array} \right)\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -1 \end{array} \right)\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{array} \right)=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>因此，<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>在 x = Qy下的标准形为<equation>f=2 y_{1}^{2}-y_{2}^{2}+y_{3}^{2}.</equation>应选A.

（法二）由题设知，二次型<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>在正交变换<equation>\boldsymbol{x}=\boldsymbol{P}\boldsymbol{y}</equation>下的标准形为<equation>f=2y_{1}^{2}+y_{2}^{2}-y_{3}^{2}.</equation>因此，该二次型所对应的对称矩阵A的特征值为2，1，-1，而<equation>e_{1},e_{2},e_{3}</equation>分别为属于特征值2，1，-1的特征向量.

若<equation>Q=\left(e_{1},-e_{3},e_{2}\right)</equation>，则由<equation>A(-e_{3})=-Ae_{3}=-(-e_{3})</equation>可知<equation>-e_{3}</equation>也为属于特征值-1的特征向量，故<equation>Q^{\mathrm{T}}AQ=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{array} \right). f\left(x_{1},x_{2},x_{3}\right)</equation>在<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>下的标准形为<equation>f=2y_{1}^{2}-y_{2}^{2}+y_{3}^{2}.</equation>应选A.

---

**2014年第14题 | 填空题 | 4分**

14. 设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=x_{1}^{2}-x_{2}^{2}+2 a x_{1} x_{3}+4 x_{2} x_{3}</equation>的负惯性指数为1，则 a的取值范围是 ___

**解析:**解 （法一）用配方法将原二次型化为标准形.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= \left(x _ {1} + a x _ {3}\right) ^ {2} - a ^ {2} x _ {3} ^ {2} - \left(x _ {2} - 2 x _ {3}\right) ^ {2} + 4 x _ {3} ^ {2} \\ &= \left(x _ {1} + a x _ {3}\right) ^ {2} - \left(x _ {2} - 2 x _ {3}\right) ^ {2} + \left(4 - a ^ {2}\right) x _ {3} ^ {2}. \end{aligned}</equation>因此，若二次型<equation>f(x_{1},x_{2},x_{3})</equation>的负惯性指数为1，则<equation>4 - a^{2}\geqslant 0</equation>，即<equation>a\in [-2,2]</equation>（法二）写出二次型<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>对应的对称矩阵A.<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & 0 & a \\ 0 & - 1 & 2 \\ a & 2 & 0 \end{array} \right).</equation>计算<equation>A</equation>的行列式得，<equation>|A| = a^{2} - 4.</equation>A的迹等于零，说明A的特征值之和为零.

下面我们证明，当3阶非零实对称矩阵<equation>A</equation>的迹为零时，<equation>A</equation>的负惯性指数为1等价于<equation>|A| \leqslant 0.</equation>当3阶非零实对称矩阵<equation>A</equation>的迹为零时，由<equation>A</equation>的负惯性指数为1可知，<equation>A</equation>的特征值可能为两正、一负，或者一正、一零、一负.在这两种情形下，<equation>|A| \leqslant 0.</equation>若 A为3阶非零实对称矩阵，且<equation>|A| \leqslant 0</equation>，则 A的特征值的符号有五种可能：（1）两正、一负；（2）一正、一零、一负；（3）两零、一负；（4）三负；（5）全为零.两个零特征值、一个负特征值与三个负特征值的情形与 A的迹为零矛盾.特征值全为零的情形与 A是非零实对称矩阵矛盾，因为若 A的特征值全为零，则 A相似于零矩阵，从而 A为零矩阵.因此，A的特征值仅可能为两正、一负，或一正、一零、一负.在这两种情形下，A的负惯性指数都为1.

综上所述，<equation>A</equation>的负惯性指数为1等价于<equation>|A| \leqslant 0</equation>，即<equation>a \in [-2,2]</equation>

---

**2013年第23题 | 解答题 | 11分**


设二次型<equation>f\left(x_{1},x_{2},x_{3}\right)=2\left(a_{1}x_{1}+a_{2}x_{2}+a_{3}x_{3}\right)^{2}+\left(b_{1}x_{1}+b_{2}x_{2}+b_{3}x_{3}\right)^{2}</equation>，记<equation>\begin{aligned} \alpha &= \left(  a _ {1} \\ a _ {2} \\ a _ {3}  \right), \quad \beta &= \left(  b _ {1} \\ b _ {2} \\ b _ {3}  \right) \end{aligned}</equation>I. 证明二次型 f对应的矩阵为<equation>2\alpha\alpha^{\mathrm{T}}+\beta\beta^{\mathrm{T}};</equation>II. 若<equation>\alpha, \beta</equation>正交且均为单位向量，证明 f在正交变换下的标准形为<equation>2 y_{1}^{2}+y_{2}^{2}.</equation>

**答案:**（23）（Ⅰ）证明略；

（Ⅱ）证明略.

**解析:**证（I）记<equation>\boldsymbol{x}=\left(x_{1},x_{2},x_{3}\right)^{\mathrm{T}}</equation><equation>f</equation>对应的矩阵为A,A为对称矩阵，则<equation>a _ {1} x _ {1} + a _ {2} x _ {2} + a _ {3} x _ {3} = \boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\alpha} = \boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {x}, \quad b _ {1} x _ {1} + b _ {2} x _ {2} + b _ {3} x _ {3} = \boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\beta} = \boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {x}.</equation><equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = 2 \left(\boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\alpha}\right) \left(\boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {x}\right) + \left(\boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\beta}\right) \left(\boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {x}\right) = \boldsymbol {x} ^ {\mathrm {T}} \left(2 \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}\right) \boldsymbol {x}.</equation>又由于<equation>(2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}})^{\mathrm{T}} = 2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>，故<equation>2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>是对称矩阵.于是<equation>2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>为所求A.

（Ⅱ）（法一）由<equation>A = 2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>且<equation>\alpha</equation>与<equation>\beta</equation>相互正交<equation>(\alpha^{\mathrm{T}}\beta = 0, \beta^{\mathrm{T}}\alpha = 0)</equation>得，<equation>A \alpha = \left(2 \alpha \alpha^ {\mathrm {T}} + \beta \beta^ {\mathrm {T}}\right) \alpha = 2 \alpha , \quad A \beta = \left(2 \alpha \alpha^ {\mathrm {T}} + \beta \beta^ {\mathrm {T}}\right) \beta = \beta .</equation>因此，2,1均为<equation>A</equation>的特征值，而<equation>\alpha ,\beta</equation>分别为属于特征值2，1的特征向量.

下面还需确定 A的另一个特征值.

考虑 A的秩.

由于对任何非零<equation>n</equation>维列向量<equation>\alpha ,\beta ,</equation>矩阵<equation>\beta \alpha^{\mathrm{T}}</equation>的秩均为1，故<equation>r (\boldsymbol {A}) = r \left(2 \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}\right) \leqslant r \left(2 \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}}\right) + r \left(\boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}\right) = 2.</equation>于是，<equation>\mathbf{A}</equation>不满秩，0也是<equation>\mathbf{A}</equation>的特征值.

因此，存在正交矩阵<equation>P</equation>使得<equation>P^{\mathrm{T}}AP=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right). f</equation>在正交变换<equation>x=Py</equation>下的标准形为<equation>f=2y_{1}^{2}+y_{2}^{2}.</equation>（法二）取<equation>\gamma</equation>为与<equation>\alpha, \beta</equation>均正交的单位向量，可取<equation>\gamma = \frac{\alpha \times \beta}{\| \alpha \times \beta \|}</equation><equation>(\alpha \times \beta</equation>为向量<equation>\alpha, \beta</equation>的向量积，<equation>\| \alpha \times \beta \|</equation>是向量<equation>\alpha \times \beta</equation>的模），则<equation>P=(\alpha ,\beta ,\gamma)</equation>为正交矩阵.<equation>\begin{aligned} P ^ {\mathrm {T}} A P &= \left(  \boldsymbol {\alpha} ^ {\mathrm {T}} \\ \boldsymbol {\beta} ^ {\mathrm {T}} \\ \boldsymbol {\gamma} ^ {\mathrm {T}}  \right) \left(2 \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}\right) (\boldsymbol {\alpha}, \boldsymbol {\beta}, \gamma) &= \left(  2 \boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}} \\ 2 \boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}} \\ 2 \boldsymbol {\gamma} ^ {\mathrm {T}} \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\gamma} ^ {\mathrm {T}} \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}  \right) (\boldsymbol {\alpha}, \boldsymbol {\beta}, \gamma). \end{aligned}</equation>由于<equation>\alpha, \beta, \gamma</equation>相互正交，故<equation>\alpha^{\mathrm{T}}\boldsymbol{\beta} = \beta^{\mathrm{T}}\alpha = \gamma^{\mathrm{T}}\alpha = \gamma^{\mathrm{T}}\boldsymbol{\beta} = 0, \alpha^{\mathrm{T}}\alpha = \beta^{\mathrm{T}}\boldsymbol{\beta} = 1.</equation><equation>\boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} = \left( \begin{array}{c} 2 \boldsymbol {\alpha} ^ {\mathrm {T}} \\ \boldsymbol {\beta} ^ {\mathrm {T}} \\ \mathbf {0} \end{array} \right) (\boldsymbol {\alpha}, \boldsymbol {\beta}, \gamma) = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>因此，<equation>f</equation>在正交变换<equation>\pmb{x} = \pmb{P}\pmb{y}</equation>下的标准形为<equation>f = 2y_{1}^{2} + y_{2}^{2}</equation>.

---

**2012年第23题 | 解答题 | 11分**

23. （本题满分11分）

已知<equation>A=\left( \begin{array}{c c c}1&0&1\\ 0&1&1\\ -1&0&a\\ 0&a&-1 \end{array} \right),</equation>二次型<equation>f \left( x_{1}, x_{2}, x_{3}\right)=\boldsymbol{x}^{\mathrm{T}} \left( \boldsymbol{A}^{\mathrm{T}} \boldsymbol{A}\right) \boldsymbol{x}</equation>的秩为2.

I. 求实数 a的值；

II. 求正交变换<equation>x=Q y</equation>将 f化为标准形.

**答案:**(23) （I）<equation>a=-1;</equation>（Ⅱ）<equation>Q=\left( \begin{array}{c c c} {\frac{1}{\sqrt{6}}} & {-\frac{1}{\sqrt{2}}} & {-\frac{1}{\sqrt{3}}} \\ {\frac{1}{\sqrt{6}}} & {\frac{1}{\sqrt{2}}} & {-\frac{1}{\sqrt{3}}} \\ {\frac{2}{\sqrt{6}}} & {0} & {\frac{1}{\sqrt{3}}} \end{array} \right)</equation>正交变换<equation>x=Q y</equation>将二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>变成标准形<equation>f = 6 y _ {1} ^ {2} + 2 y _ {2} ^ {2}.</equation>

**解析:**解（I）（法一）二次型<equation>f</equation>的秩等于它所对应的实对称矩阵<equation>A^{\mathrm{T}}A</equation>的秩，于是<equation>r(A^{\mathrm{T}}A) = 2.</equation><equation>r \left(\boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {A}\right) = r (\boldsymbol {A})</equation>由于<equation>A^{\mathrm{T}}A</equation>与A的列数相等，故证明<equation>r(A^{\mathrm{T}}A)=r(A)</equation>只需要证明<equation>A^{\mathrm{T}}Ax=0</equation>与<equation>Ax=0</equation>同解若 x满足<equation>Ax=0</equation>，则<equation>A^{\mathrm{T}}(Ax)=0</equation>即<equation>(A^{\mathrm{T}}A)x=0.</equation>另一方面，若 x满足<equation>\left( A^{\mathrm{T}} A \right) x=0</equation>，则<equation>x^{\mathrm{T}} \left( A^{\mathrm{T}} A \right) x=0</equation>，即<equation>\left( A x \right)^{\mathrm{T}} \left( A x \right)=0</equation>.由于<equation>\alpha^{\mathrm{T}}\alpha=0</equation>当且仅当<equation>\alpha=0</equation>，故<equation>A x=0.</equation><equation>\text {因 此}, r (\mathbf {A}) = r \left(\mathbf {A} ^ {\mathrm {T}} \mathbf {A}\right) = 2</equation>我们可以对<equation>A</equation>作初等行变换，求得<equation>r(A) = 2</equation>时的<equation>a</equation>的值.<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ - 1 & 0 & a \\ 0 & a & - 1 \end{array} \right) \xrightarrow [ r _ {4} - a r _ {2} ]{r _ {3} + r _ {1}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & a + 1 \\ 0 & 0 & - a - 1 \end{array} \right) \xrightarrow [ r _ {4} ^ {*} + r _ {3} ^ {*} ]{r _ {4} ^ {*} + r _ {3} ^ {*}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & a + 1 \\ 0 & 0 & 0 \end{array} \right).</equation>由此看出，仅当<equation>a + 1 = 0</equation>时，<equation>r(A) = 2</equation>，故<equation>a = -1.</equation>（法二）由于<equation>r(\mathbf{A}^{\mathrm{T}}\mathbf{A}) = 2</equation>，而<equation>\mathbf{A}^{\mathrm{T}}\mathbf{A}</equation>为<equation>3\times 3</equation>矩阵，故<equation>|\mathbf{A}^{\mathrm{T}}\mathbf{A}| = 0.</equation><equation>\boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {A} = \left( \begin{array}{c c c c} 1 & 0 & - 1 & 0 \\ 0 & 1 & 0 & a \\ 1 & 1 & a & - 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ - 1 & 0 & a \\ 0 & a & - 1 \end{array} \right) = \left( \begin{array}{c c c} 2 & 0 & 1 - a \\ 0 & 1 + a ^ {2} & 1 - a \\ 1 - a & 1 - a & 3 + a ^ {2} \end{array} \right).</equation>求得<equation>|\mathbf{A}^{\mathrm{T}}\mathbf{A}| = (a^{2} + 3)(a + 1)^{2}</equation>. 因此，由<equation>|\mathbf{A}^{\mathrm{T}}\mathbf{A}| = 0</equation>可得<equation>a = -1</equation>.

（Ⅱ）由第（I）问可得，<equation>A^{\mathrm{T}}A = \left( \begin{array}{c c c} 2 & 0 & 2 \\ 0 & 2 & 2 \\ 2 & 2 & 4 \end{array} \right)</equation>从而<equation>A^{\mathrm{T}}A</equation>的特征多项式为<equation>| \lambda E - A ^ {\mathrm {T}} A | = \left| \begin{array}{c c c} \lambda - 2 & 0 & - 2 \\ 0 & \lambda - 2 & - 2 \\ - 2 & - 2 & \lambda - 4 \end{array} \right| = \lambda (\lambda - 2) (\lambda - 6).</equation><equation>A^{\mathrm{T}}A</equation>的特征值为6,2,0.

下面分别计算属于特征值6，2，0的特征向量

当<equation>\lambda=6</equation>时，<equation>\begin{array}{l} 6 E - A ^ {\mathrm {T}} A = \left( \begin{array}{c c c} 4 & 0 & - 2 \\ 0 & 4 & - 2 \\ - 2 & - 2 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 0 & 2 & - 1 \\ 1 & 1 & - 1 \end{array} \right) \xrightarrow {r _ {3} - r _ {2}} \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 0 & 2 & - 1 \\ 1 & - 1 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} - r _ {1} + 2 r _ {3} ^ {*}} \frac {1}{r _ {2} ^ {*} \leftrightarrow r _ {3} ^ {*}} \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 1 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right), \\ \end{array}</equation>得<equation>\left\{ \begin{array}{l} 2x_{1} - x_{3} = 0, \\ x_{1} - x_{2} = 0. \end{array} \right.</equation>解得<equation>\xi_{1} = (1,1,2)^{\mathrm{T}}</equation>为该方程组的一个基础解系.

当<equation>\lambda=2</equation>时，<equation>2 \boldsymbol {E} - \boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {A} = \left( \begin{array}{c c c} 0 & 0 & - 2 \\ 0 & 0 & - 2 \\ - 2 & - 2 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right),</equation>得<equation>\left\{ \begin{array}{l l} x_{1} + x_{2} = 0, \\ x_{3} = 0. \end{array} \right.</equation>解得<equation>\xi_{2} = (-1,1,0)^{\mathrm{T}}</equation>为该方程组的一个基础解系.

当<equation>\lambda=0</equation>时，<equation>0 \boldsymbol {E} - \boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {A} = \left( \begin{array}{c c c} - 2 & 0 & - 2 \\ 0 & - 2 & - 2 \\ - 2 & - 2 & - 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 2 \end{array} \right) \xrightarrow {r _ {3} - r _ {1} - r _ {2}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right),</equation>得<equation>\left\{ \begin{array}{l l} x_{1} + x_{3} = 0, \\ x_{2} + x_{3} = 0. \end{array} \right.</equation>解得<equation>\xi_{3} = (-1, -1, 1)^{\mathrm{T}}</equation>为该方程组的一个基础解系.

由于实对称矩阵属于不同特征值的特征向量相互正交，故<equation>\xi_{1},\xi_{2},\xi_{3}</equation>相互正交.将<equation>\xi_{1},\xi_{2},\xi_{3}</equation>单位化，得<equation>\boldsymbol {\alpha} _ {1} = \frac {1}{\sqrt {6}} \left( \begin{array}{c} 1 \\ 1 \\ 2 \end{array} \right), \quad \boldsymbol {\alpha} _ {2} = \frac {1}{\sqrt {2}} \left( \begin{array}{c} - 1 \\ 1 \\ 0 \end{array} \right), \quad \boldsymbol {\alpha} _ {3} = \frac {1}{\sqrt {3}} \left( \begin{array}{c} - 1 \\ - 1 \\ 1 \end{array} \right).</equation>取<equation>Q = \left(\alpha_{1},\alpha_{2},\alpha_{3}\right)</equation>，则<equation>Q</equation>为正交矩阵，且<equation>Q^{\mathrm{T}} \left(A^{\mathrm{T}} A\right) Q = \left( \begin{array}{c c c} 6 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>因此，正交变换<equation>x = Qy</equation>将二次型<equation>f\left(x_{1}, x_{2}, x_{3}\right)</equation>变成标准形<equation>f = 6y_{1}^{2} + 2y_{2}^{2}</equation>.

---

**2011年第14题 | 填空题 | 4分**

14. 二次型<equation>f(x_{1},x_{2},x_{3})=x_{1}^{2}+3x_{2}^{2}+x_{3}^{2}+2x_{1}x_{2}+2x_{1}x_{3}+2x_{2}x_{3}</equation>, 则 f的正惯性指数为 ___

**解析:**解（法一）二次型<equation>f</equation>对应的对称矩阵<equation>A = \left( \begin{array}{c c c} 1 & 1 & 1 \\ 1 & 3 & 1 \\ 1 & 1 & 1 \end{array} \right).</equation>计算 A的特征多项式得，<equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda - 1 & - 1 & - 1 \\ - 1 & \lambda - 3 & - 1 \\ - 1 & - 1 & \lambda - 1 \end{array} \right| = \lambda (\lambda - 1) (\lambda - 4).</equation>A的特征值为0，1，4，其中正特征值的个数为2.

因此，<equation>f</equation>的正惯性指数为2.

（法二）配方法.

若对完全平方式<equation>\left(x _ {1} + x _ {2} + x _ {3}\right) ^ {2} = x _ {1} ^ {2} + x _ {2} ^ {2} + x _ {3} ^ {2} + 2 x _ {1} x _ {2} + 2 x _ {1} x _ {3} + 2 x _ {2} x _ {3}</equation>较熟悉，则能够较快地写出<equation>f</equation>的标准形.<equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = x _ {1} ^ {2} + 3 x _ {2} ^ {2} + x _ {3} ^ {2} + 2 x _ {1} x _ {2} + 2 x _ {1} x _ {3} + 2 x _ {2} x _ {3} = \left(x _ {1} + x _ {2} + x _ {3}\right) ^ {2} + 2 x _ {2} ^ {2}.</equation>或者如下计算.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= x _ {1} ^ {2} + 2 x _ {1} \left(x _ {2} + x _ {3}\right) + \left(x _ {2} + x _ {3}\right) ^ {2} + 3 x _ {2} ^ {2} + x _ {3} ^ {2} + 2 x _ {2} x _ {3} - \left(x _ {2} + x _ {3}\right) ^ {2} \\ &= \left(x _ {1} + x _ {2} + x _ {3}\right) ^ {2} + 2 x _ {2} ^ {2}. \end{aligned}</equation>因此，<equation>f</equation>的正惯性指数为2.

---

**2009年第23题 | 解答题 | 11分**

3. (本题满分11分)

设二次型<equation>f ( x_{1}, x_{2}, x_{3} )=a x_{1}^{2}+a x_{2}^{2}+( a-1 ) x_{3}^{2}+2 x_{1} x_{3}-2 x_{2} x_{3}</equation>.

I. 求二次型 f的矩阵的所有特征值；

II. 若二次型 f的规范形为<equation>y_{1}^{2}+y_{2}^{2}</equation>，求 a的值.

**答案:**(23) ( I ) a, a-2, a+1;

( II ) a=2.

**解析:**解（I）二次型<equation>f</equation>的矩阵为<equation>A = \left( \begin{array}{c c c} a & 0 & 1 \\ 0 & a & -1 \\ 1 & -1 & a - 1 \end{array} \right).</equation>计算<equation>A</equation>的特征多项式<equation>|\lambda E - A|</equation>，得<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - a & 0 & - 1 \\ 0 & \lambda - a & 1 \\ - 1 & 1 & \lambda - a + 1  \right| \xlongequal {\text {按 第一 行 展 开}} (\lambda - a) \left[ (\lambda - a) (\lambda - a + 1) - 1 \right] - (\lambda - a) \\ &= (\lambda - a) (\lambda - a + 2) (\lambda - a - 1). \end{aligned}</equation>因此，<equation>A</equation>的特征值为<equation>a, a - 2, a + 1.</equation>（Ⅱ）由<equation>f</equation>的规范形为<equation>y_{1}^{2} + y_{2}^{2}</equation>知，<equation>A</equation>的特征值有两个正数，一个为零.0为最小的特征值.

由于<equation>a - 2 < a < a + 1</equation>，故可知<equation>a - 2 = 0</equation>，即<equation>a = 2</equation>

---


### 行列式

**2021年第16题 | 填空题 | 5分**
16. 多项式 f(x) =<equation>\left| \begin{array}{c c c c} x & x & 1 & 2 x \\ 1 & x & 2 & - 1 \\ 2 & 1 & x & 1 \\ 2 & - 1 & 1 & x \end{array} \right|</equation>的<equation>x^{3}</equation>项的系数为 ___
**解析: **解 由于所给行列式的元素均为常数或 x的倍数，故根据行列式的定义，要出现<equation>x^{3}</equation>项，必须从不同行、不同列中取出3个含 x的项相乘.

将行列式记为<equation>\det ( a_{ij} ).</equation><equation>\textcircled{1} a_{11}=x</equation>不能取.若取<equation>a_{11}</equation>，则第一行中的 x与 2x不能取.于是，剩下的2个含 x的元素必来自主对角线上的3个x.无论从<equation>a_{22},a_{33},a_{44}</equation>中取哪两个，第四个元素都只能来自主对角线，从而这种取法最终将得到<equation>x^{4}</equation>，而不是<equation>x^{3}.</equation><equation>\left| \begin{array}{c c c c} \underline {{x}} & x & 1 & 2 x \\ 1 & \underline {{x}} & 2 & - 1 \\ 2 & 1 & \underline {{x}} & 1 \\ 2 & - 1 & 1 & \underline {{x}} \end{array} \right|</equation><equation>\textcircled{2}</equation>由于<equation>x^{3}</equation>项必来自于不同列的含x元素的乘积，故确定<equation>a_{11}</equation>不取后，x必来自后三列，而第三列中仅<equation>a_{33}=x</equation>，从而必取.

下面分情况讨论.

(1) 若第二列中取<equation>a_{12}=x</equation>，则组合应为<equation>a_{12}a_{21}a_{33}a_{44}</equation>.该组合对应排列2，1，3，4，逆序数为1.于是，所得<equation>x^{3}</equation>项为<equation>(-1)^{1}\cdot1\cdot x^{3}=-x^{3}.</equation>(2) 若第二列中取<equation>a_{22}=x</equation>，则组合应为<equation>a_{14}a_{22}a_{33}a_{41}</equation>.该组合对应排列4，2，3，1，逆序数为5.于是，所得<equation>x^{3}</equation>项为<equation>(-1)^{5}\cdot 2\cdot 2x^{3}=-4x^{3}.</equation><equation>\left| \begin{array}{c c c c} x & \underline {{x}} & 1 & 2 x \\ 1 & x & 2 & - 1 \\ 2 & 1 & \underline {{x}} & 1 \\ 2 & - 1 & 1 & \underline {{x}} \end{array} \right|, \quad \left| \begin{array}{c c c c} x & x & 1 & 2 x \\ 1 & \underline {{x}} & 2 & - 1 \\ 2 & 1 & \underline {{x}} & 1 \\ 2 & - 1 & 1 & x \end{array} \right|</equation>因此，<equation>f ( x )</equation>的<equation>x^{3}</equation>项为<equation>- x^{3}-4 x^{3}=-5 x^{3}, x^{3}</equation>的系数为-5.

---

**2020年第14题 | 填空题 | 4分**
14. 行列式<equation>\left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a \end{array} \right| = \underline {{\quad}}</equation>
**答案: **<equation>a^{4}-4 a^{2}.</equation>
**解析: **解（法一）利用行列式的性质对所求行列式进行转化.

若 a=0 ，则将第二行加到第一行可得零行，从而行列式为0.

若 a≠0，则<equation>\begin{aligned} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a  \right| \frac {r _ {4} + r _ {3}}{\hline} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 0 & 0 & a & a  \right| \frac {r _ {3} + \frac {1}{a} r _ {1}}{\hline} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ 0 & 1 & a - \frac {1}{a} & \frac {1}{a} \\ 0 & 0 & a & a  \right| \\ \frac {r _ {3} - \frac {1}{a} r _ {2}}{\hline} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ 0 & 0 & a - \frac {2}{a} & \frac {2}{a} \\ 0 & 0 & a & a  \right| &= \left| \begin{array}{c c} a & 0 \\ 0 & a  \right| \cdot \left| \begin{array}{c c} a - \frac {2}{a} & \frac {2}{a} \\ a & a  \right| \\ &= a ^ {2} \left[ \left(a - \frac {2}{a}\right) a - 2 \right] = a ^ {2} \left(a ^ {2} - 4\right) = a ^ {4} - 4 a ^ {2}. \end{aligned}</equation>不论是哪种情况，所求行列式均为<equation>a^{4}-4 a^{2}.</equation>（法二）注意到所求行列式的各行元素之和均为 a，故可将各列均加到第1列，然后计算行列式.<equation>\begin{array}{l} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a \end{array} \right| \frac {c _ {1} + c _ {2} + c _ {3} + c _ {4}}{\hline} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ a & a & 1 & - 1 \\ a & 1 & a & 0 \\ a & - 1 & 0 & a \end{array} \right| = a \left| \begin{array}{c c c c} 1 & 0 & - 1 & 1 \\ 1 & a & 1 & - 1 \\ 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a \end{array} \right| \\ \frac {c _ {3} + c _ {1}}{c _ {4} - c _ {1}} a \left| \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 1 & a & 2 & - 2 \\ 1 & 1 & a + 1 & - 1 \\ 1 & - 1 & 1 & a - 1 \end{array} \right| \frac {c _ {3} + c _ {4}}{\hline} a \left| \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 1 & a & 0 & - 2 \\ 1 & 1 & a & - 1 \\ 1 & - 1 & a & a - 1 \end{array} \right| \\ \frac {\mathrm {按 第一 行 展开}}{\mathrm {=} a ^ {4} - 4 a ^ {2}} a \left\{a \left[ a (a - 1) + a \right] - 2 (a + a) \right\} = a \left(a ^ {3} - 4 a\right) \\ \end{array}</equation>

---

**2019年第14题 | 填空题 | 4分**
14. 已知矩阵<equation>A=\left( \begin{array}{c c c c} 1 & -1 & 0 & 0 \\ -2 & 1 & -1 & 1 \\ 3 & -2 & 2 & -1 \\ 0 & 0 & 3 & 4 \end{array} \right), A_{ij}</equation>表示<equation>|A|</equation>中（i,j）元的代数余子式，则<equation>A_{11}-A_{12}=</equation>___
**答案: **-4.
**解析: **按 A的第一行展开计算<equation>|A|</equation>，可得<equation>| \boldsymbol {A} | = 1 \cdot A _ {1 1} + (- 1) \cdot A _ {1 2} = A _ {1 1} - A _ {1 2}.</equation>因此，<equation>\begin{aligned} A _ {1 1} - A _ {1 2} &= | A | = \left| \begin{array}{c c c c} 1 & - 1 & 0 & 0 \\ - 2 & 1 & - 1 & 1 \\ 3 & - 2 & 2 & - 1 \\ 0 & 0 & 3 & 4  \right| \underline {{\frac {c _ {2} + c _ {1}}{2}}} \left| \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ - 2 & - 1 & - 1 & 1 \\ 3 & 1 & 2 & - 1 \\ 0 & 0 & 3 & 4  \right| \\ &= 1 \cdot \left| \begin{array}{c c c} - 1 & - 1 & 1 \\ 1 & 2 & - 1 \\ 0 & 3 & 4  \right| \underline {{\frac {c _ {3} + c _ {1}}{2}}} \left| \begin{array}{c c c} - 1 & - 1 & 0 \\ 1 & 2 & 0 \\ 0 & 3 & 4  \right| \end{aligned}</equation><equation>\frac {\mathrm {按 第三 列 展 开}}{2} 4 \cdot \left| \begin{array}{c c} - 1 & - 1 \\ 1 & 2 \end{array} \right| = - 4.</equation>

---

**2014年第7题 | 选择题 | 4分 | 答案: B**
7. 行列式<equation>\left| \begin{array}{c c c c} 0 & a & b & 0 \\ a & 0 & 0 & b \\ 0 & c & d & 0 \\ c & 0 & 0 & d \end{array} \right|=</equation>(    )

A.<equation>( a d-b c )^{2}</equation>B.<equation>-( a d-b c )^{2}</equation>C.<equation>a^{2} d^{2}-b^{2} c^{2}</equation>D.<equation>b^{2} c^{2}-a^{2} d^{2}</equation>
答案: B
**解析: **解（法一）将原行列式作初等变换使之与分块对角矩阵的行列式建立联系.根据行列式的性质，交换两行或两列，所得新行列式为原行列式的负值.<equation>\left| \begin{array}{c c c c} 0 & a & b & 0 \\ a & 0 & 0 & b \\ 0 & c & d & 0 \\ c & 0 & 0 & d \end{array} \right| = - \left| \begin{array}{c c c c} 0 & a & b & 0 \\ 0 & c & d & 0 \\ a & 0 & 0 & b \\ c & 0 & 0 & d \end{array} \right| = \left| \begin{array}{c c c c} a & 0 & b & 0 \\ c & 0 & d & 0 \\ 0 & a & 0 & b \\ 0 & c & 0 & d \end{array} \right| = - \left| \begin{array}{c c c c} a & b & 0 & 0 \\ c & d & 0 & 0 \\ 0 & 0 & a & b \\ 0 & 0 & c & d \end{array} \right| = - (a d - b c) ^ {2}.</equation>应选B.

（法二）按第一行展开.<equation>\left| \begin{array}{c c c c} 0 & a & b & 0 \\ a & 0 & 0 & b \\ 0 & c & d & 0 \\ c & 0 & 0 & d \end{array} \right| = (- a) \left| \begin{array}{c c c} a & 0 & b \\ 0 & d & 0 \\ c & 0 & d \end{array} \right| + b \left| \begin{array}{c c c} a & 0 & b \\ 0 & c & 0 \\ c & 0 & d \end{array} \right| = - a ^ {2} d ^ {2} + a b c d + a b c d - b ^ {2} c ^ {2} = - (a d - b c) ^ {2}.</equation>应选B.

---


**2023年第20题 | 解答题 | 12分**

设平面有界区域 D位于第一象限，由曲线<equation>x^{2}+y^{2}-xy=1, x^{2}+y^{2}-xy=2</equation>与直线<equation>y=\sqrt{3} x, y=0</equation>围成，计算<equation>\iint_{D} \frac{1}{3 x^{2}+y^{2}} \mathrm{d} x \mathrm{d} y.</equation>
**答案: **##<equation>\frac{\sqrt{3}\pi\ln 2}{24}.</equation>
**解析: **20 设平面有界区域 D位于第一象限，由曲线<equation>x^{2}+y^{2}-xy=1, x^{2}+y^{2}-xy=2</equation>与直线<equation>y=\sqrt{3} x</equation>y=0围成，计算<equation>\iint_{D}\frac{1}{3x^{2}+y^{2}}\mathrm{d}x\mathrm{d}y.</equation>分析 本题主要考查二重积分的计算.

根据区域的特点，我们可以在极坐标系下计算二重积分.

解 在极坐标系下计算.

由<equation>\left\{ \begin{array}{l l} x=r\cos \theta \\ y=r\sin \theta \end{array} \right.</equation>可知，曲线<equation>x^{2}+y^{2}-xy=1, x^{2}+y^{2}-xy=2</equation>的极坐标方程分别为<equation>r ^ {2} - r ^ {2} \sin \theta \cos \theta = 1, \quad r ^ {2} - r ^ {2} \sin \theta \cos \theta = 2,</equation>即<equation>r=\frac{1}{\sqrt{1-\sin \theta}\cos \theta}, r=\frac{\sqrt{2}}{\sqrt{1-\sin \theta}\cos \theta}</equation>. 直线 y=<equation>\sqrt{3} x</equation>的极坐标方程为<equation>\theta=\frac{\pi}{3}</equation>. 于是，区域 D在极坐标系下的表示为<equation>D = \left\{(r, \theta) \mid \frac {1}{\sqrt {1 - \sin \theta \cos \theta}} \leqslant r \leqslant \frac {\sqrt {2}}{\sqrt {1 - \sin \theta \cos \theta}}, 0 \leqslant \theta \leqslant \frac {\pi}{3} \right\}.</equation>因此，<equation>\begin{aligned} \iint_ {D} \frac {1}{3 x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \iint_ {D} \frac {r \mathrm {d} r \mathrm {d} \theta}{3 r ^ {2} \cos^ {2} \theta + r ^ {2} \sin^ {2} \theta} &= \int_ {0} ^ {\frac {\pi}{3}} \mathrm {d} \theta \int_ {\frac {1}{\sqrt {1 - \sin \theta} \cos \theta}} ^ {\frac {\sqrt {2}}{\sqrt {1 - \sin \theta} \cos \theta}} \frac {r \mathrm {d} r}{3 r ^ {2} \cos^ {2} \theta + r ^ {2} \sin^ {2} \theta} \\ &= \frac {1}{2} \int_ {0} ^ {\frac {\pi}{3}} \frac {1}{3 \cos^ {2} \theta + \sin^ {2} \theta} \mathrm {d} \theta \int_ {\frac {1}{\sqrt {1 - \sin \theta} \cos \theta}} ^ {\frac {\sqrt {2}}{\sqrt {1 - \sin \theta} \cos \theta}} \frac {\mathrm {d} \left(r ^ {2}\right)}{r ^ {2}} \\ &= \frac {1}{2} \int_ {0} ^ {\frac {\pi}{3}} \frac {1}{3 \cos^ {2} \theta + \sin^ {2} \theta} \cdot \ln r ^ {2} \left| \frac {\frac {\sqrt {2}}{\sqrt {1 - \sin \theta} \cos \theta}}{\frac {1}{\sqrt {1 - \sin \theta} \cos \theta}} \right| \mathrm {d} \theta = \frac {\ln 2}{2} \int_ {0} ^ {\frac {\pi}{3}} \frac {\mathrm {d} \theta}{\cos^ {2} \theta \left(3 + \tan^ {2} \theta\right)} \\ &= \frac {\ln 2}{2} \int_ {0} ^ {\frac {\pi}{3}} \frac {\mathrm {d} (\tan \theta)}{3 + \tan^ {2} \theta} \frac {t = \tan \theta}{2} \frac {\ln 2}{2} \int_ {0} ^ {\sqrt {3}} \frac {\mathrm {d} t}{3 + t ^ {2}} = \frac {\ln 2}{2 \sqrt {3}} \int_ {0} ^ {\sqrt {3}} \frac {\mathrm {d} \left(\frac {t}{\sqrt {3}}\right)}{1 + \left(\frac {t}{\sqrt {3}}\right) ^ {2}} \\ &= \frac {\sqrt {3} \ln 2}{6} \arctan \frac {t}{\sqrt {3}} \Bigg | _ {0} ^ {\sqrt {3}} = \frac {\sqrt {3} \ln 2}{6} \cdot \frac {\pi}{4} = \frac {\sqrt {3} \pi \ln 2}{2 4}. \end{aligned}</equation>

---

**2022年第19题 | 解答题 | 12分**
19. (本题满分12分）

已知平面区域 D = {（x,y）| y-2≤x≤<equation>\sqrt{4-y^{2}}</equation>, 0≤y≤2} ，计算 I =<equation>\iint_{D} \frac{(x-y)^{2}}{x^{2}+y^{2}} \mathrm{d} x \mathrm{d} y.</equation>
**答案: **## I = 2<equation>\pi</equation>- 2.
**解析: **## 解 在极坐标系下计算.

由 D的表达式可知，如图（a）所示，D是由直线<equation>y=x+2</equation>，圆<equation>x^{2}+y^{2}=4</equation>以及x轴围成的部分直线<equation>y=x+2</equation>在极坐标系下的表示为<equation>r=\frac{2}{\sin \theta -\cos \theta}</equation>，圆<equation>x^{2}+y^{2}=4</equation>在极坐标系下的表示为<equation>r=2.</equation>(a)

(b)

如图（b）所示，将<equation>D</equation>分为两部分<equation>D_{1}</equation>和<equation>D_{2}</equation>.<equation>D _ {1} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2, 0 \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation><equation>D _ {2} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \frac {2}{\sin \theta - \cos \theta}, \frac {\pi}{2} \leqslant \theta \leqslant \pi \right\}.</equation>因此，<equation>\begin{aligned} \iint_ {D} \frac {\left(x - y\right) ^ {2}}{x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \iint_ {D} \frac {r ^ {2} \left(\cos \theta - \sin \theta\right) ^ {2}}{r ^ {2}} \cdot r \mathrm {d} r \mathrm {d} \theta &= \iint_ {D} \left(\cos \theta - \sin \theta\right) ^ {2} \cdot r \mathrm {d} r \mathrm {d} \theta \\ &= \int_ {0} ^ {\frac {\pi}{2}} \left(\cos \theta - \sin \theta\right) ^ {2} \mathrm {d} \theta \int_ {0} ^ {2} r \mathrm {d} r + \int_ {\frac {\pi}{2}} ^ {\pi} \left(\cos \theta - \sin \theta\right) ^ {2} \mathrm {d} \theta \int_ {0} ^ {\frac {2}{\sin \theta - \cos \theta}} r \mathrm {d} r \\ &= 2 \int_ {0} ^ {\frac {\pi}{2}} \left(1 - 2 \sin \theta \cos \theta\right) \mathrm {d} \theta + \int_ {\frac {\pi}{2}} ^ {\pi} \left(\cos \theta - \sin \theta\right) ^ {2} \cdot \frac {r ^ {2}}{2} \Bigg | _ {0} ^ {\frac {2}{\sin \theta - \cos \theta}} \mathrm {d} \theta \\ &= 2 \left(\frac {\pi}{2} - \sin^ {2} \theta \Bigg | _ {0} ^ {\frac {\pi}{2}}\right) + \int_ {\frac {\pi}{2}} ^ {\pi} \left(\cos \theta - \sin \theta\right) ^ {2} \cdot \frac {2}{\left(\sin \theta - \cos \theta\right) ^ {2}} \mathrm {d} \theta \\ &= \pi - 2 + 2 \times \left(\pi - \frac {\pi}{2}\right) = 2 \pi - 2. \end{aligned}</equation>

---

**2021年第21题 | 解答题 | 12分**
21. (本题满分12分)

曲线<equation>( x^{2}+y^{2} )^{2}=x^{2}-y^{2}</equation><equation>( x \geqslant0,y \geqslant0)</equation>与 x轴围成的区域为 D，求<equation>\iint_{D} xy\mathrm{d}x\mathrm{d}y.</equation>
**答案: **# 1 48
**解析: **解曲线<equation>( x^{2}+y^{2})^{2}=x^{2}-y^{2}</equation>（<equation>x\geqslant0,y\geqslant0</equation>）与 x轴围成的区域 D如图所示.

写出曲线<equation>( x^{2}+y^{2})^{2}=x^{2}-y^{2}</equation>的极坐标方程.将 x = rcos<equation>\theta</equation>，y = rsin<equation>\theta</equation>代入<equation>( x^{2}+y^{2})^{2}=x^{2}-y^{2}</equation>可得，<equation>r^{4}=r^{2}\cos 2\theta</equation>，即<equation>r^{2}=\cos 2\theta</equation>.于是，区域D的极坐标表示为<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \sqrt {\cos 2 \theta}, 0 \leqslant \theta \leqslant \frac {\pi}{4} \right\}.</equation>因此，<equation>\begin{aligned} \iint_ {D} x y \mathrm {d} x \mathrm {d} y \xlongequal {\text {极 坐 标}} \iint_ {D} r \cos \theta \cdot r \sin \theta \cdot r \mathrm {d} r \mathrm {d} \theta &= \int_ {0} ^ {\frac {\pi}{4}} \sin \theta \cos \theta \mathrm {d} \theta \int_ {0} ^ {\sqrt {\cos 2 \theta}} r ^ {3} \mathrm {d} r \\ &= \frac {1}{2} \int_ {0} ^ {\frac {\pi}{4}} \sin 2 \theta \cdot \frac {r ^ {4}}{4} \Bigg | _ {0} ^ {\sqrt {\cos 2 \theta}} \mathrm {d} \theta = \frac {1}{8} \int_ {0} ^ {\frac {\pi}{4}} \sin 2 \theta \cdot \cos^ {2} 2 \theta \mathrm {d} \theta \\ &= - \frac {1}{1 6} \int_ {0} ^ {\frac {\pi}{4}} \cos^ {2} 2 \theta \mathrm {d} (\cos 2 \theta) = - \frac {1}{1 6} \cdot \frac {\cos^ {3} 2 \theta}{3} \Bigg | _ {0} ^ {\frac {\pi}{4}} \\ &= - \frac {1}{1 6} \times \left(0 - \frac {1}{3}\right) = \frac {1}{4 8}. \end{aligned}</equation>

---

**2020年第19题 | 解答题 | 10分**
19. (本题满分10分)

设平面区域 D由直线 x=1，x=2，y=x与 x轴围成，计算
**答案: **##<equation>\frac{3}{4}[\sqrt{2}+\ln(\sqrt{2}+1)]。</equation>
**解析: **分析 本题主要考查二重积分的计算.

本题中的平面区域虽然由直线围成，但根据被积函数的特点（含<equation>\sqrt{x^{2}+y^{2}}</equation>），可以考虑在极坐标系下计算.

解 根据已知条件，区域 D在直角坐标系下的表示为<equation>D = \left\{(x, y) \mid 0 \leqslant y \leqslant x, 1 \leqslant x \leqslant 2 \right\}.</equation>y=x的极坐标方程为<equation>\theta=\frac{\pi}{4},</equation>x=1的极坐标方程为 rcos<equation>\theta=1,</equation>x=2的极坐标方程为 rcos<equation>\theta=2.</equation>由此可知，D的极坐标表示为<equation>D = \left\{(r, \theta) \mid \frac {1}{\cos \theta} \leqslant r \leqslant \frac {2}{\cos \theta}, 0 \leqslant \theta \leqslant \frac {\pi}{4} \right\} = \left\{(r, \theta) \mid \sec \theta \leqslant r \leqslant 2 \sec \theta , 0 \leqslant \theta \leqslant \frac {\pi}{4} \right\}.</equation>在极坐标系下计算所求二重积分.<equation>\begin{aligned} \iint_ {D} \frac {\sqrt {x ^ {2} + y ^ {2}}}{x} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \iint_ {D} \frac {r}{r \cos \theta} \cdot r \mathrm {d} r \mathrm {d} \theta &= \int_ {0} ^ {\frac {\pi}{4}} \sec \theta \mathrm {d} \theta \int_ {\sec \theta} ^ {2 \sec \theta} r \mathrm {d} r = \int_ {0} ^ {\frac {\pi}{4}} \sec \theta \cdot \frac {r ^ {2}}{2} \Bigg | _ {\sec \theta} ^ {2 \sec \theta} \mathrm {d} \theta \\ &= \int_ {0} ^ {\frac {\pi}{4}} \sec \theta \cdot \frac {3}{2} \sec^ {2} \theta \mathrm {d} \theta = \frac {3}{2} \int_ {0} ^ {\frac {\pi}{4}} \sec^ {3} \theta \mathrm {d} \theta = \frac {3}{2} \int_ {0} ^ {\frac {\pi}{4}} \sec \theta \mathrm {d} (\tan \theta) \\ &= \frac {3}{2} \left(\sec \theta \tan \theta \left| _ {0} ^ {\frac {\pi}{4}} - \int_ {0} ^ {\frac {\pi}{4}} \tan \theta \cdot \sec \theta \tan \theta \mathrm {d} \theta\right)\right) \\ &= \frac {3}{2} \left[ \sqrt {2} - \int_ {0} ^ {\frac {\pi}{4}} \sec \theta \left(\sec^ {2} \theta - 1\right) \mathrm {d} \theta \right] \\ &= \frac {3 \sqrt {2}}{2} - \frac {3}{2} \int_ {0} ^ {\frac {\pi}{4}} \sec^ {3} \theta \mathrm {d} \theta + \frac {3}{2} \int_ {0} ^ {\frac {\pi}{4}} \sec \theta \mathrm {d} \theta . \end{aligned}</equation>由上式可得，<equation>\frac {3}{2} \int_ {0} ^ {\frac {\pi}{4}} \sec^ {3} \theta \mathrm {d} \theta = \frac {3 \sqrt {2}}{2} - \frac {3}{2} \int_ {0} ^ {\frac {\pi}{4}} \sec^ {3} \theta \mathrm {d} \theta + \frac {3}{2} \int_ {0} ^ {\frac {\pi}{4}} \sec \theta \mathrm {d} \theta .</equation>由此可知，<equation>3 \int_ {0} ^ {\frac {\pi}{4}} \sec^ {3} \theta \mathrm {d} \theta = \frac {3 \sqrt {2}}{2} + \frac {3}{2} \ln | \sec \theta + \tan \theta | \Bigg | _ {0} ^ {\frac {\pi}{4}} = \frac {3 \sqrt {2}}{2} + \frac {3}{2} \ln (\sqrt {2} + 1).</equation>因此，<equation>\iint_ {D} \frac {\sqrt {x ^ {2} + y ^ {2}}}{x} \mathrm {d} x \mathrm {d} y = \frac {3}{2} \int_ {0} ^ {\frac {\pi}{4}} \sec^ {3} \theta \mathrm {d} \theta = \frac {3 \sqrt {2}}{4} + \frac {3}{4} \ln (\sqrt {2} + 1) = \frac {3}{4} \left[ \sqrt {2} + \ln (\sqrt {2} + 1) \right].</equation>

---

**2019年第18题 | 解答题 | 10分**
18. (本题满分10分）

已知平面区域<equation>D=\{(x,y)\mid |x|\leqslant y,(x^{2}+y^{2})^{3}\leqslant y^{4}\}</equation>，计算二重积分<equation>\iint_{D}\frac{x+y}{\sqrt{x^{2}+y^{2}}}\mathrm{d}x\mathrm{d}y</equation>
**答案: **##<equation>\frac{4 3 \sqrt{2}}{1 2 0}.</equation>
**解析: **分析 本题主要考查二重积分的计算.

通过观察可知，本题中的区域 D关于 y轴对称，故可以利用对称性将所求二重积分化简.根据被积函数的特点，应选择在极坐标系下计算二重积分.

解如图所示，区域D由直线<equation>y=x,y=-x</equation>，以及曲线<equation>( x^{2}+y^{2})^{3}=y^{4}</equation>围

成. 由区域 D的表达式可知，区域 D关于 y轴对称. 记<equation>D_{1}</equation>为 D位于 y轴右方的区域.

由于<equation>f ( x,y) = x</equation>为关于x的奇函数，<equation>g ( x,y) = y</equation>为关于x的偶函数，故由对称性可得，<equation>\iint_ {D} \frac {x + y}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y = \iint_ {D} \frac {y}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} \frac {y}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y.</equation>在极坐标系下计算<equation>\iint_{D_{1}} \frac{y}{\sqrt{x^{2}+y^{2}}} \mathrm{d} x \mathrm{d} y.</equation>写出区域<equation>D_{1}</equation>在极坐标系下的表示.

边界曲线 y=x的极坐标表示为<equation>\theta=\frac{\pi}{4},</equation>y轴的极坐标表示为<equation>\theta=\frac{\pi}{2},</equation><equation>( x^{2}+y^{2} )^{3}=y^{4}</equation>的极坐标表示为<equation>r^{6}=r^{4}\sin^{4}\theta</equation>即 r=<equation>\sin^{2}\theta.</equation>于是，<equation>D _ {1} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \sin^ {2} \theta , \frac {\pi}{4} \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation><equation>\begin{aligned} \iint_ {D _ {1}} \frac {y}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \iint_ {D _ {1}} \frac {r \sin \theta}{r} \cdot r \mathrm {d} r \mathrm {d} \theta &= \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \sin \theta \mathrm {d} \theta \int_ {0} ^ {\sin^ {2} \theta} r \mathrm {d} r \\ &= \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \sin \theta \cdot \frac {\sin^ {4} \theta}{2} \mathrm {d} \theta = \frac {1}{2} \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \sin^ {5} \theta \mathrm {d} \theta = - \frac {1}{2} \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \sin^ {4} \theta \mathrm {d} (\cos \theta) \\ &= - \frac {1}{2} \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \left(1 - \cos^ {2} \theta\right) ^ {2} \mathrm {d} (\cos \theta) \stackrel {\text {用} = \cos \theta} {=} \frac {1}{2} \int_ {0} ^ {\frac {\sqrt {2}}{2}} \left(1 - u ^ {2}\right) ^ {2} \mathrm {d} u \\ &= \frac {1}{2} \int_ {0} ^ {\frac {\sqrt {2}}{2}} \left(u ^ {4} - 2 u ^ {2} + 1\right) \mathrm {d} u = \frac {1}{2} \left(\frac {u ^ {5}}{5} - \frac {2 u ^ {3}}{3} + u\right) \Bigg | _ {0} ^ {\frac {\sqrt {2}}{2}} \\ &= \frac {1}{2} \times \left(\frac {\sqrt {2}}{8} \times \frac {1}{5} - \frac {\sqrt {2}}{4} \times \frac {2}{3} + \frac {\sqrt {2}}{2}\right) = \frac {4 3 \sqrt {2}}{2 4 0}. \end{aligned}</equation>因此，<equation>\text {原 积 分} = 2 \iint_ {D _ {1}} \frac {y}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y = \frac {4 3 \sqrt {2}}{1 2 0}.</equation>

---

**2019年第19题 | 解答题 | 10分**
19. (本题满分10分）

设 n为正整数，记<equation>S_{n}</equation>为曲线<equation>y=\mathrm{e}^{-x}\sin x</equation><equation>(0\leqslant x\leqslant n\pi)</equation>与 x轴所围图形的面积，求<equation>S_{n}</equation>，并求<equation>\lim_{n\to\infty}S_{n}.</equation>
**答案: **<equation>S _ {n} = \frac {1}{2} + \frac {\mathrm {e} ^ {- \pi} \left[ 1 - \mathrm {e} ^ {- (n - 1) \pi} \right]}{1 - \mathrm {e} ^ {- \pi}} + \frac {1}{2} \mathrm {e} ^ {- n \pi}, \lim _ {n \rightarrow \infty} S _ {n} = \frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}.</equation>
**解析: **解（法一）注意到<equation>\mathrm{e}^{-x}</equation>恒大于零.根据定积分的几何意义，曲线位于（<equation>k\pi</equation>，<equation>( k+1)\pi</equation>）的部分与 x轴之间的图形面积等于<equation>\int_{k\pi}^{(k+1)\pi} \mathrm{e}^{-x}|\sin x|\mathrm{d}x.</equation>计算<equation>S_{n}。</equation><equation>\begin{aligned} S _ {n} &= \sum_ {k = 0} ^ {n - 1} \int_ {k \pi} ^ {(k + 1) \pi} \mathrm {e} ^ {- x} | \sin x | \mathrm {d} x \underline {{= t = x - k \pi}} \sum_ {k = 0} ^ {n - 1} \int_ {0} ^ {\pi} \mathrm {e} ^ {- (t + k \pi)} | \sin (t + k \pi) | \mathrm {d} t \\ &= \sum_ {k = 0} ^ {n - 1} \mathrm {e} ^ {- k \pi} \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t. \end{aligned}</equation>下面计算<equation>\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t &= - \int_ {0} ^ {\pi} \sin t \mathrm {d} \left(\mathrm {e} ^ {- t}\right) = - \left(\sin t \mathrm {e} ^ {- t} \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \cos t \mathrm {d} t\right) \\ &= \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \cos t \mathrm {d} t = - \int_ {0} ^ {\pi} \cos t \mathrm {d} \left(\mathrm {e} ^ {- t}\right) \\ &= - \cos t \mathrm {e} ^ {- t} \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t \\ &= \mathrm {e} ^ {- \pi} + 1 - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t. \end{aligned}</equation>由上式可得<equation>2\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t=\mathrm{e}^{-\pi}+1</equation>，于是<equation>\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t=\frac{1}{2}\left(\mathrm{e}^{-\pi}+1\right).</equation>因此，<equation>S _ {n} = \frac {1}{2} \left(\mathrm {e} ^ {- \pi} + 1\right) \sum_ {k = 0} ^ {n - 1} \mathrm {e} ^ {- k \pi} = \frac {1}{2} \left(\mathrm {e} ^ {- \pi} + 1\right) \frac {1 - \mathrm {e} ^ {- n \pi}}{1 - \mathrm {e} ^ {- \pi}}.</equation><equation>\lim _ {n \rightarrow \infty} S _ {n} = \frac {1}{2} \left(\mathrm {e} ^ {- \pi} + 1\right) \lim _ {n \rightarrow \infty} \frac {1 - \mathrm {e} ^ {- n \pi}}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} \cdot \frac {\mathrm {e} ^ {- \pi} + 1}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}.</equation>（法二）计算<equation>S_{n}</equation><equation>S _ {n} = \sum_ {k = 0} ^ {n - 1} \int_ {k \pi} ^ {(k + 1) \pi} \mathrm {e} ^ {- x} | \sin x | \mathrm {d} x.</equation>下面计算<equation>\int\mathrm{e}^{-x}\sin x\mathrm{d}x.</equation><equation>\begin{aligned} \int \mathrm {e} ^ {- x} \sin x \mathrm {d} x &= - \int \sin x \mathrm {d} \left(\mathrm {e} ^ {- x}\right) = - \left(\sin x \mathrm {e} ^ {- x} - \int \mathrm {e} ^ {- x} \cos x \mathrm {d} x\right) \\ &= - \sin x \mathrm {e} ^ {- x} + \int \mathrm {e} ^ {- x} \cos x \mathrm {d} x = - \sin x \mathrm {e} ^ {- x} - \int \cos x \mathrm {d} \left(\mathrm {e} ^ {- x}\right) \\ &= - \sin x \mathrm {e} ^ {- x} - \left(\cos x \mathrm {e} ^ {- x} + \int \mathrm {e} ^ {- x} \sin x \mathrm {d} x\right). \end{aligned}</equation>由上式可得<equation>2 \int\mathrm{e}^{-x}\sin x\mathrm{d}x=-\mathrm{e}^{-x}(\sin x+\cos x)-C</equation>，于是<equation>\int \mathrm {e} ^ {- x} \sin x \mathrm {d} x = - \frac {1}{2} \left[ \mathrm {e} ^ {- x} (\sin x + \cos x) + C \right],</equation>其中 C为任意常数.

由于当<equation>x \in(k\pi,(k+1)\pi)</equation>（k为偶数）时，<equation>\sin x > 0</equation><equation>|\sin x |=\sin x</equation>；当<equation>x \in(k\pi,(k+1)\pi)</equation>（k为奇数）时，<equation>\sin x < 0</equation><equation>|\sin x |=-\sin x</equation>，故<equation>\begin{aligned} \int_ {k \pi} ^ {(k + 1) \pi} \mathrm {e} ^ {- x} | \sin x | \mathrm {d} x &= (- 1) ^ {k} \cdot - \frac {1}{2} \left[ \mathrm {e} ^ {- x} (\sin x + \cos x) \right] \Bigg | _ {k \pi} ^ {(k + 1) \pi} \\ \underline {{\cos k \pi = (- 1) ^ {k}}} (- 1) ^ {k} \cdot - \frac {1}{2} \left[ \mathrm {e} ^ {- (k + 1) \pi} \cdot (- 1) ^ {k + 1} - \mathrm {e} ^ {- k \pi} \cdot (- 1) ^ {k} \right] \\ &= \frac {1}{2} \left[ \mathrm {e} ^ {- k \pi} + \mathrm {e} ^ {- (k + 1) \pi} \right]. \end{aligned}</equation>因此，<equation>\begin{array}{l} S _ {n} = \sum_ {k = 0} ^ {n - 1} \left\{\frac {1}{2} \left[ \mathrm {e} ^ {- k \pi} + \mathrm {e} ^ {- (k + 1) \pi} \right] \right\} = \frac {1}{2} + \sum_ {k = 1} ^ {n - 1} \mathrm {e} ^ {- k \pi} + \frac {1}{2} \mathrm {e} ^ {- n \pi} \\ = \frac {1}{2} + \frac {\mathrm {e} ^ {- \pi} \left[ 1 - \mathrm {e} ^ {- (n - 1) \pi} \right]}{1 - \mathrm {e} ^ {- \pi}} + \frac {1}{2} \mathrm {e} ^ {- n \pi}. \\ \end{array}</equation><equation>\begin{aligned} \lim _ {n \rightarrow \infty} S _ {n} &= \lim _ {n \rightarrow \infty} \left[ \frac {1}{2} + \frac {\mathrm {e} ^ {- \pi} \left[ 1 - \mathrm {e} ^ {- (n - 1) \pi} \right]}{1 - \mathrm {e} ^ {- \pi}} + \frac {1}{2} \mathrm {e} ^ {- n \pi} \right] \\ &= \frac {1}{2} + \frac {\mathrm {e} ^ {- \pi}}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}. \end{aligned}</equation>

---

**2018年第17题 | 解答题 | 10分**
17. (本题满分10分)

设平面区域 D由曲线<equation>\left\{ \begin{array}{l} x = t - \sin t, \\ y = 1 - \cos t \end{array} \right.</equation>
**答案: **<equation>3 \pi^{2}+5 \pi.</equation>
**解析: **解区域 D如图所示.把区域 D看作 X型区域， t=0对应的点为（0,0）， t=<equation>\pi</equation>对应的点为（<equation>\pi,2</equation>）， t=2<equation>\pi</equation>对应的点为（2<equation>\pi,0</equation>），则<equation>D = \{(x, y) \mid 0 \leqslant y \leqslant y (x), 0 \leqslant x \leqslant 2 \pi \}</equation>分别计算<equation>\iint_{D}2y\mathrm{d}x\mathrm{d}y</equation>和<equation>\iint_{D}x\mathrm{d}x\mathrm{d}y.</equation><equation>\begin{aligned} \iint_ {D} 2 y \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {2 \pi} \mathrm {d} x \int_ {0} ^ {y (x)} 2 y \mathrm {d} y = \int_ {0} ^ {2 \pi} y ^ {2} (x) \mathrm {d} x = \int_ {0} ^ {2 \pi} y ^ {2} [ x (t) ] \cdot x ^ {\prime} (t) \mathrm {d} t \\ &= \int_ {0} ^ {2 \pi} (1 - \cos t) ^ {2} \cdot (1 - \cos t) \mathrm {d} t = \int_ {0} ^ {2 \pi} (1 - \cos t) ^ {3} \mathrm {d} t \\ &= 8 \int_ {0} ^ {2 \pi} \sin^ {6} \frac {t}{2} \mathrm {d} t \xlongequal {u = \frac {t}{2}} 1 6 \int_ {0} ^ {\pi} \sin^ {6} u \mathrm {d} u = 3 2 \int_ {0} ^ {\frac {\pi}{2}} \sin^ {6} u \mathrm {d} u \\ &= 3 2 \times \frac {\pi}{2} \times \frac {5}{6} \times \frac {3}{4} \times \frac {1}{2} = 5 \pi . \end{aligned}</equation>下面用三种方法计算<equation>\iint_{D} x \mathrm{d} x \mathrm{d} y.</equation><equation>\begin{aligned} \iint_ {D} x \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {2 \pi} x \mathrm {d} x \int_ {0} ^ {y (x)} \mathrm {d} y = \int_ {0} ^ {2 \pi} x y (x) \mathrm {d} x = \int_ {0} ^ {2 \pi} x (t) y [ x (t) ] \cdot x ^ {\prime} (t) \mathrm {d} t \\ &= \int_ {0} ^ {2 \pi} (t - \sin t) (1 - \cos t) ^ {2} \mathrm {d} t \stackrel {s = t - \pi} {=} \int_ {- \pi} ^ {\pi} (s + \pi + \sin s) (1 + \cos s) ^ {2} \mathrm {d} s. \end{aligned}</equation>由于<equation>( s+\sin s ) ( 1+\cos s )^{2}</equation>是关于s的奇函数，故<equation>\int_{-\pi}^{\pi} ( s+\sin s ) ( 1+\cos s )^{2}\mathrm{d}s=0.</equation><equation>\begin{aligned} \int_ {- \pi} ^ {\pi} (s + \pi + \sin s) (1 + \cos s) ^ {2} d s &= \int_ {- \pi} ^ {\pi} \pi (1 + \cos s) ^ {2} d s \xlongequal {\mathrm {对称性}} 2 \int_ {0} ^ {\pi} \pi (1 + \cos s) ^ {2} d s \\ &= 8 \pi \int_ {0} ^ {\pi} \cos^ {4} \frac {s}{2} \mathrm {d} s \xlongequal {u = \frac {s}{2}} 1 6 \pi \int_ {0} ^ {\frac {\pi}{2}} \cos^ {4} u \mathrm {d} u \\ &= 1 6 \pi \times \frac {\pi}{2} \times \frac {3}{4} \times \frac {1}{2} = 3 \pi^ {2}. \end{aligned}</equation>（法二）由法一知，<equation>\iint_{D}x\mathrm{d}x\mathrm{d}y=\int_{0}^{2\pi} \left(t-\sin t\right)\left(1-\cos t\right)^{2}\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {0} ^ {2 \pi} (t - \sin t) (1 - \cos t) ^ {2} \mathrm {d} t &= \int_ {0} ^ {2 \pi} t (1 - \cos t) ^ {2} \mathrm {d} t - \int_ {0} ^ {2 \pi} \sin t (1 - \cos t) ^ {2} \mathrm {d} t \\ &= \int_ {0} ^ {2 \pi} \left(t - 2 t \cos t + t \cos^ {2} t\right) \mathrm {d} t - \int_ {0} ^ {2 \pi} \left(1 - \cos t\right) ^ {2} \mathrm {d} \left(1 - \cos t\right) \\ &= \int_ {0} ^ {2 \pi} \left(t - 2 t \cos t + t \cdot \frac {1 + \cos 2 t}{2}\right) \mathrm {d} t - \frac {\left(1 - \cos t\right) ^ {3}}{3} \Bigg | _ {0} ^ {2 \pi} \\ &= \int_ {0} ^ {2 \pi} \frac {3}{2} t \mathrm {d} t - 2 \int_ {0} ^ {2 \pi} t \cos t \mathrm {d} t + \frac {1}{2} \int_ {0} ^ {2 \pi} t \cos 2 t \mathrm {d} t - 0 \\ \stackrel {*} {=} 3 \pi^ {2} - 0 - 0 &= 3 \pi^ {2}. \end{aligned}</equation>“<equation>\stackrel{*}{=}</equation>”处用到了<equation>\int_{0}^{2\pi} t\cos t\mathrm{d}t=0, \int_{0}^{2\pi} t\cos 2t\mathrm{d}t=0.</equation><equation>\int_ {0} ^ {2 \pi} t \cos t \mathrm {d} t \xlongequal {\mathrm {分 部 积 分}} \int_ {0} ^ {2 \pi} t \mathrm {d} (\sin t) = t \sin t \Big | _ {0} ^ {2 \pi} - \int_ {0} ^ {2 \pi} \sin t \mathrm {d} t = 0,</equation><equation>\int_ {0} ^ {2 \pi} t \cos 2 t \mathrm {d} t \xlongequal {\text {分 部 积 分}} \frac {1}{2} \int_ {0} ^ {2 \pi} t \mathrm {d} (\sin 2 t) = \frac {1}{2} \left(t \sin 2 t \Big | _ {0} ^ {2 \pi} - \int_ {0} ^ {2 \pi} \sin 2 t \mathrm {d} t\right) = 0.</equation>（法三）注意到区域 D关于直线<equation>x=\pi</equation>对称，故区域 D的形心位于该直线上，从而其形心的横坐标<equation>\overline{x}=\pi.</equation>根据形心公式，<equation>\overline{x}=\frac{\iint\limits_{D}x\mathrm{d}x\mathrm{d}y}{\iint\limits_{D}\mathrm{d}x\mathrm{d}y}</equation>.于是，<equation>\begin{aligned} \iint_ {D} x \mathrm {d} x \mathrm {d} y &= \pi \iint_ {D} \mathrm {d} x \mathrm {d} y = \pi \int_ {0} ^ {2 \pi} \mathrm {d} x \int_ {0} ^ {y (x)} \mathrm {d} y = \pi \int_ {0} ^ {2 \pi} y (x) \mathrm {d} x = \pi \int_ {0} ^ {2 \pi} y [ x (t) ] \cdot x ^ {\prime} (t) \mathrm {d} t \\ &= \pi \int_ {0} ^ {2 \pi} (1 - \cos t) \cdot (1 - \cos t) \mathrm {d} t = \pi \int_ {0} ^ {2 \pi} (1 - \cos t) ^ {2} \mathrm {d} t = 4 \pi \int_ {0} ^ {2 \pi} \sin^ {4} \frac {t}{2} \mathrm {d} t \\ \underline {{\frac {u = \frac {t}{2}}{2}}} 8 \pi \int_ {0} ^ {\pi} \sin^ {4} u \mathrm {d} u &= 1 6 \pi \int_ {0} ^ {\frac {\pi}{2}} \sin^ {4} u \mathrm {d} u = 1 6 \pi \times \frac {\pi}{2} \times \frac {3}{4} \times \frac {1}{2} = 3 \pi^ {2}. \end{aligned}</equation>因此，<equation>\iint_{D} ( x+2 y ) \mathrm{d} x \mathrm{d} y=3 \pi^{2}+5 \pi.</equation>

---

**2017年第20题 | 解答题 | 11分**
20. (本题满分11分）

已知平面区域<equation>D=\{(x,y)\mid x^{2}+y^{2}\leqslant 2y\}</equation>，计算二重积分<equation>\iint_{D}(x+1)^{2}\mathrm{d}x\mathrm{d}y.</equation>
**答案: **<equation>\frac{5\pi}{4}.</equation>
**解析: **解如图所示，积分区域 D是圆心在点（0，1），半径为1的圆盘，关于 y轴对称，面积为<equation>\pi</equation>.令<equation>D^{\prime}</equation>为 D位于右半平面的部分.

展开被积函数<equation>( x+1 )^{2}</equation>，得<equation>( x+1 )^{2}=x^{2}+2 x+1.</equation>由于<equation>x^{2}</equation>是关于x的偶函数，2x是关于x的奇函数，故<equation>\iint_{D} x^{2}\mathrm{d}x\mathrm{d}y=2\iint_{D^{\prime}} x^{2}\mathrm{d}x\mathrm{d}y, \iint_{D} 2 x\mathrm{d}x\mathrm{d}y=0.</equation>于是，<equation>\iint_{D} ( x+1 )^{2}\mathrm{d}x\mathrm{d}y=2\iint_{D^{\prime}} x^{2}\mathrm{d}x\mathrm{d}y+0+\iint_{D}\mathrm{d}x\mathrm{d}y=2\iint_{D^{\prime}} x^{2}\mathrm{d}x\mathrm{d}y+\pi.</equation>在极坐标系下计算<equation>\iint_{D^{\prime}} x^{2}\mathrm{d}x\mathrm{d}y.D^{\prime} = \left\{(r,\theta)\mid 0\leqslant r\leqslant 2\sin \theta ,0\leqslant \theta \leqslant \frac{\pi}{2}\right\}.</equation><equation>\begin{aligned} \iint_ {D ^ {\prime}} x ^ {2} \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {2 \sin \theta} r ^ {2} \cos^ {2} \theta \cdot r \mathrm {d} r = \int_ {0} ^ {\frac {\pi}{2}} \cos^ {2} \theta \mathrm {d} \theta \int_ {0} ^ {2 \sin \theta} r ^ {3} \mathrm {d} r = \int_ {0} ^ {\frac {\pi}{2}} 4 \sin^ {4} \theta \cos^ {2} \theta \mathrm {d} \theta \\ &= 4 \int_ {0} ^ {\frac {\pi}{2}} \left(\sin^ {4} \theta - \sin^ {6} \theta\right) \mathrm {d} \theta = 4 \times \frac {\pi}{2} \times \left(\frac {3}{4} \times \frac {1}{2} - \frac {5}{6} \times \frac {3}{4} \times \frac {1}{2}\right) = \frac {\pi}{8}. \end{aligned}</equation>因此，<equation>\iint_ {D} (x + 1) ^ {2} \mathrm {d} x \mathrm {d} y = 2 \times \frac {\pi}{8} + \pi = \frac {5 \pi}{4}.</equation>

---

**2016年第18题 | 解答题 | 10分**
18. (本题满分10分）

设 D是由直线 y=1，y=x，y=-x围成的有界区域，计算二重积分<equation>\iint_{D} \frac{x^{2}-xy-y^{2}}{x^{2}+y^{2}} \mathrm{d} x \mathrm{d} y.</equation>
**答案: **# 1-<equation>\frac{\pi}{2}.</equation>
**解析: **解 由于积分区域 D关于 y轴对称，而<equation>\frac{xy}{x^{2}+y^{2}}</equation>是关于 x的奇函数，故<equation>\iint_{D}\frac{xy}{x^{2}+y^{2}}\mathrm{d}x\mathrm{d}y=0.</equation>记原积分为 I，则<equation>I=\iint_{D}\frac{x^{2}-y^{2}}{x^{2}+y^{2}}\mathrm{d}x\mathrm{d}y.</equation>下面我们用两种方法来计算 I.

（法一）在直角坐标系下计算 I.<equation>I = \iint_ {D} \frac {x ^ {2} - y ^ {2}}{x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y = \iint_ {D} \left(1 - \frac {2 y ^ {2}}{x ^ {2} + y ^ {2}}\right) \mathrm {d} x \mathrm {d} y.</equation>如图所示，区域 D为由直线 y=1，y=x，y=-x围成的三角形 AOB. 求得点 A和点 B的坐标，分别为（1，1）和（-1，1）. D的面积等于<equation>S_{\triangle AOB}=\frac{1}{2}\times 2\times 1=1.</equation>从而，<equation>I = 1 - \iint_ {D} \frac {2 y ^ {2}}{x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y \stackrel {\text {对 称 性}} {=} 1 - 4 \iint_ {D _ {1}} \frac {y ^ {2}}{x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y,</equation>其中<equation>D_{1}</equation>是区域D位于第一象限内的部分.把<equation>D_{1}</equation>看作Y型区域，<equation>D_{1}=\{(x,y)\mid 0\leq x\leq y,0\leq y\leq 1\}.</equation><equation>\begin{aligned} \iint_ {D _ {1}} \frac {y ^ {2}}{x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {1} y ^ {2} \mathrm {d} y \int_ {0} ^ {y} \frac {1}{x ^ {2} + y ^ {2}} \mathrm {d} x \xlongequal {u = \frac {x}{y}} \int_ {0} ^ {1} y ^ {2} \cdot \frac {1}{y} \mathrm {d} y \int_ {0} ^ {1} \frac {1}{u ^ {2} + 1} \mathrm {d} u \\ &= \frac {1}{2} \cdot \arctan u \Bigg | _ {0} ^ {1} = \frac {1}{2} \times \frac {\pi}{4} = \frac {\pi}{8}. \end{aligned}</equation>因此，<equation>I = 1 - 4\times \frac{\pi}{8} = 1 - \frac{\pi}{2}.</equation>（法二）在极坐标系下计算 I.

在极坐标系下，<equation>x=r\cos \theta, y=r\sin \theta</equation>，直线<equation>y=1</equation>对应<equation>r=\frac{1}{\sin \theta}</equation>.区域D的极坐标表示为<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \frac {1}{\sin \theta}, \frac {\pi}{4} \leqslant \theta \leqslant \frac {3 \pi}{4} \right\}.</equation>因此，<equation>\begin{aligned} \iint_ {D} \frac {x ^ {2} - y ^ {2}}{x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y &= \int_ {\frac {\pi}{4}} ^ {\frac {3}{4} \pi} \mathrm {d} \theta \int_ {0} ^ {\frac {1}{\sin \theta}} \frac {r ^ {2} \cos^ {2} \theta - r ^ {2} \sin^ {2} \theta}{r ^ {2}} \cdot r \mathrm {d} r = \int_ {\frac {\pi}{4}} ^ {\frac {3}{4} \pi} \left(1 - 2 \sin^ {2} \theta\right) \mathrm {d} \theta \int_ {0} ^ {\frac {1}{\sin \theta}} r \mathrm {d} r \\ &= \int_ {\frac {\pi}{4}} ^ {\frac {3}{4} \pi} \frac {1 - 2 \sin^ {2} \theta}{2 \sin^ {2} \theta} \mathrm {d} \theta = \int_ {\frac {\pi}{4}} ^ {\frac {3}{4} \pi} \frac {1}{2 \sin^ {2} \theta} \mathrm {d} \theta - \frac {\pi}{2} = - \frac {1}{2} \cot \theta \left| _ {\frac {\pi}{4}} ^ {\frac {3}{4} \pi} - \frac {\pi}{2} = 1 - \frac {\pi}{2}. \right. \end{aligned}</equation>

---

**2015年第18题 | 解答题 | 10分**
18. (本题满分10分)

计算二重积分<equation>\iint_ {D} x (x + y) \mathrm {d} x \mathrm {d} y, \text {其 中} D = \{(x, y) \mid x ^ {2} + y ^ {2} \leqslant 2, y \geqslant x ^ {2} \}.</equation>
**答案: **## (18)<equation>\frac{\pi}{4}-\frac{2}{5}.</equation>
**解析: **解 由图（a）可知，区域 D关于 y轴对称，而 xy为关于 x的奇函数，故<equation>\iint_{D} xy\mathrm{d}x\mathrm{d}y=0</equation>.又因为<equation>x^{2}</equation>为关于 x的偶函数，所以<equation>\iint_ {D} x (x + y) \mathrm {d} x \mathrm {d} y = \iint_ {D} x ^ {2} \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} x ^ {2} \mathrm {d} x \mathrm {d} y,</equation>其中<equation>D_{1}</equation>是D位于右半平面的部分.我们可以用两种方法来计算<equation>\iint\limits_{\Omega}x^{2}\mathrm{d}x\mathrm{d}y.</equation>(a)

（法一）在直角坐标系下计算.

(b)

(c)

如图（b）所示，先求出圆弧<equation>x^{2}+y^{2}=2</equation>与抛物线<equation>y=x^{2}</equation>的交点.由<equation>\left\{\begin{array}{l l}x^{2}+y^{2}=2\\ y=x^{2},\end{array}\right.</equation>可求得<equation>(x,y)=(1,1)</equation>或<equation>(x,y)=(-1,1).</equation>在第一象限中的交点为<equation>(x,y)=(1,1).</equation>由圆方程<equation>x^{2}+y^{2}=2</equation>可得，<equation>y=\sqrt{2-x^{2}}</equation>.由于圆弧在第一象限，故根号前取+号.将区域<equation>D_{1}</equation>写成X型区域，<equation>D _ {1} = \left\{(x, y) \mid x ^ {2} \leqslant y \leqslant \sqrt {2 - x ^ {2}}, 0 \leqslant x \leqslant 1 \right\}.</equation>从而<equation>\begin{aligned} \iint_ {D _ {1}} x ^ {2} \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {1} \mathrm {d} x \int_ {x ^ {2}} ^ {\sqrt {2 - x ^ {2}}} x ^ {2} \mathrm {d} y = \int_ {0} ^ {1} x ^ {2} \left(\sqrt {2 - x ^ {2}} - x ^ {2}\right) \mathrm {d} x \\ &= \int_ {0} ^ {1} x ^ {2} \sqrt {2 - x ^ {2}} \mathrm {d} x - \int_ {0} ^ {1} x ^ {4} \mathrm {d} x = \int_ {0} ^ {1} x ^ {2} \sqrt {2 - x ^ {2}} \mathrm {d} x - \frac {1}{5} \\ \underline {{x = \sqrt {2} \sin t}} \int_ {0} ^ {\frac {\pi}{4}} 4 \sin^ {2} t \cos^ {2} t \mathrm {d} t - \frac {1}{5} &= \int_ {0} ^ {\frac {\pi}{4}} (\sin 2 t) ^ {2} \mathrm {d} t - \frac {1}{5} \\ &= \int_ {0} ^ {\frac {\pi}{4}} \frac {1 - \cos 4 t}{2} \mathrm {d} t - \frac {1}{5} = \frac {\pi}{8} - \frac {1}{5}. \end{aligned}</equation>因此，<equation>\iint_ {D} x (x + y) \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} x ^ {2} \mathrm {d} x \mathrm {d} y = \frac {\pi}{4} - \frac {2}{5}.</equation>（法二）在极坐标系下计算.

写出<equation>x^{2}+y^{2}=2</equation>的极坐标形式：<equation>r=\sqrt{2}</equation>写出<equation>y=x^{2}</equation>的极坐标形式：<equation>r\sin \theta=r^{2}\cos^{2}\theta</equation>化简为<equation>r=\tan \theta\sec \theta.</equation>可求得圆弧与抛物线的交点坐标为<equation>\left(\sqrt{2},\frac{\pi}{4}\right).</equation>如图（c）所示，连接极点与该交点，将区域<equation>D_{1}</equation>分成两部分，<equation>D_{1}=D_{1}^{\prime}\cup D_{1}^{\prime\prime}.</equation><equation>D_{1}^{\prime}</equation>由<equation>\theta=\frac{\pi}{4},</equation><equation>\theta=\frac{\pi}{2}</equation>以及圆弧r=<equation>\sqrt{2}</equation>围成；<equation>D_{1}^{\prime\prime}</equation>由<equation>\theta=\frac{\pi}{4},</equation><equation>r=\tan \theta\sec \theta</equation>围成，从而<equation>D _ {1} ^ {\prime} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \sqrt {2}, \frac {\pi}{4} \leqslant \theta \leqslant \frac {\pi}{2} \right\}, \quad D _ {1} ^ {\prime \prime} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \tan \theta \sec \theta , 0 \leqslant \theta \leqslant \frac {\pi}{4} \right\}</equation><equation>\begin{aligned} \iint_ {D _ {1}} x ^ {2} \mathrm {d} x \mathrm {d} y &= \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {\sqrt {2}} r ^ {3} \cos^ {2} \theta \mathrm {d} r + \int_ {0} ^ {\frac {\pi}{4}} \mathrm {d} \theta \int_ {0} ^ {\tan \theta \sec \theta} r ^ {3} \cos^ {2} \theta \mathrm {d} r \\ &= \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \frac {1 + \cos 2 \theta}{2} \mathrm {d} \theta + \int_ {0} ^ {\frac {\pi}{4}} \cos^ {2} \theta \cdot \frac {\tan^ {4} \theta \sec^ {4} \theta}{4} \mathrm {d} \theta \\ &= \frac {\pi}{8} - \frac {1}{4} + \frac {1}{4} \int_ {0} ^ {\frac {\pi}{4}} \tan^ {4} \theta \sec^ {2} \theta \mathrm {d} \theta \frac {u = \tan \theta}{\pi} - \frac {1}{4} + \frac {1}{4} \int_ {0} ^ {1} u ^ {4} \mathrm {d} u \\ &= \frac {\pi}{8} - \frac {1}{5}. \end{aligned}</equation>因此，<equation>\iint_ {D} x (x + y) \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} x ^ {2} \mathrm {d} x \mathrm {d} y = \frac {\pi}{4} - \frac {2}{5}.</equation>

---

**2014年第17题 | 解答题 | 10分**
17. (本题满分10分)

设平面区域 D = {（x,y）| 1≤x²+y²≤4,x≥0,y≥0}.计算<equation>\iint_{D} \frac{x\sin(\pi\sqrt{x^{2}+y^{2}})}{x+y}\mathrm{d}x\mathrm{d}y.</equation>
**答案: **<equation>(1 7) - \frac {3}{4}.</equation>
**解析: **解记<equation>\iint_{D}\frac{x\sin(\pi \sqrt{x^{2}+y^{2}})}{x+y}\mathrm{d}x\mathrm{d}y=I.</equation>积分区域如图所示.

（法一）首先，由于积分区域 D关于<equation>y=x</equation>对称，故对 x，y具有轮换对称性，从而<equation>I = \iint_ {D} \frac {x \sin \left(\pi \sqrt {x ^ {2} + y ^ {2}}\right)}{x + y} \mathrm {d} x \mathrm {d} y = \iint_ {D} \frac {y \sin \left(\pi \sqrt {x ^ {2} + y ^ {2}}\right)}{x + y} \mathrm {d} x \mathrm {d} y.</equation>因此，<equation>I = \frac {1}{2} \iint_ {D} \left[ \frac {x \sin \left(\pi \sqrt {x ^ {2} + y ^ {2}}\right)}{x + y} + \frac {y \sin \left(\pi \sqrt {x ^ {2} + y ^ {2}}\right)}{x + y} \right] \mathrm {d} x \mathrm {d} y = \frac {1}{2} \iint_ {D} \sin \left(\pi \sqrt {x ^ {2} + y ^ {2}}\right) \mathrm {d} x \mathrm {d} y.</equation>在极坐标系下，<equation>D=\left\{(r,\theta)\mid 1\leqslant r\leqslant 2,0\leqslant \theta \leqslant \frac{\pi}{2}\right\} .</equation><equation>I = \frac {1}{2} \int_ {0} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {1} ^ {2} \sin (\pi r) \cdot r \mathrm {d} r = \frac {\pi}{4} \int_ {1} ^ {2} r \sin (\pi r) \mathrm {d} r,</equation>其中，<equation>\int_ {1} ^ {2} r \sin (\pi r) \mathrm {d} r = - \frac {1}{\pi} \int_ {1} ^ {2} r \mathrm {d} [ \cos (\pi r) ] = - \frac {1}{\pi} \left[ r \cos (\pi r) \left| _ {1} ^ {2} - \int_ {1} ^ {2} \cos (\pi r) \mathrm {d} r \right. \right] = - \frac {3}{\pi}.</equation>因此，<equation>I = \frac{\pi}{4}\times \left(-\frac{3}{\pi}\right) = -\frac{3}{4}.</equation>（法二）在不使用轮换对称性对<equation>I</equation>进行化简的情况下计算<equation>I</equation>.

在极坐标系下，<equation>D = \left\{(r,\theta)\mid 1\leqslant r\leqslant 2,0\leqslant \theta \leqslant \frac{\pi}{2}\right\}.</equation><equation>I = \int_ {0} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {1} ^ {2} \frac {r \cos \theta \sin (\pi r)}{r (\cos \theta + \sin \theta)} \cdot r \mathrm {d} r = \int_ {0} ^ {\frac {\pi}{2}} \frac {\cos \theta}{\cos \theta + \sin \theta} \mathrm {d} \theta \int_ {1} ^ {2} r \sin (\pi r) \mathrm {d} r.</equation>由于<equation>\int_ {0} ^ {\frac {\pi}{2}} \frac {\cos \theta}{\cos \theta + \sin \theta} \mathrm {d} \theta \xlongequal {\text {等 式}} \frac {t = \frac {\pi}{2} - \theta}{\int_ {\frac {\pi}{2}} ^ {0} \frac {\sin t}{\cos t + \sin t} \mathrm {d} t} = \int_ {0} ^ {\frac {\pi}{2}} \frac {\sin \theta}{\cos \theta + \sin \theta} \mathrm {d} \theta ,</equation>故<equation>\int_ {0} ^ {\frac {\pi}{2}} \frac {\cos \theta}{\cos \theta + \sin \theta} \mathrm {d} \theta = \frac {1}{2} \int_ {0} ^ {\frac {\pi}{2}} \left(\frac {\cos \theta}{\cos \theta + \sin \theta} + \frac {\sin \theta}{\cos \theta + \sin \theta}\right) \mathrm {d} \theta = \frac {1}{2} \int_ {0} ^ {\frac {\pi}{2}} 1 \mathrm {d} \theta = \frac {\pi}{4}.</equation>因此，<equation>I = \frac{\pi}{4}\times \left(-\frac{3}{\pi}\right) = -\frac{3}{4}.</equation>

---

**2013年第17题 | 解答题 | 10分**
17. (本题满分10分)

设平面区域 D由直线 x=3y，y=3x及 x+y=8围成，计算<equation>\iint\limits_{D}x^{2}\mathrm{d}x\mathrm{d}y.</equation>
**答案: **## (17)<equation>\frac{4 1 6}{3}.</equation>
**解析: **解 （法一）在直角坐标系下计算.

如图，可以分别求出 y=3x与 x+y=8的交点，以及 x=3y与 x+y=8的交点.<equation>\left\{ \begin{array}{l l} y = 3 x, \\ x + y = 8, \end{array} \Rightarrow \left\{ \begin{array}{l l} x = 2, \\ y = 6, \end{array} \right. \quad \left\{ \begin{array}{l l} x = 3 y, \\ x + y = 8, \end{array} \Rightarrow \left\{ \begin{array}{l l} x = 6, \\ y = 2. \end{array} \right. \right.</equation>于是直线<equation>x = 2</equation>将区域<equation>D</equation>分为两部分<equation>D_{1}, D_{2}</equation>.<equation>D _ {1} = \left\{(x, y) \mid \frac {x}{3} \leqslant y \leqslant 3 x, 0 \leqslant x \leqslant 2 \right\}, \quad D _ {2} = \left\{(x, y) \mid \frac {x}{3} \leqslant y \leqslant 8 - x, 2 \leqslant x \leqslant 6 \right\}.</equation><equation>\begin{aligned} \iint_ {D} x ^ {2} \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {2} x ^ {2} \mathrm {d} x \int_ {\frac {x}{3}} ^ {3 x} \mathrm {d} y + \int_ {2} ^ {6} x ^ {2} \mathrm {d} x \int_ {\frac {x}{3}} ^ {8 - x} \mathrm {d} y = \int_ {0} ^ {2} x ^ {2} \cdot \frac {8}{3} x \mathrm {d} x + \int_ {2} ^ {6} \left(8 - \frac {4}{3} x\right) x ^ {2} \mathrm {d} x \\ &= \frac {2}{3} x ^ {4} \left| _ {0} ^ {2} + \frac {8}{3} x ^ {3} \right| _ {2} ^ {6} - \frac {1}{3} x ^ {4} \left| _ {2} ^ {6} = \frac {4 1 6}{3}. \right. \end{aligned}</equation>（法二）在极坐标系下计算.

三条直线的方程分别为<equation>\theta=\arctan \frac{1}{3},</equation><equation>\theta=\arctan 3</equation>，以及<equation>r(\cos \theta+\sin \theta)=8.</equation>此时，区域D在极坐标系下的表示为<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \frac {8}{\cos \theta + \sin \theta}, \arctan \frac {1}{3} \leqslant \theta \leqslant \arctan 3 \right\}.</equation><equation>\begin{aligned} \iint_ {D} x ^ {2} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \iint_ {D} r ^ {2} \cos^ {2} \theta \cdot r \mathrm {d} r \mathrm {d} \theta &= \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} \cos^ {2} \theta \mathrm {d} \theta \int_ {0} ^ {\frac {8}{\cos \theta + \sin \theta}} r ^ {3} \mathrm {d} r \\ &= \frac {8 ^ {4}}{4} \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} \frac {\cos^ {2} \theta}{\left(\cos \theta + \sin \theta\right) ^ {4}} \mathrm {d} \theta = \frac {8 ^ {4}}{4} \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} \frac {1}{\left(1 + \tan \theta\right) ^ {4}} \cdot \sec^ {2} \theta \mathrm {d} \theta \\ \underline {{=}} \frac {u = \tan \theta}{4} \frac {8 ^ {4}}{4} \int_ {\frac {1}{3}} ^ {3} \frac {1}{(1 + u) ^ {4}} \mathrm {d} u &= \frac {8 ^ {4}}{4} \cdot \left(- \frac {1}{3}\right) \frac {1}{(1 + u) ^ {3}} \Big | _ {\frac {1}{3}} ^ {3} = \frac {4 1 6}{3}. \end{aligned}</equation>

---

**2012年第6题 | 选择题 | 4分 | 答案: D**
6. 设区域 D由曲线<equation>y=\sin x,x=\pm \frac{\pi}{2},y=1</equation>围成，则<equation>\iint_{D}(xy^{5}-1)\mathrm{d}x\mathrm{d}y=</equation>(    )

A.<equation>\pi</equation>B.2 C.-2 D.<equation>-\pi</equation>
答案: D
**解析: **解区域D如图（a）所示。如图（b）所示，将D分为两部分，<equation>D=D_{1}\cup D_{2}.</equation><equation>D_{1}</equation>由<equation>y=1</equation><equation>y=\left| \sin x\right|</equation>在<equation>\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>上的一段围成.<equation>D_{2}</equation>由<equation>x=-\frac{\pi}{2},y=-\sin x,y=\sin x</equation>围成.<equation>D_{1}</equation>关于y轴对

(a)

(b)

称，<equation>D_{2}</equation>关于 x轴对称.

由于<equation>x y^{5}</equation>为关于x的奇函数，故<equation>\iint_{D_{1}} x y^{5} \mathrm{d} x \mathrm{d} y=0.</equation>又由于<equation>x y^{5}</equation>为关于y的奇函数，故<equation>\iint_{D_{2}} x y^{5} \mathrm{d} x \mathrm{d} y=0.</equation>从而，<equation>\iint_{D} x y^{5} \mathrm{d} x \mathrm{d} y=0.</equation>将 D写成 X型区域，<equation>D = \left\{(x, y) \mid \sin x \leqslant y \leqslant 1, - \frac {\pi}{2} \leqslant x \leqslant \frac {\pi}{2} \right\}.</equation>因此，<equation>\iint_ {D} \left(x y ^ {5} - 1\right) \mathrm {d} x \mathrm {d} y = \iint_ {D} x y ^ {5} \mathrm {d} x \mathrm {d} y - \iint_ {D} \mathrm {d} x \mathrm {d} y = - \iint_ {D} \mathrm {d} x \mathrm {d} y = - \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \left(1 - \sin x\right) \mathrm {d} x = - \pi .</equation>应选 D.

---

**2012年第18题 | 解答题 | 10分**
18. (本题满分10分）计算二重积分<equation>\iint_{D} xy\mathrm{d}\sigma</equation>，其中区域 D由曲线<equation>r=1+\cos \theta</equation>（<equation>0\leqslant \theta \leqslant \pi</equation>）与极轴围成.
**答案: **<equation>(1 8) \frac {1 6}{1 5}.</equation>
**解析: **积分区域 D如图所示. 写出区域 D的表示.<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 1 + \cos \theta , 0 \leqslant \theta \leqslant \pi \right\}</equation>因此，

$$
\begin{array}{l} \iint_ {D} x y \mathrm {d} \sigma \stackrel {\text {极 坐 标}} {=} \iint_ {D} r ^ {2} \cos \theta \sin \theta \cdot r \mathrm {d} r \mathrm {d} \theta = \int_ {0} ^ {\pi} \cos \theta \sin \theta \mathrm {d} \theta \int_ {0} ^ {1 + \cos \theta} r ^ {3} \mathrm {d} r \\ = \int_ {0} ^ {\pi} \frac {\left(1 + \cos \theta\right) ^ {4}}{4} \cos \theta \sin \theta \mathrm {d} \theta \frac {u = 1 + \cos \theta}{\underline {

---

**2011年第13题 | 填空题 | 4分**
13. 设平面区域 D 由直线 y=x，圆<equation>x^{2}+y^{2}=2y</equation>及 y轴所围成，则二重积分<equation>\iint_{D} xy\mathrm{d}\sigma=</equation>___
**答案: **# 7 12.
**解析: **解 区域 D 如图所示.

在极坐标系下，圆方程<equation>x^{2}+y^{2}=2 y</equation>化为<equation>r^{2}=2 r \sin \theta</equation>，化简得到<equation>r=2 \sin \theta</equation>直线<equation>y=x</equation>的方程化为<equation>\theta=\frac{\pi}{4}.</equation>y轴方程化为<equation>\theta=\frac{\pi}{2}.</equation>从而可写出区域D的表示.<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2 \sin \theta , \frac {\pi}{4} \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation>因此，<equation>\iint_ {D} x y \mathrm {d} \sigma = \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \sin \theta \cos \theta \mathrm {d} \theta \int_ {0} ^ {2 \sin \theta} r ^ {3} \mathrm {d} r = 4 \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \sin^ {5} \theta \cos \theta \mathrm {d} \theta = 4 \cdot \left. \frac {\sin^ {6} \theta}{6} \right| _ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} = \frac {7}{1 2}.</equation>

---

**2011年第21题 | 解答题 | 11分**
21. (本题满分11分)

已知函数 f(x,y)具有二阶连续偏导数，且<equation>f(1,y)=f(x,1)=0,\iint_{D}f(x,y)\mathrm{d}x\mathrm{d}y=a</equation>，其中 D={（x,y）|0≤x≤ 1,0≤y≤1}，计算二重积分<equation>I=\iint_{D}xyf_{xy}^{\prime\prime}(x,y)\mathrm{d}x\mathrm{d}y.</equation>
**答案: **(21) a.
**解析: **解 由于<equation>f_{xy}^{\prime \prime}(x,y)</equation>是<equation>f_x^{\prime}(x,y)</equation>对<equation>y</equation>的偏导数，故对每个固定的<equation>x,f_{xy}^{\prime \prime}(x,y)\mathrm{d}y = \mathrm{d}[f_x^{\prime}(x,y)]</equation><equation>\begin{aligned} I &= \iint_ {D} x y f _ {x y} ^ {\prime \prime} (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} x \mathrm {d} x \int_ {0} ^ {1} y f _ {x y} ^ {\prime \prime} (x, y) \mathrm {d} y = \int_ {0} ^ {1} x \mathrm {d} x \int_ {0} ^ {1} y \mathrm {d} \left[ f _ {x} ^ {\prime} (x, y) \right] \\ \underline {{\text {分 部 积 分}}} \int_ {0} ^ {1} x \left[ y f _ {x} ^ {\prime} (x, y) \right| _ {y = 0} ^ {y = 1} - \int_ {0} ^ {1} f _ {x} ^ {\prime} (x, y) \mathrm {d} y ] \mathrm {d} x &= \int_ {0} ^ {1} x f _ {x} ^ {\prime} (x, 1) \mathrm {d} x - \int_ {0} ^ {1} x \mathrm {d} x \int_ {0} ^ {1} f _ {x} ^ {\prime} (x, y) \mathrm {d} y. \end{aligned}</equation>由于<equation>f ( x, 1 ) = 0</equation>，即一元函数<equation>f ( x, 1 )</equation>是关于 x的常函数，故<equation>f_{x}^{\prime} ( x, 1 ) = 0.</equation>又由于 D为矩形区域，故交换二次积分的积分次序可得，<equation>\int_ {0} ^ {1} x \mathrm {d} x \int_ {0} ^ {1} f _ {x} ^ {\prime} (x, y) \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {1} x f _ {x} ^ {\prime} (x, y) \mathrm {d} x.</equation>从而，<equation>\begin{aligned} I &= 0 - \int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {1} x f _ {x} ^ {\prime} (x, y) \mathrm {d} x = - \int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {1} x \mathrm {d} [ f (x, y) ] \\ \underline {{\text {分 部 积 分}}} - \int_ {0} ^ {1} \left[ x f (x, y) \left| _ {x = 0} ^ {x = 1} - \int_ {0} ^ {1} f (x, y) \mathrm {d} x \right] \mathrm {d} y &= - \int_ {0} ^ {1} f (1, y) \mathrm {d} y + \int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {1} f (x, y) \mathrm {d} x \right. \\ \underline {{\underline {{f (1 , y) = 0}}}} \int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {1} f (x, y) \mathrm {d} x &= \iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = a. \end{aligned}</equation>

---

**2010年第20题 | 解答题 | 11分**
0. (本题满分10分）

计算二重积分<equation>I=\iint_{D} r^{2}\sin \theta \sqrt{1-r^{2}\cos 2\theta}\mathrm{d}r\mathrm{d}\theta</equation>，其中<equation>D=\left\{(r,\theta)\mid 0\leqslant r\leqslant \sec \theta ,0\leqslant \theta \leqslant \frac{\pi}{4}\right\} .</equation>
**答案: **<equation>2 0) I = \frac {1}{3} - \frac {\pi}{1 6}.</equation>
**解析: **解 在极坐标系下，积分区域<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \sec \theta, 0 \leqslant \theta \leqslant \frac{\pi}{4}\right\}</equation>由<equation>0 \leqslant r \leqslant \sec \theta</equation>得，<equation>0 \leqslant r \cos \theta \leqslant 1</equation>. 又由于<equation>0 \leqslant \theta \leqslant \frac{\pi}{4}</equation>，故可知在直角坐标系下，<equation>D</equation>为由<equation>x = 1, y = x</equation>以及<equation>x</equation>轴围成的三角形区域，积分区域如图所示.将<equation>D</equation>写成X型区域，<equation>D = \left\{(x, y) \mid 0 \leqslant y \leqslant x, 0 \leqslant x \leqslant 1 \right\}</equation>由<equation>\left\{ \begin{array}{l l} x = r\cos \theta , \\ y = r\sin \theta , \end{array} \right.</equation>可将<equation>r^{2}\cos 2\theta</equation>表示为<equation>r ^ {2} \cos 2 \theta = r ^ {2} \cos^ {2} \theta - r ^ {2} \sin^ {2} \theta = x ^ {2} - y ^ {2}.</equation>因此，<equation>\begin{aligned} I &= \iint_ {D} y \sqrt {1 - \left(x ^ {2} - y ^ {2}\right)} \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {x} y \sqrt {1 - \left(x ^ {2} - y ^ {2}\right)} \mathrm {d} y \\ &= \frac {1}{2} \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {x} \sqrt {y ^ {2} - x ^ {2}} + 1 \mathrm {d} \left(y ^ {2} - x ^ {2} + 1\right) = \frac {1}{2} \int_ {0} ^ {1} \frac {2}{3} \left(y ^ {2} - x ^ {2} + 1\right) ^ {\frac {3}{2}} \Bigg | _ {y = 0} ^ {y = x} \mathrm {d} x \\ &= \frac {1}{3} - \frac {1}{3} \int_ {0} ^ {1} \left(1 - x ^ {2}\right) ^ {\frac {3}{2}} \mathrm {d} x \xlongequal {x = \sin t} \frac {1}{3} - \frac {1}{3} \int_ {0} ^ {\frac {\pi}{2}} \left(\cos^ {2} t\right) ^ {\frac {3}{2}} \cdot \cos t \mathrm {d} t \\ &= \frac {1}{3} - \frac {1}{3} \int_ {0} ^ {\frac {\pi}{2}} \cos^ {4} t \mathrm {d} t = \frac {1}{3} - \frac {1}{3} \times \frac {\pi}{2} \times \frac {3}{4} \times \frac {1}{2} = \frac {1}{3} - \frac {\pi}{1 6}. \end{aligned}</equation>

---

**2009年第19题 | 解答题 | 10分**
19. (本题满分10分)

计算二重积分<equation>\iint_{D} ( x-y ) \mathrm{d} x \mathrm{d} y</equation>，其中<equation>D=\left\{( x, y ) \mid( x-1 )^{2}+( y-1 )^{2} \leqslant 2, y \geqslant x \right\} .</equation>
**答案: **<equation>(1 9) - \frac {8}{3}.</equation>
**解析: **解（法一）如图（a）所示，作极坐标变换<equation>\left\{\begin{array}{l l}x=r\cos \theta ,\\ y=r\sin \theta ,\end{array} \right.</equation>则圆方程<equation>( x-1 )^{2}+( y-1 )^{2}=2</equation>变成<equation>r=2(\cos \theta +\sin \theta )</equation>从而D在极坐标系下表示为<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2 (\cos \theta + \sin \theta), \frac {\pi}{4} \leqslant \theta \leqslant \frac {3 \pi}{4} \right\}.</equation>因此，<equation>\begin{aligned} \iint_ {D} (x - y) \mathrm {d} x \mathrm {d} y &= \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} (\cos \theta - \sin \theta) \mathrm {d} \theta \int_ {0} ^ {2 (\cos \theta + \sin \theta)} r ^ {2} \mathrm {d} r = \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} (\cos \theta - \sin \theta) \left[ \frac {r ^ {3}}{3} \Big | _ {0} ^ {2 (\cos \theta + \sin \theta)} \right] \mathrm {d} \theta \\ &= \frac {8}{3} \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} (\cos \theta + \sin \theta) ^ {2} \left(\cos^ {2} \theta - \sin^ {2} \theta\right) \mathrm {d} \theta = \frac {8}{3} \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} (1 + \sin 2 \theta) \cos 2 \theta \mathrm {d} \theta \\ \underline {{= u = \sin 2 \theta}} \frac {4}{3} \int_ {1} ^ {- 1} (1 + u) \mathrm {d} u &= - \frac {8}{3}. \end{aligned}</equation>(a)

(b)

或者也可以这样计算.<equation>\begin{aligned} \iint_ {D} (x - y) \mathrm {d} x \mathrm {d} y &= \frac {8}{3} \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} (\cos \theta + \sin \theta) ^ {3} (\cos \theta - \sin \theta) \mathrm {d} \theta = \frac {8}{3} \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} (\cos \theta + \sin \theta) ^ {3} \mathrm {d} (\cos \theta + \sin \theta) \\ &= \frac {2}{3} \left(\cos \theta + \sin \theta\right) ^ {4} \Bigg | _ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} = - \frac {8}{3}. \end{aligned}</equation>（法二）作换元<equation>\left\{\begin{array}{l l}x=1+r\cos \theta ,\\ y=1+r\sin \theta ,\end{array} \right.</equation>则圆方程<equation>( x-1 )^{2}+( y-1 )^{2}=2</equation>变为<equation>r^{2}=2</equation>，而直线 y=x变为<equation>\theta =\frac{\pi}{4}</equation>和<equation>\theta =\frac{5\pi}{4}</equation>如图（b）所示，原区域 D变成区域<equation>D^{\prime}=\left\{(r,\theta)\mid 0\leqslant r\leqslant \sqrt{2},\frac{\pi}{4}\leqslant \theta \leqslant \frac{5\pi}{4}\right\}</equation>计算该变换的雅可比行列式.<equation>J (r, \theta) = \left| \begin{array}{c c} \cos \theta & - r \sin \theta \\ \sin \theta & r \cos \theta \end{array} \right| = r.</equation>因此，<equation>\begin{aligned} \text {原 积 分} &= \iint_ {D ^ {\prime}} r (\cos \theta - \sin \theta) \cdot r \mathrm {d} r \mathrm {d} \theta = \int_ {\frac {\pi}{4}} ^ {\frac {5 \pi}{4}} (\cos \theta - \sin \theta) \mathrm {d} \theta \int_ {0} ^ {\sqrt {2}} r ^ {2} \mathrm {d} r \\ &= \int_ {\frac {\pi}{4}} ^ {\frac {5 \pi}{4}} (\cos \theta - \sin \theta) \left(\frac {r ^ {3}}{3} \Big | _ {0} ^ {\sqrt {2}}\right) \mathrm {d} \theta = \frac {2 \sqrt {2}}{3} (\sin \theta + \cos \theta) \Big | _ {\frac {\pi}{4}} ^ {\frac {5 \pi}{4}} = - \frac {8}{3}. \end{aligned}</equation>

---


**2009年第22题 | 解答题 | 11分**


假设<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ - 1 & 1 & 1 \\ 0 & - 4 & - 2 \end{array} \right), \quad \boldsymbol {\xi} _ {1} = \left( \begin{array}{c} - 1 \\ 1 \\ - 2 \end{array} \right).</equation>I. 求满足<equation>A\xi_{2}=\xi_{1}, A^{2}\xi_{3}=\xi_{1}</equation>的所有向量<equation>\xi_{2},\xi_{3}</equation>；

II. 对第一问中的任意向量<equation>\xi_{2},\xi_{3}</equation>，证明<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

**答案:**（22）（I）满足<equation>A\xi_{2}=\xi_{1}</equation>的所有向量为<equation>\xi_{2}=k_{1}(1,-1,2)^{\mathrm{T}}+(0,0,1)^{\mathrm{T}}</equation>，其中<equation>k_{1}</equation>为任意常数；满足<equation>A^{2}\xi_{3}=\xi_{1}</equation>的所有向量<equation>\xi_{3}</equation>为<equation>\xi_{3}=k_{2}(1,-1,0)^{\mathrm{T}}+k_{3}(0,0,1)^{\mathrm{T}}+\left(-\frac{1}{2},0,0\right)^{\mathrm{T}}</equation>，其中<equation>k_{2},k_{3}</equation>为任意常数.

（Ⅱ）证明略.

**解析:**解（I）解<equation>A x=\xi_{1}</equation>，这是一个非齐次线性方程组.<equation>\left(\boldsymbol {A}, \boldsymbol {\xi} _ {1}\right) = \left( \begin{array}{c c c c} 1 & - 1 & - 1 & - 1 \\ - 1 & 1 & 1 & 1 \\ 0 & - 4 & - 2 & - 2 \end{array} \right) \xrightarrow [ r _ {2} ^ {*} \leftrightarrow r _ {3} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c} 1 & - 1 & - 1 & - 1 \\ 0 & - 4 & - 2 & - 2 \\ 0 & 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {1} + r _ {2} ^ {* * *} ]{r _ {2} ^ {* *} \times \left(- \frac {1}{2}\right)} \left( \begin{array}{c c c c} 1 & 1 & 0 & 0 \\ 0 & 2 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{array} \right).</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每做一次初等行变换，加一个*.）

于是<equation>r(\mathbf{A}) = r(\mathbf{A},\xi_1) = 2.Ax = \xi_1</equation>有无穷多解.其对应的齐次方程组等价于<equation>\left\{ \begin{array}{l l} x_{1} + x_{2} = 0, \\ 2x_{2} + x_{3} = 0, \end{array} \right.</equation>故可取<equation>(1, - 1,2)^{\mathrm{T}}</equation>为它的一个基础解系.另外，<equation>\left\{ \begin{array}{l l} x_{1} + x_{2} = 0, \\ 2x_{2} + x_{3} = 1 \end{array} \right.</equation>的一个特解为<equation>(0,0,1)^{\mathrm{T}}.</equation>因此，<equation>Ax = \xi_{1}</equation>的通解为<equation>\xi_{2} = k_{1}(1, -1, 2)^{\mathrm{T}} + (0, 0, 1)^{\mathrm{T}}</equation>，其中<equation>k_{1}</equation>为任意常数.<equation>\left(\boldsymbol {A} ^ {2}, \boldsymbol {\xi} _ {1}\right) = \left( \begin{array}{c c c c} 2 & 2 & 0 & - 1 \\ - 2 & - 2 & 0 & 1 \\ 4 & 4 & 0 & - 2 \end{array} \right) \xrightarrow [ r _ {3} - 2 r _ {1} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c} 2 & 2 & 0 & - 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{array} \right).</equation>于是<equation>r \left( A^{2} \right)=r \left( A^{2}, \xi_{1} \right)=1. A^{2} x=\xi_{1}</equation>有无穷多解.其对应的齐次方程组等价于<equation>2 \left( x_{1}+x_{2} \right)=0</equation>故可取（1，-1，0）<equation>^{\mathrm{T}}</equation>和（0，0，1）<equation>^{\mathrm{T}}</equation>为它的一个基础解系.另外，<equation>2 \left( x_{1}+x_{2} \right)=-1</equation>的一个特解为<equation>\left(-\frac{1}{2},0,0\right)^{\mathrm{T}}.</equation>因此，<equation>A^{2}x = \xi_{1}</equation>的通解为<equation>\xi_{3} = k_{2}(1, -1, 0)^{\mathrm{T}} + k_{3}(0, 0, 1)^{\mathrm{T}} + \left(-\frac{1}{2}, 0, 0\right)^{\mathrm{T}}</equation>，其中<equation>k_{2}, k_{3}</equation>为任意常数.

（Ⅱ）（法一）通过计算可知，<equation>\boldsymbol {A} \boldsymbol {\xi} _ {1} = \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ - 1 & 1 & 1 \\ 0 & - 4 & - 2 \end{array} \right) \left( \begin{array}{c} - 1 \\ 1 \\ - 2 \end{array} \right) = \left( \begin{array}{c} 0 \\ 0 \\ 0 \end{array} \right).</equation>从而<equation>A^{3}\xi_{3} = A^{2}\xi_{2} = A\xi_{1} = 0.</equation>我们可以利用该性质推出<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

不妨设<equation>a\boldsymbol{\xi}_1 + b\boldsymbol{\xi}_2 + c\boldsymbol{\xi}_3 = \mathbf{0}</equation>. 该等式两端同时左乘<equation>A^2</equation>，得<equation>a A ^ {2} \xi_ {1} + b A ^ {2} \xi_ {2} + c A ^ {2} \xi_ {3} = c A ^ {2} \xi_ {3} = c \xi_ {1} = \mathbf {0}.</equation>由于<equation>\boldsymbol{\xi}_{1}</equation>为非零向量，故<equation>c=0.</equation>于是<equation>a\boldsymbol{\xi}_{1}+b\boldsymbol{\xi}_{2}=\mathbf{0}.</equation>再在<equation>a\boldsymbol{\xi}_{1}+b\boldsymbol{\xi}_{2}=\mathbf{0}</equation>两端同时左乘 A，得<equation>aA\boldsymbol{\xi}_{1}+bA\boldsymbol{\xi}_{2}=bA\boldsymbol{\xi}_{1}=b\boldsymbol{\xi}_{2}=\mathbf{0}.</equation><equation>a A \xi_ {1} + b A \xi_ {2} = b A \xi_ {2} = b \xi_ {1} = 0.</equation>同理得<equation>b = 0</equation>. 由于<equation>b = c = 0</equation>, 故<equation>a\xi_{1} = 0</equation>. 从而<equation>a = 0</equation>.

因此，<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

（法二）由第（I）问，我们得到<equation>\xi_{1},\xi_{2},\xi_{3}</equation>的表达式，从而可以通过计算<equation>|\xi_{1},\xi_{2},\xi_{3}|</equation>来说明<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.<equation>\begin{aligned} | \xi_ {1}, \xi_ {2}, \xi_ {3} | &= \left| \begin{array}{c c c} - 1 & k _ {1} & k _ {2} - \frac {1}{2} \\ 1 & - k _ {1} & - k _ {2} \\ - 2 & 2 k _ {1} + 1 & k _ {3}  \right| \frac {c _ {2} + k _ {1} c _ {1}}{c _ {3} + k _ {2} c _ {1}} \left| \begin{array}{c c c} - 1 & 0 & - \frac {1}{2} \\ 1 & 0 & 0 \\ - 2 & 1 & k _ {3} - 2 k _ {2}  \right| \\ \underline {{\text {按 第二 行 展 开}}} (- 1) \left| \begin{array}{c c} 0 & - \frac {1}{2} \\ 1 & k _ {3} - 2 k _ {2}  \right| &= - \frac {1}{2} \neq 0. \end{aligned}</equation>因此，<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

---