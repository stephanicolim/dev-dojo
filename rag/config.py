from dynaconf import Dynaconf, Validator

settings = Dynaconf(
    load_dotenv=True,
    envvar_prefix=False,
)
settings.validators.register(
    Validator("EMBED_MODEL", default="nomic-embed-text", is_type_of=str),
    Validator("CHAT_MODEL", default="llama3.2", is_type_of=str),
    Validator("CHROMA_PATH", must_exist=True, is_type_of=str),
    Validator("DOCS_DIR", must_exist=True, is_type_of=str),
    Validator("DOCS_CATEGORY_NAME", must_exist=True, is_type_of=str),
)
settings.validators.validate()