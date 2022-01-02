from fastapi import FastAPI

app=FastAPI()


@app.get('/')
def test():
    return{'details:' "this is a test"}