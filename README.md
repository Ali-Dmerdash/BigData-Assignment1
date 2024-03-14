docker build -t alidmerdash13/bd-as1 .

docker run -it --name test1 alidmerdash13/bd-as1

touch load.py eda.py dpre.py model.py vis.py

python3 load.py train_titanic.csv

<!-- Because We are on Windows -->
.\final.ps1

<!-- On Ubuntu -->
chmod +x final.sh
./final.sh