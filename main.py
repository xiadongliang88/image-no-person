import conf
import subprocess


scheme = conf.scheme


def run_script(script_name):
    try:
        subprocess.run(['python', script_name], check=True)
        print(f"{script_name} success！")

    except subprocess.CalledProcessError as e:
        print(f'Run {script_name} error: {e}')

    except FileNotFoundError:
        print(f'Can not found: {script_name}')


if __name__ == '__main__':
    if scheme == 'A':
        run_script("schemeA.py")

    elif scheme == 'B':
        run_script("schemeB.py")

    else:
        print('请检查配置文件conf.py中的scheme字段')