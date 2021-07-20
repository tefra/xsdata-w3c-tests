from dataclasses import dataclass, field
from typing import Dict, Optional

__NAMESPACE__ = "http://foobar"


@dataclass
class Foo:
    class Meta:
        name = "foo"
        namespace = "http://foobar"

    value: Optional[str] = field(
        default=None
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )
