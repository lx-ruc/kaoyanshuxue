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
