from output.models.saxon_data.all.all304_xsd.all304 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    a=[],
    b=[],
    c=[],
    one_com_element=[
        AnyElement(
            qname="{http://one.com/}one",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{http://one.com/}three",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
    ],
    e=None,
    f=[],
    two_com_element=[
        AnyElement(
            qname="{http://two.com/}two",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{http://two.com/}four",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
    ]
)
