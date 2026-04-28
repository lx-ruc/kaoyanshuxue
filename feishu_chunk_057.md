#### 幂级数的和函数及幂级数展开式

**2024年第3题 | 选择题 | 5分 | 答案: A**
3. 已知幂级数<equation>\sum_{n=0}^{\infty} a_{n} x^{n}</equation>的和函数为<equation>\ln(2+x)</equation>，则<equation>\sum_{n=0}^{\infty} n a_{2n}=</equation>(    )

A.<equation>-\frac{1}{6}</equation>B.<equation>-\frac{1}{3}</equation>C.<equation>\frac{1}{6}</equation>D.<equation>\frac{1}{3}</equation>
答案: A
**解析: **解（法一）由<equation>\ln(1+x)=\sum_{n=1}^{\infty}(-1)^{n-1}\frac{x^{n}}{n}(-1<x\leqslant 1)</equation>可得<equation>\ln (2 + x) = \ln \left[ 2 \cdot \left(1 + \frac {x}{2}\right) \right] = \ln 2 + \ln \left(1 + \frac {x}{2}\right) = \ln 2 + \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1}}{n} \left(\frac {x}{2}\right) ^ {n}.</equation>由此可得，当<equation>n > 0</equation>时，<equation>x^{2n}</equation>的系数为<equation>a_{2n} = \frac{(-1)^{2n - 1}}{2n2^{2n}} = \frac{-1}{2n2^{2n}}.</equation>因此，<equation>\sum_ {n = 0} ^ {\infty} n a _ {2 n} = \sum_ {n = 1} ^ {\infty} n a _ {2 n} = \sum_ {n = 1} ^ {\infty} \frac {- n}{2 n 2 ^ {2 n}} = \sum_ {n = 1} ^ {\infty} \frac {- 1}{2 ^ {2 n + 1}} = \frac {- \frac {1}{8}}{1 - \frac {1}{4}} = - \frac {1}{6}.</equation>应选 A.

（法二）由<equation>\sum_{n = 0}^{\infty}a_nx^n = \ln (2 + x)</equation>可得<equation>\sum_{n = 0}^{\infty}a_n(-x)^n = \sum_{n = 0}^{\infty}(-1)^n a_nx^n = \ln (2 - x)</equation>.由此可得<equation>\sum_{n = 0}^{\infty}[1 + (-1)^n]a_nx^n = \ln (2 + x) + \ln (2 - x)</equation>，即<equation>2 \sum_ {n = 0} ^ {\infty} a _ {2 n} x ^ {2 n} = \ln (2 + x) + \ln (2 - x).</equation>对（1）式两端关于<equation>x</equation>求导可得，<equation>4 \sum_ {n = 1} ^ {\infty} n a _ {2 n} x ^ {2 n - 1} = \frac {1}{2 + x} - \frac {1}{2 - x}.</equation>在(2)式中令<equation>x = 1</equation>，可得<equation>4\sum_{n = 1}^{\infty}na_{2n} = \frac{1}{3} -1 = -\frac{2}{3}</equation>，进一步可得<equation>\sum_{n = 0}^{\infty}na_{2n} = -\frac{1}{6}</equation>因此，应选A.

（法三）注意到<equation>\left[ \ln (2 + x) \right] ^ {\prime} = \frac {1}{2 + x} = \frac {1}{2 \left(1 + \frac {x}{2}\right)} = \frac {1}{2} \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} \left(\frac {x}{2}\right) ^ {n},</equation>该幂级数的收敛半径为2，故在（-2，2）上，由牛顿一莱布尼茨公式可得<equation>\begin{aligned} \ln (2 + x) - \ln 2 &= \int_ {0} ^ {x} \left[ \ln (2 + t) \right] ^ {\prime} \mathrm {d} t = \int_ {0} ^ {x} \frac {1}{2} \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} \left(\frac {t}{2}\right) ^ {n} \mathrm {d} t \\ \frac {\text {逐 项 积 分}}{} \frac {1}{2} \sum_ {n = 0} ^ {\infty} \int_ {0} ^ {x} (- 1) ^ {n} \left(\frac {t}{2}\right) ^ {n} \mathrm {d} t &= \frac {1}{2} \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{n + 1} \cdot \frac {x ^ {n + 1}}{2 ^ {n}} \\ &= \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1} x ^ {n}}{n 2 ^ {n}}. \end{aligned}</equation>因此，<equation>\ln (2 + x) = \ln 2 + \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1} x ^ {n}}{n 2 ^ {n}}.</equation>其余同法一.

---

**2021年第18题 | 解答题 | 12分**
18. (本题满分12分)

