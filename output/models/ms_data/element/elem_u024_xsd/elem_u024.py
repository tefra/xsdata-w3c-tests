from dataclasses import dataclass, field


@dataclass
class Root:
    class Meta:
        name = "root"

    r: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 10,
            "pattern": r"(ab){2}x",
        },
    )
