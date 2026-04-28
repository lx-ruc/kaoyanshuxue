#### 导数与微分的概念

**2025年第3题 | 选择题 | 5分 | 答案: D**

3. 设函数 f(x)在区间<equation>[0,+\infty)</equation>上可导，则（    )

A. 当<equation>\lim_{x\rightarrow+\infty}f(x)</equation>存在时，<equation>\lim_{x\rightarrow+\infty}f^{\prime}(x)</equation>存在

B. 当<equation>\lim_{x\rightarrow+\infty}f^{\prime}(x)</equation>存在时，<equation>\lim_{x\rightarrow+\infty}f(x)</equation>存在

C. 当<equation>\lim_{x\rightarrow+\infty}\frac{\int_{0}^{x}f(t)\mathrm{d}t}{x}</equation>存在时，<equation>\lim_{x\rightarrow+\infty}f(x)</equation>存在

D. 当<equation>\lim_{x\rightarrow+\infty}f(x)</equation>存在时，<equation>\lim_{x\rightarrow+\infty}\frac{\int_{0}^{x}f(t)\mathrm{d}t}{x}</equation>存在

答案: D

**解析:**解 对选项D，由于<equation>\lim_{x\rightarrow +\infty}f(x)</equation>存在，故可对<equation>\lim_{x\rightarrow +\infty}\frac{\int_{0}^{x}f(t)\mathrm{d}t}{x}</equation>应用洛必达法则得到<equation>\lim_{x\rightarrow +\infty}\frac{\int_{0}^{x}f(t)\mathrm{d}t}{x}\overset{\mathrm{洛必达}}{=}\lim_{x\rightarrow +\infty}\frac{f(x)}{1}=\lim_{x\rightarrow +\infty}f(x).</equation>由<equation>\lim_{x\to +\infty}f(x)</equation>存在可得<equation>\lim_{x\to +\infty}\frac{\int_0^x f(t)\mathrm{d}t}{x}</equation>存在.选项D正确.

因此，应选D.

下面说明选项A、B、C不正确.

对选项A，取<equation>f ( x )=\left\{\begin{array}{ll}\frac{\sin x^{2}}{x},&x\neq 0,\\ 0,&x=0,\end{array} \right.</equation>则<equation>\lim_{x\to 0}f(x)=\lim_{x\to 0}\frac{\sin x^{2}}{x^{2}}\cdot x=0=f(0),f^{\prime}(0)=</equation><equation>\lim_{x\to 0}\frac{\frac{\sin x^{2}}{x}-0}{x-0}=\lim_{x\to 0}\frac{\sin x^{2}}{x^{2}}=1,f(x)</equation>在<equation>x=0</equation>处可导，<equation>\lim_{x\to +\infty}f(x)=\lim_{x\to +\infty}\frac{\sin x^{2}}{x}=0</equation>，但当<equation>x\neq 0</equation>时，<equation>f^{\prime}(x)=\frac{x\cdot\cos x^{2}\cdot 2x-\sin x^{2}}{x^{2}}=2\cos x^{2}-\frac{\sin x^{2}}{x^{2}},\lim_{x\to +\infty}f^{\prime}(x)</equation>不存在. 对选项B，取<equation>f ( x )=x</equation>，则<equation>f^{\prime}(x)=1</equation>，<equation>\lim_{x\to +\infty}f^{\prime}(x)=1</equation>，但<equation>\lim_{x\to +\infty}f(x)</equation>不存在.

对选项C，取<equation>f ( x )=\cos x</equation>，则<equation>\int_{0}^{x} f ( t ) \mathrm{d} t=\sin x</equation><equation>\lim_{x\rightarrow+\infty}\frac{\int_{0}^{x} f ( t ) \mathrm{d} t}{x}=\lim_{x\rightarrow+\infty}\frac{\sin x}{x}=0</equation>，但<equation>\lim_{x\rightarrow+\infty}f ( x )</equation>不存在.

---

**2024年第4题 | 选择题 | 5分 | 答案: B**

4. 设函数 f(x)在区间（-1，1）上有定义，且<equation>\lim_{x\rightarrow 0}f(x)=0</equation>，则（    )

