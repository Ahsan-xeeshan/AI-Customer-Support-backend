from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from schemas.models import SupportRequest
from services.llm import stream_support_response

router = APIRouter()


@router.post("/support/stream")
def support_stream(request: SupportRequest):

    try:
        return StreamingResponse(
            stream_support_response(
                request.message,
                request.history
            ),
            media_type="text/plain"
        )
    except Exception as e:
        print("AI Error: ", e)
        raise HTTPException(
            status_code=500,
            detail="AI service temporarily unavailable."
        )