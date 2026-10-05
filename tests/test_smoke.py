def test_smoke():
    from lambdawalker.conda.interface import get_conda_env_location
    assert get_conda_env_location is not None
    print("conda OK")
