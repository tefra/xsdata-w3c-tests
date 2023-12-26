from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.w3.org/1999/xhtml"


@dataclass
class B:
    class Meta:
        name = "b"
        namespace = "http://www.w3.org/1999/xhtml"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
