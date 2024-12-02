from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-pattern-5-NS"


@dataclass
class NistschemaSvIvListGMonthDayPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-pattern-5"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-pattern-5-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"--0\d-1\d --\d3-1\d --0\d-\d3 --\d5-\d7 --\d2-2\d --0\d-0\d --0\d-1\d --\d1-\d9 --0\d-2\d",
            "tokens": True,
        },
    )
