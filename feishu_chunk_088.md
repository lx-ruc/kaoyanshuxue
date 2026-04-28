#### 可分离变量的微分方程与齐次方程

**2019年第10题 | 填空题 | 4分**

10. 微分方程<equation>2 y y^{\prime}-y^{2}-2=0</equation>满足条件<equation>y(0)=1</equation>的特解<equation>y=</equation>___

**解析:**解 整理原方程可得<equation>2 y \frac{\mathrm{d} y}{\mathrm{d} x}=y^{2}+2.</equation>分离变量可得<equation>\frac{2 y}{y^{2}+2}\mathrm{d} y=\mathrm{d} x.</equation>方程两端积分，<equation>\int \frac{2 y}{y^{2}+2}\mathrm{d} y=\int \frac{\mathrm{d}\left(y^{2}+2\right)}{y^{2}+2}=\ln \left(y^{2}+2\right)=x+C,</equation>其中 C为待定常数.

代入 x=0，<equation>y(0)=1</equation>可得，<equation>C=\ln 3</equation>.于是，<equation>y^{2}+2=3\mathrm{e}^{x}.</equation>又因为<equation>y(0)=1>0</equation>，所以<equation>y=\sqrt{3\mathrm{e}^{x}-2}.</equation>

---

**2014年第11题 | 填空题 | 4分**

11. 微分方程<equation>x y^{\prime}+y(\ln x-\ln y)=0</equation>满足条件<equation>y(1)=\mathrm{e}^{3}</equation>的解为<equation>y=</equation>___.

**答案:**##<equation>x \mathrm{e}^{2 x+1}.</equation>

**解析:**解 由题设中微分方程的表达式知 x > 0，y > 0，且原方程可化为<equation>y ^ {\prime} = \frac {y}{x} \ln \frac {y}{x},</equation>此为齐次方程. 令<equation>u=\frac{y}{x}</equation>，则<equation>y=ux,\frac{\mathrm{d}y}{\mathrm{d}x}=u+x\frac{\mathrm{d}u}{\mathrm{d}x}</equation>，于是方程（1）化为<equation>u + x \frac {\mathrm {d} u}{\mathrm {d} x} = u \ln u.</equation>分离变量，得到<equation>\frac {\mathrm {d} u}{u (\ln u - 1)} = \frac {\mathrm {d} x}{x},</equation>即<equation>\frac {\mathrm {d} (\ln u - 1)}{\ln u - 1} = \frac {\mathrm {d} x}{x}.</equation>对上式两端积分，得到于是<equation>\begin{aligned} \ln | \ln u - 1 | &= \ln x + C _ {1}, \\ \ln u - 1 &= C x, \end{aligned}</equation>其中<equation>C = \pm \mathrm{e}^{C_1}</equation>. 代回原变量<equation>u = \frac{y}{x}</equation>，得到原方程的通解为

注意这里由于 x > 0，y > 0，故 u > 0从而<equation>\int \frac{1}{u}=\ln u+C</equation>，但由于<equation>\ln u-1</equation>的正负无法判断，故<equation>\int \frac {\mathrm {d} (\ln u - 1)}{\ln u - 1} = \ln | \ln u - 1 | + C.</equation><equation>\ln \frac {y}{x} - 1 = C x.</equation>将<equation>y ( 1 ) = \mathrm{e}^{3}</equation>代入上式，得到<equation>C=2</equation>，于是<equation>\ln \frac{y}{x}=2x+1</equation>，从而所求初值问题的解为<equation>y = x \mathrm {e} ^ {2 x + 1}.</equation>

---


