#### 区间估计和置信区间

**2016年第14题 | 填空题 | 4分**

14. 设<equation>X_{1}, X_{2}, \cdots, X_{n}</equation>为来自总体<equation>N\left(\mu ,\sigma^{2}\right)</equation>的简单随机样本，样本均值<equation>\bar{X}=9. 5</equation>，参数<equation>\mu</equation>的置信度为0.95的双侧置信区间的置信上限为10.8，则<equation>\mu</equation>的置信度为0.95的双侧置信区间为 ___.

**答案:**## (8.2,10.8)

**解析:**解 由上述表格知，无论<equation>\sigma^{2}</equation>已知还是未知，参数<equation>\mu</equation>的置信度为1<equation>- \alpha</equation>的置信区间的置信上限和置信下限都关于样本均值对称，即<equation>\frac{\mathrm{置信上限}+\mathrm{置信下限}}{2}=\bar{X}</equation>从而置信下限<equation>= 2\overline{X}</equation>-置信上限<equation>= 2\times 9.5-10.8=8.2</equation>于是<equation>\mu</equation>的置信度为0.95的双侧置信区间为（8.2，10.8）.

---


### 随机事件和概率

**2025年第16题 | 填空题 | 5分**
16. 设 A,B为两个随机事件，且 A与 B相互独立，已知<equation>P ( A )=2 P ( B )</equation><equation>P ( A \cup B )=\frac{5}{8}</equation>，则在事件 A,B至少有一个发生的条件下，A,B中恰有一个发生的概率为___
**解析: **解 根据条件概率公式，A，B中至少有一个发生的条件下，A，B中恰好有一个发生的概率为<equation>\begin{aligned} P \left(A \bar {B} \cup \bar {A} B \mid A \cup B\right) &= \frac {P \left[ \left(A \bar {B} \cup \bar {A} B\right) \cap (A \cup B) \right]}{P (A \cup B)} = \frac {P \left(A \bar {B} \cup \bar {A} B\right)}{P (A \cup B)} \\ &= \frac {P \left(A \bar {B}\right) + P \left(\bar {A} B\right)}{P \left(A \cup B\right)} \xlongequal {\text {独立 性}} \frac {P (A) P (\bar {B}) + P (\bar {A}) P (B)}{P (A \cup B)}. \end{aligned}</equation>下面计算<equation>P ( A ) , P ( B )</equation>由于 A，B相互独立，故<equation>P ( A B )=P ( A ) P ( B )</equation>，结合<equation>P ( A )=2 P ( B )</equation>可得<equation>\frac{5}{8}=P(A\cup B)=P(A)+P(B)-P(AB)=P(A)+P(B)-P(A)P(B)=3P(B)-2[P(B)]^{2}.</equation>整理可得<equation>1 6 \left[ P (B) \right]^{2}-2 4 P (B)+5=0</equation>即<equation>\left[ 4 P (B)-1 \right] \left[ 4 P (B)-5 \right]=0.</equation>解得<equation>P (B)=\frac{1}{4}</equation>舍去<equation>P (B)=\frac{5}{4}).</equation>进一步可得<equation>P (A)=2 P (B)=\frac{1}{2}.</equation>因此<equation>P \left(A \bar {B} \cup \bar {A} B \mid A \cup B\right) = \frac {P (A) P (\bar {B}) + P (\bar {A}) P (B)}{P (A \cup B)} = \frac {\frac {1}{2} \cdot \frac {3}{4} + \frac {1}{2} \cdot \frac {1}{4}}{\frac {5}{8}} = \frac {4}{5}.</equation>

---

**2022年第16题 | 填空题 | 5分**
16. 设 A,B,C为随机事件，且 A与 B互不相容，A与 C互不相容，B与 C相互独立，<equation>P ( A )=P ( B )=P ( C )=\frac{1}{3}</equation>，则<equation>P ( B \cup C \mid A \cup B \cup C )=</equation>___
**解析: **由于<equation>A,B</equation>互不相容，<equation>A,C</equation>互不相容，<equation>B,C</equation>相互独立，故<equation>P (A B) = 0, \quad P (A C) = 0, \quad P (B C) = P (B) P (C) = \frac {1}{9}, \quad P (A B C) = 0.</equation>由条件概率公式，<equation>\begin{aligned} P (B \cup C \mid A \cup B \cup C) &= \frac {P [ (B \cup C) \cap (A \cup B \cup C) ]}{P (A \cup B \cup C)} = \frac {P (B \cup C)}{P (A \cup B \cup C)} \\ &= \frac {P (B) + P (C) - P (B C)}{P (A) + P (B) + P (C) - P (A B) - P (B C) - P (A C) + P (A B C)} \\ &= \frac {\frac {1}{3} + \frac {1}{3} - \frac {1}{9}}{\frac {1}{3} + \frac {1}{3} + \frac {1}{3} - \frac {1}{9}} = \frac {5}{8}. \end{aligned}</equation>

