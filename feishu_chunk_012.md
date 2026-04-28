考虑正项级数<equation>\sum_{n=1}^{\infty} \frac{\mid b_{n}\mid -b_{n}}{2}.</equation>对<equation>\{b_{n}\}</equation>中小于0的项，<equation>a_{n} < b_{n} < 0</equation>，于是<equation>\left| a _ {n} \right| = - a _ {n} > - b _ {n} = \frac {\left| b _ {n} \right| - b _ {n}}{2} > 0.</equation>对<equation>\{b_{n}\}</equation>中大于等于0的项，<equation>\left| a _ {n} \right| \geqslant 0 = \frac {\left| b _ {n} \right| - b _ {n}}{2}.</equation>从而，对所有正整数 n，都有<equation>|a_{n}| \geqslant \frac{|b_{n}| - b_{n}}{2} \geqslant 0.</equation>由正项级数的比较审敛法可知，级数<equation>\sum_{n=1}^{\infty} \frac{\mid b_{n}\mid -b_{n}}{2}</equation>收敛. 进一步，<equation>\sum_ {n = 1} ^ {\infty} \left| b _ {n} \right| = \sum_ {n = 1} ^ {\infty} \left[ 2 \left(\frac {\left| b _ {n} \right| - b _ {n}}{2}\right) + b _ {n} \right] = 2 \sum_ {n = 1} ^ {\infty} \frac {\left| b _ {n} \right| - b _ {n}}{2} + \sum_ {n = 1} ^ {\infty} b _ {n}.</equation>由<equation>\sum_{n=1}^{\infty}b_{n}</equation>收敛以及收敛级数的性质可知，<equation>\sum_{n=1}^{\infty}|\boldsymbol{b}_{n}|</equation>收敛，从而<equation>\sum_{n=1}^{\infty}b_{n}</equation>绝对收敛.

因此，“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的充分条件.

再考虑必要性.

由<equation>a_{n} < b_{n}</equation>可得<equation>-b_{n} < -a_{n}</equation>. 由<equation>\sum_{n=1}^{\infty} a_{n}</equation>与<equation>\sum_{n=1}^{\infty} b_{n}</equation>均收敛可知<equation>\sum_{n=1}^{\infty} (-a_{n})</equation>与<equation>\sum_{n=1}^{\infty} (-b_{n})</equation>均收敛.于是，同充分性的证明可知<equation>\sum_{n=1}^{\infty} (-b_{n})</equation>绝对收敛蕴含<equation>\sum_{n=1}^{\infty} (-a_{n})</equation>绝对收敛，即<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛蕴含<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛.

因此，“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的必要条件.

综上所述，“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的充分必要条件，应选A.

---

**2019年第3题 | 选择题 | 4分 | 答案: D**

3. 设<equation>\{u_{n}\}</equation>是单调增加的有界数列，则下列级数中收敛的是（    ）

A.<equation>\sum_{n=1}^{\infty}\frac{u_{n}}{n}</equation>B.<equation>\sum_{n=1}^{\infty}(-1)^{n}\frac{1}{u_{n}}</equation>C.<equation>\sum_{n=1}^{\infty}\left(1-\frac{u_{n}}{u_{n+1}}\right)</equation>D.<equation>\sum_{n=1}^{\infty}\left(u_{n+1}^{2}-u_{n}^{2}\right)</equation>

答案: D

**解析:**解（法一）由于<equation>u_{n+1}^{2}-u_{n}^{2}=(u_{n+1}+u_{n})(u_{n+1}-u_{n})</equation>，而<equation>\{u_{n}\}</equation>有界，故存在正数M，使得<equation>|u_{n+1}^{2}-u_{n}^{2}| \leqslant 2M|u_{n+1}-u_{n}| \frac{u_{n}}{2M(u_{n+1}-u_{n})}.</equation>单调增加考虑正项级数<equation>\sum_{n=1}^{\infty}(u_{n+1}-u_{n}).</equation>该级数的部分和为<equation>s _ {n} = \sum_ {k = 1} ^ {n} \left(u _ {k + 1} - u _ {k}\right) = \left(u _ {2} - u _ {1}\right) + \left(u _ {3} - u _ {2}\right) + \dots + \left(u _ {n + 1} - u _ {n}\right) = u _ {n + 1} - u _ {1}.</equation>由于<equation>\{u_{n}\}</equation>是单调增加的有界数列，故<equation>\lim_{n\to \infty}u_{n+1}</equation>存在，从而<equation>\lim_{n\to \infty}s_{n}</equation>存在，级数<equation>\sum_{n=1}^{\infty}\left(u_{n+1}-u_{n}\right)</equation>收敛由比较审敛法可知，<equation>\sum_{n=1}^{\infty}\left|u_{n+1}^{2}-u_{n}^{2}\right|</equation>收敛，从而<equation>\sum_{n=1}^{\infty}\left(u_{n+1}^{2}-u_{n}^{2}\right)</equation>收敛.应选D.

（法二）排除法.

选项A：取<equation>u_{n}=1-\frac{1}{n}</equation>，则<equation>\frac{u_{n}}{n}=\frac{1}{n}-\frac{1}{n^{2}}.</equation>由于<equation>\sum_{n=1}^{\infty}\frac{1}{n}</equation>发散，<equation>\sum_{n=1}^{\infty}\frac{1}{n^{2}}</equation>收敛，故<equation>\sum_{n=1}^{\infty}\left(\frac{1}{n}-\frac{1}{n^{2}}\right)</equation>发散.选项A不正确.

选项B、C：取<equation>u_{n}=-\frac{1}{n}</equation>，则<equation>(-1)^{n}\frac{1}{u_{n}}=(-1)^{n+1}n,\sum_{n=1}^{\infty}(-1)^{n}\frac{1}{u_{n}}</equation>发散；<equation>1-\frac{u_{n}}{u_{n+1}}=1-\frac{n+1}{n}=</equation><equation>-\frac{1}{n},\sum_{n=1}^{\infty}\left(1-\frac{u_{n}}{u_{n+1}}\right)</equation>发散. 选项B、C不正确.

由排除法可知，应选D.

---

**2016年第19题 | 解答题 | 10分**

19. (本题满分10分)

已知函数 f(x)可导，且<equation>f(0)=1</equation><equation>0<f^{\prime}(x)<\frac{1}{2}</equation>.设数列<equation>\{x_{n}\}</equation>满足<equation>x_{n+1}=f\left(x_{n}\right)\left(n=1,2,\cdots\right)</equation>.证明：

I. 级数<equation>\sum_{n=1}^{\infty}\left(x_{n+1}-x_{n}\right)</equation>绝对收敛；

II.<equation>\lim_{n\to\infty}x_{n}</equation>存在，且<equation>0<\lim_{n\to\infty}x_{n}<2.</equation>

**答案:**## （I）证明略；（Ⅱ）证明略.

**解析:**证（I）由题设知，<equation>\left| x _ {n + 1} - x _ {n} \right| = \left| f \left(x _ {n}\right) - f \left(x _ {n - 1}\right) \right| \frac {\text {拉 格朗 日}}{\text {中 值 定 理}} \left| f ^ {\prime} \left(\xi_ {n}\right) \left(x _ {n} - x _ {n - 1}\right) \right| \leqslant \frac {1}{2} \left| x _ {n} - x _ {n - 1} \right|,</equation>其中<equation>\xi_{n}</equation>介于<equation>x_{n}</equation>与<equation>x_{n - 1}</equation>之间（若<equation>x_{n} = x_{n - 1}</equation>，则取<equation>\xi_{n} = x_{n}</equation>，本题均作类似处理).递推得到<equation>\left| x _ {n + 1} - x _ {n} \right| \leqslant \frac {1}{2} \left| x _ {n} - x _ {n - 1} \right| \leqslant \frac {1}{2} \cdot \frac {1}{2} \left| x _ {n - 1} - x _ {n - 2} \right| \leqslant \dots \leqslant \frac {1}{2 ^ {n - 1}} \left| x _ {2} - x _ {1} \right|.</equation>又级数<equation>\sum_{n=1}^{\infty}\frac{1}{2^{n-1}} \mid x_{2}-x_{1}\mid = \mid x_{2}-x_{1}\mid \sum_{n=1}^{\infty}\frac{1}{2^{n-1}} = 2 \mid x_{2}-x_{1}\mid</equation>收敛，故由比较审敛法知，级数<equation>\sum_{n=1}^{\infty}\mid x_{n+1}-x_{n}\mid</equation>收敛，即<equation>\sum_{n=1}^{\infty}\left(x_{n+1}-x_{n}\right)</equation>绝对收敛，结论得证.

（Ⅱ）首先证明<equation>\lim x_{n}</equation>存在.


令<equation>S_{n} = \sum_{k = 1}^{n}\left(x_{k + 1} - x_{k}\right) = x_{n + 1} - x_{1}</equation>. 由（I）中结论知，级数<equation>\sum_{n = 1}^{\infty}\left(x_{n + 1} - x_{n}\right)</equation>绝对收敛，从而收敛，即<equation>\lim_{n\to \infty}S_n</equation>存在. 又<equation>x_{n + 1} = S_n + x_1</equation>，故<equation>\lim_{n\to \infty}x_{n + 1}</equation>存在，即<equation>\lim_{n\to \infty}x_n</equation>存在，结论得证.

（法二）单调有界准则.

若<equation>x_{1} < x_{2}</equation>，则由<equation>f^{\prime}(x) > 0</equation>知，<equation>x _ {3} - x _ {2} = f \left(x _ {2}\right) - f \left(x _ {1}\right) \frac {\text {拉 格 朗 日}}{\text {中 值 定 理}} f ^ {\prime} \left(\xi_ {2}\right) \left(x _ {2} - x _ {1}\right) > 0,</equation>其中<equation>x_{1} < \xi_{2} < x_{2}</equation>，于是<equation>x_{2} < x_{3}</equation>。假设<equation>x_{k} < x_{k + 1}</equation>，则由<equation>f^{\prime}(x) > 0</equation>知，<equation>x _ {k + 2} - x _ {k + 1} = f \left(x _ {k + 1}\right) - f \left(x _ {k}\right) \frac {\text {拉 格 朗 日}}{\text {中 值 定 理}} f ^ {\prime} \left(\xi_ {k + 1}\right) \left(x _ {k + 1} - x _ {k}\right) > 0,</equation>其中<equation>x_{k} < \xi_{k + 1} < x_{k + 1}</equation>，即<equation>x_{k + 1} < x_{k + 2}</equation>.由数学归纳法知，数列<equation>\{x_{n}\}</equation>单调增加.

由于<equation>f^{\prime}(x) > 0</equation>，故<equation>x _ {n + 1} - 1 = f \left(x _ {n}\right) - f (0) \frac {\text {拉 格 朗 日}}{\text {中 值 定 理}} f ^ {\prime} \left(\eta_ {n}\right) x _ {n} < f ^ {\prime} \left(\eta_ {n}\right) x _ {n + 1},</equation>其中<equation>\eta_{n}</equation>介于<equation>x_{n}</equation>与0之间，从而<equation>[1-f^{\prime}(\eta_{n})]x_{n+1} < 1.</equation>由<equation>0 < f^{\prime}(\eta_{n}) < \frac{1}{2}</equation>知，<equation>1-f^{\prime}(\eta_{n}) > \frac{1}{2} > 0.</equation>因此，<equation>x _ {n + 1} < \frac {1}{1 - f ^ {\prime} \left(\eta_ {n}\right)} < 2.</equation>综上所述，数列<equation>\{x_{n}\}</equation>单调增加且有上界.由单调有界准则知，<equation>\lim x_{n}</equation>存在.

