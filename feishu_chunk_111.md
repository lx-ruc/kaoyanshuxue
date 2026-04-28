#### 函数极限的计算

**2023年第11题 | 填空题 | 5分**

<equation>\lim _ {x \rightarrow \infty} x ^ {2} \left(2 - x \sin \frac {1}{x} - \cos \frac {1}{x}\right) = \underline {{}}</equation>

**答案:**# 2 3.

**解析:**考虑<equation>\sin x, \cos x</equation>在 x=0处的泰勒公式.当 x<equation>\to\infty</equation>时，<equation>\frac{1}{x}\to0,</equation><equation>\sin \frac {1}{x} = \frac {1}{x} - \frac {1}{6 x ^ {3}} + o \left(\frac {1}{x ^ {3}}\right),</equation><equation>\cos \frac {1}{x} = 1 - \frac {1}{2 x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right).</equation>于是，<equation>\begin{array}{l} x ^ {2} \left(2 - x \sin \frac {1}{x} - \cos \frac {1}{x}\right) = x ^ {2} \left[ 2 - 1 + \frac {1}{6 x ^ {2}} - 1 + \frac {1}{2 x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right) \right] \\ = x ^ {2} \left[ \frac {2}{3 x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right) \right] = \frac {2}{3} + o (1). \\ \end{array}</equation>因此，<equation>\lim _ {x \rightarrow \infty} x ^ {2} \left(2 - x \sin \frac {1}{x} - \cos \frac {1}{x}\right) = \frac {2}{3}.</equation>

---

**2022年第11题 | 填空题 | 5分**

<equation>1. \lim _ {x \rightarrow 0} \left(\frac {1 + \mathrm {e} ^ {x}}{2}\right) ^ {\cot x} = \underline {{}}</equation>

**解析:**取对数再求极限.<equation>\lim _ {x \rightarrow 0} \left(\frac {1 + \mathrm {e} ^ {x}}{2}\right) ^ {\cot x} = \lim _ {x \rightarrow 0} \mathrm {e} ^ {\cot x \ln \frac {1 + \mathrm {e} ^ {x}}{2}} = \mathrm {e} _ {x \rightarrow 0} ^ {\lim _ {x \rightarrow 0} \cot x \ln \frac {1 + \mathrm {e} ^ {x}}{2}}.</equation>下面计算<equation>\lim_{x\to 0}\cot x\ln \frac{1 + \mathrm{e}^{x}}{2}</equation>.<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \cot x \ln \frac {1 + e ^ {x}}{2} = \lim _ {x \rightarrow 0} \frac {\ln \frac {1 + e ^ {x}}{2}}{\tan x} \xlongequal {\tan x \sim x} \lim _ {x \rightarrow 0} \frac {\ln \left(1 + \frac {e ^ {x} - 1}{2}\right)}{x} \\ \frac {\ln \left(1 + \frac {e ^ {x} - 1}{2}\right) \sim \frac {e ^ {x} - 1}{2}}{\lim _ {x \rightarrow 0} \frac {e ^ {x} - 1}{2 x}} \lim _ {x \rightarrow 0} \frac {x}{2 x} \\ = \frac {1}{2}. \\ \end{array}</equation>因此，原极限<equation>= \mathrm{e}^{\frac{1}{2}} = \sqrt{\mathrm{e}}.</equation>

---

**2020年第1题 | 选择题 | 4分 | 答案: B**

1. 设<equation>\lim_{x\rightarrow a}\frac{f(x)-a}{x-a}=b</equation>，则<equation>\lim_{x\rightarrow a}\frac{\sin f(x)-\sin a}{x-a}=</equation>(    )

A.<equation>b\sin a</equation>B.<equation>b\cos a</equation>C.<equation>b\sin f(a)</equation>D.<equation>b\cos f(a)</equation>

答案: B

**解析:**解 由<equation>\lim_{x\to a}\frac{f(x)-a}{x-a}=b</equation>可得，<equation>\lim_{x\to a}[f(x)-a]=0</equation>，即<equation>\lim_{x\to a}f(x)=a.</equation>对<equation>[ f ( x ) , a ]</equation>或<equation>[ a,f ( x ) ]</equation>上的<equation>\sin z</equation>应用拉格朗日中值定理可得，<equation>\sin f (x) - \sin a = \cos \xi_ {x} [ f (x) - a ],</equation>其中<equation>\xi_{x}</equation>介于<equation>f(x)</equation>与<equation>a</equation>之间. 由于<equation>\lim_{x\to a}f(x) = a</equation>，故<equation>\lim_{x\to a}\xi_x = a.</equation><equation>\lim _ {x \rightarrow a} \frac {\sin f (x) - \sin a}{x - a} = \lim _ {x \rightarrow a} \frac {\cos \xi_ {x} [ f (x) - a ]}{x - a} = \lim _ {x \rightarrow a} \cos \xi_ {x} \cdot \lim _ {x \rightarrow a} \frac {f (x) - a}{x - a} = b \cos a.</equation>因此，应选B.

---

**2017年第15题 | 解答题 | 10分**

15. (本题满分10分)

**答案:**# 2 3.

