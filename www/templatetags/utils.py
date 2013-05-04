from django import template
import string

register = template.Library()

@register.simple_tag
def obscure_email(address):
    def obfuscate_char(c):
        if c in string.ascii_lowercase:
            o = string.ascii_lowercase.find(c) + 97
            return '&#%d;' % o
        elif c in string.ascii_uppercase:
            o = string.ascii_uppercase.find(c) + 65
            return '&#%d;' % o
        elif c == '@':
            return '&#0064;'
        else:
            return c
    return ''.join(map(obfuscate_char, address))

@register.simple_tag
def email_link(address):
    safe_addr = obscure_email(address)
    return '<a class="noline" href="mailto:%s">%s</a>' % (safe_addr, safe_addr,)

@register.simple_tag
def url_link(href):
    return '<a class="noline" href="%s">%s</a>' % (href, href,)


