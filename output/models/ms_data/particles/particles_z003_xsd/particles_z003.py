from dataclasses import dataclass, field
from typing import Optional
from output.models.ms_data.particles.particles_z003_xsd.particles_z003_imp import (
    Foo,
)

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    """
    :ivar foo:
    """
    foo: Optional[Foo] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="importedXSD",
            required=True
        )
    )


@dataclass
class Doc(B):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"