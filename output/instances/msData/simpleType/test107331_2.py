from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import A1
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import B1
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import Item
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import RA1
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import Root
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import UnionA
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import UnionAb
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    choice=[
        Item(
            value="abc"
        ),
        5,
        10,
        1,
        "",
        "1234567890",
        DerivedElement(
            qname="a",
            value=A1.VALUE_1
        ),
        DerivedElement(
            qname="a",
            value=A1.VALUE_2
        ),
        DerivedElement(
            qname="a",
            value=A1.VALUE_3
        ),
        DerivedElement(
            qname="a",
            value=A1.VALUE_4
        ),
        B1.A,
        B1.C123456789,
        B1.B,
        UnionA.VALUE_1,
        UnionA.VALUE_4,
        DerivedElement(
            qname="uab",
            value=UnionAb.C123456789
        ),
        DerivedElement(
            qname="uab",
            value=UnionAb.VALUE_4
        ),
        [
            A1.VALUE_1,
            A1.VALUE_2,
            A1.VALUE_3,
            A1.VALUE_4,
        ],
        [
            UnionAb.VALUE_1,
            UnionAb.C123456789,
            UnionAb.B,
            UnionAb.VALUE_4,
        ],
        RA1.VALUE_2,
        RA1.VALUE_1,
    ]
)
