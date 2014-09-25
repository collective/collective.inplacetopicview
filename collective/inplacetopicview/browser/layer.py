from plone.theme.interfaces import IDefaultPloneLayer

class IAcquisitionAwareLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
    
    This layer make Plone UI acquisition aware:
    
    * Bread crumb (path_bar)
    """
