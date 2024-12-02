from dataclasses import dataclass, field


@dataclass
class Computer:
    class Meta:
        name = "computer"

    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
