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


