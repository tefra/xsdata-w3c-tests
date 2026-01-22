from output.models.saxon_data.simple.simple001_xsd.simple001 import Chap
from output.models.saxon_data.simple.simple001_xsd.simple001 import Doc


obj = Doc(
    chap_or_appx=[
        Doc.Chap(
            section=[
                Chap.Section(
                    nr=1.0
                ),
                Chap.Section(
                    nr=2.0
                ),
                Chap.Section(

                ),
                Chap.Section(

                ),
            ]
        ),
        Doc.Appx(
            section=[
                Chap.Section(
                    nr=1.0
                ),
                Chap.Section(
                    nr=2.0
                ),
                Chap.Section(

                ),
                Chap.Section(

                ),
            ]
        ),
    ]
)
