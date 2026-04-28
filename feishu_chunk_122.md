#### 导数与微分的计算

**2022年第13题 | 填空题 | 5分**

13. 已知函数<equation>f(x)=\mathrm{e}^{\sin x}+\mathrm{e}^{-\sin x}</equation>, 则<equation>f^{\prime\prime\prime}(2\pi)=</equation>___

**解析:**由于<equation>f (- x) = \mathrm {e} ^ {\sin (- x)} + \mathrm {e} ^ {- \sin (- x)} = \mathrm {e} ^ {- \sin x} + \mathrm {e} ^ {\sin x} = f (x),</equation>故 f(x)是偶函数.从而<equation>f^{\prime}(x)</equation>是奇函数，<equation>f^{\prime\prime}(x)</equation>是偶函数，<equation>f^{\prime\prime\prime}(x)</equation>是奇函数.由奇函数的性质可知，<equation>f^{\prime\prime\prime}(0)=0.</equation>又由于<equation>\sin x</equation>是周期为<equation>2\pi</equation>的周期函数，故 f(x)也是周期为<equation>2\pi</equation>的周期函数.从而 f(x)的各阶导函数均是周期为<equation>2\pi</equation>的周期函数.

因此，<equation>f^{\prime \prime \prime}(2\pi)=f^{\prime \prime \prime}(0)=0.</equation>

---

**2021年第11题 | 填空题 | 5分**

**答案:**<equation>\frac {\sin e ^ {- 1}}{2 e}.</equation>

**解析:**根据链式法则，<equation>\frac{\mathrm{d} y}{\mathrm{d} x}=-\sin\mathrm{e}^{-\sqrt{x}}\cdot\mathrm{e}^{-\sqrt{x}}\cdot\left(-\frac{1}{2\sqrt{x}}\right).</equation>代入 x = 1 可得，<equation>\left.\frac{\mathrm{d} y}{\mathrm{d} x}\right|_{x=1}=\frac{1}{2}\cdot\mathrm{e}^{-1}\cdot\sin\mathrm{e}^{-1}=\frac{\sin\mathrm{e}^{-1}}{2\mathrm{e}}.</equation>

---

**2012年第2题 | 选择题 | 4分 | 答案: A**

2. 设函数<equation>f(x)=\mathrm{e}^{x}-1)\mathrm{e}^{2x}-2)\cdots \mathrm{e}^{nx}-n)</equation>，其中 n为正整数，则<equation>f^{\prime}(0)=</equation>(    )

A.<equation>(-1)^{n-1}(n-1)!</equation>B.<equation>(-1)^{n}(n-1)!</equation>C.<equation>(-1)^{n-1}n!</equation>D.<equation>(-1)^{n}n!</equation>

答案: A

**解析:**解（法一）由题设知，<equation>f ( x ) = \left(\mathrm{e}^{x} - 1\right)\left[\left(\mathrm{e}^{2 x} - 2\right)\dots\left(\mathrm{e}^{n x} - n\right)\right]</equation>，再由函数乘积的求导法则知，<equation>f ^ {\prime} (x) = \mathrm {e} ^ {x} \left[ \left(\mathrm {e} ^ {2 x} - 2\right) \dots \left(\mathrm {e} ^ {n x} - n\right) \right] + \left(\mathrm {e} ^ {x} - 1\right) \left[ \left(\mathrm {e} ^ {2 x} - 2\right) \dots \left(\mathrm {e} ^ {n x} - n\right) \right] ^ {\prime},</equation><equation>f ^ {\prime} (0) = (- 1) (- 2) \dots (1 - n) + 0 = (- 1) ^ {n - 1} (n - 1)!</equation>应选A.

（法二）由题设知，<equation>f(0)=0.</equation>根据导数定义有<equation>\begin{array}{l} f ^ {\prime} (0) = \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0} \frac {\left(\mathrm {e} ^ {x} - 1\right)\left(\mathrm {e} ^ {2 x} - 2\right) \cdots \left(\mathrm {e} ^ {n x} - n\right)}{x} \\ \underline {{\mathrm {e} ^ {x} - 1 \sim x}} \lim _ {x \rightarrow 0} \left(\mathrm {e} ^ {2 x} - 2\right) \dots \left(\mathrm {e} ^ {n x} - n\right) = (1 - 2) \dots (1 - n) = (- 1) ^ {n - 1} (n - 1)!. \\ \end{array}</equation>应选A.

（法三）特殊值法.

观察各选项，可知当<equation>n\geqslant 2</equation>时，每个选项的值都不同.取<equation>n = 2</equation>，则<equation>f (x) = \left(\mathrm {e} ^ {x} - 1\right) \left(\mathrm {e} ^ {2 x} - 2\right), f ^ {\prime} (x) = \mathrm {e} ^ {x} \left(\mathrm {e} ^ {2 x} - 2\right) + \left(\mathrm {e} ^ {x} - 1\right) 2 \mathrm {e} ^ {2 x}.</equation>于是<equation>f^{\prime}(0) = -1.</equation>将<equation>n=2</equation>代入各选项，只有选项A的结果等于-1.

因此，应选A.

---

**2012年第10题 | 填空题 | 4分**

10. 设函数<equation>f ( x )=\left\{\begin{array}{ll}\ln \sqrt{x},&x\geqslant 1,\\ 2 x-1,&x<1,\end{array}\right. y=f(f(x))</equation>，则<equation>\left.\frac{\mathrm{d} y}{\mathrm{d} x}\right|_{x=\mathrm{e}}=</equation>___

**解析:**解 由已知条件知<equation>f(\mathrm{e})=\ln \sqrt{\mathrm{e}}=\frac{1}{2}.</equation>由链式法则知，<equation>\begin{array}{l} \left. \frac {\mathrm {d} y}{\mathrm {d} x} \right| _ {x = \mathrm {e}} = f ^ {\prime} (f (x)) \cdot f ^ {\prime} (x) \Big | _ {x = \mathrm {e}} = f ^ {\prime} (f (\mathrm {e})) \cdot f ^ {\prime} (\mathrm {e}) = f ^ {\prime} \left(\frac {1}{2}\right) \cdot f ^ {\prime} (\mathrm {e}) \\ = \frac {\mathrm {d} (2 x - 1)}{\mathrm {d} x} \Big | _ {x = \frac {1}{2}} \cdot \frac {\mathrm {d} (\ln \sqrt {x})}{\mathrm {d} x} \Big | _ {x = \mathrm {e}} = 2 \times \frac {1}{2 \mathrm {e}} = \frac {1}{\mathrm {e}}. \\ \end{array}</equation>

---


