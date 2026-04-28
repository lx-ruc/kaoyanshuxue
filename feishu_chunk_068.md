#### 函数极限的计算

**2025年第11题 | 填空题 | 5分**

<equation>1 1. \lim _ {x \rightarrow 0 ^ {+}} \frac {x ^ {x} - 1}{\ln x \cdot \ln (1 - x)} = \underline {{}}</equation>

**解析:**解 由于<equation>x^{x}=\mathrm{e}^{x\ln x}</equation>，且当<equation>x\to0</equation>时，<equation>\mathrm{e}^{x}-1\sim x</equation>，故<equation>\lim_{x\to0^{+}}\frac{x^{x}-1}{\ln x\cdot\ln(1-x)}=\lim_{x\to0^{+}}\frac{\mathrm{e}^{x\ln x}-1}{\ln x\cdot\ln(1-x)} \frac{\mathrm{e}^{x\ln x}-1\sim x\ln x}{\ln(1-x)\sim-x} \lim_{x\to0^{+}}\frac{x\ln x}{\ln x\cdot(-x)}=-1.</equation>

---

**2021年第17题 | 解答题 | 10分**

17. (本题满分10分)

求极限 lim<equation>\left(\frac {1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t}{\mathrm {e} ^ {x} - 1} - \frac {1}{\sin x}\right)</equation>

**解析:**解 （法一）先整理原极限再计算.<equation>\begin{array}{l} \frac {\mathrm {e} ^ {x} - 1 \sim x}{\sin x \sim x} \lim _ {x \rightarrow 0} \frac {\int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t}{x} + \lim _ {x \rightarrow 0} \frac {\sin x - \mathrm {e} ^ {x} + 1}{x ^ {2}} \\ \frac {\text {洛必达}}{} \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x ^ {2}}}{1} + \lim _ {x \rightarrow 0} \frac {x - \frac {x ^ {3}}{6} - 1 - x - \frac {x ^ {2}}{2} + 1 + o \left(x ^ {2}\right)}{x ^ {2}} \\ = 1 + \lim _ {x \rightarrow 0} \frac {- \frac {x ^ {2}}{2} + o \left(x ^ {2}\right)}{x ^ {2}} = 1 - \frac {1}{2} = \frac {1}{2}. \\ \end{array}</equation>因此，原极限<equation>= \frac{1}{2}</equation>（法二）将原极限通分整理，化为<equation>\frac{0}{0}</equation>型未定式后再应用洛必达法则.<equation>\begin{aligned} \mathrm {原 极 限} &= \lim _ {x \rightarrow 0} \frac {\sin x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) - \mathrm {e} ^ {x} + 1}{\left(\mathrm {e} ^ {x} - 1\right) \sin x} \\ \frac {\mathrm {e} ^ {x} - 1 \sim x}{\sin x \sim x} \lim _ {x \rightarrow 0} \frac {\sin x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) - \mathrm {e} ^ {x} + 1}{x ^ {2}} \\ \underline {{\text {洛必达}}} \lim _ {x \rightarrow 0} \frac {\cos x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) + \sin x \cdot \mathrm {e} ^ {x ^ {2}} - \mathrm {e} ^ {x}}{2 x} \\ \underline {{\text {洛必达}}} \lim _ {x \rightarrow 0} \frac {- \sin x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) + \cos x \cdot \mathrm {e} ^ {x ^ {2}} + \cos x \cdot \mathrm {e} ^ {x ^ {2}} + 2 x \cdot \sin x \cdot \mathrm {e} ^ {x ^ {2}} - \mathrm {e} ^ {x}}{2} &= \frac {1}{2}. \\ \mathrm {因 此 , 原 极 限} &= \frac {1}{2}. \end{aligned}</equation>

---

**2020年第9题 | 填空题 | 4分**

9. lim

