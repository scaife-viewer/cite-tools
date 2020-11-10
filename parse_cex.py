#!/usr/bin/env python3


DELIM = "#"
DELIM2 = ","

class Handler:

    def __init__(self, line_num):
        self.line_num = line_num
        self.initiate()


class CEXVersion(Handler):

    def initiate(self):
        self.version = None

    def handle(self, line):
        if self.version:
            raise Exception("version already set")
        elif line == "3.0":
            self.version = line
        else:
            raise Exception("version must be 3.0")


class CITELibrary(Handler):

    def initiate(self):
        self.name = None
        self.urn = None
        self.license = None
        self.namespaces = {}

    def handle(self, line):
        data = line.split(DELIM)
        if data[0] == "name":
            self.name = data[1]
        elif data[0] == "urn":
            self.urn = data[1]
        elif data[0] == "license":
            self.license = data[1]
        elif data[0] == "namespace":
            self.namespaces[data[1]] = data[2]
        else:
            raise Exception(f"invalid key {data[0]} in citelibrary")


class CTSCatalog(Handler):

    def initiate(self):
        self.header = None
        self.entries = []

    def handle(self, line):
        data = line.split(DELIM)
        if len(data) != 8:
            raise Exception("ctscatalog rows must have eight columns")
        if self.header is None:
            self.header = data
        else:
            self.entries.append(data)


class CTSData(Handler):

    def initiate(self):
        self.nodes = []

    def handle(self, line):
        data = line.split(DELIM)
        if len(data) != 2:
            raise Exception("ctsdata rows must have two columns")
        self.nodes.append(data)


class CITECollections(Handler):

    def initiate(self):
        self.header = None
        self.collections = []

    def handle(self, line):
        data = line.split(DELIM)
        if len(data) != 5:
            raise Exception("citecollections rows must have five columns")
        if self.header is None:
            self.header = data
        else:
            self.entries.append(data)


class CITEProperties(Handler):

    def initiate(self):
        self.header = None
        self.properties = []

    def handle(self, line):
        data = line.split(DELIM)
        if len(data) != 4:
            raise Exception("citeproperties rows must have four columns")
        if self.header is None:
            self.header = data
        else:
            urn, label, datatype, enum = data
            if datatype not in ["String", "CtsUrn", "Cite2Urn", "Number", "Boolean"]:
                raise Exception(f"invalid property datatype {datatype}")
            if datatype != "String" and enum != "":
                raise Exception("only String properties can have controlled vocabularies")
            self.properties.append([urn, label, datatype, enum.split(DELIM2)])

        # one property must have label="urn" datatype="Cite2Urn"
        # presumably urn and label must be unique but spec is silent on this


class CITEData(Handler):
    # typo 'insensitivie' in spec

    # how does the system know which citecollections and citeproperties blocks are relevant?
    # do they have to occur before the citedata block?

    def initiate(self):
        self.header = None
        self.objects = []

    def handle(self, line):
        data = line.split(DELIM)
        if self.header is None:
            self.header = data
        else:
            # validate the values
            self.objects.append(dict(zip(self.header, data)))


class ImageData(Handler):

    # why does this not have an ignored header?
    # spec says four columns but example has 3 and 2

    def initiate(self):
        self.images = []

    def handle(self, line):
        data = line.split(DELIM)
        # validate the values
        self.images.append(data)


class Relations(Handler):

    # various global constraints to validate

    def initiate(self):
        self.statements = []

    def handle(self, line):
        data = line.split(DELIM)
        self.statements.append(data)
        # validate values


class DataModels(Handler):

    # typo in spec "Collections identified in the datamodel block" should be datamodels

    # extra global validation to do

    def initiate(self):
        self.header = None
        self.datamodels = []

    def handle(self, line):
        data = line.split(DELIM)
        if len(data) != 4:
            raise Exception("datamodels rows must have four columns")
        if self.header is None:
            self.header = data
        else:
            self.datamodels.append(data)


BLOCK_HANDERS = {
    "cexversion": CEXVersion,
    "citelibrary": CITELibrary,
    "ctsdata": CTSData,
    "ctscatalog": CTSCatalog,
    "citecollections": CITECollections,
    "citeproperties": CITEProperties,
    "citedata": CITEData,
    "imagedata": ImageData,
    "relations": Relations,
    "datamodels": DataModels,
}


block_handler = None

def parse(filename):
    with open(filename) as f:
        for line_num, line in enumerate(f, 1):
            line = line.rstrip("\r\n")
            if line == "":
                # ignore empty lines
                pass
            elif line.startswith("//"):
                # ignore comments
                pass
            elif line.startswith("#!"):
                # block label
                if line[2:] in BLOCK_HANDERS.keys():
                    block_handler = BLOCK_HANDERS[line[2:]](line_num)
                else:
                    raise Exception(f"line {line_num}: invalid block label {line}")
            else:
                block_handler.handle(line)


parse("cex_files/test1.cex")
parse("cex_files/test2.cex")
parse("cex_files/test3.cex")
parse("cex_files/test4.cex")
# parse("cex_files/test5.cex")
parse("cex_files/test6.cex")
parse("cex_files/test7.cex")
parse("cex_files/test8.cex")
parse("cex_files/test9.cex")
parse("cex_files/test10.cex")
