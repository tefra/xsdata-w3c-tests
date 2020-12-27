from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

__NAMESPACE__ = "http://xstest-tns/schema11_F4_3_16_v02"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_F4_3_16_v02"

    value: Optional[str] = field(
        default=None,
    )
    attr_dtime_type: Optional[datetime] = field(
        default=None,
        metadata={
            "name": "attrDTimeType",
            "type": "Attribute",
        }
    )
    attr_dtime_type_et: Optional[datetime] = field(
        default=None,
        metadata={
            "name": "attrDTimeTypeET",
            "type": "Attribute",
            "explicit_timezone": "optional",
        }
    )
    attr_dtetprohibited: Optional[datetime] = field(
        default=None,
        metadata={
            "name": "attrDTETProhibited",
            "type": "Attribute",
            "explicit_timezone": "prohibited",
        }
    )
    attr_dtetrequired: Optional[datetime] = field(
        default=None,
        metadata={
            "name": "attrDTETRequired",
            "type": "Attribute",
            "explicit_timezone": "required",
        }
    )
    attr_dtetoptional: Optional[datetime] = field(
        default=None,
        metadata={
            "name": "attrDTETOptional",
            "type": "Attribute",
            "explicit_timezone": "optional",
        }
    )