**答案:**```latex

-1.
```
**解析: **解 通分整理原极限.<equation>\lim _ {x \rightarrow 0} \left[ \frac {1}{\mathrm {e} ^ {x} - 1} - \frac {1}{\ln (1 + x)} \right] = \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - \mathrm {e} ^ {x} + 1}{\left(\mathrm {e} ^ {x} - 1\right) \ln (1 + x)} \frac {\mathrm {e} ^ {x} - 1 \sim x}{\ln (1 + x) \sim x} \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - \mathrm {e} ^ {x} + 1}{x ^ {2}}.</equation>下面用两种方法计算<equation>\lim_{x\to 0}\frac{\ln(1 + x) - \mathrm{e}^{x} + 1}{x^{2}}.</equation>（法一）利用泰勒公式.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - \mathrm {e} ^ {x} + 1}{x ^ {2}} &= \lim _ {x \rightarrow 0} \frac {x - \frac {x ^ {2}}{2} + o \left(x ^ {2}\right) - \left[ 1 + x + \frac {x ^ {2}}{2} + o \left(x ^ {2}\right)\right] + 1}{x ^ {2}} \\ &= \lim _ {x \rightarrow 0} \frac {- x ^ {2} + o \left(x ^ {2}\right)}{x ^ {2}} = - 1. \end{aligned}</equation>（法二）利用洛必达法则.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - \mathrm {e} ^ {x} + 1}{x ^ {2}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\frac {1}{1 + x} - \mathrm {e} ^ {x}}{2 x} &= \lim _ {x \rightarrow 0} \frac {1 - \mathrm {e} ^ {x} (1 + x)}{2 x (1 + x)} = \frac {1}{2} \lim _ {x \rightarrow 0} \frac {1 - \mathrm {e} ^ {x} - x \mathrm {e} ^ {x}}{x} \\ &= \frac {1}{2} \lim _ {x \rightarrow 0} \left(\frac {1 - \mathrm {e} ^ {x}}{x} - \mathrm {e} ^ {x}\right) \xlongequal {\text {洛必达}} \frac {1 - \mathrm {e} ^ {x} \sim - x}{2} \frac {1}{2} \times (- 1 - 1) = - 1. \end{aligned}</equation>

---

**2016年第9题 | 填空题 | 4分**
9. lim
**答案: **# 1 2.
**解析: **解 当<equation>x\to0</equation>时，<equation>1-\cos x^{2}\sim\frac{1}{2} x^{4},\ln(1+x\sin x)\sim x\sin x</equation>从而<equation>\lim _ {x \rightarrow 0} \frac {\int_ {0} ^ {x} t \ln (1 + t \sin t) \mathrm {d} t}{1 - \cos x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\int_ {0} ^ {x} t \ln (1 + t \sin t) \mathrm {d} t}{\frac {1}{2} x ^ {4}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {x \ln (1 + x \sin x)}{2 x ^ {3}} = \lim _ {x \rightarrow 0} \frac {x \cdot x \sin x}{2 x ^ {3}} = \frac {1}{2}.</equation>

---

**2015年第9题 | 填空题 | 4分**
（无内容）
**解析: **解 （法一）利用洛必达法则.<equation>\lim _ {x \rightarrow 0} \frac {\ln (\cos x)}{x ^ {2}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\frac {1}{\cos x} \cdot (- \sin x)}{2 x} = \lim _ {x \rightarrow 0} \left(- \frac {\sin x}{2 x}\right) = - \frac {1}{2}.</equation>（法二）利用等价无穷小替换.

当<equation>x\to 0</equation>时，<equation>\cos x - 1\to 0,\ln (1 + \cos x - 1)\sim \cos x - 1</equation>，于是<equation>\lim _ {x \rightarrow 0} \frac {\ln (\cos x)}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\ln (1 + \cos x - 1)}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\cos x - 1}{x ^ {2}} \frac {1 - \cos x - \frac {1}{2} x ^ {2}}{\overline {{=}}} \lim _ {x \rightarrow 0} \frac {- \frac {1}{2} x ^ {2}}{x ^ {2}} = - \frac {1}{2}.</equation>

---

**2014年第15题 | 解答题 | 10分**
15. (本题满分10分)

求极限<equation>\lim _ {x \rightarrow + \infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right)-t \right] \mathrm {d} t}{x ^ {2} \ln \left(1 + \frac {1}{x}\right)}.</equation>
**答案: **<equation>(1 5) \frac {1}{2}.</equation>
**解析: **解 由于<equation>\mathrm{e}^{x}</equation>在 x=0处的带拉格朗日余项的2阶泰勒公式为<equation>\mathrm{e}^{x}=1+x+\frac{x^{2}}{2}+\frac{\mathrm{e}^{\theta x}}{3!} x^{3}</equation>其中<equation>0 < \theta < 1</equation>，故当 x > 0时，<equation>\mathrm{e}^{x}>1+x+\frac{x^{2}}{2}.</equation>于是，<equation>\mathrm{e}^{\frac{1}{t}}-1 > \frac{1}{t}+\frac{1}{2t^{2}}(t > 0),</equation><equation>t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t > t ^ {2} \left(\frac {1}{t} + \frac {1}{2 t ^ {2}}\right) - t = \frac {1}{2}.</equation>从而<equation>\int_{1}^{+\infty}\left[ t^{2}\left(\mathrm{e}^{\frac{1}{t}} - 1\right) - t\right]\mathrm{d}t\to +\infty .</equation>另一方面，<equation>\lim _ {x \rightarrow + \infty} \left[ x ^ {2} \ln \left(1 + \frac {1}{x}\right)\right] \xlongequal {\ln \left(1 + \frac {1}{x}\right) \sim \frac {1}{x}} \lim _ {x \rightarrow + \infty} x = + \infty .</equation>因此，原极限为<equation>\frac{\infty}{\infty}</equation>型未定式.

