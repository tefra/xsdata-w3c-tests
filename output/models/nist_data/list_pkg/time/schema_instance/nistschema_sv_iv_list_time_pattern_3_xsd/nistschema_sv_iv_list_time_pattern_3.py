from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-pattern-3-NS"


@dataclass
class NistschemaSvIvListTimePattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-pattern-3"
        namespace = "NISTSchema-SV-IV-list-time-pattern-3-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d4:4\d:\d8 \d4:2\d:2\d 0\d:4\d:3\d \d3:\d4:1\d 1\d:\d8:5\d \d2:\d3:4\d \d3:0\d:\d6 \d6:4\d:\d6 \d8:\d2:2\d",
            "tokens": True,
        },
    )
