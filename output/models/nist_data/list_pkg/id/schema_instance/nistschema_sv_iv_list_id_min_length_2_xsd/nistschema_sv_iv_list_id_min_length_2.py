from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-ID-minLength-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListIdMinLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-ID-minLength-2"
        namespace = "NISTSchema-SV-IV-list-ID-minLength-2-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "min_length": 6,
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-list-ID-minLength-2-NS"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
