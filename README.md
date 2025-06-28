### Análise inicial:

Inicialmente o código foi refatorado pois havia problemas de relative imports e não vi necessidade em gerar um pacote "identifiermain" e associa-lo ao ambiente virtual apenas para rodar o coverage.

## Execuções iniciais:

=== Testando o Módulo IdentifierMain ===
$ python routines/IdentifierMain.py abc
Valido


=== Executando o Teste test_validate (1) ===
$ python -m pytest -v routines/tests/test_validate.py
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-8.4.1, pluggy-1.6.0 -- /home/emanuelgse/.conda/envs/esbd3_1/bin/python
cachedir: .pytest_cache
rootdir: /home/emanuelgse/ESBD3/esbd3_1
plugins: timeout-2.4.0, cov-6.2.1
collecting ... collected 3 items

routines/tests/test_validate.py::test_valido PASSED                      [ 33%]
routines/tests/test_validate.py::test_invalido PASSED                    [ 66%]
routines/tests/test_validate.py::test_invalido_meio PASSED               [100%]

============================== 3 passed in 0.02s ===============================


=== Executando o Teste test_validate (2) ===
$ python -m pytest -v routines/tests/test_validate.py
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-8.4.1, pluggy-1.6.0 -- /home/emanuelgse/.conda/envs/esbd3_1/bin/python
cachedir: .pytest_cache
rootdir: /home/emanuelgse/ESBD3/esbd3_1
plugins: timeout-2.4.0, cov-6.2.1
collecting ... collected 3 items

routines/tests/test_validate.py::test_valido PASSED                      [ 33%]
routines/tests/test_validate.py::test_invalido PASSED                    [ 66%]
routines/tests/test_validate.py::test_invalido_meio PASSED               [100%]

============================== 3 passed in 0.02s ===============================


=== Medindo a Cobertura - Run ===
$ coverage run -m pytest routines/tests
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-8.4.1, pluggy-1.6.0
rootdir: /home/emanuelgse/ESBD3/esbd3_1
plugins: timeout-2.4.0, cov-6.2.1
collected 17 items

routines/tests/test_parametrized.py .........                            [ 52%]
routines/tests/test_validate.py ...                                      [ 70%]
routines/tests/test_validate_oo.py .....                                 [100%]

============================== 17 passed in 0.08s ==============================


=== Medindo a Cobertura - Report ===
$ coverage report
Name                                  Stmts   Miss  Cover
---------------------------------------------------------
routines/Identifier.py                   26      0   100%
routines/tests/test_parametrized.py      15      0   100%
routines/tests/test_validate.py          10      0   100%
routines/tests/test_validate_oo.py       21      0   100%
---------------------------------------------------------
TOTAL                                    72      0   100%


=== Medindo a Cobertura - HTML ===
$ coverage html -d coverage
Wrote HTML report to coverage/index.html


=== Medindo a Cobertura - Branch ===
$ coverage run --branch -m pytest routines/tests
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-8.4.1, pluggy-1.6.0
rootdir: /home/emanuelgse/ESBD3/esbd3_1
plugins: timeout-2.4.0, cov-6.2.1
collected 17 items

routines/tests/test_parametrized.py .........                            [ 52%]
routines/tests/test_validate.py ...                                      [ 70%]
routines/tests/test_validate_oo.py .....                                 [100%]

============================== 17 passed in 0.08s ==============================

