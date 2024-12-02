from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-long-pattern-3-NS"


@dataclass
class NistschemaSvIvListLongPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-long-pattern-3"
        namespace = "NISTSchema-SV-IV-list-long-pattern-3-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\-\d{18} \-\d{9} \-\d{1} \d{5} \d{18}",
            "tokens": True,
        },
    )
