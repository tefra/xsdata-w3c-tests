from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-pattern-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListDecimalPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-pattern-5"
        namespace = "NISTSchema-SV-IV-list-decimal-pattern-5-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d{1} \-\d{2}\.\d{1} \.\d{5} \d{2}\.\d{5} \-\d{5}\.\d{4} \-\d{5}\.\d{6} \d{5}\.\d{8} \d{5}\.\d{10} \-\d{4}\.\d{14}",
            "tokens": True,
        },
    )
