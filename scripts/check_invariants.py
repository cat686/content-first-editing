#!/usr/bin/env python3
"""Heuristic, read-only diff of protected tokens in UTF-8 plain text/Markdown."""
import argparse
import json
import re
from collections import Counter
from pathlib import Path

PATTERNS = {
    'numbers': r'(?<![A-Za-z0-9])[-+−]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?:[eE][-+]?\d+)?(?:\s*[%％‰])?',
    'citations': r'\[(?:\d+(?:\s*[-–,，;；]\s*\d+)*)\]|\[@[^\]\n]+\]|\\cite\w*\{[^}\n]+\}',
    'urls': r'https?://[^\s<>\]\)"，。；、]+',
    'inline_code': r'(?<!`)`([^`\n]+)`(?!`)',
}

def tokens(text):
    return {key: Counter(re.findall(pattern, text)) for key, pattern in PATTERNS.items()}

def compare(before, after):
    a, b = tokens(before), tokens(after)
    return {key: {'removed': dict(a[key] - b[key]), 'added': dict(b[key] - a[key])} for key in PATTERNS}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('before', type=Path)
    parser.add_argument('after', type=Path)
    args = parser.parse_args()
    try:
        result = compare(args.before.read_text(encoding='utf-8'), args.after.read_text(encoding='utf-8'))
    except (OSError, UnicodeError) as exc:
        parser.exit(2, f'Cannot read input: {exc}\n')
    changed = any(v['removed'] or v['added'] for v in result.values())
    print(json.dumps({'status': 'review_required' if changed else 'no_matched_token_changes', 'differences': result, 'limitations': 'Heuristic only. Does not verify meaning, units, citation attachment, truth, or formatting. Repeated tokens may change legitimately.'}, ensure_ascii=False, indent=2))
    return int(changed)

if __name__ == '__main__':
    raise SystemExit(main())
