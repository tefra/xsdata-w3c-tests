from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-int-pattern-2-NS"


@dataclass
class NistschemaSvIvListIntPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-list-int-pattern-2"
        namespace = "NISTSchema-SV-IV-list-int-pattern-2-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\-\d{10} \-\d{6} \-\d{4} \-\d{2} \d{1} \d{3} \d{5} \d{10}",
            "tokens": True,
        },
    )
