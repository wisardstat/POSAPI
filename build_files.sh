pip3 install -i https://mirrors.aliyun.com/pypi/simple/ -r ./requirements.txt

python uvicorn inventory_app.main:app --reload