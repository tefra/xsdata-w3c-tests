from dataclasses import dataclass, field


@dataclass
class Root:
    class Meta:
        name = "root"

    e1: str = field(
        default="asd",
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
