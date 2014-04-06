from hashlib import md5


class SecretBallotMiddleware(object):
    def process_request(self, request):
        request.secretballot_token = self.generate_token(request)

    def generate_token(self, request):
        raise NotImplementedError


class SecretBallotIpMiddleware(SecretBallotMiddleware):
    def generate_token(self, request):
        return request.META['REMOTE_ADDR']


class SecretBallotIpUseragentMiddleware(SecretBallotMiddleware):
    def generate_token(self, request):
        s = ''.join((request.META['REMOTE_ADDR'], request.META.get('HTTP_USER_AGENT', '')))
        return md5(s).hexdigest()

#see https://github.com/praekelt/django-likes/blob/develop/likes/middleware.py
class SecretBallotIpUseragentAuthMiddleware(SecretBallotMiddleware):
	def generate_token(self, request):
		if request.user.is_authenticated():
			return request.user.username
		else:
			try:
				s = ''.join((request.META['REMOTE_ADDR'], request.META['HTTP_USER_AGENT']))
				return md5(s).hexdigest()
			except KeyError:
				return None
