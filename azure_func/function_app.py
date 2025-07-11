import azure.durable_functions as df
import azure.functions as func

from http_starters.http_start import http_bp
from orchestrator.orchestrator import orch_bp
from activities.activity1 import  act1_bp
from activities.activity2 import  act2_bp

app = df.DFApp(http_auth_level=func.AuthLevel.FUNCTION)
app.register_functions(http_bp)
app.register_functions(orch_bp)
app.register_functions(act1_bp)
app.register_functions(act2_bp)