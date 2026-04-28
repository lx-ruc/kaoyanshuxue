#### 数列敛散性的判定

**2018年第19题 | 解答题 | 10分**

19. (本题满分10分）

设数列<equation>\{x_{n}\}</equation>满足：<equation>x_{1}>0,x_{n}\mathrm{e}^{x_{n+1}}=\mathrm{e}^{x_{n}}-1(n=1,2,\cdots).</equation>证明<equation>\{x_{n}\}</equation>收敛，并求<equation>\lim_{n\rightarrow \infty}x_{n}.</equation>

**解析:**解 由<equation>x_{n}\mathrm{e}^{x_{n + 1}} = \mathrm{e}^{x_{n}} - 1(n = 1,2,\dots)</equation>可得，<equation>x _ {n + 1} = \ln \left(\frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n}}\right).</equation>先用数学归纳法证明对所有的正整数 n，都有<equation>x_{n} > 0.</equation>首先，<equation>x_{1} > 0.</equation>假设当<equation>n=k</equation>时，<equation>x_{k} > 0</equation>注意到当<equation>x > 0</equation>时，<equation>\mathrm{e}^{x}-1 > x</equation>从而<equation>\frac{\mathrm{e}^{x}-1}{x} > 1.</equation>于是，<equation>x _ {k + 1} = \ln \left(\frac {\mathrm {e} ^ {x _ {k}} - 1}{x _ {k}}\right) > \ln 1 = 0.</equation>由数学归纳法可知，对所有的正整数 n，都有<equation>x_{n} > 0.</equation>因此，数列<equation>\{x_{n}\}</equation>有下界.

下面用两种方法证明数列<equation>\{x_{n}\}</equation>单调减少，即<equation>x_{n+1} < x_{n} ( n=1,2,\dots).</equation>（法一）由<equation>x_{n}\mathrm{e}^{x_{n}+1}=\mathrm{e}^{x_{n}}-1</equation>可知，<equation>\mathrm {e} ^ {x _ {n + 1}} = \frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n}} = \frac {\mathrm {e} ^ {x _ {n}} - \mathrm {e} ^ {0}}{x _ {n} - 0} \frac {\text {拉 格 朗 日}}{\text {中 值 定 理}} \mathrm {e} ^ {\xi_ {n}},</equation>其中<equation>\xi_{n}\in (0,x_{n})</equation>由于<equation>\mathrm{e}^{x}</equation>单调增加，故由<equation>\mathrm{e}^{x_{n+1}}=\mathrm{e}^{\xi_{n}}<\mathrm{e}^{x_{n}}</equation>可得<equation>x_{n+1}<x_{n}</equation>，即数列<equation>\left\{x_{n}\right\}</equation>单调减少.

（法二）<equation>x _ {n + 1} - x _ {n} = \ln \left(\frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n}}\right) - x _ {n} = \ln \left(\frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n} \mathrm {e} ^ {x _ {n}}}\right).</equation>记<equation>f ( x )=\mathrm{e}^{x}-1-x\mathrm{e}^{x}</equation>，则<equation>f^{\prime}(x)=\mathrm{e}^{x}-\mathrm{e}^{x}-x\mathrm{e}^{x}=-x\mathrm{e}^{x}.</equation>当<equation>x > 0</equation>时，<equation>f^{\prime}(x) < 0,f(x)</equation>在<equation>[0,+\infty)</equation>上单调减少，于是，<equation>f(x) < f(0)=0.</equation>从而，当<equation>x > 0</equation>时，<equation>\frac {\mathrm {e} ^ {x} - 1}{x \mathrm {e} ^ {x}} - 1 = \frac {\mathrm {e} ^ {x} - 1 - x \mathrm {e} ^ {x}}{x \mathrm {e} ^ {x}} < 0,</equation>即<equation>\frac{\mathrm{e}^{x}-1}{x\mathrm{e}^{x}}<1.</equation>又因为对所有的正整数 n ，都有<equation>x_{n} > 0</equation>，所以<equation>\ln \left(\frac{\mathrm{e}^{x_{n}}-1}{x_{n}\mathrm{e}^{x_{n}}}\right) < \ln 1=0</equation>，即<equation>x_{n+1}-x_{n} < 0.</equation>因此，数列<equation>\left\{x_{n}\right\}</equation>单调减少.

由单调有界准则可知，数列<equation>\{x_{n}\}</equation>收敛.由于对所有的正整数n，都有<equation>x_{n} > 0</equation>，故<equation>\lim_{n\to \infty}x_{n}=a\geqslant 0.</equation>对<equation>x_{n}\mathrm{e}^{x_{n+1}}=\mathrm{e}^{x_{n}}-1</equation>两端同时令<equation>n\to \infty</equation>，可得<equation>a\mathrm{e}^{a}=\mathrm{e}^{a}-1.</equation>由前面的结果可知，<equation>x=0</equation>是<equation>f(x)=\mathrm{e}^{x}-1-x\mathrm{e}^{x}</equation>在<equation>[0,+\infty)</equation>上的唯一零点.因此，<equation>a=0</equation>即<equation>\lim_{n\to \infty}x_{n}=0.</equation>

---


### 一元函数微分学


