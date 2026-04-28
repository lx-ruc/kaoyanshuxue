A. f(x) = |x|<equation>\sin|x|</equation>B. f(x) = |x|<equation>\sin\sqrt{|x|}</equation>C. f(x) =<equation>\cos|x|</equation>D. f(x) =<equation>\cos\sqrt{|x|}</equation>
答案: D
**解析: **解 考虑选项 D.<equation>f (x) = \left\{ \begin{array}{l l} \cos \sqrt {x}, & x \geqslant 0, \\ \cos \sqrt {- x}, & x < 0. \end{array} \right.</equation><equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {\cos \sqrt {- x} - 1}{x - 0} \frac {\cos \sqrt {- x} - 1 \sim - \frac {\left(\sqrt {- x}\right) ^ {2}}{2}}{\lim _ {x \rightarrow 0 ^ {-}} \frac {x}{x}} = \frac {1}{2},</equation><equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {\cos \sqrt {x} - 1}{x - 0} \frac {\cos \sqrt {x} - 1 \sim - \frac {(\sqrt {x}) ^ {2}}{2}}{\lim _ {x \rightarrow 0 ^ {+}} \frac {- \frac {x}{2}}{x}} = - \frac {1}{2}.</equation>由于<equation>f_{-}^{\prime}(0)\neq f_{+}^{\prime}(0)</equation>，故<equation>f(x)=\cos \sqrt{|x|}</equation>在 x=0处不可导.应选D.

下面分别说明选项A、B、C不正确.

选项A：<equation>f ( x )=\left\{\begin{array}{l l}x \sin x,\\-x \sin(-x),\end{array}\right.</equation><equation>x \geqslant0</equation>又因为<equation>-x \sin(-x)=-x\cdot(-\sin x)=x \sin x</equation>，所以<equation>x<0.</equation><equation>f ( x )=x \sin x,f ( x )</equation>在 x=0处可导.

选项B：<equation>f ( x )=\left\{\begin{array}{ll}x\sin \sqrt{x},&x\geqslant 0,\\ -x\sin \sqrt{-x},&x<0.\end{array} \right.</equation><equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {- x \sin \sqrt {- x} - 0}{x - 0} = \lim _ {x \rightarrow 0 ^ {-}} (- \sin \sqrt {- x}) = 0,</equation><equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {x \sin \sqrt {x} - 0}{x - 0} = \lim _ {x \rightarrow 0 ^ {+}} \sin \sqrt {x} = 0.</equation>由于<equation>f_{-}^{\prime}(0)=f_{+}^{\prime}(0)</equation>，故<equation>f(x)=|x|\sin \sqrt{|x|}</equation>在 x=0处可导.

选项C：<equation>f ( x )=\left\{\begin{array}{ll}\cos x,&x\geqslant0,\\ \cos(-x),&x<0.\end{array} \right.</equation>又因为<equation>\cos(-x)=\cos x</equation>，所以<equation>f ( x )=\cos x,f ( x )</equation>在 x=0处可导.

---

**2015年第3题 | 选择题 | 4分 | 答案: A**
3. 设函数 f(x) =<equation>\left\{\begin{array}{l l}{x^{\alpha}\cos \frac{1}{x^{\beta}},}&{x>0,\\0,&x\leqslant 0}\end{array} \right.</equation>（<equation>\alpha>0,\beta>0</equation>）. 若 f'(x)在 x=0处连续，则（    )

A.<equation>\alpha-\beta>1</equation>B. 0 <<equation>\alpha-\beta\leqslant1</equation>C.<equation>\alpha-\beta>2</equation>D. 0 <<equation>\alpha-\beta\leqslant2</equation>
答案: A
**解析: **解 首先求<equation>f^{\prime}(0).</equation>根据导数的定义，<equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {f (x) - f (0)}{x - 0} = 0, \quad f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0 ^ {+}} \left(x ^ {\alpha - 1} \cos \frac {1}{x ^ {\beta}}\right).</equation>由于<equation>f^{\prime}(x)</equation>在<equation>x=0</equation>处连续，故<equation>f^{\prime}(0)</equation>存在，从而<equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \left(x ^ {\alpha - 1} \cos \frac {1}{x ^ {\beta}}\right) = 0 = f _ {-} ^ {\prime} (0).</equation>由于当<equation>\beta > 0</equation>时，<equation>\cos \frac{1}{x^{\beta}}</equation>有界但<equation>\lim_{x\to 0^{+}}\cos \frac{1}{x^{\beta}}</equation>不存在，故<equation>\lim_{x\to 0^{+}}\left(x^{\alpha -1}\cos \frac{1}{x^{\beta}}\right)=0</equation>当且仅当<equation>\alpha >1.</equation>由上可知，当<equation>\alpha >1</equation>时，<equation>f^{\prime}(0)=0.</equation>还需要再检查<equation>\lim_{x\to 0}f^{\prime}(x)=f^{\prime}(0)=0</equation>成立的条件.

当<equation>x \leqslant 0</equation>时，<equation>f(x)\equiv 0</equation>，故当<equation>x < 0</equation>时，<equation>f^{\prime}(x)\equiv 0</equation>，从而<equation>\lim_{x\to 0^{-}}f^{\prime}(x) = 0.</equation>当 x > 0时，<equation>f ^ {\prime} (x) = \alpha x ^ {\alpha - 1} \cos \frac {1}{x ^ {\beta}} + x ^ {\alpha} \left(- \sin \frac {1}{x ^ {\beta}}\right) (- \beta) \frac {1}{x ^ {\beta + 1}} = \alpha x ^ {\alpha - 1} \cos \frac {1}{x ^ {\beta}} + \beta x ^ {\alpha - \beta - 1} \sin \frac {1}{x ^ {\beta}}.</equation>由于<equation>\alpha >1</equation>，故<equation>\lim _ {x \rightarrow 0 ^ {+}} \left(\alpha x ^ {\alpha - 1} \cos \frac {1}{x ^ {\beta}} + \beta x ^ {\alpha - \beta - 1} \sin \frac {1}{x ^ {\beta}}\right) = \lim _ {x \rightarrow 0 ^ {+}} \left(\beta x ^ {\alpha - \beta - 1} \sin \frac {1}{x ^ {\beta}}\right).</equation>由于当<equation>\beta > 0</equation>时，<equation>\sin \frac{1}{x^{\beta}}</equation>有界但<equation>\lim_{x\to 0^{+}}\sin \frac{1}{x^{\beta}}</equation>不存在，故<equation>\lim_{x\to 0^{+}}\left(\beta x^{\alpha -\beta -1}\sin \frac{1}{x^{\beta}}\right)=0</equation>当且仅当<equation>\alpha -\beta -1 > 0</equation>即<equation>\alpha -\beta >1.</equation>联立<equation>\left\{ \begin{array}{l l} \alpha >1, \\ \alpha -\beta -1 > 0, \\ \alpha >0,\beta >0, \end{array} \right.</equation>可得<equation>\alpha -\beta -1 > 0.</equation>应选A.

---

**2013年第2题 | 选择题 | 4分 | 答案: A**
2. 设函数 y=f(x)由方程<equation>\cos(xy)+\ln y-x=1</equation>确定，则<equation>\lim_{n\rightarrow \infty}n\left[ f\left( \frac{2}{n}\right)-1\right] =</equation>(    )

A.2 B.1 C.-1 D.-2
答案: A
**解析: **解 将<equation>x = 0</equation>代入方程<equation>\cos (xy) + \ln y - x = 1</equation>可得，<equation>f(0) = 1.</equation>对方程<equation>\cos ( x y )+\ln y-x=1</equation>两端关于 x求导可得<equation>- \sin (x y) \cdot \left(y + x y ^ {\prime}\right) + \frac {y ^ {\prime}}{y} - 1 = 0.</equation>代入<equation>x = 0,f(0) = 1</equation>，可得<equation>f^{\prime}(0) = 1.</equation>由导数的定义可得，<equation>\lim _ {n \rightarrow \infty} n \left[ f \left(\frac {2}{n}\right)-1 \right] = 2 \lim _ {n \rightarrow \infty} \frac {f \left(\frac {2}{n}\right)-1}{\frac {2}{n}} = 2 \lim _ {n \rightarrow \infty} \frac {f \left(\frac {2}{n}\right)-f (0)}{\frac {2}{n}-0} = 2 f ^ {\prime} (0) = 2.</equation>应选A.

---

**2011年第2题 | 选择题 | 4分 | 答案: B**
2. 设函数 f(x)在 x=0处可导，且 f(0)=0，则<equation>\lim_{x\rightarrow 0}\frac{x^{2}f(x)-2f\left(x^{3}\right)}{x^{3}}=</equation>(    )

A.<equation>-2f^{\prime}(0)</equation>B.<equation>-f^{\prime}(0)</equation>C.<equation>f^{\prime}(0)</equation>D. 0
答案: B
**解析: **解 （法一）利用导数的定义来求极限.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {x ^ {2} f (x) - 2 f \left(x ^ {3}\right)}{x ^ {3}} &= \lim _ {x \rightarrow 0} \left[ \frac {f (x)}{x} - \frac {2 f \left(x ^ {3}\right)}{x ^ {3}} \right] \xlongequal {f (0) = 0} \lim _ {x \rightarrow 0} \left[ \frac {f (x) - f (0)}{x - 0} - 2 \cdot \frac {f \left(x ^ {3}\right) - f (0)}{x ^ {3} - 0} \right] \\ &= \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0} - 2 \lim _ {x \rightarrow 0} \frac {f \left(x ^ {3}\right) - f (0)}{x ^ {3} - 0} = f ^ {\prime} (0) - 2 f ^ {\prime} (0) = - f ^ {\prime} (0). \end{aligned}</equation>应选B.

（法二）分别写出<equation>f(x)</equation>与<equation>f(x^{3})</equation>在<equation>x=0</equation>处的一阶泰勒公式.<equation>f (x) = f (0) + f ^ {\prime} (0) x + o (x) \stackrel {f (0) = 0} {=} f ^ {\prime} (0) x + o (x),</equation><equation>f \left(x ^ {3}\right) = f (0) + f ^ {\prime} (0) x ^ {3} + o \left(x ^ {3}\right) \stackrel {f (0) = 0} {=} f ^ {\prime} (0) x ^ {3} + o \left(x ^ {3}\right).</equation>代入所求极限得<equation>\lim _ {x \rightarrow 0} \frac {x ^ {2} f (x) - 2 f \left(x ^ {3}\right)}{x ^ {3}} = \lim _ {x \rightarrow 0} \frac {f ^ {\prime} (0) x ^ {3} - 2 f ^ {\prime} (0) x ^ {3} + o \left(x ^ {3}\right)}{x ^ {3}} = - f ^ {\prime} (0).</equation>应选B.

---


#### 导数与微分的计算

**2025年第14题 | 填空题 | 5分**
14. 已知函数 y=y(x)由<equation>\left\{\begin{array}{l l}x=\ln(1+2t)\\ 2t-\int_{1}^{y+t^{2}}\mathrm{e}^{-u^{2}}\mathrm{d}u=0\end{array}\right.</equation>确定，则<equation>\left.\frac{\mathrm{d} y}{\mathrm{d} x}\right|_{t=0}=</equation>___
**解析: **解 对<equation>x = \ln (1 + 2t)</equation>关于<equation>t</equation>求导可得<equation>\frac{\mathrm{d}x}{\mathrm{d}t} = \frac{2}{1 + 2t}</equation>，于是<equation>\frac{\mathrm{d}x}{\mathrm{d}t}\bigg|_{t = 0} = \frac{2}{1 + 2t}\bigg|_{t = 0} = 2</equation>.

在<equation>2t - \int_{1}^{y + t^2}\mathrm{e}^{-u^2}\mathrm{d}u = 0</equation>中令<equation>t = 0</equation>，可得<equation>\int_{1}^{y}\mathrm{e}^{-u^2}\mathrm{d}u = 0</equation>. 由于<equation>\mathrm{e}^{-u^2} > 0</equation>，故<equation>\int_{1}^{y}\mathrm{e}^{-u^2}\mathrm{d}u = 0</equation>当且仅当<equation>y = 1</equation>，从而<equation>y(t)\big|_{t = 0} = 1</equation>.

对<equation>2t - \int_{1}^{y + t^2}\mathrm{e}^{-u^2}\mathrm{d}u = 0</equation>两端关于<equation>t</equation>求导可得<equation>2 - \mathrm{e}^{-(y + t^2)^2}\left(\frac{\mathrm{d}y}{\mathrm{d}t} + 2t\right) = 0. \tag{1}</equation>在(1)式中令<equation>t = 0</equation>可得<equation>2 - \mathrm{e}^{-1}\frac{\mathrm{d}y}{\mathrm{d}t}\bigg|_{t = 0} = 0</equation>，解得<equation>\frac{\mathrm{d}y}{\mathrm{d}t}\bigg|_{t = 0} = 2\mathrm{e}</equation>.

因此，<equation>\frac{\mathrm{d}y}{\mathrm{d}x}\bigg|_{t = 0} = \frac{2\mathrm{e}}{2} = \mathrm{e}</equation>.

---

**2024年第14题 | 填空题 | 5分**
14. 已知函数<equation>f(x)=x^{2}\left(\mathrm{e}^{x}+1\right)</equation>, 则<equation>f^{(5)}(1)=</equation>___.
**答案: **## 31e
**解析: **解记<equation>u ( x )=\mathrm{e}^{x}+1, v ( x )=x^{2}</equation>，则当 k≥1时，<equation>u^{(k)}(x)=\mathrm{e}^{x}, v^{\prime}(x)=2 x, v^{\prime \prime}(x)=2</equation>，当 k≥ 3时，<equation>v^{(k)}(x)=0</equation>.由莱布尼茨公式可得，<equation>f^{(5)}(x)=\mathrm{C}_{5}^{0} u^{(5)}(x) v(x)+\mathrm{C}_{5}^{1} u^{(4)}(x) v^{\prime}(x)+\mathrm{C}_{5}^{2} u^{(3)}(x) v^{\prime \prime}(x)</equation><equation>=\mathrm{e}^{x}\cdot x^{2}+5\cdot\mathrm{e}^{x}\cdot 2 x+1 0\cdot\mathrm{e}^{x}\cdot 2=(x^{2}+1 0 x+2 0)\mathrm{e}^{x}.</equation>当 x=1时，<equation>f^{(5)}(1)=\left[ \left(x^{2}+1 0 x+2 0\right) \mathrm{e}^{x}\right] \bigg|_{x=1}=3 1 \mathrm{e}.</equation>

---

**2022年第12题 | 填空题 | 5分**
12. 已知函数<equation>y=y(x)</equation>由方程<equation>x^{2}+xy+y^{3}=3</equation>确定，则<equation>y^{\prime\prime}(1)=</equation>___
**答案: **# -<equation>\frac{31}{32}.</equation>
**解析: **解 将 x=1代入原方程可得，<equation>1+y+y^{3}=3</equation>，即<equation>y^{3}+y-2=0</equation>. 通过观察可得 y=1是该方程的一个解. 令<equation>f(y)=y^{3}+y-2</equation>，则<equation>f^{\prime}(y)=3y^{2}+1>0</equation>，f(y)为单调增加函数，从而 y=1为<equation>y^{3}+y-2=0</equation>的唯一解.

对<equation>x^{2}+ x y+ y^{3}=3</equation>两端关于 x求导可得，<equation>2 x + y + x y ^ {\prime} + 3 y ^ {2} y ^ {\prime} = 0, \quad \mathrm {即} 2 x + y + \left(x + 3 y ^ {2}\right) y ^ {\prime} = 0.</equation>代入 x=1,y（1）=1可得<equation>3+4 y^{\prime}(1)=0</equation>.解得<equation>y^{\prime}(1)=-\frac{3}{4}.</equation>对（1）式两端再次关于 x求导可得，<equation>2 + y ^ {\prime} + \left(1 + 6 y y ^ {\prime}\right) y ^ {\prime} + \left(x + 3 y ^ {2}\right) y ^ {\prime \prime} = 0.</equation>代入<equation>x=1,y(1)=1,y^{\prime}(1)=-\frac{3}{4}</equation>可得<equation>\frac{31}{8}+4y^{\prime \prime}(1)=0.</equation>解得<equation>y^{\prime \prime}(1)=-\frac{31}{32}.</equation>

---

**2021年第12题 | 填空题 | 5分**
12. 设函数<equation>y=y(x)</equation>由参数方程<equation>\left\{ \begin{array}{l} x = 2 \mathrm {e} ^ {t} + t + 1 \\ y = 4 (t - 1) \mathrm {e} ^ {t} + t ^ {2} \end{array} \right.</equation>确定，则<equation>\left.\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}\right|_{t=0}=</equation>___
**解析: **解 根据由参数方程确定的函数的导数计算公式，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {4 \mathrm {e} ^ {t} + 4 (t - 1) \mathrm {e} ^ {t} + 2 t}{2 \mathrm {e} ^ {t} + 1} = \frac {4 t \mathrm {e} ^ {t} + 2 t}{2 \mathrm {e} ^ {t} + 1} = 2 t.</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\mathrm {d} \left(\frac {\mathrm {d} y}{\mathrm {d} x}\right)}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {2}{2 \mathrm {e} ^ {t} + 1}.</equation>代入<equation>t = 0</equation>，可得<equation>\frac{\mathrm{d}^2y}{\mathrm{d}x^2}\bigg|_{t = 0} = \frac{2}{3}</equation>.

---

**2020年第4题 | 选择题 | 4分 | 答案: A**
4. 已知函数<equation>f ( x )=x^{2} \ln(1-x)</equation>，当<equation>n\geqslant 3</equation>时，<equation>f^{(n)}(0)=</equation>（    ）

A.<equation>-\frac{n!}{n-2}</equation>B.<equation>\frac{n!}{n-2}</equation>C.<equation>-\frac{(n-2)!}{n}</equation>D.<equation>\frac{(n-2)!}{n}</equation>
答案: A
**解析: **解（法一）记<equation>u ( x )=\ln( 1-x)</equation><equation>v ( x )=x^{2}</equation>，则<equation>f ( x )=u ( x ) v ( x )</equation>，从而可以用莱布尼茨公式来计算 f(x)的高阶导数.

由于<equation>f ^ {(n)} (0) = (u v) ^ {(n)} (0) = \sum_ {k = 0} ^ {n} C _ {n} ^ {k} u ^ {(n - k)} (0) v ^ {(k)} (0),</equation>而<equation>v^{\prime \prime}(0)=2,v^{(k)}(0)=0(k\neq 2)</equation>，故<equation>f ^ {(n)} (0) = 2 \mathrm {C} _ {n} ^ {2} \left[ \ln (1 - x) \right] ^ {(n - 2)} (0) = n (n - 1) \left[ \ln (1 - x) \right] ^ {(n - 2)} (0).</equation>下面利用逐次求导的方法计算<equation>\ln(1-x)</equation>在 x=0处的的 n-2阶导数.<equation>[ \ln (1 - x) ] ^ {\prime} = - \frac {1}{1 - x} = (- 1) \cdot (1 - x) ^ {- 1},</equation><equation>[ \ln (1 - x) ] ^ {\prime \prime} = (- 1) ^ {2} \cdot (- 1) \cdot (1 - x) ^ {- 2},</equation><equation>[ \ln (1 - x) ] ^ {(3)} = (- 1) ^ {3} \cdot (- 1) \cdot (- 2) \cdot (1 - x) ^ {- 3},</equation>由数学归纳法可知，<equation>[\ln(1 - x)]^{(n)} = (-1)^{n}\cdot(-1)^{n - 1}(n - 1)!(1 - x)^{-n} = -(n - 1)!(1 - x)^{-n}.</equation>于是，<equation>[\ln(1 - x)]^{(n - 2)} = -(n - 3)!(1 - x)^{-(n - 2)}.</equation>令<equation>x=0</equation>，可得<equation>[\ln(1-x)]^{(n-2)}(0)=-(n-3)!</equation>代入（1）式可得，<equation>f ^ {(n)} (0) = n (n - 1) \cdot [ - (n - 3)! ] = - \frac {n !}{n - 2}.</equation>因此，应选A.

（法二）由于<equation>\ln(1-x)</equation>的麦克劳林级数为<equation>-\sum_{n=1}^{\infty}\frac{x^{n}}{n}</equation>，故<equation>x^{2}\ln(1-x)</equation>的麦克劳林级数为<equation>-\sum_{n=1}^{\infty}\frac{x^{n+2}}{n}.x^{n}</equation>的系数为<equation>-\frac{1}{n-2}.</equation>又因为 f(x)的麦克劳林级数中，<equation>x^{n}</equation>的系数为<equation>\frac{f^{(n)}(0)}{n!}</equation>所以<equation>\frac{f^{(n)}(0)}{n!}=-\frac{1}{n-2}, f^{(n)}(0)=-\frac{n!}{n-2}.</equation>因此，应选A.

---

**2020年第9题 | 填空题 | 4分**
9.<equation>\left\{ \begin{array}{l l} x = \sqrt {t ^ {2} + 1} \\ y = \ln (t + \sqrt {t ^ {2} + 1}) \end{array} \right. \quad \mathrm {则} \left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {t = 1} = \underline {{\quad}}</equation>
**解析: **解 根据由参数方程确定的函数的求导公式，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {1 + \frac {t}{\sqrt {t ^ {2} + 1}}}{t + \sqrt {t ^ {2} + 1}} / \frac {t}{\sqrt {t ^ {2} + 1}} = \frac {1}{\sqrt {t ^ {2} + 1}} / \frac {t}{\sqrt {t ^ {2} + 1}} = \frac {1}{t}.</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\mathrm {d} \left(\frac {\mathrm {d} y}{\mathrm {d} x}\right)}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = - \frac {1}{t ^ {2}} / \frac {t}{\sqrt {t ^ {2} + 1}} = - \frac {\sqrt {t ^ {2} + 1}}{t ^ {3}}.</equation>代入 t=1，可得<equation>\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}} \Bigg|_{t=1}=-\sqrt{2}.</equation>

---

**2017年第10题 | 填空题 | 4分**
10. 设函数 y=y(x)由参数方程<equation>\left\{ \begin{array}{l} x = t + \mathrm {e} ^ {t} \\ y = \sin t \end{array} \right.</equation><equation>\left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {t = 0} = \underline {{}}</equation>
**答案: **# -<equation>\frac{1}{8}.</equation>
**解析: **解 根据由参数方程确定的函数的求导公式，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {\cos t}{1 + \mathrm {e} ^ {t}},</equation><equation>\begin{aligned} \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} &= \frac {\mathrm {d} \left[ y ^ {\prime} (x) \right]}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {\frac {\mathrm {d} \left(\frac {\cos t}{1 + \mathrm {e} ^ {t}}\right)}{\mathrm {d} t}}{1 + \mathrm {e} ^ {t}} = \frac {\frac {- \sin t \left(1 + \mathrm {e} ^ {t}\right) - \cos t \mathrm {e} ^ {t}}{\left(1 + \mathrm {e} ^ {t}\right) ^ {2}}}{1 + \mathrm {e} ^ {t}} \\ &= \frac {- \sin t \left(1 + \mathrm {e} ^ {t}\right) - \cos t \mathrm {e} ^ {t}}{\left(1 + \mathrm {e} ^ {t}\right) ^ {3}}. \end{aligned}</equation>当<equation>t = 0</equation>时，<equation>\frac{\mathrm{d}^2y}{\mathrm{d}x^2}\bigg|_{t = 0} = -\frac{1}{8}.</equation>或者也可以这样计算<equation>\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}</equation>由于<equation>x^{\prime}(t) = 1 + \mathrm{e}^{t}, x^{\prime \prime}(t) = \mathrm{e}^{t}, y^{\prime}(t) = \cos t, y^{\prime \prime}(t) = -\sin t</equation>，故<equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {y ^ {\prime \prime} (t) x ^ {\prime} (t) - y ^ {\prime} (t) x ^ {\prime \prime} (t)}{\left[ x ^ {\prime} (t) \right] ^ {3}} = \frac {- \sin t \left(1 + \mathrm {e} ^ {t}\right) - \cos t \mathrm {e} ^ {t}}{\left(1 + \mathrm {e} ^ {t}\right) ^ {3}}.</equation>

---

**2016年第12题 | 填空题 | 4分**
12. 已知函数 f(x)在<equation>(-\infty,+\infty)</equation>上连续，且<equation>f(x)=(x+1)^{2}+2\int_{0}^{x} f(t)\mathrm{d}t</equation>，则当 n≥2时，<equation>f^{(n)}(0)=</equation>___
**答案: **5·2<equation>^{n-1}</equation>
**解析: **解 （法一）逐次求导.

虽然条件中仅给出了 f(x)的连续性，但由<equation>f ( x )=( x+1 )^{2}+2 \int_{0}^{x} f ( t ) \mathrm{d} t</equation>知，f(x）可导.由于<equation>f^{\prime}(x)=2(x+1)+2 f(x)</equation>，故<equation>f^{\prime}(x)</equation>也可导，从而可推出 f(x)为 n阶可导函数（n为任意正整数）.<equation>\begin{aligned} f ^ {\prime} (x) &= 2 (x + 1) + 2 f (x), \\ f ^ {\prime \prime} (x) &= 2 + 2 f ^ {\prime} (x), \\ f ^ {(3)} (x) &= 2 f ^ {\prime \prime} (x), \\ f ^ {(4)} (x) &= \left[ f ^ {(3)} (x) \right] ^ {\prime} = \left[ 2 f ^ {\prime \prime} (x) \right] ^ {\prime} = 2 f ^ {(3)} (x) = 2 ^ {2} f ^ {\prime \prime} (x), \\ \dots \\ \mathrm {即} f ^ {(n)} (x) &= 2 ^ {n - 2} f ^ {\prime \prime} (x), n \geqslant 2. \end{aligned}</equation>由数学归纳法可知<equation>f^{(n)}(x)=2^{n-2} f^{\prime \prime}(x), n\geqslant 2.</equation>当 x=0时，<equation>f(0)=1,f^{\prime}(0)=2+2f(0)=4,f^{\prime\prime}(0)=2+2\times 4=10.</equation>因此，<equation>f^{(n)}(0) = 2^{n - 2}\cdot 10 = 5\cdot 2^{n - 1}, n\geqslant 2.</equation>（法二）先求出<equation>f(x)</equation>的表达式，再计算其导数.

当 x=0时，由已知等式易求得<equation>f(0)=1.</equation>对已知等式两端关于 x求导，得<equation>f^{\prime}(x)=2(x+1)+2 f(x)</equation>，即<equation>f^{\prime}(x)-2 f(x)=2(x+1).</equation>这是一个一阶非齐次线性微分方程.

由求解公式，得<equation>\begin{aligned} f (x) &= C \mathrm {e} ^ {\int 2 \mathrm {d} x} + \mathrm {e} ^ {\int 2 \mathrm {d} x} \int \mathrm {e} ^ {\int (- 2) \mathrm {d} x} \cdot 2 (x + 1) \mathrm {d} x = C \mathrm {e} ^ {2 x} + \mathrm {e} ^ {2 x} \int \mathrm {e} ^ {- 2 x} \cdot 2 (x + 1) \mathrm {d} x \\ &= C \mathrm {e} ^ {2 x} - x - \frac {3}{2}. \end{aligned}</equation>代入<equation>f ( 0 )=1</equation>得，<equation>C=\frac{5}{2}.</equation>因此，<equation>f ( x )=\frac{5}{2}\mathrm{e}^{2 x}-x-\frac{3}{2}.</equation>对<equation>f ( x )</equation>逐次求导，可得<equation>f^{(n)}(x)=\frac{5}{2}\cdot 2^{n}\cdot \mathrm{e}^{2x},</equation><equation>n\geqslant 2.</equation>代入<equation>x = 0</equation>，得<equation>f^{(n)}(0) = 5\cdot 2^{n - 1}, n\geqslant 2.</equation>

---

**2015年第9题 | 填空题 | 4分**
9. 设<equation>\begin{aligned} x &= \arctan t \\ y &= 3 t + t ^ {3} \end{aligned}</equation><equation>\text {则} \left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {t = 1} = \underline {{}}</equation>
**答案: **## 48.
**解析: **解 根据由参数方程确定的函数的求导公式，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {3 t ^ {2} + 3}{\frac {1}{t ^ {2} + 1}} = 3 \left(t ^ {2} + 1\right) ^ {2},</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\mathrm {d} \left[ y ^ {\prime} (x) \right]}{\mathrm {d} t} \Bigg / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {6 \left(t ^ {2} + 1\right) \cdot 2 t}{\frac {1}{t ^ {2} + 1}} = 1 2 t \left(t ^ {2} + 1\right) ^ {2}.</equation>代入<equation>t = 1</equation>，得<equation>\frac{\mathrm{d}^2y}{\mathrm{d}x^2}\bigg|_{t = 1} = 12\times 4 = 48.</equation>

---

**2015年第10题 | 填空题 | 4分**
10. 函数<equation>f(x) = x^2 2^x</equation>在<equation>x = 0</equation>处的<equation>n</equation>阶导数<equation>f^{(n)}(0) =</equation>___
**答案: **n(n-1)<equation>(\ln 2)^{n-2}.</equation>
**解析: **解记<equation>u ( x )=2^{x},</equation><equation>v ( x )=x^{2}</equation>，则<equation>f ( x )=u ( x ) v ( x )</equation>，从而可以用莱布尼茨公式来计算<equation>f ( x )</equation>的高阶导数.

由于<equation>f ^ {(n)} (0) = (u v) ^ {(n)} (0) = \sum_ {k = 0} ^ {n} \mathrm {C} _ {n} ^ {k} u ^ {(n - k)} (0) v ^ {(k)} (0)</equation>而<equation>v^{\prime \prime}(0) = 2,v^{(k)}(0) = 0(k\neq 2)</equation>，故<equation>f ^ {(n)} (0) = 2 \mathrm {C} _ {n} ^ {2} \left(2 ^ {x}\right) ^ {(n - 2)} (0) = n (n - 1) (\ln 2) ^ {n - 2}.</equation>

---

**2013年第10题 | 填空题 | 4分**
10. 设函数<equation>f ( x )=\int_{-1}^{x}\sqrt{1-\mathrm{e}^{t}}\mathrm{d} t</equation>，则 y=f(x)的反函数<equation>x=f^{-1} ( y )</equation>在 y=0处的导数<equation>\left.\frac{\mathrm{d} x}{\mathrm{d} y}\right|_{y=0}=</equation>___
**解析: **解 因为<equation>f ( x )=\int_{-1}^{x}\sqrt{1-\mathrm{e}^{t}}\mathrm{d} t</equation>，而被积函数<equation>\sqrt{1-\mathrm{e}^{t}}\geqslant 0</equation>，所以当且仅当<equation>x=-1</equation>时，<equation>y = f (x) = \int_ {- 1} ^ {x} \sqrt {1 - \mathrm {e} ^ {t}} \mathrm {d} t = 0,</equation>即<equation>f^{-1}(0)=-1.</equation>由于<equation>f^{\prime}(-1)=\sqrt{1-\mathrm{e}^{x}} \Bigg|_{x=-1}=\sqrt{1-\frac{1}{\mathrm{e}}}</equation>，故<equation>\left[ f ^ {- 1} (y) \right] ^ {\prime} \Big | _ {y = 0} = \frac {1}{f ^ {\prime} (- 1)} = \frac {1}{\sqrt {1 - \frac {1}{e}}} = \sqrt {\frac {e}{e - 1}}.</equation>

---

**2012年第2题 | 选择题 | 4分 | 答案: A**
2. 设函数<equation>f(x)=\mathrm{e}^{x}-1)(\mathrm{e}^{2x}-2)\cdots(\mathrm{e}^{nx}-n)</equation>，其中 n为正整数，则<equation>f^{\prime}(0)=</equation>(    )

