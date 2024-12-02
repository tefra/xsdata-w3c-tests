from dataclasses import dataclass, field


@dataclass
class Doc:
    class Meta:
        name = "doc"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
