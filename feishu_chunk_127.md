#### 幂级数

**2024年第4题 | 选择题 | 5分 | 答案: A**

4. 已知幂级数<equation>\sum_{n=0}^{\infty} a_{n} x^{n}</equation>的和函数为<equation>\ln(2+x)</equation>，则<equation>\sum_{n=0}^{\infty} n a_{2n}=(\quad)</equation>A.<equation>-\frac{1}{6}</equation>B.<equation>-\frac{1}{3}</equation>C.<equation>\frac{1}{6}</equation>D.<equation>\frac{1}{3}</equation>

答案: A

**解析:**解（法一）由<equation>\ln (1 + x) = \sum_{n = 1}^{\infty}(-1)^{n - 1}\frac{x^n}{n}(-1 < x\leqslant 1)</equation>可得<equation>\ln (2 + x) = \ln \left[ 2 \cdot \left(1 + \frac {x}{2}\right) \right] = \ln 2 + \ln \left(1 + \frac {x}{2}\right) = \ln 2 + \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1}}{n} \left(\frac {x}{2}\right) ^ {n}.</equation>由此可得，当<equation>n > 0</equation>时，<equation>x^{2n}</equation>的系数为<equation>a_{2n}=\frac{(-1)^{2n-1}}{2n2^{2n}}=\frac{-1}{2n2^{2n}}.</equation>因此，<equation>\sum_ {n = 0} ^ {\infty} n a _ {2 n} = \sum_ {n = 1} ^ {\infty} n a _ {2 n} = \sum_ {n = 1} ^ {\infty} \frac {- n}{2 n 2 ^ {2 n}} = \sum_ {n = 1} ^ {\infty} \frac {- 1}{2 ^ {2 n + 1}} = \frac {- \frac {1}{8}}{1 - \frac {1}{4}} = - \frac {1}{6}.</equation>应选A.

（法二）由<equation>\sum_{n = 0}^{\infty}a_nx^n = \ln (2 + x)</equation>可得<equation>\sum_{n = 0}^{\infty}a_n(-x)^n = \sum_{n = 0}^{\infty}(-1)^n a_nx^n = \ln (2 - x)</equation>.由此可得<equation>\sum_{n = 0}^{\infty}[1 + (-1)^n]a_nx^n = \ln (2 + x) + \ln (2 - x)</equation>，即<equation>2 \sum_ {n = 0} ^ {\infty} a _ {2 n} x ^ {2 n} = \ln (2 + x) + \ln (2 - x).</equation>对（1）式两端关于<equation>x</equation>求导可得，<equation>4 \sum_ {n = 1} ^ {\infty} n a _ {2 n} x ^ {2 n - 1} = \frac {1}{2 + x} - \frac {1}{2 - x}.</equation>在(2)式中令<equation>x = 1</equation>，可得<equation>4\sum_{n = 1}^{\infty}na_{2n} = \frac{1}{3} -1 = -\frac{2}{3}</equation>，进一步可得<equation>\sum_{n = 0}^{\infty}na_{2n} = -\frac{1}{6}</equation>因此，应选A.

（法三）注意到<equation>\left[ \ln (2 + x) \right] ^ {\prime} = \frac {1}{2 + x} = \frac {1}{2 \left(1 + \frac {x}{2}\right)} = \frac {1}{2} \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} \left(\frac {x}{2}\right) ^ {n},</equation>该幂级数的收敛半径为2，故在（-2，2）上，由牛顿一莱布尼茨公式可得<equation>\begin{aligned} \ln (2 + x) - \ln 2 &= \int_ {0} ^ {x} \left[ \ln (2 + t) \right] ^ {\prime} \mathrm {d} t = \int_ {0} ^ {x} \frac {1}{2} \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} \left(\frac {t}{2}\right) ^ {n} \mathrm {d} t \\ \frac {\text {逐 项 积 分}}{} \frac {1}{2} \sum_ {n = 0} ^ {\infty} \int_ {0} ^ {x} (- 1) ^ {n} \left(\frac {t}{2}\right) ^ {n} \mathrm {d} t &= \frac {1}{2} \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{n + 1} \cdot \frac {x ^ {n + 1}}{2 ^ {n}} \\ &= \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1} x ^ {n}}{n 2 ^ {n}}. \end{aligned}</equation>因此，<equation>\ln (2 + x) = \ln 2 + \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1} x ^ {n}}{n 2 ^ {n}}.</equation>其余同法一.

---

**2023年第13题 | 填空题 | 5分**

13.<equation>3. \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n}}{(2 n) !} = \underline {{}}</equation>

**答案:**<equation>\frac {\mathrm {e} ^ {x} + \mathrm {e} ^ {- x}}{2}.</equation>

