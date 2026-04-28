#### 矩阵的运算与变换

**2022年第15题 | 填空题 | 5分**

15. 已知矩阵 A和 E-A可逆，其中 E为单位矩阵，若矩阵 B满足<equation>[ E-( E-A)^{-1} ] B=A</equation>，则 B-A=___

**答案:**<equation>- E.</equation>

**解析:**解（法一）在<equation>[E - (E - A)^{-1}]B = A</equation>两端同时左乘<equation>E - A</equation>，可得<equation>[ \boldsymbol {E} - \boldsymbol {A} - (\boldsymbol {E} - \boldsymbol {A}) (\boldsymbol {E} - \boldsymbol {A}) ^ {- 1} ] \boldsymbol {B} = (\boldsymbol {E} - \boldsymbol {A}) \boldsymbol {A}.</equation>展开整理，可得<equation>- AB=A-A^{2}.</equation>由于<equation>A</equation>可逆，故上式两端同时左乘<equation>A^{-1}</equation>可得<equation>-B = E - A</equation>，即<equation>B - A = -E</equation>（法二）注意到<equation>[E - (E - A)^{-1}](E - A) = E - A - E = -A</equation>，故由A可逆可得，<equation>[E - (E - A)^{-1}](E - A)(-A^{-1}) = E</equation>即<equation>[E - (E - A)^{-1}](E - A^{-1}) = E.</equation>于是，<equation>E - (E - A)^{-1}</equation>与<equation>E - A^{-1}</equation>互为逆矩阵.

在<equation>[E - (E - A)^{-1}]B = A</equation>两端同时左乘<equation>E - A^{-1}</equation>，可得<equation>B = (E - A^{-1})A = A - E.</equation>因此，<equation>B - A = -E.</equation>

---

**2020年第5题 | 选择题 | 4分 | 答案: B**

5. 若矩阵 A经过初等列变换化成 B，则（    ）

A. 存在矩阵 P，使得<equation>P A=B</equation>B. 存在矩阵 P，使得<equation>B P=A</equation>C. 存在矩阵 P，使得<equation>P B=A</equation>D. 方程组<equation>A x=0</equation>与<equation>B x=0</equation>同解

答案: B

**解析:**解 若矩阵 A经过初等列变换化成 B，则存在初等矩阵<equation>Q_{1}, Q_{2}, \dots , Q_{n}</equation>，使得<equation>A Q_{1} Q_{2}\cdots Q_{n}=B.</equation>令<equation>Q=Q_{1} Q_{2}\cdots Q_{n}</equation>，则 Q为可逆矩阵，且<equation>A Q=B.</equation>令 P=<equation>Q^{-1}</equation>，则 BP=A.

因此，应选B.

若矩阵 A经过初等行变换化成 B，则选项 A、C、D正确.

---

**2012年第6题 | 选择题 | 4分 | 答案: B**

6. 设 A为3阶矩阵，P为3阶可逆矩阵，且<equation>P^{-1} A P=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>若<equation>P=(\alpha_{1},\alpha_{2},\alpha_{3})</equation><equation>Q=(\alpha_{1}+\alpha_{2},\alpha_{2},\alpha_{3})</equation>，则<equation>Q ^ {- 1} A Q = (\quad)</equation>A.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>B.<equation>\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>C.<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right)</equation>D.<equation>\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>

答案: B

**解析:**解（法一）由题设知，<equation>Q=P\left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)</equation>，故<equation>Q^{-1}=\left( \begin{array}{c c c} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right) P^{-1}</equation>. 从而<equation>\begin{aligned} Q ^ {- 1} A Q &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 0 & 0 & 1  \right) P ^ {- 1} A P \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1  \right) \\ &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & 1 & 0 \\ 0 & 0 & 1  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2  \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1  \right) &= \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2  \right). \end{aligned}</equation>应选B.

（法二）由题设知，1，1，2是<equation>\boldsymbol{A}</equation>的特征值，<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>分别是属于特征值1，1，2的特征向量，即<equation>A \alpha_ {1} = \alpha_ {1}, \quad A \alpha_ {2} = \alpha_ {2}, \quad A \alpha_ {3} = 2 \alpha_ {3}.</equation>从而<equation>A\left(\alpha_{1} + \alpha_{2}\right) = \alpha_{1} + \alpha_{2},\alpha_{1} + \alpha_{2}</equation>也是<equation>A</equation>的属于特征值1的特征向量.<equation>A Q = A \left(\alpha_ {1} + \alpha_ {2}, \alpha_ {2}, \alpha_ {3}\right) = \left(\alpha_ {1} + \alpha_ {2}, \alpha_ {2}, 2 \alpha_ {3}\right) = Q \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>又由于<equation>Q</equation>由<equation>P</equation>作初等变换得到，<equation>P</equation>可逆，故<equation>Q</equation>可逆.于是<equation>Q^{-1}AQ=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{array} \right).</equation>应选B.

---

**2011年第5题 | 选择题 | 4分 | 答案: D**

5. 设 A为3阶矩阵，将 A的第2列加到第1列得矩阵 B，再交换 B的第2行与第3行得单位矩阵.记<equation>\boldsymbol {P} _ {1} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right), \boldsymbol {P} _ {2} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{array} \right), \mathrm {则} \boldsymbol {A} = (\quad)</equation>A.<equation>P_{1} P_{2}</equation>B.<equation>P_{1}^{-1} P_{2}</equation>C.<equation>P_{2} P_{1}</equation>D.<equation>P_{2} P_{1}^{-1}</equation>

答案: D

**解析:**解 将 A的第2列加到第1列对应 A右乘矩阵<equation>P_{1}</equation>，得<equation>B=A P_{1}</equation>.交换 B的第2行与第3行对应 B左乘矩阵<equation>P_{2}</equation>，得<equation>E=P_{2} A P_{1}</equation>.于是<equation>A=P_{2}^{-1} P_{1}^{-1}.</equation>又因为<equation>P_{2}^{-1}=P_{2}</equation>，所以<equation>A=P_{2} P_{1}^{-1}</equation>.应选 D.

---


