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
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    bar: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    zot: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