**解析:**解（法一）考虑<equation>\mathrm{e}^{x}</equation>与<equation>\mathrm{e}^{-x}</equation>的幂级数展开式，<equation>\mathrm {e} ^ {x} = \sum_ {n = 0} ^ {\infty} \frac {x ^ {n}}{n !}, \quad \mathrm {e} ^ {- x} = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n} x ^ {n}}{n !}, \quad - \infty < x < + \infty .</equation>由此可得<equation>\mathrm {e} ^ {x} + \mathrm {e} ^ {- x} = \sum_ {n = 0} ^ {\infty} \frac {x ^ {n}}{n !} + \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n} x ^ {n}}{n !} = \sum_ {n = 0} ^ {\infty} \frac {\left[ 1 + (- 1) ^ {n} \right] x ^ {n}}{n !} = 2 \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n}}{(2 n) !}.</equation>因此，<equation>\sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n}}{(2 n) !} = \frac {\mathrm {e} ^ {x} + \mathrm {e} ^ {- x}}{2}.</equation>（法二）当 x=0时，<equation>\sum_{n=0}^{\infty}\frac{x^{2n}}{(2n)!}</equation>显然收敛. 又当 x≠0时，<equation>\lim _ {n \rightarrow \infty} \frac {x ^ {2 n + 2}}{(2 n + 2) !} \cdot \frac {(2 n) !}{x ^ {2 n}} = \lim _ {n \rightarrow \infty} \frac {x ^ {2}}{(2 n + 1) (2 n + 2)} = 0.</equation>由正项级数的比值审敛法可知，对任意<equation>x\neq 0</equation>，都有<equation>\sum_{n=0}^{\infty}\frac{x^{2n}}{(2n)!}</equation>收敛.因此，幂级数<equation>\sum_{n=0}^{\infty}\frac{x^{2n}}{(2n)!}</equation>的收敛域为<equation>(-\infty, +\infty).</equation>记<equation>\sum_{n=0}^{\infty}\frac{x^{2n}}{(2n)!}</equation>的和函数为 S(x)，则在<equation>(-\infty, +\infty)</equation>上，<equation>S ^ {\prime} (x) = \left[ \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n}}{(2 n) !} \right] ^ {\prime} \xlongequal {\text {逐 项 求 导}} \sum_ {n = 0} ^ {\infty} \frac {\left(x ^ {2 n}\right) ^ {\prime}}{(2 n) !} = \sum_ {n = 1} ^ {\infty} \frac {x ^ {2 n - 1}}{(2 n - 1) !},</equation><equation>S ^ {\prime \prime} (x) = \left[ \sum_ {n = 1} ^ {\infty} \frac {x ^ {2 n - 1}}{(2 n - 1) !} \right] ^ {\prime} \xlongequal {\text {逐 项 求 导}} \sum_ {n = 1} ^ {\infty} \frac {\left(x ^ {2 n - 1}\right) ^ {\prime}}{(2 n - 1) !} = \sum_ {n = 1} ^ {\infty} \frac {x ^ {2 n - 2}}{(2 n - 2) !} = \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n}}{(2 n) !}.</equation>由此可得，<equation>S^{\prime \prime}(x)=S(x), S(x)</equation>满足微分方程<equation>y^{\prime \prime}-y=0.</equation>这是一个二阶常系数齐次线性微分方程，其特征方程为<equation>r^{2}-1=0</equation>，特征根为<equation>r_{1,2}=\pm 1.</equation>从而通解为<equation>y=C_{1}\mathrm{e}^{x}+C_{2}\mathrm{e}^{-x}</equation>即<equation>S(x)=C_{1}\mathrm{e}^{x}+C_{2}\mathrm{e}^{-x}.</equation>将 x = 0 代入<equation>S ( x )=\sum_{n=0}^{\infty}\frac{x^{2 n}} {(2 n)!}, S^{\prime} ( x )=\sum_{n=1}^{\infty}\frac{x^{2 n-1}} {(2 n-1)!}</equation>可得，<equation>S ( 0 )=1, S^{\prime} ( 0 )=0.</equation>另一方面，由<equation>S ( x )=C_{1}\mathrm{e}^{x}+C_{2}\mathrm{e}^{-x}</equation>可得，<equation>S ( 0 )=C_{1}+C_{2}, S^{\prime} ( 0 )=\left(C_{1}\mathrm{e}^{x}-C_{2}\mathrm{e}^{-x}\right)\mid_{x=0}=C_{1}-C_{2}.</equation>于是，解得<equation>\left\{\begin{array}{l l} C_{1}+C_{2}=1, \\ C_{1}-C_{2}=0. \end{array} \right.</equation>因此，<equation>S ( x ) = \frac {\mathrm {e}^{x} + \mathrm {e}^{-x}}{2}.</equation>

---

**2022年第20题 | 解答题 | 12分**

20. （本题满分12分）

求幂级数<equation>\sum_ {n = 0} ^ {\infty} \frac {(- 4) ^ {n} + 1}{4 ^ {n} (2 n + 1)} x</equation>的收敛域及和函数 S(x).

**答案:**收敛域为<equation>[-1,1]</equation>，和函数<equation>S ( x )=\left\{\begin{array}{ll}\frac{\arctan x}{x}+\frac{1}{x}\ln \frac{2+x}{2-x},&x\in[-1,0)\cup(0,1],\\ 2,&x=0.\end{array}\right.</equation>

**解析:**先求收敛域.

原级数是一个缺项型幂级数，我们用比值法来求它的收敛半径.<equation>\lim _ {n \rightarrow \infty} \left| \frac {\frac {(- 4) ^ {n + 1} + 1}{4 ^ {n + 1} (2 n + 3)} x ^ {2 n + 2}}{\frac {(- 4) ^ {n} + 1}{4 ^ {n} (2 n + 1)} x ^ {2 n}} \right| = \lim _ {n \rightarrow \infty} \left| \frac {(- 4) ^ {n + 1} + 1}{(- 4) ^ {n} + 1} \cdot \frac {2 n + 1}{4 (2 n + 3)} \right| x ^ {2} = x ^ {2}.</equation>由比值审敛法可知，当<equation>| x | < 1</equation>时，原幂级数收敛；当<equation>| x | > 1</equation>时，原幂级数发散，从而收敛半径为1，收敛区间为（-1，1）.

又由于当<equation>x=\pm 1</equation>时，<equation>\text {原 幂 级 数} = \sum_ {n = 0} ^ {\infty} \frac {(- 4) ^ {n} + 1}{4 ^ {n} (2 n + 1)} = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{2 n + 1} + \sum_ {n = 0} ^ {\infty} \frac {1}{4 ^ {n} (2 n + 1)},</equation>而级数<equation>\sum_{n=0}^{\infty} \frac{(-1)^{n}}{2n+1}</equation>和<equation>\sum_{n=0}^{\infty} \frac{1}{4^{n}(2n+1)}</equation>均收敛，故原幂级数收敛。因此，原幂级数的收敛域为<equation>[-1,1]</equation>下面求和函数.

记<equation>S ( x )=\sum_{n=0}^{\infty}\frac{(-4)^{n}+1}{4^{n}(2n+1)} x^{2n}, x\in[-1,1],</equation>，则<equation>S (x) = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{2 n + 1} x ^ {2 n} + \sum_ {n = 0} ^ {\infty} \frac {1}{4 ^ {n} (2 n + 1)} x ^ {2 n}.</equation>记<equation>S_{1}(x)=\sum_{n=0}^{\infty}\frac{(-1)^{n}}{2n+1} x^{2n}, S_{2}(x)=\sum_{n=0}^{\infty}\frac{1}{4^{n}(2n+1)} x^{2n}</equation>，则当 x<equation>\in[ -1,1]</equation>时，<equation>S (x) = S _ {1} (x) + S _ {2} (x).</equation>注意到<equation>x S_{1}(x)=\sum_{n=0}^{\infty}\frac{(-1)^{n}}{2n+1} x^{2n+1}</equation>，故<equation>\begin{aligned} \left[ x S _ {1} (x) \right] ^ {\prime} &= \left[ \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{2 n + 1} x ^ {2 n + 1} \right] ^ {\prime} \xlongequal {\text {逐 项 求 导}} \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n}}{2 n + 1} \left(x ^ {2 n + 1}\right) ^ {\prime} = \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} x ^ {2 n} \\ &= \frac {1}{1 + x ^ {2}}, \end{aligned}</equation><equation>x S _ {1} (x) = x S _ {1} (x) - 0 \times S _ {1} (0) = \int_ {0} ^ {x} \left[ t S _ {1} (t) \right] ^ {\prime} \mathrm {d} t = \int_ {0} ^ {x} \frac {1}{1 + t ^ {2}} \mathrm {d} t = \arctan x.</equation>当<equation>x \in[ - 1,0)\cup(0,1]</equation>时，<equation>S_{1}(x)=\frac{\arctan x}{x}</equation>当 x=0时，<equation>S_{1}(0)=\frac{(-1)^{0}}{2\times 0+1}=1.</equation>注意到<equation>x S_{2}(x)=\sum_{n=0}^{\infty}\frac{1}{4^{n}(2n+1)} x^{2n+1}</equation>，故<equation>\begin{aligned} \left[ x S _ {2} (x) \right] ^ {\prime} &= \left[ \sum_ {n = 0} ^ {\infty} \frac {1}{4 ^ {n} (2 n + 1)} x ^ {2 n + 1} \right] ^ {\prime} \stackrel {\mathrm {逐 项 求 导}} {=} \sum_ {n = 0} ^ {\infty} \frac {1}{4 ^ {n} (2 n + 1)} \left(x ^ {2 n + 1}\right) ^ {\prime} \\ &= \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n}}{4 ^ {n}} = \sum_ {n = 0} ^ {\infty} \left(\frac {x}{2}\right) ^ {2 n} = \frac {1}{1 - \left(\frac {x}{2}\right) ^ {2}} = \frac {4}{4 - x ^ {2}} \\ &= \frac {1}{2 - x} + \frac {1}{2 + x}, \end{aligned}</equation><equation>\begin{aligned} x S _ {2} (x) &= x S _ {2} (x) - 0 \times S _ {2} (0) = \int_ {0} ^ {x} \left[ t S _ {2} (t) \right] ^ {\prime} \mathrm {d} t = \int_ {0} ^ {x} \left(\frac {1}{2 - t} + \frac {1}{2 + t}\right) \mathrm {d} t \\ &= \ln \frac {2 + x}{2 - x}. \end{aligned}</equation>当<equation>x \in[ - 1,0)\cup(0,1]</equation>时，<equation>S_{2}(x) = \frac{1}{x}\ln \frac{2+x}{2-x}.</equation>当<equation>x=0</equation>时，<equation>S_{2}(0) = \frac{1}{1\times(2\times 0 + 1)} = 1.</equation>综上所述，幂级数的和函数为<equation>S (x) = \left\{ \begin{array}{l l} \frac {\arctan x}{x} + \frac {1}{x} \ln \frac {2 + x}{2 - x}, & x \in [ - 1, 0) \cup (0, 1 ], \\ 2, & x = 0. \end{array} \right.</equation>

---

**2021年第20题 | 解答题 | 12分**

20. (本题满分12分)

设 n为正整数，<equation>y=y_{n}(x)</equation>是微分方程<equation>x y^{\prime}-(n+1) y=0</equation>的满足条件<equation>y_{n}(1)=\frac{1}{n(n+1)}</equation>的解.

I. 求<equation>y_{n}(x)</equation>II. 求级数<equation>\sum_{n=1}^{\infty} y_{n}(x)</equation>的收敛域及和函数.

**答案:**（I）<equation>y_{n}(x)=\frac{x^{n+1}}{n(n+1)};</equation>（Ⅱ）收敛域为<equation>[-1,1]</equation>，和函数 s(x)<equation>= \left\{\begin{array}{ll}(1-x)\ln(1-x)+x,&x\in[-1,1),\\ 1,&x=1.\end{array}\right.</equation>

**解析:**解（I）整理<equation>x y^{\prime}-(n+1) y=0</equation>可得，<equation>y^{\prime}=\frac{n+1}{x} y.</equation>分离变量得<equation>\frac{\mathrm{d} y}{y}=\frac{n+1}{x}\mathrm{d} x.</equation>两端同时积分可得<equation>\ln |y|=(n+1)\ln |x|+C_{0}.</equation>于是，<equation>y_{n}(x)=Cx^{n+1}</equation>其中C为待定常数.

代入<equation>y_{n}(1)=\frac{1}{n(n+1)},</equation>可得<equation>C=\frac{1}{n(n+1)}.</equation>因此，<equation>y_{n}(x) = \frac{x^{n + 1}}{n(n + 1)}.</equation>（Ⅱ）记<equation>s(x) = \sum_{n = 1}^{\infty}\frac{x^{n + 1}}{n(n + 1)},</equation>其系数<equation>a_{n} = \frac{1}{n(n + 1)}.</equation><equation>\lim _ {n \rightarrow \infty} \left| \frac {a _ {n + 1}}{a _ {n}} \right| = \lim _ {n \rightarrow \infty} \frac {n (n + 1)}{(n + 1) (n + 2)} = 1.</equation>于是，<equation>s ( x )</equation>的收敛半径为1，收敛区间为<equation>(-1,1).</equation>s ( x ) 在 x=-1处为<equation>\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n(n+1)},</equation>由莱布尼茨定理可知该级数收敛. s ( x ) 在 x=1处为<equation>\sum_{n=1}^{\infty}\frac{1}{n(n+1)},</equation>由极限审敛法可知该级数收敛.因此，s ( x ) 的收敛域为<equation>[-1,1].</equation>下面用两种方法计算 s(x).

（法一）整理<equation>s(x).</equation>当 x<equation>\in(-1,1)</equation>时，<equation>\begin{aligned} s (x) &= \sum_ {n = 1} ^ {\infty} \left(\frac {x ^ {n + 1}}{n} - \frac {x ^ {n + 1}}{n + 1}\right) = x \sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n} - \sum_ {n = 1} ^ {\infty} \frac {x ^ {n + 1}}{n + 1} = x \sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n} - \sum_ {n = 2} ^ {\infty} \frac {x ^ {n}}{n} \\ &= (x - 1) \sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n} + x. \end{aligned}</equation>记<equation>t ( x )=\sum_{n=1}^{\infty}\frac{x^{n}}{n}</equation>，则<equation>s ( x )=(x-1)t ( x )+x.</equation><equation>t ^ {\prime} (x) = \left(\sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n}\right) ^ {\prime} \xlongequal {\text {逐 项 求 导}} \sum_ {n = 1} ^ {\infty} \left(\frac {x ^ {n}}{n}\right) ^ {\prime} = \sum_ {n = 1} ^ {\infty} x ^ {n - 1} = \frac {1}{1 - x}.</equation>注意到 t（0）=0，故<equation>t (x) = t (x) - t (0) = \int_ {0} ^ {x} \frac {1}{1 - t} \mathrm {d} t = - \ln (1 - x).</equation>于是，当 x<equation>\in(-1,1)</equation>时，s（x）=（1-x）<equation>\ln(1-x)+x.</equation>因为幂级数的和函数在收敛域上连续，且<equation>( 1-x)\ln(1-x)+x</equation>在 x=-1处连续，所以当 x<equation>\in[ -1,1)</equation>时，<equation>s (x) = (1 - x) \ln (1 - x) + x.</equation>当<equation>x=1</equation>时，<equation>s(1)=\sum_{n=1}^{\infty}\frac{1}{n(n+1)}.</equation>计算<equation>\sum_{n=1}^{\infty} \frac{1}{n(n+1)}</equation>的部分和<equation>\sum_{n=1}^{k} \frac{1}{n(n+1)}</equation>得<equation>\sum_ {n = 1} ^ {k} \frac {1}{n (n + 1)} = \sum_ {n = 1} ^ {k} \left(\frac {1}{n} - \frac {1}{n + 1}\right) = 1 - \frac {1}{2} + \frac {1}{2} - \frac {1}{3} + \dots + \frac {1}{k} - \frac {1}{k + 1} = 1 - \frac {1}{k + 1}.</equation>于是，<equation>\sum_{n = 1}^{\infty}\frac{1}{n(n + 1)} = \lim_{k\to \infty}\sum_{n = 1}^{k}\frac{1}{n(n + 1)} = \lim_{k\to \infty}\left(1 - \frac{1}{k + 1}\right) = 1.</equation>因此，s（x）为分段函数.<equation>s (x) = \left\{ \begin{array}{l l} (1 - x) \ln (1 - x) + x, & x \in [ - 1, 1), \\ 1, & x = 1. \end{array} \right.</equation>（法二）当<equation>x\in(-1,1)</equation>时，<equation>s ^ {\prime} (x) = \left[ \sum_ {n = 1} ^ {\infty} \frac {x ^ {n + 1}}{n (n + 1)} \right] ^ {\prime} \xlongequal {\text {逐 项 求 导}} \sum_ {n = 1} ^ {\infty} \left[ \frac {x ^ {n + 1}}{n (n + 1)} \right] ^ {\prime} = \sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n}.</equation><equation>s ^ {\prime \prime} (x) = \left(\sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n}\right) ^ {\prime} \xlongequal {\text {逐 项 求 导}} \sum_ {n = 1} ^ {\infty} \left(\frac {x ^ {n}}{n}\right) ^ {\prime} = \sum_ {n = 1} ^ {\infty} x ^ {n - 1} = \frac {1}{1 - x}.</equation>注意到<equation>s^{\prime}(0)=0</equation>，故<equation>s ^ {\prime} (x) = s ^ {\prime} (x) - s ^ {\prime} (0) = \int_ {0} ^ {x} \frac {1}{1 - t} \mathrm {d} t = - \ln (1 - t) \Big | _ {0} ^ {x} = - \ln (1 - x).</equation>又因为 s（0）=0，所以<equation>\begin{aligned} s (x) &= s (x) - s (0) = \int_ {0} ^ {x} [ - \ln (1 - t) ] \mathrm {d} t = - \left[ t \ln (1 - t) \left| _ {0} ^ {x} - \int_ {0} ^ {x} \frac {- t}{1 - t} \mathrm {d} t \right. \right] \\ &= - x \ln (1 - x) - \int_ {0} ^ {x} \frac {t}{1 - t} \mathrm {d} t = - x \ln (1 - x) - \int_ {0} ^ {x} \left(- 1 + \frac {1}{1 - t}\right) \mathrm {d} t \\ &= - x \ln (1 - x) - \left[ - t - \ln (1 - t) \right] \left| _ {0} ^ {x} = - x \ln (1 - x) + \left[ t + \ln (1 - t) \right] \right| _ {0} ^ {x} \\ &= - x \ln (1 - x) + x + \ln (1 - x) = (1 - x) \ln (1 - x) + x. \end{aligned}</equation>其余同法一.