设<equation>u_{n}(x)=\mathrm{e}^{-nx}+\frac{x^{n+1}}{n(n+1)}</equation>（<equation>n=1,2,\cdots</equation>），求级数<equation>\sum_{n=1}^{\infty}u_{n}(x)</equation>的收敛域及和函数.
**答案: **收敛域为（0，1]，和函数 s（x）=<equation>\left\{\begin{array}{l l} \frac{1}{e^{x}-1}+(1-x)\ln(1-x)+x,&x\in(0,1),\\ \frac{1}{e-1}+1,&x=1. \end{array} \right.</equation>
**解析: **解记<equation>s ( x )=\sum_{n=1}^{\infty} u_{n} ( x ).</equation>记<equation>s_{1}(x)=\sum_{n=1}^{\infty}\mathrm{e}^{-nx}.</equation>当<equation>|\mathrm{e}^{-x}|<1</equation>即<equation>x>0</equation>时，由几何级数的求和公式可得<equation>s_{1}(x)=\frac{\mathrm{e}^{-x}}{1-\mathrm{e}^{-x}}=\frac{1}{\mathrm{e}^{x}-1}</equation>该级数收敛.<equation>s_{1}(x)</equation>的收敛域为（0，<equation>+\infty).</equation>记<equation>s_{2}(x) = \sum_{n = 1}^{\infty}\frac{x^{n + 1}}{n(n + 1)}</equation>，其系数<equation>a_{n} = \frac{1}{n(n + 1)}</equation><equation>\lim _ {n \rightarrow \infty} \left| \frac {a _ {n + 1}}{a _ {n}} \right| = \lim _ {n \rightarrow \infty} \frac {n (n + 1)}{(n + 1) (n + 2)} = 1.</equation>于是，<equation>s_{2}(x)</equation>的收敛半径为1，收敛区间为<equation>(-1,1).</equation><equation>s_{2}(x)</equation>在<equation>x=-1</equation>处为<equation>\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n(n+1)}</equation>由莱布尼茨定理可知该级数收敛.<equation>s_{2}(x)</equation>在<equation>x=1</equation>处为<equation>\sum_{n=1}^{\infty}\frac{1}{n(n+1)}</equation>由极限审敛法可知该级数收敛.因此，<equation>s_{2}(x)</equation>的收敛域为<equation>[-1,1].</equation>取<equation>(0, + \infty)</equation>与<equation>[-1,1]</equation>的交集，可得<equation>(0,1]</equation>为<equation>s(x)</equation>的收敛域.

下面用两种方法计算<equation>s_{2}(x).</equation>（法一）整理<equation>s_{2}(x).</equation>当 x<equation>\in</equation>（0,1）时，<equation>\begin{aligned} s _ {2} (x) &= \sum_ {n = 1} ^ {\infty} \left(\frac {x ^ {n + 1}}{n} - \frac {x ^ {n + 1}}{n + 1}\right) = x \sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n} - \sum_ {n = 1} ^ {\infty} \frac {x ^ {n + 1}}{n + 1} = x \sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n} - \sum_ {n = 2} ^ {\infty} \frac {x ^ {n}}{n} \\ &= (x - 1) \sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n} + x. \end{aligned}</equation>记<equation>t(x) = \sum_{n = 1}^{\infty}\frac{x^n}{n}</equation>，则<equation>s_2(x) = (x - 1)t(x) + x.</equation><equation>t ^ {\prime} (x) = \left(\sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n}\right) ^ {\prime} \stackrel {\text {逐 项 求 导}} {=} \sum_ {n = 1} ^ {\infty} \left(\frac {x ^ {n}}{n}\right) ^ {\prime} = \sum_ {n = 1} ^ {\infty} x ^ {n - 1} = \frac {1}{1 - x}.</equation>注意到 t（0）=0，故<equation>t (x) = t (x) - t (0) = \int_ {0} ^ {x} \frac {1}{1 - t} \mathrm {d} t = - \ln (1 - x).</equation>因此，当<equation>x\in(0,1)</equation>时，<equation>s _ {2} (x) = (1 - x) \ln (1 - x) + x.</equation>当<equation>x = 1</equation>时，<equation>s_{2}(1) = \sum_{n = 1}^{\infty}\frac{1}{n(n + 1)}</equation>.

