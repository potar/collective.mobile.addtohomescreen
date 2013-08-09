""" It provides utils """
from zope.component import getUtility
from plone.registry.interfaces import IRegistry

from collective.mobile.addtohomescreen.interfaces import \
                                                  IAddToHomeScreenSettings


def get_add2homescreen_settings():
    """ It gets settings from the plone registry """
    registry = getUtility(IRegistry)
    field_names = IAddToHomeScreenSettings.names()
    try:
        screen_settings = registry.forInterface(IAddToHomeScreenSettings)
        convert_settings = (
            (name, getattr(screen_settings, name))
            for name in field_names
        )
    # it happens when we add a new field into the schema
    except KeyError:
        # set default settings
        convert_settings = (
            (name, IAddToHomeScreenSettings.get(name).default)
             for name in field_names
        )
    return dict(convert_settings)
