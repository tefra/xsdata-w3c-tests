from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-pattern-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateTimePattern5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-pattern-5-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d\d77-0\d-0\dT1\d:\d5:\d5",
        },
    )
