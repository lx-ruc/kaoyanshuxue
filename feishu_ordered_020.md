# 数学三

## 高等数学

### 函数、极限、连续

#### 函数的连续性与间断点的类型

**2024年第1题 | 选择题 | 5分 | 答案: D**

1. 设函数<equation>f ( x )=\lim_{n \to \infty} \frac{1+x}{1+n x^{2 n}},</equation>则 f(x)，（    ）

A. 在 x=1,x=-1处都连续 B. 在 x=1处连续，在 x=-1处不连续

C. 在 x=1,x=-1处都不连续 D. 在 x=1处不连续，在 x=-1处连续

答案: D

**解析:**解 由于<equation>\lim_{n\to \infty}x^{2n}=\left\{\begin{array}{ll}0,&|x|<1,\\ 1,&|x|=1,\text{故当}|x|<1\text{时},\lim_{n\to \infty}\frac{1+x}{1+nx^{2n}}=\lim_{n\to \infty}\frac{1+x}{1}=1+x,\text{当} \\ +\infty,&|x|>1,\end{array} \right.</equation><equation>|x| = 1</equation>时，<equation>\lim_{n\to \infty}\frac{1 + x}{1 + nx^{2n}} = \lim_{n\to \infty}\frac{1 + x}{1 + n} = 0</equation>，当<equation>|x| > 1</equation>时，<equation>\lim_{n\to \infty}\frac{1 + x}{1 + nx^{2n}} = 0.</equation>于是，<equation>f (x) = \left\{ \begin{array}{l l} 1 + x, & | x | < 1, \\ 0, & | x | \geqslant 1. \end{array} \right.</equation>由于<equation>\lim_{x\to -1^{+}}f(x) = \lim_{x\to -1^{+}}(1 + x) = 0,\lim_{x\to -1^{-}}f(x) = 0 = f(-1),\lim_{x\to -1^{-}}f(x) = \lim_{x\to -1^{+}}(1 + x) = 2,</equation><equation>\lim_{x\to 1^{+}}f(x) = 0</equation>，故<equation>f(x)</equation>在<equation>x = -1</equation>处连续，<equation>x = 1</equation>处不连续.因此，应选D.

---

**2020年第2题 | 选择题 | 4分 | 答案: C**

2. 函数<equation>f(x)=\frac{\mathrm{e}^{\frac{1}{x-1}}\ln|1+x|}{(\mathrm{e}^{x}-1)(x-2)}</equation>的第二类间断点的个数为（    )

A.1 B.2 C.3 D.4

答案: C

**解析:**解从 f(x)的表达式可以看出，<equation>x=-1,x=0,x=1,x=2</equation>为 f(x)的间断点.下面分别计算这些点处的左、右极限.<equation>\lim _ {x \rightarrow - 1} f (x) = \lim _ {x \rightarrow - 1} \frac {\mathrm {e} ^ {\frac {1}{x - 1}} \ln | 1 + x |}{\left(\mathrm {e} ^ {x} - 1\right) (x - 2)} = \frac {\mathrm {e} ^ {- \frac {1}{2}}}{\left(\mathrm {e} ^ {- 1} - 1\right) \cdot (- 3)} \lim _ {x \rightarrow - 1} \ln | 1 + x | = \infty .</equation><equation>\lim _ {x \rightarrow 0} f (x) = \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {\frac {1}{x - 1}} \ln | 1 + x |}{\left(\mathrm {e} ^ {x} - 1\right) (x - 2)} = \frac {\mathrm {e} ^ {- 1}}{- 2} \lim _ {x \rightarrow 0} \frac {\ln | 1 + x |}{\mathrm {e} ^ {x} - 1} \frac {\ln | 1 + x | \sim x}{\mathrm {e} ^ {x} - 1 \sim x} - \frac {1}{2 \mathrm {e}} \lim _ {x \rightarrow 0} \frac {x}{x} = - \frac {1}{2 \mathrm {e}}.</equation><equation>\lim _ {x \rightarrow 1 ^ {+}} f (x) = \lim _ {x \rightarrow 1 ^ {+}} \frac {\mathrm {e} ^ {\frac {1}{x - 1}} \ln | 1 + x |}{\left(\mathrm {e} ^ {x} - 1\right) (x - 2)} = - \frac {\ln 2}{\mathrm {e} - 1} \lim _ {x \rightarrow 1 ^ {+}} \mathrm {e} ^ {\frac {1}{x - 1}} = \infty .</equation><equation>\lim _ {x \rightarrow 2} f (x) = \lim _ {x \rightarrow 2} \frac {\mathrm {e} ^ {\frac {1}{x - 1}} \ln | 1 + x |}{\left(\mathrm {e} ^ {x} - 1\right) (x - 2)} = \frac {\mathrm {e} \ln 3}{\mathrm {e} ^ {2} - 1} \lim _ {x \rightarrow 2} \frac {1}{x - 2} = \infty .</equation>因此，<equation>x=-1,x=1</equation>和 x=2均为 f(x)的无穷间断点，从而也是第二类间断点. f(x)共有3个第二类间断点.应选C.

---

**2017年第1题 | 选择题 | 4分 | 答案: A**

1. 若函数 f(x)<equation>\left\{\begin{array}{l l}{\frac{1-\cos \sqrt{x}}{ax},}&{x>0,}\\ {b,}&{x\leqslant 0}\end{array}\right.</equation>在 x=0处连续，则（   ）

A.<equation>a b=\frac{1}{2}</equation>B.<equation>a b=-\frac{1}{2}</equation>C.<equation>a b=0</equation>D.<equation>a b=2</equation>

答案: A

**解析:**解 f(x)是分段函数.代入 f(x)在<equation>(-\infty, 0]</equation>和（0，<equation>+\infty</equation>）上的表达式，分别计算<equation>\lim_{x\to 0^{-}}f(x),</equation><equation>\lim_{x\to 0^{+}}f(x).</equation><equation>\lim _ {x \rightarrow 0 ^ {-}} f (x) = f (0) = b,</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} f (x) = \lim _ {x \rightarrow 0 ^ {+}} \frac {1 - \cos \sqrt {x}}{a x} \frac {1 - \cos \sqrt {x} \sim \frac {1}{2} (\sqrt {x}) ^ {2}}{\overline {{=}}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {x}{2}}{a x} = \frac {1}{2 a}.</equation>因此，<equation>b=\frac{1}{2a}</equation>即<equation>a b=\frac{1}{2}</equation>应选A.

---

**2013年第2题 | 选择题 | 4分 | 答案: C**

2. 函数<equation>f ( x )=\frac{| x |^{x}-1}{x ( x+1 ) \ln| x |}</equation>的可去间断点的个数为（    ）

A.0 B.1 C.2 D.3

答案: C