---

**2021年第8题 | 选择题 | 5分 | 答案: D**
8. 设 A,B为随机事件，且<equation>0 < P ( B ) < 1</equation>，下列命题中为假命题的是（    )

A. 若<equation>P ( A \mid B )=P ( A )</equation>，则<equation>P ( A \mid \bar{B})=P ( A )</equation>B. 若<equation>P ( A \mid B )>P ( A )</equation>，则<equation>P ( \bar{A} \mid \bar{B})>P ( \bar{A} )</equation>C. 若<equation>P ( A \mid B )>P ( A \mid \bar{B})</equation>，则<equation>P ( A \mid B )>P ( A )</equation>D. 若<equation>P ( A \mid A \cup B )>P ( \bar{A} \mid A \cup B)</equation>，则<equation>P ( A )>P ( B )</equation>
答案: D
**解析: **解 考虑选项 D.<equation>P (A \mid A \cup B) = \frac {P (A \cap (A \cup B))}{P (A \cup B)} = \frac {P (A)}{P (A) + P (B) - P (A B)},</equation><equation>P (\bar {A} \mid A \cup B) = \frac {P (\bar {A} \cap (A \cup B))}{P (A \cup B)} = \frac {P (\bar {A} B)}{P (A) + P (B) - P (A B)} = \frac {P (B) - P (A B)}{P (A) + P (B) - P (A B)}.</equation>若<equation>P(A \mid A \cup B) > P(\overline{A} \mid A \cup B)</equation>，则<equation>P(A) > P(B) - P(AB)</equation>. 但这并不能保证<equation>P(A) > P(B)</equation>.由此出发考虑选项D的反例.例如：<equation>A = B</equation>，则<equation>P(A \mid A \cup B) = 1 > 0 = P(\overline{A} \mid A \cup B)</equation>，但<equation>P(A) = P(B)</equation>.

因此，应选D.

下面说明选项A、B、C不正确.

选项A：由于<equation>P ( A )=P ( A \mid B )=\frac{P ( A B )}{P ( B )}</equation>，故<equation>P ( A B )=P ( A ) P ( B )</equation>，从而A，B独立.由A，B独立可得A，<equation>\overline{B}</equation>独立，故<equation>P ( A \mid \overline{B})=P ( A ).</equation>选项A成立.

选项B：若<equation>P ( A \mid B ) > P ( A )</equation>，即<equation>\frac{P ( A B )}{P ( B )} > P ( A )</equation>，则<equation>P ( A B ) > P ( A ) P ( B ).</equation><equation>\begin{aligned} P (\bar {A} \mid \bar {B}) &= \frac {P (\bar {A} \bar {B})}{P (\bar {B})} = \frac {1 - P (A \cup B)}{1 - P (B)} = \frac {1 - P (A) - P (B) + P (A B)}{1 - P (B)} \\ > \frac {1 - P (A) - P (B) + P (A) P (B)}{1 - P (B)} &= 1 - P (A) = P (\bar {A}). \end{aligned}</equation>选项B成立.

选项C：若<equation>P ( A \mid B ) > P ( A \mid \bar{B} )</equation>，即<equation>\frac{P ( A B )}{P ( B )} >\frac{P ( A B )}{P (\bar{B})}</equation>，则<equation>\frac{P ( A B )}{P ( B )} >\frac{P ( A ) - P ( A B )}{1 - P ( B )}.</equation>由此可得<equation>P ( A B ) - P ( B ) P ( A B ) > P ( A ) P ( B ) - P ( B ) P ( A B )</equation>即<equation>P ( A B ) > P ( A ) P ( B ).</equation>于是，<equation>P ( A ) < \frac { P ( A B ) } { P ( B ) } = P ( A \mid B ) .</equation>选项C成立.

---

**2020年第7题 | 选择题 | 4分 | 答案: D**
7. 设 A,B,C为三个随机事件，且<equation>P ( A )=P ( B )=P ( C )=\frac{1}{4}, P ( A B )=0, P ( A C )=P ( B C )=\frac{1}{1 2}</equation>，则 A,B,C中恰有一个事件发生的概率为（    ）

