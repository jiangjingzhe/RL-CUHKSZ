# 第 2 周附录：UCB1 完整证明与 Softmax 求导

[返回第 2 周](week02.md) · [学习入口](README.md) · [术语表](glossary.md)

> 来源：`Week 2.pdf` 的 P48–52。原文件在这 5 页的页脚重新标为 1/5–5/5。
>
> 课件 P30 明确注明：附录 A.1–A.4 的 **UCB1 完整证明为选读，不考期末**。Softmax 附录 B 没有被同一条说明明确列为免考。下文保留全部证明步骤，附加的直觉与检查标为补充解释。

<a id="ucb-proof"></a>
## A. UCB1 的有限时间遗憾上界

### A.0 先看证明要完成什么

目标是对每个次优动作 $a$ 证明：

$$\mathbb E[N_a(T)]\le\frac{8\log T}{\Delta_a^2}+1+\frac{\pi^2}{3}.$$

再利用遗憾分解 $\mathcal R_T=\sum_a\Delta_a\mathbb E[N_a(T)]$，得到总遗憾上界。

**补充导读：** 证明的顺序是先控制“样本均值估错”的概率，再处理采样次数会随机变化的问题，然后找出次优动作需要的样本阈值，最后统计超过阈值后还能被误选多少次。

### A.1 固定样本数下的 Hoeffding 界

来源：P48，原附录 A.1。

**模型。** $k\ge2$ 个臂各有独立同分布的奖励流，奖励在 $[0,1]$ 中，不同臂的奖励流独立。真实均值为 $q_*(a)$。开始时每只臂选择一次。

记 $\bar R_{a,n}$ 为臂 $a$ 的前 $n$ 次奖励均值，$N_t(a)$ 为第 $t$ 轮前的选择次数。$t>k$ 时：

$$
Q_t(a)=\bar R_{a,N_t(a)},\qquad r_t(n)=\sqrt{\frac{2\log t}{n}},
$$

$$
U_t(a)=Q_t(a)+r_t(N_t(a)),\qquad A_t\in\arg\max_b U_t(b).
$$

注意 $r_t(n)$ 是置信半径，不是单次奖励 $R_t$。

对于固定 $n\ge1$ 和 $u>0$，Hoeffding 不等式给出：

$$\Pr\{\bar R_{a,n}-q_*(a)\ge u\}\le e^{-2nu^2}.$$

下尾同样满足：

$$\Pr\{q_*(a)-\bar R_{a,n}\ge u\}\le e^{-2nu^2}.$$

固定 $t$，令 $u=r_t(n)$，每个尾部概率至多为：

$$e^{-2nr_t(n)^2}=e^{-2n(2\log t/n)}=e^{-4\log t}=t^{-4}.$$

> **补充解释。** 样本均值偏离真实均值越远，概率越小；样本数越多，同样偏离的概率也越小。选择 $\sqrt{2\log t/n}$ 这个半径后，尾部界恰好化成易于求和的 $t^{-4}$。

### A.2 随机、自适应的样本数怎么处理

来源：P49，原附录 A.2。

固定一个最优动作 $a^*$ 和一个次优动作 $a$。记 $q_*=q_*(a^*)$，$\Delta_a=q_*-q_*(a)>0$。

对固定时刻 $t>k$，定义置信失败事件：

$$
\begin{aligned}
F_t={}&\{Q_t(a^*)<q_*-r_t(N_t(a^*))\}\\
&\cup\{Q_t(a)>q_*(a)+r_t(N_t(a))\}.
\end{aligned}
$$

第一个事件表示最优臂被低估得太多；第二个表示这只次优臂被高估得太多。

虽然 $N_t(a)$ 随机且依赖过去奖励，但它只能取 $1,\ldots,t-1$。对所有固定样本数取联合界：

$$
\begin{aligned}
\Pr(F_t)
&\le\sum_{n=1}^{t-1}\left[
\Pr\{\bar R_{a^*,n}<q_*-r_t(n)\}
+\Pr\{\bar R_{a,n}>q_*(a)+r_t(n)\}
\right]\\
&\le2(t-1)t^{-4}\\
&\le2t^{-3}.
\end{aligned}
$$

因此，以至少 $1-2t^{-3}$ 的概率，两个所需置信界同时成立。

> **补充解释：为什么不直接把随机 $N_t(a)$ 填进固定 $n$ 的结论？**
> 采样次数取决于过去看到的奖励，不能简单假装它和数据无关。这里用“把所有可能的固定次数都覆盖住”的办法处理自适应性，不对随机次数作未经证明的条件化。

> **联合界（Union bound）补充。** 任意事件 $E_1,\ldots,E_m$ 都满足 $\Pr(\bigcup_i E_i)\le\sum_i\Pr(E_i)$，不要求这些事件相互独立。这里分别覆盖最优臂低估和次优臂高估的所有可能样本数。

### A.3 样本多到什么程度，次优动作就不会赢

来源：P50，原附录 A.3。

固定总轮数 $T\ge k$。在 $k<t\le T$ 且置信界未失效的事件 $F_t^c$ 上：

