from fastapi import APIRouter

#this create a route and add a prefix and a tag
auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get("/")
async def auth(): ##assync é uma função assíncrona que executa sem bloquear o fluxo do programa, permitindo que diversos usuarios façam requisições sem que o sistema trave
    ##essas 3 aspas criam uma nota na documentação automatica do fastapi
    """ 
    endpoint para autenticação de usuarios padrão
    """
    return {"message": "autenticações"}



