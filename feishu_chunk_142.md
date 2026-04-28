#### 常系数齐次线性微分方程

**2023年第3题 | 选择题 | 5分 | 答案: C**

3. 若微分方程<equation>y^{\prime \prime}+ay^{\prime}+by=0</equation>的解在<equation>(-\infty,+\infty)</equation>上有界，则（    )

A. a < 0,b > 0 B. a > 0,b > 0 C. a = 0,b > 0 D. a = 0,b < 0

答案: C

**解析:**解 由于二阶常系数齐次线性微分方程必有零解，而零解为有界解，故微分方程<equation>y^{\prime \prime}+a y^{\prime}+b y</equation>=0必然存在（<equation>-\infty, +\infty</equation>）上的有界解.本题实际上是要求此方程的所有解都有界.

微分方程<equation>y^{\prime \prime}+a y^{\prime}+b y=0</equation>的特征方程为<equation>\lambda^{2}+a \lambda+b=0.</equation>- 若<equation>\Delta=a^{2}-4 b>0</equation>，则特征方程有两个不同实根<equation>\lambda_{1},\lambda_{2}</equation>，从而至少有一个实根非零.此时，微分方程的解为<equation>y=C_{1}\mathrm{e}^{\lambda_{1}x}+C_{2}\mathrm{e}^{\lambda_{2}x}.</equation>- 取<equation>C_{1}=C_{2}=1</equation>，则<equation>\lim_{x\to -\infty}\left(\mathrm{e}^{\lambda_{1}x}+\mathrm{e}^{\lambda_{2}x}\right)=+\infty</equation>或<equation>\lim_{x\to +\infty}\left(\mathrm{e}^{\lambda_{1}x}+\mathrm{e}^{\lambda_{2}x}\right)=+\infty.</equation>该解在<equation>(-\infty, +\infty)</equation>上无界.

- 若<equation>\Delta=a^{2}-4 b=0</equation>，则特征方程有两个相同实根<equation>\lambda</equation>.此时，微分方程的解为<equation>y=(C_{1}+ C_{2} x) \mathrm{e}^{\lambda x}.</equation>取<equation>C_{1}=0, C_{2}=1</equation>，则<equation>\lim_{x\to -\infty}x\mathrm{e}^{\lambda x}=\infty</equation>或<equation>\lim_{x\to +\infty}x\mathrm{e}^{\lambda x}=\infty</equation>.该解在<equation>(-\infty , +\infty)</equation>上无界.

- 若<equation>\Delta=a^{2}-4 b<0</equation>，则特征方程有一对共轭复根<equation>\lambda_{1,2}=\alpha\pm\beta\mathrm{i}</equation>.此时，微分方程的解为<equation>y=\mathrm{e}^{\alpha x}\left(C_{1}\cos \beta x+C_{2}\sin \beta x\right).</equation>当<equation>\alpha\neq0</equation>时，取<equation>C_{1}=1,C_{2}=0</equation>，所得解<equation>y=\mathrm{e}^{\alpha x}\cos \beta x</equation>是<equation>(-\infty, +\infty)</equation>上的无界函数.

当<equation>\alpha=0</equation>时，微分方程的解为<equation>y=C_{1}\cos \beta x+C_{2}\sin \beta x</equation>对任意常数<equation>C_{1},C_{2}</equation>，该解在<equation>(-\infty,+\infty)</equation>上均有界.根据求根公式，<equation>\lambda_{1,2}=-\frac{a}{2}\pm \frac{\sqrt{4b-a^{2}}}{2}\mathrm{i}</equation>即<equation>\alpha=-\frac{a}{2}</equation>于是，<equation>a=0</equation>结合<equation>a^{2}-4b<0</equation>可知，<equation>b>0.</equation>因此，<equation>a=0,b>0</equation>应选C.

---

**2020年第17题 | 解答题 | 10分**

17. (本题满分10分)

设函数 y=f(x)满足<equation>y^{\prime \prime}+2 y^{\prime}+5 y=0</equation>，且 f(0)=1，<equation>f^{\prime}(0)=-1.</equation>I. 求 f(x)的表达式；

II. 设<equation>a_{n}=\int_{n \pi}^{+\infty} f(x)\mathrm{d} x</equation>，求<equation>\sum_{n=1}^{\infty} a_{n}.</equation>

**答案:**<equation>\begin{array}{l} (\mathrm {I}) f (x) = \mathrm {e} ^ {- x} \cos 2 x; \\ (\mathrm {I I}) \sum_ {n = 1} ^ {\infty} a _ {n} = \frac {1}{5 \left(\mathrm {e} ^ {\pi} - 1\right)}. \\ \end{array}</equation>

