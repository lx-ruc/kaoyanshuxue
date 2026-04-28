# 数学二

## 高等数学

### 函数、极限、连续

#### 确定极限中的参数

**2023年第11题 | 填空题 | 5分**

11. 当<equation>x \to0</equation>时，函数<equation>f(x)=ax+bx^{2}+\ln(1+x)</equation>与<equation>g(x)=\mathrm{e}^{x^{2}}-\cos x</equation>是等价无穷小，则 ab=___

**答案:**-2.

**解析:**分别写出 f（x）与 g（x）在 x=0处的二阶泰勒公式.当 x→0时，<equation>f (x) = a x + b x ^ {2} + x - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right) = (a + 1) x + \left(b - \frac {1}{2}\right) x ^ {2} + o \left(x ^ {2}\right),</equation><equation>g (x) = 1 + x ^ {2} + o \left(x ^ {2}\right) - \left[ 1 - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right) \right] = \frac {3}{2} x ^ {2} + o \left(x ^ {2}\right).</equation>由于 f(x)与 g(x）是<equation>x\to0</equation>时的等价无穷小，故<equation>1 = \lim _ {x \rightarrow 0} \frac {f (x)}{g (x)} = \lim _ {x \rightarrow 0} \frac {(a + 1) x + \left(b - \frac {1}{2}\right) x ^ {2} + o \left(x ^ {2}\right)}{\frac {3}{2} x ^ {2} + o \left(x ^ {2}\right)}.</equation>由（1）式成立可得 a+1=0,b<equation>- \frac{1}{2}=\frac{3}{2}</equation>.解得 a=-1,b=2.因此，ab=-2.

---

**2019年第1题 | 选择题 | 4分 | 答案: C**

1. 当 x→0时，若 x-tanx与<equation>x^{k}</equation>是同阶无穷小，则 k=（    ）

A.1 B.2 C.3 D.4

答案: C

**解析:**解 首先，由于当 x→0时，<equation>x-\tan x\to 0</equation>，而<equation>\lim_{x\to 0}\frac{x-\tan x}{x^{k}}</equation>为非零常数，故 k > 0.下面用两种方法讨论<equation>\lim_{x\to 0}\frac{x-\tan x}{x^{k}}.</equation>（法一）由于<equation>\tan x=x+\frac{x^{3}}{3}+o\left(x^{3}\right)</equation>，故<equation>\lim _ {x \rightarrow 0} \frac {x - \tan x}{x ^ {k}} = \lim _ {x \rightarrow 0} \frac {- \frac {x ^ {3}}{3} + o \left(x ^ {3}\right)}{x ^ {k}}.</equation>当 k > 3时，该极限为<equation>\infty</equation>；当 0 < k < 3时，该极限为0；当 k=3时，该极限为<equation>-\frac{1}{3}.</equation>于是，<equation>x-\tan x</equation>与<equation>x^{3}</equation>是同阶无穷小，k=3.

因此，应选C.

（法二）利用洛必达法则讨论<equation>\lim_{x\to 0}\frac{x-\tan x}{x^{k}}.</equation><equation>\lim _ {x \rightarrow 0} \frac {x - \tan x}{x ^ {k}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - \sec^ {2} x}{k x ^ {k - 1}} = \lim _ {x \rightarrow 0} \frac {- \tan^ {2} x}{k x ^ {k - 1}} \xlongequal {\tan x \sim x} \lim _ {x \rightarrow 0} \frac {- x ^ {2}}{k x ^ {k - 1}}.</equation>当 k > 3时，该极限为<equation>\infty</equation>；当 0 < k < 3时，该极限为0；当 k=3时，该极限为<equation>-\frac{1}{3}.</equation>于是，<equation>x-\tan x</equation>与<equation>x^{3}</equation>是同阶无穷小， k=3.

因此，应选C.

---

**2018年第1题 | 选择题 | 4分 | 答案: B**

1. 若<equation>\lim_{x\rightarrow 0} \left( \mathrm{e}^{x}+a x^{2}+b x\right)^{\frac{1}{x^{2}}}=1</equation>，则（    ）

A. a<equation>=\frac{1}{2},</equation>b<equation>=-1</equation>B. a<equation>=-\frac{1}{2},</equation>b<equation>=-1</equation>C. a<equation>=\frac{1}{2},</equation>b<equation>=1</equation>D. a<equation>=-\frac{1}{2},</equation>b<equation>=1</equation>

答案: B

**解析:**解 记<equation>I = \lim_{x\to 0}\left(\mathrm{e}^{x} + ax^{2} + bx\right)^{\frac{1}{x^{2}}}</equation>.

对原极限进行恒等变形，再凑重要极限.<equation>\begin{aligned} I &= \lim _ {x \rightarrow 0} \left(1 + \mathrm {e} ^ {x} - 1 + a x ^ {2} + b x\right) ^ {\frac {1}{x ^ {2}}} = \lim _ {x \rightarrow 0} \left(1 + \mathrm {e} ^ {x} - 1 + a x ^ {2} + b x\right) ^ {\frac {1}{\mathrm {e} ^ {x} - 1 + a x ^ {2} + b x}} \cdot \frac {\mathrm {e} ^ {x} - 1 + a x ^ {2} + b x}{x ^ {2}} \\ &= \mathrm {e} ^ {\lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x} - 1 + a x ^ {2} + b x}{x ^ {2}}}. \end{aligned}</equation>由于<equation>I = 1</equation>，故<equation>\lim_{x\to 0}\frac{\mathrm{e}^{x}-1+ax^{2}+bx}{x^{2}}=0.</equation>又因为<equation>\mathrm{e}^{x}</equation>在 x=0处的二阶泰勒公式为<equation>\mathrm{e}^{x}=1+x+\frac{x^{2}}{2}+o\left(x^{2}\right)</equation>，所以<equation>\lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x} - 1 + a x ^ {2} + b x}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {(1 + b) x + \left(\frac {1}{2} + a\right) x ^ {2} + o \left(x ^ {2}\right)}{x ^ {2}}.</equation>当且仅当<equation>1 + b = 0, \frac{1}{2} + a = 0</equation>，即<equation>b = -1</equation>，<equation>a = -\frac{1}{2}</equation>时，<equation>\lim_{x\to 0}\frac{\mathrm{e}^{x} - 1 + ax^{2} + bx}{x^{2}} = 0.</equation>因此，<equation>a=-\frac{1}{2}</equation><equation>b=-1</equation>应选B.

---

**2015年第15题 | 解答题 | 10分**

