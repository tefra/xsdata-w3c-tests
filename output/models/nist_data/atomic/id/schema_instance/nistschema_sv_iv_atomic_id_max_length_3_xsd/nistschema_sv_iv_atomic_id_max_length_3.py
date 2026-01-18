from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-maxLength-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIdMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-maxLength-3"
        namespace = "NISTSchema-SV-IV-atomic-ID-maxLength-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 58,
        },
    )


@dataclass(kw_only=True)
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-maxLength-3-NS"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
