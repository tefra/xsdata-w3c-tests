from dataclasses import dataclass, field


@dataclass
class Root:
    class Meta:
        name = "root"

    local_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
        },
    )
