当<equation>\alpha\neq0</equation>时，<equation>f (\alpha) = \int_ {2} ^ {+ \infty} \frac {1}{x (\ln x) ^ {\alpha + 1}} \mathrm {d} x = \int_ {2} ^ {+ \infty} (\ln x) ^ {- \alpha - 1} \mathrm {d} (\ln x) = - \frac {1}{\alpha} (\ln x) ^ {- \alpha} \Big | _ {2} ^ {+ \infty}.</equation>当<equation>\alpha < 0</equation>时，<equation>\lim_{x\to +\infty} (\ln x)^{-\alpha}=+\infty</equation><equation>f(\alpha)</equation>无定义；当<equation>\alpha >0</equation>时，<equation>f (\alpha) = - \frac {1}{\alpha} \left(\ln x\right) ^ {- \alpha} \Bigg | _ {2} ^ {+ \infty} = - \frac {1}{\alpha} \left[ 0 - \left(\ln 2\right) ^ {- \alpha} \right] = \frac {\left(\ln 2\right) ^ {- \alpha}}{\alpha}.</equation>因此，<equation>f(\alpha)</equation>的定义域为（0，<equation>+\infty</equation>），<equation>f(\alpha) = \frac{(\ln 2)^{-\alpha}}{\alpha}.</equation>计算<equation>f^{\prime}(\alpha).</equation><equation>f ^ {\prime} (\alpha) = \frac {- \alpha (\ln 2) ^ {- \alpha} \ln (\ln 2) - (\ln 2) ^ {- \alpha}}{\alpha^ {2}} = \frac {- (\ln 2) ^ {- \alpha} [ \alpha \ln (\ln 2) + 1 ]}{\alpha^ {2}}.</equation><equation>f^{\prime}(\alpha)=0</equation>当且仅当<equation>\alpha=-\frac{1}{\ln(\ln 2)}。</equation>当<equation>0 < \alpha < - \frac{1}{\ln(\ln 2)}</equation>时，<equation>f^{\prime}(\alpha)<0,f(\alpha)</equation>单调减少；当<equation>\alpha > - \frac{1}{\ln(\ln 2)}</equation>时，<equation>f^{\prime}(\alpha)>0,f(\alpha)</equation>单调增加.因此，<equation>\alpha_{0}=- \frac{1}{\ln(\ln 2)}</equation>为 f（<equation>\alpha</equation>）的最小值点，应选A.

---

**2022年第5题 | 选择题 | 5分 | 答案: A**
5. 设 p为常数，若反常积分<equation>\int_{0}^{1}\frac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x</equation>收敛，则 p的取值范围是（    )

A. (-1,1) B. (-1,2) C.<equation>(-\infty,1)</equation>D.<equation>(-\infty,2)</equation>
答案: A
**解析: **由于 x=0和 x=1均为可能的瑕点，故将积分拆成两部分.<equation>\int_ {0} ^ {1} \frac {\ln x}{x ^ {p} (1 - x) ^ {1 - p}} \mathrm {d} x = \int_ {0} ^ {\frac {1}{2}} \frac {\ln x}{x ^ {p} (1 - x) ^ {1 - p}} \mathrm {d} x + \int_ {\frac {1}{2}} ^ {1} \frac {\ln x}{x ^ {p} (1 - x) ^ {1 - p}} \mathrm {d} x.</equation>先考虑<equation>\int_{0}^{\frac{1}{2}}\frac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x.</equation>当 p < 0时，<equation>\lim_{x\rightarrow 0^{+}}\frac{\ln x}{x^{p}(1-x)^{1-p}}=0,x=0</equation>不是瑕点，<equation>\int_{0}^{\frac{1}{2}}\frac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x</equation>为常义积分当 0≤p < 1时，取<equation>\delta >0</equation>使得0 < p+<equation>\delta < 1</equation>从而<equation>\lim _ {x \rightarrow 0 ^ {+}} x ^ {p + \delta} \cdot \frac {\ln x}{x ^ {p} (1 - x) ^ {1 - p}} = \lim _ {x \rightarrow 0 ^ {+}} x ^ {\delta} \ln x = \lim _ {x \rightarrow 0 ^ {+}} \frac {\ln x}{x ^ {- \delta}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {1}{- \delta x ^ {- \delta}} = 0.</equation>由无界函数的极限审敛法可知，<equation>\int_{0}^{\frac{1}{2}}\frac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x</equation>收敛.

当 p=1时，<equation>\int_ {0} ^ {\frac {1}{2}} \frac {\ln x}{x} \mathrm {d} x = \int_ {0} ^ {\frac {1}{2}} \ln x \mathrm {d} (\ln x) = \frac {\left(\ln x\right) ^ {2}}{2} \Bigg | _ {0} ^ {\frac {1}{2}} = - \infty .</equation>于是，当<equation>p \geqslant 1</equation>时，<equation>\int_{0}^{\frac{1}{2}}\frac{\ln x}{x^{p}\left(1-x\right)^{1-p}}\mathrm{d}x</equation>发散.

因此，当<equation>p < 1</equation>时，<equation>\int_{0}^{\frac{1}{2}}\frac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x</equation>收敛，当<equation>p\geqslant 1</equation>时，<equation>\int_{0}^{\frac{1}{2}}\frac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x</equation>发散.

再考虑<equation>\int_{\frac{1}{2}}^{1} \frac{\ln x}{x^{p}(1-x)^{1-p}} \mathrm{d} x.</equation><equation>\lim _ {x \rightarrow 1 ^ {-}} \frac {\ln x}{x ^ {p} (1 - x) ^ {1 - p}} = \lim _ {x \rightarrow 1 ^ {-}} \frac {\ln (1 + x - 1)}{x ^ {p} (1 - x) ^ {1 - p}} = \lim _ {x \rightarrow 1 ^ {-}} \frac {- (1 - x)}{(1 - x) ^ {1 - p}} = - \lim _ {x \rightarrow 1 ^ {-}} (1 - x) ^ {p}.</equation>于是，当 p≥0时，x=1不是瑕点，<equation>\int_{\frac{1}{2}}^{1} \frac{\ln x}{x^{p}(1-x)^{1-p}} \mathrm{d} x</equation>为常义积分.

当 0 < - p < 1，即<equation>- 1 < p < 0</equation>时，<equation>\lim _ {x \rightarrow 1 ^ {-}} (1 - x) ^ {- p} \cdot \frac {- \ln x}{x ^ {p} (1 - x) ^ {1 - p}} = \lim _ {x \rightarrow 1 ^ {-}} (1 - x) ^ {- p} \cdot (1 - x) ^ {p} = 1.</equation>由无界函数的极限审敛法可知，<equation>\int_{\frac{1}{2}}^{1} \frac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x</equation>收敛.

当<equation>- p \geqslant 1</equation>，即<equation>p \leqslant - 1</equation>时，同理可得<equation>\lim_{x\to 1^{-}}(1-x)^{-p}\cdot \frac{-\ln x}{x^{p}(1-x)^{1-p}}=1</equation>从而由无界函数的极限审敛法可知，<equation>\int_{\frac{1}{2}}^{1}\frac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x</equation>发散.

因此，当 p > -1时，<equation>\int_{\frac{1}{2}}^{1} \frac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x</equation>收敛，当 p≤-1时，<equation>\int_{\frac{1}{2}}^{1} \frac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x</equation>发散.

综上所述，<equation>\int_{0}^{1}\frac{\ln x}{x^{p}(1-x)^{1-p}}\mathrm{d}x</equation>收敛当且仅当 p<equation>\in(-\infty,1)\cap(-1,+\infty)=(-1,1).</equation>应选A.

---

**2021年第11题 | 填空题 | 5分**
<equation>1 1. \int_ {- \infty} ^ {+ \infty} | x | 3 ^ {- x ^ {2}} \mathrm {d} x = \underline {{}}</equation>
**解析: **由于<equation>| x | = \left\{ \begin{array}{ll} x, & x\geqslant 0, \\ - x, & x < 0, \end{array} \right.</equation>故<equation>\begin{aligned} \int_ {- \infty} ^ {+ \infty} | x | 3 ^ {- x ^ {2}} \mathrm {d} x &= \int_ {- \infty} ^ {0} (- x) \cdot 3 ^ {- x ^ {2}} \mathrm {d} x + \int_ {0} ^ {+ \infty} x \cdot 3 ^ {- x ^ {2}} \mathrm {d} x \xlongequal {t = - x} \int_ {+ \infty} ^ {0} t \cdot 3 ^ {- t ^ {2}} \mathrm {d} (- t) + \int_ {0} ^ {+ \infty} x \cdot 3 ^ {- x ^ {2}} \mathrm {d} x \\ &= 2 \int_ {0} ^ {+ \infty} x \cdot 3 ^ {- x ^ {2}} \mathrm {d} x = \int_ {0} ^ {+ \infty} 3 ^ {- x ^ {2}} \mathrm {d} \left(x ^ {2}\right) = \frac {- 3 ^ {- x ^ {2}}}{\ln 3} \Big | _ {0} ^ {+ \infty} = 0 - \left(- \frac {1}{\ln 3}\right) = \frac {1}{\ln 3}. \end{aligned}</equation>

---

**2019年第3题 | 选择题 | 4分 | 答案: D**
3. 下列反常积分发散的是（    ）

A.<equation>\int_{0}^{+\infty} x \mathrm{e}^{-x} \mathrm{d} x</equation>B.<equation>\int_{0}^{+\infty} x \mathrm{e}^{-x^{2}} \mathrm{d} x</equation>C.<equation>\int_{0}^{+\infty} \frac{\arctan x}{1+x^{2}} \mathrm{d} x</equation>D.<equation>\int_{0}^{+\infty} \frac{x}{1+x^{2}} \mathrm{d} x</equation>
答案: D
**解析: **由于各选项中的积分都不太复杂，故可先积分，再讨论极限.<equation>\begin{aligned} \int_ {0} ^ {+ \infty} x \mathrm {e} ^ {- x} \mathrm {d} x &= - \int_ {0} ^ {+ \infty} x \mathrm {d} \left(\mathrm {e} ^ {- x}\right) = - \left(x \mathrm {e} ^ {- x} \Big | _ {0} ^ {+ \infty} - \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- x} \mathrm {d} x\right) \\ &= \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- x} \mathrm {d} x = - \mathrm {e} ^ {- x} \Big | _ {0} ^ {+ \infty} = - (0 - 1) = 1. \end{aligned}</equation><equation>\begin{aligned} \int_ {0} ^ {+ \infty} x \mathrm {e} ^ {- x ^ {2}} \mathrm {d} x &= \frac {1}{2} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- x ^ {2}} \mathrm {d} \left(x ^ {2}\right) = - \frac {1}{2} \mathrm {e} ^ {- x ^ {2}} \Bigg | _ {0} ^ {+ \infty} = - \frac {1}{2} \times (0 - 1) = \frac {1}{2}. \\ \int_ {0} ^ {+ \infty} \frac {\arctan x}{1 + x ^ {2}} \mathrm {d} x &= \int_ {0} ^ {+ \infty} \arctan x \mathrm {d} (\arctan x) = \frac {\left(\arctan x\right) ^ {2}}{2} \Bigg | _ {0} ^ {+ \infty} \\ \frac {\lim _ {x \rightarrow + \infty} \arctan x = \frac {\pi}{2}}{\frac {1}{2}} \frac {1}{2} \left[\left(\frac {\pi}{2}\right) ^ {2} - 0 \right] &= \frac {\pi^ {2}}{8}. \end{aligned}</equation><equation>\int_ {0} ^ {+ \infty} \frac {x}{1 + x ^ {2}} \mathrm {d} x = \frac {1}{2} \int_ {0} ^ {+ \infty} \frac {\mathrm {d} \left(1 + x ^ {2}\right)}{1 + x ^ {2}} = \frac {1}{2} \ln \left(1 + x ^ {2}\right) \Big | _ {0} ^ {+ \infty} = + \infty .</equation>综上所述，应选D.

---

**2018年第11题 | 填空题 | 4分**
11.
**答案: **##<equation>\frac{1}{2} \ln 2.</equation>
**解析: **<equation>\begin{array}{l} = \frac {1}{2} \ln \left| \frac {x - 3}{x - 1} \right| \Big | _ {5} ^ {+ \infty} \stackrel {*} {=} \frac {1}{2} \left(0 - \ln \frac {5 - 3}{5 - 1}\right) = \frac {1}{2} \ln 2. \\ \end{array}</equation>

---

**2017年第11题 | 填空题 | 4分**
11.<equation>\int_ {0} ^ {+ \infty} \frac {\ln (1 + x)}{(1 + x) ^ {2}} \mathrm {d} x = \underline {{}}</equation>
**解析: **采用分部积分法.<equation>\begin{aligned} \int_ {0} ^ {+ \infty} \frac {\ln (1 + x)}{(1 + x) ^ {2}} \mathrm {d} x &= - \int_ {0} ^ {+ \infty} \ln (1 + x) \mathrm {d} \left(\frac {1}{1 + x}\right) = - \left[ \frac {\ln (1 + x)}{1 + x} \Big | _ {0} ^ {+ \infty} - \int_ {0} ^ {+ \infty} \frac {1}{(1 + x) ^ {2}} \mathrm {d} x \right] \\ &= \int_ {0} ^ {+ \infty} \frac {1}{(1 + x) ^ {2}} \mathrm {d} x = - \frac {1}{1 + x} \Big | _ {0} ^ {+ \infty} = 0 - (- 1) = 1. \end{aligned}</equation>

---

**2016年第3题 | 选择题 | 4分 | 答案: B**
3. 反常积分<equation>\int_{-\infty}^{0}\frac{1}{x^{2}}\mathrm{e}^{\frac{1}{x}}\mathrm{d}x</equation>和<equation>\int_{0}^{+\infty}\frac{1}{x^{2}}\mathrm{e}^{\frac{1}{x}}\mathrm{d}x</equation>的敛散性分别为（    )

A. 收敛，收敛 B. 收敛，发散 C. 发散，收敛 D. 发散，发散
答案: B
**解析: **解分别计算<equation>\int_{- \infty}^{0} \frac{1}{x^{2}} \mathrm{e}^{\frac{1}{x}} \mathrm{d} x</equation>和<equation>\int_{0}^{+\infty} \frac{1}{x^{2}} \mathrm{e}^{\frac{1}{x}} \mathrm{d} x.</equation>设 R < c < 0.<equation>\begin{aligned} \int_ {- \infty} ^ {0} \frac {1}{x ^ {2}} \mathrm {e} ^ {\frac {1}{x}} \mathrm {d} x &= \lim _ {\substack {c \rightarrow 0 ^ {-} \\ R \rightarrow - \infty}} \int_ {R} ^ {c} \frac {1}{x ^ {2}} \mathrm {e} ^ {\frac {1}{x}} \mathrm {d} x = \lim _ {\substack {c \rightarrow 0 ^ {-} \\ R \rightarrow - \infty}} \int_ {R} ^ {c} - \mathrm {e} ^ {\frac {1}{x}} \mathrm {d} \left(\frac {1}{x}\right) = \lim _ {\substack {c \rightarrow 0 ^ {-} \\ R \rightarrow - \infty}} \left(- \mathrm {e} ^ {\frac {1}{x}} \Bigg | _ {R} ^ {c}\right) \\ &= \lim _ {x \rightarrow 0 ^ {-}} \left(- \mathrm {e} ^ {\frac {1}{x}}\right) - \lim _ {x \rightarrow - \infty} \left(- \mathrm {e} ^ {\frac {1}{x}}\right) = 0 - (- 1) = 1. \end{aligned}</equation>设 0 < c < R.<equation>\begin{aligned} \int_ {0} ^ {+ \infty} \frac {1}{x ^ {2}} \mathrm {e} ^ {\frac {1}{x}} \mathrm {d} x &= \lim _ {\substack {c \rightarrow 0 ^ {+} \\ R \rightarrow + \infty}} \int_ {c} ^ {R} \frac {1}{x ^ {2}} \mathrm {e} ^ {\frac {1}{x}} \mathrm {d} x = \lim _ {\substack {c \rightarrow 0 ^ {+} \\ R \rightarrow + \infty}} \int_ {c} ^ {R} - \mathrm {e} ^ {\frac {1}{x}} \mathrm {d} \left(\frac {1}{x}\right) = \lim _ {\substack {c \rightarrow 0 ^ {+} \\ R \rightarrow + \infty}} \left(- \mathrm {e} ^ {\frac {1}{x}} \Bigg | _ {c} ^ {R}\right) \\ &= \lim _ {x \rightarrow + \infty} \left(- \mathrm {e} ^ {\frac {1}{x}}\right) - \lim _ {x \rightarrow 0 ^ {+}} \left(- \mathrm {e} ^ {\frac {1}{x}}\right). \end{aligned}</equation>由于<equation>\lim_{x\rightarrow +\infty}(-\mathrm{e}^{\frac{1}{x}})=-1</equation>，而<equation>\lim_{x\rightarrow 0^{+}}(-\mathrm{e}^{\frac{1}{x}})=-\infty</equation>，故<equation>\int_{0}^{+\infty}\frac{1}{x^{2}}\mathrm{e}^{\frac{1}{x}}\mathrm{d}x</equation>发散.

