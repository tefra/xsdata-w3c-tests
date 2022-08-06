from output.models.ms_data.simple_type.st_g004_xsd.st_g004 import MyUnionValue
from output.models.ms_data.simple_type.st_g004_xsd.st_g004 import Root


obj = Root(
    foo_test=[
        12,
        66,
        MyUnionValue.WA,
        MyUnionValue.OR,
    ]
)