计算<equation>\sum_{n=1}^{\infty} \frac{1}{n(n+1)}</equation>的部分和<equation>\sum_{n=1}^{k} \frac{1}{n(n+1)}</equation>得<equation>s (x) = \left\{ \begin{array}{l l} \frac {1}{\mathrm {e} ^ {x} - 1} + (1 - x) \ln (1 - x) + x, & x \in (0, 1), \\ \frac {\mathrm {e}}{\mathrm {e} - 1}, & x = 1. \end{array} \right.</equation>（法二）当<equation>x\in (0,1)</equation>时，<equation>s _ {2} ^ {\prime} (x) = \left[ \sum_ {n = 1} ^ {\infty} \frac {x ^ {n + 1}}{n (n + 1)} \right] ^ {\prime} \xlongequal {\text {逐 项 求 导}} \sum_ {n = 1} ^ {\infty} \left[ \frac {x ^ {n + 1}}{n (n + 1)} \right] ^ {\prime} = \sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n}.</equation><equation>s _ {2} ^ {\prime \prime} (x) = \left(\sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n}\right) ^ {\prime} \stackrel {\text {逐 项 求 导}} {=} \sum_ {n = 1} ^ {\infty} \left(\frac {x ^ {n}}{n}\right) ^ {\prime} = \sum_ {n = 1} ^ {\infty} x ^ {n - 1} = \frac {1}{1 - x}.</equation>注意到<equation>s_{2}^{\prime}(0)=0</equation>，故<equation>s _ {2} ^ {\prime} (x) = s _ {2} ^ {\prime} (x) - s _ {2} ^ {\prime} (0) = \int_ {0} ^ {x} \frac {1}{1 - t} \mathrm {d} t = - \ln (1 - t) \Big | _ {0} ^ {x} = - \ln (1 - x).</equation>又因为<equation>s_{2}(0)=0</equation>，所以<equation>\begin{aligned} s _ {2} (x) &= s _ {2} (x) - s _ {2} (0) = \int_ {0} ^ {x} \left[ - \ln (1 - t) \right] \mathrm {d} t = - \left[ t \ln (1 - t) \left| _ {0} ^ {x} - \int_ {0} ^ {x} \frac {- t}{1 - t} \mathrm {d} t \right. \right] \\ &= - x \ln (1 - x) - \int_ {0} ^ {x} \frac {t}{1 - t} \mathrm {d} t = - x \ln (1 - x) - \int_ {0} ^ {x} \left(- 1 + \frac {1}{1 - t}\right) \mathrm {d} t \\ &= - x \ln (1 - x) - \left[ - t - \ln (1 - t) \right] \left| _ {0} ^ {x} = - x \ln (1 - x) + \left[ t + \ln (1 - t) \right] \right| _ {0} ^ {x} \\ &= - x \ln (1 - x) + x + \ln (1 - x) = (1 - x) \ln (1 - x) + x. \end{aligned}</equation>其余同法一.

---

**2020年第17题 | 解答题 | 10分**
17. (本题满分10分)

设数列<equation>\{a_{n}\}</equation>满足：<equation>a_{1}=1,(n+1)a_{n+1}=\left(n+\frac{1}{2}\right)a_{n}</equation>，证明：当<equation>|x|<1</equation>时，幂级数<equation>\sum_{n=1}^{\infty}a_{n}x^{n}</equation>收敛，并求其和函数.
**答案: **证明略，和函数为<equation>S ( x )=\frac{2}{\sqrt{1-x}}-2, x \in(-1,1).</equation>
**解析: **解 计算幂级数的收敛半径 R.由<equation>(n + 1)a_{n + 1} = \left(n + \frac{1}{2}\right)a_n</equation>可得，<equation>\frac{a_n}{a_{n + 1}} = \frac{n + 1}{n + \frac{1}{2}}.</equation><equation>R = \lim _ {n \rightarrow \infty} \left| \frac {a _ {n}}{a _ {n + 1}} \right| = \lim _ {n \rightarrow \infty} \frac {n + 1}{n + \frac {1}{2}} = 1.</equation>因此，幂级数的收敛半径<equation>R=1</equation>当<equation>|x| < 1</equation>时，幂级数<equation>\sum_{n=1}^{\infty} a_{n} x^{n}</equation>收敛下面用两种方法计算和函数<equation>S(x).</equation>（法一）令<equation>S ( x )=\sum_{n=1}^{\infty} a_{n} x^{n}, x\in(-1,1),</equation>，则<equation>\begin{aligned} S ^ {\prime} (x) &= \left(\sum_ {n = 1} ^ {\infty} a _ {n} x ^ {n}\right) ^ {\prime} \xlongequal {\text {逐 项 求 导}} \sum_ {n = 1} ^ {\infty} \left(a _ {n} x ^ {n}\right) ^ {\prime} = \sum_ {n = 1} ^ {\infty} a _ {n} n x ^ {n - 1} = \sum_ {n = 0} ^ {\infty} a _ {n + 1} (n + 1) x ^ {n} \\ &= 1 + \sum_ {n = 1} ^ {\infty} (n + 1) a _ {n + 1} x ^ {n} \xlongequal {(n + 1) a _ {n + 1} = \left(n + \frac {1}{2}\right) a _ {n}} 1 + \sum_ {n = 1} ^ {\infty} \left(n + \frac {1}{2}\right) a _ {n} x ^ {n} \\ &= 1 + x \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n - 1} + \frac {1}{2} \sum_ {n = 1} ^ {\infty} a _ {n} x ^ {n} = 1 + x S ^ {\prime} (x) + \frac {1}{2} S (x). \end{aligned}</equation>于是，<equation>S ( x )</equation>满足微分方程<equation>y^{\prime}=1+xy^{\prime}+\frac{1}{2} y</equation>即<equation>( 1-x)y^{\prime}-\frac{1}{2} y=1.</equation>整理可得<equation>y^{\prime}-\frac{1}{2(1-x)}y</equation><equation>= \frac{1}{1 - x}.</equation>这是一个一阶非齐次线性微分方程.由求解公式可得<equation>\begin{aligned} S (x) &= \mathrm {e} ^ {\int \frac {1}{2 (1 - x)} \mathrm {d} x} \left[ \int \frac {1}{1 - x} \cdot \mathrm {e} ^ {\int \frac {1}{2 (x - 1)} \mathrm {d} x} \mathrm {d} x + C \right] \xlongequal {\mid x - 1 \mid = 1 - x} \mathrm {e} ^ {- \frac {1}{2} \ln (1 - x)} \left[ \int \frac {1}{1 - x} \cdot \mathrm {e} ^ {\frac {1}{2} \ln (1 - x)} \mathrm {d} x + C \right] \\ &= \frac {1}{\sqrt {1 - x}} \left(\int \frac {1}{1 - x} \cdot \sqrt {1 - x} \mathrm {d} x + C\right) = \frac {1}{\sqrt {1 - x}} \left(\int \frac {1}{\sqrt {1 - x}} \mathrm {d} x + C\right) \\ &= \frac {1}{\sqrt {1 - x}} (- 2 \sqrt {1 - x} + C) = \frac {C}{\sqrt {1 - x}} - 2, \end{aligned}</equation>其中 C为待定常数.

