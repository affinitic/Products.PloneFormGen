from Products.Archetypes.Widget import StringWidget
from Products.Archetypes.Registry import registerWidget


class AutocompleteStringWidget(StringWidget):
    """This widget displays string field with autocomplete attribute.
    """

    # Use the base class properties, and add our own
    _properties = StringWidget._properties.copy()
    _properties.update({"macro": "widget_autocomplete"})


# Register the widget with Archetypes
registerWidget(
    AutocompleteStringWidget,
    title="Autocomplete String widget",
    description=("Renders string field with autocomplete attribute",),
    used_for=("Products.Archetypes.Field.StringField",),
)
