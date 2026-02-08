from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-pattern-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIdPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-ID-pattern-3-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"[\i-[:]][\c-[:]]{18}",
        },
    )


@dataclass(kw_only=True)
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-pattern-3-NS"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