**解析:**解（法一）令<equation>u=x-t</equation>，则<equation>t=x-u,\mathrm{d}u=-\mathrm{d}t,</equation><equation>\int_ {0} ^ {x} \sqrt {x - t} \mathrm {e} ^ {t} \mathrm {d} t = - \int_ {x} ^ {0} \sqrt {u} \mathrm {e} ^ {x - u} \mathrm {d} u = \mathrm {e} ^ {x} \int_ {0} ^ {x} \sqrt {u} \mathrm {e} ^ {- u} \mathrm {d} u.</equation>于是，<equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {x} \int_ {0} ^ {x} \sqrt {u} \mathrm {e} ^ {- u} \mathrm {d} u}{\sqrt {x ^ {3}}} \xlongequal {\lim _ {x \rightarrow 0 ^ {+}} \mathrm {e} ^ {x} = 1} \lim _ {x \rightarrow 0 ^ {+}} \frac {\int_ {0} ^ {x} \sqrt {u} \mathrm {e} ^ {- u} \mathrm {d} u}{\sqrt {x ^ {3}}} \xlongequal {\text {洛 必 达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sqrt {x} \mathrm {e} ^ {- x}}{\frac {3}{2} \sqrt {x}} = \frac {2}{3}.</equation>因此，原极限<equation>= \frac{2}{3}.</equation>（法二）由于<equation>\mathrm{e}^{t}</equation>和<equation>\sqrt{x-t}</equation>均为关于 t的连续函数，且<equation>\sqrt{x-t}</equation>在[0,x]上不变号，故由积分中值定理可得，存在<equation>\xi_{x}\in[0,x]</equation>，使得<equation>\int_ {0} ^ {x} \sqrt {x - t} \mathrm {e} ^ {t} \mathrm {d} t = \mathrm {e} ^ {\xi_ {x}} \int_ {0} ^ {x} \sqrt {x - t} \mathrm {d} t.</equation>因此，<equation>\begin{aligned} \lim _ {x \rightarrow 0 ^ {+}} \frac {\int_ {0} ^ {x} \sqrt {x - t} \mathrm {e} ^ {t} \mathrm {d} t}{\sqrt {x ^ {3}}} &= \lim _ {x \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {\xi_ {x}} \int_ {0} ^ {x} \sqrt {x - t} \mathrm {d} t}{\sqrt {x ^ {3}}} = \lim _ {\substack {x \rightarrow 0 ^ {+} \\ 0 \leqslant \xi_ {x} \leqslant x}} \mathrm {e} ^ {\xi_ {x}} \cdot \lim _ {x \rightarrow 0 ^ {+}} \frac {- \frac {2}{3} (x - t) ^ {\frac {3}{2}} \Big| _ {0} ^ {x}}{\sqrt {x ^ {3}}} \\ &= 1 \cdot \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {2}{3} x ^ {\frac {3}{2}}}{\sqrt {x ^ {3}}} = \frac {2}{3}. \end{aligned}</equation>

---

**2016年第9题 | 填空题 | 4分**

9. 已知函数 f(x)满足<equation>\lim_{x\rightarrow 0}\frac{\sqrt{1+f(x)\sin 2x}-1}{\mathrm{e}^{3x}-1}=2</equation>，则<equation>\lim_{x\rightarrow 0}f(x)=</equation>___.

**解析:**解（法一）由极限的四则运算法则知，<equation>\lim _ {x \rightarrow 0} (\sqrt {1 + f (x) \sin 2 x} - 1) = \lim _ {x \rightarrow 0} \frac {\sqrt {1 + f (x) \sin 2 x} - 1}{\mathrm {e} ^ {3 x} - 1} \cdot \lim _ {x \rightarrow 0} \left(\mathrm {e} ^ {3 x} - 1\right)=2 \times 0=0.</equation>从而<equation>\lim_{x\to 0}\sqrt{1+f(x)\sin 2x}=1</equation>，故<equation>\lim_{x\to 0}f(x)\sin 2x=\lim_{x\to 0}[\left(\sqrt{1+f(x)\sin 2x}\right)^{2}-1]=0.</equation>，当 x→0时，<equation>\sqrt{1+f(x)\sin 2x}-1\sim \frac{1}{2} f(x)\sin 2x.</equation>因此，<equation>\begin{array}{l} 2 = \lim _ {x \rightarrow 0} \frac {\sqrt {1 + f (x) \sin 2 x} - 1}{\mathrm {e} ^ {3 x} - 1} \xlongequal {\mathrm {e} ^ {3 x} - 1 \sim 3 x} \lim _ {x \rightarrow 0} \frac {\frac {1}{2} f (x) \sin 2 x}{3 x} \\ = \frac {1}{3} \lim _ {x \rightarrow 0} \frac {f (x) \sin 2 x}{2 x} \xlongequal {\sin x \sim x} \frac {1}{3} \lim _ {x \rightarrow 0} f (x), \\ \end{array}</equation>即<equation>\lim_{x\to 0}f(x) = 6.</equation>（法二）同法一可得<equation>\lim_{x\rightarrow 0}f(x)\sin 2x=0</equation>.于是<equation>\lim_{x\rightarrow 0}\sqrt{1+f(x)\sin 2x}+1=2.</equation>从而<equation>\begin{array}{l} 2 = \lim _ {x \rightarrow 0} \frac {\sqrt {1 + f (x) \sin 2 x} - 1}{\mathrm {e} ^ {3 x} - 1} \xlongequal {\text {分 子 有 理 化}} \lim _ {x \rightarrow 0} \frac {f (x) \sin 2 x}{\left[ \sqrt {1 + f (x) \sin 2 x} + 1 \right]\left(\mathrm {e} ^ {3 x} - 1\right)} \\ = \lim _ {x \rightarrow 0} \frac {f (x) \sin 2 x}{2 \left(\mathrm {e} ^ {3 x} - 1\right)} = \lim _ {x \rightarrow 0} \frac {f (x) \cdot 2 x}{2 \cdot 3 x} = \frac {1}{3} \lim _ {x \rightarrow 0} f (x), \\ \end{array}</equation>即<equation>\lim_{x\to 0}f(x) = 6.</equation>

