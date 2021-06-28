from django.db import models
from django.utils.functional import empty


# Overall models
class GameItem(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return str(self.name)


# Quiz models
class QuizQuestion(models.Model):
    game_item_fk = models.ForeignKey(
        GameItem, blank=False, verbose_name='Game item', on_delete=models.CASCADE)
    question = models.CharField(max_length=300, blank=False)
    is_correct = models.BooleanField(verbose_name='True', blank=False)

    def __str__(self) -> str:
        return str(self.game_item_fk)


# Map models
class MapQuestion(models.Model):
    game_item_fk = models.ForeignKey(
        GameItem, blank=False, verbose_name='Game item', on_delete=models.CASCADE)
    statement = models.CharField(max_length=300, blank=False)
    image = models.ImageField(blank=True)
    answers = models.ManyToManyField('MapAnswer', blank=False)
    answer_message = models.CharField(max_length=300, blank=False)

    def __str__(self) -> str:
        return 'Question'


class MapAnswer(models.Model):
    answer = models.CharField(max_length=300, blank=False)
    is_correct = models.BooleanField(blank=False)

    def __str__(self) -> str:
        return str(self.answer)
