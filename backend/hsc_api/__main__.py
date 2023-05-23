import uvicorn
from argparse import ArgumentParser


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("host", default="0.0.0.0")
    parser.add_argument("port", default=5055)
    parser.add_argument("reload", action="store_true", default=True)
    args = parser.parse_args()
    uvicorn.run("hsc_api.main:app", host=args.host, port=args.port, log_level="info", reload=args.reload)