from __future__ import annotations

from dataclasses import dataclass, field

from output.models.ms_data.element.elem_z009_xsd.elem_z009_a import A

__NAMESPACE__ = "main"


@dataclass(kw_only=True)
class Ct:
    class Meta:
        name = "ct"

    a: A = field(
        metadata={
            "type": "Element",
            "namespace": "main",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Root(Ct):
    class Meta:
        name = "root"
        namespace = "main"
