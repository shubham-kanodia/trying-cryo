import os
import cryo
from dotenv import load_dotenv

# Using this script you can save the parquet files. You can also run this script on regular intervals to have updated version of the blockchain db
load_dotenv("../data/.env")

eth_rpc = os.getenv("RPC_ENDPOINT")

END_BLOCK = 59037184
START_BLOCK = END_BLOCK - 10

cryo.freeze(
    "blocks",
    blocks=[f"{START_BLOCK}:{END_BLOCK}"],
    rpc=eth_rpc,
    output_dir="../data/output",
    hex=True
)
