from django.forms import ModelForm
from BoogeyBookAPP.models import BookRead


class BookForm(ModelForm):
    class Meta:
        model = BookRead
        exclude = ('user',)
