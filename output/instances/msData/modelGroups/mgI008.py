from output.models.ms_data.model_groups.mg_i008_xsd.mg_i008 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    w3_org_1999_xhtml_element=[
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
    ]
)