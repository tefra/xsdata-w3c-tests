from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-ID-maxLength-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListIdMaxLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-ID-maxLength-4"
        namespace = "NISTSchema-SV-IV-list-ID-maxLength-4-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "max_length": 8,
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-list-ID-maxLength-4-NS"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
