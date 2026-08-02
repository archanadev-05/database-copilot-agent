from fastapi import APIRouter
from starlette import status
from starlette.exceptions import HTTPException

from db_agent import query_db_with_natural_language
from resp_models import AgentQueryResponse, AgentQueryRequest

router = APIRouter(prefix='/agent', tags=['Database Agent Routes'])


#Study about - MCP Servers (Model Context Protocol)

@router.post('/query', response_model=AgentQueryResponse)
def query_database_agent(request: AgentQueryRequest) -> AgentQueryResponse:
    try:
        thread_id = request.thread_id
        result = query_db_with_natural_language(user_input=request.query, thread_id=thread_id)
        return AgentQueryResponse(query=request.query, result=result, thread_id=thread_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )



    


