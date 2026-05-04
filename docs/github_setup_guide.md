# GitHub 仓库配置指南

为了让 EvoAML 看起来像一个真正面向社区和监管机构的开源项目，我们需要配置以下 GitHub 仓库设置。请你（项目Owner）在 GitHub 网页端完成以下配置后告诉我：

## 1. 基础信息配置 (About 区域)
* **Description:** 开发并推进一个融合图网络跨行业监控与时序行为演化分析的智能AML检测框架（EvoAML），旨在弥合当前反洗钱基础设施在跨行业资金流追踪和动态洗钱模式识别上的系统性技术缺口，并将该方法论转化为符合美国监管框架（BSA/AMLA 2020）的可部署解决方案。
* **Website:** （如果有相关论文链接或个人主页，可以放这里，没有留空即可）
* **Topics (Tags):** `aml`, `anti-money-laundering`, `fincen`, `bsa`, `amla2020`, `regtech`, `compliance`, `graph-neural-networks`, `federated-learning`, `time-series-analysis`

## 2. 仓库设置 (Settings)
* **Features:**
    * [x] Wikis (建议开启，未来可以把合规文档放这里)
    * [x] Issues
    * [x] Discussions (建议开启，营造社区讨论的氛围)
* **Merge button:**
    * 建议只勾选 `Allow squash merging`，保持提交历史干净。

## 3. 分支保护 (Branch Protection Rules)
* **Branch name pattern:** `main` 或 `master`
* **Require a pull request before merging:** 勾选
* **Require approvals:** 勾选，设为 1 (这意味着程序员提交代码后，必须经过审查员 Approve 才能合并，体现开发规范)。

## 4. 准备好 GitHub Token (用于自动化推送)
为了让我们的“审查员”可以直接将代码推送到你的 GitHub 仓库，你需要生成一个 Personal Access Token (PAT) 或者配置 SSH Key。
* 如果使用 PAT：进入 GitHub -> Settings -> Developer settings -> Personal access tokens (Tokens (classic)) -> Generate new token。勾选 `repo` 权限。
* （或者你也可以先建好空仓库，把 Git URL 发给我，我安排审查员配置本地 Git）

请你先在 GitHub 上创建一个名为 `EvoAML` 的空仓库，然后将仓库地址（例如 `https://github.com/your-username/EvoAML.git`）发给我，如果有 Token 也请通过私信或安全方式提供（或者由你自己执行 push）。
