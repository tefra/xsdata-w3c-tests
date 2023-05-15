from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import A2
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import B2
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import Root
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    choice=[
        AnyElement(
            qname="item",
            text="abc"
        ),
        AnyElement(
            qname="item",
            text="5",
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "base-A",
            }
        ),
        AnyElement(
            qname="item",
            text="",
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "base-B",
            }
        ),
        AnyElement(
            qname="item",
            text="1234567890",
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "base-B",
            }
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
        AnyElement(
            qname="item",
            text="1",
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "Union-A",
            }
        ),
        AnyElement(
            qname="item",
            text="4",
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "Union-A",
            }
        ),
        AnyElement(
            qname="item",
            text="c123456789",
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "Union-AB",
            }
        ),
        AnyElement(
            qname="item",
            text="4",
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "Union-AB",
            }
        ),
        AnyElement(
            qname="item",
            text="1 2 3 4",
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "List-AB",
            }
        ),
        AnyElement(
            qname="item",
            text="1 c123456789 b 4",
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "List-AB",
            }
        ),
        AnyElement(
            qname="item",
            text="1",
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "R-A",
            }
        ),
        AnyElement(
            qname="item",
            text="2",
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "R-A",
            }
        ),
    ]
)
