from __future__ import annotations

from dataclasses import dataclass, field

from output.models.ms_data.element.elem_z010_xsd.elem_z010_c import C

__NAMESPACE__ = "b"


@dataclass(kw_only=True)
class B(C):
    class Meta:
        name = "b"

    b: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "b",
        },
    )
