from dataclasses import dataclass, field


@dataclass
class Ct:
    class Meta:
        name = "ct"

    a: object = field(
        default="default",
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    b: object = field(
        init=False,
        default="fixed",
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Root(Ct):
    class Meta:
        name = "root"
