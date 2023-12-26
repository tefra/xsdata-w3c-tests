from dataclasses import dataclass, field

__NAMESPACE__ = "tck_test"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "tck_test"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
