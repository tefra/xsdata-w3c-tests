from dataclasses import dataclass, field

__NAMESPACE__ = "psContents"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "psContents"

    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
