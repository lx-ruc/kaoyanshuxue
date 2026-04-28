# 数学三


## 高等数学


### 函数、极限、连续


#### 无穷小量

**2025年第1题 | 选择题 | 5分 | 答案: C**
1. 在<equation>x \rightarrow 0^{+}</equation>时，下列无穷小量中与 x等价的是（    )

A.<equation>\mathrm{e}^{-\sin x}-1</equation>B.<equation>\sqrt{x+1}-\cos x</equation>C.<equation>1-\cos \sqrt{2 x}</equation>D.<equation>1-\frac{\ln(1+x)}{x}</equation>
答案: C
**解析: **解分别记四个选项中的函数为<equation>f_{i}(x)(i = 1,2,3,4)</equation>，计算<equation>\lim_{x\to 0^{+}}\frac{f_{i}(x)}{x}</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {f _ {1} (x)}{x} = \lim _ {x \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {- \sin x} - 1}{x} \xlongequal {\mathrm {e} ^ {- \sin x} - 1 \sim - \sin x} \lim _ {x \rightarrow 0 ^ {+}} \frac {- \sin x}{x} = - 1.</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {f _ {2} (x)}{x} = \lim _ {x \rightarrow 0 ^ {+}} \frac {\sqrt {x + 1} - \cos x}{x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0 ^ {+}} \left(\frac {1}{2 \sqrt {x + 1}} + \sin x\right) = \frac {1}{2}.</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {f _ {3} (x)}{x} = \lim _ {x \rightarrow 0 ^ {+}} \frac {1 - \cos \sqrt {2 x}}{x} \xlongequal {\frac {1 - \cos \sqrt {2 x} \sim \frac {1}{2} (\sqrt {2 x}) ^ {2}}{x}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {1}{2} (\sqrt {2 x}) ^ {2}}{x} = 1.</equation><equation>\begin{aligned} \lim _ {x \rightarrow 0 ^ {+}} \frac {f _ {4} (x)}{x} &= \lim _ {x \rightarrow 0 ^ {+}} \frac {1 - \frac {\ln (1 + x)}{x}}{x} = \lim _ {x \rightarrow 0 ^ {+}} \frac {x - \ln (1 + x)}{x ^ {2}} \\ \frac {\ln (1 + x) = x - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right)}{\hline} \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {1}{2} x ^ {2} + o \left(x ^ {2}\right)}{x ^ {2}} &= \frac {1}{2}. \end{aligned}</equation>由此可得，仅有选项C的函数<equation>f_{3}(x)</equation>满足<equation>\lim_{x\rightarrow 0^{+}}\frac{f_{3}(x)}{x}=1</equation>，其余选项的函数均不符合要求因此，应选C.

---

**2024年第11题 | 填空题 | 5分**
11. 当<equation>x\to 0</equation>时，<equation>\frac {\left(1 + t ^ {2}\right) \sin t ^ {2}}{1 + \cos^ {2} t}</equation><equation>\mathrm{d}t</equation>与<equation>x^{k}</equation>是同阶无穷小，则<equation>k =</equation>___
**答案: **```latex
3
```

**解析:**解记<equation>f ( x )=\int_{0}^{x}\frac{(1+t^{2})\sin t^{2}}{1+\cos^{2}t}\mathrm{d} t</equation>，则<equation>f ( 0 )=0</equation>，且由变限积分的求导公式可得<equation>f^{\prime}(x)=</equation><equation>\frac{(1+x^{2})\sin x^{2}}{1+\cos^{2}x}.</equation>由于<equation>\lim _ {x \rightarrow 0} \frac {f ^ {\prime} (x)}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\left(1 + x ^ {2}\right) \sin x ^ {2}}{\left(1 + \cos^ {2} x\right) x ^ {2}} = \frac {1}{2} \lim _ {x \rightarrow 0} \frac {\sin x ^ {2}}{x ^ {2}} = \frac {1}{2},</equation>故当<equation>x\to0</equation>时，<equation>f^{\prime}(x)</equation>与<equation>x^{2}</equation>是同阶无穷小，且<equation>f^{\prime}(x)\sim \frac{1}{2} x^{2}.</equation>于是，<equation>f (x) = f (x) - f (0) = \int_ {0} ^ {x} f ^ {\prime} (t) \mathrm {d} t \sim \int_ {0} ^ {x} \frac {t ^ {2}}{2} \mathrm {d} t = \frac {t ^ {3}}{6} \Big | _ {0} ^ {x} = \frac {x ^ {3}}{6}. \quad (x \rightarrow 0)</equation>因此，当<equation>x\to 0</equation>时，<equation>f(x)</equation>与<equation>x^{3}</equation>同阶，<equation>k = 3.</equation>

---

**2022年第1题 | 选择题 | 5分 | 答案: C**

1. 若当<equation>x \rightarrow 0</equation>时，<equation>\alpha (x),\beta (x)</equation>是非零无穷小量，则以下四个命题：<equation>\textcircled{1}</equation>若<equation>\alpha (x)\sim \beta (x)</equation>，则<equation>\alpha^{2}(x)\sim \beta^{2}(x);</equation><equation>\textcircled{2}</equation>若<equation>\alpha^{2}(x)\sim \beta^{2}(x)</equation>，则<equation>\alpha (x)\sim \beta (x);</equation><equation>\textcircled{3}</equation>若<equation>\alpha (x)\sim \beta (x)</equation>，则<equation>\alpha (x)-\beta (x)=o(\alpha (x));</equation><equation>\textcircled{4}</equation>若<equation>\alpha (x)-\beta (x)=o(\alpha (x))</equation>，则<equation>\alpha (x)\sim \beta (x).</equation>其中所有真命题的序号是（    ）

A.<equation>\textcircled{1}\textcircled{3}</equation>B.<equation>\textcircled{1}\textcircled{4}</equation>C.<equation>\textcircled{1}\textcircled{3}\textcircled{4}</equation>D.<equation>\textcircled{2}\textcircled{3}\textcircled{4}</equation>

答案: C

**解析:**## 依次分析四个命题.

若<equation>\alpha(x)\sim\beta(x)</equation>，则<equation>\lim_{x\to0}\frac{\alpha(x)}{\beta(x)}=1</equation>，从而<equation>\lim_{x\to0}\frac{\alpha^{2}(x)}{\beta^{2}(x)}=1</equation>，即<equation>\alpha^{2}(x)\sim\beta^{2}(x).</equation>命题<equation>\textcircled{1}</equation>是真命题.

由<equation>\alpha^{2}(x)\sim\beta^{2}(x)</equation>并不能得到<equation>\alpha(x)\sim\beta(x).</equation>考虑<equation>\beta(x)=-\alpha(x)</equation>，则<equation>\lim_{x\to0}\frac{\alpha^{2}(x)}{\beta^{2}(x)}=\lim_{x\to0}\frac{\alpha^{2}(x)}{\alpha^{2}(x)}= 1</equation>，即<equation>\alpha^{2}(x)\sim\beta^{2}(x)</equation>，但<equation>\lim_{x\to0}\frac{\alpha(x)}{\beta(x)}=\lim_{x\to0}\frac{\alpha(x)}{- \alpha(x)}=-1, \alpha(x)</equation>与<equation>\beta(x)</equation>只是同阶但并不等价的无穷小量.

命题<equation>\textcircled{2}</equation>不是真命题.

要说明<equation>\alpha ( x )-\beta ( x )=o( \dot{\alpha} ( x ) )</equation>，只需说明<equation>\lim_{x\to 0}\frac{\alpha ( x )-\beta ( x )}{\alpha ( x )}=0.</equation><equation>\lim _ {x \rightarrow 0} \frac {\alpha (x) - \beta (x)}{\alpha (x)} = 1 - \lim _ {x \rightarrow 0} \frac {\beta (x)}{\alpha (x)} \frac {\alpha (x) \sim \beta (x)}{1 - 1} = 0.</equation>命题<equation>\textcircled{3}</equation>是真命题.

要说明<equation>\alpha (x)\sim \beta (x)</equation>，只需说明<equation>\lim_{x\to 0}\frac{\beta (x)}{\alpha (x)} = 1.</equation><equation>\lim _ {x \rightarrow 0} \frac {\beta (x)}{\alpha (x)} = \lim _ {x \rightarrow 0} \frac {\alpha (x) - [ \alpha (x) - \beta (x) ]}{\alpha (x)} = 1 - \lim _ {x \rightarrow 0} \frac {\alpha (x) - \beta (x)}{\alpha (x)} = 1 - 0 = 1.</equation>命题<equation>\textcircled{4}</equation>是真命题.

综上所述，应选C.

---

**2021年第1题 | 选择题 | 5分 | 答案: C**

1. 当<equation>x \rightarrow 0</equation>时，<equation>\int_{0}^{x^{2}}(\mathrm{e}^{t^{3}}-1)\mathrm{d}t</equation>是<equation>x^{7}</equation>的（    ）

A. 低阶无穷小 B. 等价无穷小

C. 高阶无穷小 D. 同阶但非等价无穷小

答案: C

**解析:**解 计算<equation>\lim_{x\rightarrow 0}\frac{\int_{0}^{x^{2}}(\mathrm{e}^{t^{3}}-1)\mathrm{d}t}{x^{7}}</equation>来比较这两个无穷小量的阶.<equation>\lim _ {x \rightarrow 0} \frac {\int_ {0} ^ {x ^ {2}} \left(\mathrm {e} ^ {t ^ {3}} - 1\right) \mathrm {d} t}{x ^ {7}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\left(\mathrm {e} ^ {x ^ {6}} - 1\right) \cdot 2 x}{7 x ^ {6}} \xlongequal {\text {e} ^ {x ^ {6}} - 1 \sim x ^ {6}} \lim _ {x \rightarrow 0} \frac {x ^ {6} \cdot 2 x}{7 x ^ {6}} = 0.</equation>因此，<equation>\int_{0}^{x^{2}}(\mathrm{e}^{t^{3}}-1)\mathrm{d}t</equation>是<equation>x^{7}</equation>的高阶无穷小.应选C.

---

**2013年第1题 | 选择题 | 4分 | 答案: D**

1. 当<equation>x \to0</equation>时，用“<equation>o(x)</equation>”表示比 x高阶的无穷小量，则下列式子中错误的是（    )

A.<equation>x \cdot o \left( x^{2} \right)=o \left( x^{3} \right)</equation>B.<equation>o(x)\cdot o \left( x^{2} \right)=o \left( x^{3} \right)</equation>C.<equation>o \left( x^{2} \right)+o \left( x^{2} \right)=o \left( x^{2} \right)</equation>D.<equation>o(x)+o \left( x^{2} \right)=o \left( x^{2} \right)</equation>

答案: D

**解析:**由于<equation>\lim _ {x \rightarrow 0} \frac {x \cdot o \left(x ^ {2}\right)}{x ^ {3}} = \lim _ {x \rightarrow 0} \frac {o \left(x ^ {2}\right)}{x ^ {2}} = 0,</equation><equation>\lim _ {x \rightarrow 0} \frac {o (x) \cdot o \left(x ^ {2}\right)}{x ^ {3}} = \lim _ {x \rightarrow 0} \frac {o (x)}{x} \cdot \lim _ {x \rightarrow 0} \frac {o \left(x ^ {2}\right)}{x ^ {2}} = 0,</equation><equation>\lim _ {x \rightarrow 0} \frac {o \left(x ^ {2}\right) + o \left(x ^ {2}\right)}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {o \left(x ^ {2}\right)}{x ^ {2}} + \lim _ {x \rightarrow 0} \frac {o \left(x ^ {2}\right)}{x ^ {2}} = 0 + 0 = 0,</equation>故选项A、B、C均正确.应选D.

对选项D，若令<equation>f ( x )=x^{2}, g ( x )=x^{3}</equation>，则当<equation>x\to 0</equation>时，<equation>x^{2}+x^{3}</equation>形如<equation>o ( x )+o \left( x^{2}\right)</equation>，但<equation>\lim_{x\to 0}\frac{x^{2}+x^{3}}{x^{2}}=1.</equation>因此，当<equation>x\to 0</equation>时，<equation>x^{2}+x^{3}</equation>不是<equation>x^{2}</equation>的高阶无穷小量.

---


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


#### 曲线的凹凸性、拐点及渐近线

**2025年第2题 | 选择题 | 5分 | 答案: B**

2. 已知函数<equation>f ( x )=\int_{0}^{x} \mathrm{e}^{t^{2}} \sin t \mathrm{d} t,g ( x )=\int_{0}^{x} \mathrm{e}^{t^{2}} \mathrm{d} t \cdot \sin^{2} x</equation>，则（    )

A. x=0是 f(x)的极值点，也是 g(x)的极值点

B. x=0是 f(x)的极值点，(0,0)是曲线 y=g(x)的拐点

C. x=0是 f(x)的极值点，(0,0)是曲线 y=f(x)的拐点

D. (0,0)是曲线 y=f(x)的拐点，(0,0)也是曲线 y=g(x)的拐点

答案: B

**解析:**解 先分析<equation>f(x)</equation>的性质，分别计算<equation>f^{\prime}(x)</equation>，<equation>f^{\prime \prime}(x)</equation>. 根据链式法则，<equation>f ^ {\prime} (x) = \sin x \mathrm {e} ^ {x ^ {2}},</equation><equation>f ^ {\prime \prime} (x) = 2 x \sin x \mathrm {e} ^ {x ^ {2}} + \cos x \mathrm {e} ^ {x ^ {2}} = \left(2 x \sin x + \cos x\right) \mathrm {e} ^ {x ^ {2}}.</equation>取<equation>\delta</equation>为充分小的正数，当<equation>x \in (-\delta, 0)</equation>时，<equation>f^{\prime}(x) < 0,f(x)</equation>单调减少，当<equation>x \in (0,\delta)</equation>时，<equation>f^{\prime}(x) > 0,f(x)</equation>单调增加.于是，<equation>x = 0</equation>是<equation>f(x)</equation>的极小值点.或者，也可以由<equation>f^{\prime}(0) = 0,f^{\prime \prime}(0) = 1 > 0</equation>以及极值的第二充分条件得到<equation>x = 0</equation>是<equation>f(x)</equation>的极小值点.

当<equation>x \in(-\delta ,\delta)</equation>时，<equation>x\sin x\geqslant0,\cos x > 0,f^{\prime \prime}(x)</equation>在<equation>(-\delta ,\delta)</equation>内恒大于0，<equation>y=f(x)</equation>是凹曲线.于是，点（0，0）不是曲线<equation>y=f(x)</equation>的拐点.

再分析<equation>g ( x )</equation>的性质，分别计算<equation>g^{\prime}(x), g^{\prime \prime}(x).</equation>根据链式法则，<equation>g ^ {\prime} (x) = \sin^ {2} x \mathrm {e} ^ {x ^ {2}} + 2 \sin x \cos x \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = \sin^ {2} x \mathrm {e} ^ {x ^ {2}} + \sin 2 x \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t,</equation><equation>\begin{aligned} g ^ {\prime \prime} (x) &= 2 \sin x \cos x \mathrm {e} ^ {x ^ {2}} + 2 x \sin^ {2} x \mathrm {e} ^ {x ^ {2}} + \sin 2 x \mathrm {e} ^ {x ^ {2}} + 2 \cos 2 x \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t \\ &= 2 \left(\sin 2 x + x \sin^ {2} x\right) \mathrm {e} ^ {x ^ {2}} + 2 \cos 2 x \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t. \end{aligned}</equation>取<equation>\delta</equation>为充分小的正数，由于<equation>\mathrm{e}^{t^2}</equation>恒大于0，故当<equation>x\in(-\delta,0)</equation>时，<equation>\int_0^x\mathrm{e}^{t^2}\mathrm{d}t < 0</equation>，结合<equation>\sin 2x < 0</equation>可得，<equation>g^{\prime}(x) > 0,g(x)</equation>单调增加，当<equation>x\in(0,\delta)</equation>时，<equation>\int_0^x\mathrm{e}^{t^2}\mathrm{d}t > 0</equation>，结合<equation>\sin 2x > 0</equation>可得，<equation>g^{\prime}(x) > 0,g(x)</equation>单调增加.于是，<equation>x = 0</equation>不是<equation>g(x)</equation>的极值点.

当<equation>x\in(-\delta ,0)</equation>时，<equation>\sin 2x + x\sin^2 x < 0,\int_0^x\mathrm{e}^{t^2}\mathrm{d}t < 0,\cos 2x > 0,g''(x) < 0,y = g(x)</equation>是凸曲线，当<equation>x\in(0,\delta)</equation>时，<equation>\sin 2x + x\sin^2 x > 0,\int_0^x\mathrm{e}^{t^2}\mathrm{d}t > 0,\cos 2x > 0,g''(x) > 0,y = g(x)</equation>是凹曲线.于是，点(0,0)是曲线<equation>y = g(x)</equation>的拐点.

综上所述，应选B.

---

**2025年第11题 | 填空题 | 5分**

11. 设<equation>g(x)</equation>是函数<equation>f(x)=\frac{1}{2}\ln \frac{3+x}{3-x}</equation>的反函数,则曲线<equation>y=g(x)</equation>的渐近线方程为___

**答案:**y=-3,y=3.

**解析:**解由<equation>y=f(x)=\frac{1}{2}\ln \frac{3+x}{3-x}</equation>可得<equation>\mathrm{e}^{2 y}=\frac{3+x}{3-x}.</equation>整理可得<equation>3(\mathrm{e}^{2 y}-1)=x(\mathrm{e}^{2 y}+1)</equation>解得 x=<equation>\frac{3(\mathrm{e}^{2 y}-1)}{\mathrm{e}^{2 y}+1}</equation>即<equation>f^{-1}(y)=\frac{3(\mathrm{e}^{2 y}-1)}{\mathrm{e}^{2 y}+1}</equation>令 g = f<equation>^{-1}</equation>，并将 y换成 x，可得 g(x)<equation>= \frac{3(\mathrm{e}^{2 x}-1)}{\mathrm{e}^{2 x}+1}.</equation>由于 g(x)是连续函数，故 y = g(x)没有铅直渐近线.

计算<equation>\lim_{x\to -\infty}g(x)</equation>，<equation>\lim_{x\to +\infty}g(x)</equation>可得<equation>\lim _ {x \rightarrow - \infty} g (x) = \lim _ {x \rightarrow - \infty} \frac {3 \left(\mathrm {e} ^ {2 x} - 1\right)}{\mathrm {e} ^ {2 x} + 1} = \frac {3 \cdot (0 - 1)}{0 + 1} = - 3,</equation><equation>\lim _ {x \rightarrow + \infty} g (x) = \lim _ {x \rightarrow + \infty} \frac {3 \left(\mathrm {e} ^ {2 x} - 1\right)}{\mathrm {e} ^ {2 x} + 1} = \lim _ {x \rightarrow + \infty} \frac {3 \left(1 - \mathrm {e} ^ {- 2 x}\right)}{1 + \mathrm {e} ^ {- 2 x}} = \frac {3 \cdot (1 - 0)}{1 + 0} = 3.</equation>因此，曲线 y=g(x)共有两条水平渐近线，y=3和y=-3.又因为曲线 y=g(x)已有两条不同的水平渐近线，所以曲线 y=g(x)没有斜渐近线.

---

**2019年第10题 | 填空题 | 4分**

10. 曲线<equation>y=x\sin x+2\cos x\left(-\frac{\pi}{2}<x<\frac{3\pi}{2}\right)</equation>的拐点坐标为 ___

**答案:**## (<equation>\pi</equation>, -2).

**解析:**解分别计算<equation>y^{\prime}(x), y^{\prime\prime}(x).</equation><equation>y ^ {\prime} (x) = x \cos x + \sin x - 2 \sin x = x \cos x - \sin x,</equation><equation>y ^ {\prime \prime} (x) = - x \sin x + \cos x - \cos x = - x \sin x.</equation>在区间<equation>\left(-\frac{\pi}{2},\frac{3\pi}{2}\right)</equation>内，仅有 x=0和 x=<equation>\pi</equation>满足<equation>y^{\prime\prime}(x)=0.</equation>下面用两种方法来判定拐点.

（法一）当<equation>-\frac{\pi}{2} < x < 0</equation>时，<equation>\sin x < 0</equation><equation>y^{\prime\prime}(x) < 0</equation>；当<equation>0 < x < \pi</equation>时，<equation>\sin x > 0</equation><equation>y^{\prime\prime}(x) < 0</equation>由于<equation>y^{\prime\prime}(x)</equation>在<equation>x=0</equation>处不变号，故曲线<equation>y=y(x)</equation>经过点（0，2）时，凹凸性没发生改变.点（0，2）不是<equation>y=y(x)</equation>的拐点.

当<equation>0 < x < \pi</equation>时，<equation>\sin x > 0</equation><equation>y^{\prime \prime}(x) < 0</equation>；当<equation>\pi < x < \frac{3\pi}{2}</equation>时，<equation>\sin x < 0</equation><equation>y^{\prime \prime}(x) > 0</equation>.由于<equation>y^{\prime \prime}(x)</equation>在<equation>x=\pi</equation>处变号，故曲线<equation>y=y(x)</equation>经过点（<equation>\pi,-2</equation>）时，凹凸性改变.点（<equation>\pi,-2</equation>）是<equation>y=y(x)</equation>的拐点.

（法二）计算<equation>y^{\prime \prime \prime}(x).</equation><equation>y ^ {\prime \prime \prime} (x) = - x \cos x - \sin x.</equation>当 x=0时，<equation>y^{\prime \prime \prime}(0)=0</equation>.此时不能确定点（0，2）是否为拐点.当 x=<equation>\pi</equation>时，<equation>y^{\prime \prime \prime}(\pi)=\pi</equation>.由拐点的充分条件可知，点（<equation>\pi,-2</equation>）是曲线 y=y(x)的拐点.

---

**2018年第2题 | 选择题 | 4分 | 答案: D**

2. 设函数 f(x)在[0,1]上二阶可导，且<equation>\int_{0}^{1} f(x)\mathrm{d}x=0</equation>，则（    )

A. 当<equation>f^{\prime}(x)<0</equation>时，<equation>f\left(\frac{1}{2}\right)<0</equation>B. 当<equation>f^{\prime\prime}(x)<0</equation>时，<equation>f\left(\frac{1}{2}\right)<0</equation>C. 当<equation>f^{\prime}(x)>0</equation>时，<equation>f\left(\frac{1}{2}\right)<0</equation>D. 当<equation>f^{\prime\prime}(x)>0</equation>时，<equation>f\left(\frac{1}{2}\right)<0</equation>

答案: D

**解析:**解（法一）考虑 f(x)在<equation>x=\frac{1}{2}</equation>处的带有拉格朗日余项的一阶泰勒公式.<equation>f (x) = f \left(\frac {1}{2}\right) + f ^ {\prime} \left(\frac {1}{2}\right) \left(x - \frac {1}{2}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {1}{2}\right) ^ {2},</equation>其中<equation>\xi_{x}</equation>介于x与<equation>\frac{1}{2}</equation>之间.<equation>\begin{aligned} \int_ {0} ^ {1} f (x) \mathrm {d} x &= \int_ {0} ^ {1} \left[ f \left(\frac {1}{2}\right) + f ^ {\prime} \left(\frac {1}{2}\right) \left(x - \frac {1}{2}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {1}{2}\right) ^ {2} \right] \mathrm {d} x \\ \underline {{\frac {\int_ {0} ^ {1} \left(x - \frac {1}{2}\right) \mathrm {d} x = 0}{\mathrm {一}}}} f \left(\frac {1}{2}\right) + \frac {1}{2} \int_ {0} ^ {1} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {1}{2}\right) ^ {2} \mathrm {d} x. \end{aligned}</equation>由于<equation>\int_{0}^{1} f(x)\mathrm{d}x=0</equation>，故<equation>f\left(\frac{1}{2}\right)=-\frac{1}{2}\int_{0}^{1} f^{\prime \prime}(\xi_{x})\left(x-\frac{1}{2}\right)^{2}\mathrm{d}x</equation>.当<equation>f^{\prime \prime}(x)>0</equation>时，<equation>\int_{0}^{1} f^{\prime \prime}(\xi_{x})\left(x-\frac{1}{2}\right)^{2}\mathrm{d}x > 0</equation>，于是，<equation>f\left(\frac{1}{2}\right)<0</equation>.同理可得，当<equation>f^{\prime \prime}(x)<0</equation>时，<equation>f\left(\frac{1}{2}\right)>0.</equation>因此，应选D.

下面说明选项A和选项C不正确.

选项A：考虑<equation>f ( x )=-x+\frac{1}{2}</equation>，则<equation>f^{\prime}(x)=-1<0</equation>且<equation>\int_{0}^{1} f(x)\mathrm{d}x=0</equation>，但<equation>f\left(\frac{1}{2}\right)=0.</equation>选项C：考虑<equation>f ( x )=x-\frac{1}{2}</equation>，则<equation>f^{\prime}(x)=1>0</equation>且<equation>\int_{0}^{1} f(x)\mathrm{d}x=0</equation>，但<equation>f\left(\frac{1}{2}\right)=0.</equation>（法二）记<equation>g ( x )=f^{\prime}\left(\frac{1}{2}\right)\left(x-\frac{1}{2}\right)+f\left(\frac{1}{2}\right)</equation>，则 y=g(x)为曲线 y=f(x)在点<equation>\left(\frac{1}{2},f\left(\frac{1}{2}\right)\right)</equation>处的切线.

如图所示，当<equation>f^{\prime \prime}(x) > 0</equation>时，由凹曲线的几何性质可知，曲线<equation>y=f(x)</equation>在点<equation>\left(\frac{1}{2}, f\left(\frac{1}{2}\right)\right)</equation>处的

切线<equation>y = g(x)</equation>位于<equation>y = f(x)</equation>之下，即<equation>g(x)\leqslant f(x)</equation>.

由于<equation>f^{\prime \prime}(x) > 0</equation>，故<equation>f(x)</equation>在[0,1]上不恒等于g(x)，从而由定积分的性质可知，<equation>0=\int_{0}^{1} f(x)\mathrm{d} x > \int_{0}^{1} g(x)\mathrm{d} x=\int_{0}^{1} f\left(\frac{1}{2}\right)\mathrm{d} x+\int_{0}^{1} f^{\prime}\left(\frac{1}{2}\right)\left(x-\frac{1}{2}\right)\mathrm{d} x=f\left(\frac{1}{2}\right).</equation>因此，<equation>f\left(\frac{1}{2}\right) < 0.</equation>应选D.

---

**2018年第9题 | 填空题 | 4分**

9. 曲线<equation>y=x^{2}+2 \ln x</equation>在其拐点处的切线方程是 ___

**答案:**# y=4x-3.

**解析:**解记<equation>f ( x )=x^{2}+2 \ln x</equation>，则<equation>f^{\prime}(x)=2 x+\frac{2}{x}, f^{\prime\prime}(x)=2-\frac{2}{x^{2}}.</equation>曲线<equation>y=f(x)</equation>的拐点<equation>\left(x_{0},f\left(x_{0}\right)\right)</equation>满足<equation>f^{\prime \prime}\left(x_{0}\right)=0</equation>解<equation>2-\frac{2}{x_{0}^{2}}=0</equation>得<equation>x_{0}=\pm 1.</equation>由于f(x)的自然定义域为<equation>\left(0,+\infty\right)</equation>，故<equation>x_{0}=1</equation>，拐点坐标为（1，1）.

又因为<equation>f^{\prime}(1)=\left. \left( 2 x+\frac{2}{x} \right) \right|_{x=1}=4</equation>，所以拐点（1，1）处的切线方程为 y-1=4(x-1)，即 y=4x-3.

---

**2016年第1题 | 选择题 | 4分 | 答案: B**

1. 设函数<equation>f ( x )</equation>在<equation>(-\infty, +\infty)</equation>内连续，其导函数的图形如图所示，则（    ）

A. 函数 f(x)有2个极值点，曲线 y=f(x)有2个拐点

B. 函数 f(x)有2个极值点，曲线 y=f(x)有3个拐点

C. 函数 f(x)有3个极值点，曲线 y=f(x)有1个拐点

D. 函数 f(x)有3个极值点，曲线 y=f(x)有2个拐点

答案: B

**解析:**解 观察图形，<equation>f(x)</equation>共有4个可能的极值点，从左至右依次记为<equation>x_{1},</equation><equation>x_{2}, x_{3}, x_{4}</equation>其中<equation>x_{2}</equation>为虚线与x轴的交点，其余三点为<equation>f^{\prime}(x)</equation>与x轴的交点.在<equation>x=x_{1}, x_{3}, x_{4}</equation>处，<equation>f^{\prime}(x)=0</equation>在<equation>x=x_{2}</equation>处，<equation>f(x)</equation>不可导.

分别考察<equation>x=x_{1}, x_{2}, x_{3}, x_{4}</equation>左、右两侧<equation>f^{\prime}(x)</equation>的符号.

- 当<equation>x < x_{1}</equation>时，<equation>f^{\prime}(x) > 0</equation>；当<equation>x_{1} < x < x_{2}</equation>时，<equation>f^{\prime}(x) < 0</equation>，故<equation>x=x_{1}</equation>是<equation>f(x)</equation>的极大值点.

- 当<equation>x_{1} < x < x_{2}</equation>时，<equation>f^{\prime}(x) < 0</equation>；当<equation>x_{2} < x < x_{3}</equation>时，<equation>f^{\prime}(x) < 0</equation>，故<equation>x = x_{2}</equation>不是<equation>f(x)</equation>的极值点.

- 当<equation>x_{2} < x < x_{3}</equation>时，<equation>f^{\prime}(x) < 0</equation>；当<equation>x_{3} < x < x_{4}</equation>时，<equation>f^{\prime}(x) > 0</equation>，故<equation>x = x_{3}</equation>是<equation>f(x)</equation>的极小值点.

- 当<equation>x_{3} < x < x_{4}</equation>时，<equation>f^{\prime}(x) > 0</equation>；当<equation>x > x_{4}</equation>时，<equation>f^{\prime}(x) > 0</equation>，故<equation>x = x_{4}</equation>不是<equation>f(x)</equation>的极值点.

因此，f（x）共有2个极值点.

曲线<equation>y=f(x)</equation>可能的拐点从左至右依次为<equation>\left(x_{2},f\left(x_{2}\right)\right),\left(x_{5},f\left(x_{5}\right)\right),\left(x_{4},f\left(x_{4}\right)\right)</equation>其中<equation>f^{\prime \prime}\left(x_{2}\right)</equation>不存在，<equation>f^{\prime \prime}\left(x_{5}\right)=f^{\prime \prime}\left(x_{4}\right)=0.</equation>- 当<equation>x<x_{2}</equation>时，<equation>f^{\prime}(x)</equation>单调减少；当<equation>x_{2}<x<x_{5}</equation>时，<equation>f^{\prime}(x)</equation>单调增加，故点（<equation>x_{2}, f(x_{2})</equation>）是曲线<equation>y=f(x)</equation>的拐点.

- 当<equation>x_{2} < x < x_{5}</equation>时，<equation>f^{\prime}(x)</equation>单调增加；当<equation>x_{5} < x < x_{4}</equation>时，<equation>f^{\prime}(x)</equation>单调减少，故点（<equation>x_{5}, f(x_{5})</equation>）是曲线<equation>y=f(x)</equation>的拐点.

- 当<equation>x_{5} < x < x_{4}</equation>时，<equation>f^{\prime}(x)</equation>单调减少；当<equation>x > x_{4}</equation>时，<equation>f^{\prime}(x)</equation>单调增加，故点（<equation>x_{4}, f(x_{4})</equation>）是曲线<equation>y=f(x)</equation>的拐点.

因此，曲线 y=f(x）共有3个拐点.

综上所述，应选B.

---

**2015年第2题 | 选择题 | 4分 | 答案: C**

2. 设函数 f(x)在<equation>(-\infty,+\infty)</equation>内连续，其2阶导函数<equation>f^{\prime\prime}(x)</equation>的图形如图所示，则曲线 y=f(x)的拐点个数为（    ）

A. 0 B. 1 C. 2 D. 3

答案: C

**解析:**由图可知，在<equation>(-\infty, +\infty)</equation>上，<equation>f^{\prime \prime}(x)=0</equation>有两个实根<equation>x_{1}, x_{2}</equation>，且<equation>f^{\prime \prime}(x)</equation>在 x=0处无定义.

下面我们分别讨论点<equation>\left(x_{1},f\left(x_{1}\right)\right),\left(0,f(0)\right)</equation>和<equation>\left(x_{2},f\left(x_{2}\right)\right)</equation>是否为拐点.

在<equation>x = x_{1}</equation>的左、右邻域内，<equation>f^{\prime \prime}(x)</equation>均大于零.<equation>f^{\prime \prime}(x)</equation>在该点两侧不变号，故点<equation>(x_{1}, f(x_{1}))</equation>不是曲线<equation>y = f(x)</equation>的拐点.

在<equation>x = 0</equation>的左侧邻域内，<equation>f^{\prime \prime}(x) > 0</equation>；在<equation>x = 0</equation>的右侧邻域内，<equation>f^{\prime \prime}(x) < 0</equation><equation>f^{\prime \prime}(x)</equation>在该点两侧变号，故点（0，<equation>f(0)</equation>）是曲线<equation>y = f(x)</equation>的拐点.

在<equation>x= x_{2}</equation>的左侧邻域内，<equation>f^{\prime \prime}(x)<0</equation>；在<equation>x= x_{2}</equation>的右侧邻域内，<equation>f^{\prime \prime}(x)>0. f^{\prime \prime}(x)</equation>在该点两侧变号，故点（<equation>x_{2}, f(x_{2})</equation>）是曲线<equation>y=f(x)</equation>的拐点.

综上所述，曲线<equation>y=f(x)</equation>共有2个拐点，应选C.

---

**2014年第2题 | 选择题 | 4分 | 答案: C**

2. 下列曲线中有渐近线的是（    ）

A. y=x+<equation>\sin x</equation>B. y=x²+<equation>\sin x</equation>C. y=x+<equation>\sin \frac{1}{x}</equation>D. y=x²+<equation>\sin \frac{1}{x}</equation>

答案: C

**解析:**解 先考察各曲线是否具有铅直渐近线.<equation>y = x + \sin x, y = x^{2} + \sin x</equation>在<equation>(-\infty , +\infty)</equation>上均无间断点，故不存在铅直渐近线；<equation>y = x + \sin \frac{1}{x}</equation>和<equation>y = x^{2} + \sin \frac{1}{x}</equation>在<equation>x = 0</equation>处无定义，但<equation>\lim_{x\to 0}\sin \frac{1}{x}</equation>不存在，从而也没有铅直渐近线.

再考察它们是否具有水平渐近线

由于选项A、B、C、D中的曲线在<equation>x\to +\infty</equation>和<equation>x\to -\infty</equation>时均趋于<equation>\infty</equation>，故它们均没有水平渐近线最后考察它们是否具有斜渐近线.

对选项C，<equation>\lim_{x\to \infty}\frac{x+\sin \frac{1}{x}}{x}=1</equation>，且<equation>\lim_{x\to \infty}\left(x+\sin \frac{1}{x}-x\right)=\lim_{x\to \infty}\sin \frac{1}{x}=0</equation>，故<equation>y=x+\sin \frac{1}{x}</equation>有斜渐近线<equation>y=x</equation>.应选C.

下面我们说明选项A、B、D没有斜渐近线.

对选项 A<equation>\lim_{x\to \infty}\frac{x+\sin x}{x}=1</equation>，但<equation>\lim_{x\to \infty}(x+\sin x-x)=\lim_{x\to \infty}\sin x</equation>不存在，故选项A没有斜渐近线

对选项 B，<equation>\lim_{x\to \infty}\frac{x^{2}+\sin x}{x}=\infty</equation>，对选项D，<equation>\lim_{x\to \infty}\frac{x^{2}+\sin \frac{1}{x}}{x}=\infty</equation>，故选项B和选项D都没有斜渐近线

---

**2014年第4题 | 选择题 | 4分 | 答案: D**

4. 设函数 f(x)具有2阶导数，<equation>g ( x )=f ( 0 ) ( 1-x )+f ( 1 ) x</equation>，则在区间[0,1]上（    )

A. 当<equation>f^{\prime}(x)\geqslant0</equation>时，<equation>f(x)\geqslant g(x)</equation>B. 当<equation>f^{\prime}(x)\geqslant0</equation>时，<equation>f(x)\leqslant g(x)</equation>C. 当<equation>f^{\prime\prime}(x)\geqslant0</equation>时，<equation>f(x)\geqslant g(x)</equation>D. 当<equation>f^{\prime\prime}(x)\geqslant0</equation>时，<equation>f(x)\leqslant g(x)</equation>

答案: D

**解析:**解 由于<equation>g ( x )=\frac{f ( 1 )-f ( 0 )}{1-0} x+f ( 0 )</equation><equation>g ( 0 )=f ( 0 )</equation><equation>g ( 1 )= f ( 1 )</equation>，故<equation>y=g ( x )</equation>表示的曲线是过点（0，f(0)），（1，f(1)）的弦由分析知，若<equation>y=f ( x )</equation>在[0,1]上凹，则<equation>f ( x ) \leqslant g ( x )</equation>；若<equation>y=f ( x )</equation>在[0,1]上凸，则<equation>f ( x ) \geqslant g ( x )</equation>.由于f(x)具有2阶导数，故曲线的凹凸性可以由<equation>f^{\prime \prime} ( x )</equation>确定.当<equation>f^{\prime \prime} ( x ) \geqslant 0</equation>时，<equation>y=f ( x )</equation>在[0,1]上凹，从而<equation>f ( x ) \leqslant g ( x )</equation>.应选D.

一阶导数的符号与曲线的凹凸性没有直接关系.作为选项A的反例，可以考虑曲线<equation>y=x^{2}</equation>；作为选项B的反例，可以考虑曲线<equation>y=\sqrt{x}.</equation>

---

**2012年第1题 | 选择题 | 4分 | 答案: C**

1. 曲线<equation>y=\frac{x^{2}+x}{x^{2}-1}</equation>的渐近线的条数为（    ）

A.0 B.1 C.2 D.3

答案: C

**解析:**解 先考虑间断点处的情况.<equation>y=\frac{x^{2}+x}{x^{2}-1}</equation>有间断点<equation>x=\pm 1.</equation>由于<equation>\lim_{x\rightarrow 1}\frac{x^{2}+x}{x^{2}-1}=\lim_{x\rightarrow 1}\frac{x}{x-1}=\infty</equation>，故曲线有铅直渐近线<equation>x=1.</equation>又由于<equation>\lim_{x\rightarrow -1}\frac{x^{2}+x}{x^{2}-1}=\lim_{x\rightarrow -1}\frac{x}{x-1}=\frac{1}{2}</equation>，故曲线在<equation>x=-1</equation>处没有渐近线.

再考虑无穷远处的情况.由于<equation>\lim_{x\rightarrow \infty}\frac{x^{2}+x}{x^{2}-1}=1</equation>，故曲线有水平渐近线<equation>y=1.</equation>综上所述，曲线共有两条渐近线.应选C.

---

**2010年第12题 | 填空题 | 4分**

12. 若曲线<equation>y=x^{3}+ax^{2}+bx+1</equation>有拐点<equation>(-1,0)</equation>, 则<equation>b=</equation>___

**解析:**解 由于点（-1，0）在曲线上，故<equation>0=-1+a-b+1=a-b</equation>即 a=b.又由拐点的必要条件知 (x)在 x=-1处的二阶导数必为零.于是<equation>y^{\prime \prime}(-1)=-6+2a=0</equation>即 a=3.因此，b=a=3.

---


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


#### 微分中值定理

**2025年第20题 | 解答题 | 12分**

20. 设函数 f(x)在区间（a,b）内可导，证明导函数<equation>f^{\prime}(x)</equation>在（a,b）内严格单调增加的充分必要条件是：对（a,b）内任意的<equation>x_{1},x_{2},x_{3}</equation>，当<equation>x_{1}<x_{2}<x_{3}</equation>时，<equation>\frac{f(x_{2})-f(x_{1})}{x_{2}-x_{1}}<\frac{f(x_{3})-f(x_{2})}{x_{3}-x_{2}}.</equation>

**解析:**证 先证明必要性.

对（a,b）内任意的<equation>x_{1}, x_{2}, x_{3}</equation>，当<equation>x_{1} < x_{2} < x_{3}</equation>时，由拉格朗日中值定理可得存在<equation>\xi_{1}\in(x_{1},x_{2})</equation><equation>\xi_{2}\in(x_{2},x_{3})</equation>，使得<equation>f^{\prime}(\xi_{1})=\frac{f(x_{2})-f(x_{1})}{x_{2}-x_{1}},f^{\prime}(\xi_{2})=\frac{f(x_{3})-f(x_{2})}{x_{3}-x_{2}}.</equation>由<equation>f^{\prime}(x)</equation>单调增加以及<equation>\xi_{1}<</equation><equation>\xi_{2}</equation>可得<equation>f^{\prime}(\xi_{1})<f^{\prime}(\xi_{2})</equation>即<equation>\frac{f(x_{2})-f(x_{1})}{x_{2}-x_{1}}<\frac{f(x_{3})-f(x_{2})}{x_{3}-x_{2}}.</equation>再证明充分性.

任取<equation>x_{0},x_{1},x_{2}\in(a,b)</equation>满足<equation>x_{1} < x_{0} < x_{2}</equation>，由已知条件可得<equation>\frac{f(x_0) - f(x_1)}{x_0 - x_1} < \frac{f(x_2) - f(x_0)}{x_2 - x_0}.</equation>取s,t满足<equation>x_{1} < s < x_{0} < t < x_{2}</equation>，由已知条件可得<equation>\frac {f (s) - f \left(x _ {1}\right)}{s - x _ {1}} < \frac {f \left(x _ {0}\right) - f (s)}{x _ {0} - s}, \quad \frac {f (t) - f \left(x _ {0}\right)}{t - x _ {0}} < \frac {f \left(x _ {2}\right) - f (t)}{x _ {2} - t}.</equation>在<equation>\frac{f(s) - f(x_1)}{s - x_1} < \frac{f(x_0) - f(s)}{x_0 - s}</equation>中令<equation>s\to x_1^+</equation>可得<equation>f ^ {\prime} \left(x _ {1}\right) = f _ {+} ^ {\prime} \left(x _ {1}\right) = \lim _ {s \rightarrow x _ {1} ^ {+}} \frac {f (s) - f \left(x _ {1}\right)}{s - x _ {1}} \leqslant \lim _ {s \rightarrow x _ {1} ^ {+}} \frac {f \left(x _ {0}\right) - f (s)}{x _ {0} - s} = \frac {f \left(x _ {0}\right) - f \left(x _ {1}\right)}{x _ {0} - x _ {1}}.</equation>在<equation>\frac{f(t) - f(x_0)}{t - x_0} < \frac{f(x_2) - f(t)}{x_2 - t}</equation>中令<equation>t\to x_2^{-}</equation>可行<equation>\frac {f \left(x _ {2}\right) - f \left(x _ {0}\right)}{x _ {2} - x _ {0}} = \lim _ {t \rightarrow x _ {2} ^ {-}} \frac {f (t) - f \left(x _ {0}\right)}{t - x _ {0}} \leqslant \lim _ {t \rightarrow x _ {2} ^ {-}} \frac {f \left(x _ {2}\right) - f (t)}{x _ {2} - t} = f _ {-} ^ {\prime} \left(x _ {2}\right) = f ^ {\prime} \left(x _ {2}\right).</equation>由(1)式，(2)式以及<equation>\frac{f(x_0) - f(x_1)}{x_0 - x_1} < \frac{f(x_2) - f(x_0)}{x_2 - x_0}</equation>可得<equation>f^{\prime}(x_{1}) < f^{\prime}(x_{2})</equation>由<equation>x_{1}, x_{2}</equation>的任意性可得<equation>f^{\prime}(x)</equation>在<equation>(a,b)</equation>内严格单调增加.

---

**2019年第19题 | 解答题 | 10分**

19. (本题满分10分)

设<equation>a_{n}=\int_{0}^{1} x^{n}\sqrt{1-x^{2}}\mathrm{d}x(n=0,1,2,\dots).</equation>I. 证明数列<equation>\{a_{n}\}</equation>单调递减，且<equation>a_{n}=\frac{n-1}{n+2} a_{n-2}(n=2,3,\cdots);</equation>II. 求<equation>\lim_{n\to\infty}\frac{a_{n}}{a_{n-1}}.</equation>

**答案:**（I）证明略；（Ⅱ）<equation>\lim_{n\to \infty}\frac{a_{n}}{a_{n-1}}=1.</equation>

**解析:**解（I）考虑<equation>a_{n+1}-a_{n}</equation>. 由于在（0，1）内，<equation>x^{n+1}-x^{n}<0,\sqrt{1-x^{2}}>0</equation>，故由定积分的保号性可知，<equation>a _ {n + 1} - a _ {n} = \int_ {0} ^ {1} \left(x ^ {n + 1} - x ^ {n}\right) \sqrt {1 - x ^ {2}} \mathrm {d} x < 0.</equation>因此，<equation>\{a_{n}\}</equation>单调递减.

下面用两种方法证明<equation>a_{n} = \frac{n - 1}{n + 2} a_{n - 2} (n = 2,3,\dots).</equation>（法一）先三角换元，再分部积分.

令<equation>x=\sin t</equation>，则<equation>\mathrm{d}x=\cos t\mathrm{d}t.</equation><equation>\begin{aligned} a _ {n} &= \int_ {0} ^ {1} x ^ {n} \sqrt {1 - x ^ {2}} \mathrm {d} x \xlongequal {x = \sin t} \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \cos t \cdot \cos t \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \cos^ {2} t \mathrm {d} t \\ &= \int_ {0} ^ {\frac {\pi}{2}} \left(\sin^ {n} t - \sin^ {n + 2} t\right) \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t + \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n + 1} t \mathrm {d} (\cos t) \\ &= \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t + \sin^ {n + 1} t \cos t \left| _ {0} ^ {\frac {\pi}{2}} - \int_ {0} ^ {\frac {\pi}{2}} \cos t \cdot (n + 1) \sin^ {n} t \cdot \cos t \mathrm {d} t \right. \\ &= \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t - (n + 1) \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \cos^ {2} t \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t - (n + 1) a _ {n}. \end{aligned}</equation>由上可得，<equation>(n + 2)a_{n} = \int_{0}^{\frac{\pi}{2}}\sin^{n}t\mathrm{d}t.</equation>另一方面，<equation>\begin{aligned} \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t &= - \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n - 1} t \mathrm {d} (\cos t) = - \left[ \sin^ {n - 1} t \cos t \Big | _ {0} ^ {\frac {\pi}{2}} - \int_ {0} ^ {\frac {\pi}{2}} \cos t \cdot (n - 1) \sin^ {n - 2} t \cdot \cos t \mathrm {d} t \right] \\ &= (n - 1) \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n - 2} t \cos^ {2} t \mathrm {d} t = (n - 1) a _ {n - 2}. \end{aligned}</equation>因此，<equation>( n+2) a_{n}=( n-1) a_{n-2}</equation>，即<equation>a_{n}=\frac{n-1}{n+2} a_{n-2}( n=2,3,\dots).</equation>（法二）直接分部积分.注意到<equation>[（1-x^{2})^{\frac{3}{2}}]^{\prime}=-3x\sqrt{1-x^{2}}</equation>，故<equation>\begin{array}{l} a _ {n} = \int_ {0} ^ {1} x ^ {n} \sqrt {1 - x ^ {2}} \mathrm {d} x = - \frac {1}{3} \int_ {0} ^ {1} x ^ {n - 1} \mathrm {d} \left(1 - x ^ {2}\right) ^ {\frac {3}{2}} \\ = - \frac {1}{3} \left\{\left[ x ^ {n - 1} \left(1 - x ^ {2}\right) ^ {\frac {3}{2}} \right] \Bigg | _ {0} ^ {1} - \int_ {0} ^ {1} \left(1 - x ^ {2}\right) ^ {\frac {3}{2}} \cdot (n - 1) x ^ {n - 2} \mathrm {d} x \right\} \\ = \frac {n - 1}{3} \int_ {0} ^ {1} \left(1 - x ^ {2}\right) \sqrt {1 - x ^ {2}} x ^ {n - 2} \mathrm {d} x = \frac {n - 1}{3} \int_ {0} ^ {1} \left(x ^ {n - 2} - x ^ {n}\right) \sqrt {1 - x ^ {2}} \mathrm {d} x \\ = \frac {n - 1}{3} \left(\int_ {0} ^ {1} x ^ {n - 2} \sqrt {1 - x ^ {2}} \mathrm {d} x - \int_ {0} ^ {1} x ^ {n} \sqrt {1 - x ^ {2}} \mathrm {d} x\right) \\ = \frac {n - 1}{3} \left(a _ {n - 2} - a _ {n}\right). \\ \end{array}</equation>因此，<equation>a_{n} = \frac{n - 1}{n + 2} a_{n - 2} (n = 2,3,\dots).</equation>（Ⅱ）由第（Ⅰ）问可知<equation>\left\{a_{n}\right\}</equation>单调递减，故<equation>a_{n} < a_{n-1} < a_{n-2}</equation>. 又由<equation>a_{n}</equation>的表达式可知<equation>a_{n} > 0 (n= 0,1,\cdots)</equation>，故<equation>\frac {n - 1}{n + 2} = \frac {a _ {n}}{a _ {n - 2}} < \frac {a _ {n}}{a _ {n - 1}} < \frac {a _ {n}}{a _ {n}} = 1.</equation>对（1）式中各项同时取极限，令<equation>n\to\infty</equation>，可得<equation>1 = \lim _ {n \rightarrow \infty} \frac {n - 1}{n + 2} \leqslant \lim _ {n \rightarrow \infty} \frac {a _ {n}}{a _ {n - 1}} \leqslant 1.</equation>由夹逼准则可知，<equation>\lim_{n\to \infty}\frac{a_n}{a_{n - 1}} = 1.</equation>

---

**2013年第19题 | 解答题 | 10分**

19. (本题满分10分)

设函数 f(x)在<equation>[0,+\infty)</equation>上可导，<equation>f(0)=0</equation>且<equation>\lim_{x\rightarrow+\infty}f(x)=2.</equation>证明：

I. 存在 a > 0，使得 f(a)=1;

II. 对第一问中的 a，存在<equation>\xi\in(0,a)</equation>，使得<equation>f^{\prime}(\xi)=\frac{1}{a}.</equation>

**答案:**（19）（I）证明略；

（Ⅱ）证明略.

**解析:**证（I）由<equation>\lim_{x\to +\infty}f(x)=2 > \frac{3}{2}</equation>以及极限的局部保号性知，存在 M > 0，使得当 x≥M时，<equation>f(x) > \frac{3}{2}</equation>，从而<equation>f(M) > \frac{3}{2} > 1 > 0 = f(0).</equation>又由于<equation>f ( x )</equation>在<equation>[ 0,M]</equation>上可导，从而连续，故由连续函数的介值定理知，存在<equation>0 < a < M</equation>，使得<equation>f ( a )=1.</equation>（Ⅱ）（法一）由于 f(x)在[0,a]上可导，故由拉格朗日中值定理知存在<equation>\xi\in(0,a)</equation>，使得 f(a）<equation>- f(0)=1-0=f^{\prime}(\xi)a</equation>，即<equation>f^{\prime}(\xi)=\frac{1}{a}.</equation>（法二）令<equation>F ( x )=f ( x )-\frac{1}{a} x</equation>，则<equation>F ( a )=f ( a )-1=0</equation>.又由于<equation>F ( 0 )=f ( 0 )-0=0</equation>，且<equation>F ( x )</equation>在<equation>[ 0,a ]</equation>上可导，故由罗尔定理可知，存在<equation>\xi\in(0,a)</equation>，使得<equation>F^{\prime}(\xi)=0</equation>，即<equation>f^{\prime}(\xi)=\frac{1}{a}.</equation>

---

**2010年第19题 | 解答题 | 10分**

19. (本题满分10分)

设函数 f(x)在[0,3]上连续，在(0,3)内存在二阶导数，且<equation>2 f ( 0 )=\int_{0}^{2} f ( x ) \mathrm{d} x=f ( 2 )+f ( 3 )</equation>.

I. 证明存在<equation>\eta \in(0,2)</equation>，使<equation>f(\eta)=f(0);</equation>II. 证明存在<equation>\xi \in(0,3)</equation>，使<equation>f^{\prime \prime}(\xi)=0.</equation>

**答案:**## （19）（I）证明略；（Ⅱ）证明略.

**解析:**证（I）（法一）设<equation>F ( x )=\int_{0}^{x} f ( t ) \mathrm{d} t, 0 \leqslant x \leqslant 2</equation>，则<equation>2 f ( 0 )=\int_{0}^{2} f ( x ) \mathrm{d} x=F ( 2 )-F ( 0 ) \frac{\mathrm{拉格朗日}}{\mathrm{中值定理}} 2 F^{\prime} (\eta)=2 f (\eta), \eta \in(0,2),</equation>即存在<equation>\eta \in(0,2)</equation>，使得<equation>f ( 0 )=f (\eta).</equation>（法二）假设不存在<equation>\eta\in(0,2)</equation>，使得<equation>f(\eta)=f(0)</equation>，则由连续函数的介值定理可知，<equation>f(x)-f(0)</equation>在 （0,2）上恒大于零或者恒小于零，从而积分值<equation>\int_{0}^{2}[f(x)-f(0)]\mathrm{d}x</equation>大于零或者小于零.

另一方面，由题设知，<equation>0 = \int_ {0} ^ {2} f (x) \mathrm {d} x - 2 f (0) = \int_ {0} ^ {2} \left[ f (x) - f (0) \right] \mathrm {d} x.</equation>这与<equation>\int_{0}^{2}[f(x)-f(0)]\mathrm{d}x>0</equation>或<equation>\int_{0}^{2}[f(x)-f(0)]\mathrm{d}x<0</equation>矛盾，故假设不成立，即存在<equation>\eta \in(0,2)</equation>使得<equation>f(\eta)=f(0).</equation>（Ⅱ）（法一）若<equation>f(2) = f(0)</equation>，则由<equation>2 f(0) = f(2) + f(3)</equation>知<equation>f(3) = f(0)</equation>，从而<equation>f(0) = f(2) = f(3).</equation>在区间[0,2],[2,3]上分别使用罗尔定理可知，存在<equation>\eta_{1}\in(0,2),\eta_{2}\in(2,3)</equation>，使得<equation>f^{\prime}(\eta_{1})= f^{\prime}(\eta_{2})=0.</equation>由于<equation>0 < \eta_{1} < 2 < \eta_{2} < 3</equation>，且<equation>f(x)</equation>在<equation>[\eta_{1},\eta_{2}]</equation>上二阶可导，故<equation>f^{\prime}(x)</equation>在<equation>[\eta_{1},\eta_{2}]</equation>上可导，从而由罗尔定理可知存在<equation>\xi \in(\eta_{1},\eta_{2})\subseteq(0,3)</equation>，使得<equation>f^{\prime\prime}(\xi)=0.</equation>若<equation>f ( 2 ) \neq f ( 0 )</equation>，不妨设<equation>f ( 2 ) > f ( 0 )</equation>，则<equation>f ( 3 ) < f ( 0 )</equation>.由连续函数的介值定理知存在<equation>\theta \in</equation>(2,3)，使得<equation>f (\theta)=f(0)</equation>.于是由第（I）问的结论有<equation>f ( 0 )=f (\eta)=f (\theta)</equation><equation>0 < \eta < 2 < \theta < 3.</equation>对区间<equation>[0,\eta ],[\eta ,\theta]</equation>上的<equation>f(x)</equation>分别使用罗尔定理可知，存在<equation>\xi_{1}\in (0,\eta),\xi_{2}\in (\eta ,\theta)</equation>，使得<equation>f^{\prime}(\xi_{1}) = f^{\prime}(\xi_{2}) = 0.</equation>由于<equation>0 < \xi_{1} < \eta < \xi_{2} < \theta</equation>，且<equation>f(x)</equation>在<equation>[\xi_{1},\xi_{2}]</equation>上二阶可导，故<equation>f^{\prime}(x)</equation>在<equation>[\xi_{1},\xi_{2}]</equation>上可导，从而由罗尔定理可知存在<equation>\xi \in (\xi_{1},\xi_{2})\subseteq (0,3)</equation>，使得<equation>f^{\prime \prime}(\xi) = 0.</equation><equation>f ( 2 ) < f ( 0 )</equation><equation>f ( 3 ) > f ( 0 )</equation>时同理可证.

综上所述，存在<equation>\xi \in (0,3)</equation>，使得<equation>f^{\prime \prime}(\xi) = 0.</equation>（法二）由于<equation>\min \{ f(2), f(3)\} \leqslant \frac{f(2)+f(3)}{2}\leqslant \max \{ f(2), f(3)\}</equation>，故由介值定理知存在 a<equation>\in</equation>[2,3]，使得<equation>f(a)=\frac{f(2)+f(3)}{2}=f(0).</equation>于是由第（I）问的结论知<equation>f (0) = f (\eta) = f (a), 0 < \eta < 2 \leqslant a \leqslant 3.</equation>对区间<equation>[0,\eta ],[\eta ,a]</equation>上的<equation>f(x)</equation>分别使用罗尔定理可知，存在<equation>\xi_{1}\in (0,\eta),\xi_{2}\in (\eta ,a)</equation>，使得<equation>f^{\prime}(\xi_{1}) = f^{\prime}(\xi_{2}) = 0.</equation>由于<equation>0 < \xi_{1} < \eta < \xi_{2} < a\leqslant 3,f(x)</equation>在<equation>[\xi_{1},\xi_{2}]</equation>上二阶可导，从而<equation>f^{\prime}(x)</equation>在<equation>[\xi_{1},\xi_{2}]</equation>上可导，故由罗尔定理可知存在<equation>\xi \in (\xi_{1},\xi_{2})\subseteq (0,3)</equation>，使得<equation>f^{\prime \prime}(\xi) = 0.</equation>

---

**2009年第18题 | 解答题 | 10分**

18. (本题满分11分)

I. 证明拉格朗日中值定理：若函数 f(x)在<equation>[a,b]</equation>上连续，在（a,b）内可导，则存在<equation>\xi\in(a,b)</equation>，使得<equation>f(b)-f(a)=f^{\prime}(\xi)(b-a).</equation>II. 证明：若函数 f(x)在 x=0处连续，在<equation>(0,\delta)(\delta>0)</equation>内可导，且<equation>\lim_{x\to 0^{+}}f^{\prime}(x)=A</equation>，则<equation>f_{+}^{\prime}(0)</equation>存在，且<equation>f_{+}^{\prime}(0)=A.</equation>

**答案:**## （18）（I）证明略；（Ⅱ）证明略.

**解析:**证（ I ）令<equation>\varphi (x) = f (x) - f (a) - \frac {f (b) - f (a)}{b - a} (x - a).</equation><equation>\varphi (x)</equation>在<equation>[a,b]</equation>上连续，在<equation>(a,b)</equation>内可导.计算得<equation>\varphi (a) = 0,\varphi (b) = 0.</equation>对<equation>\varphi(x)</equation>使用罗尔定理得，存在<equation>\xi\in(a,b)</equation>，使得<equation>\varphi^{\prime}(\xi)=0</equation>，即<equation>f^{\prime}(\xi)-\frac{f(b)-f(a)}{b-a}=0.</equation>因此，存在<equation>\xi\in(a,b)</equation>，使得<equation>f(b)-f(a)=f^{\prime}(\xi)(b-a).</equation>（Ⅱ）（法一）根据右侧导数的定义，<equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x}.</equation>任取<equation>x\in (0,\delta)</equation>，由题设知，<equation>f(x)</equation>在<equation>[0,x]</equation>上连续，在（0,x）内可导.由拉格朗日中值定理知，存在<equation>\xi_{x}\in (0,x)</equation>，使得<equation>f (x) - f (0) = f ^ {\prime} \left(\xi_ {x}\right) x.</equation>从而<equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x} = \lim _ {x \rightarrow 0 ^ {+}} \frac {f ^ {\prime} \left(\xi_ {x}\right) x}{x} = \lim _ {0 < \xi_ {x} < x, \atop x \rightarrow 0 ^ {+}} f ^ {\prime} \left(\xi_ {x}\right).</equation>由于<equation>x\to 0^{+}</equation>，故<equation>\xi_{x}\rightarrow 0^{+}</equation>.因此，<equation>f _ {+} ^ {\prime} (0) = \lim _ {0 < \xi_ {x} < x, \atop x \rightarrow 0 ^ {+}} f ^ {\prime} \left(\xi_ {x}\right) = \lim _ {x \rightarrow 0 ^ {+}} f ^ {\prime} (x) = A.</equation>（法二）由洛必达法则，<equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x} \xlongequal {\text {洛 必达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {f ^ {\prime} (x)}{1} = A.</equation>因此，<equation>f_{+}^{\prime}(0)</equation>存在，且等于A.

---


#### 微分学在经济学中的应用

**2024年第14题 | 填空题 | 5分**

14. 某产品的价格函数为<equation>p=\left\{\begin{array}{l l}2 5-0. 2 5 Q,&Q \leqslant 2 0,\\ 3 5-0. 7 5 Q,&Q>2 0\end{array}\right.</equation>（p为单价，单位：万元；Q为产量，单位：件），总成本函数为<equation>C=1 5 0+5 Q+0. 2 5 Q^{2}</equation>（万元），则经营该产品可获得的最大利润为___(万元).

**答案:**## 50

**解析:**解 由于利润 = 收益-成本，故当<equation>Q\leqslant 2 0</equation>时，利润函数<equation>L ( Q ) = p Q - C ( Q ) = ( 2 5 - 0. 2 5 Q ) Q - 1 5 0 - 5 Q - 0. 2 5 Q^{2} = - 0. 5 Q^{2} + 2 0 Q - 1 5 0</equation>当<equation>Q > 2 0</equation>时，<equation>L (Q) = p Q - C (Q) = (3 5 - 0. 7 5 Q) Q - 1 5 0 - 5 Q - 0. 2 5 Q ^ {2} = - Q ^ {2} + 3 0 Q - 1 5 0.</equation>于是，<equation>L ( Q ) = \left\{ \begin{array}{ll} - 0. 5 Q^{2} + 2 0 Q - 1 5 0, & Q \leqslant 2 0, \\ - Q^{2} + 3 0 Q - 1 5 0, & Q > 2 0. \end{array} \right.</equation>由于<equation>\lim_{Q\to 20^{-}} L ( Q ) = \lim_{Q\to 20^{+}} L ( Q ) = L ( 2 0 ) = 5 0</equation>，故

L（Q）在分界点<equation>Q=2 0</equation>处连续，从而是连续函数.

又因为当 Q < 20时，<equation>L^{\prime}(Q)=-Q+20>0,L(Q)</equation>单调增加，当 Q > 20时，<equation>L^{\prime}(Q)=-2Q+ 30<0,L(Q)</equation>单调减少，所以 Q = 20是 L（Q）的极大值点，也是最大值点.因此，最大利润为 L（20）= 50（万元）.

---

**2022年第18题 | 解答题 | 12分**

18. (本题满分12分）

设某产品的产量 Q由资本投入量 x和劳动投入量 y决定，生产函数<equation>Q=1 2 x^{\frac{1}{2}} y^{\frac{1}{6}}</equation>，该产品的销售单价 p与产量 Q的关系为<equation>p=1 1 6 0-1. 5 Q</equation>.若单位资本投入和单位劳动投入的价格分别为6和8，求利润最大时的产量.

**答案:**## 利润最大时的产量 Q=384.

**解析:**根据已知条件，该产品的成本函数为 C（x,y）=6x+8y，收益函数为<equation>R ( x,y)=p Q=(1160-1.5 Q) Q=(1160-18 x^{\frac{1}{2}} y^{\frac{1}{6}})\cdot 1 2 x^{\frac{1}{2}} y^{\frac{1}{6}}=1 3 9 2 0 x^{\frac{1}{2}} y^{\frac{1}{6}}-2 1 6 x y^{\frac{1}{3}},</equation>故利润函数为<equation>L (x, y) = R (x, y) - C (x, y) = 1 3 9 2 0 x ^ {\frac {1}{2}} y ^ {\frac {1}{6}} - 2 1 6 x y ^ {\frac {1}{3}} - 6 x - 8 y.</equation>分别计算 L（x,y）关于 x和 y的偏导数.<equation>\left\{ \begin{array}{l} L _ {x} ^ {\prime} (x, y) = 6 9 6 0 x ^ {- \frac {1}{2}} y ^ {\frac {1}{6}} - 2 1 6 y ^ {\frac {1}{3}} - 6 = \frac {3 \left(2 3 2 0 x ^ {\frac {1}{2}} y ^ {\frac {1}{6}} - 7 2 x y ^ {\frac {1}{3}}\right)}{x} - 6, \\ L _ {y} ^ {\prime} (x, y) = 2 3 2 0 x ^ {\frac {1}{2}} y ^ {- \frac {5}{6}} - 7 2 x y ^ {- \frac {2}{3}} - 8 = \frac {2 3 2 0 x ^ {\frac {1}{2}} y ^ {\frac {1}{6}} - 7 2 x y ^ {\frac {1}{3}}}{y} - 8. \end{array} \right.</equation>令<equation>\left\{\begin{array}{l l}L_{x}^{\prime}(x,y)=0,\\ L_{y}^{\prime}(x,y)=0,\end{array} \right.</equation>可得<equation>\left\{\begin{array}{l l}2320x^{\frac{1}{2}}y^{\frac{1}{6}}-72xy^{\frac{1}{3}}=2x,\\ 2320x^{\frac{1}{2}}y^{\frac{1}{6}}-72xy^{\frac{1}{3}}=8y.\end{array} \right.</equation>于是，<equation>x=4y</equation>进一步，将 x=4y 代入 2<equation>3 2 0 x^{\frac{1}{2}} y^{\frac{1}{6}}-7 2 x y^{\frac{1}{3}}=8 y</equation>即<equation>2 9 0 x^{\frac{1}{2}} y^{\frac{1}{6}}-9 x y^{\frac{1}{3}}=y</equation>可得，<equation>5 8 0 y^{\frac{2}{3}}-3 6 y^{\frac{4}{3}}=y.</equation>等式两端同时除 y 可得<equation>5 8 0 y^{-\frac{1}{3}}-3 6 y^{\frac{1}{3}}=1.</equation>(1)

令<equation>z=y^{\frac{1}{3}}</equation>，则（1）式可整理为<equation>3 6 z^{2}+z-5 8 0=0</equation>.由求根公式可得<equation>z=\frac{-1\pm \sqrt{1+4\times 3 6\times 5 8 0}}{7 2}</equation>解得<equation>z=4</equation>或<equation>z=-\frac{1 4 5}{3 6}</equation>（舍去）.于是，<equation>y=z^{3}=6 4,x=4 y=2 5 6,L(x,y)</equation>的唯一驻点为（256，64）.

由问题的实际意义可知，最大利润必定存在，故最大利润在驻点（256，64）处取得。此时，<equation>Q= 1 2 \times\sqrt{2 5 6} \times\sqrt[6]{6 4}=1 2 \times1 6 \times2=3 8 4.</equation>因此，当利润最大时，产量<equation>Q=3 8 4.</equation>

---

**2020年第11题 | 填空题 | 4分**

11. 设某厂家生产某产品的产量为 Q，成本<equation>C(Q)=1 0 0+1 3 Q</equation>，该产品的单价为 p，需求量<equation>q ( p )=\frac{8 0 0}{p+3}-2</equation>，则该厂家获得最大利润时的产量为 ___.

**解析:**解 根据经济学的含义，获得最大利润时，应满足产销平衡，即需求量等于产量。由需求量与价格的关系，将价格 p写成需求量 q的函数，进而将利润写成需求量 q的函数.

由<equation>q ( p )=\frac{8 0 0}{p+3}-2</equation>可得<equation>p ( q )=\frac{8 0 0}{q+2}-3.</equation>由利润 = 价格<equation>\times</equation>需求-成本可得，<equation>L (q) = p (q) q - C (q) = \left(\frac {8 0 0}{q + 2} - 3\right) q - 1 3 q - 1 0 0.</equation><equation>L ^ {\prime} (q) = \frac {8 0 0}{q + 2} - 3 + q \cdot \left[ - \frac {8 0 0}{(q + 2) ^ {2}} \right] - 1 3 = \frac {1 6 0 0 - 1 6 (q + 2) ^ {2}}{(q + 2) ^ {2}}.</equation>令<equation>L^{\prime}(q)=0</equation>，可得<equation>(q+2)^{2}=100</equation>.由 q>0可得 q=8.当 0 < q < 8时，<equation>L^{\prime}(q)>0,L(q)</equation>单调增加；当 q>8时，<equation>L^{\prime}(q)<0,L(q)</equation>单调减少.因此， q=8为 L(q) 的最大值点，当 q=8时， L(q) 最大.因此，获得最大利润时的产量 Q=8.

---

**2019年第12题 | 填空题 | 4分**

12. 以<equation>P_{\mathrm{A}}, P_{\mathrm{B}}</equation>分别表示 A，B两个商品的价格，设商品 A的需求函数<equation>Q_{\mathrm{A}}=5 0 0-P_{\mathrm{A}}^{2}-P_{\mathrm{A}} P_{\mathrm{B}}+2 P_{\mathrm{B}}^{2}</equation>，则当<equation>P_{\mathrm{A}}= 1 0, P_{\mathrm{B}}=2 0</equation>时，商品 A的需求量对自身价格的弹性<equation>\eta_{\mathrm{A A}}(\eta_{\mathrm{A A}}>0)=</equation>___

**解析:**解<equation>Q_{\mathrm{A}}</equation>可看作关于<equation>P_{\mathrm{A}}</equation>、<equation>P_{\mathrm{B}}</equation>的二元函数，则商品A对自身价格的需求弹性<equation>\eta_ {\mathrm {A A}} = - \frac {P _ {\mathrm {A}}}{Q _ {\mathrm {A}}} \cdot \frac {\partial Q _ {\mathrm {A}}}{\partial P _ {\mathrm {A}}} = - \frac {P _ {\mathrm {A}}}{Q _ {\mathrm {A}}} \cdot \left(- 2 P _ {\mathrm {A}} - P _ {\mathrm {B}}\right).</equation>代入<equation>P_{\mathrm{A}}=10</equation><equation>P_{\mathrm{B}}=20</equation>，可得<equation>\eta_ {\mathrm {A A}} = - \frac {1 0}{5 0 0 - 1 0 0 - 2 0 0 + 8 0 0} \times (- 2 0 - 2 0) = 0. 4.</equation>

---

**2018年第4题 | 选择题 | 4分 | 答案: D**

4. 设某产品的成本函数 C(Q)可导，其中Q为产量.若产量为<equation>Q_{0}</equation>时平均成本最小，则（    )

A.<equation>C^{\prime}(Q_{0})=0</equation>B.<equation>C^{\prime}(Q_{0})=C(Q_{0})</equation>C.<equation>C^{\prime}(Q_{0})=Q_{0}C(Q_{0})</equation>D.<equation>Q_{0}C^{\prime}(Q_{0})=C(Q_{0})</equation>

答案: D

**解析:**由于<equation>\overline{C} ( Q )=\frac{C ( Q )}{Q}</equation>，故<equation>\bar {C} ^ {\prime} (Q) = \frac {Q C ^ {\prime} (Q) - C (Q)}{Q ^ {2}}.</equation>又因为当<equation>Q=Q_{0}</equation>时，平均成本最小，所以<equation>\overline{{C}}^{\prime}(Q_{0})=0</equation>即<equation>Q_{0}C^{\prime}(Q_{0})-C(Q_{0})=0</equation>也即<equation>Q_{0}C^{\prime}(Q_{0})=C(Q_{0}).</equation>因此，应选D.

---

**2017年第11题 | 填空题 | 4分**

11. 设生产某产品的平均成本为<equation>\bar{C} (Q)=1+\mathrm{e}^{-Q}</equation>, 其中产量为<equation>Q</equation>, 则边际成本为 ___

**答案:**<equation>1 + \mathrm {e} ^ {- Q} - Q \mathrm {e} ^ {- Q}.</equation>

**解析:**解 根据题意，总成本<equation>C ( Q ) = ( 1 + \mathrm{e}^{- Q} ) Q</equation>因此，边际成本<equation>C^{\prime} ( Q ) = 1 + \mathrm{e}^{- Q} - Q \mathrm{e}^{- Q}.</equation>

---

**2016年第16题 | 解答题 | 10分**

16. (本题满分10分)

设某商品的最大需求量为1200件，该商品的需求函数<equation>Q=Q(p)</equation>，需求弹性<equation>\eta=\frac{p}{120-p}</equation><equation>(\eta>0)</equation>，p为单价（万元）.

I. 求需求函数的表达式；

II. 求 p=100万元时的边际收益，并说明其经济意义.

**答案:**（I）<equation>Q ( p )=1 2 0 0-1 0 p.</equation>（Ⅱ）当 p=100万元时，边际收益为80万元.其经济意义为，当 p=100万元，Q=200件时，销售第201件商品所得的收益为80万元.

**解析:**解（I）由需求弹性的定义知，<equation>\eta=-Q^{\prime}(p)\frac{p}{Q(p)}.</equation>由题设知，<equation>\eta=\frac{p}{120-p}>0</equation>即 0 < p < 120.于是，<equation>- Q ^ {\prime} (p) \frac {p}{Q (p)} = \frac {p}{1 2 0 - p}, \quad 0 < p < 1 2 0.</equation>整理得<equation>\frac {Q ^ {\prime} (p)}{Q (p)} = \frac {- 1}{1 2 0 - p}, \quad 0 < p < 1 2 0.</equation>对上式两端求不定积分可得<equation>\ln[Q(p)]=\ln(120-p)+C</equation>，其中C为待定常数.从而，<equation>Q (p) = C _ {1} (1 2 0 - p), \quad C _ {1} = \mathrm {e} ^ {c}, \quad 0 < p < 1 2 0.</equation>又由题设知，<equation>1\ 200=Q(0)=\lim_{p\to 0}Q(p)=120C_{1}</equation>，解得<equation>C_{1}=10</equation>因此，需求函数的表达式为<equation>Q(p)=1\ 200-10p.</equation>（Ⅱ）由第（Ⅰ）问可知，<equation>p=\frac{1200-Q}{10}</equation>，故收益函数<equation>R(Q)=pQ=\frac{(1200-Q)Q}{10}=\frac{1200Q-Q^{2}}{10}.</equation>于是，该商品的边际收益为<equation>\frac {\mathrm {d} R}{\mathrm {d} Q} = \frac {1 2 0 0 - 2 Q}{1 0} = \frac {6 0 0 - Q}{5}.</equation>当 p=100时，<equation>Q=200</equation>因此，此时的边际收益为<equation>\left.\frac{\mathrm{d}R}{\mathrm{d}Q}\right|_{Q=200}=\frac{600-200}{5}=80.</equation>综上所述，当 p=100万元时，边际收益为80万元.其经济意义为，当 p=100万元，Q=200件时，销售第201件商品所得的收益为80万元.

---

**2015年第17题 | 解答题 | 10分**


为了实现利润最大化，厂商需要对某商品确定其定价模型.设Q为该商品的需求量，p为价格，MC为边际成本，<equation>\eta</equation>为需求弹性（<equation>\eta >0</equation>）.

I. 证明定价模型为<equation>p=\frac{MC}{1-\frac{1}{\eta}};</equation>II. 若该商品的成本函数为<equation>C ( Q )=1 6 0 0+Q^{2}</equation>，需求函数为<equation>Q=4 0-p</equation>，试由第一问中的定价模型确定此商品的价格.

**解析:**解（I）利润函数<equation>L ( Q )=R ( Q )-C ( Q )=Q p-C ( Q )</equation>，其中R（Q）为总收益函数，C（Q）为总成本函数，于是<equation>L ^ {\prime} (Q) = p + Q \frac {\mathrm {d} p}{\mathrm {d} Q} - \frac {\mathrm {d} [ C (Q) ]}{\mathrm {d} Q} = p + Q \frac {\mathrm {d} p}{\mathrm {d} Q} - M C.</equation>又由需求弹性的定义知<equation>\eta=-\frac{\mathrm{d} Q}{\mathrm{d} p}\cdot \frac{p}{Q}</equation>，故<equation>\frac{\mathrm{d} p}{\mathrm{d} Q}=-\frac{p}{Q\eta}.</equation>从而，<equation>L ^ {\prime} (Q) = p - \frac {p}{\eta} - M C = p \left(1 - \frac {1}{\eta}\right) - M C.</equation>当 L(Q) 取得最大值时，<equation>L^{\prime}(Q)=0</equation>，即<equation>p=\frac{MC}{1-\frac{1}{\eta}}.</equation>因此，为了实现利润最大化，定价模型应设为<equation>p=\frac{MC}{1-\frac{1}{\eta}}.</equation>（Ⅱ）由题设知，边际成本<equation>MC=C^{\prime}(Q)=2 Q=8 0-2 p</equation><equation>\eta=-\frac{\mathrm{d} Q}{\mathrm{d} p}\cdot \frac{p}{Q}=\frac{p}{4 0-p}.</equation>代入第（I）问所得定价模型可得<equation>p = \frac {8 0 - 2 p}{1 - \frac {4 0 - p}{p}}.</equation>解得<equation>p = 30.</equation>因此，所求商品的价格为30.

---

**2014年第9题 | 填空题 | 4分**

9. 设某商品的需求函数为<equation>Q=40-2P</equation>(P为商品的价格),则该商品的边际收益为 ___

**解析:**解 由题设知，价格函数<equation>P=\frac{4 0-Q}{2}</equation>，故该商品的总收益函数<equation>R(Q)=P Q=\frac{4 0-Q}{2} \cdot Q= 2 0 Q-\frac{Q^{2}}{2}.</equation>因此，该商品的边际收益为<equation>R^{\prime}(Q)=2 0-Q.</equation>

---

**2013年第18题 | 解答题 | 10分**


8. (本题满分10分)

设生产某商品的固定成本为60000元，可变成本为20元/件，价格函数为<equation>p=60-\frac{Q}{1000}</equation>（ p是单价，单位：元；

Q是销量，单位：件）. 已知产销平衡，求：

I. 该商品的边际利润；

II. 当 p=50时的边际利润，并解释其经济意义；

III. 使得利润最大的定价 p.

**答案:**(18) （I）<equation>L^{\prime}(Q)=40-\frac{Q}{500}.</equation>（Ⅱ）当 p=50时，边际利润为20.其经济意义为，当 p=50时，销售第10001件商品时所得的利润为20元.

（Ⅲ）当定价为40元时，利润最大.

**解析:**解（I）由于该商品的成本函数为<equation>C ( Q )=6 0\ 0 0 0+2 0 Q</equation>，收益函数为<equation>R ( Q )=p Q=6 0 Q-\frac{Q^{2}}{1\ 0 0 0}</equation>，故利润函数为<equation>L (Q) = R (Q) - C (Q) = 4 0 Q - \frac {Q ^ {2}}{1 0 0 0} - 6 0 0 0 0.</equation>因此，该商品的边际利润为<equation>L^{\prime}(Q)=40-\frac{Q}{500}.</equation>（Ⅱ）当 p=50时，<equation>Q=1 0 0 0 0</equation>，此时边际利润为<equation>L^{\prime}(Q)\bigg|_{1 0 0 0 0}=4 0-\frac{Q}{5 0 0}\bigg|_{1 0 0 0 0}=2 0.</equation>其经济意义为，当 p=50时，销售第10001件商品时所得的利润为20元.

（Ⅲ）令<equation>L^{\prime}(Q)=0</equation>，解得<equation>Q=20000</equation>.又由于<equation>L^{\prime\prime}(20000)=-\frac{1}{500}<0</equation>，故当<equation>Q=20000</equation>时，L（Q）取得最大值，此时<equation>p=60-\frac{Q}{1000}=40.</equation>因此，当定价为40元时，利润最大.

---

**2010年第11题 | 填空题 | 4分**

11. 设某商品的收益函数为<equation>R(p)</equation>,收益弹性为<equation>1+p^{3}</equation>,其中<equation>p</equation>为价格,且<equation>R(1)=1</equation>,则<equation>R(p)=</equation>___.

**答案:**<equation>p e ^ {\frac {p ^ {3} - 1}{3}}.</equation>

**解析:**由收益弹性的定义及题设可知<equation>\frac {p}{R (p)} R ^ {\prime} (p) = 1 + p ^ {3}.</equation>此为可分离变量的微分方程. 分离变量得，<equation>\frac {\mathrm {d} R}{R} = \left(\frac {1}{p} + p ^ {2}\right) \mathrm {d} p.</equation>方程两端积分可得<equation>\ln R=\ln p+\frac{p^{3}}{3}+C</equation>，其中C为待定常数.于是<equation>R(p)=p\mathrm{e}^{\frac{p^{3}}{3}+C}.</equation>将<equation>R(1)=1</equation>代入上式解得<equation>C=-\frac{1}{3}.</equation>因此，<equation>R(p)=p\mathrm{e}^{\frac{p^{3}-1}{3}}.</equation>

---

**2009年第12题 | 填空题 | 4分**

12. 设某产品的需求函数为<equation>Q=Q(p)</equation>，其对价格 p的弹性<equation>\varepsilon_{p}=0.2</equation>，则当需求量为10000件时，价格增加1元会使产品收益增加 ___元.

**答案:**## 8000.

**解析:**解 由需求弹性的定义知<equation>\varepsilon_{p}=-Q^{\prime}(p)\cdot \frac{p}{Q}=0.2</equation>因为收益函数为<equation>R ( p )=Q ( p )\cdot p</equation>所以，<equation>\frac{\mathrm{d} R}{\mathrm{d} p}=Q^{\prime}(p) p+Q ( p )=Q ( p ) \left[ \frac{Q^{\prime}(p)}{Q ( p )} p+1 \right]=Q ( p ) \left( 1-\varepsilon_{p} \right).</equation>由微分的经济学意义知，当需求量为10000件，价格增加1元时，即<equation>Q=1 0 0 00</equation><equation>\mathrm{d} p=1</equation>时，产品的收益会增加<equation>\mathrm{d} R=Q(p)(1-\varepsilon_{p})\mathrm{d} p=1 0 0 0 0 \times(1-0. 2) \times1=8 0 0 0</equation>（元）.

---


#### 泰勒公式

**2024年第20题 | 解答题 | 12分**

20. (本题满分12分)

设函数 f(x)具有2阶导数，且<equation>f^{\prime}(0)=f^{\prime}(1),\left| f^{\prime\prime}(x)\right| \leqslant 1</equation>证明：

I. 当 x<equation>\in(0,1)</equation>时，<equation>|f(x)-f(0)(1-x)-f(1)x|\leqslant \frac{x(1-x)}{2}</equation>II.<equation>\left| \int_{0}^{1} f(x)\mathrm{d}x-\frac{f(0)+f(1)}{2}\right| \leqslant \frac{1}{12}.</equation>

**解析:**证（I）（法一）分别写出<equation>f(x)</equation>在<equation>x=0</equation>与<equation>x=1</equation>处的一阶泰勒公式.<equation>f (x) = f (0) + f ^ {\prime} (0) x + \frac {f ^ {\prime \prime} \left(\xi_ {1}\right) x ^ {2}}{2},</equation><equation>f (x) = f (1) + f ^ {\prime} (1) (x - 1) + \frac {f ^ {\prime \prime} \left(\xi_ {2}\right) \left(x - 1\right) ^ {2}}{2},</equation>其中<equation>\xi_{1}</equation>介于0与x之间，<equation>\xi_{2}</equation>介于1与x之间.

(2) 式<equation>\times x-</equation>(1)式<equation>\times(x-1)</equation>，并结合<equation>f^{\prime}(0)=f^{\prime}(1)</equation>可得<equation>f (x) = f (0) (1 - x) + f (1) x + \frac {x (x - 1)}{2} \left[ f ^ {\prime \prime} \left(\xi_ {2}\right) (x - 1) - f ^ {\prime \prime} \left(\xi_ {1}\right) x \right].</equation>由（3）式可得，当<equation>x\in(0,1)</equation>时，<equation>\left| f (x) - f (0) (1 - x) - f (1) x \right| = \frac {x (1 - x)}{2} \left| f ^ {\prime \prime} \left(\xi_ {2}\right) (x - 1) - f ^ {\prime \prime} \left(\xi_ {1}\right) x \right|.</equation>由于<equation>| f^{\prime \prime}(\xi_{2})(x - 1) - f^{\prime \prime}(\xi_{1})x | \leqslant | f^{\prime \prime}(\xi_{2}) | (1 - x) + | f^{\prime \prime}(\xi_{1}) | x</equation>，故结合<equation>| f^{\prime \prime}(x) | \leqslant 1</equation>以及（4）式可得<equation>| f (x) - f (0) (1 - x) - f (1) x | \leqslant \frac {x (1 - x)}{2} \cdot [ (1 - x) + x ] = \frac {x (1 - x)}{2}.</equation>（法二）所证命题等价于当<equation>x\in (0,1)</equation>时，<equation>- \frac {x (1 - x)}{2} \leqslant f (x) - f (0) (1 - x) - f (1) x \leqslant \frac {x (1 - x)}{2}.</equation>令<equation>F ( x ) = f ( x ) - f ( 0 ) ( 1 - x ) - f ( 1 ) x - \frac { x ( 1 - x ) } { 2 }</equation>，则<equation>F ( 0 ) = F ( 1 ) = 0</equation>，且<equation>F^{\prime \prime}(x)=f^{\prime \prime}(x)</equation>+1.由于<equation>| f^{\prime \prime}(x) | \leqslant 1</equation>，故<equation>F^{\prime \prime}(x)\geqslant 0.</equation>下面证明当<equation>x\in (0,1)</equation>时，<equation>F(x)\leqslant 0.</equation>若存在<equation>c\in(0,1)</equation>，使得<equation>F(c)>0</equation>，则分别对<equation>[0,c],[c,1]</equation>上的<equation>F(x)</equation>使用拉格朗日中值定理可得，存在<equation>\xi_{1}\in(0,c),\xi_{2}\in(c,1)</equation>，使得<equation>F ^ {\prime} \left(\xi_ {1}\right) = \frac {F (c) - F (0)}{c - 0} > 0, \quad F ^ {\prime} \left(\xi_ {2}\right) = \frac {F (1) - F (c)}{1 - c} < 0.</equation>再对<equation>[\xi_{1},\xi_{2} ]</equation>上的<equation>F^{\prime}(x)</equation>使用拉格朗日中值定理可得，存在<equation>\xi\in(\xi_{1},\xi_{2})</equation>，使得<equation>F ^ {\prime \prime} (\xi) = \frac {F ^ {\prime} \left(\xi_ {2}\right) - F ^ {\prime} \left(\xi_ {1}\right)}{\xi_ {2} - \xi_ {1}} < 0.</equation>这与<equation>F^{\prime \prime}(x)\geqslant 0</equation>矛盾.

因此，当<equation>x\in (0,1)</equation>时，<equation>F(x)\leqslant 0</equation>，即<equation>f(x) - f(0)(1 - x) - f(1)x\leqslant \frac{x(1 - x)}{2}.</equation>令<equation>G(x) = f(x) - f(0)(1 - x) - f(1)x + \frac{x(1 - x)}{2}</equation>，同理可得<equation>G^{\prime \prime}(x)\leqslant 0</equation>，且进一步可得当<equation>x\in</equation>(0,1)时，<equation>G(x)\geqslant 0</equation>，即<equation>f(x) - f(0)(1 - x) - f(1)x\geqslant -\frac{x(1 - x)}{2}</equation>.

综上所述，所证命题成立.

（Ⅱ）由第（Ⅰ）问可得<equation>\left| f (x) - f (0) (1 - x) - f (1) x \right| \leqslant \frac {x (1 - x)}{2}.</equation>对（5）式两端从0到1积分可得，<equation>\begin{aligned} \int_ {0} ^ {1} | f (x) - f (0) (1 - x) - f (1) x | \mathrm {d} x \leqslant \int_ {0} ^ {1} \frac {x (1 - x)}{2} \mathrm {d} x &= \frac {1}{2} \int_ {0} ^ {1} \left(x - x ^ {2}\right) \mathrm {d} x \\ &= \frac {1}{2} \left(\frac {x ^ {2}}{2} - \frac {x ^ {3}}{3}\right) \Big | _ {0} ^ {1} = \frac {1}{1 2}. \end{aligned}</equation>进一步由定积分的性质可得<equation>\begin{array}{l} \left| \int_ {0} ^ {1} f (x) \mathrm {d} x - f (0) \int_ {0} ^ {1} (1 - x) \mathrm {d} x - f (1) \int_ {0} ^ {1} x \mathrm {d} x \right| = \left| \int_ {0} ^ {1} f (x) \mathrm {d} x - \frac {f (0) + f (1)}{2} \right| \\ \leqslant \int_ {0} ^ {1} | f (x) - f (0) (1 - x) - f (1) x | \mathrm {d} x \leqslant \frac {1}{1 2}. \\ \end{array}</equation>

---

**2023年第20题 | 解答题 | 12分**

20. (本题满分12分)

设函数 f(x)在<equation>[-a,a]</equation>上有二阶连续导数.证明：

I. 若 f(0)=0，则存在<equation>\xi\in(-a,a)</equation>，使得<equation>f^{\prime\prime}(\xi)=\frac{1}{a^{2}}[f(a)+f(-a)]；

II. 若 f(x)在</equation>(-a,a)<equation>内取得极值，则存在</equation>\eta\in(-a,a)<equation>，使得</equation>|f^{\prime\prime}(\eta)|\geqslant\frac{1}{2a^{2}}|f(a)-f(-a)|. $

**答案:**# （I）证明略；

（Ⅱ）证明略.

**解析:**证（ I ）由 f（ x ）的泰勒公式可得<equation>f (a) = f (0) + f ^ {\prime} (0) a + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {1}\right) a ^ {2} \stackrel {f (0) = 0} {=} f ^ {\prime} (0) a + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {1}\right) a ^ {2},</equation><equation>f (- a) = f (0) + f ^ {\prime} (0) \cdot (- a) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {2}\right) a ^ {2} \stackrel {f (0) = 0} {=} f ^ {\prime} (0) \cdot (- a) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {2}\right) a ^ {2},</equation>其中<equation>\xi_{1}\in(0,a),\xi_{2}\in(-a,0).</equation>两式相加可得<equation>f (a) + f (- a) = \frac {a ^ {2}}{2} \left[ f ^ {\prime \prime} \left(\xi_ {1}\right) + f ^ {\prime \prime} \left(\xi_ {2}\right) \right].</equation>记<equation>\max \left\{f^{\prime \prime}\left(\xi_{1}\right),f^{\prime \prime}\left(\xi_{2}\right)\right\}=M,</equation><equation>\min \left\{f^{\prime \prime}\left(\xi_{1}\right),f^{\prime \prime}\left(\xi_{2}\right)\right\}=m</equation>，则由（1）式可得<equation>m \leqslant \frac {f (a) + f (- a)}{a ^ {2}} = \frac {1}{2} \left[ f ^ {\prime \prime} \left(\xi_ {1}\right) + f ^ {\prime \prime} \left(\xi_ {2}\right) \right] \leqslant M.</equation>由于 f(x)在<equation>[-a,a]</equation>上有二阶连续导数，故由连续函数的介值定理可知，存在<equation>\xi \in[ \xi_{2},\xi_{1} ]\subset(-a,a)</equation>，使得<equation>f^{\prime \prime}(\xi)=\frac{1}{a^{2}}[f(a)+f(-a)]</equation>（Ⅱ）设<equation>f(x)</equation>在<equation>(-a,a)</equation>内的极值点为<equation>x_{0}</equation>，则<equation>f^{\prime}(x_{0})=0.</equation>由<equation>f(x)</equation>的泰勒公式可得<equation>\begin{array}{l} f (a) = f \left(x _ {0}\right) + f ^ {\prime} \left(x _ {0}\right) \left(a - x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {1}\right) \left(a - x _ {0}\right) ^ {2} \\ \frac {f ^ {\prime} \left(x _ {0}\right) = 0}{\overline {{=}}} f \left(x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {1}\right) \left(a - x _ {0}\right) ^ {2}, \\ \end{array}</equation><equation>\begin{aligned} f (- a) &= f \left(x _ {0}\right) + f ^ {\prime} \left(x _ {0}\right) \left(- a - x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {2}\right) \left(- a - x _ {0}\right) ^ {2} \\ \frac {f ^ {\prime} \left(x _ {0}\right) = 0}{\overline {{}}} f \left(x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {2}\right) \left(a + x _ {0}\right) ^ {2}, \end{aligned}</equation>其中<equation>\eta_{1}\in(x_{0},a),\eta_{2}\in(-a,x_{0}).</equation>两式相减可得<equation>f (a) - f (- a) = \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {1}\right) \left(a - x _ {0}\right) ^ {2} - \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {2}\right) \left(a + x _ {0}\right) ^ {2}.</equation>记<equation>\max \left\{ \left| f^{\prime \prime}\left(\eta_{1}\right)\right|, \left| f^{\prime \prime}\left(\eta_{2}\right)\right| \right\}=M</equation>，则由（2）式可得<equation>\left| f (a) - f (- a) \right| \leqslant \frac {M}{2} \left[ \left(a - x _ {0}\right) ^ {2} + \left(a + x _ {0}\right) ^ {2} \right] = \frac {M}{2} \left(2 a ^ {2} + 2 x _ {0} ^ {2}\right) \leqslant \frac {M}{2} \cdot 4 a ^ {2} = 2 a ^ {2} M.</equation>因此，<equation>M\geqslant \frac{1}{2a^{2}}|f(a) - f(-a)|.</equation>取<equation>\eta \in \{\eta_1, \eta_2\}</equation>使得<equation>|f^{\prime \prime}(\eta)| = M</equation>，则<equation>\eta \in (-a, a)</equation>满足<equation>|f^{\prime \prime}(\eta)| \geqslant \frac{1}{2a^2}|f(a) - f(-a)|</equation>.

---


#### 函数的单调性、极值与最值

**2023年第17题 | 解答题 | 10分**

17. (本题满分10分)

已知可导函数 y=y(x)满足<equation>a \mathrm{e}^{x}+y^{2}+y-\ln(1+x)\cos y+b=0</equation>，且 y(0)=0，<equation>y^{\prime}(0)=0</equation>I. 求 a,b的值；

II. 判断 x=0 是否为 y(x)的极值点.

**答案:**（ I ）<equation>a=1,b=-1;</equation>（ II ）<equation>x=0</equation>是 y(x）的极大值点.

**解析:**解（I）将 y（0）=0代入<equation>a \mathrm{e}^{x}+y^{2}+y-\ln(1+x)\cos y+b=0</equation>中可得，a+b=0.对方程<equation>a \mathrm{e}^{x}+y^{2}+y-\ln(1+x)\cos y+b=0</equation>两端关于 x求导，可得<equation>a \mathrm {e} ^ {x} + 2 y y ^ {\prime} + y ^ {\prime} - \frac {\cos y}{1 + x} + \ln (1 + x) y ^ {\prime} \sin y = 0.</equation>将<equation>y ( 0 )=0, y^{\prime} ( 0 )=0</equation>代入（1）式，可得<equation>a-1=0.</equation>联立可得<equation>\left\{ \begin{array}{l l} a + b = 0, \\ a - 1 = 0, \end{array} \right.</equation>解得<equation>\left\{ \begin{array}{l l} a = 1, \\ b = -1. \end{array} \right.</equation>（Ⅱ）由<equation>y^{\prime}(0)=0</equation>可知 x=0为 y(x）的驻点.如果能确定<equation>y^{\prime\prime}(0)</equation>的符号，那么就能利用一元函数极值的第二充分条件判断 x=0是否为极值点.

将 a=1 代入（1）式，可得<equation>\mathrm {e} ^ {x} + 2 y y ^ {\prime} + y ^ {\prime} - \frac {\cos y}{1 + x} + \ln (1 + x) y ^ {\prime} \sin y = 0.</equation>对（2）式两端关于 x求导，可得<equation>\mathrm {e} ^ {x} + 2 \left(y ^ {\prime}\right) ^ {2} + 2 y y ^ {\prime \prime} + y ^ {\prime \prime} + \frac {\cos y}{(1 + x) ^ {2}} + \frac {2 y ^ {\prime} \sin y}{1 + x} + \ln (1 + x) y ^ {\prime \prime} \sin y + \ln (1 + x) \left(y ^ {\prime}\right) ^ {2} \cos y = 0.</equation>将<equation>y ( 0 ) = 0, y^{\prime} ( 0 ) = 0</equation>代入（3）式可得<equation>y^{\prime \prime} ( 0 ) + 2 = 0.</equation>于是，<equation>y^{\prime \prime} ( 0 ) = - 2 < 0.</equation>由一元函数极值的第二充分条件可知，<equation>x=0</equation>是<equation>y(x)</equation>的极大值点.

---

**2019年第15题 | 解答题 | 10分**

15. (本题满分10分）

已知函数<equation>f ( x )=\left\{\begin{array}{ll}x^{2 x},&x>0,\\ x \mathrm{e}^{x}+1,&x\leqslant 0.\end{array} \right.</equation>求<equation>f^{\prime}(x)</equation>，并求 f(x)的极值.

**答案:**)<equation>f^{\prime}(x)=\left\{\begin{array}{ll}\mathrm{e}^{x}(x+1),&x<0,\\ 2\mathrm{e}^{2x\ln x}(\ln x+1),&x>0.\end{array} \right.</equation>x=-1和 x<equation>=\frac{1} {\mathrm{e}}</equation>是 f(x)的极小值点，极小值分别为 f(-1) =1<equation>-\mathrm{e}^{-1}</equation>和<equation>f\left(\frac{1}{\mathrm{e}}\right)=\mathrm{e}^{-\frac{2}{\mathrm{e}}}</equation>；x=

0是 f(x)的极大值点，极大值为 f(0) =1.

**解析:**解 f(x)是一个分段函数. x=0是分界点.分别计算 x > 0时与 x < 0时的<equation>f^{\prime}(x).</equation>当 x > 0时，<equation>f ^ {\prime} (x) = \left(x ^ {2 x}\right) ^ {\prime} = \left(\mathrm {e} ^ {2 x \ln x}\right) ^ {\prime} = \mathrm {e} ^ {2 x \ln x} \cdot \left(2 \ln x + 2 x \cdot \frac {1}{x}\right) = 2 \mathrm {e} ^ {2 x \ln x} (\ln x + 1).</equation>当 x < 0时，<equation>f ^ {\prime} (x) = \mathrm {e} ^ {x} + x \mathrm {e} ^ {x} = \mathrm {e} ^ {x} (x + 1).</equation>计算<equation>f^{\prime}(0).</equation>由<equation>f ( x )</equation>的定义知<equation>f ( 0 )=1.</equation><equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0 ^ {-}} \frac {x \mathrm {e} ^ {x} + 1 - 1}{x} = \lim _ {x \rightarrow 0 ^ {-}} \mathrm {e} ^ {x} = 1.</equation><equation>\begin{aligned} f _ {+} ^ {\prime} (0) &= \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {2 x \ln x} - 1}{x} \frac {\mathrm {e} ^ {2 x \ln x} - 1 \sim 2 x \ln x}{\lim _ {x \rightarrow 0 ^ {+}} \frac {2 x \ln x}{x}} \\ &= 2 \lim _ {x \rightarrow 0 ^ {+}} \ln x = - \infty . \end{aligned}</equation><equation>f ( x )</equation>的右导数不存在，故<equation>f ( x )</equation>在<equation>x=0</equation>处不可导.

因此，<equation>f^{\prime}(x)=\left\{ \begin{array}{ll}\mathrm{e}^{x}(x+1),&x<0,\\ 2\mathrm{e}^{2x\ln x}(\ln x+1),&x>0. \end{array} \right.</equation>考察 f（x）的极值，需分别考察 f（x）的驻点与不可导点.

令<equation>f^{\prime}(x)=0</equation>当 x > 0时，解得<equation>x=\frac{1} {\mathrm{e}}</equation>当 x < 0时，解得 x=-1.加上不可导点 x=0，这三个点将<equation>(-\infty, +\infty)</equation>分为4个区间.

当 x < -1时，<equation>f^{\prime}(x) < 0,f(x)</equation>单调减少.

当<equation>- 1 < x < 0</equation>时，<equation>f^{\prime}(x) > 0,f(x)</equation>单调增加.

当<equation>0 < x < \frac{1} {\mathrm{e}}</equation>时，<equation>f^{\prime}(x) < 0,f(x)</equation>单调减少.

当 x ><equation>\frac{1} {\mathrm{e}}</equation>时，<equation>f^{\prime}(x) > 0</equation>f(x)单调增加.

注意到 f(x)在 x=0处连续.于是，根据极值的第一充分条件，<equation>x=-1</equation>和<equation>x=\frac{1} {\mathrm{e}}</equation>是 f(x)的极小值点，极小值分别为<equation>f(-1)=1-\mathrm{e}^{-1}</equation>和<equation>f\left(\frac{1}{\mathrm{e}}\right)=\mathrm{e}^{-\frac{2}{\mathrm{e}}}</equation>；x=0是 f(x)的极大值点，极大值为<equation>f(0)=1.</equation>f（x）的单调性与极值可整理如下.

<table border="1"><tr><td>x</td><td><equation>(-\infty,-1)</equation></td><td>-1</td><td><equation>(-1,0)</equation></td><td>0</td><td><equation>(0,\frac{1}{e})</equation></td><td><equation>\frac{1}{e}</equation></td><td><equation>(\frac{1}{e},+\infty)</equation></td></tr><tr><td><equation>f^{\prime}(x)</equation></td><td>-</td><td>0</td><td>+</td><td>不存在</td><td>-</td><td>0</td><td>+</td></tr><tr><td><equation>f(x)</equation></td><td>单调减少</td><td>极小值</td><td>单调增加</td><td>极大值</td><td>单调减少</td><td>极小值</td><td>单调增加</td></tr></table>

---

**2017年第3题 | 选择题 | 4分 | 答案: C**

3. 设函数 f(x)可导，且 f(x)f'(x)>0，则（    ）

A. f(1)>f(-1) B. f(1)<f(-1) C.<equation>|f(1)|>|f(-1)|</equation>D.<equation>|f(1)|<|f(-1)|</equation>

答案: C

**解析:**解（法一）令<equation>F ( x )=f^{2} ( x ).</equation>由题设知，<equation>F^{\prime}(x)=2 f(x) f^{\prime}(x)>0</equation>，故<equation>f^{2}(x)</equation>单调增加，于是<equation>f^{2}(1)>f^{2}(-1)</equation>即<equation>|f(1)|>|f(-1)|</equation>应选C.

（法二）由于<equation>f ( x ) f^{\prime} ( x ) > 0</equation>即恒大于零，故<equation>f ( x )</equation>恒大于零或<equation>f ( x )</equation>恒小于零（否则由<equation>f ( x )</equation>的连续性可知<equation>f ( x )</equation>存在零点，从而<equation>f ( x ) f^{\prime} ( x )</equation>不恒大于零).

若 f(x) > 0，则<equation>f^{\prime}(x) > 0</equation>，故 f(x) 单调增加. 因此 f(1) > f(-1) > 0.

若 f(x) < 0 ，则<equation>f^{\prime}(x) < 0</equation>，故 f(x) 单调减少. 因此 f(1) < f(-1) < 0.

综上所述，<equation>|f(1)| > |f(-1)|</equation>.应选C.

（法三）排除法.

取<equation>f ( x )=\mathrm{e}^{x}</equation>，则<equation>f ( x )</equation>满足<equation>f ( x ) f^{\prime} ( x )=\mathrm{e}^{x}\cdot \mathrm{e}^{x}>0</equation>，且<equation>f (1) > f (- 1) > 0, \quad | f (1) | > | f (- 1) |,</equation>故可以排除选项B、D.

取<equation>f(x)=-\mathrm{e}^{x}</equation>，则 f(x)满足<equation>f(x)f^{\prime}(x)=(-\mathrm{e}^{x})\cdot(-\mathrm{e}^{x})>0</equation>，且<equation>f(1)<f(-1)<0</equation>，故可以排除选项A.

因此，应选C.

---

**2016年第17题 | 解答题 | 10分**

17. (本题满分10分）

设函数<equation>f ( x )=\int_{0}^{1} \left| t^{2}-x^{2} \right| \mathrm{d} t ( x > 0 )</equation>，求<equation>f^{\prime} ( x )</equation>，并求 f(x)的最小值.

**答案:**<equation>f^{\prime}(x) = \left\{ \begin{array}{ll} 4x^{2} - 2x, & 0 < x < 1, \\ 2x, & x \geqslant 1. \end{array} \right.</equation>最小值<equation>f\left(\frac{1}{2}\right) = \frac{1}{4}</equation>.

**解析:**解 对 x的取值范围进行讨论.由<equation>f ( x )=\int_{0}^{1} \mid t^{2}-x^{2} \mid \mathrm{d} t</equation>知，

- 当<equation>x \geqslant 1</equation>时，<equation>x \geqslant t</equation>，<equation>|t^{2} - x^{2}| = x^{2} - t^{2}</equation>.

- 当 0 < x < 1时，有两种情况.<equation>\left| t ^ {2} - x ^ {2} \right| = \left\{ \begin{array}{l l} x ^ {2} - t ^ {2}, & 0 \leqslant t \leqslant x, \\ t ^ {2} - x ^ {2}, & x < t \leqslant 1. \end{array} \right.</equation>于是，当<equation>x\geqslant 1</equation>时，<equation>f (x) = \int_ {0} ^ {1} \left| t ^ {2} - x ^ {2} \right| \mathrm {d} t = \int_ {0} ^ {1} \left(x ^ {2} - t ^ {2}\right) \mathrm {d} t = x ^ {2} - \frac {1}{3}.</equation>当 0 < x < 1时，<equation>\begin{array}{l} f (x) = \int_ {0} ^ {1} \left| t ^ {2} - x ^ {2} \right| \mathrm {d} t = \int_ {0} ^ {x} \left(x ^ {2} - t ^ {2}\right) \mathrm {d} t + \int_ {x} ^ {1} \left(t ^ {2} - x ^ {2}\right) \mathrm {d} t \\ = \left(x ^ {2} t - \frac {t ^ {3}}{3}\right) \Bigg | _ {0} ^ {x} + \left(\frac {t ^ {3}}{3} - x ^ {2} t\right) \Bigg | _ {x} ^ {1} = \frac {4}{3} x ^ {3} - x ^ {2} + \frac {1}{3}. \\ \end{array}</equation>因此，<equation>f ( x ) = \left\{ \begin{array}{l l} \frac{4}{3} x^{3} - x^{2} + \frac{1}{3}, & 0 < x < 1, \\ x^{2} - \frac{1}{3}, & x \geqslant 1. \end{array} \right.</equation>从<equation>f ( x )</equation>的表达式可以看出，<equation>f \left(1 ^ {-}\right) = f \left(1 ^ {+}\right) = f (1) = \frac {2}{3}.</equation>f(x）在 x=1处连续.

由<equation>f ( x )</equation>的表达式可知，当<equation>0 < x < 1</equation>时，<equation>f^{\prime}(x)=4 x^{2}-2 x</equation>；当<equation>x > 1</equation>时，<equation>f^{\prime}(x)=2 x.</equation>当<equation>x=1</equation>时，根据导数的定义分别计算<equation>f ( x )</equation>在<equation>x=1</equation>处的左侧导数和右侧导数.<equation>\begin{aligned} f _ {-} ^ {\prime} (1) &= \lim _ {x \rightarrow 1 ^ {-}} \frac {\frac {4}{3} x ^ {3} - x ^ {2} - \frac {1}{3}}{x - 1} = \lim _ {x \rightarrow 1 ^ {-}} \frac {\frac {4}{3} x ^ {3} - \frac {4}{3} x ^ {2} + \frac {1}{3} x ^ {2} - \frac {1}{3}}{x - 1} \\ &= \lim _ {x \rightarrow 1 ^ {-}} \frac {(x - 1) \left[ \frac {4}{3} x ^ {2} + \frac {1}{3} (x + 1) \right]}{x - 1} = \lim _ {x \rightarrow 1 ^ {-}} \left[ \frac {4}{3} x ^ {2} + \frac {1}{3} (x + 1) \right] = 2, \end{aligned}</equation><equation>f _ {+} ^ {\prime} (1) = \lim _ {x \rightarrow 1 ^ {+}} \frac {x ^ {2} - 1}{x - 1} = \lim _ {x \rightarrow 1 ^ {+}} (x + 1) = 2.</equation>由此可见，<equation>f^{\prime}(1)=f_{-}^{\prime}(1)=f_{+}^{\prime}(1)=2.</equation>因此，<equation>f ^ {\prime} (x) = \left\{ \begin{array}{l l} 4 x ^ {2} - 2 x, & 0 < x < 1, \\ 2 x, & x \geqslant 1. \end{array} \right.</equation>当 x > 1时，<equation>f^{\prime}(x)=2x>0</equation>，故 f(x)在（1，<equation>+\infty</equation>）内单调增加.

当<equation>0 < x < 1</equation>时，<equation>f^{\prime}(x)=4x^{2}-2x</equation>求<equation>f^{\prime}(x)</equation>的零点得，<equation>x=\frac{1}{2}</equation>或<equation>x=0</equation>（舍去）.因此，当<equation>0 < x < \frac{1}{2}</equation>时，<equation>f^{\prime}(x) < 0</equation>；当<equation>\frac{1}{2} < x < 1</equation>时，<equation>f^{\prime}(x) > 0.</equation>由于 f(x) 连续，故可知 f(x) 的最小值在<equation>x=\frac{1}{2}</equation>处取得，即最小值为<equation>f \left(\frac {1}{2}\right) = \frac {4}{3} \times \frac {1}{8} - \frac {1}{4} + \frac {1}{3} = \frac {1}{4}.</equation>

---

**2010年第3题 | 选择题 | 4分 | 答案: B**

3. 设函数 f(x)，g(x)具有二阶导数，且<equation>g^{\prime \prime}(x)<0</equation>. 若 g<equation>( x_{0} )=a</equation>是 g(x)的极值，则 f(g(x))在 x0处取极大值的一个充分条件是（    ）

A.<equation>f^{\prime}(a)<0</equation>B.<equation>f^{\prime}(a)>0</equation>C.<equation>f^{\prime\prime}(a)<0</equation>D.<equation>f^{\prime\prime}(a)>0</equation>

答案: B

**解析:**由于 g(x)在<equation>x_{0}</equation>处取得极值且 g(x)可导，故<equation>g^{\prime}(x_{0})=0.</equation>于是，<equation>[ f (g (x)) ] ^ {\prime} = f ^ {\prime} (g (x)) g ^ {\prime} (x),</equation><equation>[ f (g (x)) ] ^ {\prime \prime} = f ^ {\prime \prime} (g (x)) \left[ g ^ {\prime} (x) \right] ^ {2} + f ^ {\prime} (g (x)) g ^ {\prime \prime} (x).</equation>从而<equation>[f(g(x))]' \mid_{x = x_0} = f'(g(x_0))g'(x_0) = 0, [f(g(x))]'' \mid_{x = x_0} = f'(g(x_0))g''(x_0) = f'(a)g''(x_0).</equation>由于一个二阶可导的函数在某点取得极大值的一个充分条件是该函数在该点处的一阶导数为零，二阶导数小于零，又由于<equation>g^{\prime \prime}(x_{0}) < 0</equation>，故<equation>f(g(x))</equation>在<equation>x_{0}</equation>处取极大值的一个充分条件是<equation>f^{\prime}(a) > 0.</equation>应选B.

从上述过程可以看出，当<equation>f^{\prime}(a) < 0</equation>时，<equation>f(g(x))</equation>在<equation>x_{0}</equation>处取得极小值且<equation>f(g(x))</equation>在<equation>x_{0}</equation>处取得极值与<equation>f^{\prime \prime}(a)</equation>的取值无关，故选项A、C、D都不正确.

---


#### 导数与微分的计算

**2022年第13题 | 填空题 | 5分**

13. 已知函数<equation>f(x)=\mathrm{e}^{\sin x}+\mathrm{e}^{-\sin x}</equation>, 则<equation>f^{\prime\prime\prime}(2\pi)=</equation>___

**解析:**由于<equation>f (- x) = \mathrm {e} ^ {\sin (- x)} + \mathrm {e} ^ {- \sin (- x)} = \mathrm {e} ^ {- \sin x} + \mathrm {e} ^ {\sin x} = f (x),</equation>故 f(x)是偶函数.从而<equation>f^{\prime}(x)</equation>是奇函数，<equation>f^{\prime\prime}(x)</equation>是偶函数，<equation>f^{\prime\prime\prime}(x)</equation>是奇函数.由奇函数的性质可知，<equation>f^{\prime\prime\prime}(0)=0.</equation>又由于<equation>\sin x</equation>是周期为<equation>2\pi</equation>的周期函数，故 f(x)也是周期为<equation>2\pi</equation>的周期函数.从而 f(x)的各阶导函数均是周期为<equation>2\pi</equation>的周期函数.

因此，<equation>f^{\prime \prime \prime}(2\pi)=f^{\prime \prime \prime}(0)=0.</equation>

---

**2021年第11题 | 填空题 | 5分**

**答案:**<equation>\frac {\sin e ^ {- 1}}{2 e}.</equation>

**解析:**根据链式法则，<equation>\frac{\mathrm{d} y}{\mathrm{d} x}=-\sin\mathrm{e}^{-\sqrt{x}}\cdot\mathrm{e}^{-\sqrt{x}}\cdot\left(-\frac{1}{2\sqrt{x}}\right).</equation>代入 x = 1 可得，<equation>\left.\frac{\mathrm{d} y}{\mathrm{d} x}\right|_{x=1}=\frac{1}{2}\cdot\mathrm{e}^{-1}\cdot\sin\mathrm{e}^{-1}=\frac{\sin\mathrm{e}^{-1}}{2\mathrm{e}}.</equation>

---

**2012年第2题 | 选择题 | 4分 | 答案: A**

2. 设函数<equation>f(x)=\mathrm{e}^{x}-1)\mathrm{e}^{2x}-2)\cdots \mathrm{e}^{nx}-n)</equation>，其中 n为正整数，则<equation>f^{\prime}(0)=</equation>(    )

A.<equation>(-1)^{n-1}(n-1)!</equation>B.<equation>(-1)^{n}(n-1)!</equation>C.<equation>(-1)^{n-1}n!</equation>D.<equation>(-1)^{n}n!</equation>

答案: A

**解析:**解（法一）由题设知，<equation>f ( x ) = \left(\mathrm{e}^{x} - 1\right)\left[\left(\mathrm{e}^{2 x} - 2\right)\dots\left(\mathrm{e}^{n x} - n\right)\right]</equation>，再由函数乘积的求导法则知，<equation>f ^ {\prime} (x) = \mathrm {e} ^ {x} \left[ \left(\mathrm {e} ^ {2 x} - 2\right) \dots \left(\mathrm {e} ^ {n x} - n\right) \right] + \left(\mathrm {e} ^ {x} - 1\right) \left[ \left(\mathrm {e} ^ {2 x} - 2\right) \dots \left(\mathrm {e} ^ {n x} - n\right) \right] ^ {\prime},</equation><equation>f ^ {\prime} (0) = (- 1) (- 2) \dots (1 - n) + 0 = (- 1) ^ {n - 1} (n - 1)!</equation>应选A.

（法二）由题设知，<equation>f(0)=0.</equation>根据导数定义有<equation>\begin{array}{l} f ^ {\prime} (0) = \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0} \frac {\left(\mathrm {e} ^ {x} - 1\right)\left(\mathrm {e} ^ {2 x} - 2\right) \cdots \left(\mathrm {e} ^ {n x} - n\right)}{x} \\ \underline {{\mathrm {e} ^ {x} - 1 \sim x}} \lim _ {x \rightarrow 0} \left(\mathrm {e} ^ {2 x} - 2\right) \dots \left(\mathrm {e} ^ {n x} - n\right) = (1 - 2) \dots (1 - n) = (- 1) ^ {n - 1} (n - 1)!. \\ \end{array}</equation>应选A.

（法三）特殊值法.

观察各选项，可知当<equation>n\geqslant 2</equation>时，每个选项的值都不同.取<equation>n = 2</equation>，则<equation>f (x) = \left(\mathrm {e} ^ {x} - 1\right) \left(\mathrm {e} ^ {2 x} - 2\right), f ^ {\prime} (x) = \mathrm {e} ^ {x} \left(\mathrm {e} ^ {2 x} - 2\right) + \left(\mathrm {e} ^ {x} - 1\right) 2 \mathrm {e} ^ {2 x}.</equation>于是<equation>f^{\prime}(0) = -1.</equation>将<equation>n=2</equation>代入各选项，只有选项A的结果等于-1.

因此，应选A.

---

**2012年第10题 | 填空题 | 4分**

10. 设函数<equation>f ( x )=\left\{\begin{array}{ll}\ln \sqrt{x},&x\geqslant 1,\\ 2 x-1,&x<1,\end{array}\right. y=f(f(x))</equation>，则<equation>\left.\frac{\mathrm{d} y}{\mathrm{d} x}\right|_{x=\mathrm{e}}=</equation>___

**解析:**解 由已知条件知<equation>f(\mathrm{e})=\ln \sqrt{\mathrm{e}}=\frac{1}{2}.</equation>由链式法则知，<equation>\begin{array}{l} \left. \frac {\mathrm {d} y}{\mathrm {d} x} \right| _ {x = \mathrm {e}} = f ^ {\prime} (f (x)) \cdot f ^ {\prime} (x) \Big | _ {x = \mathrm {e}} = f ^ {\prime} (f (\mathrm {e})) \cdot f ^ {\prime} (\mathrm {e}) = f ^ {\prime} \left(\frac {1}{2}\right) \cdot f ^ {\prime} (\mathrm {e}) \\ = \frac {\mathrm {d} (2 x - 1)}{\mathrm {d} x} \Big | _ {x = \frac {1}{2}} \cdot \frac {\mathrm {d} (\ln \sqrt {x})}{\mathrm {d} x} \Big | _ {x = \mathrm {e}} = 2 \times \frac {1}{2 \mathrm {e}} = \frac {1}{\mathrm {e}}. \\ \end{array}</equation>

---


#### 方程根的存在性与个数

**2021年第3题 | 选择题 | 5分 | 答案: A**

3. 设函数<equation>f(x)=a x-b \ln x(a>0)</equation>有两个零点，则<equation>\frac{b}{a}</equation>的取值范围是（    ）

A. (e,+<equation>\infty</equation>)

B. (0,e)

C.<equation>\left( 0,\frac{1} {\mathrm{e}} \right)</equation>D.<equation>\left( \frac{1}{\mathrm{e}},+\infty \right)</equation>

答案: A

**解析:**解（法一）<equation>f ( x )</equation>的定义域为（0，<equation>+ \infty</equation>）.计算<equation>f^{\prime}(x)</equation>得<equation>f^{\prime}(x)=a-\frac{b}{x}.</equation>由于 a > 0，故若 b≤0，则<equation>f^{\prime}(x)>0</equation>，f(x)单调增加.此时 f(x)不可能有2个零点.于是，b > 0.

下面分析 f（x）的单调性.

当<equation>x=\frac{b}{a}</equation>时，<equation>f^{\prime}(x)=0</equation>；当<equation>0 < x < \frac{b}{a}</equation>时，<equation>f^{\prime}(x) < 0,f(x)</equation>单调减少；当<equation>x > \frac{b}{a}</equation>时，<equation>f^{\prime}(x) > 0</equation><equation>f(x)</equation>单调增加.于是，<equation>f(x)</equation>在（0，<equation>+\infty</equation>）上先单调减少，再单调增加.<equation>f\left(\frac{b}{a}\right)</equation>为f(x)的最小值.

f(x)有2个零点等价于<equation>f\left(\frac{b}{a}\right)</equation>小于零.否则f(x）恒大于等于零，不可能存在2个零点.<equation>f \left(\frac {b}{a}\right) = a \cdot \frac {b}{a} - b \ln \frac {b}{a} = b - b \ln \frac {b}{a} = b \left(1 - \ln \frac {b}{a}\right) < 0.</equation>又因为<equation>b > 0</equation>，所以<equation>b\left(1-\ln \frac{b}{a}\right)<0</equation>等价于<equation>1-\ln \frac{b}{a}<0</equation>即<equation>\ln \frac{b}{a}>1,\frac{b}{a}>\mathrm{e}.</equation>因此，应选A.

（法二）同法一可知<equation>b > 0.</equation>ax-b<equation>\ln x=0</equation>等价于<equation>\frac{x}{\ln x}=\frac{b}{a}</equation>，故函数 f(x）=ax-b<equation>\ln x</equation>有2个零点等价于曲线 y<equation>=\frac{x}{\ln x}</equation>与直线 y<equation>=\frac{b}{a}</equation>有2个交点.

计算<equation>g ( x )=\frac{x}{\ln x}</equation>的导数<equation>g^{\prime}(x).</equation><equation>g ^ {\prime} (x) = \frac {\ln x - 1}{(\ln x) ^ {2}}.</equation>由于<equation>x=1</equation>是<equation>g(x)</equation>的无穷间断点，故<equation>x=1</equation>是<equation>y=g(x)</equation>的铅直渐近线.当<equation>0 < x < 1</equation>时，<equation>g^{\prime}(x)<0,g(x)</equation>单调减少；当<equation>1 < x < \mathrm{e}</equation>时，<equation>g^{\prime}(x)<0,g(x)</equation>单调减少；当<equation>x > \mathrm{e}</equation>时，<equation>g^{\prime}(x)>0,g(x)</equation>单调增加，且<equation>\lim _ {x \rightarrow + \infty} g (x) = \lim _ {x \rightarrow + \infty} \frac {x}{\ln x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow + \infty} \frac {1}{\frac {1}{x}} = + \infty .</equation><equation>x=\mathrm{e}</equation>是<equation>g(x)</equation>的极小值点，极小值为<equation>g(\mathrm{e})=\mathrm{e}.</equation>y = g(x）的图形如右图所示.

由图可知，曲线<equation>y=\frac{x}{\ln x}</equation>与直线<equation>y=\frac{b}{a}</equation>有2个交点当且仅当<equation>\frac{b}{a}>\mathrm{e}.</equation>因此，应选A.

---

**2019年第2题 | 选择题 | 4分 | 答案: D**

2. 已知方程<equation>x^{5}-5 x+k=0</equation>有3个不同的实根，则 k的取值范围是（    )

A.<equation>(-\infty,-4)</equation>B.<equation>(4,+\infty)</equation>C.<equation>\{-4,4\}</equation>D.<equation>(-4,4)</equation>

答案: D

**解析:**解构造辅助函数<equation>f ( x )=x^{5}-5 x+k</equation>，则<equation>f^{\prime}(x)=5 x^{4}-5=5 \left(x^{4}-1\right).</equation>当 x >1或 x<-1时，<equation>f^{\prime}(x)>0</equation>f(x)单调增加；当<equation>-1<x<1</equation>时，<equation>f^{\prime}(x)<0</equation>f(x)单调减少；当 x=<equation>\pm 1</equation>时，<equation>f^{\prime}(\pm1)=0.</equation>因此， x=-1是 f(x)的极大值点，极大值为 f(-1)， x=1是 f(x)的极小值点，极小值为 f(1).

(a)

(b)

如图（a）所示，要使得 f(x)有3个不同的零点，必须有<equation>f(1)=k-4<0, f(-1)=k+4>0.</equation>解得<equation>-4<k<4.</equation>因此，应选D.

---

**2017年第18题 | 解答题 | 10分**

18. (本题满分10分）已知方程<equation>\frac{1}{\ln(1+x)}-\frac{1}{x}=k</equation>在区间（0，1）内有实根，确定常数 k的取值范围.

**答案:**<equation>\left(\frac {1}{\ln 2} - 1, \frac {1}{2}\right).</equation>

**解析:**解设<equation>f ( x )=\frac{1}{\ln(1+x)}-\frac{1}{x}, x\in(0,1].</equation>考察 f(x)在（0，1]内的单调性.<equation>f ^ {\prime} (x) = \left[ \frac {1}{\ln (1 + x)} - \frac {1}{x} \right] ^ {\prime} = - \frac {1}{(1 + x) \ln^ {2} (1 + x)} + \frac {1}{x ^ {2}} = \frac {(1 + x) \ln^ {2} (1 + x) - x ^ {2}}{(1 + x) x ^ {2} \ln^ {2} (1 + x)}.</equation>由于当 x<equation>\in(0,1)</equation>时，<equation>(1+x)x^{2}\ln^{2}(1+x)>0</equation>，故我们考察 g(x）=（1+x）<equation>\ln^{2}(1+x)-x^{2},</equation><equation>x\in[0,1].</equation><equation>g ^ {\prime} (x) = \ln^ {2} (1 + x) + 2 \ln (1 + x) - 2 x,</equation><equation>g ^ {\prime \prime} (x) = \frac {2 \ln (1 + x)}{1 + x} + \frac {2}{1 + x} - 2 = \frac {2}{1 + x} [ \ln (1 + x) - x ].</equation>当 x<equation>\in(0,1)</equation>时，<equation>\ln(1+x)-x=-\frac{x^{2}}{2}+o(x^{2})<0</equation>.于是当 x<equation>\in(0,1)</equation>时，<equation>g^{\prime\prime}(x)<0</equation>.又因为<equation>g^{\prime}(0)=0</equation>，所以当 x<equation>\in(0,1)</equation>时，<equation>g^{\prime}(x)<0</equation>，g(x)在(0,1)内单调减少.由于<equation>g(0)=0</equation>，故<equation>g(x)<0</equation>，<equation>x\in(0,1)</equation>.因此，当 x<equation>\in(0,1)</equation>时，<equation>f^{\prime}(x)=\frac{g(x)}{(1+x)x^{2}\ln^{2}(1+x)}<0</equation>，f(x)在(0,1)内单调减少.<equation>f ( x )</equation>在（0,1）内的值域为（f（1），<equation>\lim_{x\to 0^{+}}f(x) ).</equation><equation>f (1) = \frac {1}{\ln 2} - 1.</equation>$<equation>\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} \left[\frac{1}{\ln(1+x)} - \frac{1}{x}\right] = \lim_{x \to 0^+} \frac{x - \ln(1+x)}{x\ln(1+x)} = \frac{1}{2}</equation>\left(\frac{1}{\ln2}-1,\frac{1}{2}\right). $

---

**2011年第18题 | 解答题 | 10分**

18. (本题满分10分）

证明方程<equation>4\arctan x-x+\frac{4\pi}{3}-\sqrt{3}=0</equation>恰有两个实根.

**答案:**## （18）证明略.

**解析:**证设 f(x）=4arctan x-x+<equation>\frac{4\pi}{3}-\sqrt{3}</equation>；则<equation>f ^ {\prime} (x) = \frac {4}{1 + x ^ {2}} - 1 = \frac {3 - x ^ {2}}{1 + x ^ {2}}.</equation>当<equation>x\in(-\sqrt{3},\sqrt{3})</equation>时，<equation>f^{\prime}(x) > 0</equation>；当<equation>x\in(-\infty , - \sqrt{3})</equation>或<equation>x\in(\sqrt{3}, + \infty)</equation>时，<equation>f^{\prime}(x) < 0</equation>；当<equation>x = \pm \sqrt{3}</equation>时，<equation>f^{\prime}(x) = 0.</equation>因此，<equation>f ( x )</equation>在<equation>(-\infty,-\sqrt{3})</equation>和<equation>(\sqrt{3},+\infty)</equation>上单调减少，在<equation>(-\sqrt{3},\sqrt{3})</equation>上单调增加，<equation>f(-\sqrt{3})</equation>为<equation>f ( x )</equation>的极小值，<equation>f(\sqrt{3})</equation>为<equation>f ( x )</equation>的极大值.

分别计算<equation>f(-\sqrt{3})</equation>和<equation>f(\sqrt{3})</equation>得，<equation>f (- \sqrt {3}) = 0, f (\sqrt {3}) = \frac {8}{3} \pi - 2 \sqrt {3} > 0.</equation>另一方面，当<equation>x\to+\infty</equation>时，<equation>\lim _ {x \rightarrow + \infty} f (x) = - \infty .</equation>由零点定理和单调性可知，<equation>f ( x )</equation>在<equation>(\sqrt{3}, +\infty)</equation>上有唯一零点，加上<equation>x=-\sqrt{3}, f ( x )</equation>在<equation>(-\infty, +\infty)</equation>上共有两个零点.

f（x）的性质可列表如下.

<table border="1"><tr><td></td><td>(-∞,-√3)</td><td>-√3</td><td>(-√3,√3)</td><td>√3</td><td>(√3,+∞)</td></tr><tr><td>f(x)</td><td>单调减少,无零点，limx→-∞f(x)=+∞</td><td>f(-3)=0</td><td>单调增加，无零点</td><td>f(√3)>0</td><td>单调减少，有唯一零点，limx→+∞f(x)=-∞</td></tr></table>

因此，方程<equation>f ( x ) = 0</equation>恰有两个实根.

---


#### 导数的几何意义

**2020年第10题 | 填空题 | 4分**

10. 曲线<equation>x+y+\mathrm{e}^{2 x y}=0</equation>在点 (0,-1) 处的切线方程为 ___

**解析:**对已知方程两端关于 x求导，可得<equation>1+y^{\prime}+\mathrm{e}^{2 x y}(2 y+2 x y^{\prime})=0.</equation>整理可得<equation>(1+2 x \mathrm{e}^{2 x y}) y^{\prime}=-2 y \mathrm{e}^{2 x y}-1.</equation>代入<equation>x=0,y=-1</equation>，可得<equation>y^{\prime}(0)=2-1=1.</equation>又因为切线过点（0，-1），所以该切线的点斜式方程为<equation>y+1=x-0</equation>即<equation>y=x-1.</equation>

---

**2013年第9题 | 填空题 | 4分**

9. 设曲线<equation>y=f(x)</equation>与<equation>y=x^{2}-x</equation>在点(1,0)处有公共切线，则<equation>\lim_{n\rightarrow \infty} n f\left(\frac{n}{n+2}\right)=</equation>___

**解析:**由已知条件知<equation>f ( 1 )=0</equation>且<equation>f^{\prime}(1)=\frac{\mathrm{d}\left(x^{2}-x\right)}{\mathrm{d}x}\bigg|_{x=1}=1.</equation>因此，<equation>\begin{array}{l} \lim _ {n \rightarrow \infty} n f \left(\frac {n}{n + 2}\right) = \lim _ {n \rightarrow \infty} \frac {f \left(\frac {n}{n + 2}\right) - f (1)}{\frac {1}{n}} = \lim _ {n \rightarrow \infty} \frac {f \left(\frac {n}{n + 2}\right) - f (1)}{\frac {n}{n + 2} - 1} \cdot \frac {\frac {n}{n + 2} - 1}{\frac {1}{n}} \\ \underline {{\mathrm {导 数 定 义}}} f ^ {\prime} (1) \cdot \lim _ {n \rightarrow \infty} \frac {- 2 n}{n + 2} = - 2. \\ \end{array}</equation>

---

**2011年第11题 | 填空题 | 4分**

11. 曲线<equation>\tan \left(x+y+\frac{\pi}{4}\right)=\mathrm{e}^{y}</equation>在点 (0,0) 处的切线方程为 ___

**答案:**## y = - 2x.

**解析:**解（法一）将<equation>y</equation>看作<equation>x</equation>的函数，对<equation>\tan \left(x + y + \frac{\pi}{4}\right) = \mathrm{e}^{y}</equation>两端关于<equation>x</equation>求导得，<equation>\sec^ {2} \left(x + y + \frac {\pi}{4}\right) \cdot \left(1 + \frac {\mathrm {d} y}{\mathrm {d} x}\right) = \mathrm {e} ^ {y} \cdot \frac {\mathrm {d} y}{\mathrm {d} x}.</equation>将<equation>x = 0,y = 0</equation>代入上式得<equation>2\left(1 + \frac{\mathrm{d}y}{\mathrm{d}x}\bigg|_{x = 0}\right) = \frac{\mathrm{d}y}{\mathrm{d}x}\bigg|_{x = 0}.</equation>解得<equation>\frac{\mathrm{d}y}{\mathrm{d}x}\bigg|_{x = 0} = -2.</equation>因此，曲线在点（0,0）处的切线方程为<equation>y=-2x.</equation>（法二）对<equation>\tan \left(x + y + \frac{\pi}{4}\right) = \mathrm{e}^{y}</equation>两端微分得，<equation>\sec^ {2} \left(x + y + \frac {\pi}{4}\right) \cdot \left(\mathrm {d} x + \mathrm {d} y\right) = \mathrm {e} ^ {y} \mathrm {d} y.</equation>将<equation>x=0,y=0</equation>代入上式化简得<equation>2\mathrm{d}x=-\mathrm{d}y</equation>即<equation>\left.\frac{\mathrm{d}y}{\mathrm{d}x}\right|_{x=0}=-2.</equation>其余同法一.

---


#### 不等式

**2012年第18题 | 解答题 | 10分**

18. (本题满分10分)

证明<equation>x\ln \frac{1+x}{1-x}+\cos x\geqslant 1+\frac{x^{2}}{2}(-1<x<1).</equation>

**答案:**## （18）证明略.

**解析:**证（法一）考虑辅助函数<equation>f ( x )=x \ln \frac{1+x}{1-x}+\cos x-1-\frac{x^{2}}{2}.</equation>由于<equation>f (- x) = (- x) \ln \frac {1 - x}{1 + x} + \cos x - 1 - \frac {x ^ {2}}{2} = f (x),</equation>故 f(x)为偶函数.如果能证明当 x<equation>\in[0,1)</equation>时，<equation>f(x)\geqslant0</equation>，那么当 x<equation>\in(-1,1)</equation>时，也有 f(x)<equation>\geqslant0</equation>，从而题给不等式成立.

计算<equation>f^{\prime}(x)</equation><equation>f ^ {\prime} (x) = \left(x \ln \frac {1 + x}{1 - x} + \cos x - 1 - \frac {x ^ {2}}{2}\right) ^ {\prime} = \frac {2 x}{1 - x ^ {2}} + \ln \frac {1 + x}{1 - x} - \sin x - x.</equation>由于当<equation>x\in [0,1)</equation>时，<equation>\frac{x}{1 - x^2}\geqslant x\geqslant \sin x</equation>，故<equation>\frac {2 x}{1 - x ^ {2}} \geqslant 2 x \geqslant \sin x + x,</equation>等号在 x=0时取得.又因为<equation>\frac{1+x}{1-x}\geqslant 1</equation>，所以<equation>\ln \frac{1+x}{1-x}\geqslant 0</equation>，等号在 x=0时取得.

因此，当<equation>x\in(0,1)</equation>时，<equation>f ^ {\prime} (x) = \frac {2 x}{1 - x ^ {2}} + \ln \frac {1 + x}{1 - x} - \sin x - x > 0.</equation>综上所述，<equation>f ( x )</equation>在[0,1]上单调增加，<equation>f ( 0 )</equation>为<equation>f ( x )</equation>在[0,1]上的最小值.又由<equation>f ( x )</equation>为偶函数可知，在（-1，1）上，<equation>f ( x ) \geqslant f ( 0 ) = 0</equation>即<equation>x \ln \frac{1+x}{1-x}+\cos x\geqslant 1+\frac{x^{2}}{2}(-1<x<1).</equation>（法二）在法一中求得<equation>f^{\prime}(x)=\frac{2x}{1-x^{2}}+\ln \frac{1+x}{1-x}-\sin x-x</equation>后，继续求<equation>f^{\prime\prime}(x)</equation>以判断<equation>f^{\prime}(x)</equation>的性质.<equation>f ^ {\prime \prime} (x) = \frac {2 \left(1 + x ^ {2}\right)}{\left(1 - x ^ {2}\right) ^ {2}} + \frac {1}{1 + x} - \frac {- 1}{1 - x} - \cos x - 1 = \frac {4}{\left(1 - x ^ {2}\right) ^ {2}} - \cos x - 1.</equation>由于当<equation>x\in [0,1)</equation>时，<equation>\frac {4}{\left(1 - x ^ {2}\right) ^ {2}} \geqslant 4, \quad 1 + \cos x \leqslant 2,</equation>故<equation>f^{\prime \prime}(x) > 0. f^{\prime}(x)</equation>在[0,1）上单调增加，<equation>f^{\prime}(x)\geqslant f^{\prime}(0)=0,f(x)</equation>在[0,1）上单调增加.

（法三）首先，<equation>f(x)=x\ln \frac{1+x}{1-x}+\cos x</equation>为偶函数，<equation>g(x)=1+\frac{x^{2}}{2}</equation>也为偶函数，且<equation>f(0)=g(0)=1</equation>故我们只需证明，在（0，1）上，<equation>f(x)\geqslant g(x)</equation>，便能得到在（-1，1）上，<equation>f(x)\geqslant g(x).</equation>由泰勒中值定理，<equation>\cos x=1-\frac{x^{2}}{2!}+\frac{\cos \xi}{4!} x^{4},\xi</equation>为介于0和x之间的某个值.于是，当<equation>x\in(0,1)</equation>时，<equation>\cos x\geqslant 1-\frac{x^{2}}{2}.</equation>从而<equation>f (x) = x \ln \frac {1 + x}{1 - x} + \cos x \geqslant x \ln \frac {1 + x}{1 - x} + 1 - \frac {x ^ {2}}{2}.</equation>若能证明<equation>x\ln \frac{1+x}{1-x}+1-\frac{x^{2}}{2}\geqslant 1+\frac{x^{2}}{2}</equation>，则由不等号的传递性可知原不等式得证.

由于当<equation>x\in (0,1)</equation>时，<equation>x \ln \frac {1 + x}{1 - x} + 1 - \frac {x ^ {2}}{2} \geqslant 1 + \frac {x ^ {2}}{2} \Leftrightarrow x \ln \frac {1 + x}{1 - x} \geqslant x ^ {2} \Leftrightarrow \ln \frac {1 + x}{1 - x} \geqslant x,</equation>故我们只需要证明<equation>\ln \frac{1+x}{1-x}\geqslant x.</equation>考虑<equation>\varphi(x)=\ln \frac{1+x}{1-x}-x.</equation><equation>\varphi^ {\prime} (x) = \frac {1}{1 + x} - \frac {- 1}{1 - x} - 1 = \frac {2}{1 - x ^ {2}} - 1.</equation>当<equation>x \in(0,1)</equation>时，<equation>\frac{2}{1-x^{2}}\geqslant 2</equation>从而<equation>\varphi^{\prime}(x)=\frac{2}{1-x^{2}}-1>0, \varphi(x)</equation>在（0,1）上单调增加，<equation>\varphi(x)\geqslant \varphi(0)=0.</equation>综上所述，原不等式成立.

---

**2010年第4题 | 选择题 | 4分 | 答案: C**

4. 设<equation>f(x)=\ln^{1 0} x,g(x)=x,h(x)=\mathrm{e}^{\frac{x}{1 0}}</equation>，则当 x充分大时有（    )

A. g(x) < h(x) < f(x) B. h(x) < g(x) < f(x) C. f(x) < g(x) < h(x) D. g(x) < f(x) < h(x)

答案: C

**解析:**（法一）由于<equation>\lim _ {x \rightarrow + \infty} \frac {h (x)}{g (x)} = \lim _ {x \rightarrow + \infty} \frac {\mathrm {e} ^ {\frac {x}{1 0}}}{x} \xlongequal {\text {洛 必达}} \lim _ {x \rightarrow + \infty} \frac {\frac {1}{1 0} \mathrm {e} ^ {\frac {x}{1 0}}}{1} = + \infty ,</equation>故当 x充分大时，<equation>h ( x ) > g ( x ).</equation>又由于<equation>\lim _ {x \rightarrow + \infty} \frac {g (x)}{f (x)} = \lim _ {x \rightarrow + \infty} \frac {x}{\ln^ {1 0} x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow + \infty} \frac {x}{1 0 \ln^ {9} x} \xlongequal {\text {洛必达}} \dots \xlongequal {\text {洛必达}} \lim _ {x \rightarrow + \infty} \frac {x}{1 0 !} = + \infty ,</equation>故当<equation>x</equation>充分大时，<equation>g(x) > f(x)</equation>综上所述，当<equation>x</equation>充分大时，<equation>h(x) > g(x) > f(x)</equation>.应选C.

（法二）令<equation>H ( x )=h ( x )-g ( x )=\mathrm{e}^{\frac{x}{1 0}}-x</equation>，则<equation>H^{\prime}(x)=\frac{1}{1 0}\mathrm{e}^{\frac{x}{1 0}}-1.</equation>由于当<equation>x\geqslant 1 0 0</equation>时，<equation>\frac{1}{1 0}\mathrm{e}^{\frac{x}{1 0}}-1\geqslant</equation><equation>\frac{1}{1 0}\mathrm{e}^{1 0}-1>0</equation>，故H(x）在<equation>[ 1 0 0,+\infty)</equation>上为单调增加函数，从而当<equation>x\geqslant 1 0 0</equation>时，<equation>h (x) - g (x) \geqslant h (1 0 0) - g (1 0 0) = \mathrm {e} ^ {1 0} - 1 0 0 \geqslant 2 ^ {1 0} - 1 0 0 > 0.</equation>令<equation>F(x) = x^{\frac{1}{10}} - \ln x</equation>，则<equation>F^{\prime}(x) = \frac{1}{10} x^{-\frac{9}{10}} - \frac{1}{x} = \frac{1}{10x}\left(x^{\frac{1}{10}} - 10\right)</equation>.由于当<equation>x > 10^{10}</equation>时，<equation>F^{\prime}(x) > 0</equation>，故<equation>F(x)</equation>在<equation>[10^{10}, + \infty)</equation>上为单调增加函数，从而当<equation>x > 10^{100}</equation>时，<equation>F(x) \geqslant F(10^{100}) = 10^{10} - 100\ln 10 > 0</equation>即<equation>x^{\frac{1}{10}} > \ln x.</equation>因此，<equation>x > \ln^{10}x.</equation>综上所述，当 x充分大时，<equation>h ( x ) > g ( x ) > f ( x )</equation>.应选C.

---


### 无穷级数


#### 数项级数

**2025年第3题 | 选择题 | 5分 | 答案: B**

3. 已知 k为常数，则级数<equation>\sum_{n=1}^{\infty}(-1)^{n}\left[\frac{1}{n}-\ln \left(1+\frac{k}{n^{2}}\right)\right]</equation>(    )

A. 绝对收敛 B. 条件收敛

C. 发散 D. 敛散性与 k的取

答案: B

**解析:**解 由于数列<equation>\left\{\frac{1}{n}\right\}</equation>单调减少趋于0，故由交错级数的莱布尼茨定理可知<equation>\sum_{n=1}^{\infty}(-1)^{n}\frac{1}{n}</equation>收敛.但<equation>\sum_{n=1}^{\infty}\frac{1}{n}</equation>发散，于是级数<equation>\sum_{n=1}^{\infty}(-1)^{n}\frac{1}{n}</equation>条件收敛.

由于<equation>\left|\ln \left(1+\frac{k}{n^{2}}\right)\right|= \left|\frac{k}{n^{2}}+o\left(\frac{k}{n^{2}}\right)\right|</equation>，故当 n→<equation>\infty</equation>时，<equation>\left|\ln \left(1+\frac{k}{n^{2}}\right)\right| \sim \left|\frac{k}{n^{2}}\right|</equation>，而<equation>\lim_{n\to \infty}n^{2}\left|\frac{k}{n^{2}}\right|=|k|</equation>，从而由正项级数的极限审敛法可知<equation>\sum_{n=1}^{\infty}\left|\frac{k}{n^{2}}\right|</equation>收敛，进一步可得<equation>\sum_{n=1}^{\infty}\left|\ln \left(1+\frac{k}{n^{2}}\right)\right|</equation>收敛.于是级数<equation>\sum_{n=1}^{\infty}(-1)^{n}\ln \left(1+\frac{k}{n^{2}}\right)</equation>绝对收敛.

由级数<equation>\sum_{n=1}^{\infty}(-1)^{n}\frac{1}{n}</equation>条件收敛，级数<equation>\sum_{n=1}^{\infty}(-1)^{n}\ln \left(1+\frac{k}{n^{2}}\right)</equation>绝对收敛以及分析中的结论可得级数<equation>\sum_{n=1}^{\infty}(-1)^{n}\left[\frac{1}{n}-\ln \left(1+\frac{k}{n^{2}}\right)\right]</equation>条件收敛.

因此，应选B.

---

**2023年第4题 | 选择题 | 5分 | 答案: A**

4. 已知<equation>a_{n} < b_{n} ( n=1,2,\cdots)</equation>，若级数<equation>\sum_{n=1}^{\infty} a_{n}</equation>与<equation>\sum_{n=1}^{\infty} b_{n}</equation>均收敛，则“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的（    ）

A. 充分必要条件 B. 充分不必要条件

C. 必要不充分条件 D. 既不充分也不必要条件

答案: A

**解析:**解（法一）由<equation>a_{n} < b_{n}</equation>可知，<equation>\sum_{n=1}^{\infty} \left(b_{n}-a_{n}\right)</equation>为正项级数. 进一步，由<equation>\sum_{n=1}^{\infty} a_{n}</equation>与<equation>\sum_{n=1}^{\infty} b_{n}</equation>均收敛以及收敛级数的性质可知，<equation>\sum_ {n = 1} ^ {\infty} \left(b _ {n} - a _ {n}\right) = \sum_ {n = 1} ^ {\infty} b _ {n} - \sum_ {n = 1} ^ {\infty} a _ {n}.</equation>于是，<equation>\sum_{n=1}^{\infty} \left(b_{n}-a_{n}\right)</equation>为收敛的正项级数，从而<equation>\sum_{n=1}^{\infty} \left(b_{n}-a_{n}\right)</equation>绝对收敛.

由三角不等式可得<equation>\left| b _ {n} \right| = \left| b _ {n} - a _ {n} + a _ {n} \right| \leqslant \left| b _ {n} - a _ {n} \right| + \left| a _ {n} \right|,</equation><equation>\left| a _ {n} \right| = \left| a _ {n} - b _ {n} + b _ {n} \right| \leqslant \left| b _ {n} - a _ {n} \right| + \left| b _ {n} \right|.</equation>若<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛，即<equation>\sum_{n=1}^{\infty} \mid a_{n} \mid</equation>收敛，则由（1）式以及正项级数的比较审敛法可知<equation>\sum_{n=1}^{\infty} \mid b_{n} \mid</equation>收敛，从而<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛.“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的充分条件.

若<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛，即<equation>\sum_{n=1}^{\infty} \mid b_{n} \mid</equation>收敛，则由（2）式以及正项级数的比较审敛法可知<equation>\sum_{n=1}^{\infty} \mid a_{n} \mid</equation>收敛，从而<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛.“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的必要条件.

综上所述，“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的充分必要条件，应选A.

（法二）先考虑充分性.

设<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛，即<equation>\sum_{n=1}^{\infty} \mid a_{n}\mid</equation>收敛.

考虑正项级数<equation>\sum_{n=1}^{\infty} \frac{\mid b_{n}\mid -b_{n}}{2}.</equation>对<equation>\left\{b_{n}\right\}</equation>中小于0的项，<equation>a_{n} < b_{n} < 0</equation>，于是<equation>\left| a _ {n} \right| = - a _ {n} > - b _ {n} = \frac {\left| b _ {n} \right| - b _ {n}}{2} > 0.</equation>对<equation>\left\{b_{n}\right\}</equation>中大于等于0的项，<equation>\left| a _ {n} \right| \geqslant 0 = \frac {\left| b _ {n} \right| - b _ {n}}{2}.</equation>从而，对所有正整数 n，都有<equation>|a_{n}| \geqslant \frac{|b_{n}| - b_{n}}{2} \geqslant 0.</equation>由正项级数的比较审敛法可知，级数<equation>\sum_{n=1}^{\infty} \frac{\mid b_{n}\mid -b_{n}}{2}</equation>收敛. 进一步，<equation>\sum_ {n = 1} ^ {\infty} \left| b _ {n} \right| = \sum_ {n = 1} ^ {\infty} \left[ 2 \left(\frac {\left| b _ {n} \right| - b _ {n}}{2}\right) + b _ {n} \right] = 2 \sum_ {n = 1} ^ {\infty} \frac {\left| b _ {n} \right| - b _ {n}}{2} + \sum_ {n = 1} ^ {\infty} b _ {n}.</equation>由<equation>\sum_{n=1}^{\infty}b_{n}</equation>收敛以及收敛级数的性质可知，<equation>\sum_{n=1}^{\infty}|\boldsymbol{b}_{n}|</equation>收敛，从而<equation>\sum_{n=1}^{\infty}b_{n}</equation>绝对收敛.

因此，“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的充分条件.

再考虑必要性.

由<equation>a_{n} < b_{n}</equation>可得<equation>- b_{n} < - a_{n}.</equation>由<equation>\sum_{n=1}^{\infty} a_{n}</equation>与<equation>\sum_{n=1}^{\infty} b_{n}</equation>均收敛可知<equation>\sum_{n=1}^{\infty}(-a_{n})</equation>与<equation>\sum_{n=1}^{\infty}(-b_{n})</equation>均收敛.于是，同充分性的证明可知<equation>\sum_{n=1}^{\infty}(-b_{n})</equation>绝对收敛蕴含<equation>\sum_{n=1}^{\infty}(-a_{n})</equation>绝对收敛，即<equation>\sum_{n=1}^{\infty}b_{n}</equation>绝对收敛蕴含<equation>\sum_{n=1}^{\infty}a_{n}</equation>绝对收敛.

因此，“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的必要条件.

综上所述，“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的充分必要条件，应选A.

---

**2019年第4题 | 选择题 | 4分 | 答案: B**

4. 若<equation>\sum_{n=1}^{\infty} n u_{n}</equation>绝对收敛，<equation>\sum_{n=1}^{\infty} \frac{v_{n}}{n}</equation>条件收敛，则（    ）

A.<equation>\sum_{n=1}^{\infty} u_{n} v_{n}</equation>条件收敛 B.<equation>\sum_{n=1}^{\infty} u_{n} v_{n}</equation>绝对收敛 C.<equation>\sum_{n=1}^{\infty} \left(u_{n}+v_{n}\right)</equation>收敛 D.<equation>\sum_{n=1}^{\infty} \left(u_{n}+v_{n}\right)</equation>发散

答案: B

**解析:**解（法一）由<equation>\sum_{n=1}^{\infty}\frac{v_{n}}{n}</equation>条件收敛以及级数收敛的必要条件可得，<equation>\lim_{n\to \infty}\frac{v_{n}}{n}=0.</equation>由极限的有界性可知，存在 M > 0和正整数N，使得当 n > N时，<equation>\left|\frac{v_{n}}{n}\right|\leqslant M.</equation>于是，<equation>\left| u _ {n} v _ {n} \right| = \left| n u _ {n} \cdot \frac {v _ {n}}{n} \right| \leqslant M \left| n u _ {n} \right|.</equation>由于<equation>\sum_{n=1}^{\infty} n u_{n}</equation>绝对收敛，故其收敛，从而由比较审敛法可知，<equation>\sum_{n=1}^{\infty} \mid u_{n} v_{n} \mid</equation>收敛因此，<equation>\sum_{n=1}^{\infty} u_{n} v_{n}</equation>绝对收敛.应选B.

（法二）排除法.

选项A、C：取<equation>u_{n}=\frac{1}{n^{3}}, v_{n}=(-1)^{n}</equation>，则<equation>\sum_{n=1}^{\infty}u_{n}v_{n}=\sum_{n=1}^{\infty}\frac{(-1)^{n}}{n^{3}},\sum_{n=1}^{\infty}\left(u_{n}+v_{n}\right)=\sum_{n=1}^{\infty}\left[\frac{1}{n^{3}}+(-1)^{n}\right]</equation><equation>\sum_{n=1}^{\infty}\frac{(-1)^{n}}{n^{3}}</equation>绝对收敛，<equation>\sum_{n=1}^{\infty}\left[\frac{1}{n^{3}}+(-1)^{n}\right]</equation>发散. 选项A、C不正确.

选项D：取<equation>u_{n}=\frac{1}{n^{3}},</equation><equation>v_{n}=\frac{(-1)^{n+1}}{\ln(n+1)},</equation>则<equation>\sum_{n=1}^{\infty}\frac{1}{n^{3}}</equation>收敛，且由莱布尼茨定理可知<equation>\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{\ln(n+1)}</equation>收敛.由收敛级数的性质可知<equation>\sum_{n=1}^{\infty}\left[\frac{1}{n^{3}}+\frac{(-1)^{n+1}}{\ln(n+1)}\right]</equation>收敛.选项D不正确由排除法可知，应选B.

---

**2017年第4题 | 选择题 | 4分 | 答案: C**

4. 若级数<equation>\sum_{n=2}^{\infty}\left[\sin \frac{1}{n}-k\ln \left(1-\frac{1}{n}\right)\right]</equation>收敛，则 k=（    ）

A.1 B.2 C.-1 D.-2

答案: C

**解析:**解 考虑<equation>\sin \frac{1}{n}</equation>和<equation>\ln \left( 1-\frac{1}{n} \right)</equation>的泰勒公式.<equation>\sin \frac {1}{n} = \frac {1}{n} - \frac {1}{6 n ^ {3}} + o \left(\frac {1}{n ^ {3}}\right), \quad \ln \left(1 - \frac {1}{n}\right) = - \frac {1}{n} - \frac {1}{2 n ^ {2}} + o \left(\frac {1}{n ^ {2}}\right).</equation>于是，<equation>\sin \frac {1}{n} - k \ln \left(1 - \frac {1}{n}\right) = \frac {1}{n} + \frac {k}{n} + \frac {k}{2 n ^ {2}} + o \left(\frac {1}{n ^ {2}}\right).</equation>当 n充分大时，<equation>\sin \frac{1}{n}-k\ln \left(1-\frac{1}{n}\right)=\frac{1}{n}+\frac{k}{n}+\frac{k}{2n^{2}}+o\left(\frac{1}{n^{2}}\right)</equation>不变号.又因为舍去级数的有限项不影响级数的敛散性，所以可以对级数<equation>\sum_{n=2}^{\infty}\left[\sin \frac{1}{n}-k\ln \left(1-\frac{1}{n}\right)\right]</equation>使用极限形式的比较审敛法.当 k≠-1时，<equation>\lim _ {n \rightarrow \infty} \frac {\sin \frac {1}{n} - k \ln \left(1 - \frac {1}{n}\right)}{\frac {1}{n}} = \lim _ {n \rightarrow \infty} \frac {\frac {1}{n} + \frac {k}{n} + \frac {k}{2 n ^ {2}} + o \left(\frac {1}{n ^ {2}}\right)}{\frac {1}{n}} = 1 + k,</equation>而<equation>\sum_{n=1}^{\infty}\frac{1}{n}</equation>发散，故由极限形式的比较审敛法知，原级数发散.

当 k=-1时，<equation>\sum_{n=2}^{\infty}-\left[\sin \frac{1}{n}-k\ln \left(1-\frac{1}{n}\right)\right]</equation>为正项级数，且<equation>\lim _ {n \rightarrow \infty} \frac {- \left[ \sin \frac {1}{n} + \ln \left(1 - \frac {1}{n}\right)\right]}{\frac {1}{n ^ {2}}} = \lim _ {n \rightarrow \infty} \frac {\frac {1}{2 n ^ {2}} + o \left(\frac {1}{n ^ {2}}\right)}{\frac {1}{n ^ {2}}} = \frac {1}{2},</equation>而<equation>\sum_{n=1}^{\infty}\frac{1}{n^{2}}</equation>收敛，故由极限形式的比较审敛法知，原级数收敛.

级数<equation>\sum_{n=2}^{\infty}\left[\sin \frac{1}{n}-k\ln \left(1-\frac{1}{n}\right)\right]</equation>收敛等价于 k=-1.

因此，应选C.

---

**2016年第4题 | 选择题 | 4分 | 答案: A**

4. 级数<equation>\sum_{n=1}^{\infty}\left(\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}}\right)\sin(n+k)(k</equation>为常数)（    ）

A. 绝对收敛 B. 条件收敛 C. 发散 D. 收敛性与 k有关

答案: A

**解析:**解 （法一）首先，这并不是一个正项级数，但当 n<equation>\to\infty</equation>时，它的一般项<equation>\begin{array}{l} \left(\frac {1}{\sqrt {n}} - \frac {1}{\sqrt {n + 1}}\right) \sin (n + k) = \frac {\sqrt {n + 1} - \sqrt {n}}{\sqrt {n} \sqrt {n + 1}} \sin (n + k) \\ \xlongequal {\text {分子 有 理 化}} \frac {\sin (n + k)}{\sqrt {n} \sqrt {n + 1} (\sqrt {n + 1} + \sqrt {n})} \rightarrow 0, \\ \end{array}</equation>并且<equation>\left| \left(\frac {1}{\sqrt {n}} - \frac {1}{\sqrt {n + 1}}\right) \sin (n + k) \right| \leqslant \frac {1}{\sqrt {n} \sqrt {n + 1} \left(\sqrt {n + 1} + \sqrt {n}\right)} \leqslant \frac {1}{n \cdot 2 \sqrt {n}} < \frac {1}{n ^ {\frac {3}{2}}},</equation>而<equation>\sum_{n=1}^{\infty}\frac{1}{n^{\frac{3}{2}}}</equation>收敛，故由比较审敛法可知，<equation>\sum_{n=1}^{\infty}\left| \left( \frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}} \right)\sin(n+k) \right|</equation>收敛，从而原级数绝对收敛应选A.

（法二）注意到<equation>\left| \left(\frac {1}{\sqrt {n}} - \frac {1}{\sqrt {n + 1}}\right) \sin (n + k) \right| \leqslant \frac {1}{\sqrt {n}} - \frac {1}{\sqrt {n + 1}}.</equation>由于<equation>\sum_ {n = 1} ^ {m} \left(\frac {1}{\sqrt {n}} - \frac {1}{\sqrt {n + 1}}\right) = \left(1 - \frac {1}{\sqrt {2}}\right) + \left(\frac {1}{\sqrt {2}} - \frac {1}{\sqrt {3}}\right) + \dots + \left(\frac {1}{\sqrt {m}} - \frac {1}{\sqrt {m + 1}}\right) = 1 - \frac {1}{\sqrt {m + 1}},</equation>故<equation>\sum_{n=1}^{\infty}\left(\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}}\right)=\lim_{m\to \infty}\left(1-\frac{1}{\sqrt{m+1}}\right)=1</equation>，即级数<equation>\sum_{n=1}^{\infty}\left(\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}}\right)</equation>收敛.

由比较审敛法知，级数<equation>\sum_{n=1}^{\infty}\left| \left(\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}}\right)\sin(n+k)\right|</equation>收敛，即级数<equation>\sum_{n=1}^{\infty}\left(\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}}\right)\sin(n+k)</equation>绝对收敛.应选A.

---

**2015年第4题 | 选择题 | 4分 | 答案: C**

4. 下列级数中发散的是（    ）<equation>\sum_ {n = 1} ^ {\infty} \frac {n}{3 ^ {n}}</equation><equation>\sum_ {n = 1} ^ {\infty} \frac {1}{\sqrt {n}} \ln \left(1 + \frac {1}{n}\right)</equation>C.<equation>\sum_{n=2}^{\infty} \frac{(-1)^{n}+1}{\ln n}</equation>D.<equation>\sum_{n=1}^{\infty} \frac{n!}{n^{n}}</equation>

答案: C

**解析:**解 由于当 n为奇数时，<equation>(-1)^{n}+1=0;</equation>n为偶数时，<equation>(-1)^{n}+1=2</equation>，故<equation>\sum_ {n = 2} ^ {2 N} \frac {(- 1) ^ {n} + 1}{\ln n} = \sum_ {k = 1} ^ {N} \frac {2}{\ln 2 k} = \sum_ {k = 1} ^ {N} \frac {2}{\ln 2 + \ln k} \geqslant \frac {2}{\ln 2} + \sum_ {k = 2} ^ {N} \frac {2}{2 \ln k} > \sum_ {k = 2} ^ {N} \frac {1}{\ln k} > \sum_ {k = 2} ^ {N} \frac {1}{k}.</equation>而<equation>\sum_{k=2}^{\infty} \frac{1}{k}</equation>发散.由比较审敛法可知，<equation>\sum_{n=2}^{\infty} \frac{(-1)^{n}+1}{\ln n}</equation>发散.应选C.

也可以这样说明<equation>\sum_{n=2}^{\infty} \frac{(-1)^{n}+1}{\ln n}</equation>发散.

由莱布尼茨定理可知<equation>\sum_{n = 2}^{\infty}\frac{(-1)^n}{\ln n}</equation>收敛，由比较审敛法可知<equation>\sum_{n = 2}^{\infty}\frac{1}{\ln n}</equation>发散.因此，<equation>\sum_{n = 2}^{\infty}\frac{(-1)^n + 1}{\ln n}</equation>发散.

下面我们说明选项 A、B、D不正确.

由于<equation>\lim _ {n \rightarrow \infty} \frac {n + 1}{3 ^ {n + 1}} \cdot \frac {3 ^ {n}}{n} = \lim _ {n \rightarrow \infty} \frac {n + 1}{n} \cdot \frac {1}{3} = \frac {1}{3} < 1,</equation><equation>\lim _ {n \rightarrow \infty} \frac {(n + 1) !}{(n + 1) ^ {n + 1}} \cdot \frac {n ^ {n}}{n !} = \lim _ {n \rightarrow \infty} \left(\frac {n}{n + 1}\right) ^ {n} = \lim _ {n \rightarrow \infty} \frac {1}{\left(1 + \frac {1}{n}\right) ^ {n}} = \frac {1}{\mathrm {e}} < 1,</equation>故由比值审敛法可知，选项A与选项D中的级数均收敛.

由于<equation>\lim _ {n \rightarrow \infty} \frac {\frac {1}{\sqrt {n}} \ln \left(1 + \frac {1}{n}\right)}{n ^ {- \frac {3}{2}}} \xlongequal {\ln \left(1 + \frac {1}{n}\right) \sim \frac {1}{n}} \lim _ {n \rightarrow \infty} \frac {\frac {1}{\sqrt {n}} \cdot \frac {1}{n}}{n ^ {- \frac {3}{2}}} = 1,</equation>而<equation>\sum_{n=1}^{\infty}\frac{1}{n^{\frac{3}{2}}}</equation>收敛，故由比较审敛法的极限形式可知，选项B中的级数收敛.

---

**2013年第4题 | 选择题 | 4分 | 答案: D**

4. 设<equation>\{a_{n}\}</equation>为正项数列，下列选项正确的是（    )

A. 若<equation>a_{n}>a_{n+1}</equation>，则<equation>\sum_{n=1}^{\infty}(-1)^{n-1}a_{n}</equation>收敛

B. 若<equation>\sum_{n=1}^{\infty}(-1)^{n-1}a_{n}</equation>收敛，则<equation>a_{n}>a_{n+1}</equation>C. 若<equation>\sum_{n=1}^{\infty}a_{n}</equation>收敛，则存在常数 p>1，使<equation>\lim_{n\rightarrow \infty}n^{p}a_{n}</equation>存在

D. 若存在常数 p>1，使<equation>\lim_{n\rightarrow \infty}n^{p}a_{n}</equation>存在，则<equation>\sum_{n=1}^{\infty}a_{n}</equation>收敛

答案: D

**解析:**解 观察四个选项，发现选项D即极限审敛法的内容，故选项D正确.应选D.

下面我们分别说明选项 A、B、C 不正确.

选项A：虽然<equation>\sum_{n=1}^{\infty}(-1)^{n-1}a_{n}</equation>是交错级数，但是与莱布尼茨定理的条件相比较，该级数不满足<equation>\lim_{n\to \infty}a_{n}=0</equation>的条件.因此不能使用莱布尼茨定理说明它收敛.事实上，取<equation>a_{n}=\frac{1}{n}+1</equation><equation>a_{n}>a_{n+1}</equation>，但由于<equation>\lim_{n\to \infty}(-1)^{n-1}\left(\frac{1}{n}+1\right)</equation>不存在，<equation>\sum_{n=1}^{\infty}(-1)^{n-1}a_{n}</equation>不收敛.

选项B：由于级数舍去有限项不影响其敛散性，故我们可以令<equation>a_{n}=\left\{ \begin{array}{ll}1, & n=1,2,3,\\ \frac{1}{n}, & n=4,5,\dots. \end{array} \right.</equation>级数<equation>\sum_{n=1}^{\infty}(-1)^{n-1}a_{n}</equation>收敛，但<equation>a_{1}=a_{2}=a_{3}</equation>，不满足<equation>a_{n}>a_{n+1}</equation>.

选项C：令<equation>a_{n}=\frac{1}{(n+1)\ln^{2}(n+1)}</equation>，对任意的 p > 1，都有<equation>\lim_{n\to \infty}n^{p}\frac{1}{(n+1)\ln^{2}(n+1)}=\infty.</equation>令<equation>f(x)=\frac{1}{(x+1)\ln^{2}(x+1)}.</equation><equation>\int_{1}^{+\infty}f(x)\mathrm{d}x=\int_{1}^{+\infty}\frac{1}{\ln^{2}(x+1)}\mathrm{d}\left[\ln(x+1)\right]=-\frac{1}{\ln(x+1)}\bigg|_{1}^{+\infty}=\frac{1}{\ln 2}.</equation>由积分判别法可知级数<equation>\sum_{n=1}^{\infty}a_{n}</equation>收敛.

---

**2012年第4题 | 选择题 | 4分 | 答案: D**

4. 已知级数<equation>\sum_{n=1}^{\infty}(-1)^{n}\sqrt{n}\sin \frac{1}{n^{\alpha}}</equation>绝对收敛，级数<equation>\sum_{n=1}^{\infty}\frac{(-1)^{n}}{n^{2-\alpha}}</equation>条件收敛，则（    )

A.<equation>0<\alpha \leqslant \frac{1}{2}</equation>B.<equation>\frac{1}{2}<\alpha \leqslant 1</equation>C.<equation>1<\alpha \leqslant \frac{3}{2}</equation>D.<equation>\frac{3}{2}<\alpha <2</equation>

答案: D

**解析:**解 首先，<equation>\alpha >0</equation>，否则<equation>\lim_{n\rightarrow \infty}\sin \frac{1}{n^{\alpha}}\neq 0</equation><equation>\sum_{n=1}^{\infty}(-1)^{n}\sqrt{n}\sin \frac{1}{n^{\alpha}}</equation>不绝对收敛.于是，<equation>0 < \frac{1}{n^{\alpha}}\leqslant 1</equation><equation>\sin \frac{1}{n^{\alpha}}\geqslant 0.</equation>由于<equation>\sum_{n=1}^{\infty}(-1)^{n}\sqrt{n}\sin \frac{1}{n^{\alpha}}</equation>绝对收敛，故<equation>\sum_{n=1}^{\infty}\sqrt{n}\sin \frac{1}{n^{\alpha}}</equation>收敛.

由于<equation>\lim _ {n \rightarrow \infty} \frac {\sqrt {n} \sin \frac {1}{n ^ {\alpha}}}{n ^ {\frac {1}{2} - \alpha}} \xlongequal {\sin \frac {1}{n ^ {\alpha}} \sim \frac {1}{n ^ {\alpha}}} \lim _ {n \rightarrow \infty} \frac {n ^ {\frac {1}{2} - \alpha}}{n ^ {\frac {1}{2} - \alpha}} = 1,</equation>故<equation>\sum_{n=1}^{\infty}\sqrt{n}\sin \frac{1}{n^{\alpha}}</equation>与<equation>\sum_{n=1}^{\infty}n^{\frac{1}{2}-\alpha}</equation>同敛散.

由于<equation>n^{\frac{1}{2} -\alpha} = \frac{1}{n^{\alpha -\frac{1}{2}}}</equation>，故当<equation>\alpha -\frac{1}{2} >1</equation>，即<equation>\alpha >\frac{3}{2}</equation>时，<equation>\sum_{n = 1}^{\infty}n^{\frac{1}{2} -\alpha}</equation>收敛.

由于级数<equation>\sum_{n=1}^{\infty} \frac{(-1)^{n}}{n^{2-\alpha}}</equation>条件收敛，故<equation>\sum_{n=1}^{\infty} \frac{1}{n^{2-\alpha}}</equation>发散，于是<equation>2-\alpha\leqslant1</equation>又因为级数<equation>\sum_{n=1}^{\infty} \frac{(-1)^{n}}{n^{2-\alpha}}</equation>收敛，所以<equation>\lim_{n\to\infty}\frac{(-1)^{n}}{n^{2-\alpha}}=0</equation>，从而<equation>2-\alpha>0</equation>因此，<equation>1\leqslant\alpha<2.</equation>取<equation>\left(\frac{3}{2},+\infty\right)</equation>与[1,2）的交集，得<equation>\frac{3}{2} < \alpha < 2</equation>应选D.

---

**2011年第3题 | 选择题 | 4分 | 答案: A**

3. 设<equation>\{u_{n}\}</equation>是数列，则下列命题正确的是（    ）

A. 若<equation>\sum_{n=1}^{\infty} u_{n}</equation>收敛，则<equation>\sum_{n=1}^{\infty} \left(u_{2n-1}+u_{2n}\right)</equation>收敛

C. 若<equation>\sum_{n=1}^{\infty} u_{n}</equation>收敛，则<equation>\sum_{n=1}^{\infty} \left(u_{2n-1}-u_{2n}\right)</equation>收敛

B. 若<equation>\sum_{n=1}^{\infty} \left(u_{2n-1}+u_{2n}\right)</equation>收敛，则<equation>\sum_{n=1}^{\infty} u_{n}</equation>收敛

D. 若<equation>\sum_{n=1}^{\infty} \left(u_{2n-1}-u_{2n}\right)</equation>收敛，则<equation>\sum_{n=1}^{\infty} u_{n}</equation>收敛

答案: A

**解析:**解 依次讨论各选项.

对选项A，级数<equation>\sum_{n=1}^{\infty}\left(u_{2n-1}+u_{2n}\right)</equation>可由<equation>\sum_{n=1}^{\infty}u_{n}</equation>添加括号得到.由收敛级数的性质，可知当<equation>\sum_{n=1}^{\infty}u_{n}</equation>收敛时，<equation>\sum_{n=1}^{\infty}\left(u_{2n-1}+u_{2n}\right)</equation>收敛.应选A.

取<equation>u_{2n - 1} = 1, u_{2n} = -1</equation>，则<equation>\sum_{n = 1}^{\infty}\left(u_{2n - 1} + u_{2n}\right) = 0</equation>，而<equation>\sum_{n = 1}^{\infty}u_{n}</equation>发散.选项B不正确.

取<equation>u_{n} = (-1)^{n - 1}\frac{1}{n},\sum_{n = 1}^{\infty}u_{n}</equation>为交错级数，由莱布尼茨定理可知<equation>\sum_{n = 1}^{\infty}u_{n}</equation>收敛，但<equation>\begin{aligned} \sum_ {n = 1} ^ {\infty} \left(u _ {2 n - 1} - u _ {2 n}\right) &= \sum_ {n = 1} ^ {\infty} \left[ (- 1) ^ {2 n - 2} \frac {1}{2 n - 1} - (- 1) ^ {2 n - 1} \frac {1}{2 n} \right] \\ &= \sum_ {n = 1} ^ {\infty} \left(\frac {1}{2 n - 1} + \frac {1}{2 n}\right) = \sum_ {n = 1} ^ {\infty} \frac {4 n - 1}{2 n (2 n - 1)}. \end{aligned}</equation>由于<equation>\frac{4 n-1}{2 n(2 n-1)} \geqslant \frac{2 n-1}{2 n(2 n-1)}=\frac{1}{2 n}</equation>，而级数<equation>\sum_{n=1}^{\infty}\frac{1}{2 n}</equation>发散，故<equation>\sum_{n=1}^{\infty}\left(u_{2 n-1}-u_{2 n}\right)</equation>发散.选项C不正确取<equation>u_{n}=1</equation>，则<equation>\sum_{n=1}^{\infty}\left(u_{2 n-1}-u_{2 n}\right)=0</equation>，收敛，但<equation>\sum_{n=1}^{\infty}u_{n}</equation>发散.选项D不正确.

---


#### 幂级数

**2024年第4题 | 选择题 | 5分 | 答案: A**

4. 已知幂级数<equation>\sum_{n=0}^{\infty} a_{n} x^{n}</equation>的和函数为<equation>\ln(2+x)</equation>，则<equation>\sum_{n=0}^{\infty} n a_{2n}=(\quad)</equation>A.<equation>-\frac{1}{6}</equation>B.<equation>-\frac{1}{3}</equation>C.<equation>\frac{1}{6}</equation>D.<equation>\frac{1}{3}</equation>

答案: A

**解析:**解（法一）由<equation>\ln (1 + x) = \sum_{n = 1}^{\infty}(-1)^{n - 1}\frac{x^n}{n}(-1 < x\leqslant 1)</equation>可得<equation>\ln (2 + x) = \ln \left[ 2 \cdot \left(1 + \frac {x}{2}\right) \right] = \ln 2 + \ln \left(1 + \frac {x}{2}\right) = \ln 2 + \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1}}{n} \left(\frac {x}{2}\right) ^ {n}.</equation>由此可得，当<equation>n > 0</equation>时，<equation>x^{2n}</equation>的系数为<equation>a_{2n}=\frac{(-1)^{2n-1}}{2n2^{2n}}=\frac{-1}{2n2^{2n}}.</equation>因此，<equation>\sum_ {n = 0} ^ {\infty} n a _ {2 n} = \sum_ {n = 1} ^ {\infty} n a _ {2 n} = \sum_ {n = 1} ^ {\infty} \frac {- n}{2 n 2 ^ {2 n}} = \sum_ {n = 1} ^ {\infty} \frac {- 1}{2 ^ {2 n + 1}} = \frac {- \frac {1}{8}}{1 - \frac {1}{4}} = - \frac {1}{6}.</equation>应选A.

（法二）由<equation>\sum_{n = 0}^{\infty}a_nx^n = \ln (2 + x)</equation>可得<equation>\sum_{n = 0}^{\infty}a_n(-x)^n = \sum_{n = 0}^{\infty}(-1)^n a_nx^n = \ln (2 - x)</equation>.由此可得<equation>\sum_{n = 0}^{\infty}[1 + (-1)^n]a_nx^n = \ln (2 + x) + \ln (2 - x)</equation>，即<equation>2 \sum_ {n = 0} ^ {\infty} a _ {2 n} x ^ {2 n} = \ln (2 + x) + \ln (2 - x).</equation>对（1）式两端关于<equation>x</equation>求导可得，<equation>4 \sum_ {n = 1} ^ {\infty} n a _ {2 n} x ^ {2 n - 1} = \frac {1}{2 + x} - \frac {1}{2 - x}.</equation>在(2)式中令<equation>x = 1</equation>，可得<equation>4\sum_{n = 1}^{\infty}na_{2n} = \frac{1}{3} -1 = -\frac{2}{3}</equation>，进一步可得<equation>\sum_{n = 0}^{\infty}na_{2n} = -\frac{1}{6}</equation>因此，应选A.

（法三）注意到<equation>\left[ \ln (2 + x) \right] ^ {\prime} = \frac {1}{2 + x} = \frac {1}{2 \left(1 + \frac {x}{2}\right)} = \frac {1}{2} \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} \left(\frac {x}{2}\right) ^ {n},</equation>该幂级数的收敛半径为2，故在（-2，2）上，由牛顿一莱布尼茨公式可得<equation>\begin{aligned} \ln (2 + x) - \ln 2 &= \int_ {0} ^ {x} \left[ \ln (2 + t) \right] ^ {\prime} \mathrm {d} t = \int_ {0} ^ {x} \frac {1}{2} \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} \left(\frac {t}{2}\right) ^ {n} \mathrm {d} t \\ \frac {\text {逐 项 积 分}}{} \frac {1}{2} \sum_ {n = 0} ^ {\infty} \int_ {0} ^ {x} (- 1) ^ {n} \left(\frac {t}{2}\right) ^ {n} \mathrm {d} t &= \frac {1}{2} \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{n + 1} \cdot \frac {x ^ {n + 1}}{2 ^ {n}} \\ &= \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1} x ^ {n}}{n 2 ^ {n}}. \end{aligned}</equation>因此，<equation>\ln (2 + x) = \ln 2 + \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1} x ^ {n}}{n 2 ^ {n}}.</equation>其余同法一.

---

**2023年第13题 | 填空题 | 5分**

13.<equation>3. \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n}}{(2 n) !} = \underline {{}}</equation>

**答案:**<equation>\frac {\mathrm {e} ^ {x} + \mathrm {e} ^ {- x}}{2}.</equation>

**解析:**解（法一）考虑<equation>\mathrm{e}^{x}</equation>与<equation>\mathrm{e}^{-x}</equation>的幂级数展开式，<equation>\mathrm {e} ^ {x} = \sum_ {n = 0} ^ {\infty} \frac {x ^ {n}}{n !}, \quad \mathrm {e} ^ {- x} = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n} x ^ {n}}{n !}, \quad - \infty < x < + \infty .</equation>由此可得<equation>\mathrm {e} ^ {x} + \mathrm {e} ^ {- x} = \sum_ {n = 0} ^ {\infty} \frac {x ^ {n}}{n !} + \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n} x ^ {n}}{n !} = \sum_ {n = 0} ^ {\infty} \frac {\left[ 1 + (- 1) ^ {n} \right] x ^ {n}}{n !} = 2 \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n}}{(2 n) !}.</equation>因此，<equation>\sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n}}{(2 n) !} = \frac {\mathrm {e} ^ {x} + \mathrm {e} ^ {- x}}{2}.</equation>（法二）当 x=0时，<equation>\sum_{n=0}^{\infty}\frac{x^{2n}}{(2n)!}</equation>显然收敛. 又当 x≠0时，<equation>\lim _ {n \rightarrow \infty} \frac {x ^ {2 n + 2}}{(2 n + 2) !} \cdot \frac {(2 n) !}{x ^ {2 n}} = \lim _ {n \rightarrow \infty} \frac {x ^ {2}}{(2 n + 1) (2 n + 2)} = 0.</equation>由正项级数的比值审敛法可知，对任意<equation>x\neq 0</equation>，都有<equation>\sum_{n=0}^{\infty}\frac{x^{2n}}{(2n)!}</equation>收敛.因此，幂级数<equation>\sum_{n=0}^{\infty}\frac{x^{2n}}{(2n)!}</equation>的收敛域为<equation>(-\infty, +\infty).</equation>记<equation>\sum_{n=0}^{\infty}\frac{x^{2n}}{(2n)!}</equation>的和函数为 S(x)，则在<equation>(-\infty, +\infty)</equation>上，<equation>S ^ {\prime} (x) = \left[ \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n}}{(2 n) !} \right] ^ {\prime} \xlongequal {\text {逐 项 求 导}} \sum_ {n = 0} ^ {\infty} \frac {\left(x ^ {2 n}\right) ^ {\prime}}{(2 n) !} = \sum_ {n = 1} ^ {\infty} \frac {x ^ {2 n - 1}}{(2 n - 1) !},</equation><equation>S ^ {\prime \prime} (x) = \left[ \sum_ {n = 1} ^ {\infty} \frac {x ^ {2 n - 1}}{(2 n - 1) !} \right] ^ {\prime} \xlongequal {\text {逐 项 求 导}} \sum_ {n = 1} ^ {\infty} \frac {\left(x ^ {2 n - 1}\right) ^ {\prime}}{(2 n - 1) !} = \sum_ {n = 1} ^ {\infty} \frac {x ^ {2 n - 2}}{(2 n - 2) !} = \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n}}{(2 n) !}.</equation>由此可得，<equation>S^{\prime \prime}(x)=S(x), S(x)</equation>满足微分方程<equation>y^{\prime \prime}-y=0.</equation>这是一个二阶常系数齐次线性微分方程，其特征方程为<equation>r^{2}-1=0</equation>，特征根为<equation>r_{1,2}=\pm 1.</equation>从而通解为<equation>y=C_{1}\mathrm{e}^{x}+C_{2}\mathrm{e}^{-x}</equation>即<equation>S(x)=C_{1}\mathrm{e}^{x}+C_{2}\mathrm{e}^{-x}.</equation>将 x = 0 代入<equation>S ( x )=\sum_{n=0}^{\infty}\frac{x^{2 n}} {(2 n)!}, S^{\prime} ( x )=\sum_{n=1}^{\infty}\frac{x^{2 n-1}} {(2 n-1)!}</equation>可得，<equation>S ( 0 )=1, S^{\prime} ( 0 )=0.</equation>另一方面，由<equation>S ( x )=C_{1}\mathrm{e}^{x}+C_{2}\mathrm{e}^{-x}</equation>可得，<equation>S ( 0 )=C_{1}+C_{2}, S^{\prime} ( 0 )=\left(C_{1}\mathrm{e}^{x}-C_{2}\mathrm{e}^{-x}\right)\mid_{x=0}=C_{1}-C_{2}.</equation>于是，解得<equation>\left\{\begin{array}{l l} C_{1}+C_{2}=1, \\ C_{1}-C_{2}=0. \end{array} \right.</equation>因此，<equation>S ( x ) = \frac {\mathrm {e}^{x} + \mathrm {e}^{-x}}{2}.</equation>

---

**2022年第20题 | 解答题 | 12分**

20. （本题满分12分）

求幂级数<equation>\sum_ {n = 0} ^ {\infty} \frac {(- 4) ^ {n} + 1}{4 ^ {n} (2 n + 1)} x</equation>的收敛域及和函数 S(x).

**答案:**收敛域为<equation>[-1,1]</equation>，和函数<equation>S ( x )=\left\{\begin{array}{ll}\frac{\arctan x}{x}+\frac{1}{x}\ln \frac{2+x}{2-x},&x\in[-1,0)\cup(0,1],\\ 2,&x=0.\end{array}\right.</equation>

**解析:**先求收敛域.

原级数是一个缺项型幂级数，我们用比值法来求它的收敛半径.<equation>\lim _ {n \rightarrow \infty} \left| \frac {\frac {(- 4) ^ {n + 1} + 1}{4 ^ {n + 1} (2 n + 3)} x ^ {2 n + 2}}{\frac {(- 4) ^ {n} + 1}{4 ^ {n} (2 n + 1)} x ^ {2 n}} \right| = \lim _ {n \rightarrow \infty} \left| \frac {(- 4) ^ {n + 1} + 1}{(- 4) ^ {n} + 1} \cdot \frac {2 n + 1}{4 (2 n + 3)} \right| x ^ {2} = x ^ {2}.</equation>由比值审敛法可知，当<equation>| x | < 1</equation>时，原幂级数收敛；当<equation>| x | > 1</equation>时，原幂级数发散，从而收敛半径为1，收敛区间为（-1，1）.

又由于当<equation>x=\pm 1</equation>时，<equation>\text {原 幂 级 数} = \sum_ {n = 0} ^ {\infty} \frac {(- 4) ^ {n} + 1}{4 ^ {n} (2 n + 1)} = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{2 n + 1} + \sum_ {n = 0} ^ {\infty} \frac {1}{4 ^ {n} (2 n + 1)},</equation>而级数<equation>\sum_{n=0}^{\infty} \frac{(-1)^{n}}{2n+1}</equation>和<equation>\sum_{n=0}^{\infty} \frac{1}{4^{n}(2n+1)}</equation>均收敛，故原幂级数收敛。因此，原幂级数的收敛域为<equation>[-1,1]</equation>下面求和函数.

记<equation>S ( x )=\sum_{n=0}^{\infty}\frac{(-4)^{n}+1}{4^{n}(2n+1)} x^{2n}, x\in[-1,1],</equation>，则<equation>S (x) = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{2 n + 1} x ^ {2 n} + \sum_ {n = 0} ^ {\infty} \frac {1}{4 ^ {n} (2 n + 1)} x ^ {2 n}.</equation>记<equation>S_{1}(x)=\sum_{n=0}^{\infty}\frac{(-1)^{n}}{2n+1} x^{2n}, S_{2}(x)=\sum_{n=0}^{\infty}\frac{1}{4^{n}(2n+1)} x^{2n}</equation>，则当 x<equation>\in[ -1,1]</equation>时，<equation>S (x) = S _ {1} (x) + S _ {2} (x).</equation>注意到<equation>x S_{1}(x)=\sum_{n=0}^{\infty}\frac{(-1)^{n}}{2n+1} x^{2n+1}</equation>，故<equation>\begin{aligned} \left[ x S _ {1} (x) \right] ^ {\prime} &= \left[ \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{2 n + 1} x ^ {2 n + 1} \right] ^ {\prime} \xlongequal {\text {逐 项 求 导}} \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{2 n + 1} \left(x ^ {2 n + 1}\right) ^ {\prime} = \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} x ^ {2 n} \\ &= \frac {1}{1 + x ^ {2}}, \end{aligned}</equation><equation>x S _ {1} (x) = x S _ {1} (x) - 0 \times S _ {1} (0) = \int_ {0} ^ {x} \left[ t S _ {1} (t) \right] ^ {\prime} \mathrm {d} t = \int_ {0} ^ {x} \frac {1}{1 + t ^ {2}} \mathrm {d} t = \arctan x.</equation>当<equation>x \in[ - 1,0)\cup(0,1]</equation>时，<equation>S_{1}(x)=\frac{\arctan x}{x}</equation>当 x=0时，<equation>S_{1}(0)=\frac{(-1)^{0}}{2\times 0+1}=1.</equation>注意到<equation>x S_{2}(x)=\sum_{n=0}^{\infty}\frac{1}{4^{n}(2n+1)} x^{2n+1}</equation>，故<equation>\begin{aligned} \left[ x S _ {2} (x) \right] ^ {\prime} &= \left[ \sum_ {n = 0} ^ {\infty} \frac {1}{4 ^ {n} (2 n + 1)} x ^ {2 n + 1} \right] ^ {\prime} \stackrel {\mathrm {逐 项 求 导}} {=} \sum_ {n = 0} ^ {\infty} \frac {1}{4 ^ {n} (2 n + 1)} \left(x ^ {2 n + 1}\right) ^ {\prime} \\ &= \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n}}{4 ^ {n}} = \sum_ {n = 0} ^ {\infty} \left(\frac {x}{2}\right) ^ {2 n} = \frac {1}{1 - \left(\frac {x}{2}\right) ^ {2}} = \frac {4}{4 - x ^ {2}} \\ &= \frac {1}{2 - x} + \frac {1}{2 + x}, \end{aligned}</equation><equation>\begin{aligned} x S _ {2} (x) &= x S _ {2} (x) - 0 \times S _ {2} (0) = \int_ {0} ^ {x} \left[ t S _ {2} (t) \right] ^ {\prime} \mathrm {d} t = \int_ {0} ^ {x} \left(\frac {1}{2 - t} + \frac {1}{2 + t}\right) \mathrm {d} t \\ &= \ln \frac {2 + x}{2 - x}. \end{aligned}</equation>当<equation>x \in[ - 1,0)\cup(0,1]</equation>时，<equation>S_{2}(x) = \frac{1}{x}\ln \frac{2+x}{2-x}.</equation>当<equation>x=0</equation>时，<equation>S_{2}(0) = \frac{1}{1\times(2\times 0 + 1)} = 1.</equation>综上所述，幂级数的和函数为<equation>S (x) = \left\{ \begin{array}{l l} \frac {\arctan x}{x} + \frac {1}{x} \ln \frac {2 + x}{2 - x}, & x \in [ - 1, 0) \cup (0, 1 ], \\ 2, & x = 0. \end{array} \right.</equation>

---

**2021年第20题 | 解答题 | 12分**

20. (本题满分12分)

设 n为正整数，<equation>y=y_{n}(x)</equation>是微分方程<equation>x y^{\prime}-(n+1) y=0</equation>的满足条件<equation>y_{n}(1)=\frac{1}{n(n+1)}</equation>的解.

I. 求<equation>y_{n}(x)</equation>II. 求级数<equation>\sum_{n=1}^{\infty} y_{n}(x)</equation>的收敛域及和函数.

**答案:**（I）<equation>y_{n}(x)=\frac{x^{n+1}}{n(n+1)};</equation>（Ⅱ）收敛域为<equation>[-1,1]</equation>，和函数 s(x)<equation>= \left\{\begin{array}{ll}(1-x)\ln(1-x)+x,&x\in[-1,1),\\ 1,&x=1.\end{array}\right.</equation>

**解析:**解（I）整理<equation>x y^{\prime}-(n+1) y=0</equation>可得，<equation>y^{\prime}=\frac{n+1}{x} y.</equation>分离变量得<equation>\frac{\mathrm{d} y}{y}=\frac{n+1}{x}\mathrm{d} x.</equation>两端同时积分可得<equation>\ln |y|=(n+1)\ln |x|+C_{0}.</equation>于是，<equation>y_{n}(x)=Cx^{n+1}</equation>其中C为待定常数.

代入<equation>y_{n}(1)=\frac{1}{n(n+1)},</equation>可得<equation>C=\frac{1}{n(n+1)}.</equation>因此，<equation>y_{n}(x) = \frac{x^{n + 1}}{n(n + 1)}.</equation>（Ⅱ）记<equation>s(x) = \sum_{n = 1}^{\infty}\frac{x^{n + 1}}{n(n + 1)},</equation>其系数<equation>a_{n} = \frac{1}{n(n + 1)}.</equation><equation>\lim _ {n \rightarrow \infty} \left| \frac {a _ {n + 1}}{a _ {n}} \right| = \lim _ {n \rightarrow \infty} \frac {n (n + 1)}{(n + 1) (n + 2)} = 1.</equation>于是，<equation>s ( x )</equation>的收敛半径为1，收敛区间为<equation>(-1,1).</equation>s ( x ) 在 x=-1处为<equation>\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n(n+1)},</equation>由莱布尼茨定理可知该级数收敛. s ( x ) 在 x=1处为<equation>\sum_{n=1}^{\infty}\frac{1}{n(n+1)},</equation>由极限审敛法可知该级数收敛.因此，s ( x ) 的收敛域为<equation>[-1,1].</equation>下面用两种方法计算 s(x).

（法一）整理<equation>s(x).</equation>当 x<equation>\in(-1,1)</equation>时，<equation>\begin{aligned} s (x) &= \sum_ {n = 1} ^ {\infty} \left(\frac {x ^ {n + 1}}{n} - \frac {x ^ {n + 1}}{n + 1}\right) = x \sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n} - \sum_ {n = 1} ^ {\infty} \frac {x ^ {n + 1}}{n + 1} = x \sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n} - \sum_ {n = 2} ^ {\infty} \frac {x ^ {n}}{n} \\ &= (x - 1) \sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n} + x. \end{aligned}</equation>记<equation>t ( x )=\sum_{n=1}^{\infty}\frac{x^{n}}{n}</equation>，则<equation>s ( x )=(x-1)t ( x )+x.</equation><equation>t ^ {\prime} (x) = \left(\sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n}\right) ^ {\prime} \xlongequal {\text {逐 项 求 导}} \sum_ {n = 1} ^ {\infty} \left(\frac {x ^ {n}}{n}\right) ^ {\prime} = \sum_ {n = 1} ^ {\infty} x ^ {n - 1} = \frac {1}{1 - x}.</equation>注意到 t（0）=0，故<equation>t (x) = t (x) - t (0) = \int_ {0} ^ {x} \frac {1}{1 - t} \mathrm {d} t = - \ln (1 - x).</equation>于是，当 x<equation>\in(-1,1)</equation>时，s（x）=（1-x）<equation>\ln(1-x)+x.</equation>因为幂级数的和函数在收敛域上连续，且<equation>( 1-x)\ln(1-x)+x</equation>在 x=-1处连续，所以当 x<equation>\in[ -1,1)</equation>时，<equation>s (x) = (1 - x) \ln (1 - x) + x.</equation>当<equation>x=1</equation>时，<equation>s(1)=\sum_{n=1}^{\infty}\frac{1}{n(n+1)}.</equation>计算<equation>\sum_{n=1}^{\infty} \frac{1}{n(n+1)}</equation>的部分和<equation>\sum_{n=1}^{k} \frac{1}{n(n+1)}</equation>得<equation>\sum_ {n = 1} ^ {k} \frac {1}{n (n + 1)} = \sum_ {n = 1} ^ {k} \left(\frac {1}{n} - \frac {1}{n + 1}\right) = 1 - \frac {1}{2} + \frac {1}{2} - \frac {1}{3} + \dots + \frac {1}{k} - \frac {1}{k + 1} = 1 - \frac {1}{k + 1}.</equation>于是，<equation>\sum_{n = 1}^{\infty}\frac{1}{n(n + 1)} = \lim_{k\to \infty}\sum_{n = 1}^{k}\frac{1}{n(n + 1)} = \lim_{k\to \infty}\left(1 - \frac{1}{k + 1}\right) = 1.</equation>因此，s（x）为分段函数.<equation>s (x) = \left\{ \begin{array}{l l} (1 - x) \ln (1 - x) + x, & x \in [ - 1, 1), \\ 1, & x = 1. \end{array} \right.</equation>（法二）当<equation>x\in(-1,1)</equation>时，<equation>s ^ {\prime} (x) = \left[ \sum_ {n = 1} ^ {\infty} \frac {x ^ {n + 1}}{n (n + 1)} \right] ^ {\prime} \xlongequal {\text {逐 项 求 导}} \sum_ {n = 1} ^ {\infty} \left[ \frac {x ^ {n + 1}}{n (n + 1)} \right] ^ {\prime} = \sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n}.</equation><equation>s ^ {\prime \prime} (x) = \left(\sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n}\right) ^ {\prime} \xlongequal {\text {逐 项 求 导}} \sum_ {n = 1} ^ {\infty} \left(\frac {x ^ {n}}{n}\right) ^ {\prime} = \sum_ {n = 1} ^ {\infty} x ^ {n - 1} = \frac {1}{1 - x}.</equation>注意到<equation>s^{\prime}(0)=0</equation>，故<equation>s ^ {\prime} (x) = s ^ {\prime} (x) - s ^ {\prime} (0) = \int_ {0} ^ {x} \frac {1}{1 - t} \mathrm {d} t = - \ln (1 - t) \Big | _ {0} ^ {x} = - \ln (1 - x).</equation>又因为 s（0）=0，所以<equation>\begin{aligned} s (x) &= s (x) - s (0) = \int_ {0} ^ {x} [ - \ln (1 - t) ] \mathrm {d} t = - \left[ t \ln (1 - t) \left| _ {0} ^ {x} - \int_ {0} ^ {x} \frac {- t}{1 - t} \mathrm {d} t \right. \right] \\ &= - x \ln (1 - x) - \int_ {0} ^ {x} \frac {t}{1 - t} \mathrm {d} t = - x \ln (1 - x) - \int_ {0} ^ {x} \left(- 1 + \frac {1}{1 - t}\right) \mathrm {d} t \\ &= - x \ln (1 - x) - \left[ - t - \ln (1 - t) \right] \left| _ {0} ^ {x} = - x \ln (1 - x) + \left[ t + \ln (1 - t) \right] \right| _ {0} ^ {x} \\ &= - x \ln (1 - x) + x + \ln (1 - x) = (1 - x) \ln (1 - x) + x. \end{aligned}</equation>其余同法一.

---

**2020年第4题 | 选择题 | 4分 | 答案: B**

4. 设幂级数<equation>\sum_{n=1}^{\infty} n a_{n}(x-2)^{n}</equation>的收敛区间为（-2，6），则<equation>\sum_{n=1}^{\infty} a_{n}(x+1)^{2n}</equation>的收敛区间为（    )

A. (-2,6) B. (-3,1) C. (-5,3) D. (-17,15)

答案: B

**解析:**解 由已知条件可得，幂级数<equation>\sum_{n=1}^{\infty} n a_{n}(x-2)^{n}=(x-2)\sum_{n=1}^{\infty} n a_{n}(x-2)^{n-1}</equation>的收敛中心为2，收敛区间为（-2，6），故收敛半径为6-2=4.由收敛半径的平移不变性可知，<equation>\sum_{n=1}^{\infty} n a_{n} x^{n-1}</equation>的收敛半径为4.记<equation>s(x)=\int_{0}^{x}\sum_{n=1}^{\infty} n a_{n} t^{n-1}\mathrm{d}t</equation>则<equation>s(x)\overset{\mathrm{逐项积分}}{=}\sum_{n=1}^{\infty}\int_{0}^{x} n a_{n} t^{n-1}\mathrm{d}t=\sum_{n=1}^{\infty} a_{n} x^{n}.</equation>由收敛半径的逐项积分不变性可知，<equation>\sum_{n=1}^{\infty} a_{n} x^{n}</equation>的收敛半径也为4.<equation>\sum_{n=1}^{\infty} a_{n}(x+1)^{2n}</equation>为缺项幂级数，其收敛半径等于<equation>\sum_{n=1}^{\infty} a_{n} x^{2n}</equation>的收敛半径.由<equation>\sum_{n=1}^{\infty} a_{n} x^{n}</equation>的收敛半径为4可得，<equation>\sum_{n=1}^{\infty} a_{n} x^{2n}</equation>的收敛半径为2.又因为<equation>\sum_{n=1}^{\infty} a_{n}(x+1)^{2n}</equation>的收敛中心为-1，所以其收敛区间为（-3，1）因此，应选B.

---

**2018年第18题 | 解答题 | 10分**

18. (本题满分10分)

已知<equation>\cos 2x-\frac{1}{(1+x)^{2}}=\sum_{n=0}^{\infty}a_{n}x^{n}(-1<x<1)</equation>，求<equation>a_{n}.</equation>

**答案:**<equation>a _ {n} = \left\{ \begin{array}{l l} \frac {(- 1) ^ {k} 4 ^ {k}}{(2 k) !} - 2 k - 1, & n = 2 k, \\ 2 k + 2, & n = 2 k + 1, \end{array} \right. \mathrm {其 中} k \mathrm {为 非 负 整 数}.</equation>

**解析:**由<equation>\cos x</equation>的幂级数展开式可得，<equation>\cos 2 x = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n} (2 x) ^ {2 n}}{(2 n) !} = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n} 4 ^ {n} x ^ {2 n}}{(2 n) !}, - \infty < x < + \infty .</equation>注意到<equation>\left(\frac{1}{1+x}\right)^{\prime}=-\frac{1}{(1+x)^{2}}</equation>故<equation>\begin{aligned} - \frac {1}{(1 + x) ^ {2}} &= \left(\frac {1}{1 + x}\right) ^ {\prime} = \left[ \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} x ^ {n} \right] ^ {\prime} = \sum_ {n = 1} ^ {\infty} (- 1) ^ {n} n x ^ {n - 1} \\ &= \sum_ {n = 0} ^ {\infty} (- 1) ^ {n + 1} (n + 1) x ^ {n}, - 1 < x < 1. \end{aligned}</equation>于是，<equation>\cos 2 x - \frac {1}{(1 + x) ^ {2}} = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n} 4 ^ {n} x ^ {2 n}}{(2 n) !} + \sum_ {n = 0} ^ {\infty} (- 1) ^ {n + 1} (n + 1) x ^ {n} = \sum_ {n = 0} ^ {\infty} a _ {n} x ^ {n}, - 1 < x < 1.</equation>由于<equation>a_{n}</equation>为<equation>x^{n}</equation>的系数，故<equation>\sum_{n=0}^{\infty}\frac{(-1)^{n}4^{n}x^{2n}}{(2n)!}+\sum_{n=0}^{\infty}(-1)^{n+1}(n+1)x^{n}</equation>中<equation>x^{n}</equation>的系数等于<equation>a_{n}.</equation>当<equation>n=2k</equation>，<equation>k=0,1,2,\dots</equation>时，<equation>a _ {2 k} = \frac {(- 1) ^ {k} 4 ^ {k}}{(2 k) !} + (- 1) ^ {2 k + 1} (2 k + 1) = \frac {(- 1) ^ {k} 4 ^ {k}}{(2 k) !} - 2 k - 1.</equation>当<equation>n = 2k + 1</equation>，<equation>k = 0,1,2,\dots</equation>时，<equation>a _ {2 k + 1} = (- 1) ^ {2 k + 1 + 1} (2 k + 1 + 1) = 2 k + 2.</equation>因此，<equation>a _ {n} = \left\{ \begin{array}{l l} \frac {(- 1) ^ {k} 4 ^ {k}}{(2 k) !} - 2 k - 1, & n = 2 k, \\ 2 k + 2, & n = 2 k + 1, \end{array} \right.</equation>其中 k为非负整数.

---

**2017年第19题 | 解答题 | 10分**

19. (本题满分10分)

若<equation>a_{0}=1, a_{1}=0, a_{n+1}=\frac{1}{n+1}\left(n a_{n}+a_{n-1}\right)\left(n=1, 2, 3, \cdots\right), S(x)</equation>为幂级数<equation>\sum_{n=0}^{\infty}a_{n}x^{n}</equation>的和函数.

I. 证明<equation>\sum_{n=0}^{\infty}a_{n}x^{n}</equation>的收敛半径不小于1；

II. 证明<equation>(1 - x)S^{\prime}(x) - xS(x) = 0,(x\in (-1,1))</equation>，并求<equation>S(x)</equation>的表达式.

**答案:**（I）证明略；

（Ⅱ）证明略，<equation>S ( x )=\frac{\mathrm{e}^{-x}}{1-x}, x \in(-1,1).</equation>

**解析:**解（I）（法一）利用阿贝尔定理.我们证明在（-1，1）内，幂级数<equation>\sum_{n=0}^{\infty} a_{n} x^{n}</equation>绝对收敛，从而由阿贝尔定理可知幂级数的收敛半径不小于1.

首先，证明对任意的<equation>n=0,1,2,\dots</equation>，若 m≤n，则<equation>|a_{m}| \leqslant 1.</equation>由已知条件，<equation>a_{0}=1, a_{1}=0</equation>，故<equation>a_{2}=\frac{1}{2}(0+1)=\frac{1}{2}\leqslant1.</equation>假设对<equation>n = k</equation>时，命题成立，则当<equation>n = k + 1</equation>时，只需证明<equation>|a_{k + 1}| \leqslant 1</equation>.

由递推式<equation>a_{n + 1} = \frac{1}{n + 1}\left(n a_{n} + a_{n - 1}\right)</equation>以及归纳假设可得，<equation>\left| a _ {k + 1} \right| \leqslant \frac {k}{k + 1} \left| a _ {k} \right| + \frac {1}{k + 1} \left| a _ {k - 1} \right| \leqslant \frac {k}{k + 1} + \frac {1}{k + 1} = 1.</equation>由数学归纳法可知，对任意的 n=0，1，2，…，若 m≤n，则<equation>|a_{m}| \leqslant 1.</equation>由此易知，对任意的 n=0， 1，2，…，<equation>|a_{n}| \leqslant 1.</equation><equation>x _ {0} \in (- 1, 1)</equation><equation>\sum_ {n = 0} ^ {\infty} x _ {0} ^ {n}</equation><equation>\left| a _ {n} \right| \leqslant 1</equation><equation>\left| a _ {n} x _ {0} ^ {n} \right| \leqslant \left| x _ {0} ^ {n} \right|</equation><equation>\sum_ {n = 0} ^ {\infty} \left| a _ {n} x _ {0} ^ {n} \right| \leqslant \sum_ {n = 0} ^ {\infty} \left| x _ {0} ^ {n} \right|</equation><equation>\sum_ {n = 0} ^ {\infty} a _ {n} x _ {0} ^ {n}</equation>由于对任意的<equation>x_{0}\in(-1,1)</equation>，级数<equation>\sum_{n=0}^{\infty} a_{n} x_{0}^{n}</equation>均绝对收敛，故由阿贝尔定理可知，幂级数<equation>\sum_{n=0}^{\infty} a_{n} x^{n}</equation>的收敛半径不小于1.

下面的法二、法三均需要计算<equation>a_{n}</equation>的表达式，并且可计算得幂级数的收敛半径实际上等于1.

由<equation>a_{n+1}=\frac{1}{n+1} \left(n a_{n}+a_{n-1}\right) \left(n=1,2,3,\cdots\right)</equation>可得<equation>a _ {n + 1} - a _ {n} = - \frac {1}{n + 1} \left(a _ {n} - a _ {n - 1}\right) (n = 1, 2, 3, \dots).</equation>于是，<equation>a _ {n} - a _ {n - 1} = \frac {- 1}{n} \left(a _ {n - 1} - a _ {n - 2}\right) = \frac {- 1}{n} \cdot \frac {- 1}{n - 1} \left(a _ {n - 2} - a _ {n - 3}\right) = \dots = \frac {(- 1) ^ {n - 1}}{n !} \left(a _ {1} - a _ {0}\right) = \frac {(- 1) ^ {n}}{n !}.</equation>因此，<equation>a _ {n} = \sum_ {k = 1} ^ {n} \left(a _ {k} - a _ {k - 1}\right) + a _ {0} = \sum_ {k = 1} ^ {n} \frac {(- 1) ^ {k}}{k !} + 1 = \sum_ {k = 0} ^ {n} \frac {(- 1) ^ {k}}{k !}.</equation>注意到<equation>\mathrm{e}^{-x}=\sum_{n=0}^{\infty}\frac{(-1)^{n}x^{n}}{n!}</equation>，故<equation>\lim_{n\to \infty}a_{n}=\mathrm{e}^{-1}.</equation>下面我们用两种方法证明<equation>\sum a_{n}x^{n}</equation>的收敛半径等于1.

（法二）考虑<equation>\left| \frac{a_{n+1}}{a_{n}} \right|.</equation>由<equation>\lim_{n\rightarrow\infty}a_{n}=\mathrm{e}^{-1}</equation>，可得<equation>\lim_{n\rightarrow\infty}a_{n+1}=\mathrm{e}^{-1}</equation>，从而<equation>\lim _ {n \rightarrow \infty} \left| \frac {a _ {n + 1}}{a _ {n}} \right| = 1.</equation>因此，幂级数<equation>\sum_{n=0}^{\infty} a_{n} x^{n}</equation>的收敛半径等于1.

（法三）考虑<equation>\sqrt[n]{|a_n|}.</equation><equation>\lim _ {n \rightarrow \infty} \sqrt [ n ]{| a _ {n} |} = \lim _ {n \rightarrow \infty} \mathrm {e} ^ {\frac {1}{n} \ln | a _ {n} |} = \mathrm {e} ^ {\lim _ {n \rightarrow \infty} \frac {\ln | a _ {n} |}{n}} \underline {{\frac {\lim _ {n \rightarrow \infty} a _ {n} = \mathrm {e} ^ {- 1}}{n}}} \mathrm {e} ^ {\lim _ {n \rightarrow \infty} \frac {- 1}{n}} = 1.</equation><equation>\sum_ {n = 0} ^ {\infty} a _ {n} x ^ {n}</equation>（Ⅱ）由第（Ⅰ）问可知，在区间（-1，1）内，<equation>S ( x )</equation>可逐项求导.<equation>x S (x) = \sum_ {n = 0} ^ {\infty} a _ {n} x ^ {n + 1} = \sum_ {n = 1} ^ {\infty} a _ {n - 1} x ^ {n},</equation><equation>S ^ {\prime} (x) = \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n - 1},</equation><equation>(1 - x) S ^ {\prime} (x) = \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n - 1} - \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n} = \sum_ {n = 0} ^ {\infty} (n + 1) a _ {n + 1} x ^ {n} - \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n}.</equation>将<equation>a_{n+1}=\frac{1}{n+1}\left(n a_{n}+a_{n-1}\right)\left(n=1,2,3,\dots\right)</equation>代入<equation>(1-x)S^{\prime}(x)</equation>，得<equation>\begin{aligned} (1 - x) S ^ {\prime} (x) - x S (x) &= \sum_ {n = 0} ^ {\infty} (n + 1) a _ {n + 1} x ^ {n} - \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n} - \sum_ {n = 1} ^ {\infty} a _ {n - 1} x ^ {n} \\ &= a _ {1} + \sum_ {n = 1} ^ {\infty} \left(n a _ {n} + a _ {n - 1}\right) x ^ {n} - \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n} - \sum_ {n = 1} ^ {\infty} a _ {n - 1} x ^ {n} = a _ {1} = 0. \end{aligned}</equation>解微分方程（1-x）y'-xy=0.分离变量得<equation>\frac {\mathrm {d} y}{y} = \left(\frac {x}{1 - x}\right) \mathrm {d} x.</equation>上式两端积分得<equation>\ln | y | = \int \left(- 1 + \frac {1}{1 - x}\right) \mathrm {d} x = - x - \ln (1 - x) + C.</equation>当 x=0时，y=1，代入上式得 C=0.由于初值为<equation>y(0)=1>0</equation>，故取<equation>\ln y=-x-\ln(1-x)</equation>即<equation>y=\frac{\mathrm{e}^{-x}}{1-x}.</equation>因此，<equation>S ( x ) = \frac {\mathrm {e}^{- x}}{1 - x}, x \in(-1,1).</equation>

---

**2016年第19题 | 解答题 | 10分**

19. (本题满分10分)

求幂级数<equation>\sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n + 2}}{(n + 1) (2 n + 1)}</equation>的收敛域及和函数.

**答案:**收敛域为<equation>[-1,1]</equation>，和函数 s(x)<equation>\left\{\begin{array}{l l}x\ln \frac{1+x}{1-x}+\ln(1-x^{2}),&x\in(-1,1),\\ 2\ln 2,&x=\pm 1.\end{array}\right.</equation>

**解析:**解 先求收敛域.

原级数是一个缺项型幂级数，我们用比值法来求它的收敛半径.<equation>\lim _ {n \rightarrow \infty} \left| \frac {\frac {x ^ {2 n + 4}}{(n + 2) (2 n + 3)}}{\frac {x ^ {2 n + 2}}{(n + 1) (2 n + 1)}} \right| = \lim _ {n \rightarrow \infty} \left| \frac {(n + 1) (2 n + 1)}{(n + 2) (2 n + 3)} x ^ {2} \right| = x ^ {2}.</equation>由比值审敛法可知，当<equation>|x| < 1</equation>时，原幂级数收敛；当<equation>|x| > 1</equation>时，原幂级数发散，从而收敛半径为1，收敛区间为（-1，1）.

又由于当 x=<equation>\pm 1</equation><equation>\text {原 幂 级 数} = \sum_ {n = 0} ^ {\infty} \frac {1}{(n + 1) (2 n + 1)} \leqslant \sum_ {n = 0} ^ {\infty} \frac {1}{(n + 1) ^ {2}} = \sum_ {n = 1} ^ {\infty} \frac {1}{n ^ {2}},</equation>而<equation>\sum_{n=1}^{\infty}\frac{1}{n^{2}}</equation>收敛，故原幂级数收敛.因此，原幂级数的收敛域为[-1,1].

下面求和函数.

（法一）记<equation>s(x)=\sum_{n=0}^{\infty}\frac{x^{2n+2}}{(n+1)(2n+1)}, x\in[-1,1].</equation>在收敛区间内，可对幂级数进行逐项求导，且不改变幂级数的收敛半径，从而<equation>s ^ {\prime} (x) = \left[ \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n + 2}}{(n + 1) (2 n + 1)} \right] ^ {\prime} = \sum_ {n = 0} ^ {\infty} \left[ \frac {x ^ {2 n + 2}}{(n + 1) (2 n + 1)} \right] ^ {\prime} = 2 \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n + 1}}{2 n + 1}, x \in (- 1, 1),</equation><equation>s ^ {\prime \prime} (x) = 2 \left(\sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n + 1}}{2 n + 1}\right) ^ {\prime} = 2 \sum_ {n = 0} ^ {\infty} \left(\frac {x ^ {2 n + 1}}{2 n + 1}\right) ^ {\prime} = 2 \sum_ {n = 0} ^ {\infty} x ^ {2 n} = \frac {2}{1 - x ^ {2}}, x \in (- 1, 1).</equation>先求<equation>s^{\prime}(x).</equation>.由于<equation>s^{\prime}(0)=0</equation>，故<equation>s ^ {\prime} (x) = \int_ {0} ^ {x} s ^ {\prime \prime} (t) \mathrm {d} t = \int_ {0} ^ {x} \frac {2}{1 - t ^ {2}} \mathrm {d} t = \int_ {0} ^ {x} \left(\frac {1}{1 - t} + \frac {1}{1 + t}\right) \mathrm {d} t = \ln \frac {1 + x}{1 - x}, x \in (- 1, 1).</equation>又因为 s（0）=0，所以<equation>\begin{aligned} s (x) &= \int_ {0} ^ {x} s ^ {\prime} (t) \mathrm {d} t = \int_ {0} ^ {x} \left[ \ln (1 + t) - \ln (1 - t) \right] \mathrm {d} t \\ \underline {{\mathrm {分 部 积 分}}} t \left[ \ln (1 + t) - \ln (1 - t) \right] \left| _ {0} ^ {x} - \int_ {0} ^ {x} t \left(\frac {1}{1 + t} + \frac {1}{1 - t}\right) \mathrm {d} t \right. \\ &= x \ln \frac {1 + x}{1 - x} - \int_ {0} ^ {x} \frac {2 t}{1 - t ^ {2}} \mathrm {d} t = x \ln \frac {1 + x}{1 - x} + \int_ {0} ^ {x} \frac {\mathrm {d} \left(1 - t ^ {2}\right)}{1 - t ^ {2}} \\ &= x \ln \frac {1 + x}{1 - x} + \ln \left(1 - x ^ {2}\right), x \in (- 1, 1). \end{aligned}</equation>最后，由于幂级数的和函数在收敛域上连续，故<equation>\begin{aligned} s (1) &= \lim _ {x \rightarrow 1 ^ {-}} s (x) = \lim _ {x \rightarrow 1 ^ {-}} \left[ x \ln \frac {1 + x}{1 - x} + \ln \left(1 - x ^ {2}\right)\right] \\ &= \lim _ {x \rightarrow 1 ^ {-}} \left[ x \ln (1 + x) - x \ln (1 - x) + \ln (1 + x) + \ln (1 - x) \right] \\ &= \lim _ {x \rightarrow 1 ^ {-}} \left[ (1 + x) \ln (1 + x) + (1 - x) \ln (1 - x) \right] \\ \underline {{\underline {{\lim _ {x \rightarrow 1 ^ {-}}} (1 - x) \ln (1 - x) \stackrel {\mathrm {洛 必 达}} {=} 0}}} 2 \ln 2 + 0 &= 2 \ln 2. \end{aligned}</equation>同理可得 s（-1）=2ln2.

因此，<equation>s ( x ) = \left\{ \begin{array}{l l} x \ln \frac {1 + x}{1 - x} + \ln \left( 1 - x^{2} \right), & x \in(-1,1), \\ 2 \ln 2, & x = \pm 1. \end{array} \right.</equation>（法二）记<equation>\begin{aligned} s (x) &= \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n + 2}}{(n + 1) (2 n + 1)} = 2 \cdot \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n + 2}}{(2 n + 1) (2 n + 2)} \\ &= 2 \cdot \sum_ {n = 0} ^ {\infty} \left(\frac {x ^ {2 n + 2}}{2 n + 1} - \frac {x ^ {2 n + 2}}{2 n + 2}\right), x \in [ - 1, 1 ]. \end{aligned}</equation>记<equation>s_{1}(x)=\sum_{n=0}^{\infty}\frac{x^{2n+1}}{2n+1}, s_{2}(x)=\sum_{n=0}^{\infty}\frac{x^{2n+2}}{2n+2}, x\in(-1,1),</equation>则当<equation>x\in(-1,1)</equation>时，<equation>s (x) = 2 \left[ x s _ {1} (x) - s _ {2} (x) \right].</equation>下面我们分别计算<equation>s_{1}(x)</equation>与<equation>s_{2}(x).</equation>由于<equation>s_1^{\prime}(x) = \left(\sum_{n = 0}^{\infty}\frac{x^{2n + 1}}{2n + 1}\right)^{\prime} = \sum_{n = 0}^{\infty}\left(\frac{x^{2n + 1}}{2n + 1}\right)^{\prime} = \sum_{n = 0}^{\infty}x^{2n} = \frac{1}{1 - x^2}, x\in(-1,1), s_1(0) = 0</equation>，故<equation>s _ {1} (x) = \int_ {0} ^ {x} \frac {1}{1 - t ^ {2}} \mathrm {d} t = \frac {1}{2} \ln \frac {1 + x}{1 - x}, x \in (- 1, 1).</equation>由于<equation>s_2^{\prime}(x) = \left(\sum_{n = 0}^{\infty}\frac{x^{2n + 2}}{2n + 2}\right)^{\prime} = \sum_{n = 0}^{\infty}\left(\frac{x^{2n + 2}}{2n + 2}\right)^{\prime} = \sum_{n = 0}^{\infty}x^{2n + 1} = \frac{x}{1 - x^2},x\in(-1,1),s_2(0) = 0</equation>，故<equation>s _ {2} (x) = \int_ {0} ^ {x} \frac {t}{1 - t ^ {2}} \mathrm {d} t = - \frac {1}{2} \ln \left(1 - x ^ {2}\right), x \in (- 1, 1).</equation>因此，当<equation>x\in(-1,1)</equation>时，<equation>s (x) = 2 \left[ x s _ {1} (x) - s _ {2} (x) \right] = x \ln \frac {1 + x}{1 - x} + \ln \left(1 - x ^ {2}\right).</equation>其余同法一.

---

**2014年第18题 | 解答题 | 10分**

18. (本题满分10分)

求幂级数<equation>\sum_{n=0}^{\infty} ( n+1 ) ( n+3 ) x^{n}</equation>的收敛域及和函数.

**答案:**(18) 收敛域为<equation>(-1,1)</equation>，和函数<equation>s(x) = \frac{3 - x}{(1 - x)^{3}}.</equation>

**解析:**解 先求收敛域.

令<equation>a_{n} = (n + 1)(n + 3)</equation>，则<equation>\lim _ {n \rightarrow \infty} \left| \frac {a _ {n + 1}}{a _ {n}} \right| = \lim _ {n \rightarrow \infty} \frac {(n + 2) (n + 4)}{(n + 1) (n + 3)} = 1,</equation>从而幂级数的收敛半径为1，收敛区间为（-1，1）.又因为幂级数在 x=<equation>\pm 1</equation>时发散，所以幂级数的收敛域为（-1，1）.

下面求和函数.

（法一）记<equation>s ( x )=\sum_{n=0}^{\infty} ( n+1 ) ( n+3 ) x^{n}, x\in(-1,1).</equation>由于幂级数在其收敛区间内可逐项求导和逐项积分，故<equation>\begin{aligned} s (x) &= \sum_ {n = 0} ^ {\infty} (n + 1) (n + 3) x ^ {n} = \sum_ {n = 0} ^ {\infty} (n + 3) \left(x ^ {n + 1}\right) ^ {\prime} = \sum_ {n = 0} ^ {\infty} \left(x ^ {n + 1}\right) ^ {\prime} + \sum_ {n = 0} ^ {\infty} (n + 2) \left(x ^ {n + 1}\right) ^ {\prime} \\ &= \left(\sum_ {n = 0} ^ {\infty} x ^ {n + 1}\right) ^ {\prime} + \sum_ {n = 0} ^ {\infty} \left(x ^ {n + 2}\right) ^ {\prime \prime} = \left(\sum_ {n = 0} ^ {\infty} x ^ {n + 1}\right) ^ {\prime} + \left(\sum_ {n = 0} ^ {\infty} x ^ {n + 2}\right) ^ {\prime \prime} = \left(\frac {x}{1 - x}\right) ^ {\prime} + \left(\frac {x ^ {2}}{1 - x}\right) ^ {\prime \prime} \\ &= \frac {1}{(1 - x) ^ {2}} + \frac {2}{(1 - x) ^ {3}} = \frac {3 - x}{(1 - x) ^ {3}}, x \in (- 1, 1). \end{aligned}</equation>因此，幂级数的和函数为<equation>s ( x )=\frac{3-x}{(1-x)^{3}}, x\in(-1,1).</equation>（法二）也可以如下计算<equation>s(x).</equation><equation>\begin{aligned} s (x) &= \sum_ {n = 0} ^ {\infty} (n + 1) (n + 3) x ^ {n} = \sum_ {n = 0} ^ {\infty} (n + 3) \left(x ^ {n + 1}\right) ^ {\prime} = 3 \sum_ {n = 0} ^ {\infty} \left(x ^ {n + 1}\right) ^ {\prime} + \sum_ {n = 0} ^ {\infty} n \left(x ^ {n + 1}\right) ^ {\prime} \\ &= 3 \left(\sum_ {n = 0} ^ {\infty} x ^ {n + 1}\right) ^ {\prime} + \sum_ {n = 0} ^ {\infty} (n + 1) n x ^ {n} = 3 \cdot \left(\frac {x}{1 - x}\right) ^ {\prime} + x \cdot \sum_ {n = 0} ^ {\infty} (n + 1) n x ^ {n - 1} \\ &= \frac {3}{(1 - x) ^ {2}} + x \cdot \sum_ {n = 0} ^ {\infty} \left(x ^ {n + 1}\right) ^ {\prime \prime} = \frac {3}{(1 - x) ^ {2}} + x \cdot \left(\frac {x}{1 - x}\right) ^ {\prime \prime} = \frac {3}{(1 - x) ^ {2}} + \frac {2 x}{(1 - x) ^ {3}} \\ &= \frac {3 - x}{(1 - x) ^ {3}}, x \in (- 1, 1). \end{aligned}</equation>

---

**2009年第11题 | 填空题 | 4分**

11. 幂级数<equation>\sum_{n=1}^{\infty} \frac{\mathrm{e}^{n}-(-1)^{n}}{n^{2}} x^{n}</equation>的收敛半径为 ___

**解析:**<equation>a _ {n} = \frac {\mathrm {e} ^ {n} - (- 1) ^ {n}}{n ^ {2}}</equation><equation>\lim _ {n \rightarrow \infty} \left| \frac {a _ {n + 1}}{a _ {n}} \right| = \lim _ {n \rightarrow \infty} \frac {\frac {\mathrm {e} ^ {n + 1} - (- 1) ^ {n + 1}}{(n + 1) ^ {2}}}{\frac {\mathrm {e} ^ {n} - (- 1) ^ {n}}{n ^ {2}}} = \lim _ {n \rightarrow \infty} \frac {\mathrm {e} ^ {n + 1} - (- 1) ^ {n + 1}}{\mathrm {e} ^ {n} - (- 1) ^ {n}} \cdot \frac {n ^ {2}}{(n + 1) ^ {2}} = \lim _ {n \rightarrow \infty} \frac {\mathrm {e} - \frac {(- 1) ^ {n + 1}}{\mathrm {e} ^ {n}}}{1 - \frac {(- 1) ^ {n}}{\mathrm {e} ^ {n}}} \cdot 1 = \mathrm {e}.</equation>因此，幂级数的收敛半径为<equation>\frac{1}{e}。</equation>

---


### 多元函数微积分学


#### 交换积分次序与坐标系之间的转化

**2025年第4题 | 选择题 | 5分 | 答案: D**

4. 设函数 f(x) 连续，<equation>\int_{0}^{1}\mathrm{d}y\int_{0}^{y}f(x)\mathrm{d}x=</equation>(    )

A.<equation>\int_{0}^{1}x f(x)\mathrm{d}x</equation>B.<equation>\int_{0}^{1}(x+1)f(x)\mathrm{d}x</equation>C.<equation>\int_{0}^{1}(x-1)f(x)\mathrm{d}x</equation>D.<equation>\int_{0}^{1}(1-x)f(x)\mathrm{d}x</equation>

答案: D

**解析:**解 二次积分<equation>\int_{0}^{1}\mathrm{d}y\int_{0}^{y}f(x)\mathrm{d}x</equation>对应的二重积分的积分区域<equation>D = \left\{(x, y) \mid 0 \leqslant x \leqslant y, 0 \leqslant y \leqslant 1 \right\}.</equation>区域 D如图所示.将 D写成 X型区域.<equation>D = \left\{(x, y) \mid x \leqslant y \leqslant 1, 0 \leqslant x \leqslant 1 \right\}.</equation>于是，<equation>\int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {y} f (x) \mathrm {d} x = \iint_ {D} f (x) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} f (x) \mathrm {d} x \int_ {x} ^ {1} \mathrm {d} y = \int_ {0} ^ {1} (1 - x) f (x) \mathrm {d} x.</equation>因此，应选D.

---

**2024年第3题 | 选择题 | 5分 | 答案: A**

3. 设 f(x,y)是连续函数，则<equation>\int_{\frac{\pi}{6}}^{\frac{\pi}{2}} \mathrm{d} x \int_{\sin x}^{1} f(x,y) \mathrm{d} y=</equation>(    )

A.<equation>\int_{\frac{1}{2}}^{1} \mathrm{d} y \int_{\frac{\pi}{6}}^{\arcsin y} f(x,y) \mathrm{d} x</equation>B.<equation>\int_{\frac{1}{2}}^{1} \mathrm{d} y \int_{\arcsin y}^{\frac{\pi}{2}} f(x,y) \mathrm{d} x</equation>C.<equation>\int_{0}^{\frac{1}{2}} \mathrm{d} y \int_{\frac{\pi}{6}}^{\arcsin y} f(x,y) \mathrm{d} x</equation>D.<equation>\int_{0}^{\frac{1}{2}} \mathrm{d} y \int_{\arcsin y}^{\frac{\pi}{2}} f(x,y) \mathrm{d} x</equation>

答案: A

**解析:**解二次积分<equation>\int_{\frac{\pi}{6}}^{\frac{\pi}{2}} \mathrm{d} x \int_{\sin x}^{1} f(x,y)\mathrm{d} y</equation>对应的二重积分的积分区域为<equation>D = \left\{(x, y) \mid \sin x \leqslant y \leqslant 1, \frac {\pi}{6} \leqslant x \leqslant \frac {\pi}{2} \right\}.</equation>由于<equation>\arcsin y</equation>的值域为<equation>\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>，而<equation>\left[\frac{\pi}{6},\frac{\pi}{2}\right]\subset\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>，故曲线<equation>y=\sin x \left(x\in\left[\frac{\pi}{6},\frac{\pi}{2}\right]\right)</equation>上的点（x,y）可写为（<equation>\arcsin y,y).</equation>由此可将 D改写成Y型区域，<equation>D = \left\{(x, y) \mid \frac {\pi}{6} \leqslant x \leqslant \arcsin y, \frac {1}{2} \leqslant y \leqslant 1 \right\}.</equation>因此，<equation>\int_ {\frac {\pi}{6}} ^ {\frac {\pi}{2}} \mathrm {d} x \int_ {\sin x} ^ {1} f (x, y) \mathrm {d} y = \int_ {\frac {1}{2}} ^ {1} \mathrm {d} y \int_ {\frac {\pi}{6}} ^ {\arcsin y} f (x, y) \mathrm {d} x.</equation>应选A.

---

**2015年第3题 | 选择题 | 4分 | 答案: B**

3. 设<equation>D=\{(x,y)\mid x^{2}+y^{2}\leqslant 2x,x^{2}+y^{2}\leqslant 2y\}</equation>，函数 f(x,y)在 D上连续，则<equation>\iint_{D}f(x,y)\mathrm{d}x\mathrm{d}y=</equation>(    )

A.<equation>\int_{0}^{\frac{\pi}{4}}\mathrm{d}\theta \int_{0}^{2\cos \theta}f(r\cos \theta,r\sin \theta)r\mathrm{d}r+\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}\mathrm{d}\theta \int_{0}^{2\sin \theta}f(r\cos \theta,r\sin \theta)r\mathrm{d}r</equation>B.<equation>\int_{0}^{\frac{\pi}{4}}\mathrm{d}\theta \int_{0}^{2\sin \theta}f(r\cos \theta,r\sin \theta)r\mathrm{d}r+\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}\mathrm{d}\theta \int_{0}^{2\cos \theta}f(r\cos \theta,r\sin \theta)r\mathrm{d}r</equation>C.<equation>2\int_{0}^{1}\mathrm{d}x\int_{1-\sqrt{1-x^{2}}}^{x}f(x,y)\mathrm{d}y</equation>D.<equation>2\int_{0}^{1}\mathrm{d}x\int_{x}^{\sqrt{2x-x^{2}}}f(x,y)\mathrm{d}y</equation>

答案: B

**解析:**解 圆<equation>x^{2}+y^{2}=2x</equation>的极坐标方程为<equation>r=2\cos \theta</equation>，圆<equation>x^{2}+y^{2}=2y</equation>的极坐标方程为<equation>r=2\sin \theta.</equation>由图可知，当<equation>0\leqslant \theta \leqslant \frac{\pi}{4}</equation>时，D的边界为<equation>r=2\sin \theta</equation>；当<equation>\frac{\pi}{4}\leqslant \theta \leqslant \frac{\pi}{2}</equation>时，D的边界为<equation>r=2\cos \theta</equation>于是，<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2 \sin \theta , 0 \leqslant \theta \leqslant \frac {\pi}{4} \right\} \cup \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2 \cos \theta , \frac {\pi}{4} \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation>因此，<equation>\iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {\frac {\pi}{4}} \mathrm {d} \theta \int_ {0} ^ {2 \sin \theta} f (r \cos \theta , r \sin \theta) r \mathrm {d} r + \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {2 \cos \theta} f (r \cos \theta , r \sin \theta) r \mathrm {d} r.</equation>应选B.

由上述论证可知选项A不正确.

若在直角坐标系下计算，则区域 D 可表示为<equation>D = \left\{(x, y) \mid 1 - \sqrt {1 - x ^ {2}} \leqslant y \leqslant \sqrt {2 x - x ^ {2}}, 0 \leqslant x \leqslant 1 \right\}.</equation>于是，<equation>\iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {1 - \sqrt {1 - x ^ {2}}} ^ {\sqrt {2 x - x ^ {2}}} f (x, y) \mathrm {d} y.</equation>因此，选项C、D均不正确.

---

**2014年第12题 | 填空题 | 4分**

12. 二次积分<equation>\int_{0}^{1}\mathrm{d}y\int_{y}^{1}\left(\frac{\mathrm{e}^{x^{2}}}{x}-\mathrm{e}^{y^{2}}\right)\mathrm{d}x=</equation>___

**解析:**<equation>\begin{aligned} \int_ {0} ^ {1} \mathrm {d} y \int_ {y} ^ {1} \left(\frac {\mathrm {e} ^ {x ^ {2}}}{x} - \mathrm {e} ^ {y ^ {2}}\right) \mathrm {d} x &= \int_ {0} ^ {1} \mathrm {d} y \int_ {y} ^ {1} \frac {\mathrm {e} ^ {x ^ {2}}}{x} \mathrm {d} x - \int_ {0} ^ {1} \mathrm {d} y \int_ {y} ^ {1} \mathrm {e} ^ {y ^ {2}} \mathrm {d} x \\ &= \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {x} \frac {\mathrm {e} ^ {x ^ {2}}}{x} \mathrm {d} y - \int_ {0} ^ {1} (1 - y) \mathrm {e} ^ {y ^ {2}} \mathrm {d} y \\ &= \int_ {0} ^ {1} \mathrm {e} ^ {x ^ {2}} \mathrm {d} x - \int_ {0} ^ {1} \mathrm {e} ^ {y ^ {2}} \mathrm {d} y + \int_ {0} ^ {1} y \mathrm {e} ^ {y ^ {2}} \mathrm {d} y \\ &= \frac {1}{2} \int_ {0} ^ {1} \mathrm {e} ^ {y ^ {2}} \mathrm {d} \left(y ^ {2}\right) = \frac {1}{2} \mathrm {e} ^ {y ^ {2}} \Big | _ {0} ^ {1} = \frac {\mathrm {e} - 1}{2}. \end{aligned}</equation>

---

**2012年第3题 | 选择题 | 4分 | 答案: B**

3. 设函数 f(t) 连续，则二次积分<equation>\int_{0}^{\frac{\pi}{2}} \mathrm{d}\theta \int_{2\cos \theta}^{2} f\left(r^{2}\right) r \mathrm{d} r=</equation>(    )

A.<equation>\int_{0}^{2} \mathrm{d} x \int_{\sqrt{2 x-x^{2}}}^{\sqrt{4-x^{2}}} \sqrt{x^{2}+y^{2}} f\left(x^{2}+y^{2}\right) \mathrm{d} y</equation>B.<equation>\int_{0}^{2} \mathrm{d} x \int_{\sqrt{2 x-x^{2}}}^{\sqrt{4-x^{2}}} f\left(x^{2}+y^{2}\right) \mathrm{d} y</equation>C.<equation>\int_{0}^{2} \mathrm{d} y \int_{1+\sqrt{1-y^{2}}}^{\sqrt{4-y^{2}}} \sqrt{x^{2}+y^{2}} f\left(x^{2}+y^{2}\right) \mathrm{d} x</equation>D.<equation>\int_{0}^{2} \mathrm{d} y \int_{1+\sqrt{1-y^{2}}}^{\sqrt{4-y^{2}}} f\left(x^{2}+y^{2}\right) \mathrm{d} x</equation>

答案: B

**解析:**解 原二次积分对应的二重积分的积分区域为<equation>D=\left\{(r,\theta)\mid 2\cos \theta \leqslant r\leqslant 2,0\leqslant \theta \leqslant \frac{\pi}{2}\right\}</equation>曲线 r=2，r=2cos<equation>\theta</equation>的直角坐标方程分别为<equation>x^{2}+y^{2}=4</equation><equation>x^{2}+y^{2}=2x.</equation>(a)

(b)

由于<equation>0 \leqslant \theta \leqslant \frac{\pi}{2}</equation>，故区域D如图（a）所示. D在直角坐标系下可表示为<equation>D = \left\{(x, y) \mid \sqrt {2 x - x ^ {2}} \leqslant y \leqslant \sqrt {4 - x ^ {2}}, 0 \leqslant x \leqslant 2 \right\}.</equation>将<equation>f(r^{2})</equation>换成<equation>f(x^{2}+y^{2})</equation>，将<equation>r\mathrm{d}r\mathrm{d}\theta</equation>换成<equation>\mathrm{d}x\mathrm{d}y</equation>，得<equation>\int_{0}^{2}\mathrm{d}x\int_{\sqrt{2x-x^{2}}}^{\sqrt{4-x^{2}}}f(x^{2}+y^{2})\mathrm{d}y.</equation>应选B.

下面我们说明选项 A、C、D不正确.

选项A中的积分区域表示与选项B一样，但是被积函数多了一个因子<equation>\sqrt{x^{2}+y^{2}}</equation>注意到，极坐标与直角坐标的相互转化中，<equation>\mathrm{r} \mathrm{d} r \mathrm{d} \theta=\mathrm{d} x \mathrm{d} y</equation>原积分中的<equation>\mathrm{r} \mathrm{d} r \mathrm{d} \theta</equation>转化为<equation>\mathrm{d} x \mathrm{d} y</equation>被积函数变为<equation>f \left(x^{2}+y^{2}\right)</equation>在新积分中，没有因子r.选项A不正确.

被积函数与选项A一样.选项C不正确.

选项D中的积分区域为<equation>D^{\prime}=\{(x,y)\mid 1+\sqrt{1-y^{2}}\leqslant x\leqslant \sqrt{4-y^{2}},0\leqslant y\leqslant 2\}</equation><equation>D^{\prime}</equation>如图（b）所示.选项D不正确.

---


#### 偏导数的概念与计算

**2025年第14题 | 填空题 | 5分**

14. 已知函数<equation>z=z(x,y)</equation>由<equation>z+\ln z-\int_{y}^{x}x\mathrm{e}^{-t^{2}}\mathrm{d}t=1</equation>确定，则<equation>\left.\frac{\partial^{2} z}{\partial x^{2}}\right|_{(1,1)}=</equation>___

**解析:**解 将<equation>x = 1,y = 1</equation>代入方程<equation>z + \ln z - \int_{y}^{x}x\mathrm{e}^{-t^{2}}\mathrm{d}t = 1</equation>可得，<equation>z(1,1) + \ln z(1,1) = 1.</equation>注意到<equation>z = 1</equation>是方程<equation>z + \ln z = 1</equation>的一个解，且<equation>(z + \ln z)^{\prime} = 1 + \frac{1}{z} > 0</equation>，函数<equation>z + \ln z</equation>单调增加，故1是该方程的唯一解，<equation>z(1,1) = 1.</equation>已知方程可写为<equation>z+\ln z-x\int_{y}^{x}\mathrm{e}^{-t^{2}}\mathrm{d} t=1</equation>，对该方程两端关于 x求偏导数可得<equation>\frac {\partial z}{\partial x} + \frac {1}{z} \cdot \frac {\partial z}{\partial x} - \int_ {y} ^ {x} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t - x \cdot \mathrm {e} ^ {- x ^ {2}} = 0.</equation>在(1)式中代入<equation>x = 1,y = 1,z = 1</equation>可得<equation>2\frac{\partial z}{\partial x}\bigg|_{(1,1)} = \mathrm{e}^{-1}</equation>，解得<equation>\frac{\partial z}{\partial x}\bigg|_{(1,1)} = \frac{1}{2\mathrm{e}}.</equation>对（1）式两端关于 x求偏导数可得<equation>\frac {\partial^ {2} z}{\partial x ^ {2}} + \frac {1}{z} \cdot \frac {\partial^ {2} z}{\partial x ^ {2}} - \frac {1}{z ^ {2}} \cdot \left(\frac {\partial z}{\partial x}\right) ^ {2} - \mathrm {e} ^ {- x ^ {2}} - \mathrm {e} ^ {- x ^ {2}} + 2 x ^ {2} \mathrm {e} ^ {- x ^ {2}} = 0.</equation>在（2）式中代入<equation>x=1,y=1,z=1,\frac{\partial z}{\partial x}\bigg|_{(1,1)}=\frac{1}{2\mathrm{e}}</equation>可得<equation>2\frac{\partial^{2}z}{\partial x^{2}}\bigg|_{(1,1)}-\frac{1}{4\mathrm{e}^{2}}-2\mathrm{e}^{-1}+2\mathrm{e}^{-1}=0</equation>解得<equation>\frac{\partial^{2}z}{\partial x^{2}}\bigg|_{(1,1)}=\frac{1}{8\mathrm{e}^{2}}.</equation>

---

**2024年第18题 | 解答题 | 12分**

18. (本题满分12分）设函数<equation>z=z(x,y)</equation>由方程<equation>z+\mathrm{e}^{x}-y\ln(1+z^{2})=0</equation>确定，求<equation>\left.\left(\frac{\partial^{2} z}{\partial x^{2}}+\frac{\partial^{2} z}{\partial y^{2}}\right)\right|_{(0,0)}</equation>

**解析:**解 将 x=0,y=0代入方程<equation>z+{\mathrm{e}}^{x}-y\ln(1+z^{2})=0</equation>可得，<equation>z(0,0)+1=0</equation>即<equation>z(0,0)=-1.</equation>对方程<equation>z+{\mathrm{e}}^{x}-y\ln(1+z^{2})=0</equation>两端同时关于 x求偏导数可得，<equation>\frac {\partial z}{\partial x} + \mathrm {e} ^ {x} - y \cdot \frac {2 z \frac {\partial z}{\partial x}}{1 + z ^ {2}} = 0, \quad \text {即} \frac {\partial z}{\partial x} + \mathrm {e} ^ {x} - \frac {2 y z}{1 + z ^ {2}} \cdot \frac {\partial z}{\partial x} = 0.</equation>将<equation>x = 0,y = 0,z = -1</equation>代人（1）式可得，<equation>\frac{\partial z}{\partial x}\bigg|_{(0,0)} + 1 = 0</equation>，即<equation>\frac{\partial z}{\partial x}\bigg|_{(0,0)} = -1.</equation>对<equation>\frac{\partial z}{\partial x} +\mathrm{e}^{x} -\frac{2yz}{1+z^{2}}\cdot \frac{\partial z}{\partial x} = 0</equation>两端关于<equation>x</equation>求偏导数可得，<equation>\frac {\partial^ {2} z}{\partial x ^ {2}} + \mathrm {e} ^ {x} - 2 y \cdot \frac {1 + z ^ {2} - 2 z ^ {2}}{\left(1 + z ^ {2}\right) ^ {2}} \cdot \left(\frac {\partial z}{\partial x}\right) ^ {2} - \frac {2 y z}{1 + z ^ {2}} \cdot \frac {\partial^ {2} z}{\partial x ^ {2}} = 0.</equation>将<equation>x = 0,y = 0,z = -1,\frac{\partial z}{\partial x}\bigg|_{(0,0)} = -1</equation>代人(2）式可得，<equation>\frac{\partial^2z}{\partial x^2}\bigg|_{(0,0)} + 1 = 0</equation>，即<equation>\frac{\partial^2z}{\partial x^2}\bigg|_{(0,0)} = -1.</equation>对方程<equation>z + \mathrm{e}^{x} - y\ln (1 + z^{2}) = 0</equation>两端同时关于 y求偏导数可得，<equation>\frac {\partial z}{\partial y} - \ln \left(1 + z ^ {2}\right) - y \cdot \frac {2 z \frac {\partial z}{\partial y}}{1 + z ^ {2}} = 0, \quad \text {即} \frac {\partial z}{\partial y} - \ln \left(1 + z ^ {2}\right) - \frac {2 y z}{1 + z ^ {2}} \cdot \frac {\partial z}{\partial y} = 0.</equation>将<equation>x = 0,y = 0,z = -1</equation>代人（3）式可得，<equation>\frac{\partial z}{\partial y}\bigg|_{(0,0)} - \ln 2 = 0</equation>，即<equation>\frac{\partial z}{\partial y}\bigg|_{(0,0)} = \ln 2.</equation>对<equation>\frac{\partial z}{\partial y}-\ln(1+z^{2})-\frac{2yz}{1+z^{2}}\cdot \frac{\partial z}{\partial y}=0</equation>两端关于 y求偏导数可得，<equation>\frac {\partial^ {2} z}{\partial y ^ {2}} - \frac {2 z \frac {\partial z}{\partial y}}{1 + z ^ {2}} - \frac {2 z \frac {\partial z}{\partial y}}{1 + z ^ {2}} - 2 y \cdot \frac {1 + z ^ {2} - 2 z ^ {2}}{\left(1 + z ^ {2}\right) ^ {2}} \cdot \left(\frac {\partial z}{\partial y}\right) ^ {2} - \frac {2 y z}{1 + z ^ {2}} \cdot \frac {\partial^ {2} z}{\partial y ^ {2}} = 0.</equation>将<equation>x = 0,y = 0,z = -1,\frac{\partial z}{\partial y}\bigg|_{(0,0)} = \ln 2</equation>代入(4)式可得，<equation>\frac{\partial^{2}z}{\partial y^{2}}\bigg|_{(0,0)} + 2\ln 2 = 0</equation>，即<equation>\frac{\partial^{2}z}{\partial y^{2}}\bigg|_{(0,0)} = -2\ln 2.</equation>因此，<equation>\left(\frac{\partial^{2}z}{\partial x^{2}} + \frac{\partial^{2}z}{\partial y^{2}}\right)\bigg|_{(0,0)} = -1 - 2\ln 2.</equation>

---

**2023年第1题 | 选择题 | 5分 | 答案: A**

1. 已知函数<equation>f ( x,y)=\ln ( y+| x \sin y | )</equation>，则（    ）

A.<equation>\left. \frac{\partial f}{\partial x}\right|_{(0,1)}</equation>不存在，<equation>\left. \frac{\partial f}{\partial y}\right|_{(0,1)}</equation>存在

B.<equation>\left. \frac{\partial f}{\partial x}\right|_{(0,1)}</equation>存在，<equation>\left. \frac{\partial f}{\partial y}\right|_{(0,1)}</equation>不存在

C.<equation>\left. \frac{\partial f}{\partial x}\right|_{(0,1)},\left. \frac{\partial f}{\partial y}\right|_{(0,1)}</equation>均存在

D.<equation>\left. \frac{\partial f}{\partial x}\right|_{(0,1)},\left. \frac{\partial f}{\partial y}\right|_{(0,1)}</equation>均不存在

答案: A

**解析:**由<equation>f ( x,y )</equation>的表达式可知，<equation>f ( 0,1 )=0.</equation>根据偏导数的定义，<equation>\left. \frac {\partial f}{\partial x} \right| _ {(0, 1)} = \lim _ {x \rightarrow 0} \frac {f (x , 1) - f (0 , 1)}{x - 0} = \lim _ {x \rightarrow 0} \frac {\ln (1 + | x \sin 1 |)}{x} = \lim _ {x \rightarrow 0} \frac {| x | \sin 1}{x}.</equation>由于<equation>\lim_{x\to 0^{-}}\frac{|x|}{x} = -1,</equation><equation>\lim_{x\to 0^{+}}\frac{|x|}{x} = 1,</equation>故<equation>\lim_{x\to 0}\frac{|x|}{x}</equation>不存在，从而<equation>\left.\frac{\partial f}{\partial x}\right|_{(0,1)}</equation>不存在.<equation>\left. \frac {\partial f}{\partial y} \right| _ {(0, 1)} = \lim _ {y \rightarrow 1} \frac {f (0 , y) - f (0 , 1)}{y - 1} = \lim _ {y \rightarrow 1} \frac {\ln y}{y - 1} = \lim _ {y \rightarrow 1} \frac {\ln (1 + y - 1)}{y - 1} = \lim _ {y \rightarrow 1} \frac {y - 1}{y - 1} = 1.</equation>因此，<equation>\frac{\partial f}{\partial y}\bigg|_{(0,1)}=1.</equation>综上所述，<equation>\frac{\partial f}{\partial x}\bigg|_{(0,1)}</equation>不存在，<equation>\frac{\partial f}{\partial y}\bigg|_{(0,1)}</equation>存在，应选A.

---

**2022年第3题 | 选择题 | 5分 | 答案: C**

3. 已知 f(t) 连续，令<equation>F ( x,y)=\int_{0}^{x-y} ( x-y-t ) f ( t ) \mathrm{d} t</equation>，则（    ）<equation>\begin{aligned} \mathrm {A}. \frac {\partial F}{\partial x} &= \frac {\partial F}{\partial y}, \frac {\partial^ {2} F}{\partial x ^ {2}} = \frac {\partial^ {2} F}{\partial y ^ {2}} \\ \mathrm {C}. \frac {\partial F}{\partial x} &= - \frac {\partial F}{\partial y}, \frac {\partial^ {2} F}{\partial x ^ {2}} = \frac {\partial^ {2} F}{\partial y ^ {2}} \end{aligned}</equation><equation>\begin{aligned} B. \frac {\partial F}{\partial x} &= \frac {\partial F}{\partial y}, \frac {\partial^ {2} F}{\partial x ^ {2}} = - \frac {\partial^ {2} F}{\partial y ^ {2}} \\ D. \frac {\partial F}{\partial x} &= - \frac {\partial F}{\partial y}, \frac {\partial^ {2} F}{\partial x ^ {2}} = - \frac {\partial^ {2} F}{\partial y ^ {2}} \end{aligned}</equation>

答案: C

**解析:**解 整理 F(x,y）的表达式.<equation>F (x, y) = \int_ {0} ^ {x - y} (x - y - t) f (t) \mathrm {d} t = (x - y) \int_ {0} ^ {x - y} f (t) \mathrm {d} t - \int_ {0} ^ {x - y} t f (t) \mathrm {d} t.</equation>分别计算<equation>\frac{\partial F}{\partial x},\frac{\partial^{2} F}{\partial x^{2}},\frac{\partial F}{\partial y},\frac{\partial^{2} F}{\partial y^{2}}.</equation><equation>\frac {\partial F}{\partial x} = (x - y) f (x - y) + \int_ {0} ^ {x - y} f (t) \mathrm {d} t - (x - y) f (x - y) = \int_ {0} ^ {x - y} f (t) \mathrm {d} t,</equation><equation>\frac {\partial^ {2} F}{\partial x ^ {2}} = \frac {\partial \left[ \int_ {0} ^ {x - y} f (t) \mathrm {d} t \right]}{\partial x} = f (x - y),</equation><equation>\frac {\partial F}{\partial y} = - (x - y) f (x - y) - \int_ {0} ^ {x - y} f (t) \mathrm {d} t + (x - y) f (x - y) = - \int_ {0} ^ {x - y} f (t) \mathrm {d} t,</equation><equation>\frac {\partial^ {2} F}{\partial y ^ {2}} = \frac {\partial \left[ - \int_ {0} ^ {x - y} f (t) \mathrm {d} t \right]}{\partial y} = f (x - y).</equation>因此，<equation>\frac{\partial F}{\partial x}=-\frac{\partial F}{\partial y},\frac{\partial^{2}F}{\partial x^{2}}=\frac{\partial^{2}F}{\partial y^{2}}.</equation>应选C.

---

**2019年第16题 | 解答题 | 10分**

16. (本题满分10分）

设函数 f(u,v)具有2阶连续偏导数，函数 g(x,y) = xy-f(x+y,x-y).求<equation>\frac{\partial^{2} g}{\partial x^{2}}+\frac{\partial^{2} g}{\partial x \partial y}+\frac{\partial^{2} g}{\partial y^{2}}.</equation>

**答案:**<equation>1 - 3 f_{11}^{\prime \prime} ( x + y, x - y ) - f_{22}^{\prime \prime} ( x + y, x - y ).</equation>

**解析:**<equation>\begin{aligned} \frac {\partial g}{\partial x} &= y - f _ {1} ^ {\prime} (x + y, x - y) - f _ {2} ^ {\prime} (x + y, x - y), \\ \frac {\partial g}{\partial y} &= x - f _ {1} ^ {\prime} (x + y, x - y) + f _ {2} ^ {\prime} (x + y, x - y), \\ \frac {\partial^ {2} g}{\partial x ^ {2}} &= - f _ {1 1} ^ {\prime \prime} (x + y, x - y) - f _ {1 2} ^ {\prime \prime} (x + y, x - y) - f _ {2 1} ^ {\prime \prime} (x + y, x - y) - f _ {2 2} ^ {\prime \prime} (x + y, x - y) \\ \frac {f (u , v) \mathrm {具 有} 2 \mathrm {阶 连 续 偏 导 数}}{} - f _ {1 1} ^ {\prime \prime} (x + y, x - y) - 2 f _ {1 2} ^ {\prime \prime} (x + y, x - y) - f _ {2 2} ^ {\prime \prime} (x + y, x - y), \\ \frac {\partial^ {2} g}{\partial x \partial y} &= 1 - f _ {1 1} ^ {\prime \prime} (x + y, x - y) + f _ {1 2} ^ {\prime \prime} (x + y, x - y) - f _ {2 1} ^ {\prime \prime} (x + y, x - y) + f _ {2 2} ^ {\prime \prime} (x + y, x - y) \\ \frac {f (u , v) \mathrm {具 有} 2 \mathrm {阶 连 续 偏 导 数}}{} 1 - f _ {1 1} ^ {\prime \prime} (x + y, x - y) + f _ {2 2} ^ {\prime \prime} (x + y, x - y), \\ \frac {\partial^ {2} g}{\partial y ^ {2}} &= - f _ {1 1} ^ {\prime \prime} (x + y, x - y) + f _ {1 2} ^ {\prime \prime} (x + y, x - y) + f _ {2 1} ^ {\prime \prime} (x + y, x - y) - f _ {2 2} ^ {\prime \prime} (x + y, x - y) \\ \frac {f (u , v) \mathrm {具 有} 2 \mathrm {阶 连 续 偏 导 数}}{} - f _ {1 1} ^ {\prime \prime} (x + y, x - y) + 2 f _ {1 2} ^ {\prime \prime} (x + y, x - y) - f _ {2 2} ^ {\prime \prime} (x + y, x - y). \\ \mathrm {代 入} \frac {\partial^ {2} g}{\partial x ^ {2}} + \frac {\partial^ {2} g}{\partial x \partial y} + \frac {\partial^ {2} g}{\partial y ^ {2}} \mathrm {可 得}, \\ \frac {\partial^ {2} g}{\partial x} \frac {\partial^ {2} g}{\partial y} \frac {\partial^ {2} g}{\partial y ^ {2}} \end{aligned}</equation><equation>\frac {\partial^ {2} g}{\partial x ^ {2}} + \frac {\partial^ {2} g}{\partial x \partial y} + \frac {\partial^ {2} g}{\partial y ^ {2}} = 1 - 3 f _ {1 1} ^ {\prime \prime} (x + y, x - y) - f _ {2 2} ^ {\prime \prime} (x + y, x - y).</equation>

---

**2016年第2题 | 选择题 | 4分 | 答案: D**

2. 已知函数<equation>f(x,y)=\frac{\mathrm{e}^{x}}{x-y}</equation>，则（    ）

A.<equation>f_{x}^{\prime}-f_{y}^{\prime}=0</equation>B.<equation>f_{x}^{\prime}+f_{y}^{\prime}=0</equation>C.<equation>f_{x}^{\prime}-f_{y}^{\prime}=f</equation>D.<equation>f_{x}^{\prime}+f_{y}^{\prime}=f</equation>

答案: D

**解析:**分别计算<equation>f_{x}^{\prime}, f_{y}^{\prime}</equation>得

因此，<equation>f _ {x} ^ {\prime} = \frac {\mathrm {e} ^ {x} (x - y) - \mathrm {e} ^ {x}}{(x - y) ^ {2}}, \quad f _ {y} ^ {\prime} = \frac {\mathrm {e} ^ {x}}{(x - y) ^ {2}}.</equation><equation>f _ {x} ^ {\prime} + f _ {y} ^ {\prime} = \frac {\mathrm {e} ^ {x} (x - y)}{(x - y) ^ {2}} = \frac {\mathrm {e} ^ {x}}{x - y} = f.</equation>应选 D.

---

**2013年第10题 | 填空题 | 4分**

10. 设函数<equation>z=z(x,y)</equation>由方程<equation>( z+y )^{x}= x y</equation>确定，则<equation>\left. \frac{\partial z}{\partial x} \right|_{(1,2)}=</equation>___

**答案:**# 2(1-ln2).

**解析:**解 将方程<equation>( z+y)^{x}=xy</equation>化为<equation>\mathrm{e}^{x\ln(z+y)}=xy</equation>，对所得方程两端关于 x求偏导数，可得<equation>\mathrm {e} ^ {x \ln (z + y)} \left[ \ln (z + y) + \frac {x \cdot \frac {\partial z}{\partial x}}{z + y} \right] = y.</equation>当 x=1，y=2时，由原方程可知 z=0，从而由上式可得<equation>\mathrm{e}^{\ln 2}\left(\ln 2+\frac{\frac{\partial z}{\partial x}\bigg|_{(1,2)}}{2}\right)=2</equation>即<equation>\left.\frac{\partial z}{\partial x}\right|_{(1,2)}= 2(1-\ln 2).</equation>

---

**2011年第16题 | 解答题 | 10分**

16. (本题满分10分）

已知函数 f(u,v)具有二阶连续偏导数，<equation>f(1,1)=2</equation>是 f(u,v)的极值，<equation>z=f(x+y,f(x,y))</equation>.求<equation>\left.\frac{\partial^{2} z}{\partial x \partial y}\right|_{(1,1)}.</equation>

**答案:**<equation>= f_{11}^{\prime \prime}(2,2) + f_{2}^{\prime}(2,2)f_{12}^{\prime \prime}(1,1).</equation>

**解析:**对<equation>z = f(x + y,f(x,y))</equation>两端关于<equation>x</equation>求偏导数得<equation>\frac {\partial z}{\partial x} = f _ {1} ^ {\prime} (x + y, f (x, y)) + f _ {2} ^ {\prime} (x + y, f (x, y)) \cdot f _ {1} ^ {\prime} (x, y).</equation>继续对上式两端关于 y求偏导数得<equation>\begin{array}{l} \frac {\partial^ {2} z}{\partial x \partial y} = f _ {1 1} ^ {\prime \prime} (x + y, f (x, y)) + f _ {1 2} ^ {\prime \prime} (x + y, f (x, y)) f _ {2} ^ {\prime} (x, y) \\ + \left[ f _ {2 1} ^ {\prime \prime} (x + y, f (x, y)) + f _ {2 2} ^ {\prime \prime} (x + y, f (x, y)) f _ {2} ^ {\prime} (x, y) \right] f _ {1} ^ {\prime} (x, y) \\ + f _ {2} ^ {\prime} (x + y, f (x, y)) f _ {1 2} ^ {\prime \prime} (x, y). \\ \end{array}</equation>由极值的必要条件可知<equation>f_1^{\prime}(1,1) = f_2^{\prime}(1,1) = 0.</equation>将<equation>f(1,1) = 2,f_1^{\prime}(1,1) = f_2^{\prime}(1,1) = 0</equation>代入上式可得<equation>\left. \frac {\partial^ {2} z}{\partial x \partial y} \right| _ {(1, 1)} = f _ {1 1} ^ {\prime \prime} (2, 2) + f _ {2} ^ {\prime} (2, 2) f _ {1 2} ^ {\prime \prime} (1, 1).</equation>

---

**2009年第10题 | 填空题 | 4分**

10. 设<equation>z=(x+\mathrm{e}^{y})^{x}</equation>，则<equation>\left.\frac{\partial z}{\partial x}\right|_{(1,0)}=</equation>___

**答案:**## 2ln2+1.

**解析:**（法一）在点（1，0）附近，<equation>x > 0</equation>，从而<equation>x+\mathrm{e}^{y}>0, z>0.</equation>对<equation>z=(x+\mathrm{e}^{y})^{x}</equation>两端取对数得到<equation>\ln z = x \ln \left(x + \mathrm {e} ^ {y}\right).</equation>对上式两端关于 x求导得，<equation>\frac {1}{z} \cdot \frac {\partial z}{\partial x} = \ln \left(x + \mathrm {e} ^ {y}\right) + \frac {x}{x + \mathrm {e} ^ {y}}.</equation>当<equation>x = 1</equation>，<equation>y = 0</equation>时，<equation>z = 2.</equation>因此，<equation>\frac{\partial z}{\partial x}\bigg|_{(1,0)} = 2\left(\ln 2 + \frac{1}{2}\right) = 2\ln 2 + 1.</equation>（法二）将<equation>y = 0</equation>代入<equation>z = (x + \mathrm{e}^{y})^{x}</equation>中得到<equation>z(x,0) = (x + 1)^{x}</equation>.于是，<equation>\left. \frac {\partial z}{\partial x} \right| _ {(1, 0)} = \frac {\mathrm {d} \left[ (x + 1) ^ {x} \right]}{\mathrm {d} x} \Bigg | _ {x = 1} = \left[ \mathrm {e} ^ {x \ln (x + 1)} \right] ^ {\prime} \Bigg | _ {x = 1} = \mathrm {e} ^ {x \ln (x + 1)} \left[ \ln (x + 1) + \frac {x}{x + 1} \right] \Bigg | _ {x = 1} = 2 \ln 2 + 1.</equation>

---


#### 二重积分的计算

**2025年第19题 | 解答题 | 12分**

19. 已知平面有界区域<equation>D=\{(x,y)\mid y^{2}\leqslant x,x^{2}\leqslant y\}</equation>，计算二重积分<equation>\iint_{D}(x-y+1)^{2}\mathrm{d}x\mathrm{d}y.</equation>

**解析:**分析 本题主要考查二重积分的计算.

区域 D由两条抛物线围成，且关于直线 y=x对称，故可以考虑使用轮换对称性.

解如图所示，区域D由曲线<equation>y=x^{2}</equation>与<equation>x=y^{2}</equation>围成.由于区域D位于第一象限，故<equation>x=y^{2}</equation>可写成<equation>y=\sqrt{x}.</equation>注意到区域 D关于直线 y=x对称.记<equation>D_{1}</equation>为区域 D位于直线 y=x下方的部分，则由轮换对称性的结论可得<equation>\begin{aligned} \iint_ {D} (x - y + 1) ^ {2} \mathrm {d} x \mathrm {d} y &= \iint_ {D _ {1}} (x - y + 1) ^ {2} \mathrm {d} x \mathrm {d} y + \iint_ {D \backslash D _ {1}} (x - y + 1) ^ {2} \mathrm {d} x \mathrm {d} y \\ &= \iint_ {D _ {1}} \left[ (x - y + 1) ^ {2} + (y - x + 1) ^ {2} \right] \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} \left[ (x - y) ^ {2} + 1 \right] \mathrm {d} x \mathrm {d} y. \end{aligned}</equation>将<equation>D_{1}</equation>写成X型区域.<equation>D _ {1} = \left\{(x, y) \mid x ^ {2} \leqslant y \leqslant x, 0 \leqslant x \leqslant 1 \right\}.</equation>分别计算<equation>\iint_{D_1}\mathrm{d}x\mathrm{d}y,\iint_{D_1}(x - y)^2\mathrm{d}x\mathrm{d}y.</equation><equation>\iint_ {D _ {1}} \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {x ^ {2}} ^ {x} \mathrm {d} y = \int_ {0} ^ {1} \left(x - x ^ {2}\right) \mathrm {d} x = \left(\frac {x ^ {2}}{2} - \frac {x ^ {3}}{3}\right) \Bigg | _ {0} ^ {1} = \frac {1}{2} - \frac {1}{3} = \frac {1}{6}.</equation><equation>\begin{aligned} \iint_ {D _ {1}} (x - y) ^ {2} \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {1} \mathrm {d} x \int_ {x ^ {2}} ^ {x} (x - y) ^ {2} \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {x ^ {2}} ^ {x} \left(x ^ {2} - 2 x y + y ^ {2}\right) \mathrm {d} y \\ &= \int_ {0} ^ {1} \left(x ^ {2} y - x y ^ {2} + \frac {y ^ {3}}{3}\right) \Big | _ {x ^ {2}} ^ {x} \mathrm {d} x = \int_ {0} ^ {1} \left(\frac {x ^ {3}}{3} - x ^ {4} + x ^ {5} - \frac {x ^ {6}}{3}\right) \mathrm {d} x \\ &= \left. \left(- \frac {x ^ {7}}{2 1} + \frac {x ^ {6}}{6} - \frac {x ^ {5}}{5} + \frac {x ^ {4}}{1 2}\right) \right| _ {0} ^ {1} = - \frac {1}{2 1} + \frac {1}{6} - \frac {1}{5} + \frac {1}{1 2} = \frac {1}{4 2 0}. \end{aligned}</equation>因此，<equation>\iint_ {D} (x - y + 1) ^ {2} \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} \left[ (x - y) ^ {2} + 1 \right] \mathrm {d} x \mathrm {d} y = 2 \left(\frac {1}{4 2 0} + \frac {1}{6}\right) = \frac {7 1}{2 1 0}.</equation>

---

**2024年第17题 | 解答题 | 10分**

17. (本题满分10分）设平面有界区域 D位于第一象限，由曲线<equation>x y=\frac{1}{3},</equation><equation>x y=3</equation>与直线<equation>y=\frac{1}{3} x</equation><equation>y=3 x</equation>所围成，请计算<equation>\iint_{D}(1+x-y) \mathrm{d} x \mathrm{d} y.</equation>

**答案:**##<equation>\frac{8}{3}\ln 3.</equation>

**解析:**解区域 D如图（a）所示，注意到区域 D的四条边界曲线中，交换曲线<equation>xy=\frac{1}{3}</equation>与<equation>xy=3</equation>中x， y的位置，可得<equation>yx=\frac{1}{3}</equation>与<equation>yx=3</equation>，即曲线方程不变，故这两条曲线均关于直线 y=x对称，而直线<equation>y=\frac{1}{3} x</equation>与直线 y=3x关于直线 y=x对称，故这四条曲线所围成的区域 D也关于直线 y=x对称，从而对变量 x，y具有轮换对称性.

(a)

(b)

由轮换对称性的结论（2）可得<equation>\iint_{D}x\mathrm{d}x\mathrm{d}y=\iint_{D}y\mathrm{d}x\mathrm{d}y</equation>，故<equation>\iint_ {D} (1 + x - y) \mathrm {d} x \mathrm {d} y = \iint_ {D} \mathrm {d} x \mathrm {d} y + \iint_ {D} x \mathrm {d} x \mathrm {d} y - \iint_ {D} y \mathrm {d} x \mathrm {d} y = \iint_ {D} \mathrm {d} x \mathrm {d} y.</equation>下面用两种方法计算<equation>\iint_{D}\mathrm{d}x\mathrm{d}y.</equation>（法一）在极坐标系下计算.

曲线<equation>xy = \frac{1}{3}</equation>的极坐标方程为<equation>r^2\cos \theta \sin \theta = \frac{1}{3}</equation>，整理可得<equation>r = \sqrt{\frac{2}{3\sin 2\theta}}</equation>，曲线<equation>xy = 3</equation>的极坐标方程为<equation>r^2\cos \theta \sin \theta = 3</equation>，整理可得<equation>r = \sqrt{\frac{6}{\sin 2\theta}}</equation>直线<equation>y = \frac{1}{3} x</equation>的极坐标方程为<equation>\theta = \arctan \frac{1}{3},y = 3x</equation>的极坐标方程为<equation>\theta = \arctan 3.</equation>区域 D的极坐标表示为<equation>D = \left\{(r, \theta) \mid \sqrt {\frac {2}{3 \sin 2 \theta}} \leqslant r \leqslant \sqrt {\frac {6}{\sin 2 \theta}}, \arctan \frac {1}{3} \leqslant \theta \leqslant \arctan 3 \right\}.</equation>于是，<equation>\begin{aligned} \iint_ {D} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} \mathrm {d} \theta \int_ {\sqrt {\frac {2}{3 \sin 2 \theta}}} ^ {\sqrt {\frac {6}{\sin 2 \theta}}} r \mathrm {d} r &= \frac {1}{2} \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} r ^ {2} \left|  \sqrt {\frac {6}{\sin 2 \theta}} \\ \sqrt {\frac {2}{3 \sin 2 \theta}}  \right) \mathrm {d} \theta \\ &= \frac {8}{3} \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} \csc 2 \theta \mathrm {d} \theta = \frac {4}{3} \ln | \csc 2 \theta - \cot 2 \theta | \left| _ {\arctan \frac {1}{3}} ^ {\arctan 3}. \right. \end{aligned}</equation>由于<equation>\csc 2\theta -\cot 2\theta = \frac{1 - \cos 2\theta}{\sin 2\theta} = \frac{2\sin^2\theta}{2\sin \theta \cos \theta} = \tan \theta</equation>，故<equation>\iint_{D}\mathrm{d}x\mathrm{d}y = \frac{4}{3}\ln |\tan \theta |\Bigg|_{\arctan \frac{1}{3}}^{ \arctan 3}</equation>当<equation>\theta = \arctan \frac{1}{3}</equation>时，<equation>\tan \theta = \frac{1}{3}</equation>，当<equation>\theta = \arctan 3</equation>时，<equation>\tan \theta = 3.</equation>因此，<equation>\iint_ {D} \mathrm {d} x \mathrm {d} y = \frac {4}{3} \left(\ln 3 - \ln \frac {1}{3}\right) = \frac {8}{3} \ln 3.</equation>（法二）在直角坐标系下计算.

联立<equation>\left\{\begin{array}{l l} x y=\frac{1}{3}, \\ y=\frac{1}{3} x, \end{array} \right.</equation>解得<equation>\left\{\begin{array}{l l} x=1, \\ y=\frac{1}{3}. \end{array} \right.</equation>联立<equation>\left\{\begin{array}{l l} x y=\frac{1}{3}, \\ y=3 x, \end{array} \right.</equation>解得<equation>\left\{\begin{array}{l l} x=\frac{1}{3}, \\ y=1. \end{array} \right.</equation>联立<equation>\left\{\begin{array}{l l} x y=3, \\ y=\frac{1}{3} x, \end{array} \right.</equation>解得<equation>\left\{\begin{array}{l l} x=3, \\ y=1. \end{array} \right.</equation>联立<equation>\left\{\begin{array}{l l} x y=3, \\ y=3 x, \end{array} \right.</equation>解得<equation>\left\{\begin{array}{l l} x=1, \\ y=3. \end{array} \right.</equation>如图（b）所示，直线<equation>x=1</equation>将区域D分为两部分<equation>D_{1}, D_{2}.</equation><equation>D_{1}</equation>由曲线<equation>xy=\frac{1}{3}</equation>，直线<equation>y=3x</equation>与<equation>x= 1</equation>围成，<equation>D_{2}</equation>由曲线<equation>xy=3</equation>，直线<equation>y=\frac{1}{3} x</equation>与<equation>x=1</equation>围成，<equation>\iint_{D}\mathrm{d}x\mathrm{d}y</equation>等于D的面积，即<equation>D_{1}</equation>的面积与<equation>D_{2}</equation>的面积之和.

因此，<equation>\begin{aligned} \iint_ {D} \mathrm {d} x \mathrm {d} y &= \int_ {\frac {1}{3}} ^ {1} \left(3 x - \frac {1}{3 x}\right) \mathrm {d} x + \int_ {1} ^ {3} \left(\frac {3}{x} - \frac {x}{3}\right) \mathrm {d} x = \left(\frac {3 x ^ {2}}{2} - \frac {1}{3} \ln x\right) \Bigg | _ {\frac {1}{3}} ^ {1} + \left(3 \ln x - \frac {x ^ {2}}{6}\right) \Bigg | _ {1} ^ {3} \\ &= \frac {3}{2} - \frac {1}{6} + \frac {1}{3} \ln \frac {1}{3} + 3 \ln 3 - \frac {3}{2} + \frac {1}{6} = - \frac {1}{3} \ln 3 + 3 \ln 3 = \frac {8}{3} \ln 3. \end{aligned}</equation>

---

**2023年第19题 | 解答题 | 12分**

19. (本题满分12分)

已知平面区域<equation>D=\{(x,y)\mid(x-1)^{2}+y^{2}\leqslant1\}</equation>，计算二重积分<equation>\iint_{D}|\sqrt{x^{2}+y^{2}}-1|\mathrm{d}x\mathrm{d}y.</equation>

**答案:**<equation>- \frac {3 2}{9} - \frac {\pi}{9} + 3 \sqrt {3}.</equation>

**解析:**解注意到<equation>\mid \sqrt{x^{2}+y^{2}}-1\mid</equation>为关于 y的偶函数，而积分区域 D关于 x轴对称，记 D位于上半平面的部分为<equation>D_{1}</equation>即图（b）中的蓝色部分与灰色部分，则<equation>\iint_ {D} \left| \sqrt {x ^ {2} + y ^ {2}} - 1 \right| \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} \left| \sqrt {x ^ {2} + y ^ {2}} - 1 \right| \mathrm {d} x \mathrm {d} y.</equation>在区域<equation>x^{2}+y^{2}\leqslant 1</equation>内，<equation>|\sqrt{x^{2}+y^{2}}-1|=1-\sqrt{x^{2}+y^{2}}</equation>在区域<equation>x^{2}+y^{2}\leqslant 1</equation>外，<equation>|\sqrt{x^{2}+y^{2}}-1|=</equation><equation>\sqrt{x^{2}+y^{2}}-1.</equation>记<equation>x^{2}+y^{2}\leqslant 1</equation>与<equation>D_{1}</equation>的公共部分为<equation>D_{2}</equation>即图（b）中的蓝色部分，则<equation>\begin{aligned} \iint_ {D _ {1}} \left| \sqrt {x ^ {2} + y ^ {2}} - 1 \right| \mathrm {d} x \mathrm {d} y &= \iint_ {D _ {1} \backslash D _ {2}} \left(\sqrt {x ^ {2} + y ^ {2}} - 1\right) \mathrm {d} x \mathrm {d} y + \iint_ {D _ {2}} \left(1 - \sqrt {x ^ {2} + y ^ {2}}\right) \mathrm {d} x \mathrm {d} y \\ &= \iint_ {D _ {1}} \left(\sqrt {x ^ {2} + y ^ {2}} - 1\right) \mathrm {d} x \mathrm {d} y - 2 \iint_ {D _ {2}} \left(\sqrt {x ^ {2} + y ^ {2}} - 1\right) \mathrm {d} x \mathrm {d} y. \end{aligned}</equation>下面分别计算<equation>\iint_{D_{1}}(\sqrt{x^{2}+y^{2}}-1)\mathrm{d}x\mathrm{d}y, \iint_{D_{2}}(\sqrt{x^{2}+y^{2}}-1)\mathrm{d}x\mathrm{d}y.</equation>圆周<equation>( x-1 )^{2}+y^{2}=1</equation>的极坐标方程为<equation>r=2\cos \theta</equation>，故<equation>D_{1}</equation>在极坐标系下的表示为<equation>D _ {1} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2 \cos \theta , 0 \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation>于是，<equation>\begin{aligned} \iint_ {D _ {1}} \left(\sqrt {x ^ {2} + y ^ {2}} - 1\right) \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \int_ {0} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {2 \cos \theta} (r - 1) \cdot r \mathrm {d} r &= \int_ {0} ^ {\frac {\pi}{2}} \left(\frac {r ^ {3}}{3} - \frac {r ^ {2}}{2}\right) \Bigg | _ {0} ^ {2 \cos \theta} \mathrm {d} \theta \\ &= \int_ {0} ^ {\frac {\pi}{2}} \left(\frac {8}{3} \cos^ {3} \theta - 2 \cos^ {2} \theta\right) \mathrm {d} \theta = \frac {8}{3} \int_ {0} ^ {\frac {\pi}{2}} \cos^ {3} \theta \mathrm {d} \theta - 2 \int_ {0} ^ {\frac {\pi}{2}} \cos^ {2} \theta \mathrm {d} \theta \\ &= \frac {8}{3} \cdot \frac {2}{3} - 2 \cdot \frac {\pi}{4} = \frac {1 6}{9} - \frac {\pi}{2}. \end{aligned}</equation>联立<equation>\left\{\begin{array}{l l}x^{2}+y^{2}=1,\\ (x-1)^{2}+y^{2}=1,\end{array}\right.</equation>解得<equation>\left\{\begin{array}{l l}x=\frac{1}{2},\\ y=\pm \frac{\sqrt{3}}{2},\end{array}\right.</equation>从而圆周<equation>x^{2}+y^{2}=1</equation>与圆周<equation>(x-1)^{2}+y^{2}=1</equation>在上半平面的交点为<equation>\left(\frac{1}{2},\frac{\sqrt{3}}{2}\right).</equation>连接原点O与点<equation>\left(\frac{1}{2},\frac{\sqrt{3}}{2}\right)</equation>的直线方程为<equation>y=\sqrt{3} x</equation>其极坐标方程为<equation>\theta=\frac{\pi}{3}.</equation>如图（c）所示，<equation>D_{2}</equation>可以由直线<equation>\theta=\frac{\pi}{3}</equation>分为两部分，在极坐标系下的表示为<equation>D _ {2} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 1, 0 \leqslant \theta \leqslant \frac {\pi}{3} \right\} \cup \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2 \cos \theta , \frac {\pi}{3} \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation>于是，<equation>\iint_ {D _ {2}} \left(\sqrt {x ^ {2} + y ^ {2}} - 1\right) \mathrm {d} x \mathrm {d} y \xlongequal {\text {极 坐 标}} \int_ {0} ^ {\frac {\pi}{3}} \mathrm {d} \theta \int_ {0} ^ {1} (r - 1) \cdot r \mathrm {d} r + \int_ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {2 \cos \theta} (r - 1) \cdot r \mathrm {d} r.</equation>其中，<equation>\int_ {0} ^ {\frac {\pi}{3}} \mathrm {d} \theta \int_ {0} ^ {1} (r - 1) \cdot r \mathrm {d} r = \int_ {0} ^ {\frac {\pi}{3}} \left(\frac {r ^ {3}}{3} - \frac {r ^ {2}}{2}\right) \Big | _ {0} ^ {1} \mathrm {d} \theta = \int_ {0} ^ {\frac {\pi}{3}} \left(\frac {1}{3} - \frac {1}{2}\right) \mathrm {d} \theta = - \frac {1}{6} \cdot \frac {\pi}{3} = - \frac {\pi}{1 8}.</equation><equation>\begin{aligned} \int_ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {2 \cos \theta} (r - 1) \cdot r \mathrm {d} r &= \int_ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \left(\frac {8}{3} \cos^ {3} \theta - 2 \cos^ {2} \theta\right) \mathrm {d} \theta = \frac {8}{3} \int_ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \cos^ {3} \theta \mathrm {d} \theta - 2 \int_ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \cos^ {2} \theta \mathrm {d} \theta \\ &= \frac {8}{3} \int_ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \left(1 - \sin^ {2} \theta\right) \mathrm {d} (\sin \theta) - \int_ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \left(1 + \cos 2 \theta\right) \mathrm {d} \theta \\ &= \frac {8}{3} \left(\sin \theta - \frac {\sin^ {3} \theta}{3}\right) \left| _ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} - \frac {\pi}{6} - \frac {\sin 2 \theta}{2} \right| _ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \\ &= - \frac {\pi}{6} + \frac {8}{3} \left(\frac {2}{3} - \frac {3 \sqrt {3}}{8}\right) + \frac {\sqrt {3}}{4} = - \frac {\pi}{6} + \frac {1 6}{9} - \frac {3 \sqrt {3}}{4}. \end{aligned}</equation>因此，<equation>\iint_ {D _ {2}} \left(\sqrt {x ^ {2} + y ^ {2}} - 1\right) \mathrm {d} x \mathrm {d} y = - \frac {\pi}{1 8} - \frac {\pi}{6} + \frac {1 6}{9} - \frac {3 \sqrt {3}}{4} = - \frac {2 \pi}{9} + \frac {1 6}{9} - \frac {3 \sqrt {3}}{4}.</equation>综上所述，<equation>\iint_ {D} \left| \sqrt {x ^ {2} + y ^ {2}} - 1 \right| \mathrm {d} x \mathrm {d} y = 2 \left(\frac {1 6}{9} - \frac {\pi}{2} + \frac {4 \pi}{9} - \frac {3 2}{9} + \frac {3 \sqrt {3}}{2}\right) = - \frac {3 2}{9} - \frac {\pi}{9} + 3 \sqrt {3}.</equation>

---

**2022年第14题 | 填空题 | 5分**

14. 已知函数 f(x)<equation>\left\{\begin{array}{l l} {\mathrm{e}^{x},}&{0 \leqslant x \leqslant 1,}\\ {0,}&{\mathrm{其他},}\end{array} \right.</equation>则<equation>\int_{-\infty}^{+\infty}\mathrm{d}x\int_{-\infty}^{+\infty}f(x)f(y-x)\mathrm{d}y=</equation>___.

**解析:**解 根据 f(x)的定义，f(x)仅在 0≤x≤1时非零，f(y-x)仅在 0≤y-x≤1时非零.于是，f(x)f(y-x)仅在区域 D = {（x,y）|0≤y-x≤1,0≤x≤1}，即 D = {（x,y）|x≤y≤x+1,0≤x≤1}上非零.<equation>\begin{aligned} \int_ {- \infty} ^ {+ \infty} \mathrm {d} x \int_ {- \infty} ^ {+ \infty} f (x) f (y - x) \mathrm {d} y &= \int_ {0} ^ {1} \mathrm {d} x \int_ {x} ^ {x + 1} \mathrm {e} ^ {x} \mathrm {e} ^ {y - x} \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {x} ^ {x + 1} \mathrm {e} ^ {y} \mathrm {d} y \\ &= \int_ {0} ^ {1} \left(\mathrm {e} ^ {x + 1} - \mathrm {e} ^ {x}\right) \mathrm {d} x = \left(\mathrm {e} ^ {x + 1} - \mathrm {e} ^ {x}\right) \Bigg | _ {0} ^ {1} \\ &= \left(\mathrm {e} ^ {2} - \mathrm {e}\right) - (\mathrm {e} - 1) = \mathrm {e} ^ {2} - 2 \mathrm {e} + 1. \end{aligned}</equation>

---

**2022年第19题 | 解答题 | 12分**

19. (本题满分12分）

已知平面区域 D = {（x,y）| y-2≤x≤<equation>\sqrt{4-y^{2}}</equation>, 0≤y≤2} ，计算 I =<equation>\iint_{D} \frac{(x-y)^{2}}{x^{2}+y^{2}} \mathrm{d} x \mathrm{d} y.</equation>

**解析:**解 在极坐标系下计算.

由 D的表达式可知，如图（a）所示，D是由直线<equation>y=x+2</equation>，圆<equation>x^{2}+y^{2}=4</equation>以及 x轴围成的部分.直线<equation>y=x+2</equation>在极坐标系下的表示为<equation>r=\frac{2}{\sin \theta -\cos \theta}</equation>，圆<equation>x^{2}+y^{2}=4</equation>在极坐标系下的表示为<equation>r=2.</equation>(a)

(b)

如图（b）所示，将 D分为两部分<equation>D_{1}</equation>和<equation>D_{2}.</equation><equation>D _ {1} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2, 0 \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation><equation>D _ {2} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \frac {2}{\sin \theta - \cos \theta}, \frac {\pi}{2} \leqslant \theta \leqslant \pi \right\}.</equation>因此，<equation>\begin{aligned} \iint_ {D} \frac {\left(x - y\right) ^ {2}}{x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \iint_ {D} \frac {r ^ {2} \left(\cos \theta - \sin \theta\right) ^ {2}}{r ^ {2}} \cdot r \mathrm {d} r \mathrm {d} \theta &= \iint_ {D} \left(\cos \theta - \sin \theta\right) ^ {2} \cdot r \mathrm {d} r \mathrm {d} \theta \\ &= \int_ {0} ^ {\frac {\pi}{2}} \left(\cos \theta - \sin \theta\right) ^ {2} \mathrm {d} \theta \int_ {0} ^ {2} r \mathrm {d} r + \int_ {\frac {\pi}{2}} ^ {\pi} \left(\cos \theta - \sin \theta\right) ^ {2} \mathrm {d} \theta \int_ {0} ^ {\frac {2}{\sin \theta - \cos \theta}} r \mathrm {d} r \\ &= 2 \int_ {0} ^ {\frac {\pi}{2}} \left(1 - 2 \sin \theta \cos \theta\right) \mathrm {d} \theta + \int_ {\frac {\pi}{2}} ^ {\pi} \left(\cos \theta - \sin \theta\right) ^ {2} \cdot \frac {r ^ {2}}{2} \Bigg | _ {0} ^ {\frac {2}{\sin \theta - \cos \theta}} \mathrm {d} \theta \\ &= 2 \left(\frac {\pi}{2} - \sin^ {2} \theta \Bigg | _ {0} ^ {\frac {\pi}{2}}\right) + \int_ {\frac {\pi}{2}} ^ {\pi} \left(\cos \theta - \sin \theta\right) ^ {2} \cdot \frac {2}{\left(\sin \theta - \cos \theta\right) ^ {2}} \mathrm {d} \theta \\ &= \pi - 2 + 2 \times \left(\pi - \frac {\pi}{2}\right) = 2 \pi - 2. \end{aligned}</equation>

---

**2021年第19题 | 解答题 | 12分**

19. (本题满分12分)

设有界区域 D是圆<equation>x^{2}+y^{2}=1</equation>与直线 y=x以及 x轴在第一象限围成的部分，请计算二重积分<equation>\iint_{D} \mathrm{e}^{(x+y)^{2}}(x^{2}-y^{2})\mathrm{d}x\mathrm{d}y.</equation>

**答案:**<equation>\frac {1}{8} (\mathrm {e} - 1) ^ {2}.</equation>

**解析:**区域 D在极坐标系下的表示为<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 1, 0 \leqslant \theta \leqslant \frac {\pi}{4} \right\}.</equation>在极坐标系下计算积分.<equation>\begin{aligned} \iint_ {D} \mathrm {e} ^ {(x + y) ^ {2}} \left(x ^ {2} - y ^ {2}\right) \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \iint_ {D} \mathrm {e} ^ {r ^ {2} (\cos \theta + \sin \theta) ^ {2}} \cdot r ^ {2} \left(\cos^ {2} \theta - \sin^ {2} \theta\right) \cdot r \mathrm {d} r \mathrm {d} \theta \\ &= \iint_ {D} \mathrm {e} ^ {r ^ {2} (1 + \sin 2 \theta)} r ^ {3} \cos 2 \theta \mathrm {d} r \mathrm {d} \theta = \int_ {0} ^ {1} r ^ {3} \mathrm {d} r \int_ {0} ^ {\frac {\pi}{4}} \mathrm {e} ^ {r ^ {2} (1 + \sin 2 \theta)} \cos 2 \theta \mathrm {d} \theta \\ &= \int_ {0} ^ {1} r ^ {3} \mathrm {d} r \int_ {0} ^ {\frac {\pi}{4}} \mathrm {e} ^ {r ^ {2} (1 + \sin 2 \theta)} \mathrm {d} \left(\frac {1 + \sin 2 \theta}{2}\right) = \frac {1}{2} \int_ {0} ^ {1} r ^ {3} \cdot \frac {\mathrm {e} ^ {r ^ {2} (1 + \sin 2 \theta)}}{r ^ {2}} \Bigg | _ {0} ^ {\frac {\pi}{4}} \mathrm {d} r \\ &= \frac {1}{2} \int_ {0} ^ {1} r \left(\mathrm {e} ^ {2 r ^ {2}} - \mathrm {e} ^ {r ^ {2}}\right) \mathrm {d} r = \frac {1}{4} \int_ {0} ^ {1} \left(\mathrm {e} ^ {2 r ^ {2}} - \mathrm {e} ^ {r ^ {2}}\right) \mathrm {d} \left(r ^ {2}\right) \\ &= \frac {1}{4} \left(\frac {\mathrm {e} ^ {2 r ^ {2}}}{2} - \mathrm {e} ^ {r ^ {2}}\right) \Bigg | _ {0} ^ {1} = \frac {1}{8} \left(\mathrm {e} ^ {2} - 2 \mathrm {e} + 1\right) = \frac {1}{8} (\mathrm {e} - 1) ^ {2}. \end{aligned}</equation>

---

**2020年第18题 | 解答题 | 10分**

18. (本题满分10分)

设 D = {(x,y) | x²+y²≤1,y≥0}, 连续函数 f(x,y)满足 f(x,y) = y<equation>\sqrt{1-x^{2}}</equation>+ x<equation>\iint_{D} f(x,y)\mathrm{d}x\mathrm{d}y</equation>，求<equation>\iint_{D} xf(x,y)\mathrm{d}x\mathrm{d}y.</equation>

**答案:**# 128

**解析:**解 记<equation>A=\iint_{D}f(x,y)\mathrm{d}x\mathrm{d}y.</equation>等式<equation>f ( x,y)=y \sqrt{1-x^{2}}+x \iint_{D} f ( x,y)\mathrm{d} x \mathrm{d} y</equation>两端在 D上积分，可得<equation>A=\iint_{D} y \sqrt{1-x^{2}}\mathrm{d} x \mathrm{d} y+A \iint_{D} x \mathrm{d} x \mathrm{d} y.</equation>区域 D如图所示，为位于 x轴上方的半圆盘，关于 y轴对称.又因为 x为关于 x的奇函数，所以<equation>\iint\limits_{D}x\mathrm{d}x\mathrm{d}y=0.</equation>将 D写成 X型区域.<equation>D=\{(x,y)\mid 0\leqslant y\leqslant \sqrt{1-x^{2}},-1\leqslant x\leqslant 1\}</equation>.于是，<equation>\begin{aligned} A &= \iint_ {D} y \sqrt {1 - x ^ {2}} \mathrm {d} x \mathrm {d} y = \int_ {- 1} ^ {1} \sqrt {1 - x ^ {2}} \mathrm {d} x \int_ {0} ^ {\sqrt {1 - x ^ {2}}} y \mathrm {d} y = \int_ {- 1} ^ {1} \sqrt {1 - x ^ {2}} \cdot \frac {1 - x ^ {2}}{2} \mathrm {d} x \\ \frac {\mathrm {对称 性}}{} \int_ {0} ^ {1} \left(1 - x ^ {2}\right) ^ {\frac {3}{2}} \mathrm {d} x \frac {x = \sin t}{\mathrm {对称 性}} \int_ {0} ^ {\frac {\pi}{2}} \cos^ {3} t \cdot \cos t \mathrm {d} t \\ &= \frac {3}{4} \times \frac {1}{2} \times \frac {\pi}{2} = \frac {3}{1 6} \pi . \end{aligned}</equation>因此，<equation>f ( x,y)=y\sqrt{1-x^{2}}+\frac{3\pi}{16} x.</equation><equation>\begin{aligned} \iint_ {D} x f (x, y) \mathrm {d} x \mathrm {d} y &= \iint_ {D} \left(x y \sqrt {1 - x ^ {2}} + \frac {3 \pi}{1 6} x ^ {2}\right) \mathrm {d} x \mathrm {d} y \xlongequal {\text {对称性}} \frac {3 \pi}{1 6} \iint_ {D} x ^ {2} \mathrm {d} x \mathrm {d} y \\ \underline {{\text {极 坐 标}}} \frac {3 \pi}{1 6} \int_ {0} ^ {\pi} \mathrm {d} \theta \int_ {0} ^ {1} r ^ {2} \cos^ {2} \theta \cdot r \mathrm {d} r &= \frac {3 \pi}{1 6} \int_ {0} ^ {\pi} \cos^ {2} \theta \mathrm {d} \theta \int_ {0} ^ {1} r ^ {3} \mathrm {d} r \\ &= \frac {3 \pi}{1 6} \cdot 2 \int_ {0} ^ {\frac {\pi}{2}} \cos^ {2} \theta \mathrm {d} \theta \cdot \frac {1}{4} = \frac {3 \pi}{1 6} \times 2 \times \frac {1}{2} \times \frac {\pi}{2} \times \frac {1}{4} \\ &= \frac {3 \pi^ {2}}{1 2 8}. \end{aligned}</equation>

---

**2018年第16题 | 解答题 | 10分**

16. (本题满分10分)

设平面区域 D由曲线<equation>y=\sqrt{3(1-x^{2})}</equation>与直线<equation>y=\sqrt{3}x</equation>及 y轴围成.计算二重积分<equation>\iint_{D}x^{2}\mathrm{d}x\mathrm{d}y.</equation>

**答案:**<equation>\frac {\sqrt {3}}{3 2} (\pi - 2).</equation>

**解析:**解 计算曲线<equation>y=\sqrt{3(1-x^{2})}</equation>与直线<equation>y=\sqrt{3} x</equation>的交点.

联立<equation>\left\{\begin{array}{l l}y=\sqrt{3(1-x^{2})},\\ y=\sqrt{3} x,\end{array}\right.</equation>解得<equation>x=\frac{\sqrt{2}}{2},y=\frac{\sqrt{6}}{2}.</equation>区域 D如图所示，其可以写成X型区域.<equation>D = \left\{(x, y) \mid \sqrt {3} x \leqslant y \leqslant \sqrt {3 \left(1 - x ^ {2}\right)}, 0 \leqslant x \leqslant \frac {\sqrt {2}}{2} \right\}.</equation>于是，<equation>\begin{aligned} \iint_ {D} x ^ {2} \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {\frac {\sqrt {2}}{2}} x ^ {2} \mathrm {d} x \int_ {\sqrt {3} x} ^ {\sqrt {3 (1 - x ^ {2})}} \mathrm {d} y = \sqrt {3} \int_ {0} ^ {\frac {\sqrt {2}}{2}} \left(\sqrt {1 - x ^ {2}} - x\right) x ^ {2} \mathrm {d} x \\ &= \sqrt {3} \left(\int_ {0} ^ {\frac {\sqrt {2}}{2}} x ^ {2} \sqrt {1 - x ^ {2}} \mathrm {d} x - \int_ {0} ^ {\frac {\sqrt {2}}{2}} x ^ {3} \mathrm {d} x\right). \end{aligned}</equation>分别计算<equation>\int_{0}^{\frac{\sqrt{2}}{2}}x^{2}\sqrt{1-x^{2}}\mathrm{d}x,</equation><equation>\int_{0}^{\frac{\sqrt{2}}{2}}x^{3}\mathrm{d}x.</equation><equation>\begin{aligned} \int_ {0} ^ {\frac {\sqrt {2}}{2}} x ^ {2} \sqrt {1 - x ^ {2}} \mathrm {d} x \xlongequal {x = \sin t} \int_ {0} ^ {\frac {\pi}{4}} \sin^ {2} t \cos t \cdot \cos t \mathrm {d} t &= \frac {1}{4} \int_ {0} ^ {\frac {\pi}{4}} \sin^ {2} 2 t \mathrm {d} t = \frac {1}{4} \int_ {0} ^ {\frac {\pi}{4}} \frac {1 - \cos 4 t}{2} \mathrm {d} t \\ &= \frac {1}{4} \times \frac {\pi}{8} - \frac {1}{4} \cdot \frac {\sin 4 t}{8} \Bigg | _ {0} ^ {\frac {\pi}{4}} = \frac {\pi}{3 2} - 0 = \frac {\pi}{3 2}. \end{aligned}</equation><equation>\int_ {0} ^ {\frac {\sqrt {2}}{2}} x ^ {3} \mathrm {d} x = \frac {x ^ {4}}{4} \Big | _ {0} ^ {\frac {\sqrt {2}}{2}} = \frac {1}{1 6}.</equation>因此，原积分<equation>= \sqrt{3}\times \left(\frac{\pi}{32} -\frac{1}{16}\right) = \frac{\sqrt{3}}{32}(\pi -2).</equation>也可以如下计算<equation>\int_{0}^{\frac{\sqrt{2}}{2}}x^{2}\sqrt{1-x^{2}}\mathrm{d}x.</equation><equation>\int_ {0} ^ {\frac {\sqrt {2}}{2}} x ^ {2} \sqrt {1 - x ^ {2}} \mathrm {d} x = \frac {1}{4} \int_ {0} ^ {\frac {\pi}{4}} \sin^ {2} 2 t \mathrm {d} t \xlongequal {u = 2 t} \frac {1}{8} \int_ {0} ^ {\frac {\pi}{2}} \sin^ {2} u \mathrm {d} u = \frac {1}{8} \times \frac {\pi}{2} \times \frac {1}{2} = \frac {\pi}{3 2}.</equation>

---

**2017年第16题 | 解答题 | 10分**

16. (本题满分10分)

计算积分<equation>\iint_ {D} \frac {y ^ {3}}{\left(1 + x ^ {2} + y ^ {4}\right) ^ {2}}</equation><equation>\mathrm{d}x\mathrm{d}y</equation>，其中<equation>D</equation>是第一象限中以曲线<equation>y = \sqrt{x}</equation>与<equation>x</equation>轴为边界的无界区域.

**答案:**<equation>\frac {(2 - \sqrt {2}) \pi}{1 6}.</equation>

**解析:**分析本题主要考查反常二重积分的计算.本题中的积分区域为无界区域，在计算时，写出无界区域的表示，将二重积分化为二次积分，最后得到一个反常积分.依照计算反常积分的方法求值即可.

解 积分区域 D为第一象限中，曲线<equation>y=\sqrt{x}</equation>以下，x轴以上的无界区域，写成X型区域的形式.<equation>D = \left\{(x, y) \mid 0 \leqslant y \leqslant \sqrt {x}, 0 \leqslant x < + \infty \right\}.</equation><equation>\begin{aligned} \iint_ {D} \frac {y ^ {3}}{\left(1 + x ^ {2} + y ^ {4}\right) ^ {2}} \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {+ \infty} \mathrm {d} x \int_ {0} ^ {\sqrt {x}} \frac {y ^ {3}}{\left(1 + x ^ {2} + y ^ {4}\right) ^ {2}} \mathrm {d} y = \frac {1}{4} \int_ {0} ^ {+ \infty} \mathrm {d} x \int_ {0} ^ {\sqrt {x}} \frac {\mathrm {d} \left(y ^ {4}\right)}{\left(1 + x ^ {2} + y ^ {4}\right) ^ {2}} \\ &= \frac {1}{4} \int_ {0} ^ {+ \infty} \left(- \frac {1}{1 + x ^ {2} + y ^ {4}} \Big | _ {0} ^ {\sqrt {x}}\right) \mathrm {d} x = \frac {1}{4} \int_ {0} ^ {+ \infty} \left(\frac {1}{1 + x ^ {2}} - \frac {1}{1 + 2 x ^ {2}}\right) \mathrm {d} x \\ &= \frac {1}{4} \left[ \arctan x - \frac {\sqrt {2}}{2} \arctan (\sqrt {2} x) \right] \Big | _ {0} ^ {+ \infty} = \frac {1}{4} \left(\frac {\pi}{2} - \frac {\sqrt {2}}{2} \times \frac {\pi}{2}\right) = \frac {(2 - \sqrt {2}) \pi}{1 6}. \end{aligned}</equation>

---

**2016年第12题 | 填空题 | 4分**

12. 设<equation>D=\{(x,y)\mid|x|\leqslant y\leqslant 1,-1\leqslant x\leqslant 1\}</equation>，则<equation>\iint_{D}x^{2}\mathrm{e}^{-y^{2}}\mathrm{d}x\mathrm{d}y=</equation>___

**答案:**# 2 3e.

**解析:**解如图所示，区域 D是由 y=x，y=-x以及 y=1围成的三角形区域. D关于 y轴对称.<equation>D_{1}</equation>为 D位于右半平面的部分.

由于<equation>x^{2}\mathrm{e}^{-y^{2}}</equation>是关于 x的偶函数，故<equation>\begin{aligned} \iint_ {D} x ^ {2} \mathrm {e} ^ {- y ^ {2}} \mathrm {d} x \mathrm {d} y &= 2 \iint_ {D _ {1}} x ^ {2} \mathrm {e} ^ {- y ^ {2}} \mathrm {d} x \mathrm {d} y = 2 \int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {y} x ^ {2} \mathrm {e} ^ {- y ^ {2}} \mathrm {d} x = \frac {2}{3} \int_ {0} ^ {1} y ^ {3} \mathrm {e} ^ {- y ^ {2}} \mathrm {d} y \\ \underline {{= t = y ^ {2}}} \frac {1}{3} \int_ {0} ^ {1} t \mathrm {e} ^ {- t} \mathrm {d} t &= \frac {1}{3} - \frac {2}{3 \mathrm {e}}. \end{aligned}</equation>

---

**2015年第16题 | 解答题 | 10分**

16. (本题满分10分)

计算二重积分<equation>D = \left\{(x, y) \mid x ^ {2} + y ^ {2} \leqslant 2, y \geqslant x ^ {2} \right\}.</equation>

**答案:**## (16)<equation>\frac{\pi}{4}-\frac{2}{5}.</equation>

**解析:**解 由图（a）可知，区域D关于y轴对称，而xy为关于x的奇函数，故<equation>\iint_{D} xy\mathrm{d}x\mathrm{d}y=0</equation>.又因为<equation>x^{2}</equation>为关于x的偶函数，所以

(a)

(b)

(c)<equation>\iint_ {D} x (x + y) \mathrm {d} x \mathrm {d} y = \iint_ {D} x ^ {2} \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} x ^ {2} \mathrm {d} x \mathrm {d} y,</equation>其中<equation>D_{1}</equation>是<equation>D</equation>位于右半平面的部分.我们可以用两种方法来计算<equation>\iint_{D} x^{2}\mathrm{d}x\mathrm{d}y.</equation>（法一）在直角坐标系下计算.

如图（b）所示，先求出圆弧<equation>x^{2}+y^{2}=2</equation>与抛物线<equation>y=x^{2}</equation>的交点.由<equation>\left\{ \begin{array}{l l} x^{2}+y^{2}=2, \\ y=x^{2}, \end{array} \right.</equation>可求得<equation>(x,y) = (1,1)</equation>或<equation>(x,y) = (-1,1)</equation>.在第一象限中的交点为<equation>(x,y) = (1,1).</equation>由圆方程<equation>x^{2}+y^{2}=2</equation>可得，<equation>y=\sqrt{2-x^{2}}</equation>.由于圆弧在第一象限，故根号前取+号.将区域<equation>D_{1}</equation>写成 X型区域，

从而<equation>D _ {1} = \left\{(x, y) \mid x ^ {2} \leqslant y \leqslant \sqrt {2 - x ^ {2}}, 0 \leqslant x \leqslant 1 \right\}.</equation><equation>\begin{aligned} \iint_ {D _ {1}} x ^ {2} \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {1} \mathrm {d} x \int_ {x ^ {2}} ^ {\sqrt {2 - x ^ {2}}} x ^ {2} \mathrm {d} y = \int_ {0} ^ {1} x ^ {2} \left(\sqrt {2 - x ^ {2}} - x ^ {2}\right) \mathrm {d} x \\ &= \int_ {0} ^ {1} x ^ {2} \sqrt {2 - x ^ {2}} \mathrm {d} x - \int_ {0} ^ {1} x ^ {4} \mathrm {d} x = \int_ {0} ^ {1} x ^ {2} \sqrt {2 - x ^ {2}} \mathrm {d} x - \frac {1}{5} \\ \xlongequal {x = \sqrt {2} \sin t} \int_ {0} ^ {\frac {\pi}{4}} 4 \sin^ {2} t \cos^ {2} t \mathrm {d} t - \frac {1}{5} &= \int_ {0} ^ {\frac {\pi}{4}} (\sin 2 t) ^ {2} \mathrm {d} t - \frac {1}{5} \\ &= \int_ {0} ^ {\frac {\pi}{4}} \frac {1 - \cos 4 t}{2} \mathrm {d} t - \frac {1}{5} = \frac {\pi}{8} - \frac {1}{5}. \end{aligned}</equation>因此，<equation>\iint_ {D} x (x + y) \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} x ^ {2} \mathrm {d} x \mathrm {d} y = \frac {\pi}{4} - \frac {2}{5}.</equation>（法二）在极坐标系下计算.

写出<equation>x^{2}+y^{2}=2</equation>的极坐标形式：<equation>r=\sqrt{2}</equation>写出<equation>y=x^{2}</equation>的极坐标形式：<equation>r\sin \theta=r^{2}\cos^{2}\theta</equation>化简为<equation>r=\tan \theta \sec \theta.</equation>可求得圆弧与抛物线的交点坐标为<equation>\left(\sqrt{2},\frac{\pi}{4}\right).</equation>如图（c）所示，连接极点与该交点，将区域<equation>D_{1}</equation>分成两部分，<equation>D_{1}=D_{1}^{\prime}\cup D_{1}^{\prime\prime}.</equation><equation>D_{1}^{\prime}</equation>由<equation>\theta=\frac{\pi}{4},</equation><equation>\theta=\frac{\pi}{2}</equation>以及圆弧<equation>r=\sqrt{2}</equation>围成；<equation>D_{1}^{\prime\prime}</equation>由<equation>\theta=\frac{\pi}{4},</equation><equation>r=\tan \theta\sec \theta</equation>围成从而<equation>D _ {1} ^ {\prime} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \sqrt {2}, \frac {\pi}{4} \leqslant \theta \leqslant \frac {\pi}{2} \right\}, \quad D _ {1} ^ {\prime \prime} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \tan \theta \sec \theta , 0 \leqslant \theta \leqslant \frac {\pi}{4} \right\}.</equation><equation>\begin{aligned} \iint_ {D _ {1}} x ^ {2} \mathrm {d} x \mathrm {d} y &= \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {\sqrt {2}} r ^ {3} \cos^ {2} \theta \mathrm {d} r + \int_ {0} ^ {\frac {\pi}{4}} \mathrm {d} \theta \int_ {0} ^ {\tan \theta \sec \theta} r ^ {3} \cos^ {2} \theta \mathrm {d} r \\ &= \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \frac {1 + \cos 2 \theta}{2} \mathrm {d} \theta + \int_ {0} ^ {\frac {\pi}{4}} \cos^ {2} \theta \cdot \frac {\tan^ {4} \theta \sec^ {4} \theta}{4} \mathrm {d} \theta \\ &= \frac {\pi}{8} - \frac {1}{4} + \frac {1}{4} \int_ {0} ^ {\frac {\pi}{4}} \tan^ {4} \theta \sec^ {2} \theta \mathrm {d} \theta \frac {u = \tan \theta}{\pi} - \frac {1}{4} + \frac {1}{4} \int_ {0} ^ {1} u ^ {4} \mathrm {d} u \\ &= \frac {\pi}{8} - \frac {1}{5}. \end{aligned}</equation>因此，<equation>\iint_ {D} x (x + y) \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} x ^ {2} \mathrm {d} x \mathrm {d} y = \frac {\pi}{4} - \frac {2}{5}.</equation>

---

**2014年第16题 | 解答题 | 10分**

16. (本题满分10分)

设平面区域<equation>D=\{(x,y)\mid 1\leqslant x^{2}+y^{2}\leqslant 4,x\geqslant 0,y\geqslant 0\}</equation>，计算<equation>\iint_{D}\frac{x\sin(\pi\sqrt{x^{2}+y^{2}})}{x+y}\mathrm{d}x\mathrm{d}y.</equation>

**答案:**<equation>(1 6) - \frac {3}{4}.</equation>

**解析:**解记<equation>\iint_{D} \frac{x\sin(\pi \sqrt{x^{2}+y^{2}})}{x+y}\mathrm{d}x\mathrm{d}y=I.</equation>积分区域如图所示.

（法一）在极坐标系下，<equation>D=\left\{(r,\theta)\mid 1\leqslant r\leqslant 2,0\leqslant \theta \leqslant \frac{\pi}{2}\right\} .</equation><equation>I=\int_{0}^{\frac{\pi}{2}}\mathrm{d}\theta \int_{1}^{2}\frac{r\cos \theta \sin (\pi r)}{r(\cos \theta +\sin \theta)} \cdot r\mathrm{d}r=\int_{0}^{\frac{\pi}{2}}\frac{\cos \theta}{\cos \theta +\sin \theta}\mathrm{d}\theta \int_{1}^{2}r\sin (\pi r)\mathrm{d}r.</equation>由于<equation>\int_ {0} ^ {\frac {\pi}{2}} \frac {\cos \theta}{\cos \theta + \sin \theta} \mathrm {d} \theta \stackrel {t = \frac {\pi}{2} - \theta} {=} - \int_ {\frac {\pi}{2}} ^ {0} \frac {\sin t}{\cos t + \sin t} \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \frac {\sin \theta}{\cos \theta + \sin \theta} \mathrm {d} \theta ,</equation>故<equation>\int_ {0} ^ {\frac {\pi}{2}} \frac {\cos \theta}{\cos \theta + \sin \theta} \mathrm {d} \theta = \frac {1}{2} \int_ {0} ^ {\frac {\pi}{2}} \left(\frac {\cos \theta}{\cos \theta + \sin \theta} + \frac {\sin \theta}{\cos \theta + \sin \theta}\right) \mathrm {d} \theta = \frac {1}{2} \int_ {0} ^ {\frac {\pi}{2}} 1 \mathrm {d} \theta = \frac {\pi}{4}.</equation>此外，<equation>\int_ {1} ^ {2} r \sin (\pi r) \mathrm {d} r = - \frac {1}{\pi} \int_ {1} ^ {2} r \mathrm {d} [ \cos (\pi r) ] = - \frac {1}{\pi} \left[ r \cos (\pi r) \left| _ {1} ^ {2} - \int_ {1} ^ {2} \cos (\pi r) \mathrm {d} r \right] = - \frac {3}{\pi} \right].</equation>因此，<equation>I = \frac{\pi}{4}\times \left(-\frac{3}{\pi}\right) = -\frac{3}{4}.</equation>（法二）首先，由于积分区域<equation>D</equation>关于<equation>y = x</equation>对称，故对<equation>x, y</equation>具有轮换对称性，从而<equation>I = \iint_ {D} \frac {x \sin \left(\pi \sqrt {x ^ {2} + y ^ {2}}\right)}{x + y} \mathrm {d} x \mathrm {d} y = \iint_ {D} \frac {y \sin \left(\pi \sqrt {x ^ {2} + y ^ {2}}\right)}{x + y} \mathrm {d} x \mathrm {d} y.</equation>因此，<equation>I = \frac {1}{2} \iint_ {D} \left[ \frac {x \sin \left(\pi \sqrt {x ^ {2} + y ^ {2}}\right)}{x + y} + \frac {y \sin \left(\pi \sqrt {x ^ {2} + y ^ {2}}\right)}{x + y} \right] \mathrm {d} x \mathrm {d} y = \frac {1}{2} \iint_ {D} \sin \left(\pi \sqrt {x ^ {2} + y ^ {2}}\right) \mathrm {d} x \mathrm {d} y.</equation>在极坐标系下，<equation>D = \left\{(r,\theta)\mid 1\leqslant r\leqslant 2,0\leqslant \theta \leqslant \frac{\pi}{2}\right\}.</equation><equation>I = \frac {1}{2} \int_ {0} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {1} ^ {2} \sin (\pi r) \cdot r \mathrm {d} r = \frac {\pi}{4} \int_ {1} ^ {2} r \sin (\pi r) \mathrm {d} r,</equation>由法一知<equation>\int_1^2 r\sin (\pi r)\mathrm{d}r = -\frac{3}{\pi}</equation>，故<equation>I = \frac{\pi}{4}\times \left(-\frac{3}{\pi}\right) = -\frac{3}{4}</equation>.

---

**2013年第17题 | 解答题 | 10分**

17. (本题满分10分)

设平面区域 D由直线 x=3y，y=3x及 x+y=8围成，计算<equation>\iint\limits_{D}x^{2}\mathrm{d}x\mathrm{d}y.</equation>

**答案:**## (17)<equation>\frac{4 1 6}{3}.</equation>

**解析:**解（法一）在直角坐标系下计算.

如图所示，可以分别求出<equation>y=3 x</equation>与<equation>x+y=8</equation>的交点，以及<equation>x=3 y</equation>与<equation>x+y=8</equation>的交点.<equation>\left\{ \begin{array}{l l} y = 3 x, \\ x + y = 8, \end{array} \right. \Rightarrow \left\{ \begin{array}{l l} x = 2, \\ y = 6, \end{array} \right. \quad \left\{ \begin{array}{l l} x = 3 y, \\ x + y = 8, \end{array} \right. \Rightarrow \left\{ \begin{array}{l l} x = 6, \\ y = 2. \end{array} \right.</equation>于是直线<equation>x = 2</equation>将区域<equation>D</equation>分为两部分<equation>D_{1}, D_{2}</equation>.<equation>D _ {1} = \left\{(x, y) \mid \frac {x}{3} \leqslant y \leqslant 3 x, 0 \leqslant x \leqslant 2 \right\}, \quad D _ {2} = \left\{(x, y) \mid \frac {x}{3} \leqslant y \leqslant 8 - x, 2 \leqslant x \leqslant 6 \right\}.</equation><equation>\begin{aligned} \iint_ {D} x ^ {2} \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {2} x ^ {2} \mathrm {d} x \int_ {\frac {x}{3}} ^ {3 x} \mathrm {d} y + \int_ {2} ^ {6} x ^ {2} \mathrm {d} x \int_ {\frac {x}{3}} ^ {8 - x} \mathrm {d} y = \int_ {0} ^ {2} x ^ {2} \cdot \frac {8}{3} x \mathrm {d} x + \int_ {2} ^ {6} \left(8 - \frac {4}{3} x\right) x ^ {2} \mathrm {d} x \\ &= \frac {2}{3} x ^ {4} \left| _ {0} ^ {2} + \frac {8}{3} x ^ {3} \right| _ {2} ^ {6} - \frac {1}{3} x ^ {4} \left| _ {2} ^ {6} = \frac {4 1 6}{3}. \right. \end{aligned}</equation>（法二）在极坐标系下计算.

三条直线的方程分别为<equation>\theta=\arctan \frac{1}{3},</equation><equation>\theta=\arctan 3</equation>，以及<equation>r(\cos \theta+\sin \theta)=8.</equation>此时，区域D在极坐标系下的表示为<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \frac {8}{\cos \theta + \sin \theta}, \arctan \frac {1}{3} \leqslant \theta \leqslant \arctan 3 \right\}.</equation><equation>\begin{aligned} \iint_ {D} x ^ {2} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \iint_ {D} r ^ {2} \cos^ {2} \theta \cdot r \mathrm {d} r \mathrm {d} \theta &= \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} \cos^ {2} \theta \mathrm {d} \theta \int_ {0} ^ {\frac {8}{\cos \theta + \sin \theta}} r ^ {3} \mathrm {d} r \\ &= \frac {8 ^ {4}}{4} \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} \frac {\cos^ {2} \theta}{\left(\cos \theta + \sin \theta\right) ^ {4}} \mathrm {d} \theta = \frac {8 ^ {4}}{4} \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} \frac {1}{\left(1 + \tan \theta\right) ^ {4}} \cdot \sec^ {2} \theta \mathrm {d} \theta \\ \underline {{= u = \tan \theta}} \frac {8 ^ {4}}{4} \int_ {\frac {1}{3}} ^ {3} \frac {1}{(1 + u) ^ {4}} \mathrm {d} u &= \frac {8 ^ {4}}{4} \cdot \left(- \frac {1}{3}\right) \frac {1}{(1 + u) ^ {3}} \Big | _ {\frac {1}{3}} ^ {3} = \frac {4 1 6}{3}. \end{aligned}</equation>

---

**2012年第16题 | 解答题 | 10分**

16. (本题满分10分)

计算二重积分<equation>\iint_{D} \mathrm{e}^{x} x y \mathrm{d} x \mathrm{d} y</equation>，其中 D是以曲线<equation>y=\sqrt{x}, y=\frac{1}{\sqrt{x}}</equation>及 y轴为边界的无界区域.

**答案:**## (16)<equation>\frac{1}{2}.</equation>

**解析:**分析本题主要考查反常二重积分的计算。本题中的积分区域为无界区域，在计算时，写出无界区域的表示，将二重积分化为二次积分，最后得到一个反常积分。依照反常积分的计算方法求值即可。

解 将<equation>D</equation>看作X型区域，<equation>D = \left\{(x,y)\mid \sqrt{x}\leq y\leq \frac{1}{\sqrt{x}},0 < x\leq 1\right\}</equation>，则<equation>\begin{aligned} \iint_ {D} \mathrm {e} ^ {x} x y \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {1} \mathrm {d} x \int_ {\sqrt {x}} ^ {\frac {1}{\sqrt {x}}} \mathrm {e} ^ {x} x y \mathrm {d} y = \int_ {0} ^ {1} \frac {1}{2} \left(1 - x ^ {2}\right) \mathrm {e} ^ {x} \mathrm {d} x = \frac {1}{2} \int_ {0} ^ {1} \left(1 - x ^ {2}\right) \mathrm {d} \left(\mathrm {e} ^ {x}\right) \\ &= \frac {1}{2} \left[ \left(1 - x ^ {2}\right) \mathrm {e} ^ {x} \left| _ {0} ^ {1} + \int_ {0} ^ {1} 2 x \mathrm {e} ^ {x} \mathrm {d} x \right] \right. \\ &= \frac {1}{2} \left(- 1 + 2 x \mathrm {e} ^ {x} \left| _ {0} ^ {1} - 2 \int_ {0} ^ {1} \mathrm {e} ^ {x} \mathrm {d} x\right)\right) \\ &= \frac {1}{2} \left[ - 1 + 2 \mathrm {e} - 2 (\mathrm {e} - 1) \right] = \frac {1}{2}. \end{aligned}</equation>

---

**2010年第16题 | 解答题 | 10分**

16. (本题满分10分)

计算二重积分<equation>\iint_{D} ( x+y )^{3} \mathrm{d} x \mathrm{d} y</equation>，其中 D由曲线<equation>x=\sqrt{1+y^{2}}</equation>与直线<equation>x+\sqrt{2} y=0</equation>及<equation>x-\sqrt{2} y=0</equation>围成.

**答案:**## (16)<equation>\frac{1 4}{1 5}.</equation>

**解析:**分析本题主要考查二重积分的计算.通过观察发现，积分区域 D关于 x轴对称，因此我们可以利用积分区域的对称性以及被积函数的奇偶性来简化计算.

解如图所示，积分区域 D关于 x轴对称，故<equation>\iint_ {D} (x + y) ^ {3} \mathrm {d} x \mathrm {d} y = \iint_ {D} \left(x ^ {3} + 3 x ^ {2} y + 3 x y ^ {2} + y ^ {3}\right) \mathrm {d} x \mathrm {d} y = \iint_ {D} \left(x ^ {3} + 3 x y ^ {2}\right) \mathrm {d} x \mathrm {d} y.</equation>分别计算<equation>x = \sqrt{1 + y^2}</equation>与<equation>x = \sqrt{2} y, x = -\sqrt{2} y</equation>的交点得<equation>(\sqrt{2}, 1), (\sqrt{2}, -1)</equation>. 记<equation>D_{1}</equation>为区域<equation>D</equation>位于<equation>x</equation>轴以上的部分. 将<equation>D_{1}</equation>写为 Y 型区域.<equation>D_{1} = \{(x, y) \mid \sqrt{2} y \leqslant x \leqslant \sqrt{1 + y^2}, 0 \leqslant y \leqslant 1\}</equation>. 于是，<equation>\begin{aligned} \iint_ {D} (x + y) ^ {3} \mathrm {d} x \mathrm {d} y &= 2 \iint_ {D _ {1}} \left(x ^ {3} + 3 x y ^ {2}\right) \mathrm {d} x \mathrm {d} y = 2 \int_ {0} ^ {1} \mathrm {d} y \int_ {\sqrt {2} y} ^ {\sqrt {1 + y ^ {2}}} \left(x ^ {3} + 3 x y ^ {2}\right) \mathrm {d} x \\ &= 2 \left[ \int_ {0} ^ {1} \frac {\left(1 + y ^ {2}\right) ^ {2} - \left(2 y ^ {2}\right) ^ {2}}{4} \mathrm {d} y + \int_ {0} ^ {1} \frac {3 y ^ {2} \left(1 + y ^ {2} - 2 y ^ {2}\right)}{2} \mathrm {d} y \right] \\ &= \frac {1}{2} \int_ {0} ^ {1} \left(1 + 2 y ^ {2} - 3 y ^ {4}\right) \mathrm {d} y + 3 \int_ {0} ^ {1} \left(y ^ {2} - y ^ {4}\right) \mathrm {d} y = \int_ {0} ^ {1} \left(\frac {1}{2} + 4 y ^ {2} - \frac {9}{2} y ^ {4}\right) \mathrm {d} y \\ &= \frac {1}{2} + \frac {4}{3} - \frac {9}{1 0} = \frac {1 4}{1 5}. \end{aligned}</equation>

---

**2009年第17题 | 解答题 | 10分**

17. (本题满分10分)

计算二重积分<equation>\iint\limits_{D} ( x-y ) \mathrm{d} x \mathrm{d} y</equation>，其中<equation>D=\{(x,y)\mid(x-1)^{2}+(y-1)^{2}\leqslant 2,y\geqslant x\}</equation>

**答案:**<equation>(1 7) - \frac {8}{3}.</equation>

**解析:**<equation>D</equation>分析 本题主要考查二重积分的计算.由于积分区域为圆域的一部分，故可以考虑在极坐标系下进行计算.

点M的直角坐标(x,y)与极坐标（r，θ）满足<equation>\left\{ \begin{array}{l l} x = r\cos \theta , \\ y = r\sin \theta . \end{array} \right.</equation>若在极坐标系下计算，则有公式<equation>\iint_ {D} f (x, y) \mathrm {d} \sigma = \iint_ {D} f (r \cos \theta , r \sin \theta) r \mathrm {d} r \mathrm {d} \theta ,</equation>其中<equation>r\mathrm{d}r\mathrm{d}\theta</equation>为极坐标系中的面积元素.

解如图所示，作极坐标变换<equation>\left\{ \begin{array}{l l} x = r\cos \theta , \\ y = r\sin \theta , \end{array} \right.</equation>则圆方程<equation>(x - 1)^{2}</equation><equation>+ (y - 1)^{2} = 2</equation>变成<equation>r = 2(\cos \theta +\sin \theta)</equation>，从而D在极坐标系下表示为<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2 (\cos \theta + \sin \theta), \frac {\pi}{4} \leqslant \theta \leqslant \frac {3 \pi}{4} \right\}.</equation>因此，<equation>\begin{aligned} \iint_ {D} (x - y) \mathrm {d} x \mathrm {d} y &= \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} (\cos \theta - \sin \theta) \mathrm {d} \theta \int_ {0} ^ {2 (\cos \theta + \sin \theta)} r ^ {2} \mathrm {d} r = \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} (\cos \theta - \sin \theta) \left[ \frac {r ^ {3}}{3} \right| _ {0} ^ {2 (\cos \theta + \sin \theta)} \mathrm {d} \theta \\ &= \frac {8}{3} \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} (\cos \theta + \sin \theta) ^ {2} \left(\cos^ {2} \theta - \sin^ {2} \theta\right) \mathrm {d} \theta = \frac {8}{3} \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} (1 + \sin 2 \theta) \cos 2 \theta \mathrm {d} \theta \\ \underline {{= u = \sin 2 \theta}} \frac {4}{3} \int_ {1} ^ {- 1} (1 + u) \mathrm {d} u &= - \frac {8}{3}. \end{aligned}</equation>或者也可以这样计算.<equation>\begin{aligned} \iint_ {D} (x - y) \mathrm {d} x \mathrm {d} y &= \frac {8}{3} \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} \left(\cos \theta + \sin \theta\right) ^ {3} \left(\cos \theta - \sin \theta\right) \mathrm {d} \theta = \frac {8}{3} \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} \left(\cos \theta + \sin \theta\right) ^ {3} \mathrm {d} \left(\cos \theta + \sin \theta\right) \\ &= \frac {2}{3} \left(\cos \theta + \sin \theta\right) ^ {4} \Bigg | _ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} = - \frac {8}{3}. \end{aligned}</equation>

---


#### 多元函数微分学的几何应用

**2024年第13题 | 填空题 | 5分**

13. 函数<equation>f(x,y)=2x^{3}-9x^{2}-6y^{4}+12x+24y</equation>的极值点是 ___

**答案:**## (1,1)

**解析:**解 计算 f(x,y) 的驻点.

整理<equation>\left\{\begin{array}{l l}f_{x}^{\prime}(x,y)=6x^{2}-18x+12=0\\ f_{y}^{\prime}(x,y)=-24y^{3}+24=0\end{array}\right.</equation>可得<equation>\left\{\begin{array}{l l}x^{2}-3x+2=0\\ y^{3}-1=0,\end{array}\right.</equation>解得<equation>\left\{\begin{array}{l l}x=1,\\ y=1,\end{array}\right.</equation>或<equation>\left\{\begin{array}{l l}x=2,\\ y=1,\end{array}\right.</equation>即<equation>f(x,y)</equation>的全部驻点为点（1，1），（2，1）.

计算 f（x,y）的二阶偏导数.<equation>f _ {x x} ^ {\prime \prime} (x, y) = 1 2 x - 1 8, f _ {x y} ^ {\prime \prime} (x, y) = 0, f _ {y y} ^ {\prime \prime} (x, y) = - 7 2 y ^ {2}.</equation>对点（1,1），<equation>A=f_{x x}^{\prime \prime}(1,1)=-6,B=f_{x y}^{\prime \prime}(1,1)=0,C=f_{y y}^{\prime \prime}(1,1)=-72,AC-B^{2}=(-6)\times</equation>（-72）-0>0，且<equation>A<0</equation>，故由二元函数极值存在的充分条件可知，点（1,1）是<equation>f(x,y)</equation>的极大值点.

对点（2,1），<equation>A=f_{xx}^{\prime \prime}(2,1)=6,B=f_{xy}^{\prime \prime}(2,1)=0,C=f_{yy}^{\prime \prime}(2,1)=-72,AC-B^{2}=6\times(-72)</equation><equation>- 0 < 0</equation>，故由二元函数极值存在的充分条件可知，点（2,1）不是<equation>f(x,y)</equation>的极值点.

因此，<equation>f(x,y)</equation>的唯一极值点为（1，1）.

---

**2021年第18题 | 解答题 | 12分**

18. (本题满分12分)

求函数<equation>f ( x,y)=2 \ln | x |+\frac{(x-1)^{2}+y^{2}}{2 x^{2}}</equation>的极值

的极值.

**答案:**（-1,0）为 f(x,y)的极小值点，极小值为 f(-1,0) = 2.<equation>\left(\frac{1}{2},0\right)</equation>为 f(x,y)的极小值点，极小值为<equation>f\left(\frac{1}{2},0\right)=-2\ln 2+\frac{1}{2}.</equation>

**解析:**解 先求驻点坐标. 计算<equation>f_{x}^{\prime}(x,y)</equation>与<equation>f_{y}^{\prime}(x,y).</equation><equation>\begin{array}{l} f _ {x} ^ {\prime} (x, y) = \frac {2}{x} + \frac {2 (x - 1) \cdot 2 x ^ {2} - [ (x - 1) ^ {2} + y ^ {2} ] \cdot 4 x}{4 x ^ {4}} \\ = \frac {2}{x} + \frac {(x - 1) \cdot x - (x - 1) ^ {2} - y ^ {2}}{x ^ {3}} \\ = \frac {2 x ^ {2} + x - 1 - y ^ {2}}{x ^ {3}}. \\ \end{array}</equation><equation>f _ {y} ^ {\prime} (x, y) = \frac {2 y}{2 x ^ {2}} = \frac {y}{x ^ {2}}.</equation>令<equation>\left\{\begin{array}{l l} {\frac{2x^{2}+x-1-y^{2}}{x^{3}}=0,} \\ {\frac{y}{x^{2}}=0,} \\ \end{array} \right.</equation>解得 y=0,x=<equation>\frac{1}{2}</equation>或 x=-1.于是，f(x,y)有两个驻点 (-1,0),<equation>\left(\frac{1}{2},0\right).</equation>分别计算 f（x,y）的二阶偏导数.<equation>\begin{array}{l} f _ {x x} ^ {\prime \prime} (x, y) = \frac {(4 x + 1) \cdot x ^ {3} - \left(2 x ^ {2} + x - 1 - y ^ {2}\right) \cdot 3 x ^ {2}}{x ^ {6}} \\ = \frac {(4 x + 1) \cdot x - 3 \left(2 x ^ {2} + x - 1 - y ^ {2}\right)}{x ^ {4}} \\ = \frac {- 2 x ^ {2} - 2 x + 3 + 3 y ^ {2}}{x ^ {4}}. \\ \end{array}</equation><equation>f _ {x y} ^ {\prime \prime} (x, y) = - \frac {2 y}{x ^ {3}}.</equation><equation>f _ {y y} ^ {\prime \prime} (x, y) = \frac {1}{x ^ {2}}.</equation>(1) 对驻点（-1，0），计算得 A=3,B=0,C=1. 从而<equation>A C-B^{2}>0</equation>，且 A > 0 ，故（-1，0）为<equation>f(x,y)</equation>的极小值点，极小值为<equation>f(-1,0)=2.</equation>(2) 对驻点<equation>\left(\frac{1}{2},0\right)</equation>，计算得 A=24,B=0,C=4.从而<equation>AC-B^{2}>0</equation>，且 A>0，故<equation>\left(\frac{1}{2},0\right)</equation>为<equation>f(x,y)</equation>的极小值点，极小值为<equation>f\left(\frac{1}{2},0\right)=-2\ln 2+\frac{1}{2}.</equation>

---

**2020年第16题 | 解答题 | 10分**

16. (本题满分10分)

求函数<equation>f ( x,y)=x^{3}+8 y^{3}-x y</equation>的极值.

**答案:**极小值为<equation>f\left(\frac{1}{6},\frac{1}{12}\right)=- \frac{1}{216}.</equation>

**解析:**解<equation>\left\{ \begin{array}{l l} f_{x}^{\prime}(x,y)=3x^{2}-y=0, \\ f_{y}^{\prime}(x,y)=24y^{2}-x=0. \end{array} \right.</equation>将 y=3x²代入24y²-x=0可得216x4=x，解得x=0或x<equation>=\frac{1}{6}.</equation>于是，<equation>\left\{ \begin{array}{l l} x=0, \\ y=0 \end{array} \right.</equation>或<equation>\left\{ \begin{array}{l l} x=\frac{1}{6}, \\ y=\frac{1}{12}. \end{array} \right.</equation><equation>f(x,y)</equation>有两个驻点(0,0)，<equation>\left(\frac{1}{6},\frac{1}{12}\right).</equation><equation>\textcircled{2}</equation>计算 f(x,y)的二阶偏导数.<equation>f_{xx}^{\prime\prime}(x,y)=6x,</equation><equation>f_{xy}^{\prime\prime}(x,y)=-1,</equation><equation>f_{yy}^{\prime\prime}(x,y)=48y.</equation><equation>\textcircled{3}</equation>判断驻点是否为极值点以及确定极值点类型.

• 考虑驻点(0,0).<equation>A=f_{xx}^{\prime\prime}(0,0)=0,</equation><equation>B=f_{xy}^{\prime\prime}(0,0)=-1,</equation><equation>C=f_{yy}^{\prime\prime}(0,0)=0.</equation><equation>AC-B^{2}=0-1=-1<0</equation>，故点(0,0)不是极值点.

• 考虑驻点<equation>\left(\frac{1}{6},\frac{1}{12}\right).</equation><equation>A=f_{xx}^{\prime\prime}\left(\frac{1}{6},\frac{1}{12}\right)=1,</equation><equation>B=f_{xy}^{\prime\prime}\left(\frac{1}{6},\frac{1}{12}\right)=-1,</equation><equation>C=f_{yy}^{\prime\prime}\left(\frac{1}{6},\frac{1}{12}\right)=4.</equation><equation>AC-B^{2}=4-1=3>0</equation>，且 A>0，故点<equation>\left(\frac{1}{6},\frac{1}{12}\right)</equation>为极小值点，极小值为<equation>f\left(\frac{1}{6},\frac{1}{12}\right)=\frac{1}{6^{3}}+\frac{8}{12^{3}}-\frac{1}{6\times 12}=-\frac{1}{216}.</equation>

---

**2018年第17题 | 解答题 | 10分**

17. (本题满分10分)

将长为2m的铁丝分成三段，依次围成圆、正方形与正三角形. 三个图形的面积之和是否存在最小值？若存在，求出最小值.

**答案:**三个图形的面积之和存在最小值，最小值为<equation>\frac{1}{\pi+4+3\sqrt{3}}.</equation>

**解析:**解设圆、正方形、正三角形的周长分别为 x,y,z，则圆的半径<equation>r=\frac{x}{2\pi}</equation>正方形的边长 a<equation>=\frac{y}{4}</equation>正三角形的边长 b<equation>=\frac{z}{3}</equation>.于是，三个图形的面积之和为<equation>S (x, y, z) = \pi \cdot \left(\frac {x}{2 \pi}\right) ^ {2} + \left(\frac {y}{4}\right) ^ {2} + \frac {1}{2} \cdot \left(\frac {z}{3}\right) ^ {2} \cdot \sin \frac {\pi}{3} = \frac {x ^ {2}}{4 \pi} + \frac {y ^ {2}}{1 6} + \frac {\sqrt {3}}{3 6} z ^ {2}.</equation>由于三段铁丝的周长之和为2，故<equation>x+y+z=2.</equation>建立拉格朗日函数<equation>L ( x,y,z,\lambda) = \frac{x^{2}}{4\pi} +\frac{y^{2}}{16} +\frac{\sqrt{3}}{36} z^{2} +\lambda ( x+y+z-2).</equation>令<equation>\left\{ \begin{array}{l} L _ {x} ^ {\prime} = \frac {1}{2 \pi} x + \lambda = 0, \\ L _ {y} ^ {\prime} = \frac {1}{8} y + \lambda = 0, \\ L _ {z} ^ {\prime} = \frac {\sqrt {3}}{1 8} z + \lambda = 0, \\ L _ {\lambda} ^ {\prime} = x + y + z - 2 = \end{array} \right.</equation>由前三个方程可得<equation>x = -2\pi \lambda ,y = -8\lambda ,z = -6\sqrt{3}\lambda .</equation>代入 x+y+z-2=0可得<equation>\lambda = - \frac {2}{2 \pi + 8 + 6 \sqrt {3}} = - \frac {1}{\pi + 4 + 3 \sqrt {3}}.</equation>于是，<equation>x=\frac{2\pi}{\pi+4+3\sqrt{3}}, y=\frac{8}{\pi+4+3\sqrt{3}}, z=\frac{6\sqrt{3}}{\pi+4+3\sqrt{3}}.</equation>将所得 x,y,z的值代入 S（x，y，z）可得<equation>S (x, y, z) = \frac {\pi + 4 + 3 \sqrt {3}}{(\pi + 4 + 3 \sqrt {3}) ^ {2}} = \frac {1}{\pi + 4 + 3 \sqrt {3}}.</equation>为了判定所求得可能的极值点是否为最小值点，我们把问题转化为目标函数 S（x，y，z）在有界闭区域 D = {（x，y，z）| x+y+z=2，x≥0，y≥0，z≥0}上的最值问题.

由于连续函数在有界闭区域上一定能取到最值，故若我们能分别计算出<equation>S ( x, y, z )</equation>在边界<equation>y + z = 2, z + x = 2, x + y = 2</equation>上的最值，再与<equation>\frac{1} {\pi+4+3 \sqrt{3}}</equation>比较，则所得最小值即为区域D上的最小值当 x=0时，<equation>S ( 0, y, z )</equation>在 y+z=2下的最小值为<equation>S \left( 0, \frac{8}{4+3 \sqrt{3}}, \frac{6 \sqrt{3}}{4+3 \sqrt{3}} \right)=\frac{1}{4+3 \sqrt{3}}.</equation>当 y=0时，<equation>S ( x, 0, z )</equation>在 x+z=2下的最小值为<equation>S \left( \frac{2 \pi}{\pi+3 \sqrt{3}}, 0, \frac{6 \sqrt{3}}{\pi+3 \sqrt{3}} \right)=\frac{1}{\pi+3 \sqrt{3}}.</equation>当 z=0时，<equation>S ( x, y, 0 )</equation>在 x+y=2下的最小值为<equation>S \left( \frac{2 \pi}{\pi+4}, \frac{8}{\pi+4}, 0 \right)=\frac{1}{\pi+4}.</equation>4个值比较可得，<equation>\frac{1} {\pi+4+3 \sqrt{3}}</equation>为整个区域D上的最小值，也为 x+y+z=2,x>0,y>0，z>0时的 S(x,y,z)的最小值.三个图形的面积之和存在最小值，最小值为<equation>\frac{1} {\pi+4+3 \sqrt{3}}.</equation>

---

**2017年第2题 | 选择题 | 4分 | 答案: D**

2. 二元函数 z=xy（3-x-y）的极值点是（    ）

A. (0,0) B. (0,3) C. (3,0) D. (1,1)

答案: D

**解析:**解 先求驻点坐标.计算<equation>\frac{\partial z}{\partial x}</equation>与<equation>\frac{\partial z}{\partial y}.</equation><equation>\frac {\partial z}{\partial x} = - y ^ {2} - 2 x y + 3 y = y (3 - 2 x - y),</equation><equation>\frac {\partial z}{\partial y} = - x ^ {2} - 2 x y + 3 x = x (3 - x - 2 y).</equation>解<equation>\left\{\begin{array}{l l}y(3-2x-y)=0,\\ x(3-x-2y)=0,\end{array} \right.</equation>得4组解：<equation>\left\{ \begin{array}{l l} x = 0, \\ y = 0, \end{array} \right. \quad \left\{ \begin{array}{l l} x = 0, \\ y = 3, \end{array} \right. \quad \left\{ \begin{array}{l l} x = 3, \\ y = 0, \end{array} \right. \quad \left\{ \begin{array}{l l} x = 1, \\ y = 1. \end{array} \right.</equation>计算 z的二阶偏导数得<equation>\frac {\partial^ {2} z}{\partial x ^ {2}} = - 2 y, \quad \frac {\partial^ {2} z}{\partial y ^ {2}} = - 2 x, \quad \frac {\partial^ {2} z}{\partial x \partial y} = 3 - 2 x - 2 y.</equation>当（x,y）=（0,0）或（3,0）或（0,3）时，<equation>\frac{\partial^{2}z}{\partial x^{2}}\frac{\partial^{2}z}{\partial y^{2}}-\left(\frac{\partial^{2}z}{\partial x\partial y}\right)^{2}<0</equation>，故这三个点都不是极值点当（x,y）=（1,1）时，<equation>\frac {\partial^ {2} z}{\partial x ^ {2}} \frac {\partial^ {2} z}{\partial y ^ {2}} - \left(\frac {\partial^ {2} z}{\partial x \partial y}\right) ^ {2} = 4 - 1 = 3 > 0, \quad \frac {\partial^ {2} z}{\partial x ^ {2}} = - 2 < 0.</equation>因此，点（1，1）是极大值点.应选D.

---

**2012年第17题 | 解答题 | 10分**


某企业为生产甲、乙两种型号的产品投入的固定成本为10000(万元).设该企业生产甲、乙两种产品的产量分别为 x (件)和 y (件)，且这两种产品的边际成本分别为<equation>2 0+\frac { x } { 2 }</equation>(万元/件)与<equation>6+y</equation>(万元/件).

I. 求生产甲、乙两种产品的总成本函数 C(x,y) (万元).

II. 当总产量为50件时，甲、乙两种产品的产量各为多少时可使总成本最小？求最小总成本.

III. 求总产量为50件且总成本最小时甲产品的边际成本，并解释其经济意义.

**答案:**(17) ( I )<equation>C ( x,y)=2 0 x+\frac{x^{2}}{4}+6 y+\frac{y^{2}}{2}+1 0 0 0 0.</equation>（Ⅱ）若总产量为50件，则当甲种产品的产量为24件，乙种产品的产量为26件时，总成本最小，最小成本为<equation>C ( 2 4, 2 6 ) = 1 1 1 1 8</equation>万元.

（Ⅲ）当总产量为50件且总成本最小时，甲种产品的边际成本为32万元。其经济意义为，当甲、乙两种产品的产量分别为24件，26件时，若甲种产品的产量再增加1件，则总成本增加32万元，即当乙种产品的产量为26件时，生产第25件甲种产品需要32万元.

**解析:**（I）由边际成本的定义及题设知<equation>\frac {\partial C (x , y)}{\partial x} = 2 0 + \frac {x}{2},</equation><equation>\frac {\partial C (x , y)}{\partial y} = 6 + y.</equation>由（1）式知<equation>C ( x,y)=2 0 x+\frac{x^{2}}{4}+f ( y )</equation>，其中<equation>f ( y )</equation>为关于y的待定函数.将<equation>C ( x,y)</equation>的表达式代入（2）式得<equation>f^{\prime}(y)=6+y.</equation>于是<equation>f ( y ) = 6 y + \frac{y^{2}}{2} + a</equation>其中a为待定常数.因此，<equation>C (x, y) = 2 0 x + \frac {x ^ {2}}{4} + 6 y + \frac {y ^ {2}}{2} + a.</equation>又由题设知<equation>C(0,0) = 10000</equation>，代入上式得到<equation>a = 10000</equation>，故<equation>C (x, y) = 2 0 x + \frac {x ^ {2}}{4} + 6 y + \frac {y ^ {2}}{2} + 1 0 0 0 0.</equation>（Ⅱ）（法一）由题设知<equation>x+y=50</equation>，于是<equation>\begin{array}{l} C (x, y) = C (x, 5 0 - x) = 2 0 x + \frac {x ^ {2}}{4} + 6 (5 0 - x) + \frac {(5 0 - x) ^ {2}}{2} + 1 0 0 0 0 \\ = \frac {3}{4} x ^ {2} - 3 6 x + 1 1 5 5 0 = \frac {3}{4} (x - 2 4) ^ {2} + 1 1 1 1 8. \\ \end{array}</equation>从而当<equation>x = 24</equation>时，<equation>C(x,y)</equation>取值最小且最小值为11118，此时<equation>y = 26.</equation>因此，若总产量为50件，则当甲种产品的产量为24件，乙种产品的产量为26件时，总成本最小，最小成本为11118万元.

（法二）由题设知，要求<equation>C(x,y)</equation>在<equation>x + y = 50</equation>的条件下的最值，我们可以采用拉格朗日乘数法.

作拉格朗日函数<equation>L(x,y,\lambda) = C(x,y) + \lambda (x + y - 50)</equation>，令<equation>\left\{ \begin{array}{l} L _ {x} ^ {\prime} = \frac {\partial C (x , y)}{\partial x} + \lambda = 2 0 + \frac {x}{2} + \lambda = 0, \\ L _ {y} ^ {\prime} = \frac {\partial C (x , y)}{\partial y} + \lambda = 6 + y + \lambda = 0, \\ L _ {\lambda} ^ {\prime} = x + y - 5 0 = 0. \end{array} \right.</equation>解得 x=24，y=26，这是唯一可能的极值点.因为由问题本身可知最小值一定存在，所以最小值在这个可能的极值点处取得.

因此，若总产量为50件，则当甲种产品的产量为24件，乙种产品的产量为26件时，总成本最小，最小成本为<equation>C (2 4, 2 6) = 1 1 1 1 8 (\text {万 元}).</equation>（Ⅲ）由边际成本的定义知，当总产量为50件且总成本最小时，甲种产品的边际成本为<equation>\left. \frac {\partial C}{\partial x} \right| _ {(2 4, 2 6)} = \left(2 0 + \frac {x}{2}\right) \Big | _ {(2 4, 2 6)} = 2 0 + \frac {2 4}{2} = 3 2 (\text {万 元}).</equation>其经济意义为，当甲、乙两种产品的产量分别为24件，26件时，若甲种产品的产量再增加1件，则总成本增加32万元，即当乙种产品的产量为26件时，生产第25件甲种产品需要32万元.

---

**2010年第17题 | 解答题 | 10分**

17. (本题满分10分)

求函数<equation>u=xy+2yz</equation>在约束条件<equation>x^{2}+y^{2}+z^{2}=1 0</equation>下的最大值和最小值.

**答案:**## （17）最大值为<equation>5\sqrt{5}</equation>最小值为<equation>- 5\sqrt{5}.</equation>

**解析:**作拉格朗日函数<equation>L ( x,y,z,\lambda) = x y+2 y z+\lambda \left( x^{2}+y^{2}+z^{2}-1 0 \right)</equation>，其中<equation>\lambda</equation>为参数.令<equation>\left[ L _ {x} ^ {\prime} = y + 2 \lambda x = 0, \right.</equation><equation>\left| L _ {y} ^ {\prime} = x + 2 z + 2 \lambda y = 0, \right.</equation><equation>L _ {z} ^ {\prime} = 2 y + 2 \lambda z = 0,</equation><equation>\left[ L _ {\lambda} ^ {\prime} = x ^ {2} + y ^ {2} + z ^ {2} - 1 0 = 0. \right.</equation>解得所有可能的最值点为<equation>(1, -\sqrt{5}, 2), (1, \sqrt{5}, 2), (-1, \sqrt{5}, -2), (-1, -\sqrt{5}, -2), (-2\sqrt{2}, 0, \sqrt{2}), (2\sqrt{2}, 0, -\sqrt{2})</equation>.代入<equation>u</equation>的表达式中得，<equation>u (1, - \sqrt {5}, 2) = u (- 1, \sqrt {5}, - 2) = - 5 \sqrt {5},</equation><equation>u (1, \sqrt {5}, 2) = u (- 1, - \sqrt {5}, - 2) = 5 \sqrt {5},</equation><equation>u \left(- 2 \sqrt {2}, 0, \sqrt {2}\right) = u \left(2 \sqrt {2}, 0, - \sqrt {2}\right) = 0.</equation>因此，所求最大值为<equation>5\sqrt{5}</equation>，最小值为<equation>-5\sqrt{5}</equation>.

---

**2009年第15题 | 解答题 | 10分**

15. (本题满分9分）

求二元函数<equation>f ( x,y)=x^{2}(2+y^{2})+y\ln y</equation>的极值.

**答案:**(15)<equation>f ( x,y )</equation>在点<equation>\left( 0,\frac{1} {\mathrm{e}} \right)</equation>处取得极小值<equation>f \left( 0,\frac{1} {\mathrm{e}} \right)=-\frac{1} {\mathrm{e}}.</equation>

**解析:**解 令<equation>\left\{ \begin{array}{l l} f_{x}^{\prime}(x,y)=2 x(2+y^{2})=0, \\ f_{y}^{\prime}(x,y)=2 x^{2} y+\ln y+1=0, \end{array} \right.</equation>解得驻点为<equation>\left( 0, \frac{1} {\mathrm{e}} \right). f(x,y)</equation>的二阶偏导数为<equation>f_{xx}^{\prime \prime}(x,y)=2(2+y^{2}),</equation><equation>f_{xy}^{\prime \prime}(x,y)=4 x y,</equation><equation>f_{yy}^{\prime \prime}(x,y)=2 x^{2}+\frac{1}{y}.</equation>于是<equation>A=f_{xx}^{\prime \prime}\left( 0, \frac{1} {\mathrm{e}} \right)=2\left( 2+\frac{1} {\mathrm{e}^{2}} \right),</equation><equation>B=f_{xy}^{\prime \prime}\left( 0, \frac{1} {\mathrm{e}} \right)=0,</equation><equation>C=f_{yy}^{\prime \prime}\left( 0, \frac{1} {\mathrm{e}} \right)=\mathrm{e}.</equation>由于<equation>AC-B^{2}>0, A>0,</equation>故<equation>f(x,y)</equation>在点<equation>\left( 0, \frac{1} {\mathrm{e}} \right)</equation>处取得极小值<equation>f\left( 0, \frac{1} {\mathrm{e}} \right)=-\frac{1} {\mathrm{e}}.</equation>

---


#### 全微分的概念与计算

**2023年第12题 | 填空题 | 5分**

12. 已知函数 f(x,y)满足<equation>\mathrm{d} f(x,y)=\frac{x\mathrm{d} y-y\mathrm{d} x}{x^{2}+y^{2}}, f(1,1)=\frac{\pi}{4}</equation>，则 f<equation>(\sqrt{3},3)=</equation>___.

**答案:**##<equation>\frac{\pi}{3}</equation>

**解析:**解 由<equation>\mathrm{d}f(x,y)=\frac{x\mathrm{d}y-y\mathrm{d}x}{x^{2}+y^{2}}</equation>可知，<equation>f_{x}^{\prime}(x,y)=\frac{-y}{x^{2}+y^{2}},f_{y}^{\prime}(x,y)=\frac{x}{x^{2}+y^{2}}.</equation>于是，当<equation>y > 0</equation>时，<equation>f (x, y) = \int f _ {x} ^ {\prime} (x, y) \mathrm {d} x = \int \frac {- y}{x ^ {2} + y ^ {2}} \mathrm {d} x = - \int \frac {\mathrm {d} \left(\frac {x}{y}\right)}{1 + \left(\frac {x}{y}\right) ^ {2}} = - \arctan \frac {x}{y} + \varphi (y),</equation>其中<equation>\varphi(y)</equation>为关于 y的一元函数.实际上，<equation>\varphi(y)=f(0,y).</equation>对 f(x,y）=-arctan<equation>\frac{x}{y}+\varphi(y)</equation>关于 y求偏导数可得<equation>f _ {y} ^ {\prime} (x, y) = - \frac {- \frac {x}{y ^ {2}}}{1 + \left(\frac {x}{y}\right) ^ {2}} + \varphi^ {\prime} (y) = \frac {x}{x ^ {2} + y ^ {2}} + \varphi^ {\prime} (y).</equation>比较可得<equation>\varphi^{\prime}(y)=0</equation>，从而当 y > 0时，<equation>\varphi(y)=C,f(x,y)=-\arctan \frac{x}{y}+C</equation>，其中 C为待定常数.

由<equation>f(1,1)=\frac{\pi}{4}</equation>可得，<equation>\frac{\pi}{4}=-\frac{\pi}{4}+C</equation>，解得 C<equation>=\frac{\pi}{2}.</equation>因此，<equation>f(x,y)=-\arctan \frac{x}{y}+\frac{\pi}{2}.</equation>进一步可得<equation>f (\sqrt {3}, 3) = - \arctan \frac {1}{\sqrt {3}} + \frac {\pi}{2} = \frac {\pi}{2} - \frac {\pi}{6} = \frac {\pi}{3}.</equation>

---

**2021年第4题 | 选择题 | 5分 | 答案: C**

4. 设函数 f(x,y)可微，且<equation>f ( x+1, \mathrm{e}^{x} )=x ( x+1 )^{2}, f ( x, x^{2} )=2 x^{2} \ln x</equation>，则<equation>\mathrm{d} f ( 1, 1 )=</equation>(    )

A.<equation>\mathrm{d} x+\mathrm{d} y</equation>B.<equation>\mathrm{d} x-\mathrm{d} y</equation>C.<equation>\mathrm{d} y</equation>D.<equation>-\mathrm{d} y</equation>

答案: C

**解析:**根据全微分的定义，<equation>\mathrm {d} f (1, 1) = f _ {1} ^ {\prime} (1, 1) \mathrm {d} x + f _ {2} ^ {\prime} (1, 1) \mathrm {d} y.</equation>对<equation>f ( x+1,\mathrm{e}^{x} )=x ( x+1 )^{2}, f ( x,x^{2} )=2 x^{2} \ln x</equation>两端均关于 x求导，可得<equation>f _ {1} ^ {\prime} \left(x + 1, \mathrm {e} ^ {x}\right) + f _ {2} ^ {\prime} \left(x + 1, \mathrm {e} ^ {x}\right) \cdot \mathrm {e} ^ {x} = (x + 1) ^ {2} + x \cdot 2 (x + 1) = (x + 1) (3 x + 1).</equation><equation>f _ {1} ^ {\prime} \left(x, x ^ {2}\right) + f _ {2} ^ {\prime} \left(x, x ^ {2}\right) \cdot 2 x = 4 x \ln x + 2 x ^ {2} \cdot \frac {1}{x} = 2 x \left(2 \ln x + 1\right).</equation>在（1）式中令<equation>x=0</equation>，可得<equation>f_{1}^{\prime}(1,1)+f_{2}^{\prime}(1,1)=1.</equation>在（2）式中令<equation>x=1</equation>，可得<equation>f_{1}^{\prime}(1,1)+ 2 f_{2}^{\prime}(1,1)=2.</equation>联立两式解得<equation>f_{1}^{\prime}(1,1)=0,f_{2}^{\prime}(1,1)=1.</equation>因此，<equation>\mathrm{d}f(1,1)=\mathrm{d}y.</equation>应选C.

---

**2020年第9题 | 填空题 | 4分**

9. 设<equation>z=\arctan[xy+\sin(x+y)]</equation>，则<equation>\mathrm{d}z|_{(0,\pi)}=</equation>___.

**答案:**<equation>(\pi - 1) \mathrm {d} x - \mathrm {d} y.</equation>

**解析:**根据链式法则，<equation>\frac{\partial z}{\partial x}=\frac{y+\cos(x+y)}{1+\left[ x y+\sin(x+y)\right]^{2}},</equation><equation>\frac{\partial z}{\partial y}=\frac{x+\cos(x+y)}{1+\left[ x y+\sin(x+y)\right]^{2}}.</equation>代入<equation>x=0,y=\pi</equation>，可得<equation>\frac{\partial z}{\partial x}\bigg|_{(0,\pi)}=\pi-1, \frac{\partial z}{\partial y}\bigg|_{(0,\pi)}=-1.</equation>因此，<equation>\mathrm{d}z\bigg|_{(0,\pi)}=(\pi-1)\mathrm{d}x-\mathrm{d}y.</equation>

---

**2017年第12题 | 填空题 | 4分**

12. 设函数<equation>f(x,y)</equation>具有一阶连续偏导数，且<equation>\mathrm{d} f(x,y)=y \mathrm{e}^{y} \mathrm{d} x+x(1+y) \mathrm{e}^{y} \mathrm{d} y,f(0,0)=0</equation>，则<equation>f(x,y)=</equation>___

**答案:**##<equation>x y \mathrm{e}^{y}.</equation>

**解析:**由于<equation>\mathrm {d} f (x, y) = y \mathrm {e} ^ {y} \mathrm {d} x + x (1 + y) \mathrm {e} ^ {y} \mathrm {d} y,</equation>故<equation>f_x^{\prime}(x,y) = y\mathrm{e}^{y}, f_y^{\prime}(x,y) = x(1 + y)\mathrm{e}^{y}.</equation>对<equation>f_{x}^{\prime}(x,y)</equation>关于 x积分，得<equation>f (x, y) = \int f _ {x} ^ {\prime} (x, y) \mathrm {d} x = \int y \mathrm {e} ^ {y} \mathrm {d} x = x y \mathrm {e} ^ {y} + \varphi (y),</equation>其中<equation>\varphi(y)</equation>为关于 y的一元函数.

对<equation>x y \mathrm{e}^{y}+\varphi(y)</equation>关于y求偏导数，得<equation>\frac {\partial \left[ x y \mathrm {e} ^ {y} + \varphi (y) \right]}{\partial y} = x \mathrm {e} ^ {y} + x y \mathrm {e} ^ {y} + \varphi^ {\prime} (y) = x (1 + y) \mathrm {e} ^ {y} + \varphi^ {\prime} (y).</equation>与<equation>f_{y}^{\prime}(x,y)</equation>比较，得<equation>\varphi^{\prime}(y) = 0</equation>，故<equation>\varphi(y)\equiv C</equation>，其中C为常数.

代入<equation>x = 0</equation>，<equation>y = 0</equation>，得<equation>f(0,0) = 0 + C.</equation>于是，<equation>C = 0.</equation>因此，<equation>f ( x,y)= x y \mathrm{e}^{y}.</equation>

---

**2016年第11题 | 填空题 | 4分**

11. 设函数 f(u,v) 可微，z=z(x,y) 由方程<equation>( x+1 ) z-y^{2}=x^{2} f ( x-z,y )</equation>确定，则<equation>\mathrm{d} z |_{(0,1)}=</equation>___

**答案:**## dx + 2dy.

**解析:**（法一）对已知方程两端分别关于 x，y求偏导数，可得<equation>z + (x + 1) \frac {\partial z}{\partial x} = 2 x f (x - z, y) + x ^ {2} \left[ f _ {1} ^ {\prime} (x - z, y) \cdot \left(1 - \frac {\partial z}{\partial x}\right) \right].</equation><equation>(x + 1) \frac {\partial z}{\partial y} - 2 y = x ^ {2} \left[ f _ {1} ^ {\prime} (x - z, y) \cdot \left(- \frac {\partial z}{\partial y}\right) + f _ {2} ^ {\prime} (x - z, y) \right].</equation>将（x,y）=（0,1）代入已知方程，可得 z-1=0，从而 z(0,1)=1.再将（x,y,z）=（0,1,1）代入（1）、（2）两式，可得<equation>\frac{\partial z}{\partial x}\bigg|_{(0,1)}=-1, \frac{\partial z}{\partial y}\bigg|_{(0,1)}=2.</equation>因此，<equation>\mathrm{d} z \bigg|_{(0,1)}=-\mathrm{d} x+2 \mathrm{d} y</equation><equation>\mathrm {d} z \mid_ {(0, 1)} = - \mathrm {d} x + 2 \mathrm {d} y.</equation>（法二）对已知方程两端微分，可得<equation>\mathrm{d}[(x+1)z]-\mathrm{d}(y^{2})=\mathrm{d}[x^{2}f(x-z,y)]</equation>.进一步可得，<equation>\begin{aligned} (x + 1) \mathrm {d} z + z \mathrm {d} x - 2 y \mathrm {d} y &= f (x - z, y) \mathrm {d} \left(x ^ {2}\right) + x ^ {2} \mathrm {d} \left[ f (x - z, y) \right] \\ &= 2 x f (x - z, y) \mathrm {d} x + x ^ {2} \mathrm {d} \left[ f (x - z, y) \right]. \end{aligned}</equation>将（x,y）=（0,1）代入已知方程，可得 z-1=0，从而 z（0,1）=1.代入上式可得<equation>\mathrm {d} z + \mathrm {d} x - 2 \mathrm {d} y = 0,</equation>即<equation>\mathrm{d}z\mid_{(0,1)} = -\mathrm{d}x + 2\mathrm{d}y.</equation>

---

**2015年第11题 | 填空题 | 4分**

11. 若函数<equation>z = z(x,y)</equation>由方程<equation>\mathrm{e}^{x+2y+3z} + xyz = 1</equation>确定，则<equation>\mathrm{d}z|_{(0,0)} =</equation>___

**答案:**<equation>- \frac {1}{3} \mathrm {d} x - \frac {2}{3} \mathrm {d} y.</equation>

**解析:**解下面我们分别用上述三种方法解本题.

（法一）对原方程两端分别关于 x,y求偏导数，可得<equation>\mathrm {e} ^ {x + 2 y + 3 z} \left(1 + 3 \frac {\partial z}{\partial x}\right) + y z + x y \frac {\partial z}{\partial x} = 0.</equation><equation>\mathrm {e} ^ {x + 2 y + 3 z} \left(2 + 3 \frac {\partial z}{\partial y}\right) + x z + x y \frac {\partial z}{\partial y} = 0.</equation>当<equation>x=0,y=0</equation>时，由原方程知<equation>\mathrm{e}^{3 z}=1</equation>，故<equation>z(0,0)=0</equation>代入（1）式得<equation>\frac{\partial z}{\partial x}=-\frac{1}{3}</equation>代入（2）式得<equation>\frac{\partial z}{\partial y}=-\frac{2}{3}.</equation>因此，<equation>\mathrm{d}z\mid_{(0,0)} = -\frac{1}{3}\mathrm{d}x - \frac{2}{3}\mathrm{d}y.</equation>（法二）对原方程两端微分，可得<equation>\mathrm{d}\left(\mathrm{e}^{x + 2y + 3z} + xyz\right) = 0</equation>，展开得<equation>\mathrm {e} ^ {x + 2 y + 3 z} \left(\mathrm {d} x + 2 \mathrm {d} y + 3 \mathrm {d} z\right) + y z \mathrm {d} x + x z \mathrm {d} y + x y \mathrm {d} z = 0.</equation>当<equation>x = 0, y = 0</equation>时，由原方程知<equation>\mathrm{e}^{3z} = 1</equation>，故<equation>z(0,0) = 0.</equation>代入（3）式得<equation>\mathrm {d} x + 2 \mathrm {d} y + 3 \mathrm {d} z = 0,</equation>即<equation>\mathrm{d}z\mid_{(0,0)} = -\frac{1}{3}\mathrm{d}x - \frac{2}{3}\mathrm{d}y.</equation>（法三）当<equation>x = 0, y = 0</equation>时，由原方程知<equation>\mathrm{e}^{3z} = 1</equation>，故<equation>z(0,0) = 0.</equation>令<equation>F ( x, y, z) = \mathrm{e}^{x+2 y+3 z} + x y z - 1</equation>，则由隐函数存在定理知，<equation>\left. \frac {\partial z}{\partial x} \right| _ {(0, 0)} = - \left. \frac {F _ {x} ^ {\prime}}{F _ {z} ^ {\prime}} \right| _ {(0, 0, 0)} = - \left. \frac {\mathrm {e} ^ {x + 2 y + 3 z} + y z}{3 \mathrm {e} ^ {x + 2 y + 3 z} + x y} \right| _ {(0, 0, 0)} = - \frac {1}{3},</equation><equation>\left. \frac {\partial z}{\partial y} \right| _ {(0, 0)} = - \left. \frac {F _ {y} ^ {\prime}}{F _ {z} ^ {\prime}} \right| _ {(0, 0, 0)} = - \left. \frac {2 \mathrm {e} ^ {x + 2 y + 3 z} + x z}{3 \mathrm {e} ^ {x + 2 y + 3 z} + x y} \right| _ {(0, 0, 0)} = - \frac {2}{3}.</equation>因此，<equation>\mathrm{d}z\mid_{(0,0)} = -\frac{1}{3}\mathrm{d}x - \frac{2}{3}\mathrm{d}y.</equation>

---

**2012年第11题 | 填空题 | 4分**

11. 设连续函数<equation>z=f(x,y)</equation>满足<equation>\lim_{ \begin{array}{l} x\to 0 \\ y\to 1 \end{array} } \frac{f(x,y)-2x+y-2} {\sqrt{x^{2}+(y-1)^{2}}}=0</equation>，则<equation>\mathrm{d} z|_{(0,1)}=</equation>___

**答案:**## 2dx-dy.

**解析:**解 由于<equation>\lim_{x\to 0}\frac{f(x,y)-2x+y-2}{\sqrt{x^2+(y-1)^2}} = 0</equation>，故<equation>\lim_{y\to 0}\left[f(x,y)-2x+y-2\right] = 0.</equation>又由<equation>f ( x,y )</equation>在点（0,1）处连续可知，<equation>f ( 0,1 )=\lim_{x\to 0}\lim_{y\to 1} f ( x,y)=\lim_{x\to 0}\lim_{y\to 1} ( 2 x-y+2 )=1</equation>，故<equation>f ( 0,1 )=1.</equation>代入题给条件，可得<equation>\lim _ {\substack {x \rightarrow 0 \\ y \rightarrow 1}} \frac {f (x , y) - f (0 , 1) - 2 x + (y - 1)}{\sqrt {x ^ {2} + (y - 1) ^ {2}}} = 0.</equation>因此，由函数<equation>f ( x,y )</equation>可微的定义可知，<equation>f ( x,y )</equation>在点(0,1)处可微且<equation>\frac{\partial f}{\partial x}\bigg|_{(0,1)} = 2,\frac{\partial f}{\partial y}\bigg|_{(0,1)} = -1,</equation><equation>\mathrm{d}z\mid_{(0,1)} = 2\mathrm{d}x - \mathrm{d}y.</equation>本题也可以直接计算<equation>\frac{\partial f}{\partial x}\bigg|_{(0,1)}, \frac{\partial f}{\partial y}\bigg|_{(0,1)}</equation>.

在等式<equation>\lim_{x\to 0}\frac{f(x,y)-2x+y-2}{\sqrt{x^2+(y-1)^2}} = 0</equation>中分别令<equation>y = 1</equation>，<equation>x = 0</equation>可得，<equation>\lim _ {x \rightarrow 0} \frac {f (x , 1) - 2 x - 1}{| x |} = 0, \quad \lim _ {y \rightarrow 1} \frac {f (0 , y) + y - 2}{| y - 1 |} = 0.</equation>于是，<equation>\lim _ {x \rightarrow 0} \frac {f (x , 1) - 2 x - 1}{x} = \lim _ {x \rightarrow 0} \frac {f (x , 1) - 2 x - 1}{| x |} \cdot \frac {| x |}{x} = 0.</equation>同理可得<equation>\lim_{y\rightarrow 1}\frac{f(0,y)+y-2}{y-1}=0.</equation>从而<equation>\lim_{x\rightarrow 0}\frac{f(x,1)-1}{x}=2, \lim_{y\rightarrow 1}\frac{f(0,y)-1}{y-1}=-1.</equation>又因为 f(0,1)=1，所以<equation>\left. \frac {\partial f}{\partial x} \right| _ {(0, 1)} = \lim _ {x \rightarrow 0} \frac {f (x , 1) - 1}{x} = 2, \quad \left. \frac {\partial f}{\partial y} \right| _ {(0, 1)} = \lim _ {y \rightarrow 1} \frac {f (0 , y) - 1}{y - 1} = - 1.</equation>

---

**2011年第10题 | 填空题 | 4分**

10. 设函数<equation>z=\left(1+\frac{x}{y}\right)^{\frac{x}{y}}</equation>，则<equation>\mathrm{d}z|_{(1,1)}=</equation>___

**答案:**(1 + 2ln2) (dx - dy).

**解析:**解<equation>z = \mathrm{e}^{\frac{x}{y}\ln(1 + \frac{x}{y})}</equation>.根据链式法则，<equation>\begin{array}{l} \frac {\partial z}{\partial x} = \left(1 + \frac {x}{y}\right) ^ {\frac {x}{y}} \left[ \frac {1}{y} \ln \left(1 + \frac {x}{y}\right) + \frac {x}{y (x + y)} \right], \\ \frac {\partial z}{\partial y} = - \left(1 + \frac {x}{y}\right) ^ {\frac {x}{y}} \left[ \frac {x}{y ^ {2}} \ln \left(1 + \frac {x}{y}\right) + \frac {x ^ {2}}{y ^ {2} (x + y)} \right]. \\ \mathrm {n} 2, \frac {\partial z}{\partial y} \Big | _ {(1, 1)} = - (1 + 2 \ln 2), \mathrm {d} z \Big | _ {(1, 1)} = (1 + 2 \ln 2) \\ \end{array}</equation>因此，<equation>\frac{\partial z}{\partial x}\bigg|_{(1,1)} = 1 + 2\ln 2,\frac{\partial z}{\partial y}\bigg|_{(1,1)} = -(1 + 2\ln 2),\mathrm{d}z\bigg|_{(1,1)} = (1 + 2\ln 2)(\mathrm{d}x - \mathrm{d}y).</equation>

---


#### 二重积分的概念与性质

**2016年第3题 | 选择题 | 4分 | 答案: B**

3. 设<equation>J_{i}=\iint_{D_{i}} \sqrt[3]{x-y}\mathrm{d}x\mathrm{d}y(i=1,2,3)</equation>，其中<equation>D_{1}=\{(x,y)\mid 0\leqslant x\leqslant 1,0\leqslant y\leqslant 1\}</equation><equation>D_{2}=\{(x,y)\mid 0\leqslant x\leqslant 1,0\leqslant y\leqslant \sqrt{x}\}</equation><equation>D_{3}=\{(x,y)\mid 0\leqslant x\leqslant 1,x^{2}\leqslant y\leqslant 1</equation>则（    ）

A.<equation>J_{1}<J_{2}<J_{3}</equation>B.<equation>J_{3}<J_{1}<J_{2}</equation>C.<equation>J_{2}<J_{3}<J_{1}</equation>D.<equation>J_{2}<J_{1}<J_{3}</equation>

答案: B

**解析:**解如图所示，<equation>D_{1}=D_{2}\cup D_{2}^{\prime}=D_{3}\cup D_{3}^{\prime}.</equation>在<equation>D_{2}^{\prime}</equation>上，由于<equation>x-y<0,\sqrt[3]{x-y}<0</equation>，故<equation>\iint_{D_{2}^{\prime}} \sqrt[3]{x-y}\mathrm{d}x\mathrm{d}y<0.</equation>在<equation>D_{3}^{\prime}</equation>上，由于<equation>x-y>0,\sqrt[3]{x-y}>0</equation>，故<equation>\iint_{D_{3}^{\prime}} \sqrt[3]{x-y}\mathrm{d}x\mathrm{d}y>0.</equation>因此，<equation>J _ {1} - J _ {2} = \iint_ {D _ {1} \backslash D _ {2}} \sqrt [ 3 ]{x - y} \mathrm {d} x \mathrm {d} y = \iint_ {D _ {2} ^ {\prime}} \sqrt [ 3 ]{x - y} \mathrm {d} x \mathrm {d} y < 0,</equation><equation>J _ {1} - J _ {3} = \iint_ {D _ {1} \backslash D _ {3}} \sqrt [ 3 ]{x - y} \mathrm {d} x \mathrm {d} y = \iint_ {D _ {3} ^ {\prime}} \sqrt [ 3 ]{x - y} \mathrm {d} x \mathrm {d} y > 0.</equation>综上所述，<equation>J_{1} < J_{2}, J_{1} > J_{3}</equation>，即<equation>J_{3} < J_{1} < J_{2}.</equation>应选B.

---

**2013年第3题 | 选择题 | 4分 | 答案: B**

3. 设<equation>D_{k}</equation>是圆域<equation>D=\{(x,y)\mid x^{2}+y^{2}\leqslant 1\}</equation>位于第 k象限的部分.记<equation>I_{k}=\iint_{D_{k}}(y-x)\mathrm{d}x\mathrm{d}y(k=1,2,3,4)</equation>，则（    )

A.<equation>I_{1}>0</equation>B.<equation>I_{2}>0</equation>C.<equation>I_{3}>0</equation>D.<equation>I_{4}>0</equation>

答案: B

**解析:**解（法一）由于在第一象限内 x > 0，y > 0，第二象限内 x < 0，y > 0，第三象限内 x < 0， y < 0，第四象限内 x > 0，y < 0，故被积函数 y - x在第二象限内恒大于零，从而<equation>\iint_{D_{2}}(y-x)\mathrm{d}x\mathrm{d}y>0.</equation>应选B.

（法二）在极坐标系下计算<equation>I_{k}(k = 1,2,3,4).</equation><equation>\begin{array}{l} I _ {k} \stackrel {\text {极 坐 标}} {=} \int_ {\frac {(k - 1) \pi}{2}} ^ {\frac {k \pi}{2}} (\sin \theta - \cos \theta) \mathrm {d} \theta \int_ {0} ^ {1} r ^ {2} \mathrm {d} r = \frac {1}{3} \int_ {\frac {(k - 1) \pi}{2}} ^ {\frac {k \pi}{2}} (\sin \theta - \cos \theta) \mathrm {d} \theta \\ = - \frac {\left(\sin \theta + \cos \theta\right)}{3} \Bigg | _ {\frac {(k - 1) \pi}{2}} ^ {\frac {k \pi}{2}}. \\ \end{array}</equation>分别求得<equation>I _ {1} = 0, \quad I _ {2} = \frac {2}{3}, \quad I _ {3} = 0, \quad I _ {4} = - \frac {2}{3}.</equation><equation>I_{2} > 0</equation>应选B.

---


#### 二重积分的综合与应用

**2014年第10题 | 填空题 | 4分**

10. 设 D 是由曲线<equation>xy+1=0</equation>与直线<equation>y+x=0</equation>及<equation>y=2</equation>围成的有界区域，则 D 的面积为 ___.

**答案:**<equation>\frac {3}{2} - \ln 2.</equation>

**解析:**（法一）区域D如图（a）所示.将D写为Y型区域，<equation>D = \left\{(x, y) \mid - y \leqslant x \leqslant - \frac {1}{y}, 1 \leqslant y \leqslant 2 \right\}.</equation>因此，<equation>D</equation>的面积<equation>= \iint_{D} \mathrm{d}x \mathrm{d}y = \int_{1}^{2} \mathrm{d}y \int_{-y}^{-\frac{1}{y}} \mathrm{d}x = \int_{1}^{2} \left(-\frac{1}{y} + y\right) \mathrm{d}y = -\ln y \left|_{1}^{2} + \frac{y^{2}}{2}\right|_{1}^{2} = \frac{3}{2} - \ln 2.</equation>（法二）如图（b）所示，将<equation>D</equation>分为两个X型区域<equation>D_{1}, D_{2}</equation>.<equation>D _ {1} = \left\{(x, y) \mid - x \leqslant y \leqslant 2, - 2 \leqslant x \leqslant - 1 \right\},</equation><equation>D _ {2} = \left\{(x, y) \mid - \frac {1}{x} \leqslant y \leqslant 2, - 1 \leqslant x \leqslant - \frac {1}{2} \right\}.</equation>因此，<equation>\begin{array}{l} D \text {的 面 积} = \iint_ {D} \mathrm {d} x \mathrm {d} y = \iint_ {D _ {1}} \mathrm {d} x \mathrm {d} y + \iint_ {D _ {2}} \mathrm {d} x \mathrm {d} y = \int_ {- 2} ^ {- 1} \mathrm {d} x \int_ {- x} ^ {2} \mathrm {d} y + \int_ {- 1} ^ {- \frac {1}{2}} \mathrm {d} x \int_ {- \frac {1}{x}} ^ {2} \mathrm {d} y \\ = \int_ {- 2} ^ {- 1} (2 + x) \mathrm {d} x + \int_ {- 1} ^ {- \frac {1}{2}} \left(2 + \frac {1}{x}\right) \mathrm {d} x = \frac {1}{2} + 1 + \ln \frac {1}{2} = \frac {3}{2} - \ln 2. \\ \end{array}</equation>

---

**2012年第12题 | 填空题 | 4分**

12. 由曲线<equation>y=\frac{4}{x}</equation>和直线<equation>y=x</equation>及<equation>y=4x</equation>在第一象限中围成的平面图形的面积为 ___

**答案:**## 4ln 2.

**解析:**解 D为由曲线<equation>y=\frac{4}{x}</equation>和直线 y=x及 y=4x在第一象限中围成的平面区域.由二重积分的几何意义知，所求面积为<equation>\iint\limits_{D}\mathrm{d}x\mathrm{d}y.</equation>先求出这三条曲线在第一象限中的交点，分别为（1，4），（2，2）.

(a)

(b)

（法一）如图（a）所示，将区域<equation>D</equation>划分为两个X型区域.<equation>D _ {1} = \left\{(x, y) \mid x \leqslant y \leqslant 4 x, 0 \leqslant x \leqslant 1 \right\}, \quad D _ {2} = \left\{(x, y) \mid x \leqslant y \leqslant \frac {4}{x}, 1 \leqslant x \leqslant 2 \right\}.</equation>因此，<equation>\begin{array}{l} D \text {的 面 积} = \iint_ {D} \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {x} ^ {4 x} \mathrm {d} y + \int_ {1} ^ {2} \mathrm {d} x \int_ {x} ^ {\frac {4}{x}} \mathrm {d} y = \int_ {0} ^ {1} 3 x \mathrm {d} x + \int_ {1} ^ {2} \left(\frac {4}{x} - x\right) \mathrm {d} x \\ = \frac {3}{2} + 4 \ln 2 - \frac {3}{2} = 4 \ln 2. \\ \end{array}</equation>（法二）如图（b）所示，将区域<equation>D</equation>划分为两个Y型区域.<equation>D _ {1} = \left\{(x, y) \mid \frac {y}{4} \leqslant x \leqslant y, 0 \leqslant y \leqslant 2 \right\}, \quad D _ {2} = \left\{(x, y) \mid \frac {y}{4} \leqslant x \leqslant \frac {4}{y}, 2 \leqslant y \leqslant 4 \right\}.</equation>因此，<equation>\begin{array}{l} D \text {的 面 积} = \iint_ {D} \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {2} \mathrm {d} y \int_ {\frac {y}{4}} ^ {y} \mathrm {d} x + \int_ {2} ^ {4} \mathrm {d} y \int_ {\frac {y}{4}} ^ {\frac {4}{y}} \mathrm {d} x = \int_ {0} ^ {2} \frac {3}{4} y \mathrm {d} y + \int_ {2} ^ {4} \left(\frac {4}{y} - \frac {y}{4}\right) \mathrm {d} y \\ = \frac {3}{2} + 4 \ln 2 - \frac {3}{2} = 4 \ln 2. \\ \end{array}</equation>

---

**2011年第19题 | 解答题 | 10分**

19. (本题满分10分)

设函数<equation>f(x)</equation>在区间[0,1]上具有连续导数，<equation>f(0) = 1</equation>，且满足<equation>\iint_ {D _ {t}} f ^ {\prime} (x + y) \mathrm {d} x \mathrm {d} y = \iint_ {D _ {t}} f (t) \mathrm {d} x \mathrm {d} y, \text {其 中} D _ {t} = \{(x, y) \mid 0 \leqslant y \leqslant t - x, 0 \leqslant x \leqslant t \} (0 < t \leqslant 1).</equation>求 f(x)的表达式.

**答案:**<equation>(1 9) f (x) = \frac {4}{(2 - x) ^ {2}}, 0 \leqslant x \leqslant 1.</equation>

**解析:**解<equation>\begin{array}{l} \iint_ {D _ {t}} f ^ {\prime} (x + y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {t} \mathrm {d} x \int_ {0} ^ {t - x} f ^ {\prime} (x + y) \mathrm {d} y \xlongequal {u = x + y} \int_ {0} ^ {t} \mathrm {d} x \int_ {x} ^ {t} f ^ {\prime} (u) \mathrm {d} u \\ = \int_ {0} ^ {t} \left[ f (t) - f (x) \right] \mathrm {d} x = t f (t) - \int_ {0} ^ {t} f (x) \mathrm {d} x. \\ \end{array}</equation>另一方面，由于 f（t）中不包含变量 x,y，从而<equation>\iint_ {D _ {t}} f (t) \mathrm {d} x \mathrm {d} y = f (t) \iint_ {D _ {t}} \mathrm {d} x \mathrm {d} y = \frac {t ^ {2}}{2} f (t),</equation>其中<equation>\frac{t^{2}}{2}</equation>是<equation>D_{t}</equation>的面积，故我们得到一个新的等式，<equation>t f (t) - \int_ {0} ^ {t} f (x) \mathrm {d} x = \frac {t ^ {2}}{2} f (t).</equation>对（1）式两端关于 t求导，得<equation>f ( t )+ t f^{\prime} ( t )-f ( t )= t f ( t )+\frac{t^{2}}{2} f^{\prime} ( t )</equation>，化简得<equation>( 2-t ) f^{\prime} ( t )=2 f ( t ).</equation>这是一个可分离变量的微分方程.解该方程得，<equation>f(t)=\frac{C}{(2-t)^{2}},</equation>0 < t≤1.由 f(x)在[0,1]上连续且<equation>f(0)=1</equation>得，<equation>f (0) = \lim _ {t \rightarrow 0 ^ {+}} \frac {C}{(2 - t) ^ {2}} = \frac {C}{4} = 1.</equation>从而 C=4.

因此，<equation>f ( x ) = \frac { 4 } { ( 2 - x ) ^ { 2 } }</equation><equation>0 \leqslant x \leqslant 1.</equation>

---


### 一元函数积分学


#### 反常积分的计算

**2025年第12题 | 填空题 | 5分**

12. 设<equation>\int_ {1} ^ {+ \infty} \frac {a}{x (2 x + a)} \mathrm {d} x = \ln 2, \mathrm {则} a = \underline {{}}</equation>

**解析:**解 由于<equation>\frac{a}{x(2x+a)}=\frac{1}{x}-\frac{2}{2x+a}</equation>，故<equation>\begin{aligned} \int_ {1} ^ {+ \infty} \frac {a}{x (2 x + a)} \mathrm {d} x &= \int_ {1} ^ {+ \infty} \left(\frac {1}{x} - \frac {2}{2 x + a}\right) \mathrm {d} x = \left(\ln x - \ln | 2 x + a |\right) \Bigg | _ {1} ^ {+ \infty} = \ln \frac {x}{| 2 x + a |} \Bigg | _ {1} ^ {+ \infty} \\ &= \lim _ {x \rightarrow + \infty} \ln \frac {x}{| 2 x + a |} - \ln \frac {1}{| 2 + a |} = \ln \frac {| 2 + a |}{2}. \end{aligned}</equation>由<equation>\int_{1}^{+\infty}\frac{a}{x(2x+a)} \mathrm{d}x=\ln 2</equation>可得<equation>\ln \frac{\mid 2+a\mid}{2}=\ln 2</equation>结合<equation>\ln x</equation>是单调函数可得<equation>\frac{\mid 2+a\mid}{2}=2</equation>解得 a=2或a=-6.

当 a=-6时，<equation>\int_{1}^{+\infty}\frac{a}{x(2x+a)}\mathrm{d}x=\int_{1}^{+\infty}\frac{-3}{x(x-3)}\mathrm{d}x</equation>，此时 x=3为被积函数的瑕点，且<equation>\lim_{x\to 3^{-}}\frac{x-3}{x(x-3)}=\frac{1}{3}</equation>，由无界函数的反常积分的极限审敛法可得<equation>\int_{1}^{3}\frac{1}{x(x-3)}\mathrm{d}x</equation>发散，从而<equation>\int_{1}^{+\infty}\frac{-3}{x(x-3)}\mathrm{d}x</equation>发散.于是，应舍去 a=-6.

当<equation>a = 2</equation>时，被积函数在<equation>(1, +\infty)</equation>上没有瑕点.

因此，a=2.

---

**2024年第12题 | 填空题 | 5分**

<equation>\int_ {2} ^ {+ \infty} \frac {5}{x ^ {4} + 3 x ^ {2} - 4} \mathrm {d} x = \underline {{}}</equation>

**答案:**<equation>\frac {1}{2} \ln 3 - \frac {\pi}{8}</equation>

**解析:**解（法一）注意到<equation>x^{4}+3 x^{2}-4=(x^{2}+4)(x^{2}-1)</equation>，而<equation>(x^{2}+4)-(x^{2}-1)=5</equation>，故<equation>\frac{5}{x^{4}+3 x^{2}-4}=\frac{5}{(x^{2}+4)(x^{2}-1)}=\frac{1}{x^{2}-1}-\frac{1}{x^{2}+4}=\frac{1}{2}\left(\frac{1}{x-1}-\frac{1}{x+1}\right)-\frac{1}{x^{2}+4}.</equation>因此，<equation>\begin{aligned} \int_ {2} ^ {+ \infty} \frac {5}{x ^ {4} + 3 x ^ {2} - 4} d x &= \int_ {2} ^ {+ \infty} \left[ \frac {1}{2} \left(\frac {1}{x - 1} - \frac {1}{x + 1}\right) - \frac {1}{x ^ {2} + 4} \right] d x \\ &= \frac {1}{2} \ln \left. \frac {x - 1}{x + 1} \right| _ {2} ^ {+ \infty} - \frac {1}{2} \int_ {2} ^ {+ \infty} \frac {1}{1 + \left(\frac {x}{2}\right) ^ {2}} d \left(\frac {x}{2}\right) \\ &= - \frac {1}{2} \ln \frac {1}{3} - \frac {1}{2} \arctan \frac {x}{2} \Big | _ {2} ^ {+ \infty} = \frac {1}{2} \ln 3 - \frac {1}{2} \left(\frac {\pi}{2} - \frac {\pi}{4}\right) \\ &= \frac {1}{2} \ln 3 - \frac {\pi}{8}. \end{aligned}</equation>（法二）注意到<equation>x^{4}+3 x^{2}-4=(x^{2}+4)(x+1)(x-1)</equation>，故对<equation>\frac{5}{x^{4}+3 x^{2}-4}</equation>进行部分分式分解设<equation>\frac {5}{x ^ {4} + 3 x ^ {2} - 4} = \frac {A}{x - 1} + \frac {B}{x + 1} + \frac {C x + D}{x ^ {2} + 4}.</equation>通分并整理可得，<equation>\begin{aligned} \frac {5}{x ^ {4} + 3 x ^ {2} - 4} &= \frac {A (x + 1) \left(x ^ {2} + 4\right) + B (x - 1) \left(x ^ {2} + 4\right) + (C x + D) \left(x ^ {2} - 1\right)}{x ^ {4} + 3 x ^ {2} - 4} \\ &= \frac {(A + B + C) x ^ {3} + (A - B + D) x ^ {2} + (4 A + 4 B - C) x + 4 A - 4 B - D}{x ^ {4} + 3 x ^ {2} - 4}. \end{aligned}</equation>比较<equation>x^{3},x^{2},x</equation>的系数以及常数项可得，<equation>[ A + B + C = 0,</equation><equation>A - B + D = 0,</equation><equation>4 A + 4 B - C = 0,</equation><equation>4 A - 4 B - D = 5.</equation>(1) 式与（3）式相加并整理可得<equation>A+B=0</equation>，进一步可得 C=0.将 B=-A代人（2）式与（4）式可得<equation>\left\{\begin{array}{l l}2 A+D=0,\\ 8 A-D=5,\end{array}\right.</equation>解得<equation>\left\{\begin{array}{l l}A=\frac{1}{2},\\ B=-\frac{1}{2},\\ C=0,\\ D=-1. \end{array}\right.</equation>因此，<equation>\frac {5}{x ^ {4} + 3 x ^ {2} - 4} = \frac {1}{2} \left(\frac {1}{x - 1} - \frac {1}{x + 1}\right) - \frac {1}{x ^ {2} + 4}.</equation>其余同法一.

---

**2013年第11题 | 填空题 | 4分**

<equation>\int_ {1} ^ {+ \infty} \frac {\ln x}{(1 + x) ^ {2}} \mathrm {d} x = \underline {{}}</equation>

**解析:**<equation>\begin{aligned} \int_ {1} ^ {+ \infty} \frac {\ln x}{(1 + x) ^ {2}} \mathrm {d} x &= - \int_ {1} ^ {+ \infty} \ln x \mathrm {d} \left(\frac {1}{1 + x}\right) = - \left[ \frac {\ln x}{1 + x} \Big | _ {1} ^ {+ \infty} - \int_ {1} ^ {+ \infty} \frac {1}{x (1 + x)} \mathrm {d} x \right] \\ &= - \lim _ {x \rightarrow + \infty} \frac {\ln x}{1 + x} + \int_ {1} ^ {+ \infty} \left(\frac {1}{x} - \frac {1}{x + 1}\right) \mathrm {d} x \\ \underline {{\text {洛必达}}} - \lim _ {x \rightarrow + \infty} \frac {1}{x} + \ln \frac {x}{x + 1} \Big | _ {1} ^ {+ \infty} \\ &= 0 + \ln 1 - \ln \frac {1}{2} = \ln 2. \end{aligned}</equation>

---


#### 定积分的计算

**2025年第17题 | 解答题 | 10分**

17. 计算<equation>\int_ {0} ^ {1} \frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} \mathrm {d} x.</equation>

**答案:**#<equation>\frac{3\ln 2+\pi}{10}.</equation>

**解析:**解设<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {A}{x + 1} + \frac {B x + C}{x ^ {2} - 2 x + 2}.</equation>通分并整理可得，<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {(A + B) x ^ {2} + (B + C - 2 A) x + 2 A + C}{(x + 1) \left(x ^ {2} - 2 x + 2\right)}.</equation>比较<equation>x^{2}, x</equation>的系数以及常数项可得，<equation>A + B = 0,</equation><equation>\left\{B + C - 2 A = 0, \right.</equation><equation>2 A + C = 1.</equation>由（1）式可得<equation>B=-A</equation>.将<equation>B=-A</equation>代入（2）式可得<equation>C=3A</equation>.将<equation>C=3A</equation>代入（3）式可得<equation>5A=1</equation>，即<equation>A=\frac{1}{5}</equation>.进一步可得<equation>B=-\frac{1}{5},C=\frac{3}{5}.</equation>由此可得，<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {1}{5} \left(\frac {1}{x + 1} - \frac {x - 3}{x ^ {2} - 2 x + 2}\right).</equation>下面分别计算<equation>\int_{0}^{1}\frac{1}{x+1}\mathrm{d}x</equation>与<equation>\int_{0}^{1}\frac{x-3}{x^{2}-2x+2}\mathrm{d}x.</equation><equation>\int_ {0} ^ {1} \frac {1}{x + 1} \mathrm {d} x = \ln (x + 1) \Big | _ {0} ^ {1} = \ln 2.</equation><equation>\begin{aligned} \int_ {0} ^ {1} \frac {x - 3}{x ^ {2} - 2 x + 2} \mathrm {d} x &= \int_ {0} ^ {1} \frac {x - 1}{x ^ {2} - 2 x + 2} \mathrm {d} x - \int_ {0} ^ {1} \frac {2}{x ^ {2} - 2 x + 2} \mathrm {d} x \\ &= \frac {1}{2} \int_ {0} ^ {1} \frac {\mathrm {d} \left(x ^ {2} - 2 x + 2\right)}{x ^ {2} - 2 x + 2} - 2 \int_ {0} ^ {1} \frac {1}{1 + (x - 1) ^ {2}} \mathrm {d} x \\ &= \frac {1}{2} \ln \left(x ^ {2} - 2 x + 2\right) \left| _ {0} ^ {1} - 2 \arctan (x - 1) \right| _ {0} ^ {1} \\ &= - \frac {1}{2} \ln 2 - 2 [ 0 - \arctan (- 1) ] = - \frac {1}{2} \ln 2 - \frac {\pi}{2}. \end{aligned}</equation>因此，<equation>\int_ {0} ^ {1} \frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} \mathrm {d} x = \frac {1}{5} \left[ \ln 2 - \left(- \frac {1}{2} \ln 2 - \frac {\pi}{2}\right) \right] = \frac {3 \ln 2 + \pi}{1 0}.</equation>

---

**2022年第12题 | 填空题 | 5分**

<equation>\int_ {0} ^ {2} \frac {2 x - 4}{x ^ {2} + 2 x + 4} \mathrm {d} x = \underline {{}}</equation>

**答案:**<equation>\ln 3 - \frac {\sqrt {3}}{3} \pi .</equation>

**解析:**解注意到<equation>( x^{2}+2 x+4)^{\prime}=2 x+2</equation>，<equation>\frac{2 x-4}{x^{2}+2 x+4}=\frac{2 x+2}{x^{2}+2 x+4}</equation><equation>-\frac{6}{x^{2}+2 x+4}.</equation>因此，<equation>\begin{aligned} \int_ {0} ^ {2} \frac {2 x - 4}{x ^ {2} + 2 x + 4} d x &= \int_ {0} ^ {2} \frac {2 x + 2}{x ^ {2} + 2 x + 4} d x - 6 \int_ {0} ^ {2} \frac {1}{x ^ {2} + 2 x + 4} d x \\ &= \int_ {0} ^ {2} \frac {\mathrm {d} \left(x ^ {2} + 2 x + 4\right)}{x ^ {2} + 2 x + 4} - 2 \int_ {0} ^ {2} \frac {1}{1 + \left[ \frac {1}{\sqrt {3}} (x + 1) \right] ^ {2}} d x \\ &= \ln \left(x ^ {2} + 2 x + 4\right) \Bigg | _ {0} ^ {2} - 2 \sqrt {3} \int_ {0} ^ {2} \frac {\mathrm {d} \left[ \frac {1}{\sqrt {3}} (x + 1) \right]}{1 + \left[ \frac {1}{\sqrt {3}} (x + 1) \right] ^ {2}} \\ &= \ln 3 - 2 \sqrt {3} \arctan \frac {1}{\sqrt {3}} (x + 1) \Bigg | _ {0} ^ {2} \\ &= \ln 3 - 2 \sqrt {3} \times \left(\frac {\pi}{3} - \frac {\pi}{6}\right) = \ln 3 - \frac {\sqrt {3}}{3} \pi . \end{aligned}</equation>

---

**2021年第12题 | 填空题 | 5分**

<equation>\int_ {\sqrt {5}} ^ {5} \frac {x}{\sqrt {\left| x ^ {2} - 9 \right|}} \mathrm {d} x = \underline {{}}</equation>

**解析:**当<equation>\sqrt{5} < x < 3</equation>时，<equation>x^{2}-9<0</equation>；当 3 < x < 5时，<equation>x^{2}-9>0.</equation><equation>\begin{aligned} \int_ {\sqrt {5}} ^ {5} \frac {x}{\sqrt {| x ^ {2} - 9 |}} \mathrm {d} x &= \int_ {\sqrt {5}} ^ {3} \frac {x}{\sqrt {9 - x ^ {2}}} \mathrm {d} x + \int_ {3} ^ {5} \frac {x}{\sqrt {x ^ {2} - 9}} \mathrm {d} x \\ &= - \frac {1}{2} \int_ {\sqrt {5}} ^ {3} \frac {\mathrm {d} \left(9 - x ^ {2}\right)}{\sqrt {9 - x ^ {2}}} + \frac {1}{2} \int_ {3} ^ {5} \frac {\mathrm {d} \left(x ^ {2} - 9\right)}{\sqrt {x ^ {2} - 9}} \\ &= \left(- \frac {1}{2}\right) \times 2 \times \sqrt {9 - x ^ {2}} \left| _ {\sqrt {5}} ^ {3} + \frac {1}{2} \times 2 \times \sqrt {x ^ {2} - 9} \right| _ {3} ^ {5} \\ &= - (0 - 2) + (4 - 0) = 6. \end{aligned}</equation>

---

**2019年第11题 | 填空题 | 4分**

11. 已知函数<equation>f ( x )=\int_{1}^{x}\sqrt{1+t^{4}}\mathrm{d} t</equation>，则<equation>\int_{0}^{1} x^{2} f ( x ) \mathrm{d} x=</equation>___.

**答案:**<equation>\frac{1-2\sqrt{2}}{18}.</equation>

**解析:**（法一）利用分部积分法.

注意到 f（1）=0.<equation>\begin{aligned} \int_ {0} ^ {1} x ^ {2} f (x) \mathrm {d} x &= \frac {1}{3} \int_ {0} ^ {1} f (x) \mathrm {d} \left(x ^ {3}\right) = \frac {1}{3} \left[ x ^ {3} f (x) \left| _ {0} ^ {1} - \int_ {0} ^ {1} x ^ {3} \cdot f ^ {\prime} (x) \mathrm {d} x \right] = - \frac {1}{3} \int_ {0} ^ {1} x ^ {3} \sqrt {1 + x ^ {4}} \mathrm {d} x \right. \\ &= - \frac {1}{1 2} \int_ {0} ^ {1} \sqrt {1 + x ^ {4}} \mathrm {d} \left(x ^ {4}\right) = - \frac {1}{1 2} \cdot \frac {2}{3} \cdot \left(1 + x ^ {4}\right) ^ {\frac {3}{2}} \Bigg | _ {0} ^ {1} = \frac {1 - 2 \sqrt {2}}{1 8}. \end{aligned}</equation>（法二）交换积分次序.

将 f(x) 代入所求积分.<equation>\int_ {0} ^ {1} x ^ {2} f (x) \mathrm {d} x = \int_ {0} ^ {1} x ^ {2} \left(\int_ {1} ^ {x} \sqrt {1 + t ^ {4}} \mathrm {d} t\right) \mathrm {d} x = \int_ {0} ^ {1} x ^ {2} \mathrm {d} x \int_ {1} ^ {x} \sqrt {1 + t ^ {4}} \mathrm {d} t.</equation>写出该积分对应的二重积分的积分区域 D. 由二次积分的表达式可知，边界曲线为 t=x，t=1以及 x=0，故<equation>D = \{(x, t) \mid x \leqslant t \leqslant 1, 0 \leqslant x \leqslant 1 \}.</equation>如图所示，交换积分次序可得<equation>D = \{(x, t) \mid 0 \leqslant x \leqslant t, 0 \leqslant t \leqslant 1 \}.</equation>因此，<equation>\begin{array}{l} = - \frac {1}{3} \cdot \frac {1}{4} \int_ {0} ^ {1} \sqrt {1 + t ^ {4}} \mathrm {d} \left(t ^ {4}\right) = - \frac {1}{1 2} \cdot \frac {2}{3} \cdot \left(1 + t ^ {4}\right) ^ {\frac {3}{2}} \Bigg | _ {0} ^ {1} = \frac {1 - 2 \sqrt {2}}{1 8}. \\ \end{array}</equation>

---

**2017年第9题 | 填空题 | 4分**

9.<equation>9. \int_ {- \pi} ^ {\pi} \left(\sin^ {3} x + \sqrt {\pi^ {2} - x ^ {2}}\right) \mathrm {d} x = \underline {{}}</equation>

**解析:**由于<equation>[-\pi ,\pi ]</equation>是对称区间，且<equation>\sin^{3}x</equation>是关于x的奇函数，<equation>\sqrt{\pi^{2}-x^{2}}</equation>是关于x的偶函数，故原积分<equation>\frac{\int_{-\pi}^{\pi}\sin^{3}x\mathrm{d}x=0}{\int_{-\pi}^{\pi}\sqrt{\pi^{2}-x^{2}}\mathrm{d}x} \int_{-\pi}^{\pi}\sqrt{\pi^{2}-x^{2}}\mathrm{d}x</equation><equation>\frac{x=\pi\sin t}{2} 2\int_{0}^{\frac{\pi}{2}}\pi\cos t\cdot \pi\cos t\mathrm{d}t=\pi^{2}\int_{0}^{\frac{\pi}{2}}2\cos^{2}t\mathrm{d}t</equation><equation>= \pi^{2}\int_{0}^{\frac{\pi}{2}}(1+\cos 2t)\mathrm{d}t=\pi^{2}\times \left(\frac{\pi}{2}+0\right)=\frac{\pi^{3}}{2}.</equation>

---

**2014年第11题 | 填空题 | 4分**

11. 设<equation>\int_{0}^{a} x \mathrm{e}^{2 x} \mathrm{d} x=\frac{1}{4}</equation>，则 a=___

**解析:**由于<equation>\frac{1}{4}=\int_{0}^{a}x\mathrm{e}^{2x}\mathrm{d}x=\frac{x\mathrm{e}^{2x}}{2}\bigg|_{0}^{a}-\int_{0}^{a}\frac{\mathrm{e}^{2x}}{2}\mathrm{d}x=\frac{a}{2}\mathrm{e}^{2a}-\frac{\mathrm{e}^{2x}}{4}\bigg|_{0}^{a}=\frac{a}{2}\mathrm{e}^{2a}-\frac{\mathrm{e}^{2a}}{4}+\frac{1}{4},</equation>故<equation>\frac{a}{2}\mathrm{e}^{2a}=\frac{\mathrm{e}^{2a}}{4}</equation>因此，<equation>a=\frac{1}{2}.</equation>

---


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


#### 定积分的应用

**2024年第19题 | 解答题 | 12分**

19. (本题满分12分)

设 t>0，平面有界区域 D由曲线<equation>y=x\mathrm{e}^{-2x}</equation>与直线 x=t,x=2t及 x轴围成，D的面积为 S(t)，求 S(t)的最大值.

**答案:**<equation>\frac {1}{1 6} \ln 2 + \frac {3}{6 4}.</equation>

**解析:**解 由于<equation>x\mathrm{e}^{-2x} > 0</equation>，故区域D的面积<equation>S(t) = \int_{t}^{2t}x\mathrm{e}^{-2x}\mathrm{d}x.</equation>由变限积分的求导公式可得，<equation>S ^ {\prime} (t) = \left(\int_ {t} ^ {2 t} x \mathrm {e} ^ {- 2 x} \mathrm {d} x\right) ^ {\prime} = 2 \cdot 2 t \mathrm {e} ^ {- 4 t} - t \mathrm {e} ^ {- 2 t} = 4 t \mathrm {e} ^ {- 4 t} - t \mathrm {e} ^ {- 2 t} = t \mathrm {e} ^ {- 4 t} \left(4 - \mathrm {e} ^ {2 t}\right).</equation>解<equation>4-\mathrm{e}^{2 t}=0</equation>可得<equation>t=\ln 2</equation>.于是，当<equation>0 < t < \ln 2</equation>时，<equation>S^{\prime}(t)>0,S(t)</equation>单调增加，当<equation>t > \ln 2</equation>时，<equation>S^{\prime}(t)<0,S(t)</equation>单调减少.

因此，<equation>S ( t )</equation>的最大值在<equation>t=\ln 2</equation>时取得，最大值为<equation>S (\ln 2).</equation>下面用两种方法计算<equation>S(\ln 2).</equation>（法一）<equation>\begin{array}{l} S (\ln 2) = \int_ {\ln 2} ^ {2 \ln 2} x \mathrm {e} ^ {- 2 x} \mathrm {d} x = - \frac {1}{2} \int_ {\ln 2} ^ {2 \ln 2} x \mathrm {d} \left(\mathrm {e} ^ {- 2 x}\right) = - \frac {1}{2} \left(x \mathrm {e} ^ {- 2 x} \Big | _ {\ln 2} ^ {2 \ln 2} - \int_ {\ln 2} ^ {2 \ln 2} \mathrm {e} ^ {- 2 x} \mathrm {d} x\right) \\ = - \frac {1}{2} \left(2 \ln 2 \cdot \frac {1}{1 6} - \ln 2 \cdot \frac {1}{4} + \frac {1}{2} \mathrm {e} ^ {- 2 x} \Big | _ {\ln 2} ^ {2 \ln 2}\right) = \frac {\ln 2}{1 6} - \frac {1}{4} \left(\frac {1}{1 6} - \frac {1}{4}\right) \\ = \frac {\ln 2}{1 6} + \frac {3}{6 4}. \\ \end{array}</equation>（法二）也可以计算出<equation>S(t)</equation>的表达式再代入<equation>t = \ln 2</equation>.<equation>\begin{array}{l} S (t) = \int_ {t} ^ {2 t} x \mathrm {e} ^ {- 2 x} \mathrm {d} x = - \frac {1}{2} \int_ {t} ^ {2 t} x \mathrm {d} \left(\mathrm {e} ^ {- 2 x}\right) = - \frac {1}{2} \left(x \mathrm {e} ^ {- 2 x} \Big | _ {t} ^ {2 t} - \int_ {t} ^ {2 t} \mathrm {e} ^ {- 2 x} \mathrm {d} x\right) \\ = - \frac {1}{2} \left(2 t \mathrm {e} ^ {- 4 t} - t \mathrm {e} ^ {- 2 t} + \frac {1}{2} \mathrm {e} ^ {- 2 x} \Big | _ {t} ^ {2 t}\right) = - \frac {1}{2} \left(2 t \mathrm {e} ^ {- 4 t} - t \mathrm {e} ^ {- 2 t} + \frac {1}{2} \mathrm {e} ^ {- 4 t} - \frac {1}{2} \mathrm {e} ^ {- 2 t}\right) \\ = - \frac {1}{2} \left[ \left(2 t + \frac {1}{2}\right) \mathrm {e} ^ {- 4 t} - \left(t + \frac {1}{2}\right) \mathrm {e} ^ {- 2 t} \right]. \\ \end{array}</equation>因此，<equation>S (\ln 2) = - \frac {1}{2} \left[ \left(2 \ln 2 + \frac {1}{2}\right) \cdot \frac {1}{1 6} - \left(\ln 2 + \frac {1}{2}\right) \cdot \frac {1}{4} \right] = \frac {\ln 2}{1 6} + \frac {3}{6 4}.</equation>

---

**2023年第18题 | 解答题 | 12分**

8. (本题满分12分)

已知平面区域<equation>D=\left\{(x,y)\left|0\leqslant y\leqslant \frac{1}{x\sqrt{1+x^{2}}},x\geqslant 1\right.\right\}</equation>I. 求 D的面积;

II. 求 D绕 x轴旋转所成旋转体的体积.

**答案:**( I )<equation>\ln(\sqrt{2}+1)</equation>;

( II )<equation>\pi\left(1-\frac{\pi}{4}\right).</equation>

**解析:**（I）区域 D是由曲线<equation>y=\frac{1}{x\sqrt{1+x^{2}}}</equation>，直线 x=1以及 x轴围成的无界区域，其面积为<equation>\begin{aligned} S &= \int_ {1} ^ {+ \infty} \frac {1}{x \sqrt {1 + x ^ {2}}} \mathrm {d} x \xlongequal {x = \tan t} \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \frac {\mathrm {d} (\tan t)}{\tan t \sqrt {1 + \tan^ {2} t}} = \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \frac {\sec^ {2} t}{\tan t \sec t} \mathrm {d} t \\ &= \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \frac {\mathrm {d} t}{\sin t} = \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \frac {\mathrm {d} (- \cos t)}{1 - \cos^ {2} t} \xlongequal {u = \cos t} \int_ {\frac {\sqrt {2}}{2}} ^ {0} \frac {- \mathrm {d} u}{1 - u ^ {2}} = \frac {1}{2} \int_ {0} ^ {\frac {\sqrt {2}}{2}} \left(\frac {1}{1 - u} + \frac {1}{1 + u}\right) \mathrm {d} u \\ &= \frac {1}{2} \ln \frac {1 + u}{1 - u} \Bigg | _ {0} ^ {\frac {\sqrt {2}}{2}} = \ln (\sqrt {2} + 1). \end{aligned}</equation>（Ⅱ）由旋转体的体积公式可知，区域 D绕 x轴旋转所成旋转体的体积为<equation>\begin{aligned} V &= \int_ {1} ^ {+ \infty} \pi \left(\frac {1}{x \sqrt {1 + x ^ {2}}}\right) ^ {2} \mathrm {d} x = \pi \int_ {1} ^ {+ \infty} \frac {1}{x ^ {2} \left(1 + x ^ {2}\right)} \mathrm {d} x = \pi \int_ {1} ^ {+ \infty} \left(\frac {1}{x ^ {2}} - \frac {1}{1 + x ^ {2}}\right) \mathrm {d} x \\ &= \pi \left(- \frac {1}{x} - \arctan x\right) \Bigg | _ {1} ^ {+ \infty} = \pi \left(1 - \frac {\pi}{4}\right). \end{aligned}</equation>

---

**2021年第13题 | 填空题 | 5分**

13. 设平面区域 D 由曲线<equation>y=\sqrt{x}\sin\pi x(0\leqslant x\leqslant1)</equation>与 x轴围成，则 D绕 x轴旋转所成的旋转体的体积为 ___.

**答案:**##<equation>\frac{\pi}{4}</equation>

**解析:**（法一）根据旋转体的体积公式，<equation>\begin{array}{l} V = \pi \int_ {0} ^ {1} (\sqrt {x} \sin \pi x) ^ {2} \mathrm {d} x = \pi \int_ {0} ^ {1} x \sin^ {2} \pi x \mathrm {d} x \xlongequal {\pi x = t} \frac {1}{\pi} \int_ {0} ^ {\pi} t \sin^ {2} t \mathrm {d} t = \frac {1}{\pi} \cdot \frac {\pi}{2} \int_ {0} ^ {\pi} \sin^ {2} t \mathrm {d} t \\ = \frac {1}{2} \cdot 2 \int_ {0} ^ {\frac {\pi}{2}} \sin^ {2} t \mathrm {d} t = \frac {\pi}{4}. \\ \end{array}</equation>（法二）下面用另一种方法计算<equation>\int_{0}^{\pi} t\sin^{2}t\mathrm{d}t.</equation><equation>\begin{array}{l} \int_ {0} ^ {\pi} t \sin^ {2} t \mathrm {d} t = \int_ {0} ^ {\pi} t \cdot \frac {1 - \cos 2 t}{2} \mathrm {d} t = \frac {1}{2} \int_ {0} ^ {\pi} (t - t \cos 2 t) \mathrm {d} t = \frac {1}{2} \left(\frac {t ^ {2}}{2} \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} t \cos 2 t \mathrm {d} t\right) \\ = \frac {1}{2} \left[ \frac {\pi^ {2}}{2} - \frac {1}{2} \int_ {0} ^ {\pi} t \mathrm {d} (\sin 2 t) \right] = \frac {\pi^ {2}}{4} - \frac {1}{4} \left(t \sin 2 t \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} \sin 2 t \mathrm {d} t\right) \\ = \frac {\pi^ {2}}{4} - \frac {1}{4} \left(0 + \frac {\cos 2 t}{2} \Big | _ {0} ^ {\pi}\right) = \frac {\pi^ {2}}{4}. \\ \end{array}</equation>

---

**2020年第12题 | 填空题 | 4分**

12. 设平面区域<equation>D=\left\{(x,y)\left| \frac{x}{2}\leqslant y\leqslant \frac{1}{1+x^{2}},0\leqslant x\leqslant 1\right. \right\}</equation>，则 D绕 y轴旋转所成的旋转体的体积为 ___.

**答案:**<equation>\pi \ln 2 - \frac {\pi}{3}.</equation>

**解析:**解 由已知条件可知，区域 D由曲线<equation>y=\frac{1}{1+x^{2}},y=\frac{x}{2},x=0,x=1</equation>围成，其绕 y轴旋转一周所得旋转体的体积可看作两个旋转体的体积之差.

由旋转体的体积公式可得，所求旋转体的体积<equation>\begin{array}{l} V = 2 \pi \int_ {0} ^ {1} x \left(\frac {1}{1 + x ^ {2}} - \frac {x}{2}\right) \mathrm {d} x = 2 \pi \int_ {0} ^ {1} \left(\frac {x}{1 + x ^ {2}} - \frac {x ^ {2}}{2}\right) \mathrm {d} x \\ = 2 \pi \left[ \frac {1}{2} \ln \left(1 + x ^ {2}\right) - \frac {x ^ {3}}{6} \right] \Bigg | _ {0} ^ {1} = \pi \ln 2 - \frac {\pi}{3}. \\ \end{array}</equation>

---

**2019年第18题 | 解答题 | 10分**

18. (本题满分10分)

求曲线<equation>y=\mathrm{e}^{-x}\sin x(x\geqslant 0)</equation>与x轴之间图形的面积.

**答案:**<equation>\frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}.</equation>

**解析:**如图所示，曲线<equation>y=\mathrm{e}^{-x}\sin x(x\geqslant 0)</equation>与 x轴有无穷多个交点，<equation>x=n\pi</equation>（n为非负整数）均为曲线与 x轴的交点. 因此，该曲线与 x轴围成的平面图形在 x轴上方与 x轴下方均有无穷多部分. 计算面积时，应分别计算该平面图形位于 x轴上方部分的面积与位于 x轴下方部分的面积，再求级数和.

解（法一）注意到<equation>\mathrm{e}^{-x}</equation>恒大于零.根据定积分的几何意义，曲线位于（<equation>k\pi</equation>，<equation>( k+1)\pi</equation>）的部分与 x轴之间的图形面积等于<equation>\int_{k\pi}^{(k+1)\pi} \mathrm{e}^{-x}|\sin x|\mathrm{d}x.</equation>计算<equation>S_{n}。</equation><equation>\begin{array}{l} S _ {n} = \sum_ {k = 0} ^ {n - 1} \int_ {k \pi} ^ {(k + 1) \pi} \mathrm {e} ^ {- x} | \sin x | \mathrm {d} x \underline {{= x - k \pi}} \sum_ {k = 0} ^ {n - 1} \int_ {0} ^ {\pi} \mathrm {e} ^ {- (t + k \pi)} | \sin (t + k \pi) | \mathrm {d} t \\ = \sum_ {k = 0} ^ {n - 1} \mathrm {e} ^ {- k \pi} \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t. \\ \end{array}</equation>下面计算<equation>\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t &= - \int_ {0} ^ {\pi} \sin t \mathrm {d} \left(\mathrm {e} ^ {- t}\right) = - \left(\sin t \mathrm {e} ^ {- t} \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \cos t \mathrm {d} t\right) \\ &= \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \cos t \mathrm {d} t = - \int_ {0} ^ {\pi} \cos t \mathrm {d} \left(\mathrm {e} ^ {- t}\right) \\ &= - \cos t \mathrm {e} ^ {- t} \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t \\ &= \mathrm {e} ^ {- \pi} + 1 - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t. \end{aligned}</equation>由上式可得<equation>2\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t=\mathrm{e}^{-\pi}+1</equation>，于是<equation>\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t=\frac{1}{2}\left(\mathrm{e}^{-\pi}+1\right).</equation><equation>S = \lim _ {n \rightarrow \infty} S _ {n} = \frac {1}{2} \left(\mathrm {e} ^ {- \pi} + 1\right) \lim _ {n \rightarrow \infty} \frac {1 - \mathrm {e} ^ {- n \pi}}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} \cdot \frac {\mathrm {e} ^ {- \pi} + 1}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}.</equation>（法二）注意到<equation>\mathrm{e}^{-x}</equation>恒大于零.当<equation>x\in(2n\pi,(2n+1)\pi)</equation>时，<equation>\sin x > 0</equation>；当<equation>x\in((2n+1)\pi,</equation><equation>(2n+2)\pi)</equation>时，<equation>\sin x < 0</equation>因此，根据定积分的几何意义，曲线位于<equation>(2n\pi, (2n+1)\pi)</equation>的部分与x轴之间的图形面积等于<equation>\int_{2n\pi}^{(2n+1)\pi} \mathrm{e}^{-x}\sin x\mathrm{d}x</equation>；曲线位于<equation>((2n+1)\pi, (2n+2)\pi)</equation>的部分与x轴之间的图形面积等于<equation>-\int_{(2n+1)\pi}^{(2n+2)\pi} \mathrm{e}^{-x}\sin x\mathrm{d}x.</equation>记所求面积为 S，则<equation>S = \sum_ {n = 0} ^ {\infty} \int_ {2 n \pi} ^ {(2 n + 1) \pi} \mathrm {e} ^ {- x} \sin x \mathrm {d} x - \sum_ {n = 0} ^ {\infty} \int_ {(2 n + 1) \pi} ^ {(2 n + 2) \pi} \mathrm {e} ^ {- x} \sin x \mathrm {d} x.</equation>下面计算<equation>\int\mathrm{e}^{-x}\sin x\mathrm{d}x.</equation><equation>\begin{aligned} \int \mathrm {e} ^ {- x} \sin x \mathrm {d} x &= - \int \sin x \mathrm {d} \left(\mathrm {e} ^ {- x}\right) = - \left(\sin x \mathrm {e} ^ {- x} - \int \mathrm {e} ^ {- x} \cos x \mathrm {d} x\right) \\ &= - \sin x \mathrm {e} ^ {- x} + \int \mathrm {e} ^ {- x} \cos x \mathrm {d} x = - \sin x \mathrm {e} ^ {- x} - \int \cos x \mathrm {d} \left(\mathrm {e} ^ {- x}\right) \\ &= - \sin x \mathrm {e} ^ {- x} - \left(\cos x \mathrm {e} ^ {- x} + \int \mathrm {e} ^ {- x} \sin x \mathrm {d} x\right). \end{aligned}</equation>由上式可得<equation>2\int \mathrm{e}^{-x}\sin x\mathrm{d}x = -\mathrm{e}^{-x}(\sin x + \cos x) - C</equation>，于是<equation>\int \mathrm {e} ^ {- x} \sin x \mathrm {d} x = - \frac {1}{2} \left[ \mathrm {e} ^ {- x} (\sin x + \cos x) + C \right],</equation>其中 C为任意常数.

因此，<equation>\begin{array}{l} S = \sum_ {n = 0} ^ {\infty} \left[ - \frac {1}{2} \mathrm {e} ^ {- x} (\sin x + \cos x) \right] \left| _ {2 n \pi} ^ {(2 n + 1) \pi} + \sum_ {n = 0} ^ {\infty} \left[ \frac {1}{2} \mathrm {e} ^ {- x} (\sin x + \cos x) \right] \right| _ {(2 n + 1) \pi} ^ {(2 n + 2) \pi} \\ = \frac {1}{2} \sum_ {n = 0} ^ {\infty} \left[ \mathrm {e} ^ {- (2 n + 1) \pi} + \mathrm {e} ^ {- 2 n \pi} \right] + \frac {1}{2} \sum_ {n = 0} ^ {\infty} \left[ \mathrm {e} ^ {- (2 n + 2) \pi} + \mathrm {e} ^ {- (2 n + 1) \pi} \right] \\ = \frac {1}{2} \left[ \sum_ {n = 0} ^ {\infty} \mathrm {e} ^ {- 2 n \pi} + 2 \sum_ {n = 0} ^ {\infty} \mathrm {e} ^ {- (2 n + 1) \pi} + \sum_ {n = 1} ^ {\infty} \mathrm {e} ^ {- 2 n \pi} \right] \\ = \frac {1}{2} \left(\frac {1}{1 - \mathrm {e} ^ {- 2 \pi}} + \frac {2 \mathrm {e} ^ {- \pi}}{1 - \mathrm {e} ^ {- 2 \pi}} + \frac {\mathrm {e} ^ {- 2 \pi}}{1 - \mathrm {e} ^ {- 2 \pi}}\right) = \frac {1}{2} \cdot \frac {\left(1 + \mathrm {e} ^ {- \pi}\right) ^ {2}}{\left(1 + \mathrm {e} ^ {- \pi}\right) \left(1 - \mathrm {e} ^ {- \pi}\right)} \\ = \frac {1}{2} \cdot \frac {1 + \mathrm {e} ^ {- \pi}}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}. \\ \end{array}</equation>

---

**2013年第16题 | 解答题 | 10分**

16. (本题满分10分)

设 D是由曲线<equation>y=x^{\frac{1}{3}}</equation>，直线 x=a（a>0）及 x轴所围成的平面图形，<equation>V_{x}</equation>和<equation>V_{y}</equation>分别是 D绕 x轴，y轴旋转一周所得旋转体的体积.若<equation>V_{y}=1 0 V_{x}</equation>，求 a的值.

**答案:**(16)<equation>a=7\sqrt{7}.</equation>

**解析:**解（法一）<equation>D</equation>绕<equation>x</equation>轴旋转所得的旋转体的体积<equation>V_{x}</equation>为<equation>V _ {x} = \pi \int_ {0} ^ {a} \left(x ^ {\frac {1}{3}}\right) ^ {2} \mathrm {d} x = \frac {3 \pi}{5} x ^ {\frac {5}{3}} \Bigg | _ {0} ^ {a} = \frac {3 \pi}{5} a ^ {\frac {5}{3}}.</equation><equation>D</equation>绕<equation>y</equation>轴旋转所得旋转体的体积<equation>V_{y}</equation>为<equation>V _ {y} = 2 \pi \int_ {0} ^ {a} x \cdot x ^ {\frac {1}{3}} \mathrm {d} x = 2 \pi \cdot \frac {3}{7} a ^ {\frac {7}{3}} = \frac {6 \pi}{7} a ^ {\frac {7}{3}}.</equation>由于<equation>V_{y}=1 0 V_{x}</equation>，故<equation>\frac{6\pi}{7} a^{\frac{7}{3}}=1 0\cdot \frac{3\pi}{5} a^{\frac{5}{3}}.</equation>整理得<equation>a ^ {\frac {5}{3}} \left(6 \pi - \frac {6 \pi}{7} a ^ {\frac {2}{3}}\right) = 0.</equation>因此，<equation>a = 0</equation>或<equation>a^{\frac{2}{3}} = 7.</equation>由题设知，<equation>a > 0</equation>，故<equation>a^{\frac{2}{3}} = 7</equation>，即<equation>a = 7\sqrt{7}.</equation>（法二）<equation>D</equation>绕<equation>y</equation>轴旋转所得旋转体的体积<equation>V_{y}</equation>为底面半径为<equation>a</equation>，高为<equation>a^{\frac{1}{3}}</equation>的圆柱体体积减去<equation>D^{\prime}</equation>（如图，由曲线<equation>y = x^{\frac{1}{3}}</equation>，直线<equation>y = a^{\frac{1}{3}}</equation>与<equation>y</equation>轴围成）绕<equation>y</equation>轴旋转所得旋转体的体积<equation>V_{y}^{\prime}</equation>圆柱体的体积<equation>V = \pi a^{2}\cdot a^{\frac{1}{3}} = \pi a^{\frac{7}{3}}.</equation><equation>V _ {y} ^ {\prime} = \pi \int_ {0} ^ {a ^ {\frac {1}{3}}} \left(y ^ {3}\right) ^ {2} \mathrm {d} y = \frac {\pi}{7} y ^ {7} \left| _ {0} ^ {a ^ {\frac {1}{3}}} = \frac {\pi}{7} a ^ {\frac {7}{3}}. \right.</equation>因此，<equation>V_{y} = \pi a^{\frac{7}{3}} - \frac{\pi}{7} a^{\frac{7}{3}} = \frac{6\pi}{7} a^{\frac{7}{3}}.</equation>其余同法一.

---

**2011年第12题 | 填空题 | 4分**

12. 曲线<equation>y=\sqrt{x^{2}-1}</equation>, 直线<equation>x=2</equation>及<equation>x</equation>轴所围的平面图形绕<equation>x</equation>轴旋转所成的旋转体的体积为 ___.

**解析:**解如图所示，联立方程<equation>\left\{\begin{array}{l l}y=\sqrt{x^{2}-1}\\ x=2,\end{array}\right.</equation>可解得曲线<equation>y=\sqrt{x^{2}-1}</equation>与直线<equation>x=2</equation>的交点为（2，<equation>\sqrt{3}</equation>）由旋转体的体积公式知所求体积为<equation>V = \pi \int_ {1} ^ {2} y ^ {2} (x) \mathrm {d} x = \pi \int_ {1} ^ {2} \left(x ^ {2} - 1\right) \mathrm {d} x = \pi \left(\frac {x ^ {3}}{3} - x\right) \Big | _ {1} ^ {2} = \frac {4}{3} \pi .</equation>

---

**2010年第10题 | 填空题 | 4分**

10. 设位于曲线<equation>y=\frac{1}{\sqrt{x(1+\ln^{2}x)}}</equation>（<equation>\mathrm{e}\leqslant x<+\infty</equation>）下方，x轴上方的无界区域为 G，则 G绕 x轴旋转一周所得空间区域的体积为 ___

**答案:**#<equation>\frac{\pi^{2}}{4}.</equation>

**解析:**解 由曲线表达式可知，<equation>y</equation>是关于<equation>x</equation>的单调减少函数且<equation>\lim_{x\to +\infty}y(x) = 0.</equation>由旋转体的体积公式知G绕<equation>x</equation>轴旋转一周所得空间区域的体积<equation>\begin{array}{l} V = \pi \int_ {\mathrm {e}} ^ {+ \infty} \left[ \frac {1}{\sqrt {x \left(1 + \ln^ {2} x\right)}} \right] ^ {2} \mathrm {d} x = \pi \int_ {\mathrm {e}} ^ {+ \infty} \frac {1}{x \left(1 + \ln^ {2} x\right)} \mathrm {d} x \\ = \pi \int_ {\mathrm {e}} ^ {+ \infty} \frac {\mathrm {d} (\ln x)}{1 + \ln^ {2} x} = \pi \arctan (\ln x) \Big | _ {\mathrm {e}} ^ {+ \infty} = \pi \left(\frac {\pi}{2} - \frac {\pi}{4}\right) = \frac {\pi^ {2}}{4}. \\ \end{array}</equation>

---

**2009年第19题 | 解答题 | 10分**

19. (本题满分10分)

设曲线 y=f(x)，其中 f(x)是可导函数，且 f(x)>0.已知曲线 y=f(x)与直线 y=0,x=1及 x=t(t>1)所围成的曲边梯形绕 x轴旋转一周所得的立体体积值是该曲边梯形面积值的<equation>\pi t</equation>倍，求该曲线的方程.

**答案:**(19)<equation>x=\frac{1}{3\sqrt{y}}+\frac{2}{3} y,x\geqslant 1.</equation>

**解析:**解 由旋转体的体积公式知曲边梯形绕 x轴旋转一周所得的立体体积<equation>V=\pi \int_{1}^{t}[f(x)]^{2}\mathrm{d}x.</equation>由定积分的几何意义知曲边梯形的面积<equation>S=\int_{1}^{t}f(x)\mathrm{d}x.</equation>由已知条件知<equation>V=\pi t S</equation>，故对任意的 t > 1，都有<equation>\pi \int_{1}^{t}[f(x)]^{2}\mathrm{d}x=\pi t\int_{1}^{t}f(x)\mathrm{d}x.</equation><equation>\pi \int_ {1} ^ {t} [ f (x) ] ^ {2} \mathrm {d} x = \pi t \int_ {1} ^ {t} f (x) \mathrm {d} x.</equation>上式两端消去<equation>\pi</equation>后并关于<equation>t</equation>求导得，<equation>[ f (t) ] ^ {2} = \int_ {1} ^ {t} f (x) \mathrm {d} x + t f (t).</equation>继续对上式两端关于 t求导得，<equation>2 f (t) f ^ {\prime} (t) = 2 f (t) + t f ^ {\prime} (t).</equation>令<equation>y=f(t)</equation>，得<equation>\frac {\mathrm {d} y}{\mathrm {d} t} = \frac {2 y}{2 y - t}.</equation>下面用两种方法解方程<equation>\frac{\mathrm{d}y}{\mathrm{d}t}=\frac{2y}{2y-t}.</equation>（法一）由<equation>\frac{\mathrm{d}y}{\mathrm{d}t} = \frac{2y}{2y - t}</equation>可得<equation>\frac{\mathrm{d}t}{\mathrm{d}y} + \frac{1}{2y} t = 1.</equation>此为一阶非齐次线性微分方程，其通解为<equation>t = \mathrm {e} ^ {- \int \frac {1}{2 y} \mathrm {d} y} \left(\int \mathrm {e} ^ {\int \frac {1}{2 y} \mathrm {d} y} \mathrm {d} y + C\right) = y ^ {- \frac {1}{2}} \left(\frac {2}{3} y ^ {\frac {3}{2}} + C\right) = C y ^ {- \frac {1}{2}} + \frac {2}{3} y.</equation>由（1）式可得<equation>[ f(1)]^{2}=f(1)</equation>，于是<equation>f(1)=1</equation>（舍去<equation>f(1)=0 )</equation>.代入上式解得<equation>C=\frac{1}{3}</equation>，即<equation>t=\frac{1}{3\sqrt{y}}+\frac{2}{3} y</equation>因此，所求曲线方程为<equation>x = \frac {1}{3 \sqrt {y}} + \frac {2}{3} y, \quad x \geqslant 1.</equation>（法二）此为齐次微分方程.令<equation>u=\frac{y}{t}</equation>，则<equation>y=ut,\frac{\mathrm{d}y}{\mathrm{d}t}=u+t\frac{\mathrm{d}u}{\mathrm{d}t}</equation>，从而<equation>u+t\frac{\mathrm{d}u}{\mathrm{d}t}=\frac{\mathrm{d}y}{\mathrm{d}t}=\frac{2y}{2y-t}=\frac{2u}{2u-1}.</equation>整理得<equation>\frac {2 u - 1}{3 u - 2 u ^ {2}} \mathrm {d} u = \frac {\mathrm {d} t}{t}.</equation>对上式两端积分得，<equation>\int \frac {2 u - 1}{3 u - 2 u ^ {2}} \mathrm {d} u = \int \left(- \frac {1}{3 u} + \frac {4}{3} \cdot \frac {1}{3 - 2 u}\right) \mathrm {d} u = \int \frac {\mathrm {d} t}{t}.</equation>由于 y > 0，t > 1，故 u > 0，从而<equation>-\frac{1}{3}\ln u-\frac{2}{3}\ln |3-2u|=\ln t+C_{1}</equation>，其中<equation>C_{1}</equation>为常数，即<equation>[ u (3 - 2 u) ^ {2} ] ^ {- \frac {1}{3}} = C t, \quad C = \mathrm {e} ^ {C _ {1}}.</equation>同法一可得<equation>f ( 1 )=1.</equation>于是<equation>u ( 1 )=\frac{f ( 1 )}{1}=1.</equation>代入（2）式解得<equation>C=1.</equation>将<equation>u=\frac{y}{t}</equation>代入（2）式化简得到<equation>y(3t-2y)^{2}=1</equation>，从而<equation>t=\frac{1}{3}\left(\pm \frac{1}{\sqrt{y}}+2y\right).</equation>由于<equation>y(1)=1</equation>，故<equation>t=\frac{1}{3}\left(\frac{1}{\sqrt{y}}+2y\right)</equation>即所求曲线方程为<equation>x=\frac{1}{3\sqrt{y}}+\frac{2}{3}y,x\geqslant 1.</equation>

---


#### 不定积分的计算

**2023年第2题 | 选择题 | 5分 | 答案: D**

2. 函数 f(x) =<equation>\left\{\begin{array}{l l}{\frac{1}{\sqrt{1+x^{2}}},}&{x\leqslant0,}\\ {(x+1)\cos x,}&{x>0}\end{array} \right.</equation>的一个原函数为（    )

A. F(x) =<equation>\left\{\begin{array}{l l}{\ln(\sqrt{1+x^{2}}-x),}&{x\leqslant0,}\\ {(x+1)\cos x-\sin x,}&{x>0.}\end{array} \right.</equation>B. F(x) =<equation>\left\{\begin{array}{l l}{\ln(\sqrt{1+x^{2}}-x)+1,}&{x\leqslant0,}\\ {(x+1)\cos x-\sin x,}&{x>0.}\end{array} \right.</equation>C. F(x) =<equation>\left\{\begin{array}{l l}{\ln(\sqrt{1+x^{2}}+x),}&{x\leqslant0,}\\ {(x+1)\sin x+\cos x,}&{x>0.}\end{array} \right.</equation>D. F(x) =<equation>\left\{\begin{array}{l l}{\ln(\sqrt{1+x^{2}}+x)+1,}&{x\leqslant0,}\\ {(x+1)\sin x+\cos x,}&{x>0.}\end{array} \right.</equation>

答案: D

**解析:**解（法一）首先，由于 F(x）是 f(x)的原函数，故必连续，而四个选项中的 F(x)均为分段函数，于是我们可以分别考察 F(x)在分界点处的连续性.

对选项 A,<equation>\lim_{x\rightarrow 0^{-}}F(x)=0, \lim_{x\rightarrow 0^{+}}F(x)=1. F(x)</equation>不连续.

对选项B，<equation>\lim_{x\to 0^{-}}F(x)=\lim_{x\to 0^{+}}F(x)=1=F(0).F(x)</equation>连续.

对选项 C<equation>\lim_{x\rightarrow 0^{-}}F(x)=0,\lim_{x\rightarrow 0^{+}}F(x)=1. F(x)</equation>不连续.

对选项 D<equation>\lim_{x\to 0^{-}}F(x)=\lim_{x\to 0^{+}}F(x)=1=F(0).F(x)</equation>连续.

由上可排除选项A与选项C.

选项B与选项D的差别在于函数表达式.<equation>[ (x + 1) \cos x - \sin x ] ^ {\prime} = \cos x - (x + 1) \sin x - \cos x = - (x + 1) \sin x,</equation><equation>[ (x + 1) \sin x + \cos x ] ^ {\prime} = \sin x + (x + 1) \cos x - \sin x = (x + 1) \cos x.</equation>由上可排除选项B.

因此，应选D.

（法二）当<equation>x\leqslant0</equation>时，<equation>\begin{array}{l} F (x) = \int \frac {\mathrm {d} x}{\sqrt {1 + x ^ {2}}} \xlongequal {x = \tan \theta} \int \frac {\sec^ {2} \theta}{\sec \theta} \mathrm {d} \theta = \int \sec \theta \mathrm {d} \theta = \ln | \sec \theta + \tan \theta | + C _ {1} \\ \underline {{\frac {x = \tan \theta}{2}}} \ln \left(\sqrt {1 + x ^ {2}} + x\right) + C _ {1}. \\ \end{array}</equation>当 x > 0时，<equation>\begin{aligned} F (x) &= \int (x + 1) \cos x \mathrm {d} x = \int (x + 1) \mathrm {d} (\sin x) = (x + 1) \sin x - \int \sin x \mathrm {d} x \\ &= (x + 1) \sin x + \cos x + C _ {2}. \end{aligned}</equation>四个选项中，仅有选项C、D符合要求.

由于 F(x）是 f(x)在<equation>(-\infty, +\infty)</equation>上的一个原函数，故 F(x)在 x=0处连续.<equation>\lim _ {x \rightarrow 0 ^ {-}} F (x) = \lim _ {x \rightarrow 0 ^ {-}} \left[ \ln \left(\sqrt {1 + x ^ {2}} + x\right) + C _ {1} \right] = C _ {1},</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} F (x) = \lim _ {x \rightarrow 0 ^ {+}} \left[ (x + 1) \sin x + \cos x + C _ {2} \right] = C _ {2} + 1.</equation>由<equation>\lim_{x\to 0^{-}}F(x) = \lim_{x\to 0^{+}}F(x)</equation>可得<equation>C_1 = C_2 + 1.</equation>选项C中，<equation>C_{1}=C_{2}=0,F(x)</equation>不连续，选项D中，<equation>C_{1}=1,C_{2}=0,F(x)</equation>连续，应选D.

---

**2018年第10题 | 填空题 | 4分**

**答案:**<equation>\mathrm{e}^{x}\arcsin \sqrt{1 - \mathrm{e}^{2x}} -\sqrt{1 - \mathrm{e}^{2x}} +C</equation>，其中C为任意常数.

**解析:**解 （法一）利用分部积分法.<equation>\begin{array}{l} \int \mathrm {e} ^ {x} \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} \mathrm {d} x \xlongequal {\text {分 部 积 分}} \int \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} \mathrm {d} \left(\mathrm {e} ^ {x}\right) \\ = \mathrm {e} ^ {x} \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} - \int \mathrm {e} ^ {x} \cdot \frac {1}{\sqrt {1 - 1 + \mathrm {e} ^ {2 x}}} \cdot \frac {- 2 \mathrm {e} ^ {2 x}}{2 \sqrt {1 - \mathrm {e} ^ {2 x}}} \mathrm {d} x \\ = \mathrm {e} ^ {x} \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} + \int \frac {\mathrm {e} ^ {2 x}}{\sqrt {1 - \mathrm {e} ^ {2 x}}} \mathrm {d} x \\ = \mathrm {e} ^ {x} \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} - \frac {1}{2} \int \frac {\mathrm {d} \left(1 - \mathrm {e} ^ {2 x}\right)}{\sqrt {1 - \mathrm {e} ^ {2 x}}} \\ = \mathrm {e} ^ {x} \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} - \sqrt {1 - \mathrm {e} ^ {2 x}} + C, \\ \end{array}</equation>其中 C为任意常数.

（法二）利用第二类换元法.

令<equation>\mathrm{e}^{x}=\cos t, t\in\left[0,\frac{\pi}{2}\right)</equation>，则<equation>\sqrt{1-\mathrm{e}^{2x}}=\sin t, t=\arcsin \sqrt{1-\mathrm{e}^{2x}},\mathrm{e}^{x}\mathrm{d}x=-\sin t\mathrm{d}t.</equation>因此，<equation>\begin{array}{l} \int \mathrm {e} ^ {x} \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} \mathrm {d} x = \int t \cdot (- \sin t) \mathrm {d} t = \int t \mathrm {d} (\cos t) = t \cos t - \int \cos t \mathrm {d} t \\ = t \cos t - \sin t + C = \mathrm {e} ^ {x} \arccos \mathrm {e} ^ {x} - \sqrt {1 - \mathrm {e} ^ {2 x}} + C \\ = \mathrm {e} ^ {x} \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} - \sqrt {1 - \mathrm {e} ^ {2 x}} + C, \\ \end{array}</equation>其中 C为任意常数.

---

**2011年第17题 | 解答题 | 10分**

17. (本题满分10分)

求不定积分

**答案:**(17)<equation>2 \sqrt{x} \arcsin \sqrt{x}+2 \sqrt{x} \ln x+2 \sqrt{1-x}-4 \sqrt{x}+C</equation>，其中C为任意常数.

**解析:**解 （法一）利用换元法和分部积分法.

令<equation>\sqrt{x} = t</equation>，则<equation>x = t^{2}</equation>，<equation>t > 0</equation>，<equation>\mathrm{d}x = 2t\mathrm{d}t.</equation>于是，<equation>\begin{array}{l} \int \frac {\arcsin \sqrt {x} + \ln x}{\sqrt {x}} \mathrm {d} x = \int \frac {\arcsin t + \ln t ^ {2}}{t} \cdot 2 t \mathrm {d} t = 2 \int \left(\arcsin t + \ln t ^ {2}\right) \mathrm {d} t \\ \underline {{\mathrm {分 部 积 分}}} = 2 \left[ \left(\arcsin t + \ln t ^ {2}\right) t - \int \left(\frac {1}{\sqrt {1 - t ^ {2}}} + \frac {2 t}{t ^ {2}}\right) t \mathrm {d} t \right] \\ = 2 \left(\arcsin t + \ln t ^ {2}\right) t + \int \frac {\mathrm {d} \left(1 - t ^ {2}\right)}{\sqrt {1 - t ^ {2}}} - \int 4 \mathrm {d} t \\ = 2 \left(\arcsin t + \ln t ^ {2}\right) t + 2 \sqrt {1 - t ^ {2}} - 4 t + C, \\ \end{array}</equation>其中 C为任意常数.

将<equation>t=\sqrt{x}</equation>代回，可得<equation>\text {原 积 分} = 2 \sqrt {x} \arcsin \sqrt {x} + 2 \sqrt {x} \ln x + 2 \sqrt {1 - x} - 4 \sqrt {x} + C,</equation>其中 C为任意常数.

（法二）分部积分法.<equation>\begin{array}{l} \int \frac {\arcsin \sqrt {x} + \ln x}{\sqrt {x}} \mathrm {d} x = 2 \int (\arcsin \sqrt {x} + \ln x) \mathrm {d} (\sqrt {x}) \\ \underline {{\mathrm {分 部 积 分}}} = 2 \left[ \left(\arcsin \sqrt {x} + \ln x\right) \sqrt {x} - \int \sqrt {x} \left(\frac {\frac {1}{2} x ^ {- \frac {1}{2}}}{\sqrt {1 - x}} + \frac {1}{x}\right) \mathrm {d} x \right] \\ = 2 \sqrt {x} \arcsin \sqrt {x} + 2 \sqrt {x} \ln x - \int \left(\frac {1}{\sqrt {1 - x}} + \frac {2}{\sqrt {x}}\right) \mathrm {d} x \\ = 2 \sqrt {x} \arcsin \sqrt {x} + 2 \sqrt {x} \ln x + 2 \sqrt {1 - x} - 4 \sqrt {x} + C, \\ \end{array}</equation>其中 C为任意常数.

---

**2009年第16题 | 解答题 | 10分**

16. (本题满分10分)

计算不定积分<equation>\int\ln\left(1+\sqrt{\frac{1+x}{x}}\right)\mathrm{d}x(x>0).</equation>

**答案:**(16)<equation>x \ln \left( 1+\sqrt{\frac{1+x}{x}} \right)+\frac{1}{2} \ln \left( \sqrt{1+x}+\sqrt{x} \right)-\frac{\sqrt{x}}{2\left( \sqrt{1+x}+\sqrt{x} \right)}-C</equation>，其中C为任意常数.

**解析:**解（法一）令<equation>u=\sqrt{\frac{1+x}{x}}</equation>，则<equation>x=\frac{1}{u^{2}-1}.</equation>于是，<equation>\int \ln \left(1 + \sqrt {\frac {1 + x}{x}}\right) \mathrm {d} x = \int \ln (1 + u) \mathrm {d} \left(\frac {1}{u ^ {2} - 1}\right) = \frac {\ln (1 + u)}{u ^ {2} - 1} - \int \frac {1}{\left(u ^ {2} - 1\right) \left(u + 1\right)} \mathrm {d} u.</equation>计算<equation>\int \frac{1}{(u^{2}-1)(u+1)} \mathrm{d} u.</equation><equation>\begin{aligned} \int \frac {1}{\left(u ^ {2} - 1\right) (u + 1)} \mathrm {d} u &= \frac {1}{2} \int \frac {(u + 1) - (u - 1)}{\left(u ^ {2} - 1\right) (u + 1)} \mathrm {d} u = \frac {1}{2} \left[ \int \frac {1}{u ^ {2} - 1} \mathrm {d} u - \int \frac {1}{(u + 1) ^ {2}} \mathrm {d} u \right] \\ &= \frac {1}{4} \int \left(\frac {1}{u - 1} - \frac {1}{u + 1}\right) \mathrm {d} u - \frac {1}{2} \int \frac {1}{(u + 1) ^ {2}} \mathrm {d} u = \frac {1}{4} \ln \frac {u - 1}{u + 1} + \frac {1}{2 (u + 1)} + C, \end{aligned}</equation>其中 C为任意常数.这里的<equation>\ln \frac{u-1}{u+1}</equation>没有绝对值符号，是因为<equation>u=\sqrt{\frac{1+x}{x}}>1.</equation>将 u =<equation>\sqrt{\frac{1+x}{x}}</equation>代回原积分，得<equation>\begin{aligned} \mathrm {原 积 分} &= \frac {\ln (1 + u)}{u ^ {2} - 1} + \frac {1}{4} \ln \frac {u + 1}{u - 1} - \frac {1}{2 (u + 1)} - C \\ \frac {u = \sqrt {\frac {1 + x}{x}}}{x \ln \left(1 + \sqrt {\frac {1 + x}{x}}\right)} + \frac {1}{2} \ln \left(\sqrt {1 + x} + \sqrt {x}\right) - \frac {\sqrt {x}}{2 \left(\sqrt {1 + x} + \sqrt {x}\right)} - C, \end{aligned}</equation>其中 C为任意常数.

（法二）使用待定系数法来求<equation>\int \frac{1}{(u^{2}-1)(u+1)} \mathrm{d} u.</equation><equation>\begin{aligned} \frac {1}{\left(u ^ {2} - 1\right) (u + 1)} &= \frac {a}{u - 1} + \frac {b}{u + 1} + \frac {c}{(u + 1) ^ {2}} = \frac {a (u + 1) ^ {2} + b (u - 1) (u + 1) + c (u - 1)}{(u - 1) (u + 1) ^ {2}} \\ &= \frac {(a + b) u ^ {2} + (2 a + c) u + a - b - c}{(u - 1) (u + 1) ^ {2}}. \end{aligned}</equation>比较<equation>u^{2}</equation>，<equation>u</equation>的系数以及常数项，可得<equation>\left\{ \begin{array}{l l} a + b = 0, \\ 2a + c = 0, \\ a - b - c = 1, \end{array} \right.</equation>解得<equation>a = \frac{1}{4}, b = -\frac{1}{4}, c = -\frac{1}{2}</equation>.

因此，<equation>\int \frac{1}{(u^{2}-1)(u+1)} \mathrm{d} u=\frac{1}{4} \int \left[ \frac{1}{u-1}-\frac{1}{u+1}-\frac{2}{(u+1)^{2}} \right] \mathrm{d} u=\frac{1}{4} \left( \ln \frac{u-1}{u+1}+\frac{2}{u+1} \right)+C</equation>其中C为任意常数.

其余同法一.

---


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

**2025年第5题 | 选择题 | 5分 | 答案: A**

5. 设 A是 m×n矩阵，<equation>\beta</equation>是 m维非零列向量，若 A有 k阶非零子式，则（    ）

A. 当 k=m时，<equation>A x=\beta</equation>有解 B. 当 k=m时，<equation>A x=\beta</equation>无解

C. 当 k<m时，<equation>A x=\beta</equation>有解 D. 当 k<m时，<equation>A x=\beta</equation>无解

答案: A

**解析:**解由 A有k阶非零子式可知<equation>r ( A ) \geqslant k</equation>当<equation>k=m</equation>时，<equation>r ( A ) \geqslant m</equation>另一方面，由 A是<equation>m \times n</equation>矩阵可知<equation>r ( A ) \leqslant \min \{ m, n \} \leqslant m</equation>于是，<equation>r ( A )=m</equation>从而<equation>r ( A , \beta) \geqslant m</equation>又因为（A，<equation>\beta</equation>）是<equation>m \times(n+1)</equation>矩阵，<equation>r ( A , \beta) \leqslant m</equation>所以<equation>r ( A , \beta) = m</equation>由此可得，<equation>r ( A )=r ( A , \beta)=m</equation>方程组<equation>A x=\beta</equation>有解.选项 A正确，选项B不正确.

因此，应选A.

下面说明选项C、D不正确.

取<equation>m = 2,n = 1,k = 1.</equation>对选项C，取<equation>A=\binom{1}{0},\beta=\binom{0}{1}</equation>，则方程组<equation>Ax=\beta</equation>无解.

对选项D，取<equation>A=\binom{1}{0},\beta=\binom{1}{0}</equation>，则方程组<equation>Ax=\beta</equation>有解.

---

**2024年第21题 | 解答题 | 12分**

21. （本题满分12分）

设矩阵<equation>A = \left( \begin{array}{c c c c} 1 & -1 & 0 & -1 \\ 1 & 1 & 0 & 3 \\ 2 & 1 & 2 & 6 \end{array} \right), B = \left( \begin{array}{c c c c} 1 & 0 & 1 & 2 \\ 1 & -1 & a & a - 1 \\ 2 & -3 & 2 & -2 \end{array} \right)</equation>，向量<equation>\alpha = \left( \begin{array}{c} 0 \\ 2 \\ 3 \end{array} \right), \beta = \left( \begin{array}{c} 1 \\ 0 \\ -1 \end{array} \right).</equation>I. 证明：方程组<equation>A x=\alpha</equation>的解均为方程组<equation>B x=\beta</equation>的解；

II. 若方程组<equation>Ax = \alpha</equation>与方程组<equation>Bx = \beta</equation>不同解，求<equation>a</equation>的值.

**答案:**(1) 证明略

(2) a=1.

**解析:**解（I）（法一）分别对（A，<equation>\alpha</equation>）和（B，<equation>\beta</equation>）作初等行变换<equation>\begin{array}{l} (A, \alpha) = \left( \begin{array}{c c c c c} 1 & - 1 & 0 & - 1 & 0 \\ 1 & 1 & 0 & 3 & 2 \\ 2 & 1 & 2 & 6 & 3 \end{array} \right) \xrightarrow {r _ {1} + r _ {2}} \left( \begin{array}{c c c c c} 2 & 0 & 0 & 2 & 2 \\ 1 & 1 & 0 & 3 & 2 \\ 2 & 1 & 2 & 6 & 3 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c} 1 & 0 & 0 & 1 & 1 \\ 1 & 1 & 0 & 3 & 2 \\ 2 & 1 & 2 & 6 & 3 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c} 1 & 0 & 0 & 1 & 1 \\ 0 & 1 & 0 & 2 & 1 \\ 0 & 1 & 2 & 4 & 1 \end{array}\right)\rightarrow \left( \begin{array}{c c c c c} 1 & 0 & 0 & 1 & 1 \\ 0 & 1 & 0 & 2 & 1 \\ 0 & 0 & 2 & 2 & 0 \end{array}\right)\rightarrow \left( \begin{array}{c c c c c} 1 & 0 & 0 & 1 & 1 \\ 0 & 1 & 0 & 2 & 1 \\ 0 & 0 & 1 & 1 & 0 \end{array}\right). \\ \end{array}</equation><equation>\begin{array}{l} (\boldsymbol {B}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 1 & 0 & 1 & 2 & 1 \\ 1 & - 1 & a & a - 1 & 0 \\ 2 & - 3 & 2 & - 2 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c} 1 & 0 & 1 & 2 & 1 \\ 0 & - 1 & a - 1 & a - 3 & - 1 \\ 0 & - 3 & 0 & - 6 & - 3 \end{array} \right) \\ \rightarrow \left(\begin{array}{c c c c c}1&0&1&2&1\\0&1&0&2&1\\0&- 1&a - 1&a - 3&- 1\end{array}\right)\rightarrow \left(\begin{array}{c c c c c}1&0&1&2&1\\0&1&0&2&1\\0&0&a - 1&a - 1&0\end{array}\right). \\ \end{array}</equation>注意到<equation>(1,0,1,2,1) = (1,0,0,1,1) + (0,0,1,1,0)</equation>，故无论<equation>\alpha</equation>取何值，<equation>(A,\alpha)</equation>的行向量组均能线性表示<equation>(B,\beta)</equation>的行向量组，从而方程组<equation>Ax = \alpha</equation>的解均为方程组<equation>Bx = \beta</equation>的解.

（法二）先求<equation>A x=\alpha</equation>的解.

同法一可得<equation>(A, \alpha) \rightarrow \left( \begin{array}{cccc} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 1 & 1 \\ 0 \end{array} \right)</equation>. 令<equation>x_{4} = 1</equation>, 则<equation>Ax = 0</equation>的一个基础解系可取为<equation>\left( \begin{array}{c} - 1 \\ - 2 \\ - 1 \\ 1 \end{array} \right)</equation>.

又令<equation>x_{4} = 0</equation>, 可得<equation>Ax = \alpha</equation>的一个特解为<equation>\left( \begin{array}{c} 1 \\ 1 \\ 0 \\ 0 \end{array} \right)</equation>, 从而<equation>Ax = \alpha</equation>的通解为<equation>k\left( \begin{array}{c} - 1 \\ - 2 \\ - 1 \\ 1 \end{array} \right) + \left( \begin{array}{c} 1 \\ 1 \\ 0 \\ 0 \end{array} \right)</equation>, 即<equation>\left( \begin{array}{c} - k + 1 \\ - 2k + 1 \\ - k \\ k \end{array} \right)</equation>, 其中<equation>k</equation>为任意常数.

计算<equation>B\left( \begin{array}{c} - k + 1 \\ - 2k + 1 \\ - k \\ k \end{array} \right)</equation>可得<equation>\left( \begin{array}{c c c c} 1 & 0 & 1 & 2 \\ 1 & - 1 & a & a - 1 \\ 2 & - 3 & 2 & - 2 \end{array} \right)\left( \begin{array}{c} - k + 1 \\ - 2k + 1 \\ - k \\ k \end{array} \right) = \left( \begin{array}{c} - k + 1 - k + 2k \\ - k + 1 + 2k - 1 - ak + (a - 1)k \\ - 2k + 2 + 6k - 3 - 2k - 2k \end{array} \right) = \left( \begin{array}{c} 1 \\ 0 \\ - 1 \end{array} \right)</equation>.

于是,<equation>\left( \begin{array}{c} - k + 1 \\ - 2k + 1 \\ - k \\ k \end{array} \right)</equation>是<equation>Bx = \beta</equation>的解.

因此，方程组<equation>A x=\alpha</equation>的解均为方程组<equation>B x=\beta</equation>的解.

（法三）由于方程组<equation>Ax = \alpha</equation>的解均为方程组<equation>Bx = \beta</equation>的解等价于方程组<equation>\left\{ \begin{array}{l}Ax = \alpha ,\\ Bx = \beta \end{array} \right.</equation>与方程组<equation>Ax = \alpha</equation>同解（见注），故要证明方程组<equation>Ax = \alpha</equation>的解均为方程组<equation>Bx = \beta</equation>的解，只需证明方程组<equation>\left\{ \begin{array}{l}Ax = \alpha ,\\ Bx = \beta \end{array} \right.</equation>与方程组<equation>Ax = \alpha</equation>同解.

对<equation>\left( \begin{array}{cc}A&\alpha \\ B&\beta \end{array} \right)</equation>作初等行变换.<equation>\left( \begin{array}{c c} A & \alpha \\ B & \beta \end{array} \right) \xrightarrow {\text {同 法 一}} \left( \begin{array}{c c c c c} 1 & 0 & 0 & 1 & 1 \\ 0 & 1 & 0 & 2 & 1 \\ 0 & 0 & 1 & 1 & 0 \\ 1 & 0 & 1 & 2 & 1 \\ 0 & 1 & 0 & 2 & 1 \\ 0 & 0 & a - 1 & a - 1 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c} 1 & 0 & 0 & 1 & 1 \\ 0 & 1 & 0 & 2 & 1 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>\left( \begin{array}{cc}A&\alpha \\ B&\beta \end{array} \right)</equation>的行向量组与（A，<equation>\alpha</equation>）的行向量组等价.由此可得，方程组<equation>\left\{ \begin{array}{l l}Ax = \alpha ,\\ Bx = \beta \end{array} \right.</equation>与方程组<equation>A x = \alpha</equation>同解，从而方程组<equation>A x = \alpha</equation>的解均为方程组<equation>B x = \beta</equation>的解.

（Ⅱ）（法一）由第（I）问的法一可知，当<equation>a\neq 1</equation>时，<equation>(A,\alpha)</equation>的行向量组与<equation>(B,\beta)</equation>的行向量组等价，从而<equation>A x=\alpha</equation>与<equation>B x=\beta</equation>同解.当<equation>a=1</equation>时，<equation>(A,\alpha)</equation>的行向量组能线性表示<equation>(B,\beta)</equation>的行向量组，但<equation>(B,\beta)</equation>的行向量组不能线性表示<equation>(A,\alpha)</equation>的行向量组，从而<equation>A x=\alpha</equation>与<equation>B x=\beta</equation>不同解.

因此，<equation>a = 1</equation>（法二）由第（I）问可知，方程组<equation>A x=\alpha</equation>的解均为方程组<equation>B x=\beta</equation>的解，而方程组<equation>A x=\alpha</equation>与方程组<equation>B x=\beta</equation>不同解，故<equation>A x=\alpha</equation>的解集是<equation>B x=\beta</equation>的解集的真子集.进一步可得<equation>A x=0</equation>的解集是<equation>B x=0</equation>的解集的真子集.

由第（I）问可知，<equation>r ( A )=3</equation>，故结合<equation>A x=0</equation>的解集是Bx=0的解集的真子集可得，<equation>r ( B )<</equation>3. 又因为B有2阶非零子式<equation>\left| \begin{array}{c c} {1} & {0} \\ {1} & {-1} \end{array} \right|</equation>，所以<equation>r ( B )\geqslant 2</equation>.于是，<equation>r ( B )=2.</equation>对矩阵 B作初等行变换<equation>\begin{array}{l} \boldsymbol {B} = \left( \begin{array}{c c c c} 1 & 0 & 1 & 2 \\ 1 & - 1 & a & a - 1 \\ 2 & - 3 & 2 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 0 & 1 & 2 \\ 0 & - 1 & a - 1 & a - 3 \\ 0 & - 3 & 0 & - 6 \end{array} \right) \\ \rightarrow \left(\begin{array}{c c c c}1&0&1&2\\0&- 1&a - 1&a - 3\\0&1&0&2\end{array}\right)\rightarrow \left(\begin{array}{c c c c}1&0&1&2\\0&- 1&a - 1&a - 3\\0&0&a - 1&a - 1\end{array}\right). \\ \end{array}</equation><equation>r(\boldsymbol{B}) = 2</equation>当且仅当<equation>a - 1 = 0</equation>，即<equation>a = 1</equation>因此，<equation>a=1.</equation>

---

**2023年第15题 | 填空题 | 5分**

15. 已知线性方程组<equation>\left| \begin{array}{l l l} a x _ {1} + x _ {3} = 1, \\ x _ {1} + a x _ {2} + x _ {3} = 0, \\ x _ {1} + 2 x _ {2} + a x _ {3} = 0, \\ a x _ {1} + b x _ {2} = 2 \end{array} \right. \mathrm {有 解}, \mathrm {其 中} a, b \mathrm {为 常 数 . 若} \left| \begin{array}{c c c} a & 0 & 1 \\ 1 & a & 1 \\ 1 & 2 & a \end{array} \right| = 4, \mathrm {则} \left| \begin{array}{c c c} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right| = \underline {{\quad}}.</equation>

**解析:**解（法一）记方程组<equation>\left\{ \begin{array}{l l} a x_{1}+x_{3}=1, \\ x_{1}+a x_{2}+x_{3}=0, \\ x_{1}+2 x_{2}+a x_{3}=0, \\ a x_{1}+b x_{2}=2 \end{array} \right.</equation>的系数矩阵为A，增广矩阵为（A,b），则<equation>(\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} a & 0 & 1 & 1 \\ 1 & a & 1 & 0 \\ 1 & 2 & a & 0 \\ a & b & 0 & 2 \end{array} \right).</equation>由方程组有解可知<equation>r ( \mathbf{A})=r ( \mathbf{A},\mathbf{b})</equation>.因为 A为<equation>4\times 3</equation>矩阵，所以<equation>r ( \mathbf{A})\leqslant 3</equation>，从而<equation>r ( \mathbf{A})=r ( \mathbf{A},\mathbf{b})\leqslant 3</equation>进一步可得<equation>| \mathbf{A},\mathbf{b} |=0</equation>.于是，<equation>0 = \left| \begin{array}{c c c c} a & 0 & 1 & 1 \\ 1 & a & 1 & 0 \\ 1 & 2 & a & 0 \\ a & b & 0 & 2 \end{array} \right| \xlongequal {\text {按 第四 列 展开}} - \left| \begin{array}{c c c} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right| + 2 \left| \begin{array}{c c c} a & 0 & 1 \\ 1 & a & 1 \\ 1 & 2 & a \end{array} \right| = - \left| \begin{array}{c c c} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right| + 8.</equation>因此，<equation>\left| \begin{array}{c c c} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right| = 8.</equation>（法二）记方程组<equation>\left\{\begin{array}{l l}a x_{1}+x_{3}=1,\\x_{1}+a x_{2}+x_{3}=0,\\x_{1}+2 x_{2}+a x_{3}=0,\\a x_{1}+b x_{2}=2\end{array}\right.</equation>的系数矩阵为 A，增广矩阵为（A,b）.由方程组有解可知<equation>r(A)=r(A,b).</equation>注意到<equation>\left| \begin{array}{c c c} a & 0 & 1 \\ 1 & a & 1 \\ 1 & 2 & a \end{array} \right|=4</equation>为 A的一个3阶非零子式，故<equation>r(A)\geqslant 3.</equation>又因为 A为<equation>4\times 3</equation>矩阵，所以<equation>r(A)\leqslant 3.</equation>从而<equation>r(A)=3.</equation>由<equation>r ( \mathbf{A} )=r ( \mathbf{A},\mathbf{b} )</equation>可得，<equation>r ( \mathbf{A},\mathbf{b} )=3.</equation>于是<equation>r ( \mathbf{A} )=r ( \mathbf{A},\mathbf{b} )=3</equation>，该方程组有唯一解.

考虑方程组 I：<equation>\left\{\begin{array}{l l}a x_{1}+x_{3}=1,\\x_{1}+a x_{2}+x_{3}=0,\\x_{1}+2 x_{2}+a x_{3}=0\end{array}\right.</equation>和方程组 II：<equation>\left\{\begin{array}{l l}x_{1}+a x_{2}+x_{3}=0,\\x_{1}+2 x_{2}+a x_{3}=0,\\a x_{1}+b x_{2}=2.\end{array}\right.</equation>由原方程组有唯一解

可知方程组 I 和方程组 II 有唯一公共解.

由于方程组 I的系数矩阵行列式等于4，故由克拉默法则知其仅有唯一解，进一步可得其增广矩阵的秩为3，行向量组线性无关。由此可知方程组Ⅱ的增广矩阵<equation>\left( \begin{array}{c c c c} {1} & {a} & {1} & {0} \\ {1} & {2} & {a} & {0} \\ {a} & {b} & {0} & {2} \end{array} \right)</equation>的前两行线性无关。又因为该增广矩阵的第三行为（a,b，0，2），最后一个元素非零，所以第三行与前两行线性无关。于是，方程组Ⅱ的增广矩阵的秩为3.由方程组Ⅱ有解可知，其系数矩阵的秩也为3，从而行列式非零.

记该公共解为<equation>\left(x_{1},x_{2},x_{3}\right)^{\mathrm{T}}</equation><equation>\left| \begin{array}{lll} a & 0 & 1 \\ 1 & a & 1 \\ 1 & 2 & a \end{array} \right|=A_{1}=4</equation><equation>\left| \begin{array}{lll} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right|=A_{2}\neq0.</equation>对方程组 I 使用克拉默法则可得<equation>x_{1}=\frac{\left| \begin{array}{lll}1&0&1\\ 0&a&1\\ 0&2&a \end{array} \right|}{A_{1}}=\frac{\left| \begin{array}{lll}1&0&1\\ 0&a&1\\ 0&2&a \end{array} \right|}{4}</equation>，对方程组Ⅱ使用克拉默法则可得<equation>x_{1}=\frac{\left| \begin{array}{lll}0&a&1\\ 0&2&a\\ 2&b&0 \end{array} \right|}{A_{2}}.</equation>由此可得<equation>x _ {1} = \frac {\left| \begin{array}{c c} a & 1 \\ 2 & a \end{array} \right|}{4} = \frac {2 \left| \begin{array}{c c} a & 1 \\ 2 & a \end{array} \right|}{A _ {2}}.</equation>若<equation>\left| \begin{array}{ll} a & 1 \\ 2 & a \end{array} \right|=0</equation>，则 a =<equation>\pm \sqrt{2}</equation>.但将 a =<equation>\pm \sqrt{2}</equation>代入<equation>\left| \begin{array}{lll} a & 0 & 1 \\ 1 & a & 1 \\ 1 & 2 & a \end{array} \right|</equation>所得行列式并不等于4，故<equation>\left| \begin{array}{ll} a & 1 \\ 2 & a \end{array} \right| \neq</equation>0. 因此，由（1）式可得<equation>A_{2}=8</equation>，即<equation>\left| \begin{array}{lll} 1 & a & 1 \\ 1 & 2 & a \\ a & b & 0 \end{array} \right|=8.</equation>

---

**2022年第6题 | 选择题 | 5分 | 答案: D**

6. 设矩阵<equation>A=\left( \begin{array}{c c c} {1} & {1} & {1} \\ {1} & {a} & a^{2} \\ {1} & {b} & b^{2} \end{array} \right), b=\left( \begin{array}{c} {1} \\ {2} \\ {4} \end{array} \right),</equation>则线性方程组<equation>A x=b</equation>的解的情况为（    )

A. 无解 B. 有解 C. 有无穷多解或无解 D. 有唯一解或无解

答案: D

**解析:**解 （法一）注意到<equation>| \mathbf {A} | = \left| \begin{array}{l l l} 1 & 1 & 1 \\ 1 & a & a ^ {2} \\ 1 & b & b ^ {2} \end{array} \right| = \left| \begin{array}{l l l} 1 & 1 & 1 \\ 1 & a & b \\ 1 & a ^ {2} & b ^ {2} \end{array} \right| = (b - a) (b - 1) (a - 1).</equation>当 a≠1,b≠1，且 a≠b时，<equation>|A| \neq 0.</equation>由克拉默法则可知，此时方程组<equation>A x=b</equation>有唯一解.

当 a = 1时，<equation>(A, b) = \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 2 \\ 1 & b & b ^ {2} & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 0 & 0 & 0 & 1 \\ 1 & b & b ^ {2} & 4 \end{array} \right).</equation>r（A,b）<equation>\neq r(A)</equation>，方程组无解.同理可得，当b=1时，r（A,b）<equation>\neq r(A)</equation>，方程组无解.

当 a = b时，<equation>(\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 1 & a & a ^ {2} & 2 \\ 1 & b & b ^ {2} & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 1 & a & a ^ {2} & 2 \\ 0 & 0 & 0 & 2 \end{array} \right).</equation><equation>r ( \mathbf{A}, \mathbf{b}) \neq r (\mathbf{A})</equation>，方程组无解.

综上所述，方程组<equation>A x=b</equation>的解的情况只有两种可能，有唯一解或无解.应选D.

（法二）直接对增广矩阵（A,b）作初等行变换.<equation>(\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 1 & a & a ^ {2} & 2 \\ 1 & b & b ^ {2} & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 0 & a - 1 & a ^ {2} - 1 & 1 \\ 0 & b - 1 & b ^ {2} - 1 & 3 \end{array} \right).</equation>当 a = b = 1时，<equation>r(\mathbf{A})=1, r(\mathbf{A},\mathbf{b})=2</equation>，方程组无解.

当<equation>a = 1,b\neq 1</equation>或<equation>a\neq 1,b = 1</equation>时，<equation>r(A) = 2,r(A,b) = 3</equation>，方程组无解.

当 a = b ，但均不等于1时，<equation>r(\mathbf{A})=2,r(\mathbf{A},\mathbf{b})=3</equation>，方程组无解.

当<equation>a\neq 1,b\neq 1</equation>，且<equation>a\neq b</equation>时，<equation>r(A) = r(A,b) = 3.</equation>方程组有唯一解.

综上所述，方程组<equation>A x=b</equation>的解的情况只有两种可能，有唯一解或无解.应选D.

---

**2021年第6题 | 选择题 | 5分 | 答案: D**

6. 设<equation>A=\left(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4}\right)</equation>为4阶正交矩阵，若矩阵<equation>B=\left( \begin{array}{c}\alpha_{1}^{\mathrm{T}}\\ \alpha_{2}^{\mathrm{T}}\\ \alpha_{3}^{\mathrm{T}} \end{array} \right),\beta=\left( \begin{array}{c}1\\ 1\\ 1 \end{array} \right),k</equation>表示任意常数，则线性方程组<equation>Bx=\beta</equation>的通解 x=（    ）

A.<equation>\alpha_{2}+\alpha_{3}+\alpha_{4}+k\alpha_{1}</equation>B.<equation>\alpha_{1}+\alpha_{3}+\alpha_{4}+k\alpha_{2}</equation>C.<equation>\alpha_{1}+\alpha_{2}+\alpha_{4}+k\alpha_{3}</equation>D.<equation>\alpha_{1}+\alpha_{2}+\alpha_{3}+k\alpha_{4}</equation>

答案: D

**解析:**解 由于 A为正交矩阵，故<equation>\boldsymbol{\alpha}_{i}^{\mathrm{T}}\boldsymbol{\alpha}_{i}=1, \boldsymbol{\alpha}_{i}^{\mathrm{T}}\boldsymbol{\alpha}_{j}=0 ( i \neq j )</equation>，i，j=1,2,3,4.

先求<equation>Bx=0</equation>的解. B是<equation>3\times 4</equation>矩阵，<equation>r(B)=3</equation>，故<equation>Bx=0</equation>的基础解系中包含4-3=1个解向量.<equation>B x=0</equation>即<equation>\left( \begin{array}{l} \boldsymbol{\alpha}_{1}^{\mathrm{T}} \\ \boldsymbol{\alpha}_{2}^{\mathrm{T}} \\ \boldsymbol{\alpha}_{3}^{\mathrm{T}} \end{array} \right) x=0</equation>，也即<equation>\left( \begin{array}{l} \boldsymbol{\alpha}_{1}^{\mathrm{T}} x \\ \boldsymbol{\alpha}_{2}^{\mathrm{T}} x \\ \boldsymbol{\alpha}_{3}^{\mathrm{T}} x \end{array} \right)=\left( \begin{array}{l} 0 \\ 0 \\ 0 \end{array} \right).</equation>因为<equation>\alpha_{4}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>均正交，所以<equation>\alpha_{4}</equation>是<equation>B x=0</equation>的解.<equation>Bx = 0</equation>的通解为<equation>k\alpha_{4}</equation>，其中<equation>k</equation>为任意常数.

再求<equation>B x=\beta</equation>的一个特解.

由于<equation>\boldsymbol{\alpha}_{i}^{\mathrm{T}}\boldsymbol{\alpha}_{i}=1, \boldsymbol{\alpha}_{i}^{\mathrm{T}}\boldsymbol{\alpha}_{j}=0 ( i \neq j ) , i,j=1,2,3,4</equation>，故<equation>\begin{aligned} \left(  \boldsymbol {\alpha} _ {1} ^ {\mathrm {T}} \\ \boldsymbol {\alpha} _ {2} ^ {\mathrm {T}} \\ \boldsymbol {\alpha} _ {3} ^ {\mathrm {T}}  \right) \left(\boldsymbol {\alpha} _ {1} + \boldsymbol {\alpha} _ {2} + \boldsymbol {\alpha} _ {3}\right) &= \left(  \boldsymbol {\alpha} _ {1} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {1} + \boldsymbol {\alpha} _ {1} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {2} + \boldsymbol {\alpha} _ {1} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {3} \\ \boldsymbol {\alpha} _ {2} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {1} + \boldsymbol {\alpha} _ {2} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {2} + \boldsymbol {\alpha} _ {2} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {3} \\ \boldsymbol {\alpha} _ {3} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {1} + \boldsymbol {\alpha} _ {3} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {2} + \boldsymbol {\alpha} _ {3} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {3}  \right) &= \left(  1 \\ 1 \\ 1  \right). \end{aligned}</equation><equation>\alpha_{1} + \alpha_{2} + \alpha_{3}</equation>是<equation>Bx = \beta</equation>的一个特解.

因此，<equation>B x=\beta</equation>的通解为<equation>\alpha_{1}+\alpha_{2}+\alpha_{3}+k\alpha_{4}</equation>其中k为任意常数.应选D.

---

**2020年第5题 | 选择题 | 4分 | 答案: C**

5. 设4阶矩阵<equation>A=(a_{ij})</equation>不可逆，<equation>a_{12}</equation>的代数余子式<equation>A_{12}\neq0,\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4}</equation>为矩阵 A的列向量组，<equation>A^{*}</equation>为 A的伴随矩阵，则方程组<equation>A^{*}x=0</equation>的通解为（    )

A.<equation>x=k_{1}\alpha_{1}+k_{2}\alpha_{2}+k_{3}\alpha_{3}</equation>其中<equation>k_{1},k_{2},k_{3}</equation>为任意常数

B.<equation>x=k_{1}\alpha_{1}+k_{2}\alpha_{2}+k_{3}\alpha_{4}</equation>其中<equation>k_{1},k_{2},k_{3}</equation>为任意常数

C.<equation>x=k_{1}\alpha_{1}+k_{2}\alpha_{3}+k_{3}\alpha_{4}</equation>其中<equation>k_{1},k_{2},k_{3}</equation>为任意常数

D.<equation>x=k_{1}\alpha_{2}+k_{2}\alpha_{3}+k_{3}\alpha_{4}</equation>其中<equation>k_{1},k_{2},k_{3}</equation>为任意常数

答案: C

**解析:**解 由 A不可逆可知，<equation>|A|=0</equation>.于是，<equation>A^{*}A=|A|E=O</equation>.从而， A的列向量均为<equation>A^{*}x=0</equation>的解.

另一方面，<equation>A_{12}\neq0</equation>，说明<equation>A^{*}</equation>中有非零元素，<equation>r(A^{*})\geqslant1.</equation>又因为 A不可逆，所以<equation>r(A)\leqslant3.</equation>但是当<equation>r(A)<3</equation>时，<equation>r(A^{*})=0.</equation>因此，<equation>r(A)=3, r(A^{*})=1.</equation><equation>A^{*}x=0</equation>的基础解系中包含3个解向量.

由<equation>A_{12}\neq0</equation>可知，<equation>\left( \begin{array}{c c c} a_{21} & a_{23} & a_{24} \\ a_{31} & a_{33} & a_{34} \\ a_{41} & a_{43} & a_{44} \end{array} \right)\neq0.</equation>.于是，<equation>\left( \begin{array}{c} a_{21} \\ a_{31} \\ a_{41} \end{array} \right), \left( \begin{array}{c} a_{23} \\ a_{33} \\ a_{43} \end{array} \right), \left( \begin{array}{c} a_{24} \\ a_{34} \\ a_{44} \end{array} \right)</equation>线性无关.由分析中的结论可知，<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>线性无关，从而构成<equation>A^{*}x=0</equation>的一个基础解系.

因此，<equation>A^{*}x=0</equation>的通解可写为<equation>x=k_{1}\alpha_{1}+k_{2}\alpha_{3}+k_{3}\alpha_{4}</equation>，其中<equation>k_{1},k_{2},k_{3}</equation>为任意常数.应选C.

---

**2019年第13题 | 填空题 | 4分**

13. 已知矩阵<equation>A=\left( \begin{array}{c c c} 1 & 0 & -1 \\ 1 & 1 & -1 \\ 0 & 1 & a^{2}-1 \end{array} \right), b=\left( \begin{array}{c} 0 \\ 1 \\ a \end{array} \right),</equation>若线性方程组<equation>A x=b</equation>有无穷多解，则 a=___

**解析:**由<equation>A x=b</equation>有无穷多解可得，<equation>r ( A )=r ( A , b ) < 3.</equation>对（A，b）作初等行变换.<equation>(\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} 1 & 0 & - 1 & 0 \\ 1 & 1 & - 1 & 1 \\ 0 & 1 & a ^ {2} - 1 & a \end{array} \right) \xrightarrow {r _ {2} - r _ {1}} \left( \begin{array}{c c c c} 1 & 0 & - 1 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 1 & a ^ {2} - 1 & a \end{array} \right) \xrightarrow {r _ {3} - r _ {2} ^ {*}} \left( \begin{array}{c c c c} 1 & 0 & - 1 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & a ^ {2} - 1 & a - 1 \end{array} \right).</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

由上式可知<equation>r(A)\geqslant 2</equation>，故<equation>r(A) = r(A,b) = 2.</equation>于是，<equation>a^{2} - 1 = 0</equation>且<equation>a - 1 = 0</equation>，解得<equation>a = 1.</equation>

---

**2018年第21题 | 解答题 | 11分**

21. (本题满分11分)

已知 a是常数，且矩阵<equation>A=\left( \begin{array}{c c c} 1 & 2 & a \\ 1 & 3 & 0 \\ 2 & 7 & -a \end{array} \right)</equation>可经初等列变换化为矩阵<equation>B=\left( \begin{array}{c c c} 1 & a & 2 \\ 0 & 1 & 1 \\ -1 & 1 & 1 \end{array} \right).</equation>I. 求 a;

II. 求满足<equation>A P=B</equation>的可逆矩阵<equation>P.</equation>

**答案:**（ I ）<equation>a=2;</equation>（Ⅱ）满足<equation>A P=B</equation>的可逆矩阵为<equation>\boldsymbol {P} = \left( \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right),</equation>其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数，且<equation>k_{2} \neq k_{3}</equation>.

**解析:**解（I）由于 A可经初等列变换化为 B，故矩阵方程 AX=B有解.于是，<equation>r(A)=r(A,B).</equation>对（A,B）作初等行变换.<equation>\begin{array}{l} (A, B) = \left( \begin{array}{c c c c c c} 1 & 2 & a & 1 & a & 2 \\ 1 & 3 & 0 & 0 & 1 & 1 \\ 2 & 7 & - a & - 1 & 1 & 1 \end{array} \right) \xrightarrow [ r _ {3} - 2 r _ {1} ]{r _ {2} - r _ {1}} \left( \begin{array}{c c c c c c} 1 & 2 & a & 1 & a & 2 \\ 0 & 1 & - a & - 1 & 1 - a & - 1 \\ 0 & 3 & - 3 a & - 3 & 1 - 2 a & - 3 \end{array} \right) \\ \xrightarrow [ r _ {3} ^ {*} - 3 r _ {2} ^ {*} ]{r _ {1} - 2 r _ {2} ^ {*}} \left( \begin{array}{c c c c c c} 1 & 0 & 3 a & 3 & 3 a - 2 & 4 \\ 0 & 1 & - a & - 1 & 1 - a & - 1 \\ 0 & 0 & 0 & 0 & a - 2 & 0 \end{array} \right). \\ \end{array}</equation>当且仅当 a=2时，<equation>r(\mathbf{A})=r(\mathbf{A},\mathbf{B})=2.</equation>或者，由矩阵 A可经初等列变换化为矩阵 B可知，A的列秩等于 B的列秩，从而<equation>r ( \mathbf{A})=r (\mathbf{B})</equation>.同上面的计算可知<equation>r ( \mathbf{A})=2</equation>，当且仅当 a=2时，<equation>r ( \mathbf{A})=r ( \mathbf{B})</equation>.

因此，<equation>a=2.</equation>（Ⅱ）当 a=2时，<equation>(\boldsymbol {A}, \boldsymbol {B}) \rightarrow \left(\begin{array}{c c c c c c}1&0&6&3&4&4\\0&1&- 2&- 1&- 1&- 1\\0&0&0&0&0&0\end{array}\right).</equation><equation>A X=B</equation>等价于<equation>\left( \begin{array}{c c c} 1 & 0 & 6 \\ 0 & 1 & -2 \\ 0 & 0 & 0 \end{array} \right) X=\left( \begin{array}{c c c} 3 & 4 & 4 \\ -1 & -1 & -1 \\ 0 & 0 & 0 \end{array} \right).</equation>记<equation>\left( \begin{array}{c c c} 1 & 0 & 6 \\ 0 & 1 & -2 \\ 0 & 0 & 0 \end{array} \right)=A^{\prime}.</equation>方程组<equation>A^{\prime} x=0</equation>的一个基础解系为<equation>(-6,2,1)^{\mathrm{T}}.</equation>于是，方程组<equation>A^{\prime} x=(3,-1,0)^{\mathrm{T}}</equation>的通解为<equation>x_{1}=k_{1}(-6,2,1)^{\mathrm{T}}+</equation><equation>(3,-1,0)^{\mathrm{T}}</equation>其中<equation>k_{1}</equation>为任意常数；方程组<equation>A^{\prime} x=(4,-1,0)^{\mathrm{T}}</equation>的通解为<equation>x_{2}=k_{2}(-6,2,1)^{\mathrm{T}}+</equation><equation>(4,-1,0)^{\mathrm{T}}</equation>其中<equation>k_{2}</equation>为任意常数；方程组<equation>A^{\prime} x=(4,-1,0)^{\mathrm{T}}</equation>的通解为<equation>x_{3}=k_{3}(-6,2,1)^{\mathrm{T}}+</equation><equation>(4,-1,0)^{\mathrm{T}}</equation>其中<equation>k_{3}</equation>为任意常数.

因此，矩阵方程 AX=B的通解为<equation>\boldsymbol {X} = \left( \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right),</equation>其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数.

若可逆矩阵 P满足 AP=B，则<equation>\boldsymbol {P} = \left( \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right),</equation>且<equation>| P | \neq 0.</equation>由于<equation>| P | = \left| \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right| = \left| \begin{array}{c c c} 0 & 1 & 1 \\ - 1 & - 1 & - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right| = \left| \begin{array}{c c c} 0 & 1 & 1 \\ - 1 & 0 & 0 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right| = k _ {3} - k _ {2},</equation>故当<equation>k_{2}\neq k_{3}</equation>时，P可逆.

因此，满足 AP=B的可逆矩阵为<equation>\boldsymbol {P} = \left( \begin{array}{c c c} - 6 k _ {1} + 3 & - 6 k _ {2} + 4 & - 6 k _ {3} + 4 \\ 2 k _ {1} - 1 & 2 k _ {2} - 1 & 2 k _ {3} - 1 \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right),</equation>其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数，且<equation>k_{2} \neq k_{3}</equation>.

---

**2017年第20题 | 解答题 | 11分**

20. (本题满分11分)

设3阶矩阵<equation>A=(\alpha_{1},\alpha_{2},\alpha_{3})</equation>有3个不同的特征值，且<equation>\alpha_{3}=\alpha_{1}+2\alpha_{2}.</equation>I. 证明<equation>r(A)=2;</equation>II. 若<equation>\beta=\alpha_{1}+\alpha_{2}+\alpha_{3}</equation>，求方程组<equation>A x=\beta</equation>的通解.

**答案:**（I）证明略；

（Ⅱ）<equation>k ( 1, 2,-1 )^{\mathrm{T}}+( 1, 1, 1 )^{\mathrm{T}}</equation>为线性方程组<equation>A x=\beta</equation>的通解，其中 k为任意常数.

**解析:**解（I）（法一）由于 A有3个不同的特征值<equation>\lambda_{1},\lambda_{2},\lambda_{3}</equation>，故 A相似于对角矩阵，且至多仅有一个零特征值.该对角矩阵的秩<equation>\geqslant 2</equation>.又因为相似的矩阵有相同的秩，所以<equation>r(A)\geqslant 2.</equation>另一方面，<equation>\alpha_{3} = \alpha_{1} + 2\alpha_{2}</equation>，故<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性相关，<equation>|A| = 0.</equation>由于<equation>| A| = \lambda_{1}\lambda_{2}\lambda_{3}</equation>，故A有一个特征值为零.

因此，<equation>r ( \mathbf{A} )=2.</equation>（法二）也可以如下证明0是A的一个特征值.

由<equation>\boldsymbol{\alpha}_{3}=\boldsymbol{\alpha}_{1}+2\boldsymbol{\alpha}_{2}</equation>知，<equation>\left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) \left( \begin{array}{c} 1 \\ 2 \\ - 1 \end{array} \right) = \mathbf {0} = 0 \left( \begin{array}{c} 1 \\ 2 \\ - 1 \end{array} \right).</equation>于是，0是 A的一个特征值，<equation>( 1, 2, - 1 )^{\mathrm{T}}</equation>是 A的属于特征值0的一个特征向量.

其余同法一.

（Ⅱ）考虑<equation>A x=0</equation>.由于<equation>r(A)=2</equation>，故<equation>A x=0</equation>的基础解系中只包含一个向量.又因为<equation>\alpha_{3}=\alpha_{1}+2\alpha_{2}</equation>，所以<equation>(\alpha_{1},\alpha_{2},\alpha_{3})(1,2,-1)^{\mathrm{T}}=0</equation>，即<equation>(1,2,-1)^{\mathrm{T}}</equation>是该齐次线性方程组的一个基础解系.由于<equation>\beta =\alpha_{1}+\alpha_{2}+\alpha_{3}</equation>，即<equation>(\alpha_{1},\alpha_{2},\alpha_{3})(1,1,1)^{\mathrm{T}}=\beta</equation>，故<equation>(1,1,1)^{\mathrm{T}}</equation>是<equation>A x=\beta</equation>的一个特解.因此，<equation>k(1,2,-1)^{\mathrm{T}}+(1,1,1)^{\mathrm{T}}</equation>为线性方程组<equation>A x=\beta</equation>的通解，其中<equation>k</equation>为任意常数.

---

**2016年第20题 | 解答题 | 11分**

20. （本题满分11分）

设矩阵<equation>A = \left( \begin{array}{c c c} 1 & 1 & 1 - a \\ 1 & 0 & a \\ a + 1 & 1 & a + 1 \end{array} \right),\beta = \left( \begin{array}{c} 0 \\ 1 \\ 2a - 2 \end{array} \right),</equation>且方程组<equation>A x=\beta</equation>无解.

I. 求 a的值；

II. 求方程组<equation>A^{\mathrm{T}} A x=A^{\mathrm{T}} \beta</equation>的通解.

**答案:**（ I ）<equation>a=0</equation>； （ II ）通解为<equation>k(0,-1,1)^{\mathrm{T}}+(1,-2,0)^{\mathrm{T}}</equation>，其中 k为任意常数.

**解析:**解（I）由于<equation>A x=\beta</equation>无解，故由非齐次线性方程组有解的充分必要条件可知，<equation>r(A,\beta)\neq r(A).</equation><equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c} 1 & 1 & 1 - a & 0 \\ 1 & 0 & a & 1 \\ a + 1 & 1 & a + 1 & 2 a - 2 \end{array} \right) \xrightarrow {r _ {2} - r _ {1}} \frac {r _ {2} - r _ {1}}{r _ {3} - (a + 1) r _ {1}} \left( \begin{array}{c c c c} 1 & 1 & 1 - a & 0 \\ 0 & - 1 & 2 a - 1 & 1 \\ 0 & - a & a ^ {2} + a & 2 a - 2 \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} \times (- 1)} \left( \begin{array}{c c c c} 1 & 1 & 1 - a & 0 \\ 0 & 1 & 1 - 2 a & - 1 \\ 0 & - a & a ^ {2} + a & 2 a - 2 \end{array} \right) \xrightarrow {r _ {1} - r _ {2} ^ {* *}} \left( \begin{array}{c c c c} 1 & 0 & a & 1 \\ 0 & 1 & 1 - 2 a & - 1 \\ 0 & 0 & - a ^ {2} + 2 a & a - 2 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

由上面的式子可知，<equation>r ( A ) \geqslant 2</equation>. 从而，<equation>A x=\beta</equation>无解当且仅当<equation>r ( A )=2</equation>且<equation>r ( A,\beta)=3.</equation>此时，<equation>- a^{2}+2 a=0</equation>，且<equation>a-2\neq0</equation>，解得 a=0.<equation>\begin{aligned} (\mathrm {I I}) \mathrm {当} a &= 0 \mathrm {时}, \boldsymbol {A} = \left( \begin{array}{l l l} 1 & 1 & 1 \\ 1 & 0 & 0 \\ 1 & 1 & 1  \right), \boldsymbol {A} ^ {\mathrm {T}} &= \left( \begin{array}{l l l} 1 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 0 & 1  \right), \boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {A} &= \left( \begin{array}{l l l} 3 & 2 & 2 \\ 2 & 2 & 2 \\ 2 & 2 & 2  \right), \boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {\beta} &= \left(  - 1 \\ - 2 \\ - 2  \right). \end{aligned}</equation><equation>\begin{array}{l} \left(\boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {A}, \boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {\beta}\right) = \left( \begin{array}{c c c c} 3 & 2 & 2 & - 1 \\ 2 & 2 & 2 & - 2 \\ 2 & 2 & 2 & - 2 \end{array} \right) \xrightarrow [ r _ {2} \times \frac {1}{2} ]{r _ {3} - r _ {2}} \left( \begin{array}{c c c c} 3 & 2 & 2 & - 1 \\ 1 & 1 & 1 & - 1 \\ 0 & 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {1} - 2 r _ {2} ^ {*} ]{r _ {1} - 2 r _ {2} ^ {*}} \left( \begin{array}{c c c c} 1 & 0 & 0 & 1 \\ 1 & 1 & 1 & - 1 \\ 0 & 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} - r _ {1} ^ {*}} \left( \begin{array}{c c c c} 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & - 2 \\ 0 & 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation><equation>A^{\mathrm{T}} A x=A^{\mathrm{T}} \beta</equation>对应的齐次线性方程组等价于<equation>\left\{ \begin{array}{l l} x_{1}=0, \\ x_{2}+x_{3}=0. \end{array} \right.</equation>（0，-1，1）<equation>^{\mathrm{T}}</equation>为该方程组的一个基础解系.又因为<equation>(1,-2,0)^{\mathrm{T}}</equation>是<equation>A^{\mathrm{T}} A x=A^{\mathrm{T}} \beta</equation>的一个特解，所以<equation>A^{\mathrm{T}} A x=A^{\mathrm{T}} \beta</equation>的通解为<equation>k(0,-1,1)^{\mathrm{T}}+</equation>（1，-2，0）<equation>^{\mathrm{T}}</equation>，其中k为任意常数.

---

**2015年第5题 | 选择题 | 4分 | 答案: D**

5. 设矩阵<equation>A=\left( \begin{array}{c c c} {1} & {1} & {1} \\ {1} & {2} & {a} \\ {1} & {4} & {a^{2}} \\ \end{array} \right), b=\left( \begin{array}{c} {1} \\ {d} \\ {d^{2}} \\ \end{array} \right).</equation>若集合<equation>\Omega=\{1,2\}</equation>，则线性方程组<equation>A x=b</equation>有无穷多解的充分必要条件为（    ）

A. a<equation>\notin\Omega, d\notin\Omega</equation>B. a<equation>\notin\Omega, d\in\Omega</equation>C. a<equation>\in\Omega, d\notin\Omega</equation>D. a<equation>\in\Omega, d\in\Omega</equation>

答案: D

**解析:**解 （法一）对（A，b）作初等行变换.<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 1 & 2 & a & d \\ 1 & 4 & a ^ {2} & d ^ {2} \end{array} \right) \xrightarrow [ r _ {3} - r _ {1} ]{r _ {2} - r _ {1}} \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 0 & 1 & a - 1 & d - 1 \\ 0 & 3 & a ^ {2} - 1 & d ^ {2} - 1 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {*} - 3 r _ {2} ^ {*}} \left( \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 0 & 1 & a - 1 & d - 1 \\ 0 & 0 & a ^ {2} - 3 a + 2 & d ^ {2} - 3 d + 2 \end{array} \right). \\ \end{array}</equation>(<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每作一次初等行变换，加一个*.）

由此可见，<equation>r ( \mathbf{A})=r ( \mathbf{A},\mathbf{b})<3</equation>当且仅当<equation>a^{2}-3 a+2=0</equation>且<equation>d^{2}-3 d+2=0</equation>即 a=1或a=2，且 d=1或d=2，也即 a<equation>\in\Omega</equation><equation>d \in\Omega.</equation>因此，<equation>a\in \Omega</equation>，<equation>d\in \Omega</equation>是<equation>Ax = b</equation>有无穷多解的充分必要条件.应选D.

（法二）当 a<equation>\in\Omega</equation>，d<equation>\in\Omega</equation>时，r（A）=r（A,b）=2<3，故 a<equation>\in\Omega</equation>，d<equation>\in\Omega</equation>是 Ax=b有无穷多解的充分条件.

当<equation>Ax = b</equation>有无穷多解时，<equation>r(A) = r(A,b) < 3</equation>，从而<equation>r(A) < 3</equation>，<equation>|A| = 0.</equation>由于<equation>|A|</equation>为范德蒙德行列式，故<equation>|A| = 0</equation>当且仅当<equation>a = 1</equation>或<equation>a = 2</equation>，即<equation>a \in \Omega .</equation>由于<equation>r(A,b) = r(A) < 3</equation>，故<equation>(1,d,d^{2})^{\mathrm{T}}</equation>与<equation>(1,1,1)^{\mathrm{T}}</equation>和<equation>(1,2,4)^{\mathrm{T}}</equation>线性相关，从而<equation>\left| \begin{array}{c c c} 1 & 1 & 1 \\ 1 & 2 & d \\ 1 & 4 & d^{2} \end{array} \right| = 0.</equation>再次由范德蒙德行列式的性质可推出<equation>d = 1</equation>或<equation>d = 2</equation>，即<equation>d \in \Omega .</equation>因此，<equation>a\in \Omega</equation>，<equation>d\in \Omega</equation>是<equation>Ax = b</equation>有无穷多解的充分必要条件.应选D.

（法三）排除法.我们可以把简单的值代入各选项，然后根据<equation>A x=b</equation>是否有无穷多解来排除错误选项.

选项A：代入<equation>a=0</equation>，<equation>d=0</equation>，<equation>r(\mathbf{A})=r(\mathbf{A},\mathbf{b})=3</equation>，不符合题意.

选项B：代入<equation>a=0</equation>，<equation>d\in\{1,2\}</equation>，<equation>r(\mathbf{A})=r(\mathbf{A},\mathbf{b})=3</equation>，不符合题意.

选项C：代入<equation>a\in\{1,2\}</equation>，<equation>d=0</equation>，<equation>r(\mathbf{A},\mathbf{b})=3</equation>，<equation>r(\mathbf{A})=2</equation>，不符合题意.

由上可见，选项A、B、C均不是正确选项.由排除法知，应选D.

---

**2014年第20题 | 解答题 | 11分**

20. (本题满分11分)

设矩阵<equation>A = \left( \begin{array}{c c c c} 1 & -2 & 3 & -4 \\ 0 & 1 & -1 & 1 \\ 1 & 2 & 0 & -3 \end{array} \right), E</equation>为3阶单位矩阵.

I. 求方程组<equation>A x=0</equation>的一个基础解系；

II. 求满足<equation>A B=E</equation>的所有矩阵 B.

**答案:**(20) (I)<equation>(-1,2,3,1)^{\mathrm{T}};</equation><equation>(\mathrm {I I}) \boldsymbol {B} = \left( \begin{array}{c c c} 2 - k _ {1} & 6 - k _ {2} & - 1 - k _ {3} \\ - 1 + 2 k _ {1} & - 3 + 2 k _ {2} & 1 + 2 k _ {3} \\ - 1 + 3 k _ {1} & - 4 + 3 k _ {2} & 1 + 3 k _ {3} \\ k _ {1} & k _ {2} & k _ {3} \end{array} \right)</equation>其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数.

**解析:**解（I）考察系数矩阵 A.<equation>\begin{array}{l} \boldsymbol {A} = \left( \begin{array}{c c c c} 1 & - 2 & 3 & - 4 \\ 0 & 1 & - 1 & 1 \\ 1 & 2 & 0 & - 3 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c c} 1 & - 2 & 3 & - 4 \\ 0 & 1 & - 1 & 1 \\ 0 & 4 & - 3 & 1 \end{array} \right) \xrightarrow {r _ {1} + 2 r _ {2}} \left( \begin{array}{c c c c} 1 & 0 & 1 & - 2 \\ 0 & 1 & - 1 & 1 \\ 0 & 0 & 1 & - 3 \end{array} \right) \\ \xrightarrow {r _ {1} ^ {*} - r _ {3} ^ {* *}} \frac {1}{r _ {2} + r _ {3} ^ {* *}} \left( \begin{array}{c c c c} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & - 2 \\ 0 & 0 & 1 & - 3 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每作一次初等行变换，加一个*.）<equation>Ax = 0</equation>可化为方程组<equation>\left\{ \begin{array}{l} x_{1} + x_{4} = 0, \\ x_{2} - 2x_{4} = 0, \\ x_{3} - 3x_{4} = 0. \end{array} \right.</equation>由此可得<equation>\xi = (-1, 2, 3, 1)^{\mathrm{T}}</equation>为<equation>Ax = 0</equation>的一个基础解系.

（Ⅱ）实际上我们要求的是三个非齐次线性方程组<equation>A x=(1,0,0)^{\mathrm{T}}</equation><equation>A x=(0,1,0)^{\mathrm{T}}</equation><equation>A x=(0,0,1)^{\mathrm{T}}</equation>的解.由于它们的系数矩阵都是A，故可考虑对（A，E）作初等行变换，同第（I）问中的步骤可得<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {E}) = \left( \begin{array}{c c c c c c c} 1 & - 2 & 3 & - 4 & 1 & 0 & 0 \\ 0 & 1 & - 1 & 1 & 0 & 1 & 0 \\ 1 & 2 & 0 & - 3 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c c c c c} 1 & - 2 & 3 & - 4 & 1 & 0 & 0 \\ 0 & 1 & - 1 & 1 & 0 & 1 & 0 \\ 0 & 4 & - 3 & 1 & - 1 & 0 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} + 2 r _ {2}} \frac {1}{r _ {3} ^ {*} - 4 r _ {2}} \left( \begin{array}{c c c c c c c} 1 & 0 & 1 & - 2 & 1 & 2 & 0 \\ 0 & 1 & - 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & 1 & - 3 & - 1 & - 4 & 1 \end{array} \right) \xrightarrow {r _ {1} ^ {*} - r _ {3} ^ {* *}} \left( \begin{array}{c c c c c c c} 1 & 0 & 0 & 1 & 2 & 6 & - 1 \\ 0 & 1 & 0 & - 2 & - 1 & - 3 & 1 \\ 0 & 0 & 1 & - 3 & - 1 & - 4 & 1 \end{array} \right). \\ \end{array}</equation>由于 A为<equation>3 \times4</equation>矩阵，B为3阶单位矩阵，B应为<equation>4 \times3</equation>矩阵，从而知，<equation>Ax=(1,0,0)^{\mathrm{T}}</equation><equation>Ax=(0,1,0)^{\mathrm{T}}</equation><equation>Ax=(0,0,1)^{\mathrm{T}}</equation>的一个特解分别为<equation>(2,-1,-1,0)^{\mathrm{T}}</equation><equation>(6,-3,-4,0)^{\mathrm{T}}</equation><equation>(-1,1,1,0)^{\mathrm{T}}.</equation>与第（I）问中<equation>Ax=0</equation>的一个基础解系相结合，得到<equation>Ax=(1,0,0)^{\mathrm{T}}</equation><equation>Ax=(0,1,0)^{\mathrm{T}}</equation><equation>Ax=(0,0,1)^{\mathrm{T}}</equation>的通解分别为<equation>\begin{aligned} \boldsymbol {\alpha} _ {1} &= k _ {1} (- 1, 2, 3, 1) ^ {\mathrm {T}} + (2, - 1, - 1, 0) ^ {\mathrm {T}}, \\ \boldsymbol {\alpha} _ {2} &= k _ {2} (- 1, 2, 3, 1) ^ {\mathrm {T}} + (6, - 3, - 4, 0) ^ {\mathrm {T}}, \\ \boldsymbol {\alpha} _ {3} &= k _ {3} (- 1, 2, 3, 1) ^ {\mathrm {T}} + (- 1, 1, 1, 0) ^ {\mathrm {T}}, \end{aligned}</equation>其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数.

因此，<equation>B = \left( \begin{array}{c c c} 2 - k_{1} & 6 - k_{2} & -1 - k_{3} \\ -1 + 2k_{1} & -3 + 2k_{2} & 1 + 2k_{3} \\ -1 + 3k_{1} & -4 + 3k_{2} & 1 + 3k_{3} \\ k_{1} & k_{2} & k_{3} \end{array} \right)</equation>，其中<equation>k_{1}, k_{2}, k_{3}</equation>为任意常数.

---

**2013年第20题 | 解答题 | 11分**

20. (本题满分11分)

设<equation>A = \left( \begin{array}{c c} 1 & a \\ 1 & 0 \end{array} \right), B = \left( \begin{array}{c c} 0 & 1 \\ 1 & b \end{array} \right).</equation>当<equation>a,b</equation>为何值时，存在矩阵<equation>C</equation>使得<equation>AC - CA = B</equation>，并求所有矩阵<equation>C</equation>

**答案:**(20)<equation>a=-1,b=0</equation>时，<equation>C=\left( \begin{array}{c c} k_{1}+k_{2}+1 & -k_{2} \\ k_{2} & k_{1} \end{array} \right)</equation>，其中<equation>k_{1},k_{2}</equation>为任意常数.

**解析:**解（法一）设<equation>C = \left( \begin{array}{ll} x_{1} & x_{2} \\ x_{3} & x_{4} \end{array} \right)</equation>，则由<equation>AC - CA = B</equation>可得<equation>\left( \begin{array}{c c} 1 & a \\ 1 & 0 \end{array} \right) \left( \begin{array}{c c} x _ {1} & x _ {2} \\ x _ {3} & x _ {4} \end{array} \right) - \left( \begin{array}{c c} x _ {1} & x _ {2} \\ x _ {3} & x _ {4} \end{array} \right) \left( \begin{array}{c c} 1 & a \\ 1 & 0 \end{array} \right) = \left( \begin{array}{c c} 0 & 1 \\ 1 & b \end{array} \right).</equation>写成线性方程组的形式：<equation>\left\{ \begin{array}{l} - x _ {2} + a x _ {3} = 0, \\ - a x _ {1} + x _ {2} + a x _ {4} = 1, \\ x _ {1} - x _ {3} - x _ {4} = 1, \\ x _ {2} - a x _ {3} = b. \end{array} \right.</equation>记该线性方程组为<equation>Px = \beta ,\beta = (0,1,1,b)^{\mathrm{T}}</equation>，则<equation>Px = \beta</equation>有解当且仅当<equation>r(P,\beta) = r(P)</equation><equation>\begin{array}{l} (\boldsymbol {P}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 0 & - 1 & a & 0 & 0 \\ - a & 1 & 0 & a & 1 \\ 1 & 0 & - 1 & - 1 & 1 \\ 0 & 1 & - a & 0 & b \end{array} \right) \xrightarrow {r _ {2} + a r _ {3}} \left( \begin{array}{c c c c c} 0 & - 1 & a & 0 & 0 \\ 0 & 1 & - a & 0 & a + 1 \\ 1 & 0 & - 1 & - 1 & 1 \\ 0 & 1 & - a & 0 & b \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} + r _ {1}} \binom {0} {r _ {4} + r _ {1}} \left( \begin{array}{c c c c c} 0 & - 1 & a & 0 & 0 \\ 0 & 0 & 0 & 0 & a + 1 \\ 1 & 0 & - 1 & - 1 & 1 \\ 0 & 0 & 0 & 0 & b \end{array} \right) \rightarrow \left( \begin{array}{c c c c c} 1 & 0 & - 1 & - 1 & 1 \\ 0 & 1 & - a & 0 & 0 \\ 0 & 0 & 0 & 0 & a + 1 \\ 0 & 0 & 0 & 0 & b \end{array} \right). \\ \end{array}</equation><equation>r_{2}^{*}</equation>表示对<equation>r_{2}</equation>作初等行变换后所得新的第二行.由上可见，若<equation>r ( \boldsymbol{P}, \boldsymbol{\beta})=r ( \boldsymbol{P})</equation>，则必有<equation>a+1=b=0</equation>从而<equation>a=-1</equation><equation>b=0.</equation>当 a=-1，b=0时，<equation>(\boldsymbol {P}, \boldsymbol {\beta}) \rightarrow \left(\begin{array}{c c c c c}1&0&- 1&- 1&1\\0&1&1&0&0\\0&0&0&0&0\\0&0&0&0&0\end{array}\right),</equation>即<equation>\left\{ \begin{array}{l l} x_{1}-x_{3}-x_{4}=1, \\ x_{2}+x_{3}=0. \end{array} \right.</equation>（1，0，0，1）<equation>^{\mathrm{T}}</equation>和（1，-1，1，0）<equation>^{\mathrm{T}}</equation>为该方程组对应的齐次线性方程组的一个基础解系.又（1，0，0，0）<equation>^{\mathrm{T}}</equation>为<equation>P x=\beta</equation>的一个特解，故<equation>P x=\beta</equation>的通解为<equation>k _ {1} \left(1, 0, 0, 1\right) ^ {\mathrm {T}} + k _ {2} \left(1, - 1, 1, 0\right) ^ {\mathrm {T}} + \left(1, 0, 0, 0\right) ^ {\mathrm {T}},</equation>其中<equation>k_{1}, k_{2}</equation>为任意常数.

因此，当 a=-1，b=0时，存在C使得AC-CA=B.此时的C形如<equation>\left( \begin{array}{c c} k_{1}+k_{2}+1 & -k_{2} \\ k_{2} & k_{1} \end{array} \right)</equation>，其中<equation>k_{1}, k_{2}</equation>为任意常数.

（法二）由于AC的迹等于CA的迹，故AC-CA的迹等于零.因此<equation>b=0.</equation><equation>B=\left( \begin{array}{cc}0&1\\ 1&0\end{array} \right).</equation>设<equation>C=\left( \begin{array}{cc}x_{1}&x_{2}\\ x_{3}&x_{4}\end{array} \right)</equation>，则由<equation>AC-CA=B</equation>可得<equation>\left\{ \begin{array}{l} - x _ {2} + a x _ {3} = 0, \\ - a x _ {1} + x _ {2} + a x _ {4} = 1, \\ x _ {1} - x _ {3} - x _ {4} = 1, \\ x _ {2} - a x _ {3} = 0. \end{array} \right.</equation>将<equation>x_{2}=a x_{3}</equation>代入<equation>- a x_{1}+x_{2}+a x_{4}=1</equation>可得<equation>- a \left(x_{1}-x_{3}-x_{4}\right)=1</equation>与<equation>x_{1}-x_{3}-x_{4}=1</equation>比较得，<equation>a=-1.</equation>从而得，<equation>a=-1</equation>，<equation>b=0.</equation>其余同法一.

---

**2012年第20题 | 解答题 | 11分**

20. (本题满分11分)

设<equation>\text {设} A = \left( \begin{array}{c c c c} 1 & a & 0 & 0 \\ 0 & 1 & a & 0 \\ 0 & 0 & 1 & a \\ a & 0 & 0 & 1 \end{array} \right), \beta = \left( \begin{array}{c} 1 \\ - 1 \\ 0 \\ 0 \end{array} \right).</equation>I. 计算行列式<equation>|A|</equation>;

II. 当实数<equation>a</equation>为何值时，方程组<equation>Ax = \beta</equation>有无穷多解，并求其通解.

**答案:**<equation>(\mathrm {I}) | \boldsymbol {A} | = 1 - a ^ {4};</equation>（Ⅱ）当 a=-1时，方程组<equation>A x=\beta</equation>有无穷多解，其通解为<equation>k(1,1,1,1)^{\mathrm{T}}+(0,-1,0,0)^{\mathrm{T}}</equation>，其中 k为任意常数.

**解析:**（ I ）按第一行展开<equation>|A|</equation>，得<equation>| \boldsymbol {A} | = \left| \begin{array}{c c c} 1 & a & 0 \\ 0 & 1 & a \\ 0 & 0 & 1 \end{array} \right| - a \left| \begin{array}{c c c} 0 & a & 0 \\ 0 & 1 & a \\ a & 0 & 1 \end{array} \right| = 1 - a ^ {4}.</equation>（Ⅱ）（法一）<equation>A x=\beta</equation>有无穷多解的充要条件为<equation>r(A)=r(A,\beta) < 4.</equation>由<equation>r(A) < 4</equation>可得，<equation>|A| = 0</equation>，从而<equation>a=\pm 1.</equation>当 a=1时，<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 1 & 0 & 0 & 1 & 0 \end{array} \right) \xrightarrow {r _ {4} - r _ {1}} \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & - 1 & 0 & 1 & - 1 \end{array} \right) \xrightarrow {r _ {4} ^ {*} + r _ {2}} \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1 & - 2 \end{array} \right) \\ \xrightarrow {r _ {4} ^ {* *} - r _ {3}} \left( \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & - 1 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 & - 2 \end{array} \right). \\ \end{array}</equation><equation>(r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每作一次初等行变换，加一个<equation>*.</equation>）由上可知，<equation>r(A,\beta) = 4</equation>，而<equation>r(A) = 3</equation>，<equation>Ax = \beta</equation>无解.<equation>a = 1</equation>不符合题意.

当 a=-1时，<equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 1 & - 1 & 0 & 0 & 1 \\ 0 & 1 & - 1 & 0 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ - 1 & 0 & 0 & 1 & 0 \end{array} \right) \xrightarrow {r _ {4} + r _ {1}} \left( \begin{array}{c c c c c} 1 & - 1 & 0 & 0 & 1 \\ 0 & 1 & - 1 & 0 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ 0 & - 1 & 0 & 1 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} + r _ {2}} \frac {r _ {4} ^ {*} + r _ {2}}{r _ {4} ^ {*} + r _ {2}} \left( \begin{array}{c c c c c} 1 & 0 & - 1 & 0 & 0 \\ 0 & 1 & - 1 & 0 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ 0 & 0 & - 1 & 1 & 0 \end{array} \right) \xrightarrow {r _ {1} ^ {*} + r _ {3}} \frac {r _ {2} + r _ {3}}{r _ {4} ^ {* *} + r _ {3}} \left( \begin{array}{c c c c c} 1 & 0 & 0 & - 1 & 0 \\ 0 & 1 & 0 & - 1 & - 1 \\ 0 & 0 & 1 & - 1 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>由上可知，<equation>r(\mathbf{A},\boldsymbol{\beta}) = r(\mathbf{A}) = 3 < 4</equation>，<equation>Ax = \boldsymbol{\beta}</equation>有无穷多解.

齐次方程组<equation>Ax = 0</equation>的通解为<equation>k(1,1,1,1)^{\mathrm{T}}</equation>，其中<equation>k</equation>为任意常数。又因为<equation>(0,-1,0,0)^{\mathrm{T}}</equation>为<equation>Ax = \beta</equation>的一个特解，所以<equation>Ax = \beta</equation>的通解为<equation>k(1,1,1,1)^{\mathrm{T}} + (0,-1,0,0)^{\mathrm{T}}</equation>，其中<equation>k</equation>为任意常数综上所述，当<equation>a = -1</equation>时，方程组<equation>Ax = \beta</equation>有无穷多解，其通解为<equation>k(1,1,1,1)^{\mathrm{T}} + (0,-1,0,0)^{\mathrm{T}}</equation>其中<equation>k</equation>为任意常数.

（法二）对含有参数<equation>a</equation>的增广矩阵<equation>(A, \beta)</equation>作初等行变换.<equation>(\boldsymbol {A}, \boldsymbol {\beta}) = \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ a & 0 & 0 & 1 & 0 \end{array} \right) \xrightarrow {r _ {4} - a r _ {1}} \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ 0 & - a ^ {2} & 0 & 1 & - a \end{array} \right)</equation><equation>\xrightarrow {r _ {4} ^ {*} + a ^ {2} r _ {2}} \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ 0 & 0 & a ^ {3} & 1 & - a - a ^ {2} \end{array} \right) \xrightarrow {r _ {4} ^ {* *} - a ^ {3} r _ {3}} \left( \begin{array}{c c c c c} 1 & a & 0 & 0 & 1 \\ 0 & 1 & a & 0 & - 1 \\ 0 & 0 & 1 & a & 0 \\ 0 & 0 & 0 & 1 - a ^ {4} & - a - a ^ {2} \end{array} \right).</equation>由于<equation>A x=\beta</equation>有无穷多解，故<equation>r(A)=r(A,\beta) < 4.</equation>因此，<equation>1-a^{4}=0,-a-a^{2}=0</equation>解得 a=-1其余同法一.

---

**2011年第6题 | 选择题 | 4分 | 答案: C**

6. 设 A为<equation>4 \times3</equation>矩阵，<equation>\eta_{1},\eta_{2},\eta_{3}</equation>是非齐次线性方程组<equation>A x=\beta</equation>的3个线性无关的解，<equation>k_{1},k_{2}</equation>为任意常数，则<equation>A x=\beta</equation>的通解为（    )

A.<equation>\frac{\eta_{2}+\eta_{3}}{2}+k_{1}(\eta_{2}-\eta_{1})</equation>B.<equation>\frac{\eta_{2}-\eta_{3}}{2}+k_{1}(\eta_{2}-\eta_{1})</equation>C.<equation>\frac{\eta_{2}+\eta_{3}}{2}+k_{1}(\eta_{2}-\eta_{1})+k_{2}(\eta_{3}-\eta_{1})</equation>D.<equation>\frac{\eta_{2}-\eta_{3}}{2}+k_{1}(\eta_{2}-\eta_{1})+k_{2}(\eta_{3}-\eta_{1})</equation>

答案: C

**解析:**解 由于<equation>Ax = \beta</equation>为非齐次线性方程组，故<equation>\beta \neq 0</equation>，从而<equation>A\neq O</equation>，即<equation>r(A)\geqslant 1.</equation>于是<equation>Ax = 0</equation>的基础解系里最多只含有2个线性无关的解。又由于<equation>\eta_{1},\eta_{2},\eta_{3}</equation>是<equation>Ax = \beta</equation>的3个线性无关的解，故<equation>\eta_{2} - \eta_{1}</equation><equation>\eta_{3} - \eta_{1}</equation>为<equation>Ax = 0</equation>的解且线性无关（证明见注<equation>\textcircled{2}</equation>），从而<equation>r(A)\leqslant 1.</equation>因此，<equation>r(A) = 1</equation>，<equation>Ax = 0</equation>的通解为<equation>k_{1}(\eta_{2} - \eta_{1}) + k_{2}(\eta_{3} - \eta_{1})</equation>，其中<equation>k_{1},k_{2}</equation>为任意常数.

又因为<equation>A\cdot \frac{\eta_{2}+\eta_{3}}{2}=\frac{A\eta_{2}+A\eta_{3}}{2}=\frac{\beta+\beta}{2}=\beta</equation>，即<equation>\frac{\eta_{2}+\eta_{3}}{2}</equation>为<equation>A x=\beta</equation>的解，所以<equation>A x=\beta</equation>的通解为<equation>\frac{\eta_{2}+\eta_{3}}{2}+k_{1}(\eta_{2}-\eta_{1})+k_{2}(\eta_{3}-\eta_{1})</equation>，其中<equation>k_{1},k_{2}</equation>为任意常数.应选C.

下面我们说明选项A、B、D均不正确.

由于<equation>A x=0</equation>的基础解系中包含2个向量，故选项A、B均不正确.

对选项D，<equation>\frac{\eta_{2}-\eta_{3}}{2}</equation>是<equation>A x=0</equation>的解，却不是<equation>A x=\beta</equation>的解，故选项D也不正确.

---

**2010年第20题 | 解答题 | 11分**

20. (本题满分11分)

设<equation>A=\left( \begin{array}{c c c} \lambda & 1 & 1 \\ 0 & \lambda-1 & 0 \\ 1 & 1 & \lambda \end{array} \right), b=\left( \begin{array}{c} a \\ 1 \\ 1 \end{array} \right).</equation>已知线性方程组<equation>A x=b</equation>存在两个不同的解.

I. 求<equation>\lambda, a;</equation>II. 求方程组<equation>A x=b</equation>的通解.

**答案:**（20）（I<equation>\lambda=-1</equation><equation>a=-2;</equation>（Ⅱ）<equation>k(1,0,1)^{\mathrm{T}}+\left(\frac{3}{2},-\frac{1}{2},0\right)^{\mathrm{T}}</equation>为<equation>A x=b</equation>的通解，其中k为任意常数.

**解析:**解（I）（法一）<equation>A x=b</equation>有两个不同的解意味着<equation>A x=b</equation>有解但不唯一，故<equation>r ( A )=r ( A , b ) < 3.</equation><equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} \lambda & 1 & 1 & a \\ 0 & \lambda - 1 & 0 & 1 \\ 1 & 1 & \lambda & 1 \end{array} \right) \xrightarrow {r _ {1} \leftrightarrow r _ {3}} \left( \begin{array}{c c c c} 1 & 1 & \lambda & 1 \\ 0 & \lambda - 1 & 0 & 1 \\ \lambda & 1 & 1 & a \end{array} \right) \xrightarrow {r _ {3} ^ {*} - \lambda r _ {1} ^ {*}} \left( \begin{array}{c c c c} 1 & 1 & \lambda & 1 \\ 0 & \lambda - 1 & 0 & 1 \\ 0 & 1 - \lambda & 1 - \lambda^ {2} & a - \lambda \end{array} \right) \\ \xrightarrow {r _ {3} ^ {* *} + r _ {2}} \left( \begin{array}{c c c c} 1 & 1 & \lambda & 1 \\ 0 & \lambda - 1 & 0 & 1 \\ 0 & 0 & 1 - \lambda^ {2} & a - \lambda + 1 \end{array} \right). \\ \end{array}</equation>(<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每做一次初等行变换，加一个*.）

由于<equation>r(A) < 3</equation>，故<equation>(\lambda -1)(1 - \lambda^2) = 0, \lambda = \pm 1.</equation>当<equation>\lambda = 1</equation>时，<equation>r(A,b) = 2</equation>，<equation>r(A) = 1</equation>，方程组无解，舍去.

当<equation>\lambda=-1</equation>时，<equation>(A,b)\rightarrow \left( \begin{array}{c c c c}1&1&-1&1\\ 0&-2&0&1\\ 0&0&0&a+2 \end{array} \right).</equation>此时<equation>r(A)=2.</equation>若<equation>r(A)=r(A,b)</equation>，则<equation>r(A,b)=2, a+2=0</equation>即<equation>a=-2.</equation>因此，<equation>\lambda=-1</equation>a=-2.

（法二）<equation>A x=b</equation>有两个不同的解意味着<equation>A x=b</equation>有解但不唯一，故<equation>r(A)=r(A,b)<3</equation>从而<equation>|A|=0.</equation><equation>| A | = \left| \begin{array}{c c c} \lambda & 1 & 1 \\ 0 & \lambda - 1 & 0 \\ 1 & 1 & \lambda \end{array} \right| = (\lambda - 1) ^ {2} (\lambda + 1) = 0.</equation>因此，<equation>\lambda=\pm1.</equation>当<equation>\lambda=1</equation>时，<equation>(\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} 1 & 1 & 1 & a \\ 0 & 0 & 0 & 1 \\ 1 & 1 & 1 & 1 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c c} 1 & 1 & 1 & a \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 1 - a \end{array} \right).</equation><equation>r(\mathbf{A}) = 1 < r(\mathbf{A},\mathbf{b}) = 2</equation>，原方程组无解.

当<equation>\lambda = -1</equation>时，同法一的方法对<equation>(A, b)</equation>作初等行变换可得<equation>(\boldsymbol {A}, \boldsymbol {b}) = \left( \begin{array}{c c c c} - 1 & 1 & 1 & a \\ 0 & - 2 & 0 & 1 \\ 1 & 1 & - 1 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & 1 & - 1 & 1 \\ 0 & - 2 & 0 & 1 \\ 0 & 0 & 0 & a + 2 \end{array} \right).</equation>当<equation>a + 2 = 0</equation>，即<equation>a = -2</equation>时，<equation>r(\mathbf{A}) = r(\mathbf{A},\mathbf{b}) = 2 < 3</equation>，原方程组有无穷多解.

因此，<equation>\lambda=-1</equation>，a=-2.

（Ⅱ）由第（I）问知，当<equation>\lambda=-1</equation>a=-2时，<equation>(A, b) \rightarrow \left(\begin{array}{c c c c}1&1&- 1&1\\0&- 2&0&1\\0&0&0&0\end{array}\right) \xrightarrow {r _ {2} \times \left(- \frac {1}{2}\right)} \frac {r _ {2} \times \left(- \frac {1}{2}\right)}{r _ {1} - r _ {2} ^ {*}} \left(\begin{array}{c c c c}1&0&- 1&\frac {3}{2}\\\0&1&0&- \frac {1}{2}\\\0&0&0&0\end{array}\right).</equation>其对应的齐次方程组等价于<equation>\left\{\begin{array}{l l}x_{1}-x_{3}=0,\\ x_{2}=0,\end{array}\right.</equation>故可取（1，0，1）<equation>^{\mathrm{T}}</equation>为该方程组的一个基础解系.又<equation>\left(\frac{3}{2},-\frac{1}{2},0\right)^{\mathrm{T}}</equation>为原方程组的一个特解，故<equation>A x=b</equation>的通解为<equation>k(1,0,1)^{\mathrm{T}}+\left(\frac{3}{2},-\frac{1}{2},0\right)^{\mathrm{T}}</equation>其中k为任意常数.

---


### 矩阵的特征值和特征向量


#### 矩阵的相似与相似对角化

**2025年第6题 | 选择题 | 5分 | 答案: B**

6. 设 A为三阶矩阵，则“<equation>A^{3}-A^{2}</equation>”可对角化是“ A可对角化”的（    ）

A. 充分但不必要条件 B. 必要但不充分条件

C. 充分必要条件 D. 既不充分也不必要条件

答案: B

**解析:**解 若 A可相似对角化，则存在可逆矩阵 P，使得<equation>P^{-1} A P=A</equation>，其中 A为对角矩阵.由此可得 A = P A P^{-1} ，进一步可得<equation>A^{2}=P A^{2} P^{-1}, A^{3}=P A^{3} P^{-1}</equation>，从而<equation>A ^ {3} - A ^ {2} = P A ^ {3} P ^ {- 1} - P A ^ {2} P ^ {- 1} = P \left(A ^ {3} - A ^ {2}\right) P ^ {- 1},</equation>即<equation>P^{-1}\left(A^{3} - A^{2}\right)P = A^{3} - A^{2}</equation>.

因此，<equation>A^{3}-A^{2}</equation>可相似对角化，“<equation>A^{3}-A^{2}</equation>可对角化”是“<equation>A</equation>可对角化”的必要条件.

但是由“<equation>A^{3}-A^{2}</equation>可对角化”却不能推出“<equation>A</equation>可对角化”.

若<equation>\alpha</equation>为矩阵 A的属于特征值<equation>\lambda</equation>的特征向量，即<equation>A\alpha=\lambda\alpha</equation>，则<equation>A^{k}\alpha=\lambda^{k}\alpha</equation>，即<equation>\alpha</equation>也是<equation>A^{k}</equation>的属于特征值<equation>\lambda^{k}</equation>的特征向量.但反之并不成立.

例如，取<equation>A = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>，则<equation>A^{3} = A^{2} = O, A^{3} - A^{2}</equation>有3个线性无关的特征向量，从而可相似对

角化. 但是 A的特征值0是三重特征值，而<equation>r ( A )=1</equation>，故 A只有 3-1=2个线性无关的属于0的特征向量，从而不能相似对角化.

因此，“<equation>A^{3}-A^{2}</equation>可对角化”不是“<equation>A</equation>可对角化”的充分条件.

综上所述，应选B.

---

**2023年第21题 | 解答题 | 12分**

21. (本题满分12分)

设矩阵 A满足：对任意<equation>x_{1}, x_{2}, x_{3}</equation>均有<equation>A\left( \begin{array}{c} x_{1} \\ x_{2} \\ x_{3} \end{array} \right)=\left( \begin{array}{c} x_{1}+x_{2}+x_{3} \\ 2 x_{1}-x_{2}+x_{3} \\ x_{2}-x_{3} \end{array} \right)</equation>I. 求 A;

II. 求可逆矩阵<equation>P</equation>与对角矩阵<equation>\Lambda</equation>, 使得<equation>P^{-1}AP = \Lambda</equation>.

**答案:**<equation>\begin{aligned} (\mathrm {I}) \boldsymbol {A} &= \left( \begin{array}{c c c} 1 & 1 & 1 \\ 2 & - 1 & 1 \\ 0 & 1 & - 1  \right); \\ (\mathrm {I I}) \boldsymbol {P} &= \left( \begin{array}{c c c} 0 & - 1 & 4 \\ - 1 & 0 & 3 \\ 1 & 2 & 1  \right), \boldsymbol {A} &= \left( \begin{array}{c c c} - 2 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 2  \right). \end{aligned}</equation>

**解析:**（ I ）因为<equation>\begin{aligned} \mathbf {A} \left(  x _ {1} \\ x _ {2} \\ x _ {3}  \right) &= \left(  x _ {1} + x _ {2} + x _ {3} \\ 2 x _ {1} - x _ {2} + x _ {3} \\ x _ {2} - x _ {3}  \right) &= \left( \begin{array}{c c c} 1 & 1 & 1 \\ 2 & - 1 & 1 \\ 0 & 1 & - 1  \right) \left(  x _ {1} \\ x _ {2} \\ x _ {3}  \right) \end{aligned}</equation>对任意<equation>x_{1}, x_{2}, x_{3}</equation>均成立，所以方程组<equation>\left[ A-\left( \begin{array}{c c c} 1 & 1 & 1 \\ 2 & -1 & 1 \\ 0 & 1 & -1 \end{array} \right) \right] \left( \begin{array}{l} x_{1} \\ x_{2} \\ x_{3} \end{array} \right)=\mathbf{0}</equation>的解为全体3维列向量.于是该方程组的系数矩阵的秩为0，从而<equation>A-\left( \begin{array}{c c c} 1 & 1 & 1 \\ 2 & -1 & 1 \\ 0 & 1 & -1 \end{array} \right)=\mathbf{0}</equation>即<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & 1 & 1 \\ 2 & - 1 & 1 \\ 0 & 1 & - 1 \end{array} \right).</equation>（Ⅱ）计算 A的特征值. A的特征多项式为<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - 1 & - 1 & - 1 \\ - 2 & \lambda + 1 & - 1 \\ 0 & - 1 & \lambda + 1  \right| \xlongequal {\text {按 第三 行 展开}} \left| \begin{array}{c c} \lambda - 1 & - 1 \\ - 2 & - 1  \right| + (\lambda + 1) \left| \begin{array}{c c} \lambda - 1 & - 1 \\ - 2 & \lambda + 1  \right| \\ &= - (\lambda + 1) + (\lambda + 1) \left(\lambda^ {2} - 3\right) = (\lambda + 1) \left(\lambda^ {2} - 4\right) \\ &= (\lambda + 1) (\lambda + 2) (\lambda - 2). \end{aligned}</equation>于是，A的特征值为-2，-1，2.

计算 A的属于特征值-2的特征向量.考虑方程组<equation>(-2 E-A) x=0.</equation><equation>- 2 E - A = \left( \begin{array}{c c c} - 3 & - 1 & - 1 \\ - 2 & - 1 & - 1 \\ 0 & - 1 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} - 3 & 0 & 0 \\ - 2 & 0 & 0 \\ 0 & 1 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>解方程组<equation>(-2 E-A) x=0</equation>可得<equation>\left( \begin{array}{c}0\\ -1\\ 1 \end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c}0\\ -1\\ 1 \end{array} \right)</equation>为A的属于特征值 -2的一个特征向量.

计算 A的属于特征值-1的特征向量.考虑方程组<equation>(- E-A) x=0.</equation><equation>- \boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} - 2 & - 1 & - 1 \\ - 2 & 0 & - 1 \\ 0 & - 1 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 2 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>解方程组<equation>(- E-A) x=0</equation>可得<equation>\left( \begin{array}{c}-1\\0\\2 \end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c}-1\\0\\2 \end{array} \right)</equation>为 A的属于特征值 -1的一个特征向量.

计算 A的属于特征值2的特征向量.考虑方程组（2E-A）<equation>x=0.</equation><equation>2 E - A = \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ - 2 & 3 & - 1 \\ 0 & - 1 & 3 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ 0 & 1 & - 3 \\ 0 & - 1 & 3 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & - 4 \\ 0 & 1 & - 3 \\ 0 & 0 & 0 \end{array} \right).</equation>解方程组<equation>( 2 E-A ) x=0</equation>可得<equation>\left( \begin{array}{c c c} 4 \\ 3 \\ 1 \end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c} 4 \\ 3 \\ 1 \end{array} \right)</equation>为A的属于特征值2的一个特征向量.

令<equation>P=\left( \begin{array}{c c c} 0 & -1 & 4 \\ -1 & 0 & 3 \\ 1 & 2 & 1 \end{array} \right).</equation>由于属于不同特征值的特征向量线性无关，故P的列向量组线性无关，从而P可逆.由特征向量的性质可得<equation>P^{-1} A P=A</equation>其中<equation>\Lambda=\left( \begin{array}{c c c} -2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>

---

**2022年第5题 | 选择题 | 5分 | 答案: B**

5. 设 A为3阶矩阵，<equation>\Lambda=\left( \begin{array}{c c c} {1} & {0} & {0} \\ {0} & {-1} & {0} \\ {0} & {0} & {0} \end{array} \right)</equation>，则 A的特征值为1，-1，0的充分必要条件是（    )

A. 存在可逆矩阵 P,Q，使得<equation>A=P\Lambda Q</equation>B. 存在可逆矩阵 P，使得<equation>A=P\Lambda P^{-1}</equation>C. 存在正交矩阵 Q，使得<equation>A=Q\Lambda Q^{-1}</equation>D. 存在可逆矩阵 P，使得<equation>A=P\Lambda P^{\mathrm{T}}</equation>

答案: B

**解析:**解3阶矩阵 A的特征值为1，-1，0意味着 A有3个不同的特征值，从而 A相似于与它具有相同特征值的对角矩阵，即<equation>\Lambda</equation>.于是，A的特征值为1，-1，0的充分必要条件即 A与<equation>\Lambda</equation>相似的充分必要条件.

选项B实际上为 A与<equation>\Lambda</equation>相似的定义，即存在可逆矩阵 P，使得<equation>\Lambda = P^{-1}AP</equation>，也即<equation>A=P\Lambda P^{-1}</equation>因此，应选B.

下面说明选项A、C、D不正确.

选项A是A与A等价的定义.若两矩阵相似，则它们必等价，但两个等价的矩阵不一定相似，如<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>和<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>，故选项A是A与A相似的必要不充分条件.

因为正交矩阵也是可逆矩阵，所以选项C是A与A相似的充分条件.但选项C并不是A与A相似的必要条件，因为A不一定能找到一组相互正交的特征向量，这一要求对实对称矩阵成立，对一般矩阵不成立.

取<equation>\boldsymbol{\xi}_{1}=\left( \begin{array}{c}1\\ 0\\ 0 \end{array} \right),\boldsymbol{\xi}_{2}=\left( \begin{array}{c}1\\ 1\\ 0 \end{array} \right),\boldsymbol{\xi}_{3}=\left( \begin{array}{c}1\\ 0\\ 1 \end{array} \right)</equation>，则<equation>\boldsymbol{\xi}_{1},\boldsymbol{\xi}_{2},\boldsymbol{\xi}_{3}</equation>相互均不正交.令<equation>P=(\boldsymbol{\xi}_{1},\boldsymbol{\xi}_{2},\boldsymbol{\xi}_{3})</equation>，<equation>\Lambda=</equation><equation>\left( \begin{array}{c c c}1&0&0\\ 0&-1&0\\ 0&0&0 \end{array} \right)</equation>，则<equation>A=P \Lambda P^{-1}=\left( \begin{array}{lll} 1 & 1 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)\left( \begin{array}{lll} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 0 \end{array} \right)\left( \begin{array}{lll} 1 & -1 & -1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)=\left( \begin{array}{lll} 1 & -2 & -1 \\ 0 & -1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>A与对角矩阵 A相似，但是 A的线性无关的特征向量均不正交.

选项D是A与A合同的定义.对一般矩阵而言，相似与合同之间并无相互蕴含的关系.

考虑选项A的反例<equation>\left( \begin{array}{c c c}1&0&0\\ 0&0&0\\ 0&0&0 \end{array} \right)</equation>和<equation>\left( \begin{array}{c c c}2&0&0\\ 0&0&0\\ 0&0&0 \end{array} \right)</equation>，这两个矩阵具有相同的正、负惯性指数，从而合同，但它们并不相似.

考虑选项C的反例<equation>A=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 0 \end{array} \right), A=\left( \begin{array}{c c c} 1 & -2 & -1 \\ 0 & -1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>由前面的分析可知，A与A相似又因为A是实对称矩阵，而与实对称矩阵合同的矩阵一定是实对称矩阵，但A不是实对称矩阵，所以A与A不合同.

因此，选项D既不是A与A相似的充分条件，也不是A与A相似的必要条件.

---

**2021年第21题 | 解答题 | 12分**

21. (本题满分12分)

设矩阵<equation>A = \left( \begin{array}{c c c} 2 & 1 & 0 \\ 1 & 2 & 0 \\ 1 & a & b \end{array} \right)</equation>仅有两个不同的特征值，若 A相似于对角矩阵，求 a,b的值，并求可逆矩阵 P，使<equation>P^{-1} A P</equation>为对角矩阵.

**答案:**当 a = 1,b = 1时，<equation>P=\left( \begin{array}{c c c} - 1 & 0 & 1 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right), P^{-1} A P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 3 \end{array} \right)</equation>为对角矩阵.

当 a = -1,b = 3时，<equation>P=\left( \begin{array}{c c c} 1 & 0 & - 1 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right), P^{-1} A P=\left( \begin{array}{c c c} 3 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>为对角矩阵.

**解析:**计算 A的特征多项式.<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - 2 & - 1 & 0 \\ - 1 & \lambda - 2 & 0 \\ - 1 & - a & \lambda - b  \right| \xlongequal {\text {按 第三 列 展 开}} (\lambda - b) \left| \begin{array}{c c} \lambda - 2 & - 1 \\ - 1 & \lambda - 2  \right| \\ &= (\lambda - b) \left[ (\lambda - 2) ^ {2} - 1 \right] = (\lambda - 1) (\lambda - 3) (\lambda - b). \end{aligned}</equation>A的所有特征值为1,3,b.

若 A仅有两个不同的特征值，则 b只可能为1或者3.

下面分情况讨论.

(1) 若 b=1，则 A的特征值为1,1,3.

计算 A的属于特征值1的特征向量.考虑 （E-A）x=0.<equation>\boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} - 1 & - 1 & 0 \\ - 1 & - 1 & 0 \\ - 1 & - a & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 - a & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>若 A可相似对角化，则方程组<equation>( E-A ) x=0</equation>有两个线性无关的解. r(E-A) =1.于是，a=1解方程组<equation>( E-A ) x=0</equation>可得<equation>\left( \begin{array}{c}-1\\1\\0\end{array} \right)</equation>与<equation>\left( \begin{array}{c}0\\0\\1\end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c}-1\\1\\0\end{array} \right)</equation>与<equation>\left( \begin{array}{c}0\\0\\1\end{array} \right)</equation>为 A的属于特征值1的两个线性无关的特征向量.

计算 A的属于特征值3的特征向量.考虑<equation>( 3 E-A ) x=0.</equation><equation>3 E - A = \left( \begin{array}{c c c} 1 & - 1 & 0 \\ - 1 & 1 & 0 \\ - 1 & - 1 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & - 1 & 0 \\ 0 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right).</equation>解方程组<equation>( 3 E-A ) x=0</equation>可得<equation>\left( \begin{array}{c c c} 1 \\ 1 \\ 1 \end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c} 1 \\ 1 \\ 1 \end{array} \right)</equation>为A的属于特征值3的一个特征向量.

令<equation>P=\left( \begin{array}{c c c} -1 & 0 & 1 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right)</equation>，则<equation>P^{-1} A P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 3 \end{array} \right)</equation>为对角矩阵.

(2) 若 b=3，则 A的特征值为1,3,3.

计算 A的属于特征值3的特征向量.考虑<equation>( 3 E-A ) x=0.</equation><equation>3 E - A = \left( \begin{array}{c c c} 1 & - 1 & 0 \\ - 1 & 1 & 0 \\ - 1 & - a & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & - 1 & 0 \\ 0 & - 1 - a & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>若 A可相似对角化，则方程组（3E-A）<equation>x=0</equation>有两个线性无关的解. r（3E-A）=1.于是，a=-1.解方程组（3E-A）<equation>x=0</equation>可得<equation>\left( \begin{array}{l} 1 \\ 1 \\ 0 \end{array} \right)</equation>与<equation>\left( \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{l} 1 \\ 1 \\ 0 \end{array} \right)</equation>与<equation>\left( \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right)</equation>为 A的属于特征值3的两个线性无关的特征向量.

计算 A的属于特征值1的特征向量.考虑 （E-A）x=0.<equation>\boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} - 1 & - 1 & 0 \\ - 1 & - 1 & 0 \\ - 1 & 1 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right).</equation>解方程组<equation>( E-A ) x=0</equation>可得<equation>\left( \begin{array}{c c c} - 1 \\ 1 \\ 1 \end{array} \right)</equation>为该方程组的一个基础解系，即<equation>\left( \begin{array}{c c} - 1 \\ 1 \\ 1 \end{array} \right)</equation>为 A的属于特征值1的一个特征向量.

令<equation>P=\left( \begin{array}{c c c} 1 & 0 & - 1 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right)</equation>，则<equation>P^{-1} A P=\left( \begin{array}{c c c} 3 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>为对角矩阵.

---

**2020年第21题 | 解答题 | 11分**

21. (本题满分11分)

设 A为2阶矩阵，<equation>P=(\alpha ,A\alpha)</equation>，其中<equation>\alpha</equation>是非零向量且不是 A的特征向量.

I. 证明 P为可逆矩阵；

II. 若<equation>A^{2}\alpha+A\alpha-6\alpha=0</equation>，求<equation>P^{-1}AP</equation>，并判断 A是否相似于对角矩阵.

**答案:**（I）证明略；

（Ⅱ）<equation>P^{-1} A P=\left( \begin{array}{cc} 0 & 6 \\ 1 & -1 \end{array} \right)</equation>，A相似于对角矩阵<equation>\left( \begin{array}{c c} 2 & 0 \\ 0 & -3 \end{array} \right)</equation>

**解析:**解（I）要证明 P为可逆矩阵，可证明<equation>\alpha, A\alpha</equation>线性无关.

假设<equation>\alpha, A\alpha</equation>线性相关，则存在不全为零的常数<equation>k_{1}, k_{2}</equation>，使得<equation>k_{1}\alpha+k_{2}A\alpha=0.</equation>若<equation>k_{2}=0</equation>，则<equation>k_{1}\alpha=0</equation>.但<equation>\alpha</equation>为非零向量，故<equation>k_{1}=0</equation>.这与假设矛盾.

若<equation>k_{2}\neq 0</equation>，则<equation>A\alpha=-\frac{k_{1}}{k_{2}}\alpha</equation>.由特征向量的定义可知<equation>\alpha</equation>为A的特征向量.这与<equation>\alpha</equation>不是A的特征向量矛盾.

因此，<equation>\alpha, A\alpha</equation>线性无关.P为可逆矩阵.

（Ⅱ）考虑AP.<equation>\begin{aligned} A P &= \left(A \alpha , A ^ {2} \alpha\right) \xlongequal {A ^ {2} \alpha + A \alpha - 6 \alpha = 0} \left(A \alpha , 6 \alpha - A \alpha\right) = (\alpha , A \alpha) \left( \begin{array}{c c} 0 & 6 \\ 1 & - 1  \right) \\ &= P \left( \begin{array}{c c} 0 & 6 \\ 1 & - 1  \right). \end{aligned}</equation>由第（I）问可知，P可逆.上式两端同时左乘<equation>P^{-1}</equation>可得<equation>P^{-1} A P=\left( \begin{array}{cc}0&6\\ 1&-1 \end{array} \right).</equation>记<equation>B=\left( \begin{array}{cc}0&6\\ 1&-1 \end{array} \right)</equation>，则A与B相似.A与对角矩阵相似等价于B与对角矩阵相似.

计算 B的特征多项式.<equation>| \lambda E - B | = \left| \begin{array}{c c} \lambda & - 6 \\ - 1 & \lambda + 1 \end{array} \right| = \lambda^ {2} + \lambda - 6 = (\lambda + 3) (\lambda - 2).</equation>2与-3是B的两个不同特征值.于是，B相似于对角矩阵<equation>\left( \begin{array}{cc}2&0\\ 0&-3 \end{array} \right).</equation>由相似关系的传递性可知，A相似于对角矩阵<equation>\left( \begin{array}{cc}2&0\\ 0&-3 \end{array} \right).</equation>

---

**2019年第21题 | 解答题 | 11分**

21. （本题满分11分）

已知矩阵<equation>A = \left( \begin{array}{c c c} - 2 & - 2 & 1 \\ 2 & x & - 2 \\ 0 & 0 & - 2 \end{array} \right)</equation>与<equation>B = \left( \begin{array}{c c c} 2 & 1 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & y \end{array} \right)</equation>相似.

I. 求 x,y;

II. 求可逆矩阵<equation>P</equation>，使得<equation>P^{-1}AP = B</equation>.

**答案:**（ I ）<equation>x=3, y=-2;</equation>（Ⅱ）满足<equation>P^{-1} A P=B</equation>的可逆矩阵为<equation>\boldsymbol {P} = \left( \begin{array}{c c c} - 1 & - 1 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right).</equation>

**解析:**解（ I ）由于 A,B相似，故它们的迹与行列式均相同.

由 A,B有相同的迹可得<equation>- 4+x=1+y</equation>，即 x-y=5.

计算<equation>| A |, | B |. B</equation>为上三角矩阵，故易得<equation>| B |=-2 y.</equation><equation>| A | \xlongequal {\text {按 第三 行 展 开}} (- 2) \cdot \left| \begin{array}{c c} - 2 & - 2 \\ 2 & x \end{array} \right| = 4 x - 8.</equation>由<equation>| A | = | B |</equation>可得 4x-8=-2y，即 2x+y=4.

联立<equation>\left\{ \begin{array}{l l} x-y=5, \\ 2-y=-2. \end{array} \right.</equation>解得 x=3,y=-2.<equation>2 x + y = 4,</equation>（Ⅱ）由于 A,B相似，故它们有相同的特征值.

计算 B的特征多项式.<equation>| \lambda E - B | = \left| \begin{array}{c c c} \lambda - 2 & - 1 & 0 \\ 0 & \lambda + 1 & 0 \\ 0 & 0 & \lambda + 2 \end{array} \right| = (\lambda - 2) (\lambda + 1) (\lambda + 2).</equation>于是，B的特征值为2，-1，-2. 从而A的特征值也为2，-1，-2.

由于 A,B具有3个不同的特征值2，-1，-2，故存在可逆矩阵<equation>P_{1}, P_{2}</equation>，使得<equation>P_{1}^{-1} A P_{1}=</equation><equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -2 \end{array} \right), P_{2}^{-1} B P_{2}=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -2 \end{array} \right).</equation>令<equation>P=P_{1} P_{2}^{-1}</equation>，则<equation>P^{-1} A P=P_{2} P_{1}^{-1} A P_{1} P_{2}^{-1}=P_{2}\left(P_{1}^{-1} A P_{1}\right) P_{2}^{-1}=B.</equation><equation>P_{1}</equation>的列向量为A的属于特征值2，-1，-2的特征向量，<equation>P_{2}</equation>的列向量为B的属于特征值2，-1，-2的特征向量。下面分别计算A，B的特征向量.

计算 A的属于特征值2的特征向量.考虑（2E-A）x=0.<equation>2 E - A = \left( \begin{array}{c c c} 4 & 2 & - 1 \\ - 2 & - 1 & 2 \\ 0 & 0 & 4 \end{array} \right) \xrightarrow [ r _ {1} + r _ {3} ^ {*} ]{r _ {3} \times \frac {1}{4}} \left( \begin{array}{c c c} 4 & 2 & 0 \\ - 2 & - 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {2} ^ {*} \times (- 1) ]{r _ {1} ^ {*} + 2 r _ {2} ^ {*}} \left( \begin{array}{c c c} 0 & 0 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>于是，<equation>r ( 2 E-A )=2</equation>，求得<equation>\boldsymbol{\xi}_{1}=(-1,2,0)^{\mathrm{T}}</equation>为<equation>( 2 E-A ) x=0</equation>的一个基础解系.<equation>(-1,2,0)^{\mathrm{T}}</equation>为 A的属于特征值2的特征向量.

计算 A的属于特征值-1的特征向量.考虑<equation>(- E-A) x=0.</equation><equation>- E - A = \left( \begin{array}{c c c} 1 & 2 & - 1 \\ - 2 & - 4 & 2 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {1} + r _ {3} ]{r _ {2} + 2 r _ {1}} \left( \begin{array}{c c c} 1 & 2 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>于是，<equation>r(-E-A)=2</equation>，求得<equation>\xi_{2}=(-2,1,0)^{\mathrm{T}}</equation>为<equation>(-E-A)x=0</equation>的一个基础解系.<equation>(-2,1,0)^{\mathrm{T}}</equation>为 A的属于特征值-1的特征向量.

计算 A的属于特征值-2的特征向量.考虑<equation>(-2 E-A) x=0.</equation><equation>- 2 E - A = \left( \begin{array}{c c c} 0 & 2 & - 1 \\ - 2 & - 5 & 2 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {2} + 2 r _ {1}} \left( \begin{array}{c c c} 0 & 2 & - 1 \\ - 2 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {2} ^ {*} \times (- 2) - r _ {1}} \left( \begin{array}{c c c} 0 & 2 & - 1 \\ 4 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r(-2 E-A)=2</equation>，求得<equation>\xi_{3}=(-1,2,4)^{\mathrm{T}}</equation>为<equation>(-2 E-A) x=0</equation>的一个基础解系.<equation>(-1,2,4)^{\mathrm{T}}</equation>为 A的属于特征值-2的特征向量.<equation>P _ {1}</equation><equation>\left( \begin{array}{c c c} - 1 & - 2 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right)</equation>计算 B的属于特征值2的特征向量.考虑（2E-B）x=0.<equation>2 E - B = \left( \begin{array}{c c c} 0 & - 1 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r ( 2 E-B)=2</equation>，求得<equation>\boldsymbol{\eta}_{1}^{\prime}=(1,0,0)^{\mathrm{T}}</equation>为（2E-B）<equation>\boldsymbol{x}=\mathbf{0}</equation>的一个基础解系. （1，0，0）<equation>^{\mathrm{T}}</equation>为B的属于特征值2的特征向量.

计算 B的属于特征值-1的特征向量.考虑<equation>(- E-B) x=0.</equation><equation>- \boldsymbol {E} - \boldsymbol {B} = \left( \begin{array}{c c c} - 3 & - 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {2} \leftrightarrow r _ {3} ]{r _ {1} \times (- 1)} \left( \begin{array}{c c c} 3 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r(-E-B)=2</equation>，求得<equation>\eta_{2}=(-1,3,0)^{\mathrm{T}}</equation>为<equation>(-E-B)x=0</equation>的一个基础解系.<equation>(-1,3,0)^{\mathrm{T}}</equation>为 B的属于特征值-1的特征向量.

计算 B的属于特征值-2的特征向量.考虑<equation>(-2 E-B) x=0.</equation><equation>- 2 E - B = \left( \begin{array}{c c c} - 4 & - 1 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {2} \times (- 1) ]{r _ {1} \times (- 1)} \left( \begin{array}{c c c} 4 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r(-2 E-B)=2</equation>，求得<equation>\eta_{3}=(0,0,1)^{\mathrm{T}}</equation>为<equation>(-2 E-B) x=0</equation>的一个基础解系.<equation>(0,0,1)^{\mathrm{T}}</equation>为 B的属于特征值-2的特征向量.

因此，<equation>P_{2}</equation>可取为<equation>\left( \begin{array}{c c c} 1 & -1 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>利用初等变换法计算<equation>P_{2}^{-1}</equation><equation>\left(\boldsymbol {P} _ {2}, \boldsymbol {E}\right) = \left( \begin{array}{c c c c c c} 1 & - 1 & 0 & 1 & 0 & 0 \\ 0 & 3 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {1} + r _ {2} ^ {*} ]{r _ {2} \times \frac {1}{3}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 1 & \frac {1}{3} & 0 \\ 0 & 1 & 0 & 0 & \frac {1}{3} & 0 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{array} \right).</equation>于是，<equation>P_{2}^{-1}=\left( \begin{array}{c c c} 1 & \frac{1}{3} & 0 \\ 0 & \frac{1}{3} & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>综上所述，<equation>\boldsymbol {P} = \boldsymbol {P} _ {1} \boldsymbol {P} _ {2} ^ {- 1} = \left( \begin{array}{c c c} - 1 & - 2 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right) \left( \begin{array}{c c c} 1 & \frac {1}{3} & 0 \\ 0 & \frac {1}{3} & 0 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} - 1 & - 1 & - 1 \\ 2 & 1 & 2 \\ 0 & 0 & 4 \end{array} \right).</equation>

---

**2018年第5题 | 选择题 | 4分 | 答案: A**

5. 下列矩阵中，与矩阵<equation>\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>A.

相似的为（    ）<equation>\left( \begin{array}{c c c} 1 & 1 & - 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c} 1 & 1 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>

答案: A

**解析:**解 已知矩阵与四个选项中的矩阵的特征多项式均为<equation>( x-1 )^{3}</equation>，故1为这五个矩阵的三重特征值.

记<equation>A=\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E-A=\left( \begin{array}{c c c} 0 & -1 & 0 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{array} \right).</equation>.于是<equation>r(E-A)=2.</equation>记<equation>B_{1}=\left( \begin{array}{c c c} 1 & 1 & -1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E-B_{1}=\left( \begin{array}{c c c} 0 & -1 & 1 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r \left( E-B_{1}\right) = 2.</equation>记<equation>B_{2}=\left( \begin{array}{c c c} 1 & 0 & -1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E-B_{2}=\left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r \left( E-B_{2}\right)=1.</equation>记<equation>B_{3}=\left( \begin{array}{c c c} 1 & 1 & -1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E-B_{3}=\left( \begin{array}{c c c} 0 & -1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r \left( E-B_{3}\right)=1.</equation>记<equation>B_{4} = \left( \begin{array}{c c c} 1 & 0 & -1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，则<equation>E - B_{4} = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>.于是<equation>r(\boldsymbol{E} - \boldsymbol{B}_4) = 1.</equation>由上可见，只有<equation>E - B_{1}</equation>与<equation>E - A</equation>的秩相等，而<equation>E - B_{i} ( i=2,3,4)</equation>与<equation>E - A</equation>的秩均不相等，故<equation>E - B_{i} ( i=2,3,4)</equation>与<equation>E - A</equation>不相似，从而A与<equation>B_{i} ( i=2,3,4)</equation>不相似.

由排除法可知，应选A.

---

**2017年第6题 | 选择题 | 4分 | 答案: B**

6. 已知矩阵<equation>A = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 1 \end{array} \right), B = \left( \begin{array}{c c c} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right), C = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{array} \right),</equation>则（    ）

A. A与 C相似，B与 C相似 B. A与 C相似，B与 C不相似

C. A与 C不相似，B与 C相似 D. A与 C不相似，B与 C不相似

答案: B

**解析:**解求得 A,B,C的特征多项式均为<equation>(\lambda-2)^{2} (\lambda-1)</equation>，故A,B,C具有相同的特征值，其中2是二重特征值.

矩阵 C是对角矩阵，故其相似于其自身.

考虑属于特征值2的特征向量.<equation>2 E - A = \left( \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 0 & - 1 \\ 0 & 0 & 1 \end{array} \right), \quad 2 E - B = \left( \begin{array}{c c c} 0 & - 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>由上可知，<equation>r ( 2 E-A )=1</equation><equation>r ( 2 E-B )=2</equation>.于是，<equation>( 2 E-A ) x=0</equation>的基础解系包含两个向量，故A有2个线性无关的属于特征值2的特征向量；而<equation>( 2 E-B ) x=0</equation>的基础解系只包含一个向量，故B只有1个属于特征值2的特征向量.

因此，加上属于特征值1的特征向量，A共有3个线性无关的特征向量，A与C相似；B只有2个线性无关的特征向量，B与C不相似.应选B.

---

**2016年第5题 | 选择题 | 4分 | 答案: C**

5. 设 A,B是可逆矩阵，且 A与 B相似，则下列结论错误的是（    )

A.<equation>A^{\mathrm{T}}</equation>与<equation>B^{\mathrm{T}}</equation>相似 B.<equation>A^{-1}</equation>与<equation>B^{-1}</equation>相似

C.<equation>A+A^{\mathrm{T}}</equation>与<equation>B+B^{\mathrm{T}}</equation>相似 D.<equation>A+A^{-1}</equation>与<equation>B+B^{-1}</equation>相似

答案: C

**解析:**由于 A与B相似，故存在可逆矩阵 P，使得<equation>B=P^{-1} A P.</equation>-<equation>\boldsymbol{B}^{\mathrm{T}}=\boldsymbol{P}^{\mathrm{T}}\boldsymbol{A}^{\mathrm{T}}(\boldsymbol{P}^{-1})^{\mathrm{T}}=\boldsymbol{P}^{\mathrm{T}}\boldsymbol{A}^{\mathrm{T}}(\boldsymbol{P}^{\mathrm{T}})^{-1}</equation>，选项A中的结论正确.

-<equation>B^{-1}=P^{-1} A^{-1} \left(P^{-1}\right)^{-1}=P^{-1} A^{-1} P</equation>，选项B中的结论正确.

- 由<equation>B=P^{-1} A P</equation>和<equation>B^{-1}=P^{-1} A^{-1} P</equation>可知，<equation>B+B^{-1}=P^{-1}(A+A^{-1}) P</equation>，选项D中的结论正确由排除法可知，应选C.

下面我们举例说明选项C不正确.

设<equation>A = \left( \begin{array}{cc}1 & 0\\ 0 & -1 \end{array} \right), P = \left( \begin{array}{cc}1 & 1\\ 2 & 1 \end{array} \right)</equation>，则<equation>P^{-1} = \left( \begin{array}{cc}-1 & 1\\ 2 & -1 \end{array} \right)</equation>. 令<equation>\boldsymbol {B} = \boldsymbol {P} ^ {- 1} \boldsymbol {A P} = \left( \begin{array}{c c} - 1 & 1 \\ 2 & - 1 \end{array} \right) \left( \begin{array}{c c} 1 & 0 \\ 0 & - 1 \end{array} \right) \left( \begin{array}{c c} 1 & 1 \\ 2 & 1 \end{array} \right) = \left( \begin{array}{c c} - 3 & - 2 \\ 4 & 3 \end{array} \right),</equation>则<equation>\boldsymbol {A} + \boldsymbol {A} ^ {\mathrm {T}} = \left( \begin{array}{c c} 2 & 0 \\ 0 & - 2 \end{array} \right), \quad \boldsymbol {B} + \boldsymbol {B} ^ {\mathrm {T}} = \left( \begin{array}{c c} - 6 & 2 \\ 2 & 6 \end{array} \right).</equation>计算<equation>A+A^{\mathrm{T}}</equation>的特征多项式得<equation>\lambda^{2}-4</equation>，计算<equation>B+B^{\mathrm{T}}</equation>的特征多项式得<equation>\lambda^{2}-40.</equation>因此<equation>\mathbf{A}+\mathbf{A}^{\mathrm{T}}</equation>和<equation>\mathbf{B}+\mathbf{B}^{\mathrm{T}}</equation>不相似.

---

**2016年第21题 | 解答题 | 11分**

21. （本题满分11分）

已知矩阵<equation>A = \left( \begin{array}{c c c} 0 & -1 & 1 \\ 2 & -3 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>I. 求<equation>A^{99}</equation>;

II. 设3阶矩阵<equation>B=(\alpha_{1},\alpha_{2},\alpha_{3})</equation>满足<equation>B^{2}=B A</equation>记<equation>B^{100}=(\beta_{1},\beta_{2},\beta_{3})</equation>将<equation>\beta_{1},\beta_{2},\beta_{3}</equation>分别表示为<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>的线性组合.

**答案:**(I)<equation>A^{99}=\left( \begin{array}{c c c} 2^{99}-2 & 1-2^{99} & 2-2^{98} \\ 2^{100}-2 & 1-2^{100} & 2-2^{99} \\ 0 & 0 & 0 \end{array} \right)</equation>（Ⅱ）<equation>\boldsymbol{\beta}_{1}=(2^{99}-2)\boldsymbol{\alpha}_{1}+(2^{100}-2)\boldsymbol{\alpha}_{2},\boldsymbol{\beta}_{2}=(1-2^{99})\boldsymbol{\alpha}_{1}+(1-2^{100})\boldsymbol{\alpha}_{2},\boldsymbol{\beta}_{3}=(2-2^{98})\boldsymbol{\alpha}_{1}</equation><equation>+ (2-2^{99})\boldsymbol{\alpha}_{2}.</equation>

**解析:**解（I）计算 A的特征多项式<equation>|\lambda E - A|</equation>.<equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda & 1 & - 1 \\ - 2 & \lambda + 3 & 0 \\ 0 & 0 & \lambda \end{array} \right| \xlongequal {\text {按 第三 行 展开}} \lambda \left(\lambda^ {2} + 3 \lambda + 2\right) = \lambda (\lambda + 1) (\lambda + 2).</equation>因此，A有3个不同的特征值：-2，-1，0.

由于属于不同特征值的特征向量线性无关，故A有3个线性无关的特征向量，A相似于对角矩阵<equation>\left( \begin{array}{c c c} - 2 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>分别计算 A的属于特征值-2，-1，0的特征向量.

当<equation>\lambda=-2</equation>时，解<equation>(-2 E-A) x=0</equation>.由于<equation>- 2 E - A = \left( \begin{array}{c c c} - 2 & 1 & - 1 \\ - 2 & 1 & 0 \\ 0 & 0 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} - 2 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right),</equation>故可取<equation>( 1, 2, 0 )^{\mathrm{T}}</equation>为 A的属于特征值-2的一个特征向量.

当<equation>\lambda=-1</equation>时，解<equation>(-E-A)x=0.</equation>由于<equation>- E - A = \left( \begin{array}{c c c} - 1 & 1 & - 1 \\ - 2 & 2 & 0 \\ 0 & 0 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right),</equation>故可取<equation>(1,1,0)^{\mathrm{T}}</equation>为<equation>A</equation>的属于特征值-1的一个特征向量.

当<equation>\lambda=0</equation>时，解（0E-A）x=0.由于<equation>0 E - A = \left( \begin{array}{c c c} 0 & 1 & - 1 \\ - 2 & 3 & 0 \\ 0 & 0 & 0 \end{array} \right),</equation>故可取（3，2，2）<equation>^{\mathrm{T}}</equation>为 A的属于特征值0的一个特征向量.

令<equation>P = \left( \begin{array}{c c c} 1 & 1 & 3 \\ 2 & 1 & 2 \\ 0 & 0 & 2 \end{array} \right)</equation>，则<equation>P^{-1}AP = \left( \begin{array}{c c c} - 2 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>.

计算<equation>P^{-1}</equation>得，<equation>P^{-1} = \left( \begin{array}{c c c} - 1 & 1 & \frac{1}{2} \\ 2 & - 1 & - 2 \\ 0 & 0 & \frac{1}{2} \end{array} \right).</equation><equation>\begin{aligned} \boldsymbol {A} ^ {9 9} &= \boldsymbol {P} \left( \begin{array}{c c c} (- 2) ^ {9 9} & 0 & 0 \\ 0 & (- 1) ^ {9 9} & 0 \\ 0 & 0 & 0  \right) \boldsymbol {P} ^ {- 1} &= \left( \begin{array}{c c c} 1 & 1 & 3 \\ 2 & 1 & 2 \\ 0 & 0 & 2  \right) \left( \begin{array}{c c c} - 2 ^ {9 9} & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0  \right) \left( \begin{array}{c c c} - 1 & 1 & \frac {1}{2} \\ 2 & - 1 & - 2 \\ 0 & 0 & \frac {1}{2}  \right) \\ &= \left( \begin{array}{c c c} 2 ^ {9 9} - 2 & 1 - 2 ^ {9 9} & 2 - 2 ^ {9 8} \\ 2 ^ {1 0 0} - 2 & 1 - 2 ^ {1 0 0} & 2 - 2 ^ {9 9} \\ 0 & 0 & 0  \right). \end{aligned}</equation>（Ⅱ）先求<equation>B^{100}.</equation>由于<equation>B^{2}=B A</equation>，故<equation>\boldsymbol {B} ^ {3} = \boldsymbol {B} \left(\boldsymbol {B} ^ {2}\right) = \boldsymbol {B} (\boldsymbol {B A}) = \boldsymbol {B} ^ {2} \boldsymbol {A} = (\boldsymbol {B A}) \boldsymbol {A} = \boldsymbol {B A} ^ {2}.</equation>下面我们用数学归纳法证明<equation>B^{n}=B A^{n-1}, n=2, 3, \dots</equation>当<equation>n = 2</equation>时，<equation>B^{2} = BA</equation>假设该命题对 n = k 成立，下面证明该命题对 n = k +1 也成立.<equation>\boldsymbol {B} ^ {n} = \boldsymbol {B} ^ {k + 1} = \boldsymbol {B} \boldsymbol {B} ^ {k} \xlongequal {\text {归 纳 假 设}} \boldsymbol {B} \left(\boldsymbol {B} \boldsymbol {A} ^ {k - 1}\right) = \boldsymbol {B} ^ {2} \boldsymbol {A} ^ {k - 1} = (\boldsymbol {B} \boldsymbol {A}) \boldsymbol {A} ^ {k - 1} = \boldsymbol {B} \boldsymbol {A} ^ {k} = \boldsymbol {B} \boldsymbol {A} ^ {n - 1}.</equation>于是，该命题对 n=k+1也成立，从而由数学归纳法可知，该命题对所有大于等于2的正整数均成立.

因此，<equation>\left(\boldsymbol {\beta} _ {1}, \boldsymbol {\beta} _ {2}, \boldsymbol {\beta} _ {3}\right) = \boldsymbol {B} ^ {1 0 0} = \boldsymbol {B A} ^ {9 9} = \left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\alpha} _ {2}, \boldsymbol {\alpha} _ {3}\right) \left( \begin{array}{c c c} 2 ^ {9 9} - 2 & 1 - 2 ^ {9 9} & 2 - 2 ^ {9 8} \\ 2 ^ {1 0 0} - 2 & 1 - 2 ^ {1 0 0} & 2 - 2 ^ {9 9} \\ 0 & 0 & 0 \end{array} \right).</equation>综上所述，<equation>\boldsymbol {\beta} _ {1} = \left(2 ^ {9 9} - 2\right) \boldsymbol {\alpha} _ {1} + \left(2 ^ {1 0 0} - 2\right) \boldsymbol {\alpha} _ {2},</equation><equation>\boldsymbol {\beta} _ {2} = \left(1 - 2 ^ {9 9}\right) \boldsymbol {\alpha} _ {1} + \left(1 - 2 ^ {1 0 0}\right) \boldsymbol {\alpha} _ {2},</equation><equation>\boldsymbol {\beta} _ {3} = \left(2 - 2 ^ {9 8}\right) \boldsymbol {\alpha} _ {1} + \left(2 - 2 ^ {9 9}\right) \boldsymbol {\alpha} _ {2}.</equation>

---

**2015年第21题 | 解答题 | 11分**

21. (本题满分11分)

设矩阵<equation>A = \left( \begin{array}{c c c} 0 & 2 & -3 \\ -1 & 3 & -3 \\ 1 & -2 & a \end{array} \right)</equation>相似于矩阵<equation>B = \left( \begin{array}{c c c} 1 & -2 & 0 \\ 0 & b & 0 \\ 0 & 3 & 1 \end{array} \right).</equation>I. 求 a,b的值；

II. 求可逆矩阵<equation>P</equation>，使<equation>P^{-1}AP</equation>为对角矩阵.

**答案:**(21) （I）<equation>a=4,b=5;</equation><equation>(\mathrm {I I}) \boldsymbol {P} = \left( \begin{array}{c c c} - 1 & 2 & - 3 \\ - 1 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right), \boldsymbol {P} ^ {- 1} \boldsymbol {A} \boldsymbol {P} = \left( \begin{array}{c c c} 5 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>

**解析:**解（I）由于A,B相似，故存在可逆矩阵Q使得<equation>Q^{-1} A Q=B</equation>，从而<equation>|B|=|Q^{-1}|\cdot|A|\cdot|Q|=|A|.</equation>计算得<equation>|A|=2 a-3,|B|=b.</equation>另一方面，A与B相似，故它们具有相同的迹，从而<equation>3+a=2+b.</equation>联立得<equation>\left\{\begin{array}{l l}a+3=b+2,\\2 a-3=b,\end{array}\right.</equation>解得<equation>\left\{\begin{array}{l l}a=4,\\b=5.\end{array}\right.</equation>（Ⅱ）由题设和第（Ⅰ）问得，<equation>| \lambda E - B | = \left| \begin{array}{c c c} \lambda - 1 & 2 & 0 \\ 0 & \lambda - 5 & 0 \\ 0 & - 3 & \lambda - 1 \end{array} \right| = (\lambda - 1) ^ {2} (\lambda - 5).</equation>从而<equation>B</equation>的特征值为1，1，5.由于<equation>A</equation>和<equation>B</equation>相似，故<equation>A</equation>的特征值也为1，1，5.

由第（I）问可得，<equation>A = \left( \begin{array}{c c c} 0 & 2 & -3 \\ -1 & 3 & -3 \\ 1 & -2 & 4 \end{array} \right).</equation>考虑<equation>A</equation>的属于特征值5的特征向量.<equation>\begin{array}{l} 5 E - A = \left( \begin{array}{c c c} 5 & - 2 & 3 \\ 1 & 2 & 3 \\ - 1 & 2 & 1 \end{array} \right) \xrightarrow {r _ {2} - r _ {3}} \frac {r _ {2} ^ {*} \times \frac {1}{2}}{r _ {2} ^ {*}} \left( \begin{array}{c c c} 5 & - 2 & 3 \\ 1 & 0 & 1 \\ - 1 & 2 & 1 \end{array} \right) \xrightarrow {r _ {3} + r _ {2} ^ {* *}} \frac {r _ {3} ^ {*} \times \frac {1}{2}}{r _ {3} ^ {*}} \left( \begin{array}{c c c} 5 & - 2 & 3 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} - 5 r _ {2} ^ {* *} + 2 r _ {3} ^ {* *}} \left( \begin{array}{c c c} 0 & 0 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right). \quad \text {关 注 公 众 号： 小 小 考 研} \quad \text {获 取 更 多 考 研 资 料} \\ \end{array}</equation>于是，<equation>r ( 5 E - A ) = 2</equation>，求得<equation>\xi_{1}=(-1,-1,1)^{\mathrm{T}}</equation>为<equation>( 5 E - A ) x = 0</equation>的一个基础解系.<equation>(-1,-1,1)^{\mathrm{T}}</equation>为A的属于特征值5的一个特征向量.

考虑<equation>A</equation>的属于特征值1的特征向量.<equation>\boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} 1 & - 2 & 3 \\ 1 & - 2 & 3 \\ - 1 & 2 & - 3 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & - 2 & 3 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>于是，<equation>r ( E - A ) = 1</equation>，求得<equation>\boldsymbol{\xi}_{2} = ( 2,1,0 )^{\mathrm{T}}</equation>和<equation>\boldsymbol{\xi}_{3} = (-3,0,1)^{\mathrm{T}}</equation>为<equation>( E - A ) x = 0</equation>的一个基础解系<equation>( 2,1,0 )^{\mathrm{T}}</equation>和<equation>(-3,0,1)^{\mathrm{T}}</equation>为A的属于特征值1的两个线性无关的特征向量.

取<equation>P = \left( \begin{array}{c c c} - 1 & 2 & - 3 \\ - 1 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right)</equation>，则<equation>P^{-1}AP = \left( \begin{array}{c c c} 5 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>.

---

**2014年第21题 | 解答题 | 11分**

21. (本题满分11分)

证明 n阶矩阵

相似.

**答案:**## (21) 证明略.

**解析:**证（法一）记<equation>A=\left( \begin{array}{c c c c} 1 & 1 & \dots & 1 \\ 1 & 1 & \dots & 1 \\ \vdots & \vdots & & \vdots \\ 1 & 1 & \dots & 1 \end{array} \right), B=\left( \begin{array}{c c c c} 0 & \dots & 0 & 1 \\ 0 & \dots & 0 & 2 \\ \vdots & & \vdots & \vdots \\ 0 & \dots & 0 & n \end{array} \right).</equation>由观察可知，<equation>r ( \mathbf{A} )=1</equation>，<equation>\operatorname{t r} ( \mathbf{A} )=n</equation>.又由于 A为实对称矩阵，故必相似于对角矩阵.由相似的矩阵具有相同的秩和迹可知， A相似于秩为1，迹为 n的对角矩阵，不妨记为<equation>\left( \begin{array}{c c c c} n & & & \\ & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right).</equation>另一方面，计算<equation>B</equation>的特征多项式得，<equation>| \lambda E - B | = \left| \begin{array}{c c c c} \lambda & 0 & \dots & - 1 \\ 0 & \lambda & & - 2 \\ \vdots & & \ddots & \vdots \\ 0 & \dots & 0 & \lambda - n \end{array} \right| = \lambda^ {n - 1} (\lambda - n).</equation>B的特征值为<equation>n,0,\dots ,0</equation>，其中0为<equation>n - 1</equation>重特征值.

由于<equation>0 E-B=\left( \begin{array}{c c c c} 0 & & -1 \\ 0 & & -2 \\ & \ddots & \vdots \\ & & -n \end{array} \right)</equation>，故<equation>r(0 E-B)=1. ( 0 E-B ) x=0</equation>有 n-1个线性无关的解.

B有 n-1个属于特征值0的线性无关的特征向量，再加上B的属于n的特征向量，B共有n个线性无关的特征向量.从而B也相似于<equation>\left( \begin{array}{c c c c} n & & \\ 0 & & \\ & \ddots & \\ & & 0 \end{array} \right).</equation>因此，存在可逆矩阵 P,Q，使得<equation>P^{-1} A P=Q^{-1} B Q=\left( \begin{array}{c c c c} n & & \\ 0 & & \\ & \ddots & \\ & & 0 \end{array} \right).</equation>于是<equation>Q P^{-1} A P Q^{-1}=B.</equation>令<equation>U=P Q^{-1}</equation>，则<equation>B=U^{-1} A U</equation>即A和B相似.

（法二）计算 A的特征多项式.<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c c c} \lambda - 1 & - 1 & \dots & \dots & - 1 \\ - 1 & \lambda - 1 & - 1 & \dots & - 1 \\ \vdots & \ddots & \ddots & \ddots & \vdots \\ \vdots & \ddots & \ddots & \ddots & - 1 \\ - 1 & \dots & \dots & - 1 & \lambda - 1  \right| \frac {c _ {1} + \left(c _ {2} + c _ {3} + \dots + c _ {n}\right)}{\hbar} \left| \begin{array}{c c c c c} \lambda - n & - 1 & \dots & \dots & - 1 \\ \lambda - n & \lambda - 1 & - 1 & \dots & - 1 \\ \lambda - n & \ddots & \ddots & \ddots & \vdots \\ \vdots & \ddots & \ddots & \ddots & - 1 \\ \lambda - n & - 1 & \dots & - 1 & \lambda - 1  \right| \\ &= (\lambda - n) \left| \begin{array}{c c c c c} 1 & - 1 & \dots & \dots & - 1 \\ 1 & \lambda - 1 & - 1 & \dots & - 1 \\ 1 & \ddots & \ddots & \ddots & \vdots \\ \vdots & \ddots & \ddots & \ddots & - 1 \\ 1 & - 1 & \dots & - 1 & \lambda - 1  \right| \frac {c _ {i} + c _ {1}}{i = 2 , \dots , n} (\lambda - n) \left| \begin{array}{c c c c c} 1 & 0 & \dots & \dots & 0 \\ 1 & \lambda & 0 & \dots & 0 \\ 1 & \ddots & \ddots & \ddots & \vdots \\ \vdots & \ddots & \ddots & \ddots & 0 \\ 1 & 0 & \dots & 0 & \lambda  \right| \\ &= \lambda^ {n - 1} (\lambda - n). \end{aligned}</equation>由于 A为实对称矩阵，故由 A的特征多项式为<equation>\lambda^{n-1} (\lambda-n)</equation>可知 A相似于对角矩阵<equation>\left( \begin{array}{c c c c} n & & & \\ & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right).</equation>其余同法一.

---

**2013年第6题 | 选择题 | 4分 | 答案: B**

6. 矩阵

相似的充分必要条件为（    ）

A. a=0,b=2 B. a=0,b为任意常数 C. a=2,b=0 D. a=2,b为任意常数

答案: B

**解析:**解 矩阵<equation>\left( \begin{array}{lll}1&a&1\\ a&b&a\\ 1&a&1 \end{array} \right)</equation>与<equation>\left( \begin{array}{lll}2&0&0\\ 0&b&0\\ 0&0&0 \end{array} \right)</equation>均为实对称矩阵，故它们相似等价于它们有相同的特征多项式.

矩阵<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>的特征多项式为<equation>f (\lambda)=\lambda(\lambda-2)(\lambda-b).</equation>考虑矩阵<equation>A = \left( \begin{array}{c c c} 1 & a & 1 \\ a & b & a \\ 1 & a & 1 \end{array} \right)</equation>的特征多项式<equation>g(\lambda)</equation>.<equation>g (\lambda) = | \lambda E - A | = \left| \begin{array}{c c c} \lambda - 1 & - a & - 1 \\ - a & \lambda - b & - a \\ - 1 & - a & \lambda - 1 \end{array} \right| = \lambda \left[ (\lambda - 2) (\lambda - b) - 2 a ^ {2} \right].</equation>由于<equation>f(\lambda)-g(\lambda)=2 a^{2} \lambda</equation>，故<equation>f(\lambda)=g(\lambda)</equation>当且仅当 a=0.由于上述论证不涉及到b，故b取任意常数均不影响结果.应选B.

---

**2010年第6题 | 选择题 | 4分 | 答案: D**

6. 设 A为4阶实对称矩阵，且<equation>A^{2}+A=O</equation>. 若 A的秩为3，则 A相似于（    ）

A.<equation>\left( \begin{array}{c c c c} 1 & & \\ & 1 & \\ & & 1 \\ & & 0 \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c c} 1 & & \\ & 1 & \\ & & - 1 \\ & & 0 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c c} 1 & & \\ & - 1 & \\ & & - 1 \\ & & 0 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c c} - 1 & & \\ & - 1 & \\ & & - 1 \\ & & 0 \end{array} \right)</equation>

答案: D

**解析:**解（法一）不妨设<equation>\lambda</equation>为 A的特征值，<equation>\alpha</equation>为其对应的特征向量.由<equation>A^{2}+A=O</equation>得，<equation>(A^{2}+A)\alpha=0.</equation>代入<equation>A\alpha=\lambda\alpha</equation>得，<equation>(\lambda^{2}+\lambda)\alpha=0.</equation>又由于<equation>\alpha</equation>非零，故<equation>\lambda^{2}+\lambda=0, \lambda=0</equation>或<equation>\lambda=-1.</equation>由于 A为实对称矩阵，故 A相似于对角矩阵.又因为<equation>r ( A )=3</equation>，所以对角矩阵的秩也为3，<equation>\lambda=-1</equation>是 A的三重特征值，A相似于<equation>\left( \begin{array}{c c c c} - 1 & & & \\ & - 1 & & \\ & & - 1 & \\ & & & 0 \end{array} \right)</equation>.应选D.

（法二）由于 A为实对称矩阵，故存在可逆矩阵 P使得<equation>P^{-1} A P=\left( \begin{array}{c c c c} \lambda_{1} & & & \\ & \lambda_{2} & & \\ & & \lambda_{3} & \\ & & & \lambda_{4} \end{array} \right).</equation>从而<equation>\begin{aligned} \boldsymbol {O} &= \boldsymbol {A} ^ {2} + \boldsymbol {A} = \boldsymbol {P} \left( \begin{array}{c c c c} \lambda_ {1} ^ {2} & & & \\ & \lambda_ {2} ^ {2} & & \\ & & \lambda_ {3} ^ {2} & \\ & & & \lambda_ {4} ^ {2}  \right) \boldsymbol {P} ^ {- 1} + \boldsymbol {P} \left( \begin{array}{c c c c} \lambda_ {1} & & & \\ & \lambda_ {2} & & \\ & & \lambda_ {3} & \\ & & & \lambda_ {4}  \right) \boldsymbol {P} ^ {- 1} \\ &= \boldsymbol {P} \left( \begin{array}{c c c c} \lambda_ {1} ^ {2} + \lambda_ {1} & & & \\ & \lambda_ {2} ^ {2} + \lambda_ {2} & & \\ & & \lambda_ {3} ^ {2} + \lambda_ {3} & \\ & & & \lambda_ {4} ^ {2} + \lambda_ {4}  \right) \boldsymbol {P} ^ {- 1}. \end{aligned}</equation>因此<equation>\lambda_{i}^{2}+\lambda_{i}=0 ( i=1,2,3,4).</equation>解得<equation>\lambda_{i}=0</equation>或<equation>\lambda_{i}=-1 ( i=1,2,3,4).</equation>又由于 r（A）=3，故A相似于<equation>\left( \begin{array}{c c c c} - 1 & & & \\ & - 1 & & \\ & & - 1 & \\ & & & 0 \end{array} \right).</equation>应选D.

---

**2009年第13题 | 填空题 | 4分**

13. 设<equation>\alpha=(1,1,1)^{\mathrm{T}}</equation><equation>\beta=(1,0,k)^{\mathrm{T}}</equation>，若矩阵<equation>\alpha\beta^{\mathrm{T}}</equation>相似于<equation>\left( \begin{array}{c c c} {3} & {0} & {0} \\ {0} & {0} & {0} \\ {0} & {0} & {0} \end{array} \right)</equation>，则 k=___

**解析:**解（法一）计算得<equation>\boldsymbol{\alpha}\boldsymbol{\beta}^{\mathrm{T}}=\left( \begin{array}{c c c} 1 & 0 & k \\ 1 & 0 & k \\ 1 & 0 & k \end{array} \right).</equation>由于相似矩阵的迹相等，即其主对角线上元素之和相等，故<equation>1+0+k=3+0+0.</equation>因此，<equation>k = 2</equation>（法二）由于相似矩阵的特征值相等，故3是<equation>\alpha \beta^{\mathrm{T}} = \left( \begin{array}{c c c} 1 & 0 & k \\ 1 & 0 & k \\ 1 & 0 & k \end{array} \right)</equation>的特征值. 从而，<equation>\left| 3 E - \alpha \beta^ {\mathrm {T}} \right| = \left| \begin{array}{c c c} 2 & 0 & - k \\ - 1 & 3 & - k \\ - 1 & 0 & 3 - k \end{array} \right| = 3 \left| \begin{array}{c c} 2 & - k \\ - 1 & 3 - k \end{array} \right| = 3 (6 - 3 k) = 0.</equation>因此，<equation>k = 2</equation>（法三）计算<equation>\alpha\beta^{\mathrm{T}}</equation>的特征值.<equation>| \lambda E - \alpha \boldsymbol {\beta} ^ {\mathrm {T}} | = \left| \begin{array}{c c c} \lambda - 1 & 0 & - k \\ - 1 & \lambda & - k \\ - 1 & 0 & \lambda - k \end{array} \right| = \lambda \left| \begin{array}{c c} \lambda - 1 & - k \\ - 1 & \lambda - k \end{array} \right| = \lambda^ {2} [ \lambda - (k + 1) ].</equation>特征值为0,0,k+1.又由相似矩阵的特征值相等可知<equation>k + 1 = 3</equation>.因此，<equation>k = 2.</equation>

---


#### 特征值与特征向量

**2024年第15题 | 填空题 | 5分**

15. 设 A为3阶矩阵，<equation>A^{*}</equation>为的 A伴随矩阵，E为3阶单位矩阵，若<equation>r(2 E-A)=1,r(E+A)=2</equation>，则<equation>|A^{*}|=</equation>___

**答案:**## 16

**解析:**解 由于<equation>r ( 2 E-A )=1</equation>，故由系数矩阵的秩与解集的秩的关系可知，方程组<equation>( 2 E-A ) x=0</equation>有3-1=2个线性无关的解，从而矩阵A有两个线性无关的属于特征值2的特征向量.

同理，由于<equation>r ( E+A) = 2</equation>即<equation>r (-E-A)=2</equation>故由系数矩阵的秩与解集的秩的关系可知，方程组<equation>(-E-A) x=0</equation>有3-2=1个线性无关的解，从而矩阵A有一个线性无关的属于特征值-1的特征向量.

由于属于不同特征值的特征向量线性无关，故矩阵<equation>A</equation>至少有三个线性无关的特征向量.结合<equation>A</equation>是3阶矩阵可得，<equation>A</equation>共有三个线性无关的特征向量，从而<equation>A</equation>相似于对角矩阵<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & - 1 \end{array} \right)</equation><equation>A</equation>的特征值为2，2，-1，<equation>|A|=-4.</equation>由<equation>AA^{*} = |A|E</equation>可得，<equation>|AA^{*}| = |A| |A^{*}| = |A|^{3}</equation>，故<equation>|A^{*}| = |A|^{2} = 16.</equation>或者，由伴随矩阵与矩阵的特征值的关系可知，<equation>A^{*}</equation>的特征值为<equation>\frac{|A|}{2},\frac{|A|}{2},\frac{|A|}{-1}</equation>即-2，-2，

4. 因此，<equation>|A^{*}| = (-2)\times(-2)\times 4 = 16.</equation>

---

**2020年第6题 | 选择题 | 4分 | 答案: D**

6. 设 A为3阶矩阵，<equation>\alpha_{1},\alpha_{2}</equation>为 A的属于特征值1的线性无关的特征向量，<equation>\alpha_{3}</equation>为 A的属于特征值-1的特征向量，则满足<equation>P^{-1}AP=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>的可逆矩阵 P为（    ）

A.<equation>\left( \alpha_{1}+\alpha_{3},\alpha_{2},-\alpha_{3} \right)</equation>B.<equation>\left( \alpha_{1}+\alpha_{2},\alpha_{2},-\alpha_{3} \right)</equation>C.<equation>\left( \alpha_{1}+\alpha_{3},-\alpha_{3},\alpha_{2} \right)</equation>D.<equation>\left( \alpha_{1}+\alpha_{2},-\alpha_{3},\alpha_{2} \right)</equation>

答案: D

**解析:**解 由于<equation>P^{-1} A P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，故 P的列向量应分别为属于特征值1，-1，1的特征向量，且

第1列与第3列为属于特征值1的线性无关的特征向量.

由已知条件，<equation>\alpha_{3}</equation>为 A的属于特征值-1的特征向量，故 P的第2列可取为<equation>k\alpha_{3}</equation>其中 k为任意非零常数.

由于<equation>\alpha_{1},\alpha_{2}</equation>为 A的属于特征值1的线性无关的特征向量，且<equation>\left(\alpha_{1}+\alpha_{2},\alpha_{2}\right)=\left(\alpha_{1},\alpha_{2}\right)\left( \begin{array}{cc}1&0\\ 1&1 \end{array} \right)</equation>故<equation>\alpha_{1}+\alpha_{2}</equation>也为 A的属于特征值1的特征向量，且与<equation>\alpha_{2}</equation>线性无关.

因此，<equation>P</equation>可取为<equation>\left(\alpha_{1}+\alpha_{2},-\alpha_{3},\alpha_{2}\right).</equation>应选D.

---

**2018年第13题 | 填空题 | 4分**

13. 设 A为3阶矩阵，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>是线性无关的向量组. 若<equation>A\alpha_{1}=\alpha_{1}+\alpha_{2},A\alpha_{2}=\alpha_{2}+\alpha_{3},A\alpha_{3}=\alpha_{1}+\alpha_{3}</equation>，则<equation>|A|=</equation>

**解析:**解记<equation>P=(\alpha_{1},\alpha_{2},\alpha_{3})</equation>.由于<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关，故P可逆由题设可知，<equation>A P = A \left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) = \left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) \left( \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{array} \right) = P \left( \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{array} \right).</equation>记<equation>B=\left( \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{array} \right).</equation>.于是，<equation>A=P B P^{-1}.</equation>因此，<equation>| A | = | P | \cdot | B | \cdot | P ^ {- 1} | = | B | = \left| \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{array} \right| = 2.</equation>

---

**2015年第13题 | 填空题 | 4分**

13. 设 3 阶矩阵<equation>\boldsymbol{A}</equation>的特征值为 2,-2,1,<equation>\boldsymbol{B}=\boldsymbol{A}^{2}-\boldsymbol{A}+\boldsymbol{E}</equation>,其中<equation>\boldsymbol{E}</equation>为 3 阶单位矩阵,则行列式<equation>|\boldsymbol{B}|=</equation>___.

**解析:**解（法一）由于 A有3个不同的特征值，故 A有3个线性无关的特征向量，从而存在可逆矩阵 P使得<equation>P^{-1} A P=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>.于是<equation>\boldsymbol {A} = \boldsymbol {P} \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & - 2 & 0 \\ 0 & 0 & 1 \end{array} \right) \boldsymbol {P} ^ {- 1}, \quad \boldsymbol {A} ^ {2} = \boldsymbol {P} \left( \begin{array}{c c c} 2 ^ {2} & 0 & 0 \\ 0 & (- 2) ^ {2} & 0 \\ 0 & 0 & 1 ^ {2} \end{array} \right) \boldsymbol {P} ^ {- 1},</equation><equation>\boldsymbol {B} = \boldsymbol {P} \left( \begin{array}{c c c} 2 ^ {2} - 2 + 1 & 0 & 0 \\ 0 & (- 2) ^ {2} - (- 2) + 1 & 0 \\ 0 & 0 & 1 ^ {2} - 1 + 1 \end{array} \right) \boldsymbol {P} ^ {- 1} = \boldsymbol {P} \left( \begin{array}{c c c} 3 & 0 & 0 \\ 0 & 7 & 0 \\ 0 & 0 & 1 \end{array} \right) \boldsymbol {P} ^ {- 1}.</equation>因此，<equation>|\boldsymbol{B}| = 21\cdot |\boldsymbol{P}| \cdot |\boldsymbol{P}^{-1}| = 21.</equation>（法二）设<equation>\alpha</equation>为矩阵<equation>A</equation>的属于特征值<equation>\lambda</equation>的特征向量，即<equation>A\alpha = \lambda \alpha</equation>，则<equation>\boldsymbol {B} \alpha = \left(\boldsymbol {A} ^ {2} - \boldsymbol {A} + \boldsymbol {E}\right) \alpha = \left(\lambda^ {2} - \lambda + 1\right) \alpha .</equation>由上可见，若<equation>\alpha</equation>为<equation>A</equation>的属于特征值<equation>\lambda</equation>的特征向量，则<equation>\alpha</equation>为<equation>B</equation>的属于特征值<equation>\lambda^2 - \lambda +1</equation>的特征向量.<equation>A</equation>的3个线性无关的特征向量也是<equation>B</equation>的3个线性无关的特征向量，对应的特征值为<equation>\lambda^2 - \lambda +1</equation>（<equation>\lambda = 2,-2,1</equation>）.由此可求得<equation>B</equation>的特征值为3,7,1.

因此，<equation>|B| = 3\times 7\times 1 = 21.</equation>

---

**2011年第21题 | 解答题 | 11分**


设<equation>A</equation>为3阶实对称矩阵，<equation>A</equation>的秩为2，且<equation>1 \left( \begin{array}{c c} 1 & 1 \\ 0 & 0 \\ - 1 & 1 \end{array} \right) = \left( \begin{array}{c c} - 1 & 1 \\ 0 & 0 \\ 1 & 1 \end{array} \right)</equation>I. 求 A的所有特征值与特征向量；

II. 求矩阵 A.

**答案:**(21) （I）特征值-1，1，0，分别对应特征向量<equation>k_{1}(1,0,-1)^{\mathrm{T}}, k_{2}(1,0,1)^{\mathrm{T}}, k_{3}(0,1,0)^{\mathrm{T}}</equation>，其中<equation>k_{1}, k_{2},</equation><equation>k_{3}</equation>为任意非零常数；（Ⅱ）<equation>\left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{array} \right).</equation>

**解析:**解（I）由于<equation>A\left( \begin{array}{c c} 1 & 1 \\ 0 & 0 \\ - 1 & 1 \end{array} \right)=\left( \begin{array}{c c} - 1 & 1 \\ 0 & 0 \\ 1 & 1 \end{array} \right)</equation>，故<equation>\alpha_{1}=(1,0,-1)^{\mathrm{T}}</equation>，<equation>\alpha_{2}=(1,0,1)^{\mathrm{T}}</equation>满足<equation>A\alpha_{1}=</equation><equation>-\alpha_{1},A\alpha_{2}=\alpha_{2}</equation>，从而<equation>\alpha_{1}</equation>为A的属于特征值-1的一个特征向量，<equation>\alpha_{2}</equation>为A的属于特征值1的一个特征向量.

又因为<equation>r(\mathbf{A}) = 2</equation>，<equation>|\mathbf{A}| = 0</equation>，所以<equation>\mathbf{A}</equation>还有一个特征值为零.

因为实对称矩阵属于不同特征值的特征向量相互正交，所以 A的属于特征值0的特征向量<equation>\boldsymbol{\alpha}_{3}=(x_{1},x_{2},x_{3})^{\mathrm{T}}</equation>满足<equation>\boldsymbol{\alpha}_{1}^{\mathrm{T}}\boldsymbol{\alpha}_{3}=0</equation><equation>\boldsymbol{\alpha}_{2}^{\mathrm{T}}\boldsymbol{\alpha}_{3}=0</equation>从而得<equation>\left\{ \begin{array}{l l} x_{1}-x_{3}=0, \\ x_{1}+x_{3}=0. \end{array} \right.</equation>由此可得<equation>\boldsymbol{\alpha}_{3}=k_{3}(0,1,0)^{\mathrm{T}}</equation>其中<equation>k_{3}</equation>为任意非零常数.

因此，<equation>\mathbf{A}</equation>的特征值为-1,1,0.对应的特征向量分别为<equation>k_{1}(1,0,-1)^{\mathrm{T}}</equation><equation>k_{2}(1,0,1)^{\mathrm{T}}</equation><equation>k_{3}(0,1,0)^{\mathrm{T}}</equation>其中<equation>k_{1},k_{2},k_{3}</equation>为任意非零常数.

（Ⅱ）（法一）由第（I）问可知，取<equation>P=\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)=\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \\ -1 & 1 & 0 \end{array} \right)</equation>，可得<equation>P^{-1}AP=</equation><equation>\left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>于是<equation>A=P\left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right) P^{-1}.</equation>利用初等变换法计算<equation>P^{-1}.</equation><equation>\begin{array}{l} (P, E) = \left( \begin{array}{c c c c c c} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 1 & 0 \\ - 1 & 1 & 0 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} + r _ {1}} \left( \begin{array}{c c c c c c} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 1 & 0 \\ 0 & 2 & 0 & 1 & 0 & 1 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {*} \times \frac {1}{2}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & \frac {1}{2} & 0 & - \frac {1}{2} \\ 0 & 0 & 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & \frac {1}{2} & 0 & \frac {1}{2} \end{array} \right) \xrightarrow {r _ {2} \leftrightarrow r _ {3} ^ {* *}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & \frac {1}{2} & 0 & - \frac {1}{2} \\ 0 & 1 & 0 & \frac {1}{2} & 0 & \frac {1}{2} \\ 0 & 0 & 1 & 0 & 1 & 0 \end{array} \right). \\ \end{array}</equation>于是，<equation>P^{-1} = \left( \begin{array}{c c c} \frac{1}{2} & 0 & -\frac{1}{2} \\ \frac{1}{2} & 0 & \frac{1}{2} \\ 0 & 1 & 0 \end{array} \right).</equation>因此，<equation>\begin{aligned} \boldsymbol {A} &= \boldsymbol {P} \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \boldsymbol {P} ^ {- 1} &= \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \\ - 1 & 1 & 0  \right) \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \left( \begin{array}{c c c} \frac {1}{2} & 0 & - \frac {1}{2} \\ \frac {1}{2} & 0 & \frac {1}{2} \\ 0 & 1 & 0  \right) \\ &= \left( \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & 0 & 0 \\ 1 & 1 & 0  \right) \left( \begin{array}{c c c} \frac {1}{2} & 0 & - \frac {1}{2} \\ \frac {1}{2} & 0 & \frac {1}{2} \\ 0 & 1 & 0  \right) &= \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0  \right). \end{aligned}</equation>或者，由<equation>A P = \left(A \alpha_ {1}, A \alpha_ {2}, A \alpha_ {3}\right) = \left(- \alpha_ {1}, \alpha_ {2}, 0\right)</equation>可得，<equation>\boldsymbol {A} = \left(- \alpha_ {1}, \alpha_ {2}, 0\right) \boldsymbol {P} ^ {- 1} = - \frac {1}{2} \left( \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & 0 & 0 \\ 1 & 1 & 0 \end{array} \right) \left( \begin{array}{c c c} - 1 & 0 & 1 \\ - 1 & 0 & - 1 \\ 0 & - 2 & 0 \end{array} \right) = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{array} \right).</equation>（法二）将<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>单位化，组成一正交矩阵<equation>Q = \left( \begin{array}{c c c} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0 \\ 0 & 0 & 1 \\ -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0 \end{array} \right)</equation>，则<equation>Q^{\mathrm{T}}AQ = \left( \begin{array}{c c c} -1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>.

因此，<equation>\begin{aligned} \boldsymbol {A} &= \boldsymbol {Q} \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \boldsymbol {Q} ^ {\mathrm {T}} &= \left( \begin{array}{c c c} \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {2}} & 0 \\ 0 & 0 & 1 \\ - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {2}} & 0  \right) \left( \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0  \right) \left( \begin{array}{c c c} \frac {1}{\sqrt {2}} & 0 & - \frac {1}{\sqrt {2}} \\ \frac {1}{\sqrt {2}} & 0 & \frac {1}{\sqrt {2}} \\ 0 & 1 & 0  \right) \\ &= \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0  \right). \end{aligned}</equation>

---

**2010年第21题 | 解答题 | 11分**

21. (本题满分11分)

设<equation>A=\left( \begin{array}{c c c} 0 & -1 & 4 \\ -1 & 3 & a \\ 4 & a & 0 \end{array} \right)</equation>，正交矩阵Q使<equation>Q^{\mathrm{T}}AQ</equation>为对角矩阵，若Q的第1列为<equation>\frac{1}{\sqrt{6}}(1,2,1)^{\mathrm{T}}</equation>，求a和Q.

**答案:**<equation>a = - 1, Q = \left( \begin{array}{c c c} \frac {1}{\sqrt {6}} & - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {3}} \\ \frac {2}{\sqrt {6}} & 0 & - \frac {1}{\sqrt {3}} \\ \frac {1}{\sqrt {6}} & \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {3}} \end{array} \right), Q ^ {\mathrm {T}} A Q = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & - 4 & 0 \\ 0 & 0 & 5 \end{array} \right).</equation>

**解析:**解 由题设知，<equation>\alpha_{1}=\frac{1}{\sqrt{6}}(1,2,1)^{\mathrm{T}}</equation>为 A的一个特征向量.不妨设<equation>\alpha_{1}</equation>对应的特征值为 k，则<equation>\begin{aligned} \boldsymbol {A} \boldsymbol {\alpha} _ {1} &= \frac {1}{\sqrt {6}} \left( \begin{array}{c c c} 0 & - 1 & 4 \\ - 1 & 3 & a \\ 4 & a & 0  \right) \left(  1 \\ 2 \\ 1  \right) &= \frac {1}{\sqrt {6}} \left( \begin{array}{c} 2 \\ 5 + a \\ 4 + 2 a  \right) &= \frac {k}{\sqrt {6}} \left(  1 \\ 2 \\ 1  \right). \end{aligned}</equation>从而<equation>\left\{ \begin{array}{l}2 = k,\\ 5 + a = 2k,\\ 4 + 2a = k, \end{array} \right.</equation>解得<equation>a = -1</equation>，<equation>k = 2.</equation>于是，<equation>A = \left( \begin{array}{c c c}0 & -1 & 4\\ -1 & 3 & -1\\ 4 & -1 & 0 \end{array} \right).</equation>计算 A的特征多项式得<equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda & 1 & - 4 \\ 1 & \lambda - 3 & 1 \\ - 4 & 1 & \lambda \end{array} \right| = (\lambda - 2) (\lambda - 5) (\lambda + 4).</equation>因此，<equation>A</equation>的特征值为2，5，-4.<equation>\alpha_{1}</equation>是<equation>A</equation>的属于特征值2的特征向量.

先求属于特征值-4的单位特征向量<equation>\alpha_{2}</equation>.由特征向量的定义可知，<equation>(-4E - A)x = 0.</equation><equation>\begin{array}{l} - 4 E - A = \left( \begin{array}{c c c} - 4 & 1 & - 4 \\ 1 & - 7 & 1 \\ - 4 & 1 & - 4 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c} - 4 & 1 & - 4 \\ 1 & - 7 & 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} + 4 r _ {2}} \left( \begin{array}{c c c} 0 & 1 & 0 \\ 1 & - 7 & 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} + 7 r _ {1} ^ {* *}} \binom {1} {r _ {1} ^ {* *} \leftrightarrow r _ {2} ^ {*}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>由此可得<equation>\left\{\begin{array}{l l}x_{1}+x_{3}=0,\\ x_{2}=0,\end{array}\right.</equation>故<equation>\boldsymbol{\xi}_{2}=(-1,0,1)^{\mathrm{T}}</equation>为该方程组的一个基础解系.将<equation>\boldsymbol{\xi}_{2}</equation>单位化得<equation>\boldsymbol{\alpha}_{2}=</equation><equation>\frac{1}{\sqrt{2}}(-1,0,1)^{\mathrm{T}}.</equation>同理，解（5E-A）<equation>x=0.</equation><equation>\begin{array}{l} 5 E - A = \left( \begin{array}{c c c} 5 & 1 & - 4 \\ 1 & 2 & 1 \\ - 4 & 1 & 5 \end{array} \right) \xrightarrow {r _ {3} + r _ {1} - r _ {2}} \left( \begin{array}{c c c} 5 & 1 & - 4 \\ 1 & 2 & 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} - 5 r _ {2}} \left( \begin{array}{c c c} 0 & 1 & 1 \\ 1 & 2 & 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} - r _ {1} ^ {* *}} \frac {1}{r _ {1} ^ {* *} \leftrightarrow r _ {2} ^ {*}} \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>由此可得<equation>\left\{\begin{array}{l l}x_{1}+x_{2}=0,\\ x_{2}+x_{3}=0,\end{array} \right.</equation>故<equation>\boldsymbol{\xi}_{3}=(1,-1,1)^{\mathrm{T}}</equation>为该方程组的一个基础解系.将<equation>\boldsymbol{\xi}_{3}</equation>单位化得<equation>\boldsymbol{\alpha}_{3}=</equation><equation>\frac{1}{\sqrt{3}}(1,-1,1)^{\mathrm{T}}.</equation>或者也可以如下求<equation>\boldsymbol{\alpha}_{3}.</equation>由于<equation>\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2}</equation>为属于不同特征值的特征向量，故它们相互正交.于是<equation>\boldsymbol {\alpha} _ {3} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {1} = 0, \quad \boldsymbol {\alpha} _ {3} ^ {\mathrm {T}} \boldsymbol {\alpha} _ {2} = 0.</equation><equation>\pmb{\alpha}_{3}</equation>的坐标<equation>(x_{1}, x_{2}, x_{3})^{\mathrm{T}}</equation>满足<equation>\left\{ \begin{array}{l} x_{1} + 2x_{2} + x_{3} = 0, \\ x_{1} - x_{3} = 0. \end{array} \right.</equation>因此可得<equation>\pmb{\xi}_{3} = (1, -1, 1)^{\mathrm{T}}</equation>为该方程组的一个基础解系.将<equation>\pmb{\xi}_{3}</equation>单位化得<equation>\pmb{\alpha}_{3} = \frac{1}{\sqrt{3}} (1, -1, 1)^{\mathrm{T}}.</equation>综上所述，<equation>a = -1</equation>，<equation>Q = \left( \begin{array}{c c c} \frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} \\ \frac{2}{\sqrt{6}} & 0 & -\frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{6}} & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} \end{array} \right)</equation>，<equation>Q^{\mathrm{T}}AQ = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -4 & 0 \\ 0 & 0 & 5 \end{array} \right)</equation>

---


### 二次型

**2025年第7题 | 选择题 | 5分 | 答案: B**

7. 设矩阵<equation>A=\left( \begin{array}{c c}1&2\\ -2&-a \end{array} \right), B=\left( \begin{array}{c c}1&0\\ 1&a \end{array} \right),</equation>若 f(x,y) =<equation>| x A+y B |</equation>是正定二次型，则 a的取值范围是（    )

A.<equation>( 0,2-\sqrt{3} )</equation>B.<equation>( 2-\sqrt{3},2+\sqrt{3} )</equation>C.<equation>( 2+\sqrt{3},4 )</equation>D.<equation>( 0,4 )</equation>

答案: B

**解析:**解 由于<equation>A=\left( \begin{array}{cc}1&2\\ -2&-a \end{array} \right), B=\left( \begin{array}{cc}1&0\\ 1&a \end{array} \right),</equation>故<equation>xA+yB=\left( \begin{array}{cc}x+y&2x\\ -2x+y&a(y-x) \end{array} \right).</equation>进一步可得<equation>\mid xA+yB\mid =\left| \begin{array}{cc}x+y&2x\\ -2x+y&a(y-x) \end{array} \right|=a\left(y^{2}-x^{2}\right)+4x^{2}-2xy=(4-a)x^{2}+ay^{2}-2xy.</equation>于是，二次型<equation>f(x,y)</equation>对应的对称矩阵<equation>C=\left( \begin{array}{cc}4-a&-1\\ -1&a \end{array} \right).</equation>由于<equation>f(x,y)</equation>是正定二次型，故C的各阶顺序主子式均为正数，即<equation>4-a>0, |C|=4a-a^{2}-1</equation>>0.联立<equation>\left\{ \begin{array}{l l}4-a>0,\\ a^{2}-4a+1<0, \end{array} \right.</equation>解<equation>a^{2}-4a+1<0</equation>可得<equation>2-\sqrt{3}<a<2+\sqrt{3},</equation>与a<4取交集可得a<equation>\in(2-\sqrt{3},2+\sqrt{3}).</equation>因此，应选B.

---

**2024年第5题 | 选择题 | 5分 | 答案: C**

5. 设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=\boldsymbol{x}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{x}</equation>在正交变换下可化成<equation>y_{1}^{2}-2 y_{2}^{2}+3 y_{3}^{2}</equation>，则二次型 f的矩阵 A的行列式与迹分别为（    ）

A. -6,-2 B. 6,-2 C. -6,2 D. 6,2

答案: C

**解析:**解 由于二次型<equation>f ( x_{1}, x_{2}, x_{3} )=x^{\mathrm{T}} A x</equation>在正交变换下可化为<equation>y_{1}^{2}-2 y_{2}^{2}+3 y_{3}^{2}</equation>故其对应的对称矩阵 A的特征值为1，-2，3，从而 A的行列式<equation>| A |=1 \times(-2) \times 3=-6</equation>，迹<equation>\operatorname{t r} ( A )=1-2+3=2.</equation>因此，应选C.

---

**2023年第6题 | 选择题 | 5分 | 答案: B**

6. 二次型<equation>f \left(x_{1}, x_{2}, x_{3}\right)=\left(x_{1}+x_{2}\right)^{2}+\left(x_{1}+x_{3}\right)^{2}-4\left(x_{2}-x_{3}\right)^{2}</equation>的规范形为（    )

A.<equation>y_{1}^{2}+y_{2}^{2}</equation>B.<equation>y_{1}^{2}-y_{2}^{2}</equation>C.<equation>y_{1}^{2}+y_{2}^{2}-4 y_{3}^{2}</equation>D.<equation>y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>

答案: B

**解析:**解 （法一）将<equation>f ( x_{1}, x_{2}, x_{3} )</equation>展开可得<equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = 2 x _ {1} ^ {2} - 3 x _ {2} ^ {2} - 3 x _ {3} ^ {2} + 2 x _ {1} x _ {2} + 2 x _ {1} x _ {3} + 8 x _ {2} x _ {3}.</equation>该二次型对应的矩阵为<equation>A=\left( \begin{array}{c c c} 2 & 1 & 1 \\ 1 & -3 & 4 \\ 1 & 4 & -3 \end{array} \right).</equation>计算可得<equation>| A | = \left| \begin{array}{c c c} 2 & 1 & 1 \\ 1 & - 3 & 4 \\ 1 & 4 & - 3 \end{array} \right| \xlongequal {r _ {2} + r _ {3}} \left| \begin{array}{c c c} 2 & 1 & 1 \\ 2 & 1 & 1 \\ 1 & 4 & - 3 \end{array} \right| = 0.</equation>由于<equation>| A|=0</equation>，故 A有零特征值，从而<equation>r(A)\leqslant 2</equation>，f的正、负惯性指数之和不超过2.

若 f的负惯性指数为0，则 f非负，即对任意<equation>\left(x_{1},x_{2},x_{3}\right)</equation>，均有<equation>f\left(x_{1},x_{2},x_{3}\right)\geqslant 0</equation>.但是，<equation>f(0,0,1)=0+1-4=-3<0</equation>，矛盾.同理，若 f的正惯性指数为0，则 f非正，即对任意<equation>\left(x_{1},x_{2},x_{3}\right)</equation>，均有<equation>f\left(x_{1},x_{2},x_{3}\right)\leqslant 0</equation>.但是，<equation>f(1,0,0)=1+1-0=2>0</equation>，矛盾.

由于 f的正、负惯性指数之和不超过2，而正、负惯性指数又均大于0，故其正、负惯性指数均为 1. 应选B.

（法二）记<equation>\left\{ \begin{array}{l l l} y_{1} = x_{1} + x_{2}, \\ y_{2} = x_{1} + x_{3}, \\ y_{3} = x_{2} - x_{3}, \end{array} \right.</equation><equation>P = \left( \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & -1 \end{array} \right)</equation>，则<equation>\left( \begin{array}{l} y_{1} \\ y_{2} \\ y_{3} \end{array} \right) = P \left( \begin{array}{l} x_{1} \\ x_{2} \\ x_{3} \end{array} \right)</equation>.

记<equation>\boldsymbol{\Lambda}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & - 4 \end{array} \right)</equation>，则由<equation>f \left( x_{1}, x_{2}, x_{3}\right) = \left(x_{1}+x_{2}\right)^{2}+\left(x_{1}+x_{3}\right)^{2}-4\left(x_{2}-x_{3}\right)^{2}</equation>可知，<equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = y ^ {\mathrm {T}} \Lambda y \xlongequal {y = P x} x ^ {\mathrm {T}} P ^ {\mathrm {T}} \Lambda P x.</equation>于是，<equation>A=P^{\mathrm{T}}\Lambda P</equation>为二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>对应的对称矩阵.

又因为<equation>| P | = \left| \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & - 1 \end{array} \right| = 0</equation>，所以<equation>| A | = 0</equation>，从而A有零特征值.

其余同法一.

（法三）令<equation>\left\{ \begin{array}{l l} y_{1}=x_{1}+x_{2}, \\ y_{2}=x_{1}+x_{3}, \\ y_{3}=x_{3}, \end{array} \right.</equation>则<equation>x_{2}-x_{3}=y_{1}-y_{2}</equation>，且该变换为可逆线性变换.在该变换下，二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>化为<equation>\begin{aligned} g \left(y _ {1}, y _ {2}, y _ {3}\right) &= y _ {1} ^ {2} + y _ {2} ^ {2} - 4 \left(y _ {1} - y _ {2}\right) ^ {2} = - 3 y _ {1} ^ {2} - 3 y _ {2} ^ {2} + 8 y _ {1} y _ {2} \\ &= - 3 y _ {1} ^ {2} + 3 \cdot \frac {8}{3} y _ {1} y _ {2} - 3 y _ {2} ^ {2} = - 3 \left(y _ {1} - \frac {4}{3} y _ {2}\right) ^ {2} - 3 y _ {2} ^ {2} + \frac {1 6}{3} y _ {2} ^ {2} \\ &= - 3 \left(y _ {1} - \frac {4}{3} y _ {2}\right) ^ {2} + \frac {7}{3} y _ {2} ^ {2}. \end{aligned}</equation>再令<equation>\left\{ \begin{array}{l l} z_{1}=y_{1}-\frac{4}{3} y_{2}, \\ z_{2}=y_{2}, \\ z_{3}=y_{3}, \end{array} \right.</equation>该变换为可逆线性变换.在该变换下，二次型<equation>g(y_{1},y_{2},y_{3})</equation>化为<equation>h \left(z _ {1}, z _ {2}, z _ {3}\right) = - 3 z _ {1} ^ {2} + \frac {7}{3} z _ {2} ^ {2}.</equation>因此，<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>的一个标准形为<equation>- 3 z_{1}^{2}+\frac{7}{3} z_{2}^{2}</equation>，其正、负惯性指数均为1.应选B.

---

**2022年第21题 | 解答题 | 12分**

（本题满分12分）

已知二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=3 x_{1}^{2}+4 x_{2}^{2}+3 x_{3}^{2}+2 x_{1} x_{3}</equation>.

I. 求正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>将<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>化为标准形；

II. 证明：<equation>\min_{x\neq0}\frac{f(x)}{x^{\mathrm{T}}x}=2.</equation>

**答案:**（I）<equation>Q=\left( \begin{array}{c c c} \frac{1}{\sqrt{2}} & 0 & -\frac{1}{\sqrt{2}} \\ 0 & 1 & 0 \\ \frac{1}{\sqrt{2}} & 0 & \frac{1}{\sqrt{2}} \end{array} \right)</equation>，正交变换<equation>x=Qy</equation>将二次型f化为标准形<equation>4y_{1}^{2}+4y_{2}^{2}+2y_{3}^{2};</equation>（Ⅱ）证明略.

**解析:**解（I）由 f的表达式可得 f对应的矩阵 A =<equation>\left( \begin{array}{c c c} 3 & 0 & 1 \\ 0 & 4 & 0 \\ 1 & 0 & 3 \end{array} \right).</equation>计算 A的特征多项式.<equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda - 3 & 0 & - 1 \\ 0 & \lambda - 4 & 0 \\ - 1 & 0 & \lambda - 3 \end{array} \right| = (\lambda - 4) \left[ (\lambda - 3) ^ {2} - 1 \right] = (\lambda - 4) ^ {2} (\lambda - 2).</equation>A的特征值为4,4,2.

分别计算 A的属于特征值4和2的特征向量.

考虑（4E-A）x=0.<equation>4 E - A = \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 0 & 0 \\ - 1 & 0 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation><equation>\xi_{1}=\left( \begin{array}{c}1\\ 0\\ 1 \end{array} \right)</equation>和<equation>\xi_{2}=\left( \begin{array}{c}0\\ 1\\ 0 \end{array} \right)</equation>为 A的属于特征值4的两个线性无关的特征向量.考虑<equation>( 2 E-A ) x=0</equation>考虑（2E-A）x=0.<equation>2 E - A = \left( \begin{array}{c c c} - 1 & 0 & - 1 \\ 0 & - 2 & 0 \\ - 1 & 0 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation><equation>\xi_{3}=\left( \begin{array}{c}-1\\ 0\\ 1 \end{array} \right)</equation>为 A的属于特征值2的一个特征向量.

由于<equation>\xi_{1},\xi_{2},\xi_{3}</equation>相互正交，故只需将它们各自单位化即可得一组相互正交的单位特征向量.<equation>\boldsymbol {\varepsilon} _ {1} = \frac {\boldsymbol {\xi} _ {1}}{\| \boldsymbol {\xi} _ {1} \|} = \frac {1}{\sqrt {2}} \binom {1} {1}, \quad \boldsymbol {\varepsilon} _ {2} = \frac {\boldsymbol {\xi} _ {2}}{\| \boldsymbol {\xi} _ {2} \|} = \binom {0} {1}, \quad \boldsymbol {\varepsilon} _ {3} = \frac {\boldsymbol {\xi} _ {3}}{\| \boldsymbol {\xi} _ {3} \|} = \frac {1}{\sqrt {2}} \binom {- 1} {0}</equation>令<equation>Q=(\varepsilon_{1},\varepsilon_{2},\varepsilon_{3})</equation>，可得<equation>Q^{-1}AQ=Q^{\mathrm{T}}AQ=\left( \begin{array}{c c c} 4 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>，即正交变换<equation>x=Qy</equation>将二次型f化为标准形<equation>4y_{1}^{2}+4y_{2}^{2}+2y_{3}^{2}.</equation>（Ⅱ）由第（Ⅰ）问可知，在正交变换<equation>x=Q y</equation>下，<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>的标准形为<equation>4 y_{1}^{2}+4 y_{2}^{2}+2 y_{3}^{2}.</equation>又因为<equation>\boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {x} = \left(Q \boldsymbol {y}\right) ^ {\mathrm {T}} Q \boldsymbol {y} = \boldsymbol {y} ^ {\mathrm {T}} Q ^ {\mathrm {T}} Q \boldsymbol {y} \xlongequal {Q ^ {\mathrm {T}} Q = E} \boldsymbol {y} ^ {\mathrm {T}} \boldsymbol {y} = y _ {1} ^ {2} + y _ {2} ^ {2} + y _ {3} ^ {2},</equation>所以对<equation>x\neq 0</equation><equation>\frac {f (\boldsymbol {x})}{\boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {x}} \xlongequal {\boldsymbol {x} = Q \boldsymbol {y}} \frac {4 y _ {1} ^ {2} + 4 y _ {2} ^ {2} + 2 y _ {3} ^ {2}}{y _ {1} ^ {2} + y _ {2} ^ {2} + y _ {3} ^ {2}} \geqslant \frac {2 y _ {1} ^ {2} + 2 y _ {2} ^ {2} + 2 y _ {3} ^ {2}}{y _ {1} ^ {2} + y _ {2} ^ {2} + y _ {3} ^ {2}} = 2.</equation>取<equation>y_{0}</equation>满足<equation>y_{1} = y_{2} = 0, y_{3} \neq 0, x_{0} = Qy_{0}</equation>，即<equation>x_{0} = y_{3}\varepsilon_{3}</equation>时，可得<equation>\frac{f\left(x_0\right)}{x_0^{\mathrm{T}}x_0} = 2.</equation>因此，<equation>\min_{x\neq0}\frac{f(x)}{x^{\mathrm{T}}x}=2.</equation>

---

**2021年第5题 | 选择题 | 5分 | 答案: B**

5. 二次型<equation>f \left(x_{1}, x_{2}, x_{3}\right)=\left(x_{1}+x_{2}\right)^{2}+\left(x_{2}+x_{3}\right)^{2}-\left(x_{3}-x_{1}\right)^{2}</equation>的正惯性指数与负惯性指数依次为（    )

A. 2,0 B. 1,1 C. 2,1 D. 1,2

答案: B

**解析:**解（法一）令<equation>\left\{ \begin{array}{l l} y_{1}=x_{1}+x_{2}, \\ y_{2}=x_{2}+x_{3}, \\ y_{3}=x_{3}, \end{array} \right.</equation>则<equation>x_{3}-x_{1}=y_{2}-y_{1}</equation>，且该变换为可逆线性变换.在该变换下，二次型<equation>f(x_{1},x_{2},x_{3})</equation>化为<equation>g \left(y _ {1}, y _ {2}, y _ {3}\right) = y _ {1} ^ {2} + y _ {2} ^ {2} - \left(y _ {2} - y _ {1}\right) ^ {2} = 2 y _ {1} y _ {2}.</equation>再令<equation>\left\{ \begin{array}{l l} y_{1}=z_{1}+z_{2}, \\ y_{2}=z_{1}-z_{2}, \\ y_{3}=z_{3}, \end{array} \right.</equation>则<equation>g \left( y_{1}, y_{2}, y_{3} \right)</equation>化为<equation>h \left(z _ {1}, z _ {2}, z _ {3}\right) = 2 \left(z _ {1} + z _ {2}\right) \left(z _ {1} - z _ {2}\right) = 2 z _ {1} ^ {2} - 2 z _ {2} ^ {2}.</equation>因此，<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>的一个标准形为<equation>2z_{1}^{2}-2z_{2}^{2}</equation>其正、负惯性指数分别为1，1.应选B.

（法二）将<equation>f(x_{1},x_{2},x_{3})</equation>展开可得<equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = 2 x _ {2} ^ {2} + 2 x _ {1} x _ {2} + 2 x _ {2} x _ {3} + 2 x _ {1} x _ {3}.</equation>该二次型对应的矩阵为<equation>A=\left( \begin{array}{c c c} 0 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 0 \end{array} \right)</equation>. 不难发现，A的第二行为第一行与第三行的和，故<equation>r(A)\leqslant 2</equation>. 又因为A有一个2阶非零子式<equation>\left| \begin{array}{c c} 0 & 1 \\ 1 & 2 \end{array} \right|</equation>，所以<equation>r(A)\geqslant 2</equation>. 于是，<equation>r(A)=2.</equation>由于二次型的正、负惯性指数之和等于其对应矩阵的秩，而选项C、D的两数之和均为3，故可排除选项C、D.

另一方面，若 f的负惯性指数为0，则 f非负，即对任意<equation>\left(x_{1},x_{2},x_{3}\right)</equation>，均有<equation>f\left(x_{1},x_{2},x_{3}\right)\geqslant 0.</equation>但是，<equation>f(1,0,-1)=1+1-4<0</equation>矛盾.因此，选项A不正确.

根据排除法，应选B.

---

**2020年第20题 | 解答题 | 11分**

20. (本题满分11分)

设二次型<equation>f \left( x_{1}, x_{2} \right)=x_{1}^{2}-4 x_{1} x_{2}+4 x_{2}^{2}</equation>经正交变换<equation>\binom{x_{1}}{x_{2}}=Q \binom{y_{1}}{y_{2}}</equation>化为二次型<equation>g \left( y_{1}, y_{2} \right)=a y_{1}^{2}+4 y_{1} y_{2}+b y_{2}^{2}</equation>其中 a≥b.

I. 求 a,b的值;

II. 求正交矩阵 Q.

**答案:**（ I ）<equation>a=4,b=1;</equation>（Ⅱ）<equation>Q = \left( \begin{array}{c c} - \frac{4}{5} & \frac{3}{5} \\ \frac{3}{5} & \frac{4}{5} \end{array} \right), f \left(x_{1}, x_{2}\right)</equation>经过正交变换<equation>\binom{x_1}{x_2} = Q \binom{y_1}{y_2}</equation>化为二次型<equation>g \left(y_{1}, y_{2}\right).</equation>

**解析:**解（I）写出二次型<equation>f ( x_{1}, x_{2} )=x_{1}^{2}-4 x_{1} x_{2}+4 x_{2}^{2}</equation>对应的矩阵 A，二次型<equation>g ( y_{1}, y_{2} )=a y_{1}^{2}+</equation><equation>4 y_{1} y_{2}+b y_{2}^{2}</equation>对应的矩阵 B.<equation>\boldsymbol {A} = \left( \begin{array}{c c} 1 & - 2 \\ - 2 & 4 \end{array} \right), \quad \boldsymbol {B} = \left( \begin{array}{c c} a & 2 \\ 2 & b \end{array} \right).</equation>由于正交变换也是相似变换，故 A与 B相似。又因为相似的矩阵具有相同的迹与行列式，所以<equation>\left\{ \begin{array}{l} a + b = 5, \\ a b = 4. \end{array} \right.</equation>由 a<equation>\geqslant b</equation>可确定<equation>\left\{ \begin{array}{l l} a=4, \\ b=1. \end{array} \right.</equation>（Ⅱ）由第（Ⅰ）问可知，<equation>A=\left( \begin{array}{cc}1&-2\\ -2&4 \end{array} \right), B=\left( \begin{array}{cc}4&2\\ 2&1 \end{array} \right).</equation>计算 A和B的特征多项式可得<equation>|\lambda E - A| = \left| \begin{array}{cc}\lambda -1 & 2\\ 2 & \lambda -4 \end{array} \right| = \lambda (\lambda -5).</equation>于是 A和B的特征值为5和0.分别计算 A,B的特征向量.

计算 A的属于特征值5的特征向量.

考虑（5E-A）x=0.<equation>5 E - A = \left( \begin{array}{c c} 4 & 2 \\ 2 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c} 2 & 1 \\ 0 & 0 \end{array} \right).</equation>于是，<equation>r ( 5 E-A )=1</equation>，求得<equation>\xi_{1}=(-1,2)^{\mathrm{T}}</equation>为（5E-A）<equation>\boldsymbol{x}=\mathbf{0}</equation>的一个基础解系.<equation>(-1,2)^{\mathrm{T}}</equation>为A的属于特征值5的一个特征向量.

计算 A的属于特征值0的特征向量.

考虑（0E-A）x=0.<equation>- \boldsymbol {A} = \left( \begin{array}{c c} - 1 & 2 \\ 2 & - 4 \end{array} \right) \rightarrow \left( \begin{array}{c c} - 1 & 2 \\ 0 & 0 \end{array} \right).</equation>于是，<equation>r ( 0 E-A)=1</equation>，求得<equation>\boldsymbol{\xi}_{2}=(2,1)^{\mathrm{T}}</equation>为<equation>( 0 E-A ) x=0</equation>的一个基础解系.<equation>( 2,1)^{\mathrm{T}}</equation>为 A的属于特征值0的一个特征向量.

取<equation>P_{1} = \left( \begin{array}{cc} -1 & 2 \\ 2 & 1 \end{array} \right)</equation>，则<equation>P_{1}^{-1}AP_{1} = \left( \begin{array}{cc} 5 & 0 \\ 0 & 0 \end{array} \right)</equation>.

计算 B的属于特征值5的特征向量.

考虑（5E-B）x=0.<equation>5 E - B = \left( \begin{array}{c c} 1 & - 2 \\ - 2 & 4 \end{array} \right) \rightarrow \left( \begin{array}{c c} 1 & - 2 \\ 0 & 0 \end{array} \right).</equation>于是，<equation>r ( 5 E-B )=1</equation>，求得<equation>\eta_{1}=(2,1)^{\mathrm{T}}</equation>为（5E-B）<equation>x=0</equation>的一个基础解系.<equation>(2,1)^{\mathrm{T}}</equation>为B的属于特征值5的一个特征向量.

计算 B的属于特征值0的特征向量.

考虑（0E-B）x=0.<equation>- \boldsymbol {B} = \left( \begin{array}{c c} - 4 & - 2 \\ - 2 & - 1 \end{array} \right) \rightarrow \left( \begin{array}{c c} 2 & 1 \\ 0 & 0 \end{array} \right).</equation>于是，<equation>r ( 0 E-B )=1</equation>，求得<equation>\eta_{2}=(-1,2)^{\mathrm{T}}</equation>为<equation>( 0 E-B ) x=0</equation>的一个基础解系.<equation>(-1,2)^{\mathrm{T}}</equation>为B的属于特征值0的一个特征向量.

取<equation>P_{2} = \left( \begin{array}{cc}2 & -1\\ 1 & 2 \end{array} \right)</equation>，则<equation>P_{2}^{-1}BP_{2} = \left( \begin{array}{cc}5 & 0\\ 0 & 0 \end{array} \right)</equation>.

由于<equation>B=P_{2} P_{1}^{-1} A P_{1} P_{2}^{-1}</equation>，故取<equation>Q=P_{1} P_{2}^{-1}</equation>，则<equation>Q^{-1} A Q=B.</equation>计算得<equation>P_{2}^{-1}=\frac{1}{5}\left( \begin{array}{cc}2&1\\ -1&2 \end{array} \right)</equation>，则<equation>Q=\frac{1}{5}\left( \begin{array}{cc}-1&2\\ 2&1 \end{array} \right)\left( \begin{array}{cc}2&1\\ -1&2 \end{array} \right)=\left( \begin{array}{cc}-\frac{4}{5}&\frac{3}{5}\\ \frac{3}{5}&\frac{4}{5} \end{array} \right).</equation>并且，Q已经是正交矩阵，无需再单位正交化.

因此，<equation>Q = \left( \begin{array}{cc} - \frac{4}{5} & \frac{3}{5} \\ \frac{3}{5} & \frac{4}{5} \end{array} \right), f \left(x_{1}, x_{2}\right)</equation>经过正交变换<equation>\binom{x_1}{x_2} = Q\binom{y_1}{y_2}</equation>化为二次型<equation>g \left(y_{1}, y_{2}\right).</equation>

---

**2019年第6题 | 选择题 | 4分 | 答案: C**

6. 设 A是3阶实对称矩阵，E是3阶单位矩阵.若<equation>A^{2}+A=2 E</equation>，且<equation>|A|=4</equation>，则二次型<equation>x^{\mathrm{T}} A x</equation>的规范形为（    ）

A.<equation>y_{1}^{2}+y_{2}^{2}+y_{3}^{2}</equation>B.<equation>y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>C.<equation>y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>D.<equation>-y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>

答案: C

**解析:**设<equation>\lambda</equation>为 A的一个特征值，<equation>\alpha</equation>为属于特征值<equation>\lambda</equation>的特征向量.

由<equation>A^{2}+A=2 E</equation>可得<equation>(\lambda^{2}+\lambda-2)\alpha=0</equation>. 由于<equation>\alpha</equation>为非零向量，故<equation>\lambda^{2}+\lambda-2=0</equation>. 解得<equation>\lambda=1</equation>或<equation>\lambda=-2</equation>. A的特征值只能取1和-2.

又因为<equation>| A |=4</equation>，所以 A的特征值应为-2，-2，1. 因此，二次型<equation>x^{\mathrm{T}} A x</equation>的正惯性指数为1，负惯性指数为2. 四个选项中，只有<equation>y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>满足该性质. 应选C.

---

**2018年第20题 | 解答题 | 11分**

20. (本题满分11分)

设实二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=\left( x_{1}-x_{2}+x_{3} \right)^{2}+\left( x_{2}+x_{3} \right)^{2}+\left( x_{1}+a x_{3} \right)^{2}</equation>其中 a是参数.

I. 求<equation>f \left( x_{1}, x_{2}, x_{3} \right)=0</equation>的解；

II. 求<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>的规范形.

**答案:**（I）当 a≠2时，<equation>f ( x_{1}, x_{2}, x_{3} )=0</equation>的解为<equation>( x_{1}, x_{2}, x_{3} )^{\mathrm{T}}=(0,0,0)^{\mathrm{T}}</equation>；当 a=2时，<equation>f ( x_{1}, x_{2}, x_{3} )=0</equation>的解为<equation>( x_{1}, x_{2}, x_{3} )^{\mathrm{T}}=k (-2,-1,1)^{\mathrm{T}}</equation>其中 k为任意常数.

（Ⅱ）当 a≠2时， f的规范形为<equation>f=y_{1}^{2}+y_{2}^{2}+y_{3}^{2}</equation>；当 a=2时， f的规范形为<equation>f=z_{1}^{2}+z_{2}^{2}.</equation>

**解析:**解（I）<equation>f \left( x_{1}, x_{2}, x_{3} \right)=0</equation>当且仅当<equation>\left\{ \begin{array}{l l} x_{1}-x_{2}+x_{3}=0, \\ x_{2}+x_{3}=0, \\ x_{1}+a x_{3}=0. \end{array} \right.</equation>记A为该方程组的系数矩阵.对A作初等行变换.<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & - 1 & 1 \\ 0 & 1 & 1 \\ 1 & 0 & a \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c} 1 & - 1 & 1 \\ 0 & 1 & 1 \\ 0 & 1 & a - 1 \end{array} \right) \xrightarrow {r _ {1} + r _ {2}} \frac {r _ {3} ^ {*} - r _ {2}}{r _ {3} ^ {*}} \left( \begin{array}{c c c} 1 & 0 & 2 \\ 0 & 1 & 1 \\ 0 & 0 & a - 2 \end{array} \right).</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

当 a≠2时，<equation>r(A)=3</equation>，方程组只有零解.

当 a=2时，<equation>r ( \mathbf{A} )=2.</equation>方程组的基础解系仅包含一个向量.取<equation>x_{3}</equation>为自由变元，令<equation>x_{3}=1</equation>解得<equation>\left(x_{1},x_{2},x_{3}\right)^{\mathrm{T}}=\left(-2,-1,1\right)^{\mathrm{T}}</equation>为该方程组的一个基础解系.

因此，当<equation>a\neq 2</equation>时，<equation>f(x_{1},x_{2},x_{3})=0</equation>的解为<equation>(x_{1},x_{2},x_{3})^{\mathrm{T}}=(0,0,0)^{\mathrm{T}}</equation>；当<equation>a=2</equation>时，<equation>f(x_{1},x_{2},x_{3})=0</equation>的解为<equation>(x_{1},x_{2},x_{3})^{\mathrm{T}}=k(-2,-1,1)^{\mathrm{T}}</equation>，其中k为任意常数.

（Ⅱ）由<equation>f(x_{1},x_{2},x_{3})</equation>的表达式知，<equation>f(x_{1},x_{2},x_{3})\geqslant 0.</equation>当<equation>a\neq 2</equation>时，由第（I）问可知，<equation>f(x_{1},x_{2},x_{3}) = 0</equation>只有零解，<equation>f</equation>为正定二次型.因此，当<equation>a\neq 2</equation>时，<equation>f</equation>的规范形为<equation>f = y_{1}^{2} + y_{2}^{2} + y_{3}^{2}</equation>.

当 a=2时，f不满秩.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= \left(x _ {1} - x _ {2} + x _ {3}\right) ^ {2} + \left(x _ {2} + x _ {3}\right) ^ {2} + \left(x _ {1} + 2 x _ {3}\right) ^ {2} \\ &= 2 x _ {1} ^ {2} + 2 x _ {2} ^ {2} + 6 x _ {3} ^ {2} - 2 x _ {1} x _ {2} + 6 x _ {1} x _ {3}. \end{aligned}</equation>记f对应的对称矩阵为<equation>B=\left( \begin{array}{c c c} 2 & -1 & 3 \\ -1 & 2 & 0 \\ 3 & 0 & 6 \end{array} \right).</equation>下面用三种方法求求 f的规范形.

（法一）由<equation>f ( x_{1}, x_{2}, x_{3} ) \geqslant0</equation>可知 f的负惯性指数为0（否则，若规范形有负系数，不妨设规范形为<equation>f=y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>，取<equation>( y_{1}, y_{2}, y_{3} )=(0,0,1)</equation>，则<equation>f ( y_{1}, y_{2}, y_{3} )=-1<0</equation>，矛盾).由于 B的秩等于 f的正、负惯性指数之和，故 f的正惯性指数等于 r（B）.

计算<equation>| B |</equation>得<equation>| B |=0</equation>，故<equation>r ( B ) \leqslant 2</equation>.又因为B有一个2阶子式<equation>\left| \begin{array}{c c} {2} & {-1} \\ {-1} & {2} \end{array} \right|=3\neq0</equation>，所以<equation>r ( B ) \geqslant2</equation>因此，<equation>r ( B )=2.</equation>综上所述，<equation>f</equation>的正惯性指数为2，负惯性指数为0.<equation>f</equation>的规范形为<equation>f=z_{1}^{2}+z_{2}^{2}.</equation>（法二）计算 B的特征值，从而得到 f的正、负惯性指数.

计算 B的特征多项式.<equation>| \lambda E - B | = \left| \begin{array}{c c c} \lambda - 2 & 1 & - 3 \\ 1 & \lambda - 2 & 0 \\ - 3 & 0 & \lambda - 6 \end{array} \right| = \lambda \left(\lambda^ {2} - 1 0 \lambda + 1 8\right).</equation>解<equation>\lambda^{2}-1 0 \lambda+1 8=0</equation>可得<equation>\lambda_{1,2}=\frac{1 0 \pm \sqrt{1 0 0-7 2}}{2}=5 \pm \sqrt{7}.</equation>由于<equation>5+\sqrt{7}>0, 5-\sqrt{7}>0</equation>，故f有两个正特征值，一个零特征值，从而 f的正惯性指数为2，负惯性指数为0.

因此，<equation>f</equation>的规范形为<equation>f = z_{1}^{2} + z_{2}^{2}</equation>.

（法三）配方法.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= 2 x _ {1} ^ {2} + 2 x _ {2} ^ {2} + 6 x _ {3} ^ {2} - 2 x _ {1} x _ {2} + 6 x _ {1} x _ {3} = 2 \left(x _ {1} ^ {2} - x _ {1} x _ {2} + 3 x _ {1} x _ {3}\right) + 2 x _ {2} ^ {2} + 6 x _ {3} ^ {2} \\ &= 2 \left(x _ {1} - \frac {x _ {2}}{2} + \frac {3}{2} x _ {3}\right) ^ {2} + \frac {3}{2} x _ {2} ^ {2} - \frac {9}{2} x _ {3} ^ {2} + 3 x _ {2} x _ {3} + 6 x _ {3} ^ {2} \\ &= 2 \left(x _ {1} - \frac {x _ {2}}{2} + \frac {3}{2} x _ {3}\right) ^ {2} + \frac {3}{2} \left(x _ {2} + x _ {3}\right) ^ {2}. \end{aligned}</equation>令<equation>\left\{ \begin{array}{l l} z_{1}=\sqrt{2}\left(x_{1}-\frac{x_{2}}{2}+\frac{3}{2} x_{3}\right), \\ z_{2}=\sqrt{\frac{3}{2}}\left(x_{2}+x_{3}\right), \\ z_{3}=x_{3}, \end{array} \right.</equation>则<equation>f \left(z_{1}, z_{2}, z_{3}\right)=z_{1}^{2}+z_{2}^{2}.</equation>因此，<equation>f</equation>的规范形为<equation>f = z_{1}^{2} + z_{2}^{2}</equation>.

---

**2017年第21题 | 解答题 | 11分**

21. (本题满分11分)

设二次型<equation>f \left(x_{1}, x_{2}, x_{3}\right)=2 x_{1}^{2}-x_{2}^{2}+a x_{3}^{2}+2 x_{1} x_{2}-8 x_{1} x_{3}+2 x_{2} x_{3}</equation>在正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>下的标准形为<equation>\lambda_{1} y_{1}^{2}+\lambda_{2} y_{2}^{2}</equation>求 a的值及一个正交矩阵 Q.

**答案:**<equation>a = 2, Q = \left( \begin{array}{c c c} - \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {3}} & \frac {1}{\sqrt {6}} \\ 0 & - \frac {1}{\sqrt {3}} & \frac {2}{\sqrt {6}} \\ \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {3}} & \frac {1}{\sqrt {6}} \end{array} \right), \text {且} Q ^ {\mathrm {T}} A Q = \left( \begin{array}{c c c} 6 & 0 & 0 \\ 0 & - 3 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>

**解析:**记二次型 f对应的实对称矩阵为 A，则<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 2 & 1 & - 4 \\ 1 & - 1 & 1 \\ - 4 & 1 & a \end{array} \right).</equation>由于 f在正交变换<equation>x=Q y</equation>下的标准形为<equation>\lambda_{1} y_{1}^{2}+\lambda_{2} y_{2}^{2}</equation>，故 A的特征值为<equation>\lambda_{1},\lambda_{2},0.</equation>从而<equation>|A|=0.</equation>计算 A的行列式得<equation>| A | = - 3 a + 6.</equation>因此，<equation>a = 2</equation>，<equation>A = \left( \begin{array}{c c c} 2 & 1 & -4 \\ 1 & -1 & 1 \\ -4 & 1 & 2 \end{array} \right)</equation>计算 A的特征多项式得<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - 2 & - 1 & 4 \\ - 1 & \lambda + 1 & - 1 \\ 4 & - 1 & \lambda - 2  \right| \xlongequal {r _ {1} - r _ {3}} \left| \begin{array}{c c c} \lambda - 6 & 0 & 6 - \lambda \\ - 1 & \lambda + 1 & - 1 \\ 4 & - 1 & \lambda - 2  \right| \\ \underline {{\underline {{c _ {3} + c _ {1}}}}} \left| \begin{array}{c c c} \lambda - 6 & 0 & 0 \\ - 1 & \lambda + 1 & - 2 \\ 4 & - 1 & \lambda + 2  \right| &= \lambda (\lambda - 6) (\lambda + 3). \end{aligned}</equation>于是，A的3个特征值分别为6，-3，0.

当<equation>\lambda=6</equation>时，<equation>\begin{array}{l} 6 E - A = \left( \begin{array}{c c c} 4 & - 1 & 4 \\ - 1 & 7 & - 1 \\ 4 & - 1 & 4 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c} 4 & - 1 & 4 \\ - 1 & 7 & - 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} + 4 r _ {2}} \left( \begin{array}{c c c} 0 & 1 & 0 \\ - 1 & 7 & - 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} - 7 r _ {1} ^ {* *}} r _ {2} ^ {*} \times (- 1) \left( \begin{array}{c c c} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>因此，<equation>\boldsymbol{\eta}_{1}=(-1,0,1)^{\mathrm{T}}</equation>为（6E-A）<equation>\boldsymbol{x}=\mathbf{0}</equation>的一个基础解系.

当<equation>\lambda=-3</equation>时，<equation>\begin{array}{l} - 3 E - A = \left( \begin{array}{c c c} - 5 & - 1 & 4 \\ - 1 & - 2 & - 1 \\ 4 & - 1 & - 5 \end{array} \right) \xrightarrow [ r _ {3} ^ {*} - r _ {2} ]{r _ {3} + r _ {1}} \left( \begin{array}{c c c} - 5 & - 1 & 4 \\ - 1 & - 2 & - 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {2} \times (- 1) ]{r _ {1} - 5 r _ {2}} \left( \begin{array}{c c c} 0 & 9 & 9 \\ 1 & 2 & 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow [ r _ {2} ^ {*} - r _ {1} ^ {* *} ]{r _ {1} ^ {*} \times \frac {1}{9}} \left( \begin{array}{c c c} 0 & 1 & 1 \\ 1 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>因此，<equation>\boldsymbol{\eta}_{2} = (1, - 1, 1)^{\mathrm{T}}</equation>为<equation>(-3E-A)x=0</equation>的一个基础解系.

当<equation>\lambda = 0</equation>时，<equation>\begin{array}{l} 0 E - A = \left( \begin{array}{c c c} - 2 & - 1 & 4 \\ - 1 & 1 & - 1 \\ 4 & - 1 & - 2 \end{array} \right) \xrightarrow {r _ {3} + r _ {1}} r _ {3} ^ {*} + 2 r _ {2} \left( \begin{array}{c c c} - 2 & - 1 & 4 \\ - 1 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} - 2 r _ {2}} r _ {1} ^ {*} \times \left(- \frac {1}{3}\right) \left( \begin{array}{c c c} 0 & 1 & - 2 \\ - 1 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} \times (- 1) + r _ {1} ^ {* *}} \left( \begin{array}{c c c} 0 & 1 & - 2 \\ 1 & 0 & - 1 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>因此，<equation>\boldsymbol{\eta}_{3} = (1,2,1)^{\mathrm{T}}</equation>为<equation>(0 E - A) x = 0</equation>的一个基础解系.

由于实对称矩阵对应于不同特征值的特征向量相互正交，故只需将所得特征向量单位化

将<equation>\boldsymbol{\eta}_{1},\boldsymbol{\eta}_{2},\boldsymbol{\eta}_{3}</equation>分别单位化，作为Q的列向量，得正交矩阵<equation>Q=\left( \begin{array}{c c c} -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \\ 0 & -\frac{1}{\sqrt{3}} & \frac{2}{\sqrt{6}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \end{array} \right)</equation>，且<equation>Q^{\mathrm{T}}AQ=</equation><equation>\left( \begin{array}{c c c} 6 & 0 & 0 \\ 0 & - 3 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>即f在正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>下的标准形为<equation>f=6 y_{1}^{2}-3 y_{2}^{2}.</equation>

---

**2016年第6题 | 选择题 | 4分 | 答案: C**

6. 设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=a \left( x_{1}^{2}+x_{2}^{2}+x_{3}^{2} \right)+2 x_{1} x_{2}+2 x_{2} x_{3}+2 x_{1} x_{3}</equation>的正、负惯性指数分别为1，2，则（    )

A. a > 1 B. a < -2 C.<equation>- 2 < a < 1</equation>D. a =1或a=-2

答案: C

**解析:**解（法一）f对应的对称矩阵为<equation>A=\left( \begin{array}{c c c} a & 1 & 1 \\ 1 & a & 1 \\ 1 & 1 & a \end{array} \right).</equation>A正交相似于一个对角矩阵，该矩阵的主对角元为 A的特征值.

计算 A的特征多项式，得<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - a & - 1 & - 1 \\ - 1 & \lambda - a & - 1 \\ - 1 & - 1 & \lambda - a  \right| \xlongequal {c _ {2} - c _ {3}} \left| \begin{array}{c c c} \lambda - a & 0 & - 1 \\ - 1 & \lambda - a + 1 & - 1 \\ - 1 & - (\lambda - a + 1) & \lambda - a  \right| \\ \underline {{\text {按 第一 行 展 开}}} (\lambda - a) (\lambda - a + 1) (\lambda - a - 1) - 2 (\lambda - a + 1) \\ &= (\lambda - a + 1) ^ {2} (\lambda - a - 2). \end{aligned}</equation>因此，A的特征值为 a-1，a-1，a+2.

由于 a+2>a-1，故若 f的正、负惯性指数分别为1，2，则<equation>\left\{\begin{array}{l l}a-1<0,\\ a+2>0.\end{array}\right.</equation>解得-2<a<1.应选C.

（法二）如法一，写出 A.

由于二次型 f的正、负惯性指数分别为1，2，故 A的特征值有一个为正值，两个为负值，从而<equation>| A | > 0.</equation>计算 A的行列式.<equation>| A | = \left| \begin{array}{c c c} a & 1 & 1 \\ 1 & a & 1 \\ 1 & 1 & a \end{array} \right| = (a - 1) ^ {2} (a + 2).</equation>由于<equation>|A| > 0</equation>，故<equation>a+2 > 0</equation>，即<equation>a > -2</equation>.由此可以排除选项B和选项D.

另一方面，若 a > 1，则 a > 0，<equation>a^{2}-1 > 0</equation><equation>| A | > 0</equation>A的各阶顺序主子式皆为正.由正定矩阵的判别法可知，A为正定矩阵，从而 f的正惯性指数为3.这与 f的正、负惯性指数分别为1，2矛盾，故可排除选项A.

因此，应选C.

---

**2015年第6题 | 选择题 | 4分 | 答案: A**

6. 设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>在正交变换<equation>x=P y</equation>下的标准形为<equation>2 y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>其中<equation>P=\left( e_{1}, e_{2}, e_{3} \right)</equation>若<equation>Q=\left( e_{1},-e_{3}, e_{2} \right)</equation>则<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>在正交变换<equation>x=Q y</equation>下的标准形为（    )

A.<equation>2 y_{1}^{2}-y_{2}^{2}+y_{3}^{2}</equation>B.<equation>2 y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>C.<equation>2 y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>D.<equation>2 y_{1}^{2}+y_{2}^{2}+y_{3}^{2}</equation>

答案: A

**解析:**解（法一）设<equation>f=x^{\mathrm{T}}Ax</equation>，则由题设知，<equation>f = \left(\boldsymbol {P} \boldsymbol {y}\right) ^ {\mathrm {T}} \boldsymbol {A} \left(\boldsymbol {P} \boldsymbol {y}\right) = \boldsymbol {y} ^ {\mathrm {T}} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} \boldsymbol {y} = 2 y _ {1} ^ {2} + y _ {2} ^ {2} - y _ {3} ^ {2}.</equation>从而<equation>P^{\mathrm{T}}A P = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -1 \end{array} \right).</equation>又由于<equation>Q = \left(e_{1}, - e_{3}, e_{2}\right) = \left(e_{1}, e_{2}, e_{3}\right)\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{array} \right) = P\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{array} \right)</equation>，故<equation>\begin{aligned} f &= \boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {x} = \left(\boldsymbol {Q} \boldsymbol {y}\right) ^ {\mathrm {T}} \boldsymbol {A} \left(\boldsymbol {Q} \boldsymbol {y}\right) = \boldsymbol {y} ^ {\mathrm {T}} \boldsymbol {Q} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {Q} \boldsymbol {y} = \boldsymbol {y} ^ {\mathrm {T}} \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & - 1 & 0  \right) ^ {\mathrm {T}} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & - 1 & 0  \right) \boldsymbol {y} \\ &= \boldsymbol {y} ^ {\mathrm {T}} \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & - 1 \\ 0 & 1 & 0  \right) \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & - 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & - 1 & 0  \right) \boldsymbol {y} \\ &= \boldsymbol {y} ^ {\mathrm {T}} \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 1  \right) \boldsymbol {y} &= 2 y _ {1} ^ {2} - y _ {2} ^ {2} + y _ {3} ^ {2}. \end{aligned}</equation>因此，<equation>f ( x_{1}, x_{2}, x_{3} )</equation>在<equation>\mathbf{x}=\mathbf{Q y}</equation>的标准形为<equation>f=2 y_{1}^{2}-y_{2}^{2}+y_{3}^{2}.</equation>应选A.

（法二）由题设知，二次型<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>在正交变换<equation>\boldsymbol{x}=\boldsymbol{P}\boldsymbol{y}</equation>下的标准形为<equation>f=2y_{1}^{2}+y_{2}^{2}-y_{3}^{2}.</equation>因此，该二次型所对应的对称矩阵A的特征值为2，1，-1，而<equation>e_{1},e_{2},e_{3}</equation>分别为属于特征值2，1，-1的特征向量.

若<equation>Q=(\boldsymbol{e}_1,-\boldsymbol{e}_3,\boldsymbol{e}_2)</equation>，则由<equation>A(-e_{3})=-Ae_{3}=-(-e_{3})</equation>可知<equation>-e_{3}</equation>也为属于特征值-1的特征向量，故<equation>Q^{\mathrm{T}}AQ=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{array} \right). f(x_{1},x_{2},x_{3})</equation>在<equation>\boldsymbol{x}=Q\boldsymbol{y}</equation>下的标准形为<equation>f=2y_{1}^{2}-y_{2}^{2}+y_{3}^{2}.</equation>应选A.

---

**2014年第13题 | 填空题 | 4分**

13. 设二次型<equation>f(x_{1},x_{2},x_{3})=x_{1}^{2}-x_{2}^{2}+2a x_{1} x_{3}+4 x_{2} x_{3}</equation>的负惯性指数为1，则 a的取值范围是 ___

**解析:**解 （法一）用配方法将原二次型化为标准形.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= \left(x _ {1} + a x _ {3}\right) ^ {2} - a ^ {2} x _ {3} ^ {2} - \left(x _ {2} - 2 x _ {3}\right) ^ {2} + 4 x _ {3} ^ {2} \\ &= \left(x _ {1} + a x _ {3}\right) ^ {2} - \left(x _ {2} - 2 x _ {3}\right) ^ {2} + \left(4 - a ^ {2}\right) x _ {3} ^ {2}. \end{aligned}</equation>因此，若二次型<equation>f(x_{1},x_{2},x_{3})</equation>的负惯性指数为1，则<equation>4 - a^{2}\geqslant 0</equation>，即<equation>a\in[-2,2]</equation>（法二）写出二次型<equation>f(x_{1},x_{2},x_{3})</equation>对应的对称矩阵<equation>A.</equation><equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & 0 & a \\ 0 & - 1 & 2 \\ a & 2 & 0 \end{array} \right).</equation>计算<equation>A</equation>的行列式得，<equation>|A| = a^2 - 4.</equation>A的迹等于零，说明A的特征值之和为零.

下面我们证明，当3阶非零实对称矩阵<equation>A</equation>的迹为零时，<equation>A</equation>的负惯性指数为1等价于<equation>|A| \leqslant 0.</equation>当3阶非零实对称矩阵<equation>A</equation>的迹为零时，由<equation>A</equation>的负惯性指数为1可知，<equation>A</equation>的特征值可能为两正、一负，或者一正、一零、一负.在这两种情形下，<equation>|A| \leqslant 0.</equation>若<equation>A</equation>为3阶非零实对称矩阵，且<equation>|A| \leqslant 0</equation>，则<equation>A</equation>的特征值的符号有五种可能：（1）两正、一负；（2）一正、一零、一负；（3）两零、一负；（4）三负；（5）全为零.两个零特征值、一个负特征值和三个负特征值的情形与<equation>A</equation>的迹为零矛盾.特征值全为零的情形与<equation>A</equation>是非零实对称矩阵矛盾，因为若<equation>A</equation>的特征值全为零，则<equation>A</equation>相似于零矩阵，从而<equation>A</equation>为零矩阵.因此，<equation>A</equation>的特征值仅可能为两正、一负，或一正、一零、一负.在这两种情形下，<equation>A</equation>的负惯性指数都为1.

综上所述，<equation>A</equation>的负惯性指数为1等价于<equation>|A| \leqslant 0</equation>，即<equation>a \in [-2,2]</equation>

---

**2013年第21题 | 解答题 | 11分**


设二次型<equation>f(x_{1},x_{2},x_{3}) = 2\left(a_{1}x_{1} + a_{2}x_{2} + a_{3}x_{3}\right)^{2} + \left(b_{1}x_{1} + b_{2}x_{2} + b_{3}x_{3}\right)^{2}</equation>，记<equation>\begin{aligned} \alpha &= \left(  a _ {1} \\ a _ {2} \\ a _ {3}  \right), \quad \beta &= \left(  b _ {1} \\ b _ {2} \\ b _ {3}  \right) \end{aligned}</equation>I. 证明二次型 f对应的矩阵为<equation>2\alpha\alpha^{\mathrm{T}}+\beta\beta^{\mathrm{T}};</equation>II. 若<equation>\alpha, \beta</equation>正交且均为单位向量，证明 f在正交变换下的标准形为<equation>2y_{1}^{2}+y_{2}^{2}.</equation>

**答案:**（21）（I）证明略；

（Ⅱ）证明略.

**解析:**证（I）记<equation>\boldsymbol{x} = (x_{1},x_{2},x_{3})^{\mathrm{T}}</equation>，f对应的矩阵为A，A为对称矩阵，则<equation>\begin{aligned} a _ {1} x _ {1} + a _ {2} x _ {2} + a _ {3} x _ {3} &= \boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\alpha} = \boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {x}, \quad b _ {1} x _ {1} + b _ {2} x _ {2} + b _ {3} x _ {3} = \boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\beta} = \boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {x}. \\ f \left(x _ {1}, x _ {2}, x _ {3}\right) &= 2 \left(\boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\alpha}\right) \left(\boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {x}\right) + \left(\boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\beta}\right) \left(\boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {x}\right) = \boldsymbol {x} ^ {\mathrm {T}} \left(2 \alpha \boldsymbol {\alpha} ^ {\mathrm {T}} + \beta \boldsymbol {\beta} ^ {\mathrm {T}}\right) \boldsymbol {x}. \end{aligned}</equation>又由于<equation>(2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}})^{\mathrm{T}} = 2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>，故<equation>2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>是对称矩阵.于是<equation>2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>为所求A.

（Ⅱ）（法一）由<equation>A = 2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>且<equation>\alpha</equation>与<equation>\beta</equation>相互正交<equation>(\alpha^{\mathrm{T}}\beta = 0, \beta^{\mathrm{T}}\alpha = 0)</equation>得，<equation>A \alpha = \left(2 \alpha \alpha^ {\mathrm {T}} + \beta \beta^ {\mathrm {T}}\right) \alpha = 2 \alpha , \quad A \beta = \left(2 \alpha \alpha^ {\mathrm {T}} + \beta \beta^ {\mathrm {T}}\right) \beta = \beta .</equation>因此，2,1均为<equation>A</equation>的特征值，而<equation>\alpha ,\beta</equation>分别为属于特征值2,1的特征向量.

下面还需确定 A的另一个特征值.

考虑 A的秩.

由于对任何非零<equation>n</equation>维列向量<equation>\alpha ,\beta ,</equation>矩阵<equation>\beta \alpha^{\mathrm{T}}</equation>的秩均为1，故<equation>r (\boldsymbol {A}) = r \left(2 \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}\right) \leqslant r \left(2 \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}}\right) + r \left(\boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}\right) = 2.</equation>于是，<equation>A</equation>不满秩，0也是<equation>A</equation>的一个特征值.

因此，存在正交矩阵<equation>P</equation>使得<equation>P^{\mathrm{T}}AP = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).f</equation>在正交变换<equation>x = Py</equation>下的标准形为<equation>f = 2y_{1}^{2} + y_{2}^{2}</equation>.

（法二）取<equation>\gamma</equation>为与<equation>\alpha, \beta</equation>均正交的单位向量，可取<equation>\gamma = \frac{\alpha \times \beta}{\| \alpha \times \beta \|}</equation>（<equation>\alpha \times \beta</equation>为向量<equation>\alpha, \beta</equation>的向量积，<equation>\| \alpha \times \beta \|</equation>为向量<equation>\alpha \times \beta</equation>的模），则<equation>P = (\alpha ,\beta ,\gamma)</equation>为正交矩阵.<equation>\begin{aligned} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} &= \left(  \boldsymbol {\alpha} ^ {\mathrm {T}} \\ \boldsymbol {\beta} ^ {\mathrm {T}} \\ \boldsymbol {\gamma} ^ {\mathrm {T}}  \right) \left(2 \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}\right) (\boldsymbol {\alpha}, \boldsymbol {\beta}, \gamma) &= \left(  2 \boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}} \\ 2 \boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}} \\ 2 \gamma^ {\mathrm {T}} \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \gamma^ {\mathrm {T}} \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}  \right) (\boldsymbol {\alpha}, \boldsymbol {\beta}, \gamma). \end{aligned}</equation>由于<equation>\alpha ,\beta ,\gamma</equation>相互正交，且均为单位向量，故<equation>\alpha^{\mathrm{T}}\boldsymbol{\beta} = \beta^{\mathrm{T}}\alpha = \gamma^{\mathrm{T}}\alpha = \gamma^{\mathrm{T}}\boldsymbol{\beta} = 0,</equation><equation>\alpha^{\mathrm{T}}\alpha = \beta^{\mathrm{T}}\beta = 1.</equation><equation>\boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} = \left( \begin{array}{c} 2 \boldsymbol {\alpha} ^ {\mathrm {T}} \\ \boldsymbol {\beta} ^ {\mathrm {T}} \\ \mathbf {0} \end{array} \right) (\boldsymbol {\alpha}, \boldsymbol {\beta}, \gamma) = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>因此，<equation>f</equation>在正交变换<equation>x = P y</equation>下的标准形为<equation>f = 2y_{1}^{2} + y_{2}^{2}</equation>.

---

**2012年第21题 | 解答题 | 11分**

21. (本题满分11分)

已知<equation>A=\left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ -1 & 0 & a \\ 0 & a & -1 \end{array} \right)</equation>，二次型<equation>f(x_{1},x_{2},x_{3})=\boldsymbol{x}^{\mathrm{T}}(\boldsymbol{A}^{\mathrm{T}}\boldsymbol{A})\boldsymbol{x}</equation>的秩为2.

I. 求实数 a 的值；

II. 求正交变换<equation>x = Qy</equation>将<equation>f</equation>化为标准形.

**答案:**(21) （I）<equation>a=-1;</equation>（Ⅱ）<equation>Q=\left( \begin{array}{c c c} \frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{6}} & \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{3}} \\ \frac{2}{\sqrt{6}} & 0 & \frac{1}{\sqrt{3}} \end{array} \right)</equation>，正交变换<equation>x=Qy</equation>将二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>变成标准

形<equation>f=6 y_{1}^{2}+2 y_{2}^{2}.</equation>

**解析:**解（I）（法一）二次型 f的秩等于它所对应的实对称矩阵<equation>A^{\mathrm{T}}A</equation>的秩，于是<equation>r(A^{\mathrm{T}}A)=2.</equation>下面我们证明<equation>r(A^{\mathrm{T}}A)=r(A).</equation>由于<equation>A^{\mathrm{T}}A</equation>与A的列数相等，故证明<equation>r( A^{\mathrm{T}}A)=r(A)</equation>只需要证明<equation>A^{\mathrm{T}}Ax=0</equation>与<equation>Ax=0</equation>同解.若 x满足<equation>Ax=0</equation>，则<equation>A^{\mathrm{T}}(Ax)=0</equation>即<equation>( A^{\mathrm{T}}A ) x=0.</equation>另一方面，若 x满足<equation>\left( A^{\mathrm{T}} A \right) x=0</equation>，则<equation>x^{\mathrm{T}} \left( A^{\mathrm{T}} A \right) x=0</equation>，即<equation>\left( A x \right)^{\mathrm{T}} \left( A x \right)=0</equation>.由于<equation>\alpha^{\mathrm{T}} \alpha=0</equation>当且仅当<equation>\alpha=0</equation>，故<equation>A x=0.</equation>因此，<equation>r(\mathbf{A})=r(\mathbf{A}^{\mathrm{T}}\mathbf{A})=2.</equation>我们可以对<equation>A</equation>作初等行变换，求得<equation>r(A) = 2</equation>时的<equation>a</equation>的值.<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ - 1 & 0 & a \\ 0 & a & - 1 \end{array} \right) \xrightarrow [ r _ {4} - a r _ {2} ]{r _ {3} + r _ {1}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & a + 1 \\ 0 & 0 & - a - 1 \end{array} \right) \xrightarrow [ r _ {4} ^ {*} + r _ {3} ^ {*} ]{r _ {4} ^ {*} + r _ {3} ^ {*}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & a + 1 \\ 0 & 0 & 0 \end{array} \right).</equation>由此可见，仅当<equation>a + 1 = 0</equation>时，<equation>r(A) = 2</equation>，故<equation>a = -1</equation>（法二）由于<equation>r(\mathbf{A}^{\mathrm{T}}\mathbf{A})=2</equation>，而<equation>\mathbf{A}^{\mathrm{T}}\mathbf{A}</equation>为<equation>3\times 3</equation>矩阵，故<equation>|\mathbf{A}^{\mathrm{T}}\mathbf{A}|=0.</equation><equation>\boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {A} = \left( \begin{array}{c c c c} 1 & 0 & - 1 & 0 \\ 0 & 1 & 0 & a \\ 1 & 1 & a & - 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ - 1 & 0 & a \\ 0 & a & - 1 \end{array} \right) = \left( \begin{array}{c c c} 2 & 0 & 1 - a \\ 0 & 1 + a ^ {2} & 1 - a \\ 1 - a & 1 - a & 3 + a ^ {2} \end{array} \right).</equation>求得<equation>|\mathbf{A}^{\mathrm{T}}\mathbf{A}| = (a^{2} + 3)(a + 1)^{2}</equation>. 因此，由<equation>|\mathbf{A}^{\mathrm{T}}\mathbf{A}| = 0</equation>可得<equation>a = -1</equation>（Ⅱ）由第（I）问可得，<equation>A^{\mathrm{T}}A = \left( \begin{array}{c c c} 2 & 0 & 2 \\ 0 & 2 & 2 \\ 2 & 2 & 4 \end{array} \right)</equation>，从而<equation>A^{\mathrm{T}}A</equation>的特征多项式为<equation>| \lambda E - A ^ {\mathrm {T}} A | = \left| \begin{array}{c c c} \lambda - 2 & 0 & - 2 \\ 0 & \lambda - 2 & - 2 \\ - 2 & - 2 & \lambda - 4 \end{array} \right| = \lambda (\lambda - 2) (\lambda - 6).</equation><equation>A^{\mathrm{T}}A</equation>的特征值为6,2,0.

下面分别计算属于特征值6,2,0的特征向量.

当<equation>\lambda=6</equation>时，<equation>\begin{array}{l} 6 E - A ^ {\mathrm {T}} A = \left( \begin{array}{c c c} 4 & 0 & - 2 \\ 0 & 4 & - 2 \\ - 2 & - 2 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 0 & 2 & - 1 \\ 1 & 1 & - 1 \end{array} \right) \xrightarrow {r _ {3} - r _ {2}} \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 0 & 2 & - 1 \\ 1 & - 1 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} - r _ {1} + 2 r _ {3} ^ {*}} \binom {2} {r _ {2} ^ {*} \leftrightarrow r _ {3} ^ {*}} \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 1 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right), \\ \end{array}</equation>得<equation>\left\{ \begin{array}{l} 2x_{1} - x_{3} = 0, \\ x_{1} - x_{2} = 0. \end{array} \right.</equation>解得该方程组的一个基础解系<equation>\xi_{1} = (1,1,2)^{\mathrm{T}}.</equation>当<equation>\lambda=2</equation>时，<equation>2 \boldsymbol {E} - \boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {A} = \left( \begin{array}{c c c} 0 & 0 & - 2 \\ 0 & 0 & - 2 \\ - 2 & - 2 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 1 \\ 0 & 0 & 1 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {3} - r _ {2} ]{r _ {1} - r _ {2}} \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right),</equation>得<equation>\left\{ \begin{array}{l}x_{1} + x_{2} = 0,\\ x_{3} = 0. \end{array} \right.</equation>解得该方程组的一个基础解系<equation>\xi_{2} = (-1,1,0)^{\mathrm{T}}.</equation>当<equation>\lambda=0</equation>时，<equation>0 \boldsymbol {E} - \boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {A} = \left( \begin{array}{c c c} - 2 & 0 & - 2 \\ 0 & - 2 & - 2 \\ - 2 & - 2 & - 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 2 \end{array} \right) \xrightarrow {r _ {3} - r _ {1} - r _ {2}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right),</equation>得<equation>\left\{ \begin{array}{l}x_{1} + x_{3} = 0,\\ x_{2} + x_{3} = 0. \end{array} \right.</equation>解得该方程组的一个基础解系<equation>\xi_{3} = (-1, -1, 1)^{\mathrm{T}}.</equation>由于实对称矩阵属于不同特征值的特征向量相互正交，故<equation>\xi_{1},\xi_{2},\xi_{3}</equation>相互正交.将<equation>\xi_{1},\xi_{2},\xi_{3}</equation>单位化，得<equation>\boldsymbol {\alpha} _ {1} = \frac {1}{\sqrt {6}} \left( \begin{array}{c} 1 \\ 1 \\ 2 \end{array} \right), \quad \boldsymbol {\alpha} _ {2} = \frac {1}{\sqrt {2}} \left( \begin{array}{c} - 1 \\ 1 \\ 0 \end{array} \right), \quad \boldsymbol {\alpha} _ {3} = \frac {1}{\sqrt {3}} \left( \begin{array}{c} - 1 \\ - 1 \\ 1 \end{array} \right).</equation>取<equation>Q = \left(\alpha_{1},\alpha_{2},\alpha_{3}\right)</equation>，则<equation>Q</equation>为正交矩阵，且<equation>Q^{\mathrm{T}} \left(A^{\mathrm{T}} A\right) Q = \left( \begin{array}{c c c} 6 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>因此，当<equation>Q=\left( \begin{array}{c c c} {\frac{1}{\sqrt{6}}} & {-\frac{1}{\sqrt{2}}} & {-\frac{1}{\sqrt{3}}} \\ {\frac{1}{\sqrt{6}}} & {\frac{1}{\sqrt{2}}} & {-\frac{1}{\sqrt{3}}} \\ {\frac{2}{\sqrt{6}}} & {0} & {\frac{1}{\sqrt{3}}} \end{array} \right)</equation>时，正交变换<equation>x=Qy</equation>将二次型<equation>f(x_{1},x_{2},x_{3})</equation>变成标准

形<equation>f=6 y_{1}^{2}+2 y_{2}^{2}.</equation>

---

**2011年第13题 | 填空题 | 4分**

13. 设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=\boldsymbol{x}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{x}</equation>的秩为1，A的各行元素之和为3，则 f在正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>下的标准形为

**解析:**解 设矩阵<equation>A = \left( \begin{array}{l l l} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{array} \right)</equation>.由已知条件知<equation>\left\{ \begin{array}{l l l} a_{11} + a_{12} + a_{13} = 3, \\ a_{21} + a_{22} + a_{23} = 3, \\ a_{31} + a_{32} + a_{33} = 3, \end{array} \right.</equation>即<equation>\left( \begin{array}{l l l} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{array} \right)\left( \begin{array}{l} 1 \\ 1 \\ 1 \end{array} \right) = 3\left( \begin{array}{l} 1 \\ 1 \\ 1 \end{array} \right)</equation>于是3是<equation>A</equation>的特征值.又因为<equation>r(A) = 1</equation>，且实对称矩阵<equation>A</equation>相似于以其特征值为主对角元的对角矩阵，所以0是<equation>A</equation>的2重特征值.因此，<equation>A</equation>的所有特征值为3，0，0，<equation>f</equation>在正交变换<equation>x = Qy</equation>下的标准形为<equation>3y_{1}^{2}</equation>

---

**2009年第21题 | 解答题 | 11分**

21. (本题满分11分)

设二次型<equation>f \left(x_{1}, x_{2}, x_{3}\right)=a x_{1}^{2}+a x_{2}^{2}+(a-1) x_{3}^{2}+2 x_{1} x_{3}-2 x_{2} x_{3}</equation>I. 求二次型 f的矩阵的所有特征值；

II. 若二次型 f的规范形为<equation>y_{1}^{2}+y_{2}^{2}</equation>，求 a的值.

**答案:**(21) ( I ) a, a-2, a+1;

( II ) a=2.

**解析:**（I）二次型<equation>f</equation>的矩阵为<equation>A=\left( \begin{array}{c c c} a & 0 & 1 \\ 0 & a & -1 \\ 1 & -1 & a-1 \end{array} \right).</equation>计算<equation>A</equation>的特征多项式<equation>|\lambda E - A|</equation>，得<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - a & 0 & - 1 \\ 0 & \lambda - a & 1 \\ - 1 & 1 & \lambda - a + 1  \right| \xlongequal {\text {按 第一 行 展 开}} (\lambda - a) \left[ (\lambda - a) (\lambda - a + 1) - 1 \right] - (\lambda - a) \\ &= (\lambda - a) \left[ (\lambda - a) ^ {2} + (\lambda - a) - 2 \right] = (\lambda - a) (\lambda - a + 2) (\lambda - a - 1). \end{aligned}</equation>因此，<equation>A</equation>的特征值为<equation>a, a - 2, a + 1.</equation>（Ⅱ）由<equation>f</equation>的规范形为<equation>y_{1}^{2} + y_{2}^{2}</equation>知，<equation>A</equation>的特征值有两个正数，一个为零.0为最小的特征值.

由于<equation>a - 2 < a < a + 1</equation>，故可知<equation>a - 2 = 0</equation>，即<equation>a = 2</equation>

---


### 行列式

**2025年第15题 | 填空题 | 5分**

<equation>1 5. f (x) = \left| \begin{array}{c c c c} 2 x + 1 & 3 & 2 x + 1 & 1 \\ 2 x & - 3 & 4 x & - 2 \\ 2 x + 1 & 2 & 2 x + 1 & 1 \\ 2 x & - 4 & 4 x & - 2 \end{array} \right|, g (x) = \left| \begin{array}{c c c c} 2 x + 1 & 1 & 2 x + 1 & 3 \\ 5 x + 1 & - 2 & 4 x & - 3 \\ 0 & 1 & 2 x + 1 & 2 \\ 2 x & - 2 & 4 x & - 4 \end{array} \right|</equation>则方程 f(x）=g(x）的不同的根的个数

为___

**解析:**解 由于交换两列，行列式变号，故<equation>- g ( x ) = \left| \begin{array}{c c c c} 2 x + 1 & 3 & 2 x + 1 & 1 \\ 5 x + 1 & - 3 & 4 x & - 2 \\ 0 & 2 & 2 x + 1 & 1 \\ 2 x & - 4 & 4 x & - 2 \end{array} \right|</equation>从而<equation>\begin{aligned} f (x) - g (x) &= \left| \begin{array}{c c c c} 2 x + 1 & 3 & 2 x + 1 & 1 \\ 2 x & - 3 & 4 x & - 2 \\ 2 x + 1 & 2 & 2 x + 1 & 1 \\ 2 x & - 4 & 4 x & - 2  \right| + \left| \begin{array}{c c c c} 2 x + 1 & 3 & 2 x + 1 & 1 \\ 5 x + 1 & - 3 & 4 x & - 2 \\ 0 & 2 & 2 x + 1 & 1 \\ 2 x & - 4 & 4 x & - 2  \right| \\ &= \left| \begin{array}{c c c c} 4 x + 2 & 3 & 2 x + 1 & 1 \\ 7 x + 1 & - 3 & 4 x & - 2 \\ 2 x + 1 & 2 & 2 x + 1 & 1 \\ 4 x & - 4 & 4 x & - 2  \right| \frac {c _ {1} - c _ {3}}{\frac {c _ {2} - 2 c _ {4}}{2}} \left| \begin{array}{c c c c} 2 x + 1 & 1 & 2 x + 1 & 1 \\ 3 x + 1 & 1 & 4 x & - 2 \\ 0 & 0 & 2 x + 1 & 1 \\ 0 & 0 & 4 x & - 2  \right| \\ &= \left| \begin{array}{c c} 2 x + 1 & 1 \\ 3 x + 1 & 1  \right| \cdot \left| \begin{array}{c c} 2 x + 1 & 1 \\ 4 x & - 2  \right| &= (- x) \cdot (- 8 x - 2) = x (8 x + 2). \end{aligned}</equation>因此，方程<equation>f ( x )=g ( x )</equation>即<equation>x ( 8 x+2 )=0</equation>，该方程的根共有2个：<equation>x_{1}=0,x_{2}=-\frac{1}{4}.</equation>

---

**2024年第7题 | 选择题 | 5分 | 答案: B**

7. 设矩阵<equation>A=\left( \begin{array}{c c c} a+1 & b & 3 \\ a & \frac{b}{2} & 1 \\ 1 & 1 & 2 \end{array} \right), M_{ij}</equation>表示 A的 i行 j列元素的余子式，若<equation>|A|=-\frac{1}{2}</equation>且<equation>-M_{21}+M_{22}-M_{23}=0.</equation>则（    ）

A. a=0或<equation>a=-\frac{3}{2}</equation>B. a=0或<equation>a=\frac{3}{2}</equation>C. b=1或<equation>b=-\frac{1}{2}</equation>D. b=-1或<equation>b=\frac{1}{2}</equation>

答案: B

**解析:**解 由<equation>- M_{21}+M_{22}-M_{23}=0</equation>实际上可以得到<equation>A_{21}+A_{22}+A_{23}=0</equation>，故由行列式的按行展开定理可得将矩阵 A的第二行元素全换成1所得矩阵的行列式等于0，即<equation>\left| \begin{array}{c c c} a + 1 & b & 3 \\ 1 & 1 & 1 \\ 1 & 1 & 2 \end{array} \right| \xlongequal {r _ {3} - r _ {2}} \left| \begin{array}{c c c} a + 1 & b & 3 \\ 1 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right| \xlongequal {\text {按 第三 行 展开}} a + 1 - b = 0.</equation>于是，<equation>b=a+1.</equation>由<equation>|A| = -\frac{1}{2}</equation>以及<equation>b=a+1</equation>可得<equation>\left| \begin{array}{c c c} b & b & 3 \\ b - 1 & \frac {b}{2} & 1 \\ 1 & 1 & 2 \end{array} \right| \xlongequal {c _ {1} - c _ {2}} \left| \begin{array}{c c c} 0 & b & 3 \\ \frac {b}{2} - 1 & \frac {b}{2} & 1 \\ 0 & 1 & 2 \end{array} \right| \xlongequal {\text {按 第一 列 展 开}} \left(1 - \frac {b}{2}\right) (2 b - 3) = - \frac {1}{2}.</equation>整理可得<equation>(b - 2)(2b - 3) = 1</equation>，即<equation>2b^{2} - 7b + 5 = 0.</equation>解得<equation>b = 1</equation>或<equation>b = \frac{5}{2}</equation>，从而<equation>a = 0</equation>或<equation>a = \frac{3}{2}</equation>因此，应选B.

---

**2021年第15题 | 填空题 | 5分**

15. 多项式 f(x) =<equation>\left| \begin{array}{c c c c} x & x & 1 & 2 x \\ 1 & x & 2 & - 1 \\ 2 & 1 & x & 1 \\ 2 & - 1 & 1 & x \end{array} \right|</equation>中<equation>x^{3}</equation>项的系数为 ___

**解析:**解 由于所给行列式的元素均为常数或 x的倍数，故根据行列式的定义，要出现<equation>x^{3}</equation>项，必须从不同行、不同列中取出3个含 x的项相乘.

将行列式记为<equation>\det ( a_{ij} ).</equation><equation>\textcircled{1} a_{11}=x</equation>不能取.若取<equation>a_{11}</equation>，则第一行中的 x与 2x不能取.于是，剩下的2个含 x的元素必来自主对角线上的3个 x.无论从<equation>a_{22},a_{33},a_{44}</equation>中取哪两个，第四个元素都只能来自主对角线，从而这种取法最终将得到<equation>x^{4}</equation>，而不是<equation>x^{3}.</equation><equation>\left| \begin{array}{c c c c} \underline {{x}} & x & 1 & 2 x \\ 1 & \underline {{x}} & 2 & - 1 \\ 2 & 1 & \underline {{x}} & 1 \\ 2 & - 1 & 1 & \underline {{x}} \end{array} \right|.</equation><equation>\textcircled{2}</equation>由于<equation>x^{3}</equation>项必来自于不同列的含x元素的乘积，故确定<equation>a_{11}</equation>不取后，x必来自后三列，而第三列中仅<equation>a_{33}=x</equation>，从而必取.

下面分情况讨论.

(1) 若第二列中取<equation>a_{12}=x</equation>，则组合应为<equation>a_{12}a_{21}a_{33}a_{44}</equation>.该组合对应排列2，1，3，4，逆序数为1.于是，所得<equation>x^{3}</equation>项为<equation>(-1)^{1}\cdot 1\cdot x^{3}=-x^{3}.</equation>(2) 若第二列中取<equation>a_{22}=x</equation>，则组合应为<equation>a_{14}a_{22}a_{33}a_{41}</equation>.该组合对应排列4，2，3，1，逆序数为5.于是，所得<equation>x^{3}</equation>项为<equation>(-1)^{5}\cdot 2\cdot 2x^{3}=-4x^{3}.</equation><equation>\left| \begin{array}{c c c c} x & \underline {{x}} & 1 & 2 x \\ 1 & x & 2 & - 1 \\ 2 & 1 & \underline {{x}} & 1 \\ 2 & - 1 & 1 & \underline {{x}} \end{array} \right|, \quad \left| \begin{array}{c c c c} x & x & 1 & 2 x \\ 1 & \underline {{x}} & 2 & - 1 \\ 2 & 1 & \underline {{x}} & 1 \\ 2 & - 1 & 1 & x \end{array} \right|</equation>因此，<equation>f ( x )</equation>的<equation>x^{3}</equation>项为<equation>- x^{3}-4 x^{3}=-5 x^{3}, x^{3}</equation>的系数为-5.

---

**2020年第13题 | 填空题 | 4分**

13. 行列式<equation>\left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a \end{array} \right| = \underline {{\quad}}</equation>

**答案:**<equation>a^{4}-4 a^{2}.</equation>

**解析:**解（法一）利用行列式的性质对所求行列式进行转化.

若 a=0 ，则将第二行加到第一行可得零行，从而行列式为0.

若 a≠0，则<equation>\begin{aligned} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a  \right| \frac {r _ {4} + r _ {3}}{\hline} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 0 & 0 & a & a  \right| \frac {r _ {3} + \frac {1}{a} r _ {1}}{\hline} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ 0 & 1 & a - \frac {1}{a} & \frac {1}{a} \\ 0 & 0 & a & a  \right| \\ \frac {r _ {3} - \frac {1}{a} r _ {2}}{\hline} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ 0 & 0 & a - \frac {2}{a} & \frac {2}{a} \\ 0 & 0 & a & a  \right| &= \left| \begin{array}{c c} a & 0 \\ 0 & a  \right| \cdot \left| \begin{array}{c c} a - \frac {2}{a} & \frac {2}{a} \\ a & a  \right| \\ &= a ^ {2} \left[ \left(a - \frac {2}{a}\right) a - 2 \right] = a ^ {2} \left(a ^ {2} - 4\right) = a ^ {4} - 4 a ^ {2}. \end{aligned}</equation>不论是哪种情况，所求行列式均为<equation>a^{4}-4 a^{2}.</equation>（法二）注意到所求行列式的各行元素之和均为 a，故可将各列均加到第1列，然后计算行列式.<equation>\left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a \end{array} \right| \frac {c _ {1} + c _ {2} + c _ {3} + c _ {4}}{\hline} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ a & a & 1 & - 1 \\ a & 1 & a & 0 \\ a & - 1 & 0 & a \end{array} \right| = a \left| \begin{array}{c c c c} 1 & 0 & - 1 & 1 \\ 1 & a & 1 & - 1 \\ 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a \end{array} \right|</equation><equation>\begin{array}{l} \frac {c _ {3} + c _ {1}}{c _ {4} - c _ {1}} a \left| \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 1 & a & 2 & - 2 \\ 1 & 1 & a + 1 & - 1 \\ 1 & - 1 & 1 & a - 1 \end{array} \right| \frac {c _ {3} + c _ {4}}{c _ {4}} a \left| \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 1 & a & 0 & - 2 \\ 1 & 1 & a & - 1 \\ 1 & - 1 & a & a - 1 \end{array} \right| \\ \frac {\text {按第一行展开}} {= a ^ {4} - 4 a ^ {2}} a \left\{a \left[ a (a - 1) + a \right] - 2 (a + a) \right\} = a \left(a ^ {3} - 4 a\right) \\ \end{array}</equation>

---

**2016年第13题 | 填空题 | 4分**

13. 行列式<equation>\left| \begin{array}{c c c c} \lambda & - 1 & 0 & 0 \\ 0 & \lambda & - 1 & 0 \\ 0 & 0 & \lambda & - 1 \\ 4 & 3 & 2 & \lambda + 1 \end{array} \right| = \underline {{\quad}}</equation>

**答案:**##<equation>\lambda^{4}+\lambda^{3}+2\lambda^{2}+3\lambda+4.</equation>

**解析:**（法一）按第一列展开.<equation>\begin{aligned} \left| \begin{array}{c c c c} \lambda & - 1 & 0 & 0 \\ 0 & \lambda & - 1 & 0 \\ 0 & 0 & \lambda & - 1 \\ 4 & 3 & 2 & \lambda + 1  \right| &= \lambda \left| \begin{array}{c c c} \lambda & - 1 & 0 \\ 0 & \lambda & - 1 \\ 3 & 2 & \lambda + 1  \right| - 4 \left| \begin{array}{c c c} - 1 & 0 & 0 \\ \lambda & - 1 & 0 \\ 0 & \lambda & - 1  \right| \\ &= \lambda \left(\lambda \left| \begin{array}{c c} \lambda & - 1 \\ 2 & \lambda + 1  \right| + 3 \left| \begin{array}{c c} - 1 & 0 \\ \lambda & - 1  \right|\right) - 4 \times (- 1) ^ {3} \\ &= \lambda \left[ \lambda \left(\lambda^ {2} + \lambda + 2\right) + 3 \right] + 4 \\ &= \lambda^ {4} + \lambda^ {3} + 2 \lambda^ {2} + 3 \lambda + 4. \end{aligned}</equation>（法二）利用行列式的性质.<equation>\begin{aligned} \left| \begin{array}{c c c c} \lambda & - 1 & 0 & 0 \\ 0 & \lambda & - 1 & 0 \\ 0 & 0 & \lambda & - 1 \\ 4 & 3 & 2 & \lambda + 1  \right| \frac {c _ {1} + \lambda c _ {2}}{\hline} \left| \begin{array}{c c c c} 0 & - 1 & 0 & 0 \\ \lambda^ {2} & \lambda & - 1 & 0 \\ 0 & 0 & \lambda & - 1 \\ 4 + 3 \lambda & 3 & 2 & \lambda + 1  \right| \\ \frac {c _ {1} + \lambda^ {2} c _ {3}}{\hline} \left| \begin{array}{c c c c} 0 & - 1 & 0 & 0 \\ 0 & \lambda & - 1 & 0 \\ \lambda^ {3} & 0 & \lambda & - 1 \\ 4 + 3 \lambda + 2 \lambda^ {2} & 3 & 2 & \lambda + 1  \right| \\ \frac {c _ {1} + \lambda^ {3} c _ {4}}{\hline} \left| \begin{array}{c c c c} 0 & & - 1 & 0 & 0 \\ 0 & & \lambda & - 1 & 0 \\ 0 & & 0 & \lambda & - 1 \\ 4 + 3 \lambda + 2 \lambda^ {2} + \lambda^ {3} (\lambda + 1) & 3 & 2 & \lambda + 1  \right| \\ &= (- 1) ^ {4 + 1} \left[ 4 + 3 \lambda + 2 \lambda^ {2} + \lambda^ {3} (\lambda + 1) \right] (- 1) ^ {3} \\ &= \lambda^ {4} + \lambda^ {3} + 2 \lambda^ {2} + 3 \lambda + 4. \end{aligned}</equation>

---

**2014年第5题 | 选择题 | 4分 | 答案: B**

5. 行列式<equation>\left| \begin{array}{c c c c} 0 & a & b & 0 \\ a & 0 & 0 & b \\ 0 & c & d & 0 \\ c & 0 & 0 & d \end{array} \right|.</equation>A.<equation>( a d-b c )^{2}</equation>B.<equation>-( a d-b c )^{2}</equation>C.<equation>a^{2} d^{2}-b^{2} c^{2}</equation>D.<equation>b^{2} c^{2}-a^{2} d^{2}</equation>

答案: B

**解析:**解（法一）对原行列式作初等变换.根据行列式的性质，交换两行或两列，所得新行列式为原行列式的负值.<equation>\left| \begin{array}{c c c c} 0 & a & b & 0 \\ a & 0 & 0 & b \\ 0 & c & d & 0 \\ c & 0 & 0 & d \end{array} \right| = - \left| \begin{array}{c c c c} 0 & a & b & 0 \\ 0 & c & d & 0 \\ a & 0 & 0 & b \\ c & 0 & 0 & d \end{array} \right| = \left| \begin{array}{c c c c} a & 0 & b & 0 \\ c & 0 & d & 0 \\ 0 & a & 0 & b \\ 0 & c & 0 & d \end{array} \right| = - \left| \begin{array}{c c c c} a & b & 0 & 0 \\ c & d & 0 & 0 \\ 0 & 0 & a & b \\ 0 & 0 & c & d \end{array} \right| = - (a d - b c) ^ {2}.</equation>应选B.

（法二）按第一行展开.<equation>\left| \begin{array}{c c c c} 0 & a & b & 0 \\ a & 0 & 0 & b \\ 0 & c & d & 0 \\ c & 0 & 0 & d \end{array} \right| = (- a) \left| \begin{array}{c c c} a & 0 & b \\ 0 & d & 0 \\ c & 0 & d \end{array} \right| + b \left| \begin{array}{c c c} a & 0 & b \\ 0 & c & 0 \\ c & 0 & d \end{array} \right| = - a ^ {2} d ^ {2} + a b c d + a b c d - b ^ {2} c ^ {2} = - (a d - b c) ^ {2}.</equation>应选B.

---

**2013年第13题 | 填空题 | 4分**

13. 设<equation>A=(a_{ij})</equation>是3阶非零矩阵，<equation>|A|</equation>为 A的行列式，<equation>A_{ij}</equation>为<equation>a_{ij}</equation>的代数余子式. 若<equation>a_{ij}+A_{ij}=0</equation>（i,j=1,2,3），则<equation>|A|=</equation>___

**解析:**首先，由题设可知<equation>\boldsymbol {A} ^ {*} = \left( \begin{array}{c c c} A _ {1 1} & A _ {2 1} & A _ {3 1} \\ A _ {1 2} & A _ {2 2} & A _ {3 2} \\ A _ {1 3} & A _ {2 3} & A _ {3 3} \end{array} \right) \xlongequal {a _ {i j} + A _ {i j} = 0} \left( \begin{array}{c c c} - a _ {1 1} & - a _ {2 1} & - a _ {3 1} \\ - a _ {1 2} & - a _ {2 2} & - a _ {3 2} \\ - a _ {1 3} & - a _ {2 3} & - a _ {3 3} \end{array} \right) = - \boldsymbol {A} ^ {\mathrm {T}},</equation>故<equation>|\mathbf{A}|^3 = |\mathbf{A}\mathbf{A}^*| = |-\mathbf{A}\mathbf{A}^{\mathrm{T}}| = -|\mathbf{A}|^2.</equation>因此可以得到<equation>|\mathbf{A}| = 0</equation>，或<equation>|\mathbf{A}| = -1.</equation>另一方面，由于<equation>A</equation>为非零矩阵，故不妨假设<equation>a_{11} \neq 0</equation>，则<equation>| \boldsymbol {A} | = a _ {1 1} A _ {1 1} + a _ {1 2} A _ {1 2} + a _ {1 3} A _ {1 3} = - \left(a _ {1 1} ^ {2} + a _ {1 2} ^ {2} + a _ {1 3} ^ {2}\right) < 0.</equation>因此，<equation>|A| = -1.</equation>

---


### 向量


#### 向量组之间的线性表示

**2025年第21题 | 解答题 | 12分**

21. 设矩阵<equation>A = \left( \begin{array}{c c c c c} 1 & -1 & 3 & 0 & -1 \\ -1 & 0 & -2 & -a & -1 \\ 1 & 1 & a & 2 & 3 \end{array} \right)</equation>的秩为2.

I. 求 a的值；

II. 求<equation>A</equation>的列向量组的一个极大线性无关组<equation>\alpha, \beta</equation>，并求矩阵<equation>H</equation>，使得<equation>A = GH</equation>，其中<equation>G = (\alpha ,\beta)</equation>

**答案:**（ I ）<equation>a=1;</equation>（Ⅱ）<equation>A</equation>的前两列<equation>\alpha=\left( \begin{array}{c}1\\ -1\\ 1 \end{array} \right),\beta=\left( \begin{array}{c}-1\\ 0\\ 1 \end{array} \right)</equation>构成A的列向量组的一个极大线性无关组.令<equation>H=</equation><equation>\left( \begin{array}{c c c c}1&0&2&1&1\\ 0&1&-1&1&2 \end{array} \right)</equation>，则<equation>A=GH</equation>，其中<equation>G=(\alpha ,\beta).</equation>

**解析:**解（I）对矩阵A做初等行变换.<equation>\begin{array}{l} A = \left( \begin{array}{c c c c c} 1 & - 1 & 3 & 0 & - 1 \\ - 1 & 0 & - 2 & - a & - 1 \\ 1 & 1 & a & 2 & 3 \end{array} \right) \xrightarrow [ r _ {3} - r _ {1} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c c} 1 & - 1 & 3 & 0 & - 1 \\ 0 & - 1 & 1 & - a & - 2 \\ 0 & 2 & a - 3 & 2 & 4 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c} 1 & - 1 & 3 & 0 & - 1 \\ 0 & - 1 & 1 & - a & - 2 \\ 0 & 0 & a - 1 & 2 - 2 a & 0 \end{array} \right). \\ \end{array}</equation>由上式可得，当且仅当<equation>a = 1</equation>时，<equation>r(A) = 2.</equation>因此，<equation>a = 1</equation>（Ⅱ）由第（I）问可知，<equation>A=\left( \begin{array}{c c c c c} 1 & -1 & 3 & 0 & -1 \\ -1 & 0 & -2 & -1 & -1 \\ 1 & 1 & 1 & 2 & 3 \end{array} \right).</equation>由于<equation>r(A)=2</equation>，故A的列秩为2又因为A的第一列与第二列线性无关，所以A的第一列与第二列构成A的列向量组的一个极大线性无关组，其余列向量均可由该极大线性无关组线性表示.

由第（Ⅰ）问的计算可得<equation>A \rightarrow \left(\begin{array}{c c c c c}1&- 1&3&0&- 1\\0&- 1&1&- 1&- 2\\0&0&0&0&0\end{array}\right)\rightarrow \left(\begin{array}{c c c c c}1&0&2&1&1\\0&1&- 1&1&2\\0&0&0&0&0\end{array}\right).</equation>记矩阵<equation>A = (\alpha ,\beta ,\gamma_1,\gamma_2,\gamma_3) = (A_1,A_2)</equation>，其中<equation>A_{1}</equation>为<equation>A</equation>的前两列<equation>(\alpha ,\beta),A_{2}</equation>为<equation>A</equation>的后三列<equation>(\gamma_{1},\gamma_{2},\gamma_{3})</equation>，则<equation>A</equation>为矩阵方程<equation>A_{1}X = A_{2}</equation>的增广矩阵.由（1）式可得<equation>\gamma_ {1} = 2 \alpha - \beta , \quad \gamma_ {2} = \alpha + \beta , \quad \gamma_ {3} = \alpha + 2 \beta .</equation>于是，<equation>A = \left(\alpha , \beta , \gamma_ {1}, \gamma_ {2}, \gamma_ {3}\right) = \left(\alpha , \beta\right) \left( \begin{array}{c c c c c} 1 & 0 & 2 & 1 & 1 \\ 0 & 1 & - 1 & 1 & 2 \end{array} \right).</equation>令<equation>H = \left( \begin{array}{c c c c c} 1 & 0 & 2 & 1 & 1 \\ 0 & 1 & -1 & 1 & 2 \end{array} \right)</equation>，则<equation>A = GH</equation>，其中<equation>G = (\alpha ,\beta)</equation>.

---

**2023年第7题 | 选择题 | 5分 | 答案: D**

7. 已知向量<equation>\alpha_{1}=\left( \begin{array}{c}1\\ 2\\ 3 \end{array} \right),\alpha_{2}=\left( \begin{array}{c}2\\ 1\\ 1 \end{array} \right),\beta_{1}=\left( \begin{array}{c}2\\ 5\\ 9 \end{array} \right),\beta_{2}=\left( \begin{array}{c}1\\ 0\\ 1 \end{array} \right)</equation>若<equation>\gamma</equation>既可由<equation>\alpha_{1},\alpha_{2}</equation>线性表示，也可由<equation>\beta_{1},\beta_{2}</equation>线性表示，则<equation>\gamma=(\quad)</equation>A. k<equation>\left( \begin{array}{c}3\\ 3\\ 4 \end{array} \right),k \in \mathbf{R}</equation>B. k<equation>\left( \begin{array}{c}3\\ 5\\ 10 \end{array} \right),k \in \mathbf{R}</equation>C. k<equation>\left( \begin{array}{c}-1\\ 1\\ 2 \end{array} \right),k \in \mathbf{R}</equation>D. k<equation>\left( \begin{array}{c}1\\ 5\\ 8 \end{array} \right),k \in \mathbf{R}</equation>

答案: D

**解析:**解 由于<equation>\boldsymbol{\gamma}</equation>既可由<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2}</equation>线性表示，也可由<equation>\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2}</equation>线性表示，故存在<equation>k_{1},k_{2},l_{1},l_{2}</equation>，使得<equation>\boldsymbol{\gamma}=k_{1}\boldsymbol{\alpha}_{1}</equation><equation>+ k_{2}\boldsymbol{\alpha}_{2}=l_{1}\boldsymbol{\beta}_{1}+l_{2}\boldsymbol{\beta}_{2}</equation>.于是，<equation>\left(k_{1},-l_{1},k_{2},-l_{2}\right)^{\mathrm{T}}</equation>是齐次线性方程组<equation>\left(\boldsymbol{\alpha}_{1},\boldsymbol{\beta}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\beta}_{2}\right)\boldsymbol{x}=\mathbf{0}</equation>的解.

记<equation>A=(\alpha_{1},\beta_{1},\alpha_{2},\beta_{2})</equation>，对A作初等行变换.<equation>\begin{array}{l} \boldsymbol {A} = \left( \begin{array}{c c c c} 1 & 2 & 2 & 1 \\ 2 & 5 & 1 & 0 \\ 3 & 9 & 1 & 1 \end{array} \right) \xrightarrow {r _ {2} - 2 r _ {1}} \frac {r _ {2} - 2 r _ {1}}{r _ {3} - 3 r _ {1}} \left( \begin{array}{c c c c} 1 & 2 & 2 & 1 \\ 0 & 1 & - 3 & - 2 \\ 0 & 3 & - 5 & - 2 \end{array} \right) \xrightarrow {r _ {1} - 2 r _ {2} ^ {*}} \left( \begin{array}{c c c c} 1 & 0 & 8 & 5 \\ 0 & 1 & - 3 & - 2 \\ 0 & 0 & 4 & 4 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {* *} \times \frac {1}{4}} \left( \begin{array}{c c c c} 1 & 0 & 8 & 5 \\ 0 & 1 & - 3 & - 2 \\ 0 & 0 & 1 & 1 \end{array} \right) \xrightarrow {r _ {1} ^ {*} - 8 r _ {3} ^ {* * *}} \left( \begin{array}{c c c c} 1 & 0 & 0 & - 3 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 \end{array} \right). \\ \end{array}</equation>（<equation>r_{t}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

取<equation>x_{4}=1</equation>，可得<equation>\boldsymbol{\xi}=(3,-1,-1,1)^{\mathrm{T}}</equation>为该方程组的一个基础解系，从而<equation>(k_{1},-l_{1},k_{2},-l_{2})^{\mathrm{T}}= k(3,-1,-1,1)^{\mathrm{T}}</equation>，其中 k<equation>\in\mathbf{R}.</equation>因此，<equation>\boldsymbol {\gamma} = k _ {1} \boldsymbol {\alpha} _ {1} + k _ {2} \boldsymbol {\alpha} _ {2} = 3 k \binom {1} {2} - k \binom {2} {1} = k \binom {1} {5}, \quad k \in \mathbf {R}.</equation>应选 D.

---

**2022年第7题 | 选择题 | 5分 | 答案: C**

7. 设<equation>\alpha_{1}=(\lambda,1,1)^{\mathrm{T}},\alpha_{2}=(1,\lambda,1)^{\mathrm{T}},\alpha_{3}=(1,1,\lambda)^{\mathrm{T}},\alpha_{4}=(1,\lambda,\lambda^{2})^{\mathrm{T}}</equation>. 若<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>等价，则<equation>\lambda</equation>的取值范围是（    )

A.<equation>\{0,1\}</equation>B.<equation>\{\lambda \mid \lambda \in \mathbf{R},\lambda \neq -2\}</equation>C.<equation>\{\lambda \mid \lambda \in \mathbf{R},\lambda \neq -1,\lambda \neq -2\}</equation>D.<equation>\{\lambda \mid \lambda \in \mathbf{R},\lambda \neq -1\}</equation>

答案: C

**解析:**解（法一）当<equation>\lambda=1</equation>时，<equation>\alpha_{1}=\alpha_{2}=\alpha_{3}=\alpha_{4}=\left( \begin{array}{c}1\\ 1\\ 1 \end{array} \right)</equation>.此时<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>显然等价当<equation>\lambda\neq1</equation>时，考虑矩阵<equation>A=(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4})</equation><equation>\begin{array}{l} A = \left( \begin{array}{c c c c} \lambda & 1 & 1 & 1 \\ 1 & \lambda & 1 & \lambda \\ 1 & 1 & \lambda & \lambda^ {2} \end{array} \right) \rightarrow \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 1 & 1 & \lambda & \lambda^ {2} \\ \lambda & 1 & 1 & 1 \end{array} \right) \xrightarrow {r _ {2} - r _ {1}} \frac {r _ {2} - r _ {1}}{r _ {3} - \lambda r _ {1}} \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 0 & 1 - \lambda & \lambda - 1 & \lambda^ {2} - \lambda \\ 0 & 1 - \lambda^ {2} & 1 - \lambda & 1 - \lambda^ {2} \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} \times \frac {1}{1 - \lambda}} \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 0 & 1 & - 1 & - \lambda \\ 0 & 1 + \lambda & 1 & 1 + \lambda \end{array} \right) \xrightarrow {r _ {3} ^ {* *} - (1 + \lambda) r _ {2} ^ {* *}} \left( \begin{array}{c c c c} 1 & \lambda & 1 & \lambda \\ 0 & 1 & - 1 & - \lambda \\ 0 & 0 & \lambda + 2 & (\lambda + 1) ^ {2} \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

由于 A有2阶非零子式<equation>\left| \begin{array}{cc} \lambda & 1 \\ 1 & \lambda \end{array} \right|</equation>，故<equation>r(A)\geqslant 2</equation>另一方面，因为不存在<equation>\lambda</equation>满足<equation>\lambda +2=(\lambda+1)^{2}=</equation>0，所以<equation>r(A)=3.</equation><equation>r(\alpha_{1},\alpha_{2},\alpha_{3})=3</equation>当且仅当<equation>\lambda\neq-2.</equation><equation>r(\alpha_{1},\alpha_{2},\alpha_{4})=3</equation>当且仅当<equation>\lambda\neq-1.</equation>因此，当<equation>\lambda\neq1</equation>时，<equation>r(A)=r(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4})=r(\alpha_{1},\alpha_{2},\alpha_{3})=r(\alpha_{1},\alpha_{2},\alpha_{4})</equation>当且仅当<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1.</equation>注意到<equation>\lambda=1</equation>也包含在条件<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1</equation>中，故<equation>r(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4})=r(\alpha_{1},\alpha_{2},\alpha_{3})= r(\alpha_{1},\alpha_{2},\alpha_{4})</equation>当且仅当<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1.</equation>综上所述，应选C.

（法二）分别计算<equation>|\alpha_{1},\alpha_{2},\alpha_{3}|</equation>，<equation>|\alpha_{1},\alpha_{2},\alpha_{4}|</equation><equation>\left| \alpha_ {1}, \alpha_ {2}, \alpha_ {3} \right| = \left| \begin{array}{c c c} \lambda & 1 & 1 \\ 1 & \lambda & 1 \\ 1 & 1 & \lambda \end{array} \right| = \left| \begin{array}{c c c} \lambda & 1 - \lambda & 1 - \lambda^ {2} \\ 1 & \lambda - 1 & 1 - \lambda \\ 1 & 0 & 0 \end{array} \right| = (1 - \lambda) ^ {2} (\lambda + 2).</equation><equation>\left| \alpha_ {1}, \alpha_ {2}, \alpha_ {4} \right| = \left| \begin{array}{c c c} \lambda & 1 & 1 \\ 1 & \lambda & \lambda \\ 1 & 1 & \lambda^ {2} \end{array} \right| = \left| \begin{array}{c c c} \lambda & 1 - \lambda & 1 - \lambda^ {3} \\ 1 & \lambda - 1 & \lambda - \lambda^ {2} \\ 1 & 0 & 0 \end{array} \right| = (1 - \lambda) ^ {2} (1 + \lambda) ^ {2}.</equation>当<equation>\lambda\neq1,-2,-1</equation>时，<equation>|\alpha_{1},\alpha_{2},\alpha_{3}|</equation>与<equation>|\alpha_{1},\alpha_{2},\alpha_{4}|</equation>均不为0.此时，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>和<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>均为3维列向量组的极大无关组，从而等价.

当<equation>\lambda=1</equation>时，<equation>\alpha_{1}=\alpha_{2}=\alpha_{3}=\alpha_{4}=\left( \begin{array}{c}1\\ 1\\ 1 \end{array} \right).</equation>此时<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>显然等价.

当<equation>\lambda=-2</equation>或<equation>\lambda=-1</equation>时，<equation>|\alpha_{1},\alpha_{2},\alpha_{3}| \neq |\alpha_{1},\alpha_{2},\alpha_{4}|</equation>，且其中一个为0，另一个不为0，说明两向量组的秩不相等，从而不等价.

综上所述，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>与<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>等价当且仅当<equation>\lambda\neq-2</equation>且<equation>\lambda\neq-1.</equation>应选C.

---

**2019年第20题 | 解答题 | 11分**

20. (本题满分11分)<equation>\text {已 知 向 量 组 I}: \alpha_ {1} = \left( \begin{array}{c} 1 \\ 1 \\ 4 \end{array} \right), \alpha_ {2} = \left( \begin{array}{c} 1 \\ 0 \\ 4 \end{array} \right), \alpha_ {3} = \left( \begin{array}{c} 1 \\ 2 \\ a ^ {2} + 3 \end{array} \right) \text {与 II}: \beta_ {1} = \left( \begin{array}{c} 1 \\ 1 \\ a + 3 \end{array} \right), \beta_ {2} = \left( \begin{array}{c} 0 \\ 2 \\ 1 - a \end{array} \right), \beta_ {3} = \left( \begin{array}{c} 1 \\ 3 \\ a ^ {2} + 3 \end{array} \right).</equation>若向

量组 I 与 II 等价，求<equation>a</equation>的取值，并将<equation>\beta_{3}</equation>用<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性表示.

**答案:**当 a≠-1时，向量组Ⅰ与向量组Ⅱ等价.当 a=1时，<equation>\beta_{3}=(3-2k)\alpha_{1}+(-2+k)\alpha_{2}+ k\alpha_{3}</equation>，其中k为任意常数；当 a≠±1时，<equation>\beta_{3}=\alpha_{1}-\alpha_{2}+\alpha_{3}.</equation>

**解析:**解记<equation>A=(\alpha_{1},\alpha_{2},\alpha_{3}),B=(\beta_{1},\beta_{2},\beta_{3})</equation>，则由向量组Ⅰ与向量组Ⅱ等价可知<equation>r(A)=r(B)</equation><equation>= r(A,B).</equation>对（A,B）作初等行变换.<equation>\begin{array}{l} (A, B) = \left( \begin{array}{c c c c c c} 1 & 1 & 1 & 1 & 0 & 1 \\ 1 & 0 & 2 & 1 & 2 & 3 \\ 4 & 4 & a ^ {2} + 3 & a + 3 & 1 - a & a ^ {2} + 3 \end{array} \right) \\ \xrightarrow {r _ {2} - r _ {1}} \frac {1}{r _ {3} - 4 r _ {1}} \left( \begin{array}{c c c c c c} 1 & 1 & 1 & 1 & 0 & 1 \\ 0 & - 1 & 1 & 0 & 2 & 2 \\ 0 & 0 & a ^ {2} - 1 & a - 1 & 1 - a & a ^ {2} - 1 \end{array} \right). \\ \end{array}</equation>由上式可知<equation>r(A)\geqslant 2</equation>，故<equation>r(A) = 2</equation>或<equation>r(A) = 3.</equation>当<equation>a^{2}-1=0</equation>时，<equation>a=1</equation>或<equation>a=-1</equation><equation>r(A)=2</equation>.又由于当<equation>a=-1</equation>时，<equation>r(A,B)=3</equation>，故<equation>a=-1</equation>不符合题意，而当<equation>a=1</equation>时，<equation>r(A)=r(B)=r(A,B)=2</equation>，此时向量组 I与向量组Ⅱ等价.

当 a = 1时，<equation>\left(A, \boldsymbol {\beta} _ {3}\right)\rightarrow \left(\begin{array}{c c c c}1&1&1&1\\0&- 1&1&2\\0&0&0&0\end{array}\right) \xrightarrow {r _ {2} \times (- 1)} \left(\begin{array}{c c c c}1&1&1&1\\0&1&- 1&- 2\\0&0&0&0\end{array}\right) \xrightarrow {r _ {1} - r _ {2} ^ {*}} \left(\begin{array}{c c c c}1&0&2&3\\0&1&- 1&- 2\\0&0&0&0\end{array}\right).</equation>取<equation>x_{3}</equation>为自由变元，令<equation>x_{3}=1</equation>，可得<equation>(-2,1,1)^{\mathrm{T}}</equation>为<equation>A x=0</equation>的一个基础解系.又因为<equation>(3,-2,0)^{\mathrm{T}}</equation>为<equation>A x=\beta_{3}</equation>的一个特解，所以<equation>A x=\beta_{3}</equation>的通解为<equation>k(-2,1,1)^{\mathrm{T}}+(3,-2,0)^{\mathrm{T}}</equation>其中k为任意常数因此，<equation>\boldsymbol {\beta} _ {3} = (3 - 2 k) \boldsymbol {\alpha} _ {1} + (- 2 + k) \boldsymbol {\alpha} _ {2} + k \boldsymbol {\alpha} _ {3},</equation>其中 k为任意常数.

当 a<equation>\neq\pm1</equation>时，<equation>a^{2}-1\neq0,r(A)=r(B)=r(A,B)=3</equation>，向量组Ⅰ与向量组Ⅱ等价，且它们相互之间的线性表示唯一.<equation>\left(A, \boldsymbol {\beta} _ {3}\right)\rightarrow \left(\begin{array}{c c c c}1&1&1&1\\0&- 1&1&2\\0&0&1&1\end{array}\right) \xrightarrow [ r _ {1} - r _ {2} ^ {*} ]{r _ {2} \times (- 1)} \left(\begin{array}{c c c c}1&0&2&3\\0&1&- 1&- 2\\0&0&1&1\end{array}\right) \xrightarrow [ r _ {2} ^ {*} + r _ {3} ]{r _ {1} ^ {*} - 2 r _ {3}} \left(\begin{array}{c c c c}1&0&0&1\\0&1&0&- 1\\0&0&1&1\end{array}\right).</equation>因此，<equation>A x=\beta_{3}</equation>的唯一解为<equation>(1,-1,1)^{\mathrm{T}}.</equation><equation>\boldsymbol {\beta} _ {3} = \boldsymbol {\alpha} _ {1} - \boldsymbol {\alpha} _ {2} + \boldsymbol {\alpha} _ {3}.</equation>综上所述，当<equation>a\neq -1</equation>时，向量组 I与向量组Ⅱ等价。当<equation>a = 1</equation>时，<equation>\beta_{3} = (3 - 2k)\alpha_{1} + (-2 + k)\alpha_{2}</equation><equation>+ k\alpha_{3}</equation>，其中<equation>k</equation>为任意常数；当<equation>a\neq \pm 1</equation>时，<equation>\beta_{3} = \alpha_{1} - \alpha_{2} + \alpha_{3}</equation>.

---

**2013年第5题 | 选择题 | 4分 | 答案: B**

5. 设 A,B,C均为 n阶矩阵. 若 AB=C，且 B可逆，则（    ）

A. 矩阵 C的行向量组与矩阵 A的行向量组等价

B. 矩阵 C的列向量组与矩阵 A的列向量组等价

C. 矩阵 C的行向量组与矩阵 B的行向量组等价

D. 矩阵 C的列向量组与矩阵 B的列向量组等价

答案: B

**解析:**我们证明 C的列向量组与 A的列向量组能相互线性表示.

不妨设<equation>A = \left(\alpha_{1},\alpha_{2},\dots ,\alpha_{n}\right),C = \left(\gamma_{1},\gamma_{2},\dots ,\gamma_{n}\right),B = \left(b_{ij}\right)_{n\times n}</equation>，则<equation>\boldsymbol {A B} = \left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\alpha} _ {2}, \dots , \boldsymbol {\alpha} _ {n}\right) \left(b _ {i j}\right) _ {n \times n} = \boldsymbol {C} = \left(\boldsymbol {\gamma} _ {1}, \boldsymbol {\gamma} _ {2}, \dots , \boldsymbol {\gamma} _ {n}\right),</equation><equation>\left\{ \begin{array}{l} \boldsymbol {\gamma} _ {1} = b _ {1 1} \boldsymbol {\alpha} _ {1} + b _ {2 1} \boldsymbol {\alpha} _ {2} + \dots + b _ {n 1} \boldsymbol {\alpha} _ {n}, \\ \boldsymbol {\gamma} _ {2} = b _ {1 2} \boldsymbol {\alpha} _ {1} + b _ {2 2} \boldsymbol {\alpha} _ {2} + \dots + b _ {n 2} \boldsymbol {\alpha} _ {n}, \\ \dots , \\ \boldsymbol {\gamma} _ {n} = b _ {1 n} \boldsymbol {\alpha} _ {1} + b _ {2 n} \boldsymbol {\alpha} _ {2} + \dots + b _ {n n} \boldsymbol {\alpha} _ {n}. \end{array} \right.</equation>因此，C的列向量组<equation>\left( \gamma_{1},\gamma_{2},\dots,\gamma_{n}\right)</equation>能由A的列向量组<equation>\left( \alpha_{1},\alpha_{2},\dots,\alpha_{n}\right)</equation>线性表示。同理，由于B可逆，故A的列向量组也能由C的列向量组线性表示.应选B.

下面我们说明选项 A、C、D不正确.

选项A：令<equation>A=\left( \begin{array}{cc}1&1\\ 0&0 \end{array} \right), B=\left( \begin{array}{cc}1&1\\ 0&1 \end{array} \right)</equation>，则<equation>C=AB=\left( \begin{array}{cc}1&2\\ 0&0 \end{array} \right).</equation>但A的行向量组<equation>\{(1,1),(0,0)\}</equation>与C的行向量组<equation>\{(1,2),(0,0)\}</equation>不等价.

选项C、D：取B为单位矩阵E，C为一个非满秩矩阵.于是 A=C. B的行（列）向量组线性无关， C的行（列）向量组线性相关，因此不等价.

---

**2011年第20题 | 解答题 | 11分**


设向量组<equation>\alpha_{1}=(1,0,1)^{\mathrm{T}},\alpha_{2}=(0,1,1)^{\mathrm{T}},\alpha_{3}=(1,3,5)^{\mathrm{T}}</equation>不能由向量组<equation>\beta_{1}=(1,1,1)^{\mathrm{T}},\beta_{2}=(1,2,3)^{\mathrm{T}},\beta_{3}=(3,4,a)^{\mathrm{T}}</equation>线性表示.

I. 求 a的值；

II. 将<equation>\beta_{1},\beta_{2},\beta_{3}</equation>用<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性表示.

**答案:**(20) （I）<equation>a=5;</equation>（Ⅱ）<equation>\boldsymbol{\beta}_{1}=2\boldsymbol{\alpha}_{1}+4\boldsymbol{\alpha}_{2}-\boldsymbol{\alpha}_{3},\boldsymbol{\beta}_{2}=\boldsymbol{\alpha}_{1}+2\boldsymbol{\alpha}_{2},\boldsymbol{\beta}_{3}=5\boldsymbol{\alpha}_{1}+10\boldsymbol{\alpha}_{2}-2\boldsymbol{\alpha}_{3}.</equation>

**解析:**解（I）记<equation>A=(\alpha_{1},\alpha_{2},\alpha_{3})</equation><equation>B=(\beta_{1},\beta_{2},\beta_{3})</equation><equation>A,B</equation>的列向量组分别记为<equation>A,B.</equation>首先，<equation>|A| = \left| \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 1 & 1 & 5 \end{array} \right| = 1</equation>，故<equation>r(A) = 3</equation>，A满秩.

由于向量组 B不能线性表示 A，故<equation>r(\mathbf{B})<3</equation>；否则 B也满秩，从而 B能线性表示 A，矛盾.

由于<equation>r(\boldsymbol{B}) < 3</equation>，故<equation>| \boldsymbol {B} | = \left| \begin{array}{c c c} 1 & 1 & 3 \\ 1 & 2 & 4 \\ 1 & 3 & a \end{array} \right| \frac {c _ {2} - c _ {1}}{c _ {3} - 3 c _ {1}} \left| \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 1 \\ 1 & 2 & a - 3 \end{array} \right| = a - 5 = 0.</equation>因此，<equation>a = 5</equation>（Ⅱ）（法一）求B用A的线性表示的系数，相当于求<equation>A X=B</equation>的解. X的列向量的坐标为线性表示的系数，即<equation>\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)\left(x_{1i},x_{2i},x_{3i}\right)^{\mathrm{T}}=\boldsymbol{\beta}_{i}(i=1,2,3).</equation><equation>\begin{array}{l} (\boldsymbol {A}, \boldsymbol {B}) = \left( \begin{array}{c c c c c c} 1 & 0 & 1 & 1 & 1 & 3 \\ 0 & 1 & 3 & 1 & 2 & 4 \\ 1 & 1 & 5 & 1 & 3 & 5 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c c c c} 1 & 0 & 1 & 1 & 1 & 3 \\ 0 & 1 & 3 & 1 & 2 & 4 \\ 0 & 1 & 4 & 0 & 2 & 2 \end{array} \right) \\ \xrightarrow {r _ {3} ^ {*} - r _ {2}} \left( \begin{array}{c c c c c c} 1 & 0 & 1 & 1 & 1 & 3 \\ 0 & 1 & 3 & 1 & 2 & 4 \\ 0 & 0 & 1 & - 1 & 0 & - 2 \end{array} \right) \xrightarrow {r _ {1} - r _ {3} ^ {* *}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 2 & 1 & 5 \\ 0 & 1 & 0 & 4 & 2 & 1 0 \\ 0 & 0 & 1 & - 1 & 0 & - 2 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每做一次初等行变换，加一个*.）

因此，<equation>Ax = \beta_{1}</equation>的解为<equation>(2,4,-1)^{\mathrm{T}},\beta_{1} = 2\alpha_{1} + 4\alpha_{2} - \alpha_{3};Ax = \beta_{2}</equation>的解为<equation>(1,2,0)^{\mathrm{T}},\beta_{2} = \alpha_{1} + 2\alpha_{2};Ax = \beta_{3}</equation>的解为<equation>(5,10,-2)^{\mathrm{T}},\beta_{3} = 5\alpha_{1} + 10\alpha_{2} - 2\alpha_{3}.</equation>（法二）用克拉默法则分别求<equation>A x=\beta_{1},</equation><equation>A x=\beta_{2},</equation><equation>A x=\beta_{3}</equation>的解. x的分量为线性表示的系数，即<equation>\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)\left(x_{1},x_{2},x_{3}\right)^{\mathrm{T}}=\beta_{i}(i=1,2,3).</equation>首先，根据第（I）问可得<equation>|A| = 1.</equation>由克拉默法则知，<equation>Ax = \beta_{1}</equation>的解为<equation>x _ {1} = \left| \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 3 \\ 1 & 1 & 5 \end{array} \right| = 2, \quad x _ {2} = \left| \begin{array}{c c c} 1 & 1 & 1 \\ 0 & 1 & 3 \\ 1 & 1 & 5 \end{array} \right| = 4, \quad x _ {3} = \left| \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 1 \end{array} \right| = - 1.</equation>因此，<equation>\pmb{\beta}_{1} = 2\pmb{\alpha}_{1} + 4\pmb{\alpha}_{2} - \pmb{\alpha}_{3}</equation>. 同理可得<equation>\pmb{\beta}_{2} = \pmb{\alpha}_{1} + 2\pmb{\alpha}_{2}, \pmb{\beta}_{3} = 5\pmb{\alpha}_{1} + 10\pmb{\alpha}_{2} - 2\pmb{\alpha}_{3}</equation>.

---

**2010年第5题 | 选择题 | 4分 | 答案: A**

5. 设向量组 I:<equation>\alpha_{1},\alpha_{2},\cdots,\alpha_{r}</equation>可由向量组 II:<equation>\beta_{1},\beta_{2},\cdots,\beta_{s}</equation>线性表示.下列命题正确的是（    ）

A. 若向量组 I 线性无关，则<equation>r\leqslant s</equation>B. 若向量组 I 线性相关，则<equation>r>s</equation>C. 若向量组 II 线性无关，则<equation>r\leqslant s</equation>D. 若向量组 II 线性相关，则<equation>r>s</equation>

答案: A

**解析:**解 由于向量组 I 能被向量组Ⅱ线性表示，故<equation>r_{\mathrm{I}} \leqslant r_{\mathrm{II}}</equation>.又由题设，有<equation>r_{\mathrm{I}} \leqslant r, r_{\mathrm{II}} \leqslant s.</equation>若向量组 I 线性无关，则<equation>r_{\mathrm{I}}=r</equation>，从而有<equation>r = r _ {\mathrm {I}} \leqslant r _ {\mathrm {I I}} \leqslant s,</equation>即<equation>r\leqslant s.</equation>应选A.

下面我们说明选项B、C、D不正确.

考虑 I = {<equation>\left( \begin{array}{c} 1 \\ 0 \end{array} \right), \left( \begin{array}{c} 2 \\ 0 \end{array} \right)</equation>，Ⅱ = {<equation>\left( \begin{array}{c} 1 \\ 0 \end{array} \right), \left( \begin{array}{c} 0 \\ 1 \end{array} \right), \left( \begin{array}{c} 2 \\ 0 \end{array} \right)</equation>}.Ⅱ能表示 I，且向量组 I，Ⅱ均线性相关，但 2 = r < s = 3.选项B、D不正确.

考虑 I =<equation>\left\{\begin{array}{l l}1\\0\end{array}\right.,\left(\begin{array}{l}2\\0\end{array}\right.,\left(\begin{array}{l}3\\0\end{array}\right)</equation>，Ⅱ<equation>= \left\{\begin{array}{l l}1\\0\end{array}\right.,\left(\begin{array}{l}0\\1\end{array}\right)</equation>.Ⅱ能表示Ⅰ，且向量组Ⅱ线性无关，但<equation>3=r></equation>s=2.选项C不正确.

---


#### 向量组的线性相关性

**2014年第6题 | 选择题 | 4分 | 答案: A**

6. 设<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>均为3维向量，则对任意常数 k,l，向量组<equation>\alpha_{1}+k\alpha_{3},\alpha_{2}+l\alpha_{3}</equation>线性无关是向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关的（    ）

A. 必要非充分条件 B. 充分非必要条件

C. 充分必要条件 D. 既非充分也非必要条件

答案: A

**解析:**解<equation>(\alpha_{1} + k\alpha_{3},\alpha_{2} + l\alpha_{3}) = (\alpha_{1},\alpha_{2},\alpha_{3})\left( \begin{array}{c c}1 & 0\\ 0 & 1\\ k & l \end{array} \right).</equation>若向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关，则<equation>r \left(\left(\boldsymbol {\alpha} _ {1} + k \boldsymbol {\alpha} _ {3}, \boldsymbol {\alpha} _ {2} + l \boldsymbol {\alpha} _ {3}\right)\right) = r \left(\left( \begin{array}{c c} 1 & 0 \\ 0 & 1 \\ k & l \end{array} \right)\right) = 2.</equation>因此，<equation>\alpha_{1} + k\alpha_{3},\alpha_{2} + l\alpha_{3}</equation>线性无关.

令<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2}</equation>为线性无关的两个向量，<equation>\boldsymbol{\alpha}_{3}=\mathbf{0}</equation>，则对任意常数 k，l，向量组<equation>\boldsymbol{\alpha}_{1}+k\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{2}+l\boldsymbol{\alpha}_{3}</equation>线性无关，但向量组<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性相关.

综上所述，对任意常数 k，l，向量组<equation>\boldsymbol{\alpha}_{1}+k\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{2}+l\boldsymbol{\alpha}_{3}</equation>线性无关是向量组<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性无关的必要非充分条件.应选A.

---

**2012年第5题 | 选择题 | 4分 | 答案: C**

5. 设<equation>\alpha_{1}=\left( \begin{array}{c}0\\ 0\\ c_{1}\end{array} \right),\alpha_{2}=\left( \begin{array}{c}0\\ 1\\ c_{2}\end{array} \right),\alpha_{3}=\left( \begin{array}{c}1\\ -1\\ c_{3}\end{array} \right),\alpha_{4}=\left( \begin{array}{c}-1\\ 1\\ c_{4}\end{array} \right),</equation>其中<equation>c_{1},c_{2},c_{3},c_{4}</equation>为任意常数，则下列向量组线性相关

为（    ）

A.<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>B.<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>C.<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>D.<equation>\alpha_{2},\alpha_{3},\alpha_{4}</equation>

答案: C

**解析:**解（法一）由题设可得，<equation>\boldsymbol{\alpha}_{3}+\boldsymbol{\alpha}_{4}=\left( \begin{array}{c}0\\ 0\\ c_{3}+c_{4} \end{array} \right)</equation><equation>\boldsymbol{\alpha}_{1}=\left( \begin{array}{c}0\\ 0\\ c_{1} \end{array} \right).</equation>当<equation>c_{3} + c_{4}\neq 0</equation>时，<equation>\alpha_{1} = \frac{c_{1}}{c_{3} + c_{4}} \left(\alpha_{3} + \alpha_{4}\right)</equation>，<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>线性相关；当<equation>c_{3} + c_{4} = 0</equation>时，<equation>\alpha_{3} + \alpha_{4} = 0</equation>，<equation>\alpha_{3},\alpha_{4}</equation>线性相关.从而<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>线性相关.

综上所述，<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}</equation>线性相关，应选C.

（法二）由于<equation>n</equation>个<equation>n</equation>维列向量<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{n}</equation>线性相关等价于<equation>|\alpha_{1},\alpha_{2},\dots ,\alpha_{n}| = 0</equation>，而<equation>\left| \alpha_ {1}, \alpha_ {3}, \alpha_ {4} \right| = \left| \begin{array}{c c c} 0 & 1 & - 1 \\ 0 & - 1 & 1 \\ c _ {1} & c _ {3} & c _ {4} \end{array} \right| = c _ {1} \left| \begin{array}{c c} 1 & - 1 \\ - 1 & 1 \end{array} \right| = 0,</equation>故<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}</equation>线性相关.应选C.

同理可计算其他选项中的3个向量组成的矩阵的行列式，可知它们均不恒为零.

---

**2009年第20题 | 解答题 | 11分**

20. (本题满分11分)<equation>\text {设} \boldsymbol {A} = \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ - 1 & 1 & 1 \\ 0 & - 4 & - 2 \end{array} \right), \boldsymbol {\xi} _ {1} = \left( \begin{array}{c} - 1 \\ 1 \\ - 2 \end{array} \right).</equation>I. 求满足<equation>A\xi_{2}=\xi_{1}, A^{2}\xi_{3}=\xi_{1}</equation>的所有向量<equation>\xi_{2},\xi_{3}</equation>；

II. 对第一问中的任意向量<equation>\xi_{2},\xi_{3}</equation>，证明<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

**答案:**（20）（I）满足<equation>A\xi_{2}=\xi_{1}</equation>的所有向量为<equation>\xi_{2}=k_{1}(1,-1,2)^{\mathrm{T}}+(0,0,1)^{\mathrm{T}}</equation>，其中<equation>k_{1}</equation>为任意常数；满足<equation>A^{2}\xi_{3}=\xi_{1}</equation>的所有向量<equation>\xi_{3}=k_{2}(1,-1,0)^{\mathrm{T}}+k_{3}(0,0,1)^{\mathrm{T}}+\left(-\frac{1}{2},0,0\right)^{\mathrm{T}}</equation>，其中<equation>k_{2},k_{3}</equation>为任意常数.

（Ⅱ）证明略.

**解析:**解（I）解<equation>A x=\xi_{1}</equation>，这是一个非齐次线性方程组.<equation>\left(\boldsymbol {A}, \boldsymbol {\xi} _ {1}\right) = \left( \begin{array}{c c c c} 1 & - 1 & - 1 & - 1 \\ - 1 & 1 & 1 & 1 \\ 0 & - 4 & - 2 & - 2 \end{array} \right) \xrightarrow [ r _ {2} ^ {*} \leftrightarrow r _ {3} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c} 1 & - 1 & - 1 & - 1 \\ 0 & - 4 & - 2 & - 2 \\ 0 & 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {1} + r _ {2} ^ {* * *} ]{r _ {2} ^ {* *} \times \left(- \frac {1}{2}\right)} \left( \begin{array}{c c c c} 1 & 1 & 0 & 0 \\ 0 & 2 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{array} \right).</equation>(<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每做一次初等行变换，加一个*.）

于是<equation>r(A) = r(A, \xi_1) = 2.Ax = \xi_1</equation>有无穷多解.其对应的齐次方程组等价于<equation>\left\{ \begin{array}{l}x_{1} + x_{2} = 0,\\ 2x_{2} + x_{3} = 0, \end{array} \right.</equation>故可取<equation>(1, - 1, 2)^{\mathrm{T}}</equation>为该方程组的一个基础解系.另外，<equation>\left\{ \begin{array}{l}x_{1} + x_{2} = 0,\\ 2x_{2} + x_{3} = 1 \end{array} \right.</equation>的一个特解为<equation>(0,0,1)^{\mathrm{T}}.</equation>因此，<equation>Ax = \xi_{1}</equation>的通解为<equation>\xi_{2} = k_{1}(1, -1, 2)^{\mathrm{T}} + (0, 0, 1)^{\mathrm{T}}</equation>，其中<equation>k_{1}</equation>为任意常数.<equation>\left(\boldsymbol {A} ^ {2}, \boldsymbol {\xi} _ {1}\right) = \left( \begin{array}{c c c c} 2 & 2 & 0 & - 1 \\ - 2 & - 2 & 0 & 1 \\ 4 & 4 & 0 & - 2 \end{array} \right) \xrightarrow [ r _ {3} - 2 r _ {1} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c} 2 & 2 & 0 & - 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{array} \right).</equation>于是<equation>r(A^{2}) = r(A^{2},\xi_{1}) = 1.A^{2}x = \xi_{1}</equation>有无穷多解.其对应的齐次方程组等价于<equation>2(x_{1} + x_{2}) = 0</equation>，故可取<equation>(1, - 1,0)^{\mathrm{T}}</equation>和<equation>(0,0,1)^{\mathrm{T}}</equation>为该方程组的一个基础解系.另外，<equation>2(x_{1} + x_{2}) = -1</equation>的一个特解为<equation>\left(-\frac{1}{2},0;0\right)^{\mathrm{T}}.</equation>因此，<equation>A^{2}x = \xi_{1}</equation>的通解为<equation>\xi_{3} = k_{2}(1, - 1,0)^{\mathrm{T}} + k_{3}(0,0,1)^{\mathrm{T}} + \left(-\frac{1}{2},0,0\right)^{\mathrm{T}}</equation>，其中<equation>k_{2},k_{3}</equation>为任意常数.

（Ⅱ）（法一）通过计算可知，<equation>\boldsymbol {A} \boldsymbol {\xi} _ {1} = \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ - 1 & 1 & 1 \\ 0 & - 4 & - 2 \end{array} \right) \left( \begin{array}{c} - 1 \\ 1 \\ - 2 \end{array} \right) = \left( \begin{array}{c} 0 \\ 0 \\ 0 \end{array} \right).</equation>从而<equation>A^{3}\xi_{3} = A^{2}\xi_{2} = A\xi_{1} = 0.</equation>我们可以利用该性质推出<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

不妨设<equation>a\boldsymbol{\xi}_1 + b\boldsymbol{\xi}_2 + c\boldsymbol{\xi}_3 = \mathbf{0}</equation>. 该等式两端同时左乘<equation>A^2</equation><equation>a A ^ {2} \xi_ {1} + b A ^ {2} \xi_ {2} + c A ^ {2} \xi_ {3} = c A ^ {2} \xi_ {3} = c \xi_ {1} = 0.</equation>由于<equation>\boldsymbol{\xi}_{1}</equation>为非零向量，故<equation>c=0.</equation>于是<equation>a\boldsymbol{\xi}_{1}+b\boldsymbol{\xi}_{2}=\mathbf{0}.</equation>再在<equation>a\boldsymbol{\xi}_{1}+b\boldsymbol{\xi}_{2}=\mathbf{0}</equation>两端同时左乘 A，得<equation>aA\boldsymbol{\xi}_{1}+bA\boldsymbol{\xi}_{2}=bA\boldsymbol{\xi}_{2}=b\boldsymbol{\xi}_{1}=\mathbf{0}.</equation>同理得<equation>b = 0</equation>. 由于<equation>b = c = 0</equation>，故<equation>a\boldsymbol{\xi}_1 = \mathbf{0}</equation>. 从而<equation>a = 0</equation>.

因此，<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

（法二）由第（I）问，我们知道了<equation>\xi_{1},\xi_{2},\xi_{3}</equation>的表达式，从而我们可以通过计算行列式<equation>|\xi_{1},\xi_{2},\xi_{3}|</equation>来说明<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.<equation>\begin{array}{l} \left| \xi_ {1}, \xi_ {2}, \xi_ {3} \right| = \left| \begin{array}{c c c} - 1 & k _ {1} & k _ {2} - \frac {1}{2} \\ 1 & - k _ {1} & - k _ {2} \\ - 2 & 2 k _ {1} + 1 & k _ {3} \end{array} \right| \xlongequal {r _ {1} + r _ {2}} \left| \begin{array}{c c c} 0 & 0 & - \frac {1}{2} \\ 1 & - k _ {1} & - k _ {2} \\ - 2 & 2 k _ {1} + 1 & k _ {3} \end{array} \right| \\ \underline {{\underline {{\text {按 第一 行 展开}}}}} \left(- \frac {1}{2}\right) \left| \begin{array}{c c} 1 & - k _ {1} \\ - 2 & 2 k _ {1} + 1 \end{array} \right| = - \frac {1}{2} \neq 0. \\ \end{array}</equation>因此，<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

---


### 矩阵


#### 矩阵的运算与变换

**2024年第6题 | 选择题 | 5分 | 答案: C**

6. 设 A为3阶矩阵，<equation>P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right)</equation>，若<equation>P^{\mathrm{T}} A P^{2}=\left( \begin{array}{c c c} a+2 c & 0 & c \\ 0 & b & 0 \\ 2 c & 0 & c \end{array} \right)</equation>，则 A=（    )

A.<equation>\left( \begin{array}{c c c} c & 0 & 0 \\ 0 & a & 0 \\ 0 & 0 & b \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c} b & 0 & 0 \\ 0 & c & 0 \\ 0 & 0 & a \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c} a & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & c \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} c & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & a \end{array} \right)</equation>

答案: C

**解析:**）由于<equation>P = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right)</equation>，故<equation>\boldsymbol {P} ^ {- 1} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ - 1 & 0 & 1 \end{array} \right), \quad \boldsymbol {P} ^ {\mathrm {T}} = \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right), \quad \left(\boldsymbol {P} ^ {\mathrm {T}}\right) ^ {- 1} = \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>进一步可得，<equation>\begin{aligned} \boldsymbol {A} &= \left(\boldsymbol {P} ^ {\mathrm {T}}\right) ^ {- 1} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} ^ {2} \left(\boldsymbol {P} ^ {2}\right) ^ {- 1} = \left(\boldsymbol {P} ^ {\mathrm {T}}\right) ^ {- 1} \boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} ^ {2} \left(\boldsymbol {P} ^ {- 1}\right) ^ {2} \\ &= \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1  \right) \left( \begin{array}{c c c} a + 2 c & 0 & c \\ 0 & b & 0 \\ 2 c & 0 & c  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ - 1 & 0 & 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ - 1 & 0 & 1  \right) \\ &= \left( \begin{array}{c c c} a & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & c  \right). \end{aligned}</equation>因此，应选C.

---

**2022年第15题 | 填空题 | 5分**

15. 设 A为3阶矩阵，交换 A的第2行和第3行，再将第2列的-1倍加到第1列，得到矩阵<equation>A^{-1}</equation>的迹<equation>\operatorname{tr}(A^{-1}) =</equation>___

**答案:**-1.

**解析:**解 交换第2行和第3行对应左乘初等矩阵<equation>P_{1}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{array} \right)</equation>，将第2列的-1倍加到第1列对应右乘初等矩阵<equation>P_{2}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>.记<equation>B=\left( \begin{array}{c c c} -2 & 1 & -1 \\ 1 & -1 & 0 \\ -1 & 0 & 0 \end{array} \right)</equation>.于是，<equation>P_{1}AP_{2}=B</equation>，从而<equation>A= P_{1}^{-1}BP_{2}^{-1}</equation>.由此可得，<equation>A^{-1}=P_{2}B^{-1}P_{1}.</equation>下面利用初等行变换计算<equation>B^{-1}.</equation><equation>\begin{array}{l} (B, E) = \left( \begin{array}{c c c c c c} - 2 & 1 & - 1 & 1 & 0 & 0 \\ 1 & - 1 & 0 & 0 & 1 & 0 \\ - 1 & 0 & 0 & 0 & 0 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 0 & 0 & - 1 \\ 1 & - 1 & 0 & 0 & 1 & 0 \\ - 2 & 1 & - 1 & 1 & 0 & 0 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 0 & 0 & - 1 \\ 0 & - 1 & 0 & 0 & 1 & 1 \\ 0 & 1 & - 1 & 1 & 0 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 0 & 0 & - 1 \\ 0 & - 1 & 0 & 0 & 1 & 1 \\ 0 & 0 & - 1 & 1 & 1 & - 1 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 0 & 0 & - 1 \\ 0 & 1 & 0 & 0 & - 1 & - 1 \\ 0 & 0 & 1 & - 1 & - 1 & 1 \end{array} \right). \\ \end{array}</equation>于是，<equation>B^{-1}=\left( \begin{array}{c c c} 0 & 0 & -1 \\ 0 & -1 & -1 \\ -1 & -1 & 1 \end{array} \right).</equation>因此，<equation>\boldsymbol {A} ^ {- 1} = \boldsymbol {P} _ {2} \boldsymbol {B} ^ {- 1} \boldsymbol {P} _ {1} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \left( \begin{array}{c c c} 0 & 0 & - 1 \\ 0 & - 1 & - 1 \\ - 1 & - 1 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{array} \right) = \left( \begin{array}{c c c} 0 & - 1 & 0 \\ 0 & 0 & - 1 \\ - 1 & 1 & - 1 \end{array} \right).</equation>进一步可得<equation>\operatorname{tr}(A^{-1}) = -1.</equation>

---

**2021年第7题 | 选择题 | 5分 | 答案: C**

7. 已知矩阵<equation>A=\left( \begin{array}{c c c}1&0&-1\\ 2&-1&1\\ -1&2&-5 \end{array} \right)</equation>，若存在下三角可逆矩阵 P和上三角可逆矩阵 Q，使 PAQ为对角矩阵，则

P,Q可以分别取（    ）

A.<equation>\begin{array}{l} \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right), \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right) \\ \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right), \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right) \\ \end{array}</equation>C.

B.<equation>\begin{array}{l} \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right), \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \\ \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 3 & 1 \end{array} \right), \left( \begin{array}{c c c} 1 & 2 & - 3 \\ 0 & - 1 & 2 \\ 0 & 0 & 1 \end{array} \right) \\ \end{array}</equation>D.

答案: C

**解析:**解（法一）对（A，E）作初等行变换.<equation>\begin{array}{l} (A, E) = \left( \begin{array}{c c c c c c} 1 & 0 & - 1 & 1 & 0 & 0 \\ 2 & - 1 & 1 & 0 & 1 & 0 \\ - 1 & 2 & - 5 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {2} - 2 r _ {1}} \left( \begin{array}{c c c c c c} 1 & 0 & - 1 & 1 & 0 & 0 \\ 0 & - 1 & 3 & - 2 & 1 & 0 \\ 0 & 2 & - 6 & 1 & 0 & 1 \end{array} \right) \\ \xrightarrow {r _ {2} ^ {*} \times (- 1)} \left( \begin{array}{c c c c c c} 1 & 0 & - 1 & 1 & 0 & 0 \\ 0 & 1 & - 3 & 2 & - 1 & 0 \\ 0 & 2 & - 6 & 1 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} ^ {*} - 2 r _ {2} ^ {* *}} \left( \begin{array}{c c c c c c} 1 & 0 & - 1 & 1 & 0 & 0 \\ 0 & 1 & - 3 & 2 & - 1 & 0 \\ 0 & 0 & 0 & - 3 & 2 & 1 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

取<equation>P = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & -1 & 0 \\ -3 & 2 & 1 \end{array} \right).</equation>记<equation>U=\left( \begin{array}{c c c}1&0&-1\\ 0&1&-3\\ 0&0&0 \end{array} \right)</equation>，对<equation>\binom{U}{E}</equation>作初等列变换.<equation>\binom {U} {E} = \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 1 & - 3 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) \xrightarrow {c _ {3} + c _ {1} + 3 c _ {2}} \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right).</equation>取<equation>Q = \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right).</equation>此时，PAQ =<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>为对角矩阵.因此，应选C.

（法二）代人法.

观察选项A、B发现，其中各有一个单位矩阵。

由于左乘矩阵相当于对原矩阵作行变换，右乘矩阵相当于对原矩阵作列变换，故<equation>\boldsymbol {A} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 2 & - 1 & 1 \\ - 1 & 2 & - 5 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right)</equation>的第一列为 A的第一列，即<equation>\left( \begin{array}{c}1\\ 2\\ -1 \end{array} \right)</equation><equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right) A = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 2 & - 1 & 1 \\ - 1 & 2 & - 5 \end{array} \right)</equation>的第一行为 A的第一行，即（1，0，-1），而任何矩阵与单位矩阵相乘所得结果均为原矩阵，于是选项A、B所给 P，Q均不能使得 PAQ为对角矩阵。由此可排除选项A、B.

将选项C中的两个矩阵代入计算，可得<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 2 & - 1 & 1 \\ - 1 & 2 & - 5 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{array} \right) = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 3 & 2 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & - 1 & 0 \\ - 1 & 2 & 0 \end{array} \right) = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>由此可见选项C正确. 应选C.简单计算可验证选项D不正确.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 3 & 1 \end{array} \right) A</equation>的第一行、第二行与A的第一行、第二行相同，即<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 3 & 1 \end{array} \right) A = \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 2 & - 1 & 1 \\ * & * & * \end{array} \right),</equation>记为B.B再右乘<equation>\left( \begin{array}{c c c} 1 & 2 & - 3 \\ 0 & - 1 & 2 \\ 0 & 0 & 1 \end{array} \right),</equation>则新矩阵的第一列为<equation>\left( \begin{array}{c} 1 \\ 2 \\ * \end{array} \right).</equation>于是，所得结果不是对角矩阵.

---

**2015年第20题 | 解答题 | 11分**

20. (本题满分11分)

设矩阵<equation>A=\left( \begin{array}{c c c} a & 1 & 0 \\ 1 & a & -1 \\ 0 & 1 & a \end{array} \right)</equation>，且<equation>A^{3}=O.</equation>I. 求 a的值；

II. 若矩阵<equation>X</equation>满足<equation>X - XA^{2} - AX + AXA^{2} = E</equation>，其中<equation>E</equation>为3阶单位矩阵，求<equation>X</equation>

**答案:**(20) （I）<equation>a=0;</equation><equation>(\mathrm {I I}) \boldsymbol {X} = \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1 \end{array} \right).</equation>

**解析:**解（I）（法一）由<equation>A^{3}=O</equation>知<equation>|A^{3}|=0</equation>又因为<equation>|A^{3}|=|A|^{3}</equation>所以<equation>|A|=0</equation>由题设可计算得<equation>|A|=a^{3}</equation>从而<equation>a^{3}=0</equation>，<equation>a=0.</equation>（法二）设<equation>\lambda</equation>为A的一个特征值，则由<equation>A^{3}=O</equation>可知<equation>\lambda^{3}=0.</equation>于是，A的特征值均为零.由矩阵的迹等于其特征值之和，可知<equation>\operatorname{tr}(A)=3 a=0</equation>即<equation>a=0.</equation>（Ⅱ）由第（I）问知，<equation>A=\left( \begin{array}{c c c} 0 & 1 & 0 \\ 1 & 0 & -1 \\ 0 & 1 & 0 \end{array} \right).</equation>由<equation>X - X A^{2} - A X + A X A^{2} = E</equation>可得，<equation>X \left(E - A ^ {2}\right) - A X \left(E - A ^ {2}\right) = E.</equation>化简得<equation>(E - A)X(E - A^{2}) = E.</equation>由此可知，<equation>E - A, E - A^{2}</equation>均为可逆矩阵，且<equation>\boldsymbol {X} = \left(\boldsymbol {E} - \boldsymbol {A}\right) ^ {- 1} \left(\boldsymbol {E} - \boldsymbol {A} ^ {2}\right) ^ {- 1}.</equation>下面用三种方法计算 X.

（法一）由<equation>(AB)^{-1} = B^{-1}A^{-1}</equation>得，<equation>X = (E - A)^{-1}(E - A^2)^{-1} = [(E - A^2)(E - A)]^{-1}\underline{\underline{A^3 = O}}(E - A - A^2)^{-1}.</equation>计算得<equation>A^{2} = \left( \begin{array}{c c c} 1 & 0 & -1 \\ 0 & 0 & 0 \\ 1 & 0 & -1 \end{array} \right)</equation>，故<equation>E - A - A^{2} = \left( \begin{array}{c c c} 0 & -1 & 1 \\ -1 & 1 & 1 \\ -1 & -1 & 2 \end{array} \right)</equation>，再计算得<equation>|E - A - A^2| = 1.</equation>因此<equation>\boldsymbol {X} = \left(\boldsymbol {E} - \boldsymbol {A} - \boldsymbol {A} ^ {2}\right) ^ {- 1} = \left(\boldsymbol {E} - \boldsymbol {A} - \boldsymbol {A} ^ {2}\right) ^ {*} = \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1 \end{array} \right).</equation>或利用初等变换法计算 X.<equation>\begin{array}{l} \left(\boldsymbol {E} - \boldsymbol {A} - \boldsymbol {A} ^ {2}, \boldsymbol {E}\right) = \left( \begin{array}{c c c c c c} 0 & - 1 & 1 & 1 & 0 & 0 \\ - 1 & 1 & 1 & 0 & 1 & 0 \\ - 1 & - 1 & 2 & 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {3} - r _ {2} ^ {*} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c c c} 0 & - 1 & 1 & 1 & 0 & 0 \\ - 1 & 0 & 2 & 1 & 1 & 0 \\ 0 & - 1 & 0 & - 1 & - 1 & 1 \end{array} \right) \\ \xrightarrow [ r _ {2} ^ {*} - 2 r _ {1} ^ {*} ]{r _ {1} - r _ {3} ^ {*}} \left( \begin{array}{c c c c c c} 0 & 0 & 1 & 2 & 1 & - 1 \\ - 1 & 0 & 0 & - 3 & - 1 & 2 \\ 0 & - 1 & 0 & - 1 & - 1 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 3 & 1 & - 2 \\ 0 & 1 & 0 & 1 & 1 & - 1 \\ 0 & 0 & 1 & 2 & 1 & - 1 \end{array} \right). \\ \end{array}</equation>因此，<equation>\boldsymbol {X} = \left(\boldsymbol {E} - \boldsymbol {A} - \boldsymbol {A} ^ {2}\right) ^ {- 1} = \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1 \end{array} \right).</equation>（法二）由于<equation>A^{3}=O</equation>，故<equation>A^{4}=O</equation>，从而<equation>(E - A)(E + A + A^{2}) = E - A^{3} = E, (E - A^{2})(E + A^{2}) = E - A^{4} = E.</equation>于是，<equation>(E - A)^{-1} = E + A + A^{2}, (E - A^{2})^{-1} = E + A^{2}.</equation>因此，<equation>\begin{aligned} X &= \left(E - A\right) ^ {- 1} \left(E - A ^ {2}\right) ^ {- 1} = \left(E + A + A ^ {2}\right) \left(E + A ^ {2}\right) \xlongequal {A ^ {2} = O} E + A + 2 A ^ {2} \\ &= E + \left( \begin{array}{c c c} 0 & 1 & 0 \\ 1 & 0 & - 1 \\ 0 & 1 & 0  \right) + 2 \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 0 & 0 \\ 1 & 0 & - 1  \right) &= \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1  \right). \end{aligned}</equation>（法三）分别计算<equation>(E - A)^{-1}, (E - A^{2})^{-1}</equation>.<equation>\boldsymbol {E} - \boldsymbol {A} = \left( \begin{array}{c c c} 1 & - 1 & 0 \\ - 1 & 1 & 1 \\ 0 & - 1 & 1 \end{array} \right), \quad \boldsymbol {E} - \boldsymbol {A} ^ {2} = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 1 & 0 \\ - 1 & 0 & 2 \end{array} \right).</equation>利用初等变换法计算<equation>(E - A)^{-1}, (E - A^{2})^{-1}</equation>.<equation>\begin{array}{l} (E - A, E) = \left( \begin{array}{c c c c c c} 1 & - 1 & 0 & 1 & 0 & 0 \\ - 1 & 1 & 1 & 0 & 1 & 0 \\ 0 & - 1 & 1 & 0 & 0 & 1 \end{array} \right) \xrightarrow [ r _ {3} - r _ {2} ^ {*} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c c c} 1 & - 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 & 1 & 0 \\ 0 & - 1 & 0 & - 1 & - 1 & 1 \end{array} \right) \\ \xrightarrow {r _ {1} - r _ {3} ^ {*}} \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 2 & 1 & - 1 \\ 0 & 0 & 1 & 1 & 1 & 0 \\ 0 & - 1 & 0 & - 1 & - 1 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 2 & 1 & - 1 \\ 0 & 1 & 0 & 1 & 1 & - 1 \\ 0 & 0 & 1 & 1 & 1 & 0 \end{array} \right), \\ \end{array}</equation><equation>\begin{array}{l} \left(\boldsymbol {E} - \boldsymbol {A} ^ {2}, \boldsymbol {E}\right) = \left( \begin{array}{c c c c c c} 0 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ - 1 & 0 & 2 & 0 & 0 & 1 \end{array} \right) \xrightarrow {r _ {3} - 2 r _ {1}} \left( \begin{array}{c c c c c c} 0 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ - 1 & 0 & 0 & - 2 & 0 & 1 \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c c c c} 1 & 0 & 0 & 2 & 0 & - 1 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 1 & 0 & 0 \end{array} \right). \\ \end{array}</equation>因此，<equation>\left(\boldsymbol {E} - \boldsymbol {A}\right) ^ {- 1} = \left( \begin{array}{c c c} 2 & 1 & - 1 \\ 1 & 1 & - 1 \\ 1 & 1 & 0 \end{array} \right), \quad \left(\boldsymbol {E} - \boldsymbol {A} ^ {2}\right) ^ {- 1} = \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{array} \right).</equation>综上所述，<equation>\boldsymbol {X} = \left(\boldsymbol {E} - \boldsymbol {A}\right) ^ {- 1} \left(\boldsymbol {E} - \boldsymbol {A} ^ {2}\right) ^ {- 1} = \left( \begin{array}{c c c} 2 & 1 & - 1 \\ 1 & 1 & - 1 \\ 1 & 1 & 0 \end{array} \right) \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{array} \right) = \left( \begin{array}{c c c} 3 & 1 & - 2 \\ 1 & 1 & - 1 \\ 2 & 1 & - 1 \end{array} \right).</equation>

---

**2012年第6题 | 选择题 | 4分 | 答案: B**

6. 设 A为3阶矩阵，P为3阶可逆矩阵，且<equation>P^{-1} A P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>若<equation>P=(\alpha_{1},\alpha_{2},\alpha_{3}), Q=(\alpha_{1}+\alpha_{2},\alpha_{2},\alpha_{3}),</equation>则<equation>Q^{-1} A Q=</equation>(    )

A.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>

答案: B

**解析:**解（法一）由题设知，<equation>Q=P\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，故<equation>Q^{-1}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) P^{-1}</equation>.从而<equation>\begin{aligned} Q ^ {- 1} A Q &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 0 & 0 & 1  \right) P ^ {- 1} A P \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1  \right) \\ &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 0 & 0 & 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1  \right) &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2  \right). \end{aligned}</equation>应选B.

（法二）由题设知，1，1，2是A的特征值，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>分别是属于特征值1，1，2的特征向量，即<equation>A\alpha_{1}=\alpha_{1},</equation><equation>A\alpha_{2}=\alpha_{2},</equation><equation>A\alpha_{3}=2\alpha_{3}.</equation>从而<equation>A\left(\alpha_{1} + \alpha_{2}\right) = \alpha_{1} + \alpha_{2},\alpha_{1} + \alpha_{2}</equation>也是<equation>A</equation>的属于特征值1的一个特征向量.<equation>A Q = A \left(\alpha_ {1} + \alpha_ {2}, \alpha_ {2}, \alpha_ {3}\right) = \left(\alpha_ {1} + \alpha_ {2}, \alpha_ {2}, 2 \alpha_ {3}\right) = Q \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>又由于 Q由 P作初等变换得到，P可逆，故Q可逆.于是<equation>Q^{-1} A Q=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>应选B.

---

**2011年第5题 | 选择题 | 4分 | 答案: D**

5. 设 A为3阶矩阵，将 A的第2列加到第1列得矩阵 B，再交换 B的第2行与第3行得单位矩阵，记<equation>P_{1}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right), P_{2}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{array} \right),</equation>则 A=（    )

A.<equation>P_{1} P_{2}</equation>B.<equation>P_{1}^{-1} P_{2}</equation>C.<equation>P_{2} P_{1}</equation>D.<equation>P_{2} P_{1}^{-1}</equation>

答案: D

**解析:**解 将 A的第2列加到第1列对应 A右乘矩阵<equation>P_{1}</equation>，得<equation>B=A P_{1}</equation>.交换 B的第2行与第3行对应 B左乘矩阵<equation>P_{2}</equation>，得<equation>E=P_{2} A P_{1}</equation>.于是<equation>A=P_{2}^{-1} P_{1}^{-1}.</equation>又因为<equation>P_{2}^{-1}=P_{2}</equation>，所以<equation>A=P_{2} P_{1}^{-1}.</equation>应选 D.

---

**2010年第13题 | 填空题 | 4分**

13. 设<equation>A, B</equation>为3阶矩阵，且<equation>|A| = 3, |B| = 2, |A^{-1} + B| = 2</equation>，则<equation>|A + B^{-1}</equation>

**解析:**由于<equation>A, B</equation>的行列式均不为零，故它们均可逆.因为

所以<equation>\boldsymbol {A} \left(\boldsymbol {A} ^ {- 1} + \boldsymbol {B}\right) \boldsymbol {B} ^ {- 1} = \boldsymbol {B} ^ {- 1} + \boldsymbol {A} = \boldsymbol {A} + \boldsymbol {B} ^ {- 1},</equation><equation>| A + B ^ {- 1} | = | A | \cdot | A ^ {- 1} + B | \cdot | B ^ {- 1} | \frac {| B ^ {- 1} | = \frac {1}{| B |}} {3 \times 2 \times \frac {1}{2}} = 3.</equation>

---

**2009年第6题 | 选择题 | 4分 | 答案: A**

6. 设<equation>A, P</equation>均为3阶矩阵，<equation>P^{\mathrm{T}}</equation>为<equation>P</equation>的转置矩阵，且<equation>P^{\mathrm{T}}AP = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>. 若<equation>P = \left(\alpha_{1}, \alpha_{2}, \alpha_{3}\right)</equation>，<equation>Q = \left(\alpha_{1} + \alpha_{2}, \alpha_{2}, \alpha_{3}\right)</equation>，

则<equation>Q^{\mathrm{T}} A Q</equation>为（    ）

A.<equation>\left( \begin{array}{c c c} 2 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>.<equation>\left( \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>B.

C.<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>

答案: A

**解析:**由题设知，<equation>Q</equation>为把 P的第2列加到第1列的结果，故<equation>Q=P\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>从而<equation>Q^{\mathrm{T}}A Q=\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) P^{\mathrm{T}} A P\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)=\left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation><equation>=\left( \begin{array}{c c c} 2 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>应选A.

---


#### 伴随矩阵与可逆矩阵

**2023年第5题 | 选择题 | 5分 | 答案: B**

5. 设 A,B为 n阶可逆矩阵，E为 n阶单位矩阵，<equation>M^{*}</equation>为矩阵 M的伴随矩阵，则<equation>\left( \begin{array}{cc} A & E \\ O & B \end{array} \right)^{*}=(\quad)</equation>A.<equation>\left( \begin{array}{c c} | A | B^{*} & - B^{*} A^{*} \\ O & | B | A^{*} \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c} | B | A^{*} & - A^{*} B^{*} \\ O & | A | B^{*} \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c} | B | A^{*} & - B^{*} A^{*} \\ O & | A | B^{*} \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c} | A | B^{*} & - A^{*} B^{*} \\ O & | B | A^{*} \end{array} \right)</equation>

答案: B

**解析:**解（法一）由于 A,B都可逆，故可以作初等行变换来求<equation>\left( \begin{array}{cc} A & E \\ O & B \end{array} \right)^{-1}.</equation><equation>\left( \begin{array}{c c c c} A & E & E & O \\ O & B & O & E \end{array} \right) \xrightarrow {\textcircled{1}} \left( \begin{array}{c c c c} E & A ^ {- 1} & A ^ {- 1} & O \\ O & E & O & B ^ {- 1} \end{array} \right) \xrightarrow {\textcircled{2}} \left( \begin{array}{c c c c} E & O & A ^ {- 1} & - A ^ {- 1} B ^ {- 1} \\ O & E & O & B ^ {- 1} \end{array} \right),</equation>其中操作<equation>\textcircled{1}</equation>对应左乘可逆矩阵<equation>\left( \begin{array}{cc} A^{-1} & O \\ O & B^{-1} \end{array} \right)</equation>，操作<equation>\textcircled{2}</equation>对应左乘可逆矩阵<equation>\left( \begin{array}{cc} E & -A^{-1} \\ O & E \end{array} \right)</equation>.于是，<equation>\left( \begin{array}{c c} A & E \\ O & B \end{array} \right) ^ {- 1} = \left( \begin{array}{c c} A ^ {- 1} & - A ^ {- 1} B ^ {- 1} \\ O & B ^ {- 1} \end{array} \right).</equation>对于任意 n阶方阵 M，都有<equation>M M^{*} = | M | E</equation>，从而当 M可逆时，<equation>M^{*} = | M | M^{-1}.</equation>又因为<equation>\left| \begin{array}{l l} A & E \\ O & B \end{array} \right| = | A | | B |</equation>，所以<equation>\left( \begin{array}{c c} A & E \\ O & B \end{array} \right) ^ {*} = \left| \begin{array}{c c} A & E \\ O & B \end{array} \right| \left( \begin{array}{c c} A & E \\ O & B \end{array} \right) ^ {- 1} = | A | | B | \left( \begin{array}{c c} A ^ {- 1} & - A ^ {- 1} B ^ {- 1} \\ O & B ^ {- 1} \end{array} \right) = \left( \begin{array}{c c} | B | A ^ {*} & - A ^ {*} B ^ {*} \\ O & | A | B ^ {*} \end{array} \right).</equation>因此，应选B.

也可以如下计算<equation>\left( \begin{array}{cc} A & E \\ O & B \end{array} \right)^{-1}.</equation>设<equation>\left( \begin{array}{cc} A & E \\ O & B \end{array} \right)^{-1}=\left( \begin{array}{cc} X_{1} & X_{2} \\ X_{3} & X_{4} \end{array} \right),</equation>则<equation>\left( \begin{array}{c c} A & E \\ O & B \end{array} \right) \left( \begin{array}{c c} X _ {1} & X _ {2} \\ X _ {3} & X _ {4} \end{array} \right) = \left( \begin{array}{c c} A X _ {1} + X _ {3} & A X _ {2} + X _ {4} \\ B X _ {3} & B X _ {4} \end{array} \right) = \left( \begin{array}{c c} E & O \\ O & E \end{array} \right).</equation>于是，<equation>\left\{ \begin{array}{l l} A X_{1}+X_{3}=E, \\ A X_{2}+X_{4}=O, \\ B X_{3}=O, \\ B X_{4}=E. \end{array} \right.</equation>由A，B均为可逆矩阵可得<equation>\left\{ \begin{array}{l l} X_{1}=A^{-1}, \\ X_{2}=-A^{-1}B^{-1}, \\ X_{3}=O, \\ X_{4}=B^{-1}. \end{array} \right.</equation>从而<equation>\left( \begin{array}{c c} A & E \\ O & B \end{array} \right) ^ {- 1} = \left( \begin{array}{c c} A ^ {- 1} & - A ^ {- 1} B ^ {- 1} \\ O & B ^ {- 1} \end{array} \right).</equation>（法二）分别记选项A、B、C、D中的矩阵为<equation>M_{1}, M_{2}, M_{3}, M_{4}</equation>，记<equation>\left( \begin{array}{cc} A & E \\ O & B \end{array} \right)=M.</equation>考虑<equation>M_{i}M (i=1,</equation>2,3,4). 若<equation>M_{i}=M^{*}</equation>，则<equation>M_{i}M=|A||B|E_{2n}.</equation>观察可得<equation>M_{1}M</equation>与<equation>M_{4}M</equation>的“第一列”均为<equation>\left( \begin{array}{c c} {| A | B^{*} A} \\ {O} \end{array} \right)</equation>，故<equation>M _ {1} M \neq | A | | B | E _ {2 n}, \quad M _ {4} M \neq | A | | B | E _ {2 n}.</equation>选项A、D均不正确.

又因为<equation>\left( \begin{array}{c c} | B | A ^ {*} & - B ^ {*} A ^ {*} \\ O & | A | B ^ {*} \end{array} \right) \left( \begin{array}{c c} A & E \\ O & B \end{array} \right) = \left( \begin{array}{c c} | A | | B | E & | B | A ^ {*} - B ^ {*} A ^ {*} B \\ O & | A | | B | E \end{array} \right) \neq | A | | B | E _ {2 n},</equation><equation>\left( \begin{array}{c c} | B | A ^ {*} & - A ^ {*} B ^ {*} \\ O & | A | B ^ {*} \end{array} \right) \left( \begin{array}{c c} A & E \\ O & B \end{array} \right) = \left( \begin{array}{c c} | A | | B | E & | B | A ^ {*} - A ^ {*} B ^ {*} B \\ O & | A | | B | E \end{array} \right) = | A | | B | E _ {2 n},</equation>所以选项C不正确，选项B正确. 应选B.

---

**2019年第5题 | 选择题 | 4分 | 答案: A**

5. 设 A是4阶矩阵，<equation>A^{*}</equation>是 A的伴随矩阵，若线性方程组<equation>A x=0</equation>的基础解系中只有2个向量，则<equation>r \left( A^{*} \right)=</equation>(    )

A.0 B.1 C.2 D.3

答案: A

**解析:**解 由于<equation>A x=0</equation>的基础解系中只含有2个向量，故<equation>r(A)=4-2=2</equation>又因为<equation>r(A)=2< 4-1</equation>所以<equation>r(A^{*})=0.</equation>因此，应选A.

---

**2017年第5题 | 选择题 | 4分 | 答案: A**

5. 设<equation>\alpha</equation>为 n维单位列向量，<equation>E</equation>为 n阶单位矩阵，则（    ）

A.<equation>E-\alpha\alpha^{\mathrm{T}}</equation>不可逆 B.<equation>E+\alpha\alpha^{\mathrm{T}}</equation>不可逆 C.<equation>E+2\alpha\alpha^{\mathrm{T}}</equation>不可逆 D.<equation>E-2\alpha\alpha^{\mathrm{T}}</equation>不可逆

答案: A

**解析:**解（法一）由于<equation>\alpha</equation>是n维单位列向量，故<equation>\operatorname{tr}(\alpha\alpha^{\mathrm{T}})=\alpha^{\mathrm{T}}\alpha=1</equation>因为<equation>\alpha</equation>非零，所以<equation>r(\alpha\alpha^{\mathrm{T}})\geqslant 1.</equation>又由于<equation>r(\alpha\alpha^{\mathrm{T}})\leqslant r(\alpha)=1</equation>故<equation>r(\alpha\alpha^{\mathrm{T}})=1.</equation>于是矩阵<equation>\alpha\alpha^{\mathrm{T}}</equation>的全部特征值为1，0，…，0，从而<equation>E-\alpha\alpha^{\mathrm{T}}</equation>的全部特征值为0，1，…，1.因此，<equation>E-\alpha\alpha^{\mathrm{T}}</equation>不可逆.应选A.

同理可得，<equation>E+\alpha\alpha^{\mathrm{T}}</equation>的全部特征值为2，1，…，1；<equation>E+2\alpha\alpha^{\mathrm{T}}</equation>的全部特征值为3，1，…，1；<equation>E-2\alpha\alpha^{\mathrm{T}}</equation>的全部特征值为-1，1，…，1.因此它们均可逆.

（法二）由于<equation>(\alpha\alpha^{\mathrm{T}})\alpha = \alpha(\alpha^{\mathrm{T}}\alpha) = \alpha</equation>，故<equation>(E - \alpha \alpha^ {\mathrm {T}}) \alpha = \alpha - \left(\alpha \alpha^ {\mathrm {T}}\right) \alpha = \alpha - \alpha = 0 = 0 \alpha .</equation>于是，0是<equation>E-\alpha\alpha^{\mathrm{T}}</equation>的一个特征值（或<equation>( E-\alpha\alpha^{\mathrm{T}} ) x=0</equation>有非零解<equation>\alpha ).</equation>因此，<equation>E-\alpha\alpha^{\mathrm{T}}</equation>不可逆.应选A.

（法三）排除法.

令<equation>\boldsymbol{\alpha} = (1,0,\cdots ,0)^{\mathrm{T}}</equation>，则<equation>\boldsymbol{\alpha}\boldsymbol{\alpha}^{\mathrm{T}}=\left( \begin{array}{c c c c} 1 & & & \\ & 0 & & \\ & & \ddots & \\ & & & 0 \end{array} \right).</equation>可以验证，<equation>E+\alpha\alpha^{\mathrm{T}},E+2\alpha\alpha^{\mathrm{T}},E-2\alpha\alpha^{\mathrm{T}}</equation>均可逆，从而可以排除选项B、C、D.因此，应选A.

---

**2012年第13题 | 填空题 | 4分**

13. 设<equation>A</equation>为3阶矩阵，<equation>|A|=3</equation><equation>A^{*}</equation>为<equation>A</equation>的伴随矩阵，若交换<equation>A</equation>的第1行与第2行得矩阵<equation>B</equation>，则<equation>|BA^{*}|=</equation>___.

**解析:**解（法一）由于 B为交换 A的第1行与第2行所得，故<equation>B=E(1,2)A</equation>从而<equation>\boldsymbol {B} \boldsymbol {A} ^ {*} = \boldsymbol {E} (1, 2) \boldsymbol {A} \boldsymbol {A} ^ {*} = \boldsymbol {E} (1, 2) | \boldsymbol {A} | \boldsymbol {E} = 3 \boldsymbol {E} (1, 2).</equation>因此，<equation>\left| B A ^ {*} \right| = \left| 3 E (1, 2) \right| = 3 ^ {3} \left| \begin{array}{c c c} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right| = - 2 7.</equation>（法二）由于<equation>A A^{*} = |A|E</equation>，故当A为3阶矩阵时，<equation>| \boldsymbol {A} | \cdot | \boldsymbol {A} ^ {*} | = | \boldsymbol {A A} ^ {*} | = \left| \begin{array}{c c c} | \boldsymbol {A} | & 0 & 0 \\ 0 & | \boldsymbol {A} | & 0 \\ 0 & 0 & | \boldsymbol {A} | \end{array} \right| = | \boldsymbol {A} | ^ {3}.</equation>从而<equation>|A^{*}| = |A|^{2}</equation>.

另一方面，由于<equation>B</equation>为交换<equation>A</equation>的第1行与第2行所得矩阵，故<equation>|B| = -|A|</equation>.因此，<equation>| B A ^ {*} | = | B | \cdot | A ^ {*} | = - | A | \cdot | A | ^ {2} = - 2 7.</equation>

---

**2009年第5题 | 选择题 | 4分 | 答案: B**

5. 设 A,B均为2阶方阵，<equation>A^{*}，B^{*}</equation>分别为 A,B的伴随矩阵.若<equation>|A|=2,|B|=3</equation>，则分块矩阵<equation>\left( \begin{array}{cc} O&A \\ B/O \end{array} \right)</equation>的伴随矩阵为（    )

A.<equation>\left( \begin{array}{c c} O & 3 B^{*} \\ 2 A^{*} & O \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c} O & 2 B^{*} \\ 3 A^{*} & O \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c} O & 3 A^{*} \\ 2 B^{*} & O \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c} O & 2 A^{*} \\ 3 B^{*} & O \end{array} \right)</equation>

答案: B

**解析:**解 （法一）先求<equation>\left| \begin{array}{cc}O&A\\ B/O \end{array} \right|.</equation>记<equation>C=\left( \begin{array}{cc}O&A\\ B/O \end{array} \right), C</equation>为4阶矩阵，A位于它的第1，2行和第3，4列，可按照以下步骤把C变为<equation>\left( \begin{array}{cc}A&O\\ O&B \end{array} \right).</equation>把C的第3列与第1列对换，第4列与第2列对换.因此，<equation>\left| \begin{array}{c c} O & A \\ B & O \end{array} \right| = (- 1) ^ {2} \left| \begin{array}{c c} A & O \\ O & B \end{array} \right| = | A | \cdot | B | = 6.</equation><equation>\left( \begin{array}{cc}O&A\\ B/O \end{array} \right)</equation>可逆.

由可逆矩阵与其伴随矩阵的关系可知，<equation>\left( \begin{array}{c c} O & A \\ B & O \end{array} \right) ^ {*} = \left| \begin{array}{c c} O & A \\ B & O \end{array} \right| \left( \begin{array}{c c} O & A \\ B & O \end{array} \right) ^ {- 1} = 6 \left( \begin{array}{c c} O & A \\ B & O \end{array} \right) ^ {- 1}.</equation>不妨设<equation>\left( \begin{array}{cc}O&A\\ B/O \end{array} \right)^{-1} = \left( \begin{array}{cc}X_1 & X_2\\ X_3 & X_4 \end{array} \right)</equation>，则<equation>\left( \begin{array}{c c} O & A \\ B & O \end{array} \right) \left( \begin{array}{c c} X _ {1} & X _ {2} \\ X _ {3} & X _ {4} \end{array} \right) = \left( \begin{array}{c c} A X _ {3} & A X _ {4} \\ B X _ {1} & B X _ {2} \end{array} \right) = \left( \begin{array}{c c} E & O \\ O & E \end{array} \right).</equation>由于 A,B均为可逆矩阵，故由<equation>A X_{4}=O</equation>，<equation>B X_{1}=O</equation>可知，<equation>X_{1}=X_{4}=O</equation>；由<equation>A X_{3}=E</equation>，<equation>B X_{2}=E</equation>得，<equation>X_{3}=A^{-1}</equation>，<equation>X_{2}=B^{-1}</equation>.因此，<equation>\left( \begin{array}{c c} \boldsymbol {O} & \boldsymbol {A} \\ \boldsymbol {B} & \boldsymbol {O} \end{array} \right) ^ {- 1} = \left( \begin{array}{c c} \boldsymbol {O} & \boldsymbol {B} ^ {- 1} \\ \boldsymbol {A} ^ {- 1} & \boldsymbol {O} \end{array} \right).</equation><equation>\left( \begin{array}{c c} O & A \\ B & O \end{array} \right) ^ {*} = 6 \left( \begin{array}{c c} O & B ^ {- 1} \\ A ^ {- 1} & O \end{array} \right) = 6 \left( \begin{array}{c c} O & \frac {B ^ {*}}{| B |} \\ \frac {A ^ {*}}{| A |} & O \end{array} \right) = \left( \begin{array}{c c} O & 2 B ^ {*} \\ 3 A ^ {*} & O \end{array} \right).</equation>应选B.

（法二）特殊值法.

取<equation>A=\sqrt{2} E, B=\sqrt{3} E</equation>满足<equation>|A|=2,|B|=3</equation>，则<equation>A^{*} = |A|A^{-1} = \sqrt{2} E, B^{*} = |B|B^{-1} = \sqrt{3} E.</equation>因此，<equation>\begin{aligned} \left( \begin{array}{c c} O & A \\ B & O  \right) ^ {*} &= \left( \begin{array}{c c} O & \sqrt {2} E \\ \sqrt {3} E & O  \right) ^ {*} &= \left| \begin{array}{c c} O & \sqrt {2} E \\ \sqrt {3} E & O  \right| \left( \begin{array}{c c} O & \sqrt {2} E \\ \sqrt {3} E & O  \right) ^ {- 1} &= 6 \left( \begin{array}{c c} O & \frac {1}{\sqrt {3}} E \\ \frac {1}{\sqrt {2}} E & O  \right) \\ &= \left( \begin{array}{c c} O & 2 \sqrt {3} E \\ 3 \sqrt {2} E & O  \right) &= \left( \begin{array}{c c} O & 2 B ^ {*} \\ 3 A ^ {*} & O  \right). \end{aligned}</equation>应选B.

---


#### 矩阵的秩

**2018年第6题 | 选择题 | 4分 | 答案: A**

6. 设 A,B为 n阶矩阵，记 r(X)为矩阵 X的秩，(X,Y)表示分块矩阵，则（    ）

A.<equation>r ( A, A B )=r ( A )</equation>B.<equation>r ( A, B A )=r ( A )</equation>C.<equation>r ( A, B )=\max \{ r ( A ) , r ( B ) \}</equation>D.<equation>r ( A, B )=r \left( A^{\mathrm{T}}, B^{\mathrm{T}} \right)</equation>

答案: A

**解析:**解记 C=AB.由于右乘矩阵表示对矩阵作列变换，故 C的列向量可由 A的列向量线性表示.于是，<equation>r ( A, C )=r ( A, A B )=r ( A ).</equation>因此，应选A.

下面分别说明选项B、C、D不正确.

选项B：<equation>r ( \mathbf{A}, \mathbf{B A})\geqslant r (\mathbf{A})</equation>.但是，<equation>r (\mathbf{A}, \mathbf{B A})=r (\mathbf{A})</equation>并不成立.

取<equation>A = \left( \begin{array}{ll}1 & 0\\ 0 & 0 \end{array} \right),B = \left( \begin{array}{ll}1 & 0\\ 1 & 1 \end{array} \right)</equation>，则<equation>BA = \left( \begin{array}{ll}1 & 0\\ 1 & 0 \end{array} \right),(A,BA) = \left( \begin{array}{lll}1 & 0 & 1 & 0\\ 0 & 0 & 1 & 0 \end{array} \right).r(A,BA) = 2</equation>但<equation>r(A) = 1.</equation>选项C：<equation>r ( A, B ) \geqslant\max \left\{r ( A ) , r ( B ) \right\}</equation>.但是，<equation>r ( A, B )=\max \left\{r ( A ) , r ( B ) \right\}</equation>并不成立.

取<equation>A = \left( \begin{array}{ll}1 & 0\\ 0 & 0 \end{array} \right),B = \left( \begin{array}{ll}0 & 0\\ 1 & 0 \end{array} \right)</equation>，则<equation>(A,B) = \left( \begin{array}{lll}1 & 0 & 0 & 0\\ 0 & 0 & 1 & 0 \end{array} \right),r(A,B) = 2</equation>，但<equation>r(A) = r(B) = 1.</equation>选项D：由于<equation>r(\mathbf{P})=r(\mathbf{P}^{\mathrm{T}})</equation>，而<equation>(\mathbf{A},\mathbf{B})^{\mathrm{T}}=\binom{\mathbf{A}^{\mathrm{T}}}{\mathbf{B}^{\mathrm{T}}}</equation>，故<equation>r(\mathbf{A},\mathbf{B})=r\binom{\mathbf{A}^{\mathrm{T}}}{\mathbf{B}^{\mathrm{T}}}</equation>.但是，<equation>r(\mathbf{A},\mathbf{B})=r(\mathbf{A}^{\mathrm{T}},\mathbf{B}^{\mathrm{T}})</equation>并不成立.

取<equation>A=\left( \begin{array}{ll}1&0\\ 0&0 \end{array} \right), B=\left( \begin{array}{ll}0&0\\ 1&0 \end{array} \right)</equation>，则<equation>(\mathbf{A},\mathbf{B})=\left( \begin{array}{llll}1&0&0&0\\ 0&0&1&0 \end{array} \right),(\mathbf{A}^{\mathrm{T}},\mathbf{B}^{\mathrm{T}})=\left( \begin{array}{llll}1&0&0&1\\ 0&0&0&0 \end{array} \right). r(\mathbf{A},\mathbf{B})=2,</equation>但<equation>r(\mathbf{A}^{\mathrm{T}},\mathbf{B}^{\mathrm{T}})=1.</equation>

---

**2017年第13题 | 填空题 | 4分**

13. 设矩阵<equation>A=\left( \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 2 \\ 0 & 1 & 1 \end{array} \right), \alpha_{1},\alpha_{2},\alpha_{3}</equation>为线性无关的3维列向量组，则向量组<equation>A\alpha_{1},A\alpha_{2},A\alpha_{3}</equation>的秩为 ___.

**解析:**由于<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关，故矩阵<equation>\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)</equation>可逆，从而<equation>r \left(A \alpha_ {1}, A \alpha_ {2}, A \alpha_ {3}\right) = r \left(A \left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right)\right) = r (A).</equation>下面我们用三种方法计算<equation>r(A)</equation>.

（法一）计算<equation>| A |</equation>得<equation>| A |=0</equation>，故<equation>r(A)\leqslant 2</equation>.又因为矩阵 A含有一个非零2阶子式，例如<equation>\left| \begin{array}{ll} 1 & 0 \\ 1 & 1 \end{array} \right|=1</equation>，所以<equation>r(A)\geqslant 2</equation>.因此，<equation>r(A)=2</equation>，从而向量组<equation>A\alpha_{1},A\alpha_{2},A\alpha_{3}</equation>的秩为2.

（法二）对矩阵 A作初等行变换将其化为阶梯形矩阵，进而求得其秩.<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & 0 & 1 \\ 1 & 1 & 2 \\ 0 & 1 & 1 \end{array} \right) \xrightarrow {r _ {2} - r _ {1}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 1 & 1 \end{array} \right) \xrightarrow {r _ {3} - r _ {2} ^ {*}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right).</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）因此，<equation>r ( A ) = 2.</equation>（法三）令<equation>\boldsymbol{\beta}_{1}=(1,1,0)^{\mathrm{T}}</equation><equation>\boldsymbol{\beta}_{2}=(0,1,1)^{\mathrm{T}}</equation><equation>\boldsymbol{\beta}_{3}=(1,2,1)^{\mathrm{T}}</equation>，则<equation>A=(\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2},\boldsymbol{\beta}_{3})</equation>.由于<equation>\boldsymbol{\beta}_{1}+\boldsymbol{\beta}_{2}=</equation><equation>\boldsymbol{\beta}_{3}</equation>，故<equation>r(A)\leqslant 2</equation>.又因为<equation>\boldsymbol{\beta}_{1},\boldsymbol{\beta}_{2}</equation>线性无关，所以<equation>r(A)\geqslant 2</equation>.因此，<equation>r(A)=2.</equation>

---


## 概率论与数理统计


### 随机变量的数字特征


#### 协方差与相关系数

**2025年第8题 | 选择题 | 5分 | 答案: D**

8. 设随机变量 X服从正态分布 N(-1,1), Y服从正态分布 N(1,2), 若 X与 X+2Y不相关，则 X与 X-Y的相关系数为（    ）

A.<equation>\frac{1}{3}</equation>B.<equation>\frac{1}{2}</equation>C.<equation>\frac{2}{3}</equation>D.<equation>\frac{3}{4}</equation>

答案: D

**解析:**解 由于 X服从正态分布 N（-1，1），Y服从正态分布 N（1，2），故 D（X）=1，D（Y）=2. 又因为 X与 X+2Y不相关，所以<equation>\operatorname{Cov}(X, X + 2 Y) = \operatorname{Cov}(X, X) + 2 \operatorname{Cov}(X, Y) = D (X) + 2 \operatorname{Cov}(X, Y) = 1 + 2 \operatorname{Cov}(X, Y) = 0.</equation>于是，<equation>\operatorname{Cov}(X, Y) = -\frac{1}{2}.</equation>进一步可得<equation>\operatorname {C o v} (X, X - Y) = \operatorname {C o v} (X, X) - \operatorname {C o v} (X, Y) = D (X) - \operatorname {C o v} (X, Y) = 1 - \left(- \frac {1}{2}\right) = \frac {3}{2}.</equation><equation>D (X - Y) = D (X) + D (Y) - 2 \operatorname {C o v} (X, Y) = 1 + 2 - 2 \cdot \left(- \frac {1}{2}\right) = 4.</equation>因此，X与X-Y的相关系数<equation>\rho = \frac {\operatorname {C o v} (X , X - Y)}{\sqrt {D (X)} \sqrt {D (X - Y)}} = \frac {\frac {3}{2}}{1 \cdot 2} = \frac {3}{4}.</equation>应选 D.

---

**2023年第16题 | 填空题 | 5分**

16. 设随机变量 X 与 Y 相互独立，且<equation>X \sim B ( 1, p )</equation><equation>Y \sim B ( 2, p )</equation><equation>p \in( 0, 1 )</equation>，则<equation>X+Y</equation>与<equation>X-Y</equation>的相关系数为___.

**答案:**<equation>- \frac {1}{3}.</equation>

**解析:**解 由<equation>X\sim B(1,p)</equation>可知，<equation>D ( X )=p ( 1-p ).</equation>由<equation>Y\sim B ( 2,p)</equation>可知，<equation>D ( Y )=2 p ( 1-p ).</equation><equation>X+Y</equation>与<equation>X-Y</equation>的相关系数<equation>\rho=\frac{\operatorname{Cov}(X+Y,X-Y)}{\sqrt{D(X+Y)}\sqrt{D(X-Y)}}.</equation>由于 X与 Y相互独立，故<equation>D (X + Y) = D (X) + D (Y) = 3 p (1 - p),</equation><equation>D (X - Y) = D (X) + D (Y) = 3 p (1 - p).</equation>由协方差的性质可得，<equation>\begin{aligned} \operatorname {C o v} (X + Y, X - Y) &= \operatorname {C o v} (X, X) - \operatorname {C o v} (X, Y) + \operatorname {C o v} (Y, X) - \operatorname {C o v} (Y, Y) \\ &= D (X) - D (Y) = - p (1 - p). \end{aligned}</equation>因此，<equation>\rho = \frac {- p (1 - p)}{\sqrt {3 p (1 - p)} \sqrt {3 p (1 - p)}} = - \frac {1}{3}.</equation>

---

**2022年第8题 | 选择题 | 5分 | 答案: D**

8. 设随机变量<equation>X\sim N(0,4)</equation>，随机变量<equation>Y\sim B\left(3,\frac{1}{3}\right)</equation>，且 X，Y不相关，则<equation>D(X-3Y+1)=</equation>(    )

A.2 B.4 C.6 D.10

答案: D

**解析:**解 由于 X~ N（0,4），Y~ B<equation>\left( 3, \frac{1}{3} \right)</equation>，故 X的方差 D（X）=4，Y的方差<equation>D (Y) = 3 \times \frac {1}{3} \times \left(1 - \frac {1}{3}\right) = \frac {2}{3}.</equation>又因为<equation>X, Y</equation>不相关，所以<equation>\operatorname{Cov}(X, Y) = 0.</equation>由方差的性质，<equation>\begin{aligned} D (X - 3 Y + 1) &= D (X - 3 Y) = D (X) + D (3 Y) - 2 \operatorname {C o v} (X, 3 Y) \\ &= D (X) + 9 D (Y) - 6 \operatorname {C o v} (X, Y) = 4 + 9 \times \frac {2}{3} - 0 = 1 0. \end{aligned}</equation>因此，应选D.

---

**2022年第10题 | 选择题 | 5分 | 答案: B**

10. 设二维随机变量（X，Y）的概率分布为

<table border="1"><tr><td>X\ Y</td><td>0</td><td>1</td><td>2</td></tr><tr><td>-1</td><td>0.1</td><td>0.1</td><td>b</td></tr><tr><td>1</td><td>a</td><td>0.1</td><td>0.1</td></tr></table>

若事件<equation>\{\max \{X,Y\}=2\}</equation>与事件<equation>\{\min \{X,Y\}=1\}</equation>相互独立，则<equation>\operatorname{Cov}(X,Y)=</equation>(    )

A. -0.6 B. -0.36 C. 0 D. 0.48

答案: B

**解析:**解记事件 A = {<equation>\max \{ X, Y \}=2</equation>} ，事件 B = {<equation>\min \{ X, Y \}=1</equation>} .由于事件 A与B相互独立，故 P（AB）=P(A)P(B).

分别计算 P（A），P（B），P（AB）.<equation>P (A) = P \left\{\max \left\{X, Y \right\} = 2 \right\} = P \left\{Y = 2 \right\} = b + 0. 1.</equation><equation>P (B) = P \left\{\min \left\{X, Y \right\} = 1 \right\} = P \left\{X = 1, Y = 1 \right\} + P \left\{X = 1, Y = 2 \right\} = 0. 1 + 0. 1 = 0. 2.</equation><equation>P (A B) = P \left\{\max \left\{X, Y \right\} = 2, \min \left\{X, Y \right\} = 1 \right\} = P \left\{X = 1, Y = 2 \right\} = 0. 1.</equation>于是，<equation>0. 1 = ( b + 0. 1 ) \times 0. 2</equation>，解得 b=0.4. 进一步，由联合分布律中各概率之和为1，即<equation>0. 1 + 0. 1</equation><equation>+ b + a + 0. 1 + 0. 1 = 1</equation>可得，a=0.2.

XY的可能取值为-2，-1，0，1，2.<equation>P \{X Y = - 2 \} = P \{X = - 1, Y = 2 \} = 0. 4.</equation><equation>P \left\{X Y = - 1 \right\} = P \left\{X = - 1, Y = 1 \right\} = 0. 1.</equation><equation>P \{X Y = 1 \} = P \{X = 1, Y = 1 \} = 0. 1.</equation><equation>P \{X Y = 2 \} = P \{X = 1, Y = 2 \} = 0. 1.</equation><equation>P \{X Y = 0 \} = 1 - 0. 4 - 0. 1 - 0. 1 - 0. 1 = 0. 3.</equation>分别计算 E（X），E（Y），E（XY）.<equation>E (X) = - 1 \times (0. 1 + 0. 1 + 0. 4) + 1 \times (0. 2 + 0. 1 + 0. 1) = - 0. 2.</equation><equation>E (Y) = 0 \times (0. 1 + 0. 2) + 1 \times (0. 1 + 0. 1) + 2 \times (0. 4 + 0. 1) = 1. 2.</equation><equation>E (X Y) = (- 2) \times 0. 4 + (- 1) \times 0. 1 + 0 \times 0. 3 + 1 \times 0. 1 + 2 \times 0. 1 = - 0. 6.</equation>因此，<equation>\operatorname {C o v} (X, Y) = E (X Y) - E (X) E (Y) = - 0. 6 - (- 0. 2) \times 1. 2 = - 0. 3 6.</equation>应选B.

---

**2021年第16题 | 填空题 | 5分**

16. 甲，乙两个盒子中各装有2个红球和2个白球，先从甲盒中任取一球，观察颜色后放入乙盒中，再从乙盒中任取一个球，令 X, Y分别表示从甲盒和乙盒中取到的红球个数，则 X与 Y的相关系数为___

**答案:**# 1 5.

**解析:**解 根据相关系数的计算公式，X与Y的相关系数为<equation>\rho = \frac {\operatorname {C o v} (X , Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}}.</equation>下面分别计算 X, Y的分布律与数字特征.

取球模型为等可能模型.

X的可能取值为0，1.取到白球，则<equation>X=0</equation>，取到红球，则<equation>X=1.</equation><equation>P \{X = 0 \} = \frac {1}{2}, \quad P \{X = 1 \} = \frac {1}{2}.</equation>于是，<equation>E ( X ) = \frac {1}{2}, E \left( X^{2}\right) = \frac {1}{2}, D ( X ) = \frac {1}{2} - \left(\frac {1}{2}\right)^{2} = \frac {1}{4}.</equation>Y的可能取值为0，1. 若从甲盒中取出的是白球，则后来乙盒中共有2个红球和3个白球，取到红球的概率为<equation>\frac{2}{5}</equation>即在 X=0发生的条件下 Y=1发生的概率为<equation>\frac{2}{5}</equation>；若从甲盒中取出的是红球，则后来乙盒中共有3个红球和2个白球，取到红球的概率为<equation>\frac{3}{5}</equation>即在 X=1发生的条件下 Y=1发生的概率为<equation>\frac{3}{5}.</equation><equation>\begin{aligned} P \{Y = 1 \} &= P \{Y = 1 \mid X = 0 \} P \{X = 0 \} + P \{Y = 1 \mid X = 1 \} P \{X = 1 \} \\ &= \frac {2}{5} \times \frac {1}{2} + \frac {3}{5} \times \frac {1}{2} = \frac {1}{2}. \end{aligned}</equation><equation>P \{Y = 0 \} = 1 - P \{Y = 1 \} = 1 - \frac {1}{2} = \frac {1}{2}.</equation>于是，<equation>E ( Y )=\frac{1}{2}, E ( Y^{2} )=\frac{1}{2}, D ( Y )=\frac{1}{2}-\left(\frac{1}{2}\right)^{2}=\frac{1}{4}.</equation>XY的可能取值为0,1.<equation>P \{X Y = 1 \} = P \{X = 1, Y = 1 \} = P \{Y = 1 \mid X = 1 \} P \{X = 1 \} = \frac {3}{5} \times \frac {1}{2} = \frac {3}{1 0}.</equation><equation>P \{X Y = 0 \} = 1 - \frac {3}{1 0} = \frac {7}{1 0}.</equation>于是，<equation>E ( X Y ) = P \{ X Y = 1 \} \times 1 + P \{ X Y = 0 \} \times 0 = \frac {3}{1 0}.</equation>因此，<equation>\rho = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {\frac {3}{1 0} - \frac {1}{2} \times \frac {1}{2}}{\frac {1}{2} \times \frac {1}{2}} = \frac {\frac {1}{2 0}}{\frac {1}{4}} = \frac {1}{5}.</equation>

---


#### 数学期望与方差

**2024年第8题 | 选择题 | 5分 | 答案: B**

8. 设随机变量 X的概率密度为<equation>f ( x )=\left\{\begin{array}{ll}6 x(1-x),&0<x<1,\\0,&\text{其他},\end{array}\right.</equation>则 X的三阶中心矩<equation>E \left\{ \left[ X-E ( X ) \right]^{3} \right\}=(\quad)</equation>A.<equation>-\frac{1}{3 2}</equation>B.0 C.<equation>\frac{1}{1 6}</equation>D.<equation>\frac{1}{2}</equation>

答案: B

**解析:**解 根据数学期望的定义，<equation>\begin{aligned} E (X) &= \int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \int_ {0} ^ {1} x \cdot 6 x (1 - x) \mathrm {d} x = \int_ {0} ^ {1} \left(6 x ^ {2} - 6 x ^ {3}\right) \mathrm {d} x = \left. \left(2 x ^ {3} - \frac {3 x ^ {4}}{2}\right) \right| _ {0} ^ {1} \\ &= 2 - \frac {3}{2} = \frac {1}{2}. \end{aligned}</equation>进一步可得，<equation>\begin{array}{l} E \left\{\left[ X - E (X) \right] ^ {3} \right\} = \int_ {- \infty} ^ {+ \infty} \left(x - \frac {1}{2}\right) ^ {3} f (x) \mathrm {d} x = \int_ {0} ^ {1} \left(x - \frac {1}{2}\right) ^ {3} \cdot 6 x (1 - x) \mathrm {d} x \\ \underline {{=}} t = x - \frac {1}{2} 6 \int_ {- \frac {1}{2}} ^ {\frac {1}{2}} t ^ {3} \cdot \left(t + \frac {1}{2}\right) \left(\frac {1}{2} - t\right) \mathrm {d} t = 6 \int_ {- \frac {1}{2}} ^ {\frac {1}{2}} t ^ {3} \left(\frac {1}{4} - t ^ {2}\right) \mathrm {d} t \\ = 6 \int_ {- \frac {1}{2}} ^ {\frac {1}{2}} \left(\frac {1}{4} t ^ {3} - t ^ {5}\right) \mathrm {d} t \stackrel {\text {对称性}} {=} 0. \\ \end{array}</equation>因此，应选B.

---


### 随机变量及其分布

**2025年第9题 | 选择题 | 5分 | 答案: C**

9. 设<equation>X_{1}, X_{2}, \dots , X_{2 0}</equation>是来自总体B(1,0.1)的简单随机样本，令<equation>T=\sum_{i=1}^{2 0} X_{i}</equation>利用泊松分布近似表示二项分布的方法可得<equation>P\{ T\leqslant 1\}\approx</equation>(    )

A.<equation>\frac{1} {\mathrm{e}^{2}}</equation>B.<equation>\frac{2} {\mathrm{e}^{2}}</equation>C.<equation>\frac{3} {\mathrm{e}^{2}}</equation>D.<equation>\frac{4} {\mathrm{e}^{2}}</equation>

答案: C

**解析:**解 由<equation>X_{i}(i = 1,2,\dots ,20)\sim B(1,0.1)</equation>可知，<equation>X_{i}</equation>可看作一次随机试验的结果，试验成功的概率为0.1，<equation>T = \sum_{i = 1}^{20}X_{i}</equation>可看作20次独立重复试验中试验成功的次数，服从<equation>B(20,0.1)</equation>.根据泊松定理，<equation>n = 20,p_{n} = 0.1,\lambda = 2,T</equation>近似服从参数为2的泊松分布.

因此，<equation>P \{T \leqslant 1 \} = P \{T = 0 \} + P \{T = 1 \} \approx \frac {2 ^ {0} \cdot \mathrm {e} ^ {- 2}}{1} + \frac {2 ^ {1} \cdot \mathrm {e} ^ {- 2}}{1} = \frac {3}{\mathrm {e} ^ {2}}.</equation>应选C.

---

**2025年第10题 | 选择题 | 5分 | 答案: C**

10. 设总体 X的分布函数为 F(x),<equation>X_{1}, X_{2}, \dots, X_{n}</equation>为来自总体 X的简单随机样本，样本的经验分布函数为<equation>F_{n}(x)</equation>对于给定的 x(0 < F(x) < 1), D(F_{n}(x))=（    )

A. F(x)[1-F(x)] B.<equation>[F(x)]^{2}</equation>C.<equation>\frac{1}{n} F(x)[1-F(x)]</equation>D.<equation>\frac{1}{n}[F(x)]^{2}</equation>

答案: C

**解析:**解记<equation>X_{i}</equation>的分布函数为<equation>F_{X_{i}}(x).</equation>由于<equation>X_{i} ( i=1,2,\dots,n)</equation>与X同分布，故<equation>F_{X_{i}}(x)=F(x).</equation>令<equation>Y_{i}=\left\{\begin{array}{ll}1,&X_{i}\leqslant x,\\ 0,&X_{i}>x,\end{array}\right. i=1,2,\dots,n</equation>则<equation>Y_{i}</equation>的分布律满足<equation>P \left\{Y _ {i} = 1 \right\} = P \left\{X _ {i} \leqslant x \right\} = F _ {X _ {i}} (x) = F (x),</equation><equation>P \left\{Y _ {i} = 0 \right\} = P \left\{X _ {i} > x \right\} = 1 - F _ {X _ {i}} (x) = 1 - F (x).</equation>由此可得<equation>Y_{i}\sim B(1,F(x))</equation>.于是，<equation>E \left(Y _ {i}\right) = F (x), \quad D \left(Y _ {i}\right) = F (x) [ 1 - F (x) ].</equation>注意到<equation>F_{n}(x)=\frac{1}{n}\sum_{i=1}^{n} Y_{i}</equation>，且<equation>Y_{1},Y_{2},\dots ,Y_{n}</equation>独立同分布，故<equation>D \left[ F _ {n} (x) \right] = D \left(\frac {1}{n} \sum_ {i = 1} ^ {n} Y _ {i}\right) = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} D \left(Y _ {i}\right) = \frac {1}{n} D \left(Y _ {i}\right) = \frac {1}{n} F (x) [ 1 - F (x) ].</equation>因此，应选C.

---

**2024年第9题 | 选择题 | 5分 | 答案: B**

9. 设随机变量 X, Y相互独立，且<equation>X\sim N(0,2),Y\sim N(-1,1)</equation>，设<equation>p_{1}=P\{2X>Y\}, p_{2}=P\{X-2Y>1\}</equation>，则（    )

A.<equation>p_{1}>p_{2}>\frac{1}{2}</equation>B.<equation>p_{2}>p_{1}>\frac{1}{2}</equation>C.<equation>p_{1}<p_{2}<\frac{1}{2}</equation>D.<equation>p_{2}<p_{1}<\frac{1}{2}</equation>

答案: B

**解析:**解 由于<equation>X\sim N(0,2),Y\sim N(-1,1)</equation>，故<equation>E(X) = 0,D(X) = 2,E(Y) = -1,D(Y) = 1</equation>，从而<equation>E (Y - 2 X) = E (Y) - 2 E (X) = - 1 - 0 = - 1,</equation><equation>D (Y - 2 X) = D (Y) + 4 D (X) = 1 + 4 \times 2 = 9,</equation><equation>E (2 Y - X) = 2 E (Y) - E (X) = 2 \times (- 1) - 0 = - 2,</equation><equation>D (2 Y - X) = 4 D (Y) + D (X) = 4 \times 1 + 2 = 6.</equation>于是，<equation>Y - 2 X\sim N(-1,9), 2 Y - X\sim N(-2,6).</equation>将它们标准化可得<equation>\frac{Y - 2 X + 1}{3}\sim N(0,1),</equation><equation>\frac{2 Y - X + 2}{\sqrt{6}}\sim N(0,1).</equation>由此可得，<equation>\begin{array}{l} p _ {1} = P | 2 X - Y > 0 | = P | Y - 2 X < 0 | = P \left\{\frac {Y - 2 X + 1}{3} < \frac {1}{3} \right\} \\ = P \left\{\frac {Y - 2 X + 1}{3} \leqslant \frac {1}{3} \right\} = \Phi \left(\frac {1}{3}\right), \\ \end{array}</equation><equation>\begin{array}{l} p _ {2} = P \left| X - 2 Y > 1 \right| = P \left| 2 Y - X < - 1 \right| = P \left\{\frac {2 Y - X + 2}{\sqrt {6}} < \frac {1}{\sqrt {6}} \right\} \\ = P \left\{\frac {2 Y - X + 2}{\sqrt {6}} \leqslant \frac {1}{\sqrt {6}} \right\} = \Phi \left(\frac {1}{\sqrt {6}}\right), \\ \end{array}</equation>其中<equation>\varPhi(x)</equation>是标准正态分布的分布函数.

由于<equation>\varPhi(x)</equation>单调增加，且<equation>0 < \frac{1}{3} < \frac{1}{\sqrt{6}}</equation>，故<equation>\frac{1}{2}=\varPhi(0)<\varPhi\left(\frac{1}{3}\right)<\varPhi\left(\frac{1}{\sqrt{6}}\right).</equation>因此，<equation>p_{2}>p_{1}> \frac{1}{2}</equation>应选B.

---

**2024年第16题 | 填空题 | 5分**

16. 设随机试验每次成功的概率为 p，现进行3次独立重复试验，在至少成功1次的条件下，3次试验全部成功的概率为<equation>\frac{4}{1 3}</equation>，则 p=___

**答案:**# p=2/3

**解析:**解设 X为3次独立重复试验中试验成功的次数，则<equation>X\sim B(3,p).</equation>在至少成功1次的条件下， 3次试验全部成功的概率为<equation>P\mid X=3\mid X\geqslant 1\mid =\frac{P\mid X=3,X\geqslant 1\mid}{P\mid X\geqslant 1\mid}=\frac{P\mid X=3\mid}{P\mid X\geqslant 1\mid}=\frac{\mathrm{C}_{3}^{3} p^{3}}{1-\mathrm{C}_{3}^{0}(1-p)^{3}}=\frac{4}{13}.</equation>于是，<equation>\frac{p^{3}}{1-(1-p)^{3}}=\frac{4}{13}.</equation>整理可得<equation>3 p^{3}+4 p^{2}-4 p=0</equation>即<equation>p(p+2)(3 p-2)=0.</equation>由于 p > 0，故 p =<equation>\frac{2}{3}.</equation>

---

**2019年第8题 | 选择题 | 4分 | 答案: A**

8. 随机变量 X与 Y相互独立，且都服从正态分布<equation>N(\mu ,\sigma^{2})</equation>，则<equation>P\{|X-Y|<1\}</equation>(    )

A. 与<equation>\mu</equation>无关，而与<equation>\sigma^{2}</equation>有关 B. 与<equation>\mu</equation>有关，而与<equation>\sigma^{2}</equation>无关

C. 与<equation>\mu,\sigma^{2}</equation>都有关 D. 与<equation>\mu,\sigma^{2}</equation>都无关

答案: A

**解析:**解 由于 X，Y相互独立且都服从正态分布<equation>N(\mu ,\sigma^{2})</equation>，故<equation>E(X-Y)=0,D(X-Y)=2\sigma^{2},</equation><equation>X-Y\sim N(0,2\sigma^{2}).</equation>将 X-Y标准化，可得<equation>\frac{X-Y}{\sqrt{2}\sigma}\sim N(0,1).</equation>，于是，<equation>\begin{array}{l} P \left\{\mid X - Y \mid < 1 \right\} = P \left\{- 1 < X - Y < 1 \right\} = P \left\{\frac {- 1}{\sqrt {2} \sigma} < \frac {X - Y}{\sqrt {2} \sigma} < \frac {1}{\sqrt {2} \sigma} \right\} \\ = \Phi \left(\frac {1}{\sqrt {2} \sigma}\right) - \Phi \left(\frac {- 1}{\sqrt {2} \sigma}\right) = 2 \Phi \left(\frac {1}{\sqrt {2} \sigma}\right) - 1. \\ \end{array}</equation>因此，<equation>P \left\{ \mid X - Y \mid < 1 \right\}</equation>仅与<equation>\sigma^{2}</equation>有关.应选A.

---

**2018年第7题 | 选择题 | 4分 | 答案: A**

7. 设随机变量 X的概率密度 f(x)满足<equation>f(1+x)=f(1-x)</equation>，且<equation>\int_{0}^{2} f(x)\mathrm{d}x=0.6</equation>，则<equation>P\{ X<0\}=</equation>(    )

A. 0.2 B. 0.3 C. 0.4 D. 0.5

答案: A

**解析:**解 由于<equation>f ( 1+x)=f ( 1-x)</equation>，故 f(x)的图像关于 x=1对称.于是，<equation>P\{ X < 0 \}=P\{ X > 2 \}.</equation>又因为<equation>P\{ 0\leqslant X\leqslant 2\}=\int_{0}^{2} f ( x ) \mathrm{d} x=0. 6</equation>，且<equation>P\{ X < 0 \}+P\{ 0\leqslant X\leqslant 2\}+P\{ X > 2\}=1,</equation>以<equation>P\{ X < 0 \}=\frac{1-P\{ 0\leqslant X\leqslant 2\}}{2}=\frac{1-0. 6}{2}=0. 2.</equation>因此，应选A.

---

**2013年第7题 | 选择题 | 4分 | 答案: A**

7. 设<equation>X_{1}, X_{2}, X_{3}</equation>是随机变量，且<equation>X_{1}\sim N(0,1), X_{2}\sim N(0,2^{2}), X_{3}\sim N(5,3^{2}), p_{i}=P\{-2\leqslant X_{i}\leqslant 2\} (i=1,2,3)</equation>，则（    )

A.<equation>p_{1}>p_{2}>p_{3}</equation>B.<equation>p_{2}>p_{1}>p_{3}</equation>C.<equation>p_{3}>p_{1}>p_{2}</equation>D.<equation>p_{1}>p_{3}>p_{2}</equation>

答案: A

**解析:**解 由<equation>X_{2}\sim N(0,2^{2}),X_{3}\sim N(5,3^{2})</equation>知，<equation>\frac{X_2}{2}\sim N(0,1),\frac{X_3 - 5}{3}\sim N(0,1)</equation>.于是，<equation>p_{1} = P\{-2\leqslant X_{1}\leqslant 2\} = \Phi (2) - \Phi (-2) = 1 - \Phi (-2) - \Phi (-2) = 1 - 2\Phi (-2),</equation><equation>p_{2} = P\{-2\leqslant X_{2}\leqslant 2\} = P\left\{-1\leqslant \frac{X_{2}}{2}\leqslant 1\right\} = \Phi (1) - \Phi (-1) = 1 - 2\Phi (-1),</equation><equation>p_{3} = P\{-2\leqslant X_{3}\leqslant 2\} = P\left\{-\frac{7}{3}\leqslant \frac{X_{3} - 5}{3}\leqslant -1\right\} = \Phi (-1) - \Phi \left(-\frac{7}{3}\right).</equation>于<equation>\Phi (-1) > \Phi (-2)</equation>，故<equation>p_{1} > p_{2}</equation>.

设标准正态分布的概率密度为<equation>\varphi (x)</equation>，则<equation>\varphi (x)</equation>为偶函数，且在<equation>(-\infty ,0]</equation>上单调增加（如图所示）.又由于<equation>p_{2} = \int_{-1}^{1}\varphi (x)\mathrm{d}x,p_{3} = \int_{-\frac{7}{3}}^{-1}\varphi (x)\mathrm{d}x</equation>，而<equation>\varphi (x)</equation>在（-1,1）上的取值都大于<equation>\varphi (x)</equation>在<equation>\left(-\frac{7}{3},-1\right)</equation>上的取值，且积分区间的长度满足<equation>|1-(-1)|> \left| -1-\left(-\frac{7}{3}\right) \right|</equation>，故<equation>p_{2}>p_{3}.</equation>综上所述，<equation>p_{1}>p_{2}>p_{3}.</equation>应选A.

---

**2011年第7题 | 选择题 | 4分 | 答案: D**

7. 设<equation>F_{1}(x)</equation>与<equation>F_{2}(x)</equation>为两个分布函数，其相应的概率密度<equation>f_{1}(x)</equation>与<equation>f_{2}(x)</equation>是连续函数，则必为概率密度的是（    )

A.<equation>f_{1}(x)f_{2}(x)</equation>B.<equation>2f_{2}(x)F_{1}(x)</equation>C.<equation>f_{1}(x)F_{2}(x)</equation>D.<equation>f_{1}(x)F_{2}(x)+f_{2}(x)F_{1}(x)</equation>

答案: D

**解析:**分布函数和概率密度的性质知，<equation>f_{1}(x)F_{2}(x) + f_{2}(x)F_{1}(x)\geqslant 0</equation>，且<equation>\begin{aligned} \int_ {- \infty} ^ {+ \infty} \left[ f _ {1} (x) F _ {2} (x) + f _ {2} (x) F _ {1} (x) \right] \mathrm {d} x &= \int_ {- \infty} ^ {+ \infty} \left[ F _ {1} (x) F _ {2} (x) \right] ^ {\prime} \mathrm {d} x \\ &= F _ {1} (+ \infty) F _ {2} (+ \infty) - F _ {1} (- \infty) F _ {2} (- \infty) \\ &= 1 - 0 = 1. \end{aligned}</equation>因此，<equation>f_{1}(x)F_{2}(x) + f_{2}(x)F_{1}(x)</equation>为概率密度.应选D.

---

**2010年第7题 | 选择题 | 4分 | 答案: C**

7. 设随机变量 X的分布函数 F(x) =<equation>\left\{\begin{array}{l l}0,&x<0,\\ \frac{1}{2},&0\leqslant x<1,\\ 1-\mathrm{e}^{-x},&x\geqslant 1,\end{array} \right.</equation>则 P{X=1} =（    )

A. 0 B.<equation>\frac{1}{2}</equation>C.<equation>\frac{1}{2}-\mathrm{e}^{-1}</equation>D.<equation>1-\mathrm{e}^{-1}</equation>

答案: C

**解析:**解<equation>P \{ X = 1 \} = P \{ X \leqslant 1 \} - P \{ X < 1 \} = F ( 1 ) - F ( 1^{-} ) = 1 - \mathrm{e}^{-1} - \frac{1}{2} = \frac{1}{2} - \mathrm{e}^{-1}.</equation>应选C.

---

**2010年第8题 | 选择题 | 4分 | 答案: A**

8. 设<equation>f_{1}(x)</equation>为标准正态分布的概率密度，<equation>f_{2}(x)</equation>为<equation>[-1,3]</equation>上均匀分布的概率密度，若<equation>f (x) = \left\{ \begin{array}{l l} a f _ {1} (x), & x \leqslant 0, \\ b f _ {2} (x), & x > 0 \end{array} \right. (a > 0, b > 0)</equation>为概率密度，则 a,b应满足（    ）

A. 2a+3b=4 B. 3a+2b=4 C. a+b=1 D. a+b=2

答案: A

**解析:**解 由于标准正态分布的概率密度的图形关于 y轴对称，故<equation>\int_{0}^{+\infty} f_{1}(x)\mathrm{d}x=\int_{-\infty}^{0} f_{1}(x)\mathrm{d}x=\frac{1}{2}.</equation>又由题设知，<equation>f_{2}(x)=\left\{\begin{array}{ll}\frac{1}{4},&-1\leqslant x\leqslant 3,\\ 0,&\text{其他}.\end{array} \right.</equation>由于 f(x)为概率密度，故<equation>1=\int_{-\infty}^{+\infty} f(x)\mathrm{d}x=\int_{-\infty}^{0} a f_{1}(x)\mathrm{d}x+\int_{0}^{+\infty} b f_{2}(x)\mathrm{d}x=\frac{1}{2} a+\int_{0}^{3} \frac{b}{4}\mathrm{d}x=\frac{1}{2} a+\frac{3}{4} b,</equation>即<equation>\frac{1}{2} a+\frac{3}{4} b=1</equation>从而 2a+3b=4.应选A.

---


### 随机事件和概率

**2025年第16题 | 填空题 | 5分**

16. 设 A,B,C 为三个随机事件，且 A 与 B 相互独立，B 与 C 相互独立，A 与 C 互不相容，已知<equation>P ( A )=P ( C )=\frac{1}{4},</equation><equation>P ( B )=\frac{1}{2}</equation>，则在事件 A,B,C 至少有一个发生的条件下，A,B,C 中恰有一个发生的概率为___

**解析:**解 由 A与B相互独立，B与C相互独立可得<equation>P ( A B )=P ( A ) P ( B ) , P ( B C )=P ( B ) P ( C ).</equation>由 A与C互不相容可得<equation>A \cap C=\varnothing</equation>由此可得<equation>P ( A C)=0.</equation>所求概率为<equation>P ( A \overline{B} \overline{C} \cup \overline{A} \overline{B} \overline{C} \cup \overline{A} \overline{B} C \mid A \cup B \cup C).</equation>根据条件概率公式，<equation>P \left(A \bar {B} \bar {C} \cup \bar {A} B \bar {C} \cup \bar {A} \bar {B} C \mid A \cup B \cup C\right) = \frac {P \left[ \left(A \bar {B} \bar {C} \cup \bar {A} B \bar {C} \cup \bar {A} \bar {B} C\right) \cap \left(A \cup B \cup C\right) \right]}{P \left(A \cup B \cup C\right)}.</equation>由于<equation>A\overline{B}\overline{C},\overline{A}B\overline{C},\overline{A}\overline{B}C</equation>均包含于<equation>A\cup B\cup C</equation>，故<equation>P \left[ \left(A \bar {B} \bar {C} \cup \bar {A} B \bar {C} \cup \bar {A} \bar {B} C\right) \cap (A \cup B \cup C) \right] = P \left(A \bar {B} \bar {C} \cup \bar {A} B \bar {C} \cup \bar {A} \bar {B} C\right).</equation>又因为这三个事件互不相容，故<equation>P \left(A \bar {B} \bar {C} \cup \bar {A} B \bar {C} \cup \bar {A} \bar {B} C\right) = P \left(A \bar {B} \bar {C}\right) + P \left(\bar {A} B \bar {C}\right) + P \left(\bar {A} \bar {B} C\right).</equation>由<equation>A \cap C = \varnothing</equation>可得<equation>A \subseteq \overline{C}, C \subseteq \overline{A}</equation>，于是<equation>A\overline{B}\overline{C} = A\overline{B},\overline{A}\overline{B}C = \overline{B}C.</equation>进一步可得<equation>P \left(A \bar {B} \bar {C}\right) = P \left(A \bar {B}\right) \stackrel {\mathrm {独立 性}} {=} P (A) P (\bar {B}) = \frac {1}{4} \cdot \frac {1}{2} = \frac {1}{8},</equation><equation>P (\bar {A} \bar {B} C) = P (\bar {B} C) \stackrel {\text {独立 性}} {=} P (\bar {B}) P (C) = \frac {1}{2} \cdot \frac {1}{4} = \frac {1}{8}.</equation>此外，<equation>\begin{aligned} P (\bar {A} B \bar {C}) &= P [ B \cap (\overline {{A \cup C}}) ] = P (B) - P [ B \cap (A \cup C) ] = P (B) - P (A B \cup B C) \\ &= P (B) - P (A B) - P (B C) \xlongequal {\text {独立性}} P (B) - P (A) P (B) - P (B) P (C) \\ &= P (B) [ 1 - P (A) - P (C) ] = \frac {1}{2} \cdot \frac {1}{2} = \frac {1}{4}. \end{aligned}</equation><equation>\begin{aligned} P (A \cup B \cup C) &= P (A) + P (B) + P (C) - P (A B) - P (B C) - P (A C) + P (A B C) \\ \frac {P (A C) = 0}{P (A B C) = 0} P (A) + P (B) + P (C) - P (A) P (B) - P (B) P (C) \\ &= \frac {1}{4} + \frac {1}{2} + \frac {1}{4} - \frac {1}{4} \cdot \frac {1}{2} - \frac {1}{2} \cdot \frac {1}{4} = \frac {3}{4}. \end{aligned}</equation>结合（1）式，（2）式可得<equation>P \left(A \bar {B} \bar {C} \cup \bar {A} B \bar {C} \cup \bar {A} \bar {B} C \mid A \cup B \cup C\right) = \left(\frac {1}{8} + \frac {1}{4} + \frac {1}{8}\right) / \frac {3}{4} = \frac {2}{3}.</equation>

---

**2022年第16题 | 填空题 | 5分**

16. 设 A,B,C为随机事件，且 A与B互不相容，A与C互不相容，B与C相互独立，<equation>P ( A )=P ( B )=P ( C )=\frac{1}{3}</equation>，则<equation>P ( B \cup C \mid A \cup B \cup C )=</equation>___

**答案:**## 5 8.

**解析:**由于 A，B互不相容，A，C互不相容，B，C相互独立，故<equation>P (A B) = 0, \quad P (A C) = 0, \quad P (B C) = P (B) P (C) = \frac {1}{9}, \quad P (A B C) = 0.</equation>由条件概率公式，<equation>\begin{aligned} P (B \cup C \mid A \cup B \cup C) &= \frac {P [ (B \cup C) \cap (A \cup B \cup C) ]}{P (A \cup B \cup C)} = \frac {P (B \cup C)}{P (A \cup B \cup C)} \\ &= \frac {P (B) + P (C) - P (B C)}{P (A) + P (B) + P (C) - P (A B) - P (B C) - P (A C) + P (A B C)} \\ &= \frac {\frac {1}{3} + \frac {1}{3} - \frac {1}{9}}{\frac {1}{3} + \frac {1}{3} + \frac {1}{3} - \frac {1}{9}} = \frac {5}{8}. \end{aligned}</equation>

---

**2021年第8题 | 选择题 | 5分 | 答案: D**

8. 设 A,B为随机事件，且<equation>0 < P ( B ) < 1</equation>，下列命题中为假命题的是（    )

A. 若<equation>P ( A \mid B )=P ( A )</equation>，则<equation>P ( A \mid \bar{B})=P ( A )</equation>B. 若<equation>P ( A \mid B )>P ( A )</equation>，则<equation>P ( \bar{A} \mid \bar{B})>P ( \bar{A} )</equation>C. 若<equation>P ( A \mid B )>P ( A \mid \bar{B})</equation>，则<equation>P ( A \mid B )>P ( A )</equation>D. 若<equation>P ( A \mid A \cup B )>P ( \bar{A} \mid A \cup B)</equation>，则<equation>P ( A )>P ( B )</equation>

答案: D

**解析:**解 考虑选项 D.<equation>P (A \mid A \cup B) = \frac {P (A \cap (A \cup B))}{P (A \cup B)} = \frac {P (A)}{P (A) + P (B) - P (A B)},</equation><equation>P (\bar {A} \mid A \cup B) = \frac {P (\bar {A} \cap (A \cup B))}{P (A \cup B)} = \frac {P (\bar {A} B)}{P (A) + P (B) - P (A B)} = \frac {P (B) - P (A B)}{P (A) + P (B) - P (A B)}.</equation>若<equation>P(A \mid A \cup B) > P(\overline{A} \mid A \cup B)</equation>，则<equation>P(A) > P(B) - P(AB)</equation>.但这并不能保证<equation>P(A) > P(B)</equation>.由此出发考虑选项D的反例.例如：<equation>A = B</equation>，则<equation>P(A \mid A \cup B) = 1 > 0 = P(\overline{A} \mid A \cup B)</equation>，但<equation>P(A) = P(B)</equation>.

因此，应选D.

下面说明选项A、B、C不正确.

选项A：由于<equation>P ( A )=P ( A \mid B)=\frac{P ( A B)}{P ( B)},</equation>故<equation>P ( A B)=P ( A ) P ( B ),</equation>从而A,B独立.由A,B独立可得A，<equation>\overline{B}</equation>独立，故<equation>P ( A \mid \overline{B})=P ( A ).</equation>选项A成立.

选项B：若<equation>P ( A \mid B ) > P ( A )</equation>，即<equation>\frac{P ( A B )}{P ( B )} > P ( A )</equation>，则<equation>P ( A B ) > P ( A ) P ( B ).</equation><equation>\begin{aligned} P (\bar {A} \mid \bar {B}) &= \frac {P (\bar {A} \bar {B})}{P (\bar {B})} = \frac {1 - P (A \cup B)}{1 - P (B)} = \frac {1 - P (A) - P (B) + P (A B)}{1 - P (B)} \\ > \frac {1 - P (A) - P (B) + P (A) P (B)}{1 - P (B)} &= 1 - P (A) = P (\bar {A}). \end{aligned}</equation>选项B成立.

选项C：若<equation>P ( A \mid B ) > P ( A \mid \overline{B} )</equation>，即<equation>\frac{P ( A B )}{P ( B )} >\frac{P ( A B )}{P (\overline{B})}</equation>，则<equation>\frac{P ( A B )}{P ( B )} >\frac{P ( A )-P ( A B )}{1-P ( B )}</equation>.由此可得<equation>P ( A B ) - P ( B ) P ( A B ) > P ( A ) P ( B ) - P ( B ) P ( A B )</equation>即<equation>P ( A B ) > P ( A ) P ( B )</equation>于是，<equation>P ( A ) < \frac { P ( A B ) } { P ( B ) } = P ( A \mid B )</equation>. 选项C成立.

---

**2020年第7题 | 选择题 | 4分 | 答案: D**

7. 设 A,B,C为三个随机事件，且<equation>P ( A )=P ( B )=P ( C )=\frac{1}{4}, P ( A B )=0, P ( A C )=P ( B C )=\frac{1}{1 2}</equation>，则 A,B,C中恰有一个事件发生的概率为（    ）

A.<equation>\frac{3}{4}</equation>B.<equation>\frac{2}{3}</equation>C.<equation>\frac{1}{2}</equation>D.<equation>\frac{5}{12}</equation>

答案: D

**解析:**解（法一）设A,B,C中恰有一个事件发生的概率为 p. P（A<equation>\cup</equation>B<equation>\cup</equation>C）为至少发生一个事件的概率. “至少发生一个”可拆分为“恰好发生一个”，“至少发生两个”这样两个互不相容事件.于是，<equation>P (A \cup B \cup C) = p + P (A B \cup B C \cup A C).</equation>由 P（AB）=0可得 P（ABC）=0.由三个事件的加法公式可得<equation>\begin{aligned} P (A \cup B \cup C) &= P (A) + P (B) + P (C) - P (A B) - P (B C) - P (A C) + P (A B C) \\ &= \frac {1}{4} + \frac {1}{4} + \frac {1}{4} - 0 - \frac {1}{1 2} - \frac {1}{1 2} + 0 = \frac {7}{1 2}. \end{aligned}</equation><equation>\begin{aligned} P (A B \cup B C \cup A C) &= P (A B) + P (B C) + P (A C) - P (A B C) - P (A B C) + P (A B C) \\ &= 0 + \frac {1}{1 2} + \frac {1}{1 2} + 0 = \frac {1}{6}. \end{aligned}</equation>从而，<equation>p=\frac{7}{12}-\frac{1}{6}=\frac{5}{12}.</equation>因此，应选D.

（法二）<equation>A,B,C</equation>中恰有一个事件发生的概率为<equation>p=P(A\overline{B}\overline{C})+P(\overline{A}B\overline{C})+P(\overline{A}\overline{B}C).</equation><equation>P \left(A \bar {B} \bar {C}\right) = P \left(A \bar {B}\right) - P \left(A \bar {B} C\right) = P (A) - P (A B) - \left[ P (A C) - P (A C B) \right],</equation><equation>P (\bar {A} B \bar {C}) = P (\bar {A} B) - P (\bar {A} B C) = P (B) - P (A B) - [ P (B C) - P (B C A) ],</equation><equation>P (\bar {A} \bar {B} C) = P (\bar {B} C) - P (\bar {B} C A) = P (C) - P (C B) - [ P (C A) - P (C A B) ].</equation>由<equation>P ( A B ) = 0</equation>可得<equation>P ( A B C ) = 0.</equation>因此，<equation>p = P (A) + P (B) + P (C) - 2 \left[ P (A B) + P (B C) + P (A C) \right] = \frac {3}{4} - 4 \times \frac {1}{1 2} = \frac {5}{1 2}.</equation>应选 D.

---

**2019年第7题 | 选择题 | 4分 | 答案: C**

7. 设 A,B为随机事件，则<equation>P ( A )=P ( B )</equation>的充分必要条件是（    )

A.<equation>P ( A \cup B )=P ( A )+P ( B )</equation>B.<equation>P ( A B )=P ( A ) P ( B )</equation>C.<equation>P ( A \bar{B} )=P ( B \bar{A} )</equation>D.<equation>P ( A B )=P ( \bar{A} \bar{B} )</equation>

答案: C

**解析:**解 由于<equation>A\overline{B}=A-A\cap B, B\overline{A}=B-B\cap A</equation>，故<equation>P(A\overline{B})=P(A)-P(AB), P(B\overline{A})= P(B)-P(AB).</equation>因此，<equation>P ( A )=P ( B )</equation>等价于<equation>P ( A \overline{B} )=P ( B \overline{A} ).</equation>应选C.

下面说明选项A、B、D不正确.

取<equation>A = B</equation>，且<equation>P(A) = P(B) = \frac{1}{3}</equation>.

选项 A：<equation>P ( A \cup B )=P ( A )=\frac{1}{3}, P ( A )+P ( B )=\frac{2}{3}.</equation>选项A不是<equation>P ( A )=P ( B )</equation>的必要条件.

选项B：<equation>P ( A B )=P ( A )=\frac{1}{3}, P ( A ) P ( B )=\frac{1}{9}.</equation>选项B不是<equation>P ( A )=P ( B )</equation>的必要条件.

选项 D：<equation>P ( A B )=P ( A )=\frac{1}{3}, P (\overline{A}\overline{B})=P(\overline{A})=\frac{2}{3}.</equation>选项 D不是<equation>P ( A )=P ( B )</equation>的必要条件.

---

**2018年第14题 | 填空题 | 4分**

14. 随机事件 A,B,C 相互独立，且<equation>P ( A )=P ( B )=P ( C )=\frac{1}{2}</equation>，则<equation>P ( A C \mid A \cup B )=</equation>___.

**答案:**# 1 3.

**解析:**根据事件运算的分配律，<equation>P (A C \cap (A \cup B)) = P ((A C \cap A) \cup (A C \cap B)) = P (A C \cup A B C) = P (A C).</equation>根据和事件的概率公式，<equation>P ( A \cup B ) = P ( A ) + P ( B ) - P ( A B ) .</equation>根据条件概率的计算公式，<equation>\begin{aligned} P (A C \mid A \cup B) &= \frac {P (A C \cap (A \cup B))}{P (A \cup B)} = \frac {P (A C)}{P (A) + P (B) - P (A B)} \\ \frac {\mathrm {独立 性}}{} \frac {P (A) P (C)}{P (A) + P (B) - P (A) P (B)} &= \frac {\frac {1}{2} \times \frac {1}{2}}{\frac {1}{2} + \frac {1}{2} - \frac {1}{2} \times \frac {1}{2}} = \frac {1}{3}. \end{aligned}</equation>

---

**2017年第7题 | 选择题 | 4分 | 答案: C**

7. 设 A,B,C为三个随机事件，且 A与 C相互独立，B与 C相互独立，则 A<equation>\cup</equation>B与 C相互独立的充分必要条件是（    ）

A. A与B相互独立 B. A与B互不相容 C. AB与C相互独立 D. AB与C互不相容

答案: C

**解析:**由已知条件知，<equation>P ( A C ) = P ( A ) P ( C )</equation><equation>P ( B C ) = P ( B ) P ( C )</equation>计算 P（（AUB）<equation>\cap C ）</equation>，得<equation>\begin{aligned} P ((A \cup B) \cap C) &= P ((A \cap C) \cup (B \cap C)) \\ &= P (A \cap C) + P (B \cap C) - P ((A \cap C) \cap (B \cap C)) \\ &= P (A C) + P (B C) - P (A \cap B \cap C) \\ &= P (A) P (C) + P (B) P (C) - P (A \cap B \cap C). \end{aligned}</equation>另一方面，事件 A U B与事件 C相互独立等价于<equation>\begin{aligned} P ((A \cup B) \cap C) &= P (A \cup B) P (C) = [ P (A) + P (B) - P (A B) ] P (C) \\ &= P (A) P (C) + P (B) P (C) - P (A B) P (C). \end{aligned}</equation>因此，事件 A<equation>\cup</equation>B与事件 C相互独立等价于<equation>P ( A B ) P ( C )=P ( A \cap B \cap C )=P ( A B C )</equation>即事件 AB与事件 C相互独立.应选C.

---

**2016年第7题 | 选择题 | 4分 | 答案: A**

7. 设 A,B为两个随机事件，且<equation>0 < P ( A ) < 1, 0 < P ( B ) < 1</equation>，如果<equation>P ( A \mid B )=1</equation>，则（    ）

A.<equation>P ( \bar{B} \mid \bar{A})=1</equation>B.<equation>P ( A \mid \bar{B})=0</equation>C.<equation>P ( A \cup B )=1</equation>D.<equation>P ( B \mid A )=1</equation>

答案: A

**解析:**解 由题设知，<equation>P ( A \mid B ) = \frac { P ( A B ) } { P ( B ) } = 1.</equation>于是<equation>P ( A B ) = P ( B ).</equation>因此，<equation>P (A \cup B) = P (A) + P (B) - P (A B) \xlongequal {P (A B) = P (B)} P (A),</equation><equation>P (\bar {B} \mid \bar {A}) = \frac {P (\bar {B} \bar {A})}{P (\bar {A})} = \frac {P (\overline {{A \cup B}})}{P (\bar {A})} = \frac {1 - P (A \cup B)}{1 - P (A)} = \frac {1 - P (A)}{1 - P (A)} = 1,</equation><equation>P (A \mid \bar {B}) = \frac {P \left(A \bar {B}\right)}{P (\bar {B})} = \frac {P (A) - P (A B)}{P (\bar {B})} = \frac {P (A) - P (B)}{1 - P (B)},</equation><equation>P (B \mid A) = \frac {P (B A)}{P (A)} = \frac {P (B)}{P (A)}.</equation>综上所述，选项A正确.应选A.

也可以如下举反例说明选项B、C、D均不正确.

设<equation>B\subseteq A</equation>，<equation>P(A) = \frac{1}{2}</equation>，<equation>P(B) = \frac{1}{4}</equation>，则<equation>P(A\mid \overline{B}) = \frac{1}{3}</equation>，<equation>P(A\cup B) = \frac{1}{2}</equation>，<equation>P(B\mid A) = \frac{1}{2}</equation>.

---

**2016年第14题 | 填空题 | 4分**

14. 设袋中有红、白、黑球各1个，从中有放回地取球，每次取1个，直到三种颜色的球都取到时停止，则取球次数恰好为4的概率为___

**解析:**解（法一）由于第4次取到的球可以为红、白、黑球中的任一种，故第4次取球有<equation>C_{3}^{1}</equation>种可能的情况.第4次取球的颜色固定后，前三次取球只剩下两种颜色可选，且两种颜色的球都要被取到.于是在前三次取球中，一定有两次取到剩下某一种颜色的球，有一次取到剩下的另一种颜色的球，从而前三次取球有<equation>C_{2}^{1}\cdot C_{3}^{2}</equation>种可能的情况.

因此，取球次数恰好为4的情况共有<equation>\mathrm{C}_{3}^{1}\cdot \mathrm{C}_{2}^{1}\cdot \mathrm{C}_{3}^{2}</equation>种，取球次数恰好为4的概率为<equation>\frac{\mathrm{C}_{3}^{1}\cdot \mathrm{C}_{2}^{1}\cdot \mathrm{C}_{3}^{2}}{3^{4}}=\frac{2}{9}.</equation>满足题设条件的取球情况如下表.

<table border="1"><tr><td>第4次取球</td><td colspan="3">前三次取球</td></tr><tr><td rowspan="2">红</td><td>白白黑</td><td>白黑白</td><td>黑白白</td></tr><tr><td>黑黑白</td><td>黑白黑</td><td>白黑黑</td></tr><tr><td rowspan="2">白</td><td>红红黑</td><td>红黑红</td><td>黑红红</td></tr><tr><td>黑黑红</td><td>黑红黑</td><td>红黑黑</td></tr><tr><td rowspan="2">黑</td><td>红红白</td><td>红白红</td><td>白红红</td></tr><tr><td>白白红</td><td>白红白</td><td>红白白</td></tr></table>

（法二）因为恰好四次便可取完三种颜色的球，所以前三次中一定有同一颜色的球取了两次.前三次中任取两次共有<equation>C_{3}^{2}</equation>种情况，这两次选取的颜色共有<equation>C_{3}^{1}</equation>种情况；前三次中剩下的一次取剩下的两种颜色中的一种，共<equation>C_{2}^{1}</equation>种情况；前三次的球选好后，第四次的球只剩一种选择.因此，共有<equation>C_{3}^{2}\cdot C_{3}^{1}\cdot C_{2}^{1}</equation>种情况，所求概率为<equation>\frac{C_{3}^{2}\cdot C_{3}^{1}\cdot C_{2}^{1}}{3^{4}}=\frac{2}{9}.</equation>

---

**2015年第7题 | 选择题 | 4分 | 答案: C**

7. 若 A,B为任意两个随机事件，则（    ）

A.<equation>P ( A B ) \leqslant P ( A ) P ( B )</equation>B.<equation>P ( A B ) \geqslant P ( A ) P ( B )</equation>C.<equation>P ( A B ) \leqslant \frac { P ( A ) + P ( B ) } { 2 }</equation>D.<equation>P ( A B ) \geqslant \frac { P ( A ) + P ( B ) } { 2 }</equation>

答案: C

**解析:**由于<equation>A\cap B\subseteq A,A\cap B\subseteq B</equation>，故<equation>P (A B) \leqslant P (A), \quad P (A B) \leqslant P (B).</equation>因此，<equation>2 P ( A B ) \leqslant P ( A ) + P ( B )</equation>，即<equation>P ( A B ) \leqslant \frac { P ( A ) + P ( B ) } { 2 }</equation>.应选C.

下面我们说明选项 A、B、D不正确.

选项A：若 B<equation>\subseteq A</equation>，0 < P(A) < 1，0 < P(B) < 1<equation>，则 P ( A B ) = P ( A \cap B ) = P ( B ) > P ( A ) P ( B )</equation>因此选项A不正确.

选项B、D：若 P(A）>0，P(B）>0且 A<equation>\cap</equation>B=<equation>\varnothing</equation>，则 P(AB）=P（A<equation>\cap</equation>B）=0<P(A)P(B)<equation>P(AB)<\frac{P(A)+P(B)}{2}</equation>因此选项B和选项D不正确.

---

**2014年第7题 | 选择题 | 4分 | 答案: B**

7. 设随机事件 A与 B相互独立，且<equation>P ( B )=0. 5, P ( A-B)=0. 3</equation>，则<equation>P ( B-A )=</equation>(    )

A. 0.1 B. 0.2 C. 0.3 D. 0.4

答案: B

**解析:**（法一）由 A与B相互独立知，<equation>P ( A B ) = P ( A ) P ( B ).</equation>.于是，<equation>P (A - B) = P (A) - P (A B) = P (A) - P (A) P (B) = P (A) [ 1 - P (B) ] = 0. 5 P (A).</equation>从而<equation>P ( A ) = 2 P ( A - B ) = 0. 6.</equation>进一步可得，<equation>P (B - A) = P (B) - P (A B) = P (B) - P (A) P (B) = 0. 5 - 0. 6 \times 0. 5 = 0. 2.</equation>应选B.

（法二）由<equation>A</equation>与<equation>B</equation>相互独立知，<equation>A, \bar{B}</equation>也相互独立.于是，<equation>0. 3 = P (A - B) = P (A \cap \bar {B}) = P (A \bar {B}) = P (A) P (\bar {B}) = 0. 5 P (A).</equation>因此，<equation>P ( A ) = 0. 6.</equation>进一步可得，<equation>P (B - A) = P \left(B \bar {A}\right) = P (B) P (\bar {A}) = 0. 5 \times (1 - 0. 6) = 0. 2.</equation>应选B.

---

**2012年第14题 | 填空题 | 4分**

14. 设 A,B,C是随机事件，A与C互不相容，<equation>P ( A B )=\frac{1} {2}, P ( C )=\frac{1} {3}</equation>，则<equation>P ( A B \mid \bar{C})=</equation>___

**答案:**# 3 4.

**解析:**解 由条件概率的定义可知，<equation>P ( A B \mid \bar{C})=\frac{P ( A B \bar{C})}{P (\bar{C})}=\frac{P ( A B \bar{C})}{1-P(C)}.</equation>又由于 A与C互不相容，即<equation>A \cap C=\varnothing</equation>，故<equation>A \cap B \subseteq A \subseteq \bar{C}</equation>，从而<equation>A \cap B \cap \bar{C}=A \cap B, P ( A B \bar{C})=P ( A B ).</equation>因此，<equation>P ( A B \mid \bar{C})=\frac{P ( A B \bar{C})}{1-P(C)}=\frac{P ( A B)}{1-P(C)}=\frac{\frac{1}{2}}{1-\frac{1}{3}}=\frac{3}{4}.</equation>

---

**2009年第7题 | 选择题 | 4分 | 答案: D**

7. 设事件 A与事件 B互不相容，则（    ）

A.<equation>P(\bar{A}\bar{B})=0</equation>B.<equation>P(AB)=P(A)P(B)</equation>C.<equation>P(A)=1-P(B)</equation>D.<equation>P(\bar{A}\cup\bar{B})=1</equation>

答案: D

**解析:**解 由于事件 A与事件 B互不相容，故<equation>A \cap B=\varnothing</equation>.又因为<equation>\overline{A}\cup \overline{B}=\overline{A\cap B}</equation>，所以<equation>P(\overline{A}\cup \overline{B})= P(\overline{A\cap B})=1-P(AB)=1-0=1.</equation>应选 D.

下面我们分别说明选项A、B、C不正确.

由于<equation>\overline{A}\cap \overline{B}=\overline{A\cup B}</equation>，故<equation>P(\overline{A}\overline{B})=P(\overline{A\cup B})=1-P(A\cup B).</equation>当<equation>P(A\cup B)\neq 1</equation>时，<equation>P(\overline{A}\overline{B})\neq 0.</equation>选项A不正确.

若<equation>P ( A ) \neq 0</equation>且<equation>P ( B ) \neq 0</equation>，则<equation>P ( A B ) = 0 \neq P ( A ) P ( B ).</equation>选项B不正确.

由于<equation>A \cap B = \varnothing</equation>，即<equation>A \subseteq \overline{B}</equation>，故<equation>P(A) \leqslant P(\overline{B}) = 1 - P(B)</equation>.选项C不正确.

---


### 多维随机变量及其分布


#### 边缘分布与条件分布

**2025年第22题 | 解答题 | 12分**

22. 投保人的损失事件发生时，保险公司的赔付额 Y与投保人的损失额 X的关系为<equation>Y=\left\{\begin{array}{ll}0,&X\leqslant 100\\ X-100,&X>100\end{array} \right.</equation>. 设定损事件发生时，投保人的损失额 X的概率密度为<equation>f(x)=\left\{\begin{array}{ll}\frac{2\times 100^{2}}{(100+x)^{3}},&x>0\\ 0,&x\leqslant 0\end{array} \right.</equation>I. 求<equation>P\{Y>0\}</equation>及 EY.

Ⅱ. 这种损失事件在一年内发生的次数记为 N，保险公司在一年内就这种损失事件产生的理赔次数记为 M，假设 N服从参数为8的泊松分布，在<equation>N=n</equation>（<equation>n\geqslant1</equation>）的条件下，M服从二项分布<equation>B(n,p)</equation>，其中<equation>p=P\{Y>0\}</equation>，求 M的概率分布.

**答案:**（I）<equation>P \left\{Y > 0\right\}=\frac{1}{4}, E (Y)=50;</equation>（Ⅱ）M服从参数为2的泊松分布.

**解析:**解（I）根据 Y的定义，<equation>\begin{aligned} P \{Y > 0 \} &= P \{X > 1 0 0 \} = \int_ {1 0 0} ^ {+ \infty} f (x) \mathrm {d} x = \int_ {1 0 0} ^ {+ \infty} \frac {2 \times 1 0 0 ^ {2}}{(1 0 0 + x) ^ {3}} \mathrm {d} x = - \frac {2 \times 1 0 0 ^ {2}}{2} (1 0 0 + x) ^ {- 2} \Bigg | _ {1 0 0} ^ {+ \infty} \\ &= - \frac {1 0 0 ^ {2}}{(1 0 0 + x) ^ {2}} \Bigg | _ {1 0 0} ^ {+ \infty} = \frac {1}{4}. \end{aligned}</equation>由于随机变量<equation>Y</equation>是随机变量<equation>X</equation>的函数，故根据数学期望的定义，<equation>\begin{aligned} E (Y) &= 0 \cdot P \{Y = 0 \} + \int_ {1 0 0} ^ {+ \infty} (x - 1 0 0) f (x) \mathrm {d} x = \int_ {1 0 0} ^ {+ \infty} \frac {2 \times 1 0 0 ^ {2} (x - 1 0 0)}{\left(1 0 0 + x\right) ^ {3}} \mathrm {d} x \\ &= - 1 0 0 ^ {2} \int_ {1 0 0} ^ {+ \infty} (x - 1 0 0) \mathrm {d} \left[ (1 0 0 + x) ^ {- 2} \right] = - 1 0 0 ^ {2} \left[ \frac {x - 1 0 0}{(1 0 0 + x) ^ {2}} \right| _ {1 0 0} ^ {+ \infty} - \int_ {1 0 0} ^ {+ \infty} \frac {\mathrm {d} x}{(1 0 0 + x) ^ {2}} ] \\ &= \frac {- 1 0 0 ^ {2}}{1 0 0 + x} \Bigg | _ {1 0 0} ^ {+ \infty} = 0 - \left(- \frac {1 0 0 ^ {2}}{2 0 0}\right) = 5 0. \end{aligned}</equation>（Ⅱ）由于<equation>N</equation>服从参数为8的泊松分布，故<equation>P\{N = n\} = \frac{8^n\mathrm{e}^{-8}}{n!}</equation>，进一步可得<equation>P\{N = 0\} = \mathrm{e}^{-8}</equation>由于当<equation>N = 0</equation>时，<equation>M</equation>必然等于0，故<equation>P\{M = 0\mid N = 0\} = 1</equation>，从而<equation>P \{M = 0, N = 0 \} = P \{M = 0 \mid N = 0 \} P \{N = 0 \} = 1 \cdot P \{N = 0 \} = \mathrm {e} ^ {- 8}.</equation>由 M的定义可知，当<equation>M=k</equation>时，<equation>N=n\geqslant k</equation>由在<equation>N=n(n\geqslant 1)</equation>的条件下，M服从二项分布 B(n,p）可得，<equation>P \left\{M = k \mid N = n \right\} = \mathrm {C} _ {n} ^ {k} p ^ {k} (1 - p) ^ {n - k}, \quad k = 0, 1, \dots , n, n = 1, 2, \dots .</equation>由条件概率公式以及<equation>p=\frac{1}{4}</equation>可得<equation>\begin{aligned} P \{M = k, N = n \} &= P \{M = k \mid N = n \} P \{N = n \} = C _ {n} ^ {k} p ^ {k} (1 - p) ^ {n - k} \frac {8 ^ {n} \mathrm {e} ^ {- 8}}{n !} \\ &= \frac {n !}{k ! (n - k) !} \cdot \left(\frac {1}{4}\right) ^ {k} \cdot \left(\frac {3}{4}\right) ^ {n - k} \cdot \frac {8 ^ {n} \mathrm {e} ^ {- 8}}{n !} = \frac {3 ^ {n - k} 2 ^ {n} \mathrm {e} ^ {- 8}}{k ! (n - k) !} \\ &= \frac {6 ^ {n - k} 2 ^ {k} \mathrm {e} ^ {- 8}}{k ! (n - k) !}. \end{aligned}</equation>由此可得，当<equation>k\neq 0</equation>时，<equation>\begin{aligned} P \{M = k \} &= \sum_ {n = k} ^ {\infty} P \{M = k, N = n \} = \sum_ {n = k} ^ {\infty} \frac {6 ^ {n - k} 2 ^ {k} \mathrm {e} ^ {- 8}}{k ! (n - k) !} = \frac {2 ^ {k} \mathrm {e} ^ {- 2}}{k !} \sum_ {n = k} ^ {\infty} \frac {6 ^ {n - k} \mathrm {e} ^ {- 6}}{(n - k) !} \\ &= \frac {2 ^ {k} \mathrm {e} ^ {- 2}}{k !} \sum_ {n = 0} ^ {\infty} \frac {6 ^ {n} \mathrm {e} ^ {- 6}}{n !}. \end{aligned}</equation><equation>\begin{aligned} P \{M = 0 \} &= \sum_ {n = 0} ^ {\infty} P \{M = 0, N = n \} = \mathrm {e} ^ {- 8} + \sum_ {n = 1} ^ {\infty} P \{M = 0, N = n \} = \mathrm {e} ^ {- 8} + \sum_ {n = 1} ^ {\infty} \frac {6 ^ {n} \mathrm {e} ^ {- 6}}{n !} \cdot \mathrm {e} ^ {- 2} \\ &= \mathrm {e} ^ {- 2} \sum_ {n = 0} ^ {\infty} \frac {6 ^ {n} \mathrm {e} ^ {- 6}}{n !}. \end{aligned}</equation>由泊松分布的定义可知，服从参数为6的泊松分布的随机变量Z的分布律为<equation>P\{Z = n\} = \frac{6^{n}\mathrm{e}^{-6}}{n!}</equation>.由分布律的性质可得，<equation>\sum_{n = 0}^{\infty}\frac{6^{n}\mathrm{e}^{-6}}{n!} = 1.</equation>于是，<equation>P\{M = k\} = \frac{2^{k}\mathrm{e}^{-2}}{k!},k = 0,1,2,\dots .</equation>因此，M服从参数为2的泊松分布

---

**2013年第22题 | 解答题 | 11分**


设 (X,Y)是二维随机变量，X的边缘概率密度为<equation>f_{X}(x)=\left\{ \begin{array}{ll} 3x^{2}, & 0<x<1, \\ 0, & \text{其他.} \end{array} \right.</equation>在给定 X=x(0<x<1)的条件下 Y的条件概率密度为<equation>f_{Y|X}(y\mid x)=\left\{ \begin{array}{ll} \frac{3y^{2}}{x^{3}}, & 0<y<x, \\ 0, & \text{其他.} \end{array} \right.</equation>I. 求 (X,Y)的概率密度 f(x,y);

II. 求 Y的边缘概率密度<equation>f_{Y}(y)</equation>III. 求<equation>P\{X>2Y\}</equation>

**答案:**(22) (I)<equation>f ( x,y)=\left\{\begin{array}{ll}\frac{9 y^{2}}{x},&0<y<x,0<x<1,\\ 0,&\text{其他};\end{array} \right.</equation>(Ⅱ)<equation>f_{Y}(y)=\left\{\begin{array}{ll}-9 y^{2}\ln y,&0<y<1,\\ 0,&\text{其他};\end{array} \right.</equation>(Ⅲ)<equation>\frac{1}{8}.</equation>

**解析:**解（I）当<equation>0 < x < 1</equation>时，<equation>f_{X}(x)=3x^{2},f_{Y\mid X}(y\mid x)=\frac{f(x,y)}{f_{X}(x)}=\left\{ \begin{array}{ll}\frac{3y^{2}}{x^{3}},&0<y<x,\\ 0,&\text{其他}, \end{array} \right.</equation>故当<equation>0 < x < 1</equation>时，<equation>f (x, y) = \left\{ \begin{array}{l l} \frac {9 y ^ {2}}{x}, & 0 < y < x, \\ 0, & y \leqslant 0 \text {或} y \geqslant x. \end{array} \right.</equation>下面求当<equation>x \leqslant 0</equation>或<equation>x \geqslant 1</equation>时<equation>f(x,y)</equation>的取值.

由于<equation>\int_ {0} ^ {1} \mathrm {d} x \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {x} \frac {9 y ^ {2}}{x} \mathrm {d} y = \int_ {0} ^ {1} 3 x ^ {2} \mathrm {d} x = 1,</equation>故可以认为在<equation>\left\{(x,y)\mid 0 < x < 1,-\infty < y < +\infty\right\}</equation>以外的平面上，即<equation>x\leqslant 0</equation>或<equation>x\geqslant 1</equation>时，<equation>f(x,y)=0.</equation>综上所述，<equation>(X,Y)</equation>的概率密度<equation>f(x,y) = \left\{ \begin{array}{ll}\frac{9y^2}{x}, & 0 < y < x,0 < x < 1,\\ 0, & \text{其他}. \end{array} \right.</equation>（Ⅱ）由第（I）问知<equation>Y</equation>的边缘概率密度为<equation>f _ {Y} (y) = \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} x = \left\{ \begin{array}{l l} \int_ {y} ^ {1} \frac {9 y ^ {2}}{x} \mathrm {d} x, & 0 < y < 1, \\ 0, & \text {其 他} \end{array} = \left\{ \begin{array}{l l} - 9 y ^ {2} \ln y, & 0 < y < 1, \\ 0, & \text {其 他}. \end{array} \right. \right.</equation>或者，将上述积分次序改为先对<equation>x</equation>积分，再对<equation>y</equation>积分，可得<equation>\begin{array}{l} P \left\{X > 2 Y \right\} = \iint_ {| (x, y) | x > 2 y |} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {\frac {1}{2}} \mathrm {d} y \int_ {2 y} ^ {1} \frac {9 y ^ {2}}{x} \mathrm {d} x = \int_ {0} ^ {\frac {1}{2}} \left(- 9 y ^ {2} \ln 2 y\right) \mathrm {d} y \\ = - 3 y ^ {3} \ln 2 y \left| _ {0} ^ {\frac {1}{2}} + \int_ {0} ^ {\frac {1}{2}} \frac {6 y ^ {3}}{2 y} \mathrm {d} y = \int_ {0} ^ {\frac {1}{2}} 3 y ^ {2} \mathrm {d} y = \frac {1}{8}. \right. \\ \end{array}</equation>

---


#### 二维随机变量及其分布

**2024年第10题 | 选择题 | 5分 | 答案: D**

10. 设随机变量 X，Y相互独立，且均服从参数为<equation>\lambda</equation>的指数分布. 令<equation>Z=|X-Y|</equation>，则下列随机变量中与 Z同分布的是（    ）

A.<equation>X+Y</equation>B.<equation>\frac{X+Y}{2}</equation>C. 2X D. X

答案: D

**解析:**解 由于 X, Y相互独立，且均服从参数为<equation>\lambda</equation>的指数分布，故（X，Y）的联合概率密度为<equation>f (x, y) = \left\{ \begin{array}{l l} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)}, & x > 0, y > 0, \\ 0, & \text {其 他}. \end{array} \right.</equation>记<equation>F_{Z}(z)</equation>为<equation>Z=|X-Y|</equation>的分布函数，<equation>D_{z}=\left\{(x,y)\right|-z\leq x-y\leq z\}</equation>，则<equation>F _ {Z} (z) = P \left\{Z \leqslant z \right\} = P \left\{\left| X - Y \right| \leqslant z \right\} = P \left\{- z \leqslant X - Y \leqslant z \right\} = \iint_ {D.} f (x, y) \mathrm {d} x \mathrm {d} y.</equation>当<equation>z < 0</equation>时，<equation>D_{z} = \varnothing , F_{Z}(z) = 0.</equation>当<equation>z \geqslant 0</equation>时，记<equation>D = \{(x,y) \mid x \geqslant 0, y \geqslant 0\}</equation>，则<equation>D \cap D_z \neq \emptyset</equation>，为图（a）中的灰色区域.

(a)

(b)

下面用两种方法计算<equation>z \geqslant 0</equation>时的<equation>F_{z}(z)</equation>.

(c)

（法一）如图（a）所示，由于<equation>D \cap D_{z}</equation>关于直线<equation>y=x</equation>对称，故记其位于直线<equation>y=x</equation>下方的部分为<equation>D_{0}.</equation>将<equation>D_{0}</equation>写成Y型区域，<equation>D_{0}=\left|(x,y)\right| \mid y \leqslant x \leqslant y+z,0 \leqslant y < +\infty \mid.</equation><equation>\begin{array}{l} F _ {z} (z) = \iint_ {D _ {z}} f (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {D \cap D _ {z}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y \xlongequal {\text {轮 换 对称 性}} 2 \iint_ {D _ {0}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y \\ = 2 \lambda^ {2} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \mathrm {d} y \int_ {y} ^ {y + z} \mathrm {e} ^ {- \lambda x} \mathrm {d} x = - 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \cdot \mathrm {e} ^ {- \lambda x} \Bigg | _ {x = y} ^ {x = y + z} \mathrm {d} y \\ = - 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \left(\mathrm {e} ^ {- \lambda y - \lambda z} - \mathrm {e} ^ {- \lambda y}\right) \mathrm {d} y = - 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- 2 \lambda y} \left(\mathrm {e} ^ {- \lambda z} - 1\right) \mathrm {d} y \\ = \left(\mathrm {e} ^ {- \lambda z} - 1\right) \int_ {0} ^ {+ \infty} \left(- 2 \lambda \mathrm {e} ^ {- 2 \lambda y}\right) \mathrm {d} y = \left(\mathrm {e} ^ {- \lambda z} - 1\right) \mathrm {e} ^ {- 2 \lambda y} \Bigg | _ {0} ^ {+ \infty} \\ = \left(\mathrm {e} ^ {- \lambda z} - 1\right) \cdot (- 1) = 1 - \mathrm {e} ^ {- \lambda z}. \\ \end{array}</equation>（法二）如图（b）所示，<equation>D_{1}=D\backslash D_{z}</equation>关于直线<equation>y=x</equation>对称，记其位于直线<equation>y=x</equation>下方的部分为<equation>D_{2}.</equation>将<equation>D_{2}</equation>写成Y型区域，<equation>D_{2}=\{(x,y)\mid y+z\leqslant x<+\infty ,0\leqslant y<+\infty \}.</equation><equation>\begin{array}{l} F _ {Z} (z) = \iint_ {D _ {z}} f (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {D \cap D _ {z}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y = 1 - \iint_ {D _ {1}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y \\ \underline {{\text {轮换 对称性}}} 1 - 2 \iint_ {D _ {2}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y = 1 - 2 \lambda^ {2} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \mathrm {d} y \int_ {y + z} ^ {+ \infty} \mathrm {e} ^ {- \lambda x} \mathrm {d} x \\ = 1 + 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \cdot \mathrm {e} ^ {- \lambda x} \Bigg | _ {x = y + z} ^ {+ \infty} \mathrm {d} y = 1 - 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \cdot \mathrm {e} ^ {- \lambda (y + z)} \mathrm {d} y \\ = 1 - 2 \lambda \mathrm {e} ^ {- \lambda z} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- 2 \lambda y} \mathrm {d} y = 1 + \mathrm {e} ^ {- \lambda z} \cdot \mathrm {e} ^ {- 2 \lambda y} \Bigg | _ {0} ^ {+ \infty} = 1 - \mathrm {e} ^ {- \lambda z}. \\ \end{array}</equation>因此，<equation>F_{z}(z)=\left\{ \begin{array}{ll}1-\mathrm{e}^{-\lambda z},& z\geqslant 0,\\ 0,& \text{其他}, \end{array} \right. f_{z}(z)=\left\{ \begin{array}{ll}\lambda \mathrm{e}^{-\lambda z},& z\geqslant 0,\\ 0,& \text{其他}, \end{array} \right. Z</equation>服从参数为<equation>\lambda</equation>的指数分布.进一步可得，Z与X同分布.选项D正确，选项C错误.

下面说明选项A、B不正确.

对选项A，当<equation>z\geqslant 0</equation>时，由于<equation>D_{3} = \{(x,y)|x + y\leqslant z,x\geqslant 0,y\geqslant 0\}</equation>真包含于<equation>D\cap D_{z}</equation>，故<equation>X + Y</equation>的分布函数<equation>F_{1}(z)</equation>满足，对任意<equation>z > 0,F_{1}(z) < F_{Z}(z)</equation>.从而<equation>X + Y</equation>与Z不同分布.

对选项B，当<equation>z\geqslant 0</equation>时，记<equation>D_{4} = \left| (x,y)\right| x + y\leqslant 2z,x\geqslant 0,y\geqslant 0\}</equation>，则<equation>\frac{X+Y}{2}</equation>的分布函数<equation>\begin{array}{l} F _ {2} (z) = \iint_ {D _ {4}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y = \lambda^ {2} \int_ {0} ^ {2 x} \mathrm {e} ^ {- \lambda x} \mathrm {d} x \int_ {0} ^ {2 x - x} \mathrm {e} ^ {- \lambda y} \mathrm {d} y = 1 - (2 \lambda z + 1) \mathrm {e} ^ {- 2 \lambda z} \\ \neq F _ {Z} (z). \\ \end{array}</equation>从而<equation>\frac{X+Y}{2}</equation>与Z不同分布.

综上所述，应选D.

---

**2020年第8题 | 选择题 | 4分 | 答案: C**

8. 设随机变量（X，Y）服从二维正态分布<equation>N \left( 0,0;1,4;-\frac{1}{2} \right)</equation>，则下列随机变量中服从标准正态分布且与 X相互独立的是（    )

A.<equation>\frac{\sqrt{5}}{5} ( X+Y )</equation>B.<equation>\frac{\sqrt{5}}{5} ( X-Y )</equation>C.<equation>\frac{\sqrt{3}}{3} ( X+Y )</equation>D.<equation>\frac{\sqrt{3}}{3} ( X-Y )</equation>

答案: C

**解析:**解 由（X，Y）服从二维正态分布<equation>N \left( 0,0;1,4;-\frac{1}{2} \right)</equation>可知，<equation>X\sim N (0,1), Y\sim N (0,4)</equation>，且<equation>\rho_{X Y}=-\frac{1}{2}.</equation><equation>E ( X )=0,D ( X )=1,E ( Y )=0,D ( Y )=4.</equation>由此可计算<equation>\operatorname{C o v} ( X, Y ).</equation>由协方差的计算公式，可得<equation>\operatorname {C o v} (X, Y) = \rho_ {X Y} \sqrt {D (X)} \sqrt {D (Y)} = - \frac {1}{2} \times 1 \times 2 = - 1.</equation>由选项设置，分别考虑<equation>\operatorname{Cov}(X,X+Y),\operatorname{Cov}(X,X-Y)</equation>（由注可知，<equation>(X,X+Y),(X,X-Y)</equation>均服从二维正态分布）.<equation>\operatorname {C o v} (X, X + Y) = \operatorname {C o v} (X, X) + \operatorname {C o v} (X, Y) = 1 - 1 = 0.</equation><equation>\operatorname {C o v} (X, X - Y) = \operatorname {C o v} (X, X) - \operatorname {C o v} (X, Y) = 1 - (- 1) = 2.</equation>X与X-Y相关，从而不独立，故可以排除选项B、D.

又因为所求随机变量应服从标准正态分布，所以考虑将 X+Y标准化.<equation>E (X + Y) = 0, \quad D (X + Y) = D (X) + D (Y) + 2 \operatorname {C o v} (X, Y) = 1 + 4 - 2 = 3.</equation>由于<equation>D \left[ \frac{\sqrt{5}}{5} (X+Y) \right]=\frac{1}{5} D (X+Y)=\frac{3}{5} \neq 1,D \left[ \frac{\sqrt{3}}{3} (X+Y) \right]=\frac{1}{3} D (X+Y)=1</equation>，故可排除选项A，应选C.

---

**2019年第22题 | 解答题 | 11分**

2. (本题满分11分)

设随机变量 X与 Y相互独立，X服从参数为1的指数分布，Y的概率分布为<equation>P\{Y=-1\}=p,P\{Y=1\}=</equation><equation>1-p \left( 0<p<1 \right).</equation>令<equation>Z=XY</equation>.

I. 求 Z的概率密度；

II. p为何值时，X与 Z不相关；

III. X与 Z是否相互独立？

**答案:**（I）<equation>Z</equation>的概率密度为<equation>f_{Z}(z)=\left\{\begin{array}{ll}p\mathrm{e}^{z},&z\leqslant 0,\\ (1-p)\mathrm{e}^{-z},&z>0; \end{array} \right.</equation>（Ⅱ）当<equation>p=\frac{1}{2}</equation>时，X与Z不相关；

（Ⅲ）X与Z不相互独立.

**解析:**（I）先计算 Z的分布函数<equation>F_{Z}(z).</equation><equation>\begin{array}{l} F _ {Z} (z) = P \left\{X Y \leqslant z \right\} = P \left\{X \geqslant - z, Y = - 1 \right\} + P \left\{X \leqslant z, Y = 1 \right\} \\ \underline {{\text {独立性}}} P \left\{X \geqslant - z \right\} P \left\{Y = - 1 \right\} + P \left\{X \leqslant z \right\} P \left\{Y = 1 \right\} \\ = p \left[ 1 - F _ {X} (- z) \right] + (1 - p) F _ {X} (z), \\ \end{array}</equation>其中<equation>F_{X}(x)</equation>是X的分布函数.

于是，Z的概率密度为<equation>f _ {Z} (z) = F _ {Z} ^ {\prime} (z) = \left\{p \left[ 1 - F _ {X} (- z) \right] + (1 - p) F _ {X} (z) \right\} ^ {\prime} = p f _ {X} (- z) + (1 - p) f _ {X} (z).</equation>由于<equation>X</equation>服从参数为1的指数分布，故<equation>X</equation>的概率密度为<equation>f_{X}(x) = \left\{ \begin{array}{ll} \mathrm{e}^{-x}, & x > 0, \\ 0, & x \leqslant 0. \end{array} \right.</equation>当<equation>z\leqslant0</equation>时，<equation>-z\geqslant0,f_{X}(-z)=\mathrm{e}^{z},f_{X}(z)=0</equation>；当<equation>z > 0</equation>时，<equation>-z < 0,f_{X}(z)=\mathrm{e}^{-z},f_{X}(-z)=0.</equation><equation>f _ {Z} (z) = \left\{ \begin{array}{l l} p \mathrm {e} ^ {z}, & z \leqslant 0, \\ (1 - p) \mathrm {e} ^ {- z}, & z > 0. \end{array} \right.</equation>（Ⅱ）计算<equation>\operatorname{Cov}(X,Z).</equation><equation>\begin{array}{l} \operatorname {C o v} (X, Z) = E (X Z) - E (X) E (Z) = E \left(X ^ {2} Y\right) - E (X) E (X Y) \\ \underline {{\mathrm {独立性}}} E \left(X ^ {2}\right) E (Y) - \left[ E (X) \right] ^ {2} E (Y) \\ = D (X) E (Y). \\ \end{array}</equation>下面分别计算 D（X），E（Y）.

由于 X服从参数为1的指数分布，故<equation>D ( X )=1.</equation><equation>E (Y) = 1 \times (1 - p) + (- 1) \times p = 1 - 2 p.</equation>因此，<equation>\operatorname{Cov}(X,Z) = E(Y) = 1 - 2p.</equation>当<equation>p=\frac{1}{2}</equation>时，<equation>\operatorname{Cov}(X,Z)=0</equation>，X与Z不相关.

（Ⅲ）由第（Ⅱ）问可知，当<equation>p\neq \frac{1}{2}</equation>时，X与Z相关，从而不相互独立.

下面只需考虑 p =<equation>\frac{1}{2}</equation>的情况.

（法一）当<equation>p=\frac{1}{2}</equation>时，检验<equation>P\{X < 1,Z < 1\} = P\{X < 1\} P\{Z < 1\}</equation>是否成立.<equation>P \{X < 1 \} = \int_ {0} ^ {1} \mathrm {e} ^ {- x} \mathrm {d} x = 1 - \mathrm {e} ^ {- 1}.</equation><equation>\begin{aligned} P \{Z < 1 \} &= P \{X Y < 1 \} = F _ {Z} (1) = \frac {1}{2} \left[ 1 - F _ {X} (- 1) \right] + \frac {1}{2} F _ {X} (1) \\ &= \frac {1}{2} \times (1 - 0) + \frac {1}{2} \int_ {0} ^ {1} \mathrm {e} ^ {- x} \mathrm {d} x = \frac {1}{2} + \frac {1}{2} \left(1 - \mathrm {e} ^ {- 1}\right). \end{aligned}</equation><equation>\begin{aligned} P \{X < 1, Z < 1 \} &= P \{X < 1, X Y < 1 \} = P \{X \leqslant 0, X Y < 1 \} + P \{0 < X < 1, X Y < 1 \} \\ &= P \{0 < X < 1, X Y < 1 \} = P \{0 < X < 1, Y = 1 \} + P \{0 < X < 1, Y = - 1 \} \\ &= P \{0 < X < 1 \} = P \{X < 1 \} = 1 - \mathrm {e} ^ {- 1}. \end{aligned}</equation>由于<equation>1-\mathrm{e}^{-1}\neq(1-\mathrm{e}^{-1})\cdot\left[\frac{1}{2}+\frac{1}{2}(1-\mathrm{e}^{-1})\right]</equation>，故X，Z不相互独立.

（法二）当<equation>p=\frac{1}{2}</equation>时，检验<equation>P\{X > 1,Z < 1\} = P\{X > 1\} P\{Z < 1\}</equation>是否成立.

当 X > 1时，XY < 1等价于<equation>Y < \frac{1}{X}.</equation>又因为此时<equation>\frac{1}{X} < 1</equation>，而Y只可能取1和-1两个值，所以<equation>Y < \frac{1}{X}</equation>能推出 Y=-1.于是，<equation>P \{X > 1 \} = \int_ {1} ^ {+ \infty} \mathrm {e} ^ {- x} \mathrm {d} x = \mathrm {e} ^ {- 1}.</equation><equation>P \{Z < 1 \} \xlongequal {\text {同 法 一}} \frac {1}{2} + \frac {1}{2} \left(1 - \mathrm {e} ^ {- 1}\right).</equation><equation>\begin{array}{l} P \{X > 1, Z < 1 \} = P \{X > 1, X Y < 1 \} = P \left\{X > 1, Y < \frac {1}{X} \right\} = P \{X > 1, Y = - 1 \} \\ \underline {{\mathrm {独立 性}}} P \{X > 1 \} P \{Y = - 1 \} = \frac {1}{2} \mathrm {e} ^ {- 1}. \\ \end{array}</equation>由于<equation>\frac{1}{2}\mathrm{e}^{-1}\neq \mathrm{e}^{-1}\cdot \left[\frac{1}{2}+\frac{1}{2}\left(1-\mathrm{e}^{-1}\right)\right]</equation>，故X，Z不相互独立.

综上所述，X，Z不相互独立.

---

**2016年第22题 | 解答题 | 11分**

（本题满分11分）

设二维随机变量 (X,Y)在区域 D = {(x,y) | 0 < x < 1, x² < y <<equation>\sqrt{x}</equation>}上服从均匀分布，令<equation>U=\left\{\begin{array}{l l}1,&X\leqslant Y,\\ 0,&X>Y. \end{array} \right.</equation>I. 写出 (X,Y)的概率密度；

II. 问 U与 X是否相互独立？并说明理由；

III. 求 Z=U+X的分布函数 F(z).

**答案:**（I）<equation>f ( x,y)=\left\{ \begin{array}{ll} 3, & 0 < x < 1, x^{2} < y < \sqrt{x}, \\ 0, & \text{其他}; \end{array} \right.</equation>（Ⅱ）<equation>U</equation>与X不相互独立，理由略；

(Ⅲ)<equation>F (z) = \left\{ \begin{array}{ll} 0, & z < 0, \\ \frac{3}{2} z^{2} - z^{3}, & 0 \leqslant z < 1, \\ 2 (z - 1)^{\frac{3}{2}} - \frac{3}{2} z^{2} + 3 z - 1, & 1 \leqslant z < 2, \\ 1, & z \geqslant 2. \end{array} \right.</equation>

**解析:**（I）区域 D如图（a）所示，其面积为<equation>S = \int_ {0} ^ {1} \sqrt {x} \mathrm {d} x - \int_ {0} ^ {1} x ^ {2} \mathrm {d} x = \frac {2}{3} x ^ {\frac {3}{2}} \left| _ {0} ^ {1} - \frac {x ^ {3}}{3} \right| _ {0} ^ {1} = \frac {2}{3} - \frac {1}{3} = \frac {1}{3}.</equation>又由于（X，Y）在区域 D上服从均匀分布，故（X，Y）的概率密度为<equation>f (x, y) = \left\{ \begin{array}{l l} 3, & 0 < x < 1, x ^ {2} < y < \sqrt {x}, \\ 0, & \text {其 他}. \end{array} \right.</equation>(a)

(b)

（Ⅱ）考虑<equation>P\{U = 0, X\leqslant t\}</equation><equation>P \{U = 0 \} = P \{X > Y \} = \iint_ {\{(x, y) | x > x \}} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {x ^ {2}} ^ {x} 3 \mathrm {d} y = \int_ {0} ^ {1} 3 \left(x - x ^ {2}\right) \mathrm {d} x = \frac {1}{2}.</equation>对<equation>t \leqslant 0</equation>，<equation>P\{X \leqslant t\} = 0</equation>，<equation>P\{U = 0, X \leqslant t\} = 0.</equation>于是，<equation>P \left\{U = 0, X \leqslant t \right\} = P \left\{U = 0 \right\} \cdot P \left\{X \leqslant t \right\}.</equation>对<equation>t \geqslant 1</equation><equation>P\{X \leqslant t\} = 1,P\{U = 0,X \leqslant t\} = P\{U = 0\}</equation>.于是，<equation>P \{U = 0, X \leqslant t \} = P \{U = 0 \} \cdot P \{X \leqslant t \}.</equation>对 0 < t < 1，有效积分区域为图（b）中的蓝色区域.<equation>P \left\{U = 0, X \leqslant t \right\} = P \left\{X > Y, X \leqslant t \right\} = \int_ {0} ^ {t} \mathrm {d} x \int_ {x ^ {2}} ^ {x} 3 \mathrm {d} y = \int_ {0} ^ {t} 3 \left(x - x ^ {2}\right) \mathrm {d} x = \frac {3}{2} t ^ {2} - t ^ {3},</equation><equation>P \left\{X \leqslant t \right\} = \int_ {0} ^ {t} \mathrm {d} x \int_ {x ^ {2}} ^ {\sqrt {x}} 3 \mathrm {d} y = \int_ {0} ^ {t} 3 \left(\sqrt {x} - x ^ {2}\right) \mathrm {d} x = 2 t ^ {\frac {3}{2}} - t ^ {3}.</equation>于是，<equation>\begin{aligned} P \{U = 0, X \leqslant t \} - P \{U = 0 \} \cdot P \{X \leqslant t \} &= \frac {3}{2} t ^ {2} - t ^ {3} - \frac {1}{2} \left(2 t ^ {\frac {3}{2}} - t ^ {3}\right) \\ &= \frac {3}{2} t ^ {2} - \frac {1}{2} t ^ {3} - t ^ {\frac {3}{2}} \neq 0. (\mathrm {见 注} \textcircled{1}) \end{aligned}</equation>因此，当 0 < t < 1时，U与X不相互独立.

（Ⅲ）由题设知，<equation>\begin{array}{l} F (z) = P \left\{Z \leqslant z \right\} = P \left\{U + X \leqslant z \right\} \\ = P \left\{U + X \leqslant z, U = 0 \right\} + P \left\{U + X \leqslant z, U = 1 \right\} \\ = P \left\{X \leqslant z, U = 0 \right\} + P \left\{X \leqslant z - 1, U = 1 \right\} \\ = P \left\{X \leqslant z, X > Y \right\} + P \left\{X \leqslant z - 1, X \leqslant Y \right\}. \\ \end{array}</equation>当 z < 0时，z-1<0，于是<equation>P\{X\leqslant z,X > Y\}=0,P\{X\leqslant z-1,X\leqslant Y\}=0</equation>从而 F（z）=0.当 0≤z<1时，z-1<0，于是 P<equation>\{X\leqslant z-1,X\leqslant Y\}=0</equation>从而<equation>F (z) = P \left\{X \leqslant z, X > Y \right\} = \int_ {0} ^ {z} \mathrm {d} x \int_ {x ^ {2}} ^ {x} 3 \mathrm {d} y = \int_ {0} ^ {z} 3 \left(x - x ^ {2}\right) \mathrm {d} x = \frac {3}{2} z ^ {2} - z ^ {3}.</equation>当<equation>1\leqslant z < 2</equation>时，<equation>0\leqslant z - 1 < 1</equation><equation>\begin{array}{l} F (z) = P \left\{X \leqslant z, X > Y \right\} + P \left\{X \leqslant z - 1, X \leqslant Y \right\} \\ = P \left\{X \leqslant 1, X > Y \right\} + P \left\{X \leqslant z - 1, X \leqslant Y \right\} \\ = \frac {1}{2} + \int_ {0} ^ {z - 1} \mathrm {d} x \int_ {x} ^ {\sqrt {x}} 3 \mathrm {d} y = \frac {1}{2} + \int_ {0} ^ {z - 1} 3 (\sqrt {x} - x) \mathrm {d} x \\ = \frac {1}{2} + 2 (z - 1) ^ {\frac {3}{2}} - \frac {3}{2} (z - 1) ^ {2} = 2 (z - 1) ^ {\frac {3}{2}} - \frac {3}{2} z ^ {2} + 3 z - 1. \\ \end{array}</equation>当<equation>z\geqslant 2</equation>时，<equation>z - 1\geqslant 1,F(z) = 1.</equation>综上所述，<equation>F ( z ) = \left\{ \begin{array}{ll} 0, & z < 0, \\ \frac{3}{2} z^{2} - z^{3}, & 0 \leqslant z < 1, \\ 2 ( z - 1 )^{\frac{3}{2}} - \frac{3}{2} z^{2} + 3 z - 1, & 1 \leqslant z < 2, \\ 1, & z \geqslant 2. \end{array} \right.</equation>

---

**2015年第14题 | 填空题 | 4分**

14. 设二维随机变量<equation>(X, Y)</equation>服从正态分布<equation>N(1, 0; 1, 1; 0)</equation>, 则<equation>P\{XY - Y < 0\} =</equation>___

**解析:**由题设知，X，Y不相关。又由于（X，Y）服从正态分布，故X，Y相互独立.从而<equation>\begin{aligned} P \{X Y - Y < 0 \} &= P \{(X - 1) Y < 0 \} = P \{X < 1, Y > 0 \} + P \{X > 1, Y < 0 \} \\ &= P \{X < 1 \} \cdot P \{Y > 0 \} + P \{X > 1 \} \cdot P \{Y < 0 \}. \end{aligned}</equation>由<equation>( X, Y ) \sim N ( 1, 0 ; 1, 1 ; 0 )</equation>可知，<equation>X\sim N ( 1, 1 )</equation><equation>Y\sim N ( 0, 1 )</equation>从而X，Y的概率密度的图像分别关于<equation>x=1</equation>，<equation>x=0</equation>对称，于是<equation>P \{ X < 1 \} = P \{ X > 1 \} = \frac{1}{2}</equation><equation>P \{ Y < 0 \} = P \{ Y > 0 \} = \frac{1}{2}.</equation>因此，<equation>P \left\{X Y - Y < 0 \right\} = \frac {1}{2} \times \frac {1}{2} + \frac {1}{2} \times \frac {1}{2} = \frac {1}{2}.</equation>

---

**2013年第8题 | 选择题 | 4分 | 答案: C**

8. 设随机变量 X和 Y相互独立，且 X和 Y的概率分布分别为（    ）

<table border="1"><tr><td>X</td><td>0</td><td>1</td><td>2</td><td>3</td></tr><tr><td>P</td><td><equation>\frac{1}{2}</equation></td><td><equation>\frac{1}{4}</equation></td><td><equation>\frac{1}{8}</equation></td><td><equation>\frac{1}{8}</equation></td></tr></table>

<table border="1"><tr><td>Y</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td></tr></table>

则<equation>P\{X+Y=2\}=(\quad)</equation>A.<equation>\frac{1}{1 2}</equation>B.<equation>\frac{1}{8}</equation>C.<equation>\frac{1}{6}</equation>D.<equation>\frac{1}{2}</equation>

答案: C

**解析:**由题设知<equation>\begin{array}{l} P \{X + Y = 2 \} = P \{X = 1, Y = 1 \} + P \{X = 2, Y = 0 \} + P \{X = 3, Y = - 1 \} \\ \underline {{\underline {{X , Y}} \mathrm {相 互 独立}}} P \{X = 1 \} \cdot P \{Y = 1 \} + P \{X = 2 \} \cdot P \{Y = 0 \} + P \{X = 3 \} \cdot P \{Y = - 1 \} \\ = \frac {1}{4} \times \frac {1}{3} + \frac {1}{8} \times \frac {1}{3} + \frac {1}{8} \times \frac {1}{3} = \frac {1}{6}. \\ \end{array}</equation>应选C.

---

**2012年第7题 | 选择题 | 4分 | 答案: D**

7. 设随机变量 X与 Y相互独立，且都服从区间（0,1）上的均匀分布，则<equation>P\{ X^{2}+Y^{2}\leqslant1\}=</equation>A.<equation>\frac{1}{4}</equation>B.<equation>\frac{1}{2}</equation>C.<equation>\frac{\pi}{8}</equation>D.<equation>\frac{\pi}{4}</equation>

答案: D

**解析:**解 由题设知<equation>f_{X}(x) = \left\{ \begin{array}{ll}1, & 0 < x < 1,\\ 0, & \text{其他}, \end{array} \right.</equation><equation>f_{Y}(y) = \left\{ \begin{array}{ll}1, & 0 < y < 1,\\ 0, & \text{其他}. \end{array} \right.</equation>由于X与Y相互独立，故

（X，Y）的概率密度为<equation>f (x, y) = f _ {X} (x) f _ {Y} (y) = \left\{ \begin{array}{l l} 1, & 0 < x < 1, 0 < y < 1, \\ 0, & \text {其 他}. \end{array} \right.</equation>记<equation>D = \{(x,y)\mid 0\leqslant x\leqslant 1,0\leqslant y\leqslant 1\}</equation>，<equation>P \left\{X ^ {2} + Y ^ {2} \leqslant 1 \right\} = \iint_ {\left\{(x, y) \mid x ^ {2} + y ^ {2} \leqslant 1 \right\} \cap D} f (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {\left\{(x, y) \mid x ^ {2} + y ^ {2} \leqslant 1, x \geqslant 0, y \geqslant 0 \right\}} 1 \mathrm {d} x \mathrm {d} y = \frac {\pi}{4}.</equation>应选 D.

---

**2009年第8题 | 选择题 | 4分 | 答案: B**

8. 设随机变量 X与 Y相互独立，且 X服从标准正态分布 N(0,1), Y的概率分布为<equation>P\{Y=0\}=P\{Y=1\}=\frac{1}{2}</equation>. 记<equation>F_{Z}(z)</equation>为随机变量 Z=XY的分布函数，则函数<equation>F_{Z}(z)</equation>的间断点个数为（    )

A.0 B.1 C.2 D.3

答案: B

**解析:**解 先用两种方法求<equation>F_{Z}(z).</equation>（法一）由定义知<equation>\begin{array}{l} F _ {Z} (z) = P \left\{Z \leqslant z \right\} = P \left\{X Y \leqslant z \right\} = P \left\{X Y \leqslant z, Y = 0 \right\} + P \left\{X Y \leqslant z, Y = 1 \right\} \\ = P \left\{z \geqslant 0, Y = 0 \right\} + P \left\{X \leqslant z, Y = 1 \right\} \\ \xlongequal {X, Y \text {相 互 独立}} P \left\{z \geqslant 0, Y = 0 \right\} + P \left\{X \leqslant z \right\} \cdot P \left\{Y = 1 \right\} \\ = P \left\{z \geqslant 0, Y = 0 \right\} + \frac {1}{2} \Phi (z), \\ \end{array}</equation>其中<equation>\varPhi(z)</equation>为标准正态分布函数.

当<equation>z < 0</equation>时，<equation>P\{z\geqslant 0, Y = 0\} = P(\varnothing) = 0</equation>，故<equation>F_{Z}(z) = \frac{1}{2}\Phi (z).</equation>当<equation>z \geqslant 0</equation>时，<equation>P\{z \geqslant 0, Y = 0\} = P\{Y = 0\} = \frac{1}{2}</equation>，故<equation>F_{Z}(z) = \frac{1}{2} +\frac{1}{2}\Phi (z).</equation>（法二）由全概率公式知<equation>\begin{array}{l} F _ {Z} (z) = P \left\{Z \leqslant z \right\} = P \left\{X Y \leqslant z \right\} \\ = P \left\{X Y \leqslant z \mid Y = 0 \right\} \cdot P \left\{Y = 0 \right\} + P \left\{X Y \leqslant z \mid Y = 1 \right\} \cdot P \left\{Y = 1 \right\} \\ = \frac {1}{2} P \left\{z \geqslant 0 \mid Y = 0 \right\} + \frac {1}{2} P \left\{X \leqslant z \mid Y = 1 \right\} \\ \underline {{\underline {{X , Y}} \text {相 互 独 立}}} \frac {1}{2} P \left\{z \geqslant 0 \right\} + \frac {1}{2} P \left\{X \leqslant z \right\} \\ = \left\{ \begin{array}{l l} \frac {1}{2} \Phi (z), & z < 0, \\ \frac {1}{2} + \frac {1}{2} \Phi (z), & z \geqslant 0. \end{array} \right. \\ \end{array}</equation>由于<equation>\varPhi(z)</equation>连续，故<equation>F_{z}(z)</equation>仅在<equation>z = 0</equation>处间断.应选B.

---

**2009年第23题 | 解答题 | 11分**


袋中有1个红球、2个黑球与3个白球.现有放回地从袋中取两次，每次取一个球.以 X，Y，Z分别表示两次取球所取得的红球、黑球与白球的个数.

I. 求<equation>P\{X=1\mid Z=0\}</equation>；

II. 求二维随机变量（X，Y）的概率分布.

**答案:**(23) (I)<equation>\frac{4}{9}</equation>;

（Ⅱ）X和Y的联合分布律为

<table border="1"><tr><td rowspan="2">X

Y</td><td>0</td><td>1</td><td>2</td></tr><tr><td><equation>\frac{1}{4}</equation></td><td><equation>\frac{1}{6}</equation></td><td><equation>\frac{1}{36}</equation></td></tr><tr><td>1</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{9}</equation></td><td>0</td></tr><tr><td>2</td><td><equation>\frac{1}{9}</equation></td><td>0</td><td>0</td></tr></table>

**解析:**解（I）（法一）由条件概率的定义知，<equation>P \{X = 1 \mid Z = 0 \} = \frac {P \{X = 1 , Z = 0 \}}{P \{Z = 0 \}} = \frac {P \{X = 1 , Y = 1 \}}{P \{Z = 0 \}} = \frac {\mathrm {C} _ {2} ^ {1} \times \frac {1}{6} \times \frac {2}{6}}{\frac {3}{6} \times \frac {3}{6}} = \frac {4}{9}.</equation>（法二）<equation>P \{ X=1 \mid Z=0 \}</equation>是指在 Z=0，即两次所取的球中没有白球的条件下，两次取球为一黑一红的概率，即在1个红球、2个黑球中有放回地取得一黑一红的概率.因此，<equation>P \left\{X = 1 \mid Z = 0 \right\} = C _ {2} ^ {1} \times \frac {1}{3} \times \frac {2}{3} = \frac {4}{9}.</equation>（Ⅱ）由于是有放回地取球，故 X，Y所有可能的取值均为0，1，2.于是二维随机变量（X，Y）的概率分布为，<equation>P \{X = 0, Y = 0 \} = P \{Z = 2 \} = \frac {3}{6} \times \frac {3}{6} = \frac {1}{4},</equation><equation>P \{X = 0, Y = 1 \} = P \{Y = 1, Z = 1 \} = C _ {2} ^ {1} \times \frac {2}{6} \times \frac {3}{6} = \frac {1}{3},</equation><equation>P \{X = 0, Y = 2 \} = \frac {2}{6} \times \frac {2}{6} = \frac {1}{9},</equation><equation>P \{X = 1, Y = 0 \} = P \{X = 1, Z = 1 \} = C _ {2} ^ {1} \times \frac {1}{6} \times \frac {3}{6} = \frac {1}{6},</equation><equation>P \{X = 1, Y = 1 \} = \mathrm {C} _ {2} ^ {1} \times \frac {1}{6} \times \frac {2}{6} = \frac {1}{9}, \quad P \{X = 1, Y = 2 \} = 0,</equation><equation>P \{X = 2, Y = 0 \} = \frac {1}{6} \times \frac {1}{6} = \frac {1}{3 6}, \quad P \{X = 2, Y = 1 \} = 0, \quad P \{X = 2, Y = 2 \} = 0.</equation>因此，X和Y的联合分布律为

<table border="1"><tr><td rowspan="2">Y

X</td><td>0</td><td>1</td><td>2</td></tr><tr><td><equation>\frac{1}{4}</equation></td><td><equation>\frac{1}{6}</equation></td><td><equation>\frac{1}{36}</equation></td></tr><tr><td>1</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{9}</equation></td><td>0</td></tr><tr><td>2</td><td><equation>\frac{1}{9}</equation></td><td>0</td><td>0</td></tr></table>

---


### 数理统计的基本概念

**2023年第9题 | 选择题 | 5分 | 答案: D**

9. 设<equation>X_{1}, X_{2}, \dots, X_{n}</equation>为来自总体<equation>N(\mu_{1},\sigma^{2})</equation>的简单随机样本，<equation>Y_{1}, Y_{2}, \dots, Y_{m}</equation>为来自总体<equation>N(\mu_{2}, 2\sigma^{2})</equation>的简单随机样本，且两样本相互独立，记<equation>\bar{X}=\frac{1}{n}\sum_{i=1}^{n}X_{i},\bar{Y}=\frac{1}{m}\sum_{i=1}^{m}Y_{i},S_{1}^{2}=\frac{1}{n-1}\sum_{i=1}^{n}(X_{i}-\bar{X})^{2},S_{2}^{2}=\frac{1}{m-1}\sum_{i=1}^{m}(Y_{i}-\bar{Y})^{2}</equation>，则（    )

A.<equation>\frac{S_{1}^{2}}{S_{2}^{2}}\sim F(n,m)</equation>B.<equation>\frac{S_{1}^{2}}{S_{2}^{2}}\sim F(n-1,m-1)</equation>C.<equation>\frac{2S_{1}^{2}}{S_{2}^{2}}\sim F(n,m)</equation>D.<equation>\frac{2S_{1}^{2}}{S_{2}^{2}}\sim F(n-1,m-1)</equation>

答案: D

**解析:**解<equation>S_{1}^{2}=\frac{1}{n-1}\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}</equation>为<equation>X_{1},X_{2},\dots,X_{n}</equation>的样本方差，<equation>S_{2}^{2}=\frac{1}{m-1}\sum_{i=1}^{m}\left(Y_{i}-\bar{Y}\right)^{2}</equation>为<equation>Y_{1},</equation><equation>Y_{2},\dots,Y_{m}</equation>的样本方差.由正态总体的抽样分布定理可知，<equation>\frac {(n - 1) S _ {1} ^ {2}}{\sigma^ {2}} \sim \chi^ {2} (n - 1), \quad \frac {(m - 1) S _ {2} ^ {2}}{2 \sigma^ {2}} \sim \chi^ {2} (m - 1).</equation>又因为两个样本相互独立，所以由 F分布的定义可知<equation>\frac {\frac {(n - 1) S _ {1} ^ {2}}{\sigma^ {2}} / (n - 1)}{\frac {(m - 1) S _ {2} ^ {2}}{2 \sigma^ {2}} / (m - 1)} = \frac {S _ {1} ^ {2} / \sigma^ {2}}{S _ {2} ^ {2} / 2 \sigma^ {2}} = \frac {2 S _ {1} ^ {2}}{S _ {2} ^ {2}} \sim F (n - 1, m - 1).</equation>因此，应选D.

---

**2023年第10题 | 选择题 | 5分 | 答案: A**

10. 设<equation>X_{1}, X_{2}</equation>为来自总体<equation>N(\mu ,\sigma^{2})</equation>的简单随机样本，其中<equation>\sigma(\sigma >0)</equation>为未知参数.记<equation>\hat{\sigma}=a\left| X_{1}-X_{2}\right|</equation>若<equation>E(\hat{\sigma})=\sigma</equation>则 a=（    )

A.<equation>\frac{\sqrt{\pi}}{2}</equation>B.<equation>\frac{\sqrt{2\pi}}{2}</equation>C.<equation>\sqrt{\pi}</equation>D.<equation>\sqrt{2\pi}</equation>

答案: A

**解析:**由于<equation>X_{1}, X_{2}</equation>为来自总体<equation>N(\mu ,\sigma^{2})</equation>的简单随机样本，故<equation>X_{1}, X_{2}</equation>相互独立.

令<equation>Z = X_{1} - X_{2}</equation>，则<equation>Z\sim N(0,2\sigma^{2})</equation>，从而Z的概率密度<equation>f(z) = \frac{1}{\sqrt{2\pi}\cdot \sqrt{2}\sigma}\mathrm{e}^{-\frac{z^{2}}{4\sigma^{2}}}</equation><equation>\begin{array}{l} E (\mid Z \mid) = \int_ {- \infty} ^ {+ \infty} | z | f (z) \mathrm {d} z = 2 \int_ {0} ^ {+ \infty} \frac {1}{\sqrt {2 \pi} \cdot \sqrt {2} \sigma} \cdot z \mathrm {e} ^ {- \frac {z ^ {2}}{4 \sigma^ {2}}} \mathrm {d} z = \frac {1}{2 \sqrt {\pi} \sigma} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {z ^ {2}}{4 \sigma^ {2}}} \mathrm {d} \left(z ^ {2}\right) \\ = \frac {1}{2 \sqrt {\pi} \sigma} \cdot \left(- 4 \sigma^ {2} \mathrm {e} ^ {- \frac {z ^ {2}}{4 \sigma^ {2}}}\right) \Bigg | _ {0} ^ {+ \infty} = \frac {2}{\sqrt {\pi}} \sigma . \\ \end{array}</equation>由此可得<equation>E (\hat {\sigma}) = E \left(a \mid X _ {1} - X _ {2} \mid\right) = E \left(a \mid Z \mid\right) = \frac {2 a}{\sqrt {\pi}} \sigma .</equation>又因为<equation>E(\hat{\sigma}) = \sigma</equation>，即<equation>\frac{2a}{\sqrt{\pi}}\sigma = \sigma</equation>，所以<equation>a=\frac{\sqrt{\pi}}{2}.</equation>因此，应选A.

---

**2021年第9题 | 选择题 | 5分 | 答案: B**

9. 设<equation>( X_{1}, Y_{1}), ( X_{2}, Y_{2}), \cdots, ( X_{n}, Y_{n} )</equation>为来自总体<equation>N (\mu_{1}, \mu_{2}; \sigma_{1}^{2}, \sigma_{2}^{2}; \rho)</equation>的简单随机样本，令<equation>\theta=\mu_{1}-\mu_{2}, \bar{X}=\frac{1}{n}\sum_{i=1}^{n} X_{i}, \bar{Y}=</equation><equation>\frac{1}{n}\sum_{i=1}^{n} Y_{i}, \hat{\theta}=\bar{X}-\bar{Y}</equation>，则（    )

A.<equation>E(\hat{\theta})=\theta,D(\hat{\theta})=\frac{\sigma_{1}^{2}+\sigma_{2}^{2}}{n}</equation>B.<equation>E(\hat{\theta})=\theta,D(\hat{\theta})=\frac{\sigma_{1}^{2}+\sigma_{2}^{2}-2\rho\sigma_{1}\sigma_{2}}{n}</equation>C.<equation>E(\hat{\theta})\neq\theta,D(\hat{\theta})=\frac{\sigma_{1}^{2}+\sigma_{2}^{2}}{n}</equation>D.<equation>E(\hat{\theta})\neq\theta,D(\hat{\theta})=\frac{\sigma_{1}^{2}+\sigma_{2}^{2}-2\rho\sigma_{1}\sigma_{2}}{n}</equation>

答案: B

**解析:**解 由于总体（X，Y）服从<equation>N(\mu_{1},\mu_{2};\sigma_{1}^{2},\sigma_{2}^{2};\rho)</equation>，故<equation>X\sim N(\mu_{1},\sigma_{1}^{2}),Y\sim N(\mu_{2},\sigma_{2}^{2})</equation>，从而<equation>\overline{X}\sim</equation><equation>N \left( \mu_{1},\frac{\sigma_{1}^{2}}{n} \right),\overline{Y}\sim N \left( \mu_{2},\frac{\sigma_{2}^{2}}{n} \right).</equation>计算<equation>E(\hat{\theta})</equation><equation>E (\hat {\theta}) = E (\bar {X} - \bar {Y}) = E (\bar {X}) - E (\bar {Y}) = \mu_ {1} - \mu_ {2} = \theta .</equation>计算<equation>D(\hat{\theta})。</equation><equation>D (\hat {\theta}) = D (\bar {X} - \bar {Y}) = D (\bar {X}) + D (\bar {Y}) - 2 \operatorname {C o v} (\bar {X}, \bar {Y}) = \frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{n} - 2 \operatorname {C o v} (\bar {X}, \bar {Y}).</equation>由于<equation>\left(X_{1},Y_{1}\right),\left(X_{2},Y_{2}\right),\dots,\left(X_{n},Y_{n}\right)</equation>为简单随机样本，故它们相互独立，从而当<equation>i\neq j</equation>时，<equation>X_{i}</equation>与<equation>Y_{j}</equation>独立.于是，<equation>\operatorname{Cov}(X_{i},Y_{i})=\operatorname{Cov}(X,Y),\operatorname{Cov}(X_{i},Y_{j})=0(i\neq j).</equation><equation>\begin{aligned} \operatorname {C o v} (\bar {X}, \bar {Y}) &= \operatorname {C o v} \left(\frac {\sum_ {i = 1} ^ {n} X _ {i}}{n}, \frac {\sum_ {j = 1} ^ {n} Y _ {j}}{n}\right) = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \operatorname {C o v} \left(X _ {i}, Y _ {j}\right) = \frac {1}{n ^ {2}} \cdot \sum_ {i = 1} ^ {n} \operatorname {C o v} \left(X _ {i}, Y _ {i}\right) \\ &= \frac {1}{n ^ {2}} \cdot n \operatorname {C o v} (X, Y) = \frac {\operatorname {C o v} (X , Y)}{n}. \end{aligned}</equation>因此，<equation>D (\hat {\theta}) = \frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{n} - 2 \operatorname {C o v} (\bar {X}, \bar {Y}) = \frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{n} - \frac {2}{n} \operatorname {C o v} (X, Y) = \frac {\sigma_ {1} ^ {2} + \sigma_ {2} ^ {2} - 2 \rho \sigma_ {1} \sigma_ {2}}{n}.</equation>应选B.

---

**2018年第8题 | 选择题 | 4分 | 答案: B**

8. 设<equation>X_{1}, X_{2}, \cdots , X_{n}</equation>（其中 n≥2）为来自总体<equation>N(\mu ,\sigma^{2})(\sigma >0)</equation>的简单随机样本. 令<equation>\bar{X}=\frac{1}{n}\sum_{i=1}^{n}X_{i},</equation>S=<equation>\sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(X_{i}-\bar{X})^{2}},</equation><equation>S^{*} =\sqrt{\frac{1}{n}\sum_{i=1}^{n}(X_{i}-\mu)^{2}}</equation>，则（    )

A.<equation>\frac{\sqrt{n}(\bar{X}-\mu)}{S}\sim t(n)</equation>B.<equation>\frac{\sqrt{n}(\bar{X}-\mu)}{S}\sim t(n-1)</equation>C.<equation>\frac{\sqrt{n}(\bar{X}-\mu)}{S^{*}}\sim t(n)</equation>D.<equation>\frac{\sqrt{n}(\bar{X}-\mu)}{S^{*}}-t(n-1)</equation>

答案: B

**解析:**解 由于<equation>\bar{X}</equation>为样本均值，故<equation>\bar{X}\sim N\left(\mu ,\frac{\sigma^{2}}{n}\right).</equation>于是，<equation>\frac{\overline{{X}} - \mu}{\sqrt{\frac{\sigma^{2}}{n}}} = \frac{\sqrt{n}\left(\overline{{X}} - \mu\right)}{\sigma}\sim N(0,1)</equation>根据抽样分布定理（2），有<equation>\frac{(n - 1)S^{2}}{\sigma^{2}}\sim X^{2}(n - 1).</equation>又因为<equation>\frac{\sqrt{n}\left(\bar{X} - \mu\right)}{\sigma}</equation>与<equation>\frac{(n - 1)S^{2}}{\sigma^{2}}</equation>相互独立，所以<equation>\frac{\frac{\sqrt{n}\left(\bar{X} - \mu\right)}{\sigma}}{\sqrt{\frac{(n - 1)S^{2}}{\sigma^{2}}}\bigg /(n - 1)} = \frac{\sqrt{n}\left(\bar{X} - \mu\right)}{S}\sim t(n - 1).</equation>应选B.

---

**2017年第8题 | 选择题 | 4分 | 答案: B**

8. 设<equation>X_{1}, X_{2}, \dots , X_{n} ( n \geqslant 2 )</equation>为来自总体<equation>N (\mu , 1)</equation>的简单随机样本，记<equation>\bar{X}=\frac{1}{n}\sum_{i=1}^{n} X_{i}</equation>，则下列结论中不正确的是（    ）

A.<equation>\sum_{i=1}^{n} ( X_{i}-\mu )^{2}</equation>服从<equation>\chi^{2}</equation>分布

B.<equation>2 ( X_{n}-X_{1} )^{2}</equation>服从<equation>\chi^{2}</equation>分布

C.<equation>\sum_{i=1}^{n} ( X_{i}-\bar{X} )^{2}</equation>服从<equation>\chi^{2}</equation>分布

D.<equation>n ( \bar{X}-\mu )^{2}</equation>服从<equation>\chi^{2}</equation>分布

答案: B

**解析:**解 由题设知，<equation>X_{1}, X_{2}, \dots , X_{n}</equation>相互独立且与总体同分布.

依次分析各选项.

选项A：由<equation>X_{i}\sim N(\mu,1)</equation>知，<equation>X_{i}-\mu\sim N(0,1)</equation>，<equation>i=1,2,\cdots,n</equation>，故<equation>\sum_{i=1}^{n} \left(X_{i}-\mu\right)^{2}\sim X^{2}(n).</equation>因此选项A正确.

选项B：由<equation>X_{1}\sim N(\mu ,1), X_{n}\sim N(\mu ,1)</equation>知，<equation>X_{n}-X_{1}\sim N(0,2)</equation>，故<equation>\frac{X_{n}-X_{1}}{\sqrt{2}}\sim N(0,1)</equation>，于是<equation>\frac{(X_{n}-X_{1})^{2}}{2}\sim X^{2}(1).</equation>但2（<equation>X_{n}-X_{1} )^{2}</equation>不服从<equation>\chi^{2}</equation>分布.因此选项B不正确.

事实上，若<equation>2 \left(X_{n}-X_{1}\right)^{2}\sim \mathcal{X}^{2}(m)</equation>，则<equation>E \left[ 2 \left(X _ {n} - X _ {1}\right) ^ {2} \right] = m, \quad D \left[ 2 \left(X _ {n} - X _ {1}\right) ^ {2} \right] = 2 m.</equation>但由<equation>\frac{\left(X_{n}-X_{1}\right)^{2}}{2}\sim X^{2}(1)</equation>知，<equation>E \left[ \frac {\left(X _ {n} - X _ {1}\right) ^ {2}}{2} \right] = 1, \quad D \left[ \frac {\left(X _ {n} - X _ {1}\right) ^ {2}}{2} \right] = 2,</equation>从而<equation>E[2(X_{n}-X_{1})^{2}]=4,D[2(X_{n}-X_{1})^{2}]=32.</equation>这与<equation>D[2(X_{n}-X_{1})^{2}]=2E[2(X_{n}-X_{1})^{2}]</equation>矛盾，故<equation>2(X_{n}-X_{1})^{2}</equation>不服从<equation>\chi^{2}</equation>分布.

选项C：由性质（2）知，<equation>( n-1 ) S^{2} \sim X^{2} ( n-1 ).</equation>又因为<equation>S^{2}=\frac{1}{n-1}\sum_{i=1}^{n} \left( X_{i}-\overline{X}\right)^{2}</equation>，所以<equation>\sum_{i=1}^{n} \left( X_{i}-\overline{X}\right)^{2} \sim X^{2} ( n-1 ).</equation>因此选项C正确.

选项D：由性质（2）知，<equation>\overline{X}=\frac{1}{n}\sum_{i=1}^{n}X_{i}\sim N\left(\mu ,\frac{1}{n}\right)</equation>，于是<equation>\sqrt{n} \left( \overline{{X}}-\mu \right) \sim N (0,1)</equation>，从而<equation>n \left( \overline{{X}}-\mu \right)^{2} \sim X^{2} (1).</equation>因此选项D正确.

综上所述，应选B.

---

**2015年第8题 | 选择题 | 4分 | 答案: B**

8. 设总体<equation>X\sim B(m,\theta),X_{1},X_{2},\cdots,X_{n}</equation>为来自该总体的简单随机样本，<equation>\bar{X}</equation>为样本均值，则<equation>E\left[ \sum_{i=1}^{n}(X_{i}-\bar{X})^{2}\right] =</equation>(    )

A.<equation>( m-1 ) n \theta( 1-\theta)</equation>B.<equation>m(n-1)\theta( 1-\theta)</equation>C.<equation>( m-1 ) ( n-1 ) \theta( 1-\theta)</equation>D.<equation>mn \theta( 1-\theta)</equation>

答案: B

**解析:**解（法一）由于样本方差<equation>S^{2}=\frac{1}{n-1}\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}</equation>且<equation>E(S^{2})=D(X)=m\theta(1-\theta)</equation>，故<equation>E\left[ \sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}\right] = E\left[ (n-1)S^{2}\right] = (n-1)E(S^{2})=m(n-1)\theta(1-\theta).</equation>应选B.

（法二）直接计算.<equation>\begin{array}{l} E \left[ \sum_ {i = 1} ^ {n} \left(X _ {i} - \bar {X}\right) ^ {2} \right] = E \left(\sum_ {i = 1} ^ {n} X _ {i} ^ {2} - 2 \sum_ {i = 1} ^ {n} X _ {i} \bar {X} + n \bar {X} ^ {2}\right) = E \left(\sum_ {i = 1} ^ {n} X _ {i} ^ {2} - 2 n \bar {X} ^ {2} + n \bar {X} ^ {2}\right) \\ = E \left(\sum_ {i = 1} ^ {n} X _ {i} ^ {2} - n \bar {X} ^ {2}\right) = n E \left(X ^ {2}\right) - n E \left(\bar {X} ^ {2}\right) \\ = n \left\{\left[ E (X) \right] ^ {2} + D (X) \right\} - n \left\{\left[ E (\bar {X}) \right] ^ {2} + D (\bar {X}) \right\} \\ \frac {E (\bar {X}) = E (X)}{D (\bar {X}) = \frac {1}{n} D (X)} n \left[ D (X) - \frac {1}{n} D (X) \right] = m (n - 1) \theta (1 - \theta). \\ \end{array}</equation>应选B.

---

**2014年第8题 | 选择题 | 4分 | 答案: C**

8. 设<equation>X_{1}, X_{2}, X_{3}</equation>为来自正态总体<equation>N(0,\sigma^{2})</equation>的简单随机样本，则统计量<equation>S=\frac{X_{1}-X_{2}}{\sqrt{2}|X_{3}|}</equation>服从的分布为（    )

A. F(1,1) B. F(2,1) C. t(1) D. t(2)

答案: C

**解析:**解 由题设知，<equation>X_{1}, X_{2}, X_{3}</equation>相互独立且服从正态分布<equation>N(0,\sigma^{2})</equation>，故<equation>\frac{X_{1}-X_{2}}{\sqrt{2}\sigma}\sim N(0,1),\frac{X_{3}}{\sigma}\sim</equation><equation>N(0,1),\left(\frac{X_{3}}{\sigma}\right)^{2}\sim X^{2}(1).</equation>又因为<equation>\frac{X_{1}-X_{2}}{\sqrt{2}\sigma}</equation>与<equation>\left(\frac{X_{3}}{\sigma}\right)^{2}</equation>相互独立，所以<equation>S = \frac {X _ {1} - X _ {2}}{\sqrt {2} \left| X _ {3} \right|} = \frac {\frac {X _ {1} - X _ {2}}{\sqrt {2} \sigma}}{\left| \frac {X _ {3}}{\sigma} \right|} \sim t (1).</equation>应选C.

---

**2012年第8题 | 选择题 | 4分 | 答案: B**

8. 设<equation>X_{1}, X_{2}, X_{3}, X_{4}</equation>为来自总体<equation>N(1,\sigma^{2})(\sigma >0)</equation>的简单随机样本，则统计量<equation>\frac{X_{1}-X_{2}} {|X_{3}+X_{4}-2|}</equation>的分布为（    )

A. N(0,1) B. t(1) C.<equation>X^{2}(1)</equation>D. F(1,1)

答案: B

**解析:**解<equation>X_{1}, X_{2}, X_{3}, X_{4}</equation>相互独立且都服从正态分布<equation>N(1, \sigma^{2})</equation>.由正态分布的性质可得<equation>E \left(X _ {1} - X _ {2}\right) = 0, \quad D \left(X _ {1} - X _ {2}\right) = D \left(X _ {1}\right) + D \left(X _ {2}\right) = 2 \sigma^ {2},</equation><equation>E \left(X _ {3} + X _ {4} - 2\right) = 0, \quad D \left(X _ {3} + X _ {4} - 2\right) = D \left(X _ {3}\right) + D \left(X _ {4}\right) = 2 \sigma^ {2}.</equation>于是<equation>X_{1} - X_{2}\sim N(0,2\sigma^{2})</equation>，<equation>X_{3} + X_{4} - 2\sim N(0,2\sigma^{2})</equation>，从而<equation>\frac {X _ {1} - X _ {2}}{\sqrt {2} \sigma} \sim N (0, 1), \quad \frac {X _ {3} + X _ {4} - 2}{\sqrt {2} \sigma} \sim N (0, 1), \quad \left(\frac {X _ {3} + X _ {4} - 2}{\sqrt {2} \sigma}\right) ^ {2} \sim X ^ {2} (1).</equation>又因为<equation>\frac{X_{1}-X_{2}}{\sqrt{2}\sigma}</equation>与<equation>\left(\frac{X_{3}+X_{4}-2}{\sqrt{2}\sigma}\right)^{2}</equation>相互独立，所以<equation>\frac {X _ {1} - X _ {2}}{\left| X _ {3} + X _ {4} - 2 \right|} = \frac {\frac {X _ {1} - X _ {2}}{\sqrt {2} \sigma}}{\left| \frac {X _ {3} + X _ {4} - 2}{\sqrt {2} \sigma} \right|} \sim t (1).</equation>应选B.

---

**2011年第8题 | 选择题 | 4分 | 答案: D**

8. 设总体<equation>X</equation>服从参数为<equation>\lambda(\lambda>0)</equation>的泊松分布，<equation>X_{1},X_{2},\cdots,X_{n}(n\geqslant2)</equation>为来自该总体的简单随机样本，则对于统计量<equation>T_{1}=\frac{1}{n}\sum_{i=1}^{n}X_{i}</equation>和<equation>T_{2}=\frac{1}{n-1}\sum_{i=1}^{n-1}X_{i}+\frac{1}{n}X_{n}</equation>，有（    ）

A.<equation>E(T_{1})>E(T_{2}),D(T_{1})>D(T_{2})</equation>B.<equation>E(T_{1})>E(T_{2}),D(T_{1})<D(T_{2})</equation>C.<equation>E(T_{1})<E(T_{2}),D(T_{1})>D(T_{2})</equation>D.<equation>E(T_{1})<E(T_{2}),D(T_{1})<D(T_{2})</equation>

答案: D

**解析:**由于<equation>X_{1}, X_{2}, \dots, X_{n}</equation>为简单随机样本，故它们相互独立且与总体同分布，从而<equation>E \left(T _ {1}\right) = E \left(\frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i}\right) = \frac {1}{n} \sum_ {i = 1} ^ {n} E \left(X _ {i}\right) = \frac {1}{n} \cdot n E (X) = E (X),</equation><equation>\begin{array}{l} E \left(T _ {2}\right) = E \left(\frac {1}{n - 1} \sum_ {i = 1} ^ {n - 1} X _ {i} + \frac {1}{n} X _ {n}\right) = \frac {1}{n - 1} \sum_ {i = 1} ^ {n - 1} E \left(X _ {i}\right) + \frac {1}{n} E \left(X _ {n}\right) \\ = \frac {1}{n - 1} \cdot (n - 1) E (X) + \frac {1}{n} E (X) = E (X) + \frac {1}{n} E (X), \\ \end{array}</equation><equation>D \left(T _ {1}\right) = D \left(\frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i}\right) = \frac {1}{n ^ {2}} \cdot D \left(\sum_ {i = 1} ^ {n} X _ {i}\right) = \frac {1}{n ^ {2}} \cdot n D (X) = \frac {1}{n} D (X),</equation><equation>\begin{array}{l} D \left(T _ {2}\right) = D \left(\frac {1}{n - 1} \sum_ {i = 1} ^ {n - 1} X _ {i} + \frac {1}{n} X _ {n}\right) = \frac {1}{(n - 1) ^ {2}} \sum_ {i = 1} ^ {n - 1} D \left(X _ {i}\right) + \frac {1}{n ^ {2}} D \left(X _ {n}\right) \\ = \frac {1}{(n - 1) ^ {2}} \cdot (n - 1) D (X) + \frac {1}{n ^ {2}} D (X) = \frac {1}{n - 1} D (X) + \frac {1}{n ^ {2}} D (X). \\ \end{array}</equation>又由于<equation>E ( X ) = D ( X ) = \lambda > 0</equation>，故<equation>E \left(T _ {2}\right) > E \left(T _ {1}\right), \quad D \left(T _ {2}\right) > \frac {1}{n - 1} D (X) > \frac {1}{n} D (X) = D \left(T _ {1}\right).</equation>应选 D.

---

**2010年第14题 | 填空题 | 4分**

14. 设<equation>X_{1}, X_{2}, \cdots, X_{n}</equation>是来自总体<equation>N(\mu, \sigma^{2})(\sigma>0)</equation>的简单随机样本. 记统计量<equation>T=\frac{1}{n}\sum_{i=1}^{n} X_{i}^{2}</equation>，则 E(T) = ___.

**答案:**#<equation>\sigma^{2}+\mu^{2}.</equation>

**解析:**由期望的性质可知，<equation>\begin{array}{l} E (T) = \frac {1}{n} E \left(\sum_ {i = 1} ^ {n} X _ {i} ^ {2}\right) = \frac {1}{n} \sum_ {i = 1} ^ {n} E \left(X _ {i} ^ {2}\right) = \frac {1}{n} \cdot n E \left(X ^ {2}\right) = E \left(X ^ {2}\right) \\ = D (X) + \left[ E (X) \right] ^ {2} = \sigma^ {2} + \mu^ {2}. \\ \end{array}</equation>

---

**2009年第14题 | 填空题 | 4分**

14. 设<equation>X_{1}, X_{2}, \cdots, X_{n}</equation>为来自二项分布总体 B(n,p)的简单随机样本，<equation>\bar{X}</equation>和<equation>S^{2}</equation>分别为样本均值和样本方差. 记统计量<equation>T=\bar{X}-S^{2}</equation>，则 E(T) = ___.

**解析:**解 由于 X ~ B(n,p)，故 E(X) = np，D(X) = np(1-p).于是 E<equation>\overline{{{X}}}</equation>= E(X) = np，<equation>E(S^{2})= D(X)=np(1-p).</equation>因此，<equation>E (T) = E \left(\bar {X} - S ^ {2}\right) = E \left(\bar {X}\right) - E \left(S ^ {2}\right) = n p - n p (1 - p) = n p ^ {2}.</equation>

---


### 大数定律和中心极限定理

**2022年第9题 | 选择题 | 5分 | 答案: B**

9. 设随机变量序列<equation>X_{1}, X_{2}, \dots , X_{n}, \dots</equation>独立同分布，且<equation>X_{1}</equation>的概率密度为<equation>f(x)=\left\{\begin{array}{ll}1-|x|,&|x|<1,\\0,&\text{其他},\end{array}\right.</equation>则当 n<equation>\to\infty</equation>时，<equation>\frac{1}{n}\sum_{i=1}^{n}X_{i}^{2}</equation>依概率收敛于（    )

A.<equation>\frac{1}{8}</equation>B.<equation>\frac{1}{6}</equation>C.<equation>\frac{1}{3}</equation>D.<equation>\frac{1}{2}</equation>

答案: B

**解析:**解 由于随机变量序列<equation>X_{1}, X_{2}, \dots, X_{n}, \dots</equation>独立同分布，故<equation>X_{1}^{2}, X_{2}^{2}, \dots, X_{n}^{2}, \dots</equation>独立同分布.根据辛钦大数定律，<equation>\frac{1}{n}\sum_{i=1}^{n}X_{i}^{2}</equation>依概率收敛于<equation>E \left( X_{i}^{2} \right).</equation><equation>\begin{array}{l} E \left(X _ {i} ^ {2}\right) = E \left(X _ {1} ^ {2}\right) = \int_ {- \infty} ^ {+ \infty} x ^ {2} f (x) \mathrm {d} x = \int_ {- 1} ^ {1} x ^ {2} (1 - | x |) \mathrm {d} x \xlongequal {\text {对称性}} 2 \int_ {0} ^ {1} x ^ {2} (1 - x) \mathrm {d} x \\ = 2 \left(\frac {x ^ {3}}{3} - \frac {x ^ {4}}{4}\right) \Bigg | _ {0} ^ {1} = \frac {1}{6}. \\ \end{array}</equation>因此，应选B.

---


### 参数估计

**2022年第22题 | 解答题 | 12分**


设<equation>X_{1}, X_{2}, \dots, X_{n}</equation>为来自均值为<equation>\theta</equation>的指数分布总体的简单随机样本，<equation>Y_{1}, Y_{2}, \dots, Y_{m}</equation>为来自均值为2<equation>\theta</equation>的指数分布总体的简单随机样本，且两样本相互独立，其中<equation>\theta(\theta>0)</equation>是未知参数。利用样本<equation>X_{1}, X_{2}, \dots, X_{n}, Y_{1}, Y_{2}, \dots, Y_{m}</equation>求<equation>\theta</equation>的最大似然估计量<equation>\hat{\theta}</equation>，并求<equation>D(\hat{\theta})</equation>

**答案:**<equation>\hat {\theta} = \frac {2 \sum_ {i = 1} ^ {n} X _ {i} + \sum_ {j = 1} ^ {m} Y _ {j}}{2 (m + n)}, D (\hat {\theta}) = \frac {\theta^ {2}}{m + n}.</equation>

**解析:**解<equation>X_{1}, X_{2}, \dots , X_{n}</equation>是来自总体 X的简单随机样本.由于<equation>E ( X )=\theta</equation>，故 X服从参数为<equation>\frac{1}{\theta}</equation>的指数分布.于是，X的概率密度函数为<equation>f _ {X} (x) = \left\{ \begin{array}{l l} \frac {1}{\theta} \mathrm {e} ^ {- \frac {x}{\theta}}, & x > 0, \\ 0, & x \leqslant 0. \end{array} \right.</equation><equation>Y_{1}, Y_{2}, \dots , Y_{m}</equation>是来自总体Y的简单随机样本.由于<equation>E(Y)=2\theta</equation>，故Y服从参数为<equation>\frac{1}{2\theta}</equation>的指数分布.于是，Y的概率密度函数为<equation>f _ {Y} (y) = \left\{ \begin{array}{l l} \frac {1}{2 \theta} \mathrm {e} ^ {- \frac {y}{2 \theta}}, & y > 0, \\ 0, & y \leqslant 0. \end{array} \right.</equation>设<equation>x_{1}, x_{2}, \dots , x_{n}, y_{1}, y_{2}, \dots , y_{m}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots , X_{n}, Y_{1}, Y_{2}, \dots , Y_{m}</equation>的一组样本值，则似然函数<equation>L (\theta) = \left\{ \begin{array}{l l} \frac {1}{2 ^ {m} \theta^ {m + n}} \mathrm {e} ^ {- \frac {\sum_ {i = 1} ^ {n} x _ {i}}{\theta}} - \frac {\sum_ {i = 1} ^ {m} y _ {j}}{2 \theta}, & x _ {i} > 0, y _ {j} > 0, i = 1, 2, \dots , n, j = 1, 2, \dots , m, \\ 0, & \text {其 他}. \end{array} \right.</equation>当<equation>x_{i} > 0, y_{j} > 0, i = 1, 2, \dots , n, j = 1, 2, \dots , m</equation>时，取对数得<equation>\ln L (\theta) = - m \ln 2 - (m + n) \ln \theta - \frac {\sum_ {i = 1} ^ {n} x _ {i}}{\theta} - \frac {\sum_ {j = 1} ^ {m} y _ {j}}{2 \theta}.</equation>令<equation>\frac{\mathrm{d}\left[\ln L(\theta)\right]}{\mathrm{d}\theta}=0</equation>即<equation>-\frac{m+n}{\theta}+\frac{\sum_{i=1}^{n}x_{i}}{\theta^{2}}+\frac{\sum_{j=1}^{m}y_{j}}{2\theta^{2}}=0</equation>解得<equation>\theta=\frac{2\sum_{i=1}^{n}x_{i}+\sum_{j=1}^{m}y_{j}}{2(m+n)}</equation>因此，<equation>\theta</equation>的最大似然估计量<equation>\hat{\theta}=\frac{2\sum_{i=1}^{n}X_{i}+\sum_{j=1}^{m}Y_{j}}{2(m+n)}</equation>下面计算<equation>D(\hat{\theta})</equation><equation>\begin{aligned} D (\hat {\theta}) &= D \left[ \frac {2 \sum_ {i = 1} ^ {n} X _ {i} + \sum_ {j = 1} ^ {m} Y _ {j}}{2 (m + n)} \right] = \frac {1}{(m + n) ^ {2}} D \left(\sum_ {i = 1} ^ {n} X _ {i}\right) + \frac {1}{4 (m + n) ^ {2}} D \left(\sum_ {j = 1} ^ {m} Y _ {j}\right) \\ &= \frac {1}{(m + n) ^ {2}} \sum_ {i = 1} ^ {n} D \left(X _ {i}\right) + \frac {1}{4 (m + n) ^ {2}} \sum_ {j = 1} ^ {m} D \left(Y _ {j}\right) = \frac {n D (X)}{(m + n) ^ {2}} + \frac {m D (Y)}{4 (m + n) ^ {2}} \\ &= \frac {n \theta^ {2}}{(m + n) ^ {2}} + \frac {m \cdot 4 \theta^ {2}}{4 (m + n) ^ {2}} = \frac {\theta^ {2}}{m + n}. \end{aligned}</equation>或者，注意到<equation>\hat{\theta}=\frac{2\sum_{i=1}^{n}X_{i}+\sum_{j=1}^{m}Y_{j}}{2(m+n)}=\frac{2n\overline{X}+m\overline{Y}}{2(m+n)},</equation>利用<equation>D(\overline{X})=\frac{D(X)}{n}, D(\overline{Y})=\frac{D(Y)}{m}</equation>可得，<equation>\begin{array}{l} D (\hat {\theta}) = D \left[ \frac {2 n \bar {X} + m \bar {Y}}{2 (m + n)} \right] = \frac {n ^ {2} D (\bar {X})}{(m + n) ^ {2}} + \frac {m ^ {2} D (\bar {Y})}{4 (m + n) ^ {2}} \\ = \frac {n ^ {2}}{(m + n) ^ {2}} \cdot \frac {D (X)}{n} + \frac {m ^ {2}}{4 (m + n) ^ {2}} \cdot \frac {D (Y)}{m} \\ = \frac {n \theta^ {2}}{(m + n) ^ {2}} + \frac {m \cdot 4 \theta^ {2}}{4 (m + n) ^ {2}} = \frac {\theta^ {2}}{m + n}. \\ \end{array}</equation>

---

**2021年第10题 | 选择题 | 5分 | 答案: A**

10. 设总体 X的概率分布为<equation>P\{X=1\}=\frac{1-\theta}{2}, P\{X=2\}=P\{X=3\}=\frac{1+\theta}{4}</equation>，利用来自总体的样本值1,3,2,2,1,3,1,2可得<equation>\theta</equation>的最大似然估计值为（    ）

A.<equation>\frac{1}{4}</equation>B.<equation>\frac{3}{8}</equation>C.<equation>\frac{1}{2}</equation>D.<equation>\frac{5}{8}</equation>

答案: A

**解析:**解记<equation>P \{ X=i \}=p_{i}, i=1,2,3.</equation>由于样本值中1出现3次，2出现3次，3出现2次，故似然函数<equation>L (\theta) = p _ {1} ^ {3} p _ {2} ^ {3} p _ {3} ^ {2} = \left(\frac {1 - \theta}{2}\right) ^ {3} \left(\frac {1 + \theta}{4}\right) ^ {5} = \frac {1}{2 ^ {1 3}} (1 - \theta) ^ {3} (1 + \theta) ^ {5}.</equation>计算<equation>\ln L(\theta)</equation>得，<equation>\ln L (\theta) = - 1 3 \ln 2 + 3 \ln (1 - \theta) + 5 \ln (1 + \theta).</equation>计算<equation>\frac{\mathrm{d}\left[\ln L(\theta)\right]}{\mathrm{d}\theta}</equation>得，<equation>\frac {\mathrm {d} [ \ln L (\theta) ]}{\mathrm {d} \theta} = \frac {- 3}{1 - \theta} + \frac {5}{1 + \theta}.</equation>令<equation>\frac{\mathrm{d}[\ln L(\theta)]}{\mathrm{d}\theta}=0</equation>，可得<equation>\frac{5}{1+\theta}=\frac{3}{1-\theta}</equation>，即<equation>5(1-\theta)=3(1+\theta).</equation>，解得<equation>\theta=\frac{1}{4}.</equation>因此，应选A.

---


**2020年第22题 | 解答题 | 11分**


设二维随机变量<equation>(X,Y)</equation>在区域<equation>D = \{(x,y) \mid 0 < y < \sqrt{1 - x^2}\}</equation>上服从均匀分布，令<equation>Z _ {1} = \left\{ \begin{array}{l l} 1, & X - Y > 0, \\ 0, & X - Y \leqslant 0, \end{array} \right. \quad Z _ {2} = \left\{ \begin{array}{l l} 1, & X + Y > 0, \\ 0, & X + Y \leqslant 0. \end{array} \right.</equation>I. 求二维随机变量<equation>(Z_{1}, Z_{2})</equation>的概率分布；

II. 求<equation>Z_{1}</equation>与<equation>Z_{2}</equation>的相关系数.

**答案:**（I）<equation>Z_{1}</equation>和<equation>Z_{2}</equation>的联合分布律为

（Ⅱ）<equation>\frac{1}{3}.</equation><table border="1"><tr><td>Z1Z2</td><td>0</td><td>1</td></tr><tr><td>0</td><td><equation>\frac{1}{4}</equation></td><td>0</td></tr><tr><td>1</td><td><equation>\frac{1}{2}</equation></td><td><equation>\frac{1}{4}</equation></td></tr></table>

**解析:**解（I）区域 D如图（a）所示，为半径1的半圆盘，其面积为<equation>\frac{\pi}{2}</equation>由于（X，Y）服从区域 D上的均匀分布，故（X，Y）的联合概率密度为<equation>f (x, y) = \left\{ \begin{array}{l l} \frac {2}{\pi}, & (x, y) \in D, \\ 0, & \text {其 他}. \end{array} \right.</equation>（<equation>Z_{1}, Z_{2}</equation>）为二维离散型随机变量，其有4个可能取值（0，0），（0，1），（1，0），（1，1）.

由<equation>Z_{1}, Z_{2}</equation>的定义可知，<equation>Z_{1}=0</equation>当且仅当<equation>X\leqslant Y</equation>即（X，Y）落在直线<equation>y=x</equation>上或左侧，<equation>Z_{1}=1</equation>当且仅当<equation>X>Y</equation>即（X，Y）落在直线<equation>y=x</equation>右侧；<equation>Z_{2}=0</equation>当且仅当<equation>X\leqslant -Y</equation>即（X，Y）落在直线<equation>y=-x</equation>上或左侧，<equation>Z_{2}=1</equation>当且仅当<equation>X>-Y</equation>即（X，Y）落在直线<equation>y=-x</equation>右侧.区域<equation>D_{1}, D_{2}, D_{3}</equation>如图（b）所示.

(a)

(b)

下面计算<equation>\left(Z_{1},Z_{2}\right)</equation>的分布律.注意到 Y的取值均大于0.<equation>P \left\{Z _ {1} = 0, Z _ {2} = 0 \right\} = P \left\{X \leqslant Y, X \leqslant - Y \right\} = P \left\{X \leqslant - Y \right\} = \frac {D _ {1} \text {的 面 积}}{D \text {的 面 积}} = \frac {1}{4},</equation><equation>P \left\{Z _ {1} = 0, Z _ {2} = 1 \right\} = P \left\{X \leqslant Y, X > - Y \right\} = P \left\{- Y < X \leqslant Y \right\} = \frac {D _ {2} \text {的 面 积}}{D \text {的 面 积}} = \frac {1}{2},</equation><equation>P \left\{Z _ {1} = 1, Z _ {2} = 0 \right\} = P \left\{X > Y, X \leqslant - Y \right\} = 0,</equation><equation>P \left\{Z _ {1} = 1, Z _ {2} = 1 \right\} = P \left\{X > Y, X > - Y \right\} = P \left\{X > Y \right\} = \frac {D _ {3} \text {的 面 积}}{D \text {的 面 积}} = \frac {1}{4}.</equation>因此，<equation>Z_{1}</equation>和<equation>Z_{2}</equation>的联合分布律为

<table border="1"><tr><td>Z1Z2</td><td>0</td><td>1</td></tr><tr><td>0</td><td><equation>\frac{1}{4}</equation></td><td>0</td></tr><tr><td>1</td><td><equation>\frac{1}{2}</equation></td><td><equation>\frac{1}{4}</equation></td></tr></table>

（Ⅱ）由<equation>Z_{1}, Z_{2}</equation>的联合分布律可知，<equation>P \left\{Z _ {1} = 0 \right\} = \frac {3}{4}, \quad P \left\{Z _ {1} = 1 \right\} = \frac {1}{4};</equation><equation>P \left\{Z _ {2} = 0 \right\} = \frac {1}{4}, \quad P \left\{Z _ {2} = 1 \right\} = \frac {3}{4};</equation><equation>P \left\{Z _ {1} Z _ {2} = 0 \right\} = \frac {3}{4}, \quad P \left\{Z _ {1} Z _ {2} = 1 \right\} = \frac {1}{4}.</equation>于是<equation>E ( Z_{1} )=\frac{1}{4}, E ( Z_{1}^{2} )=\frac{1}{4}, D ( Z_{1} )=\frac{3}{1 6}; E ( Z_{2} )=\frac{3}{4}, E ( Z_{2}^{2} )=\frac{3}{4}, D ( Z_{2} )=\frac{3}{1 6};</equation><equation>E ( Z_{1} Z_{2} )=\frac{1}{4}.</equation>从而<equation>\operatorname {C o v} \left(Z _ {1}, Z _ {2}\right) = E \left(Z _ {1} Z _ {2}\right) - E \left(Z _ {1}\right) E \left(Z _ {2}\right) = \frac {1}{4} - \frac {1}{4} \times \frac {3}{4} = \frac {1}{1 6}.</equation>因此，<equation>Z_{1}</equation>与<equation>Z_{2}</equation>的相关系数<equation>\rho_ {Z _ {1} Z _ {2}} = \frac {\operatorname {C o v} \left(Z _ {1} , Z _ {2}\right)}{\sqrt {D \left(Z _ {1}\right)} \sqrt {D \left(Z _ {2}\right)}} = \frac {\frac {1}{1 6}}{\sqrt {\frac {3}{1 6} \times \frac {3}{1 6}}} = \frac {1}{3}.</equation>

---

**2018年第22题 | 解答题 | 11分**

22. (本题满分11分)

设随机变量 X与 Y相互独立，X的概率分布为<equation>P\{X=1\}=P\{X=-1\}=\frac{1}{2},</equation>Y服从参数为<equation>\lambda</equation>的泊松分布. 令<equation>Z=XY</equation>.

I. 求<equation>\operatorname{Cov}(X,Z)</equation>;

II. 求 Z的概率分布.

**答案:**(I)<equation>\operatorname{C o v} ( X, Z )=\lambda</equation>;

（Ⅱ）Z的分布律为<equation>P\{Z = i\} = \left\{ \begin{array}{ll}\frac{1}{2}\cdot \frac{\lambda^{i}\mathrm{e}^{- \lambda}}{i!}, & i > 0,\\ \mathrm{e}^{- \lambda}, & i = 0,\\ \frac{1}{2}\cdot \frac{\lambda^{-i}\mathrm{e}^{- \lambda}}{(-i)!}, & i < 0. \end{array} \right.</equation>

**解析:**解（I）（法一）注意到 X与 Y相互独立，故<equation>X^{2}</equation>与 Y也相互独立根据协方差的计算公式，<equation>\begin{array}{l} \operatorname {C o v} (X, Z) = E (X Z) - E (X) E (Z) \stackrel {Z = X Y} {=} E \left(X ^ {2} Y\right) - E (X) E (X Y) \\ \underline {{\underline {{\text {独立性}}}}} E \left(X ^ {2}\right) E (Y) - \left[ E (X) \right] ^ {2} E (Y). \\ \end{array}</equation>由于 X的概率分布为 P<equation>\{ X=1\}=P\{ X=-1\}=\frac{1}{2}</equation>，故<equation>E (X) = 1 \times \frac {1}{2} + (- 1) \times \frac {1}{2} = 0, \quad E \left(X ^ {2}\right) = 1 ^ {2} \times \frac {1}{2} + (- 1) ^ {2} \times \frac {1}{2} = 1.</equation>又因为<equation>Y</equation>服从参数为<equation>\lambda</equation>的泊松分布，所以<equation>E(Y) = \lambda</equation>因此，<equation>\operatorname {C o v} (X, Z) = E \left(X ^ {2}\right) E (Y) - \left[ E (X) \right] ^ {2} E (Y) = 1 \times \lambda - 0 = \lambda .</equation>（法二）由于<equation>X^{2}=1</equation>，故<equation>XZ=X(XY)=X^{2}Y=Y</equation>，而Y服从参数为<equation>\lambda</equation>的泊松分布，于是，<equation>E(XZ)=E(Y)=\lambda.</equation>由法一可知，<equation>E ( X ) = 0</equation>因此，<equation>\operatorname {C o v} (X, Z) = E (X Z) - E (X) E (Z) = \lambda - 0 = \lambda .</equation>（Ⅱ）由于<equation>Z=XY</equation>，故Z的所有可能的取值为i，其中i为整数.

当 i > 0时，<equation>\begin{aligned} P \{Z = i \} &= P \{X Y = i \} = P \{X = 1, Y = i \} \xlongequal {\text {独立性}} P \{X = 1 \} P \{Y = i \} \\ &= \frac {1}{2} \cdot \frac {\lambda^ {i} \mathrm {e} ^ {- \lambda}}{i !}. \end{aligned}</equation>当 i = 0时，<equation>P \{Z = 0 \} = P \{X Y = 0 \} \xlongequal {X \text {不 为} 0} P \{Y = 0 \} = \mathrm {e} ^ {- \lambda}.</equation>当 i < 0时，<equation>\begin{aligned} P \{Z = i \} &= P \{X Y = i \} = P \{X = - 1, Y = - i \} \xlongequal {\text {独立性}} P \{X = - 1 \} P \{Y = - i \} \\ &= \frac {1}{2} \cdot \frac {\lambda^ {- i} \mathrm {e} ^ {- \lambda}}{(- i) !}. \end{aligned}</equation>因此，<equation>Z</equation>的分布律为<equation>P\{Z = i\} = \left\{ \begin{array}{ll} \frac{1}{2} \cdot \frac{\lambda^{i}\mathrm{e}^{-\lambda}}{i!}, & i > 0, \\ \mathrm{e}^{-\lambda}, & i = 0, \\ \frac{1}{2} \cdot \frac{\lambda^{-i}\mathrm{e}^{-\lambda}}{(-i)!}, & i < 0. \end{array} \right.</equation>

---

**2014年第23题 | 解答题 | 11分**


设随机变量 X,Y的概率分布相同，X的概率分布为<equation>P\{X=0\}=\frac{1}{3},P\{X=1\}=\frac{2}{3}</equation>，且 X与 Y的相关系数<equation>\rho_{XY}=\frac{1}{2}.</equation>I. 求 (X,Y)的概率分布；

II. 求<equation>P\{X+Y\leqslant1\}.</equation>

**答案:**(23) （I）<equation>( X, Y )</equation>的概率分布为

（Ⅱ）<equation>\frac{4}{9}.</equation><table border="1"><tr><td>X

Y</td><td>0</td><td>1</td></tr><tr><td>0</td><td><equation>\frac{2}{9}</equation></td><td><equation>\frac{1}{9}</equation></td></tr><tr><td>1</td><td><equation>\frac{1}{9}</equation></td><td><equation>\frac{5}{9}</equation></td></tr></table>

**解析:**（ I ）设<equation>P \{ X=0, Y=0 \}=p</equation>，则<equation>P \{X = 0, Y = 1 \} = P \{X = 0 \} - P \{X = 0, Y = 0 \} = \frac {1}{3} - p,</equation><equation>P \{X = 1, Y = 0 \} = P \{Y = 0 \} - P \{X = 0, Y = 0 \} = \frac {1}{3} - p,</equation><equation>P \{X = 1, Y = 1 \} = P \{X = 1 \} - P \{X = 1, Y = 0 \} = \frac {2}{3} - \left(\frac {1}{3} - p\right) = \frac {1}{3} + p,</equation>即（X，Y）的概率分布为

<table border="1"><tr><td rowspan="2">X

Y</td><td>0</td><td>1</td></tr><tr><td>p</td><td><equation>\frac{1}{3}-p</equation></td></tr><tr><td>1</td><td><equation>\frac{1}{3}-p</equation></td><td><equation>\frac{1}{3}+p</equation></td></tr></table>

由于变量 XY可能的值为0，1，故<equation>E (X Y) = 0 \cdot P \{X Y = 0 \} + 1 \cdot P \{X Y = 1 \} = P \{X = 1, Y = 1 \} = \frac {1}{3} + p.</equation>又因为<equation>E (X) = E (Y) = 0 \times \frac {1}{3} + 1 \times \frac {2}{3} = \frac {2}{3},</equation><equation>E \left(X ^ {2}\right) = E \left(Y ^ {2}\right) = 0 ^ {2} \times \frac {1}{3} + 1 ^ {2} \times \frac {2}{3} = \frac {2}{3},</equation>所以<equation>D (X) = D (Y) = E \left(Y ^ {2}\right) - \left[ E (Y) \right] ^ {2} = \frac {2}{9}.</equation>于是，<equation>\rho_ {X Y} = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {p - \frac {1}{9}}{\frac {2}{9}} = \frac {1}{2}.</equation>解得<equation>p = \frac{2}{9}</equation>因此，<equation>(X, Y)</equation>的概率分布为

<table border="1"><tr><td>X

Y</td><td>0</td><td>1</td></tr><tr><td>0</td><td><equation>\frac{2}{9}</equation></td><td><equation>\frac{1}{9}</equation></td></tr><tr><td>1</td><td><equation>\frac{1}{9}</equation></td><td><equation>\frac{5}{9}</equation></td></tr></table>

（Ⅱ）（法一）<equation>P\{X + Y\leqslant 1\} = 1 - P\{X + Y > 1\} = 1 - P\{X = 1, Y = 1\} = 1 - \frac{5}{9} = \frac{4}{9}.</equation>(二)<equation>P \{ X + Y \leqslant 1 \} = P \{ X = 0, Y = 0 \} + P \{ X = 0, Y = 1 \} + P \{ X = 1, Y = 0 \}</equation><equation>= \frac{2}{9} +\frac{1}{9} +\frac{1}{9} = \frac{4}{9}.</equation>（法二）

---

**2012年第22题 | 解答题 | 11分**


设二维离散型随机变量<equation>(X, Y)</equation>的概率分布为

<table border="1"><tr><td>X\ Y</td><td>0</td><td>1</td><td>2</td></tr><tr><td>0</td><td>1/4</td><td>0</td><td>1/4</td></tr><tr><td>1</td><td>0</td><td>1/3</td><td>0</td></tr><tr><td>2</td><td>1/12</td><td>0</td><td>1/12</td></tr></table>

I. 求<equation>P\{X=2Y\}</equation>;

II. 求<equation>\operatorname{Cov}(X-Y,Y).</equation>

**答案:**(22) (I)<equation>\frac{1}{4}</equation>;<equation>(\mathrm {I I}) - \frac {2}{3}.</equation>

**解析:**（I）由题设知，<equation>P \{X = 2 Y \} = P \{X = 0, Y = 0 \} + P \{X = 2, Y = 1 \} = \frac {1}{4} + 0 = \frac {1}{4}.</equation>（Ⅱ）由<equation>(X,Y)</equation>的概率分布知，<equation>X,Y</equation>的概率分布分别为

<table border="1"><tr><td>X</td><td>0</td><td>1</td><td>2</td></tr><tr><td>P</td><td><equation>\frac{1}{2}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{6}</equation></td></tr></table>

<table border="1"><tr><td>Y</td><td>0</td><td>1</td><td>2</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td></tr></table>

又由于随机变量 XY可能的值为0，1，2，4，故XY的概率分布为<equation>\begin{aligned} P \{X Y = 0 \} &= P \{X = 0, Y = 0 \} + P \{X = 0, Y = 1 \} + P \{X = 0, Y = 2 \} \\ + P \{X = 1, Y = 0 \} + P \{X = 2, Y = 0 \} \\ &= \frac {1}{4} + 0 + \frac {1}{4} + 0 + \frac {1}{1 2} = \frac {7}{1 2}, \end{aligned}</equation><equation>P \{X Y = 1 \} = P \{X = 1, Y = 1 \} = \frac {1}{3},</equation><equation>P \{X Y = 2 \} = P \{X = 1, Y = 2 \} + P \{X = 2, Y = 1 \} = 0 + 0 = 0,</equation><equation>P \{X Y = 4 \} = P \{X = 2, Y = 2 \} = \frac {1}{1 2},</equation>即

<table border="1"><tr><td>XY</td><td>0</td><td>1</td><td>4</td></tr><tr><td>P</td><td><equation>\frac{7}{12}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{12}</equation></td></tr></table>

于是，<equation>E (X) = 0 \times \frac {1}{2} + 1 \times \frac {1}{3} + 2 \times \frac {1}{6} = \frac {2}{3},</equation><equation>E (Y) = 0 \times \frac {1}{3} + 1 \times \frac {1}{3} + 2 \times \frac {1}{3} = 1,</equation><equation>E \left(Y ^ {2}\right) = 0 ^ {2} \times \frac {1}{3} + 1 ^ {2} \times \frac {1}{3} + 2 ^ {2} \times \frac {1}{3} = \frac {5}{3},</equation><equation>E (X Y) = 0 \times \frac {7}{1 2} + 1 \times \frac {1}{3} + 4 \times \frac {1}{1 2} = \frac {2}{3}.</equation>因此，<equation>\begin{aligned} \operatorname {C o v} (X - Y, Y) &= \operatorname {C o v} (X, Y) - \operatorname {C o v} (Y, Y) = \left[ E (X Y) - E (X) E (Y) \right] - \left[ E \left(Y ^ {2}\right) - \left[ E (Y) \right] ^ {2} \right] \\ &= \left(\frac {2}{3} - \frac {2}{3} \times 1\right) - \left(\frac {5}{3} - 1 ^ {2}\right) = - \frac {2}{3}. \end{aligned}</equation>

---

**2011年第22题 | 解答题 | 11分**


设随机变量<equation>X</equation>与<equation>Y</equation>的概率分布分别为

<table border="1"><tr><td>X</td><td>0</td><td>1</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{2}{3}</equation></td></tr></table>

<table border="1"><tr><td>Y</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td></tr></table>

且<equation>P\{X^{2}=Y^{2}\}=1.</equation>I. 求二维随机变量<equation>(X, Y)</equation>的概率分布；

II. 求<equation>Z=XY</equation>的概率分布；

III. 求 X与Y的相关系数<equation>\rho_{XY}</equation>

**答案:**(22) （I）<equation>( X, Y )</equation>的概率分布为

<table border="1"><tr><td rowspan="2">X\ Y</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>0</td><td><equation>\frac{1}{3}</equation></td><td>0</td></tr><tr><td>1</td><td><equation>\frac{1}{3}</equation></td><td>0</td><td><equation>\frac{1}{3}</equation></td></tr></table>

（Ⅱ）<equation>Z=XY</equation>的概率分布为

<table border="1"><tr><td>Z</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td></tr></table>

（Ⅲ）0.

**解析:**解（I）由<equation>P\{X^{2}=Y^{2}\}=1</equation>知，<equation>P\{X^{2}\neq Y^{2}\}=0.</equation>于是，<equation>P \{X = 0, Y = - 1 \} = P \{X = 0, Y = 1 \} = P \{X = 1, Y = 0 \} = 0.</equation>从而<equation>P \{X = 0, Y = 0 \} = P \{Y = 0 \} - P \{X = 1, Y = 0 \} = \frac {1}{3} - 0 = \frac {1}{3},</equation><equation>P \{X = 1, Y = 1 \} = P \{Y = 1 \} - P \{X = 0, Y = 1 \} = \frac {1}{3} - 0 = \frac {1}{3},</equation><equation>P \{X = 1, Y = - 1 \} = P \{Y = - 1 \} - P \{X = 0, Y = - 1 \} = \frac {1}{3} - 0 = \frac {1}{3}.</equation>因此，<equation>(X, Y)</equation>的概率分布为

<table border="1"><tr><td>X\ Y</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>0</td><td><equation>\frac{1}{3}</equation></td><td>0</td></tr><tr><td>1</td><td><equation>\frac{1}{3}</equation></td><td>0</td><td><equation>\frac{1}{3}</equation></td></tr></table>

（Ⅱ）由于<equation>Z=XY</equation>可能的取值为-1，0，1，且<equation>P \{Z = - 1 \} = P \{X = 1, Y = - 1 \} = \frac {1}{3},</equation><equation>P \{Z = 1 \} = P \{X = 1, Y = 1 \} = \frac {1}{3},</equation><equation>P \{Z = 0 \} = 1 - P \{Z = - 1 \} - P \{Z = 1 \} = \frac {1}{3},</equation>（或者<equation>P\{Z = 0\} = P\{X = 0, Y = 0\} + P\{X = 0, Y = -1\} + P\{X = 0, Y = 1\} + P\{X = 1, Y = 0\} = \frac{1}{3},</equation>）故<equation>Z = X Y</equation>的概率分布为

<table border="1"><tr><td>Z</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>P</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{3}</equation></td></tr></table><equation>E (X) = 0 \times \frac {1}{3} + 1 \times \frac {2}{3} = \frac {2}{3}, \quad E \left(X ^ {2}\right) = 0 ^ {2} \times \frac {1}{3} + 1 ^ {2} \times \frac {2}{3} = \frac {2}{3},</equation>（Ⅲ）由于<equation>D (X) = E \left(X ^ {2}\right) - \left[ E (X) \right] ^ {2} = \frac {2}{9},</equation><equation>E (Y) = (- 1) \times \frac {1}{3} + 0 \times \frac {1}{3} + 1 \times \frac {1}{3} = 0, \quad E \left(Y ^ {2}\right) = (- 1) ^ {2} \times \frac {1}{3} + 0 ^ {2} \times \frac {1}{3} + 1 ^ {2} \times \frac {1}{3} = \frac {2}{3},</equation><equation>D (Y) = E \left(Y ^ {2}\right) - \left[ E (Y) \right] ^ {2} = \frac {2}{3},</equation><equation>E (X Y) = E (Z) = (- 1) \times \frac {1}{3} + 0 \times \frac {1}{3} + 1 \times \frac {1}{3} = 0,</equation>故<equation>\rho_ {X Y} = \frac {\operatorname {C o v} (X , Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = 0.</equation>

---

**2017年第22题 | 解答题 | 11分**


设随机变量 X，Y相互独立，且 X的概率分布为<equation>P\{X=0\}=P\{X=2\}=\frac{1}{2},</equation>Y的概率密度为<equation>f (y) = \left\{ \begin{array}{l l} 2 y, & 0 < y < 1, \\ 0, & \text {其 他}. \end{array} \right.</equation>I. 求<equation>P\{Y\leqslant E(Y)\} ;</equation>II. 求<equation>Z=X+Y</equation>的概率密度

**答案:**<equation>\frac {4}{9};</equation>（Ⅱ）<equation>f_{Z}(z)=\left\{ \begin{array}{ll} z, & 0<z<1,\\ z-2, & 2<z<3,\\ 0, & \text{其他}. \end{array} \right.</equation>

**解析:**解（I）由题设知，<equation>E ( Y )=\int_{-\infty}^{+\infty} y f ( y ) \mathrm{d} y=\int_{0}^{1} 2 y^{2} \mathrm{d} y=\frac{2}{3}.</equation>因此，<equation>P \left\{Y \leqslant E (Y) \right\} = P \left\{Y \leqslant \frac {2}{3} \right\} = \int_ {0} ^ {\frac {2}{3}} 2 y \mathrm {d} y = \frac {4}{9}.</equation>（Ⅱ）Z的分布函数为<equation>\begin{aligned} F _ {Z} (z) &= P \{Z \leqslant z \} = P \{X + Y \leqslant z \} \\ &= P \{X + Y \leqslant z, X = 0 \} + P \{X + Y \leqslant z, X = 2 \} \\ &= P \{Y \leqslant z, X = 0 \} + P \{Y \leqslant z - 2, X = 2 \} \\ \underline {{\underline {{X , Y \text {相 互 独立}}}}} P \{Y \leqslant z \} \cdot P \{X = 0 \} + P \{Y \leqslant z - 2 \} \cdot P \{X = 2 \} \\ &= \frac {1}{2} P \{Y \leqslant z \} + \frac {1}{2} P \{Y \leqslant z - 2 \}. \end{aligned}</equation>下面用两种方法求 Z的概率密度.

（法一）如图所示，当<equation>z\leqslant 0</equation>时，<equation>F_{z}(z) = 0 + 0 = 0.</equation>当<equation>0 < z\leqslant 1</equation>时，<equation>F_{Z}(z) = \frac{1}{2}\int_{0}^{z}2y\mathrm{d}y + 0 = \frac{z^{2}}{2}.</equation>当<equation>1 < z\leqslant 2</equation>时，<equation>F_{z}(z) = \frac{1}{2}\int_{0}^{1}2y\mathrm{d}y + 0 = \frac{1}{2}</equation>.

当<equation>2 < z\leqslant 3</equation>时，<equation>F_{z}(z) = \frac{1}{2} +\frac{1}{2}\int_{0}^{z - 2}2y\mathrm{d}y = \frac{1}{2} +\frac{(z - 2)^{2}}{2}.</equation>当<equation>z > 3</equation>时，<equation>F_{Z}(z) = 1.</equation>综上所述，Z的概率密度为<equation>f _ {Z} (z) = F _ {Z} ^ {\prime} (z) = \left\{ \begin{array}{l l} z, & 0 < z < 1, \\ z - 2, & 2 < z < 3, \\ 0, & \text {其 他}. \end{array} \right.</equation>（法二）由 Z的分布函数<equation>F_{Z}(z)=\frac{1}{2} P\{Y\leqslant z\} +\frac{1}{2} P\{Y\leqslant z-2\}</equation>知，Z的概率密度为<equation>f _ {Z} (z) = F _ {Z} ^ {\prime} (z) = \frac {1}{2} f (z) + \frac {1}{2} f (z - 2).</equation>当<equation>z\leqslant 0</equation>时，<equation>z - 2\leqslant 0,f_{z}(z) = 0 + 0 = 0.</equation>当<equation>0 < z < 1</equation>时，<equation>z-2\leqslant 0,f_{Z}(z)=\frac{1}{2}\cdot 2z+0=z.</equation>当<equation>1\leqslant z\leqslant 2</equation>时，<equation>z - 2\leqslant 0,f_{z}(z) = 0 + 0 = 0.</equation>当<equation>2 < z < 3</equation>时，<equation>0 < z - 2 < 1,f_{Z}(z) = 0 + \frac{1}{2}\cdot 2(z - 2) = z - 2.</equation>当<equation>z\geqslant 3</equation>时，<equation>z - 2\geqslant 1,f_{Z}(z) = 0 + 0 = 0.</equation>综上所述，<equation>f_{Z}(z)=\left\{ \begin{array}{ll} z, & 0<z<1,\\ z-2, & 2<z<3,\\ 0, & \text{其他}. \end{array} \right.</equation>

---

**2016年第8题 | 选择题 | 4分 | 答案: C**

8. 设随机变量 X与 Y相互独立，且<equation>X\sim N(1,2),Y\sim N(1,4)</equation>，则<equation>D(XY)=</equation>(    )

A.6 B.8 C.14 D.15

答案: C

**解析:**解 由于<equation>X\sim N(1,2), Y\sim N(1,4)</equation>，故<equation>E(X)=E(Y)=1,D(X)=2,D(Y)=4.</equation>又由于随机变量 X与 Y相互独立，故<equation>X^{2}</equation>与<equation>Y^{2}</equation>也相互独立.于是，<equation>\begin{array}{l} E \left(X ^ {2} Y ^ {2}\right) = E \left(X ^ {2}\right) E \left(Y ^ {2}\right) = \left\{\left[ E (X) \right] ^ {2} + D (X) \right\} \left\{\left[ E (Y) \right] ^ {2} + D (Y) \right\} \\ = (1 + 2) (1 + 4) = 1 5, \\ \end{array}</equation><equation>E (X Y) = E (X) E (Y) = 1.</equation>因此，<equation>D (X Y) = E \left(X ^ {2} Y ^ {2}\right) - \left[ E (X Y) \right] ^ {2} = 1 5 - 1 = 1 4.</equation>应选C.

---


**2010年第23题 | 解答题 | 11分**


23. (本题满分11分)

箱中装有6个球，其中红、白、黑球的个数分别为1,2,3个. 现从箱中随机地取出2个球，记X为取出的红球个数，Y为取出的白球个数.

I. 求随机变量（X，Y）的概率分布；

II. 求<equation>\operatorname{C o v} ( X, Y ).</equation>

**答案:**(23) （I）随机变量<equation>(X, Y)</equation>的概率分布为

<table border="1"><tr><td rowspan="2">X\ Y</td><td>0</td><td>1</td><td>2</td></tr><tr><td><equation>\frac{1}{5}</equation></td><td><equation>\frac{2}{5}</equation></td><td><equation>\frac{1}{15}</equation></td></tr><tr><td>1</td><td><equation>\frac{1}{5}</equation></td><td><equation>\frac{2}{15}</equation></td><td>0</td></tr></table>

（Ⅱ）<equation>- \frac{4}{45}.</equation>

**解析:**解 （I）记Z为取出的黑球个数.由已知条件知X可能的取值为0，1；Y可能的取值为0，1，2.由于<equation>P \{X = 0, Y = 0 \} = P \{Z = 2 \} = \frac {\mathrm {C} _ {3} ^ {2}}{\mathrm {C} _ {6} ^ {2}} = \frac {1}{5},</equation><equation>P \{X = 0, Y = 1 \} = P \{Y = 1, Z = 1 \} = \frac {\mathrm {C} _ {2} ^ {1} \mathrm {C} _ {3} ^ {1}}{\mathrm {C} _ {6} ^ {2}} = \frac {2}{5},</equation><equation>P \{X = 0, Y = 2 \} = P \{Y = 2 \} = \frac {\mathrm {C} _ {2} ^ {2}}{\mathrm {C} _ {6} ^ {2}} = \frac {1}{1 5},</equation><equation>P \left\{X = 1, Y = 0 \right\} ^ {\prime} = P \left\{X = 1, Z = 1 \right\} = \frac {\mathrm {C} _ {1} ^ {1} \mathrm {C} _ {3} ^ {1}}{\mathrm {C} _ {6} ^ {2}} = \frac {1}{5},</equation><equation>P \left\{X = 1, Y = 1 \right\} = \frac {\mathrm {C} _ {1} ^ {1} \mathrm {C} _ {2} ^ {1}}{\mathrm {C} _ {6} ^ {2}} = \frac {2}{1 5},</equation><equation>P \{X = 1, Y = 2 \} = P (\varnothing) = 0,</equation>故随机变量（X，Y）的概率分布为

<table border="1"><tr><td>X\ Y</td><td>0</td><td>1</td><td>2</td></tr><tr><td>0</td><td><equation>\frac{1}{5}</equation></td><td><equation>\frac{2}{5}</equation></td><td><equation>\frac{1}{15}</equation></td></tr><tr><td>1</td><td><equation>\frac{1}{5}</equation></td><td><equation>\frac{2}{15}</equation></td><td>0</td></tr></table>

（Ⅱ）随机变量 XY可能的取值为0,1.

由于<equation>P \{ X Y=1 \} = P \{ X=1, Y=1 \} = \frac{2}{1 5}</equation>，故<equation>P \{ X Y=0 \} = 1 - P \{ X Y=1 \} = \frac{1 3}{1 5}</equation>（或者利用<equation>P \{ X Y=0 \} = P \{ X=0, Y=0 \} + P \{ X=0, Y=1 \} + P \{ X=0, Y=2 \} + P \{ X=1, Y=0 \} )</equation>.于是，<equation>E (X Y) = 0 \times \frac {1 3}{1 5} + 1 \times \frac {2}{1 5} = \frac {2}{1 5}.</equation>因为<equation>E (X) = 0 \cdot P \{X = 0 \} + 1 \cdot P \{X = 1 \} = P \{X = 1 \} = \frac {2}{1 5} + \frac {1}{5} = \frac {1}{3},</equation><equation>E (Y) = 0 \cdot P \{Y = 0 \} + 1 \cdot P \{Y = 1 \} + 2 \cdot P \{Y = 2 \} = 1 \times \left(\frac {2}{5} + \frac {2}{1 5}\right) + 2 \times \frac {1}{1 5} = \frac {2}{3},</equation>所以<equation>\operatorname {C o v} (X, Y) = E (X Y) - E (X) E (Y) = \frac {2}{1 5} - \frac {1}{3} \times \frac {2}{3} = - \frac {4}{4 5}.</equation>

---

**2011年第23题 | 解答题 | 11分**


设二维随机变量（X，Y）服从区域G上的均匀分布，其中G是由 x-y=0，x+y=2与 y=0所围成的三角形区域.

I. 求 X的概率密度<equation>f_{X}(x)</equation>;

II. 求条件概率密度<equation>f_{X|Y}(x \mid y).</equation>

**答案:**(23) （I）<equation>f_{X}(x)=\left\{\begin{array}{ll}x,&0<x\leqslant 1,\\ 2-x,&1<x\leqslant 2,\\ 0,&\text{其他};\end{array}\right.</equation>（Ⅱ）<equation>f_{X\mid Y}(x\mid y)=\left\{\begin{array}{ll}\frac{1}{2-2y},&y<x<2-y,\\ 0,&\text{其他}.\end{array}\right.</equation>

**解析:**(a)

(b)

(c)

解（I）如图（a）所示，G是一个底为2，高为1的三角形区域，故面积为1.于是二维随机变量 （X，Y）的概率密度为<equation>f (x, y) = \left\{ \begin{array}{l l} 1, & (x, y) \in G, \\ 0, & \text {其 他}, \end{array} \right.</equation>这里<equation>G = \{(x,y) \mid y \leqslant x \leqslant 2 - y, 0 \leqslant y \leqslant 1\}</equation>.

当<equation>x\leqslant 0</equation>时，<equation>f_{X}(x) = \int_{-\infty}^{+\infty}f(x,y)\mathrm{d}y = 0.</equation>当<equation>0 < x\leqslant 1</equation>时，<equation>f_{X}(x) = \int_{- \infty}^{+ \infty} f(x,y)\mathrm{d}y = \int_{0}^{x}1\mathrm{d}y = x.</equation>当<equation>1 < x\leqslant 2</equation>时，<equation>f_{X}(x) = \int_{-\infty}^{+\infty}f(x,y)\mathrm{d}y = \int_{0}^{2 - x}1\mathrm{d}y = 2 - x.</equation>当<equation>x > 2</equation>时，<equation>f_{X}(x) = \int_{- \infty}^{+ \infty} f(x,y)\mathrm{d}y = 0.</equation>综上所述，<equation>X</equation>的概率密度为<equation>f_{X}(x) = \left\{ \begin{array}{ll} x, & 0 < x \leqslant 1, \\ 2 - x, & 1 < x \leqslant 2, \\ 0, & \text{其他}. \end{array} \right.</equation>（Ⅱ）当<equation>0\leqslant y < 1</equation>时，<equation>f_{Y}(y) = \int_{- \infty}^{+ \infty} f(x,y)\mathrm{d}x = \int_{y}^{2 - y}1\mathrm{d}x = 2 - 2y.</equation>当<equation>y < 0</equation>或<equation>y\geqslant 1</equation>时，<equation>f_{Y}(y) = \int_{- \infty}^{+ \infty} f(x,y)\mathrm{d}x = 0.</equation>由于条件概率密度<equation>f_{X|Y}(x|y)</equation>是在Y的取值y满足<equation>f_{Y}(y) > 0</equation>的前提下定义的，故我们只考虑<equation>0\leqslant y < 1</equation>的情形.因此，在<equation>Y=y(0\leqslant y < 1)</equation>时，X的条件概率密度为<equation>f _ {X \mid Y} (x \mid y) = \frac {f (x , y)}{f _ {Y} (y)} = \left\{ \begin{array}{l l} \frac {1}{2 - 2 y}, & y < x < 2 - y, \\ 0, & \text {其 他}. \end{array} \right.</equation>

---

**2010年第22题 | 解答题 | 11分**

22. (本题满分11分)

设二维随机变量（X，Y）的概率密度为<equation>f ( x, y )=A \mathrm{e}^{-2 x^{2}+2 x y-y^{2}}</equation><equation>(-\infty < x < +\infty,-\infty < y < +\infty).</equation>求常数 A及条件概率密度<equation>f_{Y|X}(y\mid x).</equation>

**答案:**(22)<equation>A=\frac{1}{\pi}, f_{Y\mid X}(y\mid x)=\frac{1}{\sqrt{\pi}} \mathrm{e}^{-(x-y)^{2}}, y\in(-\infty ,+\infty).</equation>

**解析:**解 由概率密度的性质可知，<equation>\int_{- \infty}^{+ \infty}\int_{- \infty}^{+ \infty}f(x,y)\mathrm{d}x\mathrm{d}y=1.</equation>由于<equation>\begin{aligned} \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} x \mathrm {d} y &= \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} A \mathrm {e} ^ {- 2 x ^ {2} + 2 x y - y ^ {2}} \mathrm {d} x \mathrm {d} y = \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} A \mathrm {e} ^ {- x ^ {2} - (y - x) ^ {2}} \mathrm {d} x \mathrm {d} y \\ &= A \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- x ^ {2}} \mathrm {d} x \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- (y - x) ^ {2}} \mathrm {d} y = A \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- x ^ {2}} \mathrm {d} x \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- (y - x) ^ {2}} \mathrm {d} (y - x) \\ &= A \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- x ^ {2}} \mathrm {d} x \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t \frac {\int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t = \sqrt {\pi}}{A \pi}, \end{aligned}</equation>故<equation>A\pi = 1</equation>，从而<equation>A = \frac{1}{\pi}</equation>由条件概率密度的定义可知，<equation>f_{Y \mid X}(y \mid x) = \frac{f(x,y)}{f_X(x)}.</equation>又由于<equation>f _ {X} (x) = \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} y = \frac {1}{\pi} \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- 2 x ^ {2} + 2 x y - y ^ {2}} \mathrm {d} y = \frac {1}{\pi} \mathrm {e} ^ {- x ^ {2}} \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- (y - x) ^ {2}} \mathrm {d} y = \frac {1}{\pi} \mathrm {e} ^ {- x ^ {2}} \cdot \sqrt {\pi} = \frac {1}{\sqrt {\pi}} \mathrm {e} ^ {- x ^ {2}},</equation>故对任意给定的<equation>x\in(-\infty , + \infty)</equation>，在<equation>X = x</equation>的条件下，<equation>Y</equation>的条件概率密度为<equation>f _ {Y \mid X} (y \mid x) = \frac {f (x , y)}{f _ {X} (x)} = \frac {\frac {1}{\pi} \mathrm {e} ^ {- 2 x ^ {2} + 2 x y - y ^ {2}}}{\frac {1}{\sqrt {\pi}} \mathrm {e} ^ {- x ^ {2}}} = \frac {1}{\sqrt {\pi}} \mathrm {e} ^ {- x ^ {2} + 2 x y - y ^ {2}} = \frac {1}{\sqrt {\pi}} \mathrm {e} ^ {- (x - y) ^ {2}}, y \in (- \infty , + \infty).</equation>

---

**2009年第22题 | 解答题 | 11分**

22. (本题满分11分)

设二维随机变量（X，Y）的概率密度为 f(x,y) =<equation>\left\{\begin{array}{ll} \mathrm{e}^{-x}, & 0<y<x, \\ 0, & \mathrm{其他}. \end{array} \right.</equation>I. 求条件概率密度<equation>f_{Y|X}(y|x)</equation>II. 求条件概率<equation>P\{X\leqslant1\mid Y\leqslant1\}</equation>

**答案:**（22）（I）当<equation>f_{X}(x)\neq0</equation>，即 x > 0时，<equation>f_{Y\mid X}(y\mid x)=\frac{f(x,y)}{f_{X}(x)}=\left\{\begin{array}{ll}\frac{1}{x},&0<y<x,\\ 0,&\text{其他};\end{array}\right.</equation>（Ⅱ）<equation>\frac{\mathrm{e}-2}{\mathrm{e}-1}.</equation>

**解析:**解（I）由边缘概率密度的定义可知，当<equation>x > 0</equation>时，<equation>f _ {X} (x) = \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} y = \int_ {0} ^ {x} \mathrm {e} ^ {- x} \mathrm {d} y = x \mathrm {e} ^ {- x};</equation>当<equation>x\leqslant 0</equation>时，<equation>f _ {X} (x) = \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} y = 0.</equation>因此，当<equation>f_{X}(x) \neq 0</equation>，即<equation>x > 0</equation>时，<equation>Y</equation>在<equation>X = x</equation>的条件下的条件概率密度为<equation>f _ {Y \mid X} (y \mid x) = \frac {f (x , y)}{f _ {X} (x)} = \left\{ \begin{array}{l l} \frac {1}{x}, & 0 < y < x, \\ 0, & \text {其 他}. \end{array} \right.</equation>（Ⅱ）（法一）由条件概率的定义知<equation>\begin{aligned} P \{X \leqslant 1 \mid Y \leqslant 1 \} &= \frac {P \{X \leqslant 1 , Y \leqslant 1 \}}{P \{Y \leqslant 1 \}} = \frac {\int_ {- \infty} ^ {1} \mathrm {d} x \int_ {- \infty} ^ {1} f (x , y) \mathrm {d} y}{\int_ {- \infty} ^ {+ \infty} \mathrm {d} x \int_ {- \infty} ^ {1} f (x , y) \mathrm {d} y} \stackrel {*} {=} \frac {\int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {x} \mathrm {e} ^ {- x} \mathrm {d} y}{\int_ {0} ^ {1} \mathrm {d} y \int_ {y} ^ {+ \infty} \mathrm {e} ^ {- x} \mathrm {d} x} \\ &= \frac {\int_ {0} ^ {1} x \mathrm {e} ^ {- x} \mathrm {d} x}{\int_ {0} ^ {1} \mathrm {e} ^ {- y} \mathrm {d} y} = \frac {- x \mathrm {e} ^ {- x} \left| _ {0} ^ {1} + \int_ {0} ^ {1} \mathrm {e} ^ {- x} \mathrm {d} x \right.}{- \mathrm {e} ^ {- y} \left| _ {0} ^ {1} \right.} = \frac {1 - 2 \mathrm {e} ^ {- 1}}{1 - \mathrm {e} ^ {- 1}} = \frac {\mathrm {e} - 2}{\mathrm {e} - 1}. \end{aligned}</equation>（法二）由边缘概率密度的定义可知，当<equation>y > 0</equation>时，<equation>f _ {Y} (y) = \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} x = \int_ {y} ^ {+ \infty} \mathrm {e} ^ {- x} \mathrm {d} x = - \mathrm {e} ^ {- x} \Big | _ {y} ^ {+ \infty} = \mathrm {e} ^ {- y};</equation>当 y≤0时，<equation>f _ {Y} (y) = \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} x = 0.</equation>于是，<equation>P \left\{Y \leqslant 1 \right\} = \int_ {- \infty} ^ {1} f _ {Y} (y) \mathrm {d} y = \int_ {0} ^ {1} \mathrm {e} ^ {- y} \mathrm {d} y = 1 - \mathrm {e} ^ {- 1}.</equation>又因为<equation>P \left\{X \leqslant 1, Y \leqslant 1 \right\} = \int_ {- \infty} ^ {1} \mathrm {d} x \int_ {- \infty} ^ {1} f (x, y) \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {x} \mathrm {e} ^ {- x} \mathrm {d} y = \int_ {0} ^ {1} x \mathrm {e} ^ {- x} \mathrm {d} x = 1 - 2 \mathrm {e} ^ {- 1},</equation>所以由条件概率的定义知，<equation>P \{X \leqslant 1 \mid Y \leqslant 1 \} = \frac {P \{X \leqslant 1 , Y \leqslant 1 \}}{P \{Y \leqslant 1 \}} = \frac {1 - 2 \mathrm {e} ^ {- 1}}{1 - \mathrm {e} ^ {- 1}} = \frac {\mathrm {e} - 2}{\mathrm {e} - 1}.</equation>

---

**2016年第23题 | 解答题 | 11分**


设总体<equation>X</equation>的概率密度为<equation>f (x; \theta) = \left\{ \begin{array}{l l} \frac {3 x ^ {2}}{\theta^ {3}}, & 0 < x < \theta , \\ 0, & \text {其 他}, \end{array} \right.</equation>其中<equation>\theta\in(0,+\infty)</equation>为未知参数，<equation>X_{1},X_{2},X_{3}</equation>为来自总体 X的简单随机样本，令<equation>T=\max\{X_{1},X_{2},X_{3}\}</equation>I. 求 T的概率密度； II. 确定 a，使得<equation>E(aT)=\theta.</equation>

**答案:**（I）<equation>f_{T}(t)=\left\{\begin{array}{ll}\frac{9 t^{8}}{\theta^{9}},&0<t<\theta,\\ 0,&\text{其他};\end{array}\right.</equation>（Ⅱ）当 a<equation>=\frac{10}{9}</equation>时，<equation>E(aT)=\theta.</equation>

**解析:**解（I）设 T的分布函数为<equation>F_{T}(t), T</equation>的概率密度为<equation>f_{T}(t).</equation>由于<equation>X_{1}, X_{2}, X_{3}</equation>为来自总体 X的简单随机样本，故它们相互独立且与 X同分布.从而<equation>\begin{array}{l} F _ {T} (t) = P \{T \leqslant t \} = P \left\{X _ {1} \leqslant t, X _ {2} \leqslant t, X _ {3} \leqslant t \right\} = P \left\{X _ {1} \leqslant t \right\} \cdot P \left\{X _ {2} \leqslant t \right\} \cdot P \left\{X _ {3} \leqslant t \right\} \\ = \left[ P \left\{X \leqslant t \right\} \right] ^ {3} = \left[ F _ {X} ^ {\prime} (t) \right] ^ {3}, \\ \end{array}</equation>其中<equation>F_{X}(t)</equation>为X的分布函数.

下面用两种方法求<equation>f_{T}(t)</equation>（法一）先求<equation>F_{T}(t)</equation>，再求导得到<equation>f_{T}(t)</equation>当<equation>t < 0</equation>时，<equation>F_{X}(t) = \int_{-\infty}^{t} f(x;\theta)\mathrm{d}x = 0.</equation>于是<equation>F_{T}(t) = \left[ F_{X}(t)\right]^{3} = 0.</equation>当<equation>0 \leqslant t < \theta</equation>时，<equation>F_{X}(t) = \int_{-\infty}^{t} f(x; \theta)\mathrm{d}x = \int_{0}^{t}\frac{3x^{2}}{\theta^{3}}\mathrm{d}x = \frac{t^{3}}{\theta^{3}}.</equation>于是<equation>F_{T}(t) = [F_{X}(t)]^{3} = \frac{t^{9}}{\theta^{9}}.</equation>当<equation>t \geqslant \theta</equation>时，<equation>F_{X}(t) = 1.</equation>于是<equation>F_{T}(t) = \left[ F_{X}(t) \right]^{3} = 1.</equation>因此，<equation>F _ {T} (t) = \left\{ \begin{array}{l l} 0, & t < 0, \\ \frac {t ^ {9}}{\theta^ {9}}, & 0 \leqslant t < \theta , \\ 1, & t \geqslant \theta . \end{array} \right.</equation>综上所述，<equation>T</equation>的概率密度为<equation>f_{T}(t) = F_{T}^{\prime}(t) = \left\{ \begin{array}{ll}\frac{9t^{8}}{\theta^{9}}, & 0 < t < \theta ,\\ 0, & \text{其他}. \end{array} \right.</equation>（法二）直接求导得到<equation>f_{T}(t)</equation>后再求解.<equation>f _ {T} (t) = F _ {T} ^ {\prime} (t) = 3 F _ {X} ^ {\prime} (t) \left[ F _ {X} (t) \right] ^ {2} = 3 f (t; \theta) \left[ F _ {X} (t) \right] ^ {2}.</equation>当<equation>t < 0</equation>时，<equation>f(t; \theta) = 0.</equation>于是<equation>f_{T}(t) = 0.</equation>当<equation>0\leqslant t < \theta</equation>时，<equation>F_{X}(t) = \int_{-\infty}^{t} f(x;\theta)\mathrm{d}x = \int_{0}^{t}\frac{3x^{2}}{\theta^{3}}\mathrm{d}x = \frac{t^{3}}{\theta^{3}}.</equation>于是<equation>f _ {T} (t) = 3 f (t; \theta) \left[ F _ {X} (t) \right] ^ {2} = 3 \cdot \frac {3 t ^ {2}}{\theta^ {3}} \cdot \left(\frac {t ^ {3}}{\theta^ {3}}\right) ^ {2} = \frac {9 t ^ {8}}{\theta^ {9}}.</equation>当<equation>t \geqslant \theta</equation>时，<equation>f(t; \theta) = 0.</equation>于是<equation>f_{T}(t) = 0.</equation>综上所述，<equation>T</equation>的概率密度为<equation>f_{T}(t)=\left\{ \begin{array}{ll}\frac{9 t^{8}}{\theta^{9}},&0<t<\theta ,\\ 0,&\text{其他}. \end{array} \right.</equation>（Ⅱ）由第（Ⅰ）问中所求结果知，<equation>E (a T) = a E (T) = a \int_ {- \infty} ^ {+ \infty} t f _ {T} (t) \mathrm {d} t = a \int_ {0} ^ {\theta} \frac {9 t ^ {9}}{\theta^ {9}} \mathrm {d} t = \frac {9 a}{1 0 \theta^ {9}} t ^ {1 0} \Bigg | _ {0} ^ {\theta} = \frac {9}{1 0} a \theta .</equation>要使<equation>E ( a T)=\theta</equation>，则<equation>\frac{9}{10} a\theta =\theta</equation>，解得<equation>a=\frac{10}{9}.</equation>因此，当<equation>a = \frac{10}{9}</equation>时，<equation>E(aT) = \theta .</equation>

---

**2015年第22题 | 解答题 | 11分**

22. (本题满分11分)

设随机变量 X的概率密度为<equation>f ( x )=\left\{\begin{array}{ll}2^{-x}\ln 2,&x>0,\\ 0,&x\leqslant 0.\end{array} \right.</equation>对 X 进行独立重复的观测，直到第2个大于3的观测值出现时停止，记 Y为观测次数.

I. 求 Y的既率分布；

II. 求 E(Y).

**答案:**(22) （I）Y的概率分布为<equation>P \{Y = k \} = \frac {1}{6 4} (k - 1) \left(\frac {7}{8}\right) ^ {k - 2}, \quad k = 2, 3, 4, \dots ;</equation>

**解析:**解（ I ）由题设知，<equation>P \left\{X \leqslant 3 \right\} = \int_ {- \infty} ^ {3} f (x) \mathrm {d} x = \int_ {0} ^ {3} 2 ^ {- x} \ln 2 \mathrm {d} x = - 2 ^ {- x} \Bigg | _ {0} ^ {3} = - \frac {1}{8} - (- 1) = \frac {7}{8},</equation><equation>P \{X > 3 \} = 1 - P \{X \leqslant 3 \} = 1 - \frac {7}{8} = \frac {1}{8}.</equation>Y可能的取值为2，3，4，….又由于<equation>Y=k(k\geqslant 2)</equation>意味着前k-1次只有1次出现大于3的观测值，且第k次出现大于3的观测值，故Y的概率分布为<equation>P \{Y = k \} = C _ {k - 1} ^ {1} \times \frac {1}{8} \times \left(\frac {7}{8}\right) ^ {k - 2} \times \frac {1}{8} = \frac {1}{6 4} (k - 1) \left(\frac {7}{8}\right) ^ {k - 2}, \quad k = 2, 3, 4, \dots .</equation>（Ⅱ）（法一）由期望的定义知，<equation>E (Y) = \sum_ {k = 2} ^ {\infty} k \cdot P \{Y = k \} = \frac {1}{6 4} \sum_ {k = 2} ^ {\infty} k (k - 1) \left(\frac {7}{8}\right) ^ {k - 2}.</equation>考虑幂级数<equation>\sum_{k = 2}^{\infty}k(k - 1)x^{k - 2}</equation>，其收敛域为（-1，1），故该级数在<equation>x = \frac{7}{8}</equation>处收敛.当<equation>x\in(-1,1)</equation>时，<equation>\begin{aligned} \sum_ {k = 2} ^ {\infty} k (k - 1) x ^ {k - 2} &= \sum_ {k = 2} ^ {\infty} \left(x ^ {k}\right) ^ {\prime \prime} = \left(\sum_ {k = 2} ^ {\infty} x ^ {k}\right) ^ {\prime \prime} = \left(\frac {x ^ {2}}{1 - x}\right) ^ {\prime \prime} = \left(\frac {x ^ {2} - 1 + 1}{1 - x}\right) ^ {\prime \prime} \\ &= \left(- x - 1 + \frac {1}{1 - x}\right) ^ {\prime \prime} = \left(\frac {1}{1 - x}\right) ^ {\prime \prime} = \frac {2}{(1 - x) ^ {3}}. \end{aligned}</equation>因此，<equation>E (Y) = \frac {1}{6 4} \sum_ {k = 2} ^ {\infty} k (k - 1) \left(\frac {7}{8}\right) ^ {k - 2} = \frac {1}{6 4} \times \frac {2}{\left(1 - \frac {7}{8}\right) ^ {3}} = 1 6.</equation>（法二）利用几何分布的性质.

设<equation>Y_{1}</equation>表示出现第1个大于3的观测值时所需的观测次数，<equation>Y_{2}</equation>表示出现第1个大于3的观测值之后到出现第2个大于3的观测值时所需的观测次数，则<equation>Y=Y_{1}+Y_{2}</equation>，且<equation>Y_{1},Y_{2}</equation>均服从参数为<equation>p=\frac{1}{8}</equation>的几何分布.于是<equation>E\left(Y_{1}\right)=E\left(Y_{2}\right)=\frac{1}{p}=8.</equation>因此，<equation>E (Y) = E \left(Y _ {1}\right) + E \left(Y _ {2}\right) = 1 6.</equation>

---

**2014年第22题 | 解答题 | 11分**


22. (本题满分11分)

设随机变量 X的概率分布为<equation>P\{X=1\}=P\{X=2\}=\frac{1}{2}.</equation>在给定 X=i 的条件下，随机变量 Y服从均匀分布<equation>U(0,i)(i=1,2).</equation>I. 求 Y的分布函数<equation>F_{Y}(y);</equation>II. 求 E(Y).

**答案:**(22) (I)<equation>F_{Y}(y)=\left\{ \begin{array}{ll} 0, & y<0, \\ \frac{3}{4} y, & 0\leqslant y<1, \\ \frac{1}{2}+\frac{1}{4} y, & 1\leqslant y<2, \\ 1, & y\geqslant 2; \end{array} \right.</equation><equation>\frac {3}{4}.</equation>

**解析:**解（I）由题设知，当<equation>X=1</equation>时，<equation>Y\sim U(0,1)</equation>；当<equation>X=2</equation>时，<equation>Y\sim U(0,2).</equation>于是，<equation>\begin{array}{l} F _ {Y} (y) = P \left\{Y \leqslant y \right\} = P \left\{Y \leqslant y, X = 1 \right\} + P \left\{Y \leqslant y, X = 2 \right\} \\ = P \left\{Y \leqslant y \mid X = 1 \right\} P \left\{X = 1 \right\} + P \left\{Y \leqslant y \mid X = 2 \right\} P \left\{X = 2 \right\}. \\ \end{array}</equation>当<equation>y < 0</equation>时，<equation>F_{Y}(y)=0\times \frac{1}{2}+0\times \frac{1}{2}=0.</equation>当<equation>0 \leqslant y < 1</equation>时，<equation>F_{Y}(y) = \left(\int_{0}^{y}1\mathrm{d}y\right)\cdot \frac{1}{2} + \left(\int_{0}^{y}\frac{1}{2}\mathrm{d}y\right)\cdot \frac{1}{2} = \frac{3}{4} y.</equation>当<equation>1\leqslant y < 2</equation>时，<equation>F_{Y}(y) = \left(\int_{0}^{1}1\mathrm{d}y\right)\cdot \frac{1}{2} + \left(\int_{0}^{y}\frac{1}{2}\mathrm{d}y\right)\cdot \frac{1}{2} = \frac{1}{2} + \frac{1}{4} y.</equation>当<equation>y\geqslant 2</equation>时，<equation>F_{Y}(y) = 1\times \frac{1}{2} +1\times \frac{1}{2} = 1.</equation>因此，<equation>Y</equation>的分布函数为<equation>F_{Y}(y) = \left\{ \begin{array}{ll}0, & y < 0,\\ \frac{3}{4} y, & 0 \leqslant y < 1,\\ \frac{1}{2} +\frac{1}{4} y, & 1 \leqslant y < 2,\\ 1, & y \geqslant 2. \end{array} \right.</equation>（Ⅱ）由第（I）问中<equation>Y</equation>的分布函数的表达式知，<equation>Y</equation>的概率密度函数为<equation>f _ {Y} (y) = F _ {Y} ^ {\prime} (y) = \left\{ \begin{array}{l l} \frac {3}{4}, & 0 \leqslant y < 1, \\ \frac {1}{4}, & 1 \leqslant y < 2, \\ 0, & \text {其 他}. \end{array} \right.</equation>因此，<equation>E (Y) = \int_ {- \infty} ^ {+ \infty} y f _ {Y} (y) \mathrm {d} y = \int_ {0} ^ {1} \frac {3}{4} y \mathrm {d} y + \int_ {1} ^ {2} \frac {1}{4} y \mathrm {d} y = \frac {3}{8} + \frac {3}{8} = \frac {3}{4}.</equation>

---

**2013年第14题 | 填空题 | 4分**

14. 设随机变量<equation>X</equation>服从标准正态分布<equation>N(0,1)</equation>, 则<equation>E(X \mathrm{e}^{2 X}) =</equation>___

**解析:**解 由题设知<equation>E \left(X \mathrm {e} ^ {2 X}\right) = \int_ {- \infty} ^ {+ \infty} x \mathrm {e} ^ {2 x} \cdot \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \mathrm {d} x = \frac {\mathrm {e} ^ {2}}{\sqrt {2 \pi}} \int_ {- \infty} ^ {+ \infty} x \mathrm {e} ^ {- \frac {(x - 2) ^ {2}}{2}} \mathrm {d} x.</equation>记<equation>E=\frac{\mathrm{e}^{2}}{\sqrt{2\pi}}\int_{-\infty}^{+\infty}x\mathrm{e}^{-\frac{(x-2)^{2}}{2}}\mathrm{d}x.</equation>下面我们用两种方法计算E.

（法一）积分<equation>\frac{1}{\sqrt{2\pi}}\int_{- \infty}^{+ \infty}x\mathrm{e}^{-\frac{(x-2)^{2}}{2}}\mathrm{d}x</equation>可看作服从正态分布N（2,1）的随机变量的数学期望，故<equation>\frac{1}{\sqrt{2\pi}}\int_{- \infty}^{+ \infty}x\mathrm{e}^{-\frac{(x-2)^{2}}{2}}\mathrm{d}x=2.</equation>因此，<equation>E=2\mathrm{e}^{2}.</equation>（法二）<equation>\begin{array}{l} E = \frac {\mathrm {e} ^ {2}}{\sqrt {2 \pi}} \int_ {- \infty} ^ {+ \infty} x \mathrm {e} ^ {- \frac {(x - 2) ^ {2}}{2}} \mathrm {d} x = \frac {\mathrm {e} ^ {2}}{\sqrt {2 \pi}} \left[ \int_ {- \infty} ^ {+ \infty} (x - 2) \mathrm {e} ^ {- \frac {(x - 2) ^ {2}}{2}} \mathrm {d} x + 2 \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- \frac {(x - 2) ^ {2}}{2}} \mathrm {d} x \right] \\ \underline {{= t = x - 2}} \mathrm {e} ^ {2} \left(\frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {+ \infty} t \mathrm {e} ^ {- \frac {t ^ {2}}{2}} \mathrm {d} t + \frac {2}{\sqrt {2 \pi}} \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- \frac {t ^ {2}}{2}} \mathrm {d} t\right). \\ \end{array}</equation>由标准正态分布的性质知<equation>\frac{1}{\sqrt{2\pi}}\int_{- \infty}^{+ \infty}\mathrm{e}^{-\frac{x^{2}}{2}}\mathrm{d}x=1, E(X)=\frac{1}{\sqrt{2\pi}}\int_{- \infty}^{+ \infty}x\mathrm{e}^{-\frac{x^{2}}{2}}\mathrm{d}x=0.</equation>代入上式可得<equation>E=\mathrm{e}^{2}(0+2)=2\mathrm{e}^{2}.</equation>综上所述，<equation>E\left(X\mathrm{e}^{2X}\right)=E=2\mathrm{e}^{2}.</equation>

---

**2012年第23题 | 解答题 | 11分**

23. (本题满分11分)

设随机变量 X与 Y相互独立，且都服从参数为1的指数分布. 记<equation>U=\max \{X,Y\}, V=\min \{X,Y\}</equation>I. 求 V的概率密度<equation>f_{V}(v)</equation>II. 求<equation>E(U+V).</equation>

**答案:**(23) （ I ）<equation>f_{V}(v)=\left\{\begin{array}{ll}2\mathrm{e}^{-2v},&v>0,\\ 0,&v\leqslant 0; \end{array}\right.</equation>（Ⅱ）2.

**解析:**解（I）由题设，随机变量 X, Y的概率密度均为<equation>f ( x )=\left\{\begin{array}{ll}\mathrm{e}^{-x},&x>0,\\ 0,&\text{其他}.\end{array} \right.</equation>于是 X, Y的分布函数均为<equation>F ( x )=\left\{\begin{array}{ll}1-\mathrm{e}^{-x},&x>0,\\ 0,&\text{其他},\end{array} \right.</equation>从而 V的分布函数为<equation>\begin{array}{l} F _ {V} (v) = P \{V \leqslant v \} = 1 - P \{V > v \} = 1 - P \{X > v, Y > v \} \\ = 1 - P \{X > v \} \cdot P \{Y > v \} \\ = 1 - \left[ 1 - F (v) \right] ^ {2} = \left\{ \begin{array}{l l} 1 - \mathrm {e} ^ {- 2 v}, & v > 0, \\ 0, & v \leqslant 0. \end{array} \right. \\ \end{array}</equation>因此，V的概率密度为<equation>f _ {V} (v) = F _ {V} ^ {\prime} (v) = \left\{ \begin{array}{l l} 2 \mathrm {e} ^ {- 2 v}, & v > 0, \\ 0, & v \leqslant 0. \end{array} \right.</equation>（Ⅱ）（法一）由于<equation>U + V = \max \{X, Y\} + \min \{X, Y\} = X + Y</equation>，故<equation>E (U + V) = E (X + Y) = E (X) + E (Y) = 2 E (X) = 2 \int_ {0} ^ {+ \infty} x \mathrm {e} ^ {- x} \mathrm {d} x = 2.</equation>（法二）U的分布函数为<equation>F _ {U} (u) = P \left\{U \leqslant u \right\} = P \left\{X \leqslant u, Y \leqslant u \right\} = P \left\{X \leqslant u \right\} \cdot P \left\{Y \leqslant u \right\} = \left[ F (u) \right] ^ {2}.</equation>于是，U的概率密度为<equation>f _ {U} (u) = F _ {U} ^ {\prime} (u) = 2 F (u) f (u) = \left\{ \begin{array}{l l} 2 \mathrm {e} ^ {- u} \left(1 - \mathrm {e} ^ {- u}\right), & u > 0, \\ 0, & u \leqslant 0. \end{array} \right.</equation>分别计算<equation>E ( u ) , E ( V )</equation><equation>E (U) = \int_ {- \infty} ^ {+ \infty} u f _ {U} (u) \mathrm {d} u = \int_ {0} ^ {+ \infty} 2 u \left(\mathrm {e} ^ {- u} - \mathrm {e} ^ {- 2 u}\right) \mathrm {d} u,</equation><equation>E (V) = \int_ {- \infty} ^ {+ \infty} v f _ {V} (v) \mathrm {d} v = \int_ {0} ^ {+ \infty} 2 v \mathrm {e} ^ {- 2 v} \mathrm {d} v.</equation>因此，<equation>E (U + V) = E (U) + E (V) = \int_ {0} ^ {+ \infty} 2 u \left(\mathrm {e} ^ {- u} - \mathrm {e} ^ {- 2 u}\right) \mathrm {d} u + \int_ {0} ^ {+ \infty} 2 v \mathrm {e} ^ {- 2 v} \mathrm {d} v = \int_ {0} ^ {+ \infty} 2 u \mathrm {e} ^ {- u} \mathrm {d} u = 2.</equation>

---

**2011年第4题 | 选择题 | 4分 | 答案: B**

4. 设<equation>I=\int_{0}^{\frac{\pi}{4}}\ln(\sin x)\mathrm{d}x, J=\int_{0}^{\frac{\pi}{4}}\ln(\cot x)\mathrm{d}x, K=\int_{0}^{\frac{\pi}{4}}\ln(\cos x)\mathrm{d}x</equation>，则 I, J, K的大小关系为（    )

A. I < J < K

B. I < K < J

C. J < I < K

D. K < J < I

答案: B

**解析:**解当 0 < x <<equation>\frac{\pi}{4}</equation>时，0 < sin x < cos x < 1 < cot x.又由于 f(u) = ln u在（0，+∞）上单调增加，故当 0 < x <<equation>\frac{\pi}{4}</equation>时，<equation>\ln(\sin x) < \ln(\cos x) < 0 < \ln(\cot x).</equation>因此，由定积分的保号性可知， I < K < J.应选B.

---

**2020年第23题 | 解答题 | 11分**


设某元件的使用寿命<equation>T</equation>的分布函数为<equation>F (t) = \left\{ \begin{array}{l l} 1 - \mathrm {e} ^ {- \left(\frac {t}{\theta}\right) ^ {m}}, & t \geqslant 0, \\ 0, & \text {其 他}, \end{array} \right.</equation>其中<equation>\theta, m</equation>为参数且均大于零.

I. 求概率<equation>P\{T > t\}</equation>与<equation>P\{T > s + t \mid T > s\}</equation>，其中<equation>s > 0, t > 0</equation>；

II. 任取 n个这种元件做寿命试验，测得它们的寿命分别为<equation>t_{1}, t_{2}, \dots , t_{n}</equation>，若 m已知，求<equation>\theta</equation>的最大似然估计值<equation>\hat{\theta}.</equation>

**答案:**（I）<equation>P \left\{ T > t \right\} = \mathrm{e}^{-\left(\frac{t}{\theta}\right)^{m}}, P \left\{ T > s + t \mid T > s \right\} = \mathrm{e}^{\frac{s^{m}-(s+t)^{m}}{\theta^{m}}};</equation>（Ⅱ）<equation>\theta</equation>的最大似然估计值为<equation>\hat{\theta}=\sqrt[m]{\frac{1}{n}\sum_{i=1}^{n}t_{i}^{m}}.</equation>

**解析:**（I）由分布函数的定义以及 s > 0，t > 0可得，<equation>P \left\{T > t \right\} = 1 - P \left\{T \leqslant t \right\} = 1 - F (t) = \mathrm {e} ^ {- \left(\frac {t}{\theta}\right) ^ {m}}.</equation><equation>P \left\{T > s + t \mid T > s \right\} = \frac {P \left\{T > s + t \right\}}{P \left\{T > s \right\}} = \frac {\mathrm {e} ^ {- \left(\frac {s + t}{\theta}\right) ^ {m}}}{\mathrm {e} ^ {- \left(\frac {s}{\theta}\right) ^ {m}}} = \mathrm {e} ^ {\frac {s ^ {m} - (s + t) ^ {m}}{\theta^ {m}}}.</equation>（Ⅱ）计算概率密度<equation>f(t; \theta).</equation><equation>f (t; \theta) = F ^ {\prime} (t; \theta) = \left\{ \begin{array}{l l} - \mathrm {e} ^ {- \left(\frac {t}{\theta}\right) ^ {m}} \cdot (- m) \cdot \left(\frac {t}{\theta}\right) ^ {m - 1} \cdot \frac {1}{\theta}, & t > 0, \\ 0, & \text {其 他} = \left\{ \begin{array}{l l} \frac {m t ^ {m - 1}}{\theta^ {m}} \mathrm {e} ^ {- \left(\frac {t}{\theta}\right) ^ {m}}, & t > 0, \\ 0, & \text {其 他}. \end{array} \right. \end{array} \right.</equation>似然函数<equation>L (\theta) = \prod_ {i = 1} ^ {n} f \left(t _ {i}; \theta\right) = \left\{ \begin{array}{l l} \left(t _ {1} t _ {2} \dots t _ {n}\right) ^ {m - 1} \cdot \left(\frac {m}{\theta^ {m}}\right) ^ {n} \cdot \mathrm {e} ^ {- \frac {1}{\theta^ {m}} \sum_ {i = 1} ^ {n} t _ {i} ^ {m}}, & t _ {i} > 0, i = 1, 2, \dots , n, \\ 0, & \text {其 他}. \end{array} \right.</equation>取对数得<equation>\ln L (\theta) = (m - 1) \ln \left(t _ {1} t _ {2} \dots t _ {n}\right) + n \left(\ln m - m \ln \theta\right) - \frac {1}{\theta^ {m}} \sum_ {i = 1} ^ {n} t _ {i} ^ {m}.</equation>令<equation>\frac{\mathrm{d}\left[\ln L(\theta)\right]}{\mathrm{d}\theta}=-\frac{mn}{\theta}+\frac{m}{\theta^{m+1}}\sum_{i=1}^{n}t_{i}^{m}=0</equation>，可得<equation>mn\theta^{m}=m\sum_{i=1}^{n}t_{i}^{m}</equation>. 从而<equation>\theta^{m}=\frac{1}{n}\sum_{i=1}^{n}t_{i}^{m},</equation><equation>\hat{\theta}=\sqrt[m]{\frac{1}{n}\sum_{i=1}^{n}t_{i}^{m}}.</equation>因此，<equation>\theta</equation>的最大似然估计值为<equation>\hat{\theta}=\sqrt[m]{\frac{1}{n}\sum_{i=1}^{n}t_{i}^{m}}.</equation>

---

**2019年第23题 | 解答题 | 11分**


设总体<equation>X</equation>的概率密度为<equation>f \left(x; \sigma^ {2}\right) = \left\{ \begin{array}{l l} \frac {A}{\sigma} \mathrm {e} ^ {- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}}, & x \geqslant \mu , \\ 0, & x < \mu . \end{array} \right.</equation>其中<equation>\mu</equation>是已知参数，<equation>\sigma >0</equation>是未知参数，A是常数.<equation>X_{1},X_{2},\cdots,X_{n}</equation>是来自总体 X的简单随机样本.

I. 求 A;

II. 求<equation>\sigma^{2}</equation>的最大似然估计量.

**答案:**( I )<equation>A=\sqrt{\frac{2}{\pi}};</equation>( II )<equation>\sigma^{2}</equation>的最大似然估计量为<equation>\widehat{\sigma^{2}}=\frac{\sum_{i=1}^{n}\left(X_{i}-\mu\right)^{2}}{n}.</equation>

**解析:**解（ I ）利用<equation>\int_{- \infty}^{+ \infty} f ( x ; \sigma^{2} ) \mathrm{d} x=1</equation>来计算 A.<equation>\begin{aligned} \int_ {- \infty} ^ {+ \infty} f (x; \sigma^ {2}) \mathrm {d} x &= \int_ {\mu} ^ {+ \infty} \frac {A}{\sigma} \mathrm {e} ^ {- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}} \mathrm {d} x \underline {{= t = x - \mu}} A \int_ {0} ^ {+ \infty} \frac {1}{\sigma} \mathrm {e} ^ {- \frac {t ^ {2}}{2 \sigma^ {2}}} \mathrm {d} t = A \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {1}{2} \cdot \left(\frac {t}{\sigma}\right) ^ {2}} \mathrm {d} \left(\frac {t}{\sigma}\right) \\ \frac {\frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \mathrm {d} x = 1}{\underline {{}}} A \cdot \frac {\sqrt {2 \pi}}{2} &= 1. \end{aligned}</equation>因此，<equation>A=\frac{2}{\sqrt{2\pi}}=\sqrt{\frac{2}{\pi}}.</equation>（Ⅱ）设<equation>x_{1}, x_{2}, \dots, x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots, X_{n}</equation>的一组样本值，则关于<equation>\sigma^2</equation>的似然函数为<equation>\begin{array}{l} L \left(\sigma^ {2}\right) = \prod_ {i = 1} ^ {n} f \left(x _ {i}; \sigma^ {2}\right) = \left\{ \begin{array}{l l} \prod_ {i = 1} ^ {n} \sqrt {\frac {2}{\pi}} \cdot \frac {1}{\sigma} \cdot \mathrm {e} ^ {- \frac {\left(x _ {i} - \mu\right) ^ {2}}{2 \sigma^ {2}}}, & x _ {1} \geqslant \mu , x _ {2} \geqslant \mu , \dots , x _ {n} \geqslant \mu , \\ 0, & \text {其 他} \end{array} \right. \\ = \left\{ \begin{array}{l l} \left(\frac {2}{\pi}\right) ^ {\frac {n}{2}} \cdot \left(\frac {1}{\sigma^ {2}}\right) ^ {\frac {n}{2}} \cdot \mathrm {e} ^ {- \frac {\sum_ {i = 1} ^ {n} \left(x _ {i} - \mu\right) ^ {2}}{2 \sigma^ {2}}}, & x _ {1} \geqslant \mu , x _ {2} \geqslant \mu , \dots , x _ {n} \geqslant \mu , \\ 0, & \text {其 他}. \end{array} \right. \\ \end{array}</equation>当<equation>x_{1}\geqslant \mu ,x_{2}\geqslant \mu ,\dots ,x_{n}\geqslant \mu</equation>时，<equation>\ln L \left(\sigma^ {2}\right) = \frac {n}{2} \ln \frac {2}{\pi} - \frac {n}{2} \ln \sigma^ {2} - \frac {\sum_ {i = 1} ^ {n} \left(x _ {i} - \mu\right) ^ {2}}{2 \sigma^ {2}}.</equation>令<equation>\frac{\mathrm{d}\left[\ln L(\sigma^{2})\right]}{\mathrm{d}(\sigma^{2})}=0</equation>即<equation>-\frac{n}{2}\cdot \frac{1}{\sigma^{2}}+\frac{\sum_{i=1}^{n}\left(x_{i}-\mu\right)^{2}}{2}\cdot \frac{1}{\sigma^{4}}=0</equation>，解得<equation>\sigma^{2}=\frac{\sum_{i=1}^{n}\left(x_{i}-\mu\right)^{2}}{n}.</equation>因此，<equation>\sigma^{2}</equation>的最大似然估计量为<equation>\hat {\sigma^ {2}} = \frac {\sum_ {i = 1} ^ {n} \left(X _ {i} - \mu\right) ^ {2}}{n}.</equation>

---

**2018年第23题 | 解答题 | 11分**


设总体<equation>X</equation>的概率密度为<equation>f (x; \sigma) = \frac {1}{2 \sigma} \mathrm {e} ^ {- \frac {| x |}{\sigma}}, (- \infty < x < + \infty).</equation>其中<equation>\sigma \in(0,+\infty)</equation>为未知参数，<equation>X_{1},X_{2},\cdots,X_{n}</equation>为来自总体 X的简单随机样本.记<equation>\sigma</equation>的最大似然估计量为<equation>\hat{\sigma}.</equation>I. 求<equation>\hat{\sigma}</equation>;

II. 求<equation>E(\hat{\sigma}),D(\hat{\sigma}).</equation>

**答案:**（I）<equation>\sigma</equation>的最大似然估计量为<equation>\hat{\sigma}=\frac{\sum_{i=1}^{n} \mid X_{i}\mid}{n}；</equation>（Ⅱ）<equation>E(\hat{\sigma})=\sigma</equation>，<equation>D(\hat{\sigma})=\frac{\sigma^{2}}{n}.</equation>

**解析:**解（ I ）设<equation>x_{1}, x_{2}, \dots , x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots , X_{n}</equation>的一组样本值.似然函数为<equation>L (\sigma) = \prod_ {i = 1} ^ {n} f \left(x _ {i}; \sigma\right) = \frac {1}{2 ^ {n} \sigma^ {n}} \mathrm {e} ^ {- \frac {\left| x _ {1} \right| + \left| x _ {2} \right| + \cdots + \left| x _ {n} \right|}{\sigma}}, - \infty < x _ {i} < + \infty , i = 1, 2, \dots , n.</equation>对 L（<equation>\sigma</equation>）取对数，得<equation>\ln L (\sigma) = - \frac {\sum_ {i = 1} ^ {n} \left| x _ {i} \right|}{\sigma} - n \ln (2 \sigma).</equation>令<equation>\frac{\mathrm{d}[\ln L(\sigma)]}{\mathrm{d}\sigma}=\frac{\sum_{i=1}^{n} \mid x_{i}\mid}{\sigma^{2}}-\frac{n}{\sigma}=0</equation>即<equation>\sum_{i=1}^{n} \mid x_{i}\mid-n\sigma=0</equation>解得<equation>\sigma=\frac{\sum_{i=1}^{n} \mid x_{i}\mid}{n}.</equation>因此，<equation>\sigma</equation>的最大似然估计量为<equation>\hat {\sigma} = \frac {\sum_ {i = 1} ^ {n} \left| X _ {i} \right|}{n}.</equation>（Ⅱ）由于<equation>X_{1}, X_{2}, \dots , X_{n}</equation>为来自总体X的简单随机样本，故它们相互独立，且与总体X同分布<equation>E(X_{i})=E(X), E(|X_{i}|)=E(|X|), i=1,2,\dots ,n.</equation>根据期望的线性性质，<equation>E (\hat {\sigma}) = E \left(\frac {\sum_ {i = 1} ^ {n} \left| X _ {i} \right|}{n}\right) = \frac {\sum_ {i = 1} ^ {n} E \left(\left| X _ {i} \right|\right)}{n} = \frac {n E \left(\left| X \right|\right)}{n} = E (\left| X \right|).</equation>根据期望的定义，<equation>\begin{aligned} E (\mid X \mid) &= \int_ {- \infty} ^ {+ \infty} | x | \cdot f (x; \sigma) \mathrm {d} x = \int_ {- \infty} ^ {+ \infty} | x | \cdot \frac {1}{2 \sigma} \mathrm {e} ^ {- \frac {| x |}{\sigma}} \mathrm {d} x = 2 \int_ {0} ^ {+ \infty} \frac {x}{2 \sigma} \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x \\ &= \frac {1}{\sigma} \int_ {0} ^ {+ \infty} x \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x = - \int_ {0} ^ {+ \infty} x \mathrm {d} \left(\mathrm {e} ^ {- \frac {x}{\sigma}}\right) = - \left(x \mathrm {e} ^ {- \frac {x}{\sigma}} \Big | _ {0} ^ {+ \infty} - \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x\right) \\ &= \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x = - \sigma \mathrm {e} ^ {- \frac {x}{\sigma}} \Big | _ {0} ^ {+ \infty} = \sigma . \end{aligned}</equation>因此，<equation>E(\hat{\sigma}) = \sigma .</equation>下面计算<equation>D(\hat{\sigma})。</equation>由于<equation>X_{1}, X_{2}, \dots, X_{n}</equation>相互独立，且与总体<equation>X</equation>同分布，故<equation>D(\mid X_{i}\mid) = D(\mid X\mid)</equation>，<equation>i = 1, 2, \dots, n.</equation><equation>D (\hat {\sigma}) = D \left(\frac {\sum_ {i = 1} ^ {n} \left| X _ {i} \right|}{n}\right) = \frac {1}{n ^ {2}} D \left(\sum_ {i = 1} ^ {n} \left| X _ {i} \right|\right) = \frac {1}{n ^ {2}} \cdot n D (\mid X \mid) = \frac {D (\mid X \mid)}{n}.</equation>根据方差的计算公式，<equation>D (\mid X \mid) = E \left(\mid X \mid^ {2}\right) - \left[ E (\mid X \mid) \right] ^ {2} = E \left(X ^ {2}\right) - \left[ E (\mid X \mid) \right] ^ {2}.</equation><equation>\begin{aligned} E \left(X ^ {2}\right) &= \int_ {- \infty} ^ {+ \infty} x ^ {2} \cdot f (x; \sigma) \mathrm {d} x = \int_ {- \infty} ^ {+ \infty} x ^ {2} \cdot \frac {1}{2 \sigma} \mathrm {e} ^ {- \frac {| x |}{\sigma}} \mathrm {d} x = \frac {1}{\sigma} \int_ {0} ^ {+ \infty} x ^ {2} \cdot \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x \\ &= - \int_ {0} ^ {+ \infty} x ^ {2} \mathrm {d} \left(\mathrm {e} ^ {- \frac {x}{\sigma}}\right) = - \left(x ^ {2} \mathrm {e} ^ {- \frac {x}{\sigma}} \Big | _ {0} ^ {+ \infty} - 2 \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {x}{\sigma}} \cdot x \mathrm {d} x\right) \\ &= 2 \int_ {0} ^ {+ \infty} x \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x \stackrel {*} {=} 2 \sigma^ {2}. \end{aligned}</equation>于是，<equation>D ( \mid X \mid ) = 2 \sigma^{2} - \sigma^{2} = \sigma^{2}.</equation>因此，<equation>D(\hat{\sigma}) = \frac{D(|X|)}{n} = \frac{\sigma^{2}}{n}.</equation>

---

**2017年第23题 | 解答题 | 11分**


某工程师为了解一台天平的精度，用该天平对一物体的质量做 n次测量，该物体的质量<equation>\mu</equation>是已知的，设 n次测量结果<equation>X_{1},X_{2},\cdots ,X_{n}</equation>相互独立且均服从正态分布<equation>N\left(\mu ,\sigma^{2}\right).</equation>该工程师记录的是 n次测量的绝对误差<equation>Z_{i}=\left|X_{i}-\mu\right|(i=1,2,\cdots,n),</equation>利用<equation>Z_{1},Z_{2},\cdots,Z_{n}</equation>估计<equation>\sigma.</equation>I. 求<equation>Z_{1}</equation>的概率密度；

II. 利用一阶矩求<equation>\sigma</equation>的矩估计量；

III. 求<equation>\sigma</equation>的最大似然估计量.

**答案:**( I )<equation>f_{Z_{1}}(z) = \left\{ \begin{array}{ll} \sqrt{\frac{2}{\pi}} \frac{1}{\sigma} \mathrm{e}^{-\frac{z^{2}}{2\sigma^{2}}}, & z \geqslant 0, \\ 0, & z < 0; \end{array} \right.</equation>( II )<equation>\hat{\sigma} = \sqrt{\frac{\pi}{2}} \bar{Z}</equation>;

( III )<equation>\hat{\sigma} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} Z_{i}^{2}}</equation>.

**解析:**解（I）由题设知，<equation>X_{1}\sim N(\mu ,\sigma^{2})</equation>，从而<equation>\frac{X_{1}-\mu}{\sigma}\sim N(0,1).</equation>当 z < 0时，<equation>F_{Z_{1}}(z)=0.</equation>当<equation>z\geqslant0</equation>时，<equation>\begin{array}{l} F _ {Z _ {1}} (z) = P \left\{Z _ {1} \leqslant z \right\} = P \left\{\mid X _ {1} - \mu \mid \leqslant z \right\} \\ = P \left\{\left| \frac {X _ {1} - \mu}{\sigma} \right| \leqslant \frac {z}{\sigma} \right\} = P \left\{- \frac {z}{\sigma} \leqslant \frac {X _ {1} - \mu}{\sigma} \leqslant \frac {z}{\sigma} \right\} \\ = 2 \Phi \left(\frac {z}{\sigma}\right) - 1, \\ \end{array}</equation>其中<equation>\varPhi(x)</equation>为标准正态分布函数.

于是，<equation>Z_{1}</equation>的分布函数为<equation>F_{Z_{1}}(z)=\left\{ \begin{array}{ll} 2\Phi \left(\frac{z}{\sigma}\right)-1, & z\geqslant 0, \\ 0, & z<0. \end{array} \right.</equation>因此，<equation>Z_{1}</equation>的概率密度为<equation>f _ {Z _ {1}} (z) = F _ {Z _ {1}} ^ {\prime} (z) = \left\{ \begin{array}{l l} \frac {2}{\sigma} \varphi \left(\frac {z}{\sigma}\right), & z \geqslant 0, \\ 0, & z < 0 \end{array} = \left\{ \begin{array}{l l} \sqrt {\frac {2}{\pi}} \frac {1}{\sigma} \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}}, & z \geqslant 0, \\ 0, & z < 0, \end{array} \right. \right.</equation>其中<equation>\varphi(x)</equation>为标准正态分布的概率密度.

（Ⅱ）由于<equation>\begin{array}{l} E \left(Z _ {1}\right) = \int_ {- \infty} ^ {+ \infty} z f _ {Z _ {1}} (z) \mathrm {d} z = \int_ {0} ^ {+ \infty} z \cdot \sqrt {\frac {2}{\pi}} \frac {1}{\sigma} \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}} \mathrm {d} z = \sqrt {\frac {2}{\pi}} \sigma \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}} \mathrm {d} \left(\frac {z ^ {2}}{2 \sigma^ {2}}\right) \\ = - \sqrt {\frac {2}{\pi}} \sigma \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}} \Big | _ {0} ^ {+ \infty} = \sqrt {\frac {2}{\pi}} \sigma , \\ \end{array}</equation>故<equation>\sigma=\sqrt{\frac{\pi}{2}} E(Z_{1})</equation>用<equation>\overline{Z}=\frac{1}{n}\sum_{i=1}^{n} Z_{i}</equation>代替<equation>E(Z_{1})</equation>，得到<equation>\sigma</equation>的矩估计量<equation>\hat {\sigma} = \sqrt {\frac {\pi}{2}} \bar {Z}.</equation>（Ⅲ）设<equation>z_{1}, z_{2}, \dots , z_{n}</equation>是相应于<equation>Z_{1}, Z_{2}, \dots , Z_{n}</equation>的一组样本值，则似然函数为<equation>L (\sigma) = L \left(z _ {1}, z _ {2}, \dots , z _ {n}; \sigma\right) = \prod_ {i = 1} ^ {n} f _ {Z _ {i}} \left(z _ {i}\right) = \left\{ \begin{array}{l l} \left(\frac {2}{\pi}\right) ^ {\frac {n}{2}} \frac {1}{\sigma^ {n}} \mathrm {e} ^ {- \frac {1}{2 \sigma^ {2}} \left(z _ {1} ^ {2} + z _ {2} ^ {2} + \dots + z _ {n} ^ {2}\right)}, & z _ {1} > 0, z _ {2} > 0, \dots , z _ {n} > 0, \\ 0, & \text {其 他}. \end{array} \right.</equation>当<equation>z_{1} > 0, z_{2} > 0, \dots, z_{n} > 0</equation>时，<equation>\ln L (\sigma) = \frac {n}{2} \ln \frac {2}{\pi} - n \ln \sigma - \frac {1}{2 \sigma^ {2}} \left(z _ {1} ^ {2} + z _ {2} ^ {2} + \dots + z _ {n} ^ {2}\right).</equation>令<equation>\frac{\mathrm{d}[\ln L(\sigma)]}{\mathrm{d}\sigma} = 0</equation>，即<equation>-\frac{n}{\sigma} +\frac{1}{\sigma^3}\left(z_1^2 +z_2^2 +\dots +z_n^2\right) = 0</equation>，解得<equation>\sigma = \sqrt{\frac{1}{n}\sum_{i=1}^{n}z_i^2}</equation><equation>\sigma</equation><equation>\hat {\sigma} = \sqrt {\frac {1}{n} \sum_ {i = 1} ^ {n} Z _ {i} ^ {2}}.</equation>

---

**2015年第23题 | 解答题 | 11分**


设总体<equation>X</equation>的概率密度为<equation>f (x; \theta) = \left\{ \begin{array}{l l} \frac {1}{1 - \theta}, & \theta \leqslant x \leqslant 1, \\ 0, & \text {其 他}, \end{array} \right.</equation>其中<equation>\theta</equation>为未知参数.<equation>X_{1},X_{2},\cdots ,X_{n}</equation>为来自该总体的简单随机样本.

I. 求<equation>\theta</equation>的矩估计量;

II. 求<equation>\theta</equation>的最大似然估计量.

**答案:**<equation>\begin{array}{l} (2 3) (\mathrm {I}) \hat {\theta} = 2 \bar {X} - 1; \\ (\mathrm {I I}) \hat {\theta} = \min _ {1 \leqslant i \leqslant n} X _ {i}. \\ \end{array}</equation>

**解析:**（ I ）由于<equation>E (X) = \int_ {- \infty} ^ {+ \infty} x f (x; \theta) \mathrm {d} x = \int_ {\theta} ^ {1} \frac {x}{1 - \theta} \mathrm {d} x = \frac {1 + \theta}{2},</equation>故<equation>\theta = 2 E ( X ) - 1.</equation>用样本均值<equation>\overline{X}=\frac{1}{n}\sum_{i=1}^{n}X_{i}</equation>代替<equation>E ( X )</equation>，可得<equation>\theta</equation>的矩估计量<equation>\hat {\theta} = 2 \bar {X} - 1.</equation>（Ⅱ）设<equation>x_{1}, x_{2}, \dots, x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots, X_{n}</equation>的一组样本值，则似然函数为<equation>L (\theta) = \prod_ {i = 1} ^ {n} f \left(x _ {i}; \theta\right) = \left\{ \begin{array}{l l} \frac {1}{(1 - \theta) ^ {n}}, & \theta \leqslant x _ {1}, x _ {2}, \dots , x _ {n} \leqslant 1, \\ 0, & \text {其 他} \end{array} = \left\{ \begin{array}{l l} \frac {1}{(1 - \theta) ^ {n}}, & \theta \leqslant \min _ {1 \leqslant i \leqslant n} x _ {i}, \\ 0, & \text {其 他}. \end{array} \right. \right.</equation>又由于<equation>\frac{1}{(1-\theta)^{n}}</equation>是关于<equation>\theta</equation>的单调增加函数，故当<equation>\theta=\min_{1\leqslant i\leqslant n}x_{i}</equation>时，<equation>L(\theta)</equation>取值最大因此，<equation>\theta</equation>的最大似然估计量为<equation>\hat {\theta} = \min _ {1 \leqslant i \leqslant n} X _ {i}.</equation>

---


**2024年第22题 | 解答题 | 12分**


设总体 X服从<equation>[0,\theta]</equation>上的均匀分布，<equation>\theta\in(0,+\infty)</equation>为未知参数，<equation>X_{1},X_{2},\cdots,X_{n}</equation>为来自总体 X的简单随机样本，记为<equation>X_{(n)}=\max\{X_{1},X_{2},\cdots,X_{n}\}, T_{c}=cX_{(n)}.</equation>I. 求 c，使得<equation>E\left(T_{c}\right)=\theta;</equation>II. 记 h(c)=E<equation>[\left(T_{c}-\theta\right)^{2}]</equation>，求 c使得 h(c)最小.

**答案:**(1)<equation>c=\frac{n+1}{n}.</equation>(2)<equation>c=\frac{n+2}{n+1}</equation>时，<equation>h(c)</equation>取最小值.

**解析:**（I）由于 X服从<equation>[0,\theta]</equation>上的均匀分布，故 X的分布函数为<equation>F _ {X} (x) = \left\{ \begin{array}{l l} 0, & x < 0, \\ \frac {x}{\theta}, & 0 \leqslant x < \theta , \\ 1, & x \geqslant \theta . \end{array} \right.</equation>记随机变量<equation>Y = X_{(n)} = \max \left|X_{1},X_{2},\dots ,X_{n}\right|</equation>. 计算<equation>Y</equation>的分布函数<equation>F_{Y}(y)</equation>当<equation>y < 0</equation>时，<equation>F_{Y}(y) = 0.</equation>当<equation>0\leqslant y < \theta</equation>时，<equation>\begin{array}{l} F _ {Y} (y) = P \left\{Y \leqslant y \right\} = P \left\{\max _ {1 \leqslant i \leqslant n} X _ {i} \leqslant y \right\} = P \left\{X _ {1} \leqslant y, X _ {2} \leqslant y, \dots , X _ {n} \leqslant y \right\} \\ \underline {{\text {独立 性}}} P \left\{X _ {1} \leqslant y \right\} P \left\{X _ {2} \leqslant y \right\} \dots P \left\{X _ {n} \leqslant y \right\} = F _ {X} ^ {n} (y) = \left(\frac {y}{\theta}\right) ^ {n}. \\ \end{array}</equation>当<equation>y\geqslant \theta</equation>时，<equation>F_{Y}(y) = 1.</equation>于是，<equation>F_{Y}(y) = \left\{ \begin{array}{ll} 0, & y < 0, \\ \left(\frac{y}{\theta}\right)^{n}, & 0 \leqslant y < \theta , \\ 1, & y \geqslant \theta . \end{array} \right.</equation>对<equation>F_{\gamma}(y)</equation>求导，可得<equation>f _ {Y} (y) = F _ {Y} ^ {\prime} (y) = \left\{ \begin{array}{l l} \frac {n y ^ {n - 1}}{\theta^ {n}}, & 0 < y < \theta , \\ 0, & \text {其 他}. \end{array} \right.</equation>因此，<equation>\begin{aligned} E \left(T _ {c}\right) &= E (c Y) = c \int_ {- \infty} ^ {+ \infty} y \cdot f _ {Y} (y) \mathrm {d} y = c \int_ {0} ^ {\theta} y \cdot \frac {n y ^ {n - 1}}{\theta^ {n}} \mathrm {d} y = c \cdot \frac {n}{\theta^ {n}} \cdot \frac {y ^ {n + 1}}{n + 1} \Bigg | _ {0} ^ {\theta} \\ &= \frac {c n}{n + 1} \theta . \end{aligned}</equation>若<equation>E\left(T_{c}\right) = \theta</equation>，则<equation>\frac{cn}{n + 1}\theta = \theta</equation>，解得<equation>c = \frac{n + 1}{n}</equation>.

（Ⅱ）展开 h（c）可得<equation>h (c) = E \left[ \left(T _ {c} - \theta\right) ^ {2} \right] = E \left[ \left(c Y - \theta\right) ^ {2} \right] = c ^ {2} E \left(Y ^ {2}\right) - 2 c \theta E (Y) + \theta^ {2}.</equation>计算<equation>E ( Y^{2})</equation><equation>E \left(Y ^ {2}\right) = \int_ {- \infty} ^ {+ \infty} y ^ {2} \cdot f _ {Y} (y) \mathrm {d} y = \int_ {0} ^ {\theta} y ^ {2} \cdot \frac {n y ^ {n - 1}}{\theta^ {n}} \mathrm {d} y = \frac {n}{\theta^ {n}} \cdot \frac {y ^ {n + 2}}{n + 2} \Bigg | _ {0} ^ {\theta} = \frac {n}{n + 2} \theta^ {2}.</equation>于是，<equation>h (c) = c ^ {2} \cdot \frac {n}{n + 2} \theta^ {2} - 2 c \cdot \frac {n}{n + 1} \theta^ {2} + \theta^ {2} = \left(\frac {n}{n + 2} c ^ {2} - \frac {2 n}{n + 1} c + 1\right) \theta^ {2}.</equation>令<equation>\frac{\mathrm{d}[h(c)]}{\mathrm{d}c}=\left(\frac{2 n}{n+2} c-\frac{2 n}{n+1}\right)\theta^{2}=0</equation>，解得 c =<equation>\frac{n+2}{n+1}.</equation>该点是 h(c）的唯一驻点. 又因为<equation>h^{\prime \prime}(c)=\frac{2 n}{n+2}\theta^{2}>0</equation>，所以该唯一驻点是 h(c）的极小值点，也是最小值点.

因此，当<equation>c=\frac{n+2}{n+1}</equation>时，<equation>h(c)</equation>最小.

---

**2023年第8题 | 选择题 | 5分 | 答案: C**

8. 设随机变量<equation>X</equation>服从参数为1的泊松分布，则<equation>E[|X - E(X)|] = (\quad)</equation>A.<equation>\frac{1} {\mathrm{e}}</equation>B.<equation>\frac{1}{2}</equation>C.<equation>\frac{2} {\mathrm{e}}</equation>D. 1

答案: C

**解析:**由于 X服从参数为1的泊松分布，故<equation>E ( X )=1.</equation>从而<equation>| X - E (X) | = | X - 1 | = \left\{ \begin{array}{l l} 1, & X = 0, \\ X - 1, & X = 1, 2, \dots . \end{array} \right.</equation>由参数为1的泊松分布的分布律可知，<equation>P\{X = 0\} = \frac{1^{0}\cdot\mathrm{e}^{-1}}{0!} = \frac{1}{\mathrm{e}}.</equation>根据数学期望的定义，<equation>\begin{aligned} E [ \mid X - E (X) \mid ] &= 1 \cdot P \{X = 0 \} + \sum_ {k = 1} ^ {\infty} (k - 1) P \{X = k \} \\ &= \frac {1}{\mathrm {e}} + \sum_ {k = 0} ^ {\infty} (k - 1) P \{X = k \} - (0 - 1) P \{X = 0 \} \\ &= \frac {1}{\mathrm {e}} + E (X - 1) + \frac {1}{\mathrm {e}} = \frac {1}{\mathrm {e}} + E (X) - 1 + \frac {1}{\mathrm {e}} \\ \underline {{\underline {{E (X) = 1}}}} \frac {2}{\mathrm {e}}. \end{aligned}</equation>因此，应选C.

---

**2023年第22题 | 解答题 | 12分**

22. (本题满分12分)

设随机变量 X的概率密度为<equation>f ( x )=\frac{\mathrm{e}^{x}}{\left( 1+\mathrm{e}^{x}\right)^{2}},-\infty<x<+\infty</equation>，令<equation>Y=\mathrm{e}^{X}.</equation>I. 求 X的分布函数;

II. 求 Y的概率密度;

III. Y的数学期望是否存在?

**答案:**（I）<equation>X</equation>的分布函数<equation>F_{X}(x)=\frac{\mathrm{e}^{x}}{1+\mathrm{e}^{x}};</equation>（Ⅱ）<equation>Y</equation>的概率密度为<equation>f_{Y}(y)=\left\{\begin{array}{ll}\frac{1}{(1+y)^{2}},&y>0,\\ 0,&y\leqslant 0.\end{array}\right.</equation>（Ⅲ）Y的数学期望不存在.

**解析:**解（ I ）记 X的分布函数为<equation>F_{X}(x).</equation>由概率密度的定义可知，<equation>F _ {X} (x) = \int_ {- \infty} ^ {x} f (t) \mathrm {d} t = \int_ {- \infty} ^ {x} \frac {\mathrm {e} ^ {t}}{\left(1 + \mathrm {e} ^ {t}\right) ^ {2}} \mathrm {d} t \xlongequal {=} \int_ {0} ^ {\mathrm {e} ^ {x}} \frac {\mathrm {d} u}{\left(1 + u\right) ^ {2}} = \frac {- 1}{1 + u} \Big | _ {0} ^ {\mathrm {e} ^ {x}} = \frac {\mathrm {e} ^ {x}}{1 + \mathrm {e} ^ {x}}.</equation>（Ⅱ）（法一）定义法.

计算<equation>Y</equation>的分布函数<equation>F_{Y}(y)</equation>由于<equation>Y=\mathrm{e}^{X}>0</equation>，故当<equation>y\leqslant0</equation>时，<equation>F_{Y}(y)=P\{Y\leqslant y\}=0.</equation>当 y > 0时，<equation>F _ {Y} (y) = P \left\{Y \leqslant y \right\} = P \left\{\mathrm {e} ^ {X} \leqslant y \right\} = P \left\{X \leqslant \ln y \right\} = F _ {X} (\ln y) = \frac {y}{1 + y}.</equation>因此，<equation>F_{Y}(y)=\left\{ \begin{array}{ll}\frac{y}{1+y},&y>0,\\ 0,&y\leqslant 0. \end{array} \right.</equation>当 y > 0时，<equation>f_{Y}(y)=F_{Y}^{\prime}(y)=\frac{1}{(1+y)^{2}}.</equation>当 y≤0时，<equation>f_{Y}(y)</equation><equation>= F_{Y}^{\prime}(y)=0.</equation>综上所述，Y的概率密度为<equation>f _ {Y} (y) = \left\{ \begin{array}{l l} \frac {1}{(1 + y) ^ {2}}, & y > 0, \\ 0, & y \leqslant 0. \end{array} \right.</equation>（法二）公式法.

函数<equation>g ( x )=\mathrm{e}^{x}</equation>在<equation>(-\infty, +\infty)</equation>上处处可导且<equation>g^{\prime}(x)=\mathrm{e}^{x}>0.</equation><equation>\alpha = \min \left\{g (- \infty), g (+ \infty) \right\} = 0, \beta = \max \left\{g (- \infty), g (+ \infty) \right\} = + \infty .</equation><equation>g(x)</equation>的反函数为<equation>x = \ln y, (\ln y)^{\prime} = \frac{1}{y}</equation>.

由公式法可得，当 y > 0时，<equation>f _ {Y} (y) = f _ {X} (\ln y) \left| \frac {1}{y} \right| = \frac {1}{y} \cdot \frac {\mathrm {e} ^ {\ln y}}{\left(1 + \mathrm {e} ^ {\ln y}\right) ^ {2}} = \frac {1}{y} \cdot \frac {y}{(1 + y) ^ {2}} = \frac {1}{(1 + y) ^ {2}}.</equation>当<equation>y\leqslant0</equation>时，<equation>f_{Y}(y)=0.</equation>因此，Y的概率密度为<equation>f_{Y}(y)=\left\{ \begin{array}{ll}\frac{1}{(1+y)^{2}},&y>0,\\ 0,&y\leqslant 0. \end{array} \right.</equation>（Ⅲ）若 Y的数学期望存在，则由数学期望的定义可知<equation>\begin{array}{l} E (Y) = \int_ {- \infty} ^ {+ \infty} y f _ {Y} (y) \mathrm {d} y = \int_ {0} ^ {+ \infty} \frac {y \mathrm {d} y}{(1 + y) ^ {2}} = \int_ {0} ^ {+ \infty} \frac {1 + y - 1}{(1 + y) ^ {2}} \mathrm {d} y \\ = \int_ {0} ^ {+ \infty} \left[ \frac {1}{1 + y} - \frac {1}{(1 + y) ^ {2}} \right] \mathrm {d} y = \left[ \ln (1 + y) + \frac {1}{1 + y} \right] \Bigg | _ {0} ^ {+ \infty} = + \infty . \\ \end{array}</equation>因此，E（Y）不存在.

---

**2020年第14题 | 填空题 | 4分**

14. 设随机变量<equation>X</equation>的概率分布为<equation>P\{X=k\}=\frac{1}{2^{k}}(k=1,2,3,\cdots),Y</equation>表示<equation>X</equation>被3除的余数，则<equation>E(Y)=</equation>___.

**答案:**# 8 7

**解析:**解 X的取值为全体正整数，而 Y表示 X被3除的余数，故 Y的可能取值为0，1，2，分别对应 X = 3i+3, X=3i+1, X=3i+2（i=0，1，2，…）的情况.

下面计算 Y的分布律.<equation>P \{Y = 0 \} = \sum_ {i = 0} ^ {\infty} P \{X = 3 i + 3 \} = \sum_ {i = 0} ^ {\infty} \frac {1}{2 ^ {3 i + 3}} = \frac {1}{8} \sum_ {i = 0} ^ {\infty} \frac {1}{8 ^ {i}},</equation><equation>P \{Y = 1 \} = \sum_ {i = 0} ^ {\infty} P \{X = 3 i + 1 \} = \sum_ {i = 0} ^ {\infty} \frac {1}{2 ^ {3 i + 1}} = \frac {1}{2} \sum_ {i = 0} ^ {\infty} \frac {1}{8 ^ {i}},</equation><equation>P \{Y = 2 \} = \sum_ {i = 0} ^ {\infty} P \{X = 3 i + 2 \} = \sum_ {i = 0} ^ {\infty} \frac {1}{2 ^ {3 i + 2}} = \frac {1}{4} \sum_ {i = 0} ^ {\infty} \frac {1}{8 ^ {i}}.</equation>根据期望的定义，<equation>\begin{array}{l} E (Y) = 0 \times P \{Y = 0 \} + 1 \times P \{Y = 1 \} + 2 \times P \{Y = 2 \} \\ = 1 \times \frac {1}{2} \sum_ {i = 0} ^ {\infty} \frac {1}{8 ^ {i}} + 2 \times \frac {1}{4} \sum_ {i = 0} ^ {\infty} \frac {1}{8 ^ {i}} = \sum_ {i = 0} ^ {\infty} \frac {1}{8 ^ {i}} \\ = \frac {1}{1 - \frac {1}{8}} = \frac {8}{7}. \\ \end{array}</equation>

---

**2019年第14题 | 填空题 | 4分**

14. 设随机变量 X的概率密度为 f(x)<equation>\left\{\begin{array}{l l} {\frac{x}{2},}&{0<x<2,}\\ {0,}&{\mathrm {其 他},}\end{array}\right.</equation>F(x)为 X的分布函数，E(X)为 X的数学期望，则<equation>P\{F(X)>E(X)-1\}=</equation>___

**答案:**# 2 3.

**解析:**（法一）分别计算<equation>E ( X )</equation>，<equation>F ( x )</equation><equation>E (X) = \int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \int_ {0} ^ {2} \frac {x ^ {2}}{2} \mathrm {d} x = \frac {x ^ {3}}{6} \Big | _ {0} ^ {2} = \frac {4}{3}.</equation>当<equation>x < 0</equation>时，<equation>F ( x )=0.</equation>当<equation>0 \leqslant x < 2</equation>时，<equation>F(x) = \int_{-\infty}^{x} f(t)\mathrm{d}t = \int_{0}^{x}\frac{t}{2}\mathrm{d}t = \frac{x^2}{4}.</equation>当<equation>x\geqslant 2</equation>时，<equation>F(x) = 1.</equation>于是，<equation>F ( x ) = \left\{ \begin{array}{ll} 0, & x < 0, \\ \frac{x^{2}}{4}, & 0 \leqslant x < 2, \\ 1, & x \geqslant 2. \end{array} \right.</equation>因此，<equation>\begin{array}{l} P \left\{F (X) > E (X) - 1 \right\} = P \left\{F (X) > \frac {1}{3} \right\} = P \left\{\frac {X ^ {2}}{4} > \frac {1}{3}, 0 \leqslant X < 2 \right\} + P \left\{X \geqslant 2 \right\} \\ = P \left\{\frac {2}{\sqrt {3}} < X < 2 \right\} + \int_ {2} ^ {+ \infty} f (x) \mathrm {d} x = 1 - \int_ {0} ^ {\frac {2}{\sqrt {3}}} \frac {x}{2} \mathrm {d} x + 0 \\ = 1 - \frac {x ^ {2}}{4} \Bigg | _ {0} ^ {\frac {2}{\sqrt {3}}} = \frac {2}{3}. \\ \end{array}</equation>（法二）我们先证明<equation>Y=F(X)</equation>服从（0，1）上的均匀分布.

注意到 F(x)在（0，2）上严格单调增加，其值域为（0，1），故可定义<equation>F^{-1}(y), y\in(0,1).</equation>考虑 Y的分布函数<equation>F_{Y}(y).</equation>当<equation>y < 0</equation>时，由于<equation>F ( X )</equation>仅在[0，1]上取值，故<equation>F_{Y} ( y )=0.</equation>当<equation>0\leqslant y < 1</equation>时，<equation>F _ {Y} (y) = P \left\{Y \leqslant y \right\} = P \left\{F (X) \leqslant y \right\} = P \left\{X \leqslant F ^ {- 1} (y) \right\} = F \left(F ^ {- 1} (y)\right) = y.</equation>当<equation>y \geqslant 1</equation>时，<equation>P\{Y \leqslant y\} = 1</equation>，即<equation>F_{Y}(y) = 1.</equation>因此，<equation>F_{Y}(y)=\left\{ \begin{array}{ll}0,& y<0,\\ y,& 0\leqslant y<1,\\ 1,& y\geqslant 1. \end{array} \right.</equation>这说明<equation>Y=F(X)</equation>服从（0，1）上的均匀分布.

由法一可知<equation>E ( X )=\frac{4}{3}</equation>，故<equation>P \left\{F (X) > E (X) - 1 \right\} = P \left\{F (X) > \frac {1}{3} \right\} = 1 - P \left\{F (X) \leqslant \frac {1}{3} \right\} = 1 - \frac {1}{3} = \frac {2}{3}.</equation>

---

**2017年第14题 | 填空题 | 4分**

14. 设随机变量 X的概率分布为<equation>P\{X=-2\}=\frac{1}{2}, P\{X=1\}=a, P\{X=3\}=b</equation>，若<equation>E(X)=0</equation>，则 D(X) =___

**答案:**# 9 2.

**解析:**解 由于<equation>P\{X=-2\}=\frac{1}{2}, P\{X=1\}=a, P\{X=3\}=b</equation>为随机变量X的分布律，故<equation>\frac{1}{2}+a+b=1</equation>即 a+b<equation>= 1</equation>，即 a+b<equation>= \frac{1}{2}.</equation>又因为<equation>E ( X )=0</equation>，所以<equation>(-2)\times \frac{1}{2}+1\times a+3\times b=0</equation>，即<equation>a+3b=1.</equation>联立<equation>\left\{ \begin{array}{l l} a+b=\frac{1}{2}, \\ a+3b=1, \end{array} \right.</equation>解得 a=b=<equation>\frac{1}{4}.</equation>代入<equation>D ( X )=\sum_{k=1}^{\infty} \left[ x_{k}-E ( X ) \right]^{2} p_{k}</equation>得，<equation>D (X) = (- 2 - 0) ^ {2} \times \frac {1}{2} + (1 - 0) ^ {2} \times \frac {1}{4} + (3 - 0) ^ {2} \times \frac {1}{4} = 2 + \frac {1}{4} + \frac {9}{4} = \frac {9}{2}.</equation>也可以利用公式<equation>D ( X )=E \left( X^{2} \right)-\left[ E ( X ) \right]^{2}</equation>来计算.<equation>E \left(X ^ {2}\right) = 4 \times \frac {1}{2} + 1 \times \frac {1}{4} + 9 \times \frac {1}{4} = \frac {9}{2}, \quad D (X) = \frac {9}{2} - 0 = \frac {9}{2}.</equation>

---