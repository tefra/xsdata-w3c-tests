from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://wild053.org/"


@dataclass
class Zang:
    """
    :ivar any_element:
    """
    class Meta:
        name = "zang"
        namespace = "http://wild053.org/"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Zeng:
    """
    :ivar any_element:
    """
    class Meta:
        name = "zeng"
        namespace = "http://wild053.org/"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Zing:
    """
    :ivar name:
    :ivar local_target_namespace_element:
    """
    class Meta:
        name = "zing"

    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    local_target_namespace_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##local ##targetNamespace",
            required=True
        )
    )


@dataclass
class Zong:
    """
    :ivar any_element:
    """
    class Meta:
        name = "zong"
        namespace = "http://wild053.org/"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
