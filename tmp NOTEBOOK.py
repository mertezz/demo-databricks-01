# Databricks notebook source
dbutils.widgets.combobox(name='fruits', defaultValue='apple', choices=['apple', 'banana', 'orange'])

# COMMAND ----------

print(f"Selected combobox value: {dbutils.widgets.get('fruits')}")
