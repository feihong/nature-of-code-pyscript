from htpy import html, head, meta, title as title_tag, style, body, h1


css = """
/* https://www.swyx.io/css-100-bytes */
html {
  max-width: 70ch;
  padding: 3em 1em;
  margin: auto;
  line-height: 1.75;
  font-size: 1.25em;
}
canvas {
    border: 1px solid lightgray;
}
"""

def doc(title, caption, *children):
    return str(
        html[
            head[
                meta(charset='utf-8'),
                title_tag[title],
                style[css],
            ],
            body[
                h1[title],
                caption,
                *children,
            ],
        ]
    )
