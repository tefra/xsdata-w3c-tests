from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.tempuri.org"


@dataclass
class Root:
    """
    :ivar local_element1:
    :ivar local_element2:
    """
    class Meta:
        name = "root"
        namespace = "http://www.tempuri.org"

    local_element1: Optional[object] = field(
        default=None,
        metadata=dict(
            name="localElement1",
            type="Element",
            namespace="",
            required=True
        )
    )
    local_element2: Optional[object] = field(
        default=None,
        metadata=dict(
            name="localElement2",
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class TestContent:
    """
    :ivar value:
    """
    class Meta:
        name = "testContent"
        namespace = "http://www.tempuri.org"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
