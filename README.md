# NguyenDucDuy_Homework_DE
This project contains source code and documentation for DE application. 

# INSTALL DEPENDENCIES

## SYSTEM REQUIREMENTS
- Ubuntu 18.04 or higher
- Python 3.7 or higher
- Python3-pip is installed. If not, run this command to install:
    > sudo apt-get install python3-pip
- Git is installed. If not, run this command to install:
    > sudo apt install git

## CLONE THIS PROJECT
- 
    > cd /home/

    > git clone https://github.com/duydeja-vu/NguyenDucDuy_Homework_DE.git

    > sudo chmod 777 -R NguyenDucDuy_Homework_DE/

## EXPORT PYTHON PATH
- 
    > echo export PYTHONPATH="$PYTHONPATH:/home/NguyenDucDuy_Homework_DE" > ~/.bashrc

    > source ~/.bashrc

## INSTALL DEPENDENCIES
- Run this command:
    > cd /home/NguyenDucDuy_Homework_DE

    > pip3 install -r requirements.txt

## GET TEST COVERAGE REPORT
- 
    > cd /home/NguyenDucDuy_Homework_DE

    > ./get_coverage_report.sh

# API List

    1. /api/write_pool
    2. /api/query_pool

## /api/write_pool - POST

### Params
Description: Write (inserted/append) pool data to pool database

| Param      | DataType | Required | Description                                                    | Sample    |
|------------|------|----------|----------------------------------------------------------------|-----------|
| poolId     | Int  | Yes      | Pool ID that identify the coresponding pool in database | 123456    
| poolValues | List | Yes      | Value of pool                                              | [1,7,2,6] |
|            |      |          |                                                                |           |

### Response
| Exception/Succes    | Code | Description                                                              | Sample                                   |
|---------------------|------|--------------------------------------------------------------------------|------------------------------------------|
| Success             | 200  | Server return status when everything success, confirming "appended" or "inserted"                           | {"status":"Inserted"}                    |
| Data Type Exception | 415  | Server return status when input from user don't have correct datatype | {"status":"PoolId must in integer type"} |
|                     |      |                                                                          |                                          |

## /api/query_pool - POST

### Params
| Param      | DataType | Required | Description                                                    | Sample    |
|------------|------|----------|----------------------------------------------------------------|-----------|
| poolId     | Int  | Yes      | Unique pool ID that identify the coresponding pool in database | 123456    |
| percentile | Float/Integer in range [0, 100] | Yes      | A quantile (in percentile form)                                                | 50.0 |
|            |      |          |                                                                |           |

### Response
| Exception/Succes    | Code | Description                                                              | Sample                                   |
|---------------------|------|--------------------------------------------------------------------------|------------------------------------------|
| Success             | 200  | Server return status when everything success, include three fields: status, the calculated quantile (quantitle) and the total count of elements in the pool (len_list)                          | {"len_list":8,"quantitle":2.5,"status":"Success"}                    |
| Data Type Exception | 415  | Server return status when input from user don't have correct datatype, or out of acceptable range | {"status":"PoolId must in integer type"} |
|                     |      |                                                                          |                                          |

# RUN THE API 
1. Run the server: Open a terminal, run following commands to start the server
    >  cd /home/NguyenDucDuy_Homework_DE

    > ./run_server.sh

2. Open another terminal, run following commands to use APIs:
    - Use api/write_pool:

        > curl -i http://127.0.0.1:5000/api/write_pool -X POST -H 'Content-Type: application/json' -d '{"poolId":123, "poolValues":[1,2,3,4]}'

        > Modify option -d with your input
    
    - Use api/query_pool:

        > curl -i http://127.0.0.1:5000/api/query_pool -X POST -H 'Content-Type: application/json' -d '{"poolId":123, "percentile":50.0}'

        > Modify option -d with your input

If you have any question, contact me via:
- phone: 0763387898
- email: duybarca99@gmail.com

Best regards.
Duy.