#### 方程根的存在性与个数

**2017年第18题 | 解答题 | 10分**

18. (本题满分10分)

设函数 f(x)在区间[0,1]上具有2阶导数，且<equation>f(1)>0,\lim_{x\rightarrow 0^{+}}\frac{f(x)}{x}<0.</equation>证明：

I. 方程 f(x)=0在区间（0,1）内至少存在一个实根；

II. 方程<equation>f(x)f^{\prime \prime}(x)+[f^{\prime}(x)]^{2}=0</equation>在区间（0,1）内至少存在两个不同实根.

**答案:**## （ I ）证明略；（ II ）证明略.

**解析:**证（I）由于<equation>\lim_{x\to 0^{+}}\frac{f(x)}{x}<0</equation>，故由函数极限的局部保号性可知，存在<equation>\theta >0</equation>，在（0，<equation>\theta</equation>）内，<equation>\frac{f(x)}{x}<0</equation>从而<equation>f(x) < 0</equation>.取<equation>0 < \delta < \theta</equation>，则<equation>f(\delta) < 0.</equation>又因为<equation>f ( 1 ) > 0</equation>，所以由连续函数的零点定理知，存在<equation>\xi \in (\delta,1)\subseteq(0,1)</equation>使得<equation>f (\xi)=0.</equation>因此，<equation>f ( x )=0</equation>在区间（0,1）内至少存在一个实根.

（Ⅱ）考虑<equation>F ( x )=f ( x ) f^{\prime} ( x )</equation>，则<equation>F ^ {\prime} (x) = f (x) f ^ {\prime \prime} (x) + \left[ f ^ {\prime} (x) \right] ^ {2}.</equation>第（Ⅱ）问等价于证明<equation>F^{\prime}(x)=0</equation>在区间（0,1）内至少存在两个不同实根.

若能找到三个点 a < b < c，使得<equation>F ( a )=F ( b )=F ( c )</equation>，则由罗尔定理知，存在<equation>\eta_{1}\in(a,b),</equation><equation>\eta_{2}\in(b,c)</equation>，满足<equation>F^{\prime}(\eta_{1})=0,F^{\prime}(\eta_{2})=0.</equation>由<equation>\lim_{x\rightarrow 0^{+}}\frac{f(x)}{x}<0</equation>知，分母趋于零，而极限仍存在，故<equation>f (0) \xlongequal {\text {连 续 性}} \lim _ {x \rightarrow 0 ^ {+}} f (x) = 0, \quad F (0) = f (0) f ^ {\prime} (0) = 0.</equation>由第（I）问的结论知，存在<equation>x_{1}\in(0,1)</equation>，满足<equation>f \left( x_{1} \right)=0</equation>，从而<equation>F \left( x_{1} \right)=f \left( x_{1} \right) f^{\prime} \left( x_{1} \right)=0.</equation>另一方面，由于<equation>f ( 0 )=0</equation><equation>f \left(x_{1}\right)=0</equation>，故由罗尔定理知，存在<equation>x_{2}\in\left(0,x_{1}\right)</equation>，使得<equation>f^{\prime}\left(x_{2}\right)=0</equation>，从而<equation>F \left(x_{2}\right)=f \left(x_{2}\right) f^{\prime}\left(x_{2}\right)=0.</equation>如图所示，<equation>0 < x_{2} < x_{1}, F(0) = F(x_{2}) = F(x_{1}) = 0.</equation>由罗尔定理知，存

在<equation>\eta_{1}\in (0,x_{2})</equation>，使得<equation>F^{\prime}(\eta_{1}) = 0</equation>；存在<equation>\eta_{2}\in (x_{2},x_{1})</equation>，使得<equation>F^{\prime}(\eta_{2}) = 0</equation>。命题得证.

---

**2011年第17题 | 解答题 | 10分**

17. (本题满分10分）

求方程<equation>k \arctan x-x=0</equation>不同实根的个数，其中 k为参数.

**答案:**## (17) 当<equation>k \leqslant 1</equation>时，原方程有1个实根；当<equation>k > 1</equation>时，原方程有3个不同的实根.

**解析:**解 令<equation>f ( x ) = k \arctan x - x</equation>，显然<equation>f ( 0 ) = 0</equation>且<equation>f ( x ) = - f (- x )</equation>即<equation>f ( x )</equation>为奇函数，故只需讨论<equation>x > 0</equation>时<equation>f ( x )</equation>零点的情况.又<equation>f^{\prime} ( x )=\frac{k}{1+x^{2}}-1=\frac{(k-1)-x^{2}}{1+x^{2}}</equation>我们对k分情况讨论如下若<equation>k \leqslant 1</equation>当<equation>x \in(0,+\infty)</equation>时，<equation>f^{\prime} ( x ) < 0</equation>从而<equation>f ( x )</equation>在<equation>[ 0,+\infty)</equation>上单调减少，又<equation>f ( 0 ) = 0</equation>故<equation>f ( x )</equation>在<equation>( 0,+\infty)</equation>内没有零点，从而<equation>f ( x )</equation>在R上只有1个零点<equation>x=0.</equation>若<equation>k > 1</equation>，当<equation>x\in(0,\sqrt{k-1})</equation>时，<equation>f^{\prime}(x)>0</equation>，从而<equation>f(x)</equation>在<equation>[0,\sqrt{k-1}]</equation>上单调增加，又<equation>f(0)=0</equation>，故<equation>f(x)</equation>在<equation>(0,\sqrt{k-1}]</equation>上无零点；当<equation>x\in(\sqrt{k-1},+\infty)</equation>时，<equation>f^{\prime}(x)<0</equation>从而<equation>f(x)</equation>在<equation>[\sqrt{k-1},+\infty)</equation>上单调减少，又<equation>f(\sqrt{k-1})>f(0)</equation><equation>= 0</equation>，且<equation>\lim_{x\to +\infty}f(x) = -\infty</equation>，故由连续函数的零点定理及<equation>f(x)</equation>的单调性可知，<equation>f(x)</equation>在<equation>(\sqrt{k-1},+\infty)</equation>内恰好只有1个零点，记为a.

因此，<equation>f ( x )</equation>在<equation>( 0, + \infty)</equation>内只有1个零点a，再由对称性可知，<equation>f ( x )</equation>在<equation>(-\infty , 0)</equation>内也只有1个零点一a，从而<equation>f ( x )</equation>在R上有3个零点，分别为一a,0,a，如图所示.

综上所述，当<equation>k \leqslant 1</equation>时，原方程有1个实根；当<equation>k > 1</equation>时，原方程有3个不同的实根.

---