A. 当<equation>\lim_{x\rightarrow 0}\frac{f(x)}{x}=m</equation>时，<equation>f^{\prime}(0)=m</equation>B. 当<equation>f^{\prime}(0)=m</equation>时，<equation>\lim_{x\rightarrow 0}\frac{f(x)}{x}=m</equation>C. 当<equation>\lim_{x\rightarrow 0}f^{\prime}(x)=m</equation>时，<equation>f^{\prime}(0)=m</equation>D. 当<equation>f^{\prime}(0)=m</equation>时，<equation>\lim_{x\rightarrow 0}f^{\prime}(x)=m</equation>

答案: B

**解析:**解 若<equation>f^{\prime}(0)=m</equation>，则 f(x)在 x=0处连续.结合<equation>\lim_{x\to 0}f(x)=0</equation>可得 f(0)=0.由导数的定义可知<equation>\lim_{x\to 0}\frac{f(x)}{x}=\lim_{x\to 0}\frac{f(x)-f(0)}{x-0}=f^{\prime}(0)=m.</equation>因此，选项B正确.

下面说明选项A、C、D不正确.

对选项A、C，取<equation>f ( x )=\left\{\begin{array}{ll}m x,&x\neq 0\\ 1,&x=0\end{array} \right.</equation>则<equation>\lim_{x\to 0}\frac{f(x)}{x}=m</equation>，且<equation>\lim_{x\to 0}f^{\prime}(x)=m</equation>，但<equation>f ( x )</equation>在<equation>x=0</equation>处不连续，从而<equation>f^{\prime}(0)</equation>不存在.

对选项D，取<equation>f(x) = \left\{ \begin{array}{ll} m x + x^{2}\sin \frac{1}{x}, & x\neq 0, \\ 0, & x = 0, \end{array} \right.</equation>则<equation>f ^ {\prime} (0) = \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0} \frac {m x + x ^ {2} \sin \frac {1}{x}}{x} = m.</equation>但当<equation>x\neq 0</equation>时，<equation>f^{\prime}(x) = m + 2x\sin \frac{1}{x} -\cos \frac{1}{x},\lim_{x\to 0}f^{\prime}(x)</equation>不存在.

综上所述，应选B.

---

**2023年第3题 | 选择题 | 5分 | 答案: C**

3. 设函数 y=f(x)由<equation>\left\{\begin{array}{l l}x=2 t+|t|\\y=|t|\sin t\end{array}\right.</equation>确定，则（    )

A. f(x)连续，<equation>f^{\prime}(0)</equation>不存在 B.<equation>f^{\prime}(0)</equation>存在，<equation>f^{\prime}(x)</equation>在 x=0处不连续

C.<equation>f^{\prime}(x)</equation>连续，<equation>f^{\prime\prime}(0)</equation>不存在 D.<equation>f^{\prime\prime}(0)</equation>存在，<equation>f^{\prime\prime}(x)</equation>在 x=0处不连续

答案: C

**解析:**解 由于<equation>x=2 t+|t|=\left\{\begin{array}{ll}3 t,& t\geqslant 0\\ t,& t<0\end{array}\right.</equation>在<equation>(-\infty ,+\infty)</equation>上单调增加，且值域为<equation>(-\infty ,+\infty)</equation>，

故其存在反函数<equation>t=\left\{\begin{array}{ll}\frac{x}{3},& x\geqslant 0\\ x,& x<0.\end{array}\right.</equation>当<equation>x\geqslant 0</equation>时，<equation>t\geqslant 0</equation>；当<equation>x<0</equation>时，<equation>t<0</equation>．于是，<equation>f(x)=</equation>由其表达式可知，<equation>f(x)</equation>在<equation>x\neq0</equation>处连续．又由于<equation>\lim_{x\to 0}f(x)=0=f(0)</equation>，故<equation>f(x)</equation>在<equation>x=0</equation>处亦连续．因此<equation>f(x)</equation>连续.

计算可得<equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {f (x) - f (0)}{x - 0} \xlongequal {f (0) = 0} \lim _ {x \rightarrow 0 ^ {-}} \frac {- x \sin x}{x} = 0,</equation><equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x - 0} \xlongequal {f (0) = 0} \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {x}{3} \sin \frac {x}{3}}{x} = 0.</equation><equation>f(x)</equation>在<equation>x = 0</equation>处的左、右导数均存在且相等，故<equation>f^{\prime}(0)</equation>存在，且<equation>f^{\prime}(0) = 0.</equation>选项A不正确.

当 x < 0时，<equation>f ^ {\prime} (x) = \left(- x \sin x\right) ^ {\prime} = - \sin x - x \cos x.</equation>当 x > 0时，<equation>f ^ {\prime} (x) = \left(\frac {x}{3} \sin \frac {x}{3}\right) ^ {\prime} = \frac {1}{3} \left(\sin \frac {x}{3} + \frac {x}{3} \cos \frac {x}{3}\right).</equation>由此可知<equation>f^{\prime}(x)</equation>在<equation>x\neq0</equation>处连续.又由于<equation>\lim_{x\to0^{-}}f^{\prime}(x)=\lim_{x\to0^{+}}f^{\prime}(x)=0=f^{\prime}(0)</equation>，故<equation>f^{\prime}(x)</equation>在<equation>x=0</equation>处亦连续.因此<equation>f^{\prime}(x)</equation>连续.选项B不正确.

进一步计算可得，<equation>\begin{aligned} f _ {-} ^ {\prime \prime} (0) &= \lim _ {x \rightarrow 0 ^ {-}} \frac {f ^ {\prime} (x) - f ^ {\prime} (0)}{x - 0} \xlongequal {f ^ {\prime} (0) = 0} \lim _ {x \rightarrow 0 ^ {-}} \frac {- \sin x - x \cos x}{x} \\ &= - \lim _ {x \rightarrow 0 ^ {-}} \left(\frac {\sin x}{x} + \cos x\right) = - (1 + 1) = - 2, \end{aligned}</equation><equation>\begin{aligned} f _ {+} ^ {\prime \prime} (0) &= \lim _ {x \rightarrow 0 ^ {+}} \frac {f ^ {\prime} (x) - f ^ {\prime} (0)}{x - 0} \xlongequal {f ^ {\prime} (0) = 0} \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {1}{3} \left(\sin \frac {x}{3} + \frac {x}{3} \cos \frac {x}{3}\right)}{x} \\ &= \frac {1}{3} \lim _ {x \rightarrow 0 ^ {+}} \left(\frac {1}{3} \cdot \frac {\sin \frac {x}{3}}{\frac {x}{3}} + \frac {1}{3} \cos \frac {x}{3}\right) = \frac {1}{3} \times \left(\frac {1}{3} + \frac {1}{3}\right) = \frac {2}{9}. \end{aligned}</equation>由于<equation>f_{+}^{\prime \prime}(0)\neq f_{+}^{\prime \prime}(0),</equation>故<equation>f^{\prime \prime}(0)</equation>不存在.选项C正确，选项D不正确.

