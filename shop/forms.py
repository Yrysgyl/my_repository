from django import forms
from shop.models import Category, Product,Comment

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['owner']
        
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CategoryForm, self).__init__(*args, **kwargs)
        
    
    def save(self, commit=True):
        instance = super(CategoryForm, self).save(commit=False)
        if self.user:
            instance.owner = self.user
        if commit:
            instance.save()
        return instance

        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['slug', 'owner']
        
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ProductForm, self).__init__(*args, **kwargs)
    
    def save(self, commit=True):
        instance = super(ProductForm, self).save(commit=False)
        if self.user:
            instance.owner = self.user
        if commit:
            instance.save()
        return instance
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']