---

**2016年第15题 | 解答题 | 10分**

15. (本题满分10分）

求极限<equation>\lim_{x\to 0}(\cos 2x+2x\sin x)^{\frac{1}{x^{4}}}.</equation>

**解析:**记原极限为 I.

（法一）凑重要极限<equation>\lim_{x\to 0}(1 + x)^{\frac{1}{x}} = \mathrm{e}.</equation>由于<equation>x\to0</equation>时，<equation>\cos 2x+2x\sin x-1\to0</equation>，故<equation>\lim_{x\to0}(1+\cos 2x+2x\sin x-1)^{\frac{1}{\cos 2x+2x\sin x-1}}=e.</equation><equation>I = \lim _ {x \rightarrow 0} \left(1 + \cos 2 x + 2 x \sin x - 1\right) ^ {\frac {1}{\cos 2 x + 2 x \sin x - 1}} \cdot \frac {\cos 2 x + 2 x \sin x - 1}{x ^ {4}}.</equation>下面求<equation>\lim_{x\to 0}\frac{\cos 2x+2x\sin x-1}{x^{4}}.</equation><equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\cos 2 x + 2 x \sin x - 1}{x ^ {4}} \xlongequal {\cos 2 x - 1 = - 2 \sin^ {2} x} \lim _ {x \rightarrow 0} \frac {2 x \sin x - 2 \sin^ {2} x}{x ^ {4}} = \lim _ {x \rightarrow 0} \frac {2 \sin x (x - \sin x)}{x ^ {4}} \\ \frac {\sin x - x}{2 \lim _ {x \rightarrow 0} \frac {x - \sin x}{x ^ {3}}} = 2 \lim _ {x \rightarrow 0} \frac {x - x + \frac {x ^ {3}}{3 !} - o \left(x ^ {3}\right)}{x ^ {3}} = \frac {1}{3}. \\ \end{array}</equation>因此，<equation>I = \mathrm{e}^{\frac{1}{3}}.</equation>下面我们用另外两种方法计算<equation>\lim_{x\to 0}\frac{\cos 2x+2x\sin x-1}{x^{4}}.</equation>(1) 利用泰勒公式.<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\cos 2 x + 2 x \sin x - 1}{x ^ {4}} = \lim _ {x \rightarrow 0} \frac {1 - \frac {(2 x) ^ {2}}{2 !} + \frac {(2 x) ^ {4}}{4 !} + o \left(x ^ {4}\right) + 2 x \left[x - \frac {x ^ {3}}{3 !} + o \left(x ^ {3}\right)\right] - 1}{x ^ {4}} \\ = \lim _ {x \rightarrow 0} \frac {\frac {1}{3} x ^ {4} + o \left(x ^ {4}\right)}{x ^ {4}} = \frac {1}{3}. \\ \end{array}</equation>(2) 利用洛必达法则.<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\cos 2 x + 2 x \sin x - 1}{x ^ {4}} \xlongequal {\mathrm {洛必达}} \lim _ {x \rightarrow 0} \frac {- \sin 2 x + \sin x + x \cos x}{2 x ^ {3}} \\ \xlongequal {\mathrm {洛必达}} \lim _ {x \rightarrow 0} \frac {- 2 \cos 2 x + 2 \cos x - x \sin x}{6 x ^ {2}} \\ \xlongequal {\mathrm {洛必达}} \lim _ {x \rightarrow 0} \frac {4 \sin 2 x - 3 \sin x - x \cos x}{1 2 x} \\ \xlongequal {\mathrm {洛必达}} \lim _ {x \rightarrow 0} \frac {8 \cos 2 x - 4 \cos x + x \sin x}{1 2} = \frac {1}{3}. \\ \end{array}</equation>（法二）因为<equation>\lim_{x\to 0} (\cos 2x+2x\sin x)=1</equation>，从而我们可以对<equation>\cos 2x+2x\sin x</equation>取对数，所以 I =<equation>\mathrm{e}^{\lim_{x\to 0}\frac{\ln(\cos 2x+2x\sin x)}{x^{4}}}.</equation>下面求<equation>\lim_{x\to 0}\frac{\ln(\cos 2x+2x\sin x)}{x^{4}}.</equation><equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {\ln (\cos 2 x + 2 x \sin x)}{x ^ {4}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\frac {1}{\cos 2 x + 2 x \sin x} \cdot (- 2 \sin 2 x + 2 \sin x + 2 x \cos x)}{4 x ^ {3}} \\ &= - \frac {1}{2} \lim _ {x \rightarrow 0} \frac {\sin 2 x - \sin x - x \cos x}{x ^ {3}} \\ &= - \frac {1}{2} \lim _ {x \rightarrow 0} \frac {2 x - \frac {(2 x) ^ {3}}{3 !} + o \left(x ^ {3}\right) - x + \frac {x ^ {3}}{3 !} - o \left(x ^ {3}\right) - x \left[ 1 - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right)\right]}{x ^ {3}} \\ &= - \frac {1}{2} \lim _ {x \rightarrow 0} \frac {\left(- \frac {8}{6} + \frac {1}{6} + \frac {1}{2}\right) x ^ {3} + o \left(x ^ {3}\right)}{x ^ {3}} = \frac {1}{3}. \end{aligned}</equation>因此，<equation>I=\mathrm{e}^{\frac{1}{3}}.</equation>

