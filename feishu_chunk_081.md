#### 反常积分的计算与敛散性

**2021年第11题 | 填空题 | 5分**

<equation>\int_ {0} ^ {+ \infty} \frac {1}{x ^ {2} + 2 x + 2} \mathrm {d} x = \underline {{}}</equation>

**答案:**##<equation>\frac{\pi}{4}</equation>

**解析:**将<equation>x^{2}+2 x+2</equation>配方.<equation>\begin{aligned} \int_ {0} ^ {+ \infty} \frac {\mathrm {d} x}{x ^ {2} + 2 x + 2} &= \int_ {0} ^ {+ \infty} \frac {\mathrm {d} x}{(x + 1) ^ {2} + 1} = \int_ {0} ^ {+ \infty} \frac {\mathrm {d} (x + 1)}{(x + 1) ^ {2} + 1} = \arctan (x + 1) \Big | _ {0} ^ {+ \infty} \\ &= \frac {\pi}{2} - \arctan 1 = \frac {\pi}{2} - \frac {\pi}{4} = \frac {\pi}{4}. \end{aligned}</equation>

---

**2016年第1题 | 选择题 | 4分 | 答案: C**

1. 若反常积分<equation>\int_{0}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x</equation>收敛，则（    )

A. a < 1且b > 1 B. a > 1且b > 1 C. a < 1且a+b > 1 D. a > 1且a+b > 1

答案: C

**解析:**解 由于被积函数<equation>\frac{1}{x^{a}(1+x)^{b}}</equation>在<equation>[0,+\infty)</equation>上可能的瑕点为<equation>x=0</equation>，故将反常积分分为两部分，即<equation>\int_{0}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x=\int_{0}^{1}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x+\int_{1}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x.</equation>对于积分<equation>\int_{0}^{1}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x</equation>，若<equation>a\leqslant0</equation>，则该积分为正常的定积分；若<equation>a>0</equation>，则<equation>x=0</equation>为被积函数的瑕点.

由于<equation>\lim_{x\rightarrow 0^{+}}\frac{\frac{1}{x^{a}(1+x)^{b}}}{\frac{1}{x^{a}}}=\lim_{x\rightarrow 0^{+}}\frac{1}{(1+x)^{b}}=1</equation>，故当<equation>x\rightarrow 0^{+}</equation>时，<equation>\frac{1}{x^{a}(1+x)^{b}}</equation>与<equation>\frac{1}{x^{a}}</equation>等价. 瑕积分<equation>\int_{0}^{1}\frac{1}{x^{a}}\mathrm{d}x</equation>当且仅当<equation>0<a<1</equation>时收敛，加上<equation>a\leqslant0</equation>时的情况，<equation>\int_{0}^{1}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x</equation>当且仅当<equation>a<1</equation>时收敛.

对于反常积分<equation>\int_{1}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x</equation>，由于<equation>\lim_{x\rightarrow+\infty}\frac{\frac{1}{x^{a}(1+x)^{b}}}{\frac{1}{x^{a+b}}}=\lim_{x\rightarrow+\infty}\left(\frac{x}{1+x}\right)^{b}=1</equation>，故当<equation>x\rightarrow+\infty</equation>时，<equation>\frac{1}{x^{a}(1+x)^{b}}</equation>与<equation>\frac{1}{x^{a+b}}</equation>等价. 反常积分<equation>\int_{1}^{+\infty}\frac{1}{x^{a+b}}\mathrm{d}x</equation>当且仅当<equation>a+b>1</equation>时收敛，故<equation>\int_{1}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x</equation>当且仅当<equation>a+b>1</equation>时收敛.

综上所述，反常积分<equation>\int_{0}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}</equation>收敛当且仅当 a,b满足 a < 1 且 a+b > 1，应选 C.

---

**2013年第12题 | 填空题 | 4分**

<equation>2. \int_ {1} ^ {+ \infty} \frac {\ln x}{(1 + x) ^ {2}} \mathrm {d} x = \underline {{}}</equation>

**答案:**## ln 2.

**解析:**<equation>\begin{aligned} { } ^ { + \infty } \frac {\ln x}{( 1 + x ) ^ { 2 } } \mathrm { d } x &= - \int _ { 1 } ^ { + \infty } \ln x \mathrm { d } \left( \frac { 1 } { 1 + x } \right) = - \left[ \left. \frac {\ln x}{1 + x} \right| _ { 1 } ^ { + \infty } - \int _ { 1 } ^ { + \infty } \frac { 1 } { x ( 1 + x ) } \mathrm { d } x \right] \\ &= - \lim _ {x \rightarrow + \infty} \frac {\ln x}{1 + x} + \int_ {1} ^ {+ \infty} \left(\frac {1}{x} - \frac {1}{x + 1}\right) \mathrm {d} x \\ \underline {{\text {洛必达}}} - \lim _ {x \rightarrow + \infty} \frac {1}{x} + \ln \frac {x}{x + 1} \Bigg | _ {1} ^ {+ \infty} \\ &= 0 + \ln 1 - \ln \frac {1}{2} = \ln 2. \end{aligned}</equation>

