from django.contrib.staticfiles.storage import ManifestFilesMixin
from storages.backends.s3boto import S3BotoStorage

class CachedS3Storage(ManifestFilesMixin, S3BotoStorage):
    pass
