import logging

from django.db import DatabaseError, connections
from django.http import JsonResponse
from django.views.decorators.http import require_GET

logger = logging.getLogger(__name__)


@require_GET
def health_check(request):
    """Report application and database availability without exposing configuration."""
    try:
        connections["default"].cursor().close()
    except DatabaseError:
        logger.exception("Health check failed because the database is unavailable.")
        return JsonResponse({"status": "unhealthy", "database": "unavailable"}, status=503)
    return JsonResponse({"status": "healthy", "database": "connected"})
