from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class AttRef:
    """
    :ivar xsdtesting_aga1:
    :ivar xsdtesting_aga2:
    :ivar aga1:
    :ivar aga2:
    """
    class Meta:
        name = "attRef"

    xsdtesting_aga1: Optional[str] = field(
        default=None,
        metadata=dict(
            name="aga1",
            type="Attribute",
            namespace="http://xsdtesting"
        )
    )
    xsdtesting_aga2: Optional[str] = field(
        default=None,
        metadata=dict(
            name="aga2",
            type="Attribute",
            namespace="http://xsdtesting"
        )
    )
    aga1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://importedXSD"
        )
    )
    aga2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://importedXSD"
        )
    )


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional[AttRef] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