15. (本题满分10分）

设函数<equation>f(x)=x+a\ln(1+x)+bx\sin x,g(x)=kx^{3}.</equation>若 f(x)与 g(x)在<equation>x\rightarrow0</equation>时是等价无穷小，求 a,b,k的值.

**答案:**<equation>(1 5) a = - 1, b = - \frac {1}{2}, k = - \frac {1}{3}.</equation>

**解析:**解 由于 g(x）中 x的次数为3，故可考虑写出 f(x)在 x=0处的3阶泰勒公式.<equation>\ln (1 + x) = x - \frac {x ^ {2}}{2} + \frac {x ^ {3}}{3} + o \left(x ^ {3}\right), \sin x = x - \frac {x ^ {3}}{3 !} + o \left(x ^ {3}\right),</equation><equation>f (x) = x + a x - \frac {a x ^ {2}}{2} + \frac {a x ^ {3}}{3} + b x ^ {2} + o \left(x ^ {3}\right) = (a + 1) x + \left(b - \frac {a}{2}\right) x ^ {2} + \frac {a}{3} x ^ {3} + o \left(x ^ {3}\right).</equation>记<equation>I=\lim_{x\to 0}\frac{f(x)}{g(x)}=\lim_{x\to 0}\frac{(a+1)x+\left(b-\frac{a}{2}\right)x^{2}+\frac{a}{3}x^{3}+o\left(x^{3}\right)}{kx^{3}}.</equation>由等价无穷小量的定义知<equation>I=1.</equation>首先，<equation>k\neq 0.</equation>当<equation>k\neq 0</equation>时，若I存在，则必有<equation>\left\{ \begin{array}{l l} a+1=0, \\ b-\frac{a}{2}=0, \end{array} \right.</equation>否则<equation>I=\infty.</equation>解得<equation>a=-1, b=-\frac{1}{2}.</equation>又因为<equation>I=1</equation>所以<equation>\frac{a}{3}=k,k=-\frac{1}{3}.</equation>综上所述，<equation>a=-1</equation><equation>b=-\frac{1}{2}</equation><equation>k=-\frac{1}{3}.</equation>

---

**2014年第1题 | 选择题 | 4分 | 答案: B**

1. 当<equation>x \to 0^{+}</equation>时，若<equation>\ln^{\alpha}(1+2x),(1-\cos x)^{\frac{1}{\alpha}}</equation>均是比 x高阶的无穷小量，则<equation>\alpha</equation>的取值范围是（    ）

A. (2,+<equation>\infty</equation>) B. (1,2) C.<equation>\left(\frac{1}{2},1\right)</equation>D.<equation>\left(0,\frac{1}{2}\right)</equation>

答案: B

**解析:**解 当<equation>x\to0^{+}</equation>时，<equation>\ln(1+2x)\sim2x,1-\cos x\sim\frac{1}{2}x^{2}.</equation>若<equation>\ln^{\alpha}(1+2x)</equation>和<equation>(1-\cos x)^{\frac{1}{\alpha}}</equation>均为比x高阶的无穷小量，则<equation>(2x)^{\alpha}</equation>与<equation>\left(\frac{1}{2} x^{2}\right)^{\frac{1}{\alpha}}</equation>也均为比x高阶的无穷小量，即<equation>\left\{\begin{array}{l l} {\alpha>1,} \\ {\frac{2}{\alpha}>1,} \end{array} \right.</equation>解得<equation>1<\alpha<2.</equation>应选B.

---

**2013年第15题 | 解答题 | 10分**

15. (本题满分10分)

当<equation>x\to0</equation>时，<equation>1-\cos x\cdot\cos 2x\cdot\cos 3x</equation>与<equation>ax^{n}</equation>为等价无穷小量，求 n与 a的值.

**答案:**(15) n=2, a=7.

**解析:**解记<equation>I=\lim_{x\to 0}\frac{1-\cos x\cos 2x\cos 3x}{a x^{n}}.</equation>由题设，<equation>I=1.</equation>（法一）分别考虑<equation>\cos x,\cos 2x,\cos 3x</equation>的二阶泰勒公式，<equation>\cos x = 1 - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right),</equation><equation>\cos 2 x = 1 - \frac {1}{2} (2 x) ^ {2} + o \left(\left(2 x\right) ^ {2}\right) = 1 - 2 x ^ {2} + o \left(x ^ {2}\right),</equation><equation>\cos 3 x = 1 - \frac {1}{2} (3 x) ^ {2} + o \left((3 x) ^ {2}\right) = 1 - \frac {9}{2} x ^ {2} + o \left(x ^ {2}\right).</equation>代人I，得<equation>\begin{aligned} I &= \lim _ {x \rightarrow 0} \frac {1 - \left[ 1 - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right)\right]\left[ 1 - 2 x ^ {2} + o \left(x ^ {2}\right)\right]\left[ 1 - \frac {9}{2} x ^ {2} + o \left(x ^ {2}\right)\right]}{a x ^ {n}} \\ &= \lim _ {x \rightarrow 0} \frac {\frac {1}{2} x ^ {2} + 2 x ^ {2} + \frac {9}{2} x ^ {2} + o \left(x ^ {2}\right)}{a x ^ {n}} = \lim _ {x \rightarrow 0} \frac {7 x ^ {2} + o \left(x ^ {2}\right)}{a x ^ {n}}. \end{aligned}</equation>由于<equation>\lim _ {x \rightarrow 0} \frac {7 x ^ {2} + o \left(x ^ {2}\right)}{a x ^ {n}} = \frac {7}{a} \lim _ {x \rightarrow 0} \frac {x ^ {2}}{x ^ {n}} \left[ 1 + \frac {o \left(x ^ {2}\right)}{7 x ^ {2}} \right] = \frac {7}{a} \lim _ {x \rightarrow 0} \frac {x ^ {2}}{x ^ {n}},</equation>故当 n > 2时，<equation>\lim_{x\rightarrow 0}\frac{7x^{2}+o\left(x^{2}\right)}{ax^{n}}=\infty</equation>；当 n < 2时，<equation>\lim_{x\rightarrow 0}\frac{7x^{2}+o\left(x^{2}\right)}{ax^{n}}=0</equation>；而当 n = 2时，<equation>\lim_{x\rightarrow 0}\frac{7x^{2}+o\left(x^{2}\right)}{ax^{2}}=</equation><equation>\frac{7}{a}</equation>.因此，由 I = 1得，<equation>\frac{7}{a}=1,a=7.</equation>综上所述，<equation>n=2</equation><equation>a=7.</equation>（法二）我们先利用三角函数的积化和差公式将<equation>\cos x\cos 2x\cos 3x</equation>作恒等变形，然后再利用洛必达法则来计算 I.<equation>\begin{aligned} \cos x \cos 2 x \cos 3 x &= \frac {1}{2} (\cos 4 x + \cos 2 x) \cos 2 x = \frac {1}{4} (\cos 6 x + \cos 2 x) + \frac {1}{4} \cos 4 x + \frac {1}{4} \\ &= \frac {1}{4} (1 + \cos 2 x + \cos 4 x + \cos 6 x). \end{aligned}</equation>从而，<equation>\begin{aligned} I &= \lim _ {x \rightarrow 0} \frac {\frac {3}{4} - \frac {1}{4} (\cos 2 x + \cos 4 x + \cos 6 x)}{a x ^ {n}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\frac {1}{4} (2 \sin 2 x + 4 \sin 4 x + 6 \sin 6 x)}{n a x ^ {n - 1}} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\cos 2 x + 4 \cos 4 x + 9 \cos 6 x}{n (n - 1) a x ^ {n - 2}} &= \lim _ {x \rightarrow 0} \frac {1 4}{n (n - 1) a x ^ {n - 2}}. \end{aligned}</equation>由上可以看出，若 I存在且等于1，则 n-2=0.否则当 n-2<0时， I=0.当 n-2>0时，<equation>I=\infty</equation>当 n=2时，<equation>I=\frac{14}{2a}=1</equation>a=7.

综上所述，<equation>n=2</equation><equation>a=7.</equation>（法三）使用添项、减项的技巧对<equation>I</equation>进行恒等变形<equation>\begin{aligned} I &= \lim _ {x \rightarrow 0} \frac {1 - \cos x + \cos x - \cos x \cos 2 x + \cos x \cos 2 x - \cos x \cos 2 x \cos 3 x}{a x ^ {n}} \\ &= \lim _ {x \rightarrow 0} \left[ \frac {1 - \cos x}{a x ^ {n}} + \frac {\cos x (1 - \cos 2 x)}{a x ^ {n}} + \frac {\cos x \cos 2 x (1 - \cos 3 x)}{a x ^ {n}} \right]. \end{aligned}</equation>分别考虑<equation>\lim_{x\to 0}\frac{1 - \cos x}{ax^n},\lim_{x\to 0}\frac{\cos x(1 - \cos 2x)}{ax^n},\lim_{x\to 0}\frac{\cos x\cos 2x(1 - \cos 3x)}{ax^n}.</equation>由于当<equation>x\to0</equation>时，<equation>\cos x\to1,1-\cos x\sim\frac{x^{2}}{2}</equation>，故这三个极限均仅当 n=2时存在且不为零.当 n>2时，极限为<equation>\infty</equation>；当 n<2时，极限为零.<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {1 - \cos x}{a x ^ {2}} \xlongequal {\frac {1 - \cos x \sim \frac {x ^ {2}}{2}}{2}} \frac {1}{2 a}, \quad \lim _ {x \rightarrow 0} \frac {\cos x (1 - \cos 2 x)}{a x ^ {2}} \xlongequal {\frac {1 - \cos 2 x \sim \frac {(2 x) ^ {2}}{2}}{2}} \frac {2}{a}, \\ \lim _ {x \rightarrow 0} \frac {\cos x \cos 2 x (1 - \cos 3 x)}{a x ^ {2}} \xlongequal {\frac {1 - \cos 3 x \sim \frac {(3 x) ^ {2}}{2}}{2}} \frac {9}{2 a}. \\ \end{array}</equation><equation>I = \frac {1}{2 a} + \frac {2}{a} + \frac {9}{2 a} = \frac {7}{a} = 1.</equation>因此，<equation>n = 2</equation>，<equation>a = 7</equation>

---

**2012年第15题 | 解答题 | 10分**

15. (本题满分10分）

已知函数<equation>f ( x )=\frac{1+x}{\sin x}-\frac{1}{x}</equation>，记 a =<equation>\lim_{x\to 0}f(x).</equation>I. 求 a的值；

II. 若当<equation>x\to0</equation>时，<equation>f(x)-a</equation>与<equation>x^{k}</equation>是同阶无穷小量，求常数 k的值.

**答案:**(15) ( I ) a = 1 ;

( II ) k = 1.

**解析:**解（I）<equation>\lim_{x\to 0}f(x)</equation>为<equation>\infty -\infty</equation>型未定式，可通分写成<equation>\frac{0}{0}</equation>型未定式.<equation>a = \lim _ {x \rightarrow 0} \left(\frac {1 + x}{\sin x} - \frac {1}{x}\right) = \lim _ {x \rightarrow 0} \frac {x ^ {2} + x - \sin x}{x \sin x} \xlongequal {\sin x \sim x} \lim _ {x \rightarrow 0} \frac {x ^ {2} + x - \sin x}{x ^ {2}}.</equation>考虑<equation>\lim_{x\to 0}\frac{x-\sin x}{x^{2}}.</equation><equation>\lim _ {x \rightarrow 0} \frac {x - \sin x}{x ^ {2}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - \cos x}{2 x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\sin x}{2} = 0.</equation>或者，利用<equation>\sin x=x-\frac{x^{3}}{6}+o\left(x^{3}\right)</equation>可得<equation>\lim _ {x \rightarrow 0} \frac {x - \sin x}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\frac {x ^ {3}}{6} + o \left(x ^ {3}\right)}{x ^ {2}} = 0.</equation>因此，<equation>a = \lim _ {x \rightarrow 0} \frac {x ^ {2} + x - \sin x}{x ^ {2}} = 1 + \lim _ {x \rightarrow 0} \frac {x - \sin x}{x ^ {2}} = 1 + 0 = 1.</equation>（Ⅱ）由第（I）问得，<equation>a=\lim_{x\to 0}f(x)=1</equation>，故<equation>\lim_{x\to 0}[f(x)-1] = 0.</equation>若<equation>f ( x ) - 1</equation>与<equation>x^{k}</equation>是<equation>x\to 0</equation>时的同阶无穷小量，则<equation>\lim_{x\to 0}\frac{f(x)-1}{x^k}</equation>为一非零常数.<equation>\lim _ {x \rightarrow 0} \frac {f (x) - 1}{x ^ {k}} = \lim _ {x \rightarrow 0} \frac {x ^ {2} + x - \sin x - x \sin x}{x ^ {k + 1} \sin x} \xlongequal {\sin x \sim x} \lim _ {x \rightarrow 0} \frac {x ^ {2} + x - \sin x - x \sin x}{x ^ {k + 2}}.</equation>下面用两种方法来求上面的极限.

（法一）利用洛必达法则.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {x ^ {2} + x - \sin x - x \sin x}{x ^ {k + 2}} &= \lim _ {x \rightarrow 0} \frac {(1 + x) (x - \sin x)}{x ^ {k + 2}} = \lim _ {x \rightarrow 0} \frac {x - \sin x}{x ^ {k + 2}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - \cos x}{(k + 2) x ^ {k + 1}} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\sin x}{(k + 2) (k + 1) x ^ {k}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\cos x}{(k + 2) (k + 1) k x ^ {k - 1}} \\ &= \lim _ {x \rightarrow 0} \frac {1}{(k + 2) (k + 1) k x ^ {k - 1}} = c. \end{aligned}</equation>要使上面的极限等于非零常数<equation>c, x^{k - 1}</equation>必须等于1，即<equation>k = 1</equation>. 此时<equation>c = \frac{1}{6}</equation>.

