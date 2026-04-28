# 数学三

## 高等数学

### 一元函数积分学

#### 定积分的概念与性质

**2022年第4题 | 选择题 | 5分 | 答案: A**

4. 若<equation>I_{1}=\int_{0}^{1}\frac{x}{2(1+\cos x)}\mathrm{d}x,I_{2}=\int_{0}^{1}\frac{\ln(1+x)}{1+\cos x}\mathrm{d}x,I_{3}=\int_{0}^{1}\frac{2x}{1+\sin x}\mathrm{d}x</equation>，则（    )

A.<equation>I_{1}<I_{2}<I_{3}</equation>B.<equation>I_{2}<I_{1}<I_{3}</equation>C.<equation>I_{1}<I_{3}<I_{2}</equation>D.<equation>I_{3}<I_{2}<I_{1}</equation>

答案: A

**解析:**解 通过观察可发现，要比较<equation>I_{1}</equation>与<equation>I_{2}</equation>的大小，只需比较<equation>\frac{x}{2}</equation>与<equation>\ln(1+x)</equation>的大小.

令<equation>f(x)=\ln(1+x)-\frac{x}{2}</equation>，则<equation>f(0)=0</equation><equation>f^{\prime}(x)=\frac{1}{1+x}-\frac{1}{2}</equation>当<equation>x\in(0,1)</equation>时，<equation>f^{\prime}(x)>0</equation><equation>f(x)</equation>单调增加，从而<equation>f(x)>f(0)=0</equation>即<equation>\ln(1+x)>\frac{x}{2},\frac{\ln(1+x)}{1+\cos x}>\frac{x}{2(1+\cos x)}</equation>因此，<equation>I_{2}>I_{1}</equation>.

此外，同样的方法不难证明在(0,1)内，<equation>\ln(1+x)<x.</equation>另一方面，由于在(0,1)内，<equation>0<\sin x,\cos x<1,1<1+\sin x<2</equation>故<equation>I_{3}</equation>的被积函数<equation>\frac{2x}{1+\sin x} >x.</equation>结合<equation>\ln(1+x)<x</equation>可得，<equation>\frac{\ln(1+x)}{1+\cos x}<\frac{x}{1+\cos x}<x.</equation>于是，<equation>\frac{2x}{1+\sin x}>x>\frac{\ln(1+x)}{1+\cos x}.</equation>因此，<equation>I_{3}>I_{2}.</equation>综上所述，应选A.

---

**2018年第3题 | 选择题 | 4分 | 答案: C**

3. 设<equation>M=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{(1+x)^{2}}{1+x^{2}}\mathrm{d}x,N=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{1+x}{\mathrm{e}^{x}}\mathrm{d}x,K=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}(1+\sqrt{\cos x})\mathrm{d}x</equation>，则（    )

A. M > N > K B. M > K > N C. K > M > N D. K > N > M

答案: C

**解析:**分别计算 M,N,K.

由于<equation>\frac{2x}{1+x^{2}}</equation>是奇函数，故<equation>\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{2x}{1+x^{2}}\mathrm{d}x=0.</equation>于是，<equation>M = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {(1 + x) ^ {2}}{1 + x ^ {2}} \mathrm {d} x = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {1 + x ^ {2} + 2 x}{1 + x ^ {2}} \mathrm {d} x \frac {\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {2 x}{1 + x ^ {2}} \mathrm {d} x = 0}{\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \mathrm {d} x = \pi}.</equation>注意到当<equation>x\neq 0</equation>时，<equation>\mathrm{e}^{x}>1+x</equation>.于是，在<equation>\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>上，<equation>\frac{1+x}{e^{x}}\leqslant 1</equation>且等号仅在<equation>x=0</equation>处成立.<equation>N = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {1 + x}{\mathrm {e} ^ {x}} \mathrm {d} x < \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \mathrm {d} x = \pi .</equation>由于<equation>\sqrt{\cos x}</equation>是偶函数，且当 x<equation>\in\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>时，<equation>\cos x\geqslant0</equation>且等号仅在端点处成立，故<equation>\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\sqrt{\cos x}\mathrm{d}x=2\int_{0}^{\frac{\pi}{2}}\sqrt{\cos x}\mathrm{d}x>0.</equation>于是，<equation>K = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \left(1 + \sqrt {\cos x}\right) \mathrm {d} x = \pi + \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \sqrt {\cos x} \mathrm {d} x > \pi .</equation>综上所述，<equation>K > M > N</equation>应选C.

---

**2017年第17题 | 解答题 | 10分**

17. (本题满分10分)<equation>\text {求} \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n ^ {2}} \ln \left(1 + \frac {k}{n}\right)</equation>

