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


