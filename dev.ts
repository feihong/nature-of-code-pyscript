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
    .filter(f => f.endsWith('.json'))
    .map(f => f.substring(0, f.length - 5))
  const body = '<ul>' + files.map(filename => {
    const url = `/${chapter}/${filename}.html`
    return `<li><a href="${url}">${filename}</a></li>`
  }).join('\n') + '</ul>'
  return c.html(getHtml('Chapters', '', body))
})

app.get('/:chapter/:page{.+\.html}', async (c) => {
  const { chapter, page } = c.req.param()
  const name = page.substring(0, page.length - 5)
  const jsonFile = `./src/${chapter}/${name}.json`
  const config = JSON.parse(await Bun.file(jsonFile).text())
  const head = `<link rel="stylesheet" href="https://pyscript.net/releases/2024.11.1/core.css">
    <script type="module" src="https://pyscript.net/releases/2024.11.1/core.js"></script>
    <script src="https://q5js.org/q5.js"></script>`
  const body = `<script type="py" src="./${name}.py" config="./${name}.json"></script>
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
      padding: 3em 1em;
      margin: auto;
      line-height: 1.75;
      font-size: 1.25em;
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
