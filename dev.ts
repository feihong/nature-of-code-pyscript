import * as fs from 'node:fs/promises'
import { Hono } from 'hono'
import { serveStatic } from 'hono/bun'

const app = new Hono()

const mimes = {
  py: 'text/x-python',
}

app.use('/static/*', serveStatic({ root: './', mimes }))

app.get('/', async (c) => {
  const body = '<ul>' + (await fs.readdir('./src')).map(f => `<li><a href="/${f}/">${f}</a></li>`).join('\n') + '</ul>'
  return c.html(getHtml('Home', '', body))
})

const py2jsMap = {
  '/static/q5.py': 'https://q5js.org/q5.js',
  '/static/p5.py': 'https://cdn.jsdelivr.net/npm/p5@1.11.2/lib/p5.min.js',
  '/static/ml5.py': 'https://unpkg.com/ml5@1/dist/ml5.min.js',
  '/static/p5i.py': 'https://cdn.jsdelivr.net/npm/p5@1.11.2/lib/p5.min.js',
}

app.get('/:path{.+/}', async (c) => {
  const path = c.req.path
  const realPath = './src/' + path
  const configFile = Bun.file(realPath + 'config.json')
  if (!await configFile.exists()) {
    const files = (await fs.readdir(`./src/${path}`))
    files.sort()
    const body = '<ul>' + files.map(filename => {
      const url = `${path}${filename}` + (filename.includes('.') ? '' : '/')
      return `<li><a href="${url}">${filename}</a></li>`
    }).join('\n') + '</ul>'
    return c.html(getHtml(path, '', body))
  } else {
    const config = JSON.parse(await configFile.text())
    const pyscript = `<link rel="stylesheet" href="https://pyscript.net/releases/2024.11.1/core.css">
      <script type="module" src="https://pyscript.net/releases/2024.11.1/core.js"></script>`
    const scripts = Object.keys(config.files)
      .filter(f => py2jsMap[f])
      .map(f => `<script src="${py2jsMap[f]}"></script>`)
      .join('\n')
    const head = pyscript + scripts
    const body = '<script type="py" src="./main.py" config="./config.json"></script>'
    return c.html(getHtml(config.name, head, body))
  }
})

app.get(
  '/*',
  serveStatic({
    root: './',
    mimes,
    rewriteRequestPath: (path) => {
      return '/src' + path
    },
  })
)

function getHtml(title : string, head : string, body : string) : string {
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${title}</title>
  <style>
    /* https://www.swyx.io/css-100-bytes */
    html {
      max-width: 70ch;
      line-height: 1.25;
      font-size: 1.25em;
      padding: 0 1em;
    }
    canvas {
      border: 1px solid lightgray;
    }
  </style>
  ${head}
</head>
<body>
  <h1>${title}</h1>
  ${body}
</body>
</html>`
}

export default {
  port: 8000,
  fetch: app.fetch,
}
