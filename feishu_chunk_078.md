#### 定积分的计算

**2025年第17题 | 解答题 | 10分**
17. 计算<equation>\int_ {0} ^ {1} \frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} \mathrm {d} x.</equation>
**答案: **#<equation>\frac{3\ln 2+\pi}{10}.</equation>
**解析: **解设<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {A}{x + 1} + \frac {B x + C}{x ^ {2} - 2 x + 2}.</equation>通分并整理可得，<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {(A + B) x ^ {2} + (B + C - 2 A) x + 2 A + C}{(x + 1) \left(x ^ {2} - 2 x + 2\right)}.</equation>比较<equation>x^{2}, x</equation>的系数以及常数项可得，<equation>A + B = 0,</equation><equation>\left\{B + C - 2 A = 0, \right.</equation><equation>2 A + C = 1.</equation>由（1）式可得 B=-A.将 B=-A 代入（2）式可得 C=3A.将 C=3A 代入（3）式可得 5A=1，即<equation>A=\frac{1}{5}.</equation>进一步可得 B=-<equation>\frac{1}{5},</equation>C<equation>=\frac{3}{5}.</equation>由此可得，<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {1}{5} \left(\frac {1}{x + 1} - \frac {x - 3}{x ^ {2} - 2 x + 2}\right).</equation>下面分别计算<equation>\int_{0}^{1}\frac{1}{x+1}\mathrm{d}x</equation>与<equation>\int_{0}^{1}\frac{x-3}{x^{2}-2x+2}\mathrm{d}x.</equation><equation>\int_ {0} ^ {1} \frac {1}{x + 1} \mathrm {d} x = \ln (x + 1) \Big | _ {0} ^ {1} = \ln 2.</equation><equation>\begin{aligned} \int_ {0} ^ {1} \frac {x - 3}{x ^ {2} - 2 x + 2} \mathrm {d} x &= \int_ {0} ^ {1} \frac {x - 1}{x ^ {2} - 2 x + 2} \mathrm {d} x - \int_ {0} ^ {1} \frac {2}{x ^ {2} - 2 x + 2} \mathrm {d} x \\ &= \frac {1}{2} \int_ {0} ^ {1} \frac {\mathrm {d} \left(x ^ {2} - 2 x + 2\right)}{x ^ {2} - 2 x + 2} - 2 \int_ {0} ^ {1} \frac {1}{1 + (x - 1) ^ {2}} \mathrm {d} x \\ &= \frac {1}{2} \ln \left(x ^ {2} - 2 x + 2\right) \left| _ {0} ^ {1} - 2 \arctan (x - 1) \right| _ {0} ^ {1} \\ &= - \frac {1}{2} \ln 2 - 2 [ 0 - \arctan (- 1) ] = - \frac {1}{2} \ln 2 - \frac {\pi}{2}. \end{aligned}</equation>因此，<equation>\int_ {0} ^ {1} \frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} \mathrm {d} x = \frac {1}{5} \left[ \ln 2 - \left(- \frac {1}{2} \ln 2 - \frac {\pi}{2}\right) \right] = \frac {3 \ln 2 + \pi}{1 0}.</equation>

---

**2023年第14题 | 填空题 | 5分**
14. 设连续函数 f(x)满足<equation>f(x+2)-f(x)=x,\int_{0}^{2} f(x)\mathrm{d} x=0</equation>，则<equation>\int_{1}^{3} f(x)\mathrm{d} x=</equation>___
**解析: **解注意到<equation>\int_{2}^{3} f(x)\mathrm{d}x=\int_{0}^{1} f(x+2)\mathrm{d}x</equation>，故由<equation>f(x+2)-f(x)=x</equation>可得，<equation>\int_{2}^{3} f(x)\mathrm{d}x-\int_{0}^{1} f(x)\mathrm{d}x=\int_{0}^{1} f(x+2)\mathrm{d}x-\int_{0}^{1} f(x)\mathrm{d}x=\int_{0}^{1} x\mathrm{d}x=\frac{1}{2}.</equation>(1)

