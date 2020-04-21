from dataclasses import dataclass, field


@dataclass
class Root:
    """
    :ivar e1:
    """
    class Meta:
        name = "root"

    e1: int = field(
        default="asd",
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
