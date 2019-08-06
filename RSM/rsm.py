import xml.etree.ElementTree as ET

class TEST:
    def __str__(self):
        return "POOP"

class RSM:
    def __init__(self, file):
        self.file = self.__check_init_res(file)
        self.meta = {"NUM_PAGES": self.__find_num_pages(),
                     "NUM_EDU": 0,
                     "NUM_EMP": 0,
                     "NUM_SKILLS": 0,
                     "NUM_CERTS": 0,
                     "NUM_PROJ": 0,
                     }

        # self.data = TODO: write "find data" function(s). This is gonna be a dictionary that holds both the <header> and <info> info.

    # Exceptions:
    class InitResException(Exception):
        """ Raised When Initial Parent Tag is not 'res' """
        def __str__(self):
            return "Initial parent tag is not 'res'"

    # Data Classes:
    # TODO: write class for

    def __check_init_res(self, file):
        et = ET.parse(file)
        root = et.getroot()

        if root.tag.lower() == "res":
            return et
        else:
            raise self.InitResException()

    def __find_num_pages(self):
        root = self.file.getroot()
        num = 0

        for _ in root.iter('page'):
            num += 1

        return num

