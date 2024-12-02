from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "a"

    element: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "pattern": r"[1-9][1-9]",
        },
    )
