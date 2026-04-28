#### 不等式的证明

**2012年第15题 | 解答题 | 10分**

15. (本题满分10分)

证明：<equation>x\ln \frac{1+x}{1-x}+\cos x\geqslant 1+\frac{x^{2}}{2},(-1<x<1).</equation>

**答案:**15) 证明略.

**解析:**证（法一）考虑辅助函数<equation>f ( x )=x \ln \frac{1+x}{1-x}+\cos x-1-\frac{x^{2}}{2}.</equation><equation>f (- x) = (- x) \ln \frac {1 - x}{1 + x} + \cos x - 1 - \frac {x ^ {2}}{2} = f (x),</equation>故 f(x)为偶函数.如果能证明当 x<equation>\in[0,1)</equation>时，<equation>f(x)\geqslant0</equation>，那么当 x<equation>\in(-1,1)</equation>时，也有 f(x)<equation>\geqslant0</equation>从而题给不等式成立.

计算<equation>f^{\prime}(x)</equation><equation>f ^ {\prime} (x) = \left(x \ln \frac {1 + x}{1 - x} + \cos x - 1 - \frac {x ^ {2}}{2}\right) ^ {\prime} = \frac {2 x}{1 - x ^ {2}} + \ln \frac {1 + x}{1 - x} - \sin x - x.</equation>由于当<equation>x\in [0,1)</equation>时，<equation>\frac{x}{1 - x^2}\geqslant x\geqslant \sin x</equation>，故<equation>\frac {2 x}{1 - x ^ {2}} \geqslant 2 x \geqslant \sin x + x,</equation>等号在<equation>x=0</equation>时取得.又因为<equation>\frac{1+x}{1-x}\geqslant 1</equation>，所以<equation>\ln \frac{1+x}{1-x}\geqslant 0</equation>，等号在<equation>x=0</equation>时取得.

因此，当<equation>x\in(0,1)</equation>时，<equation>f ^ {\prime} (x) = \frac {2 x}{1 - x ^ {2}} + \ln \frac {1 + x}{1 - x} - \sin x - x > 0.</equation>综上所述，<equation>f ( x )</equation>在[0,1)上单调增加，<equation>f ( 0 )</equation>为<equation>f ( x )</equation>在[0,1)上的最小值.又由<equation>f ( x )</equation>为偶函数可知，在(-1，1)上，<equation>f ( x ) \geqslant f ( 0 ) = 0</equation>即<equation>x \ln \frac{1+x}{1-x} +\cos x\geqslant 1+\frac{x^{2}}{2}(-1<x<1).</equation>（法二）在法一中求得<equation>f^{\prime}(x)=\frac{2x}{1-x^{2}}+\ln \frac{1+x}{1-x}-\sin x-x</equation>后，继续求<equation>f^{\prime\prime}(x)</equation>以判断<equation>f^{\prime}(x)</equation>的性质.<equation>f ^ {\prime \prime} (x) = \frac {2 \left(1 + x ^ {2}\right)}{\left(1 - x ^ {2}\right) ^ {2}} + \frac {1}{1 + x} - \frac {(- 1)}{1 - x} - \cos x - 1 = \frac {4}{\left(1 - x ^ {2}\right) ^ {2}} - \cos x - 1.</equation>由于当 x<equation>\in[0,1)</equation>时，<equation>\frac {4}{\left(1 - x ^ {2}\right) ^ {2}} \geqslant 4, \quad 1 + \cos x \leqslant 2,</equation>故<equation>f^{\prime \prime}(x) > 0. f^{\prime}(x)</equation>在[0，1）上单调增加，<equation>f^{\prime}(x)\geqslant f^{\prime}(0)=0,f(x)</equation>在[0，1）上单调增加.

（法三）首先，<equation>f ( x ) = x \ln \frac { 1 + x } { 1 - x } + \cos x</equation>为偶函数，<equation>g ( x ) = 1 + \frac { x^{2}}{2}</equation>也为偶函数，故我们只需证明，在（0，1）上，<equation>f ( x ) \geqslant g ( x )</equation>，并且<equation>f ( 0 ) = g ( 0 )</equation>，便能得到在（-1，1）上，<equation>f ( x ) \geqslant g ( x )</equation>由泰勒中值定理，<equation>\cos x=1-\frac{x^{2}}{2!}+\frac{\cos \xi}{4!} x^{4},\xi</equation>为介于0和x之间的某个值.于是，当<equation>x\in(0,1)</equation>时，<equation>\cos x\geqslant 1-\frac{x^{2}}{2}.</equation>从而<equation>f (x) = x \ln \frac {1 + x}{1 - x} + \cos x \geqslant x \ln \frac {1 + x}{1 - x} + 1 - \frac {x ^ {2}}{2}.</equation>若能证明<equation>x\ln \frac{1+x}{1-x}+1-\frac{x^{2}}{2}\geqslant 1+\frac{x^{2}}{2}</equation>，则由不等号的传递性可知原不等式得证.

由于当 x<equation>\in(0,1)</equation>时，<equation>x \ln \frac {1 + x}{1 - x} + 1 - \frac {x ^ {2}}{2} \geqslant 1 + \frac {x ^ {2}}{2} \Leftrightarrow x \ln \frac {1 + x}{1 - x} \geqslant x ^ {2} \Leftrightarrow \ln \frac {1 + x}{1 - x} \geqslant x,</equation>故我们只需要证明<equation>\ln \frac{1+x}{1-x}\geqslant x.</equation>考虑<equation>\varphi(x)=\ln \frac{1+x}{1-x}-x.</equation><equation>\varphi^ {\prime} (x) = \frac {1}{1 + x} - \frac {(- 1)}{1 - x} - 1 = \frac {2}{1 - x ^ {2}} - 1.</equation>当 x<equation>\in(0,1)</equation>时，<equation>\frac{2}{1-x^{2}}\geqslant2</equation>从而<equation>\varphi^{\prime}(x)=\frac{2}{1-x^{2}}-1>0, \varphi(x)</equation>在（0，1）上单调增加，<equation>\varphi(x)\geqslant\varphi(0)=0.</equation>综上所述，原不等式成立.

---


### 无穷级数


