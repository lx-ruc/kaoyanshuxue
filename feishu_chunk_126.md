#### 数项级数

**2025年第3题 | 选择题 | 5分 | 答案: B**

3. 已知 k为常数，则级数<equation>\sum_{n=1}^{\infty}(-1)^{n}\left[\frac{1}{n}-\ln \left(1+\frac{k}{n^{2}}\right)\right]</equation>(    )

A. 绝对收敛 B. 条件收敛

C. 发散 D. 敛散性与 k的取

答案: B

**解析:**解 由于数列<equation>\left\{\frac{1}{n}\right\}</equation>单调减少趋于0，故由交错级数的莱布尼茨定理可知<equation>\sum_{n=1}^{\infty}(-1)^{n}\frac{1}{n}</equation>收敛.但<equation>\sum_{n=1}^{\infty}\frac{1}{n}</equation>发散，于是级数<equation>\sum_{n=1}^{\infty}(-1)^{n}\frac{1}{n}</equation>条件收敛.

由于<equation>\left|\ln \left(1+\frac{k}{n^{2}}\right)\right|= \left|\frac{k}{n^{2}}+o\left(\frac{k}{n^{2}}\right)\right|</equation>，故当 n→<equation>\infty</equation>时，<equation>\left|\ln \left(1+\frac{k}{n^{2}}\right)\right| \sim \left|\frac{k}{n^{2}}\right|</equation>，而<equation>\lim_{n\to \infty}n^{2}\left|\frac{k}{n^{2}}\right|=|k|</equation>，从而由正项级数的极限审敛法可知<equation>\sum_{n=1}^{\infty}\left|\frac{k}{n^{2}}\right|</equation>收敛，进一步可得<equation>\sum_{n=1}^{\infty}\left|\ln \left(1+\frac{k}{n^{2}}\right)\right|</equation>收敛.于是级数<equation>\sum_{n=1}^{\infty}(-1)^{n}\ln \left(1+\frac{k}{n^{2}}\right)</equation>绝对收敛.

由级数<equation>\sum_{n=1}^{\infty}(-1)^{n}\frac{1}{n}</equation>条件收敛，级数<equation>\sum_{n=1}^{\infty}(-1)^{n}\ln \left(1+\frac{k}{n^{2}}\right)</equation>绝对收敛以及分析中的结论可得级数<equation>\sum_{n=1}^{\infty}(-1)^{n}\left[\frac{1}{n}-\ln \left(1+\frac{k}{n^{2}}\right)\right]</equation>条件收敛.

因此，应选B.

---

**2023年第4题 | 选择题 | 5分 | 答案: A**

4. 已知<equation>a_{n} < b_{n} ( n=1,2,\cdots)</equation>，若级数<equation>\sum_{n=1}^{\infty} a_{n}</equation>与<equation>\sum_{n=1}^{\infty} b_{n}</equation>均收敛，则“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的（    ）

A. 充分必要条件 B. 充分不必要条件

C. 必要不充分条件 D. 既不充分也不必要条件

答案: A

**解析:**解（法一）由<equation>a_{n} < b_{n}</equation>可知，<equation>\sum_{n=1}^{\infty} \left(b_{n}-a_{n}\right)</equation>为正项级数. 进一步，由<equation>\sum_{n=1}^{\infty} a_{n}</equation>与<equation>\sum_{n=1}^{\infty} b_{n}</equation>均收敛以及收敛级数的性质可知，<equation>\sum_ {n = 1} ^ {\infty} \left(b _ {n} - a _ {n}\right) = \sum_ {n = 1} ^ {\infty} b _ {n} - \sum_ {n = 1} ^ {\infty} a _ {n}.</equation>于是，<equation>\sum_{n=1}^{\infty} \left(b_{n}-a_{n}\right)</equation>为收敛的正项级数，从而<equation>\sum_{n=1}^{\infty} \left(b_{n}-a_{n}\right)</equation>绝对收敛.

由三角不等式可得<equation>\left| b _ {n} \right| = \left| b _ {n} - a _ {n} + a _ {n} \right| \leqslant \left| b _ {n} - a _ {n} \right| + \left| a _ {n} \right|,</equation><equation>\left| a _ {n} \right| = \left| a _ {n} - b _ {n} + b _ {n} \right| \leqslant \left| b _ {n} - a _ {n} \right| + \left| b _ {n} \right|.</equation>若<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛，即<equation>\sum_{n=1}^{\infty} \mid a_{n} \mid</equation>收敛，则由（1）式以及正项级数的比较审敛法可知<equation>\sum_{n=1}^{\infty} \mid b_{n} \mid</equation>收敛，从而<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛.“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的充分条件.

