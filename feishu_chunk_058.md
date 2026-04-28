#### 求幂级数的收敛半径、收敛区间和收敛域

**2022年第14题 | 填空题 | 5分**

14. 已知级数<equation>\sum_{n=1}^{\infty} \frac{n!}{n^{n}} \mathrm{e}^{-nx}</equation>的收敛域为<equation>(a,+\infty)</equation>, 则 a= ___

**答案:**<equation>- 1.</equation>

**解析:**解（法一）令<equation>u_{n}=\frac{n!}{n^{n}} \mathrm{e}^{-n x}</equation>，则原级数为<equation>\sum_{n=1}^{\infty} u_{n}.</equation><equation>\lim_{n\to \infty}\left|\frac{u_{n+1}}{u_{n}}\right|=\lim_{n\to \infty}\frac{(n+1)!}{(n+1)^{n+1}}\cdot \frac{n^{n}}{n!}\mathrm{e}^{-x}=\mathrm{e}^{-x}\lim_{n\to \infty}\frac{n^{n}}{(n+1)^{n}}=\mathrm{e}^{-x}\lim_{n\to \infty}\frac{1}{\left(1+\frac{1}{n}\right)^{n}}=\mathrm{e}^{-1-x}.</equation>由比值审敛法可知，当<equation>\mathrm{e}^{-1-x}<1</equation>时，<equation>\sum_{n=1}^{\infty} u_{n}</equation>收敛，当<equation>\mathrm{e}^{-1-x}>1</equation>时，<equation>\sum_{n=1}^{\infty} u_{n}</equation>发散.由于指数函数单调增加，故<equation>\mathrm{e}^{-1-x}<1</equation>等价于<equation>-1-x<0</equation>即<equation>x>-1</equation>因此，当<equation>x>-1</equation>时，函数项级数<equation>\sum_{n=1}^{\infty}\frac{n!}{n^{n}} \mathrm{e}^{-nx}</equation>收敛，当<equation>x<-1</equation>时，函数项级数<equation>\sum_{n=1}^{\infty}\frac{n!}{n^{n}} \mathrm{e}^{-nx}</equation>发散.

当<equation>x = -1</equation>时，<equation>\mathrm{e}^{-1 - x} = 1.</equation>此时利用比值审敛法无法判定<equation>\sum_{n = 1}^{\infty} u_n</equation>的收敛性. 但是，将<equation>x = -1</equation>代回原级数可得原级数为<equation>\sum_{n = 1}^{\infty}\frac{n!}{n^n}\mathrm{e}^n.</equation>该级数的一般项极限不为0，从而发散（见注）.

因此，函数项级数<equation>\sum_{n = 1}^{\infty}\frac{n!}{n^n}\mathrm{e}^{-nx}</equation>的收敛域为<equation>(-1, +\infty)</equation>，<equation>a = -1.</equation>（法二）令<equation>t = \mathrm{e}^{-x}</equation>，则<equation>\sum_{n = 1}^{\infty}\frac{n!}{n^n}\mathrm{e}^{-nx} = \sum_{n = 1}^{\infty}\frac{n!}{n^n}t^n.</equation><equation>\lim _ {n \rightarrow \infty} \frac {(n + 1) !}{(n + 1) ^ {n + 1}} \cdot \frac {n ^ {n}}{n !} = \lim _ {n \rightarrow \infty} \frac {n ^ {n}}{(n + 1) ^ {n}} = \lim _ {n \rightarrow \infty} \frac {1}{\left(1 + \frac {1}{n}\right) ^ {n}} = \frac {1}{\mathrm {e}}.</equation>于是，<equation>\sum_{n = 1}^{\infty}\frac{n!}{n^n} t^n</equation>的收敛半径为e，收敛区间为<equation>(-\mathrm{e},\mathrm{e})</equation>解<equation>- \mathrm{e} < \mathrm{e}^{-x} < \mathrm{e}</equation>可得，<equation>x > - 1</equation>因此，当<equation>x > - 1</equation>时，函数项级数<equation>\sum_{n=1}^{\infty} \frac{n!}{n^{n}} \mathrm{e}^{-n x}</equation>收敛。并且，当<equation>x < - 1</equation>时，<equation>\mathrm{e}^{-x} > \mathrm{e}</equation>函数项级数<equation>\sum_{n=1}^{\infty} \frac{n!}{n^{n}} \mathrm{e}^{-n x}</equation>发散.

