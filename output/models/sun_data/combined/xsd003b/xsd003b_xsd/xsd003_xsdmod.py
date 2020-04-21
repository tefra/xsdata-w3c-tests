from dataclasses import dataclass
from output.models.sun_data.combined.xsd003b.xsd003b_xsd.xsd003b import (
    ComplexType,
)

__NAMESPACE__ = "foo"


@dataclass
class Root(ComplexType):
    class Meta:
        name = "root"
        namespace = "foo"
