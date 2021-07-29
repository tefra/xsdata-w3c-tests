from dataclasses import dataclass, field

__NAMESPACE__ = "foo"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "foo"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[b|c]+",
        }
    )
