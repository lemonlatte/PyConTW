from django.conf.global_settings import LANGUAGES


def language_path(request):
    context_extras = {}
    codes = []
    paths = request.path.split('/')
    for code, name in LANGUAGES:
        codes.append(code)
    try:
        if paths[1] in codes:
            del paths[1]
        if paths[2] in codes:
            del paths[2]
    except:
        pass
    context_extras["no_lang_path"] = '/'.join(paths)
    return context_extras