其余同法一.

---

**2020年第4题 | 选择题 | 4分 | 答案: A**

4. 设 R为幂级数<equation>\sum_{n=1}^{\infty} a_{n} x^{n}</equation>的收敛半径，r是实数，则（    )

A. 当<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>发散时，<equation>|r|\geqslant R</equation>B. 当<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>收敛时，<equation>|r|\leqslant R</equation>C. 当<equation>|r|\geqslant R</equation>时，<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>发散 D. 当<equation>|r|\leqslant R</equation>时，<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>收敛

答案: A

**解析:**解 由幂级数的收敛半径的定义可知，当<equation>| r | < R</equation>时，级数<equation>\sum_{n=1}^{\infty} a_{n} r^{n}</equation>绝对收敛.又因为<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>为<equation>\sum_{n=1}^{\infty} a_{n} r^{n}</equation>的偶数项子级数，所以此时由<equation>\sum_{n=1}^{\infty} a_{n} r^{n}</equation>收敛可得<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>收敛.

若<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>发散，则<equation>\sum_{n=1}^{\infty} a_{n} r^{n}</equation>不可能绝对收敛.因此，<equation>| r | \geqslant R</equation>或者，由<equation>| r | < R \Rightarrow \sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>收敛的逆否命题为<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>发散<equation>\Rightarrow | r | \geqslant R</equation>可知，<equation>| r | \geqslant R</equation>应选A.

下面说明其余选项均不正确.

