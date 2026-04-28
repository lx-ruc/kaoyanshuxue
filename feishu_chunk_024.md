B. 若<equation>\sum_{n=1}^{\infty}(-1)^{n-1}a_{n}</equation>收敛，则<equation>a_{n}>a_{n+1}</equation>C. 若<equation>\sum_{n=1}^{\infty}a_{n}</equation>收敛，则存在常数 p>1，使<equation>\lim_{n\rightarrow \infty}n^{p}a_{n}</equation>存在

D. 若存在常数 p>1，使<equation>\lim_{n\rightarrow \infty}n^{p}a_{n}</equation>存在，则<equation>\sum_{n=1}^{\infty}a_{n}</equation>收敛

答案: D

**解析:**解 观察四个选项，发现选项D即极限审敛法的内容，故选项D正确.应选D.

下面我们分别说明选项 A、B、C 不正确.

选项A：虽然<equation>\sum_{n=1}^{\infty}(-1)^{n-1}a_{n}</equation>是交错级数，但是与莱布尼茨定理的条件相比较，该级数不满足<equation>\lim_{n\to \infty}a_{n}=0</equation>的条件.因此不能使用莱布尼茨定理说明它收敛.事实上，取<equation>a_{n}=\frac{1}{n}+1</equation><equation>a_{n}>a_{n+1}</equation>，但由于<equation>\lim_{n\to \infty}(-1)^{n-1}\left(\frac{1}{n}+1\right)</equation>不存在，<equation>\sum_{n=1}^{\infty}(-1)^{n-1}a_{n}</equation>不收敛.

选项B：由于级数舍去有限项不影响其敛散性，故我们可以令<equation>a_{n}=\left\{ \begin{array}{ll}1, & n=1,2,3,\\ \frac{1}{n}, & n=4,5,\dots. \end{array} \right.</equation>级数<equation>\sum_{n=1}^{\infty}(-1)^{n-1}a_{n}</equation>收敛，但<equation>a_{1}=a_{2}=a_{3}</equation>，不满足<equation>a_{n}>a_{n+1}</equation>.

选项C：令<equation>a_{n}=\frac{1}{(n+1)\ln^{2}(n+1)}</equation>，对任意的 p > 1，都有<equation>\lim_{n\to \infty}n^{p}\frac{1}{(n+1)\ln^{2}(n+1)}=\infty.</equation>令<equation>f(x)=\frac{1}{(x+1)\ln^{2}(x+1)}.</equation><equation>\int_{1}^{+\infty}f(x)\mathrm{d}x=\int_{1}^{+\infty}\frac{1}{\ln^{2}(x+1)}\mathrm{d}\left[\ln(x+1)\right]=-\frac{1}{\ln(x+1)}\bigg|_{1}^{+\infty}=\frac{1}{\ln 2}.</equation>由积分判别法可知级数<equation>\sum_{n=1}^{\infty}a_{n}</equation>收敛.

---

**2012年第4题 | 选择题 | 4分 | 答案: D**

4. 已知级数<equation>\sum_{n=1}^{\infty}(-1)^{n}\sqrt{n}\sin \frac{1}{n^{\alpha}}</equation>绝对收敛，级数<equation>\sum_{n=1}^{\infty}\frac{(-1)^{n}}{n^{2-\alpha}}</equation>条件收敛，则（    )

A.<equation>0<\alpha \leqslant \frac{1}{2}</equation>B.<equation>\frac{1}{2}<\alpha \leqslant 1</equation>C.<equation>1<\alpha \leqslant \frac{3}{2}</equation>D.<equation>\frac{3}{2}<\alpha <2</equation>

答案: D

**解析:**解 首先，<equation>\alpha >0</equation>，否则<equation>\lim_{n\rightarrow \infty}\sin \frac{1}{n^{\alpha}}\neq 0</equation><equation>\sum_{n=1}^{\infty}(-1)^{n}\sqrt{n}\sin \frac{1}{n^{\alpha}}</equation>不绝对收敛.于是，<equation>0 < \frac{1}{n^{\alpha}}\leqslant 1</equation><equation>\sin \frac{1}{n^{\alpha}}\geqslant 0.</equation>由于<equation>\sum_{n=1}^{\infty}(-1)^{n}\sqrt{n}\sin \frac{1}{n^{\alpha}}</equation>绝对收敛，故<equation>\sum_{n=1}^{\infty}\sqrt{n}\sin \frac{1}{n^{\alpha}}</equation>收敛.

由于<equation>\lim _ {n \rightarrow \infty} \frac {\sqrt {n} \sin \frac {1}{n ^ {\alpha}}}{n ^ {\frac {1}{2} - \alpha}} \xlongequal {\sin \frac {1}{n ^ {\alpha}} \sim \frac {1}{n ^ {\alpha}}} \lim _ {n \rightarrow \infty} \frac {n ^ {\frac {1}{2} - \alpha}}{n ^ {\frac {1}{2} - \alpha}} = 1,</equation>故<equation>\sum_{n=1}^{\infty}\sqrt{n}\sin \frac{1}{n^{\alpha}}</equation>与<equation>\sum_{n=1}^{\infty}n^{\frac{1}{2}-\alpha}</equation>同敛散.

由于<equation>n^{\frac{1}{2} -\alpha} = \frac{1}{n^{\alpha -\frac{1}{2}}}</equation>，故当<equation>\alpha -\frac{1}{2} >1</equation>，即<equation>\alpha >\frac{3}{2}</equation>时，<equation>\sum_{n = 1}^{\infty}n^{\frac{1}{2} -\alpha}</equation>收敛.

由于级数<equation>\sum_{n=1}^{\infty} \frac{(-1)^{n}}{n^{2-\alpha}}</equation>条件收敛，故<equation>\sum_{n=1}^{\infty} \frac{1}{n^{2-\alpha}}</equation>发散，于是<equation>2-\alpha\leqslant1</equation>又因为级数<equation>\sum_{n=1}^{\infty} \frac{(-1)^{n}}{n^{2-\alpha}}</equation>收敛，所以<equation>\lim_{n\to\infty}\frac{(-1)^{n}}{n^{2-\alpha}}=0</equation>，从而<equation>2-\alpha>0</equation>因此，<equation>1\leqslant\alpha<2.</equation>取<equation>\left(\frac{3}{2},+\infty\right)</equation>与[1,2）的交集，得<equation>\frac{3}{2} < \alpha < 2</equation>应选D.

---

**2011年第3题 | 选择题 | 4分 | 答案: A**

3. 设<equation>\{u_{n}\}</equation>是数列，则下列命题正确的是（    ）

A. 若<equation>\sum_{n=1}^{\infty} u_{n}</equation>收敛，则<equation>\sum_{n=1}^{\infty} \left(u_{2n-1}+u_{2n}\right)</equation>收敛

C. 若<equation>\sum_{n=1}^{\infty} u_{n}</equation>收敛，则<equation>\sum_{n=1}^{\infty} \left(u_{2n-1}-u_{2n}\right)</equation>收敛

B. 若<equation>\sum_{n=1}^{\infty} \left(u_{2n-1}+u_{2n}\right)</equation>收敛，则<equation>\sum_{n=1}^{\infty} u_{n}</equation>收敛

D. 若<equation>\sum_{n=1}^{\infty} \left(u_{2n-1}-u_{2n}\right)</equation>收敛，则<equation>\sum_{n=1}^{\infty} u_{n}</equation>收敛

答案: A

**解析:**解 依次讨论各选项.

对选项A，级数<equation>\sum_{n=1}^{\infty}\left(u_{2n-1}+u_{2n}\right)</equation>可由<equation>\sum_{n=1}^{\infty}u_{n}</equation>添加括号得到.由收敛级数的性质，可知当<equation>\sum_{n=1}^{\infty}u_{n}</equation>收敛时，<equation>\sum_{n=1}^{\infty}\left(u_{2n-1}+u_{2n}\right)</equation>收敛.应选A.

取<equation>u_{2n - 1} = 1, u_{2n} = -1</equation>，则<equation>\sum_{n = 1}^{\infty}\left(u_{2n - 1} + u_{2n}\right) = 0</equation>，而<equation>\sum_{n = 1}^{\infty}u_{n}</equation>发散.选项B不正确.

取<equation>u_{n} = (-1)^{n - 1}\frac{1}{n},\sum_{n = 1}^{\infty}u_{n}</equation>为交错级数，由莱布尼茨定理可知<equation>\sum_{n = 1}^{\infty}u_{n}</equation>收敛，但<equation>\begin{aligned} \sum_ {n = 1} ^ {\infty} \left(u _ {2 n - 1} - u _ {2 n}\right) &= \sum_ {n = 1} ^ {\infty} \left[ (- 1) ^ {2 n - 2} \frac {1}{2 n - 1} - (- 1) ^ {2 n - 1} \frac {1}{2 n} \right] \\ &= \sum_ {n = 1} ^ {\infty} \left(\frac {1}{2 n - 1} + \frac {1}{2 n}\right) = \sum_ {n = 1} ^ {\infty} \frac {4 n - 1}{2 n (2 n - 1)}. \end{aligned}</equation>由于<equation>\frac{4 n-1}{2 n(2 n-1)} \geqslant \frac{2 n-1}{2 n(2 n-1)}=\frac{1}{2 n}</equation>，而级数<equation>\sum_{n=1}^{\infty}\frac{1}{2 n}</equation>发散，故<equation>\sum_{n=1}^{\infty}\left(u_{2 n-1}-u_{2 n}\right)</equation>发散.选项C不正确取<equation>u_{n}=1</equation>，则<equation>\sum_{n=1}^{\infty}\left(u_{2 n-1}-u_{2 n}\right)=0</equation>，收敛，但<equation>\sum_{n=1}^{\infty}u_{n}</equation>发散.选项D不正确.

---


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


#### 交换积分次序与坐标系之间的转化

**2025年第4题 | 选择题 | 5分 | 答案: D**

4. 设函数 f(x) 连续，<equation>\int_{0}^{1}\mathrm{d}y\int_{0}^{y}f(x)\mathrm{d}x=</equation>(    )

A.<equation>\int_{0}^{1}x f(x)\mathrm{d}x</equation>B.<equation>\int_{0}^{1}(x+1)f(x)\mathrm{d}x</equation>C.<equation>\int_{0}^{1}(x-1)f(x)\mathrm{d}x</equation>D.<equation>\int_{0}^{1}(1-x)f(x)\mathrm{d}x</equation>

答案: D

**解析:**解 二次积分<equation>\int_{0}^{1}\mathrm{d}y\int_{0}^{y}f(x)\mathrm{d}x</equation>对应的二重积分的积分区域<equation>D = \left\{(x, y) \mid 0 \leqslant x \leqslant y, 0 \leqslant y \leqslant 1 \right\}.</equation>区域 D如图所示.将 D写成 X型区域.<equation>D = \left\{(x, y) \mid x \leqslant y \leqslant 1, 0 \leqslant x \leqslant 1 \right\}.</equation>于是，<equation>\int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {y} f (x) \mathrm {d} x = \iint_ {D} f (x) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} f (x) \mathrm {d} x \int_ {x} ^ {1} \mathrm {d} y = \int_ {0} ^ {1} (1 - x) f (x) \mathrm {d} x.</equation>因此，应选D.