**解析:**解（I）<equation>y^{\prime \prime}+2 y^{\prime}+5 y=0</equation>的特征方程为<equation>r^{2}+2 r+5=0</equation>.解得特征根<equation>r_{1,2}=-1\pm 2 \mathrm{i}.</equation>由特征根与解的关系可得<equation>f (x) = \mathrm {e} ^ {- x} \left(C _ {1} \cos 2 x + C _ {2} \sin 2 x\right),</equation>其中<equation>C_{1}, C_{2}</equation>为待定常数.

由<equation>f(0) = 1</equation>可得，<equation>C_{1} = 1.</equation>计算<equation>f^{\prime}(x).</equation><equation>f ^ {\prime} (x) = - \mathrm {e} ^ {- x} \left(C _ {1} \cos 2 x + C _ {2} \sin 2 x\right) + \mathrm {e} ^ {- x} \left(- 2 C _ {1} \sin 2 x + 2 C _ {2} \cos 2 x\right).</equation>由<equation>f^{\prime}(0)=-1</equation>可得，<equation>-C_{1}+2 C_{2}=-1</equation>，解得<equation>C_{2}=0.</equation>因此，<equation>f ( x ) = \mathrm{e}^{-x}\cos 2x.</equation>（Ⅱ）（法一）由<equation>y^{\prime \prime}+2 y^{\prime}+5 y=0</equation>可得，<equation>f(x)=-\frac{1}{5}[f^{\prime \prime}(x)+2 f^{\prime}(x)]</equation>.于是，<equation>\begin{array}{l} a _ {n} = \int_ {n \pi} ^ {+ \infty} f (x) \mathrm {d} x = - \frac {1}{5} \int_ {n \pi} ^ {+ \infty} \left[ f ^ {\prime \prime} (x) + 2 f ^ {\prime} (x) \right] \mathrm {d} x = - \frac {1}{5} \left[ f ^ {\prime} (x) + 2 f (x) \right] \Bigg | _ {n \pi} ^ {+ \infty} \\ = - \frac {1}{5} \left\{\lim _ {x \rightarrow + \infty} \left[ f ^ {\prime} (x) + 2 f (x) \right] - \left[ f ^ {\prime} (n \pi) + 2 f (n \pi) \right]\right\}. \\ \end{array}</equation>由第（I）问可知，<equation>f(x) = \mathrm{e}^{-x}\cos 2x,f^{\prime}(x) = -\mathrm{e}^{-x}\cos 2x-2\mathrm{e}^{-x}\sin 2x.</equation>从而，<equation>\lim_{x\to +\infty}f(x) = 0,</equation><equation>\lim_{x\to +\infty}f^{\prime}(x) = 0,f(n\pi) = \mathrm{e}^{-n\pi},f^{\prime}(n\pi) = -\mathrm{e}^{-n\pi}.</equation>因此，<equation>a _ {n} = \frac {1}{5} \left[ f ^ {\prime} (n \pi) + 2 f (n \pi) \right] = \frac {1}{5} \mathrm {e} ^ {- n \pi}.</equation><equation>\sum_ {n = 1} ^ {\infty} a _ {n} = \frac {1}{5} \sum_ {n = 1} ^ {\infty} \mathrm {e} ^ {- n \pi} = \frac {1}{5} \cdot \frac {\mathrm {e} ^ {- \pi}}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{5 \left(\mathrm {e} ^ {\pi} - 1\right)}.</equation>（法二）计算<equation>a_{n}</equation><equation>\begin{array}{l} a _ {n} = \int_ {n \pi} ^ {+ \infty} \mathrm {e} ^ {- x} \cos 2 x \mathrm {d} x \xlongequal {t = x - n \pi} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- (t + n \pi)} \cos 2 (t + n \pi) \mathrm {d} t \\ = \mathrm {e} ^ {- n \pi} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- t} \cos 2 t \mathrm {d} t. \\ \end{array}</equation>下面计算<equation>\int_{0}^{+\infty}\mathrm{e}^{-t}\cos 2t\mathrm{d}t.</equation><equation>\begin{array}{l} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- t} \cos 2 t \mathrm {d} t = - \int_ {0} ^ {+ \infty} \cos 2 t \mathrm {d} \left(\mathrm {e} ^ {- t}\right) = - \left[ \mathrm {e} ^ {- t} \cos 2 t \Big | _ {0} ^ {+ \infty} - \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- t} \cdot (- 2 \sin 2 t) \mathrm {d} t \right] \\ = - \left(- 1 + 2 \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- t} \sin 2 t \mathrm {d} t\right) = 1 - 2 \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- t} \sin 2 t \mathrm {d} t \\ = 1 + 2 \int_ {0} ^ {+ \infty} \sin 2 t \mathrm {d} \left(\mathrm {e} ^ {- t}\right) = 1 + 2 \left(\mathrm {e} ^ {- t} \sin 2 t \Big | _ {0} ^ {+ \infty} - \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- t} \cdot 2 \cos 2 t \mathrm {d} t\right) \\ = 1 - 4 \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- t} \cos 2 t \mathrm {d} t. \\ \end{array}</equation>由上式可得，<equation>5\int_{0}^{+\infty}\mathrm{e}^{-t}\cos 2t\mathrm{d}t=1</equation>即<equation>\int_{0}^{+\infty}\mathrm{e}^{-t}\cos 2t\mathrm{d}t=\frac{1}{5}.</equation>因此，<equation>a_{n}=\frac{1}{5}\mathrm{e}^{-n\pi}.</equation><equation>\sum_ {n = 1} ^ {\infty} a _ {n} = \frac {1}{5} \sum_ {n = 1} ^ {\infty} \mathrm {e} ^ {- n \pi} = \frac {1}{5} \cdot \frac {\mathrm {e} ^ {- \pi}}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{5 \left(\mathrm {e} ^ {\pi} - 1\right)}.</equation>