选项B、C：取<equation>a_{n}=\left\{ \begin{array}{ll}1,&n=2k-1,\\ 0,&n=2k, \end{array} \right. k=1,2,3,\dots</equation>，则<equation>\sum_{n=1}^{\infty}a_{n}x^{n}=\sum_{n=1}^{\infty}x^{2n-1}.</equation>该级数为缺项幂级数，易求得其收敛半径为1. 对任何实数<equation>r,\sum_{n=1}^{\infty}a_{2n}r^{2n}</equation>均收敛.因此，选项C不正确.任取<equation>|r| > 1</equation>即可否定选项B.

选项D：当<equation>|r| < R</equation>时，级数<equation>\sum_{n=1}^{\infty} a_{n} r^{n}</equation>绝对收敛.于是由<equation>\sum_{n=1}^{\infty} a_{n} r^{n}</equation>收敛可得<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>收敛.但是，当<equation>|r|=R</equation>时，<equation>\sum_{n=1}^{\infty} a_{n} r^{n}</equation>可能收敛，也可能发散.此时，无法确定<equation>\sum_{n=1}^{\infty} a_{2n} r^{2n}</equation>的收敛性.

例如：取<equation>a_{n}=1,n=1,2,3,\dots</equation>，则<equation>\sum_{n=1}^{\infty}a_{n}x^{n}=\sum_{n=1}^{\infty}x^{n}</equation>.该幂级数的收敛半径为1.取<equation>r=1</equation>，则<equation>\sum_{n=1}^{\infty}1^{2n}</equation>发散.<equation>|r|=R</equation>时，<equation>\sum_{n=1}^{\infty}a_{2n}r^{2n}</equation>收敛的例子同选项B、C.

---

**2015年第3题 | 选择题 | 4分 | 答案: B**

3. 若级数<equation>\sum_{n=1}^{\infty} a_{n}</equation>条件收敛，则<equation>x=\sqrt{3}</equation>与 x=3依次为幂级数<equation>\sum_{n=1}^{\infty} n a_{n} ( x-1 )^{n}</equation>的（    ）

A. 收敛点，收敛点 B. 收敛点，发散点 C. 发散点，收敛点 D. 发散点，发散点

答案: B

**解析:**解（法一）由<equation>\sum_{n=1}^{\infty} a_{n}</equation>条件收敛知，<equation>\sum_{n=1}^{\infty} a_{n}</equation>收敛，<equation>\sum_{n=1}^{\infty} |a_{n}|</equation>发散.于是幂级数<equation>\sum_{n=1}^{\infty} a_{n} x^{n}</equation>在<equation>x=1</equation>处收敛，从而由阿贝尔定理知，<equation>\sum_{n=1}^{\infty} a_{n} x^{n}</equation>的收敛半径R满足<equation>R\geqslant 1</equation>假设<equation>R > 1</equation>，则由阿贝尔定理知，<equation>\sum_{n=1}^{\infty} |a_{n}|</equation>收敛，矛盾，故假设不成立，从而<equation>R=1.</equation>幂级数<equation>\sum_{n=1}^{\infty} a_{n}(x-1)^{n}</equation>与<equation>\sum_{n=1}^{\infty} a_{n}x^{n}</equation>的收敛半径相同，均为1.又逐项求导不改变收敛半径，故<equation>\sum_{n=1}^{\infty} n a_{n}(x-1)^{n-1}</equation>的收敛半径为1，从而<equation>\sum_{n=1}^{\infty} n a_{n}(x-1)^{n}</equation>的收敛半径为1.因此<equation>\sum_{n=1}^{\infty} n a_{n}(x-1)^{n}</equation>当<equation>|x-1| < 1</equation>即<equation>x\in(0,2)</equation>时收敛；当<equation>|x-1| > 1</equation>即<equation>x\in(-\infty ,0)\cup(2,+\infty)</equation>时发散.由于<equation>0 < \sqrt{3} < 2 < 3</equation>故<equation>\sum_{n=1}^{\infty} n a_{n}(x-1)^{n}</equation>在<equation>x=\sqrt{3}</equation>处收敛，在<equation>x=3</equation>处发散，从而选B.

（法二）特殊值法.

令<equation>a_{n}=\frac{(-1)^{n}}{n}</equation>满足<equation>\sum_{n=1}^{\infty} a_{n}</equation>条件收敛.又<equation>\sum_{n=1}^{\infty} n a_{n}(x-1)^{n}=\sum_{n=1}^{\infty}(-1)^{n}(x-1)^{n}</equation>的收敛域为 (0,2)，故该幂级数在<equation>x=\sqrt{3}</equation>处收敛，在<equation>x=3</equation>处发散，从而选B.

---

**2011年第2题 | 选择题 | 4分 | 答案: C**

2. 设数列<equation>\{a_{n}\}</equation>单调减少，<equation>\lim_{n\to \infty}a_{n}=0,S_{n}=\sum_{k=1}^{n}a_{k}</equation>（ n=1，2，<equation>\cdots</equation>）无界，则幂级数<equation>\sum_{n=1}^{\infty}a_{n}(x-1)^{n}</equation>的收敛域为（    ）

A. (-1,1] B. [-1,1) C. [0,2) D. (0,2]

答案: C

**解析:**解（法一）由于数列<equation>\left\{a_{n}\right\}</equation>单调减少且<equation>\lim_{n\to \infty}a_{n}=0</equation>，故<equation>a_{n}>0,n=1,2,\dots</equation>由莱布尼茨定理知，<equation>\sum_{n=1}^{\infty}a_{n}(-1)^{n}</equation>收敛，即<equation>\sum_{n=1}^{\infty}a_{n}x^{n}</equation>在<equation>x=-1</equation>处收敛，由阿贝尔定理知，<equation>\sum_{n=1}^{\infty}a_{n}x^{n}</equation>的收敛半径<equation>R\geqslant 1</equation>又<equation>S_{n}</equation>无界，故<equation>\sum_{n=1}^{\infty}a_{n}</equation>发散，即<equation>\sum_{n=1}^{\infty}a_{n}x^{n}</equation>在<equation>x=1</equation>处发散，由阿贝尔定理知，<equation>R\leqslant 1</equation>，于是<equation>R=1.</equation>因此<equation>\sum_{n=1}^{\infty} a_{n} x^{n}</equation>的收敛域为[-1,1)，从而<equation>\sum_{n=1}^{\infty} a_{n} (x-1)^{n}</equation>的收敛点满足<equation>- 1\leqslant x-1<1</equation>即收敛域为[0,2).应选C.


幂级数<equation>\sum_{n=1}^{\infty} a_{n} ( x-1 )^{n}</equation>的收敛域是以 x=1为中心，故排除选项A、B.又当 x=2时，<equation>\sum_{n=1}^{\infty} a_{n} ( x-1 )^{n}</equation><equation>= \sum_{n=1}^{\infty} a_{n}</equation>发散，故 x=2不在其收敛域中，从而排除选项D.应选C.

---


### 多元函数积分学


