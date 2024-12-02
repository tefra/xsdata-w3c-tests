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
            "pattern": r"\p{Nd}{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        },
    )
