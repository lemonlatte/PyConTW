from django.utils import translation

class I18NUrl(object):

    def process_request(self, request):
        lang = request.path.split("/")[1]
        if lang in ["en", "zh_tw"]:
            translation.activate(lang)
            request.LANGUAGE_CODE = translation.get_language()
            request.session['django_language'] = request.LANGUAGE_CODE

