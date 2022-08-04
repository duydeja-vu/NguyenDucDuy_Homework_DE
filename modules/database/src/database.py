from modules.utils.src import pool_item_schem
from modules.utils.src import constant_value, db_rescode, numeric_checker


class Database(object):
    def __init__(self) -> None:
        """
        Init database to store Pool data
        Args:
            None
        Return:
            None
        """
        self.pool = dict()

    def write_pool_to_db(self, data: dict) -> bool:
        """
        Write Pool data to database
        Args:
            data (Dict): Pool data in dictionary type
        Return:
            Bool: Res code to the user
        """
        res = None
        user_pool_id = data.get(pool_item_schem.CLIENT_DATA_KEY)
        user_pool_value = data.get(pool_item_schem.CLIENT_DATA_VALUE)

        if not numeric_checker.check_is_integer(user_pool_id):
            raise ValueError(f'PoolId must in integer type')
        elif not numeric_checker.check_is_list(user_pool_value):
            raise ValueError(f'PoolValues must in list type')
        else:
            pool_data = self.pool.get(user_pool_id)
            if pool_data is None:
                self.pool.update({user_pool_id: user_pool_value})
                res = db_rescode.RES_WRITE_SUCCESS_INSERTED
            else:
                pool_data.extend(user_pool_value)
                res = db_rescode.RES_WRITE_SUCCESS_APPEND
        return res

    def query_quantile_from_db(self, data: dict) -> float:
        """
        Query quantile from database with data is provided by user
        Example data:
        {

           "poolId": 123546,

           "percentile":99.5

        }
        Args:
            data (Dict): Pool data want to read from database
        Return:
            Float: The calculated quantile
        """

        user_pool_id = data.get(pool_item_schem.CLIENT_DATA_KEY)
        user_percentile = data.get(pool_item_schem.CLIENT_PERCENTILE)

        if not numeric_checker.check_is_integer(user_pool_id):
            raise ValueError('PoolId must in integer type')
        elif not self.is_contain(user_pool_id):
            raise ValueError('Poolid not in database')
        elif not numeric_checker.check_is_general_numeric(user_percentile):
            raise ValueError('Percentile not in numeric type')
        elif not numeric_checker.check_float_in_range(user_percentile,
                                                      constant_value.MIN_PERCENTILE,
                                                      constant_value.MAX_PERCENTILE):
            raise ValueError('Percentile must be in range [0.0, 100.0]')
        else:
            quantitle = self.calculate_quantile(user_pool_id, user_percentile)
        return quantitle

    def is_contain(self, id: int) -> bool:
        """
        Check data of given id in pool or not
        Args:
            id (Int)
        Return:
            Bool: True if poolId in pool, vice versa
        """
        if id in self.pool:
            return True
        else:
            return False

    def query_len_list_from_db(self, data: dict) -> int:
        """
        Query length of pool data list with poolId is provided by user
        Example data:
        {

           "poolId": 123546,

           "percentile":99.5

        }
        Args:
            data (Dict): Pool data want to read from database
        Return:
            Float: Length of pool data list
        """
        user_pool_id = data.get(pool_item_schem.CLIENT_DATA_KEY)

        if not self.is_contain(user_pool_id):
            raise ValueError(f'Poolid not in database')
        elif not numeric_checker.check_is_integer(user_pool_id):
            raise ValueError(f'PoolId must in integer type')
        else:
            length_list = self.calculate_count_elem(user_pool_id)
        return length_list

    def calculate_quantile(self, id: int, percentile: float) -> float:
        """
        Calculate Pool quantile from coressponding id
        Args:
            id (Int): Pool id
            percentile (Float): A percentile value, must be in range [0-100]
        Return:
            Float:  The calculated quantile
        """
        quantile = int()
        pool_data = numeric_checker._sorted((self.pool.get(id)))
        len_list = numeric_checker._len((pool_data))
        if constant_value.MAX_PERCENTILE == percentile:
            quantile = pool_data[len_list - 1]
        elif constant_value.MIN_PERCENTILE == percentile:
            quantile = pool_data[0]
        else:
            norm_p = percentile / constant_value.MAX_PERCENTILE
            id = int(len_list * norm_p - 1)
            quantile = (pool_data[id] + pool_data[id + 1]) / 2.0
        return quantile

    def calculate_count_elem(self, id: int) -> int:
        """
        Calculate total count of elements in coressponding pool id
        Args:
            id (Int) : Pool id
        Return:
            Int: Total count of elements
        """
        return len(self.pool.get(id))
