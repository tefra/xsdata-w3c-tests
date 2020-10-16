from dataclasses import dataclass, field
from typing import Dict, Optional

__NAMESPACE__ = "http://foobar"


@dataclass
class Foo:
    """
    :ivar value:
    :ivar any_attributes:
    """
    class Meta:
        name = "foo"
        namespace = "http://foobar"

    value: Optional[str] = field(
        default=None,
    )
    any_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )
