#### 不等式

**2012年第18题 | 解答题 | 10分**

18. (本题满分10分)

证明<equation>x\ln \frac{1+x}{1-x}+\cos x\geqslant 1+\frac{x^{2}}{2}(-1<x<1).</equation>

**答案:**## （18）证明略.

**解析:**证（法一）考虑辅助函数<equation>f ( x )=x \ln \frac{1+x}{1-x}+\cos x-1-\frac{x^{2}}{2}.</equation>由于<equation>f (- x) = (- x) \ln \frac {1 - x}{1 + x} + \cos x - 1 - \frac {x ^ {2}}{2} = f (x),</equation>故 f(x)为偶函数.如果能证明当 x<equation>\in[0,1)</equation>时，<equation>f(x)\geqslant0</equation>，那么当 x<equation>\in(-1,1)</equation>时，也有 f(x)<equation>\geqslant0</equation>，从而题给不等式成立.

计算<equation>f^{\prime}(x)</equation><equation>f ^ {\prime} (x) = \left(x \ln \frac {1 + x}{1 - x} + \cos x - 1 - \frac {x ^ {2}}{2}\right) ^ {\prime} = \frac {2 x}{1 - x ^ {2}} + \ln \frac {1 + x}{1 - x} - \sin x - x.</equation>由于当<equation>x\in [0,1)</equation>时，<equation>\frac{x}{1 - x^2}\geqslant x\geqslant \sin x</equation>，故<equation>\frac {2 x}{1 - x ^ {2}} \geqslant 2 x \geqslant \sin x + x,</equation>等号在 x=0时取得.又因为<equation>\frac{1+x}{1-x}\geqslant 1</equation>，所以<equation>\ln \frac{1+x}{1-x}\geqslant 0</equation>，等号在 x=0时取得.

