from output.models.ms_data.model_groups.mg_f015_xsd.mg_f015 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    one="",
    two="",
    three="",
    four="",
    five_or_five2=[
        AnyElement(
            qname="five",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
    ],
    six_or_six2=[
        AnyElement(
            qname="six",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
    ],
    seven_or_seven2=[
        AnyElement(
            qname="seven",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
    ],
    eight_or_eight2=[
        AnyElement(
            qname="eight",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
    ]
)
