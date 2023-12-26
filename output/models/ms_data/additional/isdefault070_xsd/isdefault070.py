from dataclasses import dataclass, field


@dataclass
class Ct:
    class Meta:
        name = "ct"

    a: str = field(
        init=False,
        default="fixed_value",
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class Root(Ct):
    class Meta:
        name = "root"
