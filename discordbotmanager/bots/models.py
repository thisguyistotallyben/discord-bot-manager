from django.db import models


class Bot(models.Model):
    name = models.CharField(max_length=200, default='')


class Server(models.Model):
    server_id = models.IntegerField(default=0)
    name = models.CharField(max_length=200, default='')
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)


class Channel(models.Model):
    channel_id = models.IntegerField(default=0)
    name = models.CharField(max_length=200, default='')
    server = models.ForeignKey(Server, on_delete=models.CASCADE)


class Message(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, default='')
    screen_name = models.CharField(max_length=200, default='')
    date = models.DateTimeField('date sent')
    message = models.CharField(max_length=2000, default='')