**解析:**解 由于 f(x)在 x=-1,0,1处没有定义且在其他点处连续，故 f(x)的间断点为 x=-1,0,1. 由于<equation>\lim _ {x \rightarrow 0} | x | ^ {x} = \lim _ {x \rightarrow 0} \mathrm {e} ^ {x \ln | x |} = \mathrm {e} ^ {\lim _ {x \rightarrow 0} x \ln | x |} = \mathrm {e} ^ {\lim _ {x \rightarrow 0} \frac {\ln | x |}{x ^ {- 1}} \xlongequal {\text {洛 必达}}} \mathrm {e} ^ {\lim _ {x \rightarrow 0} (- x)} = 1,</equation><equation>\lim _ {x \rightarrow 1} | x | ^ {x} = 1, \quad \lim _ {x \rightarrow - 1} | x | ^ {x} = 1,</equation>故<equation>\lim _ {x \rightarrow 0} \frac {\left| x \right| ^ {x} - 1}{x (x + 1) \ln | x |} = \lim _ {x \rightarrow 0} \frac {\left| x \right| ^ {x} - 1}{(x + 1) \ln (1 + \left| x \right| ^ {x} - 1)} = \lim _ {x \rightarrow 0} \frac {\left| x \right| ^ {x} - 1}{(x + 1) \left(\left| x \right| ^ {x} - 1\right)} = \lim _ {x \rightarrow 0} \frac {1}{x + 1} = 1,</equation><equation>\lim _ {x \rightarrow 1} \frac {\left| x \right| ^ {x} - 1}{x (x + 1) \ln | x |} \stackrel {\text {同 上}} {=} \lim _ {x \rightarrow 1} \frac {1}{x + 1} = \frac {1}{2},</equation><equation>\lim _ {x \rightarrow - 1} \frac {\left| x \right| ^ {x} - 1}{x (x + 1) \ln | x |} \stackrel {\text {同 上}} {=} \lim _ {x \rightarrow - 1} \frac {1}{x + 1} = \infty .</equation>因此，<equation>f ( x )</equation>的可去间断点为<equation>x=0,1. f ( x )</equation>共有2个可去间断点.应选C.

---

**2009年第1题 | 选择题 | 4分 | 答案: C**

1. 函数<equation>f(x)=\frac{x-x^{3}}{\sin \pi x}</equation>的可去间断点的个数为（    ）

A.1 B.2 C.3 D.无穷多个

答案: C

