#### 变限积分

**2024年第2题 | 选择题 | 5分 | 答案: B**

2. 设<equation>I=\int_{a}^{a+k\pi}|\sin x|\mathrm{d}x,k</equation>为整数，则 I的值（    ）

A. 只与 a有关 B. 只与 k有关 C. 与 a,k均有关 D. 与 a,k均无关

答案: B

**解析:**解（法一）由于<equation>|\sin (x + \pi)| = | - \sin x| = |\sin x|</equation>，故<equation>|\sin x|</equation>是周期为<equation>\pi</equation>的周期函数由分析中的结论（2）可知，<equation>I = \int_ {a} ^ {a + k \pi} | \sin x | \mathrm {d} x = k \int_ {0} ^ {\pi} | \sin x | \mathrm {d} x = k \int_ {0} ^ {\pi} \sin x \mathrm {d} x = 2 k.</equation>因此，<equation>I</equation>的值只与k有关，应选B.

（法二）我们先证明：<equation>\int_{a}^{a+k\pi}|\sin x|\mathrm{d}x=\int_{0}^{k\pi}|\sin x|\mathrm{d}x.</equation>记<equation>F ( a )=\int_{a}^{a+k\pi}|\sin x| \mathrm{d} x.</equation>考虑<equation>F^{\prime}(a).</equation><equation>\begin{aligned} F ^ {\prime} (a) &= \left(\int_ {a} ^ {a + k \pi} | \sin x | \mathrm {d} x\right) ^ {\prime} = | \sin (a + k \pi) | - | \sin a | \\ \underline {{\sin (x + k \pi) = (- 1) ^ {k} \sin x}} | (- 1) ^ {k} \sin a | - | \sin a | &= 0. \end{aligned}</equation>于是，<equation>F(a)</equation>是常函数，<equation>F(a)</equation>恒等于<equation>F(0)</equation>，即<equation>\int_{0}^{k\pi}|\sin x|\mathrm{d}x.</equation>由定积分的性质可得，<equation>I = \int_ {0} ^ {k \pi} | \sin x | \mathrm {d} x = \sum_ {i = 0} ^ {k - 1} \int_ {i \pi} ^ {(i + 1) \pi} | \sin x | \mathrm {d} x.</equation>由于<equation>\int_ {i \pi} ^ {(i + 1) \pi} | \sin x | \mathrm {d} x \xlongequal {t = x - i \pi} \int_ {0} ^ {\pi} | \sin (t + i \pi) | \mathrm {d} t = \int_ {0} ^ {\pi} \sin t \mathrm {d} t = 2,</equation>故由（1）式可得<equation>I = \sum_ {i = 0} ^ {k - 1} \int_ {i \pi} ^ {(i + 1) \pi} | \sin x | \mathrm {d} x = 2 k.</equation>因此，<equation>I</equation>的值只与k有关，应选B.

---

**2020年第3题 | 选择题 | 4分 | 答案: A**

3. 设奇函数 f(x)在<equation>(-\infty,+\infty)</equation>上具有连续导数，则（    )

A.<equation>\int_{0}^{x}[\cos f(t)+f^{\prime}(t)]\mathrm{d}t</equation>是奇函数 B.<equation>\int_{0}^{x}[\cos f(t)+f^{\prime}(t)]\mathrm{d}t</equation>是偶函数

C.<equation>\int_{0}^{x}[\cos f^{\prime}(t)+f(t)]\mathrm{d}t</equation>是奇函数 D.<equation>\int_{0}^{x}[\cos f^{\prime}(t)+f(t)]\mathrm{d}t</equation>是偶函数

答案: A

**解析:**解 由于 f(x)是奇函数，故<equation>\cos f(x)</equation>是偶函数，<equation>f^{\prime}(x)</equation>是偶函数，从而<equation>\cos f(x)+f^{\prime}(x)</equation>也是偶函数.<equation>F(x)=\int_{0}^{x}[\cos f(t)+f^{\prime}(t)]\mathrm{d}t</equation>是<equation>\cos f(x)+f^{\prime}(x)</equation>的一个原函数，且 F(0)=0.因此， F(x)是奇函数.应选A.

下面说明其余选项均不正确.

取<equation>f ( x )=x</equation>，则<equation>\cos f ( x )=\cos x,f^{\prime}(x)=1,\cos f^{\prime}(x)=\cos 1.</equation><equation>\int_{0}^{x}[\cos t+1]\mathrm{d} t=\sin x+x</equation>是奇函数，故选项B不正确.<equation>\int_{0}^{x}[\cos 1+t]\mathrm{d} t=\cos 1\cdot x+\frac{x^{2}}{2}</equation>既不是奇函数，也不是偶函数，故选项C、D不正确.

---

**2016年第18题 | 解答题 | 10分**

