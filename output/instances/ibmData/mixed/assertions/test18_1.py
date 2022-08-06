from output.models.ibm_data.mixed.assertions.test18_xsd.test18 import Test
from output.models.ibm_data.mixed.assertions.test18_xsd.test18 import X
from output.models.ibm_data.mixed.assertions.test18_xsd.test18 import Y


obj = Test(
    x=X(
        a=X.A(
            a1=[
                "aaa",
                "aaa..",
            ],
            a_count=2
        ),
        b="world",
        c=None,
        d="world.."
    ),
    y=Y(
        a=Y.A(
            a1=[
                "aaa",
                "aaa..",
            ],
            a_count=2
        ),
        b="world",
        c="hello..",
        d="world.."
    )
)