若<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛，即<equation>\sum_{n=1}^{\infty} \mid b_{n} \mid</equation>收敛，则由（2）式以及正项级数的比较审敛法可知<equation>\sum_{n=1}^{\infty} \mid a_{n} \mid</equation>收敛，从而<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛.“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的必要条件.

综上所述，“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的充分必要条件，应选A.

（法二）先考虑充分性.

设<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛，即<equation>\sum_{n=1}^{\infty} \mid a_{n}\mid</equation>收敛.

考虑正项级数<equation>\sum_{n=1}^{\infty} \frac{\mid b_{n}\mid -b_{n}}{2}.</equation>对<equation>\left\{b_{n}\right\}</equation>中小于0的项，<equation>a_{n} < b_{n} < 0</equation>，于是<equation>\left| a _ {n} \right| = - a _ {n} > - b _ {n} = \frac {\left| b _ {n} \right| - b _ {n}}{2} > 0.</equation>对<equation>\left\{b_{n}\right\}</equation>中大于等于0的项，<equation>\left| a _ {n} \right| \geqslant 0 = \frac {\left| b _ {n} \right| - b _ {n}}{2}.</equation>从而，对所有正整数 n，都有<equation>|a_{n}| \geqslant \frac{|b_{n}| - b_{n}}{2} \geqslant 0.</equation>由正项级数的比较审敛法可知，级数<equation>\sum_{n=1}^{\infty} \frac{\mid b_{n}\mid -b_{n}}{2}</equation>收敛. 进一步，<equation>\sum_ {n = 1} ^ {\infty} \left| b _ {n} \right| = \sum_ {n = 1} ^ {\infty} \left[ 2 \left(\frac {\left| b _ {n} \right| - b _ {n}}{2}\right) + b _ {n} \right] = 2 \sum_ {n = 1} ^ {\infty} \frac {\left| b _ {n} \right| - b _ {n}}{2} + \sum_ {n = 1} ^ {\infty} b _ {n}.</equation>由<equation>\sum_{n=1}^{\infty}b_{n}</equation>收敛以及收敛级数的性质可知，<equation>\sum_{n=1}^{\infty}|\boldsymbol{b}_{n}|</equation>收敛，从而<equation>\sum_{n=1}^{\infty}b_{n}</equation>绝对收敛.

因此，“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的充分条件.

再考虑必要性.

由<equation>a_{n} < b_{n}</equation>可得<equation>- b_{n} < - a_{n}.</equation>由<equation>\sum_{n=1}^{\infty} a_{n}</equation>与<equation>\sum_{n=1}^{\infty} b_{n}</equation>均收敛可知<equation>\sum_{n=1}^{\infty}(-a_{n})</equation>与<equation>\sum_{n=1}^{\infty}(-b_{n})</equation>均收敛.于是，同充分性的证明可知<equation>\sum_{n=1}^{\infty}(-b_{n})</equation>绝对收敛蕴含<equation>\sum_{n=1}^{\infty}(-a_{n})</equation>绝对收敛，即<equation>\sum_{n=1}^{\infty}b_{n}</equation>绝对收敛蕴含<equation>\sum_{n=1}^{\infty}a_{n}</equation>绝对收敛.

因此，“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的必要条件.

综上所述，“<equation>\sum_{n=1}^{\infty} a_{n}</equation>绝对收敛”是“<equation>\sum_{n=1}^{\infty} b_{n}</equation>绝对收敛”的充分必要条件，应选A.

---

**2019年第4题 | 选择题 | 4分 | 答案: B**

4. 若<equation>\sum_{n=1}^{\infty} n u_{n}</equation>绝对收敛，<equation>\sum_{n=1}^{\infty} \frac{v_{n}}{n}</equation>条件收敛，则（    ）

A.<equation>\sum_{n=1}^{\infty} u_{n} v_{n}</equation>条件收敛 B.<equation>\sum_{n=1}^{\infty} u_{n} v_{n}</equation>绝对收敛 C.<equation>\sum_{n=1}^{\infty} \left(u_{n}+v_{n}\right)</equation>收敛 D.<equation>\sum_{n=1}^{\infty} \left(u_{n}+v_{n}\right)</equation>发散

