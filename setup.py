""" google_calendar python モジュールの初期設定に関するファイル
    参考URL https://flask.palletsprojects.com/en/1.1.x/patterns/distribute/?highlight=setup%20py
"""

from setuptools import setup

def load_requires_from_file(filepath):
    """ パッケージ名だけをリストアップ """
    with open(filepath) as fp:
        return [take_package_name(pkg_name) for pkg_name in fp.readlines()]


def take_package_name(name):
    if name.startswith("-e"):
        return name[name.find("=") + 1 : name.rfind("-")]
    else:
        return name.strip()


def load_links_from_file(filepath):
    """ URL部分はsetup関数のキーワード引数dependency_linkに渡す """
    res = []
    with open(filepath) as fp:
        for pkg_name in fp.readlines():
            if pkg_name.startswith("-e"):
                res.append(pkg_name.split(" ")[1])
    return res

setup(
    name='Flask Calendar API',
    version='1.0',
    description="採用管理側と連携するカレンダーAI API",
    author="Daisuke Motoki",
    long_description=__doc__,
    packages=['flaskr'],
    include_package_data=True,
    zip_safe=False,
    install_requires=load_requires_from_file("requirements.txt"),
    dependency_links=load_links_from_file("requirements.txt"),
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
)