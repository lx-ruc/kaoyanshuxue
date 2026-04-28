#### 定积分的概念、性质及几何意义

**2022年第4题 | 选择题 | 5分 | 答案: A**

4. 若<equation>I_{1}=\int_{0}^{1}\frac{x}{2(1+\cos x)}\mathrm{d}x,I_{2}=\int_{0}^{1}\frac{\ln(1+x)}{1+\cos x}\mathrm{d}x,I_{3}=\int_{0}^{1}\frac{2x}{1+\sin x}\mathrm{d}x</equation>，则（    )

A.<equation>I_{1}<I_{2}<I_{3}</equation>B.<equation>I_{2}<I_{1}<I_{3}</equation>C.<equation>I_{1}<I_{3}<I_{2}</equation>D.<equation>I_{3}<I_{2}<I_{1}</equation>

答案: A

**解析:**解 通过观察可发现，要比较<equation>I_{1}</equation>与<equation>I_{2}</equation>的大小，只需比较<equation>\frac{x}{2}</equation>与<equation>\ln(1+x)</equation>的大小.

令<equation>f(x)=\ln(1+x)-\frac{x}{2}</equation>，则<equation>f(0)=0</equation><equation>f^{\prime}(x)=\frac{1}{1+x}-\frac{1}{2}</equation>当<equation>x\in(0,1)</equation>时，<equation>f^{\prime}(x)>0</equation><equation>f(x)</equation>单调增加，从而<equation>f(x)>f(0)=0</equation>即<equation>\ln(1+x)>\frac{x}{2},\frac{\ln(1+x)}{1+\cos x}>\frac{x}{2(1+\cos x)}</equation>因此，<equation>I_{2}>I_{1}</equation>.

此外，同样的方法不难证明在(0,1)内，<equation>\ln(1+x)<x.</equation>另一方面，由于在(0,1)内，<equation>0<\sin x,\cos x<1,1<1+\sin x<2</equation>故<equation>I_{3}</equation>的被积函数<equation>\frac{2x}{1+\sin x} > x.</equation>结合<equation>\ln(1+x)<x</equation>可得，<equation>\frac{\ln(1+x)}{1+\cos x}<\frac{x}{1+\cos x}<x.</equation>于是，<equation>\frac{2x}{1+\sin x}>x>\frac{\ln(1+x)}{1+\cos x}.</equation>因此，<equation>I_{3}>I_{2}.</equation>综上所述，应选A.

---

**2021年第4题 | 选择题 | 5分 | 答案: B**

4. 设函数 f(x)在区间[0,1]上连续，则<equation>\int_{0}^{1} f(x)\mathrm{d}x=</equation>(    )

A.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{n}f\left(\frac{2k-1}{2n}\right)\frac{1}{2n}</equation>B.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{n}f\left(\frac{2k-1}{2n}\right)\frac{1}{n}</equation>C.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{2n}f\left(\frac{k-1}{2n}\right)\frac{1}{n}</equation>D.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{2n}f\left(\frac{k}{2n}\right)\frac{2}{n}</equation>

答案: B

**解析:**解 由于 f(x)连续，故<equation>\int_{0}^{1} f(x)\mathrm{d}x</equation>存在，从而可对区间[0，1]进行划分，将该积分写为 n项和式的极限.

将[0，1]分为n等份，每个小区间为<equation>\left[ \frac{k-1}{n},\frac{k}{n}\right]</equation><equation>k=1,2,\dots,n</equation>从<equation>\left[ \frac{k-1}{n},\frac{k}{n}\right]</equation>中取点<equation>\frac{2k-1}{2n}</equation>故由<equation>\int_{0}^{1} f(x)\mathrm{d}x</equation>存在以及定积分的定义可得<equation>\int_ {0} ^ {1} f (x) \mathrm {d} x = \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} f \left(\frac {2 k - 1}{2 n}\right) \cdot \frac {1}{n}.</equation>因此，应选B.

下面说明选项A、C、D均不正确.

选项A：<equation>\lim_{n\to \infty}\sum_{k = 1}^{n}f\left(\frac{2k - 1}{2n}\right)\frac{1}{2n} = \frac{1}{2}\lim_{n\to \infty}\sum_{k = 1}^{n}f\left(\frac{2k - 1}{2n}\right)\frac{1}{n} = \frac{1}{2}\int_{0}^{1}f(x)\mathrm{d}x.</equation>选项C：<equation>\lim_{n\to \infty}\sum_{k = 1}^{2n}f\left(\frac{k - 1}{2n}\right)\frac{1}{n} = 2\lim_{n\to \infty}\sum_{k = 1}^{2n}f\left(\frac{k - 1}{2n}\right)\frac{1}{2n} = 2\int_{0}^{1}f(x)\mathrm{d}x.</equation>选项D：<equation>\lim_{n\to \infty}\sum_{k = 1}^{2n}f\left(\frac{k}{2n}\right)\frac{2}{n} = 4\lim_{n\to \infty}\sum_{k = 1}^{2n}f\left(\frac{k}{2n}\right)\frac{1}{2n} = 4\int_{0}^{1}f(x)\mathrm{d}x.</equation>

