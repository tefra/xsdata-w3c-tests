from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://xstest-tns/schema11_F4_3_16_v02"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_F4_3_16_v02"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    attr_dtime_type: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "attrDTimeType",
            "type": "Attribute",
        },
    )
    attr_dtime_type_et: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "attrDTimeTypeET",
            "type": "Attribute",
            "explicit_timezone": "optional",
        },
    )
    attr_dtetprohibited: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "attrDTETProhibited",
            "type": "Attribute",
            "explicit_timezone": "prohibited",
        },
    )
    attr_dtetrequired: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "attrDTETRequired",
            "type": "Attribute",
            "explicit_timezone": "required",
        },
    )
    attr_dtetoptional: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "attrDTETOptional",
            "type": "Attribute",
            "explicit_timezone": "optional",
        },
    )
