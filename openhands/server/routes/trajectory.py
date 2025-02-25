from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

from openhands.core.logger import openhands_logger as logger
from openhands.events.serialization import event_to_trajectory
from openhands.events.stream import AsyncEventStreamWrapper

app = APIRouter(prefix='/api/conversations/{conversation_id}')


@app.get('/trajectory')
async def get_trajectory(request: Request):
    """Get trajectory.

    This function retrieves the current trajectory and returns it.

    Args:
        request (Request): The incoming request object.

    Returns:
        JSONResponse: A JSON response containing the trajectory as a list of
        events.
    """
    try:
        filter_hidden = True
        if hasattr(request, 'query_params') and 'filter_hidden' in request.query_params:
            filter_hidden = request.query_params['filter_hidden'].lower() == 'true'

        async_stream = AsyncEventStreamWrapper(
            request.state.conversation.event_stream,
            filter_hidden=filter_hidden,
        )
        trajectory = []
        async for event in async_stream:
            trajectory.append(event_to_trajectory(event))
        return JSONResponse(
            status_code=status.HTTP_200_OK, content={'trajectory': trajectory}
        )
    except Exception as e:
        logger.error(f'Error getting trajectory: {e}', exc_info=True)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                'trajectory': None,
                'error': f'Error getting trajectory: {e}',
            },
        )