又因为<equation>\int_{0}^{1} f(x)\mathrm{d}x+\int_{1}^{2} f(x)\mathrm{d}x=\int_{0}^{2} f(x)\mathrm{d}x=0</equation>，所以<equation>-\int_{0}^{1} f(x)\mathrm{d}x=\int_{1}^{2} f(x)\mathrm{d}x.</equation>从而由（1）式可得<equation>\int_{2}^{3} f(x)\mathrm{d}x+\int_{1}^{2} f(x)\mathrm{d}x=\frac{1}{2},</equation>即<equation>\int_{1}^{3} f(x)\mathrm{d}x=\frac{1}{2}.</equation>

---

**2022年第12题 | 填空题 | 5分**
<equation>1 2. \int_ {1} ^ {\mathrm {e} ^ {2}} \frac {\ln x}{\sqrt {x}} \mathrm {d} x = \underline {{}}</equation>
**解析: **解（法一）利用根式代换.

令<equation>t = \sqrt{x}</equation>，则<equation>x = t^{2}</equation>，<equation>\mathrm{d}x = 2t\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {1} ^ {e ^ {2}} \frac {\ln x}{\sqrt {x}} \mathrm {d} x \xlongequal {t = \sqrt {x}} \int_ {1} ^ {e} \frac {2 \ln t}{t} \cdot 2 t \mathrm {d} t &= 4 \int_ {1} ^ {e} \ln t \mathrm {d} t = 4 \left(t \ln t \Big | _ {1} ^ {e} - \int_ {1} ^ {e} t \cdot \frac {1}{t} \mathrm {d} t\right) \\ &= 4 \left[ \mathrm {e} - (\mathrm {e} - 1) \right] = 4. \end{aligned}</equation>（法二）利用分部积分法.<equation>\begin{aligned} \int_ {1} ^ {\mathrm {e} ^ {2}} \frac {\ln x}{\sqrt {x}} \mathrm {d} x &= 2 \int_ {1} ^ {\mathrm {e} ^ {2}} \ln x \mathrm {d} (\sqrt {x}) = 2 \left(\sqrt {x} \ln x \Big | _ {1} ^ {\mathrm {e} ^ {2}} - \int_ {1} ^ {\mathrm {e} ^ {2}} \sqrt {x} \cdot \frac {1}{x} \mathrm {d} x\right) = 2 \left(2 \mathrm {e} - \int_ {1} ^ {\mathrm {e} ^ {2}} \frac {1}{\sqrt {x}} \mathrm {d} x\right) \\ &= 4 \mathrm {e} - 4 \sqrt {x} \Big | _ {1} ^ {\mathrm {e} ^ {2}} = 4 \mathrm {e} - (4 \mathrm {e} - 4) = 4. \end{aligned}</equation>

---

**2015年第10题 | 填空题 | 4分**
10.<equation>\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \left(\frac {\sin x}{1 + \cos x} + | x |\right) \mathrm {d} x = \underline {{}}</equation>
**解析: **由于<equation>\frac{\sin x}{1 + \cos x}</equation>是奇函数，<equation>|x|</equation>是偶函数，故<equation>\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {\sin x}{1 + \cos x} \mathrm {d} x = 0, \quad \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} | x | \mathrm {d} x = 2 \int_ {0} ^ {\frac {\pi}{2}} x \mathrm {d} x = \frac {\pi^ {2}}{4}.</equation>因此，<equation>\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \left(\frac {\sin x}{1 + \cos x} + | x |\right) \mathrm {d} x = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {\sin x}{1 + \cos x} \mathrm {d} x + \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} | x | \mathrm {d} x = 0 + \frac {\pi^ {2}}{4} = \frac {\pi^ {2}}{4}.</equation>

---

**2014年第4题 | 选择题 | 4分 | 答案: A**
4. 若<equation>\int_{-\pi}^{\pi} \left(x-a_{1}\cos x-b_{1}\sin x\right)^{2}\mathrm{d}x=\min_{a,b\in\mathbf{R}}\left\{\int_{-\pi}^{\pi}\left(x-a\cos x-b\sin x\right)^{2}\mathrm{d}x\right\}</equation>，则<equation>a_{1}\cos x+b_{1}\sin x=</equation>(    )

