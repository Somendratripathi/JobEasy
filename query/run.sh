# create env
conda env create -f environment.yml
# activate env
source activate jobeasy
# sql proxy
./cloud_sql_proxy -instances=jobeasy-columbia:us-central1:trial=tcp:3306