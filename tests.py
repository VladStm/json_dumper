import unittest

from dumper import dump


class DumperTestCase(unittest.TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Vlad",
            "surname": "Paterylo",
            "children": [
                {
                    "name": "Leo",
                    "surname": "Surname",
                    "marks": [
                        5,
                        4,
                        3,
                        2,
                        1
                    ]
                },
                {
                    "name": "Jim",
                    "surname": "wick",
                    "marks": "No marks"
                }
            ],
            "Job": {
                "company": "Nocompany",
                "position": "Developer"
            }
        }
        self.invalid_data = {
            "type": "tuple",
            "is not valid?": (1, 2),
            "raise exception?": "yes"
        }
        self.valid_data_dumped = 'name=Vlad\nsurname=Paterylo\nchildren=\n    name=Leo\n    surname=Surname\n    marks=\n        5\n        4\n        3\n        2\n        1\n\n    name=Jim\n    surname=wick\n    marks=No marks\nJob=\n  company=Nocompany\n  position=Developer'

    def test_dump_valid_data(self):
        dumped_data = dump('', self.valid_data, 0)
        self.assertEqual(dumped_data.strip(), self.valid_data_dumped)

    def test_dump_invalid_data(self):
        with self.assertRaises(TypeError):
            dump('', self.invalid_data, 0)


if __name__ == '__main__':
    unittest.main()



