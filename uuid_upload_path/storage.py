from __future__ import absolute_import, unicode_literals

import posixpath

from uuid_upload_path.uuid import uuid
from django.utils.deconstruct import deconstructible


@deconstructible
class upload_to_factory(object):
    """
    An upload path generator that uses compact UUIDs for filenames.
    """

    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, instance, filename):
        name, ext = posixpath.splitext(filename)
        return posixpath.join(self.prefix, uuid() + ext)

def upload_to(instance, filename):
    """
    An upload path generator that generates an upload prefix based
    on the instance model name, and uses a compact UUID for the filename.
    """
    opts = instance._meta
    return upload_to_factory(posixpath.join(
        opts.app_label,
        instance.__class__.__name__.lower(),
    ))(instance, filename)
