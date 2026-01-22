from output.models.ibm_data.valid.d3_4_26.d3_4_26v03_xsd.d3_4_26v03 import Root
from xsdata.models.datatype import XmlDuration


obj = Root(
    ely_mdunion_a=[
        'Computer',
        XmlDuration("P12Y34M"),
    ],
    ely_mdunion_b=[
        XmlDuration("-P45Y23M"),
        7,
    ],
    ely_mdunion_c=[
        XmlDuration("P35Y3M"),
        1,
        'once',
    ]
)
