from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.example.com/IPO"


@dataclass
class ExternFirstElement:
    class Meta:
        namespace = "http://www.example.com/IPO"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
