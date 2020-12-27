from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Union

__NAMESPACE__ = "http://simple012.ly/"


@dataclass
class DocType:
    class Meta:
        name = "doc-type"

    chap: List[Union[str, datetime]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://simple012.ly/",
            "min_occurs": 1,
        }
    )


@dataclass
class SubDocType:
    class Meta:
        name = "sub-doc-type"

    chap: List[Union[str, datetime]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://simple012.ly/",
            "min_occurs": 1,
        }
    )


@dataclass
class Doc(DocType):
    class Meta:
        name = "doc"
        namespace = "http://simple012.ly/"


@dataclass
class Subdoc(SubDocType):
    class Meta:
        name = "subdoc"
        namespace = "http://simple012.ly/"


@dataclass
class Book:
    class Meta:
        name = "book"
        namespace = "http://simple012.ly/"

    subdoc: List[Subdoc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "sequential": True,
        }
    )
    doc: List[Doc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "sequential": True,
        }
    )
