from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-2-NS"


@dataclass
class NistschemaSvIvUnionGMonthDayGYearMonthPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-2"
        namespace = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-2-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\d\d65-\d1",
        }
    )
