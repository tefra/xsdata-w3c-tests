from output.models.ibm_data.mixed.assertions.test17_xsd.test17 import Test
from output.models.ibm_data.mixed.assertions.test17_xsd.test17 import X
from output.models.ibm_data.mixed.assertions.test17_xsd.test17 import Y


obj = Test(
    x=X(
        a="hello",
        b="world",
        c=None,
        d="world.."
    ),
    y=Y(
        a="hello",
        b="world",
        c="hello..",
        d="world.."
    )
)
