from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "http://schemas.microsoft.com/office/excel/2003/xml"


class MapInfoTypeHideInactiveListBorder(Enum):
    TRUE = "true"
    FALSE = "false"


@dataclass(kw_only=True)
class SchemaType:
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )
    id: str = field(
        metadata={
            "name": "ID",
            "type": "Attribute",
            "namespace": "http://schemas.microsoft.com/office/excel/2003/xml",
            "required": True,
        }
    )
    namespace: str = field(
        metadata={
            "name": "Namespace",
            "type": "Attribute",
            "namespace": "http://schemas.microsoft.com/office/excel/2003/xml",
            "required": True,
        }
    )
    schema_ref: None | str = field(
        default=None,
        metadata={
            "name": "SchemaRef",
            "type": "Attribute",
            "namespace": "http://schemas.microsoft.com/office/excel/2003/xml",
        },
    )


class TruefalseType(Enum):
    TRUE = "true"
    FALSE = "false"


@dataclass(kw_only=True)
class MapInfoType:
    schema: list[SchemaType] = field(
        default_factory=list,
        metadata={
            "name": "Schema",
            "type": "Element",
            "namespace": "http://schemas.microsoft.com/office/excel/2003/xml",
            "min_occurs": 1,
        },
    )
    hide_inactive_list_border: MapInfoTypeHideInactiveListBorder = field(
        default=MapInfoTypeHideInactiveListBorder.FALSE,
        metadata={
            "name": "HideInactiveListBorder",
            "type": "Attribute",
            "namespace": "http://schemas.microsoft.com/office/excel/2003/xml",
        },
    )
    selection_namespaces: None | str = field(
        default=None,
        metadata={
            "name": "SelectionNamespaces",
            "type": "Attribute",
            "namespace": "http://schemas.microsoft.com/office/excel/2003/xml",
        },
    )
    hide_single_mapped_cell_border: TruefalseType = field(
        default=TruefalseType.TRUE,
        metadata={
            "name": "HideSingleMappedCellBorder",
            "type": "Attribute",
            "namespace": "http://schemas.microsoft.com/office/excel/2003/xml",
        },
    )


@dataclass(kw_only=True)
class MapInfo(MapInfoType):
    class Meta:
        namespace = "http://schemas.microsoft.com/office/excel/2003/xml"