A.<equation>(-1)^{n-1}(n-1)!</equation>B.<equation>(-1)^{n}(n-1)!</equation>C.<equation>(-1)^{n-1}n!</equation>D.<equation>(-1)^{n}n!</equation>
答案: A
**解析: **解（法一）利用求导的乘法法则来计算<equation>f^{\prime}(0)</equation>.

令<equation>g ( x ) = \left( \mathrm{e}^{2 x}-2 \right) \dots \left( \mathrm{e}^{n x}-n \right)</equation>，则<equation>f ( x ) = \left( \mathrm{e}^{x}-1 \right) g ( x )</equation>.由求导的乘法法则可得，<equation>f ^ {\prime} (x) = \mathrm {e} ^ {x} g (x) + \left(\mathrm {e} ^ {x} - 1\right) g ^ {\prime} (x).</equation>由于<equation>\mathrm{e}^{0}-1=0</equation>，故<equation>f ^ {\prime} (0) = \mathrm {e} ^ {0} g (0) = (- 1) (- 2) \dots [ - (n - 1) ] = (- 1) ^ {n - 1} (n - 1)!</equation>因此，应选A.

（法二）从导数的定义出发来计算<equation>f^{\prime}(0)</equation>.

由于 f（0）=0，故<equation>\begin{aligned} f ^ {\prime} (0) &= \lim _ {x \rightarrow 0} \frac {f (x) - f (0)}{x - 0} = \lim _ {x \rightarrow 0} \frac {f (x)}{x} = \lim _ {x \rightarrow 0} \frac {\left(\mathrm {e} ^ {x} - 1\right)\left(\mathrm {e} ^ {2 x} - 2\right) \dots \left(\mathrm {e} ^ {n x} - n\right)}{x} \\ \underline {{\mathrm {e} ^ {x} - 1 \sim x}} \lim _ {x \rightarrow 0} \left[ \left(\mathrm {e} ^ {2 x} - 2\right) \dots \left(\mathrm {e} ^ {n x} - n\right)\right] \cdot 1 &= (- 1) (- 2) \dots [ - (n - 1) ] \cdot 1 \\ &= (- 1) ^ {n - 1} (n - 1)!. \end{aligned}</equation>因此，应选A.

