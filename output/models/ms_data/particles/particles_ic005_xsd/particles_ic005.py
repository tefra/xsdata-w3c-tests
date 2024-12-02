from dataclasses import dataclass, field

from output.models.ms_data.particles.particles_ic005_xsd.particles_ic005_imp import (
    Base,
)

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Testing(Base):
    class Meta:
        name = "testing"

    e1: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "max_occurs": 5,
        },
    )
    e2: list[object] = field(
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
