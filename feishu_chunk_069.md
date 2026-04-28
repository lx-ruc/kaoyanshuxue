#### 确定极限中的参数

**2024年第11题 | 填空题 | 5分**
<equation>. \mathrm {若} \lim _ {x \rightarrow 0} \frac {\left(1 + a x ^ {2}\right) ^ {\sin x} - 1}{x ^ {3}} = 6, \mathrm {则} a = \underline {{}}</equation>
**答案: **## a=6.
**解析: **<equation>\begin{aligned} 6 &= \lim _ {x \rightarrow 0} \frac {\left(1 + a x ^ {2}\right) ^ {\sin x} - 1}{x ^ {3}} = \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {\sin x \ln \left(1 + a x ^ {2}\right)} - 1}{x ^ {3}} = \lim _ {x \rightarrow 0} \frac {\sin x \ln \left(1 + a x ^ {2}\right)}{x ^ {3}} \\ &= \lim _ {x \rightarrow 0} \frac {x \cdot a x ^ {2}}{x ^ {3}} = a. \end{aligned}</equation>因此，<equation>a=6.</equation>

---

**2023年第11题 | 填空题 | 5分**
11. 当<equation>x \to0</equation>时，函数<equation>f(x)=ax+bx^{2}+\ln(1+x)</equation>与<equation>g(x)=\mathrm{e}^{x^{2}}-\cos x</equation>是等价无穷小，则 ab=___
**答案: **<equation>- 2.</equation>
**解析: **解分别写出<equation>f ( x )</equation>与<equation>g ( x )</equation>在<equation>x=0</equation>处的二阶泰勒公式.当<equation>x\to0</equation>时，<equation>f (x) = a x + b x ^ {2} + x - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right) = (a + 1) x + \left(b - \frac {1}{2}\right) x ^ {2} + o \left(x ^ {2}\right),</equation><equation>g (x) = 1 + x ^ {2} + o \left(x ^ {2}\right) - \left[ 1 - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right) \right] = \frac {3}{2} x ^ {2} + o \left(x ^ {2}\right).</equation>由于<equation>f(x)</equation>与<equation>g(x)</equation>是<equation>x\to 0</equation>时的等价无穷小，故<equation>1 = \lim _ {x \rightarrow 0} \frac {f (x)}{g (x)} = \lim _ {x \rightarrow 0} \frac {(a + 1) x + \left(b - \frac {1}{2}\right) x ^ {2} + o \left(x ^ {2}\right)}{\frac {3}{2} x ^ {2} + o \left(x ^ {2}\right)}.</equation>由（1）式成立可得<equation>a+1=0,b-\frac{1}{2}=\frac{3}{2}.</equation>解得<equation>a=-1,b=2.</equation>因此，<equation>ab=-2.</equation>

---

**2019年第1题 | 选择题 | 4分 | 答案: C**
1. 当 x→0时，若 x-tanx与<equation>x^{k}</equation>是同阶无穷小，则 k=（    ）

A.1 B.2 C.3 D.4
答案: C
**解析: **解 首先，由于当<equation>x\to0</equation>时，<equation>x-\tan x\to0</equation>，而<equation>\lim_{x\to0}\frac{x-\tan x}{x^{k}}</equation>为非零常数，故 k > 0.下面用两种方法讨论<equation>\lim_{x\to0}\frac{x-\tan x}{x^{k}}.</equation>（法一）由于<equation>\tan x=x+\frac{x^{3}}{3}+o\left(x^{3}\right)</equation>，故<equation>\lim _ {x \rightarrow 0} \frac {x - \tan x}{x ^ {k}} = \lim _ {x \rightarrow 0} \frac {- \frac {x ^ {3}}{3} + o \left(x ^ {3}\right)}{x ^ {k}}.</equation>当 k > 3时，该极限为<equation>\infty</equation>；当0 < k < 3时，该极限为0；当 k=3时，该极限为<equation>-\frac{1}{3}.</equation>于是，<equation>x-\tan x</equation>与<equation>x^{3}</equation>是同阶无穷小，k=3.

因此，应选C.

（法二）利用洛必达法则讨论<equation>\lim_{x\to 0}\frac{x - \tan x}{x^k}</equation>.<equation>\lim _ {x \rightarrow 0} \frac {x - \tan x}{x ^ {k}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - \sec^ {2} x}{k x ^ {k - 1}} = \lim _ {x \rightarrow 0} \frac {- \tan^ {2} x}{k x ^ {k - 1}} \xlongequal {\tan x \sim x} \lim _ {x \rightarrow 0} \frac {- x ^ {2}}{k x ^ {k - 1}}.</equation>当 k > 3时，该极限为<equation>\infty</equation>；当0 < k < 3时，该极限为0；当 k=3时，该极限为<equation>-\frac{1}{3}.</equation>于是，<equation>x-\tan x</equation>与<equation>x^{3}</equation>是同阶无穷小， k=3.

因此，应选C.

