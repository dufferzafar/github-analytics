import json
import os
import pyspark.sql.types as spark_types
import shutil


def spark_schema_from_json(j):
    return spark_types.StructType([
        spark_types.StructField(
            f["name"],
            spark_types._parse_datatype_string(f.get("type", "string")),
            f.get("nullable", True),
            f.get("metadata", None)
        )
        for f in j
    ])


def load_schema():
    with open("ghtorrent-schema.json") as f:
        db_schema = json.load(f)

    return db_schema


def remove(path):
    if os.path.exists(path):
        shutil.rmtree(path)
