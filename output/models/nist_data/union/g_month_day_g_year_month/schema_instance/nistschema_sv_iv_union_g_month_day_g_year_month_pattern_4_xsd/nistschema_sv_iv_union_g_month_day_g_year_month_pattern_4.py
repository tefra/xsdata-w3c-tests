from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-4-NS"


@dataclass
class NistschemaSvIvUnionGMonthDayGYearMonthPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-4"
        namespace = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-4-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"18\d\d-\d0",
        }
    )