18. (本题满分10分）

设函数 f(x)连续，且满足<equation>\int_{0}^{x} f(x-t)\mathrm{d} t=\int_{0}^{x}(x-t)f(t)\mathrm{d} t+\mathrm{e}^{-x}-1</equation>求 f(x).

**答案:**<equation>f (x) = - \frac {\mathrm {e} ^ {- x} + \mathrm {e} ^ {x}}{2}.</equation>

**解析:**令 u=x-t，则<equation>\int_ {0} ^ {x} f (x - t) \mathrm {d} t \xlongequal {u = x - t} - \int_ {x} ^ {0} f (u) \mathrm {d} u = \int_ {0} ^ {x} f (u) \mathrm {d} u.</equation>另一方面，<equation>\int_ {0} ^ {x} (x - t) f (t) \mathrm {d} t = x \int_ {0} ^ {x} f (t) \mathrm {d} t - \int_ {0} ^ {x} t f (t) \mathrm {d} t.</equation>于是已知等式化为<equation>\int_ {0} ^ {x} f (u) \mathrm {d} u = x \int_ {0} ^ {x} f (t) \mathrm {d} t - \int_ {0} ^ {x} t f (t) \mathrm {d} t + \mathrm {e} ^ {- x} - 1.</equation>由于 f(x) 连续，故<equation>\int_{0}^{x} f(t)\mathrm{d}t</equation>可导.对上式两端关于 x求导，可得<equation>f (x) = \int_ {0} ^ {x} f (t) \mathrm {d} t + x f (x) - x f (x) - \mathrm {e} ^ {- x},</equation>即<equation>f (x) = \int_ {0} ^ {x} f (t) \mathrm {d} t - \mathrm {e} ^ {- x}.</equation>对（1）式两端关于 x求导，可得<equation>f ^ {\prime} (x) = f (x) + \mathrm {e} ^ {- x},</equation>即<equation>f^{\prime}(x) - f(x) = \mathrm{e}^{-x}</equation>.<equation>\begin{aligned} f (x) &= \mathrm {e} ^ {- \int (- 1) \mathrm {d} x} \left[ \int \mathrm {e} ^ {- x} \cdot \mathrm {e} ^ {\int (- 1) \mathrm {d} x} \mathrm {d} x + C \right] = \mathrm {e} ^ {x} \left(\int \mathrm {e} ^ {- x} \cdot \mathrm {e} ^ {- x} \mathrm {d} x + C\right) \\ &= \mathrm {e} ^ {x} \left(\int \mathrm {e} ^ {- 2 x} \mathrm {d} x + C\right) = \mathrm {e} ^ {x} \left(- \frac {1}{2} \mathrm {e} ^ {- 2 x} + C\right), \end{aligned}</equation>此为一阶非齐次线性微分方程.由求解公式可得，

其中 C为待定常数.

将 x=0代入（1）式可得，<equation>f(0)=-1</equation>.再将 x=0，<equation>f(0)=-1</equation>代入（2）式，可得<equation>-1=-\frac{1}{2}+C</equation>解得 C=-<equation>\frac{1}{2}</equation>.因此，<equation>f (x) = \mathrm {e} ^ {x} \left(- \frac {1}{2} \mathrm {e} ^ {- 2 x} - \frac {1}{2}\right) = - \frac {\mathrm {e} ^ {- x} + \mathrm {e} ^ {x}}{2}.</equation>

---

**2015年第10题 | 填空题 | 4分**

10. 设函数 f(x) 连续，<equation>\varphi(x)=\int_{0}^{x^{2}} x f(t) \mathrm{d} t</equation>. 若<equation>\varphi(1)=1, \varphi^{\prime}(1)=5</equation>，则 f(1) = ___.

**解析:**解 首先，由于在<equation>\int_0^{x^2} xf(t)\mathrm{d}t</equation>中，<equation>x</equation>不是积分变量，故可将<equation>x</equation>作为因子提出放在积分号外，即<equation>\varphi (x) = \int_ {0} ^ {x ^ {2}} x f (t) \mathrm {d} t = x \int_ {0} ^ {x ^ {2}} f (t) \mathrm {d} t.</equation>由求导的乘法法则和变限积分的求导公式可得<equation>\varphi^ {\prime} (x) = \int_ {0} ^ {x ^ {2}} f (t) \mathrm {d} t + x f \left(x ^ {2}\right) \cdot 2 x.</equation>由<equation>\varphi(1)=1</equation>可得<equation>\varphi(1)=\int_{0}^{1} f(t)\mathrm{d} t=1</equation>；由<equation>\varphi^{\prime}(1)=5</equation>可得<equation>\varphi^{\prime}(1)=\int_{0}^{1} f(t)\mathrm{d} t+2f(1)=5.</equation>因此，<equation>f(1)=\frac{\varphi^{\prime}(1)-\varphi(1)}{2}=2.</equation>

---

**2010年第9题 | 填空题 | 4分**

9. 设可导函数<equation>y=y(x)</equation>由方程<equation>\int_{0}^{x+y}\mathrm{e}^{-t^{2}}\mathrm{d}t=\int_{0}^{x}x\sin t^{2}\mathrm{d}t</equation>确定，则<equation>\left.\frac{\mathrm{d}y}{\mathrm{d}x}\right|_{x=0}=</equation>___.

**解析:**解 对方程<equation>\int_{0}^{x+y}\mathrm{e}^{-t^{2}}\mathrm{d}t=\int_{0}^{x}x\sin t^{2}\mathrm{d}t=x\int_{0}^{x}\sin t^{2}\mathrm{d}t</equation>两端关于 x求导得，<equation>\mathrm{e}^{-(x+y)^{2}}\cdot[1+y^{\prime}(x)]=\int_{0}^{x}\sin t^{2}\mathrm{d}t+x\sin x^{2}.</equation>将 x=0代入原方程得<equation>\int_{0}^{y}\mathrm{e}^{-t^{2}}\mathrm{d}t=0</equation>.由于<equation>\mathrm{e}^{-t^{2}}</equation>恒大于零，故 y=0.再将 x=0，y=0代入（1）式可知，<equation>1+y^{\prime}(0)=0</equation>.因此，<equation>\left.\frac{\mathrm{d}y}{\mathrm{d}x}\right|_{x=0}=y^{\prime}(0)=-1.</equation>

---

**2009年第3题 | 选择题 | 4分 | 答案: A**

3. 使不等式<equation>\int_{1}^{x} \frac{\sin t}{t}\mathrm{d}t > \ln x</equation>成立的 x 的范围是（    ）

A. (0,1) B.<equation>\left(1, \frac{\pi}{2}\right)</equation>C.<equation>\left(\frac{\pi}{2}, \pi\right)</equation>D.<equation>(\pi, +\infty)</equation>

答案: A

**解析:**解 令<equation>f ( x )=\int_{1}^{x}\frac{\sin t}{t}\mathrm{d} t-\ln x</equation>，则<equation>f ( 1 )=0. f ( x )</equation>的自然定义域为<equation>x > 0.</equation>计算<equation>f^{\prime}(x)</equation>得，<equation>f ^ {\prime} (x) = \frac {\sin x}{x} - \frac {1}{x} = \frac {\sin x - 1}{x} \leqslant 0,</equation>并且等号仅在<equation>x=2 n \pi+\frac{\pi}{2}</equation>（<equation>n</equation>为正整数）时成立.于是，<equation>f(x)</equation>是（0，<equation>+\infty</equation>）上的单调减少函数.

当 0 < x < 1时，<equation>f ( x ) > f ( 1 ) = 0</equation>；当 x > 1时，<equation>f ( x ) < f ( 1 ) = 0</equation>因此，使得<equation>f ( x ) > 0</equation>即<equation>\int_{1}^{x}\frac{\sin t}{t}\mathrm{d}t-\ln x>0</equation>的 x的范围是(0,1).应选A.

---

**2009年第4题 | 选择题 | 4分 | 答案: D**

4. 设函数 y=f(x)在区间[-1,3]上的图形如图所示，则函数<equation>F ( x )=\int_{0}^{x} f ( t ) \mathrm{d} t</equation>的图形为（    ）

A.

B.

C.

D.

答案: D

**解析:**解（法一）我们可以从<equation>f(x)</equation>出发具体分析<equation>F(x)</equation>的性质.

因为<equation>f ( x )</equation>分段连续，所以由变上限积分函数的性质可知，在<equation>[-1,0)</equation>，（0,2），（2,3]上，均有<equation>F^{\prime}(x)=f(x).</equation><equation>\textcircled{1}</equation>由于 f(x)在[-1,3]上有界且只有两个间断点，故 f(x)可积.又因为<equation>F(x)=\int_{0}^{x} f(t)\mathrm{d}t</equation>所以 F(x)连续.<equation>\textcircled{2}</equation>在<equation>[-1,0)</equation>上，<equation>f ( x ) > 0</equation>，故 F(x) 单调增加；在(0,1)上，<equation>f ( x ) < 0</equation>，故 F(x) 单调减少；在

