import polars as pl

# Parquet file generated using scripts/save_parquet.py script
df = pl.read_parquet("./data/output/polygon__blocks__59037174_to_59037183.parquet")
print(df)
