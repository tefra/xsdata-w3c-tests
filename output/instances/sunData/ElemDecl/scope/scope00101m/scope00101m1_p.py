from output.models.sun_data.elem_decl.scope.scope00101m.scope00101m_xsd.scope00101m import Global
from output.models.sun_data.elem_decl.scope.scope00101m.scope00101m_xsd.scope00101m import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    global_value=Global(
        any_element=AnyElement(
            text="1"
        )
    ),
    local="2"
)
