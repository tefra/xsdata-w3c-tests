from __future__ import annotations

from dataclasses import dataclass, field

from output.models.ms_data.particles.particles_z003_xsd.particles_z003_imp import (
    Foo,
)

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class B:
    foo: Foo = field(
        metadata={
            "type": "Element",
            "namespace": "importedXSD",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Doc(B):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"
