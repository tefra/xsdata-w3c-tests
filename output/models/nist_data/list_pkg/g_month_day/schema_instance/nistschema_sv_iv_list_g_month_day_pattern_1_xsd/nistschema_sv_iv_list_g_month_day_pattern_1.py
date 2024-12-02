from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-pattern-1-NS"


@dataclass
class NistschemaSvIvListGMonthDayPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-pattern-1"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-pattern-1-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"--\d1-\d8 --0\d-\d9 --\d2-\d7 --0\d-\d6 --\d0-\d0 --0\d-1\d --0\d-\d3 --\d2-\d2 --1\d-\d6",
            "tokens": True,
        },
    )
