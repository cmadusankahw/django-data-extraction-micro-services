from django.db import models

from configs.constants import *


class Day(models.Model, object):
    timestamp = models.DateTimeField()
    store_id = models.PositiveIntegerField(default=0)
    cust_id = models.PositiveIntegerField(primary_key=True, default=0)
    prod_name = models.CharField(max_length=20)
    sales_channel = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=4)
    sale_val = models.DecimalField(default=0.0, decimal_places=8, max_digits=12)

    class Meta:
        db_table = day_view
        unique_together = (('store_id', 'cust_id'),)


class Month(models.Model, object):
    timestamp = models.DateTimeField()
    store_id = models.PositiveIntegerField(default=0)
    cust_id = models.PositiveIntegerField(primary_key=True, default=0)
    prod_name = models.CharField(max_length=20)
    sales_channel = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=4)
    sale_val = models.DecimalField(default=0.0, decimal_places=8, max_digits=12)

    class Meta:
        db_table = month_view
        unique_together = (('store_id', 'cust_id'),)


class MySQLOfferTable(models.Model, object):
    offer_id = models.PositiveBigIntegerField(primary_key=True, default=0)
    churn_level = models.TextField()
    recency_category = models.TextField()
    monetary_category = models.TextField()
    frequency_category = models.TextField()
    offer_name = models.TextField()

    class Meta:
        db_table = mysql_offer_table


class DummyInsightsMonthly(models.Model, object):
    timestamp = models.DateTimeField()
    store_id = models.PositiveIntegerField(default=0)
    cust_id = models.PositiveIntegerField(primary_key=True, default=0)
    prod_name = models.CharField(max_length=20)
    sales_channel = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=4)
    sale_val = models.DecimalField(default=0.0, decimal_places=8, max_digits=12)

    class Meta:
        db_table = rac_fnb_dummy_insights_monthly_table
        unique_together = (('store_id', 'cust_id'),)


class DummyInsightsViewMapping(models.Model, object):
    id = models.PositiveIntegerField(primary_key=True, default=0)
    table_name = models.CharField(max_length=45)
    view_name = models.CharField(max_length=45)

    class Meta:
        db_table = rac_fnb_dummy_insights_view_mapping_table


class WLutTblViewMapping(models.Model, object):
    id = models.PositiveIntegerField(primary_key=True, default=0)
    table_name = models.CharField(max_length=45)
    view_name = models.CharField(max_length=45)

    class Meta:
        db_table = w_lut_tbl_view_mapping_table


class WLutTblRetStore(models.Model, object):
    ret_store = models.CharField(primary_key=True, max_length=255)

    class Meta:
        db_table = w_lut_tbl_ret_store_table


class WLutTblDepartment(models.Model, object):
    department = models.CharField(primary_key=True, max_length=255)

    class Meta:
        db_table = w_lut_tbl_department_table


class WLutTblProdType(models.Model, object):
    prod_type = models.CharField(primary_key=True, max_length=255)

    class Meta:
        db_table = w_lut_tbl_prod_type_table


class WLutTblBrand(models.Model, object):
    brand = models.CharField(primary_key=True, max_length=255)

    class Meta:
        db_table = w_lut_tbl_brand_table