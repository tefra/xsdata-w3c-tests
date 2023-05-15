from output.models.sun_data.attr_decl.ad_scope.ad_scope00101m.ad_scope00101m1_xsd.ad_scope00101m1 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_element=AnyElement(
        qname="{AttrDecl/scope}elementWithAttr",
        text="",
        attributes={
            "{AttrDecl/scope}number": "123",
        }
    )
)
