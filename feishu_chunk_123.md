#### 方程根的存在性与个数

**2021年第3题 | 选择题 | 5分 | 答案: A**

3. 设函数<equation>f(x)=a x-b \ln x(a>0)</equation>有两个零点，则<equation>\frac{b}{a}</equation>的取值范围是（    ）

A. (e,+<equation>\infty</equation>)

B. (0,e)

C.<equation>\left( 0,\frac{1} {\mathrm{e}} \right)</equation>D.<equation>\left( \frac{1}{\mathrm{e}},+\infty \right)</equation>

答案: A

**解析:**解（法一）<equation>f ( x )</equation>的定义域为（0，<equation>+ \infty</equation>）.计算<equation>f^{\prime}(x)</equation>得<equation>f^{\prime}(x)=a-\frac{b}{x}.</equation>由于 a > 0，故若 b≤0，则<equation>f^{\prime}(x)>0</equation>，f(x)单调增加.此时 f(x)不可能有2个零点.于是，b > 0.

下面分析 f（x）的单调性.

当<equation>x=\frac{b}{a}</equation>时，<equation>f^{\prime}(x)=0</equation>；当<equation>0 < x < \frac{b}{a}</equation>时，<equation>f^{\prime}(x) < 0,f(x)</equation>单调减少；当<equation>x > \frac{b}{a}</equation>时，<equation>f^{\prime}(x) > 0</equation><equation>f(x)</equation>单调增加.于是，<equation>f(x)</equation>在（0，<equation>+\infty</equation>）上先单调减少，再单调增加.<equation>f\left(\frac{b}{a}\right)</equation>为f(x)的最小值.

