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


def generate_catalog_entry(entry):
    """
    edu.holycross.shot.ohco2.CatalogEntry struct
    {
        "urn": "",
        "citation_scheme": "",
        "group_name": "",
        "work_title": "",
        "version_label": "",
        "exemplar_label": "",
        "online": "",
        "lang": "",
    }
    """
    # TODO: Create actual typed entries
    return f"{DELIMITER}".join(entry.values())


def generate_catalog_block(catalog_entries):
    return "\n".join(
        [
            generate_block_name("ctscatalog"),
            f"{DELIMITER}".join(
                [
                    "urn",
                    "citationScheme",
                    "groupName",
                    "workTitle",
                    "versionLabel",
                    "exemplarLabel",
                    "online",
                    "lang",
                ]
            ),
            "\n".join([generate_catalog_entry(entry) for entry in catalog_entries]),
        ]
    )


def main():
    print(generate_cex_metadata())
    print()
    catalog_entries = [
        {
            "urn": "foo",
            "citation_scheme": "bar",
            "group_name": "baz",
            "work_title": "bing",
            "version_label": "",
            "exemplar_label": "",
            "online": "true",
            "lang": "grc",
        }
    ]
    print(generate_catalog_block(catalog_entries))


if __name__ == "__main__":
    main()
