from dataclasses import dataclass, field
from typing import Optional
from output.models.ms_data.particles.particles_ic007_xsd.particles_ic007_imp import Base

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Testing(Base):
    class Meta:
        name = "testing"

    e1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "required": True,
        }
    )
    e2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "required": True,
        }
    )


@dataclass
class Doc(Testing):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"
