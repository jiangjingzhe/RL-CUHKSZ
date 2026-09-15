"""Regenerate source manifest, coverage table, and slide gallery.

Run with Python 3 and pypdf. Add --render to refresh page JPGs
(requires pypdfium2 and Pillow). PDF paths are relative to this project.
"""
from pathlib import Path
import argparse
import hashlib
import json
from pypdf import PdfReader

NOTES = Path(__file__).resolve().parents[1]
ROOT = NOTES.parent

SECTIONS = {
    1: {
        1: '强化学习要解决什么问题', 2: '为什么语言模型也用强化学习',
        3: '智能体怎样与环境交互', 4: '奖励、回报、策略、价值与模型',
        5: '井字棋完整例子', 6: '大状态空间、先验知识与历史',
        7: 'LLM、Bandit 与后续课程', 8: '课程安排与考核',
        9: '复习与自测', 10: '课件参考文献',
    },
    2: {
        1: '问题、真实价值与估计值', 2: '贪心与 epsilon-greedy',
        3: '增量更新与非平稳奖励', 4: '乐观初始化', 5: 'UCB',
        6: '遗憾与 UCB1 保证', 7: '梯度 Bandit', 8: '上下文 Bandit',
        9: '方法比较与 MDP 预告', 10: '复习与参考文献',
    },
}

# Every physical PDF page must map to a substantive note section.
MAP = {
    1: {
        **dict.fromkeys(range(1, 3), 8), 3: 1,
        **dict.fromkeys(range(4, 12), 2),
        **dict.fromkeys(range(12, 19), 8),
        **dict.fromkeys(range(19, 27), 1),
        **dict.fromkeys(range(27, 30), 3),
        **dict.fromkeys(range(30, 37), 4), 37: 3, 38: 4,
        **dict.fromkeys(range(39, 48), 5),
        **dict.fromkeys(range(48, 51), 6), 51: 7, 52: 7, 53: 10, 54: 10,
    },
    2: {
        **dict.fromkeys(range(1, 7), 1),
        **dict.fromkeys(range(7, 13), 2),
        **dict.fromkeys(range(13, 20), 3),
        **dict.fromkeys(range(20, 23), 4),
        **dict.fromkeys(range(23, 26), 5),
        **dict.fromkeys(range(26, 32), 6),
        **dict.fromkeys(range(32, 40), 7),
        **dict.fromkeys(range(40, 44), 8),
        **dict.fromkeys(range(44, 47), 9), 47: 10,
        **dict.fromkeys(range(48, 52), 'ucb-proof'), 52: 'softmax-proof',
    },
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--render', action='store_true')
    args = parser.parse_args()
    coverage = ['# 原课件逐页对应表', '',
                '[学习入口](README.md) · [原页图库](source-pages.md)', '',
                '逐页列出实际 PDF 页面及其笔记位置。封面、重复目录与分隔页合并到对应章节；知识点、公式、例子与实验在正文重组说明。此表用于溯源，不将仅保留原图等同于中文讲解。', '']
    gallery = ['# 原课件全页图库', '', '[学习入口](README.md) · [逐页对应表](coverage.md)', '',
               '保留用户提供课件的原始页面。中文讲解见每页的“对应笔记”，可点击图片链接查看大图。', '']
    manifest = {'version': 1, 'prepared': '2026-09-15', 'sources': []}
    for week, filename in [(1, 'Week 1-Revised.pdf'), (2, 'Week 2.pdf')]:
        path = ROOT / filename
        pdf = PdfReader(path)
        count = len(pdf.pages)
        if set(MAP[week]) != set(range(1, count+1)):
            raise ValueError(f'Coverage must be updated for {filename}')
        rendered = None
        if args.render:
            import pypdfium2
            rendered = pypdfium2.PdfDocument(path)
        manifest['sources'].append({
            'week': week, 'path': '../'+filename, 'pdf_pages': count,
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'page_numbering': '1–54' if week == 1 else '正文 1–47；PDF P48–52 的页脚为附录 1–5',
        })
        coverage.extend([f'<a id="week{week:02}"></a>', f'## 第 {week} 周：{count} 页', '',
                         '| PDF 页 | 原页主题 | 中文笔记位置 | 原始版面 |',
                         '| ---: | --- | --- | --- |'])
        gallery.extend([f'## 第 {week} 周', ''])
        for p, page in enumerate(pdf.pages, 1):
            lines = [line.strip() for line in (page.extract_text() or '').splitlines() if line.strip()]
            title = lines[0]
            if title == '.':
                title = lines[1]
            if week == 1 and p == 26:
                title += ' Long-Term Return'
            section = MAP[week][p]
            if isinstance(section, int):
                target = f'week{week:02}.md#w{week}-{section}'
                label = f'§{section} {SECTIONS[week][section]}'
            else:
                target = f'week02-appendix.md#{section}'
                label = '附录 A：UCB1 完整证明' if section == 'ucb-proof' else '附录 B：Softmax 求导'
            pic = f'assets/week{week:02}/page-{p:02}.jpg'
            title = title.replace('|', ' / ')
            coverage.append(f'| {p} | {title} | [{label}]({target}) | [P{p}]({pic}) |')
            gallery.extend([f'<a id="w{week}-p{p}"></a>', f'### 第 {week} 周 · P{p} · {title}', '',
                            f'[对应笔记]({target}) · [查看大图]({pic})', '',
                            f'![第 {week} 周原课件 P{p}：{title}]({pic})', ''])
            if rendered:
                output = NOTES / pic
                output.parent.mkdir(parents=True, exist_ok=True)
                rendered[p-1].render(scale=3.5).to_pil().convert('RGB').save(output, quality=90)
        coverage.append('')
    (NOTES / 'coverage.md').write_text('\n'.join(coverage), encoding='utf-8')
    (NOTES / 'source-pages.md').write_text('\n'.join(gallery), encoding='utf-8')
    (NOTES / 'sources.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print('Source index generated: 54 + 52 = 106 pages.')

if __name__ == '__main__':
    main()