---

**2015年第9题 | 填空题 | 4分**

（无内容）

**答案:**# -<equation>\frac{1}{2}.</equation>

**解析:**（法一）利用洛必达法则.<equation>\lim _ {x \rightarrow 0} \frac {\ln (\cos x)}{x ^ {2}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\frac {1}{\cos x} \cdot (- \sin x)}{2 x} = \lim _ {x \rightarrow 0} \left(- \frac {\sin x}{2 x}\right) = - \frac {1}{2}.</equation>（法二）利用等价无穷小替换.

当<equation>x\to0</equation>时，<equation>\cos x-1\to0,\ln(1+\cos x-1)\sim\cos x-1</equation>，于是<equation>\lim _ {x \rightarrow 0} \frac {\ln (\cos x)}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\ln (1 + \cos x - 1)}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\cos x - 1}{x ^ {2}} \xlongequal {1 - \cos x \sim \frac {1}{2} x ^ {2}} \lim _ {x \rightarrow 0} \frac {- \frac {1}{2} x ^ {2}}{x ^ {2}} = - \frac {1}{2}.</equation>

---

**2014年第15题 | 解答题 | 10分**

15. (本题满分10分)<equation>\mathrm {m} _ {\infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t \right] \mathrm {d} t}{x ^ {2} \ln \left(1 + \frac {1}{x}\right)}.</equation>

**答案:**<equation>(1 5) \frac {1}{2}.</equation>

**解析:**解 由于<equation>\mathrm{e}^{x}</equation>在 x=0处的带拉格朗日余项的2阶泰勒公式为<equation>\mathrm{e}^{x}=1+x+\frac{x^{2}}{2}+\frac{\mathrm{e}^{\theta x}}{3!} x^{3}</equation>其中<equation>0<\theta <1</equation>，故当 x > 0时，<equation>\mathrm{e}^{x}>1+x+\frac{x^{2}}{2}.</equation>于是，<equation>\mathrm{e}^{\frac{1}{t}}-1>\frac{1}{t}+\frac{1}{2t^{2}}(t>0),</equation><equation>t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t > t ^ {2} \left(\frac {1}{t} + \frac {1}{2 t ^ {2}}\right) - t = \frac {1}{2}.</equation>从而<equation>\int_1^{+\infty}[t^2(\mathrm{e}^{\frac{1}{t}} - 1) - t]\mathrm{d}t\to +\infty .</equation>另一方面，<equation>\lim _ {x \rightarrow + \infty} \left[ x ^ {2} \ln \left(1 + \frac {1}{x}\right)\right] \xlongequal {\ln \left(1 + \frac {1}{x}\right) - \frac {1}{x}} \lim _ {x \rightarrow + \infty} x = + \infty .</equation>因此，原极限为<equation>\frac{\infty}{\infty}</equation>型未定式.

当<equation>x\to +\infty</equation>时，<equation>\frac{1}{x}\rightarrow 0,\ln (1 + \frac{1}{x})\sim \frac{1}{x}</equation>，故<equation>\begin{array}{l} \lim _ {x \rightarrow + \infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t \right] \mathrm {d} t}{x ^ {2} \ln \left(1 + \frac {1}{x}\right)} \xlongequal {\ln \left(1 + \frac {1}{x}\right) - \frac {1}{x}} \lim _ {x \rightarrow + \infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t \right] \mathrm {d} t}{x} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow + \infty} \frac {x ^ {2} \left(\mathrm {e} ^ {\frac {1}{x}} - 1\right) - x}{1} = \lim _ {x \rightarrow + \infty} \frac {\mathrm {e} ^ {\frac {1}{x}} - 1 - \frac {1}{x}}{\frac {1}{x ^ {2}}} \\ \xlongequal {u = \frac {1}{x}} \lim _ {u \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {u} - u - 1}{u ^ {2}} \xlongequal {\text {洛必达}} \lim _ {u \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {u} - 1}{2 u} \\ \xlongequal {\mathrm {e} ^ {u} - 1 \sim u} \lim _ {u \rightarrow 0 ^ {+}} \frac {u}{2 u} = \frac {1}{2}. \\ \end{array}</equation>因此，原极限<equation>= \frac{1}{2}.</equation>将原极限化简为<equation>\lim_{x\to +\infty}[x^{2}(\mathrm{e}^{\frac{1}{x}} - 1) - x]</equation>后，也可以用泰勒公式来求该极限.

