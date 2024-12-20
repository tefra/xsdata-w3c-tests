from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-nonNegativeInteger-pattern-1-NS"


@dataclass
class NistschemaSvIvListNonNegativeIntegerPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-list-nonNegativeInteger-pattern-1"
        namespace = "NISTSchema-SV-IV-list-nonNegativeInteger-pattern-1-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d{1} \d{3} \d{5} \d{7} \d{9} \d{11} \d{13} \d{15} \d{18}",
            "tokens": True,
        },
    )
