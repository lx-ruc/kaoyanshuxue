#### 常数项级数敛散性的判定

**2025年第2题 | 选择题 | 5分 | 答案: B**

2. 已知级数：<equation>\textcircled{1} \sum_{n=1}^{\infty} \sin \frac{n^{3} \pi}{n^{2}+1}</equation><equation>\textcircled{2} \sum_{n=1}^{\infty}(-1)^{n}\left(\frac{1}{\sqrt[3]{n^{2}}}-\tan \frac{1}{\sqrt[3]{n^{2}}}\right)</equation>，则（    )

A.<equation>\textcircled{1}</equation>与<equation>\textcircled{2}</equation>均条件收敛 B.<equation>\textcircled{1}</equation>条件收敛，<equation>\textcircled{2}</equation>绝对收敛

C.<equation>\textcircled{1}</equation>绝对收敛，<equation>\textcircled{2}</equation>条件收敛 D.<equation>\textcircled{1}</equation>与<equation>\textcircled{2}</equation>均绝对收敛

答案: B

**解析:**解 对级数<equation>\textcircled{1}</equation>注意到<equation>\sin \frac{n^{3}\pi}{n^{2}+1}=\sin \frac{\left(n^{3}+n-n\right)\pi}{n^{2}+1}=\sin \left(n\pi-\frac{n\pi}{n^{2}+1}\right)=(-1)^{n-1}\sin \frac{n\pi}{n^{2}+1},</equation>故<equation>\left| \sin \frac{n^{3}\pi}{n^{2}+1}\right|=\sin \frac{n\pi}{n^{2}+1}.</equation>又因为<equation>\lim _ {n \rightarrow \infty} \frac {\sin \frac {n \pi}{n ^ {2} + 1}}{\frac {1}{n}} \xlongequal {\text {对 应}} \frac {\sin \frac {n \pi}{n ^ {2} + 1} - \frac {n \pi}{n ^ {2} + 1}}{\frac {1}{n}} \lim _ {n \rightarrow \infty} \frac {\frac {n \pi}{n ^ {2} + 1}}{\frac {1}{n}} = \lim _ {n \rightarrow \infty} \frac {n ^ {2} \pi}{n ^ {2} + 1} = \pi ,</equation>所以<equation>\sum_{n=1}^{\infty}\sin \frac{n\pi}{n^{2}+1}</equation>与<equation>\sum_{n=1}^{\infty}\frac{1}{n}</equation>同敛散，而<equation>\sum_{n=1}^{\infty}\frac{1}{n}</equation>发散，于是<equation>\sum_{n=1}^{\infty}\sin \frac{n\pi}{n^{2}+1}</equation>发散，即<equation>\sum_{n=1}^{\infty}\left|\sin \frac{n^{3}\pi}{n^{2}+1}\right|</equation>发散另一方面，对正整数<equation>n,\frac{n\pi}{n^{2}+1}\in\left(0,\frac{\pi}{2}\right]</equation>，而<equation>\frac{n\pi}{n^{2}+1}</equation>关于n单调减少趋于0，从而<equation>\sin \frac{n\pi}{n^{2}+1}</equation>关于n单调减少趋于0.由交错级数的莱布尼茨定理可知，<equation>\sum_{n=1}^{\infty}(-1)^{n-1}\sin \frac{n\pi}{n^{2}+1}</equation>收敛，即<equation>\sum_{n=1}^{\infty}\sin \frac{n^{3}\pi}{n^{2}+1}</equation>收敛因此，级数<equation>\textcircled{1}</equation>条件收敛.