综上所述，应选C.

---

**2022年第1题 | 选择题 | 5分 | 答案: B**

1. 设函数 f(x)满足<equation>\lim_{x\to 1}\frac{f(x)}{\ln x}=1</equation>，则（    ）

A. f(1)=0 B.<equation>\lim_{x\to 1}f(x)=0</equation>C.<equation>f^{\prime}(1)=1</equation>D.<equation>\lim_{x\to 1}f^{\prime}(x)=1</equation>

答案: B

**解析:**解 当 x→1时，<equation>\lim_{x\rightarrow 1}\ln x=0</equation>，而<equation>\lim_{x\rightarrow 1}\frac{f(x)}{\ln x}=1</equation>，故分子 f(x)满足<equation>\lim_{x\rightarrow 1}f(x)=0</equation>.应选B.下面说明选项A、C、D不正确.

对选项A、C，可以举函数<equation>f(x)</equation>在<equation>x=1</equation>处不连续，从而也不可导的例子.

对选项D，若<equation>f(x)</equation>在<equation>x=1</equation>的某去心邻域内可导，且<equation>\lim_{x\to 1}f^{\prime}(x)</equation>存在，则由洛必达法则，<equation>\lim _ {x \rightarrow 1} \frac {f (x)}{\ln x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 1} \frac {f ^ {\prime} (x)}{\frac {1}{x}} = \lim _ {x \rightarrow 1} f ^ {\prime} (x).</equation>于是，<equation>\lim_{x\to 1}f^{\prime}(x)=\lim_{x\to 1}\frac{f(x)}{\ln x}=1.</equation>因此，要举出选项D的反例，需考虑 f(x)在 x=1的某去心邻域内不可导或者<equation>\lim_{x\to 1}f^{\prime}(x)</equation>不存在的例子.

