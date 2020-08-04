from dataclasses import dataclass, field
from typing import Dict

__NAMESPACE__ = "http://foobar"


@dataclass
class Foo:
    """
    :ivar other_attributes:
    """
    class Meta:
        name = "foo"
        namespace = "http://foobar"

    other_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##other"
        )
    )
