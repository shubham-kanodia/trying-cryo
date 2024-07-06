import os
import cryo
from dotenv import load_dotenv

load_dotenv("../data/.env")

eth_rpc = os.getenv("RPC_ENDPOINT")

END_BLOCK = 59037184
START_BLOCK = END_BLOCK - 10

data = cryo.collect(
    "blocks",
    blocks=[f"{START_BLOCK}:{END_BLOCK}"],
    rpc=eth_rpc,
    output_format="polars",
    hex=True
)

print(data)