当<equation>x = 0</equation>时，<equation>S(0) = 0</equation>，故<equation>0 = \frac{C}{1} -2.</equation>解得<equation>C = 2.</equation>因此，<equation>S ( x ) = \frac { 2 } { \sqrt { 1 - x } } - 2 , x \in (- 1, 1 ) .</equation>（法二）由<equation>(n + 1)a_{n + 1} = \left(n + \frac{1}{2}\right)a_n</equation>可得<equation>\frac{a_{n + 1}}{a_n} = \frac{n + \frac{1}{2}}{n + 1} = \frac{2(n + 1) - 1}{2(n + 1)}</equation>，且<equation>a_2 = \frac{3}{4}</equation>. 于是，<equation>a _ {n} = \frac {a _ {n}}{a _ {n - 1}} \cdot \frac {a _ {n - 1}}{a _ {n - 2}} \dots \frac {a _ {2}}{a _ {1}} = \frac {2 n - 1}{2 n} \cdot \frac {2 n - 3}{2 n - 2} \dots \frac {3}{4} = 2 \cdot \frac {(2 n - 1) ! !}{(2 n) ! !}.</equation>记<equation>S(x) = \sum_{n = 1}^{\infty} a_n x^n, x \in (-1, 1)</equation>，则<equation>S(x) = 2\sum_{n = 1}^{\infty} \frac{(2n - 1)!!}{(2n)!!} x^n.</equation><equation>\begin{aligned} S ^ {\prime} (x) &= \sum_ {n = 1} ^ {\infty} \frac {(2 n - 1) ! !}{(2 n) ! !} \cdot 2 n x ^ {n - 1} = \sum_ {n = 1} ^ {\infty} \frac {(2 n - 1) ! !}{(2 n - 2) ! !} x ^ {n - 1} = \sum_ {n = 0} ^ {\infty} \frac {(2 n + 1) ! !}{(2 n) ! !} x ^ {n} \\ &= 1 + \sum_ {n = 1} ^ {\infty} \frac {(2 n + 1) ! !}{(2 n) ! !} x ^ {n} = 1 + \sum_ {n = 1} ^ {\infty} \frac {(2 n - 1) ! ! \cdot (2 n + 1)}{(2 n) ! !} x ^ {n} \\ &= 1 + \sum_ {n = 1} ^ {\infty} \frac {(2 n - 1) ! !}{(2 n) ! !} \cdot 2 n x ^ {n} + \sum_ {n = 1} ^ {\infty} \frac {(2 n - 1) ! !}{(2 n) ! !} x ^ {n} \\ &= 1 + x \sum_ {n = 1} ^ {\infty} \frac {(2 n - 1) ! !}{(2 n - 2) ! !} x ^ {n - 1} + \frac {1}{2} S (x) = 1 + x S ^ {\prime} (x) + \frac {1}{2} S (x). \end{aligned}</equation>其余同法一.

---

