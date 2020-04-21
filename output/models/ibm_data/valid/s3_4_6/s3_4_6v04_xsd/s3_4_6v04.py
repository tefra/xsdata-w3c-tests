from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xstest-tns/schema11_S3_4_6"


@dataclass
class C:
    """
    :ivar a:
    :ivar any_element:
    """
    class Meta:
        name = "c"

    a: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class D:
    """
    :ivar a:
    :ivar any_element:
    """
    class Meta:
        name = "d"

    a: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar value:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_S3_4_6"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
