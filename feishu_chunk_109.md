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


