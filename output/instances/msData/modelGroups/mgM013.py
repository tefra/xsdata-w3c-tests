from output.models.ms_data.model_groups.mg_m013_xsd.mg_m013 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    any_element=AnyElement(
        children=[
            AnyElement(
                qname="foo",
                text="",
                children=[
                    AnyElement(
                        qname="e1",
                        text=""
                    ),
                    AnyElement(
                        qname="e2",
                        text=""
                    ),
                ]
            ),
            AnyElement(
                qname="global",
                text=""
            ),
        ]
    )
)
