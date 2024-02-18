from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import A1
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import A2
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import A3
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import B1
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import B2
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import B3
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import Item
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import La
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import Lab
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import RA1
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import Ra
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import Root
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import Ua
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import Uab
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import UnionA
from output.models.ms_data.simple_type.test107331_c_xsd.test107331_c import UnionAb


obj = Root(
    choice=[
        Item(
            value='abc'
        ),
        A2(
            value=5
        ),
        A2(
            value=10
        ),
        A2(
            value=1
        ),
        B2(

        ),
        B2(
            value='1234567890'
        ),
        A3(
            value=A1.VALUE_1
        ),
        A3(
            value=A1.VALUE_2
        ),
        A3(
            value=A1.VALUE_3
        ),
        A3(
            value=A1.VALUE_4
        ),
        B3(
            value=B1.A
        ),
        B3(
            value=B1.C123456789
        ),
        B3(
            value=B1.B
        ),
        Ua(
            value=UnionA.VALUE_1
        ),
        Ua(
            value=UnionA.VALUE_4
        ),
        Uab(
            value=UnionAb.C123456789
        ),
        Uab(
            value=UnionAb.VALUE_4
        ),
        La(
            value=[
                A1.VALUE_1,
                A1.VALUE_2,
                A1.VALUE_3,
                A1.VALUE_4,
            ]
        ),
        Lab(
            value=[
                UnionAb.VALUE_1,
                UnionAb.C123456789,
                UnionAb.B,
                UnionAb.VALUE_4,
            ]
        ),
        Ra(
            value=RA1.VALUE_2
        ),
        Ra(
            value=RA1.VALUE_1
        ),
    ]
)
