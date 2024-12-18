import * as fs from "node:fs/promises"
import { Hono } from 'hono'
import { serveStatic } from 'hono/bun'

const app = new Hono()

app.use('/p5.py', serveStatic({ path: './src/p5.py' }))

app.get('/', (c) => {
  return c.html('<h1>Hello Blarp!</h1>')
})

export default {
  port: 8000,
  fetch: app.fetch,
}
