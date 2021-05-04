from dataclasses import dataclass
from output.models.ms_data.particles.particles_ic006_xsd.particles_ic006_imp import Base


@dataclass
class Testing(Base):
    class Meta:
        name = "testing"


@dataclass
class Doc(Testing):
    class Meta:
        name = "doc"
