# `Views.py`
```python    
    class InfoRequestCreate(SuccessMessageMixin, generic.CreateView):
        model = models.InfoRequest
        template_name = 'info_request_create.html'
        fields = ['name', 'email', 'cruise', 'notes']
        success_url = reverse_lazy('index')
        success_message = f"Thank you, {name}! We will email you when we have more information about {cruise}"
```