（法三）排除法.

我们可以尝试代入 n值，排除不符合题意的选项.由于当 n=2时，四个选项的取值均不同，故可选择 n=2.

当<equation>n = 2</equation>时，<equation>f(x) = \left(\mathrm{e}^{x} - 1\right)\left(\mathrm{e}^{2x} - 2\right), f^{\prime}(0) = -1</equation>，故可排除选项B、C、D.

因此，应选A.

---

**2012年第9题 | 填空题 | 4分**
9. 设 y=y(x) 是由方程<equation>x^{2}-y+1=\mathrm{e}^{y}</equation>所确定的隐函数，则<equation>\left.\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\right|_{x=0}=</equation>___
**解析: **<equation>x^{2}-y+1=\mathrm{e}^{y}</equation>可得，<equation>y(0)=0.</equation>对原方程两端关于 x 求导，可得<equation>2 x-y^{\prime}=\mathrm{e}^{y} y^{\prime}</equation>代入<equation>x=0,y(0)=0</equation>，可得<equation>-y^{\prime}(0)=y^{\prime}(0)</equation>即<equation>y^{\prime}(0)=0.</equation>对<equation>2 x-y^{\prime}=\mathrm{e}^{y} y^{\prime}</equation>两端关于 x求导，可得<equation>2-y^{\prime \prime}=\mathrm{e}^{y}\left(y^{\prime}\right)^{2}+\mathrm{e}^{y} y^{\prime \prime}.</equation>代入<equation>x=0,y(0)=0</equation><equation>y^{\prime}(0)=0</equation>，得<equation>2-y^{\prime \prime}(0)=y^{\prime \prime}(0).</equation>因此，<equation>y^{\prime \prime}(0) = 1.</equation>

---

**2010年第11题 | 填空题 | 4分**
11. 函数<equation>y = \ln(1 - 2x)</equation>在<equation>x = 0</equation>处的<equation>n</equation>阶导数<equation>y^{(n)}(0) =</equation>___
**答案: **- 2<equation>^{n}</equation>(n-1) !.
**解析: **解 利用链式法则对 y逐次求各阶导数，可得<equation>y ^ {\prime} = \frac {- 2}{1 - 2 x} = - 2 \left(1 - 2 x\right) ^ {- 1},</equation><equation>y ^ {\prime \prime} = (- 2) ^ {2} (- 1) (1 - 2 x) ^ {- 2}.</equation>由数学归纳法，可证明<equation>\begin{aligned} y ^ {(n)} &= (- 2) ^ {n} (- 1) (- 2) \dots [ - (n - 1) ] (1 - 2 x) ^ {- n} \\ &= - 2 ^ {n} (n - 1)! (1 - 2 x) ^ {- n}. \end{aligned}</equation>当<equation>x = 0</equation>时，<equation>y^{(n)}(0) = -2^{n}(n - 1)!.</equation>

---

**2009年第12题 | 填空题 | 4分**
12. 设 y=y(x) 是由方程<equation>x y+\mathrm{e}^{y}=x+1</equation>确定的隐函数，则<equation>\left.\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\right|_{x=0}=</equation>___
**解析: **由<equation>xy + \mathrm{e}^{y} = x + 1</equation>知，当<equation>x = 0</equation>时，<equation>y = 0</equation>，即<equation>y(0) = 0.</equation>对原方程两端关于 x求导，得<equation>y + x y ^ {\prime} + \mathrm {e} ^ {y} y ^ {\prime} = 1.</equation>代入<equation>x = 0, y(0) = 0</equation>得，<equation>y^{\prime}(0) = 1.</equation>继续对（1）式两端关于 x求导，得<equation>y ^ {\prime} + x y ^ {\prime \prime} + y ^ {\prime} + \mathrm {e} ^ {y} \left(y ^ {\prime}\right) ^ {2} + \mathrm {e} ^ {y} y ^ {\prime \prime} = 0.</equation>代入<equation>x = 0, y(0) = 0, y^{\prime}(0) = 1</equation>得，<equation>y^{\prime \prime}(0) = -3.</equation>

---


#### 微分中值定理

