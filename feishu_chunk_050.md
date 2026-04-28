#### 导数与微分的计算

**2021年第12题 | 填空题 | 5分**

12. 设函数<equation>y=y(x)</equation>由参数方程<equation>\left\{ \begin{array}{l} x = 2 \mathrm {e} ^ {t} + t + 1, \\ y = 4 (t - 1) \mathrm {e} ^ {t} + t ^ {2} \end{array} \right.</equation>确定，则<equation>\left.\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\right|_{t=0}=</equation>___

**答案:**# 2 3.

**解析:**解 根据由参数方程确定的函数的导数计算公式，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {4 \mathrm {e} ^ {t} + 4 (t - 1) \mathrm {e} ^ {t} + 2 t}{2 \mathrm {e} ^ {t} + 1} = \frac {4 t \mathrm {e} ^ {t} + 2 t}{2 \mathrm {e} ^ {t} + 1} = 2 t.</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\mathrm {d} \left(\frac {\mathrm {d} y}{\mathrm {d} x}\right)}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {2}{2 \mathrm {e} ^ {t} + 1}.</equation>代入<equation>t = 0</equation>，可得<equation>\frac{\mathrm{d}^2y}{\mathrm{d}x^2}\bigg|_{t = 0} = \frac{2}{3}</equation>.

---

**2020年第10题 | 填空题 | 4分**

10. 设<equation>\left\{ \begin{array}{l l} x = \sqrt {t ^ {2} + 1}, \\ y = \ln \left(t + \sqrt {t ^ {2} + 1}\right), \end{array} \right. \quad \text {则} \left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {t = 1} = \underline {{}}.</equation>

**答案:**<equation>- \sqrt {2}.</equation>

**解析:**解 根据由参数方程确定的函数的求导公式，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {1 + \frac {t}{\sqrt {t ^ {2} + 1}}}{t + \sqrt {t ^ {2} + 1}} / \frac {t}{\sqrt {t ^ {2} + 1}} = \frac {1}{\sqrt {t ^ {2} + 1}} / \frac {t}{\sqrt {t ^ {2} + 1}} = \frac {1}{t}.</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\mathrm {d} \left(\frac {\mathrm {d} y}{\mathrm {d} x}\right)}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = - \frac {1}{t ^ {2}} / \frac {t}{\sqrt {t ^ {2} + 1}} = - \frac {\sqrt {t ^ {2} + 1}}{t ^ {3}}.</equation>代入<equation>t = 1</equation>，可得<equation>\frac{\mathrm{d}^2y}{\mathrm{d}x^2}\bigg|_{t = 1} = -\sqrt{2}</equation>.

---

**2017年第9题 | 填空题 | 4分**

9. 已知函数<equation>f ( x )=\frac{1}{1+x^{2}}</equation>，则<equation>f^{(3)}(0)=</equation>___

**解析:**解（法一）由泰勒公式<equation>\frac{1}{1+x}=1-x+x^{2}+o\left(x^{2}\right)\left(x\rightarrow 0\right)</equation>知，<equation>f (x) = \frac {1}{1 + x ^ {2}} = 1 - x ^ {2} + x ^ {4} + o \left(x ^ {4}\right) (x \rightarrow 0).</equation>再由泰勒公式的唯一性知，<equation>\frac{f^{(3)}(0)}{3!}=f(x)</equation>在0处的泰勒公式中<equation>x^{3}</equation>的系数=0，从而<equation>f^{(3)}(0)=0.</equation>（法二）<equation>f ( x )=\frac{1}{1+x^{2}}</equation>为偶函数，由偶函数的导函数为奇函数，而奇函数的导函数为偶函数知，<equation>f^{\prime}(x)</equation>为奇函数，<equation>f^{\prime\prime}(x)</equation>为偶函数，<equation>f^{(3)}(x)</equation>为奇函数，从而<equation>f^{(3)}(0)=0.</equation>（法三）<equation>f ^ {\prime} (x) = \left[ \left(1 + x ^ {2}\right) ^ {- 1} \right] ^ {\prime} = - 2 x \left(1 + x ^ {2}\right) ^ {- 2},</equation><equation>f ^ {\prime \prime} (x) = - 2 \left(1 + x ^ {2}\right) ^ {- 2} + 8 x ^ {2} \left(1 + x ^ {2}\right) ^ {- 3},</equation>注意这里不需要展开，因为只要求<equation>f^{(3)}(0).</equation><equation>f ^ {(3)} (x) = 8 x \left(1 + x ^ {2}\right) ^ {- 3} + 1 6 x \left(1 + x ^ {2}\right) ^ {- 3} + 8 x ^ {2} \left[ \left(1 + x ^ {2}\right) ^ {- 3} \right] ^ {\prime},</equation>从而<equation>f^{(3)}(0) = 0.</equation>

