from output.models.sun_data.combined.xsd008.xsd008_xsd.xsd008 import Generic
from output.models.sun_data.combined.xsd008.xsd008_xsd.xsd008 import Int
from output.models.sun_data.combined.xsd008.xsd008_xsd.xsd008 import Long
from output.models.sun_data.combined.xsd008.xsd008_xsd.xsd008 import Root
from output.models.sun_data.combined.xsd008.xsd008_xsd.xsd008 import YesNo


obj = Root(
    generic=Generic(
        choice=[
            YesNo(
                value=True
            ),
            YesNo(
                value=False
            ),
            Long(
                value=52
            ),
            Long(
                value=-55555
            ),
            Int(
                value=52
            ),
            Int(
                value=-55555
            ),
        ]
    ),
    restricted=Root.Restricted(
        int_or_long=[
            Long(
                value=52
            ),
            Long(
                value=-55555
            ),
            Int(
                value=52
            ),
            Int(
                value=-55555
            ),
        ]
    )
)
