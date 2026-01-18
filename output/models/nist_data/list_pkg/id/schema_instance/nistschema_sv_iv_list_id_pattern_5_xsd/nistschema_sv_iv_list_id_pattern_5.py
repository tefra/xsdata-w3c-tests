from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-ID-pattern-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListIdPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-ID-pattern-5"
        namespace = "NISTSchema-SV-IV-list-ID-pattern-5-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[\i-[:]][\c-[:]]{59} [\i-[:]][\c-[:]]{51} [\i-[:]][\c-[:]]{49} [\i-[:]][\c-[:]]{43} [\i-[:]][\c-[:]]{28} [\i-[:]][\c-[:]]{11} [\i-[:]][\c-[:]]{28} [\i-[:]][\c-[:]]{15}",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-list-ID-pattern-5-NS"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
