from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-pattern-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicQnamePattern5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-QName-pattern-5-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{58}",
        },
    )
