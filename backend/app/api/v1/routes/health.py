from app.api.deps import MongoClient, logger
from app.core.config import config
from app.core.utils import APIRouter

router = APIRouter(tags=["Health"], prefix=config.V1_API_PREFIX)


@router.get("/health")
async def health(mongo_client: MongoClient) -> dict[str, str]:
    """Check if the servers are up and running."""
    logger.info("Checking MongoDb health")
    try:
        await mongo_client.server_info()
        return {"db": "healthy"}
    except Exception as e:
        logger.error("%s: %s", type(e).__name__, e)
        return {"db": "unhealthy"}
