# 卞颖慧

西南交通大学 · 控制工程硕士在读 · 2028 届

[个人网站](https://ovo-daisy28.github.io/)

## 关于我

我本科读无人驾驶航空器系统工程，硕士研究四旋翼无人机双摆吊运控制。有两类系统集成经历。无人机侧，我参与过 Linux／ROS 控制接口适配，用 PX4＋Gazebo 做软件在环验证。AI 应用侧，我做过企业 RAG 原型、平台和模型部署，以及从文档入库到问答的接口验证。

## 正在做什么

- **四旋翼双摆吊运控制**　用 Simulink 和 MuJoCo 建模与仿真，在 MuJoCo 中读取两级摆角和摆角速度，观察吊载的运动状态。
- **无人机 Agent 仿真**　学习如何让 Agent 调用仿真工具、读取执行反馈，并用最终状态判断任务是否完成。

## 代表项目

### 中科闻歌 · 企业 RAG 实习

**要解决的问题**　把分散在采购文件和设备资料里的内容变成可检索的知识，支持查找原文、文档问答和手册生成。

**我做的工作**　完成可操作的 POC，部署 RAG 平台和模型服务。用 FastAPI 开发批量导入与查询接口，记录每份文档的处理状态和各阶段耗时，便于定位失败任务。

**怎么验证**　做过万份量级的导入测试，通过阶段耗时定位 Embedding 瓶颈。用实际问答用例验证接口和图谱功能，并针对问答响应时间做优化。

演示使用预置结果。[下载离线演示 ZIP](https://github.com/OvO-Daisy28/OvO-Daisy28/raw/refs/heads/main/demos/industrial-document-poc.zip) → 解压 → 用 Chrome 或 Edge 打开 `industrial-document-poc.html`。

### Signal · 营销分析 Agent

**要解决的问题**　让用户用自然语言提出电商数据分析问题，获得一份可以回查数据来源、修改并确认发布的报告。

**我做的工作**　独立实现报表 Skill 和 ReAct 工具调用循环。程序按固定口径计算指标，Agent 根据问题选择查询工具并整理证据。分析过程中保存目标、假设和证据，用户可回查分组条件、样本量和计算结果。

**怎么验证**　在一轮独立数值核对中，181 个聚合结果与 CSV 重算一致。仓库里有固定体验案例、评测方法和失败样例。 [GitHub 仓库](https://github.com/OvO-Daisy28/marketing-analysis-agent)

## 技能

- **机器人软件与仿真**　`Linux` · `C++` · `ROS` · `PX4` · `Gazebo` · `MuJoCo` · `Simulink`
- **RAG 与模型部署**　`Python` · `FastAPI` · `Docker` · `RAGFlow` · `Elasticsearch` · `vLLM` · `BGE-M3`
- **Agent 开发**　`Function Calling` · `ReAct` · `PostgreSQL` · 工具结果核对和报告交付
