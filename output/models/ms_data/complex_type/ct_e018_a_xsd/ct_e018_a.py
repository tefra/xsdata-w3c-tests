from dataclasses import dataclass
from output.models.ms_data.complex_type.ct_e018_a_xsd.ct_e018_b import (
    FooType,
)

__NAMESPACE__ = "a"


@dataclass
class Doc(FooType):
    class Meta:
        name = "doc"
        namespace = "a"