**2019年第11题 | 填空题 | 4分**
11. 幂级数<equation>\sum_{n=0}^{\infty} \frac{(-1)^{n}}{(2 n)!} x^{n}</equation>在<equation>(0,+\infty)</equation>内的和函数<equation>S(x)=</equation>___
**答案: **cos<equation>\sqrt{x}.</equation>
**解析: **解 由于<equation>\sum_{n=0}^{\infty} \frac{(-1)^{n}}{(2n)!} x^{n}=\sum_{n=0}^{\infty} \frac{(-1)^{n}}{(2n)!} (\sqrt{x})^{2n}</equation>，而<equation>\cos x</equation>的幂级数展开式为<equation>\cos x=\sum_{n=0}^{\infty} \frac{(-1)^{n}}{(2n)!} x^{2n}(-\infty < x < +\infty)</equation>，故幂级数<equation>\sum_{n=0}^{\infty} \frac{(-1)^{n}}{(2n)!} x^{n}</equation>在（0，<equation>+\infty</equation>）内的和函数<equation>S(x)=\cos \sqrt{x}.</equation>

---

**2018年第3题 | 选择题 | 4分 | 答案: B**
3.<equation>\sum_{n=0}^{\infty}(-1)^{n}\frac{2n+3}{(2n+1)!}=</equation>(    )

A.<equation>\sin 1+\cos 1</equation>B.<equation>2\sin 1+\cos 1</equation>C.<equation>2\sin 1+2\cos 1</equation>D.<equation>2\sin 1+3\cos 1</equation>
答案: B
**解析: **解 由于在<equation>(-\infty, +\infty)</equation>上，<equation>\sin x=\sum_{n=0}^{\infty}\frac{(-1)^{n}}{(2n+1)!}x^{2n+1},\cos x=\sum_{n=0}^{\infty}\frac{(-1)^{n}}{(2n)!}x^{2n}</equation>，故<equation>\sin 1=\sum_{n=0}^{\infty}\frac{(-1)^{n}}{(2n+1)!},\cos 1=\sum_{n=0}^{\infty}\frac{(-1)^{n}}{(2n)!}.</equation>因此，<equation>\sum_{n=0}^{\infty}(-1)^{n}\frac{2n+3}{(2n+1)!}=\sum_{n=0}^{\infty}(-1)^{n}\frac{2+2n+1}{(2n+1)!}=2\sum_{n=0}^{\infty}\frac{(-1)^{n}}{(2n+1)!}+\sum_{n=0}^{\infty}\frac{(-1)^{n}}{(2n)!}</equation><equation>= 2\sin 1+\cos 1.</equation>应选B.

---

**2017年第12题 | 填空题 | 4分**
12. 幂级数<equation>\sum_{n=1}^{\infty} (-1)^{n-1} nx^{n-1}</equation>在区间<equation>(-1, 1)</equation>内的和函数<equation>S(x) =</equation>___
**答案: **<equation>\frac {1}{(1 + x) ^ {2}}.</equation>
**解析: **解幂级数<equation>\sum_{n=1}^{\infty}(-1)^{n-1} n x^{n-1}</equation>的收敛域为<equation>(-1,1).</equation>当<equation>-1 < x < 1</equation>时，<equation>\int_{0}^{x} S(t)\mathrm{d} t=\int_{0}^{x}\sum_{n=1}^{\infty}(-1)^{n-1} n t^{n-1}\mathrm{d} t=\sum_{n=1}^{\infty}\int_{0}^{x}(-1)^{n-1} n t^{n-1}\mathrm{d} t=\sum_{n=1}^{\infty}(-1)^{n-1} x^{n}=\frac{x}{1+x},</equation>从而<equation>S(x)=\left(\frac{x}{1+x}\right)^{\prime}=\frac{1}{(1+x)^{2}}.</equation>

---

**2013年第16题 | 解答题 | 10分**
16. (本题满分10分)

设数列<equation>\{a_{n}\}</equation>满足条件：<equation>a_{0}=3,a_{1}=1,a_{n-2}-n(n-1)a_{n}=0(n\geqslant2),S(x)</equation>是幂级数<equation>\sum_{n=0}^{\infty}a_{n}x^{n}</equation>的和函数.

I. 证明<equation>S^{\prime\prime}(x)-S(x)=0;</equation>II. 求 S(x)的表达式.
**答案: **(16) （I）证明略；

（Ⅱ）<equation>S ( x )=2 \mathrm{e}^{x}+\mathrm{e}^{-x}.</equation>
**解析: **解（I）由题设知，<equation>a_{n}=\frac{1}{n(n-1)}a_{n-2}, n\geqslant 2</equation>递推得到<equation>a _ {2 n} = \frac {1}{(2 n) !} a _ {0} = \frac {3}{(2 n) !}, \quad a _ {2 n + 1} = \frac {1}{(2 n + 1) !} a _ {1} = \frac {1}{(2 n + 1) !}, \quad n = 0, 1, 2, \dots .</equation>当<equation>n = 2m,m\in \mathbf{N}</equation>时，<equation>\frac{a_{n + 1}}{a_n} = \frac{a_{2m + 1}}{a_{2m}} = \frac{1}{3(2m + 1)} = \frac{1}{3(n + 1)}</equation>；