---

**2020年第4题 | 选择题 | 4分 | 答案: B**

4. 设幂级数<equation>\sum_{n=1}^{\infty} n a_{n}(x-2)^{n}</equation>的收敛区间为（-2，6），则<equation>\sum_{n=1}^{\infty} a_{n}(x+1)^{2n}</equation>的收敛区间为（    )

A. (-2,6) B. (-3,1) C. (-5,3) D. (-17,15)

答案: B

**解析:**解 由已知条件可得，幂级数<equation>\sum_{n=1}^{\infty} n a_{n}(x-2)^{n}=(x-2)\sum_{n=1}^{\infty} n a_{n}(x-2)^{n-1}</equation>的收敛中心为2，收敛区间为（-2，6），故收敛半径为6-2=4.由收敛半径的平移不变性可知，<equation>\sum_{n=1}^{\infty} n a_{n} x^{n-1}</equation>的收敛半径为4.记<equation>s(x)=\int_{0}^{x}\sum_{n=1}^{\infty} n a_{n} t^{n-1}\mathrm{d}t</equation>则<equation>s(x)\overset{\mathrm{逐项积分}}{=}\sum_{n=1}^{\infty}\int_{0}^{x} n a_{n} t^{n-1}\mathrm{d}t=\sum_{n=1}^{\infty} a_{n} x^{n}.</equation>由收敛半径的逐项积分不变性可知，<equation>\sum_{n=1}^{\infty} a_{n} x^{n}</equation>的收敛半径也为4.<equation>\sum_{n=1}^{\infty} a_{n}(x+1)^{2n}</equation>为缺项幂级数，其收敛半径等于<equation>\sum_{n=1}^{\infty} a_{n} x^{2n}</equation>的收敛半径.由<equation>\sum_{n=1}^{\infty} a_{n} x^{n}</equation>的收敛半径为4可得，<equation>\sum_{n=1}^{\infty} a_{n} x^{2n}</equation>的收敛半径为2.又因为<equation>\sum_{n=1}^{\infty} a_{n}(x+1)^{2n}</equation>的收敛中心为-1，所以其收敛区间为（-3，1）因此，应选B.