(1,2)上，<equation>f ( x ) > 0</equation>，故<equation>F ( x )</equation>单调增加；在（2,3]上，<equation>f ( x ) = 0</equation>，故<equation>F ( x )</equation>为常函数.<equation>\textcircled{3} F ( 0 )=\int_{0}^{0} f ( t ) \mathrm{d} t=0.</equation>在<equation>[-1,1]</equation>上，<equation>F ( x )</equation>均小于等于零.<equation>\textcircled{4}</equation><equation>f(1) = 0, x = 1</equation>为<equation>F(x)</equation>的驻点及极小值点.

同时满足以上要求的图形只有选项D.应选D.

（法二）通过图形考察<equation>f(x)</equation>在<equation>[-1,0)</equation>上的性质，可知当<equation>x\in[-1,0)</equation>时，<equation>f(x)\equiv 1</equation>，故<equation>F (- 1) = \int_ {0} ^ {- 1} 1 \mathrm {d} x = - 1, \quad F (0) = \int_ {0} ^ {0} 1 \mathrm {d} x = 0,</equation>从而可排除选项A和选项C.

又由于 f(x)在[-1,3]上有界且只有两个间断点，f(x)在[-1,3]上可积，而 F(x) =<equation>\int_{0}^{x} f(t)\mathrm{d} t</equation>，故 F(x)必连续，从而可以排除选项B.

综上所述，应选D.

---


