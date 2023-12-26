from dataclasses import dataclass, field


@dataclass
class Root:
    class Meta:
        name = "root"

    str_value: str = field(
        default="abc",
        metadata={
            "name": "str",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    number: int = field(
        default=123,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    bool_value: bool = field(
        default=True,
        metadata={
            "name": "bool",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
