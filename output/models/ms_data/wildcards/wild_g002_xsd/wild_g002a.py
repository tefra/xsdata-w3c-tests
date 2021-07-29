from dataclasses import dataclass, field

__NAMESPACE__ = "http://foo"


@dataclass
class Bar:
    class Meta:
        name = "bar"
        namespace = "http://foo"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