当<equation>n = 2m + 1,m\in \mathbf{N}</equation>时，<equation>\frac{a_{n+1}}{a_n}=\frac{a_{2m+2}}{a_{2m+1}}=\frac{3}{2m+2}=\frac{3}{n+1}.</equation>因此<equation>\lim_{n\to \infty}\frac{a_{n + 1}}{a_n} = 0</equation>，从而<equation>\sum_{n = 0}^{\infty}a_nx^n</equation>的收敛半径为<equation>+\infty</equation>. 于是在<equation>(-\infty , + \infty)</equation>上可对<equation>\sum_{n = 0}^{\infty}a_nx^n</equation>逐项求导，即<equation>S ^ {\prime} (x) = \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n - 1},</equation><equation>S ^ {\prime \prime} (x) = \sum_ {n = 2} ^ {\infty} n (n - 1) a _ {n} x ^ {n - 2} = \sum_ {n = 0} ^ {\infty} (n + 2) (n + 1) a _ {n + 2} x ^ {n}.</equation>由<equation>a_{n - 2} - n(n - 1)a_n = 0(n\geqslant 2)</equation>知，<equation>a_{n} - (n + 2)(n + 1)a_{n + 2} = 0(n\in \mathbf{N})</equation>，从而<equation>\begin{aligned} S ^ {\prime \prime} (x) - S (x) &= \sum_ {n = 0} ^ {\infty} (n + 2) (n + 1) a _ {n + 2} x ^ {n} - \sum_ {n = 0} ^ {\infty} a _ {n} x ^ {n} \\ &= \sum_ {n = 0} ^ {\infty} \left[ (n + 2) (n + 1) a _ {n + 2} - a _ {n} \right] x ^ {n} = 0. \end{aligned}</equation>结论得证.

（Ⅱ）二阶常系数齐次线性微分方程<equation>S^{\prime \prime}(x)-S(x)=0</equation>的特征方程为<equation>\lambda^{2}-1=0</equation>，解得<equation>\lambda=\pm1</equation>从而<equation>S (x) = C _ {1} \mathrm {e} ^ {x} + C _ {2} \mathrm {e} ^ {- x}, \quad C _ {1}, C _ {2} \text {为待定常数}.</equation>将<equation>S (0)=a_{0}=3,S^{\prime}(0)=a_{1}=1</equation>代入上式，得到<equation>C_{1}+C_{2}=3,C_{1}-C_{2}=1</equation>解得<equation>C_{1}=2,C_{2}=1.</equation>因此<equation>S (x) = 2 \mathrm {e} ^ {x} + \mathrm {e} ^ {- x}.</equation>

---

**2012年第17题 | 解答题 | 10分**
17. (本题满分10分)

