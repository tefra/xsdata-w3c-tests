from output.models.ms_data.element.elem_s002_xsd.elem_s002 import Fr1Valid
from output.models.ms_data.element.elem_s002_xsd.elem_s002 import Root


obj = Root(
    fr1_valid_or_fr_valid=Fr1Valid(
        value="abc",
        a=None,
        b="123"
    )
)