**2025年第21题 | 解答题 | 12分**
21. (本题满分12分）

设函数 f(x)在区间（a,b）内可导，证明导函数<equation>f^{\prime}(x)</equation>在（a,b）内严格单调增加的充分必要条件是：对（a,b）内任意的<equation>x_{1},x_{2},x_{3}</equation>，当<equation>x_{1}<x_{2}<x_{3}</equation>时，有<equation>\frac{f(x_{2})-f(x_{1})}{x_{2}-x_{1}}<\frac{f(x_{3})-f(x_{2})}{x_{3}-x_{2}}.</equation>
**解析: **证 先证明必要性.

对<equation>(a,b)</equation>内任意的<equation>x_{1}, x_{2}, x_{3}</equation>，当<equation>x_{1} < x_{2} < x_{3}</equation>时，由拉格朗日中值定理可得存在<equation>\xi_{1}\in (x_{1}, x_{2})</equation><equation>\xi_{2}\in (x_{2}, x_{3})</equation>，使得<equation>f^{\prime}(\xi_{1}) = \frac{f(x_{2}) - f(x_{1})}{x_{2} - x_{1}}</equation><equation>f^{\prime}(\xi_{2}) = \frac{f(x_{3}) - f(x_{2})}{x_{3} - x_{2}}</equation>.由<equation>f^{\prime}(x)</equation>单调增加以及<equation>\xi_{1} <</equation><equation>\xi_{2}</equation>可得<equation>f^{\prime}(\xi_{1}) < f^{\prime}(\xi_{2})</equation>，即<equation>\frac{f(x_{2}) - f(x_{1})}{x_{2} - x_{1}} < \frac{f(x_{3}) - f(x_{2})}{x_{3} - x_{2}}.</equation>再证明充分性.

任取<equation>x_{0}, x_{1}, x_{2}\in(a,b)</equation>满足<equation>x_{1} < x_{0} < x_{2}</equation>，由已知条件可得<equation>\frac{f(x_0) - f(x_1)}{x_0 - x_1} < \frac{f(x_2) - f(x_0)}{x_2 - x_0}.</equation>取s,t满足<equation>x_{1} < s < x_{0} < t < x_{2}</equation>，由已知条件可得<equation>\frac {f (s) - f \left(x _ {1}\right)}{s - x _ {1}} < \frac {f \left(x _ {0}\right) - f (s)}{x _ {0} - s}, \quad \frac {f (t) - f \left(x _ {0}\right)}{t - x _ {0}} < \frac {f \left(x _ {2}\right) - f (t)}{x _ {2} - t}.</equation>在<equation>\frac{f(s)-f(x_{1})}{s-x_{1}}<\frac{f(x_{0})-f(s)}{x_{0}-s}</equation>中令 s<equation>\rightarrow x_{1}^{+}</equation>可得<equation>f ^ {\prime} \left(x _ {1}\right) = f _ {*} ^ {\prime} \left(x _ {1}\right) = \lim _ {s \rightarrow x _ {1}} \frac {f (s) - f \left(x _ {1}\right)}{s - x _ {1}} \leqslant \lim _ {s \rightarrow x _ {1}} \frac {f \left(x _ {0}\right) - f (s)}{x _ {0} - s} = \frac {f \left(x _ {0}\right) - f \left(x _ {1}\right)}{x _ {0} - x _ {1}}.</equation>在<equation>\frac{f(t)-f(x_{0})}{t-x_{0}}<\frac{f(x_{2})-f(t)}{x_{2}-t}</equation>中令<equation>t\to x_{2}^{-}</equation>可得<equation>\frac {f \left(x _ {2}\right) - f \left(x _ {0}\right)}{x _ {2} - x _ {0}} = \lim _ {t \rightarrow x _ {2}} \frac {f (t) - f \left(x _ {0}\right)}{t - x _ {0}} \leqslant \lim _ {t \rightarrow x _ {2}} \frac {f \left(x _ {2}\right) - f (t)}{x _ {2} - t} = f _ {-} ^ {\prime} \left(x _ {2}\right) = f ^ {\prime} \left(x _ {2}\right).</equation>由(1)式，(2)式以及<equation>\frac{f(x_{0})-f(x_{1})}{x_{0}-x_{1}}<\frac{f(x_{2})-f(x_{0})}{x_{2}-x_{0}}</equation>可得<equation>f^{\prime}(x_{1})<f^{\prime}(x_{2}).</equation>由<equation>x_{1},x_{2}</equation>的任意性可得<equation>f^{\prime}(x)</equation>在（a,b）内严格单调增加.

---

**2024年第21题 | 解答题 | 12分**
21. (本题满分12分)

设函数 f(x)具有二阶导数，且<equation>f^{\prime}(0)=f^{\prime}(1),\left| f^{\prime\prime}(x)\right| \leqslant 1</equation>，证明：

I. 当 x<equation>\in(0,1)</equation>时，<equation>|f(x)-f(0)(1-x)-f(1)x|\leqslant \frac{x(1-x)}{2}</equation>；

II.<equation>\left|\int_{0}^{1} f(x)\mathrm{d}x-\frac{f(0)+f(1)}{2}\right|\leqslant \frac{1}{12}.</equation>
**解析: **证（I）（法一）分别写出<equation>f ( x )</equation>在<equation>x=0</equation>与<equation>x=1</equation>处的一阶泰勒公式.<equation>f (x) = f (0) + f ^ {\prime} (0) x + \frac {f ^ {\prime \prime} \left(\xi_ {1}\right) x ^ {2}}{2},</equation><equation>f (x) = f (1) + f ^ {\prime} (1) (x - 1) + \frac {f ^ {\prime \prime} \left(\xi_ {2}\right) \left(x - 1\right) ^ {2}}{2},</equation>其中<equation>\xi_{1}</equation>介于0与<equation>x</equation>之间，<equation>\xi_{2}</equation>介于1与<equation>x</equation>之间.

(2) 式<equation>\times x-（1）</equation>式<equation>\times (x-1)</equation>，并结合<equation>f^{\prime}(0)=f^{\prime}(1)</equation>可得<equation>f (x) = f (0) (1 - x) + f (1) x + \frac {x (x - 1)}{2} \left[ f ^ {\prime \prime} \left(\xi_ {2}\right) (x - 1) - f ^ {\prime \prime} \left(\xi_ {1}\right) x \right].</equation>由（3）式可得，当<equation>x\in (0,1)</equation>时，<equation>\left| f (x) - f (0) (1 - x) - f (1) x \right| = \frac {x (1 - x)}{2} \left| f ^ {\prime \prime} \left(\xi_ {2}\right) (x - 1) - f ^ {\prime \prime} \left(\xi_ {1}\right) x \right|.</equation>由于<equation>|f^{\prime \prime}(\xi_{2})(x - 1) - f^{\prime \prime}(\xi_{1})x| \leqslant |f^{\prime \prime}(\xi_{2})|(1 - x) + |f^{\prime \prime}(\xi_{1})|x,</equation>故结合<equation>|f^{\prime \prime}(x)| \leqslant 1</equation>以及（4）式可得<equation>\left| f (x) - f (0) (1 - x) - f (1) x \right| \leqslant \frac {x (1 - x)}{2} \cdot [ (1 - x) + x ] = \frac {x (1 - x)}{2}.</equation>（法二）所证命题等价于当<equation>x\in (0,1)</equation>时，<equation>- \frac {x (1 - x)}{2} \leqslant f (x) - f (0) (1 - x) - f (1) x \leqslant \frac {x (1 - x)}{2}.</equation>令<equation>F ( x ) = f ( x ) - f ( 0 ) ( 1 - x ) - f ( 1 ) x - \frac { x ( 1 - x ) } { 2 }</equation>，则<equation>F ( 0 ) = F ( 1 ) = 0</equation>，且<equation>F^{\prime \prime}(x)=f^{\prime \prime}(x)</equation>+1.由于<equation>| f^{\prime \prime}(x) | \leqslant 1</equation>，故<equation>F^{\prime \prime}(x) \geqslant 0.</equation>下面证明当<equation>x\in (0,1)</equation>时，<equation>F(x)\leqslant 0.</equation>若存在<equation>c\in (0,1)</equation>，使得<equation>F(c) > 0</equation>，则分别对<equation>[0,c],[c,1]</equation>上的<equation>F(x)</equation>使用拉格朗日中值定理可得，存在<equation>\xi_{1}\in (0,c),\xi_{2}\in (c,1)</equation>，使得<equation>F ^ {\prime} \left(\xi_ {1}\right) = \frac {F (c) - F (0)}{c - 0} > 0, \quad F ^ {\prime} \left(\xi_ {2}\right) = \frac {F (1) - F (c)}{1 - c} < 0.</equation>再对<equation>[\xi_{1},\xi_{2} ]</equation>上的<equation>F^{\prime}(x)</equation>使用拉格朗日中值定理可得，存在<equation>\xi\in(\xi_{1},\xi_{2})</equation>，使得<equation>F ^ {\prime \prime} (\xi) = \frac {F ^ {\prime} \left(\xi_ {2}\right) - F ^ {\prime} \left(\xi_ {1}\right)}{\xi_ {2} - \xi_ {1}} < 0.</equation>这与<equation>F^{\prime \prime}(x)\geqslant0</equation>矛盾.

因此，当<equation>x\in (0,1)</equation>时，<equation>F(x)\leqslant 0</equation>，即<equation>f(x) - f(0)(1 - x) - f(1)x\leqslant \frac{x(1 - x)}{2}.</equation>令<equation>G ( x )=f ( x )-f ( 0 ) ( 1-x )-f ( 1 ) x+\frac{x(1-x)}{2}</equation>，同理可得<equation>G^{\prime \prime}(x)\leqslant0</equation>，且进一步可得当<equation>x\in</equation>（0,1）时，<equation>G ( x )\geqslant0</equation>，即<equation>f ( x )-f ( 0 ) ( 1-x )-f ( 1 ) x\geqslant-\frac{x(1-x)}{2}.</equation>综上所述，所证命题成立.

（Ⅱ）由第（Ⅰ）问可得<equation>\left| f (x) - f (0) (1 - x) - f (1) x \right| \leqslant \frac {x (1 - x)}{2}.</equation>对（5）式两端从0到1积分可得，<equation>\begin{aligned} \int_ {0} ^ {1} | f (x) - f (0) (1 - x) - f (1) x | \mathrm {d} x \leqslant \int_ {0} ^ {1} \frac {x (1 - x)}{2} \mathrm {d} x &= \frac {1}{2} \int_ {0} ^ {1} \left(x - x ^ {2}\right) \mathrm {d} x \\ &= \frac {1}{2} \left(\frac {x ^ {2}}{2} - \frac {x ^ {3}}{3}\right) \Big | _ {0} ^ {1} = \frac {1}{1 2}. \end{aligned}</equation><equation>\begin{array}{l} \left| \int_ {0} ^ {1} f (x) \mathrm {d} x - f (0) \int_ {0} ^ {1} (1 - x) \mathrm {d} x - f (1) \int_ {0} ^ {1} x \mathrm {d} x \right| = \left| \int_ {0} ^ {1} f (x) \mathrm {d} x - \frac {f (0) + f (1)}{2} \right| \\ \leqslant \int_ {0} ^ {1} | f (x) - f (0) (1 - x) - f (1) x | \mathrm {d} x \leqslant \frac {1}{1 2}. \\ \end{array}</equation>

---

**2023年第21题 | 解答题 | 12分**
21. (本题满分12分)

设函数 f(x)在<equation>[-a,a]</equation>上具有二阶连续导数，证明：

I. 若 f(0)=0，则存在<equation>\xi\in(-a,a)</equation>，使得<equation>f^{\prime\prime}(\xi)=\frac{1}{a^{2}}[f(a)+f(-a)].

II. 若 f(x)在</equation>(-a,a)<equation>内取得极值，则存在</equation>\eta\in(-a,a)<equation>使得</equation>|f^{\prime\prime}(\eta)|\geqslant\frac{1}{2a^{2}}|f(a)-f(-a)|.
**答案: **# （I）证明略；

（Ⅱ）证明略.
**解析: **证（I）由 f(x）的泰勒公式可得<equation>f (a) = f (0) + f ^ {\prime} (0) a + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {1}\right) a ^ {2} \xlongequal {f (0) = 0} f ^ {\prime} (0) a + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {1}\right) a ^ {2},</equation><equation>f (- a) = f (0) + f ^ {\prime} (0) \cdot (- a) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {2}\right) a ^ {2} \stackrel {f (0) = 0} {=} f ^ {\prime} (0) \cdot (- a) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {2}\right) a ^ {2},</equation>其中<equation>\xi_{1}\in(0,a),\xi_{2}\in(-a,0).</equation>两式相加可得<equation>f (a) + f (- a) = \frac {a ^ {2}}{2} \left[ f ^ {\prime \prime} \left(\xi_ {1}\right) + f ^ {\prime \prime} \left(\xi_ {2}\right) \right].</equation>记<equation>\max \left\{f^{\prime \prime}\left(\xi_{1}\right),f^{\prime \prime}\left(\xi_{2}\right)\right\}=M</equation>，<equation>\min \left\{f^{\prime \prime}\left(\xi_{1}\right),f^{\prime \prime}\left(\xi_{2}\right)\right\}=m</equation>，则由（1）式可得<equation>m \leqslant \frac {f (a) + f (- a)}{a ^ {2}} = \frac {1}{2} \left[ f ^ {\prime \prime} \left(\xi_ {1}\right) + f ^ {\prime \prime} \left(\xi_ {2}\right) \right] \leqslant M.</equation>由于 f(x)在<equation>[-a,a]</equation>上有二阶连续导数，故由连续函数的介值定理可知，存在<equation>\xi \in[ \xi_{2},\xi_{1} ]\subset(-a,a)</equation>，使得<equation>f^{\prime \prime}(\xi)=\frac{1}{a^{2}}[f(a)+f(-a)]</equation>（Ⅱ）设 f(x)在<equation>(-a,a)</equation>内的极值点为<equation>x_{0}</equation>，则<equation>f^{\prime}(x_{0})=0.</equation>由 f(x)的泰勒公式可得<equation>\begin{aligned} f (a) &= f \left(x _ {0}\right) + f ^ {\prime} \left(x _ {0}\right) \left(a - x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {1}\right) \left(a - x _ {0}\right) ^ {2} \\ \frac {f ^ {\prime} \left(x _ {0}\right) = 0}{\overline {{}}} f \left(x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {1}\right) \left(a - x _ {0}\right) ^ {2}, \end{aligned}</equation><equation>\begin{aligned} f (- a) &= f \left(x _ {0}\right) + f ^ {\prime} \left(x _ {0}\right) \left(- a - x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {2}\right) \left(- a - x _ {0}\right) ^ {2} \\ \frac {f ^ {\prime} \left(x _ {0}\right) = 0}{\overline {{}}} f \left(x _ {0}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {2}\right) \left(a + x _ {0}\right) ^ {2}, \end{aligned}</equation>其中<equation>\eta_{1}\in(x_{0},a),\eta_{2}\in(-a,x_{0}).</equation>两式相减可得<equation>f (a) - f (- a) = \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {1}\right) \left(a - x _ {0}\right) ^ {2} - \frac {1}{2} f ^ {\prime \prime} \left(\eta_ {2}\right) \left(a + x _ {0}\right) ^ {2}.</equation>记<equation>\max \left\{ \left| f^{\prime \prime}\left(\eta_{1}\right)\right|, \left| f^{\prime \prime}\left(\eta_{2}\right)\right| \right\}=M</equation>，则由（2）式可得<equation>\left| f (a) - f (- a) \right| \leqslant \frac {M}{2} \left[ \left(a - x _ {0}\right) ^ {2} + \left(a + x _ {0}\right) ^ {2} \right] = \frac {M}{2} \left(2 a ^ {2} + 2 x _ {0} ^ {2}\right) \leqslant \frac {M}{2} \cdot 4 a ^ {2} = 2 a ^ {2} M.</equation>因此，<equation>M\geqslant \frac{1}{2a^{2}}|f(a)-f(-a)|.</equation>取<equation>\eta\in\{\eta_{1},\eta_{2}\}</equation>使得<equation>|f^{\prime \prime}(\eta)|=M</equation>，则<equation>\eta\in(-a,a)</equation>满足<equation>|f^{\prime \prime}(\eta)|\geqslant\frac{1}{2a^{2}}|f(a)-f(-a)|.</equation>

---

**2022年第21题 | 解答题 | 12分**
21. (本题满分12分)

设函数 f(x)在<equation>(-\infty, +\infty)</equation>上有二阶连续导数，证明：<equation>f^{\prime \prime}(x)\geqslant0</equation>的充分必要条件是对任意不同的实数 a,b，都有<equation>f\left(\frac{a+b}{2}\right)\leqslant\frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x</equation>成立.
**解析: **证 先证明必要性，即证明，若<equation>f^{\prime \prime}(x)\geqslant 0</equation>，则对不同的实数a,b，<equation>f\left(\frac{a+b}{2}\right)\leqslant \frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x.</equation>（法一）不妨设 b > a. 在区间<equation>[a,b]</equation>上，使用 f(x)在点<equation>\frac{a+b}{2}</equation>处的二阶泰勒公式.<equation>f (x) = f \left(\frac {a + b}{2}\right) + f ^ {\prime} \left(\frac {a + b}{2}\right) \left(x - \frac {a + b}{2}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a + b}{2}\right) ^ {2},</equation>其中<equation>\xi_{x}</equation>介于x与<equation>\frac{a+b}{2}</equation>之间.

将（1）式代入<equation>\int_{a}^{b} f(x)\mathrm{d}x</equation>，可得<equation>\begin{aligned} \int_ {a} ^ {b} f (x) \mathrm {d} x &= \int_ {a} ^ {b} \left[ f \left(\frac {a + b}{2}\right) + f ^ {\prime} \left(\frac {a + b}{2}\right) \left(x - \frac {a + b}{2}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a + b}{2}\right) ^ {2} \right] \mathrm {d} x \\ &= f \left(\frac {a + b}{2}\right) (b - a) + f ^ {\prime} \left(\frac {a + b}{2}\right) \int_ {a} ^ {b} \left(x - \frac {a + b}{2}\right) \mathrm {d} x \\ + \frac {1}{2} \int_ {a} ^ {b} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a + b}{2}\right) ^ {2} \mathrm {d} x. \end{aligned}</equation>注意到<equation>\int_ {a} ^ {b} \left(x - \frac {a + b}{2}\right) \mathrm {d} x = \frac {x ^ {2}}{2} \Bigg | _ {a} ^ {b} - \frac {(a + b) (b - a)}{2} = \frac {b ^ {2} - a ^ {2}}{2} - \frac {b ^ {2} - a ^ {2}}{2} = 0,</equation>故<equation>\int_ {a} ^ {b} f (x) \mathrm {d} x = f \left(\frac {a + b}{2}\right) (b - a) + \frac {1}{2} \int_ {a} ^ {b} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a + b}{2}\right) ^ {2} \mathrm {d} x.</equation>结合<equation>f^{\prime \prime}(x)\geqslant 0</equation>可得<equation>\int_{a}^{b}f(x)\mathrm{d}x\geqslant f\left(\frac{a+b}{2}\right)(b-a)</equation>，即<equation>f\left(\frac{a+b}{2}\right)\leqslant \frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x.</equation>（法二）不妨设 b > a.<equation>f\left(\frac{a+b}{2}\right)\leqslant \frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x</equation>等价于<equation>f\left(\frac{a+b}{2}\right)(b-a)-\int_{a}^{b}f(x)\mathrm{d}x\leqslant 0.</equation>令<equation>F ( x )=\int_{a}^{x} f ( t ) \mathrm{d} t-f \left( \frac{a+x}{2} \right) ( x-a), x \in[ a, b ],</equation>则<equation>F ( a )=0</equation>，且<equation>\begin{aligned} F ^ {\prime} (x) &= f (x) - f \left(\frac {a + x}{2}\right) - f ^ {\prime} \left(\frac {a + x}{2}\right) \frac {x - a}{2} \frac {\text {拉 格 朗 日}}{\text {中 值 定 理}} f ^ {\prime} \left(\eta_ {x}\right) \frac {x - a}{2} - f ^ {\prime} \left(\frac {a + x}{2}\right) \frac {x - a}{2} \\ &= \left[ f ^ {\prime} \left(\eta_ {x}\right) - f ^ {\prime} \left(\frac {a + x}{2}\right) \right] \frac {x - a}{2}, \end{aligned}</equation>其中<equation>\eta_{x}\in \left(\frac{a + x}{2},x\right)</equation>由于<equation>f^{\prime \prime}(x)\geqslant 0</equation>，故<equation>f^{\prime}(x)</equation>单调不减，从而<equation>f^{\prime}(\eta_{x})\geqslant f^{\prime}\left(\frac{a+x}{2}\right)</equation>即<equation>f^{\prime}(\eta_{x})-f^{\prime}\left(\frac{a+x}{2}\right)\geqslant 0.</equation>于是，对<equation>x\in(a,b),F^{\prime}(x)\geqslant 0,F(x)</equation>在[a,b]上单调不减.

又因为<equation>F ( a )=0</equation>，所以<equation>F ( b )\geqslant F ( a )=0</equation>，即<equation>\int_{a}^{b} f ( x )\mathrm{d} x\geqslant f \left( \frac{a+b}{2} \right) ( b-a).</equation>下面证明充分性，即证明，若对不同的实数 a,b，<equation>f\left(\frac{a+b}{2}\right)\leqslant \frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x</equation>，则<equation>f^{\prime \prime}(x)\geqslant 0.</equation>假设存在<equation>x_{0}</equation>，使得<equation>f^{\prime \prime}(x_{0})<0</equation>，由二阶导数连续可得<equation>\lim_{x\to x_{0}}f^{\prime \prime}(x)=f^{\prime \prime}(x_{0})<0</equation>，结合极限的局部保号性可知，存在<equation>\delta >0</equation>，在区间<equation>(x_{0}-\delta,x_{0}+\delta)</equation>内，均有<equation>f^{\prime \prime}(x)<0</equation>.从而取<equation>[a_{0},b_{0}]\subset(x_{0}-\delta,x_{0}+\delta)</equation>，可得在<equation>[a_{0},b_{0}]</equation>上，均有<equation>f^{\prime \prime}(x)<0.</equation>在区间<equation>[ a_{0}, b_{0} ]</equation>上重复必要性中的做法.<equation>\begin{aligned} \int_ {a _ {0}} ^ {b _ {0}} f (x) \mathrm {d} x &= \int_ {a _ {0}} ^ {b _ {0}} \left[ f \left(\frac {a _ {0} + b _ {0}}{2}\right) + f ^ {\prime} \left(\frac {a _ {0} + b _ {0}}{2}\right) \left(x - \frac {a _ {0} + b _ {0}}{2}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a _ {0} + b _ {0}}{2}\right) ^ {2} \right] \mathrm {d} x \\ &= f \left(\frac {a _ {0} + b _ {0}}{2}\right) \left(b _ {0} - a _ {0}\right) + f ^ {\prime} \left(\frac {a _ {0} + b _ {0}}{2}\right) \int_ {a _ {0}} ^ {b _ {0}} \left(x - \frac {a _ {0} + b _ {0}}{2}\right) \mathrm {d} x \\ + \frac {1}{2} \int_ {a _ {0}} ^ {b _ {0}} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a _ {0} + b _ {0}}{2}\right) ^ {2} \mathrm {d} x, \end{aligned}</equation>其中<equation>\xi_{x}</equation>介于x与<equation>\frac{a_{0}+b_{0}}{2}</equation>之间.

