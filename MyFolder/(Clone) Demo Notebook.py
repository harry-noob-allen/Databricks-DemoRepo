# Databricks notebook source
print ("Hello World")

# COMMAND ----------

# MAGIC %sql
# MAGIC select "1"

# COMMAND ----------

# MAGIC %md
# MAGIC Hi
# MAGIC What
# MAGIC ## Yiu
# MAGIC ### YIUUU
# MAGIC
# MAGIC 1. Yes
# MAGIC 2. No

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

fs = dbutils.fs.ls('/databricks-datasets/')
display(fs)
