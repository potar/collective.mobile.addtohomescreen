""" Module dedicated for views """

import json
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from zope.component import getMultiAdapter

from collective.mobile.addtohomescreen.utils import get_config_setting

def lchop(s, start):
    length = len(start)
    if s[:length] == start:
        return s[length:]
    return s


class AddToHomeScreenAllowed(BrowserView):
    """ Class dedicated to enable/disable javascript
       (add2homeloader.js) and css styles on the page.
    """
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def getCurrentPaths(self):
        portal_url = getToolByName(self.context, 'portal_url')
        obj_path = portal_url.getRelativeUrl(self.context)
        browser_path = lchop(self.request.ACTUAL_URL, portal_url())
        return ['/' + obj_path, browser_path]

    def isUrlAllowed(self):
        allowed_url_paths = get_config_setting('allowed_url_paths')
        if allowed_url_paths: 
            obj_path, browser_path = self.getCurrentPaths()
            return (obj_path in allowed_url_paths) or \
                (browser_path in allowed_url_paths) 
        else: 
            return getMultiAdapter(
                (self.context, self.request), 
                name='plone_context_state').is_portal_root()

    def __call__(self):
        return self.isUrlAllowed()


class AddToHomeScreenSettings(BrowserView):
    """ It forms settings which refer to the popup window """

    def javascriptvars(self):
        """ It overlaps settings which was set up by static/add2home.js """
        return "var addToHomeConfig = %s" % json.dumps(
                   {
                       # Show the message only to returning visitors 
                       # (ie: don't show it the first time)
                       'returningVisitor': True,     
                       'message': get_config_setting('message'),
                       # Show the message only once every 12 hours
                       'expire': 720            
                   }
        )


    def __call__(self):
        self.request.response.setHeader('content-type', 'text/javascript;;charset=utf-8')
        return self.javascriptvars()