---

**2018年第9题 | 填空题 | 4分**
9. 若<equation>\lim_{x\rightarrow 0}\left(\frac{1-\tan x}{1+\tan x}\right)^{\frac{1}{\sin k x}}=\mathrm{e}</equation>，则 k= ___
**解析: **解（法一）对原极限进行恒等变形，再凑重要极限.<equation>\lim _ {x \rightarrow 0} \left(\frac {1 - \tan x}{1 + \tan x}\right) ^ {\frac {1}{\sin k x}} = \lim _ {x \rightarrow 0} \left(1 - \frac {2 \tan x}{1 + \tan x}\right) ^ {\frac {1}{\sin k x}} = \lim _ {x \rightarrow 0} \left(1 - \frac {2 \tan x}{1 + \tan x}\right) ^ {\frac {1 + \tan x}{- 2 \tan x} \cdot \frac {- 2 \tan x}{1 + \tan x} \cdot \frac {1}{\sin k x}}.</equation>因为<equation>\lim _ {x \rightarrow 0} \left(\frac {- 2 \tan x}{1 + \tan x} \cdot \frac {1}{\sin k x}\right) = \lim _ {x \rightarrow 0} \frac {- 2 \tan x}{\sin k x} \frac {\tan x \sim x}{\sin k x \sim k x} \lim _ {x \rightarrow 0} \frac {- 2 x}{k x} = - \frac {2}{k},</equation>所以原极限<equation>= \mathrm{e}^{-\frac{2}{k}} = \mathrm{e}.</equation>因此，<equation>-\frac{2}{k} = 1,k = -2.</equation>（法二）取对数，再求极限.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \left(\frac {1 - \tan x}{1 + \tan x}\right) ^ {\frac {1}{\sin k x}} &= \lim _ {x \rightarrow 0} \mathrm {e} ^ {\frac {1}{\sin k x} \cdot \ln \left(\frac {1 - \tan x}{1 + \tan x}\right)} = \mathrm {e} ^ {\lim _ {x \rightarrow 0} \frac {1}{\sin k x} \cdot \ln \left(1 - \frac {2 \tan x}{1 + \tan x}\right)} \\ \frac {\ln \left(1 - \frac {2 \tan x}{1 + \tan x}\right) \sim \frac {- 2 \tan x}{1 + \tan x}}{\frac {\tan x \sim x}{\sin k x \sim k x}} \mathrm {e} ^ {\lim _ {x \rightarrow 0} \frac {- 2 x}{k x}} &= \mathrm {e} ^ {- \frac {2}{k}}. \end{aligned}</equation>由于原极限<equation>= \mathrm{e}</equation>，故<equation>-\frac{2}{k} = 1</equation>，即<equation>k = -2.</equation>

---

**2015年第15题 | 解答题 | 10分**
15. (本题满分10分)