---

**2018年第18题 | 解答题 | 10分**

18. (本题满分10分)

已知<equation>\cos 2x-\frac{1}{(1+x)^{2}}=\sum_{n=0}^{\infty}a_{n}x^{n}(-1<x<1)</equation>，求<equation>a_{n}.</equation>

**答案:**<equation>a _ {n} = \left\{ \begin{array}{l l} \frac {(- 1) ^ {k} 4 ^ {k}}{(2 k) !} - 2 k - 1, & n = 2 k, \\ 2 k + 2, & n = 2 k + 1, \end{array} \right. \mathrm {其 中} k \mathrm {为 非 负 整 数}.</equation>

**解析:**由<equation>\cos x</equation>的幂级数展开式可得，<equation>\cos 2 x = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n} (2 x) ^ {2 n}}{(2 n) !} = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n} 4 ^ {n} x ^ {2 n}}{(2 n) !}, - \infty < x < + \infty .</equation>注意到<equation>\left(\frac{1}{1+x}\right)^{\prime}=-\frac{1}{(1+x)^{2}}</equation>故<equation>\begin{aligned} - \frac {1}{(1 + x) ^ {2}} &= \left(\frac {1}{1 + x}\right) ^ {\prime} = \left[ \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} x ^ {n} \right] ^ {\prime} = \sum_ {n = 1} ^ {\infty} (- 1) ^ {n} n x ^ {n - 1} \\ &= \sum_ {n = 0} ^ {\infty} (- 1) ^ {n + 1} (n + 1) x ^ {n}, - 1 < x < 1. \end{aligned}</equation>于是，<equation>\cos 2 x - \frac {1}{(1 + x) ^ {2}} = \sum_ {n = 0} ^ {\infty} \frac {(- 1) ^ {n} 4 ^ {n} x ^ {2 n}}{(2 n) !} + \sum_ {n = 0} ^ {\infty} (- 1) ^ {n + 1} (n + 1) x ^ {n} = \sum_ {n = 0} ^ {\infty} a _ {n} x ^ {n}, - 1 < x < 1.</equation>由于<equation>a_{n}</equation>为<equation>x^{n}</equation>的系数，故<equation>\sum_{n=0}^{\infty}\frac{(-1)^{n}4^{n}x^{2n}}{(2n)!}+\sum_{n=0}^{\infty}(-1)^{n+1}(n+1)x^{n}</equation>中<equation>x^{n}</equation>的系数等于<equation>a_{n}.</equation>当<equation>n=2k</equation>，<equation>k=0,1,2,\dots</equation>时，<equation>a _ {2 k} = \frac {(- 1) ^ {k} 4 ^ {k}}{(2 k) !} + (- 1) ^ {2 k + 1} (2 k + 1) = \frac {(- 1) ^ {k} 4 ^ {k}}{(2 k) !} - 2 k - 1.</equation>当<equation>n = 2k + 1</equation>，<equation>k = 0,1,2,\dots</equation>时，<equation>a _ {2 k + 1} = (- 1) ^ {2 k + 1 + 1} (2 k + 1 + 1) = 2 k + 2.</equation>因此，<equation>a _ {n} = \left\{ \begin{array}{l l} \frac {(- 1) ^ {k} 4 ^ {k}}{(2 k) !} - 2 k - 1, & n = 2 k, \\ 2 k + 2, & n = 2 k + 1, \end{array} \right.</equation>其中 k为非负整数.

---

**2017年第19题 | 解答题 | 10分**

19. (本题满分10分)

若<equation>a_{0}=1, a_{1}=0, a_{n+1}=\frac{1}{n+1}\left(n a_{n}+a_{n-1}\right)\left(n=1, 2, 3, \cdots\right), S(x)</equation>为幂级数<equation>\sum_{n=0}^{\infty}a_{n}x^{n}</equation>的和函数.

I. 证明<equation>\sum_{n=0}^{\infty}a_{n}x^{n}</equation>的收敛半径不小于1；

II. 证明<equation>(1 - x)S^{\prime}(x) - xS(x) = 0,(x\in (-1,1))</equation>，并求<equation>S(x)</equation>的表达式.

**答案:**（I）证明略；

（Ⅱ）证明略，<equation>S ( x )=\frac{\mathrm{e}^{-x}}{1-x}, x \in(-1,1).</equation>

**解析:**解（I）（法一）利用阿贝尔定理.我们证明在（-1，1）内，幂级数<equation>\sum_{n=0}^{\infty} a_{n} x^{n}</equation>绝对收敛，从而由阿贝尔定理可知幂级数的收敛半径不小于1.

首先，证明对任意的<equation>n=0,1,2,\dots</equation>，若 m≤n，则<equation>|a_{m}| \leqslant 1.</equation>由已知条件，<equation>a_{0}=1, a_{1}=0</equation>，故<equation>a_{2}=\frac{1}{2}(0+1)=\frac{1}{2}\leqslant1.</equation>假设对<equation>n = k</equation>时，命题成立，则当<equation>n = k + 1</equation>时，只需证明<equation>|a_{k + 1}| \leqslant 1</equation>.

由递推式<equation>a_{n + 1} = \frac{1}{n + 1}\left(n a_{n} + a_{n - 1}\right)</equation>以及归纳假设可得，<equation>\left| a _ {k + 1} \right| \leqslant \frac {k}{k + 1} \left| a _ {k} \right| + \frac {1}{k + 1} \left| a _ {k - 1} \right| \leqslant \frac {k}{k + 1} + \frac {1}{k + 1} = 1.</equation>由数学归纳法可知，对任意的 n=0，1，2，…，若 m≤n，则<equation>|a_{m}| \leqslant 1.</equation>由此易知，对任意的 n=0， 1，2，…，<equation>|a_{n}| \leqslant 1.</equation><equation>x _ {0} \in (- 1, 1)</equation><equation>\sum_ {n = 0} ^ {\infty} x _ {0} ^ {n}</equation><equation>\left| a _ {n} \right| \leqslant 1</equation><equation>\left| a _ {n} x _ {0} ^ {n} \right| \leqslant \left| x _ {0} ^ {n} \right|</equation><equation>\sum_ {n = 0} ^ {\infty} \left| a _ {n} x _ {0} ^ {n} \right| \leqslant \sum_ {n = 0} ^ {\infty} \left| x _ {0} ^ {n} \right|</equation><equation>\sum_ {n = 0} ^ {\infty} a _ {n} x _ {0} ^ {n}</equation>由于对任意的<equation>x_{0}\in(-1,1)</equation>，级数<equation>\sum_{n=0}^{\infty} a_{n} x_{0}^{n}</equation>均绝对收敛，故由阿贝尔定理可知，幂级数<equation>\sum_{n=0}^{\infty} a_{n} x^{n}</equation>的收敛半径不小于1.

下面的法二、法三均需要计算<equation>a_{n}</equation>的表达式，并且可计算得幂级数的收敛半径实际上等于1.

由<equation>a_{n+1}=\frac{1}{n+1} \left(n a_{n}+a_{n-1}\right) \left(n=1,2,3,\cdots\right)</equation>可得<equation>a _ {n + 1} - a _ {n} = - \frac {1}{n + 1} \left(a _ {n} - a _ {n - 1}\right) (n = 1, 2, 3, \dots).</equation>于是，<equation>a _ {n} - a _ {n - 1} = \frac {- 1}{n} \left(a _ {n - 1} - a _ {n - 2}\right) = \frac {- 1}{n} \cdot \frac {- 1}{n - 1} \left(a _ {n - 2} - a _ {n - 3}\right) = \dots = \frac {(- 1) ^ {n - 1}}{n !} \left(a _ {1} - a _ {0}\right) = \frac {(- 1) ^ {n}}{n !}.</equation>因此，<equation>a _ {n} = \sum_ {k = 1} ^ {n} \left(a _ {k} - a _ {k - 1}\right) + a _ {0} = \sum_ {k = 1} ^ {n} \frac {(- 1) ^ {k}}{k !} + 1 = \sum_ {k = 0} ^ {n} \frac {(- 1) ^ {k}}{k !}.</equation>注意到<equation>\mathrm{e}^{-x}=\sum_{n=0}^{\infty}\frac{(-1)^{n}x^{n}}{n!}</equation>，故<equation>\lim_{n\to \infty}a_{n}=\mathrm{e}^{-1}.</equation>下面我们用两种方法证明<equation>\sum a_{n}x^{n}</equation>的收敛半径等于1.

（法二）考虑<equation>\left| \frac{a_{n+1}}{a_{n}} \right|.</equation>由<equation>\lim_{n\rightarrow\infty}a_{n}=\mathrm{e}^{-1}</equation>，可得<equation>\lim_{n\rightarrow\infty}a_{n+1}=\mathrm{e}^{-1}</equation>，从而<equation>\lim _ {n \rightarrow \infty} \left| \frac {a _ {n + 1}}{a _ {n}} \right| = 1.</equation>因此，幂级数<equation>\sum_{n=0}^{\infty} a_{n} x^{n}</equation>的收敛半径等于1.

（法三）考虑<equation>\sqrt[n]{|a_n|}.</equation><equation>\lim _ {n \rightarrow \infty} \sqrt [ n ]{| a _ {n} |} = \lim _ {n \rightarrow \infty} \mathrm {e} ^ {\frac {1}{n} \ln | a _ {n} |} = \mathrm {e} ^ {\lim _ {n \rightarrow \infty} \frac {\ln | a _ {n} |}{n}} \underline {{\frac {\lim _ {n \rightarrow \infty} a _ {n} = \mathrm {e} ^ {- 1}}{n}}} \mathrm {e} ^ {\lim _ {n \rightarrow \infty} \frac {- 1}{n}} = 1.</equation><equation>\sum_ {n = 0} ^ {\infty} a _ {n} x ^ {n}</equation>（Ⅱ）由第（Ⅰ）问可知，在区间（-1，1）内，<equation>S ( x )</equation>可逐项求导.<equation>x S (x) = \sum_ {n = 0} ^ {\infty} a _ {n} x ^ {n + 1} = \sum_ {n = 1} ^ {\infty} a _ {n - 1} x ^ {n},</equation><equation>S ^ {\prime} (x) = \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n - 1},</equation><equation>(1 - x) S ^ {\prime} (x) = \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n - 1} - \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n} = \sum_ {n = 0} ^ {\infty} (n + 1) a _ {n + 1} x ^ {n} - \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n}.</equation>将<equation>a_{n+1}=\frac{1}{n+1}\left(n a_{n}+a_{n-1}\right)\left(n=1,2,3,\dots\right)</equation>代入<equation>(1-x)S^{\prime}(x)</equation>，得<equation>\begin{aligned} (1 - x) S ^ {\prime} (x) - x S (x) &= \sum_ {n = 0} ^ {\infty} (n + 1) a _ {n + 1} x ^ {n} - \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n} - \sum_ {n = 1} ^ {\infty} a _ {n - 1} x ^ {n} \\ &= a _ {1} + \sum_ {n = 1} ^ {\infty} \left(n a _ {n} + a _ {n - 1}\right) x ^ {n} - \sum_ {n = 1} ^ {\infty} n a _ {n} x ^ {n} - \sum_ {n = 1} ^ {\infty} a _ {n - 1} x ^ {n} = a _ {1} = 0. \end{aligned}</equation>解微分方程（1-x）y'-xy=0.分离变量得<equation>\frac {\mathrm {d} y}{y} = \left(\frac {x}{1 - x}\right) \mathrm {d} x.</equation>上式两端积分得<equation>\ln | y | = \int \left(- 1 + \frac {1}{1 - x}\right) \mathrm {d} x = - x - \ln (1 - x) + C.</equation>当 x=0时，y=1，代入上式得 C=0.由于初值为<equation>y(0)=1>0</equation>，故取<equation>\ln y=-x-\ln(1-x)</equation>即<equation>y=\frac{\mathrm{e}^{-x}}{1-x}.</equation>因此，<equation>S ( x ) = \frac {\mathrm {e}^{- x}}{1 - x}, x \in(-1,1).</equation>