考虑<equation>f ( x )=\left\{\begin{array}{ll}x-1+2(x-1)^{2}\sin \frac{1}{x-1},&x\neq 1,\\ 1,&x=1,\end{array} \right.</equation>则<equation>\lim_{x\to 1}f(x)=0</equation>，但<equation>f ( 1 )=1</equation><equation>f ( x )</equation>在<equation>x=1</equation>处不连续，也就不可导.

当<equation>x\neq 1</equation>时，<equation>f^{\prime}(x) = 1 + 4(x - 1)\sin \frac{1}{x - 1} - 2\cos \frac{1}{x - 1}</equation>. 不难发现，<equation>x = 1</equation>是<equation>f^{\prime}(x)</equation>的振荡间断点，<equation>\lim_{x\to 1}f^{\prime}(x)</equation>不存在.

---

**2021年第1题 | 选择题 | 5分 | 答案: D**

1. 函数 f(x) =<equation>\left\{\begin{array}{l l}{\frac{\mathrm{e}^{x}-1}{x},}&{x\neq0,}\\ {1,}&{x=0}\end{array} \right.</equation>在 x=0处（    ）

A. 连续且取得极大值 B. 连续且取得极小值 C. 可导且导数等于零 D. 可导且导数不为零

答案: D

**解析:**解 首先考虑 f(x)在 x=0处的连续性.<equation>\lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x} - 1}{x} \xlongequal {\mathrm {e} ^ {x} - 1 \sim x} \lim _ {x \rightarrow 0} \frac {x}{x} = 1 = f (0).</equation>于是，<equation>f ( x )</equation>在<equation>x=0</equation>处连续

下面考虑<equation>f ( x )</equation>在<equation>x=0</equation>处的可导性.<equation>f ^ {\prime} (0) = \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0} \frac {\frac {\mathrm {e} ^ {x} - 1}{x} - 1}{x} = \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x} - 1 - x}{x ^ {2}} \frac {\mathrm {e} ^ {x} = 1 + x + \frac {x ^ {2}}{2} + o \left(x ^ {2}\right)}{\frac {1}{2} \neq 0}.</equation>于是，<equation>f ( x )</equation>在<equation>x=0</equation>处可导且导数不为0.

因此，应选D.

下面说明选项A、B不正确.

由于<equation>f^{\prime}(0)\neq 0</equation>，故<equation>x = 0</equation>不满足成为极值点的必要条件，从而选项A、B均不正确.

---

**2020年第2题 | 选择题 | 4分 | 答案: C**

2. 设函数 f(x)在区间（-1，1）内有定义，且<equation>\lim_{x\rightarrow 0}f(x)=0</equation>，则（    )

A. 当<equation>\lim_{x\rightarrow 0}\frac{f(x)}{\sqrt{|x|}}=0</equation>时，f(x)在 x=0处可导 B. 当<equation>\lim_{x\rightarrow 0}\frac{f(x)}{x^{2}}=0</equation>时，f(x)在 x=0处可导