（法二）利用等价无穷小替换.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {x ^ {2} + x - \sin x - x \sin x}{x ^ {k + 2}} &= \lim _ {x \rightarrow 0} \frac {(1 + x) (x - \sin x)}{x ^ {k + 2}} = \lim _ {x \rightarrow 0} \frac {x - \sin x}{x ^ {k + 2}} \\ \frac {x - \sin x - \frac {x ^ {3}}{6}}{\frac {1}{6}} \frac {1}{6} \lim _ {x \rightarrow 0} \frac {x ^ {3}}{x ^ {k + 2}} &= c. \end{aligned}</equation>若<equation>k+2<3</equation>，则<equation>\lim_{x\to 0}\frac{x^{3}}{x^{k+2}}=0</equation>；若<equation>k+2>3</equation>，则<equation>\lim_{x\to 0}\frac{x^{3}}{x^{k+2}}=\infty</equation>；若<equation>k+2=3</equation>，则<equation>\lim_{x\to 0}\frac{x^{3}}{x^{3}}=1.</equation>因此，<equation>k+2=3</equation>，<equation>c=\frac{1}{6}</equation>，即<equation>k=1</equation>，<equation>c=\frac{1}{6}.</equation>

---

**2011年第1题 | 选择题 | 4分 | 答案: C**

1. 已知当<equation>x\to0</equation>时，函数<equation>f(x)=3\sin x-\sin 3x</equation>与<equation>cx^{k}</equation>是等价无穷小量，则（    )

A. k=1,c=4 B. k=1,c=-4 C. k=3,c=4 D. k=3,c=-4

答案: C

**解析:**解 由题设知，<equation>c\neq 0,k > 0.</equation>记<equation>I=\lim_{x\to 0}\frac{f(x)}{cx^{k}}</equation>，则由等价无穷小量的定义知，<equation>I=1.</equation>下面我们用两种方法讨论 k,c的值.

（法一）考虑 f(x)在 x=0处的泰勒公式.由于<equation>\sin x=x-\frac{1}{3!} x^{3}+o\left(x^{3}\right)</equation>，故<equation>\sin 3x=3x-\frac{1}{3!}\left(3x\right)^{3}+o\left(x^{3}\right).</equation>因此，<equation>1 = \lim _ {x \rightarrow 0} \frac {3 \sin x - \sin 3 x}{c x ^ {k}} = \lim _ {x \rightarrow 0} \frac {3 x - \frac {1}{2} x ^ {3} - 3 x + \frac {2 7}{6} x ^ {3} + o \left(x ^ {3}\right)}{c x ^ {k}} = \lim _ {x \rightarrow 0} \frac {4 x ^ {3} + o \left(x ^ {3}\right)}{c x ^ {k}}.</equation>下面讨论使<equation>\lim_{x\to 0}\frac{4x^{3}+o\left(x^{3}\right)}{cx^{k}}=1</equation>成立的 k，c的值.

由于<equation>I = \frac {4}{c} \lim _ {x \rightarrow 0} \frac {x ^ {3}}{x ^ {k}} \left[ 1 + \frac {o \left(x ^ {3}\right)}{4 x ^ {3}} \right] = \frac {4}{c} \lim _ {x \rightarrow 0} \frac {x ^ {3}}{x ^ {k}},</equation>故当<equation>c\neq 0,k < 3</equation>时，<equation>I = 0</equation>；当<equation>c\neq 0,k > 3</equation>时，<equation>I = \infty</equation>；只有当<equation>c\neq 0,k = 3</equation>时，<equation>I = \frac{4}{c} = 1.</equation>因此，<equation>k = 3,c = 4.</equation>应选C.

