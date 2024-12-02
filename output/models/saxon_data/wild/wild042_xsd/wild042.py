from dataclasses import dataclass, field


@dataclass
class Computer:
    class Meta:
        name = "computer"

    w3_org_2001_xmlschema_instance_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "http://www.w3.org/2001/XMLSchema-instance",
        },
    )
