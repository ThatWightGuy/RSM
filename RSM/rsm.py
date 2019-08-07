import xml.etree.ElementTree as ET

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
        """ Raised when initial parent tag is not 'res' """

        def __str__(self):
            return "Initial parent tag is not 'res'"

    class TagNotRecognizedException(Exception):
        """ Raised when tag is not recognized by parent tag (incorrect formatting)"""

        def __init__(self, tag, parent):
            self.tag = tag
            self.parent = parent

        def __str__(self):
            return self.tag + " cannot be used with " + self.parent

    # Data Classes:
    # TODO: write classes for <item> and <info>

    class Info:
        def __init__(self, type, title=None):
            self.type = type
            self.title = self.__get_title(title)
            self.data = self.__get_data()

        def __get_title(self, title):
            defaults = {"sum": "Summary",
                        "edu": "Education",
                        "emp": "Employment",
                        "skills": "Skills",
                        "certs": "Certifications",
                        "proj": "Projects",
                        "head": None}

            if title is not None:
                return title
            else:
                return defaults[self.type]

        def __get_data(self):
            # TODO: create functions based on each info type

            data = {"sum": self.__sum_data(),
                    "edu": self.__edu_data(),
                    "emp": self.__emp_data(),
                    "skills": self.__skills_data(),
                    "certs": self.__certs_data(),
                    "proj": self.__proj_data()}

            return data[self.type]

        def __sum_data(self):
            # TODO

            return dict()

        def __edu_data(self):
            # TODO

            return dict()

        def __emp_data(self):
            # TODO
            return dict()

        def __skills_data(self):
            # TODO

            return dict()

        def __certs_data(self):
            # TODO

            return dict()

        def __proj_data(self):
            # TODO

            return dict()

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