因此，应选B.

---

**2015年第1题 | 选择题 | 4分 | 答案: D**
1. 下列反常积分中收敛的是（    ）

A.<equation>\int_{2}^{+\infty}\frac{1}{\sqrt{x}} \mathrm{d} x</equation>B.<equation>\int_{2}^{+\infty}\frac{\ln x}{x} \mathrm{d} x</equation>C.<equation>\int_{2}^{+\infty}\frac{1}{x \ln x} \mathrm{d} x</equation>D.<equation>\int_{2}^{+\infty}\frac{x}{\mathrm{e}^{x}} \mathrm{d} x</equation>
答案: D
**解析: **由于各选项中的积分都不太复杂，故可先积分，再讨论极限.<equation>\int_ {2} ^ {+ \infty} \frac {1}{\sqrt {x}} \mathrm {d} x = 2 \sqrt {x} \Big | _ {2} ^ {+ \infty} = + \infty ,</equation><equation>\left. \int_ {2} ^ {+ \infty} \frac {\ln x}{x} \mathrm {d} x = \frac {\left(\ln x\right) ^ {2}}{2} \right| _ {2} ^ {+ \infty} = + \infty ,</equation><equation>\left. \int_ {2} ^ {+ \infty} \frac {1}{x \ln x} \mathrm {d} x = \ln (\ln x) \right| _ {2} ^ {+ \infty} = + \infty ,</equation><equation>\left. \int_ {2} ^ {+ \infty} \frac {x}{\mathrm {e} ^ {x}} \mathrm {d} x = - \int_ {2} ^ {+ \infty} x \mathrm {d} \left(\mathrm {e} ^ {- x}\right) = - (x + 1) \mathrm {e} ^ {- x} \right| _ {2} ^ {+ \infty} = \frac {3}{\mathrm {e} ^ {2}}.</equation>综上可知，应选D.

---

**2014年第9题 | 填空题 | 4分**
（无内容）
**解析: **对被积函数的分母配方.<equation>\begin{aligned} \int_ {- \infty} ^ {1} \frac {1}{x ^ {2} + 2 x + 5} \mathrm {d} x &= \int_ {- \infty} ^ {1} \frac {1}{(x + 1) ^ {2} + 4} \mathrm {d} x = \frac {1}{2} \int_ {- \infty} ^ {1} \frac {1}{\left(\frac {x + 1}{2}\right) ^ {2} + 1} \mathrm {d} \left(\frac {x + 1}{2}\right) \\ &= \frac {1}{2} \arctan \frac {x + 1}{2} \Big | _ {- \infty} ^ {1} = \frac {1}{2} \left[ \frac {\pi}{4} - \left(- \frac {\pi}{2}\right) \right] = \frac {3 \pi}{8}. \end{aligned}</equation>

---

**2013年第4题 | 选择题 | 4分 | 答案: D**
4. 设函数 f(x) =<equation>\left\{\begin{array}{l l} \frac{1}{(x-1)^{\alpha-1}},&1<x<\mathrm{e},\\ \frac{1}{x\ln^{\alpha+1}x},&x\geqslant\mathrm{e}. \end{array} \right.</equation>若反常积分<equation>\int_{1}^{+\infty} f(x)\mathrm{d}x</equation>收敛，则（    )

A.<equation>\alpha<-2</equation>B.<equation>\alpha>2</equation>C.<equation>-2<\alpha<0</equation>D.<equation>0<\alpha<2</equation>
答案: D
**解析: **解 由 f(x) 的定义，知<equation>\int_ {1} ^ {+ \infty} f (x) \mathrm {d} x = \int_ {1} ^ {\mathrm {e}} \frac {1}{(x - 1) ^ {\alpha - 1}} \mathrm {d} x + \int_ {\mathrm {e}} ^ {+ \infty} \frac {1}{x \ln^ {\alpha + 1} x} \mathrm {d} x.</equation>由于<equation>\int_{1}^{+\infty} f(x)\mathrm{d}x</equation>收敛，故上式中的两个积分值均应存在且有限.

考虑积分<equation>\int_{1}^{e}\frac{1}{(x-1)^{\alpha-1}}\mathrm{d}x.</equation>当<equation>\alpha-1\leqslant0</equation>即<equation>\alpha\leqslant1</equation>时，该积分为普通定积分.当<equation>\alpha-1>0</equation>时，该积分为无界函数的反常积分（瑕积分），瑕点为<equation>x=1.</equation><equation>\int_ {1} ^ {\mathrm {e}} \frac {1}{(x - 1) ^ {\alpha - 1}} \mathrm {d} x = \frac {(x - 1) ^ {2 - \alpha}}{2 - \alpha} \Bigg | _ {1} ^ {\mathrm {e}}.</equation>若该积分收敛，则<equation>\lim_{x\to 1}\frac{(x - 1)^{2 - \alpha}}{2 - \alpha}</equation>存在，从而<equation>2 - \alpha > 0</equation>，即<equation>\alpha < 2</equation>考虑无穷区间上的反常积分<equation>\int_{\mathrm{e}}^{+\infty}\frac{1}{x\ln^{\alpha+1}x}\mathrm{d}x.</equation><equation>\int_ {\mathrm {e}} ^ {+ \infty} \frac {1}{x \ln^ {\alpha + 1} x} \mathrm {d} x \xlongequal {u = \ln x} \int_ {1} ^ {+ \infty} \frac {1}{u ^ {\alpha + 1}} \mathrm {d} u = - \left. \frac {u ^ {- \alpha}}{\alpha} \right| _ {1} ^ {+ \infty}.</equation>若<equation>\int_{\mathrm{e}}^{+\infty}\frac{1}{x\ln^{\alpha +1}x}\mathrm{d}x</equation>收敛，则<equation>\lim_{u\to +\infty}u^{-\alpha}</equation>存在，从而<equation>-\alpha < 0</equation>，即<equation>\alpha > 0</equation>综上所述，若<equation>\int_{1}^{+\infty} f ( x ) \mathrm{d} x</equation>收敛，则<equation>0 < \alpha < 2</equation>应选D.

---

**2011年第12题 | 填空题 | 4分**
12. 设函数<equation>f ( x )=\left\{\begin{array}{ll}\lambda \mathrm{e}^{-\lambda x}&x>0,\\ 0,&x\leqslant 0,\end{array} \right. \lambda>0</equation>，则<equation>\int_{-\infty}^{+\infty} x f ( x ) \mathrm{d} x=</equation>___
**解析: **解 由于 f(x) 具有分段表达式，故<equation>\int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \int_ {- \infty} ^ {0} x f (x) \mathrm {d} x + \int_ {0} ^ {+ \infty} x f (x) \mathrm {d} x = 0 + \int_ {0} ^ {+ \infty} x f (x) \mathrm {d} x.</equation>下面求<equation>\int_0^{+\infty} xf(x)\mathrm{d}x.</equation><equation>\begin{aligned} \int_ {0} ^ {+ \infty} x f (x) \mathrm {d} x &= \int_ {0} ^ {+ \infty} \lambda x \mathrm {e} ^ {- \lambda x} \mathrm {d} x = - \int_ {0} ^ {+ \infty} x \mathrm {d} \left(\mathrm {e} ^ {- \lambda x}\right) = - \left(x \mathrm {e} ^ {- \lambda x} \Big | _ {0} ^ {+ \infty} - \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda x} \mathrm {d} x\right) \\ &= - \left(\lim _ {x \rightarrow + \infty} x \mathrm {e} ^ {- \lambda x} - 0\right) + \left[ \lim _ {x \rightarrow + \infty} \frac {\mathrm {e} ^ {- \lambda x}}{- \lambda} - \left(\frac {1}{- \lambda}\right)\right]. \end{aligned}</equation>由于<equation>\lambda >0</equation>，故<equation>\lim _ {x \rightarrow + \infty} \frac {x}{\mathrm {e} ^ {\lambda x}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow + \infty} \frac {1}{\lambda \mathrm {e} ^ {\lambda x}} = 0, \quad \lim _ {x \rightarrow + \infty} \frac {\mathrm {e} ^ {- \lambda x}}{- \lambda} = 0.</equation>因此，<equation>\int_ {0} ^ {+ \infty} x f (x) \mathrm {d} x = \frac {1}{\lambda}, \quad \int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \frac {1}{\lambda}.</equation>

---

**2010年第4题 | 选择题 | 4分 | 答案: D**
4. 设 m,n均是正整数，则反常积分<equation>\int_{0}^{1}\frac{\sqrt[m]{\ln^{2}(1-x)}}{\sqrt[n]{x}} \mathrm{d}x</equation>的收敛性（    ）

A. 仅与 m的取值有关 B. 仅与 n的取值有关

