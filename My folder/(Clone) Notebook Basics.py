# Databricks notebook source
print('hello world')

# COMMAND ----------

# MAGIC %sql
# MAGIC select "hello world"

# COMMAND ----------

# MAGIC %md
# MAGIC # Title 1
# MAGIC ## Tittle 2
# MAGIC ### Tittle 3

# COMMAND ----------

# MAGIC %run ./demo/setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')
print(files)

# COMMAND ----------

display(files)

# COMMAND ----------


