from dataclasses import dataclass, field
from typing import Dict

__NAMESPACE__ = "http://foobar"


@dataclass
class Foo:
    class Meta:
        name = "foo"
        namespace = "http://foobar"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    local_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
        },
    )