（法二）对<equation>I</equation>使用洛必达法则可得，<equation>I = \lim _ {x \rightarrow 0} \frac {3 \sin x - \sin 3 x}{c x ^ {k}} \xlongequal {\text {洛 必达}} \lim _ {x \rightarrow 0} \frac {3 \cos x - 3 \cos 3 x}{k c x ^ {k - 1}}.</equation>由于<equation>I = 1</equation>，而<equation>\lim_{x\to 0}(3\cos x - 3\cos 3x) = 0</equation>，故<equation>k > 1</equation>，否则<equation>I = 0.</equation>当<equation>k > 1</equation>时，继续对（1）式使用洛必达法则可得，<equation>\lim _ {x \rightarrow 0} \frac {3 \cos x - 3 \cos 3 x}{k c x ^ {k - 1}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {- 3 \sin x + 9 \sin 3 x}{k (k - 1) c x ^ {k - 2}}.</equation>由于<equation>I = 1</equation>，而<equation>\lim_{x\to 0}(-3\sin x + 9\sin 3x) = 0</equation>，故<equation>k > 2</equation>，否则<equation>I = 0.</equation>当<equation>k > 2</equation>时，继续对（2）式使用洛必达法则可得，<equation>\lim _ {x \rightarrow 0} \frac {- 3 \sin x + 9 \sin 3 x}{k (k - 1) c x ^ {k - 2}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {- 3 \cos x + 2 7 \cos 3 x}{k (k - 1) (k - 2) c x ^ {k - 3}} = \lim _ {x \rightarrow 0} \frac {2 4}{k (k - 1) (k - 2) c x ^ {k - 3}}.</equation>若 I=1，则 k=3，否则当 k<3时，I=0；当 k>3时，<equation>I=\infty</equation>.进一步可得<equation>3\times 2\times c=2 4</equation>从而 c=4.应选C.

---

**2009年第2题 | 选择题 | 4分 | 答案: A**

2. 当<equation>x\to0</equation>时，<equation>f(x)=x-\sin ax</equation>与<equation>g(x)=x^{2}\ln(1-bx)</equation>是等价无穷小量，则（    )

A. a=1,b=-<equation>\frac{1}{6}</equation>B. a=1,b=<equation>\frac{1}{6}</equation>C. a=-1,b=-<equation>\frac{1}{6}</equation>D. a=-1,b=<equation>\frac{1}{6}</equation>

答案: A

**解析:**解（法一）由于<equation>x\to 0</equation>时，<equation>f(x)</equation>与<equation>g(x)</equation>是等价无穷小量，故<equation>\begin{aligned} 1 &= \lim _ {x \rightarrow 0} \frac {f (x)}{g (x)} = \lim _ {x \rightarrow 0} \frac {x - \sin a x}{x ^ {2} \ln (1 - b x)} \xlongequal {\ln (1 - b x) \sim (- b x)} \lim _ {x \rightarrow 0} \frac {x - \sin a x}{- b x ^ {3}} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - a \cos a x}{- 3 b x ^ {2}} &= I _ {1}. \end{aligned}</equation>由于<equation>\lim_{x\to 0}(-3bx^2) = 0</equation>，故若<equation>I_{1}</equation>存在，则<equation>\lim_{x\to 0}(1 - a\cos ax) = 0</equation>，从而<equation>a = 1.</equation>代人 a=1，得<equation>I _ {1} = \lim _ {x \rightarrow 0} \frac {1 - \cos x}{- 3 b x ^ {2}} \xlongequal {\text {一}} \frac {1 - \cos x \sim \frac {x ^ {2}}{2}}{\lim _ {x \rightarrow 0} \frac {\frac {x ^ {2}}{2}}{- 3 b x ^ {2}}} = - \frac {1}{6 b}.</equation>当<equation>b = -\frac{1}{6}</equation>时，<equation>I_{1}</equation>存在且等于1.

因此，当<equation>a=1,b=-\frac{1}{6}</equation>时，<equation>\lim_{x\to 0}\frac{f(x)}{g(x)}=1,f(x)</equation>与g(x）是<equation>x\to 0</equation>时的等价无穷小量.应选A.

（法二）因为<equation>\sin a x = a x - \frac {1}{6} a ^ {3} x ^ {3} + o \left(x ^ {3}\right), \quad \ln (1 - b x) = - b x + o (x),</equation>所以<equation>1 = \lim _ {x \rightarrow 0} \frac {x - \sin a x}{x ^ {2} \ln (1 - b x)} = \lim _ {x \rightarrow 0} \frac {(x - a x) + \frac {1}{6} a ^ {3} x ^ {3} - o \left(x ^ {3}\right)}{x ^ {2} \left[ - b x + o (x) \right]} = \lim _ {x \rightarrow 0} \frac {(1 - a) x + \frac {1}{6} a ^ {3} x ^ {3} - o \left(x ^ {3}\right)}{- b x ^ {3} + o \left(x ^ {3}\right)} = I.</equation>首先，<equation>b\neq 0</equation>，否则<equation>I = \infty</equation>.当<equation>b\neq 0</equation>时，若<equation>a - 1\neq 0</equation>，则<equation>I = \infty</equation>，从而可得<equation>a = 1</equation>代入 a=1，得<equation>1 = \lim _ {x \rightarrow 0} \frac {\frac {1}{6} x ^ {3} - o \left(x ^ {3}\right)}{- b x ^ {3} + o \left(x ^ {3}\right)} = - \frac {1}{6 b}.</equation>从而<equation>b = -\frac{1}{6}</equation>因此，<equation>a=1,b=-\frac{1}{6}</equation>应选A.

---


#### 函数极限的计算

**2022年第11题 | 填空题 | 5分**

<equation>1. \lim _ {x \rightarrow 0} \left(\frac {1 + \mathrm {e} ^ {x}}{2}\right) ^ {\cot x} = \underline {{}}</equation>

**解析:**取对数再求极限.<equation>\lim _ {x \rightarrow 0} \left(\frac {1 + \mathrm {e} ^ {x}}{2}\right) ^ {\cot x} = \lim _ {x \rightarrow 0} \mathrm {e} ^ {\cot x \ln \frac {1 + \mathrm {e} ^ {x}}{2}} = \mathrm {e} _ {x \rightarrow 0} ^ {\lim _ {x \rightarrow 0} \cot x \ln \frac {1 + \mathrm {e} ^ {x}}{2}}.</equation>下面计算<equation>\lim_{x\to 0}\cot x\ln \frac{1 + \mathrm{e}^{x}}{2}</equation>.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \cot x \ln \frac {1 + e ^ {x}}{2} &= \lim _ {x \rightarrow 0} \frac {\ln \frac {1 + e ^ {x}}{2}}{\tan x} \xlongequal {\tan x \sim x} \lim _ {x \rightarrow 0} \frac {\ln \left(1 + \frac {e ^ {x} - 1}{2}\right)}{x} \\ \frac {\ln \left(1 + \frac {\mathrm {e} ^ {x} - 1}{2}\right) - \frac {\mathrm {e} ^ {x} - 1}{2}}{\lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x} - 1}{2 x}} \xlongequal {\mathrm {e} ^ {x} - 1 \sim x} \lim _ {x \rightarrow 0} \frac {x}{2 x} \\ &= \frac {1}{2}. \end{aligned}</equation>因此，原极限<equation>= \mathrm{e}^{\frac{1}{2}} = \sqrt{\mathrm{e}}.</equation>

---

**2021年第17题 | 解答题 | 10分**

17. (本题满分10分)

求极限 lim<equation>\left(\frac {1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t}{\mathrm {e} ^ {x} - 1} - \frac {1}{\sin x}\right)</equation>

**解析:**解 （法一）先整理原极限再计算.<equation>\begin{array}{l} \frac {\mathrm {e} ^ {x} - 1 \sim x}{\sin x \sim x} \lim _ {x \rightarrow 0} \frac {\int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t}{x} + \lim _ {x \rightarrow 0} \frac {\sin x - \mathrm {e} ^ {x} + 1}{x ^ {2}} \\ \frac {\mathrm {洛 必 达}}{} \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x ^ {2}}}{1} + \lim _ {x \rightarrow 0} \frac {x - \frac {x ^ {3}}{6} - 1 - x - \frac {x ^ {2}}{2} + 1 + o \left(x ^ {2}\right)}{x ^ {2}} \\ = 1 + \lim _ {x \rightarrow 0} \frac {- \frac {x ^ {2}}{2} + o \left(x ^ {2}\right)}{x ^ {2}} = 1 - \frac {1}{2} = \frac {1}{2}. \\ \end{array}</equation>因此，原极限<equation>= \frac{1}{2}。</equation>（法二）将原极限通分整理，化为<equation>\frac{0}{0}</equation>型未定式后再应用洛必达法则.<equation>\begin{aligned} \mathrm {原 极 限} &= \lim _ {x \rightarrow 0} \frac {\sin x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) - \mathrm {e} ^ {x} + 1}{\left(\mathrm {e} ^ {x} - 1\right) \sin x} \\ \frac {\mathrm {e} ^ {x} - 1 \sim x}{\sin x \sim x} \lim _ {x \rightarrow 0} \frac {\sin x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) - \mathrm {e} ^ {x} + 1}{x ^ {2}} \\ \underline {{\text {洛必达}}} \lim _ {x \rightarrow 0} \frac {\cos x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) + \sin x \cdot \mathrm {e} ^ {x ^ {2}} - \mathrm {e} ^ {x}}{2 x} \\ \underline {{\text {洛必达}}} \lim _ {x \rightarrow 0} \frac {- \sin x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) + \cos x \cdot \mathrm {e} ^ {x ^ {2}} + 2 x \cdot \sin x \cdot \mathrm {e} ^ {x ^ {2}} - \mathrm {e} ^ {x}}{2} &= \frac {1}{2}. \end{aligned}</equation>因此，原极限<equation>= \frac{1}{2}.</equation>