当<equation>x\to +\infty</equation>时，<equation>\frac{1}{x}\rightarrow 0^{+}</equation>.由<equation>e^{u}</equation>在<equation>u = 0</equation>处的泰勒公式得，<equation>\mathrm {e} ^ {\frac {1}{x}} = 1 + \frac {1}{x} + \frac {1}{2 !} \cdot \frac {1}{x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right).</equation>从而，<equation>\begin{array}{l} \lim _ {x \rightarrow + \infty} \left[ x ^ {2} \left(\mathrm {e} ^ {\frac {1}{x}} - 1\right) - x \right] = \lim _ {x \rightarrow + \infty} \left\{x ^ {2} \left[ \frac {1}{x} + \frac {1}{2 !} \cdot \frac {1}{x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right)\right] - x \right\} \\ = \lim _ {x \rightarrow + \infty} \left[ \frac {1}{2} + x ^ {2} \cdot o \left(\frac {1}{x ^ {2}}\right)\right] = \frac {1}{2}. \\ \end{array}</equation>

---

**2012年第9题 | 填空题 | 4分**

（无内容）

**解析:**解（法一）取对数和利用洛必达法则.<equation>\lim _ {x \rightarrow \frac {\pi}{4}} (\tan x) ^ {\frac {1}{\cos x - \sin x}} = \lim _ {x \rightarrow \frac {\pi}{4}} \mathrm {e} ^ {\frac {\ln (\tan x)}{\cos x - \sin x}} = \mathrm {e} ^ {\lim _ {x \rightarrow \frac {\pi}{4}} \frac {\ln (\tan x)}{\cos x - \sin x}} \xlongequal {\text {洛必达}} \mathrm {e} ^ {\lim _ {x \rightarrow \frac {\pi}{4}} \frac {\frac {1}{\tan x} \cdot \sec^ {2} x}{-\sin x - \cos x}} = \mathrm {e} ^ {\frac {1 \times 2}{- \sqrt {2}}} = \mathrm {e} ^ {- \sqrt {2}}.</equation>（法二）取对数和利用等价无穷小替换.<equation>\begin{array}{l} \lim _ {x \rightarrow \frac {\pi}{4}} (\tan x) ^ {\frac {1}{\cos x - \sin x}} = \lim _ {x \rightarrow \frac {\pi}{4}} e ^ {\frac {\ln (\tan x)}{\cos x - \sin x}} = e ^ {\lim _ {x \rightarrow \frac {\pi}{4}} \frac {\ln (\tan x)}{\cos x - \sin x}} = e ^ {\lim _ {x \rightarrow \frac {\pi}{4}} \frac {\ln (1 + \tan x - 1)}{\cos x - \sin x}} \\ \underline {{\frac {\ln (1 + \tan x - 1) \sim \tan x - 1}{e}}} e ^ {\lim _ {x \rightarrow \frac {\pi}{4}} \frac {\tan x - 1}{- \cos x (\tan x - 1)}} \\ = e ^ {\lim _ {x \rightarrow \frac {\pi}{4}} \frac {1}{- \cos x}} = e ^ {- \sqrt {2}}. \\ \end{array}</equation>（法三）凑重要极限.<equation>\lim _ {x \rightarrow \frac {\pi}{4}} (\tan x) ^ {\frac {1}{\cos x - \sin x}} = \lim _ {x \rightarrow \frac {\pi}{4}} (1 + \tan x - 1) ^ {\frac {1}{\cos x - \sin x}} = \lim _ {x \rightarrow \frac {\pi}{4}} (1 + \tan x - 1) ^ {\frac {1}{\tan x - 1} \cdot \frac {\tan x - 1}{\cos x - \sin x}}.</equation>由于<equation>\lim _ {x \rightarrow \frac {\pi}{4}} \frac {\tan x - 1}{\cos x - \sin x} = \lim _ {x \rightarrow \frac {\pi}{4}} \frac {\tan x - 1}{- \cos x (\tan x - 1)} = \lim _ {x \rightarrow \frac {\pi}{4}} \left(- \frac {1}{\cos x}\right) = - \sqrt {2},</equation>故原极限等于<equation>\mathrm{e}^{- \sqrt{2}}.</equation>

---

**2012年第15题 | 解答题 | 10分**

15. (本题满分10分)

**答案:**## (15)<equation>\frac{1}{1 2}.</equation>