A.<equation>\frac{3}{4}</equation>B.<equation>\frac{2}{3}</equation>C.<equation>\frac{1}{2}</equation>D.<equation>\frac{5}{1 2}</equation>
答案: D
**解析: **<equation>\begin{aligned} P (A \cup B \cup C) &= P (A) + P (B) + P (C) - P (A B) - P (B C) - P (A C) + P (A B C) \\ &= \frac {1}{4} + \frac {1}{4} + \frac {1}{4} - 0 - \frac {1}{1 2} - \frac {1}{1 2} + 0 = \frac {7}{1 2}. \end{aligned}</equation><equation>\begin{aligned} P (A B \cup B C \cup A C) &= P (A B) + P (B C) + P (A C) - P (A B C) - P (A B C) + P (A B C) \\ &= 0 + \frac {1}{1 2} + \frac {1}{1 2} + 0 = \frac {1}{6}. \end{aligned}</equation>从而，<equation>p=\frac{7}{12}-\frac{1}{6}=\frac{5}{12}.</equation>因此，应选D.

（法二）A,B,C中恰有一个事件发生的概率为<equation>p=P(A\overline{B}\overline{C})+P(\overline{A}B\overline{C})+P(\overline{A}\overline{B}C).</equation><equation>P \left(A \bar {B} \bar {C}\right) = P \left(A \bar {B}\right) - P \left(A \bar {B} C\right) = P (A) - P (A B) - \left[ P (A C) - P (A C B) \right],</equation><equation>P (\bar {A} B \bar {C}) = P (\bar {A} B) - P (\bar {A} B C) = P (B) - P (A B) - [ P (B C) - P (B C A) ],</equation><equation>P (\bar {A} \bar {B} C) = P (\bar {B} C) - P (\bar {B} C A) = P (C) - P (C B) - [ P (C A) - P (C A B) ].</equation>由<equation>P ( A B ) = 0</equation>可得<equation>P ( A B C ) = 0.</equation>因此，<equation>p = P (A) + P (B) + P (C) - 2 \left[ P (A B) + P (B C) + P (A C) \right] = \frac {3}{4} - 4 \times \frac {1}{1 2} = \frac {5}{1 2}.</equation>应选 D.

解（法一）设 A,B,C中恰有一个事件发生的概率为 p. P（A U B U C）为至少发生一个事件的概率.“至少发生一个”可拆分为“恰好发生一个”，“至少发生两个”这样两个互不相容事件.于是，<equation>P (A \cup B \cup C) = p + P (A B \cup B C \cup A C).</equation>由<equation>P ( A B ) = 0</equation>可得<equation>P ( A B C ) = 0.</equation>由三个事件的加法公式可得

---

**2019年第7题 | 选择题 | 4分 | 答案: C**
7. 设 A,B为随机事件，则<equation>P ( A )=P ( B )</equation>的充分必要条件是（    ）

A.<equation>P ( A \cup B )=P ( A )+P ( B )</equation>B.<equation>P ( A B )=P ( A ) P ( B )</equation>C.<equation>P ( A \bar{B} )=P ( B \bar{A} )</equation>D.<equation>P ( A B )=P ( \bar{A} \bar{B} )</equation>
答案: C
**解析: **解 由于<equation>A\overline{B}=A-A\cap B, B\overline{A}=B-B\cap A</equation>，故<equation>P(A\overline{B})=P(A)-P(AB), P(B\overline{A})= P(B)-P(AB).</equation>因此，<equation>P ( A ) = P ( B )</equation>等价于<equation>P ( A \bar{B} ) = P ( B \bar{A} )</equation>应选C.

下面说明选项A、B、D不正确.

取<equation>A = B</equation>，且<equation>P(A) = P(B) = \frac{1}{3}</equation>.

选项 A：<equation>P ( A \cup B )=P ( A )=\frac{1}{3}, P ( A )+P ( B )=\frac{2}{3}.</equation>选项A不是<equation>P ( A )=P ( B )</equation>的必要条件.

选项B：<equation>P ( A B )=P ( A )=\frac{1}{3}, P ( A ) P ( B )=\frac{1}{9}.</equation>选项B不是<equation>P ( A )=P ( B )</equation>的必要条件.

选项D：<equation>P ( A B )=P ( A )=\frac{1}{3}, P ( \overline{{A}} \ \overline{{B}} )=P ( \overline{{A}} )=\frac{2}{3}.</equation>选项D不是<equation>P ( A )=P ( B )</equation>的必要条件.

---

**2018年第14题 | 填空题 | 4分**
14. 设随机事件 A与B相互独立，A与C相互独立，<equation>B C=\varnothing</equation>. 若<equation>P(A)=P(B)=\frac{1}{2}, P(AC\mid AB\cup C)=\frac{1}{4}</equation>，则 P(C)=
**解析: **解 由于事件 A与B相互独立，故<equation>P ( A B )=P ( A ) P ( B ).</equation>由于事件 A与C相互独立，故<equation>P ( A C )=P ( A ) P ( C ).</equation>根据事件运算的分配律，<equation>P ( A C \cap( A B \cup C) )=P((A C \cap A B)\cup( A C \cap C))\overset{B C=\varnothing}{=}P( A C ).</equation>根据条件概率的公式，<equation>\begin{aligned} P (A C \mid A B \cup C) &= \frac {P (A C \cap (A B \cup C))}{P (A B \cup C)} = \frac {P (A C)}{P (A B \cup C)} = \frac {P (A) P (C)}{P (A B) + P (C) - P (A B C)} \\ &= \frac {P (A) P (C)}{P (A) P (B) + P (C) - 0} = \frac {1}{4}. \end{aligned}</equation>代入<equation>P ( A )=P ( B )=\frac{1}{2}</equation>，可得<equation>\frac{\frac{1}{2} P ( C )}{\frac{1}{4}+P ( C )}=\frac{1}{4}.</equation>解得<equation>P ( C )=\frac{1}{4}.</equation>

---

**2017年第7题 | 选择题 | 4分 | 答案: A**
7. 设 A,B为随机事件.若<equation>0 < P ( A ) < 1, 0 < P ( B ) < 1</equation>，则<equation>P ( A \mid B ) > P ( A \mid \bar{B} )</equation>的充分必要条件是（    )

A.<equation>P ( B \mid A ) > P ( B \mid \bar{A} )</equation>B.<equation>P ( B \mid A ) < P ( B \mid \bar{A} )</equation>C.<equation>P ( \bar{B} \mid A ) > P ( B \mid \bar{A} )</equation>D.<equation>P ( \bar{B} \mid A ) < P ( B \mid \bar{A} )</equation>
答案: A
**解析: **解 （法一）由题设知，<equation>P (A \mid B) > P (A \mid \bar {B}) \Leftrightarrow \frac {P (A B)}{P (B)} > \frac {P (A \bar {B})}{P (\bar {B})} \Leftrightarrow \frac {P (A B)}{P (A B) + P (\bar {A} B)} > \frac {P (A \bar {B})}{P (A \bar {B}) + P (\bar {A} \bar {B})}.</equation>记<equation>P ( A B ) = a,P(\overline{A} B)=b,P(A\overline{B})=c,P(\overline{A}\overline{B})=d</equation>，则<equation>\frac{P(A B)}{P(A B)+P(\overline{A} B)} >\frac{P(A\overline{B})}{P(A\overline{B})+P(\overline{A}\overline{B})},</equation>即<equation>\frac{a}{a+b} >\frac{c}{c+d},</equation>由于 0 < P(A) < 1,0 < P(B) < 1，故 a+b=P(B),c+d=P<equation>\overline{{B}}</equation>, a+c=P(A),b+d=P<equation>\overline{{A}}</equation>均大于0.于是，<equation>\frac {a}{a + b} > \frac {c}{c + d} \Leftrightarrow a (c + d) > c (a + b) \Leftrightarrow a d > b c.</equation>ad > bc等价于<equation>a b + a d > a b + b c, \quad \text {即} \frac {a}{a + c} > \frac {b}{b + d}, \quad \text {也 即} P (B \mid A) > P (B \mid \bar {A}).</equation>因此，应选A.

（法二）由题设知，<equation>\begin{array}{l} P (A \mid B) > P (A \mid \bar {B}) \Leftrightarrow \frac {P (A B)}{P (B)} > \frac {P (A \bar {B})}{P (\bar {B})} = \frac {P (A) - P (A B)}{1 - P (B)} \\ \Leftrightarrow P (A B) [ 1 - P (B) ] > [ P (A) - P (A B) ] P (B) \\ \end{array}</equation><equation>\Leftrightarrow P (A B) > P (A) P (B).</equation>调换 A,B的位置，同上可得<equation>P (B \mid A) > P (B \mid \bar {A}) \Leftrightarrow P (B A) > P (B) P (A).</equation>又<equation>P ( A B ) = P ( B A )</equation>，故<equation>P (A \mid B) > P (A \mid \bar {B}) \Leftrightarrow P (B \mid A) > P (B \mid \bar {A}).</equation>因此，应选A.