设函数<equation>f(x)=x+a\ln(1+x)+bx\sin x,g(x)=kx^{3}.</equation>若 f(x)与 g(x)在<equation>x\rightarrow0</equation>时是等价无穷小，求 a,b,k的值.
**解析: **由于 g(x）中 x的次数为3，故可考虑写出 f(x)在 x=0处的3阶泰勒公式.

由<equation>\ln (1 + x) = x - \frac {x ^ {2}}{2} + \frac {x ^ {3}}{3} + o \left(x ^ {3}\right), \quad \sin x = x - \frac {x ^ {3}}{3 !} + o \left(x ^ {3}\right),</equation>可得<equation>f (x) = x + a x - \frac {a x ^ {2}}{2} + \frac {a x ^ {3}}{3} + b x ^ {2} + o \left(x ^ {3}\right) = (a + 1) x + \left(b - \frac {a}{2}\right) x ^ {2} + \frac {a}{3} x ^ {3} + o \left(x ^ {3}\right).</equation>记<equation>I=\lim_{x\to 0}\frac{f(x)}{g(x)}=\lim_{x\to 0}\frac{(a+1)x+\left(b-\frac{a}{2}\right)x^{2}+\frac{a}{3}x^{3}+o\left(x^{3}\right)}{kx^{3}}.</equation>由等价无穷小量的定义知<equation>I=1.</equation>首先，<equation>k\neq 0</equation>当 k≠0时，若 I存在，则必有<equation>\left\{\begin{array}{l l}a+1=0,\\ b-\frac{a}{2}=0,\end{array}\right.</equation>否则<equation>I=\infty.</equation>解得 a=-1，b=-<equation>\frac{1}{2}.</equation>又因为 I=1，所以<equation>\frac{a}{3}=k,k=-\frac{1}{3}.</equation>综上所述，<equation>a = -1</equation>，<equation>b = -\frac{1}{2}</equation>，<equation>k = -\frac{1}{3}</equation>

---

**2013年第1题 | 选择题 | 4分 | 答案: D**
1. 已知极限<equation>\lim_{x\rightarrow 0}\frac{x-\arctan x}{x^{k}}=c</equation>，其中 k,c为常数，且<equation>c\neq 0</equation>，则（    )

A. k=2, c=-<equation>\frac{1}{2}</equation>B. k=2, c=<equation>\frac{1}{2}</equation>C. k=3, c=-<equation>\frac{1}{3}</equation>D. k=3, c=<equation>\frac{1}{3}</equation>
答案: D
**解析: **解（法一）当<equation>x\to0</equation>时，<equation>\arctan x=x-\frac{x^{3}}{3}+o\left(x^{3}\right)</equation>，于是<equation>0 \neq c = \lim _ {x \rightarrow 0} \frac {x - \arctan x}{x ^ {k}} = \lim _ {x \rightarrow 0} \frac {\frac {x ^ {3}}{3} + o \left(x ^ {3}\right)}{x ^ {k}}.</equation>当<equation>k > 3</equation>时，<equation>\lim_{x\to 0}\frac{\frac{x^3}{3} + o(x^3)}{x^k} = \lim_{x\to 0}\frac{\frac{1}{3} + \frac{o(x^3)}{x^3}}{x^{k - 3}} = \lim_{x\to 0}\frac{\frac{1}{3}}{x^{k - 3}} = \infty .</equation>当 k < 3时，<equation>\lim_{x\to 0}\frac{\frac{x^{3}}{3}+o\left(x^{3}\right)}{x^{k}}=\lim_{x\to 0}\left[\frac{x^{3-k}}{3}+\frac{o\left(x^{3}\right)}{x^{3}}\cdot x^{3-k}\right]=\lim_{x\to 0}\frac{x^{3-k}}{3}=0.</equation>因此，k=3，此时<equation>c=\frac{1}{3}</equation>应选D.

（法二）由于<equation>c\neq 0</equation>且<equation>\lim_{x\to 0} \left(x-\arctan x\right)=0</equation>，故<equation>\lim_{x\to 0} x^{k}=0</equation>，从而 k>0，于是题设中极限为<equation>\frac{0}{0}</equation>型.根据洛必达法则，<equation>\lim _ {x \rightarrow 0} \frac {x - \arctan x}{x ^ {k}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - \frac {1}{1 + x ^ {2}}}{k x ^ {k - 1}} = \lim _ {x \rightarrow 0} \left(\frac {1}{1 + x ^ {2}} \cdot \frac {x ^ {2}}{k x ^ {k - 1}}\right) = \lim _ {x \rightarrow 0} \frac {1}{k x ^ {k - 3}} = c.</equation>又<equation>c\neq 0</equation>，故<equation>k=3</equation>，从而<equation>c=\frac{1}{3}</equation>应选D.

---

**2009年第1题 | 选择题 | 4分 | 答案: A**
1. 当<equation>x\to0</equation>时，<equation>f(x)=x-\sin ax</equation>与<equation>g(x)=x^{2}\ln(1-bx)</equation>是等价无穷小量，则（    )

A. a=1,b=-<equation>\frac{1}{6}</equation>B. a=1,b=<equation>\frac{1}{6}</equation>C. a=-1,b=-<equation>\frac{1}{6}</equation>D. a=-1,b=<equation>\frac{1}{6}</equation>
答案: A
**解析: **由于<equation>x\to0</equation>时，<equation>f(x)</equation>与<equation>g(x)</equation>是等价无穷小量，故<equation>\begin{aligned} 1 &= \lim _ {x \rightarrow 0} \frac {f (x)}{g (x)} = \lim _ {x \rightarrow 0} \frac {x - \sin a x}{x ^ {2} \ln (1 - b x)} \xlongequal {\ln (1 - b x) \sim (- b x)} \lim _ {x \rightarrow 0} \frac {x - \sin a x}{- b x ^ {3}} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - a \cos a x}{- 3 b x ^ {2}} &= I _ {1}. \end{aligned}</equation>由于<equation>\lim_{x\to 0}(-3bx^2) = 0</equation>，故若<equation>I_{1}</equation>存在，则<equation>\lim_{x\to 0}(1 - a\cos ax) = 0</equation>，从而<equation>a = 1.</equation>代人 a=1，得<equation>I _ {1} = \lim _ {x \rightarrow 0} \frac {1 - \cos x}{- 3 b x ^ {2}} \xlongequal {1 - \cos x \sim \frac {x ^ {2}}{2}} \lim _ {x \rightarrow 0} \frac {\frac {x ^ {2}}{2}}{- 3 b x ^ {2}} = - \frac {1}{6 b}.</equation>当<equation>b = -\frac{1}{6}</equation>时，<equation>I_{1}</equation>存在且等于1.

因此，当<equation>a = 1,b = -\frac{1}{6}</equation>时，<equation>\lim_{x\to 0}\frac{f(x)}{g(x)} = 1,f(x)</equation>与<equation>g(x)</equation>是<equation>x\to 0</equation>时的等价无穷小量.应选A.

---