---

**2024年第3题 | 选择题 | 5分 | 答案: A**

3. 设 f(x,y)是连续函数，则<equation>\int_{\frac{\pi}{6}}^{\frac{\pi}{2}} \mathrm{d} x \int_{\sin x}^{1} f(x,y) \mathrm{d} y=</equation>(    )

A.<equation>\int_{\frac{1}{2}}^{1} \mathrm{d} y \int_{\frac{\pi}{6}}^{\arcsin y} f(x,y) \mathrm{d} x</equation>B.<equation>\int_{\frac{1}{2}}^{1} \mathrm{d} y \int_{\arcsin y}^{\frac{\pi}{2}} f(x,y) \mathrm{d} x</equation>C.<equation>\int_{0}^{\frac{1}{2}} \mathrm{d} y \int_{\frac{\pi}{6}}^{\arcsin y} f(x,y) \mathrm{d} x</equation>D.<equation>\int_{0}^{\frac{1}{2}} \mathrm{d} y \int_{\arcsin y}^{\frac{\pi}{2}} f(x,y) \mathrm{d} x</equation>

答案: A

**解析:**解二次积分<equation>\int_{\frac{\pi}{6}}^{\frac{\pi}{2}} \mathrm{d} x \int_{\sin x}^{1} f(x,y)\mathrm{d} y</equation>对应的二重积分的积分区域为<equation>D = \left\{(x, y) \mid \sin x \leqslant y \leqslant 1, \frac {\pi}{6} \leqslant x \leqslant \frac {\pi}{2} \right\}.</equation>由于<equation>\arcsin y</equation>的值域为<equation>\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>，而<equation>\left[\frac{\pi}{6},\frac{\pi}{2}\right]\subset\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>，故曲线<equation>y=\sin x \left(x\in\left[\frac{\pi}{6},\frac{\pi}{2}\right]\right)</equation>上的点（x,y）可写为（<equation>\arcsin y,y).</equation>由此可将 D改写成Y型区域，<equation>D = \left\{(x, y) \mid \frac {\pi}{6} \leqslant x \leqslant \arcsin y, \frac {1}{2} \leqslant y \leqslant 1 \right\}.</equation>因此，<equation>\int_ {\frac {\pi}{6}} ^ {\frac {\pi}{2}} \mathrm {d} x \int_ {\sin x} ^ {1} f (x, y) \mathrm {d} y = \int_ {\frac {1}{2}} ^ {1} \mathrm {d} y \int_ {\frac {\pi}{6}} ^ {\arcsin y} f (x, y) \mathrm {d} x.</equation>应选A.

---

**2015年第3题 | 选择题 | 4分 | 答案: B**

3. 设<equation>D=\{(x,y)\mid x^{2}+y^{2}\leqslant 2x,x^{2}+y^{2}\leqslant 2y\}</equation>，函数 f(x,y)在 D上连续，则<equation>\iint_{D}f(x,y)\mathrm{d}x\mathrm{d}y=</equation>(    )

A.<equation>\int_{0}^{\frac{\pi}{4}}\mathrm{d}\theta \int_{0}^{2\cos \theta}f(r\cos \theta,r\sin \theta)r\mathrm{d}r+\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}\mathrm{d}\theta \int_{0}^{2\sin \theta}f(r\cos \theta,r\sin \theta)r\mathrm{d}r</equation>B.<equation>\int_{0}^{\frac{\pi}{4}}\mathrm{d}\theta \int_{0}^{2\sin \theta}f(r\cos \theta,r\sin \theta)r\mathrm{d}r+\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}\mathrm{d}\theta \int_{0}^{2\cos \theta}f(r\cos \theta,r\sin \theta)r\mathrm{d}r</equation>C.<equation>2\int_{0}^{1}\mathrm{d}x\int_{1-\sqrt{1-x^{2}}}^{x}f(x,y)\mathrm{d}y</equation>D.<equation>2\int_{0}^{1}\mathrm{d}x\int_{x}^{\sqrt{2x-x^{2}}}f(x,y)\mathrm{d}y</equation>

答案: B

**解析:**解 圆<equation>x^{2}+y^{2}=2x</equation>的极坐标方程为<equation>r=2\cos \theta</equation>，圆<equation>x^{2}+y^{2}=2y</equation>的极坐标方程为<equation>r=2\sin \theta.</equation>由图可知，当<equation>0\leqslant \theta \leqslant \frac{\pi}{4}</equation>时，D的边界为<equation>r=2\sin \theta</equation>；当<equation>\frac{\pi}{4}\leqslant \theta \leqslant \frac{\pi}{2}</equation>时，D的边界为<equation>r=2\cos \theta</equation>于是，<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2 \sin \theta , 0 \leqslant \theta \leqslant \frac {\pi}{4} \right\} \cup \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2 \cos \theta , \frac {\pi}{4} \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation>因此，<equation>\iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {\frac {\pi}{4}} \mathrm {d} \theta \int_ {0} ^ {2 \sin \theta} f (r \cos \theta , r \sin \theta) r \mathrm {d} r + \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {2 \cos \theta} f (r \cos \theta , r \sin \theta) r \mathrm {d} r.</equation>应选B.

由上述论证可知选项A不正确.

若在直角坐标系下计算，则区域 D 可表示为<equation>D = \left\{(x, y) \mid 1 - \sqrt {1 - x ^ {2}} \leqslant y \leqslant \sqrt {2 x - x ^ {2}}, 0 \leqslant x \leqslant 1 \right\}.</equation>于是，<equation>\iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {1 - \sqrt {1 - x ^ {2}}} ^ {\sqrt {2 x - x ^ {2}}} f (x, y) \mathrm {d} y.</equation>因此，选项C、D均不正确.

---

**2014年第12题 | 填空题 | 4分**

12. 二次积分<equation>\int_{0}^{1}\mathrm{d}y\int_{y}^{1}\left(\frac{\mathrm{e}^{x^{2}}}{x}-\mathrm{e}^{y^{2}}\right)\mathrm{d}x=</equation>___

**解析:**<equation>\begin{aligned} \int_ {0} ^ {1} \mathrm {d} y \int_ {y} ^ {1} \left(\frac {\mathrm {e} ^ {x ^ {2}}}{x} - \mathrm {e} ^ {y ^ {2}}\right) \mathrm {d} x &= \int_ {0} ^ {1} \mathrm {d} y \int_ {y} ^ {1} \frac {\mathrm {e} ^ {x ^ {2}}}{x} \mathrm {d} x - \int_ {0} ^ {1} \mathrm {d} y \int_ {y} ^ {1} \mathrm {e} ^ {y ^ {2}} \mathrm {d} x \\ &= \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {x} \frac {\mathrm {e} ^ {x ^ {2}}}{x} \mathrm {d} y - \int_ {0} ^ {1} (1 - y) \mathrm {e} ^ {y ^ {2}} \mathrm {d} y \\ &= \int_ {0} ^ {1} \mathrm {e} ^ {x ^ {2}} \mathrm {d} x - \int_ {0} ^ {1} \mathrm {e} ^ {y ^ {2}} \mathrm {d} y + \int_ {0} ^ {1} y \mathrm {e} ^ {y ^ {2}} \mathrm {d} y \\ &= \frac {1}{2} \int_ {0} ^ {1} \mathrm {e} ^ {y ^ {2}} \mathrm {d} \left(y ^ {2}\right) = \frac {1}{2} \mathrm {e} ^ {y ^ {2}} \Big | _ {0} ^ {1} = \frac {\mathrm {e} - 1}{2}. \end{aligned}</equation>

