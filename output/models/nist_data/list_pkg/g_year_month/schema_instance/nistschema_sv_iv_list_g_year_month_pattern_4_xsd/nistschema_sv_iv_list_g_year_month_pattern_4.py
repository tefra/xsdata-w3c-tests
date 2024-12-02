from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYearMonth-pattern-4-NS"


@dataclass
class NistschemaSvIvListGYearMonthPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYearMonth-pattern-4"
        namespace = "NISTSchema-SV-IV-list-gYearMonth-pattern-4-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d\d93-\d3 19\d\d-0\d \d\d33-\d3 18\d\d-\d1 \d\d34-0\d",
            "tokens": True,
        },
    )
