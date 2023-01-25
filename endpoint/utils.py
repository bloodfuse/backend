from core.models import User
import string
import random

def ran_gen(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def userInfo(u):
    user = User.objects.get(username=u)
    return user


def URL(r):
    h = r.scheme
    p = r.get_host()
    return h+'://'+p