---

**2016年第12题 | 填空题 | 4分**

12. 设函数<equation>f(x)=\arctan x-\frac{x}{1+a x^{2}}</equation>，且<equation>f^{\prime\prime\prime}(0)=1</equation>，则 a=___

**答案:**# 1 2.

**解析:**解 应用泰勒公式，当<equation>x\to 0</equation>时，<equation>\arctan x = x - \frac{x^3}{3} + o(x^3),\frac{1}{1 + x} = 1 - x + o(x)</equation>，从而<equation>\frac {x}{1 + a x ^ {2}} = x \left[ 1 - a x ^ {2} + o \left(x ^ {2}\right) \right] = x - a x ^ {3} + o \left(x ^ {3}\right).</equation>于是，<equation>f (x) = \arctan x - \frac {x}{1 + a x ^ {2}} = \left(a - \frac {1}{3}\right) x ^ {3} + o \left(x ^ {3}\right) \quad (x \rightarrow 0).</equation>由泰勒公式的唯一性知，<equation>\frac {f ^ {\prime \prime \prime} (0)}{3 !} = a - \frac {1}{3}.</equation>又<equation>f^{\prime \prime \prime}(0) = 1</equation>，故<equation>a = \frac{1}{2}.</equation>

---

**2013年第9题 | 填空题 | 4分**

9. 设函数 y=f(x)由方程 y-x=<equation>\mathrm{e}^{x(1-y)}</equation>确定，则<equation>\lim_{n\to\infty}n\left[ f\left(\frac{1}{n}\right)-1\right]=\underline{___}</equation>

**解析:**解 将 x=0 代入原方程中得到<equation>f(0)=\mathrm{e}^{0}=1</equation>. 对方程 y-x=<equation>\mathrm{e}^{x(1-y)}</equation>两端关于 x求导，得到<equation>y^{\prime}-1=\mathrm{e}^{x(1-y)}(1-y-xy^{\prime}).</equation>将 x=0,y=1 代入上式得到<equation>y^{\prime}(0)=1</equation>，即<equation>f^{\prime}(0)=1</equation>，从而<equation>\lim _ {n \rightarrow \infty} n \left[ f \left(\frac {1}{n}\right) - 1 \right] = \lim _ {n \rightarrow \infty} \frac {f \left(\frac {1}{n}\right) - f (0)}{\frac {1}{n} - 0} = f ^ {\prime} (0) = 1.</equation>

---

**2013年第11题 | 填空题 | 4分**

11. 设<equation>\left\{ \begin{array}{l} x = \sin t, \\ y = t \sin t + \cos t \end{array} \right.</equation>（t为参数），则<equation>\left.\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}\right|_{t=\frac{\pi}{4}}=</equation>___

**解析:**<equation>\begin{array}{l} \left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {t = \frac {\pi}{4}} = \frac {1}{\cos \frac {\pi}{4}} = \sqrt {2}. \\ \end{array}</equation>

---

**2012年第2题 | 选择题 | 4分 | 答案: A**

2. 设函数<equation>f(x)=\left(\mathrm{e}^{x}-1\right)\left(\mathrm{e}^{2x}-2\right)\cdots\left(\mathrm{e}^{nx}-n\right)</equation>，其中 n为正整数，则<equation>f^{\prime}(0)=</equation>(    )

