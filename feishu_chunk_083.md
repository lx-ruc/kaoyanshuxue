#### 不定积分的计算

**2018年第15题 | 解答题 | 10分**

15. (本题满分10分)

求不定积分

**答案:**<equation>\frac{\mathrm{e}^{2x}\arctan \sqrt{\mathrm{e}^{x} - 1}}{2} -\frac{1}{6}\left(\mathrm{e}^{x} - 1\right)^{\frac{3}{2}} - \frac{1}{2}\sqrt{\mathrm{e}^{x} - 1} + C</equation>，其中C为任意常数.

**解析:**解 利用分部积分法.<equation>\begin{aligned} \int \mathrm {e} ^ {2 x} \arctan \sqrt {\mathrm {e} ^ {x} - 1} \mathrm {d} x \stackrel {\text {分 部 积 分}} {=} \frac {1}{2} \int \arctan \sqrt {\mathrm {e} ^ {x} - 1} \mathrm {d} \left(\mathrm {e} ^ {2 x}\right) \\ &= \frac {\mathrm {e} ^ {2 x}}{2} \cdot \arctan \sqrt {\mathrm {e} ^ {x} - 1} - \frac {1}{2} \int \mathrm {e} ^ {2 x} \cdot \frac {1}{1 + \mathrm {e} ^ {x} - 1} \cdot \frac {\mathrm {e} ^ {x}}{2 \sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x \\ &= \frac {\mathrm {e} ^ {2 x} \arctan \sqrt {\mathrm {e} ^ {x} - 1}}{2} - \frac {1}{4} \int \frac {\mathrm {e} ^ {2 x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x. \end{aligned}</equation>下面用两种方法计算<equation>\int \frac{\mathrm{e}^{2x}}{\sqrt{\mathrm{e}^{x} - 1}}\mathrm{d}x.</equation>（法一）令<equation>u = \sqrt{\mathrm{e}^{x} - 1}</equation>，则<equation>x = \ln (u^{2} + 1)</equation>，<equation>\mathrm{d}x = \frac{2u}{u^{2} + 1}\mathrm{d}u.</equation><equation>\begin{aligned} \int \frac {\mathrm {e} ^ {2 x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x &= \int \frac {\left(u ^ {2} + 1\right) ^ {2}}{u} \cdot \frac {2 u}{u ^ {2} + 1} \mathrm {d} u = 2 \int \left(u ^ {2} + 1\right) \mathrm {d} u = \frac {2}{3} u ^ {3} + 2 u + C _ {1} \\ &= \frac {2}{3} \left(\mathrm {e} ^ {x} - 1\right) ^ {\frac {3}{2}} + 2 \sqrt {\mathrm {e} ^ {x} - 1} + C _ {1}, \end{aligned}</equation>其中<equation>C_{1}</equation>为任意常数.

（法二）令<equation>t = \mathrm{e}^{x}</equation>，则<equation>\mathrm{d}t = \mathrm{e}^{x}\mathrm{d}x.</equation><equation>\begin{aligned} \int \frac {\mathrm {e} ^ {2 x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x &= \int \frac {\mathrm {e} ^ {x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} \left(\mathrm {e} ^ {x}\right) = \int \frac {t}{\sqrt {t - 1}} \mathrm {d} t = \int \frac {t - 1 + 1}{\sqrt {t - 1}} \mathrm {d} t = \int \left(\sqrt {t - 1} + \frac {1}{\sqrt {t - 1}}\right) \mathrm {d} t \\ &= \frac {2}{3} (t - 1) ^ {\frac {3}{2}} + 2 \sqrt {t - 1} + C _ {1} = \frac {2}{3} \left(\mathrm {e} ^ {x} - 1\right) ^ {\frac {3}{2}} + 2 \sqrt {\mathrm {e} ^ {x} - 1} + C _ {1}, \end{aligned}</equation>其中<equation>C_{1}</equation>为任意常数.

因此，<equation>\text {原 积 分} = \frac {\mathrm {e} ^ {2 x} \arctan \sqrt {\mathrm {e} ^ {x} - 1}}{2} - \frac {1}{6} \left(\mathrm {e} ^ {x} - 1\right) ^ {\frac {3}{2}} - \frac {1}{2} \sqrt {\mathrm {e} ^ {x} - 1} + C,</equation>其中 C为任意常数.

---

**2016年第2题 | 选择题 | 4分 | 答案: D**

2. 已知函数<equation>f(x)=\left\{\begin{array}{l l}2(x-1),&x<1,\\ \ln x,&x\geqslant 1,\end{array} \right.</equation>则 f(x)的一个原函数是（    ）

A.<equation>F(x)=\left\{\begin{array}{l l}{(x-1)^{2},}&{x<1,}\\ {x(\ln x-1),}&{x\geqslant 1.}\\ \end{array} \right.</equation>B.<equation>F(x)=\left\{\begin{array}{l l}{(x-1)^{2},}&{x<1,}\\ {x(\ln x+1)-1,}&{x\geqslant 1.}\\ \end{array} \right.</equation>C.<equation>F(x)=\left\{\begin{array}{l l}{(x-1)^{2},}&{x<1,}\\ {x(\ln x+1)+1,}&{x\geqslant 1.}\\ \end{array} \right.</equation>D.<equation>F(x)=\left\{\begin{array}{l l}{(x-1)^{2},}&{x<1,}\\ {x(\ln x-1)+1,}&{x\geqslant 1.}\\ \end{array} \right.</equation>

答案: D

**解析:**解（法一）当 x < 1时，<equation>F (x) = \int 2 (x - 1) \mathrm {d} x = (x - 1) ^ {2} + C _ {1};</equation>当 x≥1时，<equation>F (x) = \int \ln x \mathrm {d} x = x (\ln x - 1) + C _ {2},</equation>其中<equation>C_{1}, C_{2}</equation>均为任意常数.

进一步，由于<equation>F(x)</equation>是<equation>f(x)</equation>在<equation>(-\infty , + \infty)</equation>上的一个原函数，故<equation>F(x)</equation>在<equation>x = 1</equation>处应连续.<equation>\lim _ {x \rightarrow 1 ^ {-}} F (x) = \lim _ {x \rightarrow 1 ^ {-}} \left(x - 1\right) ^ {2} + C _ {1} = C _ {1}, \quad \lim _ {x \rightarrow 1 ^ {+}} F (x) = \lim _ {x \rightarrow 1 ^ {+}} x \left(\ln x - 1\right) + C _ {2} = C _ {2} - 1.</equation>若<equation>F ( x )</equation>连续，则<equation>C_{1}=C_{2}-1.</equation>选项D中，<equation>C_{1}=0, C_{2}=1, F(x)</equation>连续，应选D.

（法二）首先，由于<equation>F ( x )</equation>是<equation>f ( x )</equation>的原函数，故必连续，而四个选项中的<equation>F ( x )</equation>均是分段函数，于是我们可以分别考察<equation>F ( x )</equation>在分界点处的连续性.

选项A：<equation>\lim_{x\to 1^{-}}F(x)=0,\lim_{x\to 1^{+}}F(x)=-1.F(x)</equation>不连续.

选项B：<equation>\lim_{x\to 1^{-}}F(x)=\lim_{x\to 1^{+}}F(x)=0=F(1). F(x)</equation>连续.

选项C：<equation>\lim_{x\to 1^{-}}F(x) = 0</equation>，<equation>\lim_{x\to 1^{+}}F(x) = 2.F(x)</equation>不连续.

选项D：<equation>\lim_{x\to 1^{-}}F(x) = \lim_{x\to 1^{+}}F(x) = 0 = F(1).F(x)</equation>连续.

由上可排除选项A与选项C.

选项B与选项D的差别在于函数表达式.

计算<equation>f(x)</equation>在<equation>[1, +\infty)</equation>上的原函数，得<equation>\int f (x) \mathrm {d} x = \int \ln x \mathrm {d} x = x (\ln x - 1) + C,</equation>其中 C为任意常数.比较（1）式与选项B、选项D，可排除选项B.应选D.

---


### 常微分方程