**解析:**解 根据定积分的定义，提出因子<equation>\frac{1}{n}</equation>，可得<equation>\begin{array}{l} \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n ^ {2}} \ln \left(1 + \frac {k}{n}\right) = \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n} \ln \left(1 + \frac {k}{n}\right) \cdot \frac {1}{n} = \int_ {0} ^ {1} x \ln (1 + x) d x \\ = \frac {1}{2} \int_ {0} ^ {1} \ln (1 + x) d \left(x ^ {2}\right) \xlongequal {\text {分 部 积 分}} \frac {x ^ {2}}{2} \ln (1 + x) \Bigg | _ {0} ^ {1} - \frac {1}{2} \int_ {0} ^ {1} \frac {x ^ {2}}{1 + x} d x \\ = \frac {\ln 2}{2} - \frac {1}{2} \int_ {0} ^ {1} \frac {x ^ {2} - 1 + 1}{1 + x} d x = \frac {\ln 2}{2} - \frac {1}{2} \int_ {0} ^ {1} \left(x - 1 + \frac {1}{1 + x}\right) d x \\ = \frac {\ln 2}{2} - \frac {1}{2} \left[ \frac {x ^ {2}}{2} - x + \ln (1 + x) \right] \Bigg | _ {0} ^ {1} = \frac {1}{4}. \\ \end{array}</equation>因此，原极限<equation>= \frac{1}{4}.</equation>

---

**2016年第10题 | 填空题 | 4分**

<equation>0. \mathrm {极 限} \lim _ {n \rightarrow \infty} \frac {1}{n ^ {2}} \left(\sin \frac {1}{n} + 2 \sin \frac {2}{n} + \dots + n \sin \frac {n}{n}\right) = \underline {{}}</equation>

**答案:**## sin 1-cos 1.

**解析:**解 将原表达式作恒等变形，得<equation>\frac {1}{n ^ {2}} \left(\sin \frac {1}{n} + 2 \sin \frac {2}{n} + \dots + n \sin \frac {n}{n}\right) = \frac {1}{n} \left(\frac {1}{n} \sin \frac {1}{n} + \frac {2}{n} \sin \frac {2}{n} + \dots + \frac {n}{n} \sin \frac {n}{n}\right).</equation>因此，<equation>\begin{array}{l} \lim _ {n \rightarrow \infty} \left(\frac {1}{n} \sum_ {i = 1} ^ {n} \frac {i}{n} \sin \frac {i}{n}\right) = \int_ {0} ^ {1} x \sin x d x = \int_ {0} ^ {1} x d (- \cos x) \\ = - x \cos x \left| _ {0} ^ {1} + \int_ {0} ^ {1} \cos x d x = \sin 1 - \cos 1. \right. \\ \end{array}</equation>

---

**2014年第19题 | 解答题 | 10分**

19. (本题满分10分)

设函数 f(x), g(x)在区间 [a,b]上连续，且 f(x)单调增加，<equation>0 \leqslant g ( x ) \leqslant1</equation>证明：

I.<equation>0 \leqslant\int_{a}^{x} g ( t ) \mathrm{d} t \leqslant x-a,x \in[a,b]</equation>II.<equation>\int_{a}^{a+\int_{a}^{b} g ( t ) \mathrm{d} t} f ( x ) \mathrm{d} x \leqslant\int_{a}^{b} f ( x ) g ( x ) \mathrm{d} x.</equation>

**答案:**（19）（I）证明略；

（Ⅱ）证明略.

**解析:**证（I）由于在<equation>[a,b]</equation>上，<equation>0\leqslant g(x)\leqslant 1</equation>，故<equation>0 = \int_ {a} ^ {x} 0 \mathrm {d} t \leqslant \int_ {a} ^ {x} g (t) \mathrm {d} t \leqslant \int_ {a} ^ {x} 1 \mathrm {d} t = x - a.</equation>（Ⅱ）（法一）构造辅助函数<equation>F ( u )=\int_{a}^{u} f ( x ) g ( x ) \mathrm{d} x-\int_{a}^{a+\int_{a}^{u} g ( t ) \mathrm{d} t} f ( x ) \mathrm{d} x, u \in[ a, b ],</equation>则第（Ⅱ）问中的不等式等价于<equation>F ( b ) \geqslant0.</equation>由于<equation>F ( a )=0</equation>故若能证明<equation>F^{\prime} ( u ) \geqslant0</equation>则由 F(u)在[a,b]上单调增加可推出<equation>F ( b ) \geqslant0.</equation>计算<equation>F^{\prime}(u).</equation><equation>F ^ {\prime} (u) = f (u) g (u) - f \left(a + \int_ {a} ^ {u} g (t) \mathrm {d} t\right) g (u) = g (u) \left[ f (u) - f \left(a + \int_ {a} ^ {u} g (t) \mathrm {d} t\right) \right].</equation>由第（I）问知，<equation>0 \leqslant \int_{a}^{u} g ( t ) \mathrm{d} t \leqslant u - a</equation>，故<equation>a \leqslant a + \int_{a}^{u} g ( t ) \mathrm{d} t \leqslant u.</equation>于是，由<equation>f ( x )</equation>在<equation>[ a,b]</equation>上单调增加可知，<equation>f (u) - f \left(a + \int_ {a} ^ {u} g (t) \mathrm {d} t\right) \geqslant 0.</equation>从而<equation>F^{\prime}(u)\geqslant 0</equation>，故<equation>F(u)</equation>在<equation>[a,b]</equation>上单调增加.