---

**2018年第4题 | 选择题 | 4分 | 答案: C**

4. 设<equation>M=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{(1+x)^{2}}{1+x^{2}}\mathrm{d}x</equation>，<equation>N=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{1+x}{\mathrm{e}^{x}}\mathrm{d}x</equation>，<equation>K=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}(1+\sqrt{\cos x})\mathrm{d}x</equation>，则（    )

A.<equation>M>N>K</equation>B.<equation>M>K>N</equation>C.<equation>K>M>N</equation>D.<equation>K>N>M</equation>

答案: C

**解析:**解分别计算 M,N,K.

由于<equation>\frac{2x}{1 + x^2}</equation>是奇函数，故<equation>\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{2x}{1 + x^2}\mathrm{d}x = 0.</equation>于是，<equation>M = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {(1 + x) ^ {2}}{1 + x ^ {2}} \mathrm {d} x = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {1 + x ^ {2} + 2 x}{1 + x ^ {2}} \mathrm {d} x \xlongequal {\frac {\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {2 x}{1 + x ^ {2}} \mathrm {d} x = 0}{}} \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \mathrm {d} x = \pi .</equation>注意到当<equation>x\neq 0</equation>时，<equation>\mathrm{e}^{x} > 1 + x.</equation>于是，在<equation>\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>上，<equation>\frac{1+x}{\mathrm{e}^{x}}\leqslant 1</equation>且等号仅在<equation>x=0</equation>处成立.<equation>N = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {1 + x}{\mathrm {e} ^ {x}} \mathrm {d} x < \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \mathrm {d} x = \pi .</equation>由于<equation>\sqrt{\cos x}</equation>是偶函数，且当 x<equation>\in\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>时，<equation>\cos x\geqslant0</equation>且等号仅在端点处成立，故<equation>\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\sqrt{\cos x}\mathrm{d}x=2\int_{0}^{\frac{\pi}{2}}\sqrt{\cos x}\mathrm{d}x>0.</equation>于是，<equation>K = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \left(1 + \sqrt {\cos x}\right) \mathrm {d} x = \pi + \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \sqrt {\cos x} \mathrm {d} x > \pi .</equation>综上所述，<equation>K > M > N</equation>应选C.

---

**2017年第16题 | 解答题 | 10分**

16. (本题满分10分)<equation>\text {求} \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n ^ {2}} \ln \left(1 + \frac {k}{n}\right)</equation>

**解析:**解 根据定积分的定义，提出因子<equation>\frac{1}{n}</equation>，可得<equation>\begin{aligned} \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n ^ {2}} \ln \left(1 + \frac {k}{n}\right) &= \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n} \ln \left(1 + \frac {k}{n}\right) \cdot \frac {1}{n} = \int_ {0} ^ {1} x \ln (1 + x) d x \\ &= \frac {1}{2} \int_ {0} ^ {1} \ln (1 + x) d \left(x ^ {2}\right) \xlongequal {\text {分 部 积 分}} \frac {x ^ {2}}{2} \ln (1 + x) \left| _ {0} ^ {1} - \int_ {0} ^ {1} \frac {x ^ {2}}{2 (1 + x)} d x \right. \\ &= \frac {\ln 2}{2} - \frac {1}{2} \int_ {0} ^ {1} \frac {x ^ {2} - 1 + 1}{1 + x} d x = \frac {\ln 2}{2} - \frac {1}{2} \int_ {0} ^ {1} \left(x - 1 + \frac {1}{1 + x}\right) d x \\ &= \frac {\ln 2}{2} - \frac {1}{2} \left[ \frac {x ^ {2}}{2} - x + \ln (1 + x) \right] \Bigg | _ {0} ^ {1} = \frac {1}{4}. \end{aligned}</equation>因此，原极限<equation>= \frac{1}{4}.</equation>

---

**2012年第4题 | 选择题 | 4分 | 答案: D**

4. 设<equation>I_{k}=\int_{0}^{k\pi}\mathrm{e}^{x^{2}}\sin x\mathrm{d}x(k=1,2,3)</equation>，则有（    ）

A.<equation>I_{1}<I_{2}<I_{3}</equation>B.<equation>I_{3}<I_{2}<I_{1}</equation>C.<equation>I_{2}<I_{3}<I_{1}</equation>D.<equation>I_{2}<I_{1}<I_{3}</equation>

