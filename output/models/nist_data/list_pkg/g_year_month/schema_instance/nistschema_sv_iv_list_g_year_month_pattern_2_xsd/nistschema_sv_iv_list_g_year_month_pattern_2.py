from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYearMonth-pattern-2-NS"


@dataclass
class NistschemaSvIvListGYearMonthPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYearMonth-pattern-2"
        namespace = "NISTSchema-SV-IV-list-gYearMonth-pattern-2-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"17\d\d-\d8 19\d\d-1\d 20\d\d-0\d 17\d\d-0\d \d\d42-\d7 \d\d81-1\d 18\d\d-\d6",
            "tokens": True,
        },
    )
