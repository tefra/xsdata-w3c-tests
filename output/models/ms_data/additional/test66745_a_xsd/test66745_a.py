from dataclasses import dataclass, field
from typing import Optional
from output.models.ms_data.additional.test66745_a_xsd.test66745_b import Foo

__NAMESPACE__ = "foo1"


@dataclass
class Foo1(Foo):
    class Meta:
        name = "foo1"
        namespace = "foo1"

    x: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
