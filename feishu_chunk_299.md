#### 三、置信区间

<equation>\textcircled{1}</equation>定义：若<equation>E(\partial) = \theta</equation>，称<equation>\hat{\theta}</equation>是<equation>\theta</equation>的无偏估计量.

<equation>\textcircled{2}</equation>结论：因为<equation>E(\overline{X}) = \mu , E(S^2) = \delta^2</equation>，所以<equation>\overline{X}</equation>是样本均值<equation>\mu</equation>的无偏估计量，样本方差<equation>S^{2}</equation>是总体方差<equation>\sigma^{2}</equation>的无偏估计量.


设<equation>\hat{\theta}_1 = \hat{\theta}_1\left(X_1, X_2, \dots, X_n\right)</equation>与<equation>\hat{\theta}_2 = \hat{\theta}_2\left(X_1, X_2, \dots, X_n\right)</equation>都是<equation>\theta</equation>的无偏估计量，若对任意<equation>\theta \in \Theta</equation>，有<equation>D(\hat{\theta}_1) \leqslant D(\hat{\theta}_2)</equation>，且至少对于某一个<equation>\theta \in \Theta</equation>，上式中不等号成立，则称<equation>\hat{\theta}_1</equation>较<equation>\hat{\theta}_2</equation>有效.


若对于任意<equation>\theta \in \Theta</equation>都满足：对任意<equation>\epsilon > 0</equation>，有

<equation>\lim _ {n \rightarrow \infty} P \left\{\left| \hat {\theta} - \theta \right| < \varepsilon \right\} = 1,</equation>

则称<equation>\hat{\theta}</equation>是<equation>\theta</equation>的一致估计量.


设总体<equation>X</equation>的分布律中含有未知参数<equation>\theta</equation>，来自该总体的几个样本为<equation>X_{1}, X_{2}, \dots, X_{n}, 0 < \alpha < 1.</equation>若存在统计量<equation>\hat{\theta}_{1}</equation>和<equation>\hat{\theta}_{2}</equation>，使得<equation>P(\hat{\theta}_{1} \leqslant \theta \leqslant \hat{\theta}_{2}) = 1 - \alpha</equation>，则称<equation>1 - \alpha</equation>为置信度，<equation>(\hat{\theta}_{1}, \hat{\theta}_{2})</equation>为<equation>\theta</equation>的置信区间.

---

四、常用单个正态总体参数的置信区间表

<table border="1"><tr><td>参数</td><td colspan="2"><equation>\mu</equation></td><td><equation>\delta^{2}</equation></td></tr><tr><td>条件</td><td>已知<equation>\delta^{2}</equation></td><td>未知<equation>\delta^{2}</equation></td><td><equation>\mu</equation>未知</td></tr><tr><td>置信区间</td><td><equation>\left[\bar{X}-\frac{\delta}{\sqrt{n}}z_{\frac{\alpha}{2}}, \bar{X}+\frac{\delta}{\sqrt{n}}z_{\frac{\alpha}{2}}\right]</equation></td><td><equation>\left[\bar{X}-\frac{S}{\sqrt{n}}t_{\frac{\alpha}{2}}(n-1), \bar{X}+\frac{S}{\sqrt{n}}t_{\frac{\alpha}{2}}(n-1)\right]</equation></td><td><equation>\left[\frac{(n-1)S^{2}}{\chi_{\frac{\alpha}{2}}^{2}(n-1)},\frac{(n-1)S^{2}}{\chi_{1-\frac{\alpha}{2}}^{2}(n-1)}\right]</equation></td></tr></table>

---


