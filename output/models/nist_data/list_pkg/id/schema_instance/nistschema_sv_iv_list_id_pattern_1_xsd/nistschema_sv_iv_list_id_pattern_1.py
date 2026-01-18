from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-ID-pattern-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListIdPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-list-ID-pattern-1"
        namespace = "NISTSchema-SV-IV-list-ID-pattern-1-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[\i-[:]][\c-[:]]{2} [\i-[:]][\c-[:]]{57} [\i-[:]][\c-[:]]{31} [\i-[:]][\c-[:]]{5} [\i-[:]][\c-[:]]{10} [\i-[:]][\c-[:]]{47} [\i-[:]][\c-[:]]{21}",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-list-ID-pattern-1-NS"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
