#### 假设检验

**2025年第10题 | 选择题 | 5分 | 答案: D**

10. 设<equation>X_{1}, X_{2}, \cdots, X_{n}</equation>为来自正态总体<equation>N (\mu ,2)</equation>的简单随机样本，记<equation>\bar{X}=\frac{1}{n}\sum_{i=1}^{n} X_{i}, Z_{\alpha}</equation>表示标准正态分布的上侧<equation>\alpha</equation>分位数，假设检验问题：<equation>H_{0}:\mu \leqslant 1, H_{1}:\mu >1</equation>的显著性水平为<equation>\alpha</equation>的检验的拒绝域为（    )

A.<equation>\left\{(X_{1},X_{2},\cdots,X_{n})\mid \bar{X}>1+\frac{2}{n}Z_{\alpha}\right\}</equation>B.<equation>\left\{(X_{1},X_{2},\cdots,X_{n})\mid \bar{X}>1+\frac{\sqrt{2}}{n}Z_{\alpha}\right\}</equation>C.<equation>\left\{(X_{1},X_{2},\cdots,X_{n})\mid \bar{X}>1+\frac{2}{\sqrt{n}}Z_{\alpha}\right\}</equation>D.<equation>\left\{(X_{1},X_{2},\cdots,X_{n})\mid \bar{X}>1+\sqrt{\frac{2}{n}}Z_{\alpha}\right\}</equation>

答案: D

**解析:**解 由已知条件可知，总体方差<equation>\sigma^{2}=2.</equation>根据分析，方差为2的单个正态总体对均值<equation>\mu</equation>的假设检验问题：<equation>H_{0}:\mu\leqslant1,H_{1}:\mu>1</equation>的显著性水平为<equation>\alpha</equation>的检验的拒绝域为<equation>\overline{x}>1+\sqrt{\frac{2}{n}}z_{\alpha}</equation>其中<equation>z_{\alpha}</equation>为标准正态分布的上侧<equation>\alpha</equation>分位数.

因此，应选D.

---

**2021年第10题 | 选择题 | 5分 | 答案: B**

10. 设<equation>X_{1}, X_{2}, \cdots , X_{1 6}</equation>是来自总体<equation>N (\mu , 4)</equation>的简单随机样本，考虑假设检验问题：<equation>H_{0}:\mu \leqslant 1 0, H_{1}:\mu > 1 0, \Phi (x)</equation>表示标准正态分布函数，若该检验问题的拒绝域为<equation>W=\{\bar{X}>1 1 \}</equation>，其中<equation>\bar{X}=\frac{1}{1 6} \sum_{i=1}^{1 6} X_{i}</equation>，则<equation>\mu =1 1. 5</equation>时，该检验犯第二类错误的概率为（    ）

A. 1-<equation>\Phi (0. 5)</equation>B. 1-<equation>\Phi (1)</equation>C. 1-<equation>\Phi (1. 5)</equation>D. 1-<equation>\Phi (2)</equation>

答案: B

**解析:**解 根据已知条件，<equation>\mu=1 1. 5</equation>，原假设<equation>H_{0}:\mu\leqslant1 0</equation>不为真.由于该检验问题的拒绝域为<equation>W=\left\{\overline{X}>11\right\}</equation>，故当<equation>\overline{X}\leqslant1 1</equation>时，不拒绝<equation>H_{0}</equation>.此时，该检验犯了第二类错误，其概率为<equation>P\{\overline{X}\leqslant11\}</equation>下面我们计算<equation>P\{\overline{X}\leqslant11\}</equation>由已知条件可得<equation>n=1 6</equation>，故<equation>\overline{X}\sim N\left(\mu ,\frac{4}{1 6}\right)</equation>，即<equation>\overline{X}\sim N\left(1 1. 5 , \frac{1}{4}\right)</equation>.标准化可得，<equation>\frac{\overline{X}-1 1. 5}{\frac{1}{2}}\sim N(0,1).</equation><equation>P\{\overline{X}\leqslant11\}=P\left\{\frac{\overline{X}-1 1. 5}{\frac{1}{2}}\leqslant\frac{1 1-1 1. 5}{\frac{1}{2}}\right\}=\Phi(-1)=1-\Phi(1).</equation>因此，应选B.