因此，<equation>F ( b ) \geqslant F ( a ) = 0</equation>，原不等式成立.

（法二）在下面的证明中，我们将用到积分中值定理的一个一般形式.

若<equation>f ( x )</equation>,<equation>g ( x )</equation>在<equation>[ a,b]</equation>上连续，且<equation>g ( x )</equation>在<equation>[ a,b]</equation>上不变号，则<equation>\int_ {a} ^ {b} f (x) g (x) \mathrm {d} x = f (\xi) \int_ {a} ^ {b} g (x) \mathrm {d} x,</equation>其中<equation>\xi\in[a,b].</equation>记<equation>D=\int_{a}^{b} f ( x ) g ( x ) \mathrm{d} x-\int_{a}^{a+\int_{a}^{b} g ( t ) \mathrm{d} t} f ( x ) \mathrm{d} x.</equation>我们证明<equation>D \geqslant 0</equation>注意到<equation>a+\int_{a}^{b} g ( t ) \mathrm{d} t \in[ a,b]</equation>，故<equation>\begin{aligned} D &= \int_ {a} ^ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} [ f (x) g (x) - f (x) ] \mathrm {d} x + \int_ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} ^ {b} f (x) g (x) \mathrm {d} x \\ &= \int_ {a} ^ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} f (x) [ g (x) - 1 ] \mathrm {d} x + \int_ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} ^ {b} f (x) g (x) \mathrm {d} x. \end{aligned}</equation>由于<equation>0 \leqslant g(x) \leqslant 1</equation>，故<equation>g(x) - 1</equation>在<equation>[a,b]</equation>上不变号.由积分中值定理可得<equation>D = f \left(\xi_ {1}\right) \int_ {a} ^ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} [ g (x) - 1 ] \mathrm {d} x + f \left(\xi_ {2}\right) \int_ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} ^ {b} g (x) \mathrm {d} x,</equation>其中，<equation>\xi_{1}\in \left[ a,a + \int_{a}^{b}g(t)\mathrm{d}t\right],\xi_{2}\in \left[ a + \int_{a}^{b}g(t)\mathrm{d}t,b\right].</equation>由于<equation>f(x)</equation>在<equation>[a,b]</equation>上单调增加，故<equation>f(\xi_{1})\leqslant f(\xi_{2})</equation>，从而<equation>\begin{array}{l} D \geqslant f \left(\xi_ {1}\right) \left\{\int_ {a} ^ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} [ g (x) - 1 ] \mathrm {d} x + \int_ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} ^ {b} g (x) \mathrm {d} x \right\} = f \left(\xi_ {1}\right) \left[ \int_ {a} ^ {b} g (x) \mathrm {d} x - \int_ {a} ^ {a + \int_ {a} ^ {b} g (t) \mathrm {d} t} 1 \mathrm {d} x \right] \\ = f \left(\xi_ {1}\right) \left[ \int_ {a} ^ {b} g (x) \mathrm {d} x - \int_ {a} ^ {b} g (t) \mathrm {d} t \right] = 0. \\ \end{array}</equation>因此，<equation>D\geqslant 0</equation>，故原不等式得证.

---

**2010年第18题 | 解答题 | 10分**

18. (本题满分10分)

18. (本题满分10分)

I. 比较<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>与<equation>\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t</equation>（ n=1,2，<equation>\cdots</equation>）的大小，说明理由；

II. 记<equation>u_{n}=\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>（ n=1,2，<equation>\cdots</equation>），求极限<equation>\lim_{n\to\infty}u_{n}.</equation>

**答案:**(18) （I）<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t<\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t(n=1,2,\dots),</equation>，理由略；

（Ⅱ）<equation>\lim_{n\to \infty}u_{n}=0.</equation>

**解析:**解（I）在（0,1]上，<equation>\mid \ln t\mid</equation><equation>\ln(1+t)</equation>与 t均非负，故比较<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>与<equation>\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t(n=1,2,\cdots)</equation>的大小，只需比较<equation>\ln(1+t)</equation>与 t的大小.

