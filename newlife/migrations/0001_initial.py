# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=256, verbose_name="\u0406\u043c'\u044f")),
                ('last_name', models.CharField(max_length=256, verbose_name='\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0435')),
                ('middle_name', models.CharField(default=b'', max_length=256, verbose_name='\u041f\u043e-\u0431\u0430\u0442\u044c\u043a\u043e\u0432\u0456', blank=True)),
                ('birthday', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u0440\u043e\u0434\u0436\u0435\u043d\u043d\u044f')),
                ('photo', models.ImageField(upload_to=b'', null=True, verbose_name='\u0424\u043e\u0442\u043e', blank=True)),
                ('problem', models.CharField(max_length=256, verbose_name='\u041f\u0440\u043e\u0431\u043b\u0435\u043c\u0430')),
                ('notes', models.TextField(verbose_name='\u041d\u043e\u0442\u0430\u0442\u043a\u0438', blank=True)),
            ],
            options={
                'verbose_name': '\u0414\u0438\u0442\u0438\u043d\u0430',
                'verbose_name_plural': '\u0414\u0438\u0442\u0438\u043d\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supporter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=256, verbose_name="\u0406\u043c'\u044f")),
                ('last_name', models.CharField(max_length=256, verbose_name='\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0435')),
                ('middle_name', models.CharField(default=b'', max_length=256, verbose_name='\u041f\u043e-\u0431\u0430\u0442\u044c\u043a\u043e\u0432\u0456', blank=True)),
                ('photo', models.ImageField(upload_to=b'', null=True, verbose_name='\u0424\u043e\u0442\u043e', blank=True)),
                ('country', models.CharField(default=b'', max_length=256, verbose_name='\u041a\u0440\u0430\u0457\u043d\u0430', blank=True)),
                ('notes', models.TextField(verbose_name='\u041d\u043e\u0442\u0430\u0442\u043a\u0438', blank=True)),
                ('child_supporting', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name=b'\xd0\x9f\xd1\x96\xd0\xb4\xd1\x82\xd1\x80\xd0\xb8\xd0\xbc\xd1\x83\xd1\x94', to='newlife.Child', null=True)),
            ],
            options={
                'verbose_name': '\u0421\u043f\u043e\u043d\u0441\u043e\u0440',
                'verbose_name_plural': '\u0421\u043f\u043e\u043d\u0441\u043e\u0440\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='child',
            name='child_supporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name=b'\xd0\xa1\xd0\xbf\xd0\xbe\xd0\xbd\xd1\x81\xd0\xbe\xd1\x80', to='newlife.Supporter', null=True),
            preserve_default=True,
        ),
    ]
