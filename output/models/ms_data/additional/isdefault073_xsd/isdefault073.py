from dataclasses import dataclass, field


@dataclass
class Ct:
    """
    :ivar a:
    :ivar b:
    """
    class Meta:
        name = "ct"

    a: object = field(
        default="default",
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    b: object = field(
        init=False,
        default="fixed",
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Root(Ct):
    class Meta:
        name = "root"