---

**2016年第19题 | 解答题 | 10分**

19. (本题满分10分)

求幂级数<equation>\sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n + 2}}{(n + 1) (2 n + 1)}</equation>的收敛域及和函数.

**答案:**收敛域为<equation>[-1,1]</equation>，和函数 s(x)<equation>\left\{\begin{array}{l l}x\ln \frac{1+x}{1-x}+\ln(1-x^{2}),&x\in(-1,1),\\ 2\ln 2,&x=\pm 1.\end{array}\right.</equation>

**解析:**解 先求收敛域.

原级数是一个缺项型幂级数，我们用比值法来求它的收敛半径.<equation>\lim _ {n \rightarrow \infty} \left| \frac {\frac {x ^ {2 n + 4}}{(n + 2) (2 n + 3)}}{\frac {x ^ {2 n + 2}}{(n + 1) (2 n + 1)}} \right| = \lim _ {n \rightarrow \infty} \left| \frac {(n + 1) (2 n + 1)}{(n + 2) (2 n + 3)} x ^ {2} \right| = x ^ {2}.</equation>由比值审敛法可知，当<equation>|x| < 1</equation>时，原幂级数收敛；当<equation>|x| > 1</equation>时，原幂级数发散，从而收敛半径为1，收敛区间为（-1，1）.

又由于当 x=<equation>\pm 1</equation><equation>\text {原 幂 级 数} = \sum_ {n = 0} ^ {\infty} \frac {1}{(n + 1) (2 n + 1)} \leqslant \sum_ {n = 0} ^ {\infty} \frac {1}{(n + 1) ^ {2}} = \sum_ {n = 1} ^ {\infty} \frac {1}{n ^ {2}},</equation>而<equation>\sum_{n=1}^{\infty}\frac{1}{n^{2}}</equation>收敛，故原幂级数收敛.因此，原幂级数的收敛域为[-1,1].

下面求和函数.

（法一）记<equation>s(x)=\sum_{n=0}^{\infty}\frac{x^{2n+2}}{(n+1)(2n+1)}, x\in[-1,1].</equation>在收敛区间内，可对幂级数进行逐项求导，且不改变幂级数的收敛半径，从而<equation>s ^ {\prime} (x) = \left[ \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n + 2}}{(n + 1) (2 n + 1)} \right] ^ {\prime} = \sum_ {n = 0} ^ {\infty} \left[ \frac {x ^ {2 n + 2}}{(n + 1) (2 n + 1)} \right] ^ {\prime} = 2 \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n + 1}}{2 n + 1}, x \in (- 1, 1),</equation><equation>s ^ {\prime \prime} (x) = 2 \left(\sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n + 1}}{2 n + 1}\right) ^ {\prime} = 2 \sum_ {n = 0} ^ {\infty} \left(\frac {x ^ {2 n + 1}}{2 n + 1}\right) ^ {\prime} = 2 \sum_ {n = 0} ^ {\infty} x ^ {2 n} = \frac {2}{1 - x ^ {2}}, x \in (- 1, 1).</equation>先求<equation>s^{\prime}(x).</equation>.由于<equation>s^{\prime}(0)=0</equation>，故<equation>s ^ {\prime} (x) = \int_ {0} ^ {x} s ^ {\prime \prime} (t) \mathrm {d} t = \int_ {0} ^ {x} \frac {2}{1 - t ^ {2}} \mathrm {d} t = \int_ {0} ^ {x} \left(\frac {1}{1 - t} + \frac {1}{1 + t}\right) \mathrm {d} t = \ln \frac {1 + x}{1 - x}, x \in (- 1, 1).</equation>又因为 s（0）=0，所以<equation>\begin{aligned} s (x) &= \int_ {0} ^ {x} s ^ {\prime} (t) \mathrm {d} t = \int_ {0} ^ {x} \left[ \ln (1 + t) - \ln (1 - t) \right] \mathrm {d} t \\ \underline {{\mathrm {分 部 积 分}}} t \left[ \ln (1 + t) - \ln (1 - t) \right] \left| _ {0} ^ {x} - \int_ {0} ^ {x} t \left(\frac {1}{1 + t} + \frac {1}{1 - t}\right) \mathrm {d} t \right. \\ &= x \ln \frac {1 + x}{1 - x} - \int_ {0} ^ {x} \frac {2 t}{1 - t ^ {2}} \mathrm {d} t = x \ln \frac {1 + x}{1 - x} + \int_ {0} ^ {x} \frac {\mathrm {d} \left(1 - t ^ {2}\right)}{1 - t ^ {2}} \\ &= x \ln \frac {1 + x}{1 - x} + \ln \left(1 - x ^ {2}\right), x \in (- 1, 1). \end{aligned}</equation>最后，由于幂级数的和函数在收敛域上连续，故<equation>\begin{aligned} s (1) &= \lim _ {x \rightarrow 1 ^ {-}} s (x) = \lim _ {x \rightarrow 1 ^ {-}} \left[ x \ln \frac {1 + x}{1 - x} + \ln \left(1 - x ^ {2}\right)\right] \\ &= \lim _ {x \rightarrow 1 ^ {-}} \left[ x \ln (1 + x) - x \ln (1 - x) + \ln (1 + x) + \ln (1 - x) \right] \\ &= \lim _ {x \rightarrow 1 ^ {-}} \left[ (1 + x) \ln (1 + x) + (1 - x) \ln (1 - x) \right] \\ \underline {{\underline {{\lim _ {x \rightarrow 1 ^ {-}}} (1 - x) \ln (1 - x) \stackrel {\mathrm {洛 必 达}} {=} 0}}} 2 \ln 2 + 0 &= 2 \ln 2. \end{aligned}</equation>同理可得 s（-1）=2ln2.