---

**2015年第12题 | 填空题 | 4分**

12. 设函数<equation>y=y(x)</equation>是微分方程<equation>y^{\prime\prime}+y^{\prime}-2y=0</equation>的解，且在<equation>x=0</equation>处<equation>y(x)</equation>取得极值3，则<equation>y(x)=</equation>___.

**答案:**<equation>2 \mathrm{e}^{x}+\mathrm{e}^{-2 x}.</equation>

**解析:**解<equation>y^{\prime \prime}+y^{\prime}-2 y=0</equation>的特征方程为<equation>\lambda^{2}+\lambda-2=0</equation>，解得<equation>\lambda_{1}=1,\lambda_{2}=-2.</equation>于是<equation>y(x)= C_{1}\mathrm{e}^{x}+C_{2}\mathrm{e}^{-2x}</equation>，其中<equation>C_{1},C_{2}</equation>为待定常数.

由题设及一元函数取极值的必要条件知，<equation>y ( 0 )=3, y^{\prime} ( 0 )=0.</equation>将其代入 y(x）的表达式中可得<equation>C_{1}+C_{2}=3, C_{1}-2 C_{2}=0.</equation>解得<equation>C_{1}=2, C_{2}=1.</equation>因此，<equation>y (x) = 2 \mathrm {e} ^ {x} + \mathrm {e} ^ {- 2 x}.</equation>

---

**2013年第12题 | 填空题 | 4分**

12. 微分方程<equation>y^{\prime\prime}-y^{\prime}+\frac{1}{4} y=0</equation>的通解为 y=___

**答案:**（<equation>C_{1}+C_{2}x) \mathrm{e}^{\frac{1}{2} x}</equation>，其中<equation>C_{1},C_{2}</equation>为任意常数.

**解析:**解 微分方程<equation>y^{\prime \prime}-y^{\prime}+\frac{1}{4} y=0</equation>的特征方程为<equation>\lambda^{2}-\lambda+\frac{1}{4}=0</equation>，解得<equation>\lambda_{1}=\lambda_{2}=\frac{1}{2}</equation>因此，原方程的通解为<equation>y=(C_{1}+C_{2}x)\mathrm{e}^{\frac{1}{2}x}</equation>其中<equation>C_{1}, C_{2}</equation>为任意常数.

---

**2012年第19题 | 解答题 | 10分**

19. (本题满分10分)

已知函数 f(x)满足方程<equation>f^{\prime \prime}(x)+f^{\prime}(x)-2 f(x)=0</equation>及<equation>f^{\prime \prime}(x)+f(x)=2 \mathrm{e}^{x}</equation>.

I. 求 f(x)的表达式;

II. 求曲线<equation>y=f\left(x^{2}\right)\int_{0}^{x} f\left(-t^{2}\right)\mathrm{d} t</equation>的拐点.

**答案:**(19) ( I )<equation>f(x)=\mathrm{e}^{x};</equation>( II ) ( 0,0 ).

