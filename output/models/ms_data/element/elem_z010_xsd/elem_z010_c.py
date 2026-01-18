from __future__ import annotations

from dataclasses import dataclass, field

from output.models.ms_data.element.elem_z010_xsd.elem_z010_d import D

__NAMESPACE__ = "c"


@dataclass(kw_only=True)
class C(D):
    class Meta:
        name = "c"

    c: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "c",
        },
    )