对级数<equation>\textcircled{2}</equation>，考虑<equation>\tan x</equation>在<equation>x=0</equation>处带佩亚诺余项的三阶泰勒公式：<equation>\tan x=x+\frac{1}{3} x^{3}+o\left(x^{3}\right).</equation>由此可得<equation>\tan \frac{1}{\sqrt[3]{n^{2}}}=\frac{1}{\sqrt[3]{n^{2}}}+\frac{1}{3}\cdot \frac{1}{n^{2}}+o\left(\frac{1}{n^{2}}\right)</equation>，进一步可得当<equation>n\to\infty</equation>时，<equation>\tan \frac{1}{\sqrt[3]{n^{2}}}-\frac{1}{\sqrt[3]{n^{2}}}\sim \frac{1}{3n^{2}}.</equation>于是，<equation>\sum_{n=1}^{\infty}\left(\tan \frac{1}{\sqrt[3]{n^{2}}}-\frac{1}{\sqrt[3]{n^{2}}}\right)</equation>与<equation>\sum_{n=1}^{\infty}\frac{1}{n^{2}}</equation>同敛散，而<equation>\sum_{n=1}^{\infty}\frac{1}{n^{2}}</equation>收敛，从而<equation>\sum_{n=1}^{\infty}\left(\tan \frac{1}{\sqrt[3]{n^{2}}}-\frac{1}{\sqrt[3]{n^{2}}}\right)</equation>收敛. 又由于<equation>\left| (- 1) ^ {n} \left(\frac {1}{\sqrt [ 3 ]{n ^ {2}}} - \tan \frac {1}{\sqrt [ 3 ]{n ^ {2}}}\right) \right| = \tan \frac {1}{\sqrt [ 3 ]{n ^ {2}}} - \frac {1}{\sqrt [ 3 ]{n ^ {2}}},</equation>故<equation>\sum_{n=1}^{\infty}(-1)^{n}\left(\frac{1}{\sqrt[3]{n^{2}}}-\tan \frac{1}{\sqrt[3]{n^{2}}}\right)</equation>绝对收敛.

因此，级数<equation>\textcircled{2}</equation>绝对收敛综上所述，应选B.

---

**2023年第4题 | 选择题 | 5分 | 答案: A**

4. 已知<equation>a_{n} < b_{n} ( n=1,2,\cdots)</equation>，若级数<equation>\sum_{n=1}^{\infty} a_{n}</equation>与<equation>\sum_{n=1}^{\infty} b_{n}</equation>均收敛，则“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的（    ）

A. 充分必要条件 B. 充分不必要条件

C. 必要不充分条件 D. 既不充分也不必要条件

答案: A

**解析:**解（法一）由<equation>a_{n} < b_{n}</equation>可知，<equation>\sum_{n = 1}^{\infty}\left(b_{n} - a_{n}\right)</equation>为正项级数.进一步，由<equation>\sum_{n = 1}^{\infty}a_{n}</equation>与<equation>\sum_{n = 1}^{\infty}b_{n}</equation>均收敛以及收敛级数的性质可知，<equation>\sum_ {n = 1} ^ {\infty} \left(b _ {n} - a _ {n}\right) = \sum_ {n = 1} ^ {\infty} b _ {n} - \sum_ {n = 1} ^ {\infty} a _ {n}.</equation>于是，<equation>\sum_{n=1}^{\infty} \left(b_{n}-a_{n}\right)</equation>为收敛的正项级数，从而<equation>\sum_{n=1}^{\infty} \left(b_{n}-a_{n}\right)</equation>绝对收敛.

由三角不等式可得<equation>\left| b _ {n} \right| = \left| b _ {n} - a _ {n} + a _ {n} \right| \leqslant \left| b _ {n} - a _ {n} \right| + \left| a _ {n} \right|,</equation><equation>\left| a _ {n} \right| = \left| a _ {n} - b _ {n} + b _ {n} \right| \leqslant \left| b _ {n} - a _ {n} \right| + \left| b _ {n} \right|.</equation>若<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛，即<equation>\sum_{n=1}^{\infty} \mid a_{n} \mid</equation>收敛，则由（1）式以及正项级数的比较审敛法可知<equation>\sum_{n=1}^{\infty} \mid b_{n} \mid</equation>收敛，从而<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛.“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的充分条件.

若<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛，即<equation>\sum_{n=1}^{\infty} \mid b_{n} \mid</equation>收敛，则由（2）式以及正项级数的比较审敛法可知<equation>\sum_{n=1}^{\infty} \mid a_{n} \mid</equation>收敛，从而<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛.“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的必要条件.

综上所述，“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的充分必要条件，应选A.

（法二）先考虑充分性.

设<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛，即<equation>\sum_{n=1}^{\infty} \mid a_{n}\mid</equation>收敛.

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