于是，<equation>\int_ {a _ {0}} ^ {b _ {0}} f (x) \mathrm {d} x = f \left(\frac {a _ {0} + b _ {0}}{2}\right) \left(b _ {0} - a _ {0}\right) + \frac {1}{2} \int_ {a _ {0}} ^ {b _ {0}} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a _ {0} + b _ {0}}{2}\right) ^ {2} \mathrm {d} x.</equation>结合<equation>f^{\prime \prime}(x) < 0</equation>可得<equation>\int_{a_{0}}^{b_{0}}f(x)\mathrm{d}x < f\left(\frac{a_{0}+b_{0}}{2}\right)\left(b_{0}-a_{0}\right)</equation>，即<equation>f\left(\frac{a_{0}+b_{0}}{2}\right) > \frac{1}{b_{0}-a_{0}}\int_{a_{0}}^{b_{0}}f(x)\mathrm{d}x.</equation>这与前提矛盾.

因此，假设不正确.<equation>f^{\prime \prime}(x)</equation>在<equation>(-\infty, +\infty)</equation>上恒非负.

（法二）若对不同的实数 a,b，<equation>f\left(\frac{a+b}{2}\right)\leqslant \frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x</equation>，则对任意实数<equation>x_{0}</equation>以及任意<equation>\delta >0,</equation>均有<equation>\int_{x_0 - \delta}^{x_0 + \delta}f(x)\mathrm{d}x - 2\delta f(x_0)\geqslant 0</equation>，从而<equation>\frac{\int_{x_0 - \delta}^{x_0 + \delta}f(x)\mathrm{d}x - 2\delta f(x_0)}{\delta^{3}}\geqslant 0.</equation>而<equation>\begin{array}{l} \lim _ {\delta \rightarrow 0 ^ {+}} \frac {\int_ {x _ {0} - \delta} ^ {x _ {0} + \delta} f (x) \mathrm {d} x - 2 \delta f \left(x _ {0}\right)}{\delta^ {3}} \xlongequal {\text {洛必达}} \lim _ {\delta \rightarrow 0 ^ {+}} \frac {f \left(x _ {0} + \delta\right) + f \left(x _ {0} - \delta\right) - 2 f \left(x _ {0}\right)}{3 \delta^ {2}} \\ \xlongequal {\text {洛必达}} \lim _ {\delta \rightarrow 0 ^ {+}} \frac {f ^ {\prime} \left(x _ {0} + \delta\right) - f ^ {\prime} \left(x _ {0} - \delta\right)}{6 \delta} \\ \xlongequal {\text {洛必达}} \lim _ {\delta \rightarrow 0 ^ {+}} \frac {f ^ {\prime \prime} \left(x _ {0} + \delta\right) + f ^ {\prime \prime} \left(x _ {0} - \delta\right)}{6} \\ \xlongequal {f ^ {\prime \prime} \text {连续}} \frac {1}{3} f ^ {\prime \prime} \left(x _ {0}\right), \\ \end{array}</equation>故由极限的保号性可知，<equation>f^{\prime \prime} \left( x_{0} \right) \geqslant 0.</equation>由<equation>x_0</equation>的任意性可知，对不同的实数<equation>a,b,f\left(\frac{a + b}{2}\right)\leqslant \frac{1}{b - a}\int_{a}^{b}f(x)\mathrm{d}x</equation>是<equation>f^{\prime \prime}(x)\geqslant 0</equation>的充分条件.综上所述，<equation>f^{\prime \prime}(x)\geqslant 0</equation>的充分必要条件是对不同的实数<equation>a,b,f\left(\frac{a + b}{2}\right)\leqslant \frac{1}{b - a}\int_{a}^{b}f(x)\mathrm{d}x.</equation>

---

**2020年第20题 | 解答题 | 11分**
20. (本题满分11分）

设函数<equation>f ( x )=\int_{1}^{x} \mathrm{e}^{t^{2}} \mathrm{d} t.</equation>I. 证明：存在<equation>\xi\in(1,2)</equation>，使得<equation>f(\xi)=(2-\xi)\mathrm{e}^{\xi^{2}}</equation>II. 证明：存在<equation>\eta\in(1,2)</equation>，使得<equation>f(2)=\ln 2\cdot\eta\mathrm{e}^{\eta^{2}}</equation>
**答案: **# （I）证明略；

（Ⅱ）证明略.
**解析: **证 （ I ）注意到<equation>f(1)=0.</equation>（法一）待证等式等价于<equation>f (\xi) + (\xi -2)\mathrm{e}^{\xi^{2}} = 0.</equation>令<equation>F ( x ) = f ( x ) + ( x - 2 ) \mathrm{e}^{x^{2}}</equation>，则<equation>F ( 1 ) = f ( 1 ) - \mathrm{e} = - \mathrm{e} < 0,F(2) = f(2) = \int_{1}^{2}\mathrm{e}^{t^{2}}\mathrm{d}t > 0.</equation>对[1,2]上的<equation>F(x)</equation>使用零点定理可得，存在<equation>\xi\in(1,2)</equation>，使得<equation>F(\xi)=0</equation>即<equation>f(\xi)+(\xi-2)\mathrm{e}^{\xi^{2}}=0</equation>也即<equation>f(\xi)=(2-\xi)\mathrm{e}^{\xi^{2}}.</equation>（法二）由变限积分求导公式可得，<equation>f^{\prime}(x)=\mathrm{e}^{x^{2}}</equation>，故待证等式<equation>f(\xi)=(2-\xi)\mathrm{e}^{\xi^{2}}</equation>等价于<equation>f(\xi)=(2-\xi)f^{\prime}(\xi)</equation>，也等价于<equation>f(\xi)+(\xi-2)f^{\prime}(\xi)=0.</equation>令<equation>F ( x ) = ( x - 2 ) f ( x )</equation>，则<equation>F^{\prime}(x)=f(x)+(x-2)f^{\prime}(x).</equation>由于<equation>F ( 1 )=-f ( 1 )=0,F ( 2 )=0</equation>，故由罗尔定理可知，存在<equation>\xi\in(1,2)</equation>，使得<equation>F^{\prime}(\xi)=0</equation>，即<equation>f(\xi)=(2-\xi)f^{\prime}(\xi)</equation>，也即<equation>f(\xi)=(2-\xi)\mathrm{e}^{\xi^{2}}.</equation>（法三）令<equation>F ( x )=\int_{1}^{x}\left(\int_{1}^{u}\mathrm{e}^{t^{2}}\mathrm{d} t\right)\mathrm{d} u</equation>，则利用变限积分求导公式可得<equation>F^{\prime}(x)=\int_{1}^{x}\mathrm{e}^{t^{2}}\mathrm{d} t=f(x).</equation>F（1）=0.此外，利用交换积分次序，可得<equation>F (x) = \int_ {1} ^ {x} \mathrm {d} u \int_ {1} ^ {u} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = \int_ {1} ^ {x} \mathrm {d} t \int_ {t} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} u = \int_ {1} ^ {x} (x - t) \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = x \int_ {1} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t - \int_ {1} ^ {x} t \mathrm {e} ^ {t ^ {2}} \mathrm {d} t.</equation>于是，<equation>F ( 2 )=\int_{1}^{2} ( 2-t ) \mathrm{e}^{t^{2}} \mathrm{d} t.</equation>令<equation>G ( x ) = F ( x ) - \int_{1}^{x} ( 2 - t ) \mathrm{e}^{t^{2}} \mathrm{d} t</equation>，则<equation>G ( 1 ) = 0.</equation><equation>G (2) = F (2) - \int_ {1} ^ {2} (2 - t) \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = \int_ {1} ^ {2} (2 - t) \mathrm {e} ^ {t ^ {2}} \mathrm {d} t - \int_ {1} ^ {2} (2 - t) \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = 0.</equation>由罗尔定理，存在<equation>\xi\in(1,2)</equation>，使得<equation>G^{\prime}(\xi)=0</equation>，即<equation>G ^ {\prime} (\xi) = F ^ {\prime} (\xi) - (2 - \xi) \mathrm {e} ^ {\xi^ {2}} = f (\xi) - (2 - \xi) \mathrm {e} ^ {\xi^ {2}} = 0.</equation>因此，存在<equation>\xi \in (1,2)</equation>，使得<equation>f(\xi) = (2 - \xi)\mathrm{e}^{\xi^2}</equation>（Ⅱ）令<equation>g ( x )=\ln x</equation>，则<equation>g^{\prime}(x)=\frac{1}{x}.</equation>由柯西中值定理，存在<equation>\eta\in(1,2)</equation>，使得<equation>\frac {f (2) - f (1)}{g (2) - g (1)} = \frac {f ^ {\prime} (\eta)}{g ^ {\prime} (\eta)}.</equation>由于<equation>f(1) = 0,g(1) = 0,g(2) = \ln 2</equation>，故（1）式可化为<equation>\frac{f(2)}{\ln 2} = \frac{\mathrm{e}^{\eta^2}}{\frac{1}{\eta}}</equation>即<equation>f(2) = \ln 2\cdot \eta \mathrm{e}^{\eta^2}</equation>.

---

**2019年第21题 | 解答题 | 11分**
21. (本题满分11分)

已知函数 f(x)在[0,1]上具有2阶导数，且<equation>f(0)=0,f(1)=1,\int_{0}^{1} f(x)\mathrm{d} x=1</equation>，证明：

I. 存在<equation>\xi \in(0,1)</equation>，使得<equation>f^{\prime}(\xi)=0;</equation>II. 存在<equation>\eta \in(0,1)</equation>，使得<equation>f^{\prime\prime}(\eta)<-2</equation>
**答案: **（I）证明略；

（Ⅱ）证明略.
**解析: **证（I）（法一）构造辅助函数<equation>F ( x )=\int_{0}^{x} f ( t ) \mathrm{d} t</equation>，则<equation>F ( 0 )=0,F ( 1 )=\int_{0}^{1} f ( x ) \mathrm{d} x=1.</equation>由拉格朗日中值定理可得，存在<equation>c \in(0,1)</equation>，使得<equation>F^{\prime}(c)=1</equation>即<equation>f(c)=1.</equation>再对<equation>[c,1]</equation>上的<equation>f(x)</equation>使用罗尔定理可得，存在<equation>\xi\in(c,1)\subseteq(0,1)</equation>，使得<equation>f^{\prime}(\xi)=0.</equation>（法二）反证法.

由 f(x)在[0,1]上存在2阶导数可知<equation>f^{\prime}(x)</equation>在[0,1]上连续.若不存在<equation>\xi \in(0,1)</equation>，使得<equation>f^{\prime}(\xi)=0</equation>，则由<equation>f^{\prime}(x)</equation>的连续性以及零点定理可知，<equation>f^{\prime}(x)</equation>在(0,1)上恒大于零或恒小于零.

又因为<equation>f(0)=0</equation><equation>f(1)=1</equation>，所以<equation>f^{\prime}(x)</equation>恒大于零，<equation>f(x)</equation>在[0,1]上单调增加. f(1)是f(x)在 [0,1]上的最大值.于是，<equation>\int_ {0} ^ {1} f (x) \mathrm {d} x < \int_ {0} ^ {1} f (1) \mathrm {d} x = 1.</equation>这与<equation>\int_{0}^{1} f ( x ) \mathrm{d} x=1</equation>矛盾.

因此，存在<equation>\xi\in(0,1)</equation>，使得<equation>f^{\prime}(\xi)=0.</equation>（法三）证明 f(x)在[0,1]上的最大值大于1.

假设不然，则对于任意的<equation>x\in[0,1]</equation>，都有<equation>f(x)\leqslant 1</equation>，从而<equation>\int_{0}^{1}f(x)\mathrm{d}x\leqslant 1.</equation>又因为<equation>f(0)=0,f(1)=1</equation>所以由 f(x)的连续性可知，存在<equation>\delta >0</equation>，使得当<equation>x\in(0,\delta)</equation>时，<equation>f(x) < 1.</equation>于是，<equation>\int_{0}^{1}f(x)\mathrm{d}x < 1.</equation>这与<equation>\int_{0}^{1} f(x)\mathrm{d}x=1</equation>矛盾.假设不正确.

因此，<equation>f ( x )</equation>在[0,1]上的最大值大于1.如图（a）所示，记该点为<equation>\xi</equation>，由于<equation>f ( 0 )=0,f ( 1 )=1</equation>故<equation>\xi \in(0,1).</equation><equation>f ^ {\prime} (\xi) = 0.</equation>(a)

(b)

（Ⅱ）（法一）构造辅助函数<equation>G ( x )=f ( x )+x^{2}</equation>，于是 G(x)在[0,1]上2阶可导，且<equation>G^{\prime \prime} ( x )=f^{\prime \prime} ( x )+2.</equation>取 c为第（I）问中满足<equation>f ( c )=1</equation>的点，则<equation>G ( 0 )=0,G ( c )=1+c^{2},G ( 1 )=2.</equation>由拉格朗日中值定理可得，存在<equation>\eta_{1}\in (0,c)</equation>，使得<equation>G ^ {\prime} \left(\eta_ {1}\right) = \frac {G (c) - G (0)}{c - 0} = \frac {1 + c ^ {2}}{c}.</equation>存在<equation>\eta_{2}\in(c,1)</equation>，使得<equation>G ^ {\prime} \left(\eta_ {2}\right) = \frac {G (1) - G (c)}{1 - c} = \frac {1 - c ^ {2}}{1 - c} = 1 + c.</equation>再对<equation>[\eta_{1},\eta_{2} ]</equation>上的<equation>G^{\prime}(x)</equation>使用拉格朗日中值定理，可得存在<equation>\eta\in(\eta_{1},\eta_{2})\subseteq(0,1)</equation>，使得<equation>G ^ {\prime \prime} (\eta) = \frac {G ^ {\prime} \left(\eta_ {2}\right) - G ^ {\prime} \left(\eta_ {1}\right)}{\eta_ {2} - \eta_ {1}} = \frac {1 + c - \frac {1 + c ^ {2}}{c}}{\eta_ {2} - \eta_ {1}} = \frac {1 - \frac {1}{c}}{\eta_ {2} - \eta_ {1}}.</equation>由于<equation>c\in (0,1)</equation>，故<equation>1 - \frac{1}{c} < 0</equation>，从而<equation>G^{\prime \prime}(\eta) < 0</equation>，即<equation>f^{\prime \prime}(\eta) + 2 < 0</equation>，也即<equation>f^{\prime \prime}(\eta) < -2.</equation>（法二）构造二次函数<equation>g ( x )=a x^{2}+b x+c</equation>，使得<equation>g ( 0 )=f ( 0 )=0,g ( 1 )=f ( 1 )=1</equation>且<equation>\int_{0}^{1} g ( x ) \mathrm{d} x=\int_{0}^{1} f ( x ) \mathrm{d} x=1.</equation>由 g（0）=0可得 c=0.由 g（1）=1可得 a+b=1.又由<equation>\int_{0}^{1} g(x)\mathrm{d}x=1</equation>可得<equation>\frac{a}{3}+\frac{b}{2}=1</equation>即<equation>2a+3b=6.</equation>解得 a=-3,b=4.于是，令 g(x）=-3x²+4x. f(x)与 g(x)的图形如图（b）所示.

考虑<equation>G ( x ) = f ( x ) - g ( x )</equation>，则<equation>G ( 0 ) = 0, G ( 1 ) = 0, \int_{0}^{1} G ( x ) \mathrm{d} x = 0</equation>，且<equation>G^{\prime \prime}(x) = f^{\prime \prime}(x) + 6.</equation>下面我们证明，存在<equation>\eta\in(0,1)</equation>，使得<equation>G^{\prime\prime}(\eta)=0</equation>，即<equation>f^{\prime\prime}(\eta)=-6<-2.</equation>令<equation>H ( x )=\int_{0}^{x} G ( t ) \mathrm{d} t</equation>，则<equation>H ( 0 )=0,H ( 1 )=0.</equation>由拉格朗日中值定理可得，存在<equation>k \in(0,1)</equation>使得<equation>H^{\prime}(k)=0</equation>即<equation>G(k)=0.</equation>从而，<equation>G(0)=G(k)=G(1)=0.</equation>分别对<equation>[0,k],[k,1]</equation>上的<equation>G(x)</equation>使用罗尔定理，可得存在<equation>\eta_{1}\in(0,k),\eta_{2}\in(k,1)</equation>，使得<equation>G^{\prime}(\eta_{1})=0,G^{\prime}(\eta_{2})=0.</equation>再对<equation>[\eta_{1},\eta_{2}]</equation>上的<equation>G^{\prime}(x)</equation>使用罗尔定理，可得存在<equation>\eta \in (\eta_{1},\eta_{2})\subseteq (0,1)</equation>，使得<equation>G^{\prime \prime}(\eta) = 0</equation>，即<equation>f^{\prime \prime}(\eta) = -6 < -2.</equation>

---

**2015年第21题 | 解答题 | 11分**
21. (本题满分10分)

已知函数 f(x)在区间<equation>[ a,+\infty)</equation>上具有2阶导数，<equation>f ( a )=0, f^{\prime} ( x )>0, f^{\prime\prime} ( x )>0.</equation>设 b>a，曲线 y=f(x)在点 （b,f(b)）处的切线与x轴的交点是<equation>( x_{0},0)</equation>，证明 a<x0<b.
**答案: **## (21) 证明略.
**解析: **证 首先，由于过点（b，f(b)）的切线的斜率为<equation>f^{\prime}(b)</equation>，且该切线过点（<equation>x_{0},0)</equation>，故<equation>f^{\prime}(b)=\frac{f(b)-0}{b-x_{0}}</equation>，解得<equation>x_{0}=b-\frac{f(b)}{f^{\prime}(b)}。</equation>因为<equation>b > a, f^{\prime}(x) > 0, f(x)</equation>在<equation>[a, + \infty)</equation>上单调增加，所以<equation>f(b) > f(a)=0</equation>，从而<equation>\frac{f(b)}{f^{\prime}(b)} > 0.</equation>因此，<equation>x _ {0} = b - \frac {f (b)}{f ^ {\prime} (b)} < b.</equation>如图（a）所示，记点<equation>A</equation>为<equation>(a,f(a))</equation>，点<equation>B</equation>为<equation>(b,f(b))</equation>.

