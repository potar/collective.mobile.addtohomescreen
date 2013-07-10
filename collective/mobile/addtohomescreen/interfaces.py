""" Module dedicated for interfaces """

from zope import schema
from zope.interface import Interface


class IAddToHomeScreenSettings(Interface):
    """ Settings for javascript (add2homeloader.js)
    """
    allowed_url_paths = schema.List(
        title=u"Allowed url paths",
        description=u"Enter the list of url paths where you want "
                     "add2homeloader.js and add2home.css turned on." 
                     "Eg: /front-page",
        default=[],
        value_type=schema.TextLine(title=u"Allowed urls path")
    )

    message = schema.Text(
        title=u'The popup window message',
        description=u"Enter the message which will be displayed "
                     "on the popup window.",
        default=u'',
    )
