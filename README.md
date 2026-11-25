# Content-first Editing | 内容优先的文本润色

简体中文 · [English](README.en.md)

Content-first Editing 是一个润色中英文成稿的 Agent Skill，适用于文章、论文、报告和技术文档。初稿完成后，用它删去套话和重复、理顺句段，同时保留原稿的事实、数据、引用、限定条件和作者立场。

## 快速开始

**交给 Agent 安装**

把下面这句发给支持安装 Skills 的 Agent。

> 帮我从 <https://github.com/cat686/content-first-editing> 下载并安装 Content-first Editing Skill。

**在终端安装**

在项目目录运行以下命令，按提示选择你的 Agent。

```bash
npx skills add cat686/content-first-editing --skill content-first-editing
```

也可以手动把整个仓库复制到客户端的 Skills 目录。

**使用**

安装后，粘贴草稿或提供文件路径，再发送类似的指令。

> 用 content-first-editing 润色 `draft.md`。删减套话和重复，保留数据、引用和结论的适用范围。

只想听修改建议时，可以指定“仅审阅”。需要重排段落或调整论证顺序时，可以指定“深度编辑”。

## 改写示例

**原稿**

> 这不是一次简单的流程优化，而是给人工审核加了一道质量门禁。系统在提交工单时校验必填字段，校验通过后，工单才会进入人工审核。平均审核时间从 18 分钟降到 12 分钟，但这一结果只在重复提交率超过 40% 的测试批次中观察到。

**润色后**

> 系统在工单提交时校验必填字段，通过校验后才将工单转给人工审核。只有在重复提交率超过 40% 的测试批次中，平均审核时间才从 18 分钟降到 12 分钟。

## 主要结构

| 路径 | 内容 |
| --- | --- |
| [`SKILL.md`](SKILL.md) | Skill 入口，包含编辑模式、流程和保真检查 |
| [`references/`](references/) | 文体指南、常见表达问题和调研笔记 |
| [`scripts/`](scripts/) | 可选的差异检查脚本和单元测试。脚本可标出数字、引用标记、链接和行内代码的变化 |
| [`evals/`](evals/) | 评测用例、方法与验收标准 |

当前版本未附许可证。
