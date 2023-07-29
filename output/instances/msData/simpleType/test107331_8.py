from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import A2
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import B2
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import Item
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import Root
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    choice=[
        Item(
            value="abc"
        ),
        Item(
            value="5"
        ),
        Item(

        ),
        Item(
            value="1234567890"
        ),
        DerivedElement(
            qname="item",
            value=A2(
                value=1
            ),
            type="A"
        ),
        DerivedElement(
            qname="item",
            value=A2(
                value=2
            ),
            type="A"
        ),
        DerivedElement(
            qname="item",
            value=A2(
                value=3
            ),
            type="A"
        ),
        DerivedElement(
            qname="item",
            value=A2(
                value=4
            ),
            type="A"
        ),
        DerivedElement(
            qname="item",
            value=B2(
                value="a"
            ),
            type="B"
        ),
        DerivedElement(
            qname="item",
            value=B2(
                value="c123456789"
            ),
            type="B"
        ),
        DerivedElement(
            qname="item",
            value=B2(
                value="b"
            ),
            type="B"
        ),
        Item(
            value="1"
        ),
        Item(
            value="4"
        ),
        Item(
            value="c123456789"
        ),
        Item(
            value="4"
        ),
        Item(
            value="1 2 3 4"
        ),
        Item(
            value="1 c123456789 b 4"
        ),
        Item(
            value="1"
        ),
        Item(
            value="2"
        ),
    ]
)
