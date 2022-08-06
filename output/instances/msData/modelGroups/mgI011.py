from output.models.ms_data.model_groups.mg_i011_xsd.mg_i011 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    choice=[
        AnyElement(
            qname="{http://www.w3.org/1999/xhtml}html",
            text="",
            tail=None,
            children=[
                AnyElement(
                    qname="{http://www.w3.org/1999/xhtml}body",
                    text="&#10;Hey this is html&#10;",
                    tail=None,
                    children=[],
                    attributes={}
                ),
            ],
            attributes={}
        ),
    ],
    c=None
)
