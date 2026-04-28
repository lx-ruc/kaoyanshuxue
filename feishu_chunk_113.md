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


