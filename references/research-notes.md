# 调研来源与设计选择

调研日期：2026-11-25。以下为项目公开 README / Skill 规则的比较，不代表已执行或独立验证其宣传的实验结果。未复制其规则原文或脚本；当前实现依据用户原始规范重新撰写。

| 项目 | 参考点 | 本项目取舍 |
| --- | --- | --- |
| [blader/humanizer](https://github.com/blader/humanizer) | AI 写作模式与改稿流程 | 将模式作为诊断线索，不作为目标或身份判断 |
| [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | 冗词、句式及表达检查 | 不强制禁用标点、句型、被动语态 |
| [jiji262/humanizer-chinese](https://github.com/jiji262/humanizer-chinese) | 中文语域、中文特有模式 | 保留语言适配，不主动添加立场或个人色彩 |
| [Xiangson/lieflat-less-ai-tone](https://github.com/Xiangson/lieflat-less-ai-tone) | 语料驱动检测、信息守恒与最小改动 | 同样保护信息，扩展到专业分析的显性化、读者理解成本 |
| [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | 有限迭代、审阅与编辑范围 | 一次编辑及一次复核修正，允许零修改 |
| [DawnJson/zh-paper-polish](https://github.com/DawnJson/zh-paper-polish) | 中文期刊语料基线、数值引文对比 | 不引入其语料阈值或 CC BY-NC-SA 实现，独立编写辅助检查 |
| [junbolian/Academic-Humanizer](https://github.com/junbolian/Academic-Humanizer) | 证据限定、结构保护、改前改后核验 | 后置编辑，不另设初稿写作模式 |
| [cmyhj/chinese-academic-humanizer](https://github.com/cmyhj/chinese-academic-humanizer) | 跨段论证与工程语义 | 扩展到多种非虚构文体，保持授权边界 |
| [ysyecust/write-reader-first-papers](https://github.com/ysyecust/write-reader-first-papers) | 读者优先、专业语义、编辑契约 | 用通用文本编辑及生成/编辑分阶段作为主定位 |
| [jt1024/academic-polish](https://github.com/jt1024/academic-polish) | 双语学术润色、按需参考 | 默认保留输入语言，不自动翻译 |
| [dvdsosa/scientific-writing-skills](https://github.com/dvdsosa/scientific-writing-skills) | 科研文章与段落编辑 | 按文体设参考，而非完整科研写作流水线 |
| [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) | 写作、科研证据及引用流程 | 核查和补充研究另设授权，不把研究流程混入润色 |
| [vale-cli/vale](https://github.com/vale-cli/vale)、[amperser/proselint](https://github.com/amperser/proselint)、[textlint/textlint](https://github.com/textlint/textlint) | 可编程文本检查 | 辅助提示，不替代语义判断，不作为依赖 |
| [hachiwar/Chinese-Document-Style-and-Typography-Guidelines](https://github.com/hachiwar/Chinese-Document-Style-and-Typography-Guidelines) | 中文排版与格式规范分级 | 优先已有格式和机构要求 |
| [Daguilar0123/ai-writing-skill-field-guide](https://github.com/Daguilar0123/ai-writing-skill-field-guide) | 技能比较和输出评测的思路 | 不以 stars 或单一检测器结果证明效果 |
| [Agent Skills specification](https://agentskills.io/specification) | YAML 元数据、按需加载参考文件 | 核心短规则与可选参考分离 |

差异化假设：分离充分初稿和精确编辑，以命题保真、阅读功能和授权范围共同约束编辑。相关能力已有项目实现，独特性来自组合、默认行为和未来实证，不是宣称首创。建议下一版建立人工标注的中文多文体盲评基准，尤其包含良好原文、教学解释和方法细节等不应修改的反例。
