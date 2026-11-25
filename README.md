# Content-first Editing | 内容优先的文本润色

面向已有草稿的 Agent Skill。先充分生成，再精确编辑。目标为内容保真、阅读效率、自然度和专业表达；不面向 AI 检测规避。

## 使用

将整个 `content-first-editing` 目录复制到支持 Agent Skills 的客户端所配置的 skills 目录。入口为 `SKILL.md`。无需外部 API 或依赖；可选检查脚本只使用 Python 3 标准库。

在普通对话中也可直接提供 `SKILL.md` 内容作为后置编辑指令；参考文件可按需附上。

调用示例：

- 使用 content-first-editing 标准润色以下已有稿件，只输出正文。
- 先完整检索资料并撰写信息充分的初稿，完成后调用 content-first-editing 润色。保留事实、证据和专业细节。
- 使用 content-first-editing 深度编辑第二章，保留引用与数据，另列证据缺口。
- 使用 content-first-editing 仅审阅，找出无实质信息和阅读障碍，不改文件。

## 结构

- `SKILL.md`：核心编辑契约、八条原则与流程
- `references/genres.md`：文体与读者适配
- `references/patterns.md`：问题模式及正反例
- `references/research-notes.md`：调研来源、借鉴与限制
- `evals/cases.jsonl`：人工或模型评测用例（未做跨模型实验）
- `evals/README.md`：评测方法及验收标准
- `scripts/check_invariants.py`：数字、引用、链接与行内代码的启发式差异提示
- `scripts/test_check_invariants.py`：脚本单元测试

检查器仅适用于 UTF-8 纯文本或 Markdown，不验证事实、引用指向、数字语义、Word 格式等。匹配变化可来自合理编辑，未匹配到的错误也可能存在。运行时不要把报告当作唯一验收依据。

```sh
python scripts/check_invariants.py before.md after.md
python -m unittest discover -s scripts -p 'test_*.py'
```

v1.0 为原创指令包，按 Agent Skills 公开格式组织，尚未在各客户端实际安装及跨模型实测。未指定开源许可证；发布者可在发布前自行选择许可证并检查项目名称冲突。
