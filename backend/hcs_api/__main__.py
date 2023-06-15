import uvicorn
from argparse import ArgumentParser


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", default=5055)
    parser.add_argument("--reload", action="store_true")
    args = parser.parse_args()
    uvicorn.run("hcs_api.main:app", host=args.host, port=int(args.port), log_level="info", reload=args.reload)