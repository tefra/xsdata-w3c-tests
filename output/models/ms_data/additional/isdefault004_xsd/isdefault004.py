from dataclasses import dataclass, field


@dataclass
class Root:
    """
    :ivar str_value:
    :ivar number:
    :ivar bool_value:
    """
    class Meta:
        name = "root"

    str_value: str = field(
        default="abc",
        metadata=dict(
            name="str",
            type="Element",
            namespace="",
            required=True
        )
    )
    number: int = field(
        default=123,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    bool_value: bool = field(
        default=True,
        metadata=dict(
            name="bool",
            type="Element",
            namespace="",
            required=True
        )
    )
