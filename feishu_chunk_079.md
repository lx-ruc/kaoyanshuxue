#### 变限积分

**2024年第1题 | 选择题 | 5分 | 答案: C**
1. 已知函数<equation>f ( x )=\int_{0}^{x} \mathrm{e}^{\cos t} \mathrm{d} t,g ( x )=\int_{0}^{\sin x} \mathrm{e}^{t^{2}} \mathrm{d} t</equation>，则（    )

A. f(x)是奇函数，g(x)是偶函数 B. f(x)是偶函数，g(x)是奇函数

C. f(x)与 g(x)均为奇函数 D. f(x)与 g(x)均为周期函数
答案: C
**解析: **解 由于<equation>\mathrm{e}^{\cos t}</equation>是偶函数，且<equation>f(0)=0</equation>，故由分析中的结论可得<equation>f(x)=\int_{0}^{x}\mathrm{e}^{\cos t}\mathrm{d}t</equation>是奇函数.同理，<equation>h(x)=\int_{0}^{x}\mathrm{e}^{t^{2}}\mathrm{d}t</equation>也是奇函数.

注意到<equation>g ( x )=h (\sin x)</equation>，故<equation>g (- x) = h (\sin (- x)) = h (- \sin x) = - h (\sin x) = - g (x).</equation>于是，<equation>g ( x )</equation>也是奇函数.

因此，应选C.

下面说明选项 D 不正确.

由于<equation>\sin x</equation>是周期为<equation>2\pi</equation>的周期函数，故<equation>g (x + 2 \pi) = \int_ {0} ^ {\sin (x + 2 \pi)} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = \int_ {0} ^ {\sin x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = g (x).</equation>于是，<equation>g ( x )</equation>也是周期为<equation>2 \pi</equation>的周期函数.但是，由于<equation>f^{\prime}(x)=\mathrm{e}^{\cos x}>0</equation>，故f(x）单调增加，从而f(x)不可能为周期函数.

也可以直接验证<equation>f(-x)=-f(x), g(-x)=-g(x)</equation>，从而得到它们均为奇函数.<equation>f (- x) = \int_ {0} ^ {- x} \mathrm {e} ^ {\cos t} \mathrm {d} t \underline {{= u = - t}} - \int_ {0} ^ {x} \mathrm {e} ^ {\cos (- u)} \mathrm {d} u = - \int_ {0} ^ {x} \mathrm {e} ^ {\cos u} \mathrm {d} u = - f (x),</equation><equation>g (- x) = \int_ {0} ^ {\sin (- x)} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = \int_ {0} ^ {- \sin x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t \xlongequal {u = - t} - \int_ {0} ^ {\sin x} \mathrm {e} ^ {(- u) ^ {2}} \mathrm {d} u = - \int_ {0} ^ {\sin x} \mathrm {e} ^ {u ^ {2}} \mathrm {d} u = - g (x).</equation>

---

**2009年第3题 | 选择题 | 4分 | 答案: D**
3. 设函数 y=f(x)在区间[-1,3]上的图形如图所示，则函数<equation>F ( x )=\int_{0}^{x} f ( t ) \mathrm{d} t</equation>的图形为（    ）

A.

B.

C.

D.
答案: D
**解析: **解（法一）我们可以从<equation>f(x)</equation>出发具体分析<equation>F(x)</equation>的性质.

因为<equation>f ( x )</equation>分段连续，所以由变上限积分函数的性质可知，在<equation>[-1,0)</equation>，（0，2），（2，3]上，均有<equation>F^{\prime}(x)=f(x).</equation><equation>\textcircled{1}</equation>由于 f(x)在[-1,3]上有界且只有两个间断点，故 f(x)可积.又因为<equation>F(x)=\int_{0}^{x} f(t)\mathrm{d}t</equation>所以 F(x)连续.<equation>\textcircled{2}</equation>在[-1,0）上，<equation>f ( x ) > 0</equation>，故 F(x)单调增加；在（0，1）上，<equation>f ( x ) < 0</equation>，故 F(x)单调减少；在（1，2）上，<equation>f ( x ) > 0</equation>，故 F(x)单调增加；在（2，3]上，<equation>f ( x ) = 0</equation>，故 F(x)为常函数.<equation>\textcircled{3} F ( 0 )=\int_{0}^{0} f ( t ) \mathrm{d} t=0.</equation>在<equation>[-1,1]</equation>上，<equation>F ( x )</equation>均小于等于零.<equation>\textcircled{4}</equation><equation>f(1) = 0, x = 1</equation>为<equation>F(x)</equation>的驻点及极小值点.

同时满足以上要求的图形只有选项D. 应选D.

（法二）通过图形考察<equation>f(x)</equation>在<equation>[-1,0)</equation>上的性质，可知当<equation>x\in[-1,0)</equation>时，<equation>f(x)\equiv 1</equation>，故<equation>F (- 1) = \int_ {0} ^ {- 1} 1 \mathrm {d} x = - 1, \quad F (0) = \int_ {0} ^ {0} 1 \mathrm {d} x = 0,</equation>从而可排除选项A和选项C.

又由于 f(x)在[-1，3]上有界且只有两个间断点，f(x)在[-1，3]上可积，而 F(x) =<equation>\int_{0}^{x} f(t)\mathrm{d}t</equation>，故 F(x)必连续，从而可以排除选项B.

综上所述，应选D.

---


