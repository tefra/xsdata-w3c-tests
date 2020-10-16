from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://foobar"


@dataclass
class Bar:
    """
    :ivar value:
    """
    class Meta:
        name = "bar"
        namespace = "http://foobar"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Foo:
    """
    :ivar a_b_c_d_e_target_namespace_local_element:
    """
    class Meta:
        name = "foo"
        namespace = "http://foobar"

    a_b_c_d_e_target_namespace_local_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "A B C D E ##targetNamespace ##local",
            "min_occurs": 1,
        }
    )