$$U_t(a^*)=Q_t(a^*)+r_t(N_t(a^*))\ge q_*,$$

$$U_t(a)=Q_t(a)+r_t(N_t(a))\le q_*(a)+2r_t(N_t(a)).$$

**补充解释：为什么出现 2？** 次优臂的估计 $Q_t(a)$ 本来就可能比真实均值高一个半径，UCB 指数又加一个半径，总共最多高两个半径。

选择严格大于 $8\log T/\Delta_a^2$ 的整数阈值：

$$L_a=\left\lfloor\frac{8\log T}{\Delta_a^2}\right\rfloor+1>\frac{8\log T}{\Delta_a^2}.$$

当 $N_t(a)\ge L_a$ 时：

$$2r_t(N_t(a))\le2\sqrt{\frac{2\log T}{L_a}}<\Delta_a.$$

所以：

$$U_t(a)<q_*(a)+\Delta_a=q_*\le U_t(a^*).$$

次优臂 $a$ 的指数严格低于最优臂，无法成为最大者。等价地，超过阈值之后还选到它，一定发生了置信界失败：

$$\{A_t=a,\ N_t(a)\ge L_a\}\subseteq F_t.$$

> **补充解释：严格不等号有用。** 阈值用取整再加 1，保证两个指数不会只是相等，因此结论不依赖并列时怎样选。

### A.4 统计次数并得到遗憾

来源：P51，原附录 A.4。

记 $N_a(T)=N_{T+1}(a)$ 为到第 $T$ 轮结束时的总选择次数。在历史次数低于阈值时，最多再累计到 $L_a$ 次，这已经包括初始化。之后每次额外选择都需要 $F_t$ 发生，因此：

$$N_a(T)\le L_a+\sum_{t=k+1}^T\mathbf1\{F_t\}.$$

取期望并使用 $L_a\le8\log T/\Delta_a^2+1$：

$$
\begin{aligned}
\mathbb E[N_a(T)]
&\le L_a+\sum_{t=k+1}^T\Pr(F_t)\\
&\le L_a+2\sum_{t=1}^{\infty}t^{-2}\\
&\le\frac{8\log T}{\Delta_a^2}+1+\frac{\pi^2}{3}.
\end{aligned}
$$

中间用了 $2t^{-3}\le2t^{-2}$，以及 $\sum_{t=1}^{\infty}t^{-2}=\pi^2/6$。这是方便的放宽上界，不是声称 $t^{-3}=t^{-2}$。

最后由遗憾分解：

$$
\begin{aligned}
\mathcal R_T
&=Tq_*-\mathbb E\left[\sum_{t=1}^TR_t\right]\\
&=\sum_a\Delta_a\mathbb E[N_a(T)]\\
&\le\sum_{a:\Delta_a>0}
\left[\frac{8\log T}{\Delta_a}+\left(1+\frac{\pi^2}{3}\right)\Delta_a\right].
\end{aligned}
$$

### A.5 证明读懂了吗

以下是补充检查点：

- [ ] 能从 Hoeffding 指数推出 $t^{-4}$。
- [ ] 能解释为什么还要枚举可能的样本数，得到 $2t^{-3}$。
- [ ] 能推出阈值里的常数 8：由 $2\sqrt{2\log T/n}<\Delta_a$ 解出 $n>8\log T/\Delta_a^2$。
- [ ] 能解释采样阈值以内的次数和置信失败造成的额外次数如何相加。
- [ ] 能从次数界中的 $1/\Delta_a^2$ 得到遗憾界中的 $1/\Delta_a$。

<a id="softmax-proof"></a>
## B. Softmax 对数策略的梯度

来源：P52，原附录 B。此推导是正文梯度 Bandit 更新的基础。

固定本次抽到的动作 $A$，对任意一个偏好 $H(a)$ 求偏导：

$$\pi_H(A)=\frac{e^{H(A)}}{\sum_b e^{H(b)}},$$

$$\log\pi_H(A)=H(A)-\log\sum_b e^{H(b)}.$$

第一项：

$$\frac{\partial H(A)}{\partial H(a)}=\mathbf1\{A=a\}.$$

第二项使用链式法则：

$$
\begin{aligned}
\frac{\partial}{\partial H(a)}\log\sum_b e^{H(b)}
&=\frac{1}{\sum_b e^{H(b)}}\frac{\partial}{\partial H(a)}\sum_b e^{H(b)}\\
&=\frac{e^{H(a)}}{\sum_b e^{H(b)}}\\
&=\pi_H(a).
\end{aligned}
$$

因为求和中只有 $b=a$ 的那一项依赖 $H(a)$。两项相减得到：

$$\boxed{\frac{\partial\log\pi_H(A)}{\partial H(a)}=\mathbf1\{A=a\}-\pi_H(a).}$$

**补充检查：** 将所有坐标导数相加，得到 $1-\sum_a\pi_H(a)=0$。这与“所有偏好加同一个常数不会改变策略”相一致，也解释了偏好更新各分量的增量之和为 0。

**容易犯的错：** $A$ 是本次已经采到的动作，在这一步求导中把它固定。不要对动作编号求导；求导对象是可连续调整的偏好向量 $H$。