A. 2sinx B. 2cosx C. 2<equation>\pi\sin x</equation>D. 2<equation>\pi\cos x</equation>
答案: A
**解析: **解（法一）<equation>\begin{aligned} \int_ {- \pi} ^ {\pi} \left(x - a \cos x - b \sin x\right) ^ {2} \mathrm {d} x &= \int_ {- \pi} ^ {\pi} \left(x ^ {2} + a ^ {2} \cos^ {2} x + b ^ {2} \sin^ {2} x - 2 a x \cos x - 2 b x \sin x + 2 a b \sin x \cos x\right) \mathrm {d} x \\ \xlongequal {\text {对称性}} 2 \int_ {0} ^ {\pi} x ^ {2} \mathrm {d} x + 2 \int_ {0} ^ {\pi} \left(a ^ {2} \cos^ {2} x + b ^ {2} \sin^ {2} x - 2 b x \sin x\right) \mathrm {d} x \\ &= \frac {2}{3} \pi^ {3} + \left(a ^ {2} + b ^ {2} - 4 b\right) \pi . \end{aligned}</equation>当 a=0时，<equation>a^{2}</equation>最小；当 b=2时，<equation>b^{2}-4b</equation>最小，从而当 a=0，b=2时，<equation>\int_{- \pi}^{\pi} \left(x-a\cos x-b\sin x\right)^{2}\mathrm{d}x</equation>最小.因此<equation>a_{1}=0,b_{1}=2</equation>，从而<equation>a_{1}\cos x+b_{1}\sin x=2\sin x</equation>，应选A.

（法二）看作二元函数的最值问题求解.

令<equation>f ( a,b)=\int_{-\pi}^{\pi} \left(x-a\cos x-b\sin x\right)^{2}\mathrm{d}x</equation>，则<equation>\frac {\partial f (a , b)}{\partial a} = \int_ {- \pi} ^ {\pi} \left[ - 2 (x - a \cos x - b \sin x) \cos x \right] \mathrm {d} x = 2 a \int_ {- \pi} ^ {\pi} \cos^ {2} x \mathrm {d} x = 2 a \pi ,</equation><equation>\frac {\partial f (a , b)}{\partial b} = \int_ {- \pi} ^ {\pi} \left[ - 2 \left(x - a \cos x - b \sin x\right) \sin x \right] \mathrm {d} x = 2 \int_ {- \pi} ^ {\pi} \left(b \sin^ {2} x - x \sin x\right) \mathrm {d} x = 2 \left(b \pi - 2 \pi\right).</equation>令<equation>\frac{\partial f(a,b)}{\partial a} = 0,\frac{\partial f(a,b)}{\partial b} = 0</equation>，解得<equation>a = 0,b = 2</equation>，从而<equation>a_1 = 0,b_1 = 2</equation>.应选A.

（法三）将选项A、B、C、D的值分别代入<equation>\int_{-\pi}^{\pi} \left(x-a\cos x-b\sin x\right)^{2}\mathrm{d}x</equation>，得到<equation>\int_ {- \pi} ^ {\pi} (x - 2 \sin x) ^ {2} \mathrm {d} x = \frac {2}{3} \pi^ {3} - 4 \pi ,</equation><equation>\int_ {- \pi} ^ {\pi} \left(x - 2 \cos x\right) ^ {2} \mathrm {d} x = \frac {2}{3} \pi^ {3} + 4 \pi ,</equation><equation>\int_ {- \pi} ^ {\pi} \left(x - 2 \pi \sin x\right) ^ {2} \mathrm {d} x = \frac {2}{3} \pi^ {3} + 4 \pi^ {2} (\pi - 2),</equation><equation>\int_ {- \pi} ^ {\pi} \left(x - 2 \pi \cos x\right) ^ {2} \mathrm {d} x = \frac {2}{3} \pi^ {3} + 4 \pi^ {3}.</equation>由于<equation>\frac{2}{3}\pi^{3}-4\pi<\frac{2}{3}\pi^{3}+4\pi<\frac{2}{3}\pi^{3}+4\pi^{2}(\pi-2)<\frac{2}{3}\pi^{3}+4\pi^{3}</equation>，故选A.

