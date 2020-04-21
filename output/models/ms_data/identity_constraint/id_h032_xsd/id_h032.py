from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Kid:
    """
    :ivar val:
    """
    class Meta:
        name = "kid"

    val: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Uidtype:
    """
    :ivar hid:
    :ivar iid:
    """
    class Meta:
        name = "uidtype"

    hid: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    iid: Optional["Uidtype.Iid"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )

    @dataclass
    class Iid:
        """
        :ivar val:
        """
        val: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute"
            )
        )


@dataclass
class Root:
    """
    :ivar uid:
    :ivar kid:
    """
    class Meta:
        name = "root"

    uid: List[Uidtype] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    kid: List[Kid] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
