from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://simple016.ly/"


@dataclass
class DocType:
    """
    :ivar chap:
    """
    class Meta:
        name = "doc-type"

    chap: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://simple016.ly/",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Doc(DocType):
    class Meta:
        name = "doc"
        namespace = "http://simple016.ly/"


@dataclass
class Book:
    """
    :ivar doc:
    """
    class Meta:
        name = "book"
        namespace = "http://simple016.ly/"

    doc: List[Doc] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
