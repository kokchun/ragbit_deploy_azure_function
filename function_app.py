import azure.functions as func
import api

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="{*route}", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
async def fastapi_proxy(
    req: func.HttpRequest, context: func.Context
) -> func.HttpResponse:
    return await func.AsgiMiddleware(api.app).handle_async(req, context)