C. 当 f(x)在 x=0处可导时，<equation>\lim_{x\rightarrow 0}\frac{f(x)}{\sqrt{|x|}}=0</equation>D. 当 f(x)在 x=0处可导时，<equation>\lim_{x\rightarrow 0}\frac{f(x)}{x^{2}}=0</equation>

答案: C

**解析:**解 若 f(x)在 x=0处可导，则 f(x)在 x=0处连续.由<equation>\lim_{x\rightarrow 0}f(x)=0</equation>可得 f(0)=0.并且，由 f(x)在 x=0处可导可得<equation>f ^ {\prime} (0) = \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0} \xlongequal {f (0) = 0} \lim _ {x \rightarrow 0} \frac {f (x)}{x}.</equation>计算<equation>\lim_{x\to 0}\frac{f(x)}{\sqrt{|x|}}.</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {f (x)}{\sqrt {| x |}} = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x)}{\sqrt {x}} = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x)}{x} \cdot \sqrt {x} = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x)}{x} \cdot \lim _ {x \rightarrow 0 ^ {+}} \sqrt {x} = 0.</equation><equation>\lim _ {x \rightarrow 0 ^ {-}} \frac {f (x)}{\sqrt {| x |}} = \lim _ {x \rightarrow 0 ^ {-}} \frac {f (x)}{\sqrt {- x}} = \lim _ {x \rightarrow 0 ^ {-}} \frac {f (x)}{- x} \cdot \sqrt {- x} = - \lim _ {x \rightarrow 0 ^ {-}} \frac {f (x)}{x} \cdot \lim _ {x \rightarrow 0 ^ {-}} \sqrt {- x} = 0.</equation><equation>\lim_{x\to 0^{+}}\frac{f(x)}{\sqrt{|x|}} = \lim_{x\to 0^{-}}\frac{f(x)}{\sqrt{|x|}} = 0</equation>，即<equation>\lim_{x\to 0}\frac{f(x)}{\sqrt{|x|}} = 0.</equation>选项C正确.应选C.

下面说明其余选项均不正确.

