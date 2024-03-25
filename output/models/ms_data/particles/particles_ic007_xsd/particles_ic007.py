from dataclasses import dataclass, field
from typing import List

from output.models.ms_data.particles.particles_ic007_xsd.particles_ic007_imp import (
    Base,
)

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Testing(Base):
    class Meta:
        name = "testing"

    e1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "max_occurs": 5,
        },
    )
    e2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "max_occurs": 5,
        },
    )


@dataclass
class Doc(Testing):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"