**解析:**解（I）（法一）本题中有两个微分方程，可先写出其中的二阶常系数齐次线性微分方程的通解，再将该通解代入另一个方程以确定通解中的常数.<equation>f^{\prime \prime}(x) + f^{\prime}(x) - 2 f(x) = 0</equation>为二阶常系数齐次线性微分方程它的特征方程为<equation>r^{2}+r-2=0</equation>，该方程有两个不同的实根<equation>r_{1}=1,r_{2}=-2</equation>，从而其解为<equation>f(x)=C_{1}\mathrm{e}^{x}+C_{2}\mathrm{e}^{-2x}</equation>其中<equation>C_{1},C_{2}</equation>为待定常数.

计算<equation>f^{\prime}(x), f^{\prime\prime}(x)</equation>得<equation>f ^ {\prime} (x) = C _ {1} \mathrm {e} ^ {x} - 2 C _ {2} \mathrm {e} ^ {- 2 x}, f ^ {\prime \prime} (x) = C _ {1} \mathrm {e} ^ {x} + 4 C _ {2} \mathrm {e} ^ {- 2 x}.</equation>代入<equation>f^{\prime \prime}(x) + f(x) = 2\mathrm{e}^{x}</equation>，得<equation>2C_{1}\mathrm{e}^{x} + 5C_{2}\mathrm{e}^{-2x} = 2\mathrm{e}^{x}</equation>，从而得<equation>C_{1} = 1, C_{2} = 0.</equation>因此，<equation>f ( x ) = \mathrm{e}^{x}.</equation><equation>f ^ {\prime \prime} (x) + f ^ {\prime} (x) - 2 f (x) = 0,</equation><equation>f ^ {\prime \prime} (x) + f (x) = 2 \mathrm {e} ^ {x}.</equation>(1) 式-（2）式得<equation>f^{\prime}(x) - 3f(x) = -2\mathrm{e}^{x}</equation>，为一阶非齐次线性微分方程.由求解公式得<equation>f (x) = C \mathrm {e} ^ {- \int (- 3) \mathrm {d} x} + \mathrm {e} ^ {- \int (- 3) \mathrm {d} x} \int \left(- 2 \mathrm {e} ^ {x}\right) \mathrm {e} ^ {\int (- 3) \mathrm {d} x} \mathrm {d} x = \mathrm {e} ^ {x} + C \mathrm {e} ^ {3 x},</equation>其中 C为待定常数.

代回（2）式，得<equation>\mathrm {e} ^ {x} + 9 C \mathrm {e} ^ {3 x} + \mathrm {e} ^ {x} + C \mathrm {e} ^ {3 x} = 2 \mathrm {e} ^ {x}.</equation>从而 C=0.

因此，<equation>f ( x ) = \mathrm{e}^{x}.</equation>（Ⅱ）将<equation>f(x) = \mathrm{e}^{x}</equation>代入曲线方程，对<equation>y</equation>逐次求导，得<equation>y = f \left(x ^ {2}\right) \int_ {0} ^ {x} f \left(- t ^ {2}\right) \mathrm {d} t = \mathrm {e} ^ {x ^ {2}} \int_ {0} ^ {x} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t,</equation><equation>y ^ {\prime} = \mathrm {e} ^ {x ^ {2}} \cdot \mathrm {e} ^ {- x ^ {2}} + 2 x \mathrm {e} ^ {x ^ {2}} \int_ {0} ^ {x} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t = 1 + 2 x y,</equation><equation>y ^ {\prime \prime} = \frac {\mathrm {d} (1 + 2 x y)}{\mathrm {d} x} = 2 y + 2 x y ^ {\prime} = 2 y + 2 x (1 + 2 x y) = 2 \left(2 x ^ {2} + 1\right) y + 2 x.</equation>由于<equation>\mathrm{e}^{x^{2}} > 0</equation><equation>\mathrm{e}^{-t^{2}} > 0</equation>，故当 x > 0时，y > 0.从而<equation>y ^ {\prime \prime} (x) = 2 \left(2 x ^ {2} + 1\right) y + 2 x > 0.</equation>当<equation>x < 0</equation>时，<equation>y < 0</equation><equation>y ^ {\prime \prime} (x) = 2 \left(2 x ^ {2} + 1\right) y + 2 x < 0.</equation>当<equation>x = 0</equation>时，<equation>y(0) = 0</equation>，<equation>y^{\prime \prime}(0) = 0.</equation>因此，点（0,0）为曲线<equation>y = f\left(x^{2}\right)\int_{0}^{x}f\left(-t^{2}\right)\mathrm{d}t</equation>的拐点.

---


