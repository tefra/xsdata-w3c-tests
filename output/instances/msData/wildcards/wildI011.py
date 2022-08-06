from output.models.ms_data.wildcards.wild_i011_xsd.wild_i011 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    other_element=AnyElement(
        qname=None,
        text=None,
        tail=None,
        children=[
            AnyElement(
                qname="{A}b",
                text="test",
                tail=None,
                children=[],
                attributes={}
            ),
            AnyElement(
                qname="{A}b",
                text="test",
                tail=None,
                children=[],
                attributes={}
            ),
        ],
        attributes={}
    ),
    a_element=None
)