选项A、B：取<equation>f ( x )=\left\{\begin{array}{ll}x^{3},&x\neq 0\\ 1,&x=0\end{array} \right.</equation>则<equation>\lim_{x\to 0}\frac{f(x)}{\sqrt{|x|}}=0,\lim_{x\to 0}\frac{f(x)}{x^{2}}=0</equation>，但<equation>f ( x )</equation>在<equation>x=0</equation>处不连续，当然也不可导.

选项D：取<equation>f ( x ) = x</equation>，则<equation>f ( x )</equation>在<equation>x=0</equation>处可导，但<equation>\lim_{x\to 0}\frac{f(x)}{x^{2}}</equation>不存在.

---

**2018年第1题 | 选择题 | 4分 | 答案: D**

1. 下列函数中，在 x=0处不可导的是（    ）

A. f(x）=|x|<equation>\sin |x|</equation>B. f(x)=|x|<equation>\sin \sqrt{|x|}</equation>C. f(x)=<equation>\cos |x|</equation>D. f(x)=<equation>\cos \sqrt{|x|}</equation>

答案: D

**解析:**考虑选项D.<equation>f (x) = \left\{ \begin{array}{l l} \cos \sqrt {x}, & x \geqslant 0, \\ \cos \sqrt {- x}, & x < 0. \end{array} \right.</equation><equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {\cos \sqrt {- x} - 1}{x - 0} \frac {\cos \sqrt {- x} - 1 \sim - \frac {\left(\sqrt {- x}\right) ^ {2}}{2}}{\lim _ {x \rightarrow 0 ^ {-}} \frac {x}{x}} = \frac {1}{2},</equation><equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {\cos \sqrt {x} - 1}{x - 0} \xlongequal {\cos \sqrt {x} - 1 \sim - \frac {(\sqrt {x}) ^ {2}}{2}} \lim _ {x \rightarrow 0 ^ {+}} \frac {- \frac {x}{2}}{x} = - \frac {1}{2}.</equation>由于<equation>f_{-}^{\prime}(0)\neq f_{+}^{\prime}(0)</equation>，故<equation>f(x) = \cos \sqrt{|x|}</equation>在<equation>x = 0</equation>处不可导.应选D.

下面分别说明选项A、B、C不正确.

选项A：<equation>f ( x )=\left\{\begin{array}{ll}x\sin x,&x\geqslant 0,\\ -x\sin(-x),&x<0.\end{array} \right.</equation>又因为<equation>- x\sin(-x)=-x\cdot(-\sin x)=x\sin x</equation>，所以<equation>f ( x )=x\sin x,f ( x )</equation>在 x=0处可导.

选项B：<equation>f ( x ) = \left\{ \begin{array}{ll} x \sin \sqrt{x}, & x \geqslant 0, \\ - x \sin \sqrt{-x}, & x < 0. \end{array} \right.</equation><equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {- x \sin \sqrt {- x} - 0}{x - 0} = \lim _ {x \rightarrow 0 ^ {-}} (- \sin \sqrt {- x}) = 0,</equation><equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {x \sin \sqrt {x} - 0}{x - 0} = \lim _ {x \rightarrow 0 ^ {+}} \sin \sqrt {x} = 0.</equation>由于<equation>f_{-}^{\prime}(0) = f_{+}^{\prime}(0)</equation>，故<equation>f(x) = |x|\sin \sqrt{|x|}</equation>在<equation>x = 0</equation>处可导.

选项C：<equation>f ( x )=\left\{\begin{array}{ll}\cos x,&x\geqslant 0,\\ \cos(-x),&x<0.\end{array} \right.</equation>又因为<equation>\cos(-x)=\cos x</equation>，所以<equation>f ( x )=\cos x,f ( x )</equation>在<equation>x=0</equation>处可导.

---

**2016年第4题 | 选择题 | 4分 | 答案: D**

4. 已知函数 f(x) =<equation>\left\{\begin{array}{l l}{x,}&{x \leqslant 0,}\\ {\frac{1}{n},}&{\frac{1}{n+1}<x \leqslant \frac{1}{n},(n=1,2,\cdots),}\end{array} \right.</equation>则（    )

A. x=0是 f(x) 的第一类间断点 B. x=0是 f(x) 的第二类间断点

C. f(x)在 x=0处连续但不可导 D. f(x)在 x=0处可导

答案: D

**解析:**解 由题设知，<equation>f(0)=0</equation>，于是<equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0 ^ {-}} \frac {x}{x} = 1,</equation><equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x)}{x}.</equation>当<equation>\frac{1}{n+1}<x\leqslant \frac{1}{n}</equation>时，<equation>f(x)=\frac{1}{n}</equation>从而<equation>1\leqslant \frac{f(x)}{x}=\frac{\frac{1}{n}}{x}<\frac{n+1}{n}</equation>当<equation>x\to 0^{+}</equation>时，<equation>n\to \infty</equation><equation>\frac{n+1}{n}\to 1</equation>由夹逼准则知，<equation>\lim_{x\to 0^{+}}\frac{f(x)}{x}=1</equation>即<equation>f_{+}^{\prime}(0)=1</equation>于是<equation>f_{+}^{\prime}(0)=f_{-}^{\prime}(0)</equation>从而f(x)在x=0处可导.应选D.

---

**2015年第18题 | 解答题 | 10分**

18. (本题满分10分)

I. 设函数<equation>u ( x ) , v ( x )</equation>可导，利用导数定义证明<equation>[ u ( x ) v ( x ) ]^{\prime}=u^{\prime} ( x ) v ( x )+u ( x ) v^{\prime} ( x )</equation>；

II. 设函数<equation>u_{1} ( x ) , u_{2} ( x ) , \cdots , u_{n} ( x )</equation>可导，<equation>f ( x )=u_{1} ( x ) u_{2} ( x ) \cdots u_{n} ( x )</equation>，写出 f(x)的求导公

**答案:**(18) （I）证明略；<equation>(\mathrm {I I}) [ f (x) ] ^ {\prime} = \sum_ {i = 1} ^ {n} \left[ u _ {i} ^ {\prime} (x) \prod_ {\substack {j \neq i, \\ 1 \leqslant j \leqslant n}} u _ {j} (x) \right].</equation>

**解析:**解（I）（法一）由导数的定义知，<equation>\begin{aligned} [ u (x) v (x) ] ^ {\prime} &= \lim _ {h \rightarrow 0} \frac {u (x + h) v (x + h) - u (x) v (x)}{h} \\ &= \lim _ {h \rightarrow 0} \frac {u (x + h) v (x + h) - u (x) v (x + h) + u (x) v (x + h) - u (x) v (x)}{h} \\ &= \lim _ {h \rightarrow 0} \frac {u (x + h) - u (x)}{h} \cdot v (x + h) + \lim _ {h \rightarrow 0} u (x) \cdot \frac {v (x + h) - v (x)}{h} \\ \underline {{= \frac {u (x) , v (x) \text {均 可 导}}{2}}} u ^ {\prime} (x) v (x) + u (x) v ^ {\prime} (x). \end{aligned}</equation>（法二）由导数的定义知，<equation>\begin{aligned} [ u (x) v (x) ] ^ {\prime} &= \lim _ {h \rightarrow 0} \frac {u (x + h) v (x + h) - u (x) v (x)}{h} \\ &= \lim _ {h \rightarrow 0} \frac {u (x + h) v (x + h) - u (x + h) v (x) + u (x + h) v (x) - u (x) v (x)}{h} \\ &= \lim _ {h \rightarrow 0} u (x + h) \cdot \frac {v (x + h) - v (x)}{h} + \lim _ {h \rightarrow 0} \frac {u (x + h) - u (x)}{h} \cdot v (x) \\ \underline {{= \frac {u (x) , v (x) \text {均 可 导}}{2}}} u (x) v ^ {\prime} (x) + u ^ {\prime} (x) v (x). \end{aligned}</equation>（Ⅱ）由第（Ⅰ）问知，<equation>\begin{array}{l} [ f (x) ] ^ {\prime} = \left\{u _ {1} (x) \left[ u _ {2} (x) \dots u _ {n} (x) \right] \right\} ^ {\prime} \\ = u _ {1} ^ {\prime} (x) u _ {2} (x) \dots u _ {n} (x) + u _ {1} (x) \left[ u _ {2} (x) \dots u _ {n} (x) \right] ^ {\prime} \\ = u _ {1} ^ {\prime} (x) u _ {2} (x) \dots u _ {n} (x) + u _ {1} (x) \left\{u _ {2} (x) \cdot \left[ u _ {3} (x) \dots u _ {n} (x) \right] \right\} ^ {\prime} \\ = u _ {1} ^ {\prime} (x) u _ {2} (x) \dots u _ {n} (x) + u _ {1} (x) \left\{u _ {2} ^ {\prime} (x) u _ {3} (x) \dots u _ {n} (x) + u _ {2} (x) \left[ u _ {3} (x) \dots u _ {n} (x) \right] ^ {\prime} \right\} \\ = u _ {1} ^ {\prime} (x) u _ {2} (x) \dots u _ {n} (x) + u _ {1} (x) u _ {2} ^ {\prime} (x) u _ {3} (x) \dots u _ {n} (x) + u _ {1} (x) u _ {2} (x) \left[ u _ {3} (x) \dots u _ {n} (x) \right] ^ {\prime} \\ = \dots \\ = u _ {1} ^ {\prime} (x) u _ {2} (x) \dots u _ {n} (x) + u _ {1} (x) u _ {2} ^ {\prime} (x) \dots u _ {n} (x) + \dots + u _ {1} (x) u _ {2} (x) \dots u _ {n} ^ {\prime} (x) \\ = \sum_ {i = 1} ^ {n} \left[ u _ {i} ^ {\prime} (x) \prod_ {\substack {j \neq i, \\ 1 \leqslant j \leqslant n}} u _ {j} (x) \right]. \\ \end{array}</equation>

---


