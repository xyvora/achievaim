from app.api.deps import CurrentAdminUser, MongoClient, logger
from app.core.config import config
from app.core.utils import APIRouter

router = APIRouter(tags=["Health"], prefix=config.V1_API_PREFIX)


@router.get("/health", include_in_schema=False)
async def health(mongo_client: MongoClient, _: CurrentAdminUser) -> dict[str, str]:
    """Check if the servers are up and running."""
    logger.info("Checking MongoDb health")
    try:
        # motor 3.3.0 broke types see: https://www.mongodb.com/community/forums/t/motor-3-3-0-released/241116
        # and https://jira.mongodb.org/browse/MOTOR-1177
        await mongo_client.server_info()  # type: ignore[attr-defined]
        return {"db": "healthy"}
    except Exception as e:
        logger.error("%s: %s", type(e).__name__, e)
        return {"db": "unhealthy"}
