from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-int-pattern-5-NS"


@dataclass
class NistschemaSvIvListIntPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-int-pattern-5"
        namespace = "NISTSchema-SV-IV-list-int-pattern-5-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\-\d{10} \-\d{7} \-\d{5} \-\d{3} \-\d{1} \d{2} \d{4} \d{6} \d{10}",
            "tokens": True,
        },
    )
