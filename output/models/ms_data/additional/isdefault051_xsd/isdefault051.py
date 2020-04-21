from dataclasses import dataclass, field


@dataclass
class Root:
    """
    :ivar attr1:
    :ivar attr2:
    :ivar attr3:
    """
    class Meta:
        name = "root"

    attr1: int = field(
        init=False,
        default=123,
        metadata=dict(
            type="Attribute"
        )
    )
    attr2: str = field(
        init=False,
        default="abc",
        metadata=dict(
            type="Attribute"
        )
    )
    attr3: bool = field(
        init=False,
        default=True,
        metadata=dict(
            type="Attribute"
        )
    )
