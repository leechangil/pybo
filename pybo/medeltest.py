from .models import Question, Answer
from django.utils import timezone
q = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고 싶습니다.', create_date=timezone.now())
q.save()