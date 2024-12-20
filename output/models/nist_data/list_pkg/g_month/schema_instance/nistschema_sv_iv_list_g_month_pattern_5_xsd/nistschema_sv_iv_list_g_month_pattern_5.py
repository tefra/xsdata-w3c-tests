from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-pattern-5-NS"


@dataclass
class NistschemaSvIvListGMonthPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-pattern-5"
        namespace = "NISTSchema-SV-IV-list-gMonth-pattern-5-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"--1\d --0\d --1\d --\d8 --\d8 --\d7 --0\d --\d8",
            "tokens": True,
        },
    )