因此，<equation>s ( x ) = \left\{ \begin{array}{l l} x \ln \frac {1 + x}{1 - x} + \ln \left( 1 - x^{2} \right), & x \in(-1,1), \\ 2 \ln 2, & x = \pm 1. \end{array} \right.</equation>（法二）记<equation>\begin{aligned} s (x) &= \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n + 2}}{(n + 1) (2 n + 1)} = 2 \cdot \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n + 2}}{(2 n + 1) (2 n + 2)} \\ &= 2 \cdot \sum_ {n = 0} ^ {\infty} \left(\frac {x ^ {2 n + 2}}{2 n + 1} - \frac {x ^ {2 n + 2}}{2 n + 2}\right), x \in [ - 1, 1 ]. \end{aligned}</equation>记<equation>s_{1}(x)=\sum_{n=0}^{\infty}\frac{x^{2n+1}}{2n+1}, s_{2}(x)=\sum_{n=0}^{\infty}\frac{x^{2n+2}}{2n+2}, x\in(-1,1),</equation>则当<equation>x\in(-1,1)</equation>时，<equation>s (x) = 2 \left[ x s _ {1} (x) - s _ {2} (x) \right].</equation>下面我们分别计算<equation>s_{1}(x)</equation>与<equation>s_{2}(x).</equation>由于<equation>s_1^{\prime}(x) = \left(\sum_{n = 0}^{\infty}\frac{x^{2n + 1}}{2n + 1}\right)^{\prime} = \sum_{n = 0}^{\infty}\left(\frac{x^{2n + 1}}{2n + 1}\right)^{\prime} = \sum_{n = 0}^{\infty}x^{2n} = \frac{1}{1 - x^2}, x\in(-1,1), s_1(0) = 0</equation>，故<equation>s _ {1} (x) = \int_ {0} ^ {x} \frac {1}{1 - t ^ {2}} \mathrm {d} t = \frac {1}{2} \ln \frac {1 + x}{1 - x}, x \in (- 1, 1).</equation>由于<equation>s_2^{\prime}(x) = \left(\sum_{n = 0}^{\infty}\frac{x^{2n + 2}}{2n + 2}\right)^{\prime} = \sum_{n = 0}^{\infty}\left(\frac{x^{2n + 2}}{2n + 2}\right)^{\prime} = \sum_{n = 0}^{\infty}x^{2n + 1} = \frac{x}{1 - x^2},x\in(-1,1),s_2(0) = 0</equation>，故<equation>s _ {2} (x) = \int_ {0} ^ {x} \frac {t}{1 - t ^ {2}} \mathrm {d} t = - \frac {1}{2} \ln \left(1 - x ^ {2}\right), x \in (- 1, 1).</equation>因此，当<equation>x\in(-1,1)</equation>时，<equation>s (x) = 2 \left[ x s _ {1} (x) - s _ {2} (x) \right] = x \ln \frac {1 + x}{1 - x} + \ln \left(1 - x ^ {2}\right).</equation>其余同法一.