---

**2012年第3题 | 选择题 | 4分 | 答案: B**

3. 设函数 f(t) 连续，则二次积分<equation>\int_{0}^{\frac{\pi}{2}} \mathrm{d}\theta \int_{2\cos \theta}^{2} f\left(r^{2}\right) r \mathrm{d} r=</equation>(    )

A.<equation>\int_{0}^{2} \mathrm{d} x \int_{\sqrt{2 x-x^{2}}}^{\sqrt{4-x^{2}}} \sqrt{x^{2}+y^{2}} f\left(x^{2}+y^{2}\right) \mathrm{d} y</equation>B.<equation>\int_{0}^{2} \mathrm{d} x \int_{\sqrt{2 x-x^{2}}}^{\sqrt{4-x^{2}}} f\left(x^{2}+y^{2}\right) \mathrm{d} y</equation>C.<equation>\int_{0}^{2} \mathrm{d} y \int_{1+\sqrt{1-y^{2}}}^{\sqrt{4-y^{2}}} \sqrt{x^{2}+y^{2}} f\left(x^{2}+y^{2}\right) \mathrm{d} x</equation>D.<equation>\int_{0}^{2} \mathrm{d} y \int_{1+\sqrt{1-y^{2}}}^{\sqrt{4-y^{2}}} f\left(x^{2}+y^{2}\right) \mathrm{d} x</equation>

答案: B

**解析:**解 原二次积分对应的二重积分的积分区域为<equation>D=\left\{(r,\theta)\mid 2\cos \theta \leqslant r\leqslant 2,0\leqslant \theta \leqslant \frac{\pi}{2}\right\}</equation>曲线 r=2，r=2cos<equation>\theta</equation>的直角坐标方程分别为<equation>x^{2}+y^{2}=4</equation><equation>x^{2}+y^{2}=2x.</equation>(a)

(b)

由于<equation>0 \leqslant \theta \leqslant \frac{\pi}{2}</equation>，故区域D如图（a）所示. D在直角坐标系下可表示为<equation>D = \left\{(x, y) \mid \sqrt {2 x - x ^ {2}} \leqslant y \leqslant \sqrt {4 - x ^ {2}}, 0 \leqslant x \leqslant 2 \right\}.</equation>将<equation>f(r^{2})</equation>换成<equation>f(x^{2}+y^{2})</equation>，将<equation>r\mathrm{d}r\mathrm{d}\theta</equation>换成<equation>\mathrm{d}x\mathrm{d}y</equation>，得<equation>\int_{0}^{2}\mathrm{d}x\int_{\sqrt{2x-x^{2}}}^{\sqrt{4-x^{2}}}f(x^{2}+y^{2})\mathrm{d}y.</equation>应选B.

下面我们说明选项 A、C、D不正确.

选项A中的积分区域表示与选项B一样，但是被积函数多了一个因子<equation>\sqrt{x^{2}+y^{2}}</equation>注意到，极坐标与直角坐标的相互转化中，<equation>\mathrm{r} \mathrm{d} r \mathrm{d} \theta=\mathrm{d} x \mathrm{d} y</equation>原积分中的<equation>\mathrm{r} \mathrm{d} r \mathrm{d} \theta</equation>转化为<equation>\mathrm{d} x \mathrm{d} y</equation>被积函数变为<equation>f \left(x^{2}+y^{2}\right)</equation>在新积分中，没有因子r.选项A不正确.

被积函数与选项A一样.选项C不正确.

选项D中的积分区域为<equation>D^{\prime}=\{(x,y)\mid 1+\sqrt{1-y^{2}}\leqslant x\leqslant \sqrt{4-y^{2}},0\leqslant y\leqslant 2\}</equation><equation>D^{\prime}</equation>如图（b）所示.选项D不正确.

---


#### 偏导数的概念与计算

**2025年第14题 | 填空题 | 5分**

14. 已知函数<equation>z=z(x,y)</equation>由<equation>z+\ln z-\int_{y}^{x}x\mathrm{e}^{-t^{2}}\mathrm{d}t=1</equation>确定，则<equation>\left.\frac{\partial^{2} z}{\partial x^{2}}\right|_{(1,1)}=</equation>___

**解析:**解 将<equation>x = 1,y = 1</equation>代入方程<equation>z + \ln z - \int_{y}^{x}x\mathrm{e}^{-t^{2}}\mathrm{d}t = 1</equation>可得，<equation>z(1,1) + \ln z(1,1) = 1.</equation>注意到<equation>z = 1</equation>是方程<equation>z + \ln z = 1</equation>的一个解，且<equation>(z + \ln z)^{\prime} = 1 + \frac{1}{z} > 0</equation>，函数<equation>z + \ln z</equation>单调增加，故1是该方程的唯一解，<equation>z(1,1) = 1.</equation>已知方程可写为<equation>z+\ln z-x\int_{y}^{x}\mathrm{e}^{-t^{2}}\mathrm{d} t=1</equation>，对该方程两端关于 x求偏导数可得<equation>\frac {\partial z}{\partial x} + \frac {1}{z} \cdot \frac {\partial z}{\partial x} - \int_ {y} ^ {x} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t - x \cdot \mathrm {e} ^ {- x ^ {2}} = 0.</equation>在(1)式中代入<equation>x = 1,y = 1,z = 1</equation>可得<equation>2\frac{\partial z}{\partial x}\bigg|_{(1,1)} = \mathrm{e}^{-1}</equation>，解得<equation>\frac{\partial z}{\partial x}\bigg|_{(1,1)} = \frac{1}{2\mathrm{e}}.</equation>对（1）式两端关于 x求偏导数可得<equation>\frac {\partial^ {2} z}{\partial x ^ {2}} + \frac {1}{z} \cdot \frac {\partial^ {2} z}{\partial x ^ {2}} - \frac {1}{z ^ {2}} \cdot \left(\frac {\partial z}{\partial x}\right) ^ {2} - \mathrm {e} ^ {- x ^ {2}} - \mathrm {e} ^ {- x ^ {2}} + 2 x ^ {2} \mathrm {e} ^ {- x ^ {2}} = 0.</equation>在（2）式中代入<equation>x=1,y=1,z=1,\frac{\partial z}{\partial x}\bigg|_{(1,1)}=\frac{1}{2\mathrm{e}}</equation>可得<equation>2\frac{\partial^{2}z}{\partial x^{2}}\bigg|_{(1,1)}-\frac{1}{4\mathrm{e}^{2}}-2\mathrm{e}^{-1}+2\mathrm{e}^{-1}=0</equation>解得<equation>\frac{\partial^{2}z}{\partial x^{2}}\bigg|_{(1,1)}=\frac{1}{8\mathrm{e}^{2}}.</equation>

---

**2024年第18题 | 解答题 | 12分**

18. (本题满分12分）设函数<equation>z=z(x,y)</equation>由方程<equation>z+\mathrm{e}^{x}-y\ln(1+z^{2})=0</equation>确定，求<equation>\left.\left(\frac{\partial^{2} z}{\partial x^{2}}+\frac{\partial^{2} z}{\partial y^{2}}\right)\right|_{(0,0)}</equation>

**解析:**解 将 x=0,y=0代入方程<equation>z+{\mathrm{e}}^{x}-y\ln(1+z^{2})=0</equation>可得，<equation>z(0,0)+1=0</equation>即<equation>z(0,0)=-1.</equation>对方程<equation>z+{\mathrm{e}}^{x}-y\ln(1+z^{2})=0</equation>两端同时关于 x求偏导数可得，<equation>\frac {\partial z}{\partial x} + \mathrm {e} ^ {x} - y \cdot \frac {2 z \frac {\partial z}{\partial x}}{1 + z ^ {2}} = 0, \quad \text {即} \frac {\partial z}{\partial x} + \mathrm {e} ^ {x} - \frac {2 y z}{1 + z ^ {2}} \cdot \frac {\partial z}{\partial x} = 0.</equation>将<equation>x = 0,y = 0,z = -1</equation>代人（1）式可得，<equation>\frac{\partial z}{\partial x}\bigg|_{(0,0)} + 1 = 0</equation>，即<equation>\frac{\partial z}{\partial x}\bigg|_{(0,0)} = -1.</equation>对<equation>\frac{\partial z}{\partial x} +\mathrm{e}^{x} -\frac{2yz}{1+z^{2}}\cdot \frac{\partial z}{\partial x} = 0</equation>两端关于<equation>x</equation>求偏导数可得，<equation>\frac {\partial^ {2} z}{\partial x ^ {2}} + \mathrm {e} ^ {x} - 2 y \cdot \frac {1 + z ^ {2} - 2 z ^ {2}}{\left(1 + z ^ {2}\right) ^ {2}} \cdot \left(\frac {\partial z}{\partial x}\right) ^ {2} - \frac {2 y z}{1 + z ^ {2}} \cdot \frac {\partial^ {2} z}{\partial x ^ {2}} = 0.</equation>将<equation>x = 0,y = 0,z = -1,\frac{\partial z}{\partial x}\bigg|_{(0,0)} = -1</equation>代人(2）式可得，<equation>\frac{\partial^2z}{\partial x^2}\bigg|_{(0,0)} + 1 = 0</equation>，即<equation>\frac{\partial^2z}{\partial x^2}\bigg|_{(0,0)} = -1.</equation>对方程<equation>z + \mathrm{e}^{x} - y\ln (1 + z^{2}) = 0</equation>两端同时关于 y求偏导数可得，<equation>\frac {\partial z}{\partial y} - \ln \left(1 + z ^ {2}\right) - y \cdot \frac {2 z \frac {\partial z}{\partial y}}{1 + z ^ {2}} = 0, \quad \text {即} \frac {\partial z}{\partial y} - \ln \left(1 + z ^ {2}\right) - \frac {2 y z}{1 + z ^ {2}} \cdot \frac {\partial z}{\partial y} = 0.</equation>将<equation>x = 0,y = 0,z = -1</equation>代人（3）式可得，<equation>\frac{\partial z}{\partial y}\bigg|_{(0,0)} - \ln 2 = 0</equation>，即<equation>\frac{\partial z}{\partial y}\bigg|_{(0,0)} = \ln 2.</equation>对<equation>\frac{\partial z}{\partial y}-\ln(1+z^{2})-\frac{2yz}{1+z^{2}}\cdot \frac{\partial z}{\partial y}=0</equation>两端关于 y求偏导数可得，<equation>\frac {\partial^ {2} z}{\partial y ^ {2}} - \frac {2 z \frac {\partial z}{\partial y}}{1 + z ^ {2}} - \frac {2 z \frac {\partial z}{\partial y}}{1 + z ^ {2}} - 2 y \cdot \frac {1 + z ^ {2} - 2 z ^ {2}}{\left(1 + z ^ {2}\right) ^ {2}} \cdot \left(\frac {\partial z}{\partial y}\right) ^ {2} - \frac {2 y z}{1 + z ^ {2}} \cdot \frac {\partial^ {2} z}{\partial y ^ {2}} = 0.</equation>将<equation>x = 0,y = 0,z = -1,\frac{\partial z}{\partial y}\bigg|_{(0,0)} = \ln 2</equation>代入(4)式可得，<equation>\frac{\partial^{2}z}{\partial y^{2}}\bigg|_{(0,0)} + 2\ln 2 = 0</equation>，即<equation>\frac{\partial^{2}z}{\partial y^{2}}\bigg|_{(0,0)} = -2\ln 2.</equation>因此，<equation>\left(\frac{\partial^{2}z}{\partial x^{2}} + \frac{\partial^{2}z}{\partial y^{2}}\right)\bigg|_{(0,0)} = -1 - 2\ln 2.</equation>

---

**2023年第1题 | 选择题 | 5分 | 答案: A**

1. 已知函数<equation>f ( x,y)=\ln ( y+| x \sin y | )</equation>，则（    ）

A.<equation>\left. \frac{\partial f}{\partial x}\right|_{(0,1)}</equation>不存在，<equation>\left. \frac{\partial f}{\partial y}\right|_{(0,1)}</equation>存在

B.<equation>\left. \frac{\partial f}{\partial x}\right|_{(0,1)}</equation>存在，<equation>\left. \frac{\partial f}{\partial y}\right|_{(0,1)}</equation>不存在

C.<equation>\left. \frac{\partial f}{\partial x}\right|_{(0,1)},\left. \frac{\partial f}{\partial y}\right|_{(0,1)}</equation>均存在

D.<equation>\left. \frac{\partial f}{\partial x}\right|_{(0,1)},\left. \frac{\partial f}{\partial y}\right|_{(0,1)}</equation>均不存在

答案: A

**解析:**由<equation>f ( x,y )</equation>的表达式可知，<equation>f ( 0,1 )=0.</equation>根据偏导数的定义，<equation>\left. \frac {\partial f}{\partial x} \right| _ {(0, 1)} = \lim _ {x \rightarrow 0} \frac {f (x , 1) - f (0 , 1)}{x - 0} = \lim _ {x \rightarrow 0} \frac {\ln (1 + | x \sin 1 |)}{x} = \lim _ {x \rightarrow 0} \frac {| x | \sin 1}{x}.</equation>由于<equation>\lim_{x\to 0^{-}}\frac{|x|}{x} = -1,</equation><equation>\lim_{x\to 0^{+}}\frac{|x|}{x} = 1,</equation>故<equation>\lim_{x\to 0}\frac{|x|}{x}</equation>不存在，从而<equation>\left.\frac{\partial f}{\partial x}\right|_{(0,1)}</equation>不存在.<equation>\left. \frac {\partial f}{\partial y} \right| _ {(0, 1)} = \lim _ {y \rightarrow 1} \frac {f (0 , y) - f (0 , 1)}{y - 1} = \lim _ {y \rightarrow 1} \frac {\ln y}{y - 1} = \lim _ {y \rightarrow 1} \frac {\ln (1 + y - 1)}{y - 1} = \lim _ {y \rightarrow 1} \frac {y - 1}{y - 1} = 1.</equation>因此，<equation>\frac{\partial f}{\partial y}\bigg|_{(0,1)}=1.</equation>综上所述，<equation>\frac{\partial f}{\partial x}\bigg|_{(0,1)}</equation>不存在，<equation>\frac{\partial f}{\partial y}\bigg|_{(0,1)}</equation>存在，应选A.

---

**2022年第3题 | 选择题 | 5分 | 答案: C**

3. 已知 f(t) 连续，令<equation>F ( x,y)=\int_{0}^{x-y} ( x-y-t ) f ( t ) \mathrm{d} t</equation>，则（    ）<equation>\begin{aligned} \mathrm {A}. \frac {\partial F}{\partial x} &= \frac {\partial F}{\partial y}, \frac {\partial^ {2} F}{\partial x ^ {2}} = \frac {\partial^ {2} F}{\partial y ^ {2}} \\ \mathrm {C}. \frac {\partial F}{\partial x} &= - \frac {\partial F}{\partial y}, \frac {\partial^ {2} F}{\partial x ^ {2}} = \frac {\partial^ {2} F}{\partial y ^ {2}} \end{aligned}</equation><equation>\begin{aligned} B. \frac {\partial F}{\partial x} &= \frac {\partial F}{\partial y}, \frac {\partial^ {2} F}{\partial x ^ {2}} = - \frac {\partial^ {2} F}{\partial y ^ {2}} \\ D. \frac {\partial F}{\partial x} &= - \frac {\partial F}{\partial y}, \frac {\partial^ {2} F}{\partial x ^ {2}} = - \frac {\partial^ {2} F}{\partial y ^ {2}} \end{aligned}</equation>

答案: C

**解析:**解 整理 F(x,y）的表达式.<equation>F (x, y) = \int_ {0} ^ {x - y} (x - y - t) f (t) \mathrm {d} t = (x - y) \int_ {0} ^ {x - y} f (t) \mathrm {d} t - \int_ {0} ^ {x - y} t f (t) \mathrm {d} t.</equation>分别计算<equation>\frac{\partial F}{\partial x},\frac{\partial^{2} F}{\partial x^{2}},\frac{\partial F}{\partial y},\frac{\partial^{2} F}{\partial y^{2}}.</equation><equation>\frac {\partial F}{\partial x} = (x - y) f (x - y) + \int_ {0} ^ {x - y} f (t) \mathrm {d} t - (x - y) f (x - y) = \int_ {0} ^ {x - y} f (t) \mathrm {d} t,</equation><equation>\frac {\partial^ {2} F}{\partial x ^ {2}} = \frac {\partial \left[ \int_ {0} ^ {x - y} f (t) \mathrm {d} t \right]}{\partial x} = f (x - y),</equation><equation>\frac {\partial F}{\partial y} = - (x - y) f (x - y) - \int_ {0} ^ {x - y} f (t) \mathrm {d} t + (x - y) f (x - y) = - \int_ {0} ^ {x - y} f (t) \mathrm {d} t,</equation><equation>\frac {\partial^ {2} F}{\partial y ^ {2}} = \frac {\partial \left[ - \int_ {0} ^ {x - y} f (t) \mathrm {d} t \right]}{\partial y} = f (x - y).</equation>因此，<equation>\frac{\partial F}{\partial x}=-\frac{\partial F}{\partial y},\frac{\partial^{2}F}{\partial x^{2}}=\frac{\partial^{2}F}{\partial y^{2}}.</equation>应选C.

---

**2019年第16题 | 解答题 | 10分**

16. (本题满分10分）

设函数 f(u,v)具有2阶连续偏导数，函数 g(x,y) = xy-f(x+y,x-y).求<equation>\frac{\partial^{2} g}{\partial x^{2}}+\frac{\partial^{2} g}{\partial x \partial y}+\frac{\partial^{2} g}{\partial y^{2}}.</equation>

**答案:**<equation>1 - 3 f_{11}^{\prime \prime} ( x + y, x - y ) - f_{22}^{\prime \prime} ( x + y, x - y ).</equation>

**解析:**<equation>\begin{aligned} \frac {\partial g}{\partial x} &= y - f _ {1} ^ {\prime} (x + y, x - y) - f _ {2} ^ {\prime} (x + y, x - y), \\ \frac {\partial g}{\partial y} &= x - f _ {1} ^ {\prime} (x + y, x - y) + f _ {2} ^ {\prime} (x + y, x - y), \\ \frac {\partial^ {2} g}{\partial x ^ {2}} &= - f _ {1 1} ^ {\prime \prime} (x + y, x - y) - f _ {1 2} ^ {\prime \prime} (x + y, x - y) - f _ {2 1} ^ {\prime \prime} (x + y, x - y) - f _ {2 2} ^ {\prime \prime} (x + y, x - y) \\ \frac {f (u , v) \mathrm {具 有} 2 \mathrm {阶 连 续 偏 导 数}}{} - f _ {1 1} ^ {\prime \prime} (x + y, x - y) - 2 f _ {1 2} ^ {\prime \prime} (x + y, x - y) - f _ {2 2} ^ {\prime \prime} (x + y, x - y), \\ \frac {\partial^ {2} g}{\partial x \partial y} &= 1 - f _ {1 1} ^ {\prime \prime} (x + y, x - y) + f _ {1 2} ^ {\prime \prime} (x + y, x - y) - f _ {2 1} ^ {\prime \prime} (x + y, x - y) + f _ {2 2} ^ {\prime \prime} (x + y, x - y) \\ \frac {f (u , v) \mathrm {具 有} 2 \mathrm {阶 连 续 偏 导 数}}{} 1 - f _ {1 1} ^ {\prime \prime} (x + y, x - y) + f _ {2 2} ^ {\prime \prime} (x + y, x - y), \\ \frac {\partial^ {2} g}{\partial y ^ {2}} &= - f _ {1 1} ^ {\prime \prime} (x + y, x - y) + f _ {1 2} ^ {\prime \prime} (x + y, x - y) + f _ {2 1} ^ {\prime \prime} (x + y, x - y) - f _ {2 2} ^ {\prime \prime} (x + y, x - y) \\ \frac {f (u , v) \mathrm {具 有} 2 \mathrm {阶 连 续 偏 导 数}}{} - f _ {1 1} ^ {\prime \prime} (x + y, x - y) + 2 f _ {1 2} ^ {\prime \prime} (x + y, x - y) - f _ {2 2} ^ {\prime \prime} (x + y, x - y). \\ \mathrm {代 入} \frac {\partial^ {2} g}{\partial x ^ {2}} + \frac {\partial^ {2} g}{\partial x \partial y} + \frac {\partial^ {2} g}{\partial y ^ {2}} \mathrm {可 得}, \\ \frac {\partial^ {2} g}{\partial x} \frac {\partial^ {2} g}{\partial y} \frac {\partial^ {2} g}{\partial y ^ {2}} \end{aligned}</equation><equation>\frac {\partial^ {2} g}{\partial x ^ {2}} + \frac {\partial^ {2} g}{\partial x \partial y} + \frac {\partial^ {2} g}{\partial y ^ {2}} = 1 - 3 f _ {1 1} ^ {\prime \prime} (x + y, x - y) - f _ {2 2} ^ {\prime \prime} (x + y, x - y).</equation>

---

**2016年第2题 | 选择题 | 4分 | 答案: D**

2. 已知函数<equation>f(x,y)=\frac{\mathrm{e}^{x}}{x-y}</equation>，则（    ）

A.<equation>f_{x}^{\prime}-f_{y}^{\prime}=0</equation>B.<equation>f_{x}^{\prime}+f_{y}^{\prime}=0</equation>C.<equation>f_{x}^{\prime}-f_{y}^{\prime}=f</equation>D.<equation>f_{x}^{\prime}+f_{y}^{\prime}=f</equation>

答案: D

**解析:**分别计算<equation>f_{x}^{\prime}, f_{y}^{\prime}</equation>得

因此，<equation>f _ {x} ^ {\prime} = \frac {\mathrm {e} ^ {x} (x - y) - \mathrm {e} ^ {x}}{(x - y) ^ {2}}, \quad f _ {y} ^ {\prime} = \frac {\mathrm {e} ^ {x}}{(x - y) ^ {2}}.</equation><equation>f _ {x} ^ {\prime} + f _ {y} ^ {\prime} = \frac {\mathrm {e} ^ {x} (x - y)}{(x - y) ^ {2}} = \frac {\mathrm {e} ^ {x}}{x - y} = f.</equation>应选 D.

---

**2013年第10题 | 填空题 | 4分**

10. 设函数<equation>z=z(x,y)</equation>由方程<equation>( z+y )^{x}= x y</equation>确定，则<equation>\left. \frac{\partial z}{\partial x} \right|_{(1,2)}=</equation>___

**答案:**# 2(1-ln2).

**解析:**解 将方程<equation>( z+y)^{x}=xy</equation>化为<equation>\mathrm{e}^{x\ln(z+y)}=xy</equation>，对所得方程两端关于 x求偏导数，可得<equation>\mathrm {e} ^ {x \ln (z + y)} \left[ \ln (z + y) + \frac {x \cdot \frac {\partial z}{\partial x}}{z + y} \right] = y.</equation>当 x=1，y=2时，由原方程可知 z=0，从而由上式可得<equation>\mathrm{e}^{\ln 2}\left(\ln 2+\frac{\frac{\partial z}{\partial x}\bigg|_{(1,2)}}{2}\right)=2</equation>即<equation>\left.\frac{\partial z}{\partial x}\right|_{(1,2)}= 2(1-\ln 2).</equation>

---

**2011年第16题 | 解答题 | 10分**

16. (本题满分10分）

已知函数 f(u,v)具有二阶连续偏导数，<equation>f(1,1)=2</equation>是 f(u,v)的极值，<equation>z=f(x+y,f(x,y))</equation>.求<equation>\left.\frac{\partial^{2} z}{\partial x \partial y}\right|_{(1,1)}.</equation>

**答案:**<equation>= f_{11}^{\prime \prime}(2,2) + f_{2}^{\prime}(2,2)f_{12}^{\prime \prime}(1,1).</equation>

**解析:**对<equation>z = f(x + y,f(x,y))</equation>两端关于<equation>x</equation>求偏导数得<equation>\frac {\partial z}{\partial x} = f _ {1} ^ {\prime} (x + y, f (x, y)) + f _ {2} ^ {\prime} (x + y, f (x, y)) \cdot f _ {1} ^ {\prime} (x, y).</equation>继续对上式两端关于 y求偏导数得<equation>\begin{array}{l} \frac {\partial^ {2} z}{\partial x \partial y} = f _ {1 1} ^ {\prime \prime} (x + y, f (x, y)) + f _ {1 2} ^ {\prime \prime} (x + y, f (x, y)) f _ {2} ^ {\prime} (x, y) \\ + \left[ f _ {2 1} ^ {\prime \prime} (x + y, f (x, y)) + f _ {2 2} ^ {\prime \prime} (x + y, f (x, y)) f _ {2} ^ {\prime} (x, y) \right] f _ {1} ^ {\prime} (x, y) \\ + f _ {2} ^ {\prime} (x + y, f (x, y)) f _ {1 2} ^ {\prime \prime} (x, y). \\ \end{array}</equation>由极值的必要条件可知<equation>f_1^{\prime}(1,1) = f_2^{\prime}(1,1) = 0.</equation>将<equation>f(1,1) = 2,f_1^{\prime}(1,1) = f_2^{\prime}(1,1) = 0</equation>代入上式可得<equation>\left. \frac {\partial^ {2} z}{\partial x \partial y} \right| _ {(1, 1)} = f _ {1 1} ^ {\prime \prime} (2, 2) + f _ {2} ^ {\prime} (2, 2) f _ {1 2} ^ {\prime \prime} (1, 1).</equation>

---

**2009年第10题 | 填空题 | 4分**

10. 设<equation>z=(x+\mathrm{e}^{y})^{x}</equation>，则<equation>\left.\frac{\partial z}{\partial x}\right|_{(1,0)}=</equation>___

**答案:**## 2ln2+1.

**解析:**（法一）在点（1，0）附近，<equation>x > 0</equation>，从而<equation>x+\mathrm{e}^{y}>0, z>0.</equation>对<equation>z=(x+\mathrm{e}^{y})^{x}</equation>两端取对数得到<equation>\ln z = x \ln \left(x + \mathrm {e} ^ {y}\right).</equation>对上式两端关于 x求导得，<equation>\frac {1}{z} \cdot \frac {\partial z}{\partial x} = \ln \left(x + \mathrm {e} ^ {y}\right) + \frac {x}{x + \mathrm {e} ^ {y}}.</equation>当<equation>x = 1</equation>，<equation>y = 0</equation>时，<equation>z = 2.</equation>因此，<equation>\frac{\partial z}{\partial x}\bigg|_{(1,0)} = 2\left(\ln 2 + \frac{1}{2}\right) = 2\ln 2 + 1.</equation>（法二）将<equation>y = 0</equation>代入<equation>z = (x + \mathrm{e}^{y})^{x}</equation>中得到<equation>z(x,0) = (x + 1)^{x}</equation>.于是，<equation>\left. \frac {\partial z}{\partial x} \right| _ {(1, 0)} = \frac {\mathrm {d} \left[ (x + 1) ^ {x} \right]}{\mathrm {d} x} \Bigg | _ {x = 1} = \left[ \mathrm {e} ^ {x \ln (x + 1)} \right] ^ {\prime} \Bigg | _ {x = 1} = \mathrm {e} ^ {x \ln (x + 1)} \left[ \ln (x + 1) + \frac {x}{x + 1} \right] \Bigg | _ {x = 1} = 2 \ln 2 + 1.</equation>

---


#### 二重积分的计算

**2025年第19题 | 解答题 | 12分**

19. 已知平面有界区域<equation>D=\{(x,y)\mid y^{2}\leqslant x,x^{2}\leqslant y\}</equation>，计算二重积分<equation>\iint_{D}(x-y+1)^{2}\mathrm{d}x\mathrm{d}y.</equation>

**解析:**分析 本题主要考查二重积分的计算.

区域 D由两条抛物线围成，且关于直线 y=x对称，故可以考虑使用轮换对称性.

解如图所示，区域D由曲线<equation>y=x^{2}</equation>与<equation>x=y^{2}</equation>围成.由于区域D位于第一象限，故<equation>x=y^{2}</equation>可写成<equation>y=\sqrt{x}.</equation>注意到区域 D关于直线 y=x对称.记<equation>D_{1}</equation>为区域 D位于直线 y=x下方的部分，则由轮换对称性的结论可得<equation>\begin{aligned} \iint_ {D} (x - y + 1) ^ {2} \mathrm {d} x \mathrm {d} y &= \iint_ {D _ {1}} (x - y + 1) ^ {2} \mathrm {d} x \mathrm {d} y + \iint_ {D \backslash D _ {1}} (x - y + 1) ^ {2} \mathrm {d} x \mathrm {d} y \\ &= \iint_ {D _ {1}} \left[ (x - y + 1) ^ {2} + (y - x + 1) ^ {2} \right] \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} \left[ (x - y) ^ {2} + 1 \right] \mathrm {d} x \mathrm {d} y. \end{aligned}</equation>将<equation>D_{1}</equation>写成X型区域.<equation>D _ {1} = \left\{(x, y) \mid x ^ {2} \leqslant y \leqslant x, 0 \leqslant x \leqslant 1 \right\}.</equation>分别计算<equation>\iint_{D_1}\mathrm{d}x\mathrm{d}y,\iint_{D_1}(x - y)^2\mathrm{d}x\mathrm{d}y.</equation><equation>\iint_ {D _ {1}} \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {x ^ {2}} ^ {x} \mathrm {d} y = \int_ {0} ^ {1} \left(x - x ^ {2}\right) \mathrm {d} x = \left(\frac {x ^ {2}}{2} - \frac {x ^ {3}}{3}\right) \Bigg | _ {0} ^ {1} = \frac {1}{2} - \frac {1}{3} = \frac {1}{6}.</equation><equation>\begin{aligned} \iint_ {D _ {1}} (x - y) ^ {2} \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {1} \mathrm {d} x \int_ {x ^ {2}} ^ {x} (x - y) ^ {2} \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {x ^ {2}} ^ {x} \left(x ^ {2} - 2 x y + y ^ {2}\right) \mathrm {d} y \\ &= \int_ {0} ^ {1} \left(x ^ {2} y - x y ^ {2} + \frac {y ^ {3}}{3}\right) \Big | _ {x ^ {2}} ^ {x} \mathrm {d} x = \int_ {0} ^ {1} \left(\frac {x ^ {3}}{3} - x ^ {4} + x ^ {5} - \frac {x ^ {6}}{3}\right) \mathrm {d} x \\ &= \left. \left(- \frac {x ^ {7}}{2 1} + \frac {x ^ {6}}{6} - \frac {x ^ {5}}{5} + \frac {x ^ {4}}{1 2}\right) \right| _ {0} ^ {1} = - \frac {1}{2 1} + \frac {1}{6} - \frac {1}{5} + \frac {1}{1 2} = \frac {1}{4 2 0}. \end{aligned}</equation>因此，<equation>\iint_ {D} (x - y + 1) ^ {2} \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} \left[ (x - y) ^ {2} + 1 \right] \mathrm {d} x \mathrm {d} y = 2 \left(\frac {1}{4 2 0} + \frac {1}{6}\right) = \frac {7 1}{2 1 0}.</equation>

---

**2024年第17题 | 解答题 | 10分**

17. (本题满分10分）设平面有界区域 D位于第一象限，由曲线<equation>x y=\frac{1}{3},</equation><equation>x y=3</equation>与直线<equation>y=\frac{1}{3} x</equation><equation>y=3 x</equation>所围成，请计算<equation>\iint_{D}(1+x-y) \mathrm{d} x \mathrm{d} y.</equation>

**答案:**##<equation>\frac{8}{3}\ln 3.</equation>

**解析:**解区域 D如图（a）所示，注意到区域 D的四条边界曲线中，交换曲线<equation>xy=\frac{1}{3}</equation>与<equation>xy=3</equation>中x， y的位置，可得<equation>yx=\frac{1}{3}</equation>与<equation>yx=3</equation>，即曲线方程不变，故这两条曲线均关于直线 y=x对称，而直线<equation>y=\frac{1}{3} x</equation>与直线 y=3x关于直线 y=x对称，故这四条曲线所围成的区域 D也关于直线 y=x对称，从而对变量 x，y具有轮换对称性.

(a)

(b)

由轮换对称性的结论（2）可得<equation>\iint_{D}x\mathrm{d}x\mathrm{d}y=\iint_{D}y\mathrm{d}x\mathrm{d}y</equation>，故<equation>\iint_ {D} (1 + x - y) \mathrm {d} x \mathrm {d} y = \iint_ {D} \mathrm {d} x \mathrm {d} y + \iint_ {D} x \mathrm {d} x \mathrm {d} y - \iint_ {D} y \mathrm {d} x \mathrm {d} y = \iint_ {D} \mathrm {d} x \mathrm {d} y.</equation>下面用两种方法计算<equation>\iint_{D}\mathrm{d}x\mathrm{d}y.</equation>（法一）在极坐标系下计算.

曲线<equation>xy = \frac{1}{3}</equation>的极坐标方程为<equation>r^2\cos \theta \sin \theta = \frac{1}{3}</equation>，整理可得<equation>r = \sqrt{\frac{2}{3\sin 2\theta}}</equation>，曲线<equation>xy = 3</equation>的极坐标方程为<equation>r^2\cos \theta \sin \theta = 3</equation>，整理可得<equation>r = \sqrt{\frac{6}{\sin 2\theta}}</equation>直线<equation>y = \frac{1}{3} x</equation>的极坐标方程为<equation>\theta = \arctan \frac{1}{3},y = 3x</equation>的极坐标方程为<equation>\theta = \arctan 3.</equation>区域 D的极坐标表示为<equation>D = \left\{(r, \theta) \mid \sqrt {\frac {2}{3 \sin 2 \theta}} \leqslant r \leqslant \sqrt {\frac {6}{\sin 2 \theta}}, \arctan \frac {1}{3} \leqslant \theta \leqslant \arctan 3 \right\}.</equation>于是，<equation>\begin{aligned} \iint_ {D} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} \mathrm {d} \theta \int_ {\sqrt {\frac {2}{3 \sin 2 \theta}}} ^ {\sqrt {\frac {6}{\sin 2 \theta}}} r \mathrm {d} r &= \frac {1}{2} \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} r ^ {2} \left|  \sqrt {\frac {6}{\sin 2 \theta}} \\ \sqrt {\frac {2}{3 \sin 2 \theta}}  \right) \mathrm {d} \theta \\ &= \frac {8}{3} \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} \csc 2 \theta \mathrm {d} \theta = \frac {4}{3} \ln | \csc 2 \theta - \cot 2 \theta | \left| _ {\arctan \frac {1}{3}} ^ {\arctan 3}. \right. \end{aligned}</equation>由于<equation>\csc 2\theta -\cot 2\theta = \frac{1 - \cos 2\theta}{\sin 2\theta} = \frac{2\sin^2\theta}{2\sin \theta \cos \theta} = \tan \theta</equation>，故<equation>\iint_{D}\mathrm{d}x\mathrm{d}y = \frac{4}{3}\ln |\tan \theta |\Bigg|_{\arctan \frac{1}{3}}^{ \arctan 3}</equation>当<equation>\theta = \arctan \frac{1}{3}</equation>时，<equation>\tan \theta = \frac{1}{3}</equation>，当<equation>\theta = \arctan 3</equation>时，<equation>\tan \theta = 3.</equation>因此，<equation>\iint_ {D} \mathrm {d} x \mathrm {d} y = \frac {4}{3} \left(\ln 3 - \ln \frac {1}{3}\right) = \frac {8}{3} \ln 3.</equation>（法二）在直角坐标系下计算.