A.<equation>(-1)^{n-1}(n-1)!</equation>B.<equation>(-1)^{n}(n-1)!</equation>C.<equation>(-1)^{n-1}n!</equation>D.<equation>(-1)^{n}n!</equation>

答案: A

**解析:**解（法一）利用求导的乘法法则来计算<equation>f^{\prime}(0)</equation>.

令<equation>g(x) = \left(\mathrm{e}^{2x} - 2\right)\dots \left(\mathrm{e}^{nx} - n\right)</equation>，则<equation>f(x) = \left(\mathrm{e}^{x} - 1\right)g(x)</equation>. 由求导的乘法法则可得，<equation>f ^ {\prime} (x) = \mathrm {e} ^ {x} g (x) + \left(\mathrm {e} ^ {x} - 1\right) g ^ {\prime} (x).</equation>由于<equation>\mathrm{e}^{0}-1=0</equation>，故<equation>f ^ {\prime} (0) = \mathrm {e} ^ {0} g (0) = (- 1) (- 2) \dots [ - (n - 1) ] = (- 1) ^ {n - 1} (n - 1)!</equation>因此，应选A.

（法二）从导数的定义出发来计算<equation>f^{\prime}(0)</equation>.

由于<equation>f(0)=0</equation>，故<equation>\begin{aligned} f ^ {\prime} (0) &= \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0} \frac {f (x)}{x} = \lim _ {x \rightarrow 0} \frac {\left(\mathrm {e} ^ {x} - 1\right)\left(\mathrm {e} ^ {2 x} - 2\right) \dots \left(\mathrm {e} ^ {n x} - n\right)}{x} \\ \underline {{\mathrm {e} ^ {x} - 1 \sim x}} \lim _ {x \rightarrow 0} \left[ \left(\mathrm {e} ^ {2 x} - 2\right) \dots \left(\mathrm {e} ^ {n x} - n\right)\right] \cdot 1 &= (- 1) (- 2) \dots [ - (n - 1) ] \cdot 1 \\ &= (- 1) ^ {n - 1} (n - 1)!. \end{aligned}</equation>因此，应选A.

（法三）排除法.

我们可以尝试代入 n值，排除不符合题意的选项.由于当 n=2时，四个选项的取值均不同，故可选择 n=2.

当<equation>n = 2</equation>时，<equation>f(x) = \left(\mathrm{e}^{x} - 1\right)\left(\mathrm{e}^{2x} - 2\right), f^{\prime}(0) = -1</equation>，故可排除选项B、C、D.

因此，应选A.

---

**2010年第9题 | 填空题 | 4分**

<equation>9. \mathrm {设} \left\{ \begin{array}{l l} x = \mathrm {e} ^ {- t}, \\ y = \int_ {0} ^ {t} \ln \left(1 + u ^ {2}\right) \mathrm {d} u, \end{array} \right. \mathrm {则} \left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {t = 0} = \underline {{}}</equation>

**解析:**<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\frac {\mathrm {d} y}{\mathrm {d} t}}{\frac {\mathrm {d} x}{\mathrm {d} t}} = \frac {\ln \left(1 + t ^ {2}\right)}{- \mathrm {e} ^ {- t}} = - \mathrm {e} ^ {t} \ln \left(1 + t ^ {2}\right),</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\frac {\mathrm {d} \left(\frac {\mathrm {d} y}{\mathrm {d} x}\right)}{\mathrm {d} t}}{\frac {\mathrm {d} x}{\mathrm {d} t}} = - \frac {\frac {2 t}{1 + t ^ {2}} \cdot \mathrm {e} ^ {t} + \ln \left(1 + t ^ {2}\right) \cdot \mathrm {e} ^ {t}}{- \mathrm {e} ^ {- t}} = \mathrm {e} ^ {2 t} \left[ \frac {2 t}{1 + t ^ {2}} + \ln \left(1 + t ^ {2}\right) \right].</equation>因此，<equation>\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}\bigg|_{t=0}=0.</equation>

---


