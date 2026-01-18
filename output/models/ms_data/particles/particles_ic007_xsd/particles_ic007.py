from __future__ import annotations

from dataclasses import dataclass

from output.models.ms_data.particles.particles_ic007_xsd.particles_ic007_imp import (
    Base,
)

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class Testing(Base):
    class Meta:
        name = "testing"


@dataclass(kw_only=True)
class Doc(Testing):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"
