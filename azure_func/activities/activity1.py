import azure.durable_functions as df

act1_bp = df.Blueprint()
@act1_bp.activity_trigger(input_name="msg")
def activity1(msg: str) -> str:
    return msg