求幂级数<equation>\sum_ {n = 0} ^ {\infty} \frac {4 n ^ {2} + 4 n + 3}{2 n + 1} x ^ {2}</equation>的收敛域及和函数.
**答案: **(17) 收敛域为（-1，1），和函数为<equation>S(x) = \left\{\begin{array}{ll}\frac{1+x^{2}}{(1-x^{2})^{2}}+\frac{1}{x}\ln\frac{1+x}{1-x}, & -1<x<1 \text{且} x\neq 0, \\ 3, & x=0.\end{array}\right.</equation>
**解析: **解 令<equation>u_{n}(x)=\frac{4 n^{2}+4 n+3}{2 n+1} x^{2 n}</equation>，则<equation>u_{n+1}(x)=\frac{4(n+1)^{2}+4(n+1)+3}{2(n+1)+1} x^{2(n+1)}</equation>，从而<equation>\lim_{n\to \infty}\left| \frac{u_{n+1}(x)}{u_{n}(x)} \right|=x^{2}.</equation>由比值审敛法知，当<equation>|x| < 1</equation>时，原幂级数收敛；当<equation>|x| > 1</equation>时，原幂级数发散，从而收敛半径为1.

当<equation>x=\pm 1</equation>时，<equation>\sum_{n=0}^{\infty}\frac{4n^{2}+4n+3}{2n+1}x^{2n}=\sum_{n=0}^{\infty}\frac{4n^{2}+4n+3}{2n+1}.</equation>又<equation>\lim_{n\to\infty}\frac{4n^{2}+4n+3}{2n+1}=\infty\neq0</equation>，故原幂级数发散.

综上所述，幂级数<equation>\sum_{n=0}^{\infty} \frac{4 n^{2}+4 n+3}{2 n+1} x^{2 n}</equation>的收敛域为（-1，1）.

令<equation>S ( x )=\sum_{n=0}^{\infty}\frac{4 n^{2}+4 n+3}{2 n+1} x^{2 n}(-1<x<1)</equation>，则<equation>S (x) = \sum_ {n = 0} ^ {\infty} \frac {\left(2 n + 1\right) ^ {2} + 2}{2 n + 1} x ^ {2 n} = \sum_ {n = 0} ^ {\infty} (2 n + 1) x ^ {2 n} + \sum_ {n = 0} ^ {\infty} \frac {2}{2 n + 1} x ^ {2 n}.</equation>当<equation>- 1 < x < 1</equation>时，<equation>\sum_ {n = 0} ^ {\infty} (2 n + 1) x ^ {2 n} = \sum_ {n = 0} ^ {\infty} \left(x ^ {2 n + 1}\right) ^ {\prime} = \left(\sum_ {n = 0} ^ {\infty} x ^ {2 n + 1}\right) ^ {\prime} = \left(\frac {x}{1 - x ^ {2}}\right) ^ {\prime} = \frac {1 + x ^ {2}}{\left(1 - x ^ {2}\right) ^ {2}}.</equation>当<equation>- 1 < x < 1</equation>且<equation>x\neq 0</equation>时，<equation>\sum_ {n = 0} ^ {\infty} \frac {2}{2 n + 1} x ^ {2 n} = \frac {2}{x} \sum_ {n = 0} ^ {\infty} \frac {1}{2 n + 1} x ^ {2 n + 1}.</equation>注意这里 x要作分母，故需分情况 x≠0与 x=0来讨论.

又<equation>\left(\sum_{n = 0}^{\infty}\frac{1}{2n + 1} x^{2n + 1}\right)^{\prime} = \sum_{n = 0}^{\infty}\left(\frac{1}{2n + 1} x^{2n + 1}\right)^{\prime} = \sum_{n = 0}^{\infty}x^{2n} = \frac{1}{1 - x^2}</equation>，故<equation>\sum_ {n = 0} ^ {\infty} \frac {1}{2 n + 1} x ^ {2 n + 1} = \int_ {0} ^ {x} \frac {1}{1 - t ^ {2}} \mathrm {d} t = \frac {1}{2} \ln \frac {1 + x}{1 - x}.</equation>从而<equation>\sum_ {n = 0} ^ {\infty} \frac {2}{2 n + 1} x ^ {2 n} = \frac {1}{x} \ln \frac {1 + x}{1 - x}, - 1 < x < 1 \text {且} x \neq 0.</equation>当<equation>x = 0</equation>时，<equation>\sum_{n = 0}^{\infty}\frac{2}{2n + 1} x^{2n} = 2,\sum_{n = 0}^{\infty}(2n + 1)x^{2n} = 1</equation>，故<equation>S(0) = 3.</equation>综上所述，<equation>S(x) = \left\{ \begin{array}{ll} \frac{1 + x^{2}}{(1 - x^{2})^{2}} + \frac{1}{x} \ln \frac{1 + x}{1 - x}, & -1 < x < 1 \text{且} x \neq 0, \\ 3, & x = 0. \end{array}\right.</equation>

---

**2010年第18题 | 解答题 | 10分**
18. (本题满分10分）

求幂级数<equation>\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{2 n-1} x^{2 n}</equation>的收敛域及和函数.
**答案: **(18) 收敛域为<equation>[-1,1]</equation>，和函数为<equation>x\arctan x(-1\leqslant x\leqslant 1)</equation>
**解析: **解 令<equation>u_{n}(x) = \frac{(-1)^{n - 1}}{2n - 1} x^{2n}</equation>，则<equation>\lim _ {n \rightarrow \infty} \left| \frac {u _ {n + 1} (x)}{u _ {n} (x)} \right| = \lim _ {n \rightarrow \infty} \left| \frac {\frac {(- 1) ^ {n}}{2 n + 1} x ^ {2 n + 2}}{\frac {(- 1) ^ {n - 1}}{2 n - 1} x ^ {2 n}} \right| = \lim _ {n \rightarrow \infty} \left| \frac {2 n - 1}{2 n + 1} x ^ {2} \right| = x ^ {2}.</equation>由比值审敛法可知，当<equation>|x| < 1</equation>时，<equation>\sum_{n = 1}^{\infty}u_n(x)</equation>收敛；当<equation>|x| > 1</equation>时，<equation>\sum_{n = 1}^{\infty}u_n(x)</equation>发散，于是<equation>\sum_{n = 1}^{\infty}u_n(x)</equation>的收敛半径为1.又当<equation>x = \pm 1</equation>时，由莱布尼茨定理知，<equation>\sum_{n = 1}^{\infty}u_n(\pm 1) = \sum_{n = 1}^{\infty}\frac{(-1)^{n - 1}}{2n - 1}</equation>收敛.因此幂级数<equation>\sum_{n = 1}^{\infty}\frac{(-1)^{n - 1}}{2n - 1} x^{2n}</equation>的收敛域为<equation>[-1,1]</equation>令<equation>S(x) = \sum_{n = 1}^{\infty}\frac{(-1)^{n - 1}}{2n - 1} x^{2n}, S_{1}(x) = \sum_{n = 1}^{\infty}\frac{(-1)^{n - 1}}{2n - 1} x^{2n - 1}, -1\leqslant x\leqslant 1</equation>，则<equation>S(x) = xS_{1}(x)</equation>下面用两种方法求<equation>S_{1}(x)</equation>（法一）由<equation>\arctan x</equation>的麦克劳林展开式知，<equation>S _ {1} (x) = \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1}}{2 n - 1} x ^ {2 n - 1} = \arctan x, - 1 \leqslant x \leqslant 1.</equation>（法二）当<equation>- 1 < x < 1</equation>时，<equation>\begin{aligned} S _ {1} ^ {\prime} (x) &= \left[ \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1}}{2 n - 1} x ^ {2 n - 1} \right] ^ {\prime} = \sum_ {n = 1} ^ {\infty} \left[ \frac {(- 1) ^ {n - 1}}{2 n - 1} x ^ {2 n - 1} \right] ^ {\prime} \\ &= \sum_ {n = 1} ^ {\infty} (- 1) ^ {n - 1} x ^ {2 n - 2} = \frac {1}{1 + x ^ {2}}. \end{aligned}</equation>注意逐项求导后所得幂级数的收敛半径不变，但在端点处的敛散性可能会发生变化，所以在收敛区间（-1，1）上进行讨论.