---

**2018年第8题 | 选择题 | 4分 | 答案: D**

8. 设总体 X服从正态分布<equation>N\left(\mu ,\sigma^{2}\right).</equation><equation>X_{1},X_{2},\cdots,X_{n}</equation>是来自总体 X的简单随机样本，据此样本检验假设：<equation>H_{0}:\mu=\mu_{0},H_{1}:\mu\neq\mu_{0}</equation>，则（    )

A. 如果在检验水平<equation>\alpha=0. 0 5</equation>下拒绝<equation>H_{0}</equation>，那么<equation>\alpha=0. 0 1</equation>下必拒绝<equation>H_{0}</equation>B. 如果在检验水平<equation>\alpha=0. 0 5</equation>下拒绝<equation>H_{0}</equation>，那么<equation>\alpha=0. 0 1</equation>下必接受<equation>H_{0}</equation>C. 如果在检验水平<equation>\alpha=0. 0 5</equation>下接受<equation>H_{0}</equation>，那么<equation>\alpha=0. 0 1</equation>下必拒绝<equation>H_{0}</equation>D. 如果在检验水平<equation>\alpha=0. 0 5</equation>下接受<equation>H_{0}</equation>，那么<equation>\alpha=0. 0 1</equation>下必接受<equation>H_{0}</equation>

答案: D

**解析:**解 由于<equation>\sigma^2</equation>未知，故应采用<equation>t</equation>检验法，检验统计量可取为<equation>Z = \frac{\bar{X} - \mu_0}{S / \sqrt{n}}</equation>（注：<equation>S^{2}</equation>为样本方差，为方差<equation>\sigma^2</equation>的无偏估计量）.<equation>\bar{X} = \frac{1}{n}\sum_{i = 1}^{n}X_{i},\bar{X}\sim N\left(\mu ,\frac{\sigma^{2}}{n}\right)</equation>，故当假设<equation>H_{0}</equation>为真时，<equation>Z\sim t(n - 1)</equation>.

当<equation>\alpha = 0.05</equation>时，拒绝域为<equation>\left|\frac{\bar{x} - \mu_0}{S / \sqrt{n}}\right| > t_{\frac{\alpha}{2}} = t_{0.025}</equation>，其中<equation>t_{0.025}</equation>为上0.025分位点.<equation>\alpha = 0.05</equation>对应的接受域为<equation>\left(\mu_0 - t_{0.025}\frac{S}{\sqrt{n}},\mu_0 + t_{0.025}\frac{S}{\sqrt{n}}\right)</equation>.

当<equation>\alpha=0.01</equation>时，拒绝域为<equation>\left| \frac{\overline{{x}}-\mu_{0}}{S / \sqrt{n}} \right| > t_{\frac{\alpha}{2}}=t_{0.005}</equation>，其中<equation>t_{0.005}</equation>为上0.005分位点.<equation>\alpha=0.01</equation>对应的接受域为<equation>\left(\mu_{0}-t_{0.005}\frac{S}{\sqrt{n}},\mu_{0}+t_{0.005}\frac{S}{\sqrt{n}}\right).</equation>因为<equation>t_{0.025}<t_{0.005}</equation>，所以<equation>\alpha=0.05</equation>对应的接受域包含于<equation>\alpha=0.01</equation>对应的接受域.若当检验水平<equation>\alpha=0.05</equation>时，接受<equation>H_{0}</equation>，则当检验水平<equation>\alpha=0.01</equation>时，必接受<equation>H_{0}.</equation>因此，应选D.

---


