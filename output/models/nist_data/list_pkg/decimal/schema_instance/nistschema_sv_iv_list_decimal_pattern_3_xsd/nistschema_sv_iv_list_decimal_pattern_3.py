from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-pattern-3-NS"


@dataclass
class NistschemaSvIvListDecimalPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-pattern-3"
        namespace = "NISTSchema-SV-IV-list-decimal-pattern-3-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\-\d{1} \-\d{1}\.\d{2} \.\d{5} \d{1}\.\d{6} \-\d{8}\.\d{1} \-\d{1}\.\d{10} \-\d{11}\.\d{2} \-\d{8}\.\d{10}",
            "tokens": True,
        },
    )
