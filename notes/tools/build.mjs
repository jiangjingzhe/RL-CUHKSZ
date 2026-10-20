// Rebuild the offline reader from Markdown. No network or npm install required.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { Marked } from '../vendor/marked/marked.esm.mjs';
import katex from '../vendor/katex/dist/katex.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const pages = [
  ['README.md', 'index.html', '学习入口'],
  ['week01.md', 'week01.html', '第 1 周 · 强化学习导论'],
  ['week02.md', 'week02.html', '第 2 周 · 多臂老虎机'],
  ['week03.md', 'week03.html', '第 3 周 · MDP 与动态规划'],
  ['week04-05.md', 'week04-05.html', '第 4–5 周 · 基于价值的方法'],
  ['week06.md', 'week06.html', '第 6 周 · 价值函数近似与 DQN'],
  ['week02-appendix.md', 'week02-appendix.html', '第 2 周 · 附录证明'],
  ['glossary.md', 'glossary.html', '术语与符号'],
  ['coverage.md', 'coverage.html', '逐页对应表'],
  ['source-pages.md', 'source-pages.html', '原页图库'],
  ['chapter-template.md', 'chapter-template.html', '后续章节模板'],
  ['MAINTENANCE.md', 'MAINTENANCE.html', '维护说明'],
];
const outputs = new Map(pages.map(([input, output]) => [input, output]));
const esc = s => s.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
let mathCount = 0;
function math(tex, displayMode) {
  mathCount++;
  return katex.renderToString(tex.trim(), { displayMode, throwOnError: true, strict: false, output: 'htmlAndMathml' });
}
const markdown = new Marked({ gfm: true, extensions: [
  {
    name: 'blockMath', level: 'block', start: src => src.indexOf('$$'),
    tokenizer(src) {
      const m = /^\$\$([\s\S]+?)\$\$(?:\n|$)/.exec(src);
      if (m) return { type: 'blockMath', raw: m[0], text: m[1] };
    },
    renderer(token) { return `<div class="equation">${math(token.text, true)}</div>\n`; },
  },
  {
    name: 'inlineMath', level: 'inline', start: src => src.indexOf('$'),
    tokenizer(src) {
      const m = /^\$([^$\n]+?)\$/.exec(src);
      if (m) return { type: 'inlineMath', raw: m[0], text: m[1] };
    },
    renderer(token) { return math(token.text, false); },
  },
] });

for (const [input, output, label] of pages) {
  const source = fs.readFileSync(path.join(root, input), 'utf8');
  let body = markdown.parse(source);
  const toc = [];
  let heading = 0;
  body = body.replace(/<h([23])>([\s\S]*?)<\/h\1>/g, (_, level, content) => {
    const id = `heading-${++heading}`;
    const text = content.replace(/<[^>]+>/g, '').replaceAll('&amp;', '&');
    if (level === '2') toc.push(`<a href="#${id}">${esc(text)}</a>`);
    return `<h${level} id="${id}">${content}</h${level}>`;
  });
  body = body.replace(/href="([^"#]+\.md)(#[^"]*)?"/g, (_, dest, anchor = '') => {
    if (!outputs.has(dest)) throw new Error(`Unknown Markdown link: ${dest}`);
    return `href="${outputs.get(dest)}${anchor}"`;
  });
  body = body.replace(/<table>/g, '<div class="table-scroll"><table>').replace(/<\/table>/g, '</table></div>');
  body = body.replace(/<img /g, '<img loading="lazy" decoding="async" ');
  body = body.replace(/<img\b[^>]*src="([^"]+)"[^>]*>/g, (tag, src) =>
    `<a class="figure-link" href="${src}" target="_blank" rel="noopener" title="打开原课件大图">${tag}</a>`);
  const nav = pages.filter(([input]) => !['chapter-template.md', 'MAINTENANCE.md'].includes(input)).map(([, href, text]) =>
    `<a ${href === output ? 'aria-current="page"' : ''} href="${href}">${text}</a>`).join('\n');
  const html = `<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="CSC6129 强化学习中文自学笔记，保留原例、公式与推导。">
<title>${esc(label)} · 强化学习自学笔记</title>
<link rel="stylesheet" href="vendor/katex/dist/katex.min.css"><link rel="stylesheet" href="reader.css">
</head><body>
<a class="skip" href="#content">跳到正文</a>
<aside class="sidebar"><div class="brand">CSC6129<span>强化学习 · 中文自学笔记</span></div>
<nav aria-label="章节导航">${nav}</nav>
<details class="page-toc" open><summary>本页目录</summary><nav aria-label="本页目录">${toc.join('\n')}</nav></details>
<p class="reader-tip">查找内容：⌘F / Ctrl+F<br>公式可直接阅读，图片可放大查看。</p></aside>
<main id="content"><div class="eyebrow">课程笔记 / 2026 秋季</div><article>${body}</article>
<footer>依据用户提供的课件整理 · 原例与补充解释分开标记 · <a href="${input}">Markdown 原稿</a> · <a href="index.html">返回入口</a></footer></main>
</body></html>`;
  fs.writeFileSync(path.join(root, output), html);
}
console.log(`Built ${pages.length} offline pages; rendered ${mathCount} math expressions.`);