---

**2019年第9题 | 填空题 | 4分**

（无内容）

**答案:**##<equation>4 \mathrm{e}^{2}.</equation>

**解析:**（法一）凑重要极限.<equation>\lim _ {x \rightarrow 0} \left(x + 2 ^ {x}\right) ^ {\frac {2}{x}} = \lim _ {x \rightarrow 0} \left(1 + x + 2 ^ {x} - 1\right) ^ {\frac {1}{x + 2 ^ {x} - 1}} \cdot \frac {2 \left(x + 2 ^ {x} - 1\right)}{x}.</equation>计算<equation>\lim_{x\to 0}\frac{2(x+2^{x}-1)}{x}.</equation><equation>\lim _ {x \rightarrow 0} \frac {2 \left(x + 2 ^ {x} - 1\right)}{x} = 2 + 2 \lim _ {x \rightarrow 0} \frac {2 ^ {x} - 1}{x} \frac {2 ^ {x} - 1 \sim x \ln 2}{2} + 2 \lim _ {x \rightarrow 0} \frac {x \ln 2}{x} = 2 + 2 \ln 2.</equation>因此，原极限<equation>= \mathrm{e}^{2 + 2\ln 2} = 4\mathrm{e}^{2}.</equation>（法二）取对数，再求极限.<equation>\lim _ {x \rightarrow 0} \left(x + 2 ^ {x}\right) ^ {\frac {2}{x}} = \lim _ {x \rightarrow 0} \mathrm {e} ^ {\frac {2 \ln \left(x + 2 ^ {x}\right)}{x}} = \mathrm {e} ^ {\lim _ {x \rightarrow 0} \frac {2 \ln \left(x + 2 ^ {x}\right)}{x}} \xlongequal {\text {洛必达}} \mathrm {e} ^ {2 \lim _ {x \rightarrow 0} \frac {1 + 2 ^ {x} \ln 2}{x + 2 ^ {x}}} = \mathrm {e} ^ {2 + 2 \ln 2} = 4 \mathrm {e} ^ {2}.</equation>

---

**2018年第9题 | 填空题 | 4分**

9.<equation>\lim x^{2}[\arctan(x+1)-\arctan x]=</equation>

**答案:**```latex

1.
```
**解析: **解（法一）由拉格朗日中值定理可得，存在<equation>\xi_{x}\in(x,x+1)</equation>，使得<equation>\arctan (x + 1) - \arctan x = \frac {1}{1 + \xi_ {x} ^ {2}}.</equation>于是，原极限<equation>= \lim_{x\to +\infty}\frac{x^{2}}{1 + \xi_{x}^{2}}.</equation>由于当 x > 0时，<equation>\frac{x^{2}}{1+(x+1)^{2}}\leqslant \frac{x^{2}}{1+\xi_{x}^{2}}\leqslant \frac{x^{2}}{1+x^{2}}</equation>，而<equation>\lim_{x\rightarrow +\infty}\frac{x^{2}}{1+(x+1)^{2}}=\lim_{x\rightarrow +\infty}\frac{x^{2}}{1+x^{2}}=1</equation>，故由夹逼准则可知<equation>\lim_{x\rightarrow +\infty}\frac{x^{2}}{1+\xi_{x}^{2}}=1.</equation>因此，原极限 = 1.

（法二）利用洛必达法则.<equation>\begin{aligned} \lim _ {x \rightarrow + \infty} x ^ {2} [ \arctan (x + 1) - \arctan x ] &= \lim _ {x \rightarrow + \infty} \frac {\arctan (x + 1) - \arctan x}{\frac {1}{x ^ {2}}} \\ \underline {{\mathrm {洛 必 达}}} \lim _ {x \rightarrow + \infty} \frac {\frac {1}{1 + (x + 1) ^ {2}} - \frac {1}{1 + x ^ {2}}}{- 2 \cdot \frac {1}{x ^ {3}}} \\ &= - \frac {1}{2} \lim _ {x \rightarrow + \infty} \frac {\left[ x ^ {2} - (x + 1) ^ {2} \right] \cdot x ^ {3}}{\left[ 1 + (x + 1) ^ {2} \right]\left(1 + x ^ {2}\right)} \\ &= - \frac {1}{2} \lim _ {x \rightarrow + \infty} \frac {- 2 x ^ {4} - x ^ {3}}{x ^ {4} + 2 x ^ {3} + 3 x ^ {2} + 2 x + 2} = 1. \end{aligned}</equation>

---

**2017年第3题 | 选择题 | 4分 | 答案: D**
3. 设数列<equation>\{x_{n}\}</equation>收敛，则（    )

A. 当<equation>\lim_{n\rightarrow \infty}\sin x_{n}=0</equation>时，<equation>\lim_{n\rightarrow \infty}x_{n}=0</equation>B. 当<equation>\lim_{n\rightarrow \infty}(x_{n}+\sqrt{|x_{n}|})=0</equation>时，<equation>\lim_{n\rightarrow \infty}x_{n}=0</equation>C. 当<equation>\lim_{n\rightarrow \infty}(x_{n}+x_{n}^{2})=0</equation>时，<equation>\lim_{n\rightarrow \infty}x_{n}=0</equation>D. 当<equation>\lim_{n\rightarrow \infty}(x_{n}+\sin x_{n})=0</equation>时，<equation>\lim_{n\rightarrow \infty}x_{n}=0</equation>
答案: D
**解析: **解（法一）记<equation>\lim_{n\to \infty}x_n = a</equation>，则由<equation>\sin x</equation>是连续函数以及<equation>\lim_{n\to \infty}(x_n + \sin x_n) = 0</equation>可知，<equation>\lim _ {n \rightarrow \infty} \left(x _ {n} + \sin x _ {n}\right) = a + \sin a = 0.</equation>x=a是函数<equation>f ( x )=x+\sin x</equation>的零点.

注意到<equation>f(0)=0</equation>，又因为<equation>f^{\prime}(x)=1+\cos x\geqslant 0</equation>，所以 f(x)单调增加.于是 x=0是 f(x)的唯一零点，a=0.因此，<equation>\lim_{n\to \infty}x_{n}=0.</equation>应选D.

（法二）记<equation>f ( x )=x+\sin x</equation>，则<equation>f ( 0 )=0</equation><equation>f^{\prime}(x)=1+\cos x\geqslant0.</equation>于是 f(x)是单调增加的可导函数，<equation>f^{-1}</equation>存在且连续.

由于<equation>\lim_{n\to \infty} \left(x_{n}+\sin x_{n}\right)=0</equation>，故<equation>\lim _ {n \rightarrow \infty} x _ {n} = \lim _ {n \rightarrow \infty} f ^ {- 1} \left(f \left(x _ {n}\right)\right) = \lim _ {n \rightarrow \infty} f ^ {- 1} \left(x _ {n} + \sin x _ {n}\right) = f ^ {- 1} \left(\lim _ {n \rightarrow \infty} \left(x _ {n} + \sin x _ {n}\right)\right) = f ^ {- 1} (0) = 0.</equation>（法三）排除法.

对选项A：考虑<equation>x_{n}=\pi +\frac{1}{n}</equation>，则<equation>\lim_{n\to \infty}\sin x_{n}=0</equation>，但<equation>\lim_{n\to \infty}x_{n}=\pi.</equation>对选项B和选项C：考虑<equation>x_{n}\equiv-1</equation>，则<equation>\lim _ {n \rightarrow \infty} \left(x _ {n} + \sqrt {\left| x _ {n} \right|}\right) = 0, \quad \lim _ {n \rightarrow \infty} \left(x _ {n} + x _ {n} ^ {2}\right) = 0,</equation>但<equation>\lim_{n\to \infty}x_{n}=-1.</equation>由排除法知，应选D.

---