**解析:**<equation>\begin{array}{l} \frac {\mathrm {e} ^ {2 - 2 \cos x - x ^ {2}} - 1 - 2 - 2 \cos x - x ^ {2}}{\lim _ {x \rightarrow 0} \left(2 - 2 \cos x - x ^ {2}\right)} \lim _ {x \rightarrow 0} 1 \cdot \frac {- \left(2 - 2 \cos x - x ^ {2}\right)}{x ^ {4}} \\ = \lim _ {x \rightarrow 0} \frac {x ^ {2} - 2 + 2 \left[ 1 - \frac {x ^ {2}}{2 !} + \frac {x ^ {4}}{4 !} + o \left(x ^ {4}\right)\right]}{x ^ {4}} = \lim _ {x \rightarrow 0} \frac {\frac {1}{1 2} x ^ {4}}{x ^ {4}} = \frac {1}{1 2}. \\ \end{array}</equation><equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x ^ {2}} - \mathrm {e} ^ {2 - 2 \cos x}}{x ^ {4}} \frac {\mathrm {拉 格 朗 日}}{\mathrm {中 值 定 值}} \lim _ {x \rightarrow 0} \mathrm {e} ^ {\xi_ {x}} \cdot \frac {x ^ {2} - (2 - 2 \cos x)}{x ^ {4}} \\ = \lim _ {x \rightarrow 0} \frac {x ^ {2} - (2 - 2 \cos x)}{x ^ {4}} \frac {\mathrm {同 法 一}}{\mathrm {同 法 一}} \frac {1}{1 2}. \\ \end{array}</equation>

---

**2011年第9题 | 填空题 | 4分**

**答案:**##<equation>(1 + 3x)\mathrm{e}^{3x}.</equation>

**解析:**由<equation>\lim_{t\to 0}(1 + t)^{\frac{1}{t}} = \mathrm{e}</equation>知，<equation>f(x) = x\lim_{t\to 0}\left[(1 + 3t)^{\frac{1}{3t}}\right]^{3x} = x\mathrm{e}^{3x}</equation>. 因此，<equation>f ^ {\prime} (x) = \mathrm {e} ^ {3 x} + 3 x \mathrm {e} ^ {3 x} = (1 + 3 x) \mathrm {e} ^ {3 x}.</equation>也可以用另一种方法来计算 f(x).把 x看作常数，t看作变量，极限为<equation>1^{\infty}</equation>型.采用改写成指数形式的方法.<equation>\begin{array}{l} f (x) = \lim _ {t \rightarrow 0} x \left(1 + 3 t\right) ^ {\frac {x}{t}} = \lim _ {t \rightarrow 0} x \mathrm {e} ^ {\frac {x}{t} \ln (1 + 3 t)} = x \cdot \mathrm {e} ^ {\lim _ {t \rightarrow 0} \frac {x}{t} \ln (1 + 3 t)} \\ \underline {{\ln (1 + 3 t) - 3 t}} x \cdot \mathrm {e} ^ {\lim _ {t \rightarrow 0} \frac {x}{t} \cdot 3 t} = x \mathrm {e} ^ {3 x}. \\ \end{array}</equation>

---

**2011年第15题 | 解答题 | 10分**

15. (本题满分10分)

求极限 lim<equation>\frac {\sqrt {1 + 2 \sin x} - x - 1}{x \ln (1 + x)}.</equation>

**答案:**<equation>(1 5) - \frac {1}{2}.</equation>

**解析:**解 （法一）利用等价无穷小替换和洛必达法则.<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\sqrt {1 + 2 \sin x} - x - 1}{x \ln (1 + x)} \xlongequal {\ln (1 + x) \sim x} \lim _ {x \rightarrow 0} \frac {\sqrt {1 + 2 \sin x} - x - 1}{x ^ {2}} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\left(1 + 2 \sin x\right) ^ {- \frac {1}{2}} \cdot \cos x - 1}{2 x} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {- \frac {1}{2} \left(1 + 2 \sin x\right) ^ {- \frac {3}{2}} \cdot 2 \cos^ {2} x - \left(1 + 2 \sin x\right) ^ {- \frac {1}{2}} \cdot \sin x}{2} \\ = \frac {- \frac {1}{2} \times 1 \times 2 - 0}{2} = - \frac {1}{2}. \\ \end{array}</equation>（法二）利用分子有理化对极限式进行转化.<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\sqrt {1 + 2 \sin x} - x - 1}{x \ln (1 + x)} \xlongequal {\ln (1 + x) \sim x} \lim _ {x \rightarrow 0} \frac {\sqrt {1 + 2 \sin x} - x - 1}{x ^ {2}} \\ \xlongequal {\mathrm {分 子 有 理 化}} \lim _ {x \rightarrow 0} \frac {1 + 2 \sin x - (x + 1) ^ {2}}{x ^ {2} \left(\sqrt {1 + 2 \sin x} + x + 1\right)} = \lim _ {x \rightarrow 0} \frac {2 \sin x - x ^ {2} - 2 x}{2 x ^ {2}} \\ \xlongequal {\sin x = x - \frac {x ^ {3}}{3 !} + o \left(x ^ {3}\right)} \lim _ {x \rightarrow 0} \frac {- x ^ {2} - \frac {x ^ {3}}{3} + o \left(x ^ {3}\right)}{2 x ^ {2}} = - \frac {1}{2}. \\ \end{array}</equation>（法三）当<equation>x\to 0</equation>时，<equation>(1+x)^{\alpha}</equation>的二阶泰勒公式为<equation>(1+x)^{\alpha}=1+\alpha x+\frac{\alpha(\alpha-1)}{2} x^{2}+o\left(x^{2}\right).</equation>由于<equation>x\to 0</equation>时，<equation>\sin x\to 0</equation>，故<equation>(1 + 2 \sin x) ^ {\frac {1}{2}} = 1 + \sin x - \frac {1}{2} \sin^ {2} x + o \left(4 \sin^ {2} x\right) = 1 + \sin x - \frac {1}{2} \sin^ {2} x + o \left(x ^ {2}\right),</equation>这里<equation>o\left(4\sin^{2}x\right) = o\left(x^{2}\right)</equation>是因为<equation>\sin^{2}x</equation>与<equation>x^{2}</equation>是<equation>x\to 0</equation>时的等价无穷小量.因此，<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\sqrt {1 + 2 \sin x} - x - 1}{x \ln (1 + x)} \xlongequal {\ln (1 + x) - x} \lim _ {x \rightarrow 0} \frac {\sqrt {1 + 2 \sin x} - x - 1}{x ^ {2}} \\ = \lim _ {x \rightarrow 0} \frac {1 + \sin x - \frac {1}{2} \sin^ {2} x + o \left(x ^ {2}\right) - x - 1}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\sin x - x - \frac {1}{2} \sin^ {2} x}{x ^ {2}} \\ = \lim _ {x \rightarrow 0} \left(\frac {\sin x - x}{x ^ {2}} - \frac {\sin^ {2} x}{2 x ^ {2}}\right) = \lim _ {x \rightarrow 0} \frac {\sin x - x}{x ^ {2}} - \frac {1}{2} \\ \end{array}</equation><equation>\frac {\sin x = x - \frac {x ^ {3}}{3 !} + o \left(x ^ {3}\right)}{\lim _ {x \rightarrow 0} \frac {- \frac {x ^ {3}}{6} + o \left(x ^ {3}\right)}{x ^ {2}} - \frac {1}{2}} = 0 - \frac {1}{2} = - \frac {1}{2}.</equation>

