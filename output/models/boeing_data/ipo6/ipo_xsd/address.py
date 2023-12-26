from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.example.com/add"


@dataclass
class Salutation:
    class Meta:
        name = "salutation"
        namespace = "http://www.example.com/add"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
