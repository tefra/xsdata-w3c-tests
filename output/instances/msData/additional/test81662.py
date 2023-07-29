from output.models.ms_data.additional.test81662_xsd.test81662 import Ct1
from output.models.ms_data.additional.test81662_xsd.test81662 import Ct2
from output.models.ms_data.additional.test81662_xsd.test81662 import Ct3
from output.models.ms_data.additional.test81662_xsd.test81662 import Ct4
from output.models.ms_data.additional.test81662_xsd.test81662 import Ct5
from output.models.ms_data.additional.test81662_xsd.test81662 import Ct6
from output.models.ms_data.additional.test81662_xsd.test81662 import Element1
from output.models.ms_data.additional.test81662_xsd.test81662 import Test


obj = Test(
    e1=[
        Ct1(
            any_element=Element1(

            ),
            element1=Element1(

            )
        ),
    ],
    e2=[
        Ct2(
            element1=Element1(

            ),
            any_element=Element1(

            )
        ),
    ],
    e3=[
        Ct3(
            element1_or_any_element=[
                Element1(

                ),
                Element1(

                ),
                Element1(

                ),
            ]
        ),
    ],
    e4=[
        Ct4(
            any_element_or_element1=[
                Element1(

                ),
                Element1(

                ),
                Element1(

                ),
            ]
        ),
    ],
    e5=[
        Ct5(
            element1=Element1(

            ),
            any_element=[
                Element1(

                ),
                Element1(

                ),
            ]
        ),
    ],
    e6=[
        Ct6(
            element1=Element1(

            ),
            any_element=[
                Element1(

                ),
                Element1(

                ),
            ]
        ),
    ]
)