考虑<equation>f(t)=\ln(1+t)-t</equation>考虑<equation>f ( t )=\ln( 1+t)-t.</equation><equation>f ^ {\prime} (t) = \frac {1}{1 + t} - 1.</equation>当<equation>t\in (0,1]</equation>时，<equation>f^{\prime}(t) < 0,f(t)\leqslant f(0) = 0.</equation>因此，当<equation>t\in [0,1]</equation>时，<equation>\ln (1 + t)\leqslant t.</equation>由于两被积函数仅在<equation>t = 1</equation>处相等，故<equation>\int_ {0} ^ {1} | \ln t | [ \ln (1 + t) ] ^ {n} \mathrm {d} t < \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t (n = 1, 2, \dots).</equation>（Ⅱ）（法一）由第（I）问知，<equation>0 < u_{n} < \int_{0}^{1} t^{n}|\ln t|\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {0} ^ {1} t ^ {n} \mid \ln t \mid \mathrm {d} t &= \frac {- 1}{n + 1} \int_ {0} ^ {1} \ln t \mathrm {d} \left(t ^ {n + 1}\right) = \frac {- 1}{n + 1} \left(t ^ {n + 1} \ln t \mid_ {0} ^ {1} - \int_ {0} ^ {1} t ^ {n + 1} \cdot \frac {1}{t} \mathrm {d} t\right) \\ \frac {\lim _ {t \rightarrow 0 ^ {+}} t ^ {n + 1} \ln t = 0}{\overline {{\quad}}} \frac {1}{n + 1} \int_ {0} ^ {1} t ^ {n} \mathrm {d} t &= \frac {1}{(n + 1) ^ {2}}. \end{aligned}</equation>因此，<equation>\lim _ {n \rightarrow \infty} \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t = \lim _ {n \rightarrow \infty} \frac {1}{(n + 1) ^ {2}} = 0.</equation>由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>（法二）由第（I）问知，<equation>0 < u_{n} < \int_{0}^{1} t^{n}|\ln t|\mathrm{d}t.</equation>又因为<equation>\lim_{t\to 0^{+}}t\ln t = 0</equation>，所以存在<equation>M > 0</equation>，使得对任意的<equation>t\in (0,1]</equation>，有<equation>t|\ln t|\leqslant M</equation>，从而<equation>0 < u _ {n} < \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t \leqslant M \int_ {0} ^ {1} t ^ {n - 1} \mathrm {d} t = \frac {M}{n}.</equation>由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>（法三）由于<equation>t\in[0,1]</equation>时，<equation>\ln(1 + t)\leqslant \ln 2 < 1</equation>，故<equation>u_{n}\leqslant (\ln 2)^{n}\int_{0}^{1}|\ln t|\mathrm{d}t.</equation>计算<equation>\int_{0}^{1}|\ln t| \mathrm{d} t</equation>得，<equation>\int_ {0} ^ {1} | \ln t | \mathrm {d} t = - \int_ {0} ^ {1} \ln t \mathrm {d} t = - \left(t \ln t \left| _ {0} ^ {1} - \int_ {0} ^ {1} 1 \mathrm {d} t\right)\right) \xlongequal {\lim _ {t \rightarrow 0 ^ {+}} t \ln t = 0} 1.</equation>从而<equation>0 < u_{n}\leqslant (\ln 2)^{n}</equation>因为<equation>\lim_{n\to \infty}(\ln 2)^n = 0</equation>，所以由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>

---


### 常微分方程与差分方程
#### 一阶非齐次线性微分方程

**2025年第13题 | 填空题 | 5分**

13. 微分方程<equation>x y^{\prime}-y+x^{2} \mathrm{e}^{x}=0</equation>满足条件<equation>y(1)=- \mathrm{e}</equation>的解为 y=___

**答案:**## xe<equation>^x</equation>.

**解析:**解 整理原方程可得<equation>y^{\prime}-\frac{y}{x}=-x\mathrm{e}^{x}.</equation>由一阶非齐次线性微分方程的通解公式可得<equation>y=\mathrm{e}^{\int \frac{1}{x}\mathrm{d}x}\left[\int(-x\mathrm{e}^{x})\cdot\mathrm{e}^{\int(-\frac{1}{x})\mathrm{d}x}\mathrm{d}x+C\right]=\mid x\mid\left[\int(-x\mathrm{e}^{x})\cdot\frac{1}{\mid x\mid}\mathrm{d}x+C\right]</equation><equation>=-x\int\mathrm{e}^{x}\mathrm{d}x+C\mid x\mid=-x\mathrm{e}^{x}+C\mid x\mid.</equation>将 y（1）=-e代入<equation>y=-x\mathrm{e}^{x}+C\left| x\right|</equation>可得<equation>-\mathrm{e}=-\mathrm{e}+C</equation>，解得 C=0.因此，<equation>y=-x\mathrm{e}^{x}.</equation>

---

**2022年第17题 | 解答题 | 10分**

