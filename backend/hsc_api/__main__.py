import uvicorn

if __name__ == "__main__":
    uvicorn.run("hsc_api.main:app", host="0.0.0.0", port=5055, log_level="info", reload=True)