from dataclasses import dataclass, field

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Bar:
    class Meta:
        name = "bar"
        namespace = "http://xsdtesting"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