**2016年第15题 | 解答题 | 10分**
15. (本题满分10分）

求极限<equation>\lim_{x\to 0}(\cos 2x+2x\sin x)^{\frac{1}{x^{4}}}.</equation>
**解析: **## 记原极限为 I.

（法一）凑重要极限<equation>\lim_{x\to 0}(1+x)^{\frac{1}{x}}=e.</equation>由于<equation>x\to0</equation>时，<equation>\cos 2x+2x\sin x-1\to0</equation>，故<equation>\lim_{x\to0}\left(1+\cos 2x+2x\sin x-1\right)^{\frac{1}{\cos 2x+2x\sin x-1}}=e.</equation><equation>I = \lim _ {x \rightarrow 0} \left(1 + \cos 2 x + 2 x \sin x - 1\right) ^ {\frac {1}{\cos 2 x + 2 x \sin x - 1}} \cdot \frac {\cos 2 x + 2 x \sin x - 1}{x ^ {4}}.</equation>下面求<equation>\lim_{x\rightarrow0}\frac{\cos 2x+2x\sin x-1}{x^{4}}.</equation><equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {\cos 2 x + 2 x \sin x - 1}{x ^ {4}} \xlongequal {\cos 2 x - 1 = - 2 \sin^ {2} x} \lim _ {x \rightarrow 0} \frac {2 x \sin x - 2 \sin^ {2} x}{x ^ {4}} &= \lim _ {x \rightarrow 0} \frac {2 \sin x (x - \sin x)}{x ^ {4}} \\ \frac {\sin x - x}{x} 2 \lim _ {x \rightarrow 0} \frac {x - \sin x}{x ^ {3}} &= 2 \lim _ {x \rightarrow 0} \frac {x - x + \frac {x ^ {3}}{3 !} - o \left(x ^ {3}\right)}{x ^ {3}} = \frac {1}{3}. \end{aligned}</equation>因此，<equation>I=\mathrm{e}^{\frac{1}{3}}.</equation>下面我们用另外两种方法计算<equation>\lim_{x\to 0}\frac{\cos 2x+2x\sin x-1}{x^{4}}.</equation>(1) 利用泰勒公式.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {\cos 2 x + 2 x \sin x - 1}{x ^ {4}} &= \lim _ {x \rightarrow 0} \frac {1 - \frac {(2 x) ^ {2}}{2 !} + \frac {(2 x) ^ {4}}{4 !} + o \left(x ^ {4}\right) + 2 x \left[x - \frac {x ^ {3}}{3 !} + o \left(x ^ {3}\right)\right]}{x ^ {4}} - 1 \\ &= \lim _ {x \rightarrow 0} \frac {\frac {1}{3} x ^ {4} + o \left(x ^ {4}\right)}{x ^ {4}} = \frac {1}{3}. \end{aligned}</equation>(2) 利用洛必达法则.<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {\cos 2 x + 2 x \sin x - 1}{x ^ {4}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {- \sin 2 x + \sin x + x \cos x}{2 x ^ {3}} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {- 2 \cos 2 x + 2 \cos x - x \sin x}{6 x ^ {2}} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {4 \sin 2 x - 3 \sin x - x \cos x}{1 2 x} \\ \end{array}</equation><equation>\frac {\mathrm {洛 必 达}}{\mathrm {}} \lim _ {x \rightarrow 0} \frac {8 \cos 2 x - 4 \cos x + x \sin x}{1 2} = \frac {1}{3}.</equation>（法二）因为<equation>\lim_{x\to 0} \left(\cos 2x+2x\sin x\right)=1</equation>，从而我们可以对<equation>\cos 2x+2x\sin x</equation>取对数，所以<equation>I=\mathrm{e}^{\lim_{x\to 0}\frac{\ln(\cos 2x+2x\sin x)}{x^{4}}}.</equation>下面求<equation>\lim_{x\rightarrow0}\frac{\ln(\cos 2x+2x\sin x)}{x^{4}}.</equation><equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {\ln (\cos 2 x + 2 x \sin x)}{x ^ {4}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\frac {1}{\cos 2 x + 2 x \sin x} \cdot (- 2 \sin 2 x + 2 \sin x + 2 x \cos x)}{4 x ^ {3}} \\ &= - \frac {1}{2} \lim _ {x \rightarrow 0} \frac {\sin 2 x - \sin x - x \cos x}{x ^ {3}} \\ &= - \frac {1}{2} \lim _ {x \rightarrow 0} \frac {2 x - \frac {(2 x) ^ {3}}{3 !} + o \left(x ^ {3}\right) - x + \frac {x ^ {3}}{3 !} - o \left(x ^ {3}\right) - x \left[ 1 - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right)\right]}{x ^ {3}} \\ &= - \frac {1}{2} \lim _ {x \rightarrow 0} \frac {\left(- \frac {8}{6} + \frac {1}{6} + \frac {1}{2}\right) x ^ {3} + o \left(x ^ {3}\right)}{x ^ {3}} = \frac {1}{3}. \end{aligned}</equation>因此，<equation>I=\mathrm{e}^{\frac{1}{3}}.</equation>

---

**2014年第5题 | 选择题 | 4分 | 答案: D**
5. 设函数 f(x) = arctanx. 若 f(x) = xf'(<equation>\xi</equation>)，则<equation>\lim_{x\to 0}\frac{\xi^{2}}{x^{2}}</equation>= (    )

A. 1 B.<equation>\frac{2}{3}</equation>C.<equation>\frac{1}{2}</equation>D.<equation>\frac{1}{3}</equation>
答案: D
**解析: **解 由于<equation>f^{\prime}(x)=(\arctan x)^{\prime}=\frac{1}{1+x^{2}}</equation>，故<equation>f^{\prime}(\xi)=\frac{1}{1+\xi^{2}}</equation>. 由于<equation>f(x)=xf^{\prime}(\xi)=\frac{x}{1+\xi^{2}}</equation>，解得<equation>\xi^{2}=\frac{x}{f(x)}-1.</equation><equation>\lim _ {x \rightarrow 0} \frac {\xi^ {2}}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\frac {x}{\arctan x} - 1}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {x - \arctan x}{x ^ {2} \arctan x}.</equation>下面我们用两种方法计算上面的极限.

（法一）由于<equation>\arctan x</equation>的3阶泰勒公式为<equation>\arctan x = x - \frac{x^3}{3} + o(x^3)</equation>，故当<equation>x\to 0</equation>时，<equation>\arctan x \sim x, \quad x - \arctan x \sim \frac {x ^ {3}}{3}.</equation><equation>\lim _ {x \rightarrow 0} \frac {x - \arctan x}{x ^ {2} \arctan x} \xlongequal {\arctan x \sim x} \lim _ {x \rightarrow 0} \frac {x - \arctan x}{x ^ {3}} \xlongequal {x - \arctan x \sim \frac {x ^ {3}}{3}} \lim _ {x \rightarrow 0} \frac {\frac {1}{3} x ^ {3}}{x ^ {3}} = \frac {1}{3}.</equation>应选 D.

（法二）利用洛必达法则计算该极限.<equation>\lim _ {x \rightarrow 0} \frac {x - \arctan x}{x ^ {2} \arctan x} \xlongequal {\arctan x \sim x} \lim _ {x \rightarrow 0} \frac {x - \arctan x}{x ^ {3}} \xlongequal {\text {洛 必 达}} \lim _ {x \rightarrow 0} \frac {1 - \frac {1}{1 + x ^ {2}}}{3 x ^ {2}} = \lim _ {x \rightarrow 0} \frac {x ^ {2}}{3 x ^ {2}} = \frac {1}{3}.</equation>

---

**2014年第15题 | 解答题 | 10分**
15. (本题满分10分)<equation>\lim _ {r \rightarrow + \infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t \right] \mathrm {d} t}{x ^ {2} \ln \left(1 + \frac {1}{x}\right)}.</equation>
**答案: **## (15)<equation>\frac{1}{2}.</equation>
**解析: **解 由于<equation>\mathrm{e}^{x}</equation>在 x=0处的带拉格朗日余项的2阶泰勒公式为<equation>\mathrm{e}^{x}=1+x+\frac{x^{2}}{2}+\frac{\mathrm{e}^{\theta x}}{3!} x^{3}</equation>其中<equation>0 < \theta < 1</equation>，故当 x > 0时，<equation>\mathrm{e}^{x}>1+x+\frac{x^{2}}{2}.</equation>于是，<equation>\mathrm{e}^{\frac{1}{t}}-1 > \frac{1}{t} +\frac{1}{2t^{2}}(t > 0),</equation><equation>t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t > t ^ {2} \left(\frac {1}{t} + \frac {1}{2 t ^ {2}}\right) - t = \frac {1}{2}.</equation>从而<equation>\int_1^{+\infty}\left[ t^2\left(\mathrm{e}^{\frac{1}{t}} -1\right) - t\right]\mathrm{d}t\to +\infty .</equation>另一方面，<equation>\lim _ {x \rightarrow + \infty} \left[ x ^ {2} \ln \left(1 + \frac {1}{x}\right)\right] \xlongequal {\ln \left(1 + \frac {1}{x}\right) \sim \frac {1}{x}} \lim _ {x \rightarrow + \infty} x = + \infty .</equation>因此，原极限为<equation>\frac{\infty}{\infty}</equation>型未定式.

