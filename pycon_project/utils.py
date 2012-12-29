import markdown
from html5lib import html5parser, sanitizer


def sanitize_html(stream):

    bits = []
    parser = html5parser.HTMLParser(tokenizer=sanitizer.HTMLSanitizer)
    for token in parser.parseFragment(stream).childNodes:
        bits.append(token.toxml())
    return "".join(bits)


def markdown_parser(text):
    text = markdown.markdown(text, extensions=["extra"], safe_mode=False)
    return sanitize_html(text)
