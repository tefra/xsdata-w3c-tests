from output.models.sun_data.combined.xsd008.xsd008_xsd.xsd008 import Generic
from output.models.sun_data.combined.xsd008.xsd008_xsd.xsd008 import Int
from output.models.sun_data.combined.xsd008.xsd008_xsd.xsd008 import Long
from output.models.sun_data.combined.xsd008.xsd008_xsd.xsd008 import Root
from output.models.sun_data.combined.xsd008.xsd008_xsd.xsd008 import YesNo


obj = Root(
    generic=Generic(
        choice=[
            YesNo(
                annotation=None,
                value=True
            ),
            YesNo(
                annotation=None,
                value=False
            ),
            Long(
                annotation=None,
                value=52
            ),
            Long(
                annotation=None,
                value=-55555
            ),
            Int(
                annotation=None,
                value=52
            ),
            Int(
                annotation=None,
                value=-55555
            ),
        ]
    ),
    restricted=Root.Restricted(
        int_or_long=[
            Long(
                annotation=None,
                value=52
            ),
            Long(
                annotation=None,
                value=-55555
            ),
            Int(
                annotation=None,
                value=52
            ),
            Int(
                annotation=None,
                value=-55555
            ),
        ]
    )
)
