from django.contrib.auth.models import User
from django.db import models


# Create your models here.
default_avatar = "iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAAABmJLR0QA/wD/AP+gvaeTAAALfElEQVR42u1dW4wjVxFtHoEEhQg" \
                 "pkEB4rRIQQkHwxR8QKQTCkoQIooDgh+8gBSQkxC8fgHZDCFnxxQdECR8kiwCJQCBkZ/0Yu932eNzd9nh2njs7mffOe3bseftSp+" \
                 "1dzXpnxna7213XfY9Umo3jR/et6nvr1q06pWldBiHEO3r78vf36tbj0ZT1bDxl/Taqm3+NpexoLGUVYro1S39XSDZJRE02ndeq/" \
                 "6+A98YN+7zzWXxH2nwM34nv1hR4oUe3PkpK+y7JuZhh6/R345BivRZ8dzKmmy+SUT2dSOTuUxroMCKRidsjuv0NR+Epa9hHZTcl" \
                 "UcMaIsP7XVy3Hn3jjdH3Kg35gGKx+B5M6TTIr9Cgrwet9BNkLWaYL2PJyGaztynNtQkazE/ToJ4hmWes9OME13wukbEeVJpsdZo" \
                 "3rC+R8/U6DWBFQsUfJYloyn5COZENvPeobn07Zlhmlyj9KOmPG+aTyhDqEE3lT9PgZLtY8TeLbvfBaQy94hMJ+zO09/5XaBRfJ/" \
                 "GU/VYkaX8udIonD/l9CLLQIOyFVfmHZJfG4qyu63eEw8FL5R6hp35cKf4WGY2l7Ye7OoBT29IdKGUfKxV6OP6AGbKrlB83Cp8nD" \
                 "39AKbhpyXdN/CCq29+vO3hR0pyUYynzh9Iq/vz58+9CjFwpsm15nuIG75Qudk8X/ppSnmfyd/hQkjh7xTvJkXlTKc1zuWgYxl2s" \
                 "lX/BKNyLcKdSlm+STSbte5ju781Tzl5WKclvGcFY89rmxXMfchIjlHI6FEI2xyKZ4odZKB/rkpr2gxDTjkTMD3Dw9v+nlBGcYxh" \
                 "YGhr2psicVUoIPCfxH4i5BJCupYI8fHwC62xnla+bP5BpgJJ9BVEcnhBTs1fF8uqGKJe3xd7evqhUKo7g3yV6bXl13XnPwNCE8x" \
                 "mZDpGQadSxgx36wRL3QelN58XQ2KRYWdsQbgDDwGcvjU7Sd9kyOIVLsUzh45040s1zV/z45KzY2d0TXmFnd1eMX5lxvpu5IRi+p" \
                 "qPTD/ye8wAMDF0WW9s7wi/guwuXLnM3gjP+ZfIwTdPGFD09tyg6hfnFFc6zQSWu5x7yIYfPHON4w6n+otgslUWncW2zLFLZAa5G" \
                 "UPR0KaglcLK70Yw56OuU3wjlrR2Rzg3y3Brq5s88Wvf7P4vMVY5PfpDKP+wXMJ0JSj3J3Ce9ePr/w9HTD2LaP2k54LhVBC+CFxU" \
                 "77G5sbmFZcMPM/BLTpcD+qutaPfqCDMetHlcULo1zNIKky2xeKtRkOPVzWPdPcgpZLgVp+8suDnv4Velepggfd4xRxJBfMar1pp" \
                 "ugD7tgD0Ky3IEQNMcgUTRpflFqzx8HO7IAB0gc8waanPodWhZ2Id/VtWvSGACOnDmGiHuShQeaefrPcjzPlwk4Sk5m+OUTUDj/V" \
                 "41i/rfRG+e4XTiSOWQDtqsMZ4G5E88IQGTEMZiBLB3ZMDWzwDIwBI7FEwzA+jPHi8aaKhuWV9Z5JpGmrJdOyvZhScJY3tqWzgCQ" \
                 "d8jyqNiwVpHOf6sBVOlXWV40kjZlwy7FA7iOJ+I8R6V7neN6wfCqZcPBQYU158BRBjCiDCA0BlC8Sfk1ynWhloBwLAFOTCCb/cj" \
                 "hp/97nC9WOYE+GIBhPyXF+l/dBq5LZwBLTLeBh7aDLxyu89M5X6wKBPnDYH6jypf+4xrrgg8VCvaluQWyvmj/3/8pGYo7ZdoJcD" \
                 "0Mqhcna5hr/L9e3BZ5quPgk/yA/GkYwI9luNihUZkSQq5IYgD2M2yrfo5MCduRISVsV5JycmQJ2c9p1aaKchAhoESbfVLoxLRMx" \
                 "BKvIQUsJssF808L35bm6b9OMqXJRuNeYFwYkudZGHIi1ZxW65cr1YXPLiyxU/4M8RNISDA1jTDwmmwXjmkWBZlcsHGtJNvUf11W" \
                 "tGpjAvmo0XQqyeZwSIRyMMZEEQ1LyGEA+7Ly44GcIViCiG22BBFNyr7UBuAQRdDTF8RygGlfl/fJv8kAypLfhCKJanMJWOuCG6l" \
                 "uEYnCDWuyn1O+fFu9xk7gTDfx5jpEkRQx9LKSeJtC0GMOUaTdTcqHTMEACt1IoAxloUoXp4hujpLxGZzqyUMV6yoryMJhUKTb2b" \
                 "SRT4AEDWTpoGIHxNC7e3s3yKLx71J5y0njwnvwXhnO8z2QC1IdBinx4TBIluNgJT71GaB14Fk1GOEUJyGkV7ceV4MRTnFKxXv78" \
                 "verwQipoMGEqBJCrqsBCZ1U08JrlUFJNSChcwB7DzeBelENSujk+UO0sObTakBCtgMgKuAbBpBI5O5TgxKyHUB972F6cTjoizKo" \
                 "CcTI5SmxtLzmnLzt7cvHC1AP3APuBfeEe8M9Mnj6B45qBhmYH5AfHBfrG5siLMC92oNjwRmBbv7mVoZQ3Xq00xfSZw2J1fVrIqw" \
                 "A/W2fdanzO4CjmkigC3Unk0OQvNENU3y72N8/cJhQA6eJqxFFv6xKvAIqKetUnwHD+uPxRNFp8zHF+xscBkeudMIAvn5Cb+DIu/" \
                 "2sFOrPDxN92oHS9DHA2GCMAiOLrm0Hz/h1AWHy9F3vECjd3D8DsH/ZuF1MlTLG84YRIE1QCHQpqODkt8luofa/FddfcCj5wzH4z" \
                 "+Y7hqXth738cXNgVGm1RZiFEW+jf622jqMP9Xv145PTC0qjLWJyet5LAzBa7xlsmE96dQFhjva1EyX0butnftNl53Ar7cUFyEDu" \
                 "xA2oRvLIADI3Mn9angU8Oh8AdbpC6zEBTwyA/Lm2Ooh7sSNQcAcPDOBVrV3U4gI7ygCkM4AN9IHQvEC7zSQVOm8AVPDzU80r6Lp" \
                 "+B33pqDIAOQwAGT8NY/4t+wLV4FBFGQB7AzhoOejTtBG4TBtT6JwBNOwP3A6QNQRSgVYvSsauX5IaQMrzqb8eiYz1IP3QZqtJn0" \
                 "h9UmgeM/NLrSp/MWLYH9M6ARQVtOoP5PIjTis1hca4MtXyOQDpwv6W1kmgtMgNsaOfLF6yA0vlyPiUC95/89dapyGqzaZebZnYk" \
                 "QojVGbQrUCGNDKlXez3/wJdaEEADgclGf7XRdNCZ5pTqGJjsyQypov6AN3qgWOuBYlEYuj9dDFZt9z/YOgKM8BwigeideXbfZFI" \
                 "8U6NAyLZ7AejhjXkqh6Q/IIw5gvskEPsZsqv7fXHLhiFezVOiKTMU7E2OpCDm287JHkD4BrW+1zzEI44/f444kI6fTeCEW6NIEE" \
                 "0r28TUWO3Bo7AMJ5rJ9ePpv1k0r5H4wysS24cw8OStYfF4vJa1ygeGdGgnG2votfqMQzjLk0GoPgQ2xMvqocxXco6I2yWtsTQ2K" \
                 "Q7J+9m+VskMnG7JhOwN63lEbRdZIItEhpF7UtSTQyn1q2DVx/hQ5AnsH2+N85h7hG6kXmvGMDhLF5dWmU3K6CYA7GNjOlZC5lF1" \
                 "9m87IyADilAS+Z1qxh06QSle1AHTZulspiavepHQWcauyqtm+BUHqfMXyBhwXPGC1pjUX008facM/36YRCYcbCmI3CDEvc2tnEN" \
                 "DnWsc74f6QaJuJ57qBPdSkHGZBfHHGKmaXpKl1fXxRqdQaDBFDqNIQKJ1Gsodm9v33kNPQOwVUOTibmFZTE+OUtLzoTIEI2LB45" \
                 "cI8n7lsnDcjYw7J8gc1VRtlklzIzH0rZ0M8BPSMUnr4SXrt16PZHIfkILO8BaRYGOeIiUn2q7YqcbEUvmv9JuFJG5pLtma+cnet" \
                 "O5L9SWhv0uUHolnrLfou4cTyjNtjojUEMDGsCfU77bpHSKr5JtnelJFh5QmvRg14D2JuQ0vQSiQ86dOCng9SdUVeOaleb8Omgyz" \
                 "K/Vup0VORAvI0EWIe9QbuUCnx2I9pyCNE/R7PACKSLhM93tGkLatd/6DrusHIXrB1DmqWgqf5pmih9FDfu5WvbyRQq42PR3GlN1" \
                 "XRBqo/badO09F3Gcjc+itRqWH7ZZOG3i//OvYZKJbYYIAAAAAElFTkSuQmCC"


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    avatar = models.TextField(default=default_avatar)
    description = models.TextField(default="")

    def __str__(self):
        return f"<Profile: user {self.user}>"