联立<equation>\left\{\begin{array}{l l} x y=\frac{1}{3}, \\ y=\frac{1}{3} x, \end{array} \right.</equation>解得<equation>\left\{\begin{array}{l l} x=1, \\ y=\frac{1}{3}. \end{array} \right.</equation>联立<equation>\left\{\begin{array}{l l} x y=\frac{1}{3}, \\ y=3 x, \end{array} \right.</equation>解得<equation>\left\{\begin{array}{l l} x=\frac{1}{3}, \\ y=1. \end{array} \right.</equation>联立<equation>\left\{\begin{array}{l l} x y=3, \\ y=\frac{1}{3} x, \end{array} \right.</equation>解得<equation>\left\{\begin{array}{l l} x=3, \\ y=1. \end{array} \right.</equation>联立<equation>\left\{\begin{array}{l l} x y=3, \\ y=3 x, \end{array} \right.</equation>解得<equation>\left\{\begin{array}{l l} x=1, \\ y=3. \end{array} \right.</equation>如图（b）所示，直线<equation>x=1</equation>将区域D分为两部分<equation>D_{1}, D_{2}.</equation><equation>D_{1}</equation>由曲线<equation>xy=\frac{1}{3}</equation>，直线<equation>y=3x</equation>与<equation>x= 1</equation>围成，<equation>D_{2}</equation>由曲线<equation>xy=3</equation>，直线<equation>y=\frac{1}{3} x</equation>与<equation>x=1</equation>围成，<equation>\iint_{D}\mathrm{d}x\mathrm{d}y</equation>等于D的面积，即<equation>D_{1}</equation>的面积与<equation>D_{2}</equation>的面积之和.

因此，<equation>\begin{aligned} \iint_ {D} \mathrm {d} x \mathrm {d} y &= \int_ {\frac {1}{3}} ^ {1} \left(3 x - \frac {1}{3 x}\right) \mathrm {d} x + \int_ {1} ^ {3} \left(\frac {3}{x} - \frac {x}{3}\right) \mathrm {d} x = \left(\frac {3 x ^ {2}}{2} - \frac {1}{3} \ln x\right) \Bigg | _ {\frac {1}{3}} ^ {1} + \left(3 \ln x - \frac {x ^ {2}}{6}\right) \Bigg | _ {1} ^ {3} \\ &= \frac {3}{2} - \frac {1}{6} + \frac {1}{3} \ln \frac {1}{3} + 3 \ln 3 - \frac {3}{2} + \frac {1}{6} = - \frac {1}{3} \ln 3 + 3 \ln 3 = \frac {8}{3} \ln 3. \end{aligned}</equation>

---

**2023年第19题 | 解答题 | 12分**

19. (本题满分12分)

已知平面区域<equation>D=\{(x,y)\mid(x-1)^{2}+y^{2}\leqslant1\}</equation>，计算二重积分<equation>\iint_{D}|\sqrt{x^{2}+y^{2}}-1|\mathrm{d}x\mathrm{d}y.</equation>

**答案:**<equation>- \frac {3 2}{9} - \frac {\pi}{9} + 3 \sqrt {3}.</equation>

**解析:**解注意到<equation>\mid \sqrt{x^{2}+y^{2}}-1\mid</equation>为关于 y的偶函数，而积分区域 D关于 x轴对称，记 D位于上半平面的部分为<equation>D_{1}</equation>即图（b）中的蓝色部分与灰色部分，则<equation>\iint_ {D} \left| \sqrt {x ^ {2} + y ^ {2}} - 1 \right| \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} \left| \sqrt {x ^ {2} + y ^ {2}} - 1 \right| \mathrm {d} x \mathrm {d} y.</equation>在区域<equation>x^{2}+y^{2}\leqslant 1</equation>内，<equation>|\sqrt{x^{2}+y^{2}}-1|=1-\sqrt{x^{2}+y^{2}}</equation>在区域<equation>x^{2}+y^{2}\leqslant 1</equation>外，<equation>|\sqrt{x^{2}+y^{2}}-1|=</equation><equation>\sqrt{x^{2}+y^{2}}-1.</equation>记<equation>x^{2}+y^{2}\leqslant 1</equation>与<equation>D_{1}</equation>的公共部分为<equation>D_{2}</equation>即图（b）中的蓝色部分，则<equation>\begin{aligned} \iint_ {D _ {1}} \left| \sqrt {x ^ {2} + y ^ {2}} - 1 \right| \mathrm {d} x \mathrm {d} y &= \iint_ {D _ {1} \backslash D _ {2}} \left(\sqrt {x ^ {2} + y ^ {2}} - 1\right) \mathrm {d} x \mathrm {d} y + \iint_ {D _ {2}} \left(1 - \sqrt {x ^ {2} + y ^ {2}}\right) \mathrm {d} x \mathrm {d} y \\ &= \iint_ {D _ {1}} \left(\sqrt {x ^ {2} + y ^ {2}} - 1\right) \mathrm {d} x \mathrm {d} y - 2 \iint_ {D _ {2}} \left(\sqrt {x ^ {2} + y ^ {2}} - 1\right) \mathrm {d} x \mathrm {d} y. \end{aligned}</equation>下面分别计算<equation>\iint_{D_{1}}(\sqrt{x^{2}+y^{2}}-1)\mathrm{d}x\mathrm{d}y, \iint_{D_{2}}(\sqrt{x^{2}+y^{2}}-1)\mathrm{d}x\mathrm{d}y.</equation>圆周<equation>( x-1 )^{2}+y^{2}=1</equation>的极坐标方程为<equation>r=2\cos \theta</equation>，故<equation>D_{1}</equation>在极坐标系下的表示为<equation>D _ {1} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2 \cos \theta , 0 \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation>于是，<equation>\begin{aligned} \iint_ {D _ {1}} \left(\sqrt {x ^ {2} + y ^ {2}} - 1\right) \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \int_ {0} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {2 \cos \theta} (r - 1) \cdot r \mathrm {d} r &= \int_ {0} ^ {\frac {\pi}{2}} \left(\frac {r ^ {3}}{3} - \frac {r ^ {2}}{2}\right) \Bigg | _ {0} ^ {2 \cos \theta} \mathrm {d} \theta \\ &= \int_ {0} ^ {\frac {\pi}{2}} \left(\frac {8}{3} \cos^ {3} \theta - 2 \cos^ {2} \theta\right) \mathrm {d} \theta = \frac {8}{3} \int_ {0} ^ {\frac {\pi}{2}} \cos^ {3} \theta \mathrm {d} \theta - 2 \int_ {0} ^ {\frac {\pi}{2}} \cos^ {2} \theta \mathrm {d} \theta \\ &= \frac {8}{3} \cdot \frac {2}{3} - 2 \cdot \frac {\pi}{4} = \frac {1 6}{9} - \frac {\pi}{2}. \end{aligned}</equation>联立<equation>\left\{\begin{array}{l l}x^{2}+y^{2}=1,\\ (x-1)^{2}+y^{2}=1,\end{array}\right.</equation>解得<equation>\left\{\begin{array}{l l}x=\frac{1}{2},\\ y=\pm \frac{\sqrt{3}}{2},\end{array}\right.</equation>从而圆周<equation>x^{2}+y^{2}=1</equation>与圆周<equation>(x-1)^{2}+y^{2}=1</equation>在上半平面的交点为<equation>\left(\frac{1}{2},\frac{\sqrt{3}}{2}\right).</equation>连接原点O与点<equation>\left(\frac{1}{2},\frac{\sqrt{3}}{2}\right)</equation>的直线方程为<equation>y=\sqrt{3} x</equation>其极坐标方程为<equation>\theta=\frac{\pi}{3}.</equation>如图（c）所示，<equation>D_{2}</equation>可以由直线<equation>\theta=\frac{\pi}{3}</equation>分为两部分，在极坐标系下的表示为<equation>D _ {2} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 1, 0 \leqslant \theta \leqslant \frac {\pi}{3} \right\} \cup \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2 \cos \theta , \frac {\pi}{3} \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation>于是，<equation>\iint_ {D _ {2}} \left(\sqrt {x ^ {2} + y ^ {2}} - 1\right) \mathrm {d} x \mathrm {d} y \xlongequal {\text {极 坐 标}} \int_ {0} ^ {\frac {\pi}{3}} \mathrm {d} \theta \int_ {0} ^ {1} (r - 1) \cdot r \mathrm {d} r + \int_ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {2 \cos \theta} (r - 1) \cdot r \mathrm {d} r.</equation>其中，<equation>\int_ {0} ^ {\frac {\pi}{3}} \mathrm {d} \theta \int_ {0} ^ {1} (r - 1) \cdot r \mathrm {d} r = \int_ {0} ^ {\frac {\pi}{3}} \left(\frac {r ^ {3}}{3} - \frac {r ^ {2}}{2}\right) \Big | _ {0} ^ {1} \mathrm {d} \theta = \int_ {0} ^ {\frac {\pi}{3}} \left(\frac {1}{3} - \frac {1}{2}\right) \mathrm {d} \theta = - \frac {1}{6} \cdot \frac {\pi}{3} = - \frac {\pi}{1 8}.</equation><equation>\begin{aligned} \int_ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {2 \cos \theta} (r - 1) \cdot r \mathrm {d} r &= \int_ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \left(\frac {8}{3} \cos^ {3} \theta - 2 \cos^ {2} \theta\right) \mathrm {d} \theta = \frac {8}{3} \int_ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \cos^ {3} \theta \mathrm {d} \theta - 2 \int_ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \cos^ {2} \theta \mathrm {d} \theta \\ &= \frac {8}{3} \int_ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \left(1 - \sin^ {2} \theta\right) \mathrm {d} (\sin \theta) - \int_ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \left(1 + \cos 2 \theta\right) \mathrm {d} \theta \\ &= \frac {8}{3} \left(\sin \theta - \frac {\sin^ {3} \theta}{3}\right) \left| _ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} - \frac {\pi}{6} - \frac {\sin 2 \theta}{2} \right| _ {\frac {\pi}{3}} ^ {\frac {\pi}{2}} \\ &= - \frac {\pi}{6} + \frac {8}{3} \left(\frac {2}{3} - \frac {3 \sqrt {3}}{8}\right) + \frac {\sqrt {3}}{4} = - \frac {\pi}{6} + \frac {1 6}{9} - \frac {3 \sqrt {3}}{4}. \end{aligned}</equation>因此，<equation>\iint_ {D _ {2}} \left(\sqrt {x ^ {2} + y ^ {2}} - 1\right) \mathrm {d} x \mathrm {d} y = - \frac {\pi}{1 8} - \frac {\pi}{6} + \frac {1 6}{9} - \frac {3 \sqrt {3}}{4} = - \frac {2 \pi}{9} + \frac {1 6}{9} - \frac {3 \sqrt {3}}{4}.</equation>综上所述，<equation>\iint_ {D} \left| \sqrt {x ^ {2} + y ^ {2}} - 1 \right| \mathrm {d} x \mathrm {d} y = 2 \left(\frac {1 6}{9} - \frac {\pi}{2} + \frac {4 \pi}{9} - \frac {3 2}{9} + \frac {3 \sqrt {3}}{2}\right) = - \frac {3 2}{9} - \frac {\pi}{9} + 3 \sqrt {3}.</equation>

---

**2022年第14题 | 填空题 | 5分**

14. 已知函数 f(x)<equation>\left\{\begin{array}{l l} {\mathrm{e}^{x},}&{0 \leqslant x \leqslant 1,}\\ {0,}&{\mathrm{其他},}\end{array} \right.</equation>则<equation>\int_{-\infty}^{+\infty}\mathrm{d}x\int_{-\infty}^{+\infty}f(x)f(y-x)\mathrm{d}y=</equation>___.

**解析:**解 根据 f(x)的定义，f(x)仅在 0≤x≤1时非零，f(y-x)仅在 0≤y-x≤1时非零.于是，f(x)f(y-x)仅在区域 D = {（x,y）|0≤y-x≤1,0≤x≤1}，即 D = {（x,y）|x≤y≤x+1,0≤x≤1}上非零.<equation>\begin{aligned} \int_ {- \infty} ^ {+ \infty} \mathrm {d} x \int_ {- \infty} ^ {+ \infty} f (x) f (y - x) \mathrm {d} y &= \int_ {0} ^ {1} \mathrm {d} x \int_ {x} ^ {x + 1} \mathrm {e} ^ {x} \mathrm {e} ^ {y - x} \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {x} ^ {x + 1} \mathrm {e} ^ {y} \mathrm {d} y \\ &= \int_ {0} ^ {1} \left(\mathrm {e} ^ {x + 1} - \mathrm {e} ^ {x}\right) \mathrm {d} x = \left(\mathrm {e} ^ {x + 1} - \mathrm {e} ^ {x}\right) \Bigg | _ {0} ^ {1} \\ &= \left(\mathrm {e} ^ {2} - \mathrm {e}\right) - (\mathrm {e} - 1) = \mathrm {e} ^ {2} - 2 \mathrm {e} + 1. \end{aligned}</equation>

---

**2022年第19题 | 解答题 | 12分**

19. (本题满分12分）

已知平面区域 D = {（x,y）| y-2≤x≤<equation>\sqrt{4-y^{2}}</equation>, 0≤y≤2} ，计算 I =<equation>\iint_{D} \frac{(x-y)^{2}}{x^{2}+y^{2}} \mathrm{d} x \mathrm{d} y.</equation>

**解析:**解 在极坐标系下计算.

由 D的表达式可知，如图（a）所示，D是由直线<equation>y=x+2</equation>，圆<equation>x^{2}+y^{2}=4</equation>以及 x轴围成的部分.直线<equation>y=x+2</equation>在极坐标系下的表示为<equation>r=\frac{2}{\sin \theta -\cos \theta}</equation>，圆<equation>x^{2}+y^{2}=4</equation>在极坐标系下的表示为<equation>r=2.</equation>(a)

(b)

如图（b）所示，将 D分为两部分<equation>D_{1}</equation>和<equation>D_{2}.</equation><equation>D _ {1} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2, 0 \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation><equation>D _ {2} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \frac {2}{\sin \theta - \cos \theta}, \frac {\pi}{2} \leqslant \theta \leqslant \pi \right\}.</equation>因此，<equation>\begin{aligned} \iint_ {D} \frac {\left(x - y\right) ^ {2}}{x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \iint_ {D} \frac {r ^ {2} \left(\cos \theta - \sin \theta\right) ^ {2}}{r ^ {2}} \cdot r \mathrm {d} r \mathrm {d} \theta &= \iint_ {D} \left(\cos \theta - \sin \theta\right) ^ {2} \cdot r \mathrm {d} r \mathrm {d} \theta \\ &= \int_ {0} ^ {\frac {\pi}{2}} \left(\cos \theta - \sin \theta\right) ^ {2} \mathrm {d} \theta \int_ {0} ^ {2} r \mathrm {d} r + \int_ {\frac {\pi}{2}} ^ {\pi} \left(\cos \theta - \sin \theta\right) ^ {2} \mathrm {d} \theta \int_ {0} ^ {\frac {2}{\sin \theta - \cos \theta}} r \mathrm {d} r \\ &= 2 \int_ {0} ^ {\frac {\pi}{2}} \left(1 - 2 \sin \theta \cos \theta\right) \mathrm {d} \theta + \int_ {\frac {\pi}{2}} ^ {\pi} \left(\cos \theta - \sin \theta\right) ^ {2} \cdot \frac {r ^ {2}}{2} \Bigg | _ {0} ^ {\frac {2}{\sin \theta - \cos \theta}} \mathrm {d} \theta \\ &= 2 \left(\frac {\pi}{2} - \sin^ {2} \theta \Bigg | _ {0} ^ {\frac {\pi}{2}}\right) + \int_ {\frac {\pi}{2}} ^ {\pi} \left(\cos \theta - \sin \theta\right) ^ {2} \cdot \frac {2}{\left(\sin \theta - \cos \theta\right) ^ {2}} \mathrm {d} \theta \\ &= \pi - 2 + 2 \times \left(\pi - \frac {\pi}{2}\right) = 2 \pi - 2. \end{aligned}</equation>

---

**2021年第19题 | 解答题 | 12分**

19. (本题满分12分)

设有界区域 D是圆<equation>x^{2}+y^{2}=1</equation>与直线 y=x以及 x轴在第一象限围成的部分，请计算二重积分<equation>\iint_{D} \mathrm{e}^{(x+y)^{2}}(x^{2}-y^{2})\mathrm{d}x\mathrm{d}y.</equation>

**答案:**<equation>\frac {1}{8} (\mathrm {e} - 1) ^ {2}.</equation>

**解析:**区域 D在极坐标系下的表示为<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 1, 0 \leqslant \theta \leqslant \frac {\pi}{4} \right\}.</equation>在极坐标系下计算积分.<equation>\begin{aligned} \iint_ {D} \mathrm {e} ^ {(x + y) ^ {2}} \left(x ^ {2} - y ^ {2}\right) \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \iint_ {D} \mathrm {e} ^ {r ^ {2} (\cos \theta + \sin \theta) ^ {2}} \cdot r ^ {2} \left(\cos^ {2} \theta - \sin^ {2} \theta\right) \cdot r \mathrm {d} r \mathrm {d} \theta \\ &= \iint_ {D} \mathrm {e} ^ {r ^ {2} (1 + \sin 2 \theta)} r ^ {3} \cos 2 \theta \mathrm {d} r \mathrm {d} \theta = \int_ {0} ^ {1} r ^ {3} \mathrm {d} r \int_ {0} ^ {\frac {\pi}{4}} \mathrm {e} ^ {r ^ {2} (1 + \sin 2 \theta)} \cos 2 \theta \mathrm {d} \theta \\ &= \int_ {0} ^ {1} r ^ {3} \mathrm {d} r \int_ {0} ^ {\frac {\pi}{4}} \mathrm {e} ^ {r ^ {2} (1 + \sin 2 \theta)} \mathrm {d} \left(\frac {1 + \sin 2 \theta}{2}\right) = \frac {1}{2} \int_ {0} ^ {1} r ^ {3} \cdot \frac {\mathrm {e} ^ {r ^ {2} (1 + \sin 2 \theta)}}{r ^ {2}} \Bigg | _ {0} ^ {\frac {\pi}{4}} \mathrm {d} r \\ &= \frac {1}{2} \int_ {0} ^ {1} r \left(\mathrm {e} ^ {2 r ^ {2}} - \mathrm {e} ^ {r ^ {2}}\right) \mathrm {d} r = \frac {1}{4} \int_ {0} ^ {1} \left(\mathrm {e} ^ {2 r ^ {2}} - \mathrm {e} ^ {r ^ {2}}\right) \mathrm {d} \left(r ^ {2}\right) \\ &= \frac {1}{4} \left(\frac {\mathrm {e} ^ {2 r ^ {2}}}{2} - \mathrm {e} ^ {r ^ {2}}\right) \Bigg | _ {0} ^ {1} = \frac {1}{8} \left(\mathrm {e} ^ {2} - 2 \mathrm {e} + 1\right) = \frac {1}{8} (\mathrm {e} - 1) ^ {2}. \end{aligned}</equation>

---

**2020年第18题 | 解答题 | 10分**

18. (本题满分10分)

设 D = {(x,y) | x²+y²≤1,y≥0}, 连续函数 f(x,y)满足 f(x,y) = y<equation>\sqrt{1-x^{2}}</equation>+ x<equation>\iint_{D} f(x,y)\mathrm{d}x\mathrm{d}y</equation>，求<equation>\iint_{D} xf(x,y)\mathrm{d}x\mathrm{d}y.</equation>

**答案:**# 128