答案: D

**解析:**解（法一）记<equation>J_{k}=\int_{(k-1)\pi}^{k\pi}\mathrm{e}^{x^{2}}\sin x\mathrm{d}x(k=1,2,3)</equation>，则<equation>I _ {1} = J _ {1}, \quad I _ {2} = J _ {1} + J _ {2}, \quad I _ {3} = J _ {1} + J _ {2} + J _ {3}.</equation>由于<equation>\mathrm{e}^{x^{2}} > 0</equation>，且在（0，<equation>\pi</equation>）上，<equation>\sin x > 0</equation>；在（<equation>\pi,2\pi</equation>）上，<equation>\sin x < 0</equation>；在（<equation>2\pi,3\pi</equation>）上，<equation>\sin x > 0</equation>，故<equation>J_{1}>0</equation>，<equation>J_{2}<0</equation>，<equation>J_{3}>0</equation>.由此可得，<equation>I_{1}>I_{2}</equation>，<equation>I_{3}>I_{2}</equation>.

下面比较<equation>I_{1}</equation>和<equation>I_{3}.</equation><equation>I _ {3} - I _ {1} = J _ {2} + J _ {3}.</equation><equation>J _ {3} = \int_ {2 \pi} ^ {3 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x > \mathrm {e} ^ {(2 \pi) ^ {2}} \int_ {2 \pi} ^ {3 \pi} \sin x \mathrm {d} x,</equation><equation>\left| J _ {2} \right| = \left| \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x \right| < \mathrm {e} ^ {(2 \pi) ^ {2}} \left| \int_ {\pi} ^ {2 \pi} \sin x \mathrm {d} x \right|, \quad J _ {2} > - \mathrm {e} ^ {(2 \pi) ^ {2}} \left| \int_ {\pi} ^ {2 \pi} \sin x \mathrm {d} x \right|.</equation>由定积分的几何意义可知，<equation>\int_{2\pi}^{3\pi}\sin x\mathrm{d}x</equation>和<equation>|\int_{\pi}^{2\pi}\sin x\mathrm{d}x|</equation>分别为<equation>\sin x</equation>在<equation>(2\pi ,3\pi)</equation>上以及在<equation>(\pi ,2\pi)</equation>上的部分与<equation>x</equation>轴围成的图形面积.根据<equation>\sin x</equation>的图形，这两部分面积相等，即<equation>\int_{2\pi}^{3\pi}\sin x\mathrm{d}x = \left|\int_{\pi}^{2\pi}\sin x\mathrm{d}x\right|.</equation>于是，

于是，<equation>J _ {2} + J _ {3} > \mathrm {e} ^ {(2 \pi) ^ {2}} \left(\int_ {2 \pi} ^ {3 \pi} \sin x \mathrm {d} x - \left| \int_ {\pi} ^ {2 \pi} \sin x \mathrm {d} x \right|\right) = 0,</equation>即<equation>I_{3} > I_{1}.</equation>因此，<equation>I_{2} < I_{1} < I_{3}</equation>应选D.

（法二）在法一中，证明<equation>J_{2} + J_{3} > 0</equation>，也可以使用如下方法.<equation>J _ {3} = \int_ {2 \pi} ^ {3 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x \xlongequal {u = x - \pi} \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {(u + \pi) ^ {2}} \sin (u + \pi) \mathrm {d} u = - \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {(u + \pi) ^ {2}} \sin u \mathrm {d} u,</equation><equation>J _ {2} + J _ {3} = \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x - \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {(x + \pi) ^ {2}} \sin x \mathrm {d} x = \int_ {\pi} ^ {2 \pi} \sin x \left[ \mathrm {e} ^ {x ^ {2}} - \mathrm {e} ^ {(x + \pi) ^ {2}} \right] \mathrm {d} x.</equation>当<equation>x\in (\pi ,2\pi)</equation>时，<equation>\sin x < 0,\mathrm{e}^{x^2} - \mathrm{e}^{(x + \pi)^2} < 0,\sin x[\mathrm{e}^{x^2} - \mathrm{e}^{(x + \pi)^2}] > 0</equation>，从而<equation>J_{2} + J_{3} > 0.</equation>其余同法一.

---

**2011年第4题 | 选择题 | 4分 | 答案: B**

4. 设<equation>I=\int_{0}^{\frac{\pi}{4}}\ln(\sin x)\mathrm{d}x, J=\int_{0}^{\frac{\pi}{4}}\ln(\cot x)\mathrm{d}x, K=\int_{0}^{\frac{\pi}{4}}\ln(\cos x)\mathrm{d}x</equation>，则 I,J,K的大小关系为（    )

A. I<J<K B. I<K<J C. J<I<K D. K<J<I

答案: B

**解析:**解 当 0 < x <<equation>\frac{\pi}{4}</equation>时，0 < sin x < cos x < 1 < cot x.又 f(t) = ln t在（0，+<equation>\infty</equation>）上单调增加，故当 0 < x <<equation>\frac{\pi}{4}</equation>时，<equation>\ln(\sin x) < \ln(\cos x) < \ln(\cot x)</equation>，从而由积分的保号性可知， I < K < J ，选B.

---

**2010年第17题 | 解答题 | 10分**

17. (本题满分10分)

17. (本题满分10分)

I. 比较<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>与<equation>\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t</equation>（ n=1,2，<equation>\cdots</equation>）的大小，说明理由；

II. 记<equation>u_{n}=\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>（ n=1,2，<equation>\cdots</equation>），求极限<equation>\lim_{n\to\infty}u_{n}.</equation>

**答案:**(17) （I）<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t<\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t</equation>，理由略；（Ⅱ）<equation>\lim_{n\to\infty}u_{n}=0.</equation>

**解析:**解（I）在（0，1]上，<equation>|\ln t|</equation><equation>\ln(1+t)</equation>与 t均非负，故比较<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>与<equation>\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t(n=1,2,\cdots)</equation>的大小，只需比较<equation>\ln(1+t)</equation>与 t的大小.

