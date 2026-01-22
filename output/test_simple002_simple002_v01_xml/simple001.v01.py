from output.models.saxon_data.simple.simple002_xsd.simple002 import Chap
from output.models.saxon_data.simple.simple002_xsd.simple002 import Doc


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
