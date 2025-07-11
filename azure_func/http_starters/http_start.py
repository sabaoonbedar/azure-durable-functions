import azure.durable_functions as df
import azure.functions as func
import logging
http_bp=df.Blueprint()
# in an HTTP-triggered function:

@http_bp.route(route="HttpStart")
@http_bp.durable_client_input(client_name="client")
async def HttpStart(req: func.HttpRequest, client: df.DurableOrchestrationClient):
    logging.info('the HTTP trigger function was called.')
    instance_id = await client.start_new("Orchestrator", None)
    return client.create_check_status_response(req, instance_id)
