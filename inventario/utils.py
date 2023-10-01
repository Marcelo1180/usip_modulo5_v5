from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied


def permission_required(perm):
    def check_perms(user):
        if user.has_perms(perm) or user.is_superuser:
        # if user.has_perms(perm):
            return True
        else:
            raise PermissionDenied

    return user_passes_test(check_perms)
