#### 无穷小量的比较

**2020年第1题 | 选择题 | 4分 | 答案: D**

1. 当<equation>x \to 0^{+}</equation>时，下列无穷小量中最高阶的是（    )

A.<equation>\int_{0}^{x} \left( \mathrm{e}^{t^{2}}-1 \right) \mathrm{d} t</equation>B.<equation>\int_{0}^{x} \ln(1+\sqrt{t^{3}}) \mathrm{d} t</equation>C.<equation>\int_{0}^{\sin x} \sin t^{2} \mathrm{d} t</equation>D.<equation>\int_{0}^{1-\cos x} \sqrt{\sin^{3} t} \mathrm{d} t</equation>

答案: D

**解析:**解 由于求一次导，无穷小量的阶数降低1，且选项A、B的积分上、下限相同，故比较这两项的无穷小量的阶的大小，可以转化为比较它们的被积函数的阶。又因为<equation>t\to 0^{+}</equation>时，<equation>\mathrm{e}^{t^{2}}-1\sim t^{2},</equation><equation>\ln(1+\sqrt{t^{3}})\sim t^{\frac{3}{2}}</equation>，所以<equation>\int_{0}^{x}\left(\mathrm{e}^{t^{2}}-1\right)\mathrm{d}t</equation>与<equation>x^{3}</equation>同阶，比<equation>\int_{0}^{x}\ln(1+\sqrt{t^{3}})\mathrm{d}t</equation>高阶.

比较<equation>\int_{0}^{\sin x}\sin t^{2}\mathrm{d}t</equation>与<equation>x^{3}</equation>的阶.<equation>\begin{aligned} \lim _ {x \rightarrow 0 ^ {+}} \frac {\int_ {0} ^ {\sin x} \sin t ^ {2} \mathrm {d} t}{x ^ {3}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sin (\sin x) ^ {2} \cdot \cos x}{3 x ^ {2}} &= \frac {1}{3} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sin (\sin x) ^ {2}}{x ^ {2}} \xlongequal {\text {s i n} u \sim u} \frac {1}{3} \lim _ {x \rightarrow 0 ^ {+}} \frac {(\sin x) ^ {2}}{x ^ {2}} \\ &= \frac {1}{3} \lim _ {x \rightarrow 0 ^ {+}} \left(\frac {\sin x}{x}\right) ^ {2} \xlongequal {\sin x \sim x} \frac {1}{3}. \end{aligned}</equation>于是，<equation>\int_{0}^{\sin x}\sin t^{2}\mathrm{d}t</equation>也与<equation>x^{3}</equation>同阶.

比较<equation>\int_{0}^{1-\cos x}\sqrt{\sin^{3}t}\mathrm{d}t</equation>与<equation>x^{3}</equation>的阶.<equation>\begin{aligned} \lim _ {x \rightarrow 0 ^ {+}} \frac {\int_ {0} ^ {1 - \cos x} \sqrt {\sin^ {3} t} \mathrm {d} t}{x ^ {3}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sqrt {\sin^ {3} (1 - \cos x)} \sin x}{3 x ^ {2}} \xlongequal {\text {s i n} x \sim x} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sin^ {\frac {3}{2}} (1 - \cos x)}{3 x} \\ &= \lim _ {x \rightarrow 0 ^ {+}} \frac {\sin^ {\frac {3}{2}} (1 - \cos x)}{(1 - \cos x) ^ {\frac {3}{2}}} \cdot \frac {(1 - \cos x) ^ {\frac {3}{2}}}{3 x} \\ \frac {1 - \cos x \sim \frac {x ^ {2}}{2}}{} \lim _ {x \rightarrow 0 ^ {+}} \left[ \frac {\sin (1 - \cos x)}{1 - \cos x} \right] ^ {\frac {3}{2}} \cdot \frac {\left(\frac {x ^ {2}}{2}\right) ^ {\frac {3}{2}}}{3 x} \\ &= 1 \times 0 = 0. \end{aligned}</equation>因此，<equation>\int_0^{1 - \cos x}\sqrt{\sin^3t}\mathrm{d}t</equation>比<equation>x^{3}</equation>高阶，从而比选项A、B、C中的无穷小量均高阶.应选D.

---


