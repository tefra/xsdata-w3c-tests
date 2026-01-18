from __future__ import annotations

from dataclasses import dataclass

from output.models.ms_data.particles.particles_ic006_xsd.particles_ic006_imp import (
    Base,
)


@dataclass(kw_only=True)
class Testing(Base):
    class Meta:
        name = "testing"


@dataclass(kw_only=True)
class Doc(Testing):
    class Meta:
        name = "doc"
