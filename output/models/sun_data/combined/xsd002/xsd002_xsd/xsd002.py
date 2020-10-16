from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://foo.com"


@dataclass
class Root:
    """
    :ivar foo:
    :ivar bar:
    :ivar zot:
    """
    class Meta:
        name = "root"
        namespace = "http://foo.com"

    foo: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    bar: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    zot: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
