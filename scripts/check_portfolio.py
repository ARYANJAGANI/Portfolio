"""Check generated pages for broken local references and structural mistakes."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids, self.refs, self.external_errors = [], [], []
        self.h1 = 0
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'h1':
            self.h1 += 1
        for name in ('href', 'src'):
            if name in attrs:
                self.refs.append(attrs[name])
        if tag == 'a' and attrs.get('target') == '_blank':
            if 'noopener' not in attrs.get('rel', '').split():
                self.external_errors.append(attrs.get('href', ''))

pages = {p.name: Page(p) for p in ROOT.glob('*.html')}
errors = []
for name, page in pages.items():
    if page.h1 != 1:
        errors.append(f'{name}: expected one h1, found {page.h1}')
    for identifier, count in Counter(page.ids).items():
        if count > 1:
            errors.append(f'{name}: duplicate ID {identifier}')
    for ref in page.refs:
        url = urlsplit(ref)
        if url.scheme or url.netloc:
            continue
        target = unquote(url.path) or name
        if not (ROOT / target).exists():
            errors.append(f'{name}: missing local target {target}')
        if url.fragment and target in pages and url.fragment not in pages[target].ids:
            errors.append(f'{name}: missing anchor {ref}')
    for ref in page.external_errors:
        errors.append(f'{name}: new-tab link missing noopener: {ref}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(pages)} pages; local references, IDs, headings, and new-tab links verified.')
