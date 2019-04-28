ON DOWNLOAD
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

TO RUN
*in jobeasy/main directory*
./run.sh

TODOs
- make status_dict thread safe to allow concurrency
