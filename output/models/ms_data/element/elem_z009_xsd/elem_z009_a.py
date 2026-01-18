from __future__ import annotations

from dataclasses import dataclass, field

from output.models.ms_data.element.elem_z009_xsd.elem_z009_b import B

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class A(B):
    class Meta:
        name = "a"

    a: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "a",
        },
    )
