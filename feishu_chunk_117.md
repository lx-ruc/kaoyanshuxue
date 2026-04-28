#### 导数与微分的概念

**2025年第18题 | 解答题 | 12分**

18. 设函数 f(x)在 x=0处连续，且<equation>\lim_{x\rightarrow 0}\frac{x f(x)-\mathrm{e}^{2\sin x}+1}{\ln(1+x)+\ln(1-x)}=-3</equation>，证明 f(x)在 x=0处可导，并求<equation>f^{\prime}(0).</equation>

**答案:**证明略，<equation>f^{\prime}(0)=5.</equation>

**解析:**解分别计算<equation>\mathrm{e}^{2\sin x}</equation>在 x=0处的一阶、二阶导数，并写出<equation>\mathrm{e}^{2\sin x}</equation>在该点处的带佩亚诺余项的二阶泰勒公式.<equation>\left(\mathrm {e} ^ {2 \sin x}\right) ^ {\prime} = \mathrm {e} ^ {2 \sin x} \cdot 2 \cos x,</equation><equation>\left(\mathrm {e} ^ {2 \sin x}\right) ^ {\prime \prime} = 2 \left(\mathrm {e} ^ {2 \sin x} \cdot \cos x\right) ^ {\prime} = 2 \left(2 \mathrm {e} ^ {2 \sin x} \cos^ {2} x - \mathrm {e} ^ {2 \sin x} \sin x\right).</equation>于是，<equation>(\mathrm{e}^{2\sin x})^{\prime}|_{x=0} = 2,(\mathrm{e}^{2\sin x})^{\prime \prime}|_{x=0} = 4.</equation>结合<equation>\mathrm{e}^{2\sin x}|_{x=0} = 1</equation>可得，<equation>\mathrm {e} ^ {2 \sin x} = 1 + 2 x + \frac {4 x ^ {2}}{2} + o \left(x ^ {2}\right) = 1 + 2 x + 2 x ^ {2} + o \left(x ^ {2}\right).</equation>将（1）式代人已知极限可得，<equation>\begin{aligned} - 3 &= \lim _ {x \rightarrow 0} \frac {x f (x) - \mathrm {e} ^ {2 \sin x} + 1}{\ln (1 + x) + \ln (1 - x)} = \lim _ {x \rightarrow 0} \frac {x f (x) - 2 x - 2 x ^ {2} + o \left(x ^ {2}\right)}{\ln \left(1 - x ^ {2}\right)} \\ \frac {\ln \left(1 - x ^ {2}\right) - - x ^ {2}}{- x ^ {2}} \lim _ {x \rightarrow 0} \frac {x f (x) - 2 x - 2 x ^ {2} + o \left(x ^ {2}\right)}{- x ^ {2}} &= \lim _ {x \rightarrow 0} \frac {f (x) - 2}{- x} + 2. \end{aligned}</equation>由此可得，<equation>\lim_{x\to 0}\frac{f(x) - 2}{-x} = -5</equation>，即<equation>\lim_{x\to 0}\frac{f(x) - 2}{x} = 5.</equation>由于<equation>\lim_{x\to 0}x = 0</equation>，故<equation>\lim_{x\to 0}[f(x) - 2] = 0</equation>，从而<equation>\lim_{x\to 0}f(x) = 2.</equation>结合<equation>f(x)</equation>在<equation>x = 0</equation>处连续可得<equation>f(0)</equation><equation>= \lim_{x\to 0}f(x) = 2.</equation>进一步可得<equation>5 = \lim _ {x \rightarrow 0} \frac {f (x) - 2}{x} = \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0}.</equation>根据导数的定义，<equation>f(x)</equation>在<equation>x = 0</equation>处可导，且<equation>f^{\prime}(0) = 5.</equation>

---

**2021年第2题 | 选择题 | 5分 | 答案: D**

2. 函数 f(x) =<equation>\left\{\begin{array}{l l}{\frac{\mathrm{e}^{x}-1}{x},}&{x\neq0,\\{1,}&{x=0}\end{array} \right.</equation>在 x=0处（    ）

A. 连续且取极大值 B. 连续且取极小值 C. 可导且导数为零 D. 可导且导数不为零

答案: D

**解析:**首先考虑 f(x)在 x=0处的连续性.<equation>\lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x} - 1}{x} \xlongequal {\mathrm {e} ^ {x} - 1 \sim x} \lim _ {x \rightarrow 0} \frac {x}{x} = 1 = f (0).</equation>于是，f（x）在 x=0处连续.