17. (本题满分10分）

设函数 y(x）是微分方程<equation>y^{\prime}+\frac{1}{2\sqrt{x}} y=2+\sqrt{x}</equation>满足条件 y(1）=3的解，求曲线 y=y(x）的渐近线.

**答案:**y=2x为曲线 y=2x+<equation>\mathrm{e}^{1-\sqrt{x}}</equation>的斜渐近线，也是唯一的渐近线.

**解析:**根据求解公式，<equation>y = \mathrm {e} ^ {- \int \frac {1}{2 \sqrt {x}} \mathrm {d} x} \left[ \int (2 + \sqrt {x}) \mathrm {e} ^ {\int \frac {1}{2 \sqrt {x}} \mathrm {d} x} \mathrm {d} x + C _ {0} \right] = \mathrm {e} ^ {- \sqrt {x}} \left[ \int (2 + \sqrt {x}) \mathrm {e} ^ {\sqrt {x}} \mathrm {d} x + C _ {0} \right].</equation>下面计算<equation>\int(2+\sqrt{x})\mathrm{e}^{\sqrt{x}}\mathrm{d}x.</equation>令<equation>u=\sqrt{x}</equation>，则<equation>x=u^{2}</equation>，<equation>\mathrm{d} x=2 u \mathrm{d} u.</equation><equation>\begin{aligned} \int (2 + \sqrt {x}) \mathrm {e} ^ {\sqrt {x}} \mathrm {d} x \xlongequal {u = \sqrt {x}} 2 \int (2 + u) u \mathrm {e} ^ {u} \mathrm {d} u &= 2 \left(\int u ^ {2} \mathrm {e} ^ {u} \mathrm {d} u + \int 2 u \mathrm {e} ^ {u} \mathrm {d} u\right) \\ &= 2 \left[ \int u ^ {2} \mathrm {d} \left(\mathrm {e} ^ {u}\right) + \int 2 u \mathrm {e} ^ {u} \mathrm {d} u \right] = 2 \left(u ^ {2} \mathrm {e} ^ {u} - \int 2 u \mathrm {e} ^ {u} \mathrm {d} u + \int 2 u \mathrm {e} ^ {u} \mathrm {d} u\right) \\ &= 2 u ^ {2} \mathrm {e} ^ {u} + C _ {1} = 2 x \mathrm {e} ^ {\sqrt {x}} + C _ {1}. \end{aligned}</equation>将该结果代入（1）式，可得<equation>y = \mathrm {e} ^ {- \sqrt {x}} \left(2 x \mathrm {e} ^ {\sqrt {x}} + C\right) = 2 x + C \mathrm {e} ^ {- \sqrt {x}},</equation>其中 C为待定常数.代入<equation>y ( 1 )=3</equation>，可得<equation>3=2+C\cdot\mathrm{e}^{-1}</equation>，解得<equation>C=\mathrm{e}.</equation>因此，<equation>y ( x ) = 2 x + \mathrm {e} ^ {1 - \sqrt {x}} , x \in ( 0, + \infty) .</equation>由于函数<equation>y(x)=2 x+\mathrm{e}^{1-\sqrt{x}}</equation>在（0，<equation>+\infty</equation>）内连续，且<equation>\lim_{x\to 0^{+}}y(x)=\mathrm{e}</equation>，故曲线<equation>y=2 x+\mathrm{e}^{1-\sqrt{x}}</equation>没有铅直渐近线.

又因为<equation>\lim_{x\to +\infty}y(x) = \lim_{x\to +\infty}\left(2x + \mathrm{e}^{1 - \sqrt{x}}\right) = +\infty</equation>，所以曲线<equation>y = 2x + \mathrm{e}^{1 - \sqrt{x}}</equation>没有水平渐近线.

下面计算斜渐近线.<equation>\lim _ {x \rightarrow + \infty} \frac {y (x)}{x} = \lim _ {x \rightarrow + \infty} \frac {2 x + \mathrm {e} ^ {1 - \sqrt {x}}}{x} = 2,</equation><equation>\lim _ {x \rightarrow + \infty} [ y (x) - 2 x ] = \lim _ {x \rightarrow + \infty} \mathrm {e} ^ {1 - \sqrt {x}} = 0.</equation>因此，<equation>y=2x</equation>为曲线<equation>y=2x+\mathrm{e}^{1-\sqrt{x}}</equation>的斜渐近线，也是唯一的渐近线.

---

**2019年第17题 | 解答题 | 10分**

17. (本题满分10分)

设函数 y(x)是微分方程<equation>y^{\prime}-xy=\frac{1}{2\sqrt{x}} \mathrm{e}^{\frac{x^{2}}{2}}</equation>满足条件 y(1)<equation>=\sqrt{\mathrm{e}}</equation>的特解.

I. 求 y(x);

II. 设平面区域 D = {(x,y) | 1≤x≤2,0≤y≤y(x)}，求 D绕 x轴旋转所得旋转体的体积.

**答案:**(I)<equation>y(x)=\sqrt{x}\mathrm{e}^{\frac{x^{2}}{2}}</equation>; (II)<equation>\frac{1}{2}\pi(\mathrm{e}^{4}-\mathrm{e}).</equation>

**解析:**（I）由一阶非齐次线性微分方程的求解公式可得，<equation>\begin{aligned} y &= \mathrm {e} ^ {\int x \mathrm {d} x} \left[ \int \frac {1}{2 \sqrt {x}} \cdot \mathrm {e} ^ {\frac {x ^ {2}}{2}} \cdot \mathrm {e} ^ {\int (- x) \mathrm {d} x} \mathrm {d} x + C \right] = \mathrm {e} ^ {\frac {x ^ {2}}{2}} \left(\int \frac {1}{2 \sqrt {x}} \cdot \mathrm {e} ^ {\frac {x ^ {2}}{2}} \cdot \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \mathrm {d} x + C\right) \\ &= \mathrm {e} ^ {\frac {x ^ {2}}{2}} \left(\int \frac {1}{2 \sqrt {x}} \mathrm {d} x + C\right) = \sqrt {x} \mathrm {e} ^ {\frac {x ^ {2}}{2}} + C \mathrm {e} ^ {\frac {x ^ {2}}{2}}, \end{aligned}</equation>其中 C为待定常数.

代入<equation>x = 1,y(1) = \sqrt{\mathrm{e}}</equation>，可得<equation>\sqrt{\mathrm{e}} = \sqrt{\mathrm{e}} + C\sqrt{\mathrm{e}}.</equation>解得<equation>C = 0.</equation>因此，<equation>y ( x ) = \sqrt{x}\mathrm{e}^{\frac{x^{2}}{2}}.</equation>（Ⅱ）区域 D 如图所示.

根据旋转体的体积计算公式，<equation>\begin{aligned} V &= \pi \int_ {1} ^ {2} \left(\sqrt {x} \mathrm {e} ^ {\frac {x ^ {2}}{2}}\right) ^ {2} \mathrm {d} x = \pi \int_ {1} ^ {2} x \mathrm {e} ^ {x ^ {2}} \mathrm {d} x = \frac {1}{2} \pi \int_ {1} ^ {2} \mathrm {e} ^ {x ^ {2}} \mathrm {d} \left(x ^ {2}\right) \\ &= \frac {1}{2} \pi \mathrm {e} ^ {x ^ {2}} \Bigg | _ {1} ^ {2} = \frac {1}{2} \pi \left(\mathrm {e} ^ {4} - \mathrm {e}\right). \end{aligned}</equation>

---

**2014年第17题 | 解答题 | 10分**

17. (本题满分10分)

设函数 f(u)具有连续导数，且<equation>z=f(\mathrm{e}^{x}\cos y)</equation>满足<equation>\cos y\frac{\partial z}{\partial x}-\sin y\frac{\partial z}{\partial y}=(4z+\mathrm{e}^{x}\cos y)\mathrm{e}^{x}.</equation>若 f(0)=0，求 f(u)的表达式.

**答案:**<equation>(1 7) f (u) = \frac {1}{1 6} \mathrm {e} ^ {4 u} - \frac {1}{4} u - \frac {1}{1 6}.</equation>

**解析:**由链式法则知，<equation>\frac {\partial z}{\partial x} = f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right) \cdot \left(\mathrm {e} ^ {x} \cos y\right), \quad \frac {\partial z}{\partial y} = f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right) \cdot \left(- \mathrm {e} ^ {x} \sin y\right).</equation>代入题设等式中可得，<equation>\mathrm {e} ^ {x} \cos^ {2} y f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right) + \mathrm {e} ^ {x} \sin^ {2} y f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right) = \left(4 z + \mathrm {e} ^ {x} \cos y\right) \mathrm {e} ^ {x}.</equation>化简得<equation>f ^ {\prime} \left(\mathrm {e} ^ {x} \cos y\right) = 4 f \left(\mathrm {e} ^ {x} \cos y\right) + \mathrm {e} ^ {x} \cos y.</equation>令<equation>u=\mathrm{e}^{x}\cos y</equation>，得<equation>f ^ {\prime} (u) - 4 f (u) = u.</equation>此为一阶非齐次线性微分方程，由求解公式知，<equation>f (u) = \mathrm {e} ^ {- \int (- 4) \mathrm {d} u} \left[ \int u \mathrm {e} ^ {\int (- 4) \mathrm {d} u} \mathrm {d} u + C \right] = \mathrm {e} ^ {4 u} \left(\frac {\mathrm {e} ^ {- 4 u}}{- 4} u - \int \frac {\mathrm {e} ^ {- 4 u}}{- 4} \mathrm {d} u + C\right) = - \frac {1}{4} u - \frac {1}{1 6} + C \mathrm {e} ^ {4 u},</equation>其中 C为待定常数.

