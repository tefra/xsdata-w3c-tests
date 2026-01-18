from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-minLength-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIdMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-minLength-5"
        namespace = "NISTSchema-SV-IV-atomic-ID-minLength-5-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 64,
        },
    )


@dataclass(kw_only=True)
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-minLength-5-NS"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