当<equation>x\to +\infty</equation>时，<equation>\ln \left(1 + \frac{1}{x}\right)\sim \frac{1}{x}</equation>，故<equation>\lim _ {x \rightarrow + \infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t \right] \mathrm {d} t}{x ^ {2} \ln \left(1 + \frac {1}{x}\right)} \xlongequal {\ln \left(1 + \frac {1}{x}\right) \sim \frac {1}{x}} \lim _ {x \rightarrow + \infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t \right] \mathrm {d} t}{x}</equation><equation>\begin{aligned} \underline {{\text {洛必达}}} \lim _ {x \rightarrow + \infty} \frac {x ^ {2} \left(\mathrm {e} ^ {\frac {1}{x}} - 1\right) - x}{1} &= \lim _ {x \rightarrow + \infty} \frac {\mathrm {e} ^ {\frac {1}{x}} - 1 - \frac {1}{x}}{\frac {1}{x ^ {2}}} \\ \underline {{\frac {u = \frac {1}{x}}}} \lim _ {u \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {u} - u - 1}{u ^ {2}} \underline {{\underline {{\text {洛必达}}}}} \lim _ {u \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {u} - 1}{2 u} \\ \underline {{\frac {\mathrm {e} ^ {u} - 1 \sim u}{u \rightarrow 0 ^ {+}}}} \lim _ {u \rightarrow 0 ^ {+}} \frac {u}{2 u} &= \frac {1}{2}. \end{aligned}</equation>因此，原极限<equation>= \frac{1}{2}.</equation>将原极限化简为<equation>\lim_{x\to +\infty}[x^{2}(\mathrm{e}^{\frac{1}{x}} - 1) - x]</equation>后，也可以用泰勒公式来求该极限.

当<equation>x\to +\infty</equation>时，<equation>\frac{1}{x}\rightarrow 0^{+}</equation>.由<equation>\mathrm{e}^{u}</equation>在<equation>u = 0</equation>处的泰勒公式得，<equation>\mathrm {e} ^ {\frac {1}{x}} = 1 + \frac {1}{x} + \frac {1}{2 !} \cdot \frac {1}{x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right).</equation>从而，<equation>\begin{array}{l} \lim _ {x \rightarrow + \infty} \left[ x ^ {2} \left(\mathrm {e} ^ {\frac {1}{x}} - 1\right) - x \right] = \lim _ {x \rightarrow + \infty} \left\{x ^ {2} \left[ \frac {1}{x} + \frac {1}{2 !} \cdot \frac {1}{x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right)\right] - x \right\} \\ = \lim _ {x \rightarrow + \infty} \left[ \frac {1}{2} + x ^ {2} \cdot o \left(\frac {1}{x ^ {2}}\right)\right] = \frac {1}{2}. \\ \end{array}</equation>

---

**2013年第9题 | 填空题 | 4分**
9. lim
**解析: **解（法一）将原极限改写，得<equation>\lim _ {x \rightarrow 0} \left[ 2 - \frac {\ln (1 + x)}{x} \right] ^ {\frac {1}{x}} = \lim _ {x \rightarrow 0} \left\{\left[ 1 + \frac {x - \ln (1 + x)}{x} \right] ^ {\frac {x}{x - \ln (1 + x)}} \right\} ^ {\frac {x - \ln (1 + x)}{x}}. \frac {1}{x}.</equation>由于<equation>\lim _ {x \rightarrow 0} \frac {x - \ln (1 + x)}{x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - \frac {1}{1 + x}}{1} = 0,</equation><equation>\lim _ {x \rightarrow 0} \frac {x - \ln (1 + x)}{x ^ {2}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - \frac {1}{1 + x}}{2 x} = \lim _ {x \rightarrow 0} \frac {1}{2 (1 + x)} = \frac {1}{2},</equation>故利用重要极限<equation>\lim_{x\to 0}(1 + x)^{\frac{1}{x}} = \mathrm{e}</equation>可得原极限<equation>= \sqrt{\mathrm{e}}.</equation>（法二）由于<equation>\ln \left[ 2 - \frac{\ln(1 + x)}{x} \right]^{\frac{1}{x}} = \frac{1}{x}\ln \left[ 2 - \frac{\ln(1 + x)}{x} \right],</equation>故<equation>\lim_{x\to 0}\left[ 2 - \frac{\ln(1 + x)}{x} \right]^{\frac{1}{x}} = \mathrm{e}^{\lim_{x\to 0}\frac{\ln[2 - \frac{\ln(1 + x)}{x}]}{x}}.</equation>下面求<equation>\lim_{x\to 0}\frac{\ln\left[2 - \frac{\ln(1 + x)}{x}\right]}{x}</equation>.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {\ln \left[ 2 - \frac {\ln (1 + x)}{x} \right]}{x} &= \lim _ {x \rightarrow 0} \frac {\ln \left[ 1 + 1 - \frac {\ln (1 + x)}{x} \right]}{x} \\ \underline {{\underline {{\ln \left[ 1 + 1 - \frac {\ln (1 + x)}{x} \right] \sim 1 - \frac {\ln (1 + x)}{x}}}}} \lim _ {x \rightarrow 0} \frac {1 - \frac {\ln (1 + x)}{x}}{x} \\ &= \lim _ {x \rightarrow 0} \frac {x - \ln (1 + x)}{x ^ {2}} \xlongequal {\text {洛 必达}} \lim _ {x \rightarrow 0} \frac {1 - \frac {1}{1 + x}}{2 x} = \lim _ {x \rightarrow 0} \frac {1}{2 (1 + x)} = \frac {1}{2}. \end{aligned}</equation>因此，原极限<equation>= \sqrt{\mathrm{e}}.</equation>也可以利用<equation>\ln (1 + x) = x - \frac{x^2}{2} + o\left(x^2\right)</equation>来求<equation>\lim_{x\to 0}\frac{x - \ln(1 + x)}{x^2}</equation>.<equation>\lim _ {x \rightarrow 0} \frac {x - \ln (1 + x)}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {x - x + \frac {x ^ {2}}{2} - o \left(x ^ {2}\right)}{x ^ {2}} = \frac {1}{2}.</equation>

---

