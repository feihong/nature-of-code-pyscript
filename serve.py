
from pathlib import Path

from aiohttp import web
from htpy import ul, li, a

import template


src_dir = Path('src')


async def index(_request):
    doc = template.doc('Index', None,
        ul[
            (li[a(href=f'/{f.name}/')[f.name]]
             for f in sorted(src_dir.iterdir()))
        ]
    )
    return web.Response(text=doc, content_type='html')

app = web.Application()
app.add_routes([
    web.get('/', index),
])

if __name__ == '__main__':
    web.run_app(app)
