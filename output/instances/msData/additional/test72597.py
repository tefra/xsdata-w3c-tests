from output.models.ms_data.additional.test72597_xsd.test72597 import A
from output.models.ms_data.additional.test72597_xsd.test72597 import Root


obj = Root(
    a=A(
        part=[
            A.Part(
                value="",
                number=1,
                number2=2
            ),
            A.Part(
                value="",
                number=2,
                number2=1
            ),
        ]
    )
)