下面我们用两种方法证明<equation>a < x_{0}。</equation>(a)

(b)

（法一）由拉格朗日中值定理可得，存在<equation>\xi\in(a,b)</equation>，使得<equation>f^{\prime}(\xi)(b-a)=f(b)-f(a)</equation>，即弦AB的斜率等于曲线弧<equation>\widehat{AB}</equation>上某点<equation>(\xi,f(\xi))</equation>处的切线斜率<equation>f^{\prime}(\xi).</equation>由于<equation>f^{\prime\prime}(x)>0</equation>，故<equation>f^{\prime}(x)</equation>在<equation>[a,+\infty)</equation>上为单调增加函数，从而<equation>f^{\prime}(\xi)<f^{\prime}(b).</equation><equation>\frac {f (b) - f (a)}{b - a} = f ^ {\prime} (\xi) < f ^ {\prime} (b) = \frac {f (b) - 0}{b - x _ {0}}.</equation>代入<equation>f ( a ) = 0</equation>，得<equation>\frac{f ( b )}{b - a} < \frac{f ( b )}{b - x_0}.</equation>由于<equation>b - a > 0, b - x_0 > 0, f ( b ) > 0</equation>，故<equation>b - a > b - x_0</equation>，即<equation>a < x_0.</equation>（法二）要证<equation>x_{0} > a</equation>，即要证<equation>x_{0}=b-\frac{f(b)}{f^{\prime}(b)} > a.</equation>整理该不等式得<equation>b - \frac {f (b)}{f ^ {\prime} (b)} > a \xleftrightarrow {f ^ {\prime} (b) > 0} (b - a) f ^ {\prime} (b) - f (b) > 0.</equation>该不等式的几何意义为过点（a，0），斜率为<equation>f^{\prime}(b)</equation>的直线l在 x=b的纵坐标大于f(b).我们可证明在（a，b]上，直线l位于曲线 y=f(x）之上，如图（b）.

记<equation>g ( x )=f^{\prime} ( b ) ( x-a )</equation>，直线 l的方程为<equation>y=g ( x ).</equation>要证在（a,b]上，直线 l位于曲线<equation>y=f(x)</equation>之上，即要证当<equation>x\in(a,b]</equation>时，<equation>g ( x )-f ( x ) > 0.</equation>由拉格朗日中值定理，有<equation>f ( x ) = f ( a ) + f^{\prime} ( \xi_{x} ) ( x - a )</equation>，这里<equation>x \in(a,b]</equation><equation>\xi_{x} \in(a,x).</equation>从而<equation>g ( x ) - f ( x ) = f^{\prime} ( b ) ( x - a ) - f ( a ) - f^{\prime} ( \xi_{x} ) ( x - a)\frac{f ( a ) = 0}{=} \left[ f^{\prime} ( b ) - f^{\prime} ( \xi_{x} ) \right] ( x - a).</equation>由于对任意的<equation>x \in(a,b]</equation>，都有<equation>\xi_{x} < b</equation>，而<equation>f^{\prime\prime}(x)>0</equation><equation>f^{\prime}(x)</equation>在[a,b]上单调增加，故<equation>f ^ {\prime} (b) - f ^ {\prime} \left(\xi_ {x}\right) > 0.</equation>因此，<equation>g ( x ) - f ( x )</equation>在（a，b]上恒大于零.特别地，<equation>g ( b ) - f ( b ) > 0</equation>即<equation>f^{\prime} ( b ) ( b - a ) - f ( b ) > 0</equation><equation>x_{0}>a.</equation>综上所述，<equation>a < x_{0} < b.</equation>

---

**2013年第18题 | 解答题 | 10分**
8. (本题满分10分)

设奇函数 f(x)在<equation>[-1,1]</equation>上具有2阶导数，且 f(1)=1.证明：

I. 存在<equation>\xi \in(0,1)</equation>，使得<equation>f^{\prime}(\xi)=1;</equation>II. 存在<equation>\eta \in(-1,1)</equation>，使得<equation>f^{\prime\prime}(\eta)+f^{\prime}(\eta)=1.</equation>
**答案: **（18）（I）证明略；

（Ⅱ）证明略.
**解析: **证（I）由 f(x)为奇函数得 f(0)=0.由于 f(1)=1，且 f(x)在[-1,1]上可导，故由拉格朗日中值定理得，存在<equation>\xi \in(0,1)</equation>，使得<equation>f(1)-f(0)=f^{\prime}(\xi)</equation>，即<equation>f^{\prime}(\xi)=1.</equation>（Ⅱ）（法一）构造辅助函数<equation>g ( x )=f^{\prime} ( x )+f ( x )-x. g ( x )</equation>在[-1，1]上可导.

若能在[-1，1]上找到两个点<equation>x_{1}, x_{2}</equation>，使得<equation>g(x_{1})=g(x_{2})</equation>，则由罗尔定理可得，存在<equation>\eta \in</equation>（-1，1），<equation>g^{\prime}(\eta)=0</equation>，即<equation>f^{\prime\prime}(\eta)+f^{\prime}(\eta)=1.</equation>由于 f(x）是<equation>[-1,1]</equation>上的奇函数，故<equation>f(x)=-f(-x).</equation>该等式两端同时关于 x求导得<equation>f^{\prime}(x)=</equation><equation>f^{\prime}(-x).</equation>于是<equation>f^{\prime}(x)</equation>是<equation>[-1,1]</equation>上的偶函数.从而，<equation>g (1) = f ^ {\prime} (1) + f (1) - 1, \quad g (- 1) = f ^ {\prime} (- 1) + f (- 1) - (- 1) = f ^ {\prime} (1) - f (1) + 1.</equation>由于<equation>f(1) - 1 = 0</equation>，故<equation>g(1) = g(-1)</equation>由罗尔定理可知，存在<equation>\eta \in (-1,1)</equation>，<equation>g^{\prime}(\eta) = 0</equation>，即<equation>f^{\prime \prime}(\eta) + f^{\prime}(\eta) = 1.</equation>（法二）构造辅助函数<equation>G ( x ) = \mathrm{e}^{x} \left[ f^{\prime} ( x )-1 \right]. G ( x )</equation>在[-1，1]上可导.<equation>G ^ {\prime} (x) = \mathrm {e} ^ {x} \left[ f ^ {\prime} (x) - 1 \right] + \mathrm {e} ^ {x} f ^ {\prime \prime} (x) = \mathrm {e} ^ {x} \left[ f ^ {\prime \prime} (x) + f ^ {\prime} (x) - 1 \right].</equation>由于<equation>f ( x )</equation>是<equation>[-1,1]</equation>上的奇函数，同法一中的论证可知<equation>f^{\prime}(x)</equation>是<equation>[-1,1]</equation>上的偶函数.<equation>\xi</equation>为第（I）问中所得，满足<equation>f^{\prime}(\xi)=1</equation>，从而<equation>f^{\prime}(-\xi)=f^{\prime}(\xi)=1.</equation>因此<equation>G(\xi)=G(-\xi)=0.</equation>由罗尔定理，存在<equation>\eta\in(-1,1)</equation>，使得<equation>G^{\prime}(\eta)=0</equation>.又因为<equation>\mathrm{e}^{\eta}>0</equation>，所以<equation>f^{\prime\prime}(\eta)+f^{\prime}(\eta)-1=0</equation>，即<equation>f^{\prime\prime}(\eta)+f^{\prime}(\eta)=1.</equation>

---

**2010年第21题 | 解答题 | 11分**
21. (本题满分10分)

假设函数 f(x)在闭区间[0,1]上连续，在开区间（0，1）内可导，且 f(0)=0，f(1)=<equation>\frac{1}{3}</equation>.证明：存在<equation>\xi \in\left(0,\frac{1}{2}\right),\eta \in</equation><equation>\left(\frac{1}{2},1\right)</equation>，使得：<equation>f^{\prime}(\xi)+f^{\prime}(\eta)=\xi^{2}+\eta^{2}.</equation>
**解析: **证构造辅助函数<equation>g ( x )=f ( x )-\frac{1}{3} x^{3}</equation>，则 g(x)在[0，1]上连续，(0，1)内可导，<equation>g^{\prime} ( x )=</equation><equation>f^{\prime} ( x )-x^{2}.</equation>，于是，所要证的结论变为“存在<equation>\xi\in\left(0,\frac{1}{2}\right),\eta\in\left(\frac{1}{2},1\right)</equation>，使得<equation>g^{\prime} (\xi)+g^{\prime} (\eta)=0.</equation>”首先，由题设，有<equation>g ( 0 )=f ( 0 )=0</equation>，<equation>g ( 1 )=f ( 1 )-\frac{1}{3}=0.</equation>分别在<equation>\left[0,\frac{1}{2}\right]</equation>和<equation>\left[\frac{1}{2},1\right]</equation>上对 g(x)使用拉格朗日中值定理可得，存在<equation>\xi\in\left(0,\frac{1}{2}\right),\eta\in</equation><equation>\left(\frac{1}{2},1\right)</equation>，使得<equation>g \left(\frac {1}{2}\right) - g (0) = \frac {1}{2} g ^ {\prime} (\xi), \quad g (1) - g \left(\frac {1}{2}\right) = \frac {1}{2} g ^ {\prime} (\eta).</equation>由（1）式，得<equation>g ( 1 ) - g ( 0 ) = \frac { 1 } { 2 } \left[ g^{\prime} ( \xi ) + g^{\prime} ( \eta ) \right]</equation>.又因为<equation>g ( 0 ) = g ( 1 ) = 0</equation>，所以<equation>g^{\prime} (\xi) + g^{\prime} (\eta) = 0</equation>即<equation>f^{\prime} (\xi) + f^{\prime} (\eta) = \xi^{2} + \eta^{2}.</equation>

---

**2009年第21题 | 解答题 | 11分**

I. 证明拉格朗日中值定理：若函数 f(x)在<equation>[a,b]</equation>上连续，在（a,b）内可导，则存在点<equation>\xi\in(a,b)</equation>，使得<equation>f(b)-f(a)=f^{\prime}(\xi)(b-a).</equation>II. 证明：若函数 f(x)在 x=0处连续，在<equation>(0,\delta)(\delta>0)</equation>内可导，且<equation>\lim_{x\rightarrow 0^{+}}f^{\prime}(x)=A</equation>，则<equation>f_{+}^{\prime}(0)</equation>存在，且<equation>f_{+}^{\prime}(0)=A.</equation>
**答案: **（21）（Ⅰ）证明略.

（Ⅱ）证明略.
**解析: **证（ I ）令<equation>\varphi (x) = f (x) - f (a) - \frac {f (b) - f (a)}{b - a} (x - a).</equation><equation>\varphi (x)</equation>在<equation>[a,b]</equation>上连续，在<equation>(a,b)</equation>内可导.计算得<equation>\varphi (a) = 0,\varphi (b) = 0.</equation>对<equation>\varphi(x)</equation>使用罗尔定理得，存在<equation>\xi\in(a,b)</equation>，使得<equation>\varphi^{\prime}(\xi)=0</equation>，即<equation>f^{\prime}(\xi)-\frac{f(b)-f(a)}{b-a}=0.</equation>因此，存在<equation>\xi\in(a,b)</equation>，使得<equation>f(b)-f(a)=f^{\prime}(\xi)(b-a).</equation>（Ⅱ）（法一）根据右侧导数的定义，<equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x}.</equation>由拉格朗日中值定理，对任意的<equation>x\in (0,\delta)</equation>，都存在<equation>\xi_{x}\in (0,x)</equation>，使得<equation>f (x) - f (0) = f ^ {\prime} \left(\xi_ {x}\right) x.</equation>从而<equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x} = \lim _ {x \rightarrow 0 ^ {+}} \frac {f ^ {\prime} \left(\xi_ {x}\right) x}{x} = \lim _ {0 < \xi_ {x} < x, \atop x \rightarrow 0 ^ {+}} f ^ {\prime} \left(\xi_ {x}\right).</equation>由于<equation>x\to 0^{+}</equation>，故<equation>\xi_{x}\to 0^{+}</equation>.因此，<equation>f _ {+} ^ {\prime} (0) = \lim _ {0 < \xi_ {x} < x, x \rightarrow 0 ^ {+}} f ^ {\prime} \left(\xi_ {x}\right) = \lim _ {x \rightarrow 0 ^ {+}} f ^ {\prime} (x) = A.</equation>（法二）由洛必达法则，<equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {f ^ {\prime} (x)}{1} = A.</equation>因此，<equation>f_{+}^{\prime}(0)</equation>存在，且等于A.

---


#### 导数的应用

