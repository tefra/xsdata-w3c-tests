from output.models.ms_data.complex_type.ct_l011_xsd.ct_l011 import FooTest
from output.models.ms_data.complex_type.ct_l011_xsd.ct_l011 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    foo_test=FooTest(
        content=[
            "&#10;&#9;mixed content&#10;&#9;",
            AnyElement(
                qname="child_1",
                text="info",
                tail=None,
                children=[],
                attributes={}
            ),
            AnyElement(
                qname="child_2",
                text="3",
                tail=None,
                children=[],
                attributes={}
            ),
        ]
    )
)
