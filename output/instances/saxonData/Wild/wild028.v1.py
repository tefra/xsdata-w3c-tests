from output.models.saxon_data.wild.wild028_xsd.wild028 import Eden
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Eden(
    any_element=[
        AnyElement(
            qname="adam",
            text="m",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{http://devil.com/}eve",
            text="f",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{http://genesis.com/}cain",
            text="m",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{http://genesis.com/}abel",
            text="m",
            tail=None,
            children=[],
            attributes={}
        ),
    ]
)
