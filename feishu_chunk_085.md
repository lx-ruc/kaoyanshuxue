#### 其他方程

**2024年第14题 | 填空题 | 5分**

14. 微分方程<equation>y^{\prime}=\frac{1}{(x+y)^{2}}</equation>满足条件 y(1)=0的解为 ___

**答案:**<equation>\arctan (x + y) = y + \frac {\pi}{4}</equation>

**解析:**解 令<equation>u=x+y</equation>，则<equation>\frac{\mathrm{d}u}{\mathrm{d}x}=1+\frac{\mathrm{d}y}{\mathrm{d}x}</equation>，原方程化为<equation>\frac{\mathrm{d}u}{\mathrm{d}x}-1=\frac{1}{u^{2}}</equation>，即<equation>\frac{\mathrm{d}u}{\mathrm{d}x}=\frac{1+u^{2}}{u^{2}}.</equation>这是一个可分离变量的微分方程，分离变量可得<equation>\left(1-\frac{1}{1+u^{2}}\right)\mathrm{d}u=\mathrm{d}x.</equation>方程两端同时积分可得<equation>u-\arctan u=x+C.</equation>由<equation>y(1)=0</equation>可得，<equation>u(1)=1.</equation>代入<equation>u-\arctan u=x+C</equation>可得<equation>1-\frac{\pi}{4}=1+C,</equation>解得<equation>C=-\frac{\pi}{4}.</equation>于是，<equation>u-\arctan u=x-\frac{\pi}{4}.</equation>将<equation>u=x+y</equation>代回<equation>u-\arctan u=x-\frac{\pi}{4}</equation>并整理可得<equation>y-\arctan(x+y)+\frac{\pi}{4}=0.</equation>

---

**2021年第13题 | 填空题 | 5分**

13. 欧拉方程<equation>x^{2} y^{\prime \prime}+x y^{\prime}-4 y=0</equation>满足条件<equation>y(1)=1, y^{\prime}(1)=2</equation>的解为<equation>y=</equation>___.

**答案:**<equation>x^{2}.</equation>

**解析:**解 由初始条件<equation>y ( 1 ) = 1, y^{\prime} ( 1 ) = 2</equation>可知应在<equation>x > 0</equation>的范围内求解.

令<equation>x = \mathrm{e}^{t}</equation>. 于是，<equation>\frac {\mathrm {d} y}{\mathrm {d} t} = \frac {\mathrm {d} y}{\mathrm {d} x} \cdot \mathrm {e} ^ {t}.</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} t ^ {2}} = \frac {\mathrm {d} \left(\frac {\mathrm {d} y}{\mathrm {d} x} \cdot \mathrm {e} ^ {t}\right)}{\mathrm {d} t} = \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \cdot \frac {\mathrm {d} x}{\mathrm {d} t} \cdot \mathrm {e} ^ {t} + \frac {\mathrm {d} y}{\mathrm {d} x} \cdot \mathrm {e} ^ {t} = \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \cdot \mathrm {e} ^ {2 t} + \frac {\mathrm {d} y}{\mathrm {d} x} \cdot \mathrm {e} ^ {t} = \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \cdot \mathrm {e} ^ {2 t} + \frac {\mathrm {d} y}{\mathrm {d} t}.</equation>从而，<equation>y^{\prime} = \mathrm{e}^{-t}\frac{\mathrm{d}y}{\mathrm{d}t}, y^{\prime \prime} = \mathrm{e}^{-2t}\left(\frac{\mathrm{d}^{2}y}{\mathrm{d}t^{2}} - \frac{\mathrm{d}y}{\mathrm{d}t}\right).</equation>因此，<equation>xy^{\prime} = \frac{\mathrm{d}y}{\mathrm{d}t}, x^{2}y^{\prime \prime} = \frac{\mathrm{d}^{2}y}{\mathrm{d}t^{2}} - \frac{\mathrm{d}y}{\mathrm{d}t}.</equation>代入<equation>x^{2} y^{\prime \prime}+x y^{\prime}-4 y=0</equation>可得<equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} t ^ {2}} - \frac {\mathrm {d} y}{\mathrm {d} t} + \frac {\mathrm {d} y}{\mathrm {d} t} - 4 y = \frac {\mathrm {d} ^ {2} y}{\mathrm {d} t ^ {2}} - 4 y = 0.</equation><equation>\frac{\mathrm{d}^2y}{\mathrm{d}t^2} - 4y = 0</equation>是一个二阶常系数齐次线性微分方程，其特征方程为<equation>r^2 - 4 = 0</equation>，特征根为<equation>r_{1,2} = \pm 2.</equation>于是，该方程的解为<equation>y = C_{1}\mathrm{e}^{2t} + C_{2}\mathrm{e}^{-2t} = C_{1}x^{2} + C_{2}x^{-2}</equation>，其中<equation>C_{1},C_{2}</equation>为待定常数. 从而，<equation>y^{\prime} = 2C_{1}x - 2C_{2}x^{-3}.</equation>代入 y（1）=1可得<equation>1=C_{1}+C_{2}</equation>代入<equation>y^{\prime}(1)=2</equation>可得<equation>2=2 C_{1}-2 C_{2}</equation>解得<equation>C_{1}=1,C_{2}=0.</equation>综上所述，原方程的解为<equation>y=x^{2}.</equation>

---