将<equation>f ( 0 )=0</equation>代入上式得<equation>C=\frac{1}{1 6}.</equation>因此，<equation>f (u) = \frac {1}{1 6} \mathrm {e} ^ {4 u} - \frac {1}{4} u - \frac {1}{1 6}.</equation>

---


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


#### 差分方程

**2021年第14题 | 填空题 | 5分**

14. 差分方程<equation>\Delta y_{t} = t</equation>的通解为<equation>y_{t} =</equation>___

**答案:**<equation>\frac{1}{2} t^{2}-\frac{1}{2} t+C</equation>，其中C为任意常数.

**解析:**解（法一）由于<equation>\Delta y_{t}=y_{t+1}-y_{t}</equation>，故<equation>\Delta y_{t}=t</equation>等价于<equation>y_{t+1}-y_{t}=t</equation>，为一阶常系数非齐次线性差分方程.

因为<equation>a = 1</equation>，所以<equation>\tilde{y}_t = C</equation>为<equation>y_{t + 1} - y_t = 0</equation>的通解.

又因为自由项为 t，所以可设<equation>y_{t}^{*} = t \left(B_{0} + B_{1} t\right).</equation>代回<equation>y_{t+1}-y_{t}=t</equation>可得<equation>B _ {0} (t + 1) + B _ {1} (t + 1) ^ {2} - B _ {0} t - B _ {1} t ^ {2} = 2 B _ {1} t + B _ {1} + B _ {0} = t.</equation>于是，<equation>B_{1}=\frac{1}{2}, B_{0}=-\frac{1}{2}.</equation>从而，<equation>y_{t}^{*}=\frac{1}{2} t^{2}-\frac{1}{2} t.</equation>因此，原方程的通解为<equation>y_{t}=\frac{1}{2} t^{2}-\frac{1}{2} t+C</equation>，其中C为任意常数.

