from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Foo:
    class Meta:
        name = "foo"

    foo_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "http://foo",
        },
    )