---

**2014年第18题 | 解答题 | 10分**

18. (本题满分10分)

求幂级数<equation>\sum_{n=0}^{\infty} ( n+1 ) ( n+3 ) x^{n}</equation>的收敛域及和函数.

**答案:**(18) 收敛域为<equation>(-1,1)</equation>，和函数<equation>s(x) = \frac{3 - x}{(1 - x)^{3}}.</equation>

**解析:**解 先求收敛域.

令<equation>a_{n} = (n + 1)(n + 3)</equation>，则<equation>\lim _ {n \rightarrow \infty} \left| \frac {a _ {n + 1}}{a _ {n}} \right| = \lim _ {n \rightarrow \infty} \frac {(n + 2) (n + 4)}{(n + 1) (n + 3)} = 1,</equation>从而幂级数的收敛半径为1，收敛区间为（-1，1）.又因为幂级数在 x=<equation>\pm 1</equation>时发散，所以幂级数的收敛域为（-1，1）.

下面求和函数.

（法一）记<equation>s ( x )=\sum_{n=0}^{\infty} ( n+1 ) ( n+3 ) x^{n}, x\in(-1,1).</equation>由于幂级数在其收敛区间内可逐项求导和逐项积分，故<equation>\begin{aligned} s (x) &= \sum_ {n = 0} ^ {\infty} (n + 1) (n + 3) x ^ {n} = \sum_ {n = 0} ^ {\infty} (n + 3) \left(x ^ {n + 1}\right) ^ {\prime} = \sum_ {n = 0} ^ {\infty} \left(x ^ {n + 1}\right) ^ {\prime} + \sum_ {n = 0} ^ {\infty} (n + 2) \left(x ^ {n + 1}\right) ^ {\prime} \\ &= \left(\sum_ {n = 0} ^ {\infty} x ^ {n + 1}\right) ^ {\prime} + \sum_ {n = 0} ^ {\infty} \left(x ^ {n + 2}\right) ^ {\prime \prime} = \left(\sum_ {n = 0} ^ {\infty} x ^ {n + 1}\right) ^ {\prime} + \left(\sum_ {n = 0} ^ {\infty} x ^ {n + 2}\right) ^ {\prime \prime} = \left(\frac {x}{1 - x}\right) ^ {\prime} + \left(\frac {x ^ {2}}{1 - x}\right) ^ {\prime \prime} \\ &= \frac {1}{(1 - x) ^ {2}} + \frac {2}{(1 - x) ^ {3}} = \frac {3 - x}{(1 - x) ^ {3}}, x \in (- 1, 1). \end{aligned}</equation>因此，幂级数的和函数为<equation>s ( x )=\frac{3-x}{(1-x)^{3}}, x\in(-1,1).</equation>（法二）也可以如下计算<equation>s(x).</equation><equation>\begin{aligned} s (x) &= \sum_ {n = 0} ^ {\infty} (n + 1) (n + 3) x ^ {n} = \sum_ {n = 0} ^ {\infty} (n + 3) \left(x ^ {n + 1}\right) ^ {\prime} = 3 \sum_ {n = 0} ^ {\infty} \left(x ^ {n + 1}\right) ^ {\prime} + \sum_ {n = 0} ^ {\infty} n \left(x ^ {n + 1}\right) ^ {\prime} \\ &= 3 \left(\sum_ {n = 0} ^ {\infty} x ^ {n + 1}\right) ^ {\prime} + \sum_ {n = 0} ^ {\infty} (n + 1) n x ^ {n} = 3 \cdot \left(\frac {x}{1 - x}\right) ^ {\prime} + x \cdot \sum_ {n = 0} ^ {\infty} (n + 1) n x ^ {n - 1} \\ &= \frac {3}{(1 - x) ^ {2}} + x \cdot \sum_ {n = 0} ^ {\infty} \left(x ^ {n + 1}\right) ^ {\prime \prime} = \frac {3}{(1 - x) ^ {2}} + x \cdot \left(\frac {x}{1 - x}\right) ^ {\prime \prime} = \frac {3}{(1 - x) ^ {2}} + \frac {2 x}{(1 - x) ^ {3}} \\ &= \frac {3 - x}{(1 - x) ^ {3}}, x \in (- 1, 1). \end{aligned}</equation>

---

**2009年第11题 | 填空题 | 4分**

11. 幂级数<equation>\sum_{n=1}^{\infty} \frac{\mathrm{e}^{n}-(-1)^{n}}{n^{2}} x^{n}</equation>的收敛半径为 ___

**解析:**<equation>a _ {n} = \frac {\mathrm {e} ^ {n} - (- 1) ^ {n}}{n ^ {2}}</equation><equation>\lim _ {n \rightarrow \infty} \left| \frac {a _ {n + 1}}{a _ {n}} \right| = \lim _ {n \rightarrow \infty} \frac {\frac {\mathrm {e} ^ {n + 1} - (- 1) ^ {n + 1}}{(n + 1) ^ {2}}}{\frac {\mathrm {e} ^ {n} - (- 1) ^ {n}}{n ^ {2}}} = \lim _ {n \rightarrow \infty} \frac {\mathrm {e} ^ {n + 1} - (- 1) ^ {n + 1}}{\mathrm {e} ^ {n} - (- 1) ^ {n}} \cdot \frac {n ^ {2}}{(n + 1) ^ {2}} = \lim _ {n \rightarrow \infty} \frac {\mathrm {e} - \frac {(- 1) ^ {n + 1}}{\mathrm {e} ^ {n}}}{1 - \frac {(- 1) ^ {n}}{\mathrm {e} ^ {n}}} \cdot 1 = \mathrm {e}.</equation>因此，幂级数的收敛半径为<equation>\frac{1}{e}。</equation>

---


### 多元函数微积分学


