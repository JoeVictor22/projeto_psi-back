from pydantic import BaseModel, constr


class AuthSchema(BaseModel):

    email: constr(min_length=2, max_length=255)
    senha: constr(min_length=4, max_length=255)
