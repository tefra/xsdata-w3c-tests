from dataclasses import dataclass, field


@dataclass
class Doc:
    class Meta:
        name = "doc"

    elem: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "pattern": r"\p{Nd}{2}:\d\d:\d\d(\-\d\d:\d\d)?",
        },
    )
