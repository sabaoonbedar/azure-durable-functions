import azure.durable_functions as df

act2_bp = df.Blueprint()

@act2_bp.function_name(name="Activity2")
@act2_bp.activity_trigger(input_name="msg")
def activity2(msg: str) -> str:
    return msg