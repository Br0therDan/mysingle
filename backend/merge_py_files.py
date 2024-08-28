import os

# .py 파일이 저장된 루트 디렉토리를 지정합니다.
root_directory_path = os.getcwd()
current_directory_name = os.path.basename(root_directory_path)

# 결과를 저장할 파일 경로를 지정합니다.
output_path = "merged_py_files.txt"

# 모든 .py 파일을 재귀적으로 읽어오는 함수입니다.
def get_all_py_files(dir_path):
    py_files = []
    for root, dirs, files in os.walk(dir_path):
        # venv 폴더는 제외합니다.
        dirs[:] = [d for d in dirs if d != '.venv']  # '.venv' 디렉토리를 제외합니다.
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))
    return py_files

# 모든 .py 파일의 경로를 가져옵니다.
py_files = get_all_py_files(root_directory_path)

if not py_files:
    print("No .py files found.")
else:
    print(f"{len(py_files)} .py files found.")

merged_code = ""

# 모든 .py 파일의 내용을 읽어서 하나의 문자열로 합칩니다.
for file in py_files:
    try:
        # 파일 경로를 현재 디렉토리 기준으로 상대 경로로 변환합니다.
        relative_path = os.path.relpath(file, root_directory_path)
        full_path_with_dir = os.path.join(current_directory_name, relative_path)
        print(f"Reading file: {full_path_with_dir}")
        
        with open(file, 'r', encoding='utf-8') as f:
            file_content = f.read()
            # 상대 경로와 현재 디렉토리명을 주석으로 추가합니다.
            file_content_with_path = f"# File: {full_path_with_dir}\n\n{file_content}"  
            merged_code += f"\n\n{file_content_with_path}"  # 파일 내용 추가
    except Exception as e:
        print(f"Error reading file {file}: {e}")

# 합쳐진 코드를 출력 파일에 저장합니다.
try:
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(merged_code)
    print(f"Merged code written to {output_path}")
except Exception as e:
    print(f"Error writing to file {output_path}: {e}")
