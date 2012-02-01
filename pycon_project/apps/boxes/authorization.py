from django.conf import settings

from boxes.utils import load_path_attr


def default_can_edit(request, *args, **kwargs):
    """
    This is meant to be overridden in your project per domain specific
    requirements.
    """
    return request.user.is_staff


def load_can_edit():
    import_path = getattr(settings, "BOXES_CAN_EDIT_CALLABLE", None)
    
    if import_path is None:
        return default_can_edit
    
    return load_path_attr(import_path)
