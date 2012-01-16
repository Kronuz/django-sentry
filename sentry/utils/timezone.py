"""
sentry.utils.timezone
~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2012 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

try:
    from django.utils import timezone
    utc = timezone.utc
    now = timezone.now
    is_naive = timezone.is_naive
    is_aware = timezone.is_aware
    make_naive = timezone.make_naive
    make_aware = timezone.make_aware
except ImportError:
    from datetime import datetime
    utc = None
    now = datetime.now
    is_naive = is_aware = lambda x: False
    make_naive = make_aware = lambda x, y: x
