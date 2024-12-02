from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-positiveInteger-pattern-3-NS"


@dataclass
class NistschemaSvIvListPositiveIntegerPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-positiveInteger-pattern-3"
        namespace = "NISTSchema-SV-IV-list-positiveInteger-pattern-3-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d{1} \d{2} \d{3} \d{4} \d{5} \d{6} \d{7} \d{8} \d{9} \d{18}",
            "tokens": True,
        },
    )