若<equation>x_{1} > x_{2}</equation>，同理可证，数列<equation>\{x_{n}\}</equation>单调减少且有下界.由单调有界准则知，<equation>\lim x_{n}</equation>存在.

若<equation>x_{1} = x_{2}</equation>，则<equation>\forall n\in \mathbf{N}_{+},x_{n} = x_{1}</equation>，此时<equation>\lim_{n\to \infty}x_{n}</equation>显然存在.

再证明<equation>0 < \lim_{n\to \infty}x_{n} < 2.</equation>设<equation>\lim_{n\to \infty}x_{n} = a</equation>，对等式<equation>x_{n + 1} = f(x_n)</equation>两端令<equation>n\to \infty</equation>，由<equation>f(x)</equation>可导从而连续得到<equation>a = f(a).</equation>下面用两种方法证明<equation>0 < a < 2.</equation>（法一）由拉格朗日中值定理知，存在<equation>\xi</equation>介于a与0之间，使得<equation>f(a)-f(0)=f^{\prime}(\xi)a</equation>又<equation>f(a)=a</equation><equation>f(0)=1</equation>，故有<equation>a-1=f^{\prime}(\xi)a</equation>，解得<equation>a=\frac{1}{1-f^{\prime}(\xi)}.</equation>由题设知，<equation>0 < f^{\prime}(\xi) < \frac{1}{2}</equation>，于是<equation>\frac{1}{2} < 1-f^{\prime}(\xi) < 1</equation>，从而<equation>0 < 1 < a=\frac{1}{1-f^{\prime}(\xi)} < 2</equation>，结论得证.