下面考虑 f(x)在 x=0处的可导性.<equation>f ^ {\prime} (0) = \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0} \frac {\frac {\mathrm {e} ^ {x} - 1}{x} - 1}{x} = \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x} - 1 - x}{x ^ {2}} \frac {\mathrm {e} ^ {x} = 1 + x + \frac {x ^ {2}}{2} + o \left(x ^ {2}\right)}{\frac {1}{2} \neq 0}.</equation>于是，<equation>f ( x )</equation>在<equation>x=0</equation>处可导且导数不为0.

因此，应选D.

下面说明选项A、B不正确.

由于<equation>f^{\prime}(0)\neq 0</equation>，故 x=0不满足成为极值点的必要条件，从而选项A、B均不正确.

---

**2018年第1题 | 选择题 | 4分 | 答案: D**

1. 下列函数中，在 x=0处不可导的是（    ）

A. f(x）=|x|sin|x|

B. f(x)=|x|sin<equation>\sqrt{|x|}</equation>C. f(x)=cos|x|

D. f(x)=cos<equation>\sqrt{|x|}</equation>

答案: D

**解析:**解 考虑选项 D.<equation>f (x) = \left\{ \begin{array}{l l} \cos \sqrt {x}, & x \geqslant 0, \\ \cos \sqrt {- x}, & x < 0. \end{array} \right.</equation><equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {\cos \sqrt {- x} - 1}{x - 0} \frac {\cos \sqrt {- x} - 1 \sim - \frac {\left(\sqrt {- x}\right) ^ {2}}{2}}{\lim _ {x \rightarrow 0 ^ {-}} \frac {\frac {x}{2}}{x}} = \frac {1}{2},</equation><equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {\cos \sqrt {x} - 1}{x - 0} \frac {\cos \sqrt {x} - 1 \sim - \frac {\left(\sqrt {x}\right) ^ {2}}{2}}{\lim _ {x \rightarrow 0 ^ {+}} \frac {- \frac {x}{2}}{x}} = - \frac {1}{2}.</equation>由于<equation>f_{-}^{\prime}(0)\neq f_{+}^{\prime}(0)</equation>，故<equation>f(x)=\cos \sqrt{|x|}</equation>在 x=0处不可导.应选D.

下面分别说明选项A、B、C不正确.

选项A：<equation>f ( x )=\left\{\begin{array}{l l}x \sin x,\\- x \sin(- x),\end{array}\right.</equation><equation>x \geqslant0,</equation><equation>x < 0.</equation>又因为<equation>- x \sin(- x)=- x \cdot(- \sin x)=x \sin x</equation>，所以<equation>f ( x )=x \sin x,f ( x )</equation>在 x=0处可导.

选项B：<equation>f ( x )=\left\{\begin{array}{ll}x\sin \sqrt{x},&x\geqslant 0,\\ -x\sin \sqrt{-x},&x<0.\end{array} \right.</equation><equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {- x \sin \sqrt {- x} - 0}{x - 0} = \lim _ {x \rightarrow 0 ^ {-}} (- \sin \sqrt {- x}) = 0,</equation><equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {x \sin \sqrt {x} - 0}{x - 0} = \lim _ {x \rightarrow 0 ^ {+}} \sin \sqrt {x} = 0.</equation>由于<equation>f_{-}^{\prime}(0)=f_{+}^{\prime}(0)</equation>，故<equation>f(x)=|x|\sin \sqrt{|x|}</equation>在 x=0处可导.

选项C：<equation>f ( x )=\left\{\begin{array}{ll}\cos x,&x\geqslant0,\\ \cos(-x),&x<0.\end{array} \right.</equation>又因为<equation>\cos(-x)=\cos x</equation>，所以<equation>f ( x )=\cos x,f ( x )</equation>在 x=0处可导.

---

**2018年第12题 | 填空题 | 4分**

12. 设函数<equation>f(x)</equation>满足<equation>f(x+\Delta x)-f(x)=2 x f(x)\Delta x+o(\Delta x)(\Delta x\to 0)</equation>, 且<equation>f(0)=2</equation>, 则 f(1) ___

**解析:**由已知方程可得，<equation>\frac {f (x + \Delta x) - f (x)}{\Delta x} = 2 x f (x) + \frac {o (\Delta x)}{\Delta x}.</equation>在（1）式中，令<equation>\Delta x\rightarrow 0</equation>，可得<equation>f ^ {\prime} (x) \xlongequal {\text {导 数 定 义}} \lim _ {\Delta x \rightarrow 0} \frac {f (x + \Delta x) - f (x)}{\Delta x} = 2 x f (x) + \lim _ {\Delta x \rightarrow 0} \frac {o (\Delta x)}{\Delta x} = 2 x f (x),</equation>即<equation>f^{\prime}(x) = 2xf(x).f(x)</equation>满足微分方程<equation>y^{\prime} = 2xy.</equation>这是一个可分离变量的微分方程.分离变量得，<equation>\frac{\mathrm{d}y}{y}=2x\mathrm{d}x.</equation>方程两端积分可得，<equation>\ln |y|=x^{2}+C_{1},|y|=\mathrm{e}^{C_{1}}\cdot \mathrm{e}^{x^{2}}=C_{2}\mathrm{e}^{x^{2}}</equation>，其中<equation>C_{2}>0</equation>.于是，<equation>y=\pm C_{2}\mathrm{e}^{x^{2}}.</equation>由于 y=0也是<equation>y^{\prime}=2 x y</equation>的解，故<equation>y^{\prime}=2 x y</equation>的通解可写为<equation>y=C\mathrm{e}^{x^{2}}</equation>，其中C为任意常数.

将<equation>x = 0,f(0) = 2</equation>代入<equation>y = C\mathrm{e}^{x^2}</equation>，解得<equation>C = 2.</equation>因此，<equation>f(x) = 2\mathrm{e}^{x^2}</equation>，从而<equation>f(1) = 2\mathrm{e}.</equation>

---

**2015年第19题 | 解答题 | 10分**

19. (本题满分10分)

I. 设函数 u(x), v(x)可导，利用导数定义证明<equation>[ u ( x ) v ( x ) ]^{\prime}=u^{\prime} ( x ) v ( x )+u ( x ) v^{\prime} ( x )</equation>；

II. 设函数<equation>u_{1} ( x ) , u_{2} ( x ) , \cdots , u_{n} ( x )</equation>可导，<equation>f ( x )=u_{1} ( x ) u_{2} ( x ) \cdots u_{n} ( x )</equation>，写出 f(x)的求导公

**答案:**(19) （I）证明略；（Ⅱ）<equation>[ f ( x ) ]^{\prime} = \sum_{i=1}^{n} \left[ u_{i}^{\prime} ( x ) \prod_{j \neq i} u_{j} ( x ) \right].</equation>

**解析:**（I）（法一）由导数的定义知，<equation>\begin{aligned} [ u (x) v (x) ] ^ {\prime} &= \lim _ {h \rightarrow 0} \frac {u (x + h) v (x + h) - u (x) v (x)}{h} \\ &= \lim _ {h \rightarrow 0} \frac {u (x + h) v (x + h) - u (x) v (x + h) + u (x) v (x + h) - u (x) v (x)}{h} \\ &= \lim _ {h \rightarrow 0} \frac {u (x + h) - u (x)}{h} \cdot v (x + h) + \lim _ {h \rightarrow 0} u (x) \cdot \frac {v (x + h) - v (x)}{h} \\ \underline {{= \frac {u (x) , v (x) \text {均 可 导}}{2}}} u ^ {\prime} (x) v (x) + u (x) v ^ {\prime} (x). \end{aligned}</equation>（法二）由导数的定义知，<equation>\begin{aligned} [ u (x) v (x) ] ^ {\prime} &= \lim _ {h \rightarrow 0} \frac {u (x + h) v (x + h) - u (x) v (x)}{h} \\ &= \lim _ {h \rightarrow 0} \frac {u (x + h) v (x + h) - u (x + h) v (x) + u (x + h) v (x) - u (x) v (x)}{h} \\ &= \lim _ {h \rightarrow 0} u (x + h) \cdot \frac {v (x + h) - v (x)}{h} + \lim _ {h \rightarrow 0} \frac {u (x + h) - u (x)}{h} \cdot v (x) \\ \underline {{u (x), v (x) \text {均 可 导}}} u (x) v ^ {\prime} (x) + u ^ {\prime} (x) v (x). \end{aligned}</equation>（Ⅱ）由第（Ⅰ）问知，<equation>\begin{array}{l} [ f (x) ] ^ {\prime} = \left\{u _ {1} (x) \left[ u _ {2} (x) \dots u _ {n} (x) \right] \right\} ^ {\prime} \\ = u _ {1} ^ {\prime} (x) u _ {2} (x) \dots u _ {n} (x) + u _ {1} (x) \left[ u _ {2} (x) \dots u _ {n} (x) \right] ^ {\prime} \\ = u _ {1} ^ {\prime} (x) u _ {2} (x) \dots u _ {n} (x) + u _ {1} (x) \left\{u _ {2} (x) \cdot \left[ u _ {3} (x) \dots u _ {n} (x) \right] \right\} ^ {\prime} \\ = u _ {1} ^ {\prime} (x) u _ {2} (x) \dots u _ {n} (x) + u _ {1} (x) \left\{u _ {2} ^ {\prime} (x) u _ {3} (x) \dots u _ {n} (x) + u _ {2} (x) \left[ u _ {3} (x) \dots u _ {n} (x) \right] ^ {\prime} \right\} \\ = u _ {1} ^ {\prime} (x) u _ {2} (x) \dots u _ {n} (x) + u _ {1} (x) u _ {2} ^ {\prime} (x) u _ {3} (x) \dots u _ {n} (x) + u _ {1} (x) u _ {2} (x) \left[ u _ {3} (x) \dots u _ {n} (x) \right] ^ {\prime} \\ = \dots \\ = u _ {1} ^ {\prime} (x) u _ {2} (x) \dots u _ {n} (x) + u _ {1} (x) u _ {2} ^ {\prime} (x) \dots u _ {n} (x) + \dots + u _ {1} (x) u _ {2} (x) \dots u _ {n} ^ {\prime} (x) \\ = \sum_ {i = 1} ^ {n} \left[ u _ {i} ^ {\prime} (x) \prod_ {\substack {j \neq i, \\ 1 \leq j \leq n}} u _ {j} (x) \right]. \\ \end{array}</equation>

---

**2011年第2题 | 选择题 | 4分 | 答案: B**

2. 设函数 f(x)在 x=0处可导，且 f(0)=0，则<equation>\lim_{x\rightarrow 0}\frac{x^{2}f(x)-2f(x^{3})}{x^{3}}=</equation>(    )

A.<equation>-2f^{\prime}(0)</equation>B.<equation>-f^{\prime}(0)</equation>C.<equation>f^{\prime}(0)</equation>D. 0

答案: B

**解析:**解 （法一）利用导数的定义来求极限.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {x ^ {2} f (x) - 2 f \left(x ^ {3}\right)}{x ^ {3}} &= \lim _ {x \rightarrow 0} \left[ \frac {f (x)}{x} - \frac {2 f \left(x ^ {3}\right)}{x ^ {3}} \right] \xlongequal {f (0) = 0} \lim _ {x \rightarrow 0} \left[ \frac {f (x) - f (0)}{x - 0} - 2 \cdot \frac {f \left(x ^ {3}\right) - f (0)}{x ^ {3} - 0} \right] \\ &= \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0} - 2 \lim _ {x \rightarrow 0} \frac {f \left(x ^ {3}\right) - f (0)}{x ^ {3} - 0} = f ^ {\prime} (0) - 2 f ^ {\prime} (0) = - f ^ {\prime} (0). \end{aligned}</equation>应选B.

（法二）分别写出<equation>f(x)</equation>与<equation>f(x^{3})</equation>在<equation>x = 0</equation>处的一阶泰勒公式.<equation>f (x) = f (0) + f ^ {\prime} (0) x + o (x) \stackrel {f (0) = 0} {=} f ^ {\prime} (0) x + o (x),</equation><equation>f \left(x ^ {3}\right) = f (0) + f ^ {\prime} (0) x ^ {3} + o \left(x ^ {3}\right) \stackrel {f (0) = 0} {=} f ^ {\prime} (0) x ^ {3} + o \left(x ^ {3}\right).</equation>代入所求极限得<equation>\lim _ {x \rightarrow 0} \frac {x ^ {2} f (x) - 2 f \left(x ^ {3}\right)}{x ^ {3}} = \lim _ {x \rightarrow 0} \frac {f ^ {\prime} (0) x ^ {3} - 2 f ^ {\prime} (0) x ^ {3} + o \left(x ^ {3}\right)}{x ^ {3}} = - f ^ {\prime} (0).</equation>应选B.

---


