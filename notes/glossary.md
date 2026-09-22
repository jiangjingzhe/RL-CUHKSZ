# 术语与符号速查

[学习入口](README.md) · [第 1 周](week01.md) · [第 2 周](week02.md) · [第 3 周](week03.md)

## 1. 基础术语

| 中文 | 英文 | 本课程含义 | 首次详细解释 |
| --- | --- | --- | --- |
| 强化学习 | Reinforcement learning，RL | 从经验改进决策，最大化期望累积奖励 | [W1 §1](week01.md#w1-1) |
| 智能体 | Agent | 决策的主体，可以只是较大系统的一个组件 | [W1 §1](week01.md#w1-1) |
| 环境 | Environment | 与智能体交互并产生后果与奖励的部分 | [W1 §3](week01.md#w1-3) |
| 状态 | State | 用于预测动作后果的情境表示 | [W1 §3](week01.md#w1-3) |
| 观测 | Observation | 实际可见的信息，未必足以表示完整状态 | [W1 §3](week01.md#w1-3) |
| 动作 | Action | 智能体选择的行为 | [W1 §3](week01.md#w1-3) |
| 轨迹 | Trajectory | 状态、动作、奖励组成的交互序列 | [W1 §3](week01.md#w1-3) |
| 回合 | Episode | 有自然终点的一段交互 | [W1 §3](week01.md#w1-3) |
| 奖励 | Reward | 一次交互得到的数值反馈 | [W1 §4](week01.md#w1-4) |
| 回报 | Return | 后续奖励的总和或折扣总和 | [W1 §4](week01.md#w1-4) |
| 折扣因子 | Discount factor | 未来奖励的时间权重参数 | [W1 §4](week01.md#w1-4) |
| 策略 | Policy | 从状态到动作或动作概率的规则 | [W1 §4](week01.md#w1-4) |
| 状态价值 | State value | 从状态出发遵循策略的期望回报 | [W1 §4](week01.md#w1-4) |
| 动作价值 | Action value | 先选定动作，再遵循策略的期望回报 | [W1 §4](week01.md#w1-4) |
| 模型 | Model | 此处指预测下一状态、奖励等后果的环境模型 | [W1 §4](week01.md#w1-4) |
| 规划 | Planning | 利用模型推演未来、计算价值或策略 | [W1 §4](week01.md#w1-4) |
| 无模型方法 | Model-free | 不利用显式环境转移模型规划，直接学价值或策略 | [W1 §4](week01.md#w1-4) |
| 基于模型的方法 | Model-based | 使用已知或学到的环境模型 | [W1 §4](week01.md#w1-4) |
| 信用分配 | Credit assignment | 判断先前哪些动作促成最终结果 | [W1 §4](week01.md#w1-4) |
| 价值备份 | Value backup | 用后面的价值信息修正前面的价值估计 | [W1 §5](week01.md#w1-5) |
| 时序差分 | Temporal difference，TD | 基于先后预测之间的差异学习 | [W1 §5](week01.md#w1-5) |
| 自我对弈 | Self-play | 学习者与自己或同时学习的对手对弈 | [W1 §5](week01.md#w1-5) |
| 函数近似 | Function approximation | 用共享参数函数代替独立表项 | [W1 §6](week01.md#w1-6) |
| 在线 / 离线 RL | Online / Offline RL | 训练时收集新交互 / 从固定经验数据学习 | [W1 §1](week01.md#w1-1) |

## 2. Bandit 与优化

| 中文 | 英文 | 含义 | 详细解释 |
| --- | --- | --- | --- |
| 多臂老虎机 | Multi-armed bandit | 多个未知奖励动作，只有所选动作的反馈 | [W2 §1](week02.md#w2-1) |
| 臂 | Arm | 一个可选择的动作 | [W2 §1](week02.md#w2-1) |
| 平稳 | Stationary | 奖励分布不随时间变 | [W2 §1](week02.md#w2-1) |
| 非平稳 | Nonstationary | 奖励分布或均值可能变化 | [W2 §3](week02.md#w2-3) |
| 探索 / 利用 | Exploration / Exploitation | 收集未来有用的信息 / 依据当前估计获取奖励 | [W2 §2](week02.md#w2-2) |
| 贪心 | Greedy | 选当前估计最大者 | [W2 §2](week02.md#w2-2) |
| 样本均值 | Sample average | 所观察奖励的算术平均 | [W2 §3](week02.md#w2-3) |
| 步长 | Step size | 一次误差修正的幅度 | [W2 §3](week02.md#w2-3) |
| 乐观初值 | Optimistic initial values | 通过高初始估计激发早期探索 | [W2 §4](week02.md#w2-4) |
| 上置信界 | Upper confidence bound，UCB | 估计值加不确定性附加项 | [W2 §5](week02.md#w2-5) |
| 遗憾 / 后悔值 | Regret | 相对始终选最佳臂损失的期望奖励 | [W2 §6](week02.md#w2-6) |
| 次优差距 | Suboptimality gap | 最优均值减去该动作均值 | [W2 §6](week02.md#w2-6) |
| 偏好 | Preference | 决定选择概率的可学习实数 | [W2 §7](week02.md#w2-7) |
| 基线 | Baseline | 用来比较当前奖励高低的参考水平 | [W2 §7](week02.md#w2-7) |
| 随机梯度上升 | Stochastic gradient ascent | 用采样产生的梯度估计提高目标 | [W2 §7](week02.md#w2-7) |
| 上下文 | Context | 本轮动作前可观察、会影响奖励的信息 | [W2 §8](week02.md#w2-8) |
| 关联搜索 | Associative search | 教材对上下文 Bandit 的称呼 | [W2 §8](week02.md#w2-8) |

## 3. LLM 预览缩写

| 缩写 | 全称 | 本周理解范围 |
| --- | --- | --- |
| LLM | Large language model | 大语言模型 |
| SFT | Supervised fine-tuning | 监督微调，模仿示范 |
| RLHF | Reinforcement learning from human feedback | 从人类反馈学习，课件用比较训练奖励模型 |
| RLVR | Reinforcement learning with verifiable rewards | 使用可验证奖励 |
| PPO | Proximal policy optimization | 用优势估计和裁剪目标优化策略 |
| GRPO | Group relative policy optimization | 同一提示下用组内相对奖励，不需要独立价值模型 |
| DPO | Direct preference optimization | 从固定偏好对直接优化，无需在线 rollout |
| KL | Kullback–Leibler divergence | 图中用于约束策略偏离参考模型的程度 |
| GAE | Generalized advantage estimation | PPO 图中的优势估计组件，本周未推导 |
| MDP | Markov decision process | 马尔可夫决策过程，见 [W3 §1](week03.md#w3-1) |

## 4. 数学记号

| 记号 | 含义 | 注意 |
| --- | --- | --- |
| $S_t,A_t,R_t$ | 随机状态、动作、奖励 | 小写通常表示具体取值 |
| $s,a,r$ | 一次实现的状态、动作、奖励 | 附录 $r_t(n)$ 特指置信半径 |
| $G_t$ | 回报 | 不是单次奖励 |
| $\gamma$ | 折扣因子 | 与学习步长 $\alpha$ 不同 |
| $\pi(a\mid s)$ | 给定状态选择动作的概率 | 附录常数 $\pi^2/3$ 的 $\pi$ 是圆周率 |
| $\theta,\mathbf w$ | 参数向量 | 如策略、价值近似器参数；第 3 周 DP 算法的 $\theta$ 特指停止阈值 |
| $v_\pi(s),q_\pi(s,a)$ | 给定策略下的状态 / 动作价值 | 依赖后续策略 |
| $V(s),Q(s,a)$ | 学到的价值估计 | 一般不等于真实价值 |
| $q_*(a)$ | Bandit 动作的真实平均奖励 | 单步均值，不含后继状态项 |
| $q_*$ | 最优平均奖励 | 是数值 |
| $a^*$ | 一个最优动作 | 是动作编号 |
| $Q_t(a)$ | 第 $t$ 轮前的动作价值估计 | 不是真实均值 |
| $N_t(a)$ | 第 $t$ 轮之前选 $a$ 的次数 | 只到 $t-1$ |
| $N_a(T)$ | 完整 $T$ 轮内选 $a$ 的次数 | 等于 $N_{T+1}(a)$ |
| $n$ | 单个动作自己的采样序号 | 与全局 $t$ 区分 |
| $\epsilon$ | 随机探索分支概率 | 随机分支也可能选贪心动作 |
| $\alpha$ | 第 2 周为步长；第 3 周机器人中为转移概率 | 根据当前例子的定义区分 |
| $c$ | UCB 探索系数 | 定理和不同例子的值不相同 |
| $\Delta_a$ | 次优差距 | $q_*-q_*(a)$ |
| $\mathcal R_T$ | 期望累积遗憾 | 别与单次奖励 $R_T$ 混淆 |
| $H_t(a)$ | 梯度 Bandit 的偏好 | 不是奖励估计 |
| $b_t$ | 基线 | 当前采样前确定 |
| $X_t$ | 上下文 | 不受当前动作控制未来的变化 |
| $\mathbb E$ | 数学期望 | 平均意义，不是每次样本值 |
| $\mathbf1\{E\}$ | 指示函数 | 事件成立取 1，否则取 0 |
| $\arg\max$ | 达到最大值的自变量集合 | 区别于最大值 $\max$ |
| $\log$ | 自然对数 | 尤其 UCB 的对数 |
| $\mathcal N(\mu,\sigma^2)$ | 均值为 $\mu$、方差为 $\sigma^2$ 的正态分布 | 第二个参数是方差 |
| i.i.d. | Independent and identically distributed | 独立同分布 |

## 5. 三组高频混淆

**奖励、回报、价值：** 奖励是一次反馈，回报是之后奖励的总和，价值是给定状态或动作、指定后续策略时回报的期望。

**估计值、探索率、步长：** $Q$ 是目前相信的奖励水平，$\epsilon$ 决定多常随机尝试，$\alpha$ 决定新证据改变旧估计的幅度。

**Bandit 与一般序列决策：** Bandit 中动作不改变未来决策状态，所以动作价值是该动作的即时奖励均值；MDP 中动作还改变未来状态，价值必须考虑后续回报。


## 6. MDP 与动态规划

| 中文 | 英文 / 记号 | 含义 | 详细解释 |
| --- | --- | --- | --- |
| 马尔可夫性质 | Markov property | 给定当前状态和动作后，早期历史不再提供预测下一后果的额外信息 | [W3 §1](week03.md#w3-1) |
| 联合转移模型 | $p(s',r\mid s,a)$ | 下一状态与奖励的联合条件分布 | [W3 §1](week03.md#w3-1) |
| 转移概率 | $p(s'\mid s,a)$ | 对奖励求和后的后继状态概率 | [W3 §2](week03.md#w3-2) |
| 期望奖励 | $r(s,a)$ / $r(s,a,s')$ | 给定状态动作 / 进一步给定后继状态的平均奖励 | [W3 §2](week03.md#w3-2) |
| 吸收状态 | Absorbing state | 只转移到自身；本章用零后续奖励的吸收状态表示终止 | [W3 §3](week03.md#w3-3) |
| 平稳策略 | Stationary policy | 行动规则不显式随时间改变，仍可随机选择动作 | [W3 §4](week03.md#w3-4) |
| 贝尔曼期望方程 | Bellman expectation equation | 给定策略的当前价值等于即时奖励加折扣后继价值的期望 | [W3 §4](week03.md#w3-4) |
| 最优价值 | $v_*(s),q_*(s,a)$ | 对后续策略最大化后的期望回报；区别于 Bandit 的即时均值 | [W3 §6](week03.md#w3-6) |
| 贝尔曼最优方程 | Bellman optimality equation | 对动作取最大值，对环境后果仍求期望 | [W3 §6](week03.md#w3-6) |
| 动态规划 | Dynamic programming，DP | 利用已知环境模型进行价值计算和策略优化 | [W3 §7](week03.md#w3-7) |
| 预测 / 控制 | Prediction / Control | 评估给定策略 / 寻找最优策略 | [W3 §7](week03.md#w3-7) |
| 扫描 | Sweep | 每个非终止状态更新一次 | [W3 §7](week03.md#w3-7) |
| 同步 / 原地更新 | Synchronous / In-place | 整轮读旧值 / 更新后立即可用 | [W3 §7](week03.md#w3-7) |
| 策略评估 | Policy evaluation | 固定策略，计算或逼近其价值 | [W3 §7](week03.md#w3-7) |
| 策略改进 | Policy improvement | 依据旧策略价值构造不更差的贪心策略 | [W3 §9](week03.md#w3-9) |
| 策略迭代 | Policy iteration | 交替执行策略评估与策略改进 | [W3 §9](week03.md#w3-9) |
| 价值迭代 | Value iteration | 用含动作最大化的备份更新价值，最终提取策略 | [W3 §10](week03.md#w3-10) |
| 广义策略迭代 | Generalized policy iteration，GPI | 评估与改进以不同粒度相互作用 | [W3 §11](week03.md#w3-11) |
| $\Delta,\theta$ | 本轮最大变化、停止阈值 | 本章 DP 中使用；不同于 Bandit 次优差距 $\Delta_a$ | [W3 §7](week03.md#w3-7) |
