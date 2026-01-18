from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-length-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIdLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-length-2"
        namespace = "NISTSchema-SV-IV-atomic-ID-length-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "length": 57,
        },
    )


@dataclass(kw_only=True)
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-length-2-NS"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