C. 与 m,n的取值都有关 D. 与 m,n的取值都无关
答案: D
**解析: **由于被积函数有两个可能的瑕点，<equation>x=0</equation>和<equation>x=1</equation>，故将原积分拆成两部分进行考虑.<equation>\int_ {0} ^ {1} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} \mathrm {d} x = \int_ {0} ^ {\frac {1}{2}} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} \mathrm {d} x + \int_ {\frac {1}{2}} ^ {1} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} \mathrm {d} x.</equation>先讨论<equation>\int_0^{\frac{1}{2}}\frac{\left[\ln(1 - x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>的收敛性.考虑<equation>\lim_{x\to 0^{+}}\frac{\left[\ln(1 - x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}</equation>.<equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} \xlongequal {\ln (1 - x) \sim (- x)} \lim _ {x \rightarrow 0 ^ {+}} x ^ {\frac {2}{m} - \frac {1}{n}} = \left\{\begin{array}{l l}0,&\frac {2}{m} - \frac {1}{n} > 0,\\1,&\frac {2}{m} - \frac {1}{n} = 0,\\\infty ,&\frac {2}{m} - \frac {1}{n} < 0.\end{array}\right.</equation>当 m，n为正整数时，<equation>\frac{2}{m} -\frac{1}{n}\geqslant \frac{2}{m} -1 > -1.</equation>- 当<equation>\frac{2}{m}-\frac{1}{n}\geqslant0</equation>时，<equation>x=0</equation>是被积函数的可去间断点，<equation>\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}</equation>在<equation>\left[0,\frac{1}{2}\right]</equation>上可积，<equation>\int_{0}^{\frac{1}{2}}\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>存在且有限.

- 当<equation>- 1 < \frac{2}{m} - \frac{1}{n} < 0</equation>时，<equation>x=0</equation>是被积函数的瑕点.取<equation>p=\frac{1}{n}-\frac{2}{m}</equation>则<equation>0 < p < 1</equation><equation>\lim_{x\to 0^{+}}\frac{x^{p}\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}=1.</equation>由极限审敛法可知反常积分<equation>\int_{0}^{\frac{1}{2}}\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>收敛.

因此，不论 m，n 取何正整数，积分<equation>\int_{0}^{\frac{1}{2}}\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>均收敛.

下面讨论<equation>\int_{\frac{1}{2}}^{1}\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>的收敛性. x=1为被积函数的瑕点.

考虑极限<equation>\lim _ {x \rightarrow 1 ^ {-}} \sqrt {1 - x} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} = \lim _ {x \rightarrow 1 ^ {-}} \sqrt {1 - x} \left[ \ln (1 - x) \right] ^ {\frac {2}{m}}.</equation>记<equation>I _ {0} = \lim _ {x \rightarrow 1 ^ {-}} \sqrt {1 - x} \left[ \ln (1 - x) \right] ^ {\frac {2}{m}} \xlongequal {u = 1 - x} \lim _ {u \rightarrow 0 ^ {+}} u ^ {\frac {1}{2}} (\ln u) ^ {\frac {2}{m}}.</equation>若 m=1，则<equation>I _ {0} = \lim _ {u \rightarrow 0 ^ {+}} \frac {\left(\ln u\right) ^ {2}}{u ^ {- \frac {1}{2}}} \xlongequal {\text {洛必达}} \lim _ {u \rightarrow 0 ^ {+}} \frac {- 4 \ln u}{u ^ {- \frac {1}{2}}} \xlongequal {\text {洛必达}} \lim _ {u \rightarrow 0 ^ {+}} 8 u ^ {\frac {1}{2}} = 0.</equation>若 m=2，则<equation>I _ {0} = \lim _ {u \rightarrow 0 ^ {+}} \frac {\ln u}{u ^ {- \frac {1}{2}}} \xlongequal {\text {洛 必达}} \lim _ {u \rightarrow 0 ^ {+}} (- 2) u ^ {\frac {1}{2}} = 0.</equation>若<equation>m > 2</equation>，则<equation>0 < \frac{2}{m} < 1</equation>，同理使用洛必达法则可计算得<equation>I_0 = 0.</equation>因此，由极限审敛法知，不论 m，n 取何正整数，积分<equation>\int_{\frac{1}{2}}^{1} \frac{\left[ \ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>均收敛.综上所述，不论 m，n 取何正整数，积分<equation>\int_{0}^{1} \frac{\left[ \ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>均收敛.应选D.

---

**2009年第10题 | 填空题 | 4分**
10. 已知
**答案: **-2.
**解析: **解 由已知等式知，<equation>k\neq 0</equation>，否则<equation>\int_{-\infty}^{+\infty}\mathrm{e}^{k|x|}\mathrm{d}x</equation>不收敛.

去掉被积函数中的绝对值符号.<equation>1 = \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {k | x |} \mathrm {d} x = \int_ {- \infty} ^ {0} \mathrm {e} ^ {- k x} \mathrm {d} x + \int_ {0} ^ {+ \infty} \mathrm {e} ^ {k x} \mathrm {d} x = 2 \int_ {0} ^ {+ \infty} \mathrm {e} ^ {k x} \mathrm {d} x.</equation>由（1）式知，<equation>\int_{0}^{+\infty}\mathrm{e}^{kx}\mathrm{d}x=\frac{1}{2}</equation>从而，<equation>\frac {1}{2} = \int_ {0} ^ {+ \infty} \mathrm {e} ^ {k x} \mathrm {d} x = \lim _ {t \rightarrow + \infty} \left(\int_ {0} ^ {t} \mathrm {e} ^ {k x} \mathrm {d} x\right) = \lim _ {t \rightarrow + \infty} \left. \frac {\mathrm {e} ^ {k x}}{k} \right| _ {0} ^ {t} = \lim _ {t \rightarrow + \infty} \left(\frac {\mathrm {e} ^ {k t}}{k} - \frac {1}{k}\right).</equation>由函数<equation>y=\mathrm{e}^{k x}</equation>的性质知，当<equation>t\to +\infty</equation>时，若<equation>\lim_{t\to +\infty}\mathrm{e}^{k t}</equation>存在，则<equation>k<0.</equation>此时<equation>\lim_{t\to +\infty}\mathrm{e}^{k t}=0.</equation>因此由（2）式可得<equation>-\frac{1}{k}=\frac{1}{2}</equation>即<equation>k=-2.</equation>

---


#### 定积分的概念与性质

**2025年第13题 | 填空题 | 5分**
<equation>\lim _ {n \rightarrow \infty} \frac {1}{n ^ {2}} \left[ \ln \frac {1}{n} + 2 \ln \frac {2}{n} + \dots + (n - 1) \ln \frac {n - 1}{n} \right] = \underline {{}}</equation>
**答案: **# -<equation>\frac{1}{4}</equation>
**解析: **解 从定积分的定义出发，对原极限进行恒等变形，注意到<equation>\ln 1 = 0</equation>，故<equation>\ln \frac {1}{n} + 2 \ln \frac {2}{n} + \dots + (n - 1) \ln \frac {n - 1}{n} = \ln \frac {1}{n} + 2 \ln \frac {2}{n} + \dots + (n - 1) \ln \frac {n - 1}{n} + n \ln \frac {n}{n}.</equation>进一步可得<equation>\begin{aligned} \lim _ {n \rightarrow \infty} \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {i}{n} \ln \frac {i}{n} &= \int_ {0} ^ {1} x \ln x d x = \frac {1}{2} \int_ {0} ^ {1} \ln x d \left(x ^ {2}\right) \\ &= \frac {1}{2} \left(x ^ {2} \ln x \Big | _ {0} ^ {1} - \int_ {0} ^ {1} x ^ {2} \cdot \frac {1}{x} d x\right) = \frac {1}{2} \left(0 - \lim _ {x \rightarrow 0 ^ {+}} x ^ {2} \ln x - \frac {x ^ {2}}{2} \Big | _ {0} ^ {1}\right) \\ \frac {\lim _ {x \rightarrow 0 ^ {+}} x ^ {2} \ln x = 0}{\frac {1}{2}} - \frac {1}{2} \cdot \frac {x ^ {2}}{2} \Big | _ {0} ^ {1} &= - \frac {1}{4}. \end{aligned}</equation>

---

**2022年第7题 | 选择题 | 5分 | 答案: A**
7. 若<equation>I_{1}=\int_{0}^{1}\frac{x}{2(1+\cos x)} \mathrm{d} x, I_{2}=\int_{0}^{1}\frac{\ln(1+x)}{1+\cos x} \mathrm{d} x, I_{3}=\int_{0}^{1}\frac{2x}{1+\sin x} \mathrm{d} x</equation>，则（    )

A.<equation>I_{1}<I_{2}<I_{3}</equation>B.<equation>I_{2}<I_{1}<I_{3}</equation>C.<equation>I_{1}<I_{3}<I_{2}</equation>D.<equation>I_{3}<I_{2}<I_{1}</equation>
答案: A
**解析: **解 通过观察可发现，要比较<equation>I_{1}</equation>与<equation>I_{2}</equation>的大小，只需比较<equation>\frac{x}{2}</equation>与<equation>\ln(1+x)</equation>的大小.

令<equation>f(x)=\ln(1+x)-\frac{x}{2}</equation>，则<equation>f(0)=0</equation><equation>f^{\prime}(x)=\frac{1}{1+x}-\frac{1}{2}</equation>当<equation>x\in(0,1)</equation>时，<equation>f^{\prime}(x)>0</equation><equation>f(x)</equation>单调增加，从而<equation>f(x)>f(0)=0</equation>即<equation>\ln(1+x) > \frac{x}{2},\frac{\ln(1+x)}{1+\cos x} > \frac{x}{2(1+\cos x)}</equation>因此，<equation>I_{2}>I_{1}</equation>此外，同样的方法不难证明在(0,1)内，<equation>\ln(1+x)<x.</equation>另一方面，由于在(0,1)内，<equation>0<\sin x,\cos x<1,1<1+\sin x<2</equation>故<equation>I_{3}</equation>的被积函数<equation>\frac{2x}{1+\sin x} > x.</equation>结合<equation>\ln(1+x)<x</equation>可得，<equation>\frac{\ln(1+x)}{1+\cos x} < \frac{x}{1+\cos x} < x.</equation>于是，<equation>\frac{2x}{1+\sin x}>x > \frac{\ln(1+x)}{1+\cos x}.</equation>因此，<equation>I_{3}>I_{2}.</equation>综上所述，应选A.

---

**2021年第7题 | 选择题 | 5分 | 答案: B**
7. 设函数 f(x)在区间[0,1]上连续，则<equation>\int_{0}^{1} f(x)\mathrm{d}x=</equation>(    )

A.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{n}f\left(\frac{2k-1}{2n}\right)\frac{1}{2n}</equation>B.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{n}f\left(\frac{2k-1}{2n}\right)\frac{1}{n}</equation>C.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{2n}f\left(\frac{k-1}{2n}\right)\frac{1}{n}</equation>D.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{2n}f\left(\frac{k}{2n}\right)\frac{2}{n}</equation>
答案: B
**解析: **解 由于 f(x) 连续，故<equation>\int_{0}^{1} f(x)\mathrm{d}x</equation>存在，从而可对区间[0，1]进行划分，将该积分写为 n项和式的极限.

将[0,1]分为n等份，每个小区间为<equation>\left[ \frac{k-1}{n},\frac{k}{n}\right]</equation><equation>k=1,2,\dots,n</equation>从<equation>\left[ \frac{k-1}{n},\frac{k}{n}\right]</equation>中取点<equation>\frac{2k-1}{2n}</equation>，故由<equation>\int_{0}^{1} f(x)\mathrm{d}x</equation>存在以及定积分的定义可得<equation>\int_ {0} ^ {1} f (x) \mathrm {d} x = \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} f \left(\frac {2 k - 1}{2 n}\right) \cdot \frac {1}{n}.</equation>因此，应选B.

下面说明选项A、C、D均不正确.

选项A：<equation>\lim_{n\to \infty}\sum_{k=1}^{n}f\left(\frac{2k-1}{2n}\right)\frac{1}{2n}=\frac{1}{2}\lim_{n\to \infty}\sum_{k=1}^{n}f\left(\frac{2k-1}{2n}\right)\frac{1}{n}=\frac{1}{2}\int_{0}^{1}f(x)\mathrm{d}x.</equation>选项C：<equation>\lim_{n\to \infty}\sum_{k=1}^{2n}f\left(\frac{k-1}{2n}\right)\frac{1}{n}=2\lim_{n\to \infty}\sum_{k=1}^{2n}f\left(\frac{k-1}{2n}\right)\frac{1}{2n}=2\int_{0}^{1}f(x)\mathrm{d}x.</equation>选项D：<equation>\lim_{n\to \infty}\sum_{k=1}^{2n}f\left(\frac{k}{2n}\right)\frac{2}{n}=4\lim_{n\to \infty}\sum_{k=1}^{2n}f\left(\frac{k}{2n}\right)\frac{1}{2n}=4\int_{0}^{1}f(x)\mathrm{d}x.</equation>

---

**2018年第5题 | 选择题 | 4分 | 答案: C**
5. 设<equation>M=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{(1+x)^{2}}{1+x^{2}}\mathrm{d}x,N=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{1+x}{\mathrm{e}^{x}}\mathrm{d}x,K=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}(1+\sqrt{\cos x})\mathrm{d}x</equation>，则（    )

A. M > N > K B. M > K > N C. K > M > N D. K > N > M
答案: C
**解析: **分别计算 M,N,K.

由于<equation>\frac{2x}{1+x^{2}}</equation>是奇函数，故<equation>\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{2x}{1+x^{2}}\mathrm{d}x=0.</equation>于是，<equation>M = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {(1 + x) ^ {2}}{1 + x ^ {2}} \mathrm {d} x = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {1 + x ^ {2} + 2 x}{1 + x ^ {2}} \mathrm {d} x \frac {\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {2 x}{1 + x ^ {2}} \mathrm {d} x = 0}{\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \mathrm {d} x = \pi}.</equation>注意到当<equation>x\neq 0</equation>时，<equation>\mathrm{e}^{x}>1+x</equation>.于是，在<equation>\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>上，<equation>\frac{1+x}{e^{x}}\leqslant 1</equation>且等号仅在<equation>x=0</equation>处成立.<equation>N = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {1 + x}{\mathrm {e} ^ {x}} \mathrm {d} x < \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \mathrm {d} x = \pi .</equation>由于<equation>\sqrt{\cos x}</equation>是偶函数，且当 x<equation>\in\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>时，<equation>\cos x\geqslant0</equation>且等号仅在端点处成立，故<equation>\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\sqrt{\cos x}\mathrm{d}x=2\int_{0}^{\frac{\pi}{2}}\sqrt{\cos x}\mathrm{d}x>0.</equation>于是，<equation>K = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \left(1 + \sqrt {\cos x}\right) \mathrm {d} x = \pi + \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \sqrt {\cos x} \mathrm {d} x > \pi .</equation>综上所述，<equation>K > M > N</equation>应选C.

---

**2017年第17题 | 解答题 | 10分**
17. (本题满分10分)<equation>\text {求} \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n ^ {2}} \ln \left(1 + \frac {k}{n}\right)</equation>
**解析: **解 根据定积分的定义，提出因子<equation>\frac{1}{n}</equation>，可得<equation>\begin{aligned} \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n ^ {2}} \ln \left(1 + \frac {k}{n}\right) &= \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n} \ln \left(1 + \frac {k}{n}\right) \cdot \frac {1}{n} = \int_ {0} ^ {1} x \ln (1 + x) d x \\ &= \frac {1}{2} \int_ {0} ^ {1} \ln (1 + x) d \left(x ^ {2}\right) \xlongequal {\mathrm {分 部 积 分}} \frac {x ^ {2}}{2} \ln (1 + x) \Bigg | _ {0} ^ {1} - \int_ {0} ^ {1} \frac {x ^ {2}}{2 (1 + x)} d x \\ &= \frac {\ln 2}{2} - \frac {1}{2} \int_ {0} ^ {1} \frac {x ^ {2} - 1 + 1}{1 + x} d x = \frac {\ln 2}{2} - \frac {1}{2} \int_ {0} ^ {1} \left(x - 1 + \frac {1}{1 + x}\right) d x \\ &= \frac {\ln 2}{2} - \frac {1}{2} \left[ \frac {x ^ {2}}{2} - x + \ln (1 + x) \right] \Bigg | _ {0} ^ {1} = \frac {1}{4}. \end{aligned}</equation>因此，原极限<equation>= \frac{1}{4}.</equation>

---

**2016年第10题 | 填空题 | 4分**
<equation>0. \mathrm {极 限} \lim _ {n \rightarrow \infty} \frac {1}{n ^ {2}} \left(\sin \frac {1}{n} + 2 \sin \frac {2}{n} + \dots + n \sin \frac {n}{n}\right) = \underline {{}}</equation>
**答案: **sin 1-cos 1.
**解析: **解 将原表达式作恒等变形，提出因子<equation>\frac{1}{n}</equation><equation>\frac {1}{n ^ {2}} \left(\sin \frac {1}{n} + 2 \sin \frac {2}{n} + \dots + n \sin \frac {n}{n}\right) = \frac {1}{n} \left(\frac {1}{n} \sin \frac {1}{n} + \frac {2}{n} \sin \frac {2}{n} + \dots + \frac {n}{n} \sin \frac {n}{n}\right).</equation><equation>\begin{aligned} \mathrm {原 极 限} &= \lim _ {n \rightarrow \infty} \left(\frac {1}{n} \sum_ {i = 1} ^ {n} \frac {i}{n} \sin \frac {i}{n}\right) = \int_ {0} ^ {1} x \sin x \mathrm {d} x = \int_ {0} ^ {1} x \mathrm {d} (- \cos x) \\ &= - x \cos x \Bigg | _ {0} ^ {1} + \int_ {0} ^ {1} \cos x \mathrm {d} x = \sin 1 - \cos 1. \end{aligned}</equation>

---

**2012年第4题 | 选择题 | 4分 | 答案: D**
4. 设<equation>I_{k}=\int_{0}^{k\pi}\mathrm{e}^{x^{2}}\sin x\mathrm{d}x(k=1,2,3)</equation>，则有（    ）

