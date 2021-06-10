from data import *
import unittest
import add


class TestSecretaryProgram(unittest.TestCase):
    def test_name_people(self):
        result = add.secretary.name_people('11-2')
        self.assertEqual('Геннадий Покемонов', result)

    def test_shelf(self):
        shelf_number = add.secretary.shelf('11-2')
        self.assertEqual('Номер полки: 1', shelf_number)

    def test_del_doc(self):
        self.assertNotIn(add.secretary.del_doc('11-2'), documents[1])

    def test_move_doc(self):
        add.secretary.move_doc(documents[1]['number'], 2)
        self.assertIn(documents[1]['number'], directories['1'])

    def test_add_shelf(self):
        shelf_number = add.secretary.shelf(4)
        self.assertEqual(shelf_number, 'полка 4 создана')


if __name__ == '__main__':
    unittest.main()
