import * as fs from "node:fs/promises"
import toml from 'toml'
import { Hono } from 'hono'
import { serveStatic } from 'hono/bun'

const app = new Hono()

const mimes = {
  py: 'text/x-python',
}

app.use('/static/*', serveStatic({ root: './', mimes }))

app.get('/', async (c) => {
  const files = await fs.readdir('./src')
  const body = '<ul>' + files.map(f => `<li><a href="/${f}/">${f}</a></li>`).join('\n') + '</ul>'
  return c.html(getHtml('Chapters', '', body))
})

app.get('/:chapter/', async (c) => {
  const chapter = c.req.param('chapter')
  const files = (await fs.readdir(`./src/${chapter}`))
  const body = '<ul>' + files.map(filename => {
    const url = `/${chapter}/${filename}/`
    return `<li><a href="${url}">${filename}</a></li>`
  }).join('\n') + '</ul>'
  return c.html(getHtml(chapter, '', body))
})

app.get('/:chapter/:example/', async (c) => {
  const { chapter, example } = c.req.param()
  const jsonFile = `./src/${chapter}/${example}/config.json`
  const config = JSON.parse(await Bun.file(jsonFile).text())
  const head = `<link rel="stylesheet" href="https://pyscript.net/releases/2024.11.1/core.css">
    <script type="module" src="https://pyscript.net/releases/2024.11.1/core.js"></script>
    <script src="https://q5js.org/q5.js"></script>`
  const body = `<script type="py" src="./main.py" config="./config.json"></script>
    <div id="sketch"></div>`
  return c.html(getHtml(config.name, head, body))
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
    }
    main {
      padding: 0 1em;
    }
    canvas {
      border: 1px solid lightgray;
    }
  </style>
  ${head}
</head>
<body>
  <main>
    <h1>${title}</h1>
    ${body}
  </main>
</body>
</html>`
}

export default {
  port: 8000,
  fetch: app.fetch,
}