因此，当<equation>x\in(0,1)</equation>时，<equation>f ^ {\prime} (x) = \frac {2 x}{1 - x ^ {2}} + \ln \frac {1 + x}{1 - x} - \sin x - x > 0.</equation>综上所述，<equation>f ( x )</equation>在[0,1]上单调增加，<equation>f ( 0 )</equation>为<equation>f ( x )</equation>在[0,1]上的最小值.又由<equation>f ( x )</equation>为偶函数可知，在（-1，1）上，<equation>f ( x ) \geqslant f ( 0 ) = 0</equation>即<equation>x \ln \frac{1+x}{1-x}+\cos x\geqslant 1+\frac{x^{2}}{2}(-1<x<1).</equation>（法二）在法一中求得<equation>f^{\prime}(x)=\frac{2x}{1-x^{2}}+\ln \frac{1+x}{1-x}-\sin x-x</equation>后，继续求<equation>f^{\prime\prime}(x)</equation>以判断<equation>f^{\prime}(x)</equation>的性质.<equation>f ^ {\prime \prime} (x) = \frac {2 \left(1 + x ^ {2}\right)}{\left(1 - x ^ {2}\right) ^ {2}} + \frac {1}{1 + x} - \frac {- 1}{1 - x} - \cos x - 1 = \frac {4}{\left(1 - x ^ {2}\right) ^ {2}} - \cos x - 1.</equation>由于当<equation>x\in [0,1)</equation>时，<equation>\frac {4}{\left(1 - x ^ {2}\right) ^ {2}} \geqslant 4, \quad 1 + \cos x \leqslant 2,</equation>故<equation>f^{\prime \prime}(x) > 0. f^{\prime}(x)</equation>在[0,1）上单调增加，<equation>f^{\prime}(x)\geqslant f^{\prime}(0)=0,f(x)</equation>在[0,1）上单调增加.

（法三）首先，<equation>f(x)=x\ln \frac{1+x}{1-x}+\cos x</equation>为偶函数，<equation>g(x)=1+\frac{x^{2}}{2}</equation>也为偶函数，且<equation>f(0)=g(0)=1</equation>故我们只需证明，在（0，1）上，<equation>f(x)\geqslant g(x)</equation>，便能得到在（-1，1）上，<equation>f(x)\geqslant g(x).</equation>由泰勒中值定理，<equation>\cos x=1-\frac{x^{2}}{2!}+\frac{\cos \xi}{4!} x^{4},\xi</equation>为介于0和x之间的某个值.于是，当<equation>x\in(0,1)</equation>时，<equation>\cos x\geqslant 1-\frac{x^{2}}{2}.</equation>从而<equation>f (x) = x \ln \frac {1 + x}{1 - x} + \cos x \geqslant x \ln \frac {1 + x}{1 - x} + 1 - \frac {x ^ {2}}{2}.</equation>若能证明<equation>x\ln \frac{1+x}{1-x}+1-\frac{x^{2}}{2}\geqslant 1+\frac{x^{2}}{2}</equation>，则由不等号的传递性可知原不等式得证.

由于当<equation>x\in (0,1)</equation>时，<equation>x \ln \frac {1 + x}{1 - x} + 1 - \frac {x ^ {2}}{2} \geqslant 1 + \frac {x ^ {2}}{2} \Leftrightarrow x \ln \frac {1 + x}{1 - x} \geqslant x ^ {2} \Leftrightarrow \ln \frac {1 + x}{1 - x} \geqslant x,</equation>故我们只需要证明<equation>\ln \frac{1+x}{1-x}\geqslant x.</equation>考虑<equation>\varphi(x)=\ln \frac{1+x}{1-x}-x.</equation><equation>\varphi^ {\prime} (x) = \frac {1}{1 + x} - \frac {- 1}{1 - x} - 1 = \frac {2}{1 - x ^ {2}} - 1.</equation>当<equation>x \in(0,1)</equation>时，<equation>\frac{2}{1-x^{2}}\geqslant 2</equation>从而<equation>\varphi^{\prime}(x)=\frac{2}{1-x^{2}}-1>0, \varphi(x)</equation>在（0,1）上单调增加，<equation>\varphi(x)\geqslant \varphi(0)=0.</equation>综上所述，原不等式成立.

---

**2010年第4题 | 选择题 | 4分 | 答案: C**

4. 设<equation>f(x)=\ln^{1 0} x,g(x)=x,h(x)=\mathrm{e}^{\frac{x}{1 0}}</equation>，则当 x充分大时有（    )

A. g(x) < h(x) < f(x) B. h(x) < g(x) < f(x) C. f(x) < g(x) < h(x) D. g(x) < f(x) < h(x)

答案: C

**解析:**（法一）由于<equation>\lim _ {x \rightarrow + \infty} \frac {h (x)}{g (x)} = \lim _ {x \rightarrow + \infty} \frac {\mathrm {e} ^ {\frac {x}{1 0}}}{x} \xlongequal {\text {洛 必达}} \lim _ {x \rightarrow + \infty} \frac {\frac {1}{1 0} \mathrm {e} ^ {\frac {x}{1 0}}}{1} = + \infty ,</equation>故当 x充分大时，<equation>h ( x ) > g ( x ).</equation>又由于<equation>\lim _ {x \rightarrow + \infty} \frac {g (x)}{f (x)} = \lim _ {x \rightarrow + \infty} \frac {x}{\ln^ {1 0} x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow + \infty} \frac {x}{1 0 \ln^ {9} x} \xlongequal {\text {洛必达}} \dots \xlongequal {\text {洛必达}} \lim _ {x \rightarrow + \infty} \frac {x}{1 0 !} = + \infty ,</equation>故当<equation>x</equation>充分大时，<equation>g(x) > f(x)</equation>综上所述，当<equation>x</equation>充分大时，<equation>h(x) > g(x) > f(x)</equation>.应选C.

（法二）令<equation>H ( x )=h ( x )-g ( x )=\mathrm{e}^{\frac{x}{1 0}}-x</equation>，则<equation>H^{\prime}(x)=\frac{1}{1 0}\mathrm{e}^{\frac{x}{1 0}}-1.</equation>由于当<equation>x\geqslant 1 0 0</equation>时，<equation>\frac{1}{1 0}\mathrm{e}^{\frac{x}{1 0}}-1\geqslant</equation><equation>\frac{1}{1 0}\mathrm{e}^{1 0}-1>0</equation>，故H(x）在<equation>[ 1 0 0,+\infty)</equation>上为单调增加函数，从而当<equation>x\geqslant 1 0 0</equation>时，<equation>h (x) - g (x) \geqslant h (1 0 0) - g (1 0 0) = \mathrm {e} ^ {1 0} - 1 0 0 \geqslant 2 ^ {1 0} - 1 0 0 > 0.</equation>令<equation>F(x) = x^{\frac{1}{10}} - \ln x</equation>，则<equation>F^{\prime}(x) = \frac{1}{10} x^{-\frac{9}{10}} - \frac{1}{x} = \frac{1}{10x}\left(x^{\frac{1}{10}} - 10\right)</equation>.由于当<equation>x > 10^{10}</equation>时，<equation>F^{\prime}(x) > 0</equation>，故<equation>F(x)</equation>在<equation>[10^{10}, + \infty)</equation>上为单调增加函数，从而当<equation>x > 10^{100}</equation>时，<equation>F(x) \geqslant F(10^{100}) = 10^{10} - 100\ln 10 > 0</equation>即<equation>x^{\frac{1}{10}} > \ln x.</equation>因此，<equation>x > \ln^{10}x.</equation>综上所述，当 x充分大时，<equation>h ( x ) > g ( x ) > f ( x )</equation>.应选C.

---


### 无穷级数


