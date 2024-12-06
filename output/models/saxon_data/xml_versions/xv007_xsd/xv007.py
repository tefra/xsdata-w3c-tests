from dataclasses import dataclass, field


@dataclass
class Doc:
    class Meta:
        name = "doc"

    item: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "pattern": r"\c",
        },
    )
