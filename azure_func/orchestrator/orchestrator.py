import azure.durable_functions as df


orch_bp = df.Blueprint()
@orch_bp.function_name(name="Orchestrator")
@orch_bp.orchestration_trigger(context_name="context")
def orchestrator_function(context: df.DurableOrchestrationContext):
    msg = context.get_input()
    result1 = yield context.call_activity("Activity1", msg)
    result2 = yield context.call_activity("Activity2", result1)
    return result2
