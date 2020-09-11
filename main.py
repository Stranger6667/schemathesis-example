from app.settings import load_config
from app.app import create_app


def main(config_path, port):
    config = load_config(config_path)
    app = create_app(config)
    app.run(port)


if __name__ == "__main__":
    main("config.json", port=5000)
