from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xstest-tns/schema11_S3_4_2_4"


@dataclass
class Root:
    """
    :ivar default_attr:
    :ivar e1:
    :ivar e2:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_S3_4_2_4"

    default_attr: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="defaultAttr",
            type="Attribute",
            namespace="http://xstest-tns/schema11_S3_4_2_4",
            required=True
        )
    )
    e1: Optional["Root.E1"] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    e2: Optional["Root.E2"] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )

    @dataclass
    class E1:
        """
        :ivar default_attr:
        """
        default_attr: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="defaultAttr",
                type="Attribute",
                namespace="http://xstest-tns/schema11_S3_4_2_4",
                required=True
            )
        )

    @dataclass
    class E2:
        """
        :ivar default_attr:
        """
        default_attr: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="defaultAttr",
                type="Attribute",
                namespace="http://xstest-tns/schema11_S3_4_2_4",
                required=True
            )
        )