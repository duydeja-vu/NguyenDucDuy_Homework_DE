# Unittest for modules modules.api.src.api

import unittest
import json
from unittest.mock import patch

from modules.api.src import api

from modules.utils.src import rest_api_rescode
from modules.utils.src import db_rescode


class TestMain(unittest.TestCase):

    def setUp(self):
        self.app = api.app.test_client()

    def test_write_pool(self):
        """
        Unit test for /api/write_pool
        Mock all method of module modules.database.src.database.Database
        """

        # write_pool_to_db return db_rescode.RES_WRITE_SUCCESS_INSERTED
        with patch('modules.database.src.database.Database.write_pool_to_db') \
                as mock_1:
            payload = json.dumps({
                "poolId": 123546,
                "poolValues": [1, 7, 2, 6]
            })
            mock_1.return_value = db_rescode.RES_WRITE_SUCCESS_INSERTED
            response = self.app.post(
                '/api/write_pool',
                headers={
                    "Content-Type": "application/json"},
                data=payload)
            self.assertEqual(rest_api_rescode.OK, response.status_code)
            self.assertEqual("Inserted", response.json['status'])

        # write_pool_to_db return db_rescode.RES_WRITE_SUCCESS_APPEND
        with patch('modules.database.src.database.Database.write_pool_to_db') as mock_1:
            payload = json.dumps({
                "poolId": 123546,
                "poolValues": [11, 17, 12, 16]
            })
            mock_1.return_value = db_rescode.RES_WRITE_SUCCESS_APPEND
            response = self.app.post(
                '/api/write_pool',
                headers={
                    "Content-Type": "application/json"},
                data=payload)
            self.assertEqual(rest_api_rescode.OK, response.status_code)
            self.assertEqual("Appended", response.json['status'])

        # write_pool_to_db raise ValueError("PoolId must in integer type")
        with patch('modules.database.src.database.Database.write_pool_to_db') as mock_1:
            payload = json.dumps({
                "poolId": "a",
                "poolValues": [11, 17, 12, 16]
            })
            mock_1.side_effect = ValueError("PoolId must in integer type")
            response = self.app.post(
                '/api/write_pool',
                headers={
                    "Content-Type": "application/json"},
                data=payload)
            self.assertEqual(
                rest_api_rescode.UNSUPPORTED_MEDIA_TYPE, response.status_code)
            self.assertEqual("PoolId must in integer type",
                             response.json['status'])

        # write_pool_to_db raise ValueError("PoolValues must in list type")
        with patch('modules.database.src.database.Database.write_pool_to_db') as mock_1:
            payload = json.dumps({
                "poolId": 123546,
                "poolValues": "a"
            })
            mock_1.side_effect = ValueError("PoolValues must in list type")
            response = self.app.post(
                '/api/write_pool',
                headers={
                    "Content-Type": "application/json"},
                data=payload)
            self.assertEqual(
                rest_api_rescode.UNSUPPORTED_MEDIA_TYPE, response.status_code)
            self.assertEqual("PoolValues must in list type",
                             response.json['status'])

        # write_pool_to_db raise ValueError("PoolId must in integer type")
        with patch('modules.database.src.database.Database.write_pool_to_db') as mock_1:
            payload = json.dumps({
                "poolId": "a",
                "poolValues": "a"
            })
            mock_1.side_effect = ValueError("PoolId must in integer type")
            response = self.app.post(
                '/api/write_pool',
                headers={
                    "Content-Type": "application/json"},
                data=payload)
            self.assertEqual(
                rest_api_rescode.UNSUPPORTED_MEDIA_TYPE, response.status_code)
            self.assertEqual("PoolId must in integer type",
                             response.json['status'])

    def test_read_pool(self):
        """
        Unit test for /api/query_pool
        Mock all method of module modules.database.src.database.Database
        """

        # query_quantile_from_db success return a float
        # query_len_list_from_db success return a integer
        with patch('modules.database.src.database.Database.query_quantile_from_db') as mock_1, \
                patch('modules.database.src.database.Database.query_len_list_from_db') as mock_2:
            payload = json.dumps({
                "poolId": 123456,
                "percentile": 99.5
            })
            mock_1.return_value = float()
            mock_2.return_value = int()
            response = self.app.post(
                '/api/query_pool',
                headers={
                    "Content-Type": "application/json"},
                data=payload)
            self.assertEqual(rest_api_rescode.OK, response.status_code)
            self.assertEqual("Success", response.json['status'])
            self.assertIsInstance(response.json['quantitle'], float)
            self.assertIsInstance(response.json['len_list'], int)

        # query_quantile_from_db raise ValueError(f'PoolId must in integer
        # type')
        with patch('modules.database.src.database.Database.query_quantile_from_db') as mock_1, \
                patch('modules.database.src.database.Database.query_len_list_from_db') as mock_2:
            payload = json.dumps({
                "poolId": 123.4,
                "percentile": 99.5
            })
            mock_1.side_effect = ValueError(f'PoolId must in integer type')
            response = self.app.post(
                '/api/query_pool',
                headers={
                    "Content-Type": "application/json"},
                data=payload)
            self.assertEqual(
                rest_api_rescode.UNSUPPORTED_MEDIA_TYPE, response.status_code)
            self.assertEqual("PoolId must in integer type",
                             response.json['status'])

        # query_quantile_from_db raise ValueError(f'Poolid not in database'))
        with patch('modules.database.src.database.Database.query_quantile_from_db') as mock_1, \
                patch('modules.database.src.database.Database.query_len_list_from_db') as mock_2:
            payload = json.dumps({
                "poolId": 1234,
                "percentile": 99.5
            })
            mock_1.side_effect = ValueError(f'Poolid not in database')
            response = self.app.post(
                '/api/query_pool',
                headers={
                    "Content-Type": "application/json"},
                data=payload)
            self.assertEqual(
                rest_api_rescode.UNSUPPORTED_MEDIA_TYPE, response.status_code)
            self.assertEqual("Poolid not in database", response.json['status'])

        # query_quantile_from_db raise ValueError('Percentile not in numeric
        # type')
        with patch('modules.database.src.database.Database.query_quantile_from_db') as mock_1, \
                patch('modules.database.src.database.Database.query_len_list_from_db') as mock_2:
            payload = json.dumps({
                "poolId": 1234,
                "percentile": "a"
            })
            mock_1.side_effect = ValueError(f'Percentile not in numeric type')
            response = self.app.post(
                '/api/query_pool',
                headers={
                    "Content-Type": "application/json"},
                data=payload)
            self.assertEqual(
                rest_api_rescode.UNSUPPORTED_MEDIA_TYPE, response.status_code)
            self.assertEqual("Percentile not in numeric type",
                             response.json['status'])

        # query_quantile_from_db raise ValueError(f'Percentile must be in range
        # [0.0, 100.0])
        with patch('modules.database.src.database.Database.query_quantile_from_db') as mock_1, \
                patch('modules.database.src.database.Database.query_len_list_from_db') as mock_2:
            payload = json.dumps({
                "poolId": 1234,
                "percentile": 125.0
            })
            mock_1.side_effect = ValueError(
                f'Percentile must be in range [0.0, 100.0]')
            response = self.app.post(
                '/api/query_pool',
                headers={
                    "Content-Type": "application/json"},
                data=payload)
            self.assertEqual(
                rest_api_rescode.UNSUPPORTED_MEDIA_TYPE, response.status_code)
            self.assertEqual(
                "Percentile must be in range [0.0, 100.0]",
                response.json['status'])

        # query_len_list_from_db raise ValueError('Poolid not in database'))
        with patch('modules.database.src.database.Database.query_quantile_from_db') as mock_1, \
                patch('modules.database.src.database.Database.query_len_list_from_db') as mock_2:
            payload = json.dumps({
                "poolId": 12346,
                "percentile": 99.5
            })
            mock_2.side_effect = ValueError(f'Poolid not in database')
            response = self.app.post(
                '/api/query_pool',
                headers={
                    "Content-Type": "application/json"},
                data=payload)
            self.assertEqual(
                rest_api_rescode.UNSUPPORTED_MEDIA_TYPE, response.status_code)
            self.assertEqual("Poolid not in database", response.json['status'])

        # query_len_list_from_db raise ValueError('PoolId must in integer
        # type'))
        with patch('modules.database.src.database.Database.query_quantile_from_db') as mock_1, \
                patch('modules.database.src.database.Database.query_len_list_from_db') as mock_2:
            payload = json.dumps({
                "poolId": 12346,
                "percentile": 99.5
            })
            mock_2.side_effect = ValueError('PoolId must in integer type')
            response = self.app.post(
                '/api/query_pool',
                headers={
                    "Content-Type": "application/json"},
                data=payload)
            self.assertEqual(
                rest_api_rescode.UNSUPPORTED_MEDIA_TYPE, response.status_code)
            self.assertEqual("PoolId must in integer type",
                             response.json['status'])
