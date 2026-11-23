"""Bundle a locally supplied POC into one offline HTML, without a web server."""
import argparse
import base64
import mimetypes
import re
import zipfile
from pathlib import Path


def build(source: Path, destination: Path):
    source = source.resolve()
    assets = {}
    for p in (source / 'assets').rglob('*'):
        if p.is_file():
            mime = mimetypes.guess_type(p.name)[0] or 'application/octet-stream'
            assets[p.relative_to(source).as_posix()] = 'data:' + mime + ';base64,' + base64.b64encode(p.read_bytes()).decode('ascii')

    def read(relative):
        p = (source / relative).resolve()
        if not p.is_relative_to(source):
            raise ValueError('Resource outside selected source')
        return p.read_text(encoding='utf-8-sig')

    html = read('index.html')

    def script(match):
        code = read(match.group(1))
        for relative, data in assets.items():
            code = code.replace(relative, data)
        # Data URLs preserve vendor strings containing HTML parser delimiters.
        encoded = base64.b64encode(code.encode('utf-8')).decode('ascii')
        return '<script src="data:text/javascript;base64,' + encoded + '"></script>'

    def style(match):
        css = read(match.group(1))
        if re.search(r'@import\s', css):
            raise ValueError('External CSS import requires explicit bundling')
        return '<style>\n' + css + '\n</style>'

    html = re.sub(r'<script\s+src="([^"]+)"\s*>\s*</script>', script, html)
    html = re.sub(r'<link\s+rel="stylesheet"\s+href="([^"]+)"\s*/?>', style, html)
    html = html.replace('<head>', '<head>\n<!-- Offline single-file POC. All runtime scripts, styles and images embedded. AI processing remains simulated. -->', 1)
    assert not re.search(r'<script\s+src="(?!data:)|<link\s+rel="stylesheet"', html)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(html, encoding='utf-8')
    # ZIP downloads reliably instead of displaying HTML as raw source.
    with zipfile.ZipFile(destination.with_suffix('.zip'), 'w', zipfile.ZIP_DEFLATED) as bundle:
        bundle.write(destination, destination.name)
    print(f'Bundled {len(assets)} images; {destination.stat().st_size:,} bytes; {destination.name}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--output', type=Path, default=Path(__file__).resolve().parents[1] / 'demos/industrial-document-poc.html')
    args = parser.parse_args()
    build(args.source, args.output)