（法二）令 F(x）=f(x）-x，则 F(a）=f(a）-a=0.又 f(x)可导且 0 < f'(x) <<equation>\frac{1}{2}</equation>，故<equation>F^{\prime}(x)=f^{\prime}(x)-1<0</equation>，从而 F(x)单调减少.因此要证 0 < a < 2，只需证明 F(0)>F(a)= 0 > F(2).

显然 F（0）=f（0）=1>0.又<equation>F (2) = f (2) - 2 = f (2) - f (0) - 1 \frac {\text {拉 格 朗 日}}{\text {中 值 定 理}} 2 f ^ {\prime} (\eta) - 1 < 0,</equation>其中<equation>0 < \eta < 2</equation>，故<equation>F(0) > F(a) = 0 > F(2)</equation>，结论得证.

---

**2014年第19题 | 解答题 | 10分**

19. (本题满分10分)

9. (本题满分10分)

设数列<equation>\{a_{n}\}</equation><equation>\{b_{n}\}</equation>满足<equation>0 < a_{n} < \frac{\pi}{2}, 0 < b_{n} < \frac{\pi}{2}, \cos a_{n}-a_{n}=\cos b_{n}</equation>，且级数<equation>\sum_{n=1}^{\infty} b_{n}</equation>收敛.

I. 证明<equation>\lim_{n\rightarrow \infty} a_{n}=0;</equation>II. 证明级数<equation>\sum_{n=1}^{\infty}\frac{a_{n}}{b_{n}}</equation>收敛.

**解析:**证（I）（法一）由于<equation>0 < a_{n} < \frac{\pi}{2}, 0 < b_{n} < \frac{\pi}{2}, \cos b_{n} = \cos a_{n} - a_{n} < \cos a_{n}</equation>，且<equation>\cos x</equation>在<equation>\left( 0, \frac{\pi}{2} \right)</equation>上单调减少，故<equation>0 < a_{n} < b_{n} < \frac{\pi}{2}.</equation>又级数<equation>\sum_{n=1}^{\infty} b_{n}</equation>收敛，故<equation>\lim_{n\to \infty}b_{n}=0</equation>，从而由夹逼准则知<equation>\lim_{n\to \infty}a_{n}=0</equation>，结论得证.

（法二）当<equation>x\in \left(0,\frac{\pi}{2}\right)</equation>时，<equation>\cos x > 1 - \frac{x^2}{2}</equation>，从而<equation>-\cos x < \frac{x^2}{2} -1.</equation>由于<equation>b_{n}\in \left(0,\frac{\pi}{2}\right)</equation>，故<equation>a _ {n} = \cos a _ {n} - \cos b _ {n} < 1 + \frac {b _ {n} ^ {2}}{2} - 1 = \frac {b _ {n} ^ {2}}{2},</equation>即<equation>0 < a_{n} < \frac{b_{n}^{2}}{2}</equation>. 又级数<equation>\sum_{n = 1}^{\infty}b_{n}</equation>收敛，故<equation>\lim_{n\to \infty}b_n = 0</equation>，从而由夹逼准则知<equation>\lim_{n\to \infty}a_n = 0</equation>，结论得证.

（Ⅱ）（法一）由（I）中法一知，<equation>0 < a_{n} < b_{n} < \frac{\pi}{2}</equation>从而<equation>\begin{aligned} \frac {a _ {n}}{b _ {n}} &= \frac {\cos a _ {n} - \cos b _ {n}}{b _ {n}} = \frac {2 \sin \frac {a _ {n} + b _ {n}}{2} \sin \frac {b _ {n} - a _ {n}}{2}}{b _ {n}} \\ < \frac {2 \cdot \frac {a _ {n} + b _ {n}}{2} \cdot \frac {b _ {n} - a _ {n}}{2}}{b _ {n}} \quad (x > 0 \text {时}, \sin x < x) \\ &= \frac {b _ {n} ^ {2} - a _ {n} ^ {2}}{2 b _ {n}} < \frac {b _ {n} ^ {2}}{2 b _ {n}} = \frac {1}{2} b _ {n}. \end{aligned}</equation>又<equation>\sum_{n = 1}^{\infty}b_{n}</equation>收敛，故由比较审敛法知，<equation>\sum_{n = 1}^{\infty}\frac{a_n}{b_n}</equation>收敛，结论得证.

（法二）由（I）中法一知，<equation>0 < a_{n} < b_{n} < \frac{\pi}{2}</equation>从而由拉格朗日中值定理知，存在<equation>\xi_{n}\in\left(a_{n},b_{n}\right)\subset\left(0,\frac{\pi}{2}\right)</equation>，使得<equation>\frac{a_{n}}{b_{n}}=\frac{\cos a_{n}-\cos b_{n}}{b_{n}}=\frac{-\sin \xi_{n}\cdot\left(a_{n}-b_{n}\right)}{b_{n}}=\frac{\sin \xi_{n}}{b_{n}}\left(b_{n}-a_{n}\right)<\frac{\sin \xi_{n}}{b_{n}}\cdot b_{n}=\sin \xi_{n}<\xi_{n}<b_{n}.</equation>又<equation>\sum_{n=1}^{\infty}b_{n}</equation>收敛，故由比较审敛法知，<equation>\sum_{n=1}^{\infty}\frac{a_{n}}{b_{n}}</equation>收敛，结论得证.

（法三）同（I）中法二得到<equation>0 < a_{n} < \frac{b_{n}^{2}}{2}</equation>，于是由<equation>b_{n} > 0</equation>知，<equation>0 < \frac{a_{n}}{b_{n}} < \frac{1}{2} b_{n}</equation>. 又<equation>\sum_{n = 1}^{\infty}b_{n}</equation>收敛，故由比较审敛法知<equation>\sum_{n = 1}^{\infty}\frac{a_n}{b_n}</equation>收敛，结论得证.

（法四）由（I）知，<equation>\lim_{n\to \infty}a_n = \lim_{n\to \infty}b_n = 0.</equation>又<equation>\cos b_{n} = \cos a_{n} - a_{n}</equation>，故<equation>\begin{aligned} \lim _ {n \rightarrow \infty} \frac {\frac {a _ {n}}{b _ {n}}}{b _ {n}} &= \lim _ {n \rightarrow \infty} \frac {a _ {n}}{b _ {n} ^ {2}} = \lim _ {n \rightarrow \infty} \left(\frac {1 - \cos b _ {n}}{b _ {n} ^ {2}} \cdot \frac {a _ {n}}{1 - \cos b _ {n}}\right) = \frac {1}{2} \lim _ {n \rightarrow \infty} \frac {a _ {n}}{1 - \cos b _ {n}} \\ &= \frac {1}{2} \lim _ {n \rightarrow \infty} \frac {a _ {n}}{1 - \left(\cos a _ {n} - a _ {n}\right)} = \frac {1}{2} \lim _ {n \rightarrow \infty} \frac {1}{\frac {1 - \cos a _ {n}}{a _ {n}} + 1} = \frac {1}{2}. \end{aligned}</equation>再由<equation>\sum_{n = 1}^{\infty}b_{n}</equation>收敛及比较审敛法的极限形式知，<equation>\sum_{n = 1}^{\infty}\frac{a_n}{b_n}</equation>收敛，结论得证.

---

**2009年第4题 | 选择题 | 4分 | 答案: C**

4. 设有两个数列<equation>\{a_{n}\} ,\{b_{n}\}</equation>，若<equation>\lim_{n\to\infty}a_{n}=0</equation>，则（    ）

A. 当<equation>\sum_{n=1}^{\infty}b_{n}</equation>收敛时，<equation>\sum_{n=1}^{\infty}a_{n}b_{n}</equation>收敛

C. 当<equation>\sum_{n=1}^{\infty} \left| b_{n} \right|</equation>收敛时，<equation>\sum_{n=1}^{\infty} a_{n}^{2} b_{n}^{2}</equation>收敛

B. 当<equation>\sum_{n=1}^{\infty}b_{n}</equation>发散时，<equation>\sum_{n=1}^{\infty}a_{n}b_{n}</equation>发散

D. 当<equation>\sum_{n=1}^{\infty}|\boldsymbol{b}_{n}|</equation>发散时，<equation>\sum_{n=1}^{\infty}a_{n}^{2}b_{n}^{2}</equation>发散

答案: C

**解析:**解 令<equation>a_{n}=\frac{(-1)^{n+1}}{\sqrt{n}}, b_{n}=\frac{(-1)^{n+1}}{\sqrt{n}}</equation>，则<equation>\lim_{n\to\infty}a_{n}=0</equation><equation>\sum_{n=1}^{\infty}b_{n}</equation>收敛，但<equation>\sum_{n=1}^{\infty}a_{n}b_{n}=\sum_{n=1}^{\infty}\frac{1}{n}</equation>发散.选项 A不正确.

令<equation>a_{n}=\frac{1}{n}, b_{n}=\frac{1}{n}</equation>，则<equation>\lim_{n\to\infty}a_{n}=0</equation><equation>\sum_{n=1}^{\infty}b_{n}</equation>发散，但<equation>\sum_{n=1}^{\infty}a_{n}b_{n}=\sum_{n=1}^{\infty}\frac{1}{n^{2}}</equation>收敛.选项B不正确.

令<equation>a_{n}=\frac{1}{n}, b_{n}=\frac{1}{n}</equation>，则<equation>\lim_{n\to\infty}a_{n}=0</equation><equation>\sum_{n=1}^{\infty}|\boldsymbol{b}_{n}|</equation>发散，但<equation>\sum_{n=1}^{\infty}a_{n}^{2}b_{n}^{2}=\sum_{n=1}^{\infty}\frac{1}{n^{4}}</equation>收敛.选项D不正确.

由排除法可知，应选C.

下面证明选项C正确.

由<equation>\sum_{n=1}^{\infty} \mid b_{n}\mid</equation>收敛知，<equation>\lim_{n\rightarrow \infty} \mid b_{n}\mid =0</equation>，于是存在<equation>N_{1}</equation>，使得当 n > N1时，<equation>\mid b_{n}\mid <1</equation>，从而<equation>b_{n}^{2}\leqslant \mid b_{n}\mid</equation>又<equation>\lim_{n\rightarrow \infty} a_{n}=0</equation>，故存在<equation>N_{2}</equation>，使得当 n > N2时，<equation>\mid a_{n}\mid <1</equation>，从而<equation>a_{n}^{2}<1</equation>.令 N =<equation>\max \{N_{1},N_{2}\}</equation>，则当 n > N时，<equation>0\leqslant a_{n}^{2}b_{n}^{2}\leqslant \mid b_{n}\mid</equation>，再由比较审敛法知，<equation>\sum_{n=1}^{\infty} a_{n}^{2}b_{n}^{2}</equation>收敛.

---


#### 傅里叶级数

**2025年第12题 | 填空题 | 5分**
12. 已知函数 f(x)<equation>\left\{\begin{array}{l l}0,&0 \leqslant x < \frac{1}{2}\\ x^{2},&\frac{1}{2} \leqslant x \leqslant 1\end{array} \right.</equation>，的傅里叶级数为<equation>\sum_{n=1}^{\infty} b_{n} \sin n \pi x</equation>，S(x)为<equation>\sum_{n=1}^{\infty} b_{n} \sin n \pi x</equation>的和函数，则<equation>S\left(-\frac{7}{2}\right)=</equation>
**解析: **解 由 S(x)为正弦级数的和函数可知，<equation>S ( x )</equation>为[0,1]上的 f(x)作奇延拓后再作周期为2的周期延拓所得函数的傅里叶级数.

由于 S（x）是周期为2的奇函数，故<equation>S \left(- \frac {7}{2}\right) = S \left(- 4 + \frac {1}{2}\right) = S \left(\frac {1}{2}\right).</equation>又因为<equation>x=\frac{1}{2}</equation>是<equation>f(x)</equation>的间断点，所以由狄利克雷收敛定理可得<equation>S \left(\frac {1}{2}\right) = \frac {1}{2} \left[ \lim _ {x \rightarrow \frac {1}{2} ^ {-}} f (x) + \lim _ {x \rightarrow \frac {1}{2} ^ {+}} f (x) \right] = \frac {1}{2} \left(0 + \frac {1}{4}\right) = \frac {1}{8}.</equation>因此，<equation>S\left(-\frac{7}{2}\right)=\frac{1}{8}.</equation>

---

**2024年第13题 | 填空题 | 5分**
13. 已知函数 f(x)=x+1，若 f(x)<equation>\frac{a_{0}}{2}+\sum_{n=1}^{\infty} a_{n} \cos n x,x \in[0,\pi]</equation>，则<equation>\lim_{n \to \infty} n^{2} \sin a_{2n-1}=</equation>___.
**答案: **\[ -\frac{1}{\pi} \]
**解析: **解 由于 f(x)的傅里叶级数展开式为余弦级数，故 f(x)为偶函数.由余弦级数的系数公式可知，当 n≥1时，<equation>\begin{aligned} a _ {n} &= \frac {2}{\pi} \int_ {0} ^ {\pi} (x + 1) \cos n x d x = \frac {2}{\pi} \left(\int_ {0} ^ {\pi} \cos n x d x + \int_ {0} ^ {\pi} x \cos n x d x\right) \\ &= \frac {2}{\pi} \left[ \frac {1}{n} \sin n x \Big | _ {0} ^ {\pi} + \frac {1}{n} \int_ {0} ^ {\pi} x d (\sin n x) \right] = \frac {2}{n \pi} \int_ {0} ^ {\pi} x d (\sin n x) \\ &= \frac {2}{n \pi} \left(x \sin n x \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} \sin n x d x\right) = - \frac {2}{n \pi} \int_ {0} ^ {\pi} \sin n x d x \\ &= \frac {2}{n \pi} \cdot \frac {\cos n x}{n} \Big | _ {0} ^ {\pi} = \frac {2}{n ^ {2} \pi} (\cos n \pi - 1) = \frac {2}{n ^ {2} \pi} [ (- 1) ^ {n} - 1 ]. \end{aligned}</equation>于是，<equation>a _ {2 n - 1} = \frac {2}{(2 n - 1) ^ {2} \pi} [ (- 1) ^ {2 n - 1} - 1 ] = \frac {2}{(2 n - 1) ^ {2} \pi} (- 1 - 1) = \frac {- 4}{(2 n - 1) ^ {2} \pi}.</equation>因此，<equation>\lim _ {n \rightarrow \infty} n ^ {2} \sin a _ {2 n - 1} = \lim _ {n \rightarrow \infty} n ^ {2} \sin \frac {- 4}{(2 n - 1) ^ {2} \pi} = \lim _ {n \rightarrow \infty} \frac {- 4 n ^ {2}}{(2 n - 1) ^ {2} \pi} = - \frac {1}{\pi}.</equation>

---

**2023年第13题 | 填空题 | 5分**
13. 设 f(x)为周期为2的周期函数，且 f(x)=1-x,x∈[0,1]，若 f(x)<equation>\frac{a_{0}}{2}+\sum_{n=1}^{\infty} a_{n} \cos n \pi x</equation>，则<equation>\sum_{n=1}^{\infty} a_{2n}=</equation>___.
**解析: **解 由于 f(x) 的傅里叶级数展开式为余弦级数，故 f(x)为偶函数.由余弦级数的系数计算公式可知，当 n≥1时，<equation>\begin{aligned} a _ {n} &= 2 \int_ {0} ^ {1} (1 - x) \cos n \pi x \mathrm {d} x = 2 \left(\int_ {0} ^ {1} \cos n \pi x \mathrm {d} x - \int_ {0} ^ {1} x \cos n \pi x \mathrm {d} x\right) \\ &= 2 \left[ \frac {1}{n \pi} \sin n \pi x \Big | _ {0} ^ {1} - \frac {1}{n \pi} \int_ {0} ^ {1} x \mathrm {d} (\sin n \pi x) \right] = - \frac {2}{n \pi} \int_ {0} ^ {1} x \mathrm {d} (\sin n \pi x) \\ &= - \frac {2}{n \pi} \left(x \sin n \pi x \Big | _ {0} ^ {1} - \int_ {0} ^ {1} \sin n \pi x \mathrm {d} x\right) = \frac {2}{n \pi} \int_ {0} ^ {1} \sin n \pi x \mathrm {d} x \\ &= \frac {2}{n \pi} \cdot \left(- \frac {\cos n \pi x}{n \pi}\right) \Big | _ {0} ^ {1} = \frac {- 2}{n ^ {2} \pi^ {2}} (\cos n \pi - 1). \end{aligned}</equation>于是，<equation>a _ {2 n} = \frac {- 2}{(2 n) ^ {2} \pi^ {2}} \left(\cos 2 n \pi - 1\right) = \frac {- 1}{2 n ^ {2} \pi^ {2}} (1 - 1) = 0.</equation>因此，<equation>\sum_{n=1}^{\infty} a_{2n}=0.</equation>

---

**2013年第3题 | 选择题 | 4分 | 答案: C**
3. 设<equation>f(x)=\left| x-\frac{1}{2}\right|, b_{n}=2\int_{0}^{1} f(x)\sin(n\pi x)\mathrm{d}x(n=1,2,\cdots).</equation>令<equation>S(x)=\sum_{n=1}^{\infty}b_{n}\sin(n\pi x),</equation>则<equation>S\left(-\frac{9}{4}\right)=</equation>(    )

A.<equation>\frac{3}{4}</equation>B.<equation>\frac{1}{4}</equation>C.<equation>-\frac{1}{4}</equation>D.<equation>-\frac{3}{4}</equation>
答案: C
**解析: **解设<equation>F ( x )</equation>是以2为周期的奇函数，且当<equation>- 1 \leqslant x \leqslant 1</equation>时，<equation>F (x) = \left\{ \begin{array}{l l} f (x), & 0 < x < 1, \\ - f (- x), & - 1 < x < 0, \\ 0, & x = 0, \pm 1. \end{array} \right.</equation>如右图所示，<equation>F ( x )</equation>的傅里叶系数为<equation>\widetilde {a} _ {n} = \int_ {- 1} ^ {1} F (x) \cos n \pi x \mathrm {d} x = 0, n = 0, 1, 2, \dots ,</equation>

---


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


#### 求幂级数的收敛半径、收敛区间和收敛域

**2022年第14题 | 填空题 | 5分**

14. 已知级数<equation>\sum_{n=1}^{\infty} \frac{n!}{n^{n}} \mathrm{e}^{-nx}</equation>的收敛域为<equation>(a,+\infty)</equation>, 则 a= ___

**答案:**<equation>- 1.</equation>

**解析:**解（法一）令<equation>u_{n}=\frac{n!}{n^{n}} \mathrm{e}^{-n x}</equation>，则原级数为<equation>\sum_{n=1}^{\infty} u_{n}.</equation><equation>\lim_{n\to \infty}\left|\frac{u_{n+1}}{u_{n}}\right|=\lim_{n\to \infty}\frac{(n+1)!}{(n+1)^{n+1}}\cdot \frac{n^{n}}{n!}\mathrm{e}^{-x}=\mathrm{e}^{-x}\lim_{n\to \infty}\frac{n^{n}}{(n+1)^{n}}=\mathrm{e}^{-x}\lim_{n\to \infty}\frac{1}{\left(1+\frac{1}{n}\right)^{n}}=\mathrm{e}^{-1-x}.</equation>由比值审敛法可知，当<equation>\mathrm{e}^{-1-x}<1</equation>时，<equation>\sum_{n=1}^{\infty} u_{n}</equation>收敛，当<equation>\mathrm{e}^{-1-x}>1</equation>时，<equation>\sum_{n=1}^{\infty} u_{n}</equation>发散.由于指数函数单调增加，故<equation>\mathrm{e}^{-1-x}<1</equation>等价于<equation>-1-x<0</equation>即<equation>x>-1</equation>因此，当<equation>x>-1</equation>时，函数项级数<equation>\sum_{n=1}^{\infty}\frac{n!}{n^{n}} \mathrm{e}^{-nx}</equation>收敛，当<equation>x<-1</equation>时，函数项级数<equation>\sum_{n=1}^{\infty}\frac{n!}{n^{n}} \mathrm{e}^{-nx}</equation>发散.

当<equation>x = -1</equation>时，<equation>\mathrm{e}^{-1 - x} = 1.</equation>此时利用比值审敛法无法判定<equation>\sum_{n = 1}^{\infty} u_n</equation>的收敛性. 但是，将<equation>x = -1</equation>代回原级数可得原级数为<equation>\sum_{n = 1}^{\infty}\frac{n!}{n^n}\mathrm{e}^n.</equation>该级数的一般项极限不为0，从而发散（见注）.

因此，函数项级数<equation>\sum_{n = 1}^{\infty}\frac{n!}{n^n}\mathrm{e}^{-nx}</equation>的收敛域为<equation>(-1, +\infty)</equation>，<equation>a = -1.</equation>（法二）令<equation>t = \mathrm{e}^{-x}</equation>，则<equation>\sum_{n = 1}^{\infty}\frac{n!}{n^n}\mathrm{e}^{-nx} = \sum_{n = 1}^{\infty}\frac{n!}{n^n}t^n.</equation><equation>\lim _ {n \rightarrow \infty} \frac {(n + 1) !}{(n + 1) ^ {n + 1}} \cdot \frac {n ^ {n}}{n !} = \lim _ {n \rightarrow \infty} \frac {n ^ {n}}{(n + 1) ^ {n}} = \lim _ {n \rightarrow \infty} \frac {1}{\left(1 + \frac {1}{n}\right) ^ {n}} = \frac {1}{\mathrm {e}}.</equation>于是，<equation>\sum_{n = 1}^{\infty}\frac{n!}{n^n} t^n</equation>的收敛半径为e，收敛区间为<equation>(-\mathrm{e},\mathrm{e})</equation>解<equation>- \mathrm{e} < \mathrm{e}^{-x} < \mathrm{e}</equation>可得，<equation>x > - 1</equation>因此，当<equation>x > - 1</equation>时，函数项级数<equation>\sum_{n=1}^{\infty} \frac{n!}{n^{n}} \mathrm{e}^{-n x}</equation>收敛。并且，当<equation>x < - 1</equation>时，<equation>\mathrm{e}^{-x} > \mathrm{e}</equation>函数项级数<equation>\sum_{n=1}^{\infty} \frac{n!}{n^{n}} \mathrm{e}^{-n x}</equation>发散.

其余同法一.

---

**2020年第4题 | 选择题 | 4分 | 答案: A**

4. 设 R为幂级数<equation>\sum_{n=1}^{\infty} a_{n} x^{n}</equation>的收敛半径，r是实数，则（    )

A. 当<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>发散时，<equation>|r|\geqslant R</equation>B. 当<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>收敛时，<equation>|r|\leqslant R</equation>C. 当<equation>|r|\geqslant R</equation>时，<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>发散 D. 当<equation>|r|\leqslant R</equation>时，<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>收敛

答案: A

**解析:**解 由幂级数的收敛半径的定义可知，当<equation>| r | < R</equation>时，级数<equation>\sum_{n=1}^{\infty} a_{n} r^{n}</equation>绝对收敛.又因为<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>为<equation>\sum_{n=1}^{\infty} a_{n} r^{n}</equation>的偶数项子级数，所以此时由<equation>\sum_{n=1}^{\infty} a_{n} r^{n}</equation>收敛可得<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>收敛.

若<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>发散，则<equation>\sum_{n=1}^{\infty} a_{n} r^{n}</equation>不可能绝对收敛.因此，<equation>| r | \geqslant R</equation>或者，由<equation>| r | < R \Rightarrow \sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>收敛的逆否命题为<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>发散<equation>\Rightarrow | r | \geqslant R</equation>可知，<equation>| r | \geqslant R</equation>应选A.

下面说明其余选项均不正确.

选项B、C：取<equation>a_{n}=\left\{ \begin{array}{ll}1,&n=2k-1,\\ 0,&n=2k, \end{array} \right. k=1,2,3,\dots</equation>，则<equation>\sum_{n=1}^{\infty}a_{n}x^{n}=\sum_{n=1}^{\infty}x^{2n-1}.</equation>该级数为缺项幂级数，易求得其收敛半径为1. 对任何实数<equation>r,\sum_{n=1}^{\infty}a_{2n}r^{2n}</equation>均收敛.因此，选项C不正确.任取<equation>|r| > 1</equation>即可否定选项B.

选项D：当<equation>|r| < R</equation>时，级数<equation>\sum_{n=1}^{\infty} a_{n} r^{n}</equation>绝对收敛.于是由<equation>\sum_{n=1}^{\infty} a_{n} r^{n}</equation>收敛可得<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>收敛.但是，当<equation>|r|=R</equation>时，<equation>\sum_{n=1}^{\infty} a_{n} r^{n}</equation>可能收敛，也可能发散.此时，无法确定<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>的收敛性.

例如：取<equation>a_{n}=1,n=1,2,3,\dots</equation>，则<equation>\sum_{n=1}^{\infty}a_{n}x^{n}=\sum_{n=1}^{\infty}x^{n}</equation>.该幂级数的收敛半径为1.取<equation>r=1</equation>，则<equation>\sum_{n=1}^{\infty}1^{2n}</equation>发散.<equation>|r|=R</equation>时，<equation>\sum_{n=1}^{\infty}a_{2n}r^{2n}</equation>收敛的例子同选项B、C.

---

**2015年第3题 | 选择题 | 4分 | 答案: B**

3. 若级数<equation>\sum_{n=1}^{\infty} a_{n}</equation>条件收敛，则<equation>x=\sqrt{3}</equation>与 x=3依次为幂级数<equation>\sum_{n=1}^{\infty} n a_{n} ( x-1 )^{n}</equation>的（    ）

A. 收敛点，收敛点 B. 收敛点，发散点 C. 发散点，收敛点 D. 发散点，发散点

答案: B

**解析:**解（法一）由<equation>\sum_{n=1}^{\infty} a_{n}</equation>条件收敛知，<equation>\sum_{n=1}^{\infty} a_{n}</equation>收敛，<equation>\sum_{n=1}^{\infty} |a_{n}|</equation>发散.于是幂级数<equation>\sum_{n=1}^{\infty} a_{n} x^{n}</equation>在<equation>x=1</equation>处收敛，从而由阿贝尔定理知，<equation>\sum_{n=1}^{\infty} a_{n} x^{n}</equation>的收敛半径R满足<equation>R\geqslant 1</equation>假设<equation>R > 1</equation>，则由阿贝尔定理知，<equation>\sum_{n=1}^{\infty} |a_{n}|</equation>收敛，矛盾，故假设不成立，从而<equation>R=1.</equation>幂级数<equation>\sum_{n=1}^{\infty} a_{n}(x-1)^{n}</equation>与<equation>\sum_{n=1}^{\infty} a_{n}x^{n}</equation>的收敛半径相同，均为1.又逐项求导不改变收敛半径，故<equation>\sum_{n=1}^{\infty} n a_{n}(x-1)^{n-1}</equation>的收敛半径为1，从而<equation>\sum_{n=1}^{\infty} n a_{n}(x-1)^{n}</equation>的收敛半径为1.因此<equation>\sum_{n=1}^{\infty} n a_{n}(x-1)^{n}</equation>当<equation>|x-1| < 1</equation>即<equation>x\in(0,2)</equation>时收敛；当<equation>|x-1| > 1</equation>即<equation>x\in(-\infty ,0)\cup(2,+\infty)</equation>时发散.由于<equation>0 < \sqrt{3} < 2 < 3</equation>故<equation>\sum_{n=1}^{\infty} n a_{n}(x-1)^{n}</equation>在<equation>x=\sqrt{3}</equation>处收敛，在<equation>x=3</equation>处发散，从而选B.

（法二）特殊值法.

令<equation>a_{n}=\frac{(-1)^{n}}{n}</equation>满足<equation>\sum_{n=1}^{\infty} a_{n}</equation>条件收敛.又<equation>\sum_{n=1}^{\infty} n a_{n}(x-1)^{n}=\sum_{n=1}^{\infty}(-1)^{n}(x-1)^{n}</equation>的收敛域为 (0,2)，故该幂级数在<equation>x=\sqrt{3}</equation>处收敛，在<equation>x=3</equation>处发散，从而选B.

---

**2011年第2题 | 选择题 | 4分 | 答案: C**

2. 设数列<equation>\{a_{n}\}</equation>单调减少，<equation>\lim_{n\to \infty}a_{n}=0,S_{n}=\sum_{k=1}^{n}a_{k}</equation>（ n=1，2，<equation>\cdots</equation>）无界，则幂级数<equation>\sum_{n=1}^{\infty}a_{n}(x-1)^{n}</equation>的收敛域为（    ）

A. (-1,1] B. [-1,1) C. [0,2) D. (0,2]

答案: C

**解析:**解（法一）由于数列<equation>\left\{a_{n}\right\}</equation>单调减少且<equation>\lim_{n\to \infty}a_{n}=0</equation>，故<equation>a_{n}>0,n=1,2,\dots</equation>由莱布尼茨定理知，<equation>\sum_{n=1}^{\infty}a_{n}(-1)^{n}</equation>收敛，即<equation>\sum_{n=1}^{\infty}a_{n}x^{n}</equation>在<equation>x=-1</equation>处收敛，由阿贝尔定理知，<equation>\sum_{n=1}^{\infty}a_{n}x^{n}</equation>的收敛半径<equation>R\geqslant 1</equation>又<equation>S_{n}</equation>无界，故<equation>\sum_{n=1}^{\infty}a_{n}</equation>发散，即<equation>\sum_{n=1}^{\infty}a_{n}x^{n}</equation>在<equation>x=1</equation>处发散，由阿贝尔定理知，<equation>R\leqslant 1</equation>，于是<equation>R=1.</equation>因此<equation>\sum_{n=1}^{\infty} a_{n} x^{n}</equation>的收敛域为[-1,1)，从而<equation>\sum_{n=1}^{\infty} a_{n} (x-1)^{n}</equation>的收敛点满足<equation>- 1\leqslant x-1<1</equation>即收敛域为[0,2).应选C.


幂级数<equation>\sum_{n=1}^{\infty} a_{n} ( x-1 )^{n}</equation>的收敛域是以 x=1为中心，故排除选项A、B.又当 x=2时，<equation>\sum_{n=1}^{\infty} a_{n} ( x-1 )^{n}</equation><equation>= \sum_{n=1}^{\infty} a_{n}</equation>发散，故 x=2不在其收敛域中，从而排除选项D.应选C.

---


### 多元函数积分学


#### 交换积分次序与坐标系之间的转化

**2025年第4题 | 选择题 | 5分 | 答案: A**

4. 设函数 f(x,y) 连续，则<equation>\int_{-2}^{2}\mathrm{d}x\int_{4-x^{2}}^{4}f(x,y)\mathrm{d}y=</equation>(    )

A.<equation>\int_{0}^{4}\left[\int_{-2}^{-\sqrt{4-y}}f(x,y)\mathrm{d}x+\int_{\sqrt{4-y}}^{2}f(x,y)\mathrm{d}x\right]\mathrm{d}y</equation>B.<equation>\int_{0}^{4}\left[\int_{-2}^{\sqrt{4-y}}f(x,y)\mathrm{d}x+\int_{\sqrt{4-y}}^{2}f(x,y)\mathrm{d}x\right]\mathrm{d}y</equation>C.<equation>\int_{0}^{4}\left[\int_{-2}^{-\sqrt{4-y}}f(x,y)\mathrm{d}x+\int_{2}^{\sqrt{4-y}}f(x,y)\mathrm{d}x\right]\mathrm{d}y</equation>D.<equation>2\int_{0}^{4}\mathrm{d}y\int_{\sqrt{4-y}}^{2}f(x,y)\mathrm{d}x</equation>

答案: A

**解析:**解 如图所示，二次积分<equation>\int_{-2}^{2}\mathrm{d}x\int_{4-x^{2}}^{4}f(x,y)\mathrm{d}y</equation>对应的二重积分的积分区域 D为图中灰色区域.<equation>D = \left\{(x, y) \mid 4 - x ^ {2} \leqslant y \leqslant 4, - 2 \leqslant x \leqslant 2 \right\}.</equation>当 x < 0时，解 y = 4 - x²可得 x = -<equation>\sqrt{4-y}</equation>，当 x > 0时，解 y = 4 - x²可得 x =<equation>\sqrt{4-y}</equation>.于是，将 D写成 Y型区域需要将其分块，<equation>D=\{(x,y)\mid-2\leqslant x\leqslant-\sqrt{4-y},0\leqslant y\leqslant 4\} \cup \{(x,y)\mid\sqrt{4-y}\leqslant x\leqslant 2,0\leqslant y\leqslant 4\}</equation>从而，<equation>\int_ {- 2} ^ {2} \mathrm {d} x \int_ {4 - x ^ {2}} ^ {4} f (x, y) \mathrm {d} y = \iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {4} \left[ \int_ {- 2} ^ {- \sqrt {4 - y}} f (x, y) \mathrm {d} x + \int_ {\sqrt {4 - y}} ^ {2} f (x, y) \mathrm {d} x \right] \mathrm {d} y.</equation>选项A正确，选项B、C不正确.

对选项D，该选项正确意味着<equation>\iint_{D} f(x,y)\mathrm{d}x\mathrm{d}y = 2\iint_{D_1} f(x,y)\mathrm{d}x\mathrm{d}y</equation>，其中<equation>D_{1}</equation>为D位于y轴右边的部分，而该式成立需要<equation>f(x,y)</equation>是关于x的偶函数，但题干条件中并没有这一信息，故该选项不正确.例如，取<equation>f(x,y) = x</equation>，则<equation>\iint_{D} f(x,y)\mathrm{d}x\mathrm{d}y = 0</equation>，而<equation>\iint_{D_1} f(x,y)\mathrm{d}x\mathrm{d}y > 0.</equation>因此，应选A.

---

**2015年第4题 | 选择题 | 4分 | 答案: B**

4. 设 D是第一象限中的曲线<equation>2 x y=1, 4 x y=1</equation>与直线 y=x,y=<equation>\sqrt{3} x</equation>围成的平面区域，函数 f(x,y)在 D上连续，则<equation>\iint \limits_{D} f(x,y)\mathrm{d} x\mathrm{d} y=</equation>(    )

A.<equation>\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \mathrm{d} \theta \int_{\frac{1}{2 \sin 2 \theta}}^{\frac{1}{\sin 2 \theta}} f ( r \cos \theta,r \sin \theta ) r \mathrm{d} r</equation>B.<equation>\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \mathrm{d} \theta \int_{\frac{1}{\sqrt{2 \sin 2 \theta}}}^{\frac{1}{\sqrt{\sin 2 \theta}}} f ( r \cos \theta,r \sin \theta ) r \mathrm{d} r</equation>C.<equation>\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \mathrm{d} \theta \int_{\frac{1}{2 \sin 2 \theta}}^{\frac{1}{\sin 2 \theta}} f ( r \cos \theta,r \sin \theta ) \mathrm{d} r</equation>D.<equation>\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \mathrm{d} \theta \int_{\frac{1}{\sqrt{2 \sin 2 \theta}}}^{\frac{1}{\sqrt{\sin 2 \theta}}} f ( r \cos \theta,r \sin \theta ) \mathrm{d} r</equation>

答案: B

**解析:**解 将曲线<equation>2 x y=1</equation>，<equation>4 x y=1</equation>，直线<equation>y=x</equation>，<equation>y=\sqrt{3} x</equation>改写为极坐标形式.积分区域如图所示.<equation>2 x y = 1 \Rightarrow r ^ {2} \sin 2 \theta = 1 \Rightarrow r = \frac {1}{\sqrt {\sin 2 \theta}},</equation><equation>4 x y = 1 \Rightarrow 2 r ^ {2} \sin 2 \theta = 1 \Rightarrow r = \frac {1}{\sqrt {2 \sin 2 \theta}},</equation><equation>y = x \Rightarrow \theta = \frac {\pi}{4},</equation><equation>y = \sqrt {3} x \Rightarrow \theta = \frac {\pi}{3},</equation><equation>\mathrm {d} x \mathrm {d} y = r \mathrm {d} r \mathrm {d} \theta .</equation>于是，积分区域<equation>D</equation>在极坐标系下表示为<equation>D = \left\{(r, \theta) \mid \frac {1}{\sqrt {2 \sin 2 \theta}} \leqslant r \leqslant \frac {1}{\sqrt {\sin 2 \theta}}, \frac {\pi}{4} \leqslant \theta \leqslant \frac {\pi}{3} \right\}.</equation>因此，<equation>\iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{3}} \mathrm {d} \theta \int_ {\frac {1}{\sqrt {2 \sin 2 \theta}}} ^ {\frac {1}{\sqrt {\sin 2 \theta}}} f (r \cos \theta , r \sin \theta) r \mathrm {d} r.</equation>应选B.

---

**2014年第3题 | 选择题 | 4分 | 答案: D**

3. 设 f(x,y)是连续函数，则<equation>\int_{0}^{1}\mathrm{d}y\int_{-\sqrt{1-y^{2}}}^{1-y}f(x,y)\mathrm{d}x=</equation>(    )

A.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{x-1}f(x,y)\mathrm{d}y+\int_{-1}^{0}\mathrm{d}x\int_{0}^{\sqrt{1-x^{2}}}f(x,y)\mathrm{d}y</equation>B.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{1-x}f(x,y)\mathrm{d}y+\int_{-1}^{0}\mathrm{d}x\int_{-\sqrt{1-x^{2}}}^{0}f(x,y)\mathrm{d}y</equation>C.<equation>\int_{0}^{\frac{\pi}{2}}\mathrm{d}\theta \int_{0}^{\frac{1}{\cos \theta+\sin \theta}}f(r\cos \theta,r\sin \theta)\mathrm{d}r+\int_{\frac{\pi}{2}}^{\pi}\mathrm{d}\theta \int_{0}^{1}f(r\cos \theta,r\sin \theta)\mathrm{d}r</equation>D.<equation>\int_{0}^{\frac{\pi}{2}}\mathrm{d}\theta \int_{0}^{\frac{1}{\cos \theta+\sin \theta}}f(r\cos \theta,r\sin \theta)r\mathrm{d}r+\int_{\frac{\pi}{2}}^{\pi}\mathrm{d}\theta \int_{0}^{1}f(r\cos \theta,r\sin \theta)r\mathrm{d}r</equation>

答案: D

**解析:**分析本题主要考查二次积分的积分次序交换和换元法.观察选项A、B，是将先x后y的二次积分化为先y后x的二次积分，结合积分区域的图形来转化会比较方便；观察选项C、D，是将原二次积分化为极坐标系下的二次积分，需要用到换元公式<equation>\iint_{D} f(x,y)\mathrm{d}x\mathrm{d}y=\iint_{D} f(r\cos \theta ,r\sin \theta )r\mathrm{d}r\mathrm{d}\theta.</equation>解题设中二次积分的积分区域为<equation>D=\{(x,y)\mid 0\leqslant y\leqslant 1,-\sqrt{1-y^{2}}\leqslant x\leqslant 1-y\}</equation>，将区域D分成两部分<equation>D_{1}</equation>和<equation>D_{2}</equation>（如上图所示），其中<equation>\begin{array}{l} D _ {1} = \left\{(x, y) \mid 0 \leqslant y \leqslant \sqrt {1 - x ^ {2}}, - 1 \leqslant x \leqslant 0 \right\}, \\ D _ {2} = \left\{(x, y) \mid 0 \leqslant y \leqslant 1 - x, 0 \leqslant x \leqslant 1 \right\}. \\ \end{array}</equation>于是<equation>\int_0^1\mathrm{d}y\int_{- \sqrt{1 - y^2}}^{1 - y}f(x,y)\mathrm{d}x = \int_{-1}^0\mathrm{d}x\int_0^{\sqrt{1 - x^2}}f(x,y)\mathrm{d}y + \int_0^1\mathrm{d}x\int_0^{1 - x}f(x,y)\mathrm{d}y</equation>，从而选项A、B均不正确.

在极坐标变换下，区域<equation>D_{1}</equation>的边界方程为<equation>\theta = \frac{\pi}{2},\theta = \pi,r = 1</equation>；区域<equation>D_{2}</equation>的边界方程为<equation>\theta = 0,\theta = \frac{\pi}{2},r = \frac{1}{\cos \theta + \sin \theta}</equation>设区域<equation>D_{1},D_{2}</equation>在极坐标变换下对应于直角坐标平面<equation>rO\theta</equation>上的区域为<equation>D_{1}^{\prime},D_{2}^{\prime}</equation>，则<equation>D _ {1} ^ {\prime} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 1, \frac {\pi}{2} \leqslant \theta \leqslant \pi \right\},</equation><equation>D _ {2} ^ {\prime} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \frac {1}{\cos \theta + \sin \theta}, 0 \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation>从而<equation>\int_ {0} ^ {1} \mathrm {d} y \int_ {- \sqrt {1 - y ^ {2}}} ^ {1 - y} f (x, y) \mathrm {d} x = \int_ {0} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {\frac {1}{\cos \theta + \sin \theta}} f (r \cos \theta , r \sin \theta) r \mathrm {d} r + \int_ {\frac {\pi}{2}} ^ {\pi} \mathrm {d} \theta \int_ {0} ^ {1} f (r \cos \theta , r \sin \theta) r \mathrm {d} r.</equation>应选 D.

选项C错误的原因是少了雅可比式<equation>r</equation>

---


#### 第二类曲线积分

**2025年第14题 | 填空题 | 5分**
14. 已知有向曲线 L是沿抛物线<equation>y=1-x^{2}</equation>从点（1,0）到点（-1,0）的一段，则曲线积分<equation>\int_{L}(y+\cos x)\mathrm{d}x+(2x+\cos y)\mathrm{d}y=</equation>___
**答案: **<equation>\frac {4}{3} - 2 \sin 1.</equation>
**解析: **解（法一）如图所示，添加一条有向线段<equation>L_{1}</equation>，使之起点为<equation>(-1,0)</equation>，终点为（1，0），则<equation>L + L_{1}</equation>围成一个平面封闭区域<equation>D,L + L_{1}</equation>为<equation>D</equation>的正向边界.

注意到区域 D关于 y轴对称，记<equation>D_{1}</equation>为 D位于 y轴右边的部分.将<equation>D_{1}</equation>写成 X型区域.<equation>D _ {1} = \left\{(x, y) \mid 0 \leqslant y \leqslant 1 - x ^ {2}, 0 \leqslant x \leqslant 1 \right\}.</equation>记<equation>P ( x,y)=y+\cos x, Q ( x,y)=2 x+\cos y</equation>，则<equation>\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}=2-1=1.</equation>根据格林公式，<equation>\begin{aligned} \oint_ {L + L _ {1}} (y + \cos x) \mathrm {d} x + (2 x + \cos y) \mathrm {d} y &= \iint_ {D} \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} \mathrm {d} x \mathrm {d} y = 2 \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {1 - x ^ {2}} \mathrm {d} y \\ &= 2 \int_ {0} ^ {1} \left(1 - x ^ {2}\right) \mathrm {d} x = 2 \left(1 - \frac {x ^ {3}}{3} \Big | _ {0} ^ {1}\right) = \frac {4}{3}. \end{aligned}</equation>另一方面，<equation>\int_ {L _ {1}} \left(y + \cos x\right) \mathrm {d} x + \left(2 x + \cos y\right) \mathrm {d} y \stackrel {y = 0} {=} \int_ {L _ {1}} \cos x \mathrm {d} x = \int_ {- 1} ^ {1} \cos x \mathrm {d} x = 2 \int_ {0} ^ {1} \cos x \mathrm {d} x = 2 \sin 1.</equation>因此，<equation>\int_{L}(y + \cos x)\mathrm{d}x + (2x + \cos y)\mathrm{d}y = \frac{4}{3} - 2\sin 1.</equation>（法二）曲线 L的参数方程为<equation>\left\{\begin{array}{l}x=x,\\ y=1-x^{2},\end{array}\right.</equation>x从1变到-1.将参数方程代入曲线积分可得<equation>\int_{L}(y+\cos x)\mathrm{d}x+(2x+\cos y)\mathrm{d}y=\int_{1}^{-1}\left\{(1-x^{2}+\cos x)+[2x+\cos(1-x^{2})]\cdot(-2x)\right\}\mathrm{d}x</equation><equation>= \int_{1}^{-1}\left[1-5x^{2}+\cos x-2x\cos \left(1-x^{2}\right)\right]\mathrm{d}x</equation><equation>\frac{\mathrm{对称性}}{}2\int_{0}^{1}\left(5x^{2}-1-\cos x\right)\mathrm{d}x=2\left(\frac{5x^{3}}{3}-x-\sin x\right)\Bigg|_{0}^{1}</equation><equation>= 2\left(\frac{2}{3}-\sin 1\right)=\frac{4}{3}-2\sin 1.</equation>

---

**2024年第20题 | 解答题 | 12分**
20. (本题满分12分)

已知有向曲线 L为球面<equation>x^{2}+y^{2}+z^{2}=2x</equation>与平面 2x-z-1=0的交线，从z轴正向往z轴负向看去为逆时针方向，计算曲线积分<equation>\int_{L}(6xyz-yz^{2})\mathrm{d}x+2x^{2}z\mathrm{d}y+xyz\mathrm{d}z.</equation>
**答案: **##<equation>\frac{4\sqrt{5}}{25}\pi.</equation>
**解析: **分析 本题主要考查第二类曲线积分的计算.

本题中的曲线 L是一条封闭曲线，可以考虑利用斯托克斯公式将曲线积分转化为曲面积分.

解 曲线<equation>L</equation>的方程为<equation>\left\{ \begin{array}{l l} x^{2} + y^{2} + z^{2} = 2x, \\ 2x - z - 1 = 0. \end{array} \right.</equation>如图所示，<equation>L</equation>为封闭曲线，其所围平面<equation>2x - z - 1 = 0</equation>上的有界部分为<equation>\Sigma</equation>，取上侧.

记所求曲线积分为<equation>I</equation>，由于曲线<equation>L</equation>的方向和曲面<equation>\Sigma</equation>的方向符合右手法则，故根据斯托克斯公式，<equation>\begin{aligned} I &= \oint_ {L} \left(6 x y z - y z ^ {2}\right) \mathrm {d} x + 2 x ^ {2} z \mathrm {d} y + x y z \mathrm {d} z = \iint_ {\Sigma} \left| \begin{array}{c c c} \mathrm {d} y \mathrm {d} z & \mathrm {d} z \mathrm {d} x & \mathrm {d} x \mathrm {d} y \\ \frac {\partial}{\partial x} & \frac {\partial}{\partial y} & \frac {\partial}{\partial z} \\ 6 x y z - y z ^ {2} & 2 x ^ {2} z & x y z  \right| \\ &= \iint_ {\Sigma} \left(x z - 2 x ^ {2}\right) \mathrm {d} y \mathrm {d} z + \left(6 x y - 3 y z\right) \mathrm {d} z \mathrm {d} x + \left(z ^ {2} - 2 x z\right) \mathrm {d} x \mathrm {d} y \\ &= \iint_ {\Sigma} (2 x - z) \cdot (- x) \mathrm {d} y \mathrm {d} z + (2 x - z) \cdot 3 y \mathrm {d} z \mathrm {d} x + (2 x - z) \cdot (- z) \mathrm {d} x \mathrm {d} y \\ \frac {2 x - z = 1}{\sim} \iint_ {\Sigma} (- x) \mathrm {d} y \mathrm {d} z + 3 y \mathrm {d} z \mathrm {d} x + (- z) \mathrm {d} x \mathrm {d} y. \end{aligned}</equation>利用两类曲面积分之间的联系将<equation>\iint_{\Sigma} (-x)\mathrm{d}y\mathrm{d}z + 3y\mathrm{d}z\mathrm{d}x + (-z)\mathrm{d}x\mathrm{d}y</equation>转化为关于坐标<equation>x,y</equation>的积分再计算

令<equation>F ( x,y,z) = z - 2 x + 1</equation>，则曲面<equation>\varSigma</equation>的方程为<equation>F ( x,y,z) = 0</equation>，法向量 n可取为<equation>\left(F_{x}^{\prime},F_{y}^{\prime},F_{z}^{\prime}\right) =</equation>（-2,0,1).于是，<equation>\varSigma</equation>的法向量 n的方向余弦为<equation>\cos \alpha = \frac {- 2}{\sqrt {5}}, \quad \cos \beta = 0, \quad \cos \gamma = \frac {1}{\sqrt {5}}.</equation>由此可得<equation>\mathrm{d}y\mathrm{d}z = \frac{\cos \alpha}{\cos \gamma}\mathrm{d}x\mathrm{d}y = -2\mathrm{d}x\mathrm{d}y,\mathrm{d}z\mathrm{d}x = 0\mathrm{d}x\mathrm{d}y = 0.</equation>进一步可得<equation>I = \iint_{\Sigma} (-x)\mathrm{d}y\mathrm{d}z + 3y\mathrm{d}z\mathrm{d}x + (-z)\mathrm{d}x\mathrm{d}y = \iint_{\Sigma} [(-x)\cdot(-2) + (-z)\cdot 1]\mathrm{d}x\mathrm{d}y = \iint_{D}\mathrm{d}x\mathrm{d}y,</equation>其中<equation>D</equation>为<equation>\varSigma</equation>在<equation>xOy</equation>面上的投影区域.于是，<equation>I</equation>的值等于区域D的面积.

将<equation>z = 2x - 1</equation>代入<equation>x^{2} + y^{2} + z^{2} = 2x</equation>可得<equation>x^{2} + y^{2} + (2x - 1)^{2} - 2x = 0</equation>，整理可得<equation>5x^{2} - 6x + y^{2} + 1 = 0</equation>，即<equation>5\left(x - \frac{3}{5}\right)^{2} + y^{2} = \frac{4}{5}</equation>，也即<equation>\frac{\left(x - \frac{3}{5}\right)^{2}}{\frac{4}{25}} + \frac{y^{2}}{\frac{4}{5}} = 1.</equation>这是<equation>xOy</equation>面上以点<equation>\left(\frac{3}{5},0\right)</equation>为中心，长半轴长为<equation>\sqrt{\frac{4}{5}}</equation>，短半轴长为<equation>\sqrt{\frac{4}{25}}</equation>的椭圆，从而区域 D为由该椭圆所围成的椭圆盘，其面积为<equation>\pi \cdot \sqrt{\frac{4}{5}}\cdot \sqrt{\frac{4}{25}} = \frac{4\pi}{5\sqrt{5}} = \frac{4\sqrt{5}\pi}{25}.</equation>因此，<equation>I=\frac{4\sqrt{5}\pi}{25}.</equation>

---

**2022年第19题 | 解答题 | 12分**
19. (本题满分12分)

已知曲线 L是曲面<equation>\Sigma: 4 x^{2}+y^{2}+z^{2}=1, x\geqslant0, y\geqslant0, z\geqslant0</equation>的边界，曲面<equation>\Sigma</equation>方向朝上，曲线 L的方向和曲面<equation>\Sigma</equation>的方向符合右手法则，计算<equation>I=\oint_{L}(y z^{2}-\cos z) \mathrm{d} x+2 x z^{2} \mathrm{d} y+(2 x y z+x \sin z) \mathrm{d} z.</equation>
**解析: **（法一）根据右手法则，曲线<equation>L</equation>应取逆时针方向.

(a)

(b)

如图（a）所示，记<equation>L_{1}, L_{2}, L_{3}</equation>分别为 L在 xOy面，yOz面，zOx面的部分在<equation>L_{1}</equation>上，<equation>z=0,\int_{L_{1}}\mathrm{d}z=0.</equation>起点为<equation>\left(\frac{1}{2},0,0\right)</equation>终点为（0，1，0）.在<equation>L_{2}</equation>上，<equation>x=0,\int_{L_{2}}\mathrm{d}x=0.</equation>起点为（0，1，0），终点为（0，0，1）.在<equation>L_{3}</equation>上，<equation>y=0,\int_{L_{3}}\mathrm{d}y=0.</equation>起点为（0，0，1），终点为<equation>\left(\frac{1}{2},0,0\right).</equation>因此，<equation>\begin{aligned} I &= \oint_ {L} \left(y z ^ {2} - \cos z\right) \mathrm {d} x + 2 x z ^ {2} \mathrm {d} y + \left(2 x y z + x \sin z\right) \mathrm {d} z \\ &= \int_ {L _ {1}} (- \cos 0) \mathrm {d} x + 0 + \int_ {L _ {3}} (- \cos z) \mathrm {d} x + x \sin z \mathrm {d} z \\ &= (- 1) \times \left(0 - \frac {1}{2}\right) + \int_ {L _ {3}} \mathrm {d} (- x \cos z) = \frac {1}{2} + (- x \cos z) \Big | _ {(0, 0, 1)} ^ {\left(\frac {1}{2}, 0, 0\right)} \\ &= \frac {1}{2} - \frac {1}{2} = 0. \end{aligned}</equation>由于曲线<equation>L</equation>的方向和曲面<equation>\Sigma</equation>的方向符合右手法则，故根据斯托克斯公式，<equation>\begin{aligned} I &= \iint_ {\Sigma} \left| \begin{array}{c c c} \mathrm {d} y \mathrm {d} z & \mathrm {d} z \mathrm {d} x & \mathrm {d} x \mathrm {d} y \\ \frac {\partial}{\partial x} & \frac {\partial}{\partial y} & \frac {\partial}{\partial z} \\ y z ^ {2} - \cos z & 2 x z ^ {2} & 2 x y z + x \sin z  \right| \\ &= \iint_ {\Sigma} \left(2 x z - 4 x z\right) \mathrm {d} y \mathrm {d} z + (- 1) \left(2 y z + \sin z - 2 y z - \sin z\right) \mathrm {d} z \mathrm {d} x + \left(2 z ^ {2} - z ^ {2}\right) \mathrm {d} x \mathrm {d} y \\ &= \iint_ {\Sigma} (- 2 x z) \mathrm {d} y \mathrm {d} z + z ^ {2} \mathrm {d} x \mathrm {d} y. \end{aligned}</equation>如图（b）所示，添加平面<equation>\varSigma_{1}:z=0(4x^{2}+y^{2}\leqslant 1)</equation>，取下侧，<equation>\varSigma_{2}:x=0(y^{2}+z^{2}\leqslant 1)</equation>，取后侧，<equation>\varSigma_{3}:y=0(4x^{2}+z^{2}\leqslant 1)</equation>，取左侧，则<equation>\varSigma_{1},\varSigma_{2},\varSigma_{3}</equation>与<equation>\varSigma</equation>共同围成一个空间封闭区域<equation>\varOmega</equation>，且法向量指向外侧.<equation>\oiint_ {\Sigma + \Sigma_ {1} + \Sigma_ {2} + \Sigma_ {3}} (- 2 x z) \mathrm {d} y \mathrm {d} z + z ^ {2} \mathrm {d} x \mathrm {d} y = \iiint_ {\Omega} (- 2 z + 2 z) \mathrm {d} v = 0.</equation>另一方面，由于<equation>\varSigma_{1}</equation>和<equation>\varSigma_{3}</equation>均垂直于yOz面，故在这两个面上关于坐标y,z的积分为0.由于<equation>\varSigma_{2}</equation>和<equation>\varSigma_{3}</equation>均垂直于xOy面，故在这两个面上关于坐标x,y的积分为0.从而在<equation>\varSigma_{3}</equation>上，关于坐标y,z和关于坐标x,y的积分均为0.于是，<equation>\iint_ {\Sigma_ {3}} (- 2 x z) \mathrm {d} y \mathrm {d} z + z ^ {2} \mathrm {d} x \mathrm {d} y = 0.</equation>再分别代入<equation>\varSigma_{1}</equation>和<equation>\varSigma_{2}</equation>的方程可得<equation>\begin{aligned} \iint_ {\Sigma_ {1}} (- 2 x z) \mathrm {d} y \mathrm {d} z + z ^ {2} \mathrm {d} x \mathrm {d} y \stackrel {z = 0} {=} 0. \\ \iint_ {\Sigma_ {2}} (- 2 x z) \mathrm {d} y \mathrm {d} z + z ^ {2} \mathrm {d} x \mathrm {d} y \stackrel {x = 0} {=} 0. \end{aligned}</equation>因此，<equation>I = \oiint_ {\Sigma + \Sigma_ {1} + \Sigma_ {2} + \Sigma_ {3}} (- 2 x z) \mathrm {d} y \mathrm {d} z + z ^ {2} \mathrm {d} x \mathrm {d} y - \oiint_ {\Sigma_ {1} + \Sigma_ {2} + \Sigma_ {3}} (- 2 x z) \mathrm {d} y \mathrm {d} z + z ^ {2} \mathrm {d} x \mathrm {d} y = 0 - 0 = 0.</equation>

---

**2021年第20题 | 解答题 | 12分**
20. （本题满分12分）

设<equation>D\subset \mathbf{R}^{2}</equation>是有界单连通闭区域，<equation>I(D)=\iint_{D}(4-x^{2}-y^{2})\mathrm{d}x\mathrm{d}y</equation>取得最大值的积分区域为<equation>D_{1}.</equation>I. 求<equation>I ( D_{1} )</equation>的值；

II. 计算<equation>\int_{\partial D_1}\frac{(x\mathrm{e}^{x^2 + 4y^2} + y)\mathrm{d}x + (4y\mathrm{e}^{x^2 + 4y^2} - x)\mathrm{d}y}{x^2 + 4y^2}</equation>，其中<equation>\partial D_{1}</equation>是<equation>D_{1}</equation>的正向边界.
**答案: **( I )<equation>I ( D_{1} )=8 \pi;</equation>( II )<equation>-\pi.</equation>
**解析: **解（I）取区域<equation>D_{1}</equation>，使其包含所有使得被积函数非负的点，且不包含使得被积函数小于零的点，则在<equation>D_{1}</equation>上<equation>I(D)</equation>取得最大值. 可取<equation>D_{1}</equation>为<equation>4 - x^{2} - y^{2}\geqslant 0</equation>的区域，即圆盘域<equation>D_{1} = \{(x,y)|x^{2} + y^{2}\leqslant 4\}</equation>.<equation>\begin{aligned} I \left(D _ {1}\right) &= \iint_ {D _ {1}} \left(4 - x ^ {2} - y ^ {2}\right) \mathrm {d} x \mathrm {d} y \xlongequal {\text {极 坐 标}} \iint_ {D _ {1}} \left(4 - r ^ {2}\right) r \mathrm {d} r \mathrm {d} \theta = \int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {0} ^ {2} \left(4 r - r ^ {3}\right) \mathrm {d} r \\ &= 2 \pi \left(2 r ^ {2} - \frac {r ^ {4}}{4}\right) \Bigg | _ {0} ^ {2} = 2 \pi \times (8 - 4) = 8 \pi . \end{aligned}</equation>（Ⅱ）记所求积分为<equation>I, P(x,y) = \frac{x\mathrm{e}^{x^2 + 4y^2} + y}{x^2 + 4y^2}, Q(x,y) = \frac{4y\mathrm{e}^{x^2 + 4y^2} - x}{x^2 + 4y^2}</equation>，则当<equation>(x,y)\neq (0,0)</equation>时，<equation>\begin{aligned} \frac {\partial Q}{\partial x} &= \frac {\left(8 x y \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} - 1\right) \left(x ^ {2} + 4 y ^ {2}\right) - \left(4 y \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} - x\right) \cdot 2 x}{\left(x ^ {2} + 4 y ^ {2}\right) ^ {2}} \\ &= \frac {8 x y \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} \left(x ^ {2} + 4 y ^ {2} - 1\right) + x ^ {2} - 4 y ^ {2}}{\left(x ^ {2} + 4 y ^ {2}\right) ^ {2}}, \end{aligned}</equation><equation>\begin{aligned} \frac {\partial P}{\partial y} &= \frac {\left(8 x y \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} + 1\right) \left(x ^ {2} + 4 y ^ {2}\right) - \left(x \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} + y\right) \cdot 8 y}{\left(x ^ {2} + 4 y ^ {2}\right) ^ {2}} \\ &= \frac {8 x y \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} \left(x ^ {2} + 4 y ^ {2} - 1\right) + x ^ {2} - 4 y ^ {2}}{\left(x ^ {2} + 4 y ^ {2}\right) ^ {2}}. \end{aligned}</equation>于是，<equation>\frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y}</equation>原点为被积函数的奇点，且包含在<equation>D_{1}</equation>内.