当<equation>x\to +\infty</equation>时，<equation>\ln \left(1 + \frac{1}{x}\right)\sim \frac{1}{x}</equation>，故<equation>\begin{aligned} \lim _ {x \rightarrow + \infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t \right] \mathrm {d} t}{x ^ {2} \ln \left(1 + \frac {1}{x}\right)} \xlongequal {\ln \left(1 + \frac {1}{x}\right) \sim \frac {1}{x}} \lim _ {x \rightarrow + \infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t \right] \mathrm {d} t}{x} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow + \infty} \frac {x ^ {2} \left(\mathrm {e} ^ {\frac {1}{x}} - 1\right) - x}{1} &= \lim _ {x \rightarrow + \infty} \frac {\mathrm {e} ^ {\frac {1}{x}} - 1 - \frac {1}{x}}{\frac {1}{x ^ {2}}} \\ \xlongequal {u = \frac {1}{x}} \lim _ {u \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {u} - u - 1}{u ^ {2}} \xlongequal {\text {洛必达}} \lim _ {u \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {u} - 1}{2 u} \\ \xlongequal {\mathrm {e} ^ {u} - 1 \sim u} \lim _ {u \rightarrow 0 ^ {+}} \frac {u}{2 u} &= \frac {1}{2}. \end{aligned}</equation>因此，原极限<equation>= \frac{1}{2}.</equation>将原极限化简为<equation>\lim_{x\to +\infty}[x^{2}(\mathrm{e}^{\frac{1}{x}} -1) - x]</equation>后，也可以用泰勒公式来求该极限.

当<equation>x\to +\infty</equation>时，<equation>\frac{1}{x}\rightarrow 0^{+}</equation>.由<equation>\mathrm{e}^{u}</equation>在<equation>u = 0</equation>处的泰勒公式得，<equation>\mathrm {e} ^ {\frac {1}{x}} = 1 + \frac {1}{x} + \frac {1}{2 !} \cdot \frac {1}{x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right).</equation>从而，<equation>\begin{array}{l} \lim _ {x \rightarrow + \infty} \left[ x ^ {2} \left(\mathrm {e} ^ {\frac {1}{x}} - 1\right) - x \right] = \lim _ {x \rightarrow + \infty} \left\{x ^ {2} \left[ \frac {1}{x} + \frac {1}{2 !} \cdot \frac {1}{x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right)\right] - x \right\} \\ = \lim _ {x \rightarrow + \infty} \left[ \frac {1}{2} + x ^ {2} \cdot o \left(\frac {1}{x ^ {2}}\right)\right] = \frac {1}{2}. \\ \end{array}</equation>

---

**2011年第15题 | 解答题 | 10分**
15. (本题满分10分)
**解析: **解（法一）由于当<equation>x\to 0</equation>时，<equation>\frac{\ln(1+x)}{x}>0</equation>，故可以对函数<equation>\left[\frac{\ln(1+x)}{x}\right]^{\frac{1}{e^{x}-1}}</equation>取对数.又<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {1}{\mathrm {e} ^ {x} - 1} \ln \frac {\ln (1 + x)}{x} \xlongequal {\mathrm {e} ^ {x} - 1 \sim x} \lim _ {x \rightarrow 0} \frac {\ln \left[ 1 + \frac {\ln (1 + x) - x}{x} \right]}{x} \\ \xlongequal {\ln (1 + t) - t} \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - x}{x ^ {2}} \\ = \lim _ {x \rightarrow 0} \frac {x - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right) - x}{x ^ {2}} = - \frac {1}{2}, \\ \end{array}</equation>故<equation>\lim_{x\to 0}\left[\frac{\ln(1 + x)}{x}\right]^{\frac{1}{e^x - 1}} = \mathrm{e}^{-\frac{1}{2}}.</equation>(法二)<equation>\lim_{x\to 0}\left[\frac{\ln(1 + x)}{x}\right]^{\frac{1}{e^x - 1}} = \lim_{x\to 0}\left[1 + \frac{\ln(1 + x) - x}{x}\right]^{\frac{x}{\ln(1 + x) - x} \cdot \frac{\ln(1 + x) - x}{x} \cdot \frac{1}{e^x - 1}}.</equation>由于<equation>\lim _ {x \rightarrow 0} \left[ \frac {\ln (1 + x) - x}{x} \cdot \frac {1}{\mathrm {e} ^ {x} - 1} \right] = \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - x}{x ^ {2}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\frac {1}{1 + x} - 1}{2 x} = \lim _ {x \rightarrow 0} \frac {- 1}{2 (1 + x)} = - \frac {1}{2},</equation><equation>= \mathrm {e} ^ {- \frac {1}{2}}</equation>（法三）由于