---

**2014年第10题 | 填空题 | 4分**
10. 设<equation>f(x)</equation>是周期为4的可导奇函数,且<equation>f^{\prime}(x)=2(x-1),x\in[0,2]</equation>,则<equation>f(7)=</equation>___.
**解析: **由于<equation>f ( x )</equation>是周期为4的函数，且<equation>7=2\times4-1</equation>，故<equation>f ( 7 ) = f (-1).</equation>(a)

(b)

（法一）由 f(x)为奇函数可得<equation>f(0)=0</equation>.由当<equation>x\in[0,2]</equation>时，<equation>f^{\prime}(x)=2(x-1)</equation>可得， f(x)在 [0,2]上的表达式为<equation>f (x) = \int_ {0} ^ {x} 2 (t - 1) \mathrm {d} t + f (0) = x ^ {2} - 2 x = (x - 1) ^ {2} - 1.</equation>于是<equation>f(1) = -1.</equation>由<equation>f(x)</equation>为奇函数得，<equation>f(-1) = -f(1) = 1</equation>，即<equation>f(7) = 1.</equation>（法二）由 f(x)为奇函数可知，<equation>f(x)=-f(-x).</equation>在等式两端求导得<equation>f^{\prime}(x)=f^{\prime}(-x),</equation>从而<equation>f^{\prime}(x)</equation>为偶函数，<equation>f^{\prime}(x)</equation>的图像关于y轴对称.在[0，2]上，<equation>f^{\prime}(x)=2(x-1),</equation>为一条过点（0，-2）和点（1，0）的直线。由此可知，在[-2，0]上，<equation>y=f^{\prime}(x)</equation>为过点（0，-2）和点（-1，0）的直线，可求得<equation>f^{\prime}(x)=-2(x+1).</equation>从而，<equation>f(x)</equation>在[-2，0]上为<equation>f (x) = \int_ {0} ^ {x} - 2 (t + 1) \mathrm {d} t + f (0) = - x ^ {2} - 2 x = - (x + 1) ^ {2} + 1.</equation>因此，<equation>f(-1)=1</equation>，即<equation>f(7)=1.</equation>

---

**2013年第15题 | 解答题 | 10分**
15. (本题满分10分)