（法二）由已知条件可知，<equation>y_{t + 1} - y_{t} = t.</equation>于是，<equation>y _ {t} - y _ {t - 1} = t - 1, \quad y _ {t - 1} - y _ {t - 2} = t - 2, \quad \dots , \quad y _ {2} - y _ {1} = 1.</equation>从而，<equation>y _ {t} = \left(y _ {t} - y _ {t - 1}\right) + \left(y _ {t - 1} - y _ {t - 2}\right) + \dots + \left(y _ {2} - y _ {1}\right) + y _ {1} = \frac {t (t - 1)}{2} + y _ {1}.</equation>由于<equation>y_{1}</equation>可以取任意常数，故<equation>y_{t}=\frac{t(t-1)}{2}+C=\frac{1}{2} t^{2}-\frac{1}{2} t+C</equation>，其中C为任意常数.

---

**2018年第11题 | 填空题 | 4分**

11. 差分方程<equation>\Delta^{2} y_{x}-y_{x}=5</equation>的通解为 ___

**答案:**<equation>y_{x}=C2^{x}-5</equation>，其中C为任意常数.

**解析:**解 由于<equation>\Delta^{2} y_{x}=\Delta y_{x+1}-\Delta y_{x}</equation>，故<equation>\Delta^{2} y_{x}=\Delta y_{x+1}-\Delta y_{x}=\left(y_{x+2}-y_{x+1}\right)-\left(y_{x+1}-y_{x}\right)=y_{x+2}-2y_{x+1}+y_{x}.</equation>由<equation>\Delta^{2} y_{x}-y_{x}=5</equation>可得，<equation>y_{x+2}-2y_{x+1}=5</equation>即<equation>y_{x+1}-2y_{x}=5.</equation>下面用两种方法解<equation>y_{x + 1} - 2y_{x} = 5.</equation>（法一）这是一个一阶非齐次线性差分方程.该方程对应的齐次差分方程的通解为<equation>\tilde{y}_{x}=C2^{x}</equation>其中C为任意常数.

设原方程的一个特解为<equation>y_{x}^{*} = k</equation>，代入原方程得 k-2k=5.解得 k=-5.于是，特解为<equation>y_{x}^{*} = -5.</equation>因此，原方程的通解为<equation>y_{x} = C2^{x} - 5</equation>其中 C为任意常数.

（法二）由<equation>y_{x+1}-2 y_{x}=5</equation>可得，<equation>y_{x+1}+5=2 \left( y_{x}+5 \right).</equation>于是，<equation>\left\{y_{x}+5\right\}_{x \in \mathbf{N}}</equation>是一个首项为<equation>y_{0}+5</equation>公比为2的等比数列.记<equation>C=y_{0}+5</equation>，可得<equation>y_{x}+5=C2^{x}</equation>即<equation>y_{x}=C2^{x}-5.</equation>由于<equation>y_{0}</equation>可取任意常数，故C为任意常数.

---

**2017年第10题 | 填空题 | 4分**

10. 差分方程<equation>y_{t+1}-2y_{t}=2^{t}</equation>的通解为<equation>y_{t}=</equation>___.

**答案:**<equation>\left(C + \frac{1}{2} t\right)2^{t}</equation>，其中C为任意常数.