答案: B

**解析:**解（法一）由<equation>\sum_{n=1}^{\infty}\frac{v_{n}}{n}</equation>条件收敛以及级数收敛的必要条件可得，<equation>\lim_{n\to \infty}\frac{v_{n}}{n}=0.</equation>由极限的有界性可知，存在 M > 0和正整数N，使得当 n > N时，<equation>\left|\frac{v_{n}}{n}\right|\leqslant M.</equation>于是，<equation>\left| u _ {n} v _ {n} \right| = \left| n u _ {n} \cdot \frac {v _ {n}}{n} \right| \leqslant M \left| n u _ {n} \right|.</equation>由于<equation>\sum_{n=1}^{\infty} n u_{n}</equation>绝对收敛，故其收敛，从而由比较审敛法可知，<equation>\sum_{n=1}^{\infty} \mid u_{n} v_{n} \mid</equation>收敛因此，<equation>\sum_{n=1}^{\infty} u_{n} v_{n}</equation>绝对收敛.应选B.

（法二）排除法.

选项A、C：取<equation>u_{n}=\frac{1}{n^{3}}, v_{n}=(-1)^{n}</equation>，则<equation>\sum_{n=1}^{\infty}u_{n}v_{n}=\sum_{n=1}^{\infty}\frac{(-1)^{n}}{n^{3}},\sum_{n=1}^{\infty}\left(u_{n}+v_{n}\right)=\sum_{n=1}^{\infty}\left[\frac{1}{n^{3}}+(-1)^{n}\right]</equation><equation>\sum_{n=1}^{\infty}\frac{(-1)^{n}}{n^{3}}</equation>绝对收敛，<equation>\sum_{n=1}^{\infty}\left[\frac{1}{n^{3}}+(-1)^{n}\right]</equation>发散. 选项A、C不正确.

选项D：取<equation>u_{n}=\frac{1}{n^{3}},</equation><equation>v_{n}=\frac{(-1)^{n+1}}{\ln(n+1)},</equation>则<equation>\sum_{n=1}^{\infty}\frac{1}{n^{3}}</equation>收敛，且由莱布尼茨定理可知<equation>\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{\ln(n+1)}</equation>收敛.由收敛级数的性质可知<equation>\sum_{n=1}^{\infty}\left[\frac{1}{n^{3}}+\frac{(-1)^{n+1}}{\ln(n+1)}\right]</equation>收敛.选项D不正确由排除法可知，应选B.

---

**2017年第4题 | 选择题 | 4分 | 答案: C**

4. 若级数<equation>\sum_{n=2}^{\infty}\left[\sin \frac{1}{n}-k\ln \left(1-\frac{1}{n}\right)\right]</equation>收敛，则 k=（    ）

A.1 B.2 C.-1 D.-2

答案: C

**解析:**解 考虑<equation>\sin \frac{1}{n}</equation>和<equation>\ln \left( 1-\frac{1}{n} \right)</equation>的泰勒公式.<equation>\sin \frac {1}{n} = \frac {1}{n} - \frac {1}{6 n ^ {3}} + o \left(\frac {1}{n ^ {3}}\right), \quad \ln \left(1 - \frac {1}{n}\right) = - \frac {1}{n} - \frac {1}{2 n ^ {2}} + o \left(\frac {1}{n ^ {2}}\right).</equation>于是，<equation>\sin \frac {1}{n} - k \ln \left(1 - \frac {1}{n}\right) = \frac {1}{n} + \frac {k}{n} + \frac {k}{2 n ^ {2}} + o \left(\frac {1}{n ^ {2}}\right).</equation>当 n充分大时，<equation>\sin \frac{1}{n}-k\ln \left(1-\frac{1}{n}\right)=\frac{1}{n}+\frac{k}{n}+\frac{k}{2n^{2}}+o\left(\frac{1}{n^{2}}\right)</equation>不变号.又因为舍去级数的有限项不影响级数的敛散性，所以可以对级数<equation>\sum_{n=2}^{\infty}\left[\sin \frac{1}{n}-k\ln \left(1-\frac{1}{n}\right)\right]</equation>使用极限形式的比较审敛法.当 k≠-1时，<equation>\lim _ {n \rightarrow \infty} \frac {\sin \frac {1}{n} - k \ln \left(1 - \frac {1}{n}\right)}{\frac {1}{n}} = \lim _ {n \rightarrow \infty} \frac {\frac {1}{n} + \frac {k}{n} + \frac {k}{2 n ^ {2}} + o \left(\frac {1}{n ^ {2}}\right)}{\frac {1}{n}} = 1 + k,</equation>而<equation>\sum_{n=1}^{\infty}\frac{1}{n}</equation>发散，故由极限形式的比较审敛法知，原级数发散.

当 k=-1时，<equation>\sum_{n=2}^{\infty}-\left[\sin \frac{1}{n}-k\ln \left(1-\frac{1}{n}\right)\right]</equation>为正项级数，且<equation>\lim _ {n \rightarrow \infty} \frac {- \left[ \sin \frac {1}{n} + \ln \left(1 - \frac {1}{n}\right)\right]}{\frac {1}{n ^ {2}}} = \lim _ {n \rightarrow \infty} \frac {\frac {1}{2 n ^ {2}} + o \left(\frac {1}{n ^ {2}}\right)}{\frac {1}{n ^ {2}}} = \frac {1}{2},</equation>而<equation>\sum_{n=1}^{\infty}\frac{1}{n^{2}}</equation>收敛，故由极限形式的比较审敛法知，原级数收敛.

级数<equation>\sum_{n=2}^{\infty}\left[\sin \frac{1}{n}-k\ln \left(1-\frac{1}{n}\right)\right]</equation>收敛等价于 k=-1.

因此，应选C.

---

**2016年第4题 | 选择题 | 4分 | 答案: A**

4. 级数<equation>\sum_{n=1}^{\infty}\left(\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}}\right)\sin(n+k)(k</equation>为常数)（    ）

A. 绝对收敛 B. 条件收敛 C. 发散 D. 收敛性与 k有关

答案: A

**解析:**解 （法一）首先，这并不是一个正项级数，但当 n<equation>\to\infty</equation>时，它的一般项<equation>\begin{array}{l} \left(\frac {1}{\sqrt {n}} - \frac {1}{\sqrt {n + 1}}\right) \sin (n + k) = \frac {\sqrt {n + 1} - \sqrt {n}}{\sqrt {n} \sqrt {n + 1}} \sin (n + k) \\ \xlongequal {\text {分子 有 理 化}} \frac {\sin (n + k)}{\sqrt {n} \sqrt {n + 1} (\sqrt {n + 1} + \sqrt {n})} \rightarrow 0, \\ \end{array}</equation>并且<equation>\left| \left(\frac {1}{\sqrt {n}} - \frac {1}{\sqrt {n + 1}}\right) \sin (n + k) \right| \leqslant \frac {1}{\sqrt {n} \sqrt {n + 1} \left(\sqrt {n + 1} + \sqrt {n}\right)} \leqslant \frac {1}{n \cdot 2 \sqrt {n}} < \frac {1}{n ^ {\frac {3}{2}}},</equation>而<equation>\sum_{n=1}^{\infty}\frac{1}{n^{\frac{3}{2}}}</equation>收敛，故由比较审敛法可知，<equation>\sum_{n=1}^{\infty}\left| \left( \frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}} \right)\sin(n+k) \right|</equation>收敛，从而原级数绝对收敛应选A.

（法二）注意到<equation>\left| \left(\frac {1}{\sqrt {n}} - \frac {1}{\sqrt {n + 1}}\right) \sin (n + k) \right| \leqslant \frac {1}{\sqrt {n}} - \frac {1}{\sqrt {n + 1}}.</equation>由于<equation>\sum_ {n = 1} ^ {m} \left(\frac {1}{\sqrt {n}} - \frac {1}{\sqrt {n + 1}}\right) = \left(1 - \frac {1}{\sqrt {2}}\right) + \left(\frac {1}{\sqrt {2}} - \frac {1}{\sqrt {3}}\right) + \dots + \left(\frac {1}{\sqrt {m}} - \frac {1}{\sqrt {m + 1}}\right) = 1 - \frac {1}{\sqrt {m + 1}},</equation>故<equation>\sum_{n=1}^{\infty}\left(\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}}\right)=\lim_{m\to \infty}\left(1-\frac{1}{\sqrt{m+1}}\right)=1</equation>，即级数<equation>\sum_{n=1}^{\infty}\left(\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}}\right)</equation>收敛.

由比较审敛法知，级数<equation>\sum_{n=1}^{\infty}\left| \left(\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}}\right)\sin(n+k)\right|</equation>收敛，即级数<equation>\sum_{n=1}^{\infty}\left(\frac{1}{\sqrt{n}}-\frac{1}{\sqrt{n+1}}\right)\sin(n+k)</equation>绝对收敛.应选A.

---

**2015年第4题 | 选择题 | 4分 | 答案: C**

4. 下列级数中发散的是（    ）<equation>\sum_ {n = 1} ^ {\infty} \frac {n}{3 ^ {n}}</equation><equation>\sum_ {n = 1} ^ {\infty} \frac {1}{\sqrt {n}} \ln \left(1 + \frac {1}{n}\right)</equation>C.<equation>\sum_{n=2}^{\infty} \frac{(-1)^{n}+1}{\ln n}</equation>D.<equation>\sum_{n=1}^{\infty} \frac{n!}{n^{n}}</equation>

答案: C

**解析:**解 由于当 n为奇数时，<equation>(-1)^{n}+1=0;</equation>n为偶数时，<equation>(-1)^{n}+1=2</equation>，故<equation>\sum_ {n = 2} ^ {2 N} \frac {(- 1) ^ {n} + 1}{\ln n} = \sum_ {k = 1} ^ {N} \frac {2}{\ln 2 k} = \sum_ {k = 1} ^ {N} \frac {2}{\ln 2 + \ln k} \geqslant \frac {2}{\ln 2} + \sum_ {k = 2} ^ {N} \frac {2}{2 \ln k} > \sum_ {k = 2} ^ {N} \frac {1}{\ln k} > \sum_ {k = 2} ^ {N} \frac {1}{k}.</equation>而<equation>\sum_{k=2}^{\infty} \frac{1}{k}</equation>发散.由比较审敛法可知，<equation>\sum_{n=2}^{\infty} \frac{(-1)^{n}+1}{\ln n}</equation>发散.应选C.

也可以这样说明<equation>\sum_{n=2}^{\infty} \frac{(-1)^{n}+1}{\ln n}</equation>发散.

由莱布尼茨定理可知<equation>\sum_{n = 2}^{\infty}\frac{(-1)^n}{\ln n}</equation>收敛，由比较审敛法可知<equation>\sum_{n = 2}^{\infty}\frac{1}{\ln n}</equation>发散.因此，<equation>\sum_{n = 2}^{\infty}\frac{(-1)^n + 1}{\ln n}</equation>发散.

下面我们说明选项 A、B、D不正确.

由于<equation>\lim _ {n \rightarrow \infty} \frac {n + 1}{3 ^ {n + 1}} \cdot \frac {3 ^ {n}}{n} = \lim _ {n \rightarrow \infty} \frac {n + 1}{n} \cdot \frac {1}{3} = \frac {1}{3} < 1,</equation><equation>\lim _ {n \rightarrow \infty} \frac {(n + 1) !}{(n + 1) ^ {n + 1}} \cdot \frac {n ^ {n}}{n !} = \lim _ {n \rightarrow \infty} \left(\frac {n}{n + 1}\right) ^ {n} = \lim _ {n \rightarrow \infty} \frac {1}{\left(1 + \frac {1}{n}\right) ^ {n}} = \frac {1}{\mathrm {e}} < 1,</equation>故由比值审敛法可知，选项A与选项D中的级数均收敛.

由于<equation>\lim _ {n \rightarrow \infty} \frac {\frac {1}{\sqrt {n}} \ln \left(1 + \frac {1}{n}\right)}{n ^ {- \frac {3}{2}}} \xlongequal {\ln \left(1 + \frac {1}{n}\right) \sim \frac {1}{n}} \lim _ {n \rightarrow \infty} \frac {\frac {1}{\sqrt {n}} \cdot \frac {1}{n}}{n ^ {- \frac {3}{2}}} = 1,</equation>而<equation>\sum_{n=1}^{\infty}\frac{1}{n^{\frac{3}{2}}}</equation>收敛，故由比较审敛法的极限形式可知，选项B中的级数收敛.

---

**2013年第4题 | 选择题 | 4分 | 答案: D**

4. 设<equation>\{a_{n}\}</equation>为正项数列，下列选项正确的是（    )

A. 若<equation>a_{n}>a_{n+1}</equation>，则<equation>\sum_{n=1}^{\infty}(-1)^{n-1}a_{n}</equation>收敛

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