---

**2010年第15题 | 解答题 | 10分**

15. (本题满分10分)

求极限<equation>\lim_{x\to +\infty}\left(x^{\frac{1}{x}} - 1\right)^{\frac{1}{\ln x}}.</equation>

**答案:**(15)<equation>\mathrm{e}^{-1}.</equation>

**解析:**解（法一）记<equation>y = \left(x^{\frac{1}{x}} - 1\right)^{\frac{1}{\ln x}}</equation>，则<equation>\ln y = \frac {\ln \left(x ^ {\frac {1}{x}} - 1\right)}{\ln x}.</equation>利用洛必达法则计算<equation>\lim \ln y</equation>得，<equation>\begin{array}{l} \lim _ {x \rightarrow + \infty} \frac {\ln \left(x ^ {\frac {1}{x}} - 1\right)}{\ln x} = \lim _ {x \rightarrow + \infty} \frac {\ln \left(\mathrm {e} ^ {\frac {\ln x}{x}} - 1\right)}{\ln x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow + \infty} \frac {\mathrm {e} ^ {\frac {\ln x}{x}} \cdot \frac {1 - \ln x}{x ^ {2}}}{\frac {1}{x} \left(\mathrm {e} ^ {\frac {\ln x}{x}} - 1\right)} \xlongequal {\lim _ {x \rightarrow + \infty} \mathrm {e} ^ {\frac {\ln x}{x}} = 1} \lim _ {x \rightarrow + \infty} \frac {\frac {1 - \ln x}{x}}{\frac {\ln x}{x}} \\ = \lim _ {x \rightarrow + \infty} \frac {1 - \ln x}{\ln x} = \lim _ {x \rightarrow + \infty} \left(\frac {1}{\ln x} - 1\right) = - 1. \\ \end{array}</equation>因此，原极限<equation>= \mathrm{e}^{-1}</equation>或者也可以这样计算.<equation>\begin{array}{l} \lim _ {x \rightarrow + \infty} \frac {\ln \left(x ^ {\frac {1}{x}} - 1\right)}{\ln x} = \lim _ {x \rightarrow + \infty} \frac {\ln \left(\mathrm {e} ^ {\frac {\ln x}{x}} - 1\right)}{\ln x} \stackrel {\text {洛必达}} {=} \lim _ {x \rightarrow + \infty} \frac {\frac {\mathrm {e} ^ {\frac {\ln x}{x}} \cdot \frac {1 - \ln x}{x ^ {2}}}{\frac {1}{x} \left(\mathrm {e} ^ {\frac {\ln x}{x}} - 1\right)}}{\frac {\lim _ {x \rightarrow + \infty} \mathrm {e} ^ {\frac {\ln x}{x}} = 1}{\lim _ {x \rightarrow + \infty} \frac {1 - \ln x}{x}}} \\ \underline {{\mathrm {洛必达}}} \lim _ {x \rightarrow + \infty} \frac {\frac {- 2 + \ln x}{x ^ {2}}}{\mathrm {e} ^ {\frac {\ln x}{x}} \cdot \frac {1 - \ln x}{x ^ {2}}} = \lim _ {x \rightarrow + \infty} \frac {- 2 + \ln x}{1 - \ln x} = - 1. \\ \end{array}</equation>（法二）注意到<equation>\lim_{u\to 0^{+}}\frac{\ln(\mathrm{e}^{u}-1)}{\ln u}\xlongequal{\text{洛必达}}\lim_{u\to 0^{+}}\frac{u\mathrm{e}^{u}}{\mathrm{e}^{u}-1}\xlongequal{\text{e}^{u}-1\sim u}\lim_{u\to 0^{+}}\frac{u\mathrm{e}^{u}}{u}=1</equation>，故<equation>\frac {\ln \left(\mathrm {e} ^ {\frac {\ln x}{x}} - 1\right)}{\ln \frac {\ln x}{x}} \cdot \ln \frac {\ln x}{x}</equation><equation>\begin{array}{l} \lim _ {x \rightarrow + \infty} \frac {\ln \left(x ^ {\frac {1}{x}} - 1\right)}{\ln x} = \lim _ {x \rightarrow + \infty} \frac {\ln \left(\mathrm {e} ^ {\frac {\ln x}{x}} - 1\right)}{\ln x} = \lim _ {x \rightarrow + \infty} \frac {\ln \frac {\ln x}{x} ^ {x}}{\ln x} \\ = \lim _ {x \rightarrow + \infty} \frac {\ln \frac {\ln x}{x}}{\ln x} = \lim _ {x \rightarrow + \infty} \frac {\ln \ln x - \ln x}{\ln x} \\ \underline {{\underline {{\text {洛必达}}}}} \lim _ {x \rightarrow + \infty} \left(\frac {1}{\ln x} - 1\right) = - 1. \\ \end{array}</equation>因此，原极限<equation>= \mathrm{e}^{-1}</equation>

