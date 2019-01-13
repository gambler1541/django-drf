from django.conf import settings
from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter

from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# [
# ('python', 'Python'),
# ('rb', 'Ruby'),
# ]
# 튜플의 0번째 값이 db에 저장, 1번째 값이 사용자에게 보여짐
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
# 테마

class Snippets(models.Model):
    # 작성자
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              )
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    # code를 syntax-highlight시킨 HTML코드가 저장될 필
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)


    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)

        linenos = 'table' if self.linenos else False
        option = {'title' : self.title} if self.title else {}

        #
        # linenos = self.linenos and 'table' or False
        # option = self.title and {'title':self.title} or {}

        formatter = HtmlFormatter(
            style=self.style,
            linenos=linenos,
            full=True,
            **option,
        )
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)