from dataclasses import dataclass
from output.models.ms_data.particles.particles_ic005_xsd.particles_ic005_imp import Base

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Testing(Base):
    class Meta:
        name = "testing"


@dataclass
class Doc(Testing):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"
