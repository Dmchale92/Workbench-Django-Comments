import requests
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

class StackOverflowMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        if settings.DEBUG:
            intitle = u'{}: {}'.format(exception.__class__.__name__,  exception.message)
            print (intitle)

            url = 'https://api.stackexchange.com/2.2/search'
            headers = { 'User-Agent': 'github.com/dmchale92' }
            params = {
                'order': 'desc',
                'sort': 'votes',
                'site': 'stackoverflow',
                'pagesize': 3,
                'tagged': 'python;django',
                'intitle': intitle
            }

            r = requests.get(url, params=params, headers=headers)
            questions = r.json()

            print('')

            for question in questions['items']:
                print(question['title'])
                print(question['link'])
                print('')

        return None

class PostLimitMiddleware(MiddlewareMixin):
	def process_request(self, request):
		print('Your request is' + str(request))
	# 	# First check to see that IP address is not locked out
	# 	# due to excessively frequent POST requests (more than 2 comments per minute).
	#     ip_blocked = 'IP_BLOCKED_AT_%s' % request.META.get('REMOTE_ADDR')

	#     ip_strike = cache.get(ip_blocked) or 0

	#     # allow up to 2 failures per hour
	#     if ip_strike >= 2:
	#         raise Exception('Locked out for one minute: Too many POST attempts from this address')

	#     try:
	#         return super(TokenAuthentication, self).authenticate(request)

	#     except Exception as e:
	#         # update cache
	#         cache.set(ip_blocked, ip_strike + 1, 60)
	#         raise e

class DuplicateLimitMiddleware(MiddlewareMixin):
	def process_exception(self, request, exception):
		print(exception)
	#     # First check to see that IP address is not locked out
	#     # due to duplicate POST requests.
	#     ip_blocked = 'IP_BLOCKED_AT_%s' % request.META.get('REMOTE_ADDR')

	#     ip_strike = cache.get(ip_blocked) or 0

	#     # allow up to 2 failures per hour
	#     if ip_strike:
	#         raise Exception('Locked out for five minutes: Duplicate comment detected.')

	#     try:
	#         return super(TokenAuthentication, self).authenticate(request)

	#     except Exception as e:
	#         # update cache
	#         cache.set(ip_blocked, ip_strike + 1, 300)
	#         raise e
		return None
	pass
