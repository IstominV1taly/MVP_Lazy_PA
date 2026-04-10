from app.config import PROJECT_ROOT, RAW_DATA_FILE # import of the root and input file paths from the config file

def test_project_root_is_exist(): # root dir is exist and its a directory
    assert PROJECT_ROOT.exists()
    assert PROJECT_ROOT.is_dir()

def test_raw_data_file_is_exist(): # raw data file is exist and its a file
    assert RAW_DATA_FILE.exists()
    assert RAW_DATA_FILE.is_file()