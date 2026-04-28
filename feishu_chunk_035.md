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


