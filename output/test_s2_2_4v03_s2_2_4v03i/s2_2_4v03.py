from output.models.ibm_data.valid.s2_2_4.s2_2_4v03_xsd.s2_2_4v03 import Root
from output.models.ibm_data.valid.s2_2_4.s2_2_4v03_xsd.s2_2_4v03 import T0
from output.models.ibm_data.valid.s2_2_4.s2_2_4v03_xsd.s2_2_4v03 import T1


obj = Root(
    hi1=T0(
        e1=[
            T1(
                a1=0
            ),
            T1(
                a1=1,
                a2=1
            ),
        ],
        e2=[
            T1(
                a1=0,
                a2=0
            ),
            T1(
                a1=1,
                a2=1
            ),
        ]
    ),
    hi2=T0(
        e1=[
            T1(
                a1=0
            ),
            T1(
                a1=1,
                a2=1
            ),
        ],
        e2=[
            T1(
                a1=0,
                a2=0
            ),
            T1(
                a1=1,
                a2=1
            ),
        ]
    )
)
