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
        init=False,
        default="abc",
        metadata={
            "name": "str",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    number: int = field(
        init=False,
        default=123,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    bool_value: bool = field(
        init=False,
        default=True,
        metadata={
            "name": "bool",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
