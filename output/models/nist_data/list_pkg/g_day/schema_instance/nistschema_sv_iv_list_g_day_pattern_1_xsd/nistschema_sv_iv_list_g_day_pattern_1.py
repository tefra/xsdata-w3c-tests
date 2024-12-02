from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-gDay-pattern-1-NS"


@dataclass
class NistschemaSvIvListGDayPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-list-gDay-pattern-1"
        namespace = "NISTSchema-SV-IV-list-gDay-pattern-1-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"---\d7 ---2\d ---\d9 ---\d8 ---\d8 ---\d8 ---\d2 ---0\d",
            "tokens": True,
        },
    )
