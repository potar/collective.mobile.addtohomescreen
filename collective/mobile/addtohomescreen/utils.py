""" It provides utils """
from zope.component import getUtility
from plone.registry.interfaces import IRegistry

from collective.mobile.addtohomescreen.interfaces import \
                                                  IAddToHomeScreenSettings


def get_add2homescreen_settings(check=False):
    """ It gets settings from the plone registry """
    registry = getUtility(IRegistry)
    # if you want to omit KeyError set 'check=False'
    return registry.forInterface(IAddToHomeScreenSettings, check=check)


def get_config_setting(fieldname):
    settings = get_add2homescreen_settings()
    value = getattr(settings, fieldname)
    if value == settings.__schema__[fieldname].missing_value:
        value = settings.__schema__[fieldname].default
    return value
