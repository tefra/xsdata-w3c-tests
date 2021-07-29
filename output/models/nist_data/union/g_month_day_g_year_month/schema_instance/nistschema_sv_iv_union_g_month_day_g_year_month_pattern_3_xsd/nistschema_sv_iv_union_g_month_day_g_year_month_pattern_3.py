from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-3-NS"


@dataclass
class NistschemaSvIvUnionGMonthDayGYearMonthPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-3"
        namespace = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-3-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"--\d2-2\d",
        }
    )
