# Content-first Editing

[简体中文](README.md) · English

Content-first Editing is an Agent Skill for revising Chinese and English drafts, including articles, papers, reports, and technical documentation. Once you have a draft, use it to cut filler and repetition, clarify sentences and paragraphs, and preserve the facts, data, citations, qualifications, and author's position.

## Quick Start

**Install through your agent**

Send the following to an agent that can install skills.

> Please download and install the Content-first Editing skill from <https://github.com/cat686/content-first-editing>.

**Install from the terminal**

Run this command in your project directory and select your agent when prompted.

```bash
npx skills add cat686/content-first-editing --skill content-first-editing
```

You can also copy the entire repository into your client's skills directory.

**Use the skill**

Paste your draft or provide its file path, then send a request like this one.

> Use content-first-editing to revise `draft.md`. Cut filler and repetition. Preserve the data, citations, and scope of the conclusions.

Ask for a review only if you want feedback on the draft. Ask for a substantive edit if you want to reorder paragraphs or restructure the argument.

## Editing Example

**Before**

> This is not just a workflow improvement but a quality gate for manual review. The system checks required fields when a ticket is submitted, and only tickets that pass the check proceed to manual review. Average review time dropped from 18 to 12 minutes, but this result was observed only in test batches with a duplicate submission rate above 40%.

**After**

> When a ticket is submitted, the system checks its required fields. Only tickets that pass the check proceed to manual review. The drop in average review time from 18 to 12 minutes was observed only in test batches with a duplicate submission rate above 40%.

## Repository Structure

| Path | Contents |
| --- | --- |
| [`SKILL.md`](SKILL.md) | Entry point with editing modes, workflow, and checks for preserving meaning |
| [`references/`](references/) | Genre guides, common writing issues, and research notes |
| [`scripts/`](scripts/) | Optional checker for changes to numbers, citation markers, links, and inline code, plus unit tests |
| [`evals/`](evals/) | Evaluation cases, methods, and acceptance criteria |

This release does not include a license.