A.<equation>I_{1}<I_{2}<I_{3}</equation>B.<equation>I_{3}<I_{2}<I_{1}</equation>C.<equation>I_{2}<I_{3}<I_{1}</equation>D.<equation>I_{2}<I_{1}<I_{3}</equation>
答案: D
**解析: **解（法一）记<equation>J_{k}=\int_{(k-1)\pi}^{k\pi}\mathrm{e}^{x^{2}}\sin x\mathrm{d}x(k=1,2,3)</equation>，则<equation>I _ {1} = J _ {1}, \quad I _ {2} = J _ {1} + J _ {2}, \quad I _ {3} = J _ {1} + J _ {2} + J _ {3}.</equation>由于<equation>\mathrm{e}^{x^{2}}>0</equation>，且在（0，<equation>\pi</equation>）上，<equation>\sin x>0</equation>；在（<equation>\pi,2\pi</equation>）上，<equation>\sin x<0</equation>；在（<equation>2\pi,3\pi</equation>）上，<equation>\sin x>0</equation>，故<equation>J_{1}>0</equation>，<equation>J_{2}<0</equation>，<equation>J_{3}>0</equation>.由此可得，<equation>I_{1}>I_{2},I_{3}>I_{2}.</equation>下面比较<equation>I_{1}</equation>和<equation>I_{3}.</equation><equation>I _ {3} - I _ {1} = J _ {2} + J _ {3}.</equation><equation>J _ {3} = \int_ {2 \pi} ^ {3 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x > \mathrm {e} ^ {(2 \pi) ^ {2}} \int_ {2 \pi} ^ {3 \pi} \sin x \mathrm {d} x,</equation><equation>\left| J _ {2} \right| = \left| \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x \right| < \mathrm {e} ^ {(2 \pi) ^ {2}} \left| \int_ {\pi} ^ {2 \pi} \sin x \mathrm {d} x \right|, \quad J _ {2} > - \mathrm {e} ^ {(2 \pi) ^ {2}} \left| \int_ {\pi} ^ {2 \pi} \sin x \mathrm {d} x \right|.</equation>由定积分的几何意义可知，<equation>\int_{2\pi}^{3\pi}\sin x\mathrm{d}x</equation>和<equation>|\int_{\pi}^{2\pi}\sin x\mathrm{d}x|</equation>分别为<equation>\sin x</equation>在<equation>(2\pi ,3\pi)</equation>上以及在<equation>(\pi ,2\pi)</equation>上的部分与<equation>x</equation>轴围成的图形面积.根据<equation>\sin x</equation>的图形，这两部分面积相等，即<equation>\int_{2\pi}^{3\pi}\sin x\mathrm{d}x = \left|\int_{\pi}^{2\pi}\sin x\mathrm{d}x\right|.</equation>于是，<equation>J _ {2} + J _ {3} > \mathrm {e} ^ {(2 \pi) ^ {2}} \left(\int_ {2 \pi} ^ {3 \pi} \sin x \mathrm {d} x - \left| \int_ {\pi} ^ {2 \pi} \sin x \mathrm {d} x \right|\right) = 0,</equation>即<equation>I_{3} > I_{1}.</equation>因此，<equation>I_{2} < I_{1} < I_{3}</equation>应选D.

（法二）在法一中，证明<equation>J_{2} + J_{3} > 0</equation>，也可以使用如下方法.<equation>J _ {3} = \int_ {2 \pi} ^ {3 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x \xlongequal {u = x - \pi} \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {(u + \pi) ^ {2}} \sin (u + \pi) \mathrm {d} u = - \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {(u + \pi) ^ {2}} \sin u \mathrm {d} u,</equation><equation>J _ {2} + J _ {3} = \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x - \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {(x + \pi) ^ {2}} \sin x \mathrm {d} x = \int_ {\pi} ^ {2 \pi} \sin x \left[ \mathrm {e} ^ {x ^ {2}} - \mathrm {e} ^ {(x + \pi) ^ {2}} \right] \mathrm {d} x.</equation>当<equation>x \in(\pi, 2\pi)</equation>时，<equation>\sin x < 0,\mathrm{e}^{x^{2}}-\mathrm{e}^{(x+\pi)^{2}} < 0,\sin x[\mathrm{e}^{x^{2}}-\mathrm{e}^{(x+\pi)^{2}}] > 0</equation>从而<equation>J_{2}+J_{3}>0.</equation>其余同法一.

---

**2012年第10题 | 填空题 | 4分**
10.<equation>\lim_{n\to\infty}n</equation>
**解析: **从定积分的定义出发，对原极限进行恒等变形<equation>\begin{aligned} \lim _ {n \rightarrow \infty} n \left(\frac {1}{1 + n ^ {2}} + \frac {1}{2 ^ {2} + n ^ {2}} + \dots + \frac {1}{n ^ {2} + n ^ {2}}\right) &= \lim _ {n \rightarrow \infty} \frac {1}{n} \left(\frac {n ^ {2}}{1 + n ^ {2}} + \frac {n ^ {2}}{2 ^ {2} + n ^ {2}} + \dots + \frac {n ^ {2}}{n ^ {2} + n ^ {2}}\right) \\ &= \lim _ {n \rightarrow \infty} \frac {1}{n} \left[ \frac {1}{\left(\frac {1}{n}\right) ^ {2} + 1} + \frac {1}{\left(\frac {2}{n}\right) ^ {2} + 1} + \dots + \frac {1}{\left(\frac {n}{n}\right) ^ {2} + 1} \right] \\ &= \lim _ {n \rightarrow \infty} \frac {1}{n} \left[ \sum_ {i = 1} ^ {n} \frac {1}{1 + \left(\frac {i}{n}\right) ^ {2}} \right] = \int_ {0} ^ {1} \frac {1}{1 + x ^ {2}} d x \\ &= \arctan x \Bigg | _ {0} ^ {1} = \frac {\pi}{4}. \end{aligned}</equation>

---

**2011年第6题 | 选择题 | 4分 | 答案: B**
6. 设<equation>I=\int_{0}^{\frac{\pi}{4}}\ln(\sin x)\mathrm{d}x, J=\int_{0}^{\frac{\pi}{4}}\ln(\cot x)\mathrm{d}x, K=\int_{0}^{\frac{\pi}{4}}\ln(\cos x)\mathrm{d}x</equation>，则 I, J, K的大小关系为（    )

A. I < J < K

B. I < K < J

C. J < I < K

D. K < J < I
答案: B
**解析: **解 由于在<equation>\left( 0, \frac{\pi}{4} \right)</equation>上，<equation>0 < \sin x < \cos x < 1 < \cot x</equation>，而<equation>\ln u</equation>为（0，<equation>+\infty</equation>）上的单调增加函数，故<equation>\ln(\sin x) < \ln(\cos x) < 0 < \ln(\cot x).</equation>又因为 I，J，K的积分区间一致，所以 I < K < J.应选B.

---

**2010年第16题 | 解答题 | 10分**
16. (本题满分10分)

16. (本题满分10分)

I. 比较<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>与<equation>\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t</equation>（ n=1,2,<equation>\cdots</equation>）的大小，说明理由；

II. 记<equation>u_{n}=\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>（ n=1,2,<equation>\cdots</equation>），求极限<equation>\lim_{n\to\infty}u_{n}.</equation>
**答案: **（16）（I）<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t<\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t(n=1,2,\cdots)</equation>，理由略；

（Ⅱ）<equation>\lim_{n\to \infty}u_{n}=0.</equation>
**解析: **解（I）在（0，1]上，<equation>|\ln t|</equation><equation>\ln(1+t)</equation>与 t均非负，故比较<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>与<equation>\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t(n=1,2,\cdots)</equation>的大小，只需比较<equation>\ln(1+t)</equation>与 t的大小.

考虑 f（t）=<equation>\ln(1+t)-t.</equation><equation>f ^ {\prime} (t) = \frac {1}{1 + t} - 1.</equation>当<equation>t\in (0,1]</equation>时，<equation>f^{\prime}(t) < 0,f(t)\leqslant f(0) = 0.</equation>因此，当<equation>t\in[0,1]</equation>时，<equation>\ln(1 + t)\leqslant t.</equation>由于两被积函数仅在<equation>t = 1</equation>处相等，故<equation>\int_ {0} ^ {1} | \ln t | [ \ln (1 + t) ] ^ {n} \mathrm {d} t < \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t (n = 1, 2, \dots).</equation>（Ⅱ）（法一）由第（I）问知，<equation>0 < u_{n} < \int_{0}^{1} t^{n}|\ln t|\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {0} ^ {1} t ^ {n} \mid \ln t \mid \mathrm {d} t &= \frac {- 1}{n + 1} \int_ {0} ^ {1} \ln t \mathrm {d} \left(t ^ {n + 1}\right) = \frac {- 1}{n + 1} \left(t ^ {n + 1} \ln t \mid_ {0} ^ {1} - \int_ {0} ^ {1} t ^ {n + 1} \cdot \frac {1}{t} \mathrm {d} t\right) \\ \frac {\lim _ {t \rightarrow 0 ^ {+}} t ^ {n + 1} \ln t = 0}{\overline {{\quad}}} \frac {1}{n + 1} \int_ {0} ^ {1} t ^ {n} \mathrm {d} t &= \frac {1}{(n + 1) ^ {2}}. \end{aligned}</equation>因此，<equation>\lim _ {n \rightarrow \infty} \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t = \lim _ {n \rightarrow \infty} \frac {1}{(n + 1) ^ {2}} = 0.</equation>由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>（法二）由第（I）问知，<equation>0 < u_{n} < \int_{0}^{1} t^{n}|\ln t|\mathrm{d}t.</equation>又因为<equation>\lim_{t\to 0^{+}}t\ln t = 0</equation>，所以存在<equation>M > 0</equation>，使得对任意的<equation>t\in (0,1]</equation>，有<equation>t|\ln t|\leqslant M</equation>，从而<equation>0 < u _ {n} < \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t \leqslant M \int_ {0} ^ {1} t ^ {n - 1} \mathrm {d} t = \frac {M}{n}.</equation>由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>（法三）由于<equation>t\in[0,1]</equation>时，<equation>\ln(1 + t)\leqslant \ln 2 < 1</equation>，故<equation>u_{n}\leqslant (\ln 2)^{n}\int_{0}^{1}|\ln t|\mathrm{d}t.</equation>计算<equation>\int_{0}^{1}|\ln t| \mathrm{d} t</equation>得，<equation>\int_ {0} ^ {1} | \ln t | \mathrm {d} t = - \int_ {0} ^ {1} \ln t \mathrm {d} t = - \left(t \ln t \Big | _ {0} ^ {1} - \int_ {0} ^ {1} 1 \mathrm {d} t\right) \xlongequal {\lim _ {t \rightarrow 0 ^ {+}} t \ln t = 0} 1.</equation>从而<equation>0 < u_{n}\leqslant (\ln 2)^{n}</equation>因为<equation>\lim_{n\to \infty}(\ln 2)^n = 0</equation>，所以由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>

---


#### 定积分的计算

**2025年第17题 | 解答题 | 10分**
17. (本题满分10分)

计算<equation>\int_ {0} ^ {1} \frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} \mathrm {d} x</equation>
**答案: **<equation>\frac {3}{1 0} \ln 2 + \frac {\pi}{1 0}</equation>
**解析: **解设<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {A}{x + 1} + \frac {B x + C}{x ^ {2} - 2 x + 2}.</equation>通分并整理可得，<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {(A + B) x ^ {2} + (B + C - 2 A) x + 2 A + C}{(x + 1) \left(x ^ {2} - 2 x + 2\right)}.</equation>比较<equation>x^{2}, x</equation>的系数以及常数项可得，<equation>A + B = 0,</equation><equation>B + C - 2 A = 0,</equation><equation>2 A + C = 1.</equation>由（1）式可得<equation>B=-A</equation>.将<equation>B=-A</equation>代入（2）式可得<equation>C=3A</equation>.将<equation>C=3A</equation>代入（3）式可得<equation>5A=1</equation>，即<equation>A=\frac{1}{5}</equation>.进一步可得<equation>B=-\frac{1}{5},C=\frac{3}{5}.</equation>由此可得，<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {1}{5} \left(\frac {1}{x + 1} - \frac {x - 3}{x ^ {2} - 2 x + 2}\right).</equation>下面分别计算<equation>\int_0^1\frac{1}{x + 1}\mathrm{d}x</equation>与<equation>\int_0^1\frac{x - 3}{x^2 - 2x + 2}\mathrm{d}x.</equation><equation>\int_ {0} ^ {1} \frac {1}{x + 1} \mathrm {d} x = \ln (x + 1) \Big | _ {0} ^ {1} = \ln 2.</equation><equation>\begin{aligned} \int_ {0} ^ {1} \frac {x - 3}{x ^ {2} - 2 x + 2} \mathrm {d} x &= \int_ {0} ^ {1} \frac {x - 1}{x ^ {2} - 2 x + 2} \mathrm {d} x - \int_ {0} ^ {1} \frac {2}{x ^ {2} - 2 x + 2} \mathrm {d} x \\ &= \frac {1}{2} \int_ {0} ^ {1} \frac {\mathrm {d} \left(x ^ {2} - 2 x + 2\right)}{x ^ {2} - 2 x + 2} - 2 \int_ {0} ^ {1} \frac {1}{1 + (x - 1) ^ {2}} \mathrm {d} x \\ &= \frac {1}{2} \ln \left(x ^ {2} - 2 x + 2\right) \left| _ {0} ^ {1} - 2 \arctan (x - 1) \right| _ {0} ^ {1} \\ &= - \frac {1}{2} \ln 2 - 2 [ 0 - \arctan (- 1) ] = - \frac {1}{2} \ln 2 - \frac {\pi}{2}. \end{aligned}</equation>因此，<equation>\int_ {0} ^ {1} \frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} \mathrm {d} x = \frac {1}{5} \left[ \ln 2 - \left(- \frac {1}{2} \ln 2 - \frac {\pi}{2}\right) \right] = \frac {3 \ln 2 + \pi}{1 0}.</equation>

---

**2023年第15题 | 填空题 | 5分**
15. 设连续函数 f(x)满足<equation>f(x+2)-f(x)=x,\int_{0}^{2} f(x)\mathrm{d} x=0</equation>，则<equation>\int_{1}^{3} f(x)\mathrm{d} x=</equation>___
**答案: **# 1/2
**解析: **解注意到<equation>\int_{2}^{3} f ( x ) \mathrm{d} x=\int_{0}^{1} f ( x+2 ) \mathrm{d} x</equation>，故由<equation>f ( x+2 )-f ( x )=x</equation>可得，<equation>\int_{2}^{3} f ( x ) \mathrm{d} x-\int_{0}^{1} f ( x ) \mathrm{d} x=\int_{0}^{1} f ( x+2 ) \mathrm{d} x-\int_{0}^{1} f ( x ) \mathrm{d} x=\int_{0}^{1} x \mathrm{d} x=\frac{1}{2}.</equation>(1)

又因为<equation>\int_{0}^{1} f ( x ) \mathrm{d} x+\int_{1}^{2} f ( x ) \mathrm{d} x=\int_{0}^{2} f ( x ) \mathrm{d} x=0</equation>，所以<equation>-\int_{0}^{1} f ( x ) \mathrm{d} x=\int_{1}^{2} f ( x ) \mathrm{d} x.</equation>从而由（1）式可得<equation>\int_{2}^{3} f ( x ) \mathrm{d} x+\int_{1}^{2} f ( x ) \mathrm{d} x=\frac{1}{2},</equation>即<equation>\int_{1}^{3} f ( x ) \mathrm{d} x=\frac{1}{2}.</equation>

---

**2022年第13题 | 填空题 | 5分**
13.<equation>\int_ {0} ^ {1} \frac {2 x + 3}{x ^ {2} - x + 1} \mathrm {d} x = \underline {{}}</equation>
**答案: **<equation>\frac{8\sqrt{3}\pi}{9}.</equation>
**解析: **解注意到<equation>( x^{2}-x+1)^{\prime}=2 x-1</equation>，<equation>\frac{2 x+3}{x^{2}-x+1}=\frac{2 x-1}{x^{2}-x+1}+\frac{4}{x^{2}-x+1}.</equation>因此，<equation>\begin{aligned} \int_ {0} ^ {1} \frac {2 x + 3}{x ^ {2} - x + 1} \mathrm {d} x &= \int_ {0} ^ {1} \frac {2 x - 1}{x ^ {2} - x + 1} \mathrm {d} x + 4 \int_ {0} ^ {1} \frac {1}{\left(x - \frac {1}{2}\right) ^ {2} + \frac {3}{4}} \mathrm {d} x \\ &= \int_ {0} ^ {1} \frac {\mathrm {d} \left(x ^ {2} - x + 1\right)}{x ^ {2} - x + 1} + \frac {1 6}{3} \int_ {0} ^ {1} \frac {1}{1 + \left[ \frac {2}{\sqrt {3}} \left(x - \frac {1}{2}\right) \right] ^ {2}} \mathrm {d} x \\ &= \ln \left(x ^ {2} - x + 1\right) \Bigg | _ {0} ^ {1} + \frac {8 \sqrt {3}}{3} \int_ {0} ^ {1} \frac {\mathrm {d} \left[ \frac {2}{\sqrt {3}} \left(x - \frac {1}{2}\right) \right]}{1 + \left[ \frac {2}{\sqrt {3}} \left(x - \frac {1}{2}\right) \right] ^ {2}} \\ &= \frac {8 \sqrt {3}}{3} \arctan \frac {2}{\sqrt {3}} \left(x - \frac {1}{2}\right) \Bigg | _ {0} ^ {1} = \frac {8 \sqrt {3}}{3} \times \frac {\pi}{3} = \frac {8 \sqrt {3} \pi}{9}. \end{aligned}</equation>

---

**2020年第3题 | 选择题 | 4分 | 答案: A**
3. 

.<equation>\int_{0}^{1} \frac{\arcsin \sqrt{x}}{\sqrt{x(1-x)}} \mathrm{d} x=</equation>(    )

