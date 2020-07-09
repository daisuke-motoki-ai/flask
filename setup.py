""" 
google_calendar python モジュールの初期設定に関するファイル
参考URL 
https://flask.palletsprojects.com/en/1.1.x/patterns/distribute/?highlight=setup%20py
https://qiita.com/knknkn1162/items/d76d03a5245ca42edd7a

"""

from setuptools import setup

setup(
    name='Flask Calendar API',
    version='1.0',
    description="採用管理側と連携するカレンダーAI API",
    author="Daisuke Motoki",
    long_description=__doc__,
    packages=['flaskr'],
    include_package_data=True,
    zip_safe=False,
    install_requires= [
                "Flask==1.1.2",
                'optimize_calendar_events==0.0.0'
            ],
    # # vcs(gitなど)の場合は、必ず、eggを追記する必要がある
    dependency_links = [
    "git+https://daisuke-motoki-ai:57c4b8a37f1aff9f13e00dc851256a072962dbf3@github.com/dai-motoki/calendar.git@master#egg=optimize_calendar_events-0.0.0"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
)