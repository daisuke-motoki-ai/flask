# calendar

## 環境構築

python は3.7.7を利用しています。以下のコマンドでpython 3.7.7 の仮想環境を立ち上げ、requirement.txt fileから必要なpython module をインストールしてください。

```
brew update && brew upgrade pyenv
brew install pyenv
pyenv install 3.7.7
pyenv local 3.7.7
python -m venv venv/flask
source venv/flask/bin/activate
pip install --upgrade pip
python setup.py build
pip install -e .
```




## 開発方法

基本的なコードは src/optimize_calendar_events 内にあります。（最も上位のファイルはこの中の __main__.py です。）

全体のコードを実行する際は python -m optimize_calendar_events とします。

内部の関数が正しく作成されているかのチェックは pytest -v などで確認をしてください。


