# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 : */

from django.utils.translation import ugettext_lazy as _
from django.db import models

from openid_provider.conf import AUTH_USER_MODEL
from openid_provider.utils import get_username

class OpenID(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL)
    openid = models.CharField(max_length=200, blank=True, unique=True)
    default = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('OpenID')
        verbose_name_plural = _('OpenIDs')
        ordering = ['openid']

    def __unicode__(self):
        return u"%s|%s" % (get_username(self.user), self.openid)

    def save(self, *args, **kwargs):
        if self.openid in ['', u'', None]:
            from hashlib import sha1
            import random, base64
            sha = sha1()
            sha.update(unicode(get_username(self.user)).encode('utf-8'))
            sha.update(str(random.random()))
            value = str(base64.b64encode(sha.digest()))
            value = value.replace('/', '').replace('+', '').replace('=', '')
            self.openid = value
        super(OpenID, self).save(*args, **kwargs)
        if self.default:
            self.user.openid_set.exclude(pk=self.pk).update(default=False)

class TrustedRoot(models.Model):
    openid = models.ForeignKey(OpenID)
    trust_root = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.trust_root)
