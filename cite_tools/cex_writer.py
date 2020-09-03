CEX_VERSION = "3.0"
DELIMITER = "#"


def generate_block_name(name):
    return f"#!{name}"


def generate_version_block():
    return "\n".join([generate_block_name("cexversion"), CEX_VERSION])


def generate_cex_metadata(name="", urn="", license=""):
    cex_name = name or "CEX Library created by cite-tools"
    cex_urn = urn or "urn:cite2:cex:TEMPCOLL.TEMPVERSION:TEMP_ID"
    cex_license = license or "Public Domain."
    return "\n".join(
        [
            generate_version_block(),
            "",
            generate_block_name("citelibrary"),
            f"name{DELIMITER}{cex_name}",
            f"urn{DELIMITER}{cex_urn}",
            f"license{DELIMITER}{cex_license}",
        ]
    )