---

**2009年第9题 | 填空题 | 4分**

（无内容）

**解析:**（法三）<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\mathrm {e} - \mathrm {e} ^ {\cos x}}{\sqrt {3} \sqrt {1 + x ^ {2}} - 1} = \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {1} - \mathrm {e} ^ {\cos x}}{\frac {1}{3} x ^ {2}} \\ \frac {\mathrm {拉 格 朗 日}}{\mathrm {中 值 定 值}} \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {\xi_ {x}} (1 - \cos x)}{\frac {1}{3} x ^ {2}} (\xi_ {x} \mathrm {在} 1 \mathrm {与} \cos x \mathrm {之间}, \mathrm {当} x \rightarrow 0 \mathrm {时}, \xi_ {x} \rightarrow 1) \\ = \lim _ {x \rightarrow 0} \mathrm {e} \cdot \frac {\frac {1}{2} x ^ {2}}{\frac {1}{3} x ^ {2}} = \frac {3}{2} \mathrm {e}. \\ \end{array}</equation>（法四）<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\mathrm {e} - \mathrm {e} ^ {\cos x}}{\sqrt {3} \left(1 + x ^ {2}\right) - 1} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {\cos x} \cdot \sin x}{\frac {1}{3} \left(1 + x ^ {2}\right) ^ {- \frac {2}{3}} \cdot 2 x} = \lim _ {x \rightarrow 0} \frac {3}{2} \left(1 + x ^ {2}\right) ^ {\frac {2}{3}} \cdot \frac {\mathrm {e} ^ {\cos x} \cdot \sin x}{x} \\ = \frac {3}{2} \times 1 \times \mathrm {e} = \frac {3}{2} \mathrm {e}. \\ \end{array}</equation>解（法一）<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\mathrm {e} - \mathrm {e} ^ {\cos x}}{\sqrt {3} \left(1 + x ^ {2}\right) - 1} \equiv \frac {(1 + x) ^ {\alpha} - 1 \sim \alpha x}{\overline {{\quad}}} \lim _ {x \rightarrow 0} \frac {\mathrm {e} - \mathrm {e} ^ {\cos x}}{\frac {1}{3} x ^ {2}} \equiv \frac {\text {洛必达}}{\overline {{\quad}}} \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {\cos x} \cdot \sin x}{\frac {2}{3} x} \\ = \lim _ {x \rightarrow 0} \frac {3}{2} \mathrm {e} ^ {\cos x} = \frac {3}{2} \mathrm {e}. \\ \end{array}</equation>（法二）<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\mathrm {e} - \mathrm {e} ^ {\cos x}}{\sqrt {3} \sqrt {1 + x ^ {2}} - 1} \xlongequal {(1 + x) ^ {\alpha} - 1 \sim \alpha x} \lim _ {x \rightarrow 0} \frac {\mathrm {e} \left(1 - \mathrm {e} ^ {\cos x - 1}\right)}{\frac {1}{3} x ^ {2}} \\ \xlongequal {\mathrm {e} ^ {\cos x - 1} - 1 \sim \cos x - 1} \lim _ {x \rightarrow 0} \frac {\mathrm {e} [ - (\cos x - 1) ]}{\frac {1}{3} x ^ {2}} \\ \xlongequal {1 - \cos x \sim \frac {1}{2} x ^ {2}} \lim _ {x \rightarrow 0} \frac {\frac {1}{2} \mathrm {e} x ^ {2}}{\frac {1}{3} x ^ {2}} = \frac {3}{2} \mathrm {e}. \\ \end{array}</equation>

---


