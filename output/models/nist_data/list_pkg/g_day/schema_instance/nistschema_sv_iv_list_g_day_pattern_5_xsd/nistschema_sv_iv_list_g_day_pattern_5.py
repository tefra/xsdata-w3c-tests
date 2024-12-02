from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-gDay-pattern-5-NS"


@dataclass
class NistschemaSvIvListGDayPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-gDay-pattern-5"
        namespace = "NISTSchema-SV-IV-list-gDay-pattern-5-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"---\d5 ---1\d ---1\d ---0\d ---1\d ---\d9 ---\d3 ---1\d ---\d1 ---1\d",
            "tokens": True,
        },
    )