考虑 f（t）=<equation>\ln(1+t)-t.</equation><equation>f ^ {\prime} (t) = \frac {1}{1 + t} - 1.</equation>当<equation>t\in (0,1]</equation>时，<equation>f^{\prime}(t) < 0,f(t)\leqslant f(0) = 0.</equation>因此，当<equation>t \in [0,1]</equation>时，<equation>\ln (1 + t) \leqslant t.</equation>由于两被积函数仅在<equation>t = 1</equation>处相等，故<equation>\int_ {0} ^ {1} | \ln t | [ \ln (1 + t) ] ^ {n} \mathrm {d} t < \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t (n = 1, 2, \dots).</equation>（Ⅱ）（法一）由第（I）问知，<equation>0 < u_{n} < \int_{0}^{1} t^{n}|\ln t|\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {0} ^ {1} t ^ {n} \mid \ln t \mid \mathrm {d} t &= \frac {- 1}{n + 1} \int_ {0} ^ {1} \ln t \mathrm {d} \left(t ^ {n + 1}\right) = \frac {- 1}{n + 1} \left(t ^ {n + 1} \ln t \mid_ {0} ^ {1} - \int_ {0} ^ {1} t ^ {n + 1} \cdot \frac {1}{t} \mathrm {d} t\right) \\ \frac {\lim _ {t \rightarrow 0 ^ {+}} t ^ {n + 1} \ln t = 0}{\overline {{\quad}}} \frac {1}{n + 1} \int_ {0} ^ {1} t ^ {n} \mathrm {d} t &= \frac {1}{(n + 1) ^ {2}}. \end{aligned}</equation>因此，<equation>\lim _ {n \rightarrow \infty} \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t = \lim _ {n \rightarrow \infty} \frac {1}{(n + 1) ^ {2}} = 0.</equation>由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>（法二）由第（I）问知，<equation>0 < u_{n} < \int_{0}^{1} t^{n}|\ln t|\mathrm{d}t.</equation>又因为<equation>\lim_{t\to 0^{+}}(t\ln t) = 0</equation>，所以存在<equation>M > 0</equation>，使得对任意的<equation>t\in (0,1]</equation>，有<equation>t|\ln t|\leqslant M</equation>，从而<equation>0 < u _ {n} < \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t \leqslant M \int_ {0} ^ {1} t ^ {n - 1} \mathrm {d} t = \frac {M}{n}.</equation>由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>（法三）由于<equation>t\in[0,1]</equation>时，<equation>\ln(1 + t)\leqslant \ln 2 < 1</equation>，故<equation>u_{n}\leqslant (\ln 2)^{n}\int_{0}^{1}|\ln t|\mathrm{d}t.</equation>计算<equation>\int_{0}^{1}|\ln t| \mathrm{d} t</equation>得，<equation>\int_ {0} ^ {1} | \ln t | \mathrm {d} t = - \int_ {0} ^ {1} \ln t \mathrm {d} t = - \left(t \ln t \left| _ {0} ^ {1} - \int_ {0} ^ {1} 1 \mathrm {d} t\right)\right) \xlongequal {\lim _ {t \rightarrow 0 ^ {+}} t \ln t = 0} 1.</equation>从而<equation>0 < u_{n}\leqslant (\ln 2)^{n}</equation>因为<equation>\lim_{n\to \infty}(\ln 2)^n = 0</equation>，所以由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>

---


