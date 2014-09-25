"""Here we want to change the behaviour of portlet rendering process.

We want to be acquisition aware:

If you have A/B and A/C and do A/B/C, on a default plone,
portlet rendering process take parents from A only.

This module change that behaviour to first render portlets from C, then B then A
"""


from plone.app.portlets.portletcontext import ContentContext
from Acquisition import aq_parent, aq_inner, aq_base
from zope import component
from zope import interface

class ContentContextAcquisition(ContentContext):
    """Override the default plone.app.portlets ContentContext"""
    #implements and adapts already done in ContentContext

    def getParent(self):
        """getParent respecting the acquisition chain.
        
        This code is recursive
        """
        parent = aq_parent(aq_inner(self.context))
        request = getattr(self.context, 'REQUEST', None)
        if request:
            try:
                url = request.URL
                first_parent = request.PARENTS[0]
                if self.context.UID() != first_parent.UID():
                    parent = aq_parent(self.context)
            except AttributeError:
                # AttributeError: UID
                pass
        return parent
