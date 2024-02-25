from output.models.ms_data.model_groups.mg_d009_xsd.mg_d009 import Root
from output.models.ms_data.model_groups.mg_d009_xsd.mg_d009 import Test
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    a_or_b=Test.A(
        content=AnyElement(
            text='test'
        )
    )
)
