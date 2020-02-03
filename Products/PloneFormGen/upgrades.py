from Products.CMFCore.utils import getToolByName
from Products.PloneFormGen.widgets import AutocompleteStringWidget
from plone import api


def null_upgrade_step(tool):
    """ This is a null upgrade, use it when nothing happens """
    pass

def upgrade_to_170(context):
    #apply the new dependency c.js.jqueryui
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-collective.js.jqueryui:default')

def upgrade_to_171(context):
    # just reload profile
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-Products.PloneFormGen:default')

def upgrade_to_172(context):
    # use autocomplete widget for existing string fields
    brains = api.content.find(portal_type="FormStringField", Language="all")
    for brain in brains:
        fg_string_field = brain.getObject()
        fg_string_field.fgField.widget.__class__ = AutocompleteStringWidget
        fg_string_field.fgField.widget._properties.update({"macro": "widget_autocomplete"})
        fg_string_field.fgField.widget.macro = "widget_autocomplete"