A.<equation>\frac{\pi^{2}}{4}</equation>B.<equation>\frac{\pi^{2}}{8}</equation>C.<equation>\frac{\pi}{4}</equation>D.<equation>\frac{\pi}{8}</equation>
答案: A
**解析: **解 令<equation>\sqrt{x}=\sin t,t\in\left(0,\frac{\pi}{2}\right)</equation>，则 x=<equation>\sin^{2}t</equation>,<equation>\mathrm{d}x=2\sin t\cos t\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {0} ^ {1} \frac {\arcsin \sqrt {x}}{\sqrt {x (1 - x)}} \mathrm {d} x \xlongequal {\sqrt {x} = \sin t} \int_ {0} ^ {\frac {\pi}{2}} \frac {t}{\sqrt {\sin^ {2} t \cos^ {2} t}} \cdot 2 \sin t \cos t \mathrm {d} t &= \int_ {0} ^ {\frac {\pi}{2}} 2 t \mathrm {d} t \\ &= t ^ {2} \Big | _ {0} ^ {\frac {\pi}{2}} = \frac {\pi^ {2}}{4}. \end{aligned}</equation>因此，应选A.

---

**2019年第13题 | 填空题 | 4分**
13. 已知函数<equation>f ( x )=x \int_{1}^{x} \frac{\sin t^{2}}{t} \mathrm{d} t</equation>，则<equation>\int_{0}^{1} f ( x ) \mathrm{d} x=</equation>___.
**答案: **<equation>\frac {1}{4} (\cos 1 - 1).</equation>
**解析: **解 （法一）利用分部积分法.

记<equation>F ( x )=\int_{1}^{x}\frac{\sin t^{2}}{t}\mathrm{d} t</equation>，则<equation>F ( 1 )=0,F^{\prime}(x)=\frac{\sin x^{2}}{x}.</equation><equation>\begin{aligned} \int_ {0} ^ {1} f (x) \mathrm {d} x &= \int_ {0} ^ {1} x F (x) \mathrm {d} x = \frac {1}{2} \int_ {0} ^ {1} F (x) \mathrm {d} \left(x ^ {2}\right) = \frac {1}{2} \left[ x ^ {2} F (x) \left| _ {0} ^ {1} - \int_ {0} ^ {1} x ^ {2} \cdot F ^ {\prime} (x) \mathrm {d} x \right. \right] \\ &= - \frac {1}{2} \int_ {0} ^ {1} x ^ {2} \cdot \frac {\sin x ^ {2}}{x} \mathrm {d} x = - \frac {1}{2} \int_ {0} ^ {1} x \sin x ^ {2} \mathrm {d} x = - \frac {1}{4} \int_ {0} ^ {1} \sin x ^ {2} \mathrm {d} \left(x ^ {2}\right) \\ &= \frac {1}{4} \cos x ^ {2} \Bigg | _ {0} ^ {1} = \frac {1}{4} (\cos 1 - 1). \end{aligned}</equation>（法二）交换积分次序.

将 f(x) 代入所求积分.<equation>\int_ {0} ^ {1} f (x) \mathrm {d} x = \int_ {0} ^ {1} x \left(\int_ {1} ^ {x} \frac {\sin t ^ {2}}{t} \mathrm {d} t\right) \mathrm {d} x = \int_ {0} ^ {1} x \mathrm {d} x \int_ {1} ^ {x} \frac {\sin t ^ {2}}{t} \mathrm {d} t.</equation>写出该积分对应的二重积分的积分区域 D. 由二次积分的表达式可知，边界曲线为 t=x， t=1以及 x=0，故<equation>D = \left\{(x, t) \mid x \leqslant t \leqslant 1, 0 \leqslant x \leqslant 1 \right\}.</equation>如图所示，交换积分次序可得<equation>D = \left\{(x, t) \mid 0 \leqslant x \leqslant t, 0 \leqslant t \leqslant 1 \right\}.</equation>因此，<equation>\begin{aligned} \mathrm {原 积 分} &= - \iint_ {D} \frac {x \sin t ^ {2}}{t} \mathrm {d} x \mathrm {d} t = - \int_ {0} ^ {1} \frac {\sin t ^ {2}}{t} \mathrm {d} t \int_ {0} ^ {t} x \mathrm {d} x = - \int_ {0} ^ {1} \frac {\sin t ^ {2}}{t} \cdot \frac {t ^ {2}}{2} \mathrm {d} t \\ &= - \frac {1}{2} \int_ {0} ^ {1} t \sin t ^ {2} \mathrm {d} t = - \frac {1}{4} \int_ {0} ^ {1} \sin t ^ {2} \mathrm {d} \left(t ^ {2}\right) = \frac {1}{4} \cos t ^ {2} \Big | _ {0} ^ {1} = \frac {1}{4} (\cos 1 - 1). \end{aligned}</equation>

---