记<equation>\partial D_{1}=L</equation>作辅助曲线<equation>L^{\prime}:x^{2}+4y^{2}=\varepsilon^{2}</equation>并使<equation>\varepsilon</equation>足够小，使<equation>L^{\prime}</equation>围成的椭圆包含在 L围成的圆中，其参数方程为<equation>\left\{ \begin{array}{l l} x=\varepsilon\cos t, \\ y=\frac{\varepsilon}{2}\sin t, \end{array} \right.</equation>t从0变到<equation>2\pi</equation>如图所示，<equation>L^{\prime}</equation>的正向为逆时针方向，<equation>L^{\prime}</equation>所围成的区域记为<equation>D_{0}, L+L^{\prime}-</equation>围成区域<equation>D_{1}\backslash D_{0}</equation>被积函数在<equation>D_{1}\backslash D_{0}</equation>上没有奇点.

由格林公式，<equation>\oint_ {L + L ^ {\prime} -} \frac {\left(x \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} + y\right) \mathrm {d} x + \left(4 y \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} - x\right) \mathrm {d} y}{x ^ {2} + 4 y ^ {2}} \xlongequal {\text {格 林 公 式}} \iint_ {D _ {1} \backslash D _ {0}} 0 \mathrm {d} x \mathrm {d} y = 0,</equation>因此，<equation>\begin{aligned} I &= \oint_ {L} \frac {\left(x \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} + y\right) \mathrm {d} x + \left(4 y \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} - x\right) \mathrm {d} y}{x ^ {2} + 4 y ^ {2}} = \oint_ {L ^ {\prime}} \frac {\left(x \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} + y\right) \mathrm {d} x + \left(4 y \mathrm {e} ^ {x ^ {2} + 4 y ^ {2}} - x\right) \mathrm {d} y}{x ^ {2} + 4 y ^ {2}} \\ \xlongequal {x ^ {2} + 4 y ^ {2} = \varepsilon^ {2}} \frac {1}{\varepsilon^ {2}} \oint_ {L ^ {\prime}} \left(x \mathrm {e} ^ {\varepsilon^ {2}} + y\right) \mathrm {d} x + \left(4 y \mathrm {e} ^ {\varepsilon^ {2}} - x\right) \mathrm {d} y \\ \xlongequal {\text {格 林 公 式}} \frac {1}{\varepsilon^ {2}} \iint_ {D _ {0}} \left[ \frac {\partial \left(4 y \mathrm {e} ^ {\varepsilon^ {2}} - x\right)}{\partial x} - \frac {\partial \left(x \mathrm {e} ^ {\varepsilon^ {2}} + y\right)}{\partial y} \right] \mathrm {d} x \mathrm {d} y &= \frac {1}{\varepsilon^ {2}} \iint_ {D _ {0}} (- 1 - 1) \mathrm {d} x \mathrm {d} y \\ &= - \frac {2}{\varepsilon^ {2}} \cdot D _ {0} \text {的 面 积} = - \frac {2}{\varepsilon^ {2}} \times \pi \times \varepsilon \times \frac {\varepsilon}{2} = - \pi . \end{aligned}</equation>