**解析:**解 因为当 k为整数时，<equation>\sin k\pi=0</equation>，所以 f(x）在 x=k（k为整数）时无定义，在其余点连续.当<equation>k-k^{3}\neq0</equation>时，即 k≠0，<equation>\pm1</equation>时，<equation>\lim _ {x \rightarrow k} \frac {x - x ^ {3}}{\sin \pi x} = \infty .</equation>x=k为f（x）的无穷间断点.

当<equation>k - k^{3} = 0</equation>时，即<equation>k = 0, \pm 1</equation>时，<equation>\lim_{x\to k}f(x)</equation>为<equation>\frac{0}{0}</equation>型未定式极限，可用洛必达法则求极限.<equation>\lim _ {x \rightarrow 0} \frac {x - x ^ {3}}{\sin \pi x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - 3 x ^ {2}}{\pi \cos \pi x} = \frac {1}{\pi},</equation><equation>\lim _ {x \rightarrow 1} \frac {x - x ^ {3}}{\sin \pi x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 1} \frac {1 - 3 x ^ {2}}{\pi \cos \pi x} = \frac {- 2}{- \pi} = \frac {2}{\pi},</equation><equation>\lim _ {x \rightarrow - 1} \frac {x - x ^ {3}}{\sin \pi x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow - 1} \frac {1 - 3 x ^ {2}}{\pi \cos \pi x} = \frac {- 2}{- \pi} = \frac {2}{\pi}.</equation>因此，<equation>f ( x )</equation>共有3个可去间断点，<equation>x=0</equation>，<equation>\pm 1.</equation>应选C.

---


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


#### 数列极限的概念与性质

**2022年第2题 | 选择题 | 5分 | 答案: A**

2. 已知<equation>a_{n}=\sqrt[n]{n}-\frac{(-1)^{n}}{n}(n=1,2,\cdots),</equation>，则<equation>\{a_{n}\}</equation>(    )

A. 有最大值，有最小值 B. 有最大值，没有最小值

C. 没有最大值，有最小值 D. 没有最大值，没有最小值

答案: A

**解析:**解（法一）<equation>\lim_{n\to \infty}a_{n}=\lim_{n\to \infty}\left[\sqrt[n]{n}-\frac{(-1)^{n}}{n}\right]=1.</equation>由极限的定义可知，在1的附近，例如区间（0.99，1.01）内，聚集了<equation>\left\{a_{n}\right\}</equation>除有限项以外的所有项，即存在正整数N，对 n > N，<equation>a_{n}\in</equation>（0.99，1.01）.注意到<equation>a_{1}=2>1.01, a_{2}=\sqrt{2}-\frac{1}{2}<0.99</equation>，故<equation>a_{1},a_{2}</equation>为落在该区间外的有限项中的两项.<equation>\left\{a_{n}\right\}</equation>的最值必在没有落入该区间内的有限项中取得.

因此，<equation>\left\{a_{n}\right\}</equation>必能取得最大值，也能取得最小值，且最大值不小于<equation>a_{1}</equation>，最小值不大于<equation>a_{2}</equation>.应选A.

（法二）由<equation>a_{n}</equation>的表达式可知，<equation>a_{n}=\left\{\begin{array}{ll}\sqrt[n]{n}+\frac{1}{n},&n=2k-1,\\ \sqrt[n]{n}-\frac{1}{n},&n=2k,\end{array}\right. k=1,2,\dots.</equation>考虑数列<equation>\left\{b_{n}\right\}</equation>，其中<equation>b_{n}=\sqrt[n]{n}.</equation>令<equation>f ( x )=x^{\frac{1}{x}}(x>0)</equation>，则<equation>f ( x )=\mathrm{e}^{\frac{1}{x}\ln x}.</equation>记<equation>g ( x )=\frac{\ln x}{x}.</equation>由于<equation>\mathrm{e}^{u}</equation>关于u单调增加，故g(x)的最大值对应f(x)的最大值.<equation>g^{\prime}(x)=\frac{1-\ln x}{x^{2}}</equation>当 0 < x < e时，<equation>g^{\prime}(x)>0,g(x)</equation>单调增加；当 x > e时，<equation>g^{\prime}(x)<0,g(x)</equation>单调减少.于是，<equation>x=\mathrm{e}</equation>为 g(x）的极大值点，也是最大值点.从而 x = e也是 f(x) 的最大值点.

当 n≥3时，<equation>\left\{b_{n}\right\}</equation>单调减少.于是，数列<equation>\left\{\sqrt[n]{n}+\frac{1}{n}\right\}_{n=2k-1}^{\infty}</equation>从 n=3开始单调减少，数列<equation>\left\{\sqrt[n]{n}+\frac{1}{n}\right\}_{n=2k}^{\infty}</equation>从 n=2开始单调减少.<equation>a_{1}=1+1=2, a_{3}=\sqrt[3]{3}+\frac{1}{3}.</equation>注意到<equation>\sqrt[3]{\frac{27}{9}}<\sqrt[3]{\frac{27}{8}}=\frac{3}{2}</equation>故<equation>a_{3}<\frac{3}{2}+\frac{1}{3}<2</equation>从而，<equation>a_{1}=2</equation>为<equation>\left\{\sqrt[n]{n}+\frac{1}{n}\right\}_{n=2k-1}^{\infty}</equation>的最大值，该数列单调减少趋于1，取不到最小值.

考虑数列<equation>\left\{\sqrt[n]{n} -\frac{1}{n}\right\}_{n = 2k}^{\infty}</equation>.

令 h(x）= x<equation>^{\frac{1}{x}}-\frac{1}{x}</equation>，则<equation>h ^ {\prime} (x) = \left(\mathrm {e} ^ {\frac {\ln x}{x}} - \frac {1}{x}\right) ^ {\prime} = \mathrm {e} ^ {\frac {\ln x}{x}} \cdot \frac {1 - \ln x}{x ^ {2}} + \frac {1}{x ^ {2}} = \frac {1}{x ^ {2}} \left[ x ^ {\frac {1}{x}} (1 - \ln x) + 1 \right].</equation>当 x充分大时，<equation>h^{\prime}(x)<0,h(x)</equation>单调减少，且<equation>\lim_{x\rightarrow +\infty}h(x)=1</equation>事实上，由于<equation>8>7.84=(2.8)^{2}>\mathrm{e}^{2},</equation><equation>x^{\frac{1}{x}}>1(x>1),1-\ln 8<1-\ln\mathrm{e}^{2}=-1</equation>，故<equation>h^{\prime}(8)<0</equation>.于是，当 n≥4时，<equation>\left\{a_{2n}\right\}</equation>单调减少，且<equation>a_{2n}</equation>均大于1.

另一方面，<equation>a _ {2 n} = \sqrt [ 2 n ]{2 n} - \frac {1}{2 n} < \sqrt [ 2 n ]{2 n} + \frac {1}{2 n} < \sqrt {2} + \frac {1}{2} < 2.</equation>于是，<equation>\left\{a_{2n}\right\}</equation>的最大值小于2.<equation>a_{2}=\sqrt{2}-\frac{1}{2}<1, a_{4}=\sqrt[4]{4}-\frac{1}{4}=\sqrt{2}-\frac{1}{4}>a_{2},</equation><equation>a _ {6} = \sqrt [ 6 ]{6} - \frac {1}{6} = \sqrt [ 3 ]{\sqrt {6}} - \frac {1}{6} > \sqrt [ 3 ]{2} - \frac {1}{6} > \sqrt [ 4 ]{2} - \frac {1}{6} > 1.</equation>因此，<equation>a_{2}</equation>为<equation>\left\{\sqrt[n]{n}-\frac{1}{n}\right\}^{\infty}</equation>的最小值.

综上所述，<equation>a_{1}</equation>为<equation>\left\{a_{n}\right\}</equation>的最大值，<equation>a_{2}</equation>为<equation>\left\{a_{n}\right\}</equation>的最小值.应选A.

---

**2015年第1题 | 选择题 | 4分 | 答案: D**

1. 设<equation>\{x_{n}\}</equation>是数列.下列命题中不正确的是（    ）

A. 若<equation>\lim_{n\rightarrow \infty}x_{n}=a</equation>，则<equation>\lim_{n\rightarrow \infty}x_{2n}=\lim_{n\rightarrow \infty}x_{2n+1}=a</equation>B. 若<equation>\lim_{x\rightarrow \infty}x_{2n}=\lim_{n\rightarrow \infty}x_{2n+1}=a</equation>，则<equation>\lim_{n\rightarrow \infty}x_{n}=a</equation>C. 若<equation>\lim_{n\rightarrow \infty}x_{n}=a</equation>，则<equation>\lim_{n\rightarrow \infty}x_{3n}=\lim_{n\rightarrow \infty}x_{3n+1}=a</equation>D. 若<equation>\lim_{n\rightarrow \infty}x_{3n}=\lim_{n\rightarrow \infty}x_{3n+1}=a</equation>，则<equation>\lim_{n\rightarrow \infty}x_{n}=a</equation>

答案: D

**解析:**解 令<equation>x_{k} = \left\{ \begin{array}{ll}0, & k = 3n \text{或} 3n + 1,\\ 1, & k = 3n + 2. \end{array} \right.</equation>n为正整数，则<equation>\lim_{n\to \infty}x_{3n} = \lim_{n\to \infty}x_{3n+1} = 0, \lim_{n\to \infty}x_{3n+2} = 1</equation>，从而<equation>\lim_{n\to \infty}x_{n}</equation>不存在，故选项D不正确.应选D.

若一个数列收敛于<equation>a</equation>，则它的任一子数列也收敛于<equation>a</equation>，故选项A、C均正确.

若<equation>\lim_{n\to \infty}x_{2n} = \lim_{n\to \infty}x_{2n + 1} = a</equation>，则由数列极限的定义可知，对任意给定的<equation>\varepsilon > 0</equation>，存在正整数<equation>N_{1}, N_{2}</equation>，使得<equation>\left| x _ {2 n} - a \right| < \varepsilon , n > N _ {1}, \quad \left| x _ {2 n + 1} - a \right| < \varepsilon , n > N _ {2}.</equation>令<equation>N=\max \left\{2 N_{1},2 N_{2}+1\right\}</equation>，则当 n > N时，<equation>|x_{n}-a|<\varepsilon</equation>.由数列极限的定义可知<equation>\lim_{n\to \infty}x_{n}=a</equation>，故选项B正确.

---

**2014年第1题 | 选择题 | 4分 | 答案: A**

1.<equation>\lim_{n\rightarrow \infty}a_{n}=a</equation>，且 a≠0，则当 n充分大时有（    ）

A.<equation>|a_{n}|>{\frac{|a|}{2}}</equation>B.<equation>|a_{n}|<{\frac{|a|}{2}}</equation>C.<equation>a_{n}>a-{\frac{1}{n}}</equation>D.<equation>a_{n}<a+{\frac{1}{n}}</equation>

答案: A

**解析:**解 由三角不等式<equation>|a| - |b| \leqslant |a - b| \leqslant |a| + |b|</equation>可知，<equation>|a_{n}| - |a| \leqslant |a_{n} - a|</equation>. 又由<equation>\lim_{n\to \infty}a_n = a</equation>知，对于任意给定的正数<equation>\varepsilon</equation>，总存在正整数<equation>N</equation>，使得当<equation>n > N</equation>时，不等式<equation>|a_{n} - a| < \varepsilon</equation>都成立. 因此，当<equation>n > N</equation>时，<equation>|a_{n}| - |a| \leqslant |a_{n} - a| < \varepsilon</equation>，<equation>\lim_{n\to \infty}|a_{n}| = |a| > 0</equation>由极限的定义可知，给定<equation>\varepsilon = \frac{|a|}{2} > 0</equation>，当<equation>n</equation>充分大时，有<equation>|a_{n}| - |a| < \frac{|a|}{2}</equation>，故<equation>|a_{n}| > \frac{|a|}{2}</equation>从而选项A正确，选项B不正确.应选A.

下面我们举例说明选项C、D不正确.

令<equation>a_{n}=1-\frac{1}{n}</equation>，则 a=1，可知选项C不正确；令<equation>a_{n}=1+\frac{1}{n}</equation>，则 a=1，可知选项D不正确.

---


#### 确定极限中的参数

**2021年第17题 | 解答题 | 10分**

17. (本题满分10分)

已知<equation>\lim_{x\to 0}\left[a\arctan \frac{1}{x}+(1+|x|)^{\frac{1}{x}}\right]</equation>存在，求 a的值.

**答案:**<equation>\frac {1}{\pi} \left(\frac {1}{\mathrm {e}} - \mathrm {e}\right).</equation>

**解析:**解分别计算<equation>\lim_{x\to 0^{-}}\left[\alpha\arctan \frac{1}{x}+(1+|x|)^{\frac{1}{x}}\right]</equation>和<equation>\lim_{x\to 0^{+}}\left[\alpha\arctan \frac{1}{x}+(1+|x|)^{\frac{1}{x}}\right].</equation><equation>\begin{array}{l} \lim _ {x \rightarrow 0 ^ {-}} \left[ \alpha \arctan \frac {1}{x} + (1 + | x |) ^ {\frac {1}{x}} \right] = \lim _ {x \rightarrow 0 ^ {-}} \alpha \arctan \frac {1}{x} + \lim _ {x \rightarrow 0 ^ {-}} (1 + | x |) ^ {\frac {1}{x}} \\ = - \frac {\pi}{2} \alpha + \lim _ {x \rightarrow 0 ^ {-}} (1 - x) ^ {\frac {1}{x}} \\ = - \frac {\pi}{2} \alpha + \lim _ {x \rightarrow 0 ^ {-}} (1 - x) ^ {- \frac {1}{x} \cdot (- 1)} \\ = - \frac {\pi}{2} \alpha + \frac {1}{\mathrm {e}}. \\ \end{array}</equation><equation>\begin{array}{l} \lim _ {x \rightarrow 0 ^ {+}} \left[ \alpha \arctan \frac {1}{x} + (1 + | x |) ^ {\frac {1}{x}} \right] = \lim _ {x \rightarrow 0 ^ {+}} \alpha \arctan \frac {1}{x} + \lim _ {x \rightarrow 0 ^ {+}} (1 + | x |) ^ {\frac {1}{x}} \\ = \frac {\pi}{2} \alpha + \lim _ {x \rightarrow 0 ^ {+}} (1 + x) ^ {\frac {1}{x}} \\ = \frac {\pi}{2} \alpha + \mathrm {e}. \\ \end{array}</equation>由于极限<equation>\lim_{x\to 0}\left[ \alpha \arctan \frac{1}{x}+(1+|x|)^{\frac{1}{x}} \right]</equation>存在，故<equation>- \frac {\pi}{2} \alpha + \frac {1}{\mathrm {e}} = \frac {\pi}{2} \alpha + \mathrm {e}.</equation>解得<equation>\alpha =\frac{1}{\pi}\left(\frac{1}{e}-e\right).</equation>

---

**2020年第15题 | 解答题 | 10分**

15. (本题满分10分）

已知 a,b为常数，若<equation>\left( 1+\frac{1}{n}\right)^{n}-\mathrm{e}</equation>与<equation>\frac{b}{n^{a}}</equation>在 n<equation>\to\infty</equation>时是等价无穷小，求 a,b.

**答案:**<equation>a = 1, b = - \frac {\mathrm {e}}{2}.</equation>

**解析:**解 由<equation>\left( 1+\frac{1}{n}\right)^{n}-\mathrm{e}</equation>与<equation>\frac{b}{n^{a}}</equation>在<equation>n\to \infty</equation>时是等价无穷小可知，<equation>a > 0,b\neq 0.</equation>并且，<equation>\begin{array}{l} \lim _ {n \rightarrow \infty} \frac {\left(1 + \frac {1}{n}\right) ^ {n} - e}{\frac {b}{n ^ {a}}} = \lim _ {n \rightarrow \infty} \frac {\mathrm {e} ^ {n \ln \left(1 + \frac {1}{n}\right)} - \mathrm {e}}{\frac {b}{n ^ {a}}} = \lim _ {n \rightarrow \infty} \frac {\mathrm {e} \left[ \mathrm {e} ^ {n \ln \left(1 + \frac {1}{n}\right)} - 1 \right]}{\frac {b}{n ^ {a}}} \\ \frac {\mathrm {e} ^ {n \ln \left(1 + \frac {1}{n}\right) - 1} - 1 \sim n \ln \left(1 + \frac {1}{n}\right) - 1}{\mathrm {e} \lim _ {n \rightarrow \infty} \frac {n \ln \left(1 + \frac {1}{n}\right) - 1}{\frac {b}{n ^ {a}}}} \\ \frac {t = \frac {1}{n}}{\mathrm {e} \lim _ {t \rightarrow 0 ^ {+}} \frac {\ln (1 + t)}{t} - 1} = \mathrm {e} \lim _ {t \rightarrow 0 ^ {+}} \frac {\ln (1 + t) - t}{b t ^ {a + 1}} \\ \frac {\ln (1 + t) = t - \frac {t ^ {2}}{2} + o \left(t ^ {2}\right)}{\mathrm {e} \lim _ {t \rightarrow 0 ^ {+}} \frac {- \frac {t ^ {2}}{2} + o \left(t ^ {2}\right)}{b t ^ {a + 1}}} = 1. \\ \end{array}</equation>当 a < 1时，<equation>\lim_{t\rightarrow 0^{+}}\frac{-\frac{t^{2}}{2}+o\left(t^{2}\right)}{b t^{a+1}}=0</equation>；当 a > 1时，<equation>\lim_{t\rightarrow 0^{+}}\frac{-\frac{t^{2}}{2}+o\left(t^{2}\right)}{b t^{a+1}}=\infty</equation>；当且仅当 a = 1时，<equation>\lim_{t\rightarrow 0^{+}}\frac{-\frac{t^{2}}{2}+o\left(t^{2}\right)}{b t^{2}}</equation>为非零常数.此时，e<equation>\lim_{t\rightarrow 0^{+}}\frac{-\frac{t^{2}}{2}+o\left(t^{2}\right)}{b t^{2}}=-\frac{\mathrm{e}}{2}\cdot \frac{1}{b}=1.</equation>解得 b = -<equation>\frac{\mathrm{e}}{2}.</equation>因此，a = 1,b = -<equation>\frac{\mathrm{e}}{2}.</equation>

---

**2019年第1题 | 选择题 | 4分 | 答案: C**

1. 当 x→0时，若 x-tanx与<equation>x^{k}</equation>是同阶无穷小，则 k=（    ）

A.1 B.2 C.3 D.4

答案: C

**解析:**解 首先，由于当 x→0时，<equation>x-\tan x\to 0</equation>，而<equation>\lim_{x\to 0}\frac{x-\tan x}{x^{k}}</equation>为非零常数，故 k > 0.下面用两种方法讨论<equation>\lim_{x\to 0}\frac{x-\tan x}{x^{k}}.</equation>（法一）由于<equation>\tan x=x+\frac{x^{3}}{3}+o\left(x^{3}\right)</equation>，故<equation>\lim _ {x \rightarrow 0} \frac {x - \tan x}{x ^ {k}} = \lim _ {x \rightarrow 0} \frac {- \frac {x ^ {3}}{3} + o \left(x ^ {3}\right)}{x ^ {k}}.</equation>当 k > 3时，该极限为<equation>\infty</equation>；当0 < k < 3时，该极限为0；当 k=3时，该极限为<equation>-\frac{1}{3}.</equation>于是，<equation>x-\tan x</equation>与<equation>x^{3}</equation>是同阶无穷小，k=3.

因此，应选C.

（法二）利用洛必达法则讨论<equation>\lim_{x\to 0}\frac{x-\tan x}{x^{k}}.</equation><equation>\lim_{x\to 0}\frac{x-\tan x}{x^{k}}\overset{\mathrm{洛必达}}{=}\lim_{x\to 0}\frac{1-\sec^{2}x}{kx^{k-1}}=\lim_{x\to 0}\frac{-\tan^{2}x}{kx^{k-1}}\overset{\mathrm{tan}x\sim x}{=}\lim_{x\to 0}\frac{-x^{2}}{kx^{k-1}}.</equation>当 k > 3时，该极限为<equation>\infty</equation>；当 0 < k < 3时，该极限为0；当 k=3时，该极限为<equation>-\frac{1}{3}.</equation>于是，<equation>x-\tan x</equation>与<equation>x^{3}</equation>是同阶无穷小， k=3.

因此，应选C.

---

**2018年第15题 | 解答题 | 10分**

15. (本题满分10分）已知实数 a,b满足<equation>\lim_{x\rightarrow +\infty}[(ax+b)\mathrm{e}^{\frac{1}{x}}-x]=2</equation>，求 a,b.

**答案:**## a=1,b=1.

**解析:**解（法一）令<equation>t=\frac{1}{x}</equation>，则<equation>\lim _ {x \rightarrow + \infty} [ (a x + b) \mathrm {e} ^ {\frac {1}{x}} - x ] = \lim _ {t \rightarrow 0 ^ {+}} \left[ \left(\frac {a}{t} + b\right) \mathrm {e} ^ {t} - \frac {1}{t} \right] = \lim _ {t \rightarrow 0 ^ {+}} \frac {(a + b t) \mathrm {e} ^ {t} - 1}{t} = 2.</equation>由于<equation>t\to 0^{+}</equation>，而<equation>\lim_{t\to 0^{+}}\frac{(a+bt)\mathrm{e}^{t}-1}{t}=2</equation>，故<equation>\lim_{t\to 0^{+}}[(a+bt)\mathrm{e}^{t}-1]=a-1=0.</equation>，<equation>a=1.</equation>将 a=1 代入<equation>\lim_{t\to 0^{+}}\frac{(a+bt)\mathrm{e}^{t}-1}{t}</equation>，可得<equation>\begin{array}{l} \lim _ {t \rightarrow 0 ^ {+}} \frac {(a + b t) \mathrm {e} ^ {t} - 1}{t} = \lim _ {t \rightarrow 0 ^ {+}} \frac {(1 + b t) \mathrm {e} ^ {t} - 1}{t} \xlongequal {\text {洛必达}} \lim _ {t \rightarrow 0 ^ {+}} [ (1 + b t) \mathrm {e} ^ {t} + b \mathrm {e} ^ {t} ] \\ = \lim _ {t \rightarrow 0 ^ {+}} (1 + b + b t) \mathrm {e} ^ {t} = 1 + b = 2. \\ \end{array}</equation>于是，<equation>b=1.</equation>因此，<equation>a=1</equation><equation>b=1.</equation>（法二）利用泰勒公式.

当<equation>x\to +\infty</equation>时，<equation>\frac{1}{x}\to 0^{+}</equation>.于是，<equation>\mathrm{e}^{\frac{1}{x}}=1+\frac{1}{x}+o\left(\frac{1}{x}\right).</equation><equation>\begin{array}{l} \lim _ {x \rightarrow + \infty} [ (a x + b) \mathrm {e} ^ {\frac {1}{x}} - x ] = \lim _ {x \rightarrow + \infty} \left\{(a x + b) \left[ 1 + \frac {1}{x} + o \left(\frac {1}{x}\right)\right] - x \right\} \\ = \lim _ {x \rightarrow + \infty} \left[ a x + b + a + \frac {b}{x} + o (1) + o \left(\frac {1}{x}\right) - x \right] \\ = \lim _ {x \rightarrow + \infty} [ (a - 1) x + a + b ]. \\ \end{array}</equation>当且仅当<equation>\left\{\begin{array}{l l}a-1=0,\\ a+b=2,\end{array}\right.</equation>即<equation>\left\{\begin{array}{l l}a=1,\\ b=1\end{array}\right.</equation>时，<equation>\lim_{x\to +\infty}[(a-1)x+a+b]=2.</equation>因此，<equation>a=1</equation><equation>b=1.</equation>

---

**2015年第15题 | 解答题 | 10分**

15. (本题满分10分）

设函数<equation>f(x)=x+a\ln(1+x)+bx\sin x,g(x)=kx^{3}.</equation>若 f(x)与 g(x)在<equation>x\rightarrow0</equation>时是等价无穷小，求 a,b,k的值.

**答案:**<equation>(1 5) a = - 1, b = - \frac {1}{2}, k = - \frac {1}{3}.</equation>

**解析:**（法一）首先，<equation>k\neq 0.</equation>由于 g(x）中 x的次数为3，故可考虑写出 f(x)在 x=0处的3阶泰勒公式由<equation>\ln (1 + x) = x - \frac {x ^ {2}}{2} + \frac {x ^ {3}}{3} + o \left(x ^ {3}\right), \quad \sin x = x - \frac {x ^ {3}}{3 !} + o \left(x ^ {3}\right),</equation>可得<equation>f (x) = x + a x - \frac {a x ^ {2}}{2} + \frac {a x ^ {3}}{3} + b x ^ {2} + o \left(x ^ {3}\right) = (a + 1) x + \left(b - \frac {a}{2}\right) x ^ {2} + \frac {a}{3} x ^ {3} + o \left(x ^ {3}\right).</equation>记<equation>I=\lim_{x\to 0}\frac{f(x)}{g(x)}=\lim_{x\to 0}\frac{(a+1)x+\left(b-\frac{a}{2}\right)x^{2}+\frac{a}{3}x^{3}+o\left(x^{3}\right)}{kx^{3}}.</equation>由等价无穷小量的定义知 I=1.

于是，<equation>\left\{\begin{array}{l l}a+1=0,\\ b-\frac{a}{2}=0,\end{array}\right.</equation>否则 I=<equation>\infty</equation>.解得 a=-1，b=-<equation>\frac{1}{2}</equation>.又因为 I=1，所以<equation>\frac{a}{3}=k</equation>，k=-<equation>\frac{1}{3}</equation>.

综上所述， a=-1，b=-<equation>\frac{1}{2}</equation>，k=-<equation>\frac{1}{3}</equation>（法二）记<equation>I=\lim_{x\to 0}\frac{f(x)}{g(x)}.</equation>由等价无穷小量的定义知<equation>I=1.</equation>下面使用洛必达法则来讨论I.

首先，<equation>k\neq 0</equation>当<equation>k\neq 0</equation>时，<equation>\lim_{x\to 0}\frac{f(x)}{g(x)}</equation>是<equation>\frac{0}{0}</equation>型未定式.由洛必达法则得，<equation>I = \lim _ {x \rightarrow 0} \frac {x + a \ln (1 + x) + b x \sin x}{k x ^ {3}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 + \frac {a}{1 + x} + b \sin x + b x \cos x}{3 k x ^ {2}}.</equation>由于<equation>\lim _ {x \rightarrow 0} \left(1 + \frac {a}{1 + x} + b \sin x + b x \cos x\right) = 1 + a,</equation>故若<equation>1 + a\neq 0</equation>，则<equation>I = \infty</equation>，与题设矛盾.因此，<equation>a = -1.</equation>代入<equation>a = -1</equation>，继续对（1）式使用洛必达法则，

(1)<equation>\text {式} \stackrel {\text {洛必达}} {=} \lim _ {x \rightarrow 0} \frac {\frac {1}{(1 + x) ^ {2}} + b \cos x + b \cos x - b x \sin x}{6 k x}.</equation>由于<equation>\lim _ {x \rightarrow 0} \left[ \frac {1}{(1 + x) ^ {2}} + 2 b \cos x - b x \sin x \right] = 1 + 2 b,</equation>故若<equation>1 + 2b\neq 0</equation>，则<equation>I = \infty</equation>，与题设矛盾.因此，<equation>b = -\frac{1}{2}</equation>代入 b=-<equation>\frac{1}{2}</equation>，继续对（2）式使用洛必达法则，

(2)<equation>\text {式} \stackrel {\text {洛必达}} {=} \lim _ {x \rightarrow 0} \frac {- \frac {2}{(1 + x) ^ {3}} + \sin x + \frac {1}{2} \sin x + \frac {1}{2} x \cos x}{6 k} = \frac {- 2}{6 k} = 1.</equation>因此，<equation>k = -\frac{1}{3}</equation>综上所述，<equation>a=-1</equation><equation>b=-\frac{1}{2}</equation><equation>k=-\frac{1}{3}.</equation>

---

**2014年第3题 | 选择题 | 4分 | 答案: D**

3. 设 p(x)=a+bx+cx²+dx³. 当 x→0时，若 p(x)-tanx是比<equation>x^{3}</equation>高阶的无穷小量，则下列选项中错误的是（    )

A. a=0 B. b=1 C. c=0 D. d=<equation>\frac{1}{6}</equation>

答案: D

**解析:**解（法一）写出<equation>\tan x</equation>在<equation>x=0</equation>处的三阶泰勒公式.<equation>\tan x = \left(\tan x\right) ^ {\prime} \left| _ {x = 0} \cdot x + \frac {1}{2 !} \left(\tan x\right) ^ {\prime \prime} \right| _ {x = 0} \cdot x ^ {2} + \frac {1}{3 !} \left(\tan x\right) ^ {\prime \prime \prime} \left| _ {x = 0} \cdot x ^ {3} + o \left(x ^ {3}\right). \right.</equation>又由于<equation>(\tan x) ^ {\prime} = \sec^ {2} x, \quad (\tan x) ^ {\prime \prime} = 2 \sec x \cdot \sec x \tan x = 2 \sec^ {2} x \tan x,</equation><equation>(\tan x) ^ {\prime \prime \prime} = 4 \sec x \cdot \sec x \tan x \cdot \tan x + 2 \sec^ {2} x \cdot \sec^ {2} x,</equation>故<equation>\tan x = x + \frac {1}{3} x ^ {3} + o \left(x ^ {3}\right).</equation>由题设知，<equation>p (x) - \tan x = a + (b - 1) x + c x ^ {2} + \left(d - \frac {1}{3}\right) x ^ {3} + o \left(x ^ {3}\right) = o \left(x ^ {3}\right).</equation>从而<equation>a = 0, \quad b - 1 = 0, \quad c = 0, \quad d - \frac {1}{3} = 0.</equation>因此，<equation>a = 0, \quad b = 1, \quad c = 0, \quad d = \frac {1}{3}.</equation>（法二）由已知条件知

从而选项 D 不正确.应选 D.<equation>\begin{array}{l} 0 = \lim _ {x \rightarrow 0} \frac {\left(a + b x + c x ^ {2} + d x ^ {3}\right) - \tan x}{x ^ {3}} (\mathrm {分 母 趋 于 零 , 故 分 子 也 趋 于 零 , 从 而} a = 0) \\ = \lim _ {x \rightarrow 0} \frac {b x + c x ^ {2} + d x ^ {3} - \tan x}{x ^ {3}} \\ \mathrm {洛必达} \lim _ {x \rightarrow 0} \frac {b + 2 c x + 3 d x ^ {2} - \sec^ {2} x}{3 x ^ {2}} (\mathrm {分 母 趋 于 零 , 故 分 子 也 趋 于 零 , 从 而} b = 1) \\ \mathrm {洛必达} \lim _ {x \rightarrow 0} \frac {2 c + 6 d x - 2 \sec^ {2} x \tan x}{6 x} (\mathrm {同 上 可 知} c = 0) \\ \mathrm {洛必达} \lim _ {x \rightarrow 0} \frac {6 d - 4 \sec^ {2} x \tan^ {2} x - 2 \sec^ {4} x}{6} = \frac {6 d - 2}{6}. \\ \end{array}</equation>或者在得到<equation>c = 0</equation>后，利用等价无穷小替换<equation>\tan x\sim x</equation>，得<equation>\text {原 式} = \lim _ {x \rightarrow 0} \frac {6 d x - 2 \sec^ {2} x \tan x}{6 x} = d - \lim _ {x \rightarrow 0} \frac {2 \sec^ {2} x \tan x}{6 x} = d - \frac {1}{3}.</equation>解得<equation>d = \frac{1}{3}</equation>因此，<equation>a=0,b=1,c=0,d=\frac{1}{3}</equation>应选D.

---

**2013年第15题 | 解答题 | 10分**

15. (本题满分10分)

当<equation>x\to0</equation>时，<equation>1-\cos x\cdot\cos 2x\cdot\cos 3x</equation>与<equation>ax^{n}</equation>为等价无穷小量，求 n与 a的值.

**答案:**(15) n=2, a=7.

**解析:**解记<equation>I=\lim_{x\to 0}\frac{1-\cos x\cos 2x\cos 3x}{a x^{n}}.</equation>由题设，<equation>I=1.</equation>（法一）分别考虑<equation>\cos x,\cos 2x,\cos 3x</equation>的二阶泰勒公式，<equation>\cos x = 1 - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right),</equation><equation>\cos 2 x = 1 - \frac {1}{2} (2 x) ^ {2} + o \left(\left(2 x\right) ^ {2}\right) = 1 - 2 x ^ {2} + o \left(x ^ {2}\right),</equation><equation>\cos 3 x = 1 - \frac {1}{2} (3 x) ^ {2} + o \left(\left(3 x\right) ^ {2}\right) = 1 - \frac {9}{2} x ^ {2} + o \left(x ^ {2}\right).</equation>由于<equation>o\left(x^{2}\right)\cdot x^{n}</equation>仍为<equation>o\left(x^{2}\right)\left(n\geqslant 0\right)</equation>，故<equation>\begin{array}{l} \cos x \cos 2 x \cos 3 x = \left(1 - \frac {1}{2} x ^ {2}\right) \left(1 - 2 x ^ {2}\right) \left(1 - \frac {9}{2} x ^ {2}\right) + o \left(x ^ {2}\right) \\ = 1 - \frac {1}{2} x ^ {2} - 2 x ^ {2} - \frac {9}{2} x ^ {2} + o \left(x ^ {2}\right). \\ \end{array}</equation>代人I，得<equation>\begin{array}{l} I = \lim _ {x \rightarrow 0} \frac {1 - \left[ 1 - \frac {1}{2} x ^ {2} - 2 x ^ {2} - \frac {9}{2} x ^ {2} + o \left(x ^ {2}\right)\right]}{a x ^ {n}} \\ = \lim _ {x \rightarrow 0} \frac {\frac {1}{2} x ^ {2} + 2 x ^ {2} + \frac {9}{2} x ^ {2} + o \left(x ^ {2}\right)}{a x ^ {n}} = \lim _ {x \rightarrow 0} \frac {7 x ^ {2} + o \left(x ^ {2}\right)}{a x ^ {n}}. \\ \end{array}</equation>由于<equation>\lim _ {x \rightarrow 0} \frac {7 x ^ {2} + o \left(x ^ {2}\right)}{a x ^ {n}} = \frac {7}{a} \lim _ {x \rightarrow 0} \frac {x ^ {2}}{x ^ {n}} \left[ 1 + \frac {o \left(x ^ {2}\right)}{7 x ^ {2}} \right] = \frac {7}{a} \lim _ {x \rightarrow 0} \frac {x ^ {2}}{x ^ {n}},</equation>故当 n > 2时，<equation>\lim_{x\to 0}\frac{7x^{2}+o\left(x^{2}\right)}{ax^{n}}=\infty</equation>；当 n < 2时，<equation>\lim_{x\to 0}\frac{7x^{2}+o\left(x^{2}\right)}{ax^{n}}=0</equation>；而当 n = 2时，<equation>\lim_{x\to 0}\frac{7x^{2}+o\left(x^{2}\right)}{ax^{2}}</equation><equation>= \frac{7}{a}</equation>.因此，由 I = 1得，<equation>\frac{7}{a}=1</equation>，a=7.

综上所述，<equation>n=2</equation>a=7.

（法二）我们先利用三角函数的积化和差公式将<equation>\cos x\cos 2x\cos 3x</equation>作恒等变形，然后再利用洛必达法则来计算 I.

由积化和差公式，我们有<equation>\begin{array}{l} \cos x \cos 2 x \cos 3 x = \frac {1}{2} (\cos 4 x + \cos 2 x) \cos 2 x = \frac {1}{2} \cos 4 x \cos 2 x + \frac {1}{2} \cos^ {2} 2 x \\ = \frac {1}{4} (\cos 6 x + \cos 2 x) + \frac {1}{4} \cos 4 x + \frac {1}{4} \\ = \frac {1}{4} (1 + \cos 2 x + \cos 4 x + \cos 6 x). \\ \end{array}</equation>从而，<equation>I = \lim _ {x \rightarrow 0} \frac {\frac {3}{4} - \frac {1}{4} \left(\cos 2 x + \cos 4 x + \cos 6 x\right)}{a x ^ {n}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\frac {1}{4} \left(2 \sin 2 x + 4 \sin 4 x + 6 \sin 6 x\right)}{n a x ^ {n - 1}}.</equation>由于<equation>\lim_{x\to 0}(2\sin 2x+4\sin 4x+6\sin 6x)=0</equation>，而 I=1，故<equation>\lim_{x\to 0}nax^{n-1}=0</equation>，于是 n > 1.否则当 n≤1时， I=0，与 I=1矛盾.

当<equation>n > 1</equation>时，继续使用洛必达法则可得，<equation>I \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\cos 2 x + 4 \cos 4 x + 9 \cos 6 x}{n (n - 1) a x ^ {n - 2}} = \lim _ {x \rightarrow 0} \frac {1 4}{n (n - 1) a x ^ {n - 2}}.</equation>若 I存在且等于1，则 n-2=0.否则当 n-2<0时，I=0；当 n-2>0时，<equation>I=\infty</equation>.当 n=2时，<equation>I=\frac{14}{2a}=1</equation>，a=7.

综上所述，n=2,a=7.

（法三）使用添项、减项的技巧对<equation>I</equation>进行恒等变形.<equation>\begin{array}{l} I = \lim _ {x \rightarrow 0} \frac {1 - \cos x + \cos x - \cos x \cos 2 x + \cos x \cos 2 x - \cos x \cos 2 x \cos 3 x}{a x ^ {n}} \\ = \lim _ {x \rightarrow 0} \left[ \frac {1 - \cos x}{a x ^ {n}} + \frac {\cos x (1 - \cos 2 x)}{a x ^ {n}} + \frac {\cos x \cos 2 x (1 - \cos 3 x)}{a x ^ {n}} \right]. \\ \mathrm {虑} \lim _ {x \rightarrow 0} \frac {1 - \cos x}{\cos x (1 - \cos 2 x)}. \lim _ {x \rightarrow 0} \frac {\cos x \cos 2 x (1 - \cos 3 x)}{\cos x \cos 2 x (1 - \cos 3 x)}. \\ \end{array}</equation>分别考虑<equation>\lim_{x\to 0}\frac{1-\cos x}{ax^{n}}, \lim_{x\to 0}\frac{\cos x(1-\cos 2x)}{ax^{n}}, \lim_{x\to 0}\frac{\cos x\cos 2x(1-\cos 3x)}{ax^{n}}.</equation>由于当<equation>x\to 0</equation>时，<equation>\cos x\to 1,1 - \cos x\sim \frac{x^2}{2}</equation>，故这三个极限均仅当<equation>n = 2</equation>时存在且不为零.当<equation>n > 2</equation>时，极限为<equation>\infty</equation>；当<equation>n < 2</equation>时，极限为零.

当 n=2时，<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {1 - \cos x}{a x ^ {2}} \xlongequal {1 - \cos x \sim \frac {x ^ {2}}{2}} \frac {1}{2 a}, \quad \lim _ {x \rightarrow 0} \frac {\cos x (1 - \cos 2 x)}{a x ^ {2}} \xlongequal {1 - \cos 2 x \sim \frac {(2 x) ^ {2}}{2}} \frac {2}{a}, \\ \lim _ {x \rightarrow 0} \frac {\cos x \cos 2 x (1 - \cos 3 x)}{a x ^ {2}} \xlongequal {1 - \cos 3 x \sim \frac {(3 x) ^ {2}}{2}} \frac {9}{2 a}. \\ I = \frac {1}{2 a} + \frac {2}{a} + \frac {9}{2 a} = \frac {7}{a} = 1. \\ \end{array}</equation>因此，<equation>n=2</equation>，<equation>a=7.</equation>

---

**2011年第1题 | 选择题 | 4分 | 答案: C**

1. 已知当<equation>x\to0</equation>时，函数<equation>f(x)=3\sin x-\sin 3x</equation>与<equation>cx^{k}</equation>是等价无穷小量，则（    )

A. k=1,c=4 B. k=1,c=-4 C. k=3,c=4 D. k=3,c=-4

答案: C

**解析:**解 由题设知，<equation>c\neq 0,k > 0.</equation>记<equation>I = \lim_{x\to 0}\frac{f(x)}{cx^{k}}</equation>，则由等价无穷小量的定义知，<equation>I = 1.</equation>由于<equation>\sin x=x-\frac{1}{3!} x^{3}+o\left(x^{3}\right)</equation>，故<equation>\sin 3x=3x-\frac{1}{3!}\left(3x\right)^{3}+o\left(x^{3}\right).</equation>因此，<equation>1 = \lim _ {x \rightarrow 0} \frac {3 \sin x - \sin 3 x}{c x ^ {k}} = \lim _ {x \rightarrow 0} \frac {3 x - \frac {1}{2} x ^ {3} - 3 x + \frac {2 7}{6} x ^ {3} + o \left(x ^ {3}\right)}{c x ^ {k}} = \lim _ {x \rightarrow 0} \frac {4 x ^ {3} + o \left(x ^ {3}\right)}{c x ^ {k}}.</equation>下面讨论使<equation>\lim_{x\to 0}\frac{4x^{3}+o\left(x^{3}\right)}{cx^{k}}=1</equation>成立的k，c的值.

由于<equation>I = \frac {4}{c} \lim _ {x \rightarrow 0} \frac {x ^ {3}}{x ^ {k}} \left[ 1 + \frac {o \left(x ^ {3}\right)}{4 x ^ {3}} \right] = \frac {4}{c} \lim _ {x \rightarrow 0} \frac {x ^ {3}}{x ^ {k}},</equation>故当<equation>c\neq0,k<3</equation>时，<equation>I=0</equation>；当<equation>c\neq0,k>3</equation>时，<equation>I=\infty</equation>；只有当<equation>c\neq0,k=3</equation>时，<equation>I=\frac{4}{c}=1.</equation>因此，<equation>k=3,c=4</equation>应选C.

---

**2010年第1题 | 选择题 | 4分 | 答案: C**

1. 若<equation>\lim_{x\rightarrow 0}\left[ \frac{1}{x}-\left( \frac{1}{x}-a\right) \mathrm{e}^{x}\right] =1</equation>，则 a等于（    ）

A.0 B.1 C.2 D.3

答案: C

**解析:**（法一）由于<equation>\lim _ {x \rightarrow 0} \left[ \frac {1}{x} - \left(\frac {1}{x} - a\right) \mathrm {e} ^ {x} \right] = \lim _ {x \rightarrow 0} \frac {1 - (1 - a x) \mathrm {e} ^ {x}}{x} \xlongequal {\text {洛 必达}} \lim _ {x \rightarrow 0} \frac {a \mathrm {e} ^ {x} - (1 - a x) \mathrm {e} ^ {x}}{1} = a - 1,</equation>故由已知条件知<equation>a - 1 = 1.</equation>因此，<equation>a = 2.</equation>应选C.

（法二）由于当<equation>x\to 0</equation>时，<equation>\mathrm{e}^{x} - 1\sim x</equation>，故<equation>\lim _ {x \rightarrow 0} \left[ \frac {1}{x} - \left(\frac {1}{x} - a\right) \mathrm {e} ^ {x} \right] = \lim _ {x \rightarrow 0} \left(\frac {1 - \mathrm {e} ^ {x}}{x} + a \mathrm {e} ^ {x}\right) = - 1 + a = 1.</equation>解得 a=2.应选C.

---

**2009年第2题 | 选择题 | 4分 | 答案: A**

2. 当<equation>x\to0</equation>时，<equation>f(x)=x-\sin ax</equation>与<equation>g(x)=x^{2}\ln(1-bx)</equation>是等价无穷小量，则（    )

A. a=1,b=-<equation>\frac{1}{6}</equation>B. a=1,b=<equation>\frac{1}{6}</equation>C. a=-1,b=-<equation>\frac{1}{6}</equation>D. a=-1,b=<equation>\frac{1}{6}</equation>

答案: A

**解析:**由于<equation>x\to 0</equation>时，<equation>f(x)</equation>与<equation>g(x)</equation>是等价无穷小量，故<equation>\begin{aligned} 1 &= \lim _ {x \rightarrow 0} \frac {f (x)}{g (x)} = \lim _ {x \rightarrow 0} \frac {x - \sin a x}{x ^ {2} \ln (1 - b x)} \xlongequal {\ln (1 - b x) \sim (- b x)} \lim _ {x \rightarrow 0} \frac {x - \sin a x}{- b x ^ {3}} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - a \cos a x}{- 3 b x ^ {2}} &= I _ {1}. \end{aligned}</equation>由于<equation>\lim_{x\to 0}(-3bx^2) = 0</equation>，故若<equation>I_{1}</equation>存在，则<equation>\lim_{x\to 0}(1 - a\cos ax) = 0</equation>，从而<equation>a = 1.</equation>代人 a=1，得<equation>I _ {1} = \lim _ {x \rightarrow 0} \frac {1 - \cos x}{- 3 b x ^ {2}} \xlongequal {\text {一}} \frac {1 - \cos x \sim \frac {x ^ {2}}{2}}{\lim _ {x \rightarrow 0} \frac {\frac {x ^ {2}}{2}}{- 3 b x ^ {2}}} = - \frac {1}{6 b}.</equation>当<equation>b = -\frac{1}{6}</equation>时，<equation>I_{1}</equation>存在且等于1.

因此，当<equation>a = 1,b = -\frac{1}{6}</equation>时，<equation>\lim_{x\to 0}\frac{f(x)}{g(x)} = 1,f(x)</equation>与<equation>g(x)</equation>是<equation>x\to 0</equation>时的等价无穷小量.应选A.

---


#### 数列极限的计算

**2019年第9题 | 填空题 | 4分**

9. lim

**解析:**解注意到<equation>\frac{1}{n(n+1)}=\frac{1}{n}-\frac{1}{n+1}</equation>，故<equation>\frac {1}{1 \cdot 2} + \frac {1}{2 \cdot 3} + \dots + \frac {1}{n (n + 1)} = 1 - \frac {1}{2} + \frac {1}{2} - \frac {1}{3} + \dots + \frac {1}{n} - \frac {1}{n + 1} = 1 - \frac {1}{n + 1}.</equation>因此，

原极限<equation>= \lim_{n\to \infty}\left(1 - \frac{1}{n + 1}\right)^{n} = \lim_{n\to \infty}\left(1 - \frac{1}{n + 1}\right)^{-(n + 1)\cdot \frac{n}{-(n + 1)}} = \mathrm{e}^{-1}.</equation>

---


#### 数列敛散性的判定

**2018年第19题 | 解答题 | 10分**

19. (本题满分10分）

设数列<equation>\{x_{n}\}</equation>满足：<equation>x_{1}>0,x_{n}\mathrm{e}^{x_{n+1}}=\mathrm{e}^{x_{n}}-1(n=1,2,\cdots).</equation>证明<equation>\{x_{n}\}</equation>收敛，并求<equation>\lim_{n\rightarrow \infty}x_{n}.</equation>

**解析:**解 由<equation>x_{n}\mathrm{e}^{x_{n + 1}} = \mathrm{e}^{x_{n}} - 1(n = 1,2,\dots)</equation>可得，<equation>x _ {n + 1} = \ln \left(\frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n}}\right).</equation>先用数学归纳法证明对所有的正整数 n，都有<equation>x_{n} > 0.</equation>首先，<equation>x_{1} > 0.</equation>假设当<equation>n=k</equation>时，<equation>x_{k} > 0</equation>注意到当<equation>x > 0</equation>时，<equation>\mathrm{e}^{x}-1 > x</equation>从而<equation>\frac{\mathrm{e}^{x}-1}{x} > 1.</equation>于是，<equation>x _ {k + 1} = \ln \left(\frac {\mathrm {e} ^ {x _ {k}} - 1}{x _ {k}}\right) > \ln 1 = 0.</equation>由数学归纳法可知，对所有的正整数 n，都有<equation>x_{n} > 0.</equation>因此，数列<equation>\{x_{n}\}</equation>有下界.

下面用两种方法证明数列<equation>\{x_{n}\}</equation>单调减少，即<equation>x_{n+1} < x_{n} ( n=1,2,\dots).</equation>（法一）由<equation>x_{n}\mathrm{e}^{x_{n}+1}=\mathrm{e}^{x_{n}}-1</equation>可知，<equation>\mathrm {e} ^ {x _ {n + 1}} = \frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n}} = \frac {\mathrm {e} ^ {x _ {n}} - \mathrm {e} ^ {0}}{x _ {n} - 0} \frac {\text {拉 格 朗 日}}{\text {中 值 定 理}} \mathrm {e} ^ {\xi_ {n}},</equation>其中<equation>\xi_{n}\in (0,x_{n})</equation>由于<equation>\mathrm{e}^{x}</equation>单调增加，故由<equation>\mathrm{e}^{x_{n+1}}=\mathrm{e}^{\xi_{n}}<\mathrm{e}^{x_{n}}</equation>可得<equation>x_{n+1}<x_{n}</equation>，即数列<equation>\left\{x_{n}\right\}</equation>单调减少.

（法二）<equation>x _ {n + 1} - x _ {n} = \ln \left(\frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n}}\right) - x _ {n} = \ln \left(\frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n} \mathrm {e} ^ {x _ {n}}}\right).</equation>记<equation>f ( x )=\mathrm{e}^{x}-1-x\mathrm{e}^{x}</equation>，则<equation>f^{\prime}(x)=\mathrm{e}^{x}-\mathrm{e}^{x}-x\mathrm{e}^{x}=-x\mathrm{e}^{x}.</equation>当<equation>x > 0</equation>时，<equation>f^{\prime}(x) < 0,f(x)</equation>在<equation>[0,+\infty)</equation>上单调减少，于是，<equation>f(x) < f(0)=0.</equation>从而，当<equation>x > 0</equation>时，<equation>\frac {\mathrm {e} ^ {x} - 1}{x \mathrm {e} ^ {x}} - 1 = \frac {\mathrm {e} ^ {x} - 1 - x \mathrm {e} ^ {x}}{x \mathrm {e} ^ {x}} < 0,</equation>即<equation>\frac{\mathrm{e}^{x}-1}{x\mathrm{e}^{x}}<1.</equation>又因为对所有的正整数 n ，都有<equation>x_{n} > 0</equation>，所以<equation>\ln \left(\frac{\mathrm{e}^{x_{n}}-1}{x_{n}\mathrm{e}^{x_{n}}}\right) < \ln 1=0</equation>，即<equation>x_{n+1}-x_{n} < 0.</equation>因此，数列<equation>\left\{x_{n}\right\}</equation>单调减少.

由单调有界准则可知，数列<equation>\{x_{n}\}</equation>收敛.由于对所有的正整数n，都有<equation>x_{n} > 0</equation>，故<equation>\lim_{n\to \infty}x_{n}=a\geqslant 0.</equation>对<equation>x_{n}\mathrm{e}^{x_{n+1}}=\mathrm{e}^{x_{n}}-1</equation>两端同时令<equation>n\to \infty</equation>，可得<equation>a\mathrm{e}^{a}=\mathrm{e}^{a}-1.</equation>由前面的结果可知，<equation>x=0</equation>是<equation>f(x)=\mathrm{e}^{x}-1-x\mathrm{e}^{x}</equation>在<equation>[0,+\infty)</equation>上的唯一零点.因此，<equation>a=0</equation>即<equation>\lim_{n\to \infty}x_{n}=0.</equation>

---


### 一元函数微分学