由于<equation>S_{1}(0) = 0</equation>，故<equation>S_{1}(x) = \int_{0}^{x}\frac{1}{1 + t^{2}}\mathrm{d}t = \arctan x, - 1 < x < 1.</equation>又和函数<equation>S_{1}(x)</equation>在其收敛域[-1,1]上连续，且<equation>\arctan x</equation>在[-1,1]上连续，故<equation>S_{1}(x) = \arctan x, - 1\leqslant x\leqslant 1.</equation>综上所述，<equation>S ( x ) = x S_{1} ( x ) = x \arctan x, - 1 \leqslant x \leqslant 1.</equation>

---

**2009年第16题 | 解答题 | 10分**
16. (本题满分9分)

设 a n为曲线 y=x n与 y=x<equation>^{n+1}</equation>（ n=1,2,<equation>\cdots</equation>）所围成区域的面积，记<equation>S_{1}=\sum_{n=1}^{\infty} a_{n}, S_{2}=\sum_{n=1}^{\infty} a_{2n-1}</equation>，求<equation>S_{1}</equation>与<equation>S_{2}</equation>的值.
**解析: **解曲线<equation>y=x^{n}</equation>与<equation>y=x^{n+1}</equation>交于两点（0，0），（1，1），它们所围成区域的面积为<equation>a _ {n} = \int_ {0} ^ {1} \left(x ^ {n} - x ^ {n + 1}\right) \mathrm {d} x = \left. \left(\frac {x ^ {n + 1}}{n + 1} - \frac {x ^ {n + 2}}{n + 2}\right) \right| _ {0} ^ {1} = \frac {1}{n + 1} - \frac {1}{n + 2}.</equation>级数<equation>\sum_{n=1}^{\infty} a_{n}</equation>的前k项和为<equation>\sum_ {n = 1} ^ {k} a _ {n} = \left(\frac {1}{2} - \frac {1}{3}\right) + \left(\frac {1}{3} - \frac {1}{4}\right) + \dots + \left(\frac {1}{k + 1} - \frac {1}{k + 2}\right) = \frac {1}{2} - \frac {1}{k + 2},</equation>于是<equation>S_{1}=\lim_{k\to \infty}\sum_{n=1}^{k}a_{n}=\lim_{k\to \infty}\left(\frac{1}{2}-\frac{1}{k+2}\right)=\frac{1}{2}.</equation>又<equation>S _ {2} = \sum_ {n = 1} ^ {\infty} a _ {2 n - 1} = \sum_ {n = 1} ^ {\infty} \left(\frac {1}{2 n} - \frac {1}{2 n + 1}\right) = \frac {1}{2} - \frac {1}{3} + \frac {1}{4} - \frac {1}{5} + \dots + \frac {1}{2 n} - \frac {1}{2 n + 1} + \dots ,</equation>而<equation>\ln (1 + x)</equation>的麦克劳林展开式为<equation>\ln (1 + x) = \sum_{n = 1}^{\infty}\frac{(-1)^{n - 1}}{n} x^n,x\in(-1,1]</equation>，故令<equation>x = 1</equation>，得<equation>\ln 2 = 1 - \frac {1}{2} + \frac {1}{3} - \frac {1}{4} + \dots - \frac {1}{2 n} + \frac {1}{2 n + 1} - \dots ,</equation>从而<equation>S_{2}=-(\ln 2-1)=1-\ln 2.</equation>综上所述，<equation>S_{1}=\frac{1}{2}, S_{2}=1-\ln 2.</equation>

---


