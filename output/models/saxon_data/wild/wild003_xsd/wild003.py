from dataclasses import dataclass, field


@dataclass
class Eden:
    class Meta:
        name = "eden"

    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
