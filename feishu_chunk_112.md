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


