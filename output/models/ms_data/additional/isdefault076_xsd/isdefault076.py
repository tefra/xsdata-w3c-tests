from dataclasses import dataclass, field


@dataclass
class Root:
    class Meta:
        name = "root"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