---

**2010年第3题 | 选择题 | 4分 | 答案: D**

3. 设 m,n均是正整数，则反常积分<equation>\int_{0}^{1}\frac{\sqrt[m]{\ln^{2}(1-x)}}{\sqrt[n]{x}} \mathrm{d} x</equation>的收敛性（    ）

A. 仅与 m的取值有关 B. 仅与 n的取值有关

C. 与 m,n的取值都有关 D. 与 m,n的取值都无关

答案: D

**解析:**由于被积函数有两个可能的瑕点，<equation>x=0</equation>和<equation>x=1</equation>，故将原积分拆成两部分进行考虑.<equation>\int_ {0} ^ {1} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} \mathrm {d} x = \int_ {0} ^ {\frac {1}{2}} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} \mathrm {d} x + \int_ {\frac {1}{2}} ^ {1} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} \mathrm {d} x.</equation>先讨论<equation>\int_0^{\frac{1}{2}}\frac{[\ln(1 - x)]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>的收敛性.考虑<equation>\lim_{x\to 0^{+}}\frac{[\ln(1 - x)]^{\frac{2}{m}}}{x^{\frac{1}{n}}}</equation>.<equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} \xlongequal {\ln (1 - x) \sim (- x)} \lim _ {x \rightarrow 0 ^ {+}} x ^ {\frac {2}{m} - \frac {1}{n}} = \left\{\begin{array}{l l}0,&\frac {2}{m} - \frac {1}{n} > 0,\\1,&\frac {2}{m} - \frac {1}{n} = 0,\\\infty ,&\frac {2}{m} - \frac {1}{n} < 0.\end{array}\right.</equation>当 m，n为正整数时，<equation>\frac{2}{m} -\frac{1}{n}\geqslant \frac{2}{m} -1 > -1.</equation>- 当<equation>\frac{2}{m}-\frac{1}{n}\geqslant0</equation>时，<equation>x=0</equation>是被积函数的可去间断点，<equation>\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}</equation>在<equation>\left[0,\frac{1}{2}\right]</equation>上可积，<equation>\int_{0}^{\frac{1}{2}}\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>存在且有限.

- 当<equation>- 1 < \frac{2}{m} - \frac{1}{n} < 0</equation>时，<equation>x=0</equation>是被积函数的瑕点.取<equation>p=\frac{1}{n}-\frac{2}{m}</equation>则<equation>0 < p < 1</equation><equation>\lim_{x\rightarrow 0^{+}}\frac{x^{p}\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}=1.</equation>由极限审敛法可知反常积分<equation>\int_{0}^{\frac{1}{2}}\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>收敛.

因此，不论 m，n 取何正整数，积分<equation>\int_{0}^{\frac{1}{2}}\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>均收敛.

下面讨论<equation>\int_{\frac{1}{2}}^{1}\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>的收敛性. x=1为被积函数的瑕点.

考虑极限<equation>\lim _ {x \rightarrow 1 ^ {-}} \sqrt {1 - x} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} = \lim _ {x \rightarrow 1 ^ {-}} \sqrt {1 - x} \left[ \ln (1 - x) \right] ^ {\frac {2}{m}}.</equation>记<equation>I _ {0} = \lim _ {x \rightarrow 1 ^ {-}} \sqrt {1 - x} \left[ \ln (1 - x) \right] ^ {\frac {2}{m}} \xlongequal {u = 1 - x} \lim _ {u \rightarrow 0 ^ {+}} u ^ {\frac {1}{2}} (\ln u) ^ {\frac {2}{m}}.</equation>若 m=1，则<equation>I _ {0} = \lim _ {u \rightarrow 0 ^ {+}} \frac {\left(\ln u\right) ^ {2}}{u ^ {- \frac {1}{2}}} \xlongequal {\text {洛必达}} \lim _ {u \rightarrow 0 ^ {+}} \frac {- 4 \ln u}{u ^ {- \frac {1}{2}}} \xlongequal {\text {洛必达}} \lim _ {u \rightarrow 0 ^ {+}} 8 u ^ {\frac {1}{2}} = 0.</equation>若 m=2，则<equation>I _ {0} = \lim _ {u \rightarrow 0 ^ {+}} \frac {\ln u}{u ^ {- \frac {1}{2}}} \xlongequal {\text {洛 必达}} \lim _ {u \rightarrow 0 ^ {+}} (- 2) u ^ {\frac {1}{2}} = 0.</equation>若<equation>m > 2</equation>，则<equation>0 < \frac{2}{m} < 1</equation>，同理使用洛必达法则可计算得<equation>I_0 = 0.</equation>因此，由极限审敛法知，不论 m，n 取何正整数，积分<equation>\int_{\frac{1}{2}}^{1} \frac{\left[ \ln(1 - x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>均收敛综上所述，不论 m，n 取何正整数，积分<equation>\int_{0}^{1} \frac{\left[ \ln(1 - x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>均收敛.应选D.

---


