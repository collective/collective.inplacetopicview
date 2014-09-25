from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import utils
from plone.app.layout.viewlets.common import PathBarViewlet
from Products.CMFCore.interfaces._content import ISiteRoot
from plone.app.layout.navigation.interfaces import INavigationRoot

class AcquisitionBarViewlet(PathBarViewlet):
    """This is a path bar viewlet aware of the acquisition chain
    
    Lets say you have :
    A / B
    A / C
    
    You display C throw B: A / B / C
    Default plone path bar will display A/C
    
    This one will display A / B / C

    You also can exclude from the bar some relative path if you want throw the
    portal_properties.site_properties by adding path_not_to_list lines property
    For example add B's id to this list and the bar will display A / C

    """
    index = PathBarViewlet.index

    def update(self):
        super(AcquisitionBarViewlet, self).update()

        chain = self.getAcquisitionChain()

        pp = getToolByName(self.context, 'portal_properties').site_properties
        urltool = getToolByName(self.context, 'portal_url')

        url_not_to_list = [urltool() + '/' + path\
                           for path in getattr(pp,'path_not_to_list', [])]
        
        self.breadcrumbs = []
        for ob in chain:
            if utils.isDefaultPage(ob,self.request, self.context):continue
            url = ob.absolute_url()
            if url in url_not_to_list:continue
            self.breadcrumbs.append({'absolute_url':ob.absolute_url(),
                             'Title':ob.Title()})
        self.breadcrumbs.reverse()
        self.breadcrumbs.pop(0) #remove the first because its the root


    def getAcquisitionChain(self):
        """
        @return: List of objects from context, its parents to the portal root
    
        Example::
    
            chain = getAcquisitionChain(self.context)
            print "I will look up objects:" + str(list(chain))
    
        @param object: Any content object
        @return: Iterable of all parents from the direct parent to the site root
        """
        object = self.context
        # It is important to use inner to bootstrap the traverse,
        # or otherwise we might get surprising parents
        # E.g. the context of the view has the view as the parent
        # unless inner is used
        inner = object.aq_inner
    
        iter = inner
    
        while iter is not None:
            # if iter => return False if iter is an empty ATBTreeFolder!
            
            yield iter
    
            if ISiteRoot.providedBy(iter) or INavigationRoot.providedBy(iter):
               break
    
            if not hasattr(iter, "aq_parent"):
                raise RuntimeError("Parent traversing interrupted by object: " + str(parent))
    
            iter = iter.aq_parent