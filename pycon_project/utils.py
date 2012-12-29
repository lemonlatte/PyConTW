from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.contrib.sites.models import Site

from mailer import send_html_mail


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


def send_email(to, kind, **kwargs):

    current_site = Site.objects.get_current()

    ctx = {
        "current_site": current_site,
        "STATIC_URL": settings.STATIC_URL,
    }
    ctx.update(kwargs.get("context", {}))
    subject = render_to_string("emails/%s/subject.txt" % kind, ctx).strip()
    message_html = render_to_string("emails/%s/message.html" % kind, ctx)
    message_plaintext = strip_tags(message_html)

    from_email = settings.DEFAULT_FROM_EMAIL

    send_html_mail(subject, message_plaintext, message_html, from_email, to)
