from output.models.ms_data.additional.test81662_xsd.test81662 import Ct1
from output.models.ms_data.additional.test81662_xsd.test81662 import Ct2
from output.models.ms_data.additional.test81662_xsd.test81662 import Ct3
from output.models.ms_data.additional.test81662_xsd.test81662 import Ct4
from output.models.ms_data.additional.test81662_xsd.test81662 import Ct5
from output.models.ms_data.additional.test81662_xsd.test81662 import Ct6
from output.models.ms_data.additional.test81662_xsd.test81662 import Test
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Test(
    e1=[
        Ct1(
            any_element=AnyElement(
                qname="element1",
                text=""
            ),
            element1=""
        ),
    ],
    e2=[
        Ct2(
            element1="",
            any_element=AnyElement(
                qname="element1",
                text=""
            )
        ),
    ],
    e3=[
        Ct3(
            element1_or_any_element=[
                AnyElement(
                    qname="element1",
                    text=""
                ),
                AnyElement(
                    qname="element1",
                    text=""
                ),
                AnyElement(
                    qname="element1",
                    text=""
                ),
            ]
        ),
    ],
    e4=[
        Ct4(
            any_element_or_element1=[
                AnyElement(
                    qname="element1",
                    text=""
                ),
                AnyElement(
                    qname="element1",
                    text=""
                ),
                AnyElement(
                    qname="element1",
                    text=""
                ),
            ]
        ),
    ],
    e5=[
        Ct5(
            element1="",
            any_element=[
                AnyElement(
                    qname="element1",
                    text=""
                ),
                AnyElement(
                    qname="element1",
                    text=""
                ),
            ]
        ),
    ],
    e6=[
        Ct6(
            element1="",
            any_element=[
                AnyElement(
                    qname="element1",
                    text=""
                ),
                AnyElement(
                    qname="element1",
                    text=""
                ),
            ]
        ),
    ]
)
