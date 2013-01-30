
class NoCache(object):

    def process_response(self, request, response):
        response['Cache-Control'] = 'private, max-age=0, no-cache, no-store, must-revalidate'
        return response
