# Generated by Django 4.1.7 on 2023-04-05 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '类别信息',
                'verbose_name_plural': '类别信息',
                'db_table': 'db_category',
            },
        ),
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('price', models.IntegerField(verbose_name='价格')),
                ('image', models.ImageField(max_length=300, upload_to='', verbose_name='图片')),
                ('content', models.TextField(verbose_name='介绍')),
                ('number', models.IntegerField(verbose_name='数量')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info_manage.categorymodel', verbose_name='所属分类')),
            ],
            options={
                'verbose_name': '商品信息',
                'verbose_name_plural': '商品信息',
                'db_table': 'db_item',
            },
        ),
        migrations.CreateModel(
            name='UserInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='用户名')),
                ('password', models.CharField(max_length=100, verbose_name='密码')),
                ('money', models.IntegerField(verbose_name='余额')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='加入时间')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'db_user_info',
            },
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='数量')),
                ('price', models.IntegerField(verbose_name='总价格')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info_manage.itemmodel', verbose_name='所属商品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info_manage.userinfomodel', verbose_name='所属用户')),
            ],
            options={
                'verbose_name': '订单信息',
                'verbose_name_plural': '订单信息',
                'db_table': 'db_order',
            },
        ),
        migrations.CreateModel(
            name='HotModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info_manage.itemmodel', verbose_name='热门商品')),
            ],
            options={
                'verbose_name': '热门商品',
                'verbose_name_plural': '热门商品',
                'db_table': 'db_hot',
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='数量')),
                ('price', models.IntegerField(verbose_name='总价格')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('is_pay', models.BooleanField(default=False, verbose_name='是否购买')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info_manage.itemmodel', verbose_name='所属商品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info_manage.userinfomodel', verbose_name='所属用户')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
                'db_table': 'db_car',
            },
        ),
    ]
