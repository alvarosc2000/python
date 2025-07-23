FastAPI

pipenv install fastapi uvicorn pydantic
pipenv install -r requirements.txt
pipenv run pytest -v
pipenv run uvicorn api:app --reload

 --> poner en la ruta /docs da lugar a documentacion


| Categoría                    | Código | Significado                     |
| ---------------------------- | ------ | ------------------------------- |
| **1XX** Informativos         | 100    | Continue                        |
|                              | 103    | Early Hints (Checkpoint)        |
| **2XX** Éxito                | 200    | OK                              |
|                              | 201    | Created                         |
| **3XX** Redirección          | 301    | Moved Permanently               |
|                              | 302    | Found (Moved Temporarily)       |
| **4XX** Errores del cliente  | 400    | Bad Request                     |
|                              | 401    | Unauthorized                    |
|                              | 403    | Forbidden                       |
|                              | 404    | Not Found                       |
| **5XX** Errores del servidor | 500    | Internal Server Error           |
|                              | 503    | Service Temporarily Unavailable |



--------------------

py -m venv venv
pip install fastapi uvicorn