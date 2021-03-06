from Comments.models import Comment
from django import http
from django.conf import settings
from django.core.cache import cache
from django.utils.deprecation import MiddlewareMixin

import datetime
import requests

class StackOverflowMiddleware(MiddlewareMixin):
	# Catch exceptions and retrieve related Stack Overflow results for streamlined troubleshooting
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
	# Prevent users from excessive POST requests (on a per-IP basis)
	def process_request(self, request):
		if request.method == "POST":
			# First check to see that IP address is not locked out
			# due to excessively frequent POST requests (more than 2 comments per minute).
			ip_blocked_post = 'IP_BLOCKED_AT_%s' % request.META.get('REMOTE_ADDR')
			ip_strike_post = cache.get(ip_blocked_post, 0)
			cache.set(ip_blocked_post, ip_strike_post + 1, 60)
			if ip_strike_post > 2:
				raise Exception('Locked out for one minute: Too many POST attempts from this address')
		return None

class DuplicateLimitMiddleware(MiddlewareMixin):
	# Prevent users from creating duplicate posts on the same day (on a per-IP basis)
	def process_request(self, request):
		if request.method == "POST":
			# First check to see that IP address is not locked out
			# due to comment matching existing comment from past 24 hours.
			ip_duplicate = 'DUPLICATE_IP_BLOCKED_AT_%s' % request.META.get('REMOTE_ADDR')
			ip_strike = cache.get(ip_duplicate, 0)
			print('ip strike = ' + str(ip_strike))
			if ip_strike >= 1:
				raise Exception('Locked out for five minutes: Duplicate Comment detected.')
			comment = request.POST['comment']
			try:
				comment_match = Comment.objects.filter(created__gte=datetime.date.today()).filter(comment__exact=comment)
				if comment_match.count() > 0:
					cache.set(ip_duplicate, ip_strike + 1, 300)
					raise Exception('Locked out for five minutes: Duplicate Comment detected.')
				else:
					pass
			except Exception as e:
				print(e)
		return None