**2011年第9题 | 填空题 | 4分**
（无内容）
**解析: **解 （法一）由于<equation>\lim _ {x \rightarrow 0} \left(\frac {1 + 2 ^ {x}}{2}\right) ^ {\frac {1}{x}} = \lim _ {x \rightarrow 0} \mathrm {e} ^ {\frac {1}{x} \ln \frac {1 + 2 ^ {x}}{2}} = \mathrm {e} ^ {\lim _ {x \rightarrow 0} \frac {1}{x} \ln \frac {1 + 2 ^ {x}}{2}},</equation>故只需要求<equation>\lim_{x\to 0}\frac{1}{x}\ln \frac{1 + 2^x}{2}</equation>.<equation>\lim _ {x \rightarrow 0} \frac {\ln \frac {1 + 2 ^ {x}}{2}}{x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \left(\frac {2}{1 + 2 ^ {x}} \cdot \frac {2 ^ {x}}{2} \cdot \ln 2\right)=\frac {\ln 2}{2}.</equation>因此，<equation>\lim _ {x \rightarrow 0} \left(\frac {1 + 2 ^ {x}}{2}\right) ^ {\frac {1}{x}} = \mathrm {e} ^ {\frac {\ln 2}{2}} = \sqrt {2}.</equation>（法二）由于<equation>\left(\frac {1 + 2 ^ {x}}{2}\right) ^ {\frac {1}{x}} = \left(1 + \frac {2 ^ {x} - 1}{2}\right) ^ {\frac {1}{x}} = \left[ \left(1 + \frac {2 ^ {x} - 1}{2}\right) ^ {\frac {2}{2 ^ {x} - 1}} \right] ^ {\frac {2 ^ {x} - 1}{2 x}},</equation>而利用重要极限可得<equation>\lim_{x\to 0}\left(1 + \frac{2^x - 1}{2}\right)^{\frac{2}{2^x - 1}} = \mathrm{e},\lim_{x\to 0}\frac{2^x - 1}{2x}\xlongequal{\text{洛必达}}\lim_{x\to 0}\frac{2^x\ln 2}{2} = \frac{\ln 2}{2}</equation>，故<equation>\lim _ {x \rightarrow 0} \left(\frac {1 + 2 ^ {x}}{2}\right) ^ {\frac {1}{x}} = \mathrm {e} ^ {\frac {\ln 2}{2}} = \sqrt {2}.</equation>

---

**2011年第15题 | 解答题 | 10分**
15. (本题满分10分）

已知函数 F(x)<equation>= \frac{\int_{0}^{x}\ln(1+t^{2})\mathrm{d}t}{x^{\alpha}}</equation>. 设<equation>\lim_{x\rightarrow+\infty}F(x)=\lim_{x\rightarrow 0^{+}}F(x)=0</equation>，试求<equation>\alpha</equation>的取值范围.
**答案: **(15) 1 <<equation>\alpha < 3</equation>
**解析: **解记<equation>f ( x )=\int_{0}^{x}\ln(1+t^{2})\mathrm{d} t</equation>，则<equation>F ( x )=\frac{f ( x )}{x^{\alpha}}.</equation>可以看出，<equation>\lim_{x\to 0^{+}}f(x) = 0,</equation><equation>\lim_{x\to +\infty}f(x) = +\infty.</equation><equation>\textcircled{1}</equation><equation>x \to+\infty</equation>时的情形.

当<equation>\alpha \leqslant 0</equation>时，<equation>\lim_{x\to +\infty}\frac{f(x)}{x^{\alpha}} = +\infty</equation>当<equation>\alpha > 0</equation>时，<equation>\lim_{x\to +\infty}\frac{f(x)}{x^{\alpha}}</equation>为<equation>\frac{\infty}{\infty}</equation>型未定式.<equation>\lim _ {x \rightarrow + \infty} \frac {f (x)}{x ^ {\alpha}} \xlongequal {\text {洛 必达}} \lim _ {x \rightarrow + \infty} \frac {\ln \left(1 + x ^ {2}\right)}{\alpha x ^ {\alpha - 1}}.</equation>- 当<equation>0 < \alpha \leqslant 1</equation>时，<equation>\lim_{x\to +\infty}\frac{\ln(1 + x^2)}{\alpha x^{\alpha -1}} = +\infty .</equation>- 当<equation>\alpha >1</equation>时，<equation>\lim_{x\rightarrow +\infty}\frac{\ln(1+x^{2})}{\alpha x^{\alpha-1}}</equation>为<equation>\frac{\infty}{\infty}</equation>型未定式，继续使用洛必达法则得<equation>\begin{aligned} \lim _ {x \rightarrow + \infty} \frac {\ln \left(1 + x ^ {2}\right)}{\alpha x ^ {\alpha - 1}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow + \infty} \frac {\frac {2 x}{x ^ {2} + 1}}{\alpha (\alpha - 1) x ^ {\alpha - 2}} &= \lim _ {x \rightarrow + \infty} \frac {2}{\alpha (\alpha - 1) \left(x ^ {2} + 1\right) x ^ {\alpha - 3}} \\ &= \lim _ {x \rightarrow + \infty} \frac {2}{\alpha (\alpha - 1) x ^ {\alpha - 1} \left(1 + \frac {1}{x ^ {2}}\right)} = \lim _ {x \rightarrow + \infty} \frac {2}{\alpha (\alpha - 1) x ^ {\alpha - 1}} = 0. \end{aligned}</equation>因此，当<equation>\alpha > 1</equation>时，<equation>\lim_{x\to +\infty}\frac{f(x)}{x^{\alpha}} = 0.</equation><equation>\textcircled{2}</equation><equation>x\to 0^{+}</equation>时的情形.

当<equation>\alpha \leqslant 0</equation>时，<equation>\lim_{x\to 0^{+}}\frac{f(x)}{x^{\alpha}} = 0.</equation>当<equation>\alpha > 0</equation>时，<equation>\lim_{x\to 0^{+}}\frac{f(x)}{x^{\alpha}}</equation>为<equation>\frac{0}{0}</equation>型未定式.<equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {f (x)}{x ^ {\alpha}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\ln \left(1 + x ^ {2}\right)}{\alpha x ^ {\alpha - 1}} \xlongequal {\text {~} \ln \left(1 + x ^ {2}\right) \sim x ^ {2}} \lim _ {x \rightarrow 0 ^ {+}} \frac {x ^ {2}}{\alpha x ^ {\alpha - 1}} = \frac {1}{\alpha} \lim _ {x \rightarrow 0 ^ {+}} x ^ {3 - \alpha}.</equation>因此，当<equation>\alpha > 3</equation>时，<equation>\lim_{x\to 0^{+}}\frac{f(x)}{x^{\alpha}}=+\infty</equation>；当<equation>\alpha =3</equation>时，<equation>\lim_{x\to 0^{+}}\frac{f(x)}{x^{3}}=\frac{1}{3}</equation>；当<equation>\alpha < 3</equation>时，<equation>\lim_{x\to 0^{+}}\frac{f(x)}{x^{\alpha}}=0.</equation>综上所述，<equation>1 < \alpha < 3.</equation>

---

**2009年第15题 | 解答题 | 10分**
15. (本题满分9分)

求极限<equation>\lim _ {x \rightarrow 0} \frac {(1 - \cos x) [ x - \ln (1 + \tan x) ]}{\sin^ {4} x}.</equation>
**答案: **<equation>(1 5) \frac {1}{4}.</equation>
**解析: **解 （法一）使用等价无穷小替换结合洛必达法则求极限.

当<equation>x\to0</equation>时，<equation>1-\cos x\sim \frac{1}{2} x^{2},\sin^{4}x\sim x^{4},\tan x\sim x.</equation>因此，<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {(1 - \cos x) [ x - \ln (1 + \tan x) ]}{\sin^ {4} x} &= \lim _ {x \rightarrow 0} \frac {\frac {1}{2} x ^ {2} [ x - \ln (1 + \tan x) ]}{x ^ {4}} = \lim _ {x \rightarrow 0} \frac {x - \ln (1 + \tan x)}{2 x ^ {2}} \\ \underline {{\text {洛必达}}} \lim _ {x \rightarrow 0} \frac {1 - \frac {\sec^ {2} x}{1 + \tan x}}{4 x} &= \lim _ {x \rightarrow 0} \frac {1 + \tan x - \sec^ {2} x}{4 x} \\ &= \lim _ {x \rightarrow 0} \frac {(1 - \tan x) \tan x}{4 x} = \lim _ {x \rightarrow 0} \frac {\tan x}{4 x} \underline {{\frac {\tan x \sim x}{4}}} \frac {1}{4}. \end{aligned}</equation>（法二）同法一的步骤化简原极限式，之后利用泰勒公式来求<equation>\lim_{x\to 0}\frac{x-\ln(1+\tan x)}{2x^{2}}.</equation>利用<equation>\ln(1+x)=x-\frac{1}{2}x^{2}+o\left(x^{2}\right)</equation>得<equation>\ln (1 + \tan x) = \tan x - \frac {\left(\tan x\right) ^ {2}}{2} + o \left(\tan^ {2} x\right) = \tan x - \frac {\left(\tan x\right) ^ {2}}{2} + o \left(x ^ {2}\right).</equation>因此，<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {x - \ln (1 + \tan x)}{2 x ^ {2}} &= \lim _ {x \rightarrow 0} \frac {x - \tan x + \frac {\left(\tan x\right) ^ {2}}{2} - o \left(x ^ {2}\right)}{2 x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\frac {\left(\tan x\right) ^ {2}}{2}}{2 x ^ {2}} + \lim _ {x \rightarrow 0} \frac {x - \tan x}{2 x ^ {2}} \\ \underline {{\text {洛必达}}} \frac {1}{4} + \lim _ {x \rightarrow 0} \frac {1 - \sec^ {2} x}{4 x} &= \frac {1}{4} - \lim _ {x \rightarrow 0} \frac {\tan^ {2} x}{4 x} \\ \underline {{\frac {\tan x - x}{4}}} \frac {1}{4} - \lim _ {x \rightarrow 0} \frac {x}{4} &= \frac {1}{4}. \end{aligned}</equation>因此，原极限<equation>= \frac{1}{4}.</equation>

---


### 一元函数积分学