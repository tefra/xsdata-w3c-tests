from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-1-NS"


@dataclass
class NistschemaSvIvUnionGMonthDayGYearMonthPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-1"
        namespace = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-1-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"--\d7-2\d",
        },
    )
