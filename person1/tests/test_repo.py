import os
def test_repo_has_python_files():
    # проверим, что ключевые файлы/папки из репо на месте
    assert os.path.exists("writer.py")
    assert os.path.exists("person1")
