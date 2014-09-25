from zope import component
from collective.inplacetopicview import portlets

def setupContentPortletLocalAdapter(context):
    """ """
    sm = component.getSiteManager(context)
    sm.registerAdapter(portlets.ContentContextAcquisition)

def unregisterContentPortletLocalAdapter(context):
    sm = component.getSiteManager(context)
    sm.unregisterAdapter(portlets.ContentContextAcquisition)
