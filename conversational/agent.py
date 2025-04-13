"""Agent module for the Insightly agent."""

import logging
import warnings
from google.adk import Agent
from .config import Config
from .prompts import GLOBAL_INSTRUCTION, INSTRUCTION
from conversational.tools.connector import executeQuery

# from .shared_libraries.callbacks import (
#     rate_limit_callback,
#     before_agent,
#     before_tool,
# )
# from .tools.tools import (
#     send_call_companion_link,
#     approve_discount,
#     sync_ask_for_approval,
#     update_salesforce_crm,
#     access_cart_information,
#     modify_cart,
#     get_product_recommendations,
#     check_product_availability,
#     schedule_planting_service,
#     get_available_planting_times,
#     send_care_instructions,
#     generate_qr_code,
# )

warnings.filterwarnings("ignore", category=UserWarning, module=".*pydantic.*")

configs = Config()

# configure logging __name__
logger = logging.getLogger(__name__)


root_agent = Agent(
    model=configs.agent_settings.model,
    global_instruction=GLOBAL_INSTRUCTION,
    instruction=INSTRUCTION,
    name=configs.agent_settings.name,
    tools=[
        executeQuery
    ]
)