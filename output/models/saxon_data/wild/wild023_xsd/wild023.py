from dataclasses import dataclass, field


@dataclass
class T:
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass
class Eden(T):
    class Meta:
        name = "eden"
