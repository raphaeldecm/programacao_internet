from django.core.exceptions import PermissionDenied


def user_editor(user):
  if user.groups.filter(name='Editor').exists():
    return True
  raise PermissionDenied