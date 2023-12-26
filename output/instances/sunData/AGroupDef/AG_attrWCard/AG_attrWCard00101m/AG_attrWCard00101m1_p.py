from output.models.sun_data.agroup_def.ag_attr_wcard.ag_attr_wcard00101m.ag_attr_wcard00101m1_xsd.ag_attr_wcard00101m1 import ElementWithAttr
from output.models.sun_data.agroup_def.ag_attr_wcard.ag_attr_wcard00101m.ag_attr_wcard00101m1_xsd.ag_attr_wcard00101m1 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_element=AnyElement(
        children=[
            ElementWithAttr(
                number=157
            ),
            ElementWithAttr(
                any_attributes={
                    'notDefined': 'wood',
                }
            ),
        ]
    )
)
