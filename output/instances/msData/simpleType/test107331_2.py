from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import A1
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import B1
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import RA1
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import Root
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import UnionA
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import UnionAb


obj = Root(
    ra=[
        RA1.VALUE_2,
        RA1.VALUE_1,
    ],
    lab=[
        [
            UnionAb.VALUE_1,
            UnionAb.C123456789,
            UnionAb.B,
            UnionAb.VALUE_4,
        ],
    ],
    la=[
        [
            A1.VALUE_1,
            A1.VALUE_2,
            A1.VALUE_3,
            A1.VALUE_4,
        ],
    ],
    uab=[
        UnionAb.C123456789,
        UnionAb.VALUE_4,
    ],
    ua=[
        UnionA.VALUE_1,
        UnionA.VALUE_4,
    ],
    b_element=[
        B1.A,
        B1.C123456789,
        B1.B,
    ],
    a_element=[
        A1.VALUE_1,
        A1.VALUE_2,
        A1.VALUE_3,
        A1.VALUE_4,
    ],
    b=[
        "",
        "1234567890",
    ],
    a=[
        5,
        10,
        1,
    ],
    item=[
        "abc",
    ]
)