---

**2015年第7题 | 选择题 | 4分 | 答案: C**
7. 若 A,B为任意两个随机事件，则（    ）

A.<equation>P ( A B ) \leqslant P ( A ) P ( B )</equation>B.<equation>P ( A B ) \geqslant P ( A ) P ( B )</equation>C.<equation>P ( A B ) \leqslant \frac { P ( A ) + P ( B ) } { 2 }</equation>D.<equation>P ( A B ) \geqslant \frac { P ( A ) + P ( B ) } { 2 }</equation>
答案: C
**解析: **解 由于 A<equation>\cap B \subseteq A</equation>，A<equation>\cap B \subseteq B</equation>，故<equation>P (A B) \leqslant P (A), \quad P (A B) \leqslant P (B).</equation>因此，<equation>2 P ( A B ) \leqslant P ( A )+P ( B )</equation>，即<equation>P ( A B ) \leqslant \frac { P ( A ) + P ( B ) } { 2 }</equation>应选C.

下面我们说明选项A、B、D不正确.

若 B<equation>\subseteq</equation>A,0 < P(A) < 1,0 < P(B) < 1<equation>，则 P(AB)=P(A</equation>\cap<equation>B）=P(B）>P(A)P(B).选项A不正确.

若 P(A) > 0，P(B) > 0且 A</equation>\cap<equation>B=</equation>\varnothing<equation>，则 P(AB) = P(A</equation>\cap<equation>B) = 0 < P(A)P(B)，P(AB) <</equation>\frac{P(A)+P(B)}{2} $ .选项B和选项D不正确.

---

**2014年第7题 | 选择题 | 4分 | 答案: B**
7. 设随机事件 A与 B相互独立，且<equation>P ( B )=0. 5, P ( A-B)=0. 3</equation>，则<equation>P ( B-A )=</equation>(    )

A. 0.1 B. 0.2 C. 0.3 D. 0.4
答案: B
**解析: **解（法一）由 A与B相互独立知，<equation>P ( A B ) = P ( A ) P ( B ).</equation>，于是，<equation>P (A - B) = P (A) - P (A B) = P (A) - P (A) P (B) = P (A) [ 1 - P (B) ] = 0. 5 P (A).</equation>从而<equation>P ( A ) = 2 P ( A - B ) = 0. 6.</equation>进一步可得，<equation>P (B - A) = P (B) - P (A B) = P (B) - P (A) P (B) = 0. 5 - 0. 6 \times 0. 5 = 0. 2.</equation>应选B.

（法二）由<equation>A</equation>与<equation>B</equation>相互独立知，<equation>A, B</equation>也相互独立.于是，<equation>0. 3 = P (A - B) = P (A \cap \bar {B}) = P (A \bar {B}) = P (A) P (\bar {B}) = 0. 5 P (A).</equation>因此，<equation>P ( A ) = 0. 6</equation>进一步可得，<equation>P (B - A) = P \left(B \bar {A}\right) = P (B) P (\bar {A}) = 0. 5 \times (1 - 0. 6) = 0. 2.</equation>应选B.

---

**2012年第14题 | 填空题 | 4分**
14. 设 A,B,C是随机事件，A与C互不相容，<equation>P ( A B )=\frac{1} {2}, P ( C )=\frac{1} {3}</equation>，则<equation>P ( A B \mid \bar{C})=</equation>___
**解析: **解 由条件概率的定义可知，<equation>P ( A B \mid \bar{C})=\frac{P ( A B \bar{C})}{P (\bar{C})}=\frac{P ( A B \bar{C})}{1-P(C)}.</equation>又 A与C互不相容，即<equation>A \cap C=\varnothing</equation>，故<equation>A \cap B \subset A \subset \bar{C}</equation>，从而<equation>A \cap B \cap \bar{C}=A \cap B.</equation>因此<equation>P ( A B \mid \bar{C})=\frac{P ( A B)}{1-P(C)}=\frac{\frac{1}{2}}{\frac{2}{3}}=\frac{3}{4}.</equation>

---


### 多维随机变量及其分布


