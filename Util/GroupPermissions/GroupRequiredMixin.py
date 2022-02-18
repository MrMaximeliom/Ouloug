from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import ImproperlyConfigured
class GroupRequiredMixin(AccessMixin):
    """Verify that the current user has all specified permissions."""
    groups_required = None

    def get_group_required(self):
        """
        Override this method to override the permission_required attribute.
        Must return an iterable.
        """
        if self.groups_required is None:
            raise ImproperlyConfigured(
                '{0} is missing the groups_required attribute. Define {0}.groups_required, or override '
                '{0}.get_groups_required().'.format(self.__class__.__name__)
            )
        if isinstance(self.groups_required, str):
            groups = (self.groups_required,)
        else:
            groups = self.groups_required
        return groups

    def has_permission(self):
        """
        Override this method to customize the way permissions are checked.
        """
        groups = self.get_group_required()
        user_groups = self.request.user.groups.values('name')
        for group in groups:
            for user_group in user_groups:
                if user_group['name'] == group:
                    return True


    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)