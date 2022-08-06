from output.models.saxon_data.simple.simple001_xsd.simple001 import Chap
from output.models.saxon_data.simple.simple001_xsd.simple001 import Doc
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Doc(
    chap_or_appx=[
        Chap(
            section=[
                Chap.Section(
                    value="",
                    nr=1.0,
                    ref="+INF"
                ),
                Chap.Section(
                    value="",
                    nr=2.0,
                    ref="+INF"
                ),
                Chap.Section(
                    value="",
                    nr=float("inf"),
                    ref="+INF"
                ),
                Chap.Section(
                    value="",
                    nr=float("inf"),
                    ref="+INF"
                ),
            ]
        ),
        DerivedElement(
            qname="{http://simple001.ly/}appx",
            value=Chap(
                section=[
                    Chap.Section(
                        value="",
                        nr=1.0,
                        ref="+INF"
                    ),
                    Chap.Section(
                        value="",
                        nr=2.0,
                        ref="+INF"
                    ),
                    Chap.Section(
                        value="",
                        nr=float("inf"),
                        ref="+INF"
                    ),
                    Chap.Section(
                        value="",
                        nr=float("inf"),
                        ref="+INF"
                    ),
                ]
            ),
            type=None
        ),
    ]
)
