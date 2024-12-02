from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-pattern-1-NS"


@dataclass
class NistschemaSvIvListTimePattern1:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-pattern-1"
        namespace = "NISTSchema-SV-IV-list-time-pattern-1-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"1\d:\d3:\d2 \d2:0\d:4\d \d5:\d1:\d8 \d7:0\d:0\d 0\d:1\d:5\d \d4:0\d:\d6",
            "tokens": True,
        },
    )
