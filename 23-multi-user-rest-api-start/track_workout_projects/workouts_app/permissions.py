from rest_framework.permissions import IsAuthenticated

class IsOwnerOfResourceOrReadOnly(IsAuthenticated):
    """
    Custom permission to only allow owners of an object to edit it.
    Is order for this to work, the model instance need to 
    have a 'user' attribute
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we will always allow GET, HEAD, or OPTIONS requests.
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return (obj.user == request.user) or (obj.user is None)