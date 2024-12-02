from dataclasses import dataclass, field


@dataclass
class Eden:
    class Meta:
        name = "eden"

    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )
