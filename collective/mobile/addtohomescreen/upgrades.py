import logging

logger = logging.getLogger(__name__)
default_profile = 'profile-collective.mobile.addtohomescreen:default'


def upgrade_1000_to_1001(context):
    logger.info("Upgrade the plone registry")
    context.runImportStepFromProfile(default_profile, 'plone.app.registry')
