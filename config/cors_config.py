from litestar.config.cors import CORSConfig

allowedOrigins = [
    "http://127.0.0.1/:*",
    "http://127.0.0.1:3000",
    'capacitor://localhost',
    'ionic://localhost',
    'http://localhost',
    'http://localhost:8080',
    'http://localhost:8100',
]

cors_config = CORSConfig(allow_origins=allowedOrigins,
                         allow_methods=["*"],
                         allow_headers=["Authorization", "Content-Type"],
                         allow_credentials=True,
                         expose_headers=[],
                         max_age=600)