计算<equation>\int_ {0} ^ {1} \frac {f (x)}{\sqrt {x}} \mathrm {d} x, \text {其 中} f (x) = \int_ {1} ^ {x} \frac {\ln (t + 1)}{t} \mathrm {d} t.</equation>
**解析: **解（法一）由题设知，<equation>f^{\prime}(x) = \frac{\ln(x + 1)}{x}, x\in(0,1],</equation>且<equation>f(1)=0</equation>，于是<equation>\begin{aligned} \int_ {0} ^ {1} \frac {f (x)}{\sqrt {x}} \mathrm {d} x &= 2 \int_ {0} ^ {1} f (x) \mathrm {d} (\sqrt {x}) = 2 \left[ \sqrt {x} f (x) \left| _ {0} ^ {1} - \int_ {0} ^ {1} \sqrt {x} f ^ {\prime} (x) \mathrm {d} x \right] \right. \\ &= 0 - 2 \int_ {0} ^ {1} \sqrt {x} \cdot \frac {\ln (x + 1)}{x} \mathrm {d} x = - 2 \int_ {0} ^ {1} \frac {\ln (x + 1)}{\sqrt {x}} \mathrm {d} x \\ &= - 4 \int_ {0} ^ {1} \ln (x + 1) \mathrm {d} (\sqrt {x}) \\ &= - 4 \left[ \sqrt {x} \ln (x + 1) \left| _ {0} ^ {1} - \int_ {0} ^ {1} \frac {\sqrt {x}}{x + 1} \mathrm {d} x \right] \right. \\ \underline {{= - 4}} \left[ \sqrt {x} \ln (x + 1) \left| _ {0} ^ {1} - \int_ {0} ^ {1} \frac {\sqrt {x}}{x + 1} \mathrm {d} x \right] \right. \\ &= - 4 \ln 2 + 4 \int_ {0} ^ {1} \frac {t}{t ^ {2} + 1} \cdot 2 t \mathrm {d} t \\ &= - 4 \ln 2 + 8 \int_ {0} ^ {1} \left(1 - \frac {1}{t ^ {2} + 1}\right) \mathrm {d} t \\ &= - 4 \ln 2 + 8 \left(t - \arctan t\right) \Bigg | _ {0} ^ {1} \\ &= - 4 \ln 2 + 8 - 2 \pi . \end{aligned}</equation><equation>\begin{array}{l} \frac {\text {交换 积 分}}{\text {次 序}} - \int_ {0} ^ {1} \mathrm {d} t \int_ {0} ^ {t} \frac {\ln (t + 1)}{t} \cdot \frac {1}{\sqrt {x}} \mathrm {d} x = - 2 \int_ {0} ^ {1} \frac {\ln (t + 1)}{\sqrt {t}} \mathrm {d} t \\ \underline {{\text {同 法 一}}} - 4 \ln 2 + 8 - 2 \pi . \\ \end{array}</equation>

---

**2012年第10题 | 填空题 | 4分**
<equation>1 0. \int_ {0} ^ {2} x \sqrt {2 x - x ^ {2}} \mathrm {d} x = \underline {{}}</equation>
**解析: **解<equation>\sqrt{2 x-x^{2}}=\sqrt{1-(x-1)^{2}}.</equation>令 t=x-1，则有<equation>\begin{aligned} \int_ {0} ^ {2} x \sqrt {2 x - x ^ {2}} \mathrm {d} x &= \int_ {- 1} ^ {1} (t + 1) \sqrt {1 - t ^ {2}} \mathrm {d} t = \int_ {- 1} ^ {1} t \sqrt {1 - t ^ {2}} \mathrm {d} t + \int_ {- 1} ^ {1} \sqrt {1 - t ^ {2}} \mathrm {d} t \\ \underline {{\text {对称性}}} 0 + 2 \int_ {0} ^ {1} \sqrt {1 - t ^ {2}} \mathrm {d} t \\ \underline {{\underline {{t = \sin \theta}}}} 2 \int_ {0} ^ {\frac {\pi}{2}} \cos^ {2} \theta \mathrm {d} \theta &= \int_ {0} ^ {\frac {\pi}{2}} (1 + \cos 2 \theta) \mathrm {d} \theta = \frac {\pi}{2}. \end{aligned}</equation>

---

**2010年第10题 | 填空题 | 4分**
10.
**解析: **<equation>\begin{aligned} \int_ {0} ^ {\pi^ {2}} \sqrt {x} \cos \sqrt {x} \mathrm {d} x \stackrel {t = \sqrt {x}} {=} \int_ {0} ^ {\pi} t \cos t \mathrm {d} \left(t ^ {2}\right) \\ &= \int_ {0} ^ {\pi} 2 t ^ {2} \cos t \mathrm {d} t = \int_ {0} ^ {\pi} 2 t ^ {2} \mathrm {d} (\sin t) \\ \underline {{\mathrm {分 部 积 分}}} (\sin t \cdot 2 t ^ {2}) \left| _ {0} ^ {\pi} - \int_ {0} ^ {\pi} 4 t \sin t \mathrm {d} t &= \int_ {0} ^ {\pi} 4 t \mathrm {d} (\cos t) \right. \\ \underline {{\mathrm {分 部 积 分}}} (\cos t \cdot 4 t) \left| _ {0} ^ {\pi} - \int_ {0} ^ {\pi} 4 \cos t \mathrm {d} t &= - 4 \pi . \right. \end{aligned}</equation>

---


