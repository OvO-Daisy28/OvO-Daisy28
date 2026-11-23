# 卞颖慧 · 大模型应用与 AI 解决方案

西南交通大学 · 控制工程硕士在读 · 2028 届

关注如何将业务需求落实为可操作的 AI 应用：**POC 开发、RAG 集成与模型部署、Agent 工具调用、上下文管理和评测验证**。

## 项目与体验入口

| 项目 | 解决什么问题 | 体验方式 |
|---|---|---|
| **中科闻歌 · 采购文件活化 POC** | 将工程文档的解析、人工审核、知识检索和手册生成串成可操作流程 | **[下载离线演示 ZIP](https://github.com/OvO-Daisy28/OvO-Daisy28/raw/refs/heads/main/demos/industrial-document-poc.zip)** · 解压后打开 HTML |
| **Signal · 营销分析 Agent** | 用报表 Skill 与研究 Loop 完成营销数据分析、证据关联和报告交付 | **[查看项目源码与运行说明](https://github.com/OvO-Daisy28/marketing-analysis-agent)** · [打开在线案例](https://ovo-daisy28.github.io/marketing-analysis-agent/) |

## 中科闻歌｜POC 实现与部署验证

**我的工作：**依据团队与甲方技术部门沟通形成的技术规范书，完成 POC 开发与演示材料制作，并独立开展后续 RAG 平台部署、开发、测试和优化。

- **规范落地与原型：**将解析、入库、知识化、治理和生成要求落实为页面及跨页交互，支持原文对照审核、内容复用和手册导出。
- **部署与集成：**实际实习工作涉及 RAGFlow、FastAPI、MinerU、Elasticsearch、vLLM 和 BGE-M3 GPU 服务，完成导入开发、建图链路排障及问答测试。
- **演示材料：**整理重点需求与功能截图的对应关系，以及完整业务流程的演示脚本。

**离线体验：**点击上方链接下载 ZIP → 解压 → 用 Chrome 或 Edge 打开其中的 `industrial-document-poc.html`。JavaScript、CSS 和图片已经嵌入同一文件，无需安装依赖、启动服务或填写模型密钥。

推荐路线：**工作台 → 内容解析 → 知识库与图谱 → 手册生成 → 导出 Word**。

> 此文件保留原 POC 的前端交互，AI 处理使用预置结果与动画模拟，界面中的准确率、耗时等数字为演示数据。离线演示不连接企业后台；后续 RAG 部署和测试属于另行开展的实习工作。

## 营销分析 Agent｜个人开源项目

面向营销人员的数据查询、策略分析与报告需求，基于公开电商数据独立实现。

- **报表 Skill：**封装指标与接口合同、受控页面模板和图表配方，支持预览、版本修改和用户确认发布。
- **研究 Loop：**自建 ReAct 工具调用循环，持久化目标、假设、证据与结论，逐轮构建上下文并检查完成条件。
- **工程验证：**后台 Worker、PostgreSQL 任务租约、幂等与恢复、预算限制、固定案例及数值核验。

在线案例是无需密钥的固定示例；真实模型模式的运行步骤、评测结果与已知边界见[项目 README](https://github.com/OvO-Daisy28/marketing-analysis-agent)。

## 技术方向

`Python` · `FastAPI` · `RAGFlow` · `Elasticsearch` · `Docker` · `vLLM` · `Embedding / LoRA` · `ReAct / Tool Calling` · `Skill` · `Context Management`

下载说明：GitHub 的 HTML 原始文件链接可能展示源码，因此入口提供 ZIP 下载包。解压后的 HTML 可以直接在浏览器中运行，不依赖 `chatgpt.site`；下载过程仍需要能够访问 GitHub。
