# Unittest for modules.database.src.database

import unittest
from unittest.mock import patch

from modules.database.src.database import Database

from modules.utils.src import db_rescode


class MockPythonDict(object):
    def __init__(self) -> None:
        pass

    def get(self, id):
        return True

    def update(self, data: dict):
        return True

    def extend(self, id: int):
        return True


class TestMain(unittest.TestCase):
    def setUp(self):
        self.test_object = Database()
        self.test_object.pool = MockPythonDict()

    def test_init(self):
        self.assertIsInstance(self.test_object, Database)

    def test_write_pool_to_db(self):
        with patch.object(self.test_object.pool, 'get') as mock_1, \
                patch.object(self.test_object.pool, 'update') as mock_2:
            mock_1.return_value = None

            data = {
                "poolId": 123546,
                "poolValues": [1, 7, 2, 6]
            }
            res = self.test_object.write_pool_to_db(data)
            self.assertTrue(mock_1.called)
            self.assertTrue(mock_2.called)
            self.assertEqual(res, db_rescode.RES_WRITE_SUCCESS_INSERTED)

        with patch.object(self.test_object.pool, 'get') as mock_1, \
                patch.object(self.test_object.pool, 'update') as mock_2:
            mock_1.return_value = [1, 7, 2, 6]

            data = {
                "poolId": 123546,
                "poolValues": [1, 7, 2, 6]
            }

            res = self.test_object.write_pool_to_db(data)
            self.assertTrue(mock_1.called)
            self.assertFalse(mock_2.called)
            self.assertEqual(res, db_rescode.RES_WRITE_SUCCESS_APPEND)

        with patch.object(self.test_object.pool, 'get') as mock_1, \
                patch.object(self.test_object.pool, 'update') as mock_2, \
                patch('modules.utils.src.numeric_checker.check_is_integer') as mock_3,\
                patch('modules.utils.src.numeric_checker.check_is_list') as mock_4:
            mock_1.return_value = [1, 7, 2, 6]
            mock_2.return_value = True
            mock_3.return_value = False
            mock_4.return_value = True
            data = {
                "poolId": 123546,
                "poolValues": [1, 7, 2, 6]
            }

            with self.assertRaises(ValueError):
                self.test_object.write_pool_to_db(data)

        with patch.object(self.test_object.pool, 'get') as mock_1, \
                patch.object(self.test_object.pool, 'update') as mock_2, \
                patch('modules.utils.src.numeric_checker.check_is_integer') as mock_3,\
                patch('modules.utils.src.numeric_checker.check_is_list') as mock_4:
            mock_1.return_value = [1, 7, 2, 6]
            mock_2.return_value = True
            mock_3.return_value = True
            mock_4.return_value = False
            data = {
                "poolId": 123546,
                "poolValues": [1, 7, 2, 6]
            }
            with self.assertRaises(ValueError):
                self.test_object.write_pool_to_db(data)

    def test_query_quantile_from_db(self):

        with patch.object(self.test_object, 'calculate_quantile') as mock_1, \
                patch.object(self.test_object, 'is_contain') as mock_2, \
                patch('modules.utils.src.numeric_checker.check_is_integer') as mock_3,\
                patch('modules.utils.src.numeric_checker.check_is_general_numeric') as mock_4, \
                patch('modules.utils.src.numeric_checker.check_float_in_range') as mock_5:

            # data have correct data type
            data = {
                "poolId": 123546,
                "percentile": 99.5
            }
            mock_1.return_value = 2.0
            mock_2.return_value = True
            mock_3.return_value = True
            mock_4.return_value = True
            mock_5.return_value = True
            res = self.test_object.query_quantile_from_db(data)
            self.assertEqual(res, 2.0)

        with patch.object(self.test_object, 'calculate_quantile') as mock_1, \
                patch.object(self.test_object, 'is_contain') as mock_2, \
                patch('modules.utils.src.numeric_checker.check_is_integer') as mock_3,\
                patch('modules.utils.src.numeric_checker.check_is_general_numeric') as mock_4, \
                patch('modules.utils.src.numeric_checker.check_float_in_range') as mock_5:

            # data have correct data type
            data = {
                "poolId": 123546,
                "percentile": 99.5
            }
            mock_1.return_value = 2.0
            mock_2.return_value = False
            mock_3.return_value = True
            mock_4.return_value = True
            mock_5.return_value = True
            with self.assertRaises(ValueError):
                self.test_object.query_quantile_from_db(data)

        with patch.object(self.test_object, 'calculate_quantile') as mock_1, \
                patch.object(self.test_object, 'is_contain') as mock_2, \
                patch('modules.utils.src.numeric_checker.check_is_integer') as mock_3,\
                patch('modules.utils.src.numeric_checker.check_is_general_numeric') as mock_4, \
                patch('modules.utils.src.numeric_checker.check_float_in_range') as mock_5:

            # data have correct data type
            data = {
                "poolId": 123546,
                "percentile": 99.5
            }
            mock_1.return_value = 2.0
            mock_2.return_value = True
            mock_3.return_value = False
            mock_4.return_value = True
            mock_5.return_value = True
            with self.assertRaises(ValueError):
                self.test_object.query_quantile_from_db(data)

        with patch.object(self.test_object, 'calculate_quantile') as mock_1, \
                patch.object(self.test_object, 'is_contain') as mock_2, \
                patch('modules.utils.src.numeric_checker.check_is_integer') as mock_3,\
                patch('modules.utils.src.numeric_checker.check_is_general_numeric') as mock_4, \
                patch('modules.utils.src.numeric_checker.check_float_in_range') as mock_5:

            # data have correct data type
            data = {
                "poolId": 123546,
                "percentile": 99.5
            }
            mock_1.return_value = 2.0
            mock_2.return_value = True
            mock_3.return_value = True
            mock_4.return_value = False
            mock_5.return_value = True
            with self.assertRaises(ValueError):
                self.test_object.query_quantile_from_db(data)

        with patch.object(self.test_object, 'calculate_quantile') as mock_1, \
                patch.object(self.test_object, 'is_contain') as mock_2, \
                patch('modules.utils.src.numeric_checker.check_is_integer') as mock_3,\
                patch('modules.utils.src.numeric_checker.check_is_general_numeric') as mock_4, \
                patch('modules.utils.src.numeric_checker.check_float_in_range') as mock_5:

            # data have correct data type
            data = {
                "poolId": 123546,
                "percentile": 99.5
            }
            mock_1.return_value = 2.0
            mock_2.return_value = True
            mock_3.return_value = True
            mock_4.return_value = True
            mock_5.return_value = False
            with self.assertRaises(ValueError):
                self.test_object.query_quantile_from_db(data)

    def test_query_len_list_from_db(self):
        with patch.object(self.test_object, 'is_contain') as mock_1, \
                patch('modules.utils.src.numeric_checker.check_is_integer') as mock_2, \
                patch.object(self.test_object, 'calculate_count_elem') as mock_3:
            data = {
                "poolId": 123546,
                "percentile": 99.5
            }
            mock_1.return_value = False
            mock_2.return_value = True
            mock_3.return_value = 3
            with self.assertRaises(ValueError):
                self.test_object.query_len_list_from_db(data)

        with patch.object(self.test_object, 'is_contain') as mock_1, \
                patch('modules.utils.src.numeric_checker.check_is_integer') as mock_2, \
                patch.object(self.test_object, 'calculate_count_elem') as mock_3:
            data = {
                "poolId": 123546,
                "percentile": 99.5
            }
            mock_1.return_value = True
            mock_2.return_value = False
            mock_3.return_value = 3
            with self.assertRaises(ValueError):
                self.test_object.query_len_list_from_db(data)

        with patch.object(self.test_object, 'is_contain') as mock_1, \
                patch('modules.utils.src.numeric_checker.check_is_integer') as mock_2, \
                patch.object(self.test_object, 'calculate_count_elem') as mock_3:
            data = {
                "poolId": 123546,
                "percentile": 99.5
            }
            mock_1.return_value = True
            mock_2.return_value = True
            mock_3.return_value = 3
            res = self.test_object.query_len_list_from_db(data)
            self.assertEqual(res, 3)

    def test_calculate_quantile(self):
        with patch('modules.utils.src.numeric_checker._sorted') as mock_1, \
                patch('modules.utils.src.numeric_checker._len') as mock_2, \
                patch.object(self.test_object.pool, 'get') as mock_3:
            mock_1.return_value = [1, 2, 3, 4]
            mock_2.return_value = 4
            mock_3.return_value = [1, 2, 3, 4]
            res = self.test_object.calculate_quantile(123546, 50.0)
            self.assertEqual(res, 2.5)

        with patch('modules.utils.src.numeric_checker._sorted') as mock_1, \
                patch('modules.utils.src.numeric_checker._len') as mock_2, \
                patch.object(self.test_object.pool, 'get') as mock_3:
            mock_1.return_value = [1, 2, 3, 4]
            mock_2.return_value = 4
            mock_3.return_value = [1, 2, 3, 4]
            res = self.test_object.calculate_quantile(123546, 50.0)
            self.assertEqual(res, 2.5)

    def test_calculate_count_elem(self):
        with patch.object(self.test_object.pool, 'get') as mock_1:
            self.test_object.calculate_count_elem(1)
            self.assertTrue(mock_1.called)
