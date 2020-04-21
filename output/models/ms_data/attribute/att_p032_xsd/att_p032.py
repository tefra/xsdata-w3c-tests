from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class AttRef:
    """
    :ivar att:
    :ivar red_att:
    :ivar inc_att:
    :ivar imp_att:
    """
    class Meta:
        name = "attRef"

    att: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://xsdtesting"
        )
    )
    red_att: Optional[str] = field(
        default=None,
        metadata=dict(
            name="redAtt",
            type="Attribute",
            namespace="http://xsdtesting"
        )
    )
    inc_att: Optional[str] = field(
        default=None,
        metadata=dict(
            name="incAtt",
            type="Attribute",
            namespace="http://xsdtesting"
        )
    )
    imp_att: Optional[str] = field(
        default=None,
        metadata=dict(
            name="impAtt",
            type="Attribute",
            namespace="http://importedXSD"
        )
    )


@dataclass
class Red:
    """
    :ivar red_ctatt:
    :ivar xx:
    """
    class Meta:
        name = "red"

    red_ctatt: Optional[str] = field(
        default=None,
        metadata=dict(
            name="redCTAtt",
            type="Attribute",
            namespace="http://xsdtesting"
        )
    )
    xx: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://xsdtesting"
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
