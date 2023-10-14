from litestar import Litestar
from controllers.llm_controller import LLMController
from config.cors_config import cors_config

if __name__ == "__main__":
    app = Litestar(route_handlers=[LLMController], cors_config=cors_config)