**2016年第16题 | 解答题 | 10分**
16. (本题满分10分）

设函数<equation>f ( x )=\int_{0}^{1} \left| t^{2}-x^{2} \right| \mathrm{d} t ( x > 0 )</equation>，求<equation>f^{\prime} ( x )</equation>，并求 f(x)的最小值.
**答案: **<equation>f^{\prime}(x)=\left\{ \begin{array}{ll} 4x^{2}-2x, & 0<x<1,\\ 2x, & x\geqslant1. \end{array} \right.</equation>最小值<equation>f\left(\frac{1}{2}\right)=\frac{1}{4}.</equation>
**解析: **解 对 x的取值范围进行讨论.由<equation>f ( x )=\int_{0}^{1} \mid t^{2}-x^{2} \mid \mathrm{d} t</equation>知， •当 x≥1时，<equation>x\geqslant t</equation><equation>\mid t^{2}-x^{2}\mid=x^{2}-t^{2}.</equation>- 当 0 < x < 1时，有两种情况.<equation>\left| t ^ {2} - x ^ {2} \right| = \left\{ \begin{array}{l l} x ^ {2} - t ^ {2}, & 0 \leqslant t \leqslant x, \\ t ^ {2} - x ^ {2}, & x < t \leqslant 1. \end{array} \right.</equation>于是，当 x > 1时，<equation>f (x) = \int_ {0} ^ {1} \left| t ^ {2} - x ^ {2} \right| \mathrm {d} t = \int_ {0} ^ {1} \left(x ^ {2} - t ^ {2}\right) \mathrm {d} t = x ^ {2} - \frac {1}{3}.</equation>当 x=1时，<equation>f (x) = \int_ {0} ^ {1} \left| t ^ {2} - 1 \right| \mathrm {d} t = \int_ {0} ^ {1} \left(1 - t ^ {2}\right) \mathrm {d} t = 1 - \frac {1}{3} = \frac {2}{3}.</equation>当 0 < x < 1时，<equation>\begin{aligned} f (x) &= \int_ {0} ^ {1} \left| t ^ {2} - x ^ {2} \right| \mathrm {d} t = \int_ {0} ^ {x} \left(x ^ {2} - t ^ {2}\right) \mathrm {d} t + \int_ {x} ^ {1} \left(t ^ {2} - x ^ {2}\right) \mathrm {d} t \\ &= x ^ {3} - \frac {t ^ {3}}{3} \left| _ {0} ^ {x} + \frac {t ^ {3}}{3} \right| _ {x} ^ {1} - x ^ {2} (1 - x) = \frac {4}{3} x ^ {3} - x ^ {2} + \frac {1}{3}. \end{aligned}</equation>因此，<equation>f ( x )=\left\{\begin{array}{ll}\frac{4}{3} x^{3}-x^{2}+\frac{1}{3},&0<x<1,\\ x^{2}-\frac{1}{3},&x\geqslant 1.\end{array}\right.</equation>从<equation>f ( x )</equation>的表达式可以看出，<equation>f \left(1 ^ {-}\right) = f \left(1 ^ {+}\right) = f (1) = \frac {2}{3}.</equation>f（x）在 x=1处连续.

由 f(x)的表达式可知，当<equation>0 < x < 1</equation>时，<equation>f^{\prime}(x)=4x^{2}-2x</equation>；当 x > 1时，<equation>f^{\prime}(x)=2x.</equation>当 x=1时，根据导数的定义分别计算 f（x）在 x=1处的左侧导数和右侧导数.<equation>\begin{aligned} f _ {-} ^ {\prime} (1) &= \lim _ {x \rightarrow 1 ^ {-}} \frac {\frac {4}{3} x ^ {3} - x ^ {2} - \frac {1}{3}}{x - 1} = \lim _ {x \rightarrow 1 ^ {-}} \frac {\frac {4}{3} x ^ {3} - \frac {4}{3} x ^ {2} + \frac {1}{3} x ^ {2} - \frac {1}{3}}{x - 1} \\ &= \lim _ {x \rightarrow 1 ^ {-}} \frac {(x - 1) \left[ \frac {4}{3} x ^ {2} + \frac {1}{3} (x + 1) \right]}{x - 1} = \lim _ {x \rightarrow 1 ^ {-}} \left[ \frac {4}{3} x ^ {2} + \frac {1}{3} (x + 1) \right] = 2, \end{aligned}</equation><equation>f _ {+} ^ {\prime} (1) = \lim _ {x \rightarrow 1 ^ {+}} \frac {x ^ {2} - 1}{x - 1} = \lim _ {x \rightarrow 1 ^ {+}} (x + 1) = 2.</equation>由此可见，<equation>f^{\prime}(1)=f_{-}^{\prime}(1)=f_{+}^{\prime}(1)=2.</equation>因此，<equation>f ^ {\prime} (x) = \left\{ \begin{array}{l l} 4 x ^ {2} - 2 x, & 0 < x < 1, \\ 2 x, & x \geqslant 1. \end{array} \right.</equation>从<equation>f^{\prime}(x)</equation>的表达式可以看出，<equation>f^{\prime}(x)</equation>连续，从而<equation>y=f(x)</equation>是一条光滑曲线.

当 x > 1时，<equation>f^{\prime}(x)=2x>0</equation>，故 f(x)在（1，<equation>+\infty</equation>）内单调增加.

当 0 < x < 1时，<equation>f^{\prime}(x)=4x^{2}-2x.</equation>求<equation>f^{\prime}(x)</equation>的零点得，<equation>x=\frac{1}{2}</equation>或 x=0（舍去）.因此，当 0 < x <<equation>\frac{1}{2}</equation>时，<equation>f^{\prime}(x)<0</equation>；当<equation>\frac{1}{2} < x < 1</equation>时，<equation>f^{\prime}(x)>0.</equation>由于 f(x) 连续，故可知 f(x) 的最小值在 x =<equation>\frac{1}{2}</equation>处取得.<equation>f\left(\frac{1}{2}\right)=\frac{4}{3}\times \frac{1}{8}-\frac{1}{4}+\frac{1}{3}=\frac{1}{4}.</equation>

---

**2014年第10题 | 填空题 | 4分**
10. 设<equation>f(x)</equation>是周期为4的可导奇函数,且<equation>f^{\prime}(x)=2(x-1),x\in[0,2]</equation>,则<equation>f(7)=</equation>___.
**解析: **由于<equation>f ( x )</equation>是周期为4的函数，且<equation>7=2 \times4-1</equation>，故<equation>f ( 7 )=f (-1).</equation>(a)

(b)

（法一）由 f(x)为奇函数可得 f（0）=0.由当 x<equation>\in[0,2]</equation>时，<equation>f^{\prime}(x)=2(x-1)</equation>可得， f(x)在 [0,2]上的表达式为<equation>f (x) = \int_ {0} ^ {x} 2 (t - 1) \mathrm {d} t + f (0) = x ^ {2} - 2 x = (x - 1) ^ {2} - 1.</equation>于是<equation>f(1) = -1.</equation>由<equation>f(x)</equation>为奇函数得，<equation>f(-1) = -f(1) = 1</equation>，即<equation>f(7) = 1.</equation>（法二）由 f(x)为奇函数可知，<equation>f(x)=-f(-x).</equation>在等式两端求导得<equation>f^{\prime}(x)=f^{\prime}(-x),</equation>从而<equation>f^{\prime}(x)</equation>为偶函数，<equation>f^{\prime}(x)</equation>的图像关于 y轴对称.在[0，2]上，<equation>f^{\prime}(x)=2(x-1)</equation>，为一条过点（0，-2）和点（1，0）的直线.由此可知，在[-2，0]上，<equation>y=f^{\prime}(x)</equation>为过点（0，-2）和点（-1，0）的直线，可求得<equation>f^{\prime}(x)=-2(x+1).</equation>从而，<equation>f(x)</equation>在[-2，0]上为<equation>f (x) = \int_ {0} ^ {x} - 2 (t + 1) \mathrm {d} t + f (0) = - x ^ {2} - 2 x = - (x + 1) ^ {2} + 1.</equation>因此，<equation>f(-1)=1</equation>，即<equation>f(7)=1.</equation>

---

**2009年第11题 | 填空题 | 4分**
11.<equation>\lim_{n \to \infty} \int_{0}^{1} \mathrm{e}^{-x} \sin nx \mathrm{d}x=</equation>___
**解析: **解 （法一）由分部积分法，可得<equation>\int_ {0} ^ {1} \mathrm {e} ^ {- x} \sin n x \mathrm {d} x = \int_ {0} ^ {1} \mathrm {e} ^ {- x} \mathrm {d} \left(- \frac {\cos n x}{n}\right) = - \frac {1}{n} \int_ {0} ^ {1} \mathrm {e} ^ {- x} \mathrm {d} (\cos n x) = - \frac {1}{n} \left(\mathrm {e} ^ {- x} \cos n x \mid_ {0} ^ {1} + \int_ {0} ^ {1} \mathrm {e} ^ {- x} \cos n x \mathrm {d} x\right).</equation>当<equation>x\in[0,1]</equation>时，<equation>\mathrm{e}^{-x}\in\left[\frac{1}{\mathrm{e}},1\right],|\cos nx|\leqslant1</equation>从而<equation>\left| \int_ {0} ^ {1} \mathrm {e} ^ {- x} \cos n x \mathrm {d} x \right| \leqslant \int_ {0} ^ {1} | \mathrm {e} ^ {- x} \cos n x | \mathrm {d} x \leqslant \int_ {0} ^ {1} 1 \mathrm {d} x \leqslant 1.</equation>因此，<equation>0 \leqslant \left| \mathrm {e} ^ {- x} \cos n x \right| _ {0} ^ {1} + \int_ {0} ^ {1} \mathrm {e} ^ {- x} \cos n x \mathrm {d} x \leqslant \left| \frac {\cos n}{\mathrm {e}} - 1 \right| + 1 \leqslant 3.</equation>从而<equation>\lim _ {n \rightarrow \infty} \int_ {0} ^ {1} \mathrm {e} ^ {- x} \sin n x \mathrm {d} x = \lim _ {n \rightarrow \infty} \left(- \frac {\mathrm {e} ^ {- x} \cos n x \Big| _ {0} ^ {1} + \int_ {0} ^ {1} \mathrm {e} ^ {- x} \cos n x \mathrm {d} x}{n}\right) \stackrel {\text {分 子 有 界}} {=} 0.</equation>（法二）记<equation>I_{n} = \int_{0}^{1}\mathrm{e}^{-x}\sin nx\mathrm{d}x.</equation>我们可以计算出<equation>I_{n}</equation>的值，再求<equation>\lim_{n\to \infty}I_{n}.</equation><equation>\begin{aligned} I _ {n} &= \int_ {0} ^ {1} \mathrm {e} ^ {- x} \sin n x \mathrm {d} x = - \int_ {0} ^ {1} \sin n x \mathrm {d} \left(\mathrm {e} ^ {- x}\right) = - \mathrm {e} ^ {- x} \sin n x \left| _ {0} ^ {1} + n \int_ {0} ^ {1} \mathrm {e} ^ {- x} \cos n x \mathrm {d} x \right. \\ &= - \mathrm {e} ^ {- x} \sin n x \left| _ {0} ^ {1} - n \mathrm {e} ^ {- x} \cos n x \right| _ {0} ^ {1} - n ^ {2} I _ {n}. \end{aligned}</equation>整理得，<equation>I _ {n} = - \frac {n \cos n + \sin n}{\mathrm {e} \left(n ^ {2} + 1\right)} + \frac {n}{n ^ {2} + 1}.</equation>因此，<equation>\lim _ {n \rightarrow \infty} I _ {n} = \lim _ {n \rightarrow \infty} \left[ - \frac {n \cos n + \sin n}{\mathrm {e} \left(n ^ {2} + 1\right)} + \frac {n}{n ^ {2} + 1} \right] = 0.</equation>

---


#### 变限积分

**2024年第3题 | 选择题 | 5分 | 答案: D**
3. 已知函数<equation>f ( x )=\int_{0}^{\sin x}\sin t^{3}\mathrm{d} t,g ( x )=\int_{0}^{x} f ( t )\mathrm{d} t</equation>，则（    ）

A. f(x)是奇函数，g(x)是奇函数 B. f(x)是奇函数，g(x)是偶函数

C. f(x)是偶函数，g(x)是偶函数 D. f(x)是偶函数，g(x)是奇函数
答案: D
**解析: **解（法一）由于<equation>\sin t^{3}</equation>是奇函数，故由分析中的结论可得<equation>h(x)=\int_{0}^{x}\sin t^{3}\mathrm{d}t</equation>是偶函数，而<equation>f(x)=h(\sin x),</equation><equation>f (- x) = h (\sin (- x)) = h (- \sin x) = h (\sin x) = f (x).</equation>于是，<equation>f(x)</equation>是偶函数.

另一方面，<equation>g ( x )</equation>是<equation>f ( x )</equation>的一个原函数，且<equation>g ( 0 ) = \int_{0}^{0} f ( t ) \mathrm{d} t = 0</equation>，故由分析中的结论可得<equation>g ( x )</equation>是奇函数.

因此，<equation>f ( x )</equation>是偶函数，<equation>g ( x )</equation>是奇函数，应选D.

（法二）首先考察<equation>f(-x).</equation><equation>\begin{aligned} f (- x) &= \int_ {0} ^ {\sin (- x)} \sin t ^ {3} \mathrm {d} t = \int_ {0} ^ {- \sin x} \sin t ^ {3} \mathrm {d} t \xlongequal {u = - t} - \int_ {0} ^ {\sin x} \sin (- u) ^ {3} \mathrm {d} u \\ &= - \int_ {0} ^ {\sin x} \left(- \sin u ^ {3}\right) \mathrm {d} u = \int_ {0} ^ {\sin x} \sin u ^ {3} \mathrm {d} u = f (x). \end{aligned}</equation>于是，<equation>f(x)</equation>是偶函数.

下面考察<equation>g(-x).</equation><equation>g (- x) = \int_ {0} ^ {- x} f (t) \mathrm {d} t \underline {{= u = - t}} - \int_ {0} ^ {x} f (- u) \mathrm {d} u = - \int_ {0} ^ {x} f (u) \mathrm {d} u = - g (x).</equation>于是，<equation>g ( x )</equation>是奇函数.

因此，<equation>f(x)</equation>是偶函数，<equation>g(x)</equation>是奇函数，应选D.

---

**2020年第16题 | 解答题 | 10分**
16. (本题满分10分）

已知函数 f(x)连续且<equation>\lim_{x\rightarrow 0}\frac{f(x)}{x}=1,g(x)=\int_{0}^{1}f(xt)\mathrm{d}t</equation>，求 g'(x)并证明 g'(x)在 x=0处连续.
**答案: **<equation>g ^ {\prime} (x) = \left\{ \begin{array}{l l} \frac {x f (x) - \int_ {0} ^ {x} f (u) \mathrm {d} u}{x ^ {2}}, & x \neq 0, \\ \frac {1}{2}, & x = 0. \end{array} \right. \mathrm {证 明 略}.</equation>
**解析: **解 对 g（x）进行恒等变形.<equation>g (x) = \int_ {0} ^ {1} f (x t) \mathrm {d} t \stackrel {u = x t} {=} \int_ {0} ^ {x} f (u) \cdot \frac {1}{x} \mathrm {d} u = \frac {\int_ {0} ^ {x} f (u) \mathrm {d} u}{x} (x \neq 0).</equation>由<equation>\lim_{x\rightarrow 0}\frac{f(x)}{x}=1</equation>可知，分母趋于零，而极限存在，故<equation>\lim_{x\rightarrow 0}f(x)=0.</equation>又因为 f(x) 连续，所以 f(0) = 0.于是，<equation>g(0)=\int_{0}^{1} f(0)\mathrm{d} t=f(0)=0.</equation>当 x≠0时，<equation>g ^ {\prime} (x) = \frac {\left[ \int_ {0} ^ {x} f (u) \mathrm {d} u \right] ^ {\prime} \cdot x - \int_ {0} ^ {x} f (u) \mathrm {d} u}{x ^ {2}} = \frac {x f (x) - \int_ {0} ^ {x} f (u) \mathrm {d} u}{x ^ {2}}.</equation>当<equation>x=0</equation>时，根据导数的定义计算<equation>g^{\prime}(0).</equation><equation>\begin{aligned} g ^ {\prime} (0) &= \lim _ {x \rightarrow 0} \frac {g (x) - g (0)}{x - 0} = \lim _ {x \rightarrow 0} \frac {\frac {\int_ {0} ^ {x} f (u) \mathrm {d} u}{x} - 0}{x} = \lim _ {x \rightarrow 0} \frac {\int_ {0} ^ {x} f (u) \mathrm {d} u}{x ^ {2}} \\ \underline {{\mathrm {洛 必达}}} \lim _ {x \rightarrow 0} \frac {f (x)}{2 x} &= \frac {1}{2}. \end{aligned}</equation>因此，<equation>g^{\prime}(x)=\left\{ \begin{array}{ll}\frac{x f(x)-\int_{0}^{x} f(u)\mathrm{d} u}{x^{2}},&x\neq 0,\\ \frac{1}{2},&x=0. \end{array} \right.</equation>计算<equation>\lim_{x\to 0}g^{\prime}(x).</equation><equation>\lim _ {x \rightarrow 0} g ^ {\prime} (x) = \lim _ {x \rightarrow 0} \frac {x f (x) - \int_ {0} ^ {x} f (u) \mathrm {d} u}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {f (x)}{x} - \lim _ {x \rightarrow 0} \frac {\int_ {0} ^ {x} f (u) \mathrm {d} u}{x ^ {2}} = 1 - \frac {1}{2} = \frac {1}{2}.</equation>由于<equation>\lim_{x\to 0}g^{\prime}(x)=g^{\prime}(0)</equation>，故<equation>g^{\prime}(x)</equation>在 x=0处连续.

---

**2017年第15题 | 解答题 | 10分**
15. (本题满分10分)
**解析: **解（法一）令<equation>u=x-t</equation>，则<equation>t=x-u,\mathrm{d}u=-\mathrm{d}t,</equation><equation>\int_ {0} ^ {x} \sqrt {x - t} \mathrm {e} ^ {t} \mathrm {d} t = - \int_ {x} ^ {0} \sqrt {u} \mathrm {e} ^ {x - u} \mathrm {d} u = \mathrm {e} ^ {x} \int_ {0} ^ {x} \sqrt {u} \mathrm {e} ^ {- u} \mathrm {d} u.</equation>于是，<equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {x} \int_ {0} ^ {x} \sqrt {u} \mathrm {e} ^ {- u} \mathrm {d} u}{\sqrt {x ^ {3}}} \xlongequal {\lim _ {x \rightarrow 0 ^ {+}} \mathrm {e} ^ {x} = 1} \lim _ {x \rightarrow 0 ^ {+}} \frac {\int_ {0} ^ {x} \sqrt {u} \mathrm {e} ^ {- u} \mathrm {d} u}{\sqrt {x ^ {3}}} \xlongequal {\text {洛 必 达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sqrt {x} \mathrm {e} ^ {- x}}{\frac {3}{2} \sqrt {x}} = \frac {2}{3}.</equation>因此，原极限<equation>= \frac{2}{3}.</equation>（法二）由于<equation>\mathrm{e}^{t}</equation>和<equation>\sqrt{x-t}</equation>均为关于 t的连续函数，且<equation>\sqrt{x-t}</equation>在[0,x]上不变号，故由积分中值定理可得，存在<equation>\xi_{x}\in[0,x]</equation>，使得<equation>\int_ {0} ^ {x} \sqrt {x - t} \mathrm {e} ^ {t} \mathrm {d} t = \mathrm {e} ^ {\xi_ {x}} \int_ {0} ^ {x} \sqrt {x - t} \mathrm {d} t.</equation>因此，<equation>\begin{aligned} \lim _ {x \rightarrow 0 ^ {+}} \frac {\int_ {0} ^ {x} \sqrt {x - t} \mathrm {e} ^ {t} \mathrm {d} t}{\sqrt {x ^ {3}}} &= \lim _ {x \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {\xi_ {x}} \int_ {0} ^ {x} \sqrt {x - t} \mathrm {d} t}{\sqrt {x ^ {3}}} = \lim _ {\substack {x \rightarrow 0 ^ {+} \\ 0 \leqslant \xi_ {x} \leqslant x}} \mathrm {e} ^ {\xi_ {x}} \cdot \lim _ {x \rightarrow 0 ^ {+}} \frac {- \frac {2}{3} (x - t) ^ {\frac {3}{2}} \Big| _ {0} ^ {x}}{\sqrt {x ^ {3}}} \\ &= 1 \cdot \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {2}{3} x ^ {\frac {3}{2}}}{\sqrt {x ^ {3}}} = \frac {2}{3}. \end{aligned}</equation>

---

**2015年第11题 | 填空题 | 4分**
11. 设函数 f(x) 连续，<equation>\varphi(x)=\int_{0}^{x^{2}} x f(t)\mathrm{d} t</equation>. 若<equation>\varphi(1)=1, \varphi^{\prime}(1)=5</equation>，则 f(1) =___
**解析: **解 首先，由于在<equation>\int_{0}^{x^{2}}xf(t)\mathrm{d}t</equation>中，x不再是积分变量，故可将 x作为因子提出放在积分号外，即<equation>\varphi (x) = \int_ {0} ^ {x ^ {2}} x f (t) \mathrm {d} t = x \int_ {0} ^ {x ^ {2}} f (t) \mathrm {d} t.</equation>由求导的乘法法则和变限积分的求导公式可得<equation>\varphi^ {\prime} (x) = \int_ {0} ^ {x ^ {2}} f (t) \mathrm {d} t + x f \left(x ^ {2}\right) \cdot 2 x.</equation>由<equation>\varphi(1)=1</equation>可得<equation>\varphi(1)=\int_{0}^{1} f(t)\mathrm{d} t=1</equation>；由<equation>\varphi^{\prime}(1)=5</equation>可得<equation>\varphi^{\prime}(1)=\int_{0}^{1} f(t)\mathrm{d} t+2f(1)=5.</equation>因此，<equation>f(1)=\frac{\varphi^{\prime}(1)-\varphi(1)}{2}=2.</equation>

---

**2013年第3题 | 选择题 | 4分 | 答案: C**
3. 设函数 f(x) =<equation>\left\{\begin{array}{l l} \sin x, & 0 \leqslant x < \pi, \\ 2, & \pi \leqslant x \leqslant 2 \pi, \end{array} \right.</equation>F(x) =<equation>\int_{0}^{x} f(t)\mathrm{d}t</equation>，则（    ）

A. x=<equation>\pi</equation>是函数 F(x)的跳跃间断点 B. x=<equation>\pi</equation>是函数 F(x)的可去间断点

C. F(x)在 x=<equation>\pi</equation>处连续但不可导 D. F(x)在 x=<equation>\pi</equation>处可导
答案: C
**解析: **解（法一）由于<equation>f ( x )</equation>有界且只有一个跳跃间断点，故<equation>f ( x )</equation>可积，而<equation>F ( x ) = \int_{0}^{x} f ( t ) \mathrm{d} t</equation>，于是 F(x)连续.另一方面，由于<equation>x=\pi</equation>是f(x)的跳跃间断点，故F(x)在<equation>x=\pi</equation>处不可导.应选C.

（法二）在<equation>[0,\pi)</equation>上，<equation>F (x) = \int_ {0} ^ {x} \sin t \mathrm {d} t = \left(- \cos t\right) \Bigg | _ {0} ^ {x} = - \cos x + 1.</equation>在<equation>[\pi ,2\pi ]</equation>上，<equation>F (x) = \int_ {0} ^ {\pi} \sin t \mathrm {d} t + \int_ {\pi} ^ {x} 2 \mathrm {d} t = 2 + 2 (x - \pi).</equation>因此，<equation>F (x) = \left\{ \begin{array}{l l} - \cos x + 1, & 0 \leqslant x < \pi , \\ 2 (x + 1 - \pi), & \pi \leqslant x \leqslant 2 \pi . \end{array} \right.</equation>由于<equation>\lim _ {x \rightarrow \pi^ {-}} F (x) = \lim _ {x \rightarrow \pi^ {-}} (- \cos x + 1) = 2, \quad \lim _ {x \rightarrow \pi^ {+}} F (x) = \lim _ {x \rightarrow \pi^ {+}} 2 (x + 1 - \pi) = 2,</equation>且由<equation>F(x)</equation>的定义可得<equation>F(\pi) = 2</equation>，故<equation>F(x)</equation>在<equation>x = \pi</equation>处连续.

由于<equation>F _ {-} ^ {\prime} (\pi) = \lim _ {x \rightarrow \pi^ {-}} \frac {F (\pi) - F (x)}{\pi - x} = \lim _ {x \rightarrow \pi^ {-}} \frac {2 - 1 + \cos x}{\pi - x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow \pi^ {-}} \frac {- \sin x}{- 1} = 0,</equation><equation>F _ {+} ^ {\prime} (\pi) = \lim _ {x \rightarrow \pi^ {+}} \frac {F (x) - F (\pi)}{x - \pi} = \lim _ {x \rightarrow \pi^ {+}} \frac {2 (x + 1 - \pi) - 2}{x - \pi} = 2,</equation>故<equation>F_{-}^{\prime}(\pi)\neq F_{+}^{\prime}(\pi), F(x)</equation>在<equation>x=\pi</equation>处不可导.应选C.

---

**2009年第6题 | 选择题 | 4分 | 答案: D**
6. 设函数 y=f(x)在区间[-1,3]上的图形如图所示，则函数<equation>F ( x )=\int_{0}^{x} f ( t ) \mathrm{d} t</equation>的图形为（    ）

A.

B.

C.

D.
答案: D
**解析: **解（法一）我们可以从<equation>f(x)</equation>出发具体分析<equation>F(x)</equation>的性质.

因为 f(x) 分段连续，所以由变上限积分函数的性质可知，在[-1，0），（0，2），（2，3]上，均有<equation>F^{\prime}(x)=f(x).</equation><equation>\textcircled{1}</equation>由于 f(x)在[-1,3]上有界且只有两个间断点，故 f(x)可积.又因为<equation>F(x)=\int_{0}^{x} f(t)\mathrm{d}t</equation>所以 F(x)连续.<equation>\textcircled{2}</equation>在[-1,0）上，<equation>f ( x ) > 0</equation>，故 F(x)单调增加；在（0，1）上，<equation>f ( x ) < 0</equation>，故 F(x)单调减少；在（1，2）上，<equation>f ( x ) > 0</equation>，故 F(x)单调增加；在（2，3]上，<equation>f ( x ) = 0</equation>，故 F(x)为常函数.<equation>\textcircled{3} F ( 0 )=\int_{0}^{0} f ( t ) \mathrm{d} t=0.</equation>在<equation>[-1,1]</equation>上，<equation>F ( x )</equation>均小于等于零.<equation>\textcircled{4}</equation><equation>f(1) = 0, x = 1</equation>为<equation>F(x)</equation>的驻点及极小值点.

同时满足以上要求的图形只有选项D. 应选D.

（法二）通过图形考察<equation>f(x)</equation>在<equation>[-1,0)</equation>上的性质，可知当<equation>x\in[-1,0)</equation>时，<equation>f(x)\equiv 1</equation>，故<equation>F (- 1) = \int_ {0} ^ {- 1} 1 \mathrm {d} x = - 1, \quad F (0) = \int_ {0} ^ {0} 1 \mathrm {d} x = 0,</equation>从而可排除选项A和选项C.

又由于 f(x)在[-1，3]上有界且只有两个间断点，f(x)在[-1，3]上可积，而 F(x) =<equation>\int_{0}^{x} f(t)\mathrm{d} t</equation>，故 F(x)必连续，从而可以排除选项B.

综上所述，应选D.

---


#### 不定积分的计算

**2023年第2题 | 选择题 | 5分 | 答案: D**

2. 函数 f(x) =<equation>\left\{\begin{array}{l l}{\frac{1}{\sqrt{1+x^{2}}},}&{x\leqslant0}\\ {(x+1)\cos x,}&{x>0}\end{array} \right.</equation>的一个原函数为（    )

A. F(x) =<equation>\left\{\begin{array}{l l}{\ln(\sqrt{1+x^{2}}-x),}&{x\leqslant0}\\ {(x+1)\cos x-\sin x,}&{x>0}\end{array} \right.</equation>B. F(x) =<equation>\left\{\begin{array}{l l}{\ln(\sqrt{1+x^{2}}-x)+1,}&{x\leqslant0}\\ {(x+1)\cos x-\sin x,}&{x>0}\end{array} \right.</equation>C. F(x) =<equation>\left\{\begin{array}{l l}{\ln(\sqrt{1+x^{2}}+x),}&{x\leqslant0}\\ {(x+1)\sin x+\cos x,}&{x>0}\end{array} \right.</equation>D. F(x) =<equation>\left\{\begin{array}{l l}{\ln(\sqrt{1+x^{2}}+x)+1,}&{x\leqslant0}\\ {(x+1)\sin x+\cos x,}&{x>0}\end{array} \right.</equation>

答案: D

**解析:**解（法一）首先，由于 F(x）是 f(x)的原函数，故必连续，而四个选项中的 F(x)均为分段函数，于是我们可以分别考察 F(x)在分界点处的连续性.

对选项 A,<equation>\lim_{x\rightarrow 0^{-}}F(x)=0, \lim_{x\rightarrow 0^{+}}F(x)=1. F(x)</equation>不连续.

对选项B，<equation>\lim_{x\to 0^{-}}F(x)=\lim_{x\to 0^{+}}F(x)=1=F(0).F(x)</equation>连续.

对选项 C<equation>\lim_{x\to 0^{-}}F(x)=0,\lim_{x\to 0^{+}}F(x)=1. F(x)</equation>不连续.

对选项 D<equation>\lim_{x\to 0^{-}}F(x)=\lim_{x\to 0^{+}}F(x)=1=F(0). F(x)</equation>连续.

由上可排除选项A与选项C.

选项B与选项D的差别在于函数表达式.<equation>[ (x + 1) \cos x - \sin x ] ^ {\prime} = \cos x - (x + 1) \sin x - \cos x = - (x + 1) \sin x,</equation><equation>[ (x + 1) \sin x + \cos x ] ^ {\prime} = \sin x + (x + 1) \cos x - \sin x = (x + 1) \cos x.</equation>由上可排除选项B.

因此，应选D.

（法二）当<equation>x\leqslant0</equation>时，<equation>\begin{aligned} F (x) &= \int \frac {\mathrm {d} x}{\sqrt {1 + x ^ {2}}} \xlongequal {x = \tan \theta} \int \frac {\sec^ {2} \theta}{\sec \theta} \mathrm {d} \theta = \int \sec \theta \mathrm {d} \theta = \ln | \sec \theta + \tan \theta | + C _ {1} \\ \frac {x = \tan \theta}{2} \ln \left(\sqrt {1 + x ^ {2}} + x\right) + C _ {1}. \end{aligned}</equation>当 x > 0时，<equation>\begin{aligned} F (x) &= \int (x + 1) \cos x \mathrm {d} x = \int (x + 1) \mathrm {d} (\sin x) = (x + 1) \sin x - \int \sin x \mathrm {d} x \\ &= (x + 1) \sin x + \cos x + C _ {2}. \end{aligned}</equation>四个选项中，仅有选项C、D符合要求.

由于 F(x）是 f(x)在<equation>(-\infty, +\infty)</equation>上的一个原函数，故 F(x)在 x=0处连续.<equation>\lim _ {x \rightarrow 0 ^ {-}} F (x) = \lim _ {x \rightarrow 0 ^ {-}} \left[ \ln \left(\sqrt {1 + x ^ {2}} + x\right) + C _ {1} \right] = C _ {1},</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} F (x) = \lim _ {x \rightarrow 0 ^ {+}} \left[ (x + 1) \sin x + \cos x + C _ {2} \right] = C _ {2} + 1.</equation>由<equation>\lim_{x\to 0^{-}}F(x) = \lim_{x\to 0^{+}}F(x)</equation>可得<equation>C_1 = C_2 + 1.</equation>选项C中，<equation>C_{1}=C_{2}=0,F(x)</equation>不连续，选项D中，<equation>C_{1}=1,C_{2}=0,F(x)</equation>连续，应选D.

---

**2019年第16题 | 解答题 | 10分**

16. (本题满分10分)

求不定积分<equation>\frac {3 x + 6}{(x - 1) ^ {2} \left(x ^ {2} + x + 1\right)} \mathrm {d} x.</equation>

**答案:**-2ln<equation>| x-1 |-\frac{3}{x-1}+\ln( x^{2}+x+1 )+C</equation>，其中C为任意常数.

**解析:**解设<equation>\frac {3 x + 6}{(x - 1) ^ {2} \left(x ^ {2} + x + 1\right)} = \frac {A _ {1}}{x - 1} + \frac {A _ {2}}{(x - 1) ^ {2}} + \frac {B _ {1} x + B _ {2}}{x ^ {2} + x + 1}.</equation>通分并整理可得，<equation>\frac {3 x + 6}{(x - 1) ^ {2} \left(x ^ {2} + x + 1\right)} = \frac {\left(A _ {1} + B _ {1}\right) x ^ {3} + \left(A _ {2} - 2 B _ {1} + B _ {2}\right) x ^ {2} + \left(A _ {2} + B _ {1} - 2 B _ {2}\right) x + \left(- A _ {1} + A _ {2} + B _ {2}\right)}{(x - 1) ^ {2} \left(x ^ {2} + x + 1\right)}.</equation>比较<equation>x^{3}, x^{2}, x</equation>的系数以及常数项可得，<equation>\left[ A _ {1} + B _ {1} = 0, \right.</equation><equation>\left| A _ {2} - 2 B _ {1} + B _ {2} = 0, \right.</equation><equation>A _ {2} + B _ {1} - 2 B _ {2} = 3,</equation><equation>- A _ {1} + A _ {2} + B _ {2} = 6.</equation>由（1）式可得<equation>- A_{1}=B_{1}.</equation>代入（4）式可得<equation>A _ {2} + B _ {1} + B _ {2} = 6.</equation>(5) 式与（3）式相减，可得<equation>3 B_{2}=3</equation>即<equation>B_{2}=1.</equation>分别代入（2）式与（3）式，可解得<equation>A_{2}=3,B_{1}=2.</equation>从而<equation>A_{1}=-2.</equation>因此，<equation>\frac {3 x + 6}{(x - 1) ^ {2} \left(x ^ {2} + x + 1\right)} = \frac {- 2}{x - 1} + \frac {3}{(x - 1) ^ {2}} + \frac {2 x + 1}{x ^ {2} + x + 1}.</equation><equation>\begin{aligned} \int \frac {3 x + 6}{(x - 1) ^ {2} \left(x ^ {2} + x + 1\right)} \mathrm {d} x &= \int \left[ \frac {- 2}{x - 1} + \frac {3}{(x - 1) ^ {2}} + \frac {2 x + 1}{x ^ {2} + x + 1} \right] \mathrm {d} x \\ &= \int \frac {- 2}{x - 1} \mathrm {d} x + \int \frac {3}{(x - 1) ^ {2}} \mathrm {d} x + \int \frac {2 x + 1}{x ^ {2} + x + 1} \mathrm {d} x \\ &= - 2 \ln | x - 1 | - \frac {3}{x - 1} + \int \frac {\mathrm {d} \left(x ^ {2} + x + 1\right)}{x ^ {2} + x + 1} \\ \stackrel {*} {=} - 2 \ln | x - 1 | - \frac {3}{x - 1} + \ln \left(x ^ {2} + x + 1\right) + C, \end{aligned}</equation>其中 C为任意常数.

---

**2018年第15题 | 解答题 | 10分**

15. (本题满分10分)

求不定积分

**答案:**<equation>\frac{\mathrm{e}^{2x}\arctan \sqrt{\mathrm{e}^{x} - 1}}{2} -\frac{1}{6}\left(\mathrm{e}^{x} - 1\right)^{\frac{3}{2}} - \frac{1}{2}\sqrt{\mathrm{e}^{x} - 1} + C</equation>，其中C为任意常数.

**解析:**解 利用分部积分法.<equation>\begin{aligned} \int \mathrm {e} ^ {2 x} \arctan \sqrt {\mathrm {e} ^ {x} - 1} \mathrm {d} x \xlongequal {\text {分 部 积 分}} \frac {1}{2} \int \arctan \sqrt {\mathrm {e} ^ {x} - 1} \mathrm {d} \left(\mathrm {e} ^ {2 x}\right) \\ &= \frac {\mathrm {e} ^ {2 x}}{2} \cdot \arctan \sqrt {\mathrm {e} ^ {x} - 1} - \frac {1}{2} \int \mathrm {e} ^ {2 x} \cdot \frac {1}{1 + \mathrm {e} ^ {x} - 1} \cdot \frac {\mathrm {e} ^ {x}}{2 \sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x \\ &= \frac {\mathrm {e} ^ {2 x} \arctan \sqrt {\mathrm {e} ^ {x} - 1}}{2} - \frac {1}{4} \int \frac {\mathrm {e} ^ {2 x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x. \end{aligned}</equation>下面用两种方法计算<equation>\int \frac{\mathrm{e}^{2 x}}{\sqrt{\mathrm{e}^{x}-1}}\mathrm{d}x.</equation>（法一）令<equation>u=\sqrt{\mathrm{e}^{x}-1}</equation>，则<equation>x=\ln \left(u^{2}+1\right)</equation>，<equation>\mathrm{d}x=\frac{2u}{u^{2}+1}\mathrm{d}u.</equation><equation>\begin{aligned} \int \frac {\mathrm {e} ^ {2 x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x &= \int \frac {\left(u ^ {2} + 1\right) ^ {2}}{u} \cdot \frac {2 u}{u ^ {2} + 1} \mathrm {d} u = 2 \int \left(u ^ {2} + 1\right) \mathrm {d} u = \frac {2}{3} u ^ {3} + 2 u + C _ {1} \\ &= \frac {2}{3} \left(\mathrm {e} ^ {x} - 1\right) ^ {\frac {3}{2}} + 2 \sqrt {\mathrm {e} ^ {x} - 1} + C _ {1}, \end{aligned}</equation>其中<equation>C_{1}</equation>为任意常数.

（法二）令<equation>t=\mathrm{e}^{x}</equation>，则<equation>\mathrm{d}t=\mathrm{e}^{x}\mathrm{d}x.</equation><equation>\begin{aligned} \int \frac {\mathrm {e} ^ {2 x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x &= \int \frac {\mathrm {e} ^ {x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} \left(\mathrm {e} ^ {x}\right) = \int \frac {t}{\sqrt {t - 1}} \mathrm {d} t = \int \frac {t - 1 + 1}{\sqrt {t - 1}} \mathrm {d} t \\ &= \int \left(\sqrt {t - 1} + \frac {1}{\sqrt {t - 1}}\right) \mathrm {d} t = \frac {2}{3} (t - 1) ^ {\frac {3}{2}} + 2 \sqrt {t - 1} + C _ {1} \\ &= \frac {2}{3} \left(\mathrm {e} ^ {x} - 1\right) ^ {\frac {3}{2}} + 2 \sqrt {\mathrm {e} ^ {x} - 1} + C _ {1}, \end{aligned}</equation>其中<equation>C_{1}</equation>为任意常数.

因此，<equation>\text {原 积 分} = \frac {\mathrm {e} ^ {2 x} \arctan \sqrt {\mathrm {e} ^ {x} - 1}}{2} - \frac {1}{6} \left(\mathrm {e} ^ {x} - 1\right) ^ {\frac {3}{2}} - \frac {1}{2} \sqrt {\mathrm {e} ^ {x} - 1} + C,</equation>其中 C为任意常数.

---

**2016年第2题 | 选择题 | 4分 | 答案: D**

2. 已知函数<equation>f ( x )=\left\{\begin{array}{l l}2 ( x-1 ),&x<1,\\\ln x,&x\geqslant 1,\end{array} \right.</equation>则 f(x)的一个原函数是（    )

A.<equation>F ( x )=\left\{\begin{array}{l l} ( x-1 )^{2},&x<1,\\x(\ln x-1),&x\geqslant 1.\end{array} \right.</equation>B.<equation>F ( x )=\left\{\begin{array}{l l} ( x-1 )^{2},&x<1,\\x(\ln x+1)-1,&x\geqslant 1.\end{array} \right.</equation>C.<equation>F ( x )=\left\{\begin{array}{l l} ( x-1 )^{2},&x<1,\\x(\ln x+1)+1,&x\geqslant 1.\end{array} \right.</equation>D.<equation>F ( x )=\left\{\begin{array}{l l} ( x-1 )^{2},&x<1,\\x(\ln x-1)+1,&x\geqslant 1.\end{array} \right.</equation>

答案: D

**解析:**解 （法一）当 x < 1时，<equation>F (x) = \int 2 (x - 1) \mathrm {d} x = (x - 1) ^ {2} + C _ {1};</equation>当 x≥1时，<equation>F (x) = \int \ln x \mathrm {d} x = x (\ln x - 1) + C _ {2},</equation>其中<equation>C_{1}, C_{2}</equation>均为任意常数.

进一步，由于 F(x）是 f(x)在<equation>(-\infty, +\infty)</equation>上的一个原函数，故 F(x)在 x=1处应连续.<equation>\lim _ {x \rightarrow 1 ^ {-}} F (x) = \lim _ {x \rightarrow 1 ^ {-}} \left(x - 1\right) ^ {2} + C _ {1} = C _ {1}, \quad \lim _ {x \rightarrow 1 ^ {+}} F (x) = \lim _ {x \rightarrow 1 ^ {+}} x (\ln x - 1) + C _ {2} = C _ {2} - 1.</equation>若 F(x) 连续，则<equation>C_{1}=C_{2}-1.</equation>选项D中，<equation>C_{1}=0,C_{2}=1,F(x)</equation>连续，应选D.

（法二）首先，由于 F(x）是 f(x)的原函数，必连续，而四个选项中的 F(x)均是分段函数，故我们可以分别考察 F(x)在分界点处的连续性.

选项A：<equation>\lim_{x\to 1^{-}}F(x)=0</equation><equation>\lim_{x\to 1^{+}}F(x)=-1.</equation>不连续.

选项B：<equation>\lim_{x\to 1^{-}}F(x)=0</equation><equation>\lim_{x\to 1^{+}}F(x)=0.</equation>连续.

选项C：<equation>\lim_{x\to 1^{-}}F(x)=0</equation><equation>\lim_{x\to 1^{+}}F(x)=2.</equation>不连续.

选项D：<equation>\lim_{x\to 1^{-}}F(x)=0</equation><equation>\lim_{x\to 1^{+}}F(x)=0.</equation>连续.

由上可排除选项A与选项C.

选项B与选项D的差别在于函数表达式.

计算 f（x）在<equation>[ 1,+\infty)</equation>上的原函数，得<equation>\int f (x) \mathrm {d} x = \int \ln x \mathrm {d} x = x (\ln x - 1) + C,</equation>其中 C为任意常数.比较（1）式与选项B、选项D，可排除选项B.应选D.

---

**2009年第16题 | 解答题 | 10分**

16. (本题满分10分)

计算不定积分<equation>\int\ln\left(1+\sqrt{\frac{1+x}{x}}\right)\mathrm{d}x(x>0).</equation>

**答案:**(16)<equation>x \ln \left( 1+\sqrt{\frac{1+x}{x}} \right)+\frac{1}{2} \ln \left( \sqrt{1+x}+\sqrt{x} \right)-\frac{\sqrt{x}}{2(\sqrt{1+x}+\sqrt{x})}-C</equation>，其中C为任意常数.

**解析:**解（法一）令<equation>u=\sqrt{\frac{1+x}{x}}</equation>，则<equation>x=\frac{1}{u^{2}-1}.</equation>于是，<equation>\int \ln \left(1 + \sqrt {\frac {1 + x}{x}}\right) \mathrm {d} x = \int \ln (1 + u) \mathrm {d} \left(\frac {1}{u ^ {2} - 1}\right) = \frac {\ln (1 + u)}{u ^ {2} - 1} - \int \frac {1}{\left(u ^ {2} - 1\right) \left(u + 1\right)} \mathrm {d} u.</equation>计算<equation>\int \frac{1}{(u^{2}-1)(u+1)} \mathrm{d} u.</equation><equation>\begin{aligned} \int \frac {1}{\left(u ^ {2} - 1\right) (u + 1)} \mathrm {d} u &= \frac {1}{2} \int \frac {(u + 1) - (u - 1)}{\left(u ^ {2} - 1\right) (u + 1)} \mathrm {d} u = \frac {1}{2} \left[ \int \frac {1}{u ^ {2} - 1} \mathrm {d} u - \int \frac {1}{(u + 1) ^ {2}} \mathrm {d} u \right] \\ &= \frac {1}{4} \int \left(\frac {1}{u - 1} - \frac {1}{u + 1}\right) \mathrm {d} u - \frac {1}{2} \int \frac {1}{(u + 1) ^ {2}} \mathrm {d} u = \frac {1}{4} \ln \frac {u - 1}{u + 1} + \frac {1}{2 (u + 1)} + C, \end{aligned}</equation>其中 C为任意常数.这里的<equation>\ln \frac{u - 1}{u + 1}</equation>没有绝对值符号，是因为<equation>u = \sqrt{\frac{1 + x}{x}} > 1.</equation>将 u =<equation>\sqrt{\frac{1+x}{x}}</equation>代回原积分，得<equation>\begin{aligned} \mathrm {原 积 分} &= \frac {\ln (1 + u)}{u ^ {2} - 1} + \frac {1}{4} \ln \frac {u + 1}{u - 1} - \frac {1}{2 (u + 1)} - C \\ \frac {u = \sqrt {\frac {1 + x}{x}}}{x \ln \left(1 + \sqrt {\frac {1 + x}{x}}\right)} + \frac {1}{2} \ln \left(\sqrt {1 + x} + \sqrt {x}\right) - \frac {\sqrt {x}}{2 \left(\sqrt {1 + x} + \sqrt {x}\right)} - C, \end{aligned}</equation>其中 C为任意常数.

（法二）使用待定系数法来求<equation>\int \frac{1}{(u^2 - 1)(u + 1)}\mathrm{d}u.</equation><equation>\begin{aligned} \frac {1}{\left(u ^ {2} - 1\right) (u + 1)} &= \frac {a}{u - 1} + \frac {b}{u + 1} + \frac {c}{(u + 1) ^ {2}} = \frac {a (u + 1) ^ {2} + b (u - 1) (u + 1) + c (u - 1)}{(u - 1) (u + 1) ^ {2}} \\ &= \frac {(a + b) u ^ {2} + (2 a + c) u + a - b - c}{(u - 1) (u + 1) ^ {2}}. \end{aligned}</equation>比较<equation>u^{2}</equation>，<equation>u</equation>的系数以及常数项，可得<equation>\left\{ \begin{array}{l l} a + b = 0, \\ 2a + c = 0, \\ a - b - c = 1, \end{array} \right.</equation>解得<equation>a = \frac{1}{4}, b = -\frac{1}{4}, c = -\frac{1}{2}</equation>.

因此，<equation>\int \frac{1}{(u^{2}-1)(u+1)} \mathrm{d} u=\frac{1}{4} \int \left[ \frac{1}{u-1}-\frac{1}{u+1}-\frac{2}{(u+1)^{2}} \right] \mathrm{d} u=\frac{1}{4} \left( \ln \frac{u-1}{u+1}+\frac{2}{u+1} \right)+C</equation>其中C为任意常数.

其余同法一.

---


#### 一元函数积分学综合题

**2018年第16题 | 解答题 | 10分**
16. (本题满分10分)

已知连续函数 f(x)满足<equation>\int_{0}^{x} f(t)\mathrm{d} t+\int_{0}^{x} t f(x-t)\mathrm{d} t=a x^{2}.</equation>I. 求 f(x);

II. 若 f(x)在区间[0,1]上的平均值为1，求 a的值.
**答案: **( I )<equation>f ( x ) = 2 a \left( 1 - \mathrm{e}^{-x} \right)</equation>;

( II )<equation>a = \frac{\mathrm{e}}{2}.</equation>
**解析: **解（I）令<equation>u=x-t</equation>，则

于是，<equation>\int_{0}^{x}tf(x - t)\mathrm{d}t = \int_{x}^{0}(x - u)f(u)\mathrm{d}(x - u) = \int_{0}^{x}(x - u)f(u)\mathrm{d}u = x\int_{0}^{x}f(u)\mathrm{d}u - \int_{0}^{x}uf(u)\mathrm{d}u.</equation><equation>\int_ {0} ^ {x} f (t) \mathrm {d} t + \int_ {0} ^ {x} t f (x - t) \mathrm {d} t = \int_ {0} ^ {x} f (t) \mathrm {d} t + x \int_ {0} ^ {x} f (t) \mathrm {d} t - \int_ {0} ^ {x} t f (t) \mathrm {d} t = a x ^ {2}.</equation>对<equation>\int_{0}^{x} f(t)\mathrm{d} t+x\int_{0}^{x} f(t)\mathrm{d} t-\int_{0}^{x} t f(t)\mathrm{d} t=a x^{2}</equation>两端关于 x求导，可得<equation>f (x) + \int_ {0} ^ {x} f (t) \mathrm {d} t + x f (x) - x f (x) = 2 a x,</equation>即<equation>f (x) + \int_ {0} ^ {x} f (t) \mathrm {d} t = 2 a x.</equation>由（1）式可知，<equation>f ( x )=2 a x-\int_{0}^{x} f ( t ) \mathrm{d} t</equation>，而 f(x) 连续，故<equation>\int_{0}^{x} f ( t ) \mathrm{d} t</equation>可导，从而 f(x) 可导.

对（1）式两端关于 x求导，可得<equation>f ^ {\prime} (x) + f (x) = 2 a.</equation>这是一个一阶非齐次线性微分方程. 由求解公式可得，<equation>f (x) = \mathrm {e} ^ {- \int \mathrm {d} x} \left(\int 2 a \cdot \mathrm {e} ^ {\int \mathrm {d} x} \mathrm {d} x + C\right) = \mathrm {e} ^ {- x} \left(2 a \mathrm {e} ^ {x} + C\right) = 2 a + C \mathrm {e} ^ {- x},</equation>其中 C为待定常数.

在（1）式中，令 x=0，可得 f(0)=0.将 x=0，f(0)=0代入 f(x）=2a+C<equation>\mathrm{e}^{-x}</equation>可得，0=2a+C，即 C=-2a.

因此，<equation>f ( x ) = 2 a \left( 1 - \mathrm{e}^{-x} \right).</equation>（Ⅱ）根据平均值的定义，<equation>\frac{\int_{0}^{1} f(x)\mathrm{d} x}{1-0}=1</equation>即<equation>\int_{0}^{1} f(x)\mathrm{d} x=1.</equation>由于<equation>\int_ {0} ^ {1} f (x) \mathrm {d} x = \int_ {0} ^ {1} 2 a \left(1 - \mathrm {e} ^ {- x}\right) \mathrm {d} x = 2 a + 2 a \mathrm {e} ^ {- x} \Bigg | _ {0} ^ {1} = 2 a \mathrm {e} ^ {- 1},</equation>故<equation>2a\mathrm{e}^{-1} = 1.</equation>解得<equation>a = \frac{\mathrm{e}}{2}.</equation>因此，<equation>a=\frac{\mathrm{e}}{2}.</equation>

---

**2016年第21题 | 解答题 | 11分**
21. (本题满分11分)

已知函数 f(x)在<equation>\left[ 0, \frac{3\pi}{2} \right]</equation>上连续，在<equation>\left( 0, \frac{3\pi}{2} \right)</equation>内是函数<equation>\frac{\cos x}{2x-3\pi}</equation>的一个原函数，且 f(0)=0.

I. 求 f(x)在区间<equation>\left[ 0, \frac{3\pi}{2} \right]</equation>上的平均值；

II. 证明 f(x)在区间<equation>\left( 0, \frac{3\pi}{2} \right)</equation>内存在唯一零点
**答案: **（I）平均值为<equation>\frac{1}{3\pi}</equation>；

（Ⅱ）证明略.
**解析: **解（I）由于 f(x）是<equation>\frac{\cos x}{2x-3\pi}</equation>的一个原函数，故不妨设 f(x)<equation>= \int_{0}^{x}\frac{\cos t}{2t-3\pi}\mathrm{d}t+C.</equation>由 f(0) = 0可知，C=0.于是，<equation>f(x)=\int_{0}^{x}\frac{\cos t}{2t-3\pi}\mathrm{d}t.</equation>根据 f(x)在区间<equation>\left[0,\frac{3\pi}{2}\right]</equation>上的平均值的定义，可知<equation>A = \frac {\int_ {0} ^ {\frac {3 \pi}{2}} f (x) \mathrm {d} x}{\frac {3 \pi}{2}} = \frac {\int_ {0} ^ {\frac {3 \pi}{2}} \left(\int_ {0} ^ {x} \frac {\cos t}{2 t - 3 \pi} \mathrm {d} t\right) \mathrm {d} x}{\frac {3 \pi}{2}}.</equation>（法一）我们可以使用分部积分法来处理（1）式中的<equation>\int_{0}^{\frac{3\pi}{2}} f(x)\mathrm{d}x.</equation>由上可知，<equation>f^{\prime}(x) = \frac{\cos x}{2x - 3\pi}.</equation>记<equation>I = \int_{0}^{\frac{3\pi}{2}} f(x)\mathrm{d}x</equation>，则<equation>\begin{aligned} I &= \frac {1}{2} \int_ {0} ^ {\frac {3 \pi}{2}} f (x) \mathrm {d} (2 x - 3 \pi) = \frac {1}{2} f (x) (2 x - 3 \pi) \left| _ {0} ^ {\frac {3 \pi}{2}} - \frac {1}{2} \int_ {0} ^ {\frac {3 \pi}{2}} (2 x - 3 \pi) \mathrm {d} [ f (x) ] \right. \\ &= - \frac {1}{2} \int_ {0} ^ {\frac {3 \pi}{2}} (2 x - 3 \pi) \cdot f ^ {\prime} (x) \mathrm {d} x = - \frac {1}{2} \int_ {0} ^ {\frac {3 \pi}{2}} \cos x \mathrm {d} x = \frac {1}{2}. \end{aligned}</equation>因此，<equation>A=\frac{\frac{1}{2}}{\frac{3\pi}{2}}=\frac{1}{3\pi}.</equation>（法二）（1）式右端分式中的分子为一个二次积分.由于被积函数是仅关于 t的函数，故我们不妨交换积分次序，先关于 x积分，再关于 t积分.

该二次积分对应的二重积分的积分区域为<equation>D = \left\{(x, t) \mid 0 \leqslant t \leqslant x, 0 \leqslant x \leqslant \frac {3 \pi}{2} \right\}.</equation>将区域 D写成 Y型区域，得<equation>D = \left\{(x, t) \mid t \leqslant x \leqslant \frac {3 \pi}{2}, 0 \leqslant t \leqslant \frac {3 \pi}{2} \right\}.</equation>因此，<equation>\begin{aligned} A &= \frac {\int_ {0} ^ {\frac {3 \pi}{2}} \left(\int_ {0} ^ {x} \frac {\cos t}{2 t - 3 \pi} \mathrm {d} t\right) \mathrm {d} x}{\frac {3 \pi}{2}} = \frac {\int_ {0} ^ {\frac {3 \pi}{2}} \frac {\cos t}{2 t - 3 \pi} \mathrm {d} t \int_ {t} ^ {\frac {3 \pi}{2}} \mathrm {d} x}{\frac {3 \pi}{2}} = \frac {\int_ {0} ^ {\frac {3 \pi}{2}} \frac {\cos t}{2 t - 3 \pi} \left(\frac {3 \pi}{2} - t\right) \mathrm {d} t}{\frac {3 \pi}{2}} \\ &= - \frac {1}{3 \pi} \int_ {0} ^ {\frac {3 \pi}{2}} \cos t \mathrm {d} t = \frac {1}{3 \pi}. \end{aligned}</equation>（Ⅱ）<equation>f^{\prime}(x)=\frac{\cos x}{2x-3\pi}.</equation>由于在<equation>\left(0,\frac{3\pi}{2}\right)</equation>内，<equation>2x-3\pi < 0</equation>，而在<equation>\left(0,\frac{\pi}{2}\right)</equation>内，<equation>\cos x > 0</equation>；在<equation>\left(\frac{\pi}{2},\frac{3\pi}{2}\right)</equation>内，<equation>\cos x < 0</equation>，故在<equation>\left(0,\frac{\pi}{2}\right)</equation>内，<equation>f^{\prime}(x) < 0</equation>，f(x)单调减少，在<equation>\left(\frac{\pi}{2},\frac{3\pi}{2}\right)</equation>内，<equation>f^{\prime}(x) > 0</equation>，f(x)单调增加.

由于<equation>f ( 0 )=0</equation>，而 f(x)在<equation>\left( 0,\frac{\pi}{2} \right)</equation>内单调减少，故<equation>f\left(\frac{\pi}{2}\right)<0</equation>，f(x)在<equation>\left( 0,\frac{\pi}{2} \right)</equation>内无零点.

若<equation>f\left(\frac{3\pi}{2}\right)>0</equation>，则由连续函数的零点定理以及单调性可知，f(x)在<equation>\left(\frac{\pi}{2},\frac{3\pi}{2}\right)</equation>内存在唯一零点.