---

**2020年第16题 | 解答题 | 10分**
16. (本题满分10分)

计算曲线积分<equation>I=\oint_{L}\frac{4x-y}{4x^{2}+y^{2}}\mathrm{d}x+\frac{x+y}{4x^{2}+y^{2}}\mathrm{d}y</equation>，其中 L为<equation>x^{2}+y^{2}=2</equation>，方向为逆时针方向.
**解析: **解记 L围成的封闭区域为 D.记<equation>P ( x,y)=\frac{4 x-y}{4 x^{2}+y^{2}}, Q ( x,y)=\frac{x+y}{4 x^{2}+y^{2}}</equation>，则当（x,y）<equation>\neq</equation>（0,0）时，<equation>\frac {\partial Q}{\partial x} = \frac {4 x ^ {2} + y ^ {2} - (x + y) 8 x}{\left(4 x ^ {2} + y ^ {2}\right) ^ {2}} = \frac {y ^ {2} - 4 x ^ {2} - 8 x y}{\left(4 x ^ {2} + y ^ {2}\right) ^ {2}},</equation><equation>\frac {\partial P}{\partial y} = \frac {- \left(4 x ^ {2} + y ^ {2}\right) - (4 x - y) 2 y}{\left(4 x ^ {2} + y ^ {2}\right) ^ {2}} = \frac {y ^ {2} - 4 x ^ {2} - 8 x y}{\left(4 x ^ {2} + y ^ {2}\right) ^ {2}}.</equation>于是，<equation>\frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y}</equation>原点为被积函数的奇点，且包含在由 L围成的封闭区域 D内.