**2024年第11题 | 填空题 | 5分**
11. 曲线<equation>y^{2}=x</equation>在点(0,0)处的曲率圆方程为 ___
**答案: **<equation>\left(x - \frac {1}{2}\right) ^ {2} + y ^ {2} = \frac {1}{4}</equation>
**解析: **解曲线<equation>y^{2}=x</equation>的参数方程可写为<equation>\left\{\begin{array}{l l}x=y^{2},\\ y=y,\end{array}\right.</equation>故<equation>\frac{\mathrm{d}x}{\mathrm{d}y}=2y,\frac{\mathrm{d}^{2}x}{\mathrm{d}y^{2}}=2,\frac{\mathrm{d}y}{\mathrm{d}y}=1,\frac{\mathrm{d}^{2}y}{\mathrm{d}y^{2}}=0</equation>曲线上点 （x,y）处的曲率<equation>K=\frac{\left|2y\cdot0-2\cdot1\right|}{\left[(2y)^{2}+1^{2}\right]^{\frac{3}{2}}}=\frac{2}{\left(4y^{2}+1\right)^{\frac{3}{2}}}.</equation>(1)

由（1）式可得，点（0,0）处的曲率<equation>K=\frac{2}{(0+1)^{\frac{3}{2}}}=2</equation>，故该点处的曲率半径为<equation>\frac{1}{K}=\frac{1}{2}.</equation>由于曲线在点（0,0）处的切线为y轴，故法线为x轴，曲率中心在点<equation>\left(\frac{1}{2},0\right).</equation>因此，所求曲率圆方程为<equation>\left(x-\frac{1}{2}\right)^{2}+y^{2}=\frac{1}{4}.</equation>

---

**2024年第15题 | 填空题 | 5分**
15. 设某物体以速度<equation>v ( t )=t+k \sin \pi t</equation>做直线运动. 若它从 t=0到 t=3的时间段内平均速度是<equation>\frac{5}{2}</equation>，则 k=___
**答案: **##<equation>\frac{3}{2}\pi</equation>
**解析: **解 由函数的平均值的定义可知，物体从 t=0到 t=3的时间段内平均速度<equation>\bar{v} ( t )=\frac{\int_{0}^{3} v ( t ) \mathrm{d} t}{3}.</equation>于是，由平均速度为<equation>\frac{5}{2}</equation>可得<equation>\frac {\int_ {0} ^ {3} v (t) \mathrm {d} t}{3} = \frac {5}{2}, \quad \text {即} \int_ {0} ^ {3} (t + k \sin \pi t) \mathrm {d} t = \frac {1 5}{2}.</equation>由于<equation>\int_ {0} ^ {3} \left(t + k \sin \pi t\right) \mathrm {d} t = \left(\frac {t ^ {2}}{2} - \frac {k}{\pi} \cos \pi t\right) \Bigg | _ {0} ^ {3} = \frac {9}{2} - \frac {k}{\pi} (- 1 - 1) = \frac {9}{2} + \frac {2 k}{\pi},</equation>故由（1）式可得<equation>\frac{9}{2} +\frac{2k}{\pi} = \frac{15}{2}</equation>，解得<equation>k = \frac{3\pi}{2}</equation>

---

**2023年第14题 | 填空题 | 5分**
14. 曲线<equation>3 x^{3}=y^{5}+2 y^{3}</equation>在<equation>x=1</equation>对应点处的法线斜率为 ___
**答案: **# 11 9
**解析: **解记<equation>f ( y )=y^{5}+2 y^{3}-3</equation>，则<equation>f ( 1 )=0</equation>.又因为<equation>f^{\prime}(y)=5 y^{4}+6 y^{2}\geqslant 0</equation>，所以f(y）单调增加，<equation>y=1</equation>是f(y）的唯一零点.由于当且仅当 x=1时，<equation>3 x^{3}=3</equation>，故当且仅当 y=1时，x=1，从而曲线<equation>3 x^{3}=y^{5}+2 y^{3}</equation>在 x=1处的对应点为点（1,1）.

对方程<equation>3 x^{3}=y^{5}+2 y^{3}</equation>两端关于 x求导，可得<equation>9 x ^ {2} = \left(5 y ^ {4} + 6 y ^ {2}\right) y ^ {\prime}.</equation>将<equation>x = 1,y = 1</equation>代入（1）式，可得<equation>9 = 11y^{\prime}</equation>.因此，<equation>y^{\prime}(1) = \frac{9}{11}</equation>即<equation>x = 1</equation>对应点处的切线斜率为<equation>\frac{9}{11}</equation>.

由于同一点处的切线与法线相互垂直，此时切线斜率与法线斜率的乘积为-1，故 x=1对应点处的法线斜率为<equation>-\frac{11}{9}.</equation>

---

**2021年第3题 | 选择题 | 5分 | 答案: C**
3. 有一圆柱体，底面半径与高随时间的变化率分别为<equation>2 \mathrm{~cm} / \mathrm{s},-3 \mathrm{~cm} / \mathrm{s}</equation>，当底面半径为10cm，高为5cm时，圆体的体积与表面积随时间的变化速率为（    )

A.<equation>1 2 5 \pi \mathrm{c m}^{3} / \mathrm{s},4 0 \pi \mathrm{c m}^{2} / \mathrm{s}</equation>B.<equation>1 2 5 \pi \mathrm{c m}^{3} / \mathrm{s},-4 0 \pi \mathrm{c m}^{2} / \mathrm{s}</equation>C.<equation>- 1 0 0 \pi \mathrm{c m}^{3} / \mathrm{s},4 0 \pi \mathrm{c m}^{2} / \mathrm{s}</equation>D.<equation>- 1 0 0 \pi \mathrm{c m}^{3} / \mathrm{s},-4 0 \pi \mathrm{c m}^{2} / \mathrm{s}</equation>
答案: C
**解析: **解设圆柱体的底面半径为 r(t)，高为 h(t)，则圆柱体的体积<equation>V ( t )=\pi r^{2} ( t ) h ( t )</equation>，表面积<equation>S ( t )=2 \pi r ( t ) h ( t )+2 \pi r^{2} ( t ).</equation>由链式法则，<equation>\frac {\mathrm {d} V}{\mathrm {d} t} = \frac {\partial V}{\partial r} \frac {\mathrm {d} r}{\mathrm {d} t} + \frac {\partial V}{\partial h} \frac {\mathrm {d} h}{\mathrm {d} t} = 2 \pi r h \frac {\mathrm {d} r}{\mathrm {d} t} + \pi r ^ {2} \frac {\mathrm {d} h}{\mathrm {d} t}.</equation><equation>\frac {\mathrm {d} S}{\mathrm {d} t} = \frac {\partial S}{\partial r} \frac {\mathrm {d} r}{\mathrm {d} t} + \frac {\partial S}{\partial h} \frac {\mathrm {d} h}{\mathrm {d} t} = (2 \pi h + 4 \pi r) \frac {\mathrm {d} r}{\mathrm {d} t} + 2 \pi r \frac {\mathrm {d} h}{\mathrm {d} t}.</equation>代入 r=10 cm,h=5 cm<equation>\frac{\mathrm{d} r}{\mathrm{d} t}=2 \mathrm{~ c m / s}, \frac{\mathrm{d} h}{\mathrm{d} t}=-3 \mathrm{~ c m / s}</equation>可得<equation>\frac {\mathrm {d} V}{\mathrm {d} t} = 2 \pi \times 1 0 \times 5 \times 2 + \pi \times 1 0 0 \times (- 3) = 2 0 0 \pi - 3 0 0 \pi = - 1 0 0 \pi \left(\mathrm {c m} ^ {3} / \mathrm {s}\right).</equation><equation>\frac {\mathrm {d} S}{\mathrm {d} t} = \left(2 \pi \times 5 + 4 \pi \times 1 0\right) \times 2 + 2 \pi \times 1 0 \times (- 3) = 1 0 0 \pi - 6 0 \pi = 4 0 \pi \left(\mathrm {c m} ^ {2} / \mathrm {s}\right).</equation>因此，应选C.

---

**2019年第6题 | 选择题 | 4分 | 答案: A**
6. 已知 f(x), g(x)二阶可导，且2阶导函数在 x=a处连续，则<equation>\lim_{x\rightarrow a}\frac{f(x)-g(x)}{(x-a)^{2}}=0</equation>是曲线 y=f(x)和 y=g(x)在 x=a对应的点处相切且曲率相等的（    ）

A. 充分非必要条件 B. 充分必要条件

C. 必要非充分条件 D. 既非充分又非必要条件
答案: A
**解析: **解 由<equation>f ( x )</equation>，<equation>g ( x )</equation>在<equation>x=a</equation>处的二阶泰勒公式可得，<equation>f (x) = f (a) + f ^ {\prime} (a) (x - a) + \frac {f ^ {\prime \prime} (a)}{2} (x - a) ^ {2} + o \left(\left(x - a\right) ^ {2}\right),</equation><equation>g (x) = g (a) + g ^ {\prime} (a) (x - a) + \frac {g ^ {\prime \prime} (a)}{2} (x - a) ^ {2} + o \left(\left(x - a\right) ^ {2}\right).</equation>代入<equation>\lim_{x\to a}\frac{f(x) - g(x)}{(x - a)^2}</equation>可得，<equation>\lim_{x\to a}\frac{f(x) - g(x)}{(x - a)^2} = \lim_{x\to a}\frac{[f(a) - g(a)] + [f'(a) - g'(a)](x - a) + \frac{f''(a) - g''(a)}{2}(x - a)^2 + o((x - a)^2)}{(x - a)^2}.</equation>由上式可知<equation>\lim_{x\to a}\frac{f(x) - g(x)}{(x - a)^2} = 0</equation>当且仅当<equation>\left\{ \begin{array}{l} f(a) = g(a), \\ f'(a) = g'(a), \\ f''(a) = g''(a). \end{array} \right.</equation>曲线<equation>y=f(x)</equation>与<equation>y=g(x)</equation>在<equation>x=a</equation>对应的点处相切当且仅当<equation>\left\{ \begin{array}{l l} f(a)=g(a), \\ f^{\prime}(a)=g^{\prime}(a). \end{array} \right.</equation>又由曲率的计算公式<equation>K=\frac{\left|y^{\prime \prime}\right|}{\left[1+(y^{\prime})^{2}\right]^{\frac{3}{2}}}</equation>以及<equation>f^{\prime \prime}(a)=g^{\prime \prime}(a)</equation>可得两条曲线在<equation>x=a</equation>对应的点处曲率相等.

因此，<equation>\lim_{x\to a}\frac{f(x)-g(x)}{(x-a)^{2}}=0</equation>是曲线 y=f(x）和 y=g(x）在 x=a对应的点处相切且曲率相等的充分条件.

注意到两曲线在 x=a对应的点处曲率相等只能说明<equation>|f^{\prime \prime}(a)|=|g^{\prime \prime}(a)|</equation>，但并不能推出<equation>f^{\prime \prime}(a)=g^{\prime \prime}(a)</equation>，故<equation>\lim_{x\to a}\frac{f(x)-g(x)}{(x-a)^{2}}=0</equation>不是曲线 y=f(x)和 y=g(x)在 x=a对应的点处相切且曲率相等的必要条件.

例如：取<equation>f ( x )=1-\sqrt{1-x^{2}}</equation><equation>g ( x )=-1+\sqrt{1-x^{2}}</equation><equation>y=f(x), y=g(x)</equation>这两条曲线均为半径为1的半圆弧（圆弧上各点的曲率半径均为1）.于是，各点处曲率相等，均等于1.如图所示，这两条曲线在原点处相切，但<equation>y=f(x)</equation>在[-1，1]上是凹曲线，<equation>y=g(x)</equation>在[-1，1]上是凸曲线，<equation>f^{\prime \prime}(0)\neq g^{\prime \prime}(0).</equation>综上所述，应选A.

---

**2019年第10题 | 填空题 | 4分**
10. 曲线<equation>\left\{ \begin{array}{l} x = t - \sin t \\ y = 1 - \cos t \end{array} \right.</equation>在<equation>t=\frac{3\pi}{2}</equation>对应点处的切线在 y 轴上的截距为 ___
**答案: **#<equation>\frac{3\pi}{2}+2.</equation>
**解析: **分析 本题主要考查由参数方程确定的函数求导以及导数的几何意义.

如图所示，本题中的曲线为摆线，可利用由参数方程确定的函数求导计算<equation>t=\frac{3\pi}{2}</equation>对应点处的导数值，从而得到该点处的切线方程，再计算该切线在 y轴上的截距.

解 计算<equation>t=\frac{3\pi}{2}</equation>对应点处的导数值.<equation>\left. \frac {\mathrm {d} y}{\mathrm {d} x} \right| _ {t = \frac {3 \pi}{2}} = \left. \frac {\mathrm {d} y}{\mathrm {d} t} \right| / \left. \frac {\mathrm {d} x}{\mathrm {d} t} \right| _ {t = \frac {3 \pi}{2}} = \left. \frac {\sin t}{1 - \cos t} \right| _ {t = \frac {3 \pi}{2}} = \frac {- 1}{1} = - 1.</equation>当 t =<equation>\frac{3\pi}{2}</equation>时，x =<equation>\frac{3\pi}{2}+1</equation>，y=1.于是，该点处的切线方程为 y-1=-<equation>\left(x-\frac{3\pi}{2}-1\right).</equation>令 x=0，可得 y =<equation>\frac{3\pi}{2}+2.</equation>因此，所求截距为<equation>\frac{3\pi}{2}+2.</equation>

---

**2018年第12题 | 填空题 | 4分**
12. 曲线<equation>\left\{ \begin{array}{l} x = \cos^ {3} t \\ y = \sin^ {3} t \end{array} \right.</equation>
**答案: **# 2 3.
**解析: **解分别计算<equation>\frac{\mathrm{d} y}{\mathrm{d} x},\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}.</equation><equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {3 \sin^ {2} t \cos t}{- 3 \cos^ {2} t \sin t} = - \tan t,</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\mathrm {d} \left(\frac {\mathrm {d} y}{\mathrm {d} x}\right)}{\mathrm {d} t} / \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {- \sec^ {2} t}{- 3 \cos^ {2} t \sin t} = \frac {\sec^ {4} t}{3 \sin t}.</equation>当 t =<equation>\frac{\pi}{4}</equation>时，<equation>\left. \frac{\mathrm{d} y}{\mathrm{d} x}\right|_{t=\frac{\pi}{4}}=-1</equation><equation>\left. \frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\right|_{t=\frac{\pi}{4}}=\frac{(\sqrt{2})^{4}}{3\times \frac{\sqrt{2}}{2}}=\frac{4\sqrt{2}}{3}</equation>根据曲率的计算公式，所求曲率<equation>= \frac{\frac{4\sqrt{2}}{3}}{\left[ 1+(-1)^{2}\right]^{\frac{3}{2}}}=\frac{4\sqrt{2}}{3}\bigg /2\sqrt{2}=\frac{2}{3}.</equation>

---

**2016年第13题 | 填空题 | 4分**
13. 已知动点 P在曲线<equation>y=x^{3}</equation>上运动，记坐标原点与点 P间的距离为 l. 若点 P的横坐标对时间的变化率为常数<equation>v_{0}</equation>，则当点 P运动到点（1,1）时，l对时间的变化率是 ___
**答案: **##<equation>2 \sqrt{2} v_{0}.</equation>
**解析: **解设点 P的坐标为<equation>( x,x^{3} )</equation>，则<equation>l=\sqrt{x^{2}+x^{6}}</equation>点 P的横坐标对时间的变化率为<equation>\frac{\mathrm{d} x}{\mathrm{d} t}=v_{0}.</equation>记 l对时间的变化率为<equation>\frac{\mathrm{d} l}{\mathrm{d} t}.</equation>由链式法则得<equation>\frac {\mathrm {d} l}{\mathrm {d} t} = \frac {\mathrm {d} l}{\mathrm {d} x} \cdot \frac {\mathrm {d} x}{\mathrm {d} t} = \frac {1}{2} \cdot \frac {6 x ^ {5} + 2 x}{\sqrt {x ^ {2} + x ^ {6}}} \cdot v _ {0}.</equation>当 x=1时，代入（1）式得<equation>\frac{\mathrm{d} l}{\mathrm{d} t}\bigg|_{x=1}=\frac{4}{\sqrt{2}} v_{0}=2\sqrt{2} v_{0}.</equation>

---

**2014年第4题 | 选择题 | 4分 | 答案: C**
4. 曲线<equation>\left\{\begin{array}{l l}x=t^{2}+7,\\y=t^{2}+4 t+1\end{array}\right.</equation>上对应于 t=1的点处的曲率半径是（    )

A.<equation>\frac{\sqrt{1 0}}{5 0}</equation>B.<equation>\frac{\sqrt{1 0}}{1 0 0}</equation>C.<equation>1 0 \sqrt{1 0}</equation>D.<equation>5 \sqrt{1 0}</equation>
答案: C
**解析: **解 先求对应于<equation>t = 1</equation>的点处的曲率，需要得到该点处的<equation>y^{\prime}, y^{\prime \prime}</equation>.<equation>\left. \frac {\mathrm {d} y}{\mathrm {d} x} \right| _ {t = 1} = \left. \frac {\mathrm {d} y}{\mathrm {d} t} \right/ \left. \frac {\mathrm {d} x}{\mathrm {d} t} \right| _ {t = 1} = \left. \frac {2 t + 4}{2 t} \right| _ {t = 1} = \left. \frac {t + 2}{t} \right| _ {t = 1} = 3,</equation><equation>\left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {t = 1} = \frac {\mathrm {d} \left(\frac {\mathrm {d} y}{\mathrm {d} x}\right)}{\mathrm {d} t} / \left. \frac {\mathrm {d} x}{\mathrm {d} t} \right| _ {t = 1} = \frac {- \frac {2}{t ^ {2}}}{2 t} \left| _ {t = 1} = - \frac {1}{t ^ {3}} \right| _ {t = 1} = - 1.</equation>因此，该点处的曲率半径<equation>\rho = \frac{1}{K} = \frac{[1 + (y^{\prime})^{2}]^{\frac{3}{2}}}{|y^{\prime \prime}|} = \frac{(1 + 3^{2})^{\frac{3}{2}}}{|-1|} = 10\sqrt{10}</equation>. 应选C.

---

**2014年第12题 | 填空题 | 4分**
12. 曲线<equation>L</equation>的极坐标方程是<equation>r=\theta</equation>, 则<equation>L</equation>在点<equation>(r,\theta)=\left(\frac{\pi}{2},\frac{\pi}{2}\right)</equation>处的切线的直角坐标方程是 ___
**答案: **<equation>\frac {2}{\pi} x + y - \frac {\pi}{2} = 0.</equation>
**解析: **解（法一）由<equation>\left\{\begin{array}{l l}x=r\cos \theta \\ y=r\sin \theta\end{array}\right.</equation>以及r=得，<equation>\left\{\begin{array}{l l}x=\theta\cos \theta \\ y=\theta\sin \theta.\end{array}\right.</equation>于是，根据由参数方程确定的函数的求导公式，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\mathrm {d} y}{\mathrm {d} \theta} / \frac {\mathrm {d} x}{\mathrm {d} \theta} = \frac {\sin \theta + \theta \cos \theta}{\cos \theta - \theta \sin \theta}.</equation>于是，<equation>\frac{\mathrm{d}y}{\mathrm{d}x}\bigg|_{\theta = \frac{\pi}{2}} = \frac{1 + 0}{0 - \frac{\pi}{2}} = -\frac{2}{\pi}.</equation>由坐标变换公式得，极坐标系下的点<equation>\left(\frac{\pi}{2},\frac{\pi}{2}\right)</equation>对应直角坐标系下的点<equation>\left(0,\frac{\pi}{2}\right).</equation>因此，所求切线的点斜式方程为<equation>y-\frac{\pi}{2}=-\frac{2}{\pi} (x-0)</equation>即<equation>\frac{2}{\pi} x+y-\frac{\pi}{2}=0.</equation>（法二）曲线<equation>r = \theta</equation>是阿基米德螺线.这是一条光滑曲线.

由<equation>\left\{\begin{array}{l}x=r\cos \theta,\\ y=r\sin \theta\end{array}\right.</equation>可得，当<equation>\theta\in\left[0,\frac{\pi}{2}\right)</equation>时，<equation>r=\sqrt{x^{2}+y^{2}},</equation><equation>\theta=\arctan \frac{y}{x}.</equation>将该曲线方程写成直角坐标系下的形式，可得<equation>\sqrt{x^{2}+y^{2}}=\arctan \frac{y}{x}</equation>即当<equation>\theta\in\left[0,\frac{\pi}{2}\right)</equation>时，曲线<equation>r=\theta</equation>的直角坐标方程为<equation>\sqrt{x^{2}+y^{2}}=\arctan \frac{y}{x}.</equation>由（r，<equation>\theta)=\left(\frac{\pi}{2},\frac{\pi}{2}\right)</equation>得（x，y）<equation>=\left(0,\frac{\pi}{2}\right).</equation>虽然点<equation>\left(0,\frac{\pi}{2}\right)</equation>并不满足该方程，但由于曲线光滑，故该点处的斜率等于<equation>\lim_{x\to 0^{+}}y^{\prime}(x).</equation>对<equation>\sqrt{x^{2}+y^{2}}=\arctan \frac{y}{x}</equation>两端关于 x求导得<equation>\frac {2 x + 2 y y ^ {\prime}}{2 \sqrt {x ^ {2} + y ^ {2}}} = \frac {1}{1 + \left(\frac {y}{x}\right) ^ {2}} \cdot \frac {x y ^ {\prime} - y}{x ^ {2}}.</equation>化简得<equation>\frac {x y ^ {\prime} - y}{\sqrt {x ^ {2} + y ^ {2}}} = x ^ {-} + y y ^ {\prime}.</equation>由（1）式可得<equation>( x-y\sqrt{x^{2}+y^{2}}) y^{\prime}=x\sqrt{x^{2}+y^{2}}+y.</equation>令<equation>x\to0^{+}</equation>，并代入<equation>\lim_{x\to0^{+}}x=0,\lim_{x\to0^{+}}y(x)=\frac{\pi}{2}</equation>，可得<equation>\lim_{x\to0^{+}}y^{\prime}(x)=-\frac{2}{\pi}.</equation>因此，所求切线方程为<equation>y-\frac{\pi}{2}=- \frac{2}{\pi} x</equation>即<equation>\frac{2}{\pi} x+y-\frac{\pi}{2}=0.</equation>

---

**2013年第12题 | 填空题 | 4分**
12. 曲线<equation>\begin{aligned} x &= \arctan t, \\ y &= \ln \sqrt {1 + t ^ {2}} \end{aligned}</equation>上对应于<equation>t=1</equation>的点处的法线方程为 ___
**答案: **<equation>x+y=\frac{\pi}{4}+\frac{1}{2}\ln 2.</equation>
**解析: **曲线上对应于<equation>t = 1</equation>的点处的切线斜率为<equation>\left. \frac {\mathrm {d} y}{\mathrm {d} x} \right| _ {t = 1} = \frac {y ^ {\prime} (1)}{x ^ {\prime} (1)} = \frac {\frac {1}{2} \cdot \frac {2 t}{1 + t ^ {2}}}{\frac {1}{1 + t ^ {2}}} \Bigg | _ {t = 1} = 1,</equation>故曲线上对应于<equation>t=1</equation>的点处的法线斜率为-1.

又因为当 t=1时，<equation>x=\frac{\pi}{4}</equation><equation>y=\frac{1}{2}\ln 2</equation>，所以该法线过点<equation>\left(\frac{\pi}{4},\frac{1}{2}\ln 2\right)</equation>，从而可写出所求法线的点斜式方程<equation>y-\frac{1}{2}\ln 2=-\left(x-\frac{\pi}{4}\right)</equation>，即<equation>x+y=\frac{\pi}{4}+\frac{1}{2}\ln 2.</equation>

---

**2012年第13题 | 填空题 | 4分**
13. 曲线<equation>y=x^{2}+x \ ( x<0 )</equation>上曲率为<equation>\frac{\sqrt{2}}{2}</equation>的点的坐标是 ___
**答案: **## (-1,0).
**解析: **利用曲线方程可求得<equation>y^{\prime}=2 x+1</equation><equation>y^{\prime\prime}=2</equation>，故<equation>K = \frac {2}{\left[ 1 + \left(2 x + 1\right) ^ {2} \right] ^ {\frac {3}{2}}} = \frac {\sqrt {2}}{2}.</equation>由此可求得<equation>(2x + 1)^{2} = 1</equation>，故<equation>x = 0</equation>或<equation>x = -1</equation>.又因为<equation>x < 0</equation>，所以<equation>x = -1</equation>，此时<equation>y = 0</equation>因此，所求点的坐标为（-1，0）.

---

**2010年第3题 | 选择题 | 4分 | 答案: C**
3. 曲线<equation>y=x^{2}</equation>与曲线<equation>y=a\ln x \ (a\neq0)</equation>相切，则 a=（    ）

A. 4e B. 3e C. 2e D. e
答案: C
**解析: **解 若两曲线的公切点为<equation>\left(x_{0}, y_{0}\right)</equation>，则点<equation>\left(x_{0}, y_{0}\right)</equation>满足<equation>\left\{ \begin{array}{l} y _ {0} = x _ {0} ^ {2}, \\ y _ {0} = a \ln x _ {0} \\ 2 x _ {0} = \frac {a}{x _ {0}}. \end{array} \right.</equation>解上述方程组得，<equation>a=2\mathrm{e},\ x_{0}=\sqrt{\mathrm{e}},y_{0}=\mathrm{e}.</equation>应选C.

---

**2010年第13题 | 填空题 | 4分**
13. 已知一个长方形的长 l以 2 cm/s的速率增加，宽 w以 3 cm/s的速率增加，则当 l=12 cm，w=5 cm时，它的对角线增加的速率为___
**答案: **3 cm/s.
**解析: **解 设对角线长为 s（t），则<equation>s ^ {2} (t) = l ^ {2} (t) + w ^ {2} (t).</equation>等式两端同时关于 t 求导，得<equation>s \frac {\mathrm {d} s}{\mathrm {d} t} = l \frac {\mathrm {d} l}{\mathrm {d} t} + w \frac {\mathrm {d} w}{\mathrm {d} t}.</equation>当<equation>l = 12\mathrm{cm},w = 5\mathrm{cm}</equation>时，<equation>s = \sqrt{12^{2} + 5^{2}}\mathrm{cm} = 13\mathrm{cm}</equation>. 代入（1）式得<equation>1 3 \frac {\mathrm {d} s}{\mathrm {d} t} = 1 2 \times 2 + 5 \times 3.</equation>因此，<equation>\frac{\mathrm{d}s}{\mathrm{d}t}=3\mathrm{cm / s}.</equation>

---

**2009年第5题 | 选择题 | 4分 | 答案: B**
5. 若<equation>f^{\prime\prime}(x)</equation>不变号，且曲线<equation>y=f(x)</equation>在点（1，1）处的曲率圆为<equation>x^{2}+y^{2}=2</equation>，则函数 f(x)在区间（1，2）内（    ）

A. 有极值点，无零点 B. 无极值点，有零点 C. 有极值点，有零点 D. 无极值点，无零点
答案: B
**解析: **解（法一）由于曲线<equation>y=f(x)</equation>在点（1，1）附近的凹凸性与点 （1，1）处的曲率圆的凹凸性一致，而曲率圆为<equation>x^{2}+y^{2}=2</equation>，是凸曲线，故<equation>y^{\prime \prime}<0.</equation>考虑曲线在点（1，1）处的切线.

连接点（0，0）和点（1，1）的半径为点（1，1）处的法线，该法线斜率为<equation>\frac{1 - 0}{1 - 0} = 1</equation>，于是点（1，1）处的切线斜率为-1，即<equation>f^{\prime}(1) = -1.</equation>由于<equation>f^{\prime \prime}(x)</equation>不变号，故在区间（1，2）上，仍有<equation>f^{\prime \prime}(x)<0</equation>，从而<equation>f^{\prime}(x)</equation>在（1，2）上单调减少。又因为<equation>f^{\prime}(1)=-1<0</equation>，所以<equation>f^{\prime}(x)</equation>在（1，2）上恒小于零.于是 f(x)在（1，2）上单调减少.因此， f(x)在（1，2）上没有极值点.

再考虑<equation>f ( x )</equation>在（1，2）上的零点情况.

由拉格朗日中值定理知，存在<equation>\xi\in(1,2)</equation>，使得<equation>f(2)-f(1)=f^{\prime}(\xi)</equation>，即<equation>f(2)=1+f^{\prime}(\xi).</equation>由于<equation>f^{\prime}(x)</equation>在（1，2）上单调减少，且<equation>f^{\prime}(1)=-1</equation>，从而<equation>f^{\prime}(\xi)< - 1</equation>，故<equation>f(2)=1+f^{\prime}(\xi)< 0.</equation>因为<equation>f(1)=1>0,f(2)<0</equation>，所以由连续函数的介值定理知，<equation>f(x)</equation>在（1，2）上存在零点因此，<equation>f(x)</equation>在（1，2）上有零点，没有极值点.应选B.

（法二）由于曲线<equation>y=f(x)</equation>在点（1，1）附近的方程可由它在点（1，1）处的曲率圆方程来近似，即<equation>x^{2}+y^{2}=2</equation>，故我们可以用该方程算出<equation>f^{\prime}(1)</equation>和<equation>f^{\prime \prime}(1).</equation>对<equation>x^{2} + y^{2} = 2</equation>两端关于 x求导，得<equation>2 x + 2 y y ^ {\prime} = 0.</equation>代入<equation>x = 1</equation>，<equation>y(1) = 1</equation>得，<equation>y^{\prime}(1) = -1</equation>.继续对（1）式两端求导，得<equation>2 + 2 \left(y ^ {\prime}\right) ^ {2} + 2 y y ^ {\prime \prime} = 0.</equation>代入<equation>x = 1, y(1) = 1, y^{\prime}(1) = -1</equation>得，<equation>y^{\prime \prime}(1) = -2.</equation>由于<equation>y^{\prime \prime}</equation>不变号，故<equation>y^{\prime \prime}</equation>在（1，2）上恒小于零.

其余论证<equation>y = f(x)</equation>在（1，2）上有零点，没有极值点的过程同法一.

---

**2009年第9题 | 填空题 | 4分**
9. 曲线<equation>\left\{ \begin{array}{l} x = \int_ {0} ^ {1 - t} \mathrm {e} ^ {- u ^ {2}} \mathrm {d} u, \\ y = t ^ {2} \ln \left(2 - t ^ {2}\right) \end{array} \right.</equation>在点 (0,0) 处的切线方程为 ___
**答案: **## y=2x.
**解析: **解 先求点（0，0）所对应的参数 t的值.
