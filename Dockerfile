FROM python:3.11.3

WORKDIR /app

COPY . .

RUN pip install -U pip && pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["src/app/app.py"]