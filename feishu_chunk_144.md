#### 差分方程

**2021年第14题 | 填空题 | 5分**

14. 差分方程<equation>\Delta y_{t} = t</equation>的通解为<equation>y_{t} =</equation>___

**答案:**<equation>\frac{1}{2} t^{2}-\frac{1}{2} t+C</equation>，其中C为任意常数.

**解析:**解（法一）由于<equation>\Delta y_{t}=y_{t+1}-y_{t}</equation>，故<equation>\Delta y_{t}=t</equation>等价于<equation>y_{t+1}-y_{t}=t</equation>，为一阶常系数非齐次线性差分方程.

因为<equation>a = 1</equation>，所以<equation>\tilde{y}_t = C</equation>为<equation>y_{t + 1} - y_t = 0</equation>的通解.

又因为自由项为 t，所以可设<equation>y_{t}^{*} = t \left(B_{0} + B_{1} t\right).</equation>代回<equation>y_{t+1}-y_{t}=t</equation>可得<equation>B _ {0} (t + 1) + B _ {1} (t + 1) ^ {2} - B _ {0} t - B _ {1} t ^ {2} = 2 B _ {1} t + B _ {1} + B _ {0} = t.</equation>于是，<equation>B_{1}=\frac{1}{2}, B_{0}=-\frac{1}{2}.</equation>从而，<equation>y_{t}^{*}=\frac{1}{2} t^{2}-\frac{1}{2} t.</equation>因此，原方程的通解为<equation>y_{t}=\frac{1}{2} t^{2}-\frac{1}{2} t+C</equation>，其中C为任意常数.

（法二）由已知条件可知，<equation>y_{t + 1} - y_{t} = t.</equation>于是，<equation>y _ {t} - y _ {t - 1} = t - 1, \quad y _ {t - 1} - y _ {t - 2} = t - 2, \quad \dots , \quad y _ {2} - y _ {1} = 1.</equation>从而，<equation>y _ {t} = \left(y _ {t} - y _ {t - 1}\right) + \left(y _ {t - 1} - y _ {t - 2}\right) + \dots + \left(y _ {2} - y _ {1}\right) + y _ {1} = \frac {t (t - 1)}{2} + y _ {1}.</equation>由于<equation>y_{1}</equation>可以取任意常数，故<equation>y_{t}=\frac{t(t-1)}{2}+C=\frac{1}{2} t^{2}-\frac{1}{2} t+C</equation>，其中C为任意常数.

---

**2018年第11题 | 填空题 | 4分**

11. 差分方程<equation>\Delta^{2} y_{x}-y_{x}=5</equation>的通解为 ___

**答案:**<equation>y_{x}=C2^{x}-5</equation>，其中C为任意常数.

**解析:**解 由于<equation>\Delta^{2} y_{x}=\Delta y_{x+1}-\Delta y_{x}</equation>，故<equation>\Delta^{2} y_{x}=\Delta y_{x+1}-\Delta y_{x}=\left(y_{x+2}-y_{x+1}\right)-\left(y_{x+1}-y_{x}\right)=y_{x+2}-2y_{x+1}+y_{x}.</equation>由<equation>\Delta^{2} y_{x}-y_{x}=5</equation>可得，<equation>y_{x+2}-2y_{x+1}=5</equation>即<equation>y_{x+1}-2y_{x}=5.</equation>下面用两种方法解<equation>y_{x + 1} - 2y_{x} = 5.</equation>（法一）这是一个一阶非齐次线性差分方程.该方程对应的齐次差分方程的通解为<equation>\tilde{y}_{x}=C2^{x}</equation>其中C为任意常数.

设原方程的一个特解为<equation>y_{x}^{*} = k</equation>，代入原方程得 k-2k=5.解得 k=-5.于是，特解为<equation>y_{x}^{*} = -5.</equation>因此，原方程的通解为<equation>y_{x} = C2^{x} - 5</equation>其中 C为任意常数.

（法二）由<equation>y_{x+1}-2 y_{x}=5</equation>可得，<equation>y_{x+1}+5=2 \left( y_{x}+5 \right).</equation>于是，<equation>\left\{y_{x}+5\right\}_{x \in \mathbf{N}}</equation>是一个首项为<equation>y_{0}+5</equation>公比为2的等比数列.记<equation>C=y_{0}+5</equation>，可得<equation>y_{x}+5=C2^{x}</equation>即<equation>y_{x}=C2^{x}-5.</equation>由于<equation>y_{0}</equation>可取任意常数，故C为任意常数.

---

**2017年第10题 | 填空题 | 4分**

10. 差分方程<equation>y_{t+1}-2y_{t}=2^{t}</equation>的通解为<equation>y_{t}=</equation>___.

**答案:**<equation>\left(C + \frac{1}{2} t\right)2^{t}</equation>，其中C为任意常数.

**解析:**解<equation>y_{t+1}-2 y_{t}=2^{t}</equation>对应的齐次方程为<equation>y_{t+1}-2 y_{t}=0</equation>，其通解为<equation>\widetilde{y}_{t}=C2^{t}</equation>其中C为任意常数设原方程的一个特解为<equation>y_{t}^{*} = k t 2^{t}</equation>，代入原方程得<equation>k ( t+1 ) 2^{t+1}-2 k t 2^{t}=2^{t}</equation>解得<equation>k=\frac{1}{2}</equation>于是，特解为<equation>y_{t}^{*} = \frac{1}{2} t 2^{t}</equation>因此，原方程的通解为<equation>y_{t} = \left(C + \frac{1}{2} t\right) 2^{t}</equation>其中C为任意常数.

---


