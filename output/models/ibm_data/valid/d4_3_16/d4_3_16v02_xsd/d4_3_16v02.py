from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xstest-tns/schema11_F4_3_16_v02"


@dataclass
class Root:
    """
    :ivar value:
    :ivar attr_dtime_type:
    :ivar attr_dtime_type_et:
    :ivar attr_dtetprohibited:
    :ivar attr_dtetrequired:
    :ivar attr_dtetoptional:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_F4_3_16_v02"

    value: Optional[str] = field(
        default=None,
    )
    attr_dtime_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attrDTimeType",
            type="Attribute"
        )
    )
    attr_dtime_type_et: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attrDTimeTypeET",
            type="Attribute",
            explicit_timezone="optional"
        )
    )
    attr_dtetprohibited: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attrDTETProhibited",
            type="Attribute",
            explicit_timezone="prohibited"
        )
    )
    attr_dtetrequired: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attrDTETRequired",
            type="Attribute",
            explicit_timezone="required"
        )
    )
    attr_dtetoptional: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attrDTETOptional",
            type="Attribute",
            explicit_timezone="optional"
        )
    )
