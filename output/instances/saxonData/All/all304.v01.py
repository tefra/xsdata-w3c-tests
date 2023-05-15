from output.models.saxon_data.all.all304_xsd.all304 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    one_com_element=[
        AnyElement(
            qname="{http://one.com/}one",
            text=""
        ),
        AnyElement(
            qname="{http://one.com/}three",
            text=""
        ),
    ],
    two_com_element=[
        AnyElement(
            qname="{http://two.com/}two",
            text=""
        ),
        AnyElement(
            qname="{http://two.com/}four",
            text=""
        ),
    ]
)
