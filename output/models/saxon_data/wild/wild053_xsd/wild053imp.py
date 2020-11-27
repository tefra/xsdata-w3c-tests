from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://wild053.org/"


@dataclass
class Zang:
    class Meta:
        name = "zang"
        namespace = "http://wild053.org/"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class Zeng:
    class Meta:
        name = "zeng"
        namespace = "http://wild053.org/"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class Zing:
    class Meta:
        name = "zing"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    local_target_namespace_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##local ##targetNamespace",
            "required": True,
        }
    )


@dataclass
class Zong:
    class Meta:
        name = "zong"
        namespace = "http://wild053.org/"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