**解析:**解<equation>y_{t+1}-2 y_{t}=2^{t}</equation>对应的齐次方程为<equation>y_{t+1}-2 y_{t}=0</equation>，其通解为<equation>\widetilde{y}_{t}=C2^{t}</equation>其中C为任意常数设原方程的一个特解为<equation>y_{t}^{*} = k t 2^{t}</equation>，代入原方程得<equation>k ( t+1 ) 2^{t+1}-2 k t 2^{t}=2^{t}</equation>解得<equation>k=\frac{1}{2}</equation>于是，特解为<equation>y_{t}^{*} = \frac{1}{2} t 2^{t}</equation>因此，原方程的通解为<equation>y_{t} = \left(C + \frac{1}{2} t\right) 2^{t}</equation>其中C为任意常数.

---


#### 二阶常系数非齐次线性微分方程

**2019年第3题 | 选择题 | 4分 | 答案: D**

3. 已知微分方程<equation>y^{\prime \prime}+ay^{\prime}+by=c\mathrm{e}^{x}</equation>的通解为<equation>y=(C_{1}+C_{2}x)\mathrm{e}^{-x}+\mathrm{e}^{x}</equation>，则 a,b,c依次为（    )

A. 1,0,1 B. 1,0,2 C. 2,1,3 D. 2,1,4

答案: D

**解析:**解 由原方程的通解形式可知，<equation>y = ( C_{1} + C_{2} x ) \mathrm{e}^{-x}</equation>是原方程对应的齐次线性微分方程的通解，故<equation>r=-1</equation>为该齐次方程的特征方程的二重根.于是，特征方程为<equation>( r+1 )^{2}=0</equation>即<equation>r^{2}+2 r+1=0.</equation>从而，<equation>a=2,b=1.</equation>由原方程的通解形式可知，<equation>y=\mathrm{e}^{x}</equation>是原方程的一个特解.将<equation>y=\mathrm{e}^{x}</equation>代入<equation>y^{\prime \prime}+2y^{\prime}+y=c\mathrm{e}^{x}</equation>可得，<equation>4\mathrm{e}^{x}=c\mathrm{e}^{x}.</equation>于是，<equation>c=4.</equation>因此，<equation>a=2,b=1,c=4.</equation>应选D.

---


#### 线性微分方程的解的结构

**2010年第2题 | 选择题 | 4分 | 答案: A**

2. 设<equation>y_{1}, y_{2}</equation>是一阶线性非齐次微分方程<equation>y^{\prime}+p(x)y=q(x)</equation>的两个特解，若常数<equation>\lambda,\mu</equation>使<equation>\lambda y_{1}+\mu y_{2}</equation>是该方程的解，<equation>\lambda y_{1}-\mu y_{2}</equation>是该方程对应的齐次方程的解，则（    )

A.<equation>\lambda=\frac{1}{2},\mu=\frac{1}{2}</equation>B.<equation>\lambda=-\frac{1}{2},\mu=-\frac{1}{2}</equation>C.<equation>\lambda=\frac{2}{3},\mu=\frac{1}{3}</equation>D.<equation>\lambda=\frac{2}{3},\mu=\frac{2}{3}</equation>

答案: A

**解析:**由题设知，<equation>y _ {1} ^ {\prime} + p (x) y _ {1} = q (x), \quad y _ {2} ^ {\prime} + p (x) y _ {2} = q (x).</equation>又由题设知，<equation>\lambda y_{1} + \mu y_{2}</equation>也是<equation>y^{\prime} + p(x)y = q(x)</equation>的解，故<equation>\left(\lambda y _ {1} + \mu y _ {2}\right) ^ {\prime} + p (x) \left(\lambda y _ {1} + \mu y _ {2}\right) = q (x).</equation>整理（1）式，得<equation>\lambda \left[ y _ {1} ^ {\prime} + p (x) y _ {1} \right] + \mu \left[ y _ {2} ^ {\prime} + p (x) y _ {2} \right] = q (x),</equation>即<equation>(\lambda +\mu)q(x) = q(x)</equation>. 由于<equation>q(x)\neq 0</equation>，故<equation>\lambda +\mu = 1.</equation>又由<equation>\lambda y_{1} - \mu y_{2}</equation>是<equation>y^{\prime} + p(x)y = 0</equation>的解知<equation>\left(\lambda y _ {1} - \mu y _ {2}\right) ^ {\prime} + p (x) \left(\lambda y _ {1} - \mu y _ {2}\right) = 0.</equation>整理（2）式，得<equation>\lambda \left[ y _ {1} ^ {\prime} + p (x) y _ {1} \right] - \mu \left[ y _ {2} ^ {\prime} + p (x) y _ {2} \right] = 0,</equation>即<equation>(\lambda -\mu)q(x) = 0.</equation>由于<equation>q(x)\neq 0</equation>，故<equation>\lambda -\mu = 0.</equation>联立<equation>\left\{ \begin{array}{l l} \lambda +\mu =1, \\ \lambda -\mu =0, \end{array} \right.</equation>解得<equation>\lambda =\frac{1}{2},\mu =\frac{1}{2}</equation>.应选A.

---


## 线性代数
### 线性方程组
### 矩阵的特征值和特征向量