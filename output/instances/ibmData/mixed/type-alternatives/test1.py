from output.models.ibm_data.mixed.type_alternatives.test1_xsd.test1 import Quadrilateral
from output.models.ibm_data.mixed.type_alternatives.test1_xsd.test1 import Shapes
from output.models.ibm_data.mixed.type_alternatives.test1_xsd.test1 import Triangular


obj = Shapes(
    polygon=[
        Quadrilateral(
            a=10,
            b=10,
            c=10,
            kind="square",
            d=10
        ),
        Quadrilateral(
            a=10,
            b=8,
            c=10,
            kind="rectangle",
            d=8
        ),
        Triangular(
            a=5,
            b=10,
            c=15,
            kind="triangle"
        ),
    ]
)
