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
