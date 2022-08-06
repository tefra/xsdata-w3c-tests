from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import A2
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import B2
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    ra=[],
    lab=[],
    la=[],
    uab=[],
    ua=[],
    b_element=[],
    a_element=[],
    b=[],
    a=[],
    item=[
        "abc",
        AnyElement(
            qname="item",
            text="5",
            tail=None,
            children=[],
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "base-A",
            }
        ),
        AnyElement(
            qname="item",
            text="",
            tail=None,
            children=[],
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "base-B",
            }
        ),
        AnyElement(
            qname="item",
            text="1234567890",
            tail=None,
            children=[],
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "base-B",
            }
        ),
        A2(
            value=1
        ),
        A2(
            value=2
        ),
        A2(
            value=3
        ),
        A2(
            value=4
        ),
        B2(
            value="a"
        ),
        B2(
            value="c123456789"
        ),
        B2(
            value="b"
        ),
        AnyElement(
            qname="item",
            text="1",
            tail=None,
            children=[],
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "Union-A",
            }
        ),
        AnyElement(
            qname="item",
            text="4",
            tail=None,
            children=[],
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "Union-A",
            }
        ),
        AnyElement(
            qname="item",
            text="c123456789",
            tail=None,
            children=[],
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "Union-AB",
            }
        ),
        AnyElement(
            qname="item",
            text="4",
            tail=None,
            children=[],
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "Union-AB",
            }
        ),
        AnyElement(
            qname="item",
            text="1 2 3 4",
            tail=None,
            children=[],
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "List-AB",
            }
        ),
        AnyElement(
            qname="item",
            text="1 c123456789 b 4",
            tail=None,
            children=[],
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "List-AB",
            }
        ),
        AnyElement(
            qname="item",
            text="1",
            tail=None,
            children=[],
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "R-A",
            }
        ),
        AnyElement(
            qname="item",
            text="2",
            tail=None,
            children=[],
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "R-A",
            }
        ),
    ]
)