f(x)有2个零点等价于<equation>f\left(\frac{b}{a}\right)</equation>小于零.否则f(x）恒大于等于零，不可能存在2个零点.<equation>f \left(\frac {b}{a}\right) = a \cdot \frac {b}{a} - b \ln \frac {b}{a} = b - b \ln \frac {b}{a} = b \left(1 - \ln \frac {b}{a}\right) < 0.</equation>又因为<equation>b > 0</equation>，所以<equation>b\left(1-\ln \frac{b}{a}\right)<0</equation>等价于<equation>1-\ln \frac{b}{a}<0</equation>即<equation>\ln \frac{b}{a}>1,\frac{b}{a}>\mathrm{e}.</equation>因此，应选A.

（法二）同法一可知<equation>b > 0.</equation>ax-b<equation>\ln x=0</equation>等价于<equation>\frac{x}{\ln x}=\frac{b}{a}</equation>，故函数 f(x）=ax-b<equation>\ln x</equation>有2个零点等价于曲线 y<equation>=\frac{x}{\ln x}</equation>与直线 y<equation>=\frac{b}{a}</equation>有2个交点.

计算<equation>g ( x )=\frac{x}{\ln x}</equation>的导数<equation>g^{\prime}(x).</equation><equation>g ^ {\prime} (x) = \frac {\ln x - 1}{(\ln x) ^ {2}}.</equation>由于<equation>x=1</equation>是<equation>g(x)</equation>的无穷间断点，故<equation>x=1</equation>是<equation>y=g(x)</equation>的铅直渐近线.当<equation>0 < x < 1</equation>时，<equation>g^{\prime}(x)<0,g(x)</equation>单调减少；当<equation>1 < x < \mathrm{e}</equation>时，<equation>g^{\prime}(x)<0,g(x)</equation>单调减少；当<equation>x > \mathrm{e}</equation>时，<equation>g^{\prime}(x)>0,g(x)</equation>单调增加，且<equation>\lim _ {x \rightarrow + \infty} g (x) = \lim _ {x \rightarrow + \infty} \frac {x}{\ln x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow + \infty} \frac {1}{\frac {1}{x}} = + \infty .</equation><equation>x=\mathrm{e}</equation>是<equation>g(x)</equation>的极小值点，极小值为<equation>g(\mathrm{e})=\mathrm{e}.</equation>y = g(x）的图形如右图所示.

由图可知，曲线<equation>y=\frac{x}{\ln x}</equation>与直线<equation>y=\frac{b}{a}</equation>有2个交点当且仅当<equation>\frac{b}{a}>\mathrm{e}.</equation>因此，应选A.

---

**2019年第2题 | 选择题 | 4分 | 答案: D**

2. 已知方程<equation>x^{5}-5 x+k=0</equation>有3个不同的实根，则 k的取值范围是（    )

A.<equation>(-\infty,-4)</equation>B.<equation>(4,+\infty)</equation>C.<equation>\{-4,4\}</equation>D.<equation>(-4,4)</equation>

答案: D

**解析:**解构造辅助函数<equation>f ( x )=x^{5}-5 x+k</equation>，则<equation>f^{\prime}(x)=5 x^{4}-5=5 \left(x^{4}-1\right).</equation>当 x >1或 x<-1时，<equation>f^{\prime}(x)>0</equation>f(x)单调增加；当<equation>-1<x<1</equation>时，<equation>f^{\prime}(x)<0</equation>f(x)单调减少；当 x=<equation>\pm 1</equation>时，<equation>f^{\prime}(\pm1)=0.</equation>因此， x=-1是 f(x)的极大值点，极大值为 f(-1)， x=1是 f(x)的极小值点，极小值为 f(1).

(a)

(b)

如图（a）所示，要使得 f(x)有3个不同的零点，必须有<equation>f(1)=k-4<0, f(-1)=k+4>0.</equation>解得<equation>-4<k<4.</equation>因此，应选D.

---

**2017年第18题 | 解答题 | 10分**

18. (本题满分10分）已知方程<equation>\frac{1}{\ln(1+x)}-\frac{1}{x}=k</equation>在区间（0，1）内有实根，确定常数 k的取值范围.

**答案:**<equation>\left(\frac {1}{\ln 2} - 1, \frac {1}{2}\right).</equation>

**解析:**解设<equation>f ( x )=\frac{1}{\ln(1+x)}-\frac{1}{x}, x\in(0,1].</equation>考察 f(x)在（0，1]内的单调性.<equation>f ^ {\prime} (x) = \left[ \frac {1}{\ln (1 + x)} - \frac {1}{x} \right] ^ {\prime} = - \frac {1}{(1 + x) \ln^ {2} (1 + x)} + \frac {1}{x ^ {2}} = \frac {(1 + x) \ln^ {2} (1 + x) - x ^ {2}}{(1 + x) x ^ {2} \ln^ {2} (1 + x)}.</equation>由于当 x<equation>\in(0,1)</equation>时，<equation>(1+x)x^{2}\ln^{2}(1+x)>0</equation>，故我们考察 g(x）=（1+x）<equation>\ln^{2}(1+x)-x^{2},</equation><equation>x\in[0,1].</equation><equation>g ^ {\prime} (x) = \ln^ {2} (1 + x) + 2 \ln (1 + x) - 2 x,</equation><equation>g ^ {\prime \prime} (x) = \frac {2 \ln (1 + x)}{1 + x} + \frac {2}{1 + x} - 2 = \frac {2}{1 + x} [ \ln (1 + x) - x ].</equation>当 x<equation>\in(0,1)</equation>时，<equation>\ln(1+x)-x=-\frac{x^{2}}{2}+o(x^{2})<0</equation>.于是当 x<equation>\in(0,1)</equation>时，<equation>g^{\prime\prime}(x)<0</equation>.又因为<equation>g^{\prime}(0)=0</equation>，所以当 x<equation>\in(0,1)</equation>时，<equation>g^{\prime}(x)<0</equation>，g(x)在(0,1)内单调减少.由于<equation>g(0)=0</equation>，故<equation>g(x)<0</equation>，<equation>x\in(0,1)</equation>.因此，当 x<equation>\in(0,1)</equation>时，<equation>f^{\prime}(x)=\frac{g(x)}{(1+x)x^{2}\ln^{2}(1+x)}<0</equation>，f(x)在(0,1)内单调减少.<equation>f ( x )</equation>在（0,1）内的值域为（f（1），<equation>\lim_{x\to 0^{+}}f(x) ).</equation><equation>f (1) = \frac {1}{\ln 2} - 1.</equation>$<equation>\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} \left[\frac{1}{\ln(1+x)} - \frac{1}{x}\right] = \lim_{x \to 0^+} \frac{x - \ln(1+x)}{x\ln(1+x)} = \frac{1}{2}</equation>\left(\frac{1}{\ln2}-1,\frac{1}{2}\right). $

---

**2011年第18题 | 解答题 | 10分**

18. (本题满分10分）

证明方程<equation>4\arctan x-x+\frac{4\pi}{3}-\sqrt{3}=0</equation>恰有两个实根.

**答案:**## （18）证明略.

**解析:**证设 f(x）=4arctan x-x+<equation>\frac{4\pi}{3}-\sqrt{3}</equation>；则<equation>f ^ {\prime} (x) = \frac {4}{1 + x ^ {2}} - 1 = \frac {3 - x ^ {2}}{1 + x ^ {2}}.</equation>当<equation>x\in(-\sqrt{3},\sqrt{3})</equation>时，<equation>f^{\prime}(x) > 0</equation>；当<equation>x\in(-\infty , - \sqrt{3})</equation>或<equation>x\in(\sqrt{3}, + \infty)</equation>时，<equation>f^{\prime}(x) < 0</equation>；当<equation>x = \pm \sqrt{3}</equation>时，<equation>f^{\prime}(x) = 0.</equation>因此，<equation>f ( x )</equation>在<equation>(-\infty,-\sqrt{3})</equation>和<equation>(\sqrt{3},+\infty)</equation>上单调减少，在<equation>(-\sqrt{3},\sqrt{3})</equation>上单调增加，<equation>f(-\sqrt{3})</equation>为<equation>f ( x )</equation>的极小值，<equation>f(\sqrt{3})</equation>为<equation>f ( x )</equation>的极大值.

分别计算<equation>f(-\sqrt{3})</equation>和<equation>f(\sqrt{3})</equation>得，<equation>f (- \sqrt {3}) = 0, f (\sqrt {3}) = \frac {8}{3} \pi - 2 \sqrt {3} > 0.</equation>另一方面，当<equation>x\to+\infty</equation>时，<equation>\lim _ {x \rightarrow + \infty} f (x) = - \infty .</equation>由零点定理和单调性可知，<equation>f ( x )</equation>在<equation>(\sqrt{3}, +\infty)</equation>上有唯一零点，加上<equation>x=-\sqrt{3}, f ( x )</equation>在<equation>(-\infty, +\infty)</equation>上共有两个零点.

f（x）的性质可列表如下.

<table border="1"><tr><td></td><td>(-∞,-√3)</td><td>-√3</td><td>(-√3,√3)</td><td>√3</td><td>(√3,+∞)</td></tr><tr><td>f(x)</td><td>单调减少,无零点，limx→-∞f(x)=+∞</td><td>f(-3)=0</td><td>单调增加，无零点</td><td>f(√3)>0</td><td>单调减少，有唯一零点，limx→+∞f(x)=-∞</td></tr></table>

因此，方程<equation>f ( x ) = 0</equation>恰有两个实根.

---


