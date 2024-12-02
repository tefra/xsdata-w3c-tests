from dataclasses import dataclass, field


@dataclass
class Doc:
    class Meta:
        name = "doc"

    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )
