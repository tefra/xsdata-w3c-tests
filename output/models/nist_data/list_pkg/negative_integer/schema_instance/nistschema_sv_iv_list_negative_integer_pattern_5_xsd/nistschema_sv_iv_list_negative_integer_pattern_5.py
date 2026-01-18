from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-negativeInteger-pattern-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListNegativeIntegerPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-negativeInteger-pattern-5"
        namespace = "NISTSchema-SV-IV-list-negativeInteger-pattern-5-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\-\d{1} \-\d{3} \-\d{5} \-\d{7} \-\d{9} \-\d{11} \-\d{13} \-\d{18}",
            "tokens": True,
        },
    )
