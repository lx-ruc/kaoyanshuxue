#### 重积分的概念与性质

**2010年第4题 | 选择题 | 4分 | 答案: D**

4.<equation>\lim_{n\rightarrow \infty}\sum_{i=1}^{n}\sum_{j=1}^{n}\frac{n}{(n+i)(n^{2}+j^{2})}=</equation>(    )

A.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{x}\frac{1}{(1+x)(1+y^{2})}\mathrm{d}y</equation>B.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{x}\frac{1}{(1+x)(1+y)}\mathrm{d}y</equation>C.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{1}\frac{1}{(1+x)(1+y)}\mathrm{d}y</equation>D.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{1}\frac{1}{(1+x)(1+y^{2})}\mathrm{d}y</equation>

答案: D

**解析:**解 （法一）考虑将原极限写成二重积分.

令<equation>\Delta \sigma_{ij} = \left[\frac{i - 1}{n},\frac{i}{n}\right]\times \left[\frac{j - 1}{n},\frac{j}{n}\right](i,j = 1,2,\dots ,n)</equation>，则<equation>\{\Delta \sigma_{ij}\}_{1\leqslant i,j\leqslant n}</equation>为<equation>D = [0,1]\times [0,1]</equation>上的一个划分，<equation>\Delta \sigma_{ij}</equation>的面积为<equation>\frac{1}{n^2}</equation>.取<equation>\Delta \sigma_{ij}</equation>上的一点<equation>\left(\frac{i}{n},\frac{j}{n}\right)</equation>.

由于<equation>\sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {n}{(n + i) \left(n ^ {2} + j ^ {2}\right)} = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {1}{\left(1 + \frac {i}{n}\right) \left(1 + \frac {j ^ {2}}{n ^ {2}}\right)} \cdot \frac {1}{n ^ {2}},</equation>故<equation>\begin{aligned} \text {原 极 限} &= \lim _ {n \rightarrow \infty} \left[ \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {1}{\left(1 + \frac {i}{n}\right)\left(1 + \frac {j ^ {2}}{n ^ {2}}\right)} \right] = \iint_ {D} \frac {1}{(1 + x) \left(1 + y ^ {2}\right)} \mathrm {d} \sigma \\ &= \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {1} \frac {1}{(1 + x) \left(1 + y ^ {2}\right)} \mathrm {d} y. \end{aligned}</equation>应选 D.

（法二）由于所求极限的表达式中 i，j无关，故可以考虑将原极限写成定积分的乘积.由于<equation>\begin{aligned} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {n}{(n + i) \left(n ^ {2} + j ^ {2}\right)} &= \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \left(\frac {1}{1 + \frac {i}{n}} \cdot \frac {1}{n}\right) \left(\frac {1}{1 + \frac {j ^ {2}}{n ^ {2}}} \cdot \frac {1}{n}\right) \\ \underline {{i , j \text {无关}}} \sum_ {i = 1} ^ {n} \left(\frac {1}{1 + \frac {i}{n}} \cdot \frac {1}{n}\right) \sum_ {j = 1} ^ {n} \left(\frac {1}{1 + \frac {j ^ {2}}{n ^ {2}}} \cdot \frac {1}{n}\right), \end{aligned}</equation>故<equation>\begin{aligned} &= \lim _ {n \rightarrow \infty} \sum_ {i = 1} ^ {n} \left(\frac {1}{1 + \frac {i}{n}} \cdot \frac {1}{n}\right) \cdot \lim _ {n \rightarrow \infty} \sum_ {j = 1} ^ {n} \left(\frac {1}{1 + \frac {j ^ {2}}{n ^ {2}}} \cdot \frac {1}{n}\right) = \left(\int_ {0} ^ {1} \frac {1}{1 + x} \mathrm {d} x\right)\left(\int_ {0} ^ {1} \frac {1}{1 + y ^ {2}} \mathrm {d} y\right) \\ &= \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {1} \frac {1}{(1 + x) \left(1 + y ^ {2}\right)} \mathrm {d} y. \end{aligned}</equation>应选 D.

---

**2009年第2题 | 选择题 | 4分 | 答案: A**

2. 如图，正方形<equation>\{(x,y)\mid|x|\leqslant1,|y|\leqslant1\}</equation>被其对角线划分为四个区域<equation>D_{k}(k=1,2,3,4),I_{k}=\iint_{D_{k}}y\cos x\mathrm{d}x\mathrm{d}y</equation>则<equation>\max_{1\leqslant k\leqslant4}\{I_{k}\}=</equation>（    ）

A.<equation>I_{1}</equation>B.<equation>I_{2}</equation>C.<equation>I_{3}</equation>D.<equation>I_{4}</equation>

答案: A

**解析:**解 令<equation>f ( x,y)=y \cos x</equation>，由于<equation>D_{4}</equation>关于x轴对称，且<equation>f ( x,y)=-f ( x,-y)</equation>，故<equation>I_{4}=0</equation>.同理得到<equation>I_{2}=0</equation>.又<equation>f ( x,y)</equation>在<equation>D_{1}</equation>内部恒大于0，在<equation>D_{3}</equation>内部恒小于0，故由重积分的保号性知，<equation>I_{1}>0, I_{3}<0.</equation>综上所述，<equation>\max_{1\leq k\leq 4}\left\{I_{k}\right\}=I_{1}</equation>应选A.

---


### 函数、极限、连续


