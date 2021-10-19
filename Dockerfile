from mcr.microsoft.com/playwright:focal

COPY . .

RUN apt-get update && apt-get install -y python3-pip && pip3 install -r requirements.txt && python -m playwright install

RUN python3 main.py