注意该技巧！添加绝对值后不用分情况讨论.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {1}{\mathrm {e} ^ {x} - 1} \ln \frac {\ln (1 + x)}{x} &= \lim _ {x \rightarrow 0} \frac {\ln \left| \frac {\ln (1 + x)}{x} \right|}{\mathrm {e} ^ {x} - 1} = \lim _ {x \rightarrow 0} \frac {\ln | \ln (1 + x) | - \ln | x |}{x} \\ \underline {{\text {洛必达}}} \lim _ {x \rightarrow 0} \left[ \frac {\frac {1}{1 + x}}{\ln (1 + x)} - \frac {1}{x} \right] &= \lim _ {x \rightarrow 0} \frac {x - (1 + x) \ln (1 + x)}{x (1 + x) \ln (1 + x)} \\ \underline {{\frac {\ln (1 + x) - x}{\lim _ {x \rightarrow 0} (1 + x) = 1}}} \lim _ {x \rightarrow 0} \frac {x - (1 + x) \ln (1 + x)}{x ^ {2}} \\ \underline {{\text {洛必达}}} \lim _ {x \rightarrow 0} \frac {- \ln (1 + x)}{2 x} &= - \frac {1}{2}, \end{aligned}</equation>故<equation>\lim_{x\to 0}\left[\frac{\ln(1 + x)}{x}\right]^{\frac{1}{e^x - 1}} = \mathrm{e}^{-\frac{1}{2}}.</equation>

---

**2010年第1题 | 选择题 | 4分 | 答案: C**
1. 极限<equation>\lim_{x\to \infty}\left[\frac{x^{2}}{(x-a)(x+b)}\right]^{x}=(\quad)</equation>A. 1 B. e C.<equation>e^{a-b}</equation>D.<equation>e^{b-a}</equation>
答案: C
**解析: **解（法一）若 a,b 不同时为0，则<equation>( a-b) x+a b\neq0</equation>由<equation>\lim_{x\to\infty}\frac{(a-b)x+ab}{(x-a)(x+b)}=0</equation>以及重要极限<equation>\lim_{x\to\infty}\left(1+\frac{1}{x}\right)^{x}=e</equation>的复合形式可知，<equation>\begin{aligned} \lim _ {x \rightarrow \infty} \left[ \frac {x ^ {2}}{(x - a) (x + b)} \right] ^ {x} &= \lim _ {x \rightarrow \infty} \left[ 1 + \frac {(a - b) x + a b}{(x - a) (x + b)} \right] ^ {x} \\ &= \lim _ {x \rightarrow \infty} \left[ \left[ 1 + \frac {(a - b) x + a b}{(x - a) (x + b)} \right] ^ {\frac {(x - a) (x + b)}{(a - b) x + a b}} \right] ^ {\left[ \frac {(a - b) x + a b}{(x - a) (x + b)} \cdot x \right]} \\ &= \mathrm {e} ^ {\lim _ {x \rightarrow \infty} \frac {(a - b) x ^ {2} + a b x}{x ^ {2} - (a - b) x - a b}} = \mathrm {e} ^ {\lim _ {x \rightarrow \infty} \frac {(a - b) + \frac {a b}{x}}{- \frac {a - b}{x} - \frac {a b}{x ^ {2}}}} = \mathrm {e} ^ {a - b}. \end{aligned}</equation>若<equation>a = b = 0</equation>，则原式<equation>= \lim_{x\to \infty}1^{x} = 1 = \mathrm{e}^{a - b}</equation>.

综上所述，应选C.

（法二）当<equation>x\to \infty</equation>时（无论是<equation>+\infty</equation>还是<equation>-\infty</equation>），<equation>\frac{x^{2}}{(x-a)(x+b)}>0</equation>，故可以对<equation>\left[ \frac{x^{2}}{(x-a)(x+b)} \right]^{x}</equation>取对数.又<equation>\begin{aligned} \lim _ {x \rightarrow \infty} \ln \left[ \frac {x ^ {2}}{(x - a) (x + b)} \right] ^ {x} &= \lim _ {x \rightarrow \infty} x \ln \frac {x ^ {2}}{(x - a) (x + b)} = \lim _ {x \rightarrow \infty} x \ln \left[ 1 + \frac {(a - b) x + a b}{(x - a) (x + b)} \right] \\ &= \lim _ {x \rightarrow \infty} \left[ x \cdot \frac {(a - b) x + a b}{(x - a) (x + b)} \right] = \lim _ {x \rightarrow \infty} \frac {(a - b) x ^ {2} + a b x}{(x - a) (x + b)} = a - b, \end{aligned}</equation>故原式<equation>= \mathrm{e}^{a - b}.</equation>应选C.

---


