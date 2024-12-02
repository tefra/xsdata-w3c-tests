from dataclasses import dataclass, field


@dataclass
class Root:
    class Meta:
        name = "root"

    e: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 2,
            "max_occurs": 20,
        },
    )