作辅助曲线<equation>L^{\prime}:4x^{2} + y^{2} = \varepsilon^{2}</equation>，并使<equation>\varepsilon</equation>足够小，使<equation>L^{\prime}</equation>围成的椭圆包含在<equation>L</equation>围成的圆中，其参数方程为<equation>\left\{ \begin{array}{l l} x = \frac{\varepsilon}{2}\cos t, t \text{ 从} 0 \\ y = \varepsilon \sin t, \end{array} \right.</equation>变到<equation>2\pi</equation>.如图所示，<equation>L^{\prime}</equation>的正向为逆时针方向，<equation>L^{\prime}</equation>所围成的区域记为<equation>D^{\prime}, L + L^{\prime}^{-}</equation>围成区域<equation>D\backslash D^{\prime}</equation>.被积函数在<equation>D\backslash D^{\prime}</equation>上没有奇点.

由格林公式，<equation>\oint_ {L + L ^ {\prime} -} \frac {4 x - y}{4 x ^ {2} + y ^ {2}} \mathrm {d} x + \frac {x + y}{4 x ^ {2} + y ^ {2}} \mathrm {d} y \xlongequal {\text {格 林 公 式}} \iint_ {D \backslash D ^ {\prime}} 0 \mathrm {d} x \mathrm {d} y = 0,</equation>因此，<equation>\begin{aligned} I &= \oint_ {L} \frac {4 x - y}{4 x ^ {2} + y ^ {2}} \mathrm {d} x + \frac {x + y}{4 x ^ {2} + y ^ {2}} \mathrm {d} y = \oint_ {L ^ {\prime}} \frac {4 x - y}{4 x ^ {2} + y ^ {2}} \mathrm {d} x + \frac {x + y}{4 x ^ {2} + y ^ {2}} \mathrm {d} y \\ \frac {4 x ^ {2} + y ^ {2} = \varepsilon^ {2}}{\varepsilon^ {2}} \frac {1}{\varepsilon^ {2}} \oint_ {L ^ {\prime}} (4 x - y) \mathrm {d} x + (x + y) \mathrm {d} y \xlongequal {\text {格 林 公 式}} \frac {1}{\varepsilon^ {2}} \iint_ {D ^ {\prime}} 2 \mathrm {d} x \mathrm {d} y \\ &= \frac {2}{\varepsilon^ {2}} \cdot D ^ {\prime} \text {的 面 积} = \frac {2}{\varepsilon^ {2}} \times \pi \times \frac {\varepsilon}{2} \times \varepsilon = \pi . \end{aligned}</equation>

---

**2019年第4题 | 选择题 | 4分 | 答案: D**
4. 设函数<equation>Q ( x,y )=\frac{x}{y^{2}}</equation>. 如果对上半平面（<equation>y>0</equation>）内的任意有向光滑封闭曲线 C都有<equation>\oint_{C}P(x,y)\mathrm{d}x+Q(x,y)\mathrm{d}y=0</equation>，那么函数 P(x,y)可取为（    ）

A.<equation>y-\frac{x^{2}}{y^{3}}</equation>B.<equation>\frac{1}{y}-\frac{x^{2}}{y^{3}}</equation>C.<equation>\frac{1}{x}-\frac{1}{y}</equation>D.<equation>x-\frac{1}{y}</equation>
答案: D
**解析: **解 由 Q(x,y)的表达式可知该函数在上半平面 y > 0内具有一阶连续偏导数，故若 P(x,y)满足在上半平面内具有一阶连续偏导数且<equation>\frac{\partial Q}{\partial x}\equiv \frac{\partial P}{\partial y}</equation>，则曲线积分<equation>\oint_{C}P(x,y)\mathrm{d}x+Q(x,y)\mathrm{d}y</equation>在单连通区域 y > 0内与路径无关，即对上半平面 y > 0内的任意分段光滑闭曲线 C都有<equation>\oint_{C}P(x,y)\mathrm{d}x+</equation><equation>Q(x,y)\mathrm{d}y=0.</equation>由于<equation>\frac{\partial Q}{\partial x}=\frac{1}{y^{2}}</equation>，故<equation>\frac{\partial P}{\partial y}</equation>应等于<equation>\frac{1}{y^{2}}</equation>. 选项C与选项D的函数均满足该要求. 但是选项C的函数<equation>\frac{1}{x}-\frac{1}{y}</equation>在 x = 0处无定义，从而也就不满足曲线积分与路径无关的条件.

因此，应选D.

---

**2017年第11题 | 填空题 | 4分**
11. 若曲线积分<equation>\int_ {L} \frac {x \mathrm {d} x - a y \mathrm {d} y}{x ^ {2} + y ^ {2} - 1}</equation>在区域<equation>D=\{(x,y)\mid x^{2}+y^{2}<1\}</equation>内与路径无关，则 a=___
**答案: **<equation>- 1.</equation>
**解析: **解 令<equation>P=\frac{x}{x^{2}+y^{2}-1}, Q=\frac{-ay}{x^{2}+y^{2}-1}</equation>，则<equation>\frac{\partial P}{\partial y}=\frac{-2xy}{\left(x^{2}+y^{2}-1\right)^{2}},</equation><equation>\frac{\partial Q}{\partial x}=\frac{2axy}{\left(x^{2}+y^{2}-1\right)^{2}}.</equation>又 D为单连通区域，且曲线积分与路径无关，故<equation>\frac{\partial P}{\partial y}=\frac{\partial Q}{\partial x}</equation>即<equation>\frac{-2xy}{\left(x^{2}+y^{2}-1\right)^{2}}=\frac{2axy}{\left(x^{2}+y^{2}-1\right)^{2}}</equation>从而 a=-1.

---

**2016年第17题 | 解答题 | 10分**
17. (本题满分10分）

设函数 f(x,y)满足<equation>\frac{\partial f(x,y)}{\partial x}=(2 x+1) \mathrm{e}^{2 x-y}</equation>，且 f(0,y)=y+1，<equation>L_{t}</equation>是从点（0，0）到点（1,t）的光滑曲线.计算曲线积分<equation>I(t)=\int_{L_{t}} \frac{\partial f(x,y)}{\partial x} \mathrm{d} x+\frac{\partial f(x,y)}{\partial y} \mathrm{d} y</equation>，并求 I(t)的最小值.
**答案: **##<equation>I ( t ) = \mathrm {e} ^ {2 - t} + t, I ( t )</equation>的最小值为3.
**解析: **解由<equation>\frac{\partial f(x,y)}{\partial x} = (2x+1)\mathrm{e}^{2x-y}</equation>知，<equation>\begin{aligned} f (x, y) &= \int (2 x + 1) \mathrm {e} ^ {2 x - y} \mathrm {d} x = \mathrm {e} ^ {- y} \int (2 x + 1) \mathrm {e} ^ {2 x} \mathrm {d} x \\ &= \mathrm {e} ^ {- y} \left[ \frac {1}{2} \mathrm {e} ^ {2 x} (2 x + 1) - \int \mathrm {e} ^ {2 x} \mathrm {d} x \right] \\ &= \mathrm {e} ^ {- y} \left[ \frac {1}{2} \mathrm {e} ^ {2 x} (2 x + 1) - \frac {1}{2} \mathrm {e} ^ {2 x} + \varphi_ {1} (y) \right] \\ &= x \mathrm {e} ^ {2 x - y} + \varphi_ {2} (y), \end{aligned}</equation>这里<equation>\varphi_{1}(y),\varphi_{2}(y)</equation>都是以<equation>y</equation>为自变量的待定函数，且<equation>\varphi_{2}(y) = \mathrm{e}^{-y}\varphi_{1}(y)</equation>. 由<equation>f(0,y) = y + 1</equation>得到<equation>\varphi_{2}(y) = y + 1</equation>，从而<equation>f (x, y) = x \mathrm {e} ^ {2 x - y} + y + 1.</equation>下面用两种方法求<equation>I ( t )</equation>（法一）<equation>\frac{\partial f}{\partial x} = (2x + 1)\mathrm{e}^{2x - y},\frac{\partial f}{\partial y} = -x\mathrm{e}^{2x - y} + 1</equation>在整个平面上都连续，故由定理1知，<equation>I (t) = \int_ {L _ {t}} \frac {\partial f (x , y)}{\partial x} \mathrm {d} x + \frac {\partial f (x , y)}{\partial y} \mathrm {d} y = f (1, t) - f (0, 0) = \mathrm {e} ^ {2 - t} + t.</equation>（法二）<equation>\frac{\partial^2 f}{\partial x\partial y} = \frac{\partial^2 f}{\partial y\partial x} = -(2x + 1)\mathrm{e}^{2x - y}</equation>在整个平面上连续，故由定理2知，曲线积分<equation>I(t)</equation>与路径无关.下面我们选择两条不同的路径来计算<equation>I(t)</equation>.

（a）如图，令<equation>L_{1}</equation>是从点（0,0）到点（1,0），再到点（1,t）的折线段，于是<equation>\begin{aligned} I (t) &= \int_ {L _ {1}} \frac {\partial f (x , y)}{\partial x} \mathrm {d} x + \frac {\partial f (x , y)}{\partial y} \mathrm {d} y \\ &= \int_ {0} ^ {1} \frac {\partial f (x , 0)}{\partial x} \mathrm {d} x + \int_ {0} ^ {t} \frac {\partial f (1 , y)}{\partial y} \mathrm {d} y \\ &= f (x, 0) \left| _ {x = 0} ^ {x = 1} + f (1, y) \right| _ {y = 0} ^ {y = t} \\ &= f (1, 0) - f (0, 0) + f (1, t) - f (1, 0) \\ &= f (1, t) - f (0, 0) = \mathrm {e} ^ {2 - t} + t. \end{aligned}</equation>（b）如图，令<equation>L_{2}</equation>是从点<equation>(0,0)</equation>到点<equation>(0,t)</equation>，再到点<equation>(1,t)</equation>的折线段，于是<equation>\begin{aligned} I (t) &= \int_ {L _ {2}} \frac {\partial f (x , y)}{\partial x} \mathrm {d} x + \frac {\partial f (x , y)}{\partial y} \mathrm {d} y \\ &= \int_ {0} ^ {t} \frac {\partial f (0 , y)}{\partial y} \mathrm {d} y + \int_ {0} ^ {1} \frac {\partial f (x , t)}{\partial x} \mathrm {d} x \\ &= f (0, y) \left| _ {y = 0} ^ {y = t} + f (x, t) \right| _ {x = 0} ^ {x = 1} \\ &= f (0, t) - f (0, 0) + f (1, t) - f (0, t) \\ &= f (1, t) - f (0, 0) = \mathrm {e} ^ {2 - t} + t. \end{aligned}</equation>下面求 I（t）的最小值.<equation>I^{\prime}(t) = 1 - \mathrm{e}^{2 - t}.</equation>令<equation>I^{\prime}(t) = 0</equation>，解得<equation>t = 2</equation>当<equation>t > 2</equation>时，<equation>I^{\prime}(t) > 0</equation>，于是<equation>I(t)</equation>在<equation>[2, +\infty)</equation>上单调增加；当<equation>t < 2</equation>时，<equation>I^{\prime}(t) < 0</equation>，于是<equation>I(t)</equation>在<equation>(-\infty ,2]</equation>上单调减少，从而<equation>t = 2</equation>为<equation>I(t)</equation>的最小值点，最小值为<equation>I (2) = \mathrm {e} ^ {2 - 2} + 2 = 3.</equation>

---

**2015年第19题 | 解答题 | 10分**
19. (本题满分10分)

已知曲线 L的方程为<equation>\left\{\begin{array}{l l}z=\sqrt{2-x^{2}-y^{2}},\\ z=x, \end{array} \right.</equation>起点为 A(0,<equation>\sqrt{2},0)</equation>，终点为 B(0，<equation>-\sqrt{2},0)</equation>，请计算曲线积分 I=<equation>\int_{L}(y+z)\mathrm{d}x+(z^{2}-x^{2}+y)\mathrm{d}y+x^{2}y^{2}\mathrm{d}z.</equation>
**答案: **<equation>(1 9) I = \frac {\sqrt {2}}{2} \pi .</equation>