from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class DeptType:
    deptno: int = field(
        metadata={
            "name": "Deptno",
            "type": "Element",
            "namespace": "a",
            "required": True,
        }
    )
    dname: str = field(
        metadata={
            "name": "Dname",
            "type": "Element",
            "namespace": "a",
            "required": True,
        }
    )
    loc: str = field(
        metadata={
            "name": "Loc",
            "type": "Element",
            "namespace": "a",
            "required": True,
        }
    )
    id: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class EmployeeType:
    empno: int = field(
        metadata={
            "name": "Empno",
            "type": "Element",
            "namespace": "a",
            "required": True,
        }
    )
    ename: str = field(
        metadata={
            "name": "Ename",
            "type": "Element",
            "namespace": "a",
            "required": True,
        }
    )
    sal: float = field(
        metadata={
            "name": "Sal",
            "type": "Element",
            "namespace": "a",
            "required": True,
        }
    )
    deptno: int = field(
        metadata={
            "name": "Deptno",
            "type": "Element",
            "namespace": "a",
            "required": True,
        }
    )
    id: int = field(
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "a",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "a"

    dept: list[DeptType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    employee: list[EmployeeType] = field(
        default_factory=list,
        metadata={
            "name": "Employee",
            "type": "Element",
            "min_occurs": 1,
        },
    )
