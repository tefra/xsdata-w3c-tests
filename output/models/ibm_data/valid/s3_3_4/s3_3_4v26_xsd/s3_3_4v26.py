from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Ids:
    """
    :ivar idref_element:
    :ivar id_attr:
    """
    class Meta:
        name = "ids"

    idref_element: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    id_attr: str = field(
        default="zxc",
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Root(Ids):
    class Meta:
        name = "root"